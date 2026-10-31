# Practical Portfolio Performance Measurement and Attribution -- Bacon, Carl R_ -- 10_1002_9781119206309, 2012 jan 02 -- John Wiley & Sons, Inc_ -- doi 10_1002_9781119206309 -- bc9440f8ca87cf4e34d9c3fda66edb46 -- Anna.pdf — pages 115–134

--- page 115 ---

JWBK178-04
JWBK178-Bacon
July 28, 2008
11:13
Char Count= 0
Risk
103
Downside risk σ
Return
σ
rT
M2 for Sortino
A
DM
D
Figure 4.17
M2 for Sortino
portfolio with the same Sortino ratio of portfolio A but at the same downside risk of the
benchmark:
M2
S
rP
Sortino ratio
(
DM
D)
(4.95)
Benchmark downside risk, omega, omega–Sharpe ratio and M2
S are calculated in Table 4.13.
Omega excess return
Another form of downside risk-adjusted return is omega excess return (Sortino et al., 1997) (not
related to the omega ratio). Similar to differential return the downside risk-adjusted benchmark
return is calculated by multiplying the downside variance of the style benchmark by 3 times
the style beta.
The 3 is arbitrary and assumes the investor requires 3 units of return for one unit of variance
(3
2
MD effectively takes the place of the benchmark excess return above the risk-free rate
in the differential return calculation). The style beta adjusts for the downside risk taken by
the portfolio manager by taking the ratio of the downside risk of the portfolio divided by the
downside risk of the style benchmark:
Downside risk-adjusted-style benchmark 3
S
2
MD
(4.96)
Omega excess return
rp
3
S
2
M D
(4.97)
where:
2
M D
style benchmark variance.
Style beta
S
D
MD
(4.98)
For much the same reasons as I prefer M2 excess return above differential return I prefer M2
for Sortino to omega excess return.
--- page 116 ---

JWBK178-04
JWBK178-Bacon
July 28, 2008
11:13
Char Count= 0
104
Practical Portfolio Performance Measurement and Attribution
Hurst index
The Hurst index† is a useful statistic for detecting if a portfolio manager’s returns are mean
reverting (anti-persistent), totally random or persistent. It is calculated as follows:
H
log (m)
log (n)
(4.99)
where:
m
[max (ri)
min (ri)]
p
(4.100)
n
number of observations.
A Hurst index between 0 and 0.5 would suggest a portfolio manager’s series of returns are
mean reverting (anti-persistent).
A Hurst index of 0.5 would suggest the series of returns was totally random.
A Hurst index between 0.5 and 1 would suggest the series of returns are persistent, i.e. there
is memory in the return series.
Clearly, persistent positive returns or excess returns would be a desirable property for an
asset manager.
FIXED INCOME RISK
Duration (or volatility)
In many ways ﬁxed income securities or bonds are easier to measure than equities; they consist
(for the most part) of predictable future cash ﬂows in the form of coupon payments and a ﬁnal
redemption value.
Durationisdeﬁnedastheaveragelifeofthepresentvaluesofallfuturecashﬂowsfromaﬁxed
income security. Duration is a systematic risk or volatility measure for bonds. In calculating
the present value of the future cash ﬂows, a discount rate equal to the redemption yield is used.
This measures the ﬁxed income securities’ sensitivities to changes in interest rates.
Macaulay duration
Frederick Macaulay (1938) was among the ﬁrst to suggest the use of duration for studying the
returns on bonds:
D
n
i
1
Fi
ti
dti
n
i
1
Fi
dti
(4.101)
where:
n
number of future coupon and capital repayments
Fi
ith future coupon or capital repayment
ti
time in years to the ith coupon or capital repayment
d
discount factor.
† H.E. Hurst originally developed the Hurst index to help in the difﬁcult task of establishing optimal water storage along the
Nile. Nile ﬂoods are extremely persistent as evidenced by a Hurst index of 0.9. Equity markets have a Hurst index of around 0.7. See
Clarkson (2001).
--- page 117 ---

JWBK178-04
JWBK178-Bacon
July 28, 2008
11:13
Char Count= 0
Risk
105
Note that:
d
1
(1
y)
(4.102)
where:
y
yield to maturity or redemption yield.
The denominator in Equation (4.101) is equal to the present value of future coupon and capital
repayments of the securities or, in the other words, the price P:
P
n
i
1
Fi
dti
(4.103)
Substituting Equation (4.103) into Equation (4.101) we have the formula for Macaulay duration:
D
n
i
1
Fi
ti
dti
P
(4.104)
Modiﬁed duration
A slight variant of Macaulay duration is modiﬁed duration:
MD
D
1
y
k
(4.105)
where:
k
number of cash ﬂows or coupons per year.
Duration measures the sensitivity of a bond’s price to changes in yield. Price changes can be
estimated by:
P
MD
y
(4.106)
Macaulay–Weil duration
There is no reason why the discount rate should be constant for all coupon payments; in fact,
interest rates are likely to be different for different time periods. Macaulay–Weil duration uses
the appropriate spot rate for each cash ﬂow and is therefore more accurate.
Price, Macaulay, modiﬁed and Macaulay–Weil duration are calculated for a simple bond in
Table 4.14.
Portfolio duration
Durations in a ﬁxed income portfolio or benchmark are additive. The entire duration of the
portfolio can be computed directly from the weighted sum of each bond in the portfolio:
Portfolio duration
i
n
i
1
i
MDi
(4.107)
--- page 118 ---

