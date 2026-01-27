# Getting Started

In this chapter, we introduce the implied cost of capital (ICC): a forward-looking expected return estimate obtained by solving a valuation model for the discount rate. The goal is to understand why ICC exists, how it differs from historical-return approaches, and what families of ICC methods the literature uses.

```{note}
We use *expected return* and *cost of equity* interchangeably when the context is equity valuation.
```

## What are expected returns?

Expected returns represent the compensation investors demand for bearing risk and for the time value of money. Expected returns are central to almost every major financial decision:

- **Valuation:** They serve as the discount rate to convert expected future cash flows into present value.
- **Capital budgeting:** Firms use them as hurdle rates to evaluate whether projects create shareholder value.
- **Portfolio optimization:** Investors use them to construct efficient portfolios that maximize return for a given level of risk (Markowitz, 1952).

Gross returns are defined as: 

$$R_{t+1} = \frac{P_{t+1} + D_{t+1} - P_t}{P_t}$$

where $P_t$ is the price at time $t$, $P_{t+1}$ is the price at time $t+1$, and $D_{t+1}$ is the dividend paid between $t$ and $t+1$. The expected return is the conditional expectation of future returns given information available at time $t$:

$$E_t[R_{t+1}] = \frac{E_t[P_{t+1} + D_{t+1}] - P_t}{P_t}$$

The cost of equity is the expected return required by investors to hold a firm's equity. It reflects compensation for time value of money and risk. This is the discount rate used to value future cash flows from equity:

$$P_t = E_t\left[\sum_{s=1}^{\infty} \frac{X_{t+s}}{(1 + r_e)^s}\right]$$

where $X_{t+s}$ are the expected future cash flows to equity (e.g., dividends, earnings, residual income) and $r_e$ is the cost of equity (or expected return).

Yet **expected returns are not observable**, so every empirical approach must pick a proxy. In the following sections, we discuss two common historical approaches.

## Two common historical approaches

There is no shortage of models that explain expected returns (Cochrane, 2011): macroeconomic models, behavioral theories, and factor models. But in practice, most applied work still relies on historical returns—either directly (sample averages) or indirectly (factor models estimated from past data).

### Historical mean returns

A natural proxy is the sample mean of realized returns: 

$$\hat{E}[R] = \frac{1}{N} \sum_{t=1}^{N} R_t$$

It was long a standard recommendation in practice (Harris and Marston, 1992). But it comes with a practical drawback: the estimate can be dominated by noise, requiring long windows to become stable (Elton, 1999).

```python
# 1) download prices
# 2) compute returns
# 3) compute sample mean + rolling mean
```
### Factor models

Factor models impose structure: expected returns are tied to exposures to a small set of systematic risks. The CAPM is the canonical example (Sharpe, 1964; Lintner, 1965; Mossin, 1966): the only priced risk is the market excess return, and the key object is beta, typically estimated from historical return regressions:

$$E[R_i] = R_f + \beta_i (E[R_m] - R_f)$$

where $\beta_i = \frac{Cov(R_i, R_m)}{Var(R_m)}$.

Factor models can reduce some measurement error relative to individual mean returns, but they still depend on historical estimation (betas, factor premia), and results are sensitive to implementation choices. Despite these issues, the CAPM remains a widely taught benchmark (e.g., Berk and DeMarzo, 2013).

```python 
# 1) estimate beta via regression
# 2) plug beta into CAPM expected return formula
```

Empirical asset pricing introduced additional factors—size (Banz, 1981), value (Fama and French, 1992), momentum (Jegadeesh and Titman, 1993), investment (Titman et al., 2004), profitability (Novy-Marx, 2013):

$$E[R_i] = R_f + \beta_{i,m}(E[R_m] - R_f) + \beta_{i,SMB}E[SMB] + \beta_{i,HML}E[HML] + ... $$

These models are powerful in many applications, yet expected return estimates can remain noisy even in multi-factor settings (Fama and French, 1997).

```python 
# 1) load factor returns
# 2) estimate betas
# 3) compute expected returns using factor premia
```

## A Forward-looking alternative: Implied Cost of Capital (ICC)


