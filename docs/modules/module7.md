# Earnings Forecast Models, Valuation, and the Research Feedback Loop

## Motivation

Empirical asset pricing often relies on earnings expectations as a proxy for firms’ future cash flows. Traditionally, these expectations are taken from analyst forecasts (e.g. IBES). However, a large literature documents that analyst forecasts are neither unbiased nor uniformly superior to simple statistical models, especially at longer horizons or for certain firm types.

Rather than taking any single forecasting approach as given, this project treats earnings forecasts as model outputs that can be systematically evaluated and improved.

The key idea is to embed earnings forecasts inside a valuation identity, and then use both realized earnings and market prices as external discipline devices.

## The valuation anchor

Let $\hat{e}_{i,t+h}$ denote a model-based forecast of firm $i$’s earnings at time $t+h$, made at time $t$. These forecasts are mapped into a valuation equation (e.g. residual income or equivalent present-value representation) which defines an implied discount rate $k_{i,t}$ such that: 

$$ P_{i,t} = V(\{\hat{e}_{i,t+h}\}_{h\geq 1}, k_{i,t}) $$

where $P_{i,t}$ is the market price of firm $i$ at time $t$, and $V(\cdot)$ is the valuation function.

Crucially, this step is not meant to “estimate expected returns” in isolation, but to translate earnings expectations into a price–forecast consistency object.

## The dual evaluation criteria 

The framework evaluates an earnings forecast model along two complementary dimensions.

### Forecast accuracy (cash-flow discipline)

Forecasts are evaluated out-of-sample using standard metrics:
- Mean Squared Forecast Error (MSFE)
- Horizon-specific performance (e.g. short-term vs long-term
- Directional accuracy (sign prediction)

This answers the narrow question: Does the model improve conditional expectations of future earnings?

### Valuation and market coherence (price discipline)

The same forecasts are evaluated through their implied discount rates:
- Are implied rates economically plausible?
- Are they stable outside genuine information events?
- Do they generate predictable return patterns?

This answers a broader question: Do the forecasts behave as market-relevant expectations when embedded in prices?

Importantly, return predictability is not automatically interpreted as “alpha”. It may reflect:
- market underreaction to information,
- systematic forecast errors that are later corrected,
- or misspecification of valuation assumptions.

## The research feedback loop

Putting the pieces together yields the following iterative loop:
1. Specify an earnings forecast model
2. Map forecasts into valuation and implied discount rates
3. Evaluate forecast accuracy
4. Evaluate implied discount rate behavior
5. Diagnose failures (forecast error vs price adjustment)
6. Refine the forecast model

This loop allows incremental improvement of earnings models while maintaining consistency with financial valuation identities.

## Interpretation discipline

A central principle of the framework is interpretation discipline:
- Forecast accuracy alone is not sufficient.
- Return predictability alone is not sufficient.
- Both must be considered jointly.

The framework therefore treats earnings forecasting, valuation, and asset pricing as a single connected system, rather than separate exercises.