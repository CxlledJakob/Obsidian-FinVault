# Statistical Arbitrage_ Algorithmic Trading Insights and -- Karen M_ Sowers; Andrew Pole -- Wiley Finance, 1, 2007 -- Wiley & Sons, Incorporated, John -- isbn13 9780470138441 -- 6b0138550172e24db7f13c932e054fb9 -- An.pdf — pages 134–153

--- page 134 ---

0.2
0.4
0.6
0.8
19990104 19990129 19990226 19990331 19990430 19990528 19990630
FIGURE 6.4
GM–F rolling 20-day correlation
−0.05
0.0
0.05
percent
19990104
19990129
19990226
19990331
19990430
19990528
19990630
FIGURE 6.5
GM–F spread daily return
107
--- page 135 ---

108
STATISTICAL ARBITRAGE
typical procedures used to reduce unrealistic jumps in such indirectly
measured quantities as volatility (see Chapter 3). Figure 6.5 shows
the spread return: return on GM minus return on F.
6.2.4
Primer on Measuring Spread Volatility
Let’s begin by asking the question: Does statistical arbitrage generate
higher returns when volatility is high or when it is low?
Absent any stock-speciﬁc events, higher interstock (spread) volatility should generate greater returns from a well calibrated model.
Figure 6.6 shows the average local volatility (20-day moving window) for pairwise spreads for stocks in the S&P 500 index from
1995 through 2003. Two years of outstanding returns for statistical
arbitrage were 2000 and 2001. Both were years of record high spread
volatility; 2000 higher in spread volatility and statistical arbitrage
return than 2001—nicely supporting the ceteris paribus answer.
But 1999 was the worst year for statistical arbitrage return in a
decade while spread volatility was equally high. There were many
0.05
0.10
0.15
199503
199703
199903
200103
200303
FIGURE 6.6
Average local standard deviation of spreads
--- page 136 ---

Interstock Volatility
109
stock-speciﬁc events, principally earnings related, with uniformly
negative impact on return in 1999. So noticeable, widespread, and
troubling were these events that the SEC eventually passed Regulation
Fair Disclosure (Reg. FD) to outlaw the activities.
Using a local estimate of volatility, what picture is obtained
from representative spread series? What can we infer from the spread
volatility chart in Figure 6.6 using the sample local volatility reference
patterns?
Figure 6.7 illustrates local volatility (using an equally weighted,
20-point window) for two sample spread series. The top panel, (a),
shows the spread series, the center panel, (b), the local volatility
estimates. There is nothing surprising here, the calculation being a
measure of variation about a constant line segment of the curves in
the top frame. Noteworthy is the observation that the average level
of local volatility is similar for the two series.
What happens when a different measure of ‘‘local’’ is used? The
bottom panel, Figure 6.7(c), illustrates the situation for a 60-point
window: The striking feature now is the higher level of volatility indicated for the greater amplitude spread. (While we continue to couch
the presentation in terms of a spread, the discussion applies equally to
any time series.) Once again, there is no surprise here. The 60-point
window captures almost a complete cycle of the greater amplitude
series—the estimated volatility would be constant if precisely a full
cycle was captured—and, hence, the local volatility estimate reﬂects
the amplitude of the series. In the previous case, the shorter window
was reﬂecting only part of the slower moving series variation. Which
estimate of volatility reﬂects reversion return opportunity? Here the
answer is easy.
Now consider what picture would emerge if an average over a
set of such series were examined, each such series mixed with its own
‘‘noise’’ on both amplitude and frequency.
Properly cautioned, what can be inferred from Figure 6.6? Before
attempting an answer, the archetypal example analyses clearly advise
looking at local volatility estimates from a range of windows (or
local weighting schemes)—it does seem advisable to concentrate on
evidence from shorter intervals and focus on average levels of local
volatility; mundane variation in the estimate may be little more than
artifact. May be.
--- page 137 ---

