# The Kelly capital growth investment criterion _ theory and -- Leonard C_ Maclean, Edward O_ Thorp, W_ T_ Ziemba, Leonard -- World Scientific Handbook -- isbn13 9781283148344 -- bec576e26410d0c695fd5b867d08ec4f -- An.pdf — pages 495–514

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
--- page 496 ---

Lifetime Portfolio Selection by Dynamic Stochastic Programming
467
LIFETIME PORTFOLIO SELECTION
241
the risky asset, with 1 - w, going into the safe
asset? Once these optimal portfolio fractions
are known, the constraint of (5) must be
written
C - [W
W.+ 1
]
,-
,- [(l-w,)(I+r) + w,Zd
.
(10)
~ ow we use (to) instead of (4), and recogni:zmg the stochastic nature of our problem
specify that we maximize the expected valu~
of total utility over time. This gives us the
stochastic generalizations of (4) and (5) or
(6)
Mill
T
{C"w,}E ~ (1 +p}-'U[Ct]
(11)
._0
subject to
C, = [Wt _
Wt+l
]
(!+r)(1-w,) +w,Zt
Wo given, W!'+I prescribed.
If there is no bequeathing of wealth at death,
presumably W 2'+1 = O. Alternatively, we could
replace a prescribed W!' +, by a final bequest
functi~n added to (11), of the form B(W2'+l),
and with W 2'+1 a free decision variable to be
chosen so as to maximi:ze (11) + B(WN ,).
For the most part, I shall consider C2' = W T
and W2'+l = O ..
In (11), E stands for the "expected value
of," so that, for example,
E Zt = l"'ztdP(fl,) .
In our simple case of C 9),
1
1
EZt = '2A+ '2,X-I.
Equation (11) is our basic stochastic programming problem that needs to be solved simultaneously for optimal saving-consumption and
portfolio-selection decisions over time.
Before proceeding to solve this problem, reference may be made to similar problems that
seem to have been dealt with explicitly in the
economics literature. First, there is the valuable paper by Phelps on the Ramsey problem
in which capital's yield is a prescribed random
variable. This corresponds, in my notation, to
the (w,} strategy being frozen at some fractional level, there being no portfolio selection
problem. (My analysis could be amplified to
consider Phelps' 5 wage income, and even in
the stochastic form that he cites Martin Beckmann as having analyzed.)
More recently
Levhari and Srinivasan [4] have also treated
the Phelps problem for T =
00 by means of
the Bellman functional equations of dynamic
programming, :and have indicated a proof that
concavity of U is sufficient for a maximum.
Then, there is Professor Mirrlees' important
work on the Ramsey problem with Harrodneutral technological change as a random variable.6 Our problems become equivalent if I
~eplace W. -
W,+I[(l+I')(I-w.) + wtZ.J-1
m (10) by A,j(W,IA t ) -
nW, -
(W'+l - WI)
let technical change be governed by the probability distrihution
Prob {A, ;:;; A,_,Z} = P(Z);
rein.terpret my W, to be Mirrlees' per capita
capital, K,IL" where L t is growing at the natural rate of growth 11.; and posit that AdCW I
At) is a homogeneous first degree, concave, ne~­
classical production function in terms of capital 'and efficiency-units of labor.
It should be remarked that I am confirming
myself here to regular interior maxima and
. .
'
not gomg mto the Kuhn-Tucker inequalities
that easily handle boundary maxima.
Solution of the Problem
The meaning of our basic problem
T
J~(Wo) = Max E ~ (1+p)-t U[C.l
(11)
{C"w.}
,-0 .
subject to C, = W t -
Wt+ 1[(1-w.) (1+1')
+ w,Z.] _1 is not easy to grasp. I act now at
t == 0 to select Co and wo, knowing Wo but not
yet knowing how Zo will turn out. I must act
now, knowing that one period later, knowledge
of Zo's outcome will be known and that W, will
then be known. Depending upon knowledge of
WI, a new decision will be made for C, and
WI. Now I can only guess what that decision
will be.
As so often is the case in dynamic programming, it helps to begin at the end of the planning period. This brings us to the well-known
• E. S. Phelp' [8].
• J. A. Mirrlees [6]. I h~ve canverted his treatment
into a discrete·Ume version. Robert Metton's companion
paper throw. light on Mlrrlees' Brownian-motion model
for A. ••
--- page 497 ---

468
P. A. Samuelson
242
THE REVIEW OF ECONOMICS AND STATISTICS
one-period portfolio problem. In our terms,
this becomes
J1(W2'_d '""'
Max
U[C2'-d
{ C2'-1,W2'_1}
+ E(l+p) - ~V[(W'l'_l- C:r-l)
{(1- W'l'_1}(1+1')
+ WT-1ZT-I}-"'}.
(12)
Here the expected value operator E operates
only on the random variable of the next period
since current consumption C'l'-1 is known once
we have made our decision. Writing the second
term as EF(Z'l') , this becomes
EF(Z",) :=: jF(Z'I')dP(Z",IZ"'_l'Z'l'_'" .. , ZQ)
o
= jF(ZT)dP(ZT), by our indepen:dence
postulate.
In the general case, at a later stage of decision
making, say t = T-l, knowledge will be available of the outcomes of earlier random variables, Z'_Zl • . . ; since these might be relevant
to the distribution of subsequent random variables, conditional probabilities of the form
P(Z"'_l IZ",_" . .. ) are thus involved. However, in cases like the present one, where independence of distributions is posited, conditional probabilities can be dispensed within
favor of simple distributions.
Note that in (12) we have substituted for
C'I' its value as given by the constraint in (11)
or (10).
To determine this optimum (C'l'_l, W T _ 1 ),
we differentiate with respect to each separately,
to get
0= V' (CT-d -
(1+1') -1 EV' [C'I')
(I-WT_tl(1+I') + 2V1'_lZ",_d
(12')
0= EV' [CTJ(WT- 1 -CI'_l) (Z'I'_1-1-r)
= jlf' [(W'I'-I -C2'-I)
o
{(l-wT_l(l+r) -
W'l'- lZT-dJ
(W2'-1-CT- 1 ) (ZT_l-l-r)dP(Z:r_l)
(12")
Solving these simultaneously, we get our
optimal decisions (C""'_l' W""_l) as functions
of initial wealth W 2'-1 alone. Note that if
somehow C"'l'-l were known, (12") would by
itself be the familiar one-period portfolio optimality condition, and could trivially be rewritten to handle any number of alternative
assets.
Substituting (C*T_lt w*T-d into the elCpression to be maximized gives us 11(WT - t ) explicitly. From the equations in (12), we can,
by standard calculus methods, relate the derivatives of U to those of I, namely, by the
envelope relation
J{(W"'_l) = u' [CT-d .
(13)
Now that we know Jt[WTrJ, it is easy to
determine optimal behavior one period earlier,
namely by
12(W'l'-z} =
Max
U[C,,_z]
(C"'_2,WT_'}
+ E(1+p)-IJ1 [(WT _ Z-C"_2)
{(2 -WT_Z) (1+r) + W'l'_ZZ 'l'_2}].
(14)
Differentiating (14) just as we did (11)
gives the fallowing equations like those of (12)
0-- U' [C"-2] -
(l+p)-'EJ,' [WT _ 2 ]
{(1-w'l'_2) (1+r) + W'I'-2ZT_Z}
(IS')
0= EIr' [WT-d (W",_z -
C" _2)(Z"_2 -
1-1')
= [jl' [(W:r-2 -C'l'- Z){(1-WT_2) (I+r)
+ WT_ZZ'I'_2}] (WT- 2 -C:r-2) (Z" _ 2 - 1-,.)
dP(Z'l'_2).
(15")
These equations, which could by (13) be related to U'[CT _ I ], can be solved simultaneously to determine optimal (C*"- 2, W*'I'_2) and
12(WT _ 2 ).
Continuing recursively in this way for 1'- 3,
T-4, ... ,2, 1,0, we finally have our problem
solved. The general recursive optimality equations can be written as
{
0 = V'[Co] - (1+p)-lEI',,_l[WO)
{(l-wo)(l+r) + woZo)
0= EI'T_l[Wr](WO -
Co)(Zo - I-r)
o = U'[C'I'-lJ -
(l+p) -, EJ'T_t(W,]
{(l-w,-d (1+') + Wt_ ,Z,_r}
(l6')
0= EJ''I'_. [W,_l -C._I) (Zt_l - l-r),
(l = 1, ... ,T-1).
(16")
In (16')' of course, the proper substitutions
must be made and the E operators must be
over the proper probability distributions: Solving (16") at any stage will give the optimal
decision rules for consumption-saving and for
portfolio selection, in the form
c*. = ![W.; ZI_1, ... , zoJ
= !",_t[Wt } if the Z's are independently
distributed
--- page 498 ---

Lifetime Portfolio Selection by Dynamic Stochastic Programming
469
LIFETIME PORTFOLIO SELECTION
243
W"'t = g[Wt ; Zt_L, ... , ZoJ
= g",-,[Wtl if the Z'g are independently
distributed.
Our problem is now solved for every case
but the important case of infinite-time horizon.
For well-behaved cases, one can simply let
T -+ 00 in the above formulas. Or, as often
happens, the infinite case may be the easiest of
all to solve, since for it C*t = feW,) , w*. =
g(W,), independently of time and both these
unknown functions can be deduced as solutions
to the foHowing functional equations:
0= V' [f(W)J -
(l+p)-l
Ii'«W - j(W» «1+1')
- g(W)(Z -
1 -
r)}) [(1+1')
- g(W)(Z -
1 -
,»)dP(Z)
(17')
0= fi/'[(w - f(W)}
o
{1 + I' -
g(W) (Z -
1 - r)}]
[Z -
1 -
r).:i p«-)
(17")
Equation (17'), by itself with g(W) pretended
to be known, would be equivalent to equation
(13) of Levha ... i and Srinivasan (4, p. £]. [n
deriving (17')-( 17"), [ have utilized the envelope relation of my (13), which is equivalent to
Levhari and Srinivasan's equation (12) [4,
p.5J.
Bernoulli and Isoelastic Cases
To apply our results, let us consider the interesting Bernoulli case where U = log C. This
does not have the bounded utility that Arrow
[1} and many writers have convinced themselves is desirable for an axiom system. Since
I do not believe that Karl Menger paradoxes
of the generalized St. Petersburg type hold any
terrors for the economist, I have no particular
interest in boundedness of utility and consider
log C to be interesting and admissible. For this
case, we have, from (12) ,
l l (W) = Max 10gC
{C,w}
+E(L+p)-1Iog [(W - C)
{(1-w) (1+1') + wZ} ¥
= MaxlogC + (1+p)-ltog [W-C]
{C}
+ Max jiog [(l-w)(I+r)
o
{w}
+ 14'ZJdP(Z)~
(IS)
Hence, equations (12) and (16')-( 16") split
into two independent parts and the Ramsey-
Phelps saving problem becomes quite indepen- .
dent of the lifetime portfolio selection problem.
Now we have
0= (1/C) -
(l+p)-l (W - C)-lor
C"'_l = (1+p) (2+ p) - lW!'_1
(19')
0= l'(z-l-r)[(I - W) (1+r)
+ 14'Z) - 1 dP(Z) or
14''''_1 = w· independently of W 1'-1.
(19")
These independence results, of the C7'_l and
W7'-I decisions and of the dependence of W7'-l
on W"'_l, hold for an U functions with isoelastic marginal utility. I.e., (16') and (16")
become decomposable conditions for all
V (C) = 1/y C'Y,
y < 1
(20)
as well as for U(C) = log C, corresponding by
L 'Hopi tal's rule to 'Y = o.
To see this, write (12) or (18) as
C'Y
(W-C)'Y
1, (W) = Max '---- + (1+p)-l __
-
(C,w} y
y
j'"[(l-W)(l+r) + wZ}'YdP(Z)
C'Y
(W-C) 'Y
=Max-+(l+p)_l
X
{C} y
y
Max!1(I-W)(1+r)
w
0
+ 14'Zp dp(Z).
(21)
Hence, (I 2") or ( 15") or (16") becomes
.£~[ (1-14') (1+1')
+ 14'Z)'Y-l (Z-r-l) dP (Z) = 0,
(22")
which defines optimal w* and gives
Max l'"[(t-w)U+r) +wZ]'YdP(Zl
{w}
0
= i
"'W- W*) (1+1') + w·Zj'Y dP(Z)
= [l + r*) 'Y, for short.
Here, r* is the subjective or util-prob mean
return of the portfolio, where diminishing marginal utility has been taken into account.7 To
get optimal consumption-saving, differentiate
(21) to get the new form of (12') , (15'), or
( 16')
f See Samuelson and Merton for the utll-prab concept
[131 .
--- page 499 ---

470
P. A. Samuelson
244
THE REVIEW OF ECONOMICS AND STATISTICS
0= C-rt -
(l+p)-1 (1+"*)"1' (W_C)-r-1.
(22')
Solving, we have the consumption decision rule
C*P_l = ~WI'_l
1 + al
where
al = [(l+,,*)-r/(1+p)j1h-1.
Hence, by substitution, we find
I t (Wp _ 1 ) = b1W'1',,_tly
where
hI = a,'1'(I+a'z)-')'
(23)
(24)
(25)
+ (l+p)-1 (1+r*)'1' (l+at)-'Y.
(26)
Thus, I 1(·) is of the same elasticity form as
U ( .) was. Evaluating indeterminate forms for
i' = 0, we find I, to be of log form if U was.
Now, by mathematical induction, it is easy
to show that this isoelastic property must also
hold for
J2 (W"_2), Ja(W,,_a)," "
since,
whenever it holds for J,,(W'l'_ .. ) it is deducible
that it holds for J,,+l(WT_,,_I)' Hence, at
every stage, solving the general equations (16')
and (16"), they decompose into two parts in
the case of isoelastic utility. Hence,
Theorem:
For isoelastic marginal utility functions, U'(C}
= C'1'-I, i' < 1, the optimal portfolio decision
is independent of wealth at each stage and in~
dependent of all consumption-saving decisions,
ieading to a constant w*, the solution to
0= ir. (l-w) (1+,) +WZl"-l(Z- L-,,)dP(Z).
o
Then optimal consumption decisions at each
stage are, for a. no-bequest model, of the form
C"'T_' = CtWI'_1
where one can deduce the recursion relations
at
Cl = ---
I+Wl'
a, = (l+p)/(L+,,*),>,jVl -'1'
(1+,*)'>' = 1'" (I - w*)(l+r)
+ w* Z],>, dP (Z)
alc' _l
c. = ~"::""";--"-
I +alcl-l
al+'t _ I '
1
= l+i '
In the limiting case, as 'Y -+ ° and we have
Bernoulli's logarithmic function, al = (l+p),
independent of 1'*, and all saving propensities
depend on subjective time preference p only,
being independent of technOlogical investment
opportunities (except to the degree that Wt
will itself definitely depend on those opportunities) .
We can interpret 1 +1'* as kind of a "riskcorrected" mean yield; and behavior of a longlived man depends criticaLLy on whether
( 1 +,*) 'Y .2:. (1 + p ), corresponding to al ..:::.. 1.
<
>
(i) For O+r*)'>' = (l+p), one plans always to
wnsumt at a uniform rate, dividingcun~nt W <_, evenly
by remaining life, l/(l+i) . If young enough, one saves
on the average; in the familiar "hump saving" fashion,
one dissaves later as the end comes sufficiently close
into sight.
(ii) For (1+.*)'1' > (l+p), a, < I, and investment
opportunities are, so to speak, so wnpting compared
to psychological time preference that one consumes
nothing at tbe beginning of a long-long life, i.e., rigor.
ously
Lim c. = 0,
~ < 1
i-+ CD
and again hump saving must take place. For O+r*)'1'
> (1+p), the perpetWJJ lifetime problem, with T = "",
is divergent and ill-defined, i.e., /.(W) -> co as i -> 00,
For 'Y";; a and p > 0, this case cannot arise.
(iii) For (1+r*)'1 < (l+p), a, > I, consumption
at very early ages drops only to a limiting positive
fraction (ratber than zero), namely
Lim ~. '" I - I/ d., < I, a, > L
i~ Of.)
Now whether there will be, on the average, initial hump
saving depends upon the size of r* -
c<o' or whether
(l +.*)'1'/1 -,>,
r* - 1 -
>0.
(l+p)l/l - '1'
This ends the Theorem. Although many of
the results depend upon the no-bequest assumption, W,,+l. = 0, as Merton's companion
paper shows (p. 247, this Review) we can easily
generalize to the cases where a bequest func·
tion B'l'(WT + t ) is added to ~?o (l+p)-iU(C t ).
If B'l' is itself of isoelastic form,
B'I' = bT(W N 1)'1' h,
the algebra is little changed. Also, the same
comparative statics put forward in Merton's
continuous-time case will be applicable here,
e.g" the Bernoulli 'Y = 0 case is a watershed
between ca.ses where thrift is enhanced by riskiness rather than reduced; etc.
--- page 500 ---

Lifetime Portfolio Selection by Dynamic Stochastic Programming
471
LIFETIME PORTFOLIO SELECTION
245
Since proof of the theorem is straightforward, I skip all details except to indicate how
the recursion relations for c, and h, are derived,
namely from the identities
b'+lW"!y = J'+l(W)
= Max (C'V/y
C
+ b,(l+~*)'V(l+p)-I(W-C)'V!y}
= (c'V'+1 + b,(1+r*)1'
(l+p) -l(l-C'+ l )1'} W'V/y
and the optimality condition
0 = 0
- 1 -
b,(I+r*)'V(1+p)-1(W-C)'Y- 1
= (£,+IWP- 1 -
6,(1+,..*)1'(1 +p)-1
(1-£i+l)'V-1W'V- 1 ,
which defines C'+1 in terms of bi •
What if we relax the assumption of isoelastic
marginal utility functions?
Then WT ~ J becomes a function of WT - J- 1 (and, of course,
of r, P, and a functional of the probability distribution P). Now the Phelps-Ramsey optimal
stochastic saving decisions do interact with the
optimal portfolio decisions, and these have to
be arrived at by simultaneous solution of the
nondecomposable equations (16') and (16").
What if we have more than one alternative
asset to safe cash? Then merely interpret Z,
as a (column) vector of returns (Z2"za" ... )
on the respective risky assets; also interpret
w, as a (row) vector (W2t,W3" .. . ), interpret
P(Z) as vector notation for
Prob {Z2, ~ Z2, Zs, ~ Z3, ... }
= P(Z2, Z3, ... ) = P(Z) ,
interpret all integrals of the formJG(Z)dP(Z)
as multiple integrals fG(Z2,Z3, . . . )dP(Z2,ZS,
... ). Then (16/1) becomes a vector-set of
equations, one for each component of the vector
Z" and these can be solved simultaneously for
the unknown w, vector.
If there are many consumption items, we
can handle the general problem by giving a
similar vector interpretation to C,.
Thus, the most general portfolio lifetime
problem is handled by our equations or obvious
extensions thereof.
Conclusion
We have now come full circle. Our model
denies the validity of the concept of businessman's risk j for isoelastic marginal utilities, in
your prime of life you have the same relative
risk-tolerance as toward the end of life! The
"cbance to recoup" and tendency for the law
of large numhers to operate in the case of repeated investments is not relevant.
(Note:
if the elasticity of marginal utility, - UI (W) /
WU"(W), rises empirically with wealth, and if
the capital market is imperfect as far 'as lending
and harrowing against future earnings is concerned, then it seems to me to be likely
that a doctor of age 35-50 might rationally
have his highest consumption then, and certainly show greatest risk tolerance then -
in other
words be open to a "businessman's risk." But
not in the frictionless isoelastic model!)
As usual, one expects w* and risk tolerance
to be higher with algebraically large y . One
expects C, to be higher late in life when rand
r'" is high relative to p . As in a one-period
model, one expects any increase in "riskiness"
of Z" for the same mean, to decrease w*. One
expects a similar increase in riskiness to lower
or raise consumption depending upon whether
marginal utility is greater or less than unity in
its elasticity.s
Our analysis enables us to dispel a fallacy
that has been borrowed into portfolio theory
from information theory of the Shannon type.
Associated with independent discoveries by
J. B. Williams [16], John Kelly [2 J, and H. A.
Latane [3] is the notion that if one is investing for many periods, the proper behavior is to
maximize the geometric mean of return rather
than the arithmetic mean. I believe this to be
incorrect (except in the Bernoulli logarithmic
case where it happens 9 to be correct for reasons
• See Merton's cited companion paper in this issue, for
explicit discussion of the comparative statical shifts of (16) 's
C*t and W*t functions as the parameter-> (P, ""'1 Y, r*t and
P(Z) or P(2" ... ) or B(Wr) functions chang~. The s~me
results hold in the discrete·and·continuous-time models.
·S"'- Latane [3, p. lSlJ for explicit recognition of this
point. I find somewhat mystifying his footnote there which
<~y<, "As pointed out to me by Profes5or L. J. Savage (in
correspondence), not only is the maximization of G Ithe
geometric mean) the rule for ma"irnulll •• peeled utility in
connection with Bemoulli's function but (in so far .. certain appro:<imations are permissible) this same rule is approximately valid for all utility functions." [Latane, p. lSI,
n.13.1 The geometric mean crtterion is definitely too c(ln-
!ervati~ to maXltni2C! .an isoelastk utility function corrosponding to positive "; in my equation (20), and it is
definitely too daring to maximize expected utility when
"; < o. Professor Savage has informed m. rec~ntly that his
19M position differs from the view attributed to him in
1959.
--- page 501 ---

472
P A. Samuelson
246
THE REVIEW OF ECONOMICS AND STATISTICS
quite distinct from the Williams-Kelly-Latane
reasoning) .
These writers must have in mind reasoning
that goes something like the following: If one
maximizes for a dista.nt goal, investing and
reinvesting (all one's proceeds) many times on
the way! then the probability becomes great
that with a portfolio that maximizes the geometric mean at each stage you will end up
with a larger terminal wealth than with any
other decision strategy.
This is indeed a valid consequence of the
central limit theorem as appUed to the additive logaritluns of portfolio outcomes. (I.e.,
maximizing the geometric mean is the same
thing as maximizing the arithmetic mean of
the logarithm of outcome at each sta.ge; if at
each stage, we get a mean log of m"'* > m*,
then after a large number of stages we will
have m**T > > m"'T, and the properly normalized probabilities will cluster around a
higher value.)
There is nothing wrong with the logical
deduction from premise to theorem. But the
implicit premise is faulty to begin with, as I
have shown elsewhere in another connection
[Samuelson, 10, p. 3]. It is a mistake to think
that, just because a w** decision ends up with
almost-certain probability to be better than a
w* decision, this implies that w** must yield a
better expected value of utility. Our analysis
for marginal utility with elasticity differing
from that of Bernoulli provides an effective
counter example, if indeed a counter example
is needed to refute a gratuitous assertion.
Moreover, as I showed elsewhere, the ordering
principle of selecting between two actions in
terms of which has the greater probability of
producing a higher result does not even possess
the property of being transitive.10 By that
principle, we could have w*** better than w*"',
and w** better than w*, and also have w*
better than w***.
.. See Sao:nu~Json [Ill.
REFERENCES
[1] Arrow, K. ]., "Aspects of the Theory of Risk·
Bearing" (Helsinld, Finland: Yrjo Jahnssonin
Slilitio, 1965).
[2] Kelly, J., "A New Interpretation of Information
Rate," BeU System Technical Joumal (Aug.
1956),917-926.
[3] Latane, H. A., "Criteria for Choice Among Risky
Ventures," Journal oj Politi.Gn.l Economy 67 (Apr.
1959), 144-155.
[4] Levh2.ri, D. and T. N. Srinivasan, "Optimal Savings Under Uncertainty," Institute for Mathematical Studies in the Sodal Sciences, Technical
Report No.8, Stanford University, Dec. 1967.
[5] Markowitz, H., Portfolio Sekction:
Effid.~nt
Dive1'sificatwn 0/ investment (New York: John
Wiley & Sons, 1959).
[6] Mirrlees, J. A., "Optimum Accumulation Under
Uncertainty," Dec. 1965, unpublished.
[7] Mossin, J., "Optimal Multiperiod Portfolio Policies," JouJ'tuIl of Busin.!ss 41, 2 (Apr. 19611),
215-229.
[8] Phelps, E. S., "The Accumulation of Risky Cap·
ital: A Sequential Utility Analysis," Economet-
T~a 30, 4 (1962), 729-743.
[9] Pratt, J., "Risk Aversion in the Small and in the
Large," Econonutrica 32 (Jan. 1964).
[10] Samuelson, P. A., "General Proof that Diversification Pays," J oUfntil 0/ Pinanciat tind Quantitative
Analysis II (Mar. 1967), 1- 13.
[11] --, "Risk and Un(;ertainty : A Fallacy of
Large Numbers," Sc.~ntUl, 6th. Series, 57th. year
(April-May, 1963).
[12] --, "A Turnpike Refutation of the Golden
Rule in a Welfare Maximizing Many-Year Plan,"
Essay XIV Essays on the Theo,y of Optimal
EGonomi, Growth, Karl Shell (ed.) (Cambridge,
Mass.: MIT Press, 1967).
[13] --, and R. C. Merton, "A Complete Model
of Warrant Pridng that Maximizes Utility," IndustrUll Management Rf!vkw (in pr~).
[14J Tobin, J., "Liquidity Preference as Behavior
Towards Risk," Review of Econom.i& Studies,
XXV, 67, Feb. 1958, 65-86.
[15J --, "The Theol'Y of Portfolio Selection,"
The TMo,y of [merest Rates, F. H. Hahn and
F. P. R. Brechling (eds.) (London: Macmillan,
1965).
[16J Williams, J. B., "Speculation and the Carryover,"
Qut.u'terly Journal of Economics SO (May 1936),
436-455 .
--- page 502 ---

473
32
Models of Optimal Capital Accumulation and Portfolio Selection and
the Capital Growth Criterion*
William T. Ziemba
Professor Emeritus, University of British Columbia, Vancouver, BC
Visiting Professor, Mathematical Institute, Oxford University, UK
ICMA Centre, University of Reading, UK
University of Bergamo, Italy
Raymond G. Vickson
Professor Emeritus, University of Waterloo
Abstract
T his edited and updated excerpt from the Ziemba and Vickson (1975, 2006)
volume discusses various aspects of the history of optimal capital accumulation
and the capital growth criterion, and supplements the introduction to Part IV of
this volume.
1
Optimal Capital Accumulation
Phelps (1962) extended the Ramsey (1928) model of lifetime saving to include uncertainty. In Phelps' problem, the choice in each period was between consumption
and investment in a single risky asset, with the objective being the maximization
of expected utility of life time consumption. Phelps assumed that the utility function was additive in each period's utility for consumption, and he obtained explicit
solutions when each utility function was the same and a member of the isoelastic
marginal utility family. The papers reprinted in Ziemba and Vickson (1975, 2006)
(ZV) and in this volume generalize and extend the work of Phelps in several directions: Portfolio choice is included in Samuelson (1969) and Hakansson (1970, 1971a)
papers, and more general utility functions are treated in Neave (1971b), which is in
ZV. These papers also constitute generalizations of the multiperiod consumptioninvestment papers of Part IV.l
Neave (1971 b) treats the multiperiod consumption-investment problem for a
preference structure given by a sum of utility functions of consumption in different
periods, including a utility for terminal bequests. Future utilities are discounted by
• Reprinted, edited and updated from Ziemba and Vickson (1975, 2006).
lSee Zabel (1973) for an interesting extension of the Phelps-Samuelson-Hakansson model to include
proportional transaction costs.
--- page 503 ---

474
W T Ziemba and R. G. Vickson
an "impatience" factor, compounded in time. The portfolio problem is neglected,
with the only decisions at any time being the amount of wealth to be consumed,
the non-negative remainder being invested in a single risky asset. In each period,
terminal wealth consists of a certain, fixed income plus gross return on investment,
and this terminal wealth becomes initial wealth for the following period, from which
consumption and investment decisions are again to be made, and so forth. Neave
is concerned with conditions under which risk-aversion properties are preserved in
the induced utility functions for wealth. He demonstrates the important result
that the property of non-increasing Arrow-Pratt absolute risk aversion is preserved
under rather general conditions. For inter temporally independent risky returns,
if the single-period utilities for consumption and the utility for terminal bequests
exhibit non-increasing absolute risk aversion, then all the induced utility functions
for wealth also have this property. Mathematically, this result arises from the
fact that convex combinations of functions having decreasing absolute risk aversion
also have this property (see Pratt, 1964, reprinted in ZV). Thus, the decreasing
absolute risk-aversion property is preserved under the expected-value operation,
and is further preserved under maximization. The paper specifically includes the
possibility of boundary as well as interior solutions in the presentation.
Neave (1971b) also considers the behavior of the Arrow-Pratt relative riskaversion index of induced utility for wealth. He presents sufficient conditions under
which the property of non-decreasing relative risk aversion is preserved. Since this
property is not, in general, preserved under convex combinations, results can be obtained only under special conditions. Unfortunately, these conditions are not easily
interpreted, and involve the specific values of the optimal decision variables as well
as the properties of the utility functions. In general, however, non-decreasing relative risk aversion obtains for sufficiently large values of wealth. In ZV's Exercise
V-ME-6, the reader is asked to attempt to widen Neave's classes of utility functions
that generate desirable risk-aversion properties for the induced utility functions.
Neave also relates properties of the relative risk-aversion measures to wealth elasticity of demand for risky investment. Arrow (1971) performed a similar study in
the context of choice between a risk-free and a risky asset, with no consumption. In
this case, the choice is between consumption and risky investment, with no risk-free
asset. Neave shows that if the utilities for consumption and terminal wealth in any
period exhibit constant relative risk aversion equal to unity, then the wealth elasticity for risky investment in that period is also equal to unity. He further shows that
the wealth elasticity of risky investment exceeds unity if and only if the relative
risk-aversion index of expected utility for wealth is less than or equal to that of
utility for consumption in the relevant period.
Samuelson (1969) studies the optimal consumption-investment problem for an
investor whose utility for consumption over time is a discounted sum of single-period
utilities, with the latter being constant over time and exhibiting constant relative
risk aversion (power-law functions or logarithmic functions). Samuelson assumes
--- page 504 ---

Models of Optimal Capital Accumulation
475
that the investor possesses in period t an initial wealth W t which can be consumed
or invested between two assets. One of the assets is safe, with constant known
rate of return r per period, while the other asset is risky, with known probability
distribution of return Zt in period t. The Zt are assumed to be intertemporally
independent and identically distributed. Samuelson thus generalizes Phelps' model
to include portfolio choice as well as consumption.
Terminal wealth Wt + 1 in period t consists of gross return on investment, and
becomes initial wealth governing the consumption-investment decisions in period
t + 1. The problem is to determine the fraction of wealth to be consumed and
the optimal mix between riskless and risky investment in each period (given an
initial wealth wo), so as to maximize expected utility of lifetime consumption. The
usual backward induction procedure of dynamic programming yields a sequence
of induced single-period utility functions Ut for terminal wealth in period t, with
optimal consumption and investment in period t being determined by maximizing
expected utility of consumption plus terminal wealth. Assuming interior maxima
in each period, a recursive set of first-order conditions is derived for the optimal
consumption-investment program.
The explicit form of the optimal solution is derived for the special case of utility
functions having constant relative risk aversion. Samuelson shows that the optimal
portfolio decision is independent of time, of wealth, and of the consumption decision
at each stage. This optimal portfolio is identical with the optimal portfolio resulting from the investment of one dollar in the two assets so as to maximize expected
utility of gross return, using the instantaneous utility for consumption as the "utility
for wealth" function in the optimization procedure. Furthermore, in each period,
the optimal amount to consume is a known fraction of initial wealth in the period,
with the optimal fraction being dependent only on the subjective discount factor
for consumption over time, the return on the risk-free asset, the probability distribution of risky return, and the relative risk-aversion index. For logarithmic utilities,
the optimal consumption fraction further simplifies to a function of the subjective
discount factor alone, and is independent of the asset returns.
Samuelson utilizes his solutions to analyze optimal consumption and investment
behavior as a function of time of life. As observed above, the optimal mix of
riskless versus risky investment is (for constant relative risk aversion) completely
independent of time of life. Samuelson relates the optimal consumption over time to
the asset returns and the subjective discount factor, and discusses conditions under
which the consumer-investor will save during early life and dissave in old age.
Throughout the paper, Samuelson assumes the validity of interior maxima in
the optimization problems. The validity of such an assumption in the multiperiod
portfolio problem was seriously questioned in Hakansson (1970, 1971a), and in ZV-
Exercises including IV-CR-3, 5, and 6. When consumption decisions are included, as
they are in the present case, the question of boundary solutions is presumably even
more important than it was in the pure investment case. The reader may wish to
--- page 505 ---

476
W T. Ziemba and R. G. Vickson
ponder whether these considerations can materially affect Samuelson's conclusions.
ZV-Exercise V-CR-16 shows that a stationary policy is not optimal in a multiperiod
mean-variance model even under strong independence assumptions.
Hakansson (1970) studies a generalization of the problem treated by Samuelson
(1969). Hakansson's assumptions regarding utility for consumption are identical to
Samuelson's, except for an assumed infinite lifetime. The investment possibilities
facing Hakansson's investor are, however, more general. The individual is assumed
to possess a (possibly negative) initial capital position plus a non-capital steady
income stream which is known with certainty. In each period, borrowing and lending
at a known, time-independent rate of interest, and investment in a number of risky
assets with known joint distribution of returns, are possible. The risky asset returns
are assumed to be independent identically distributed (iid) over time. It is further
assumed that a subset of the risky assets may be sold short. In each period, initial
wealth to be consumed and invested consists of the certain income plus gross return
on the previous period's investment. The objective is maximization of the expected
utility of consumption over an infinite lifetime.
Hakansson introduces two important and apparently realistic constraints on the
risky returns and the investor's decision variables. The capital market is assumed
to impose a so-called no-easy-money restriction on the risky asset returns. This
restriction ensures that no mix of risky assets exists, which provides with probability 1 a return exceeding the risk-free rate, and that no mix of long and short
sales exists, which guarantees against loss in excess of the riskfree lending rate.
The consumption-investment decision variables are assumed to satisfy the so-called
solvency constraint. This requires that the investor always remain solvent with
probability 1, i.e., that in any period t, the investor's initial capital position plus
the capitalized value of the future income stream be non-negative with certainty.
Hakansson uses the familiar Bellman backward induction procedure of dynamic
programming to set up a functional equation for the optimal return function (i.e.,
the maximum expected utility of present and future consumption, given any value
of initial wealth). Since the risky returns are iid and the lifetime infinite, the functional equation obtained is stationary over time: The optimal decision variables
in period t depend only on initial wealth (in period t), on the single-period asset
returns, and on the relative risk-aversion index of consumption. Hakansson's treatment of the infinite horizon dynamic programming problem is intuitively plausible,
but not wholly satisfactory from a rigorous standpoint. (The results are correct,
however.) First, he assumes that the optimal return function exists and satisfies
the functional equation; in a totally rigorous development, these facts need proof.
Next, he verifies the form of the optimal solution by direct substitution, that is, by
showing that the assumed form of solution actually solves the functional equation.
Here the question of uniqueness arises, and is not treated satisfactorily in the development. One way of treating the problem rigorously would be to deal first with
the finite horizon problem (as Samuelson does) and subsequently go to the infinite
--- page 506 ---

Models of Optimal Capital Accumulation
477
horizon limit. At each stage in the finite horizon backward induction procedure,
one would have a functional equation similar to Hakansson's (but rigorously justified). As shown in the paper, the decision variable feasibility region defined by
the solvency constraint is compact and convex, and (as in Hakansson's proof of his
lemma, and its corollaries) the functional equation has a finite, unique solution. By
considering the limiting behavior of the optimal solution and optimal return function, the given infinite horizon results could be justified. For the case of a power-law
utility function unbounded from above, Hakansson needs a restriction on the utility
function parameters, the optimal risky asset returns, and the subjective discount
factor, in order to obtain a solution. In a limiting argument as outlined above, such
a restriction would be required in order to obtain a finite return function in the
limit of infinite horizon.
For constant relative risk-aversion utilities, the form of the optimal solution is (i)
a fixed fraction of initial wealth plus capitalized future income is consumed in each
period; and (ii) a fixed proportion of initial wealth plus capitalized future income
is invested in each of the risky assets, with the optimal asset proportions being
independent of time, initial wealth, capitalized income stream, and impatience to
consume. The remainder of initial wealth is invested in the risk-free asset. For
logarithmic utilities, the optimal consumption fraction is completely independent
of all asset returns, and is a function only of the impatience factor. Hakansson
also considers the interesting case of constant absolute risk aversion (exponential
utilities) , and states without proof the form of the optimal policy under special
restrictions. The conditions required for the solution and the form of the optimal
policy are more difficult to interpret than the corresponding results for the constant
relative risk-aversion case. The reasons for this different behavior in the two classes
of utilities may be understood as follows. For a power-law (or logarithmic) utility,
expected utility of terminal wealth decomposes into a product (or sum) of utility of
initial wealth and expected utility of rate of return on one dollar of investment (since
terminal wealth equals initial wealth times rate of return). Such a factorization does
not obtain for exponential utilities. See ZV Exercise IV-CR-3 for a clarification of
this point in a simple example.
A number of conclusions regarding consumption and investment behavior are
derived as corollaries to the optimal solution. As stated previously, the optimal
level of consumption is a fixed fraction of initial wealth plus capitalized future income. Furthermore, the optimal amount of consumption increases with increasing
impatience to consume, as expected. The optimal solution is such that the individual borrows when poor and generally lends when rich. Additional behavioral
implications of the solutions are discussed in the paper.
In the Samuelson-Hakansson additive utility models of this section, the individual's consumption versus saving and investment behavior may vary as a function
of time of life, but attitudes toward risk do not. In these models, the same risky
portfolios are chosen in youth and in old age. In ZV-Exercise V-ME-21, a multiplica-
--- page 507 ---

478
W T. Ziemba and R. G. Vickson
tive utility model, based on Pye (1972) , is developed. In this model, risk aversion
in portfolio selection increases or decreases with age according as risk tolerance is
greater or less than that of the logarithmic utility function. Logarithmic utility is a
member of both the additive and multiplicative families. In the multiplicative family, risk aversion in portfolio selection depends on impatience to consume as well as
on age. The multiplicative family thus allows greater richness in portfolio selection
behavior over time. On the other hand, consumption behavior over time is simpler
in the multiplicative model: Given the impatience factor and the length of remaining life, the propensity to consume is identical for all members of the multiplicative
family, and is independent of present and future investment opportunities. Furthermore, in the infinite horizon limit, portfolio selection behavior changes over time,
but consumption behavior does not: A constant fraction of wealth is consumed in
every period.
To summarize, these papers show that an optimal lifetime consumptioninvestment program is simple to calculate for additive utilities belonging to the
constant relative risk-aversion family. The optimal portfolio remains unchanged
throughout life for asset returns which are iid over time. Consumption in any
period is always proportional to wealth (including capitalized future income), the
proportionality factor being dependent in general on impatience to consume, on the
capital market, and possibly also on time of life. The optimal portfolio and the optimal consumption fraction are easily determined by solving a static, one-period, pure
portfolio problem using utility for consumption as the appropriate utility for wealth
function. Effects due to age-dependent risk aversion can be incorporated through
a multiplicative form of utility function. In this case, the optimal consumption
program may be calculated (in the absence of exogenous income, at least) without
solving any "optimization" problem and without reference to the capital market.
Optimal portfolio choice depends on time, however, and must be continually recalculated in successive periods. In both the additive and multiplicative cases, a useful
form of myopia obtains: In each period, past or future realized random outcomes
need not be known in choosing the optimal portfolio, and past outcomes affect
present consumption decisions only by fixing the available wealth.
Some of the conclusions would remain unchanged under a slight weakening of
hypotheses. In particular, the assumption of identically distributed asset returns
over time may be dropped (while retaining independence). For additive utilities
having constant relative risk aversion, the optimal amount of consumption will still
be proportional to wealth. The relative risk aversion of induced utility for wealth
will remain constant over time. The optimal asset proportions at any time t will be
independent of wealth, consumption, and past or future asset returns, and will depend only on the nature of the capital market at time t. Calculation of the optimal
consumption fraction at time t will, however, generally require the solution of all
"future" consumption and portfolio problems, and will thus be much more complex
than in the iid case. Hakansson (1971b) studied a significant generalization of his
--- page 508 ---

Models of Optimal Capital Accumulation
479
model where the individual's impatience is variable, his lifetime is stochastic, and
the capital assets (both risk free and risky) change in time. The individual consumes, borrows (or lends), invests in risky assets, and purchases life insurance. For
additive utilities having constant relative risk aversion, solutions are obtained for
the optimal lifetime consumption, investment, and insurance-buying program. For
logarithmic utilities, Miller (1974ab) analyzed the optimal consumption strategies
over an infinite lifetime with a stochastic (possible nonstationary) income stream
and a single, safe asset. Rentz (1971, 1972, 1973) has analyzed optimal consumption and portfolio policies with life insurance, for stochastic lifetimes and changing
family size. Additional extensions are in Hakansson (1969), Long (1972), and Neave
(1971a).
2
The Capital Growth Criterion
The papers by Breiman and Thorp are concerned with Kelly's capital growth criterion for long-term portfolio growth. The criterion states that in each period one
should allocate funds to investments so that the expected logarithm of wealth is
maximized. Hence, the investor behaves in a myopic fashion using the stationary
logarithmic utility function and the current distribution of wealth.
Kelly (1956) supposed that the maximization of the exponential rate of growth
of wealth was a very desirable investment criterion. Mathematically the criterion
is the limit as time t goes to infinity of the logarithm of period t's wealth relative
to initial wealth divided by t. If one considers Bernoulli investments in which a
fixed fraction of each period's present wealth is invested in a specific favorable
double-or-nothing gamble, then the criterion is easily shown to be equivalent to the
maximization of the expected logarithm of wealth. ZV Exercise V-CR-18 illustrates
the calculations involved and related elementary properties of Kelly's criterion.
The desirability of Kelly's criterion was further enhanced when Breiman
[Breiman (1961) and his 1960 article reprinted here] showed that the expected log
strategy produced a sequence of decisions that had two additional desirable properties. First, if in each period two investors have the same investment opportunities
and one uses the Kelly criterion while the other uses an essentially different strategy
(i.e., the limiting difference in expected logs is infinite), then in the limit the former
investor will have infinite times as much wealth as the latter investor with probability 1. Second, the expected time to reach a pre-assigned goal is asymptotically
(as the goal increases) least with the expected log strategy. Latane (1959) provided
an earlier intuitive justification of the first property.
Breiman (1961) established these results for discrete intertemporally independent identically distributed random variables. In this case, as in the Bernoulli case,
a stationary policy is optimal. In ZV Exercise V-ME-22, the reader is asked to
develop these and related results for the Bernoulli case. The main technical tool
involved in the proof is the Borel strong law of large numbers, which states that
--- page 509 ---

480
W T Ziemba and R. G. Vickson
with probability 1 the limiting ratio of the number of successes to trials equals the
Bernoulli probability of a success. Breiman's paper reprinted here proves the first
result for positive bounded random variables. Results from the theory of martingales form the basis of proof of his conclusions. ZV Exercise V-CR-19 provides the
reader with some elementary background on martingales. The reader is asked in
ZV Exercise V-CR-20 to consider some questions concerning Breiman's analysis.
The proof of the results in Breiman's paper involves difficult and advanced mathematical tools. ZV Exercise V-ME-23 shows how similar results may be proved in
a simple fashion using the Chebychev inequality. The crucial assumption is that
the variance of the relative one-period gain be finite in every investment period.
Breiman's assumption that the random returns are finite and bounded away from
zero is sufficient but not necessary for the satisfaction of this assumption. ZV Exercise V-CR-22 presents an extension of Breiman's model to allow for more general
constraint sets and value functions. The development extends his Theorem 1 and
indicates that no strategy has higher expected return than the expected log strategy in any period. The model applies to common investment circumstances that
include borrowing, transactions and brokerage costs, taxes, possibilities. of short
sales, and so on. In ZV Exercise V-ME-24, the reader is invited to consider the relationship between properties 1 and 2, to attempt to verify the validity of property
2 for Breiman's model reprinted here, and to consider the discrete asset allocation
case.
Thorp's paper provides a lucid expository treatment of the Kelly criterion and
Breiman's results. He also discusses some relationships between the max expected
log approach and Markowitz's mean-variance approach. In addition, he points out
some of the misconceptions concerning the Kelly criterion, the most notable being
the fact that decisions that maximize the expected log of wealth do not necessarily
maximize expected utility of terminal wealth for arbitrarily large time horizons. The
basic fallacy is that points that maximize expected log of wealth do not generally
maximize the expected utility of wealth if an investor has nonlogarithmic utility
function; see ZV Exercise V-ME-25 for one such example and Thorp and Whitley
(1973) for a general analysis. See Markowitz (1976) for a refutation, in a limited
sense, of the fallacy if the investor's utility function is bounded. For some enlightening discussion of this and other fallacies in dynamic stochastic investment analysis
see Merton and Samuelson (1974) and ZV Exercise V-ME-26. Miller (1974b) shows
how one can avoid the fallacy altogether by utilizing what is called the utility of
an infinite capital sequence criterion. Under this criterion, the investor's utility is
assumed to depend only on the wealth levels in one or more periods infinitely distant from the present; that is, capital is accumulated for its own sake, namely its
prestige. In this formulation, the time and expectation limit operators are reversed
(from the conventional formulation) and hence the improper limit exchange that
yields the fallacy does not need to be made. One disadvantage of this formulation
is that the admissible utility functions generally are variants of the unconventional
--- page 510 ---

Models of Optimal Capital Accumulation
481
form: limit infimum of the utility of period t's wealth. The reader is invited in ZV
Exercise V-CR-21 to consider some questions concerning Thorp's paper. In ZV Exercise V-ME-27, the reader is asked to determine whether good decisions obtained
from other utility functions have a property "similar" to the expected log strategy
when they produce infinitely more expected utility.
For additional discussion and results concerning the Kelly criterion the reader
may consult Aucamp (1971), Breiman (1961), Dubins and Savage (1965), Goldman
(1974) , Hakansson (1971a,b,d) , Hakansson and Miller (1972), Jen (1971, 1972),
Latane (1959, 1972), Markowitz (1976), Roll (1972), Samuelson (1971) , Merton
and Samuelson (1974) , Thorp (1969), Young and Trent (1969), and Ziemba (1972b).
For an elementary presentation of the theory of martingales the reader may consult
Doob (1971). More advanced material may be found in the work of Breiman (1968),
Burrill (1972), and Chow et al. (1971).
The highly technical Merton paper discusses the optimal consumption technical
investment problem in continuous time. Because of its heavy reliance on stochastic
differential equations and stochastic optimal control theory, the paper may be quite
intimidating upon first reading. To make the paper intelligible to readers unfamiliar
with these mathematical concepts, we deviate from our previous policy of keeping
formalism out of the introduction: Appendix A contains a brief, intuitive introduction to stochastic differential equations and stochastic control theory. Although not
rigorous, the arguments are, hopefully, sufficiently plausible as to enable the reader
to understand Merton's paper with relative ease.
Merton assumes the investor's utility for lifetime consumption to be an integral of
utilities for instantaneous consumption over time. This is a natural, continuous-time
version of the additive utility assumption in discrete time. The general formalism
of the optimal control problem is outlined first for utilities that vary arbitrarily
in time and is specialized in later sections to the pure "impatience" case, as in the
Samuelson and Hakansson discrete time models. Most of Merton's explicit solutions
pertain to utility functions of the hyperbolic absolute risk aversion (HARA) class,
that is, to the class where the reciprocal of the Arrow-Pratt absolute risk-aversion
index is linear in wealth. This class contains as special cases utilities having constant
absolute or relative risk aversion. The individual must decide at each point in time
how to allocate his existing wealth to between consumption and investment in a
number of financial assets. The risky asset returns are governed by a known Markov
process. The objective is maximization of expected utility of lifetime consumption,
including terminal bequests.
In the spirit of dynamic programming, there exists at each time t a derived utility function for wealth w, namely, the maximum expected utility of future lifetime
consumption given that wealth is w at time t. The instantaneous consumptioninvestment problem requires the maximization of utility of consumption and terminal wealth at time t, or rather, at an "infinitesimal" time later than t. For
risky asset returns governed by a stationary log-normal process (see Appendix A),
--- page 511 ---

482
W. T. Ziemba and R. G. Vickson
terminal wealth at the end of the "infinitesimal" time span is almost deterministic.
The expected utility maximization thus involves only means and variances of risky
returns, as in the Samuelson paper in Part III, Chapter 1. The portfolio selection
aspect of the continuous-time consumption-investment problem is thus solved exactly using mean-variance analysis. As in the Lintner and Ziemba papers in Part
III, this implies that the optimal portfolio possesses the mutual fund separation
property: All investors will choose a linear combination of two composite assets,
which are, moreover, independent of individual preferences. If there exists a riskfree asset, it may be chosen as one of the mutual funds, and all portfolios reduce
to a mix of this risk-free asset and a single composite risky asset which is the same
for all investors. The returns on the mutual fund are also governed by a stationary
log-normal process. Note that such a result is only true in continuous time.
In discrete time, a non-negative linear combination of log-normally distributed
random returns is not log-normally distributed. Through the use of a continuoustime formulation, the consumption-investment problem is thus reduced to a twoasset model with consumption. Using this reduction, Merton obtains explicit solutions for the optimal consumption-investment program for utility functions of the
HARA class. As in the papers of Part V, the optimal amount of consumption
and the optimal amount of investment are linear functions of wealth. Furthermore,
when a steady noncapital income stream is included, this remains true with "wealth"
reinterpreted as present wealth plus future income (capitalized at the risk-free rate
of return).
Merton discusses the effects on optimal consumption and investment due to
the possibility of large but rare random events. Specifically, among such rare but
significant events which he discusses are: (1) a bond which is otherwise risk free,
may suddenly become worthless, or (2) the investor dies. The modeling of such
processes in continuous time is achieved through the use of Poisson differential
equations (see Appendix A). Merton derives the optimal consumption-investment
policy for choice between a log-normally distributed common stock and a "suddenly
worthless" bond, for utilities having constant relative risk aversion. As before, the
optimal amount of consumption is linear in wealth. The optimal investment in
the common stock is an increasing function of the probability of bond default, as
expected. Merton also discusses the effect of uncertain lifetime, using a stationary
Poisson process to model the arrival of the consumer's death. He shows that the
optimal consumption-investment problem in this case (with no bequests) is identical
to that of an infinite-lifetime model, with the consumer's utility discounted by a
subjective rate of time preference equal to the reciprocal of life expectancy.
There are a number of other topics covered in the paper, which we mention
only briefly. These pertain to the important and usually neglected question of
nonstationary random asset returns. Merton presents solutions for the optimal
consumption-investment problem in three such nonstationary models. In the first
model, he assumes there exists an asymptotic, deterministic price curve pet) , toward
--- page 512 ---

Models of Optimal Capital Accumulation
483
which the stochastic asset prices tend (in expected value) in the distant future. In
the second model, he assumes that the risky return is given by a log-normal distribution whose mean is itself a random process of a special form. Finally, in the third
model, he assumes that the risky return is given by a stationary log-normal process whose parameters are unknown, but must be estimated from past behavior of
the random variable. Explicit solutions for these three models are obtained in a
two-asset setting, for utility functions having constant absolute risk aversion.
ZV Exercise V-ME-28 considers a deterministic continuous-time consumptioninvestment model. If utility is intertemporally additive, then it is possible to
develop explicit optimality criteria that yield an algorithm for constructing an
optimal policy.
References
Arrow, K. J. (1971). Essays in the Theory of Risk Bearing. Chicago: Markham Publishing.
Aucamp, D. C. (1971). A new t heory of optimal investment. Working Paper, Southern
Illinois University.
Breiman, L. (1961). Optimal gambling system for favorable games. Proceedings of the 4th
Berkeley Symposium on Mathematical Statistics and Probability, 1, 63- 8.
Breiman, L. (1968). Probability. MA: Addison-Wesley, Reading.
Burrill, C. W. (1972). Measure, Integration and Probability. NY: McGraw-Hill.
Chow, Y. S. (1971) . Great Expectations: The Theory of Optimal Stopping. MA: Houghton,
Boston.
Doob, J. L. (1971). What is a Martingale? AMM, 78, 451- 462.
Dubins, L. and L. Savage (1965). How to Gamble if You Must. NY: McGraw-Hill.
Goldman, M. B. (1974). A negative report on the "near optimality" of the max-expected log
policy and appled to bounded utilities for long-lived programs. Journal of Financial
Economics, 1, 97- 103.
Hakansson, N. H. (1969). Optimal investment and consumption strategies under risk, an
uncertain lifetime, and insurance. International Economic Review, 10, 443- 466.
Hakansson, N. H. (1970). Optimal investment and consumption strategies under risk for
a class of utility functions. Econometrica, 38, 587- 607.
Hakansson, N. H. (1971a). Capital growth and the mean-variance approach to portfolio
selection. JFQA , 6, 517- 557.
Hakansson, N. H. (1971b). Mean-variance analysis of average compound returns. Working
Paper, University of California, Berkeley.
Hakansson, N. H. (1971c). On optimal myopic portfolio policies, with and without serial
correlation of yields. The Journal of Business, 44, 324- 334.
Hakansson, N. H. (1971d) . Optimal entrepreneurial decisions in a completely stochastic
environment. Management Science, 17, 427- 449.
Hakansson, N. H. and B. L. Miller (1972). Compound-return mean-variance efficient portfolios never riskruin. Working Paper No.8, Research Program in Finance, Graduate
School of Business Administration, University of California, Berkeley.
Jen, F. (1971) . Multi-period portfolio strategies. Working Paper No. 108. State University
of New York, Buffalo.
Jen, F . (1972). Criteria in multi-period portfolio decisions. Working Paper No. 131. State
University of New York, Buffalo.
--- page 513 ---

484
W T. Ziemba and R. G. Vickson
Kelly, Jr., J. R. (1956). A new interpretation of the information rate. Bell System Technical
Journal, 35, 917- 926.
Latane, H. (1959). Criteria for choice among risky ventures. Journal of Political Economy,
67, 144- 155.
Latane, H. A. (1972). An optimum growth portfolio selection model. In G. Szego and
K. Shell (Eds.), Mathematical Methods in Investment and Finance, pp. 336- 343.
Amsterdam: NorthHolland.
Lintner, J. (1975). The valuation of risk assets and the selection of risky investments in
stock portfolios and capital budgets. In W. T. Ziemba and R. G. Vickson (Eds.) ,
Stochastic Optimization Models in Finance, pp. 131- 155. NY: Academic Press.
Long, Jr, J. B. (1972). Consumption-investment decisions and equilibrium in the securities market. In M. C. Jensen (Ed.) , Studies in the Theory of Capital Markets,
pp. 146- 222. New York: Praeger.
Markowitz, H. M. (1976). Investment for the long run: New evidence for an old rule.
Journal of Finance, 31(5) , 1273- 1286.
Merton, R. C. and P. A. Samuelson (1974). Fallacy of the log-normal approximation to optimal portfolio decision-making over many periods. Journal of Financial Economics,
1, 67- 94.
Miller, B. L. (1974a) . Optimal consumption with a stochastic income stream. Econometrica, 42, 253- 266.
Miller, B. L. (1974b) . Optimal portfolio decision making where the horizon is infinite.
Working Paper, Western Management Science Institute, University of California,
Los Angeles.
Neave, E. H. (1971a) . Multiperiod consumption-investment decisions and risk preference.
Working paper, Queen's University, Kingston, Ontario, Canada.
Neave, E. H. (1971b). Optimal consumption-investment decisions and discrete-time dynamic programming. Journal of Economic Theory, 3, 40-53.
Phelps, E . S. (1962) . The accumulation of risky capital: A sequential utility analysis.
Econometrica, 30, 729- 743.
Pratt, J. W. (1964) . Risk aversion in the small and the large. Econometrica, 32, 122-136.
Pye, G. (1971) . Minimax policies for selling an asset and dollar averaging. Management
Science, 17, 379- 393.
Ramsey, F . P. (1928) . A mathematical theory of saving. Economic Journal, 38, 543-559.
Rentz, W . F . (1971). Optimal consumption and portfolio policies. Unpublished dissertation, University of Rochester, Rochester, New York.
Rentz, W. F . (1972). Optimal multi-period consumption and portfolio policies with life
insurance. Working Paper No. 72-36, Graduate School of Business University of
Texas, Austin.
Rentz, W . F . (1973) . The family's optimal multi period consumption, term insurance and
portfolio policies under risk. Working Paper No. 73-20. Graduate School of Business,
University of Texas, Austin.
Roll, R. (1972). Evidence on the 'growth-optimum' model. Journal of Finance, 28,
551- 566.
Samuelson, P. A. (1969). Lifetime portfolio selection by dynamic stochastic programming.
Review of Economics and Statistics, 51 , 239-246.
Samuelson, P. A. (1971). The fallacy of maximizing the geometric mean in long sequences
of investing or gambling. Proceedings National Academy of Science, 68, 2493- 2496.
Thorp, E. O. (1969). Optimal gambling systems for favorable games. Review of the International Statistical Institute, 37(3), 273- 293.
--- page 514 ---

Models of Optimal Capital Accumulation
485
Thorp, E. O. and R. Whitley (1973). Concave utilities are distinguished by their optimal strategies. Working Paper, Mathematics Department, University of California,
Irvine.
Young, W. E. and R . H. Trent (1969). Geometric mean approximations of individual
security and portfolio performance. JFQA , 4, 179- 199.
Zabel, E. (1973). Consumer choice, portfolio decisions and transaction costs. Econometrica,
44, 321- 335.
Ziemba, W. T. (1972). Note on optimal growth portfolios when yields are serially
correlated. JFQA , 7, 1995- 2000.
Ziemba, W. T. and R. G. Vicks on (Eds.) (1975). Stochastic Optimization Models in
Finance. NY: Academic Press.
Ziemba, W. T. and R. G. Vicks on (Eds.) (2006). Stochastic Optimization Models in
Finance, (2 ed.) . Singapore: World Scientific.
