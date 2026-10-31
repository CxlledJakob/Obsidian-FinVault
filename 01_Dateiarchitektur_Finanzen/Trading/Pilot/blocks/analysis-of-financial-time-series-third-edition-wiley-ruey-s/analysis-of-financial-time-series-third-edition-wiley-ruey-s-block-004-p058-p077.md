# Analysis of Financial Time Series, Third Edition (Wiley -- Ruey S_ Tsay -- Wiley series in probability and statistics, 3rd ed_, -- John Wiley & Sons, -- isbn13 9780470414354 -- 9f99b80c7b2dedd477f463dc5323f3b6 -- An.pdf — pages 58–77

--- page 58 ---

correlation and autocorrelation function
31
sample {(xt, yt)}T
t=1 is available, the correlation can be consistently estimated by
its sample counterpart
ˆρx,y =
T
t=1(xt −¯x)(yt −¯y)
T
t=1(xt −¯x)2 T
t=1(yt −¯y)2
,
where ¯x = T
t=1 xt/T and ¯y = T
t=1 yt/T are the sample mean of X and Y,
respectively.
Autocorrelation Function (ACF)
Consider a weakly stationary return series rt. When the linear dependence between
rt and its past values rt−i is of interest, the concept of correlation is generalized
to autocorrelation. The correlation coefﬁcient between rt and rt−ℓis called the
lag-ℓautocorrelation of rt and is commonly denoted by ρℓ, which under the weak
stationarity assumption is a function of ℓonly. Speciﬁcally, we deﬁne
ρℓ=
Cov(rt, rt−ℓ)

Var(rt)Var(rt−ℓ)
= Cov(rt, rt−ℓ)
Var(rt)
= γℓ
γ0
,
(2.1)
where the property Var(rt) = Var(rt−ℓ) for a weakly stationary series is used. From
the deﬁnition, we have ρ0 = 1, ρℓ= ρ−ℓ, and −1 ≤ρℓ≤1. In addition, a weakly
stationary series rt is not serially correlated if and only if ρℓ= 0 for all ℓ> 0.
For a given sample of returns {rt}T
t=1, let ¯r be the sample mean (i.e., ¯r =
T
t=1 rt/T ). Then the lag-1 sample autocorrelation of rt is
ˆρ1 =
T
t=2(rt −¯r)(rt−1 −¯r)
T
t=1(rt −¯r)2
.
Under some general conditions, ˆρ1 is a consistent estimate of ρ1. For example, if
{rt} is an independent and identically distributed (iid) sequence and E(r2
t ) < ∞,
then ˆρ1 is asymptotically normal with mean zero and variance 1/T ; see Brockwell
and Davis (1991, Theorem 7.2.2). This result can be used in practice to test the
null hypothesis H0 : ρ1 = 0 versus the alternative hypothesis Ha : ρ1̸ = 0. The test
statistic is the usual t ratio, which is
√
T ˆρ1 and follows asymptotically the standard
normal distribution. The null hypothesis H0 is rejected if the t ratio is large in
magnitude or, equivalently, the p value of the t ratio is small, say less than 0.05.
In general, the lag-ℓsample autocorrelation of rt is deﬁned as
ˆρℓ=
T
t=ℓ+1(rt −¯r)(rt−ℓ−¯r)
T
t=1(rt −¯r)2
,
0 ≤ℓ< T −1.
(2.2)
If {rt} is an iid sequence satisfying E(r2
t ) < ∞, then ˆρℓis asymptotically normal
with mean zero and variance 1/T for any ﬁxed positive integer ℓ. More generally,
if rt is a weakly stationary time series satisfying rt = µ + q
i=0 ψiat−i, where
--- page 59 ---

32
linear time series analysis and its applications
ψ0 = 1 and {aj} is a sequence of iid random variables with mean zero, then ˆρℓis
asymptotically normal with mean zero and variance (1 + 2 q
i=1 ρ2
i )/T for ℓ> q.
This is referred to as Bartlett’s formula in the time series literature; see Box,
Jenkins, and Reinsel (1994). For more information about the asymptotic distribution
of sample autocorrelations, see Fuller (1976, Chapter 6) and Brockwell and Davis
(1991, Chapter 7).
Testing Individual ACF
For a given positive integer ℓ, the previous result can be used to test H0 : ρℓ= 0
vs. Ha : ρℓ̸ = 0. The test statistic is
t ratio =
ˆρℓ

(1 + 2 ℓ−1
i=1 ˆρ2
i )/T
.
If {rt} is a stationary Gaussian series satisfying ρj = 0 for j > ℓ, the t ratio
is asymptotically distributed as a standard normal random variable. Hence, the
decision rule of the test is to reject H0 if |t ratio| > Zα/2, where Zα/2 is the
100(1 −α/2)th percentile of the standard normal distribution. For simplicity, many
software packages use 1/T as the asymptotic variance of ˆρℓfor all ℓ̸ = 0. They
essentially assume that the underlying time series is an iid sequence.
In ﬁnite samples, ˆρℓis a biased estimator of ρℓ. The bias is in the order of
1/T , which can be substantial when the sample size T is small. In most ﬁnancial
applications, T is relatively large so that the bias is not serious.
Portmanteau Test
Financial applications often require to test jointly that several autocorrelations of
rt are zero. Box and Pierce (1970) propose the Portmanteau statistic
Q∗(m) = T
m

