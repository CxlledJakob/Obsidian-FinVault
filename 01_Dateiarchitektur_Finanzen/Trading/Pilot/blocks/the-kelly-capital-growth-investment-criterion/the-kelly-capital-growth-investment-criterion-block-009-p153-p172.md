# The Kelly capital growth investment criterion _ theory and -- Leonard C_ Maclean, Edward O_ Thorp, W_ T_ Ziemba, Leonard -- World Scientific Handbook -- isbn13 9781283148344 -- bec576e26410d0c695fd5b867d08ec4f -- An.pdf — pages 153–172

--- page 153 ---

126
R.Roll
552
The Journal oj Finance
utility viewpoint, despite ultimate ruin. No mathematician can prove the
contrary, especially when it is recognized that a typical investor's horizon will
probably fall short of infinity and that he will likely consume a fraction of his
assets each period. However, one of our basic concerns should not be with
formal proof, but with practical and intuitively credible models of investor
behavior. In this regard, "growth-optimum" portfolios possess appealing features even during a finite time span. For example, such portfolios maximize the
probability of exceeding a given level of wealth within a fixed time.2
Hakansson also pointed out other features of the growth-optimum model that
may be more or less appealing. It implies a logarithmic (in wealth) utility
function, which displays decreasing absolute risk aversion, and it implies
optimal decision rules that are myopic. As a further embellishment, Hakansson
and Liu derived a "separation theorem" that holds the optimal sequence of
investments to be independent of the sequence of wealth levels even when
returns are stochastically dependent across time. (Myopia also holds with temporaldependence).
Although these are strong challenges to the practical superiority of twoparameter portfolio models, we should not abandon the latter too hurriedly.
They have been successfully used in many empirical contexts and their competitors should be required to weather empirical examination; so the purpose of
this paper is to report on some empirical tests of growth-optimum theory using
common stock returns.
Briefly, the growth-optimum model receives mixed support. In some tests it
performs extremely well while the results of other tests are puzzling. In comparison to the mean-variance model it also performs well but the test results are
clouded by the close operational similarity of the two models.
II. A TEST STATISTIC FOR THE GROWTH-OPTIMUM MODEL
The quantitative derivation of the growth-optimum rule will employ the
following convenient
NOTATION:
nJ-number of shares purchased of security j initially
p'ot-price per share of security j in period t.
N
Vt = L n,p'ot-Value of a portfolio of N distinct securities in period t.
J=1
X'ot == n,PJotlf n,PJ.t-fraction of resources invested in security j in t.
RJot = {[ (Pjot + D,.t) /PJ.t _ d -l}-rate of return to security j from t -
1
to t.
D,. t-per share dividend or coupon paid to security j between t -
1 and t.
E-Mathematical expectation.
2. Breiman [1961, section 5). Hakansson seems to have erred slightly when he stl,tes that
"Breiman has shown that if the objective is to achieve a certain level of capital as soon as possible,
then the optimal-growth portfolio .. . minimizes the expected time to reach the given level,"
Hakansson [1971, p. 540]. Breiman conjectured that this was true but was unable to state a proof
for a fixed level of wealth. As wealth grows indefinitely large, however, the limited expected
minimum time is in fact achieved by the "growth-optimum" portfolio.
--- page 154 ---

Evidence on the "Growth-Optimum " Model
127
Growth Optimum Model
553
Since the rule for maximizing the expected growth of portfolio value is
myopic, one only needs to optimize between successive periods. Thus, the
growth-optimum rule is
maximize
E[loge(Vt/Vt_d] == E {1oge[l:jXI.t_l (I + Ri.t )]}
(1)
X t _ 1
subject to l:iXi.t-l == 1. Negative values of X represent short sales which, by
assumption, can be accomplished without penalty. Transaction costs are neglected.
Although the problem is easily solved without further qualifications, for
historical comparison purposes it is worth assuming that the Nth asset, denoted
F, is risk-free and that it receives the residual portion from the amounts invested in all risky assets; i.e.,
~-l
~-l
Vt/Vt_ 1 = L XJ.t - 1 (1 + RJ.t ) + (1 + RF,t) (1 - L xJ.t-J.
First-order conditions from problem (1) show that the investor's growthoptimum portfolio will be determined by proportions X* such that
E
N
== 0; J == 1, ... , N -
1.
(2)
[
~J,t- RF,t
].
1 + RF" + t. X" ,H (i!", -
RF,,)
.
As illustrated by Hakansson [1971] and Breiman [1960], these optimal investment fractions generally will imply a diversified portfolio but their exact values
cannot be determined without specifying the joint probability distribution of
the Rt's.
To obtain a testable proposition from (2), however, it will not be necessary
to specify that distribution. We can rely instead on the fact that in a given
period, the value of
N
,
I + R.".t + l:rXI.t-t (Ri.t -
R F .t ) 1
I
expected by each individual is equal for every risky security. Advancing to an
aggregate level will require either of two traditional assumptions: (a) that all
investors hold identical probability beliefs or (b) that a "representative" investor holds the expectations of equation (2) with the invested proportions
(X*'s) being equal to relative values of existing asset supplies, In either case,
the denominator of (2) is equal to 1 + Rm.I> a "market return" defined as a
value-weighted average of all individual asset returns, The approximately observable8 variable
1 + RJ,t
z"ta! 1 + R m.t
(3 )
3. It is only approximately observable because no comprehensive value-weighted asset indexes
exist.
--- page 155 ---

128
R. Roll
554
The Journal of Finance
will have the same mean for all securities. It will also be true, of course, that
some unexplained variation may occur about these expectations so that the
quantities Zj.t will not be exactly equal in every period. However, an appropriate test of the identity of expectations only requires that corresponding
sample means be statistically equal; that is, the temporally averaged means
T
-
""" 1 + Rj,t /
Zj=L..J
T
t=l 1 + Rm•t
(4)
must be insignificantly different across securities. Testing the equality of N
sample means is an analysis of variance problem. Its application to New York
and American Stock Exchange listed securities will be reported in the next
section.
III. A SIMPLE TEST OF THE GROWTH-OPTIMUM MODEL'S BASIC VALIDITY
Data used in this section are rates of return obtained from the Wells Fargo
rate-oC-return tape prepared by M. Scholes. The tape contains daily price
changes for all common stocks listed on the New York and American exchanges
from June 2, 1962 through July 11, 1969. It is a condensation and thus a
tractable version of the ISL Quarterly Historical Stock Price Tapes. The
Standard & Poor's Composite Price Index (The" SaO") is used to obtain the
"market return."
In the following test, returns were taken over weekly intervals. Thus, the
statistic
ZJ,t = (1 + Rj,t)/( 1 + Rm,t)
was calculated for stock j at the end of week t; where 1 + Rj.t = (Pj,t +
DJ,t)/PJ.t-l and 1 + R m•t was similarly calculated using the S&P Composite
Index. The null hypothesis requires the expected return ratios to be equal,
E(ZJ.t) = E(ZI.t), Cor all i, j, and t. Usually, this would be tested by one-way
-
1
analysis of variance on the temporally-averaged means, Zj == T ~t Zj,t but
simple ·analysis of variance procedures requires that all the ZJ.t'S be uncorrelated cross-sectionally and have equal variances under the null hypothesis.
These assumptions are obviously too strong and are not required by the (null)
growth-optimum hypothesis anyway. Furthermore, we have the evidence of
many previous studies to confirm the existence of positive covariation between
stock returns and returns on a market index. Some researchers (notably King,
[1966]) have calculated directly a substantial co-movement among stock
returns. Although the co variation between two individual stocks returns, say Rj
and Rk , may be reduced in the return ratios (Z's) as the result of division by
1 + R m , it would be too audacious to assert a complete ~limination:...,Further­
more, there is no a priori reason to suppose that Var (ZJ) = V ar (Zk ), as is
required by a simple one-way of' variance.
Fortunately, the Hotelling T2 statistic4 is available for precisely those cases
4. See Morrison [1967, pp. 117-1241 or Graybill, [1961, pp. 205-2061.
--- page 156 ---

Evidence on the "Growth-Optimum" Model
129
Growth Optimum Model
555
where independence among observations and equal variances do not hold. At
the expense of considerable computer time, which is patiently borne by Carnegie-Mellon's undergraduates and the Nation's taxpayers, and is thus free to
its current beneficiaries, this statistic was calculated for groups of 31 stocks
selected alphabetically according to the procedure described below.
Hotelling's T2 is computed as a quadratic form in the sample vector of
differences between adjacent return ratios and the sample covariance matrix
of those differences.s It is distributed as an F distribution with k -
1 and
N -
k + 1 degrees of freedom where N is the sample size (weeks) and k is the
number of stocks in a group.n Since stocks are not always traded over coincidental calendar periods, and since coincidental observations are required in
order to calculate sample covariances, the sample size N of each group was
reduced to the number of weeks when all 31 stocks had been traded and recorded. At most, this was the number of weeks for the stock that had the
minimum in its group and it was generally somewhat less. In fact, realizing in
advance that some groups might be reduced to a very low number of coincidental observations, I decided to discard a stock if keeping it in the group
meant reducing the second number of degrees of freedom, N -
k + 1, below
30. When a stock was discarded, the next alphabetical one on the' tape was
added to the group. Of course this meant that a stock was then missing from
the subsequent group and another had to be taken from the group following
that and similarly to the end of the tape. Finally, 68 groups of 31 stocks remained for analysis and this number comprises all the stocks on the tape with
sufficient coincidental observations for the test procedure. These 68 F statistics
are depicted in Figure 1 and tabulated in Table 1.
The distribution of Figure 1 is stochastically below the expected null distribution. For example, using a Chi-square goodness-of-fit test with 17 classes to
compare the F sampling distribution with the null distribution, the test statistic
is about 70, which is far above the .005 level of significant difference between
the two distributions. It should be emphasized, however, that only high F values
reject the null growth-optimum hypothesis. Thus, growth-optimum theory is
strongly, even too strongly, supported by this test of its basic validity.'
5. As further cxplanation, recall that Zj.t == (1 + Rj.t)/(l + Rm.t) is the ratio of return on
stock j to the market return. For a given group of 31 stocks, the differences in return ratios are
calculated as Yj,t == Zj,t -
Zj+1.I for j = I, . . , ,30. The means of Yj,t and covariances of yj,t
and Yu are then calculated ovcr time. Hotelling's statistic is based on the sample quadratic form
9'S-I}' where 5' is the vector of sample mean differences and 5 is the sample covariance matrix
of differences. Differences were calculated between adjacent alphabetic pairs but any other random
scheme for selecting pairs would have been equally acceptable. Cf. Morrison [1967, pp. 135-1381.
6. This is the rationa1e for using a group size of 31 stocks: since the number of degrees of
freedom for the test is k-l, where k is the number of stocks, a group size of 31 is both large
and makes tabular comparison easy. If the group size had been chosen larger, the second degrees
of freedom parameter, N-k+l, (where N is the number of available time points), would be reduced
to a low number. Thus, I thought k=31 would balance the two d.f. parameters and still leave
them quite large.
7. Because the Hotelling test supports the null hypothesis too strongly, I decided to check several
potential causes, One obvious possibility is the thick-tailed distributions of stock returns that hnc
been pointed out by many researchers, (Cf. Fama [19651, Blume r 1970 /), The appropriate way
to check this problem is to use a non-parametric analysis of variance, Friedman's multi-sample
test, (Bradley, r1968, p, 1271) . This was done for exactly the same sample of stocks grouped in
--- page 157 ---

130
556
Frequency
10
8
6
4
2
Computed
F Statistics
The Journal oj Finance
FIGURE 1
F DIstributIon
expected under
null hypothesis
R. Roll
Distribution of F Statistics from Hotelling's T2 Test of Equality Among Mean Return Ratios
IV.
RELATIONS BETWEEN THE GROWTH-OPTIMUM AND THE SHARPE-LINTNER
MODELS
A.
Theory
When one compares the first order conditions for the growth-optimum model
1 + RJ
1
E
;(
= (1 + Rr). E
R ; j = 1, .. . N -
1
I+Km
1+ m
(5)
with those for the Sharpe [1964]-Lintner [1965] model
E(1 + RJ)
(1 + Rr)
E(l + Rm} = ~J + (l -
~J) E( 1 + Rm)
j = 1, ... ,N -
1
(6)
(where ~j = Cov (R" ~m) jVar (Rul)), some correspondence appears but it is
rather difficult to evaluate fully just by inspection. For example, when the
Sharpe-Lintner risk coefficient, ~j, is equal to zero, equation (6) becomes
E(1 + Rj )
1 + Rr
E(l + Rm}
E(1 + Rm}
But when ~j = 0, COy (R), RnJ = 0, and the growth optimum condition expressed in equation (5) becomes
the same way. The results were identical to those obtained by using HotelUng's T2, the growthoptimum model was too strongly supported.
A second possible misspecification is a deficiency in the market price index. The Standard &
Poor's Composite Price Index, used in the preceding tests, is heavily-weighted in favor of a few
stocks. Also, since it is essentially a "buy-and-hold" portfolio, weights of individual stocks change
over time as relative prices change. Evans [1968] and Cheng and Deets [1971 J have provided
empirical evidence that such an index performs Quite differently from 'a "fixed-investment proportion" or "rebalanced" index. Therefore, a rebalanced index composed of stocks on the tape was
constructed and used in reporting the tests already done. Again, no difference was detected.
Thirdly, the possibility that an unrepresentative episode biased the entire sample period of seven
years of weekly observations was checked by repeating the tests for annual sub-periods. There was
no perceptible difference among the sub-periods or between the overall period and any sub-period.
In every case the growth-optimum model was strongly supported.
Further details of all the tests in this footnote are available in an earlier working paper. (It was
edited to conserve Journal space.)
--- page 158 ---

Evidence on the "Growth-Optimum " Model
131
Growth Optimum Model
557
TABLE 1
CALCULATED VALUES OF HOTELLlNC'S T2 STATISTIC FROM COMMON STOCK
MEAN RETURN RATIOS, 1962·1969
Sample size
Sample size
Group
(weeks)
T2
Group
(weeks)
1'2
1
113
36.0
36
98
30.8
2
81
20.2
37
76
35.0
3
61
53.3
38
101
29.2
4
61
45.4
39
79
54.1
5
143
28.4
40
69
56.3
6
76
35.3
41
107
32.3
7
132
55.5
42
61
6S.9
8
61
14.4
43
61
72.0
9
148
29.7
44
78
32.0
10
131
24.1
45
64
35.9
11
90
22.6
46
97
46.3
12
68
28.7
47
66
56.9
13
lOS
41.3
48
62
57.1
14
76
27.5
49
91
24.9
15
109
41.5
50
60
50.1
16
273
29.4
51
61
37.6
17
III
33.5
52
64
40.3
IS
110
35.0
53
63
38.3
19
175
36.5
54
65
25.6
20
75
42.0
55
60
35.1
21
95
27.9
56
67
63.S
22
76
51.3
57
80
4S.2
23
112
22.4
58
60
107.0
24
74
64.5
S9
96
24.9
25
11 2
23.4
60
79
39.0
26
127
31.8
61
73
57.8
27
158
38.6
62
82
56.2
28
78
23.0
63
72
28.5
29
123
39.6
64
66
65.7
30
112
40.2
65
61
47.3
31
104
49.7
66
65
53.5
32
61
32.3
67
75
42.3
33
115
35.2
68
63
52.9
34
62
65.6
Note: The F statistic is calculated as
35
70
30.6
N -30
T2.
(N -
1) 30
E(l + RJ) E ( 1
+Rm ) = (I + Rr) E ( 1; Rm ).
Since the terms containing market returns cancel in both of the displayed
equations just above, the growth optimum model provides a market diversification result which is well-known from Sharpe-Lintner theory; namely, a security
whose portfolio risk is zero will sell at an expected return equal to the riskless
rate.
--- page 159 ---

132
R.Roll
558
The Journal 0/ Finance
Stock B
Stock A
1 + Rm
o
FIG1.1RE 2
Stocks Satisfying the Growth-Optimum Model with Different Degrees of Market Response
It is not true that the growth-optimum model implies a constant ~ coefficient
although it may seem to after a first glance at equation (6) ,8 A simple example
is sufficient to show the contrary, Figure 2 illustrates the discrete probability
8, Because (6) is
and (5) is
EO + Rj )
E(l + Rm)
1 + RF
[
----+~j 1
E(l + Rm)
(
1 + Rj
)
(
1 + RF )
E
;(
=E
_
,
1 + J(.m
1 + Rill
a reader not cautious about quotients and reciprocals of random variables mi~ht think that the
latter model implies ~j = zero, independent of j.
--- page 160 ---

Evidence on the "Growth-Optimum " Model
133
Growth Optimum Model
559
distributions of stocks A and B and of the market. In this example, only four
equally likely returns are possible for the market and each stock can return
corresponding amounts to those four. The growth-optimum model requires that
( 1 + RA ) _ (1 + RJl )
E
""
_E
""
1 + Rm
1 + Rm
which in geometric terms implies that the expected slopes of rays from the
origin through each possible point in the 1 + RJ, 1 + Rno plane is equal for both
stocks. This is clearly satisfied by the radially symmetric solid lines which
pass through the points of possible occurrence in Figure 2 . Nevertheless, the
slopes of regression lines of RJ on Rm, indicated by dashes, are quite different.
Stock A has low portfolio risk because its ~ is low, while stock B has much
greater response to the market and thus higher risk. Both securities' returns
are perfectly functionally related to the market return but it is already apparent
that correlation per se will have the same relatively unimportant role in a
growth-optimum as it has in the Sharpe-Lintner framework (i.e., the expected
slopes of rays can be equal no matter what correlation occurs between a stock's
return and the market's).
A close correspondence between the two models can be made more apparent by rearranging a few terms. The result (derived in the footnote9 ), is
E(RJ -
RF ) = [ COY ( Rj,
1..,
) / COY ( Rm,
1",) ] E(Rm -
RF );
•
1 + Rm
1 + Rno
(7)
which is very similar indeed to the Sharpe-Lintner equilibrium equation. In
fact, since Cov (Rm'
1,.,,) is negative, one is tempted to suggest that
1 + Rno
a second implication of Sharpe-Lintner theory is also satisfied by the growthoptimum model: namely, that security j's expected return will exceed the
riskless return if and only if Cov (RJ' Rm) is positive. One would need to prove,
9. To obtain (7) , note that equation (5) is equivalent to
CovlRj , I/ (l + Rill) 1 = (I + R~.)K -
EO + Rj)K
where K ;: Ef I/(l + Rm)l.
( Sa)
Multiplying both sides of (Sa) by Xj' the proportion of wealth invested in security j, (or the
fraction of aggregate economic wealth represented by security j),
Covfl:XJRj , I/O + Rill) J = -K l: fXjEdtJ -
R .. ) J
J
J
and substituting for the definition of Rill' i.e., for Rm ;: RF + l:XJ(RJ -
RF),
CovlRm -
RF(l -l: XJ)' 1/ (1 + Rm) 1 = -K E(Rm -
R I._).
j
Since RF(l-l:x) is a constant,
K = -Cov[Rm, 1/ (1 + Rill) ]/ E(Rm -
Rt,) .
Substituting this for K in (Sa) provides equation (7).
--- page 161 ---

134
R. Roll
560
The Journal of Finance
however, that Cov (Rj , Rm) > 0 implies Cov (Rj , __
1~_) < 0 and this
1 + Rm
is definitely not true in general. Counterexamples can be displayed for highlyskewed distributions.1o
B.
Testing Sharpe-Lintner vs. Growth-Optimum
The two models will provide approximately equivalent empirical implications
if certain restrictions are placed on the ranges of individual rates of return. To
verify this, one only needs to note the following facts: (a) quadratic utility
functions and homogenous anticipations will lead to the Sharpe-Lintner equilibrium result of equation (6) and (b) the logarithmic utility function implied
by portfolio growth maximization can be approximated by a quadratic as
log (1 + RT ) .... RT -
1/2 RT2
provided that the portfolio's total return is restricted to less than 100 per cent
per periodY It is indeed trivial to show that the two models are identical when
this approximation to the logarithm is made. Thus, given the truth of one
theory, we should not be surprised to find that an empirical test of the other
supports it very well, especially when the observed rates of return used in testing fall predominantly near zero. Of course, this leads us to ask whether the
strong empirical support for the growth-optimum model reported in the preceding section is really damnation for Sharpe-Lintner or just an accidental
stroke of choosing a short time interval (one week) which guaranteed that
returns were never observed far from zero.
An obvious way to test this is suggested by the logarithmic approximation.
If growth-optimum theory appears to satisfy the data only because the logarithm approximates a quadratic when returns are near zero, one should choose a
longer time interval for empirical testing so that many more large and small
returns are observed.l2 This was done for both four week and twenty-six week
periods with the same common stock data as used previously and the conclusions were identical to those for weekly periods already reported.
A more refined and direct test to discriminate between the two models can be
based on equilibrium conditions of the two competing theories,
E(RJ - RF ) = {cov [RJ'
1..., JI
1 + Rm
COY [ Rm,
1 R J} E(Rm -
Rd = Yj
(8)
1 +
m
10. However, for at least one special asymmetric case, (lognormal distributions) the growthoptimum model does agree completely with the Sharpe-Lintner result that a security's expected
return will be a linear function of systematic risk i i.e., of /iJ' I am indebted to Robert Litzenberger
for demonstrating this point.
11. And more than minus 100 per cent per period. Without short sales, this last restriction is
presumably satisfied for common stocks by the elristence of limited liability. Samuelson [1970) has
derived a broader "fundamental approximation theorem" which shows the close match of meanvariance to any correct portfolio theory when the joint distribution of returns has a small dispersion.
12. This completely ignores the crucial question of investor horizon period that may have a significant effect on the form of the Sharpe-Lintner market model. Cf. Jensen [1969, pp. 186-191 J.
--- page 162 ---

Evidence on the "Growth-Optimum " Model
135
Growth Optimum Model
561
which is the growth-optimum condition (7), and
E(Rj -
R F ) = {COy [Rj, RmllVar (Rm)} E(~m -
R F ) == bj
(9)
which is the familiar Sharpe-Lintner condition. A suggested test procedure
obtains the best estimates of all components of (8) and (9) from time series
and then performs cross-sectional regression with those estimates.
A series of comparative tests of these two equations was conducted with the
common stock returns mentioned previously. In each case, time series were used
to calculate Rj , the mean return, and ?j or ~J' the estimated risk measures implied by the growth-optimum or the Sharpe-Lintner model, respectively.13
Then, cross-sectional computations were performed for the regression models
Rj = 30 + a;~J
(10)
and
(II)
Estimated coefficients from (10) and (11) should be compared to their theoretical counterparts: depending on which theory is correct, ~ or bo should equal
RF, the average risk-free interest rate, and ~I or 1)1 should equal unity.
In the first test, all calculations were carried out with individual security
returns during the same time periodY For example, 1192 separate values of
R, ~, and t were obtained from weekly data covering the annual sub-period
July, 1962 through June, 1963. Cross-sectional regressions using these 1192
estimates gave fto = 20.1 and 1)11 = 20.3 per cent. The value of RF , as measured
by the weekly average interest rate on short-term government debt obligations
during the year, was only 3.27 per cent; so neither model satisfied its theoretical prediction very well in this particular annual sub-period.15 OVer all the
seven years of available data, the estimated values of ~1 and bl were very significantly positive and they were scattered around unity in nice accord with
their expected level. fto and 1)0 were also reasonably close to RF, at least on
average. As a distinguishing test of the two competing theories, however, these
results failed miserably; for the estimates were very highly correlated between
the models. The two competitive intercepts were practically identical in every
13. To be precise,
and
8J == rCSv(RJ,RIlI)/Vir(Rm)J(R", - RF )
where' indicates the sample analog of a population parameter, calculated from weekly observations
over a specified period, and -
indicates sample mean from the same period.
14. To save computation expense, only New York Exchange listed stocks with at least 30 weekly
quotations during a year were included in the sample. The risk-free rate was measured by a weekly
"average of short-term government debt obligations" taken from Standard & Poor's Trade Statistics.
The market indexes used were: The S&P Composite Index and a rebalanced index constructed by
weighting all NYSE Stock Returns equally each week. The results were very similar but only tbe
results ' for the rebalanced index are quoted in the text.
IS. To save space, only one annual sub-period is reported here but all the results are available
from the author upon request.
--- page 163 ---

136
R.Roll
562
The Journal oj Finance
period as were the two competitive slope coefficients. They deviated much more
from theoretical predictions than from each other.
In order to sharpen the discriminatory resolution of the data, a different
procedure1G was necessary. The first problem to be alleviated was an extremely
low explanatory power which was indicated by low R2's (on the order of .05),
for the cross-sectional models with individual stock returns. A technique to
remedy this is to form portfolios of stocks and conduct cross-sectional tests on
portfolios rather than on individual securities. A difficulty arises, however, because randomly-selected portfolios would have very similar values of the risk
measures t:t and l To create a cross-sectional spread in risk measures, portfolios
~ust be selected on the basis of risk by grouping stocks with the lowest 1"s or
6's in one portfolio, stocks with higher ?'s or fI's in the next portfolio, and so
on.
This procedure for forming portfolios makes another econometric problem
obvious: In the cross-sectional regression, the explanatory variables contain
errors which will tend to bias slope coefficient estimates toward zeroY To
alleviate this problem somewhat, stocks were placed in portfolios based on their
risk measures calculated from weekly data of a given year and then the mean
portfolio return and risk measures for the portfolio as a whole were calculated
from weekly data in the subsequent year. Cross-sectional models (10) and (11)
were then estimated using these latter estimates and the results are given in
Table 2 and Figure 3. To recapitulate, the procedure which resulted in the
output of Table 2 and Figure 3 was as follows:
l. For each stock (j) in year t, the total risk premia ?J and 8J were calculated from the time series of year t using the rebalanced market index
(see note 7).
2. Stocks were ranked from smallest to largest ?J and from smallest to
largest ~J'
3. Twenty portfolios were selected by assigning the lowest five per cent of
ranked stocks to one portfolio, the next lowest five per cent to a second
portfolio, etc. Thus, two sets of 20 portfolios each were formed; one set
based on y rankings and. one set on b rankings.
4. Each portfolio's mean return, R-p, was calculated from time series in year
t + 1. For each portfolio that had been formed on the basis of y rankings,
the growth-optimum risk premium ~II was calculated from year t + 1
data. Similarly, the Sharpe-Lintner premium 8p was calculated from year
t + 1 data for each portfolio that had been formed by ?) rankings.
5. For each of six years (1963-64, 1964-65, ... 1968-69), these calculated
portfolio mean returns and risk measures are plotted in Figure 3 and
regressions across portfolios are reported in Table 2.
In Figure 3, the scatters of mean portfolio returns versus the two competing risk measures are displayed for six different years. The solid lines mark
16. Blume [1970] I Miller and Scholes {i9721, Black, Jensen, and SchQles [19721. and Farna
and MacBeth [1972], have originated and developed the procedures used here in their work with
the empirical validity of the two· parameter portfolio model.
17. This is true, of course, for regressions using individual stocks as well as for those usinl1
portfolios.
--- page 164 ---

TABLE 2
RELATIONS BETWEEN AVERAGE RETURNS AND RISK COEFFICIENTS OF 20 PORTFOLIOS SELECTED ON THE BASIS
OF INDIVIDUAL RISK COEFFICIENTS CALCULATED ONE PERIOD EARLIER
(Rebalanced Index)
Growth Optimum Model
Sharpe-Lintner Model
Period
RFe
3.0
to
Size of
(July through
% per
% per
% per
tId
Portfolio"
June) a
annum
Rm
annum
aId
R2
annum
R2
(No. of Stocks)
1963-1964
3.71
14.4
15.8
- .0817
.0077
15.S
-.0781
.0065
59
(6.29)
(-.374)
~6.05)
(.343)
1964-1965
3.81
12.6
12.4
.0195
.0005
12.5
.00604
.0001
58
(6.53)
(.0918)
(6.90)
(.0297)
1965-1966
4.34
21.0
-9.91
1.85
.940
-9.6S
1.83
.951
62
( -5.14)
(I6.S)
( -5.62)
(IS.6)
1966-1967
4.61
29.4
-2.72
1.27
.896
-3.02
1.28
.895
63
( -1.04)
(}2.5)
( -1.14)
(12.4)
1967-1968
5.1S
29.2
21.7
.261
.247
22.2
.241
.172
62
(S.20)
(2.43)
(7.23 )
(1.93)
1968-1969
5.36
-2AS
13.3
1.97
.500
13.2
1.96
.537
59
(3.55)
( 4.24)
(3.84)
(4.57)
a The last date in 1969 was July 11. In other years the first date was the first Thuxsday in July, 196X, and the last date was the last Thursday in June,
196(X + 1).
b t-ratios are in parentheses .
., This is equal to the total numher of stocks that have at least 30 available prices in periods t -
1 and t, N, divided by 20. The remainder from N/20,
J = MOD(N,20), was distributed such that one extra stock was included in each of the fixst ' J portfolios.
d Means of sample values al = .881; t1 = .873; RF = 4.50; ao = 8.43; to = 8.50.
e Mean of weekly observations of short-term government debt obligations, Standard and Poor's Tratk Statistics.
C)
~
<;)
~
....
~
a
~
.... ...
;!
;:
;!
~
<;)
~
'"
.....
""
0-
c...
~
~
;:
" '"
<::> ;:
;;.:.
'" Q
c; :;
;;.:.
~
§'.
:::: ;:
"
~
~
W
-.J
--- page 165 ---

138
564
" "
'"
1:
z
· "'.
c"
~o .
... .
,
•
.....
c- · .
.. ..
wb.oo
'.00
I . 00
RISK . (S-U. 1963-6ij
g
i
•
z
~g
., .
a
.....
aa
lI!-
~ • '.
• •
•
0 ..
'11. 00
'.00
1' . 00
"15K, (e-Ol, 1963-64
g /
,; ,
z
"'"
=>0
....
......
c ..
•
..
~;:I.~oo:--"""'~::-"""'~"".-:oo-:-
"15K.
1966-67
"
D
~ / .. '.
. .
•
g""",,-....,,.,...,-:---.,.,::--::,-
~ . oo
2 .00
~0.00
"ISK. (C-Ol. 1966-67
The Journal oj Finance
,.
" " .. . ...
. .
z "'0
..
~"
... .
w"
c- . •
" "
~.oo
RISK.
g
:2
z
•
"'"
"\,
=>0
.....
w"
",-
0 " "i.. 00
"15K.
o
D
::
z c"
=> ..
... .
.... ..
",'"
'.00
(S-LJ •
• •
• .
•
'.00
((;-01.
IS . 00
196~-65
12.00
1964-65
..
g
";:+""'-+--:0:-::-:----.--
'
. 00
00.00
"IS •
1967-68
FIGURE 3
" " " "
z c
=>"
..."
~o •
;
le.oo
RISK.
g
g
z
'"
=>0
"'0
~o •
"
0
" .. le.oo
" " " ..
RISK.
R. Roll
11.00
26.00
(S-LI • 1965-66
16. 00
11. 00
(C-O) • 1965-66
z
'"
~:
.. ~
~.
g
~+-L-_~ ___ _
'_15.00
- 10.00
-5.00
RISK.
(S-L). 1968-69
g
~+-------:--~-
1. 13 . 00
·a.oo
·S.GO
RISK,
IC-OI. 1968-69
Mean Portfolio Returns and Estimated Portfolio Risk Premia, New York Exchange Stocks,
1962-1969, Rebalanced Index
* (S-L) Denotes Sharpe-Lintner Risk Premia and (G-O) denotes Growth-Optimum Premia.
the theoretical predictions, an intercept of RF and a slope of unity.ls Table 2
contains results from cross-sectional models (10) and (11) applied to these
data.
On average across the six years, both the growth-optimum and the Sharpe-
Lintner model seem to have excessive intercepts, (~I' bo > RF), and deficient
slopes, (il' bl < 1). The averages are given in footnote d of Table 2. These
deviations from the anticipated can no doubt be attributed, at least in part,
18. Since the axes are scaled differently in each plot, the lines do not appear to have slopes of
unity upon first examination. Note that the plotted lines are the theoretical predictions and are
not the regression lines reported in Table 2.
--- page 166 ---

Evidence on the "Growth-Optimum" Model
139
Growth Optimum Model
565
to errors in the measurement of risk premia. In the first two years and in
year 5 (1967 -68) the wide scatter suggests that either the mean portfolio
returns or the risk premia were measured inaccurately.
In the two years of best fit, 1965-66 and 1966-67, portfolios with low risk
premia return less than anticipated while portfolios with high premia return
more. This is unlikely to be just a sampling phenomena if the standard errors
of al and bl are credible. For example, the growth-optimum slope for 1965-66
is al = 1.85 which is nearly eight standard errors above unity.19
Perhaps the most striking characteristic of the two models is their very
close relation over time. The slope coefficients and intercepts given in Table
2 vary widely across periods but are extremely close, between the two models,
in each period. This is obvious from even a quick look at Figure 3.20 Based on
these results, one can only conclude that the two models are empirically
identical. A qualification is in order, of course; assets whose returns are much
more highly skewed (e.g., warrants), may permit a finer discriminatory test.
V.
SUMMARY AND CONCLUSIONS
If investors wish to maximize the probability of achieving a given level of
wealth within a fixed time, they should choose the "growth-optimum" portfolio; that is, the portfolio with highest expected rate of increase in value.
This paper has examined the implications for observed common stock returns
of all investors selecting such a portfolio.
Given some widely-used (and useful) aggregation assumptions, the growthoptimum model implies that the expected return ratio E[(l + RJ)/(1 + Rm)]
is equal for all securities.21 This implied equality of expected return ratios
was utilized in analysis of variance tests with New York and American Exchange listed stocks from 1962-1969 in order to ascertain the basic validity
of the growth-optimum model. The model was well-supported by the data.
The growth-optimum model was compared algebraically to Sharpe-Lintner
theory, which is probably the most widely-used portfolio result in empirical
work. A close correspondence was demonstrated between their qualitative implications. For example, both models imply that an asset's expected return
will equal the risk-free interest rate if the covariance between the asset's return
and the average return on all assets, Cov(~J' Rm), is zero. For most cases,
the growth-optimum model also shares the Sharpe-Lintner implication that an
asset's expected return will exceed the risk-free rate if and only if Cov (RJ' Rm)
> O. There are, however, some cases of highly-skewed probability distributions
where this implication does not follow for the growth-optimum model.
A close empirical correspondence between the two models was demonstrated
for common stock returns. The procedure (1) estimated returns and risk premia
19. For a more detailed discussion of this point, see Friend and Blume [1970],
20. The greatest difference between '3.1 and £1 is .02 which is only about 2.3 per cent of their
average value. Between 10 'So, the greatest difference is about six per cent of their average value .
.'\ close connection between the two models was previously implied by the work of Young and
Trent [1969], They showed that the geometric mean of portfolio returns was closely approximated
by functions of the arithmetic m~an and variance of returns. These functions were developed as
approximations to the geometric mean. For accuracy, they require a minimal amount of skewness
and are, therefore, analogous to the truncated (after two terms), Taylor series expansions of
log. (l+R) .
21. RJ is the rate of return on security j and Rm is the rate of return on a portfolio of all assets.
--- page 167 ---

140
R.Roll
566
The Journal of Finance
implied by the two models from time series; (2) calculated cross-sectional
relations between estimated returns and risks; and (3) compared the crosssectional relations to the theoretical predictions of the two models. They could
not be distinguished on an empirical basis. In every period, estimated corresponding coefficients of the two models were nearly equal; and indeed, they
deviated much further from their theoretically anticipated levels than they
deviated from each other.
REFERENCES
Fischer Black, Michael C. Jensen, and Myron Scholes. "The Capital Asset Pricing Model: Some
Empirical Tests," in Jensen, ed., [1972].
Marshall E. Blume. "Portfolio Theory : A Step Towards Its Practical Application," Journal 0/
Business, 43, (April, 1970), 152-173.
James V. Bradley. Distribfltion-/ree Statistical Tests, (Englewood Cliffs, :-;;.J.: Prentice-Hall), 1968.
Leo Breiman. "Investment Policies for Expanding Businesses Optimal in a Lonl!:-Run Sense," Saval
Research Logistics Quarterly, 7, (December, 1960), 647-651.
L. Breiman. "Optimal Gambling Systems for Favorable Games," Proceedings 0/ the Fourth Berkeley
Symposium on Mathematical Statistics and Probability, I (Berkeley. University of California
Press), 1961, 65-78.
Pao L. Cheng and M. King Deets. "Portfolio Returns and the Random Walk Theory," Journal 0/
Finance, 26 (March, 1971), 11-30.
John L. Evans. "The Random Walk Hypothesis, Portfolio Analysis and the Buy-and-Hold Criterion," Journal 0/ Financial and Quantitative Analysis, 3 (September, 1968), 327-342 .
Eugene F. Fama and James MacBeth. "Risk, Return and Equilibrium: Empirical Tests," (Workin!(
paper, University of Chicago, Graduate School of Business, February, 1972).
Eugene F. Fama. "The Behavior of Stock Market Prices," Journal 0/ Bllsiness, 38 (January, 1965),
34-105.
Irwin Friend and Marshall Blume. "Measurement of Portfolio Performance Under Uncertainty,"
American Economic Review, 60, (September, 1970), 561-575.
Franklin A. Graybill. An Introduction to Linear Statistical Models, Vol. I, (:-;;ew York: McGraw-
HilI,1961).
Nils H. Hakansson. "Capital Growth and the Mean-Variance Approach to Portfolio Selection,"
Journal 0/ Financial and Quantitative Analysis, VI (January, 1971), 517-557.
Nils H. Hakansson and Tien-Ching Liu. "Optimal Growth Portfolios When Yields are Serially
Correlated," Review 0/ Economics and Statistics, 52 (November, 1970), .185-394.
Michael C. Jensen, ed., Studies in The Theory 0/ Capital Markets, (:-':ew York, Praeger Publishing
Co., 1972).
Michael C. Jensen. "Risk, The Pricing of Capital Assets, and the Evaluation of Investment Portfolios," Journal 0/ Business, LXII (April, 1969), 167-247.
Benjamin F. King. "Market and Industry Factors in Stock Price Behavior," Journal 0/ Bllsiness,
39 (January, 1966 supp.), 131}-190.
.
Henry Allen Latane. "Criteria for Choice Among Risky Ventures," Journal 0/ Political Economy,
67 (April, 1959), 144-155 .
John Lintner. "The Valuation of Risk Assets and the Selection of Risky Investments in Stock
Portfolios and Capital Budgets," Review 0/ Economics and Statistics, 47 (February, 1965),
13-37.
Harry M. Markowitz. Port/olio Selection : Efficient Diversification 0/ investments, (New York:
John Wiley & Sons, Inc.), 1959.
Merton H. Miller and Myron Scholes. "Rates of Return in Relation to Risk: A Re-examination of
Some Recent Findings," in Jensen, ed., (1972).
Donald F. Morrison. Multivariate Statistical Methods, (New York: McGraw-Hili, 1967) .
A. D. Roy. "Safety First and the Holding of Assets," Econometrica, 20 (July, 1952), 431-449.
P. A. Samuelson. "The Fundamental Approximation Theorem of Portfoli(l Analysis in Terms of
Means, Variances and Higher Moments," Review 0/ Economic Stlldies, 37 (October, 1970) ,
537-542.
William F. Sharpe. "Capital Asset Prices: A Theory of Market Equilibrium Under Conditions of
Risk," Journal 0/ Finance, 19 <September, 1964),425-442.
J. Tobin. "Liquidity Preference as Behavior Toward Risk," Review 0/ Economic Studies, 26
(February, 1958), 65-86.
William E. Young and Robert H. Trent. "Geometric Mean Approximations of Individual Seruritv
and Portfolio Performance," Journal 0/ Financial and Quantitative Analysis 4 <June 1969i
179-199.
'
,
,
--- page 168 ---

Part II
Classic papers and theories
--- page 169 ---

This page is intentionally left blank
--- page 170 ---

143
11
Introduction to the Classic Papers and Theories
In this part of the book, we present papers that formalize, generalize, and extend
the early results on the Kelly strategy. Although the early papers on the Kelly
optimal growth strategy contained powerful results, the topic was not significant
in mainstream financial economics. Unfortunately, despite lots of good evidence,
it is still not a serious part of academic financial economics. Roll (1973), for example, shows that in his data set, capital growth and mean-variance portfolios are
similar. Thorp (1971) had shown that the Kelly strategies were not necessarily
mean-variance efficient and Markowitz (1976) argued that the Kelly strategy was
the limiting mean-variance portfolio. These papers appear later in this book. Here
we take up the work of those who extended the early results and begin to consider
the good and bad properties of these strategies and the sensitivity of the results to
data inputs and errors.
Bell and Cover (1980) consider the static one period behavior of two investors.
They each can allocate among m stocks and have one dollar to invest. The winner
has the most money after one period's returns of the portfolio. They show that the
optimal one period policy is an appropriately randomized version uA * of the Kelly
growth rate optimal portfolio A *. Then for any other portfolio A, Pr{W(A) ~
W (uA *} ~ ~. So this establishes a good short run property in addition to the
previously known good long term asymptotic Kelly criterion properties. In part IV,
we review the good and bad properties of the E log Kelly capital growth criterion.
Algoet and Cover (1988) generalize the classic Breiman (1961) results to general dependent asset return distributions. Breiman assumed iid asset returns. So
maximizing conditionally expected log in each period t given information up to t
is optimal in that it maximizes the asymptotic growth rate of wealth for arbitrary
asset returns. Algoet and Cover (1988) and Thorp (2006), in part VI, present the
most general Kelly asymptotic optimality properties.
Cover (1991) presents an algorithm and theory for a universal portfolio that will
perform as well as if the investor knew the realized distribution of the future asset
returns. There are no assumption on these asset returns. The universal portfolio
strategy is based on the past returns Xi, ... , Xtl up to the given period t, and will
perform asymptotically as well as the best constant rebalanced portfolio based on
foreknowledge of the sequence of price relatives. The universal portfolio in period
1 is uniform equally weighted over all the stocks, and the portfolio in period t is
the performance weighted average of all constant rebalanced portfolios. Examples
in Cover's paper show the exponential outperformance of the universal portfolio
--- page 171 ---

144
L. C. MacLean, E. 0. Thorp and W. T Ziemba
with respect to the assets used to construct this portfolio, Cover assumes zero
transaction costs,
Ordentlich, E. and T, M, Cover (1998) greatly refine the statements in the 1991
paper and provide exact results for the minimax relative behavior of an investor's
wealth with respect to the wealth of the universal investor.
When one sees the naturalness of growth optimality as a goal in investment and
then finds the natural mathematics behind it (to maximize the geometric mean) ,
it is tempting to think that the optimal strategy, which turns out to be Kelly
gambling or, if you will, log optimal investment, has many other properties as well.
Such correspondences certainly occur in mathematics. For example, numbers like
7r and e occur in hundreds of different contexts and are characterized by the set of
all problems that give 7r and e as answers. 7r and e do not have just one defining
property but many. Looking at it from this point of view, we ask for the properties
of growth optimal investment beyond that of growth optimality itself.
The first question is what are the short run properties of growth optimal investment? Is Kelly also good for just one investment period and if so in what sense?
Bell and Cover (1980) find the strategy that maximizes the probability of outperforming one's opponent during a single investment period. The optimal one period
strategy is to choose a fairly randomized version of the portfolio that maximizes
the expected logarithm of wealth. A generalization of this to other payoff functions appears in Bell and Cover (1988). All of these generalizations are achieved
by randomized version of the log optimal strategy. Logarithms are nowhere in the
statement of the problem. Is this a fortuitous coincidence or is it a property of the
naturalness of the approach?
Next, we turn to Kelly and the value of side information. Kelly proves in his
classic 1956 paper that the mutual information I(X; Y) between a horse race market l X and side information Y gives an increase, 6W = I(X; Y) , in the growth
rate of wealth in repeated investments. This is generalized in Barron and Cover
(1988) to general stock market distributions. The mutual information is always an
upper bound, 6W ~ I, on the increase in the growth rate of wealth, with equality
if and only if the underlying stock market distribution is a horse race market.
A summary of the properties of Kelly gambling and growth optimal investment
is given in Cover and Thomas (2006), Chapter 6 (Gambling and Data Compression)
and Chapter 16 (Portfolio Theory).
Algoet and Cover (1988) use a simple sandwich argument to prove that the time
average of the log wealth converges to a constant with probability one for any ergodic
market. This, then, gives the proof of the famous Shannon MacMillan Breiman
theorem as a special case in which the underlying market is a horse race, that
is, there is one winner from all the entrants. This work also shows the asymptotic
optimality of the investment scheme maximizing the conditional expected logarithm
of wealth given the available past. These results are simplified and summarized in
Cover and Thomas (2006, Chapter 16).
1 By a horse race market we mean a situation where out of N entrants, only one wins.
--- page 172 ---

Introduction to the Classic Papers and Theories
145
The idea of a universal portfolio is to asymptotically achieve the same long-run
growth rate as if one had known ahead of time the realized distribution of the stock
market outcomes. This parallels universal data compression, where one wants a
data compression scheme that works for any source of data, like music or voice or
text, and compresses it to the limit that one could achieve if one knew ahead of time
whether it was music or voice or text. The answer is Yes, there is such a scheme,
and with a negligible cost of learning which washes out over time. Cover (1991) is
the first in the series of three papers. Cover and Ordentlich (1996) and Ordentlich
and Cover (1998) refine the statements in the 1991 paper. The latter gives exact
results for the minimax relative behavior of an investor's wealth with respect to the
wealth of the universal investor.
In summary, Kelly investing and its generalization to expected log optimal investing have good short run as well as long run properties. Furthermore, Wn/W~ is
a martingale, where W~ is the wealth generated by Kelly investing, and Wn is the
wealth generated by any other investment scheme. Moreover, there is an asymptotic equipartition result that says that ~ In W~ converges to W, where W is the
maximum expected log wealth conditioned on the infinite past. These are some of
the natural properties of the Kelly criterion.
Finkelstein and Whitley (1981) generalize the Breiman (1960, 1961) results to
iid assets that are not necessarily discretely distributed as Breiman assumed, but
to arbitrary iid random variables with finite expectations. They then show how
Breiman's basic results can be easily proved. For non iid assets the reader is referred
to Algoet and Cover (1988) and Thorp (2006) in this book.
Chopra and Ziemba (1993) show how sensitive mean-variance optimization portfolios are to errors in the estimates of the input parameters. Mean-variance analysis
assumes that all the means, variances and covariances are constant and known. In
practice, they are estimated. Earlier studies by Kallberg and Ziemba (1981, 1984)
showed that the errors in the means are the most important by far, being about
ten times errors in variances, which are about twice as important as the co-variance
errors. The loss is measured in certainty equivalent terms. Chopra and Ziemba
(1993) refine the analysis and investigate the effect of the investor's risk aversion.
They show that the relative importance of the mean errors increases as the risk
aversion decreases. So instead of a 20 : 2 : 1 ratio of importance its more like 60: 3 : 1
for low risk aversion and for extremely low risk aversion like log, it is well over
100, so the ratio is about 100: 3 : 1. So Kelly bettors must accurately estimate
their parameter values especially the means so as not to get into an overbet situation. Geyer and Ziemba (2008) show in a five year period asset-liability model
that the sensitivity is huge in period 1, low in period 2 and by period 5, essentially
non-existent.
MacLean, Ziemba and Li (2005) consider a dynamic investment problem where
there are upper and lower limits on wealth. Instead of typical rebalancing at discrete
fixed or variable points in time one rebalances when one of the limits is reached.
