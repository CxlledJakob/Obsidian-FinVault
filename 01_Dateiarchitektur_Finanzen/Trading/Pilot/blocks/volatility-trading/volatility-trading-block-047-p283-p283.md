# Volatility Trading_ Sinclair_Volatility Trading -- Euan Sinclair(auth_) -- Wiley Trading, 1, 2013 -- John Wiley & Sons, Incorporated -- isbn13 9781118347133 -- 2634a86bfed8248fa7ba3fb72595bbbc -- Anna’s Archive.pdf — Chapter 9: Trade Evaluation — ABOUT THE WEBSITE (pages 283–283)

--- page 283 ---

ABOUT THE WEBSITE
274
■Go to http://ﬁnance.yahoo.com.
■Enter the ticker symbol in the ‘‘Get Quotes’’ box.
■Go to the ‘‘Historical Prices’’ link, which is third from the top in the box
‘‘More on (ABC)’’ on the left of the page.
■Set the start date to be four years before the end date and click ‘‘Get
Prices.’’
■Scroll to the bottom of the page and click on ‘‘Download to Spreadsheet.’’
Choose the option ‘‘Open.’’
■Cut and paste all of the data to the Yahoo! Finance data tab in Garch.xls.
■Go to Data->Sort->By Date Ascending.
■Go to the GARCH(1,1) tab and make sure all the data at the lower
range are correct. Four calendar years can contain slightly different
numbers of trading days so some samples will be of different lengths. It
is also important to clear the Yahoo! data before reusing the sheet on a
different day.
■Go to Tools->Solver. The inputs should be set up to maximize cell G2
by varying cells C3 through C5 with the constraints C3 >= 0, C4 >= 0
and C6 <= 0. Run Solver.
■On the ‘‘Calendar Curve’’ tab, you can enter your best estimate of
current volatility in cell C7 and look at the calendar curve being implied
by the ﬁtted GARCH model.
■Volatility Cones and Skew
and Kurtosis Cones
These spreadsheets produce various volatility, skewness, and kurtosis cones
from historical data.
■Go to http://ﬁnance.yahoo.com.
■Enter the ticker symbol in the ‘‘Get Quotes’’ box.
■Go to the ‘‘Historical Prices’’ link, which is third from the top in the box
‘‘More about (ABC)’’ on the left of the page.
■Set the start date to be four years before the end date and click on ‘‘Get
Prices.’’