110
STATISTICAL ARBITRAGE
(a)
0
50
100
150
200
0
50
100
150
200
−2
−1
0
1
2
(b)
0.0
0.5
1.0
1.5
0.0
0.5
1.0
1.5
(c)
60
80
100
120
140
160
180
200
FIGURE 6.7
(a) Archetypal spread series; (b) local volatility estimate (20-point
window, equal weights) of spread series; (c) local volatility estimate (60-point
window) of spread series
Figure 6.8 reproduces the two example spread curves from Figure
6.7 and adds a third. The new series exhibits the same amplitude
as the original high-amplitude series and the same frequency as the
original higher frequency series. It therefore has the advantage of
more frequent and higher value reversion opportunities. The center
panel, (b), depicting local volatility estimates, indicates that the
--- page 138 ---

Interstock Volatility
111
(a)
0
50
100
150
200
−2
−1
0
1
2
(b)
50
100
150
200
(c)
60
80
100
120
140
160
180
200
0.0
0.5
1.0
1.5
0.0
0.5
1.0
1.5
FIGURE 6.8
(a) Archetypal spread series; (b) local volatility estimate (20-point
window, equal weights) of spread series; (c) local volatility estimate (60-point
window) of spread series
average volatility of this third series is twice that of the original two,
just as expected.
Now look at bottom panel, (c), which shows local volatility
estimates from the longer window. Interesting? Once again, the
analysis points to using a shorter, more local view when inferring
reversion opportunity from average levels of spread volatility.
--- page 139 ---

112
STATISTICAL ARBITRAGE
With these archetypal models, one can undertake an appropriate time-frequency analysis to precisely quantify the magnitude of
reversionary moves. Real spread series are less obliging, beset with
nonstationarity and ‘‘contaminating’’ noise.
The foregoing remarks are generally descriptive, characterizing
how series variation is reﬂected in empirical summary statistics and
indicating how the magnitude of potential gain from simple reversion
plays may be estimated. Actual reversion exploitation strategies must
be analyzed directly to make sensible inferences on expectations
therefrom, whether in the idealized settings of noise-free sinusoidal
series used here or in application to real spread histories.
Chapter 9 revisits interstock volatility in the context of the decline
in statistical arbitrage performance since 2002.
--- page 140 ---

CHAPTER7
Quantifying Reversion
Opportunities
Fortitudine vincimus—By endurance we conquer.
—Family motto of Sir E. H. Shackleton, polar explorer
7.1
INTRODUCTION
I
n this chapter, we extend the theoretical developments of the
previous three chapters in the search for a deeper understanding of
the properties of reversion in time series. There are more abstractions
and more difﬁcult mathematics here than elsewhere in the book, but
in all cases, the theoretical development is subsequently grounded
in application. Most of the discussion is framed in the language of
price series, however, the developments generally apply to any time
series. In particular, the analysis can readily be applied, sometimes
with necessary revision of inference, to transformations of price series
including returns, spreads, spread returns, factors, and so forth.
The question ‘‘What is reversion?’’ is addressed in the context of
assumed probability models for stock price generation. The models
are highly stylized and oversimpliﬁed, being entertained purely as
a device for considering notions of reversion. There is no conceit
that the models serve even as ﬁrst pass approximations to the
true, unknown, price generation mechanism. By determining the
implications of deﬁnitions of reversion under the very restrictive
assumptions of these simple models, it is hoped that a coherent
view of what reversion is will emerge. The goal is to extract from
such a view meaningful and quantiﬁable notions of reversion that
113
--- page 141 ---

