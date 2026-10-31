# The Kelly capital growth investment criterion _ theory and -- Leonard C_ Maclean, Edward O_ Thorp, W_ T_ Ziemba, Leonard -- World Scientific Handbook -- isbn13 9781283148344 -- bec576e26410d0c695fd5b867d08ec4f -- An.pdf — pages 552–571

--- page 552 ---

Understanding the Kelly Criterion
523
In contrast to Proebsting's example, the property that betting Kelly or any fixed
fraction thereof less than one leads to exponential growth is typically derived by
assuming a series of independent bets or, more generally, with limitations on the degree of dependence between successive bets. For example, in blackjack there is weak
dependence between the outcomes of successive deals from the same unreshuffied
pack of cards but zero dependence between different packs of cards, or equivalently
between different shuffiings of the same pack. Thus the paradox is a surprise but
doesn't contradict the Kelly optimal growth property.
R eferences
Ethier, S. (2010) . The Doctrine of Chances. Berlin: Springer-Verlag.
Geyer, A. and W. T . Ziemba (2008) . The innovest Austrian pension fund financial planning
model InnoALM. Operations Research, 56(4), 797- 810.
MacLean, L. C., W . T. Ziemba and G. Blazenko (1992). Growth versus security in dynamic
investment analysis. Management Science, 38, 1562- 1585.
Markowitz, H. M. and E. van Dijk (2006). Risk return analysis, in S. A. Zenios and
W. T. Ziemba (eds.) , Handbook of Asset and Liability Management, Vol. I: Theory
and Methodology. Amsterdam: North Holland, 139- 197.
Pabrai, M. (2007). The Dhandho Investor. New York: Wiley.
Poundstone, W. (2005). Fortune 's Formula. US: Hill and Wang.
Taleb, N. N. (2007). The Black Swan: The Impact of the Highly Improbable. US: Barnes
and Noble.
Thorp, E. O. (2006). The Kelly Criterion in blackjack, sports betting and the stock market,
in S. A. Zenios and W. T. Ziemba (eds.) , Handbook of Asset and Liability Management, Vol. I: Theory and Methodology. Amsterdam: North Holland, 385- 428.
Thorp, E . O. and R. Whitley (1972). Concave utilities are distinguished by their optimal
strategies. Colloquia Mathematica Societatis Janos Bolyai, 9.
Thorp, E. O. and R. Whitley (1974). Progress in statistics, in Proceedings of the European
Meeting of Statisticians, Budapest. North Holland, pp. 813- 830.
Ziemba, R. E. S. and W. T. Ziemba (2007). Scenarios for Risk Management and Global
Investment Strategies. New York: Wiley.
Ziemba, W. T. (2003). The Stochastic Programming Approach to Asset Liability Management. AIMR.
Ziemba, W . T . and R. G. Vickson, eds. (2006) . Stochastic Optimization Models in Finance,
2nd Edition. Singapore: World Scientific.
--- page 553 ---

This page is intentionally left blank
--- page 554 ---

525
COLLOQUIA MATHEMATICA SOCIETATIS JA.NOS BOLVAI
9 . EUROPEAN MEETING OF STATISTICIANS, BUDAPEST (HUNGARY) . '972.
37
CONCAVE UTILITIES ARE DISTINGUISHED BY THEIR
OPTIMAL STRATEGIES
E . THORP -- R. WHITLEY
1. INTRODUCTION
Mossin [5], Thorp [7], and Samuelson [6] showed for specific pairs of utility functions that different utilities can lead to different
optimal strategies. In particular the optimal investment strategy for the
utility logx is not necessarily the optimal strategy for the utility 1 x'Y
'Y
These examples suggest the following generalization, of obvious importance to general utility theory.
Consider a T stage investment process. At each stage allocate resources among the available investments. Each chosen sequence A of allocations ("strategy") yields a corresponding terminal probability distribution F1 of assets at the completion of stage T. For each utility function U(.), consider those strategies A *( U) which maximize the expected value f U(x)dF1 (x) of terminal utility. Assume sufficient hypotheses
- 813 -
--- page 555 ---

