# Setup & Philosophy

## What This Course Is About

Estimating expected returns is one of the fundamental problems in finance. The traditional approach uses historical data: compute realized returns over some period and hope they're representative of future expectations. But past returns are noisy, backward-looking, and may not reflect current market conditions or future prospects.

Over the past two decades, researchers have developed an alternative: the implied cost of capital (ICC). Instead of looking backward at realized returns, ICC looks forward. It's rooted in valuation theory. Start with the premise that price equals the present value of expected cash flows. Take analysts' earnings forecasts as a proxy for expected cash flows. Combine them with observed market prices. Then solve for the discount rate that equates the two. That discount rate is ICC—an expected return measure derived from current prices and forward-looking forecasts.

The appeal is obvious. ICC uses information that's forward-looking and market-based. It updates continuously as prices and forecasts change. Researchers have used it to estimate the equity risk premium, test asset pricing models, evaluate corporate investment decisions, and measure changes in required returns over time.

But ICC rests on valuation premises that may not hold. The approach assumes investors agree with analyst forecasts and that prices reflect fundamental values. If those assumptions fail—if analysts are systematically biased or if prices deviate from fundamentals—then ICC might not equal the true expected return.

Still, ICC gives us a way to estimate expected returns without relying solely on historical data. Whether it's better than alternatives is an empirical question. This course shows you how to compute ICC, understand what it measures, and evaluate whether it works as an expected return proxy.

Here's what you'll learn:
- The valuation theory underlying ICC: residual income models, dividend discount models, and their connection to expected returns
- How to compute ICC from analyst forecasts and market prices
- Different ICC estimation methods and their assumptions
- How ICC compares to historical return estimates as a measure of expected returns
- The practical details: data sources, numerical methods, implementation choices

By the end, you'll have working Python code for computing ICC across stocks and over time. You'll understand the valuation premises behind ICC, what assumptions are required for it to measure expected returns, and how to evaluate those assumptions empirically. You'll see how ICC varies across firms and how it relates to realized returns.

This is about measurement, not prediction. Can we use valuation models and analyst forecasts to construct reasonable expected return proxies? That's the question we'll answer.

## The Economic Logic

The logic starts with valuation theory. Any valuation model says price equals the present value of expected cash flows, discounted at the expected return:

$$P_0 = \sum_{t=1}^{\infty} \frac{E[CF_t]}{(1+r)^t}$$

This equation has three components: current price $P_0$, expected cash flows $E[CF_t]$, and the expected return $r$. Standard valuation uses $r$ to compute $P_0$. ICC flips it around: use observed $P_0$ and forecasted cash flows to solve for $r$. That's the implied cost of capital.

The most common implementation uses the residual income model. Start with the accounting identity that relates earnings, book value, and dividends. Substitute into the dividend discount model. Rearrange, and you get price as a function of current book value, forecasted earnings, and a discount rate. Solve for the discount rate—that's ICC.

The interpretation depends on two premises. First, analyst forecasts represent market expectations of future cash flows. Second, prices equal fundamental value—the present value of those expected cash flows. If both hold, then ICC is the expected return required by investors, the cost of capital.

These are strong premises. Analyst forecasts might not match market expectations. Analysts have their own biases, information sets, and incentives. Prices might not equal fundamental value. There's noise, liquidity effects, limits to arbitrage. So ICC might not equal the true expected return.

But ICC still gives us an expected return measure that's forward-looking and model-based. Compare it to the alternative: estimate expected returns from historical data. That approach assumes past returns are representative of future expectations—also a strong assumption. ICC trades one set of assumptions for another.

The empirical question is whether ICC works as an expected return proxy. Does it vary sensibly across firms and over time? Does it relate to realized returns the way expected returns should? Can we understand when the underlying premises are more or less likely to hold? Those questions have empirical answers.

## ICC: What It Measures

The implied cost of capital is the internal rate of return that equates current price to forecasted cash flows under a specific valuation model. You choose a model (residual income, dividend discount, abnormal earnings growth), plug in analyst forecasts, set the equation equal to observed price, and solve for the discount rate. That solution is ICC.

**Under the premises:** If analyst forecasts match market expectations and prices equal fundamental value, then ICC measures the market's expected return for that stock. It's the cost of capital—the return investors require to hold the stock given its risk.

