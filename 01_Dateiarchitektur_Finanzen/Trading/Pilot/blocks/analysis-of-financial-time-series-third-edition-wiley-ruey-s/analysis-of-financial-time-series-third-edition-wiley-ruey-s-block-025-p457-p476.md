# Analysis of Financial Time Series, Third Edition (Wiley -- Ruey S_ Tsay -- Wiley series in probability and statistics, 3rd ed_, -- John Wiley & Sons, -- isbn13 9780470414354 -- 9f99b80c7b2dedd477f463dc5323f3b6 -- An.pdf — pages 457–476

--- page 457 ---

430
multivariate time series analysis and its applications
Lag
ACF
0
5
10
15
20
0.0
0.4
0.8
Lag
ACF
0
5
10
15
20
0.0
0.4
0.8
Figure 8.11
Sample autocorrelation functions of two simulated component series. There are 200
observations, and model is given by Eq. (8.31) with identity covariance matrix for shocks.
In particular, the model in Eq. (8.32) shows that there is only a single unit root in
the system. Consequently, the unit roots of x1t and x2t are introduced by the unit
root of y1t. In the literature, y1t is referred to as the common trend of x1t and x2t.
The phenomenon that both x1t and x2t are unit-root nonstationary, but there is
only a single unit root in the vector series, is referred to as cointegration in the
econometric and time series literature. Another way to deﬁne cointegration is to
focus on linear transformations of unit-root nonstationary series. For the simulated
example of model (8.31), the transformation shows that the linear combination
y2t = 0.5x1t + x2t does not have a unit root. Consequently, x1t and x2t are cointegrated if (a) both of them are unit-root nonstationary, and (b) they have a linear
combination that is unit-root stationary.
Generally speaking, for a k-dimensional unit-root nonstationary time series, cointegration exists if there are less than k unit roots in the system. Let h be the number
of unit roots in the k-dimensional series xt. Cointegration exists if 0 < h < k, and
the quantity k −h is called the number of cointegrating factors. Alternatively, the
number of cointegrating factors is the number of different linear combinations
that are unit-root stationary. The linear combinations are called the cointegrating
vectors. For the prior simulated example, y2t = (0.5, 1)xt so that (0.5, 1)′ is a
cointegrating vector for the system. For more discussions on cointegration and
cointegration tests, see Box and Tiao (1977), Engle and Granger (1987), Stock
and Watson (1988), and Johansen (1988). We discuss cointegrated VAR models in
Section 8.6.
The concept of cointegration is interesting and has attracted a lot of attention in
the literature. However, there are difﬁculties in testing for cointegration in a real
--- page 458 ---

unit-root nonstationarity and cointegration
431
application. The main source of difﬁculties is that cointegration tests overlook the
scaling effects of the component series. Interested readers are referred to Cochrane
(1988) and Tiao, Tsay, and Wang (1993) for further discussion.
While I have some misgivings on the practical value of cointegration tests, the
idea of cointegration is highly relevant in ﬁnancial study. For example, consider the
stock of Finnish Nokia Corporation. Its price on the Helsinki Stock Market must
move in unison with the price of its American Depositary Receipts on the New York
Stock Exchange; otherwise there exists some arbitrage opportunity for investors.
If the stock price has a unit root, then the two price series must be cointegrated.
In practice, such a cointegration can exist after adjusting for transaction costs and
exchange rate risk. We discuss issues like this later in Section 8.7.
8.5.1
An Error Correction Form
Because there are more unit-root nonstationary components than the number of
unit roots in a cointegrated system, differencing individual components to achieve
stationarity results in overdifferencing. Overdifferencing leads to the problem of
unit roots in the MA matrix polynomial, which in turn may encounter difﬁculties in
parameter estimation. If the MA matrix polynomial contains unit roots, the vector
time series is said to be noninvertible.
Engle and Granger (1987) discuss an error correction representation for a cointegrated system that overcomes the difﬁculty of estimating noninvertible VARMA
models. Consider the cointegrated system in Eq. (8.31). Let
xt = xt −xt−1 be
the differenced series. Subtracting xt−1 from both sides of the equation, we obtain
a model for
xt as

x1t

x2t

=

 −0.5
−1.0
−0.25
−0.5

 x1,t−1
x2,t−1

+

 a1t
a2t

−

0.2
−0.4
−0.1
0.2

 a1,t−1
a2,t−1

=

 −1
−0.5

[0.5, 1.0]

 x1,t−1
x2,t−1

+

 a1t
a2t

−

0.2
−0.4
−0.1
0.2

 a1,t−1
a2,t−1

.
This is a stationary model because both
xt and [0.5, 1.0]xt = y2t are unit-root
stationary. Because xt−1 is used on the right-hand side of the previous equation,
the MA matrix polynomial is the same as before and, hence, the model does not
encounter the problem of noninvertibility. Such a formulation is referred to as an
error correction model for
xt, and it can be extended to the general cointegrated
VARMA model. For a cointegrated VARMA(p, q) model with m cointegrating
factors (m < k), an error correction representation is

xt = αβ′xt−1 +
p−1

i=1
∗
i
xt−i + at −
q

j=1
jat−j,
(8.33)
--- page 459 ---

432
multivariate time series analysis and its applications
where α and β are k × m full-rank matrices. The AR coefﬁcient matrices ∗
i are
functions of the original coefﬁcient matrices j. Speciﬁcally, we have
∗
j = −
p

