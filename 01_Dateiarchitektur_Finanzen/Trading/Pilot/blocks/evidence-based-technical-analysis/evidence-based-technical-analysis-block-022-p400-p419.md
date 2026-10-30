# Evidence-based Technical Analysis_ Applying the Scientific Method and Statistical Inference to Trading Signals.pdf — pages 400–419

--- page 400 ---

My ﬁrst exposure to an ISL was Gener, which was developed in 1983
for Raden Research Group by friend and colleague Professor John Wolberg. Today, ISLs are common. All rule back-testing platforms,19 such as
TradeStation, Wealth-Lab, Neuro-Shell, Financial Data Calculator, and so
forth have an ISL. Though each ISL has features unique to it, they share
similar syntaxes. The most basic ISL statement is a time-series operator
followed by a set of parentheses that contain the arguments of the operator. The arguments are the items that must be deﬁned for the operator to
do its thing. Operators differ in terms of the number of arguments required. For example, the moving-average operator requires two arguments: a data series to which the operator will be applied and the number
of periods in the look-back span. Thus a moving-average indicator would
be speciﬁed by a statement such as this:
Moving Average Indicator = MA (input series, N)
Where:
MA is the moving average operator
N is the number of days in the moving average.
The general form of an indicator expression in scripting language is:
Indicator = Operator (Argument1, Argument2, . . . , Argumenti)
Where:
i is the number of arguments required by the operator.
Figure 8.8 shows the ISL syntax for the operators deﬁned thus far:
channel breakout, moving average, and channel normalization.
A key beneﬁt of ISL is the ability to deﬁne complex indicators by nesting operators. In nesting, the output of one operator becomes an argument for a second operator and so on. For example, if one wanted to
deﬁne an indicator that is the 60-day channel normalization of another
time series that is a 10-day moving average of the Dow Jones Transportation Index, the expression for the indicator in ISL would look something
like this:
Indicator = CN [MA(DJTA, 10), 60]
404
CASE STUDY: SIGNAL RULES FOR THE S&P 500 INDEX
--- page 401 ---

INPUT SERIES TO RULES: RAW TIME SERIES
AND INDICATORS
This section describes the 24 raw time series used in the case study as
well as the 39 time series that were ultimately used as rule inputs. Ten of
the 39 inputs were in the form of raw unprocessed time series: S&P 500
closing price, Dow Jones Transportations Index closing price, NASDAQ
Composite Index closing price, and so forth. The additional rule 29 inputs
were indicators derived from one or more raw time series.
Raw Time Series
The 24 raw time series used in the case study came from two sources:
Ultra Financial Systems20 and Market Timing Reports.21 They are shown
in Table 8.1.
Indicators
Twenty-nine of the 39 rule inputs were indicators derived by transforming one or more raw time series with various mathematical, logical, and
Case Study of Rule Data Mining for the S&P 500
405
Number of Arguments = 2:
Channel-Breakout Operator (CBO)
Indicator = CBO (Time Series, n)
Number of Arguments = 2:
Channel-Normalization Operator (CN)
Indicator = CN (Time Series, n)
Number of Arguments = 2:
Moving-Average Operator (MA) or Linear Weighted MA (LMA)
Indicator = MA or LMA (Time Series, n)
FIGURE 8.8
Indicator scripting language for three TA operators.
--- page 402 ---

