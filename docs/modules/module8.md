# Climate Risk: Testing the Claims

## The Confusion About Climate Risk

Walk into any asset management firm today and someone will tell you about "climate risk." They'll show you portfolios that underweight or exclude companies with high carbon emissions. They'll talk about stranded assets, transition risk, physical risk. They'll show projections of losses by 2050.

Here's what they won't tell you: they're confused about what risk means in finance.

If climate change creates systematic risk that's priced by the market, then high-carbon companies should earn *higher* returns going forward. That's how risk works. Risk and return are positively related. If you want compensation for bearing risk, you invest in risky assets. You don't avoid them.

But that's not what the industry does. They recommend *underweighting* high-carbon companies. They're implicitly assuming these companies are *overvalued*—that the market hasn't properly priced in future climate impacts. That's not a statement about risk. That's a statement about mispricing.

So which is it? Risk or mispricing?

This matters. If it's risk, climate-exposed firms should be in your portfolio (if you want the risk premium). If it's mispricing, climate-exposed firms should be shorted (if the mispricing is large enough to overcome trading costs and risk).

The industry doesn't want to answer this question clearly, because the answer would force them to confront uncomfortable facts about market efficiency. Instead, they muddle the two concepts, call everything "risk," and hope nobody notices.

Let's be clear about what's actually being claimed and how to test it.

## Risk vs. Mispricing: The Difference Matters

In finance, **risk** means exposure to systematic factors that affect returns. If climate change is a systematic risk, then firms exposed to climate impacts (high carbon emissions, coastal real estate, whatever) should have higher expected returns. The market prices in the risk, and investors demand compensation for bearing it.

**Implication:** If you believe climate risk is priced, you should *overweight* climate-exposed firms. They offer higher returns to compensate for the risk.

**Mispricing** means the market hasn't correctly valued future cash flows. If investors underestimate the costs of climate change—regulatory risk, physical damage, stranded assets—then high-carbon firms are overvalued. When reality hits, prices fall and returns are low.

**Implication:** If you believe climate risk creates mispricing, you should *underweight* or *short* climate-exposed firms. They'll underperform when the market wakes up.

These are opposite investment strategies. You can't have it both ways.

So what is the industry actually claiming? They say "climate risk" but recommend underweighting. That's a mispricing claim, dressed up in risk language to sound more respectable.

Fine. Let's test it.

## What the Industry Says (And Doesn't Say)

The typical climate risk report will tell you:

1. **High-carbon companies face future costs** from carbon taxes, regulation, stranded assets, physical damage.
2. **These costs aren't fully priced in** by the market today.
3. **Therefore**, you should reduce exposure to these companies to avoid losses.

Notice what's missing: any testable prediction about near-term returns.

Instead, they show you scenarios for 2050. Carbon prices rise to $200/ton. Global temperatures increase by 2°C. Coastal infrastructure gets flooded. Oil reserves become stranded. Losses mount.

By 2050.

This is clever. You can't falsify a 2050 prediction with 2026 data. You can make any claim you want, show scary charts, and nobody can prove you wrong for decades. By then, you'll have collected your consulting fees and moved on.

This is not science. This is storytelling.

If the market really underprices climate risk today, that should show up in returns *now*. Not in 25 years. Now. High-carbon firms should underperform starting today, as the market gradually reprices them.

That's testable. Let's test it.

## The Testable Hypothesis

Here's the claim we're testing: **High-carbon companies are overvalued because the market underestimates future climate-related costs.**

If true, we should observe:

1. **High-carbon firms have lower ICC** (implied cost of capital) than fundamentals justify. The market prices them for high cash flows that won't materialize.

2. **High-carbon firms underperform going forward.** As climate risks become clearer, prices adjust downward, generating low or negative returns.

3. **The underperformance concentrates around climate-related information events:** regulatory announcements, climate policy changes, earnings surprises related to climate costs.

This is the same logic we used to test analyst forecast mispricing. Now we apply it to climate.

