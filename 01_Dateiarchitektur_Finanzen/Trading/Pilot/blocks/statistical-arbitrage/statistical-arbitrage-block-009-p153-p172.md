# Statistical Arbitrage_ Algorithmic Trading Insights and -- Karen M_ Sowers; Andrew Pole -- Wiley Finance, 1, 2007 -- Wiley & Sons, Incorporated, John -- isbn13 9780470138441 -- 6b0138550172e24db7f13c932e054fb9 -- An.pdf — pages 153–172

--- page 153 ---

126
STATISTICAL ARBITRAGE
−4
−2
0
2
4
0.4
0.2
0.0
0.4
0.2
0.0
(a) Unit variance normal and Student t5
Student t5
Normal
−6
−4
−2
0
2
4
6
(b) Unit variance normal and unit scale Student t5
FIGURE 7.5
Comparison of normal and Student t distributions
distance from the center. Recall that the variance of the t distribution
is the scale multiplied by dof/(dof −2) where dof denotes the degrees
of freedom; the unit scale t5 distribution has variance 5
3. Thus, the
t5 distribution with scale 3
5 has unit variance and exhibits revealed
reversion (in this sample) of 0.95 ×

3/5 = 0.74, which is smaller
than the value for the standard normal distribution.
These comparisons may be more readily appreciated by looking
at Figure 7.5.
Pure reversion
See the remarks in Example 1.
Example 3
Prices are distributed according to the Cauchy distribution. Since the moments of the Cauchy distribution are not deﬁned,
the measures of expected reversion are also not deﬁned, so this is not
a fruitful example in the present context. Imposing ﬁnite limits—the
truncated Cauchy distribution—is an interesting intellectual exercise,
one that is best pursued under the aegis of an investigation of the t
distribution, since the Cauchy is the t on one degree of freedom.
Example 4
An empirical experiment. Daily closing prices (adjusted
for dividends and stock splits) for stock AA for the period 1987–1990
are shown in Figure 7.6. Obviously, the daily prices are not independent, nor could they reasonably be assumed to be drawn from the
--- page 154 ---

Quantifying Reversion Opportunities
127
25
20
15
30
2
1
−1
−3
3
(a)
870102
871008
880714
890420
900125
901101
(b)
0
200
400
600
800
1,000
FIGURE 7.6
Daily close price for stock AA (adjusted for dividends and stock
splits): (a) actual, (b) standardized for local median and standard deviation
same distribution. These violations can be mitigated somewhat by
locally adjusting the price series for location and spread. Even so, it
is not expected that the 75 percent reversion result will be exhibited:
Serial correlation structure in the data is not addressed for one thing.
The point of interest is just how much reversion actually is exhibited
according to the measures suggested. (An unﬁnished task is apportionment of the departure of empirical results from the theoretical
results to the several assumption violations.)
The daily price series is converted to a standardized series by
subtracting a local estimate of location (mean or median) and dividing
by a similarly local estimate of standard deviation. The local estimates
are based on an exponentially weighted moving average of recent
past data: In this way an operational online procedure is mimicked
(see Chapter 3). Figure 7.6 shows the standardized price series using
an effective window length of 10 business days; the location estimate
is the median. Compare this with Figure 7.8, referred to later, which
shows the price series adjusted for location only.
For the location-adjusted series, not standardized for variance,
the proportion of reversionary moves is 58 percent, considerably less
than the theoretical 75 percent. Note that 0 is used as the median of
the adjusted series. By construction, the median should be close to
zero; more signiﬁcantly, the procedure retains an operational facility
by this choice. A few more experiments, with alternative weighting
--- page 155 ---

