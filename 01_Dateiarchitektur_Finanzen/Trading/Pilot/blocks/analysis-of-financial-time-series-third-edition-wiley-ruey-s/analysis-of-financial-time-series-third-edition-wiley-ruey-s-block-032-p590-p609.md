# Analysis of Financial Time Series, Third Edition (Wiley -- Ruey S_ Tsay -- Wiley series in probability and statistics, 3rd ed_, -- John Wiley & Sons, -- isbn13 9780470414354 -- 9f99b80c7b2dedd477f463dc5323f3b6 -- An.pdf — pages 590–609

--- page 590 ---

local trend model
563

 µt
vt

Ft−1
∼N

 µt|t−1
0

,

 t|t−1
t|t−1
t|t−1
Vt

.
By Theorem 11.1, the conditional distribution of µt given Ft is normal with mean
and variance
µt|t = µt|t−1 + t|t−1vt
Vt
= µt|t−1 + Ktvt,
(11.10)
t|t = t|t−1 −
2
t|t−1
Vt
= t|t−1(1 −Kt),
(11.11)
where Kt = t|t−1/Vt is commonly referred to as the Kalman gain, which is the
regression coefﬁcient of µt on vt. From Eq. (11.10), Kalman gain is the factor that
governs the contribution of the new shock vt to the state variable µt.
Next, one can make use of the knowledge of µt given Ft to predict µt+1 via
Eq. (11.2). Speciﬁcally, we have
µt+1|t = E(µt + ηt|Ft) = E(µt|Ft) = µt|t,
(11.12)
t+1|t = Var(µt+1|Ft) = Var(µt|Ft) + Var(ηt) = t|t + σ 2
η .
(11.13)
Once the new data yt+1 is observed, one can repeat the above procedure to update
knowledge of µt+1. This is the famous Kalman ﬁlter algorithm proposed by Kalman
(1960).
In summary, putting Eqs. (11.7) and (11.13) together and conditioning on the
initial assumption that µ1 is distributed as N(µ1|0, 1|0), the Kalman ﬁlter for the
local trend model is as follows:
vt = yt −µt|t−1,
Vt = t|t−1 + σ 2
e ,
Kt = t|t−1/Vt,
(11.14)
µt+1|t = µt|t−1 + Ktvt,
t+1|t = t|t−1(1 −Kt) + σ 2
η ,
t = 1, . . . , T.
There are many ways to derive the Kalman ﬁlter. We use Theorem 11.1, which
describes some properties of multivariate normal distribution, for its simplicity. In
practice, the choice of initial values 1|0 and µ1|0 requires some attention and we
shall discuss it later in Section 11.1.6. For the local trend model in Eqs. (11.1) and
(11.2), the two parameters σe and ση can be estimated via the maximum-likelihood
method. Again, the Kalman ﬁlter is useful in evaluating the likelihood function of
the data in estimation. We shall discuss estimation in Section 11.1.7.
--- page 591 ---

564
state-space models and kalman ﬁlter
Day
(a)
Filtered state
0
100
200
300
0.4
0.8
1.2
1.6
v(t)
−2
−1
0
1
2
Day
(b)
0
100
200
300
Figure 11.2
Time plots of output of Kalman ﬁlter applied to daily realized log volatility of Alcoa
stock based on local trend state-space model: (a) ﬁltered state µt|t and (b) 1-step-ahead forecast error vt.
Example 11.1 (Continued).
To illustrate application of the Kalman ﬁlter, we
use the ﬁtted state-space model for daily realized volatility of Alcoa stock returns
and apply the Kalman ﬁlter algorithm to the data with 1|0 = ∞and µ1|0 = 0. The
choice of these initial values will be discussed in Section 11.1.6. Figure 11.2(a)
shows the time plot of the ﬁltered state variable µt|t, and Figure 11.2(b) is the time
plot of the 1-step-ahead forecast error vt. Compared with Figure 11.1, the ﬁltered
states are smoother. The forecast errors appear to be stable and center around zero.
These forecast errors are out-of-sample 1-step-ahead prediction errors.
11.1.3
Properties of Forecast Error
The 1-step-ahead forecast errors {vt} are useful in many applications, hence it pays
to study carefully their properties. Given the initial values 1|0 and µ1|0, which
are independent of yt, the Kalman ﬁlter enables us to compute vt recursively as a
linear function of {y1, . . . , yt}. Speciﬁcally, by repeated substitutions,
v1 = y1 −µ1|0,
v2 = y2 −µ2|1 = y2 −µ1|0 −K1(y1 −µ1|0),
v3 = y3 −µ3|2 = y3 −µ1|0 −K2(y2 −µ1|0) −K1(1 −K2)(y1 −µ1|0),
--- page 592 ---

local trend model
565
and so on. This transformation can be written in matrix form as
v = K(y −µ1|01T ),
(11.15)
where v = (v1, . . . , vT )′, y = (y1, . . . , yT )′, 1T is the T -dimensional vector of
ones, and K is a lower triangular matrix deﬁned as
K =


