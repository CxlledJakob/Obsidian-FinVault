# Analysis of Financial Time Series, Third Edition (Wiley -- Ruey S_ Tsay -- Wiley series in probability and statistics, 3rd ed_, -- John Wiley & Sons, -- isbn13 9780470414354 -- 9f99b80c7b2dedd477f463dc5323f3b6 -- An.pdf — pages 609–628

--- page 609 ---

582
state-space models and kalman ﬁlter
where the last equality uses Eq. (11.34). Combining Eqs. (11.33) and (11.35) for
j = 2, . . . , m −1, and (11.36) together, we have


yt+1
yt+2|t+1
...
yt+m−1|t+1
yt+m|t+1


=


0
1
0
· · ·
0
0
0
1
0
...
...
0
0
0
· · ·
1
φm
φm−1
φm−2
· · ·
φ1




yt
yt+1|t
...
yt+m−2|t
yt+m−1|t


+


1
ψ1
...
ψm−2
ψm−1


at+1.
(11.37)
Thus, the transition equation of Akaike’s approach is
st+1 = T st + Rηt,
ηt ∼N(0, σ 2
a ),
(11.38)
where ηt = at+1, and T and R are the coefﬁcient matrices in Eq. (11.37).
Harvey’s Approach
Harvey (1993, Section 4.4) provides a state-space form with an m-dimensional
state vector st, the ﬁrst element of which is yt, that is, s1t = yt. The other elements
of st are obtained recursively. From the ARMA(m, m −1) model, we have
yt+1 = φ1yt +
m

i=2
φiyt+1−i −
m−1

j=1
θjat+1−j + at+1
≡φ1s1t + s2t + ηt,
where s2t = m
i=2 φiyt+1−i −m−1
j=1 θjat+1−j, ηt = at+1, and as deﬁned earlier
s1t = yt. Focusing on s2,t+1, we have
s2,t+1 =
m

i=2
φiyt+2−i −
m−1

j=1
θjat+2−j
= φ2yt +
m

i=3
φiyt+2−i −
m−1

j=2
θjat+2−j −θ1at+1
≡φ2s1t + s3t + (−θ1)ηt,
--- page 610 ---

model transformation
583
where s3t = m
i=3 φiyt+2−i −m−1
j=2 θjat+2−j. Next, considering s3,t+1, we have
s3,t+1 =
m

i=3
φiyt+3−i −
m−1

j=2
θjat+3−j
= φ3yt +
m

i=4
φiyt+3−i −
m−1

j=3
θjat+3−j + (−θ2)at+1
≡φ3s1t + s4t + (−θ2)ηt,
where s4t = m
i=4 φiyt+3−i −m−1
j=3 θjat+3−j. Repeating the procedure, we have
smt = m
i=m φiyt+m−1−i −m−1
j=m−1 θjat+m−1−j = φmyt−1 −θm−1at. Finally,
sm,t+1 = φmyt −θm−1at+1
= φms1t + (−θm−1)ηt.
Putting the prior equations together, we have a state-space form
st+1 = T st + Rηt,
ηt ∼N(0, σ 2
a ),
(11.39)
yt = Zst,
(11.40)
where the system matrices are time invariant deﬁned as Z = (1, 0, . . . , 0)1×m,
T =


φ1
1
0
· · ·
0
φ2
0
1
0
...
...
φm−1
0
0
1
φm
0
0
· · ·
0


,
R =


1
−θ1
...
−θm−1

,
and dt, ct, and H t are all zero. The model in Eqs. (11.39) and (11.40) has no
measurement errors. It has an advantage that the AR and MA coefﬁcients are
directly used in the system matrices.
Aoki’s Approach
Aoki (1987, Chapter 4) discusses several ways to convert an ARMA model into a
state-space form. First, consider the MA model, that is, yt = θ(B)at. In this case,
we can simply deﬁne st = (at−q, at−q+2, . . . , at−1)′ and obtain the state-space form
--- page 611 ---

584
state-space models and kalman ﬁlter


at−q+1
at−q+2
...
at−1
at


=


0
1
0
· · ·
0
0
0
1
0
...
...
0
0
0
1
0
0
0
· · ·
0




at−q
at−q+1
...
at−2
at−1


+


0
0
...
0
1


at,
(11.41)
yt = (−θq, −θq−1, . . . , −θ1)st + at.
Note that, in this particular case, at appears in both state and measurement
equations.
Next, consider the AR model, that is, φ(B)zt = at. Aoki (1987) introduces two
methods. The ﬁrst method is a straightfoward one by deﬁning st = (zt−p+1, . . . , zt)′
to obtain


zt−p+2
zt−p+3
...
zt
zt+1


=


0
1
0
· · ·
0
0
0
1
0
...
...
0
0
0
1
φp
φp−1
φp−2
· · ·
φ1




zt−p+1
zt−p+2
...
zt+1
zt


+


0
0
...
0
1


