# Portfolio Formation: Sorting on ICC 

## Testing the Theory—Or Lack Thereof

You have ICC estimates for thousands of stocks. Now what?

Remember what ICC actually is: it's the IRR that equates current price to analyst-forecasted cash flows. That's it. It's a mechanical calculation, not a deep theoretical prediction about expected returns.

But here's the question: do high ICC stocks actually earn higher returns going forward? If they do, that tells us something interesting. Maybe analyst forecasts contain information the market hasn't fully priced in yet. Maybe there's slow information diffusion. Maybe there's mispricing you can exploit.

We're not testing whether "ICC equals expected returns in equilibrium"—that's a statement about efficient markets with correct forecasts, and we know those assumptions are heroic. We're testing whether ICC sorts stocks in a way that predicts future returns. That's an empirical question about market behavior, not a test of asset pricing theory.

How do you test it? Build portfolios sorted on ICC. Track their returns. See if high-ICC portfolios actually outperform low-ICC portfolios.

This is standard in empirical asset pricing. Sort stocks into groups based on some characteristic (size, value, momentum, whatever). Form portfolios. Measure returns. That's the game.

But the details matter. A lot. How many portfolios do you form? Equal-weighted or value-weighted? Monthly rebalancing or annual? Buy-and-hold or overlapping returns? Each choice affects your results.

This module walks through portfolio formation step-by-step. We'll build quintile portfolios sorted on ICC, compute returns, and see if the theory holds up in the data.

## The Basic Sort

Here's the standard procedure:

1. **Each month**, rank all stocks by their most recent ICC estimate
2. **Sort** stocks into quintiles (five groups of equal size)
3. **Form portfolios** from each quintile
4. **Hold for one year** and measure returns
5. **Repeat** every month, creating overlapping portfolios

The result: five portfolios (Q1 through Q5) where Q1 contains the lowest ICC stocks and Q5 contains the highest ICC stocks. If theory is right, Q5 should earn higher returns than Q1.

You also construct a **long-short portfolio**: long Q5 (high ICC), short Q1 (low ICC). This is the ICC factor. It isolates the return spread between high and low ICC stocks, netting out common market exposure.

If analyst forecasts contain useful information that's not immediately arbitraged away, this spread should be positive on average.

## Step 1: Ranking Stocks by ICC

At the end of each month, you need the most recent ICC estimate for each stock. "Most recent" means the last time you computed ICC for that stock before the portfolio formation date.

**Issue 1: Stale estimates.** Some stocks don't get updated ICC estimates every month. Maybe analyst forecasts haven't changed, or the stock dropped out of your sample temporarily. Do you use the old ICC estimate or exclude the stock?

Common practice: use ICC estimates up to, say, 6 months old. After that, they're too stale. Drop the stock from that month's sort.

**Issue 2: Look-ahead bias.** Make sure your ICC estimate at time $t$ uses only information available at time $t$. Don't accidentally use forecasts from later periods. This sounds obvious, but database timestamps can be tricky.

**Issue 3: Sample size.** You need enough stocks to form meaningful portfolios. If you only have 100 stocks with valid ICC in a given month, your quintiles will have 20 stocks each. That's noisy. Ideally you want several hundred stocks per month.

### Code: Monthly Ranking

```python
# Placeholder: Rank stocks by ICC each month
# Filter to valid ICC estimates (not too old, not missing)
# Assign quintile rankings (1 = lowest ICC, 5 = highest ICC)

import polars as pl

def assign_icc_quintiles(data: pl.DataFrame, 
                         date_col: str = 'date',
                         icc_col: str = 'icc') -> pl.DataFrame:
    """
    Assign quintile ranks based on ICC within each month.
    
    Args:
        data: DataFrame with stock-month observations
        date_col: Name of date column
        icc_col: Name of ICC column
    
    Returns:
        DataFrame with added 'quintile' column (1-5)
    """
    # Rank within each month
    # Use qcut or similar to create equal-sized bins
    # Handle edge cases (ties, missing values)
    
    result = (data
              .filter(pl.col(icc_col).is_not_null())
              .with_columns([
                  pl.col(icc_col)
                    .qcut(5, labels=['Q1', 'Q2', 'Q3', 'Q4', 'Q5'])
                    .over(date_col)
                    .alias('quintile')
              ]))
    
    return result

# [Full implementation to be completed]
```

