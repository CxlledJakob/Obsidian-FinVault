# Analysis of Financial Time Series, Third Edition (Wiley -- Ruey S_ Tsay -- Wiley series in probability and statistics, 3rd ed_, -- John Wiley & Sons, -- isbn13 9780470414354 -- 9f99b80c7b2dedd477f463dc5323f3b6 -- An.pdf — pages 229–248

--- page 229 ---

202
nonlinear models and their applications
For the 2–3–1 network in Figure 4.8, if the output activation function is linear,
then Eq. (4.33) becomes
o = α0o +
3

j=1
wjohj,
where hj is given in Eq. (4.31). The network thus has 13 parameters. If Eq. (4.34)
is used, then the network becomes
o = α0o +
2

i=1
αioxi +
3

j=1
wjohj,
where again hj is given in Eq. (4.31). The number of parameters of the network
increases to 15.
We refer to the function in Eq. (4.33) or (4.34) as a semiparametric function
because its functional form is known, but the number of nodes and their biases and
weights are unknown. The direct connections from the input layer to the output
layer in Eq. (4.34) mean that the network can skip the hidden layer. We refer to
such a network as a skip-layer feed-forward network.
Feed-forward networks are known as multilayer percetrons in the neural network
literature. They can approximate any continuous function uniformly on compact sets
by increasing the number of nodes in the hidden layer; see Hornik, Stinchcombe,
and White (1989), Hornik (1993), and Chen and Chen (1995). This property of neural networks is the universal approximation property of the multilayer percetrons.
In short, feed-forward neural networks with a hidden layer can be seen as a way
to parameterize a general continuous nonlinear function.
Training and Forecasting
Application of neural networks involves two steps. The ﬁrst step is to train the
network (i.e., to build a network, including determining the number of nodes and
estimating their biases and weights). The second step is inference, especially forecasting. The data are often divided into two nonoverlapping subsamples in the
training stage. The ﬁrst subsample is used to estimate the parameters of a given
feed-forward neural network. The network so built is then used in the second subsample to perform forecasting and compute its forecasting accuracy. By comparing
the forecasting performance, one selects the network that outperforms the others
as the “best” network for making inference. This is the idea of cross validation
widely used in statistical model selection. Other model selection methods are also
available.
In a time series application, let {(rt, xt)|t = 1, . . . , T } be the available data for
network training, where xt denotes the vector of inputs and rt is the series of
interest (e.g., log returns of an asset). For a given network, let ot be the output of
--- page 230 ---

nonlinear models
203
the network with input xt; see Eq. (4.34). Training a neural network amounts to
choosing its biases and weights to minimize some ﬁtting criterion—for example,
the least squares
S2 =
T

t=1
(rt −ot)2.
This is a nonlinear estimation problem that can be solved by several iterative methods. To ensure the smoothness of the ﬁtted function, some additional constraints
can be added to the prior minimization problem. In the neural network literature,
the back propagation (BP) learning algorithm is a popular method for network
training. The BP method, introduced by Bryson and Ho (1969), works backward
starting with the output layer and uses a gradient rule to modify the biases and
weights iteratively. Appendix 2A of Ripley (1993) provides a derivation of back
propagation. Once a feed-forward neural network is built, it can be used to compute
forecasts in the forecasting subsample.
Example 4.7.
To illustrate applications of the neural network in ﬁnance, we
consider the monthly log returns, in percentages and including dividends, for IBM
stock from January 1926 to December 1999. We divide the data into two subsamples. The ﬁrst subsample consisting of returns from January 1926 to December
1997 for 864 observations is used for modeling. Using model (4.34) with three
inputs and two nodes in the hidden layer, we obtain a 3–2–1 network for the
series. The three inputs are rt−1, rt−2, and rt−3 and the biases and weights are
given next:
ˆrt = 3.22 −1.81f1(rt−1) −2.28f2(rt−1) −0.09rt−1 −0.05rt−2 −0.12rt−3,
(4.35)
where rt−1 = (rt−1, rt−2, rt−3) and the two logistic functions are
f1(rt−1) =
exp(−8.34 −18.97rt−1 + 2.17rt−2 −19.17rt−3)
1 + exp(−8.34 −18.97rt−1 + 2.17rt−2 −19.17rt−3),
f2(rt−1) =
exp(39.25 −22.17rt−1 −17.34rt−2 −5.98rt−3)
1 + exp(39.25 −22.17rt−1 −17.34rt−2 −5.98rt−3).
The standard error of the residuals for the prior model is 6.56. For comparison, we
also built an AR model for the data and obtained
rt = 1.101 + 0.077rt−1 + at,
σa = 6.61.
(4.36)
The residual standard error is slightly greater than that of the feed-forward model
in Eq. (4.35).
--- page 231 ---

204
nonlinear models and their applications
Forecast Comparison
The monthly returns of IBM stock in 1998 and 1999 form the second subsample and
are used to evaluate the out-of-sample forecasting performance of neural networks.
As a benchmark for comparison, we use the sample mean of rt in the ﬁrst subsample
as the 1-step-ahead forecast for all the monthly returns in the second subsample.
This corresponds to assuming that the log monthly price of IBM stock follows a
random walk with drift. The mean squared forecast error (MSFE) of this benchmark
model is 91.85. For the AR(1) model in Eq. (4.36), the MSFE of 1-step-ahead
forecasts is 91.70. Thus, the AR(1) model slightly outperforms the benchmark.
For the 3–2–1 feed-forward network in Eq. (4.35), the MSFE is 91.74, which is
essentially the same as that of the AR(1) model.
Remark.
The estimation of feed-forward networks is done by using the nnet
package of S-Plus with default starting weights; see Venables and Ripley (1999)
for more information. Our limited experience shows that the estimation results
vary. For the IBM stock returns used in Example 4.7, the out-of-sample MSE for
a 3–2–1 network can be as low as 89.46 and as high as 93.65. If we change the
number of nodes in the hidden layer, the range for the MSE becomes even wider.
The S-Plus commands used in Example 4.7 are given in Appendix B.
□
Example 4.8.
Nice features of the feed-forward network include its ﬂexibility
and wide applicability. For illustration, we use the network with a Heaviside activation function for the output layer to forecast the direction of price movement for
IBM stock considered in Example 4.7. Deﬁne a direction variable as
dt =

