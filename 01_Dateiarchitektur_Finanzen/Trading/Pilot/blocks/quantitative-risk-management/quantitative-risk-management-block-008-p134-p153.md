# Quantitative Risk Management_ Concepts, Techniques, and -- Alexander J_ McNeil, Rüdiger Frey, Paul Embrechts -- Princeton series in finance, -- isbn13 9780691122557 -- 478a0059673fecd0c76229cd3d8884e7 -- Anna’s Arc.pdf — pages 134–153

--- page 134 ---

118
4. Financial Time Series
−0.10
−0.05
0
0.05
02.01.85
02.01.86
02.01.87
02.01.88
02.01.89
02.01.90
02.01.91
02.01.92
02.01.93
02.01.94
−0.10
−0.05
0
0.05
Time
0
500
1000
1500
2000
2500
−0.10
−0.05
0
0.05
(a)
(b)
(c)
Figure 4.1.
(a) Log-returns for the DAX index from 2 January 1985 to 30 December 1994
compared with simulated iid data from (b) a normal and (c) a t distribution, where the
parameters have been determined by ﬁtting the models to the DAX data.
The simulated normal data are clearly very different from the DAX return data
and do not show the same range of extreme values, which does not surprise us given
our observations on the inadequacy of the Gaussian model in Chapter 3. While the
Student t model can generate comparable extreme values to the real data, more
careful observation reveals that the DAX returns exhibit a phenomenon known as
volatility clustering, which is not present in the simulated series.Volatility clustering
is the tendency for extreme returns to be followed by other extreme returns, although
not necessarily with the same sign. In the DAX data we see periods such as the stockmarket crash of October 1987 or the political uncertainty in the period between late
1989 and German reuniﬁcation in 1990 which are marked by large positive and
negative moves.
In Figure 4.2 the correlograms of the raw data and the absolute data for all three
datasets are shown. The correlogram is a graphical display for estimates of serial
--- page 135 ---

4.1. Empirical Analyses of Financial Time Series
119
ACF
0
0.2
0.4
0.6
0.8
1.0
DAX
ACF
0
0.2
0.4
0.6
0.8
1.0
Normal
Lag
ACF
0
10
20
30
0
0.2
0.4
0.6
0.8
1.0
t
Normal
Lag
0
10
20
30
t
DAX
(a)
(b)
Figure 4.2.
Correlograms for (a) the three datasets in Figure 4.1 and (b) the absolute values
ofthesedata.Dashedlinesmarkthestandard95%conﬁdenceintervalsfortheautocorrelations
of a process of iid ﬁnite-variance rvs.
correlation, and its construction and interpretation are discussed in Section 4.2.3.
While there is very little evidence of serial correlation in the raw data for all datasets,
theabsolutevaluesoftherealﬁnancialdataappeartoshowevidenceofserialdependence. Clearly, more than 5% of the estimated correlations lie outside the dashed lines,
which are the 95% conﬁdence intervals for a process of iid ﬁnite-variance rvs. This
serial dependence in the absolute returns would be equally apparent in squared return
values, and seems to conﬁrm the presence of volatility clustering. We conclude that,
although there is no evidence against the iid hypothesis for the genuinely iid data,
there is strong evidence against the iid hypothesis for the DAX return data.
Table 4.1 contains more evidence against the iid hypothesis for daily stock-return
data. The Ljung–Box test of randomness (described in Section 4.2.3) has been
performed for the stocks comprising the Dow Jones 30 index in the period 1993–
2000. In the two columns for daily returns the test is applied, respectively, to the raw
return data (LBraw) and their absolute values (LBabs), and p-values are tabulated;
--- page 136 ---

120
4. Financial Time Series
Table 4.1.
Tests of randomness for returns of 30 Dow Jones stocks in the eight-year period
1993–2000. The columns LBraw and LBabs show p-values for Ljung–Box tests applied to
the raw and absolute values, respectively.
Daily
Monthly






Name
Symbol
LBraw
LBabs
LBraw
LBabs
Alcoa
AA
0.00
0.00
0.23
0.02
American Express
AXP
0.02
0.00
0.55
0.07
AT&T
T
0.11
0.00
0.70
0.02
Boeing
BA
0.03
0.00
0.90
0.17
Caterpillar
CAT
0.28
0.00
0.73
0.07
Citigroup
C
0.09
0.00
0.91
0.48
Coco-Cola
KO
0.00
0.00
0.50
0.03
DuPont
DD
0.03
0.00
0.75
0.00
Eastman Kodak
EK
0.15
0.00
0.61
0.54
Exxon Mobil
XOM
0.00
0.00
0.32
0.22
General Electric
GE
0.00
0.00
0.25
0.09
General Motors
GM
0.65
0.00
0.81
0.27
Hewlett-Packard
HWP
0.09
0.00
0.21
0.02
Home Depot
HD
0.00
0.00
0.00
0.41
Honeywell
HON
0.44
0.00
0.07
0.30
Intel
INTC
0.23
0.00
0.79
0.62
IBM
IBM
0.18
0.00
0.67
0.28
International Paper
IP
0.15
0.00
0.01
0.09
JPMorgan
JPM
0.52
0.00
0.43
0.12
Johnson & Johnson
JNJ
0.00
0.00
0.11
0.91
McDonald’s
MCD
0.28
0.00
0.72
0.68
Merck
MRK
0.05
0.00
0.53
0.65
Microsoft
MSFT
0.28
0.00
0.19
0.13
3M
MMM
0.00
0.00
0.57
0.33
Philip Morris
MO
0.01
0.00
0.68
0.82
Proctor & Gamble
PG
0.02
0.00
0.99
0.74
SBC
SBC
0.05
0.00
0.13
0.00
United Technologies
UTX
0.00
0.00
0.12
0.01
Wal-Mart
WMT
0.00
0.00
0.41
0.64
Disney
DIS
0.44
0.00
0.01
0.51
these show strong evidence (particularly when applied to absolute values) against the
iid hypothesis. If ﬁnancial log-returns are not iid, then this contradicts the popular
random-walk hypothesis for the discrete-time development of log-prices (or, in this
case, index values). If log-returns are neither iid nor normal, then this contradicts
the geometric Brownian motion hypothesis for the continuous-time development of
prices on which the Black–Scholes–Merton pricing theory is based.
Moreover, if there is serial dependence in ﬁnancial return data, then the question
arises: to what extent can this dependence be used to make predictions about the
future? This is the subject of the third and fourth stylized facts. It is very difﬁcult to
predict the return in the next time period based on historical data alone. This can be
--- page 137 ---

