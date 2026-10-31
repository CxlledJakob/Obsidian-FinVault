# Analysis of Financial Time Series, Third Edition (Wiley -- Ruey S_ Tsay -- Wiley series in probability and statistics, 3rd ed_, -- John Wiley & Sons, -- isbn13 9780470414354 -- 9f99b80c7b2dedd477f463dc5323f3b6 -- An.pdf — pages 438–457

--- page 438 ---

vector autoregressive models
411
I .306E+02 I .659E+02 I
I
I . .
----+----------+----------+---------+----------+--------------
3 I .484E+02 I .132E+02 I
10.34 I
6.786 I . .
I .303E+02 I .655E+02 I
I
I . -
----+----------+----------+---------+----------+--------------
4 I .484E+02 I .131E+02 I
7.78 I
6.786 I . .
I .302E+02 I .655E+02 I
I
I . .
----+----------+----------+---------+----------+--------------
5 I .480E+02 I .131E+02 I
12.07 I
6.782 I . +
I .299E+02 I .648E+02 I
I
I - +
----+----------+----------+---------+----------+--------------
6 I .479E+02 I .131E+02 I
1.93 I
6.788 I . .
I .298E+02 I .647E+02 I
I
I . .
----+----------+----------+---------+----------+--------------
7 I .479E+02 I .130E+02 I
2.68 I
6.793 I . .
I .298E+02 I .647E+02 I
I
I . .
----+----------+----------+---------+----------+--------------
8 I .477E+02 I .130E+02 I
7.09 I
6.794 I . .
I .296E+02 I .643E+02 I
I
I . .
----+----------+----------+---------+----------+--------------
9 I .476E+02 I .130E+02 I
5.23 I
6.797 I . .
I .295E+02 I .642E+02 I
I
I . .
----+----------+----------+---------+----------+--------------
10 I .476E+02 I .130E+02 I
1.43 I
6.803 I . .
I .295E+02 I .641E+02 I
I
I . .
----+----------+----------+---------+----------+--------------
11 I .475E+02 I .130E+02 I
1.81 I
6.809 I . .
I .294E+02 I .640E+02 I
I
I . .
----+----------+----------+---------+----------+--------------
12 I .475E+02 I .129E+02 I
1.88 I
6.815 I . .
I .294E+02 I .640E+02 I
I
I . .
----+----------+----------+---------+----------+--------------
NOTE:CHI-SQUARED CRITICAL VALUES WITH 4 DEGREES OF FREEDOM ARE
5 PERCENT:
9.5
1 PERCENT:
13.3
-- % model specification of a VAR(5) model without lag 4.
mtsm m1. series ibm, sp5. model @
(i-p2*b-p2*b**2-p3*b**3-p5*b**5)series=c+noise.
-- % estimation
mestim m1. hold resi(r1,r2).
-- % demonstration of setting zero constraint
p2(2,2)=0
--
cp2(2,2)=1
--
p3(1,2)=0
--
cp3(1,2)=1
--
mestim m1. hold resi(r1,r2)
--- page 439 ---

412
multivariate time series analysis and its applications
FINAL MODEL SUMMARY WITH CONDITIONAL LIKELIHOOD PAR. EST.
----- CONSTANT VECTOR (STD ERROR) -----
1.039
(
0.223
)
0.390
(
0.176
)
----- PHI MATRICES -----
ESTIMATES OF
PHI(
1 ) MATRIX AND SIGNIFICANCE
.000
.129
. +
.000
.080
. +
STANDARD ERRORS
--
.040
--
.031
ESTIMATES OF
PHI(
2 ) MATRIX AND SIGNIFICANCE
.000
-.090
. -
.000
.000
. .
STANDARD ERRORS
--
.031
--
--
ESTIMATES OF
PHI(
3 ) MATRIX AND SIGNIFICANCE
.000
.000
. .
.000
-.061
. -
STANDARD ERRORS
--
--
--
.024
ESTIMATES OF
PHI(
5 ) MATRIX AND SIGNIFICANCE
.000
.093
. +
.000
.087
. +
STANDARD ERRORS
--
.040
--
.032
------------------------
ERROR COVARIANCE MATRIX
------------------------
1
2
1
48.328570
2
24.361464
30.027406
--------------------------------------------------------------
-- % compute residual cross-correlation matrices
miden r1,r2. maxl 12.
-- % prediction
mfore m1. nofs 6.
--------------------------------------------------------------
6 FORECASTS, BEGINNING AT ORIGIN = 996
--------------------------------------------------------------
SERIES:
IBM
SP5
TIME
FORECAST
STD ERR
FORECAST
STD ERR
997
1.954
6.952
1.698
5.480
--- page 440 ---