## Building a Climate Exposure Measure

First, we need to measure climate exposure. What firms are most exposed to climate risk?

**Carbon emissions:** The obvious measure. Scope 1, 2, and 3 emissions. High emitters face regulatory risk and transition costs. Data available from CDP, Trucost, or company disclosures.

**Fossil fuel reserves:** Oil, gas, coal reserves that might become stranded if demand falls. Available from financial statements and industry databases.

**Physical exposure:** Coastal real estate, agriculture in drought-prone regions, infrastructure vulnerable to extreme weather. Harder to measure but increasingly available from climate data providers.

**Revenue exposure:** Percent of revenue from high-carbon products or services. Electric utilities burning coal, automakers selling gas cars, etc.

Pick a measure. Carbon emissions intensity (emissions per dollar of revenue) is a good starting point. It's widely available and captures regulatory and transition risk.

Sort firms into quintiles by carbon intensity. Q1 is low carbon (cleanest). Q5 is high carbon (dirtiest). If the climate mispricing hypothesis is true, Q5 should underperform Q1 going forward.

## Test 1: Do High-Carbon Firms Have Lower ICC?

Compute ICC for all firms using analyst forecasts (or model-based forecasts if you built your own). Then compare ICC across carbon quintiles.

**Climate mispricing hypothesis predicts:** High-carbon firms (Q5) have *lower* ICC than low-carbon firms (Q1), controlling for other factors. The market is pricing them for optimistic cash flows that don't account for climate costs.

**Climate risk hypothesis predicts:** High-carbon firms (Q5) have *higher* ICC than low-carbon firms (Q1). The market demands higher returns to compensate for climate risk.

Run the regression:

$$
ICC_{i,t} = \alpha + \beta \cdot Carbon_{i,t} + \gamma \cdot Controls_{i,t} + \varepsilon_{i,t}
$$

Control for size, value (B/M), profitability, leverage—standard factors that affect expected returns. You want to isolate the carbon effect.

What do you expect to find?

If $\beta < 0$: High carbon, low ICC. That's evidence of mispricing—the market underprices climate risk.

If $\beta > 0$: High carbon, high ICC. That's evidence of priced risk—the market prices in climate costs and demands compensation.

If $\beta \approx 0$: Carbon exposure doesn't affect ICC. Either climate risk isn't material, or it's already priced in through other channels.

## Test 2: Do High-Carbon Firms Underperform?

Form portfolios sorted on carbon intensity. Hold for 12 months. Measure returns.

**Climate mispricing hypothesis predicts:** Q5 (high carbon) underperforms Q1 (low carbon). The long-short portfolio (Q1 - Q5) earns positive returns. You're shorting overvalued firms and buying undervalued firms.

