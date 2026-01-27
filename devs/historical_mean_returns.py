import polars as pl 
import yfinance as yf
import matplotlib.pyplot as plt
import numpy as np

# Download AAPL price data
ticker = yf.Ticker("AAPL")
prices = ticker.history(period="10y")  # Last 10 years of data

# Convert to Polars DataFrame
df = pl.DataFrame({
    'date': prices.index,
    'price': prices['Close'].values
})

# Compute returns
df = (df.with_columns([
    (pl.col('price') / pl.col('price').shift(1) - 1).alias('return')
    ])
    .drop_nulls()
)
# # Remove first row (NaN return)
# df = df.filter(pl.col('return').is_not_null())

# # Print summary statistics
# print(f"Mean return: {df['return'].mean():.4f}")
# print(f"Std dev: {df['return'].std():.4f}")
# print(f"Min return: {df['return'].min():.4f}")
# print(f"Max return: {df['return'].max():.4f}")

# # Plot distribution of returns
# fig, axes = plt.subplots(1, 2, figsize=(14, 5))

# # Histogram
# axes[0].hist(df['return'].to_numpy(), bins=50, edgecolor='black', alpha=0.7)
# axes[0].axvline(df['return'].mean(), color='red', linestyle='--', linewidth=2, label=f'Mean: {df["return"].mean():.4f}')
# axes[0].set_xlabel('Daily Return')
# axes[0].set_ylabel('Frequency')
# axes[0].set_title('Distribution of AAPL Daily Returns')
# axes[0].legend()
# axes[0].grid(True, alpha=0.3)

# # Time series of returns
# axes[1].plot(df['date'].to_numpy(), df['return'].to_numpy(), linewidth=0.8, alpha=0.7)
# axes[1].axhline(0, color='black', linestyle='-', linewidth=0.5)
# axes[1].axhline(df['return'].mean(), color='red', linestyle='--', linewidth=2, label=f'Mean: {df["return"].mean():.4f}')
# axes[1].set_xlabel('Date')
# axes[1].set_ylabel('Daily Return')
# axes[1].set_title('AAPL Daily Returns Over Time')
# axes[1].legend()
# axes[1].grid(True, alpha=0.3)

# plt.tight_layout()
# plt.savefig('../docs/modules/figures/module1/aapl_returns_distribution.png', dpi=300, bbox_inches='tight')
# plt.show()


# # Demonstrate instability of historical mean estimates
# print("\n" + "="*60)
# print("INSTABILITY OF HISTORICAL MEAN RETURNS")
# print("="*60)

# # Compute rolling mean returns with different window sizes
# window_sizes = [60, 126, 252, 504]  # ~3 months, 6 months, 1 year, 2 years (trading days)

# df_rolling = df.select(['date', 'return'])

# for window in window_sizes:
#     df_rolling = df_rolling.with_columns([
#         pl.col('return').rolling_mean(window_size=window).alias(f'mean_{window}d')
#     ])

# # Annualize the rolling means (assuming 252 trading days per year)
# for window in window_sizes:
#     df_rolling = df_rolling.with_columns([
#         (pl.col(f'mean_{window}d') * 252).alias(f'annual_{window}d')
#     ])

# # Plot rolling mean estimates
# fig, axes = plt.subplots(2, 1, figsize=(14, 10))

# # Panel 1: Rolling mean estimates over time
# for window in window_sizes:
#     axes[0].plot(df_rolling['date'].to_numpy(), 
#                 df_rolling[f'annual_{window}d'].to_numpy(),
#                 label=f'{window} days (~{window//252} yr)' if window >= 252 else f'{window} days',
#                 alpha=0.7, linewidth=1.5)

# axes[0].axhline(df['return'].mean() * 252, color='black', linestyle='--', 
#                linewidth=2, label='Full sample mean')
# axes[0].set_xlabel('Date')
# axes[0].set_ylabel('Annualized Expected Return')
# axes[0].set_title('Rolling Mean Return Estimates: High Time Variation')
# axes[0].legend(loc='best')
# axes[0].grid(True, alpha=0.3)

# # Panel 2: Distribution of rolling mean estimates
# data_for_box = []
# labels_for_box = []

# for window in window_sizes:
#     valid_estimates = df_rolling[f'annual_{window}d'].drop_nulls().to_numpy()
#     data_for_box.append(valid_estimates)
#     labels_for_box.append(f'{window}d')

# bp = axes[1].boxplot(data_for_box, labels=labels_for_box, patch_artist=True)
# for patch in bp['boxes']:
#     patch.set_facecolor('lightblue')
#     patch.set_alpha(0.7)

# axes[1].axhline(df['return'].mean() * 252, color='red', linestyle='--', 
#                linewidth=2, label='Full sample mean')
# axes[1].set_xlabel('Rolling Window Size')
# axes[1].set_ylabel('Annualized Expected Return')
# axes[1].set_title('Distribution of Rolling Mean Estimates: Wide Dispersion')
# axes[1].legend()
# axes[1].grid(True, alpha=0.3, axis='y')

# plt.tight_layout()
# plt.savefig('../docs/modules/figures/module1/aapl_rolling_mean_estimates.png', dpi=300, bbox_inches='tight')
# plt.show()

# # Compute standard deviation of rolling estimates
# print("\nStandard Deviation of Rolling Mean Estimates (Annualized):")
# for window in window_sizes:
#     std_estimate = df_rolling[f'annual_{window}d'].drop_nulls().std()
#     print(f"  {window:4d} days: {std_estimate:.4f} ({std_estimate*100:.2f}%)")