at+1,
(11.42)
zt = (0, 0, · · · , 0, 1)st.
The second method deﬁnes the state vector in the same way as the ﬁrst method
except that at is removed from the last element; that is, st = zt −at if p = 1 and
st = (zt−p+1, . . . , zt−1, zt −at)′ if p > 1. Simple algebra shows that


zt−p+2
zt−p+3
...
zt
zt+1 −at+1


=


0
1
0
· · ·
0
0
0
1
0
...
...
0
0
0
1
φp
φp−1
φp−2
· · ·
φ1




zt−p+1
zt−p+2
...
zt−1
zt −at


+


0
0
...
1
φ1


at,
(11.43)
zt = (0, 0, . . . , 0, 1)st + at.
Again, at appears in both transition and measurement equations.
--- page 612 ---

model transformation
585
Turn to the ARMA(p, q) model φ(B)yt = θ(B)at. For simplicity, we assume
q < p and introduce an auxiliary variable zt = [1/φ(B)]at. Then, we have
φ(B)zt = at,
yt = θ(B)zt.
Since zt is an AR(p) model, we can use the transition equation in Eq. (11.42) or
(11.43). If Eq. (11.42) is used, we can use yt = θ(B)zt to construct the measurement
equation as
yt = (−θp−1, −θp−2, . . . , −θ1, 1)st,
(11.44)
where it is understood that p > q and θj = 0 for j > q. On the other hand, if Eq.
(11.43) is used as the transition equation, we construct the measurement equation
as
yt = (−θp−1, −θp−2, . . . , −θ1, 1)st + at.
(11.45)
In summary, there are many state-space representations for an ARMA model.
Each representation has its pros and cons. For estimation and forecasting purposes,
one can choose any one of those representations. On the other hand, for a timeinvariant coefﬁcient state-space model in Eqs. (11.26) and (11.27), one can use the
Cayley–Hamilton theorem to show that the observation yt follows an ARMA(m, m)
model, where m is the dimension of the state vector.
SsfPack Command
In SsfPack/S-Plus, a command GetSsfArma can be used to transform an ARMA
model into a state-space form. Harvey’s approach is used. To illustrate, consider
the AR(1) model
yt = 0.6yt−1 + at,
at ∼N(0, 0.42).
The state-space form of the model is
> ssf.ar1 = GetSsfArma(ar=0.6,sigma=0.4)
> ssf.ar1
$mPhi:
[,1]
[1,]
0.6
[2,]
1.0
$mOmega:
[,1] [,2]
[1,] 0.16
0
[2,] 0.00
0
$mSigma:
[,1]
[1,] 0.25
[2,] 0.00
--- page 613 ---

586
state-space models and kalman ﬁlter
Since the AR(1) model is stationary, the program uses 1|0 = Var(yt) = (0.4)2/
(1 −0.62) = 0.25 and µ1|0 = 0. These values appear in the matrix mSigma.
As a second example, consider the ARMA(2,1) model
yt = 1.2yt−1 −0.35yt−2 + at −0.25at−1,
at ∼N(0, 1.12).
The state-space form of the model is
> arma21.m = list(ar=c(1.2,-0.35),ma=c(-0.25),sigma=1.1)
> ssf.arma21= GetSsfArma(model=arma21.m)
> ssf.arma21
$mPhi:
[,1] [,2]
[1,]
1.20
1
[2,] -0.35
0
[3,]
1.00
0
$mOmega:
[,1]
[,2] [,3]
[1,]
1.2100 -0.302500
0
[2,] -0.3025
0.075625
0
[3,]
0.0000
0.000000
0
$mSigma:
[,1]
[,2]
[1,]
4.060709 -1.4874057
[2,] -1.487406
0.5730618
[3,]
0.000000
0.0000000
As expected, the output shows that
T =

1.2
1
−0.35
0

,
Z = (1, 0),
and mPhi and mOmega follow the format of Eq. (11.28), and the covariance matrix
of (s1t, s2t)′ is used in mSigma, where s1t = yt and s2t = −0.35yt−1 −0.25yt−2.
Note that in SsfPack, the MA polynomial of an ARMA model assumes the form
θ(B) = 1 + θ1B + . . . + θqBq, not the form θ(B) = 1 −θ1B −. . . −θqBq commonly used in the literature.
11.3.3
Linear Regression Model
Multiple linear regression models can also be represented in state-space form.
Consider the model
yt = x′
tβ + et,
et ∼N(0, σ 2
e ),
--- page 614 ---

model transformation
587
where xt is a p-dimensional explanatory variable and β is a p-dimensional parameter vector. Let st = β for all t. Then the model can be written as

 st+1
yt

=

 I p
x′
t

st +

 0p
et