ℓ=1
ˆρ2
ℓ
as a test statistic for the null hypothesis H0 : ρ1 = · · · = ρm = 0 against the alternative hypothesis Ha : ρi̸ = 0 for some i ∈{1, . . . , m}. Under the assumption that
{rt} is an iid sequence with certain moment conditions, Q∗(m) is asymptotically a
chi-squared random variable with m degrees of freedom.
Ljung and Box (1978) modify the Q∗(m) statistic as below to increase the power
of the test in ﬁnite samples,
Q(m) = T (T + 2)
m

ℓ=1
ˆρ2
ℓ
T −ℓ.
(2.3)
The decision rule is to reject H0 if Q(m) > χ2
α, where χ2
α denotes the 100(1 −α)th
percentile of a chi-squared distribution with m degrees of freedom. Most software
--- page 60 ---

correlation and autocorrelation function
33
packages will provide the p value of Q(m). The decision rule is then to reject H0
if the p value is less than or equal to α, the signiﬁcance level.
In practice, the choice of m may affect the performance of the Q(m) statistic.
Several values of m are often used. Simulation studies suggest that the choice of
m ≈ln(T ) provides better power performance. This general rule needs modiﬁcation
in analysis of seasonal time series for which autocorrelations with lags at multiples
of the seasonality are more important.
The statistics ˆρ1, ˆρ2, . . . deﬁned in Eq. (2.2) is called the sample autocorrelation function (ACF) of rt. It plays an important role in linear time series analysis.
As a matter of fact, a linear time series model can be characterized by its ACF,
and linear time series modeling makes use of the sample ACF to capture the linear dynamic of the data. Figure 2.1 shows the sample autocorrelation functions
of monthly simple and log returns of IBM stock from January 1926 to December 2008. The two sample ACFs are very close to each other, and they suggest
that the serial correlations of monthly IBM stock returns are very small, if any.
The sample ACFs are all within their two standard error limits, indicating that
they are not signiﬁcantly different from zero at the 5% level. In addition, for the
simple returns, the Ljung–Box statistics give Q(5) = 3.37 and Q(10) = 13.99,
which correspond to p values of 0.64 and 0.17, respectively, based on chi-squared
Lag
(a)
ACF
0
20
40
60
80
100
−0.2 −0.1 0.0
0.1
0.2
Lag
(b)
ACF
0
20
40
60
80
100
−0.2 −0.1 0.0
0.1
0.2
Figure 2.1
Sample autocorrelation functions of monthly (a) simple returns and (b) log returns of
IBM stock from January 1926 to December 2008. In each plot, two horizontal dashed lines denote two
standard error limits of sample ACF.
--- page 61 ---

34
linear time series analysis and its applications
Lag
(a)
ACF
0
20
40
60
80
100
−0.2 −0.1 0.0
0.1
0.2
Lag
(b)
ACF
0
20
40
60
80
100
−0.2 −0.1 0.0
0.1
0.2
Figure 2.2
Sample autocorrelation functions of monthly (a) simple returns and (b) log returns of valueweighted index of U.S. markets from January 1926 to December 2008. In each plot, two horizontal
dashed lines denote two standard error limits of sample ACF.
distributions with 5 and 10 degrees of freedom. For the log returns, we have
Q(5) = 3.52 and Q(10) = 13.39 with p values 0.62 and 0.20, respectively. The
joint tests conﬁrm that monthly IBM stock returns have no signiﬁcant serial correlations. Figure 2.2 shows the same for the monthly returns of the value-weighted
index from the Center for Research in Security Prices (CRSP), at the University
of Chicago. There are some signiﬁcant serial correlations at the 5% level for both
return series. The Ljung–Box statistics give Q(5) = 29.71 and Q(10) = 39.55 for
the simple returns and Q(5) = 28.38 and Q(10) = 36.16 for the log returns. The
p values of these four test statistics are all less than 0.0001, suggesting that monthly
returns of the value-weighted index are serially correlated. Thus, the monthly market index return seems to have stronger serial dependence than individual stock
returns.
In the ﬁnance literature, a version of the capital asset pricing model (CAPM)
theory is that the return {rt} of an asset is not predictable and should have no autocorrelations. Testing for zero autocorrelations has been used as a tool to check the
efﬁcient market assumption. However, the way by which stock prices are determined and index returns are calculated might introduce autocorrelations in the
observed return series. This is particularly so in analysis of high-frequency ﬁnancial
data. We discuss some of these issues, such as bid–ask bounce and nonsynchronous
trading, in Chapter 5.
--- page 62 ---

correlation and autocorrelation function
35
R Demonstration
The following output has been edited and % denotes explanation:
> da=read.table("m-ibm3dx2608.txt",header=T) % Load data
> da[1,]
% Check the 1st row of the data
date
rtn
vwrtn
ewrtn
sprtn
1 19260130 -0.010381 0.000724 0.023174 0.022472
> sibm=da[,2] % Get the IBM simple returns
> Box.test(sibm,lag=5,type=’Ljung’) % Ljung-Box statistic Q(5)
Box-Ljung test
data: sibm
X-squared = 3.3682, df = 5, p-value = 0.6434
> libm=log(sibm+1)
% Log IBM returns
> Box.test(libm,lag=5,type=’Ljung’)
Box-Ljung test
data: libm
X-squared = 3.5236, df = 5, p-value = 0.6198
S-Plus Demonstration
Output edited.
> module(finmetrics)
> da=read.table("m-ibm3dx2608.txt",header=T) % Load data
> da[1,]
% Check the 1st row of the data
date
rtn
vwrtn
ewrtn
sprtn
1 19260130 -0.010381 0.000724 0.023174 0.022472
> sibm=da[,2] % Get IBM simple returns
> autocorTest(sibm,lag=5) % Ljung-Box Q(5) test
Test for Autocorrelation: Ljung-Box
Null Hypothesis: no autocorrelation
Test Statistics:
Test Stat 3.3682
p.value 0.6434
Dist. under Null: chi-square with 5 degrees of freedom
Total Observ.: 996
> libm=log(sibm+1) % IBM log returns
> autocorTest(libm,lag=5)
Test for Autocorrelation: Ljung-Box
Null Hypothesis: no autocorrelation
Test Statistics:
Test Stat 3.5236
p.value 0.6198
--- page 63 ---