1
if rt ≥0,
0
if rt < 0.
We use eight input nodes consisting of the ﬁrst four lagged values of both rt and
dt and four nodes in the hidden layer to build an 8–4–1 feed-forward network
for dt in the ﬁrst subsample. The resulting network is then used to compute the
1-step-ahead probability of an “upward movement” (i.e., a positive return) for the
following month in the second subsample. Figure 4.9 shows a typical output of
probability forecasts and the actual directions in the second subsample with the
latter denoted by circles. A horizontal line of 0.5 is added to the plot. If we take a
rigid approach by letting ˆdt = 1 if the probability forecast is greater than or equal to
0.5 and ˆdt = 0 otherwise, then the neural network has a successful rate of 0.58. The
success rate of the network varies substantially from one estimation to another, and
the network uses 49 parameters. To gain more insight, we did a simulation study of
running the 8–4–1 feed-forward network 500 times and computed the number of
errors in predicting the upward and downward movement using the same method
as before. The mean and median of errors over the 500 runs are 11.28 and 11,
respectively, whereas the maximum and minimum number of errors are 18 and 4.
--- page 232 ---

nonlinearity tests
205
Month
Probability
1998.5
1999.0
1999.5
2000.0
0.0
0.2
0.4
0.6
0.8
1.0
o
o
o
o
o
o
o
o
o
o
o
o
o
o
o
o
o
o
o
o
o
o
o
o
Figure 4.9
One-step-ahead probability forecasts for positive monthly return for IBM stock using an
8–4–1 feed-forward neural network. Forecasting period is from January 1998 to December 1999.
For comparison, we also did a simulation with 500 runs using a random walk with
drift—that is,
ˆdt =

1
if ˆrt = 1.19 + ϵt ≥0,
0
otherwise,
where 1.19 is the average monthly log return for IBM stock from January 1926 to
December 1997 and {ϵt} is a sequence of iid N(0, 1) random variables. The mean
and median of the number of forecast errors become 10.53 and 11, whereas the
maximum and minimum number of errors are 17 and 5, respectively. Figure 4.10
shows the histograms of the number of forecast errors for the two simulations. The
results show that the 8–4–1 feed-forward neural network does not outperform the
simple model that assumes a random walk with drift for the monthly log price of
IBM stock.
4.2
NONLINEARITY TESTS
In this section, we discuss some nonlinearity tests available in the literature that
have decent power against the nonlinear models considered in Section 4.1. The tests
discussed include both parametric and nonparametric statistics. The Ljung–Box
--- page 233 ---

206
nonlinear models and their applications
4
6
8
10
12
14
16
18
0
50
100
150
Neural network
6
8
10
12
14
16
0
20
40
60
80
100
120
Random walk with a drift
Figure 4.10
Histograms of number of forecasting errors for directional movements of monthly log
returns of IBM stock. Forecasting period is from January 1998 to December 1999.
statistics of squared residuals, the bispectral test, and the Brock, Dechert, and
Scheinkman (BDS) test are nonparametric methods. The RESET test (Ramsey,
1969), the F tests of Tsay (1986, 1989), and other Lagrange multiplier and likelihood ratio tests depend on speciﬁc parametric functions. Because nonlinearity
may occur in many ways, there exists no single test that dominates the others in
detecting nonlinearity.
4.2.1
Nonparametric Tests
Under the null hypothesis of linearity, residuals of a properly speciﬁed linear model
should be independent. Any violation of independence in the residuals indicates
inadequacy of the entertained model, including the linearity assumption. This is
the basic idea behind various nonlinearity tests. In particular, some of the nonlinearity tests are designed to check for possible violation in quadratic forms of the
underlying time series.
Q-Statistic of Squared Residuals
McLeod and Li (1983) apply the Ljung–Box statistics to the squared residuals of
an ARMA(p, q) model to check for model inadequacy. The test statistic is
Q(m) = T (T + 2)
m

i=1
ˆρ2
i (a2
t )
T −i ,
--- page 234 ---

nonlinearity tests
207
where T is the sample size, m is a properly chosen number of autocorrelations
used in the test, at denotes the residual series, and ˆρi(a2
t ) is the lag-i ACF of a2
t .
If the entertained linear model is adequate, Q(m) is asymptotically a chi-squared
random variable with m −p −q degrees of freedom. As mentioned in Chapter
3, the prior Q-statistic is useful in detecting conditional heteroscedasticity of at
and is asymptotically equivalent to the Lagrange multiplier test statistic of Engle
(1982) for ARCH models; see Section 3.4.3. The null hypothesis of the test is
H0 : β1 = · · · = βm = 0, where βi is the coefﬁcient of a2
t−i in the linear regression
a2
t = β0 + β1a2
t−1 + · · · + βma2
t−m + et
for t = m + 1, . . . , T . Because the statistic is computed from residuals (not directly
from the observed returns), the number of degrees of freedom is m −p −q.
Bispectral Test
This test can be used to test for linearity and Gaussianity. It depends on the result
that a properly normalized bispectrum of a linear time series is constant over all
frequencies and that the constant is zero under normality. The bispectrum of a time
series is the Fourier transform of its third-order moments. For a stationary time
series xt in Eq. (4.1), the third-order moment is deﬁned as
c(u, v) = g
∞

