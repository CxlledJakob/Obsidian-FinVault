# Quantitative financial analytics_ the path to investment profits.pdf — pages 476–495

--- page 476 ---

Capital Market Theory, Eﬃciency, and Imperfections
453
M
0
1.0
µ
CiM
rpure
µM
bi
SML
2
Figure 10.7. The SML
correlated). Therefore, the return of the security should only contain
a risk premium to the extent of the risk that will actually be borne
(that is, that portion of the total risk which cannot be eliminated
by diversiﬁcation — which is variously called nondiversiﬁable risk or
systematic risk).
If this logic is accepted, it is then possible to generate a security
market line (SML), as shown in Figure 10.7, where the return on
individual securities is related to their covariance with the market.
If capital markets are in equilibrium and all the other assumptions
of this chapter hold, then the parameters of each security should
lie on the SML. Furthermore, because the risk of a portfolio is the
weighted sum of the nondiversiﬁable risk of its component securities,
all portfolios should also fall on the SML in equilibrium. It should be
noted that although all portfolios will fall on the SML, as a general
rule no individual securities will fall on the CML (they will all lie to
the right of the CML).
Several additional points may be made regarding the SML. In
the ﬁrst place, several authors diﬀerentiate between defensive and
aggressive securities on the basis of whether the covariance of the
security with the market is less or greater than the variance of the
market return itself. If CiM < σ2
M, then the changes in the security’s
return caused by market changes are less than the market changes
themselves and the security is considered defensive. If CiM > σ2
M,
--- page 477 ---

454
Quantitative Financial Analytics
then the security responds more than proportionally to market
changes and is considered aggressive.
It is also possible to discuss the SML in terms of Sharpe’s index
model (see Chapter 9), where:
µi = ai + biµI + ci.
(10.3)
The bi term (called Sharpe’s beta coeﬃcient), given µI, is equal to:
(bi|µI) = CiI
σ2
I
= CiI

1/σ2
I

.
(10.4)
which, if the index is a valid depiction of the market:
(bi|µI) = CiM
σ2
M
= CiM

1/σ2
M

.
(10.5)
Under these assumptions, the abscissa of a point on the SML
expressed in terms of bi is merely 1/σ2
M times that of the same
point expressed in terms of CiM and the two are directly comparable.
Viewed another way, the risk premium an individual security would
exhibit in equilibrium is:
(µi −rpure) =
µM −rpure
σ2
M

CiM = (µI −rpure)bi.
(10.6)
It is further possible to say that defensive securities would have a
bi less than, and aggressive securities greater than, unity. A major
advantage of transferring the discussion into beta terminology is
that the regression coeﬃcient can be used directly to estimate the
systematic risk of the asset.
Unfortunately, the beta concept also possesses serious pitfalls. In
the ﬁrst place, its very simplicity and popularity cause it to be used
by many people who fail to understand its limitations. Because the
concept is subject to all the assumptions of both regression analysis
and the eﬃcient capital market hypothesis, statistical problems
and economic imperfections may undermine its usefulness. Many
investors are unaware of these limitations and have blithely employed
--- page 478 ---

Capital Market Theory, Eﬃciency, and Imperfections
455
the beta as a new get-rich-quick scheme. The notion that one need
only ﬁll his portfolio with securities possessing large betas and wealth
shall surely follow has been adopted in many quarters by individuals
who do not appreciate the fact that at best the beta is a risk-measure
surrogate and not an indicator of future returns. The idea that the
assumption of large amounts of risk will generate large returns only
approaches being correct over the long run in reasonably eﬃcient
markets, and even then it ignores utility considerations.
A further diﬃculty with the beta concept follows from empirical
ﬁndings that betas for small portfolios (and, of course, individual
securities) over short periods can be highly unstable, although there
is evidence of reasonable stability for the betas of large portfolios over
long holding periods. It would thus appear that one of the few valid
applications of the beta concept would be as a risk–return measure
for large portfolios. An example of how betas can be used in this
regard is presented in the next section.
Portfolio Evaluation
Several measures directly related to capital market theory have been
developed for the purpose of a portfolio evaluation. The latter is
essentially a retrospective view of how well a particular portfolio or
portfolio manager did over a speciﬁed period in the past. Most of
the published research in this area has dealt with mutual funds,
seemingly because they are controversial, economically important
in certain ﬁnancial markets, and possessed of long life with readily
available data. Much of the early work in this area (including the
advertisements of the funds themselves) was of a simple time-series
nature, showing how well an investor could have done over a given
period in the past if he had invested then or else comparing these
results to what the investor could have earned in other funds or the
market as a whole. The more recent work considers both return and
its variability, contending that mutual funds that invest in riskier
securities should exhibit higher returns.
One result of this work, considered subsequently, has been the
ﬁnding that investors do as well or better on average by selecting
--- page 479 ---