1
0
0
· · ·
0
k21
1
0
· · ·
0
k31
k32
1
0
...
...
...
kT 1
kT 2
kT 3
· · ·
1


,
where ki,i−1 = −Ki−1 and kij = −(1 −Ki−1)(1 −Ki−2) · · · (1 −Kj+1)Kj for i =
2, . . . , T and j = 1, . . . , i −2. It should be noted that, from the deﬁnition, the
Kalman gain Kt does not depend on µ1|0 or the data {y1, . . . , yt}; it depends on
1|0 and σ 2
e and σ 2
η .
The transformation in Eq. (11.5) has several important implications. First, {vt}
are mutually independent under the normality assumption. To show this, consider
the joint probability density function of the data
p(y1, . . . , yT ) = p(y1)
T
j=2
p(yj|Fj−1).
Equation (11.15) indicates that the transformation from yt to vt has a unit Jacobian
so that p(v) = p(y). Furthermore, since µ1|0 is given, p(v1) = p(y1). Consequently, the joint probability density function of v is
p(v) = p(y) = p(y1)
T
j=2
p(yj|Fj−1) = p(v1)
T
j
p(vj) =
T
j=1
p(vj).
This shows that {vt} are mutually independent.
Second, the Kalman ﬁlter provides a Cholesky decomposition of the covariance
matrix of y. To see this, let  = Cov(y). Equation (11.15) shows that Cov(v) =
KK′. On the other hand, {vt} are mutually independent with Var(vt) = Vt. Therefore, KK′ = diag{V1, . . . , VT }, which is precisely a Cholesky decomposition of
. The elements kij of the matrix K thus have some nice interpretations; see
Chapter 10.
State Error Recursion
Turn to the estimation error of the state variable µt. Deﬁne
xt = µt −µt|t−1
--- page 593 ---

566
state-space models and kalman ﬁlter
as the forecast error of the state variable µt given data Ft−1. From Section 11.1.1,
Var(xt|Ft−1) = t|t−1. From the Kalman ﬁlter in Eq. (11.14),
vt = yt −µt|t−1 = µt + et −µt|t−1 = xt + et,
and
xt+1 = µt+1 −µt+1|t = µt + ηt −(µt|t−1 + Ktvt)
= xt + ηt −Ktvt = xt + ηt −Kt(xt + et) = Ltxt + ηt −Ktet,
where Lt = 1 −Kt = 1 −t|t−1/Vt = (Vt −t|t−1)/Vt = σ 2
e /Vt. Consequently,
for the state errors, we have
vt = xt + et,
xt+1 = Ltxt + ηt −Ktet,
t = 1, . . . , T,
(11.16)
where x1 = µ1 −µ1|0. Equation (11.16) is in the form of a time-varying state-space
model with xt being the state variable and vt the observation.
11.1.4
State Smoothing
Next we consider the estimation of the state variables {µ1, . . . , µT } given the data
FT and the model. That is, given the state-space model in Eqs. (11.1) and (11.2),
we wish to obtain the conditional distribution µt|FT for all t. To this end, we ﬁrst
recall some facts available about the model:
• All distributions involved are normal so that we can write the conditional
distribution of µt given FT as N(µt|T , t|T ), where t ≤T . We refer to µt|T
as the smoothed state at time t and t|T as the smoothed state variance.
• Based on the properties of {vt} shown in Section 11.1.3, {v1, . . . , vT } are
mutually independent and are linear functions of {y1, . . . , yT }.
• If y1, . . . , yT are ﬁxed, then Ft−1 and {vt, . . . , vT } are ﬁxed, and vice versa.
• {vt, . . . , vT } are independent of Ft−1 with mean zero and variance Var(vj) =
Vj for j ≥t.
Applying Theorem 11.1(3) to the conditional joint distribution of (µt,
vt, . . . , vT ) given Ft−1, we have
µt|T = E(µt|FT ) = E(µt|Ft−1, vt, . . . , vT )
= E(µt|Ft−1) + Cov[µt, (vt, . . . , vT )′]Cov[(vt, . . . , vT )′]−1(vt, . . . , vT )′
= µt|t−1 +


Cov(µt, vt)
Cov(µt, vt+1)
...
Cov(µt, vT )


′ 

Vt
0
· · ·
0
0
Vt+1
· · ·
0
...
...
...
0
0
· · ·
VT


−1 

vt
vt+1
...
vT


--- page 594 ---

local trend model
567
= µt|t−1 +
T