k=−∞
ψkψk+uψk+v,
(4.37)
where u and v are integers, g = E(a3
t ), ψ0 = 1, and ψk = 0 for k < 0. Taking
Fourier transforms of Eq. (4.37), we have
b3(w1, w2) =
g
4π2 [−(w1 + w2)](w1)(w2),
(4.38)
where (w) = ∞
u=0 ψu exp(−iwu) with i =
√
−1, and wi are frequencies. Yet
the spectral density function of xt is given by
p(w) = σ 2
a
2π |(w)|2,
where w denotes the frequency. Consequently, the function
b(w1, w2) =
|b3(w1, w2)|2
p(w1)p(w2)p(w1 + w2) = constant for all (w1, w2).
(4.39)
The bispectrum test makes use of the property in Eq. (4.39). Basically, it estimates
the function b(w1, w2) in Eq. (4.39) over a suitably chosen grid of points and
applies a test statistic similar to Hotelling’s T 2 statistic to check the constancy of
b(w1, w2). For a linear Gaussian series, E(a3
t ) = g = 0 so that the bispectrum is
zero for all frequencies (w1, w2). For further details of the bispectral test, see Priestley (1988), Subba Rao and Gabr (1984), and Hinich (1982). Limited experience
shows that the test has decent power when the sample size is large.
--- page 235 ---

208
nonlinear models and their applications
BDS Statistic
Brock, Dechert, and Scheinkman (1987) propose a test statistic, commonly referred
to as the BDS test, to detect the iid assumption of a time series. The statistic is,
therefore, different from other test statistics discussed because the latter mainly
focus on either the secondor third-order properties of xt. The basic idea of the
BDS test is to make use of a “correlation integral” popular in chaotic time series
analysis. Given a k-dimensional time series Xt and observations {Xt}Tk
t=1, deﬁne
the correlation integral as
Ck(δ) = lim
Tk→∞
2
Tk(Tk −1)

i<j
Iδ(Xi, Xj),
(4.40)
where Iδ(u, v) is an indicator variable that equals one if ∥u −v∥< δ, and zero
otherwise, where ∥· ∥is the supnorm. The correlation integral measures the fraction
of data pairs of {Xt} that are within a distance of δ from each other. Consider
next a time series xt. Construct k-dimensional vectors Xk
t = (xt, xt+1, . . . , xt+k−1)′,
which are called k histories. The idea of the BDS test is as follows. Treat a k
history as a point in the k-dimensional space. If {xt}T
t=1 are indeed iid random
variables, then the k-histories {Xt}Tk
t=1 should show no pattern in the k-dimensional
space. Consequently, the correlation integrals should satisfy the relation Ck(δ) =
[C1(δ)]k. Any departure from the prior relation suggests that xt are not iid. As
a simple, but informative example, consider a sequence of iid random variables
from the uniform distribution over [0, 1]. Let [a, b] be a subinterval of [0, 1] and
consider the “2-history” (xt, xt+1), which represents a point in the two-dimensional
space. Under the iid assumption, the expected number of 2-histories in the subspace
[a, b] × [a, b] should equal the square of the expected number of xt in [a, b]. This
idea can be formally examined by using sample counterparts of correlation integrals.
Deﬁne
Cℓ(δ, T ) =
2
Tk(Tk −1)

i<j
Iδ(X∗
i , X∗
j),
ℓ= 1, k,
where Tℓ= T −ℓ+ 1 and X∗
i = xi if ℓ= 1 and X∗
i = Xk
i if ℓ= k. Under the
null hypothesis that {xt} are iid with a nondegenerated distribution function F(·),
Brock, Dechert, and Scheinkman (1987) show that
Ck(δ, T ) →[C1(δ)]k
with probability 1,
as
T →∞
for any ﬁxed k and δ. Furthermore, the statistic
√
T {Ck(δ, T ) −[C1(δ, T )]k} is
asymptotically distributed as normal with mean zero and variance:
σ 2
k (δ) = 4

Nk + 2
k−1

j=1
Nk−jC2j + (k −1)2C2k −k2NC2k−2

,
--- page 236 ---

nonlinearity tests
209
where
C =

[F(z + δ) −F(z −δ)] dF(z)
and
N =

[F(z + δ) −F(z −δ)]2
dF(z). Note that C1(δ, T ) is a consistent estimate of C, and N can be consistently
estimated by
N(δ, T ) =
6
Tk(Tk −1)(Tk −2)

t<s<u
Iδ(xt, xs)Iδ(xs, xu).
The BDS test statistic is then deﬁned as
Dk(δ, T ) =
√
T {Ck(δ, T ) −[C1(δ, T )]k}
σk(δ, T )
,
(4.41)
where σk(δ, T ) is obtained from σk(δ) when C and N are replaced by C1(δ, T ) and
N(δ, T ), respectively. This test statistic has a standard normal limiting distribution.
For further discussion and examples of applying the BDS test, see Hsieh (1989)
and Brock, Hsieh, and LeBaron (1991). In application, one should remove linear
dependence, if any, from the data before applying the BDS test. The test may be
sensitive to the choices of δ and k, especially when k is large.
4.2.2
Parametric Tests
Turning to parametric tests, we consider the RESET test of Ramsey (1969) and its
generalizations. We also discuss some test statistics for detecting threshold nonlinearity. To simplify the notation, we use vectors and matrices in the discussion.
If necessary, readers may consult Appendix A of Chapter 8 for a brief review on
vectors and matrices.
The RESET Test
Ramsey (1969) proposes a speciﬁcation test for linear least-squares regression analysis. The test is referred to as a RESET test and is readily applicable to linear AR
models. Consider the linear AR(p) model
xt = X′
t−1φ + at,
(4.42)
where Xt−1 = (1, xt−1, . . . , xt−p)′ and φ = (φ0, φ1, . . . , φp)′. The ﬁrst step of the
RESET test is to obtain the least-squares estimate φ of Eq. (4.42) and compute
the ﬁt ˆxt = X′
t−1φ, the residual ˆat = xt −ˆxt, and the sum of squared residuals
SSR0 = T
t=p+1 ˆa2
t , where T is the sample size. In the second step, consider the
linear regression
ˆat = X′
t−1α1 + M′
t−1α2 + vt,
(4.43)
where Mt−1 = (ˆx2
t , . . . , ˆxs+1
t
)′ for some s ≥1, and compute the least-squares residuals
ˆvt = ˆat −X′
t−1α1 −M′
t−1α2
--- page 237 ---

