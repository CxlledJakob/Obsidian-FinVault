# Quantitative financial analytics_ the path to investment profits.pdf — pages 191–210

--- page 191 ---

168
Quantitative Financial Analytics
b. You are considering the purchase of Boheme common stock.
In order to value the security, you have attempted to project
future sales and earnings for 2015. You are convinced that sales
will increase according to the past pattern (that is, up by 100
percent) and the EBIT margin will be about the same as it was
in 2014. You assume debt levels and the tax rate will remain
constant.
(1) Determine sales, EBIT, and net income to common shareholders for 2015.
(2) EPS of common were $0.16 in 2012 and $0.40 in 2013.
Determine EPS for 2014 and projected EPS for 2015.
(3) The ﬁrm paid no dividend in 2012 or 2013 but did pay out
one-third of the 2014 earnings. Cash DPS are expected to
double in 2015. How much in dividends were paid in 2014?
What projected pay-out rate is expected for 2015?
(4) The P/E multiple for Boheme averaged 20× in 2012 and
2013. What was the average price of the stock for each
year?
(5) As of January 2, 2015, Boheme was selling at $15 per share.
What is the current P/E multiple based on 2014 earnings?
(6) What may account for this change in the multiple?
(7) Based on the current price of Boheme and your expectations about the future of the company, would you buy it?
References
Bernstein, L. A., Analysis of Financial Statements, 5th edn. New York:
McGraw-Hill, 1999.
Drake, P. P. and F. J. Fabozzi, “Financial Ratio Analysis,” in Fabozzi,
F. J., Handbook of Finance, Vol III, Chapter 54, pp. 581–595. New York:
John Wiley & Sons, 2008.
Fabozzi, F. J., P. P. Drake, and R. S. Polimeni, The Complete CFO
Handbook: From Accounting to Accountability. Hobobken, NJ: John
Wiley & Sons, 2007.
Fridson, M. and F. Alvarez, Financial Statement Analysis: A Practitioner’s
Guide, 3rd edn. Hobobken, NJ: John Wiley & Sons, 2002.
--- page 192 ---

Financial Statement Analysis
169
Graham, Benjamin and D. L. Dodd, Security Analysis, 6th edn. New York:
McGraw-Hill Book Company, 2009.
Peterson, P. P. and F. J. Fabozzi, Analysis of Financial Statements,
2nd edn. Hoboken, NJ: John Wiley & Sons, 2006.
Thompson, J. R., E. E. Williams, and M. C. Findlay, Models for Investors
in Real World Markets. New York: John Wiley & Sons, 2003.
--- page 193 ---

This page intentionally left blank
This page intentionally left blank
This page intentionally left blank
This page intentionally left blank
--- page 194 ---

Chapter 5
Forecasting Techniques
History never repeats itself but it rhymes.
Mark Twain
Introduction to Forecasting
Forecasting can be deﬁned as making a statement about an unknown
event. It usually entails calculating and predicting future events,
typically based on extrapolation from past experience. For physical
systems, using past data is not a bad idea. For example, we have seen
that the sunspot cycle follows a fairly regular 11-year pattern.
For the 3,179 months of sunspot numbers from 1749 through
2013, there is a deﬁnite cyclic component to the observations.
When we look at a smaller window, we deﬁnitely can “eyeball” a
132-month period. Indeed, from peak-to-peak, we have an average of
131.25 months separation, with an average 132.5 months needed in
the trough-to-trough undulation.
Again, using this rough technique, we can observe that the most
recent sunspot peak activity occurred in Figure 5.1 at month 656,
which corresponds to May 2012. We are fairly conﬁdent that the next
trough in sunspot activity will occur around month 742, or August
2019. Although this example does not try to predict the number of
sunspots, it does verify that May 2012 saw the lowest peak sunspot
activity since about 1898.
Alas, the ﬁnancial phenomenon that we wish to forecast is
not governed by the same forces that make celestial observations
predictable; however, the past is all we have to work with, so we will
171
--- page 195 ---