i=j+1
i,
j = 1, . . . , p −1,
αβ′ = p + p−1 + · · · + 1 −I = −(1).
(8.34)
These results can be obtained by equating coefﬁcient matrices of the AR matrix
polynomials. The time series β′xt is unit-root stationary, and the columns of β are
the cointegrating vectors of xt.
Existence of the stationary series β′xt−1 in the error correction representation
(8.33) is natural. It can be regarded as a “compensation” term for the overdifferenced system
xt. The stationarity of β′xt−1 can be justiﬁed as follows. The
theory of unit-root time series shows that the sample correlation coefﬁcient between
a unit-root nonstationary series and a stationary series converges to zero as the sample size goes to inﬁnity; see Tsay and Tiao (1990) and the references therein. In an
error correction representation, xt−1 is unit-root nonstationary, but
xt is stationary. Therefore, the only way that
xt can relate meaningfully to xt−1 is through
a stationary series β′xt−1.
Remark.
Our discussion of cointegration assumes that all unit roots are of
multiplicity 1, but the concept can be extended to cases in which the unit roots have
different multiplicities. Also, if the number of cointegrating factors m is given, then
the error correction model in Eq. (8.33) can be estimated by likelihood methods.
We discuss the simple case of cointegrated VAR models in the next section. Finally,
there are many ways to construct an error correction representation. In fact, one
can use any αβ′xt−v for 1 ≤v ≤p in Eq. (8.33) with some modiﬁcations to the
AR coefﬁcient matrices ∗
i .
□
8.6
COINTEGRATED VAR MODELS
To better understand cointegration, we focus on VAR models for their simplicity
in estimation. Consider a k-dimensional VAR(p) time series xt with possible time
trend so that the model is
xt = µt + 1xt−1 + · · · + pxt−p + at,
(8.35)
where the innovation at is assumed to be Gaussian and µt = µ0 + µ1t, where µ0
and µ1 are k-dimensional constant vectors. Write (B) = I −1B −· · · −pBp.
Recall that if all zeros of the determinant |(B)| are outside the unit circle, then
xt is unit-root stationary. In the literature, a unit-root stationary series is said to
be an I (0) process; that is, it is not integrated. If |(1)| = 0, then xt is unit-root
nonstationary. For simplicity, we assume that xt is at most an integrated process of
--- page 460 ---

cointegrated var models
433
order 1; that is, an I (1) process. This means that (1 −B)xit is unit-root stationary
if xit itself is not.
An error correction model (ECM) for the VAR(p) process xt is

xt = µt + xt−1 + ∗
1
xt−1 + · · · + ∗
p−1
xt−p+1 + at,
(8.36)
where ∗
j are deﬁned in Eq. (8.34) and  = αβ′ = −(1). We refer to the term
xt−1 of Eq. (8.36) as the error correction term, which plays a key role in cointegration study. Notice that i can be recovered from the ECM representation via
1 = I +  + ∗
1,
i = ∗
i −∗
i−1,
i = 2, . . . , p,
where ∗
p = 0, the zero matrix. Based on the assumption that xt is at most I (1),

xt of Eq. (8.36) is an I (0) process.
If xt contains unit roots, then |(1)| = 0 so that  = −(1) is singular. Therefore, three cases are of interest in considering the ECM in Eq. (8.36):
1. Rank() = 0. This implies  = 0 and xt is not cointegrated. The ECM of
Eq. (8.36) reduces to

xt = µt + ∗
1
xt−1 + · · · + ∗
p−1
xt−p+1 + at,
so that
xt follows a VAR(p −1) model with deterministic trend µt.
2. Rank() = k. This implies that |(1)|̸ = 0 and xt contains no unit roots;
that is, xt is I (0). The ECM model is not informative and one studies xt
directly.
3. 0 < Rank() = m < k. In this case, one can write  as
 = αβ′,
(8.37)
where α and β are k × m matrices with Rank(α) = Rank(β) = m. The ECM
of Eq. (8.36) becomes

xt = µt + αβ′xt−1 + ∗
1
xt−1 + · · · + ∗
p−1
xt−p+1 + at.
(8.38)
This means that xt is cointegrated with m linearly independent cointegrating vectors, wt = β′xt, and has k −m unit roots that give k −m common
stochastic trends of xt.
If xt is cointegrated with Rank() = m, then a simple way to obtain a presentation of the k −m common trends is to obtain an orthogonal complement matrix
α⊥of α; that is, α⊥is a k × (k −m) matrix such that α′
⊥α = 0, a (k −m) × m
zero matrix, and use yt = α′
⊥xt. To see this, one can premultiply the ECM by α′
⊥
--- page 461 ---

434
multivariate time series analysis and its applications
and use  = αβ′ to see that there would be no error correction term in the resulting equation. Consequently, the (k −m)-dimensional series yt should have k −m
unit roots. For illustration, consider the bivariate example of Section 8.5.1. For this
special series, α = (−1, −0.5)′ and α⊥= (1, −2)′. Therefore, yt = (1, −2)xt =
x1t −2x2t, which is precisely the unit-root nonstationary series y1t in Eq. (8.32).
Note that the factorization in Eq. (8.37) is not unique because for any m × m
orthogonal matrix  satisfying ′ = I, we have a
αβ′ = α′β′ = (α)(β)′ ≡α∗β′
∗,
where both α∗and β∗are also of rank m. Additional constraints are needed to
uniquely identify α and β. It is common to require that β′ = [I m, β′
1], where I m
is the m × m identity matrix and β1 is a (k −m) × m matrix. In practice, this may
require reordering of the elements of xt such that the ﬁrst m components all have
a unit root. The elements of α and β must also satisfy other constraints for the
process wt = β′xt to be unit-root stationary. For example, consider the case of a
bivariate VAR(1) model with one cointegrating vector. Here k = 2, m = 1, and the
ECM is

xt = µt +

 α1
α2

