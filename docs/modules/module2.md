# What is the Implied Cost of Capital?

## The Basic Idea

You observe three things: price, forecasted cash flows, and time. You want to know one thing: what discount rate connects them? That's the implied cost of capital (ICC).

Stock price is \$100. Analysts forecast earnings, dividends, or book value. What discount rate makes the present value of those forecasts equal \$100? Solve for that rate. Done. You have the ICC.

It's mechanically simple. It's an IRR calculation:

$$
P_0 = \sum_{t=1}^{\infty} \frac{E[CF_t]}{(1 + r_{ICC})^t}
$$

Here $P_0$ is today's price, $E[CF_t]$ are forecasted cash flows, and $r_{ICC}$ is what you're solving for. The discount rate that makes this equation hold—that's the ICC.

So far, so straightforward. But now ask: what does this number mean? What are you actually measuring?

That's where it gets interesting.

## What Does ICC Measure?

The standard story goes like this: if markets are efficient and everyone shares the analysts' forecasts, then ICC equals the true expected return. Stocks with high ICC are risky. Stocks with low ICC are safe. Cross-sectional variation in ICC reflects risk differences.

Nice story. But it only works if two things are true:

**First**, prices have to be right. The market correctly values future cash flows given available information. No systematic errors. No behavioral biases. No slow incorporation of information.

**Second**, the forecasts have to be right—or at least, everyone has to agree with them. If analysts say earnings will grow 10%, the market prices in 10%, and 10% is what investors expect.

If both hold, ICC is expected return. It's what investors require to hold the stock. Done.

But what if prices are wrong? What if the stock is undervalued?

Then you need a *higher* discount rate to make the present value of good forecasts equal a too-low price. The ICC rises. But not because the stock is riskier. Because it's cheap.

Conversely, if the stock is overvalued, you need a *lower* discount rate to justify the high price. ICC falls. Not because the stock is safer. Because it's expensive.

So ICC captures two things: expected returns (risk) and mispricing (valuation errors). You can't tell them apart just by looking at the ICC. That's the identification problem.

## The Identification Problem

Say you compute ICC for every stock. You sort them into portfolios. High ICC stocks earn 15% next year. Low ICC stocks earn 8%. The spread is 7%. Statistically significant. Economically large.

Great! But why did high ICC stocks outperform?

**Story 1: Risk.** High ICC stocks were riskier. Investors demanded higher returns. They got them. This is just the usual risk-return tradeoff. Nothing surprising here. CAPM works. Markets are efficient. 

**Story 2: Mispricing.** High ICC stocks were undervalued. The market priced them too low relative to their fundamentals. Over time, prices corrected. The stocks went up. This is mispricing reversal. Markets are inefficient (at least temporarily). High ICC signaled cheap stocks. You should tilt toward high ICC—that's where the alpha is.

Both stories explain the return spread. Both fit the data. But they have opposite implications for investment strategy.

If it's risk, you don't have an edge. You're just earning a risk premium. Returns are compensation for bearing risk. No free lunch.

If it's mispricing, you do have an edge. You found a signal the market hasn't incorporated. Exploit it before it disappears.

So which is it?

You can't tell from the ICC alone. The number is the same whether it's risk or mispricing. You need additional evidence.

## Evidence for Mispricing

Here's what makes us think mispricing matters—maybe even dominates.

**First**: timing. If high ICC stocks outperform because they're risky, returns should accrue gradually over time. Risk premia get paid out steadily. You hold the stock, you bear the risk, you earn the premium. Every day, every month.

But that's not what happens. A huge chunk of the ICC return spread shows up at earnings announcements. Firms announce earnings, the market updates, prices jump. High ICC stocks jump up more than low ICC stocks. Between announcements? Not much happens.

This is hard to square with a risk story. Why would risk premia concentrate at earnings announcements? Risk doesn't suddenly appear for three days per quarter and then vanish. Risk is continuous.

Mispricing, though, fits perfectly. The market underestimates earnings for high ICC stocks. Analysts forecast X, but the market seems skeptical. Then earnings come in at X (or better), and the market says "oh, I guess analysts were right." Price jumps to reflect the new information. That's mispricing correction, not risk compensation.

**Second**: where it works. If ICC captured risk, the return spread should be similar across all stocks. Risk is risk. Doesn't matter if you're big or small, liquid or illiquid.

But the ICC spread is much larger among small, illiquid stocks. Precisely where arbitrage is hard. Precisely where mispricing is known to persist because sophisticated investors can't easily trade away the errors.

Again: hard to explain with risk. Easy to explain with mispricing.

None of this proves ICC is pure mispricing. It could still be a mix. But the evidence strongly suggests mispricing is part of the story—maybe the dominant part.

## So What Is ICC?

Here's the honest answer: ICC is what the market's pricing in. It's the discount rate implied by price and forecasts. 

What it measures depends on whether markets are efficient:

- If markets are efficient and forecasts are shared, ICC = expected return = risk.
- If markets misprice stocks or react slowly to information, ICC = expected return + mispricing signal.

You don't get to choose which story is true. The market chooses.

Most of the evidence points toward the second story. Markets misprice stocks, especially around information events. ICC picks this up because it's mechanically backed out of prices. High ICC stocks tend to be undervalued. They outperform when the market corrects.

Does that mean ICC is a pure mispricing signal? No. Risk probably matters too. High ICC stocks might genuinely be riskier on average. The return spread likely reflects both risk and mispricing.

Can you use ICC to make money? Maybe. The spreads are there. But they're small, they're time-varying, and transaction costs matter. We'll test all this in later modules.

For now, just understand what ICC is and isn't. It's an implied discount rate. It predicts returns (we'll see the evidence). But why it predicts returns—risk, mispricing, or both—that's an empirical question. Not a definitional one.

## What's Next

You now understand what ICC is: a discount rate implied by price and forecasts. You understand the identification problem: it could measure risk, mispricing, or both. And you've seen preliminary evidence suggesting mispricing matters.

In the next module, we'll dig into exactly how to compute ICC using the residual income model. This is the workhorse for ICC estimation. You'll see the algebra, understand the assumptions, and learn where the numbers come from.

Then we'll implement it. Get data. Write code. Handle all the messy details—missing values, negative earnings, convergence failures.

After that: portfolio tests. Does ICC actually predict returns out of sample? How big are the spreads? Are they statistically and economically significant?

Let's get started.