## Step 2: Forming Portfolios

Once you have quintile assignments, you form portfolios. Each portfolio contains all stocks in that quintile for that month.

**Equal-weighted vs. value-weighted:** Should you weight each stock equally, or weight by market cap?

**Equal-weighted pros:**
- Simple. Every stock contributes equally.
- Gives more influence to small stocks (since most stocks are small).
- Closer to a realistic trading strategy for smaller investors.

**Equal-weighted cons:**
- Overweights small, illiquid stocks that are expensive to trade.
- Not representative of the aggregate market.
- Returns can be driven by micro-caps that nobody actually trades.

**Value-weighted pros:**
- Represents the market portfolio.
- Emphasizes liquid, tradable stocks.
- Less sensitive to micro-cap anomalies.

**Value-weighted cons:**
- Dominated by a few mega-cap stocks.
- Small stocks barely matter, even if they have strong ICC signals.

What do researchers do? Both. Compare equal-weighted and value-weighted results. If you find strong results in equal-weighted portfolios but not value-weighted, that's a red flag—your signal might only work for tiny stocks.

We'll start with equal-weighted. It's simpler and gives a cleaner read on whether ICC predicts returns across all stocks.

### Code: Portfolio Returns

```python
# Placeholder: Compute portfolio returns
# Equal-weighted return = average of all stock returns in the portfolio

def compute_portfolio_returns(data: pl.DataFrame,
                              portfolio_col: str = 'quintile',
                              return_col: str = 'ret',
                              date_col: str = 'date') -> pl.DataFrame:
    """
    Compute equal-weighted portfolio returns.
    
    Args:
        data: DataFrame with stock returns and portfolio assignments
        portfolio_col: Column indicating portfolio membership
        return_col: Column with stock returns
        date_col: Date column
    
    Returns:
        DataFrame with portfolio returns by date
    """
    portfolio_returns = (data
                        .groupby([date_col, portfolio_col])
                        .agg(pl.col(return_col).mean().alias('port_ret'))
                        .sort([date_col, portfolio_col]))
    
    return portfolio_returns

# [Full implementation to be completed]
```

## Step 3: Measuring Returns Over What Horizon?

This is subtle. You formed portfolios based on month $t$ ICC estimates. Over what period do you measure returns?

**Option 1: One-month returns.** Buy at the end of month $t$, sell at the end of month $t+1$. Standard for testing monthly signals like momentum.

**Option 2: One-year returns.** Buy at the end of month $t$, sell at the end of month $t+12$. Common for testing annual signals like value or ICC.

**Why one year for ICC?** Because ICC is based on long-horizon forecasts (3-5 years). It's not trying to predict next month's return. It's estimating the average annual return over many years. So you should measure realized returns over a similar horizon.

But here's the catch: if you only form portfolios once a year, you waste data. You have 12 times fewer portfolio observations. Your tests have less power.

**Solution: Overlapping returns.** Form portfolios every month, but measure 12-month holding period returns. This gives you monthly observations of annual returns. Yes, the returns overlap (month $t$ return includes months $t+1$ through $t+12$, which overlaps with month $t+1$ return covering months $t+2$ through $t+13$). That creates serial correlation in your return series. But you can handle that in your standard errors using Newey-West or clustered standard errors.

**Bottom line:** Use overlapping 12-month returns. It's the right horizon for ICC and gives you enough data for robust tests.

### Code: Computing Overlapping Returns

