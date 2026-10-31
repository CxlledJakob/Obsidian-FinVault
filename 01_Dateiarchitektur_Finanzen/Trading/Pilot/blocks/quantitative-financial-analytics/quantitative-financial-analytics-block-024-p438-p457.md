# Quantitative financial analytics_ the path to investment profits.pdf — pages 438–457

--- page 438 ---

Risk, Uncertainty, Utility and Portfolio Theory
415
appears even more divorced from reality. Additional measures seem
required.
The implications of risk aversion varying over wealth levels and
especially, diminishing as wealth increases have been investigated.
A measure of local risk aversion (for small changes in wealth) r(W),
equal to the following:
r(W) = −U′′(W)
U′(W) .
The argument continues on to demonstrate that local risk aversion
is a decreasing function of wealth if and only if the premium
required to undertake any given risk declines as assets rise. It further
demonstrates that this requirement, r′(W) ≤0, is equivalent to the
condition U′′(W)U′(W) ≥[U∗(W)]2. A measure of proportional risk
aversion, r∗(W) = W × r(W) may also be introduced along with an
analysis and clariﬁcation of various functions in terms of constant,
increasing, or decreasing proportional and absolute risk aversion. One
example of constant risk aversion (the special case of no aversion) is
U(W) = f(W); an example of constant proportional risk aversion is
U(W) = f(log W).
Portfolio Theory
For the last 70–80 years, a very clear division has existed between the
work of the security analyst and that of the portfolio manager. The
analyst attempts to divide the universe of securities into three parts:
(1) underpriced (recommended purchase); (2) fully priced (recommended long-run hold); and (3) overpriced (no longer recommended).
The portfolio manager then constructs groups of securities into
recommended holdings based on risk/return characteristics. The ﬁrst
decision to be made usually involves the breakdown between stocks
and bonds; a general heuristic is to place enough of the portfolio in
bonds so that the interest payments, plus a token dividend from the
remainder in stocks, would meet the minimum income requirement
of the portfolio in all but the very worst of years. Beyond this
consideration, the ratio of bonds to stocks might also be varied
--- page 439 ---

416
Quantitative Financial Analytics
depending upon the manager’s view of the cycle (more bonds at the
peak of a boom, and so on). The bond portfolio would then be divided
among governments, municipals (depending upon the portfolio’s tax
status), industrials, utilities, and transportation issues according to
perceived risk or the manager’s tastes; diversiﬁcation by maturity
was also obtained (to avoid the necessity of reinvesting large sums at
any future point in time). The stock portfolio would be apportioned
among cyclical, defensive, and growth issues on the basis of income
required, state of the market, and the ability to bear risk. Among the
three stock categories, further allocations by industry might be made.
Finally, with the bond portfolio apportioned by type and maturity
range and the stock portfolio apportioned by industry, the manager
would select the appropriate securities in the apportioned amounts
from the analyst’s list of recommendations.
Following the above sequence, the proverbial widow (in a pre-
Fem-lib era) who had just received a bequest would generally have
minimum income needs that would be quite large in relation to her
principal and extend over a long time. Because a failure to earn
the required income would quickly exhaust her capital and make
her a public charge (in the days before receiving welfare became
fashionable), the portfolio manager would apportion most, if not all,
of her portfolio to bonds (and governments at that); any equities
purchased would also be of a defensive-income variety. On the other
hand, the proverbial successful businessman (or businesswoman in
today’s more egalitarian world) would generally have enough other
assets and income to make no current income requirements of his or
her portfolio and also to be able to endure a fair amount of risk. Thus,
the portfolio manager would allocate most of the funds to equities
and, with no income constraint, much of that to growth companies.
Therefore, the resulting portfolios of government bonds for widows
and of high-risk growth stocks for businesspeople were derived by the
systematic application of the same decision framework to diﬀering
individual circumstances.
Institutional portfolio regulations and policies were derived
in a similar manner. Because banks’ assets represent the funds
of depositors and life insurance companies’ investments represent
--- page 440 ---

