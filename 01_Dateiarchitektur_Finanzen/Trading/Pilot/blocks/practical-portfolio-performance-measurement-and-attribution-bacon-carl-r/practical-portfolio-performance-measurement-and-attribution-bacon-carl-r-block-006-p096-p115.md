# Practical Portfolio Performance Measurement and Attribution -- Bacon, Carl R_ -- 10_1002_9781119206309, 2012 jan 02 -- John Wiley & Sons, Inc_ -- doi 10_1002_9781119206309 -- bc9440f8ca87cf4e34d9c3fda66edb46 -- Anna.pdf — pages 96–115

--- page 96 ---

JWBK178-04
JWBK178-Bacon
July 28, 2008
11:13
Char Count= 0
84
Practical Portfolio Performance Measurement and Attribution
We can measure the degree of skewness (or more accurately Fisher’s skewness) in the
following formula:
Skewness S
ri
¯r
P
3
1
n
(4.40)
A normal distribution will have a skewness of 0. Note that in Equation (4.40) extreme values carry greater weight since they are cubed while maintaining their initial sign positive or
negative.
We can use skewness to make a judgement about the possibility of large negative or positive
outliers when comparing portfolio returns. Skewness provides more information about the
shape of return distribution, where deviations from the mean are greater in one direction than
the other; this measure will deviate from zero in the direction of the larger deviations. Positive
and negative skew are illustrated in Figure 4.11.
Sample skewness
Sample skewness is calculated as follows:
Sample skewness SS
ri
¯r
S p
3
n
(n
1)
(n
2)
(4.41)
where:
Sp
portfolio sample standard deviation.
Note that the standard Excel function called skewness is in fact sample skewness.
Negative skew
Positive skew
Figure 4.11
Positive and negative skew
Kurtosis (Pearson’s kurtosis)
Kurtosis(Pearson,1905)(ormorecorrectlyPearson’skurtosis)providesadditionalinformation
about the shape of a return distribution; formally, it measures the weight of returns in the tails
of the distribution relative to standard deviation but is more often associated as a measure of
ﬂatness or peakedness of the return distribution:
Kurtosis K
ri
¯r
p
4
1
n
(4.42)
--- page 97 ---

JWBK178-04
JWBK178-Bacon
July 28, 2008
11:13
Char Count= 0
Risk
85
The kurtosis of a normal distribution is 3 (called mesokurtic); greater than 3 would indicate
a peaked distribution with fat tails (called platykurtic) and less than 3 would indicate a less
peaked distribution with thin tails (called leptokurtic).
Subtracting 3 from Equation (4.42) we obtain a measure of excess kurtosis (or Fisher’s
kurtosis). The terms kurtosis and excess kurtosis are often confused:
Excess kurtosis K E
ri
¯r
p
4
1
n
3
(4.43)
High and low kurtosis are illustrated in Figures 4.12 and 4.13 respectively.
Sample kurtosis
Sample kurtosis is calculated as follows:
Sample kurtosis KS
ri
¯r
S p
4
n
(n
1)
(n
1)
(n
2)
(n
3)
(4.44)
Sample excess kurtosis is calculated as follows:
KSE
ri
¯r
S p
4
n
(n
1)
(n
1)
(n
2)
(n
3)
3
(n
1)2
(n
2)
(n
3)
(4.45)
The standard Excel function labelled kurtosis is in fact sample excess kurtosis.
A better understanding of the shape of the distribution of returns will aid in assessing the
relative qualities of portfolios. Whether we prefer higher or lower kurtosis (or for that matter
positive or negative skewness) will depend on the type of return series we want to see.
Equity markets tend to have fat tails. When markets fall portfolio managers tend to sell
and when they rise portfolio managers tend to buy; there is a higher probability of extreme
events than the normal distribution would suggest. Therefore tracking error and VaR statistics
calculated using normal assumptions may underestimate risk.
Investors will tend to seek positive skew and lower kurtosis or thinner tails.
The variance of a distribution is known as the 2nd moment about the mean, skewness the
3rd moment and kurtosis the 4th moment.
Figure 4.12
Kurtosis
3 peaked with fat tails
--- page 98 ---