vector autoregressive models
413
998
0.304
6.988
0.173
5.497
999
-0.815
7.001
-1.263
5.497
1000
0.138
7.001
-0.494
5.507
1001
1.162
7.002
0.408
5.508
1002
1.294
7.022
0.649
5.528
8.2.5
Impulse Response Function
Similar to the univariate case, a VAR(p) model can be written as a linear function
of the past innovations, that is,
rt = µ + at + 1at−1 + 2at−2 + · · · ,
(8.21)
where µ = [(1)]−1φ0 provided that the inverse exists, and the coefﬁcient matrices
ψi can be obtained by equating the coefﬁcients of Bi in the equation
(I −1B −· · · −pBp)(I + 1B + 2B2 + · · ·) = I,
where I is the identity matrix. This is a moving-average representation of rt with
the coefﬁcient matrix i being the impact of the past innovation at−i on rt. Equivalently, i is the effect of at on the future observation rt+i. Therefore, i is often
referred to as the impulse response function of rt. However, since the components
of at are often correlated, the interpretation of elements in i of Eq. (8.21) is
not straightforward. To aid interpretation, one can use the Cholesky decomposition
mentioned earlier to transform the innovations so that the resulting components
are uncorrelated. Speciﬁcally, there exists a lower triangular matrix L such that
 = LGL′, where G is a diagonal matrix and the diagonal elements of L are
unity. See Eq. (8.9). Let bt = L−1at. Then, Cov(bt) = G so that the elements bjt
are uncorrelated. Rewrite Eq. (8.21) as
rt = µ + at + 1at−1 + 2at−2 + · · ·
= µ + LL−1at + 1LL−1at−1 + 2LL−1at−2 + · · ·
= µ + ∗
0bt + ∗
1bt−1 + ∗
2bt−2 + · · · ,
(8.22)
where ∗
0 = L and ∗
i = iL. The coefﬁcient matrices ∗
i are called the impulse
response function of rt with respect to the orthogonal innovations bt. Speciﬁcally,
the (i, j)th element of ∗
ℓ; that is, ∗
ij(ℓ), is the impact of bj,t on the future
observation ri,t+ℓ. In practice, one can further normalize the orthogonal innovation
bt such that the variance of bit is one. A weakness of the above orthogonalization
is that the result depends on the ordering of the components of rt. In particular,
b1t = a1t so that a1t is not transformed. Different orderings of the components of
rt may lead to different impulse response functions. Interpretation of the impulse
response function is, therefore, associated with the innovation series bt.
Both SCA and S-Plus enable one to obtain the impulse response function of a
ﬁtted VAR model. To demonstrate analysis of VAR models in S-Plus, we again use
--- page 441 ---

414
multivariate time series analysis and its applications
the monthly log return series of IBM stock and the S&P 500 index of Example
8.1. For details of S-Plus commands, see Zivot and Wang (2003).
S-Plus Demonstration
The following output has been edited and % denotes explanation:
> module(finmetrics)
> da=read.table("m-ibmsp2608.txt",header=T) % Load data
> ibm=log(da[,2]+1)*100 % Compute percentage log returns
> sp5=log(da[,3]+1)*100
> y=cbind(ibm,sp5) % Create a vector series
> y1=data.frame(y) % Crate a data frame
> ord.choice=VAR(y1,max.ar=10) % Order selection using BIC
> names(ord.choice)
[1] "R"
"coef" "fitted"
"residuals" "Sigma" "df.resid"
[7] "rank" "call" "ar.order" "n.na"
"terms" "Y0"
[13] "info"
> ord.choice$ar.order % selected order
[1] 1
> ord.choice$info
ar(1)
ar(2)
ar(3)
ar(4)
ar(5)
ar(6)
BIC 12325.41 12339.42 12356.58 12376.28 12391.57 12417.2
ar(7)
ar(8)
ar(9)
ar(10)
BIC
12442.03 12462.5212484.78 12510.91
> ord=VAR(y1,max.ar=10,criterion=’AIC’) % Using AIC
> ord$ar.order
[1] 5
> ord$info
ar(1)
ar(2)
ar(3)
ar(4)
ar(5)
ar(6)
AIC 12296.04 12290.48
12288.07 12288.2 12283.91 12289.96
ar(7)
ar(8)
ar(9)
ar(10)
AIC 12295.22 12296.13
12298.82 12305.37
The AIC selects a VAR(5) model as before, but BIC selects a VAR(1) model.
For simplicity, we shall use VAR(1) speciﬁcation in the demonstration. Note that
different normalizations are used between the two packages so that the values of
information criteria appear to be different; see the AIC in Table 8.3. This is not
important because normalization does not affect order selection. Turn to estimation.
> var1.fit=VAR(y∼ar(1)) % Estimate a VAR(1) model
> summary(var1.fit)
Call:
VAR(formula = y ∼ar(1))
Coefficients:
ibm
sp5
(Intercept)
1.0614
0.4087
(std.err)
0.2249
0.1773
--- page 442 ---