j=t
Cov(µt, vj)V −1
j
vj.
(11.17)
From the deﬁnition and independence of {vt}, Cov(µt, vj) = Cov(xt, vj) for j =
t, . . . , T , and
Cov(xt, vt) = E[xt(xt + et)] = Var(xt) = t|t−1,
Cov(xt, vt+1) = E[xt(xt+1 + et+1)] = E[xt(Ltxt + ηt −Ktet)] = t|t−1Lt.
Similarly, we have
Cov(xt, vt+2) = E[xt(xt+2 + et+2)] = · · · = t|t−1LtLt+1,
...
Cov(xt, vT ) = E[xt(xT + eT )] = · · · = t|t−1
T −1

j=t
Lj.
Consequently, Eq. (11.17) becomes
µt|T = µt|t−1 + t|t−1
vt
Vt
+ t|t−1Lt
vt+1
Vt+1
+ t|t−1LtLt+1
vt+2
Vt+2
+ · · ·
≡µt|t−1 + t|t−1qt−1,
where
qt−1 = vt
Vt
+ Lt
vt+1
Vt+1
+ LtLt+1
vt+2
Vt+2
+ · · · +


T −1

j=t
Lj

vT
VT
(11.18)
is a weighted linear combination of the innovations {vt, . . . , vT }. This weighted
sum satisﬁes
qt−1 = vt
Vt
+ Lt

vt+1
Vt+1
+ Lt+1
vt+2
Vt+2
+ · · · +


T −1

j=t+1
Lj

vT
VT


= vt
Vt
+ Ltqt.
Therefore, using the initial value qT = 0, we have the backward recursion
qt−1 = vt
Vt
+ Ltqt,
t = T, T −1, . . . , 1.
(11.19)
Putting Eqs. (11.17) and (11.19) together, we have a backward recursive algorithm
to compute the smoothed state variables:
--- page 595 ---

568
state-space models and kalman ﬁlter
qt−1 = V −1
t
vt + Ltqt,
µt|T = µt|t−1 + t|t−1qt−1,
t = T, . . . , 1,
(11.20)
where qT = 0, and µt|t−1, t|t−1 and Lt are available from the Kalman ﬁlter in
Eq. (11.14).
Smoothed State Variance
The variance of the smoothed state variable µt|T can be derived in a similar manner
via Theorem 11.1(4). Speciﬁcally, letting vT
t = (vt, . . . , vT )′, we have
t|T = Var(µt|FT ) = Var(µt|Ft−1, vt, . . . , vT )
= Var(µt|Ft−1) −Cov[µt, (vT
t )′]Cov[(vT
t )]−1Cov[µt, (vT
t )]
= t|t−1 −
T

j=t
[Cov(µt, vj)]2V −1
j
,
(11.21)
where Cov(µt, vj) = Cov(xt, vj) are given earlier after Eq. (11.17). Thus,
t|T = t|t−1 −2
t|t−1
1
Vt
−2
t|t−1L2
t
1
Vt+1
−· · · −2
t|t−1


T −1

j=t
L2
j

1
VT
≡t|t−1 −2
t|t−1Mt−1,
(11.22)
where
Mt−1 = 1
Vt
+ L2
t
1
Vt+1
+ L2
t L2
t+1
1
Vt+2
+ · · · +


T −1

j=t
L2
j

1
VT
,
is a weighted linear combination of the inverses of variances of the 1-step-ahead
forecast errors after time t −1. Let MT = 0 because no 1-step-ahead forecast error
is available after time index T . The statistic Mt−1 can be written as
Mt−1 = 1
Vt
+ L2
t

1
Vt+1
+ L2
t+1
1
Vt+2
+ · · · +


T −1

j=t+1
L2
j

1
VT


= 1
Vt
+ L2
t Mt,
t = T, T −1, . . . , 1.
Note that from the independence of {vt} and Eq. (11.18), we have
Var(qt−1) = 1
Vt
+ L2
t
1
Vt+1
+ · · · +


T −1

j=t
L2
j

1
VT
= Mt−1.
--- page 596 ---

local trend model
569
Day
Value
0
100
200
300
0.0
0.5
1.0
1.5
2.0
2.5
Figure 11.3
Filtered state variable µt|t and its 95% pointwise conﬁdence interval for daily log realized
volatility of Alcoa stock returns based on ﬁtted local-trend state-space model.
Combining the results, variances of the smoothed state variables can be computed
efﬁciently via the backward recursion
Mt−1 = V −1
t
+ L2
t Mt,
t|T = t|t−1 −2
t|t−1Mt−1,
t = T, . . . , 1,
(11.23)
where MT = 0.
Example 11.1 (Continued).
Applying the Kalman ﬁlter and state-smoothing
algorithms in Eqs. (11.20) and (11.23) to the daily realized volatility of Alcoa stock
using the ﬁtted state-space model, we can easily compute the ﬁltered state µt|t and
the smoothed state µt|T and their variances. Figure 11.3 shows the ﬁltered state
variable and its 95% pointwise conﬁdence interval, whereas Figure 11.4 provides
the time plot of smoothed state variable and its 95% pointwise conﬁdence interval.
As expected, the smoothed state variables are smoother than the ﬁltered state variables. The conﬁdence intervals for the smoothed state variables are also narrower
than those of the ﬁltered state variables. Note that the width of the 95% conﬁdence
interval of µ1|1 depends on the initial value 1|0.
--- page 597 ---