4.1. Empirical Analyses of Financial Time Series
121
explained to some extent by the lack of serial correlation in the raw return series data.
For some series we do see evidence of correlations at the ﬁrst lag (or ﬁrst few lags);
for example, a small positive correlation at the ﬁrst lag might suggest that there is
some discernible tendency for a return with a particular sign (positive or negative)
to be followed in the next period by a return with the same sign. However, this is
not apparent in the DAX data, which suggests that our best guess for tomorrow’s
return based on our observations up to today is zero. This idea is expressed in the
assertion of the third stylized fact, that conditional expected returns are close to
zero.
Volatility is often formally modelled as the conditional standard deviation of
ﬁnancial returns given historical information and, although the conditional expected
returns are consistently close to zero, the presence of volatility clustering suggests
that conditional standard deviations are continually changing in a partly predictable
manner. If we know that returns have been large in the last few days, due to market excitement, then there is reason to believe that the distribution from which
tomorrow’s return is “drawn” should have a large variance. It is this idea that
lies behind the time series models for changing volatility that we will examine
in Section 4.3.
Tails and extremal behaviour.
We have already observed in Chapter 3 that the
normal distribution is a poor model for daily and longer-interval returns (whether
univariate or multivariate). The Jarque–Bera test, which is based on empirical skewness and kurtosis measures given in (3.15), clearly rejects the normal hypothesis
(see Example 3.3). In particular, daily ﬁnancial return data appear to have a much
higher kurtosis than is consistent with the normal distribution; their distribution is
said to be leptokurtic, meaning that it is more narrow in the centre but has longer
and heavier tails than the normal distribution.
Further empirical analysis often suggests that the distribution of daily or other
short-interval ﬁnancial return data has tails that decay slowly according to a power
law, rather than the faster, exponential-type decay of the tails of a normal distribution.
This means that we tend to see rather more extreme values than might be expected in
such return data; we discuss this phenomenon further in Chapter 7, which is devoted
to extreme value theory (EVT).
A further observation about extremes is, however, pertinent to our discussion
of serial dependence in ﬁnancial return data. In the discussion of Figure 4.1 we
remarked that there is a tendency for the extreme values in return series to occur in
close succession in volatility clusters; further evidence for this phenomenon is given
in Figure 4.3, where the time series of the 100 largest daily losses for the DAX returns
and the 100 largest values for the simulated t data are plotted. In Section 7.4.1 of
Chapter 7 we summarize theory which suggests that the very largest values in iid data
willoccurlikeeventsinaPoissonprocess,separatedbywaitingtimesthatareiidwith
an exponential distribution. Parts (b) and (d) of Figure 4.3 show QQplots of these
waiting times against an exponential reference distribution. While the hypothesis of
the Poisson occurrence of extreme values for the iid data is supported, there are too
--- page 138 ---

122
4. Financial Time Series
0.02
0.04
0.06
0.08
0.10
0.12
0.14
09.07.85
09.07.88
09.07.91
09.07.94
•••••••••••••••••••••••••••••••••••••••••••• •••• ••• •
•
•
•
0.02 0.04 0.06 0.08 0.10 0.12 0.14
Exponential quantiles
Time
0
500 1000150020002500
0.02
0.03
0.04
0.05
0.06
0.07
0.08
•••••••••••••••••••••••••••••••••••••••••••••••••• •••• ••
•
•
•
0.02 0.03 0.04 0.05 0.06 0.07 0.08
0
2
4
Ordered data
Exponential quantiles
(a)
(c)
1
3
5
0
2
4
1
3
5
(b)
(d)
Ordered data
Figure 4.3.
Time series plots of the 100 largest negative values for (a) the DAX returns
and (c) the simulated t data as well as (b), (d) QQplots of the waiting times between these
extreme values against an exponential reference distribution.
many short waiting times caused by the clustering of extreme values in the DAX
data to support the exponential hypothesis; this constitutes further evidence against
the iid hypothesis for return data.
Longer-interval return series.
As we progressively increase the interval of the
returns by moving from daily to weekly, monthly, quarterly and yearly data, the
phenomena we have identiﬁed tend to become less pronounced.Volatility clustering
decreases and returns begin to look both more iid and less heavy-tailed.
Suppose we begin with a sample of n returns measured at some time interval
(say daily or weekly) and aggregate these to form longer-interval log-returns. The
h-period log-return at time t is given by
X(h)
t
= ln
 St
St−h

= ln
 St
St−1
· · · St−h+1
St−h

=
h−1

j=0
Xt−j,
(4.1)
--- page 139 ---

4.1. Empirical Analyses of Financial Time Series
123
and from our original sample we can form a sample of non-overlapping h-period
returns {X(h)
t
: t = h, 2h, . . . , [n/h]h}, where [·] denotes the integer part. Due
to the sum structure of the h-period returns, it is to be expected that some central
limit effect takes place, whereby their distribution becomes less leptokurtic and
more normal as h is increased. Note that, although we have cast doubt on the iid
model for daily data, a central limit theorem applies to many stationary time series
processes, including the GARCH models that are a focus of this chapter.
In Table 4.1 the Ljung–Box tests of randomness have also been applied to nonoverlapping monthly return data. For 20 out of 30 stocks the null hypothesis of iid
data is not rejected at the 5% level in Ljung–Box tests applied to both the raw and
absolute returns. Thus it is harder to ﬁnd evidence of serial dependence in such
monthly returns.
Aggregating data to form non-overlapping h-period returns reduces the sample
size from n to n/h, and for longer-period returns (such as quarterly or yearly returns)
this may be a very serious reduction in the amount of data. An alternative in this
case is to form overlapping returns. For 1 ⩽k ⩽h, a general recipe for forming
aggregated h-period returns (overlapping or non-overlapping) is to form

X(h)
t
=
h−1

j=0
Xt−j : t = h, h + k, h + 2k, . . . , h + [(n −h)/k]k

;
(4.2)
this would give (1 + [(n −h)/k]) values that overlap by an amount (h −k). In
forming overlapping returns we can preserve a large number of data, but we do
build additional serial dependence into the data. Even if the original data were iid,
overlapping data would be dependent.
4.1.2
Multivariate Stylized Facts
Inriskmanagementweareseldominterestedinsingleﬁnancialtimeseries,butrather
with multiple series of ﬁnancial risk-factor changes. The stylized facts identiﬁed in
Section 4.1.1 may be augmented by a number of stylized facts of a multivariate
nature.
We now consider multivariate return data X1, . . . , Xn. Each component series
X1,j, . . . , Xn,j for j = 1, . . . , d is a series formed by logarithmic differencing of a
daily price, index or exchange-rate series as before. We consider the following set
of multivariate stylized facts.
(M1) Multivariate return series show little evidence of cross-correlation, except for
contemporaneous returns.
(M2) Multivariate series of absolute returns show profound evidence of crosscorrelation.
(M3) Correlations between series (i.e. between contemporaneous returns) vary over
time.
(M4) Extreme returns in one series often coincide with extreme returns in several
other series.
--- page 140 ---