Risk, Uncertainty, Utility and Portfolio Theory
417
policyholders’ reserves, it was felt that little risk could be undertaken;
portfolio regulation of these institutions reﬂects this philosophy. On
the other hand, institutions like mutual funds are closer to the
concept of “businessman’s risk,” and, consequently, they are not as
severely regulated in regard to the risk of the assets they may hold.
The major diﬃculty with the approach outlined above is that it
is based upon the assumption that portfolio risk is a weighted sum
of the total risk of the component securities, considered in isolation;
as demonstrated in the next section of this chapter, this is simply
untrue. Another unfortunate assumption of the above methodology is
that the “interior decorator” approach to security selection (“a little
of this, a little of that”) results in eﬃcient diversiﬁcation; as indicated
below, this contention is also incorrect.
The impact of the modern theory upon the role of security
analysis has been implied in the previous chapters. It will be noted
that securities have not been “priced” in this book, because securities
cannot be priced upon the basis of their risk considered in isolation
from other securities; furthermore, security purchasers are price
takers, not price makers. The function of the security analyst has
been viewed here to be the estimation of security return, risk, and
covariance with the returns of the securities (perhaps employing
a market index, as considered later in this chapter). Thus, the
portfolio manager should no longer be provided with a buy, hold,
or sell recommendation, but rather an estimate of the parameters
of the distribution of security returns. At least, this is true in
theory. In fact, most analysts today still “price” stocks and provide
recommendations accordingly. Stocks have “price” objectives; and
when they are reached or the objective is changed, a “sell” or “fully
priced” recommendation is issued.
The considerations of client-required return and ability to bear
risk should be treated in the form of utility function determination.
The goal is the same, but the use of a utility framework is more
precise and also allows for trade-oﬀs between risk and return. The
proverbial widow would have a very risk-averse function (which,
as demonstrated in the rest of this chapter, will cause a low-risk
portfolio to be chosen), and the proverbial businessperson will have
--- page 441 ---

418
Quantitative Financial Analytics
a less risk-averse function (and a riskier portfolio). Under the modern
theory, then, the manager takes the analyst’s parameters, determines
for each level of risk that portfolio with the highest attainable return
(the eﬃciency frontier, derived in the next section), compares the
market’s trade-oﬀof risk and return to his client’s preferences, and
selects the utility-maximizing portfolio.
The goal of portfolio management, like all other human endeavors, is thus assumed to be utility maximization. It has further been
demonstrated that this goal is operationally similar to the more
traditional goals (for example, income, limited income with growth,
and so on), because it will have diﬀerent operational implications for
individuals in diﬀering circumstances and of diﬀering risk predilections. In addition, the goal of institutional portfolio management
should be the maximization of beneﬁciary utility. If markets are
eﬃcient, the last goal can be achieved by an institutional portfolio
policy designed to place the parameters of its own securities on the
highest attainable market (risk-return trade-oﬀ) line; this policy will
maximize the market value of investors’ holdings, from which point
they can go about the maximization of their own utility in isolation.
If markets are not eﬃcient, the institution will need to adopt a
“clientele” approach, estimate a utility function representative of its
beneﬁciaries, and work to put the parameters of its own securities
on the highest attainable indiﬀerence curve of the posited utility
function.
In theory, the goal of portfolio management is utility maximization, and the institutional objective is the maximization of
the market value of the wealth of the portfolio beneﬁciary. The
ﬁrst step in this process is an understanding of the eﬀects of
diversiﬁcation upon risk and return. The simplest way to begin is
with an examination of the two-asset portfolio.
Suppose that we were oﬀered the opportunity to bet $1 against
$2 on a fair coin being ﬂipped “heads,” or the same odds on “tails.”
The expected value of such an opportunity is [(0.5)(+2)+(0.5)(−1) =
50 cents] and, because of the small sum involved, we would probably
overlook the risk [σ =

(2.00 −0.50)2(0.5) + (−1.00 −0.50)2 =
$1.50] and undertake the bet. If, however, the stakes were raised to
--- page 442 ---

