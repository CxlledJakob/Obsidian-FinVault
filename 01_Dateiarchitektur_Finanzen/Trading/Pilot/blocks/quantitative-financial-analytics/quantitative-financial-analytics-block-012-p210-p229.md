# Quantitative financial analytics_ the path to investment profits.pdf — pages 210–229

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
--- page 211 ---

188
Quantitative Financial Analytics
2. Sales for Peason-Jackson are clearly a function of industry sales.
It has also been determined that a high correlation exists between
the ﬁrm’s sales and one other variable, the number of salesmen
employed by the ﬁrm (N). The following equation has been ﬁtted:
Sp = −50.6 + 0.18(Si) + 0.03(N).
where Sp is measured in millions. A prediction for Peason-Jackson
sales for next year if N = 1280 would be:
Sp = −50.6 + 0.18(367.1) + 0.03(1280)
Sp = 53.878
or
$53,878,000.
Independent Variables and Sensitivity Analysis
Two major problems confront the analyst when using multiple
regression analysis to forecast: (1) What are the key independent
variables? And (2) How sensitive are the ﬁnal forecasted results
to changes in the values of the independent variables? The ﬁrst of
these questions is diﬃcult to answer. Frequently, the analyst will try
a number of combinations of variables, examining the coeﬃcients
of partial determination, R2, and the statistical signiﬁcance of
the results in order to ﬁnd the combination that yields the best
prediction. The second problem can be handled through the use of
sensitivity analysis. Simply explained, sensitivity analysis seeks to
demonstrate how large a change in the value of a single independent
variable is required to alter signiﬁcantly the forecasted outcome.
Because the values assigned to the exogenous variables in a system
of forecasting equations are rarely known with certainty, it may be
necessary for the analyst to try likely values ﬁrst and then examine
his results as less-likely values are used. It is clear, of course, that
forecasted results for a dependent variable are no more accurate than
the input assumed for the independent variables.
Sensitivity analysis may be employed in a number of contexts.
The independent variables in any regression equation may be
subjected to sensitivity tests. Many analysts have attempted to
forecast stock prices directly without going through the extensive
--- page 212 ---

Forecasting Techniques
189
fundamental analysis that we recommend in this book. When such
an approach (direct forecasting) is employed, sensitivity analysis may
become a necessary supplement. Consider the case of the Second
Philadelphia Corp., an investment banking house that attempts to
forecast stock prices with regression analysis. The following equation
is used:
Pt = f(Pt−1, Dt−1, St, L, r, i).
(5.2)
Where:
Pt
is the stock price in period t.
Pt−1
was the average stock price in the previous period.
Dt−1
was the dividend in the previous period.
St
is expected sales per share in period t.
L
is the degree of ﬁnancial leverage (debt to equity) for the
ﬁrm expected in period t.
r
is the rate of return on investment (EBIT to total assets)
expected in period t.
i
is the prime rate of interest expected in period t.
For this ﬁrm, the regression equation below has been determined:
Pt = −6.50 + (0.76)Pt−1 + (0.15)Dt−1 + (1.34)St
−(8.24)L + (12.54)r −(26.12)i.
Values for each independent variable have been estimated for period
t as:
St = $10
L = 0.40
r = 0.25
i = 0.06.
The average share price for Second Philadelphia during the previous
period was $22. The ﬁrm paid a dividend of $1 per share in the
--- page 213 ---