456
Quantitative Financial Analytics
securities at random as they could with the average mutual fund.
Another implication, of more relevance here, is the growing feeling
that the managers of any kind of portfolio should be rated not on the
return they earn alone but rather on the return they earn adjusted
for the risk to which they subject the portfolio.
Before proceeding, however, a caveat is in order about the
nature of ex post risk and return measures. As in any problem in
measurement, one must delineate (1) why a measurement is being
made, (2) what is to be measured, (3) which measurement technique
is appropriate, and (4) the import of the results of the measurement.
If one is not careful, ex post return measurements can easily result
in the “if only I had . . .” syndrome, which is a waste of time and
eﬀort as far as making an investment in the present is concerned.
For such measures to be of use, one must assume that the ability of
a manager or fund to earn greater-than-average returns in the past
is some indication of ability to do so in the future.
As the empirical work cited below indicates, there is little
evidence to support this contention. As far as risk is concerned,
there is some doubt about what the concept of ex post risk means.
Most of the writers in this area are careful to stress the term
“return variability” instead of risk per se. Because the outcomes
of all past events are currently known with certainty, the use of
return variability as a measure of risk in this instance involves a
diﬀerent notion of risk than we have been using. Again, to make
operational investment decisions, it would seem necessary to assume
that past risk–return behavior of managers or portfolios either could
or would be maintained in the future. Deferring judgment for the
moment on the above reservations, let us consider the proposed
evaluation measures. Sharpe (1966) has proposed the use of a rewardto-variability ratio related to the slope of the CML:
µi −rpure
σi
.
(10.7)
In eﬀect, Sharpe is computing the slope of the borrowing–lending
line going through the given portfolio and arguing that a greater
slope is more desirable. In terms of Figure 10.8, Sharpe demonstrates
--- page 480 ---

Capital Market Theory, Eﬃciency, and Imperfections
457
i
rpure
ri
J
K
Direction of increasing
desirability
Figure 10.8. Sharpe’s Return-to-Variability Criterion
that no a priori judgments about the performance of portfolios J
and K can be made until the borrowing–lending lines are added.
Subsequently, it is possible to note that a combination of the greater
return to variability portfolio J and riskless loans dominates any
combination of K and loans. Equation (10.7) has become quite
famous among practitioners and is now known as the “Sharpe Ratio.”
It is regularly employed to adjust portfolio returns for risk and to
compare these risk-adjusted returns with market averages (S&P 500,
DJIA, etc.).
A second measure based on the SML has been proposed by
Treynor:
µi −rpure
bi
.
(10.8)
The line in (beta, return) space = rpure + (µi −rpure)/(bi) = characteristic line of security or portfolio i (Figure 10.9). See Treynor
(1965) and Treynor and Mazuy (1966).
The implications of this analysis for the determination of the
relative performance of portfolios J and K are shown in Figure 10.9.
The methodology is fairly similar to that of Sharpe, except that by
using the SML instead of the CML, the Treynor measure is capable
of evaluating individual security holdings as well as portfolios.
A disadvantage is that the accuracy of the rankings depends in part
upon the assumption (implicit in the use of the SML) that the fund
--- page 481 ---