36
linear time series analysis and its applications
2.3
WHITE NOISE AND LINEAR TIME SERIES
White Noise
A time series rt is called a white noise if {rt} is a sequence of independent and
identically distributed random variables with ﬁnite mean and variance. In particular,
if rt is normally distributed with mean zero and variance σ 2, the series is called a
Gaussian white noise. For a white noise series, all the ACFs are zero. In practice,
if all sample ACFs are close to zero, then the series is a white noise series. Based
on Figures 2.1 and 2.2, the monthly returns of IBM stock are close to white noise,
whereas those of the value-weighted index are not.
The behavior of sample autocorrelations of the value-weighted index returns
indicates that for some asset returns it is necessary to model the serial dependence
before further analysis can be made. In what follows, we discuss some simple time
series models that are useful in modeling the dynamic structure of a time series.
The concepts presented are also useful later in modeling volatility of asset returns.
Linear Time Series
A time series rt is said to be linear if it can be written as
rt = µ +
∞

i=0
ψiat−i,
(2.4)
where µ is the mean of rt, ψ0 = 1, and {at} is a sequence of iid random variables
with mean zero and a well-deﬁned distribution (i.e., {at} is a white noise series). It
will be seen later that at denotes the new information at time t of the time series
and is often referred to as the innovation or shock at time t. In this book, we are
mainly concerned with the case where at is a continuous random variable. Not
all ﬁnancial time series are linear, however. We study nonlinearity and nonlinear
models in Chapter 4.
For a linear time series in Eq. (2.4), the dynamic structure of rt is governed by
the coefﬁcients ψi, which are called the ψ weights of rt in the time series literature.
If rt is weakly stationary, we can obtain its mean and variance easily by using the
independence of {at} as
E(rt) = µ,
Var(rt) = σ 2
a
∞

i=0
ψ2
i ,
(2.5)
where σ 2
a is the variance of at. Because Var(rt) < ∞, {ψ2
i } must be a convergent
sequence, that is, ψ2
i →0 as i →∞. Consequently, for a stationary series, impact
of the remote shock at−i on the return rt vanishes as i increases.
The lag-ℓautocovariance of rt is
γℓ= Cov(rt, rt−ℓ) = E


 ∞

i=0
ψiat−i
 

∞

j=0
ψjat−ℓ−j




--- page 64 ---

simple ar models
37
= E


∞

i,j=0
ψiψjat−iat−ℓ−j


=
∞

j=0
ψj+ℓψjE(a2
t−ℓ−j) = σ 2
a
∞

j=0
ψjψj+ℓ.
(2.6)
Consequently, the ψ weights are related to the autocorrelations of rt as follows:
ρℓ= γℓ
γ0
=
∞
i=0 ψiψi+ℓ
1 + ∞
i=1 ψ2
i
,
ℓ≥0,
(2.7)
where ψ0 = 1. Linear time series models are econometric and statistical models
used to describe the pattern of the ψ weights of rt. For a weakly stationary time
series, ψi →0 as i →∞and, hence, ρℓconverges to zero as ℓincreases. For asset
returns, this means that, as expected, the linear dependence of current return rt on
the remote past return rt−ℓdiminishes for large ℓ.
2.4
SIMPLE AR MODELS
The fact that the monthly return rt of CRSP value-weighted index has a statistically
signiﬁcant lag-1 autocorrelation indicates that the lagged return rt−1 might be useful
in predicting rt. A simple model that makes use of such predictive power is
rt = φ0 + φ1rt−1 + at,
(2.8)
where {at} is assumed to be a white noise series with mean zero and variance
σ 2
a . This model is in the same form as the well-known simple linear regression
model in which rt is the dependent variable and rt−1 is the explanatory variable.
In the time series literature, model (2.8) is referred to as an autoregressive (AR)
model of order 1 or simply an AR(1) model. This simple model is also widely
used in stochastic volatility modeling when rt is replaced by its log volatility; see
Chapters 3 and 12.
The AR(1) model in Eq. (2.8) has several properties similar to those of the
simple linear regression model. However, there are some signiﬁcant differences
between the two models, which we discuss later. Here it sufﬁces to note that an
AR(1) model implies that, conditional on the past return rt−1, we have
E(rt|rt−1) = φ0 + φ1rt−1,
Var(rt|rt−1) = Var(at) = σ 2
a .
That is, given the past return rt−1, the current return is centered around φ0 + φ1rt−1
with standard deviation σa. This is a Markov property such that conditional on rt−1,
the return rt is not correlated with rt−i for i > 1. Obviously, there are situations
in which rt−1 alone cannot determine the conditional expectation of rt and a more
--- page 65 ---

