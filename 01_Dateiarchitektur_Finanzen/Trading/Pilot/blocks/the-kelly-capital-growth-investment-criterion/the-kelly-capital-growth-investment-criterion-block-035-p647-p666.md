# The Kelly capital growth investment criterion _ theory and -- Leonard C_ Maclean, Edward O_ Thorp, W_ T_ Ziemba, Leonard -- World Scientific Handbook -- isbn13 9781283148344 -- bec576e26410d0c695fd5b867d08ec4f -- An.pdf — pages 647–666

--- page 647 ---

618
D. G. Luenberger
906
D.G. Luenberger. Log meanvariance criteria in investment problems
Latani:, H., 1959, Criteria for choice among risky ventures, Journal of Political Economy 67,
144-155.
Leland, H., 1972, On turnpike portfolios, in: G. Szego and K. Shell, eds., Mathematical methods in
investment and finance (North-Holland, Amsterdam).
Lintner, J., 1965, The valuation of risk assets and the selection of risky investments in stock
portfolios and capital budgets, Review of Economics and Statistics 48, 13- 37.
Markowitz, H., 1952, Portfolio selection, Journal of Finance 12, 77-9\.
Markowitz, H., 1959, Portfolio selection: Efficient diversification of investment (Wiley, New York,
NY).
Merton, R.C. and P.A. Samuelson, 1974, Fallacy of the log-normal approximation to optimal
portfolio decision-making over many periods, Journal of Financial Economics I, 67-94.
Samuelson, P.A., 1969, Lifetime portfolio selection by dynamic stochastic programming, Review of
Economics and Statistics 51,239-246.
Samuelson, P.A., 1970, The fundamental approximation theorem of portfolio analysis in terms of
means, variances, and higher moments, Review of Economic Studies 37, 537-542.
Samuelson, P.A., 1971, The 'fallacy' of maximizing the geometric mean in long sequences of investing
or gambling, Proceedings of the National Academy of Sciences 68, 2493-2496.
Sharpe, W., 1970, Portfolio theory and capital markets (McGraw-Hill, New York, NY).
Shiryayev, A.N., 1984, Probability (Springer-Verlag, New York, NY).
Tobin, J., 1965, The theory of portfolio selection. in: I.H. Hahn and F.P.R. Brechling, eds., The
theory of interest rates (Macmillan, New York. NY).
Williams. J.B., 1936, Speculation and the carryover, Quarterly Journal of Economics 50, 436.
--- page 648 ---

ELSEVIER
Available online at www.sciencedirect.com
aCIENCE@DIRECYO
Journal of Econometrics 116 (2003) 365-386
619
JOURNAL OF
Econometrics
www.elsevier.com/locate/econbase
43
Portfolio choice with endogenous utility: a large
deviations approach
Michael Stutzer*
Burridge Center for Securities Analysis and Valuation, Leeds School of Business. University of
Colorado, Boulder, CO 20309-0419, USA
Abstract
This paper provides an alternative behavioral foundation for an investor's use of power utility
in the objective function and its particular risk aversion parameter. The foundation is grounded in
an investor's desire to minimize the objective probability that the growth rate of invested wealth
will not exceed an investor-selected target growth rate. Large deviations theory is used to show
that this is equivalent to using power utility, with an argument that depends on the investor's
target, and a risk aversion parameter determined by maximization. As a result, an investor's risk
aversion parameter is not independent of the investment opportunity set, contrary to the standard
model assumption.
© 2003 Elsevier B.V. All rights reserved.
JEL classification: C4; 08; GO
Keywords: Portfolio theory; Large deviations; Safety-first; Risk aversion
1. Introduction
What criterion function should be used to guide personal investment decisions? Perhaps the earliest contribution was Bernoulli's critique of expected wealth maximization,
which led him to advocate maximization of the expected log wealth as a resolution of the S1. Petersburg Paradox. This was resurrected as a long-term investment
strategy in the 1950s, and is now synonymously described as either the log optimal,
growth-maximal, geometric mean, or Kelly investment strategy. As also noted in their
'Tel.: +1-319-335-1239.
E-mail address: michael-stutzer@colorado.edu (M. Stutzer).
0304-4076/03/$ - see front matter © 2003 Elsevier B.Y. All rights reserved.
doi:1 0.1 016/S0304-4076(03 )001 12-X
--- page 649 ---

620
M Stutzer
366
M. Stutzer /Journal of Econometrics 116 (2003) 365-386
excellent survey on this portfolio selection rule, Hakansson and Ziemba (1995,
pp. 65-70) argue that " .. . the power and durability of the model is due to a remarkable
set of properties", e.g. that it "almost surely leads to more capital in the long run than
any other investment policy which does not converge to it". 1
But even as a long-term investment strategy, the log optimal portfolio is problematic. It often invests very heavily in risky assets, which has led several researchers to
highlight the possibilities that invested wealth will fall short of investor goals, even
over the multi-decade horizons typical of young workers saving for retirement. For
example, MacLean et al. (1992, p. 1564) note that "the Kelly strategy never risks ruin,
but in general it entails a considerable risk of losing a substantial portion of wealth".
Findings like these motivated Browne (1995, 1999a) to develop a variety of alternative, shortfall probability-based criteria, in specific continuous-time portfolio choice
problems. Browne (1999b) considers these ideas in the context of the simplest possible investment decision, which will also be utilized to illustrate the criterion developed
herein. Further discussion of his work is included in Section 2.3. Another similarly
motivated criterion for continuous time portfolio choice is developed in Bielecki et al.
(2000), which will be discussed further in Section 2.2.
The problem is exacerbated when investors have specific, short to medium term values for their respective investment horizons. If so, some criteria will lead to horizondependent optimal asset allocations, but others will not. For example, Samuelson (1969)
proposes the criterion of intertemporal maximization of expected discounted, timeadditive constant relative risk aversion (eRRA) power utility of consumption. He
proves that when asset returns are lID, portfolio weights are independent of the horizon length. So in that case, long horizon investors should not invest more heavily
in stocks than do short horizon investors. Samuelson (1994) provided caveats to this
investor advice, citing six modifications of this specification that will result in horizon
dependencie~. 2
But an investment advisor, hired to help an investor formulate asset allocation advice, may have difficulty determining a specific value for the investor's horizon. The
advisor may be unable to determine an'investor's exact horizon length when it exists, while other investors may not have a specific investment horizon length at all.
A considerable simplification results when an infinite horizon is assumed, as has also
been done when deriving many, but not all, consumption-based asset pricing models. 3
An exception to the infinite horizon formulations is found in Detemple and Zapatero
(1991). Of course, the cost of this simplification is the inability to model horizon
dependencies.
While the time horizon parameter is irrelevant for Samuelson's intertemporal power
utility investor with IID returns, the optimal asset allocation is still very sensitive to the
specific risk aversion parameter adopted, so an advisor would have to determine it with
I See the analysis of Algoet--and Cover (1988) and the lucid exposition of Cover and Thomas (1991,
Chapter 15) for more informationon the growth maximal portfolio problem. For a spirited nonnative defense
of the growth maximal portfolio criterion, see Thorp (1975).
2 However not all of these modifications would support the oft-repeated advice to invest more heavily in
stocks when the investor's horizon is longer.
3 For a survey, see Kocherlakota (1996).
--- page 650 ---