128
STATISTICAL ARBITRAGE
schemes using effective window lengths up to 20 business days and
using the local mean in place of the local median for location estimate,
yield similar results: the proportion of reversionary moves being in
the range 55 to 65 percent. The results clearly suggest that one
or more of the theorem assumptions are not satisﬁed by the local
location adjusted series.
Figure 7.7 shows the distribution of price changes (close–previous
close) for those days predicted to be reverting downward and (previous close–close) for those days predicted to be reverting upward. The
price changes are calculated from the raw price series (not median
adjusted) since those are the prices that will determine the outcome of
a betting strategy. Figure 7.7 therefore shows the distribution of raw
proﬁt and loss (P&L) from implementing a betting strategy based on
stock price movement relative to local average price. Panel (a) shows
the distribution of trade P&L for forecast downward reversions from
a price above the local median, panel (b) shows the distribution of
trade P&L for forecast upward reversions from a price below the
local median. Clearly neither direction is, on average, proﬁtable. In
sum, the proﬁt is $−31.95 on 962 trades of the $15–30 stock (there
are 28 days on which the local median adjusted price is 0, and
2 × k = 20 days are dropped from the beginning of the series for
initialization of local median and standard deviation thereof).
(a)
−1.0
−0.5
0.0
0.5
1.0
120
80
40
0
100
50
0
Moves from above median
(b)
−4
−2
0
Negative moves from below median
FIGURE 7.7
Stock AA one-day moves around local median: (a) from above the
median and (b) from below the median
--- page 156 ---

Quantifying Reversion Opportunities
129
(a)
0
200
400
600
800
1,000
(b)
−8
−6
−4
−2
0
2
2
100
0
−4
−8
0
200
FIGURE 7.8
Stock AA local median adjusted close price: (a) time series and (b)
histogram
Figure 7.8 shows the distribution of price minus local median.
Taking this as the distribution in Section 7.2 (with the median therein
becoming zero), the total revealed reversion is $597.79/990 = $0.60
per day. The actual result reported in the preceding paragraph,
$−31.95, shows the extent to which assumption violations (with
unmodeled or poorly modeled structure) impact expected revealed
reversion in this example.
This ‘‘missing structure’’ impact is perhaps more readily appreciated from a pure analysis of the median adjusted series. The revealed
reversion from this series (in contrast to the already reported reversion from the raw price series given signals from the adjusted series) is
$70.17. This means that less than one-eighth of the revealed reversion
from the independent, identically distributed model is recoverable
from the local location adjusted data series. (Outlier removal would
be a pertinent exercise in a study of an actual trading system. In an
operational context, the large outlier situations would be masked by
risk control procedures.) Example 5 attempts to uncover how much
reversion might be lost through local location adjustment.
Figure 7.9 shows the sample autocorrelation and partial autocorrelation estimates: Evidently there is strong 1- and 2-day serial
correlation structure in the locally adjusted series. Undoubtedly that
--- page 157 ---

130
STATISTICAL ARBITRAGE
(a)
0
5
10
15
20
1.0
0.8
0.8
0.6
0.6
0.4
0.4
0.2
0.2
0.0
−0.2
autocorrelation
(b)
partial autocorrelation
FIGURE 7.9
Stock AA: (a) autocorrelations and (b) partial autocorrelations of
local median adjusted close price
accounts for part (most?) of the deviation of actual revealed reversion from the theoretically expected value under the assumption of
independence.
Pure reversion
For the record, total pure reversion in the median
adjusted price series (from the actual time series, since we do not yet
have a closed-form result to apply to the price-move distributions,
although we do know that it must exceed the sample estimate of the
theoretical value of revealed reversion or $597.79) is $191.44 on 562
days. Pure reversion from the raw price series (using signals from the
adjusted series) is just 60 percent of this at $117.74.
Example 5
This is an extended analysis of the data used in Example 1. In Example 4, the operational procedure of local median
--- page 158 ---

