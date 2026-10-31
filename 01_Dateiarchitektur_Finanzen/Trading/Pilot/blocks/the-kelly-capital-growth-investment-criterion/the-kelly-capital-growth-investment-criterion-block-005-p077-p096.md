# The Kelly capital growth investment criterion _ theory and -- Leonard C_ Maclean, Edward O_ Thorp, W_ T_ Ziemba, Leonard -- World Scientific Handbook -- isbn13 9781283148344 -- bec576e26410d0c695fd5b867d08ec4f -- An.pdf — pages 77–96

--- page 77 ---

50
L. Breiman
68
FOURTH BERKELEY SYMPOSIUM: BREIMAN
Now let >:* be such that W = W(>:*) and define A * as (>:*, >:*, ... ). Although
>:* may not be unique, the random variables Wi, W~, . .. arising from ~ are by
proposition 1 uniquely defined, and form a sequence of indepelldent,--identically
distributed random variables.
Questions of uniqueness and description of >:* are complicated in the general
case. But some insight into the type of strategy we get using A * is afforded by
PROPOSITION 2.
Let the sets AI, • • . , Ar be disjoint, then no matter what the
odds OJ are, >:* is given by Xj = P{X E A j }.
The proof is a simple computation and is omitted.
From now on we restrict attention to favorable games and give the following
criterion.
PROPOSITION 3.
A game is favorable if and only if W > O.
PROOF.
We have
n
(2.6)
log S~ = l: Wt
I
If W = EW: is positive, then the strong law of large numbers yields S~ -? 00 a.s.
(Conversely, if there is a strategy A such that Sn -? 00 a.s. we use the result of
i
section 4, which says that for any strategy A, limn SnIS~ exists a.s. finite. Hence
S~ -? 00 a.s. and therefore W ~ O. Suppose W = 0, then the law of the iterated
logarithm comes to our rescue and provides a contradiction to S~ -? 00 •
3. The asymptotic time minimization problem
For any strategy A and any number x > I, define the random variable T(x) by
(3.1)
T(x) = {smallest n such that Sn ~ x},
and T*(x) the corresponding random variable using the strategy A*. That is,
T(x) is the number of plays needed under A to amass or exceed the fortune x.
This section is concerned with the proof of the following theorem.
THEOREM 1. If the random variables Wi, W;, ... are nonlattice,t then for any
strategy
(3.2)
1 .,
lim [ET(x) -
ET*(x)] = W l: (W -
EWn )
x~~
1
and there is a constant a, indepMdent of A and x such that
(3.3)
ET*(x) -
ET(x) ~ a.
Notice that the right side of (3.2) is always nonnegative and is zero only if A
is equivalent to A * in the sense that for every n, we have W n = W~. The reason
for the restriction that W: be nonlattice is f~_ .~pI>~.re.~t. But as this restriction
is on log V: rather than on V~ itself, the common games with rational values of
the odds OJ and probabilities Pi usually will be nonlattice. For instance, a little
number-theoretic juggling proves that in the coin-tossing case the countable set
of values of P for which W~ is lattice consists only of irrationals.'"
--- page 78 ---

Optimal Gambling Systems for Favorable Games
51
OPTIMAL GAMBLING SYSTEMS
69
The proof of the above theorem is long and will be carried out in a sequence
of propositions. The heart is an asymptotic estimate of the excess in Wald's
identity [4].
PROPOSI'l'ION 4.
Let Xl, X 2, • •• be a sequence of identically distributed, independent nonlattice random variables with 0 < EX I < 00. Let Y n = Xl + ... + X n'
For any real numbers x, ~, with ~ > 0, let F,,,W = P{first Y" ~ x is < x + ~}.
Then there is a continuous distribution GW such that for every value of ~,
(3.4)
lim F",W = GW.
PROOF. The above statement is contained in known results concerning the
renewal theorem. If Xl > 0 a.s. and has the distribution function F, it is known
(see, for example, [5]) that limx-.", F",(~) = (1/ EXI ) fo~ [1 - F(t)] dt. If Xl is
not positive, we use a device due to Blackwell [6]. Define the integer-valued
random variables nl < n2 < ... by nl = {first n such that Xl + ... + Xn > O},
n2 = {first n such that X n1+1 + ... + Xn > O}, and so forth. Then the random
variables Xi = Xl + ... + X m , X~ = X n1+1 + ... + X m , ••. are independent,
identically distributed, positive, and EXi < 00 (see [6]). Letting y~ = Xi + ...
+ X~, note that P{first Y" ~ x is < x + n = P{first Y~ ~ x is < x + ~},
which completes the proof.
We find it useful to transform this problem by defining for any strategy A,
a random variable N(y),
(3.5)
N(y) = {smallest n such that W" + ... + WI ~ y}
with N*(y) the analogous thing for A *. To prove (3.2) we need to prove
1
00
(3.6)
lim [EN(y) -
EN*(y)] = W L: (W - EWn),
y_oo
1
and we use a result very close to Wald's identity.
PROPOSITION 5.
For any strategy A such that Sn -t 00 a.s. and any y
1
{N(Y)
}
1
[N(Y)
]
EN(y) = WE L: [W -
E(Wk!Rk_ I)] + WE L: Wk
•
k=l
k~l
(3.7)
PROOF.
The above identity is derived in a very similar fashion to Doob's
derivation ~
of Wald's identity. The difficult point is an integrability condition
and we get around this by using, instead of the strategy A, a modification AJ
which consists in using A for the first J plays and then switching to X*. The
condition Sn -t 00 a.s. implies that none of the W k may take on the value -
00
and that N(y) is well defined. Let N J(Y) be the random variable analogous to
N(y) under AJ and WY) to Wk. Define a sequence of random variabJes Zn by
(3.8)
This sequence is a martingale with EZn = O. By Wald's identity, ENJ(y) < 00
and it is seen that the conditions of the optional sampling theorem ([7], theorem
2.2-C3) are validated with the conclusion that EZNJ = O. Therefore
--- page 79 ---

52
L. Breiman
70
FOURTH BERKELEY SYMPOSIUM: BREIMAN
(3.9)
WENJ = E [I: W]
k-l
The second term on the right satisfies
(3.10)
y ~ E [~ WYl] ~ Y + ex,
k=l
where ex = maXj (log OJ). Hence, if EN = 00, then limJ EN J = 00, so that
E {I:fJ [W -
E(WkIRk_ 1)]} = 00 and (3.7) is degenerately true. Now assume
that EN < 00, and let J -? 00. The first term on the right in (3.9) converges to
E{I:f [W -
E(WkIRk- 1)]} monotonically. The random variables I:fJ WYl
converge a.s. to I:f W k and are bounded below and above by y and y + ex so
that the expectations conve~ge. It remains to show that limJ EN J = EN. Since
(3.11)
ENJ = ;;N~JI N dP + ;;N>JI NJ dP,
we need to show that the extreme right term converges to zero. Let
J
n+J
(3.12)
UJ = I: W k , N(UJ) = {first n such that I: Wfl ~ Y -
UJ}
1
J+l
so that
(3.13)
;;N>JI NJ dP = JP(N > J) + ;;N>J} N(UJ) dP.
Since EN < 00, we have limJ JP{N > J} = O. We write the second term as
E{E[N(UJ)IUJ]IN> J} P{N > J}. By Wald's identity,
(3.14)
On the other hand, since the most we can win at any play is ex, the inequality
(3.15)
N ~ y -
UJ + J
ex
holds on the set {N > J}. Putting together the pieces,
(3.16) r
N(UJ) dP ~ ;, r
(N -
J) dP + ; peN > J).
) {N >J}
) {N>J}
The right side converges to zero and the proposition is proven.
If we subtract from (3.7) the analogous result for A* we get
(3.17)
EN(y) - EN*(y)
1
{ N
}
1
[N
N*]
= WE I: [W -
E(WkIRk _ 1)] + WE I: W k -
I: W;
.
k=l
k=l
k=!
--- page 80 ---

