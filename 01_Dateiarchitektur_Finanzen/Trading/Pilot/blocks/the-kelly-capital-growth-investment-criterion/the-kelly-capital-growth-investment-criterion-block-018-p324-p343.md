# The Kelly capital growth investment criterion _ theory and -- Leonard C_ Maclean, Edward O_ Thorp, W_ T_ Ziemba, Leonard -- World Scientific Handbook -- isbn13 9781283148344 -- bec576e26410d0c695fd5b867d08ec4f -- An.pdf — pages 324–343

--- page 324 ---

Application of the Kelly Criterion to Ornstein-Uhlenbeck Processes
297
Application o/the Kelly Criterion to Ornstein-Uhlenbeck Processes
In conclusion this article gives a quantitative insight into the trade-off between risk
and return as diversification opportunities are added, correlation structure changed,
and other constraints modified.
Acknowledgements. YL expresses his thanks to one of his dearest friends, Huiqing
Chen, for her kind encouragement and support. BKM acknowledges support from the
NSF of China and multiple informative discussions with DC Brody and 0 Peters.
References
I. Kelly, l L.: A New Interpretation of Information Rate. Bell System Technical Journal. 35,
917 --926 (1956)
2. Thorp, E.O.: The Kelly Criterion in Blackjack, Sports Betting, and the Stock Market. The
10th International Conference on Gambling and Risk Taking (1997)
3. Breiman, L.: Optimal Gambling Systems for Favorable Games. Jerzy Neyman, Proceedings
of the Berkeley Symposium on Mathematical Statistics and Probability. 1, 65-78 (1961)
4. Kargin, V.: Optimal Convergence Trading, arXiv: math.OC/0302l04 (2003)
5. Musiela, M., Rutkowski, M.: Martingale Methods in Financial Modelling. Springer, New
York (1997)
6. Karatzas, I., Shreve, S.: Brownian Motion and Stochastic Calculus. Springer, Heidelberg
(1998)
7. Lv, Y., Meister, B.K., Peters, 0 .: Implications of the Kelly Criterion for MUltiple Ornstein-
Uhlenbeck Processes, Bachelier Finance Society Fifth World Congress (2008)
8. Hakansson, N.H.: On Optimal Myopic Portfolio Policies, with and without Serial
Correlation of Yields , Journal of Business 44,324-34 (1971)
13
--- page 325 ---

This page is intentionally left blank
--- page 326 ---

Part III
The relationship of Kelly to asset
allocation
--- page 327 ---

This page is intentionally left blank
--- page 328 ---