.
(11.46)
Thus, the system matrices are T t = I p, Zt = x′
t, dt = 0, ct = 0, Qt = 0, and
H t = σ 2
e . Since the state vector is ﬁxed, a diffuse initialization should be used.
One can extend the regression model so that βt is random, say,
βt+1 = βt + Rtηt,
ηt ∼N(0, 1),
and Rt = (σ1, . . . , σp)′ with σi ≥0. If σi = 0, then βi is time invariant.
SsfPack Command
In SsfPack, the command GetSsfReg creates a state-space form for the multiple
linear regression model. The command has an input argument that contains the data
matrix of explanatory variables. To illustrate, consider the simple market model
rt = β0 + β1rM,t + et,
t = 1, . . . , 168,
where rt is the return of an asset and rM,t is the market return, for example, the
S&P 500 composite index return. The state-space form can be obtained as
> ssf.reg=GetSsfReg(cbind(1,sp)) % ’sp’ is market return.
> ssf.reg
$mPhi:
[,1] [,2]
[1,]
1
0
[2,]
0
1
[3,]
0
0
$mOmega:
[,1] [,2] [,3]
[1,]
0
0
0
[2,]
0
0
0
[3,]
0
0
1
$mSigma:
[,1] [,2]
[1,]
-1
0
[2,]
0
-1
[3,]
0
0
$mJPhi:
[,1] [,2]
[1,]
-1
-1
[2,]
-1
-1
[3,]
1
2
$mX:
--- page 615 ---

588
state-space models and kalman ﬁlter
numeric matrix: 168 rows, 2 columns.
sp
[1,] 1 -0.075187
...
[168,] 1
0.05002
11.3.4
Linear Regression Models with ARMA Errors
Consider the regression model with ARMA(p, q) errors:
yt = x′
tβ + zt,
φ(B)zt = θ(B)at,
(11.47)
where at ∼N(0, σ 2
a ) and xt is a k-dimensional vector of explanatory variables. A
special case of this model is the nonzero mean ARMA(p, q) model in which xt
= 1 for all t and β becomes a scalar parameter. Let st be a state vector for the zt
series, for example, that deﬁned in Eq. (11.39). We can deﬁne a state vector s∗
t for
yt as
s∗
t =

 st
βt

,
(11.48)
where βt = β for all t. Then, a state-space form for yt is
s∗
t+1 = T ∗s∗
t + R∗ηt,
(11.49)
yt = Z∗
t s∗
t ,
(11.50)
where Z∗
t = (1, 0, . . . , 0, x′
t)1×(m+k), m = max(p, q + 1), and
T ∗=

 T
0
0
I k

,
R∗=

 R
0

,
where T and R are deﬁned in Eq. (11.39). In a compact form, we have the statespace model

 s∗
t+1
yt

=

 T ∗
Z∗
t

s∗
t +

 R∗ηt
0

.
SsfPack Command
SsdPack uses the command GetSsfRegArma to construct a state-space form for
linear regression models with ARMA errors. The arguments of the command can be
found using the command args(GetSsfRegArma). They consist of a data matrix
for the explanatory variables and ARMA model speciﬁcation. To illustrate, consider
the model
--- page 616 ---

model transformation
589
yt = β0 + β1xt + zt,
t = 1, · · · , 168,
zt = 1.2zt−1 −0.35zt−2 + at −0.25at−1,
at ∼N(0, σ 2
a ).
We use the notation X to denote the T × 2 matrix of regressors (1, xt). A state-space
form for the prior model can be obtained as
> ssf.reg.arma21=GetSsfRegArma(X,ar=c(1.2,-0.35),
+ ma=c(-0.25))
> ssf.reg.arma21
$mPhi:
[,1] [,2] [,3] [,4]
[1,]
1.20
1
0
0
[2,] -0.35
0
0
0
[3,]
0.00
0
1
0
[4,]
0.00
0
0
1
[5,]
1.00
0
0
0
$mOmega:
[,1]
[,2] [,3] [,4] [,5]
[1,]
1.00 -0.2500
0
0
0
[2,] -0.25
0.0625
0
0
0
[3,]
0.00
0.0000
0
0
0
[4,]
0.00
0.0000
0
0
0
[5,]
0.00
0.0000
0
0
0
$mSigma:
[,1]
[,2] [,3] [,4]
[1,]
3.35595 -1.229260
0
0
[2,] -1.22926
0.473604
0
0
[3,]
0.00000
0.000000
-1
0
[4,]
0.00000
0.000000
0
-1
[5,]
0.00000
0.000000
0
0
$mJPhi:
[,1] [,2] [,3] [,4]
[1,]
-1
-1
-1
-1
[2,]
-1
-1
-1
-1
[3,]
-1
-1
-1
-1
[4,]
-1
-1
-1
-1
[5,]
-1
-1
1
2
$mX:
numeric matrix: 168 rows, 2 columns.
xt
[1,] 1 0.4993
...
[168,] 1 0.7561
--- page 617 ---