JWBK178-04
JWBK178-Bacon
July 28, 2008
11:13
Char Count= 0
Table 4.14
Price, Macaulay, modiﬁed and Macaulay–Weil duration
20-year bond 6% coupon
Macaulay
Macaulay–Weil
Period
Cash ﬂow
Present value
Time
present value
Spot rate
Present value
Time
present value
1
6
5.78
5.78
3.5
5.80
5.80
2
6
5.56
11.12
3.5
5.60
11.20
3
6
5.35
16.05
3.5
5.41
16.23
4
6
5.15
20.60
3.5
5.23
20.91
5
6
4.96
24.79
3.5
5.05
25.26
6
6
4.77
28.63
3.5
4.88
29.29
7
6
4.59
32.15
3.5
4.72
33.01
8
6
4.42
35.36
3.5
4.56
36.45
9
6
4.25
38.29
3.75
4.31
38.77
10
6
4.1
40.95
3.75
4.15
41.52
11
6
3.94
43.36
3.75
4.00
44.02
12
6
3.79
45.53
3.75
3.86
46.29
13
6
3.65
47.48
3.75
3.72
48.33
14
6
3.52
49.21
3.75
3.58
50.17
15
6
3.38
50.75
3.75
3.45
51.81
16
6
3.26
52.11
3.75
3.33
53.27
17
6
3.13
53.29
4.0
3.08
52.36
18
6
3.02
54.31
4.0
2.96
53.31
19
6
2.9
55.18
4.0
2.85
54.11
20
106
49.39
987.75
4.0
48.38
967.54
Price
128.91
1692.70
Price
128.91
1679.67
IRR (y)
3.89%
IRR (y)
3.89%
Macaulay duration
1692 7
128 91
13 13
Macaulay–Weil
duration
1679 67
128 91
13 03
Modiﬁed duration
13 13
1 0389
12 64
Modiﬁed duration
13 03
1 0389
12 54
106
--- page 119 ---

JWBK178-04
JWBK178-Bacon
July 28, 2008
11:13
Char Count= 0
Risk
107
Effective duration (or option-adjusted duration)
Modiﬁed duration does not calculate the effective duration of the bond if there is any optionality
in future payments. To calculate the effective duration the estimate price must be calculate for
both a positive and negative change in interest rates:
ED
P
P
2
P
y
(4.108)
where:
y
change in interest rates
P
estimated price if interest rate is decreased by
y
P
estimated price if interest rate is increased by
y.
If there is no optionality in future payments effective duration will be identical to modiﬁed
duration.
The effective duration of the bond used in Table 4.14 is calculated in Table 4.15 based on a
parallel change of 25 basis points. Notice that the answer is close to modiﬁed Macaulay–Weil
duration as expected.
Duration to worst
Duration to worst is identical to modiﬁed duration but if there is optionality using the cash
ﬂow this results in the worst yield for the investor.
Table 4.15
Effective duration
20 year bond 6% coupon
0.25% parallel shift
0.25% parallel shift
Cash ﬂow
Spot rate (%)
Present value
Spot rate (%)
Present value
6
3.75
5.78
3.25
5.81
6
3.75
5.57
3.25
5.63
6
3.75
5.37
3.25
5.45
6
3.75
5.18
3.25
5.28
6
3.75
4.99
3.25
5.11
6
3.75
4.81
3.25
4.95
6
3.75
4.64
3.25
4.80
6
3.75
4.47
3.25
4.65
6
4.0
4.22
3.5
4.40
6
4.0
4.05
3.5
4.25
6
4.0
3.90
3.5
4.11
6
4.0
3.75
3.5
3.97
6
4.0
3.60
3.5
3.84
6
4.0
3.46
3.5
3.71
6
4.0
3.33
3.5
3.58
6
4.0
3.20
3.5
3.46
6
4.25
2.96
3.75
3.21
6
4.25
2.84
3.75
3.09
6
4.25
2.72
3.75
2.98
106
4.25
46.11
3.75
50.76
Price
124.96
Price
133.04
Effective duration
ED
P
P
2
P
y
133 04
124 96
2
128 91
0 25%
12 54
--- page 120 ---