JWBK178-04
JWBK178-Bacon
July 28, 2008
11:13
Char Count= 0
86
Practical Portfolio Performance Measurement and Attribution
Figure 4.13
Kurtosis
3 less peaked with thin tails
Bera–Jarque statistic
Since normal distributions should have skewness near 0 and kurtosis near 3 we can test for
normality using the Bera–Jarque test:
Bera–Jarque statistic BJ
n
6
S2
K 2
E
4
(4.46)
With a conﬁdence level of 5% we will reject a distribution as normal if the Bera–Jarque
statistic exceeds 5.99, and with a conﬁdence level of 1% if it exceeds 9.21. Perfectly normal
distributions will have a BJ
0.
Skewness, kurtosis and the Bera–Jarque statistic are calculated in Table 4.10.
RISK-ADJUSTED PERFORMANCE MEASURES
FOR HEDGE FUNDS
There are numerous deﬁnitions of hedge funds; my favourite is from Ineichen (2003):
A hedge fund constitutes an investment program whereby the managers or partners seek absolute
returns by exploiting investment opportunities while protecting principal from potential ﬁnancial
loss.
Predominately, hedge fund management styles are designed to be asymmetric in their return
patterns. If successful this leads to variability of returns on the upside but not on the downside. Investors are less concerned with variability on the upside but of course are extremely
concerned about variability on the downside. This leads to an extended family of risk-adjusted
measures reﬂecting the downside risk tolerances of investors seeking absolute not relative
returns. Investors should prefer high average returns, lower variance or standard deviation,
positive skewness and lower kurtosis.
In addition, hedge funds can be further differentiated by:
(1) More ﬂexible investment strategies and the ability to employ leverage.
(2) Substantial personal holding by the portfolio manager and performance fees.
(3) Light regulation.
(4) Liquidity – investors are typically subject to a lock-up period.
--- page 99 ---

JWBK178-04
JWBK178-Bacon
July 28, 2008
11:13
Char Count= 0
Table 4.10
Skewness and kurtosis
Portfolio
Deviation from
Deviation
Deviation
4th power
monthly
average
squared
cubed
deviation
return ri (%)
(ri
¯r)
(ri
¯r)2
(ri
¯r)3
(ri
¯r)4
0.3
0.6
0.36
0.22
0.13
2.6
1.7
2.89
4.91
8.35
1.1
0.2
0.04
0.01
0.00
1.0
1.9
3.61
6.86
13.03
1.5
0.6
0.36
0.22
0.13
2.5
1.6
2.56
4.10
6.55
1.6
0.7
0.49
0.34
0.24
6.7
5.8
33.64
195.11
1131.65
1.4
2.3
5.29
12.17
27.98
4.0
3.1
9.61
29.79
92.35
0.5
1.4
1.96
2.74
3.84
8.1
7.2
51.84
372.25
2687.39
4.0
3.1
9.61
29.79
92.35
3.7
4.6
21.16
97.34
444.75
6.1
7.0
49.00
343.00
2401.00
1.7
0.8
0.64
0.51
0.41
4.9
5.8
33.64
195.11
1131.65
2.2
3.1
9.61
29.79
92.35
7.0
6.1
37.21
226.98
1384.58
5.8
4.9
24.01
117.65
576.48
6.5
7.4
54.76
405.22
2998.66
2.4
1.5
2.25
3.38
5.06
0.5
1.4
1.96
2.74
3.84
0.9
1.8
3.24
5.83
10.50
Sum
359.74
114.99
13 116.28
Monthly standard deviation
359 74
24
3 87%
Skewness S
ri
¯r
P
3
1
n
114 99
3 873
24
0 08
Sample standard deviation
359 74
24
1
3 95%
Kurtosis
ri
¯r
p
4
1
n
13 116 28
3 874
24
2 43
Excess kurtosis
2 43
3
0 57
Bera–Jacque BJ
n
6
S2
K 2
E
4
24
6
0 082
0 572
4
0 35
Sample skewness SS
ri
¯r
S p
3
n
(n
1)
(n
2)
0.09
Sample excess kurtosis KSE
ri
¯r
S p
4
n
(n
1)
(n
1)
(n
2)
(n
3)
3
(n
1)2
(n
2)
(n
3)
0 41
87
--- page 100 ---