210
nonlinear models and their applications
and the sum of squared residuals SSR1 = T
t=p+1 ˆv2
t of the regression. The basic
idea of the RESET test is that if the linear AR(p) model in Eq. (4.42) is adequate,
then α1 and α2 of Eq. (4.43) should be zero. This can be tested by the usual F
statistic of Eq. (4.43) given by
F = (SSR0 −SSR1)/g
SSR1/(T −p −g)
with
g = s + p + 1,
(4.44)
which, under the linearity and normality assumption, has an F distribution with
degrees of freedom g and T −p −g.
Remark.
Because
ˆxk
t
for k = 2, . . . , s + 1 tend to be highly correlated
with Xt−1 and among themselves, principal components of Mt−1 that are not
co-linear with Xt−1 are often used in ﬁtting Eq. (4.43). Principal component
analysis is a statistical tool for dimension reduction; see Chapter 8 for more
information.
□
Keenan (1985) proposes a nonlinearity test for time series that uses ˆx2
t only and
modiﬁes the second step of the RESET test to avoid multicollinearity between ˆx2
t
and Xt−1. Speciﬁcally, the linear regression (4.43) is divided into two steps. In
step 2(a), one removes linear dependence of ˆx2
t on Xt−1 by ﬁtting the regression
ˆx2
t = X′
t−1β + ut
and obtaining the residual ˆut = ˆx2
t −Xt−1β. In step 2(b), consider the linear regression
ˆat = ˆutα + vt,
and obtain the sum of squared residuals SSR1 = T
t=p+1(ˆat −ˆut ˆα)2 = T
t=p+1 ˆv2
t
to test the null hypothesis α = 0.
The F Test
To improve the power of Keenan’s test and the RESET test, Tsay (1986) uses a
different choice of the regressor Mt−1. Speciﬁcally, he suggests using Mt−1 =
vech(Xt−1X′
t−1), where vech(A) denotes the half-stacking vector of the matrix
A using elements on and below the diagonal only; see Appendix B of Chapter 8
for more information about the operator. For example, if p = 2, then Mt−1 =
(x2
t−1, xt−1xt−2, x2
t−2)′. The dimension of Mt−1 is p(p + 1)/2 for an AR(p) model.
In practice, the test is simply the usual partial F statistic for testing α = 0 in the
linear least-squares regression
xt = X′
t−1φ + M′
t−1α + et,
where et denotes the error term. Under the assumption that xt is a linear AR(p)
process, the partial F statistic follows an F distribution with degrees of freedom
--- page 238 ---

nonlinearity tests
211
g and T −p −g −1, where g = p(p + 1)/2. We refer to this F test as the Ori-
F test. Luukkonen, Saikkonen, and Ter¨asvirta (1988) further extend the test by
augmenting Mt−1 with cubic terms x3
t−i for i = 1, . . . , p.
Threshold Test
When the alternative model under study is a SETAR model, one can derive speciﬁc
test statistics to increase the power of the test. One of the speciﬁc tests is the
likelihood ratio statistic. This test, however, encounters the difﬁculty of undeﬁned
parameters under the null hypothesis of linearity because the threshold is undeﬁned
for a linear AR process. Another speciﬁc test seeks to transform testing threshold
nonlinearity into detecting model changes. It is then interesting to discuss the
differences between these two speciﬁc tests for threshold nonlinearity.
To simplify the discussion, let us consider the simple case that the alternative model is a 2-regime SETAR model with threshold variable xt−d. The null
hypothesis H0: xt follows the linear AR(p) model
xt = φ0 +
p

i=1
φixt−i + at,
(4.45)
whereas the alternative hypothesis Ha: xt follows the SETAR model
xt =

φ(1)
0
+ p
i=1 φ(1)
i xt−i + a1t
if xt−d < r1,
φ(2)
0
+ p
i=1 φ(2)
i xt−i + a2t
if xt−d ≥r1,
(4.46)
where r1 is the threshold. For a given realization {xt}T
t=1 and assuming normality,
let l0( ˆφ, ˆσ 2
a ) be the log-likelihood function evaluated at the maximum-likelihood
estimates of φ = (φ0, . . . , φp)′ and σ 2
a . This is easy to compute. The likelihood
function under the alternative is also easy to compute if the threshold r1 is given.
Let l1(r1; ˆφ1, ˆσ 2
1 ; ˆφ2, ˆσ 2
2 ) be the log-likelihood function evaluated at the maximumlikelihood estimates of φi = (φ(i)
0 , . . . , φ(i)
p )′ and σ 2
i conditioned on knowing the
threshold r1. The log-likelihood ratio l(r1) deﬁned as
l(r1) = l1(r1; ˆφ1, ˆσ 2
1 ; ˆφ2, ˆσ 2
2 ) −l0( ˆφ, ˆσ 2
a )
is then a function of the threshold r1, which is unknown. Yet under the null hypothesis, there is no threshold and r1 is not deﬁned. The parameter r1 is referred to
as a nuisance parameter under the null hypothesis. Consequently, the asymptotic
distribution of the likelihood ratio is very different from that of the conventional
likelihood ratio statistics. See Chan (1991) for further details and critical values of
the test. A common approach is to use lmax = supv<r1<u l(r1) as the test statistic,
where v and u are prespeciﬁed lower and upper bounds of the threshold. Davis
(1987) and Andrews and Ploberger (1994) provide further discussion on hypothesis
testing involving nuisance parameters under the null hypothesis. Simulation is often
used to obtain empirical critical values of the test statistic lmax, which depends on
--- page 239 ---