JWBK178-04
JWBK178-Bacon
July 28, 2008
11:13
Char Count= 0
108
Practical Portfolio Performance Measurement and Attribution
Convexity
Duration is only the ﬁrst order approximation in the change of the ﬁxed income securities’ price.
The approximation is due to the fact that a curved line represents the relationship between bond
prices and interest rates. Duration assumes there is a linear relationship. This approximation
can be improved by using a second approximation, convexity:
C
n
i
1
Fi
ti
(ti
1)
dti
P
(4.109)
Modiﬁed convexity
MC
d2
n
i
1
Fi
ti
(ti
1)
dti
P
(4.110)
Effective convexity
Again, modiﬁed convexity does not calculate the effective convexity of the bond if there is any
optionality in future payments. Using estimated prices to calculate effective convexity:
EC
P
P
2
P
P
(
y)2
(4.111)
Duration beta
The ratio of the portfolio’s sensitivity to yield changes with that of the benchmark provides a
measure equivalent to beta:
D
DP
DM
(4.112)
Reward to duration
Reward to duration is the Treynor ratio for ﬁxed income portfolios with modiﬁed duration
replacing beta as the measure of systematic risk.
Reward to duration
rP
rF
MD
(4.113)
WHICH RISK MEASURES TO USE?
Risk like beauty is very much in the eye of the beholder. Determining which risk measure to use
is determined by the objectives and preferences of the investor. Although most risk measures
are easy to calculate they are not all easy to interpret and are often contradictory.
My advice is to calculate only a few risk measures which are consistent with the investment
objectives and easily understood by all parties.
--- page 121 ---

JWBK178-04
JWBK178-Bacon
July 28, 2008
11:13
Char Count= 0
Risk
109
Whichever risk measure you decide to focus on it is important to monitor the change in that
measure over time. Risk controllers can never assume the measure is accurate; far better to
analyse the change over time and investigate any sudden changes.
The measure may be incorrect but any sudden change provides additional information. The
change may result from data errors, system or model errors, change in model assumptions, or
an intentional or unintentional change in portfolio risk. Whatever the reason for the change, it
should be discussed with the portfolio manager and fully understood.
Most risk measures take the same form, that of a ratio of reward to risk. A summary of
reward to risk ratios is shown in Table 4.16.
These measures are most suitable for ranking portfolio performance. The most appropriate
ratios take account of investors’ risk tolerances. In most circumstances it would be inappropriate to use more than one ratio. For downside risk measures the minimum acceptable or
target return should be consistent with the asset manager’s investment objectives and strategy.
There is relatively little value in using a range of minimum target returns to analyse portfolio
performance if the asset manager is targeting relative return.
Ratios all suffer the same problem, they allow us to rank portfolios in order of preference but
do not inform us in terms so that we can understand the return advantage of a higher ranking.
Risk-adjusted returns on the other hand convert ratios to returns we can understand. Riskadjusted returns are shown in Table 4.17. Although M2 is shown for total risk and downside
risk, in theory M2 can be calculated for any risk statistic.
Ex post risk measures will not change dramatically but for effective risk control it is essential
to compare the predictive risk calculated by internal systems with the actual realised risk of
portfolios.
A number of statistics summarised in Table 4.18 are descriptive only and cannot be used
for ranking portfolios but do provide additional information about the nature of portfolio
returns.
Risk efﬁciency ratio
It is important to monitor changes over time in both the ex ante and ex post tracking errors.
It is also important to compare the forecast tracking error with the realised tracking error to
gauge how close the forecast is to reality.
The risk efﬁciency ratio compares realised risk with forecast risk–ideally we would like the
ratio to be 1 indicating that our forecasting tools were efﬁcient. If the ratio is much greater
than 1 then we are aware that our forecasting tool is underestimating relative risk:
Ex post tracking error
Ex ante tracking error or Realised risk
Forecast risk
(4.114)
Or alternatively:
Ex post VaR
Ex ante VaR
(4.115)
Fund rating systems
Noel Amenc and Veronique Le Sourd (2007) wrote a very interesting article on fund rating systems critiquing the methods of Standard & Poor’s Micropal, Morningstar and Lipper, essential
--- page 122 ---