[1, β1]xt−1 + at.
Premultiplying the prior equation by β′, using wt−i = β′xt−i, and moving wt−1 to
the right-hand side of the equation, we obtain
wt = β′µt + (1 + α1 + α2β1)wt−1 + bt,
where bt = β′at. This implies that wt is a stationary AR(1) process. Consequently,
αi and β1 must satisfy the stationarity constraint |1 + α1 + α2β1| < 1.
The prior discussion shows that the rank of  in the ECM of Eq. (8.36) is the
number of cointegrating vectors. Thus, to test for cointegration, one can examine
the rank of . This is the approach taken by Johansen (1988, 1995) and Reinsel
and Ahn (1992).
8.6.1
Speciﬁcation of the Deterministic Function
Similar to the univariate case, the limiting distributions of cointegration tests depend
on the deterministic function µt. In this section, we discuss some speciﬁcations of
µt that have been proposed in the literature. To understand some of the statements
made below, keep in mind that α′
⊥xt provides a presentation for the common
stochastic trends of xt if it is cointegrated.
1. µt = 0: In this case, all the component series of xt are I (1) without drift
and the stationary series wt = β′xt has mean zero.
--- page 462 ---

cointegrated var models
435
2. µt = µ0 = αc0, where c0 is an m-dimensional nonzero constant vector. The
ECM becomes

xt = α(β′xt−1 + c0) + ∗
1
xt−1 + · · · + ∗
p−1
xt−p+1 + at,
so that the components of xt are I (1) without drift, but wt have a nonzero
mean −c0. This is referred to as the case of restricted constant.
3. µt = µ0, which is nonzero. Here the component series of xt are I (1) with
drift µ0 and wt may have a nonzero mean.
4. µt = µ0 + αc1t, where c1 is a nonzero vector. The ECM becomes

xt = µ0 + α(β′xt−1 + c1t) + ∗
1
xt−1 + · · · + ∗
p−1
xt−p+1 + at,
so that the components of xt are I (1) with drift µ0 and wt has a linear time
trend related to c1t. This is the case of restricted trend.
5. µt = µ0 + µ1t, where µi are nonzero. Here both the constant and trend are
unrestricted. The components of xt are I (1) and have a quadratic time trend
and wt have a linear trend.
Obviously, the last case is not common in empirical work. The ﬁrst case is not
common for economic time series but may represent the log price series of some
assets. The third case is also useful in modeling asset prices.
8.6.2
Maximum-Likelihood Estimation
In this section, we brieﬂy outline the maximum-likelihood estimation (MLE) of a
cointegrated VAR(p) model. Suppose that the data are {xt|t = 1, . . . , T }. Without
loss of generality, we write µt = µdt, where dt = [1, t]′, and it is understood that
µt depends on the speciﬁcation of the previous section. For a given m, which is
the rank of , the ECM model becomes

xt = µdt + αβ′xt−1 + ∗
1
xt−1 + · · · + ∗
p−1
xt−p+1 + at,
(8.39)
where t = p + 1, . . . , T . A key step in the estimation is to concentrate the likelihood function with respect to the deterministic term and the stationary effects. This
is done by considering the following two multivariate linear regressions:

xt = γ 0dt + 1
xt−1 + · · · + p−1
xt−p+1 + ut,
(8.40)
xt−1 = γ 1dt + 1
xt−1 + · · · + p−1
xt−p+1 + vt.
(8.41)
Let ˆut and ˆvt be the residuals of Eqs. (8.40) and (8.41), respectively. Deﬁne the
sample covariance matrices
S00 =
1
T −p
T

t=p+1
ˆut ˆu′
t,
S01 =
1
T −p
T

t=p+1
ˆut ˆv′
t,
S11 =
1
T −p
T

t=p+1
ˆvt ˆv′
t.
--- page 463 ---

436
multivariate time series analysis and its applications
Next, compute the eigenvalues and eigenvectors of S10S−1
00 S01 with respect to S11.
This amounts to solving the eigenvalue problem
|λS11 −S10S−1
00 S01| = 0.
Denote the eigenvalue and eigenvector pairs by (ˆλi, ei), where ˆλ1 > ˆλ2 > · · · > ˆλk.
Here the eigenvectors are normalized so that e′S11e = I, where e = [e1, . . . , ek]
is the matrix of eigenvectors.
The unnormalized MLE of the cointegrating vector β is ˆβ = [e1, . . . , em] and
from which we can obtain an MLE for β that satisﬁes the identifying constraint
and normalization condition. Denote the resulting estimate by ˆβc with the subscript
c signifying constraints. The MLE of other parameters can then be obtained by the
multivariate linear regression

xt = µdt + α ˆβ
′
cxt−1 + ∗
1
xt−1 + · · · + ∗
p−1
xt−p+1 + at.
The maximized value of the likelihood function based on m cointegrating vectors is
L−2/T
max ∝|S00|
m

i=1
(1 −ˆλi).
This value is used in the maximum-likelihood ratio test for testing Rank() = m.
Finally, estimates of the orthogonal complements of α and β can be obtained using
ˆα⊥= S−1
00 S11[em+1, . . . , ek],
ˆβ⊥= S11[em+1, . . . , ek].
8.6.3
Cointegration Test
For a speciﬁed deterministic term µt, we now discuss the maximum-likelihood test
for testing the rank of the  matrix in Eq. (8.36). Let H(m) be the null hypothesis
that the rank of  is m. For example, under H(0), Rank() = 0 so that  = 0
and there is no cointegration. The hypotheses of interest are
H(0) ⊂· · · ⊂H(m) ⊂· · · ⊂H(k).
For testing purpose, the ECM in Eq. (8.39) becomes