vector autoregressive models
415
(t.stat)
4.7198
2.3053
ibm.lag1
-0.0320 -0.0223
(std.err)
0.0413
0.0326
(t.stat)
-0.7728 -0.6855
sp5.lag1
0.1503
0.1020
(std.err)
0.0525
0.0414
(t.stat)
2.8612
2.4637
Regression Diagnostics:
ibm
sp5
R-squared 0.0101 0.0075
Adj. R-squared 0.0081 0.0055
Resid. Scale 7.0078 5.5247
Information Criteria:
logL
AIC
BIC
HQ
-6193.988
12399.977
12429.393
12411.159
total residual
Degree of freedom:
995
992
> plot(var1.fit)
Make a plot selection (or 0 to exit):
1: plot: All
2: plot: Response and Fitted Values
3: plot: Residuals
....
8: plot: PACF of Squared Residuals
Selection: 3
The ﬁtted model is
IBMt = 1.06 −0.03IBMt−1 + 0.15SP5t−1 + a1t,
SP5t = 0.41 −0.02IBMt−1 + 0.10SP5t−1 + a2t.
Based on t statistics of the coefﬁcient estimates, only the lagged variable SP5t−1 is
informative in both equations. Figure 8.5 shows the time plots of the two residual
series, where the two horizontal lines indicate the two standard error limits. As
expected, there exist clusters of outlying observations.
Next, we compute 1-stepto 6-step-ahead forecasts and the impulse response
function of the ﬁtted VAR(1) model when the IBM stock return is the ﬁrst component of rt. Compared with those of a VAR(5) model in Table 8.5, the forecasts
of the VAR(1) model converge faster to the sample mean of the series.
> var1.pred=predict(var1.fit,n.predict=6) % Compute forecasts
> summary(var1.pred)
--- page 443 ---

416
multivariate time series analysis and its applications
0
200
400
600
800
1000
−20
0
20
−20
0
20
ibm
200
0
400
600
800
1000
sp5
Residuals vs.Time
Figure 8.5
Residual plots of ﬁtting a VAR(1) model to the monthly log returns, in percentages, of
IBM stock and S&P 500 index. Sample period is from January 1926 to December 2008.
Predicted Values with Standard Errors:
ibm
sp5
1-step-ahead 1.0798 0.4192
(std.err) 7.0078 5.5247
2-step-ahead 1.0899 0.4274
(std.err) 7.0434 5.5453
3-step-ahead 1.0908 0.4280
(std.err) 7.0436 5.5454
...
6-step-ahead 1.0909 0.4280
(std.err) 7.0436 5.5454
> plot(var1.pred,y,n.old=12) % Obtain forecast plot
% Below is to compute the impulse response function
> var1.irf=impRes(var1.fit,period=6,std.err=′asymptotic′)
> summary(var1.irf)
Impulse Response Function:
(with responses in rows, and innovations in columns)
, , lag.0
ibm
sp5
ibm 6.9973 0.0000
(std.err) 0.1569 0.0000
sp5 3.5432 4.2280
(std.err) 0.1558 0.0948
, , lag.1
ibm
sp5
ibm 0.3088 0.6353
(std.err) 0.2217 0.2221
--- page 444 ---

vector moving-average models
417
−20
−15
−10
−5
0
5
985
990
995
1000
−15
−10
−5
0
5
985
990
995
1000
sp5
ibm
Index
Values
Figure 8.6
Forecasting plots of ﬁtted VAR(1) model to monthly log returns, in percentages, of IBM
stock and S&P 500 index. Sample period is from January 1926 to December 2008.
sp5 0.2050 0.4312
(std.err) 0.1746 0.1750
.....
> plot(var1.irf)
Figure 8.6 shows the forecasts and their pointwise 95% conﬁdence intervals
along with the last 12 data points of the series. Figure 8.7 shows the impulse
response functions of the ﬁtted VAR(1) model where the IBM stock return is the
ﬁrst component of rt. Since the dynamic dependence of the returns is weak, the
impulse response functions exhibit simple patterns and decay quickly.
8.3
VECTOR MOVING-AVERAGE MODELS
A vector moving-average model of order q, or VMA(q), is in the form
rt = θ0 + at −1at−1 −· · · −qat−q
or
rt = θ0 + (B)at,
(8.23)
where θ0 is a k-dimensional vector, i are k × k matrices, and (B) = I −
1B −· · · −qBq is the MA matrix polynomial in the back-shift operator B.
Similar to the univariate case, VMA(q) processes are weakly stationary provided
--- page 445 ---