38
linear time series analysis and its applications
ﬂexible model must be sought. A straightforward generalization of the AR(1) model
is the AR(p) model:
rt = φ0 + φ1rt−1 + · · · + φprt−p + at,
(2.9)
where p is a nonnegative integer and {at} is deﬁned in Eq. (2.8). This model
says that the past p variables rt−i (i = 1, . . . , p) jointly determine the conditional
expectation of rt given the past data. The AR(p) model is in the same form as
a multiple linear regression model with lagged values serving as the explanatory
variables.
2.4.1
Properties of AR Models
For effective use of AR models, it pays to study their basic properties. We discuss
properties of AR(1) and AR(2) models in detail and give the results for the general
AR(p) model.
AR(1) Model
We begin with the sufﬁcient and necessary condition for weak stationarity of the
AR(1) model in Eq. (2.8). Assuming that the series is weakly stationary, we have
E(rt) = µ, Var(rt) = γ0, and Cov(rt, rt−j) = γj, where µ and γ0 are constant and
γj is a function of j, not t. We can easily obtain the mean, variance, and autocorrelations of the series as follows. Taking the expectation of Eq. (2.8) and because
E(at) = 0, we obtain
E(rt) = φ0 + φ1E(rt−1).
Under the stationarity condition, E(rt) = E(rt−1) = µ and hence
µ = φ0 + φ1µ
or
E(rt) = µ =
φ0
1 −φ1
.
This result has two implications for rt. First, the mean of rt exists if φ1̸ = 1.
Second, the mean of rt is zero if and only if φ0 = 0. Thus, for a stationary AR(1)
process, the constant term φ0 is related to the mean of rt via φ0 = (1 −φ1)µ and
φ0 = 0 implies that E(rt) = 0.
Next, using φ0 = (1 −φ1)µ, the AR(1) model can be rewritten as
rt −µ = φ1(rt−1 −µ) + at.
(2.10)
By repeated substitutions, the prior equation implies that
rt −µ = at + φ1at−1 + φ2
1at−2 + · · ·
=
∞

i=0
φi
1at−i.
(2.11)
--- page 66 ---

simple ar models
39
This equation expresses an AR(1) model in the form of Eq. (2.4) with ψi = φi
1.
Thus, rt −µ is a linear function of at−i for i ≥0. Using this property and the
independence of the series {at}, we obtain E[(rt −µ)at+1] = 0. By the stationarity
assumption, we have Cov(rt−1, at) = E[(rt−1 −µ)at] = 0. This latter result can
also be seen from the fact that rt−1 occurred before time t and at does not depend
on any past information. Taking the square, then the expectation of Eq. (2.10), we
obtain
Var(rt) = φ2
1Var(rt−1) + σ 2
a ,
where σ 2
a is the variance of at, and we make use of the fact that the covariance
between rt−1 and at is zero. Under the stationarity assumption, Var(rt) = Var(rt−1),
so that
Var(rt) =
σ 2
a
1 −φ2
1
provided that φ2
1 < 1. The requirement of φ2
1 < 1 results from the fact that the
variance of a random variable is bounded and nonnegative. Consequently, the weak
stationarity of an AR(1) model implies that −1 < φ1 < 1, that is, |φ1| < 1. Yet if
|φ1| < 1, then by Eq. (2.11) and the independence of the {at} series, we can show
that the mean and variance of rt are ﬁnite and time invariant; see Eq. (2.5). In
addition, by Eq. (2.6), all the autocovariances of rt are ﬁnite. Therefore, the AR(1)
model is weakly stationary. In summary, the necessary and sufﬁcient condition for
the AR(1) model in Eq. (2.8) to be weakly stationary is |φ1| < 1.
Using φ0 = (1 −φ1)µ, one can rewrite a stationary AR(1) model as
rt = (1 −φ1)µ + φ1rt−1 + at.
This model is often used in the ﬁnance literature with φ1 measuring the persistence
of the dynamic dependence of an AR(1) time series.
Autocorrelation Function of an AR(1) Model
Multiplying Eq. (2.10) by at, using the independence between at and rt−1, and
taking expectation, we obtain
E[at(rt −µ)] = φ1E[at(rt−1 −µ)] + E(a2
t ) = E(a2
t ) = σ 2
a ,
where σ 2
a is the variance of at. Multiplying Eq. (2.10) by rt−ℓ−µ, taking expectation, and using the prior result, we have
γℓ=

φ1γ1 + σ 2
a
if ℓ= 0
φ1γℓ−1
if ℓ> 0,
--- page 67 ---

40
linear time series analysis and its applications
where we use γℓ= γ−ℓ. Consequently, for a weakly stationary AR(1) model in
Eq. (2.8), we have
Var(rt) = γ0 =
σ 2
1 −φ2
1
and
γℓ= φ1γℓ−1,
for
ℓ> 0.
From the latter equation, the ACF of rt satisﬁes
ρℓ= φ1ρℓ−1,
for
ℓ> 0.
Because ρ0 = 1, we have ρℓ= φℓ
1. This result says that the ACF of a weakly
stationary AR(1) series decays exponentially with rate φ1 and starting value ρ0 = 1.
For a positive φ1, the plot of ACF of an AR(1) model shows a nice exponential
decay. For a negative φ1, the plot consists of two alternating exponential decays
with rate φ2
1. Figure 2.3 shows the ACF of two AR(1) models with φ1 = 0.8 and
φ1 = −0.8.
AR(2) Model
An AR(2) model assumes the form
rt = φ0 + φ1rt−1 + φ2rt−2 + at.
(2.12)
ACF
−1.0
−0.5
0.0
0
5
10
Lag
(a)
15
0.5
1.0
ACF
−1.0
−0.5
0.0
0
5
10
Lag
(b)
15
0.5
1.0
Figure 2.3
Autocorrelation function of an AR(1) model: (a) for φ1 = 0.8 and (b) for φ1 = −0.8.
--- page 68 ---

