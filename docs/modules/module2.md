# What is the Implied Cost of Capital 

## What Are We Actually Measuring?

Here's the basic idea. You observe a stock price, say \$100. Analysts forecast the company will pay dividends and grow. You ask: what discount rate makes those forecasts equal the $100 price? That discount rate is the implied cost of capital (ICC).

It's just an IRR calculation:

$$
P_0 = \sum_{t=1}^{\infty} \frac{E[CF_t]}{(1 + r_{ICC})^t}
$$

where $P_0$ is today's price, $E[CF_t]$ are the forecasted cash flows, and $r_{ICC}$ is what we're solving for.

Simple enough. But what does this number actually mean? That question turns out to be harder than it looks.

## Two Very Different Questions

Asset pricing and valuation ask fundamentally different questions, and it's crucial to keep them separate.

**The asset pricing question:** Given the stock's risk, what return should I expect to earn in equilibrium? We use models—CAPM, Fama-French, whatever—to tell us:

$$E[R] = R_f + \beta \times \text{risk premium}$$

The logic: if you know the risk, you know the return. The price follows.

**The valuation question:** Given the stock's price and some forecasts of cash flows, what return am I getting? This is the ICC calculation. 
The logic runs backwards: if you know the price and the cash flows, you can back out the return.

Now, if markets are efficient and everyone agrees on the cash flow forecasts, these two numbers should be the same. The ICC should equal the equilibrium expected return. That's the textbook story.

But here's the problem: markets aren't always efficient, and people don't always agree on forecasts. So the ICC and the expected return can differ. Sometimes by a lot.

## Why Expected and Implied Returns Diverge

Let's be concrete about when and why these numbers come apart.

**Mispricing.** If the stock is overpriced—say, because of a bubble—the ICC will be too low. You're solving 

$$\text{high price} = \sum CF_t / (1+r)^t$$

so you get a low $r$. But the true expected return, accounting for an eventual correction, is higher. Conversely, if the stock is underpriced, the ICC is too high.

The ICC does not know about mispricing. It takes the price as given and asks what return is baked into that price. It's a mechanical calculation, not an economic prediction.

**Forecast errors.** Analysts are human. They make mistakes. More problematically, they make *systematic* mistakes. Analysts tend to be optimistic, especially about growth stocks. They're slow to cut forecasts when things go south. They herd.

If you feed optimistic forecasts into the ICC calculation, you get an optimistic (low) discount rate. But what return will you actually earn? That depends on whether the optimistic forecasts come true. Probably not.

So here's a key insight: the ICC tells you what return you'd get *if the forecasts were correct*. Not what return you'll actually get.

**Time-varying risk premia.** Even in efficient markets, expected returns vary over time. Risk premia rise in recessions. They fall in booms. That's fine—it's just economic variation in risk and risk appetite.

The ICC picks up this variation. In a recession, risk premia rise, stock prices fall, and the ICC spikes. In a boom, the opposite. So the ICC is not a constant; it's a time-varying measure of market conditions.

Is that a bug or a feature? Depends what you're using it for. If you want a stable cost of capital for capital budgeting, time variation is a nuisance. If you're studying how risk premia move over time, it's exactly what you want.

## Expected Return: A Thought Experiment

Think of it this way. You're considering buying a stock. You want to know: what return can I expect? 

The **asset pricing approach** says: look at the stock's beta (or whatever risk measures you believe in). Compare to other stocks with similar risk. That tells you the expected return in equilibrium. If the stock is priced correctly, you'll earn that return.

The **ICC approach** says: look at the current price and the analyst forecasts. Solve for the return that makes them consistent. That's the ICC.

These are different animals. The asset pricing approach makes a claim about equilibrium and risk. The ICC approach is agnostic—it just inverts the present value formula.

When should they agree? When (1) markets are efficient, (2) everyone agrees on the forecasts, and (3) those forecasts are correct on average. Strong assumptions. Often violated.

## Connecting ICC to Value Investing

The divergence between ICC and model-based expected returns is where things get interesting—and potentially profitable.

Suppose your asset pricing model says a stock should have an expected return of 10%. But the ICC, calculated from the current (depressed) price, is 15%. What's going on?

Either the stock is mispriced (undervalued), or your model is wrong, or the analyst forecasts are too pessimistic. If you believe the first explanation, you have a potential value opportunity.

Value investors love this. They're always looking for stocks where the implied return (ICC) exceeds the required return (expected return from models). That gap is the margin of safety, the potential alpha.

The same logic works in reverse. If the ICC is 6% but your model says expected returns are 10%, something's off. Maybe the stock is overpriced. Maybe the analyst forecasts are too rosy. Either way, be careful.

## What Should You Do With This?

Here's my view. The ICC is not the expected return. It's an estimate of the return implied by prices and forecasts. It's useful precisely because it doesn't impose equilibrium assumptions.

Use the ICC to:
- **Measure market conditions.** When average ICC is high across stocks, the market is demanding high returns. Risk premia are elevated. That's useful information.
- **Spot potential mispricings.** When ICC and model-based expected returns differ sharply, something interesting is happening. Investigate.
- **Estimate cost of capital forward-looking.** Historical average returns are noisy and backward-looking. The ICC uses current prices and forecasts. It's not perfect, but it's often better than the alternatives.

But don't confuse the ICC with the true expected return. They're the same only under strong assumptions—assumptions that are often wrong.

The ICC is an input to your analysis, not the final answer. Use it wisely.