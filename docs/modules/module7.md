# Building Your Own Earnings Forecasts

## Why Not Just Use Analyst Forecasts?

We've been using analyst forecasts to compute ICC. That's the standard approach. But there's a problem.

Analyst forecasts are public information. Everyone sees them. If they contain useful information about future returns, smart money should trade on it until the information gets priced in. Eventually, the mispricing disappears.

So maybe the ICC premium we found in earlier modules won't last. Or maybe it's already weaker than it used to be. Markets learn.

Here's an alternative idea: what if you could build *better* forecasts than analysts? Or at least *different* forecasts that capture information analysts miss?

If your forecasts predict earnings better than analysts, and if the market doesn't fully price in your forecasts, you have a potential edge. You can compute ICC using your forecasts instead of analyst forecasts, form portfolios, and see if you get abnormal returns.

This is what Easton and Monahan (2016) and others have explored. Build earnings forecast models using historical fundamentals. Use those forecasts to compute ICC. Trade on it. See if it works.

Let me show you how it's done and what it tells us.

## The Basic Idea: Earnings Are Predictable

Earnings don't follow a random walk. They're predictable, at least partially, using historical information.

What predicts future earnings?

**1. Past earnings:** Earnings are persistent. High earnings today forecast high earnings tomorrow. But there's mean reversion too—extremely high earnings tend to fall, extremely low earnings tend to rise.

**2. Profitability ratios:** ROE, ROA, profit margins. Firms with high profitability tend to stay profitable for a while, though competition erodes it over time.

**3. Growth metrics:** Sales growth, asset growth, investment rates. Growing firms often sustain that growth for several years.

**4. Accruals:** The difference between earnings and cash flows. High accruals (earnings exceeding cash flows) predict lower future earnings. This is the accrual anomaly—well documented, still not fully arbitraged away.

**5. Financial structure:** Leverage, asset composition, working capital. These affect earnings stability and growth potential.

All of this is publicly available from financial statements. You can build a model that uses this information to forecast earnings.

## Why Analysts Might Miss This

Analysts are smart. They have more information than you do—management guidance, industry contacts, proprietary research. So why would a simple model based on historical financials beat them?

A few reasons:

**1. Behavioral biases:** Analysts are optimistic, especially about growth stocks. They're slow to revise forecasts downward. They herd. Your model doesn't have these biases.

**2. Conflicts of interest:** Sell-side analysts have incentives to maintain good relationships with management. They're reluctant to issue negative forecasts. Your model doesn't care about hurt feelings.

**3. Coverage gaps:** Not all firms have analyst coverage. Small firms, especially. For those firms, a model-based forecast might be the best available.

**4. Different information sets:** Analysts focus on near-term earnings (1-2 years). Your model might better capture long-term mean reversion or structural trends that analysts underweight.

You're not trying to beat analysts at their own game. You're trying to exploit systematic patterns in the data that analysts, for whatever reason, don't fully incorporate.

## Building a Forecast Model: What Goes In?

Let's get concrete. You want to forecast earnings for firm $i$ in year $t+1$. What variables do you use?

Here's a standard specification, based on Easton-Monahan and related work:

$$
E_{i,t+1} = f(E_{i,t}, ROE_{i,t}, BM_{i,t}, Accruals_{i,t}, Growth_{i,t}, \ldots)
$$

**Earnings level ($E_{i,t}$):** Most important predictor. High earnings today, high earnings tomorrow. Use earnings per share or earnings scaled by book equity.

**Profitability ($ROE_{i,t}$):** Return on equity. Captures how efficiently the firm uses shareholder capital. High ROE firms tend to maintain profitability, but with mean reversion over time.

**Book-to-market ($BM_{i,t}$):** Low B/M (growth firms) tend to have higher earnings growth, but also more mean reversion. High B/M (value firms) are more stable.

**Accruals:** Earnings minus cash flows, scaled by assets. High accruals predict *lower* future earnings. This is a robust pattern.

**Growth measures:** Sales growth, asset growth. Fast-growing firms often sustain growth, at least for a few years.

**Industry effects:** Control for industry. Earnings dynamics differ across sectors (tech vs. utilities).

You run a cross-sectional regression each year:

$$
E_{i,t+1} = \alpha + \beta_1 E_{i,t} + \beta_2 ROE_{i,t} + \beta_3 BM_{i,t} + \beta_4 Accruals_{i,t} + \varepsilon_{i,t+1}
$$

Estimate the coefficients using historical data (say, the past 10 years). Then forecast out-of-sample for year $t+1$.

This is a simple linear model. You could use more sophisticated methods—machine learning, nonlinear specifications, time-varying coefficients. But start simple. 

## From Earnings Forecasts to ICC

Once you have earnings forecasts, you plug them into the ICC calculation just like you did with analyst forecasts.

**Step 1: Forecast multiple years ahead.** You need earnings for years $t+1, t+2, \ldots, t+5$. Forecast $E_{t+1}$ directly. For $E_{t+2}$, you can either:
- Forecast it directly using $E_{t+1}$ and other variables
- Assume some growth or mean reversion pattern

Most researchers assume earnings grow at a declining rate after year 2, converging toward an industry or market average ROE.

**Step 2: Compute ICC.** Use the residual income model (or another ICC model). You have price $P_t$, book value $B_t$, and forecasted earnings $\{E_{t+1}, \ldots, E_{t+5}\}$. Solve for the discount rate $r$ that equates price to present value. That's your model-based ICC.

**Step 3: Form portfolios.** Sort stocks by model-based ICC. Form quintiles or deciles. Hold for one year. Measure returns.

If your model captures information the market doesn't price in, high ICC stocks should outperform low ICC stocks.

## The Easton-Monahan (2016) Approach

Easton and Monahan test whether a simple earnings forecast model generates profitable trading strategies.

**Their model:** Forecast earnings using:
- Lagged earnings
- Lagged ROE
- Book-to-market
- Dividend payout
- Industry effects

They estimate the model using Compustat data, forecast earnings for all firms, compute ICC, and form portfolios.

**Their results:** The model-based ICC strategy generates significant abnormal returns. High ICC stocks outperform low ICC stocks by about 4-6% per year, depending on the specification. This is similar to the returns from using analyst forecasts.

Importantly, the model-based ICC works even for firms *without* analyst coverage. For those firms, there's no analyst forecast to arbitrage away. The market doesn't seem to fully price in the information in historical fundamentals.

## What Does This Tell Us?

If a simple forecast model using publicly available data generates abnormal returns, that's evidence of market inefficiency.

The information is out there—financial statements, freely available. Anyone can run these regressions. Yet the patterns persist. Why?

**Explanation 1: Limits to arbitrage.** Small stocks, which are most profitable in these strategies, are expensive to trade. High transaction costs, low liquidity, short-sale constraints. The mispricing persists because arbitraging it away is costly or risky.

**Explanation 2: Slow information diffusion.** Investors are slow to process information from financial statements. They focus on headlines, earnings surprises, analyst revisions. They underweight the predictive power of fundamentals. Eventually prices adjust, but slowly.

**Explanation 3: Risk.** Maybe these aren't abnormal returns. Maybe high ICC stocks (based on model forecasts) are fundamentally riskier in ways we don't measure. The returns are compensation for bearing that risk.

Which explanation is right? Probably a mix. The evidence leans toward mispricing—the returns concentrate at earnings announcements, just like with analyst-based ICC. But there's likely some unmeasured risk too.

## Building Your Own Model: Practical Steps

Let's walk through the implementation.

### Step 1: Get the Data

You need:
- **Financial statement data:** Compustat or equivalent. Annual or quarterly.
- **Stock returns:** CRSP or equivalent.
- **Prices and market values:** For computing ICC and forming portfolios.

Merge these datasets by firm and date. This is non-trivial—identifiers don't always match, fiscal years are messy, timing lags matter. Budget time for data wrangling.

### Step 2: Construct Forecast Variables

Compute the variables you'll use to forecast earnings:

```python
# Placeholder: Construct forecast variables

import polars as pl

def construct_forecast_variables(data: pl.DataFrame) -> pl.DataFrame:
    """
    Construct variables for earnings forecasting.
    
    Variables:
    - earnings: Net income or EPS
    - roe: Return on equity (NI / Book Equity)
    - bm: Book-to-market ratio
    - accruals: (NI - Operating Cash Flow) / Total Assets
    - sales_growth: (Sales_t - Sales_{t-1}) / Sales_{t-1}
    - leverage: Debt / Assets
    
    Returns:
        DataFrame with added forecast variables
    """
    
    # Compute ROE
    # Compute B/M
    # Compute accruals
    # Compute growth metrics
    # Handle missing values, outliers
    
    # [Implementation to be completed]
    pass
```