JWBK178-04
JWBK178-Bacon
July 28, 2008
11:13
Char Count= 0
Table 4.16
Reward to risk ratios
Return measure vertical axis
Risk measure horizontal axis
Ratio
numerator
denominator
Comment
Traditional
Sharpe
Return above risk-free rate
Total risk variability Standard
deviation
Reward to variability. The grandfather of all reward to risk ratios
Treynor
Return above risk-free rate
Systematic risk
or volatility
Reward to volatility. Actually deﬁned before the Sharpe ratio but
rarely used in practice
Information
Excess return
Tracking error Relative risk
Frequently used. Favoured by institutional asset managers
Appraisal
Jensen’s alpha
Speciﬁc risk
Rarely used
Modiﬁed Jensen
Jensen’s alpha
Systematic risk
or volatility
Rarely used
Drawdown
Calmar
Return above risk-free rate
Maximum drawdown
Quite common for commodity, future and hedge funds
Burke
Return above risk-free rate
Drawdown deviation
Penalises deep drawdowns in particular
Sterling–Calmar
Return above risk-free rate
Average annual maximum
drawdown
Most common form of Sterling ratio
Sterling
Return above risk-free rate
Average drawdown
Similar to Sharpe–omega ratio. Multiple deﬁnitions of average
drawdown used
Martin
Return above risk-free rate
Ulcer index
Similar to Burke. Penalises both depth and duration of
drawdowns
Pain
Return above risk-free rate
Pain index
Similar to Martin index but not squared
Downside
Sortino
Return above risk-free rate
Downside risk
The most appropriate downside risk statistic
Upside potential
Upside potential
Downside risk
Combines upside potential with downside risk
Omega
Upside potential
Downside potential
Similar to upside potential but extreme losses are less harshly
penalised
110
--- page 123 ---

JWBK178-04
JWBK178-Bacon
July 28, 2008
11:13
Char Count= 0
Sharpe–omega
Return above risk-free rate
Downside potential
Identical ranking statistic to omega
Prospect
Utility-adjusted return
Downside risk
Gives greater weight to negative returns
Volatility skewness
Upside variance
Downside variance
Similar to omega but extreme returns are more signiﬁcant on both
the upside and downside
Variability skewness
Upside risk
Downside risk
Square root of volatility skewness
VaR
Reward to VaR
Return above risk-free rate
VaR
Unconcerned with shape of tail
Conditional Sharpe
Return above risk-free rate
Conditional VaR Tail loss or tail
VaR Expected shortfall
Takes account of tail shape
Modiﬁed Sharpe
Return above risk-free rate
Modiﬁed VaR
Adjusts for Skewness and kurtosis
Other
Adjusted Sharpe
Return above risk-free rate
Risk, skewness and kurtosis
For those concerned takes account of higher moments.
Surprisingly easy to calculate
Reward to duration
Return above risk-free rate
Duration Systematic risk
volatility
For ﬁxed income only. Equivalent to Treynor ratio
Kappa
Return above risk-free rate
lth lower moment
Generalised downside measure. For l
1 equivalent to Sharpe–
omega ratio; for l
2 equivalent to Sortino ratio
111
--- page 124 ---

JWBK178-04
JWBK178-Bacon
July 28, 2008
11:13
Char Count= 0
112
Practical Portfolio Performance Measurement and Attribution
Table 4.17
Risk-adjusted return measures
Measure
Risk adjusted for
Comment
Total return
M2
Total risk variability
The original and my preferred measure. Underused throughout the asset management industry
M2 for downside risk
Downside risk
Rarely used although demonstrably better than
Sortino ratio
Excess return
Jensen’s alpha
Systematic risk
By far the most common. Term often confused
with simple excess return. Jensen’s alpha is
more accurately excess return adjusted for systematic risk
Regression alpha
Systematic risk
Similar to Jensen’s alpha ignoring risk-free rate
M2 excess
Depends on the M2 measure used
Most often expressed arithmetically but
geometric is more appropriate
Net selectivity
Systematic risk and diversiﬁcation
Good measure for mutual ﬁnds. Early
version of attribution
Differential return
Total risk
Benchmark return adjusted to risk of portfolio.
Less effective than M2 excess
GH1
Total risk
Efﬁcient frontier equivalent of differential return
GH2
Total risk
Efﬁcient frontier equivalent of M2
Omega excess
Downside-style variance
Rarely used
reading for any portfolio manager benchmarked against one of these peer group providers.
Good ratings from these organisations will inﬂuence retail investors and drive sales, therefore it is essential that portfolio managers understand how these ratings are calculated. In
effect, these organisations select the most appropriate risk measures on behalf of the retail
investor.
The Standard & Poor’s Micropal star rating is based on the information ratio relative to the
sector average (or median) performance of the funds belonging to the same peer group over a
36-month period. Stars are attributed as follows:
Fund percentile
Rating
Top 10%
*****
10% to 30%
****
30% to 50%
***
50% to 75%
**
Bottom 25%
*
Apart from the problems of peer groups already discussed in Chapter 3, the fact that the
benchmark used for the calculation of the information ratio is the average return of the peer
group can lead to the counterintuitive result that a fund with less absolute variability is less
well regarded simply because it has greater variability against the competition; low absolute
risk is not necessarily rewarded in this rating system.
--- page 125 ---