xt = µdt + xt−1 + ∗
1
xt−1 + · · · + ∗
p−1
xt−p+1 + at,
where t = p + 1, . . . , T . Our goal is to test the rank of . Mathematically, the
rank of  is the number of nonzero eigenvalues of , which can be obtained if a
consistent estimate of  is available. Based on the prior equation, which is in the
form of a multivariate linear regression, we see that  is related to the covariance
matrix between xt−1 and
xt after adjusting for the effects of dt and
xt−i for i
--- page 464 ---

cointegrated var models
437
= 1, . . . , p −1. The necessary adjustments can be achieved by the techniques of
multivariate linear regression shown in the previous section. Indeed, the adjusted
series of xt−1 and
xt are ˆvt and ˆut, respectively. The equation of interest for the
cointegration test then becomes
ˆut = ˆvt + at.
Under the normality assumption, the likelihood ratio test for testing the rank of
 in the prior equation can be done by using the canonical correlation analysis
between ˆut and ˆvt. See Johnson and Wichern (1998) for information on canonical
correlation analysis. The associated canonical correlations are the partial canonical
correlations between
xt−1 and xt−1 because the effects of dt and
xt−i have
been adjusted. The quantities {ˆλi} are the squared canonical correlations between
ˆut and ˆvt.
Consider the hypotheses
H0 : Rank() = m
versus
Ha : Rank()>m.
Johansen (1988) proposes the likelihood ratio (LR) statistic
LRtr(m) = −(T −p)
k

i=m+1
ln(1 −ˆλi)
(8.42)
to perform the test. If Rank() = m, then ˆλi should be small for i > m and hence
LRtr(m) should be small. This test is referred to as the trace cointegration test. Due
the presence of unit roots, the asymptotic distribution of LRtr(m) is not chi squared
but a function of standard Brownian motions. Thus, critical values of LRtr(m) must
be obtained via simulation.
Johansen (1988) also considers a sequential procedure to determine the number
of cointegrating vectors. Speciﬁcally, the hypotheses of interest are
H0 : Rank() = m
versus
Ha : Rank() = m + 1.
The LR ratio test statistic, called the maximum eigenvalue statistic, is
LRmax(m) = −(T −p) ln(1 −ˆλm+1).
Again, critical values of the test statistics are nonstandard and must be evaluated
via simulation.
8.6.4
Forecasting of Cointegrated VAR Models
The ﬁtted ECM can be used to produce forecasts. First, conditioned on the estimated
parameters, the ECM equation can be used to produce forecasts of the differenced
series
xt. Such forecasts can in turn be used to obtain forecasts of xt. A difference
between ECM forecasts and the traditional VAR forecasts is that the ECM approach
imposes the cointegration relationships in producing the forecasts.
--- page 465 ---

438
multivariate time series analysis and its applications
Year
(a)
Rate
1960
1970
1980
1990
2000
5
10
15
Year
(b)
Rate
1960
1970
1980
1990
2000
5
10
15
Figure 8.12
Time plots of weekly U.S. interest rate from December 12, 1958, to August 6, 2004.
(a) The 3-month Treasury bill rate and (b) 6-month Treasury bill rate. Rates are from secondary market.
8.6.5
An Example
To demonstrate the analysis of cointegrated VAR models, we consider two weekly
U.S. short-term interest rates. The series are the 3-month Treasury bill (TB) rate
and 6-month Treasury bill rate from December 12, 1958, to August 6, 2004, for
2383 observations. The TB rates are from the secondary market and obtained from
the Federal Reserve Bank of St. Loius. Figure 8.12 shows the time plots of the
interest rates. As expected, the two series move closely together.
Our analysis uses the S-Plus software with commands VAR for VAR analysis, coint for cointegration test, and VECM for vector error correction estimation. Denote the two series by tb3m and tb6m and deﬁne the vector series xt =
(tb3mt, tb6mt)′. The augmented Dickey–Fuller unit-root tests fail to reject the
hypothesis of a unit root in the individual series; see Chapter 2. Indeed, the test
statistics are −2.34 and −2.33 with p value about 0.16 for the 3-month and 6-month
interest rate when an AR(3) model is used. Thus, we proceed to VAR modeling.
For the bivariate series xt, the BIC criterion selects a VAR(3) model:
> x=cbind(tb3m,tb6m)
> y=data.frame(x)
> ord.choice$ar.order
[1] 3
--- page 466 ---

cointegrated var models
439
To perform a cointegration test, we choose a restricted constant for µt because
there is no reason a priori to believe the existence of a drift in the U.S. interest
rate. Both Johansen’s tests conﬁrm that the two series are cointegrated with one
cointegrating vector when a VAR(3) model is entertained.
> cointst.rc=coint(x,trend=’rc’, lags=2)
% lags = p-1.
> cointst.rc
Call:
coint(Y = x, lags = 2, trend = "rc")
Trend Specification:
H1*(r): Restricted constant
Trace tests sign. at the 5% level are flagged by ’ +’.
Trace tests sign. at the 1% level are flagged by ’++’.
Max Eig. tests sign. at the 5% level are flagged by ’ *’.
Max Eig. tests sign. at the 1% level are flagged by ’**’.
Tests for Cointegration Rank:
Eigenvalue Trace Stat
95% CV
99% CV
H(0)++**
0.0322
83.2712
19.96
24.60
H(1)
0.0023
5.4936
9.24
12.97
Max Stat
95% CV
99% CV
H(0)++**
77.7776
15.67
20.20
H(1)
5.4936
9.24
12.97
Next, we perform the maximum-likelihood estimation of the speciﬁed cointegrated VAR(3) model using an ECM presentation. The results are as follows:
> vecm.fit=VECM(cointst.rc)
> summary(vecm.fit)
Call:
VECM(test = cointst.rc)
Cointegrating Vectors:
coint.1
1.0000
tb6m
-1.0124
(std.err)
0.0086
(t.stat) -118.2799
Intercept*
0.2254
(std.err)
0.0545
(t.stat)
4.1382
VECM Coefficients:
--- page 467 ---