124
4. Financial Time Series
The ﬁrst two observations are fairly obvious extensions of univariate stylized facts
(1) and (2) from Section 4.1.1. Just as the stock returns for, say, General Motors
on days t and t + h (for h > 0) show very little serial correlation, so we generally
detect very little correlation between the General Motors return on day t and, say,
the Coca-Cola return on day t + h. Of course, stock returns on the same day may
show non-negligible correlation, due to factors that affect the whole market on that
day. When we look at absolute returns we should bear in mind that periods of high
or low volatility are generally common to more than one stock. Thus returns of
large magnitude in one stock may tend to be followed on subsequent days by further
returns of large magnitude for both that stock and other stocks, which would explain
(M2). The issue of cross-correlation and its estimation will be addressed with an
example in Section 4.5.
Stylized fact (M3) is a multivariate counterpart to univariate observation (4):
that volatility appears to vary with time. While the latter appears “obvious” to the
naked eye from illustrations such as Figure 4.1, the multivariate observation is less
straightforward to demonstrate. In fact, although it is widely believed that correlations change, there are various ways of interpreting this stylized fact in terms of
underlying models.We may believe that correlations are constant within regimes but
that there is evidence of relatively frequent regime changes. Or we may believe that
correlation changes continually and dynamically like volatility. Just as volatility is
often formally modelled as the conditional standard deviation of returns given historical information, we can also devise models that feature a conditional correlation
that is allowed to change dynamically. We consider some models of this kind in
Section 4.6.
The only way to collect evidence for (M3) and to decide in what way correlation
changes is to ﬁt different models for changing correlation and then to make formal
statistical comparisons of the models. More ad hoc attempts to demonstrate (M3)
should generally be avoided. For example, it is not sufﬁcient to calculate correlations
between two daily series for monthly samples and to observe that these values may
vary greatly from month to month; there is considerable error in estimating correlations from small samples, particularly when the underlying distribution is something
more like a heavy-tailed multivariate t distribution than a Gaussian distribution (see
also Example 3.31 in this context).
Stylized fact (M4) is encountered in other forms; one often hears the view that
“correlations go to one in times of market stress”. The idea this observation attempts
to express is that in volatile periods the level of dependence between, for example,
various stock returns appears to be higher. Consider, for example, Figure 4.4, which
shows the BMW and Siemens log-return series the same 1985–1994 time period as
in Figure 4.1. In both the time series plots and the scatterplot three days on which
large negative returns occurred for both stocks have been marked with a number; all
of these days occurred during periods of volatility on the German market. They are,
respectively, 19 October 1987, Black Monday onWall Street; 16 October 1989, when
over 100 000 Germans protested against the East German regime in Leipzig during
thechainofeventsthatledtothefalloftheBerlinWallandGermanreuniﬁcation;and
--- page 141 ---