590
state-space models and kalman ﬁlter
11.3.5
Scalar Unobserved Component Model
The basic univariate unobserved component model, or the structural time series
model (STSM), assumes the form
yt = µt + γt + ωt + et,
(11.51)
where µt, γt, and ωt represent the unobserved trend, seasonal, and cycle components, respectively, and et is the unobserved irregular component. In the literature,
a nonstationary (possibly double-unit-root) model is commonly used for the trend
component:
µt+1 = µt + βt + ηt,
ηt ∼N(0, σ 2
η ),
(11.52)
βt = βt−1 + ςt,
ςt ∼N(0, σ 2
ς ),
where µ1 ∼N(0, ξ) and β1 ∼N(0, ξ) with ξ a large real number, for example, ξ =
108. See, for instance, Kitagawa and Gersch (1996). If σς = 0, then µt follows a
random walk with drift β1. If σς = ση = 0, then µt represents a linear deterministic
trend.
The seasonal component γt assumes the form
(1 + B + · · · + Bs−1)γt = ωt,
ωt ∼N(0, σ 2
ω),
(11.53)
where s is the number of seasons in a year, that is, the period of the seasonality. If σω = 0, then the seasonal pattern is deterministic. The cycle component is
postulated as

 ωt+1
ω∗
t+1

= δ

cos(λc)
sin(λc)
−sin(λc)
cos(λc)

 ωt
ω∗
t

+

 εt
ε∗
t

,
(11.54)
where

 εt
ε∗
t

∼N

 0
0

, σ 2
ε (1 −δ2)I 2

,
ω0 ∼N(0, σ 2
ε ), ω∗
0 ∼N(0, σ 2
ε ), and Cov(ω0, ω∗
0) = 0, δ ∈(0, 1] is called a damping factor, and the frequency of the cycle is λc = 2π/q with q being the period.
If δ = 1, then the cycle becomes a deterministic sine–cosine wave.
SsfPack/S-Plus Command
The command GetSsfStsm constructs a state-space form for the structural time
series model. It allows for 10 cycle components; see the output of the command
args(GetSsfStsm). Table 11.4 provides a summary of the arguments and their
corresponding symbols of the model. To illustrate, consider the local trend model
in Eqs. (11.1) and (11.2) with σe = 0.4 and ση = 0.2. This is a special case of the
scalar unobserved component model. One can obtain a state-space form as
--- page 618 ---

kalman ﬁlter and smoothing
591
TABLE 11.4
Arguments of Command GetSsfStsm in SsfPack/S-Plus
Argument
STSM parameter
irregular
σe
level
ση
slope
σς
seasonalDummy
σω, s
seasonalTrig
σω, s
SeasonalHS
σω, s
Cycle0
σε, λc, δ
...
...
Cycle9
σε, λc, δ
> ssf.stsm=GetSsfStsm(irregular=0.4,level=0.2)
> ssf.stsm
$mPhi:
[,1]
[1,]
1
[2,]
1
$mOmega:
[,1] [,2]
[1,] 0.04 0.00
[2,] 0.00 0.16
$mSigma:
[,1]
[1,]
-1
[2,]
0
11.4
KALMAN FILTER AND SMOOTHING
In this section, we study the Kalman ﬁlter and various smoothing methods for
the general state-space model in Eqs. (11.26) and (11.27). The derivation follows
closely the steps taken in Section 11.1. For readers interested in applications, this
section can be skipped at the ﬁrst read. A good reference for this section is Durbin
and Koopman (2001, Chapter 4).
11.4.1
Kalman Filter
Recall that the aim of the Kalman ﬁlter is to obtain recursively the conditional
distribution of st+1 given the data Ft = {y1, . . . , yt} and the model. Since the
conditional distribution involved is normal, it sufﬁces to study the conditional mean
and covariance matrix. Let sj|i and j|i be the conditional mean and covariance
matrix of sj given Fi, that is, sj|Fi ∼N(sj|i, j|i). From Eq. (11.26),
--- page 619 ---

592
state-space models and kalman ﬁlter
st+1|t = E(dt + T tst + Rtηt|Ft) = dt + T tst|t,
(11.55)
t+1|t = Var(T tst + Rtηt|Ft) = T tt|tT ′
t + RtQtR′
t.
(11.56)
Similarly to that of Section 11.1, let yt|t−1 be the conditional mean of yt given
Ft−1. From Eq. (11.27),
yt|t−1 = ct + Ztst|t−1.
Let
vt = yt −yt|t−1 = yt −(ct + Ztst|t−1) = Zt(st −st|t−1) + et,
(11.57)
be the 1-step-ahead forecast error of yt given Ft−1. It is easy to see that (a)
E(vt|Ft−1) = 0; (b) vt is independent of Ft−1, that is, Cov(vt, yj) = 0 for 1 ≤
j < t; and (c) {vt} is a sequence of independent normal random vectors. Also, let
V t = Var(vt|Ft−1) = Var(vt) be the covariance matrix of the 1-step-ahead forecast
error. From Eq. (11.57), we have
V t = Var[Zt(st −st|t−1) + et] = Ztt|t−1Z′
t + H t.
(11.58)
Since Ft = {Ft−1, yt} = {Ft−1, vt}, we can apply Theorem 11.1 to obtain
st|t = E(st|Ft) = E(st|Ft−1, vt)
= E(st|Ft−1) + Cov(st, vt)[Var(vt)]−1vt
= st|t−1 + CtV −1
t vt,
(11.59)
where Ct = Cov(st, vt|Ft−1) given by
Ct = Cov(st, vt|Ft−1) = Cov[st, Zt(st −st|t−1) + et|Ft−1]
= Cov[st, Zt(st −st|t−1)|Ft−1] = t|t−1Z′
t.
Here we assume that V t is invertible because H t is. Using Eqs. (11.55) and (11.59),
we obtain
st+1|t = dt + T tst|t−1 + T tCtV −1
t vt = dt + T tst|t−1 + Ktvt,
(11.60)
where
Kt = T tCtV −1
t
= T tt|t−1Z′
tV −1
t ,
(11.61)
--- page 620 ---