JWBK178-04
JWBK178-Bacon
July 28, 2008
11:13
Char Count= 0
88
Practical Portfolio Performance Measurement and Attribution
DRAWDOWN
Perhaps the simplest measure of risk in a return series from an absolute return investor’s
perspective, wishing to avoid losses, is any continuous losing return period or drawdown.
Average drawdown
As its name suggests, the average drawdown is the average continuous negative return over an
investment period, 3 years being a typical period of measurement:
Average drawdown ¯D
j
d
j
1
D j
d
(4.47)
where:
D j
jth drawdown over entire period
d
total number of drawdowns in entire period.
Some investors take the view that only the largest drawdowns in the return series are of any
consequence and therefore restrict d to a predetermined maximum limit of say 3 or 5 thus
enabling fair comparison between portfolios.
Maximum drawdown
The maximum drawdown (DMax), not to be confused with the largest individual drawdown, is
the maximum potential loss over a speciﬁc time period, typically 3 years. Maximum drawdown
represents the maximum loss an investor can suffer in the fund buying at the highest point and
selling at the lowest. Like any other statistic it is essential to compare performance over the
same time period.
Largest individual drawdown
As its name suggests the largest individual drawdown (DLar) is the largest individual uninterrupted loss in a return series.
Recovery time (or drawdown duration)
The recovery time or drawdown duration is the time taken to recover from an individual or
maximum drawdown to the original level.
Individual and maximum drawdowns and recovery time are illustrated in Figure 4.14. The
largest individual loss is D3.
Drawdown deviation
Drawdown deviation calculates a standard deviation-type statistic using individual drawdowns
as follows:
Drawdown deviation DD
j
d
j
1
D2
j
n
(4.48)
--- page 101 ---

JWBK178-04
JWBK178-Bacon
July 28, 2008
11:13
Char Count= 0
Risk
89
Ulcer index
The ulcer index developed by Peter G. Martin in 1987 (Martin and McCann, 1987) (so called
because of the worry suffered by both the portfolio manager and investor) is similar to drawdown deviation with the exception that the impact of the duration of drawdowns is incorporated
by selecting the negative return for each period below the previous peak or high water mark.
The impact of long, deep drawdowns will have a signiﬁcant impact since the underperformance
since the last peak is squared:
Ulcer index UI
i
n
i
1
D 2
i
n
(4.49)
where:
Di
drawdown since pervious peak in period i.
Thisapproachisclearlysensitivetothefrequencyoftimeperiodandclearlypenalisesmanagers
that take time to recover to previous highs, taking into account both the depth and duration of
drawdowns.
Pain index
If the drawdowns are not squared then the resulting pain index is very similar to the Zephyr
pain index in discrete form as proposed by Thomas Becker in 2006:
Pain index PI
i
n
i
1
Di
n
(4.50)
Calmar ratio
The Calmar ratio is a Sharpe-type measure that uses maximum drawdown rather than standard
deviation to reﬂect the investor’s risk. In the context of hedge fund performance it is easy to
understand why investor’s might prefer the maximum possible loss from peak to valley as an
appropriate measure of risk:
Calmar ratio CR
rP
rF
DMax
(4.51)
Sterling ratio
The Sterling ratio replaces maximum drawdown in the Calmar ratio with the average drawdown
over the period of analysis.
There are multiple variations of the Sterling ratio in common usage, perhaps reﬂecting its
use across a range of differing asset categories and outside the ﬁeld of ﬁnance.
The original deﬁnition attributed to Deanne Sterling Jones (McCafferty, 2003) appears to
be:
Original Sterling ratio OSR
rp
¯DLar
10%
(4.52)
--- page 102 ---

JWBK178-04
JWBK178-Bacon
July 28, 2008
11:13
Char Count= 0
90
Practical Portfolio Performance Measurement and Attribution
Maximum drawdown
Cumulative return
Time
D1
D2
D3
Recovery time
Figure 4.14
Drawdown statistics
The denominator is deﬁned as the average largest drawdown plus 10%. The addition of 10%
is arbitrary compensation for the fact that the average largest drawdown is inevitably smaller
than the maximum drawdown. Typically, only a ﬁxed number of the largest drawdowns are
averaged with apologies to Deanne Sterling Jones, I suggest the deﬁnition is standardised to
exclude the 10% but in Sharpe form as follows:
Sterling ratio SR
rp
rF
j
d
j
1
D j
d
(4.53)
The number of observations d ﬁxed to the investor’s preference.
Sterling–Calmar ratio
Perhaps the most common variation of the Sterling ratio uses the average annual maximum
drawdown in the denominator over 3 years. A combination of both Sterling and Calmar concepts, to avoid confusion and to encourage consistent use across the industry I suggest the
following standardised deﬁnition:
Sterling–Calmar ratio SCR
rp
rF
¯Dmax
(4.54)
Given the variety of Sterling ratio deﬁnitions great care should be taken to ensure the same
deﬁnition is used over the same time period using the same frequency of data when ranking
portfolio performance.
Burke ratio
Burke (1994) in his article “A sharper Sharpe ratio” suggested using the familiar concept of the
square root of the sum of the squares of each drawdown in order to penalise major drawdowns
--- page 103 ---