418
multivariate time series analysis and its applications
0
1
2
3
0
2
4
6
0
1
2
3
4
5
Inno.: ibm
Resp.: sp5
0
1
2
3
4
Inno.: sp5
Resp.: sp5
Inno.: ibm
Resp.: ibm
0.0
0.2
0.4
0.6
0.8
0
1
2
3
4
5
Inno.: sp5
Resp.: ibm
Steps
Impulse response
Figure 8.7
Plots of impulse response functions of orthogonal innovations for ﬁtted VAR(1) model to
monthly log returns, in percentages, of IBM stock and S&P 500 index. Sample period is from January
1926 to December 2008.
that the covariance matrix  of at exists. Taking expectation of Eq. (8.23), we
obtain that µ = E(rt) = θ0. Thus, the constant vector θ0 is the mean vector of rt
for a VMA model.
Let ˜rt = rt −θ0 be the mean-corrected VAR(q) process. Then using Eq. (8.23)
and the fact that {at} has no serial correlations, we have
1. Cov(rt, at) = .
2.
0 =  + 1′
1 + · · · + q′
q.
3.
ℓ= 0 if ℓ> q.
4.
ℓ= q
j=ℓj′
j−ℓif 1 ≤ℓ≤q, where 0 = −I.
Since
ℓ= 0 for ℓ> q, the cross-correlation matrices (CCMs) of a VMA(q) process rt satisfy
ρℓ= 0,
ℓ>q.
(8.24)
Therefore, similar to the univariate case, the sample CCMs can be used to identify
the order of a VMA process.
--- page 446 ---

vector moving-average models
419
To better understand the VMA processes, let us consider the bivariate MA(1)
model
rt = θ0 + at −at−1 = µ + at −at−1,
(8.25)
where, for simplicity, the subscript of 1 is removed. This model can be written
explicitly as

 r1t
r2t

=

 µ1
µ2

+

 a1t
a2t

−

 11
12
21
22

 a1,t−1
a2,t−1

.
(8.26)
It says that the current return series rt only depends on the current and past shocks.
Therefore, the model is a ﬁnite-memory model.
Consider the equation for r1t in Eq. (8.26). The parameter 12 denotes the linear
dependence of r1t on a2,t−1 in the presence of a1,t−1. If 12 = 0, then r1t does not
depend on the lagged values of a2t and, hence, the lagged values of r2t. Similarly,
if 21 = 0, then r2t does not depend on the past values of r1t. The off-diagonal
elements of  thus show the dynamic dependence between the component series.
For this simple VMA(1) model, we can classify the relationships between r1t and
r2t as follows:
1. They are uncoupled series if 12 = 21 = 0.
2. There is a unidirectional dynamic relationship from r1t to r2t if ′
12 = 0,
but 21̸ = 0. The opposite unidirectional relationship holds if 21 = 0, but
12̸ = 0.
3. There is a feedback relationship between r1t and r2t if 12̸ = 0 and 21̸ = 0.
Finally, the concurrent correlation between rit is the same as that between ait. The
previous classiﬁcation can be generalized to a VMA(q) model.
Estimation
Unlike the VAR models, estimation of VMA models is much more involved;
see Hillmer and Tiao (1979), L¨utkepohl (2005), and the references therein.
For the likelihood approach, there are two methods available. The ﬁrst is the
conditional-likelihood method that assumes that at = 0 for t ≤0. The second is
the exact-likelihood method that treats at with t ≤0 as additional parameters of
the model. To gain some insight into the problem of estimation, we consider the
VMA(1) model in Eq. (8.25). Suppose that the data are {rt|t = 1, . . . , T } and at
is multivariate normal. For a VMA(1) model, the data depend on a0.
Conditional MLE
The conditional-likelihood method assumes that a0 = 0. Under such an assumption
and rewriting the model as at = rt −θ0 + at−1, we can compute the shock at
recursively as
a1 = r1 −θ0,
a2 = r2 −θ0 + 1a1,
. . . .
--- page 447 ---

420
multivariate time series analysis and its applications
Consequently, the likelihood function of the data becomes
f (r1, . . . , rT |θ0, 1, ) =
T
t=1
1
(2π)k/2||1/2 exp

−1
2a′
t−1at

,
which can be evaluated to obtain the parameter estimates.
Exact MLE
For the exact-likelihood method, a0 is an unknown vector that must be estimated
from the data to evaluate the likelihood function. For simplicity, let ˜rt = rt −θ0
be the mean-corrected series. Using ˜rt and Eq. (8.25), we have
at = ˜rt + at−1.
(8.27)
By repeated substitutions, a0 is related to all ˜rt as
a1 = ˜r1 + a0,
a2 = ˜r2 + a1 = ˜r2 + ˜r1 + 2a0,
...
(8.28)
aT = ˜rT + ˜rT −1 + · · · + T −1˜r1 + T a0.
Thus, a0 is a linear function of the data if θ0 and  are given. This result enables
us to estimate a0 using the data and initial estimates of θ0 and . More speciﬁcally,
given θ0, , and the data, we can deﬁne
r∗
t = ˜rt + ˜rt−1 + · · · + t−1˜r1,
for
t = 1, 2, . . . , T.
Equation (8.28) can then be rewritten as
r∗
1 = −a0 + a1,
r∗
2 = −2a0 + a2,
...
r∗
T = −T a0 + aT .
This is in the form of a multiple linear regression with parameter vector a0, even
though the covariance matrix  of at may not be a diagonal matrix. If initial
estimate of  is also available, one can premultiply each equation of the prior
system by −1/2, which is the square root matrix of . The resulting system is
indeed a multiple linear regression, and the ordinary least-squares method can be
used to obtain an estimate of a0. Denote the estimate by a0.
--- page 448 ---

