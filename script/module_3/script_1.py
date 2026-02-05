import polars as pl
import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import brentq
from pathlib import Path

# Sample data structure
df = pl.DataFrame({
    'ticker': ['AAPL', 'MSFT', 'GOOGL'],
    'price': [150.0, 300.0, 100.0],
    'book_value': [50.0, 80.0, 60.0],
    'E1': [10.0, 20.0, 8.0],
    'E2': [11.0, 22.0, 9.0],
    'E3': [12.0, 24.0, 10.0],
    'payout_ratio': [0.25, 0.30, 0.0],  # dividend / earnings
})

def compute_future_book_values(
    B0: float,
    earnings: list[float],
    payout_ratio: float
) -> list[float]:
    """
    Compute future book values using clean surplus.
    
    B_t = B_{t-1} + E_t - D_t
    
    Parameters
    ----------
    B0 : float
        Current book value
    earnings : list[float]
        Forecasted earnings [E1, E2, ..., ET]
    payout_ratio : float
        Dividend payout ratio (dividends / earnings)
    
    Returns
    -------
    list[float]
        Book values [B0, B1, B2, ..., BT]
    """
    book_values = [B0]
    
    for E_t in earnings:
        D_t = E_t * payout_ratio
        B_t = book_values[-1] + E_t - D_t
        book_values.append(B_t)
    
    return book_values

def compute_residual_income(
    earnings: list[float],
    book_values: list[float],
    r: float
) -> list[float]:
    """
    Compute residual income for each forecast period.
    
    RI_t = E_t - r * B_{t-1}
    
    Parameters
    ----------
    earnings : list[float]
        Forecasted earnings [E1, E2, ..., ET]
    book_values : list[float]
        Book values [B0, B1, ..., BT]
    r : float
        Discount rate (trial value when solving for ICC)
    
    Returns
    -------
    list[float]
        Residual income for each period
    """
    RI = []
    
    for t, E_t in enumerate(earnings, start=1):
        B_prev = book_values[t - 1]
        RI_t = E_t - r * B_prev
        RI.append(RI_t)
    
    return RI

def rim_price(
    B0: float,
    earnings: list[float],
    book_values: list[float],
    r: float,
    g: float
) -> float:
    """
    Compute price using the two-stage residual income model.
    
    P = B0 + sum(RI_t / (1+r)^t) + TV
    
    where TV = RI_T * (1+g) / [(r-g) * (1+r)^T]
    
    Parameters
    ----------
    B0 : float
        Current book value
    earnings : list[float]
        Forecasted earnings
    book_values : list[float]
        Projected book values
    r : float
        Discount rate
    g : float
        Terminal growth rate
    
    Returns
    -------
    float
        Model-implied price
    """
    if r <= g:
        return float('inf')  # Invalid: discount rate must exceed growth
    
    # Compute residual income
    RI = compute_residual_income(earnings, book_values, r)
    
    T = len(RI)
    
    # Present value of explicit forecast period
    pv_ri = sum(RI[t-1] / (1 + r)**t for t in range(1, T + 1))
    
    # Terminal value
    RI_T = RI[-1]
    TV = (RI_T * (1 + g)) / ((r - g) * (1 + r)**T)
    
    # Total value
    price = B0 + pv_ri + TV
    
    return price


def solve_rim_icc(
    P0: float,
    B0: float,
    earnings: list[float],
    payout_ratio: float,
    g: float,
    r_min: float = 0.01,
    r_max: float = 0.50
) -> float:
    """
    Solve for ICC using the residual income model.
    
    Uses Brent's method - robust and reliable.
    """
    book_values = compute_future_book_values(B0, earnings, payout_ratio)
    
    def objective(r):
        return rim_price(B0, earnings, book_values, r, g) - P0
    
    try:
        f_min = objective(r_min)
        f_max = objective(r_max)
        
        if f_min * f_max > 0:
            return float('nan')
        
        icc = brentq(objective, r_min, r_max, xtol=1e-6)
        return icc
    
    except (ValueError, RuntimeError):
        return float('nan')


# =============================================================================
# VISUALIZATION 1: Clean Surplus Accounting Table (Example Company)
# =============================================================================

