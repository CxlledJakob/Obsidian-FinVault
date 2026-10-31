# The Kelly capital growth investment criterion _ theory and -- Leonard C_ Maclean, Edward O_ Thorp, W_ T_ Ziemba, Leonard -- World Scientific Handbook -- isbn13 9781283148344 -- bec576e26410d0c695fd5b867d08ec4f -- An.pdf — pages 590–609

--- page 590 ---

Medium Term Simulations of the Full Kelly and Fractional Kelly Investment Strategies
561
5
Appendix
The proportional investment strategies in the experiments of Bicksler and Thorp (1973) have fractional Kelly equivalents. The Kelly investment proportion for the experiments are deveolped in this
appendix.
5.1
KELLY STRATEGY WITH UNIFORM RETURNS
Consider the problem
Max x {E(ln(l + r + x(R - rn ,
where R is uniform on [a, bJ and r =the risk free rate.
We have the first order condition
l
b
R - r
1
----,-------,- x -b -dR = 0,
a l+r+x(R-r)
-a
which reduces to
(b
)
(
)1 ( l+r+X(b-r))
[l+r+X(b-r)]!
b - a
X
- a = 1 + r n
{==?
= e l + r •
l+r+x(a-r)
l+r+x(a-r)
In the case considered in Experiment II, a = -0.25, b = 0.5, r = O.
The equation becomes
1
[~];; = eO. 75 with a solution x = 2.8655. So the Kelly strategy is to invest 286.55% of
1-O.25x
'
wealth in the risky asset.
5.2
Kelly Strategy with Normal Returns
Consider the problem
Max x {E(ln(l + r + x(R - rn,
where R is Gaussian with mean J.LR and standard deviation (JR, and r =the risk free rate. The
solution is given by Merton (1990) as
The values in Experiment III are J.LR
x = 1.5288.
J.LR - r
X=---.
(JR
0.102 , (JR = 0.203, r
19
0.039, so the Kelly strategy is
--- page 591 ---

This page is intentionally left blank
--- page 592 ---

39
Good and Bad Properties of the Kelly Criterion*
Leonard C. MacLean
School of Business, Dalhousie University, Halifax, NS
Edward O. Thorp
E. O. Thorp and Associates, Newport Beach, CA
Professor Emeritus, University of California, Irvine
William T. Ziemba
Professor Emeritus, University of British Columbia, Vancouver, BC
Visiting Professor, Mathematical Institute, Oxford University, UK
ICMA Centre, University of Reading, UK
University of Bergamo, Italy
Abstract
We summarize what we regard as the good and bad properties of the Kelly criterion and its variants. Additional properties are discussed as observations.
563
The main advantage of the Kelly criterion, which maximizes the expected value of
the logarithm of wealth period by period, is that it maximizes the limiting exponential growth rate of wealth. The main disadvantage of the Kelly criterion is that
its suggested wagers may be very large. Hence, the Kelly criterion can be very risky
in the short term.
In the one asset two valued payoff case, the optimal Kelly wager is the edge
(expected return) divided by the odds. Chopra and Ziemba (1993), reprinted in
Part II of this volume, following earlier studies by Kallberg and Ziemba (1981,
1984) showed for any asset allocation problem that the mean is much more important than the variances and co-variances. Errors in means versus errors in variances
were about 20: 2 : 1 in importance as measured by the cash equivalent value of final
wealth. Table 1 and Figure 1 show this and illustrate that the relative importance
depends on the degree of risk aversion. The lower is the Arrow-Pratt risk aversion, RA = -u" (w) / u' (w), the higher are the relative errors from incorrect means.
Chopra (1993) further shows that portfolio turnover is larger for errors in means
'Special thanks go to Tom Cover and John Mulvey for helpful comments on an earlier draft of
this paper.
1
--- page 593 ---

564
L. C. MacLean, E. 0. Thorp and W T Ziemba
Table 1
Average Ratio of Certainty Equivalent Loss for Errors in Means, Variances and Covariances. [Source: Chopra and Ziemba (1993)]
Errors in Means
Errors in Means
Errors in Variances
Risk Tolerance*
vs Covariances
vs Variances
vs Covariances
25
5.38
3.22
1.67
50
22.50
10.98
2.05
75
56.84
21.42
2.68
1
1
1
20
10
2
Error Mean
Error Var
Error Covar
20
2
1
*Risk tolerance=RT(w) = ~C
) where RA(W) = _ u';CCw»
zRA w
U
W
% Cash
Equivalent4lss
11~----------------------------~~----,
10
Means
9
8
7
6
5
4
3
2
o -'
o
0.05
0.10
0.15
Magnitude of eor (k)
_
Varianes
,-- Covarial1lS
0.20
Figure 1
Mean Percentage Cash Equivalent Loss Due to Errors in Inputs
than for variances and for co-variances but the degree of difference in the size of the
errors is much less than the performance as shown in Figure 2.
Since log has RA(W) = l/w, which is close to zero, the Kelly bets may be exceedingly large and risky for favorable bets. In MacLean et aZ. (2009), we present
simulations of medium term Kelly, fractional Kelly, and proportional betting strategies. The results show that, with favorable investment opportunities, Kelly bettors
attain large final wealth most of the time. However, because a long sequence of
bad scenario outcomes is possible, any strategy can lose substantially even if there
are many independent investment opportunities and the chance of losing at each
investment decision point is small. The Kelly and fractional Kelly rules, like all
other rules, are never a sure way of winning for a finite sequence.
In Part VI of this volume, we describe the use of the Kelly criterion in many
applications and by many great investors. Two of them, Keynes and Buffett, were
long term investors whose wealth paths were quite rocky but with good long term
2
--- page 594 ---

Good and Bad Properties of the Kelly Criterion
Average Turnover (% per month)
50 r----------------------------------------------=~~
40
Means
30
20
Variances
......
......
Covariances
10 I
... ~~=====~
10~
5
10
15
20
25
30
35
40
45
50
Change(%)
565
Figure 2
Average turnover for different percentage changes in means, variances and covariances.
[Source: Based on data from Chopra (1993)]
outcomes. Our analyses suggest that Buffett seems to act similar to a fully Kelly
bettor (subject to the constraint of no borrowing) and Keynes like a 80% Kelly
bettor with a negative power utility function _W-0 .25 , see Ziemba (2003) and the
wealth graphs reprinted in Part VI from Ziemba (2005).
Graphs such as Figure 3 show that growth is traded off for security with the use
of fractional Kelly strategies and negative power utility functions. Log maximizes
the long run growth rate. Utility functions such as positive power that bet more
than Kelly have more risk and lower growth. One of the properties shown below
that is illustrated in the graph is that for processes, which are well approximated
by continuous time, the growth rate becomes zero plus the risk free rate when one
bets exactly twice the Kelly wager.
Hence, it never pays to bet more than the Kelly strategy because then risk increases (lower security) and growth decreases, so Kelly dominates all these strategies
in geometric risk-return or mean-variance space. See Ziemba (2009) in this volume.
As you exceed the Kelly bets more and more, risk increases and long term growth
falls, eventually becoming more and more negative. Long Term Capital is one of
many real world instances in which overbetting led to disaster. See Ziemba and
Ziemba (2007) for additional examples.
Thus, long term growth maximizing investors should bet Kelly or less. We call
betting less than Kelly "fractional Kelly", which is simply a blend of Kelly and
cash. Consider the negative power utility function ow d for 0 < O. This utility
function is concave and when 0 ---+ 0, it converges to log utility. As 0 becomes
more negative, the investor is less aggressive since his absolute Arrow-Pratt risk
aversion index is also higher. For the case of a stationary lognormal process and a
given 0 for utility function owd and ex = 1/(1 - 0) between 0 and I , they both will
3
--- page 595 ---

566
Prohability
1.0
0.8
0.6
0.4
0.2
L. C. MacLean, E. O. Thorp and W T Ziemba
Optimal Kelly wager
0 .01+----r---+----r--~
0.0
0.81
0.02
0.03
Fraction .fWealth Wagered
Figure 3
Probability of doubling and quadrupling before halving and relative growth rates versus
fraction of wealth wagered for Blackjack (2% advantage, p = 0.51 and q = 0.49). [Source: MacLean
and Ziemba (1999)]
provide the same optimal portfolio when ex is invested in the Kelly portfolio and
1 - ex is invested in cash. This handy formula relating the coefficient of the negative
power utility function to the Kelly fraction is correct for lognormal investments and
approximately correct for other distributed assets; see MacLean, Ziemba and Li
(2005). For example, half Kelly is 6 = -1 and quarter Kelly is 6 = -3. So if you
want a less aggressive path than Kelly, pick an appropriate 6. This formula does
not apply more generally. For example, for coin tossing, where Pr(X = 1) = p,
Pr(X - 1) = q, p + q = I,
1
1
*
p'- 6 _ q~
fo =
1
1
p'- 6 + q'- 6
which is not exf*, where f* = p - q ;? 0 is the Kelly bet.
We now list these and other important Kelly criterion properties, updated from
MacLean, Ziemba, and Blazenko (1992), MacLean and Ziemba (1999), and Ziemba
and Ziemba (2007). See also Cover and Thomas (2006, Chapter 16).
The Good Properties
Good Maximizing ElogX asymptotically maximizes the rate of asset growth. See
Breiman (1961), Algoet and Cover (1988).
Good The expected time to reach a preassigned goal A is asymptotically least as
A increases without limit with a strategy maximizing ElogXN . See Breiman
(1961), Algoet and Cover (1988), Browne (1997a).
Good Under fairly general conditions, maximizing ElogX also asymptotically maximizes median logX. See Ethier (1987, 2004, 2010).
4
--- page 596 ---

Good and Bad Properties of the Kelly Criterion
Good The ElogX bettor never risks ruin. See Hakansson and Miller (1975).
Good The absolute amount bet is monotone increasing in wealth.
567
Good The ElogX bettor has an optimal myopic policy. He does not have to consider prior nor subsequent investment opportunities. This is a crucially
important result for practical use. Hakansson (1971) proved that the myopic policy obtains for dependent investments with the log utility function.
For independent investments and any power utility, a myopic policy is optimal, see Mossin (1968). In fact, past outcomes can be taken into account by
maximizing the conditional expected logarithm given the past (Algoet and
Cover, 1988).
Good Simulation studies show that the ElogX bettor's fortune pulls ahead of other
"essentially different" strategies' wealth for most reasonable-sized samples.
"Essentially different" has a limited meaning. For example, g* ~ 9 but
g* - 9 = E will not lead to rapid separation if E is small enough. The key
again is risk. See Bicksler and Thorp (1973), Ziemba and Hausch (1986),
and MacLean, Thorp, Zhao and Ziemba (2009) in this volume. General
formulas are in Aucamp (1993).
Good If you wish to have higher security by trading it off for lower growth, then
use a negative power utility function, 6wo, or fractional Kelly strategy. See
MacLean, Sanegre, Zhao and Ziemba (2004) reprinted in Part III, who show
how to compute the coefficent to stay above a growth path at discrete points
in time with given probability or to be above a given drawdown with a certain
confidence limit. MacLean, Zhao and Ziemba (2009) add the feature that
path violations are penalized with a convex cost function. See also Stutzer
(2009) for a related but different model of such security.
Good Competitive optimality.
Kelly gambling yields wealth X* such that
E ( ; . ) ~ 1, for all other strategies X. This follows from the Kuhn Tucker
conditions. Thus, by Markov's inequality, Pr [X ~ tX*] ~ i, for t ~ 1,
and for all other induced wealths x . Thus, an opponent cannot outperform
X* by a factor t with probability greater than i. This inequality can be
improved when t = 1 by allowing fair randomization U. Let U be drawn
according to a uniform distribution over the interval [0,2], and let U be independent of X*. Then the result improves to Pr [X ~ U X*] ~ ~ for all
portfolios X. Thus, fairly randomizing one's initial wealth and then investing it according to the Kelly criterion, one obtains a wealth U X* that can
only be beaten half the time. Since a competing investor can use the same
strategy, probability ~ is the best competitive performance one can expect.
We see that Kelly gambling is the heart of the solution for this two-person
zero sum game of who ends up with the most money. So we see that X*
(actually U X*) is competitively optimal in a single investment period (Bell
and Cover 1980, 1988).
5
--- page 597 ---

568
L. C. MacLean, E. O. Thorp and W. T Ziemba
Good If X* is the wealth induced by the log optimal (Kelly) portfolio, then the
expected wealth ratio is no greater than one, i.e., E( ;.) ~ 1, for the wealth
X induced by any other portfolio (Bell and Cover, 1980, 1988).
Good Super St. Petersburg. Any cost c for the St. Petersburg random variable X,
Pr [X = 2k] = 2-k, is acceptable. But the larger the cost c, the less wealth
one should invest. The growth rate G* of wealth resulting from repeated
such investments is
G* = max E In (1 -f + 1 x)
0";1";1
C
where f is the fraction of wealth invested. The maximizing 1* is the Kelly
proportion (Cover and Bell, 1980). The Kelly fraction 1* can be computed
even for a super St. Petersburg random variable Pr [Y = 22k] = 2- k , k =
1,2, . . . , where E In Y = 00, by maximizing the relative growth rate
1-f+ly
max Eln lIe
0";1";1
'2 + 2c:Y
This is bounded for all f in [0,1] .
Now, although the exponential growth rate of wealth is infinite for all
proportions f and it seems that all f E [0,1] are equally good, the maximizing 1* in the previous equation guarantees that the 1* portfolio will
asymptotically exponentially outperform any other portfolio f E [0,1]. Both
investors' wealth have super exponential growth, but the 1* investor will exponentially outperform any other essentially different investor.
The Bad Properties
Bad The bets may be a large fraction of current wealth when the wager is favorable
and the risk of loss is very small. For one such example, see Ziemba and
Hausch (1986; 159- 160). There, in the inaugural 1984 Breeders Cup Classic
$3 million race, the optimal fractional wager, using the Dr. Z place and show
system using the win odds as the probability of winning, on the 3- 5 shot
Slew of Gold was 64% (see also the 74% future bet on the J anuary effect in
MacLean, Ziemba and Blazenko (1992) reprinted in this volume). Thorp and
Ziemba actually made this place, show bet and won with a low fractional
Kelly wager. Slew finished third but the second place horse Gate Dancer was
disqualified and placed third. Wild Again won this race and it was the first
great victory of the masterful jockey Pat Day.
Bad For coin tossing, any fixed fraction strategy has the property that if the number of wins equals the number of losses, then the bettor is behind. For n wins
and n losses and initial wealth Wo, we have W2n = Wo(lj2)n.
6
--- page 598 ---

Good and Bad Properties of the Kelly Criterion
569
Bad The unweighted average rate of return converges to half the arithmetic rate
of return. Thus, you may regularly win less than you expect. This is a
consequence of weighting equally rather than by size of the wager. See Ethier
and Tavare (1983) and Griffin (1985).
Some Observations
• For an iid process and a myopic policy, which results from maximizing expected utility in case the utility function is log or a negative power, the result
is fixed fraction betting, hence fractional Kelly includes all these policies.
• A betting strategy is "essentially different" from Kelly if Sn == L~l Elog(l +
it X i) -
L~l Elog(l + i iX i) tends to infinity as n increases. The sequence
un denotes the Kelly betting fractions and the sequence Ud denotes the
corresponding betting fractions for the essentially different strategy.
• The Kelly portfolio does not necessarily lie on the efficient frontier in a meanvariance model (Thorp, 1971).
• Despite its superior long-run growth properties, Kelly, like any other strategy,
can have a poor return outcome. For example, making 700 wagers, all of
which have a 14% advantage, the least of which has a 19% chance of winning,
can turn $1000 into $18. But with full Kelly 16.6% of the time, $1000 turns
into at least $100,000, see Ziemba and Hausch (1996). Half Kelly does not
help much as $1000 can become $145 and the growth is much lower with only
$100,000 plus final wealth 0.1 % of the time. For more such calculations, see
Bicksler and Thorp (1973) and MacLean, Thorp, Zhao and Ziemba (2009) in
this volume.
• Fallacy: If maximizing E log X N almost certainly leads to a better outcome,
then the expected utility of its outcome exceeds that of any other rule provided
N is sufficiently large. Counter-example: u(x) = x,1/2 < p < 1, Bernoulli
trials i = 1 maximizes EU(x) but i = 2p - 1 < 1 maximizes ElogXN. See
Samuelson (1971) and Thorp (1971, 2006).
• It can take a long time for any strategy, including Kelly, to dominate an essentially different strategy. For instance, in continuous time with a geometric
Wiener process, suppose /.Lo: = 20%, /.L f3 = 10%, (Jo: = (Jf3 = 10%. Then in five
years, A is ahead of B with 95% confidence. But if (Jo: = 20%, (Jf3 = 10% with
the same means, it takes 157 years for A to beat B with 95% confidence. As
another example, in coin tossing, suppose game A has an edge of 1.0% and
game B 1.1%. It takes two million trials to have an 84% chance that game A
dominates game B, see Thorp (2006).
The theory and practical application of the Kelly criterion is straightforward
when the underlying probability distributions are fairly accurately known. However,
in investment applications, this is usually not the case. Realized future equity
7
--- page 599 ---

570
L. C. MacLean, E. O. Thorp and W T Ziemba
returns may be very different from what one would expect using estimates based on
historical returns. Consequently, practitioners who wish to protect capital above
all, sharply reduce risk as their drawdown increases.
Prospective users of the Kelly Criterion can check our list of good properties,
bad properties and observations to test whether Kelly is well suited to their intended
application. Given the extreme sensitivity of E log calculations to errors in mean
estimates, these estimates must be accurate and to be on the safe side, the size of
the wagers should be reduced.
For long term compounders, the good properties dominate the bad properties
of the Kelly criterion, but the bad properties may dampen the enthusiasm of naive
prospective users of the Kelly criterion. The Kelly and fractional Kelly strategies are
very useful if applied carefully with good data input and proper financial engineering
risk control.
Appendix
In continuous time, with a geometric Wiener process, betting exactly double the
Kelly criterion amount leads to a growth rate equal to the risk free rate. This result
is due to Thorp (1997), Stutzer (1998), Janacek (1998), and possibly others. The
following simple proof, under the further assumption of the Capital Asset Pricing
Model, is due to Harry Markowitz and appears in Ziemba (2003).
In continuous time
1
gp = Ep -
2Vp
E p, Vp, gp are the portfolio expected return, variance and expected log, respectively.
In the CAPM
Vp = 0'~X2
where X is the portfolio weight and ro is the risk free rate. Collecting terms and
setting the derivative of gp to zero yields
X = (EM -
ro)jO'~
which is the optimal Kelly bet with optimal growth rate
g* = ro + (EM - ro)2 -
~[(EMro)jO'~l20'~
= ro + (EM - ro)2 jO'~ - ~(EM - ro)2 jO'~
1
2
= ro + 2[(E - M - r))jO'Ml .
8
--- page 600 ---

Good and Bad Properties of the Kelly Criterion
571
Substituting double Kelly, namely Y = 2X for X above into
1 2
2
gp = TO + (EM - TO)y - "2aMY
and simplifying yields
go - TO = 2(EM - To)2/a'iI - ~(EM - To)2/a'iI = o.
Hence go = TO when Y = 2S.
The CAPM assumption is not needed. For a more general proof and illustration,
see Thorp (2006).
References
Algoet, P. H. and T . Cover (1988). Asymptotic optimality and asymptotic equipartition
properties of log-optimum investment. Annals of Probability, 16(2), 876- 898.
Aucamp, D. (1993). On the extensive number of plays to achieve superior performance
with the geometric mean strategy. Management Science, 39, 1163- 1172.
Bell, R. M. and T. M. Cover (1980). Competitive optimality of logarithmic investment.
Math of Operations Research, 5, 161- 166.
Bell, R. M. and T. M. Cover (1988). Game-theoretic optimal portfolios. Management
Science, 34(6), 724- 733.
Bicksler, J. L. and E. O. Thorp (1973). The capital growth model: an empirical investigation. Journal of Financial and Quantitative Analysis, 8(2) , 273- 287.
Breiman, L. (1961). Optimal gambling system for favorable games. Proceedings of the 4th
Berkeley Symposium on Mathematical Statistics and Probability, 1, 63- 8.
Browne, S. (1997). Survival and growth with a fixed liability: optimal portfolios in continuous time. Math of Operations Research, 22, 468- 493.
Chopra, V. K. (1993). Improving optimization. Journal of Investing, 2(3) , 51- 59.
Chopra, V. K. and W. T. Ziemba (1993). The effect of errors in mean, variance and covariance estimates on optimal portfolio choice. Journal of Portfolio Management,
19, 6- 11.
Cover, T. and J. A. Thomas (2006). Elements of Information Theory (2 ed.).
Ethier, S. (1987). The proportional bettor's fortune. Proceedings 7th International Conference on Gambling and Risk Taking, Department of Economics, University of Nevada,
Reno.
Ethier, S. (2004). The Kelly system maximizes median fortune. Journal of Applied
Probability, 41, 1230- 1236.
Ethier, S. (2010). The Doctrine of Chances: Probabilistic Aspects of Gambling. New York:
Springer.
Ethier, S. and S. Tavare (1983). The proportional bettor's return on investment. Journal
of Applied Probability, 20, 563- 573.
Finkelstein, M. and R. Whitley (1981). Optimal strategies for repeated games. Advanced
Applied Probability, 13, 415- 428.
Griffin, P. (1985). Different measures of win rates for optimal proportional betting. Management Science, 30, 1540- 1547.
Hakansson, N. H. (1971). On optimal myopic portfolio policies with and without serial
correlation. Journal of Business, 44, 324-334.
9
--- page 601 ---

572
L. C. MacLean, E. 0. Thorp and W. T. Ziemba
Hakansson, N. H. and B. Miller (1975). Compound-return mean-variance efficient portfolios
never risk ruin. Management Science, 22, 391- 400.
Janacek, K. (1998). Optimal growth in gambling and investing. M.Sc. Thesis, Charles
University, Prague.
Kallberg, J . G. and W. T. Ziemba (1981). Remarks on optimal portfolio selection. In
G. Bamberg and O. Opitz (Eds.), Methods of Operations Research, pp. 507- 520.
Cambridge, MA: Oelgeschlager.
Kallberg, J. G. and W. T. Ziemba (1984). Mis-specifications in portfolio selection problems.
In G. Bamberg and K. Spremann (Eds.) , Risk and Capital, pp. 74- 87. New York:
Springer Verlag.
MacLean, L., R. Sanegre, Y. Zhao, and W. T. Ziemba (2004). Capital growth with security.
Journal of Economic Dynamics and Control, 28(4), 937- 954.
MacLean, L. , E. O. Thorp, Y. Zhao, and W. T. Ziemba (2009). Medium term simulations
of Kelly and fractional Kelly strategies.
MacLean, L. and W . T . Ziemba (1999). Growth versus security tradeoffs in dynamic investment analysis. Annals of Operations Research, 85, 193- 227.
MacLean, L., W. T. Ziemba, and G. Blazenko (1992). Growth versus security in dynamic
investment analysis. Management Science, 38, 1562- 85.
MacLean, L., W. T. Ziemba, and Li (2005) . Time to wealth goals in capital accumulation and the optimal trade-off of growth versus security. Quantitative Finance, 5(4) ,
343- 357.
MacLean, L. C., Y. Zhao, and W . T. Ziemba (2009). Optimal capital growth with convex
loss penalties. Working Paper, Dalhousie University.
Mossin, J. (1968). Optimal multiperiod portfolio policies. Journal of Business, 41, 215- 229.
Samuelson, P. A. (1971). The fallacy of maximizing the geometric mean in long sequences
of investing or gambling. Proceedings, National Academy of Science, 68, 2493-2496.
Stutzer, M. (2009). On growth optimality versus security against underperformance.
Thorp, E. O. (1971). Portfolio choice and the Kelly criterion. Proceedings of the Business
and Economics Section of the American Statistical Association, 215-224.
Thorp, E. O. (2006) . The Kelly criterion in blackjack, sports betting and the stock market. In S. A. Zenios and W. T. Ziemba (Eds.) , Handbook of Asset and Liability
Management, Handbooks in Finance, pp. 385-428. Amsterdam: North Holland.
Ziemba, R. E. S. and W. T. Ziemba (2007). Scenarios for Risk Management and Global
Investment Strategies. NY: Wiley.
Ziemba, W. T. (2003). The Stochastic Programming Approach to Asset Liability and
Wealth Management. AIMR, Charlottesville, VA.
Ziemba, W. T. (2005). The symmetric downside risk Sharpe ratio and the evaluation of
great investors and speculators. Journal of Portfolio Management, Fall, 108-122.
Ziemba, W. T. (2009). Utility theory for growth versus security. Working Paper.
Ziemba, W. T. and D. B. Hausch (1986) . Betting at the Racetrack. Dr. Z. Investments,
San Luis Obispo, CA.
10
--- page 602 ---

Part V
Utility foundations
--- page 603 ---

This page is intentionally left blank
--- page 604 ---

575
40
Introduction to the Utility Foundations of Kelly
The criticisms of the Kelly strategy based on utility are general. If preferences are
identified with wealth characteristics such as growth and tail values, then there is
a utility foundation for Kelly and fractional Kelly strategies.
Hakansson and Ziemba (1995) survey their and others' works on capital growth
theory. They discuss Hakansson's consumption-investment model over time in the
expected log context and MacLean and Ziemba's growth and security tradeoffs and
its relationship with fractional Kelly strategies. They discuss the properties of these
models and relate capital growth to expected utility.
Luenberger (1993) investigates the long term behavior of E log strategies. Merton and Samuelson (1974) show that
lim E [u(Wn )]
n-HXJ
is not an expected utility so the idea of using utility at a terminal time and taking
the limit is not valid. Hence, the log mean-variance approach is not consistent
with expected utility theory. Luenberger provides a new preference based approach
to the problem assuming independent non-negative identically distributed returns.
He establishes preferences on infinite sequences of wealth rather than wealth at a
fixed (but later taken to the limit) terminal time. This approach avoids the limit
problems and allows use of probability limit theorems.
If the tail preference is defined by a simple utility function, then the utility
must be the expected log of wealth. Tail preferences are appropriate if the goal of
investment is long term wealth maximization. If preferences are represented by a
compound utility function, then that function will be a function of the expected
logarithm and the variance of the logarithm of wealth. So in that case, there is
a Markowitz type efficient tradeoff frontier of E log Wand Var log W that was
originally suggested by Williams (1936).
Stutzer (2003) provides an alternative behavioral foundation for an investor's use
of power utility and its defining risk aversion parameter. This involves an investor's
desire to minimize the probability that the wealth growth rate will not exceed an
exogenous target growth rate. Stutzer uses the Gartner-Ellis large deviations theory
to show that this leads to an equivalent power utility function. This means that
the investor's risk aversion parameter depends on the investment opportunity set
contrary to typical model assumptions. Stutzer's formulation uses a wealth variable
in the utility function that is the ratio of current wealth to the level of wealth growing
at the constant target rate. Also the power coefficient is not specified in advance
--- page 605 ---

576
L. C. MacLean, E. 0. Thorp and W T. Ziemba
but rather is an output of the optimization. For ease of estimation, an independent
identically distributed asset return assumption is made.
Stutzer (2010) in a followup paper discusses further how to increase security
against under-performance in dynamic investment analysis over finite horizons
against a specified exogenous benchmark. Motivation is provided because it takes
a long time to be fairly sure that Kelly strategies dominate, and the Kelly strategy
has considerable risk of under-performing or having very low returns. He uses a
Bayesian formulation of the Occam's Razor Principle to illustrate the unavoidable
reduction of statistical testability (namely the ability to more easily falsify) inherent
in objective functions that have non-directly observable parameters. The coefficient
of the power utility function is endogenously determined. The setting used is the
familiar blackjack example previously discussed by Thorp and by MacLean, Ziemba,
and Blazenko (1992).
--- page 606 ---

R. Jarrow et aI., Eds., Handbooks in OR & MS, Vol. 9
© 1995 Elsevier Science B.Y. All rights reserved
Chapter 3
41
Capital Growth Theory
Nils H Hakansson
Walter A. Haas School of Business, University of California, Berkeley, CA 94720, U.S.A.
William T. Ziemba
Faculty of Commerce and Business Administration, University of British Columbia, Vancouver,
B.c. V6T lY8, Canada
1. Introduction
577
Even casual observation strongly suggests that capital growth is not just a
catch-phrase but something which many actively strive to achieve. It is therefore
rather surprising that capital growth theory is a relatively obscure subject. For
example, the great bulk of today's MBA's have had little or no exposure to the
subject, having had their attention focussed almost exclusively on the single-period
mean-variance model of portfolio choice. The purpose of this essay is to review
the theory of capital growth, in particular the so-called growth-optimal investment
strategy, its properties, its uses, and its links to betting and other investment
models. We also discuss several applications that have tended to refine the basic
theory.
The central feature of the growth-optimal investment strategy, also known as
the geometric mean model and the Kelly criterion, is the logarithmic shape of
the objective function. But the power and durability of the model is due to a
remarkable set of properties. Some of these are unique to the growth-optimal
strategy and the others are shared by all the members of the (remarkable) small
family to which the growth optimal strategy belongs.
Investment over time is multiplicative, not additive, due to the compounding
nature of the process itself. This makes a number of results in dynamic investment
theory appear nonintuitive. For example, in the single-period portfolio problem,
the optimal investment policy is very sensitive to the utility function being used;
the set of policies that are inadmissible or dominated across all utility functions is
relatively small. The same observation holds in the dynamic case when the number
of periods is not large. But as the number of periods does become large, the set of
investment policies that are optimal for current investment tends to shrink drastically, at least in the basic reinvestment case without transaction costs. As we will
see, many strikingly different investors will, in essence, invest the same way when
the horizon is distant and will only begin to part company as their horizons near.
65
--- page 607 ---

578
N. H. Hakansson and W T. Ziemba
66
N.H. Hakansson, w.T. Ziemba
It is tempting to conjecture that all long-run investment policies to which
risk-averse investors with monotone increasing utility functions will flock, under a
favorable return structure, insure growth of capital with a very high probability.
Such a conjecture is false; many investors will, even in this case, converge
on investment policies which almost surely risk ruin in the long run, in effect
ignoring feasible policies which almost surely lead to capital growth. Similarly,
the relationship between the behavior of capital over time and the behavior
of the expected utility of that same capital over time often appears strikingly
nonintuitive.
Section 2 reviews the origins of the capital growth model while Section 3
contains a derivation and identifies its key properties. The conditions for capital
growth are examined in Section 4. The model's relationship to other long-run
investment models is studied in Section 5 and Section 6 contains its role in
intertemporal investment/consumption models. Section 7 adds various constraints
for accomplishing tradeoffs between growth and security, while Section 8 reviews
various applications. A concluding summary is given in Section 9.
2. Origins of the model
The approach to investment commonly known as the growth-optimal investment
strategy has a number of apparently independent origins. In particular, Williams
[1936], Kelly [1956], Latane [1959], and Breiman [1960, 1961] seem to have
been unaware of each other's papers. But one can also argue that Bernoulli
(1738) unwittingly stumbled on it in 1738 in his resolution of the st. Petersburg
Paradox -
see the 1954 translation -
and Samuelson's survey [1977].
Samuelson [1971] appears to be the earliest to have related the geometric mean
criterion to utility theory -
and to find it wanting. The growth optimal strategy's
inviolability in the larger consumption-investment context when preferences for
consumption are logarithmic was first noted by Hakansson [1970]. Finally, models
considering tradeoffs between capital growth and security appear to have been
pioneered by MacLean & Ziemba [1986].
3. The model and its basic properties
The following notation and basic assumptions will be employed:
Wt
= amount of investment capital at decision point t (the end of the tth
period);
M t
= the number of investment opportunities available in period t, where
Mt:S M;
St
the subset of investment opportunities which it is possible to sell short in
period t;
nt
rate of interest in period t;
--- page 608 ---

Capital Growth Theory
579
Ch. 3. Capital Growth Theory
67
rit
= return per unit of capital invested in opportunity i, where i = 2, . . . , Mt ,
in the tth period (random variable). That is, if we invest an amount () in i
at the beginning of the period, we will obtain (1 + rit W at the end of that
period;
ZIt
= amount lent in period t (negative ZIt indicate borrowing) (decision variable);
Zit
amount invested in opportunity i, i = 2, ... ,Mt at the beginning of the
tth period (decision variable);
Ft(Y2, Y3 ,···, YM,) == Pr {r2t S Y2, r3t S Y3, . . . , rM,t S YM,};
Zt
-
(Z2t, . . . , ZM,t);
Zit
Wt-l
i = 1, .. . , Mt ;
The capital market will generally be assumed to be perfect, i.e. that there are no
transaction costs or taxes, that the investor has no influence on prices or returns,
that the amount invested can be any real number, and that the investor has full
use of the proceeds from any short sale.
The following basic properties of returns will be assumed:
rlt 2: 0,
t = 1,2, ...
E[rit] 2: 8 + rlf>
8> 0,
some i, t = 1,2, . . .
E[rit] S K,
all i, t.
(1)
(2)
(3)
These assumptions imply that the financial market provides a 'favorable game.'
We also assume that the (nonstationary) return distributions Ft are either
independent from period to period or obey a Markov process and they also satisfy
the 'no-easy-money condition'
!
M,
I
M,
P t; (rit - rlt Wi < 81
> 82 for all t and all (}i such that t; I(}i I = 1,
and (}i 2: °
for all i ¢ St,
(4)
where 81 < 0, 82 > 0.
Condition (4) is equivalent to what is often referred to as the no-arbitrage
condition. It is generally a necessary condition for the portfolio problem to have a
solution.
We also assume that the investor must remain solvent in each period, i.e., that
he or she must satisfy the solvency constraints
Pr{Wt 2: O} = 1,
t = 1,2, . .. .
(5)
--- page 609 ---

580
N. H. Hakansson and W T. Ziemba
68
N.H. Hakansson, w.T. Ziemba
The amount invested at time t - 1 is
Mt
LZit = Wt-l
i=l
and the value of the investment at time t, broken down between its risky and
riskfree components, is
Mt
Mt
Wt = L(1 + rit)Zit + (1 + rlt)( 1 - L
Zit),
i=2
i=2
which together yield the basic difference equation
where
Mt
Wt = L(rit -rlt)Zit+ Wt-l(1+rlt),
i=2
M t
Rt(Xt) == L(rit - rlt)xit + 1 + rlt ·
i=2
t = 1,2, . . .
(6)
t = 1,2, .. .
(7)
Let us now turn to the basic reinvestment problem which (ignores capital
infusions and distributions and) simply revises the portfolio at discrete points in
time. In view of (5), (6) may be written
t
Wt = Wo exp { LIn Rn(Xn)},
n=l
Defining
(8) becomes
Wt = wo[exp{Gt«(Xt)}]t
= wo(1 + gt)t,
t = 1,2, ....
(8)
(9)
(10)
where gt = exp G t «(Xt) - 1 is the compound growth rate of capital over the first t
periods.
By the law of large numbers,
under mild conditions, Thus, it is evident that for large T,
Wt -+ 0 if E[Gd s 8 < 0,
t 2: T,
(11)