simple ar models
41
Using the same technique as that of the AR(1) case, we obtain
E(rt) = µ =
φ0
1 −φ1 −φ2
provided that φ1 + φ2̸ = 1. Using φ0 = (1 −φ1 −φ2)µ, we can rewrite the AR(2)
model as
(rt −µ) = φ1(rt−1 −µ) + φ2(rt−2 −µ) + at.
Multiplying the prior equation by (rt−ℓ−µ), we have
(rt−ℓ−µ)(rt −µ) = φ1(rt−ℓ−µ)(rt−1 −µ)
+ φ2(rt−ℓ−µ)(rt−2 −µ) + (rt−ℓ−µ)at.
Taking expectation and using E[(rt−ℓ−µ)at] = 0 for ℓ> 0, we obtain
γℓ= φ1γℓ−1 + φ2γℓ−2,
for
ℓ> 0.
This result is referred to as the moment equation of a stationary AR(2) model.
Dividing the above equation by γ0, we have the property
ρℓ= φ1ρℓ−1 + φ2ρℓ−2,
for
ℓ> 0,
(2.13)
for the ACF of rt. In particular, the lag-1 ACF satisﬁes
ρ1 = φ1ρ0 + φ2ρ−1 = φ1 + φ2ρ1.
Therefore, for a stationary AR(2) series rt, we have ρ0 = 1,
ρ1 =
φ1
1 −φ2
ρℓ= φ1ρℓ−1 + φ2ρℓ−2,
ℓ≥2.
The result of Eq. (2.13) says that the ACF of a stationary AR(2) series satisﬁes the
second-order difference equation
(1 −φ1B −φ2B2)ρℓ= 0,
where B is called the back-shift operator such that Bρℓ= ρℓ−1. This difference
equation determines the properties of the ACF of a stationary AR(2) time series.
It also determines the behavior of the forecasts of rt. In the time series literature,
some people use the notation L instead of B for the back-shift operator. Here
L stands for lag operator. For instance, Lrt = rt−1 and Lψk = ψk−1.
--- page 69 ---

42
linear time series analysis and its applications
Corresponding to the prior difference equation, there is a second-order polynomial equation:
1 −φ1x −φ2x2 = 0.
(2.14)
Solutions of this equation are
x =
φ1 ±

φ2
1 + 4φ2
−2φ2
.
In the time series literature, inverses of the two solutions are referred to as the
characteristic roots of the AR(2) model. Denote the two characteristic roots by
ω1 and ω2. If both ωi are real valued, then the second-order difference equation
of the model can be factored as (1 −ω1B)(1 −ω2B) and the AR(2) model can
be regarded as an AR(1) model operates on top of another AR(1) model. The
ACF of rt is then a mixture of two exponential decays. If φ2
1 + 4φ2 < 0, then ω1
and ω2 are complex numbers (called a complex-conjugate pair), and the plot of
ACF of rt would show a picture of damping sine and cosine waves. In business and
economic applications, complex characteristic roots are important. They give rise to
the behavior of business cycles. It is then common for economic time series models
to have complex-valued characteristic roots. For an AR(2) model in Eq. (2.12) with
a pair of complex characteristic roots, the average length of the stochastic cycles is
k =
2π
cos−1[φ1/(2√−φ2)],
where the cosine inverse is stated in radians. If one writes the complex solutions
as a ± bi, where i =
√
−1, then we have φ1 = 2a, φ2 = −(a2 + b2), and
k =
2π
cos−1(a/
√
a2 + b2)
,
where
√
a2 + b2 is the absolute value of a ± bi. See Example 2.1 for an illustration.
Figure 2.4 shows the ACF of four stationary AR(2) models. Part (b) is the ACF
of the AR(2) model (1 −0.6B + 0.4B2)rt = at. Because φ2
1 + 4φ2 = 0.36 + 4 ×
(−0.4) = −1.24 < 0, this particular AR(2) model contains two complex characteristic roots, and hence its ACF exhibits damping sine and cosine waves. The
other three AR(2) models have real-valued characteristic roots. Their ACFs decay
exponentially.
Example 2.1.
As an illustration, consider the quarterly growth rate of U.S.
real gross national product (GNP), seasonally adjusted, from the second quarter
of 1947 to the ﬁrst quarter of 1991. This series shown in Figure 2.5 is also used
in Chapter 4 as an example of nonlinear economic time series. Here we simply
employ an AR(3) model for the data. Denoting the growth rate by rt, we can use
--- page 70 ---

simple ar models
43
Lag
ACF
0
5
10
15
20
−1.0 −0.5 0.0
0.5
1.0
(a)
Lag
ACF
0
5
10
15
20
−1.0 −0.5 0.0
0.5
1.0
(c)
Lag
ACF
0
5
10
15
20
−1.0 −0.5 0.0
0.5
1.0
(b)
Lag
ACF
0
5
10
15
20
−1.0 −0.5 0.0
0.5
1.0
(d)
Figure 2.4
Autocorrelation function of an AR(2) model: (a) φ1 = 1.2 and φ2 = −0.35, (b) φ1 = 0.6
and φ2 = −0.4, (c) φ1 = 0.2 and φ2 = 0.35, and (d) φ1 = −0.2 and φ2 = 0.35.
the model building procedure of the next subsection to estimate the model. The
ﬁtted model is
rt = 0.0047 + 0.348rt−1 + 0.179rt−2 −0.142rt−3 + at,
ˆσa = 0.0097. (2.15)
Rewriting the model as
rt −0.348rt−1 −0.179rt−2 + 0.142rt−3 = 0.0047 + at,
we obtain a corresponding third-order difference equation
1 −0.348B −0.179B2 + 0.141B3 = 0,
which can be factored approximately as
(1 + 0.521B)(1 −0.869B + 0.274B2) = 0.
The ﬁrst factor (1 + 0.521B) shows an exponentially decaying feature of the GNP
growth rate. Focusing on the second-order factor 1 −0.869B −(−0.274)B2 = 0,
we have φ2
1 + 4φ2 = 0.8692 + 4(−0.274) = −0.341 < 0. Therefore, the second
factor of the AR(3) model conﬁrms the existence of stochastic business cycles
--- page 71 ---