**Climate risk hypothesis predicts:** Q5 outperforms Q1. High-risk firms earn higher returns. The long-short portfolio earns *negative* returns (you're shorting the high-return firms).

Compute summary statistics:
- Mean return for each quintile
- Long-short return (Q1 - Q5 or Q5 - Q1, depending on your hypothesis)
- Sharpe ratio
- Alpha relative to Fama-French factors

If high-carbon firms underperform by, say, 3-5% per year with a significant alpha, that's evidence of mispricing. The market is slowly waking up to climate costs.

If high-carbon firms outperform, that's evidence of priced risk. Investors are getting compensated for bearing climate exposure.

If returns are flat, climate exposure doesn't predict returns. Either it's not material or it's already priced in.

## Test 3: When Do Returns Materialize?

This is the smoking gun test, like Rusticus (2019) for ICC mispricing.

If climate mispricing is real, returns should concentrate around climate-related information events:
- Climate policy announcements (carbon taxes, emissions regulations)
- IPCC reports or major climate conferences (COP meetings)
- Climate-related earnings surprises (unexpected costs from extreme weather, write-downs of fossil assets)

Take your high-carbon portfolio and decompose its returns:
- **Climate event days:** Returns during and around major climate-related announcements
- **Non-event days:** Returns on all other days

If the climate mispricing hypothesis is right, a disproportionate share of the underperformance should happen on event days. That's when the market updates beliefs about climate costs.

If returns are spread evenly across all days, it looks more like compensation for bearing continuous risk, not discrete mispricing corrections.

## What Does the Evidence Say?

This is an active research area. The evidence so far is mixed and depends heavily on sample period and methodology.

**Some studies find:** High-carbon firms underperformed in recent years (roughly 2015-2023), especially in Europe where climate regulation is stricter. This is consistent with the mispricing hypothesis—markets are slowly pricing in climate risk.

**Other studies find:** The underperformance is small, statistically weak, and disappears once you control for standard factors (value, quality, momentum). High-carbon firms tend to be old economy (energy, utilities, industrials), which underperformed growth stocks during the 2010s for reasons unrelated to climate.

**Time variation matters:** Before 2015, there was no clear carbon-return relationship. Post-2015, as climate became a bigger policy and media focus, high-carbon firms started underperforming in some regions. This suggests the "mispricing" (if it exists) is time-varying and driven by changing investor attention.

**Geography matters:** The relationship is stronger in Europe than in the US. Probably because European investors and regulators take climate policy more seriously.

**The ICC evidence:** Limited studies so far. Preliminary evidence suggests high-carbon firms have *lower* ICC (consistent with mispricing), but the effect is small and not robust across specifications.

Bottom line: The evidence for large, persistent climate mispricing is weak. There might be some underpricing of climate risk in the late 2010s/early 2020s, but it's not a slam dunk. And even if it exists, it's probably small—a few percent per year at most—and concentrated in specific sectors and regions.

## Using Earnings Forecasts to Test Climate Mispricing

Here's another angle. Build an earnings forecast model (like module 7) that incorporates climate risk.

Add climate-related variables to your forecast model:
- Carbon intensity
- Exposure to carbon pricing (based on geography and industry)
- Physical climate risk measures (coastal exposure, water stress)
- Climate-related capital expenditures or provisions

If high-carbon firms face future costs that analysts underestimate, your model should predict lower earnings for those firms than analysts do. The gap between model forecasts and analyst forecasts tells you whether the market is underestimating climate impacts.

Then compute ICC using:
1. Analyst forecasts (market's view)
2. Your climate-adjusted model forecasts (your view)

If your climate-adjusted ICC is higher than analyst-based ICC for high-carbon firms, you're saying the market underprices climate risk. Form portfolios based on the gap. If the gap predicts returns, you've found mispricing.

This is hard to do well—you need good climate data, a sound earnings model, and careful controls. But it's doable. And it's more rigorous than hand-waving about 2050 scenarios.

## The Fundamental Problem: Uncertainty

The biggest challenge with climate risk is uncertainty. We don't know:

1. **How much warming will occur:** The range of IPCC scenarios is wide. 1.5°C vs. 3°C makes a huge difference for physical impacts and policy responses.

2. **What policies will be enacted:** Will there be a global carbon price? When? How high? Or will regulation be piecemeal and ineffective?

3. **How technology will evolve:** Will cheap renewables and storage make fossil fuels obsolete? Will carbon capture work at scale? Will fusion come online?

4. **How firms will adapt:** Some firms will transition successfully (oil majors becoming energy companies). Others will be stranded. It's hard to predict who wins and who loses.

This uncertainty makes climate risk genuinely hard to price. Even if markets are "efficient," prices will reflect current beliefs about these unknowns. As beliefs change—and they will—prices will adjust. That creates volatility and potential mispricings.

But here's the thing: if *you* don't have better information than the market about these unknowns, you can't systematically exploit climate mispricing. You're just taking a different bet on uncertain outcomes. That's not alpha. That's idiosyncratic risk.

To claim mispricing, you need to show the market is making a systematic error you can identify and trade on. Not just that you have a different view about the future.

## Practical Implications: What Should You Do?

**If you're building portfolios:**

- **Don't blindly underweight carbon.** The evidence for persistent outperformance from low-carbon portfolios is weak. You might be giving up returns.

- **If you want climate exposure, be explicit.** Decide whether you're tilting away from carbon because of (1) mispricing beliefs, (2) risk management, or (3) non-financial preferences (ESG, values). These are different objectives with different implementations.

- **Test it yourself.** Use the tools from this course. Compute ICC by carbon quintile. Form portfolios. Measure returns. See if you can find evidence of mispricing in your sample.

**If you're estimating cost of capital:**

- **Climate risk probably increases cost of capital for high-carbon firms.** Regulatory uncertainty, stranded asset risk, reputational risk—these matter. But by how much? 50 bps? 100 bps? It's hard to pin down.

- **Use scenario analysis.** Compute cost of capital under different climate policy scenarios. Show a range. Don't pretend you know the answer.

- **Don't double-count.** If you adjust cash flows downward for climate costs (lower future earnings, carbon taxes, stranded assets), don't also increase the discount rate. You're penalizing the firm twice.

**If you're a researcher:**

- **This is a great area for empirical work.** The questions are important and largely unsettled. The data is getting better. The methods from this course (ICC, earnings forecasts, return decomposition) apply directly.

- **Be careful with time-varying effects.** The carbon-return relationship probably isn't stable. It depends on policy, investor attention, and technology shocks. Don't assume patterns from 2015-2020 will persist.

- **International evidence is key.** The US is not the world. Europe, China, and emerging markets have different climate exposures and policies. Cross-country tests are informative.

## The Industry's Sleight of Hand

Let's come back to where we started. Why does the industry call it "climate risk" when they're really talking about mispricing?

**Marketing.** "Risk" sounds objective and scientific. Everyone agrees risk should be managed. "Mispricing" sounds like you're claiming to be smarter than the market. That's a harder sell.

**Regulation.** Financial regulators care about risk. If you frame climate as a risk, you can argue for mandatory disclosures, stress tests, capital requirements. If you frame it as mispricing, regulators will ask: "Why should we intervene if the market can price it?"

**Business model.** Asset managers sell "climate-aware" portfolios at higher fees. If they admitted they're just betting on a mispricing, clients might ask: "Why should I pay you 50 bps for a bet I could make myself?" But if it's "managing climate risk," it sounds like sophisticated expertise.

None of this means climate change isn't real or important. It is. But the financial industry's treatment of it is often intellectually dishonest. They conflate risk and mispricing. They make untestable long-term claims. They charge fees for strategies that might not deliver.

As an analyst or investor, your job is to cut through the noise and ask: **What does the evidence actually say?**

## The Bottom Line

Climate change is real. It will affect the economy and financial markets. But "climate risk" as marketed by the industry is often confused and untestable.

If you want to test whether climate exposure creates mispricing, use the tools from this course:

1. **Measure climate exposure** (carbon intensity, physical risk, transition risk)
2. **Compute ICC** for high vs. low exposure firms
3. **Form portfolios** and measure returns
4. **Decompose returns** around climate-related events
5. **Build earnings forecast models** that incorporate climate variables

This gives you testable, falsifiable predictions. If high-carbon firms consistently underperform with returns concentrating around climate events, that's evidence of mispricing. If they outperform, climate risk is priced. If returns are flat, climate exposure doesn't matter much (yet).

The early evidence is mixed. There's some sign of climate-related underperformance in recent years, especially in Europe. But it's small, time-varying, and not robust across all specifications. It's not the "stranded asset crisis" the industry warns about.

Maybe that will change. Maybe as climate impacts become clearer and policy gets more aggressive, the mispricing will grow. Or maybe the market will efficiently price in new information, and there won't be systematic mispricings to exploit.

Either way, the right approach is empirical. Test the claims. Don't take them on faith. And be skeptical of anyone making bold predictions about 2050 that conveniently can't be checked until they've retired.

That's the scientific perspective on climate risk. Follow the evidence, not the sales pitch.