# # Show how estimates change with sample period
# print("\nExpected Return Estimates by Sub-Period:")
# periods = [
#     ("Full sample", df['date'].min(), df['date'].max()),
#     ("First half", df['date'].min(), df['date'].quantile(0.5)),
#     ("Second half", df['date'].quantile(0.5), df['date'].max()),
#     ("Last 2 years", df['date'].max() - pl.duration(days=504), df['date'].max()),
# ]

# for period_name, start, end in periods:
#     period_df = df.filter((pl.col('date') >= start) & (pl.col('date') <= end))
#     mean_ret = period_df['return'].mean() * 252
#     std_ret = period_df['return'].std() * np.sqrt(252)
#     n_obs = len(period_df)
#     se = std_ret / np.sqrt(n_obs)
    
#     print(f"\n{period_name}:")
#     print(f"  Mean: {mean_ret:.4f} ({mean_ret*100:.2f}%)")
#     print(f"  Std Error: {se:.4f} ({se*100:.2f}%)")
#     print(f"  95% CI: [{(mean_ret - 1.96*se)*100:.2f}%, {(mean_ret + 1.96*se)*100:.2f}%]")
#     print(f"  N observations: {n_obs}")

# # New analysis 1: Show relationship between window size and estimate stability
# print("\n" + "="*60)
# print("ESTIMATION STABILITY VS WINDOW SIZE")
# print("="*60)

# # Compute variability metrics for different window sizes
# stability_results = []
# window_range = [20, 40, 60, 126, 252, 504, 756]  # From 1 month to 3 years

# for window in window_range:
#     rolling_mean = df['return'].rolling_mean(window_size=window)
#     rolling_mean_annualized = rolling_mean * 252
    
#     # Remove nulls and compute standard deviation
#     valid_estimates = rolling_mean_annualized.drop_nulls()
#     std_of_estimates = valid_estimates.std()
#     range_of_estimates = valid_estimates.max() - valid_estimates.min()
    
#     stability_results.append({
#         'window': window,
#         'window_years': window / 252,
#         'std': std_of_estimates,
#         'range': range_of_estimates,
#         'n_estimates': len(valid_estimates)
#     })
    
#     print(f"\nWindow: {window:4d} days ({window/252:.2f} years)")
#     print(f"  Std of estimates: {std_of_estimates:.4f} ({std_of_estimates*100:.2f}%)")
#     print(f"  Range: {range_of_estimates:.4f} ({range_of_estimates*100:.2f}%)")


# # New analysis 2: Annual average returns to show time variation
# print("\n" + "="*60)
# print("ANNUAL AVERAGE RETURNS: TIME VARIATION")
# print("="*60)

# # Extract year from date and compute annual averages
# df_annual = df.with_columns([
#     pl.col('date').dt.year().alias('year')
# ])

# annual_stats = df_annual.group_by('year').agg([
#     pl.col('return').mean().alias('mean_return'),
#     pl.col('return').std().alias('std_return'),
#     pl.col('return').count().alias('n_obs')
# ]).sort('year')

# # Annualize the returns
# annual_stats = annual_stats.with_columns([
#     (pl.col('mean_return') * 252).alias('annual_return'),
#     (pl.col('std_return') * np.sqrt(252)).alias('annual_volatility')
# ])

# print("\nAnnual Average Returns:")
# print(annual_stats)

# # Plot annual returns
# fig, axes = plt.subplots(2, 1, figsize=(14, 10))

# # Panel 1: Bar chart of annual returns
# years = annual_stats['year'].to_numpy()
# returns = annual_stats['annual_return'].to_numpy()
# colors = ['green' if r > 0 else 'red' for r in returns]

# axes[0].bar(years, returns, color=colors, alpha=0.7, edgecolor='black')
# axes[0].axhline(df['return'].mean() * 252, color='blue', linestyle='--', 
#                linewidth=2, label=f'Full sample mean: {df["return"].mean()*252:.2%}')
# axes[0].axhline(0, color='black', linestyle='-', linewidth=0.5)
# axes[0].set_xlabel('Year')
# axes[0].set_ylabel('Annualized Return')
# axes[0].set_title('Annual Average Returns: High Year-to-Year Variation')
# axes[0].legend()
# axes[0].grid(True, alpha=0.3, axis='y')

# # Panel 2: Volatility over time
# volatility = annual_stats['annual_volatility'].to_numpy()

# axes[1].plot(years, volatility, marker='o', linewidth=2, markersize=8, color='purple')
# axes[1].axhline(volatility.mean(), color='orange', linestyle='--', 
#                linewidth=2, label=f'Average volatility: {volatility.mean():.2%}')
# axes[1].set_xlabel('Year')
# axes[1].set_ylabel('Annualized Volatility')
# axes[1].set_title('Volatility Also Varies Through Time')
# axes[1].legend()
# axes[1].grid(True, alpha=0.3)

# plt.tight_layout()
# plt.savefig('../docs/modules/figures/module1/aapl_annual_returns_volatility.png', dpi=300, bbox_inches='tight')
# plt.show()

# # Summary statistics of annual returns
# print(f"\nSummary of Annual Returns:")
# print(f"  Mean: {annual_stats['annual_return'].mean():.4f} ({annual_stats['annual_return'].mean()*100:.2f}%)")
# print(f"  Std Dev: {annual_stats['annual_return'].std():.4f} ({annual_stats['annual_return'].std()*100:.2f}%)")
# print(f"  Min: {annual_stats['annual_return'].min():.4f} ({annual_stats['annual_return'].min()*100:.2f}%)")
# print(f"  Max: {annual_stats['annual_return'].max():.4f} ({annual_stats['annual_return'].max()*100:.2f}%)")
# print(f"  Range: {(annual_stats['annual_return'].max() - annual_stats['annual_return'].min())*100:.2f}%")