JWBK178-04
JWBK178-Bacon
July 28, 2008
11:13
Char Count= 0
Risk
91
as opposed to many mild ones:
Burke ratio BR
rP
rF
j
d
j
1
D2
j
(4.55)
Just like the Sterling ratio the number of drawdowns used can be restricted to a set number of
the largest drawdowns.
Modiﬁed Burke ratio
For consistency with other Shape-type statistics it might be more appropriate to deﬁne the
modiﬁed Burke ratio using drawdown deviation in the denominator as follows:
Modiﬁed Burke ratio MBR
rP
rF
j
d
j
1
D2
j
n
(4.56)
Clearly, both the modiﬁed and standard Burke ratios will generate identical portfolio rankings
if the number of drawdowns is not restricted to the largest drawdowns.
Martin ratio (or ulcer performance index)
If the duration of drawdowns is a concern for investors the Martin ratio is similar to the modiﬁed
Burke index but using the ulcer index in the denominator:
Martin ratio MR
rP
rF
i
n
i
1
D 2
i
n
(4.57)
Pain ratio
The equivalent to the Martin ratio but using the pain index is the pain ratio:
Pain ratio PR
rP
rF
i
m
i
1
Di
n
(4.58)
Lake ratio
Seykota (2003) suggests an alternative drawdown statistic combining drawdown magnitude
with drawdown duration. The lake ratio is constructed from the ratio of the volume in the
valleys (or lakes) of the performance track record with the total volume under the cumulative
return. Lower lake ratios are preferred. Both the pain and Martin ratios penalise managers with
early high water marks in their track record, therefore it is far better to peak later rather than
earlier when applying these ratios. To some degree the lake ratio compensates for high early
peaks in performance by taking into account the duration and timing of the peaks.
--- page 104 ---

JWBK178-04
JWBK178-Bacon
July 28, 2008
11:13
Char Count= 0
92
Practical Portfolio Performance Measurement and Attribution
Peak ratio
The volume of lakes in the lake ratio is equivalent to the pain index. The lake ratio is presented
in inverted form, with the pain index in the numerator. The inverse of the lake index, if I might
suggest a name, is the peak ratio, which is more consistent with our standard return/risk-type
ratios.
Examples of drawdown, maximum drawdown, pain index, ulcer index, Sterling, Calmar,
Burke, pain and Martin ratios are contained in Table 4.11.
DOWNSIDE RISK (OR SEMI-STANDARD DEVIATION)
Standard deviation and the symmetrical normal distribution are the foundations of modern
portfolio theory. Post-modern portfolio theory recognises that investors prefer upside risk
rather than downside risk and utilises semi-standard deviation.
Semi-standard deviation measures the variability of underperformance below a minimum
target rate. The minimum target rate could be the risk-free rate, the benchmark or any other
ﬁxed threshold required by the client. All positive returns are included as zero in the calculation
of semi-standard deviation or downside risk as follows:
Downside risk
D
n
i
1
min [(ri
rT ) 0]2
n
(4.59)
where:
rT
minimum target return.
Clearly, since positive returns are excluded there are potentially fewer or in some cases no
observations less than the target return. Therefore great care must be taken to ensure there are
sufﬁcient returns to ensure the calculation is meaningful.
Alternatively, a distribution curve can be ﬁtted to the data points and integral calculus used
to model the probability of returns below the minimum target return (Sortino and Satchell,
2001), a type of semi-ex ante analysis.
As should be expected downside variance is the square of downside risk and downside
potential is simply the average sum of returns below target:
Downside variance
2
D
n
i
1
min [(ri
rT ) 0]2
n
(4.60)
Downside potential DP
n
i
1
min [(ri
rT ) 0]
n
(4.61)
Downside variance is the second lower partial moment of return LPM2 (rT ), and downside
potential is the ﬁrst lower partial moment LPM1 (rT )
Upside risk
The equivalent upside statistics are as expected:
Upside risk
U
n
i
1
max [(ri
rT ) 0]2
n
(4.62)
--- page 105 ---

