# Getting Started

In this chapter, we introduce the implied cost of capital (ICC): a forward-looking expected return estimate obtained by solving a valuation model for the discount rate. The goal is to understand why ICC exists, how it differs from historical-return approaches, and what families of ICC methods the literature uses.

We use *expected return* and *cost of equity* interchangeably when the context is equity valuation.

## Why expected returns are hard

Expected returns matter in many asset pricing and corporate finance settings—from portfolio allocation (Markowitz, 1952) and factor timing (Li et al., 2014) to studying determinants of the cost of equity (Botosan, 1997) or outcomes shaped by it (Frank and Shen, 2016). Yet expected returns are not observable, so every empirical approach must pick a proxy.

There is no shortage of models that explain expected returns (Cochrane, 2011): macroeconomic models, behavioral theories, and factor models. But in practice, most applied work still relies on historical returns—either directly (sample averages) or indirectly (factor models estimated from past data).

The core tension is simple:
- historical returns are easy to use, but noisy in finite samples (Elton, 1999);
- ICC is harder to build, but forward-looking because it uses prices and forecasts.

## Two common historical approaches

### Historical mean returns

A natural proxy is the sample mean of realized returns. It is conceptually clean and was long a standard recommendation in practice (Harris and Marston, 1992). But it comes with a practical drawback: the estimate can be dominated by noise, requiring long windows to become stable (Elton, 1999).

This creates problems in exactly the places where researchers and practitioners want local expected returns:
- event studies (pre/post windows are short)
- portfolio choice (mean estimates lead to extreme weights; Best and Grauer, 1991).

```python
# 1) download prices
# 2) compute returns
# 3) compute sample mean + rolling mean
```
### CAPM and factor model

Factor models impose structure: expected returns are tied to exposures to a small set of systematic risks. The CAPM is the canonical example (Sharpe, 1964; Lintner, 1965; Mossin, 1966): the only priced risk is the market excess return, and the key object is beta, typically estimated from historical return regressions.

Factor models can reduce some measurement error relative to individual mean returns, but they still depend on historical estimation (betas, factor premia), and results are sensitive to implementation choices. Despite these issues, the CAPM remains a widely taught benchmark (e.g., Berk and DeMarzo, 2013).

```python 
# 1) estimate beta via regression
# 2) plug beta into CAPM expected return formula
```

Empirical asset pricing introduced additional factors—size (Banz, 1981), value (Fama and French, 1992), momentum (Jegadeesh and Titman, 1993), investment (Titman et al., 2004), profitability (Novy-Marx, 2013). These models are powerful in many applications, yet expected return estimates can remain noisy even in multi-factor settings (Fama and French, 1997).

```python 
# 1) load factor returns
# 2) estimate betas
# 3) compute expected returns using factor premia
```

## Why ICC: the discount-rate perspective

A useful way to understand ICC is through the “discount-rate variation” view of stock prices. Shiller (1981) argues that prices fluctuate too much to be justified by dividend changes alone, which implies that discount rates must vary over time. This view fits naturally with the return predictability literature and with approaches that try to infer discount rates from prices.

Historical-return approaches estimate expected returns from the time series of realized returns. ICC flips the direction.

Instead of estimating expected returns from past returns, we infer the discount rate that makes today’s price consistent with expected future payoffs.

This is the “reverse valuation” idea that underlies ICC methods such as Gebhardt et al. (2001), Claus and Thomas (2001), Easton (2004), and Ohlson and Juettner-Nauroth (2005).


### ICC in one equation 

Most ICC methods start from a valuation identity with price on the left-hand side and discounted expected payoffs on the right-hand side, then solve for $r$:

$$P_0 = \sum^T_{t=1} \frac{E[X_t]}{(1+r)^t} + \frac{E[TV_T]}{(1+r)^T}$$

where $X_t$ could be dividends, earnings, residual income, or abnormal earnings growth, depending on the model. The unknown $r$ is the implied cost of equity. ICC methods differ less in “philosophy” than in the choice of (i) the payoff definition $X_t$ and (ii) the terminal value / long-run assumptions.