458
Quantitative Financial Analytics
i
rpure
ri
J
K
Direction of increasing
desirability
Figure 10.9. Treynor’s Characteristic Line Analysis
i
rpure
ri
J
K
M
SML
Direction of increasing
desirability
Figure 10.10. Jensen’s Measure
evaluated would have been held in an otherwise perfectly diversiﬁed
portfolio.
A third measure, also based on the SML but diﬀerent from
Treynor’s, has been proposed by Jensen (1968, 1969):
(µi −rpure) −bi(µM −rpure).
(10.9)
This measure is expressed in units of return above or below the
pure rate of a line drawn through the parameters of the security
or portfolio parallel to the SML, as illustrated in Figure 10.10.
This measure does allow comparisons of a portfolio to the market
and is also amenable to estimation by regression; because of its
--- page 482 ---

Capital Market Theory, Eﬃciency, and Imperfections
459
treatment of diﬀerential risk, however, direct comparisons between
funds or portfolios generally cannot be made. Furthermore, it has
been suggested that all three of the above measures are biased against
high-risk portfolios by failing to recognize the inequality of borrowing and lending rates and the resulting nonlinearity of the SML
and CML.
Both the Sharpe and the Treynor ratios measure excess return
per unit of risk. The Sharpe ratio provides this per unit of total
risk (standard deviation), and the Treynor measures the excess
return per unit of systematic risk (beta). It is clear, however, that
upside variance is a positive outcome for portfolio returns, but that
downside deviation with respect to some target return is the harmful
component. This distinction is an attempt to better deﬁne “risk”
as opposed to “volatility.” As Markowitz (1959) noted (p. 194, 1st
edition),
Analysis based on semi-variance tends to produce better portfolios
than those based on variance. Variance considers extremely high
and extremely low returns equally desirable. An analysis based
on variance seeks to eliminate both extremes. An analysis based
on semi-variance, on the other hand, concentrates on reducing
losses.
In the early 1980s’ Frank Sortino’s research developed a relative
risk ratio which bears his name, based on the downside semi-variance
relative to a target rate of return. He originally wanted to call the
measure the “mean-lower partial moment ranking ratio,” but instead
it was coined the Sortino ratio. It is calculated as:
µi −rDTR
σD
,
(10.10)
where DTR = desired target return (formerly known as MAR,
minimum acceptable return);
σD =



 1
n
n

t=1
(µt −rDTR)2 · I(µt < rDTR)
--- page 483 ---

460
Quantitative Financial Analytics
is the downside deviation (lower semi-variance); and I(x) is the
indicator function, i.e. I(x) = 1 if x ≥0 and
I(x) = 0
if x < 0.
Professor Sortino has collaborated with Robert van der Meer
and Auke Plantinga to advocate their Upside Potential Ratio
(UPR), calculated as upside potential divided by downside deviation (Sortino et al., 1999). In this framework reward is measured
not in expected return but in upside potential (exceeding DTR);
and risk is measured as downside volatility of returns failing to
meet DTR.
Another measure introduced earlier that seems to hold some
promise as an evaluation tool is the geometric mean. Over a given
time period, the geometric mean portfolio return could be compared
to that of other portfolios or some market index. There are several
advantages to such a measure. Assuming that the interval considered
is “suﬃciently” long (and if it is not, one may doubt the validity of
any evaluation technique), then undue risk-taking should manifest
itself in numerous low period returns and, thus, a reduced geometric
mean (or terminal wealth, which is an equivalent concept in this
context). If such is not the case, then the equivalence of historical
variability and risk becomes increasingly dubious.
The geometric mean also facilitates the use of very short investment periods (because funds value their holdings from one to four or
more times a day, up to one thousand observations per year could
be obtained). It provides a cumulative eﬀect if desired by simply
including each new set of observations without discarding any of
the old which could, in turn, be used to determine a cumulative
management performance fee (some of which would be withheld
against poor future performance).
Depending upon the information desired by the investor, therefore, several measures of portfolio performance are available. We must
again stress, however, that the past is generally a “sunk cost” and
--- page 484 ---