vector moving-average models
421
Using the estimate a0, we can compute the shocks at recursively as
a1 = r1 −θ0 + a0,
a2 = r2 −θ0 + a1,
. . . .
This recursion is a linear transformation from (a0, r1, . . . , rT ) to (a0, a1, . . . , aT ),
from which we can (a) obtain the joint distribution of a0 and the data, and (2)
integrate out a0 to derive the exact-likelihood function of the data. The resulting
likelihood function can then be evaluated to obtain the exact ML estimates. For
details, see Hillmer and Tiao (1979).
In summary, the exact-likelihood method works as follows. Given initial estimates of θ0, , and , one uses Eq. (8.28) to derive an estimate of a0. This
estimate is in turn used to compute at recursively using Eq. (8.27) and starting
with a1 = ˜r1 + a0. The resulting {at}T
t=1 are then used to evaluate the exactlikelihood function of the data to update the estimates of θ0, , and . The whole
process is then repeated until the estimates converge. This iterative method to
evaluate the exact-likelihood function applies to the general VMA(q) models.
From the previous discussion, the exact-likelihood method requires more intensive computation than the conditional-likelihood approach does. But it provides
more accurate parameter estimates, especially when some eigenvalues of  are
close to 1 in modulus. Hillmer and Tiao (1979) provide some comparison between
the conditionaland exact-likelihood estimations of VMA models. In multivariate
time series analysis, the exact maximum-likelihood method becomes important if
one suspects that the data might have been overdifferenced. Overdifferencing may
occur in many situations (e.g., differencing individual components of a cointegrated
system; see discussion later on cointegration).
In summary, building a VMA model involves three steps: (a) Use the sample
cross-correlation matrices to specify the order q —for a VMA(q) model, ρℓ= 0 for
ℓ> q; (b) estimate the speciﬁed model by using either the conditionalor exactlikelihood method—the exact method is preferred when the sample size is not
large; and (c) the ﬁtted model should be checked for adequacy [e.g., applying the
Qk(m) statistics to the residual series]. Finally, forecasts of a VMA model can be
obtained by using the same procedure as a univariate MA model.
Example 8.5.
Consider again the bivariate series of monthly log returns in
percentages of IBM stock and the S&P 500 index from January 1926 to December 2008. Since signiﬁcant cross correlations occur mainly at lags 1, 2, 3 and 5,
we employ the VMA(5) model
rt = θ0 + at −1at−1 −2at−2 −3at−3 −5at−5
(8.29)
for the data. Table 8.6 shows the estimation results of the model. The Qk(m)
statistics for the residuals of the simpliﬁed model give Q2(4) = 16.00 and Q2(8) =
29.46. Compared with chi-squared distributions with 10 and 26 degrees of freedom,
the p values of these statistics are 0.10 and 0.291, respectively. Thus, the model
is adequate at the 5% signiﬁcance level.
--- page 449 ---

422
multivariate time series analysis and its applications
TABLE 8.6
Estimation Results for Monthly Log Returns of IBM Stock and S&P
500 Index Using the Vector Moving-Average Model in Eq. (8.29)a
Parameter
θ0
1
2
3
5
(a) Full Model with Conditional-Likelihood Method
Estimate
1.1
0.02
−0.15
−0.09
0.15
−0.05
0.11
0.05
−0.15
0.4
0.02
−0.10
−0.04
0.04
−0.01
0.11
0.07
−0.15
Standard error
0.24
0.04
0.05
0.04
0.05
0.04
0.05
0.04
0.05
0.19
0.03
0.04
0.03
0.04
0.03
0.04
0.03
0.04
(b) Full Model with Exact-Likelihood Method
Estimate
1.1
0.02
−0.05
−0.09
0.15
−0.05
0.11
0.05
−0.15
0.4
0.02
−0.10
−0.04
0.04
−0.01
0.11
0.07
−0.15
Standard error
0.24
0.04
0.05
0.04
0.05
0.04
0.05
0.04
0.05
0.19
0.03
0.04
0.03
0.04
0.03
0.04
0.03
0.04
(c) Simpliﬁed Model with Exact-Likelihood Method
Estimate
1.1
0.0
−0.13
0.0
0.08
0.0
0.0
0.0
−0.10
0.4
0.0
−0.09
0.0
0.0
0.0
0.07
0.0
−0.09
Standard error
0.24
—
0.04
—
0.03
—
—
—
0.04
0.19
—
0.03
—
—
—
0.02
—
0.03
aThe sample period is from January 1926 to December 2008. The residual covariance matrix is not
shown as it is similar to that in Table 8.4
From Table 8.6, we make the following observations:
1. The difference between conditionaland exact-likelihood estimates is small
for this particular example. This is not surprising because the sample size is
not small and, more important, the dynamic structure of the data is weak.
2. The VMA(5) model provides essentially the same dynamic relationship for
the series as that of the VAR(5) model in Example 8.4. The monthly log
return of IBM stock depends on the previous returns of the S&P 500 index.
The market return, in contrast, does not depend on lagged returns of IBM
stock. In other words, the dynamic structure of the data is driven by the
market return, not by the IBM return. The concurrent correlation between
the two returns remains strong, however.
8.4
VECTOR ARMA MODELS
Univariate ARMA models can also be generalized to handle vector time series. The
resulting models are called VARMA models. The generalization, however, encounters some new issues that do not occur in developing VAR and VMA models. One
of the issues is the identiﬁability problem. Unlike the univariate ARMA models,
VARMA models may not be uniquely deﬁned. For example, the VMA(1) model

 r1t