44
linear time series analysis and its applications
•
•
•
•
•
••
•
•
•
•
•
•
•
•
•
•
•
•
•
•
•
•
•
•
•
•
•
•
•
•
•
•
•
•
•
•
•
•
•
•
•
•
•
•
••
•
•
•
•
•
•
•
•
•••
•
•
••
•
••
•
•
•
••
•
•
••
•
•
•
•
•••
•
•
•
•
•
•
•
•
•
•
•
•
•
•
•
•
•
•
•
•
•
•
•
•
•
•
•
•
•
•
•
•
•
•
•
••
•
•
•
•
•
•
•
•
•
••
•
•
•
•
•
•
•
•
•
••
•
•
•
•
•
•
•
•
•
•
•
•
•
•
•
•
•
•
•
•
••
•
•
•
••
•
••
•
•
•
•
•
•
Year
Growth
1950
1960
1970
1980
1990
−2
−1
0
1
2
3
4
Figure 2.5
Time plot of growth rate of U.S. quarterly real GNP from 1947.II to 1991.I. Data are
seasonally adjusted and in percentages.
in the quarterly growth rate of U.S. real GNP. This is reasonable as the U.S.
economy went through expansion and contraction periods. The average length of
the stochastic cycles is approximately
k =
2(3.14159)
cos−1[φ1/(2√−φ2)] = 10.62 quarters,
which is about 3 years. If one uses a nonlinear model to separate U.S. economy
into “expansion” and “contraction” periods, the data show that the average duration
of contraction periods is about three quarters and that of expansion periods is about
3 years; see the analysis in Chapter 4. The average duration of 10.62 quarters is
a compromise between the two separate durations. The periodic feature obtained
here is common among growth rates of national economies. For example, similar
features can be found for many OECD (Organization for Economic Cooperation
and Development) countries.
R Demonstration
The R demonstration for Example 2.1, where % denotes explanation, follows:
> gnp=scan(file=’dgnp82.txt’) % Load data
% To create a time-series object
> gnp1=ts(gnp,frequency=4,start=c(1947,2))
> plot(gnp1)
--- page 72 ---

simple ar models
45
> points(gnp1,pch=’*’)
> m1=ar(gnp,method=’’mle’’) % Find the AR order
> m1$order
% An AR(3) is selected based on AIC
[1] 3
> m2=arima(gnp,order=c(3,0,0)) % Estimation
> m2
Call:
arima(x = gnp, order = c(3, 0, 0))
Coefficients:
ar1
ar2
ar3
intercept
0.3480
0.1793
-0.1423
0.0077
s.e.
0.0745
0.0778
0.0745
0.0012
sigma^2 estimated as 9.427e-05: log likelihood=565.84,
aic=-1121.68
% In R, ‘‘intercept’’ denotes the mean of the series.
% Therefore, the constant term is obtained below:
> (1-.348-.1793+.1423)*0.0077
[1] 0.0047355
> sqrt(m2$sigma2)
% Residual standard error
[1] 0.009709322
> p1=c(1,-m2$coef[1:3]) % Characteristic equation
> roots=polyroot(p1) % Find solutions
> roots
[1] 1.590253+1.063882i -1.920152+0.000000i 1.590253-1.063882i
> Mod(roots) % Compute the absolute values of the solutions
[1] 1.913308 1.920152 1.913308
% To compute average length of business cycles:
> k=2*pi/acos(1.590253/1.913308)
> k
[1] 10.65638
Stationarity
The stationarity condition of an AR(2) time series is that the absolute values of
its two characteristic roots are less than 1, that is, its two characteristic roots
are less than 1 in modulus. Equivalently, the two solutions of the characteristic
equation are greater than 1 in modulus. Under such a condition, the recursive
equation in (2.13) ensures that the ACF of the model converges to 0 as the
lag ℓincreases. This convergence property is a necessary condition for a stationary time series. In fact, the condition also applies to the AR(1) model where
the polynomial equation is 1 −φ1x = 0. The characteristic root is w = 1/x = φ1,
which must be less than 1 in modulus for rt to be stationary. As shown before,
ρℓ= φℓ
1 for a stationary AR(1) model. The condition implies that ρℓ→0 as
ℓ→∞.
--- page 73 ---