```python
# Placeholder: Compute 12-month holding period returns
# For each stock-month, compute return from t to t+12
# Handle missing returns, delistings, etc.

def compute_forward_returns(data: pl.DataFrame,
                           return_col: str = 'ret',
                           horizon: int = 12) -> pl.DataFrame:
    """
    Compute forward holding period returns.
    
    Args:
        data: DataFrame with monthly stock returns
        return_col: Column with monthly returns
        horizon: Number of months to hold (e.g., 12 for one year)
    
    Returns:
        DataFrame with added column for forward returns
    """
    # Sort by stock and date
    # Compute cumulative returns over next 'horizon' months
    # Use lead() or shift() operations
    # Compound returns: (1+r1)*(1+r2)*...*(1+r12) - 1
    
    # [Implementation to be completed]
    pass

# [Full implementation to be completed]
```

## Step 4: The Long-Short Portfolio

The long-short portfolio is your main object of interest. It's the ICC factor return.

**Construction:**
- Long the high ICC portfolio (Q5)
- Short the low ICC portfolio (Q1)
- Return = $R_{Q5} - R_{Q1}$

This is a zero-cost, market-neutral portfolio. It captures the return difference between high and low ICC stocks. If analyst forecasts contain information that predicts returns—either because of mispricing or slow information diffusion—this spread should be positive on average.

How positive? Hard to say a priori. But you'd expect something economically meaningful—say, 2-5% per year—if ICC really contains tradable information. If you're getting 0.5%, that's too small to matter after trading costs. If you're getting 20%, something's probably wrong (or you've found the trade of the century).

### Code: Long-Short Portfolio

```python
# Placeholder: Compute long-short returns
# Q5 - Q1 for each month

def compute_long_short(portfolio_returns: pl.DataFrame,
                      portfolio_col: str = 'quintile',
                      return_col: str = 'port_ret') -> pl.DataFrame:
    """
    Compute long-short portfolio returns (Q5 - Q1).
    
    Args:
        portfolio_returns: DataFrame with portfolio returns
        portfolio_col: Column indicating portfolio (Q1, Q2, ..., Q5)
        return_col: Column with portfolio returns
    
    Returns:
        DataFrame with long-short returns
    """
    q5_returns = portfolio_returns.filter(pl.col(portfolio_col) == 'Q5')
    q1_returns = portfolio_returns.filter(pl.col(portfolio_col) == 'Q1')
    
    long_short = (q5_returns
                  .join(q1_returns, on='date', suffix='_q1')
                  .with_columns([
                      (pl.col(return_col) - pl.col(f'{return_col}_q1'))
                      .alias('long_short_ret')
                  ])
                  .select(['date', 'long_short_ret']))
    
    return long_short

# [Full implementation to be completed]
```

## Step 5: Summary Statistics

Now you have return series for five quintile portfolios and the long-short portfolio. What do you compute?

**Basic statistics:**
- **Mean return:** Average over all months
- **Standard deviation:** Volatility
- **Sharpe ratio:** Mean divided by standard deviation (annualized)
- **t-statistic:** Mean divided by standard error

The mean tells you the average performance. The Sharpe ratio tells you risk-adjusted performance. The t-statistic tells you whether the mean is statistically distinguishable from zero.

**What's a good Sharpe ratio?** For annual holding periods:
- 0.3-0.5: Decent, worth paying attention to
- 0.5-1.0: Strong, economically significant
- Above 1.0: Excellent, rare for long-only portfolios

For the long-short portfolio, Sharpe ratios above 0.5 are impressive. That's a tradable signal.

**Monotonicity:** Do returns increase steadily from Q1 to Q5? That's what theory predicts. If you see Q3 > Q4 or Q2 > Q5, that's weird. Might be noise, or might indicate your ICC estimates are flawed.

### Code: Summary Statistics