Portfolio Choice with Endogenous Utility: A Large Deviations Approach
621
M. Stutzer/]ournal of Econometrics 116 (2003) 365-386
367
precision. An even more basic consideration is specification of the utility functional
form and its argument. Should it be a power function, or an exponential function, or
perhaps some function outside the HARA class? Should the argument be a function of
current wealth, current consumption, or some function of the consumption path (as in
habit formation models)? As a first step toward answering these questions, Section 2 of
this paper develops a new criterion of investor behavior. It starts from the observation
that the realized growth rate of investor wealth is a random variable, dependent on
the returns to invested wealth and the time that it is left invested (i.e. the investment
horizon). To obviate the need to specify a value for the latter, first assume that an
investor acts as-if she wants to ensure that the (horizon-dependent) realized growth
rate of her invested wealth will exceed a numerical target that she has, e.g. 8% per
year. By choosing a portfolio that results in a higher expected growth rate of wealth
than the target rate, the investor can ensure that the probability of not exceeding the
target growth rate decays to zero asymptotically, as the time horizon T ~ 00. But
the probability that the realized growth rate of wealth at finite time T will not exceed
the target might vary from portfolio to portfolio. Which portfolio should be chosen?
Without adopting a specific value of T, a sensible strategy is to choose a portfolio that
makes this probability decay to zero as fast as possible as T ~ 00. This will ensure
that the probability will be minimized for all but the relatively small values of T. In
other words, the decay rate maximizing portfolio will maximize the probability that the
realized growth rate will exceed the target growth rate at time T, for all but relatively
small values of T. In fact, this turns out to be true for all values of T in the special
lID cases studied in Sections 2.1 and 3.
Calculation of the decay rate maximizing portfolio is enabled by use of a simply
stated, yet powerful result from large deviations theory, known as the Gartner-Ellis
Theorem. Straightforward application of it in Section 2.2 provides an expected power
utility formulation of the decay rate criterion. But there are two important differences
between this formulation and the standard expecte4 power utility problem. First, the
argument of the utility function is the ratio of invested wealth to a level of wealth
growing at the constant target rate. Second, the value of the power, i.e. the risk aversion
parameter, is also determined by maximization. As a result, a decay rate maximizing
investor's degree of relative risk aversion will depend on the investment opportunity
set, an effect absent in extant uses of power utility.
Because this endogenous degree of risk aversion is greater than 1, the third derivative of the utility is positive, so there is also an endogenous degree of skewness
preference. This is fortunate, as some have argued that skewness preference helps
explain expected asset returns. To see why, note that in the standard CAPM, investor aversion to variance makes an asset return's covariance with the market return a risk factor, so it is positively related to an asset's expected return. Kraus and
Litzenberger (1976) argue that investor preference for positively skewed wealth distributions (ceteris paribus) should make market coskewness an additional factor, that
should be negatively related to an asset's expected return. They thus generalized the
standard CAPM to incorporate a market coskewness factor. The estimated model supports this implication of investor skewness preference. Harvey and Siddique (2000) extended this approach by incorporating conditional coskewness, concluding that "a model
--- page 651 ---

622
M Stutzer
368
M. StUlzer/]ournal oj Econometrics 116 (2003) 365-386
incorporating coskewness is helpful in explaining the cross-sectional variation of asset
returns". 4
The decay rate maximization criterion also nests Bernoulli's expected log maximization (a.k.a. growth optimal) criterion. An investor who has a target growth rate suitably
close to the maximum feasible expected growth rate has an endogenous degree of risk
aversion slightly greater than 1. As a result, the associated decay rate maximizing portfolio approaches the expected log maximizing portfolio. If the investor's target growth
rate is lower, the investor uses a higher degree of risk aversion, and the associated
decay rate maximizing portfolio is more conservative, with a lower expected growth
rate, but a higher decay rate for the probability of underperforming that target growth
rate (and hence a higher probability of realizing a growth rate of wealth in excess of
that target). The (perhaps unlikely) presence of an unconditionally riskless asset, i.e.
one with an intertemporally constant return, provides a floor on the attainable target
growth rates. When the target growth rate is sufficiently near that floor, the investor's
risk aversion will be quite high, and the associated decay rate maximizing portfolio
will be close to full investment in the unconditionally riskless asset. The relationship
between the target growth rate and the associated (maximum) decay rate of the probability that it will not be exceeded quantifies the tradeoff between growth and shortfall
risk that has concerned analysts studying the expected log criterion.
Exact calculation of the decay rate (or equivalently, the expected power utility)
requires the exact portfolio return process. In practice, the distribution is not exactly
known. Even if its functional form is known, its parameters must still be estimated. To
cope with this lack of exact knowledge, Section 3 adopts the assumption that portfolio
log returns are IID with an unknown distribution, and follows Kroll et a1. (1984) in
estimating expected utility by substitution of a time average for the expectation operator.
The estimated optimal portfolio and endogenous risk aversion parameter are those that
jointly maximize the estimated expected power utility. An illustrative application of this
estimator is included, contrasting decay rate maximization to both Sharpe Ratio and
expected log maximization when allocating funds among domestic industry sectors. In
it, decay rate maximization selects portfolios with higher skewness than Sharpe ratio
maximization does. The IID assumption that underlies the estimator also permits the
use of both a relative entropy minimizing, Esscher transformed log return distribution
and a cumulant expansion to help interpret the empirical findings.
Section 4 summarizes the most important results, and concludes with some good
topics for future research.
2. Porfolio analysis
Following Hakansson and Ziemba (1995, p. 68), the wealth at time T resulting from
investment in a portfolio is Wr= WO I1:=1 Rpt. where Rpl is the gross (hence positive)
4 Hence, it is possible that an asset pricing model incorporating decay rate maximizing investors could
outperform the CAPM, which incorpmhtes Sharpe ratio maximizing investors. This topic is left for another
paper.
--- page 652 ---