46
linear time series analysis and its applications
AR(p) Model
The results of the AR(1) and AR(2) models can readily be generalized to the
general AR(p) model in Eq. (2.9). The mean of a stationary series is
E(rt) =
φ0
1 −φ1 −· · · −φp
provided that the denominator is not zero. The associated characteristic equation
of the model is
1 −φ1x −φ2x2 −· · · −φpxp = 0.
If all the solutions of this equation are greater than 1 in modulus, then the series
rt is stationary. Again, inverses of the solutions are the characteristic roots of the
model. Thus, stationarity requires that all characteristic roots are less than 1 in
modulus. For a stationary AR(p) series, the ACF satisﬁes the difference equation
(1 −φ1B −φ2B2 −· · · −φpBp)ρℓ= 0,
for
ℓ> 0.
The plot of ACF of a stationary AR(p) model would then show a mixture of
damping sine and cosine patterns and exponential decays depending on the nature
of its characteristic roots.
2.4.2
Identifying AR Models in Practice
In application, the order p of an AR time series is unknown. It must be speciﬁed
empirically. This is referred to as the order determination (or order speciﬁcation)
of AR models, and it has been extensively studied in the time series literature. Two
general approaches are available for determining the value of p. The ﬁrst approach
is to use the partial autocorrelation function, and the second approach uses some
information criteria.
Partial Autocorrelation Function (PACF)
The PACF of a stationary time series is a function of its ACF and is a useful
tool for determining the order p of an AR model. A simple, yet effective way to
introduce PACF is to consider the following AR models in consecutive orders:
rt = φ0,1 + φ1,1rt−1 + e1t,
rt = φ0,2 + φ1,2rt−1 + φ2,2rt−2 + e2t,
rt = φ0,3 + φ1,3rt−1 + φ2,3rt−2 + φ3,3rt−3 + e3t,
rt = φ0,4 + φ1,4rt−1 + φ2,4rt−2 + φ3,4rt−3 + φ4,4rt−4 + e4t,
...
--- page 74 ---

simple ar models
47
where φ0,j, φi,j, and {ejt} are, respectively, the constant term, the coefﬁcient of
rt−i, and the error term of an AR(j) model. These models are in the form of a
multiple linear regression and can be estimated by the least-squares method. As a
matter of fact, they are arranged in a sequential order that enables us to apply the
idea of partial F test in multiple linear regression analysis. The estimate ˆφ1,1 of
the ﬁrst equation is called the lag-1 sample PACF of rt. The estimate ˆφ2,2 of the
second equation is the lag-2 sample PACF of rt. The estimate ˆφ3,3 of the third
equation is the lag-3 sample PACF of rt, and so on.
From the deﬁnition, the lag-2 PACF ˆφ2,2 shows the added contribution of rt−2
to rt over the AR(1) model rt = φ0 + φ1rt−1 + e1t. The lag-3 PACF shows the
added contribution of rt−3 to rt over an AR(2) model, and so on. Therefore, for
an AR(p) model, the lag-p sample PACF should not be zero, but ˆφj,j should be
close to zero for all j > p. We make use of this property to determine the order
p. For a stationary Gaussian AR(p) model, it can be shown that the sample PACF
has the following properties:
• ˆφp,p converges to φp as the sample size T goes to inﬁnity.
• ˆφℓ,ℓconverges to zero for all ℓ> p.
• The asymptotic variance of ˆφℓ,ℓis 1/T for ℓ> p.
These results say that, for an AR(p) series, the sample PACF cuts off at
lag p.
As an example, consider the monthly simple returns of CRSP value-weighted
index from January 1926 to December 2008. Table 2.1 gives the ﬁrst 12 lags of
sample PACF of the series. With T = 996, the asymptotic standard error of the
sample PACF is approximately 0.032. Therefore, using the 5% signiﬁcant level,
we identify an AR(3) or AR(9) model for the data (i.e., p = 3 or 9). If the 1%
signiﬁcant level is used, we specify an AR(3) model.
As another example, Figure 2.6 shows the PACF of the GNP growth rate series
of Example 2.1. The two dotted lines of the plot denote the approximate two
standard error limits ±(2/
√
176). The plot suggests an AR(3) model for the data
because the ﬁrst three lags of sample PACF appear to be large.
TABLE 2.1
Sample Partial Autocorrelation Function and Some Information
Criteria for the Monthly Simple Returns of CRSP Value-Weighted Index from
January 1926 to December 2008
p
1
2
3
4
5
6
PACF
0.115
−0.030
−0.102
0.033
0.062
−0.050
AIC
−5.838
−5.837
−5.846
−5.845
−5.847
−5.847
BIC
−5.833
−5.827
−5.831
−5.825
−5.822
−5.818
p
7
8
9
10
11
12
PACF
0.031
0.052
0.063
0.005
−0.005
0.011
AIC
−5.846
−5.847
−5.849
−5.847
−5.845
−5.843
BIC
−5.812
−5.807
−5.805
−5.798
−5.791
−5.784
--- page 75 ---

48
linear time series analysis and its applications
Lag
PACF
2
4
6
8
10
12
−0.4
 −0.2
0.0
0.2
0.4
Figure 2.6
Sample partial autocorrelation function of U.S. quarterly real GNP growth rate from 1947.II
to 1991.I. Dotted lines give approximate pointwise 95% conﬁdence interval.
Information Criteria
There are several information criteria available to determine the order p of an AR
process. All of them are likelihood based. For example, the well-known Akaike
information criterion (AIC) (Akaike, 1973) is deﬁned as
AIC = −2
T ln(likelihood) + 2
T × (number of parameters),
(2.16)
where the likelihood function is evaluated at the maximum-likelihood estimates
and T is the sample size. For a Gaussian AR(ℓ) model, AIC reduces to
AIC(ℓ) = ln(˜σ 2
ℓ) + 2ℓ
T
where ˜σ 2
ℓis the maximum-likelihood estimate of σ 2
a , which is the variance of at,
and T is the sample size; see Eq. (1.18). The ﬁrst term of the AIC in Eq. (2.16)
measures the goodness of ﬁt of the AR(ℓ) model to the data, whereas the second
term is called the penalty function of the criterion because it penalizes a candidate
model by the number of parameters used. Different penalty functions result in
different information criteria.
Another commonly used criterion function is the Schwarz–Bayesian information
criterion (BIC). For a Gaussian AR(ℓ) model, the criterion is
BIC(ℓ) = ln(˜σ 2
ℓ) + ℓln(T )
T
.
--- page 76 ---

