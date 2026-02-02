# Computing ICC in Practice

## From Theory to Code

The models look clean on paper. Price equals present value, solve for the discount rate, done. But when you sit down to actually compute ICC for thousands of stocks using real data, you run into problems.

Analyst forecasts are missing. Earnings are negative. Book values don't match between databases. Prices have stale quotes. The root-finding algorithm doesn't converge. You get ICC estimates of 150% or -20%, which are obvious nonsense.

This is the messy reality of empirical work. The theory doesn't tell you how to handle it. The academic papers gloss over it or hide the details in footnotes. You have to figure it out yourself.

This module walks through the actual implementation. We'll go step-by-step: getting the data, cleaning it, computing ICC, and dealing with all the things that go wrong. By the end, you'll have code that works on real data—not just textbook examples.

## The Basic Pipeline

Here's the workflow for computing ICC:

1. **Get analyst forecasts** from IBES (or your data source)
2. **Get prices** as of the same date
3. **Get book equity** from financial statements
4. **Construct the expected earnings path** using the forecasts and growth assumptions
5. **Solve numerically** for the discount rate that equates price to present value
6. **Clean the results** by filtering out nonsense estimates

Each step has pitfalls. Let's go through them.

## Step 1: Loading Analyst Forecasts

You need earnings forecasts for the next few years. IBES (Institutional Brokers' Estimate System) is the standard source. It aggregates forecasts from sell-side analysts.

What you want:
- **Consensus forecasts** (mean or median) for annual earnings per share (EPS)
- **Forecast horizon** of at least 3 years, ideally 5
- **Point-in-time data** so you're not looking into the future

What you'll get:
- Some firms have forecasts out 5 years, others only 1 year
- Some forecasts are stale (not updated in months)
- Some are for fiscal years, others for calendar years
- IBES identifiers don't always match your price or accounting database identifiers

You have to decide: what do you do when a firm only has 2-year forecasts but your model needs 5? Most researchers extrapolate using long-term growth (LTG) forecasts from IBES. But those are notoriously unreliable. We'll come back to this.

### Code: Loading IBES Data

```python
# Placeholder: Load IBES consensus forecasts
# We'll use polars for speed and WRDS for data access

# Example structure:
# - ticker, date, fpi (forecast period indicator), meanest (consensus EPS)
# - We need FPI=1 (1-year ahead), FPI=2 (2-year ahead), etc.

# [Code to be implemented with polars and WRDS]
```

## Step 2: Getting Prices

You need the stock price on the same date as your forecasts. Sounds simple. It's not.

Issues:
- **Timing:** IBES forecast dates might not match trading days. You need the closest available price.
- **Corporate actions:** Prices need to be adjusted for splits and dividends. IBES forecasts are usually adjusted too, but check.
- **Stale prices:** Thinly traded stocks might have prices that haven't updated in days. Do you use the last available price or skip the stock?
- **Delisting:** Stocks that got delisted aren't in your price database anymore, but they were in IBES. This creates survivorship bias if you're not careful.

Best practice: use point-in-time prices from a reliable source (CRSP if you're in academia). Match by date within a reasonable window (say, ±5 days).

### Code: Merging Prices

```python
# Placeholder: Merge IBES forecasts with CRSP prices
# Use ticker or PERMNO for matching
# Handle date alignment with asof joins

# [Code to be implemented with polars and WRDS]
```

## Step 3: Getting Book Equity

Book equity comes from balance sheets. Standard sources: Compustat (annual or quarterly).

The ICC models need book value $B_0$ at the start of the forecast period. Ideally, you'd use the most recent reported book equity before your forecast date.

Complications:
- **Timing lag:** Financial statements are released with a lag. The most recent statement might be from 3 months ago.
- **Fiscal year mismatch:** Some firms have fiscal years ending in June, others in December. You need to align with your forecast dates.
- **Negative book equity:** Some firms (especially distressed or tech startups) have negative book equity. The RIM breaks down. You'll have to exclude them.

You also need to track book equity forward to compute residual income in future years. That requires forecasting book values using the clean surplus relation: $B_t = B_{t-1} + E_t - D_t$. You need a dividend payout assumption. Common choice: constant payout ratio based on historical average.

### Code: Getting Book Values

```python
# Placeholder: Load book equity from Compustat
# Merge with IBES data by firm identifier and date
# Compute payout ratios from historical data

# [Code to be implemented with polars and WRDS]
```

## Step 4: Constructing the Earnings Path

Now you have forecasts for years 1, 2, maybe 3-5. You need to build the full expected earnings path out to your terminal horizon (say, $T = 5$ years).

If you have all 5 years of forecasts, great. Just use them. If not, you need to extrapolate.

**Option 1:** Use IBES long-term growth (LTG) forecasts. These are 5-year expected growth rates. If you have $E_1$ and $E_2$, you can compute $E_3 = E_2 \times (1 + \text{LTG})$, $E_4 = E_3 \times (1 + \text{LTG})$, etc.

**Option 2:** Assume earnings converge to an industry median ROE. This is more conservative but requires industry classification data.

**Option 3:** Drop firms without sufficient forecasts. This reduces your sample but avoids extrapolation errors.

There's no perfect answer. Just be consistent and document your choice.

You also need to convert earnings into residual income: $RI_t = E_t - r \cdot B_{t-1}$. But you don't know $r$ yet—that's what you're solving for. So you'll do this inside the ICC calculation.

### Code: Building Earnings Path

```python
# Placeholder: Construct forward earnings path
# Use available forecasts + extrapolation for missing years
# Handle edge cases (missing LTG, inconsistent growth)

# [Code to be implemented]
```

## Step 5: Solving for ICC Numerically

Here's the core calculation. You have price $P_0$, book value $B_0$, forecasted earnings $E_1, \ldots, E_T$, and terminal growth $g$. You need to find $r$ such that:

$$
P_0 = B_0 + \sum_{t=1}^{T} \frac{RI_t(r)}{(1+r)^t} + \frac{RI_T(r) \cdot (1+g)}{(r-g)(1+r)^T}
$$

where $RI_t(r) = E_t - r \cdot B_{t-1}$.

Notice residual income depends on $r$, so this is a nonlinear equation. You can't solve it in closed form. You need a numerical root-finding algorithm.

**Standard approach:** Use a root-finding method like Brent's algorithm (implemented in `scipy.optimize.brentq`). Define a function that computes the right-hand side minus $P_0$. Find the value of $r$ that makes it zero.

**Practical issues:**
- **Initial bounds:** You need to give the algorithm a bracket, say $r \in [0.01, 0.50]$ (1% to 50%). If the true ICC is outside this range, the algorithm fails. 
- **No solution:** Sometimes there's no $r$ that satisfies the equation, especially if the firm has negative earnings or book value. The algorithm will throw an error. Catch it and set ICC to missing.
- **Multiple solutions:** Theoretically possible, though rare. The root-finder will return one solution. Hope it's the right one.
- **Convergence:** Root-finding can be slow for large datasets. Make sure your code is vectorized or use multiprocessing.

### Code: Numerical Root-Finding

```python
# Placeholder: Define the pricing equation as a function of r
# Use scipy.optimize.brentq to solve for r
# Handle convergence failures and edge cases

# Example:
# def pricing_error(r, P0, B0, earnings, terminal_growth):
#     # Compute RHS of pricing equation
#     # Return RHS - P0
#     pass
# 
# icc = brentq(pricing_error, 0.01, 0.50, args=(P0, B0, earnings, g))

# [Code to be implemented]
```

## Step 6: Cleaning the Results

You've computed ICC for every stock. Now look at the distribution. You'll see:
- Some ICCs are negative. This happens when price is high relative to forecasts—implies the market is pricing in growth beyond what analysts forecast, or the stock is overvalued.
- Some ICCs are above 50% or even 100%. Usually means something went wrong (negative book value, stale forecast, data error).
- Some ICCs are missing because the root-finder failed.

What do you do?

**Negative ICCs:** Some researchers set them to missing. Others keep them and interpret as mispricing signals. Depends on your use case. If you're building a long-only portfolio, you'll probably exclude them.

**Extreme ICCs:** Winsorize or trim. Common choice: drop ICC below 0% or above 30-50%. Or winsorize at the 1st and 99th percentiles.

**Missing data:** Firms with missing ICC can't be used. Document how many you lose.

This is judgment. There's no "correct" cutoff. Just be consistent and report what you did.

### Code: Filtering and Cleaning

```python
# Placeholder: Filter ICC estimates
# Remove negatives, extreme values, missings
# Winsorize if needed

# Example:
# icc = icc[(icc > 0) & (icc < 0.50)]  # Keep ICC between 0% and 50%

# [Code to be implemented]
```

## Design Choices: What Matters?

Let's talk about the decisions you have to make and how much they matter.

### Root-Finding vs. Closed Form

Some ICC models have approximate closed-form solutions. For example, if you assume constant residual income growth from year 1 onward, you can derive an explicit formula for $r$.

**Closed form pros:** Fast. No numerical issues. Easy to implement.

**Closed form cons:** Requires strong assumptions (constant growth, perpetual residual income). Less flexible.

For the two-stage RIM we're using, there's no clean closed form. You need numerical methods. The cost is speed, but modern computers are fast enough that it's not a problem unless you're computing ICC for millions of stocks every day.

**Recommendation:** Use numerical root-finding. It's more flexible and accurate.

### Handling Negative Earnings

Firms with negative earnings are a problem. Residual income is $RI = E - r \cdot B$. If $E < 0$ and $B > 0$, then $RI$ is even more negative. The present value of future residual income can exceed $B_0$, making the theoretical price negative. That's nonsense.

Options:
1. **Exclude firms with any negative earnings** in the forecast horizon. This is safe but throws away a lot of data (startups, distressed firms).
2. **Use only positive earnings years** and set negative years to zero. Biases ICC upward.
3. **Switch to a different model** for firms with negative earnings, like a dividend discount or asset-based valuation. More work.

Most researchers do (1) and exclude firms with negative forecasted earnings. It's practical, though it means your sample is tilted toward mature, profitable firms.

**Recommendation:** Exclude firms with negative forecasted earnings in any of the first $T$ years. Document the sample loss.

### Winsorization and Trimming

Your ICC estimates will have outliers. What do you do?

**Trimming:** Drop extreme values entirely. Example: remove ICC < 0 or ICC > 0.50.

**Winsorizing:** Cap extreme values at a threshold. Example: set all ICC > 0.50 to exactly 0.50.

**Which is better?** Trimming is cleaner—you're not creating artificial data points. But you lose information. Winsorizing keeps the sample size but creates a mass point at the threshold.

For descriptive analysis and portfolio construction, trimming is usually better. For regression analysis, winsorizing might be preferred to maintain sample size.

**Recommendation:** Trim at reasonable economic thresholds (e.g., 0% to 30% or 50%). Report how many observations you lose.

## Putting It All Together

Here's the full workflow in code:

```python
# Placeholder: Full ICC computation pipeline

# Step 1: Load data
# forecasts = load_ibes_forecasts(date)
# prices = load_crsp_prices(date)
# book_values = load_compustat_book_equity(date)

# Step 2: Merge datasets
# data = merge_data(forecasts, prices, book_values)

# Step 3: Construct earnings path
# data = construct_earnings_path(data, horizon=5)

# Step 4: Solve for ICC
# data['icc'] = data.apply(lambda row: solve_icc(row), axis=1)

# Step 5: Clean results
# data = data[(data['icc'] > 0) & (data['icc'] < 0.50)]

# Output: DataFrame with ticker, date, icc, and other variables

# [Full code to be implemented]
```

## What Can Go Wrong?

Everything. Here are the common issues you'll run into:

**Data alignment problems:** Tickers don't match across databases. Dates are off by a few days. Fiscal years don't align. You merge and lose half your sample.

**Missing forecasts:** Many firms don't have 5-year forecasts. You have to decide whether to extrapolate or drop them. Either choice has costs.

**Convergence failures:** The root-finder doesn't converge for 10-20% of stocks. Usually because of extreme values, negative earnings, or data errors. You have to drop them.

**Nonsense estimates:** Even after cleaning, some ICC estimates just look wrong. A stable utility with a 25% ICC? A high-growth tech firm with a 5% ICC? Check your data and model assumptions.

**Speed:** Computing ICC for 5,000 stocks is fast. For 50,000 stocks over 20 years? That's millions of root-finding problems. You'll need to optimize your code.

Don't get discouraged. This is normal. Empirical work is messy. The key is to be systematic: document your choices, check intermediate outputs, validate against known benchmarks.

## Validation: Does It Make Sense?

Before you trust your ICC estimates, run some sanity checks:

1. **Descriptive statistics:** What's the median ICC? The 10th and 90th percentiles? Should be in the 8-15% range for most stocks. If median is 50%, something's wrong.

2. **Cross-sectional patterns:** High P/B firms should have lower ICC (growth expectations). High beta firms should have higher ICC (risk). Check if these patterns hold.

3. **Time series:** Average ICC across all stocks should vary with market conditions. High in recessions, low in booms. Plot it over time and see if it makes sense.

4. **Known benchmarks:** Some papers report ICC estimates for specific firms or years. Try to replicate them. If you can't, figure out why.

If your estimates pass these checks, you're probably okay. If not, go back and debug.

## Summary: Implementation Matters

The ICC models are simple in theory. But implementation is where the rubber meets the road. The quality of your data, your choices for handling missing values and outliers, your numerical methods—all of this matters.

There's no one "correct" way to implement ICC. Different researchers make different choices. What matters is that you're consistent, transparent, and thoughtful about your decisions.

In the next modules, we'll use these ICC estimates to analyze stock returns and build portfolios. But remember: garbage in, garbage out. If your ICC computation is flawed, everything downstream will be flawed too.

Take the time to get this right.