Winsorize extreme values (1% and 99% percentiles). Financial ratios can have insane outliers that mess up regressions.

### Step 3: Estimate the Forecast Model

Run a cross-sectional regression each year using a rolling window of historical data:

```python
# Placeholder: Estimate earnings forecast model

def estimate_forecast_model(data: pl.DataFrame, 
                            estimation_window: int = 10) -> dict:
    """
    Estimate earnings forecast model using historical data.
    
    Model: E_{t+1} = α + β₁ E_t + β₂ ROE_t + β₃ BM_t + β₄ Accruals_t + ε
    
    Args:
        data: DataFrame with firm-year observations
        estimation_window: Number of years to use for estimation
    
    Returns:
        Dictionary with estimated coefficients
    """
    
    # Run regression on historical data
    # Use statsmodels or sklearn
    # Handle industry fixed effects if desired
    # Return coefficient estimates
    
    # [Implementation to be completed]
    pass
```

Use ordinary least squares (OLS). You could use robust standard errors, but for forecasting, the coefficients matter more than the standard errors.

### Step 4: Generate Forecasts

Apply the estimated model to forecast next year's earnings for all firms:

```python
# Placeholder: Generate earnings forecasts

def forecast_earnings(data: pl.DataFrame, 
                     model_coefficients: dict,
                     horizon: int = 5) -> pl.DataFrame:
    """
    Generate earnings forecasts using estimated model.
    
    Args:
        data: DataFrame with current year data
        model_coefficients: Estimated coefficients from forecast model
        horizon: Number of years to forecast
    
    Returns:
        DataFrame with forecasted earnings
    """
    
    # Forecast E_{t+1} directly using model
    # For E_{t+2} through E_{t+horizon}, assume growth/mean reversion
    # Common approach: exponential decay to industry median ROE
    
    # [Implementation to be completed]
    pass
```

For multi-year forecasts, you need assumptions about growth beyond year 1. Common approach: assume ROE decays exponentially toward an industry or market median. Or use a constant growth rate derived from historical patterns.

### Step 5: Compute Model-Based ICC

Use the forecasted earnings to compute ICC, just like before:

```python
# Placeholder: Compute ICC using model forecasts

def compute_model_icc(data: pl.DataFrame,
                     price_col: str = 'price',
                     book_col: str = 'book_equity',
                     earnings_cols: list = None) -> pl.DataFrame:
    """
    Compute ICC using model-based earnings forecasts.
    
    Same procedure as analyst-based ICC, but using model forecasts.
    
    Args:
        data: DataFrame with prices, book values, and forecasted earnings
        price_col: Column name for stock price
        book_col: Column name for book equity
        earnings_cols: List of column names for forecasted earnings (E1, E2, ...)
    
    Returns:
        DataFrame with computed ICC
    """
    
    # Use residual income model
    # Solve numerically for discount rate
    # Handle failures and edge cases
    
    # [Implementation to be completed]
    pass
```

Same numerical root-finding as before. Same issues with convergence, extreme values, missing data.

### Step 6: Form Portfolios and Measure Returns

Sort on model-based ICC, form portfolios, measure returns:

```python
# Placeholder: Portfolio formation with model-based ICC

def backtest_model_icc_strategy(icc_data: pl.DataFrame,
                               returns_data: pl.DataFrame,
                               n_portfolios: int = 5) -> pl.DataFrame:
    """
    Backtest trading strategy based on model-based ICC.
    
    Args:
        icc_data: DataFrame with stock-date ICC estimates
        returns_data: DataFrame with stock-date returns
        n_portfolios: Number of portfolios to form (e.g., 5 for quintiles)
    
    Returns:
        DataFrame with portfolio returns and performance statistics
    """
    
    # Sort stocks by model-based ICC
    # Form portfolios
    # Compute 12-month forward returns
    # Calculate summary statistics
    
    # [Implementation to be completed]
    pass
```

Same portfolio methodology as before. Equal-weighted, 12-month holding period, overlapping returns.

## Does It Work?

