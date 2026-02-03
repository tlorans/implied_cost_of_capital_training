# Mispricing vs. Risk: What's Actually Going On?

## The Central Question

You formed ICC portfolios. High ICC stocks outperformed low ICC stocks. Great. But what does that mean?

Two possibilities:

**1. Risk:** High ICC stocks are riskier. The return premium is compensation for bearing that risk. This is the asset pricing theorist's view. ICC is a risk factor, or it proxies for risk factors. The market is working as it should.

**2. Mispricing:** High ICC stocks are undervalued. Analyst forecasts signal good fundamentals, but the market hasn't caught on yet. The return premium is mispricing correction—alpha, not risk compensation. This is the value investor's view.

These are fundamentally different stories. They have different implications for market efficiency, for portfolio strategy, for cost of capital. So which is it?

This is not an easy question to answer. But there's a clever test, developed by Rusticus (2019), that gets at it. The key insight: risk and mispricing generate returns in different ways over time.

Let me show you how it works.

## The Problem: Both Stories Predict the Same Thing

Here's why this is hard. Suppose you find that high ICC stocks earn higher returns. That's consistent with both stories.

**Risk story:** High ICC stocks have higher expected returns because they're riskier. You measure returns, find they're higher, and conclude: yep, risk is priced.

**Mispricing story:** High ICC stocks are undervalued. Over time, prices converge to fundamentals. You measure returns, find they're higher, and conclude: yep, mispricing corrected.

Both stories fit the same fact. How do you distinguish them?

You need to look at *when* the returns happen. Not just whether high ICC stocks outperform, but *how* that outperformance accumulates over time.

## The Key Insight: Risk and Mispricing Have Different Time Signatures

Think about how returns accrue.

**Risk-based returns:** These accrue continuously. If you hold a risky stock for a year, you earn the risk premium gradually, day by day. Some days are up, some are down, but on average you're getting compensated for risk every day you hold it.

**Mispricing correction:** This happens when information arrives. If the market undervalues a stock because it underestimates future earnings, the correction happens when those earnings get revealed. Prices jump at earnings announcements. The rest of the time, nothing much happens.

That's the difference. Risk returns are smooth. Mispricing returns are lumpy.

If ICC captures risk, returns should be spread evenly across the year. If ICC captures mispricing, returns should concentrate at information events—specifically, earnings announcements.

That's testable.

## The Setup: Decomposing Returns Over Time

Here's what you do. Take your ICC hedge portfolio: long high ICC stocks, short low ICC stocks. Measure its annual return, say 4%. That's the total return.

Now break that 4% into two pieces:

**1. Earnings announcement return ($R^{EA}$):** The return during earnings announcement windows. Use a 3-day window around each quarterly announcement. Four quarters, so 12 trading days total.

**2. Non-announcement return ($R^{NON}$):** The return on all the other days. That's 240 out of 252 trading days.

The total return is just the sum: $R^{BH} = R^{EA} + R^{NON}$.

Simple accounting. Now ask: what fraction of the total return happens during earnings announcements?

$$
\text{Earnings Announcement Share} = \frac{R^{EA}}{R^{BH}}
$$

## What Should You Expect?

If ICC captures risk, you'd expect the announcement share to be small. Earnings announcements are 12 out of 252 trading days, or about 5%. If returns accrue evenly over time, roughly 5% of the annual return should happen during announcements.

Maybe a bit more, because earnings announcements are high-volatility days. But not *much* more. If you see 10-15%, that's still consistent with risk.

If ICC captures mispricing, you'd expect the announcement share to be large. Mispricing corrections happen when information arrives. Earnings announcements are the most important information events. You might see 30%, 40%, even 50% of the annual return during announcements.

That would be hard to explain with a risk story. Risk doesn't take a vacation for 240 days and then show up for 12 days.

## The Math: Why Mispricing Predicts This Pattern

Let me be more precise. Suppose the observed price has two components:

$$
P_{i,t} = FV_{i,t}(r_i) + MP_{i,t}
$$

where $FV_{i,t}(r_i)$ is fundamental value discounted at the true expected return $r_i$, and $MP_{i,t}$ is the mispricing component. Positive $MP$ means overvalued, negative means undervalued.

The ICC is the IRR that equates price to forecasted cash flows. If there's mispricing, the ICC will be distorted:

$$
ICC_{i,t} = r_i + \phi \cdot MP_{i,t}
$$

where $\phi < 0$. Overpriced stocks have low ICC. Underpriced stocks have high ICC.

Now, the realized return next year is:

$$
R_{i,t+1} = r_i + \Delta MP_{i,t+1} + \varepsilon_{i,t+1}
$$

where $\Delta MP_{i,t+1}$ is the change in mispricing (if it corrects, this is negative for overvalued stocks), and $\varepsilon$ is news about cash flows or discount rates.

Here's the key: if mispricing corrects at earnings announcements, then $\Delta MP$ happens during announcement windows. The return decomposition becomes:

$$
R_{i,t+1}^{EA} \approx \Delta MP_{i,t+1}
$$

$$
R_{i,t+1}^{NON} \approx r_i + \varepsilon_{i,t+1}
$$

So the ICC hedge portfolio return is:

- **Announcement days:** You get the mispricing correction. This is large if $MP$ is large.
- **Non-announcement days:** You get the risk premium plus noise. This averages to close to zero for a long-short portfolio (risk premia are similar across stocks).

Bottom line: if ICC sorts on mispricing, most of the hedge return should show up at announcements.

## The Test: What Rusticus (2019) Did