Risk, Uncertainty, Utility and Portfolio Theory
419
$100,000 against $200,000, our enthusiasm for the $50,000 expected
value might well be tempered by the $150,000 standard deviation; at
the least, some reference to utility considerations would be required.
These diﬃculties could be overcome if we were allowed to
subdivide our $1 (or $100,000) bet into one-half on “heads” and
one-half on “tails” of the same coin. In this case, we would lose $0.50
on one bet and win $1.00 on the other each time. Thus, the expected
value of the game would remain $0.50, but the risk would be totally
eliminated. The reduction in risk is eﬀected because our winning is
contingent upon the outcome of several events that do not always
occur together (are not perfectly positively correlated). Indeed, we
were able to eliminate risk in our example because our events (both
sides of the same coin) were perfectly negatively correlated. The
existence of events (that is, the return on securities) that are less
than perfectly positively correlated with each other gives rise to the
concept of diversiﬁcation for risk reduction that underlies portfolio
theory.
The expected return on a portfolio of assets is simply the
weighted average of their individual expected returns, or
Let:
µ = expected return on portfolio
αi = proportion of portfolio invested in ith asset
µi = expected return on ith asset
n = number of assets in portfolio
Then:
µ =
n

i=1
αiµi.
(9.1)
Therefore, a portfolio composed 50 percent of an asset with a 10
percent expected return and 50 percent of an asset with a 20 percent
expected return would have an expected return of [(0.5)(10 percent)+
(0.5)(20 percent)] = 15 percent. It is important to note that risk does
not enter the computation of expected return; the example above
has µ = 15 percent regardless of the standard deviations of the two
securities. Because of the eﬀects of correlation upon risk, the standard
deviation of the portfolio is not as easily computed as the expected
value.
--- page 443 ---

420
Quantitative Financial Analytics
Let: Cij = rijσiσj Cij = rijσiσj be the covariance between the
returns of securities i and j, where rij is the correlation coeﬃcient
of returns between securities i and j, and σ = standard deviation of
portfolio returns.
Then:
σ =




n

i=1
n

j=1
αiαjCij,
(9.2)
or
σ =




n

i=1
n

j=1
αiαjσiσjrij.
(9.3)
Note that the correlation coeﬃcient, r, plays a major role
in Equations (9.2) and (9.3). Brieﬂy, rij =
E[(I−µj)(J−µj)]
σiσj
and,
therefore, Cij may be restated as E[(I−µi)(J−µj)] or [E(IJ)−µiµj].
It should be noted that if i = j, then rij = 1 and Cij is the
variance (σ2
i=j).
Let us now consider the simple two-security case. The expected
return will be (for n = 2):
µ = α1µ1 + α2µ2,
(9.4)
and the standard deviation will be:
σ =

α2
1σ2
1 + 2α1α2σ1σ2r12 + α2
2σ2
2.
(9.5)
Beginning with the assumption that both securities are risky, let us
examine the importance of r12 in determining the risk of the portfolio.
Assume the following data:
Security
µi
σi
1
10 percent
3 percent
2
20 percent
7 percent
--- page 444 ---

Risk, Uncertainty, Utility and Portfolio Theory
421
.20
.10
0
µ
A
#1
#2
C
B
.03
.07
Figure 9.9. The Two-asset Portfolio (Risky Securities)
Case A: r12 = +1.00. In this instance, Equation (9.5) becomes:
σ =

(α2
1σ2
1) + 2(α1σ1)(α2σ2) + (α2
2σ2
2)
which is of the general algebraic form (a + b)2 = a2 + 2ab + b2. Thus,
σ = (α1σ1) + (α2σ2), and risk, like return, increases linearly in (σ, µ)
space. Such a case is graphed as A in Figure 9.9 and illustrates that
risk cannot be reduced without accepting a lower return (no gains
from diversiﬁcation) in the case of perfect positive correlation.
Case B: r12 = −1.00. In this instance, Equation (9.5) becomes:
σ =

α2
1σ2
1

−2(α1σ1)(α2σ2) +

α2
2σ2
2