440
multivariate time series analysis and its applications
tb3m
tb6m
coint.1 -0.0949 -0.0211
(std.err)
0.0199
0.0179
(t.stat) -4.7590 -1.1775
tb3m.lag1
0.0466 -0.0419
(std.err)
0.0480
0.0432
(t.stat)
0.9696 -0.9699
tb6m.lag1
0.2650
0.3164
(std.err)
0.0538
0.0484
(t.stat)
4.9263
6.5385
tb3m.lag2 -0.2067 -0.0346
(std.err)
0.0481
0.0433
(t.stat) -4.2984 -0.8005
tb6m.lag2
0.2547
0.0994
(std.err)
0.0543
0.0488
(t.stat)
4.6936
2.0356
Regression Diagnostics:
tb3m
tb6m
R-squared 0.1081 0.0913
Adj. R-squared 0.1066 0.0898
Resid. Scale 0.2009 0.1807
> plot(vecm.fit)
Make a plot selection (or 0 to exit):
1: plot: All
2: plot: Response and Fitted Values
3: plot: Residuals
...
13: plot: PACF of Squared Cointegrating Residuals
Selection:
As expected, the output shows that the stationary series is wt ≈tb3mt −tb6mt
and the mean of wt is about −0.225. The ﬁtted ECM is

xt =

 −0.09
−0.02

(wt−1 + 0.23) +

0.05
0.27
−0.04
0.32


xt−1
+

 −0.21
0.25
−0.03
0.10


xt−2 + at,
and the estimated standard errors of ait are 0.20 and 0.18, respectively. Adequacy of the ﬁtted ECM can be examined via various plots. For illustration,
Figure 8.13 shows the cointegrating residuals. Some large residuals are shown
--- page 468 ---

cointegrated var models
441
−1.5
−1.0
−0.5
0.0
0.5
1.0
1.5
0
500
1000
1500
2000
coint.1
Figure 8.13
Time plot of cointegrating residuals for an ECM ﬁt to weekly U.S. interest rate series.
Data span is from December 12, 1958, to August 6, 2004.
in the plot, which occurred in the early 1980s when the interest rates were high
and volatile.
Finally, we use the ﬁtted ECM to produce 1-stepto 10-step-ahead forecasts for
both
xt and xt. The forecast origin is August 6, 2004.
> vecm.fst=predict(vecm.fit, n.predict=10)
> summary(vecm.fst)
Predicted Values with Standard Errors:
tb3m
tb6m
1-step-ahead -0.0378
-0.0642
(std.err)
0.2009
0.1807
2-step-ahead -0.0870
-0.0864
(std.err)
0.3222
0.2927
...
10-step-ahead -0.2276 -0.1314
(std.err)
0.8460
0.8157
> plot(vecm.fst,xold=diff(x),n.old=12)
> vecm.fit.level=VECM(cointst.rc,levels=T)
> vecm.fst.level=predict(vecm.fit.level, n.predict=10)
> summary(vecm.fst.level)
Predicted Values with Standard Errors:
tb3m
tb6m
1-step-ahead 1.4501
1.7057
--- page 469 ---

442
multivariate time series analysis and its applications
−1.0
 −0.5
0.0
0.5
2375
2380
2385
2390
tb3m
−1.0
−0.5
0.0
0.5
2375
2380
2385
2390
tb6m
Index
Values
Figure 8.14
Forecasting plots of ﬁtted ECM model for weekly U.S. interest rate series. Forecasts are
for differenced series and forecast origin is August 6, 2004.
(std.err) 0.2009
0.1807
2-step-ahead 1.4420
1.7017
(std.err) 0.3222
0.2927
...
10-step-ahead 1.4722 1.7078
(std.err) 0.8460 0.8157
> plot(vecm.fst.level, xold=x, n.old=50)
The forecasts are shown in Figures 8.14 and 8.15 for the differenced data and the
original series, respectively, along with some observed data points. The dashed
lines in the plots are pointwise 95% conﬁdence intervals. Because of unit-root
nonstationarity, the intervals are wide and not informative.
Remark.
The package urca of R can be used to perform Johansen’s cointegration test. The command is ca.jo. It requires speciﬁcation of some subcommands. See the section of pairs trading for demonstration.
□
8.7
THRESHOLD COINTEGRATION AND ARBITRAGE
In this section, we focus on detecting arbitrage opportunities in index trading by
using multivariate time series methods. We also demonstrate that simple univariate
--- page 470 ---

threshold cointegration and arbitrage
443
1.0
1.5
2.0
2340 2350 2360 2370 2380 2390
tb3m
1.0
1.5
2.0
2.5
tb6m
Index
Values
2340 2350 2360 2370 2380 2390
Figure 8.15
Forecasting plots of ﬁtted ECM model for weekly U.S. interest rate series. Forecasts are
for interest rates and forecast origin is August 6, 2004.
nonlinear models of Chapter 4. can be extended naturally to the multivariate case
in conjunction with the idea of cointegration.
Our study considers the relationship between the price of the S&P 500 index
futures and the price of the shares underlying the index on the cash market. Let
ft,ℓbe the log price of the index futures at time t with maturity ℓ, and let st be
the log price of the shares underlying the index on the cash market at time t. A
version of the cost-of-carry model in the ﬁnance literature states
ft,ℓ−st = (rt,ℓ−qt,ℓ)(ℓ−t) + z∗
t ,
(8.43)
where rt,ℓis the risk-free interest rate, qt,ℓis the dividend yield with respect to
the cash price at time t, and (ℓ−t) is the time to maturity of the futures contract;
see Brenner and Kroner (1995), Dwyer, Locke, and Yu (1996), and the references
therein.
The z∗
t process of model (8.43) must be unit-root stationary; otherwise there
exist persistent arbitrage opportunities. Here an arbitrage trading consists of simultaneously buying (short-selling) the security index and selling (buying) the index
futures whenever the log prices diverge by more than the cost of carrying the index
over time until maturity of the futures contract. Under the weak stationarity of z∗
t ,
--- page 471 ---