114
STATISTICAL ARBITRAGE
may be used in the study of realistic price generation models. It
is hoped that such understanding will provide new insight into
statistical arbitrage, helping us to analyze and understand how and
why statistical arbitrage works at a systems or mechanistic level, and
from that build a valid market rationale for the driving forces of the
exploitable opportunities. That may be a little ambitious; perhaps
it is reaching to hope for more than indications of what kinds of
processes to think about for such a rationale. The mechanics and the
rationale are both critical to investigating and solving the problems
that beset statistical arbitrage starting in 2004 and which continue to
affect performance today: How do market structural changes impact
strategy performance?
7.2
REVERSION IN A STATIONARY RANDOM PROCESS
We begin the study with consideration of the simplest stochastic system, a stationary random process. Prices are supposed to be generated
independently each day from the same probability distribution, that
distribution being characterized by unchanging parameters. We shall
assume a continuous distribution. Price on day t will be denoted by
Pt, lowercase being reserved for particular values (such as a realized
price).
Some considerations that immediately suggest themselves are:
1. If Pt lies in the tail of the distribution, then it is likely that Pt+1
will be closer to the center of the distribution than is Pt. In more
formal terms: Suppose that Pt > ninety-ﬁfth percentile of the
distribution. Then the odds that Pt+1 will be smaller than Pt are
95 : 5 (19 : 1). A similar statement is obtained for the lower tail,
of course.
The 19 : 1 odds do not express quite the same idea as is
expressed in the ﬁrst sentence. Being ‘‘closer to the center than’’
is not the same as being ‘‘smaller than.’’ Certainly the odds ratio
quoted, and by implication the underlying scenario, are very
interesting. For completeness, it is useful to examine the ‘‘closer
to the center’’ scenario. The obvious notion of closer to the center
is formally: the magnitude of the deviation from the center on
the price scale. An alternative notion is to consider distance from
--- page 142 ---

Quantifying Reversion Opportunities
115
the center in terms of percentiles of the underlying distribution
of prices. The two notions are equivalent for distributions with
symmetric density functions, but not otherwise.
2. If Pt is close to the center of the distribution, then it is likely that
Pt+1 will be further from the center than Pt.
After a little reﬂection, (ii) seems to offer infertile ground for a
reversion study; but in a sequential context, values close to the center
are useful ﬂags for subsequent departure from the center and, hence,
of future reversionary opportunities. Recall the popcorn process of
Chapter 2 and the discussion of stochastic resonance in Chapter 3.
A generalization of the notion in (i) offers a potential starting
point for the study: If Pt > pth percentile of the distribution, then the
odds that Pt+1 < Pt are p : 100 −p. Interest here is conﬁned to those
cases where the odds are better than even. Investors largely prefer
strategies that exhibit more winning bets than losing bets, considering
such relative frequency of outcomes a reﬂection of a stable process.
The thought process is deﬁcient because by itself the win–lose ratio
imparts no information at all on the stability properties of a strategy other than the raw win–lose ratio itself. Essential information
necessary for that judgment includes the description of the magnitudes of gains from winners and losses from losers. A strategy that
loses 80 percent of the time but that never exhibits individual losses
exceeding 0.1 percent and whose winners always gain 1 percent is
a stable and proﬁtable system. Judgments about easily labeled but
complicated notions such as ‘‘stability’’ need careful speciﬁcation
of personal preferences. Often these are not made explicit and are
therefore readily miscommunicated because individuals’ preferences
are quite variable.
For Pt > median, the odds that Pt+1 < Pt are greater than
one; similarly, for Pt < median, the odds that Pt+1 > Pt are also
greater than one. The assumption of continuity is critical here, and
a reasonable approximation for price series notwithstanding the
discrete reality thereof. You may want to revisit Chapter 4 for a
rehearsal of the difﬁculties discrete distributions can pose.
Two questions are immediately apparent:
1. Is the odds result exploitable in trading?
■With artiﬁcial data following the assumed stationary process.
--- page 143 ---