22
Introduction to the Relationship of Kelly Optimization to
Asset Allocation
301
The Kelly growth optimum approach is an attractive formula for investing. If the
formula is robust and can be adapted to include realistic constraints on investing,
then the practicality of the method is clear. The various papers here discuss these
issues including liabilities, fractional Kelly, benchmarks, fixed mix strategies, and
volatility induced wealth growth.
The first paper discusses asset allocations with withdrawals. Browne (1997) analyzes the optimal behavior of an investor (or pension fund manager) who withdraws
funds continuously at a fixed rate per unit time. The investor can allocate funds to
a given number of risky assets whose prices follow geometric Brownian motion and
a risk free asset with a known constant rate of return. He shows that there are safe
and risky zones with the latter being a region with a positive probability of ruin and
the former where there is no chance of bankruptcy with those asset allocations. It
is not possible to reach the safe region with probability one before bankruptcy or to
determine an optimal policy to reach an upper level before a given lower level. But
the safe region can be reached (optimized) with E-optimality. Brown then finds the
optimal growth policy for safe zone investors, which is a E log (Kelly) maximizing
policy where the investor invests a constant proportion of wealth above a stochastic
target floor in a form of constant proportions portfolio insurance.
The next two papers discuss fractional Kelly strategies. MacLean, Ziemba and
Blazenko (1992) discuss growth versus security tradeoffs in dynamic investment
analysis. We know that the E log maximizing strategies have the highest asymptotic
long term growth rates. This approach is combined with the maximal security
literature of Ferguson (1965), Epstein (1977), and Feller (1962). They propose
three growth measures and three security measures. The growth measures are:
(1) The mean accumulation of wealth at the end of time t, that is how much do we
expect to have, on average, after t periods.
(2) The mean exponential growth rate and its limit as t ----> 00 .
(3) The mean first passage time to reach the set [U, (0), that is, how long on average
does it take the investor to reach a specific level of wealth.
The measures of security are:
(1) The probability that the investor will have a specific accumulated wealth at
time t, that is what are the chances of reaching a given target in a fixed amount
of time.
--- page 329 ---

302
L. C. MacLean, E. 0. Thorp and W. T. Ziemba
(2) The probability that the investor's wealth is above a specified path.
(3) The probability of reaching a goal U which is higher than the initial wealth Yo
before falling to a wealth level L below Yo.
MacLean et al. study growth-security efficiency analgously to mean-variance
efficiency as well as the weaker conditions of growth-security monotonicity. This
latter tradeoff is called effective. They show that fractional Kelly strategies trace
out effective growth-security tradeoffs. Later in MacLean, Ziemba, and Li (2005),
it is shown that these fractionally Kelly strategies are efficient, if the assets are
log-normally distributed, so they maximize growth for any given security level. The
analysis leads to simple two dimensional graphs that compare growth rates with the
probability of achieving a higher goal before falling to a lower level. Applications
are made to blackjack, horse racing , lotto games, and futures trading. This range
of applications runs the full range of asset weights from very small to very large
percentages of the investor's wealth.
MacLean, Sanegre, Zhao, and Ziemba (MSZZ) (2004) provide an approach to
calculate the optimal fractional Kelly weights at discrete intervals of time. The idea
is to maximize the expected log subject to being above a specified wealth path with
high probability. This is a value at risk type of constraint and leads to a model
where a modified Kelly strategy can be computed at the discrete intervals of the
planning horizon. This strategy is not necessarily fractional Kelly. In general, as
risk rises, the expected return will fall so there is an effective tradeoff. With geometric Brownian motion in continuous time, fractional Kelly is optimal for the value
at risk (VaR) and conditional value at risk (CVaR) where returns in the VaR tails
are lineraly penalized constraints. The algorithm proposed uses a disjunctive form
for the probabilistic constraints which identifies an outer problem of choosing an
optimal set of scenarios and an inner (conditional) problem of finding the optimal
decisions for a given discrete scenario set. The multiperiod inner problem is composed of a sequence of conditional one period problems. The theory is illustrated
for the dynamic allocation of wealth in stocks, bonds and cash.
There are two ways to model the application, maximize the expected log of final
wealth subject to
(1) wealth being above the specified wealth path with high probability; and
(2) a secured annual drawdown with a drawdown amount and a security level both
exogenously specified.
The VaR model only controls loss at the horizon but not at intermediate decision
points. The more stringent risk control constraint in the drawdown model considers
the loss in each period.
At low levels of risk control, the full Kelly strategy is optimal. As the risk control
requirements are raised, the strategy becomes more conservative, especially when
close to the planning horizon. Assets are assumed to be log-normally distributed
with geometric random walk but the computational procedure is general and applies
to general price distributions.
--- page 330 ---

Introduction to the Relationship of Kelly Optimization to Asset Allocation
303
In an extension, MacLean, Zhao, and Ziemba (2009) add one more feature to
the MSZZ model, namely that when the predetermined exogenous path is violated,
there is a convex penalty for there shortfall violations (see Mulvey, Bilgili, and Vural
(2010) in part VI for an application along these lines).
The next three papers discuss the impact of benchmarks. Browne (2000) considers a dynamic portfolio management problem where the objective concerns the
tradeoff of performance goals and the risk of a shortfall below a benchmark target.
Return is measured by the expected time to reach investment goals relative to the
benchmark. This return is maximized subject to the risk constraint in terms of the
probability of shortfall relative to the benchmark. The setting is Merton's (1971)
continuous time framework.
Davis and 11eo (2009) extend the definition of fractional Kelly strategies to the
situation in which the investor's objective is to outperform a benchmark. These
benchmarked fractional Kelly strategies are efficient portfolios even when the asset
returns are not log-normally distributed. They find the benchmarked fractional
Kelly strategies for various types of benchmarks such as the S&P500 and the Salomon Smith Barney World Government Bond Index. They also determine the relations between the investor's risk aversion and the given benchmarks. The setting
is a stochastic control model in continuous time. They develop, following Merton,
two and three mutual fund theorems. This means that the optimal weights over n
assets can be found by optimally weighting the two or three mutual funds which are
linear combinations of the original n assets, where n > 3, see Rudolf and Ziemba
(2004) for a four mutual fund theory with liabilities in part VI; see also Davis and
11eo (2008a,b). In addition to single index benchmarks, there can be composite
benchmarks plus alpha or composite weighted multiple index benchmarks with or
without an alpha.
The Davis and 11eo two fund theorem for the case without and with benchmarks
is that the assets can be split between the full Kelly portfolio and a correction
portfolio C with the weights dependent on the investor's risk sensitivity. C is
an intertemporal hedging portfolio, which can be the risk free asset under certain
assumptions. They develop a three mutual fund theorem for the case of benchmarks
with risky and risk free assets. Formulas are developed for the optimal equity
portfolio weightings in the various mutual funds.
Any portfolio can be expressed as a linear combination of a mutual fund, an
index fund and a long-short hedge fund with risky and risk free asset allocations.
Again, the weights are dependent on the risk sensitivity. The risk sensitivity varies
from zero (the full Kelly expected log case) to infinity where the investor replicates
the benchmark with an index fund. With moderate risk sensitivity there will be a
blend of all three asset funds.
Platen (2010) discusses the benchmark approach for dynamic investing and pricing. A numeraire portfolio exists which is strictly positive that makes all benchmarked nonnegative portfolios downward trending or trendless. The benchmark
--- page 331 ---

304
L. C. MacLean, E. 0. Thorp and W T. Ziemba
portfolio is the Kelly E log maximizing portfolio which cannot be outperformed by
another long only portfolio. The benchmark portfolio can be used for pricing and
computing conditional expectations.
The final paper in this part deals with fixed-mix and volatility induced wealth
growth. Dempster, Evstigneev, and Schenk-Hoppe (2009) discuss the literature concerning the growth of wealth over time through volatility using fixed-mix strategies.
These self-financing strategies rebalance the portfolio at each decision point to keep
constant the proportions of wealth invested in various assets. Through volatility,
the portfolio will gain wealth even with assets that do not have strictly positive
means. This is a generalization of the buy-low sell-high investment strategy. But
they show that there is much more to the story than this implies. The analysis does
not need utility assumptions and compares the fixed-mix rebalancing with buy and
hold strategies. The key assumption is that the period by period returns of the various assets are stationary. Dempster, Evstigneev, and Schenk-Hoppe discuss some
counter-intuitive examples such as growth with assets having zero means. They
discuss the effects of transaction costs on their results and determine conditions for
growth to occur with sufficiently small transaction costs. They also show that the
conjecture, the higher the volatility, the higher the induced growth rate is not true
in general. The key idea is to rebalance to an arbitrary fixed mix portfolio.
--- page 332 ---

This page is intentionally left blank
--- page 333 ---

This page is intentionally left blank
--- page 334 ---

MATHEMATICS OF OPERATIONS RESEARCH
23
Vol 22, No 2, May 1997
Pmucdlll USA
SURVIVAL AND GROWTH WITH A LlABILITY: OPTIMAL
PORTFOLIO STRATEGIES IN CONTINUOUS TIME
SID BROWNE
We siudy the optimal behavior of an investor who is forced to withdraw funds continuously
at a fixed rate per unit time (e.g., to pay for a liability, to consume, or to pay dividends). The
investor is allowed to invest In any or all of a given number of risky stocks, whosc prices
follow geometnc Brownian motion, as well as in a nskless asset which has a constant rate of
return. The fact that the withdrawal is continuously enforced, regardless of the wealth level,
ensures that there IS a region where there is a positive probability of ruin. In the complementary region ruin can be avoided with certainty. Call the former region the danger-zone and
the latter region the safe-region. We first consider the problem of maximizing the probability
that the safe-region is reached before bankruptcy, which we caU the survival problem. While
we show, among other results, that an opltmal policy does not eXIst for this problem. we are
able to construct explicit f-optimal policies, for any E > O. In the safe-region, where ultimate
survival is assured, we turn our attention to grm'1h. Among other results, we find the optimlli
growth poitcy for the Investor, i.e., the pohcy which reaches another {higher valued} goal as
quickly as possible. Other varIants of both the survival problem as well as the growth problem
are also discussed. Our results for the latter are Intimately related to the theory of Constant
Proportions PortfolIo Insurance.
307
1.
Introduction. The problem considered here is to solve for the optimal investment decision of an investor who must withdraw funds (e.g., to pay for some liability
or to consume) continuously at a given rate per unit time. Income can be obtained
only from investment in any of n + 1 assets: II risky stocks, and a bond with a
deterministic constant return. The objectives considered here relate solely to what
can be termed "goal problems," in that we assume the investor is interested in
reaching some given values of wealth (called goals) with as high a probability as
possible and/or as quickly as possible.
The fact that the investor must continuously withdraw funds at a fixed rate
introduces a new difficulty that was not present in the previous studies of objectives
related to reaching goals quickly (cf. Heath et al. 1987). Specifically the forced
withdrawals ensure that at certain levels of wealth, there is a positive probability of
going bankrupt, and thus the investor is forced to invest in the risky stocks to avoid
ruin. In this paper we address the two basic problems faced by such an investor: how
to survive, and how to grow. The survival problem turns out to be somewhat tricky, in
that we prove that no fully optimal policy exists. Nevertheless, we are able to
construct e-optimal policies, for any e > O. The growth problem is answered completely, once the survival aspect is clarified.
While this model is directly applicable to the workings of certain economic
enterprises, such as a pension fund manager with fixed expenses that must be paid
continuously (regardless of the level of wealth in the fund), our results are also
related to investment strategies that are referred to as Constant Proportion Portfolio
Received January 11, 1995; reVised October 3,1995; July 20,1996.
AMS 1991 subject claSSIfication. Primary: 90A09, 60HlO; Secondary: 93E20, 60G40, 60J60.
OR/MS Index 1978 subject classificallon. Primary: Finance/Portfoho; Secondary: Optimal controljStochastic.
Key words. Stochastic control, portfolio theory, diffuSions, martingales, bankruptcy, optimal gambling,
Hamilton-Jacobi-Bellman equatIOns, portfolio insurance.
468
0364-765X/97/2202/0468/$05.00
CopYflght S 1997, lnc;htutc for Opera lion!!. Rt'-.c.tTch and the Managcmt:nl SClencc'!'
--- page 335 ---

308
S. Browne
OPTIMAL PORTFOLIO STRATEGIES
469
Insurance (eppI). In fact a related model was used as the economic justification of
epPl in Black and Perold (1992), where both the theory and application of such
strategies is described. In Black and Perold (1992), optimal strategies were obtained
for the objective of maximizing utility of consumption, for a very specific utility
function, subject to a minimum consumption constraint. However, the analysis and
policies of Black and Perold (1992) are relevant only when initial wealth is in a
particular region (specifically, when initial wealth is above the "floor"), wherein for
that policy, there is no possibility of bankruptcy. Black and Perold (1992) did not
address the fact that for the model described there, ruin, or bankruptcy, is a very real
possibility when initial wealth is in the complementary region (below the "floor").
Here we focus on the objectives of survival and growth, which are intrinsic
objective· criteria that are independent of any specific individual utility function. As
such, our results for both aspects of the problem will therefore complement the
results of Black and Perold (1992) (as well as the more recent related work of Dybvig
1995). Firstly, the survival problem has not been addressed before for this model
(although see Majumdar and Radner 1991 and Roy 1995), and secondly, the optimal
growth policies we obtain provides another objective justification for the use of the
epPI policies prescribed in Black and Perold (1992), since for this problem we get
similar policies as those obtained there.
The remainder of the paper is organized as follows: In the next section, we will
describe the model in greater detail, and prove a general theorem in stochastic
control from which all our subsequent results will follow. To facilitate the exposition,
we will at first consider the case where there is only one risky stock and where the
withdrawal rate is constant per unit time. It turns out that the state space (for wealth)
can be divided into two regions, which we will call the "danger-zone" and the
"safe-region." In the latter region. the investor need never face the possibility of ruin,
and so we can concentrate purely on the growth aspects of the investor. (The
aforementioned studies of Black and Perold 1992 and Dybvig 1995 considered only
this region in their analyses of the maximization of utility from consumption problem.)
In the former region, ruin, or bankruptcy, is a possibility (hence the term "dangerzone") and therefore we first concentrate on passing from the danger-zone into the
safe-region. This is the survival problem and it is completely analyzed in §3. In
particular, two problems are considered, maximizing the probability of reaching the
"safe-region" before going bankrupt, and minimizing the discounted penalty that must be
paid upon reaching bankruptcy. It is the former problem that does not admit an
optimal policy, although we are able to explicitly construct an e-optimal policy. The
latter problem does admit an optimal policy, which we find explicitly. The structure of
both policies are quite similar, in that they both essentially invest a (different)
proportional amount of the distance to the safe-region. In §4 we consider the growth
problem in the safe-region. We define growth as reaching a given (high) level of
wealth as quickly as possible. Two related problems are then solved completely. First,
we find the policy that minimizes the expected time to the (good) goal, and then we find
the policy that maximizes the expected discounted reward of getting to the goal. Our
resulting optimal growth policies turn out to be quite similar to the epPI policies
obtained for a different problem by Black and Perold (1992), in that they invest a
(different) proportional amount of the distance from the danger-zone. Extensions to
the multiple asset case as well as the case of a wealth-dependent withdrawal rate are
discussed in §§5 and 6.
All the control problems considered in this paper are special cases of a particular
general control problem that is solved in Theorem 2.1 in §2 below. For this problem
we use the Hamiiton-lacobi-Bellman (H1B) equations of stochastic control (see, e.g.,
Fleming and Rishel 1975, or Krylov 1980) to obtain a candidate optimal policy in
--- page 336 ---

Survival and Growth with a Liability: Optimal Portfolio Strategies in Continuous Time
309
470
s. BROWNE
terms of a candidate value function and this value function is then in turn given as the
solution to a particular nonlinear Dirichlet problem. These candidate values are then
verified and rigorously proved to be optimal by the martingale optimality principle (see
§V.lS in Rogers and Williams 1987, or §2 in Davis and Norman 1990). The resulting
nonlinear differential equations are then solved in turn for each of the problems
considered below, yielding the optimal solutions in explicit form.
2. The model and continuous-time stochastic control. Without loss of generality,
we assume that there is only one risky stock available for investment (e.g., a mutual
fund), whose price at time t will be denoted by Pl. {Extension to the multidimensional case (for a complete market) is quite straightforward, and since the excess
notation required adds little to the understanding, we will simply outline how to
obtain the results for the multidimensional case in a later section.) As is quite
standard (see, e.g., Merton 1971, 1990, Davis and Norman 1990, Black and Perold
1992, Grossman and Zhou 1993, Pliska 1986), we will assume that the price process of
the risky stock follows a geometric Brownian motion, i.e., P, satisfies the stochastic
differential equation
( 1)
where f.L and 0" are positive constants and {I¥,: t :?: O} is a standard Brownian motion
defined on the complete probability space (0,7, P), where {9;} is the P-augmentation of the natural filtration 9;w := O"{J¥.; °
::S: s ::S: f}. (Thus the instantaneous return
on the risky stock, dPtl PI' is a linear Brownian motion.)
The other investment opportunity is a bond, whose price at time t is denoted by Bt •
We will assume that
(2)
where r > O. To avoid triviality, we assume f.L > r.
We assume, for now, that the investor must withdraw funds continuously at a
constant rate, say e > 0 per unit time, regardless of the level of wealth. (This would
be applicable for example if the investor faces a constant liability to which $e must be
paid continuously.) In a later section we generalize this to a case where the
withdrawals are wealth-dependent.
Let It denote the total amount of money invested in the risky stock at time t under an
investment policy f. An investment policy f is admissible if {f" t :?: O} is a measurable,
{9;}-adapted process for which /[f/ dt < co, a.s., for every T < co. Let :9' denote the
set of admissible policies.
For each admissible control process f E :9', let {XI, t :?: O} denote the associated
wealth process, i.e., X! is the wealth of the investor at time f, if he follows policy f.
Since any amount not invested in the risky stock is held in the bond, this process then
evolves as
(3)
dPt
(f
) dBt
dX[ = It p + X, - I, B - edt
,
,
= [rX! + f,( f.L - r) - e] dt + ftO" d~
upon substituting from (1) and (2).
--- page 337 ---

310
S. Browne
OPTIMAL PORTFOLIO STRATEGIES
471
Thus, for Markov control processes f , and functions \ft(t , x) E ~,,j. 2, the generator
of the wealth process is
We will put no constraints on the control f, (other than admissibility). In particular, we will allow /, < 0, as weJI as /, > X(. In the first instance, the company is
selling the stock short, while in the second instance it is borrowing money to invest
long in the stock. (While we do allow shortselling, it turns out that none of our
optimal policies will ever in fact do this.)
What will differentiate our model and results from previous work are the objectives
considered and the fact that here the withdrawal rate c is constant, and not a
decision variable.
The usual portfolio and asset allocation problems considered in the financial
economics literature deal with an investor whose wealth also evolves according to a
stochastic differential equation as in (3), where instead of being constant, c is now a
control variable as well, i.e., the consumption function c, = c(xf). For a specific
utility function u(·), the investor's objective is then to maximize the expected utility of
consumption and terminal wealth over some finite horizon, i.e., for T > 0, and some
"bequest function" '1'(.), the investor wishes to solve
(5)
for some discount factor A ~ O. Alternatively, the investor may wish to solve the
discounted infinite horizon problem
(6)
In both of these cases, since the process (e,l is usually assumed to be completely
controllable, it is clear that for certain utility functions at least, ruin need never occur,
since we may simply stop consuming at some level. Alternatively, as is the case when
the utility function is of the form u(c) = C 1- R /0 - R) for some R < 1, or u(c) =
In(c), the resulting optimal policy takes both investment I, and consumption c, to be
proportional to wealth, i.e., f, = 1T'l{t)XI' C, = 1T'2(t)X" which in turns makes the
optimal wealth process into a geometric Brownian motion, and thus the origin
becomes an inaccessible barrier. Classical accounts of such (and more sophisticated)
problems are discussed in Merton (1971, 1990) and Davis and Norman (1990) among
others.
Optimal investment decisions with constraints on consumption have also been
considered in the literature previously. Most relevant to our model is the literature on
constant proportion portfolio insurance (CPPI), ' as introduced in Black and Perold
(1992), where the resulting policy is to invest a constant proportion of the excess of
wealth over a given constant floor. (As its name suggests, portfolio insurance can be
loosely considered any trading and investment strategy that ensures that the value of
a portfolio never decrease below some limit. Alternative approaches to portfolio
insurance using options and other techniques are described in e.g., Luskin 1988.)
Black and Perold (1992) introduced this policy as the solution to the discounted
infinite horizon problem of (6) subject to the constraint that c, ~ cmlO ' where cm," is
--- page 338 ---

Survival and Growth with a Liability: Optimal Portfolio Strategies in Continuous Time
311
472
S. BROWNE
some given constant. The specific utility function considered there was
{
C I - R/(l - R)
U(C) =
K - K c
I
2
for c ~ c* ,
for c .:-;:; c*,
where c* is a given constant, R ~ 1 and K], K2 are constants chosen to ensure u(')
continuous throughout. While others (e.g., Dybvig 1995) have raised some technical
questions about the analysis in Black and Perold (1992), more relevant to our point of
view is the fact that this model (and the resulting optimal policy) allows for the
possibility of ruin, or bankruptcy, if wealth is initially below the given floor. This
possibility was never addressed in Black and Perold (1992).
In this paper we do not concentrate on the usual utility maximization problems of
(5) and (6). Rather, here we are concerned with the objective problems of survival and
growth. In particular, we first study the problem of how the investor (whose wealth
evolves according to (3» should invest to maximize the probability that the investor
survives forever (which turns out to be related to maximizing the probability of
achieving a given fixed fortune before going bankrupt), as well as the problem of how the
investor should invest so as to minimize the time until a given level of wealth has been
achieved. The former problem is called the survival problem, and is discussed in §3.
The latter is called the growth problem and is the content of §4. Related problems
have been studied in general under the label of "goal problems" in the works of
Pestien and Sudderth (1985, 1988), Heath et al. (1987) and Orey et al. (1987). The
survival problem for some specific related models were studied in Browne (1995) and
Majumdar and Radner (991). The former treated an "incomplete market" model,
where the withdrawals are not fixed but rather follow a stochastic process, and the
latter treated a model with forced constant consumption but without the possibility of
investing in a risk free asset.
Recently, in order to provide a consumption based economic justification for the
interesting portfolio strategies introduced in Grossman and Zhou (1993) (where the
optimal policy invests a constant proportion of wealth over a stochastic floor), Dybvig
(1995) considered the consumption-investment problem of (6) with the constraint that
consumption never decrease, i.e., that C1 > cs ' for all t ~ s, with Co > O. Thus consumption is forced in his model as well. He considered utility functions of the form
u(c) = c) - R /0 - R) and u(e) = In(e). However he only considered the problem in
the feasible region, where initial wealth Xu , satisfies Xu > co/r, and so for which ruin
need not occur. Dybvig (1995) did not consider the case when Xo > cu/r, and hence
where ruin is possibility, and so our results on this problem in §3 will complement his
analysis as well. Since in this paper our objectives deals solely with the achievement
of particular goals associated with wealth, it is clear that if there is a constraint on
consumption as in the models of Black and Perold (1992) and Dybvig (1995), we
should always set consumption at the minimum level, which in both cases is a
constant (cmm in Black and Perold 1992 and Co in Dybvig 1995). This is consistent
with the model we analyze here, where we will (at least at first) take consumption as a
fixed constant c per unit time. This implies that at least for some values of wealth,
the origin is accessible, and thus ruin is in fact a possibility.
In the next section we consider the problem of how to invest in order to survive.
However, before we study that problem, we need a preliminary result from control
theory that will provide the basis of all our future results.
2.1.
Optimal control. The problems of survival and growth considered in this
paper are all special cases of (Dirichlet-type) optimal control problems of the
--- page 339 ---

312
S. Browne
OPTIMAL PORTFOLIO STRATEGIES
473
following form: For each admissible control process {f" t ~ a}, let
T! := inf{t > 0: Xf = z}
denote the first hitting time to the point z of the associated wealth process {X!} of
(3), under policy f. For given numbers (t. u) with I < Xo < u, let Tf := min{T!, Tj}
denote the first escape time from the interval (I, u).
For a given nonnegative continuous function A(x) ~ 0, a given real bounded
continuous function g(x), and a function hex) given for x = I, x = u, let vf(x) be
defined by
with
vex) = sup J1 f(x)
and
fv*(x) = argsup vf(x).
~ .
~ ,
We note at the outset that we are only interested in controls (and initial values x) for
which vf(x) < 00.
As a matter of notation, we note first that here, and throughout the remainder of
the paper, the parameter 'Y will be defined by
(8)
THEOREM 2.1.
Suppose that w(x): (I, u) ~ (- 00, (0) is a ~2 Junction that is the
concave increasing (i.e., Wx > 0 and Wxx < 0) solution to the nonlinear Dirichlet problem
(9)
W2(X)
(1X-C)WX<X)-'Y~() +g(x)-A(x)w(x) =0, forl<x<u,
Wxx x
with
(10)
W(I) = h(l)
and w(u) = h(u),
and satisfies the conditions:
(i) w;(x)/wx/x) is bounded for all x in (I, u);
(ij) there exists an integrable random variable Y such that for all t ~ 0, w(X/) ~ Y;
(iii) w/x)/wx/x) is locally Lipschitz continuous.
Then w(x) is the optimal value Junction, i.e., w(x) = vex), and moreover the optimal
control, f v* ' can then be written as
(11 )
fv* ( x) = -
( J.L ~ r) wA x), for I < x < u.
U
wxAx)
PROOF. The appropriate HJB optimality equation of dynamic programming for
maximizing vf(x) of (7) over control policies ft> to be solved for a function
II is
SUPfE ~{.wfv + g -
All} = 0, subject to the Dirichlet boundary conditions v(1) = h(l)
and v(u) = heu) (cf. Theorem 1.4.5 of Krylov 1980). Since vex) is independent of
--- page 340 ---