r2t

=

 a1t
a2t

−

 0
2
0
0

 a1,t−1
a2,t−1

--- page 450 ---

vector arma models
423
is identical to the VAR(1) model

 r1t
r2t

−

 0
−2
0
0

 r1,t−1
r2,t−1

=

 a1t
a2t

.
The equivalence of the two models can easily be seen by examining their component models. For the VMA(1) model, we have
r1t = a1t −2a2,t−1,
r2t = a2t.
For the VAR(1) model, the equations are
r1t + 2r2,t−1 = a1t,
r2t = a2t.
From the model for r2t, we have r2,t−1 = a2,t−1. Therefore, the models for r1t are
identical. This type of identiﬁability problem is harmless because either model can
be used in a real application.
Another type of identiﬁability problem is more troublesome. Consider the
VARMA(1,1) model

 r1t
r2t

−

 0.8
−2
0
0

 r1,t−1
r2,t−1

=

 a1t
a2t

−

 −0.5
0
0
0

 a1,t−1
a2,t−1

.
This model is identical to the VARMA(1,1) model

 r1t
r2t

−

 0.8
−2 + η
0
ω

 r1,t−1
r2,t−1

=

 a1t
a2t

−

 −0.5
η
0
ω

 a1,t−1
a2,t−1

,
for any nonzero ω and η. In this particular instance, the equivalence occurs
because we have r2t = a2t in both models. The effects of the parameters ω and
η on the system cancel out between AR and MA parts of the second model.
Such an identiﬁability problem is serious because, without proper constraints, the
likelihood function of a vector ARMA(1,1) model for the data is not uniquely
deﬁned, resulting in a situation similar to the exact multicollinearity in a regression
analysis. This type of identiﬁability problem can occur in a vector model even if
none of the components is a white noise series.
These two simple examples highlight the new issues involved in the generalization to VARMA models. Building a VARMA model for a given data set thus
requires some attention. In the time series literature, methods of structural speciﬁ-
cation have been proposed to overcome the identiﬁability problem; see Tiao and
Tsay (1989), Tsay (1991), and the references therein. We do not discuss the detail of
structural speciﬁcation here because VAR and VMA models are sufﬁcient in most
ﬁnancial applications. When VARMA models are used, only lower order models
are entertained [e.g., a VARMA(1,1) or VARMA(2,1) model] especially when the
time series involved are not seasonal.
--- page 451 ---

424
multivariate time series analysis and its applications
A VARMA(p, q) model can be written as
(B)rt = φ0 + (B)at,
where (B) = I −1B −· · · −pBp and (B) = I −1B −· · · −qBq are
two k × k matrix polynomials. We assume that the two matrix polynomials have
no left common factors; otherwise, the model can be simpliﬁed. The necessary
and sufﬁcient condition of weak stationarity for rt is the same as that for the
VAR(p) model with matrix polynomial (B). For v > 0, the (i, j)th elements
of the coefﬁcient matrices v and v measure the linear dependence of r1t on
rj,t−v and aj,t−v, respectively. If the (i, j)th element is zero for all AR and MA
coefﬁcient matrices, then rit does not depend on the lagged values of rjt. However,
the converse proposition does not hold in a VARMA model. In other words, nonzero
coefﬁcients at the (i, j)th position of AR and MA matrices may exist even when
rit does not depend on any lagged value of rjt.
To illustrate, consider the following bivariate model

 11(B)
12(B)
21(B)
22(B)

 r1t
r2t

=

 11(B)
12(B)
21(B)
22(B)

 a1t
a2t

.
Here the necessary and sufﬁcient conditions for the existence of a unidirectional
dynamic relationship from r1t to r2t are
22(B)12(B) −12(B)22(B) = 0,
but
11(B)21(B) −21(B)11(B)̸ = 0.
(8.30)
These conditions can be obtained as follows. Letting
(B) = |(B)| = 11(B)22(B) −12(B)21(B)
be the determinant of the AR matrix polynomial and premultiplying the model by
the matrix

22(B)
−12(B)
−21(B)
11(B)