kalman ﬁlter and smoothing
593
which is the Kalman gain at time t. Applying Theorem 11.1(2), we have
t|t = Var(st|Ft−1, vt)
= Var(st|Ft−1) −Cov(st, vt)[Var(vt)]−1Cov(st, vt)′
= t|t−1 −CtV −1
t C′
t
= t|t−1 −t|t−1Z′
tV −1
t Ztt|t−1.
(11.62)
Plugging Eq. (11.62) into Eq. (11.56) and using Eq. (11.61), we obtain
t+1|t = T tt|t−1L′
t + RtQtR′
t,
(11.63)
where
Lt = T t −KtZt.
Putting the prior equations together, we obtain the celebrated Kalman ﬁlter for the
state-space model in Eqs. (11.26) and (11.27). Given the starting values s1|0 and
1|0, the Kalman ﬁlter algorithm is
vt = yt −ct −Ztst|t−1,
V t = Ztt|t−1Z′
t + H t,
Kt = T tt|t−1Z′
tV −1
t ,
(11.64)
Lt = T t −KtZt,
st+1|t = dt + T tst|t−1 + Ktvt,
t+1|t = T tt|t−1L′
t + RtQtR′
t,
t = 1, . . . , T.
If the ﬁltered quantities st|t and t|t are also of interest, then we modify the ﬁlter
to include the contemporaneous ﬁltering equations in Eqs. (11.59) and (11.62). The
resulting algorithm is
vt = yt −ct −Ztst|t−1,
Ct = t|t−1Z′
t,
V t = Ztt|t−1Z′
t + H t = ZtCt + H t,
st|t = st|t−1 + CtV −1
t vt,
t|t = t|t−1 −CtV −1
t C′
t,
st+1|t = dt + T tst|t,
t+1|t = T tt|tT ′
t + RtQtR′
t.
--- page 621 ---

594
state-space models and kalman ﬁlter
Steady State
If the state-space model is time invariant, that is, all system matrices are time
invariant, then the matrices t|t−1 converge to a constant matrix ∗, which is a
solution of the matrix equation
∗= T ∗T ′ −T ∗ZV −1Z∗T ′ + RQR′,
where V = Z∗Z′ + H. The solution that is reached after convergence to ∗is
referred to as the steady-state solution of the Kalman ﬁlter. Once the steady state is
reached, V t, Kt, and t+1|t are all constant. This can lead to considerable saving
in computing time.
11.4.2
State Estimation Error and Forecast Error
Deﬁne the state prediction error as
xt = st −st|t−1.
From the deﬁnition, the covariance matrix of xt is Var(xt|Ft−1) = Var(st|Ft−1) =
t|t−1. Following Section 11.1, we investigate properties of xt. First, from Eq.
(11.57),
vt = Zt(st −st|t−1) + et = Ztxt + et.
Second, from Eqs. (11.64) and (11.26), and the prior equation, we have
xt+1 = st+1 −st+1|t
= T t(st −st|t−1) + Rtηt −Ktvt
= T txt + Rtηt −Kt(Ztxt + et)
= Ltxt + Rtηt −Ktet,
where, as before, Lt = T t −KtZt. Consequently, we obtain a state-space form for
vt as
vt = Ztxt + et,
xt+1 = Ltxt + Rtηt −Ktet,
(11.65)
with x1 = s1 −s1|0 for t = 1, . . . , T .
Finally, similar to the local-trend model in Section 11.1, we can show that the
1-step-ahead forecast errors {vt} are independent of each other and {vt, . . . , vT } is
independent of Ft−1.
--- page 622 ---

kalman ﬁlter and smoothing
595
11.4.3
State Smoothing
State smoothing focuses on the conditional distribution of st given FT . Notice that
(a) Ft−1 and {vt, . . . , vT } are independent and (b) vt are serially independent. We
can apply Theorem 11.1 to the joint distribution of st and {vt, . . . , vT } given Ft−1
and obtain
st|T = E(st|FT ) = E(st|Ft−1, vt, . . . , vT )
= E(st|Ft−1) +
T

j=t
Cov(st, vj)[Var(vj)]−1vj
= st|t−1 +
T

