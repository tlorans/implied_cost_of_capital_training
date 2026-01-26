# Getting Started

This module covers the fundamental concepts of implied cost of capital.

## Motivation and Outline 

Expected return estimates are used in many asset pricing and corporate finance studies. These applications cover diverse areas, from portfolio allocation problems (Markowitz, 1952) through factor timing (Li et al., 2014) to studying variables that influence the expected return (for example, Botosan, 1997) or variables that are influenced by the expected return (for example, Frank and Shen, 2016). 

Since the expected return is such a central topic in finance, there is a large variety of theories and models that attempt to explain it (see Cochrane, 2011, for a summary). These include macroeconomic theories (modelling parts of the economy, such as consumption and aggregate risk, and general equilibrium models), behavioral finance models, and factor models. 

Despite this wide range of models, the methodology used in most applied finance research settings, as well as in practice, is based on historic stock returns. Indeed, for many years the recommended practice was to use the historic mean return as a proxy for the expected return (Harris and Marston, 1992). While this proxy is an unbiased estimate of the true expected return, it contains a large amount of noise (Elton, 1999), which can make it unsuitable for specific applications. Also, a long estimation period is necessary to obtain a reliable estimate (Elton, 1999). For example, event studies that compare the cost of equity before and after an event cannot use a long estimation period for the post-event estimate. In portfolio allocation problems, employing the historic mean return often leads to extreme allocation decisions due to their high volatility and measurement error (Best and Grauer, 1991). 


In comparison to using the historic average return, a factor model helps to reduce measurement error. It also reduces complexity by linking the expected return to the exposure to a limited number of factors, which represent systematic risks. The capital asset pricing model (CAPM) was the first factor model to be developed and it is based on work by Sharpe (1964), Lintner (1965) and Mossin (1966). It assumes that the only priced risk factor in the stock market is the market return above the risk-free rate. The epxected return of each stock can thus be determined by estimating the sensitivity of the respective stock's return toward the market return using a regression (this sensitivity is named beta). Therefore, this approach also relies on historic data and the estimation of beta is sensitivite toward the empirical implementation. Nevertheless, the CAPM is still the method taught in standard texbooks (for example, Berk and DeMarzo, 2013). 


The focus on two select methods to estimate the expected return may reflect the fact that for a long time, cash-flow estimates were deemed to be the more important driver in stock returns. This view has only shifted recently to the discount rate for firm's cash flows (Cochrane, 2011). A major break-through was the study by Shiller (1981), which finds that stock prices fluctuate too much to be explained by changes in dividends. Thus, the discount rate for these cash flows has to vary over time and should not be assumed to be constant. This invigorated the return predictability literature, which explires if future returns can be accurately predicted. 


Return predictability centers on market returns (see Koijen and Van Nieuwerburgh, 2011 and Cochrane 2011 for an overview of the literature) or, more recently on portfolios (Kelly and Pruitt, 2015). as such, they cannot be directly used to estimate the expected return of a single stock. The work in this area has substantially increased our understanding of the time-variance of expected returns as well as its economic drivers. Researchers have proposed various variables to predict stock market returns: financial ratios (for example, price-to-dividend and price-to-earnings), term and credit spread in bond yields, the consumption-wealth ratio, and macro-economic variables (Koijen and Van Nieuwerburgh, 2011). Also, return predictability is no longer seen as conflicting with the efficient market hypothesis (Fama, 1965, Fama, 1970), as asset pricing equilibrium models have merged that account for the time-variance in expected returns (Koijen and Van Nieuwerburgh, 2011). For example, Campbell and Cochrane (1999) develop a model with fluctuating risk aversion, Bansal and Yaron (2004) and Bansal et al. (2009) focus on fluctuating consumption risk. 


The disadvantages of methodologies implementing past returns to estimate expected returns has spawned a new string of literature which explores methods using a combination of current stock prices, accounting data, and earnings forecasts to compute expected returns (Gebhardt et al.2001, Claus and Thomas 2001, Easton 2004, Ohlson and Juettner-Nauroth 2005). This novel approach does not rely on time-series of stock returns but instead uses a valuation equation (such as a residual income model) with the current stock price on the left-hand side and the discounted expected earnings on the right-hand side. Then the equation is solved for the implied discount rate, which is termed the implied cost of capital (ICC).

This website explores different applications of the ICC, using Python. Especially in portfolio allocation problems, investors can benefit from the predictive power of the ICC, as it employs forward-looking earnings estimates. 

## Expected Returns Using Historical Data

Expected returns are a fundamental concept in finance (Elton, 1999) and a lot of effort is devoted to their estimation as they cannot be observed. 

### Historical mean return

