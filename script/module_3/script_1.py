import polars as pl

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