which is of the general algebraic form (a −b)2 = a2 −2ab + b2. Thus,
σ = |(α1σ1) −(α2σ2)|, and σ = 0 where α1 = σ2/(σ1 + σ2).
Combinations of two securities under this assumption are
graphed as B in Figure 9.9. Here, the gains from diversifying a
portfolio composed entirely of security 1 at least to the riskless point
are obvious.
Case C: r12 = 0. In this instance, the equation becomes:
σ =

α2
1σ2
1

+

α2
2σ2
2

.
(Note that, assuming normal returns, r12 = 0 is the same thing
as statistical independence of returns, that is, [(P(I|J) = P(I)].)
--- page 445 ---

422
Quantitative Financial Analytics
This combination is graphed as C in Figure 9.9 and exhibits gains
from diversiﬁcation. For the speciﬁc data given above, the curve
reaches a minimum σ at µ = 11.55 percent. In general, the minimum
σ point in the two-asset case is given by dσ/da1 = 0, with α′ =
(σ2 −σ1σ2r12)/(σ2
1 + σ2
2 −2σ1σ2r12). Furthermore, as the number of
assets with statistically independent returns grows larger, and the
proportion invested in each becomes increasingly smaller, the law of
large numbers (or more precisely, the central limit theorem) implies
that risk can be essentially eliminated in the limit, leaving us in the
simple case of dominance discussed earlier.
If we may assume the investor to be rational and risk-averse,
then certain combinations of securities 1 and 2 may be immediately
eliminated. In case B of Figure 9.9 (where r12 = −1), for example, it
will be noted that for every portfolio from the all 1 portfolio to the
σ = 0 portfolio, which has the same σ and a larger µ. Thus, regardless
of the speciﬁc shape of one’s utility function, one would be foolish to
invest in any of the former set of portfolios with the latter available.
This notion leads directly to the concept of eﬃciency. A portfolio is
“eﬃcient” when it is impossible to obtain a greater average return
without incurring greater standard deviation and it is impossible to
obtain smaller standard deviation without giving up return on the
average. Therefore, all the portfolios below minimum σ on curves
B and C of Figure 9.9 are ineﬃcient. All the points on curve A
are eﬃcient. The points representing the coordinates of all eﬃcient
portfolios form a curve called the eﬃciency frontier. The eﬃciency
frontier for C from Figure 9.9 has been graphed as EF in Figure 9.10.
Although it cannot be known at this stage which portfolio is optimal
for a given investor, it is known from the above logic that for a
rational, risk-averse investor, the optimal portfolio will be on the
eﬃciency frontier.
The selection of an optimal portfolio follows in a straightforward
fashion, however. Indiﬀerence curves (derived above) are applied, and
the optimal portfolio is found at the point of tangency of EF with
the highest attainable indiﬀerence curve (point X in Figure 9.10).
This point is preferable to any other on the curve (for example, E
or F) because it provides a higher level of utility (that is, U2 >U1).
--- page 446 ---

Risk, Uncertainty, Utility and Portfolio Theory
423
µ
U1
U2
U3
.200
.116
0.028
0.070
E
X
F
Figure 9.10. Portfolio Selection
1
µ
µ1
µ2
U1
U2
U3
X
0
#1
#2
Figure 9.11. The Two-asset Portfolio (Including a Riskless Security)
A point on a higher indiﬀerence curve (for example, on U3) would
be even better, but by the deﬁnition of an eﬃciency frontier given
above, points above EF do not exist.
We may consider the special case in which one of the securities
(assume security 2) is riskless. Then σ2 ≡0 and Equation (9.5)
becomes σ = α1σ1, such that the risk of the portfolio is proportional
to the investment in the risky asset. Thus, any combination of
securities 1 and 2 could be drawn as a straight line in (σ, µ) space, as
shown in Figure 9.11. Furthermore, if 1 were a portfolio of securities
with parameters (σ1, µ1), the same result would be obtained if a
riskless security with return µ2 were added to the portfolio. The
--- page 447 ---

424
Quantitative Financial Analytics
optimal combination of the risky security or portfolio and the riskless
asset may also be determined by the application of indiﬀerence
curves (point X). We shall return later to the implications of this
phenomenon.
When we move from the two-security case to the many (or, n)
security case, the theoretical problems are not very great. We could
merely say that the investor (1) takes all the opportunities available
to him; (2) combines them in various proportions to form several (or
several million) hypothetical portfolios; (3) computes the µ and σ for
each of these portfolios; (4) for each level of µ, selects the portfolio
with the least σ; (5) generates the eﬃciency frontier that is ready
for application of his indiﬀerence curves; and (6) selects the optimal
portfolio. This, conceptually speaking, is all there is to the n-security
portfolio analysis case.
From a practical standpoint, however, the problems are enormous. Aside from computing the µ and σ for each security to be
analyzed, we would also estimate the covariance for each security
with every other security (a matter of (n2 −n)/2 covariances, or
499,500 in the n = 1000 security case). Furthermore, to follow the
above-suggested method, we would then compute the parameters
of a very large number of portfolios; if we limited our position
in a security to even multiples of 1 percent of our portfolio, in
the 1000-security case there are (1000,000!)/[(99,900!)(100!)] possible
portfolios to analyze. Even with the aid of modern computers, such
a task is impossible.
A ﬁrst step in the simpliﬁcation of the task is to reduce the
number of portfolios to be analyzed. Because we are only interested
in the portfolios that form the eﬃciency frontier, it is only the
parameters of these portfolios that should be computed. Such a
problem may be approached by reference to Figure 9.12. Here dots
represent security parameters and the boxes represent portfolio
parameters. The objective is to minimize a function of the type
σ2 −θµ.
By initializing the procedure at θ = ∞, the highest return
security (F) is obtained; note that, because diversiﬁcation cannot
increase return, the highest return portfolio will be composed entirely
--- page 448 ---

Risk, Uncertainty, Utility and Portfolio Theory
425
2
µ
E
F
=0
=
Figure 9.12. Eﬃciency Frontier Generation
of the highest return security. From this point, one may employ
a quadratic programming algorithm to trace the eﬃciency frontier
by allowing θ to decrease to 0 (at which point E, the minimumvariance portfolio, is obtained). In actuality, the iterative procedures
only determine “corner” portfolios, which are those points at which
a security enters or leaves the eﬃcient portfolio; the eﬃciency
frontier between two corner portfolios is a linear combination of the
corner portfolios. Aside from the objective function, these techniques
also generally involve constraints, such as the requirement that the
weights assigned to securities be non-negative and/or sum to one.
It is also possible to generate an eﬃciency frontier employing calculus. The following formulation provides the minimum-risk portfolio
subject to an expected return µ* and full investment (Σα = 1).
Minimize Z, where
Z =
n

i=1
n

j=1
αiαjCij + λ1

 n

i=1
αiµi −µ∗

+ λ2

 n

i=1
αi −1

,
(9.6)
and minimum Z is found where ∂Z/∂αi = 0, ∂Z/∂λk = 0 for all i
and k, and second order conditions are met. The λ’s are Lagrangian
multipliers and are conceptually equivalent to a dual in programming
or a shadow price (or opportunity cost) in more common parlance.
A calculus maximization may also be employed.
--- page 449 ---

426
Quantitative Financial Analytics
Maximize Z where
Z = φ
n

i=1
(αiµi) −


n

i=1
n

j=1
αiαjCij

+ λ

1 −
n

i=1
αi

.
(9.7)
And again, maximum Z is found where ∂Z/∂αi = ∂Z/∂λ = 0 and
φ is an indicator of return-risk preference.
To illustrate the hand solution for one point on the eﬃciency
frontier (and also the need for access to a computer if one plans to
do much work in this area), suppose that the eﬃcient portfolio at
µ∗= 15 percent were desired for the two-asset case below.
Security
µi
σi
A
10 percent
3 percent
B
20 percent
7 percent
rAB = 0
Although there are certainly easier solutions, employing Equation
(9.6), we obtain:
Z = α2
Aσ2
A + α2
Bσ2
B + λ1(0.1αA + 0.2αB −0.15) + λ2(αA + αB −1)
= α2
Aσ2
A + α2
Bσ2
B + 0.1αAλ1 + 0.2αBλ1 −0.15λ1 + αAλ2
+ αBλ2 −λ2.
Taking partial derivatives and setting them equal to zero, we obtain:
(1)
∂Z
∂αA
= 2αAσ2
A + 0.1λ1 + λ2 = 0.
(2)
∂Z
∂αB
= 2αBσ2
B + 0.2λ1 + λ2 = 0.
(3) ∂Z
∂λ1
= 0.1αA + 0.2αB −0.15 = 0.
(4) ∂Z
∂λ2
= αA + αB −1 = 0.
--- page 450 ---

Risk, Uncertainty, Utility and Portfolio Theory
427
Finally, we substitute algebraically for a solution (if the problem were
any larger, matrix algebra at least would be necessary).
(4) αA + αB −1 = 0
αA = 1 −αB.
(3) 0.1(1 −αB) + 0.2αB −0.15 = 0
0.1 −0.1αB + 0.2αB −0.15 = 0
0.1αB = 0.05
αB = 0.5
∴αA = 0.5.
(2) 2(0.5)(0.07)2 + 0.2λ1 + λ2 = 0
0.0049 + 0.2λ1 + λ2 = 0
λ2 = −0.0049 −0.2λ1.
(1) 2(0.5)(0.03)2 + 0.1λ1 + (−0.0049 −0.2λ1) = 0
0.0009 + 0.1λ1 −0.0049 −0.2λ1 = 0
−0.1λ1 −0.004 = 0
λ1 = −0.04
∴λ2 = −0.0049 −0.2(−0.04) = 0.0031.
Therefore, the weights are 50 percent security A and 50 percent
security B. The two Lagrangian multipliers are interpreted as ∂
(optimal Z satisfying other constraints)/∂(given constraint), the
denominators being 0.15 for λ1 and 1 for λ2.
In general, the quadratic programming method can deal with
inequalities as constraints but cannot handle negative variables, such
as leverage or short sales; the opposite is true in both cases for
the calculus methods. The use of artiﬁcial variables or additional
Lagrangian constraints can eliminate these limitations, however. The
input data (µi, σi, Cij) are the same in all cases, and computer
programs are available to solve problems by many of these methods.
A hand solution to any but the simplest problem is very tedious and
involves mathematics well beyond the scope of this book.
--- page 451 ---

428
Quantitative Financial Analytics
Not only do the methods discussed thus far require that a
covariance matrix (for each security with every other security) be
estimated, but also the computational procedures generally require
that this matrix be inverted for each portfolio to be analyzed. The
inversion of large matrices (our n = 1,000 case would provide a
1,000 × 1,000 covariance matrix), even with the aid of a computer,
is extremely time consuming. To deal with both the problems of
estimation and inversion, Professor Sharpe devised a simpliﬁed model
of portfolio analysis that seems to provide reasonably accurate
results.
Sharpe (1963), in his seminal paper, introduced the Sharpe
Diagonal Model which assumes that the return on a security may be
related to an index (such as the Dow-Jones, S&P 500, gross domestic
product (GDP), or whatever) as follows:
Returni = ai + biReturnI + ci
(9.8)
µi = ai + biµI + ci,
(9.9)
where:
ai and bi are constants
µI is the return (including dividends) on the index
ci is an error term with µci = 0 and σci = a constant.
It is further assumed that ci is not correlated with µI, with
itself over time, nor with any other security’s c (the last implying
that securities are only correlated through their common relationship
to the index). Therefore, µi can be estimated as (ai + biµI). The
parameters ai and bi can either be estimated, computed by regression
analysis, or both. Furthermore, σcican be viewed as the variation in
µi not caused by its relationship to the index, while σi −σci is that
portion of the total variation in µi caused by variation in µI.
The return on the portfolio becomes:
µ =
n

i=1
αi(ai + biµI + ci)
µ =
n

i=1
αi(ai + ci) +

 n

i=1
αibi

µI,
(9.10)
--- page 452 ---

Risk, Uncertainty, Utility and Portfolio Theory
429
where the ﬁrst term is viewed as an investment in the essential nature
of the securities, and the second term is an investment in the index.
The risk of the portfolio is:
σ =




n

i=1
(αiσci)2 +

 n

i=1
αibi
2
σ2
I,
(9.11)
where, again, the ﬁrst term may be viewed as the risk of the
portfolio attributable to the particular characteristics of the individual securities, and the second term as the risk attributable to the
index.
Thus, the Sharpe model greatly simpliﬁes the input problem by
making it directly amenable to regression analysis. In addition, by
assuming that securities are only related through the index, the nonzero elements in the covariance matrix are reduced to those on the
diagonal, thus easing the computational burden.
To illustrate the Sharpe approach, assume that the index currently stands at 1000 and, with reinvestment of dividends, it is
expected to be at 1100 at the end of the year. Given the following
data, suppose we wished to determine portfolio µ and σ for α1 = 0.2,
α2 = 0.5, and α3 = 0.3.
σI = 0.10
µ1 = 0.06 + 0.1µI,
σc1 = 0.03
µ2 = 0.03 + 2µI,
σc2 = 0.20
µ3 = 0.00 + µI,
σc3 = 0.10.
Employing Equation (9.10) we obtain:
µ = (0.2)(0.06) + (0.5)(−0.03) + (0.3)(0.00)
+ [(0.2)(0.1) + (0.5)(0.3)(1)](0.10)
µ = 0.012 −0.015 + (1.32)(0.10) = 12.9 percent.
--- page 453 ---

430
Quantitative Financial Analytics
Employing Equation (9.11):
σ =



[(0.2)(0.03)]2 + [(0.5)(0.2)]2 + [(0.3)(0.1)]2
+ [(0.2)(0.1) + (0.5)(2) + (0.3)(1)]2(0.1)2
σ =

(0.006)2 + (0.1)2 + (0.03)2 + (1.32)2(0.1)2
σ =
√
0.000036 + 0.01 + 0.0009 + 0.017424
=
√
0.02836 = 16.8 percent.
The three-security case of portfolio analysis has historically been
analyzed graphically and, because it provides some useful insights,
we shall consider it brieﬂy.
1. We initially set a conservation condition that the entire portfolio
will be invested (α1 + α2 + α3 = 1). The amount invested in the
third security (α3), therefore, is the amount not invested in the
other two (α3 = 1 −α1 −α2), and it is possible to conduct the
analysis in two-dimensional space.
2. We then set α1 on the abscissa and α2 on the ordinate, as shown
in Figure 9.13. Point A represents the all 1 portfolio (α1 = 1,
α2 = α3 = 0), point B the all 2 portfolio (α2 = 1, α1 = α3 = 0),
and point C the all 3 portfolio (α1 = α2 = 0, α3 = 1). If we
further add non-negativity conditions (α1 ≥0; α2 ≥0; α3 ≥0),
then triangle ABC becomes the attainable set of portfolios.
α1
C
A
B
α2
Figure 9.13. Three Asset Portfolios
--- page 454 ---

Risk, Uncertainty, Utility and Portfolio Theory
431
3. The mean of any portfolio in this system is thus:
µ = α1µ1 + α2µ2 + α3µ3
µ = α1µ1 + α2µ2 + (1 −α1 −α2)µ3
µ = µ3 + α1(µ1 −µ3) + α2(µ2 −µ3).
Then, if µ2̸ = µ3
α2 = µ −µ3
µ2 −µ3
−µ1 −µ3
µ2 −µ3
α1,
(9.12)
in the familiar Y = a + bX form.
Equation (9.12) is signiﬁcant because it provides the combinations of α1 and α2 (and implicitly α3) that will return a given µ. It
is also signiﬁcant because it is the equation for a line with slope of
−(µ1 −µ3)/(µ2 −µ3) and intercept of (µ−µ3)/(µ2 −µ3); it will be
noted that as the given return, µ, changes, the intercept of the line
changes but the slope does not. From this observation derived the
concept of isomean lines, which are a series of parallel lines with
each point on a given line promising the same return, and return
increasing from one isomean line to the next in the direction of
the security having the greatest expected value. A system of such
lines has been drawn in Figure 9.14 under the assumption that
µ3 > µ2 > µ1.
4. The variance of the three-security portfolio is:
σ2 = α2
1σ2
1 + α2
2σ2
2 + α2
3σ3
3 + 2α1α2C12 + 2α1α3C13 + 2α2α3C23,
which upon substitution and expansion is:
σ2 = α2
1

σ2
1 −2C13 + σ2
3

+ α2
2

σ2
2 −2C23 + σ2
3

+ 2α1α2

C12 −C13 −C23 + σ2
3

+ 2α1

C13 −σ2
3

+ 2α2

C23 −σ2
3

+ σ2
3,
which is, in turn, the equation for an ellipse. Therefore, the points
representing all the portfolios having the same σ2 will form an
ellipse, a so-called isovariance curve. Other sets of portfolios all
having the same variance but larger than the ﬁrst set will form a
larger ellipse that has the same center.
--- page 455 ---

432
Quantitative Financial Analytics
α1
C
A
B
α2
Direction of increasing µ
I1
I4
I3
I2
Figure 9.14. Isomean Curves
α1
C
A
B
α2
1/0
1/3
1/2
1/1
Figure 9.15. Isovariance Curves
The isovariance curves are therefore said to be a series of
concentric ellipses. The center of these ellipses is, of course,
the minimum-variance portfolio. A series of isovariance curves is
shown in Figure 9.15.
5. A moment’s reﬂection should indicate that (a) the highest return
to be found on any isovariance curve is at its point of tangency
with the highest attainable isomean curve (the tangent on the
--- page 456 ---

Risk, Uncertainty, Utility and Portfolio Theory
433
α1
C
A
B
α2
α2
X
M
N
O
Z
I1
I
I
I3
I2
V3
V2
V1
V0
*
Figure 9.16. The Eﬃciency Frontier in (α1, α2) Space
other side of the isovariance curve will give the lowest attainable
return), and (b) the lowest attainable risk on any isomean curve
is at its point of tangency with an isovariance curve. The locus of
these points of tangency is called the critical line and shown as
ll in Figure 9.16. The critical line is a straight line that always
passes through the center of the isovariance ellipses (the minimumvariance portfolio) and is, by deﬁnition, the locus of optimal
portfolios. Not all these portfolios are attainable, however. The
set of eﬃcient portfolios, therefore, tends to follow the critical
line where possible and to select the minimum-variance portfolio
in the direction of increasing return otherwise.
6. The set of eﬃcient portfolios (or the eﬃciency frontier) can
be observed in Figure 9.16 to follow the critical line from X,
the minimum-variance portfolio, to Z, the boundary of the
attainable set, and then along the boundary to C. Because points
on the critical line beyond Z are not attainable, those on ZC give
the best available trade-oﬀof σ2 for µ.
7. Finally, it is possible to transfer the eﬃciency frontier from
(α1, α2) space of Figure 9.16 to (σ2, µ) space in Figure 9.17.
--- page 457 ---

434
Quantitative Financial Analytics
2
µ
U1
U2
U3
M
C
Z
O
N
X
Figure 9.17. The Eﬃciency Frontier in (σ2, µ) Space
8. The ﬁnal step in portfolio selection is then to place the investor’s
indiﬀerence curves on the same axes and select that portfolio
represented by the point on the eﬃciency frontier that is tangent
to the highest indiﬀerence curve. In the case illustrated, this would
be point O which is tangent to U2. Referring to Figure 9.17, it
can be seen that portfolio O is composed of α∗
1 of 1, α∗
2 of 2, and
1 −α∗
1 −α∗
2 of 3.
Example
The eﬃciency frontier for the following diagram may be traced:
α1
C
X
A
B
α2
µ
I
I