JWBK178-04
JWBK178-Bacon
July 28, 2008
11:13
Char Count= 0
Risk
93
Table 4.11
Drawdown statistics (assume risk-free rate rF
)
Portfolio
Continuous
Continuous
Drawdown
Drawdown
monthly
drawdown
drawdown
from
from peak
return (%)
D j
squared D2
j
peak Di
squared D 2
i
0.3
0.00
0.00
2.6
0.00
0.00
1.1
0.00
0.00
1.0
1.0
1.00
1.00
1.00
1.5
0.00
0.00
2.5
0.00
0.00
1.6
0.00
0.00
6.7
0.00
0.00
1.4
1.4
1.96
1.40
1.96
4.0
0.00
0.00
0.5
0.5
0.25
0.50
0.25
8.1
0.00
0.00
4.0
0.00
0.00
3.7
3.70
13.69
6.1
9.6
91.67
9.57
91.67
1.7
8.04
64.59
4.9
12.54
157.33
2.2
7.0
48.89
14.47
209.30
7.0
8.48
71.91
5.8
3.17
10.06
6.5
6.5
42.25
9.47
89.60
2.4
7.29
53.19
0.5
7.76
60.16
0.9
1.4
1.95
8.59
73.73
Annualised
portfolio
return 10.37%
Total
187.97
Total
95.98
Total
898.44
Maximum drawdown
15.47
Largest drawdown
9.57
Pain index
95 98
24
4 0
Average largest
drawdown (3)
9 57
6 99
6 50
3
7 69
Ulcer index
898 44
24
6 12
Sterling
ratio
10 37
0
9 57
1 08
Pain ratio
10 37
0
4 0
2 59
Calmar ratio
10 37
0
15 47
0 67
Martin ratio
10 37
0
6 12
1 69
Burke ratio
10 37
0
187 97
0 76
--- page 106 ---

JWBK178-04
JWBK178-Bacon
July 28, 2008
11:13
Char Count= 0
94
Practical Portfolio Performance Measurement and Attribution
Upside variance
2
U
n
i
1
max [(ri
rT ) 0]2
n
(4.63)
Upside potential UP
n
i
1
max [(ri
rT ) 0]
n
(4.64)
Notethatinalltheaboveequationsthetotalnumberofobservationsnisalwaysusedirrespective
of the number of observations above or below target.
Loss and gain standard deviation measures the variability of returns above or below target
only and are typically not used in performance analysis:
Loss standard deviation
d
n
i
1
min [(ri
rT )]2
nd
(4.65)
Gain standard deviation
u
n
i
1
max [(ri
rT )]2
nu
(4.66)
where:
nd
number of returns less than target
nu
number of returns greater than target.
Shortfall risk (or downside frequency)
Shortfall risk is the ratio (or probability) of returns below target compared to the total number
of returns:
Shortfall risk
nd
n
(4.67)
Omega ratio (
)
In their article “A universal performance measure” Shadwick and Keating (2002) suggest a
gain–loss ratio that captures the information in the higher moments of a return distribution as
follows:
Omega ratio
1
n
i
n
i
1
max(ri
rT 0)
1
n
i
n
i
1
max(rT
ri 0)
(4.68)
Note:
i
n
i
1
max(rT
ri 0)
1
i
n
i
1
min(ri
rT 0)
(4.69)
The omega ratio can be used as a ranking statistic; the higher the better. It equals 1 when rT is
the mean return.
The omega ratio implicitly adjusts for both skewness and kurtosis in the return distribution.
--- page 107 ---

JWBK178-04
JWBK178-Bacon
July 28, 2008
11:13
Char Count= 0
Risk
95
Bernardo and Ledoit (or gain–loss) ratio
The Bernardo and Ledoit (1996) ratio is a special case of the omega ratio with rT
0:
Bernado
Ledoit ratio
1
n
i
n
i
1
max(ri 0)
1
n
i
n
i
1
max(0
ri 0)
(4.70)
d ratio
The d ratio (Lavinio, 1999) is similar to the Bernado Ledoit ratio but inverted and taking into
account the frequency of positive and negative returns:
d ratio
nd
i
n
i
1
max (0
ri 0)
nu
i
n
i
1
max (ri 0)
(4.71)
where:
nd
number of returns less than zero
nu
number of returns greater than zero.
The d ratio will have values between zero and inﬁnity and can be used to rank the performance
of portfolios. The lower the d ratio the better the performance, a value of zero indicating there
are no returns less than zero and a value of inﬁnity indicating there are no returns greater than
zero. Portfolio managers with positively skewed returns will have lower d ratios.
Omega–Sharpe ratio
The omega ratio can be converted to a ranking statistic in familiar form to the Sharpe ratio.
Clearly, the average portfolio return less the target return is equal to the sum of the upside and
downside potential:
Omega–Sharpe ratio
rP
rT
1
n
i
n
i
1
max(rT
ri 0)
(4.72)
Noting again Equation (4.69):
rP
rT
1
n
i
n
i
1
ri
rT
1
n
i
n
i
1
max(ri
rT 0)
1
n
i
n
i
1
max(rT
ri 0)
(4.73)
Substituting Equation (4.73) into Equation (4.72):
1
n
i
n
i
1
max (ri
rT 0)
1
n
i
n
i
1
max (rT
ri 0)
1
n
i
n
i
1
max (rT
ri 0)
(4.74)
--- page 108 ---