4.2. Fundamentals of Time Series Analysis
125
•
••
•
•
•
•
••
•
•• •
••
•
•
•••
•
•
••
•
•
•
•
••
• •
• •
•
•
•
•••••
•
••
•
•••
•
•
•
••
•
•
•
•
•
•
• ••
• •
• ••• •
••••
••
•
••• •
••• •
•
•
•
• •
•
• ••
••• •
•
•
•
•
•
•• •
••
••• ••
•
•
•• •
••
• •
••
•
••
•
••••
••
•
•
•
•
•• ••
•••
•
••
••
•
•
•
•
•
•
•
••••
•
•
• • •
•
•
•
•
••
••
•
•
•
•
•
• •
•
•
•
•
•
•
••
•
•
•
•
•••••
•
•
•
•••
• ••
••
•
•
•
•
•
•
•
••
•
•
•
••
•
•
•
•
• •
••••
•
•
•
•
•
• •
•
• •
•
• • •
•
••
•
• •
•
•
••
•
•
•
•
•
• ••
•
•
•
•
•
•
•
•
•
•
•
•
•
•• ••
•
•
• ••
•
•
•
•
•
•
•
•
•
•
•
•
•
••
•
•
• •
•
•
•
•
•
•
•
•
•• •
•
••• •••
•
•
•
••••
•
•
•
•
•
••
•
•
••
•
•
•
•
•
•
•
•
•
• •
•
• •
•
•
•
• •• •
•
•
•
••
•
••
••
•
• •
•
•
•
•
•
•
•
•
•
•
•
•
•
• •
• •
•
•
•
•
•
••
• •
•
•
•
•
••
•
•
• •
•
•
•
•
•
•
••
•
•
••
•
•
•
•••
•
•
•
•
••
•
•
••
•
•
•
•
•
••••
•
•
•
••••
• ••
•
•
•• ••
•• •
•
••
••
• •
•
•••
••
•
••••• •
•
•
• •
••
•
•
••••••
••
•
•
•
•
•
•
••••
•
••
••
•
•
•
•••
•
•
•
••
•
•
•
••
•
•
•
•
•
•
•• •••
•
•
•
•
• •••• ••
•
•
•••
•
••• •
•
•
•
•
•
•
•
•
•
•
•
•
•
•
•
• •
••
•
•
•• •
•
•
•
•
•
•
•••
• •
•
•
•
•
••
• •
•
•
• •
• ••
••
•
•
•
•••• • •
•
•
••
•••
•
• •
•
•
•
•
•
•
• •
•
•••
•••
• •• •• •
•••
•
••
••
•
•
•
•
••
•
•
•••
••
• •••
•
•
•
•
• ••
•
••
•
•
•
••
•
•••
•
•
••
•
•
•
•
• •
•
•
••
•
•
•
•
•
•
•
•
•
•
•
•
•
•
•
•
•
•
•
•
•
•
•
•
•
•
•
•
•
•
•
•
•
•
•
••••
•
•
•
•
•
•
•
•
••
•
•
•
•
•
•
•• •
•
•
•
•
•
•
•
•
•
•
•
•
••
•
•
••
•
•
•
•
•
•
••
••••
•
•
•
•
•• •
••
•
••••
• •
••
••
•••
•
•
•
•
•
•••••
•
• •
••
•
••
•
• •••• •
•
•
•
•
••
••
•
•
•
•
• •
•
••• •
••
•
•
•
•
•
•
••
•
•••
•
• •
•
•
•
•
•
•
•
•
••
•
•
•
•
••
•
•
•
•
• •
•
•
••
•
•
•
•
••
•
•
••
•
•
•
••
•
•
•••
•
•
• • •
•
•
•• ••
••
•
• •
••
•
•
•
•••••
••
• ••• •
•
••
••
•
••
••
•
• •
••
•
•
••
•
•
•
•••
•
••• ••
••••
• ••
•• •
• •
•
•
••• •
•
• •
•
••
•
• •••
•
•
•
• •
•
••
••
•
••
••
••
•
•
•
•
•
•
••• •
••
•
•
•
•
••
•••
•
•
••
•••
••••
•
••
••
•
••••
•
••
• •
•••••••
•••••••••••••••
•
•
• •
•
•
•• •• ••
• •
••• ••• •
•
•
••••
•
•
••
•
•
• •
•• •
••
•
••
•••
••
•
•
•
•
• ••
•• ••
••• ••
• •• ••
••
••••
•
•
•
• •
•••
•• •
•
•
••
•
••
•
•
••• •
••
•
•••• ••
•• •
••
•
•
•
•
••
•
•
••
•
•
•• •
•
•
•
•
•••
•
•
•
•
•
•
• •
•••
•
•
•
•
•
••
• •
•••• •••
•
•
•
•
•
••
•
• •
•
•
••
•
•
•
•
• ••
•
•
• •
• •
•••
•
•
•
•
•••• •
••
•
•
•
•
•
•
•
•
••
•
•
••
••••
•
••
• •
•
•
• •
•
•
•
•
••
•
• • ••
•• • •
•
•
•
• •
• •
• •
•
•
•
•
•
••••• •
•
•
•
•• ••
•
• •••
• ••
•••••
•
•
•
••
•
•
••
•
•
•
•
•
••
••••
•
•
•••
•••
•
• •
•••
•
•
•
•
•
•
• •
•
•
•
•
•
•
•
•
•
•
•
•
•
•
•
• •
•
•
•
•• •
•
•
•
•
•
•
•
• •
•
•
••
•
•
••
• •
•
••
•
•
•
•
•
•
•
•
•
•
•• •
•
•
• •
•
•
• ••
•
••
•
•
•• ••
••
•
• •
•
••
•
•
•
•
•
•
•
••
•
••
•
•
•
•
•
•
••
•
••
•
• •
•
•
••
• •
• •
• •
• ••
••
•
••
•
•
•
•
•••
•
•
••
••
•
•
•
•
•
•
•
•• •
•
• •
•
•
•
•
•
•
•
• •
••
• •
•
•
• •••
•
•
••
••
•••
••••••
•••
•
•
• •
•
•••
• ••
•
••
•
•
•
••
•• ••••• •
•
•
• •
•
•
• •••
•
•
• ••
•
•• •
• •
•
••••••••
•
•
••
•
•
•
•
•
•
•
• •
•
•
•••
•••
• •••••••
••• •• •••••••••
•••• •
•••
••••••
•• •••
••••••
•
••
•
••
•• •••
•
• ••
•
• •
•••••• •
•••
• •• • •
•• ••
•••
•
•
••
•
•••••
• •
•
•
• • •
•
• •
•••••
••••
•
••••• •
••
•
•••
•
•
•
•
•••• •
• •••
••••
•
•
•
•
•
••
• ••••••••••••
• •••••
•
• ••
•
•
•
•
•
•
•• •••••
••••••
•••••••••
•
•
•• ••
••
•
••
• •• •
•
•
•
•
•
•
••
•
• •
•
••
••
•
•••••
••••
•
•
•
•
•
•
• •
••• •
•
••
•
•
•• •
••
•
•
•
•
•
•
•
•
•
•
•
•
••
•
•• •• •
••
••
•
•
• •
•
•
• • ••
•
•
•
• •••
•••
••• •
•
••••••
• • •
• •• ••
•• •
•
•
•
•
•
••
•
•
•
• •••
•
•
•
•
•
•• •
• •
•
•
•
•
••
••••
•
•
• •
•
•••
•••
• •
•
••
•
••
•
•
•
•
•
•
••••
••••
•
•
•
••••••
•• •
•
• ••• ••
•• •
••••
•
••
• •••
•
•••••••• •
••• ••
• • •
• ••••
• •
•••••• •
•
•
•
••••
•
•
• •••
• • •
•
• ••
•
•
•••
•
•
••••
••
••
•
• ••
•••
••
••
•
••
• • •••
•
•
•
•
•••••
•
••
••
• ••
••••
•
•
•
•••
•
•
•
•
••
• ••
••
•
•• ••
•
• ••
••• ••
• •
•
•
••
•
•
•
• •
•
••
•
•
•
•
•
••
•• •
•
•
•
•
•
•
•
•
•
•
•
•
•
•••
•
•
•
••
•
•
•
•
•
•
•
•
•
•
• ••
•
•
•
•
•
•••
•
•
•
•
••
•••• •
••
•
•
•• •• ••
•• •
•••
•
•
•••
•
•
• •
•
•
• •
•••
• ••••
•
• •• •
••
•
•
•
•••••
•
•• •
•
•
•
•
•
•
•
••
••
••
•
• •
•
• •
••
••
• •
••
•
•
•
•
•
•• •
•
••
•• ••
••
•
•••
••• • ••
•••••
• ••••
•• •
••
•• ••
•
•
• •
•
••
• •
• •
••
•• •
•
•
•
•
•
•
•
•
•
••
••• •
•
••
•
•• •
•• ••
•
•
•
••
•
•
• • •
•
••••••
••
•
•
••••••
•
•
BMW
Siemens
−0.15
−0.10 −0.05
0
−0.15
−0.10
−0.05
0
1
2
3
−0.15
−0.05
0.05
02.01.85
02.01.87
02.01.89
02.01.91
02.01.93
1
2
3
−0.15
−0.05
0.05
1
2
3
(a)
(b)
(c)
0.10
0.05
0.10
0.05
Figure 4.4.
Three extreme days on which German stock returns (in this case (a) BMW and
(b) Siemens) showed large negative returns. The dates are 19 October 1987, 16 October 1989
and 19 August 1991; see text for historical commentary.
19 August 1991, the day of the coup by communist hardliners during the reforming
era of Gorbachev in the USSR. Clearly, the returns on these extreme days are lined
up on the diagonal of the scatterplot in the lower-left-hand corner and it is easy to
see why one might describe these as occasions on which correlations tend to one.
While it may be partly true that useful multivariate time series models for returns
should have the property that conditional correlations tend to become large when
volatilities are large, the phenomenon of simultaneous extreme values can also be
addressed by choosing distributions in multivariate models that allow so-called tail
or extremal dependence; a mathematical deﬁnition of this notion and a discussion
of its importance may be found in Section 5.2.3 of the chapter on copulas.
Notes and Comments
A number of texts contain extensive empirical analyses of ﬁnancial return series and
discussions of their properties. We mention in particular Taylor (1986), Alexander
(2001), Tsay (2002) and Zivot andWang (2003). For more discussion of the randomwalkhypothesisforstockreturnsanditsshortcomingsseeLoandMacKinlay(1999).
4.2
Fundamentals of Time Series Analysis
This section provides a short summary of the essentials of classical univariate time
series analysis with a focus on that which is relevant for modelling risk-factor return
series. We have based the presentation on Brockwell and Davis (1991, 2002), so
these texts may be used as supplementary reading.
4.2.1
Basic Deﬁnitions
A time series model for a single risk factor is a stochastic process (Xt)t∈Z, i.e. a family of rvs, indexed by the integers and deﬁned on some probability space (Ω, F , P).
--- page 142 ---

126
4. Financial Time Series
Moments of a time series.
Assuming they exist, we deﬁne the mean function µ(t)
and autocovariance function γ (t, s) of (Xt)t∈Z by
µ(t) = E(Xt),
t ∈Z,
γ (t, s) = E((Xt −µ(t))(Xs −µ(s))),
t, s ∈Z.
It follows that the autocovariance function satisﬁes γ (t, s) = γ (s, t) for all t, s, and
γ (t, t) = var(Xt).
Stationarity.
Generally, the processes we consider will be stationary in one or both
of the following two senses.
Deﬁnition 4.1 (strict stationarity). The time series (Xt)t∈Z is strictly stationary if
(Xt1, . . . , Xtn) d= (Xt1+k, . . . , Xtn+k),
for all t1, . . . , tn, k ∈Z and for all n ∈N.
Deﬁnition 4.2 (covariance stationarity). The time series (Xt)t∈Z is covariance
stationary (or weakly or second-order stationary) if the ﬁrst two moments exist and
satisfy
µ(t) = µ,
t ∈Z,
γ (t, s) = γ (t + k, s + k),
t, s, k ∈Z.
Both these deﬁnitions attempt to formalize the notion that the behaviour of a time
series is similar in any epoch in which we might observe it. Systematic changes in
mean, variance or the covariances between equally spaced observations are inconsistent with stationarity.
It may be easily veriﬁed that a strictly stationary time series with ﬁnite variance
is covariance stationary, but it is important to note that we may deﬁne inﬁnitevariance processes (including certain ARCH and GARCH processes) which are
strictly stationary but not covariance stationary.
Autocorrelation in stationary time series.
The deﬁnition of covariance stationarity
implies that for all s, t we have γ (t −s, 0) = γ (t, s) = γ (s, t) = γ (s −t, 0), so
that the covariance between Xt and Xs only depends on their temporal separation
|s −t|, which is known as the lag. Thus, for a covariance-stationary process we
write the autocovariance function as a function of one variable:
γ (h) := γ (h, 0),
∀h ∈Z.
Noting that γ (0) = var(Xt), ∀t, we can now deﬁne the autocorrelation function of
a covariance-stationary process.
Deﬁnition 4.3 (autocorrelation function). The autocorrelation function (ACF)
ρ(h) of a covariance-stationary process (Xt)t∈Z is
ρ(h) = ρ(Xh, X0) = γ (h)/γ (0),
∀h ∈Z.
Wespeakoftheautocorrelationorserialcorrelation ρ(h)atlagh.Inclassicaltime
series analysis the set of serial correlations and their empirical analogues estimated
from data are the objects of principal interest. The study of autocorrelations is known
as analysis in the time domain.
--- page 143 ---

