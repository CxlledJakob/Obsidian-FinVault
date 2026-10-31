# The Kelly capital growth investment criterion _ theory and -- Leonard C_ Maclean, Edward O_ Thorp, W_ T_ Ziemba, Leonard -- World Scientific Handbook -- isbn13 9781283148344 -- bec576e26410d0c695fd5b867d08ec4f -- An.pdf — pages 362–381

--- page 362 ---

Growth versus Security in Dynamic Investment Analysis
333
1564
L. C. MACLEAN, W. T. ZIEMBA AND G. BLAZENKO
G3. 7/(Yo , p) = ET { Y(p );?U) .
This is the mean first passage time T to reach the set
[V, OC! ). That is, how long on average does it take the investor to reach a specific level
of wealth. For example, how long must the investor wait before he is a millionaire.
1.2. Measures of Security
Sl. "It(Yo, p) = Pr[Yt(p) ~ btl· This is the probability that the investor will have a
specific accumulated wealth bt E ~ at time I . That is, what are his chances of reaching
a given target in a fixed amount of time. For example, what chance does the investor
have of accumulating $200,000 one hundred days from now?
S2. a(yo, p) = Pr [YI(p) ~ bl , 1 = I, ... l. This is the probability that the investor's
wealth is above a specified path. Our concern for an investor is that his wealth will fall
back too much in any period. He may want protection against losing more than, say,
10% of current wealth at any point in time.
S3. i3(yo, p) = Pr[ T { Y(p );,oU) < T { y( p);,o Ld. This is the probability of reaching a goal
V which is higher than his initial wealth Yo, before falling to a wealth level L which is
less than Yo . For example, if V = 2yo and L = Yo/2, this is the probability of doubling
before halving.
The rationale for the measures selected is to profile the growth and security dimensions
of the accumulation process. In each case there is a natural pairing of the measures:
(ILl, "II) for accumulated wealth at a point in time; (c/J, a) for the behavior of growth
paths; and (7/, 13) for first passage to terminal or stopping states. The choice of profile
(pair of measures) is largely a function of personal preference and problem context. It
is expected that the information contained in each of the profiles would be useful in
selecting an investment strategy.
The usual criterion for evaluating a decision rule is tc/J/(YO , p) , the expected log of
accumulated wealth. When Ki/(w/) = ai(t)Ei(w/), i = I, ... , n, 1 = I, . .. , then the log
optimal strategy is proportional, Pil( wt- I ) = Pil. Furthermore, if Pi , i = I, . . . , n, solves
the one-period problem
Pi ~ 0,
i = I· .. n}
,
,
thenpil = inf {a i l (t)Pi , I} for i = I, . .. , n, 1 = I, . . .. In the case where ai(t) = ai,
i = I, . . . , n, the log optimal strategy is a fixed fraction (independent of time) , and is
referred to as the Kelly (1956) strategy.
Considering the other growth measures we find that the Kelly strategy (i) maximizes
the long run exponential growth rate c/J(Yo, p) , and (ii) minimizes the expected time to
reach large goals 7/(Yo , p) (Breiman 1961, Algoet and Cover 1988). The main properties
of the Kelly strategy are summarized in Table 1. The performance of the Kelly strategy
on the security measures is not so favorable. As with any fixed fraction rule, the Kelly
strategy never risks ruin, but in general it entails a considerable risk oflosing a substantial
portion of wealth.
In terms of security an optimal policy is often to keep virtually all wealth in the riskless
asset (Eithier 1987). We will let Po = (I , 0, . .. , 0) be the extreme security strategy,
where all assets are held in cash.
Our purpose is to monitor the growth and security measures as the investment decisions
vary with the goal of balancing the measures to obtain a strategy which performs well
on both the growth and security dimensions. For a particular (growth, security) combination, the complete set of values is given by the graph (see Figure 1)
Vi = {( Gi(p) , Si(P» I p is a feasible investment strategy } .
--- page 363 ---

334
Good/Bad
G
G
G
B
G
B
G
B
L. C. MacLean, W. T. Ziemba and G. Blazenko
GROWTH VERSUS SECURITY IN DYNAMIC INVESTMENT ANALYSIS
1565
TABLE I-PART I
Main Properties for the Kelly Criterion
Property
Maximizing E log X asymptotically
maximizes the rate of asset growth.
The expected time to reach a
preassigned goal is asymptotically as
X increases least with a strategy
maximizing E log XN .
Maximizing median log X.
False Property: If maximizing E log X N
almost certainly leads to a better
outcome then the expected utility of
its outcome exceeds that of any
other rule provided n is sufficiently
large.
Counterexample: u(x) = X, 1 < p < I,
Bernoulli trials,] = I maximizes
EU(x) butf* = 2p -
I < I
maximizes E log XN •
The E log X bettor never risks ruin.
If the E log X bettor wins then loses or
loses then wins he is behind. The
order of wi n and loss is immaterial
for one, two, . . . sets of trials.
The absolute amount het is monotone
in wealth.
The bets are extremely large when the
wager is favorable and the risk is
very low.
Reference
Breiman (1961), Algoet and Cover (1988)
Breiman (1961), Algoet and Cover (1988)
Ethier (1987)
Thorp (1975)
Hakansson and Miller (1975)
(I + ')')(1 - ')')Xo = (I - ')")Xo <0
(aE log X)/8Wo > 0
Roughly the optimal wager is proportional to the
edge divided by the odds. Hence for low risk
situations and corresponding low odds the
wager can be extremely large. For one such
example, see Ziemha and Hausch (1985, pp.
159-160). There in a $3 million race the
optimal fractional wager on a 3-5 shot
was 64%.
The most obvious points in V; to identify are efficient points given by (G;(p,,), S;(p,,»
E V; with
G;(p,,) = max { G;(p) I S;(p) ~ lX, P feasible}.
Alternatively the efficient points are ( G;(pf3), S;(pf3» with
S;(PIi) = max {S;(p) I G;(p) ~ fl, p feasible} .
Given the required level of security (or growth) the efficient points are undominated.
The set of efficient points constitutes the efficient frontier.
Two key efficient points are the unconstrained optimal growth and optimal security
points, respectively (G;(p), S;(p» with G;(p) = max {G;(p) I p feasible} and (G,(po),
S;(Po» with S;(Po) = max {S;(p) I p feasible}. The optimal growth strategy is the Kelly
strategy p and the optimal security strategy is the cash strategy Po. These are both fixed
fraction strategies. Other strategies yielding points on the efficient frontier would not
typically be fixed fraction, but rather would be dynamic strategies, depending on current
wealth and/ or time. Gottlieb ( 1985) has derived such a strategy for the criteria of maximizing mean first passage time to a goal (G3 ), subject to a high probability of reaching
the goal (S3)'
--- page 364 ---

Growth versus Security in Dynamic Investment Analysis
335
1566
Good/Bad
B
B
B
G
G
G
G
L. C. MACLEAN, W. T. ZIEMBA AND G. BLAZENKO
TABLE I-PART 2
Main Properliesjor the Kelly Criterion
Property
One overbets when the problem data
is uncertain.
The total amount wagered swamps
the winningsthat is, there is
much "churning."
The unweighted average rate of
return converges to half the
arithmetic rate of return.
The E log X bettor is never behind
any other bettor on average in I,
2, ... trials.
The E log X bettor has an optimal
myopic policy. He does not have
to consider prior to subsequent
investment opportunities.
The chance that an E log X wagerer
will be ahead of any other wagerer
after the first play is at least 50%.
Simulation studies show that the E
log X bettor's fortune pulls way
ahead of other strategies' wealth
for reasonably-sized sequences of
investments.
Reference
Betting more than the optimal Kelly wager is
dominated in a growth-security sense. Hence if
the problem data provides probabilities, edges
and odds that may be in error, then the
suggested wager will be too large. This property
is discussed in and largely motivates this paper.
Ethier and Tavare (1983) and Griffin (1985) show
that the Expected Gain/ E Bet is arbitrarily small
and converges to zero in a Bernoulli game where
one wins the expected fraction p of games.
Related to property 5 this indicates that you do not
seem to win as much as you expect; see Ethier
and Tavare (1983) and Griffin (1985).
Finkelstein and Whitley (1981)
This is a crucially important result for practical use.
Hakansson (1971 b) proved that the myopic
policy obtains for dependent investments with
the log utility function. For independent
investments and power utility a myopic policy is
optimal.
Bell and Cover (1980)
Ziemba and Hausch (1985)
Rather than trying to move from optimal growth to optimal security along the efficient
frontier, we will consider the path generated by convex combinations of the optimal
growth and optimal security strategies, namely
p(A) = Aft + (l -
A)PO ,
Clearly p( A) is a fixed fraction strategy and we will call it fractional Kelly since it
blends part of the Kelly with the cash strategy. The fractional Kelly strategy is n-dimensional, specifying investments in all opportunities, and the key parameter is A, which we
can consider as a tradeoffindex.
The path traced by the fractional Kelly strategies is
u9 = {(G;(p(A)), S;(p(A)))IO ~ A ~ I}.
The fractional Kelly path is illustrated in Figure I. This path has attractive properties.
First, it is easily computable, as shown in the next section. When A varies from 0 to I
we continuously trade growth for security. Although this tradeoff is not always efficient,
it is effective in that we see a monotone increase in security as we decrease growth.
However, the rate of change in growth or security with respect to A is not constant and
thus the Kelly path is curvilinear. In fact, MacLean and Ziemba ( 1990) established that
the Kelly path is above the straight line (secant) joining the optimal growth and optimal
security points. These properties are discussed in §3.
--- page 365 ---

336
L. C. MacLean, W T. Ziemba and G. Blazenko
GROWTH VERSUS SECURITY IN DYNAMIC INVESTMENT ANALYSIS
1567
Si
Efficient frontier
Ui
Fractional Kelly path (effective)
Gi
FIGURE 1.
Graph of (Growth, Security) Profile Showing Efficient Frontier and Effective Path.
2. Computation of Measures
If we select a strategy which specifies our investment in the various opportunities and
we stick with that strategy, then each of the measures described in §2 is easily computable.
We will now develop the computational formulae. Since most of our discussion focuses
on fractional Kelly strategies, we work with them. However, more general fixed strategies
could be used.
Consider the fractional Kelly strategy p(}..) and use the transformation
Z/(p(}..) , Wi) = In YI(p(}..), Wi).
From (I) ,
ZI(P(}..), Wi) = Zo +\~ In C~ R;(Ws)P;(}..») = Z'_I(P(}..), w H
) + J(p(}..) , WI),
where J(p(}..) , w) = In ( L ;'=0 R;( w )p;(}..» is a stationary jump process and Zo = In Yo.
Hence, Z/> t = I, . .. , is a random walk and we can evaluate the various measures of
interest using this process. An alternative approach to evaluating these measures is presented in Ethier ( 1987) where the discrete time (and maybe discrete state) process YI(p(}..»
is approximated by geometric Brownian motion.
The mean wealth accumulation measure G I is
iL/(Yo, p(}..» = EYI(p(}..» = YOED C~ R;(Ws)P;(}..)) = YOC~ R;p;(}..) r (2)
where R; = ER;(w), i = 0, ... , n.
For the mean growth rate measure G2
(Myo , p(}..»
~ E In (Y,(p(}..»I /I ) = l/tEZ,(p(}..»
= E In L R;(w)p;(}..) + - Zo = EJ(p(}..), w) + - zo,
(
n
)
I
I
;~ o
t
t
(3)
which is an easy calculation to make.
For measure S I assume the process
Z,(p(}..), Wi) = Zo + L J(p(}..), ws)
s= I
--- page 366 ---

Growth versus Security in Dynamic Investment Analysis
337
1568
L. C. MACLEAN, W. T. ZIEMBA AND G. BLAZENKO
has an approximate normal distribution. Using this approximation yields
>.
_
F(bt - E(Z,(P(>'»»)
'yAyo, p( » - 1 -
u(Z,(p(>'»)
,
(4)
where F is the cumulative for the standard normal, bt = In b" and E(Z,(p(A»),
u(Z,(p(>'») are the mean and standard deviation respectively.
Measure S2 is given by
a(yo, p(A» = Pr[Z/(p(>.»:2 bt, t = I, ... ]
00
= II Pr[Z,(p(>.»:2 btIZs(p(>'»:2 b:, s = 1, . .. , /- I]
' ~
I
00
= II a,(zo, p(A».
' ~
I
Then with h,( z,1 Zs :2 b: , s = I, ... , t -
I) the conditional density
a,=J .h,(z,I Zs :2b:,s= 1, ... ,t-l)dz/
z/~ bl
where 7r(x) is the density for J(p(>.»,
- J
{J
h'- I(Z,-xI Zs:2M,s=I, ... ,t-2)
d}d
-
7r(x) x
Z,.
z,?::b;
XSZ,- b;_l
(Xt- 2
(5)
(6)
(7)
Equation (7) provides a sequential procedure to compute measure S2, requiring only
the distribution from the previous stage and the jump probabilities.
For the other measures assume that the random variable J(p( >'» has finite support
given by the interval [Jm(P(>'», JM(p(>.»]. Consider measure S3
!1(yo,p(>'» = Pr[T{y(p(~» " U ) < T { Y(p(~» " L) Iyo].
Transforming to an additive process with z = In y and letting
!1(z, p(>.» = Pr[ T{Z(p(X» " lnU ) < T{Z(p(~» " lnL) Iz]
yields
!1(zo,p(>'» = E{!1(zo + J(p(>,»,p(A»}.
(8)
The expectation in (8) is over the random variable J(p(>'». We must solve (8) for!1
subject to the boundary conditions
!1(z, p(>.»
= 0
!1( z, p( >.»
= 1
if
if
z::o;; In L
z :2 In U.
(8a)
(8b)
A solution to (8) is of the form !1( z, p( >.» = L: 1~ 1 AkOL where Ak are chosen to satisfy
(8a, 8b) and the roots 01 , ••• , Os satisfy the equation EOJ(p(~» = 1. It is easy to show
that there are two positive roots 01 = 1 and O2 = 0, where O2 < 1 or O2 > 1 depending on
whether EJ(p(A» > 0 or EJ(p(>.» < 0 respectively. Similar to the methods discussed
in Feller (1962, pp. 330-334), we take the minimum Jm(p(>.» < 0 and maximum
--- page 367 ---

338
L. C. MacLean, W T. Ziemba and G. Blazenko
GROWTH VERSUS SECURITY IN DYNAMIC INVESTMENT ANALYSIS
1569
TABLE 2
Computational Formulas for Growth Measures GI-G3 and Security
Measures SI-S3
GI
G2
q,(p) = E In (~ Ri(W)Pi)
G3
- Z
oz.
(U*(P)
u*(P»)
20
'I( 0, p) = 2EJ(p)
OU.(p) + OU'(p)
-
EJ(p)
SI
_
(b~ - Zo - tEJ(P»)
")'(20, p) = I - F
Vtu(J(p»
00
S2
<>(20, p) = IT <>/(Zo, p),
(=)
S3
JM(p("A» > 0 jumps and find bounds on the solution by solving a simple system with
the extreme boundary conditions satisfied as equalities. For the upper bound,
!J(ln L + Jm(p("A» , p("A» = 0
and
!J(ln U, p("A»
= 1.
For the lower bound,
!J(ln L, p("A»
= 0
and
Let L * = In L, L *(p("A» = In L + Jm(p("A» , U* = In U, and U*(p("A» = In U
+ JM(p("A».
The bounds for measure S3 are then
0=0 - 01.'
0=0 _ OL'(P( A»
OU'(P(A» _ OL* ~ (3(yo, p("A» ~ Ou· _ OL*(P(A» .
For measure G3,
1)(Yo,p("A» = ET I Y(p(A» " UIJ'o } = ET IZ(P(A» ,dnUlzo}'
we use the recursive equation
l1(Zo, p(>..» = E {1)(zo + J(p(>..», p(>"»} + I
subject to the boundary condition
1)(Z, p(>..»
= 0
if
Z~ In U.
(9)
( 10)
( lOa)
One solution to (10) is 1)*(z, p("A» = - z/(EJ(p("A»). Any other solution can be
written as 1)( z, p( >..» = 1)*( z, p("A» + ~(z, p("A» where ~(z , p( >..» satisfies the system
~(z, p(>..» = E{ ~(z + J(p(>..», p("A»}.
( lOb)
Solutions of ( lOb) have the form ~(z, p("A»
= L AkO%. Solutions of ( 10) are then
l1(Z, p) = L AkOZ - z/(EJ(p(>"»)
where the Ak are chosen to satisfy the boundary conditions (lOa). With U*(p(>"»
--- page 368 ---

Growth versus Security in Dynamic Investment Analysis
339
1570
L. C. MACLEAN, W. T. ZIEMBA AND G. BLAZENKO
= In U - Jm(p( X» we can solve the extreme boundary conditions as equalities, namely
1]( U*(p(X» , p(X» = 0 and 1]( U*(p(X», p(X» = 0 yields the following bounds on G3:
[ U*(P(X»]( 0=0
)
Zo
EJ(p(X»
OU.( p ( I-.»
-
EJ(p(X» ~ 1](Yo, p(X»
[ u*(P(X»](
OZO)
Zo
~ EJ(p(A»
O U *(p(I-.»
- EJ(p(X»' (II)
The bounds in (9) and (II) are quite tight when the jumps are small relative to the
initial wealth Zo.
Table 2 summarizes the formulas we can use to compute the six growth and security
measures. For G3 and S3 we have bounds and the formulas given provide midpoint
estimates of these bounds. A similar table appears in Ethier ( 1987) for the geometric
Brownian motion model.
3. Effective Growth-security Tradeoff
The fact that the various growth and security measures can be easily evaluated for
fractional Kelly strategies provides an opportunity to interactively investigate the performance of strategies for various measures and scenarios. The ability to evaluate various
performance measures and determine a preferred strategy will depend on an effective
tradeoffbetween complementary measures of growth and security. A tradeoff is effective
if the loss of performance in one dimension (say growth) is compensated by a gain in
the other dimension (security). In this section we establish that the tradeoff using fractional
Kelly strategies is effective for each of the profile combinations. In calculating the rates
of change for the various measures we will see that the tradeoff between growth and
security is not constant for all X, 0 ~ X ~ I.
(i) Rate Profile: (4), a).
LEMMA 3.1. Suppose p( X) is a Factional Kelly strategy and p is the Kelly strategy.
Then
a4>(yo , p(X» > 0
ax
'
PROOF. Consider the optimal growth strategy given by p = (Po , .. . , Pn), and the
optimal security strategy Po = ( I, 0, ... , 0).
Then
p(X) = (XPo + (I - A) , .. . , Xp n) = (Po(X) , . .. , Pn(X»
and
d
d
dXPo(X) <0,
dXP;(X»
0,
i = I, ... , n.
We have the optimal growth problem
max 4>(p(X»
= max E In C~ R i/(w)P ,(X») .
Then
and
-
24>(p(X»=-E
11
, ~ I
1/W
<0.
a2
[ I -
2.: ~1
R ( )]2
apo
2.:i~O R;,(W)Pi(X)
--- page 369 ---

340
L. C. MacLean, W T. Ziemba and G. Blazenko
GROWTH VERSUS SECURITY IN DYNAMIC INVESTMENT ANALYSIS
1571
So 4>(p(A)) is concave in Po and with Po such that a4>(p(A))/apo = 0, we have
Therefore
a
-a 4>(p(A)) < 0,
Po
d
dpo ( a
)
dA 4>(p(A)) = dA
apo 4>(p(A)) > 0
Po < Po.
and 4>(p(A)) is increasing in A.
D
LEMMA 3.2. Let p( A) be a/ractional Kelly strategy and In a < 0 be a given[allback
rate. Then
a
aA a(a, p(A)) $ O.
PROOF. We have for the security measure
a(a, p(A)) = Prob [Y,(p(A)) ~ yoa', t = I, ... ]
= II Prob [Y,(p(A)) ~ a'l Y,(p(A)) ~ a', s = 1, ... , t -
I]
I ~
I
= II a,(a, p(A)).
,,,,1
Along any path I'YI' ... 'YI_ lwithy,~ a ',s= 1, ... , t-1.
a,(a, p(A)) = Prob [In (L R"(W)P;(A)) > In a - t ~ I :~ z,],
where z, = In y, and In a - (t -
I ) - 1 L
.~: II z, < O. With b = In a - (t -
I) - I L z, and
R,P(A) = L R,,(w)p,(A) we have a,(A) ==
a,(a, p(A)) = Prob [In (R,P(A)) ~ b]
= Prob [In (AR,P + (I -
A)R,po) ~ b]
= Prob [A In (R,P) + (I - A) In (R,po) + b. ~ b]
[
b ~ b.]
= Prob In (R,P) ~ -
A-
= I -
.r~ (x(A)),
where X(A) = (b -
b.)/A and F, is the distribution function for the optimal growth
process In (R,po) .
Then dX(A)/dA > 0 and Fnondecreasing imply da,(A)/dA $ O. Hence da(a, p(A))/
dA s O.
D
Thus along the fractional Kelly path growth is increasing and security is decreasing
and an eff"cclive tradeoff is possible.
(ii) Wealth Profile: (/-L" 1'1).
LEMMA 3.3. J[p(A) is a Factional Kelly strategy then
d
dA /-L,(p(A)) > 0,
O s A s l.
--- page 370 ---

Growth versus Security in Dynamic Investment Analysis
341
1572
L. C. MACLEAN, W. T. ZIEMBA AND G. BLAZENKO
PROOF. We have
= E[YO ,~ a~O (~ R;(W, )Pj (A)) ~I C~ Rj(Ws)Pj(A))]
= -tYoE[K(w' )Y'_ 1 (W'- I)] = -tyo(EK)(EYH
) < O.
Then
d
dPo(A) a
dA J.L,(p(A)) = ---;n:- apo J.L,(p(A)) > O.
o
LEMMA 3.4.
Suppose p( A) is ajractional Kelly strategy and consider the growth rate
(\' = 1. Then
for
O ~ A <
1.
PROOF. We have
'Y,(Yu, peA)) = Prob [Y,(p(A)) ~ yoa'] = Prob [.'*1 In R,p(A) ~ tin a]
= Prob [ :z.: In (ARJj + (I -
A)RsPo) ~ 0]
= Prob [ A :z.: In (R,ij) + :z.: Ils ~ 0]
where
Ils > 0
[
- L: Ils ]
= Prob :z.: In (RJj) ~ -A-
= I - F'(x,( A)) ,
where X,(A) = (-L: Ils)/A and F' is the distribution function for L:'\ ~ I In (Rjj). Then
(d/dA)x(A) > 0 and F ' nondecreasing gives the desired result.
0
Hence for the wealth profile an effective tradeoff is possible along the fractional
Kelly path.
(iii) SlOpping Rule Profile : ( 11 - 1, (3). Our analysis of the stopping rule profile focuses
on the computational formulas ~(p(A)) and (3(p(A)). Since we have upper and lower
bounds for the true values, the accuracy of the approximation is easy to determine in a
particular application. Our choice of strategy is based on the profile graph and that
requires ~ and {3.
The formulas for ~ and (3 are based on the random walk Z,(p( A)) with jump process
J(p( A)). The process J(p( A)) isjlexible at the fractional Kelly strategy p( A) if the condition
L '*( p( A)) (J L *( p ( ~))
E1' (p( A) )(JJ(P( ~ ))
U'*( p( A)) (J U*( p( ~))
L*(p(A))(J L*( " (~ ) ) < EJ(p(A))(JJ( P(A )) < U*(p(A))(J U*(p(A) )
holds, where (J < I is a positive root of the equation E(J(p(A))J( P(A)) = I , and prime
denotes the derivative W.r.t. A.
LEMMA 3.5. Suppose p( A) is ajractional Kelly strategy and consider the wealth process
Y,(p(A)) , t = I , ... and the absorbing states U = kyo , L = k - 1yo, k > 1.IjJ(p(A)) is
jlexible at p( A) then .for 0 ~ A ~ 1
--- page 371 ---

342
L. C. MacLean, W. T. Ziemba and G. Blazenko
GROWTH VERSUS SECURITY IN DYNAMIC INVESTMENT ANALYSIS
1573
(i)
a _
ax 1)(Yo,p(X» <0,
(ii)
a -
ax {3(yo, p(X» < O.
PROOF. (i) For the mean first passage time consider the lower bound
2
X
_
U*(p(X»
1) (p( » - EJ(p(X»OU.(P(A» ,
where without loss of generality assume Yo = 1 (zo = 0). Then
where
and
N2(p(X» = [EJ(p(X»Ou,(P(X»J;n(P(X» - U*(p(X»EJ'(p(X»Ou,(p(X»
- U*(p(X»EJ(p(X»OU.(f,(A»J;Il(p(X» In 0
-
U* (p( X) )EJ(p( X»)O U.(J,(A» U* (p( X) )0' / 0],
where the prime denotes the first derivative W.r.t. Po. Since EJ'(p(X» < 0 and EJ(p(X»
> 0, J;I1(P(X» > 0, 0' < 0, we get all terms in N2(p(X» positive and (a/apo)1) 2(p(X»
> O. In the same way for the upper bound 1)1(p(X» we get (a;apo)1)I(p(X» > O. With
(d/ dX)po( X) < 0 the average of the bounds yields ( 1 ).
(ii) For the first passage probability we utilize the upper bound
1 -
OI'*(P(A»
{31(p(X» = Ou* _ OI.*(P(A»·
Then the numerator of(a;apo){3l(p(X» is
N(p(X» = (Ou* -
1) ~
OI.*(p(A» - (1 - OL*(p(A») ~
OU*.
apo
apo
We have EO(p(X»J(p( A» = 1 and (a;apo)EO(p(X»J(p(X» = 0 from which
Then
and
a
-
O(p(X»
= -O(p(X» In O(p(X))[EJ'(p(X))OJ(P(A))/ EJ(p(X»OJ(p(A»]
apo
= (-O(p(X» In O(p(X»)y;(p(X».
~
OI-*{J'(X» = OI.*(P(A»( L *(p( X» ~
0 + In 0 ~
L *(p( X»)
apo
O(p( X»
apo
apo
= - L*(p(X»OL*(P(A»y;(p(X» In 0 + L'*(p(X»OI.*(P(A» In 0,
--- page 372 ---

Growth versus Security in Dynamic Investment Analysis
1574
L. C. MACLEAN, W. T. ZIEMBA AND G. BLAZENKO
Substituting into N(p( 'J...)) with a little algebra yields
N(p('J...)) = -(O U" -
I)L *(p('J...))OL"(P(A))l/;(p('J...)) In 0
+ (J - OL"(p(A»)U*O U"l/;(p('J...) In 0
-
(O U" -
J)L'*(p('J...»)OL"(P( A» In O.
With U = kyo and L = k - 1yo it is easy to show that
U*O U"
L(p('J...))OL"(P( A))
I - OU' <
I - OL'(p(A»
and therefore
A = (J - eL"(p(A»)U*OU" > -(OU" -
I )L*(p('J...))OL'(p(A)) = B.
We have, then, substituting B for A
N(p('J...)) > 2( 1- OU") In O(L*(p('J...))OL"(p( A))l/;(p('J...)) + L'*(p('J...))OL*(P(A))) > 0
since J flexible at p( 'J...) implies
So
L *(p('J...))OL*(p( A))l/;(p('J...)) + L'*(p('J...))OL"(p(A)) < O.
a
-
{31 > O.
apo
343
With the same result for the lower bound and with (d/d'J...)p('J...) < 0 we get (ii).
0
The proof of the above lemma depends on the flexibility condition but not the requirement that the strategy be fractional Kelly. The significance of the fractional Kelly
strategies is that the flexibility condition is always satisfied if it is satisfied for the Kelly
strategy.
For the stopping rule profile (~ -
I , if) we have along the fractional Kelly path growth
increasing and security decreasing. The inverse of expected stopping time is a measure
of growth since faster growth would imply getting to the target U sooner.
In summary, for each of the profile types we have the same type of behavior. The
complementary measures, growth and security, move in opposite directions as we change
the blend between the Kelly and cash strategies. This enables a continuous tradeoff between
growth and security.
TRADEOFF THEOREM. Suppose p( 'J...) is a fractional Kelly strategy, Then for each
profile there is an effective tradeoff between growth and security by varying 'J... , the tradeqfJ index,
Additional theoretical results concerning these tradeoffs are presented in MacLean
and Ziemba ( 1990),
Friedman ( 1982) seems to have first considered fractional Kelly strategies in the context
of blackjack, His results are along the lines discussed in §4, I below. Other references on
fractional Kelly strategies are Gottlieb ( 1984); Ethier ( 1987); Li, MacLean and Ziemba
(1990) ; and Wu and Ziemba (1990).
The tradeoff theorem in this section establishes the use of growth and security measures
in determining an investment strategy. There are many possible tradeoffs depending
upon the choice of measures and the parameters specified in these measures. Rather than
further considering the preferred measures and tradeoff in theory, we will apply the
concepts to some real world examples and explore the choice of investment decisions in
practice.
--- page 373 ---

344
L. C. MacLean, W. T. Ziemba and G. Blazenko
GROWTH VERSUS SECURITY IN DYNAMIC INVESTMENT ANALYSIS
1575
4. Applications
The methods described in previous sections are now applied to a variety of well-known
problems in gambling and investment. Rather than concentrating on the results in the
tradeoff theorem, we will explore a variety of growth and security measures to see how
interactively a satisfactory decision is achieved from both perspectives. In each case we
emphasize a pair of measures (growth, security). There are a few points we should make
about our approach to these applications. Satisfaction with a particular investment strategy
will depend on many factors. The measures of performance we have described are helpful,
but they are functions of inputs such as initial wealth, return distribution, and performance
standards. We must vary those inputs in appropriate ways to see a decision rule under
different scenarios. In cases where inputs are soft we may need many diverse scenarios.
Throughout the theory and examples we use fixed strategies. This is not to imply that
the particular fixed strategy is used forever, but rather a statement that ifall inputs remain
constant we can predict the results from the fixed strategy. Of course, the inputs ,are
dynamic and we would regularly (continuously) update the strategy and measures of
performance based on new input data. This process is facilitated by easily computable
measures.
4.1. Blackjack: (¢, (3)
The game of blackjack seems to have evolved from several related card games in the
19th century. It became popular in World War I and has since reached enormous popularity. It is played by millions of people in casinos around the world. Billions of dollars
are lost each year by people playing the game. A relatively small number of professionals
and advanced amateurs, using various methods such as card counting, are able to beat
the game. The object is to reach, or be close to, twenty-one with two or more cards.
Scores above twenty-one are said to bust or lose. Cards two to ten are worth their face
value, Jacks, Queens, and Kings are worth ten points and Aces are worth one or eleven
at the player's choice. The game is called blackjack because an Ace and a ten-valued card
was paid three for two and an additional bonus accrued if the two cards were the Ace of
Spades and the Jack of Spades or Clubs. While this extra bonus has been dropped by
current casinos, the name has stuck. Dealers normally playa fixed strategy of hit until
Probability
1.0
0.8
0.6
0.4
0.2
R.lativ. growth
Optimal K.lly wag.r
0.0 -\------,,...------..-----,-------,
0.0
0.01
0.02
0.03
Fraction of W.alth Wag.r.d
FIGURE 2. Probability of Doubling and Quadrupling before Halving and Relative Growth Rates Versus
Fraction of Wealth Wagered for Blackjack (2% Advantage, p = 0.5\ and q = 0.49) .
--- page 374 ---

Growth versus Security in Dynamic Investment Analysis
1576
Range
for
Blackjack
Teams
Overkill --+
Too Risky
L. C. MACLEAN, W. T. ZIEMBA AND G. BLAZENKO
TABLE 3
Growth Rates Versus Probability of Doubling before Halving for Blackjack
/3(0, p)
= P[Doubling
"-
before Halving]
0.1
0.999
0.2
0.998
0.3
t
0.98
t
0.4
SAFER
0.94
LESS GROWTH
0.5
0.89
0.6
RISKIER
0.83
MORE GROWTH
0.7
~
0.78
~
0.8
0.74
0.9
0.70
1.0
KELLY
0.67
1.5
0.56
2.0
0.50
345
<p(p)
= Relative
Growth Rate
0.19
0.36
0.51
0.64
0.75
0.84
0.91
0.96
0.99
1.00
0.75
0.00
a seventeen is reached and then stay. A variation is whether or not a soft seventeen (ar.
ace with cards totalling six) is hit. It is slightly better for the player if the dealer stands
on soft seventeen. The house has an edge of 2-1 0% against typical players. For example,
the strategy mimicking the dealer loses about 8% because the player must hit first and
busts about 28% of the time (0.28 2 ~ 0.08).
In general, the edge for a successful card counter varies from about -10% to + 10%
depending upon the favorability of the deck. By wagering more in favorable situations
and less or nothing when the deck is unfavorable, an average edge weighted by the size
of the bet of about 2% is reasonable. Hence, an approximation that will provide us insight
into the long-run behavior of a player's fortune is to simply assume that the game is a
Bernoulli trial with a probability of success 7f = 0.51 and probability of loss I -
7f
= 0.49.
We then have Q = {O, I}, K( 0, p) = p with probability 7f, and K( I, p) = - p with
probability I - 7f. The mean growth rate is
Eln(1 +K(w,p)=7fln(1 +p)+(l-7f)ln(l-p).
Simple calculus gives the optimal fixed fraction strategy: p* = 27f -
I if EK > 0; p*
= 0 if EK ~ O. (This optimal strategy may be interpreted as the edge divided by the odds
(I-I in this case).) In general, for win or lose for two outcome situations where the size
of the wager does not influence the odds, the same intuitive formula holds. Hence with
a 2% edge betting on a 10-1 shot, the optimal wager is 0.2% of one's fortune.) The growth
rate of the investor's fortune is
rJ>(p) = 7fln(1 +p)+(I - 7f)ln(l - p)
and this is shown in Figure 2. It is nearly symmetrical around p* = 0.02. Security measure
S3 is also displayed in Figure 2, in terms of the probability of doubling or quadrupling
before halving. The bounds, from (5), are fairly sharp. Since the growth rate and the
security are both decreasing for p > p*, it follows that it is never advisable to wager more
than p*. However, one may wish to trade off lower growth for more security using a
fractional Kelly strategy. Table 3 illustrates the relationship between the fraction A and
growth and security. For example, a drop from p = 0.02 to 0.01 for a 0.5 fractional Kelly
strategy, drops the growth rate by 25%, but increases the chance of doubling before
halving from 67% to 89%.
--- page 375 ---

346
L. C. MacLean, W. T. Ziemba and G. Blazenko
GROWTH VERSUS SECURITY IN DYNAMIC INVESTMENT ANALYSIS
1577
In the blackjack example we see how the additional information provided by the
security measure (3(yo, p) was valuable in reaching a final investment decision. In a
flexible or adaptive decision environment, competing criteria would be balanced to achieve
a satisfactory path of accumulated wealth. With this approach professional blackjack
teams typically use a fractional Kelly wagering strategy with the fraction 'A = 0.2 to 0.8.
See Gottlieb ( 1985) for discussion including the use of adaptive strategies.
4.2. Horseracing: (JIt, 'Yt)
Suppose we have n horses entered in a race. Only the first three finishers have positive
return to the bettor. For the remaining positions, you lose your bet. Then
n = {( 1, 2, 3), ... , (i, j, k), ... , (n - 2, n -
1, n) }
is the set of all outcomes with probability 1fijk . We wager the fractions Pi I, Pn, Pi 3 of our
fortune Yo on horse i to win, place, or show, respectively. One collects on a win bet only
when the horse is first, on a place bet when the horse is first or second, and on a show
bet when the horse is first, second, or third. The order of finish does not matter for place
and show bets. The bettors, wagering on a particular horse, share the net pool in proportion
to the amount wagered, once the original amount of the bets are refunded and the winning
horses share the resulting profits. Let P be the n X 3 matrix of wager fractions, where
L:;'~ ) L:]~ ) Pij:$ 1. The return function for a particular (i, j, k) outcome is
K((i,j, k) , p) = (QW -
Wi) ~[) + (QP - ;i - Pj) (~i2 + ~j2)
+
-
+-+-
( QS - Si - Sj - Sk)(Pi3
Pj3
Pk3)
3
Si
Sj
Sk
- (~i PI) + I~j PI2 + Il.k P13) ,
where Q = I - the track take, Wi, Pj and Sk are the total amounts bet to win, place, and
show on the various horses, respectively, and W = L: Wi, P = L: p;, S = L: Sk .
As an example we will consider a simplified scheme where a wager is made on a single
horse per race and there are five races occurring simultaneously across tracks (Hausch
and Ziemba 1990). The required information on the races is given below. Each of the
horses has an expected return on a $1 bet of $1.14, so this is a very favorable situation.
Probability of Collecting
Race
Horse
on Wager
Odds
I
A
0.570
I-I
2
B
0.380
2-1
3
C
0.285
3-1
4
D
0.228
4-1
5
E
0.190
5- 1
The Kelly strategy is
P* = (p~, p~, pi, pr, p!, p~) = (0.8529,0.0140,0.0210,0.0141,0.0700,0.0280) .
So 1.4% of your fortune is bet on horse A in race 1. Using the growth measure JIt(p)
= mean accumulation of wealth, and the security measure 'Yt(p) = probability that
accumulated wealth will exceed b[, the Kelly strategy was compared to half Kelly and
the fixed fraction strategies which bet 0.0 I, 0.05 and 0.10 respectively, distributed across
--- page 376 ---

Growth versus Security in Dynamic Investment Analysis
1578
b,
500
1,000
5,000
10,000
100,000
I-',(p)*
L. C. MACLEAN, W . . T. ZIEMBA AND G. BLAZENKO
TABLE 4
-y,( Yo, p) = Prob Y,(p) Will Exceed b, (t = 700, Yo = 1000)
Strategy - p
Proportional
Kelly
0.5 Kelly
1%
5%
0.940
0.992
1.000
0.915
0.892
0.961
0.980
0.856
0.713
0.691
0.061
0.631
0.603
0.445
0.003
0.512
0.231
0.028
0.000
0.148
$17,497
$8,670
$2,394
$10,464
* The median is used here since Y,(p) is approximately log normal (skewed) (Ethier 1987).
347
10%
0.518
0.517
0.358
0.304
0.141
$1 ,176
horses in the proportions (0.1 , 0.3, 0.3, 0.2, 0.1). These fixed fraction strategies are not
fractional Kelly.
The results for J.Lr(P) and "(r(p) are given in Table 4. The Kelly strategy with a 6%
betting fraction and the 5% fixed fraction are similar, both having favorable growth and
security. The smaller betting fractions provide slightly more security but have much less
growth. Since the 10% strategy is beyond the Kelly fraction it has less growth and less
security. An interesting point is that the total fraction bet is more significant than the
distribution of the bets across the horses.
Implicit in the above example is the ability to identify races where there is a substantial
edge in the bettor's favor. There has been considerable research into that question. Hausch
et al. ( 1981) demonstrated the existence of anomalies in the place and show market. At
thoroughbred racetracks about 2-4 profitable wagers with an edge of 10% or more exist
on an average day. The profitable wagers occur mainly because: ( I ) the public has a
distaste for the high probability-low payoff wagers that occur on short priced horses to
place and show, and (2) the public's inability to properly evaluate the worth of place
and show wagers because of their complexity-for example, in a ten-horse race there are
72 possible show finishes, each with a different payoff and chance of occurrence. In
Hausch et al. ( 1981 ) and more fully in Hausch and Ziemba ( 1985) equations are developed that approximate the expected return and optimal Kelly wagers based on minimal
amounts of data to make the edge operational in the limited time available at the track.
Ziemba and Hausch ( 1987) implement and discuss these ideas and explore various
applications, extensions, simulations and results. A laymen's article discussing this appears
in the May 1989 issue of OMNI. A survey of the academic literature on racetrack and
other forms of sports betting is in Hausch and Ziemba (1992) .
4.3. Lollo Games: (1/, (3)
Lotteries have been played since before the birth of Christ. Organizations and governments have long realized the enormous profits that can be made, based on the greed and
hopes of the players. Lotteries tend to go through various periods of government control
and when excessive abuses occur, they have often been shut down or outlawcd, only to
resurface later. Since 1964, there has been an unprecedented growth in lottery games in
the United States and Canada. Current yearly sales are over thirty billion dollars, while
net profits to various governmental bodies are well over ten billion dollars. Since the
prizes are very large, the public cares little that the expected return per dollar wagered is
only 40-50 cents. Typically, half the money goes to prizes, a sixth to expenses, and a
third to profits. With such a low payback, it is exceedingly difficult to win at these games
--- page 377 ---

348
L. C. MacLean, W. T. Ziemba and G. Blazenko
GROWTH VERSUS SECURITY IN DYNAMIC INVESTMENT ANALYSIS
l579
Prizes
Jackpot
Bonus, 5/6+
5/6
4/6
3/6
Edge
Optimal Kelly Bet
Probability
of Winning
1/13,983,8 16
1/2,330,636
1/55,492
1/1,032
1/57
Optimal Number of Tickets
Purchased per Draw with
$10 M Bankroll
TABLE 5
Lollo Games
Prize
$6M
$0.8
M
$5,000
$150
$10
Case A
Contribution
to Expected
Value
42.9
34.3
9.0
14.5
~
118.1
18.1 %
0.000,000, I I
II
Prize
$10 M
$1.2 M
$10,000
$250
$10
Case B
Contribution
to Expected
Value
71.5
51.5
18.0
24.2
-B.1
182.7
82.7%
0.000,000,65
65
and the chances of winning any prize at all, let alone one of the big prizes, is very small.
Is it possible to beat such a game with a scientific system? The only hope of winning is
to wager on unpopular numbers in pari-mutuel lotto games. A lotto game is based on a
small selection of numbers chosen by the players. Typically, games have forty to fortynine numbers and you must choose five or six numbers. Management then draws the
winning numbers and prizes typically accrue to those with three, four or more correctly
matching numbers. By pari-mutuel, it is meant that the net pools for the various prizes
are shared by those with winning tickets. Hence, if a small number of people, with socalled unpopular numbers, win a prize, it will be larger than if more people with popular
numbers are sharing. Ziemba et al. ( 1986) investigated the Canadian 6/49, which played
across the country, and other regional games. They found that numbers ending in nines
and zeros and high numbers tended to be unpopular. Collections of unpopular numbers
have a slight edge, a dollar wagered was worth more than a dollar on average, and this
edge became fairly substantial when there was a large carryover. With a large carryover,
that is, a jackpot pool that is steadily growing because the jackpot has not been won
lately, the edge can be as high as 100% or more. Despite this promise, investors may still
lose because of the very reasons that Chernoff found, essentially reverberation to the
mean and gamblers ruin. Still, with such substantial edges, it is interesting to see how an
investor might do playing such numbers over a long period of time.
Two realistic cases are developed in Table 5. Case A corresponds to the situation when
the investor wagers only when there is a medium-sized carryover and the numbers that
are drawn are quite unpopular. Case B corresponds to the situation where there is a huge
carryover and the numbers drawn are the most unpopular. About one draw in every five
to ten is similar to Case A and one draw in every twenty or more corresponds to Case
B. Also, we have been generous in the suggested prizes. In short, we are giving the unpopular number system an at least fair chance to see ifit has any hope of being a winning
system in the long run. These cases correspond to the Canadian situation of paying the
lotto winnings in cash up front tax free. The US situation of paying the lotto winnings
over twenty years and taxing these winnings yields prizes with expected returns about
one-third of those in Canada.
First we observe that the optimal Kelly wagers are miniscule. This is not surprising
since for Case A, 77.2 cents of the $1.18 expected value and for Case B, $1.23 of the
--- page 378 ---

Growth versus Security in Dynamic Investment Analysis
1580
L. C. MACLEAN, W. T. ZIEMBA AND G. BLAZENKO
Probability
.9
.8
.7
.6
.5
.4
.3
.2
.1
.0
O.OE+OO
Optimal K!llly wager
9.7E-08
1.9E-07
2.9E-07
Fraction of wealth wagered
Double
Quadruple
Tenfold
349
FIGURE 3.
Probability of Doubling, Quadrupling and Tenfolding before Halving for Lotto 6/49, Case A.
$1.83 expected value, respectively, is composed of less than a one in a million chance of
winning the jackpot or the bonus prize. One needs a bankroll of $1 million to justify
even one $1 ticket for Case A and over $150,000 for Case B. If one had a bankroll of
$10 million, the optimal Kelly wagers are just II and 65 $1 tickets respectively. Figures
3 and 4 show the chance that the investor will double, quadruple, or tenfold his fortune
before it is halved, using Kelly and fractional Kelly strategies for Cases A and B respectively.
For the Kelly strategies, these chances are 0.4 to 0.6 for Case A and 0.55 to 0.80 for Case
B. With fractional Kelly strategies in the range of 0.00000004 and 0.00000025 or less,
the chance oftenfolding one's initial fortune before halving it is 95% or more with Cases
A and B respectively. This is encouraging, but it takes an average 294 and 55 billion
Probability
1.0
Growth rate
0.8
0.6
0.4
0.2
0.0 "-------,-------,----0"----,-----,-------,
O.OE+OO
2.0E-07
4.0E-07
Optimal Kelly
Wager
6.0E-07
8.0E-07
I.OE-06
I.2E-06
Fraction of Wealth Wagered
FIGURE 4.
Probability of Doubling, Quadrupling and Tenfolding before Halving for Lotto 6/49, Case B.
--- page 379 ---

350
L. C. MacLean, W T. Ziemba and G. Blazenko
GROWTH VERSUS SECURITY IN DYNAMIC INVESTMENT ANALYSIS
1581
o 1/2
2
6
8
10
Initial Wealth ($ million)
FIGURE 5.
Probability of Reaching the Goal of$IO Million before Falling to $! Million with Various Initial
Wealth Levels for Kelly, ! Kelly and ~ Kelly Wagering Strategies for Case A.
years, respectively, to achieve this goal. These calculations assume that there are 100
draws per year.
Figure 5 shows the probability of reaching $10 million before falling to $! million for
various initial wealth levels in the range H-$IO million for Cases A and B with full
Kelly, half Kelly and quarter Kelly wagering strategies. The results are encouraging to
the millionaire lotto player especially with the smaller wagers. For example, starting with
$1 million there is over a 95% chance of achieving this goal with the quarter Kelly strategy
for Cases A and B. Again, however, the time needed to do this is very long being 914
million years for Case A and 482 million years for Case B. More generally we have that
Case A with full Kelly will take 22 million years, half Kelly 384 million years and quarter
Kelly 915 million years. Case B with full Kelly will take 2.5 million years, half Kelly
Probability
1.00
0.8
0.6
0.4
0.2
0.00
o 1/2
2
3.08
6
8
10
Initial Wealth ($ million)
FIGURE 6. Probability of Reaching $10 million before Falling to $25,000 with Various Initial Wealth Levels
for Kelly and! Kelly Wagering Strategies for Case B.
--- page 380 ---

Growth versus Security in Dynamic Investment Analysis
351
1582
L. C. MACLEAN, W. T. ZIEMBA AND G. BLAZENKO
19.3 million years and quarter Kelly 482 million years. It will take a lot less time to
merely double one's fortune rather than tenfolding it, but it is still millions of years. For
Case A it will take 4.6, 2.6 and 82.3 million years for full, half, and quarter Kelly,
respectively. For Case B it will take 0.792, 2.6 and 12.7 million years for full, half and
quarter Kelly.
Finally, we investigate the situation for the nonmillionaire wishing to become one.
First, our aspiring gambler must pool his funds with some colleagues to get enough
bankroll to proceed since at least $150,000 is needed for Case Band $1 million for Case
A. Such a tactic is legal in Canada and in fact highly encouraged by the lottery corporations
who supply legal forms for such an arrangement. For Case A, our player needs a pool
of $1 million even if the group wagers only $1 per draw. Hence the situation is well
modeled by Figure 5. Our aspiring millionaire "puts up" $100,000 along with nine other
friends for the $1 million bankroll and when they reach $10 million each share is worth
$1 million. The pool must play full Kelly and has a chance of success of nearly 50%
before disbanding if they lose half their stake. Each participant does not need to put up
the whole $100,000 at the start. Indeed, the cash outflow is easy to bankroll, namely 10
cents per week per participant. However, to have a 50% chance of reaching the $1 million
goal each participant (and his heirs) must have $50,000 at risk. On average it will take
22 million years to achieve the goal.
The situation is improved for Case B players. First, the bankroll needed is about
$154,000 since 65 tickets are purchased per draw for a $10 million wealth level. Suppose
our aspiring nouveau riche is satisfied with $500,000 and is willing to put all but $25,000 I
2 or $12,500 of the $154,000 at risk. With one partner he can play half Kelly strategy
and buy one ticket per Case B type draw. Figure 6 indicates that the probability of success
is about 0.95. On average with initial wealth of $308,000 and full Kelly it will take ~
million years to achieve this goal. With half Kelly it will take 2.7 million years and with
quarter Kelly it will take 300 million years.
The conclusion then seems to be: millionaires who play lotto games can enhance their
dynasties' long-run wealth provided their wagers are sufficiently small and made only
when carryovers are reasonably large; and it is not possible for non-already-rich people,
except in pooled syndicates, to use the unpopular numbers in a scientific way to beat the
lotto and have confidence of becoming rich; moreover these aspiring millionaires are
most likely going to be residing in a cemetery when their distant heir finally reaches
the goal.
4.4. Playing the Turn q(the Year Ejject with Index FlIlures: (</J, (3)
Ibbotson Associates ( 1986) have considered the actual returns received from investments in US assets with different levels of risk during the period 1926-1985. While small
stocks outperformed common stocks by more than 4 to I, in terms of the cumulative
wealth levels, their advantage is totally in the last two decades and most of the gains are
in the 1974+ bull market. These returns are before taxes so that the net return after taxes
adjusted for inflation for the "riskless" investments and bonds may well be negative for
many investors.
One way to invest in this anomaly in light of the Roll ( 1983) and Ritter ( 1988) results
is to hold long positions in a small stock index and short positions in large stock indices,
because the transaction costs are less than a tenth of that of trading the corresponding
basket of securities. During the time of this study the March Value Line index was a
geometric average of the prices of about 1,700 securities and emphasizes the small stocks
while the S&P 500 is a value weighted index of 500 large stocks. Hence the VL/S&P
special makes are long in small stocks and short in big stocks at the end of the year. Each
point change in the index spread is worth $500. By January 15, the biggest gains are over
and the risks increase. On average, the spread drops 0.92 points in this period with a
--- page 381 ---

352
L. C. MacLean, W. T. Ziemba and G. Blazenko
GROWTH VERSUS SECURITY IN DYNAMIC INVESTMENT ANALYSIS
1583
Probability
1.0
0.9
0.8
Growth Rate
0.7
0.6
0.5
Double
0.4
Triple
0.3
Tenfold
0.2
0.1
o .1 .2 .3 .4 .5 .6 .7 .8 .9 1.0
Investment Fraction
FIGURE 7. Tum of Year Effect: Relative Growth Rate and the Probability of Doubling, Tripling and Tenfolding
before Halving for Various Fractional Kelly Strategies.
high variance. The projected gain from a successful trade is 0-5 points and averages 2.85
points or $1 ,342.50 per spread, assuming a commission of 1.5 X $55. On average, the
December 15 to ( -I) day gain on the spread, is 0.57 points. However, it was 1.05 in
1985 and 3.15 in 1986 which may reflect the fact that with the thin trading in the VL
index, the market can be moved with a reasonably small number of players, who are
learning about the success of this trade, i.e. the basis was bid up anticipating the January
move. The average standard deviation of the VLjS&P spread was about 3.0. With a
mean of 2.85 the following is an approximate return distribution for the trade:
Gain
7
6
5
4
2
o
- I
Probability 0.007
0.024
0.070
0.146
0.217
0.229
0.171
0.091
0.045
The optimal Kelly investment based on the return distribution is a shocking 74% of
one's fortune! Such high wagers are typical for profitable situations with a small probability
of loss. Given the uncertainty of the estimates involved and the volatility and margin
requirements of the exchanges a much smaller wager is suggested.
Figure 7 displays the probability of doubling, tripling and tenfolding one's fortune
before losing half of it, as well as the growth rates, for various fractional Kelly strategies.
At fractional strategies of 25% or less the probability of tenfolding one's fortune before
halving it exceeds 90% with a growth rate in excess of 50% of the maximal growth rate.
Figure 8 gives the probability of reaching the distant goal of $1 0 million before ruining
for Kelly, half Kelly and quarter Kelly strategies with wealth levels in the range of $0-
$10 million. The results indicate that the quarter Kelly strategy seems very safe with a
99+% chance of achieving this goal.
These concepts were used in a $100,000 speculative account for a client of CAR I Ltd.,
a Canadian investment management company. Five VLjS&P spreads were purchased
to approximate a slightly less than 25% fractional Kelly strategy. Watching the market
carefully, these were bought on December 17, 1986 at a spread of - 22.18 which was