Historical-return approaches estimate expected returns from the time series of realized returns. ICC flips the direction. Instead of estimating expected returns from past returns, we infer the discount rate that makes today’s price consistent with expected future payoffs.

This is the “reverse valuation” idea that underlies ICC methods such as Gebhardt et al. (2001), Claus and Thomas (2001), Easton (2004), and Ohlson and Juettner-Nauroth (2005).


### ICC in one equation 

Most ICC methods start from a valuation identity with price on the left-hand side and discounted expected payoffs on the right-hand side, then solve for $r$:

$$P_t = E_t\left[\sum_{s=1}^{\infty} \frac{X_{t+s}}{(1 + r)^s}\right]$$

where $X_t$ could be dividends, earnings, residual income, or abnormal earnings growth, depending on the model. The unknown $r$ is the implied cost of equity. ICC methods differ less in “philosophy” than in the choice of (i) the payoff definition $X_t$ and (ii) the terminal value / long-run assumptions.

### Dividend Discount models (DDM)
DDM methods forecast dividends (or payout ratios) and impose assumptions about long-run growth.

$$P_t = \sum_{t=1}^{n} \frac{D_t}{(1+r)^t} + \frac{P_n}{(1+r)^n}$$

with terminal value $P_n$ often computed using the Gordon Growth Model:

$$P_n = \frac{D_{n+1}}{r - g}$$

where $g$ is the long-run growth rate.

- Malkiel (1979) uses the classic constant-growth logic and highlights sensitivity to the long-run growth assumption; Malkiel (1970) proposes mean reversion of growth toward GDP growth.
- Harris (1986) links ICC to dividend yield plus long-term growth forecasts (using IBES forecasts).
- Gordon and Gordon (1997) assume a finite growth horizon.
- Botosan and Plumlee (2002) incorporate multi-year dividend forecasts and a target price.
- Pastor et al. (2008) use explicit short-run forecasts, mean-revert growth toward macro anchors, and set a terminal structure consistent with “value-irrelevant” growth beyond a horizon.

```python
Figure placeholders

DDM timeline / cash flow forecast diagram

Sensitivity plot: long-run growth vs ICC
```

### Clean surplus accounting and earnings-based models
When dividends are irregular or absent (common in modern equity markets), clean surplus accounting provides an alternative. The dividend discount model can be restated in terms of earnings and book values (Ohlson, 1995):

$$P_t = B_t + E_t\left[\sum_{s=1}^{\infty} \frac{E_{t+s} - r B_{t+s-1}}{(1 + r)^s}\right]$$

where $B_t$ is the book value of equity at time $t$, and $E_{t+s}$ are expected earnings. The clean surplus identity states that changes in book value equal earnings minus dividends:

$$B_{t} = B_{t-1} + E_{t} - D_{t}$$



This motivates models that are often easier to operationalize with accounting data:
- Residual Income Model (RIM): price equals book value plus discounted residual income; residual income depends on earnings minus $r$ times beginning book value (Kothari et al., 2016).
- Gebhardt et al. (2001): forecast ROE explicitly for a few years, then transition ROE toward an industry benchmark.
- Claus and Thomas (2001): market-level ICC with explicit forecast structure and a long-run residual income growth assumption tied to inflation.
- Abnormal Earnings Growth (AEG): anchor value on capitalized earnings and adjust for abnormal earnings growth (Easton, 2004; Ohlson and Juettner-Nauroth, 2005).

```python
Figure placeholders

Clean surplus identity diagram

RIM vs AEG: “valuation hook” comparison
```

### Refinements and extensions in the literature

We now turn to several refinements and extensions proposed in the ICC literature.
These focus on (i) reducing reliance on long-run growth assumptions, (ii) adapting methods for higher-frequency estimation, (iii) addressing forecast errors and analyst bias, and (iv) replacing analyst forecasts with model-based forecasts.

#### The long-run growth problem

Almost all ICC implementations must confront a key modeling choice: what happens in the long run. Long-run growth assumptions can have large effects on ICC estimates (Easton, 2007).