116
STATISTICAL ARBITRAGE
■With stock data using locally deﬁned moments (to approximate
conditional stationarity).
2. How should reversion be deﬁned in this context?
■Reversion to the center requires modiﬁcation of the foregoing
odds to something like 75 percent →50 percent and 25 percent
→50 percent.
■Reversion in the direction of the center—so that overshoot is
allowed and the odds exhibited are pertinent.
Whichever of (1) or (2) is appropriate (which in the context
of this chapter must be interpreted as ‘‘useful for the analysis and
interpretation of reversion in price series’’), how should reversion
be characterized? As the proportion of cases exhibiting the required
directional movement (a distribution free quantity)? As the expected
(average) price movement in the qualifying reversionary cases (which
requires integration over an assumed price distribution and is not
distribution-free)?
Both aspects are important for a trading system. In a conventional trading strategy, betting on direction and magnitude of price
movements, total proﬁts are controlled by the expected amount of
reversion. If the model is reasonable, the greater the expected price
movement, the greater the expected proﬁt. The volatility of proﬁts
in such a system is determined in part by the proportion of winning
to losing moves. For the same unconditional price distributions, the
higher the ratio of winners to losers, the lower the proﬁt variance thus
spreading proﬁt over more winning bets and fewer losing bets. Stop
loss rules and bet sizing signiﬁcantly impact outcome characteristics
of a strategy, making more general absolute statements unwise.
It is worth noting the following observation. Suppose we pick
only those trades that are proﬁtable round trip. Daily proﬁt variation
will still, typically, be substantial. Experiments with real data using
a popcorn process model show that the proportion of winning days
can be as low as 52 percent for a strategy with 75 percent winning
bets and a Sharpe ratio over 2.
Reversion deﬁned as any movement from today’s price in the
direction of the center of the price distribution includes overshoot
cases. The scenario characterizes as reversionary movement a price
greater than the median that moves to any lower price—including to
any price lower than the median, the so-called overshoot. Similarly,
--- page 144 ---

Quantifying Reversion Opportunities
117
movement from a price below the median that moves to any higher
price is reversionary.
7.2.1
Frequency of Reversionary Moves
For any price greater than the median price, Pt = pt > m:
Pr[Pt+1 < pt] = FP(pt)
where FP(·) denotes the distribution function of the probability
distribution from which prices are assumed to be generated. (This
result is a direct consequence of the independence assumption.)
An overall measure of the occurrence of reversion in this situation
is then:
 ∞
m
FP(pt)fP(pt)dpt = 3
8
where fp(.) is the density function of the price distribution. Therefore,
also considering prices less than the median, Pt < m, we might say
that reversion occurs 75 percent of the time. This is the result proved
and discussed at length in Chapter 4.
Previously it was noted that the proportion of reversionary moves
is a useful characterization of a price series. The 75 percent result
states that underlying distributional form makes no difference to the
proportion of reversionary moves. Therefore, low volatility stocks
will exhibit the same proportion of opportunities for a system exploiting reversion as high volatility stocks. Furthermore, stocks that are
more prone to comparatively large moves (outliers, in statistical
parlance) will also exhibit the same proportion of reversionary opportunities as stocks that are not so prone. The practical signiﬁcance
of this result is that the proportion of reversionary moves is not
a function of the distribution of the underlying randomness. Thus,
when structure is added to the model for price generation, there are
no complications arising from particular distribution assumptions.
Moreover, when analyzing real price series, observed differences in
the proportion of reversionary moves unambiguously indicate differences in temporal structure other than in the random component.
--- page 145 ---