JWBK178-04
JWBK178-Bacon
July 28, 2008
11:13
Char Count= 0
96
Practical Portfolio Performance Measurement and Attribution
1
n
i
n
i
1
max (ri
rT 0)
1
n
i
n
i
1
max (rT
ri 0)
1
n
i
n
i
1
max (rT
ri 0)
1
n
i
n
i
1
max (rT
ri 0)
1
(4.75)
Omega–Sharpe ratio
1
(4.76)
Hence, the omega–Sharpe ratio will rank portfolios in the same order as the omega ratio.
Sortino ratio
A natural extension of the Sharpe and Sharpe–omega ratios is suggested by Sortino and van
der Meer (1991) (Figure 4.15) which uses downside risk in the denominator as follows:
Sortino ratio
(rP
rT )
D
(4.77)
Clearly, investors should be seeking returns greater than the risk-free rate (why take any risk
otherwise), therefore the minimum accepted return in most cases should be greater than the
risk-free rate.
Kappa ( l)
Kaplan and Knowles (2004) in their paper “Kappa: a generalized downside risk-adjusted
performance measure”, demonstrate that both the Sortino ratio and the Sharpe–omega ratio
are special cases of kappa:
Kl
rp
rT
1
n
i
n
i
1
max (rT
ri 0)l
(4.78)
For l
1 K1 is the Sharpe–omega ratio and for l
2 K2 is the Sortino ratio. It is difﬁcult
to interpret the meanings of K3 and K4 but they would equate to the 3rd and 4th moments of
skewness and kurtosis, respectively.
Return
rT
Downside risk σD
A
Figure 4.15
Sortino ratio
--- page 109 ---

JWBK178-04
JWBK178-Bacon
July 28, 2008
11:13
Char Count= 0
Risk
97
Note that in continuous form the lth lower partial moment function is deﬁned as:
LPMl(rT )
rT
(rT
r)ldF(r)
(4.79)
The lth lower partial moment can be estimated from a sample of discrete returns as follows:
LPMl(rT )
1
n
i
n
i
1
max(rT
ri 0)l
(4.80)
Some would argue that analysis using just discrete values tells only part of the story and
that the continuous form is preferred. However, the discrete form is both easier to understand
and calculate, doesn’t require a probability function to be estimated and focuses on the return
periods (nomally monthly) of most concern to the investor. Admittedly, reaching a ﬁxed amount
each month is a different proposition than reaching the annualised equivalent each year but
then again many investors are concerned about monthly performance below target.
Upside potential ratio
The upside potential ratio suggested by Sortino et al. (1999) can also be used to rank portfolio
performance and combines upside potential with downside risk as follows:
Upside potential ratio UPR
i
n
i
1
max (ri
rT 0)
D
(4.81)
Portfolio downside risk, Sortino ratio, upside and downside potential, omega, omega–Sharpe
ratio and upside potential ratio are calculated in Table 4.13.
Investors retain an interest in the actual return delivered. I take the view that the actual return
in the numerator is relevant to most investors and hence my preference for the Sortino ratio.
Volatility skewness
A similar measure to omega but using the second partial moment is volatility skewness (Rom
and Ferguson, 2001), the ratio of the upside variance compared to the downside variance.
Values greater than 1 would indicate positive skewness and values less than 1 would indicate
negative skewness:
Volatility skewness
2
U
2
D
(4.82)
This measure, in particular, rewards extreme positive events and penalises extreme negative
events. For those like me that are unsure about the merits of overrewarding extreme, potentially
one-off positive events then perhaps the upside potential ratio is more appropriate.
--- page 110 ---