570
state-space models and kalman ﬁlter
Day
Value
0
100
200
300
0.0
0.5
1.0
1.5
2.0
2.5
Figure 11.4
Smoothed state variable µt|T and its 95% pointwise conﬁdence interval for daily log
realized volatility of Alcoa stock returns based on ﬁtted local-trend state-space model.
11.1.5
Missing Values
An advantage of the state-space model is in handling missing values. Suppose
that the observations {yt}ℓ+h
t=ℓ+1 are missing, where h ≥1 and 1 ≤ℓ< T . There
are several ways to handle missing values in state-space formulation. Here we
discuss a method that keeps the original time scale and model form. For t ∈{ℓ+
1, . . . , ℓ+ h}, we can use Eq. (11.2) to express µt as a linear combination of µℓ+1
and {ηj}t−1
j=ℓ+1. Speciﬁcally,
µt = µt−1 + ηt−1 = · · · = µℓ+1 +
t−1

j=ℓ+1
ηj,
where it is understood that the summation term is zero if its lower limit is greater
than its upper limit. Therefore, for t ∈{ℓ+ 1, . . . , ℓ+ h},
E(µt|Ft−1) = E(µt|Fℓ) = µℓ+1|ℓ,
Var(µt|Ft−1) = Var(µt|Fℓ) = ℓ+1|ℓ+ (t −ℓ−1)σ 2
η .
Consequently, we have
µt|t−1 = µt−1|t−2,
t|t−1 = t−1|t−2 + σ 2
η ,
(11.24)
--- page 598 ---

local trend model
571
for t = ℓ+ 2, . . . , ℓ+ h. These results show that we can continue to apply the
Kalman ﬁlter algorithm in Eq. (11.14) by taking vt = 0 and Kt = 0 for t = ℓ+
1, . . . , ℓ+ h. This is rather natural because when yt is missing, there is no new
innovation or new Kalman gain so that vt = 0 and Kt = 0.
11.1.6
Effect of Initialization
In this section, we consider the effects of initial condition µ1 ∼N(µ1|0, 1|0) on
the Kalman ﬁlter and state smoothing. From the Kalman ﬁlter in Eq. (11.14),
v1 = y1 −µ1|0,
V1 = 1|0 + σ 2
e ,
and, by Eqs. (11.10)–(11.13),
µ2|1 = µ1|0 + 1|0
V1
v1 = µ1|0 +
1|0
1|0 + σ 2e
(y1 −µ1|0),
2|1 = 1|0

1 −
1|0
1|0 + σ 2e

+ σ 2
η =
1|0
1|0 + σ 2e
σ 2
e + σ 2
η .
Therefore, letting 1|0 increase to inﬁnity, we have µ2|1 = y1 and 2|1 = σ 2
e + σ 2
η .
This is equivalent to treating y1 as ﬁxed and assuming µ1 ∼N(y1, σ 2
e ). In the literature, this approach to initializing the Kalman ﬁlter is called diffuse initialization
because a very large 1|0 means one is uncertain about the initial condition.
Next, turn to the effect of diffuse initialization on state smoothing. It is obvious
that based on the results of Kalman ﬁltering, state smoothing is not affected by the
diffuse initialization for t = T, . . . , 2. Thus, we focus on µ1 given FT . From Eq.
(11.20) and the deﬁnition of L1 = 1 −K1 = V −1
1 σ 2
e ,
µ1|T = µ1|0 + 1|0q0
= µ1|0 + 1|0

1
1|0 + σ 2e
v1 +

1 −
1|0
1|0 + σ 2e

q1

= µ1|0 +
1|0
1|0 + σ 2e
(v1 + σ 2
e q1).
Letting 1|0 →∞, we have µ1|T = µ1|0 + v1 + σ 2
e q1 = y1 + σ 2
e q1. Furthermore,
from Eq. (11.23) and using V1 = 1|0 + σ 2
e , we have
1|T = 1|0 −2
1|0

1
1|0 + σ 2e
+

1 −
1|0
1|0 + σ 2e
	2
M1

= 1|0

1 −
1|0
1|0 + σ 2e

−

1 −
1|0
1|0 + σ 2e
	2
2
1|0M1
=

1|0
1|0 + σ 2e

σ 2
e −

1|0
1|0 + σ 2e
	2
σ 4
e M1.
--- page 599 ---