4.2. Fundamentals of Time Series Analysis
127
White noise processes.
The basic building blocks for creating useful time series
models are stationary processes without serial correlation, known as white noise
processes and deﬁned as follows.
Deﬁnition 4.4 (white noise). (Xt)t∈Z is a white noise process if it is covariance
stationary with autocorrelation function
ρ(h) =

1,
h = 0,
0,
h̸ = 0.
A white noise process centred to have mean zero with variance σ 2 = var(Xt)
will be denoted WN(0, σ 2). A simple example of a white noise process is a series
of iid rvs with ﬁnite variance, and this is known as a strict white noise process.
Deﬁnition 4.5 (strict white noise). (Xt)t∈Z is a strict white noise process if it is a
series of iid, ﬁnite-variance rvs.
A strict white noise (SWN) process centred to have mean zero and variance σ 2
will be denoted SWN(0, σ 2). Although SWN is the easiest kind of noise process to
understand, it is not the only noise that we will use. We will later see that covariancestationary ARCH and GARCH processes are in fact white noise processes.
Martingale difference.
One further noise concept that we use, particularly when we
come to discuss volatility and GARCH processes, is that of a martingale-difference
sequence. To discuss this concept we further assume that the time series (Xt)t∈Z
is adapted to some ﬁltration (Ft)t∈Z which represents the accrual of information
over time. The sigma algebra Ft represents the available information at time t and
typically this will be the information contained in past and present values of the time
series itself (Xs)s⩽t, which we refer to as the history up to time t and denote by
Ft = σ({Xs : s ⩽t}); the corresponding ﬁltration is known as the natural ﬁltration.
In a martingale-difference sequence the expectation of the next value, given current information, is always zero, and we have observed in Section 4.1.1 that this
property may be appropriate for ﬁnancial return data. A martingale difference is
often said to model our winnings in consecutive rounds of a fair game.
Deﬁnition 4.6 (martingale difference). The time series (Xt)t∈Z is known as a
martingale-difference sequence with respect to the ﬁltration (Ft)t∈Z if E|Xt| < ∞,
Xt is Ft-measurable (adapted) and
E(Xt | Ft−1) = 0,
∀t ∈Z.
Obviously the unconditional mean of such a process is also zero:
E(Xt) = E(E(Xt | Ft−1)) = 0,
∀t ∈Z.
Moreover, if E(X2
t ) < ∞for all t, then autocovariances satisfy
γ (t, s) = E(XtXs)
=

E(E(XtXs | Fs−1)) = E(XtE(Xs | Fs−1)) = 0,
t < s,
E(E(XtXs | Ft−1)) = E(XsE(Xt | Ft−1)) = 0,
t > s.
--- page 144 ---

128
4. Financial Time Series
Thus a ﬁnite-variance martingale-difference sequence has zero mean and zero
covariance. If the variance is constant for all t, it is a white noise process.
4.2.2
ARMA Processes
The family of classical ARMA processes are widely used in many traditional applications of time series analysis. They are covariance-stationary processes that are
constructed using white noise as a basic building block. As a general notational
convention in this section and the remainder of the chapter we will denote white
noise by (εt)t∈Z and strict white noise by (Zt)t∈Z.
Deﬁnition 4.7 (ARMA process). Let (εt)t∈Z be WN(0, σ 2
ε ).The process (Xt)t∈Z is
a zero-mean ARMA(p, q) process if it is a covariance-stationary process satisfying
difference equations of the form
Xt −φ1Xt−1 −· · · −φpXt−p = εt + θ1εt−1 + · · · + θqεt−q,
∀t ∈Z.
(4.3)
(Xt) is an ARMA process with mean µ if the centred series (Xt −µ)t∈Z is a zeromean ARMA(p, q) process.
Note that, according to our deﬁnition, there is no such thing as a non-covariancestationary ARMA process. Whether the process is strictly stationary or not will
depend on the exact nature of the driving white noise, also known as the process
of innovations. If the innovations are iid, or themselves form a strictly stationary
process, then the ARMA process will also be strictly stationary.
For all practical purposes we can restrict our study of ARMA processes to causal
ARMA processes. By this we mean processes satisfying the equations (4.3) which
have a representation of the form
Xt =
∞

i=0
ψiεt−i,
(4.4)
where the ψi are coefﬁcients which must satisfy
∞

i=0
|ψi| < ∞.
(4.5)
Remark 4.8. The so-called absolute summability condition (4.5) is a technical
condition which ensures that E|Xt| < ∞. This guarantees that the inﬁnite sum
in (4.4) converges absolutely, almost surely, meaning that both ∞
i=0 |ψi∥εt−i| and
∞
i=0 ψiεt−i are ﬁnite with probability one (see Brockwell and Davis 1991, Proposition 3.1.1).
We now verify by direct calculation that causal ARMA processes are indeed
covariance stationary and calculate the form of their autocorrelation function before
going on to look at some simple standard examples.
Proposition 4.9. Any process satisfying (4.4) and (4.5) is covariance stationary
with an autocorrelation function given by
ρ(h) =
∞
i=0 ψiψi+|h|
∞
i=0 ψ2
i
,
h ∈Z.
(4.6)
--- page 145 ---

4.2. Fundamentals of Time Series Analysis
129
Proof. Obviously, for all t we have E(Xt) = 0 and var(Xt) = σ 2
ε
∞
i=0 ψ2
i < ∞,
due to (4.5). Moreover, the autocovariances are given by
cov(Xt, Xt+h) = E(XtXt+h) = E
 ∞

i=0
ψiεt−i
∞

j=0
ψjεt+h−j

.
Since (εt) is white noise, it follows that E(εt−iεt+h−j)̸ = 0 ⇐⇒j = i + h, and
hence that
γ (h) = cov(Xt, Xt+h) = σ 2
ε
∞

i=0
ψiψi+|h|,
h ∈Z,
(4.7)
which depends only on the lag h and not on t. The autocorrelation function follows
easily.
Example 4.10 (MA(q) process). It is clear that a pure moving-average process
Xt =
q