190
Quantitative Financial Analytics
previous period. A projection of the stock price would provide:
Pt = −6.50 + (0.76)(22.00) + (0.15)(1.00) + (1.34)(10.00)
−(8.24)(0.40) + (12.54)(0.25) −(26.12)(0.06)
= −6.50 + 16.72 + 0.015 + 13.40 −3.30 + 3.14 −1.57
= $22.04.
Because future sales for Second Philadelphia are not known
with certainty, sensitivity analysis may be employed to examine the
diﬀerences in share prices produced by various sales estimates. If
economic conditions are good, sales may be $11.00 per share. If they
do not change from the past period, the $10.00 ﬁgure will prevail. If
conditions deteriorate, sales per share could fall to $9.00. Sensitivity
analysis could be applied to these three possible events:
1. If St = $11.00, Pt becomes $23.38
2. If St = $9.00, Pt becomes $20.70
3. Thus, a 10 percent deviation in sales per share can produce a
6 percent variation in forecasted price (that is, 1.34/22.04).
The analysis could be applied to other variables as well. Suppose
i might be 0.05, 0.06, or 0.07. The best event (i = 0.05) would
add $0.26 to the share price, and the worst one (i = 0.07) would
reduce the price by $0.26. This does not appear to be a very sensitive
variable.
The forecasting procedure used by Second Philadelphia, even
when supplemented by sensitivity analysis, leaves much to be desired.
We are not given R2, the coeﬃcients of partial determination, or
F test values to measure statistical signiﬁcance (see Appendix B
for discussion of these concepts). Furthermore, one could suspect
the presence of serial correlation, given the fact that one of the
independent variables is a lagged version of the dependent variable.
In any case, forecasting equations of this general sort should be
used with great care. A more diﬃcult, but also more adequate,
method is to project stock “values” (rather than prices) using a series
--- page 214 ---

Forecasting Techniques
191
of equations indicating fundamental relationships such as company
revenues to industry revenues, costs to revenues, and so on.
Summary
Forecasting can be deﬁned as making a statement about an unknown
event. It usually entails calculating and predicting future events,
typically based on extrapolation from past experience. Unfortunately,
the ﬁnancial phenomena that we wish to forecast is not governed by
the same forces that make physical observations predictable. The
past is all we have to work with.
Various measures to assess the accuracy of forecast numbers have
been devised; we presented three of the most common above. These
are MAE, RMSE, and MAPE. In all three cases, we desire that
the total forecast error measure be as small as possible, indicating
that each period forecast is as accurate as possible. In each case,
absolutely accurate forecasts result in zero forecast error; the diﬀerences in these measures lie in how much to penalize the inevitable
errors.
Forecasting techniques vary from the simplest na¨ıve projections
to the development of complicated regression models of the ﬁrm’s
total activities. Budgets and ﬁnancial statements play a role in almost
every kind of forecasting technique, although the sophistication of
the use of these data may vary considerably. The use of ratios with
na¨ıve projections has long been the mainstay of ﬁnancial analysis.
A frequently used procedure is to project sales one or two years
into the future and then apply historical ratios to generate pro
forma income statements and balance sheets. When it appears to the
analyst that various ratio patterns might change in the near future,
one may incorporate these adjustments into the analysis.
Very popular forecasting techniques are based on smoothing
of the data series. Smoothing takes out the seemingly random
ﬂuctuations and allows one to better quantify any underlying trends
and so calculate some n-period look-ahead forecasts. Single dimensional smoothers are typically simple or exponential moving average
ﬁlters.
--- page 215 ---

192
Quantitative Financial Analytics
Rather than relying on the na¨ıve average growth values to make
forecasts, it makes much more economic sense to incorporate the
natural variability seen in the annual growth rates in making the
estimates. There are two main ways to incorporate period variability
in data of this sort. The ﬁrst is so-called parametric simulation, and
the second is non-parametric.
Parametric simulation attempts to model the variable of interest
using a statistical probability distribution. The forecaster then draws
from this distribution a sales growth ﬁgure, say, and then calculates
the resulting sales value. This is done N times, corresponding to the
number of forecast periods being attempted.
In non-parametric simulation, we let the data speak for themselves by resampling (with replacement) from the collection of sales
growths in our data sample. We then draw two annual growth factors
and assemble the forecast sales levels for each year. This is repeated
some large number of times (say 500) and a resulting distribution
of sales levels is obtained for each year, without having to specify a
model distribution or to estimate parameters.
Time series models (ARIMA) and their oﬀspring and other
relatives are extremely ﬂexible and provide powerful insight into
time series phenomena. They are quite strong in diagnosing and
predicting trends and seasonality, all of which are important for
the entrepreneur doing forecasting; however, even an introductory
review of the key concepts would be beyond the intended scope of this
chapter; the interested reader can review the references at the end
of this section. Most statistical and spreadsheet computer programs
have some time series capability built into them since all the methods
are computer-intensive.
The use of multiple regression and correlation analysis and
corporate modeling allows the analyst to specify more accurately
values for a far larger number of variables than the na¨ıve methods.
Like the na¨ıve techniques previously discussed, however, regression
analysis assumes some underlying trend in the data being examined.
If no trend is there (short run or long run), the regression results will
be of little value for forecasting purposes.
--- page 216 ---