212
nonlinear models and their applications
the choices of v and u. The average of l(r1) over r1 ∈[v, u] is also considered by
Andrews and Ploberger as a test statistic.
Tsay (1989) makes use of arranged autoregression and recursive estimation to
derive an alternative test for threshold nonlinearity. The arranged autoregression
seeks to transfer the SETAR model under the alternative hypothesis Ha into a model
change problem with the threshold r1 serving as the change point. To see this, the
SETAR model in Eq. (4.46) says that xt follows essentially two linear models
depending on whether xt−d < r1 or xt−d ≥r1. For a realization {xt}T
t=1, xt−d can
assume values {x1, . . . , xT −d}. Let x(1) ≤x(2) ≤· · · ≤x(T −d) be the ordered statistics of {xt}T −d
t=1 (i.e., arranging the observations in increasing order). The SETAR
model can then be written as
x(j)+d = β0 +
p

i=1
βix(j)+d−i + a(j)+d,
j = 1, . . . , T −d,
(4.47)
where βi = φ(1)
i
if x(j) < r1 and βi = φ(2)
i
if x(j) ≥r1. Consequently, the threshold
r1 is a change point for the linear regression in Eq. (4.47), and we refer to Eq. (4.47)
as an arranged autoregression (in increasing order of the threshold xt−d). Note that
the arranged autoregression in (4.47) does not alter the dynamic dependence of xt
on xt−i for i = 1, . . . , p because x(j)+d still depends on x(j)+d−i for i = 1, . . . , p.
What is done is simply to present the SETAR model in the threshold space instead
of in the time space. That is, the equation with a smaller xt−d appears before that
with a larger xt−d. The threshold test of Tsay (1989) is obtained as follows.
• Step 1. Fit Eq. (4.47) using j = 1, . . . , m, where m is a prespeciﬁed positive
integer (e.g., 30). Denote the least-squares estimates of βi by ˆβi,m, where m
denotes the number of data points used in estimation.
• Step 2. Compute the predictive residual
ˆa(m+1)+d = x(m+1)+d −ˆβ0,m −
p

i=1
ˆβi,mx(m+1)+d−i
and its standard error. Let ˆe(m+1)+d be the standardized predictive residual.
• Step 3. Use the recursive least-squares method to update the least-squares
estimates to ˆβi,m+1 by incorporating the new data point x(m+1)+d.
• Step 4. Repeat steps 2 and 3 until all data points are processed.
• Step 5. Consider the linear regression of the standardized predictive residual
ˆe(m+j)+d = α0 +
p

i=1
αix(m+j)+d−i + vt,
j = 1, . . . , T −d −m (4.48)
and compute the usual F statistic for testing αi = 0 in Eq. (4.48) for i =
0, . . . , p. Under the null hypothesis that xt follows a linear AR(p) model,
--- page 240 ---

nonlinearity tests
213
the F ratio has a limiting F distribution with degrees of freedom p + 1 and
T −d −m −p.
We refer to the earlier F test as a TAR-F test. The idea behind the test is that
under the null hypothesis there is no model change in the arranged autoregression
in Eq. (4.47) so that the standardized predictive residuals should be close to iid
with mean zero and variance 1. In this case, they should have no correlations with
the regressors x(m+j)+d−i. For further details including formulas for a recursive
least-squares method and some simulation study on performance of the TAR-F
test, see Tsay (1989). The TAR-F test avoids the problem of nuisance parameters
encountered by the likelihood ratio test. It does not require knowing the threshold
r1. It simply tests that the predictive residuals have no correlations with regressors
if the null hypothesis holds. Therefore, the test does not depend on knowing the
number of regimes in the alternative model. Yet the TAR-F test is not as powerful
as the likelihood ratio test if the true model is indeed a 2-regime SETAR model
with a known innovational distribution.
4.2.3
Applications
In this subsection, we apply some of the nonlinearity tests discussed previously to
ﬁve time series. For a real ﬁnancial time series, an AR model is used to remove
any serial correlation in the data, and the tests apply to the residual series of the
model. The ﬁve series employed are as follows:
1. r1t: A simulated series of iid N(0, 1) with 500 observations.
2. r2t: A simulated series of iid Student-t distribution with 6 degrees of freedom.
The sample size is 500.
3. a3t: The residual series of monthly log returns of CRSP equal-weighted index
from 1926 to 1997 with 864 observations. The linear AR model used is
(1 −0.180B + 0.099B3 −0.105B9)r3t = 0.0086 + a3t.
4. a4t: The residual series of monthly log returns of CRSP value-weighted index
from 1926 to 1997 with 864 observations. The linear AR model used is
(1 −0.098B + 0.111B3 −0.088B5)r4t = 0.0078 + a4t.
5. a5t: The residual series of monthly log returns of IBM stock from 1926 to
1997 with 864 observations. The linear AR model used is
(1 −0.077B)r5t = 0.011 + a5t.
Table 4.2 shows the results of the nonlinearity test. For the simulated series and
IBM returns, the F tests are based on an AR(6) model. For the index returns, the
--- page 241 ---

