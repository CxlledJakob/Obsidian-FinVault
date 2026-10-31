# The Kelly capital growth investment criterion _ theory and -- Leonard C_ Maclean, Edward O_ Thorp, W_ T_ Ziemba, Leonard -- World Scientific Handbook -- isbn13 9781283148344 -- bec576e26410d0c695fd5b867d08ec4f -- An.pdf — pages 476–495

--- page 476 ---

Growing Wealth with Fixed-Mix Strategies
447
and sell high'-the common sense dictum of stock market trading. Those assets
whose prices have risen from the last rebalance date will be overweighted in the
portfolio, and their holdings must be reduced to meet the required proportions and
to be replaced in part by assets whose prices have fallen and whose holdings must
therefore be increased. This behavior leads to growth if asset returns exhibit some
stationarity properties.
In Section 2.3, we argued that this explanation is correct for stationary prices.
In the present case, accepting this explanation would mean to fall victim to the
gambler's fallacy. This explanation is not valid because when the price follows a
geometric random walk, the set of its values is generally unbounded and for every
value there is a smaller as well as a larger value. Suppose returns are iid, then 'high'
and 'low' do not have any meaning. Reversion to the long run trend (as postulated
by the ergodic theorem) is not an explanation either: arguing that the longer the
run of black numbers, the higher the odds of red numbers at the next spin of the
roulette wheel is the gambler's fallacy. When returns are determined by the flip of
a coin, an asset's upside and downside potential does not change over time. Such
an asset is not cheap or expensive at any point in time.
5.2
The importance of constancy
A more substantial lacuna in the above reasoning is that it does not reflect the
assumption of constancy of investment proportions. This leads to the question:
what will happen if the portfolio is rebalanced so as to sell all those assets that gain
value and buy only those ones which lose it? (This should lead to an even higher
growth rate -
provided volatility could be 'pumped'.)
Assume, for example, that there are two assets, the price PE of the first (riskless)
is always 1, and the price P; of the second (risky) follows a geometric random walk,
so that the gross return on it can be either 2 or 1/ 2 with equal probabilities. Suppose
the investor sells the second asset and invests all wealth in the first if the price PZ
goes up and performs the converse operation, betting all wealth on the risky asset,
if P; goes down. Then the sequence At = (Al,t, A2,t) of the vectors of investment
proportions will be iid with values (0, 1) and (1 ,0) taken on with equal probabilities.
Furthermore, Atl will be independent of Rt . By virtue of (34), the growth rate
of the portfolio value for this strategy is equal to Eln(RtAt-d = [In(O· 1 + 1 . 2)+
In(O· 1 + 1 . ~) + In(l . 1 + O· 2)+ In(l . 1 + O· ~)l/ 4 = 0, which is the same as the
growth rate of each of the two assets k = 1, 2. But this growth rate is strictly lower
than that of any completely mixed constant proportions strategy.
5.3
Energy-interpretation of volatility
Our results highlight the importance of volatility because fixed-mix strategies do
not produce growth beyond buy-and-hold portfolios in any of the above models
when prices or returns are constant. It is tempting to see volatility as a source of
energy that can be tapped to generate growth.
--- page 477 ---

448
M A. H. Dempster, 1. V. Evstigneev and K. R. Schenk-Hoppe
Indeed, Luenberger (1998) presents an intriguing continuous-time example which
supports this view. (A closely related observation is made in Fernholz and Shay
(1982).) There are K assets whose prices follow independent (but identical) geometric Brownian motions. The constant proportions strategy with equal weights
on all assets has a higher growth rate than any asset price. The remarkable feature
however is that increasing the number of assets K leads to a higher growth rate and
- at the same timeto a reduction in the volatility of the return. It would seem as
if fixed-mix strategies turn the classical return-volatility tradeoff on its head.
The framework for this example is the well-known continuous-time model developed by Merton and others, in which the price processes Sf, t :::: 0, of two
assets k = 1, 2 are supposed to be solutions to the stochastic differential equations dSf / Sf = J.Lkdt + CYkdWtk, where the Wtk are independent (standard) Wiener
processes and S8 = 1. As is well-known, these equations admit explicit solutions
Sf = exp[J.Lkt - (cyV2)t+CYkWn Given some B E (0,1), the value vt of the constant
proportions portfolio prescribing investing the proportions Band 1- B of wealth into
assets k = 1, 2 is the solution to the equation
dvt/vt = [BJ.Ll + (1 - B)J.L2]dt + Bcy1dWl + (1 - B)CY2dW?
Equivalently, vt can be represented as the solution to the equation dvt /vt = pdt +
iTdWt, where p := BJ.Ll + (1- B)J.L2, iT2 := (Bcyd2 + [(1 - B)CY2j2 and Wt is a standard
Wiener process. Thus, vt = exp[pt - (iT2/2)t + iTWt], and so the growth rate and
the volatility of the portfolio value process Vt are given by p - (iT2/2) and iT. In
particular, if J.Ll = J.L2 = J.L and CYl = CY2 = CY, then the growth rate and the volatility
of vt are equal to
(36)
while for each individual asset , the growth rate and the volatility are J.L -
(cy2/2)
and CY, respectively.
Thus, in this example, the use of a constant proportions strategy prescribing
investing in a mixture of two assets leads (due to diversification) to an increase of
the growth rate and to a simultaneous decrease of the volatility. When looking at the
expressions in (36) , the temptation arises even to say that the volatility reduction
is the cause of volatility-induced growth. Indeed, the growth rate J.L -
(iT2/2) is
greater than the growth rate J.L - (cy2/2) because iT < CY. This suggests speculation
along the following lines. Volatility is something like energy. When constructing a
mixed portfolio, it converts into growth and therefore decreases. The greater the
volatility reduction, the higher the growth acceleration.
5.4
A counter-example
Do the observations made in the previous section have any grounds in the general
case, or do they have a justification only in the above example? To formalize this
question and answer it, let us return to the discrete-time framework. Suppose there
--- page 478 ---

Growing Wealth with Fixed-Mix Strategies
449
are two assets with iid vectors of returns R t = (R}, R;). Let (~, 'f}) := (Rt, Rr)
and assume, to avoid technicalities, that the random vector (~, 'f}) takes on a finite
number of values and is strictly positive. The value vt of the portfolio generated
by a fixed-mix strategy with proportions x and 1 - x (0 < x < 1) is computed
according to the formula
t
vt = V1 II[xR~ + (1- x)R;], t ~ 2
n=2
see (33). The growth rate of this process and its volatility are given, respectively,
by the expectation E In (x and the standard deviationv'Var In (x of the random
variable In (x, where (x := x~ + (1- x)'f}. We know from the above analysis that the
growth rate increases when mixing assets with the same growth rate. What can be
said about volatility? Specifically, we consider the following question.
Question 3. (a) Suppose Varln~ = Var In 'f}. Is it true that Varln[x~ + (1- x)'f}] ::;
Varln~ when x E (0, 1)? (b) More generally, is it true that Varln [x~ + (1 - x) 'f}] ::;
max(Varln~, Var In 'f}) for x E (0,1)?
Query (b) asks whether the logarithmic variance is a quasi-convex functional.
Questions ( a) and (b) can also be stated for volatility defined as the square root of
logarithmic variance. They will have the same answers because the square root is a
strictly monotone function. Positive answers to these questions would substantiate
the above conjecture of volatility reduction -
negative, refute it.
In general (without additional assumptions on ~ and 'f}) , the above questions 3(a)
and 3(b) have negative answers. To show this, consider two iid random variables
U and V with values 1 and a > 0 realized with equal probabilities. Consider the
function
f(y) := Varln [yU + (1- y)V], y E [0, 1]
(37)
By evaluating the first and the second derivatives of this function at y = 1/ 2, one
can show the following. There exist some numbers 0 < a_ < 1 and a+ > 1 such
that the function f(y) attains its minimum at the point y = 1/ 2 when a belongs to
the closed interval [a_, a+] and it has a local maximum (!) at y = 1/ 2 when a does
not belong to this interval. The numbers a_ and a+ are given by
a± = 2e4 - 1 ± J(2e4 - 1)2 - 1
where a_ ~ 0.0046 and a+ ~ 216.388. If a E [a_, a+], the function f(y) is convex,
but if a ~ [a_,a+], its graph has the shape illustrated in Figure 2.
Fix any a for which the graph of f(y) looks like the one depicted in Figure 2.
Consider any number Yo < 1/ 2 which is greater than the smallest local minimum
of f(y) and define ~ := YoU + (1 - Yo)V and 'f} := Yo V + (1 - Yo)U. (U and V may
be interpreted as "factors" on which the returns ~ and 'f} on the two assets depend.)
Then Var In[ (~ + 'f}) / 2] > Var In ~ = Var In 'f}, which yields a negative answer both
--- page 479 ---

450
M A. H. Dempster, I. V. Evstigneev and K. R. Schenk-Hoppe
16
15.5 ,1--------------------1
15~------------------_+
14.5 tl-------=======-------I
0.1
0.2
0.3
0.4
0.5
0.6
0.7
0.8
0.9
Figure 2
Graph of the function j(y) in equation (37) for a = 104 .
to (a) and (b). In this example, ~ and 7] are dependent. It would be of interest to
investigate questions (a) and (b) for general independent random variables ~ and 7].
It can be shown that the answer to (b) is positive if one of the variables ~ and 7] is
constant. But even in this case the function Var In[x~ + (1- x)7]] is not necessarily
convex: it may have an inflection point in (0,1), which can be easily shown by
examples involving two-valued random variables.
Thus, it can happen that a fixed-mix portfolio may have a greater volatility than
each of the assets from which it has been constructed. Consequently, the above
conjecture and the 'energy interpretation' of volatility are generally not valid. It is
interesting, however, to find additional conditions under which assertions regarding
volatility reduction hold true. In this connection, we can assert the following fact,
see Theorem 4 in Dempster, Evstigneev, and Schenk-Hoppe (2007).
Theorem 4. Let U and V be independent random variables bounded above and
below by strictly positive constants.
If U is not constant, then one has that
Varln[yU + (1- y)V] < VarlnU for all y E (0,1) sufficiently close to 1.
Volatility can be regarded as a quantitative measure of instability of the portfolio
value. The above result shows that small independent noise can reduce volatility.
This result is akin to a number of known facts about noise-induced stability, e.g.,
Abbott (2001) and Mielke (2000). An analysis of links between the topic of the
present work and results about stability under random noise might constitute an
interesting theme for further research.
5.5
Growth under transaction costs
In this section, we consider an example (a binomial model) in which quantitative
estimates for the size of the transaction costs needed for the validity of the result
--- page 480 ---

Growing Wealth with Fixed-Mix Strategies
451
on volatility-induced growth can be provided. Suppose that there are two assets
k = 1,2: one riskless and one risky. The price of the former is constant and equal
to l. The price of the latter follows a geometric random walk. It can either jump
up by u > 1 or down by u- 1 with equal probabilities. Thus, both security prices
have growth rate zero.
Suppose the investor pursues the constant proportions strategy prescribing to
keep 50% of wealth in each of the securities. There are no transaction costs for
buying and selling the riskless asset, but there is a transaction cost rate for buying
and selling the risky asset of c: E [0, 1). Assume the investor's portfolio at time t - 1
contains v units of cash; then the value of the risky position of the portfolio must
be also equal to v. At time t, the riskless position of the portfolio will remain the
same, and the value of the risky position will become either uv or u-1v with equal
probability. In the former case, the investor rebalances his/her portfolio by selling
an amount of the risky asset worth A so that
v + (1 - c:)A = vu - A
(38)
By selling an amount of the risky asset of value A in the current prices, the investor
receives (1 - c:)A, and this sum of cash is added to the riskless position of the
portfolio. After rebalancing, the values of both portfolio positions must be equal,
which is expressed in (38). From (38) we obtain A = v( u-l)(2-c:) -1. The positions
of the new (rebalanced) portfolio, measured in terms of their current values, are
equal to v + (1- c:)A = v[l+ (1 - c:)(2 - c:)-I(U - 1)]. In the latter case (when the
value of the risky position becomes u- 1v), the investor buys some amount of the
risky asset worth B, for which the amount of cash (1 + c:)B is needed, so that
v - (1 + c:)B = u-1v + B
From this, we find -B = v(u-1 - 1)(2 + c:)-I, and so v - (1 + c:)B = v[l + (1 +
c:)(2 + c:)-1(u-1 - 1)].
Thus, the portfolio value at each time t is equal to its value at time t - 1
multiplied by the random variable ~ such that P{~ = g'} = P{~ = g"} = 1/2, where
g' := 1 + (1 +c: )(2+c:)-1( u-1-1) and g" := 1 + (1-c:)(2 -c:)-1( u-l). Consequently,
the asymptotic growth rate of the portfolio value, Eln~ = (1/2)(lng' + lng"), is
equal to (1/2)ln¢(c:, u), where
[
U-1 - 1] [
u - 1]
¢(c:,u):= 1+(1+c:) 2+c:
1+(1-C:)2_c:
We have Eln~ > 0, i.e., the phenomenon of volatility induced growth takes place,
if ¢(c:, u) > l. For c: E [0,1), this inequality turns out to be equivalent to the
following very simple relation: 0::; c: < (u -l)(u + 1)-1. Thus, given u > 1, the
asymptotic growth rate of the fixed-mix strategy under consideration is greater than
zero if the transaction cost rate c: is less than c:*(u) := (u - l)(u + 1)-1. We call
c:* (u) the threshold transaction cost rate. Volatility-induced growth takes placein
the present example, where the portfolio is rebalanced in everyone periodwhen
o ::; c: < c:* ( u).
--- page 481 ---

452
M A. H. Dempster, 1. V. Evstigneev and K. R. Schenk-Hoppe
The volatility IJ of the risky asset under consideration (the standard deviation
of its logarithmic return) is equal to In u. In the above considerations, we assumed
that IJ-or equivalently, u-is fixed, and we examined ¢(s, u) as a function of s. Let
us now examine ¢(s, u) as a function of u when the transaction cost rate s is fixed
and strictly positive. For the derivative of ¢(s, u) with respect to u, we have
"" ( ) _ 1
+ s [1 -s
-2]
'!-' su - --- --- -u
u'
4 - S2
1 + s
If u = 1, then ¢~(s, 1) < O.
Thus, if the volatility of the risky asset is small,
the performance of the constant proportions strategy at hand is worse than the
performance of each individual asset. This fact refutes the possible conjecture that
'the higher the volatility, the higher the induced growth rate '. Further, the derivative
¢~(s,u) is negative when u E [O,u*(s)), where u*(s) := (1-S)-1/2(1 +S)1/2. For
u = u*(s), the asymptotic growth rate of the constant proportions strategy at hand
attains its minimum value. For those values of u which are greater than u*(s),
the growth rate increases, and it tends to infinity as u ---+ 00. Thus, although the
assertion 'the greater the volatility, the greater the induced growth rate' is not valid
always, it is valid (in the present example) under the additional assumption that
the volatility is large enough.
6
Conclusion
This chapter surveys the authors' recent theoretical work on the phenomenon of
volatility-induced growth. We study the performance of fixed-mix strategies in
markets where asset prices or returns are stationary ergodic. We have established
the surprising result that these strategies generate portfolio growth rates in excess
of the individual asset growth rates, provided some volatility is present. As a
consequence, even if the growth rates of the individual securities all have mean
zero, the value of a fixed-mix portfolio tends to infinity with probability one.
By contrast with the twenty five years in which the effects of 'volatility pumping'
have been investigated in the literature by example, our results are quite general.
They are obtained under assumptions that accommodate virtually all the empirical
market return properties discussed in the literature. We have in this paper also
dispelled the notion that the demonstrated acceleration of portfolio growth is simply
a matter of 'buying low and selling high' or stems from some 'volatilityenergy' link.
The example of Section 5.2 shows that our result depends critically on rebalancing to an arbitrary fixed mix of portfolio proportions. Any such mix defines the
relative magnitudes of individual asset returns realized from volatility effects. This
observation and our analysis of links between growth, arbitrage, and noise-induced
stability suggest that financial growth driven by volatility is a subtle and delicate
phenomenon.
A major obstacle in practical applications of our results is the fact that investment is not over an infinite period. This point has been forcefully argued by
--- page 482 ---

Growing Wealth with Fixed-Mix Strategies
453
Samuelson (1979) , but its validity is not as clear cut as one may be led to believe, see
MacLean, Zhao, and Ziemba (2006), Ziemba (2008) and the discussion in Part IV in
this volume. Other issues are the size of transaction costs in real markets. Though
our findings do hold under sufficiently small proportional transaction costs, this
issue can only be resolved empirically. Another intriguing question is how much
stationarity is present in real markets. All of these questions are left for future
research.
References
Abbott, D. (2001). Overview: Unsolved problems of noise and fluctuations. Chaos 11,
526- 538.
Algoet, P. H. and T. M. Cover (1988). Asymptotic optimality and asymptotic equipartition
properties of log-optimum investment. Annals of Probability, 16, 876- 898.
Arnold, L. (1998). Random Dynamical Systems. New York: Springer.
Arnold, L., I. V. Evstigneev and V. M. Gundlach (1999). Convex-valued random dynamical systems: A variational principle for equilibrium states. Random Operators and
Stochastic Equations, 7, 23- 28.
Aurell, E., R Baviera, O. Hammarlid, M. Serva and A. Vulpiani (2000). A general methodology to price and hedge derivatives in incomplete markets. International Journal of
Theoretical and Applied Finance, 3, 1- 24.
A urell , E. and P. Muratore-Ginanneschi (2000) . Financial friction and multiplicative
Markov market games. International Journal of Theoretical and Applied Finance,
3, 501- 510.
Billingsley, P. (1965). Ergodic Theory and Information. New York: John Wiley.
Breiman, L. (1961). Optimal gambling systems for favorable games. In Proceedings of
the Fourth Berkeley Symposium on Mathematical Statistics and Probability, Vol. 1
(ed. Neyman, J.) , pp. 65-78. LA: University of California Press.
Browne, S. (1998). The return on investment from proportional portfolio strategies.
Advances in Applied Probability, 30, 216- 238.
Browne, S. and W. Whitt (1996). Portfolio choice and the Bayesian Kelly criterion.
Advances in Applied Probability, 28, 1145- 1176.
Cover, T. M. (1991). Universal portfolios. MathematicaL Finance, 1, 1- 29.
Cover, T. M. (1998). Shannon and investment. IEEE Information Theory Society Newsletter, Summer 1998, Special Golden Jubilee Issue, pp. 10- 11.
Dempster, M. A. H., I. V. Evstigneev and K. R Schenk-Hoppe (2003). Exponential
growth of fixed-mix strategies in stationary asset markets. Finance (3 Stochastics, 7,
263- 276.
Dempster, M. A. H., 1. V. Evstigneev and K. R Schenk-Hoppe (2007). Volatility-induced
financial growth. Quantitative Finance, 7, 151- 160.
Dempster, M. A. H., 1. V. Evstigneev and K. R Schenk-Hoppe (2008). Financial Markets:
The joy of volatility. Quantitative Finance, 8, 1- 3.
Dempster, M. A. H., M. Germano, E. A. Medova and M. Villaverde (2003). Global asset
liability management. British Actuarial Journal, 9, 137- 195.
Dries, D., A. Ilhan, J. Mulvey, K. D. Simsek and R Sircar (2002). Trend-following hedge
funds and multi-period asset allocation. Quantitative Finance, 2, 354- 361.
Evstigneev, LV., T. Hens and K. R Schenk-Hoppe (2009a). Evolutionary Finance. In
Handbook of Financial Markets: Dynamics and Evolution (eds. Hens, T. and Schenk-
Hoppe, K. R), Chapter 9, pp. 507-566. Amsterdam: North-Holland.
--- page 483 ---

454
M A. H. Dempster, 1. V. Evstigneev and K. R. Schenk-Hoppe
Evstigneev, 1. V., T . Hens and K. R . Schenk-Hoppe (2009b) . Evolutionary stability of
investment rules.
Evstigneev, 1. V. and D. Kapoor (2006). Arbitrage in stationary markets. Discussion Paper
0608, School of Economic Studies, University of Manchester.
Evstigneev, 1. V. and K. R. Schenk-Hoppe (2002). From rags to riches: On constant
proportions investment strategies. International Journal of Theoretical and Applied
Finance, 5, 563-573.
Fernholz, R. and B. Shay (1982). Stochastic portfolio theory and stock market equilibrium.
Journal of Finance, 37, 615- 624.
Fernholz, E. R. (2002) . Stochastic Portfolio Theory. New York: Springer.
Fernholz, E. R. and 1. Karatzas (2005). Relative arbitrage in volatility-stabilized markets.
Annals of Finance, 1, 149-177.
Fernholz, E . R. , 1. Karatzas and C. Kardaras (2005). Diversity and arbitrage in equity
markets. Finance CJ Stochastics, 9, 1- 27.
Hakansson, N. H. and W. T. Ziemba (1995) . Capital Growth Theory. In Handbooks
in Operations Research and Management Science, Vol. 9, Finance (eds. Jarrow,
R. A. , Maksimovic, V. and Ziemba, W. T.) , Chapter 3, pp. 65- 86. Amsterdam:
North-Holland.
Huberman, G. (1982). A simple approach to Arbitrage Pricing Theory. Journal of Economic Theory, 28, 183- 19l.
Kabanov, Yu. M. (1999). Hedging and liquidation under transaction costs in currency
markets. Finance CJ Stochastics, 3, 237- 248.
Kabanov, Yu. M. and D. A. Kramkov (1994) . Large financial markets: Asymptotic arbitrage and contiguity. Theory of Probability and its Applications, 39, 222- 228.
Kabanov, Yu. M. and Ch. Stricker (2001). The Harrison- Pliska arbitrage pricing theorem
under transaction costs. Journal of Mathematical Economics, 35, 185- 196.
Kelly, J. (1956). A new interpretation of information rate. Bell System Technical Journal,
35, 917- 926.
Kemeny, J. G. and J. L. Snell (1960). Finite Markov Chains. New York: Van Nostrand.
Klein, 1. and W. Schachermayer (1996). Asymptotic arbitrage in non-complete large financial markets. Theory of Probability and its Applications, 41, 927- 934.
Kuhn, D. and D. G. Luenberger (2010). Analysis of the rebalancing frequency in logoptimal portfolio selection. Quantitative Finance. (Forth coming).
Li, y. (1998). Growth-security investment strategy for long and short runs. Management
Science, 39, 915- 924.
Luenberger, D. G. (1998). Investment Science. UK: Oxford University Press.
MacLean, L. C., Y. Zhao and W. T . Ziemba (2006). Dynamic portfolio selection with
process control. Journal of Banking and Finance, 30, 317- 339.
MacLean, L. C., W. T. Ziemba and G. Blazenko (1992) . Growth versus security in dynamic
investment analysis. Management Science, 38, 1562- 1585.
Mielke, A. (2000). Noise induced stability in fluctuating bistable potentials. Physical Review Letters, 84, 818- 82l.
Mulvey, J. M. (2001). Multi-period stochastic optimization models for long-term investors. In M. Avellaneda (Ed.) , Quantitative Analysis in Financial Markets, Vol. 3,
pp. 66- 85. Singapore: World Scientific.
Mulvey, J. M. (2009). Applying Kelly and related strategies during turbulent markets.
Mulvey, J. M., C. Ural and Z. Zhang (2007) . Improving performance for long-term investors: Wide diversification, leverage, and overlay strategies. Quantitative Finance,
7, 175- 187.
Perold, A. F. and W. F. Sharpe (1988). Dynamic strategies for asset allocation. Financial
Analysts Journal, 44, 16-27.
--- page 484 ---

Growing Wealth with Fixed-Mix Strategies
455
Radner, R. (1971). Balanced stochastic growth at the maximum rate. In C. Bruckman and
W . Weber (Eds.), Contributions to the von Neumann Growth Model (Zeitschrijt fur
Nationalokonomie, Suppl. 1), pp. 39- 62. New York: Springer.
Ross, S. A. (1976). The arbitrage theory of asset pricing. JournaL of Economic Theory, 13,
341- 360.
Samuelson, P. A. (1979). Why we should not make mean log of wealth big though years
to act are long. Journal of Banking and Finance, 3, 307- 309.
Thorp, E. O. (1971) . Portfolio choice and the Kelly criterion. In Business and Economics
Statistics Section, Proceedings of the American StatisticaL Association, pp. 215- 224.
Reprinted in: Stochastic Optimization Models in Finance (eds. Ziemba, W. T. and
Vickson, R. C .) , pp. 599-619. US: Academic Press (1975, reprinted in 2006).
Ziemba, W. T. (2008). The Kelly Criterion. The Actuary, September issue, Features:
Investment.
Ziemba, W. T. and J. M. Mulvey (eds.) (1998). Worldwide Asset and Liability Modeling.
UK: Cambridge University Press.
--- page 485 ---

Part IV
Critics and assessing the good and
bad properties of Kelly
--- page 486 ---

This page is intentionally left blank
--- page 487 ---

This page is intentionally left blank
--- page 488 ---

Growing Wealth with Fixed-Mix Strategies
455
30
Introduction to the Good and Bad Properties of Kelly
Multiperiod lifetime investment-savings optimization dates at least to Ramsey
(1928). Phelps (1962) extended the model to include uncertainty while maximizing expected utility of lifetime consumption by choosing between consumption and
investment in a single risky asset using an additive utility function. He obtained
explicit solutions for a constant member of the isolastic utility class. Samuelson
(1969) and Merton (1969) in companion articles develop, following Ramsey (1928)
and Phelps (1962), in both discrete-time and continuous time, lifetime portfolio
selection models where the objective function is the discounted sum of concave
functions of period by period consumption. Samuelson solves the case when there
are interior maxima, and shows that for isoelastic period by period utility functions
u' (C) = Co -1, 0 < 1, the optimal portfolio decisions are independent of current
wealth at each stage and independent of all consumption-savings decisions with a
stationary optimal policy to invest a fixed proportion of current wealth in each period. Ziemba and Vickson (2010) review this literature and point to some queries
regarding the validity of the interior maxima as discussed in problems in Ziemba
and Vickson (1975, 2006).
For log utility, 0 -+ 0, Samuelson (1969) showed that the optimal decision splits
into two independent parts with the Ramsey savings problem independent of the
lifetime portfolio selection problem. Log utility frequently splits the problem in this
way, see Rudolf and Ziemba (2004) reprinted in part VI of this book for a similar
splitting in a multi period pension model.
Samuelson (1971) focuses on the third point of his 1979 paper that follows. He
states the following result which has broad agreement.
Theorem: If one acts to maximize the geometric mean at each step, and if the
period is "sufficiently long", "almost certainly" higher terminal wealth and terminal
utility [for a log utility investor]l will result than from any other [essentially different]
decision rule.
Samuelson points out the following:
False Corollary: If maximizing the geometric mean almost certainly leads to a
better outcome, then the expected utility of its outcomes exceeds that of any other
rule, provided T is sufficiently large.
The editors of this book agree with Samuelson that the E log maximization is
for the special utility function u( w) = log w and not for other utility functions.
1 [] indicate phrase added by the editors
--- page 489 ---

460
L. C. MacLean, E. 0. Thorp and W. T. Ziemba
Samuelson presents one example that illustrates this. Samuelson's criticisms are
with the pure theory and not in conflict with any of the conclusions of this book,
much of which is summarized in the papers in this part of the book. But he ends
with the observation that his critical remarks
" .. . do not deny that this criterion, arbitrary as it is, still avoids
some of the even greater arbitrariness of conventional meanvariance analysis. Its essential defect is that it attempts to replace the pair of "asymptotically sufficient parameters" E log X i,
Variance(logXi ) by the first of these alone, thereby gratuitously
ruling out arbitrary 'Y in the family u(x) =
x '" in favor of
"I
u(x) = log x".
Luenberger (1993), reprinted in part V, provides a careful analysis of these two
parameters. The paper on Kelly simulations in part IV by MacLean et al. also
considers both parameters in an analysis of proportional investment strategies.
Samuelson' paper (1979) is written in a style, with one syllable words, that is
hard to read, but when you cut through the language he makes a few points:
(1) Those who follow the rule maximization of mean log of wealth will with higher
and higher probability have more wealth in the long run than those that use
an [essentially different] strategy. This is agreed and is one of the basic results
due to Breiman and others.
(2) Some of those who have favorable asset returns period by period and maximize
the expected log of wealth can lose a lot and in fact almost all of their wealth.
This is agreed and examples of this are in the simulation paper by MacLean,
Thorp, Zhao and Ziemba (MTZZ) (2010) which appears in this part of the book.
While the Kelly expected log criterion faced with favorable positive expectation
bets will provide very high returns much of the time, in a small percent of the
time there will be huge losses. In one example in Ziemba and Hausch (1986),
which is redone in MTZZ with a 14% advantage on each play you can lose 98%
of your initial wealth. Of course, with fairly high probability, you can achieve
a 10- or 100- fold increase in your initial wealth. This is, of course, the pure
theory and in actual applications by hedge funds and other investors, financial
engineering methods may be used to limit losses should they occur.
(3) Latane (1959, 1978) seems to have claimed (although even that is debatable)
that the expected log maximizing strategy is in some sense better than a strategy based on some other utility function, this is not discussed or claimed by
those involved with this book. The expected log maximizing strategy is about
long run wealth maximizing most of the time. The only utility functions used
are log in general for full Kelly and negative power in the special case with log
normally distributed assets. The papers in this part of the book discuss these
and other points further.
--- page 490 ---

Introduction to the Good and Bad Properties of Kelly
461
Markowitz (1976) argues that when one traces out the set of mean-variance
(MV) efficient portfolios, one passes through a portfolio which gives approximately
the maximum E log X. Thorp (1969) gives an example of an asset distribution
such that the Kelly log optimal portfolio is not on the efficient frontier, so the
approximation is not exact. Markowitz argues that this Kelly portfolio should be
considered the upper limit for conservative choice among E,V efficient portfolios,
since portfolios with higher (arithmetic) mean give greater short-run variability with
less return in the long run. A real investor might prefer a lower mean and variance
giving up return in the long run for stability in the short run. Markowitz (1952)
conjectured and Young and Trent (1969) proved that
Elog(Xi ) ~ logE - ~ {;2}
for a wide class of ex post distributions of portfolio returns, where X = gross return,
E=EX and V=VarX.
Thorp (2008) provides an introduction to the Kelly criterion and discusses a
number of interesting topics about it. His paper and the following ones on simulations of Kelly returns and good and bad properties show what Kelly strategies do
and do not do. Thorp begins with how he coined the term "Fortune's Formula" in
1960 in his blackjack application, where he developed favorable card counting strategies that have had a huge impact across the world. He discusses various examples
and paradoxes and the issue of bet concentration, that is, limited diversification.
Experts with good asset situations can plunge heavily into a few assets as Warren
Buffett has done. Thorp's treatment and Ziemba's paper on great investors in part
VI of this book provide clues that Buffett acts like a Kelly bettor. Buffett himself
argues that amateurs are likely better off diversifying into index funds, after all,
they beat about 75% of the professional managers in net returns with essentially no
work. Thorp cautions the reader against common errors in the application of Kelly
betting such as the failure to consider all investments, risk tolerance misjudgments,
forgetting how aggressive Kelly betting is in the short run, overbetting because of
data errors, forgetting about the impact of bad scenario black swans and forgetting
that most of the superior Kelly betting properties are for the very long run. He
presents some results on fractional Kelly wagering that supplement the papers in
part III of this book. He discusses the subtle concept of "essentially different" that
confounds even some top experts. He discusses some subtleties such as strategies
that can beat Kelly strategies. An important topic is the use of Kelly strategies
by great investors trying to multiply their fortunes, akin to the Kelly property
that it will get you to a wealth goal faster than any other essentially different
strategy for asymptotically high goals. Thorp shows the relationship between fractional Kelly strategies and Markowitz mean-variance strategies with the full Kelly
being the limiting portfolio on this surface supplementing the Markowitz paper
discussed above.
--- page 491 ---

462
L. C. MacLean, E. O. Thorp and W T Ziemba
Thorp also discusses and deals with Paul Samuelson's criticisms of Kelly investment strategies and his discussion supplements the three Samuelson papers and the
last papers in this part. The editors of this book agree that even when you make
a long sequence of very good bets, you can, in fact, lose and the loss can be a lot.
But most of the time you win a lot. Thorp mentions two papers he co-authored
in the 1970s which show that different utility functions indeed have different optimal solutions. That, as fully discussed in the Thorp and Whitley's (1972) paper
reprinted here, deals with the false notion that Kelly proponents think that log
optimal strategies are optimal for other concave utility functions, which notion is
neither claimed nor true.
Thorp's paper concludes with a discussion of Proebsting's paradox which shows
you can make a series of favorable bets and be asymptotically ruined. But the
paradox needs a series of correlated bets made at different points in time to show
this result. So it does not contradict the property that betting full Kelly or any
fixed fraction less than full Kelly leads to exponential growth assuming the bets are
independent (as in Breiman's paper in part I or have weak dependence as in Cover's
papers in part II or Thorp's paper in part VI).
One approach to successfully model black swans is to use a scenario optimization
stochastic programming model where you include the possibility of an extreme
event, specifying its consequences but not actually indicating the nature of the event
(see Geyer and Ziemba (2008) for the application to the Siemens Austria Pension
Fund). Correlations change as the scenario sets move from normal conditions to
volatile to crash which include the black swans (see also Ziemba (2003) for additional
applications of this approach). This is, of course, fully applicable to Kelly betting
and will lower the wager.
Thorp and Whitley (1972) show, for interesting concave utilities, that different
utility functions, namely those which differ by more than a positive linear transformation, have distinctly different sets of optimal strategies. Moreover, for the case
of cash and a two valued risky investment, the optimal strategies are unique. This
means that if two utility functions have the same set of optimal strategies for each
such investment, then these two utility functions are equivalent, that is, they are
positive linear transformations of one another. Hence, given any concave utility different from log there are investment settings in which the two utilities have different
optimal strategies. Thorp and Whitley show that utility functions that are close to
one another may have very different optimal solutions. Kallberg and Ziemba (1983)
show that two utility functions with the same Rubinstein risk aversion,2 under the
assumption of normality, will have the same sets of optimal solutions. Thorp and
Whitley show that for two continuous non-decreasing utility functions that are not
equivalent, there is a one-period two security investment setting such that these
two utility functions have distinct optimal strategies if either (a) the two utility
2The Rubinstein risk aversion - ~~::g::1 wo is a constant.
--- page 492 ---

Introduction to the Good and Bad Properties of Kelly
463
functions are either concave or convex, or (b) they have a second derivative that
exists except possibly for a set of isolated points.
Short term Kelly and even fractional Kelly strategies are very risky since the
Arrow-Pratt risk aversion index is very low. MacLean, Thorp, Zhao and Ziemba
(2010) present three simple investment situations to simulate the behavior of full
Kelly and fractional Kelly over medium time horizons. These simulations extend
and redo over longer horizons with more scenarios earlier studies by Bicksler and
Thorp (1973) and Ziemba and Hausch (1986). The results show that:
(1) The great superiority of full Kelly and close to full Kelly strategies over medium
term horizons (40 to 700 periods) with very large gains a large fraction of
the time.
(2) The short term performance of Kelly and high fractional Kelly strategies is
very risky.
(3) There is a well defined and consistent tradeoff of growth versus security as a
function of the bet size determined by the various strategies.
(4) No matter how favorable the investment opportunities are or how long the finite
horizon is, a sequence of bad scenarios can lead to poor final wealth outcomes
with a loss of most of the investor's initial capital.
The calculations show the final wealth distributions including possible huge gains
and huge losses and show the fraction of the time these are likely to occur. Meanvariance tradeoffs are shown versus the Kelly fraction. The mean is highest for full
Kelly and decreases for lower and higher Kelly fractions. The variance increases
with the Kelly fraction confirming that full Kelly is very volatile. The minimum
and maximum wealth levels are shown versus the Kelly fraction. The wealth accumulated from the full Kelly strategy does not stochastically dominate fractional
Kelly strategies. To lower risk, one must lower the Kelly fraction. The results
showed that for reasonable horizons with three different experiments, that the full
Kelly and fractional Kelly strategies are not merely long run approaches. Proper use
over short and medium time horizons can yield good wealth goals while protecting
against drawdowns most of the time.
The Kelly criterion has many good long-term properties and some favorable
short-term properties. MacLean, Thorp, and Ziemba (2010) discuss the good and
bad properties of the Kelly criterion. The main advantage is the long run growth
rate maximization. That is an asymptotic mathematical result. Also the medium
term simulation results show that most of the time the Kelly bettor has a lot higher
final wealth than that from other strategies. But for a small percentage of the
time, despite many periods of play with very favorable investments, there can be
huge losses. Besides this, the main disadvantage of the Kelly criterion is that it is
very risky short term and the near zero Arrow-Pratt risk aversion index typically
leads to wild swings in the wealth path. But the Kelly strategy has favorable short
run competitive optimality compared to other strategies. Moreover, the extreme
--- page 493 ---

464
L. C. MacLean, E. O. Thorp and W T Ziemba
sensitivity of E log to errors in the mean signals that mean estimates must be
carefully and conservatively estimated to avoid overbetting which can lead to large
portfolio losses. Fractional Kelly strategies such as half Kelly, moderate this but
they can still have large losses. There is a tradeoff of lower growth for more security
as the Kelly fraction is reduced and more is invested in riskless cash. Also it may
take a long time for the Kelly bettor to dominate an essentially different strategy
with high probability. No one disagrees with the Samuelson objection that E log
maximizing policies are optimal for only log utility functions. Thorp and Whitley's
(1972, 1974) result shows that this "objection" is simply a universal fact, true for
all utilities. None the less, the long run properties indicate very high final wealth
most of the time for Kelly and fractional Kelly bettors.
--- page 494 ---

Review of Economics and Statistics, 51,239- 246 (1969)
465
31
LIFETIME PORTFOLIO SELECTION
BY DYNAMIC STOCHASTIC PROGRAMMING
Paul A. Samuelson *
Introduction
MOST .analyses of portfolio selection,
whether they are of the Markowitz·
Tobin mean-variance or of more general type,
maximize over one period.1 I shaD here formu·
late and solve a many-period generalization,
corresponding to lifetime planning of consumption and investment decisions. For simplicity
of exposition I shall confine my explicit discussion to special and easy cases that suffice to
illustrate the general principles involved.
As an example of topics that can be investigated within the framework of the present
model, consider the question of a "businessman risk" kind of investment. In the literature '
of finance, one often reads; "Security A should
be avoided by widows as too risky, but is highly
suitable as a businessman's risk." What is involved in this distinction? Many things.
First, the «businessman" is more affluent
than the widow; and being further removed
from the threat of falling below some sub·-
sistence level, he has a high propensity to
embrace variance for the sake of better yield.
Second, he can look forward to a high salary
in the future; and with so high a present discounted value of wealth, it is only prudent for
him to put more into common stocks compared
to his present tangible wealth, borrowing if
necessary for the purpose, or accomplishing
the same thing by selecting volatile stocks that
widows shun.
,. Aid from the National Science Foundation", gratefully
acknowledged. Robert C. Merton has provided me with
much stimulus; and In a companion paper in this issue of
the RE\II£W he is tackling the much harder problem of
optimal control in tbe presence of continuous-time stochastic variation. lowe thanks also to Stanley Fi!cher.
'See for example Harry Markowitz [51; James TobIn
[14], Paul A. S"muelson [10]; Paul A. Samuelson and
Robert C. M~ton [1.1]. See, however, James Tobin [151,
for a pioneermg treatment of the multi.period portfolio
problem; and Jan Massin [7] which overlaps with the
pr=nt analysis in showing how to solve tbe basic dynamic
stochastic program recursively by worldng backward from
the end in tbe Bdlman fashion, and which prov,", the
theorem tbat portfolio proportions wilt be invariant only
if the marginal utility function is iso-elastic.
Third, being still in the prime of life, the
businessman can "recoup" any present losses
in the future. The widow or retired man nearing life's end has no such "second or nIh
chance."
Fourth (and apparently related to the last
point), since the businessman will be investing
for so many periods, "the law of averages will
even out for him," and he can afford to act
almost as if he were not subject to diminishing
marginal utility.
What are we to make of these arguments?
It wiD be realized that the first could be purely
a one-period argument. Arrow Pratt and
h
2
'
,
ot ers
have shown that any investor who
faces a range of wealth in which the elasticity
of his marginal utility schedule is grea.t will
have high fisk tolerance; and most writers
seem to believe that the elasticity is at its
highest
for
rich -
but not ultra-rich!-
people. Since the present model has no new
insight to offer in connection with statical risk
tolerance, I shall ignore the first point here
and confine almost all my attention to utility
functions with the same relative risk aversion
at all levels of wealth. Is it then still true that
lifetime considerations justify the concept of
a businessman's risk in his prime of life?
Point two above does justify leveraged investment financed by borrowing against future
earnings. But it does not rea.lIy involve any
increase in relative risk-taking once we have
related what is at risk to the proper larger base.
(Admittedly, if market imperfections make
loans difficult or costly, recourse to volatile,
"leveraged" securities may be a rational procedure.)
The fourth point can easily involve the innumerable fallacies connected with the "law of
large numbers." I have commented elsewhere a
on the mistaken notion that multiplying the
same kind of risk leads to cancellation rather
'See K. Arrow [ll i J. Pratt [9] i P. A. Samuelson and
R. C. Merton [L31.
'P. A. Samuelson [111.
(H9 ]
--- page 495 ---

466
P A. Samuelson
240
THE REVIEW OF ECONOMICS AND STATISTICS
than augmentation of risk.
I.e., insuring
many ships adds to risk (but only as Vn) j
hence, only by insuring more ships and by
also subdividing those risks among more people
is risk on each brought down (in ratio l/Vn).
However, before writing this paper, I had
thought that points three and four could be
refmmulated so as to give a valid demonstration of businessman's risk, my thought being
that investing for each period is akin to agreeing to take a l/ntb. interest in insuring n independent ships.
The present lifetime model reveals that investing for many periods does not itself introduce extra tolerance for riskiness at early,
or any, stages of life.
Basic Assumptions
The familiar Ramsey model may be used as
a point of departure. Let an individual maximize
11' e-pt U[C(t) ]dt
(1)
subject to initial wealth Wo that can always be
invested for an exogeneously-given certain .
rate of yield Y; or subject to the constraint
C{t) = rW(t) -
W{t)
(2)
If there is no bequest at death, terminal wealth
is zero.
This leads to the standard calculus-of-variations problem
J = Max jTe_pj U[rW -
W]dt
(3)
{W(t)}
0
This can be easily related' to a discretetime formulation
Max::S~_ o (l+p)-tU[Ctl
(4)
subject to
WH1
)
Ct=W.---
(S
1+ r
or,
Max :s~~ o (l+p)-t U [ Wt -
W1+t+l ]
{W,}
r
(6)
• See P. A. Samuelson [12], p. 273 for an exposition of
discrete-time analogu.. to calculus-of-variations models.
Note: here I assume tJu.t consumption, C t, takes plate at
the beginning rath~r than at the end of the petlod. This
change alters slightly the appearance of the equilibrium
conditio,,", but not their substance.
for prescribed (Wo, W'I'+l). Differentiating
partially with respect to each WI in turn, we
derive recursion conditions for a regular interior maximum
(1+ .. ) U'[ Wt - 1 -
Wt ]
1+1'
l+r
= U' [ Wt _Wt +1 ]
1+1'
(7)
If U is concave, solving these second-order
difference equations with boundary conditions
(Wo, W 'l'+l) will suffice to give us an optimal
lifetime consumption-investment program.
Since there has thus far been one asset, and
that a safe one, the time has come to introduce
a stochastically-risky alternative asset and to
face up to a portfolio problem. Let us postulate
the existence, alongside of the safe asset that
makes $1 invested in it at time t return to you
at tbe end of the period $1 (1 + ,), a risk asset
that makes $1 invested in, at time t, return to
you after one period $lZ" where Z, is a random
variable subject to the probability distribution
Prob {Z, ;;a z} = P(2) .
Z ~ 0
(8)
Hence, Z'+l -
1 is the percentage "yield" of
each outcome. The most general probability
distribution is admissible: i.e., a probability
density over continuous g'S, or finite positive
probabilities at discrete values of z. Also I
shall usually assume independence between
yields at different times so that P(zo, 2 1, • • • ,
Zt, ... ,2.'1') = P(Zt)P(Zl) ... P(ZT)'
For simplicity, the reader might care to deal
with the easy case
Prob {Z = .\.} = 1/ 2
= Prob{Z= >..-l},
.\.>1
(9)
In order that risk averters with concave utility
should not shun this risk asset when maximizing the expected value of their portfolio, A must
be large enough so that the expected value of
the risk asset exceeds that of the safe asset, Le.,
1
1
_,\. + _.\ -1 > 1 + 1', or
2
2
A > 1 + r + y2r + r~ .
Thus, for A = 1.4, the risk asset has a mean
yield of 0.057, which is greater than a safe
asset's certain yield of , = .04.
At each instant of time, what will be the
optimal fraction, W" that you should put in
