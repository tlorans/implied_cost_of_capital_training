# Residual Income Model (RIM)

## Why Another Valuation Model?

You already know the dividend discount model: price equals the present value of dividends. So why do we need the residual income model?

Two reasons. First, many firms don't pay dividends, or pay erratic dividends that don't reflect value. Second—and this is the real reason—the RIM converges faster. You don't have to forecast cash flows out to infinity and hope your terminal value calculation isn't garbage. The RIM front-loads value into near-term forecasts.

That's worth understanding. Let's see how it works.

## Clean Surplus Accounting: The Foundation

The whole model rests on one accounting identity. It's called **clean surplus relation**, and it says:

$$
B_t = B_{t-1} + E_t - D_t
$$

where $B_t$ is book equity, $E_t$ is earnings, and $D_t$ is dividends.

What does this mean? Book value today equals book value yesterday, plus what you earned, minus what you paid out. Everything flows through the income statement—nothing bypasses it to go directly to equity. That's "clean surplus."

Is this true in practice? Mostly. There are some exceptions (comprehensive income, foreign currency adjustments), but for practical purposes, it's close enough. And it's theoretically exact if you interpret earnings the right way.

Now, why do we care? Because this identity lets us rewrite the dividend discount model in terms of earnings and book values instead of dividends. Watch.

## From Dividends to Residual Income

Start with the dividend discount model:

$$
P_0 = \sum_{t=1}^{\infty} \frac{E[D_t]}{(1+r)^t}
$$