214
nonlinear models and their applications
TABLE 4.2
Nonlinearity Tests for Simulated Series and Some Log Stock Returnsa
Q
Q
BDS(δ = 1.5ˆσa)
Data
(5)
(10)
2
3
4
5
N(0,1)
3.2
6.5
−0.32
−0.14
−0.15
−0.33
t6
0.9
1.7
−0.87
−1.18
−1.56
−1.71
ln(ew)
2.9
4.9
9.94
11.72
12.83
13.65
ln(vw)
1.0
9.8
8.61
9.88
10.70
11.29
ln(ibm)
0.6
7.1
4.96
6.09
6.68
6.82
d = 1
BDS(δ = ˆσa)
Data
Ori-F
TAR-F
2
3
4
5
N(0,1)
1.13
0.87
−0.77
−0.71
−1.04
−1.27
t6
0.69
0.81
−0.35
−0.76
−1.25
−1.49
ln(ew)
5.05
6.77
10.01
11.85
13.14
14.45
ln(vw)
4.95
6.85
7.01
7.83
8.64
9.53
ln(ibm)
1.32
1.51
3.82
4.70
5.45
5.72
aThe sample size of simulated series is 500 and that of stock returns is 864. The BDS test uses
k = 2, . . . , 5.
AR order is the same as the model given earlier. For the BDS test, we chose δ =
ˆσa and δ = 1.5ˆσa with k = 2, . . . , 5. Also given in the table are the Ljung–Box
statistics that conﬁrm no serial correlation in the residual series before applying
nonlinearity tests. Compared with their asymptotic critical values, the BDS test and
F tests are insigniﬁcant at the 5% level for the simulated series. However, the BDS
tests are highly signiﬁcant for the real ﬁnancial time series. The F tests also show
signiﬁcant results for the index returns, but they fail to suggest nonlinearity in the
IBM log returns. In summary, the tests conﬁrm that the simulated series are linear
and suggest that the stock returns are nonlinear.
4.3
MODELING
Nonlinear time series modeling necessarily involves subjective judgment. However,
there are some general guidelines to follow. It starts with building an adequate linear model on which nonlinearity tests are based. For ﬁnancial time series, the
Ljung–Box statistics and Engle’s test are commonly used to detect conditional
heteroscedasticity. For general series, other tests of Section 4.2 apply. If nonlinearity is statistically signiﬁcant, then one chooses a class of nonlinear models to
entertain. The selection here may depend on the experience of the analyst and the
substantive matter of the problem under study. For volatility models, the order
of an ARCH process can often be determined by checking the partial autocorrelation function of the squared series. For GARCH and EGARCH models, only
lower orders such as (1,1), (1,2), and (2,1) are considered in most applications.
--- page 242 ---

forecasting
215
Higher order models are hard to estimate and understand. For TAR models, one
may use the procedures given in Tong (1990) and Tsay (1989, 1998) to build an
adequate model. When the sample size is sufﬁciently large, one may apply nonparametric techniques to explore the nonlinear feature of the data and choose a
proper nonlinear model accordingly; see Chen and Tsay (1993a) and Cai, Fan, and
Yao (2000). The MARS procedure of Lewis and Stevens (1991) can also be used
to explore the dynamic structure of the data. Finally, information criteria such as
the Akaike information criterion (Akaike, 1974) and the generalized odd ratios in
Chen, McCulloch, and Tsay (1997) can be used to discriminate between competing
nonlinear models. The chosen model should be carefully checked before it is used
for prediction.
4.4
FORECASTING
Unlike the linear model, there exist no closed-form formulas to compute forecasts
of most nonlinear models when the forecast horizon is greater than 1. We use
parametric bootstraps to compute nonlinear forecasts. It is understood that the model
used in forecasting has been rigorously checked and is judged to be adequate for the
series under study. By a model, we mean the dynamic structure and innovational
distributions. In some cases, we may treat the estimated parameters as given.
4.4.1
Parametric Bootstrap
Let T be the forecast origin and ℓbe the forecast horizon (ℓ> 0). That is, we
are at time index T and interested in forecasting xT +ℓ. The parametric bootstrap
considered computes realizations xT +1, . . . , XT +ℓsequentially by (a) drawing a
new innovation from the speciﬁed innovational distribution of the model, and (b)
computing xT +i using the model, data, and previous forecasts xT +1, . . . , xT +i−1.
This results in a realization for xT +ℓ. The procedure is repeated M times to obtain
M realizations of xT +ℓdenoted by {x(j)
T +ℓ}M
j=1. The point forecast of xT +ℓis then
the sample average of x(j)
T +ℓ. Let the forecast be xT (ℓ). We used M = 3000 in
some applications and the results seem ﬁne. The realizations {x(j)
T +ℓ}M
j=1 can also
be used to obtain an empirical distribution of xT +ℓ. We make use of this empirical
distribution later to evaluate forecasting performance.
4.4.2
Forecasting Evaluation
There are many ways to evaluate the forecasting performance of a model, ranging
from directional measures to magnitude measures to distributional measures. A
directional measure considers the future direction (up or down) implied by the
model. Predicting that tomorrow’s S&P 500 index will go up or down is an example
of directional forecasts that are of practical interest. Predicting the year-end value
of the daily S&P 500 index belongs to the case of magnitude measure. Finally,
--- page 243 ---

216
nonlinear models and their applications
assessing the likelihood that the daily S&P 500 index will go up 10% or more
between now and the year end requires knowing the future conditional probability
distribution of the index. Evaluating the accuracy of such an assessment needs a
distributional measure.
In practice, the available data set is divided into two subsamples. The ﬁrst subsample of the data is used to build a nonlinear model, and the second subsample
is used to evaluate the forecasting performance of the model. We refer to the
two subsamples of data as estimation and forecasting subsamples. In some studies, a rolling forecasting procedure is used in which a new data point is moved
from the forecasting subsample into the estimation subsample as the forecast origin
advances. In what follows, we brieﬂy discuss some measures of forecasting performance that are commonly used in the literature. Keep in mind, however, that there
exists no widely accepted single measure to compare models. A utility function
based on the objective of the forecast might be needed to better understand the
comparison.
Directional Measure
A typical measure here is to use a 2 × 2 contingency table that summarizes the
number of “hits” and “misses” of the model in predicting ups and downs of xT +ℓ
in the forecasting subsample. Speciﬁcally, the contingency table is given as
Actual
Predicted
Up
Down
Up
m11
m12
m10
Down
m21
m22
m20
m01
m02
m
where m is the total number of ℓ-step-ahead forecasts in the forecasting subsample,
m11 is the number of “hits” in predicting upward movements, m21 is the number
of “misses” in predicting downward movements of the market, and so on. Larger
values in m11 and m22 indicate better forecasts. The test statistic
χ2 =
2

i=1
2