j=t
Cov(st, vj)V −1
j vj,
(11.66)
where the covariance matrices are conditional on Ft−1. The covariance matrices
Cov(st, vj) for j = t, . . . , T can be derived as follows. By Eq. (11.65),
Cov(st, vj) = E(stv′
j)
= E[st(Zjxj + ej)′] = E(stx′
j)Z′
j,
j = t, . . . , T.
(11.67)
Furthermore,
E(stx′
t) = E[st(st −st|t−1)′] = Var(st) = t|t−1,
E(stx′
t+1) = E[st(Ltxt + Rtηt −Ktet)′] = t|t−1L′
t,
E(stx′
t+2) = t|t−1L′
tL′
t+1,
(11.68)
...
E(stx′
T ) = t|t−1L′
t · · · L′
T −1.
Plugging the prior two equations into Eq. (11.66), we have
sT |T = sT |T −1 + T |T −1Z′
T V −1
T vT ,
sT −1|T = sT −1|T −2 + T −1|T −2Z′
T −1V −1
T −1vT −1 + T −1|T −2L′
T −1Z′
T V −1
T vT ,
st|T = st|t−1 + t|t−1Z′
tV −1
t vt + t|t−1L′
tZ′
t+1V −1
t+1vt+1
+ · · · + t|t−1L′
tL′
t+1 · · · L′
T −1Z′
T V −1
T vT ,
for t = T −2, T −3, . . . , 1, where it is understood that L′
t · · · L′
T −1 = I m when
t = T . These smoothed state vectors can be expressed as
st|T = st|t−1 + t|t−1qt−1,
(11.69)
--- page 623 ---

596
state-space models and kalman ﬁlter
where qT −1 = Z′
T V −1
T vT , qT −2 = Z′
T −1V −1
T −1vT −1 + L′
T −1Z′
T V −1
T vT , and
qt−1 = Z′
tV −1
t vt + L′
tZ′
t+1V −1
t+1vt+1 + · · · + L′
tL′
t+1 · · · L′
T −1Z′
T V −1
T vT ,
for t = T −2, T −3, . . . , 1. The quantity qt−1 is a weighted sum of the 1-stepahead forecast errors vj occurring after time t −1. From the deﬁnition in the prior
equation, qt can be computed recursively backward as
qt−1 = Z′
tV −1
t vt + L′
tqt,
t = T, . . . , 1,
(11.70)
with qT = 0. Putting the equations together, we have a backward recursion for the
smoothed state vectors as
qt−1 = Z′
tV −1
t vt + L′
tqt,
st|T = st|t−1 + t|t−1qt−1,
t = T, . . . , 1,
(11.71)
starting with qT = 0, where st|t−1, t|t−1, Lt, and V t are available from the Kalman
ﬁlter. This algorithm is referred to as the ﬁxed interval smoother in the literature;
see de Jong (1989) and the references therein.
Covariance Matrix of Smoothed State Vector
Next, we derive the covariance matrices of the smoothed state vectors. Applying
Theorem 11.1(4) to the conditional joint distribution of st and {vt, . . . , vT } given
Ft−1, we have
t|T = t|t−1 −
T

j=t
Cov(st, vj)[Var(vj)]−1[Cov(st, vj)]′.
Using the covariance matrices in Eqs. (11.67) and (11.68), we further obtain
t|T = t|t−1 −t|t−1Z′
tV −1
t Ztt|t−1 −t|t−1L′
tZ′
t+1V −1
t+1Zt+1Ltt|t−1
−· · · −t|t−1L′
t · · · L′
T −1Z′
T V −1
T ZT LT −1 · · · Ltt|t−1
= t|t−1 −t|t−1Mt−1t|t−1,
where
Mt−1 = Z′
tV −1
t Zt + L′
tZ′
t+1V −1
t+1Zt+1Lt
+ · · · + L′
t · · · L′
T −1Z′
T V −1
T ZT LT −1 · · · Lt.
Again, L′
t · · · LT −1 = I m when t = T . From its deﬁnition, the Mt−1 matrix satisﬁes
Mt−1 = Z′
tV −1
t Zt + L′
tMtLt,
t = T, . . . , 1,
(11.72)
--- page 624 ---