,
we can rewrite the bivariate model as
(B)

r1t
r2t

=

22(B)11(B) −12(B)21(B)
22(B)12(B) −12(B)22(B)
11(B)21(B) −21(B)11(B)
11(B)22(B) −21(B)12(B)

×

a1t
a2t

.
--- page 452 ---

vector arma models
425
Year
Log rate
1960
1970
1980
1990
2000
0.0
0.5
1.0
1.5
2.0
2.5
3.0
Figure 8.8
Time plots of log U.S. monthly interest rates from April 1953 to January 2001. Solid line
denotes 1-year Treasury constant maturity rate and dashed line denotes 3-year rate.
Consider the equation for r1t. The ﬁrst condition in Eq. (8.30) shows that r1t does
not depend on any past value of a2t or r2t. From the equation for r2t, the second
condition in Eq. (8.30) implies that r2t indeed depends on some past values of
a1t. Based on Eq. (8.30), 12(B) = 12(B) = 0 is a sufﬁcient, but not necessary,
condition for the unidirectional relationship from r1t to r2t.
Estimation of a VARMA model can be carried out by either the conditional or
exact maximum-likelihood method. The Qk(m) statistic continues to apply to the
residual series of a ﬁtted model, but the degrees of freedom of its asymptotic chisquared distribution are k2m −g, where g is the number of estimated parameters
in both the AR and MA coefﬁcient matrices.
Example 8.6.
To demonstrate VARMA modeling, we consider two U.S.
monthly interest rate series. The ﬁrst series is the 1-year Treasury constant maturity
rate, and the second series is the 3-year Treasury constant maturity rate. The data
are obtained from the Federal Reserve Bank of St. Louis, and the sampling period
is from April 1953 to January 2001. There are 574 observations. To ensure the
positiveness of U.S. interest rates, we analyze the log series. Figure 8.8 shows the
time plots of the two log interest rate series. The solid line denotes the 1-year
maturity rate. The two series moved closely in the sampling period.
The M(i) statistics and AIC criterion specify a VAR(4) model for the data. However, we employ a VARMA(2,1) model because the two models provide similar
--- page 453 ---

426
multivariate time series analysis and its applications
TABLE 8.7
Parameter Estimates of VARMA(2,1) Model for Two Monthly U.S.
Interest Rate Series Based on Exact-Likelihood Method
Parameter
1
2
φ0
1
 × 103
Estimate
1.82
−0.97
−0.84
0.98
0.028
0.90
−1.66
3.58
2.50
—
0.99
—
—
0.025
—
−0.47
2.50
2.19
Standard error
0.03
0.08
0.03
0.08
0.014
0.03
0.10
—
0.01
—
—
0.011
—
0.04
ﬁts. Table 8.7 shows the parameter estimates of the VARMA(2,1) model obtained
by the exact-likelihood method. We removed the insigniﬁcant parameters and reestimated the simpliﬁed model. The residual series of the ﬁtted model has some minor
serial and cross correlations at lags 7 and 11. Figure 8.9 shows the residual plots
and indicates the existence of some outlying data points. The model can be further
improved, but it seems to capture the dynamic structure of the data reasonably well.
The ﬁnal VARMA(2,1) model shows some interesting characteristics of the
data. First, the interest rate series are highly contemporaneously correlated. The
concurrent correlation coefﬁcient is 2.5/
√
3.58 × 2.19 = 0.893. Second, there is a
Year
(a)
Residuals
1960
1970
1980
1990
2000
−0.2
0.0
0.2
Residuals
−0.1
0.0
0.1
Year
(b)
1960
1970
1980
1990
2000
Figure 8.9
Residual plots for log U.S. monthly interest rate series of Example 8.6. Fitted model is
VARMA(2,1): (a) 1-year rate and (b) 3-year rate.
--- page 454 ---

vector arma models
427
unidirectional linear relationship from the 3-year rate to the 1-year rate because the
(2, 1)th elements of all AR and MA matrices are zero, but some (1, 2)th element
is not zero. As a matter of fact, the model in Table 8.7 shows that
r3t = 0.025 + 0.99r3,t−1 + a3t + 0.47a3,t−1,
r1t = 0.028 + 1.82r1,t−1 −0.84r1,t−2 −0.97r3,t−1 + 0.98r3,t−2
+ a1t −0.90a1,t−1 + 1.66a3,t−1,
where rit is the log series of i-year interest rate and ait is the corresponding shock
series. Therefore, the 3-year interest rate does not depend on the past values of
the 1-year rate, but the 1-year rate depends on the past values of the 3-year rate.
Third, the two interest rate series appear to be unit-root nonstationary. Using the
back-shift operator B, the model can be rewritten approximately as
(1 −B)r3t = 0.03 + (1 + 0.47B)a3t,
(1 −B)(1 −0.82B)r1t = 0.03 −0.97B(1 −B)r3,t + (1 −0.9B)a1t + 1.66Ba3,t.
Finally, the SCA commands used in the analysis are given in Appendix C.
8.4.1
Marginal Models of Components
Given a vector model for rt, the implied univariate models for the components rit
are the marginal models. For a k-dimensional ARMA(p, q) model, the marginal
models are ARMA[kp, (k −1)p + q]. This result can be obtained in two steps.
First, the marginal model of a VMA(q) model is univariate MA(q). Assume that
rt is a VMA(q) process. Because the cross-correlation matrix of rt vanishes after
lag q (i.e., ρℓ= 0 for ℓ> q), the ACF of rit is zero beyond lag q. Therefore, rit is
an MA process and its univariate model is in the form rit = θi,0 + q
j=1 θi,jbi,t−j,
where {bit} is a sequence of uncorrelated random variables with mean zero and
variance σ 2
ib. The parameters θi,j and σib are functions of the parameters of the
VMA model for rt.
The second step to obtain the result is to diagonalize the AR matrix polynomial
of a VARMA(p, q) model. For illustration, consider the bivariate AR(1) model

 1 −11B