```python
# Placeholder: Compute summary statistics for portfolio returns

def compute_summary_stats(returns: pl.DataFrame,
                         return_col: str = 'port_ret',
                         annualize: bool = True) -> pl.DataFrame:
    """
    Compute summary statistics for portfolio returns.
    
    Args:
        returns: DataFrame with return time series
        return_col: Column with returns
        annualize: Whether to annualize mean and volatility
    
    Returns:
        DataFrame with summary statistics
    """
    n_obs = returns.select(pl.col(return_col).count())[0, 0]
    mean_ret = returns.select(pl.col(return_col).mean())[0, 0]
    std_ret = returns.select(pl.col(return_col).std())[0, 0]
    
    if annualize:
        # For 12-month overlapping returns, already annual
        # No adjustment needed
        # For monthly returns, would multiply by 12 (mean) and sqrt(12) (std)
        pass
    
    sharpe_ratio = mean_ret / std_ret if std_ret > 0 else None
    t_stat = mean_ret / (std_ret / (n_obs ** 0.5)) if std_ret > 0 else None
    
    stats = pl.DataFrame({
        'mean': [mean_ret],
        'std': [std_ret],
        'sharpe': [sharpe_ratio],
        't_stat': [t_stat],
        'n_obs': [n_obs]
    })
    
    return stats

# [Full implementation to be completed]
```

## Why Quintiles?

Why five portfolios? Why not deciles (10) or terciles (3)?

**Fewer portfolios (terciles):**
- More stocks per portfolio, so less noisy
- But coarser measure—might miss variation within groups
- Less granular test of monotonicity

**More portfolios (deciles):**
- Finer sorting, better isolates extreme ICC stocks
- But fewer stocks per portfolio, so noisier returns
- Harder to see clean patterns with 10 groups

**Quintiles are the Goldilocks choice:** Enough granularity to see patterns, enough stocks per portfolio to reduce noise. It's the standard in empirical asset pricing for a reason.

You can also try other cuts. If you're testing a very strong signal, deciles might work. If you have a small sample, terciles might be safer. But start with quintiles.

## Why Equal Weights?

We covered this earlier, but it's worth repeating: equal-weighted portfolios treat every stock the same. This is good for testing whether ICC predicts returns broadly across the universe of stocks.

But it's bad for assessing economic significance. If your ICC premium only shows up in micro-cap stocks that cost 50 bps to trade, it's not implementable. The Sharpe ratio looks great, but you can't capture it.

**Best practice:** Report both equal-weighted and value-weighted results. If the signal survives both, it's robust. If it only works equal-weighted, it's a small-stock effect. That's still interesting, but less useful for asset pricing theories that claim to explain aggregate market returns.

## What You Expect to Find

If ICC sorts stocks in a way that predicts returns—whether because of mispricing, analyst forecast information, or slow-moving capital:
- **Q5 returns > Q4 returns > ... > Q1 returns:** Monotonic increase across quintiles
- **Long-short return > 0:** High ICC stocks outperform low ICC stocks  
- **Sharpe ratio > 0.3-0.5:** Economically meaningful risk-adjusted returns
- **t-statistic > 2:** Statistically significant at 5% level

If you find this, you've got evidence that analyst forecasts embedded in ICC contain information the market doesn't immediately arbitrage away.

If you don't find this:
- **Monotonicity fails:** ICC isn't cleanly related to returns. Could be measurement error, could be that analyst forecasts don't predict returns, could be that any information is already in prices.
- **Long-short return ≈ 0:** No ICC premium. Either analyst forecasts are useless for predicting returns, or the market is efficient enough that the information gets arbitraged away.
- **Sharpe ratio < 0.3:** Premium is too small to matter economically, even if statistically significant.

**Reality check:** The literature on ICC is mixed. Some papers find strong results, others find weak results. It depends on the sample period, the ICC model, the portfolio construction, and how you handle outliers. Don't expect magic. Expect messy, noisy data that sometimes shows a premium and sometimes doesn't.

## Practical Issues You'll Hit

**Missing returns:** Stocks delist, get acquired, or stop trading. You can't compute 12-month returns if the stock disappears after 6 months. What do you do?