time-series operators. This section describes the transformations used to
produce these indicators.
The indicators are presented in four categories: (1) price and volume
functions, (2) market-breadth indicators, (3) prices-of-debt instruments,
and (4) interest-rate-spread indicators.
Price & Volume Functions.
Fifteen (15) indicators were functions
that combine price and volume information. A number of studies have
406
CASE STUDY: SIGNAL RULES FOR THE S&P 500 INDEX
TABLE 8.1
Raw Time Series
Number
Raw Data Series
Abbreviation
Source
1
S&P 500 Daily Close
SPX
Ultra 8
2
S&P 500 Open
SPO
Ultra 8
3
DJIA High
DJH
Ultra 8
4
DJIA Low
DJL
Ultra 8
5
DJIA Close
DJC
Ultra 8
6
S&P Industrials
SPIA
Market Timing Reports
7
Dow Jones Transports
DJTA
Market Timing Reports
8
Dow Jones Utilities
DJUA
Market Timing Reports
9
NYSE Financial Index
NYFA
Market Timing Reports
10
Dow Jones 20 Bonds
DJB
Ultra 8
11
NASDAQ Composite Close
OTC
Ultra 8
12
Value Line Geometric Close
VL
Ultra 8
13
NYSE Advancing Issues
ADV
Ultra 8
14
NYSE Declining Issues
DEC
Ultra 8
15
NYSE Unchanged Issues
UNC
Ultra 8
16
NYSE New 52-Week Highs
NH
Ultra 8
17
NYSE New 52-Week Lows
NL
Ultra 8
18
NYSE Total Volume
TVOL
Ultra 8
19
NYSE Upside Volume
UVOL
Ultra 8
20
NYSE Downside Volume
DVOL
Ultra 8
21
3-Month T-Bill Yields
T3M
Market Timing Reports
22
10-Year T-Bond Yields
T10Y
Market Timing Reports
23
AAA Bond Yields
AAA
Market Timing Reports
24
BAA Bond Yields
BAA
Market Timing Reports
--- page 403 ---

shown that trading volume contains useful information both on its
own and when used in conjunction with price.22 Technical analysis
practitioners have suggested a number of price and volume functions:
on-balance volume, accumulation distribution volume, money ﬂow,
negative volume, and positive volume. Each of these functions is described below.
The price-volume functions were used to create two types of indicators: (1) cumulative sums and (2) moving averages. An indicator deﬁned
as a cumulative sum is the algebraic sum of all prior daily values of the
price-volume function. The daily value of a price-volume function can either be a positive or negative quantity. Thus, an indicator deﬁned as the
cumulative sum of the on-balance volume, at a given point in time, is equal
to the sum of all prior values of the daily on-balance-volume quantity. An
indicator deﬁned as a cumulative sum will display long-term trends similar to those observed in the levels of asset prices and interest rates. In
other words, these indicators are nonstationary time series.
In contrast, a moving average of a price-volume function will be a stationary time series. In other words, it will not display trends. This is explained by the fact that a moving average only considers the observations
within the look-back span. Since price and volume functions can assume
both positive or negative values, a moving average will tend to remain
within a relatively conﬁned range near zero. See Figure 8.9.
Case Study of Rule Data Mining for the S&P 500
407
Cumulative Sum
Price-Volume Function
Moving Average
Price-Volume Function
Time
Time
0
FIGURE 8.9
Cumulative sum versus moving average of price-volume functions.
--- page 404 ---

Cumulative On-Balance Volume.
Perhaps the ﬁrst invented price &
volume function was the cumulative on-balance-volume indicator,
which is attributed to Joseph Granville and Woods and Vignolia.23 It is a
cumulative sum of signed (+ or –) total market volume. The algebraic
sign of the volume for any given day is determined by the sign of the
change in a market index for the current day, week, or whatever time
interval is being used. The case study used daily market changes in the
S&P 500 to determine the appropriate sign for the volume. If the price
of the index rose on a given day, that day’s entire NYSE volume was assigned a positive value and the number of shares traded was added to
the prior cumulative sum. On days when the price declined, the NYSE
volume was assigned a negative value and added to the prior cumulative sum (i.e., subtracted).
The computation for the cumulative on-balance volume is shown in
the following equation:24
Moving Averages of On-Balance Volume.
In addition to the cumulative on-balance volume, two moving averages of daily on-balance vol-
Where:
OBVt = (ftVt) = On-Balance Volume for day t
COBVt = Cumulative On-Balance Volume for day t
Vt = NYSE volume for day t
Pct = Closing price S&P 500 for day t
COBVt  = COBVt–1 + (ftVt)
ft  = 1.0
if Pct > Pct–1
ft  = –1.0
if Pct < Pct–1
ft  = 0
if Pct = Pct–1
Cumulative On-Balance Volume (COBV)
408
CASE STUDY: SIGNAL RULES FOR THE S&P 500 INDEX
--- page 405 ---

