# The Kelly capital growth investment criterion _ theory and -- Leonard C_ Maclean, Edward O_ Thorp, W_ T_ Ziemba, Leonard -- World Scientific Handbook -- isbn13 9781283148344 -- bec576e26410d0c695fd5b867d08ec4f -- An.pdf — pages 419–438

--- page 419 ---

390
M Davis and S. Lleo
2.3.4
The general case
In the general case, the value function iP for the auxiliary criterion function
I(v,x;h;t,T), defined as
iP(t, x) = sup I(v,x;h;t,T)
ACT)
(17)
satisfies the Hamilton-Jacobi-Bellman Partial Differential Equation (HJB PDE)
oiP
~ + sup L~iP(X(t)) = 0
(18)
vt
h EiR'"
where
L~iP( t, x) = (b + Ex - BA'L,' h( s))' DiP + ~tr (AA' D2iP)
-
~(DiP)' AA' DiP - g(x, h; B)
(19)
where DiP is the gradient vector defined as DiP := ( 881), ... , 881>., ... , 881»' and
Xl
X t
Xn
D2iP is the Hessian matrix defined as D2iP := [ 8~:!j] , i, j = 1, ... ,n. The value
function iP satisfies the terminal condition iP(T, x) = ln v.
Solving the optimization problem gives the optimal investment policy h * (t)
h*(t) = B ~ 1 ('L,'L,,)-l [a + AX(t) - B'L,A' DiP(t, X(t))]
(20)
Moreover, the solution of the PDE is of the form
iP(t, x) = x'Q(t)x + x'q(t) + k(t)
(21)
where Q(t) solves a n-dimensional matrix Riccati equation and q(t) solves a ndimensional linear ordinary differential equation depending on Q (see Kuroda and
Nagai (2002) for details).
3
Fractional Kelly Strategies in the Risk-Sensitive Asset
Management Model
3.1
A mutual fund theorem
Theorem 1 (Mutual Fund Theorem (Davis and Lleo, 2008a)). Any portfolio can be expressed as a linear combination of investments into two "mutual
funds" with respective risky asset allocations:
hK(t) = ('L,'L,,)-l (a + AX(t))
hC(t) = -('L,'L,')-1'L,A' (q(t) + Q(t)X(t))
(22)
and respective allocation to the money market account given by
h{!(t) = 1-1'('L,'L,,)-1 (a+AX(t))
h~(t) = 1 + l'('L,'L,,)-l'L,A' (q(t) + Q(t)X(t))
(23)
Moreover, if an investor has a risk sensitivity B, then the respective weights of each
mutual fund in the investor's portfolio equal e!l and e!l' respectively.
--- page 420 ---

Fractional Kelly Strategies for Benchmarked Asset Management
391
The main implication of this theorem is that the allocation between the two
funds is a sole function of the investor's risk sensitivity e. As e -+ 0, the investor's
wealth gets invested in the Kelly criterion portfolio (portfolio K). On the other
hand, as e -+ 00, the investor's wealth gets invested in the correction portfolio
C. The investment strategy of this portfolio can be interpreted as a large position
in the short-term rate and a set of positions trading on the comovement of assets
and valuation factors. In financial economics, portfolio C is referred to as the
'intertemporal hedging term'.
When we assume that there are no underlying valuation factors, the risky securities follow geometric Brownian motions with drift vector J.L and the money market
account becomes the risk-free asset (i.e., ao = rand Ao = 0). In this case, ~A' = 0
and we can then easily see that fund C is fully invested in the risk-free asset. As a
result, we recover Merton's Mutual Fund Theorem for m risky assets and a risk-free
asset (e.g., Theorem 15.1, p. 489 in Merton (1992)).
3.2
Fractional Kelly strategies in the risk-sensitive asset
management model
Fractional Kelly strategies arise naturally in the Merton investment model, since
Merton's Mutual Fund Theorems guarantees that the optimal investment strategy
can be split in an allocation to the risk-free asset and an allocation to a mutual fund
investing in the Kelly criterion portfolio. However, the optimality offractional Kelly
strategies is the exception rather than the rule: in the Merton model, fractional
Kelly strategies are optimal as a result of the assumption that asset prices are
lognormally distributed. In the factor-based risk-sensitive asset management model,
we cannot expect either that the 'classical' definition of fractional Kelly strategies
to yield optimal or near optimal asset allocations as soon as e -=f=. O.
To address this difficulty, Davis and Lleo (2008a) proposed a generalization of the
concept of fractional Kelly strategy based on the findings expressed in the Mutual
Fund Theorem 1. Rather than regarding the fractional Kelly strategy as a split
between the Kelly portfolio and the short-term rate, Davis and Lleo propose to
define it as a split between the Kelly portfolio and the portfolio C, as defined in
the Mutual Fund Theorem 1. In this case, the Kelly fraction, which represents the
proportion of wealth invested in the Kelly portfolio, is inversely proportional to the
investor's risk sensitivity and is equal to Ii!l'
This redefinition of fractional Kelly strategies has two important consequences:
• The fractional Kelly portfolios are always optimal portfolios;
• In the lognormal case (i.e. when n = 0), the generalized definition of fractional Kelly strategies reverts to the 'classical' definition. This can be verified from the fact that in the lognormal case, the Mutual Fund Theorem 1
simplifies into Merton's Mutual Fund Theorem for m risky assets and a
risk-free asset.
--- page 421 ---

392
M Davis and S. Lleo
4
Fractional Kelly Strategies, Risk-Sensitive Asset Management
and the Merton Model with Power Utility
4.1
Objective
In this section, we go further in our analysis by drawing a comparison between risksensitive asset management and the Merton model from the perspective of fractional
Kelly strategies.
For comparison purpose, we consider:
• a fractional Kelly strategy with fraction f;
• the Merton model maximizing utility of terminal wealth, with the utility
function chosen to be the homogeneous power utility or hyperbolic absolute
risk aversion (HARA) function; and
• the diffusion risk-sensitive asset management model without any underlying
valuation factors.
In order to perform a comparison between the risk-sensitive asset allocation
model and the original Merton model, we assume that the market is comprised of
m risky assets and that the investor's objective is to find an optimal m-dimensional
portfolio allocation vector h(t), where hi (t) represents the proportion of the portfolio
invested in risky security i. We also assume that there are no valuation factors and
hence n = O.
We will show that the treatment of fractional Kelly strategies is
comparable in both cases up to a sign difference in the risk-aversion/risk-sensitive
coefficient.
4.2
A brief review of the Merton model
In the Merton model, the objective of an investor is to maximize the utility of
terminal wealth represented by the criterion:
where
I(t, s, h; e) := E [U(V(t, s, h))]
(24)
• V(t, x, h) is the investor's wealth at time t in response to a securities market
with price vector s and an investment policy h;
• U is the homogeneous power utility or hyperbolic absolute risk aversion
(HARA) function, defined as
z'Y
U(z) =-
I
where I E (-00,0) U (0,1) is the risk-aversion coefficient.
(25)
The dynamics of the prices of the m risky assets follows a geometric Brownian
motion of the form
dSi(t)
m
Si(t) = Midt + {; O"ikdWk(t) ,
Si(O) = Si,
i = 1, ... , m
(26)
--- page 422 ---

Fractional Kelly Strategies for Benchmarked Asset Management
393
where W(t) is a m-dimensional Brownian motion. The price of the money market
asset satisfies
d50(t) _ d
50(t) - r t,
50(0) = So
In this setting, the optimal asset allocation is given by
h*(t) = _l_(I:I:/)-lP
1- '1
(27)
(28)
with P := fL - r l where 1 is the m-element unit vector and I: is the diffusion matrix,
defined as I: = [(Tij].
4.3
Observations and conclusions
From a fractional Kelly perspective, the two models are strikingly similar. Taking
the case of an investor allocating a fraction f of his/her wealth to the Kelly portfolio,
we see that
• in the Merton model, such strategy would be optimal for an investor with
a level of risk aversion 'I equal to
1
'1= 1 -
-f
(29)
• in the risk-sensitive model, such strategy would be optimal for an investor
with a level of risk-sensitivity 8 equal to
1
8 = f - 1
(30)
Looking solely at the Kelly component of the optimal investment policy, this
would imply that
(31)
This similarity is in not surprising. Indeed, when we restrict the risk-sensitive
approach to a 0 factor model, we get the same optimal asset allocation as in the
Merton model with homogeneous power utility, but for the fact that 'I has been
replaced by - 8, i.e.
(32)
This observation is confirmed by both the range of 8 and 'I and by the functional
form of the utility function associated with the risk-sensitive approach.
These findings are summarized in Table 1.
Key Points:
• The situation between the Merton model with homogeneous power utility
and the risk-sensitive asset management model is parallel, and we can use
the guideline correspondence 8 = -'I = 1/ f - 1 to link them with the
fractional Kelly approach;
--- page 423 ---

394
M Davis and S. Lleo
Table 1
Comparison of the Merton Model and of the Risk-Sensitive Asset Management Model from
a Kelly Perspective
Merton model with
Risk-Sensitive Asset Management
homogeneous power utility
Risk-sensitive parameter / Risk
eE(-I,O)U(O,oo)
"'( E (-00, 0) U (0,1)
aversion coefficient
Range of the risk-sensitive pa-
(0,00)
(-00, 0)
rameter/ risk aversion coefficient for risk-averse investors
Form of Utility Function
U(z) = z-8
z'Y
U(z)=-
"'(
Optimal asset allocation h*(t)
_
I _(~~')_l (P,(X(t)) + ~A' D1»
e + I
_
I _(~~')_l P,
1 -"'(
Value of the risk aversion
I/f - 1
I - I / f
coefficient/ risk-sensitive
parameter corresponding to a
Kelly fraction f
Range of Kelly fractions for
(0, 1)
(0, 1)
risk-averse investors
• The risk-sensitive approach is therefore consistent with the Merton model
with homogeneous power utility;
• In the case when there are no factors (i.e., n = 0) , the optimal asset allocation obtained in the risk-sensitive approach reverts to that associated with
the Merton model;
• In the general case (n > 0), the definition of fractional Kelly strategies in
the risk-sensitive asset management model can be extended as proposed
above while remaining consistent with the 'classical' definition of fractional
Kelly strategies as a split bewteen the Kelly portfolio and the risk-free asset.
5
Adding an Investment Benchmark: Risk Sensitive Benchmarked
Asset Management Model
So far, we have introduced risk sensitive asset management in the classical asset
only context of an investor attempting to maximize the terminal utility of his/ her
wealth. We will now examine the related benchmarked asset management problem
in which the investor selects an asset allocation to outperform a given investment
benchmark.
In the benchmarked case, Davis and Lleo (2008a) propose that the reward function F(t, x; h) be defined as the (log) excess return of the investor's portfolio over
--- page 424 ---

Fractional Kelly Strategies for Benchmarked Asset Management
the return of the benchmark, i.e.
F(
h) '= I V(t, x, h)
t,x,
.
n L(t,x,h)
where L is the level of the benchmark.
Furthermore, the dynamics of the benchmark is modelled by the SDE:
dL(t)
L(t) = (c + G' X(t))dt +~' dW(t),
L(O) = l
395
(33)
(34)
where G is a scalar constant, G is a n-element column vector, and ~ is aN-element
column vector.
This formulation is wide enough to encompass a multitude of situations such as:
• the single benchmark case, where the benchmark is, e.g. an equity index
such as the S&P500 or the FTSE 100.
• the single benchmark plus alpha, where, for example, a hedge fund has for
benchmark a target based on a short-term interest rate plus alpha.
• the composite benchmark case, e.g., a benchmark constituted of 5% cash,
35% Citigroup World Government Bond Index, 25% S&P 500 and 35%
MSCI EAFE.
• the composite benchmark plus alpha that is a combination of the previous
two cases.
By Ito's lemma, the log of the excess return in response to a strategy h is
F(t, x; h) = In y + lot dIn V(s) - lot dlnL(s)
= lny+ lot (ao+A~X(s)+h( s)'(a+AX(s)))ds
lit
it
- -
h(s)'l:,l:,'h(s)ds +
h(s)'l:,dW(s)
2
0
0
it
lit
-
(c + G' X(s))ds + -
~'~ds
o
2
0
- lot~, dW(s)
v
F(O,x;h) = fo:= lny
(35)
Following an appropriate change of measure, the criterion function can be
expressed as
J(fo , x; h; t, T) = In fo - ~ In E~ [exp {e loT-t g(Xs, h(s); e)ds } 1
(36)
--- page 425 ---

396
M Davis and S. Lieo
where
1
'
g(x, h; B) = 2" (B + 1) h'2:,2:,'h - ao -
A~x - h'(a + Ax)
1
-
Bh'2:,~ + (c + e'x) + 2" (B -1) ~'~
(37)
Once again, the control problem simplifies into a LEQG problem.
The value function q, for the auxiliary criterion function I(fo , x; h; t, T). Then
q, is defined as
q,(t, x) = sup I(fo ,x;h;t,T)
(38)
A(T)
and it satisfies the HJB PDE
where
aq,
h
-a + sup L t q, = 0
t
hEIR=
L?q, = (b+ Bx - BA(2:,'h -
~))' Dq, + ~tr (AA'D2q,)
-~(Dq,)'AA'Dq, - g(x,h;B)
Solving the optimization problem gives the optimal investment policy h * (t)
h * = B ~ 1 (2:,2:,') -1 (a + Ax - B2:,A'Dq, + B2:,~ )
The solution of the PDE is still of the form
q,(t, x) = x'Q(t)x + x'q(t) + k(t)
(39)
(40)
( 41)
( 42)
where Q(t) solves a n-dimensional matrix Riccati equation and q(t) solves a ndimensional linear ordinary differential equation.
6
What About the Kelly Criterion?
6.1
A mutual fund theorem
In the benchmarked case, we will follow the same logic as in the asset only and
rewrite the optimal asset allocation as an allocation between two funds. We will
then use this result to define benchmarked optimal fractional Kelly strategies, that is
fractional Kelly strategies, which are also optimal investment policies in the benchmarked asset management model. All we will need to do after that is to verify that
this new definition is consistent with the definition we gave earlier in the asset only
case, and thus, with the 'classical' definition of fractional Kelly strategies in the
limit as our model converges to the Merton model.
The following benchmarked mutual fund theorem is due to Davis and LIeo
(2008a):
--- page 426 ---

Fractional Kelly Strategies for Benchmarked Asset Management
397
Theorem 2 (Benchmarked Mutual Fund Theorem). Given a time t and a
state vector X (t), any portfolio can be expressed as a linear combination of investments into two "mutual funds" with respective risky asset allocations
hK (t) = (~~/)-l (a + AX(t»)
hC(t) = (~~/)-l [~c; -
~A' (q(t) + Q(t)X(t»]
( 43)
and respective allocation to the money market account given by
hff (t) = 1 -
l/(~~/) -l (a + AX(t»)
h~(t) = 1- l/(~~/) -l [~c; -
~A' (q(t) + Q(t)X(t»]
(44)
Moreover, if an investor has a risk sensitivity e, then the respective weights of each
mutual fund in the investor's portfolio equal e!l and e!l' respectively.
There are two main differences between Theorems 1 and 2: the definition of
portfolio C and the role played by the risk sensitivity e. In the asset only case of
Theorem 1, portfolio C is comprised of the money market asset and of a strategy
trading the comovement of assets and valuation factors. In the benchmark case
of Theorem 2, portfolio C still includes an allocation to the money market asset
and the asset-factor co-movement strategy, but it also contains an allocation to a
strategy designed to replicate the risk profile of the benchmark. Indeed, the term
U := (~~/)-l~c; represents an unbiased estimator of a linear relationship between
asset risks and benchmark risk c; = ~/u. In financial economics, the interpretation
of u is as the vector of asset systematic exposure, or "betas", computed with respect
to the benchmark.
Hence, when e is low, the investor will take more active risk by investing larger
amounts into the log-utility or Kelly portfolio. On the other hand, when e is high,
the investor will divert most of his/her wealth to the correction fund, which is
dominated by the term (~~/)-l~c; and designed to track the index. In short, while
an investor with e = 0 is a Kelly criterion investor, an investor with extremely high
e is a passive investor.
This first observation leads us to reconsider the role and definition of the risk
sensitive parameter e. Indeed, while in the asset only case, e represents the sensitivity of an investor to total risk, in the benchmark case, e corresponds to the
investor's sensitivity to active risk. To some extent, in the benchmark case the
investor already takes the benchmark risk as granted. The main unknown is therefore how much additional risk the investor is willing to take in order to outperform
the benchmark. This amount of risk is directly quantified by the risk sensitive
parameter e.
6.2
Fractional Kelly strategies revisited
In the benchmark case, as in the asset only case, we can expand the classical definition of fractional Kelly strategies by defining them as a split between the Kelly
--- page 427 ---

398
M Davis and S. Lleo
portfolio K and the benchmark-tracking portfolio C , as per the Mutual Fund Theorem 2 and which is includes a benchmark replicating strategy.
We can quickly check that the extended definition in the benchmarked case is
consistent with the definition given earlier in the asset only case by setting the
benchmark to 0, which de facto implies the absence of a benchmark. We see then
that the definitions of fund C given in Theorems 2 and 1 are identical: the two
theorems now coincide. As expected, the asset only problem can be viewed as a
special case of the benchmarked allocation.
Thus, if we set n = ° so that no valuation factor is considered and set the
benchmark to 0, the risk-sensitive benchmarked asset management model is the
Merton model and the definition of optimal benchmarked fractional Kelly strategies
reverts to the classical definition of fractional Kelly strategies.
7
Case Studies
We will now apply the model to study some specific benchmark structures and
assess the appropriateness of benchmarks for Kelly criterion investors.
7.1
Benchmark as a portfolio of traded assets
First , we revisit two examples considered by Davis and Lleo (2008a) in which the
benchmark is a portfolio of traded assets respectively with or without the money
market asset.
7.1.1
Benchmark as a portfolio of traded assets and the money market asset
Developing the ideas from the previous paragraph, we consider a benchmark whose
dynamics is given by
dLt
A
-
= (ao + A~X(t)) + v'(t)(& + AX(t))dt + v'(t)~dWt
Lt
= [( 1 - v'l) ao + v' a + (( 1 - v'l) A~ + v' A ) X ( t ) 1 dt
+ v'(t)~dWt
where v is an m-element allocation vector satisfying the budget equation
l'v = 1 -
h~
(45)
(46)
and hf; is the allocation left in the money market account. The process L(t) represents the (log) return of a constant proportion portfolio with risky allocation vector
v and the remainder (i.e., 1 - l'v) invested in the money market account.
Corollary 3. (Fund Separation Theorem with a Constant Proportion Benchmark
(II)). Given a time t and a state vector X(t) , any portfolio can be expressed as
--- page 428 ---

Fractional Kelly Strategies for Benchmarked Asset Management
399
a linear combination of investments into a "mutual fund", an index fund and a
"long-short hedge fund" with respective risky asset allocations
hK(t) = (~~')-1 (a+AX(t))
hI(t) = v
hH (t) = _(~~')-l~A' (q(t) + Q(t)X(t))
and respective allocation to the money market account given by
h{f(t) = 1-1'(~~')-1 (a + AX(t))
h6(t) = 1 - l'v
hf! (t) = 0
( 47)
( 48)
Moreover, if an investor has a risk sensitivity 8, then the respective weights of each
fund in the investor's portfolio equal 11!1' 11!1 and 11!1' respectively.
We can interpret this Corollary in terms of optimal fractional Kelly strategies
in a similar way as we did for Corollary 4. The second component of the strategy,
the correction fund C, can again be split into:
1. a portfolio J with risky asset allocation given by v which is designed to strictly
replicate the risk exposure of the index;
2. a "long-short hedge fund" H with risky asset allocation given by h H (t) and whose
sole purpose is to trade the comovement of assets and factors.
Here again, we could show that H is a zero net weight strategy, i.e.
( 49)
7.1.2
Benchmark as a portfolio of traded assets only
We assume that the benchmark follows a constant proportion strategy invested
in a combination of traded assets. Its dynamics is given by the equation
dL
_t = v'(a + AX(t))dt + v'~dWt
L t
where v is a m-element allocation vector satisfying the budget equation
l'v = 1
In this setting, Corollary 3 can be expressed as:
(50)
(51)
Corollary 4. (Fund Separation Theorem with a Constant Proportion Benchmark
(J)). Given a time t and a state vector X(t), any portfolio can be expressed as
--- page 429 ---

400
M Davis and S. Lleo
a linear combination of investments into a "mutual fund", an index fund and a
"long-short hedge fund" with respective risky asset allocations
hK (t) = (~~I)-l (a + AX(t))
hI(t)=v
hH(t) = _(~~I)- l~A' (q(t) + Q(t)X(t))
and respective allocation to the money market account given by
hfJ (t) = 1 -
11(~~') -l (a + AX(t))
h6(t) = 0
h{f (t) = 11(~~') -l~A' (q(t) + Q(t)X(t))
(52)
(53)
Moreover, if an investor has a risk sensitivity (), then the respective weights of each
mutual fund in the investor's portfolio equal e!l' e!l and e!l' respectively.
From the perspective of optimal fractional Kelly strategies, the implication of
this corollary is that the second component of the strategy, the correction fund C,
can now be explicitly split into two sub portfolios:
1. a portfolio I with asset allocation given by v which is designed to strictly replicate
the risk exposure of the index. Observe that the linear estimator u := (~~I) - l~<;
has vanished and been replaced by the actual asset allocation v: since the benchmark is now comprised of traded assets it can be replicated by a direct investment
in the appropriate asset allocation and does not require any further estimation;
2. a "long-short hedge fund" H with risky asset allocation given by
_ (~~I) - l~A' (q(t) + Q(t)X(t))
(54)
and whose sole purpose is to trade the comovement of assets and factors.
The "long-short hedge fund" H is particularly interesting because it has zero
net weight in the sense that the sum of all the long positions in the portfolio is
exactly matched by the sum of short positions. As a result, fund H satisfies the
budget equation
(55)
This "long-short hedge fund" can therefore be viewed as a macro-oriented overlay
strategy within the asset allocation.
7.2
Benchmark with alpha target
We now consider two new examples involving a benchmark based on an interest
rate plus some measure of risk-adjusted excess return known as alpha.
--- page 430 ---

Fractional Kelly Strategies for Benchmarked Asset Management
401
7.2.1
Money market rate plus alpha benchmark
Money market rate plus some predetermined alpha has been adopted as a benchmark by a large number of hedge funds. What are the implications of this choice
in terms of the optimal fractional Kelly strategies?
The dynamics of such a money market rate plus alpha benchmark can be expressed as
dLt
Lt = (ao + AoX(t))dt + adt
(56)
where a represents the instantaneous level of risk-adjusted excess return, or alpha,
required of the fund manager.
The optimal asset allocation in this case is
(57)
which is simply the asset only asset allocation as given in (20). As a result, the conclusion of the Mutual Fund Theorem 1 hold and optimal fractional Kelly strategies
can be defined accordingly.
So, what has happened to the benchmark? In our risk-sensitive framework, the
benchmark is tracked through its risk profile rather than its return profile. Since
a money market plus alpha benchmark does not have any direct risk, there cannot
be any comovement between the assets and the benchmark. Thus, the benchmark
risk profile cannot be replicated, and as a result, the asset allocation is established
without any regard to the benchmark.
The money market plus alpha benchmark will have an impact on the value
function q,.
Indeed, in the benchmarked case, the auxiliary criterion function
J(fo , Xi hi t, T) reflects excess return over the benchmark, rather than total return as
in the asset only case. The value function for the benchmarked problem is therefore
consistent with excess return rather than total return, resulting in different value
functions for the benchmark problem and for the asset only case.
The main conclusion from this case study is that from the perspective of a rational risk-sensitive investor with no investment constraints, money market plus alpha
benchmarks results in the same investment strategy as not having any benchmark
at all. To some extent, in a risk-sensitive setting, money market plus alpha is a
benchmark-free benchmark. In particular, and somehow counter intuitively, the
choice a higher value for alpha does not result in a the design of a riskier asset
allocation. In fact, the value of alpha has no impact at all!
7.2.2
Bill rate or bond yield plus alpha benchmark
The situation would however be slightly different if the benchmark was for example
3 month Treasury bill rate plus alpha or a 5 year Treasury note yield plus alpha.
To generalize slightly, the benchmark dynamics could be expressed as an extension
--- page 431 ---

402
M Davis and S. Lleo
of the model considered above in the "Benchmark as a Portfolio of Traded Assets
Only" case (in Section 7.1.2) 1:
dL
_
t = v'(a + AX(t))dt + adt + v'~dWt
L t
where v is a m-element allocation vector satisfying the budget equation
l'v = 1
(58)
(59)
As expected, the level of alpha does not influence the optimal asset allocation
and the conclusions stemming from Corollary 4 are still valid in this case.
7.2.3
Solving the alpha puzzle
Why is the alpha not producing any impact on the asset allocation? The reason is
that the risk-sensitive benchmarked asset management model does not penalize for
a non-achievement of the benchmark return. As we have seen above, risk sensitivity
implies that the risk of the asset portfolio relative to the benchmark matters, but
not the expected return. Since an alpha target is in essence a "pure return" target,
it does not change the behaviour of the risk sensitive investor.
Should the investor be penalized for a non-achievement of the benchmark return?
Not in our opinion. For an investor who decides of their own asset allocation,
the benchmark is a measure of acceptable risk rather than an minimum return
objective. Indeed, the portfolio optimization process will always select , for a given
risk sensitivity, the asset allocation which maximizes the relative return of the asset
portfolio with respect to its benchmark. The issue of an alpha target is irrelevant
in this problem.
The situation might however be different if the investor hires a manager to
perform the asset allocation. The alpha imperative may in this case be understood
as a control imposed by the investor to force the asset manager to select an optimal
(or near optimal) asset allocation. The investor should still not be penalized for
a non achievement of the benchmark, but it is conceivable that the investor may
want to penalize the manager for non achievement of the benchmark return. Here,
the penalization would occur at the level of the fee earned by the manager and not
at the level of the investor's terminal wealth. This would result in a completely
different control problem in which we would need to take the perspective of the
manager whose objective is to allocate the investor's assets in order to maximize
the management fee received and subject to a non-achievement penalty.
IThis slight generalization is required in the event the benchmark is based on a bond. Indeed ,
in the risk-sensitive model, zero coupon bonds are the representatives of the fixed income asset
class in the investment universe. Any coupon bond must therefore be "recreated" as a linear
combination of zero coupon bonds. In the event, the benchmark is a Treasury bill, then we have
the degenerate case in which v is a vector with the element corresponding to the Treasury bill set
to 1 and all other elements equal to 0
--- page 432 ---

Fractional Kelly Strategies for Benchmarked Asset Management
403
7.3
Alpha-omega targets
An alternative to the pure alpha target is an alpha-omega target, where omega
represents the variability of alpha (see Grinold and Kahn (1999) for a view of the
role of alpha and omega in active management). This approach implictly recognises
that alpha generation is not only uncertain but also risky. The introduction of the
omega terms changes only slightly the asset allocation problem. The dynamics of
a benchmark with alpha - omega targets can be modelled as
df(~~) = [(c + C' X(t))dt +~' dW(t)] + [adt + w'dW(t) ]
=(c+a+C'X(t))dt+(~+ w) 'dW(t) ,
L(O) = l
(60)
where the scalar constant c, the n-element column vector C, and ~ is aN-element
column vector are related to the benchmark itself and the scalar a and vector w
refer to the excess return demanded by the investor. The last element of ~ is set to
o while the first n + m element of the vector ware set to O. This condition ensures
that the variability of alpha is uncorrelated with the factors and assets, as active
asset management theory suggests.
7.3.1
The optimal investment policy
Extending the reasoning in Davis and Lleo (2008a), we would find that the optimal
investment policy h* is
h* = e! 1 (~~')-l (a + Ax - e~A' Dif> + e~(~ + w))
The solution of the PDE is still of the form
if>(t, x) = x'Q(t)x + x' q(t) + k(t)
(61)
(62)
where Q(t) solves a n-dimensional matrix Riccati equation and q(t) solves a ndimensional linear ordinary differential equation. Specifically,
Q(t) - Q(t)KoQ(t) + K~ Q(t) + Q(t)Kl + -e
1
A'(~~')-l A = 0
(63)
+1
for t E [0, T ], with terminal condition Q(T) = 0 and with
K
= B -
_e_A~'(~~')-l A
1
e + 1
q(t) + (K~ - Q(t)Ko) q(t) + Q(t)b + eQ'(t)A(~ + w) + Ao - C
+ e! 1 (2A' - eQ'(t)A~') (~~')-l (a + e~(~ + w))
= 0
(64)
(65)
(66)
--- page 433 ---

404
M Davis and S. Lleo
with terminal condition q(T) = O.
k(s) = fo + iT l(t)dt
(67)
for 0 <:::: s <:::: T and where
1
e
l(t) = 2tr (AA'Q(t)) - 2q'(t)AA'q(t) + b'q(t)
+ _1_0,1(2:2:/)-10, + -1-e2q'(t)A2:/(2:2:/)-12:A'q(t)
e+1
e+1
__
e_q'(t)A2:/(2:2:/)-1O, _
2e2 q'(t)A2:/(2:2:/)-12:')'
e+1
e+1
1
e
+ e(~ + W)I A'q(t) - - (e -
1)(~ + w)'(~ + w) + -e -O,I(2:2:/)-12:(~ + w)
2
+1
+ -e
1
e2')'/2:(2:2:/)-12:(~ + w) + ao - (c + a)
(68)
+1
7.3.2
Mutual fund theorem
We can now restate the optimal asset allocation in terms of the following Mutual
Fund Theorem:
Theorem 5 (Alpha-Omega Benchmarked Mutual Fund Theorem).
Given a time t and a state vector X(t), any portfolio can be expressed as a linear combination of investments into two "mutual funds" with respective risky asset
allocations
hK (t) = (2:2:/)-1 (a + AX(t))
hC(t) = (2:2:/)-1 [2:(<; + w) - 2:A' (q(t) + Q(t)X(t))]
and respective allocation to the money market account given by
h{! (t) = 1 - 1/(2:2:/)- 1 (a + AX(t))
h~(t) = 1- 1/(2:2:/)-1 [2:(<; + w) - 2:A' (q(t) + Q(t)X(t))]
(69)
(70)
Moreover, if an investor has a risk sensitivity e, then the respective weights of each
mutual fund in the investor's portfolio equal e!1 and e!1' respectively.
Proof.
This Corollary can be proved in a similar fashion to Theorem 3 in Davis
and Lleo (2008a).
0
7.3.3
Kelly strategies
In terms of Kelly strategies, this Mutual Fund Theorem represents a split between
a fraction e!1 invested in the Kelly portfolio K, and a fraction e!1 invested in
the correction fund C. As in Theorem 2, portfolio C includes an allocation to the
money market asset and the asset-factor co-movement strategy and an allocation
to a strategy designed to replicate the risk profile of the benchmark. In addition,
--- page 434 ---

Fractional Kelly Strategies for Benchmarked Asset Management
405
the allocation to portfolio C features a new term related to the variability of alpha,
defined as it := (~~/)-l~w and which represents an unbiased estimator of a linear
relationship between asset risks and alpha risk w = ~I u.
When e is high, the investor will divert most of the wealth to the correction fund
in order to replicate the risk profile of the benchmark and the appropriate level of
active risk given by w. On the other hand, when e is low, the investor will take
more active risk by investing larger amounts into the Kelly portfolio and will not
attempt to stay within the bounds of active risk imposed by w.
7.4
Benchmarks and Kelly investors: No benchmark for buffett!
Our last application of the idea of benchmarked fractional Kelly strategies takes
the form of an anecdote concerning the appropriateness of benchmarks for Kelly
investors. A few years ago, a controversy shook the North American investment
industry: what would be a proper investment benchmark to assess the performance
of legendary investor Warren Buffettt's Berkshire Hathaway? Although this question may appear, at first glance, trivial, it is in fact the reflection of a wider concern
shared by asset managers and investors alike on what constitutes an appropriate
investment benchmark. This question has received an increasing deal of attention
in the past two decades and it is considered so important in the investment management industry that the Research Foundation of the CFA Institute (then called
AIMR) , a leading professional association in the investment management industry, has recently devoted a monograph to the question (see Siegel (2003) for more
details) .
Although we do not intend on entering the benchmark design and specification
debate2 , the results we derived reveal a new dimension to the problem: the impact
of the investment benchmark on a fund manager's investment strategy depends
to a significant extent on the risk-aversion of the manager or investor. Indeed,
we have shown that in the risk-sensitive benchmarked asset management model,
the importance of the benchmark in the investment decision increases as the risk
aversion of the investor increases. In fact , the risk-sensitivity e is a direct indication
of the amount of active risk that an investor is willing to take. Thus, the exercise
consisting in setting an investment benchmark becomes increasingly irrelevant as
risk-aversion gets nearer to 0: Kelly criterion investors invest in the log-utility
portfolio and have no regards for a benchmark.
Before setting a benchmark, it is imperative to know the investor's risk preferences as this will influences his/her investment style. A very rough correspondence
would be to identify extremely high risk aversion investors to passive portfolio managers whose mandate is to track an index, low risk aversion investors to purely active
managers, whose mandate is to generate the best possible risk-adjusted return in
2We have, after all, conveniently assumed throughout that an appropriate care had been taken
beforehand to select the benchmark.
--- page 435 ---

406
M Davis and S. Lleo
a specific market, and medium risk-aversion investors to so called "core plus" or
"index plus" managers who track closely and index while trying to generate some
incremental extra return or "alpha". The only time these three broad categories of
investors will coincide is when their benchmark is the Kelly portfolio.
Going back to our original question, Warren Buffet focuses on long-term growth
maximization rather than the avoidance of short-term losses (see Ziemba (2005) for
a discussion of Berkshire Hathaway's risk-adjusted performance and Thorp (2006)
for a Kelly criterion perspective). In this sense, Mr. Buffet behaves similarly to a
Kelly criterion bettor. The RSBAM model then demonstrates that benchmarks are
irrelevant to Mr. Buffet's investment strategy.
As a concluding note, since at least 1995, the Berkshire Hathaway annual report
features a table presenting a proxy for the performance of the Berkshire Hathaway
share against the return of the S&P500 going back to 1965. Warren Buffet, however,
does not recognize the S&P500 as his benchmark. He made it clear that this
comparative table had been included in the annual reports at the request of investors
but that he personally sees little value in it.
8
Conclusion
Historically, Kelly and fractional Kelly strategies have played an important part
in asset-only investment management. But the essential role of fractional Kelly
strategies does not stop at this level: it also extends to benchmarks and even to
asset and libaility management (see Davis and Lleo (2008b)). In benchmarked
asset allocation problems, fractional Kelly strategies highlight the fundamental split
between a purely active growth maximizing strategy (the Kelly criterion portfolio)
and pure benchmark replication. Moreover, the Kelly fraction, which represent the
fraction of one's wealth invested in the Kelly portfolio, is a sole function of the
investor's degree of risk-sensitivity.
This has profound implications. A Kelly investor, with 0 risk-sensitivity, will
invest solely in the purely active portfolio and as a result, benchmarks are irrelevant
to Kelly investors. On the other end of the spectrum, investors with extremely
large risk-sensitivity will tend to opt for full replication of the benchmark: they
are passive investors. Somewhere in the middle, we find investors with an average
risk-sensitivity, who adopt core-plus strategies: a basic replication of the benchmark
with some departure in order to generate excess returns. The only time these three
broad categories of investors will coincide is when their benchmark is the Kelly
portfolio.
References
A. Bensoussan and J. H. van Schuppen (1985). Optimal control of partially observable
stochastic systems with an exponential-of-integral performance index. SIAM Journal
on Control and Optimization, 23(4), 599- 613.
--- page 436 ---

Fractional Kelly Strategies for Benchmarked Asset Management
407
Bielecki, T . R. and S. R. Pliska (1999) . Risk-sensitive dynamic asset management. Applied
Mathematics and Optimization, 39, 337- 360.
Davis, M. H. A. and S. Lleo (2008a) . Risk-sensitive benchmarked asset management. Quantitative Finance, 8(4), 415- 426.
Davis, M. H. A. and S. Lleo (2008b). A risk sensitive asset and liability management
model. Working Paper.
Grinold, R. and R. Kahn (1999) . Active Portfolio Management: A Quantative Approach
for Producing Superior Returns and Selecting Superior Money Managers. New York:
McGraw-Hill.
Jacobson, D. H. (1973). Optimal stochastic linear systems with exponential criteria and
their relation to deterministic differential games. IEEE Transactions on Automatic
Control, 18(2), 114- 13l.
Kuroda, K. and H. Nagai (2002) . Risk-sensitive portfolio optimization on infinite time
horizon. Stochastics and Stochastics Reports, 73, 309- 33l.
Lefebvre, M. and P. Montulet (1994) . Risk-sensitive optimal investment policy. International Journal of Systems Science, 22, 183- 192.
Merton, R. C. (1969). Lifetime portfolio selection under uncertainty: The continuous time
case. Review of Economics and Statitsics, 51, 247- 257.
Merton, R. C. (1971). Optimal consumption and portfolio rules in a continuous-time model.
Journal of Economic Theory, 3, 373- 4113.
Merton, R. C. (1992). Continuous-Time Finance. US: Blackwell Publishers.
Siegel, L. (2003). Benchmarks and Investment Management. The Research Foundation of
AIMR.
Thorp, E. (2006). The Kelly criterion in blackjack, sports betting and the stock market. In S. A. Zenios and W. T. Ziemba, editors, Handbook of Asset and Liability
Management, Volume 1, Chapter 9, pp. 385-428. Amersdam: North Holland.
P. Whittle (1990). Risk Sensitive Optimal Control. New York: John Wiley & Sons.
Ziemba, W. T. (2003). The Stochastic Programming Approach to Asset, Liability, and
Wealth Management. Research Foundation Publication. CFA Institute.
Ziemba, W. T. (2005). The symmetric downside-risk sharpe ratio. Journal of Portfolio
Management, 32(1), 108- 122.
--- page 437 ---

This page is intentionally left blank
--- page 438 ---

28
A Benchmark Approach to Investing and Pricing
Eckhard Platen
University of Technology Sydney,
School of Finance €3 Economics and Department of Mathematical Sciences,
PO Box 123, Broadway, NSW, 2007, Australia
Abstract
This paper introduces a general market modeling framework, the benchmark
approach, which assumes the existence of the numeraire portfolio. This is the
strictly positive portfolio that when used as benchmark makes all benchmarked
non-negative portfolios supermartingales, that is intuitively speaking downward
trending or trendless. It can be shown to equal the Kelly portfolio, which maximizes expected logarithmic utility. In several ways, the Kelly or numernire portfolio is the "best" performing portfolio and cannot be outperformed systematically
by any other non-negative portfolio. Its use in pricing as numeraire leads directly to the real world pricing formula, which employs the real world probability
when calculating conditional expectations. In a large regular financial market ,
the Kelly portfolio is shown to be approximated by well-diversified portfolios.
JEL Classification: G 10, G 13
1991 Mathematics Subject Classification: primary 90A12; secondary 60G30,
62P20.
Keywords and phrases: Kelly portfolio, real world pricing, numeraire portfolio,
strong arbitrage, diversification.
1
Introduction
409
The classical asset pricing theories, as developed in Debreu (1959), Sharpe (1964),
Lintner (1965), Merton (1973a,b), Ross (1976), Harrison and Kreps (1979), Constantinides (1992), and Cochrane (2001) represent forms of relative pricing, since
the existence of an equivalent risk neutral probability measure is typically requested.
However, relative pricing ignores in the long run the presence of the equity premium.
This paper presents an extension of classical risk neutral pricing in a general modeling framework, the benchmark approach, where a form of absolute pricing naturally
emerges, see Platen (2002) Platen (2002, 2006) and Platen and Heath (2006). The
benchmark represents here the "best" performing, strictly positive, tradable portfolio, which turns out to be the K elly portfolio, see Kelly (1956). Most results we
