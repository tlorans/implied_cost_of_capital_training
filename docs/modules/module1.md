# Setup & Philosophy

## What This Course Is About

This course teaches you how to build and implement investment strategies using the implied cost of capital (ICC). Not just the theory—though we'll cover that—but the actual practice of computing ICC estimates, analyzing them, and using them to make investment decisions.

Here's the deal. You'll learn:
- How to extract ICC estimates from market prices and analyst forecasts
- How different ICC models work and when to use which one
- How to implement these models in Python from scratch
- How to use ICC for stock selection, portfolio construction, and risk management
- What works, what doesn't, and why

By the end, you'll have a working toolkit for ICC-based investing. You'll understand the models well enough to modify them for your own purposes. And you'll know the limitations—where ICC works and where it fails.

## Why ICC-Based Strategies?

Traditional quantitative strategies use historical returns, price momentum, value metrics like P/E or P/B, or factor exposures. These all work to some degree. So why bother with ICC?

**Because ICC is forward-looking.** Historical returns are noisy and backward-looking. By the time you measure them, the information is stale. ICC uses current prices and forecasts to estimate expected returns right now. When market conditions change—and they always do—ICC adapts immediately.

**Because ICC combines price and fundamentals.** Value metrics like P/B look at one snapshot. ICC integrates the entire forecast trajectory and asks what discount rate makes it consistent with the price. It's a more complete measure of value.

**Because academic evidence suggests it works.** Dozens of papers show that stocks with high ICC tend to outperform stocks with low ICC. The effect persists after controlling for standard factors. It's not a slam dunk—nothing in finance is—but the evidence is there.

That said, ICC strategies are not magic. They have problems:
- They depend on analyst forecasts, which are often biased
- They're sensitive to terminal value assumptions
- They assume some market inefficiency to generate alpha
- They can go through long periods of underperformance

We'll confront these issues head-on. You need to understand what you're getting into.

## Why Python?

Python is the lingua franca of quantitative finance. If you want to do anything serious with data—and ICC strategies are data-intensive—you need Python.

Specifically, you'll use:
- **pandas** for data manipulation (cleaning analyst forecasts, computing book values, aligning datasets)
- **numpy** for numerical computations (solving for ICC, matrix operations)
- **scipy** for optimization (ICC is usually solved with a root-finding algorithm)
- **matplotlib/seaborn** for visualization (plotting ICC distributions, returns, strategy performance)
- **statsmodels** for regression analysis (testing ICC predictive power)

If you're not comfortable with Python, that's fine. We'll walk through the code step-by-step. But you should have basic programming skills—loops, functions, reading documentation. If you've never programmed, start there first.

The goal is not just to use off-the-shelf libraries. We'll implement the models from scratch so you understand what's happening under the hood. Then you can modify them, debug them, and trust them when real money is on the line.

## The Philosophy: Build It Yourself

There's a difference between using a black box and understanding how it works. In this course, we'll build the models ourselves.

Why? Three reasons.

**First, you learn by doing.** Reading a paper is one thing. Coding the model, debugging it, seeing what breaks—that's when you actually understand it. You'll discover edge cases the paper didn't mention. You'll see why certain assumptions matter and others don't.

**Second, you can't trust black boxes.** Academic papers are notoriously vague about implementation details. Commercial data vendors don't tell you how they compute things. If you want to know what's really going on—and you should—you have to build it yourself.

**Third, you'll want to customize it.** Maybe you want to use different terminal growth assumptions. Maybe you want to adjust for analyst bias. Maybe you want to combine ICC with other signals. You can't do any of that if you're stuck with someone else's code.

So we'll start from first principles. Take the model equations, translate them into Python, test them on real data, and see what happens.

## What You'll Actually Do

Each module combines theory, implementation, and application. Here's the pattern:

1. **Concept:** What's the model? What assumptions does it make? What's it supposed to measure?

2. **Math:** The key equations. Not a full derivation—you can read the papers for that—but enough to understand what you're computing.

3. **Code:** Implementing the model in Python. We'll walk through it line by line. You'll see how to handle missing data, numerical issues, edge cases.

4. **Data:** Working with real analyst forecasts, prices, and financial statements. Data is messy. You'll learn how to clean it.

5. **Results:** Does it work? We'll compute ICC for real stocks, analyze the cross-section, test predictive power, build portfolios.

6. **Critique:** What are the limitations? When does the model break down? How sensitive are the results to assumptions?

By the end of each module, you'll have working code you can apply immediately.

## The Honest Truth About ICC Strategies

Let me be blunt. ICC-based strategies are not a guaranteed path to riches. They're a tool. Sometimes they work, sometimes they don't.

**What the academic evidence shows:** On average, over long periods, stocks with high ICC outperform stocks with low ICC. The effect is economically significant—maybe 5-8% per year difference between high and low ICC portfolios. It persists after controlling for size, value, and momentum.

**What the academic evidence doesn't show:** That you can implement this strategy profitably in real time. Academic tests are in-sample or use simple backtests. They ignore transaction costs, liquidity, capacity, changing analyst coverage, data availability in real time.

**What we'll do:** We'll implement the strategies as realistically as possible. Use point-in-time data. Account for survivorship bias. Think about transaction costs. Test out-of-sample. And be honest about when it works and when it doesn't.

The goal is not to sell you on ICC strategies. It's to teach you how to build and evaluate them so you can decide for yourself.

## Prerequisites

You should have:
- **Finance background:** Understand present value, discount rates, basic asset pricing. Know what CAPM is, even if you don't believe it.
- **Python skills:** Can write functions, use pandas DataFrames, make plots. If you've taken an intro to Python for data science, you're fine.
- **Statistics basics:** Understand regression, hypothesis testing, standard errors. We'll do empirical tests, so you need to interpret them.

You don't need:
- PhD-level math. The models are algebraically simple.
- Experience with trading systems. We'll explain the practical stuff.
- Prior knowledge of ICC. That's what we're teaching.

## How to Use This Course

Work through the modules in order. Each one builds on the previous.

Don't just read the theory—run the code. Download the data (we'll provide sources), implement the models, replicate the results. Then modify something and see what changes. That's how you learn.

If something doesn't make sense, stop and figure it out. If the ICC estimate looks weird, debug it. If the strategy loses money, understand why. The point is to develop intuition, not just memorize formulas.

And be skeptical. Question the assumptions. Run sensitivity tests. Ask: does this make economic sense? Would I actually trade this with real money?

## Let's Get Started

The next modules will cover:
- **What is ICC?** The theory and intuition
- **Residual Income Model (RIM):** The workhorse model for ICC estimation
- **Alternative models:** Dividend discount, abnormal earnings growth, ohlson
- **Data and implementation:** Working with analyst forecasts, financial statements, prices
- **Cross-sectional analysis:** ICC and stock returns
- **Portfolio strategies:** Building ICC-based portfolios
- **Advanced topics:** Bias correction, time variation, risk management

We'll move fast but thoroughly. By the end, you'll have a complete ICC toolkit and the understanding to use it intelligently.

Let's go.