ume were considered: for 10 and 30 days (OBV10, OBV30). In ISL they
would be:
OBV10=MA(OBV,10)
OBV30=MA(OBV,30)
where OBV represents the on-balance volume for a given day.
Cumulative Accumulation-Distribution Volume (CADV).
Another
price-volume
function,
accumulation
distribution
volume,
is
attributed to Marc Chaiken.25 However, there are several similar functions including: Intra-day Intensity developed by David Bostian and
Variable Accumulation Distribution developed by Larry Williams.
These transformations attempt to overcome a perceived limitation in
on-balance volume, which treats the entire day’s volume as positive
(negative) even if the market index had a miniscule positive (negative)
price change. It was felt that minor price changes should not be treated
the same as large price changes. The proposed modiﬁcations to onbalance volume sought to ameliorate on-balance volume’s all-or-none
approach.
Chaiken proposed that a day’s price activity could be more accurately characterized by quantifying the position of the closing price
within the high-low range. Speciﬁcally, his calculation takes the difference between the closing price and the midpoint of the daily range and
divides the difference by the size of the range. The assumption is that,
when the market closes above the midpoint of its daily range, bullish or
accumulation activity dominated the day’s trading activity (accumulation) and should predict higher prices. Conversely when the market
closes below the midpoint of its daily range, the day is said to be dominated by bearish or distribution activity and should predict lower
prices. Only if the index closed at the low of the day or the high of the
day is the entire day’s volume assigned a negative (distribution) or positive (accumulation) value. More typically, the close is somewhere
within the day’s range resulting in some fraction of the volume being assigned to accumulation (positive volume) or to distribution (negative
volume). The range factor, which is deﬁned below, quantiﬁes the position of the closing price within the day’s range. The range factor is
multiplied by the daily volume, and this ﬁgure is accumulated to produce the cumulative sum. The calculation is shown in the following
equation.26
Case Study of Rule Data Mining for the S&P 500
409
--- page 406 ---

The case study used data for Dow Jones Industrials for the calculation of the accumulation-distribution function rather than the S&P 500 because daily high and low prices were not available for it. I assumed that
the closing position of the Dow Industrials within its range would be similar to the closing position of the S&P 500 within its range.
Moving Averages of Accumulation Distribution Volume.
Moving
averages of daily accumulation/distribution values were constructed for
10- and 30-day periods. In ISL they are:
ADV10=MA(ADV,10)
ADV30=MA(ADV,30)
Cumulative Money Flow (CMF).
Cumulative money ﬂow (CMF) is
similar to CADV with the exception that the product of volume and
range factor is further multiplied by the price level in dollars of the S&P
500 Index. This is intended to measure the monetary value of the volume. The price level used is an average of the daily high, low, and closing prices. The computation is shown in the following equation:27
Where:
ADVt =Vt ¥ Rft = Accumulation/Distribution Volume for day t
CADVt = Cumulative Accumulation/Distribution Volume for day t
Vt = NYSE volume for day t
Rft = Range factor for day t
Pct = Closing price Dow Jones Industrials for day t
Plt = Low price Dow Jones Industrials for day t
Pht = High price Dow Jones Industrials for day t
CADVt  = CADVt–1 + (Vt ¥ Rft)
Range Factor (Rft)  =
(Pct – Plt) – (Pht – Pct)
(Pht – Plt)
Cumulative Accumulation/Distribution Volume
410
CASE STUDY: SIGNAL RULES FOR THE S&P 500 INDEX
--- page 407 ---