- **Option 1:** Set the return to zero from the delisting date onward. Biases results if delistings are for bad reasons (bankruptcy).
- **Option 2:** Use the delisting return from CRSP (which includes final liquidation value). More accurate but requires careful data handling.
- **Option 3:** Drop stocks with incomplete return histories. Cleaner but creates survivorship bias.

Most researchers use Option 2 when possible, fall back to Option 3.

**Overlapping returns and standard errors:** Your 12-month returns overlap, so consecutive observations are correlated. Standard t-statistics will be wrong (too high). You need Newey-West standard errors with at least 12 lags to account for the overlap.

Alternatively, use non-overlapping returns (form portfolios in January only). But then you only have 1/12 as many observations. The power cost is huge.

**Rebalancing costs:** We're assuming you can trade costlessly. You can't. Turnover in the portfolios (stocks moving between quintiles) generates trading costs. If turnover is 50% per month, that's a lot of trades. For small or illiquid stocks, bid-ask spreads and price impact can eat up several percent per year.

For now, ignore trading costs. Just compute gross returns. Later, if you're building a real strategy, you'll need to account for costs.

## Interpreting the Results

Suppose you find a significant ICC premium. Q5 earns 12% per year, Q1 earns 8%, long-short earns 4% with a Sharpe ratio of 0.6. Great result. What does it mean?

**Three interpretations:**

**1. Mispricing:** The market doesn't fully incorporate analyst forecast information into prices. High ICC stocks are undervalued—analysts see strong future cash flows, but the market hasn't priced them in yet. The 4% premium is compensation for identifying mispricing. This is the value investing story.

**2. Slow information diffusion:** Analyst forecasts are public information, but it takes time for the market to react. By the time you compute ICC and form portfolios, the information hasn't been fully arbitraged away. You're capturing a window of opportunity before prices adjust.

**3. Unmeasured risk:** High ICC stocks might be systematically riskier in ways traditional risk models don't capture. The 4% premium is compensation for bearing that risk, not abnormal returns. This is the asset pricing theorist's fallback position.

**How do you distinguish these?**

- **Risk explanation:** Show that ICC loads on known risk factors (market, size, value, etc.) or that high ICC stocks have higher exposures to macroeconomic shocks. Run Fama-French regressions. If the alpha is zero after controlling for factors, it's risk.
  
- **Mispricing/information explanation:** Show that the ICC premium is stronger among stocks with limits to arbitrage (high idiosyncratic volatility, low institutional ownership, small size). Or show that it predicts future earnings surprises or analyst forecast revisions. If the premium concentrates where arbitrage is hard or information is slow, it's mispricing.
  
- **Data mining:** Test out-of-sample (different time period, different country) or with a different ICC model. If it replicates, probably not data mining.

None of these are conclusive. But they help you build a story about what's going on.

## Statistical vs. Economic Significance

A t-statistic of 2.5 means your result is statistically significant at the 5% level. The probability of seeing this result by chance is less than 5%. Good.

But that doesn't mean the result matters economically. If your long-short portfolio earns 0.5% per year with a t-statistic of 3, it's highly significant statistically, but 0.5% is too small to care about. Transaction costs will eat it up. It doesn't explain much variation in returns.

**Economic significance asks:** Is the magnitude large enough to matter for investors or asset pricing theory?

**Rules of thumb:**
- **Long-short annual return > 2-3%:** Starting to be economically meaningful
- **Sharpe ratio > 0.5:** Definitely matters for portfolio construction
- **Explains > 5% of return variation (R²):** Matters for asset pricing