572
state-space models and kalman ﬁlter
Thus, letting 1|0 →∞, we obtain 1|T = σ 2
e −σ 4
e M1.
Based on the prior discussion, we suggest using diffuse initialization when little
is known about the initial value µ1. However, it might be hard to justify the use
of a random variable with inﬁnite variance in real applications. If necessary, one
can treat µ1 as an additional parameter of the state-space model and estimate it
jointly with other parameters. This latter approach is closely related to the exact
maximum-likelihood estimation of Chapters 2 and 8.
11.1.7
Estimation
In this section, we consider the estimation of σe and ση of the local trend model
in Eqs. (11.1) and (11.2). Based on properties of forecast errors discussed in
Section 11.1.3, the Kalman ﬁlter provides an efﬁcient way to evaluate the likelihood function of the data for estimation. Speciﬁcally, the likelihood function
under normality is
p(y1, . . . , yT |σe, ση) = p(y1|σe, ση)
T
t=2
(yt|Ft−1, σe, ση)
= p(y1|σe, ση)
T
t=2
(vt|Ft−1, σe, ση),
where y1 ∼N(µ1|0, V1) and vt = (yt −µt|t−1) ∼N(0, Vt). Consequently, assuming µ1|0 and 1|0 are known, and taking the logarithms, we have
ln[L(σe, ση)] = −T
2 ln(2π) −1
2
T

t=1

ln(Vt) + v2
t
Vt

,
(11.25)
which involves vt and Vt. Therefore, the log-likelihood function, including cases
with missing values, can be evaluated recursively via the Kalman ﬁlter. Many software packages perform state-space model estimation via a Kalman ﬁlter algorithm
such as Matlab, RATS, and S-Plus. In this chapter, we use the SsfPack program
developed by Koopman, Shephard, and Doornik (1999) and available in S-Plus and
OX. Both Ssfpack and OX are free and can be downloaded from their websites.
11.1.8
S-Plus Commands Used
We provide here the SsfPack commands used to perform analysis of the daily
realized volatility of Aloca stock returns. Only brief explanations are given. For
further details of the commands used, see Durbin and Koopman (2001, Section
6.6). S-Plus uses speciﬁc notation to specify a state-space model; see Table 11.1.
The notation must be followed closely. In Table 11.2, we give some commands
and their functions.
--- page 600 ---

local trend model
573
TABLE 11.1
State-Space Form and Notation in S-Plus
State-Space Parameter
S-Plus Name
δ
mDelta

mPhi

mOmega

mSigma
TABLE 11.2
Some Commands of SsfPack Package
Command
Function
SsfFit
Maximum-likelihood estimation
CheckSsf
Create “Ssf” object in S-Plus
KalmanFil
Perform Kalman ﬁltering
KalmanSmo
Perform state smoothing
SsfMomentEst with task “STFIL”
Compute ﬁltered state and variance
SsfMomentEst with task “STSMO”
Compute smoothed state and variance
SsfCondDens with task “STSMO”
Compute smoothed state without variance
In our analysis, we ﬁrst perform maximum-likelihood estimation of the statespace model in Eqs. (11.1) and (11.2) to obtain estimates of σe and ση. The initial
values used are 1|0 = −1 and µ1|0 = 0, where −1 signiﬁes diffuse initialization,
that is, 1|0 is very large. We then treat the ﬁtted model as given to perform Kalman
ﬁltering and state smoothing.
SsfPack and S-Plus Commands for State-Space Model
> da = read.table(file=’aa-rv-0304.txt’,header=F) % load data
> y = log(da[,1]) % log(RV)
> ltm.start=c(3,1)
% Initial parameter values
> P1 = -1
% Initialization of Kalman filter
> a1 = 0
> ltm.m=function(parm){
% Specify a function for the
+ sigma.eta=parm[1]
% local trend model.
+ sigma.e=parm[2]
+ ssf.m=list(mPhi=as.matrix(c(1,1)),
+ mOmega=diag(c(sigma.eta^2,sigma.e^2)),
+ mSigma=as.matrix(c(P1,a1)))
+ CheckSsf(ssf.m)
+ }
% perform estimation
> ltm.mle=SsfFit(ltm.start,y,"ltm.m",lower=c(0,0),
+ upper=c(100,100))
> ltm.mle$parameters
--- page 601 ---

574
state-space models and kalman ﬁlter
[1] 0.07350827 0.48026284
> sigma.eta=ltm.mle$parameters[1]
> sigma.eta
[1] 0.07350827
> sigma.e=ltm.mle$parameters[2]
> sigma.e
[1] 0.4802628
% Specify a state-space model in S-Plus.
> ssf.ltm.list=list(mPhi=as.matrix(c(1,1)),
+ mOmega=diag(c(sigma.eta^2,sigma.e^2)),
+ mSigma=as.matrix(c(P1,a1)))
% check validity of the specified model.
> ssf.ltm=CheckSsf(ssf.ltm.list)
> ssf.ltm
$mPhi:
[,1]
[1,]
1
[2,]
1
$mOmega:
[,1]
[,2]
[1,] 0.0054035 0.0000000
[2,] 0.0000000 0.2306524
$mSigma:
[,1]
[1,]
-1
[2,]
0
$mDelta:
[,1]
[1,]
0
[2,]
0
$mJPhi:
[1] 0
$mJOmega:
[1] 0
$mJDelta:
[1] 0
$mX:
[1] 0
$cT:
[1] 0
$cX:
[1] 0
$cY:
[1] 1
$cSt:
[1] 1
attr(, "class"):
[1] "ssf"
% Apply Kalman filter
--- page 602 ---