526
E. Thorp and R. Whitley
on U and the set of F1 so that the integral is defined and that furthermore the maximizing strategy A *( U) exists. Then is it true in general
that A*(U1 ) is not A*(U2 ) for "distinct" utilities UI
and U2?
As we now show, the answer is yes: the Mossin - Thorp - Samuelson
results for specific utility pairs generalizes to the principal class of interest
in modern utility theory.
2. THE MAIN THEOREM
We prove this for the class of "interesting" concave utilities. We begin with more special hypotheses.
Theorem 1. Let U and V be utilities defined and differentiable
on (0,00) with U'(x) and V'(x) positive and strictly decreasing as x
increases. Then if U and V are inequivalent, there is a one period investment setting such that U and V have distinct sets of optimal strategies. Furthermore, the investment setting may be chosen to consist only
of cash and a two-valued random investment, in which case the optimal
strategies are unique.
Corollary 2. If the utilities U and V have the same (sets of) optimal strategies for each finite sequence of investment settings, then V and
V are equivalent.
Two utilities UI
and U2 are equivalent if and only if there are
constants a and b such that UzCx) = aUI (x) + b (a> 0), otherwise
VI
and U2 are inequivalent.
Let X. (I ~ i ~ k) be the (random) outcome per unit invested in
I
the ith "security". We call (Xl"'" Xk ) the investment setting. We assume X. is independent of the amount invested. Let the initial capital be
I
Zo and let the final capital be ZI' A strategy is an allocation W =
= (WI' . .. , wk ) where
Wj is the fraction of Zo allocated to security i.
We assume w. ~ ° for all i, that Z w. = I, and that wealth is infinite-
I
j
I
ly divisible. Thus the w. may assume any real values consistent with the
I
- 814 -
--- page 556 ---

Concave Utilities are Distinguished by Their Optimal Strategies
527
constraints and with the requirement that ~ wiX, is in the domain of
the utility function U.
I
Given a particular U satisfying the hypotheses of the theorem, suppose E U(Zl (W)) is maximized by some strategy W*. Then W* is an
optimal (or best) strategy for U relative to the given investment setting.
Proof of Theorem. Suppose that U and V have the same optimal
strategies for everyone period investment setting consisting of cash and a
two-valued random investment. It will be shown that U and V are equivalent, which will establish the logical contrapositive to the theorem and
hence the theorem itself.
In the proof of theorems we shall assume for technical simplicity
that the initial capital Zo = 1. When theorems have been established for
this case, consideration of the transformation Uo(s) = U(Zos) = UU)
gives the theorems for arbitrary Zo > O. We shall therefore state the general results without further comment after proving the Zo = 1 case.
Let the only investment (besides cash) be X where P(X = 1 - b) =
= q = 1 - p and P(X = 1 + a) = p, where a> 0 and 0 < p, b < 1.
The choice 0 < b < I, rather than simply b = I, has been made because
for b = 1 arid w = I, the expression U(O) would arise and 0 is not
necessarily in the domain of U (e.g., U(x) = log x). The available strategies are to allocate the fraction w of recources to X and 1 - w to
cash, with 0 ~ w ~ 1.
At the end of the period, we have
(2.1)
EU(ZI (w») = pU(l + aw) + qU(l - bw) = ftw) .
To find the maximum, consider f'(w) = apU'(l + aw) - bqU'(lbw).
Since U'(t) strictly decreases as t increases, we have f'(w) decreasing
strictly as w increases. Thus there is a unique maximum. If f'(w*) == 0
for some w* with 0 ~ w* ~ I, then the maximum is at this unique w* .
If i'(w) > 0 for all w with 0 ~ w ~ 1, then the unique maximum is
at w = 1. If instead f'(w) < 0 for 0 ~ w ~ 1, then the unique maximum is at w = O.
- 815 --
--- page 557 ---

528
E. Thorp and R. Whitley
If f '( ) - 0
h
u
~ 1 + aW) - !!!I SOd
w -
we
ave
U'(l _ bw) -
ap'
uppose a>
an
1
, 1
.
U' (I + 2~)
2 < b < 1 are given and we wish f (2b) = O. Lettmg A =
I'
U'("2)
we can solve A = Pfp for p, with 0 < p < 1. Thus for each a> 0
1
there is a choice of p, hence an X, such that w* = 2b is optimal for
U.
Now suppose that U and V have the same optimal strategies for
all such investment settings. Then w* = 2Ib for V also and we have
U' (l + 2~)
V' ( 1 + ~)
1
1
--~l-
=
1
for all a > O. Letting V' ( -2) = o:U' ( -2 )
U'("2)
V'( 2)
we find V'(t) = o:U'(t) (t> 1) whence V(t) = o:U(t) + f3 (t> I).
When t < 1, we proceed similarly. Choose X so that P(X = 2) = P
and P(X = I - b) = q, where 0 < b < 1. Then
EU(ZI (w)) = pU(1 + w) + qU(l - bw) = f(w)
f'(w) = pU'(l + w) - bqU'(l - bw)
and the maximum is unique and located as before.
If f '()
0
h
"\
U'( 1 - awl
~
d'
b
w =
we ave
1\ = U'( I + w) = aq an glven w =
,
0< b < 1, we can choose p with 0 < p < I such that A = L. Then
aq
as before we find V'(l - ab) = -yU'(l - ab) and since a and b can be
any numbers such that 0 < a, b < 1, then V'(t) = -yU'(t) (0 < t < 1)
V'(l + b)
where -y = U'(l + b)' But -y was shown to be 0:.
Thus V(t) = o:U(t) + 6 (0 < t < 1). Also V(l) = o:U(l) + E. Hence
V(t) - o:U(t) = f3 if t> 1, 6 if t < 1 and
E if t = 1. But V(t)-
- o:U(t) is continuous so f3 = 6 = € so
V(t) = o:U(t) +~. Thus U and
- 816 -
--- page 558 ---

