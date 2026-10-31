# Volatility Trading_ Sinclair_Volatility Trading -- Euan Sinclair(auth_) -- Wiley Trading, 1, 2013 -- John Wiley & Sons, Incorporated -- isbn13 9781118347133 -- 2634a86bfed8248fa7ba3fb72595bbbc -- Anna’s Archive.pdf — Chapter 9: Trade Evaluation — ABOUT THE WEBSITE (pages 284–284)

--- page 284 ---

ABOUT THE WEBSITE
275
■Scroll to the bottom of the page and click ‘‘Download to Spreadsheet.’’
Choose the option ‘‘Open.’’
■Cut and paste all of the data to the Yahoo! Finance data tab in Volatility
Cones.xls or Skew and Kurtosis cones.xls.
■Daily Option Hedging Simulation
Here we simulate the evolution of a hedged long option position of 1,000
vega (this can be changed in cell O18 on the historical returns sheet and
cell N18 on the normal returns sheet), where we hedge each day on the
close. We use the standard U.S. option convention where one option is for
100 shares. The tab ‘‘Normal Returns’’ generates a GBM process from the
parameters in cells N3 and N4. The tab ‘‘Historical Returns’’ uses historical
data. Here cell O4 is a derived quantity and cell O3 is set to zero. This is
consistent with our basic assumptions regarding measuring volatility from
historical time series.
■Go to http://ﬁnance.yahoo.com.
■Enter the ticker symbol in the ‘‘Get Quotes’’ box.
■Set the start date to be one year before the end date and click on ‘‘Get
Prices.’’ Check that this gives 250 days of data. Some adjustment will
be needed here (and clearly the sheet can be modiﬁed to deal with any
length of historical data).
■Scroll to the bottom of the page and click ‘‘Download to Spreadsheet.’’
Choose the option ‘‘Open.’’
■Cut and paste all of the data to the Yahoo! Finance data tab in
Garch.xls.
■Go to Data->Sort->By Date Ascending.
■In cell 013 (or N13 on the ‘‘Normal Returns’’ tab) enter the implied
volatility at which the option was purchased (the zero-sum nature of
derivatives trading means that the results for a short position are the exact
opposite of those for a long).
■The hedging volatility can be adjusted in cell O7 (N7 on the ‘‘Normal
Returns’’ tab).
■The ‘‘Normal Returns’’ sheet can be recalculated by hitting the
F9 key.