def create_clean_surplus_table(ticker: str, df: pl.DataFrame) -> pl.DataFrame:
    """
    Create a detailed table showing clean surplus accounting step by step.
    """
    row = df.filter(pl.col('ticker') == ticker).row(0, named=True)
    
    B0 = row['book_value']
    earnings = [row['E1'], row['E2'], row['E3']]
    payout_ratio = row['payout_ratio']
    
    years = ['Year 0', 'Year 1', 'Year 2', 'Year 3']
    book_vals = [B0]
    earning_vals = [None] + earnings
    dividend_vals = [None]
    retained_vals = [None]
    
    for E_t in earnings:
        D_t = E_t * payout_ratio
        retention = E_t - D_t
        B_t = book_vals[-1] + retention
        
        dividend_vals.append(D_t)
        retained_vals.append(retention)
        book_vals.append(B_t)
    
    table = pl.DataFrame({
        'Period': years,
        'Book Value': [f'${x:.2f}' for x in book_vals],
        'Earnings': ['-' if x is None else f'${x:.2f}' for x in earning_vals],
        'Dividends': ['-' if x is None else f'${x:.2f}' for x in dividend_vals],
        'Retained': ['-' if x is None else f'${x:.2f}' for x in retained_vals],
    })
    
    return table


# =============================================================================
# CHART 1: General Principle - How Model Price Responds to Discount Rate
# =============================================================================

def plot_general_price_sensitivity(df: pl.DataFrame, g: float = 0.03):
    """
    Show the general relationship: how RIM price varies with discount rate.
    Demonstrates the monotonic relationship and root-finding concept.
    """
    # Use first company as example
    row = df.row(0, named=True)
    ticker = row['ticker']
    P0 = row['price']
    B0 = row['book_value']
    earnings = [row['E1'], row['E2'], row['E3']]
    payout_ratio = row['payout_ratio']
    
    book_values = compute_future_book_values(B0, earnings, payout_ratio)
    icc = solve_rim_icc(P0, B0, earnings, payout_ratio, g)
    
    # Generate range of discount rates
    r_range = np.linspace(g + 0.01, 0.30, 100)
    prices = [rim_price(B0, earnings, book_values, r, g) for r in r_range]
    
    # Plot - clean Cochrane style
    fig, ax = plt.subplots(figsize=(9, 6))
    ax.plot(r_range * 100, prices, 'k-', linewidth=2, label='Model price')
    ax.axhline(y=P0, color='gray', linestyle='--', linewidth=1.5, label='Market price')
    
    if not np.isnan(icc):
        ax.axvline(x=icc * 100, color='gray', linestyle=':', linewidth=1.5)
        ax.plot(icc * 100, P0, 'ko', markersize=8, zorder=5)
        ax.text(icc * 100 + 1, P0 + 10, f'ICC = {icc*100:.1f}%', fontsize=10)
    
    ax.set_xlabel('Discount rate (%)', fontsize=11)
    ax.set_ylabel('Price ($)', fontsize=11)
    ax.set_title('Model price decreases with discount rate', fontsize=12, pad=15)
    ax.legend(fontsize=10, frameon=False)
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.grid(True, alpha=0.2, linestyle='-', linewidth=0.5)
    
    plt.tight_layout()
    return fig


# =============================================================================
# CHART 2: ICC Sensitivity Comparison Across Firms
# =============================================================================

def plot_icc_sensitivity_comparison(df: pl.DataFrame):
    """
    Compare ICC sensitivity to terminal growth across all firms.
    Shows which firms are more sensitive to growth assumptions.
    """
    fig, ax = plt.subplots(figsize=(9, 6))
    
    g_range = np.linspace(0.00, 0.06, 30)
    colors = ['black', 'darkgray', 'gray']
    linestyles = ['-', '--', ':']
    
    for idx, row in enumerate(df.iter_rows(named=True)):
        ticker = row['ticker']
        P0 = row['price']
        B0 = row['book_value']
        earnings = [row['E1'], row['E2'], row['E3']]
        payout_ratio = row['payout_ratio']
        
        iccs = []
        for g in g_range:
            icc = solve_rim_icc(P0, B0, earnings, payout_ratio, g)
            iccs.append(icc * 100 if not np.isnan(icc) else None)
        
        # Filter out None values
        valid_points = [(g, icc) for g, icc in zip(g_range, iccs) if icc is not None]
        if valid_points:
            g_vals, icc_vals = zip(*valid_points)
            ax.plot(np.array(g_vals) * 100, icc_vals, 
                   color=colors[idx], linewidth=2, label=ticker,
                   linestyle=linestyles[idx])
    
    # Highlight standard assumption
    ax.axvline(x=3.0, color='lightgray', linestyle='-', linewidth=1)
    ax.text(3.05, ax.get_ylim()[0] + 0.5, 'g = 3%', fontsize=9, color='gray')
    
    ax.set_xlabel('Terminal growth rate (%)', fontsize=11)
    ax.set_ylabel('Implied cost of capital (%)', fontsize=11)
    ax.set_title('ICC sensitivity to terminal growth assumption', fontsize=12, pad=15)
    ax.legend(fontsize=10, frameon=False, loc='upper right')
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.grid(True, alpha=0.2, linestyle='-', linewidth=0.5)
    
    plt.tight_layout()
    return fig


# =============================================================================
# CHART 3: Value Decomposition - All Firms Compared
# =============================================================================