i=1
θiεt−i + εt
(4.8)
forms a simple example of a causal process of the form (4.4). It is easily inferred
from (4.6) that the autocorrelation function is given by
ρ(h) =
q−|h|
i=0
θiθi+|h|
q
i=0 θ2
i
,
|h| ∈{0, 1, . . . , q},
where θ0 = 1. For |h| > q we have ρ(h) = 0 and the autocorrelation function is
said to cut off at lag q. If this feature is observed in the estimated autocorrelations
of empirical data, it is often taken as an indicator of moving-average behaviour. A
realization of an MA(4) process together with the theoretical form of its ACF is
shown in Figure 4.5.
Example 4.11 (AR(1) process). The ﬁrst-order AR process satisﬁes the set of
difference equations
Xt = φXt−1 + εt,
∀t.
(4.9)
This process is causal if and only if |φ| < 1, and this may be understood intuitively
by iterating the equation (4.9) to get
Xt = φ(φXt−2 + εt−1) + εt−2
= φk+1Xt−k−1 +
k

i=0
φiεt−i.
Using more careful probabilistic arguments it may be shown that the condition
|φ| < 1 ensures that the ﬁrst term disappears as k →∞and the second term
converges. The process
Xt =
∞

i=0
φiεt−i
(4.10)
--- page 146 ---

130
4. Financial Time Series
−4
−2
0
ACF
0
0.2
0.4
0.6
0.8
1.0
ACF
−0.5
0
0.5
1.0
0
200
400
600
800
1000
Lag
ACF
0
10
15
20
25
30
0
0.2
0.4
0.6
0.8
1.0
5
4
2
−4
−2
0
4
2
−4
−2
0
4
2
(a)
(b)
(c)
Figure 4.5.
A number of simulated ARMA processes with their autocorrelation functions (dashed) and correlograms. Innovations are Gaussian. (a) AR(1), φ = 0.8. (b) MA(4),
θ = −0.8, 0.4, 0.2, −0.3. (c) ARMA(1, 1), φ = 0.6, θ = 0.5.
turns out to be the unique solution of the deﬁning equations (4.9). It may be easily
veriﬁed that this is a process of the form (4.4) and that ∞
i=0 |φ|i = (1 −|φ|)−1
so that (4.5) is satisﬁed. Looking at the form of the solution (4.10), we see that the
AR(1) process can be represented as an MA(∞) process: an inﬁnite-order movingaverage process.
Theautocovarianceandautocorrelationfunctionsoftheprocessmaybecalculated
from (4.7) and (4.6) to be
γ (h) = φ|h|σ 2
ε
1 −φ2 ,
ρ(h) = φ|h|,
h ∈Z.
Thus theACF is exponentially decaying with possibly alternating sign.A realization
of an AR(1) process together with the theoretical form of its ACF is shown in
Figure 4.5.
--- page 147 ---

4.2. Fundamentals of Time Series Analysis
131
Remarks on general ARMA theory.
In the case of the general ARMA process of
Deﬁnition 4.7, the issue of whether this process has a causal representation of the
form (4.4) is resolved by the study of two polynomials in the complex plane, which
are given in terms of the ARMA model parameters by
˜φ(z) = 1 −φ1z −· · · −φpzp,
˜θ(z) = 1 + θ1z + · · · + θqzq.
Provided that ˜φ(z) and ˜θ(z) have no common roots, then the ARMA process is a
causal process satisfying (4.4) and (4.5) if and only if ˜φ(z) has no roots in the unit
circle |z| ⩽1. The coefﬁcients ψi in the representation (4.4) are determined by the
equation
∞

i=0
ψizi =
˜θ(z)
˜φ(z)
,
|z| < 1.
Example 4.12 (ARMA(1, 1) process). For the process given by
Xt −φXt−1 = εt + θεt−1,
∀t ∈Z,
the complex polynomials are ˜φ(z) = 1 −φz and ˜θ(z) = 1 + θz and these have no
common roots provided φ + θ̸ = 0. The solution of ˜φ(z) = 0 is z = 1/φ and this
is outside the unit circle provided |φ| < 1, so that this is the condition for causality
(as in the AR(1) model of Example 4.11).
The representation (4.4) can be obtained by considering
∞

i=0
ψizi = 1 + θz
1 −φz = (1 + θz)(1 + φz + φ2z2 + · · · ),
|z| < 1,
and is easily calculated to be
Xt = εt + (φ + θ)
∞

i=1
φi−1εt−i.
(4.11)
Using (4.6) we may calculate that for h̸ = 0 the ACF is
ρ(h) = φ|h|−1(φ + θ)(1 + φθ)
1 + θ2 + 2φθ
.
A realization of an ARMA(1, 1) process together with the theoretical form of its
ACF is shown in Figure 4.5.
Invertibility.
Equation (4.11) shows how the ARMA(1, 1) process may be thought
of as an MA(∞) process. In fact, if we impose the condition |θ| < 1, we can also
express (Xt) as the AR(∞) process given by
Xt = εt + (φ + θ)
∞

i=1
(−θ)i−1Xt−i.
(4.12)
If we rearrange this to be an equation for εt, then we see that we can, in a sense,
“reconstruct” the latest innovation εt from the entire history of the process (Xs)s⩽t.
--- page 148 ---

132
4. Financial Time Series
The condition |θ| < 1 is known as an invertibility condition, and for the general
ARMA(p, q) process the invertibility condition is that ˜θ(z) should have no roots
in the unit circle |z| ⩽1. In practice, the models we ﬁt to real data will be both
invertible and causal solutions of the ARMA-deﬁning equations.
Models for the conditional mean.
Consider a general invertibleARMA model with
non-zero mean. For what comes later it will be useful to observe that we can write
such models as
Xt = µt + εt,
µt = µ +
p

i=1
φi(Xt−i −µ) +
q

j=1
θjεt−j.
(4.13)
Since we have assumed invertibility, the terms εt−j, and hence µt, can be written in
terms of the inﬁnite past of the process up to time t −1; µt is said to be measurable
with respect to Ft−1 = σ({Xs : s ⩽t −1}).
If we make the assumption that the white noise (εt)t∈Z is a martingale-difference
sequence (see Deﬁnition 4.6) with respect to (Ft)t∈Z, then E(Xt | Ft−1) = µt.
In other words, such an ARMA process can be thought of as putting a particular
structure on the conditional mean µt of the process. ARCH and GARCH processes
will later be seen to put structure on the conditional variance var(Xt | Ft−1).
ARIMA models.
In traditional time series analysis we often consider an even larger
class of model known as ARIMA, or autoregressive integrated moving-average
models. Let ∇denote the difference operator, so that for a time series process
(Yt)t∈Z we have ∇Yt = Yt −Yt−1. Denote repeated differencing by ∇d, where
∇dYt =