Capital Market Theory, Eﬃciency, and Imperfections
461
unless certain continuity assumptions appear valid, the predictive
power of these measures is seriously questionable.
Additional Topics in Portfolio Management
The portfolio selection methodology described in Chapter 9 requires
a complete enumeration of the parameters of available investments
and of the investor’s utility function. Because of the costs of
obtaining such information and the fact that some information may
be unavailable at any price, any methodology that further delimits
the area of investigation is that of value. A major breakthrough was
accomplished when Markowitz devised the quadratic programming
algorithm to generate the eﬃciency frontier (see Chapter 9). Another
advance was made when Sharpe employed an index model to simplify
input generation (Chapter 9). This section considers additional
techniques for reducing the number of portfolios under consideration.
A criterion that is more an addendum to the concept of eﬃ-
ciency than a selection criterion, but nevertheless provides a good
introduction to the discussion, may be considered. Portfolios with
low µ and σ may not be eliminated by the concept of eﬃciency in
comparison with portfolios having much higher µ and only slightly
larger σ, even though the probability that the best outcome of the
former would ever exceed the worst outcome of the latter was very
small. Therefore a lower conﬁdence limit could be set at µ −Kσ
and low-return portfolios dominated by this rule could be dropped
from the eﬃciency frontier. The parameter K would be a function of
the investor’s degree of risk aversion and, if return could be assumed
to be normally distributed, could be determined on a one-tail test
of the percentage of the time the investor would tolerate a shortfall
of actual returns (for example, 16 percent for K = 1, 2 percent for
K = 2, and so on).
For example, suppose that an investor was prepared to ignore
low returns that occurred no more than 2 percent of the time. This
percentage would correspond to the portion remaining in the left tail
of a normal distribution at a point two standard deviations below
--- page 485 ---

462
Quantitative Financial Analytics
the mean; thus, K = 2. Now consider the following points on an
eﬃciency frontier:
A
B
µ
4 percent
10 percent
σ
1
3
µ −2σ
2
4
Neither point can be termed ineﬃcient, as B has a higher return
but at greater risk. It may be noted, however, that the investor’s
perceived worst outcome of B (the lower conﬁdence limit of B) is
greater than the same for A (that is, 4 percent >2 percent). Thus,
portfolio A, and other portfolios in the lower range of the eﬃciency
frontier, could be eliminated by the conﬁdence-limit criterion.
A far more comprehensive concept, called stochastic dominance,
allows for the elimination from further consideration of securities or
portfolios on the basis of known characteristics of entire classes of
utility functions. First-degree stochastic dominance (FSD) requires
only the assumption that more wealth is preferable to less (that is,
dU/dW > 0). It may then be said that investment B exhibits FSD
over investment A if, for each possible level of return, the cumulative
probability of B falling below the level of return is less than or equal
to the same for A (and the strict inequality holds in at least one
case). Consider the following example:
ri
Prob. (A)
Prob. (B)
5 percent
0.2
0.1
10
0.3
0.2
15
0.4
0.3
20
0.1
0.4
1.0
1.0
µ
12 percent
15 percent
σ
4.6
5.0
--- page 486 ---

Capital Market Theory, Eﬃciency, and Imperfections
463
RETURN (no greater than)
CUMULATIVE PROBABILITY
1.0
0.9
0.8
0.7
0.6
0.5
0.4
0.3
0.2
0.1
0
5%
10%
15%
20%
B
A
Figure 10.11. First-Degree Stochastic Dominance
The cumulative probability distributions of returns for A and B are
shown in Figure 10.11. The FSD decision rule is shown as follows:
ri
Cumulative
Probability
A = A(ri)
Cumulative
Probability
B = B(ri)
A(ri) −B(ri)
5 percent
0.2
0.1
+.1
10
0.5
0.3
+.2
15
0.9
0.6
+.3
20
1.0
1.0
0
For investment B:
FSD(ri) = A(ri) −B(ri) ≥0
for all ri, and
> 0
for at least one ri.
Thus, investment B exhibits FSD over investment A and would be
preferred by anyone to whom more wealth was preferable to less (that
is, all rational persons, including risk seekers and neutrals, as well as
averters).
Second-degree stochastic dominance (SSD) requires the assumption of risk neutrality or aversion (d2U/dW 2 ≤0) as well as
--- page 487 ---