j=1
(mij −mi0m0j/m)2
mi0m0j/m
can then be used to evaluate the performance of the model. A large χ2 signiﬁes that
the model outperforms the chance of random choice. Under some mild conditions,
χ2 has an asymptotic chi-squared distribution with 1 degree of freedom. For further
discussion of this measure, see Dahl and Hylleberg (1999).
For illustration of the directional measure, consider the 1-step-ahead probability
forecasts of the 8–4–1 feed-forward neural network shown in Figure 4.9. The
2 × 2 table of “hits” and “misses” of the network is
--- page 244 ---

forecasting
217
Actual
Predicted
Up
Down
Up
12
2
14
Down
8
2
10
20
4
24
The table shows that the network predicts the upward movement well, but fares
poorly in forecasting the downward movement of the stock. The chi-squared statistic of the table is 0.137 with a p value of 0.71. Consequently, the network does
not signiﬁcantly outperform a random-walk model with equal probabilities for
“upward” and “downward” movements.
Magnitude Measure
Three statistics are commonly used to measure performance of point forecasts. They
are the mean squared error (MSE), mean absolute deviation (MAD), and mean
absolute percentage error (MAPE). For ℓ-step-ahead forecasts, these measures are
deﬁned as
MSE(ℓ) = 1
m
m−1

j=0
[xT +ℓ+j −xT +j(ℓ)]2,
(4.49)
MAD(ℓ) = 1
m
m−1

j=0
|xT +ℓ+j −xT +j(ℓ)|,
(4.50)
MAPE(ℓ) = 1
m
m−1

j=0
| xT +j(ℓ)
xT +j+ℓ
−1 |,
(4.51)
where m is the number of ℓ-step-ahead forecasts available in the forecasting
subsample. In application, one often chooses one of the above three measures, and
the model with the smallest magnitude on that measure is regarded as the best ℓ-
step-ahead forecasting model. It is possible that different ℓmay result in selecting
different models. The measures also have other limitations in model comparison;
see, for instance, Clements and Hendry (1993).
Distributional Measure
Practitioners recently began to assess forecasting performance of a model using
its predictive distributions. Strictly speaking, a predictive distribution incorporates
parameter uncertainty in forecasts. We call it conditional predictive distribution if
the parameters are treated as ﬁxed. The empirical distribution of xT +ℓobtained
by the parametric bootstrap is a conditional predictive distribution. This empirical
distribution is often used to compute a distributional measure. Let uT (ℓ) be the
percentile of the observed xT +ℓin the prior empirical distribution. We then have
--- page 245 ---

218
nonlinear models and their applications
a set of m percentiles {uT +j(ℓ)}m−1
j=0 , where again m is the number of ℓ-stepahead forecasts in the forecasting subsample. If the model entertained is adequate,
{uT +j(ℓ)} should be a random sample from the uniform distribution on [0, 1].
For a sufﬁciently large m, one can compute the Kolmogorov–Smirnov statistic of
{uT +j(ℓ)} with respect to uniform [0, 1]. The statistic can be used for both model
checking and forecasting comparison.
4.5
APPLICATION
In this section, we illustrate nonlinear time series models by analyzing the quarterly
U.S. civilian unemployment rate, seasonally adjusted, from 1948 to 1993. This
series was analyzed in detail by Montgomery et al. (1998). We repeat some of
the analyses here using nonlinear models. Figure 4.11 shows the time plot of
the data. Well-known characteristics of the series include that (a) it tends to move
countercyclically with U.S. business cycles, and (b) the rate rises quickly but decays
slowly. The latter characteristic suggests that the dynamic structure of the series is
nonlinear.
Denote the series by xt and let
xt = xt −xt−1 be the change in unemployment
rate. The linear model
(1 −0.31B4)(1 −0.65B)
xt = (1 −0.78B4)at,
ˆσ 2
a = 0.090
(4.52)
••••
•
•
••
•
•
•
•
•
•••
•••
••••
•
•
••
•
•
•
•••••••••
•
•
••
•
•
••
•
••
•
•
•••
•
••••••••••••••
••••••••••••••••••
•
•
•
•••••••••
••••
••
•
•
•
•
••
•••••
•••
•
•••••••
•
•
•••••
•
•
•
•
•
••
•
•
•
••••••••••••
•••••••••••••
•
•
••••••••
••••
Year
Unemployment rate
1950
1960
1970
1980
1990
4
6
8
10
Figure 4.11
Time plot of U.S. quarterly unemployment rate, seasonally adjusted, from 1948 to 1993.
--- page 246 ---

application
219
was built by Montgomery et al. (1998), where the standard errors of the three
coefﬁcients are 0.11, 0.06, and 0.07, respectively. This is a seasonal model even
though the data were seasonally adjusted. It indicates that the seasonal adjustment
procedure used did not successfully remove the seasonality. This model is used as
a benchmark model for forecasting comparison.
To test for nonlinearity, we apply some of the nonlinearity tests of Section 4.2
with an AR(5) model for the differenced series
xt. The results are given
in Table 4.3. All of the tests reject the linearity assumption. In fact, the
linearity assumption is rejected for all AR(p) models we applied, where p = 2,
. . . , 10.
Using a modeling procedure similar to that of Tsay (1989), Montgomery et al.
(1998) build the following TAR model for the
xt series:

xt =