Moving Averages of Money Flow.
Moving averages of money ﬂow
were constructed for 10- and 30-day periods. In ISL they are:
MF10=MA(MF,10)
MF30=MA(MF,30)
Cumulative Negative Volume Index (CNV).
Cumulative negative
volume is an accumulation of price changes on days of lower trading volume. In other words, it is a continuous algebraic sum of daily percentage
changes in a stock market index on days when volume is less than the
prior day. When volume is equal to or greater than a prior day, the CNV remains unchanged.
The inventor of CNV is unclear. Several sources attribute it to Norman Fosback28 but several sources, including Fosback, attribute the
idea to Paul Dysart.29 However, it seems clear that it was Fosback who
developed objective signal rules for CNV and evaluated their predictive
power.30
The notion of negative volume is based on the conjecture that “trading by unsophisticated investors occurs predominately on days of exuberantly rising volume, whereas informed buying and selling (i.e.,
Where:
MFt = (Vt  Apt  Rft) = Money Flow for day t
CMFt = Cumulative Money Flow for day t
Apt = Average price S&P 500 for day t: (Hi + Lo + Close)/3
Vt = NYSE volume for day t
Rft = Range Factor for day t
Pct = Closing price Dow Jones Industrials for day t
Plt = Low price Dow Jones Industrials for day t
Pht = High price Dow Jones Industrials for day t
CMFt  = CMFt–1 + (Vt × Apt  Rft)
Range Factor (Rft)  =
(Pct – Plt) – (Pht – Pct)
(Pht – Plt)
Cumulative Money Flow
 ×
 ×
 ×
Case Study of Rule Data Mining for the S&P 500
411
--- page 408 ---

smart-money activity) usually occurs during quieter periods of declining volume. Therefore, the direction that the market assumes on days of
negative volume purportedly reﬂects accumulation (buying) or distribution (selling) of stock by those who are in the know.”31
The computation of the index is as shown in the following equation:
Moving Averages of Negative Volume Index.
Moving averages of the
daily value of negative volume index (i.e., index’s percentage change on
lower volume days) were constructed for 10- and 30-day periods. In ISL:
NV10=MA(NV,10)
NV30=MA(NV,30)
Cumulative Positive Volume Index (CPV).
Cumulative positive volume (CPV) is the opposite of CNV. It is an algebraic accumulation of market index changes for days when volume is greater than the prior day.
Positive volume index is variously attributed to Fosback32 and to Dysart.
The calculation is presented in the equation that follows. It seems as if
Dysart proposed the positive volume index and suggested ways of inter-
Where:
NVt = ft = Negative Volume Index for day t
CNVt = Cumulative Negative Volume Index for day t
Vt = NYSE volume for day t
Pct = Closing price S&P 500 for day t
CNVt  = CNVt–1 + ft
ft  = [(Pct/Pct–1)–1] ¥ 100
if Vt < Vt–1
ft  = 0

if Vt > or = Vt–1
Cumulative Negative Volume Index (CNV)
412
CASE STUDY: SIGNAL RULES FOR THE S&P 500 INDEX
--- page 409 ---

preting it in a subjective manner, whereas Fosback deﬁned objective rules
and formally tested them:
Moving Averages of Positive Volume.
Moving averages of daily values of the positive volume index were constructed for 10- and 30-day periods (PV10 and PV30). In ISL:
PV10=MA(PV,10)
PV30=MA(PV,30)
Market Breadth Indicators.
Market breadth refers to the spread or
difference between the number of stocks advancing and the number declining on a given day, week, or other deﬁned time interval. Breadth has
been measured in a variety of ways, and they are reviewed in a scholarly
study by Harlow.33 For purposes of the case study, breadth is deﬁned as
the daily advance-decline ratio; that is, it is the difference between a day’s
advancing and declining issues divided by the total number of issues
traded. The data is based on all issues traded on the NYSE rather than an
alternative version that is restricted to NYSE common stocks. The series
restricted to common stocks, which some have claimed is superior because it excludes closed-end stock and bond funds and preferred stocks,
was not available in computer-readable form for the time period required.
Where:
PVt = ft = Positive Volume Index for day t
CPVt = Cumulative Positive Volume Index for day t
Vt = NYSE volume for day t
Pct = Closing price S&P 500 for day t
CPVt  = CPVt–1 + ft
ft  = [(Pct/Pct–1)–1] ¥ 100
if Vt > Vt–1
ft  = 0

if Vt < or = Vt–1
Cumulative Positive Volume Index (CPV)
Case Study of Rule Data Mining for the S&P 500
413
--- page 410 ---