464
Quantitative Financial Analytics
rationality (dU/dW > 0). Under these assumptions, it is possible
to make selections between certain investments that do not exhibit
FSD. Consider the following investment alternatives:
ri
Prob. (A)
Prob. (B)
5 percent
0.2
0.1
10
0.3
0.4
15
0.3
4.0
20
0.2
0.1
1.0
1.0
µ
12.5 percent
12.5 percent
σ
5.1
4.03
The FSD analysis would provide:
ri
Cumulative
Probability
A = A(ri)
Cumulative
Probability
B = B(ri)
A(ri) −B(ri)
= FSD(ri)
5 percent
0.2
0.1
+.1
10
0.5
0.5
0
15
0.8
0.9
−.1
20
1.0
1.0
0
Thus, neither investment would exhibit FSD over the other. SSD,
in eﬀect, considers the cumulative diﬀerence between the two cumulative probability distributions employed in FSD. Again considering
investment B:
SSD(ri) = SSD(ri−1) + (ri −ri−1)[A(ri−1) −B(ri−1)]
SSD(ri) = SSD(ri−1) + (ri −ri−1)FSD(ri−1).
--- page 488 ---

Capital Market Theory, Eﬃciency, and Imperfections
465
(1)
(2)
(3)
(4)
(5)
(6)
(7)
i
ri
ri −ri−1 FSD(ri−1) (3) × (4) SSD(ri−1) SSD(ri)
1
5 percent
—
—
—
—
0
2
10
0.05
+.1
+.005
0
+.005
3
15
0.05
0
0
+.005
+.005
4
20
0.05
−.1
−.005
+.005
0
By the SSD equation, col (7) = col (5) + col (6) and, in turn, becomes
the entry in col (6) on the next row. Thus, investment B is preferred
by SSD if SSD(ri) ≥0 for all i and the strict inequality holds in at
least one case.
Finally, if neither FSD nor SSD will allow a choice to be made
between two investments, Third-degree stochastic dominance (TSD)
may be employed. In addition to the ﬁrst and second order conditions
for the utility of wealth function discussed above, TSD also requires
that d3U/dW 3 ≥0. Following the parallelism previously established,
TSD is essentially concerned with the cumulative functions employed
in SSD. We present our ﬁnal investment comparison with regard to
showing the dominance of B:
ri
Prob. (A)
Prob. (B)
5 percent
0.1
0
10
0
0.3
15
0.9
0.6
20
0
0.1
1.0
1.0
µ
14 percent
14 percent
σ
3
3
--- page 489 ---

466
Quantitative Financial Analytics
ri
A(ri)
B(ri)
FSD(ri)
5 percent
0.1
0.0
+.1
10
0.1
0.3
−.2
15
1.0
0.9
+.1
20
1.0
1.0
0
(1)
(2)
(3)
(4)
(5)
(6)
(7)
i
ri
ri −ri−1 FSD(ri−1) (3) × (4) SSD(ri−1) SSD(ri)
1
5 percent
—
—
—
—
0
2
10
0.05
+0.1
+0.005
0
+0.005
3
15
0.05
−0.2
−0.01
+0.005
−0.005
4
20
0.05
+0.1
−0.005
−0.005
0
Because neither FSD nor SSD can be shown, the TSD for B is
given by:
TSD(ri) = TSD(ri−1 + (ri −ri−1))[SSD(ri) + SSD(ri−1)]/2.
For B to be preferred, then, TSD(ri) ≥0 for all i (with the strict
inequality holding for at least one i) and, furthermore, µB ≥µA. The
TSD of B over A is shown in Figure 10.12.
At this writing, there exist no algorithms for the generation
of stochastic dominance (SD) eﬃcient portfolios and the analysis
implied has remained dormant for decades. The work done has
been of a sampling nature, primarily to demonstrate the diﬀerences
between SD and (σ, µ) eﬃcient portfolios. The Sharpe mutual-fund
studies (see above) were replicated for 34 funds between 1954 and
1963, and it was found that no fund dominated the Dow Jones
Industrial Index although the latter exhibited SSD over six funds
and TSD over nine. The ability to select optimal portfolios with a
--- page 490 ---