118
STATISTICAL ARBITRAGE
7.2.2
Amount of Reversion
Following the preceding discussion of how often reversion is exhibited, some possible measures of the size of expected reversion from a
price greater than the median are:
1. E[Pt −Pt+1|Pt > Pt+1] Expected amount of reversion, given that
reversion occurs.
2. E[Pt −Pt+1|Pt > m] Average amount of reversion.
3. E[Pt −Pt+1|Pt > Pt+1]Pr[Pt+1 < Pt] Overall expected amount of
reversion.
Remarks: Pt > m is an underlying condition. The difference between
cases 1 and 2 is that case 2 includes the 25 percent of cases where
Pt > m but reversion does not occur, Pt+1 > Pt, while case 1 does
not. Case 1 includes only reversionary moves.
If case 1 is taken to deﬁne the total amount of ‘‘pure’’ reversion
in the system, then case 2 may be considered as the ‘‘revealed’’
reversion in the system. With this terminology, it is possible to
envisage a system in which the revealed reversion is zero or negative
while the pure reversion is always positive (except in uninteresting,
degenerate cases).
Moves from a price less than the median are characterized
analogously.
Pure Reversion
Expected pure reversion is deﬁned as:
E[Pt −Pt+1|Pt+1 < Pt, Pt > m] × 1
2
+ E[Pt+1 −Pt|Pt+1 > Pt, Pt < m] × 1
2
The two pieces correspond to (a) downward moves from a price above
the median and (b) upward moves from a price below the median. It is
important to keep the two parts separate because the expected values
of each are generally different; only for symmetric distributions are
they equal. Consider the ﬁrst term only. From Figure 7.1, the cases of
interest deﬁne the conditional distribution represented by the shaded
region. For any particular price Pt = pt > m, the expected amount
--- page 146 ---

Quantifying Reversion Opportunities
119
pt
m
FIGURE 7.1
Generic price distribution
of reversion is just Pt minus the expected value of the conditional
distribution:
pt −EPt+1|Pt+1<pt[Pt+1] = pt −
 pt
−∞
pt+1fPt+1|Pt+1<pt(pt+1)dpt+1
The density of the conditional distribution of Pt+1, given that Pt+1 <
Pt, is just the rescaled unconditional density (from the independence
assumption), the scale factor being one minus the probability of the
subset of the original domain excluded by the conditioning. Expected
reversion is therefore:
pt −
1
FP(pt)
 pt
−∞
pfP(p)dp
Now we are interested in the expected value of this quantity
averaged over all those possible values Pt = pt > m:
EPt>m

Pt −EPt+1|Pt+1<Pt[Pt+1]

=
 ∞
m

pt −
1
FP(pt)
 pt
−∞
pfP(p)dp

fPt|Pt>m(pt)dpt
--- page 147 ---

120
STATISTICAL ARBITRAGE
Substituting for fPt|Pt>m(pt) = fP(pt)/(1 −FP(m)) = 2fP(pt) for Pt >
m, then the overall expected amount of pure (one-day) reversion
when Pt > m is:
E[Pt −Pt+1|Pt+1 < Pt, Pt > m]
= 2
 ∞
m

pt −
1
FP(pt)
 pt
−∞
pfP(p)dp

fP(pt)dpt
A similar analysis for the second term in the original expectation
yields:
E[Pt+1 −Pt|Pt+1 > Pt, Pt < m]
= 2
 m
−∞

1
1 −FP(pt)
 ∞
pt
pfP(p)dp −pt

fP(pt)dpt
Adding (one half times) these two results gives the expected pure
reversion as:
 ∞
m

pt −
1
FP(pt)
 pt
−∞
pfP(p)dp

fP(pt)dpt
+
 m
−∞

1
1 −FP(pt)
 ∞
pt
pfP(p)dp −pt

fP(pt)dpt
Some simpliﬁcation of this expression would be nice. Example 1,
which follows, shows simpliﬁcation possible for the normal distribution, the double integral here reducing to a single integral; however,
even there, a closed form solution remains elusive. The symmetry is
suggestive. Would the result simplify if the cut-off is taken as the
mean rather than the median? Certainly an assumption of a symmetric density leads to cancellation of the two direct terms in Pt; in fact,
the two parts of the sum are equal. Perhaps Fubini’s rule, reversing the order of integration, can usefully be applied? We do know
that the result is positive! A closed-form theoretical result remains
unknown at this time, but computation of any speciﬁc example is
straightforward (see the examples that follow).
--- page 148 ---