Forecasting Techniques
193
Sensitivity analysis may be employed in a number of contexts.
The independent variables in any regression equation may be
subjected to sensitivity tests. Many analysts have attempted to
forecast stock prices directly without going through the extensive
fundamental analysis that we recommend in this book. When such
an approach (direct forecasting) is employed, sensitivity analysis may
become a necessary supplement.
Problems
1. Obtain the sunspot data for monthly mean total sunspot number
(+13-month smoothed numbers [Jan 1749–now]. This is available from the Sunspot Index and Long-term Solar Observations
(SILSO), provided by the Solar Inﬂuences Data Analysis Center
(SIDC), which is the solar physics research department of the
Royal Observatory of Belgium. The SIDC includes the World
Data Center for the sunspot index and the ISES Regional Warning
Center Brussels for space weather forecasting. You may obtain the
data from the following internet site: http://sidc.oma.be/silso/
dataﬁles.
a. Censoring the most recent 250 months of sunspot activity
data (approximately the last two sunspot cycles), forecast
the time and intensity of the sunspot activity up through
the present time. You should narrow your prediction to the
nearest month. Your forecasting technique will be using what
we call “in-sample” data to predict the “out-of-sample data”
for 250 months ago to today.
b. Comparing your forecast with the actual data, calculate your
MAE, RMSE and MAPE for your predictions.
c. Forecast the time and intensity of the next three peaks of
sunspot activity.
2. Using the data in Appendix C, forecast select SCI Ratios and
Supplementals for 12/31/13 through 12/31/18. You may validate
your forecasts using ﬁnancial statement data which has subsequently become available. Note that you will need to forecast the
--- page 217 ---

194
Quantitative Financial Analytics
stock price as well. If you use others’ forecasts of the stock price,
such as Valueline, or Thompson/Reuters, be sure and reference
the source. Speciﬁcally, you should forecast:
Price/Earnings
Price/sales
Price/cash ﬂow
Earnings per share (EPS)/(recurring)
Dividends per share (DPS)
Dividend Yield (percent)
3. Using a 20-day SMA, forecast three-period ahead stock price for
three publicly traded stocks of your choice. Wait three days and
record the actual price obtained, and calculate the MAE, RMSE,
and MAPE for your predictions.
References
Albright, S. C., Wayne Winston, and Christopher Zappe, Data Analysis
and Decision Making, 4th edn. Mason, OH: South Western Cengage
Learning, 2011.
Basi, B. A., K. J. Carey, and D. T. Richard, “A Comparison of the
Accuracy of Corporate and Security Analysts’ Forecasts of Earnings,”
The Accounting Review, Apr. 1976, pp. 244–254.
Box, G. E. P., G. M. Jenkins, and G. C. Reinsel, Time Series Analysis,
Forecasting and Control, 3rd edn. Englewood Cliﬀs, NJ: Prentice Hall,
1994.
Crichﬁeld, T., Thomas Dyckman, and Josef Lakonishok, “An Evaluation
of Security Analysts’ Forecasts,” The Accounting Review, Jul. 1978,
pp. 651–668.
Evans, M. K., Practical Business Forecasting, Malden, MA: Blackwell
Publishing, 2003.
Givoly, D. and Josef Lakonishok, “The Quality of Analysts’ Forecasts of
Earnings.” Financial Analysts Journal, Sep.–Oct. 1984, pp. 40–47.
James, R. T., Empirical Model Building: Data, Models, and Reality, 2nd edn.
Hoboken, NJ: John Wiley & Sons, Inc., 2011.
McMahon, E. K. and J. A., Dobelman, A Market for Water: Constructing
a Custom Weighted Water Index. The Rice University, Statistics
Department Technical Report TR-2014-02. Jan. 2014.
Thompson, J. R., E., E. Williams, and M. C. Findlay, Models for Investors
in Real World Markets. Hoboken, NJ: John Wiley & Sons, 2003.
--- page 218 ---

Chapter 6
Analysis of Fixed Income Securities
I am more concerned with the return of my money than
the return on my money.
Will Rogers
Forecasts and Bond Analysis
Fixed-income securities are generally purchased because of the
reduced risk associated with returns generated by these instruments.
A bond obligates the issuing ﬁrm (or government) to pay interest at
a speciﬁc rate, at a particular interval, and in a prescribed manner.
Also, payments of principal are to be made periodically according
to the terms speciﬁed in the indenture (the contractual agreement
between the issuer and holder of the bond). The mere fact that
a security takes the form of a ﬁxed-income instrument does not
insure the safety of the security. Indeed, the common stocks of some
enterprises are less risky than the bonds of others. Nevertheless,
the bond form does generally set a maximum payment ceiling (the
coupon rate), and lesser amounts will be paid only if the issuer
encounters ﬁnancial diﬃculty.
Determining the probability that a ﬁrm (or other issuer) will
be unable to meet coupon or principal payments is the primary
responsibility of the bond analyst. Clearly, this task requires a
complete analysis of the present and future ﬁnancial position of the
ﬁrm, and the bond analyst will employ the techniques outlined in
the previous chapters to determine this position.
A recommended procedure is to forecast the earnings of the ﬁrm
as far into the future as possible. In the ideal case, the analyst will be
195
--- page 219 ---

196
Quantitative Financial Analytics
able to project throughout the life of the bond. Given this forecast,
the analyst may then prepare annual probability distributions of
interest (and principal) payments. From this set of distributions, the
risk and return from purchasing the instrument may be determined.
We may consider an example of the appropriate methodology.
An analyst has constructed a corporate model for the Consolidated
Electric Appliance Corp. (CEA) He wishes to use this model in
order to determine the risk and return associated with Consolidated’s
5 percent subordinated debenture due on December 31, 2019. The
bond pays interest semiannually, although the analyst is assuming
annual payments to simplify his calculations.
Consolidated grossed $120 million in 2014. A revenue-forecasting
equation has been generated with a reasonably good ﬁt by means to
multiple regression analysis:
R = 72.72 + 0.004(Y ) + 4.26(P),
where:
R = annual revenue (in millions),
Y = per capita income of individuals in Consolidated’s sales area,
P = population of Consolidated’s sales area (in millions).
Analysis of past income statements has revealed that Consolidated
incurs annual operating ﬁxed costs of $80 million (including $40 million
in depreciation) and has a variable cost ratio of about 0.2. Interest
payments on the ﬁrm’s bond indebtedness have totaled $5 million
annually. The ﬁrm pays an average income tax of 40 percent.
1. Forecast total revenues for consolidated for 2015–2019 assuming
the following values:
Y
P
2015
$3,000
8.75M
2016
3,125
9.00
2017
3,300
9.40
2018
3,500
9.60
2019
3,800
10.00
--- page 220 ---

Analysis of Fixed Income Securities
197
The forecasted revenues would be:
2015
72.72 + (0.004)(3,000) + (4.26)(8.75) = $122.00 million
2016
72.72 + (0.004)(3,125) + (4.26)(9.00) = $123.56
2017
72.72 + (0.004)(3,300) + (4.26)(9.40) = $125.96
2018
72.72 + (0.004)(3,500) + (4.26)(9.60) = $127.62
2019
72.72 + (0.004)(3,800) + (4.26)(10.00) = $130.52
2. Prepare simpliﬁed pro forma income statements for 2015–2019.
(in millions)
2015
2016
2017
2018
2019
Revenues
$122.00 $123.56 $125.96 $127.62 $130.52
Fixed operating
costs
80.00
80.00
80.00
80.00
80.00
Variable operating
costs
24.40
24.71
25.19
25.52
26.10
Earnings before
interest and taxes
(EBIT)
17.60
18.85
20.77
22.10
24.42
Interest
5.00
5.00
5.00
5.00
5.00
Earnings before
taxes (EBT)
12.60
13.85
15.77
17.10
19.42
Taxes
5.04
5.54
6.31
6.84
7.77
Net income
7.56
8.31
9.46
10.26
11.65
3. Compute the times-interest-earned ratio expected for 2015–2019.
2015 :
17.60
5.00 = 3.52X
2016 :
18.85
5.00 = 3.77X
2017 :
20.77
5.00 = 4.15X
--- page 221 ---

198
Quantitative Financial Analytics
2018 :
22.10
5.00 = 4.42X
2019 :
24.42
5.00 = 4.88X.
4. How far would revenues have to decline before interest payments
would be endangered in 2015?
Revenues
$(X)
$106.25
Fixed operating costs
80.00
80.00
Variable operating costs
(0.2)(X)
21.25
EBIT
$5.00
$5.00
X −80.00 −(0.2)(X) = 5.00
X = $106.25 million
Revenues would have to decline by 11.5 percent from 2014
revenues and be 12.9 percent under the 2015 projection before
interest payments would be jeopardized.
5. What probability would one assign to the event: 2015 revenues
are less than $106.25 million? This is the toughest question the
analyst must answer, and it is obviously a very subjective matter.
A decline in revenues of the magnitude indicated would be possible
for ﬁrms in many industries. If Consolidated were a railroad, for
example, the probability of such an event might be reasonably
high. For a public utility, however, the chances of a decrease
in revenues of over 3 or 4 percent is not great. Manufacturing
concerns have varying patterns of revenue volatility, and the best
guide may be to examine the experience of past years.
6. Does the regression result help the analyst in determining the
probability of interest-payment jeopardization? One of the major
characteristics of regression techniques is that they only indicate
trends (positive or negative). Thus, a regression estimator will
not, by itself, aid the analyst in determining the probability that
a projection will be worse than expected.
However, the analyst may examine other statistics that will
help in this determination. Initially one may inspect the R2 value
--- page 222 ---

Analysis of Fixed Income Securities
199
to check on the closeness of ﬁt among the variables. A low R2
might reduce the conﬁdence in the estimated value and may
cause the analyst to re-examine the historical data (the regression
inputs) to determine whether large declines had been experienced
in the past. Next, one should re-examine the standard error of
the estimate. If the analyst believes the underlying distribution is
essentially normal, then the standard error of the estimate may
be used to determine the probability P (R ≤$106.25 million).
Suppose the revenue distribution for Consolidated is normally
distributed with a standard error of $2 million. Then, P(R ≤
$106.25 million) ∼= 0. For R ≤$106.25 million, a value almost 8
standard errors [that is (122 −106)/2] from the expected value
would have to occur. The probability of this event is extremely
small.
7. What other variables, in addition to revenue variability, would the
analyst have to examine in order to determine the probability that
interest payments would be jeopardized? From the example above,
the reader can recognize the importance of operating leverage
on interest payments. A relatively small decline in revenues
(11.5 percent) would completely wipe out EBIT for Consolidated.
This is true because of the high level of ﬁxed operating costs
incurred by the company. For a ﬁrm with a lower degree of
operating leverage, a larger decline in revenues could be tolerated
before interest payments would be endangered. Thus, in addition
to the stability of revenues, the analyst should examine the cost
structure of the ﬁrm in order to determine the probability of
interest-payment coverage as revenue declines.
8. Suppose revenues did indeed fall to $106.25 million. Would the
ﬁrm default on its bond interest payments? Not necessarily.
Interest payments are made out of cash ﬂows — not just earnings
before interest and taxes. A ﬁrm may continue to pay interest on
its indebtedness even though it is losing money. Several sources of
funds other than earnings can be employed.
(a) Cash generated from depreciation ﬂows, for example, may be
used to pay interest rather than replace plant and equipment.
--- page 223 ---

200
Quantitative Financial Analytics
When a ﬁrm uses depreciation ﬂows for this purpose, of
course, its long-run earnings potential is reduced.
(b) A ﬁrm may have built up a stock of cash that may be used
to make interest payments. If the cash ﬂows of the ﬁrm are
independent over time, then the cash account may be used for
interest payments during bad years and replenished during
good years. If, as is more likely, the ﬂows are dependent over
time, then one bad year would follow another and the cash
account would be soon depleted.
(c) The ﬁrm may borrow to meet interest obligations. Nevertheless, loans are granted for such purposes rarely, and then
only when it appears that the ﬁrm is temporarily suﬀering
an earnings decline.
(d) Historically, railroads had a habit of meeting debt charges by
deferring maintenance of equipment and right of way. Hence,
they allowed deterioration of facilities that eventually had to
be repaired or replaced. Even today, the rail analyst examines
the maintenance ratio when analyzing the position of a
railroad. Although all these methods of continuing interest
payments under depressed conditions may delay default,
there is a tendency for them to be stopgap measures that
only postpone the inevitable. Note that consolidation of the
railroads (from over 90 Class I roads 50 years ago to just
seven today) has signiﬁcantly reduced the practice of deferring
maintenance, and railroads like the Union Paciﬁc and the
BNSF (formerly the Burlington Northern Santa Fe and now a
subsidiary of Warren Buﬀet’s Berkshire Hathaway) are quite
strong ﬁnancially.
Coverage Ratios and Income Security
In addition to using the forecasting tools employed in the previous
section, the analyst will also use several ratios to aid him or her
in the determination of possible default. He will frequently compute
the time-interest-earned ratio for past years and compare the ﬁrm’s
ratio with that of other ﬁrms in the same business. He will also
--- page 224 ---

Analysis of Fixed Income Securities
201
examine the trend of the ratio for the ﬁrm over time. Of course, these
ratios should not be substitutes in analysis for forecasting. Rather,
they should serve as additional data to give added perspective to the
results obtained from projections.
When a ﬁrm has several bond issues outstanding, it is possible
to compute several variations of the times-interest-earned ratio.
The simplest of these ratios is computed by adding all interest
payments and dividing this sum into EBIT. The resulting ratio is
called the overall-interest-coverage ratio. A second group of ratios,
called cumulative-deduction-coverage ratios, attempts to diﬀerentiate
among bonds on the basis of their claim on earnings (and assets in
the case of liquidation in order to show a higher coverage for more
secure obligations). The interest coverage of claims is computed in
order of priority. First, the interest requirement for the most senior
security is divided into EBIT to obtain its coverage ratio. Next,
the claims of junior securities are added to the denominator of the
coverage ratio successively in order to determine the coverage of each
issue.
Although the exact arrangement of priorities can be ascertained
only from the indentures of the relevant securities, the general order
of priority is: ﬁrst mortgage bonds and equivalents (for example,
equipment trust certiﬁcates, collateral trust agreements, and so on),
second mortgage bonds, debentures, subordinated debentures, junior
subordinated debentures, preferred stock, and, ﬁnally, common
stock. A third method of computing coverage ratios is the prior
deductions method. Instead of adding the interest requirement of
senior issues to the denominator as in the cumulative deduction
method, this approach subtracts them from the numerator (EBIT).
The coverage is then computed as [(EBIT −prior charges)/interest
on security under analysis]. The computation may produce the
absurd result that a junior obligation appears to be safer than a
senior issue. Although this method gives no useful information, many
investment banking houses once employed it to give a deceptively
good picture for a bond they were about to underwrite. It should be
avoided by the analyst. These three methods of computing coverage
ratios are illustrated below.
--- page 225 ---

202
Quantitative Financial Analytics
The long-term debt (LTD) section of the balance sheet of the
Atlantic and Paciﬁc R.R. is as follows (in order of earnings claim):
First mortgage 5’s of 2025
$24,200,000
Second mortgage 8 1/8’s of 2019
20,000,000
Collateral trust notes 4’s of 2025
50,000,000
Subordinated debentures 9’s of 2030
6,000,000
$100,200,000
Earnings before interest and taxes for Atlantic and Paciﬁc is
$10,750,000. The overall interest coverage would be:
(0.05)(24.2 million) =
$1,210,000
(0.08125)(20 million) =
1,625,000
(0.04)(50 million) =
2,000,000
(0.09)(6 million) =
540,000
$5,375,000
10,750,000/5,375,000 = 2.0X.
The cumulative coverage for each issue would be:
First mortgage bonds
(10,750,000)/(1,210,000) = 8.9X.
Second mortgage bonds
(10,750,000)/(1,210,000 + 1,625,000) = 3.8X.
Collateral trust notes
(10,750,000)/(1,210,000 + 1,625,000 + 2,000,000) = 2.2X.
Subordinated debentures
(10,750,000)/(1,210,000 + 1,625,000 + 2,000,000 + 540,000) = 2.0X.
Notice that the coverage for the most junior issue is the same as the
overall coverage.
--- page 226 ---

Analysis of Fixed Income Securities
203
The prior deduction coverage for each issue would be:
First mortgage bonds
(10,750,000)/(1,210,000) = 8.9X.
Second mortgage bonds
(10,750,000 −1,210,000)/(1,625,000) = 5.9X.
Collateral trust notes
(10,750,000 −1,210,000 −1,625,000)/(2,000,000) = 3.9X.
Subordinated debentures
(10,750,000 −1,210,000 −1,625,000 −2,000,000)/(540,000) = 10.9X.
Note the absurd result here indicates greater security for the
subordinated debentures than for the ﬁrst mortgage bonds.
Protection in Case of Financial Diﬃculty
The major determinants of the ﬁrm’s ability to make its interest
payments are the volume of interest payments the ﬁrm owes in each
period and the earnings available for those payments. Other tests
used to determine the safety of the coupon and principal payments for
a bond were discussed in Chapter 4. The degree of ﬁnancial leverage
possessed by the ﬁrm may be indicated by various debt-to-equity and
debt-to-total-capital ratios.
The asset security of obligations may be tested by computing
several asset-coverage ratios (such as the tangible asset debt coverage). Although the capital-structure and asset-coverage ratios do
provide additional information about the position of the ﬁrm’s debt
obligations, they are most useful as indicators of what the holders
might receive in case of liquidation or reorganization. Because the
primary reason for bond purchases is the avoidance of any problems
associated with payment default or delay, the analyst should be
not be satisﬁed simply because a ﬁrm has little indebtedness or a
bond is well secured by assets in case of diﬃculty. Of course, once
the analyst is conﬁdent that coupon and principal payments are
adequately protected by future earnings, added security provided by
--- page 227 ---

204
Quantitative Financial Analytics
low indebtedness and large asset holdings can be considered a safety
hedge in case a very poor state of events develops.
When ﬁnancial diﬃculties do occur for a company, there are
several courses of action available. If creditors believe that the ﬁrm
will never be able to earn enough to repay its obligations, they may
sue to place the ﬁrm in bankruptcy. If it is decided that the ﬁrm
should be liquidated, a referee is appointed to sell the ﬁrm’s assets
at the best price he or she can obtain. The funds received are used
ﬁrst to pay for the cost of liquidation (legal fees and so on). Next,
any back taxes, wages payable, and certain other claims are paid.
Secured creditors are entitled to the proceeds obtained from the sale
of the assets against which they have claims. In case their claims
are not fully satisﬁed, they become general creditors for the balance
owed them. Remaining funds are distributed to the general creditors.
If funds are insuﬃcient to meet all obligations, they are pro-rated by
size of claim. When the general creditors are satisﬁed, distribution
is made to subordinated creditors and then preferred stockholders.
The balance, if any, goes to the common stockholders.
Because the process of bankruptcy is expensive administratively,
many creditors will make great concessions to avoid the procedure.
A frequently employed method is simply to give the debtor an
extension, that is, more time to pay the obligation. This method
is particularly attractive if interest payments are still being made
(fully or partially) and only principal payments are being missed.
A second method, used generally where interest payments have
been stopped, is the composition, by which less than the total
amount due is accepted as full payment of the obligation. Many
creditors are willing to accept such an arrangement, because the
funds become available for investment elsewhere fairly quickly and
also the settlement may be greater than that which could be obtained
from legal proceedings.
It may be decided that a ﬁrm should be reorganized rather than
liquidated under bankruptcy. This is almost always the case for
companies engaged in providing a vital public service (such as public
utilities and railroads). Under reorganization, a receiver is appointed
by the courts to operate the business until a satisfactory plan can be
worked out. This process may take months or even years. During
--- page 228 ---

Analysis of Fixed Income Securities
205
the Great Depression of the 1930s, for example, many railroads
were in receivership for 20 years before a reorganization could be
accomplished. The reorganization plan is determined by a referee
who decides upon a new capital structure for the ﬁrm.
The objective of the new structure is to make it possible for
the ﬁrm to become viable again. This usually means that the ﬁrm
will not be overly burdened with ﬁxed charges. Because interest on
income bonds must be paid only if earned, this security has become
a standard part of many reorganizations. (The poor reputation
generally accorded income bonds in the past is no doubt accounted
for by its use in reorganizations.)
Reorganization may take place under two rules. The absolute
priority rule settles claims with strict regard to their legal priority,
and all senior claims must be satisﬁed in full before junior claims can
be settled. Under relative priority, all claimants participate in the
reorganization (including common stockholders), although heavier
losses are apportioned to junior claims than senior. One method of
distributing new securities under relative priority is to allocate on
the basis of the market values of the old securities. We may consider
a couple of examples.
The Singleton Publishing Co. is in ﬁnancial diﬃculty. The company has been unable to meet interest payments on its subordinated
debentures for two years, and preferred stock dividends have been
passed for ﬁve years. Junior bondholders have granted two extensions
of interest payments, but they are unwilling to grant a third. Lawyers
for the company have polled the bondholders about the possibility of
a composition, but full payment was demanded. Hence, the ﬁrm has
petitioned to be declared bankrupt. A balance sheet for Singleton is
given below (in 000’s):
Cash
$ 50,000
Current liabilities
$ 200,000
Receivables
100,000
Mortgage bonds
300,000
Inventories
350,000
Subordinated debentures
300,000
Fixed assets
500,000
Preferred stock
100,000
$1,000,000
Common equity
100,000
$1,000,000
--- page 229 ---

206
Quantitative Financial Analytics
Receivables could be factored for 80 percent of their book value.
Inventories can be sold at 70 percent of book value, and ﬁxed assets
could be liquidated at 40 percent of book value. It is expected that
liquidation costs would be about $100 million. Among the ﬁrm’s
current liabilities are $50 million in wages payable, and $10 million
in accrued taxes. Mortgage bondholders have a prior claim against all
ﬁxed assets. Upon liquidation, creditors would receive the following
proceeds (in 000’s):
Cash
$50,000
Receivables
80,000
Inventories
245,000
Fixed assets
200,000
$575,000
(a) First mortgage bondholders would have claim to $200 million
from the sale of ﬁxed assets and would become general creditors for
the balance of $100 million. (b) Liquidation costs, wages payable,
and accrued taxes would have a claim against $160 million. (c) The
balance ($575 million less $200 million less $160 million equals
$215 million) would go to the general creditors. Other current
liabilities are $140 million. Subordinated debenture holders have a
claim of $300 million.
Thus, the payment to current liabilities would be 14/54 ×
$215 million
∼= $55 million, ﬁrst mortgage bondholders would
initially get an additional 10/54 × $215 million ∼= $40 million,
and subordinated holders would claim 30/54 × $215 million ∼=
$120 million. However, because the debentures are subordinated to
the mortgage bonds, the bondholders are entitled to have satisﬁed
any remaining claims against the portion due the debentures. Thus,
$60 million would be transferred from the debenture claim to the
mortgage bondholders. In sum, the mortgage bondholders would
be paid in full, the other liability holders would be paid about
39 percent of their claim, and the debenture holders would receive
about 20 percent of their claim.