Capital Market Theory, Eﬃciency, and Imperfections
467
(1)
(2)
(3)
(4)
(5)
(6)
i
ri
ri −ri−1
FSD(ri−1)
(3) × (4)
SSD(ri−1)
1
5 percent
—
—
—
—
2
10
0.05
+0.1
+0.005
0
3
15
0.05
−0.2
−0.01
+0.005
4
20
0.05
+0.1
−0.005
−0.005
(7)
(8)
(9)
(10)
(11)
SSD(ri)
(6) × (7)
2
(8) × (3)
TSD(ri−1)
TSD(ri) = (9) + (10)
0
—
—
—
0
+0.005
+0.0025
+0.000125
0
+0.000125
−0.005
0
0
+0.000125
+0.000125
0
−0.0025
−0.000125
+0.000125
0
Figure 10.12. Worksheet for TSD
minimal knowledge of individual preferences provided by SD holds
great promise, but many problems of implementation remain to be
solved.
In addition to stochastic dominance, several authors have
attempted to provide other portfolio selection criteria that avoid
the necessity of collecting utility data from the investor. If such
techniques could prove satisfactory, numerous problems could be
avoided. Among them are those cases in which an investor’s risk
aversion is not known, when risk aversion changes over time, or when
more than one person is the beneﬁciary of a portfolio. A speciﬁc
technique for portfolio selection, on the basis of minimizing the
probability of the occurrence of some disastrous level of loss (D),
was presented over 60 years ago by Roy (1952). He employed
Chebyschev’s inequality, which does not require the assumption of a
special form of probability distribution for returns. Expressed in our
terminology, the relevant form of the inequality is:
P(X|X ≤D) ≤
σ2
(µ −D)2 .
(10.11)
--- page 491 ---

468
Quantitative Financial Analytics
which, when diﬀerentiated, set equal to zero, and solved, provides
a minimum probability at σ/(µ −D). In Figure 10.12, it will be
observed that any line connecting point D to the eﬃciency frontier
will have slope σ/(µ −D) but only at the point of tangency will the
point itself have the requisite slope. The point of tangency is thus
the safety-ﬁrst portfolio associated with a given minimum required
return. Two such points are illustrated in Figure 10.13.
An approach similar in methodology has been suggested by John
Lintner (1965). If we let rpure represent the rate to be earned on some
µ
µ
D2
D2
D1
D1
SF2
SF2
SF1
SF1
E
E
F
F
(a) As Per Roy
(b) Axes Reversed
Figure 10.13. Safety-First Portfolio
--- page 492 ---

Capital Market Theory, Eﬃciency, and Imperfections
469
riskless asset then Lintner deﬁnes the excess return (X) to be earned
on a given risky asset as:
Xi = µi −rpure.
It will be recalled that the parameters for the two-asset portfolio
when security 2 is riskless are:
µ = α1µ1 + α2µ2,
and
σ = α1σ1
thus:
α1 = σ
σ1
.
Bear in mind all the while that asset 1 can be a risky portfolio as
well as a security. But:
µ2 = rpure
and
α2 = 1 −α1,
therefore:
µ = α1µ1 + (1 −α1)rpure
µ = α1µ1 + rpure −α1rpure
µ = rpure + α1(µ1 −rpure),
and substituting the relationships deﬁned above:
µ = rpure + σ
σ1
X1
µ = rpure + X1
σ1
σ
µ = rpure + θσ,
where
θ = µ1 −rpure
σ1
.
(10.12)
An examination of Equation (10.12) will indicate that a portfolio
that maximizes θ will also maximize µ for a given σ and rpure. The
verbal sense of this is that we are trying to maximize excess return
per unit of risk. The geometric equivalence to the Roy approach is
shown in Figure 10.14. Here again, any line connecting rpure with
a risky security or portfolio will possess the requisite slope, but a
--- page 493 ---

470
Quantitative Financial Analytics
µ
r*
F
E
C
B
A
Figure 10.14. Excess-return Criterion Portfolio
maximum slope is desired. Thus, it follows that the risk-excess return
trade-oﬀis better in the case of B than A, and further that C would
be even better except that, by deﬁnition, no securities or portfolios
exist above the eﬃciency frontier. Further reﬂection should indicate
that the optimal portfolio by the excess-return criterion is found
at the point of tangency between a ray emanating from rpure and
the eﬃciency frontier. The similarity to the Roy technique is further
illustrated by the fact that, if the Roy disaster level (D) is set equal
to rpure, the two approaches will select the same portfolio.
In comparing the Roy and Lintner approaches, several points
should
be
made.
The
safety-ﬁrst
model,
from
its
basis
in
Chebyschev’s inequality to its goal of minimization of probability of
outcomes below one speciﬁc point, seems to come as close to decision
making under uncertainty as any technique presented in this book;
very little is assumed to be known about either the risk preferences
of the investor or the distribution of returns on investment. This lack
of speciﬁcation is an advantage in many real-world situations, and
this is one reason the model was included here. On the other hand,
if more complete information is available, more precise models may
be employed. Surprisingly enough, given their technical similarity,
the Lintner model is on the other end of the spectrum in regard to
equilibrium and perfection assumptions. To be universally applicable
--- page 494 ---