∇Yt,
d = 1,
∇d−1(∇Yt) = ∇d−1(Yt −Yt−1),
d > 1.
(4.14)
The time series (Yt) is said to be an ARIMA(p, d, q) process if the differenced
series (Xt) given by Xt = ∇dYt is an ARMA(p, q) process. For d > 1 ARIMA
processes are non-stationary processes. They are popular in practice because the
operation of differencing (once or more than once) can turn a dataset that is obviously
“non-stationary” into a dataset that might plausibly be modelled by a stationary
ARMA process. For example, if we use an ARMA(p, q) process to model daily
log-returns of some price series (St), then we are really saying that the original
logarithmic price series (ln St) follows an ARIMA(p, 1, q) model.
When the word integrated is used in the context of time series it generally implies
that we are looking at a non-stationary process that might be made stationary by
differencing; see also the discussion of IGARCH models in Section 4.3.2.
4.2.3
Analysis in the Time Domain
We now assume that we have a random sample X1, . . . , Xn from a covariancestationary time series model (Xt)t∈Z.Analysis in the time domain involves calculating empirical estimates of autocovariances and autocorrelations from this random
sample and using these estimates to make inference about the serial dependence
structure of the underlying process.
--- page 149 ---

4.2. Fundamentals of Time Series Analysis
133
Correlogram.
The sample autocovariances are calculated according to
ˆγ (h) = 1
n
n−h

t=1
(Xt+h −¯X)(Xt −¯X),
0 ⩽h < n,
where ¯X = n
t=1 Xt/n is the sample mean, which estimates µ, the mean of the
time series. From these we calculate the sample ACF:
ˆρ(h) = ˆγ (h)/ ˆγ (0),
0 ⩽h < n.
Thecorrelogram istheplot{(h, ˆρ(h)) : h = 0, 1, 2, . . . },whichisdesignedtofacilitatetheinterpretationofthesampleACF.CorrelogramsforvarioussimulatedARMA
processes are shown in Figure 4.5; note that the estimated correlations correspond
reasonably closely to the theoretical ACF for these particular realizations.
To interpret such estimators of serial correlation, we need to know something
about their behaviour for particular time series. The following general result is for
causal linear processes, which are processes of the form (4.4) driven by strict white
noise.
Theorem 4.13. Let (Xt)t∈Z be the linear process
Xt −µ =
∞

i=0
ψiZt−i,
where
∞

i=0
|ψi| < ∞, (Zt)t∈Z ∼SWN(0, σ 2
Z).
Suppose that either E(Z4
t ) < ∞or ∞
i=0 iψ2
i < ∞. Then, for h ∈{1, 2, . . . }, we
have
√n( ˆρ(h) −ρ(h))
d−→Nh(0, W),
where
ˆρ(h) = ( ˆρ(1), . . . , ˆρ(h))′,
ρ(h) = (ρ(1), . . . , ρ(h))′,
and W has elements
Wij =
∞

k=1
(ρ(k + i) + ρ(k −i) −2ρ(i)ρ(k))(ρ(k + j) + ρ(k −j) −2ρ(j)ρ(k)).
Proof. This follows as a special case of a result in Brockwell and Davis (1991,
pp. 221–223).
The condition ∞
i=0 iψ2
i < ∞holds for ARMA processes, so ARMA processes
driven by SWN fall under the scope of this theorem (regardless of whether fourth
moments exist for the innovations or not).
Trivially, the theorem also applies to SWN itself. For SWN we have
√n ˆρ(h)
d−→Nh(0, Ih),
so for sufﬁciently large n the sample autocorrelations of data from an SWN
process will behave like iid normal observations with mean zero and variance
--- page 150 ---

134
4. Financial Time Series
1/n. Ninety-ﬁve per cent of the estimated correlations should lie in the interval
(−1.96/√n, 1.96/√n), and it is for this reason that correlograms are drawn with
conﬁdence bands at these values. If more than 5% of estimated correlations lie outside these bounds, then this is considered as evidence against the null hypothesis
that the data are strict white noise.
Remark 4.14. In light of the discussion of the asymptotic behaviour of sample
autocorrelations for SWN it might be asked how these estimators behave for white
noise. However, this is an extremely general question because white noise encompasses a variety of possible underlying processes (including the standard ARCH
and GARCH processes we later address) which only share second-order properties
(ﬁniteness of variance and lack of serial correlation). In some cases the standard
Gaussian conﬁdence bands apply; in some cases they do not. For a GARCH process
the critical issue turns out to be the heaviness of the tail of the stationary distribution
(see Mikosch and St˘aric˘a 2000, for more details).
Portmanteau tests.
It is often useful to combine the visual analysis of the correlogram with a formal numerical test of the strict white noise hypothesis, and a popular
test is that of Ljung and Box, as applied in Section 4.1.1. Under the null hypothesis
of SWN, the statistic
QLB = n(n + 2)
h

j=1
ˆρ(j)2
n −j
has an asymptotic chi-squared distribution with h degrees of freedom. This statistic
is generally preferred to the simpler Box–Pierce statistic QBP = nh
j=1 ˆρ(j)2,
which also has an asymptotic χ2
h distribution under the null hypothesis, although
the chi-squared approximation may not be so good in smaller samples. These tests
are the most commonly applied portmanteau tests.
If a series of rvs forms an SWN process, then the series of absolute or squared
variables must also be iid. It is a good idea to also apply the correlogram and Ljung–
Box tests to absolute values as a further test of the SWN hypothesis. We prefer to
perform tests of the SWN hypothesis on the absolute values rather than the squared
values because the squared series is only an SWN (according to the deﬁnition we
use) when the underlying series has a ﬁnite fourth moment. Daily log-return data
often point to models with an inﬁnite fourth moment
4.2.4
Statistical Analysis of Time Series
In practice, the statistical analysis of time series data X1, . . . , Xn follows a programme consisting of the following stages.
Preliminary analysis.
The data are plotted and the plausibility of a single stationary model is considered. Since we concentrate here on differenced logarithmic value
series, we will assume that at most minor preliminary manipulation of our data is
required. Classical time series analysis has many techniques for removing trends
and seasonalities from “non-stationary” data; these techniques are discussed in all
standard texts including Brockwell and Davis (2002) and Chatﬁeld (1996). While
--- page 151 ---

4.2. Fundamentals of Time Series Analysis
135
certain kinds of ﬁnancial time series certainly do show seasonal patterns, such as
earnings time series, we will assume that such effects are relatively minor in the
kinds of daily or weekly return series that are the basis of risk-management methods. If we were to base our risk management on high-frequency data, preliminary
cleaning would be more of an issue, since these show clear diurnal cycles and other
deterministic features (see Dacorogna et al. 2001).
Obviously the assumption of stationarity becomes more questionable if we take
long data windows, or if we choose windows in which well-known economic policy
shifts have taken place.Although the markets change constantly there will always be
a tension between our desire to use the most up-to-date data and our need to include
enough data to have precision in statistical estimation. Whether half a year of data,
one year, ﬁve years or 10 years are appropriate will depend on the situation. It is
certainly a good idea to perform a number of analyses with different data windows
and to investigate the sensitivity of statistical inference to the amount of data.
Analysis in the time domain.
Having settled on the data, the techniques of Section 4.2.3 come into play. By applying correlograms and portmanteau tests such as
Ljung–Box to both the raw data and their absolute values, the SWN hypothesis is
evaluated. If it cannot be rejected for the data in question, then the formal time series
analysis is over and simple distributional ﬁtting could be used instead of dynamic
modelling.
For daily risk-factor return series we expect to quickly reject the SWN hypothesis.
Despite the fact that correlograms of the raw data may show little evidence of serial
correlation, correlograms of the absolute data are likely to show evidence of strong
serial dependence. In other words the data may support a white noise model but not
a strict white noise. In this case ARMA modelling is not required, but the volatility
models of Section 4.3 may be useful.
If the correlogram does provide evidence of the kind of serial correlation patterns
produced by ARMA processes, then we can attempt to ﬁt ARMA processes to data.
Model ﬁtting.
A traditional approach to model ﬁtting ﬁrst attempts to identify the
order of a suitable ARMA process using the correlogram and a further tool known
as the partial correlogram (not described in this book but found in all standard texts).
For example, the presence of a cut-off at lag q in the correlogram (see Example 4.10)
is taken as a diagnostic for pure moving-average behaviour of order q (and similar behaviour in a partial correlogram indicates pure AR behaviour). With modern
computing power it is now quite easy to simply ﬁt a variety of MA, AR and ARMA
models and to use a model-selection criterion like that of Akaike (described in Section A.3.6) to choose the “best” model. There are also automated model choice
procedures such as the method of Tsay and Tiao (1984).
Sometimes there are a priori reasons for expecting certain kinds of model to
be most appropriate. For example, suppose we analyse longer-period returns that
overlap, as in Equation 4.2. Consider the case where the raw data are daily returns
and we build weekly returns. In (4.2) we set h = 5 (to get weekly returns) and k = 1
(to get as much data as possible). Assuming that the underlying data are genuinely
--- page 152 ---

