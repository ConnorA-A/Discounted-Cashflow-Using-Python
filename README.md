DCF MODEL FIRST ATTEMPT (USING SEC EDGAR)

This was my first attempt at building a DCF model using Python, pulling data directly from SEC EDGAR 10-K Annual reports.

I abandoned this approach because the tagging and formats were inconsistent across companies. For example, Alphabet Inc. (GOOGL) records depreciation and amortization as just "depreciation of property and equipment". 
Many different firms had similar issues across their reports, which kept crashing the model or pulled the wrong figures.

Rather than fighting the data source, I rethought the approach and rebuilt the model using yfinance.

This is just kept here as a record of the approach that didn't work.

The finished model lives here: https://github.com/ConnorA-A/DCF-updated