The case study’s breadth indicators are of two forms: cumulative
sums of daily ﬁgures and moving averages of daily ﬁgures. For reasons
previously explained, the breadth indicators that are cumulative sums display long-term trends, whereas moving-average breadth indicators tend to
have reasonably stable mean values and ﬂuctuation ranges.
Cumulative Advance-Decline Ratio (CADR).
The cumulative advance decline ratio or CADR is a cumulative sum of the daily advancedecline ratio:
Moving Averages of Advance-Decline Ratio.
Moving averages of
daily advance-decline ratio (ADR) were constructed for 10- and 30-day periods (ADR10 and ADR30). In ISL they are:
ADR10=MA(ADR,10)
ADR30=MA(ADR,30)
Cumulative Net Volume Ratio (CNVR).
Another measure of market
breadth is the net volume ratio. It is based on the difference between daily
upside and downside volume. Upside (downside) volume is the total number of shares traded in stocks that closed up (down) for the day. The innovation of calculating and analyzing upside and downside volume
separately is attributed to Lyman M. Lowry in 1938.34 The daily net volume
ratio, a quantity that can assume either positive or negative values, is the
difference between upside and downside volume divided by total trading
volume. The case study used statistics released daily by the New York
Where:
CADRt = Cumulative Advance/Decline Ratio for day t
ADRt = Advance/Decline Ratio for day t
advt = NYSE advancing issues for day t
dect = NYSE declining issues for day t
uncht = NYSE unchanged issues for day t
CADRt  = CADRt–1 + ADRt
ADRt  =
advt – dect
advt + dect + uncht
414
CASE STUDY: SIGNAL RULES FOR THE S&P 500 INDEX
--- page 411 ---

Stock Exchange. The cumulative net volume ratio (CNVR) is the cumulative sum of daily ratios:
Moving Averages of Net Volume Ratio.
Moving averages of the daily
net volume ratio were constructed for 10- and 30-day periods (NVR10 and
NVR30). In ISL:
NVR10=MA(NVR,10)
NVR30=MA(NVR,30)
Cumulative New Highs-Lows Ratio (CHLR).
A third measure of
breadth, the cumulative new highs and new lows ratio (CHLR), takes a
longer-term view. In contrast to CADR and CNVR, which are based on
daily price changes and daily volumes, CHLR is based on a stock’s current
price relative to its maximum and minimum price over the preceding year.
Speciﬁcally, CHLR is the cumulative sum of the daily new highs-new lows
ratio (HLR), a quantity that can assume positive or negative values. The
high-low ratio is deﬁned as the difference between the number of stocks
making new 52-week highs on the day and the number of stocks making
new 52-week lows on the same day divided by the total number of issues
traded that day. This ﬁgure is accumulated algebraically to obtain CHLR.
There is nothing particularly signiﬁcant about using a look-back interval of 52 weeks. It is simply the mostly widely available statistic for new
high and new low data. Prior to 1978, the number of issues making highs
and lows was not based on a consistent 52-week look-back span. From
the middle of March in any given year, the data were based only on the
Where:
CNVRt = Cumulative Net Volume Ratio for day t
NVRt = Net Volume Ratio for day t
upvolt = NYSE advancing volume for day t
dnvolt = NYSE declining volume for day t
unchvolt = NYSE unchanged volume for day t
CNVRt  = CNVRt–1 + NVRt
Cumulative Net Volume Ratio (CNVR)
NVRt  =
     upvolt – dnvolt
upvolt + dnvolt + unchvolt
Case Study of Rule Data Mining for the S&P 500
415
--- page 412 ---

current calendar year. Prior to the middle of March, the ﬁgures were
based on the current and prior years. Thus, over the course of a given
year, the look-back span used to determine if a stock was making a new
low or a new high varied from 2.5 months in mid-March to as long as 14.5
months just before mid-March. Most of the data used in this study was
post-1978.
Despite the distortions created by the variable look-back span, rule
tests based on pre-1978 high-low data suggested that the indicator’s information content was robust to this distortion. For example, Fosback developed and tested an indicator called the high-low logic index over the
period 1944 to 1980. His results showed that indicator demonstrated predictive power over the entire period even though the bulk of the data was
infected with the variable look-back span distortion.35 The formula for
constructing the CHLR series is shown here:36
Moving Averages of New Highs/New Lows Ratio (HLR1 and
HLR30).
Moving averages of the daily high/low ratio were constructed
for 10- and 30-day periods (HLR10 and HLR30). In ISL they are:
HLR10=MA(HLR,10)
HLR30=MA(HLR,30)
Prices-of-Debt Instruments from Interest Rates.
Typically, interest rates and stock price levels move inversely. However, by taking the recip-
Where:
CNHLt = Cumulative New Highs New Lows on day t
HLRt = New Highs New Lows on day t
nuhit = NYSE new 52-week highs day t
nulot = NYSE new 52-week lows day t
advt = NYSE advancing issues for day t
dect = NYSE declining issues for day t
uncht = NYSE unchanged issues for day t
CHLRt  = CHLRt–1 + HLRt
Cumulative New Highs New Lows (CHLR)
   advt + dect + uncht