A major line of work tries to reduce reliance on an exogenous long-run growth assumption:
- Easton et al. (2002): estimate ICC and long-run growth jointly at the portfolio level via an iterative regression approach.
- Ashton and Wang (2013): regression-based approach grounded in linear information dynamics.
- Nekrasov and Ogneva (2011): extend joint estimation logic toward firm-level ICC via a multi-step procedure.

```python
Figure placeholder

Iteration schematic: guess r → compute LHS → regress → update r
```

#### From annual to daily ICC 

Many early ICC studies produce annual estimates and sometimes restrict to December fiscal year ends. Daske et al. (2006) show how to adapt methods for daily ICC estimation by constructing a “virtual” book value at time $t$ and aligning forecasted earnings with the fraction of the fiscal year remaining.

```python
Figure placeholder

Calendar alignment: fiscal year end vs estimation date
```

#### Forecast errors and analyst bias

ICC depends on forecasts. A second set of refinements focuses on the quality of earnings forecasts:
- Easton and Sommers (2007): analysts are optimistic in the U.S., biasing ICC upward; propose aggregation choices (e.g., value-weighting) to reduce bias effects in market measures.
- Guay et al. (2011): analysts react sluggishly to price information, generating predictable measurement error; propose portfolio-based adjustments.
- Larocque (2013) and Mohanram and Gode (2013): model forecast errors using observable firm characteristics; results differ on whether corrections improve association with realized returns.

```python
Figure placeholder

Forecast error adjustment pipeline
```

#### Replacing analysts: model-based earnings forecasts

Rather than correcting analyst forecasts, some papers replace them:
- Hou et al. (2012): pooled cross-sectional earnings forecast models using accounting predictors.
- Allee (2011): time-series earnings forecasts.
- Li and Mohanram (2014): earnings persistence (EP) and residual income (RI) forecasting models that allow asymmetric persistence for losses vs profits.


## Summary table of ICC implementations

| Reference | Valuation Model | Period | Earnings forecasts data |Long-term growth assumption |
|------:|:-----:|:------|------:|------:|
| Malkiel (1979)     | DDM     | 1966-1977     | Value Line     | Value Line/GDP growth rate |
| Harris (1986)     | DDM     | 1982-1984     | IBES     | Long-term growth forecasts from IBES |
| Gordon and Gordon (1997)    | DDM     | 1985-1991     | IBES     | Long-term growth forecasts from IBES |
| Botosan and Plumlee (2002)    | DDM     | 1986-2000    | Value Line     | Use of target price from Value Line |
| Pastor et al. (2008)    | DDM     | 1981-2002    | IBES     | Growth after year 15 is value irrelevant |
| Claus and Thomas (2001)    | RIM     | 1985-1998    | IBES     | Risk-free rate minus three percent |
| Gebhardt et al. (2001)  | RIM     | 1979-1995    | IBES     | Median industry ROE |
| Easton (2004)  | AEG     | 1981-1999    | IBES     | No growth in abnormal earnings |
| Ohlson and Juettner-Nauroth (2005)  | AEG     | 1984-1998    | IBES     | Risk-free rate minus three percent |
| Easton et al. (2002)  | RIM     | 1981-1998    | IBES     | Estimated simultaneously with the ICC |
| Ashton and Wang (2013)  | RIM     | 1975-2006    | IBES     | Estimated simultaneously with the ICC |
| Nekrasov and Ogneva (2011)  | RIM     | 1980-2007    | IBES     | Estimated simultaneously with the ICC |
| Allee (2011)  | AEG     | 1981-2010    | Time-series model     | No growth in abnormal earnings |
| Hou et al. (2012)  | DDM, RIM, AEG     | 1968-2008    | Cross-sectional model     | According to the respective valuation model |
| Li and Mohanram (2014)  | RIM, AEG     | 1969-2012    | EP and RI model    | According to the respective valuation model |



## Key Takeaways

```{note}
Historical mean returns and factor models are easy baselines, but expected return estimates can be dominated by sampling error.
```


```{note}
ICC methods are forward-looking: they infer discount rates from prices and forecasts via a valuation identity.
```