0.01 + 0.73
xt−1 + 0.10
xt−2 + a1t
if
xt−2 ≤0.1,
0.18 + 0.80
xt−1 −0.56
xt−2 + a2t
otherwise.
(4.53)
The sample variances of a1t and a2t are 0.76 and 0.165, respectively, the standard
errors of the three coefﬁcients of regime 1 are 0.03, 0.10, and 0.12, respectively,
and those of regime 2 are 0.09, 0.1, and 0.16. This model says that the change in the
U.S. quarterly unemployment rate,
xt, behaves like a piecewise linear model in
the reference space of xt−2 −xt−3 with threshold 0.1. Intuitively, the model implies
that the dynamics of unemployment act differently depending on the recent change
in the unemployment rate. In the ﬁrst regime, the unemployment rate has had either
a decrease or a minor increase. Here the economy should be stable, and essentially
the change in the rate follows a simple AR(1) model because the lag-2 coefﬁcient is
insigniﬁcant. In the second regime, there is a substantial jump in the unemployment
rate (0.1 or larger). This typically corresponds to the contraction phase in the
business cycle. It is also the period during which government interventions and
industrial restructuring are likely to occur. Here
xt follows an AR(2) model with a
positive constant, indicating an upward trend in xt. The AR(2) polynomial contains
two complex characteristic roots, which indicate possible cyclical behavior in
xt.
Consequently, the chance of having a turning point in xt increases, suggesting
that the period of large increases in xt should be short. This implies that the
contraction phases in the U.S. economy tend to be shorter than the expansion
phases.
TABLE 4.3
Nonlinearity Test for Changes in the U.S. Quarterly Unemployment
Rate: 1948.II–1993.IVa
Type
Ori-F
LST
TAR(1)
TAR(2)
TAR(3)
TAR(4)
Test
2.80
2.83
2.41
2.16
2.84
2.98
p Value
.0007
.0002
.0298
.0500
.0121
.0088
aAn AR(5) model was used in the tests, where LST denotes the test of Luukkonen et al. (1988) and
TAR(d) means threshold test with delay d.
--- page 247 ---

220
nonlinear models and their applications
Applying a Markov chain Monte Carlo method, Montgomery et al. (1998) obtain
the following Markov switching model for
xt:

xt =

−0.07 + 0.38
xt−1 −0.05
xt−2 + ϵ1t
if st = 1,
0.16 + 0.86
xt−1 −0.38
xt−2 + ϵ2t
if st = 2.
(4.54)
The conditional means of
xt are −0.10 for st = 1 and 0.31 for st = 2. Thus, the
ﬁrst state represents the expansionary periods in the economy, and the second state
represents the contractions. The sample variances of ϵ1t and ϵ2t are 0.031 and 0.192,
respectively. The standard errors of the three parameters in state st = 1 are 0.03,
0.14, and 0.11, and those of state st = 2 are 0.04, 0.13, and 0.14, respectively. The
state transition probabilities are P (st = 2|st−1 = 1) = 0.084(0.060) and P (st =
1|st−1 = 2) = 0.126(0.053), where the number in parentheses is the corresponding
standard error. This model implies that in the second state the unemployment rate xt
has an upward trend with an AR(2) polynomial possessing complex characteristic
roots. This feature of the model is similar to the second regime of the TAR model
in Eq. (4.53). In the ﬁrst state, the unemployment rate xt has a slightly decreasing
trend with a much weaker autoregressive structure.
Forecasting Performance
A rolling procedure was used by Montgomery et al. (1998) to forecast the unemployment rate xt. The procedure works as follows:
1. Begin with forecast origin T = 83, corresponding to 1968.II, which was used
in the literature to monitor the performance of various econometric models in
forecasting unemployment rate. Estimate the linear, TAR, and MSA models
using the data from 1948.I to the forecast origin (inclusive).
2. Perform 1-quarter to 5-quarter ahead forecasts and compute the forecast errors
of each model. Forecasts of nonlinear models used are computed by using
the parametric bootstrap method of Section 4.4.
3. Advance the forecast origin by 1 and repeat the estimation and forecasting
processes until all data are employed.
4. Use MSE and mean forecast error to compare performance of the models.
Table 4.4 shows the relative MSE of forecasts and mean forecast errors for the
linear model in Eq. (4.52), the TAR model in Eq. (4.53), and the MSA model in
Eq. (4.54), using the linear model as a benchmark. The comparisons are based on
overall performance as well as the status of the U.S. economy at the forecast origin.
From the table, we make the following observations:
1. For the overall comparison, the TAR model and the linear model are very
close in MSE, but the TAR model has smaller biases. Yet the MSA model
has the highest MSE and smallest biases.
--- page 248 ---

application
221
TABLE 4.4
Out-of-Sample Forecast Comparison among Linear, TAR, and MSA
Models for the U.S. Quarterly Unemployment Ratea
Relative MSE of Forecast
Model
1-step
2-step
3-step
4-step
5-step
Overall Comparison
Linear
1.00
1.00
1.00
1.00
1.00
TAR
1.00
1.04
0.99
0.98
1.03
MSA
1.19
1.39
1.40
1.45
1.61
MSE
0.08
0.31
0.67
1.13
1.54
Forecast Origins in Economic Contractions
Linear
1.00
1.00
1.00
1.00
1.00
TAR
0.85
0.91
0.83
0.72
0.72
MSA
0.97
1.03
0.96
0.86
1.02
MSE
0.22
0.97
2.14
3.38
3.46
Forecast Origins in Economic Expansions
Linear
1.00
1.00
1.00
1.00
1.00
TAR
1.06
1.13
1.10
1.15
1.17
MSA
1.31
1.64
1.73
1.84
1.87
MSE
0.06
0.21
0.45
0.78
1.24
Mean of Forecast Errors
Model
1-step
2-step
3-step
4-step
5-step
Overall Comparison
Linear
0.03
0.09
0.17
0.25
0.33
TAR
−0.10
−0.02
−0.03
−0.03
−0.01
MSA
0.00
−0.02
−0.04
−0.07
−0.12
Forecast Origins in Economic Contractions
Linear
0.31
0.68
1.08
1.41
1.38
TAR
0.24
0.56
0.87
1.01
0.86
MSA
0.20
0.41
0.57
0.52
0.14
Forecast Origins in Economic Expansions
Linear
−0.01
0.00
0.03
0.08
0.17
TAR
−0.05
−0.11
−0.17
−0.19
−0.14
MSA
−0.03
−0.08
−0.13
−0.17
−0.16
aThe starting forecast origin is 1968.II, where the row marked by MSE shows the MSE of the benchmark
linear model.