kalman ﬁlter and smoothing
597
with the starting value MT = 0. Collecting the results, we obtain a backward
recursion to compute t|T as
Mt−1 = Z′
tV −1
t Zt, +L′
tMtLt,
t|T = t|t−1 −t|t−1Mt−1t|t−1, (11.73)
for t = T, . . . , 1 with MT = 0. Note that, like that of the local trend model in
Section 11.1, Mt = Var(qt).
Combining the two backward recursions of smoothed state vectors, we have
qt−1 = Z′
tV −1
t vt + L′
tqt,
st|T = st|t−1 + t|t−1qt−1,
(11.74)
Mt−1 = Z′
tV −1
t Zt + L′
tMtLt,
t|T = t|t−1 −t|t−1Mt−1t|t−1,
t = T, . . . , 1,
with qT = 0 and MT = 0.
Suppose that the state-space model in Eqs. (11.26) and (11.27) is known. Application of the Kalman ﬁlter and state smoothing can proceed in two steps. First, the
Kalman ﬁlter in Eq. (11.64) is used for t = 1, . . . , T and the quantities vt,V t, Kt,
st|t−1, and t|t−1 are stored. Second, the state smoothing algorithm in Eq. (11.74)
is applied for t = T, T −1, . . . , 1 to obtain st|T and t|T .
11.4.4
Disturbance Smoothing
Let et|T = E(et|FT ) and ηt|T = E(ηt|FT ) be the smoothed disturbances of the
observation and transition equation, respectively. These smoothed disturbances are
useful in many applications, for example, in model checking. In this section, we
study recursive algorithms to compute smoothed disturbances and their covariance
matrices. Again, applying Theorem 11.1 to the conditional joint distribution of et
and {vt, . . . , vT } given Ft−1, we obtain
et|T = E(et|Ft−1, vt, . . . , vT ) =
T

j=t
E(etv′
j)V −1
j vj,
(11.75)
where E(et|Ft−1) = 0 is used. Using Eq. (11.65),
E(etv′
j) = E(etx′
j)Z′
j + E(ete′
j).
Since E(etx′
t) = 0, we have
E(etv′
j) =

H t,
if j = t,
E(etx′
j)Z′
j,
for j = t + 1, . . . , T.
(11.76)
--- page 625 ---

598
state-space models and kalman ﬁlter
Using Eq. (11.65) repeatedly and the independence between {et} and {ηt}, we
obtain
E(etx′
t+1) = −H tK′
t,
E(etx′
t+2) = −H tK′
tL′
t+1,
...
(11.77)
E(etx′
T ) = −H tK′
tL′
t+1 · · · L′
T −1,
where it is understood that L′
t+1 · · · L′
T −1 = I m if t = T −1. Based on Eqs. (11.76)
and (11.77),
et|T = H t(V −1
t vt −K′
tZ′
t+1V −1
t+1vt+1 −· · · −K′
tL′
t+1 · · · L′
T −1Z′
T V −1
T vT )
= H t(V −1
t vt −K′
tqt)
= H tot,
t = T, · · · , 1,
(11.78)
where qt is deﬁned in Eq. (11.69) and ot = V −1
t vt −K′
tqt. We refer to ot as the
smoothing measurement error.
The smoothed disturbance ηt|T can be derived analogously, and we have
ηt|T =
T

j=t
E(ηtv′
j)V −1
j vj.
(11.79)
The state-space form in Eq. (11.69) gives
E(ηtv′
j) =

QtR′
tZ′
t+1,
if j = t + 1,
E(ηtx′
j)Z′
j,
if j = t + 2, · · · , T,
where
E(ηtx′
t+2) = QtR′
tL′
t+1,
E(ηtx′
t+3) = QtR′
tL′
t+1L′
t+2,
...
E(ηtx′
T ) = QtR′
tL′
t+1 · · · L′
T −1,
for t = 1, . . . , T . Consequently, Eq. (11.79) implies
ηt|T = QtR′
t(Z′
t+1V −1
t+1vt+1 + L′
t+1Z′
t+2V −1
t+2vt+2
+ · · · + L′
t+1 · · · L′
T −1ZT V −1
T vT )
= QtR′
tqt,
t = T, . . . , 1,
(11.80)
--- page 626 ---

kalman ﬁlter and smoothing
599
where qt is deﬁned earlier in Eq. (11.70).
Koopman (1993) uses the smoothed disturbance ηt|T to derive a new recursion
for computing st|T . From the transition equation in Eq. (11.26),
st+1|T = dt + T tst|T + Rtηt|T .
Using Eq. (11.80), we have
st+1|T = dt + T tst|T + RtQtR′
tqt,
t = 1, . . . , T,
(11.81)
where the initial value is s1|T = s1|0 + 1|0q0 with q0 obtained from the recursion
in Eq. (11.70).
Covariance Matrices of Smoothed Disturbances
The covariance matrix of the smoothed disturbance can also be obtained using
Theorem 11.1. Speciﬁcally,
Var(et|FT ) = Var(et|Ft−1, vt, . . . , vT )
= Var(et|Ft−1) −
T

j=t
Cov(et, vj)V −1
j [Cov(et, vj)]′.
Note that Cov(et, vj) = E(etv′
j), which is given in Eq. (11.76). Thus, we have
Var(et|FT ) = H t −H t(V −1
t
+ K′
tZ′
t+1V −1
t+1Zt+1Kt
+ K′
tL′
t+1Z′
t+2V −1
t+2Zt+2Lt+1Kt
+ · · · + K′
tL′
t+1 · · · L′
T −1Z′
T V −1
T ZT LT −1 · · · Lt+1Kt)H t
= H t −H t(V −1
t
+ K′
tMtKt)H t
= H t −H tNtH t,
where Nt = V −1
t
+ K′
tMtKt, where Mt is given in Eq. (11.72). Similarly,
Var(ηt|FT ) = Var(ηt) −
T

