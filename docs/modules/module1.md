# Setup & Philosophy

## What This Course Is About

This course teaches you how to test whether markets are mispricing assets. Not with vague hand-waving about "inefficiency" or untestable claims about what will happen in 2050. With falsifiable hypotheses you can test with data today.

Here's the basic problem. People claim markets misprice all sorts of things: climate risk, analyst forecasts, earnings quality, whatever the latest story is. They'll tell you which stocks to avoid and which to buy. They'll show you scary scenarios decades out. They'll charge you fees to manage your money based on these claims.

But they won't give you testable predictions. They won't tell you what should happen to returns *now* if their theory is right. They won't give you a way to prove them wrong.

This course fixes that.

We'll build a rigorous framework for testing mispricing claims. You'll learn:
- How to extract future return estimates from market prices using the implied cost of capital (ICC)
- How to build earnings forecast models that might contain information the market misses
- How to form portfolios and test whether your signals predict returns
- How to distinguish risk from mispricing (these are not the same thing)
- How to decompose returns to see when they actually materialize
- How to apply all of this to test claims about climate risk

By the end, you'll have a complete toolkit for evaluating mispricing claims empirically. You'll implement everything in Python from scratch. And you'll understand the limitations—where these tests work and where they don't.

Most importantly, you'll be able to cut through the nonsense. When someone tells you markets misprice climate risk or any other factor, you'll know how to test whether they're right.

## The Problem: Claims Without Tests

Walk into any asset management pitch these days. They'll tell you about market inefficiencies. Behavioral biases. Climate risk. ESG. AI disruption. Whatever sells.

The pitch always follows the same pattern:
1. Here's a risk or factor the market supposedly misses
2. Here's a projection showing it will matters (by 2050, naturally)
3. Here's our portfolio that exploits it

What's missing? Any way to check if they're right *before* 2050.

This is not science. You can't falsify a 2050 prediction with 2026 data. You can make any claim you want, collect fees for decades, and retire before anyone can prove you wrong.

Real science requires testable predictions. If markets misprice climate risk today, that should show up in returns *now*—not 25 years from now. If analyst forecasts contain information the market misses, high ICC stocks should outperform starting today. If your earnings model captures mispricing, it should predict returns out-of-sample.

These are all testable. You can be proven wrong. That's the standard we're going to hold ourselves to.

## Risk vs. Mispricing: The Confusion That Drives Everything

Here's the most important conceptual distinction in this course: **risk and mispricing are not the same thing**.

**Risk** (rewarded) means systematic exposure to factors that affect returns. In equilibrium, assets with more risk should earn higher returns. If you identify a risk factor, you should *buy* assets exposed to it (to earn the risk premium), not sell them.

**Mispricing** means the market hasn't correctly valued future cash flows. If you identify mispricing, you should *sell* overvalued assets and *buy* undervalued assets to capture the correction.

These lead to opposite investment strategies. You can't have it both ways.

But the industry constantly conflates them. They call everything "risk" because it sounds scientific and justifies regulation. But their recommended strategies are all about shorting or avoiding certain exposures—which only makes sense if you think those assets are overvalued.

Climate is the perfect example. The industry calls it "climate risk." They show stress tests and VaR calculations. But they recommend underweighting high-carbon firms. That's a mispricing claim, not a risk claim. If climate risk were truly priced, high-carbon firms would earn higher returns (to compensate for the risk), and you'd want to overweight them.

This confusion is not accidental. It's marketing. "Risk management" sounds respectable. "We think we're smarter than the market" does not.

This course will make you rigorous about the distinction. When you test a claim, you'll know whether you're testing for risk or mispricing. And you won't let people get away with muddling them together.

## The Tools: ICC, Earnings Forecasts, and Return Tests

We'll use three main tools to test for mispricing:

**1. Implied Cost of Capital (ICC):** This is the discount rate that makes current prices equal to forecasted cash flows. It's just an internal rate of return (IRR) calculation. But it's useful because it summarizes market expectations in a single number.