Rusticus ran this test on the standard ICC models (CT, OJ, GLS, etc.). Here's the procedure:

1. **Each month:** Sort stocks into deciles by ICC
2. **Form hedge portfolio:** Long decile 10 (high ICC), short decile 1 (low ICC)
3. **Hold for one year** and measure returns
4. **Decompose returns:** Separate announcement days from non-announcement days
5. **Compute the earnings announcement share**

Do this for the full sample (1981-2013). Average across all portfolio formations. What do you find?

## The Result: Mispricing Wins

The earnings announcement share is **43-53%**, depending on the ICC model.

Read that again. About half of the annual hedge portfolio return happens during earnings announcements. That's 12 trading days out of 252.

If returns were evenly distributed, you'd expect 5%. You're seeing 50%. That's a 10x concentration.

This is not consistent with risk. Risk premia don't concentrate like that. You can't tell a story where high ICC stocks are riskier, but only during earnings announcements. Risk is about exposure to aggregate shocks, and those happen all the time, not just on 12 specific days.

This *is* consistent with mispricing. The market undervalues high ICC stocks (analysts see strong earnings coming, but the market is skeptical). When earnings get announced and confirm the analysts were right, prices adjust. The mispricing corrects. That's when you make your money.

## What About the Other 50%?

Good question. If half the return is at announcements, what's the other half?

Some of it is drift—post-earnings-announcement drift, to be specific. Prices don't adjust fully at the announcement. They keep moving in the same direction for weeks afterward. That's a well-known anomaly.

Some of it is other information events—analyst revisions, news, guidance updates. Not all information arrives at quarterly earnings.

And some of it is noise. Returns are volatile. Even if the expected return outside announcements is zero, realized returns won't be.

But the key point is: the concentration at announcements is the smoking gun. It tells you what's driving the ICC premium.

## Why This Matters

This result changes how you interpret ICC.

If ICC measured risk, you'd think of the ICC premium as compensation for bearing systematic risk. You'd expect it to persist as long as that risk is priced. You'd use ICC to estimate cost of capital, because it reflects the return investors require.

But if ICC captures mispricing, the premium is not about risk. It's about analyst forecasts containing information the market hasn't incorporated yet. The premium might disappear if:
- Analysts get worse at forecasting
- The market gets better at reacting to forecasts
- The information in forecasts becomes more widely known and arbitraged away

You can still trade on it—buy high ICC stocks, short low ICC stocks, capture the mispricing correction. But you're doing value investing, not harvesting a risk premium. And your edge depends on the market staying inefficient.

For cost of capital estimation, this is trickier. If you estimate ICC for a firm and get, say, 12%, you can't just use that as the cost of capital. Part of that 12% might be mispricing. The true expected return (what investors require going forward) might be 10%. You'd overestimate the cost of capital and reject good projects.

## Limitations: What This Test Doesn't Prove

Let me be clear about what this test shows and what it doesn't.

**What it shows:** The ICC hedge portfolio return concentrates at earnings announcements. That's a fact. It's hard to reconcile with a pure risk story.

**What it doesn't show:** That ICC has *nothing* to do with risk. Maybe ICC loads on both risk and mispricing. The announcement test tells you mispricing is important, but it doesn't rule out risk entirely.

Also, this test focuses on the cross-section. It asks: why do high ICC stocks outperform low ICC stocks? But ICC also varies over time. Average ICC is high in recessions, low in booms. That time-series variation might still reflect risk premia, even if the cross-sectional variation is driven by mispricing.

Finally, the test assumes mispricing corrects at earnings announcements. That's plausible, but not the only possibility. Maybe mispricing corrects at other events, or gradually over time. The test would understate the mispricing component in those cases.

Still, 50% announcement share is striking. Even if there are caveats, the evidence leans heavily toward mispricing.

## Practical Implications: What Should You Do?

If you're using ICC for research:
- **Don't assume ICC equals expected returns.** It doesn't. It's a mix of expected returns, mispricing, and forecast errors.
- **Be careful with cost of capital estimation.** ICC might overstate or understate the true cost of capital depending on whether the firm is mispriced.
- **Use ICC to study mispricing.** This is where it shines. ICC tells you what the market is pricing in relative to analyst forecasts. Deviations are informative.

If you're building a trading strategy:
- **High ICC stocks are likely undervalued.** The evidence suggests the premium is mispricing, not risk. So you're doing value investing.
- **Watch earnings announcements.** That's when you make your money. You might even concentrate your strategy around those dates.
- **Be aware of limits to arbitrage.** Mispricing persists because it's costly or risky to arbitrage away. If you're trading this, you're taking on those costs and risks.

If you're estimating cost of capital for capital budgeting:
- **Don't rely on ICC alone.** Supplement with other methods (factor models, historical returns, comparables). ICC is an input, not the answer.
- **Adjust for mispricing if you can.** If you think your firm is undervalued, the ICC will be too high. Adjust downward. If overvalued, adjust upward. This is judgment, not science.

## The Bottom Line

Rusticus (2019) provides some of the cleanest evidence on what ICC actually measures. By showing that ICC hedge portfolio returns concentrate at earnings announcements, the paper makes a strong case that ICC-return predictability is driven by mispricing correction, not cross-sectional variation in expected returns.

This doesn't mean ICC is useless. It's a valuable measure of what the market is pricing in. But it's not a clean measure of expected returns. It's contaminated by mispricing and forecast errors.

Use it wisely. Know what it's telling you. And don't confuse the ICC with the cost of capital.