Concave Utilities are Distinguished by Their Optimal Strategies
529
V are equivalent under the assumption that they have the same optimal
strategies for all one period investment settings containing only (cash and)
a two-valued random investment. The logical contrapositive assertion is the
Theorem. This completes the proof. The Corollary follows a fortiori.
Note that a single investment setting of the type in the proof will not
in general distinguish inequivalent utility functions. For instance, if E(X) ~
~ 0 then w = 0 is the unique optimal strategy for all the utilities of
Theorem I (more generally, for all strictly concave utilities, as defined below) so such X distinguish between none of these utilities. It may be of
interest to characterize each investment setting by the pairs of utility functions it distinguishes between or "separates", and to similarly characterize
collections of investment settings.
For a security X, let m(X) and M(X) be the greatest and least
numbers, respectively, such that P(m(X) ~ X ~ M(X)) = 1. Then for a
collection C of investment settings whose securities are {Xa: a E A },
where A is some index set, let m A = inf {m(X a): a E A} and M A =
= sup {M(Xa ): a E A}. Evidently, if U(t) = V(t) for mA ~ t ~ M A , the
collection C will not separate U and
V. Thus a collection with m A =
= 0 and M A = 00 will be needed in general to prove the conclusion of
Theorem 1.
Next we generalize Theorem I to concave non-decreasing utilities defined on (0, 00). We do not make the common assumption that first or
even second derivatives exist. A function ! is concave on an interval I
if for each pair of points xl*- X 2 in I and each number s with
O<S< 1, then !(sx 1 + (1-s)x2)~sflxl)+ (l-s)flx 2)· If flsx 1 +
+ (l - s)x 2) > sflx 1) + (1 - s)flx 2) always, then ! is strictly concave.
(We use "concave" to mean "concave from below".)
The more general definition includes such computationally and empirically natural functions as the "polygonal" utilities. In these, the utility is
a sequence of linear segments. The vertices are such that the function lies
on or below each segment extended, and the ordinates of the vertices increase as the abscissas increase.
- 817 -
--- page 559 ---