If the market undervalues a stock, its ICC will be high (you need a high discount rate to justify the low price given the forecasts). If the market overvalues a stock, its ICC will be low. By sorting stocks on ICC and measuring returns, you can test whether the market systematically messes up.

**2. Earnings Forecast Models:** Analysts provide earnings forecasts, but they make systematic mistakes. They're optimistic about growth stocks, slow to cut numbers, influenced by conflicts of interest. You can build statistical models using historical fundamentals that might forecast earnings better—or at least differently—than analysts.

If your model predicts earnings that differ from analyst forecasts, and if the market prices in analyst forecasts more than yours, you've found potential mispricing. You can test it by forming portfolios based on your model-based ICC.

**3. Portfolio Formation and Return Decomposition:** The ultimate test is returns. If you claim high ICC stocks are undervalued, form a portfolio that goes long high ICC and short low ICC. Measure returns. If you're right, you make money. If you're wrong, you lose money.

But don't stop there. Decompose when the returns happen. If it's mispricing, returns should concentrate at information events (earnings announcements, policy changes). If it's risk, returns should accrue steadily over time.

## The Application: Climate Risk

Climate is the perfect testbed for these methods because:

**1. The claims are everywhere.** Every asset manager has a climate strategy. Every regulator talks about climate stress tests. The claims about climate mispricing are loud and persistent.

**2. The claims are confused.** Nobody clearly distinguishes climate risk from climate mispricing. They use the words interchangeably. This creates opportunity for rigorous analysis.

**3. The claims are mostly untestable (on purpose).** Show me a climate strategy that makes predictions about 2026 returns. You won't find many. They all project to 2050.

**4. We can test it.** We have data on carbon emissions. We can compute ICC by carbon exposure. We can form portfolios. We can decompose returns around climate policy announcements. We can see if high-carbon firms actually underperform, and if so, whether it's concentrated at information events.

This is the culminating application of the course. Once you know how to test climate mispricing, you can test anything. ESG, AI exposure, geopolitical risk—whatever the next story is. The method generalizes.

## What You'll Actually Learn

Here's the course roadmap:

**Module 2-3: Understanding ICC**
- What ICC measures (and what it doesn't)
- Why ICC ≠ expected returns
- The residual income model (the workhorse for computing ICC)
- How to think about analyst forecasts and their biases

**Module 4: Implementation**
- Getting data (IBES, CRSP, Compustat)
- Computing ICC numerically
- Handling missing data, negative earnings, convergence failures
- All the messy details the papers hide

**Module 5: Testing Whether ICC Predicts Returns**
- Forming portfolios sorted on ICC
- Measuring returns (overlapping, equal-weighted vs. value-weighted)
- Statistical tests and economic significance
- What the evidence actually shows

**Module 6: Risk or Mispricing?**
- The Rusticus (2019) test: decomposing returns over time
- Earnings announcement vs. non-announcement returns
- Why this distinction matters
- What we learn about analyst forecast information

**Module 7: Building Your Own Forecasts**
- Why not just use analyst forecasts?
- Building earnings forecast models from fundamentals
- The Easton-Monahan (2016) approach
- Testing whether model-based ICC predicts returns
- Evidence on market inefficiency

**Module 8: Application to Climate Risk**
- The confusion about climate risk in finance
- Building testable hypotheses about climate mispricing
- Computing ICC by carbon exposure
- Testing whether high-carbon firms underperform
- Decomposing returns around climate events
- What the evidence actually shows (spoiler: it's mixed)

By the end, you'll have implemented all of this in Python. You'll have working code you can apply to any mispricing claim.

## The Philosophy: Empiricism Over Storytelling

Here's the mindset for this course:

**1. Testable predictions.** If you can't test it with data today, it's not science. Be suspicious of claims that only matter decades from now.

**2. Out-of-sample tests.** In-sample fits are meaningless. Anyone can find patterns in historical data. The test is whether it works on new data you haven't seen yet.

**3. Economic significance over statistical significance.** A t-statistic of 3 is nice, but if the return is 50 basis points per year, who cares? Focus on whether the magnitude matters economically.

**4. Honest about uncertainty.** You won't always get clean answers. Returns are noisy. Models have errors. Markets change. Be honest about what you know and don't know.

**5. Skeptical of industry claims.** The asset management industry has incentives to manufacture complexity and claim special insights. Most of what they sell is repackaged beta or luck. Demand evidence.

**6. Build it yourself.** Don't trust black boxes. Implement the models from scratch so you understand what they actually do. This is the only way to develop real intuition.

This is not a "get rich quick" course. Mispricing, if it exists, is small, time-varying, and hard to exploit profitably. Transaction costs matter. Limits to arbitrage matter. Even if you find something, it might not survive real-world trading.

But that's fine. The goal is to think clearly about mispricing claims and test them rigorously. If you can do that, you're ahead of 95% of the industry.

## Prerequisites

You should have:
- **Finance background:** Understand present value, risk and return, basic asset pricing. Know what CAPM is (even if you don't believe it works).
- **Python skills:** Can write functions, use polars or pandas, make plots. If you've done intro Python for data science, you're ready.
- **Statistics basics:** Understand regression, hypothesis testing, standard errors. We'll run tests and you need to interpret them.
- **Skepticism:** Don't believe everything you read in academic papers or industry reports. Question assumptions. Demand evidence.

You don't need:
- PhD-level math. The models are algebraically simple.
- Experience with trading systems. We'll explain the practical details.
- Prior knowledge of ICC. That's what we're teaching.

## How to Use This Course

Work through the modules in order. Each builds on the previous.

Don't just read—code. Download the data (we'll provide sources), implement the models, replicate the results. Then modify something and see what changes. That's how you learn.

When something doesn't make sense, stop and figure it out. If the ICC estimate looks weird, debug it. If the portfolio loses money, understand why. The point is to develop intuition, not memorize formulas.

Be skeptical. Question the assumptions. Run sensitivity tests. Ask: does this make economic sense? Would I actually trade this? What could go wrong?

And remember: most mispricing claims are wrong or overstated. That's fine. Learning to identify the rare cases where markets actually do misprice assets requires first learning to dismiss the 99% of claims that are nonsense.

## The Honest Truth

Let me be blunt about what this course will and won't do.

**What you'll learn:**
- How to test mispricing claims rigorously
- How to implement ICC and earnings forecast models
- How to form portfolios and measure returns properly
- How to distinguish risk from mispricing
- How to apply this framework to climate or any other claimed inefficiency

**What you won't learn:**
- A guaranteed strategy to beat the market
- The "secret" to picking stocks
- How to get rich quick

**What the evidence shows:**
- Some mispricing exists, especially related to analyst forecasts and fundamentals
- It's small (a few percent per year at most)
- It's time-varying (works sometimes, not always)
- It's concentrated in small, illiquid stocks where transaction costs matter
- It might not survive real-world implementation

**What this means for you:**
- Use these tools to evaluate claims critically
- Don't expect magic—markets are pretty efficient
- If you do find something, be realistic about economic significance
- The main value is in thinking clearly, not in generating alpha

This is a course in empirical asset pricing. The goal is to teach you the scientific method applied to finance. Test claims. Demand evidence. Be honest about what you find.

That's a valuable skill, whether or not you beat the market.

## Let's Get Started

The next modules will walk through the framework step by step. We'll start with the theory (what is ICC? how does it relate to expected returns?), move to implementation (computing ICC from real data), then to testing (do ICC-sorted portfolios outperform?), and finally to application (testing climate mispricing claims).

By the end, you'll have a complete toolkit for evaluating any mispricing claim empirically.

Ready? Let's go.
- **Alternative models:** Dividend discount, abnormal earnings growth, ohlson
- **Data and implementation:** Working with analyst forecasts, financial statements, prices
- **Cross-sectional analysis:** ICC and stock returns
- **Portfolio strategies:** Building ICC-based portfolios
- **Advanced topics:** Bias correction, time variation, risk management

We'll move fast but thoroughly. By the end, you'll have a complete ICC toolkit and the understanding to use it intelligently.

Let's go.