JWBK178-04
JWBK178-Bacon
July 28, 2008
11:13
Char Count= 0
Risk
113
Table 4.18
Descriptive statistics
Statistic
Comment
Regression statistics
Covariance
Tendency of the portfolio and benchmark returns to
move together
Correlation
Standardised covariance
R2
Square of correlation
Beta
Systematic risk or volatility
Speciﬁc risk
Standard deviation of the error term
Other
Tracking error, relative risk, active risk
Standard deviation of excess returns. The dominant
measure of risk for long only institutional asset managers
Total risk, standard deviation variability
Standard deviation of portfolio returns
Downside risk
Semi-standard deviation of returns below target
Kurtosis
Measures ﬂatness of distribution
Skewness
Determines if returns are positively or negatively skewed
Hurst index
Persistency
Average drawdown
Maximum drawdown
Maximum loss over any investment period. Buy at the top,
sell at the bottom
Fixed income measures
Modiﬁed duration
Systematic risk for bonds
Convexity
Rate of change of duration
Value at Risk statistics
VaR
Expected maximum loss with certain level of conﬁdence
Conditional VaR, Expected shortfall
Tail loss
Modiﬁed VaR
VaR modiﬁed for kurtosis and skewness
Potential gain
Positive (right-hand) equivalent of Value at Risk
Morningstar created their own risk-adjusted performance measure MRAR( ):
MRAR( )
1
T
t
T
t
1
1
rt
1
rFt
12
1
(4.116)
where:
a parameter reﬂecting the investor’s degree of risk aversion.
This measure is subtracted from the annualised excess return relative to the risk-free rate over
36 months. Morningstar set
2 thus more variable excess returns relative to the risk-free
rate are penalised. Stars are attributed as follows:
Fund percentile
Rating
Top 10%
*****
10% to 32.5%
****
32.5% to 67.5%
***
67.5% to 90%
**
Bottom 10%
*
--- page 126 ---

JWBK178-04
JWBK178-Bacon
July 28, 2008
11:13
Char Count= 0
114
Practical Portfolio Performance Measurement and Attribution
Lipper Micropal provides several different rankings using total return, persistence, capital
preservationandexpenseratios.[ForpersistencetheHurstindexisused,forcapitalpreservation
the sum of negative returns over the cumulative period]. Lipper Micropal scores are attributed
as follows:
Fund percentile
Score
Top 20%
Lipper leaders
20% to 40%
2
40% to 60%
3
60% to 80%
4
Bottom 20%
5
Scores are allocated for 3, 5, 10 years and overall. The overall calculation uses an equal
weighted average percentile for each period thus giving greater weight to recent performance.
The usefulness of these rankings will very much depend on the quality and monitoring of
each sector to ensure consistency by the peer group provider and the relevance of the risk
measure to the investor.
RISK CONTROL STRUCTURE
Performance measurers have a key role to play in the risk control environment of asset managers. In the ideal asset management organisation I would have performance measurement,
risk control, the legal department and the internal audit function reporting to the head of middle ofﬁce. Performance measurers should never report to the front ofﬁce or the marketing
department.
For effective risk management in an asset management ﬁrm the following should be in place:
(1) Written risk policy. To provide a framework for the risk control environment every asset
management ﬁrm should have a risk policy that clearly articulates the ﬁrm’s attitude to
risk.
(2) Independence. For effective risk control it is essential there are appropriate checks and
balances within the ﬁrm with a clear front, middle and back ofﬁce structure with clear
areas of responsibility and reporting lines.
Board
Middle office
Back office
Front office
Performance
measurement
Risk control
Legal
Internal audit
Figure 4.18
Risk control structure
--- page 127 ---

JWBK178-04
JWBK178-Bacon
July 28, 2008
11:13
Char Count= 0
Risk
115
(3) Risk awareness. Risk awareness should be embedded within the ﬁrm. All employees will
own some aspect of risk, it is essential they understand the risks they own and are constantly
self-assessing their own risks. Once identiﬁed there are four possible responses to risk:
(a) Ignoretheidentiﬁedrisk.Ariskalthoughidentiﬁedmaybeignoredifthecost(including
opportunity cost) of controlling is greater than the potential cost of risk failure.
(b) Mitigate. Arranging appropriate insurance cover may mitigate the cost of risk failure.
(c) Control. Risk may be controlled by establishing risk limits and establishing monitoring
procedures.
(d) Eliminated. It may be appropriate to eliminate an identiﬁed risk by ceasing that type
of activity.
(4) Clear risk limits. Risk limits should be clear and unambiguous and agreed by the client
and asset manager in the investment management agreement.
(5) Risk and performance attribution. The sources of risk and return should be identiﬁed
and monitored independently using performance return attribution and other techniques.
Accurate return and risk attribution can be used to identify the consistency of added value
across the ﬁrm and consistency with the agreed investment objectives.
(6) Appropriate risk-adjusted measures. Risk and reward should be combined in risk-adjusted
performance measures appropriate to the investment management strategy.
(7) Review process for new products, instruments and strategies. All new products, instruments
and strategies should be rigorously reviewed. For example, a new derivative instrument
may meet the needs of the portfolio manager but could generate signiﬁcant operational
and counterparty risks that must be assessed and approved.
An appropriate risk control infrastructure for an asset management ﬁrm would include:
(1) Risk management committee. Reporting to the board, probably chaired by the head of risk
control. Coordinating all risk control activity including senior representatives from front,
middle and back ofﬁce. Responsible for portfolio risk, counterparty risk, compliance risk,
review of insurance arrangements disaster recovery and systems change control.
(2) Portfolio risk committee. Reporting to the risk management committee, probably chaired
by the head of front ofﬁce. Review that portfolios are managed within client expectations
and mandate restrictions. Approve new products, strategies and instruments.
(3) Credit risk committee. Reporting to risk management committee. Approve counterparties
and limits and monitor ﬁrm exposures.
(4) Operational risk committee. Reporting to risk management committee. Responsible for
error monitoring and information quality.
--- page 128 ---