444
multivariate time series analysis and its applications
for arbitrage to be proﬁtable, z∗
t must exceed a certain value in modulus determined
by transaction costs and other economic and risk factors.
It is commonly believed that the ft,ℓand st series of the S&P 500 index contain
a unit root, but Eq. (8.43) indicates that they are cointegrated after adjusting for
the effect of interest rate and dividend yield. The cointegrating vector is (1, −1)
after the adjustment, and the cointegrated series is z∗
t . Therefore, one should use
an error correction form to model the return series rt = (
ft,
st)′, where
ft =
ft,ℓ−ft−1,ℓand
st = st −st−1, where for ease in notation we drop the maturity
time ℓfrom the subscript of
ft.
8.7.1
Multivariate Threshold Model
In practice, arbitrage tradings affect the dynamic of the market, and hence the
model for rt may vary over time depending on the presence or absence of arbitrage
tradings. Consequently, the prior discussions lead naturally to the following model:
rt =



c1 + p
i=1 (1)
i rt−i + β1zt−1 + a(1)
t
if zt−1 ≤γ1,
c2 + p
i=1 (2)
i rt−i + β2zt−1 + a(2)
t
if γ1 < zt−1 ≤γ2,
c3 + p
i=1 (3)
i rt−i + β3zt−1 + a(3)
t
if γ2 < zt−1,
(8.44)
where zt = 100z∗
t , γ1 < 0 < γ2 are two real numbers, and {a(i)
t } are sequences
of two-dimensional white noises and are independent of each other. Here we use
zt = 100z∗
t because the actual value of z∗
t is relatively small.
The model in Eq. (8.44) is referred to as a multivariate threshold model with
three regimes. The two real numbers γ1 and γ2 are the thresholds and zt−1 is
the threshold variable. The threshold variable zt−1 is supported by the data; see
Tsay (1998). In general, one can select zt−d as a threshold variable by considering
d ∈{1, . . . , d0}, where d0 is a prespeciﬁed positive integer.
Model (8.44) is a generalization of the threshold autoregressive model of
Chapter 4. It is also a generalization of the error correlation model of Eq.
(8.33). As mentioned earlier, an arbitrage trading is proﬁtable only when z∗
t or,
equivalently, zt is large in modulus. Therefore, arbitrage tradings only occurred in
regimes 1 and 3 of model (8.44). As such, the dynamic relationship between ft,ℓ
and st in regime 2 is determined mainly by the normal market force, and hence
the two series behave more or less like a random walk. In other words, the two
log prices in the middle regime should be free from arbitrage effects and, hence,
free from the cointegration constraint. From an econometric viewpoint, this means
that the estimate of β2 in the middle regime should be insigniﬁcant.
In summary, we expect that the cointegration effects between the log price of
the futures and the log price of security index on the cash market are signiﬁcant
in regimes 1 and 3, but insigniﬁcant in regime 2. This phenomenon is referred to
as a threshold cointegration; see Balke and Fomby (1997).
--- page 472 ---

threshold cointegration and arbitrage
445
Time index
(a)
0
2000
4000
6000
−0.001 0.0
0.001
−0.001 0.0
0.001 0.002
−0.2
0.0
0.2
Time index
(b)
0
2000
4000
6000
Time index
(c)
0
2000
4000
6000
Figure 8.16
Time plots of 1-minute log returns of S&P 500 index futures and cash prices and associated threshold variable in May 1993: (a) log returns of index futures, (b) log returns of index cash
prices, and (c) zt series.
8.7.2
The Data
The data used in this case study are the intraday transaction data of the S&P 500
index in May 1993 and its June futures contract traded at the Chicago Mercantile
Exchange; see Forbes, Kalb, and Kofman (1999), who used the data to construct a
minute-by-minute bivariate price series with 7060 observations. To avoid the undue
inﬂuence of unusual returns, I replaced 10 extreme values (5 on each side) by the
simple average of their two nearest neighbors. This step does not affect the qualitative conclusion of the analysis but may affect the conditional heteroscedasticity
in the data. For simplicity, we do not consider conditional heteroscedasticity in the
study. Figure 8.16 shows the time plots of the log returns of the index futures and
cash prices and the associated threshold variable zt = 100z∗
t of model (8.43).
8.7.3
Estimation
A formal speciﬁcation of the multivariate threshold model in Eq. (8.44) includes
selecting the threshold variable, determining the number of regimes, and choosing
--- page 473 ---