Now substitute the clean surplus relation. Solve for dividends: $D_t = E_t - (B_t - B_{t-1})$. Plug that in, do some algebra (I'll spare you the details), and you get:

$$
P_0 = B_0 + \sum_{t=1}^{\infty} \frac{E[RI_t]}{(1+r)^t}
$$

where **residual income** is defined as:

$$
RI_t = E_t - r \cdot B_{t-1}
$$

What's going on here? Residual income is earnings minus a charge for the book equity employed. It's the earnings left over after paying investors for their capital. If the firm earns exactly the cost of capital on book equity, residual income is zero and the stock is worth book value. If it earns more, residual income is positive and the stock trades at a premium to book.

This is just accounting manipulation—no new economics. But it changes everything about how we implement the model.

## Why This Is Useful

Here's the key insight: **residual income tends to zero faster than dividends**.

Why? Because residual income measures *abnormal* earnings—the difference between what the firm actually earns and what it should earn given its book equity. In competitive markets, abnormal profits get competed away. High ROE attracts entry. Low ROE triggers exit or restructuring. Over time, ROE reverts to the cost of capital, so residual income fades.

Dividends, by contrast, can grow forever if the firm is growing. You have to forecast them out decades and then slap on a terminal value. That terminal value often dominates the valuation—which means your valuation is really just a guess about the growth rate 20 years out.

With the RIM, near-term forecasts matter more. The terminal value is smaller. Your valuation is less sensitive to crazy assumptions about the distant future.

That's the practical advantage. Now let's see how to implement it.

## The Two-Stage RIM (Claus-Thomas Specification)

In practice, we need to make the model finite. The standard approach—used by Claus and Thomas (2001) and many others—is a two-stage model.

**Stage 1: Explicit forecast period.** Use analyst forecasts of earnings for the next few years (say, $t = 1$ to $T$, where $T$ is typically 3 to 5 years).

**Stage 2: Terminal value.** After year $T$, assume residual income grows at a constant rate $g$ forever.

The valuation formula becomes:

$$
P_0 = B_0 + \sum_{t=1}^{T} \frac{E[RI_t]}{(1+r)^t} + \frac{RI_{T+1}}{(r - g)(1+r)^T}
$$

where $RI_{T+1} = RI_T \cdot (1 + g)$ is the residual income in year $T+1$.

Now you solve for $r$ such that this equation holds given the observed price $P_0$. That $r$ is your ICC.

## The Devil Is in the Assumptions

Let's be honest: this model is only as good as its inputs. And there are three big assumptions you have to make.

### Assumption 1: Analyst Forecasts Are Reasonable

You're using analyst earnings forecasts for years 1 through $T$. Are they any good?

Sometimes yes, sometimes no. Analysts are systematically optimistic about growth stocks. They're slow to cut numbers. They herd. You know this. So what do you do?

There's no perfect answer. You can use consensus forecasts and hope the errors average out. You can adjust for known biases. Or you can use your own forecasts—but then you're doing fundamental analysis, not extracting market-implied returns.

The point is: garbage in, garbage out. If the earnings forecasts are wrong, your ICC estimate is wrong.

### Assumption 2: Terminal Growth Rate $g$

After year $T$, you assume residual income grows at rate $g$ forever. What should $g$ be?

Here's the standard argument: in the long run, firms can't earn abnormal profits. Competition drives ROE toward the cost of capital. So residual income should decay to zero, not grow. That suggests $g \leq 0$.

But there's a counterargument: even if ROE reverts to $r$, nominal book equity grows with inflation. So residual income should grow at the inflation rate. If inflation is 2%, set $g = 0.02$.

This is the **inflation-anchored growth** assumption, and it's what most researchers use. Claus and Thomas, for instance, use $g$ equal to the median long-run inflation forecast.

Does it matter? Oh yes. If you set $g = 0$ instead of $g = 0.03$, the terminal value changes dramatically, and so does your ICC estimate. This assumption is not innocuous.

### Assumption 3: Book Value Is Meaningful

The model starts with $P_0 = B_0 + \text{stuff}$. You're anchoring value to book equity. Is that reasonable?

For banks, maybe. For manufacturers, usually. For tech companies with massive intangible assets that aren't capitalized? Not so much. If book value is wildly understated because of R&D or acquired goodwill or whatever, the model is going to have a hard time.

You can adjust for this—capitalize R&D, adjust for off-balance-sheet assets, etc. But each adjustment introduces noise. There's no free lunch.

## What Really Matters Here

I want to emphasize something. The math is trivial. The accounting manipulations are clever but mechanical. What matters—what determines whether your ICC estimate is useful—is the quality of your assumptions.

Are the analyst forecasts reasonable? Is the terminal growth rate sensible? Is book value a meaningful anchor? Get these wrong and your ICC is nonsense, no matter how many decimal places you report.

This is a general point about valuation models. They're all sensitive to assumptions. The RIM is no exception—though it's arguably less sensitive than the dividend discount model because the terminal value is smaller.

But don't kid yourself. You're not extracting some pure, assumption-free measure of expected returns. You're making a bunch of assumptions and seeing what discount rate makes the numbers work. Be clear about what you're assuming and why.

## Example Calculation

Let's make this concrete. Suppose:
- Current price: $P_0 = 50$
- Current book value: $B_0 = 30$
- Forecasted earnings: $E_1 = 4$, $E_2 = 4.5$, $E_3 = 5$
- Terminal growth: $g = 0.03$ (3% inflation)
- Forecast horizon: $T = 3$ years

We need to find $r$ such that the RIM equation holds.

First, compute book values using clean surplus (assume no dividends for simplicity, or back them out from payout ratios):
$$
B_1 = B_0 + E_1 - D_1
$$

Then compute residual income for each year:
$$
RI_t = E_t - r \cdot B_{t-1}
$$

Finally, solve:
$$
50 = 30 + \frac{RI_1}{1+r} + \frac{RI_2}{(1+r)^2} + \frac{RI_3}{(1+r)^3} + \frac{RI_3 \cdot 1.03}{(r - 0.03)(1+r)^3}
$$

This is a nonlinear equation in $r$. You solve it numerically. Try $r = 0.10$, compute the right-hand side, see if it equals 50. If not, adjust $r$ and iterate.

The ICC is whatever value of $r$ makes the equation balance.

## Bottom Line

The residual income model is a practical tool for estimating the ICC. It's theoretically equivalent to the dividend discount model but converges faster, making it more reliable for finite-horizon forecasts.

But—and this is crucial—it's not magic. Your estimate is only as good as your inputs: the analyst forecasts, the terminal growth assumption, and the quality of book equity as a measure of invested capital.

Use the model. But don't trust it blindly. Check your assumptions. Run sensitivity analysis. And remember: the precision is illusory. A 10% ICC is not fundamentally different from 10.5%. Don't over-interpret small differences.