nuhit – nulot
HLRt  =
416
CASE STUDY: SIGNAL RULES FOR THE S&P 500 INDEX
--- page 413 ---

rocal (1/interest rate) interest rates can be transformed into price-like
time series that are, in general, positively correlated with stock prices.
This reciprocal series can be multiplied by a scaling factor such as 100.
Thus, a rate of 6.05 percent would be equivalent to a price of 15.38 (1/6.05
× 100).
This transformation was used in the case study and was performed
on four interest rate series: three-month treasury bills, 10-year treasury
bonds, Moody’s AAA corporate bonds, and Moody’s BAA corporate
bonds.
Interest Rate Spreads.
An interest-rate spread is the difference
between two comparable interest rates. Two types of interest-rate
spreads were constructed for the case study; the duration spread and
the quality spread. The duration spread, also known as the slope of the
yield curve, is the difference between yields on debt instruments having
the same credit quality but having different durations (i.e., time to maturity). The duration spread used in the case study was deﬁned as the yield
on the 10-year treasury note minus the yield on the three-month treasury
bills (10-year yield minus 3-month yield). The spread was deﬁned in this
way rather than 3-month minus 10-year so that an upward trend in the
spread would presumably have bullish implications for the stock market
(S&P 500).37
A quality spread measures the difference in yield between instruments with similar durations but with different credit qualities (default
risk). The quality spread for the case study was based on two of
Moody’s38 long-term corporate bond series: AAA,39 which are the highest rated corporate debt, and BAA,40 a lower rated grade of corporate
debt. The quality spread is deﬁned here as AAA yield –BAA yield. When
rates on lower quality debt (higher default risk such as BAA rated
bonds) are falling faster than rates on higher quality debt such as AAA
rated bonds, it is interpreted as indication that investors are more willing to assume additional risk to earn the higher yields on lower quality
debt. In other words, a rising trend in the quality spread is a signal that
investors are willing to take higher risks to earn higher returns. By this
reasoning, the quality spread should trend in the same direction as
stocks.
TABLE OF 40 INPUT SERIES USED IN CASE STUDY
Table 8.2 lists all of the data series used as rule inputs in the case study.
Case Study of Rule Data Mining for the S&P 500
417
--- page 414 ---

418
CASE STUDY: SIGNAL RULES FOR THE S&P 500 INDEX
TABLE 8.2
Input Series Used in the Case Study
Number
Description
Abbreviation
Form
1
S&P 500 Close
SPX
Raw
2
S&P 500 Open
SPO
Raw
3
S&P Industrials Close
SPIA
Raw
4
Dow Jones Transportation Index
DJTA
Raw
5
Dow Jones Utility Index
DJUA
Raw
6
NYSE Financial Index
NYFA
Raw
7
NASDAQ Composite
OTC
Raw
8
Value Line Geometric Close
VL
Raw
9
Cumulative On-Balance Volume
COBV
Indicator
10
On-Balance Volume 10-Day MA
OBV10
Indicator
11
On-Balance Volume 30-Day MA
OBV30
Indicator
12
Cumulative Accum. Distr. Volume
CADV
Indicator
13
Accum. Distr. Volume 10-Day MA
ADV10
Indicator
14
Accum. Distr. Volume 30-Day MA
ADV30
Indicator
15
Cumulative Money Flow
CMF
Indicator
16
Money Flow 10-Day MA
MF10
Indicator
17
Money Flow 30-Day MA
MF30
Indicator
18
Cumulative Negative Volume Index
CNV
Indicator
19
Negative Volume Index 10-Day MA
NV10
Indicator
20
Negative Volume Index 30-Day MA
NV30
Indicator
21
Cumulative Positive Volume Index
CPV
Indicator
22
Positive Volume Index 10-Day MA
PV10
Indicator
23
Positive Volume Index 30-Day MA
PV30
Indicator
24
Cum. Advance Decline Ratio
CADR
Indicator
25
Advance Decline Ratio 10-Day MA
ADR10
Indicator
26
Advance Decline Ratio 30-Day MA
ADR30
Indicator
27
Cum. Up Down Volume Ratio
CUDR
Indicator
28
Up Down Volume Ratio 10-Day MA
UDR10
Indicator
29
Up Down Volume Ratio 30-Day MA
UDR30
Indicator
30
Cum. New Highs/New Lows Ratio
CHLR
Indicator
31
New Highs/New Lows Ratio 10-Day MA
HLR10
Indicator
32
New Highs/New Lows Ratio 30-Day MA
HLR30
Indicator
33
NYSE Volume
TVOL
Raw
34
Dow Jones 20 Bond Index
DJB
Raw
35
Price 3-Month T-Bill
PT3M
Indicator
36
Price 10-Year Treasury Bond
PT10Y
Indicator
37
Price AAA Corporate Bonds
PAAA
Indicator
38
Price BAA Corporate Bonds
PBAA
Indicator
39
Duration Spread (10 Year –3 Month)
DURSPD
Indicator
40
Quality Spread (BAA–AAA)
QUALSPD
Indicator
--- page 415 ---