446
multivariate time series analysis and its applications
the order p for each regime. Interested readers are referred to Tsay (1998) and
Forbes, Kalb, and Kofman (1999). The thresholds γ1 and γ2 can be estimated
by using some information criteria [e.g., the Akaike information criterion (AIC)
or the sum of squares of residuals]. Assuming p = 8, d ∈{1, 2, 3, 4}, γ1 ∈
[−0.15, −0.02], and γ2 ∈[0.025, 0.145], and using a grid search method with
300 points on each of the two intervals, the AIC selects zt−1 as the threshold
variable with thresholds ˆγ1 = −0.0226 and ˆγ2 = 0.0377. Details of the parameter
estimates are given in Table 8.8.
From Table 8.8, we make the following observations. First, the t ratios of β2 in
the middle regime show that, as expected, the estimates are insigniﬁcant at the 5%
level, conﬁrming that there is no cointegration between the two log prices in the
absence of arbitrage opportunities. Second,
ft depends negatively on
ft−1 in all
three regimes. This is in agreement with the bid–ask bounce discussed in Chapter 5.
Third, past log returns of the index futures seem to be more informative than the
past log returns of the cash prices because there are more signiﬁcant t ratios in

ft−i than in
st−i. This is reasonable because futures series are in general more
liquid. For more information on index arbitrage, see Dwyer, Locke, and Yu (1996).
8.8
PAIRS TRADING
Pairs trading is a market-neutral trading strategy. There are several versions of pairs
trading in the equity markets. In this section, we focus on the statistical arbitrage
pairs trading, which makes use of the ideas of cointegration and error correction
model discussed in the chapter. Our discussion will be brief. For more information
concerning pairs trading and statistical arbitrage, see Vidyamurthy (2004) and Pole
(2007).
The general theme for trading in the equity markets is to buy undervalued stocks
and sell overvalued ones. However, the true price of a stock is hard to assess.
Pairs trading attempts to resolve this difﬁculty using the idea of relative pricing.
Based on the arbitrage pricing theory (APT) in ﬁnance, if two stocks have similar
characteristics, then the prices of both stocks must be more or less the same. If
the prices differ, then it is likely that one of the stocks is overpriced and the other
underpriced. Pairs trading involves selling the higher priced stock and buying the
lower priced stock with the hope that the mispricing will correct itself in the future.
Note that the true prices of the two stocks are not important. The observed prices
may be wrong. What is important is that the observed prices be the same. The
gap (properly scaled) between the two observed prices is called the spread. For
pairs trading, the greater the spread, the larger the magnitude of mispricing and the
greater the proﬁt potential. Before discussing a trading strategy, we ﬁrst introduce
the theoretical framework.
8.8.1
Theoretical Framework
Consider two stocks. Let Pit be the observed price of stock i at time t and pit =
ln(Pit) be the corresponding log price. As mentioned in earlier chapters, it is
--- page 474 ---

pairs trading
447
TABLE 8.8
Least-Squares Estimates and Their t Ratios of Multivariate Threshold
Model in Eq. (8.43) for S&P 500 Index Data in May 1993a
Regime 1
Regime 2
Regime 3

ft

st

ft

st

ft

st
φ0
0.00002
0.00005
0.00000
0.00000
−0.00001
−0.00005
t
(1.47)
(7.64)
(−0.07)
(0.53)
(−0.74)
(−6.37)

ft−1
−0.08468
0.07098
−0.03861
0.04037
−0.04102
0.02305
t
(−3.83)
(6.15)
(−1.53)
(3.98)
(−1.72)
(1.96)

ft−2
−0.00450
0.15899
0.04478
0.08621
−0.02069
0.09898
t
(−0.20)
(13.36)
(1.85)
(8.88)
(−0.87)
(8.45)

ft−3
0.02274
0.11911
0.07251
0.09752
0.00365
0.08455
t
(0.95)
(9.53)
(3.08)
(10.32)
(0.15)
(7.02)

ft−4
0.02429
0.08141
0.01418
0.06827
−0.02759
0.07699
t
(0.99)
(6.35)
(0.60)
(7.24)
(−1.13)
(6.37)

ft−5
0.00340
0.08936
0.01185
0.04831
−0.00638
0.05004
t
(0.14)
(7.10)
(0.51)
(5.13)
(−0.26)
(4.07)

ft−6
0.00098
0.07291
0.01251
0.03580
−0.03941
0.02615
t
(0.04)
(5.64)
(0.54)
(3.84)
(−1.62)
(2.18)

ft−7
−0.00372
0.05201
0.02989
0.04837
−0.02031
0.02293
t
(−0.15)
(4.01)
(1.34)
(5.42)
(−0.85)
(1.95)

ft−8
0.00043
0.00954
0.01812
0.02196
−0.04422
0.00462
t
(0.02)
(0.76)
(0.85)
(2.57)
(−1.90)
(0.40)

st−1
−0.08419
0.00264
−0.07618
−0.05633
0.06664
0.11143
t
(−2.01)
(0.12)
(−1.70)
(−3.14)
(1.49)
(5.05)

st−2
−0.05103
0.00256
−0.10920
−0.01521
0.04099
−0.01179
t
(−1.18)
(0.11)
(−2.59)
(−0.90)
(0.92)
(−0.53)

st−3
0.07275
−0.03631
−0.00504
0.01174
−0.01948
−0.01829
t
(1.65)
(−1.58)
(−0.12)
(0.71)
(−0.44)
(−0.84)

st−4
0.04706
0.01438
0.02751
0.01490
0.01646
0.00367
t
(1.03)
(0.60)
(0.71)
(0.96)
(0.37)
(0.17)

st−5
0.08118
0.02111
0.03943
0.02330
−0.03430
−0.00462
t
(1.77)
(0.88)
(0.97)
(1.43)
(−0.83)
(−0.23)

st−6
0.04390
0.04569
0.01690
0.01919
0.06084
−0.00392
t
(0.96)
(1.92)
(0.44)
(1.25)
(1.45)
(−0.19)

st−7
−0.03033
0.02051
−0.08647
0.00270
−0.00491
0.03597
t
(−0.70)
(0.91)
(−2.09)
(0.16)
(−0.13)
(1.90)

