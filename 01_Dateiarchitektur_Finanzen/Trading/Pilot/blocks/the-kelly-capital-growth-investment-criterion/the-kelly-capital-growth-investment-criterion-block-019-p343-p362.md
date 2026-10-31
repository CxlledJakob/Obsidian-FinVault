# The Kelly capital growth investment criterion _ theory and -- Leonard C_ Maclean, Edward O_ Thorp, W_ T_ Ziemba, Leonard -- World Scientific Handbook -- isbn13 9781283148344 -- bec576e26410d0c695fd5b867d08ec4f -- An.pdf — pages 343–362

--- page 343 ---

316
S. Browne
OPTIMAL PORTFOLIO STRATEGIES
477
To show explicitly why no policy obtains optimality for the model treated here, and
how we may construct to-optimal strategies, we will first consider the following
problem: for any point b in the danger-zone, i.e., with a < x < b < clr, we will find
the optimal policy to maximize the probability of hitting b before a. For b strictly less
than clr, an optimal policy does exist for this problem, and we will identify it in the
following theorem. To that end let
V( x: a, b) = SUpPx(7! > Tn, and let N = arg sup PAT! > 7{).
~?
~?
THEOREM 3.1.
The optimal policy is to invest, at each wealth level a < x < b, the
state dependent amount
(20)
f;(x) = ~2~r(7:-x).
The optimal value junction is
(21)
(c - ra r
/ r + 1 -
(c _ 7X)y/ r +l
Vex : a, b) =
(
)y/ r+!
(
b)y/r +"
fora:s x:s b,
c-ra
-
c-r
where 'Y is defined by (8).
REMARK 3.1.
Note that the policy of (20) invests less as the wealth gets closer to
the goal b. In fact, it invests a constant proportion of the distance to the "safe point"
clr, regardless of the value of the goal b, and the bankruptcy point a. It is interesting to
observe that while here this constant proportion is independent of the underlying
diffusion parameter (T 2, this does not hold when there are multiple risky stocks in
which to invest in (see §5 beloW). The constant proportion is greater (less) than 1 as
~/r < ( »
3. Thus it is interesting to observe that as the wealth gets closer to the
bankruptcy point, a, the optimal policy does not " panic" and start investing an
enormous amount, rather the optimal policy stays calm and invests at most f:(a) =
2(c - ra)/( ~ - d. The investor does get increasingly more cautious as his wealth
gets closer to the goal b. (This behavior should be compared with the "timid" vs.
"bold" play in the discrete-time problems considered in the classic book of Dubins
and Savage 1965. See also Majumdar and Radner 1991 and Roy 1995.)
Observe further that the investor is borrowing money to invest in the stock only
when x < 2cl(jl + r) but not when 2c/(~ + r) <x < clr. This can be seen by
observing directly that in the former case N(x) > x and in the latter case f:(x) < x.
(The fact that 2c/( jl + r) < clr follows from the assumption that ~ > r.)
PROOF.
While we could prove Theorem 3.1 from a more general theorem in
Pestien and Sudderth (1985) (see also Pestien and Sudderth 1988) which we will
discuss later (see Remark 3.4 beloW), recognize that this is simply a special case of the
control problem solved in Theorem 2.1 for I = a, U = b with A = 0, g = 0 and
h(b) = 1, h(a) = O. As such the nonlinear Dirichlet problem of (9) for the optimal
value function V becomes in this case
(22)
v2
(IX - c) Vx - ,.,; = 0, for a < x < b
xx
subject to the (Dirichlet) boundary conditions V(a) = 0, V(b) = 1.
--- page 344 ---

Survival and Growth with a Liability: Optimal Portfolio Strategies in Continuous Time
317
478
S. BROWNE
The general solution to the second-order nonlinear ordinary differential equation
of (22) is KI - K 2(c - IX)"y/ r+ I, where Kp K2 are arbitrary constants which will be
determined from the boundary conditions. The boundary condition V(a) = 0 determines that K1 = Kic - ra)y/ r+l, and the boundary condition V(b) = 1 then determines K 2, which then leads directly to the function Vex) given in (21). It is clear that
this function V is in %,Z and does in fact satisfy V. > 0 and v.. < 0, and moreover
satisfies conditions (0, (ii) and Gii) of Theorem 2.1 on the interval (a, b). (Condition
(ij) is trivially met since V is bounded on (a, b).) As such V is indeed the optimal
value function and the associated optimal control function ft of (20) is then obtained
by substituting the function V of (21) for w in (11).
0
Note that under policy ft, the wealth process, say X,*, satisfies the stochastic
differential equation
(23)
dX,* = (c - rX,*) dt + JL2~ r(c - rX,*) d~, for t ~ T*,
where T* = min{Ta*, Tt}, and Tz* = inf{t > 0; X,* = z}. This is obtained by placing
the control (20) into the evolutionary equation (3). Equation (23) defines a linear
stochastic differential equation, i.e., X* is a time-homogeneous diffusion on (a, b)
with drift function JL*(x) = c -IX, and diffusion coefficient function O'z*(x) =
«20'1(JL - r»(c -IX»Z == (2/'YXc -IX)2. As such its scale function is defined by
(24)
S*(x) = {exp{ - t 2JLt(u/ dU} dy:= -( 'Y + r) -I(C - IX»)'/r+l,
for a :::;; x ~ b
0' * (u
where 'Y = i« JL - r) 1 0' )2. For this process therefore,
*
*
S*(x) - S*(a) _ (c - ra)y/r+l - (c - IXr/r+ 1
P.(T. >Tb)= S*(b)-S*(a) = (c_ray>'/r+l_(c_rb)'Y/r+l'
which of course agrees with (21). Thus the process (S*(X,*)} is a diffusion in natural
scale, and is therefore a (uniformly integrable) martingale with respect to the
filtration g; (as is the optimal value function), i.e., E(S*(X,*)Ig;) = S*(X.*) for
o ~ s :::;; t ~ T*, where TOo := min{Ta*' Ttl. Note further that the scale function S*(x)
of (24), is increasing in x (although negative) for 0:::;; x < clr.
3.1.1. Inaccessibility of the safe-region under f~ and E-optimal strategies. While
we have found a policy that maximizes the probability of reaching any b < c Ir before
any a < b, it is important to realize that if we extend b to clr, then this policy will
never achieve the safe point c Ir with positive probability in finite time. We can of course
extend the function displayed in (21) to the point c Ir to get
S*(x)-S*(a) =1_(C-IX)y/r+1 <<Xl
fora<x~clr
S*(clr)-S*(a)
c-ra
'
which shows than in fact clr is an attracting barrier for the process X* . However, it is
an unattainable barrier. (See §lS.6 in Karlin and Taylor (1981) for a discussion of the
--- page 345 ---

318
S. Browne
OPTIMAL PORTFOLIO STRATEGI ES
479
boundary classification terminology used here') To verify this, first recall that if we let
s*(x) = dS*(x )Idx denote the scale density of the diffusion X*, then its speed density
is given by
_ Y(
) - (1'/ r + 2)
-Zc-a
and it is well known then that
E,(min{ Ta*, T,*/,}) < x' if and only if
f /'[S*(clr) - S*(y)]m*(y) dy < 00.
x
However, it can be seen from (24) and (26) that the latter quantity is
je/,
Y
je/, 1
[S*(clr) - S*(y)]m*(y) dy =
--dy = 00,
x
2( Y + r) x
c - ry
and thus we see that while N minimizes the probability of hitting the ruin point a,
and so is in fact optimal for the problem of mint PiT! = x), it does so in a way which
makes the upper goal, clr, unattainable in finite expected time. In fact, under f~ we
have T,*/ r = 00 a.s., and thus no optimal policy exists for the problem of maximizing the
probability of reaching the safe-region prior to bankruptcy!
Intuitively, what's going on is that as the wealth gets closer to the boundary of the
safe-region, c Ir, the investor gets increasingly more cautious so as not to forfeit his
chances of getting there. This of course entails investing less and less, but in
continuous-time, where the wealth is infinitely divisible, this just means eventually
investing (close to) nothing. However while this in tum does in effect shut off the drift
of the resulting wealth process (see (23», it also shuts off the variance, and some
positive variance is needed to cross over the c Ir-barrier from the danger-zone into
the safe-region. This is not supplied by the policy described above, which essentially
tells the investor that the best he can hope to do (j.e., with maximal probability) is to
try to get pulled into an asymptote that is drifting toward clr.
In terms of our Theorem 2.1, it is clear that V is no longer concave increasing for
x> clr (i.e., for x> elr, we have ~(x) > 0 and ~/x) < 0), and thus Theorem 2.1
is not valid for any u > clr.
REMARK 3.3. This difficulty disappears if r = 0, since if there is no risk-free
investment, the investor always faces a positive probability of ruin and the only way to
survive is to always invest in the risky stock. To see this, note that letting a = 0 and
taking limits as r ! 0 (so that the "safe point" goes to infinity, i.e., when r = 0, there is
always a positive probability of bankruptcy) shows that the value function, V(x:
0, e Ir), then goes to an exponential, i.e., as r J. 0,
(27)
Vex: O,clr) -+ 1 - exp { - 2:2eX}
and for this case the (unconstrained) optimal control to minimize the probability of
ruin is to always invest the fixed constant 2 e I 11-. (This model then becomes a
--- page 346 ---

Survival and Growth with a Liability: Optimal Portfolio Strategies in Continuous Time
319
480
S. BROWNE
degenerate special case of Browne 1995.) In this case the optimal wealth process
follows a linear Brownian motion with drift c and diffusion coefficient 2cU" I J.L, for
which the probability of ruin is the exponential (27). Ferguson (1965) conjectured that
an ordinary investor (in discrete-time and space) can asymptotically minimize the
probability of ruin by maximizing the exponential utility of terminal wealth, for some risk
aversion parameter. It is interesting to observe that for this model the conjecture turns
out to be true. To verify this, one would have to solve the finite-horizon utility
maximization problem for the utility function u(x) = 0 -
1/ exp{ - 2exl J.L}, with arbitrary 1] > 0 and o. Since this problem is then essentially a special case of the
(Cauchy) problem considered in §3 of Browne (1995), we refer the reader there for
further details. If we impose the constraint that the investor is not allowed to borrow,
then it can be shown (Browne 1995, Theorem 3) that the optimal control in this case
is f* = max{x, 2cl J.L}, whereby the investor must invest all his wealth in the risky
stock when wealth is below the critical level 2c / J.L. In this case the value function is
no longer concave below 2c I J.L. Such extremal behavior (or "bold" play, ala Dubins
and Savage 1965) and nonconcavity of the value function below a threshold is also a
feature of the optimal policies in the related survival models studied in Majumdar
and Radner (1991) and Roy (1995), where borrowing is not allowed.
REMARK 3.4. This inaccessibility and the resulting nonexistence of an optimal
policy can be best understood in the context of the more general "goal" problem:
Consider a controlled diffusion {Y/l on the interval (a, b) satisfying
dY/ = m(f,y) dt + v(f,y) dW;,
with the objective of determining a control to maximize the probability of hitting b
before a. Let 'It(x) denote the optimal value function for this problem, i.e., 'It(x) =
SUPt E go Px(Tj > TD with optimal control t/I(x) = arg SUPt E .If Px(Tj > 'rD· This problem was first studied by Pestien and Sudderth (1985, 1988), who showed-using a
different formulation-that
(28)
{ m(f,x)}
t/I( x) = argsj v2(f, x) ,
and indeed our f~(x) of (20) can be obtained from maximizing m/v2 for m and v2 in
(19). However as noted in Pestien and Sudderth (1985, 1988), this is the case only
when infx v~ (f, x) > 0, where t/I = m* Iv 2 *.
These results can be obtained from somewhat simpler methods (albeit with some
lesser generality) then those used in Pestien and Sudderth (1985, 1988) as follows:
'It(x) must satisfy the HJB equation
(29)
== sup {[m(f,x) 'It +.!.'It ] ·v2(f X)} = 0
2( f
)
x
2
xx
,
,
f
v
,x
subject to the Dirichlet boundary conditions 'I'(a) = 0, 'I'(b) = 1.
If 'I' is a classical solution to the HJB equation (29), then we must have 'l'x > 0 and
'lJfxx < O. Therefore as long as v2(f, x) > 0, it is clear from (29) that the maximum of
(29) occurs at the maximum of m/v2, which by (28) is denoted by t/I. If we now let
p(x) = sUPr{m(f, x)/v2(J, x)}, i.e., p(x) = m(t/I(x), x)/v2(",(x), x), then the solution to (29) subject to the Dirichlet conditions is simply 'I'(x) = faXs(z) dzlfabs(z) dz,
--- page 347 ---

320
S. Browne
OPTIMAL PORTFOLIO STRATEGIES
481
where s(z) = exp{ - 2 J 'p(y) dy}, with which our value function (21) of course agrees,
for b < clr.
However, it is also clear from (29) that for v2(f, x) = 0, the HJB equation need not
hold, and therefore, no policy is in general optimal when this is the case, which is
precisely what is happening here for b = clr (see also Example 4.1 in Pestien and
Sudderth 1988).
For more details on the general problem from a different perspective, we refer the
reader to the fundamental papers of Pestien and Sudderth (1985, 1988). We now
return to the problem of determining a 'good' strategy for crossing the clr barrier.
An E-optimal strategy. As we have just seen, the inaccessibility of clr is due to
the fact that N dictates an investment policy that causes the drift and variance of the
resulting wealth process to go to zero as the clr barrier is approached from below. A
practical way around this difficulty is to modify N as follows:
Let i8* denote the (suboptimal) policy which agrees with It below the point
elr - 8, and then above it invests K in the risky stock until the el r barrier is
crossed, i.e.,
18*(X) = {;(x)
for x ~ elr - 0,
for x> elr - o.
Now V(xo, a, elr) as given in (25) is an upper bound on the probability of escaping
the interval (a, elr) into the safe-region starting from an initial wealth level Xo < elr
(see Krylov 1980, page 5). Without loss of generality, we may take a = 0 here. Thus
for any € > 0, and initial wealth Xo < elr, the best we can do is find a policy which
gives
(30)
(
rx ) ,,(/ r+ 1
V(Xo: 0, elr) - e = 1 -
1 - -f
- e
as its value. Therefore for any given e, and initial wealth Xo < elr, we need to find
0= 8(xo, €) and K = K(XO' e) which will achieve the value (30). To keep the drift
and diffusion parameters continuous, we must take K = (2r I( I-L - r»o(xo, e), and so
is(x) = (2r I( I-L - r »max{e Ir - x, O), which then gives a corresponding wealth process X 8 which has the (continuous) drift function I-Lo(x) and diffusion function u/(x)
given
by
J-Lo(x) = max{e -
rx, 2ro + rx -
C},
and
u/(x) = max{2(e -
rx)2 11', 2r20 2 I 1'}'
The scale density for this new process, defined by
{ f
y 21-L8 ( Z )
}
SIl(Y) = exp -
u/(z) dz
can then be written as
for y ~ elr - 0,
for y ~ elr -
0,
where cp denotes the standard normal p.d.f.
--- page 348 ---

Survival and Growth with a Liability: Optimal Portfolio Strategies in Continuous Time
321
482
S. BROWNE
The probability of reaching the safe-region from initial wealth Xo < c/r under this
policy is therefore
.
fJos8(y)dy
_I
Vs(xo·O,c/r) = je / r
( )d == V(xu: O,c/r)(1 + oy/ r+IH(y,r,c»)
o
58 Y
Y
where V is as in (25) and H is given by
H( y, r, c) = (1 + y/r)(r/c)y/ r+1 ey/(2rl./27Tr/y [cJ>(2'h/r) -
<1>( fy/r)],
where <I> denotes the standard normal c.dJ. Setting v.., = V -
€, and then solving for
8 therefore gives
(31)
Therefore, for the particular o(xo, €) given in (31), the policy fa* is within e of
optimality. Since we chose a = 0 here purely for notational convenience, we summarize this in the following theorem for the case with an arbitrary bankruptcy point a,
with 0 ~ a < xo'
THEOREM 3.2.
The policy fa*, given by
(32)
(
N(X)
fs*(x) =
2r
r ( +r)
p,_r[f./(H(y,r,c)[V(xo:a,clr) -e])] / y
fora <x~c/r- 0,
forx~c/r-o,
is an €-optima/ policy for maximizing the probability of crossing the c Ir barrier before
hitting the point a, starting from an initial wealth level xu' where a < Xo < c/r, and
V(-: a, c Ir) is the function given by (25).
3.2. Minimizing discounted penalty of bankruptcy. Suppose now that instead of
minimizing the probability of ruin, we are instead interested in choosing a policy that
maximizes the time until bankruptcy, in some sense. Obviously, this problem is nontrivial only in the danger-zone a < x < clr, which is the case considered here. Maximizing the expected time until bankruptcy is a trivial problem, since there are any number
of policies under which the expected time to bankruptcy is in fact infinite. In
particular the f.-optimal policy described above gives a positive probability of reaching
the clr barrier, and since the safe-region (x ~ clr) is absorbing, it therefore gives an
infinite expected time to ruin. Thus we need to look at other criteria. Here we will
consider the objective of minimizing the expected discounted time until bankruptcy (a
related problem without forced withdrawals was treated in Dutta 1994 in a different
framework, and in an incomplete market in Browne 1995). In particular, suppose
there is a large penalty, say M, that must be paid if and when the ruin point a is hit.
If there is a (constant) discount rate A > 0, then the amount due upon hitting this
point is therefore Me - AT!, and we would like to find a policy that minimizes the
expected value of this penalty. Clearly, this policy is equivalent to the policy that
minimizes E/e - ),~J).
To that end, let F(x) = infro E/e - AT!), and let t: denote the associated
optimal policy, i.e., t: = arg inf] E r; EA (e -AT!). For reasons that will become clear
--- page 349 ---

322
S. Browne
OPTIMAL PORTfOLIO STRATEGIES
483
soon, define the constants 1'/ + and D by
(33)
(34)
D = D( >.) = (y + >. - r)2 + 4ry,
where 'Y is defined by (8). The optimal policy and optimal value function for this
problem is then given in the following theorem.
THEOREM 3.3.
The optimal control is
(35)
and the optimal value fimction is
(36)
( c-rx)'Tf ~
F(x) = --
c - ra
'
fora :s: x s clr.
REMARK 3.5. Note that TJ+> 1, and that F(a) = 1, F(clr) = 0, and F(x) is
monotonically decreasing on the interval (0, clr), as is the optima} policy r;, which
once again invests a constant proportion of the distance to the goal. Observe too that we
are therefore once again faced with the problem that under this policy, the safe-point
clr is inaccessible. However, in this case it is indeed the unique optimal policy. The
condition F(a) = 1 is by construction, but the fact that F(cl r) = 0 is determined by
the optimality equation itself, i.e., optimality determines that the clr barrier is
inaccessible. The intuition behind this is that this policy-although it never allows the
fortune to cross the clr-barrier-does indeed minimize the expected discounted time
until ruin. The best one can do in this case is to get trapped in an asymptote
approaching clr, which this policy tries to do. Any additional investment near the
c Ir-barrier (such as in the E-optimal strategy of the previous problem) allows a
greater possibility of hitting a, thus increasing the value of Ex(e - hu ) .
REMARK 3.6. As a consistency check, note too that when we substitute the control
N of (35) back into the evolutionary equation (3), we obtain a wealth process, say
X/" that satisfies the stochastic differential equation
(37)
dX/' = [ (Tj+~ l)r -
1 ](c - rXn dt + u( ~+-=-rl)r (c - rX/) dW;, for t < T\
where TA = min{'T:, 'TC~TJ, where 'T/ = inf{t > 0: X/ = z}.
For this process, it is well known that the Laplace transform of T} evaluated at the
point A, say L(x: A) = E,(eh :'), is the unique solution of the Dirichlet problem
with L(a: A) = 1 and L(clr: A) = O. It can be easily checked that we do in fact have
F(x) == L(x: A). It should be noted that 'To" is a defective random variable, with
Ex('T:) = 00, as can be seen from the fact that
( c - rx )y/ r+l
L(x: 0) =
c _ ra
== 1 - V(x: a, clr),
--- page 350 ---

Survival and Growth with a Liability: Optimal Portfolio Strategies in Continuous Time
323
484
S. BROWNE
where VeX: ',' ) is the function defined by (21). This of course is due to the fact that
c Ir essentially acts as an absorbing barrier, and it can be hit with positive probability
(albeit in infinite time). Specifically, as A l 0, it is clear that Tf +( A) ---) Tf +(0) == 'Y Ir + 1,
and thus F(x) converges (uniformly in x) to the probability that the bankruptcy point
a is hit before the safe point clr, which implies that the control t:(x) converges
(uniformly in x) to the control f~(x) of (20), i.e. as A lO:
F(x) ---) 1 - Vex: a,cl r)
2
and t: ( x) ---) p, _ r (c - rx) == g ( x ) .
Note also that for A > 0, we have f~ > f~ , which is of course consistent with the fact
that a "bolder" strategy maximizes the probability of survival, while a " timid"strategy
maximizes expected playing time (for subfair games).
PROOF. Theorem 2.1 is again relevant, however since Theorem 2.1 deals with the
maximization pro_blem, recognize that F = -sup/{ _E\(e ~ AT!)}. We can now apply
Theorem 2.1 to F:= -F with A(x) = A, g = 0, h(a) = -1. Reverting back to F, we
then see that the nonlinear Dirichlet problem of (9) for F becomes then:
(38)
F2
(rx-c)F,-'Y/ -AF=O, fora <x<clr,
xx
subject to the Dirichlet boundary condition F(a) = 1, where 'Y = t« p, - r)1 0-)2.
Observe of course that we now require Fx < 0 and Fxx. > O.
The nonlinear second-order ordinary differential equation in (38) admits the two
solutions C(c - rx)TJ+, and K(c -
rx)TJ~, where C and K are constants to be determined from the boundary condition, and where Tf+' Tf ~ are the roots to the quadratic
equation Q(Tf) = 0, where
(39)
To determine which (if any) of these two solutions are appropriate we need to
examine these roots in greater detail. The discriminant of (39) is the constant D of
(34) which is clearly positive, and thus the two roots are real and, for A > 0, distinct.
In particular
Since Tf + Tf ~ = A I r > 0, both roots are of the same sign, and since Tf + > 0, they are
both positive. The boundary condition F(a) = 1 determines the constants C, K as
C = (c -
ra)~TJ + and K = (c -
ra)~TJ - and so clearly C> 0 and K> 0, and therefore, Fx < 0 for both solutions. However it is easy to check the roots in (40) to see
that Tf + > 1, while Tf ~ < 1, and so Fxx. > 0 only for the root Tf +. Thus we find that the
(unique) solution to the (38) that satisfies F(a) = 1 and Fx < 0 Fxx > 0 is given by
the function F(x) defined in (36). Moreover, it is a simple matter to check that
conditions (j), (ij) and (iii) of Theorem 2.1 are indeed met for F (F is bounded on
(a, b», and so we may conclude that F is optimal. The associated optimal control
function, t: of (35), is then obtained by placing F (or F = - F) into (11).
0
REMARK 3.7. An alternative proof of Theorem 3.4 can be constructed by modifying the arguments in Orey et al. (1987), who treat the converse problem of maximizing discounted time to a goal, to deal with the minimization problem treated here.
--- page 351 ---

324
S. Browne
OPTIMAL PORTFOLIO STRATEGIES
485
The evolutionary equation (3) would have to be reparameterized by taking /1 =
1T1 •
(elr - Xl), for admissible control processes 1T, and then applying the results of Orey
et a!. (1987) to the further transformed process Y,7T = In[(c - rX;r')/(c - rb)).
Note that since the wealth process, say X/" under the policy ft, satisfies the
stochastic differential equation (37), we can apply Ito's formula to the function FO
given by (36) to show, after simplification, that
(41)
dF(X/,) = F(Xn[ (1-,+)2r
;+ ~+fr + Y) dt - {iY T/:;~ I da'l forO < 1< TA.
The quadratic of (39) then shows that (T/+)2 r -
T/+(r + Y) = A(T/+- 0, and thus
substituting this into the r.h.s. of (40, and then solving the resulting (linear)
stochastic differential equation gives
which shows that the value function FO operating on the process X/, is a geometric
Brownian motion on the interval (0, 1), for a .:::; X/, S; c Ir.
Unfortunately, as noted above, this policy, while optimal for the stated problem,
will never cross the c Ir bam·er into the safe-region, and thus the investor should utilize a
policy similar to the e-optimal policy described earlier to get into the safe-region.
Since this can be achieved at relatively little cost, we will assume for the sequel that
the investor does in fact invest in a way that will allow a positive probability of getting
into the safe-region. When (if) the safe-region is achieved, the investor no longer
faces the problem of bankruptcy, and should then be concerned with other optimality
criteria. We consider two such criteria in the next section.
4. Optimal growth policies, in the safe-region. Suppose now that we have
survived, i.e., we have achieved a level x > clr. As noted earlier it is clear that in this
region there need never be a possibility of ruin, and therefore the investor who has
achieved this safe-region will be interested in criteria other than survival. In particular, we assume here that in this region the investor is interested in growth, by which
we mean achieving a high level of wealth as quickly as possible. Suppose therefore
that there is now some target goal, which we will denote again by b with b > x, which
the investor wants to get to (e.g., to payout dividends) as quickly as possible. In this
section we consider two related aspects of this problem. First we consider the
problem of minimizing the expected time to the goaL, and then we consider the related
problem of maximizing the expected discounted reward of achieving the goal. In both
cases, the optimal strategies are interesting generalizations of the Kelly criterion that
has been studied in discrete-time in Kelly (1956), Breiman (1961) and Thorp (1969),
and in continuous-time in Pestien and Sudderth (1985) and Heath et a!. (1987). (See
also Theorem 6.5 in Merton 1990, where it is called the growth-optimum strategy. For
Bayesian versions of both the discrete and continuous-time Kelly criterion, see
Browne and Whitt 1996.) Such policies dictate investing a constant multiple of the
wealth in the risky stock. Here our policies invest a constant multiple of the excess
wealth over the boundary cl r, in the risky stock. This will make the clr boundary
inaccessible from above, ensuring that the investor will stay in the safe-region forever,
almost surely.
--- page 352 ---

Survival and Growth with a Liability: Optimal Portfolio Strategies in Continuous Time
325
486
S. BROWNE
4.1.
Minimizing the time to a goal.
To formalize this, let Xo = x, but now with
elr < x < b. For Tt:= int{t > 0: xl = b}, let
C(x) = infE\(Tt), and let fJ=arginfEATt).
~ .
~ .
THEOREM 4.1.
For the problem of minimizing the expected lime to the goal b, lhe
optimal policy is to invest
(42)
l1--r(
C)
fJ(x) = --;;'2 x - r ' forclr < x < b.
The optimal value function is
(43)
1
(rb-c)
C(x) = --In --
r+1'
rx-c' forelr < x::; b.
REMARK 4.1.
Note that the proportion ( 11- - r) I u 2 in (42) is the same proportion
as in the ordinary continuous-time Kelly criterion (or optimal growth policy) (see
Heath et al. 1987, Merton 1990, Browne and Whitt 1996). However in our policy fJ,
this proportion operates only on the excess wealth over the boundary elr. Under this
policy therefore, the lower boundary, c Ir is inaccessible. It is quite interesting to
obseIVe that this policy is independent of the goal b. This is quite remarkable, since
while it was to be expected a priori that the optimal policy should look something like
(42) near the point clr, which ensures that clr is inaccessible from above, it is not
clear why one should expect such behavior to continue throughout even when the
wealth is far away from elr. Nevertheless, it appears that the best one can do is to
simply put c Ir into the safe asset, and leave it there forever, continuously compounding at rate r . This is the endowment which will finance the withdrawal at the constant
rate c forever. (Recall, e Ir = c /; e - r1 d/.) Once this is done, the optimal policy then
plays the best ordinary optimal growth game with the remainder of the wealth,
x - e Ir. This policy is quite similar to the policy prescribed in Proposition 11 of Black
and Perold (1992) as a form of CPPJ (see also Dybvig 1995). Thus, we have shown
that CPPI has another optimality property associated with it, namely that of optimal
growth.
PROOF. Since here we are minimizing expected time, we could apply Theorem 2.1
to q(x) = sUPJ{ -E/Tl)}, with g(x) = -1, A = 0, h(b) = 0. Recognizing that C =
-G, it is then seen that in terms of G, Theorem 2.1 now requires Cx < 0 and
Gxx > 0, and that the nonlinear Dirichlet problem of (9) specializes to
(44)
G2
(rx - c)q" - 1'C x + 1 = 0, for clr <x < b,
xx
subject to the boundary condition G(b) = O. It is readily verified that the function G
of (43) satisfies this, and that moreover for this function we have Gx < 0 and Gxx > 0
for all clr < x < b. The control function fJ(x) of (42) is obtained by substituting C
of (43) for /I in (11). However, note that while it is easy to see that conditions (i) and
(iii) of Theorem 2.1 are satisfied by C, it is also clear that G is unbounded on
(elr, b), since G(x) -> :0 as x J., elr. Thus it is doubtful that condition (ii) of
--- page 353 ---

326
S. Browne
OPTIMAL PORTFOLIO STRATEGIES
487
Theorem 2.1 holds for this case. Nevertheless, we will show that Theorem 4.1 holds
and j:J is indeed the optimal policy, however the final proof of this awaits the
development in §4.2, and we will complete the proof there after Lemma 4.3.
0
Note that when we substitute the control j:J of (42) back into the evolutionary
equation (3), we obtain an (optimal) wealth process, say X b, that satisfies
where 7t := inf{t > 0: X rb = b}, which is again a linear stochastic differential equation. (It is clear from this that c Ir is in fact an inaccessible lower boundary for X b.)
The solution to (45) is
X/ = (XS - 7
)exp{(r + y)t + y'2Yw;} + 7' for 0 s: t < 76,
from which it follows that
( 46)
for 0 s: t < 7; ,
i.e., under the (optimal) policy j:J, the process {G(Xn - G(Xo)}, follows a simple
Brownian motion on (0,00) with a drift coefficient equal to -1. (From this it is easy to
recover the value function (43) from (46) by evaluating the expected value of (46) at
t = 7; using the fact that G(b) = 0, which then gives Ex(rt) = G(x).)
REMARK 4.2.
The "minimal time to a goal" problem for the case c = 0 was first
solved in the fundamental paper of Heath et al. (1987) without direct recourse to
HJB methods (see also Schill 1993). The result in that case is simply (42) with c = 0
(see §4 in Heath et al. 1987). Merton (1990, Theorem 6.5), also obtained this policy
via another, rather complicated, argument. Since the proof given here holds too for
the case c = 0, our results also provide an alternative and complementary proof for
that case to the ones in Heath et al. (1987) and Merton (990).
In fact, it is possible to apply the results of Heath et a1. (1987) to construct a
different proof of Theorem 4.1. First one would need to reparameterize the wealth
equation (3) by taking fr = TTr ' (X! - clr), and then applying results of Heath et al.
(1987) to the further transformed process 1';" = In[(rXr" - c)/(rb - c)]. However the
results in Heath et al. (1987) are specific to the case where the controls must lie on a
given constant set that is independent of the current wealth, while the approach here,
based on the HJB methods of Theorem 2.1 could be modified to allow for a state
dependent opportunity set.
4.2.
Maximizing expected discounted reward of achieving the goal. Suppose now
that instead of minimizing the expected time to the goal b, we are instead interested
in maximizing E/e- AT1), for cl r < x s: b. To that end Jet
U(x) = supEAe- ATb ), and let fJ(x) = argsupEAe - AT6 ).
~s
~s
As we show in the following theorem, the optimal policy for this problem also
invests a (different) constant proportion of the excess wealth above the c/r barrier,
and is hence another version of the CPPI strategy as in Black and Perold (1992).
--- page 354 ---

Survival and Growth with a Liability: Optimal Portfolio Strategies in Continuous Time
327
488
s. BROWNE
THEOREM 4.2.
The optimal control is
( 47)
p,-r
(
C)
f~(x) =
u 2(1 _ T/ - ) x - r' forc/r <x < b,
and the optimal value function is
(48)
v ( x) = (: =
~ r, for c I r 5, X 5, b,
where T/ - == T/- ( A) was defined previously in (40).
REMAR~ 4.3.
Recall that_ T/- is the root that satisfies 0 5, T/- < 1 to the quadratic
equation Q(T/) = 0, where Q(.) is given in (39). Note that U(b) = I, Uk/r) = 0, with
U(x) monotonically increasing on (c l r, b). As was the case earlier in §3, the fact that
U(b) = 1 is by construction, but it is optimality that causes V(c Ir) = 0, and hence
makes the danger-zone inaccessible from the safe-region.
PROOF.
The proof is essentially the same as for Theorem 3.3. Specifically, here
Theorem 2.1 applies directly with u = b, A(X) = A> 0, g = 0 and h(b) = 1. Thus
the nonlinear Dirichlet problem of (9) for this case specializes to
(49)
V 2
(IX - e)Vx -
y_X -
AU = 0,
for e/r < x < b,
Uu
subject to the boundary condition U(b) = 1. Since we require Vx > 0 and Vxx < 0, it
is clear the solution of interest here involves the smaller root, T/ -, to the quadratic
Q( T/) = 0 (see (39» , since T/- < 1. The control function f(J(x) of (47) is then obtained
by substituting V of (48) for }J into (11). Finally, it is easy to check that V of (48)
satisfies conditions (i), (ii) and (iii) of Theorem 2.1, and we may therefore conclude
that ft is indeed optimal.
0
1t is interesting to observe that when we place the control ft back into tpe
evolutionary equation (3), we find that the resulting optimal wealth process, say X/"
satisfies the stochastic differential equation
(50)
dX-A
= (2Y
] ( -A)
I2Y (-A)
I
(1 _ T/ )r + 1 rXI
- c dt + (1 _ T/ )r rXt
- c d~, for t < 'Tt
where 'Tt = inf{t > 0: X/, = b}. An application now of Ito's formula to the function
UO of (48) using (50) (and (39» gives
which shows that the value function U(·) operatina on the process X/, is a geometric
Brownian motion on the interval (0, 1), for c Ir < X/, < b.
REMARK 4.4. Orey, Pestien and Sudderth (1987), using different methods, studied
some general goal problems with a similar objective as that considered here, and as a
particular example study a version of our problem with r = c = 0 (Orey Pestien and
Sudderth 1987, page 1258). An alternative proof of Theorem 4.3 can therefore be
--- page 355 ---

328
S. Browne
OPTIMAL PORTFOLIO STRA TEG IES
489
constructed by using the results of Orey et aJ. (l987) using the transformation and
reparameterization described above in Remark 4.2.
We may now use the results of Theorem 4.2 to complete the proof of Theorem 4.1.
However, we first need the following lemma, which is of independent interest since it
is applicable to more general processes than those considered here (for related
results, see SchiH 1993, §4).
LEMMA 4.3.
Suppose that for every A > 0, we have
( I
- liT' )
V ( x; A) = i?f Ex
- ~
,with optima} control/" ( x; A),
with v(x; A) < 00, limA) {) p(x; A) = v(x; 0) < 00, and limA> {) f*(x; A) = [(x; 0).
Then
(51)
(1 -}OTf)
(1 -AT')
Jim infE,
- ~
= infE. lim
- ~
== infEX< 7'f),
. .qo f
f
AtO
f
with infl Ex(Ti) = v(x;O) and with optimal controlf(x;O).
PROOF. It is the first equality in (51) that needs to be established since the second
is just an identity. To proceed, it is obvious that A -Ill - eh () ::;; 1'f for all .A ~ 0,
and hence £ .. 0 - '[1 - e- Mf ]) ::;; Ex(T f ), as well as infi E t(A- 1(1 - e- AT']) ::;;
inf! £/7'i). Since the r.h.s. of this inequality is independent of the parameter A, it
follows that we may take limits on A to get
(52)
For notational convenience now, Jet f1l* denote the policy f*(.; A), and for any policy
I, let 1'[f) = Tf. Note that under this notation, we may write v(x; A) = E/A -1[1 -
e - ~ T(in]).
To go the other way now, suppose that there is an admissible policy, say f, such
that T[N) ~a
S T[/J as A ~ O. Then it is clear that
An application of Fatou's lemma then shows that
(53)
The inequalities (52) and (53) yield (51).
0
COMPLETION OF PROOF OF THEOREM 4.1.
ObselVe first that 77-(A) ~ 0 as ,q 0,
and that therefore fi; --7 fJ as A ~ 0, where fiJ and ft are given by (47) and (42).
--- page 356 ---

Survival and Growth with a Liability: Optimal Portfolio Strategies in Continuous Time
329
490
S. BROWNE
Note further that for any c Ir < x < b, we have
I·
1 - U( x) = G( )
1m
A
x ,
,qo
where U and_ G are given by (48) and (43). Finally, since 1/ - ( A) ~ °
as A lO, we have
X/,, ". ~"' . X,\ "; as At 0, where X,b and i"/ are defined by (4S) and (SO), from
which it is clear that 7l ~a s
7" h as A lO. Therefore, Lemma 4.3 may be applied
directly to Theorem 4.2 to deduce Theorem 4.1.
0
5.
The multiple asset case. As promised earlier, here we show how all of our
previous results extend in a very straightforward way to the case with multiple risky
stocks. The model here is that of a complete market (as in, e.g., Karatzas and Shreve
1988) where there are n risky assets generated by n independent Brownian motions.
The prices of these stocks evolve as
(54)
i=l, ... ,n,
while the riskless asset, B" still evolves as dB, = rB, dt. The wealth of the investor
therefore evolves as
(S5)
dXr = [rxr - c + ,~f,( J.i-, - r)] + ,~ Jt f,u,} dHl;(J),
where now f, denotes the total amount of money invested in the ith stock.
If we introduce now the matrix a = (0' \
' and the (column) vectors f.l. =
(J.i-l' .•. , J.i-,,)T, f = (fl'" . , fn)T, and then set A = aaT, we may write the generator
of the (one-dimensional) wealth process, for functions \)I(x) E W 2 as
(S6)
where 1 denotes a vector of 1 'so The assumption of completeness implies that A - I
exists, and thus all our results will go through exactly as before. In particular, if an
optimal value function for a specific problem is denoted by vex), the optimal control
vector is f~(x) where
(57)
The differential equations «22), (38), (44) and (49» , and hence the value functions
«21), (36), (43) and (48», all remain the same except for the fact that now the scalar 'Y
is evaluated as
(58)
It is interesting to note that for the problem of maximizing the probability of
reaching b before a when b is in the danger-zone, considered in §3.1, the optimal
policy now does depend on the variances and covariances of the risky assets, since
--- page 357 ---

330
S. Browne
OPTIMAL PORTFOLIO STRATEGI ES
491
instead of (20), in the multiple asset case we now get
(59)
The €-optimal policy of §3 needs to be modified, but the extension is straightforward
and we leave the details for the reader. For reference, we note further that if we
define the vector K by K := A - I (fA. - r1), then the optimal controls (35), (42) and
(47) of §§3.2, 4.1 and 4.2 become, respectively
(60)
ft( x) = K( 7] + -
1) - 1 (f - x) ,
ft ( x) = K( 1 -
7] - ) - I ( X - f ).
f~(x) = K(X - f),
6.
Linear withdrawal rate. In this section we show how all of our previous
results and analysis for the case of forced withdrawals at the constant rate c > 0 can
be generalized to the case where there is a wealth-dependent withdrawal rate, c(x)
where
c(x) = c + Ox.
Here we will only consider the case where 0 S; 6 < r. For notational ease, we will
consider again only the case with one risky stock. The generalization to the multiple
stock case as in the previous section is very straightforward, and so we leave the
details for the reader.
For this case the evolutionary equation (3) becomes
(61)
dP
dB
.
dJ(I = [,_' + (Xl - [,)_' - (c + eX') dt
t
'P,
"
B,
I
= [Cr - e)x( + It( JL - r) - c] dt + f,udW, .
If we now define r:= r - e > 0, then for Markov control processes f, and 'I' E %,2
the generator of the wealth process is
(62)
The parameter r is simply the adjusted (risk-free) compounding rate. Essentially,
nothing really changes except for the fact that the danger-zone is now the region
x < elf, and the safe-region is its complement. The differential equations (22), (38),
(44) and (49) all remain the same except for the fact that we must replace rx - c with
rx - e. The parameter 'Y in all those equations, as well as here, is still defined as in
(8), i.e., 'Y = ~« JL - r) I u )2, where r is the standard interest rate. Thus, the previous
analysis will go through with relatively little change, and so we will only point out the
essential differences. In particular, the structure of the policies remain the same, in
that the optimal survival policies of §3 invest a fixed proportion of the distance to the
(new) safe-region barrier, elf, while the optimal growth policies of §4 invest a fixed
proportion of the excess of wealth over the barrier.
6.1. Sunival problems in the danger-zone. The analysis of §§3.1 and 3.2 can be
repeated almost verbatim. What changes is that now for a < x < b < eli, the value
--- page 358 ---

Survival and Growth with a Liability: Optimal Portfolio Strategies in Continuous Time
331
492
S. BROWNE
function veX; a, b) of (21) becomes instead
(c - Fa)Y!f+1 - (c - i'x)Y!f+l
V( x: a , b) =
.
,
for a s x s b.
(c - Fa)"l r+l - (c - Fb)""!f+1
(63)
Since (11) still holds, the resulting optimal control becomes, instead of (20),
(64)
For the disc0!1nted problem of §3.2 (~s well as for the discounted problem of §4.2),
the quadratic Q(.) oj (39) changes to Q('Yj) = 'Yj2;: -
'Yj(y + A + F) + A, and thus the
two (real) roots to Q('Yj) = 0, denoted by 1,+ and 1,-, become, instead of (40),
(65)
It is easy to check that once again, we have 0 .s 1,- < 1 < 1,+, and so the optimal
value function (36) and the optimal control function (35) become, respectively
(66)
( c
i'x)T,+
F(x)= c-fa
'
6.2. Growth policies in the safe-region. Once again, the analysis is almost
identical to that in §§4.1 and 4.2. The value and the optimal control functions for the
minimal expected time to the goal problem, (43) and (42) are replaced respectively by
(67)
1
(Fb-C)
G(x) = -_ -In -_-
r+y
rx-c'
p,-r(
C)
f6 ( x) = -;;'2 x - j , for c If < x < b.
Note that the optimal (Kelly) proportion of the excess wealth invested in the stock,
(p, - r) I u 2, is unchanged in this case.
Similarly for the discounted problem considered in §4.2, the value function (48)
and optimal policy (47) become
(68)
( fx
c )T,-
Vex) = --
,
Fb - c
1'* (
)
P, - r
(
c )
}U X
=
2(
__ ) x -
-= .
u
1 -
'Yj
r
The case where e> r, and hence with f < 0, introduces new difficulties that will
be discussed elsewhere.
Acknowledgments. The author is most grateful to Professors Ioannis Karatzas of
Columbia University and Bill Sudderth of the University of Minnesota for very
helpful discussions. In particular, the proof of Lemma 4.3 is due to Ioannis Karatzas.
He is also thankful to two anonymous referees for very helpful comments and
suggestions and for bringing the references Schiil (1993), Dutta (1994) and Roy (1995)
to his attention.
References
Black, F., A. F. Perold (1992). Theory of constant proportion portfolio insurance. Jour. Econ. Dyn. and
elllri. 16 403-426.
Brelman, L. (]961). Optimal gambling systems for favorable games FO/lrrh Berkeley Symp. Malh. Slal. and
Prob. 1 65-78.
--- page 359 ---

332
S. Browne
OPTIMAL PORTFOLIO STRATEGIES
493
Browne, S. (995). Optimal investment policies for a firm with a random risk process: Exponential utility
and minimizing the probability of ruin. Math. Oper. Res. 20 937-958.
__ , W. Whitt (1996). Portfolio choice and the Bayesian Kelly criterion. Adv. Appl. Prob. 28 1145-1176.
Davis, M. H. A, A R. Norman (1990). Portfolio selection with transactions costs, Math. Oper. Res. 15
676-713.
Dubins, L. E., L. J. Savage (965). How to Gamble If You Must: Inequalities for Stochastic Processes,
McGraw-Hili, New York.
Dutta, P. (1994). Bankruptcy and expected utility maximization. Jour. ECOfl. Dyfl. and Cntrl. 18 539-560.
Dybvig, P. H. (1995). Dusenberry's ratcheting of consumption: Optimal dynamic consumption and investment given intolerance for any decline in standard of living. Review of EconomIc StudIes 62287-313.
Ferguson, T. (1965). Betting systems which mimmize the probability of ruin. J. SlAM 13 795- 818.
Fleming, W. H., R. W. Rishel (975). Detenninistic and Stochastic OptImal Control, Springer-Verlag, New
York.
__ , H. M. Soner (I993). Controlled Markov Processes and Viscoslly SolutIOns, Springer-Verlag, New York.
Grossman, S. J., Z. Zhou (J993). Optimal investment strategies for controlling drawdowns. Math. Fin. 3
241-276.
Heath, D., S. Orey, V. Pestien, W. Sudderth (1987). Minimizing or maximizing the expected time to reach
zero. SlAM J. Contr. and Opt. 25 195- 205.
Karatzas, L, S. Shreve (1988). Brownian Motion and StochastiC Calculus, Springer-Verlag, New York.
Karlin, S., H. M. Taylor (1981). A Second Course on Stochastic Processes, Academic, New York.
Kelly, 1. (1956). A new interpretation of information rate. BeJi Sys. Tech. 1. 35 917-926.
Krylov, N. V. (1980). Controlled DiffusIOn Processes, Springer-Verlag, New York.
Luskin, D. L. (Editor) (1988). PortfolIO Insurance: A Guide to DynamIC Hedging, Wiley, New York.
Majumdar, M., R. Radner 099l). Linear models of economic survival under production uncertamty. Econ.
Theol)' I 13-30.
Merton, R. (1971). Optimum consumption and portfolio rules in a continuous time model. J. Ecoll. Theol)'
3373-413.
__ ([990). ContinuoUl Time Finance, Blackwell, Massachusetts.
Orey, S., V. Pestien, W. Sudderth (1987). Reaching zero rapidly. SlAM J. COni. and Opt. 2S 1253-1265.
Pestien, V. C., W. Sudderth (1985). Continuous-time red and black: How to control a diffusion to a goal.
Malh. Oper. Res. 10599-611.
__ , __ (1988). Continuous-time casino problems. Math. Oper. Res. 13 364-376.
Pliska, S. R. (1986). A stochastic calculus model of continuous trading: Optimal portfolios. Math. Oper.
Res. 11 371-382.
Rogers, L C. G., D. Williams (]987). Diffusions, Markov Processes, and Mamngales, Vol. 2, Wiley, New
York.
Roy, S. (1995). Theory of dynamic portfolio choice for survival under uncertainty. Math. Soc. Sci. 30
171-194.
Schiil, M. (J993). On hitting times for Jump-diffusion processes with pasl dependent local charactenstics.
Stoch. Proc. Appl. 47 131- 142.
Thorp, E. o. (1969). Optimal gambling systems for favorable games. Rev. In/. Stat. Inst. 37 273-292.
S. Browne: Graduate School of Business, Columbia University, 402 Uris Hall, New York, NY 10027;
e-mail: sb30@columbia.edu
--- page 360 ---

MANAGEMENT SCIENCE
Vol. 38. No. I I. November 1992
Primed in U.S.A.
24
GROWTH VERSUS SECURITY IN DYNAMIC
INVESTMENT ANALYSIS *
L. C. MACLEAN, W. T. ZIEMBA AND G. BLAZENKO
School 0/ Business Administration, Dalhousie University, Halifax ,
Nova Scotia, Canada B3H lZ5
Faculty o/Commerce, University 0/ British Columbia, Vancouver,
British Columbia, Canada V6T lZ2
School of Business Administration, Simon Fraser University,
Burnaby, British Columbia, Canada V5A IS6
This paper concerns the problem of optimal dynamic choice in discrete time for an investor.
In each period the investor is faced with one or more risky investments. The maximization of
the expected logarithm of the period by period wealth, referred to as the Kelly criterion, is a very
desirable investment procedure. It has many attractive properties, such as maximizing the asymptotic rate of growth of the investor's fortune. On the other hand, instead of focusing on maximal
growth, one can develop strategies based on maximum security. For example, one can minimize
the ruin probability subject to making a positive return or compute a confidence level of increasing
the investor's initial fortune to a given final wealth goal. This paper is concerned with methods
to combine these two approaches. We derive computational formulas for a variety of growth and
security measures. Utilizing fractional Kelly strategies, we can develop a complete tradeoff of
growth versus security. The theory is applicable to favorable investment situations such as blackjack,
horseracing, lotto games, index and commodity futures and options trading. The results provide
insight into how one should properly invest in these situations.
(CAPITAL ACCUMULATION; FRACTIONAL KELLY STRATEGIES; EFFECTIVE
GROWTH-SECURITY TRADEOFF; BLACKJACK; HORSERACING; LOTTO GAMES;
TURN OF THE YEAR EFFECT)
331
This paper develops an approach to the analysis of risky investment problems for
practical use by individuals. The idea is to provide simple-to-understand two-dimensional
graphs that provide essential information for intelligent investment choice. Although the
situation studied is multiperiod, the approach is couched in a growth versus security
fashion akin to the static Markowitz mean-variance portfolio selection tradeoff. The
approach is a marriage of the capital growth literature of Kelly (1956), Breiman (1961 ),
Thorp (1966, 1975), Hakansson (1971, 1979), Algoet and Cover (1988) and others,
which emphasizes maximal growth, with the maximal security literature of Ferguson
(1965), Epstein (1977), and Feller (1962). In §I, we formulate a general investment
model and desr:ribe three growth measures and three security measures. The measures
all relate to single-valued aggregates of the investment results over mUltiple periods such
as the mean first passage time to a particular wealth level and the probability of doubling
one's wealth before halving it. In §2, we model the investment process as a random walk.
Then, using familiar procedures from probability theory, we can easily generate computable quantities which are usually close approximations to the measures of interest.
To generate tradeoffs of growth versus security one can utilize fractional Kelly strategies
as discussed in §3. A simple but powerful result is that a complete trade-off of growth
versus security for the most interesting growth and security measures is implementable
simply by choosing various fractional Kelly strategies. Theoretical justification for the
fractional Kelly strategies in a multi period context can be made using a continuous time
approach and log normality assumptions (see Li et al. 1990 and Wu and Ziemba 1990).
1562
0025-1909/92/3811/1562$01.25
Copyright © 1992, The Institute of Management Sciences
--- page 361 ---

332
L. C. MacLean, W T. Ziemba and G. Blazenko
GROWTH VERSUS SECURITY IN DYNAMIC INVESTMENT ANALYSIS
1563
Application of the theory to four favorable investment situations is made in §4. In each
case the basic game or investment situation is unfavorable to the typical or average
player. However, systems have been developed that beat the game in the sense that they
have positive expected value. The question then remains how large should the wagers be
and how confident is one that particular goals will be achieved. The various games,
blackjack, horseracing, lotto games and the turn of the year effect differ markedly in their
character. The size of the wagers vary from over half of one's fortune to less than one
millionth of the fortune. The graphs that are outputted for each of these applications
show how to trade off risk and return and provide crucial insight into how one should
invest intelligently in these situations.
1. The Basic Investment Problem
An investor has initial wealth Yo E IR and is facing n risky investments in periods 1, 2,
... , t, .... The return on investments follows a stochastic process defined on the probability space (Q, B, P) with corresponding product spaces (QI, B I, PI) . Given the realization
history W 1- I E Q t-I , the investor's capital at the beginning of period t is Y I_I ( W 1- I ). The
investment in period t in each opportunity i, i = I, ... , n , is Xjl(w t-I ), Xj,(W I- I )
:$: Y I_I (w 1- I ). The in vestment decisions in terms of proportions are X'I ( W 1- I )
= Pjl( WI- I )YI_I (WI- I) for i = I, .. . , n, andpI( WI- I) = (POI( WI- I), ... ,Pnt( WI- I », where
L7~oPjl(WI) = I andpoI(wl- I)YI_I(wll) is the investment at time t in riskless cash-like
instruments. In this general form the investment strategy PI( WI- I) depends on time and
the history QI- I of the investment process. The net return per unit of capital invested in
i, i = I, . .. , n, given the outcome WI E Q, in period t is given by K'I ( wJ , i = I, ... , n,
t = I, .. . . The return on the risk-free asset is given by KOl = O. It is assumed that K jl( Wj)
is defined by the multiplicative model
Kjl(wl) = O'j(t)Ej(wl),
where 0',(1) > 0 is the average time path and E,( Wi) is an independent error term. Special
cases result when O'j(t) = O'j or O'j(t) = a: for t = I, . ... The error terms in this model
are not autocorrelated. A more general approach would be to consider the conditional
return at time t given the history WI- I, denoted by K jl( WI I WI- I). A Bayesian analysis
with such a model is theoretically tractable, but it is not as suited to computations as the
multiplicative model.
An investment environment is said to be favorable if EKj ( w) > 0 for some i. We are
only concerned with favorable environments. The total return on investment is KI( Wi )
= I + K jl ( WI), and the investment decisions are P = (Ph P2( Wi), ... , PI(W I- I ), •.. ).
Then the accumulated wealth at the end of period t is
wIEQI,
t = I , ... .
(I)
For the stochastic capital accumulation process {YI(p)} ~ I we are interested in characterizing the accumulation paths as the investment decisions vary. Consider the following
measures of growth and security.
1.1. Measures of Growth
G 1. J./.I(YO , p) = EYI(p). This is the mean accumulation of wealth at the end of time
t. That is, how much do we expect to have, on average, after t periods.
G2. (f>t(yo, p) = E In (YI(p)I /I). This is the mean exponential growth rate over t
periods. It is a measure of how fast the investor is accumulating wealth. We also consider
the long-run growth rate cJ>(p) = liml_ co cJ>1(YO , p) .
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