−12B
−21B
1 −22B

 r1t
r2t

=

 a1t
a2t

.
Premultiplying the model by the matrix polynomial

 1 −22B
12B
21B
1 −11B

,
we obtain
[(1 −11B)(1 −22B) −1222B2]

r1t
r2t

=

1 −22B
−12B
−21B
1 −11B

a1t
a2t

.
--- page 455 ---

428
multivariate time series analysis and its applications
The left-hand side of the prior equation shows that the univariate AR polynomials
for rit are of order 2. In contrast, the right-hand side of the equation is in a VMA(1)
form. Using the result of VMA models in step 1, we show that the univariate
model for rit is ARMA(2,1). The technique generalizes easily to the k-dimensional
VAR(1) model, and the marginal models are ARMA(k, k −1). More generally, for
a k-dimensional VAR(p) model, the marginal models are ARMA[kp, (k −1)p].
The result for VARMA models follows directly from those of VMA and VAR
models.
The order [kp, (k −1)p + q] is the maximum order (i.e., the upper bound) for
the marginal models. The actual marginal order of rit can be much lower.
8.5
UNIT-ROOT NONSTATIONARITY AND COINTEGRATION
When modeling several unit-root nonstationary time series jointly, one may
encounter the case of cointegration. Consider the bivariate ARMA(1,1) model

x1t
x2t

−

 0.5
−1.0
−0.25
0.5

x1,t−1
x2,t−1

=

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
,
(8.31)
where the covariance matrix  of the shock at is positive deﬁnite. This is not a
weakly stationary model because the two eigenvalues of the AR coefﬁcient matrix
are 0 and 1. Figure 8.10 shows the time plots of a simulated series of the model with
200 data points and  = I, whereas Figure 8.11 shows the sample autocorrelations
of the two component series xit. It is easy to see that the two series have high
autocorrelations and exhibit features of unit-root nonstationarity. The two marginal
models of xt are indeed unit-root nonstationary. Rewrite the model as

 1 −0.5B
B
0.25B
1 −0.5B

 x1t
x2t

=

 1 −0.2B
0.4B
0.1B
1 −0.2B

 a1t
a2t

.
Premultiplying the above equation by

 1 −0.5B
−B
−0.25B
1 −0.5B

,
we obtain the result

 1 −B
0
0
1 −B

 x1t
x2t

=

 1 −0.7B
−0.6B
−0.15B
1 −0.7B

 a1t
a2t

.
Therefore, each component xit of the model is unit-root nonstationary and follows
an ARIMA(0,1,1) model.
--- page 456 ---

unit-root nonstationarity and cointegration
429
Time
x1
0
50
100
150
200
−10
0
10
20
Time
x2
0
50
100
150
200
−10
0
10
20
Figure 8.10
Time plots of simulated series based on model (8.31) with identity covariance matrix for
shocks.
However, we can consider a linear transformation by deﬁning

y1t
y2t

=

1.0
−2.0
0.5
1.0

x1t
x2t

≡Lxt,

b1t
b2t

=

1.0
−2.0
0.5
1.0

a1t
a2t

≡Lat.
The VARMA model of the transformed series yt can be obtained as follows:
Lxt = Lxt−1 + Lat −Lat−1
= LL−1Lxt−1 + Lat −LL−1Lat−1
= LL−1(Lxt−1) + bt −LL−1bt−1.
Thus, the model for yt is

 y1t
y2t

−

 1.0
0
0
0

 y1,t−1
y2,t−1

=

 b1t
b2t

−

 0.4
0
0
0

 b1,t−1
b2,t−1

. (8.32)
From the prior model, we see that (a) y1t and y2t are uncoupled series with concurrent correlation equal to that between the shocks b1t and b2t, (b) y1t follows a
univariate ARIMA(0,1,1) model, and (c) y2t is a white noise series (i.e., y2t = b2t).
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