The literature suggests yes, at least historically. Model-based earnings forecasts generate profitable ICC strategies.

**Typical results:**
- Long-short returns of 4-6% per year
- Sharpe ratios around 0.4-0.6
- Returns concentrate at earnings announcements (suggesting mispricing)
- Works better for small stocks and firms without analyst coverage

But there are caveats.

**1. Out-of-sample performance.** The studies that document this use historical data. Does it still work today? Markets learn. Trading costs have fallen, but so has the low-hanging fruit. You'd need to test it live to know for sure.

**2. Model specification.** Which variables you include, how you specify the model, how you handle outliers—all of this matters. It's easy to overfit in-sample. The true out-of-sample performance might be weaker.

**3. Transaction costs.** These strategies involve high turnover, especially if you rebalance monthly. For small stocks, transaction costs can be substantial. The gross returns might not survive trading costs.

**4. Risk.** Maybe the returns are compensation for risk we're not measuring. The strategies tend to load on value and size factors. If you think those are risk factors, not mispricings, then the "alpha" isn't alpha.

## Comparing Model Forecasts to Analyst Forecasts

An interesting question: do model forecasts work better than analyst forecasts, or do they capture different information?

**Evidence:**
- For large firms with good analyst coverage, analyst forecasts are usually more accurate. Analysts have more information.
- For small firms without coverage, model forecasts are all you have, and they work.
- Even for covered firms, model forecasts sometimes capture information analysts miss, especially related to mean reversion and accruals.

**Implication:** You could combine model forecasts and analyst forecasts. Use analyst forecasts when available, fill in with model forecasts when not. Or create a weighted average. There's room for creativity here.

## What This Tells Us About Market Efficiency

The fact that simple forecast models using public data generate abnormal returns is a challenge to market efficiency.

The weak-form efficient market hypothesis says past prices don't predict future returns (beyond risk). That's mostly true—momentum and reversal are the main exceptions.

The semi-strong form says publicly available information is priced in. That's what's being tested here. And it fails, at least partially.

Financial statement information predicts earnings. Earnings forecasts predict returns. The information is public, easy to access. Yet the market doesn't fully price it in, or doesn't price it in quickly.

Why not? Probably because:
1. **It takes effort.** You have to collect data, clean it, run regressions, manage portfolios. Most investors don't bother.
2. **Transaction costs matter.** The profits are biggest for small, illiquid stocks. Trading those is expensive. The mispricing persists because arbitrage is costly.
3. **Risk and limits to arbitrage.** Exploiting these strategies requires capital, patience, and tolerance for tracking error. Not everyone can do it, even if they know about it.

So yes, there's inefficiency. But it's limited inefficiency, constrained by costs and frictions. That's the realistic view of markets: mostly efficient, but not perfectly so.

## Should You Trade on This?

That's up to you.

If you're a researcher, this is fertile ground. Lots of interesting questions:
- Can you improve the forecast model with machine learning?
- Does the strategy work internationally?
- How much of the return is mispricing vs. risk?
- Can you identify which firms are most mispriced?

If you're a practitioner building portfolios, it's worth exploring. But be realistic:
- Backtest carefully, out-of-sample, accounting for transaction costs.
- Don't expect 6% alpha. Expect something smaller, and be prepared for it to shrink over time as markets learn.
- Combine model-based ICC with other signals (value, quality, momentum) for diversification.

If you're estimating cost of capital for a firm, model-based forecasts can supplement analyst forecasts, especially for firms without coverage. But don't treat the model forecasts as gospel. They're noisy. Use them as one input among many.

## The Bottom Line

Building your own earnings forecast model is an alternative to relying on analyst forecasts. It tests whether fundamental information that's publicly available contains signals the market hasn't fully priced in.

The evidence says yes—these models generate abnormal returns, at least historically. The returns look like mispricing correction (they concentrate at earnings announcements), not risk compensation.

But exploiting this requires effort, sophistication, and tolerance for transaction costs. It's not free money. It's a trade-off between the value of the information and the cost of extracting it.

That's the realistic view. Markets are pretty efficient, but not perfectly so. There are pockets of exploitable inefficiency, especially in less liquid stocks and less scrutinized corners of the market. If you're willing to put in the work, there's alpha to be found.

Just don't expect it to be easy or to last forever.