Quantifying Reversion Opportunities
131
(a)
−4
−2
0
2
150
50
0
2
0
−2
(b)
0
200
400
600
800
1,000
FIGURE 7.10
Random price series, local median analogs of Figure 7.2:
(a) histogram and (b) time series
adjustment was introduced as a pragmatic way of applying the 75
percent result to real, but nonstationary, data series. It is of interest
to understand the implications of the operational procedure for a
series that is actually stationary. Such knowledge will help determine
the relative impact of empirical adjustment for location against other
assumption violations such as serial correlation.
Figures 7.10 to 7.12 are local median adjusted versions of Figures
7.2 to 7.4. (The local median is calculated from a window of the
preceding 10 data points.) The summary statistics, with values from
the original analysis in Example 1 in parentheses, are: 77 percent
(74 percent) of reversionary moves; total pure reversion = 900(952);
total revealed reversion = 753(794).
The analysis depicted in Figures 7.13 to 7.15 is perhaps more
pertinent. The median adjusted series determines when a point is
above or below the local median but, in contrast to the case reported
in the preceding paragraph, the raw, unadjusted series is used to
calculate the amount of reversion. This is the situation that would
be obtained in practice. Signals may be generated by whatever model
one chooses, but actual market prices determine the trading result.
Interestingly, pure reversion increases to 906—but this value is still
--- page 159 ---

(a)
−2
0
2
4
100
50
0
Moves from above median
(b)
−2
−1
0
1
2
3
4
100
60
20
0
Negative moves from below median
FIGURE 7.11
Random price series, local median analogs of Figure 7.3: (a) moves
from the median and above the median (b) moves from below the median
(a)
0
1
2
3
4
Moves down from above median
80
60
40
20
0
(b)
0
1
2
3
4
Negative moves up from below median
100
60
20
0
FIGURE 7.12
Random price series, local median analogs of Figure 7.4: (a) moves
from above the median and (b) moves from below the medium
132
--- page 160 ---

Quantifying Reversion Opportunities
133
(a)
−4
−2
0
2
150
50
0
2
0
−2
(b)
0
200
400
600
800
1,000
FIGURE 7.13
Random price series, signals from local median adjusted series with
reversion from raw series: (a) histogram and (b) time series
(a)
−2
0
2
4
120
80
40
0
Moves from above median
(b)
−2
0
2
4
60
20
0
Negative moves from below median
FIGURE 7.14
Random price series, signals from local median adjusted series with
reversion from raw series: (a) moves from above median and (b) moves from below
median
well below the unadjusted series result of 952. Revealed reversion
decreases to 733.
Figure 7.15 is interesting. Notice that there are negative ‘‘moves
down from above the median’’ which is logically impossible! This
reﬂects the fact that the signals are calculated from the local median
--- page 161 ---

134
STATISTICAL ARBITRAGE
(a)
0
1
2
2
3
4
1
0
3
4
40
20
0
60
Moves down from above median
(b)
0
60
20
Negative moves up from below median
FIGURE 7.15
Random price series, signals from local median adjusted series with
reversion from raw series: (a) moves from above the median and (b) moves from
below the median
adjusted price series, but then moves for those signals are calculated
from the raw, unadjusted series. The relatively few small magnitude,
negative moves is expected. Curiously in this particular sample,
despite the negative contributions to pure reversion, the total actually
increases; that is the result of the more-than-offsetting changes in
magnitude of the positive moves (in the raw series compared with
the standardized series).
Example 6
Prices are distributed according to the lognormal distribution. If log X is normally distributed with mean µ and variance
σ 2, then X has the lognormal distribution with mean µX = exp(µ +
1/2σ 2),
variance
σ 2
X = exp(2µ + σ 2)(exp(σ 2) −1),
and
median
exp(µ). Using results for the truncated lognormal distribution from
Johnson and Kotz, Volume 1, p.129, total expected revealed reversion is:
exp(µ + σ 2/2)[1 −(−σ)]
where (.) denotes the cumulative standard normal distribution
function. Details are given in Appendix 7.1 at the end of this chapter.
Figure 7.16 shows the histogram and time series representation of
a random sample of 1,000 draws from the lognormal distribution
--- page 162 ---