JWBK178-05
JWBK178-Bacon
March 28, 2008
13:7
Char Count= 0
5
Performance Attribution
Never try to walk across a river just because it has an average depth of four feet.
Milton Friedman (1912–2006)
Deﬁnition
Performance attribution is a technique used to quantify the excess return of a
portfolio against its benchmark into the active decisions of the investment decision process.
Performance return attribution is a key management tool for several key stakeholders in the
asset management process.
Above all it is the key tool for performance analysts; it allows them to participate in the
investment decision process and demonstrably add value, thus justifying their salary. Performance return attribution, together with risk analysis, is the key tool that allows the analyst
to understand the sources of return in a portfolio and to communicate that understanding to
portfolio managers, senior management and clients.
Effective attribution requires that the analyst thoroughly understands the investment decision
process. The task of the analyst is to quantify the decisions taken by the portfolio manager. If
the analyst can demonstrate an understanding of the decision process and accurately quantify
the decisions taken then the conﬁdence of the portfolio manager will soon be gained. There is
little value in analysing factors that are not part of the decision process.
Portfolio managers are obviously major users of attribution analysis. Clearly, they will
have a good qualitative understanding of the portfolio but not necessarily a good quantitative understanding. It is all too easy to overestimate the impact of good performing securities and underestimate failures. It is even harder, sometimes, to consider the impact of
stocks not held in the portfolio. Stocks represented in the index but not in the portfolio are
often large “bets” and may have a signiﬁcant impact on relative performance, positive or
negative.
Attribution analysis provides a good starting point for a dialogue with clients entering a discussion on the positive and negative aspects of recent performance. It is possible to use attribution analysis extremely aggressively, identifying underperformance early
and visiting clients with a thorough explanation of underperformance. It is crucial to gain
the conﬁdence of the client by demonstrating a good understanding of the drivers of
performance.
Senior management take an active interest in attribution analysis to provide them with a tool
to monitor their portfolio managers. They will be keen to identify performance outliers – good
or bad – and to ensure that value is added consistently across the ﬁrm.
ARITHMETIC ATTRIBUTION
The foundations of performance attribution were established in two articles published by
Brinson et al. (1986) and Brinson and Fachler (1985) now collectively know as the Brinson
model.
117
Practical Portfolio Performance Measurement
and Attribution, Second Edition
By Carl R. Bacon
Copyright © 2008 John Wiley & Sons Ltd.
--- page 129 ---

JWBK178-05
JWBK178-Bacon
March 28, 2008
13:7
Char Count= 0
118
Practical Portfolio Performance Measurement and Attribution
These articles build on the assumption that the total portfolio returns and benchmark returns are the sum of their parts; in other words, both portfolio and benchmark returns can be
disaggregated as follows:
Portfolio return
r
i
n
i
1
i
ri
(5.1 or 2.33)
where
i
weight of the portfolio in the ith asset class (note
i
n
i
1
i
1)
ri
return of the portfolio assets in the ith asset class:
Benchmark return
b
i
n
i
1
Wi
bi
(5.2 or 3.6)
where
Wi
weight of the benchmark in the ith asset class (note also
i
n
i
1
Wi
1)
bi
return of the benchmark in the ith asset class.
The challenge for single period attribution is to quantify each of the portfolio manager’s active
decisions that contribute to the difference between the portfolio return r and the benchmark
return b.
Brinson, Hood and Beebower
Brinson, Hood and Beebower suggested a model to break down the arithmetic excess return
(r
b) assuming a standard investment decision process in which the portfolio manager seeks
to add value through both asset allocation and security selection.
In asset allocation the portfolio manager (or asset allocator) will seek to add value by
taking different asset category (or sector) weights in the portfolio in comparison to category
benchmark weights. A category weight in the portfolio greater than the equivalent benchmark
category weight would be described as overweight and a lesser weight would be described as
underweight.
Clearly, the asset allocator will aim to overweight good performing categories and underweight poor performing categories. In their original article Brinson, Hood and Beebower
called this impact timing; asset or market allocation is now a more common and appropriate
description.
In security selection the portfolio manager (or stock selector) will seek to add value by
selecting individual securities within the asset category.
Again the stock selector will aim to be overweight in good-performing securities and underweight in poor-performing securities
Asset allocation
To identify the added value from asset allocation we must calculate the return of an intermediate
fund called the “allocation or semi-notional fund”, which is one step away from the benchmark
portfolio, one step towards the actual portfolio.
--- page 130 ---