j=t
Cov(ηt, vt)V −1
t [Cov(ηt, vt)]−1,
where Cov(ηt, vj) = E(ηtv′
j), which is given before when we derived the formula
for ηt|T . Consequently,
Var(ηt|FT ) = Qt −QtR′
t(Z′
t+1V −1
t+1Zt+1 + L′
t+1Z′
t+2V −1
t+2Zt+2Lt+1
+ · · · + L′
t+1 · · · L′
T −1Z′
T V −1
T ZT LT −1 · · · Lt+1)RtQt
= Qt −QtR′
tMtRtQt.
--- page 627 ---

600
state-space models and kalman ﬁlter
In summary, the disturbance smoothing algorithm is as follows:
et|T = H t(V −1
t vt −K′
tqt),
ηt|T = QtR′
tqt,
qt−1 = Z′
tV −1
t vt + L′
tqt,
(11.82)
Var(et|FT ) = H t −H t(V −1
t
+ K′
tMtKt)H t,
Var(ηt|FT ) = Qt −QtR′
tMtRtQt,
Mt−1 = Z′
tV −1
t Zt + L′
tMtLt,
t = T, . . . , 1,
where qT = 0 and MT = 0.
11.5
MISSING VALUES
For the general state-space model in Eqs. (11.26) and (11.27), we consider two
cases of missing values. First, suppose that similar to the local trend model in
Section 11.1 the observations yt at t = ℓ+ 1, . . . , ℓ+ h are missing. In this case,
there is no new information available at these time points and we set
vt = 0,
Kt = 0,
for
t = ℓ+ 1, . . . , ℓ+ h.
The Kalman ﬁlter in Eq. (11.64) can then proceed as usual. That is,
st+1|t = dt + T tst|t−1,
t+1|t = T tt|t−1T ′
t + RtQtR′
t,
for t = ℓ+ 1, . . . , ℓ+ h. Similarly, the smoothed state vectors can be computed
as usual via Eq. (11.74) with
qt−1 = T ′
tqt,
Mt−1 = T ′
tMtT t,
for t = ℓ+ 1, . . . , ℓ+ h.
In the second case, some components of yt are missing. Let y∗
t = Jyt be the
vector of observed data at time t, where J is an indicator matrix identifying the
observed data. More speciﬁcally, rows of J are a subset of the rows of the k × k
identity matrix. In this case, the observation equation (11.27) of the model can be
transformed as
y∗
t = c∗
t + Z∗
t st + e∗
t ,
where c∗
t = Jct, Z∗
t = JZt, and e∗
t = Jet with covariance matrix Var(e∗
t ) = H ∗
t =
JH tJ ′. The Kalman ﬁlter and state-smoothing recursion continue to apply except
that the modiﬁed observation equation is used at time t. Consequently, the ease in
handling missing values is a nice feature of the state-space model.
--- page 628 ---

forecasting
601
11.6
FORECASTING
Suppose that the forecast origin is t and we are interested in predicting yt+j
for j = 1, . . . , h, where h > 0. Also, we adopt the minimum mean-squared error
forecasts. Similar to the ARMA models, the j-step-ahead forecast yt(j) turns out to
be the expected value of yt+j given Ft and the model. That is, yt(j) = E(yt+j|Ft).
In what follows, we show that these forecasts and the covariance matrices of the
associated forecast errors can be obtained via the Kalman ﬁlter in Eq. (11.64) by
treating {yt+1, . . . , yt+h} as missing values, that is, the ﬁrst case in Section 11.5.
Consider the 1-step-ahead forecast. From Eq. (11.27),
yt(1) = E(yt+1|Ft) = ct+1 + Zt+1st+1|t,
where st+1|t is available via the Kalman ﬁlter at the forecast origin t. The associated
forecast error is
et(1) = yt+1 −yt(1) = Zt+1(st+1 −st+1|t) + et+1.
Therefore, the covariance matrix of the 1-step-ahead forecast error is
Var[et(1)] = Zt+1t+1|tZ′
t+1 + H t+1.
This is precisely the covariance matrix V t+1 of the Kalman ﬁlter in Eq. (11.64).
Thus, we have showed the case for h = 1.
Now, for h > 1, we consider 1-stepto h-step-ahead forecasts sequentially. From
Eq. (11.27), the j-step-ahead forecast is
yt(j) = ct+j + Zt+jst+j|t,
(11.83)
and the associated forecast error is
et(j) = Zt+j(st+j −st+j|t) + et+j.
Recall that st+j|t and t+j|t are, respectively, the conditional mean and covariance
matrix of st+j given Ft. The prior equation says that
Var[et(j)] = Zt+jt+j|tZ′
t+j + H t+j.
(11.84)
Furthermore, from Eq. (11.26),
st+j+1|t = dt+j + T t+jst+j|t,
which in turn implies that
st+j+1 −st+j+1|t = T t+j(st+j −st+j|t) + Rt+jηt+j.