**When premises fail:** If forecasts don't match market expectations or prices deviate from fundamentals, ICC measures something else. It might reflect analyst biases, market sentiment, or measurement error from model misspecification. ICC is only as good as its inputs and assumptions.

**As an expected return proxy:** ICC gives us a forward-looking return measure that updates with prices and forecasts. Compare it to historical averages, which are noisy and backward-looking. ICC might be better, or it might substitute one set of errors for another. That's an empirical question.

**Cross-sectional variation:** If ICC works as an expected return measure, it should vary sensibly across stocks. Higher ICC for riskier firms, lower ICC for safer firms. The patterns should match what asset pricing theory predicts about required returns.

**Time-series variation:** If ICC captures changes in required returns, it should move with market conditions. Higher when risk premiums are high, lower when they're low. It should relate to measures of aggregate risk or investor sentiment.

These are testable implications. We can compute ICC, examine how it varies, and check whether the patterns make economic sense for an expected return measure.

## Validating ICC as an Expected Return Measure

If ICC measures expected returns, it should predict realized returns. Expected returns vary across stocks—some stocks are riskier and should earn higher returns. If ICC captures that variation, then stocks with high ICC should subsequently earn high returns, and stocks with low ICC should earn low returns.

That's testable. Here's how:

**1. Compute ICC for each stock:** Take analyst earnings forecasts from IBES, combine them with stock prices from CRSP and balance sheet data from Compustat. Use the residual income model to compute ICC for every stock each month.

**2. Sort stocks on ICC:** Rank stocks by their ICC and form portfolios. Deciles, quintiles, or simple high/low sorts. This creates portfolios with different ex-ante expected returns if ICC measures those expectations correctly.

**3. Measure realized returns:** Track the portfolios forward and measure their returns. If ICC is a good expected return proxy, high ICC portfolios should earn high returns, low ICC portfolios should earn low returns.

**4. Evaluate the relationship:** Does ICC predict returns? How strong is the relationship? Is it economically significant or just statistically detectable? Does it survive risk adjustments?

This is the standard approach for validating expected return proxies. The literature has done this extensively with ICC. The results: ICC does predict returns in the cross-section. High ICC stocks outperform low ICC stocks on average. The effect is robust across different sample periods, different ICC models, and different portfolio formation methods.

But there's a puzzle. If ICC were a perfect expected return measure, and if expected returns reflected compensation for risk, then the ICC-return relationship should be explained by standard risk factors. It's not. High ICC stocks outperform even after controlling for market, size, and value factors. That suggests either ICC captures risk dimensions that standard factors miss, or the underlying premises don't fully hold.

## What You'll Actually Learn

Here's the course roadmap:

**Module 2-3: Understanding ICC**
- The residual income model and how it leads to ICC
- The relationship between ICC and expected returns (and why they're not the same)
- How analyst forecasts enter the calculation
- Common ICC models and their assumptions

**Module 4: Implementation**
- Getting data from WRDS: IBES for analyst forecasts, CRSP for prices and returns, Compustat for fundamentals
- Working with parquet files for efficient data storage and access
- Computing ICC numerically (it's a root-finding problem)
- Handling edge cases: missing data, negative earnings, convergence failures
- The practical details that determine whether this works in practice

**Module 5: Portfolio Formation and Returns**
- Sorting stocks on ICC and forming portfolios
- Equal-weighted vs. value-weighted returns
- Overlapping vs. non-overlapping holding periods
- Computing portfolio statistics and risk-adjusted returns
- What the historical evidence shows


By the end, you'll have working Python code for the entire pipeline: data acquisition, ICC computation, portfolio formation, return measurement, and performance evaluation.

## Technical Setup

We'll use modern Python tools that make working with financial data efficient and reproducible:

**uv for package management:** We'll use `uv` to manage Python environments and dependencies. It's fast, it's simple, and it keeps your project isolated. No more dependency hell.

**Parquet files for data storage:** Financial data is large and you'll use it repeatedly. We'll store everything in parquet format—compressed columnar storage that's fast to read and write. Much better than CSV files or repeatedly hitting databases.

**WRDS for data:** We'll get our data from Wharton Research Data Services (WRDS). You'll need access (most universities and research institutions have it). We'll pull:
- IBES: Analyst earnings forecasts and recommendations  
- CRSP: Stock prices, returns, and market caps
- Compustat: Balance sheet and income statement data

The first module will walk through setting up data pipelines: connecting to WRDS, downloading what you need, converting to parquet, and organizing it so you can work efficiently. Once the data is local and in parquet format, everything runs fast.

**Polars for data manipulation:** We'll use Polars (not pandas) for data manipulation. It's faster, more memory-efficient, and has a better API for the operations we need. If you know pandas, Polars will feel familiar but better.

All code will be in Python 3.11+. We'll write clean, readable code that you can understand and modify. No clever tricks, no unnecessary abstraction—just straightforward implementations of the models and portfolio strategies.

## Prerequisites

You should have:
- **Finance basics:** Understand present value, discount rates, and what expected returns mean. Know that stock prices are supposed to equal the present value of cash flows. That's enough.
- **Python:** Can write functions, use dataframes (pandas or polars), make plots. If you've done any data analysis in Python, you're ready.
- **Statistics:** Understand means, standard deviations, regression. We'll compute portfolio returns and run some regressions. Nothing fancy.

You don't need:
- PhD-level asset pricing theory. We'll explain what we need.
- Prior knowledge of ICC models. That's what we're teaching.
- Experience with WRDS. We'll show you how to get the data.

The course assumes you're comfortable reading and writing code. We'll provide complete implementations, but you should be able to read through a Python function and understand what it does. If you can't, go learn Python first.

## How to Use This Course

Work through the modules in order. Each builds on the previous one.

Actually implement the code. Don't just read. Download the data, compute ICC, form portfolios, measure returns. Then modify something—change the holding period, try different sorting rules, use different forecasts—and see what happens. That's how you learn.

When results look strange, figure out why. If ICC estimates are weird for some stocks, debug it. If portfolio returns are negative, understand whether that's a bad out-of-sample period or a sign something's wrong with the implementation. The details matter.

Start simple. Get the basic analyst-based ICC strategy working before adding complexity. Make sure you can replicate the basic return patterns in the literature. Then add your own extensions.

Think about economics, not just statistics. A t-statistic of 2.5 is nice, but if the return spread is 1% per year and you're trading small stocks with 50bp transaction costs, there's no money there. Focus on whether magnitudes make economic sense.

## What to Expect

This course takes a measurement perspective on ICC. The goal is to understand ICC as an expected return proxy, evaluate when it works, and understand its limitations.

**The framework:** You'll learn the valuation theory underlying ICC, how to implement different ICC models, and how to compute ICC from real data. This is about understanding the methodology, not just applying a formula.

**The evidence:** We'll examine whether ICC behaves like an expected return measure should. Does it vary sensibly across firms? Does it predict realized returns? How does it compare to historical return estimates or other proxies?

**The assumptions:** Every measurement approach makes assumptions. For ICC, the key assumptions concern analyst forecasts and market prices. We'll examine those assumptions empirically and understand when they're more or less likely to hold.

**The applications:** ICC has been used to measure the equity risk premium, evaluate corporate investment decisions, and test asset pricing models. Understanding how ICC is constructed and what it measures is essential for interpreting this research.

**The puzzles:** ICC predicts returns, but in ways that don't fully align with standard risk-based asset pricing. Is that because ICC captures risk dimensions we don't fully understand? Or because the underlying valuation premises sometimes fail? These are open questions.

This is fundamentally about measurement methodology in empirical finance. How do we estimate expected returns? What role can valuation models and analyst forecasts play? Those are important questions whether or not you ever trade an ICC-based strategy.

## Let's Get Started

The next modules work through ICC systematically. We'll start with valuation theory: the residual income model, how it connects to expected returns, and how to derive ICC from it. Then implementation: getting data from WRDS, computing ICC numerically, handling the practical complications. Then empirical validation: do ICC estimates vary sensibly across stocks? Do they predict returns? How do they compare to alternative expected return measures?

By the end, you'll have working code for computing ICC and a deep understanding of what it measures, what assumptions it requires, and how well it works as an expected return proxy. That's valuable knowledge for anyone doing empirical asset pricing research.

Let's go.