Quantifying Reversion Opportunities
121
Revealed Reversion
Expected revealed reversion is deﬁned as:
E[Pt −Pt+1|Pt > m] × 1
2 + E[Pt+1 −Pt|Pt < m] × 1
2
Consider the ﬁrst term of the expression:
E[Pt −Pt+1|Pt > m] = E[Pt|Pt > m] −E[Pt+1|Pt > m]
= E[Pt|Pt > m] −E[Pt+1]
by independence
= E[Pt|Pt > m] −µ
where µ denotes the mean of the price distribution. Similarly, the
second term of the expression reduces to E[Pt+1 −Pt|Pt < m] =
µ −E[Pt|Pt > m]. It is worth noting that both terms have the same
value, which follows from:
µ = E[Pt] =
 ∞
−∞
pfP(p)dp
=
 m
−∞
pfP(p)dp +
 ∞
m
pfP(p)dp
= 1
2E[Pt|Pt < m] + 1
2E[Pt|Pt > m]
whereupon:
E[Pt|Pt > m] −µ = E[Pt|Pt > m] −1
2E[Pt|Pt < m] −1
2E[Pt|Pt > m]
= 1
2E[Pt|Pt > m] −1
2E[Pt|Pt < m]
= 1
2E[Pt|Pt > m] + 1
2E[Pt|Pt < m] −E[Pt|Pt < m]
= µ −E[Pt|Pt < m]
Total expected revealed reversion may therefore be expressed equivalently as:
total expected revealed reversion = 0.5×(E[Pt|Pt> m] −E[Pt|Pt < m])
= E[Pt|Pt > m] −µ
= µ −E[Pt|Pt < m]
--- page 149 ---

122
STATISTICAL ARBITRAGE
which (for continuous distributions) is positive except in uninteresting, degenerate cases.
Note 1: This result provides a lower bound for case 1 since the
latter excludes those outcomes, included here, for which the actual
reversion is negative, namely {Pt+1 : Pt+1 > Pt, Pt > m} and {Pt+1 :
Pt+1 < Pt, Pt < m}.
Note 2: A desirable property for the reversion measure to have is
invariance to location shift. The amount of reversion, in price units,
should not change if every price is increased by $1. It is easy to
see that the expression for expected revealed reversion is location
invariant: Moving the distribution along the scale changes the mean
and median in the same amount. For the pure reversion result, it
is not very easy to see the invariance from the equation. However,
consideration of Figure 7.1 ﬁlls that gap.
Some Speciﬁc Examples
Example 1
Prices are normally distributed. If X is normally distributed with mean µ and variance σ 2, then the conditional distribution of X such that X < µ is the half normal distribution. Total
expected revealed reversion is 0.8σ. (The mean of the truncated normal distribution is given in Johnson and Kotz, Volume 1, p. 81; for
the half normal distribution the result is E[X⟩] = 2σ/
√
2π.) Thus,
the greater the dispersion of the underlying price distribution, the
greater the expected revealed reversion: a result that is nicely in tune
with intuition and desire.
From a random sample of size, 1,000 from the standard normal
distribution, the sample value is 0.8, which is beguilingly close to the
theoretical value. Figure 7.2 shows the sample distribution.
The pure reversion general result can be reduced somewhat for
the normal distribution. First, as already remarked, the terms in Pt
cancel because the density is symmetric, leaving:
−
 ∞
m

1
F(pt)
 pt
−∞
pf(p)dp

f(pt)dpt
+
 m
−∞

1
1 −F(pt)
 ∞
pt
pf(p)dp

f(pt)dpt
(The subscript on f and F has been dropped since it is not necessary
to distinguish different conditional and unconditional distributions
--- page 150 ---

Quantifying Reversion Opportunities
123
(a)
(b)
−4
−2
0
2
Index
0
200
400
600
800
1,000
−3
−1
1
2
3
150
50
0
FIGURE 7.2
Random ‘‘price’’ series: (a) sample distribution, (b) sequential
ordering
here: Only the unconditional price distribution is used.) Johnson and
Kotz give results for moments of truncated normal distributions. In
particular, the expected values of singly truncated normals required
here are:
 pt