THE RULES
The rules tested in the case study can be grouped into three categories,
each representing a different theme of technical analysis: (1) trends, (2)
extremes and transitions, and (3) divergence. The following sections describe the rules in each category.
Trend Rules
The ﬁrst category of rules is based on trends. A foundational principle of
TA is that prices and yields move in trends that can be identiﬁed in a sufﬁ-
ciently timely manner to generate proﬁts. Practitioners have developed a
variety of objective indicators to deﬁne the direction of the current trend
and signal trend reversals. Among the most widely used are moving averages, moving-average bands, channel breakout, and Alexander ﬁlters also
known as zigzag ﬁlters. These are described in Kaufman41 and there is no
need to cover them all here.
The trend rules in the case study used the channel breakout operator
or CBO to deﬁne trends in the input time series. Thus, the CBO operator
transformed the input time series into a binary valued time series consisting of +1 and –1. When the trend of the input series was in an uptrend, as
determined by the CBO, the rule’s output was +1. Conversely, when the
analyzed series was determined to be in a downtrend, the output was –1.
The identiﬁcation of trend reversals in the input series by CBO is subject to lag. All trend indicators necessarily incur lag—a delay between the
time the input series experiences a trend reversal and the time the operator is able to detect it. Lag can be reduced by making the indicator more
sensitive. For example, in the case of CBO, lag can be reduced by decreasing the number of periods in the look-back span. However, this ﬁx creates
a different problem—an increased number of false signals. In other words,
there is a tradeoff between a trend-following indicator’s lag and its accuracy. Therefore, all trend indicators attempt to strike a reasonable balance
between signal accuracy and signal timeliness. Finding the optimum is a
challenge in the design of any signaling system, be it a household smoke
detector or a TA trend rule. In the end, optimal is whatever maximizes the
indicator’s performance, such as average return, risk-adjusted rate of return, and so forth. Since the behavior of ﬁnancial market time series
changes over time, the optimal look-back span for the CBO operator would
change as well. Adaptive versions of CBO were not used in the case study.
Of the 40 input series depicted in Table 8.2, 39 were used as inputs for
the trend rules. The open price of the S&P 500, input series 2 in Table 8.2,
was excluded on grounds of being redundant of the S&P 500 close.
Case Study of Rule Data Mining for the S&P 500
419
--- page 416 ---