def plot_value_decomposition_comparison(df: pl.DataFrame, g: float = 0.03):
    """
    Compare value decomposition across all firms.
    Shows how much of value comes from book, near-term RI, and terminal value.
    """
    fig, ax = plt.subplots(1, 1, figsize=(9, 6))
    
    tickers = []
    book_values = []
    pv_ri_values = []
    tv_values = []
    iccs = []
    
    for row in df.iter_rows(named=True):
        ticker = row['ticker']
        P0 = row['price']
        B0 = row['book_value']
        earnings = [row['E1'], row['E2'], row['E3']]
        payout_ratio = row['payout_ratio']
        
        book_vals = compute_future_book_values(B0, earnings, payout_ratio)
        icc = solve_rim_icc(P0, B0, earnings, payout_ratio, g)
        
        if not np.isnan(icc):
            RI = compute_residual_income(earnings, book_vals, icc)
            T = len(RI)
            pv_ri = sum(RI[t-1] / (1 + icc)**t for t in range(1, T + 1))
            TV = (RI[-1] * (1 + g)) / ((icc - g) * (1 + icc)**T)
            
            tickers.append(ticker)
            book_values.append(B0)
            pv_ri_values.append(pv_ri)
            tv_values.append(TV)
            iccs.append(icc)
    
    # Simple stacked bar chart
    x = np.arange(len(tickers))
    width = 0.6
    
    colors = ['white', 'lightgray', 'darkgray']
    edgecolor = 'black'
    
    ax.bar(x, book_values, width, label='Book value', color=colors[0], 
           edgecolor=edgecolor, linewidth=1.5)
    ax.bar(x, pv_ri_values, width, bottom=book_values, 
           label='PV(RI)', color=colors[1], edgecolor=edgecolor, linewidth=1.5)
    ax.bar(x, tv_values, width, 
           bottom=np.array(book_values) + np.array(pv_ri_values),
           label='Terminal value', color=colors[2], edgecolor=edgecolor, linewidth=1.5)
    
    ax.set_ylabel('Value ($)', fontsize=11)
    ax.set_title('Value decomposition: book value, residual income, terminal value', 
                 fontsize=12, pad=15)
    ax.set_xticks(x)
    ax.set_xticklabels(tickers, fontsize=10)
    ax.legend(fontsize=10, frameon=False, loc='upper left')
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.grid(True, alpha=0.2, axis='y', linestyle='-', linewidth=0.5)
    
    plt.tight_layout()
    return fig


# =============================================================================
# CHART 4: Residual Income Evolution - Example Company
# =============================================================================

def plot_residual_income_example(ticker: str, df: pl.DataFrame, g: float = 0.03):
    """
    Show residual income evolution for one example company.
    Demonstrates how RI depends on the discount rate assumption.
    """
    row = df.filter(pl.col('ticker') == ticker).row(0, named=True)
    
    B0 = row['book_value']
    P0 = row['price']
    earnings = [row['E1'], row['E2'], row['E3']]
    payout_ratio = row['payout_ratio']
    
    book_values = compute_future_book_values(B0, earnings, payout_ratio)
    icc = solve_rim_icc(P0, B0, earnings, payout_ratio, g)
    
    # Compare different scenarios
    scenarios = [
        (f'r = {icc*100:.1f}% (ICC)', icc if not np.isnan(icc) else 0.10, 'black', '-'),
        ('r = 6%', 0.06, 'darkgray', '--'),
        ('r = 15%', 0.15, 'gray', ':')
    ]
    
    fig, ax = plt.subplots(figsize=(9, 6))
    
    years = range(1, len(earnings) + 1)
    
    for label, r, color, ls in scenarios:
        RI = compute_residual_income(earnings, book_values, r)
        ax.plot(years, RI, linewidth=2, label=label, color=color, linestyle=ls)
    
    # Add zero line
    ax.axhline(y=0, color='lightgray', linestyle='-', linewidth=1)
    
    ax.set_xlabel('Year', fontsize=11)
    ax.set_ylabel('Residual income ($)', fontsize=11)
    ax.set_title(f'Residual income over time: {ticker}', fontsize=12, pad=15)
    ax.legend(fontsize=10, frameon=False, loc='best')
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.grid(True, alpha=0.2, linestyle='-', linewidth=0.5)
    ax.set_xticks(years)
    
    plt.tight_layout()
    return fig


# =============================================================================
# VISUALIZATION 6: Summary Table with ICC Estimates
# =============================================================================