Portfolio Choice with Endogenous Utility: A Large Deviations Approach
623
M. Stutzer!Journal of Econometrics 116 (2003) 365-386
369
rate of return between times t - 1 and t from a portfolio p. Note that Wr does not
depend on the length of the time interval between return measurements, but only on
the product of the returns between those intervals. Dividing by WQ, taking the log of
both sides, mUltiplying and dividing the right-hand side by T and exponentiating both
sides produces the alterative expression
(1)
From (1), we see that Wr is a monotone increasing function of the realized time
average of the log gross return, denoted log R p, which is the realized growth rate of
wealth through time T. When the log return process is ergodic in the mean, this will
converge to a number denoted E[logRp), as T -> 00. Accordingly, there was early (and
still continuing) interest in the portfolio choice that maximizes this expected growth
rate, i.e. selects the portfolio argmaxpE[logRp], also known as the "growth optimal"
or "Kelly" criterion. As noted by Hakansson and Ziemba (1995, p. 65) " . .. the power
and durability of the model is due to a remarkable set of properties", e.g. that it "almost
surely leads to more capital in the long run than any other investment policy which
does not converge to it". 5
But maximizing the expected log return often invests very heavily in assets with
volatile returns, which has led several researchers to highlight its substantial downside
performance risks. Specifically, we will now examine the probability of the event that
the realized growth rate of wealth log R p will not exceed a target growth rate log r
specified by the investor or analyst. This is an event that will cause W T in (1) to fail
to exceed an amount equal to that earned by an account growing at a constant rate
log r. The following subsection uses a simple and widely analyzed portfolio problem
to calculate this downside performance risk for the growth optimal portfolio and a
portfolio chosen to minimize it.
2.1. The normal case
A simple portfolio choice problem, used in Browne (1999b), requires choice of a
proportion of wealth p to invest in single stock, whose price is lognormally distributed
at all times, with the rest invested in a riskless asset with continuously compounded
constant return i. In this case, 10gRpI rv IID %(E[logRp), Var[logRp)). We now compute the probability that 10gRp ~ logr. Because the returns are independent, 10gRp rv
% (E[logRp], Var[logRp]/ T). The elementary transformation to the standard normal
variate Z shows that the desired probability is
__
[IOgr - E[IOgR p ]]
Prob[log R p ~ log r) = Prob Z ~
. /
.
V Var[Rp]/ T
(2)
5 See the analysis of Algoet and Cover (1988) and the lucid exposition of Cover and Thomas (1991,
Chapter 15) for more information on the expected log criterion. For a spirited normative defense of this
criterion, see Thorp (1975).
--- page 653 ---

624
M Stutzer
370
M. StutzerlJournal of Econometrics 116 (2003) 365-386
Tn order to minimize (2), i.e. to maximize the complementary probability that
10gRp > logr, one must choose the proportion of wealth p to minimize the expression on the right-hand side of (2). This is equivalent to maximizing -I times this
expression. Independent of the specific value of T, this portfolio stock weight is
E[log R p] - log r
argmax.
(3)
p
JVar[logR p]
Portfolio (3) will differ considerably from the following growth optimal portfolio
arg max E[log R p]
"
(4)
because of the presence of the target log r in the numerator of (3) and the standard
deviation of the log portfolio return in its denominator. Portfolio (3) will also differ
from the following Sharpe Ratio maximizing portfolio:
E[R ] - i
argmax
p
(5)
p JVar[Rp]
because of the presence of the presence of the target log r in (3) in place of the riskless
rate i in (5), and because of the presence of log gross returns in (3) in place of the
net returns used in (5).
It will soon prove useful to reformulate the rule (3) in the following way. Note that
Prob[log R p ~ log r] will not decay asymptotically to zero unless the numerator of (3)
is positive, so we need only consider portfolios p for which
E[log R p] > log r,
(6)
in which case the objective in problem (3) can be equivalently reformulated by squaring, and dividing by 2. The result is the following criterion:
(
)
2
1
E[logR] -logr
arg max D p(log r) == arg max -
p
p
p 2
JVar[logRp]
(7)
Tn order to quantitatively compare criteria (4), (5), and (7), it is useful to follow
Browne (1999b) in using a parametric stochastic stock price process that results in
the stock price being lognormally distributed at all times t, so that 10gRpt '" IID
5(E[logRp], Var[logRp]) as assumed above. Specifically, the stock price S follows
the geometric brownian motion with drift dSIS = m dt + v dW, where m denotes the
instantaneous mean parameter, v denotes the instantaneous volatility parameter, and W
denotes a standard Wiener process. The bond price B follows dBIB = i dt. Denoting
the period length between times t and t + 1 by i::lt, Hull (1993, p. 210) shows that
(8)
(9)
Now substitute Eqs. (8) and (9) into (7), and write down the first-order condition
for the maximizing stock weight p. You can verity by substitution that the following
--- page 654 ---