Each trend rule was deﬁned by two parameters or arguments: the
CBO look-back span and a time series chosen from the set of 39 candidates shown in Table 8.2. A set of 11 values were tested as look-back
spans. They were 3, 5, 8, 12, 18, 27, 41, 61, 91, 137, and 205 days. The values were chosen to be separated by a multiplier of approximately 1.5. For
example, the look-back span of 205 days is approximately 1.5 times 137
days. This resulted in a total of 858 trend rules, 429 (39 × 11) based on a
traditional TA interpretation, and an additional 429 inverse-trend rules.
A traditional version of a trend rule produced an output value of +1
(long position in the S&P 500) when the input time series was determined
to be in an upward trend by CBO operator, and an output value of –1
(short position in the S&P 500) when the time series was in downtrend according to CBO operator. Inverse trend rules simply produced the opposite signals (e.g., short S&P 500 when the analyzed series was determined
to be in an uptrend).
In Chapter 9, where test results are reported, the following shorthand
naming convention will be used for the traditional and inverse trend rules.
A naming convention was necessitated by the large number of rules. The
syntax of the naming convention is as follows (note this syntax is different
from the syntax used for indicator scripting):
Rule (TT or TI) – Input Series Number – Look-back Span
Where TT stands for a traditional trend rule
and
TI stands for an inverse trend rule
For example, the rule named TT-15-137, is a traditional trend rule applied to input series 15 (Cumulative Money Flow) using a look-back
span of 137 says. A rule named TI-40-41 is an inverse trend rule applied
to input series 40 (the quality spread BAA– AAA) using a look-back span
of 41 days.
Extreme Values and Transitions
The second category of rules considered in the case study is “Extreme
Values and Transitions” or E rules. This category is based on the notion
that a time series conveys information when it assumes an extreme high
or low value or as it makes the transition between extremes. High and
low extremes can be deﬁned in terms of ﬁxed value thresholds if the time
series has a relatively stable mean and ﬂuctuation range (i.e., is stationary). All input series used for E rules were made stationary by applying
the CN operator.
420
CASE STUDY: SIGNAL RULES FOR THE S&P 500 INDEX
--- page 417 ---

Thirty-nine of the 40 input series were used for the E-type rules. The
open price of the S&P 500 was excluded on grounds of redundancy. The
input series used for E rules were ﬁrst smoothed with a four-day linearly
weighted moving average (LMA) before applying the CN operator. The
smoothing was done to reduce the number of signals that would have resulted from an unsmoothed version of the input series wiggling above and
below the signal threshold. Though smoothing may have been inappropriate for series that were already smoothed, for example the 30-day moving
average of negative volume, all series were treated with the LMA on
grounds of consistency.
In ISL, the expression for the input time series used for E rules is
given by the expression:
=CN (LMA (Input Series, 4), N-days)
Where:
CN is the channel normalization operator
LMA is a linearly weighted moving-average operator
This sequence of transformations is illustrated in Figure 8.10.
Case Study of Rule Data Mining for the S&P 500
421
Input
Time Series
4-day LMA Smoother
CN Operator
Smoothed
Time Series
Smoothed
Channel-Normalized
Series
E
Rule
FIGURE 8.10
Smoothed channel normalized series.
--- page 418 ---

E-rule signals were generated when the channel normalized smoothed
series crossed a threshold. Given that there are two thresholds, an upper and
lower, and given that there are two directions in which a crossing can occur
(up or down) there are four possible threshold-crossing events:
1. Lower threshold is crossed in the downward direction.
2. Lower threshold is crossed in the upward direction.
3. Upper threshold is crossed in the upward direction.
4. Upper threshold is crossed in the downward direction.
These events are illustrated in Figure 8.11.
Each E rule was deﬁned in terms of two threshold-crossing events:
one specifying the long entry/short exit and the other specifying the short
entry/long exit. This scheme yields 12 possible E-rule types. They are
listed in Table 8.3. Because they cover all possibilities, there would be no
point in including inverse versions. Note that type 7 is an inversion of
Type 1, Type 8 is an inversion of Type 2, and so on.
The 12 E-rule types are illustrated in Figures 8.12 to 8.23.
422
CASE STUDY: SIGNAL RULES FOR THE S&P 500 INDEX
Channel-Normalized
Smoothed
Series
Events
Upper
Threshold
Lower
Threshold
Events
Time
0
100
50
1
2
3
4
FIGURE 8.11
Threshold crossing events.
--- page 419 ---

Case Study of Rule Data Mining for the S&P 500
423
TABLE 8.3
The 12 E-Rule Types Deﬁned in Terms of Threshold Crossing Events
E-Rule Types
Long Entry/Short Exit
Short Entry/Long Exit
1
Event 1
Event 2
2
Event 1
Event 3
3
Event 1
Event 4
4
Event 2
Event 3
5
Event 2
Event 4
6
Event 3
Event 4
7
Event 2
Event 1
8
Event 3
Event 1
9
Event 4
Event 1
10
Event 3
Event 2
11
Event 4
Event 2
12
Event 4
Event 3
Upper
Threshold
Lower
Threshold
Time
0
100
50
2
1
2
1
+1
–1
Rule
Output
0
L
S
L
S
FIGURE 8.12
Extreme value and transition rule: Type 1.