The most intuitive method is to use the mean of a sample of historica returns. Indeed, this was previously the recommendation found in textbooks for practitionners (Harris and Marston, 1992). Even though the historic mean return is an unbiased estimated of the expected return, it suffers greatly from estimation error and statistical noise (Elton, 1999). Even as early as the 1950s, Markowitz (1952) recommends the use of a combination of the historic mean return and judgement. Frankfurter et al. (1971) and Barry (1974) caution against treating the mean historic return as the expected return. 

"""""Put example of retrieving and computing expected returns as average""""""

### The Capital Asset Pricing Model

The large estimation error of individual historical stock returns is somewhat mitigated by the use of a factor model model. A factor model assumes that every asset can be priced by its exposure to a limited set of factors. These factors represent systematic risks in the market. The first factor model to emerge was the CAPM (Sharpe 1964, Lintner 1965, Mossin 1966), which posits that there is only one relevant factor (the market risk premium) that explains stock returns. 

"""""" Example of CAPM model """""""""""

### Factor Models

Over time, more factors emerged in the literature. Banz (1981) proposes a size factor (based on the firm's market capitalization). Fama and French (1992) develop a three-factor model that includes the two aforementioned factors plus the book-to-market value factor. Jegadeesh and Titman (1993) discover the momentum factor. Further additions are the investment factor (Titman et al., 2004) and the profitability factor (Novy-Marx 2013). These factor models are well-suited in many applications in asset pricing and corporate finance. However, even Fama and French (1997) acknowledge that expected returns based on factor models still contain a large amount of statistical noise.

"""""" Example of Multi factors model """""""""""


### Key Takeaways

```{note}
The Gordon Growth Model is best suited for mature companies with stable dividend growth rates.
```

```{warning}
Always validate your assumptions about growth rates - they significantly impact the results!
```

## Implied Cost of Capital Methods

The term ICC was coined by Gebhardt et al. (2001). I use it to encompass all accounting-based valuation methods that use current stock prices and earnings forecasts in a valuation equation to solve for the discount rate. 

Strictly speaking, the ICC is the implied cost of equity capital but I will follow the literature and use the two terms synonymously. The idea to reverse engineer a valuation model to obtain the discount rate goes back much farther than the study by Gebhardt et al. (2001). 

### From Dividend Discount Model...

Malkiel (1979) uses a dividend discount model (DDM) in which the current price is equal to the current dividend times one plus the long-term growth rate divided by the ICC minus the long-term growth rate. As this method is very sensitive to the long-term growth rate, Malkiel (1970) also imlements a different approach in which the long-term growth rate exponentially declines to the gross domestic product (GDP) growth rate over a course of five years. He obtains the long-term growth rate in a dividend growth from Value Line's financial database. 

"""Chart Malkiel """"

In contrast, Harris (1986), who employs a DDM where the ICC equals the dividend yield plus the long-term growth forecast, obtains forecasts from the Institutional Broker's Estimate System (IBES). Gordon and Gordon (1997) also follow the DDM approach but assume a finite growth horizon. Botosan and Plumlee (2002) build on the DDM by using dividend forecasts for the following four years and the respective stock's target price from Value Line. 

""" Chart """"

The approach by Pastor et al. (2008) is a more recent refinement of the DDM. The authors use explicit earnings forecasts from IBES for the first three years. They compute the growth rate in earnings and mean-revert this growth rate to the sum of long-run real GDP growth rate and the long-run average rate of inflation, the latter of which is set to the implicit GDP deflator (estimated using historic data). Earnings for years four to 15 are forecasted using this growth rate. The terminal value in year 15 equals the forecasted earnings from year 16 divided by the ICC. Thereby, they assume that after year 15, any new investments earn zero economic profits. To calculate dividends, the uathors forecast the payout ratio as the most recent payout ratio for the first three years and then they interpolate the payout ratio to the steady-state payout ratio in year 15. The steady-state payout ratio is one minus the long-term growth rate over the ICC.

""" Charts Pastor """"

### ... to Clean Surplus Accounting 

Forecasting dividends can be challenging, especially when a firm has a history of not paying dividends (Kothari et al. 2016). To alleviate this issue, researchers developed valuation models that rely on "clean surplus accounting" (Ohlson 1995). With clean surplus accounting, the DDM can be restated in terms of earnings and changes in book values. One of these methods is the residual income model (RIM). This model equates the current stock price with book-value per share (BPS) and the sum of discounted residual income (Kothari et al., 2016). Residual income is defined as earnings per share (EPS) minus the ICC times BPS from the previous period. 

""" From Ohlson, diagram to explain """

Gebhardt et al. (2001) use a RIM in which they employ explicit earnings forecasts to compute return on equity (ROE) for the subsequent three years. From year four to 12, they linearly interpolate ROE to the median industry ROE. In comparison, Claus and Thomas (2001) compute the ICC on a market level (instead of on a firm level). They use up to five years of analysts' earnings forecasts and assume that the long-term growth rate in residual income equals the expected nominal inflation rate. The authors seet the nominal expected inflation rate equal to the nominal risk-free rate minus three percent (i.e. the nominal inflation rate is equal to the nominal risk-free rate minus the real risk-free rate).

The RIM uses book value of equity as a valuation hook and then adjusts this value according to future expected residual income (Easton, 2007). Next, I present two versions of the abnormal earnings growth model (AEG), which anchors the firm's value on capitalized earnings and then adjusts this value according to expected abnormal growth in earnings. Easton (2004) develops a modified price-eargnings-growth formula in which the growth in abnormal earnings is set to zero. Ohlson and Juettner-Nauroth (2005) transform the AEG model so that a short-term and a long-term growth rate in abnormal earnings can be set. 

### Long-term growth rate

The methods presented so far require the researcher to make an assumption about the long-term growth rate. This is a difficult choice which can have a large impact on the ICC (Easton, 2007). To circumvent this problem (Easton et al., 2002) propose to estimate the ICC and the long-term growth rate simultaneously for a portfolio fo firms. To this end, the authors restate the RIM as a regression equation and then obtain values for the ICC and the long-term growth rate from estimated regression coefficients. This procedure requires an iterative approach, as the ICC is needed for the computation of the left-hand side of the regression equation. Easton et al. (2002) set the ICC starting value to 12 percent (the historical market return in their sample) and then compare that value to the estimated value. If it differs, they use the new value to re-compute the left-hand side variable of the regression equation and re-run the regression. The procedure is repeated until there are no more significant changes in the ICC estimate.

""" chart """

Ashton and Wang (2013) also follow a regression approach but their underlying model is based on linear information dynamics (Ohlson 1990, Ohlson 1995, Feltham and Ohlson 1995, Feltham and Ohlson 1996). They regress expected earnings on current earnings, current book value of equity and last period's book value of equity (all variables are deflated by share price). This cross-sectional regression is performed for each year of the sample. From the estimated regression coefficients, the authors derive the ICC and the implied long-term growth rate. Their results are in line with the findings of other studies that estimate the ICC, albeit being at the lower end of the range.

Nekrasov and Ogneva (2011) extend the study of Easton et al. (2002) so that the ICC can be estimated on a firm level instead of only on a portfolio or market level. They employ a three-step procedure. First, they run a cross-sectional weighted-least squares regression with the sum of expected four-year earnings (including compounded dividends) over book value on the left-hand side and market-to-book value, risk variables (CAPM beta, size, market-to-book value, and momentum), and growth variables (expected long-term growth rate from IBEs, difference between industry ROE and company's forecasted ROE, and research and development expenses over sales) on the right-hand side (note that market-to-book value appears twice in the regression equation). This regression is run iteratively since an estimate of the ICC (which is one of the variables to be estimated through this regression) is reguired in the calculation of the left-hand side variable. Second, they use the estimated coefficients from the cross-sectional regression previously described to calculate the ICC and the implied growth rate on a market level. Finally, they compute the irm level ICC and growth rate using the residuals and the weights from the weighted-least squares regression above, the company's market-to-book value, the company's risk and growth characteristics, and the average ICC and growth rate estimates. 

### From Yearly to Daily ICC

The literature has also produced a number of refinements to existing methods. The studies mentioned so far estimate the ICC on a yearly basis, sometimes only for companies with a fiscal-year ending on December 31 (e.g. Easton et al., 2002). Daske et al. (2006) demonstrate how existing methods can be modified to allow for a daily ICC estimation. More specifically, they compute a virtual book value of equity at time $t$ (the point in time of the ICC estimation) using the firm's forecasted ROE. Then they adjust the company's forecasted earnings for the next fiscal year-end to reflect only the earnings from $t$ to the financial year-end (instead of the earnings from the last fiscal year-end to the upcoming fiscal year-end). In this way, the authors exclusively use current available information and the estimation is independent of the current date and the fiscal year-end of the company.

"""Chart"""


### Correcting Analysts' Biases in Earnings Forecasts

Easton and Sommers (2007) find that analysts' earnings forecasts tend to be too optimistic in the U.S., which leads to an upward bias in ICC estimates. They estimate this bias by comparing ICC estimates based on analysts to ICC estimates based on subsequently realized earnings. They find that this upward bias is 2.84% in their sample (1993-2004). The authors propose to value-weight ICC estimates when aggregating them to a portfolio or market level instead of equal-weighting the estimates since the optimism bias in smaller for larger firms.

Guay et al. (2011) also investigate the quality of analysts' earnings forecasts and discover that analysts tend to incorporate stock price performance too slowly. This results ina predictable meaasurement error of the ICC. To correct for this error, the authors propose to sort companies into 12 portfolios based on their past 12-month stock return. Then, for every company, the historical forecast error (up to the respective date) scaled by total assets is computed. Finally, the median historical forecast error of each portfolio is calculated and subsequently used to adjust the earnings forecasts for each firm.

The studies by Larocque (2013) and Mohanram and Gode (2013) look at a range of variables that could be correlated with analysts' forecast errors. Larocque (2013) builds on the framework of Ali et al. (1992), who also investigated whether analysts' forecast errors can be predicted with information available at a respective point in time. She augments the Ali et al. (1992) model by two variables so that in her cross-sectional regression, the forecast error (scaled by the lagged share price) is regressed on the previous period's scaled forecast error, the stock return over the preceding 12 months, the natural logarithm of the market value of equity and the abnormal stock return between the last earnings announcement date and the forecast date. Then, the average coefficients from the cross-sectional regression over the preceding three years together with each firm's current variables are used to estimate the forecast error for the next two earnings forecasts. Last forecasted eargnings are adjusted by substracting the estimated forecast error. Larocque (2013) finds that this correction technique substantially lowers resulting ICC estimates but does not improve their correlation with realized returns.

Mohanram and Gode (2013) develop a larger model to predict forecast errors. They run a cross-sectional regression with the earnings forecast error scaled by share price as regressand and the following variables as regressors: firm's accruals divided by lagged total assets, sales growth over the last fiscal year, analysts' long-term growth forecast, property, plant and equipement growth over the last fiscal year, growth in other long-term assets over the last fiscal year, stock return over the preceding 12 months, and the difference between the current earnings forecast and the forecast at the beginning of the respective year. In contrast to Larocque (2013), the authors find that adjusting eargnings forecasts for predictable errors significantly improves the association between realized returns and the resulting ICC.

### Forecasting Earnings

A different approach to dealing with analysts' eargnings forecast errors is to replace analyst data altogether. Hou et al. (2012) implement eargnings forecasts derived from a pooled cross-sectional regression model using data covering the preceding 10 years. Specifically, they regress dollar earnings for year $t +\tau$ on total assets, dividends, an indicator variable that equals on if the company paid a dividend and zero otherwise, earnings, an indicator variable that equals one if the company had negative earnings and zero otherwise, and accruals. All explanatory variables are taken from year $t$. The authors find that their model estimates earnings with less bias and for a wider range of companies than estimates from analysts.

Conversely, Allee (2011) uses a time-series regression model, which makes use of the past five years of earnings, to forecast earnings. Gerakos and Gramacy (2013) evaluate numerous models to forecast earnings and find that, at a one-year horizon, a naive random walk model performs as well as cross-sectional models. Motivated by the fact that a random walk model is unsuitable for all ICC methods that rely on short-term earnings growth, Li and Mohanram (2014) propose the earnings persistence model (EP) and the residual income (RI) model (Feltham and Ohlson, 1996) to forecast earnings. The EP model estimates a pooled cross-sectional regression with forecasted earnings on the left-hand side and an indicator variable that equals one if earnings are negative and zero otherwise, current earnings, and an interaction term between the indicator variable for negative earnings and current earnings on the right-hand side. The interaction term allows for asymetric persistence of loss and profit (Li 2011). Their RI model runs the following regression. The dependent variable is again forecasted earnings but the independent variables are the following: an indicator variable that equals one if earnings are negative and zero otherwise, current earnings, an interaction term between the negative earnings indicator variable and current earnings, current book value, and total accruals (from Richardson et al. 2005). All figures are on a per-share level and both regressions use 10 years of data. The authors show that these models outperform the cross-sectional model from Hou et al. (2012) and the random walk model with respect to accuracy, forecast bias, and association with future realized returns.

| Reference | Valuation Model | Period | Earnings forecasts data |Long-term growth assumption |
|------:|:-----:|:------|------:|------:|
| Malkiel (1979)     | DDM     | 1966-1977     | Value Line     |Value Line/GDP growth rate     |
| 1     | 2     | 3     | 4     |4     |


### Key Takeaways

```{note}
The Gordon Growth Model is best suited for mature companies with stable dividend growth rates.
```

```{warning}
Always validate your assumptions about growth rates - they significantly impact the results!
```

## Studies Using the Implied Cost of Capital

### Impact of corporate governance and disclosure policies on the cost of capital

### Other accounting and corporate finance settings

### Trade-off between expected returns and risk

### Asset pricing

### Investment strategies

### Key Takeaways

```{note}
The Gordon Growth Model is best suited for mature companies with stable dividend growth rates.
```

```{warning}
Always validate your assumptions about growth rates - they significantly impact the results!
```