Survival and Growth with a Liability: Optimal Portfolio Strategies in Continuous Time
313
474
S. BROWNE
time, the generator of (4) shows that this is equivalent to
(12)
sup {U( p- - r) + rx - c)vx + if2(T2Vxx + g - >.v} = O.
fE~'
Assuming now that (12) admits a classical solution with /Ix > 0 and IIxx < 0 (see, e.g.,
Fleming and Saner 1993), we may then use standard calculus to optimize with respect
to f in (12) to obtain the maximizer f.* = -« p- - r)/(T2)/lx/llxx (compare with
(11)). When this r:(x) is then substituted back into (12) and the resulting equation is
simplified, we obtain the nonlinear Dirichlet problem of (9) (with II = w).
It remains only to verify that the policy g is indeed optimal. The aforementioned
theorem in Krylav (1980) does not apply here, since in particular the degeneracy
condition (Krylov 1980, page 23) is not met. We will use instead the martingale
optimality principle, which entails finding an appropriate functional which is a
uniformly integrable martingale under the (candidate) optimal policy, but a supermartingale under any other admissible policy, with respect to the filtration .7, (see
Rogers and Williams 1987, Davis and Norman 1990).
To that end, let A/(s, t) := J,'>'(X[) du, and define the process
(13)
M(t, Xl) := e - A1(O·l)w(X!) + j'e -,\ i(O")g(Xf) ds,
for 0 S t S Tt,
o
where w is the concave increasing solution to (9).
Optimality of g of (11) is then a direct consequence of the following lemma.
LEMMA 2.2.
For allY admissible policy f, and M(t, . ) as defined in (13), we have
(14)
with equality holding if and only iff = g, where f .* is the policy given in (11). Moreover,
under policy fv* ' the process {M(t A TI, X,*" Tf )} is a unifonnly integrable martingale.
PROOF.
Applying Ito's formula to M(t, X() of (13) using (3) shows that for
Os sst S Tt
where Q(z; y) denotes the quadratic (in z) defined by
Q(z;y) ,= z 2[ ~<T2Wxx (Y)1 + z[( p- - r)wx(Y)]
+(ry - c)wAY) + g(y) - ,\(y)w(y).
Recognize now that since Qz/z;y) = (T"wxx(Y) < 0, we always have Q(z;y) s 0,
and the maximum is achieved at the value
z*(v):= _(J.L - r) wAy)
.
u 2
w,:.rCy)
with corresponding maximal value
wAy)2
( )_
Q(z* ; y) = (ry - c)wAy) -
y wx,(Y) + g(y) - A(y)w Y
= 0
--- page 341 ---

