# A systematic alpha-finding framework based on earnings announcements, CARs, and ICC

We impose two rules up front:
1. CAR (Cumulative Abnormal Return) are not systematically a source of alpha. A CAR only says prices moved. It does not say prices were wrong before. 
2. Alpha requires an ex-ante benchmark. To claim mispricing, we must show that:
- a valuation or forecast existed before the announcement and,
- prices systematically failed to reflect it.

Everything that follows respects these two rules.

## Do Earnings Announcements Generate Repricing? 

Question: do stock prices move abnormally around earnings announcements?

Method:
- Standard event study around earnings announcements.
- Window: e.g. [-3, +3] days around announcement.
- Abnormal return computed via: 
- market adjusted 
- factor-adjusted (e.g. Fama-French 3-factor, Carhart 4-factor)

Output: 
- CARs around earnings announcements 

Interpretation:
- If CARs are significantly different from zero, prices move abnormally around earnings announcements.
- At this stage, we can only say that prices are reacting to earnings news. We cannot yet say whether prices were wrong before the announcement.
- This is repricing, but not necessarily mispricing.

At this stage:
- No strategy yet.
- No alpha claim.

## Is the Repricing Fully Unpredictable?

Now we ask the only question that matters for alpha: 
Was the eargnings information that moved prices entirely unpredictable, or was it partially foreseeable but underweighted by the market?

## Construct an ex-ante valuation benchmark: Implied Cost of Capital (ICC)

We now assert the existence of a better expectation than the market's. This is not free - it must be justified.

Two admissible approaches:
- Analyst-based ICC:
  - Use analyst earnings forecasts to compute ICC via the residual income model or discounted cash flow model.
  - Analysts are informed and have incentives to be accurate.
  - Assumption: Analysts aggregate and process information better than the marginal investor 

- Model-based ICC:
  - Use a structural model (e.g. Ohlson model, residual income model) to back out ICC from prices and fundamentals.
  - Assumption: The model captures fundamental value better than the market does.


At this point, we are not saying that analysts or models are correct. We are only saying they define a coherent alternative expectation. 

## Identification Step 

If ICC captures risk, then its associated returns should accrue smoothly through time.
If ICC captures mispricing, then its associated returns should cluster around earnings announcements.

### Build ICC-sorted portfolios
- Sort stocks into portfolios based on ICC (e.g. quintiles).
- Long high ICC, short low ICC.
- This is the candidate alpha portfolio.

At this point:
- ICC hedge portfolios has a positive average reutnr (as usual).
- This alone does not imply alpha.

### Decompose realized returns by timing 

Split the realized returns of the ICC hedge portfolio into:
1. Returns around earnings announcements (e.g. [-3, +3] days)
2. Returns outside earnings announcements

Compute: 
- fraction of total return coming from earnings announcement windows.
- compare to fraction of calendar times those windows represent.

### Interpretation

Case A: Returns are spread evenly through time
- Hedge returns accrue mostly outside announcements.
- Interpretation:
    - ICC reflectss compensation for risk.
    - No mispricing evidence.
    - No announcement-based alpha.

Case B: Returns concentrate at earnings announcements
- A large share of ICC hedge returns realized in short announcement windows.
- Interpretation: 
    - Earnings information validateds ICC-implied expectations
    - Prices catch up to information already embedded in ICC 
    - This is mispricing correction.


## Connecting back to CARs 

Now we reinterpret the CARs from Stage 1

CAR without ICC:
- Prices moved because earnings news arrived.

CAR with ICC
- Prices moved because eargnings news caused investors to update beliefs toward expectations that were already embedded in ICC.

## From identification to systematic alpha 

Only now can we say the word alpha without hand-waving. 

The strategy is: hold firms whose prices underweight foreseeable earnings information (high ICC) and short firms whose prices overweight foreseeable earnings information (low ICC). Earn returns when that information is revealed at earnings announcements.