JWBK178-05
JWBK178-Bacon
March 28, 2008
13:7
Char Count= 0
Performance Attribution
119
In the semi-notional fund the asset allocation weights of the actual fund are applied to index
returns within each category. By deﬁnition the return on this notional fund reﬂects the portfolio
manager’s asset allocation “bets” but since index returns are used within the asset category it
includes no stock selection:
Allocation or semi-notional fund
bS
i
n
i
1
i
bi
(5.3)
The contribution from asset allocation is therefore the difference between the semi-notional
fund and the benchmark fund or:
bS
b
i
n
i
1
i
bi
i
n
i
1
Wi
bi
i
n
i
1
(
i
Wi)
bi
(5.4)
The contribution to asset allocation in the ith category is:
Ai
(
i
Wi)
bi
(5.5)
Note that:
i
n
i
1
Ai
bS
b
(5.6)
Security (or stock) selection
Similarly, to identify the added value from security selection we must calculate the return of
a different intermediate fund called the “selection notional fund”, which is also by deﬁnition
one step away from the benchmark return. In the selection notional fund the asset allocation
weights of the benchmark are kept static and applied to the category returns within the actual
portfolio. By deﬁnition the return on this notional fund reﬂects the portfolio manager’s stock
selection since real returns are applied to index weights, but excludes any contribution from
asset allocation:
Selection notional fund
rS
i
n
i
1
Wi
ri
(5.7)
The contribution from stock selection is therefore the difference between the selection notional
fund and the benchmark fund or:
rS
b
i
n
i
1
Wi
ri
i
n
i
1
Wi
bi
i
n
i
1
Wi
(ri
bi)
(5.8)
The contribution to stock selection in category i is:
Si
Wi
(ri
bi)
(5.9)
--- page 131 ---

JWBK178-05
JWBK178-Bacon
March 28, 2008
13:7
Char Count= 0
120
Practical Portfolio Performance Measurement and Attribution
Note that:
i
n
i
1
Si
rS
b
(5.10)
Interaction
In this the “classical” deﬁnition of attribution, stock selection and asset allocation do not
explain the arithmetic difference completely – a third term is required:
Stock selection
Asset allocation
rS
b
bS
b
(5.11)
or
rS
bS
2
b
To achieve r
b we must add a third term called interaction:
rS
b
Stock
selection
bS
b
Asset
allocation
r
rS
bS
b
Interaction
r
b
(5.12)
In their article Brinson, Hood and Beebower described this term as other; interaction is perhaps
a better description and is in common usage today:
r
rs
bs
b
i
n
i
1
i
ri
i
n
i
1
Wi
ri
i
n
i
1
i
bi
i
n
i
1
Wi
bi
(5.13)
This simpliﬁes to:
i
n
i
1
(
i
Wi)
(ri
bi)
(5.14)
It can be seen from Equation (5.14) that interaction is the combination of asset allocation and
stock selection effects.
The contribution to interaction in category i is:
Ii
(
i
Wi)
(ri
bi)
(5.15)
Note that:
i
n
i
1
Ii
r
rS
bS
b
(5.16)
Figure 5.1 illustrates the Brinson framework for return attribution.
Figure 5.2 graphically illustrates the attribution factors for each category i. The contribution
to total portfolio return from category i is the area ri
i, the contribution from the benchmark
is area bi
Wi.
The contribution to excess return in category i is the sum of the areas representing selection
Wi
(ri
bi), allocation (
i
Wi)
bi and interaction (
i
Wi)
(ri
bi).
Table 5.1 provides the data for a simple numerical example of a three-category portfolio
consisting of UK, Japanese and US equities.
--- page 132 ---

JWBK178-05
JWBK178-Bacon
March 28, 2008
13:7
Char Count= 0
Performance Attribution
121
Selection
Actual
Passive
Allocation
Passive
Actual
QuadrantIV
Portfolio return
i=n
i=1
wi × ri
wi × bi
Wi × bi
Wi × ri
r =
QuadrantII
Semi-notional
=
i=n
i=1
bS
QuadrantIII
Selection notional
=
i=n
i=1
i=n
i=1
rS
QuadrantI
Benchmark return
=
b
Excess returns due to:
Asset allocation
II  – I
Security selection
III – I
Interaction

IV – III – II + I
Total