JWBK178-04
JWBK178-Bacon
July 28, 2008
11:13
Char Count= 0
98
Practical Portfolio Performance Measurement and Attribution
Table 4.12
Portfolio downside risk (monthly minimum target return
0.5%, annual minimum target
return
6.17%)
Portfolio
Deviation against
Squared
Upside
monthly
target (downside
deviation
only
return ri (%)
only) (ri
rT ) (%)
(ri
rT )2
(ri
rT ) (%)
0.3
0.2
0.04
2.6
2.1
1.1
0.6
1.0
1.5
2.25
1.5
1.0
2.5
2.0
1.6
1.1
6.7
6.2
1.4
1.9
3.61
4.0
3.5
0.5
1.0
1.00
8.1
7.6
4.0
3.5
3.7
4.2
17.64
6.1
6.6
43.56
1.7
1.2
4.9
5.4
29.16
2.2
2.7
7.29
7.0
6.5
5.8
5.3
6.5
7.0
49.00
2.4
1.9
0.5
1.0
1.00
0.9
1.4
1.96
Annualised
portfolio
return 10.37%
Total
32.9%
Total
156.51
Total
42.5%
Monthly downside risk
156 51
24
2 55%
Annualised downside risk
2 55 %
12
8 85%
Sortino ratio
10 37%
6 17%
8 85%
0 48
Downside
potential
32 9%
24
1 37%
Upside potential
42 5%
24
1 77%
Upside potential ratio
1 77%
8 85%
0 20
Omega
1 77%
1 37%
1 29
Omega–Sharpe ratio
1 29
1
0 2
Variability skewness
Although the rankings will be identical for consistency with other measures I prefer the square
root of volatility skewness. To differentiate the term I use the name variability skewness:
Variability skewness
Upside risk
Downside risk
U
D
(4.83)
--- page 111 ---

JWBK178-04
JWBK178-Bacon
July 28, 2008
11:13
Char Count= 0
Risk
99
Table 4.13
Benchmark downside risk (monthly minimum target return
0.5%, annual minimum
target return
6.17%)
Benchmark
Deviation against
Squared
monthly
target (downside
deviation
return bi (%)
only) (bi
rT ) (%)
(bi
rT )2
0.2
0.3
0.09
2.5
1.8
1.1
1.6
2.56
1.4
1.8
1.4
6.5
1.5
2.0
4.00
4.2
0.6
1.1
1.21
8.3
3.9
3.8
4.3
18.49
6.2
6.7
44.89
1.5
4.8
5.3
28.09
2.1
6.0
5.6
6.7
7.2
51.84
1.9
0.3
0.8
0.64
0.0
0.5
0.25
Total
152.06
Monthly downside risk
152 06
24
2 52%
Annualised downside risk
2 52%
12
8 72%
M2
S
rP
Sortino Ratio
(
DM
D)
10 42%
0 48
(8 72%
8 84%)
10 36%
Adjusted Sharpe ratio
P´ezier and White (2006) suggests using the adjusted Sharpe ratio (ASR) which explicitly
adjusts for skewness and kurtosis by incorporating a penalty factor for negative skewness and
excess kurtosis as follows:
Adjusted Sharpe ratio ASR
SR
1
S
6
SR
K
3
24
SR2
(4.84)
Skewness–kurtosis ratio
Watanabe (2006) also explicitly adjusts for skewness and kurtosis by suggesting using the
skewness–kurtosis ratio in conjunction with the Sharpe ratio, ranking portfolios using the
addition of the two rather than the Sharpe ratio in isolation. Again, higher rather than lower
--- page 112 ---

JWBK178-04
JWBK178-Bacon
July 28, 2008
11:13
Char Count= 0
100
Practical Portfolio Performance Measurement and Attribution
ratios are preferred:
Skewness
kurtosis ratio
S
K
(4.85)
Prospect ratio
Watanabe notes that people have a tendency to feel loss greater than gain – a well-known phenomena described by prospect theory (Kahneman and Tversky, 1979). He suggests penalising
loss as follows in the prospect ratio:
Prospect ratio
1
n
i
n
i
1
(Max (ri 0)
2 25
Min (ri 0))
rT
D
(4.86)
VALUE AT RISK (VaR)
VaRmeasurestheworstexpectedlossoveragiventimeintervalundernormalmarketconditions
at a given conﬁdence level. For example, an annual value of risk of £5m at a 95% conﬁdence
level for a portfolio would suggest that only once in 20 years would the annual loss exceed
£ 5m. Therefore it is far from the maximum possible loss. Value at Risk measures the downside;
upside potential measures the equivalent best-expected gain.
VaR, like tracking error, can be calculated ex post or ex ante. Typically, VaR is calculated
ex ante although like tracking error it is useful to calculate ex post as well to monitor risk
efﬁciency.
VaR can be calculated in conjunction with tracking error, since tracking error is a 1 standard deviation measure covering approximately 68% of returns; within 1 standard deviation of the average it is entirely possible that a change in strategy may reduce tracking
error while increasing VaR in the tails of the distribution. Client preferences will determine which of these measures is the most relevant. There are three different methods for
calculating VaR.
Variance–covariance (or parametric)
The variance–covariance method assumes that portfolio returns are normally distributed. Only
the mean return and standard deviation are required. With 95% conﬁdence we know the VaR
is:
VaR
¯r
1 65
(4.87)
With 99% conﬁdence we know the VaR is:
VaR
¯r
2 33
(4.88)
Historical simulation (or non-parametric)
Historical simulation simply reorganises actual historical returns, putting them in order from
worst to best. The Value at Risk is determined at the 95th percentile.
--- page 113 ---