def create_icc_summary_table(df: pl.DataFrame, g: float = 0.03) -> pl.DataFrame:
    """
    Compute ICC for all firms and create summary table.
    """
    results = []
    
    for row in df.iter_rows(named=True):
        ticker = row['ticker']
        P0 = row['price']
        B0 = row['book_value']
        earnings = [row['E1'], row['E2'], row['E3']]
        payout_ratio = row['payout_ratio']
        
        icc = solve_rim_icc(P0, B0, earnings, payout_ratio, g)
        
        # Compute value components
        if not np.isnan(icc):
            book_values = compute_future_book_values(B0, earnings, payout_ratio)
            RI = compute_residual_income(earnings, book_values, icc)
            T = len(RI)
            pv_ri = sum(RI[t-1] / (1 + icc)**t for t in range(1, T + 1))
            TV = (RI[-1] * (1 + g)) / ((icc - g) * (1 + icc)**T)
            model_price = B0 + pv_ri + TV
        else:
            model_price = None
        
        results.append({
            'Ticker': ticker,
            'Market Price': f'${P0:.2f}',
            'Book Value': f'${B0:.2f}',
            'ICC (%)': f'{icc*100:.2f}' if not np.isnan(icc) else 'N/A',
            'Model Price': f'${model_price:.2f}' if model_price else 'N/A',
            'P/B Ratio': f'{P0/B0:.2f}',
        })
    
    return pl.DataFrame(results)


# =============================================================================
# MAIN EXECUTION
# =============================================================================

if __name__ == '__main__':
    print("=" * 80)
    print("RESIDUAL INCOME MODEL (RIM) - TUTORIAL VISUALIZATIONS")
    print("=" * 80)
    print()
    
    # Sample data for three firms
    data = {
        'ticker': ['AAPL', 'MSFT', 'GOOGL'],
        'price': [150.0, 300.0, 100.0],
        'book_value': [50.0, 80.0, 60.0],
        'E1': [10.0, 20.0, 12.0],
        'E2': [11.0, 22.0, 13.0],
        'E3': [12.0, 24.0, 14.0],
        'payout_ratio': [0.3, 0.4, 0.2],
    }
    
    df = pl.DataFrame(data)
    g = 0.03  # Terminal growth = 3% (inflation)
    
    # =========================================================================
    # TABLE 1: Clean Surplus Accounting Example (One Company)
    # =========================================================================
    print("\n" + "=" * 80)
    print("TABLE 1: Clean Surplus Accounting Example (AAPL)")
    print("=" * 80)
    table = create_clean_surplus_table('AAPL', df)
    print(table)
    print("\nNote: Book Value evolves as B_t = B_{t-1} + Earnings - Dividends")
    
    # =========================================================================
    # TABLE 2: ICC Summary for All Firms
    # =========================================================================
    print("\n" + "=" * 80)
    print("TABLE 2: ICC Estimates Summary (All Firms)")
    print("=" * 80)
    summary = create_icc_summary_table(df, g)
    print(summary)
    
    # =========================================================================
    # CHARTS: Generate Consolidated Visualizations
    # =========================================================================
    print("\n" + "=" * 80)
    print("GENERATING CHARTS...")
    print("=" * 80)
    
    output_dir = Path(".")
    
    # Chart 1: General Principle - Price Sensitivity (using one example)
    print("\n1. General principle: Price vs. discount rate...")
    fig = plot_general_price_sensitivity(df, g)
    fig.savefig(output_dir / "rim_general_price_sensitivity.png", dpi=300, bbox_inches='tight')
    plt.close(fig)
    
    # Chart 2: ICC Sensitivity Comparison (all firms)
    print("2. ICC sensitivity comparison across firms...")
    fig = plot_icc_sensitivity_comparison(df)
    fig.savefig(output_dir / "rim_icc_sensitivity_comparison.png", dpi=300, bbox_inches='tight')
    plt.close(fig)
    
    # Chart 3: Value Decomposition Comparison (all firms)
    print("3. Value decomposition comparison...")
    fig = plot_value_decomposition_comparison(df, g)
    fig.savefig(output_dir / "rim_value_decomposition_comparison.png", dpi=300, bbox_inches='tight')
    plt.close(fig)
    
    # Chart 4: Residual Income Example (one company)
    print("4. Residual income example (AAPL)...")
    fig = plot_residual_income_example('AAPL', df, g)
    fig.savefig(output_dir / "rim_residual_income_example.png", dpi=300, bbox_inches='tight')
    plt.close(fig)
    
    print("\n" + "=" * 80)
    print("✓ COMPLETE! All charts generated successfully!")
    print("=" * 80)
    print("\nOutput Summary:")
    print("  • 2 Tables: Clean surplus example + ICC summary")
    print("  • 4 Charts:")
    print("    1. rim_general_price_sensitivity.png (concept)")
    print("    2. rim_icc_sensitivity_comparison.png (all firms)")
    print("    3. rim_value_decomposition_comparison.png (all firms)")
    print("    4. rim_residual_income_example.png (AAPL example)")
    print("=" * 80)