local trend model
575
> KalmanFil.ltm=KalmanFil(y,ssf.ltm,task="STFIL")
> names(KalmanFil.ltm)
[1] "mOut"
"innov"
"std.innov"
"mGain"
"loglike"
[6] "loglike.conc" "dVar"
"mEst"
"mOffP"
"task"
[11] "err"
"call"
> par(mfcol=c(2,1))
% Obtain plot
> plot(KalmanFil.ltm$ mEst[,1],xlab=’day’,
+ ylab=’filtered state’,type=’l’)
> title(main=’(a) Filtered state variable’)
> plot(KalmanFil.ltm$ mOut[,1],xlab=’day’,
+ ylab=’v(t)’,type=’l’)
> title(main=’(b) Prediction error’)
% Obtain residuals and their variances
> KalmanSmo.ltm=KalmanSmo(KalmanFil.ltm,ssf.ltm)
> names(KalmanSmo.ltm)
[1] "state.residuals"
"response.residuals" "state.variance"
[4] "response.variance" "aux.residuals"
"scores"
[7] "call"
% Filtered states
> FiledEst.ltm=SsfMomentEst(y,ssf.ltm,task="STFIL")
> names(FiledEst.ltm)
[1] "state.moment"
"state.variance"
"response.moment"
[4] "response.variance" "task"
% Smoothed states
> SmoedEst.ltm=SsfMomentEst(y,ssf.ltm,task="STSMO")
> names(SmoedEst.ltm)
[1] "state.moment"
"state.variance"
"response.moment"
[4] "response.variance" "task"
% Obtain plots of filtered and smoothed states with 95% C.I.
> up=FiledEst.ltm$ state.moment+
+ 2*sqrt(FiledEst.ltm$ state.variance)
> lw=FiledEst.ltm$ state.moment-
+ 2*sqrt(FiledEst.ltm$ state.variance)
> par(mfcol=c(1,1))
> plot(FiledEst.ltm$ state.moment,type=’l’,xlab=’day’,
+ ylab=’value’,ylim=c(-0.1,2.5))
> lines(1:340,up,lty=2)
> lines(1:340,lw,lty=2)
> title(main=’Filed state variable’)
> up=SmoedEst.ltm$ state.moment+
+ 2*sqrt(SmoedEst.ltm$ state.variance)
> lw=SmoedEst.ltm$ state.moment-
+ 2*sqrt(SmoedEst.ltm$ state.variance)
> plot(SmoedEst.ltm$ state.moment,type=’l’,xlab=’day’,
+ ylab=’value’,ylim=c(-0.1,2.5))
> lines(1:340,up,lty=2)
> lines(1:340,lw,lty=2)
> title(main=’Smoothed state variable’)
% Model checking via standardized residuals
--- page 603 ---

576
state-space models and kalman ﬁlter
> resi=KalmanFil.ltm$ mOut[,1]*sqrt(KalmanFil.ltm$ mOut[,3])
> archTest(resi)
> autocorTest(resi)
For the daily realized volatility of Alcoa stock returns, the ﬁtted local trend
model is adequate based on residual analysis. Speciﬁcally, given the parameter
estimates, we use the Kalman ﬁlter to obtain the 1-step-ahead forecast error vt and
its variance Vt. We then compute the standardized forecast error ˜vt = vt/√Vt and
check the serial correlations and ARCH effects of {˜vt}. We found that Q(25) =
23.37(0.56) for the standardized forecast errors, and the LM test statistic for ARCH
effect is 18.48(0.82) for 25 lags, where the number in parentheses denotes p
value.
11.2
LINEAR STATE-SPACE MODELS
We now consider the general state-space model. Many dynamic time series models
in economics and ﬁnance can be represented in state-space form. Examples include
the ARIMA models, dynamic linear models with unobserved components, timevarying regression models, and stochastic volatility models. A general Gaussian
linear state-space model assumes the form
st+1 = dt + T tst + Rtηt,
(11.26)
yt = ct + Ztst + et,
(11.27)
where st = (s1t, . . . , smt)′ is an m-dimensional state vector, yt = (y1t, . . . , ykt)′ is a
k-dimensional observation vector, dt and ct are mand k-dimensional deterministic
vectors, T t and Zt are m × m and k × m coefﬁcient matrices, Rt is an m × n matrix
often consisting of a subset of columns of the m × m identity matrix, and {ηt} and
{et} are nand k-dimensional Gaussian white noise series such that
ηt ∼N(0, Qt),
et ∼N(0, H t),
where Qt and H t are positive-deﬁnite matrices. We assume that {et} and {ηt} are
independent, but this condition can be relaxed if necessary. The initial state s1 is
N(µ1|0, 1|0), where µ1|0 and 1|0 are given, and is independent of et and ηt for
t > 0.
Equation (11.27) is the measurement or observation equation that relates the
vector of observations yt to the state vector st, the explanatory variable ct, and
the measurement error et. Equation (11.26) is the state or transition equation that
describes a ﬁrst-order Markov Chain to govern the state transition with innovation
ηt. The matrices T t, Rt, Qt, Zt, and H t are known and referred to as system
matrices. These matrices are often sparse, and they can be functions of some
parameters θ, which can be estimated by the maximum-likelihood method.
The state-space model in Eqs. (11.26) and (11.27) can be rewritten in a compact
form as
--- page 604 ---