A result can be statistically significant without being economically significant. The reverse is also possible (economically large effect that's not statistically significant due to small sample). Report both. Be honest about what your results mean.

## The Full Pipeline

Here's how it all fits together:

```python
# Placeholder: Full portfolio formation and analysis pipeline

import polars as pl
from typing import Dict

def run_icc_portfolio_analysis(icc_data: pl.DataFrame,
                               returns_data: pl.DataFrame,
                               start_date: str,
                               end_date: str) -> Dict:
    """
    Complete pipeline for ICC portfolio analysis.
    
    Steps:
    1. Rank stocks by ICC each month
    2. Form quintile portfolios
    3. Compute 12-month forward returns
    4. Calculate portfolio returns (equal-weighted)
    5. Compute long-short returns
    6. Generate summary statistics
    
    Args:
        icc_data: DataFrame with stock-month ICC estimates
        returns_data: DataFrame with stock-month returns
        start_date: Start of analysis period
        end_date: End of analysis period
    
    Returns:
        Dictionary with portfolio returns and summary statistics
    """
    # Step 1: Merge ICC and returns data
    # [Code to merge]
    
    # Step 2: Assign quintile ranks
    # ranked_data = assign_icc_quintiles(merged_data)
    
    # Step 3: Compute forward returns
    # ranked_data = compute_forward_returns(ranked_data, horizon=12)
    
    # Step 4: Compute portfolio returns
    # portfolio_returns = compute_portfolio_returns(ranked_data)
    
    # Step 5: Compute long-short
    # long_short = compute_long_short(portfolio_returns)
    
    # Step 6: Summary statistics
    # stats = compute_summary_stats(portfolio_returns)
    
    # Return results
    # results = {
    #     'portfolio_returns': portfolio_returns,
    #     'long_short': long_short,
    #     'summary_stats': stats
    # }
    
    # return results
    
    pass

# [Full implementation to be completed]
```

## Replication Checklist

When you run your analysis, check these key outputs:

**✓ Raw returns by quintile:**
- Q1: ~8-10% per year
- Q5: ~10-14% per year
- Generally increasing from Q1 to Q5

**✓ Long-short returns:**
- Mean: 2-5% per year
- Sharpe ratio: 0.3-0.7
- t-statistic: > 2.0

**✓ Return monotonicity:**
- No large reversals (e.g., Q4 < Q3)
- Spread between adjacent quintiles makes sense

**✓ Sample characteristics:**
- At least 100+ stocks per quintile
- Reasonable turnover (20-40% per month)
- Not dominated by penny stocks or micro-caps

If your results look wildly different from these benchmarks, something might be wrong. Check your data and code.

## Common Pitfalls

**Pitfall 1: Look-ahead bias.** Using ICC estimates computed with information not available at portfolio formation date. Obvious in theory, easy to do in practice when timestamps are messy.

**Pitfall 2: Survivorship bias.** Only including stocks that survive the full sample period. Drops all delistings, bankruptcies, and acquisitions. Makes returns look better than they were.

**Pitfall 3: Ignoring delisting returns.** When a stock gets delisted (especially for bad reasons), the final return can be -100%. If you drop it or set to zero, you miss a huge loss.

**Pitfall 4: Wrong standard errors.** Using regular standard errors on overlapping returns gives you inflated t-statistics. Use Newey-West with appropriate lags.

**Pitfall 5: Data errors.** Wrong prices, bad merges, stale forecasts. Always validate intermediate steps. Check sample counts, mean values, and a few examples by hand.

These aren't hypothetical. Every researcher makes these mistakes at some point. The key is to catch them before you present results.

## Summary: From ICC to Returns

You've computed ICC. You've formed portfolios. You've measured returns. Now you know whether ICC—as a summary of analyst forecasts relative to price—predicts returns in your sample.

If it does, you have evidence that analyst forecasts contain information not immediately reflected in prices. Whether that's mispricing, slow information diffusion, or compensation for unmeasured risk is a question for further analysis.

If it doesn't, you've learned something too. Maybe analyst forecasts are already in prices. Maybe they're too noisy. Maybe the sample period is bad. Maybe ICC is just a poor way to extract information from forecasts. That's useful to know.

Either way, you've done the core empirical work. The next step is to understand *why* ICC predicts returns (if it does) or *why not* (if it doesn't). That requires more sophisticated tests—risk adjustment, characteristic controls, robustness checks. We'll get there.

For now, you have portfolios. You have returns. That's progress.