Optimal Gambling Systems for Favorable Games
53
OPTIMAL GAMBLING SYSTEMS
71
This last result establishes inequality (3.3) of the theorem. As we let y ~
00,
then N(y) ~
00 a.s. and we see that
(3.18)
lim E {t [W - E(WkIRk_I)]} = t (W - EWk ).
y ..... '"
k=l
k=l
By proposition 4, the distribution Ft of Lf" Wk - y converges, as y ~
00, to
some continuous distribution F* and we finish by proving that the distribution
Fy of Lf W k -
y also converges to F*.
PROPOSITION 6. Let Y n, En be two sequences of random variables such that
Y n ~
00, Y n + En ~
00 a.s. If Z is any random variable, if E = Supn ~l lEn\, and
if we define
(3.19)
Hy(~) = P{first Y" ~ Z + y is < Z + y + ~},
(3.20)
DvW = P {first Y n + En ~ Z + y is < Z + y + ~},
then for any u > 0,
(3.21)
F,,+u(~ -
2u) -
P{E ~ u} ~ DuW ~ D.y(~) ~ H,,-'U(~ + 2u) + P{E ~ u}.
PROOF.
(3.22)
D"W ~ P{first Y n + En ~ Z + y is < Z + y +~, E < u} + P{E ~ u}
(3.23)
~ P{first Y n > Z + y -
u is < Z+ y + ~ + u, E < u} + P{e ~ u}
~ Hu-u(~ + 2u) + P{E ~ u}.
DvW ~ P{first Yn + En ~ Z + y i~ < Z + y +~, E < U}
~ P {first Y n ~ Z + y + u is < Z + y + ~ - U, E < u}
~ H11+1t(~ - 2u) -
P{E ~ u} .
PROPOSITION 7.
Let XI, X 2, ••• be a sequence of independent identically distributed nonlattice random variables, ° < EX I < 00, with Y n = X I + ... + X n·
If Z is any random variable independent of Xl, X 2, ••• , G the limiting distribution of proposition 4, and
(3.24)
F".zW = P{first Yn ~ Z + y is < Z + y +~},
then lim" F".zW = GW·
PROOF.
(3.25)
F".zW = E[P{first Y n ~ Z + y is < Z + y + ~IZ}]
= E[FII+zW],
where F,l~) = P{first Yn ~ y is < y + n. But limy FlI+zW = GW a.s. which,
together with the boundedness of F11+zW, establishes the result.
We start putting things together with
--- page 81 ---

54
L. Breiman
72
FOURTH BERKELEY SYMPOSIUM: BREIMAN
PROPOSITION 8.
Let:2:1 W k -
:2:~ W: converge a.s. to an everywhere finite limit.
If the W: are nonlattice, if Film is the distribution function for :2:f W .. -
y, then
limll Film = F*(~).
PROOF.
Fix m, let
n
n
(3.26)
~m.n = :2: W k -
:2: W;,
Em = SUp IEm.nl,
m
m
n
and by assumption ~m ~ °
a.s. Now
n
(3.27)
Film = P{first :2: Wk ~ Y is < y + ~}
1
= P{first (~ W; + Em.n) ~ Z", + y is < Zm + y + t}.
If
(3.28)
n
Hllm = P{first :2: W~ ~ Zm + y is < Zm + y + n,
m
then by proposition 6, for any u > 0,
(3.29)
HII+u(~ -
2u) -
P{~m ~ u} ~ Film ~ HlI-'U(~ + 2u) + P{Em ~ tt}.
Letting y ~
00 and applying proposition 7,
(3.30)
F*(~ -
2u) -
P{Em ~ u} ~ lim Film ~ lim Film ~ F*(~ + 2u) + P{Em ~ u}.
V
II
Taking first m ~
00 and then u ~ °
we get
(3.31)
lim Film = lim Film = F*m·
-11-
II
To finish the proof, we invoke theorems 2 and 3 of section 4. The content we use
is that if :2:1 W k -
:2:~ W: does not converge a.s. to an everywhere finite limit,
then :2:i [W - E(WkIRk _ 1)] = +00 on a set of positive probability. Therefore,
if the conditions of propositions 5 and 8 are not validated, then by (3.17) both
sides of (3.2) are infinite. Thus the theorem is proved .
.,;._ .f
~
la. Asymptotic magnitude problem
The main results of this section can be stated roughly as: asymptotically, S~
is as large as the Sn provided by any strategy A, and if A is not asymptotically
close to 11.*, then S~ is infinitely larger than Sn. The results are valid whether or
not the games are favorable.
THEOREM 2.
Let A be any strategy leading to the fortune Sn after n plays. Then
limn Sn/S: exists a.s. and E(limn Sn/S~) ~ 1.
For the statement of theorem 3 we need
DEFINITION.
A is a nonterminating strategy if there are no values of Xn stlch
that :2:tEAI >-.In)Oj = 0, for any n.
--- page 82 ---

Optimal Gambling Systems for Favorable Games
55
OPTIMAL GAMBLING SYSTEMS
73
THEOREM 3. If A is a nonterminating strategy, then almost surely
.
~
L [W -
E(Wk [Rk_ I )] = 00 ¢=> lim S" = 00.
1
n
n
(4.1)
PROOFS.
We present the theorems together as their proofs are similar and
hinge on the martingale theorems. For every n
(4.2)
If we prove that E(VnjV~IRn_l) ~ 1 a.s., then SnjS~ IS a decreasing semimartingale with limn Snj S~ existing a.s. and
(4.3)
E 1·
Sn < E So - 1
Im S·= S·-
·
n
n
0
By the definition of A*, for every E > 0,
(4.4)
E{log [(1 -
E) V: + EVn] - log V:[Rn_l} ~ o.
Manipulating gives
(4.5)
1 [(
E
V n)1
]
1
1
- E log 1 + -- -. Rn_ 1
~ - log --.
E
1 -
E Vn
E
1 -
E
By Fatou's lemma, as E --t 0
(4.6)
E (~;IRn_l) = E [lim (; log 1 + 1 ~ E ~;)IRn-1 ]
:$; lim.! log _1_ = 1.
--E
1-E
Theorem 3 resembles a martingale theorem given by Doob ([6], pp. 323-324),
but integrability conditions get in our way and force some deviousness. Fix a
number M > 0 and take A to be the event {W - E(W nIRn - 1) !?; M Lo.}. If
p = min; pi, then E(W: -
W nIRnl ) !?; M implies P {W~ -
W n !?; MIRn- 1} !?; p.
By the conditional version of the Borel-Cantelli lemma ([7], p. 324), the
set on which Li P{W~ -
Wn !?; M[Rn_l} = 00 and the set {W~ -
Wn !?; M i.o.}
are a.s. the same. Therefore, a.s. on A, we have W~ -
Wn !?; M i.o. and
log (S~jSn) = L~ (W~ -
Wk ) cannot converge. We conclude that both sides of
(4.1) diverge a.s. on A.
Starting with a strategy A, define an amended strategy AM by: if W-
E(W n[Rnl ) < M, use A on the nth play, otherwise use A * on the nth play. The
random variables
(4.7)
form a martingale sequence with
(4.8)
Un -
Un- I = W~ -
W~Ml -
[W - E(Wi.MlIRn_l)].
--- page 83 ---

56
L. Breiman
74
FOURTH BERKELEY SYMPOSIUM: BREIMAN
For AM, we have E(W: -
W~M)IRn_l) < 111, leading to the inequalities,
(4.9)
sup (W: -
W~M)) :s;; lVI,
U~ _ U,,-1 :s;; lVI.
_ p
u
_
p
On the other side, if
(4.10)
a = min log ( I: Xjoi) ,
/3 = max log 0h
j
iEAi
j
then Un -
U n-1 ~ a -
/3 - M. These bounds allow the use of a known martingale theorem ([7], pp. 319-320) to conclude that limn Un exists a.s. whenever
one of lim U" < 00, lim Un > - 00 is satisfied. This implies the statement
(4.11)
However, on the complement of the set A the convergence or divergence of the
above expressions involves the convergence or divergence of the corresponding
quantities in (4.1) which proves the theorem.
COROLLARY l. If for some strategy A, we have I:i [W - E(WkIRk _ 1) ] = 00
with probability l' > 0, then for every E > 0, there is a strategy A such that with
probability at least l' -
E, lim SnIS" = 0 and except for a set of probability at most E,
lim SnlSn ~ l.
PROOF.
Let E be the set on which lim SnIS~ = 0, with P{E} = 1'. For any
€ > 0, for N sufficiently large, there is a set EN, measurable with respect to the
field generated by RN such that P{EN DoE} < E, where Do denotes the symmetric
set difference. Define A as follows: if n < N, use A, if Rn , with n ~ N, is such
that the first N outcomes (Xl, ... ,XN) is not in EN, use A, otherwise use A*.
On EN, we have I:i [W - E(WkIRk-l)] < 00, hence limSnlS: > 0 so that
lim SnIS" = 0 on EN n E. Further, P{EN n E} ~ P{E} -
E = r -
E. On the
complement of EN, we have Sn = Sn, leading to lim SnlSn ~ 1, except for a set
with probability at most E.
5. Problems with finite goals in coin tossing
In this section we consider first the problem: fix an integer n > 0, and two
numbers y > x > 0, find a strategy which maximizes P{Sn ~ ylSo = x}. In
this situation, then, only n plays of the game are allowed and we wish to maximize the probability of exceeding a certain return. We will also be interested in
what happens as n, y become large. By changing the unit of money, note that
(5.1)
sup P{S" ~ ylSo = x} = sup P {Sn ~ 11So = ~}
where the supremum is over all strategies. Thus, the problem reduces to the
unit interval, and we may evidently translate back to the general case if we find
an optimum strategy in the reduced case. Define, for ~ ~ 0, n ~ 1,
--- page 84 ---

Optimal Gambling Systems for Favorable Games
(5.2)
and
(5.3)
OPTIMAL GAMBLING SYSTEMS
{ SUP P{Sn ~ 11So = ~},
cf>,,(~) =
1,
{a,
cf>oW = 1 ,
~ < 1,
~ ~ 1.
~ < 1,
~ ~ 1,
In addition cf>"W satisfies
(5.4)
cf>nm = supE[P{Sn ~ 11S1, So} ISo =
~]
~ sup E[cf>n-l(SI) ISo =
~]
' ~ sup
[Pcf>n-l(~ + z) + qcf>n-l(~ - z)]'
O;>z ~~
To find cf>nW and an optimal strategy, we define functions ¢n(O by
(5.5)
¢om = cf>om,
¢nm = sup [p¢n-l(~ + z) + q¢n-1(~ -
Z»)
o;>z ;:>~
57
75
having the property cf>nm ~ ¢nm, for all n, ~. If we can find a strategy A such
that under A we have ¢n(O = P{Sn ~ 11So = n, then, evidently, A is optimum,
and ¢n = cf>n. But, if for every n ~ 1, and ~ there is a ZnW, with °
~ ZnW ~ ~,
such that
(5.6)
then we assert that the optimum strategy is A defined as: if there are m plays
left and we have fortune ~, bet the amount ZmW, Because, suppose that under A,
for n = 0,1, ... ,m we have ¢nW = P{Sn ~ 11So = n, then
(5.7)
P{Sm+l ~ 11So = n = E[P{Sm+l ~ 11S1, So} ISo = ~]
= E[t,bm(S1)ISo = ~] = ¢m+lW,
Hence, we need only solve recursively the functional equation (5.5) and then
look for solutions of (5.6) in order to find an optimal strategy. We will not go
through the complicated but straightforward computation of ¢"W. It can be
described by dividing the unit interval into 2" equal intervals h '" , 12n such
that h = [k/2 n , (k + 1)/2"]. In tossing a coin with P{H} = p, rank the probabilities of the 2" outcomes of n tosses in descending order PI ~ P2 ~ .•. ~ P2-,
that is, P l = p", P2- = q". Then, as shown in figure 1,
(5.8)
cf> .. (O = L Ph
j<k
Note that if p > 1/2, then lim" cf>n(O = 1, with ~ > 0; and in the limiting case
]J = 1/2, then limn cf>n(~) =
~, with ~ ~ 1, in agreement with the Dubins-Savage
result [2].
.
There are many different optimum strategies, and we describe the one which
seems simplest. Divide the unit interval into n + 1 subintervals Ibn), '" , nn),
such that the length of Ikn) is 2-n(~) where the (~) are binomial coefficients. On
--- page 85 ---

58
L. Breiman
76
FOURTH BERKELEY SYMPOSIUM: BREIMAN
o
FIGURE 1
Graph of 4>nW for the case n = 3.
each lin) as base, erect a 45°-45° isosceles triangle. Then the graph of Zn+lW is
formed by the sides of these triangles, as shown in figure 2. Roughly, this
strategy calls for a preliminary "jockeying for position," with the preferred positions with m plays remaining being the midpoints of the intervals 11m). Notice
that the endpoints of the intervals {lin)} form the midpoints of the intervals
{11n- 1)}. So that if with n plays remaining we are at a midpoint of {lin)}, then
at all remaining plays we will be at midpoints of the appropriate system of
intervals. Very interestingly, this strategy is independent of the values of p so
o
I
"4
I
"2
FIGURE 2
Graph of Zn+lW for the case n = 3.
3
"4
--- page 86 ---

Optimal Gambling Systems for Favorable Games
59
OPTIMAL GAMBLING SYSTEMS
77
long as p > 1/2. The strategy A * in this case is: bet a fraction p - q of our
fortune at every play. Let cf>:W = P{S: ~ 11So = n. In light of the above
remark, the following result is not without gratification.
THEOREM 4.
limn sup~ [c:PnW - c:P:WJ = 0.
PROOF.
The proof is somewhat tedious, using the central limit theorem and
tail estimates. However, some interesting properties of c:P"W will be discovered
along the way. Let P{kll/2} be the probability of k or fewer tails in tossing a
fair coin n times, P{klp} the probability of k or fewer tails in n tosses of a coin
with P{H} = p. If ~ = P{kI1/2} + 2-", note that cjJ,,(~-) = P{klp}, Let
u = Vpq, by the central limit theorem, if ~t.n = P{qn + tuV;ll/2} + 2-",
then
(5.9)
uniformly in t. Thus, if we establish that
(5.10)
uniformly for t in any bounded interval, then by the monotonicity of c:PnW, c:P:W,
the theorem will follow.
By definition,
(5.11)
c:P:(~) = P{Wi + ... + W: ~ 0IWo
= log n = P {Wt + ," . + W: ~ -log~},
where the WI are independent, and identically distributed with probabilities
P{Wt = log 2p} = p and P{W: = log 2q} = q. Again using the central limit
theorem, the problem reduces to showing that
(5.12)
lim log ~n.t + nEWt = t
n
Vnu(Wt)
uniformly in any bounded interval. By a theorem on tail estimates [8J, if
Xl, X 2, • •• are independent random variables with P{Xk = 1} = 1/2 and
P{Xk = O} = 1/2, then
(5.13)
log P{Xl + ... + Xn ~ na} = n6(a) + /L(n, a) log n,
where /L(n, a) is bounded for all n, with 1/2 + 0 ~ a ~ 1 - a, and 6(a) =
-a log (2a) -
(1 -
a) log [2(1 -
a)]. Now
(5.14)
log ~n.t = log [P{Xl + ... + Xn ~ np - tuVn) + 2-n]
so that the appropriate a = p - tu/Vn with
(5. 15)
6(a) = 6(p) - ~
log 2 + 0 (1).
Vn
p
n
Since 6(p) > -log 2, we may ignore the 2-" term and estimate
--- page 87 ---

60
78
(5.16)
But 8(p)
(5.17)
FOURTH BERKELEY SYMPOSIUM: BREIMAN
log ~n.t = nO(p) -
i<TV;; log 9. + O(log n).
p
- EWi, and the left-hand expression in (5.12) becomes
t<Tlog 1!
--c:~q + 0 (log_n).
<T(Wn
vn
L. Breiman
Now the short computation resulting, <T(Wn = u log (plq), completes the proof
of the theorem.
There is one final problem we wish to discuss. Fix ~, with 0 < ~ < 1, and let
(5.18)
Tet) = E(first n with 8n ~ 1\80 = 0,
find the strategy which provides a minimum value of T(~). We have not been
able to solve this problem, but we hopefully conjecture that an optimal strategy
is: there is a number ~o, with 0 < ~o < I, such that if our fortune is less than ~o,
we use A *, and if our fortune is greater than or equal to ~o, we bet to 1, that is,
we bet an amount such that, upon winning, our fortune would be unity.
REFERENCES
[1] L. DUBINS and L. J. SAVAGE, How to Gamble if You Mus~ (tentative title), to be published . .
-[2] J. L. KELLY, JR., "A new interpretation of information rate," Bell System Tech. J., Vol. 35
(1956), pp. 917-926.
[3] R. BELLMAN, Dynamic Programming, Princeton, Princeton University Press, 1957.
[4] A. WALD, Sequemial Analysis, New York, Wiley, 1947.
[5] E . B. DYNKIN, "Limit theorems for sums of independent random quantities," /zvestiia
Akad. Nauk SSSR, Vol. 19 (1955), pp. 247-266.
[6] D. BLACKWELL, "Extension of a renewal theorem," Pacific J. Math., Vol. 3 (1953), pp.
315-320.
[7] J. L. DOOB, Stochastic Processes, New York, Wiley, 1953.
[8J D. BLACKWELL and J. L. HODGES, JR., "The probability in the extreme tail of a convolution," Ann. Math. Statist., Vol. 30 (1959), pp. 1113-1120.
--- page 88 ---

"EVlEW OF TIll! INTERNAll
STAnsnCAL INSTITlJ11
Volume 37 : 3, 1969
6
OPTIMAL GAMBLING SYSTEMS FOR FAVORABLE GAMESI
by
E. O. Thorp
Mathematics Department, University of California at Irvine
INTRODUCTION
61
In the last decade it was found that the player may have the advantage in some
games of chance. We shall see that blackjack, the side bet in Nevada-style Baccarat,
roulette, and the wheel of fortune all may offer the player positive expectation. The
stock market has many of the features of these games of chance [5]. It offers special
situations with expected returns ranging above an annual rate of 25 % [23].
Once the particular theory of a game has been used to identify favorable situations,
we have the problem of how best to apportion our resources. Paralleling the discoveries
of favorable situations in particular games, the outlines of a general mathematical
theory for exploiting these opportunities has developed [2, 3, 10, 13].
We first describe the favorable games mentioned above, those being the ones with
which the author is most familiar. Then we discuss the general mathematical theory,
as it has developed thus far, and its application to these games. Detailed knowledge
of particular games is not needed to follow the exposition. Each discussion of a
favorable game in Part I motivates a concluding probabilistic summary of that game.
These summaries suffice for the discussion in Part II so that a reader who has no
interest in a particular game may skip directly to the summary.
References are provided for those who wish to explore particular games in detail.
For the present, a favorable game means one in which there is a ::;trategy such that
P (lim Sn = (0) > 0 where Sn is the player's capital after n trials.
PART 1. FAVORABLE GAMES
1. BLACKJACK
Blackjack, or twenty-one, is a card game played throughout the world. The casinos
in Nevada currently realize an annual net profit of roughly eighty million dollars
from the game. TaKing a price/earnings ratio of 15 as typical for present day common
stocks, the Nevada blackjack operation might be compared to a $ 1.2 billion corporation.
To begin the game a dealer randomly shuffles n decks of cards and players place
their bets. (The value of n does not materially affect our discussion. It generally is
1, 2, or 4, and we shall use 1 throughout.) There are a maximum and a minimum
allowed bet.
The minimum insures a positive probability of eventual ruin for the player who
continues to bet. The maximum protects the casino from large adverse fluctuations
and in particular prevents the game from being beaten by a martingale (e.g. doubling
up), especially one starting with a massive bet. In fact, without a maximum, a casino
1 The research for this paper was supported in part by the Air Force Office of Scientific Research
through Grant AF-AFOSR 1113-66.
The paper is intended in large part to be an exposition for the general mathematical reader with some
probability background, rather than for the expert.
--- page 89 ---

62
E. 0. Thorp
274
with finite resources can in general be ruined a.s. (almost surely) by a player with
infinite resources. The player simply bets enough at each trial so that the casino is
ruined if it loses that trial. A practical way for the player to have infinite resources
would be for the casino to extend unlimited credit for the finite time it might be needed.
The players' hands are dealt after they have placed their bets. Each player then uses
skill in his choice of a strategy for improving his hand. Finally, the dealer plays out
his hand according to a fixed strategy which does not allow skill, and bets are settled.
In the case where play begins from one complete randomly shuffled deck, an approximate best strategy (i.e. one giving greatest expected return) was first given in 1956 [I].
Though the rules of blackjack vary slightly, the player following [I] typicaUy has
the tiny edge of + .10 %. (The pessimistic figure of -
.62 % cited in [I] was erroneous
and may have discouraged the authors from further analysis.) These mathematical
results were in sharp contrast to the earlier and very different intuitive strategies
generally recommended by card experts, and the associated player disadvantage of
two or three per cent. We call the best strategy against a complete deck the basic
strategy. Determined in 1965, it is almost identical with the strategy in [I] and it gives
the player an edge of + 0.13 % [22].
If the game were always dealt from a complete shuffled deck, we would have
repeated independent trials. But for compelling practical reasons, the deck is not
generally reshuffled after each round of play. Thus as successive rounds are played
from a given deck, we have sampling without replacement and dependent trials. It is
necessary to show the players most or all of the cards used on a given rOllnd of play
before they place their bets for the next round. They can then use this knowledge of
which cards have been played both to sharpen their strategy, and to more precisely
estimate their edge. (The strategies for various card counting procedures, and their
expectations, were determined directly from probability theory with the aid of computers. The results were reverified by independent Monte Carlo calculations.)
For a given card counting procedure and associated strategy, there is a probability
distribution Fe describing the player's expectation on the next hand, provided c cards
have been counted. As c increases, Fe spreads out. (This is a theorem. whose proof
resembles that for the similar theorem in Baccarat, mentioned in [24], page 316).
This spread in Fe can be exploited by placing large bets when the expectation is positive and small bets when it is negative. Part II indicates how best to do this.
If the basic strategy is always used, E(Fc) = + 0.13 %,just as from a complete deck.
But if an improved strategy, based on the card count, is used, E(Fc) increases as c
increases, approaching values of one to two per cent or more.
Ties, in which no money is won or lost, may be discounted. They occur about one
tenth of the time. Most, but not all, of the other outcomes result in the player either
winning or losing an amount equal to his original bet.
The conditional means E(Fe I Fe-d; k = 1,2, ... , c, of the successive Fe are nondecreasing. The Fe are dependent; in particular when a deck "goes good", it tends
to stay good.
Probabilistic summary
To a good first approximation, Blackjack is a coin toss where the probability p 01
success is selected independently on each trial from a known distribution F (which
is a suitably weighted average of the Fe) and announced before each trial.
A more accurate model considers that the p's are dependent in short consecutive
groups, corresponding to successive rounds of play from the same deck. Another
--- page 90 ---

Optimal Gambling Systems f or Favorable Games
63
275
more accurate observation is that insurance, naturals, doubling down, and pair
splitting. each win or lose an amount different from the amount initially bet. We do
not consider this more accurate model in part II because the improvement in results
is slight and the increase in complexity is considerable.
2. BACCARAT
The terms Baccarat and Chemin de Fer are used, sometimes interchangeably, to
refer to several closely related variants of what is essentially one card game. The game
is currently popular in England and France, where it is sometimes played for unlimited stakes. It is also played in Nevada. The game-theoretic aspects of Baccarat
have been discussed in [11,14]. The Nevada game is analyzed in [24] which includes
results of extensive computer calculations.
The studies of Baccarat show that the available bets generally offer an expectation
on the order of -1 %. The use of mixed strategies, to the very limited extent that this
is possible in some variants of the game, has but slight effect on the expectation.
Despite the resemblances between Baccarat and Blackjack, the favorable situations
detected by perfect card counting methods are not sufficient to make the game
favorable. Thus Baccarat is not in general a favorable game.
The game as played in Nevada sometimes permits certain side bets. The minimum
on the side bets was observed to be $ 5 to $ 20 and the maximum was $ 200. The bets
either won nine times the amount bet or lost the amount bet. The game was played
with eight well shuffled decks dealt from a dealing box, or shoe. Using the card
counting techniques described in [24], the side bets were favorable about 20 % of the
time. When they were favorable, the expectations ranged as high as + 100 %. The
expectation initially was about -
5 % and as the number c of cards seen increased,
the distribution Fe of expectations spread out ([24], page 316) as in Blackjack. In
practice the betting methods discussed in part II, in which the bet increased with the
expectation, doubled initial capital in twenty hours.
Unlike the Blackjack player, the Baccarat side bettor has no strategic decisions to
make so E(Fe) does not vary as c changes. When the expectation of the side bet falls
below a certain value, it is best to make a "waiting" bet on one of the main bets.
There are either two or four side bets, similar and dependent. How to apportion funds
on the side bets is complicated by the fact that there are several of them. These complexities are treated in [24].
Probabilistic summary
When only one side bet is available, the pay-off for a one unit side bet is either + 9
or -
1. If p is the probability of success, we may suppose that p is selected independently from a known distribution F and announced before each trial. When several
side bets are available, the situation is more complex. It illustrates the general setting
of [3], page 65.
As in Blackjack, a more accurate model considers that the p's are dependent in
consecutive groups, corresponding to successive rounds of play from the same ensemble of (eight) decks. It also considers the effect of waiting bets.
The situation here is more complex than in Blackjack. First, it is important to
exploit any opportunities of making simultaneous bets on two or more favorable side
bet situations. Second, the pay-off is never one to one.
--- page 91 ---

64
E. 0. Thorp
276
3. ROULETTE
Roulette has long been the prototype of unbeatable gambling games. It is normally
regarded as a repeated independent trials process which generates at each trial
precisely one from a set of random numbers. In Monte Carlo these numbers are 0,
1, 2, .. . , 36. Players may wager on particular conventional subsets of random numbers (e.g. the first dozen, even, {27}, etc.), winning if the number which comes up is
a number of the chosen subset. A player may wager on several subsets simultaneously,
and each bet is settled without reference to the others. The expectation of each bet is
negative (in Nevada generally -
5.26 %, except for one worse bet, and in Monte
Carlo -
1.35 %.) Thus it has been long known that the classical laws of large numbers
insure that the player will with probability one fall behind and stay behind, tending
to lose in the long run at a rate close to the expectation of his bets.
Despite this, Henri Poincare and Karl Pearson each examined roulette. Poincare
([20], pages 69-70, pages 76-77; [21], pages 201-203; [9], pages 61-62) supposes that
the uncertainty in initial conditions (e.g. the angular position and velocity of the ball
and of the rotor at a given time) leads to a continuous probability density / in the
ball's final position. He shows by an argument involving continuity only that if/has
sufficient spread, then the finitely many final ball positions are to very high approximation equally likely.
Karl Pearson statistically analyzed certain published roulette data and found very
significant patterns. In particular Pearson says, "If Monte Carlo roulette had gone
on since the beginning of geological time on this earth, we should not have expected
such an occurrence as this fortnight's play to have occurred once on the supposition
that the game is one of chance." And again, "To sum up, then: Monte Carlo roulette
... is ... the most prodigious miracle of the nineteenth century." I've been told that
it was later learned that the roulette data was supplied for a newspaper by journalists
hired to sit at the wheel and record outcomes. The journalists instead simply made up
numbers and submitted them. It was their personal bias that Pearson detected as
statistically significant.
It brings to mind David Hume's essay 0./ Miracles: "No testimony is sufficient to
establish a miracle, unless the testimony be of such a kind that its falsehood would be
more miraculous than the fact that it endeavors to establish .... it is nothing strange
.. . that men should lie in all ages."
Poincare assumed a mechanically perfect roulette wheel. However, wheels sometimes have considerable bias due to mechanical imperfections. Some observed instances and their exploitation are discussed in detail in [25].
In Blackjack and Baccarat, we used the following fundamental principle: The
payoff random variables, hence the favorability of a game to an optimal player, depend
on the information set used to determine the optimal strategy. For instance, if used
cards are ignored in Blackjack, then we simply have Bernoulli trials with p =
+ 0.13 %. However, as more card counting information is employed, the distribution
of p spreads out (has more structure), its expected value increases, and it can be more
effectively exploited. The roulette system we now describe illustrates the use of an
enlarged information set.
Play at roulette begins when the croupier launches the ball on a circular track which
inclines towards the center so the ball will fall into the center when it slows down
sufficiently. The center contains a rotor with a circle of congruent numbered pockets
rotating in the opposite direction to the ball. The ball eventually slows and falls from
its track on the stator, spiralling into the moving rotor and eventually coming to rest
--- page 92 ---

Optimal Gambling Systems f or Favorable Games
65
277
in a numbered pocket, the "winning number". Bets may generally be placed until the
ball leaves its track. This is crucial for what follows.
A collaborator and I tried to use the mechanical perfection of the wheel - the very
perfection needed to eliminate the bias method - to gain positive expectation. Our
basic idea was to determine an initial position and velocity for the ball and rotor. We
then hoped to predict the final position of the ball in much the same way that a
planet's later position around the sun is predicted from initial conditions, hence the
nickname "the Newtonian method".
The Newtonian method occurred to me in 1957, and by 1961 the work described
here had been completed. Although the wheel of fortune device was mentioned in
LIFE Magazine, March 27, 1964, pp. 80-91, we pointedly did not mention the roulette
work there. However, we do so in [22], page 181-182. The Newtonian method is also
mentioned in the significant book by R. A. Epstein, The Theory of Gambling and
Statistical Logic, Academic Press, pp. 135-136, (1967).
The stator has metal deflectors placed to scatter the ball when it spirals down and
the pockets are separated by vertical dividers ("frets") which also introduce scattering.
These scatterings were measured and found to be far from sufficient to frustrate the
Newtonian approach. However, there were additional sources of randomness which
did frustrate this approach. (We never satisfactorily identified these causes and can
only speculate - perhaps the causes included minute imperfections in track or ball or
high sensitivity of the coefficient of friction to dirt or atmospheric humidity.)
We were led to a variation we called the quantum method. If a roulette wheel is
tilted slightly the ball will not fall from a sector of the track on the "high" side. The
effect is strong with a tilt of just 0.2°, which creates a forbidden zone of a quarter to a
third of the wheel. The non-linear differential equation governing the ball's motion
on the track is the equation for a pendulum which at first swings completely around
its pivot, but is gradually slowed by air resistance. (It is illuminating to sketch the
orbits of the equation, as indicated in [4], page 402, problem 3.) The experimental
orbits of angle versus time could be plotted easily in the laboratory by taking a movie
of the system in motion, along with a large electric clock whose hand swept out one
revolution per second!
The existence of a forbidden zone partially quantizes the angle at which the ball
can exit, and hence quantizes the final angular position of the ball on the rotor. The
physics involved suggests that the quantization is in fact very sharp: Suppose the ball
is going to exit beyond the low point of the tilted wheel. Then it must have been
moving faster than a ball exiting at the low point, so it reaches its destination sooner.
But it has also gone farther, and the two effects tend to cancel. They in fact cancel
very well. A similar argument shows that balls which exit before the low point have
been slower, hence later, offsetting the fact they have not gone as far. Observation
verifies the conclusions of this heuristic argument.
The sharp quantization of ball final position, as a function of initial conditions,
makes remarkably accurate prediction possible.
Using algorithms, it was possible by eye judgements alone to estimate the ball's
final position three or four revolutions before exit (perhaps five to seven seconds
before exit, which was ample time in which to bet) well enough to have a + 15%
expectation on each of the five most favored numbers. A cigarette pack sized transistorized computer which we designed and built was able to predict up to eight revolutions in advance. The expectation in tests was + 44 %.
One third of the Nevada roulette wheels which we observed had the desired tilt of
at least 0.2°. The input to the computer consisted of four push-button hits: two when
--- page 93 ---

66
E. 0. Thorp
278
the 0 of the rotor crossed a fiducial mark during successive revolutions and two when
the ball crossed a fiducial mark on successive revolutions. The decay constants of ball
and rotor, approximately constant over the class of wheels observed, had been determined earlier by simple observations.
The ultimate weakness of the system was that the house could foil it by forbidding
bets after the ball had been launched.
Probabilistic summary
Roulette on a slightly tilted wheel is repeated independent trials. At each trial the
player may wager on one or more subsets of the finitely many elementary outcomes.
A wager on a subset wins if and only if it contains the elementary outcome that occurs.
There are subsets with expectations of 44 %. Our procedure in practice was to bet on
one of eight neighborhoods of five numbers. Thus the payoff for a bet of .2 units on
each of five numbers was either -lor + 6.2. The expectation of + 44 % corresponds
to a probability of success of .2. We remark that our knowledge of p increases with
the sample size.
4. THE WHEEL OF FORTUNE
The wheel of fortune, featured in many Nevada casinos, is a six foot vertical wheel
with horizontal equally spaced pegs in its rim. As the wheel spins, a rubber flapper
strikes successive pegs, slowing the wheel. There are generally 48 to 54 spaces between
the pegs, numbered with Is, 2s, 5s, lOs, 20s, and two distinct 40s. A player betting a
unit on one of these outcomes is paid that number of units if his outcome occurs. The
wheel behaves to good approximation as though a constant increment of energy is
lost each time a peg passes the flapper. Thus e, the total angle of rotation, is proportional to the energy E, which equals Iw 2, where I is the moment of inertia and w is
the angular velocity of the wheel.
In practice, a transistor timing device of match box size (a "spinoff" from the
roulette technology) produced a faint click a chosen time after a push-button was hit.
The button was hit when a specified 40 passed the flapper. The timer was set so the
click was approximately when the second 40 reached the flapper. Ifit clicked after the
second 40 reached the flapper, the wheel was "fast" and would go farther than
average before stopping. If it clicked before the second 40 reached the flapper, the
wheel was "slow".
For a given timer setting, a table was constructed empirically, giving the approximate final position of the wheel as a function of the number of spaces the second 40
was fast or slow when the click was heard.
In practice one could determine with certainty which of the two 40s could not occur.
Thus, one could always bet on the "right" 40. On a wheel observed in the Riviera
Hotel there were 50 numbers, including 22 ones, 14 twos, 7 fives, 3 tens, 2 twenties
and 2 forties. Betting on the "right" 40 would win on average 80 units in 50 trials and
lose 48, for an expectation of 32/50 or 64 %.
Probabilistic summary
Ignoring obvious refinements, we have repeated independent trials with probability
p = 1/25 of success at each trial, a payoff for a I unit bet of -
1 or + 40, and an
expectation of + 64 %.
--- page 94 ---

Optimal Gambling Systems for Favorable Games
67
279
5. THE STOCK MARKET
The stock market is a natural economic object for mathematical analysis because
vast quantities of precise historical data are available in numerical form. There have
been many attempts to mathematically predict future price behavior, using as a basis
various subsets of the available information. Most notable are the attempts to predict
future prices from past price behavior. These attempts have caused the view to be
widespread in academic circles that, to first order, common stock prices are a random
walk and changes in common stock prices are log normally distributed with a certain
mean and standard deviation [5).
Practitioners hotly contest this view. Part of the dispute is caused by practitioners
who are unwilling or unable to test their claims scientifically and part of it is due to
the success of a few practitioners who use much more information than past price
history alone. A recent study suggests strongly that "relative strength" in a price series
is continued and, consequently, that past prices do have some value in predicting
future prices [16].
Whether or not we can predict the future course of stock prices!, there are investments in combinations of securities which can yield high expected return [23]. These
investments involve convertible securities. A convertible security is one which, in
some cases with the addition of money, is exchangeable (per share) for a certain number of shares of another security. Convertible securities include convertible bonds,
convertible preferreds, stock options, stock rights, and warrants. There are several
billion dollars worth of convertibles listed on the New York and American Stock
Exchanges.
The analysis of other convertibles follows from the analysis of the common stock
purchase warrant. We therefore restrict ourselves to these in our discussion, and shall
refer to them simply as warrants.
A warrant is the right or option to buy a certain number of shares of common for
a certain price, until a certain expiration date (warrants which do not expire are
called perpetual). The terms ordinarily read: A warrants plus E dollars buy C shares
until D date. To avoid normalization problems, we suppose A = C = I. Then E is
the "exercise price" of the warrant. The prices of warrant and common are related
and it is this which allows successful investments. One observes: (I) The price Wof
the warrant should increase as the price S of the stock increases. (2) If W + E < S,
warrants can be bought and common sold short, simultaneously. The warrants are
then converted to common which is delivered against the short position. Neglecting
commissions, a profit of S - W - E per warrant results. The purchase of warrants
tends to increase Wand the sale of common tends to decrease S, until W + E > S.
Thus W > S - E normally holds. (3) The common has advantages over the warrant
such as possible dividends, or voting rights, hence we also normally expect W < S.
Thus for practical purposes points (S, W) representing (nearly) simultaneous prices
of a common stock and its warrant are confined to the part of the positive quadrant
between the lines W = Sand W = S - E.
The prices Wand S at a future time are random variables but they are related.
As E(S) increases we would expect, and past history verifies ([12, 23]), that E( W)
tends to increase. In fact the points (S, W) tend to lie on certain curves which depend
1 The great mathematician Karl Friedrich Gauss was successful in the market but we have little
knowledge of his methods. On a basic salary of 1000 thalers per year he left an estate in cash plus
securities of 170,857 thalers ([7], page 237).
--- page 95 ---

68
E. 0. Thorp
280
on several variables, most notably the time remaining until expiration of the warrant.
Thus, although we may not know the price S of the common, or the price W of the
warrant at a given future time, we do know that ( W, S) is near one of these curves.
The family of curves qualitatively resembles the family W = (SZ + £Z)l/Z - E, where
z = 1.3 + 5.3/T and T is the number of months remaining until expiration.
A historical study of expiring warrants (from here on we limit ourselves for convenience to warrants traded on the American Stock Exchange) suggests that during
the last two years or so before expiration they tend to trade at prices which are much
too high. For instance the average loss from buying each of a certain 11 listed warrants 18 months before expiration and holding until 2 months before expiration was
46.0 %, an annual rate of 34.5 % ([23], page 37). Thus selling warrants short seems to
yield high expectation. However, it also happens to result in occasional large losses
which, by the criterion of Part II, are extremely undesirable despite the high overall
expectation. We can sharply reduce this high variance and yet retain a high expectation by using the so-called warrant hedge. The technique is to simultaneously sell
short overpriced warrants and buy common in a fixed ratio (generally from one to
three warrants will be shorted for each share of common bought). The position is
held until just before expiration of the warrant (at which time the warrant sells at a
"correct" price) and then it is liquidated.
Here is the rationale. We are mixing two investments with positive annual expectations of say 34.5 % for the warrants and 10 % for the common, resulting in an investment whose overall expectation must therefore be somewhere between these figures.
(We suggest 10% for the common because this approximates the observed mean rate
of return from common stocks during this century due to price appreciation plus
dividends.) Buying the common leads to a gain when the common rises and a loss
when it falls whereas shorting warrants leads to a gain when the common falls and
leads to a loss only if the common rises substantially. Thus the risks tend to cancel
out. In fact, the hedge generally yields a profit upon expiration of the warrant, for a
wide range of prices of the common.
If we make assumptions about the probability distribution of the price of the common at expiration of the warrant, we get more precise information about the random
variable representing the payoff from the hedge. Let the probability measure P with
support [0, 00) describe the distribution of the stock price Slat expiration. Then
00
E ( Sf) = J x" d P ( x ) .
o
Let So be the present price and let E be the exercise price. Assume that P( S I > So
+ t) > P(SI < So - t) for each t > 0, i.e. for any t, the chance of a price rise of at
least t is no less than the chance of a price drop of at least t. This is a very weak
assumption. Note that it does imply E( S I) > So·
Just before expiration WI == 0 if SI < E and WI == SI - E if SI > E. Thus the
final gain from shorting a warrant at Wo is Wo if S I < E and is Wo - Sf + E if
S I > E. The gain from buying a share of common at So is, of course, Sf - So·
Hence if we assume one share of common is purchased at .5E and one warrant is
shorted at .2E, the final gain G I is S I - .3E if S I < E and. 7 E jf Sf > E. A standard
measure-theoretic argument yields E( G I) > .2E. Using 100% margin, the percent
profit is E( G I) / .7 E > 28 %. With 100 % margin on the warrants and 70 % margin
on the common, it is at least .2E / .55E > 36 %. With 70 % margin on each, it is at
least .2 / .49 > 40 %, an annual rate of more than 20 % jf the warrant expires in
two years.
--- page 96 ---

Optimal Gambling Systems for Favorable Games
69
281
It is interesting to calculate E( G J ) by assuming that S J is log normally distributed.
Letting S J = S J I E, we thus assume that S J has the density function
f ( x) = (x cr .J2"it) -1 exp [ - (In x - Jl)2 I 2 cr2 ], where Jl and cr are parameters depending on the stock. We note E (s J) = exp (Jl + cr2 /2).
If t is the time in months remaining until expiration (which is when S J is realized),
then we assume (J. = log So + mt and 0"2 = a2t, where So = So E is the present stock
price and m and a are constants depending on the stock. Thus E(s J) = So exp
[em + a2/2)t]. A mean increase of 10% per year is approximated by setting 12(m +
a2/2) = .1. If we estimate a2 from past price changes we can solve for m.
Letting w, = WIlE, where W, is the final warrant price, a calculation yields
E( w,) = E(s,) N«(J./O" + 0") - N«(J./O"), where N is the normal distribution. (Compare
the equivalent expression from pp. 464-466 of [5].) Now suppose that So = .5, that a
has the realistic value of .Iso or .05, and that 12(m + a2/2) = .1, whence m =
.085/12. Then for t = 24 we have cr = ).06 = .245 and Jl = log .5 + .17 = -.523.
This yields E(w,) = .0015 and E(s,) = .61, whence E(G,) = .20 + .11 = .31. Thus
the profit, with 70% margin on both warrant and common, is .31/.49 or 63.3% and
the annual rate is 31.6 %. Note that the warrant is virtually worthless!
Instead of selling one warrant short and buying one share of common, we can sell
short w warrants and buy s shares of common. Neglecting commissions, which we do
throughout for simplicity, the gain G at any point (S, W) is s(S - So) -we W - Wo).
Thus the line G = 0, the zero profit line, is the line through (Wo, So) with positive
slope slw = 11m. We call m the mix. Points below the zero profit line represent gain
and points above it represent loss. If 1 < m < co, the zero profit line intersects the S
axis at So - m Wo and it intersects the line W = S - E at S = [me Wo + E) - So] /
(m - 1); W = (m Wo + E - So) I (m - 1).
When the warrant expires the hedge position will yield a profit if S, is between
the S values of the two intersections and it will yield a loss if S, is beyond the intersections. For instance, if So = .5E and Wo = .2E, the choice m = 2 insures a final
profit if .IE < s, < 1.9E. Such safety is characteristic of the warrant hedge.
The final gain G, is s(S,- So) + wWo if S, < E and it is sCSI - So) + w( Wo +
E - S,) if S, > E. Thus as a function of S, it is an inverted "V" with apex above
S, = E. With 100 % margin, the initial investment is s So + w Wo so the gain per
unit invested is g, = G ,/(s So + w Wo). With margin of ot on the common and f3 on
the warrants it is g, = G,/(ot s So + f3 w Wo).
We have assumed so far that a hedge position is held unchanged until expiration,
then closed out. This static or "desert island" strategy is not optimal. In practice
intermediate decisions in the spirit of dynamic programming lead to considerably
superior dynamic strategies. The methods, technical details, and probabilistic summary are more complex so we defer the details for possible subsequent publication.
Probabilistic summary
The warrant hedge may offer high expectation with low risk. The gain per unit
g,isg, = [(Sf + So) + m Wo] / (ot So + f3m Wo) when SJ < Eandg, = [(S,- So)
+ m( Wo + E - Sf)] / (ot So + f3m Wo) if SJ > E. The gain per unit depends only
on the random variable S ,. This has an unknown distribution but it can be estimated.
The other quantities are constants depending on circumstances.