model transformation
577

st+1
yt

= δt + tst + ut,
(11.28)
where
δt =

 dt
ct

,
t =

 T t
Zt

,
ut =

 Rtηt
et

,
and {ut} is a sequence of Gaussian white nosies with mean zero and covariance
matrix
t = Cov(ut) =

RtQtR′
t
0
0
H t

The case of diffuse initialization is achieved by using
1|0 = ∗+ λ∞,
where ∗and ∞are m × m symmetric positive-deﬁnite matrices and λ is a large
real number, which can approach inﬁnity. In S-Plus and SsfPack, the notation
 =

1|0
µ′
1|0

(m+1)×m
is used; see the notation in Table 11.1.
In many applications, the system matrices are time invariant. However, these
matrices can be time varying, making the state-space model ﬂexible.
11.3
MODEL TRANSFORMATION
To appreciate the ﬂexibility of the state-space model, we rewrite some well-known
econometric and ﬁnancial models in state-space form.
11.3.1
CAPM with Time-Varying Coefﬁcients
First, consider the capital asset pricing model (CAPM) with time-varying intercept
and slope. The model is
rt = αt + βtrM,t + et,
et ∼N(0, σ 2
e ),
(11.29)
αt+1 = αt + ηt,
ηt ∼N(0, σ 2
η ),
βt+1 = βt + ϵt,
ϵt ∼N(0, σ 2
ϵ ),
where rt is the excess return of an asset, rM,t is the excess return of the market,
and the innovations {et, ηt, ϵt} are mutually independent. This CAPM allows for
--- page 605 ---

578
state-space models and kalman ﬁlter
time-varying α and β that evolve as a random walk over time. We can easily
rewrite the model as

αt+1
βt+1

=

1
0
0
1

αt
βt

+

ηt
ϵt

,
rt = [1, rM,t]

αt
βt

+ et.
Thus, the time-varying CAPM is a special case of the state-space model with st =
(αt, βt)′, T t = Rt = I 2, the 2 × 2 identity matrix, dt = 0, ct = 0, Zt = (1, rM,t),
H t = σ 2
e , and Qt = diag{σ 2
η , σ 2
ϵ }. Furthermore, in the form of Eq. (11.28), we
have δt = 0, ut = (ηt, ϵt, et)′,
t =


1
0
0
1
1
rM,t

,
t =


σ 2
η
0
0
0
σ 2
ϵ
0
0
0
σ 2
e

.
If diffuse initialization is used, then
 =


−1
0
0
−1
0
0

.
SsfPack/S-Plus Speciﬁcation of Time-Varying Models
For the CAPM in Eq. (11.29), t contains rM,t, which is time varying. Some
special input is required to specify such a model in SsfPack. Basically, it requires
two additional variables: (a) a data matrix X that stores Zt and (b) an index matrix
for t that identiﬁes Zt from the data matrix. The notation for index matrices of
the state-space model in Eq. (11.28) is given in Table 11.3. Note that the matrix
J  must have the same dimension as t. The elements of J  are all set to −1
except the elements for which the corresponding elements of t are time varying.
The nonnegative index value of J  indicates the column of the data matrix X,
which contains the time-varying values.
To illustrate, consider the monthly simple excess returns of General Motors
stock from January 1990 to December 2003 used in Chapter 9. The monthly simple
TABLE 11.3
Notation and Name Used in SsfPack/S-Plus for Time-Varying
State-Space Model
Index Matrix
Name Used in SsfPack/S-Plus
J δ
mJDelta
J 
mJPhi
J 
mJOmega
Time-Varying Data Matrix
Name Used in SsfPack/S-Plus
X
mX
--- page 606 ---