Portfolio Choice with Endogenous Utility: A Large Deviations Approach
M. Stutzer/Journal of Econometrics 116 (2003) 365-386
p solves it:
arg max D p(log r) =
p
2(log r - i)
v2
Using (8), the growth optimal criterion (4) yields the portfolio
(m - i)
argmaxE[logRp] = --2- '
P
V
625
371
(10)
(11 )
Using Browne's (1999b, p. 77) parameter values m = 15%, v = 30%, i = 7%, and
a target growth rate log r = 8%, the outperformance probability maximizing rule (10)
advocates investing a constant p=47% of wealth in the stock, while the growth optimal
rule (11) advocates p=89%. Of course, (10)'s p=47% minimizes the probability that
the realized growth rate log R p ~ 8%. Fig. I illustrates the phenomena, by graphing
Prob[logRp ~ 8%] for the two portfolios, and a third portfolio with just 33% invested
in the stock. It shows that Prob[log R p ~ 8%] decays to zero for all three portfolios,
but decays at the fastest rate when (IO)'s p=47% is used. Section 2.2 will show that
the rate of probability decay rate in Fig. 1 is Dp(logr) in (7). Fig. I also shows that
even though investors can invest in a riskless asset earning 7%, and can try to beat
the modest 8% target growth rate by also investing in a stock with an instantaneous
expected return of 15%, there is still almost a 20% probability that the investor's
realized growth rate of wealth after 50 years will be less than 8%!
Table I contrasts performance statistics for the outperformance probability maximizing portfolios and the growth optimal portfolio p = 89% over the feasible range of
target growth rates log r. Because the riskless rate of interest is only 7%, the probability of earning more than a target rate log r > 7% is always less than one. If the
target rate log r ~ 7%, the investor could always ensure outperforming that rate by investing solely in the riskless asset. Hence the lower limit of the feasible target growth
rates is the 7% riskless rate. 6 Line 1 in Table 1 shows that 'in order to maximize
the probability of outperforming a target growth rate one basis point higher than this,
i.e. log r = 7.01 %, the investor need invest only p = 5% of wealth in the stock. As a
result of this conservative portfolio, this investor will have a relatively low probability of not exceeding this target; the decay rate of the underperformance probability is
max p Dp(7.01)=3.l9%. But by investing 89% of wealth in the stock, the growth optimal investor will have a higher probability of not exceeding this 7.01 % target, because
its associated decay rate is just 0.88%. This occurs despite its much higher expected
growth rate E[log R p] (10.6% vs. 7.4%) and higher expected net return J1= pm+( 1 - p)i
(14.1% vs. 7.4%). Of course, the major reason for this is its higher volatility (J = pV
(26.7% vs. 1.5%), which increases the probability that a bad series of returns will drive
the growth optimal portfolio's realized growth rate below log r = 7.01 %. Also note in
line 1 that in order to maximize the probability of outperforming the 7.01% target, the
investor must choose a portfolio with a higher expected growth rate (7.4%) than the
target, as explained earlier.
6 Of course, if a riskless rate does not exist, it would not provide a floor on the feasible target rates.
--- page 655 ---

626
372
~
:c
til
~
2
II..
0.5
0.45
0.4
0.35
0.3
0.25
0.2
0.15
M Stutzer!Journal of Econometrics 116 (2003) 365-386
Underperformance Probabilities
log r= 8%
--+-p= 89%
-&-p=33%
-lr-p =47%
M Stutzer
0.1+----+----+----+----+----+----+----+----~--~----~
10
20
30
40
50
60
70
90
90
100
T (years)
Fig. I. The probability of not exceeding the 8% target growth rate approaches zero at a portfolio dependent
rate of decay. The rate of decay is highest for the portfolio with p = 47% invested in the stock.
There is an important tradeoff present in Table 1. Note from columns I and 3
that investors with successively higher growth targets log r have successively lower
underperformance probability decay rates max p D p(log r). This implies that investors
with higher targets will be exposed to a higher probability of realizing growth rates
of wealth that do not exceed their respective targets. This occurs despite the fact that
they did the best they could to minimize the probability of that happening. This is a
consequence of the successively more aggressive portfolios needed to ensure asymptotic
outperformance of their successively higher targets.
This tradeoff is analogous to the tradeoff between mean and standard deviation associated with the efficiency criterion that selects the portfolio with the smallest standard
--- page 656 ---

Portfolio Choice with Endogenous Utility: A Large Deviations Approach
627
M. StutzerlJournal oj Econometrics 116 (2003) 365-386
373
Table I
Perfonnance statistics for the maximum expected log portfolio and maximum decay rate portfolios associated
with feasible target growth rates log r, when portfolios are fonned from a lognonnally distributed stock with
m=15% instantaneous mean return and v=30% instantaneous volatility, and a riskless asset with instantaneous
riskless rate i = 7%
Perfonnance of portfolio (II) vs. portfolio (10)
logr%
Stock weight p%
Dp(logr)%
E[logRp]%
~%
0-%
7.01
89 (5)
0.88 (3.19)
10.6 (7.4)
14.1 (7.4)
26.7 (1.5)
7.5
89 (33)
0.66 (1.39)
10.6 (9.2)
14.1 (9.6)
26.7 (9.9)
8.0
89 (47)
0.46 (0.78)
10.6 (9.8)
14.1 (10.8)
26.7 (14.1)
8.5
89 (58)
0.30 (0.44)
10.6 (10.1)
14.1 (11.6)
26.7 (17.4)
9.0
89 (67)
0.17 (0.22)
10.6 (10.3)
14.1 (12.4)
26.7 (20.1)
9.5
89 (75)
0.08 (0.09)
10.6 (10.5)
14.1 (\3.0)
26.7 (22.5)
10.0
89 (82)
0.02 (0.02)
10.6 (10.5)
14.1 (13.6)
26.7 (24.6)
10.6
89 (89)
0.00 (0.00)
10.6 (10.6)
14.1 (14.1)
26.7 (26.7)
deviation of return, once the investor fixes a mean return. Here, the criterion selects the
portfolio with the highest underperformance probability decay rate, once the investor
fixes a target growth rate. In this way, the tradeoff between logr and maxpDp(logr)
can be thought of as an alternative efficiency frontier, which yields the growth optimal portfolio on one extreme and full investment in the constant interest rate (when
it exists) on the other. The efficiency frontier is graphed in Fig. 2, which shows it to
be a convex curve in this example. In Section 2.2, we will see that this is true more
generally, i.e. with multiple risky assets, whose log returns are not necessarily normal
nor IlD.
Finally, there is just one risky asset used to form the optimal portfolios in Table 1,
so the mean-standard deviation efficiency frontier is just swept out by varying the stock
weight and calculating the mean fJ and standard deviation (J of the net returns. For
comparison purposes, this is reported in the last two columns of Table 1. Reading down
the last three columns of the table, note that the difference between fJ and the expected
growth rate E[log R,,] of wealth grows wider as the standard deviation of portfolio
returns (T gets larger. The mean return increasingly overstates the expected growth
rate of wealth as portfolio volatility increases. This is due to (1); as Hakansson and
Ziemba (1995, p. 69) note, " .. . capital growth (positive or negative) is a multiplicative,
not an additive process".7 Here, due to lognormality, there isa precise relationship
between the two: E[logRpJ = fJ- (J2 j2 (see Hull, 1993, p. 212).
The following section will show that a simple, yet powerful result from large deviations theory permits us to rigorously characterize D p(log r) in Table 1 as the decay rate
of the portfolios' underperformance probabilities graphed in Fig. 1. More importantly,
the result also shows how to correctly calculate the decay rate and associated decay
rate maximizing portfolios when portfolio returns are not lognormally distributed.
7 In this regard, see Stutzer (2000) for a simpler model of fund managers who use arithmetic average net
returns rather than average log gross returns, under the assumption that net returns are lID.
--- page 657 ---

628
374
3.5
3
2.5
<f1.
2
.!
III
a:::
~
CJ
QI
Q
1.5
0.5
M. Stutzer I Journal of Econometrics I16 (2003) 365-386
O+---~----r---4----4----+----+~~~--4
7
7.5
8
8.5
9
9.5
10
10.5
11
Target Growth Rate %
M Stutzer
Fig. 2. The convex tradeoff between the target growth and underperforrnance probability decay rates for the
optimal portfolios in Table I. The convexity is generic.
2.2. The general case
As shown in the last section, when a portfolio's log returns were IID normally
distributed, exact underperformance probabilities of the realized growth rate could
be easily calculated using (2). But it is widely accepted that stock returns are often skewed and leptokurtotic. Even if they weren't, the skewed returns of derivative
--- page 658 ---

Portfolio Choice with Endogenous Utility: A Large Deviations Approach
629
M. StutzerlJournal of Econometrics 116 (2003) 365-386
375
securities like stock options are inherently non-normally distributed. Hence there is
an important need to rank portfolios according to their underperformance probabilities
Prob[log R p ~ log r] in non-lID, non-normal circumstances. It is now shown how to
calculate the decay rate of this probability in more general cases. We will then apply
the general result to prove that D p(log r) in (7) is indeed the correct decay rate for
the lID normal case.
As in the previous section, we seek to rank portfolios p for which the underperformance probability Prob[logRp ~ logr] --> 0 as T --> 00. Calculation of this probability's decay rate D p(log r) is facilitated by use of the powerful, yet simple to apply,
Gartner-Ellis Large Deviations Theorem, e.g. see Bucklew (1990, pp. 14-20). For a
log portfolio return process with random log return 10gRpt at time t, consider the
following time average of the partial sums' log moment generating functions, i.e.:
¢J(8) == lim ~ 10gE[e0L:;=1 logRp,] = lim ~ logE [( WT)O] ,
T->oo T
T->oo T
Wo
(12)
where the last expression is found by usipg (1) to compute WT/Wo = I1 Rpl , substituting 10g(WT/ Wo) for the sum of the logs in (12), and simplifying. Hence (12)
depends on the value of the random WT , and so does not depend on the particUlar
discrete time intervals between the log returns 10gRpt . We maintain the assumptions
that the limit in (12) exists for all 8, possibly as the extended real number +00,
and is differentiable at any 8 yielding a finite limit. From the last expression in (12),
these assumptions must apply to the asymptotic growth rate of the expected power of
Wr/Wo. Some well-analyzed log return processes will satisfy these hypotheses, as will
be demonstrated shortly by example. However, these assumptions do rule out some proposed stock return processes, e.g. the stable Levy processes with characteristic exponent
'1. < 2 and hence infinite variance, used in Fama and Miller (1972, pp. 261-274).
The calculation of the decay rate D p(log r) is the following Legendre-Fenchel transform of (12):
Dp(log r) == max D log r - ¢J(D).
°
(13 )
When log returns are independent, but not identically distributed, (12) specializes to
1 TIT
¢J(8)= lim -
~logE[eOlogR p, ]= lim -T~logE[R~I].
(14)
T->oo T ~
T->oo
~
1= 1
1= 1
When log returns are additionally identically distributed (lID), (12) simplifies to
¢J(D) = 10gE[eBIOgRp] = 10gE[R~],
(15)
which when substituted into (13) yields the decay rate calculation for the IID case.
This result will form the basis for the empirical application in Section 3. It is known
as Cramer's Theurem (Bucklew, 1990, pp. 7-9).
To illustrate these calculations, let us return to the widely analyzed case where the
log portfolio return log R pI is a covariance-stationary normal process with absolutely
summable autocovariances. Then the partial sum of log returns in (12) is also normally
--- page 659 ---

630
M Stutzer
376
M. SlUtzer /Journal of Econometrics 116 (2003) 365-386
distributed. The mean and variance of it can be easily calculated by adapting Hamilton's
(1994, p. 279) calculations for the distribution of the sample mean, i.e. the partial sum
divided by T. One immediately obtains
T
10g(Wr/Wo) == L 10gRpI ,....,.At (TE[logRp), T Covo
t=l
T-l
)
+ ~(T-r)(COVr+COV_ r) ,
(16)
where E[log R p) denotes the log return process' common mean and Cov, denotes its
r-Iagged autocovariance. Formula (12) is the limiting time average of the log moment
generating functions of these normal distributions. Now remember from elementary
statistics that a normal distribution's log moment generating function is linear in its
mean and quadratic in its variance. As a result, use (12) to calculate
,=+00
= E[logRp)8 + L Cov,8 2/2.
(17)
r=-OC)
N ow substitute (17) into (13) and set its first derivative with respect to (J equal to zero
to find that the maximum in (13) is attained by the following maximizer:
8max = (logr - E[logRp)) I:'J;: Cov,.
(18)
Substituting (18) back into (17) and rearranging yields the underperformance probability decay rate
(1
1 (E[IOgR p) _IOgr)2
Dp ogr) =-
2
/",=+00 C
V ~,=-oo OV,
(19)
Note that maximization of the decay rate (19) rewards portfolios with a high expected
growth rate E[logRp) (in its numerator) and a low asymptotic variance 2:::~: Cov, ==
limT--->oo Var[log(Wr/Wo»)/T (in its denominator). This differs from the criterion in
Bielecki et al. (2000), which is approximately the asymptotic expected growth rate
minus a mUltiple of the asymptotic variance. For the lID case used in Section 2.1,
all covariance terms in (19) are zero except Covo == Var[logRp), so the decay rate
function (19) reduces to the expression (7) used in Section 2.1 and Table 1. Fig. 3
depicts this decay rate function over a range of log r, for each of the three portfolios
whose underperformance probabilities are graphed in Fig. 1. There, we see that the
portfolio p = 47% from (10) does indeed have the highest decay rate when log r = 8%.
--- page 660 ---

Portfolio Choice with Endogenous Utility: A Large Deviations Approach
631
M. Stutzer!Journal of Econometrics I/6 (2003) 365-386
377
Underperformance Probability Decay Rates
1.00%
-+-p=89%
-I!J-p=33%
0.90%
-6-p=47%
0.80%
0.70%
0.30%
0.20%
0.10%
0.00%
~
?ft
?ft
?ft
~
~
?ft
~
~
~
~
.
.
.
0
'"
0
'"
0
'"
0
'"
0
'"
0
0
C\I
'"
'"
0
C\I
'"
.....
0
N
'"
cO
a:i
cO
to
oj
oj
oj
oj
0
0
g
~
Target Rate log(r)
Fig. 3. The decay rate function Dp(log r) is convex, with a minimum at log r = E[log R p]. The portfolio
p = 47% attains the highest decay rate when log r = 8%.
Note that the decay rate function D p(log r) in (19) for a covariance stationary Gaussian portfolio log return process is non-negative, and is a strictly convex function of
log r, achieving its global minimum of zero at the value log r = E[log R pl. These
properties are true for more general processes (for a discussion, see Bucklew, 1990).
As a result, remember from (6) that the decay rate criterion ranks portfolios with
E[logRp] > logr, and apply the envelope theorem to the general rate function (13) to
yield
dDp(logr)
a
.
d I
= -::'-1 -
max Blogr - c/J(B) = Bmax < 0
ogr
v ogr
{/
(20)
--- page 661 ---

632
M Stutzer
378
M. Stutzer!Journal of Econometrics 116 (2003) 365-386
as seen in the special case (18). Now differentiate (20) to find
dD~(Iog r)
dtJmax
--"--..:.".- = -- > 0
d log r2
d log r
(21 )
due to convexity of Dp(logr). Again due to the envelope theorem, (20) and (21) continue to hold for max p D p(log r) as well. Fig. 2 depicts the convexity of max p D p(log r)
over the relevant range of log r in the example of Table 1.
2.3. Analogy with power utility
The general decay rate criterion is a generalization of the expected power utility
criterion. To uncover the generalization, substitute the right-hand side of (12) into
(13), to derive
max Dp(log r) == max max 810g r -
lim ~ logE [( WT)II]
p
p
()
T->oo T
Wo
=maxmaxlogrB -
lim ~logE [(WT)B]
p
B
T-+oo T
Wo
= max max -
lim 2. logE [( WTT)O] ,
P
()
T-+oo T
Wor
(22)
which yields the following large T approximation:
(23)
where we write 8max(P) in (23) to stress dependence (through the joint maximization
(22» of tJ on the portfolio p. The left-hand side of (23) increases with D p' so a large
T approximation of the portfolio ranking is produced by use of the expected power
utility on the right-hand side of (23).
There are both similarities and differences between the right-hand side of (23) and a
conventional expected power utility E[ - (WT )BJ.. From (20), 8max(P) < O. Evaluating
it at the investor's decay rate maximizing portfolio p, note that the power function
in (23) with the form U = -(. YJm",(P) increases toward zero as its argument grows
to infinity, is strictly concave, and has a constant degree of relative risk aversion
y == 1 - 8max(P) > 1. Furthermore, 8max(P) < 0 implies that the third derivative of U
is positive, so the criterion exhibits positive skewness preference. But there are two
important differences between the concepts. First, the argument of the power function
in (23) is altered; it is the ratio of invested wealth to a "benchmark" level of wealth
accruing in an account that grows at the geometric rate r. While absent from traditional criteria, this ratio is also present in other non-standard criteria, such as Browne's
(1999a, p. 276) criterion to "maximize the probability' of beating the benchmark by
some predetermined percentage, before going below it by some other predetermined
--- page 662 ---

Portfolio Choice with Endogenous Utility: A Large Deviations Approach
633
M. Stutzerllournal of Econometrics 116 (2003) 365-386
379
percentage". Browne (1999a, p. 277) notes that " ... the relevant state variable is the ratio of the investor's wealth to the benchmark". 8 Second, conventional portfolio theory
assumes that the risk aversion parameter () is a preference parameter that is independent
of the investment opportunity set. But in (23), () = ()max (p) is detennined by maximization, and hence is not independent of the investment opportunity set. Investors could
utilize different investment opportunity sets, either because of differential regulatory
constraints, such as hedge funds' greater ability to short sell, or because of different
opinions about the parameters of portfolios' log return processes. When this happens,
investors will have different decay rate maximizing portfolios p, and different degrees
of risk aversion y = 1 - ()max(P), even if they have the same target growth rate logr.
Assuming that asset returns are generated by a continuous time, correlated geometric
Brownian process, Browne (1999a, p. 290) compares the fonnula for the optimal portfolio weights resulting from his criterion, to the fonnula resulting from conventional
maximization of expected power utility at a fixed tenninal time T. In this special case,
he finds that the two fonnulae are isomorphic, i.e. there is a mapping between the
models' parameters that equates the two fonnulae. He concludes that "there is a connection between maximizing the expected utility of tenninal wealth for a power utility
function, and the objective criteria of maximizing the probability of reaching a goal, or
maximizing or minimizing the expected discounted reward of reaching certain goals".
Connection (23) between decay rate maximization and expected power utility is quite
specific, yet does not depend on a specific parametric model of the assets' joint return
process.
Critics such as Bodie (1995, p. 19) have argued that "the probability of a shortfall
is a flawed measure of risk because it completely ignores how large the potential
shortfall might be". It is possible that this is a fair assessment of expected power
utility maximization of wealth at a fixed horizon date T, subject to a "Value-At-Risk"
(VaR) constraint that fixes a low probability for the event that tenninal wealth could
faIl below a fixed floor. This problem was intensively studied by Basak and Shapiro
(2001, p. 385), who concluded that "The shortcomings ... stem from the fact that the VaR
agent is concerned with controlling the probability of a loss rather than its magnitude".
They proposed replacing the VaR constraint with an ad hoc expected loss constraint,
resulting in fewer shortcomings. The investor's target growth rate serves a similar
function in the horizon-free, unconstrained criterion (22).
3. Non-parametric implementation
Tn the TID case, there is a simple, distribution-free way to estimate D p(log r) for a
portfolio p. Following the comparative portfolio study of Kroll et al. (1984), we replace
the expectation operator in (15) by an historical time average operator, substitute into
( 13), and numerically maximize that. 9 This estimator eliminates the need for prior
8 While Browne considers a stochastic benchmark, the constant growth benchmark here can be modified
to consider an arbitrary stochastic benchmark, at the cost of fewer concrete expository results.
9 It is important to remember that the log moment generating function of the log return distribution
necessarily has to exist near Ilrnax in order for this technique to work here.
--- page 663 ---

634
M Stutzer
380
M. StutzerlJournal of Econometrics 116 (2003) 365-386
knowledge of the log return distribution's functional fonn and parameters. Specifically,
let Rp(t)= L;=o pjRj(t) denote the historical return at time t of a portfolio comprised
of n+ 1 assets with respective returns Rj(t), with constantly rebalanced portfolio weights
Lj Pj = 1. The estimator is
If,(log r) ~ m;x e log r - log [ ~ t (t, PjRj(')) l
(24)
and the optimal portfolio weights are estimated to be
jJ = arg max max () log r
PI ,···.P"
(J
(25)
The maximum expected log portfolio was similarly estimat"ed, by numerically finding
the weights that maximize the time average of 10gRp(t).
Let us now contrast the estimated decay rate maximizing portfolio (25) to both
the expected log and Sharpe ratio maximizing, constantly rebalanced portfolios fonned
from Fama and French's 10 domestic industry, value-weighted assets,1O whose annual
returns run from 1927 through 2000. The sample cross-correlations of the 10 industries' gross returns range from 0.32 to 0.86, suggesting that diversified portfolios of
them will provide significant investor benefits. The sample covariance matrix is invertible, pennitting estimation of the Sharpe ratio maximizing "tangency" portfolio, by
mUltiplying this inverse by the vector of sample mean excess returns over a riskless
rate, and then nonnalizing the result. We assume that it was possible to costlessly
store money between 1927-2000, with no positive constant nominal rate riskless asset
available. 11 Hence we assume a zero constant riskless rate when computing the Sharpe
ratio maximizing tangency portfolio of the 10 industry assets.
The results are seen in Table 2.
The perfonnance statistics in Table 2 show that the Sharpe ratio maximizing portfolio
has almost no skewness. But the decay rate maximizing portfolios all have a skewness
of about 1, as does the expected log maximizing portfolio. This reflects the skewness
preference inherent in the generalized expected power utilities with degrees of risk
aversion greater than (in the log case, equal to) one. 12 In fact, these investors prefer
all odd order moments and are averse to all even order moments. To see this, note
that (15) is the cumulant generating function for the (assumed) TID log portfolio return
10 The data are currently available for download from a website maintained by Kenneth French at MIT.
II Treasury Bills are not a constant rate riskless asset, like the one used to form portfolios in Section 2.1.
A fixed percentage of wealth invested in Treasury Bills is just like any other risky asset.
12 See Kraus and Litzenberger (1976) and Harvey and Siddique (2000) for evidence that investors prefer
skewness.
--- page 664 ---

Portfolio Choice with Endogenous Utility: A Large Deviations Approach
635
M. Stutzerllournal of Econometrics 116 (2003) 365-386
381
Table 2
Comparison of estimated Sharpe ratio, expected log, and decay rate maximizing portfolios from Fama-French
10 industry indices, 1927-2000
Industries
Asset moments
Portfolio weights
Max
logr
logr
logr
Max
J.I.
(J
Skewness
Sharpe
5%
10%
15%
Log
NoDur
0.130
0.198
-0.12
0.80
0.92
1.0
1.11
1.15
Durbl
0.166
0.328
0.86
-0.01
0.27
0.52
0.97
1.22
Oil
0.137
0.220
0.01
0.75
0.77
0.96
1.24
1.36
Chems
0.146
0.225
0.63
0.14
0.35
0.52
0.89
1.15
Manuf
0.136
0.254
0.21
0.03
-0.10
0
0.11
0.20
Telcm
0.123
0.200
0.07
0.35
0.48
0.38
0.30
0.28
Utils
0.118
0.225
0.25
0.05
-0.20
-0.34
-0.61
-0.76
Shops
0.141
0.256
- 0.25
- 0.13
- 0.44
- 0.60
- 0.96
-1.2
Money
0.142
0.245
- 0.43
-0.23
-0.20
0.07
0.48
0.70
Other
0.106
0.242
- 0.04
- 0.76
- 0.86
- 1.5
-2.52
-3.09
Performance statistics
Mean
0.148
0.162
0.195
0.248
0.278
Std. dev.
0.153
0.181
0.240
0.368
0.446
Skewness
-0.02
1.05
1.07
1.06
1.05
Decay rate D pClog r)
0.18
0.04
0.004
0
Risk aversion I - emax Cp)
5.3
2.5
1.3
I
distribution. Substituting it into (J 3) and evaluating it at 8max (p) yields the following
cumulant expansion:
~Ki
i
- ~
~Umax (P)'
l.
i=3
(26)
which uses the facts that E[log R p] is the first cumulant of the log return distribution and
that Var[log R p] is its second cumulant, while Ki denotes its ith order cumulant. Because
8max(P) < 0, we see that the decay rate increases in odd-order cumulants and decreases
in even-order cumulants. With normally distributed log returns, all the cumulants in the
infinite sum are zero. But with non-normally distributed returns, increased skewness will
increase the decay rate (due to K3)' The relative weighting of the mean, variance and
skewness in (26) is determined by their sizes, the sizes of the higher order cumulants,
the target growth rate log r, and the value of Umax(P) < 0 associated with log r.
The top panel of Table 2 contains the 10 industry weights in each portfolio. As is
typical of estimated Sharpe ratio maximizing portfolios with more than a few assets, it
is heavily long in just three industries (Non-durables, Oil, and Telecommunications).
The decay rate maximizing portfolio for the target growth rate log r = 0.10 is also
heavily invested in these industries, but in addition it has considerable long positions
in the two most positively skewed industries (Durables and Chemicals). The Sharpe
--- page 665 ---

636
M Stutzer
382
M. Stutzer /Journal oj Econometrics 116 (2003) 365-386
ratio maxlmlzmg portfolio is heavily short in one industry (Other). The decay rate
maximizing portfolios are heavily short in both this industry and as well as two others
(Shops and Utilities). The differences between Sharpe ratio and decay rate maximizing
portfolios are due to the presence of the target growth rate in decay rate maximization,
its use of log gross returns rather than net returns when calculating portfolio means
and variances, and the presence of higher order moments. It is difficult to assess the
impact of higher order moments on the differences in portfolio weights. Bekaert et aI.
(1998, p. 113) were able to produce only a two percentage point difference in an asset
weight, when simulating the effects of its return's skewness over the range -1 to 2.0,
on the portfolio chosen by an expected power utility maximizing agent whose degree
of risk aversion was close to 10. This suggests that the use of a target growth rate, and
the use of log gross returns rather than arithmetic net returns, account for most of the
differences between the decay rate and Sharpe ratio maximizing portfolios' weights.
The convergence of decay rate maximizing portfolios to the expected log maximizing
portfolio is seen when reading across the last four columns of Table 2. The last two
rows in the bottom panel of Table 2 show the relationship between the target growth
rates, their respective efficient portfolios' maximum decay rates, and their respective
endogenous degrees of risk aversion. Despite the fact that 8max(P) is determined by
maximization in (25), we see that the degree of risk aversion 1 -
f)max(P) is not
unusually large in any of the decay rate maximizing portfolios tabled, 13 and converges
toward 1 as log r --> maxp E[logRp). An alternative interpretation of this is enabled by
computing the first order condition for 8max(P) in the IID case. To do so, substitute
(15) into (13) and differentiate to find
E [IOgR p :;] = logr,
(27)
where the Esscher transformed probability density
dQ
Ro,;"(P)
dP = E[R~m"( ")]
(28)
is used to compute the expected log return (i.e. growth rate) in (27). 14 Furthermore, a
result known as Kul\back's Lemma (1990) shows that the Esscher transformed density
(28) is the solution to the following constrained minimization of relative entropy, whose
minimized value is the decay rate, i.e.
[dQ
dQ]
D p(log r) = min E dP log dP s.t. (27).
(29)
From (27), an efficient portfolio has the highest decay rate among those with a
fixed transformed expected growth rate equal to logr. As logr -4 maxpE[logRp),
13 Of course, it can get unusually large when the target growth rate is unusually low, i.e. when the investor
is unusually conservative.
14 See Gerber and Shiu (1994) for option pricing fonnula derivations that use the Esscher transfonn to
calculate the risk-neutral density required for option pricing.
--- page 666 ---

Portfolio Choice with Endogenous Utility: A Large Deviations Approach
637
M. S{u{zer /Journal of Econometrics 116 (2003) 365-386
383
0.4
Underperformance Probabilities
0.35
0.3
0.25
~
:0
0.2
«I
.J:l
0 ...
Q.
0.15
0.1
Tyears
Fig. 4. Bootstrap estimated underperformance probabilities for portfolios in Table 2, when log r = 10%.
f}max( p) --> 0, density (28) concentrates at unity and the minimal relative entropy in
(29) approaches zero, i.e. the transformed probabilities approach the actual probabilities.
As a result, the transformed expected log return in (27) approaches the actual expected
log return, so constraint (27) collapses the portfolio constraint set onto the log optimal
portfolio.
In order to determine if a decay rate maximizing portfolio in Table 2 will have
lower underperformance probabilities than the Sharpe ratio and expected log maximizing portfolios do, the probabilities were estimated by resampling the portfolios' log
returns 5000 times for each investment horizon length T, and then tabulating the empirical frequency df underperformance for each T. The results for the target decay rate