### ICC method families 

#### Dividend Discount models (DDM)
DDM methods forecast dividends (or payout ratios) and impose assumptions about long-run growth.
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

#### Clean surplus accounting and earnings-based models
When dividends are irregular or absent (common in modern equity markets), clean surplus accounting provides an alternative. The dividend discount model can be restated in terms of earnings and book values (Ohlson, 1995). This motivates models that are often easier to operationalize with accounting data:
- Residual Income Model (RIM): price equals book value plus discounted residual income; residual income depends on earnings minus $r$ times beginning book value (Kothari et al., 2016).
- Gebhardt et al. (2001): forecast ROE explicitly for a few years, then transition ROE toward an industry benchmark.
- Claus and Thomas (2001): market-level ICC with explicit forecast structure and a long-run residual income growth assumption tied to inflation.
- Abnormal Earnings Growth (AEG): anchor value on capitalized earnings and adjust for abnormal earnings growth (Easton, 2004; Ohlson and Juettner-Nauroth, 2005).

```python
Figure placeholders

Clean surplus identity diagram

RIM vs AEG: “valuation hook” comparison
```

#### The long-run growth problem (and how papers handle it)

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

In this course: we will implement at least one analyst-based ICC and one model-based ICC so you can see how the inputs change the output.


#### Summary table of ICC implementations

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

### Key Takeaways

```{note}
The Gordon Growth Model is best suited for mature companies with stable dividend growth rates.
```

```{warning}
Always validate your assumptions about growth rates - they significantly impact the results!
```

## Studies Using the Implied Cost of Capital

Historical-return cost of capital proxies are noisy (Elton, 1999; Fama and French, 1997), which makes it harder to detect relations in regressions. ICC estimates are typically much less volatile (Lee et al., 2009), so they have been used broadly to study determinants and consequences of the cost of equity.

### Governance and disclosure
This literature links disclosure quality, regulation, and internal controls to the cost of capital:
- firm-level voluntary disclosure and cost of capital (Botosan, 1997),
- disclosure measures across channels and contexts (Botosan and Plumlee, 2002; Francis et al., 2005),
- internal control deficiencies (Ashbaugh-Skaife et al., 2009),
- country-level enforcement and cross-listing effects (Hail and Leuz, 2006, 2009).

### Other accounting and corporate finance settings
ICC has been used to study taxation, earnings quality attributes, restatements, diversification, and asset illiquidity (e.g., Dhaliwal et al., 2005; Francis et al., 2004; Hribar and Jenkins, 2004; Hann et al., 2013; Ortiz-Molina and Phillips, 2014). Frank and Shen (2016) revisit investment–cost-of-capital relations using ICC rather than CAPM proxies.

### Risk and expected return
Several papers examine whether ICC behaves like a risk-based expected return proxy (Pastor et al., 2008; Chava and Purnanadam, 2010) and whether different ICC measures line up with standard risk proxies (Botosan et al., 2011).

### Asset pricing and predictability

ICC is less common in classic asset pricing than in accounting, but key contributions include:
- cross-sectional relations with betas and firm characteristics (Lee et al., 2009),
- market return predictability using market ICC (Li et al., 2013),
- international evidence (Cooper and Sarkar, 2016),
- implied value premium predictability (Li et al., 2014),
- anomaly evaluation ex-ante vs ex-post (Tang et al., 2014).

### Investment strategies

Quintile sorts on ICC have been studied as implementable strategies, with mixed results once transaction costs are considered (Esterer and Schröder, 2014).


### Key Takeaways

```{note}
Historical mean returns and factor models are easy baselines, but expected return estimates can be dominated by sampling error.
```


```{note}
ICC methods are forward-looking: they infer discount rates from prices and forecasts via a valuation identity.
```

```{warning}
ICC estimates can be highly sensitive to long-run assumptions (terminal value, growth, payout) and to forecast quality.
```

