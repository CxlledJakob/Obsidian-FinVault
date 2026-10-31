# The Kelly capital growth investment criterion _ theory and -- Leonard C_ Maclean, Edward O_ Thorp, W_ T_ Ziemba, Leonard -- World Scientific Handbook -- isbn13 9781283148344 -- bec576e26410d0c695fd5b867d08ec4f -- An.pdf — pages 248–267

--- page 248 ---

222
E. Ordentlich and T M Cover
COST OF AC HIEVIN G THE BEST PORTFOLIO IN HI NDSIGHT
971
I- I
I- I
I- I
We/- I, I) TIXiji = I Wf- ,(k , I)
TIXiji
;=1
k=O
I-I
= I wf- , (k, 1 )XI _ I (k) ,
k=O
where wf- , (k, 1) equals We/- I, 1) when nl (/-1) = k and
The denominator can be rewritten in a similar way.
It is now clear that only the quantities X I_ I (k) need be computed and stored instead of
the exponentially many products n~: : XUi . The complexity of this is linear in I, since there
are only I such quantities. The simple recursions
suffice to update the X I_ I (k) .
The above generalizes in the obvious way to m > 2 assets resulting in a computational
complexity growing like /111- 1. Therefore, the max-min optimal portfolio is, in fact, computationally feasible for moderate m.
3.1.
Game-theoretic analysis.
A full game-theoretic result can also be proved. Specifically, we imagine the same contest as above, except that mixed strategies are allowed.
The payoff function is
A(b, x") = S,,(x") .
S:;'(x")
As before, the investor and nature respectively try to maximize and minimize the payoff.
Let $" denote the game when played with this payoff function.
A mixed strategy for the investor is a probability distribution 'P( b) on the space of
nonanticipating investment strategies, b = (b" b2(XI) , ... , b,,( X,,- I» . Similarly, nature's
mixed strategies are probability distributions on the space of price-relative sequences and
will be denoted by !l(x"). The following theorem can then be proved.
THEOREM 2.
The value of the game 9" is
max min EA(b , x") = min max EA(b, x") = V,,,
1\ 11 )
'y( XIl )
.!;I(x")
"\ )))
where V" is given by (2) . Further, the investor's optimum strategy 'J»" is the pure strategy
specified by (8) - (13 ) .
PROOF.
We prove this for m = 2, the generalization being obvious. The pure strategy
'P* is precisely the max-min optimal strategy (8) - ( 13) achieving the maximum in The-
--- page 249 ---

The Cost of Achieving the Best Portfolio in Hindsight
223
972
E. ORDENTLlCH AND T. M . COVER
orem 1. Nature's optimum mixed strategy.2* (for m = 2) consists of choosing sequences
from
'K = {X"(j") : j" E {1, 2}" }
according to the probability distribution W(j") given by (9). The proof of
(26)
min max EA(b, x") :s VII'
2(x ll )
tlb)
follows from Equations (22) through (25). The theorem follows from (26) and (] 9).
0
The full game-theoretic analysis brings out a nice symmetry between the optimal investment strategy and nature's optimal strategy. The optimal investment strategy 'P* is a
pure strategy constructed from the distribution W(j") on binary strings given by (9).
Nature's optimal strategy, on the other hand, is to choose 0-1 price-relative vectors at
random according to this same probability distribution.
This analysis generalizes to games with payoff
_
( S,,(x") )
A,(b , x") = 1> S,t(x")
,
for which the following holds.
THEOREM 3.
For concave nondecreasing 1>, the game fJ,'{1»
with payoff A",(b, x")
has a value V ($11 (1) » given by
V ($11 ( 1> » = 1>( V,,),
where VII is given by (2) and the optimal strategies are the same as those for fJ" .
3.2.
Bounds on VII'
We prove the following lemma for m = 2.
LEMMA 2.
For all n,
1
2
---
:s VII :s --- .
2[,;+1
[,;+I
PROOF.
We first prove the lower bound. In Cover and Ordentlich ( 1996), a sequential
portfolio selection strategy called the Dirichlet( 112, . . . , 1/2) weighted universal portfolio was shown to achieve a wealth S~(x") satisfying
.
S~(X")
1
mll1--- 2:
.
x" S;;'(x")
2[,;+1
Therefore
--- page 250 ---

224
E. Ordentlich and T M Cover
COST OF ACHIEVING THE BEST PORTFOLIO IN HINDSIGHT
973
.
S~(x")
2': mlll---
x" S;i'(X")
> ---
-2[,;+1'
proving the lower bound on VII'
We now establish the upper bound. Write I/VII as
VII
(27)
r(n + I)
II
k'(n - k)"- k
=
nil
k~) r(k + 1 )r(n - k + 1) ,
where r(x) = .C (, - I e - / dt is the Gamma function. If x is an integer, then rex + 1) = x!.
In Marshall and Olkin (1979), it is shown that (XI, X2) t-7 (x1'x'?) /(r(xl + 1 )r(X2 +
I» is Schur convex. This implies that under the constraint XI + X2 = n, it is minimized
by setting XI = X2 = nl2. Therefore, each term in the summation (27) can be bounded
from below by
11/2
11/2
n
n
e(n -
k)" - k
2
2
:>
r(k+ I)r(n-k+ I) -
r(~+ I)r(~+ 1)
to obtain
11/2
n/2
n
n
(n + I)r(n + I)
2'T 2 (~ + I)
The identity (see Rudin ( 1976))
(28)
2" (n + I) (n
)
r(n + I) = r;;. r - 2-
r "2 + 1 ,
can now be applied to obtain
--- page 251 ---

The Cost of Achieving the Best Portfolio in Hindsight
225
974
E. ORDENTLICH AND T. M. COVER
(29)
The log convexity of nX) (see Rudin 1976) now implies that
(30)
= r(~ +!) mIl
2
2 V~'
where we have used the identity n x + 1) = xn x). Combining (29) and (30) we obtain
= V2(n 7r+ 1)
thereby proving that
2
Vil :S )n + 1
for all n .
D
This bound can be generalized to m > 2 with the help of
r(!!.2..!.)
III
m
rc n + 1) = mil IT
( i )
, ~J rm
an extension of (28) to general m.
3.3.
Asymptotics of Vil • The following lemma characterizes the asymptotic behavior
of Vil for m stocks.
LEMMA 3.
For all m , Vil satisfies
(31 )
v ~ r( ;) (~) (III- J)12
Il
I v 7r
n
in the sense that
--- page 252 ---

226
E. Ordentlich and T M Cover
COST OF ACHIEVING THE BEST PORTFOLIO IN HINDSIGHT
975
The quantity VII arises in a variety of settings including the max-min data compression
problem (see Shtarkov 1987), the distribution of the longest common subsequence between two random sequences (Karlin 1996), and bounds on the probability of undetected
errors by linear codes (see Kl0ve 1995, Massey 1978, and Szpankowski 1995). Lemma
3 is proved in Shtarkov, Tjalkens, and Willems (1995) and an asymptotic expansion of
VII to arbitrary order is given in Szpankowski (1995, 1996). A direct proof of Lemma 3
based on a Riemann sum approximation is given in Ordentlich ( 1996).
In addition, Shtarkov ( 1987) obtains the bound
V ~ ['" (m) ~
(!!.) (i-11/2 ]-1
II
i~
i
rU!2)
2
implying one half of the asymptotic behavior in Equation (31 ).
4.
The hindsight allocation option.
The results of the previous section motivate the
analysis of the hindsight allocation option, a derivative security which pays S,T(X/), the
result of investing one dollar according to the best constant rebalanced portfolio computed
in hindsight for the observed market behavior XII . Let
-
I
HII =-.
VII
Certainly the price of the hindsight allocation option should be no higher than fill . This
follows because fill dollars invested in the nonanticipating s\Iategy described in the proof
of Theorem 1 is guaranteed to result in wealth at time n no less than S;r(xll ) for all market
sequences x". If the price of the hindsight allocation option were more than fill, selling
the option and investing only fill of the proceeds in the above strategy would be an
arbitrage. Note that this argument assumes the existence of a riskless asset for investing
the surplus.
Therefore, fill is an upper bound on the price of the hindsight allocation option valid
for any market model (with a risk free asset). Furthermore, while the return of the best
constant rebalanced portfolio is expected to grow exponentially with n, the upper bound
on the price of the hindsight allocation option fill behaves like r,;. This polynomial factor
is exponentially negligible relative to S~'
.
Is fill a reasonable price for the hindsight allocation option? Probably not; the price
should be lower. Pricing the option at fill may be appropriate if no assumptions about
market behavior can be made. This is the case in §3, where no restrictions are placed on
nature's choice for the market behavior. Returns on assets can be arbitrarily high or low,
even zero. Actual markets, however, are typically less volatile. We gain more insight into
this issue by using established derivative security pricing theory to determine the noarbitrage price of the hindsight allocation option for two much studied models of market
behavior, the binomial lattice and continuous time geometric Brownian motion models.
4.1. Binomial lattice price.
We consider a risky stock and a riskless bond. Accordingly, the price-relatives Xi are assumed to take on one of two values
--- page 253 ---

The Cost of Achieving the Best Portfolio in Hindsight
227
976
E. ORDENTLICH AND T. M. COVER
Xi E {(l + u, 1 + r)', (1 + d, 1 + r)'}
with r :2: 0, U > r > d. The first component of Xi reflects the change in the price of the
stock as measured by the ratio of closing to opening price. The second component indicates
that the riskless bond compounds at an interest rate of r for each investment period. The
parameters of the model are thus u, d, and r. If the stock price changes by a factor of 1
+ u it has gone " (u )p"; if it changes by a factor of 1 + d it has gone" (d )own."
We will find that the no-arbitrage price H" of the hindsight allocation option for this
model is closely related to fi", the upper bound obtained in the previous sections. It will
be apparent that for certain choices of d, u, and r, the upper bound fill is essentially
attained.
For a sequence of n price-relatives x" = XI, .. . , X"' the wealth acquired by a constant
rebalanced portfolio b = (b, 1 ~ b)' can be written as
where k is the number of vectors Xi for which X i i = 1 + u . Since log Sn(b) is concave
in b, the best constant rebalanced portfolio b * = (b *, 1 ~ b * )' is easily determined using
calculus. For 0 < k < n, define b * as the solution to
It is given by
d log S,,(b) = O.
db
b* = (\ + r) (_k_ ~ n ~ k) .
n
r ~ d
u ~
r
For k = 0, set b * = 0, and for k = n, set b* = 1. Then b* is given by
b * = max (0, min ( 1, b * ) ).
We then obtain the wealth achieved by the best constant rebalanced portfolio as
s,t(X") = [1 + r + b*(u ~ r)]k[l + r + b*(d ~ r)],,-k
{
(l + r)"
if b* = 0,
(1 + U)k(l + d),,- k
if b* = \,
[1 + r + h*(u ~ r)] k[l + r + h*(d ~ r)],,-k if 0 < b* < 1.
If 0 < b* < 1, the wealth achieved can be written more explicitly as
S,teXn)=(l+r + (l+r)[
k
~ n ~ k ](u~r»)k
ner ~ d)
neu ~
r)
. 1 + r + e 1 + r)
~
(d ~ r)
(
[
k
n
k ]
)"-k
n(r~d)
neu~r)
which simplifies to
--- page 254 ---

228
E. Ordentlich and T M Cover
COST OF ACHIEVING TH E BEST PORTFOLIO IN HINDSIGHT
977
( k)k(n - k)"-k(U - d)k(U - d)"-k
S;;'(x") = (1 + r) " -
--
--
--
n
11
r-d
u - r
It is well known that for this model the no-arbitrage price P" of any derivative security
with payoff S" at time 11 is given by
1
EQ S
P" = (I + r)"
(
,,) ,
where the expectation is taken with respect to Q, the so called equivalent martingale
measure on asset price changes. The unique equivalent martingale measure for this market
is a Bernoulli distribution on the sequence of "up" and " down" moves of the asset price
with the probability of an " up" equal to p" = (r - d)/ (u - d) and the " down" probability
equal to Pd = I - (r - d)/(u - d) = (u - r)/(u - d).
We note that for the case of 0 < h* < 1
( k)k(
k)"-k
S,~ (x") = (I + r)" -;;
11 ~
p,-/ p ;;(I1- k)
~ S:':(k).
Therefore,
H = EQ(S:':)
"
(1 + r)"
-
S* k
k ,,-k +
I + r "
k ,,-k
I
(n)
I
(n)
-(I+r)"k()<~'< 1 ,,() k PuP"
(I+r)" u~~ ()(
)
k PuPd
which simplifies to
H" =
I
(11) ('5.) k (~)"-k + I
(1I)p ~p;;_ k
U)< /'''< I
k
n
11
k:/'*~ O
k
( 11) ( (I + u ))k ( (I + d) ),,-k
+ !I~~ I
k
Pu ~ Pd ~
The range of k such that 0 < h* < I is
k
(U+I)
Pu< - < p" --
.
11
r+1
Thus
--- page 255 ---

The Cost of Achieving the Best Portfolio in Hindsight
229
978
E. ORDENTLICH AND T. M. COVE R
H =
L
-
-
-
+ L
pkp"-k
(n) (k)k( n - k)"-k
(n)
11
Pr/ < kln <PII(II+ 1 )/(r + I)
k
n
n
klll S PII
k
u
d
(n) ( (1 + U))k ( (1 + d) )"-k
+ k l " "'P,,(I~I )/('+I )
k
PI< ~ Pd 1+r
It is useful to note that
I + u
l+d
Pu 1+r + p" 1+r = l.
This implies that
(n) (k)k( n - k)n-k
H I! :2: P"<kl" <P~+ I)/(r + I )
k
;;
-n-
,
and
H" :5
L
-
--
+ 2.
(n)(k)k(n - k)"-k
pl/< klll < p,lu + l)/(r+l )
k
n
n
Notice the similarities between these bounds and the expression for V" = 1/ H" given by
(3 ). It is possible to choose r , u , and d so that p" < 1/ nand p" ( (u + 1) / (r + 1)) > (n
-
1 )/n , in which case the value of the hindsight allocation option is at least H" - 2.
In summary, the no-arbitrage price H" of the hindsight allocation is given by
H =
L
- --
+ L
pk p,,-k
(n) (k)k( n - k)"-k
(n)
/I
l'u< klll < p,lu+ l )/(r+i)
k
n
11
klfl'S PII
k
Ii
d
(n) ( (1 + u ) )k ( (1 + d) )"-k
+ kl" "'I'''(I~I )/(r+ l)
k
p" 1+r
p" 1+r
'
where the first summation comprises the bulk of the price for reasonable parameter values.
The terms appearing in this sum are identical to those in the expression (3) for V" = 1/
H". The number of such terms appearing in the sum depends on the parameter values. A
Reimann sum approximation argument shows that for fixed parameter values H"
~ ern, where the constant c depends only on the parameters.
4.2.
Geometric Brownian motion price.
In this section, we give the price of the
hindsight allocation option for the classical continuous time Black-Scholes market model
with one stock and one bond. The stock price X, follows a geometric Brownian motion
and evolves according to the stochastic differential equation
dX, = /1X,dt + aX,dB"
where J1 and (J are constant, and B is a standard Brownian motion. Note that here X,
denotes a price, not a price-relative. The bond price /3, obeys
--- page 256 ---

230
E. Ordentlich and T M Cover
COST OF ACHIEVING TH E BEST PORTFOLIO IN HINDSIGHT
979
d/3, = /3,rdt
where r is constant and therefore
/3, = e rt/3o·
Let S,(b) be the wealth obtained by investing one dollar at t = 0 in the constant rebalanced
portfolio b = (b , 1 - b)', where b is the proportion of wealth invested in the stock. Then
S,(b) satisfies the stochastic differential equation
(32)
dSJb) = b dX, + (1 _ b) d/3,
S,(b)
X,
/3, '
which can be solved to give
(33)
S,(b) = exp ( - b
2;2t + b( log ;~ + O";t) + (l - b)rt) .
That this solves (32) can be verified directly using Ito's lemma (see Duffie 1996, Karatzas
and Shreve 1991). Notice that, for fixed 0" 2 and r, the wealth S,(b) depends on the stock
price path only through the final price X,.
The best constant rebalanced portfolio in hindsight at time T is obtained by maximizing
the exponent of (33) for t = T under the constraint that 0 :5 b :5 I. This results in
(34)
b*-
(0 · ( ~
(LlT)IOg(XTIXo)-r))
T -
max
,mm I ,
+
0
•
2
0"-
The wealth achieved by the best constant rebalanced portfolio is then obtained by evaluating (33) at b = b?f resulting in
{
erT
S* - S (b*) -
1,,2T12)b?+rT
T-
T
T
-
e
XT
Xo
if b* =0
T
if o :5 b ~ :5
if
b~ 2 I.
From the martingale approach to options pricing, the no-arbitrage price at t = 0 of the
hindsight allocation option with duration T is given by
(35)
SrCb~)
Ho:r = /3oEQ -/3--
T
where Q is the equivalent martingale measure or the unique (in this case) probability
measure under which XJ /3, is a martingale, and assuming that ST( bj.) is integrable under
Q, which it is.
It is well known (see Duffie 1996) that under the equivalent martingale measure Q the
stock price X, obeys
dX, = rX,dt + O"X,dB,.
--- page 257 ---

The Cost of Achieving the Best Portfolio in Hindsight
231
980
E. ORDENTLlCH AND T. M. COVER
This and Ito's lemma imply that under Q, the expression log(XTIXo) appearing in the
exponent of (33) is normally distributed with mean (r -
(112 )a 2 ) T and variance a 2T.
Therefore, the random variable
is standard normal. It can be rewritten as
(36)
so that, by equation (34),
~a2T(bi) = max(O, min(~a2T, Y».
Equation (36) can be solved for XTIXo resulting in
XT
YWT +(ru '!2)T
-=e
.
Xo
The expectation (35) is then easily evaluated as
(37)
The first expectation is clearly equal to !, since Y is standard normal. The middle expectation is
Finally, the third expectation is
1
f
ro
- (1 /2)(V-WT )' d
= -
e
.
Y
&
~
1
2
--- page 258 ---

232
E. Ordentlich and T M Cover
COST OF ACHIEVING THE BEST PORTFOLIO IN HINDSIGHT
9S1
Thus (37) reduces to a surprisingly simple form. The no-arbitrage price HOJ of the hindsight allocation option is
The price is affinely increasing in the volatility (J and increases like the square root of the
duration T. The dependence on duration matches the r;; growth of the discrete-time upper
bound fi" and the binomial lattice price H". If the hindsight allocation option payoff is
redefined to be S J (x") - e rT (the excess return of the best constant rebalanced portfol io
beyond the return of the bond) then the price is simply ) (J lTI (27r) . This can be thought
of as a premium for volatility.
5.
Conclusion.
The worst sequence approach to the problem of achieving the best
portfolio in hindsight leads to a favorable result: the max-min optimal portfolio strategy
for m assets loses only « m -
I )/2) (log n)1 n in the rate of return in the worst case. This
yields an asymptotically negligible difference in growth rate as the number of investment
periods n grows to infinity. In practice we would expect even better performance, since
real markets are less volatile than the max-min market identified here. This intuition is
partially validated by the hindsight allocation pricing analysis for the binomial and geometric Wiener market models which indicates that the cost of achieving the best portfolio
in hindsight depends monotonically on market volatility.
Acknowledgment. This work was supported by NSF grant NCR-9205663, JSEP contract DAAH04-94-G-005S, and ARPA contract JFBI-94-2IS-2. Portions of this paper
were presented at CIFER 96, COLT 96, IMS 96.
References
Blackwell, D. ( 1956a). Controlled random walks. In Proceedings td Il1fernational Congress '!l Mathematics,
vol. III , pages 336- 338, Amsterdam, North Holland.
--- ( 1956b). An analog of the minimax theorem for vector payoffs. Pacific J . Mathe. 6.
Cover, T. M. (1991). Universal portfolios. Math . Finance 1( I) 1- 29.
-
-
- , D. Gluss ( 1986). Empirical Bayes stock market portfolios. Adv. Appl. Math. 7 170- 181.
---, E. Ordentlich ( 1996). Universal portfolios with side information. IEEE Trans. Itl/O. TheOlY 42( 2).
Cox, J .. C. Huang (1992). A continuous time portfolio turnpike theorem. J. Economics Dynamics and Control
16491 - 501.
Duffie, D. ( 1996). Dynamic Asset Pricing Theory . Second Edition. Princeton University Press, Princeton, New
Jersey.
Huberman, G .. S. Ross ( 1983). Portfolio turnpike theorem, risk aversion, and regularly varying functions.
Econometrica 51.
Jamshidian. F. (1992). Asymptotically optimal portfolios. Math. Finance 2(2) .
Karatzas, I., S. E. Shreve ( 1991 ). Brownian Motion and Stochastic Calculus. Graduate Texts in Mathematics.
Springer-Verlag, second edition.
Karlin. S. ( 1996). Private communication.
KklVe, T. ( 1995). Bounds for the worst case probability of undetected error. IEEE Trans . Info. Theory 41 ( I ).
Larson, D. C. ( 1986). Growth optimal trading strategies. Ph.D. thesis, Stanford University, Stanford, California.
Marshall, A. W., I. Olkin (1979) . Inequalities: Theory of Majorization and Its Applications, volume 143 of
Mathematics in Science and Engineering . Academic Press, London.
Massey, J. (1978). Coding techniques for digital networks. In Proceedings Intenwtional Conference on Information Theory Systems , Berlin. Germany.
Merhav, N .. M. Feder ( 1993). Universal schemes for sequential decision from individual data sequences. IEEE
Trans. Inli) . Theory 39(4) 1280- 1292.
Ordentlich, E. ( 1996). Universal investment and universal data compression. Ph.D. thesis, Stanford University,
Stanford. California.
--- page 259 ---

The Cost of Achieving the Best Portfolio in Hindsight
233
982
E. ORDENTLICH AND T. M. COVER
---, T. M. Cover ( 1996). On-line portfolio selection. In Proceedings of Ninth Conference on Computational
Learning Theory , Desenzano del Garda, Italy.
Rudin, W. ( 1976). Principles of Mathematical Analysis. McGraw-Hill, third edilion.
Shtarkov, Yu. M. (1987). Universal sequential coding of single messages. Problems of Information Transmission
23(3),3-17.
- --, T. Tjalkens, F. M. Willems ( 1995) . Multi-alphabet universal coding of memoryless sources. Problems
of Information Transmission 31 114- 127.
Szpankowski, W. (1995). On asymptotics of certain sums arising in coding theory. IEEE Trans. Info. Theory
41(6).
--- (1996). Some new sums arising in coding theory. Preprint.
E. Ordentlich: Hewlett-Packard Laboratories, 1501 Page Mill Road 3U-4, Palo Alto, California 94304-1126
T. M. Cover: Departments of Statistics and Electrical Engineering, Stanford University, Stanford, California
94305
--- page 260 ---

This page is intentionally left blank
--- page 261 ---

This page is intentionally left blank
--- page 262 ---

235
17
Adv. Appl. Prob.13, 415-428 (1981)
Printed in N. Ireland
0001-8678/81/020415-14$01.65
© Applied Probability Trust 1981
OPTIMAL STRATEGIES FOR REPEATED GAMES
MARK FINKELSTEIN* AND
ROBERT WHITLEY,· University of California, Iroine
We extend the optimal strategy results of Kelly and Breiman and extend the
class of random variables to which they apply from discrete to arbitrary
random variables with expectations. Let Fn be the fortune obtained at the nth
time period by using any given strategy and let F! be the fortune obtained by
using the Kelly-Breiman strategy. We show ('Theorem 1(i» that Fn/F! is a
supermartingale with E(Fn/f!):a 1 and, consequently, E(lim FJF!):a 1. This
establishes one sense in which the Kelly-Breiman strategy is optimal. However, this criterion for 'optimality' is blunted by our result ('Theorem 1(ii» that
E(Fn/F!) = 1 for many strategies differing from the Kelly-Breiman strategy.
This ambiguity is resolved, to some extent, by our result (Theorem 2) that
F!/Fn is a submartingale with E(F!/Fn)S::1 and E(limF!lFn)ii:I ; and
E(F!/Fn) = 1 if and only if at each time period i, 1;'ii i ~ n, the strategies
leading to Fn and F! are 'the same'.
KEU.Y CRITERION; OPTIMAL STRATEGY; FAVORABLE GAME; OPTIMAL GAMBLING
SYSTEM; PORTFOUO SELECI'rON; CAPITAL GROWTH MODEL
1. Introduction
Suppose a gambler is given the opportunity to bet a fixed fraction y of his
(infinitely divisible) capital on successive flips of a biased coin: on each flip,
with probability p >! he wins an amount equal to his bet and with probability
q = 1- P he loses his bet. What is a good choice for y and why is it good?
This question is subtle because the obvious answer has an obvious flaw. The
obvious answer is for the gambler to choose y = 1 to maximize the expected
value of his fortune. The obvious flaw is that he is then broke in n or fewer
trials with probability 1- p", which tends to 1 as n tends to 1Xl.
A germinal answer was given by Kelly [10]: a gambler should choose
y = p - q so as to maximize the expected value of the log of his fortune. He
shows that a gambler who chooses y = p - q will 'with probability 1 eventually
get ahead and stay ahead of one using any other value of y' ([10], p. 920).
In an important paper Breiman [4] generalizes and considers strategies other
Received 23 April 1980; revision received 12 August 1980.
• Postal address: Department of Mathematics, University of California, Irvine, CA 92717,
U.S.A.
415
--- page 263 ---

236
M Finkelstein and R. Whitley
416
MARK FINKELSTEIN AND ROBERT WHITLEY
than fixed-fraction strategies and generalizes the random variable as follows:
Let X be a random variable taking values in {I, 2, ... ,s} = I, ~ be a class
{AI> A 2, ••• , A,.} of subsets of I whose union is I, and 0b 02, ••• , 0, be positive
numbers (odds). If for one round of betting a gambler bets fractional amounts
f3I> f32, ... ,f3, of his capital on the events {X E AI}' ... , {X E A,.}, then when
X = i he gets a payoff of L f3jOj summed over those j with i in A j • In this setting
Breiman discusses several 'optimal' properties of the fixed-fraction strategy
which chooses f31> f32, . . . ,f3, so as to maximize the expected value of the log of
the fortune and then bets these fractions on each trial, leading to the fortune
F: at the conclusion of the nth trial. He shows that if Fn is a fortune resulting
from the use of any strategy, then lim F.JF~ almost surely exists and
E(lim F.JF~)~ 1. In what follows we shall be concerned solely with magnitude
results, like this asymptotic magnitude result of Breiman's, but the reader
should be aware that under additional hypotheses Breiman also shows that
T(x), the time required to have a fortune exceeding x, has an expectation
which is asymptotically minimized by the above fixed-fraction strategy.
The problem of how to apportion capital between various random variables
is exactly the problem of portfolio selection, and so it is correct to suppose that
these results on optimal allocation of capital are of considerable interest to
economists, as Kelly recognized ([10], p. 926). He also prophetically realized
that economists, familar with logarithmic utility, could easily misunderstand his
result and think, incorrectly, that the choice of maximizing the expected value
of the log of the fortune depended upon using logarithmic utility for money.
For discussion see [15], p. 216 and [17]. An interesting concise discussion of
the 'capital growth model of Kelly [10], Breiman [4], and Latane [11]' from an
economic point of view can be found in [3].
A brief discussion of Kelly's proof will motivate his criterion and allow us to
make an important conceptual distinction between his results and Breiman's.
Suppose a gambler bets the fixed fraction 'Y of his capital at each toss of the
p-coin. Kelly considers the exponential growth rate
G = lim log [(F.JFo) lin].
If our gambler has W wins and L losses in the first n trials, Fn =
(1 + 'Y)w(1- 'Y)LFO' so
G = lim (: log (1 +'Y)+;IOg (1- 'Y») = p log (1 + 'Y)+q log (1- 'Y),
by the law of large numbers. The growth rate G is maximized by 'Y = P - q, and
if he uses another 'Y his G will be less and therefore eventually so will his
fortune. A complication enters when we consider, as Kelly did not, strategies
which are not fixed-fraction strategies. In that case we can have different
--- page 264 ---

Optimal Strategies for Repeated Games
237
Optimal strategies for repeated games
417
strategies with the same G, e.g., use 'Y = 1 for the first 1000 trials and then use
'Y = P - q. This complication is intrinsic in the use of G and it has consequences
which are quite serious for any application. For example, two strategies which
at trial n give fortunes, respectively, of 1 and exp (.In), both have G = I! It is
obviously unsatisfactory to regard these two strategies with the same G as 'the
same', but it is done because using G makes it easy to extend the Kelly results
to more general situations which involve more general random variables; using
G the argument is a simple one employing either the law of large numbers or
techniques which 'rely heavily on those used to generalize the law of large
numbers' ([15], p. 218). Breiman understood the problems created by using G
and so he considered F,JF!, not (F,JF!)l'''. This is mathematically more
difficult, but the results are more useful.
2. Definitions and lemmas
We shall consider situations with the property that at each time period a
gambler can lose no more than the amount he invests, e.g., buying stock or
betting on Las Vegas table games. Since there is a real limit to a gambler's
liability, based on his total fortune, a broad interpretation of the phrase 'the
amount he invests' will allow the inclusion of such situations as selling stock
short or entering commodity futures contracts.
We suppose that there are a finite number of situations 1,2, . .. ,N on which
a gambler can bet various fractions of his (infinitely divisible) capital. The
random variables Xl> X 2 , ••• , XN represent, respectively, the outcome of a
unit bet on situations 1,2, ... , N. Because the loss can be no more than the
investment, Xk ~ -1 for 1 ~ k ~ N. (Breiman considers the amount returned to
the gambler after he has given up his bet in order to play, a real example of this
sequence of events being betting on the horses. Here the amount the gambler
gets back is ~O, which corresponds to the amount he wins being ~ -1). We
further suppose, with no loss of applicability, that in all of what follows each X k
has an expectation, i.e., that E(IXk D is finite. These will be the only restrictions
on the random variables, and so we are considering a substantially larger class
than those discrete random variables Breiman considers.
We also suppose that the gambler can repeatedly reinvest and change the
proportion of the capital bet on the situations. The outcome at time j corresponds to the random variables x:y),~), ... , XW. For each k, 1 ~ k ~ N, the
results of repeated betting of one unit on the kth situation is a sequence
X~/), Xl2), ... , x~m) , ... of independent random variables, each having the
same distribution as Xk • In contrast to this independence, it is quite important
for applications that Xl' X 2 , ••• , XN be allowed to be dependent.
--- page 265 ---

238
M Finkelstein and R. Whitley
418
MARK FINKElSTEIN AND ROBERT WHITI..EY
A strategy for the game will be a sequence 'Y(1\ • •• , 'Y(m>, ... of vectors,
'Y(m) = (y~m), 'Y~m), ... ,'Y~» giving the fractional amount 'Y~m) of the capital
which at the mth bet is bet on the kth situation. Thus 'Y~m) ~ 0, 1 ~ k ~ N, and
L~-l 'Y~m) ~ 1. We allow the possibility that 'Y(m) can depend, as a Borelmeasurable
function,
on
the
past
outcomes
XV), ... , xW,
X\2), ... ,X<J>' ... ,x\m-1), ... ,X<N'-1). (Breiman includes the sure-thing bet
Xo= 1, so that betting 'Yo on Xo is the same thing as putting 'Yo aside; in this
way his 'Y's always sum to 1. We shall not do this.)
Letting F m be the fortune which is the result of m bets using
'Y(1), 'Y(2), ... , 'Y(m), and Fo be the initial fortune,
(1)
To simplify the notation, let XO) = (x<i), ... ,XW) and denote the scalar
product with 'Y{J) = ( 'Y~)' 'Y~), .. " 'YW) by 'Y{J) . XO), obtaining
(2)
Fm = Fo n
[1 + 'Y{J) . XO)].
A fixed-fraction strategy is a strategy 'Y(m) = ('YI> 'Y2, ... , 'YN) which bets the
same amount 'Yk on situation k for all m. The result of using 'Y = 'Y(j), 1 ~ j ~ m,
for m bets is Fm = Fo &-1 (1 + 'Y . X{J». We shall be particularly interested in
'the'
fixed-fraction
strategy
'Y* = ('Yt, 'Y~, ... , 'Y~)
which
maxuruzes
E(log (Fm». In Lemma 3 we shall show that 'Y* exists, and Lemma 1 shows in
what sense it is unique. The strategy 'Y* maximizes E(log (Fm» if and only if it
maximizes the function
(3)
</>( 'Y) = </>( 'YI> ... , 'YN) = E(Iog (1 + L 'YkXk» = E(Iog (1 +"1 . X»
over the domain
(4)
D = {('Yl' "', 'YN): 'Yk~O, 1 ~k ~N, L 'Yk ~ 1}.
Lemma 1.
(i) The function </> of (3) is concave.
(ii) If </>(aa+(1-a){3)=a</>(a)+(I-a)</>({3) for 0<a<1 with </>(a) and
</>({3) finite, a . X = {3 . X almost surely. In particular, if a = (at> a2, ... ,aN)
and {3 = ({31' {32, ... , {3N) both maximize </> over its domain D, then L akXk =
L {3kXk a.s.
(iii) At 'Y = ('YI>' .. ,'YN) in D with L 'Yk < 1, the partial derivative d</>/d'Yi
exists and equals E(K;/(1 + 'Y . X», 1 ~ i ~N.
Proof.
(i) The function f(x)=log(1+x) is strictly concave on (-1,00), and so for
X=(Xl"" ,XN) a value of X,a and {3 in D, and 0<a<1,
(5)
f(aa· x+(1-a){3' x)~af(a' x)+(I-a)f({3' x),
--- page 266 ---

Optimal Strategies for Repeated Games
239
Optimal strategies for repeated games
419
an inequality which also holds if either a • x or /3 . x is -1. Integrating (5) with
respect to the probability measure P of the space on which X is defined,
<I>(aa+(1-a)/3)= Jf(aa ' X+(1-a)/3' X) dP
~ J
(af(a . X) +(1- a)f(/3 . X) dP = a<l>(a)+(1- a)<I>(/3).
(ii) Since <I> is concave the set where it attains its max is convex. If
<I>(a) = <1>(/3)
is
a
max,
then
for
0< a < 1,
<1>(00 + (1- a)/3) =
a<l>(a)+(1-a)<I>(/3), or
(6)
J
(f(a· aX+(1-a)/3 ' X)-af(a ' X)-(1-a)f(/3' X» dP=O.
From (5) and (6),
(7)
f(aa · X+(1-a)/3' X}=af(a' X)+(1-a)f(/3' X) a.s.
Because f is strictly concave, aa • X +(1- a)/3 . X = a . X = /3 • X at all values
of X where f is finite. Both sides of (7) are -00 only at values of X where
a . X = /3 • X = -1. In any case, a . X = /3 • X almost surely.
(iii) Choose E > 0 so that L 'Yk < 1- E. Then 1111 + 'Y . XI ;:a 11 E. The difference
quotient for iJ<I>/iJ'Yi is
J
log ( 1 + L 'YkXk + ('Yi + A 'YI)X; ) -log (1 + L 'YkXk)
k .. 1
dP
A~
.
(8)
Let x = (Xl' ... ,XN) be a value of X and consider the function g('Yi) =
log (1 + Lk .. i 'YkXk + 'YiXj) . By the mean value theorem,
I
g(yj + A'YJ - g(yj) 1=
IXj I
A 'Yi
11 + L 'YkXn + ~Xj I '
o < ~i < A'Yi' So the integrand in (8) is dominated by the L 1 function IX; liE for
A'Yi small. Result (iii) follows from the Lebesgue dominated convergence
theorem.
Here is a simple example which conceptually illustrates a practical use of the
Kelly-Breiman criterion: maximize E(log Fm).
Example 1. Define two random variables Xl and X2 by flipping a fair coin:
if heads, then Xl = 100 and X 2 = -10, if tails, then Xl = -1 and X 2 = 1. The
payoff from Xl is far superior to the payoff from X 2, but because Xl and X 2
are (completely) correlated and have payoffs with opposite signs, the criterion
--- page 267 ---

240
M. Finkelstein and R. Whitley
420
MARK FINKELSTEIN AND ROBERT WHITLEY
will mix both in order to smooth out the rate of capital growth. A simple
calculation shows that <1>( 'Y) = E(log (1 + 'YIXl + 'Y2X2» is maximized over D on
the face 'Yl + 'Y2 = 1 at 'Yf == 0.54 and 'Y~ == 0.46. (Lemma 3 will discuss the basic
problem created by maxima occurring at non-interior points of D.) The extent
to which the criterion will sacrifice expectation is surprising: E(O.54X1 +
0.46X2) ==24.7 vs. E(X1) =49.5.
A fascinating example of the use of this criterion, in which the underlying
idea is the same as this example, is in hedging a warrant against its stock as
described in [15], pp. 220-222.
Example 2. For A> 0, let X have density Ae-"(x+1) for x ~ -1, and 0 for
x < -1; an exponential shifted to allow losses. We shall show that there is a
unique 'Y*, 0 ~ 'Y* < 1, which maximizes <I>{y) = E(log (1 + yX», 0 ~ y ~ 1; y* =
o iff A ~ 1.
By Lemma 1,
Further,
<I>'(y) = -
rex> _x_ Ae-"(x+1) dx.
1-1 1+yx
<1>"( y) = rex>
-x2
Ae-Mx+1) dx < 0
1-1 (1 + yX)2
,
so <I> is strictly concave on [0, 1). Since <1>'(0) = E(X) = A -} -1, the strict
concavity of <I> shows that y* = 0 iff <1>'(0) ~ O.
It remains to show that for 0 < A < 1 there is a unique maximizing point y*
with O<y*< 1. By a change of variable, <I>'(y) = (Aly2)ea[g(a)-E1(a)], where
a = A«1/y) -1), g(a) = e-a/(a + A), and the exponential integral E1(a) =
J:e-'/tdt. Since El(O) =00 and g(0)=1/A, <I>'{Y)<O for 'Y close to 1; as <I> is
strictly convex, there is thus a unique point y*,0<'Y*<1, at which <I> is
maximized.
For future reference we note that it is not obvious that <I> is continuous at 1;
part of the computation involves an integration by parts and a change of
variable to obtain <1>( y) = log (1- 'Y) + ea E 1( a), a as above. The expansion
El(a)=e-a(-loga-yo+o(a» ([1], p. 229), where yo=0.577··· is Euler's
constant, shows that li.my-+l <1>( 'Y) = -log (A) - 'Yo.
In Example 2 'Y* = 0 iff E(X) ~ 0, i.e., a gambler bets on X only if it has
positive expectation. This is a special case of a more general result. Breiman
[4], p. 65, calls a game favorable if there is a strategy such that the associated
fortune Fn tends almost surely to 00 with n, and he shows that this condition is
equivalent to <I>('Y*) being positive ([4], Proposition 3, p. 68). Lemma 2
establishes the equivalence with the intuitive Condition (iv).