314
S. Browne
OPTIMAL PORTFOLIO STRATEGIES
475
where the final equality follows from (9). Therefore the second term in the r.h.s. of
(15) is always less than or equal to O. Moreover (15) shows that we have
Thus, by (ij) we see that the stochastic integral term in (15) is a local martingale that
is in fact a supennartingale. Hence, taking expectations on (15), with s = 0, therefore
shows that
(16) E( M(t 1\ rf, X(II Tf)) :::; w( x) + E( f;ATfe - t\f(O,U)Q(tu; Xl) dV)
:::; w(x) + E( IaI Il Tfe-Af(O,U)[ s~"PQ(tu ; Xt)] dV)
= w(x)
with the equality in (16) being achieved at the policy fv*.
Thus we have established (14).
Note that under the policy fv* of (11), the wealth process X* satisfies the
stochastic differential equation
where 7* := rl:. By (iii) this equation admits a unique strong solution (Karatzas and
Shreve 1988, Theorem 5.2.5).
Furthermore note that under the (optimal) policy, f: , we have, for all 0 :::; s :::; t :::;
r* ,
(
(
*)
* )
·rrc:fl { fV ( *)d} w;(X:) dW
18)
M [,X,
=M(s, X s
- v21' s exp -
sA Xp
P wrAX: )
v
which by (i) above is seen to be a uniformly integrable martingale. This completes the
proof of the theorem.
0
We now return to the survival problem.
3. Maximizing survival. We consider in this section two objectives related to
maximizing the survival of the investor. First we consider the problem of minimizing
the probability of ruin which is related to the problem of maximizing the probability of
reaching a particular given upper level of wealth before a given lower level. We will show
that an optimal strategy for this latter problem does not exist, although exploiting the
solution to a related solvable problem will allow us to explicitly construct €-optimal
ones. Next we consider the related objective of minimizing the expected discounted
penalty of ruin, which is equivalent to minimizing the expected discounted time to
--- page 342 ---

Survival and Growth with a Liability: Optimal Portfolio Strategies in Continuous Time
315
476
S. BROWNE
bankruptcy. This problem does admit an optima) solution and we find it explicitly. The
structure of the (optimal) survival policies obtained in this section are similar in that
they all invest a fixed fraction of the positive distance of wealth to a particular goal.
3.1.
Minimizing the probability of ruin. The evolutionary equation (3) exhibits
clearly that under policy f, the wealth process is a diffusion with drift function m and
diffusion coefficient function v given respectively by
( 19)
m(J, x, t) = J,( J.L - r) + IX -
e,
Thus for any admissible control f < 00 there is a region (in X space) where there is a
positive probability of bankruptcy. This is due to the fact that while the variance of
the wealth process is completely controllable, as is apparent from (19), the drift is not
completely controllable due to the fact that c > 0, and hence the drift can be
negative at certain wealth levels. This feature differentiates this model from those
usually studied in the investment literature (e.g., Merton 1971, 1990, Pliska 1986,
Davis and Norman 1990), with Majumdar and Radner (991) being a notable
exception. (For results on an "incomplete market" model where the variance, as well
as the drift, is also not completely controllable, see Browne 1995.) Specifically, let a
denote the bankruptcy level or point, with corresponding "bankruptcy time"(or ruin
time) 7/, where 0 s a < XO' One survival objective is then to choose an investment
policy which minimizes the probability of ruin, i.e., one which minimizes P(7j < x),
or equivalently, maximizes P(7! = 00) (see, e.g., Majumdar and Radner 1991, Browne
1995, Roy 1995).
Clearly this objective is meaningless for xl ~ e/r. To see this directly, consider the
case where the wealth level is x> e/r. We may then choose a policy which puts all
wealth into the bond, and then under this policy the probability of bankruptcy is O.
Specifically, if we take f = 0 for x > c /r, (3) shows that the wealth will then follow
the deterministic differential equation dX, = (rX, - c)dt, Xo = x> e/r, which exhibits exponential growth and for which P(7x _ . = x) = 1, for all € > O. Thus the
survival problem is interesting and relevant only in the region a < x < c/r, which we will
call the "danger-zone." This is of course due to the fact that e /r = c J; e-n dt is the
amount that is needed to be invested in the perpetual bond to payoff the forced
withdrawals forever. Since the investor need never face the possibility of ruin for
x > e Ir, we will call the region (c Ir, 00) the "safe-region."
Our objective in this section therefore is to determine a strategy that maximizes the
probability of hitting the safe-region or "safe pOint," c/r, prior 10 the "bankruptcy point,"
a, when initial wealth is in the danger-zone, i.e., a < x < c/r. As noted above, we will
show that an optimal policy for this problem does 110t exist, necessitating the
construction of an €-optimal strategy.
A somewhat related survival problem with constant withdrawals was studied in
Majumdar and Radner (1991) in a different setting, although without a risk-free
investment, and hence without a safe-region. Moreover, their results are not applicable to our case since here inf! v2(J, x, t} = 0, which violates the conditions of the
model in Majumdar and Radner (1991). As we shall see, it is in fact precisely this fact
that negates the existence of an optimal policy for our problem. A related survival
model which allows for investment in a risk-free asset, but where the "withdrawals"
are assumed to follow another (possibly dependent). Brownian motion with drift, was
treated in Browne (1995). Since the Brownian motion is unbounded, there was no
safe-region in Browne (1995) either. A discrete-time model with constant withdrawals
that does allow for a risk-free investment was treated in Roy (1995), but with no
borrowing allowed and bounded support for the return on the risky asset.
--- page 343 ---

316
S. Browne
OPTIMAL PORTFOLIO STRATEGIES
477
To show explicitly why no policy obtains optimality for the model treated here, and
how we may construct to-optimal strategies, we will first consider the following
problem: for any point b in the danger-zone, i.e., with a < x < b < clr, we will find
the optimal policy to maximize the probability of hitting b before a. For b strictly less
than clr, an optimal policy does exist for this problem, and we will identify it in the
following theorem. To that end let
V( x: a, b) = SUpPx(7! > Tn, and let N = arg sup PAT! > 7{).
~?
~?
THEOREM 3.1.
The optimal policy is to invest, at each wealth level a < x < b, the
state dependent amount
(20)
f;(x) = ~2~r(7:-x).
The optimal value junction is
(21)
(c - ra r
/ r + 1 -
(c _ 7X)y/ r +l
Vex : a, b) =
(
)y/ r+!
(
b)y/r +"
fora:s x:s b,
c-ra
-
c-r
where 'Y is defined by (8).
REMARK 3.1.
Note that the policy of (20) invests less as the wealth gets closer to
the goal b. In fact, it invests a constant proportion of the distance to the "safe point"
clr, regardless of the value of the goal b, and the bankruptcy point a. It is interesting to
observe that while here this constant proportion is independent of the underlying
diffusion parameter (T 2, this does not hold when there are multiple risky stocks in
which to invest in (see §5 beloW). The constant proportion is greater (less) than 1 as
~/r < ( »
3. Thus it is interesting to observe that as the wealth gets closer to the
bankruptcy point, a, the optimal policy does not " panic" and start investing an
enormous amount, rather the optimal policy stays calm and invests at most f:(a) =
2(c - ra)/( ~ - d. The investor does get increasingly more cautious as his wealth
gets closer to the goal b. (This behavior should be compared with the "timid" vs.
"bold" play in the discrete-time problems considered in the classic book of Dubins
and Savage 1965. See also Majumdar and Radner 1991 and Roy 1995.)
Observe further that the investor is borrowing money to invest in the stock only
when x < 2cl(jl + r) but not when 2c/(~ + r) <x < clr. This can be seen by
observing directly that in the former case N(x) > x and in the latter case f:(x) < x.
(The fact that 2c/( jl + r) < clr follows from the assumption that ~ > r.)
PROOF.
While we could prove Theorem 3.1 from a more general theorem in
Pestien and Sudderth (1985) (see also Pestien and Sudderth 1988) which we will
discuss later (see Remark 3.4 beloW), recognize that this is simply a special case of the
control problem solved in Theorem 2.1 for I = a, U = b with A = 0, g = 0 and
h(b) = 1, h(a) = O. As such the nonlinear Dirichlet problem of (9) for the optimal
value function V becomes in this case
(22)
v2
(IX - c) Vx - ,.,; = 0, for a < x < b
xx
subject to the (Dirichlet) boundary conditions V(a) = 0, V(b) = 1.
