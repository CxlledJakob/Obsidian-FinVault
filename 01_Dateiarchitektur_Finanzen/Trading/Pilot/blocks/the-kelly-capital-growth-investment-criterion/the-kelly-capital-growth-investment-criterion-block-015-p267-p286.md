# The Kelly capital growth investment criterion _ theory and -- Leonard C_ Maclean, Edward O_ Thorp, W_ T_ Ziemba, Leonard -- World Scientific Handbook -- isbn13 9781283148344 -- bec576e26410d0c695fd5b867d08ec4f -- An.pdf — pages 267–286

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
--- page 268 ---

Optimal Strategies f or Repeated Games
Optimal strategies for repeated games
Lemma 2. The following are equivalent:
(i) There is a strategy with the associated fortune
(ii) F! -+ 00 a.s.
(iii) cf>( 1'*) > O.
Fn -+ 00
a.s.
as
n-+ oo•
(iv) E(X;) > 0 for at least one i, 1 ~ i ~ N.
Proof·
241
421
(i) implies (ii). In Theorem 1 we show that F,JF~ tends almost surely to
a finite limit.
(ii) implies (iii). If cf>( 1'*) = 0, then F! = Fo for all n.
(iii) implies (iv). If 1'* . X = 0, then cf>( 1'*) = O. So 'Y~ > 0 for some i with X;
not identically O.
Fix all variables in
<p
but 1';
and set '1'( 1';) =
cf>('Y!, 'Y!, ' .. , 'Y~-l> 1';, 'Y~+l"'" 'Y~), a concave function which has a positive
max at 'Yf. If E(Xi ) ~ 0, then '11"(0) ~ 0, and 'I' has a local max at 0 and so has a
global max there because it is concave. Hence E(X;) > O.
(iv) implies (i). Define 'I' by setting all the variables but 1'; equal to 0 in
cf>: '1'(0, 0, ' ",0, 'Yi, 0,"',0). As E(X;»O, '1"(0»0 and so '1'(1';»0 for 'Yi
close to O. Thus cf>( 1'*) > O. Since log (F!/Fo) = g log (1 + 1'* . X(j)
and
E((log F!/Fo)/n) = cf>( 1'*) > 0, the strong law of large numbers shows that
F!/Fo -+ 00 almost surely.
Example 3. Let Xl and X2 be the coordinates of a point distributed
uniformly on [-1, b]x[ -1, b]. Then cf>('Yh 1'2) = E(log (1 +'YlXl +'Y2X2» has a
maximum at 1'* = O,!) if b ~ log (16)-1.
If (1'1' 1'2) is a point where cf> attains its max, then so is (1'2' 1'1) by symmetry.
Since cf> is concave, G>(cf>('Yh'Y2)+cf>('Y2,'Yl»~cf>G('Yl+'Y2),!('Yl+'Y2»' and we
may look for the maximum of cf> along the diagonal (1', 1'), 0:;; l' :;;!. Then
d
1 rb rb
Xl +X2
d'Y cf>( 1',1') = (b + 1)2 tl tl (1 + 'Y(X I + X2» dxl dx2·
The second derivative is <0, and cf>' is decreasing. A direct but tedious
integration and calculation shows that
.
d
((log 16))
11m -
cf>('Y, 1') =2 1- ---
.
..,-!- d'Y
(b + 1)
Hence cf>('Y, 1'), which can be shown to be continuous on [0, n increases up to
its max at G,!) as long as b $;log (16)-1 = 1.77 · . . .
It is interesting to compare this situation with betting on only one variable,
say Xl' Then cf>l( 1'1) = E(log (1 + 'YIXl» is continuous on [0, 1]. Continuity on
[0, 1) follows from Lemma 1 or inspection. Because of the singularity at
--- page 269 ---

242
M Finkelstein and R. Whitley
422
MARK. FINKELSTEIN AND ROBERT WHm..EY
Yt . Xl = -1 in the integrand, continuity at 1 is not by inspection; one must
compute cf>l (1) = log (1 + b) - 1 and show it is equal to the limit. (The situation
in two variables, which we dismissed with a word, is not easier.)
The function cf>1 is differentiable on [0, 1) by inspection or Lemma 1. It is
only differentiable at 1 in an extended sense; we can show that <1>'1(1) = -00 and
that lillly_l cf>'kf) = -00.
The function <1>1 has a unique maximum at a point yf, 0< yf< 1. From
Lemma 2, yf = 0 iff E(X) = (b -1)/2 ~ O. The existence of yt < 1 follows from
<I>'t (0) = (b -1)/2 and cf>'l (1) = -00, the uniqueness from strict concavity.
The surprising fact is that for one variable Xl a gambler does not bet all his
fortune no matter what b is, but he does bet all his fortune on two
independent copies of Xl for b large enough.
The reader who has carried out the calculations of Examples 2 and 3 knows
that, because of the possible singularity on L Yk = 1, it is not clear that <I>
attains a maximum, and the differentiability of <I> on the boundary L Yk = 1 is
even less clear.
Think of a continuous strictly increasing concave function 1 on [0,1] and
redefine it at 1 so that its value there is less than 1(0). If this redefined function
were E(log (1 + yX», then X would be a most interesting game with no
Kelly-Breiman optimal strategy: with unit fortune, if a gambler bet an amount
less than 1 he could always do better by betting slightly more, but betting all
would be worst.
One result of Lemma 3 is that there is an optimal y* so no game can have
the property discussed in the paragraph above. Another result of Lemma 3 is
that <I> is continuous, when finite. This is important because when we compute
y*, a numerical calculation which will generally give y* to a certain number of
decimals, we want to know that using this approximation to the exact y* will
give close to optimal perfonnance.
The other result is a substitute for differentiation when y* has I y~ = 1,
which allows us to derive the basic ineqUalities (9) and (10). Note that if all the
random variables Xl> X 2 , ••• , XN are discrete, with a finite number of values,
as they are in [4], then we can differentiate cf> at y*: for then if y •. X equals
-1 it does so with positive probability and <1>( y*) = -00 < <1>(0) = 0, contrary to
<1>( y*) a maximum; thus <I> is actually defined on a neighborhood of y. (which
may extend outside D) and is differentiable as in Lemma 1. The problems
which Lemma 3 resolves are those which arise from more general random
variables.
Lemma 3.
(i) The function <I> is continuous where finite, and attains a maximum at a
point y* in D.
--- page 270 ---

Optimal Strategies for Repeated Games
243
Optimal Slrategies for repeated games
423
(ij) Let K = {k : yt 1= O}. For k in K, E(X,,/(1 + 1'* . X) is finite and nonnegative. If k belongs to K, then for all m
(9)
E(XJ(1 + 1'* . X) ~E(x..J(1 + 1'* . X) .
If both k and m belong to K,
(10)
E(Xk/(1 + 1'* . X) = E(X"J(1 + 1'* . X).
Proof. Suppose that y(n) converges to 1'(0) with 4>(1'(0» finite. Denote the
positive and negative parts of log by log+ and log- : log+(x) = log x if x ~ 1,
log+ (x) = 0 if x ~ 1 and log-ex) = -log (x) if x;i 1, log-ex) = 0 if x ~ 1. Since
log+ (1 + l' . X) ~ 11' . XI ;i max IXk I, 4> is infinite only if it is -00. By the Lebesgue
dominated
convergence
theorem
lim J log+ (1 + y(n) . X) dP =
J log+ (1 + 1'(0) . X) dP,
by Fatou's lemma lim inf J log- (1 + y(n) . X) dP ~
J log- (1 + 1'(0) . X) dP, and putting these two facts together, lim sup 4>( y(n» ~
4>(1'(0» . Thus 4> is upper semicontinuous and therefore attains its maximum on
the compact set {y in D: 4>(y)~O}.
For
0< a < 1,
4>(ay+(Ia)y(O» ~ aq,{y)+(1- a)4>(y(O»,
and
so
lim infa-o 4>(ay + (1- a)y(O» ~ 4>( 1'(0» if 4>(1') is finite, i.e., 4> is continuous
along lines directed towards 1'(0) from points where 4> is finite.
Suppose that yO) and 1'(2) are in D with 4>(1'(2» finite, and let a E [0, 1). Now
1 +ay(1)· X +(1-a)y(2). X ~ 1 +a L yLl)(-l)+(1- a)y(2). X
~(1- a)+ (1- a)y(2) . X
= (1- a)(1 + 1'(2) . X).
Since log- (1 + z) is a decreasing function of z, log- (1 + ay(1) · X +
(1- a)y(2). X)~log-(1-a)(1 +1'(2). X)
which
equals
-log (1-a)-
log (1 + 1'(2) . X) when (1- a)(1 + 1'(2) . X) ~ 1, and equals 0 otherwise. Hence
JIog- (1 + ay(l)· X +(1- a)y(2). X) dP~-log (1-a)+J log- (1 + 1'(2). X) dP < 00,
and thus 4>(ay(1) + (1- a )y(2» is finite for a 1= 1.
Let a point l' be a given at which 4> is finite. For 1;i k ~ N, let elk) be the
vector in D whose kth coordinate is 1, e~k) = a/let e(O) = 0, and set y(k) =
ae(k)+(1- a)y, a in (0,1), for O~ k ~N. Note that D is the convex hull
co(e(O), e(1), . .. , e(N» . As we have seen above, cf>( y(k» is finite and so cf> is
continuous on the line joining y(k) to y. Given e > 0, by choosing a small
enough we have 14>( y(k» - cf>{y)\ ~ e for 0 ~ k ~ N. For any vector v in the
convex hull U = co (1'(0), 1'(1), .. . , y(N», v = L a,. y(k), ale ~ 0, L a,. = 1, we have
cf>(V)~L ak4>(y(k»~cf>(y)-e. The convex hull U is easily seen to have an
interior
(relative
to
D).
Since
4>
is
upper semicontinuous,
V =
{a : cf>(a) < cf>(y) + e} is open. Therefore for v in the neighborhood VOn
V, Icf>( v) - cf>( y)\;i e and cf> is continuous at y.
--- page 271 ---

244
M Finkelstein and R. Whitley
424
MARK FINKEl.STEIN AND ROBERT WHITLEY
For y in D with LYi<1, and 0~a~1, define qr(a) = 4>(ay+(1-a)y*). We
have seen that qr is continuous on [0,1]. Given 0 < e < 1, for a in
[e, 1], 1 +(ay+(1-a)y*) . X~E(1-L Yi»O.
As
in
Lemma
1,
\(Y-Y*)'X/(1+(ay+(1-a)y*)'x)\ is bounded by the Ll function \(yy*) . X/E(1-L Yi)\ and we may use the Lebesgue dominated convergence
theorem to justify differentiating under the integral to obtain
qr'(a) = f
(y-y*). X
dP
1 +(ay +(1- a)y*) . X
.
Since e was arbitrary, this holds on (0, 1J.
If L y: < 1, then Lemma 1 establishes the fact that the expectations in (10)
are O. As in Lemma 2, if m is not in K, then fixing all the variables in 4> but Ym
and considering that concave function with a max at 0 shows that a4>/ aYm (Y*) ~
o and (9) follows.
Now suppose that L Y: = 1 and let x = (Xl> • •• , XN) be some value of the
random variable X in which not all the x" = -1 for k in K. Note that the event
x" = -1 for all k in K has probability 0 since the integrand in the integral
defining 4> is -00 there and 4>( y*) is finite.
For 0 ~ a < 1 and Y in DO, define
f(a) = log (1 + (ay + (1- a)y*) . x).
The function f is finite because x was so chosen, and is differentiable with
(y - y*) . x
f'(a)=-~~~--
1 +(ay +(1-a)y*)· x .
Because f"~0, f'(a) increases to (y-y*) . x/(1 + y*. x) as a decreases to O. For
a+O, (y-y*). X/(l+(ay+(l-a)y*)' X) in Ll we may apply the B. Levi
theorem to obtain
.
f ( y - y*) . X
lIm ¥(a) =
1
* X dP.
aJ.O
+y .
By tl)e mean value theorem, (qr(a)-qr(O)/a = 'I"(b), 0< b < a. Then, because qr'
is increasing, limaJ.o qr'(a) = limaJ.o «'I'(a) -'I'(O»/a). Since 4>( -y*) is a maximum
the right-hand side is ~O and we obtain the basic
(11)
f(y-y*),X
<
1
* X dP=O.
+y .
For 0 < e < 1 and k in K, the choice Yi = y1 for j =f k and Yk = y:(1- e) in
(11) gives - S X,J(1 + y* . X) dP ~ 0, and S Xk/(1 + y* . X) dP is non-negative
and therefore finite.
For kinK and any m, and 0 < e < y:, the choice y/ = yr for j neither k nor
--- page 272 ---

Optimal Strategies f or Repeated Games
245
Optimal strategies for repeated ga~s
425
m, Yn = y~ - e, Ym = Y! + e in (11) gives (9). Finally, (10) follows from (9) by
symmetry.
3. Theorems
If Fn is a gambler's fortune at the nth time period, obtained by using some
strategy y(1), y(2), ... , y(n), ... , and F! is the fortune obtained by using the
fixed fraction strategy y*, y*, ... , y*, . • . , then Breiman concludes ([4],
Theorem 2, p. 72) that lim F,J F! almost surely exists and E(lim F,J F!) ~ 1. We
extend these results in Theorem 1 below. Two comments are in order.
First, the advantage in using y*, as indicated by the fact that E(lim F,JF!);:a
1, does not require passage to the limit. This was noted by Durham, for the
case of two branching processes, in the proof of Theorem 1 of [6], p. 571. In
fact, given that the limiting result is true and given a finite strategy
y(1), ... , y(m), extend it by setting yO) = y* for j > m; then F,J F~ = F ml F! for
n ~ m and E(FmIF!);:a 1. This should reassure the careful investor who wonders whether a strategy good in the long run may not be inferior in any
practical number of trials-disregard of this point leads to an overevaluation of
games of the type which produces the St. Petersburg paradox.
Second, by our analysis of q" we are able to show in Theorem 1 that the
presence of the expectation in E(lim Fn/F~);:a 1 raises serious problems in any
superficial attempt to use this as an indication of the superiority of y*.
Theorem 1. Let Fn be the fortune obtained by using a strategy y =
y(l), ... ,y(n) for n repeated investment periods, and let F! be the fortune
obtained by using the fixed fraction strategy y*. Then
(i) F,JF! is a supermartingale with B(F,JF!)~ 1. Consequently, lim F,JF!
exists almost surely as a finite number and E(lim F,JF!) ~ 1.
(ii) Suppose that y bets only on those X" with y: > 0, i.e., that yp) = 0 if I ¢ K,
1 ;:a I ;:a N and all j. If L y: = 1, then funher suppose that L y~) = 1 for all j. Then
Fn/F! is a martingale with E(Fn/F!) = 1.
Proof. Let m be given and let f€m be the sigma-algebra generated by X1t),
l;:ak~N, l~j~m. Then
fEm+l\ )= (l+ y(m+l).x(m+l).Fm \
)
E\F*
f€m
E
1
* . X<m+ll
F*
~m'
m+l
+y
m
Since Fm/F! is ~m-measurable, this equals
Fm (1 + y(m+l) . x(m+t> I )
F! E
1 + y* . X
f€m .
Because y(m+l) is a strategy depending on the past values of the X~), it too is
--- page 273 ---

246
M Finkelstein and R. Whitley
426
MARK FINKELSI'EIN AND ROBERT WHITLEY
C€m-measurable. That, together with the independence of x(m+1) and the
previous XO), shows this equals
Fm E(
1
)
~ (m+l) ( Xkm +1) )
F!
1 + y* . X + k'=l Yk
E 1 + Y* . X .
Since x(m+l) has the same distribution as X, this can be written
(12)
~
[ E(l + y1* . X) + k~l y~m+l)E(l +~: . X)] = A, say.
By Lemma 3, E(Xk/(1 + y* . X) equals a constant c for k in K and is ~c for
all k; this constant c = 0 if L yt < 1. Hence
A ~=~ [E(1+y1* . x)+ L yt· c]= ;;EG:~:: ~]= ;;.
We have shown that F,JF! is a positive supermartingale, with E(F,JF!)~
E(Fn-1/F!-1) ~ ... ~ E(Fo/Fo) = 1, and so by the supermartingale convergence
theorem it converges almost surely to a finite limit. Using Fatou's lemma,
E(Iim F,JF~ ~ lim inf E(F,JF!) ~ 1.
An examination of (12) shows that under the conditions of (ii),
E(Fm+l/F!+l I C€m) = Fm/F,!, and (ii) follows.
The requirement in Theorem l(ii) that if L y! = 1 then we must have
L y~) = 1, for all j, in order to be sure to get a martingale, is made clear by a
one-variable example, Let X=2. Then cP(y) = log (1+2y) is maximal at y*=
1. The gambler will do worse betting any amount less than 1, even though he
still bets on the same random variable as y. does, the key observation being
cf/(l) > O. In general, the 'partial derivatives' E(X,J(l + y* . X), k in K, may be
positive if L yt = 1, whereas they are all 0 if L yt < 1.
The surprising result of Theorem 1 is the broad conditions in (li) under which
E(F,JF!) = 1. To see what the surprise is, we shall superficially interpret
Theorem 1(i): since 'on the average', and 'for large n', F,JF!~ 1, the gambler
'does better' with F! than with Fn. But then Theorem l(ii) tells us that if the
gambler simply bets on the same variables as y. does, but in any proportions at
all, and if y* bets all so does he, then E(FnlF!) = 1. So with the same intuitive
interpretation as above, 'on the average' the gambler does the same with Fn as
with F!, so it really does not matter which strategy he uses! But we know that
it does matter. For example, in a repeated biased-coin toss, if he plays a fixed
fraction strategy betting an amount y f y. = p - q, then almost surely F,J F! -+
O. Yet we have E(F,JF!) = 1. In general it will not help to look at lim F,JF~ .
For example, if on the first flip of the coin he bets all his fortune, and from then
on he bets p - q, F,J F! > 1 with probability p.
--- page 274 ---

Optimal Strategies for Repeated Games
247
Optimal strategies for repeated games
427
Theorem 2 will help our understanding of this situation by showing that F!
is the only denominator with E(F,./F!) ~ 1 for all F,,; in fact E(F!/Fn) > 1 if Fn
does not come from a strategy equivalent to using ,.* repeatedly. The suspicious reader will note that this characterization of the sense in which ,.* is
optimal contains an expectation. Anyone attempting to state intuitively the
result of Theorem 2(i) in the form 'F! is better than Fn because, on the
average, F!/Fn!: 1', should also be willing to apply the same interpretation to
Theorem 1(ii) and conclude that often, 'F,./F! = 1 on the average and so Fn
and F! are often the same after all'.
Theorem 2.
(i) F!/Fn is a submartingale with E(F!/Fn) ~ 1. Urn F!/Fn almost surely
exists as an extended real number and E(lim F!/Fn) iE;; 1.
(ii) E(F!/Fn ) = 1 iff ,.0), ,.(2), •.• ,,.(n) are all equivalent to ,.*, i.e., iff
y(j) . X'= y* . X almost surely for almost all values of X<l), ... ,XV) (of which
yU) is a function) for 1 ~ j ~ n.
Proof. By Theorem 1, the non-negative lim F,./F! almost surely exists, and
so lim F!/Fn almost surely exists as an extended real number.
As in Theorem 1,
(F*
\
)
F* ( l+y*' X<m+l)
\
)
E F m+l
~m = F mE 1 +y(m+1). X<m+l)
~m'
m+l
m
Suppose that (X<1),' .. ,X<m» takes on the value w in R mN, at which point
y(m+1) takes on the value ,.(m+1)(w). Then
( 1 +1* . X<m+l) \
) _
(
1 +1*' X<m+l)
)_
(13) E 1 + ,.m+l . X<m+l) ()«l) •.•.• )«M»_ ...
- E 1 + ,.(m+l)(w) . X<m+l) - B,
say,
because X<m+l) is independent of the values of (X<l), ... ,x<m» ([5], Corollary
4.38, p. 80). By Jensen's ineqUality,
(14) B ~exp (E(log (1 +,.* . x<m+l»)_ E(log (1 +-y(m+l)(w) . X<m+l»)))
= C, say.
By Lemma 1, C> 1 unless ,.*. X = ,.m+1(w)· X almost surely, in which case
C= 1. Thus
(15)
with equality holding jff,.*· X = ,.~::.,>+1) . X almost surely for almost all values w
in
the
range
of
(X<I>, ... , X< .... ».
If E(F!+dFm +1) = 1,
then
1 =
E(E(F!+I/Fm+l I ~m» iE;; E(F!/Fm) iE;; ... iE;;E(Fo/Fo) = 1.
By
(15),
equality
holds in (15) and therefore ,.* . X = ,.(m+1)(w) . X for almost all w in the range
of (X<1), ... ,X<"'». Continue for m, m -1, ... , I, to obtain (ii).
--- page 275 ---

248
M Finkelstein and R. Whitley
428
MARK FINKEI..STEIN AND ROBERT WHITl...EY
Let Y=limF~/F". By Theorem 1, P(Y=O)=O and E(1/¥)~l. The function g(x) = l/x is convex in (0,00) and Jensen's inequality applies, to obtain
1 ~ E(1/¥) ~ l/E(¥) which completes the proof.
References
[1] ABRAMOWITZ, M. AND S'TEGUN, A. (1965) Handbook of Mathematical Functions. National
Bureau of Standards, Washington, D.C.
[2] AuCAMP, D. (1975) Comment on "the random nature of stock market prices" authored by
Barrett and Wright. Operat. Res. 13, 587-591.
[3] BICKSI.J:R, J. AND THORP, E. (1973) The capital growth model: an empirical investigation. 1.
Finance and Quant. Anal. vm, 273-287.
[4] BREIMAN, L. (1961) Optimal gambling systems for favorable games. Proc. 4th Berkeley
Symp. Math. Statist Prob. 1, 65-78.
[5] BREIMAN, L. (1968) Probability. Addison-Wesley, New York.
[6] DURHAM, S. (1975) An optimal branching migration process. 1. Appl. Prob. 1l, 569-573.
[7] FERGUSON, T. (1965) Betting systems which minimize the probability of ruin. 1. SIAM 13,
795-818.
(8) HEWITT, E. AND STROMBERG, K. (1965) Real and Abstract Analysis. Springer-Verlag, New
York.
(9) HAKANSSON, N. (1971) Capital growth and the mean-variance approach to portfolio
selection. 1. Finance and Quant. Anal. VI, 517-557.
[10] KmLv, J. (1956) A new interpretation of information rate. Bell System Tech. 1. 35,
917-926.
[11] LATANE, H. (1959) Criteria for choice among risky ventures. 1. Political Beon. 67,
144-155.
[12) LATANE, H., TlJm.E, D., AND JAMES, C. (1975) Security Analysis and Portfolio Management. Wiley, New York.
[13] OLVER, F. (1974) Introduction to Asymptotics and Special Functions. Academic Press, New
York.
[14) ROBERTS, A. AND VARBERG, D. (1973) Convex Functions. Academic Press, New York.
[15) THORP, E. (1971) Portfolio choice and the Kelly criterion. Proc. Amer. Statist. Assoc,
Business, Beon. and Stat. Section, 215-224.
[16] THORP, E. (1969) Optimal gambling systems for favorable games. Rev. Internal. Statisl.
Inst. 37, 273-293.
[17] THORP, E. AND WHm..EV, R. (1972) Concave utilities are distinguished by their optimal
strategies. Coil. Math. Soc. Janos Bolya, European Meeting of Statisticians, Budapest (Hungary),
813-830.
--- page 276 ---

Journal of Portfolio Management, 19, 6-11 (1993)
249
18
The Effect of Errors in Means,
Variances, and Covariances on Optimal
Portfolio Choice*
Vijay K. Chopra and William T. Ziemba
Good mean forecasts are critical to the mean-variance framework
There is considerable literature on the strengths and limitations of meanvariance analysis. The basic theory and extensions of MV analysis are discussed in Markowitz [1987] and Ziemba & Vickson [1975]. Bawa, Brown &
Klein [1979] and Michaud [1989] review some of its problems.
MV optimization is very sensitive to errors in the estimates of the inputs.
Chopra [1993] shows that small changes in the input parameters can result in
large changes in composition of the optimal portfolio. Best & Grauer [1991]
present some empirical and theoretical results on the sensitivity of optimal
portfolios to changes in means. This article examines the relative impact of
estimation errors in means, variances, and covariances.
Kallberg & Ziemba [1984] examine the question of mis-specification in
normally distributed portfolio selection problems. They discuss three areas
of misspecification: the investor's utility function, the mean vector, and the
covariance matrix of the return distribution.
They find that utility functions with similar levels of Arrow-Pratt absolute
risk aversion result in similar optimal portfolios irrespective of the functional
form of the utilityl; Thus, mis-specification of the utility function is not a
major concern because several different utility functions (quadratic, negative exponential, logarithmic, power) result in similar portfolio allocations
for similar levels of risk aversion.
Misspecification of the parameters of the return distribution, however, does
make a significant difference. Specifically, errors in means are at least ten
times as important as errors in variances and covariances.
We show that it is important to distinguish between errors in variances
and covariances. The relative impact of errors in means, variances, and covariances also depends on the investor's risk tolerance. For a risk tolerance of
-Reprinted, with permission, from Journal 0/ Portfolio Management, 1993. Copyright
1993 Institutional Investor Journals.
IFor an investor with utility function U and wealth W, the Arrow- Pratt absolute risk
aversion is ARA == -U"(W)jU'(W). Friend and Blume 11975] show that investor behavior
is consistent with decreasing ARA; that is, as investors' wealth increases, their aversion to
a given risk decreases.
53
--- page 277 ---

250
V K. Chopra and W T Ziemba
54
Chopra and Ziemba
50, errors in means are about eleven times as important as errors in variances,
a result similar to that of Kallberg & Ziemba.2 Errors in variances are about
twice as important as errors in covariances.
At higher risk tolerances, errors in means are even more important relative
to errors in variances and covariances. At lower risk tolerances, the relative
impact of errors in means, variances, and covariances is closer. Even though
errors in means are more important than those in variances and covariances,
the difference in importance diminishes with a decline in risk tolerance.
These results have an implication for allocation of resources according to
the MV framework. The primary emphasis should be on obtaining superior
estimates of means, followed by good estimates of variances. Estimates of
covariances are the least important in terms of their influence on the optimal
portfolio.
Theory
For a utility function U and gross returns r - i (or return relatives) for assets
i = 1,2, .. . , N, an investor's optimal portfolio is the solution to:
N
maximize Z(x) = E[U(Wo ~]ri)xi)]
i=l
N
such that Xi> 0, L = 1,
i=1
where Z(x) is the investor's expected utility of wealth, Wo is the investor's
initial wealth, the returns ri have a distribution F(r), and Xi are the portfolio
weights that sum to one.
Assuming a negative exponential utility function U(W) = - exp( -aW)
and a joint normal distribution of returns, the expected utility maximization
problem is equivalent to the MV-optimization problem:
N
1 N
N
maximize Z(x) = L E[ri]Xj - t L L xixjE[Uij]
i=1
i=lj=1
N
such that Xi > 0,
LXi = 1,
i=l
2The risk tolerance reflects the investor's desired trade-off between extra return and
extra risk (variance). It is the inverse slope of the investor's indifference curve in meanvariance space. The greater the risk tolerance, the more risk an investor is willing to
take for a little extra return. Under fairly general input assumptions, a risk tolerance of 50
describes the typical portfolio allocations of large US pensions funds and other institutional
investors. Risk tolerances of 25 and 75 characterize extremely conservative and aggressive
investors, respectively.
--- page 278 ---

The Effect of Errors in Means, Variances, and Covariances on Optimal Portfolio Choice
251
The Effect of Errors
55
EXHIBIT 1:
List of Ten Randomly Chosen DJIA Securities
1.
Aluminum Co. of America
2.
American Express Co.
3. Boeing Co.
4.
Chevron Co.
5.
Coca Cola Co.
6.
E.!. Du Pont De Nemours & Co.
7.
Minnesota Mining and Manufacturing Co.
8.
Procter & Gamble Co.
9. Sears, Roebuck & Co.
10.
United Technologies Co.
where E[TiJ is the expected return for asset i, t is the risk tolerance of the
investor, and E[OijJ is the covariance between the returns on assets i and j.3
A natural question arises: How much worse off is the investor if the distribution of returns is estimated with an error? This is an important consideration because the future distribution of returns is unknown. Investors rely on
limited data to estimate the parameters of the distribution, and estimation
errors are unavoidable. Our investigation assumes that the distribution of
returns is stationary over the sample period. If it is time-varying or nonstationary, the estimated parameters will be erroneous.
To measure how close one portfolio is to another, we compare the cash
equivalent (CE) values of the two portfolios. The cash equivalent of a risky
portfolio is the certain amount of cash that provides the same utility as the
risky portfolio, that is, U(CE) = Z(x) or CE = U- 1[Z(x)] where, as defined
before, Z(x) is the expected utility ofthe risky portfolio.4 The cash equivalent
is an appropriate measure because it takes into account the investor's risk
tolerance and the inherent uncertainty in returns, and it is independent of
utility units. For a risk-free portfolio, the cash equivalent is equal to the
certain return.
Given a set of asset parameters and the investors risk tolerance, a MYoptimal portfolio has the largest CE value of any portfolio of those assets. The
3 Although the exponential utility function is convenient for deriving the MV problem
with normally distributed returns, the MV framework is consistent with expected utility
maximization for any concave utility function, assuming normality.
4For negative exponential utility, Freund [19561 shows that the expected utility of portfolio x is Z(x) = 1 - exp( -aE[x] + (a2/2)Var[x]), where E[X] and Var[xl are the expected
return and variance of the portfolio. The cash equivalent is eEl: = (lla) log(l - Z(x)).
If returns are assumed to have a multivariate normal distribution, this is also the cash
equivalent of an MV-optimal portfolio. See Dexter, Yu & Ziemba [1980] for more details.
--- page 279 ---

252
V K. Chopra and W T. Ziemba
56
Chopra and Ziemba
percentage cash equivalent loss (CEL) from holding an arbitrary portfolio, x
instead of an optimal portfolio 0 is
CEL = CEo - CEx
CEo
where CEo and CEx are the cash equivalents of portfolio 0 and portfolio x
respectively.
Data and Methodology
The data consist of monthly observations from January 1980 through December 1989 on ten randomly selected Dow Jones Industrial Average (DJIA) securities. We use the Center for Research in Security Prices (CRSP) database,
having deleted one security (Allied-Signal, Inc.) because of lack of data prior
to 1985. Each of the remaining twenty-nine securities had an equal probability of being chosen. The securities are listed in Exhibit 1.
MV optimization requires as inputs forecasts for: mean returns, variances,
and covariances. We computed historical means (Ti), variances (aii), and
covariances (aij), and assumed that these are the 'true' values of these parameters. Thus, we assumed that E[ri] = Ti, E[aii] = aii, and E[aij] = aij' A
base optimal portfolio allocation is computed on the basis of these parameters
for a risk tolerance of 50 (equivalent to the parameter a = 0.04).
Our results are independent of the source of the inputs. Whether we use
historical inputs or those based on a complete forecasting scheme, the results
continue to hold as long as the inputs have errors.
Exhibit 2 gives the input parameters and the optimal base portfolio resulting from these inputs. To examine the influence of errors in parameter
estimates, we change the true parameters slightly and compute the resulting
optimal portfolio. This portfolio will be suboptimal for the investor because
it is not based on the true input parameters.
Next we compute the cash equivalent values of the base portfolio and the
new optimal portfolio. The percentage cash equivalent loss from holding the
suboptimal portfolio instead of the true optimal portfolio measures the impact
of errors in input parameters on investor utility.
To evaluate the impact of errors in means, we replaced the assumed true
mean Ti for asset i by the approximation Ti(l + kzi) where Zi has a standard
normal distribution. The parameter k is varied from 0.05 through 0.20 in
steps of 0.05 to examine the impact of errors of different sizes. Larger values
of k represent larger errors in the estimates. The variances and covariances
are left unchanged in this case to isolate the influence of errors in means.
The percentage cash equivalent loss from holding a portfolio that is optimal
for approximate means Ti (1 + kzi ) but is suboptimal for the true means r, is
--- page 280 ---

The Effect of Errors in Means, Variances, and Covariances on Optimal Portfolio Choice
253
The Effect of Errors
57
EXHIBIT 2:
Inputs to the Optimization and the Resulting Optimal Portfolio for a
Risk Tolerance of 50 (January 198G-December 1989)
Alcoa Amex Boeing Chev.
Coke Du Pont MMM
P&G
Sears UTech
Means ('Yo
per month)
1.5617 1.9477
1.907
1.5801 2.1643
1.6010
1.4892 1.6248 1.4075 1.1537
Std. Dev. ('Yo
per month)
8.8308 8.4585 10.040 8.6215 5.988
6.8767
5.8162 5.6385 8.0047
8.212
Correlations
Alcoa
1.0000
Amex
0.3660 1.0000
Boeing
0.3457 0.5379 1.0000
Chev.
0.1606 0.2165 0.2218 1.0000
Coke
0.2279 0.4986 0.4283 0.0569 1.0000
Du Pont
0.5133 0.5823 0.4051 0.3609 0.3619
1.0000
MMM
0.5203 0.5569 0.4492 0.2325 0.4811
0.6167
1.0000
P&G
0.2176 0.4760 0.3867 0.2289 0.5952
0.4996
0.6037 1.0000
Sears
0.3267 0.6517 0.4883 0.1726 0.4378
0.58Il
0.5671 0.5012 1.0000
UTech
0.5101 0.5853 0.6569 0.3814 0.4368
0.5644
0.6032 0.4772 0.6039 1.0000
Optimal Port.
Weights
0 .0350 0.0082
0.0
0.1626 0.7940
0.0
0.0
0.0
0.00
0.00
then computed. This procedure is repeated with a new set of Z values for a
total of 100 iterations for each value of k.
To investigate the impact of errors in variances each variance forecast O'ii
was replaced by O'ii(l + kZj ). To isolate the influence of variance errors, the
means and covariances are left unchanged.
Finally, the influence of errors in covariances is examined by replacing
each covariance O'ij (i # j) by O'ij + kZij where Zij has a standard normal
distribution, while retaining the original means and variances. The procedure
is repeated 100 times for each value of k, each time with a new set of Z values,
and the cash equivalent loss computed. The entire procedure is repeated for
risk tolerances of 25 and 75 to examine how the results vary with investors'
risk tolerance.
Results
Exhibit 3 shows the mean, minimum, and maximum cash equivalent loss over
the 100 iterations for a risk tolerance of 50. Exhibit 4 plots the average eEL
--- page 281 ---

254
V K. Chopra and W T. Ziemba
58
Chopra and Ziemba
EXHIBIT 3:
Cash Equivalent Loss (CEL) for Errors of Different Sizes
k (size of
Parameter
Mean
Min.
Max.
error)
with Error
CEL
CEL
CEL
0.05
Means
0.66
0.01
5.05
0.05
Variances
0.05
0.00
0.34
0.05
Covariances
0.02
0.00
0.25
0.10
Means
2.45
0.01
15.61
0.05
Variances
0.22
0.00
1.39
0.10
Covariances
0.11
0.00
0.66
0.15
Means
5.12
0.15
24.35
0.15
Variances
0.55
0.00
3.35
0.15
Covariances
0.27
0.00
1.11
0.20
Means
10.16
0.17
3609
0.20
Variances
0.90
0.01
4.16
0.20
Covariances
0.47
0.00
1.94
as a function of k. The CEL for errors in means is approximately eleven
times that for errors in variances and over twenty times that for errors in
covariances. Thus, it is important to distinguish between errors in variances
and errors in covariances.:; For example, for k = 0.10, the CEL is 2.45 for
errors in means, 0.22 for errors in variances, and 0.11 for errors in covariances.
Our results on the relative importance of errors in means and variances
are similar to those of Kallberg & Ziemba [1984J. They find that errors in
means are approximately ten times as important as errors in variances and
covariances considered together (they do not distinguish between variances
and covariances).
Our results show that for a risk tolerance of 50 the importance of errors
in covariances is only half as much as previously believed. Furthermore, the
relative importance of errors in means, variances, and covariances depends
upon the investor's risk tolerance.
Exhibit 5 shows the average ratio (averaged over errors of different sizes, k)
of the CELs for errors in means, variances, and covariances. An investor with
a high risk tolerance focuses on raising the expected return of the portfolio
5The result for covariances also applies to correlation coefficients, as the correlations
differ from the covariances only by a scale factor equal to the product of two standard
deviations.
--- page 282 ---

The Effect a/Errors in Means, Variances, and Covariances on Optimal Portfolio Choice
255
The Effect of Errors
59
% Cash
Equivalant lo ..
11,---------------------------~----_,
Means
10
9
8
7
6
5
4
3
2
___ .... __ .... . V.ri.~ce •
... ~_.:_-::::: .... _ ................ Covlnances
O~~--~-*~~~~~~----~----~
o
0.05
0.10
0.15
0.20
Magnituda of error (kl
EXHIBIT 4
Mean percentage cash equivalent loss due to errors in inputs
EXHIBIT 5
A verage Ratio of CELs for Errors in Means, Variances, and Covariances
Risk
Errors in Means
Errors in Means
Errors in Variances
Tolerance versus Variances versus Covariances
25
3.22
5.38
50
1.98
22.50
75
21.42
56.84
versus Covariances
1.67
2.05
2.68
and discounts the variance more relative to the expected return. To this
investor, errors in expected returns are considerably more important than
errors in variances and covariances. For an investor with a risk tolerance of
75, the average CEL for errors in means is over twenty-one times that for
errors in variances and over fifty-six times that for errors in covariances.
Minimizing the variance of the portfolio is more important to an investor
with a low risk tolerance than raising the expected return. To this investor,
errors in means are somewhat less important than errors in variances and
covariances. For an investor with a risk tolerance of 25, the average CEL for
errors in expected returns is about three times that for errors in variances
and about five times that for errors in covariances.
Most large institutional investors have a risk tolerance in the 40 to 60 range.
Over that range, there is considerable difference in the relative importance
of errors in means, variances, and covariances. Irrespective of the level of
risk tolerance, errors in means are the most important, followed by errors
--- page 283 ---

256
V K. Chopra and W T. Ziemba
60
Chopra and Ziemba
in variances. Errors in covariances are the least important in terms of their
influence on portfolio optimality.
Implications and Conclusions
Investors have limited resources available to spend on obtaining estimates of
necessarily unknowable future parameters of risk and reward. This analysis
indicates that the bulk of these resources should be spent on obtaining the
best estimates of expected returns of the asset classes under consideration.
Sometimes, investors using the MV framework to allocate wealth among
individual stocks set all the expected returns to zero (or a non-zero constant).
This can lead to a better portfolio allocation because it is often very difficult
to obtain good forecasts for expected returns. Using forecasts that do not
accurately reflect the relative expected returns of different securities can substantially degrade MV performance.
In some cases it may be preferable to set all forecasts equal. 6 The optimization then focuses on minimizing portfolio variance and does not suffer
from the error-in-means problem. In such cases it is important to have good
estimates of variances and covariances for the securities, as MV optimizes
only with respect to these characteristics.
Of course, if investors truly believe that they have superior estimates of
the means, they should use them. In this case it may be acceptable to use
historical values for variances and covariances.
For investors with moderate to high risk tolerance, the cash equivalent loss
for errors in means is an order of magnitude greater than that for errors in
variances or covariances. As variances and covariances do not much influence
the optimal MV allocation (relative to the means), investors with moderateto-high risk tolerance need not expend considerable resources to obtain better
estimates of these parameters.
References
Bawa, Vijay S., Stephen J. Brown and Roger W. Klein (1979). 'Estimation Risk and
Optimal Portfolio Choice.' Studies in Bayesian Econometrics, Bell Laboratories
Series. North Holland.
6This approach is in the spirit of Stein estimation and is discussed in Chopra, Hensel, and
'Thrner [1993]. As a practical matter, it should be used for assets that belong to the same
asset class. e.g., equity indexes of different countries or stocks within a country. It would
be inappropriate to apply it to financial instruments with very different characteristics; for
example, stocks and T-bills.
--- page 284 ---

The Effect of Errors in Means, Variances, and Covariances on Optimal Portfolio Choice
257
The Effect of Errors
61
Best, Michael J. and Robert R. Grauer (1991). 'On the Sensitivity of Means-
Variance-Efficient Portfolios to Changes in Asset Means: Some Analytical and
Computational Results.' Review of Financial Studies 4, No.2, 315-342.
Chopra, Vijay K. (1991). 'Mean-Variance Revisited: Near-Optimal Portfolios and
Sensitivity to Input Variations.' Russell Research Commentary.
Chopra, Vijay K., Chris R. Hensel and Andrew L. Thrner (1993). 'Massaging
Mean-Variance Inputs: Returns from Alternative Global Investment Strategies
in the 1980s.' Management Science, (July): 845-855.
Dexter, Albert S., Johnny N.W. Yu and William T. Ziemba (1980). 'Portfolio
Selection in a Lognormal Market when the Investor has a Power Utility Function: Computational Results.' In Proceedings of the International Conference
on Stochastic Programming, M.A.H. Dempster (ed.), Academic Press, 507-523.
Freund, Robert A. (1956). 'The Introduction of Risk into a Programming Model.'
Econometrica 24253-263.
Freund, L. and M. Blume (1975). 'The Demand for Risky Assets.' The American
Economic Review, December, 900-922.
Kallberg, Jarl G. and William T. Ziemba (1984). 'Mis-specification in Portfolio
Selection Problems'. In Risk and Capital, G. Bamberg and K. Spremann (eds.),
Lecture Notes in Econometrics and Mathematical Systems. Springer-Verlag.
Klein, Roger W, and Vijay S. Bawa (1976). 'The Effect of Estimation Risk on
Optimal Portfolio Choice. J. of Financial Economics 3 (June), 215-231.
Markowitz, Harry M. (1987) . Mean- Variance Analysis in Portfolio Choice and
Capital Markets. Basil Blackwell.
Michaud. Richard O. (1989). 'The Markowitz Optimization Enigma: is 'Optimized' Optimal?' Financial Analysts Journal 45 (January-February), 31-42.
Ziemba, William T. and Raymond G. Vickson, eds. (1975) Stochastic Optimization
Models in Finance. Academic Press.
--- page 285 ---

This page is intentionally left blank
--- page 286 ---

259
QU(llItilatilie Fillance, Vol. 5, No. 4, August 2005, 343- 355
11 Routledge
~
TayIor& Fraoci' Groop
19
Time to wealth goals in capital accumulation
LEONARD c. MACLEAN*t , WILLIAM T. ZIEMBAt§ and YUMING LI ~
tSchool of Business Administration, Dalhousie University, Halifax, NS, Canada B3H IZ5
t Sauder School of Business, University of British Columbia, Vancouver, BC, Canada V6T IZ2
§Department of Finance, Sloan School of Management, 50 Memorial Drive E52-410,
Massachusetts Institute of Technology, Cambridge, MA 02142-1 347, USA
I. Introduction
-,rSchool of Business, California State University, Fullerton, CA 92834, USA
(Received 26 January 2004; infina/form /5 Apri/ 2005)
This paper considers the problem of investment of capital in risky assets in a dynamic capital
market in continuolls time. The model controls risk, and in particular the risk associated with
errors in the estimation of asset returns. The framework for investment risk is a geometric
Brownian motion model for asset prices. with random rates of return. The information
filtration process and the capital allocation decisions are considered separately. The fi ltration
is based on a Bayesian model for asset prices, and an (empirical) Bayes estimator for current
price dynamics is developed from the price history. Given the conditional price dynamics,
investors allocate wealth to achieve their fi nancial goals efficiently over time. The price updating and wealth reallocations occur when control limits on the wealth process are attained.
A Bayesian fractional Kelly strategy is optimal at each rebalancing, assuming that the risky
assets are jointly lognormal distributed. The strategy minimizes the expected time to the upper
wealth limit while maintaining a high probability of reaching that goal before falling to a
lower wealth limit. The fractional Kelly strategy is a blend of the log-optimal portfolio and
cash and is eq uivalently represented by a negative power utility function, under the multiva riate lognormal distribution assumption. By rebalancing when control limits are reached,
the wealth goals approach provides greater control over downside risk and upside growth. The
wealth goals approach with random rebalancing times is compared to the expected utility
approach with fixed rebalancing ti mes in an asset allocation problem involving stocks, bonds,
and cash.
Keywords: Capital accumulation; Wealth goals; Investment of capital
In capital accumulation under uncertainty, a decisionmaker must determine how much capital to invest in
riskless and risky investment opportunities at each point
in time. The investment strategy yields a stream of capital
over time, with investment decisions made so that
the distribution of wealth has desirable properties.
An investment strategy which has generated considerable
interest is the growth optimal or Kelly strategy, where the
expected logarithm of wealth is maximized (Kelly 1956).
The wealth distribution of this strategy has many attractive characteristics (see e.g. Hakansson 1970, 1971,
Markowitz 1976, Hakansson and Ziemba 1995). As
Breiman (1 960, 1961 ), and Algoet and Cover (1 988)
have shown, the Kelly strategy maximizes the long run
expected rate of growth of capital and minimizes the
expected time to reach a fixed level of wealth for sufficiently large goals under mild conditions. Researchers
such as Thorp (1975), Hausch et al. (1981), Grauer and
Hakansson (1986, 1987), and Mulvey and Vladimirow
(1992) have used the optimal growth strategy to compute
optimal portfolio weights in multi-asset and worldwide
asset allocation problems.
The literature considers the stream of capital foll owing
from an investment policy from either a wealth or a time
perspective. In most situations the expected utility of
accumulated capital at a fixed point in time is analysed.
There is particular interest in the logarithm of accumulated capital, and the corresponding rate of capital
growth. Alternatively, the growth rate can be viewed as
the time it takes for accumulated capital to reach wealth
milestones.
*Correspondi ng author. Email: Imac1ean@mgmt.dal.ca
The distribution of accumulated capital to a fixed
point in time and the distribution of the first passage
Qual/fi/afire Fillallce
ISSN 1469- 7688 print/ISSN 1469- 7696 online © 2005 Taylor & Francis
http://www.tandf.co.uk/journals
DO lo 10.1080/1 4697680500149552