st−8
−0.02920
0.03018
0.01887
−0.00213
0.00030
0.02171
t
(−0.68)
(1.34)
(0.49)
(−0.14)
(0.01)
(1.14)
zt−1
0.00024
0.00097
−0.00010
0.00012
0.00025
0.00086
t
(1.34)
(10.47)
(−0.30)
(0.86)
(1.41)
(9.75)
aThe numbers of data points for the three regimes are 2234, 2410, and 2408, respectively.
--- page 475 ---

448
multivariate time series analysis and its applications
reasonable to assume that pit is unit-root nonstationary and follows a random-walk
model; that is, pit = pi,t−1 + rit, where {rit} is the return and forms a sequence
of uncorrelated innovations. If the two stocks have similar risk factors, then they
should have similar returns based on APT. Therefore, p1t and p2t are likely to be
driven by a common component and are cointegrated. In other words, there exists a
linear combination wt = p1t −γp2t, which is unit-root stationary and, hence, mean
reverting. The two price series {p1t} and {p2t} thus assume an error correction form

 p1t −p1,t−1
p2t −p2,t−1

=

 α1
α2

(wt−1 −µw) +

 ϵ1t
ϵ2t

,
(8.45)
where µw = E(wt) denotes the mean of wt. The four parameters γ , µw, α1, and
α2 can be estimated, for instance, by the maximum-likelihood or least-squares
methods; see Section 8.6.2. We refer to the stationary series wt as the spread
between the two log stock prices.
The left-hand side of Eq. (8.45) consists the log returns of the two stocks. The
equation says that the returns depend on wt−1, which is the stationary. Speciﬁcally,
wt−1 −µw denotes the deviation from the log-run equilibrium between the two
stocks. Equation (8.45) shows that, for cointegrated stocks, the returns depend on
the past deviation from equilibrium. The coefﬁcients α1 and α2 show the effect of
past deviation on the returns r1t and r2t, respectively. In practice, α1 and α2 should
have opposite signs, indicating reversion to the equilibrium.
Next, consider a portfolio with long one share of stock 1 and short γ shares of
stock 2. The return of the portfolio for a given time period i is
rp,t+i = (p1,t+i −p1t) −γ (p2,t+i −p2t)
= (p1,t+i −γp2,t+i) −(p1t −γp2t)
= wt+i −wt.
Therefore, the return rp,t+i of the portfolio is the increment of the spread in the
time period. As expected, the return of the portfolio does not depend on the mean
of wt.
8.8.2
Trading Strategy
The idea behind a pairs-trading strategy is to trade on the oscillations about the
equilibrium value of the spread. The oscillations in spread occur because the spread
is mean reverting. Since the equilibrium value is the mean of wt, that is, µw, we
can put on a trade when wt deviates substantially from its mean and unwind the
trade when the equilibrium is restored. In practice, how big the deviation needs
to be in order for the trading to be proﬁtable depends on several factors. Trading
costs, marginal interest rates, and bid–ask spreads of the two stocks are three
obvious factors. Mathematically, let η be the cost involved in carrying out a pairs
trading. Let
 be a target deviation of wt from its mean µw for pairs trading. Then,
conditioned on 2
 > η, a simple trading strategy is as follows:
--- page 476 ---

pairs trading
449
• Buy a share of stock 1 and short γ shares of stock 2 at time t if wt =
p1t −γp2t = µw −
.
• Unwind the position at time t + i (i > 0) if wt+i = p1,i+i −γp2,t+i = µw +

.
One can identify the time point t so long as
 is not too large compared with
the standard deviation of wt. The time point t + i will occur because of the mean
reverting of the spread series. In this particular instance, the return of the portfolio
wt+i −wt = 2
 and the net proﬁt of the trade is 2
 −η > 0.
Discussion.
The aforementioned trading strategy is just one of many possibilities. For instance, if
 > η, one can unwind the position when wt+i = µw. The
net proﬁt of the pairs trading then is
 −η > 0. This may result in more transactions and trading costs, but it shortens the holding period of the portfolio. If
is negative, then one can short one share of stock 1 and buy γ shares of stock 2
to make a net proﬁt −2
 −η. The quantity η is the threshold for trading and is
likely to depend on several factors such as transaction fees and bid–ask spreads of
the two stocks.
□
8.8.3
Simple Illustration
To demonstrate pairs trading, we consider two stocks traded on the New York
Stock Exchange. The two companies are the Billiton Ltd. of Australia and the
Vale S.A. of Brazil with stock symbols BHP and VALE, respectively. BHP of
Australia is a natural resources company with business in Australia, the Americans,
and Southern Africa. Vale of Brazil is a worldwide metals and mining company.
Thus, both multinational companies belong to the natural resources industry and
encounter similar risk factors. The daily prices of the two stocks were downloaded
from Yahoo Finance, and we employ adjusted closing prices from July 1, 2002, to
March 31, 2006, in our study.
Figure 8.17 shows the time plots of the daily log prices of the two stocks
(adjusted closing prices). The upper plot is for the BHP stock. From the plots, the
prices of the two stocks exhibit certain characteristics of comovement. Let p1t and
p2t be the daily log closing prices of BHP and VALE, respectively. We analyze
the series using both the least-squares and maximum-likelihood methods.
Least-Squares Estimation
A simple way to verify that the two stocks are suitable for pairs trading is to check
the cointegration of their log stock prices. To this end, we consider the simple
linear regression p1t = β0 + β1p2t + wt, where wt denotes the residual series. For
the BHP and VALE stocks, we have
p1t = 1.823 + 0.717p2t + ˆwt,
σw = 0.044.