Quantifying Reversion Opportunities
135
(a)
0
10
15
0
200
400
Index
(b)
0
200
400
600
800
1,000
5
0
10
15
5
FIGURE 7.16
Random sample from lognormal distribution (with median
subtracted): (a) histogram and (b) time series
with µ = 0 and σ = 1. (The median, 1, is subtracted to center the
distribution on 0.) The sample value of expected revealed reversion is
1.08 (theoretical value is 1.126). Treating the sample as a time series
in the manner of Example 5, the sample estimate of pure reversion is
1.346.
7.2.3
Movements from Quantiles Other Than
the Median
The analysis thus far has concentrated on all moves conditional
on today’s price being above or below the median. Figure 7.17
shows that, for the normal and Student t distributions, the median
is the sensible focal point. For example, if we consider the subset of
moves when price exceeds the sixtieth percentile (and, by symmetry
here, does not exceed the fortieth percentile), the expected price
change from today to tomorrow is less than the expected value when
considering the larger subset of moves that is obtained when price
exceeds the median.
It is expected that this result will not remain true when serially
correlated series are examined. Trading strategies must also consider
transaction costs, which are not included in the analysis here.
--- page 163 ---

136
STATISTICAL ARBITRAGE
percentile
E[P(t)-P(t+1) | P(t) > pth percentile
50
60
50
40
30
20
10
0
60
70
80
90
100
Student-t3
normal
FIGURE 7.17
Expected pure reversion by conditioning percentile of price
distribution
7.3
NONSTATIONARY PROCESSES:
INHOMOGENEOUS VARIANCE
The very stringent assumptions of the strictly stationary, independent,
identically distributed (iid) process examined in Section 7.2 are
relaxed in this section. Here we generalize the measures of pure
and revealed reversion to the inhomogeneous variance analog of
the iid process. See Chapter 4 for generalization of the ‘‘75 percent
theorem.’’
Prices are supposed to be generated independently each day
from a distribution in a given family of distributions. The family of
distributions is ﬁxed but the particular member from which price is
generated on a given day is uncertain. Members of the family are
distinguished only by the variance. Properties of the realized variance
sequence now determine what can be said about the price series.
7.3.1
Sequentially Structured Variances
Conditional on known, but different, variances, each day a normalized price series could be constructed, then the results of Section
--- page 164 ---

Quantifying Reversion Opportunities
137
7.2 would apply directly to that normalized series. Retrospectively,
it is possible to compare a normalized price series with theoretical
expectations (much as we did in Section 7.3 where normalization
was not required); it is also possible to calculate actual pure and
revealed reversion, of course. However, it is not clear that one can
say anything prospectively and therefore construct a trading rule to
exploit expected reversions.
One possibility is to look at the range of variances exhibited and
any systematic patterns in the day-to-day values. In the extreme case
where it is possible to predict very well the variance tomorrow, a
suitable modiﬁcation of the 75 percent rule and calculation of pure
and revealed reversion is possible. Such calculations would be useful
providing that the same (or, in practice, very similar) circumstances
(variance today versus variance tomorrow) occur often enough to
apply expected values from probability distributions. This may be
a realistic hope as variance clusters frequently characterize ﬁnancial
series: See Chapter 3 for modeling possibilities.
As a particularly simple special case of perfect variance prediction,
suppose that the only variance inhomogeneity in a price series is that
variances on Fridays are always twice the value obtained for the
rest of the week. In this case, there is no need to expend effort
on discovering modiﬁed rules or expected reversion values: The 75
percent rule and calculations of expected pure and revealed reversion
apply for the price series with Fridays omitted. Recall that we are still
assuming independence day to day so that selective deletion from a
price series history does not affect the validity of results. In practice,
serial correlation precludes such a simple solution. Moreover, why
give up Friday trading if, with a little work, a more general solution
may be derived?
7.3.2
Sequentially Unstructured Variances
This is the case analyzed in detail in Chapter 4, Section 3. For
the normal-inverse Gamma example explored there (see Figure
4.2) the expected reversion calculations yield the following. Actual
revealed reversion is 206.81/999 = 0.21 per day; pure reversion is
260.00/999 = 0.26 per day. Notice that the ratio of pure to revealed,
0.26/0.21 = 1.24, is larger than for the normal example (Example
1) in Section 7.3, 0.94/0.8 = 1.18.
--- page 165 ---

138
STATISTICAL ARBITRAGE
7.4
SERIAL CORRELATION
In Section 7.3, the analysis of stock AA (Example 4) showed that the
price series, actually the local median adjusted series, exhibited strong
ﬁrst-order autocorrelation, and weaker but still notable second-order
autocorrelation. We commented that the presence of that serial
correlation was probably largely responsible for the discrepancy
between the theoretical results on expected reversion for iid series
(75 percent) and the actual amount calculated for the (median
adjusted) series (58 percent). The theoretical result is extended for
serial correlation in Section 4 of Chapter 4. We end the chapter here
using the example from Chapter 4.
Example 7
One thousand terms were generated from a ﬁrst-order
autoregressive model with serial correlation parameter r = 0.71 and
normally distributed random terms (see Example 1 in Chapter 4).
Figure 4.4 shows the time plot and the sample marginal distribution.
The proportion of reversionary moves exhibited by the series is
62 percent; total revealed reversion is 315 and total pure reversion
is 601. Ignoring serial correlation and using the sample marginal
(a)
−3
−2
−1
0
1
2
3
0
20
60
100
Moves from above median
(b)
−2
0
2
4
0
20
60
100
 Negative moves from below median
FIGURE 7.18
Analysis of autocorrelated series, Example 7: (a) moves from above
the median and (b) moves from below the median
--- page 166 ---

Quantifying Reversion Opportunities
139
(a)
−4
−2
0
2
0
50
150
Moves from above median
(b)
−2
−1
0
2
4
3
1
40
80
0
Negative moves from below median
FIGURE 7.19
Analysis of autocorrelated model, local median adjusted: (a) moves
from above the median and (b) moves from below the median
distribution to calculate the result in Section 7.2.2, the theoretical
revealed reversion is 592—almost double the actual value. Figure
7.18 illustrates aspects of the analysis.
The local median adjusted series (window length of 10) is shown
in Figure 4.4; aspects of the reversion assessment are illustrated in
Figure 7.19. A slightly greater proportion of reversionary moves
is exhibited by the adjusted series, 65 percent (compared with 62
percent previously noted for the raw series). Total revealed reversion
is 342 (compared to 315 in the unadjusted series); total pure reversion
is 605 (compared to 601).
APPENDIX 7.1: DETAILS OF THE LOGNORMAL CASE
IN EXAMPLE 6
Y = log X ∼N[µY, σ 2
Y]
Set:
E[X] = µX = exp(µY + σ 2
Y/2)
--- page 167 ---

140
STATISTICAL ARBITRAGE
V[X] = σ 2
X = exp(2µY + σ 2
Y)(exp(σ 2
Y) −1)
median = exp(µY)
Deﬁne Z = X truncated at X0 (equivalently, Y is truncated at Y0 =
logX0. Then (Johnson and Kotz, p. 129):
E[Z] = µZ = µX
1 −(U0 −σY)
1 −(U0)
where:
U0 = log X0 −µY
σY
Total expected revealed reversion can be written as E[X|X > m] −
E[X]. Now, E[X|X > m] = E[Z] with X0 = m = exp(µY). In this
case, U0 reduces to 0 and:
µZ = µX
1 −(−σY)
1 −(0)
= 2µX[1 −(−σY)]
Therefore, total expected revealed reversion is:
2µX[1 −(−σY)] −µX = µX[1 −(−σY)]
= exp(µY + σ 2
Y/2)[1 −(−σY)]
Special Case µY = 0, σY = 1. Then µX = √e, σ 2
X = e(e −1), X0 =
median = e0 = 1. Now, U0 = logX0 = 0, so that:
µZ = √e1 −(−1)
1 −(0) = 2√e[1 −(−1)]
From standard statistical tables (see references in Johnson, Kotz,
and Balakrishnan), (−1) = 0.15865 so the mean of the median
truncated lognormal distribution (with µY = 0, σ = 1) is 2.774.
--- page 168 ---

CHAPTER8
Nobel Difﬁculties
Chance favors the prepared mind.
—Louis Pasteur
8.1
INTRODUCTION
I
n this chapter, we examine scenarios that create negative results for
statistical arbitrage plays. When operating an investment strategy,
and notwithstanding risk ﬁlters and stop loss rules, surprises should
be expected to occur with some frequency. The ﬁrst demonstration
examines a single pair that exhibits textbook reversionary behavior
until a fundamental development, a takeover announcement, creates
a breakpoint. Next we discuss the twofold impact of an international
economic development, the credit crisis of 1998: introducing a new
risk factor into the equity market—temporary price discrimination
as a function of credit rating on corporate debt—and turning a
proﬁtable year (to May) into a negative year (to August). Next we
consider how large redemptions from funds such as hedge, mutual,
and pension, create temporary disruptions to stock price dynamics
with deleterious effects on statistical arbitrage performance. Next
we relate the story of Regulation FD. Finally, in all this discussion
of performance trauma we revisit the theme of Chapter 5, clearing
up misunderstandings, speciﬁcally on the matter of correlation of
manager performance in negative return periods.
141
--- page 169 ---

142
STATISTICAL ARBITRAGE
8.2
EVENT RISK
Figure 8.1 shows the price histories (daily close price, adjusted for
stock splits and dividends) for stocks Federal Home Loan Mortgage
Corporation (FRE) and Sunamerica, Inc. (SAI) from January 2, 1996
to March 31, 1998. The two price traces track each other closely
with a strong upward trend, the spread between the two repeatedly
widening and closing.
The analysis and demonstration that follows focuses on pair
spread trading, but the salient points on structural shifts are relevant
more widely to statistical arbitrage models. A factor model forecasting individual stock movements (in groups) is similarly vulnerable
to the described motions, but the mechanics are more involved and
explanation requires greater subtlety of detail. We will keep the analysis simple and remind the reader once more that the basic points are
applicable more generally to statistical arbitrage models.
Daily returns for the two stocks do not correlate particularly
strongly; the correlation is 0.4. However, looking at returns between
events, the correlation is much higher at 0.7. Event correlation
10
20
30
40
50
60
70
19960102
19961231
19971231
19980806
SAI
FRE
FIGURE 8.1
Adjusted price histories for FRE and SAI
--- page 170 ---

Nobel Difﬁculties
143
10
20
30
40
50
60
70
19960102
19961231
19971231
19980806
SAI
FRE
FIGURE 8.2
Adjusted price histories for FRE and SAI to August 1998
indicates what might be expected to trade well in groups within
prescribed risk tolerances (see Chapter 2).
Visually and statistically, it looks as though the pair [FRE, SAI]
will trade proﬁtably in a simple spread reversion model. Simulation
of a basic popcorn process model (see Chapter 2) demonstrates that
was indeed the case.
Figure 8.2 shows the adjusted price series for FRE and SAI
extended through the second quarter of 1998 to August 6. Interesting?
The spread widened considerably to more than double the recent
historical maximum. As already noted, the size of the spread does
not give rise to losing trades, the process of spread widening does.
When a spread begins a persistent period of growth, trades tend to be
unwound (a) after a longer than usual period and (b) when the local
mean spread is substantially different from where it was when the
trade was entered, causing a loss. (This analysis assumes autopilot
application of the forecast model without intervention schemes.
Including monitors and related early exit [stop loss] rules would
attenuate losses but complicate the description without changing the
basic message.)
--- page 171 ---

144
STATISTICAL ARBITRAGE
Using an exponentially weighted moving average model for an
assumed popcorn process with a constrained trend component (see
Chapter 3) trades in [FRE, SAI] entered in late February lasted
through late April, and trades entered in early June lasted through
early July. Both occasions returned substantial losses. (There was a
fast turnaround, proﬁtable trade in late July.)
8.2.1
Will Narrowing Spreads Guarantee Proﬁts?
Sadly, there are no guarantees of proﬁtable scenarios. However, one
beneﬁcial asymmetry of decreasing volatility compared to increasing
volatility is that in the former case the model’s lagged view works to
advantage when the local mean is changing. (Recall that when the
local mean is not changing, changes in volatility are not a problem,
though there may be opportunity costs, in the form of missed proﬁts,
if volatility forecasts are slow to adapt.)
When the spread local mean is persistently moving in one direction in excess of the model’s limited pace of adaptation, the strategy
loses because the trade exit point (zero expected return) is bad relative
to the trade entry. Contemporaneous entry and exit points exhibit
the proper relationship; the problem arises from changes over time
as the spread develops differently from the forecast made at the time
of the trade entry. If the prediction of local volatility is greater than
actual volatility, then current trade entries will be conservative (fewer
actual trades, and each with higher expected return). When the trend
continues to the disadvantage of the model, this conservatism reduces
losses, quite the reverse of what happens when volatility is increasing
and the model is underestimating it.
Cutting off losing trades when spread relationships change is
ideal. However, implementing this requires another prediction: a
prediction of the change. Typically the best we can do is identify
change soon after it happens, and characterize it soon after that.
Even this is challenging. See Chapter 3 and the referenced discussion
in Pole et al., 1994.
Looking at current FRE–SAI trades from the perspective of
August 1998 we ask: Must we maintain a persistently losing position?
Obviously not; a position can be unwound at a manager’s discretion.
But when should the pair be readmitted to the candidate trade
universe? The historically tight coupling of FRE and SAI seems to be
--- page 172 ---

Nobel Difﬁculties
145
breaking down; if the breakdown applies to the underlying common
structure of the stock return series, then the stocks will cease to satisfy
pair selection criteria and trading will cease. If the common structure
remains, with spreads oscillating about a new level or returning to
the recent historical level, the stocks will continue to be selected and
will again be traded proﬁtably once the disturbance is over.
On Thursday August 20, 1998 the takeover of SAI by AIG was
announced. SAI closed on Wednesday at $64 3
8 the all stock deal
valued SAI at a 25 percent premium (before the market opening).
One might seriously wonder at the nature of the buying pressure
behind the run-up in price of SAI before the takeover.
8.3
RISE OF A NEW RISK FACTOR
The international credit crisis of the summer of 1998 was an interesting time for the practice of statistical arbitrage. Performance
problems began in June and, for many, accelerated through July and
August. During this time, it became starkly apparent for the ﬁrst time
that perceptions about the credit quality of a company had a direct
impact on investor conﬁdence in near-term company valuation. As
sentiment became negative and stocks were marked down across the
market, the magnitude of price decline was strongly related to the
credit rating of outstanding corporate debt. Companies with lower
rating had their stock price decimated by a factor of three to one
more than companies with a higher rating. Such dramatic discriminatory action had not previously been described; certainly there was
no prior episode in the history of statistical arbitrage.
There are many hypotheses, fewer now entertained than was the
case at the time, about the nature of the linkages between credit and
equity markets in 1998, and why the price movements were so dramatic. Without doubt, the compounding factor of the demise of the
hedge fund Long-Term Capital Management and the unprecedented
salvage operation forced by the Federal Reserve upon unenthusiastic
investment banks heightened prevalent fears of systemic failure of the
U.S. ﬁnancial system. At the naive end of the range of hypotheses is
the true, but not by itself sufﬁcient, notion that the Fed’s actions simply ampliﬁed normal panic reactions to a major economic failing. An
important factor was the speed with which information, speculation,
gossip, and twaddle was disseminated and the breadth of popular