IV – I
Figure 5.1
Brinson framework for return attribution
ri
bi
Wi
wi
Benchmark
contribution
Wi × bi
Allocation
(wi − Wi ) × bi
Selection
Wi × (ri − bi)
Interaction
(wi − Wi ) × (ri − bi )
Figure 5.2
Brinson, Hood and Beebower attribution model
Table 5.1
Three category portfolio
Portfolio
Benchmark
Portfolio
Benchmark
weight
weight
return
return
(%)
(%)
(%)
(%)
UK equities
40
40
20
10
Japanese equities
30
20
5
4
US equities
30
40
6
8
Total
100
100
8.3
6.4
--- page 133 ---

JWBK178-05
JWBK178-Bacon
March 28, 2008
13:7
Char Count= 0
122
Practical Portfolio Performance Measurement and Attribution
Total portfolio, benchmark and notional funds are calculated in Exhibit 5.1:
Exhibit 5.1
Return calculations
Using the data from Table 5.1 the portfolio return r
i
n
i
1
i
ri is:
r
40%
20%
30%
5%
30%
6%
8 3%
The benchmark return b
i
n
i
1
Wi
bi is:
b
40%
10%
20%
4%
40%
8%
6 4%
The allocation notional return bS
i
n
i
1
i
bi is:
bS
40%
10%
30%
4%
30%
8%
5 2%
The selection notional return rS
i
n
i
1
Wi
ri is:
rS
40%
20%
20%
5%
40%
6%
9 4%
The challenge of attribution analysis is to break down and quantify the decisions made by
the portfolio manager contributing to the arithmetic excess return of 1.9%.
Using Equation (5.5) we can derive the asset allocation effects shown in Exhibit 5.2 for the
data in Table 5.1:
Exhibit 5.2
Asset allocation
Total asset (or country) allocation:
bS
b
5 2%
6 4%
1 2%
Individual country asset allocation effects are:
UK equities
(40%
40%)
10%
0 0%
Japanese equities
(30%
20%)
4 0%
0 4%
US equities
(30%
40%)
8%
0 8%
Total
0 0%
0 4%
0 8%
1 2%
In Exhibit 5.2 the portfolio weight in UK equities is exactly in line with the benchmark
weight, therefore there is no contribution to asset allocation in this category.
There is, however, an overweight position of 10% in Japanese equities which when applied
to the negative market return in Japanese equities of
4.0% results in a negative contribution
of
0.4%.
If there is an overweight position in a portfolio it follows there must be a least one underweight position. In Table 5.1 there is a 10% underweight position in US equities resulting in a
negative contribution of
0.8% when applied to the positive market return in the US market
of 8.0%.
The total contribution to arithmetic excess return from asset allocation is
1.2%.
--- page 134 ---

JWBK178-05
JWBK178-Bacon
March 28, 2008
13:7
Char Count= 0
Performance Attribution
123
Using Equation (5.9) stock selection effects are calculated in Exhibit 5.3:
Exhibit 5.3
Stock selection
Total stock selection:
rS
b
9 4%
6 4%
3 0%
Individual country stock selection effects are:
UK equities
40%
(20%
10%)
4 0%
Japanese equities
20%
( 5 0%
4 0%)
0 2%
US equities
40%
(6 0%
8 0%)
0 8%
Total
4 0%
0 2%
0 8%
3 0%
UKequityperformanceisverystrong,outperformingthebenchmarkby10%;thebenchmark
suggests that 40% of the portfolio should be invested in this category resulting in a 4.0%
contribution to arithmetic excess return.
Japanese equities underperformed by 1%; the benchmark suggested a 20% weighting, therefore resulting in a negative contribution of
0.2% from Japanese stock selection.
US equity performance is also poor, underperforming by 2%; the benchmark suggests a 40%
weighting, therefore generating a negative contribution of
0.8% from US stock selection.
Total contribution to arithmetic excess return from stock selection is
3.0%. Combining asset allocation of
1.2% and stock selection of
3.0%, 1.8% of added value is explained. The remaining term is interaction calculated by Equation (5.15) as demonstrated in
Exhibit 5.4:
Exhibit 5.4
Interaction
Total interaction in Table 5.1 is:
r
rS
bS
b
8 3%
9 4%
5 2%
6 4%
0 1%
Individual interaction effects are:
UK equities
(40%
40%)
(20%
10%)
0 0%
Japanese equities
(30%
20%)
( 5 0%
4 0%)
0 1%
US equities
(30%
40%)
(6 0%
8 0%)
0 2%
Total
0 0%
0 1%
0 2%
0 1%
The overall contribution from interaction is small. For UK equities the portfolio weight is in
line with the benchmark weight and therefore there is no contribution to interaction.
For Japanese equities there is an asset allocation bet of 10%; we have 10% more of this
underperforming asset category than suggested by the benchmark, therefore causing a further
negative impact of
0.1%.
In US equities there is an underweight bet of 10% in this underperforming category. There
is less of this underperforming category than the benchmark suggests, therefore the combined
effect of an underweight position in an underperforming category is an added value of
0.2%.
Total contribution from interaction is
0.1%
The attribution results are summarised in Table 5.2.