136
4. Financial Time Series
from a white noise process (Xt)t∈Z ∼WN(0, σ 2), the weekly aggregated returns
at times t and t + l satisfy
cov(X(5)
t
, X(5)
t+l) = cov

4

i=0
Xt−i,
4

j=0
Xt+l−j

=

(5 −l)σ 2,
l = 0, . . . , 4
0,
l ⩾5,
so that the overlapping returns have the correlation structure of an MA(4) process,
and this would be a natural choice of time series model for them.
Having chosen the model to ﬁt, there are a number of possible ﬁtting methods,
including specialized methods for AR processes, such as Yule–Walker, that make
minimal assumptions concerning the distribution of the white noise innovations;
we refer to the standard time series literature for more details. In Section 4.3.4 we
discuss the method of (conditional) maximum likelihood, which may be used to ﬁt
ARMA models with (or without) GARCH errors to data.
Residual analysis and model comparison.
Recall the representation of a causal
and invertible ARMA process in (4.13) and suppose we have ﬁtted such a process
and estimated the parameters φi and θj. The residuals are inferred values ˆεt for the
unobserved innovations εt and they are calculated recursively from the data and
ﬁtted model by
ˆεt = Xt −ˆµt,
ˆµt = ˆµ +
p

i=1
ˆφi(Xt−i −ˆµ) +
q

j=1
ˆθj ˆεt−j,
(4.15)
where the values ˆµt are sometimes known as the ﬁtted values. Obviously, we have a
problem calculating the ﬁrst few values of ˆεt due to the ﬁniteness of our data sample
and the inﬁnite nature of the recursions (4.15). One of many possible solutions might
be to set ˆε−q+1 = ˆε−q+2 = · · · = ˆε0 = 0 and X−p+1 = X−p+2 = · · · = X0 = ¯X
and then to use (4.15) for t = 1, . . . , n. Since the ﬁrst few values will be inﬂuenced
by these starting values, they might be ignored in later analyses.
The residuals (ˆεt) should behave like a realization of a white noise process,
since this is our model assumption for the innovations, and this can be assessed by
constructing their correlogram. If there is still evidence of serial correlation in the
correlogram, then this suggests that a good ARMA model has not yet been found.
Moreover, we can use portmanteau tests to test formally that the residuals behave
like a realization of a strict white noise process. If the residuals behave like SWN,
then no further time series modelling is required; if they behave like WN but not
SWN, then the volatility models of Section 4.3 may be required.
It is usually possible to ﬁnd more than one reasonable ARMA model for the
data, and formal model-comparison techniques may be required to decide on an
overall best model or models. The Akaike model-selection criterion described in
Section A.3.6 might be used, or one of a number of variants on this criterion which
are often preferred for time series (see Brockwell and Davis 2002, Section 5.5.2).
4.2.5
Prediction
There are many approaches to the forecasting or prediction of time series and we
summarize two which extend easily to the case of GARCH models. The ﬁrst strategy
--- page 153 ---

4.2. Fundamentals of Time Series Analysis
137
makes use of ﬁtted ARMA (or ARIMA) models and is sometimes called the Box–
Jenkins approach (Box and Jenkins 1970). The second strategy is a model-free
approach to forecasting known as exponential smoothing, which is related to the
exponentially weighted moving-average technique for predicting volatility.
Prediction using ARMA models.
Consider the invertible ARMA model and its
representation in (4.13). Let Ft denote the history of the process up to and including time t as before and assume that the innovations (εt)t∈Z have the martingaledifference property with respect to (Ft)t∈Z.
For the prediction problem it will be convenient to denote our sample of n data
by Xt−n+1, . . . , Xt. We assume these are realizations of rvs following a particular
ARMA model. Our aim is to predict Xt+1 or more generally Xt+h, and we denote
our prediction by PtXt+h. The method we describe assumes that we have access
to the inﬁnite history of the process up to time t and derives a formula that is then
approximated for our ﬁnite sample.
As a predictor of Xt+h we use the conditional expectation E(Xt+h | Ft). Among
all predictions PtXt+h based on the inﬁnite history of the process up to time t, this
predictor minimizes the mean squared prediction error E((Xt+h −PtXt+h)2).
The basic idea is that, for h ⩾1, the prediction E(Xt+h | Ft) is recursively
evaluated in terms of E(Xt+h−1 | Ft). We use the fact that E(εt+h | Ft) = 0 (the
martingale-difference property of innovations) and that the rvs (Xs)s⩽t and (εs)s⩽t
are “known” at time t. The assumption of invertibility (4.12) ensures that the innovation εt can be written as a function of the inﬁnite history of the process (Xs)s⩽t.
To illustrate the approach it will sufﬁce to consider an ARMA(1, 1) model, the
generalization to ARMA(p, q) models following easily.
Example 4.15 (prediction for the ARMA(1, 1) model). Suppose an ARMA(1, 1)
model of the form (4.13) has been ﬁtted to the data and its parameters µ, φ and θ
have been determined. Our one-step prediction for Xt+1 is
E(Xt+1 | Ft) = µt+1 = µ + φ(Xt −µ) + θεt,
since E(εt+1 | Ft) = 0. For a two-step prediction we get
E(Xt+2 | Ft) = E(µt+2 | Ft) = µ + φ(E(Xt+1 | Ft) −µ)
= µ + φ2(Xt −µ) + φθεt,
and in general we have
E(Xt+h | Ft) = µ + φh(Xt −µ) + φh−1θεt.
Without knowing all historical values of (Xs)s⩽t this predictor cannot be evaluated exactly, but it can be accurately approximated if n is reasonably large. The
easiest way of doing this is to substitute the model residual ˆεt calculated from (4.15)
for εt. Note that limh→∞E(Xt+h | Ft) = µ, almost surely, so that the prediction
converges to the estimate of the unconditional mean of the process for longer time
horizons.