172
Quantitative Financial Analytics
Figure 5.1. (Left) Sunspot Numbers, January 1749 to November 2013; Sunspot
Numbers September 1967 to November 2013 (Right)
provide some overview of essential forecasting techniques, along with
the caveat that their use might lead to disappointing results.
Forecast Accuracy Measures
Various measures to assess the accuracy of forecast numbers have
been devised; we present three of the most common here. In all three
cases, we desire that the total forecast error measure be as small
as possible, indicating that each period forecast is as accurate as
possible. In each case, absolutely accurate forecasts result in zero
forecast error; the diﬀerences in these measures lie in how much to
penalize the inevitable errors.
We deﬁne a prediction error at a time t as the diﬀerence between
the forecast value Ft and the actual time series value Xt, for example,
putting Et = Ft−Xt. In each measure, we accumulate errors over the
N-period forecast horizon. The following formulas deﬁne cumulative
three error measures.
1. Mean absolute error (MAE).
MAE =
 N

t=1
|Et|

1
N .
--- page 196 ---

Forecasting Techniques
173
2. Root mean square error (RMSE).
RMSE =

E2
t
 1
N
1/2
.
3. Mean absolute percentage error (MAPE).
MAPE =
 N

t=1
|Et/Xt|

1
N .
Note that both MAE and RMSE have the same units as the
underlying time series, and that MAE is based on the absolute error
versus the RMSE which relies on squared errors, and thus penalizes
larger errors more than the MAE.
It can be seen that MAPE is expressed as a percentage, which
some feel is a more natural way to summarize forecast errors. An
intuitive description of interpreting various measures of error may
be found in Basi et al. (1976). In any case, lower forecast errors
result in lower summary measures, so once experience with one of
these measures has been gained, the analyst may continue to use it in
evaluating forecasts until there is a speciﬁc need to change evaluation
techniques.
Na¨ıve Forecasts
We will ﬁnd in subsequent chapters that the most important variables
indicating the worth and security of bonds and stocks were those
relating to the future income-generating abilities of the ﬁrm. Because
bond interest, sinking-fund payments, and common stock dividends
are paid out of future rather than past revenues, it is imperative that
the analyst forecast the position of the ﬁrm he or she is investigating
as far into the future as possible.
Forecasting techniques vary from the simplest na¨ıve projections
to the development of complicated regression models of the ﬁrm’s
total activities. Budgets and ﬁnancial statements play a role in almost
every kind of forecasting technique, although the sophistication of the
use of these data may vary considerably.
--- page 197 ---

174
Quantitative Financial Analytics
Analysts have been making na¨ıve forecasts for years. Before the
advent of the computer, practically all forecasts were simplistic by
necessity. Some of the more common na¨ıve techniques consist of
making linear extrapolations of past performance. For example, if
a ﬁrm’s earnings have been growing at 20 percent compounded
annually, the analyst may simply add this amount to current earnings
in order to get next year’s earnings. The main weakness of such
an approach is obvious in that no consideration is given to the
underlying determinants of earnings. Furthermore, the analyst is
assuming blindly that past performance will always be repeated.
(This assumption is explicit even in many of the more-sophisticated
techniques.)
The use of ratios with na¨ıve projections has long been the
mainstay of ﬁnancial analysis. A frequently used procedure is to
project sales one or two years into the future and then apply historical
ratios to generate pro forma income statements and balance sheets.
When it appears to the analyst that various ratio patterns might
change in the near future, these adjustments may be incorporated
into the analysis.
We may consider an example. Suppose the Recensement Data
Gathering Corporation has shown rapid growth in recent years. Sales
have advanced by 30 percent annually, and proﬁts have been growing
by 40 percent. Ratios for Recensement for the past three years are
given below:
Ratio
2012
2013
2014
Current
2.40
2.80
2.60
Gross margin
0.22
0.23
0.24
EBIT ratio
0.15
0.16
0.17
Net margin
0.06
0.07
0.09
Asset turnover
3.00
3.25
3.60
Long-term debt to capital
0.09
0.08
0.06
Sales for 2014 were $500,000. The analyst believes the past
growth rate will continue for next year. He or she also feels that
the current ratio will remain at about the 2014 level, that the
--- page 198 ---