530
E. Thorp and R. Whitley
First, recall some facts from the elementary theory of concave functions. (Most texts give results for convex functions. But I is concave exactly when -I is convex so the theories of concave and convex functions
are equivalent.) A concave function is either continuous in the interior of
its domain or non-measurable. An increasing function is always measurable
so our utilities are continuous. A continuous concave function I defined
on an open interval has a left derivative f~ and a right derivative I~
defined everywhere. (If the left endpoint a is includ~d in the interval of
definition, then f~ (a) is not defined and f~ (a) mayor may not be defined. Similarly, if the right endpoint b is included in the interval of definition, then I~ (b) is not defined and I~ (b) mayor may not be defined.) Furthermore,
I~ (t) ~ I~ (t) for all
t except the endpoints in
the domain of I and whenever t 1 < t 2 then I~ (t 1 ) ~ f~ (t 2) and
I: (tl) ~ I: (t2)· There are at most countably many points where I~ (t) >
> I~ (t); otherwise f~ (t) = I~ (t) = f'(t) and I is differentiable. Proofs
of these assertions and further theorems on concave functions are given for
instance in H a r d y, Lit tIe woo d, Pol y a [3].
Theorem 3. Let U and V be concave utilities defined on (0,00),
one of which is strictly increasing on (0, 1 + e) for some e> 0. If U
and V are inequivalent then there is a one period investment setting such
that the sets of optimal strategies lor U and for V are distinct. The investment setting may be chosen to consist only of cash and a two-valued
random investment. If U and V are each strictly concave on the same
one of the sets (0, Zo] or [Zo' (0), then the optimal strategies are unique
and U and V therefore have distinct optimal strategies.
Proof. We proceed as in the proof of Theorem 1 until we obtain
equiation (2.1).
Note that f is concave and that if U is strictly concave on either
(0, I] or [I, (0) then I is strictly concave. Now f(w) is a continuous
function defined on the closed bounded set {w: 0 ~ w ~ I} hence f
has an absolute maximum. Let w* be a pOint where f attains its maximum. It follows from the continuity of f that the set of all such w*
is closed.
- 818 -
--- page 560 ---

Concave Utilities are Distinguished by Their Optimal Strategies
531
From the concavity of f, the set of points w* where f attains its
maximum is also convex, hence it is a closed interval in [0, 1]. If f is
strictly concave the maximum is unique.
For any w* with ° < w* < l, f is a maximum if and only if
f~ (w*) ~ °
~ f~ (w*). A maximum occurs at w* = ° if and only if
f~ (0) :s:;;; 0. A maximum occurs at w* = I if and only if f~ (I) ~ 0. If
the maxima occur on an interval [a, b] with o:s:;;; a < b:S:;;; 1, then
f~ (a) ~ ° and f~ (a) = 0, f~ (b) = ° and
f~{b):S:;;; 0, and ['(w*) exists and is zero for a < w* < b.
Equation (2.1) yields
f~ (w) = apU~ (1 + aw) -
bqU~ (l - bw) ~
(2.2)
~ apU~ (l + aw) -
bqU~ (l - bw) = f~ (w) .
Since
U~ (t) and
U~ (t) are non-increasing as t increases, it follows
from equation (2.2) that f~ (w) and f~ (w) are non-increasing as w increases.
Let c be such that 0 < c < band U/(l -
c) and V'(l - c) are
defined. This is possible because U' and V' are both defined except at
countably many points hence there are uncountably many points in (0, 1)
where both U' and V' exist. With a and b already given, choose
w = %. Consider now the case where
U~ (1 + a:) > 0. Then we may
choose p with 0 < p < 1 in equation (2.2) so that f~ (%) = 0. This
means f~ ( %) :s:;;; 0 and since w = % is not an endpoint of [0, 1 J this
means f attains its maximum at %, thus % is optimal for U in the
given investment setting.
I
e
.
t'
Since U and V have the same optima strategies, w = b
IS op 1-
mal for
V hence
V attains its maximum there so for w = %,
g~ (w) = apV~ (1 + aw) -
bqV~ (l - bw) ~ ° and
apV~ (1 + aw)-
- 819-
--- page 561 ---

532
E. Thorp and R. Whitley
- bq V~ (l - bw) = g~ (w) ~ O.
Note that
g~ (%) ~ 0
and the fact
V~ (1 - e) > 0 implies that
V~ ( 1 + at) > O. We may show similarly
that if
V~ ( 1 + ~) > 0 then U~ ( 1 + ~) > O. Since a is chosen independently of band e
this means that for each t> 1,
U~ (t) > 0
if and only if
V~ (t) > O. But this is readily shown to be equivalent to
the statement that (t: U(t) = sup U(t)} = (t: V(t) = sup V(t)}, i.e. that
if either U or V become horizontal for t ~ e > 1 then they both become horizontal for t ~ e> 1. For t> e, we have of course U'(t) =
= V'(t) = O. For t < e, the argument continues as follows.
From f' (w) = 0, apU~ (1 + ~) = bqU'(l - e), noting that
U' ( 1 + ae)
-
b!!!J..
'
U~ (l - e) = U'(l - e). Thus
U'(l _ e)
= ap' From g_ (w) ~ 0, it
. .
V~ (1 + 1f)!!!J..
.
V'(l - e)
follows slIllilarly that
V'( 1 _ e)
~ ap' Lettmg a = U'( 1 _ e) yields
V~ ( 1 + ~) ~ aU~ ( 1 + at). Since the choices of band e were independent of that a, the result holds for all a> 0, therefore
V~ (t) ~
~ aU~ (t) for all t > 1.
A similar argument shows that V: (t) ~ aU: (t) for all t> 1. Thus,
except for at most countably many points, V'(t) = aU'(t) for t> I.
Now U and V are readily shown to be absolutely continuous on any
closed subinterval of (I, 00), as a consequence of the fact they are continuous, concave, and non-decreasing, thus V - aU is absolutely continuous. The absolute continuity of U - aV and the fact that (V - aU)' =
= 0
almost everywhere implies that
V - aU = (3,
a constant
(Goffman [2], p. 242, Prop. 12).
A similar argument shows that Vet) = aU(t) + "Y for t < 1. The
role of 2 in the proof of Theorem I is played by any number e such
that 1 < e < e and U'(e) and V'(e) are both defined. One then shows
as in the proof of Theorem I that V(i1'= aU(t) + {3 for 0 < t < 00. We
- 820-
--- page 562 ---

Concave Utilities are Distinguished by Their Optimal Strategies
533
have established the contrapositive assertion as in the proof of Theorem I.
This completes the proof.
The hypothesis that either U or V (hence both, from the proof)
is strictly increasing for a positive distance to the right of 1 is required.
If instead U and V are merely concave and non-decreasing, the conclusion of Theorem 3 need not hold. For instance, let U(t) = V(t) = 0 if
t ~ d , where 0 < d ~ 1. Let U(t) and J]t)each be extended to
(0, d) so that they are continuous, concave, and strictly increasing on
(0, d). Then all such utilities have the same optimal strategies, yet many
pairs are inequivalent.
To obtain an inequivalent pair, let UU) = t - d if 0 < t < d and
let V(t) = - (t - d)2. If for some constants a and 13, V(t) = exUU) + 13
then V'(t) = exU'(t). But V'(t) = - 2(t - d) ~ ex = exU'(t).
To see that all such utilities U have the same optimal strategies, note
that W = (wI' ... , wk ) is optimal for the investment setting (Xl""
... , Xk ) if and only if P (~ wiXi ~ d) = I, in which case E U(ZI (W» =
I
= O. If instead P Cf WjXi < d) > 0 then for some e> 0, P (t: WjXj ,
:s;;; d - e) = 0> O. Then EU(ZI (W»:s;;; oU(d - e) < 0 so W is not optimal.
3. OTHER SEPARATING FAMILIES
We next establish the conclusion of Theorem 1 using investment settings with n points in their range. We detennine the effect of varying the
payoffs (xl"' " xn) and their probabilities (PI"'" Pn ) separately.
One surprising conclusion (part (b» can be stated in tenns of an example.
Suppose X consists of betting on a wheel of fortune divided into red,
white and blue sectors, with payoffs of ~,1, and ~ respectively. Then
if U and V are inequivalent on [i, ~] the areas of the sectors may
be chosen so U and V have distinct optimal strategies. But if the wheel
is divided into just red and blue sectors, with payoffs of ~ and 1, then
- 821 -
--- page 563 ---

534
E. Thorp and R. Whitley
there are two inequivalent utilities on [~, ~] :which have the same optimal strategies for every choice of areas for the two sectors.
Theorem 4. Suppose U and V are increasing strictly concave utilities on (0,00). Let X be a random variable with outcomes °
~ x 1 ~
~ X2 ~ ... ~ xn with xl < 1 and xn > 1. Suppose P(X = xi) = Pi> 0,
n
2' p. = l.
i= 1
I
(a) Let n and the Pi be given. If U and V have the same optimal strategies for each X (t.e.
Xl"
" 'Xn vary), then U and V are
equivalent.
(b) Let n and the xi be given. Suppose U' and V' exist and
are continuous at 1. If U and V have the same optimal strategies for
each X (t.e. PI"" 'Pn vary) and at least three xi are unequal to 1,
then U and V are equivalent on [ZOxl,ZOxnJ. If exactly two of the
x/ s are unequal to one, there are utilities U and V which are not equivalent on [ZOX l' ZOxn], but which have the same optimal strategy for
each X.
Proof. Assume Zo = 1. Let R = X-I and
Yj = Xj -
1. Then investing w in X gives an expected return (with respect to U) of
n
E(U(wR + 1»)::= Z p.U(wr. + O. Each function U(wr. + 1) is differeni= 1
I
I
I
tiab1e except at a countable set Cj of points, so except for w in the
countable set C1 U ... U Cn the expectation E( U(wR + 1)) is differenn
tiable at w with dE(UC;R + 1) = L; p.,.U'(wr. + 1). Similarly each
w
i= Itt
I
function V(wr. + 1) is differentiable except at a countable set. Thus, ext
cept at a countable set D of points in [0,00] both E(U(wR + 1)) and
E( V(wR + I»
are differentiable functions of w.
They are also strictly
concave functions of w.
For part (a) let PI"'" Pn be given and choose Wo in (0, 1) - D.
Consider the vectors ~ = (U/(wO'l + I), ... , U'(worn + 1)) and
{3 =
= (V'(wOrl + 1), ... , V'(worn + 1». Suppose that the non-zero vector
- 822-
--- page 564 ---

Concave Utilities are Distinguished by Their Optimal Strategies
535
'Y = (C I' C2 ' . .. , cn )
is perpendicular to a,
i.e., the inner product
(a, 'Y) = O. Choose
C.
,. =
I
I
Pi { f itt I
ci I}
with € = max
1 ~ i ~ n .
p/
Since each component of a is positive, some ct > 0 and some cj < 0,
hence some x . > 1 and some x. < 1. Also ,. + 1 = x. > 0 Then
I
J
I
I
'
dE(U(wR + 1» I
~,
.
dw
Iw:wo = i~ P;'jU (wO't + 1) = 0 and E(U(wR + 1)
has a maximum at wOo By hypothesis E(V(wR + 1» has a maximum
at w 0
and, since it is differentiable there,
dEC V(;R + 1,» I
=
w
w=wo
n
= .Z P;'i V'(wO'j + 1) = 0 Le., ({3, 'Y) = O. Hence the set of vectors per-
I == I
pendicular to a is also perpendicular to {3 which implies that {3 = aa.
Since the components of a and (3 are non-negative, a ~ O. Equating
components
(3.1)
U'(wor. + 1) = aV'(wor. + 1)
I .
I
where a is a non-negative function of '1, . . . ,'n ~nd wOo Since U
and V are strictly concave there is a point to not in D, Wo < to < 1,
with V'(to) > 0 and U'(to) > O. Choose '1 so that wOrt + 1 = to'
choose '2 > 0 with t = wor 2 + 1 not in D , and choose '3 < ... < rn
so they are not in D. Then
U'(to) = a('l"'" rn , wo)V'(to) and
,
,
U'(to)
.
U (w2'2 + 1) = aC'I' ... ,'n' wo) V (wO'2 + 1). Thus a = V'Uo) > 0
IS
constant. So
V'(t) = aU'(t) for any t> 1 not in D. Since V and U
are absolutely continuous on any closed subinterval, Vet) = aU(t) + b
for all t> 1. A similar argument shows that V(t) = cU(t) + d for t < 1
V '(to)
with
C = YI'(t ) = a. The equivalence of U and V now follows (as in
o
the proof of Theorem 1) from their continuity.
For part (b) suppose that the Xi are given, with 0 < xl < X 2 < ...
. . . < Xp ~ 1 ~ xp + 1 < .. . < x n . We proceed as before, but now consider,
for 0 < Wo < 1 and U, V differentiable at WO'j + 1, 1 ~ j ~ n,
the
- 823 -
--- page 565 ---

536
E. Thorp and R. Whitley
vectors a = ('1 U'(wO'1 + 1), ... ,'n U'(WO'n + 1»
and
'if =
= ('1 V'(WO'l + 1), .. ·"n V'(WO'n + 1». Since a has both positive and
negative components there is a vector (dl , d2 , ••• , dn) perpendicular to
....,
d.
~
a with each dt > 1. Choose Pt =
n I
thus Pi> 0 and
£..J P; = 1,
Zd
I
;= 1
j
and define X by P(X = xI) = PI. Thus
= dE(U(wR + 1)) I
dw
w=wo
.
dE(U(wR+ 1))1
@,(dl,···,dn))
By hypotheSls
dw
w=wo =
v
= 0 so
t dl
('P, (dt ,· •. , dn») = o. Suppose that :y = (e1 , e2 , • •• , en) is perpendicuel + dod;
lar to a. Let do > max I el I and choose PI = "
Note that
n
P, > 0 and Z P, = 1. Thus
1= 1
,~ e, + dod,
n
dE(U(wR + 1)) I
= ~ P [, U'(w , + 1)]
dw
w = w 0
1= 1
I I
0 I
n
and letting D = Z (el + dod,.) gives
1= 1
DI i e.,.U'(wo' · + 1) + DI do Z d,·'IU'(wO'j + 1) =
1= 1
I I
I
j
1 ....,....,
1
....,
= D (a, "Y) + D do(a,(d1,·· · ,dn ))= o.
- 824 -
--- page 566 ---

Concave Utilities are Distinguished by Their Optimal Strategies
537
Hence, dE(V(;R + 1» I
= O. Th·
. Id
(R -)
d '"
W
w=wo
IS Yle s
,.,I'Y + 0(/3, (dl , ...
. . . , dn» = (ii, -:y) = O. Thus
(3/2)
U'(wO'i + 1) = a(pl' Pz' ... , Pn' wo) V'(wo'; + 1)
(1 ~ i ~ n) .
For W in (0, I) with U, V differentiable at W't + I (1 ~ i ~ n) we
have (3.2) with Wo = w. Consider the quotient
U'(w,; -Fl)
(3.3)
h( w) = a(p (, . . .. , P n' w) = V' (w,. + I)
(l <; i ~ n) .
,
First look at the case where at least three x;'s are unequal to one. Suppose that x I < I < xn _ I < xn; the proof where two or more points fall
to the left of I is similar.
Let 'P;<w) = w'; + 1. The countable collection of functions
{u V U 0 .f')- 1
V 0 .f')- 1
U 0 .f')-l 0
.f')
0 .f')-l
V 0 .f')-l 0 If)
0 .f)- 1
"
Tn'
Tn'
Tn
Tn - 1
Tn'
Tn
Tn - 1
Tn
'
U 0 If')- 1 0 .f)
0 .f')- 1 0 .f)
0 If')- 1
V 0 .f')- 1 0
.f')
0 .f')- I 0 .f')
0
Tn
Tn - 1
Tn
Tn - I
Tn'
Tn
Tn - 1
Tn
Tn - 1
o 'P; I , ... } is simultaneously differentiable except at a countable set of
points Do in (0, 1).
Choose tin (l,xn)-D O and write t=wI'n + 1, so wI =
= 'P; 1 (t), and set t I = WI'n _ I + I = 'Pn _ 1 ['P; I (t)]. We can also write
tl = w 2'n + I; w2 = 'P;l(tl)· By (3.3) we have h(wl ) = h(w2 ), since
U and V are differentiable at WI and wz. Note that w 2 < wI' in
'n
1
fact, w2 = AWl with A = ---. Setting t2 = W 2'n -1 + I = 'Pn _ 1 (w 2 ),
'n
t2 = W3 'n + I and w3 = 'P; 1 (t2). Then h(w2 ) = h(w3 ) since U and
V are differentiable at Wz = 'P; 1 0 'Pn _ 1 0 'P; 1 (t) and at W3 = 'P; 1 0
o 'Pn _ 1 0 'P; 1 0 'Pn _ 1 0 'P; 1 (t). Continuing inductively t, = w/n -.1 + I =
= Wj + 1 'n + I and wj+ 1 = AWr Iterating this equation wj+ 1 = X'W I ~ °
as j ~ 00, thus h( wI) = ... = h( W n ) ~ h(l) since U' and V' are continuous at I. Hence the equation ~:~~~ = h( 1) holds except for countably many t in (1, xn) and thus, since U and V are absolutely continuous on any closed subinterval,
U(t) = h(l) Vet) + c for all t in [l, x n)·
- 825 -
--- page 567 ---

538
E. Thorp and R. Whitley
Let t belong to (x l' 1) with U and V differentiable at wr. + 1,
.
U'(t)
I
and from equatIon (3.3)
V'(t) =
1 ~ f ~ n.
Then
t = w'l + 1
U'(wrn + 1)
= V'(w, + 1) = h(l). Since U and V are absolutely continuous on
n
closed subintervals of (x l ' I), U(t) = h(l) V(t) + d. The continuity of
U and V at I implies that c = d and thus U and V are equivalent
on [Xl' xn ]·
To complete the proof we must consider the case where there are only two x/s distinct from one, say, ° < x I < 1 < X 2' Let go be any
non-constant positive function on [I, X 2] with a continuous derivative
which is zero at 1. Define g on [Xl' 1] by g(w'l + 1)=g(w'2 + 1)
for °
~ w ~ 1. Choose a so that
max
I g'(t) I - a·
min
19(t)1 <
xI~t~x2
xl~t~x2
t
1
- at
t
< ° and define UU) = f eat dt = - e
and VCt) = f eat g(t)dt.
o
a
0
Because U"U) = - aeat < ° and V"(t) = eat (g'(t) - ag(t» < 0,
U
and V are strictly concave. Also U'(t) = eat and V'(t) = eat g(t) are
positive so U and V are strictly increasing. Clearly U and V are not
equivalent on [xl' x 2 ].
For these two functions U and V and ° < w < 1,
dEC V(wR + 1»
V'
V'(
1 -
dw
= 'IP I
(w'l + 1) + '2P2
w'2 + )-
= 'IPtg(w'l + I)U'(w'l + 1) + '2P2g(w'2 + I)U'(wr2 + 1)=
_ g(
+ 1) dE(U(wR + 1»
-
w'l
dw
Hence dECUC;~ + 1» = ° if and only if dEC V(;~ + 1» = 0, and so
w ,(0 < Wo < 1), is an optimal strategy for U (with respect to X) if
o
.
.
dE(U(wR + 1»
and only if it is an optimal strategy for V. If the denvatIve
dw
is never 0, the equation above shows that it has the same sign as
dEC V(wR + 1» . so ° (or 1) is an optimal strategy for U if and only
dw
'
- 826 -
--- page 568 ---

Concave Utilities are Distinguished by Their Optimal Strategies
539
if it is an optimal strategy for V.
We have seen that U and V are two utilities on [xl' X2 J which
are not equivalent, but which have the same optimal strategies for all random variables with outcomes Xl and x 2 .
Remark. Our proofs may be modified readily to prove the theorems
when V and V are defined on the closed interval [0, (0) and also when
the interval is (c, (0) or [c, (0), with c < ZOo P:resumably c> O. (Alternately, the [c, 00) result implies the (c, (0) result: if V(x) = V(x) on
every interval [c+€,oo) (O<€<Zo-c) then V(x) = Vex) on (c,oo).)
4. QUESTIONS FOR FURTHER INVESTIGATION
F r i e d man -
S a vag e [1 J and Mar k 0 w it z [4] have shown
that utilities which are not everywhere concave are of interest. This leads
us to a question which we have not been able to answer yet:
Is the class of utilities which are continuous and strictly increasing
(and differentiable everywhere, bounded, and even strictly positive derivative, if you like) distinguished by their optimal strategies?
In the real world factors such as human error, the discreteness of assets and monetary units, etc. make it in general not possible to choose the
optimal allocation W* = (wr, ... ,w;). The continuity of the utility in
conjunction with boundedness of the attainable utilities implies that "sufficiently small" deviations from W* will ensure that the realized utility
is "close" to the optimum.
One feels as well that in the real world, the exact values of the utility
function should not be critical. In other words, if two utility functions are
somehow "close," the consequences of choosing one rather than the other
should be "close."
What should it mean for two utility functions to be "close? " First,
observe that we must define closeness not for functions, but for equivalence
classes of functions. Let U be a utility. The equivalence class of V, written [VJ, is the set {V: V = aU + {3, ex> O}. For the class {3 of bounded
- 827 -
--- page 569 ---

540
E. Thorp and R. Whitley
utilities, I.e., Me U) == sup VU) < 00, m( U) == inf VU) > -
00, we suggest
h
h
V
.
""
V-M
t at eac
[ ] eqUIvalence class be represented by V = M
+ 1.
-m
Note that M( iJ) = 1 and m( iJ) = O.
Then the "closeness" of V and
V, i.e., of [UJ and [V], is defined to be sup [V(t) -
V(t)l and written
either d( U, V) or d([ UJ, [V]) or d( V, V).
We now show that U and V can be "close" yet the optimal strategies for U and V need not be. For n~ 2, let Vn and V n be defined as follows:
V (t) = ~
- 1 if 0 < t ~ 1 + 1. and 1 if t > 1 + 1. .
n
n+l
n
n'
~
2n - I.
1
Y n (t) = n + 1 t - 1 If 0 <. t <. 1 + n '
t : ~ 13 if 1 + ~ < t <. 2, and 1 if t> 2 .
Then d( Un' Vn) =~. Now choose an investment setting consisting
only of cash and the security X, fihere P(X = 1 - E) = q, P(X = 1 + a) =
1
~
= p, 11 < a < 1, and 0 < E, p, q < 1. Assume Zo = 1. A calculation
(2n-l)(n-l)
shows that if ap > q€
n + 1
,then the unique optimal strategy
for V
is w* = _1 and for V
the unique optimal strategy is w* = 1.
n
an
n
Thus for any
f> > 0 we can construct sequences Un
and Vn such
tha t d( V , V ) ~ 0 as n ~ 00 and I w * (V ) - wit (V ) I ~ I -
f>, where
n
n
n
n
w* (iJ) means an optimal strategy for V.
Even though a small "error" in the utility function can lead to a large
change in optimal strategy, it can only lead to a small change in consequences, in the following sense. (We use the abbreviation
V(W) for
EU(Zo ~ wiXi ).
Thus for each
W, U(W)
is a number and
I
U(Zo Z w.X.) is a random variable.)
i
I
I
-
828 -
--- page 570 ---

Concave Utilities are Distinguished by Their Optimal Strategies
541
Lemma. If d( U, V) is" small," then U(W*( V») == U(W*( V)) and
V(W*( U)) == V(W*( V)), ie., if U and V are" close," an optimal strategy for one is "nearly optima!' for the other.
Proof. Let d( U, V) ~ € so V( t) + € ~ U(t). Then for any allocation W, V(Zo ZZ" wtXi ) + € ~ U(Zo ~
wiXi ) and E (V(Zo ~ wiX,) +
z
z
+ €) = E (V(Zo ~ wjX,)) + € ~ EU(Zo ~WiXi), or V(W) + € ~ U(W).
"""
-.,
I
"J
-.,
Interchanging U and V in the argument yields U(W) + € ~ V(W) so
I U(W) - V(W) I ~ €. The choices for W of W*( V) and W*( V) yield
the conclusion of the lemma.
The lemma and the example show us what may happen if we replace
a U by a nearby V which may have more desirable properties, such as
differentiability (of various orders), strictly increasing, etc.: The optimal
strategies may change drastically but the maximum utility over all strategies changes only slightly.
Note added in proof: The authors have since extended the central result of the paper, Theorem 3, as follows.
Theorem. Let U and V be continuous non-decreasing functions
defined on an arbitrary interval I of the real line. Then if U and V
are inequivalent, there is a one-period two security investment setting such
that U and V have distinct optimal strategies if either (a) U and V
are in the class of all functions which are either concave or convex, or
(b) U and V are in the class of all functions with a second derivative
which exists and is continuous, except perhaps for a set of isolated points.
Thus the Theorem includes the utility functions generally encountered.
- 829-
--- page 571 ---

542
E. Thorp and R. Whitley
REFERENCES
[1] M. F r i e d man -
L. J. S a v ag e, The Utility Analysis of Choices
Involving Risk, Journal of Political Economy, 56 (1948), 279-304.
[2] C. Go ffm an, Real Functions, Holt, Rinehart and Winston Inc.,
New York, 1953.
[3] G. Hardy -
J . Littlewood
.~ G. Polya, Inequalities,
Cambridge University Press, 1959.
[4] H. Markowitz, The Utility of Wealth, Journal of Political Economy, (1952), 151-158.
[5] J. M 0 s si n, Optimal Multiperiod Portfolio Policies, Journal of Business, (April 1968) .
. [6] P. A. Sam u e 1 son, The 'Fallacy' of Maximizing the Geometric
Mean in Long Sequences of Investing or Gambling, unpublished preliminary preprint, 1971.
[7] E. O. Tho r p, Optimal Gambling Systems for Favorable Games,
Review of the International Statistical Institute, 37 (1969), 273-293.
- 830-