simple ar models
49
The penalty for each parameter used is 2 for AIC and ln(T ) for BIC. Thus, compared with AIC, BIC tends to select a lower AR model when the sample size is
moderate or large.
Selection Rule
To use AIC to select an AR model in practice, one computes AIC(ℓ) for ℓ=
0, . . . , P , where p is a prespeciﬁed positive integer and selects the order k that has
the minimum AIC value. The same rule applies to BIC.
Table 2.1 also gives the AIC and BIC for p = 1, . . . , 12. The AIC values are
close to each other with minimum −5.849 occurring at p = 9, suggesting that an
AR(9) model is preferred by the criterion. The BIC, on the other hand, attains
its minimum value −5.833 at p = 1 with −5.831 as a close second at p = 3.
Thus, the BIC selects an AR(1) model for the value-weighted return series. This
example shows that different approaches or criteria to order determination may
result in different choices of p. There is no evidence to suggest that one approach
outperforms the other in a real application. Substantive information of the problem
under study and simplicity are two factors that also play an important role in
choosing an AR model for a given time series.
Again, consider the growth rate series of U.S. quarterly real GNP of
Example 2.1. The AIC obtained from R also identiﬁes an AR(3) model. Note that
the AIC value of the ar command in R has been adjusted so that the minimum
AIC is zero.
> gnp=scan(file=’q-gnp4791.txt’)
> ord=ar(gnp,method=’’mle’’)
> ord$aic
[1] 27.847 2.742 1.603 0.000 0.323 2.243
[7]
4.052 6.025 5.905 7.572 7.895 9.679
> ord$order
[1] 3
Parameter Estimation
For a speciﬁed AR(p) model in Eq. (2.9), the conditional least-squares method,
which starts with the (p + 1)th observation, is often used to estimate the parameters.
Speciﬁcally, conditioning on the ﬁrst p observations, we have
rt = φ0 + φ1rt−1 + · · · + φprt−p + at,
t = p + 1, . . . , T,
which is in the form of a multiple linear regression and can be estimated by the
least-squares method. Denote the estimate of φi by ˆφi. The ﬁtted model is
ˆrt = ˆφ0 + ˆφ1rt−1 + · · · + ˆφprt−p,
and the associated residual is
ˆat = rt −ˆrt.
--- page 77 ---

50
linear time series analysis and its applications
The series {ˆat} is called the residual series, from which we obtain
ˆσ 2
a =
T
t=p+1 ˆa2
t
T −2p −1.
If the conditional-likelihood method is used, the estimates of φi remain unchanged,
but the estimate of σ 2
a becomes ˜σ 2
a = ˆσ 2
a × (T −2p −1)/(T −p). In some packages, ˜σ 2
a is deﬁned as ˆσ 2
a × (T −2p −1)/T . For illustration, consider an AR(3)
model for the monthly simple returns of the value-weighted index in Table 2.1.
The ﬁtted model is
rt = 0.0091 + 0.116rt−1 −0.019rt−2 −0.104rt−3 + ˆat,
ˆσa = 0.054.
The standard errors of the coefﬁcients are 0.002, 0.032, 0.032, and 0.032, respectively. Except for the lag-2 coefﬁcient, all parameters are statistically signiﬁcant at
the 1% level.
For this example, the AR coefﬁcients of the ﬁtted model are small, indicating that
the serial dependence of the series is weak, even though it is statistically signiﬁcant
at the 1% level. The signiﬁcance of ˆφ0 of the entertained model implies that the
expected mean return of the series is positive. In fact, ˆµ = 0.0091/(1 −0.116 +
0.019 + 0.104) = 0.009, which is small but has an important long-term implication.
It implies that the long-term return of the index can be substantial. Using the
multiperiod simple return deﬁned in Chapter 1, the average annual simple gross
return is [996
t=1(1 + Rt)]12/996 −1 ≈0.093. In other words, the monthly simple
returns of the CRSP value-weighted index grew about 9.3% per annum from 1926
to 2008, supporting the common belief that equity market performs well in the
long term. A one-dollar investment at the beginning of 1926 would be worth about
$1593 at the end of 2008.
> vw=read.table(’m-ibm3dx.txt’,header=T)[,3]
> t1=prod(vw+1)
> t1
[1] 1592.953
> t1^(12/996)-1
[1] 0.0929
Model Checking
A ﬁtted model must be examined carefully to check for possible model inadequacy.
If the model is adequate, then the residual series should behave as a white noise.
The ACF and the Ljung–Box statistics in Eq. (2.3) of the residuals can be used to
check the closeness of ˆat to a white noise. For an AR(p) model, the Ljung–Box
statistic Q(m) follows asymptotically a chi-squared distribution with m −g degrees
of freedom, where g denotes the number of AR coefﬁcients used in the model. The
adjustment in the degrees of freedom is made based on the number of constraints
added to the residuals ˆat from ﬁtting the AR(p) to an AR(0) model. If a ﬁtted