Forecasting Techniques
175
long-run gross margin should be about 24 percent of sales, and
that the earnings before interests and taxes (EBIT) and net margins
will continue at 2014 levels. Long-run improvement in turnovers is
anticipated, however, and the analyst feels 3.80 is an accurate total
asset turnover projection. The ﬁrm has $10,000 in long-term debt
(LTD) that should not change next year. The ﬁxed asset investment
should increase to about $150,000. Earnings for 2014 could be
projected using a simple extrapolation of the earnings growth rate:
2014 earnings = (0.09) ($500,000) = $45,000
(0.4) ($45,000) = $18,000
2015 earnings = $45,000 + $18,000 = $63,000.
A less na¨ıve approach might be to prepare a pro forma income
statement and balance sheet given the sales growth and ratio
assumptions made above:
Rescentment Data
Pro forma Statement of Income
Sales [(500,000) + (.3)(500,000)]
$650,000
Cost of goods sold [(.76)(650,000)]
494,000
Gross margin
156,000
Other expenses
45,000
EBIT [(.17)(650,000)]
110,500
Interest and taxes
52,200
Net Income [(.09)(650,000]
58,250
Pro forma Balance Sheet
Current assets
$21,000
Fixed assets
150,000
Total assets [(650,000) ÷ (3.8)]
171,000
Current liabilities [(21,000) ÷ (2.6)]
8,000
Long-term debt
10,000
Net worth
153,000
171,000
--- page 199 ---

176
Quantitative Financial Analytics
Notice that the earnings growth rate indicated by the second
approach is less than that of the ﬁrst:
(58,500 −45,000) ÷ 45,000 = 30 percent
This growth rate was implicit in the assumptions made in the
second approach. If sales are growing by a given percentage and the
net margin is assumed to be constant, then the earnings growth rate
must equal the sales growth rate. In this instance, as in all examples
in which ratio values are assumed, the analyst should be sure that
internally inconsistent assumptions are not being made.
Some mention should be made as to the position of the ﬁrm with
respect to the life-cycle business model. Growth for a company is
usually described by an S-shaped curve, with startup/development,
growth, rapid growth, maturity, and decline being typical divisions
of this cycle. Knowing where the company is on this curve can help
determine what na¨ıve assumptions are applicable. Part of the ceteris
paribus model is that the growth rate for earnings or sales remains
relatively constant. This of course leads to an exponential level over
time, which most recognize is not sustainable. Indeed, consideration
needs to be given to the position of the ﬁrm in the growth life-cycle.
Figure 5.2 shows the sales and sales growth ﬁgures for both
Polaroid (1962–2000) and for Intel (1972–2012). We note that
Polaroid appears to be in the linear growth portion of the life-cycle
curve. Polaroid’s development, launch, and “rapid growth” phase
would have occurred in the 1948–1980 period when its hallmark
products came online. We do note the year-over-year growth for
Polaroid was decreasing from 30 percent in the early 1960s down
to negative growth (decline) prior to its bankruptcy in 2001.
Intel displays the development, launch, and rapid growth stages,
and we would argue maturity through 2012. Na¨ıve projections of the
average 20 percent growth may be sustained in the near future as
long as the growth in maturity is sustained.
In Figure 5.3, we see another example of changing life-cycle.
Apple, Inc. (AAPL, formerly Apple Computer, Inc.) exhibits the
launch and rapid growth phases from its 1980 initial public oﬀering
(IPO) until the mid-1990s, with an apparent maturing at that point.
--- page 200 ---

Forecasting Techniques
177
Figure 5.2. Sales and Sales Growth Percentages for Polaroid and Intel
Figure 5.3. Apple, Inc. Sales and Sales Growth
This is easily seen from the declining growth rates until they hit
negative in 1996–1998; however, the exponential peak of 1995 sales
is dwarfed by its subsequent renaissance after the early 2000s.
Smoothing Techniques
Very popular forecasting techniques are based on smoothing of the
data series. Smoothing takes out the seemingly random ﬂuctuations
--- page 201 ---

178
Quantitative Financial Analytics
and allows one to better quantify any underlying trends and so
calculate some n-period look-ahead forecasts. Single dimensional
smoothers are typically simple or exponential moving average
ﬁlters.
Consider the sales ﬁgures for Solid Cyrogenics, Incorporated
(SCI) for December 1988 through December 2010, superimposed with
a three-year simple moving average (SMA) of sales. Note that the
SMA smooths the sales ﬁgures. We would like to make a two-year
ahead forecast, and given the trend reversals from 2000 to 2005 and
vice versa, it makes most sense to forecast level sales of $2.133 billion
based oﬀon the smoothed average (Figure 5.4).
Compare this forecast with that based on the na¨ıve approach. In
it, we project using the average growth rate of recent periods which
supposedly take into account the life-cycle of the ﬁrm. We see wide
Figure 5.4. SCI Sales 1988–2010 with 2011 and 2012 Forecasts
--- page 202 ---

Forecasting Techniques
179
variety depending if we use the previous 5, 10, 15, or ALL the sales
growth data.
Na¨ıve Forecasts Based on Average Growth Rates
(percent)
5 years
10 years
15 years
29 years
5.8%
−0.8%
−3.2%
10.0%
2012
2,451
2,156
2,332
2,653
2011
2,317
2,173
2,260
2,411
Since it is not immediately evident what constitutes a “fair” representation of the average growth rate over a business cycle, we plot
all of the na¨ıve forecasts, from which we may select an appropriate
subset of growth values. One observes that these forecasts seem to be
optimistic, so various ad hoc means of tapering oﬀthe calculations
may be employed (such as expert opinion), but to be true to the
process we leave the forecasts as they are.
If we were to forecast the bottom line, we would need in addition
to forecast sales, estimates for future margins and expense ratios, as
well as possibly some contingencies. We see from Figure 5.5 that the
na¨ıve assumption of rather stable margins might not be that helpful
as a basis of a simple model. It will be necessary to devise a more
adaptive model if we wish to forecast the bottom line.
Stochastic Modeling
Rather than relying on the na¨ıve average growth values to make
forecasts, it makes much more economic sense to incorporate the
natural variability seen in the annual growth rates in making the
estimates. There are two main ways to incorporate period variability
in data of this sort. The ﬁrst is so-called parametric simulation, and
the second is non-parametric.
Parametric simulation attempts to model the variable of concern
using a statistical probability distribution. The forecaster then draws
--- page 203 ---

180
Quantitative Financial Analytics
Figure 5.5. SCI Margins 1980–2010
from this distribution a sales growth ﬁgure, say, and then calculates
the resulting sales value. This is done N times, corresponding to the
number of forecast periods being attempted.
There are many considerations needed to create such a parametric model. The main challenge is its speciﬁcation, which is determining which probability distribution to use for the data. It is well
known that there are an inﬁnite number of appropriate distributions,
numbered either by the parameter values, or by the form of the
distribution. Moreover, these distributions may be compound, for
example, frequency and severity models. Additionally, a Bayesian
approach might be warranted. In any case, blindly specifying, for
example, a normal distribution for sales growth might be grossly
wrong; considerable care (and experience) must be used in the model
speciﬁcation process.
Second to the distribution speciﬁcation, the next problem is
parameter estimation, which is how one determines what parameters
are needed to specify the form of the distribution. In addition, there
must be conﬁdence bounds on these parameter estimates which can
--- page 204 ---

Forecasting Techniques
181
signiﬁcantly aﬀect the forecasts, showing the need for performing
sensitivity analysis (see subsequent sections). There are many ways
to estimate model parameters, but none of them work very well when
the amount of historical data is small, which is usually the case in
ﬁnancial problems. It is almost certainly going to be a real problem
for the entrepreneur in evaluating future outlook for a company given
no track record, or at least very limited historical data.
For example, we use a parametric model for the sales forecast
since some preliminary diagnostics on the sales growth values indicated that a normal model is not that bad, which conclusion is also
borne out from comparison with a non-parametric approach (see next
section). So the model for sales growth at time t is Gt ∼N(ˆµ, ˆσ2).
The mean and standard deviation parameters were estimated using
the standard estimators1 and found to be ˆµ = avg(Gt) = 10.04% and
ˆσ =

var(Gt) = 18.6%, respectively. We conducted 500 simulations
for each year 2011 and 2012, and obtained a terminal distribution of
sales ﬁgures as shown in Figure 5.6 above. (The median forecast for
each year is indicated with the open square □.)
Note that the forecast median and mean are very close to one
another, again indicating that the normal distribution might not be
all that wrong. Also note that the median forecasts of $2.425 and
$2.603 billion (the open dots) seem more “intuitively” correct, or at
least not too out of line. Lastly, it should be emphasized that the full
range of variation is seen on the ﬁgure and in the summary statistics
below.
Parametric Forecasts for FY 2011 and FY 2012 ($B)
Min.
1st Qu.
Median
Mean
3rd Qu.
Max.
2011 Est.
1,216
2,135
2,425
2,418
2,703
3,593
2012 Est.
832
2,212
2,603
2,644
3,009
4,754
In non-parametric simulation, we let the data speak for themselves by resampling (with replacement) from the collection of sales
1See for example Thompson, Williams and Findlay (2003), pp. 229–231.
--- page 205 ---

182
Quantitative Financial Analytics
Figure 5.6. Parametric Forecast for SCI Sales 2011 and 2012
growths in our data sample. We then draw two annual growth factors
and assemble the forecast sales levels for each year. This is repeated
some large number of times (say 500) and a resulting distribution
of sales levels is obtained for each year, without having to specify a
model distribution or to estimate parameters.
The non-parametric approach is arguably the preeminent method
of model building, but it certainly is so when there is no immediately
apparent parametric model to ﬁt, or when data are lacking, or
both. As in the parametric approach, the outcome is a complete
distribution of outcomes, from which the forecaster chooses a representative value for use in the forecast. Usually the mean or median
is employed, and in cases where they diﬀer substantially, the latter is
preferred.
--- page 206 ---

Forecasting Techniques
183
Figure 5.7. Non-Parametric Forecast for SCI Sales, 2011 and 2012 (“-”) Superimposed on Parametric Forecasts (“.”)
The non-parametric forecasts are summarized below, and their
complete distributions are plotted in Figure 5.7.
A quantitative assessment of forecast accuracy is given below,
with ex post results of $2.316 and $2.410 billion obtained in FY
2011 and FY 2012. We note the stochastic approach is superior
to the na¨ıve approach under all accuracy measures, and that the
median forecast is preferable to the mean forecast in both the
parametric (Normal) and the non-parametric methods. Additionally,
in the example, the parametric model is slightly better than the nonparametric model, but this is so only because the percentage sales
growth data is symmetric and not signiﬁcantly non-normal under
diagnosis, reinforcing the adage that when a parametric model is
indicated and available, then it is best to use it.
--- page 207 ---

184
Quantitative Financial Analytics
SCI Sales Forecast, 2011 and 2012, Performance Comparison
2011
2012
MAE
RMSE
MAPE
SMA(3)
2,133
2,133
230
235
0.097
Avg. 10-Yr Growth
2,173
2,156
199
206
0.084
Median Normal
2,411
2,572
129
133
0.054
Mean Normal
2,397
2,631
151
166
0.063
Median Resampled
2,391
2,604
132
144
0.055
Mean Resampled
2,411
2,651
168
183
0.071
Actual Sales
2,316
2,410
Sales Growth (percent)
5.73
4.08
The same conclusions are reached when we attempt to perform a
four-period forecast. Over this timeframe and compared with reality,
the na¨ıve and SMA forecasts returned about a 16 percent prediction
error, compared with the stochastic error rates of about 6–7 percent.
SCI Sales Forecast, 2011–2014, Performance Comparison
2011
2012
2013
2014
MAE RMSE MAPE
SMA(3)
2,133
2,133
2,133
2,133
435
507
0.161
Avg. 10-Yr
Growth
2,173
2,156
2,139
2,122
420
504
0.155
Median Normal
2,411
2,572
2,807
3,115
159
170
0.062
Mean Normal
2,397
2,631
2,891
3,239
222
240
0.085
Median
Resampled
2,391
2,604
2,896
3,071
173
205
0.068
Mean Resampled
2,411
2,651
2,948
3,267
252
274
0.097
Actual Sales
2,316 2,410 2,551
2,994
Sales Growth
(percent)
5.73
4.08
5.85
17.37
There are a considerable number of enhancements to the stochastic modeling process that could be made. (1) For example, it could
be argued that there is correlation in the growth rates for a ﬁrm;
that is, for whatever econometric reason, declines in growth tend
to be accompanied by follow-on declines, or vice versa. (2) In
--- page 208 ---

Forecasting Techniques
185
forecasting bottom line results, additional probabilistic models need
to be speciﬁed. (3) Attempts can be made to model the processes
involved in determining expense ratios and hence margins. However,
we argue that a rather sophisticated forecast of future earnings
before interest, taxes, depreciation, and amortization (EBITDA) or
earnings can be made through this technique, which is much more
tied to reality than that from the na¨ıve forecasting approach, and is
attainable without too much additional work.
Time Series Analysis
At the time this book was written, a simple Amazon.com book
search for “Forecasting” returned 348,155 results, indicating that the
subject is a timely, complex, and evolving one. Modern “Time Series
Analysis” is rooted in the Autoregressive Integrated Moving Average
model (ARIMA) methodology, although almost countless extensions
and generalizations have been developed over the years.
The model is often written as ARIMA (p, d, q), with parameters
p, d, and q. These parameters are non-negative integers that characterize the order of the autoregressive (AR), integrated (I), and
moving average (MA) components of ARIMA model, respectively.
The model is usually represented as follows:

1 −
p

i=1
φiLi

(1 −L)dXt = µ +

1 +
q

i=1
θiLi

εt,
(5.1)
where Xt is the time series data, t is an integer, L is a lag operator
(i.e., LkZt = Zt−k), µ is a grand mean, φi and θi are parameters of
the autoregression and moving average, respectively, and εt are error
terms.
ARIMA and its oﬀspring and other relatives are extremely ﬂexible and provide powerful insight into time series phenomena. They
are quite strong in diagnosing and predicting trends and seasonality,
all of which are important for the analyst doing forecasting. However,
even an introductory review of the key concepts would be beyond the
intended scope of this book and the interested reader can review
the references at the end of this chapter for further ediﬁcation.
Most statistical and spreadsheet computer programs have some time
--- page 209 ---

186
Quantitative Financial Analytics
series capability built into them since all the methods are computerintensive.
Interestingly, academic research (as described in Givoly and
Lakonishok, 1984) has shown the superiority of, for example, the
Value Line Investment Survey estimates over sophisticated time
series models. ARIMA models have consistently disappointed those
trying to use them to forecast ﬁnancial phenomena.
Regression and Correlation Analysis
Na¨ıve forecasting techniques are reasonably satisfactory if the analyst
is projecting only one or two years into the future. When longer
forecasts are needed, however, more sophisticated approaches are
required. For a number of ﬁrms, there are no underlying long-run
trends in performance. If it appears to the analyst that a ﬁrm’s
activities are more or less stable (that is, sales, costs, and earnings do
not vary by much), then there really is no forecasting problem. There
are not many ﬁrms in this category, however. Much more likely is the
case of the cyclical ﬁrm that evidences no long-run trends but that
does have a consistent performance in the short run. Forecasting
the position of a cyclical enterprise may be accomplished by the
use of regression and correlation analysis, provided continuation
of an upswing (or a downswing) in activities prevails. It must be
remembered, however, that changes from an upswing to a downswing
position (or vice versa) cannot be predicted with least-squares
techniques. Statistical procedures are available for attempting this
problem, but they are beyond the scope of this book.
The use of multiple regression and correlation analysis and
corporate modeling allows the analyst to specify more accurately
values for a far larger number of variables than the na¨ıve methods.
Like the na¨ıve techniques previously discussed, however, regression
analysis assumes some underlying trend in the data being examined.
If no trend is there (short run or long run), the regression results will
be of little value for forecasting purposes.
A typical analysis employing regression procedures will begin
with a forecast of aggregate economic activity. Some securities
--- page 210 ---

Forecasting Techniques
187
analysts prepare their own predictions of such variables as gross
domestic product (GDP), prices, the level of interest rates, and
so on. Others depend upon the large econometric models, such as
those developed at the University of Pennsylvania’s Wharton School
(now operated as IHS Global Insight), and the Brookings Institution,
to generate aggregate predictions. Once the aggregate projection is
made, the analyst then concentrates on developing a model of the
industry of interest. Finally, a model is prepared for speciﬁc ﬁrms (or
a ﬁrm) within that industry. Typically, the results of the aggregate
forecast are fed into the industry model, and the output from the
industry model is used as input for the ﬁrm projection. At each stage
of developing the forecast, the analyst must be careful to select those
independent variables that make a priori sense as determinants.
Although it is possible to generate “good” statistical results (that is,
high R2 values that are also statistically signiﬁcant) by correlating
any two or more variables, it would be diﬃcult for an analyst to
defend a forecast that, say, based a prediction of sales on the phases
of the moon. Even if high sales and a full moon correlated with a
very good, statistically signiﬁcant ﬁt, one would be hard pressed to
ﬁnd an economic explanation for the phenomenon.
Examples
1. Peason-Jackson is a large, nationwide publisher of college textbooks. Textbook sales seem to depend on a number of factors, but
two variables stand out as being particularly signiﬁcant: family
median income (Y ) and the total college population (P). An
analyst has determined the following equation to project total
annual industry textbook sales:
Si = 140.3 + 2.7(Y ) + 5.94(P).
Where Si is measured in millions, Y in thousands, and P in
millions. For next year, if Y = $40,000 and P = 20,000,000, a
projection of Si would be:
Si = 140.3 + 2.7(40) + 5.94(20)
Si = 367.10
or
$367,100,000.
