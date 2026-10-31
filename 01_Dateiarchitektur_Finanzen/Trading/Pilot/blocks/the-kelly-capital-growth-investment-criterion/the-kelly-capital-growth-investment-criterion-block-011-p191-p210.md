# The Kelly capital growth investment criterion _ theory and -- Leonard C_ Maclean, Edward O_ Thorp, W_ T_ Ziemba, Leonard -- World Scientific Handbook -- isbn13 9781283148344 -- bec576e26410d0c695fd5b867d08ec4f -- An.pdf — pages 191–210

--- page 191 ---

164
P H Algael and T. M Cover
LOG-OPTIMUM INVESTMENT
883
maximum expected log return can be expressed as the sum
(24)
w*(P) = r(P) + w*(Q), where w*(Q) = supEQ{log(b, U)}.
bE f$
Maximizing w( b, P) or w( b, Q) are equivalent operations, so that B*( P) =
B*(Q). Notice that w*(Q) = w*(P) - reP) ~ 0, with equality iff the reference
portfolio {3 is log-optimum.
It is an interesting fact that the maximum expected log return w*(Q) is
always attained by some portfolio choice. However, we need a stronger result,
namely, the existence of log-optimum portfolios b*(Q) that depend measurably
on Q. To prove the existence of a measurable selection of log-optimum portfolios,
we make use of topological properties, including compactness of !2 and upper
semicontinuity of the expected log return web, Q) = EQ{log(b, U)} in (b, Q).
The space 2 of probability measures on the compact metric space i¥f is
compact and metrizable when equipped with the weak topology [that is the
weakest topology on 2 such that Q ~ EQ{f(U)} is continuous in Q E 2 for all
bounded continuous functions f: i¥f ~ .?l). Its Borel a-field is the smallest a-field
on 2 such that A ~ Q(A) is measurable in Q for all Borel subsets A ~ i¥f.
THEOREM 2.
The maximum expect log return w*(Q) = sUPbE YtEQ{log(b, U)}
is convex, bounded [between 0 and max/-log f31)] and uniformly continuous
when the space 2 of probability measures on i¥f is equipped with the weak
topology. The set of log-optimum portfolios B *( Q) is a nonempty compact convex
subset of !2 for every distribution Q on i¥f, and a log-optimum portfolio b*(Q) E
B*(Q) can be selected for each Q E 2 so that b*(Q) is measurable in Q.
PROOF. Clearly w*(Q) is convex in Q for the same reason that w*(P) is
convex in P . We argue that w*(Q) is bounded below and lower semicontinuous
on 2, because ({3, u) is bounded below on i¥f and (b, u) is concave in bE !2 and
lower semicontinuous in u E i¥f. We also prove that w( b, Q) is bounded above
and upper semicontinuous, using compactness of !2 and boundedness above and
upper semicontinuity of (b, u) on !2 X i¥f. Boundedness and uniform continuity
of w*(Q) and existence of a measurable selection of log-optimum portfolios
b*(Q) will follow automatically.
First, we argue that w*(Q) is nonnegative and lower semicontinuous on 2.
For 0 ~ A ~ 1 and bE !2, let X = 1 - A, b>-. = X{3 + Ab, !2>-. = {b>-.: bE !2} and
(25)
wx(Q) = sup EQ{log(b,U)} = supEQ{log(b>-.,U)} .
bE f$~
bE f$
Observe that wx(Q) is monotonically increasing in A, since the supremum is
taken over a larger set !2 >-. as A increases. Furthermore, !2 1 = !2, !2 0 = {{3} and
({3, u) = 1 for all u E i¥f, so that
w*( Q) = wt( Q) ~ wx( Q) ~ wo*( Q) = EQ{log({3, U)} = o.
If A < 1, then loge b>-., u) is bounded below (by log X) and lower semicontinuous
in u, so that w(b>-., Q) = EQ{log(b>-., U)} and wx(Q) = SUPbE YtW(b>-., Q) are
lower semicontinuous in Q. On the other hand, the inequality (b>-., u) ~ A(b, u)
--- page 192 ---

Asymptotic Optimality and Asymptotic Equipartition Properties of Log-Optimum Investment
165
884
P. H. ALGOET AND T. M. COVER
implies that
w>.* ( Q) ::; w* ( Q) ::; w: ( Q) - log A,
and hence w>.*(Q).l' w*(Q) as A.l' 1. Since w*(Q) is the supremum of lower
semicontinuous functions w:(Q), it follows that w*(Q) is lower semicontinuous
as well.
The expected log return w( b, Q) = EQ{log( b, U)} is bounded above and upper
semicontinuous on 86 X 2, since (b, u) is bounded and upper semicontinuous on
86 X CiJ/. Since 86 is compact, it follows [ef. Bertsekas and Shreve (1978), Proposition 7.33] that w*( Q) = SUPb E &Bw( b, Q) is bounded above and upper semicontinuous on 2 . Furthermore, log-optimum portfolios b*(Q) E B*(Q) can be
selected in a measurable fashion for all Q E 2 by the measurable selection
theorem of Kuratowski and Ryll-Nardzewski (1961). The upper bound w*(Q) ::;
max/-log,8i) holds since (b,u)::; LiUi ::; maxi(l/,8i) for all bE86 if u
satisfies (,8, u) = 1. 0
It is impossible to select a portfolio b*(Q) E B*(Q) for all distributions Q on
CiJ/ so that b*(Q) is continuous in Q. However, if Qn -+ Qoo and b: E B*(Qn) for
all n, then any accumulation point b:' of the sequence {b:} is a point in
B*(Qoo)' Furthermore, (b:, U) -+ (b:', U) almost surely under Qoo' These continuity properties of the multivalued correspondence Q ~ B*(Q) follow from the
following.
THEOREM 3. The set Gr(B*) = {(Q, b*): b* E B*(Q)} is closed in 2 X 86.
Consequently, any selection of log-optimum portfolios Q ~ b*(Q) E B*(Q) is
continuous at any Q E 2 such that B*(Q) = {b*(Q)} is a singleton set.
PROOF. Since 86 is compact, the theorem will follow from the following
claim: If Qn -+ Qoo in 2, b: -+ b:' in 86 and b: E B*(Qn) for all n, then
b:, E B*(Qoo)'
To prove the claim we consider the sequence of maximum expected log returns
w*(Qn) = w(b:, Qn). It is clear that w*(Qn) -+ w*(Qoo) since Qn -+ Qoo in 2
and w*(Q) is continuous in Q. On the other hand (see the proof of Theorem 2),
w( b, Q) is upper semicontinuous on 86 X 2 and hence
limsupw(b:,Qn)::; w(limb:, limQn) = w(b:' , Qoo)'
n
n
n
The claim b:' E B*(Qoo) and Theorem 3 follow, since
w(b:',Qoo ) ~ limsupw(b:,Qn) = limw*(Qn) = w*(Qoo) = supw(b,Qoo)'
0
n
n
b
The maximum expected log return w*( P) is neither bounded nor continuous
(for the weak topology) as P ranges over the space of probability measures on
!Je';:. But if the support of P is constrained to a closed subset f
of !Je';:, then
w*(P) is lower semicontinuous and bounded below iff f
is bounded away from
0, upper semicontinuous and bounded above iff f
is bounded, and bounded and
--- page 193 ---

166
P H Algael and T. M Cover
LOG-OPTIMUM INVESTMENT
885
uniformly continuous iff f
is bounded away from o. In particular, if f = 01/ (i.e.,
if X is distributed on the simplex 01/), then P = Q and w*(P) = w*(Q) is
bounded and continuous.
Some of the conclusions of Theorems 2 and 3 continue to hold if the investor
may distribute his funds over a countable set or even a separable metrizable
space d of investment opportunities. Indeed, suppose every realization of the
return X is a nonnegative lower semi continuous function x( a) on d. (This is no
restriction if d
is a countable set with the discrete topology.) The average
return (b, x) = L.-x( a )b( cia) is then well defined for every portfolio b [i.e., for
every normalized measure b( cia) on the Borel a-field of d]. Further assume the
existence of a reference portfolio {1 such that ({1, x) > 0 is strictly positive for
any return function x( a) that is not identically o. [Such {1 exists if d is locally
compact, and, in particular, if d is countable.] If P and Q denote the distribution of X and U = X / ({1, X), then the maximum expected log return w*(P)
admits the decomposition r(P) + w*(Q), and w*(Q) is nonnegative and lower
semicontinuous by the argument presented in the proof of Theorem 2. If,
moreover, d
is compact and the return functions x( a) are continuous and
bounded by a fixed constant, then w*(Q) is bounded and continuous and a
measurable selection of log-optimum portfolios b*(Q) exists by Theorem 2, and
Gr( B*) is closed by Theorem 3.
4. Martingale properties. It will be shown that the maximum expected log
return given increasing information fields tends to the maximum expected log
return given the limiti~g a-field. We assume that the random return vector
X( w) E !1f';' is defined on a perfect probability space (Q, $", P), so that X admits
a regular conditional probability distribution given any sub-a-field of $". See
Jifina (1954) for a proof of this fact, and Ramachandran (1979) for a complete
discussion of perfect measures.
THEOREM 4. Suppose the random vector X is defined on a perfect probability
space (Q, $", P), and {~}o < t < 00 is an increasing sequence of sub-a-fields of $"
with limiting a-field ~oo ~ ff.
(a) If Pt is a regular conditional probability distribution of X given ~, then
(26)
Pt -+ Poo
weaklya.s.
(b) If b*( ·) is a measurable selector of log-optimum portfolios, then be* =
b*( Pt) is an ~-measurable portfolio attaining the maximum conditional expected log return given ~ . Moreover, (be*, X) -+ (b~, X) a.s., and hence
(27)
log(be* , X) -+ log(b~, X)
a.s.
If the log-optimum portfolio given ~oo is unique [B*(Poo) = {b;;}], then be* -+ b;;
a.s. as weU.
(c) If w*(·) denotes the maximum expected log return function , then the
maximum conditional expected log return given ~ is given by
(28)
w/ = w*( Pt) = sup E{log( b, X)~} = E{log(be*, X)I~} a.s.
bEff,
--- page 194 ---

Asymptotic Optimality and Asymptotic Equipartition Properties of Log-Optimum Investment
167
886
P. H. ALGOET AND T. M. COVER
Furthermore, {w/, ~}o" t" 00 is a submartingale and
(29)
w/ -
W';
a.s. (and in V it We: < 00).
(d) The maximum expected log return given ~ is given by
(30)
~
* = E {w/} = sup E {log( b, X)} = E (log( be* , X) } .
bEff,
Furthermore,
(31)
~*)" We:, ast- 00.
PROOF.
Levy's martingale convergence theorem for conditional expectations
of a bounded continuous (or nonnegative measurable) function t(x) states that
This proves (a), and assertion (b) follows in view of Theorem 3. Notice that
be* = b*(Pe) and w/ = w*(Pt) are ~-measurable, since Pt is measurable on
(rl, ~) and both b*(·) and w*(·) are measurable functions.
If 0:::; s :::; t:::; 00, then ~ ~~, so that every ~-measurable portfolio (including bs*) is also ~-measurable. It follows that
E{log(bs*, X)I~} :::; w/ = sup E{log( b, X)I~}.
bEff,
Taking
~-conditional expectations proves that ws* = E{log(bs*' X)I~} :::;
E{wt*I~}' and hence {w/, ~}o < t <oo is a submartingale. The maximum expected log returns ~
* = sup b E .?~ E {log( b, X)} ~crease with t since the supremum is taken over larger and larger sets (b E ~ = b E ffe). More information
does not hurt!
It remains to show that ~* )" We: and w/ ~ w'; a.s. (and in V if We: is
finite). For this purpose we choose a reference portfolio {3 (with {3i > 0 for all
1 :::; j :::; m), and we recall the decomposition w*( P) = r( P) + w*( Q) of the
maximum expected log return into a reference level r(P) = Ep{log({3, X)} and a
relative improvement w*(Q) that only depends on the distribution Q of the
scaled return vector U = u(X) = X/({3, X).
Let Qt designate a regular conditional probability distribution of U = u(X)
given
~, for 0:::; t :::; 00. Then Qt -
Qoo
weakly almost surely and
{w*(Qt), ~}o"t<oo is a submartingale. Since w*(Q) is bounded and continuous
in Q, it follows that w*(Qt) -
w*(Qoo) a.s. and in V, and E{w*(Qt)} )"
E{w*(Qoo )}' The sequence {r(Pt), ~}o"t"oo [where r(Pt) = E{log({3, X)~}] is
a martingale [at least if 10g({3, X) has finite expectation], and the martingale
convergence theorem for conditional expectations asserts that
r(Pe) = E{log({3, X)I~} - r(Poo ) = E{log({3, X)iffoo}
a.s.
[and in V if E{log({3, X)} is finite]. Since wt* = r(Pe) + w*(Qt), we may
conclude that {Wt*, ~}o " t< 00 is a submartingale such that w/ ~ w'; a.s. (and in
--- page 195 ---

168
PH Algoet and T M Cover
LOG-OPTIMUM INVESTMENT
887
V if We: is finite). The expectations satisfy
We* = E{log(,B, X)} + E{w*(Qt}} ? We: = E{log(,B, X)} + E{w*(Qoo}}·
o
The main conclusion of Theorem 4 is that no gap exists between lim t i ltV;*
and We: . Thus the limit of the expectations ltV;* = E{log(bt, X)} coincides with
We: = ~{log(b~, X)}, which is the expectation of the limit log(b~, X) =
lim tlog( bt, X).
We have shown that wt --+ w~ a.s. and ltV; * ? Woo*' using boundedness and
continuity of w*(Q). These convergence theorems also hold for a market with
infinitely many investment opportunities, when w*(Q) is only nonnegative and
lower semico~inuous. Indeed, {wt, ~}o ,;; t ,;; 00 is still a submartingale, so that
wt:s; E{w~I~} and limtiE{we*}:s; E{w~} and hence, by Levy's martingale
convergence theorem for conditional expectations,
(32)
limsupwt :s; limE{w~I~} = E{w~l§oo } = w~ a.s.
t
t
Since {w *(Qt), ~}o ,;; t ,;; 00 is a submartingale also, one similarly obtains
limsupw*(Qt} :s; w*(Qoo}
a.s.
(33)
t
and
But Qt --+ Qoo weakly a.s. and w*(Q) is lower semicontinuous in Q, so that
(34)
liminfw*(Qt} ~ w*(Qoo}
a.s.
t
We conclude that w*(Qt) --+ w*(Qoo ) a.s. Since w*(Q) is also nonnegative
Fatou's lemma implies that E{w*(Qt)} ? E{w*(Qoo )}. It follows that wt --+ w~
a.s. and We* ? We:, at least if E{log(,B, Xo)} > - 00 or SUPkE{W*(Qk)} < 00 .
5. The asymptotic optimality principle. We now prove the asymptotic
optimality principle for sequential log-optimum investment. The market is
described by a sequence of return vectors {Xt}o ,;; t <00 defined on a perfect
probability space (12, .%, P), and capital invested according to a portfolio bt at
the beginning of period t will grow by a factor (bt> Xt) when the random
outcome X t is revealed at the end of that period. If the initial fortune is
normalized to So = 1, then the compounded capital Sn after n periods is given by
(35)
Sn = n (bt , Xt)·
O,;; t < n
The objective is to select portfolios bt so as to maximize the capital growth rate
lim inf n n - 1 log Sn. Portfolio bt must be selected on the basis of an information
field ~ that embodies what is known at the beginning of period t. In other
words, bt must be ~-measurable (bt E ~, for short).
Let Fe denote a regular conditional probability distribution of X t given ~,
and let b*(·) be a measurable selector of log-optimum portfolios. Then bt =
--- page 196 ---

Asymptotic Optimality and Asymptotic Equipartition Properties of Log-Optimum Investment
169
888
P. H. ALGOET AND T. M. COVER
b*(Pe) is an ~-measurable portfolio attaining the maximum conditional expected log return
(36)
w/ = w*(Pt) = E{log( bt, Xt)I~} = sup E{log( b, Xt)I~}.
bEff,
The expectation of the log return log( bt, Xt) and of its conditional expectation
wt* are both equal to the maximum expected log return for period t given ~,
(37)
~* = E{w/} = E{log(bt, Xt)} = sup E{log(b, Xt)}.
bEff,
We argue that {bno <t<oo is optimum in the long run.
THEOREM 5 (Asymptotic optimality principle).
Suppose the random outcomes {Xt}o<t<oo are defined on a perfect probability space (Q, §',P), and
{ ~}o s; t < 00
is an increasing sequence of sub-a-fields of §' such that
a(Xo,"" Xt-I) ~ ~ for all 0::;: t < 00. Let the compounded capital after n
periods of investment according to the log-optimum strategy {bt}o s; t < 00 and
some competing nonanticipating strategy {bt}o < t < 00 be denoted by
(38)
Sn* =
TI (bt, Xt)
and Sn =
TI (bt> Xt)·
Os;t<n
Os;t<n
Then {S,/ Sn*, ~}O s; n < 00 is a nonnegative supermartingale converging almost
surely to be a random variable Y with E{Y} ::;: 1. Furthermore, E{S,/Sn*} ::;: 1
for all n, and
(39)
PROOF.
The log-optimum investor and his competitor start with equal
fortunes, so that So/So* = 1. The ratio Sn/Sn* = nO<;t<n(bt, Xt)/(bt, Xt) is
~-measurable, and the conditional log-optimality of b: given ~ is equivalent
to the Kuhn-Tucker condition
It follows that
So {S,/Sn*' ~}o
<; n < 00 is a nonnegative supermartingale. Any nonnegative supennartingale converges almost surely, and the expectations decrease monotonically to a limit no smaller than the expectation of the limit, by Fatou's lemma.
Thus S,/Sn* converges almost surely to a nonnegative random variable Yand
1 = E{So/So*} ~ E{S,/Sn*} ~ lim !E{S,/Sn*} ~ E{Y}.
n
--- page 197 ---

170
PH Algoet and T M Cover
LOG-OPTIMUM INVESTMENT
889
Since E{S,,/Sn*} .:s; 1, it follows from the Markov inequality that, for rn> 0,
P{S,,/Sn* ;;:: rn} .:s; rnlE{S,,/Sn*} .:s; r;l .
If rn increases sufficiently fast so that Lnr;l < 00, then
L:P{S,,/Sn* ;;:: rn} .:s; L:r;l < 00 ,
n
n
and hence S,,/Sn* < rn eventually for large n, by the Borel-Cantelli lemma. In
particular, choosing rn = exp(ne) with e > 0 proves that
p{ n - llog(S,,/Sn*) ;;:: €infinitely often} = O.
Since e> 0 was arbitrary we may conclude that limsuPnn- 1log(S,,/Sn*) .:s; 0 a.s.
[This fact can be proved also by observing that Sn/Sn* converges to a random
variable Y with E{Y} .:s; 1 and hence 0 .:s; Y < 00 a.s. Indeed, Sn/Sn* .:s; (1 + Y)
for large n and hence limsuPnn-1log(S,,/Sn*) .:s; limnn - 1log(1 + Y) = 0 a.s.] 0
Theorem 5 asserts that any alternative is dominated in the long run by the
log-optimum strategy. Indeed, E{S,,/Sn*} .:s; 1 for all n, and the Borel-Cantelli
lemma implies that S,,/Sn* < rn eventually for any sequence {rn} such that
Lnrn-1 < 00 (e.g., rn = n1+ E or rn = eM). The maximal inequality for nonnegative
supermartingales [cf. Neveu (1972), Proposition II-2-7, page 23] asserts that
(40)
p{ supS,,/Sn* ;;:: A} .:s; I/A.
n
Thus with probability at least 1 - I/ A, a competing investor will never outperform Sn* by a factor greater than A. The random variable sUPnSn/Sn* is finite
almost surely, although its expectation is generally infinite. A game-theoretic
sense in which Sn* dominates Sn for games with payoff E{<p(SA1)/SA2»} with <p
increasing is given in Bell and Cover (1980, 1986).
The conclusions of Theorem 5 hold if {~} is an increasing sequence of
information fields with o(Uo, ... , Ut- 1) ~ ~ for all t. Indeed, Sn/ Sn* =
no:s; t < n( bt> Ut)/( bt, Ut) is completely determined by the history of the scaled
outcomes Ut = u( Xt).
6. The asymptotic equiparitition property. Breiman (1960, 1961) considered a market with outcomes {Xt } that are independent and identically distributed according to an atomic measure, and he argued that repeated choice of the
log-optimum portfolio b* is optimum according to various criteria. In particular,
the capital Sn* = no < t < n( b*, Xt) will grow exponentially fast almost surely
with limiting rate equal to the maximum expected log return w * =
sUPbE{log(b, X)}, by the strong law of large numbers,
(41)
n-llogSn* = n - 1 L: log(b*, Xt) ~ w* = E{log(b*, X)}
a.s.
O:s; t<n
We prove an asymptotic equipartition property for log-optimum investment
in a market that is stationary ergodic. The successive outcomes Xt(w) = X(Ttw)
are defined in terms of a random vector X( w) E!!J':' and an invertible measure-
--- page 198 ---

Asymptotic Optimality and Asymptotic Equipartition Properties of Log-Optimum Investment
171
890
P. H. ALGOET AND T. M. COVER
preserving and metrically transitive transformation T defined on a perfect
probability space (n, ~, P). Since T is invertible, the returns can be embedded
in a two-sided sequence {X t} - 00 < t < 00'
Let bt be a log-optimum portfolio for period t based on the t-past ~
=
a(Xo, ... , Xt- I)' and let bt be log-optimum for period 0 based on the shifted
infonnation field ~ = T~ = a( X _I' . .. , X _ t). Portfolios bt and be* attain the
maximum conditional expected log returns wt* = sUPbEs-;E{log(b, Xt)I~} and
w/ = sUPbEft,E{log(b, Xo)I~} . We denote by ~* = E{log(be*, Xt)} and
~* = E{log(bt, Xo)} the maximum expected log returns. Then ~* =
W*(XoIX _l>'''' X _t) equals ~* = W*(XtIXt_I , . .. , Xo) by stationarity. If
b:' is a log-optimum portfolio for period 0 based on the limiting a-field ffoo =
a(X _I, X_ 2 , ••• ), then
~* = ~* increases monotonically to We: =
E{log(b:', Xo)}' This limiting expectation is equal to the maximum expected log
return given the infinite past, and is denoted by We: = W*(XoIX _p X- 2, .. . ) .
It may be noted that W*(XOIX _I, ... , X - h) is the maximum expected log
return given the infinite past under the stationary kth-order Markov process
having the same (k + 1 )st-order marginal distribution as {X t}.
Let Sn* = IIo <t<n(bt, Xt) denote the capital growth over n periods of
log-optimum investment. The AEP asserts that the time-averaged growth rate
n - llogSn* and its expectation n - 1E{logSn*} = n - IW*(Xo," " X n- I) converge
to the same limit.
THEOREM 6 (Asymptotic equipartition property).
If the sequence of stock
return vectors {Xt } is stationary ergodic, then capital will grow exponentially
fast under the log-optimum investment strategy, almost surely with constant
asymptotic rate equal to the maximum expected log return given the infinite past
(42)
n - llogSn* -+ We: = W*(XOIX _I , X - 2 , ... )
a.s.,
where
(43)
= lim i n-IW*(Xo,"" Xnl )·
n
PROOF.
One potential approach to establish the AEP for log-optimum investment is to invoke the extended ergodic theorem that was used by Breiman
(1957/ 1960) to prove the AEP of information theory. This extension of the
ergodic theorem asserts that
(44) n - llogSn*=n-1 L we*(Ttw)-+Woo*=E{w;} a.s.andinV,
Os; t <n
if we* = log(bt, Xo) converges to w; = log(b:', Xo) and {we*}o s; t<oo is Vdominated. Theorem 4 asserts that we* -+ w; a.s., but it seems hard to check
the integrability condition E{suptlwt*l} < 00. We shall instead reduce the AEP
to direct applications of the ergodic theorem, using a sandwich argument.
--- page 199 ---

172
P H A 19oet and T M Cover
LOG-OPTIMUM INVESTMENT
891
The information field :Fe = a( Xo, ... , Xt-I) is approximated by a more refined a-field :Fe(oo) and by less refined a-fields :Fe(k), defined for 0 ::s; k < 00 as
follows:
(45)
(46)
Let b}k) and b~oo) denote log-optimum portfolios for period t based on the
approximating a-fields :Fe(k) and :Fe(oo), and let the corresponding capital
growths over n periods be denoted by
(47)
S~k) = L
(b~k), Xt) and
S~oo) = fl (b~OO), Xt).
O:£ t < n
O:£ t < n
Thus S~k), Sn* and S~oo) denote the capital growth over n periods of log-optimum
investment when the investor is allowed to look back at each stage, respectively,
at the k-past (but not beyond period 0), up to time 0 and into the infinitely
distant past.
Observe that b~k)(w) = bt(Tt-kw) if t ~ k. Given the expansion
(48)
n - llogS~k) = n - llogSk* + n - I L
log(b~k), Xt),
k:£ t < n
it follows from the ergodic theorem that
(49)
n - llogS~k) ~ Wk* = E{log(bt , Xk)} a.s.
The sequence {log(b~OO), Xt)} is stationary ergodic and b&oo) = b:', so that again
by the ergodic theorem,
(50)
n-llogS~"") = n- I L
10g(b~00 ) , Xt) ~ W,: = E{log(b:', Xo)}
a.s.
0 :£ t < n
The log-optimum :Fe(ktmeasurable portfolio
b~k) is :Fe-measurable since
~(k) ~:Fe, and the log-optimum :Fe-measurable portfolio bt is :Fe(oo!.measurable
since :Fe ~ :Fe(00). It follows from the asymptotic optimality principle that
(51)
lim:upn- Ilog( ~n:») ::s; 0 and
lim:upn- Ilog( ~:) ) ::s; 0 a.s.
Thus we obtain the chain of asymptotic inequalities
a.s.
The AEP follows since Wi.* = Wk* l' W,: with no gap as k ~ 00. 0
The sandwich proof of the AEP remains valid if the log-optimum portfolios
bt are based on information fields :Fe other than the history of past outcomes
a( Xo, . . . , Xt-I)' However, {:Fe}o ~ t < 00 must be monotonically increasing and the
--- page 200 ---

Asymptotic Optimality and Asymptotic Equipartition Properties of Log-Optimum Investment
173
892
P. H. ALGOET AND T. M. COVER
history of the scaled return vectors a(Vo, ... , Vt- I) must be contained in ~, so
that the asymptotic optimality principle can be invoked. Monotonicity of {~}
means that information available about the past should never be erased from
memory. In addition, one must assume that the shifted fields ~
= T~ are
monotonically increasing to a limiting a-field ~OO' so that We* /' We: by Theorem 4. Monotonicity of {~} means that later investors have an advantage in
information when compared on common grounds, after shifting back to the
reference period 0, where all face the same decision problem of selecting boo
Suppose in particular that side information Ye( w) = Y(Ttw) is revealed together with the return vector X t at the end of period t. Then ~
=
a(Xo, Yo, · ··, Xt-I' Ye-I) and ~ = a(X_t> Y - t,···, X _I' Y- I) are monotonically
increasing, and n-llogSn* ~ We: almost surely where We: = W*(XOIX _I'
Y- I, X _2 , Y- 2 , • •• ) is the maximum expected log return given the infinite past.
The proof is identical to that of Theorem 6, except that bt = b*(Qt) and
bt = b*(Qt) are now defined by applying a measurable selector of log-optimum
portfolios b*(·) to regular conditional probability distributions Qt and Qt of
Vt = u(Xt) given ~ and of Vo = u(Xo) given ~.
The true log return log( bt, Xt) will generally differ from the conditional
expected log return wt = E{log(bt, Xt)I~}. If conditional expected log returns
were always exactly realized then the capital growth over n periods would be not
Sn* but rather
(53)
Sn* = TI exp[E{log( bt, Xt)I~}].
O~t < n
If Sn = no < t < nexp[E{log( bt, Xt)I~}] denotes the corresponding quantity under the co~peting strategy {btl, then Sn ~ Sn* for all n, and hence
(54)
lim supn -Ilog( S";Sn*) ~ 0 a.s.
n
This may be called an asymptotic optimality principle for the hypothetical
growth rate Sn*. If the market is stationary ergodic, then an asymptotic equipartition property for Sn* can be proved as well, under certain integrability conditions. Let L log L designate the class of random variables g( w) such that
E{lglloglgl} < 00.
THEOREM 7. If the market is stationary ergodic and E{log(,B, Xo)l~oo}
belongs to L log L, then
(55)
n - Ilog Sn* ~ We:
a.s. and in V .
PROOF. Breiman's (1957/1960) extension of the ergodic theorem asserts that
n-lLO ~ t < nge<TtwL ~ E{g} a.s. and in V if gt ~ g a.s. and E{sUPtlgtl} < 00 . In
particular, if {gt, ~}o~t < oo is a martingale or a nonnegative submartingale with
limit g in L log L, then the integrability condition E{ sUPtlgtl} < 00 is satisfied.
Indeed, Wiener's dominated ergodic theorem [cf. Chung (1974), example 7, page
355] asserts that
E{ S~Plgtl} ~ e: 1 [1 + S~PE{lgtllog+lgtl}] ~ e: 1 [1 + E{lgllog+lgl}] .
--- page 201 ---

174
PH Algoet and T M Cover
LOG-OPTIMUM INVESTMENT
893
Consider the decomposition wt* = rt + w*(Qt), where rt = E{log(,B, Xo)I~}­
Since {ro ~}o ,; t< 00 is a martingale with limit roo = E{log(,B, Xo)l.%oo} in L log L,
Breiman's extended ergodic theorem implies that
n- I L E{log(,B, Xt)I~} ~ E{log(,B, Xo)}
a.s. and in V .
O,; t<n
Since {w*(Qt)} is bounded and w*(Qt) ~ w*(Qoo ) a.s., we also have
n - 1 L
E{log(bt,lfe)I~} ~E{w*(Qoo)} a.s.andinV.
0 ,; t< n
By summation we may conclude that
n - llogSn* = n - 1 L w/ ~ E{w;} = W~ a.s. and in V.
0
O,; t<n
7. Stationary markets. We shall prove the AEP for markets that are
stationary but not necessarily ergodic. A stationary market is a mixture of
stationary ergodic modes [cf. Maitra (1977)], but no finite number of observations may suffice to exactly identify the (random) ergodic mode of {Xt}. However, log-optimum portfolios based on the t-past are better and better suited to
the ergodic mode as t increases, and the log-optimum portfolio given the infinite
past will be perfectly tailored because the ergodic mode is uniquely determined
by the infinite past. It is therefore not surprising that Sn* will grow with the
same asymptotic rate as if the ergodic mode were known to begin with.
The AEP may hold even if the market is stationary in an asymptotic sense
only. A dynamical system (Q, :F, P, T) asymptotically mean stationary (a.m.s.)
if the Cesaro averages n-1L.O <t<nP(TtF) converge for any event FE:F.
Setting the limit equal to P(F) then defines a stationary (T-invariant) probability distribution P on (Q, :F), and P is perfect whenever Pis. P the stationary
mean of P , and expectations with respect to P are denoted by E{·}. The
measures P and P have the same restriction to the invariant a-field J = {F E :F:
T-1F = F}, so that E{ ·IJ} = E{ ·IJ}. See Gray and Kieffer (1980) for further
discussion of asymptotically mean statioaary measures, and Section 34.2 in
Loeve (1978) for a proof that the following strong law of large numbers holds for
nonnegative measurable g( w ):
(56)
n - 1 L g(Ttw) ~ E{gIJ} = E{gIJ} a.s. (P) and a.s. (P).
0 ,; t< n
A market asymptotically mean stationary if the underlying dynamical system
(Q, :F, P, T) is a.m.s. As before we assume that T is invertible, P is perfect, and
Xt(w) = X(Ttw) for some random vector X(w) E !!l';'. The AEP holds for an
asymptotically mean stationary market, unless the investor goes broke after a
few rounds and remains trapped in a state that is infinitely worse than any
other. The investor should not be completely ruined by the time he reaches the
asymptotic regime, so that he can recover from transient losses.
THEOREM 8.
Suppose the market is stationary, and b:O is a log-optimum
portfolio for period 0 given the infinite past .%00. Then
(57)
n-llogSn* ~ E{log(b:O, Xo)IJ}
a.s.
--- page 202 ---

Asymptotic Optimality and Asymptotic £quipartition Properties of Log-Optimum Investment
175
894
P. H. ALGOET AND T. M. COVER
The same conclusion holds if the market is asymptotically mean stationary and
b:' is log-optimum under the stationary mean, at least if n-Ilog Sk* ~ 0 a.s. for
some sequence {kn} such that k n )'f 00 and k,,/n ~ o.
n
PROOF.
We consider the asymptotically mean stationary case. Recall that
Sn* = no,; t < n( bt, Xt), where bt is a log-optimum portfolio for period t based
on the t-past ~
= a(Xo,"" Xt-I)' Portfolio bt is log-optimum with respect to
the true distribution P. Let b; and b:' designate portfolios for period 0 that are
log-optimum with respect to the stationary mean P, based on the shifted
information field
ffk = a(X_k , ••• , X_I) and the limiting a-field ffoo =
a( ... , X _ 2' X _ I)' If an investor selects log-optimum portfolios bt during the
first k periods 0 ~ t < k, and in later periods t ~ k switches to suboptimum
portfolios b;(Ttw) (i.e., portfolios based on the k-past that are log-optimum with
respect to the stationary mean P), then capital growth over n periods will be
given by
(
Sn* ,
if 0 ~ n < k,
S~k) =
Sk* fl (b;(Ttw), Xt),
if k ~ n < 00.
k,; t< n
If the investor always selects the portfolio b:'(Ttw) that is log-optimum based on
the infinite past with respect to the stationary mean P, then capital growth is
given by
S~oo) = fl (b:'(Ttw), XJ
O,;t<n
It is clear that E{S~k)/Sn*} ~ 1 and E{Sn* /S~oo)} ~ 1, so that by Markov's
inequality and the Borel-Cantelli lemma (d. the proof of Theorem 5),
( S(k»)
limnsupn- Ilog ;n*
~ 0 a.s. (P) and
The ergodic theorem for a.m.s. measures implies that
and
Combining the previous results yields
E{log(b;(Tkw), Xk)I.F} = E{log(b;, Xo)I.F} ~ liminfnllogSn* a.s. (P)
n
and
limsupn-Ilog Sn* ~ E{log(b:', Xo)I.F}
a.s. (P).
n
The last inequality also holds a.s. (P) since both sides are invariant (the
--- page 203 ---

176
P H Algael and T M Cover
LOG·OPTIMUM INVESTMENT
895
left-hand side by assumption). We obtain the chain of asymptotic inequalities
E{log(bt, Xo)I.F} ~ liminfn-llogSn*
n
n
We claim that E{log(bt, Xo)I.F} is increasing in k. Indeed, if k ~ I, then the
event where E{log(bt, Xo)I.F} exceeds E{log(bt, Xo)I.F} must have zero probability, since conditioning on this invariant event and taking expectations would
otherwise contradict the inequality Wk* ~ W;*. The expectations Wk* =
E{log(bt, Xo)} increase to Woo* = E{log(b~ , Xo)} as k ~ 00 , so that by the
monotone convergence theorem,
E{log(bt, Xo)I.F} ? E{log(b~, Xo)I.F}
a.s. (1)).
Convergence also holds a.s. (P) since we are dealing with invariant random
variables, and Theorem 8 follows since E{log(b~, Xo)I.F} = E{log(b~ , Xo)I.F}. 0
8. Gambling as investment. We consider a market in which exactly one
stock will yield a nonzero return, the jth stock with probability qi. The random
outcome X is then oriented along one of the coordinate axes of !Jf m, and the
scaled return U is an extreme point of the simplex 0If = {u E !Jf ':' : (f3, u) = I}. As
observed by Kelly (1956), investing in such a market is like gambling on the
outcome of a horse race in which horse j has win probability qi. Since one unit
bet on horse j yields Vi = l/f3i if horse j wins, we have
w( b, Q) = EQ{log( b, V)} = L qilog( bi / f3 i ) = D( qllf3) - D( qllb).
15,i5,m
The information divergence D(qllb) = Ll 5,i5, mqilog(qi/ bi) is nonnegative, and
equal to zero iff b = q. It follows that the bet vector b = q = (qJ) l5, i 5, m is the
unique log-optimum portfolio. Thus the gambler should ignore the odds l/f3i
and place an amount on each horse j proportional to its win probability q i. The
maximum expected log of the scaled return w*(Q) is precisely the Kullback-
Leibler divergence between the probability vector q and the reference portfolio f3
that defines the odds, i.e.,
(58)
w*(Q) = D(qllf3) = L qilog(qi/f3 i ).
i5,i 5, m
Gambling on a set of m stocks out of which exactly one will yield a nonzero
return is a most risky type of investment game. Least risky is a market whose
return vector has a fixed direction, so that the stock(s) with highest return can
be predicted with certainty. In general, we say that a distribution Q on 0If is less
risky than another distribution Q', and write Q ~ Q', if there exists a dilation
f(duIJL) of au such that Q' = fQ, i.e., Q'( ,) = f<flf( ·lu)Q(du). [A dilation of 0If is
a transition probability f( dulJL) from 0If to 0If such that JL is equal to the
barycenter of f( ' IJL) for all JL E 0If.] See Alfsen (1971) for more discussion of this
so-called dilation or Choquet order on the space.2 of probability measures on 0If.
--- page 204 ---

Asymptotic Optimality and Asymptotic Equipartition Properties of Log-Optimum Investment
177
896
P. H. ALGOET AND T. M. COVER
If Q ~ Q', then Q is less risky and more attractive than Q', in terms of
expected log return. Indeed, Q ~ Q' iff f tfLlP(u)Q(du) ~ f tfLlP(u)Q'(du) for all
lower semkontinuous convex IP: dIf ~ (- 00, 00]. Choosing IP( u) = -log( b, u)
proves that w( b, Q) = EQ{log( b, U)} is increasing in Choquet order, and taking
suprema proves
THEOREM 9. The maximum expected log return w*(Q) = sUPbE{log(b, U)}
is monotonically decreasing in Choquet order on 2, i.e.,
(59)
if Q ~ Q' in 2, then w*( Q) ~ w*( Q' ).
I1If is a Choquet simplex, so every distribution Q on dIf admits a barycenter
p.(Q) E dIf and for every point p. E I1If there exists a unique probability measure
'IT,. on the set of extreme points of dIf that admits p. as barycenter. Two measures
that are comparable in Choquet order have the same barycenter. The point mass
8,. that is concentrated at p. is minimal and the measure 'IT,. on the extreme points
of I1If is maximal with respect to Choquet order on 2, among all distributions
that admit the point p. E dIf as barycenter. Notice that 'IT,.(Q) = IIQ, where
II(dulp.) = 'IT,.(du) is the maximal dilation that sweeps all mass to the extreme
points of 11If; the minimal dilation is the identity kernel Ll( dulp.) = 8,.( du) that
leaves all mass put.
Among all distributions Q on dIf with a given barycenter p.(Q) = p., the most
concentrated measure 8,. is best and the most dilated measure 'IT,. is worst in
terms of expected log return. Indeed, let p. = p.(Q) and let q denote the
probability vector proportional to p. [with components qj = p) / ('[, jp.j)]. Since
8,. ~ Q ~ 'IT,., Theorem 9 implies that
(60)
max log p) = w * ( 8,.) ~ w * ( Q),
(61)
J
w*(Q) ~ w*('IT,.) = D(qll,8) = Lqjlogqj.
j
The most natural choice for ,8 is the uniform portfolio (1/ m)1 5 j 5 m' which.
allocates an equal amount to each of the m stocks and whose yield (,8, X) is the
arithmetical average return m-1(Xl + ... +xm). Then D(qll,8) = log m-
JIt1( q), where JIt1( q) = - '[, jq j log qj is the Shannon entropy of the probability
vector q. In general, one may interpret h*(Q) = log m - w*(Q) as the minimum loss of expected log return relative to the ideal reference level r( P) + log m.
When the chain of inequalities 0 ~ w *( 8,.) ~ w *( Q) ~ w *( 'IT,.) ~ log m is rewritten in terms of h *( Q), one obtains
(62)
0 ~ min ( -logqj) = h*(8,.) ~ h*(Q) = logm - w*(Q),
J
(63)
h*(Q) ~ h*('IT,.) =JIt1(q) = Lq j(-logqj).
j
If one starts with a point mass 8,. located at p. E dIf and repeatedly dilates mass,
then Q traces out a linearly
~ -ordered chain of distributions all having
barycenter p.(Q) = p. in dIf. Ultimately, one ends up with a measure 'IT,., when all
--- page 205 ---

178
P H Algael and T. M Cover
LOG-OPTIMUM INVESTMENT
897
mass is swept to the comers (extreme points) of the simplex CiJI_ Initially (when
Q = 8 ), one can place all bets on the stock(s) j for which the minimum
~
.
information loss ( -log qJ) is minimum, but in the end (when Q =
'1T~) one has to
place proportional bets and concede an average loss equal to the Shannon
entropy£'(q) = Ll:S;i:s;mqi(-logqi).
Gambling on the next outcome of a horse race is a special type of investment
game. Proportional betting is log-optimum, and the asymptotic optimality
principle and asymptotic equipartition property can be formulated in a way that
does not seem to involve a maximization, since the log-optimum strategy is
explicitly known. The same is true for proportional betting on the next outcome
of a random process with values in a Polish space. Indeed, let p(xo,"" x n - 1)
denote the marginal density with respect to some dominating measure of
the first n outcomes of a random process {Xt}, and let q(xo,"" x n - 1) denote the density under some alternative distribution. The likelihood ratio
q(Xo," " Xn-1)/p(XO"'" Xn- 1) is then a nonnegative supermartingale converging almost surely to a random variable Y with E{Y} ::; 1, and
(64)
( q(Xo,"" X n - 1))
limsupn- 1log
(
X)::; 0 a.s.
n
P Xo,""
n - l
If, moreover, {Xt } is stationary ergodic and densities are taken with respect to a
Markovian reference measure, then p( Xo,' .. , X n - 1 ) will grow exponentially fast
with constant limiting rate almost surely equal to the relative entropy rate of
the true distribution with respect to the reference measure, i.e.,
(65)
n - 1logp(Xo," " X n - 1) -> supE{logp(Xo,"" X n - 1 )}
a.s.
n
See Barron (1985) and Orey (1985) for a proof of this generalized Shannon-
McMillan-Breiman theorem using Breiman's extension of the ergodic theorem
and Algoet and Cover (1988) for a sandwich proof.
Acknowledgments. We wish to acknowledge supporting discussions with
John Gill and David Larson.
REFERENCES
ALFSEN, E. M. (1971). Compact Convex Sets and Boundary Integrals. Springer, New York.
ALGOET, P. H. and COVER, T. M. (1988). A sandwich proof of the Shannon-McMillan-Breiman
theorem. Ann. Probab. 16 899-909.
BARRON, A. R. (1985). The strong ergodic theorem for densities: Generalized Shannon-McMillan-
Breiman theorem. Ann. Probab. 13 1292-1303.
BELL, R. and COVER, T. M. (1980). Competitive optimality of logarithmic investment. Math. Oper.
Res. 5 161-166.
BELL, R. and COVER, T. M. (1986). Game-theoretic optimal portfolios. Preprint.
BERTSEKAS, D. P. and SHREVE, S. E. (1978). Stochastic Optimal Control, the Discrete Time Case.
Academic, New York.
BREI MAN, L. (1957/1960), The individual ergodic theorem of information theory. Ann. Math.
Statist. 28809-811. Correction 31 809-810.
BREIMAN, L. (1960). Investment policies for expanding businesses optimal in a long run sense. Naval
Res. Logist. Quart. 7 647-651.
--- page 206 ---

Asymptotic Optimality and Asymptotic £quipartition Properties of Log-Optimum Investment
179
898
P. H. ALGOET AND T. M. COVER
BREIMAN, L. (1961). Optimal gambling systems for favorable games. Proc. Fourth Berkeley Symp.
Math. Skltist. Probab.l 65-78. Univ. California Press.
CHUNG, K. L. (1974). A Course in Probability Theory, 2nd ed. Academic, New York.
COVER, T. M. (1984). An algorithm for maximizing expected log investment return. IEEE Trans.
Inform. Theory IT-30 369-373.
FINKELSTEIN, M. and WHITLEY, R. (1981). Optimal strategies for repeated games. Adv. in Appl.
Probab. 13 415-428.
GRAY, R. M. and KIEFFER, J. C. (1980). Asymptotically mean stationary measures. Ann. Probab.8
962-973.
Jd~INA, M. (1954). Conditional probabilities on a-algebras with countable basis. Czechoslavak Math.
J. 4 372-380. (English translation in A mer. Math. Soc. Transl. Ser. 2 2 (1962) 79-86.)
KELLY, J . L., JR. (1956). A new interpretation of information rate. Bell System Tech. J . 35917-926.
KURATOWSKI, K. and RYLL-NARDZEWSKI, C. (1961). A general theorem on selectors. Bull. A cad.
Polon. Sci. 13 397-403.
LoEVE, M. (1978). Probability Theory 2, 4th ed. Springer, New York.
MAITRA, A. (1977). Integral representations of integral measures. Trans. Amer. Math. Soc. 229
209-225.
MARKOWITZ, H. M. (1952). Portfolio selection. J. Finance 777-91.
MARKOWITZ, H. M. (1959). Portfolio Selection. Wiley, New York.
NEVEU, J. (1972). Martingales a Temps Discret. Masson, Paris.
OREY, S. (1985). On the Shannon-Perez-Moy theorem. Contemp. Math. 41 319-327.
RAMACHANDRAN, D. (1979). Perfect Measures I-Basic Theory and II-Special Topics. lSI Lecture Notes 5,7. Macmillan, New York.
SAMUELSON, P. (1967). General proof that diversification pays. J. Financial and Quantitative Anal.
2 1-13.
SAMUEI.SON, P. (1970). The fundamental approximation theorem of portfolio analysis in terms of
means, variances and higher moments. Rev. Econom. Stud. 37 537-542.
SAMUELSON, P. (1971). The "fallacy" of maximizing the geometric mean in long sequences of
investing or gambling. Proc. Nat. Acad. Sci. U.S.A. 68 2493-2496.
SHARPE, W. F. (1985). Investments, 3rd ed. McGraw-Hili, New York.
THORP, E. O. (1971). Portfolio choice and the Kelly criterion. In Stochastic Optimization Models in
Finance (W. T. Ziemba and R. G. Vickson, eds.) 599-619. Academic, New York.
COLLEGE OF ENGINEERING
BOSTON UNIVERSITY
110 CUMMINGTON STREET
BOSTON, MASSACHUSETTS 02215
DEPARTMENTS OF STATISTICS AND
ELECTRICAL ENGINEERING
STANFORD UNIVERSITY
STANFORD, CALIFORNIA 94305
--- page 207 ---

This page is intentionally left blank
--- page 208 ---

Mathematical Finance, Vol. I, No.1 (January 1991), 1-29
15
UNIVERSAL PORTFOLIOS
THOMAS M. COVER I
Departments of Statistics and Electrical Engineering, Stanford University,
Stanford, CA
We exhibit an algorithm for portfolio selection that asymptotically outperforms the best
stock in the market. Let Xj == (xi), xi2' ... ,Xjm)' denote the performance of the stock
market on day i, where xi) is the factor by which the jth stock increases on day i.
Let bj == (bjl , bj2, ... , bjm )', bi) ~ 0, Ejbi) == I, denote the proportion bi) of wealth
invested in the jth stock on day i. Then Sn == II?= I b)xj is the factor by which wealth
is increased in n trading days. Consider as a goal the wealth S: == maxb II?= I b'xj that can
be achieved by the best constant rebalanced portfolio chosen after the stock outcomes are
revealed. It can be shown that S: exceeds the best stock, the Dow Jones average, and the
value line index at time n. In fact, S: usually exceeds these quantities by an exponential
factor. Let xI' x2' . . . , be an arbitrary sequence of market vectors. It will be shown
that the .Q0nanticipating sequence of portfolios bk ~ j bII t=-II b'xj db/j II ;k=-II b'x; db yields
wealth Sn == IIZ=I b~Xk such that (I/n)ln(S:/Sn) -+ 0, for every bounded sequence
XI' x2' .. . , and, under mild conditions, achieves
"
S:(m -
1)!(211'/n)(m-I)J2
Sn -
IJnl l / 2
where I n is an (m -
I) x (m -
I) sensitivity matrix. Thus this portfolio strategy has the
same exponential rate of growth as the apparently unachievable S: .
KEYWORDS: portfolio selection, robust trading strategies, performance weighting,
rebalancing
I. INTRODUCTION
181
We consider a sequential portfolio selection procedure for investing in the stock
market with the goal of performing as well as if we knew the empirical distribution
of future market performance. Throughout the paper we are unwilling to make
any statistical assumption about the behavior of the market. In particular, we
allow for the possibility of market crashes such as those occurring in 1929 and
1987. We seek a robust procedure with respect to the arbitrary market sequences
that occur in the real world.
We first investigate what a natural goal might be for the growth of wealth for
arbitrary market sequences. For example, a natural goal might be to outperform
the best buy-and-hold strategy, thus beating an investor who is given a look at a
newspaper n days in the future.
We propose a more ambitious goal. To motivate this goal let us consider all
constant rebalanced portfolio strategies. Let x = (XI> X2, ••• , xm)\ ~ 0 denote a
stock market vector for one investment period, where Xi is the price relative for
I I wish to thank Hal Stern for his invaluable contributions in obtaining and analyzing the stock
market data. I also wish to thank the referee for helpful comments. This work was partially supported
by NSF Grant NCR 89-14538.
Manuscript received January 1990; final revision received July 1990.
--- page 209 ---

182
T M Cover
2
THOMAS M. COVER
the ith stock - i.e., the ratio of closing to opening price for stock i. A portfolio
b = (b l , b2, . . . ,bm)t, bi ;;:: 0, E bi = 1, is the proportion of the current wealth
invested in each of the m stocks. Thus S = btx = E bixi, where b and x are
considered to be column vectors, is the factor by which wealth increases in one
investment period using portfolio b.
Consider an arbitrary (nonrandom) sequence of stock vectors xl> X2, ... , Xn
E R~. Here xij is the price relative of stock j on day i. A constant rebalanced
portfolio strategy b achieves wealth
n
0.1)
Sn(b) = II btXi'
i=1
where the initial wealth So (b) = 1 is normalized to 1. Let
(1.2)
denote the maximum wealth achievable on the given stock sequence maximized
over all constant rebalanced portfolios. Our goal is to achieve S:.
We will be able to show that there is a "universal" portfolio strategy hh where
hk is based only on the past xl> X2, . . . , Xk-l> that will perform asymptotically as
well as the best constant rebalanced portfolio based on foreknowledge of the
sequence of price relatives. At first it may seem surprising that the portfolio hk
should depend on the past, because the future has no relationship to the past.
Indeed the stock sequence is arbitrary, and a malicious nature can structure future
Xk'S to take advantage of past beliefs as expressed in the portfolio hk • Nonetheless
the resulting wealth can be made to track S:.
The proposed universal adaptive portfolio strategy is the performance weighted
strategy specified by
(1.3)
hi = (~,~, . .. , ~),
m m
m
where
(1.4)
k
Sdb) = II btXi'
i=1
and the integration is over the set of (m -
1 )-dimensional portfolios
B = [bERm: bi ;;:: O"~ bi = I).
1=1
0.5)
The wealth Sn resulting from the universal portfolio is given by
n
0 .6)
SA II Abt
n =
kXk·
k=1
Thus the initial universal portfolio hi is uniform over the stocks, and the port-
--- page 210 ---

Universal Portfolios
183
UNIVERSAL PORTFOLIOS
3
folio bk at time k is the performance weighted average of all portfolios bE B. An
approximate computation will be given in Section 8, and a generalization of this
algorithm will be given in Section 9.
We will show that
(1.7)
(lln)ln Sn - (lIn)ln S; --+ 0,
for arbitrary bounded stock sequences Xl> X2, . .•• Thus Sn and S; have the same
exponent to first order. A more refined analysis for two stocks shows
A
{h *
(1.8)
Sn -
~;iJ,; Sn'
in a sense that will be made precise. It is difficult to summarize the behavior of
Sn relative to S; because of the arbitrariness of the sequence and the fact that we
cannot assume a limiting distribution. For example, even the limit of (lIn)ln S;
cannot be assumed to exist.
The goal of uniformly achieving S;(XI, X2, .. . , xn ), as specified in (1.7), was
partially achieved by Cover and Gluss (1986) for discrete-valued stock markets
by using the theory of compound sequential Bayes decision rules developed
in Robbins (1951), Hannan and Robbins (1955), and the game-theoretic
approachability-excludability theory of Blackwell (1956a, b). Work on natural
investment goals can be found in Samuelson (1967) and Arrow (1974). The vast
theory of undominated portfolios in the mean-variance plane is exemplified in
Markowitz (1952) and Sharpe (1963), wbile the theory of rebalanced portfolios for
known underlying distributions is developed in Kelly (1956), Mossin (1968), Thorp
(1971), Markowitz (1976), Hakansson (1979), Bell and Cover (1980, 1988), Cover
and King (1978), Cover (1984), Barron and Cover (1988), and Algoet and Cover
(1988). A spirited defense of utility theory and the incompatibility of utility theory
with the asymptotic growth rate approach is made in Samuelson (1967, 1969, 1979)
and Merton and Samuelson (1974).
We see the present work as a departure from the above model-based investment
theories, whether they be based on utility theory or growth rate optimality. Here
the goal S; = maxbII;= I btx; depends solely on the data and does not depend
upon underlying statistical assumptions. Moreover, Theorem 5.1, for example,
provides a finite sample lower bound for the performance Sn of the universal
portfolio with respect to S;. Therefore the case for success rests almost entirely
on the acceptance of S; as a natural investment goal.
The performance of the universal portfolio is exhibited in Section 8, where
numerous examples are given of Sn (b), S;, and Sn for various pairs of stocks. In
general, volatile uncorrelated stocks lead to great gains of S; and Sn over the best
buy-and-hold strategy. However, ponderous stocks like IBM and Coca-Cola show
only modest improvements.