−∞
pf(p)dp = −f(pt)
F(pt)
and
 ∞
pt
pf(p)dp =
f(pt)
1 −F(pt)
Therefore, expected pure reversion is:
−
 ∞
m
1
F(p)
−f(p)
F(p) f(p)dp +
 m
−∞
1
1 −F(p)
f(p)
1 −F(p)f(p)dp
=
 ∞
m
 f(p)
F(p)
2
dp +
 m
−∞

f(p)
1 −F(p)
2
dp
For a symmetric density, inspection shows that the two terms in the
sum are equal. Algebraically, noting that f(m −ϵ) = f(m + ϵ) and
F(m −ϵ) = 1 −F(m + ϵ), then a simple change of variable, q = −p,
gives the result immediately. The quantity (1 −F(x))/f(x) is known
--- page 151 ---

124
STATISTICAL ARBITRAGE
as Mills’ ratio. Therefore, expected pure reversion for the normal
independent identically distributed (iid) model is twice the integral
of the inverse squared Mills’ ratio with integration over half the
real line:
2
 m
−∞
M(p)−2dp
Panel (b) of Figure 7.2 shows the random sample referred to at the
beginning of the section as a time series. From this series: The number
of downward moves from above the median, {xt : xt > 0 ∩xt+1 <
xt}, is 351; the number of upward moves from below the median,
{xt : xt < 0 ∩xt+1 > xt}, is 388; the proportion of reversionary moves
is 100 ∗(351 + 388)/999 = 74% (the denominator is reduced by one
because of the need to work with pairs (xt, xt+1) and, of course, there
is no value to pair with x1,000).
Revealed reversion for this time series
Figure 7.3 shows the distribution of one-day ‘‘price’’ differences for (a) moves from above the
median, {xt −xt+1 : xt > 0}, and (b) moves from below the median,
{xt+1 −xt : xt < 0}. Not surprisingly, for such a large sample the two
look remarkably similar (in fact, the sums, or sample estimates of
expected values, agree to four signiﬁcant ﬁgures); the total of these
moves is 794/999 = 0.795, which is very close to the theoretical
expected value of 0.8. Some discrepancy is expected because treating the random sample as a time series imposes constraints on the
components of the sets of pairs of values comprising the moves.
Pure reversion for this time series
Figure 7.4 shows the distribution
of one-day ‘‘price’’ differences for (a) moves from above the median
in a downward direction only, {xt −xt+1 : xt > 0 ∩xt > xt+1}, and
(b) moves from below the median in an upward direction only,
{xt+1 −xt : xt < 0 ∩xt < xt+1}. These histograms are simply truncated versions of those in Figure 7.3, with 0 being the truncation
point. Total pure reversion is 957/999 = 0.95.
This example data is further discussed in Example 5.
Example 2
Prices are distributed according to the Student t distribution on 5 degrees of freedom. A Monte Carlo experiment yielded
the expected revealed reversion to be 0.95 (for the unit scale t5
distribution). Notice that this value is larger than the corresponding
--- page 152 ---

Quantifying Reversion Opportunities
125
(a)
−2
0
2
4
−2
0
2
4
120
80
40
0
(b)
100
60
20
0
Moves from above median
Negative moves from below median
FIGURE 7.3
Random ‘‘price’’ series: distribution of one-day moves
60
40
20
0
Moves down from above median
(a)
0
0
1
2
3
4
1
2
3
4
60
20
0
100
Negative moves up from below median
(b)
FIGURE 7.4
Random ‘‘price’’ series: distribution of one-day moves
value for the unit scale (standard) normal distribution (0.8). The
increase is a consequence of the pinching of the t density in the
center and stretching in the tails in comparison with the normal:
The heavier tails mean that more realizations occur at considerable
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