JWBK178-04
JWBK178-Bacon
July 28, 2008
11:13
Char Count= 0
Risk
101
Monte Carlo simulation
Monte Carlo simulation is similar to historical simulation, but rather than use observed changes
in market factors a model is chosen for future portfolio returns and a random number generator
is used to calculate thousands of hypothetical portfolio returns. The Value at Risk is then
determined from this distribution.
The variance–covariance method is possibly the easiest to implement but it relies on a normal
assumption of returns. We know portfolio returns, and hedge fund returns in particular, are not
normally distributed.
Historical simulation is perhaps the most accurate; it’s suitable for all asset types and certainly conceptually easier to explain to pension fund trustees but requires the processing of
tremendous amounts of historical data.
Monte Carlo simulation is more complex and suffers from a greater model risk.
VaR ratio
VaR ratio is the ratio of Value of Risk divided by the total size of the portfolio, essentially the
percentage of the portfolio at risk:
VaR
Assets
(4.89)
Reward to VaR ratio
Reward to VaR is a Sharpe-type measure but with VaR ratio replacing standard deviation as
the measure of risk in the denominator:
RVaR
rP
rF
VaR ratio
(4.90)
Conditional VaR (or expected shortfall)
VaR does not provide any information about the shape of the tail or the expected size of
loss beyond the conﬁdence level. In this sense it is a very unsatisfactory risk measure; of
more interest is conditional VaR (Figure 4.16), otherwise known as expected shortfall, mean
expected loss tail VaR and tail loss which takes into account the shape of the tail. Historical
simulation methods, which make no assumptions of normality, are particularly suitable for
calculating conditional VaR.
Conditional Sharpe ratio
Conditional Sharpe ratio replaces VaR with conditional VaR in the denominator of the reward to
VaR ratio. Clearly, if expected shortfall is the major concern of the investor then the conditional
Sharpe ratio is demonstrably favourable to the reward to VaR ratio:
Conditional Sharpe ratio
rP
rF
CVaR
(4.91)
--- page 114 ---

JWBK178-04
JWBK178-Bacon
July 28, 2008
11:13
Char Count= 0
102
Practical Portfolio Performance Measurement and Attribution
Conditional
VaR
Figure 4.16
Conditional VaR
Modiﬁed VaR
Alternatively, VaR can be modiﬁed (Favre and Galeano, 2002) to adjust for kurtosis and
skewness using a Cornish–Fisher expansion as follows:
MVaR
¯rp
zc
z2
c
1
6
S
z3
c
3zc
24
K E
2z3
c
5zc
36
S2
(4.92)
where:
zc
1.96 with 95% conﬁdence
zc
2.33 with 99% conﬁdence.
Note that if the return distribution is normal, S and KE are zero and Equation (4.92) reduces
to the equivalent of Equation (4.87):
VaR
¯r
zc
(4.93)
This method works less well for distributions with more extreme skewness and excess kurtosis.
Modiﬁed Sharpe ratio
Similar to the adjusted Sharpe ratio, the modiﬁed Sharpe ratio uses modiﬁed VaR adjusted for
skewness and kurtosis:
Modiﬁed Sharpe ratio
rP
rF
MVaR
(4.94)
RETURN ADJUSTED FOR DOWNSIDE RISK
Like all ranking statistics it is easy to rank portfolios in order of preference using the Sortino
ratio but it is rather more difﬁcult to answer the question exactly how much better one portfolio
is than the other.
M2 for Sortino
M2 can be calculated for downside risk in the same way as it is calculated for total risk.
In Figure 4.17 a straight line is drawn vertically through the downside risk of the benchmark; the intercept with the Sortino ratio line of portfolio A would give the return of the
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