Capital Market Theory, Eﬃciency, and Imperfections
471
for risk averters, the excess-return criterion requires the separation
theorem (discussed earlier) to hold, which assumes, among other
things, that the portfolio can borrow or lend at the same rate
(speciﬁcally, at rpure). The excess-return criterion essentially involves
the application of the basic capital market theory model to the
selection of individual portfolios. Although this application does not
require all the equilibrium assumptions of capital market theory, the
likely inapplicability of the separation theorem is enough to raise
doubts regarding its general adoption.
A ﬁnal criterion for portfolio selection without speciﬁc reference
to utility considerations that has been suggested is the maximization
of geometric mean. If it may be assumed that (1) the same
investment opportunities are available in each investment period;
(2) the outcomes of these opportunities are independent over time;
and (3) all income is reinvested, then the terminal wealth at the end
of n periods associated with investment in any given portfolio is given
by the following equations. Let Wi,n = wealth in period n associated
with investment in portfolio i; ρi,j = return earned in period j on
portfolio i; W0 = initial wealth; N = number of periods.
Then
Wi,n = W0(1 + ρi,1)(1 + ρi,2) · · · (1 + ρi,n)
Wi,n = W0
n

j=1
(1 + ρi,j)
(10.13)
Wi,n
W0
=
n

j=1
(1 + ρi,j)

Wi,n
W0
 1
n
=


n

j=1
(1 + ρi,j)


1
n
E

Wi,n
W0
 1
n
−1

= E




n

j=1
(1 + ρi,j)


1
n
−1

.
(10.14)
--- page 495 ---

472
Quantitative Financial Analytics
The right side of Equation (10.14) is the expected geometric mean
return on portfolio i. The portfolio that maximizes this expectation
thus will maximize the expectation of terminal wealth. It can also
be shown (by the central-limit theorem) that the probability of the
maximum geometric mean portfolio resulting in greater terminal
wealth than any other available portfolio approaches unity as n
approaches inﬁnity.
All the above, however, are simply mathematical tautology. It
was shown earlier that the maximization of the geometric mean of
returns is consistent with the maximization of a log utility-of-wealth
function. Thus, if the investor possesses a log utility function or,
given the central limit theorem, if the number of investment periods
is inﬁnite, the geometric-mean criterion is suﬃcient. In some other
cases, it has been found to be a reasonable approximation. However,
Samuelson has shown that as long as n is ﬁnite, there exist classes of
utility functions for which the proposed criterion is not even a good
approximation. Indeed, he also demonstrated that there are classes
of utility functions for which no uniform strategy is optimal (see Paul
Samuelson, 1971) Even without Professor Samuelson’s argument,
there is a good question as to whether assumptions (1)–(3) above are
very realistic. The problems of multiperiod optimization are indeed
great, however, and are considered subsequently. It will soon be
apparent that the other techniques are suﬃciently troublesome that
geometric mean maximization becomes a very attractive alternative
if the assumptions are anywhere close to being fulﬁlled.
It should be noted from the outset that the portfolio and capital
market theory outlined above remains essentially unimplemented
even in the security investment ﬁeld. This result follows despite
the facts that: (1) securities are homogeneous and divisible; (2) the
returns from securities do not vary greatly with the holder (little
management and relatively simple tax eﬀects, at least at the margin);
(3) the markets for securities are relatively eﬃcient (in terms of
transaction costs, liquidity, and so on); (4) the returns from securities
appear to be independent over time (little if any serial correlation)
and, thus, independent of holding period; (5) a great deal of publicly