model transformation
579
excess return of the S&P 500 composite index is used as the market return. The
speciﬁcation of a time-varying CAPM requires values of the variances σ 2
η , σ 2
ϵ , and
σ 2
e . Suppose that (ση, σϵ, σe) = (0.02, 0.04, 0.1). The state-space speciﬁcation for
the CAPM under SsfPack/S-Plus is given below:
> X.mtx=cbind(1,sp) % Here ‘‘sp’’ is market excess returns.
> Phi.t = rbind(diag(2),rep(0,2))
> Sigma=-Phi.t
> sigma.eta=.02
> sigma.ep=.04
> sigma.e=.1
> Omega=diag(c(sigma.eta^2,sigma.ep^2,sigma.e^2))
> JPhi = matrix(-1,3,2)
% Create a 3-by-2 matrix of -1.
> JPhi[3,1]=1
> JPhi[3,2]=2
> ssf.tv.capm=list(mPhi=Phi.t,
+ mOmega=Omega,
+ mJPhi=JPhi,
+ mSigma=Sigma,
+ mX=X.mtx)
> ssf.tv.capm
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
[,1]
[,2] [,3]
[1,] 4e-04 0.0000 0.00
[2,] 0e+00 0.0016 0.00
[3,] 0e+00 0.0000 0.01
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
$mX:
numeric matrix: 168 rows, 2 columns.
sp
[1,] 1 -0.075187
...
[168,] 1
0.05002
--- page 607 ---

580
state-space models and kalman ﬁlter
11.3.2
ARMA Models
Consider a zero-mean ARMA(p, q) process yt of Chapter 2:
φ(B)yt = θ(B)at,
at ∼N(0, σ 2
a ),
(11.30)
where φ(B) = 1 −p
i=1 φiBi and θ(B) = 1 −q
j=1 θjBj, and p and q are nonnegative integers. There are many ways to transform such an ARMA model into
a state-space form. We discuss three methods available in the literature. Let m =
max(p, q + 1) and rewrite the ARMA model in Eq. (11.30) as
yt =
m

i=1
φiyt−i + at −
m−1

j=1
θjat−j,
(11.31)
where φi = 0 for i > p and θj = 0 for j > q. In particular, θm = 0 because m > q.
Akaike’s Approach
Akaike (1975) deﬁnes the state vector st as the minimum collection of variables
that contains all the information needed to produce forecasts at the forecast origin
t. It turns out that, for the ARMA process in Eq. (11.30) with m = max(p, q +
1), st = (yt|t, yt+1|t, . . . , yt+m−1|t)′, where yt+j|t = E(yt+j|Ft) is the conditional
expectation of yt+j given Ft = {y1, . . . , yt}. Since yt|t = yt, the ﬁrst element of st
is yt. Thus, the observation equation is
yt = Zst,
(11.32)
where Z = (1, 0, . . . , 0)1×m. We derive the transition equation in several steps.
First, from the deﬁnition,
s1,t+1 = yt+1 = yt+1|t + (yt+1 −yt+1|t) = s2t + at+1,
(11.33)
where sit is the ith element of st. Next, consider the MA representation of ARMA
models given in Chapter 2. That is,
yt = at + ψ1at−1 + ψ2at−2 + · · · =
∞

i=0
ψiat−i,
where ψ0 = 1 and other ψ weights can be obtained by equating coefﬁcients of Bi
in 1 + ∞
i=1 ψiBi = θ(B)/φ(B). In particular, we have
ψ1 = φ1 −θ1,
ψ2 = φ1ψ1 + φ2 −θ2,
...
--- page 608 ---

model transformation
581
ψm−1 = φ1ψm−2 + φ2ψm−3 + · · · + φm−2ψ1 + φm−1 −θm−1
=
m−1

i=1
φiψm−1−i −θm−1.
(11.34)
Using the MA representation, we have, for j > 0,
yt+j|t = E(yt+j|Ft) = E
 ∞

i=0
ψiat+j−i|Ft

= ψjat + ψj+1at−1 + ψj+2at−2 + · · ·
and
yt+j|t+1 = E(yt+j|Ft+1) = ψj−1at+1 + ψjat + ψj+1at−1 + · · ·
= ψj−1at+1 + yt+j|t.
Thus, for j > 0, we have
yt+j|t+1 = yt+j|t + ψj−1at+1.
(11.35)
This result is referred to as the forecast updating formula of ARMA models. It
provides a simple way to update the forecast from origin t to origin t + 1 when
yt+1 becomes available. The new information of yt+1 is contained in the innovation
at+1, and the time-t forecast is revised based on this new information with weight
ψj−1 to compute the time-(t + 1) forecast.
Finally, from Eq. (11.31) and using E(at+j|Ft+1) = 0 for j > 1, we have
yt+m|t+1 =
m

i=1
φiyt+m−i|t+1 −θm−1at+1.
Taking Eq. (11.35), the prior equation becomes
yt+m|t+1 =
m−1

i=1
φi(yt+m−i|t + ψm−i−1at+1) + φmyt|t −θm−1at+1
=
m

i=1
φiyt+m−i|t +
m−1

i=1
φiψm−1−i −θm−1

at+1
=
m

i=1
φiyt+m−i|t + ψm−1at+1,
(11.36)
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
