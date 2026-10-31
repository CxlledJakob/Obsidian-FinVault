# Analysis of Financial Time Series, Third Edition (Wiley -- Ruey S_ Tsay -- Wiley series in probability and statistics, 3rd ed_, -- John Wiley & Sons, -- isbn13 9780470414354 -- 9f99b80c7b2dedd477f463dc5323f3b6 -- An.pdf — pages 647–666

--- page 647 ---

620
markov chain monte carlo methods with applications
Result 12.2. Suppose that x1, . . . , xn form a random sample from a normal
distribution with a given mean µ and an unknown precision η. If the prior distribution of η is a gamma distribution with positive parameters α and β, then the
posterior distribution of η is a gamma distribution with parameters α + (n/2) and
β + n
i=1(xi −µ)2/2.
A random variable θ has a beta distribution with positive parameters α and β
if its probability density function is
f (θ|α, β) = (α + β)
(α)(β)θα−1(1 −θ)β−1,
0 < θ < 1.
The mean and variance of θ are E(θ) = α/(α + β) and Var(θ) = αβ/[(α + β)2(α +
β + 1)].
Result 12.3. Suppose that x1, . . . , xn form a random sample from a Bernoulli
distribution with parameter θ. If the prior distribution of θ is a beta distribution
with given positive parameters α and β, then the posterior of θ is a beta distribution
with parameters α + n
i=1 xi and β + n −n
i=1 xi.
Result 12.4. Suppose that x1, . . . , xn form a random sample from a Poisson
distribution with parameter λ. Suppose also that the prior distribution of λ is a
gamma distribution with given positive parameters α and β. Then the posterior
distribution of λ is a gamma distribution with parameters α + n
i=1 xi and β + n.
Result 12.5. Suppose that x1, . . . , xn form a random sample from an exponential
distribution with parameter λ. If the prior distribution of λ is a gamma distribution
with given positive parameters α and β, then the posterior distribution of λ is a
gamma distribution with parameters α + n and β + n
i=1 xi.
A random variable X has a negative binomial distribution with parameters m
and λ, where m > 0 and 0 < λ < 1, if X has a probability mass function
p(n|m, λ) =



 m + n −1
n

λm(1 −λ)n
if n = 0, 1, . . . ,
0
otherwise.
A simple example of negative binomial distribution in ﬁnance is how many MBA
graduates a ﬁrm must interview before ﬁnding exactly m “right candidates” for its
m openings, assuming that the applicants are independent and each applicant has
a probability λ of being a perfect ﬁt. Denote the total number of interviews by Y.
Then X = Y −m is distributed as a negative binomial with parameters m and λ.
Result 12.6. Suppose that x1, . . . , xn form a random sample from a negative
binomial distribution with parameters m and λ, where m is positive and ﬁxed. If
--- page 648 ---

bayesian inference
621
the prior distribution of λ is a beta distribution with positive parameters α and β,
then the posterior distribution of λ is a beta distribution with parameters α + mn
and β + n
i=1 xi.
Next we consider the case of a normal distribution with an unknown mean µ
and an unknown precision η. The two-dimensional prior distribution is partitioned
as P (µ, η) = P (µ|η)P (η).
Result 12.7. Suppose that x1, . . . , xn form a random sample from a normal distribution with an unknown mean µ and an unknown precision η. Suppose also that
the conditional distribution of µ given η = ηo is a normal distribution with mean
µo and precision τoηo and the marginal distribution of η is a gamma distribution
with positive parameters α and β. Then the conditional posterior distribution of µ
given η = ηo is a normal distribution with mean µ∗and precision η∗,
µ∗= τoµo + n¯x
τo + n
and
η∗= (τo + n)ηo,
where ¯x = n
i=1 xi/n is the sample mean, and the marginal posterior distribution
of η is a gamma distribution with parameters α + (n/2) and β∗, where
β∗= β + 1
2
n

i=1
(xi −¯x)2 + τon(¯x −µo)2
2(τo + n)
.
When the conditional variance of a random variable is of interest, an inverted
chi-squared distribution (or inverse chi-squared) is often used. A random variable Y
has an inverted chi-squared distribution with v degrees of freedom if 1/Y follows a
chi-squared distribution with the same degrees of freedom. The probability density
function of Y is
f (y|v) = 2−v/2
(v/2)y−(v/2+1)e−1/(2y),
y > 0.
For this distribution, we have E(Y) = 1/(v −2) if v > 2 and Var(Y) = 2/[(v −
2)2(v −4)] if v > 4.
Result 12.8. Suppose that a1, . . . , an form a random sample from a normal
distribution with mean zero and variance σ 2. Suppose also that the prior distribution of σ 2 is an inverted chi-squared distribution with v degrees of freedom [i.e., (vλ)/σ 2 ∼χ2
v , where λ > 0]. Then the posterior distribution of σ 2 is
also an inverted chi-squared distribution with v + n degrees of freedom—that is,
(vλ + n
i=1 a2
i )/σ 2 ∼χ2
v+n.
--- page 649 ---

622
markov chain monte carlo methods with applications
12.4
ALTERNATIVE ALGORITHMS
In many applications, there are no closed-form solutions for the conditional posterior distributions. But many clever alternative algorithms have been devised in the
statistical literature to overcome this difﬁculty. In this section, we discuss some of
these algorithms.
12.4.1
Metropolis Algorithm
This algorithm is applicable when the conditional posterior distribution is known
except for a normalization constant; see Metropolis and Ulam (1949) and Metropolis et al. (1953). Suppose that we want to draw a random sample from the distribution f (θ|X), which contains a complicated normalization constant so that a direct
draw is either too time-consuming or infeasible. But there exists an approximate
distribution for which random draws are easily available. The Metropolis algorithm
generates a sequence of random draws from the approximate distribution whose
distributions converge to f (θ|X). The algorithm proceeds as follows:
1. Draw a random starting value θ0 such that f (θ0|X) > 0.
2. For t = 1, 2, . . .,
a. Draw a candidate sample θ∗from a known distribution at iteration t given
the previous draw θt−1. Denote the known distribution by Jt(θt|θt−1),
which is called a jumping distribution in Gelman et al. (2003). It is also
referred to as a proposal distribution. The jumping distribution must be
symmetric—that is, Jt(θi|θj) = Jt(θj|θi) for all θi, θj, and t.
b. Calculate the ratio
r =
f (θ∗|X)
f (θt−1|X).
c. Set
θt =
 θ∗
with probability min(r, 1),
θt−1
otherwise.
Under some regularity conditions, the sequence {θt} converges in distribution to
f (θ|X); see Gelman et al. (2003).
Implementation of the algorithm requires the ability to calculate the ratio r for
all θ∗and θt−1, to draw θ∗from the jumping distribution, and to draw a random
realization from a uniform distribution to determine the acceptance or rejection of
θ∗. The normalization constant of f (θ|X) is not needed because only a ratio is
used.
The acceptance and rejection rule of the algorithm can be stated as follows:
(i) if the jump from θt−1 to θ∗increases the conditional posterior density, then
accept θ∗as θt; (ii) if the jump decreases the posterior density, then set θt = θ∗
--- page 650 ---

alternative algorithms
623
with probability equal to the density ratio r, and set θt = θt−1 otherwise. Such a
procedure seems reasonable.
Examples of symmetric jumping distributions include the normal and Studentt distributions for the mean parameter. For a given covariance matrix, we have
f (θi|θj) = f (θj|θi), where f (θ|θo) denotes a multivariate normal density function
with mean vector θo.
12.4.2
Metropolis–Hasting Algorithm
Hasting (1970) generalizes the Metropolis algorithm in two ways. First, the jumping
distribution does not have to be symmetric. Second, the jumping rule is modiﬁed to
r =
f (θ∗|X)/Jt(θ∗|θt−1)
f (θt−1|X)/Jt(θt−1|θ∗) =
f (θ∗|X)Jt(θt−1|θ∗)
f (θt−1|X)Jt(θ∗|θt−1).
This modiﬁed algorithm is referred to as the Metropolis–Hasting algorithm. Tierney
(1994) discusses methods to improve computational efﬁciency of the algorithm.
12.4.3
Griddy Gibbs
In ﬁnancial applications, an entertained model may contain some nonlinear parameters (e.g., the moving-average parameters in an ARMA model or the GARCH
parameters in a volatility model). Since conditional posterior distributions of nonlinear parameters do not have a closed-form expression, implementing a Gibbs sampler
in this situation may become complicated even with the Metropolis–Hasting algorithm. Tanner (1996) describes a simple procedure to obtain random draws in
a Gibbs sampling when the conditional posterior distribution is univariate. The
method is called the Griddy Gibbs sampler and is widely applicable. However, the
method could be inefﬁcient in a real application.
Let
θi
be
a
scalar
parameter
with
conditional
posterior
distribution
f (θi|X, θ−i), where θ−i is the parameter vector after removing θi. For instance,
if θ = (θ1, θ2, θ3)′, then θ−1 = (θ2, θ3)′. The Griddy Gibbs proceeds as follows:
1. Select a grid of points from a properly selected interval of θi, say, θi1 ≤
θi2 ≤· · · ≤θim. Evaluate the conditional posterior density function to obtain
wj = f (θij|X, θ−i) for j = 1, . . . , m.
2. Use w1, . . . , wm to obtain an approximation to the inverse cumulative distribution function (CDF) of f (θi|X, θ−i).
3. Draw a uniform (0,1) random variate and transform the observation via the
approximate inverse CDF to obtain a random draw for θi.
Some remarks on the Griddy Gibbs are in order. First, the normalization constant of the conditional posterior distribution f (θi|X, θ−i) is not needed because
the inverse CDF can be obtained from {wj}m
j=1 directly. Second, a simple approximation to the inverse CDF is a discrete distribution for {θij}m
j=1 with probability p(θij) = wj/ m
v=1 wv. Third, in a real application, selection of the interval
--- page 651 ---

624
markov chain monte carlo methods with applications
[θi1, θim] for the parameter θi must be checked carefully. A simple checking procedure is to consider the histogram of the Gibbs draws of θi. If the histogram indicates
substantial probability around θi1 or θim, then the interval must be expanded. However, if the histogram shows a concentration of probability inside the interval
[θi1, θim], then the interval is too wide and can be shortened. If the interval is
too wide, then the Griddy Gibbs becomes inefﬁcient because most of wj would be
zero. Finally, the Griddy Gibbs or Metropolis–Hasting algorithm can be used in a
Gibbs sampling to obtain random draws of some parameters.
12.5
LINEAR REGRESSION WITH TIME SERIES ERRORS
We are ready to consider some speciﬁc applications of MCMC methods. Examples
discussed in the next few sections are for illustrative purposes only. The goal here
is to highlight the applicability and usefulness of the methods. Understanding these
examples can help readers gain insights into applications of MCMC methods in
ﬁnance.
The ﬁrst example is to estimate a regression model with serially correlated
errors. This is a topic discussed in Chapter 2, where we use SCA to perform the
estimation. A simple version of the model is
yt = β0 + β1x1t + · · · + βkxkt + zt,
zt = φzt−1 + at,
where yt is the dependent variable, xit are explanatory variables that may contain
lagged values of yt, and zt follows a simple AR(1) model with {at} being a sequence
of independent and identically distributed normal random variables with mean zero
and variance σ 2. Denote the parameters of the model by θ = (β′, φ, σ 2)′, where
β = (β0, β1, . . . , βk)′, and let xt = (1, x1t, . . . , xkt)′ be the vector of all regressors
at time t, including a constant of unity. The model becomes
yt = x′
tβ + zt,
zt = φzt−1 + at,
t = 1, . . . , n,
(12.6)
where n is the sample size.
A natural way to implement Gibbs sampling in this case is to iterate between
regression estimation and time series estimation. If the time series model is known,
we can estimate the regression model easily by using the least-squares method.
However, if the regression model is known, we can obtain the time series zt by
using zt = yt −x′
tβ and use the series to estimate the AR(1) model. Therefore, we
need the following conditional posterior distributions:
f (β|Y, X, φ, σ 2),
f (φ|Y, X, β, σ 2),
f (σ 2|Y, X, β, φ),
where Y = (y1, . . . , yn)′ and X denotes the collection of all observations of
explanatory variables.
--- page 652 ---

linear regression with time series errors
625
We use conjugate prior distributions to obtain closed-form expressions for the
conditional posterior distributions. The prior distributions are
β ∼N(βo, o),
φ ∼N(φo, σ 2
o ),
vλ
σ 2 ∼χ2
v ,
(12.7)
where again ∼denotes distribution, and βo, o, λ, v, φo, and σ 2
o are known quantities. These quantities are referred to as hyperparameters in Bayesian inference.
Their exact values depend on the problem at hand. Typically, we assume that βo
= 0, φo = 0, and o is a diagonal matrix with large diagonal elements. The prior
distributions in Eq. (12.7) are assumed to be independent of each other. Thus, we
use independent priors based on the partition of the parameter vector θ.
The conditional posterior distribution f (β|Y, X, φ, σ 2) can be obtained by using
Result 12.1a of Section 12.3. Speciﬁcally, given φ, we deﬁne
yo,t = yt −φyt−1,
xo,t = xt −φxt−1.
Using Eq. (12.6), we have
yo,t = β′xo,t + at,
t = 2, . . . , n.
(12.8)
Under the assumption of {at}, Eq. (12.8) is a multiple linear regression. Therefore,
information of the data about the parameter vector β is contained in its least-squares
estimate
β =
 n

t=2
xo,tx′
o,t
−1  n

t=2
xo,tyo,t

,
which has a multivariate normal distribution
β ∼N

β,
σ 2
 n

t=2
xo,tx′
o,t
−1
.
Using Result 12.1a, the posterior distribution of β, given the data, φ, and σ 2, is
multivariate normal. We write the result as
(β|Y, X, φ, σ) ∼N(β∗, ∗),
(12.9)
where the parameters are given by
−1
∗
=
n
t=2 xo,tx′
o,t
σ 2
+ −1
o ,
β∗= ∗
n
t=2 xo,tx′
o,t
σ 2
β + −1
o βo

.
--- page 653 ---

626
markov chain monte carlo methods with applications
Next, consider the conditional posterior distribution of φ given β, σ 2, and the
data. Because β is given, we can calculate zt = yt −β′xt for all t and consider
the AR(1) model
zt = φzt−1 + at,
t = 2, . . . , n.
The information of the likelihood function about φ is contained in the least-squares
estimate
φ =
 n

t=2
z2
t−1
−1  n

t=2
zt−1zt

,
which is normally distributed with mean φ and variance σ 2(n
t=2 z2
t−1)−1. Based
on Result 12.1, the posterior distribution of φ is also normal with mean φ∗and
variance σ 2
∗, where
σ −2
∗
=
n
t=2 z2
t−1
σ 2
+ σ −2
o ,
φ∗= σ 2
∗
n
t=2 z2
t−1
σ 2
φ + σ −2
o φo

.
(12.10)
Finally, turn to the posterior distribution of σ 2 given β, φ, and the data. Because
β and φ are known, we can calculate
at = zt −φzt−1,
zt = yt −β′xt,
t = 2, . . . , n.
By Result 12.8, the posterior distribution of σ 2 is an inverted chi-squared
distribution—that is,
vλ + n
t=2 a2
t
σ 2
∼χ2
v+(n−1),
(12.11)
where χ2
k denotes a chi-squared distribution with k degrees of freedom.
Using the three conditional posterior distributions in Eqs. (12.9)–(12.11), we
can estimate Eq. (12.6) via Gibbs sampling as follows:
1. Specify the hyperparameter values of the priors in Eq. (12.7).
2. Specify arbitrary starting values for β, φ, and σ 2 (e.g., the ordinary leastsquares estimate of β without time series errors).
3. Use the multivariate normal distribution in Eq. (12.9) to draw a random
realization for β.
4. Use the univariate normal distribution in Eq. (12.10) to draw a random realization for φ.
5. Use the chi-squared distribution in Eq. (12.11) to draw a random realization
for σ 2.
--- page 654 ---

linear regression with time series errors
627
Repeat steps 3–5 for many iterations to obtain a Gibbs sample. The sample means
are then used as point estimates of the parameters of model (12.6).
Example 12.1.
As an illustration, we revisit the example of U.S. weekly interest rates of Chapter 2. The data are the 1-year and 3-year Treasury constant maturity
rates from January 5, 1962, to April 10, 2009, and are obtained from the Federal
Reserve Bank of St. Louis. Because of unit-root nonstationarity, the dependent and
independent variables are
1. c3t = r3t −r3,t−1, which is the weekly change in 3-year maturity rate,
2. c1t = r1t −r1,t−1, which is the weekly change in 1-year maturity rate,
where the original interest rates rit are measured in percentages. In Chapter 2, we
employed a linear regression model with an MA(1) error for the data. Here we
consider an AR(2) model for the error process. Using the traditional approach in
R, we obtain the model
c3t = 0.782c1t + zt,
zt = 0.183zt−1 −0.036zt−2 + at,
(12.12)
where σa = 0.068. Standard errors of the coefﬁcient estimates of Eq. (12.12)
are 0.0075, 0.0201, and 0.0201, respectively. Except for a marginally signiﬁcant
residual ACF at lags 4 and 6, the prior model seems adequate.
Writing the model as
c3t = βc1t + zt,
zt = φ1zt−1 + φ2zt−2 + at,
(12.13)
where {at} is an independent sequence of N(0, σ 2) random variables, we estimate
the parameters by Gibbs sampling. The prior distributions used are
β ∼N(0, 4),
φ ∼N[0, diag(0.25, 0.16)],
(vλ)/σ 2 = (10 × 0.05)/σ 2 ∼χ2
10.
The initial parameter estimates are obtained by the ordinary least-squares method
[i.e., by using a two-step procedure of ﬁtting the linear regression model ﬁrst, then
ﬁtting an AR(2) model to the regression residuals]. Since the sample size 2466 is
large, the initial estimates are close to those given in Eq. (12.12). We iterated the
Gibbs sampling for 2100 iterations but discard results of the ﬁrst 100 iterations.
Table 12.1 gives the posterior means and standard errors of the parameters. From
the table, the posterior mean of σ is approximately 0.069. Figure 12.1 shows the
time plots of the 2000 Gibbs draws of the parameters. The plots show that the draws
are stable. Figure 12.2 gives the histogram of the marginal posterior distribution of
each parameter.
We repeated the Gibbs sampling with different initial values but obtained similar
results. The Gibbs sampling appears to have converged. From Table 12.1, the
posterior means are close to the estimates of Eq. (12.12).This is expected as the
sample size is large and the model is relatively simple.
--- page 655 ---

628
markov chain monte carlo methods with applications
TABLE 12.1
Posterior Means and Standard Errors of Model (12.13)
Estimated by Gibbs Sampling with 2100 Iterationsa
Parameter
β
φ1
φ2
σ 2
Mean
0.793
0.184
−0.036
0.00479
Standard error
0.008
0.019
0.021
0.00013
aThe results are based on the last 2000 iterations, and the prior distributions are given
in the text.
b
0
500
1000
1500
2000
0.77
0.79
0.81
Iterations
Iterations
Iterations
Iterations
f1
0
500
1000
1500
2000
0.12 0.16 0.20 0.24
f2
0
500
1000
1500
2000
0.10 0.06 0.02 0.02
s2
0
500
1000
1500
2000
0.0044
0.0048
0.0052
Figure 12.1
Time plots of Gibbs draws for the model in Eq. (12.13) with 2100 iterations. Results are
based on last 2000 draws. Prior distributions and starting parameter values are given in text.
12.6
MISSING VALUES AND OUTLIERS
In this section, we discuss MCMC methods for handling missing values and detecting additive outliers. Let {yt}n
t=1 be an observed time series. A data point yh is an
additive outlier if
yt =
 xh + ω
if t = h,
xt
otherwise,
(12.14)
where ω is the magnitude of the outlier and xt is an outlier-free time series.
Examples of additive outliers include recording errors (e.g., typos and measurement
errors). Outliers can seriously affect time series analysis because they may induce
substantial biases in parameter estimation and lead to model misspeciﬁcation.
--- page 656 ---

missing values and outliers
629
0.77 0.78 0.79 0.80 0.81 0.82
0 100200300400500
b
0.12 0.14 0.16 0.18 0.20 0.22 0.24 0.26
0
100 200 300 400
f1
0.10
0.06
0.02
0.0
0.02
0
100 200 300 400
f2
0.0044 0.0046 0.0048 0.0050 0.0052
0
50
100 200 300
s1
Figure 12.2
Histograms of Gibbs draws for model in Eq. (12.13) with 2100 iterations. Results are
based on last 2000 draws. Prior distributions and starting parameter values are given in text.
Consider a time series xt and a ﬁxed time index h. We can learn a lot about xh by
treating it as a missing value. If the model of xt were known, then we could derive
the conditional distribution of xh given the other values of the series. By comparing
the observed value yh with the derived distribution of xh, we can determine whether
yh can be classiﬁed as an additive outlier. Speciﬁcally, if yh is a value that is likely
to occur under the derived distribution, then yh is not an additive outlier. However,
if the chance to observe yh is very small under the derived distribution, then yh
can be classiﬁed as an additive outlier. Therefore, detection of additive outliers and
treatment of missing values in time series analysis are based on the same idea.
In the literature, missing values in a time series can be handled by using either
the Kalman ﬁlter or MCMC methods; see Jones (1980), Chapter 11, and McCulloch
and Tsay (1994a). Outlier detection has also been carefully investigated; see Chang,
Tiao, and Chen (1988), Tsay (1988), Tsay, Pe˜na, and Pankratz (2000), and the
references therein. The outliers are classiﬁed into four categories depending on the
nature of their impacts on the time series. Here we focus on additive outliers.
12.6.1
Missing Values
For ease in presentation, consider an AR(p) time series
xt = φ1xt−1 + · · · + φpxt−p + at,
(12.15)
--- page 657 ---

630
markov chain monte carlo methods with applications
where {at} is a Gaussian white noise series with mean zero and variance σ 2.
Suppose that the sampling period is from t = 1 to t = n, but the observation xh is
missing, where 1 < h < n. Our goal is to estimate the model in the presence of a
missing value.
In this particular instance, the parameters are θ = (φ′, xh, σ 2)′, where φ =
(φ1, . . . , φp)′. Thus, we treat the missing value xh as an unknown parameter. If we
assume that the prior distributions are
φ ∼N(φo, o),
xh ∼N(µo, σ 2
o ),
vλ
σ 2 ∼χ2
v ,
where the hyperparameters are known, then the conditional posterior distributions
f (φ|X, xh, σ 2) and f (σ 2|X, xh, φ) are exactly as those given in the previous
section, where X denotes the observed data. The conditional posterior distribution
f (xh|X, φ, σ 2) is univariate normal with mean µ∗and variance σ 2
h. These two
parameters can be obtained by using a linear regression model. Speciﬁcally, given
the model and the data, xh is only related to {xh−p, . . . , xh−1, xh+1, . . . , xh+p}.
Keeping in mind that xh is an unknown parameter, we can write the relationship
as follows:
1. For t = h, the model says
xh = φ1xh−1 + · · · + φpxh−p + ah.
Letting yh = φ1xh−1 + · · · + φpxh−p and bh = −ah, the prior equation can
be written as
yh = xh + bh = φ0xh + bh,
where φ0 = 1.
2. For t = h + 1, we have
xh+1 = φ1xh + φ2xh−1 + · · · + φpxh+1−p + ah+1.
Letting yh+1 = xh+1 −φ2xh−1 −· · · −φpxh+1−p and bh+1 = ah+1, the prior
equation can be written as
yh+1 = φ1xh + bh+1.
3. In general, for t = h + j with j = 1, . . . , p, we have
xh+j = φ1xh+j−1 + · · · + φjxh + φj+1xh−1 + · · · + φpxh+j−p + ah+j.
Let
yh+j = xh+j −φ1xh+j−1−· · ·−φj−1xh+1−φj+1xh−1−· · ·−φpxh+j−p
and bh+j = ah+j. The prior equation reduces to
yh+j = φjxh + bh+j.
--- page 658 ---

missing values and outliers
631
Consequently, for an AR(p) model, the missing value xh is related to the model,
and the data in p + 1 equations
yh+j = φjxh + bh+j,
j = 0, . . . , p,
(12.16)
where φ0 = 1. Since a normal distribution is symmetric with respect to its mean, ah
and −ah have the same distribution. Consequently, Eq. (12.16) is a special simple
linear regression model with p + 1 data points. The least-squares estimate of xh
and its variance are
xh =
p
j=0 φjyh+j
p
j=0 φ2
j
,
Var(xh) =
σ 2
p
j=0 φ2
j
.
For instance, when p = 1, we have xh = [φ1/(1 + φ2
1)](xh−1 + xh+1), which is
referred to as the ﬁltered value of xh. Because a Gaussian AR(1) model is time
reversible, equal weights are applied to the two neighboring observations of xh to
obtain the ﬁltered value.
Finally, using Result 12.1, we obtain that the posterior distribution of xh is
normal with mean µ∗and variance σ 2
∗, where
µ∗=
σ 2µo + σ 2
o (p
j=0 φ2
j)xh
σ 2 + σ 2o (p
j=0 φ2
j )
,
σ 2
∗=
σ 2σ 2
o
σ 2 + σ 2o
p
j=0 φ2
j
.
(12.17)
Missing values may occur in patches, resulting in the situation of multiple consecutive missing values. These missing values can be handled in two ways. First,
we can generalize the prior method directly to obtain a solution for multiple ﬁltered values. Consider, for instance, the case that xh and xh+1 are missing. These
missing values are related to {xh−p, . . . , xh−1; xh+2, . . . , xh+p+1}. We can deﬁne a
dependent variable yh+j in a similar manner as before to set up a multiple linear
regression with parameters xh and xh+1. The least-squares method is then used to
obtain estimates of xh and xh+1. Combining with the speciﬁed prior distributions,
we have a bivariate normal posterior distribution for (xh, xh+1)′. In Gibbs sampling,
this approach draws the consecutive missing values jointly. Second, we can apply
the result of a single missing value in Eq. (12.17) multiple times within a Gibbs
iteration. Again consider the case of missing xh and xh+1. We can employ the
conditional posterior distributions f (xh|X, xh+1, φ, σ 2) and f (xh+1|X, xh, φ, σ 2)
separately. In Gibbs sampling, this means that we draw the missing value one at a
time.
Because xh and xh+1 are correlated in a time series, drawing them jointly is
preferred in a Gibbs sampling. This is particularly so if the number of consecutive
missing values is large. Drawing one missing value at a time works well if the
number of missing values is small.
Remark.
In the previous discussion, we assumed h −p ≥1 and h + p ≤n.
If h is close to the end points of the sample period, the number of data points
available in the linear regression model must be adjusted.
□
--- page 659 ---

632
markov chain monte carlo methods with applications
12.6.2
Outlier Detection
Detection of additive outliers in Eq. (12.14) becomes straightforward under the
MCMC framework. Except for the case of a patch of additive outliers with similar
magnitudes, the simple Gibbs sampler of McCulloch and Tsay (1994a) seems to
work well; see Justel, Pe˜na, and Tsay (2001). Again we use an AR model to
illustrate the problem. The method applies equally well to other time series models
when the Metropolis–Hasting algorithm or the Griddy Gibbs is used to draw values
of nonlinear parameters.
Assume that the observed time series is yt, which may contain some additive
outliers whose locations and magnitudes are unknown. We write the model for
yt as
yt = δtβt + xt,
t = 1, . . . , n,
(12.18)
where {δt} is a sequence of independent Bernoulli random variables such that
P (δt = 1) = ϵ and P (δt = 0) = 1 −ϵ, ϵ is a constant between 0 and 1, {βt} is a
sequence of independent random variables from a given distribution, and xt is an
outlier-free AR(p) time series,
xt = φ0 + φ1xt−1 + · · · + φpxt−p + at,
where {at} is a Gaussian white noise with mean zero and variance σ 2. This model
seems complicated, but it allows additive outliers to occur at every time point. The
chance of being an outlier for each observation is ϵ.
Under the model in Eq. (12.18), we have n data points, but there are 2n + p + 3
parameters—namely, φ = (φ0, . . . , φp)′, δ = (δ1, . . . , δn)′, β = (β1, . . . , βn)′, σ 2,
and ϵ. The binary parameters δt are governed by ϵ and the βt are determined by the
speciﬁed distribution. The parameters δ and β are introduced by using the idea of
data augmentation with δt denoting the presence or absence of an additive outlier
at time t, and βt is the magnitude of the outlier at time t when it is present.
Assume that the prior distributions are
φ ∼N(φo, o),
vλ
σ 2 ∼χ2
v ,
ϵ ∼Beta(γ1, γ2),
βt ∼N(0, ξ 2),
where the hyperparameters are known. These are conjugate prior distributions. To
implement Gibbs sampling for model estimation with outlier detection, we need to
consider the conditional posterior distributions of
f (φ|Y, δ, β, σ 2),
f (δh|Y, δ−h, β, φ, σ 2),
f (βh|Y, δ, β−h, φ, σ 2),
f (ϵ|Y, δ),
f (σ 2|Y, φ, δ, β),
where 1 ≤h ≤n, Y denotes the data, and θ−i denotes that the ith element of θ is
removed.
--- page 660 ---

missing values and outliers
633
Conditioned on δ and β, the outlier-free time series xt can be obtained by
xt = yt −δtβt. Information of the data about φ is then contained in the least-squares
estimate
φ =


n

t=p+1
xt−1x′
t−1


−1 

n

t=p+1
xt−1xt

,
where xt−1 = (1, xt−1, . . . , xt−p)′, which is normally distributed with mean φ and
covariance matrix
 = σ 2


n

t=p+1
xt−1x′
t−1


−1
.
The conditional posterior distribution of φ is therefore multivariate normal with
mean φ∗and covariance matrix ∗, which are given in Eq. (12.9) with β being
replaced by φ and xo,t by xt−1. Similarly, the conditional posterior distribution of
σ 2 is an inverted chi-squared distribution—that is,
vλ + n
t=p+1 a2
t
σ 2
∼χ2
v+(n−p),
where at = xt −φ′xt−1 and xt = yt −δtβt.
The conditional posterior distribution of δh can be obtained as follows. First, δh is
only related to {yj, βj}h+p
j=h−p, {δj}h+p
j=h−p with j̸ = h, φ, and σ 2. More speciﬁcally,
we have
xj = yj −δjβj,
j̸ = h.
Second, xh can assume two possible values: xh = yh −βh if δh = 1 and xh = yh,
otherwise. Deﬁne
wj = x∗
j −φ0 −φ1x∗
j−1 −· · · −φpx∗
j−p,
j = h, . . . , h + p,
where x∗
j = xj if j̸ = h and x∗
h = yh. The two possible values of xh give rise to
two situations:
• Case I: δh = 0. Here the hth observation is not an outlier and x∗
h = yh = xh.
Hence, wj = aj for j = h, . . . , h + p. In other words, we have
wj ∼N(0, σ 2),
j = h, . . . , h + p.
--- page 661 ---

634
markov chain monte carlo methods with applications
• Case II: δh = 1. Now the hth observation is an outlier and x∗
h = yh = xh + βh.
The wj deﬁned before is contaminated by βh. In fact, we have
wh ∼N(βh, σ 2)
and
wj ∼N(−φj−hβh, σ 2),
j = h + 1, . . . , h + p.
If we deﬁne ψ0 = −1 and ψi = φi for i = 1, . . . , p, then we have wj ∼
N(−ψj−hβh, σ 2) for j = h, . . . , h + p.
Based on the prior discussion, we can summarize the situation as follows:
1. Case I: δh = 0 with probability 1 −ϵ. In this case, wj ∼N(0, σ 2) for j =
h, . . . , h + p.
2. Case II: δh = 1 with probability ϵ. Here wj ∼N(−ψj−hβh, σ 2) for j =
h, . . . , h + p.
Since there are n data points, j cannot be greater than n. Let m = min(n, h + p).
The posterior distribution of δh is therefore
P (δh = 1|Y, δ−h, β, φ, σ 2)
=
ϵ exp[−m
j=h(wj + ψj−hβh)2/(2σ 2)]
ϵ exp[−m
j=h(wj + ψj−hβh)2/(2σ 2)] + (1 −ϵ) exp[−m
j=h w2
j/(2σ 2)].
(12.19)
This posterior distribution is simply to compare the weighted values of the likelihood function under the two situations with weight being the probability of each
situation.
Finally, the posterior distribution of βh is as follows.
• If δh = 0, then yh is not an outlier and βh ∼N(0, ξ 2).
• If δh = 1, then yh is contaminated by an outlier with magnitude βh. The
variable wj deﬁned before contains information of βh for j = h, h + 1,
. . . , min(h + p, n).
Speciﬁcally,
we
have
wj ∼N(−ψj−hβh, σ 2)
for
j = h, h + 1, . . . , min(h + p, n). The information can be put in a linear
regression framework as
wj = −ψj−hβh + aj,
j = h, h + 1, . . . , min(h + p, n).
Consequently, the information is embedded in the least-squares estimate
βh =
m
j=h −ψj−hwj
m
j=h ψ2
j−h
,
m = min(h + p, n),
--- page 662 ---

missing values and outliers
635
which is normally distributed with mean βh and variance σ 2/(m
j=h ψ2
j−h).
By Result 12.1, the posterior distribution of βh is normal with mean β∗
h and
variance σ 2
h∗, where
β∗
h =
−(m
j=h ψj−hwj)ξ 2
σ 2 + (m
j=h ψ2
j−h)ξ 2 ,
σ 2
h∗=
σ 2ξ 2
σ 2 + (m
j=h ψ2
j−h)ξ 2 .
Example 12.2.
Consider the weekly change series of U.S. 3-year Treasury
constant maturity interest rate from March 18, 1988, to September 10, 1999, for 600
observations. The interest rate is in percentage and is a subseries of the dependent
variable c3t of Example 12.1. The time series is shown in Figure 12.3(a). If AR
models are entertained for the series, the partial autocorrelation function suggests
an AR(3) model and we obtain
c3t = 0.227c3,t−1 + 0.006c3,t−2 + 0.114c3,t−2 + at,
σ 2 = 0.0128,
Year
c3t
1988
(a)
1990
1992
1994
1996
1998
2000
−0.4−0.20.0 0.2 0.4
Year
(b)
Probability
1988
1990
1992
1994
1996
1998
2000
0.0 0.2 0.4 0.6 0.8
Year
(c)
Magnitude
1988
1990
1992
1994
1996
1998
2000
−0.3−0.2−0.1 0.0 0.1
Figure 12.3
Time plots of weekly change series of U.S. 3-year Treasury constant maturity interest
rate from March 18, 1988, to September 10, 1999: (a) data, (b) posterior probability of being an outlier,
and (c) posterior mean of outlier size. Estimation is based on Gibbs sampling with 1050 iterations with
ﬁrst 50 iterations as burn-ins.
--- page 663 ---

636
markov chain monte carlo methods with applications
where standard errors of the coefﬁcients are 0.041, 0.042, and 0.041, respectively.
The Ljung–Box statistics of the residuals show Q(12) = 11.4, which is insigniﬁcant
at the 5% level.
Next, we apply the Gibbs sampling to estimate the AR(3) model and to detect
simultaneously possible additive outliers. The prior distributions used are
φ ∼N(0, 0.25I 3),
vλ
σ 2 = 5 × 0.00256
σ 2
∼χ2
5,
γ1 = 5,
γ2 = 95,
ξ 2 = 0.1,
where 0.00256 ≈σ 2/5 and ξ 2 ≈9σ 2. The expected number of additive outliers is
5%. Using initial values ϵ = 0.05, σ 2 = 0.012, φ1 = 0.2, φ2 = 0.02, and φ3 =
0.1, we run the Gibbs sampling for 1050 iterations but discard results of the ﬁrst
50 iterations. Using posterior means of the coefﬁcients as parameter estimates, we
obtain the ﬁtted model
c3t = 0.252c3,t−1 + 0.003c3,t−2 + 0.110c3,t−2 + at,
σ 2 = 0.0118,
where posterior standard deviations of the parameters are 0.046, 0.045, 0.046, and
0.0008, respectively. Thus, the Gibbs sampling produces results similar to that
of the maximum-likelihood method. Figure 12.3(b) shows the time plot of posterior probability of each observation being an additive outlier, and Figure 12.3(c)
plots the posterior mean of outlier magnitude. From the probability plot, some
observations have high probabilities of being an outlier. In particular, t = 323 has
a probability of 0.83 and the associated posterior mean of outlier magnitude is
−0.304. This point corresponds to May 20, 1994, when the c3t changed from 0.24
to −0.34 (i.e., about a 0.6% drop in the weekly interest rate within 2 weeks). The
point with second highest posterior probability of being an outlier is t = 201, which
is January 17, 1992. The outlying posterior probability is 0.58 and the estimated
outlier size is 0.176. At this particular time point, c3t changed from −0.02 to 0.33,
corresponding to a jump of about 0.35% in the weekly interest rate.
Remark.
Outlier detection via Gibbs sampling requires intensive computation
but the approach performs a joint estimation of model parameters and outliers. Yet
the traditional approach to outlier detection separates estimation from detection. It
is much faster in computation, but may produce spurious detections when multiple
outliers are present. For the data in Example 12.2, the SCA program also identiﬁes
t = 323 and t = 201 as the two most signiﬁcant additive outliers. The estimated
outlier sizes are −0.39 and 0.36, respectively.
□
12.7
STOCHASTIC VOLATILITY MODELS
An important ﬁnancial application of MCMC methods is the estimation of stochastic volatility models; see Jacquier, Polson, and Rossi (1994) and the references
--- page 664 ---

stochastic volatility models
637
therein. We start with a univariate stochastic volatility model. The mean and volatility equations of an asset return rt are
rt = β0 + β1x1t + · · · + βpxpt + at,
at =

htϵt,
(12.20)
ln ht = α0 + α1 ln ht−1 + vt,
(12.21)
where {xit|i = 1, . . . , p} are explanatory variables available at time t −1, the βj
are parameters, {ϵt} is a Gaussian white noise sequence with mean 0 and variance
1, {vt} is also a Gaussian white noise sequence with mean 0 and variance σ 2
v , and
{ϵt} and {vt} are independent. The log transformation is used to ensure that ht is
positive for all t. The explanatory variables xit may include lagged values of the
return (e.g., xit = rt−i). In Eq. (12.21), we assume that |α1| < 1 so that the log
volatility process ln ht is stationary. If necessary, a higher order AR(p) model can
be used for ln ht.
Denote the coefﬁcient vector of the mean equation by β = (β0, β1, . . . , βp)′
and the parameter vector of the volatility equation by ω = (α0, α1, σ 2
v )′. Suppose
that R = (r1, . . . , rn)′ is the collection of observed returns and X is the collection
of explanatory variables. Let H = (h1, . . . , hn)′ be the vector of unobservable
volatilities. Here β and ω are the “traditional” parameters of the model and H
is an auxiliary variable. Estimation of the model would be complicated via the
maximum-likelihood method because the likelihood function is a mixture over the
n-dimensional H distribution as
f (R|X, β, ω) =

f (R|X, β, H)f (H|ω) dH.
However, under the Bayesian framework, the volatility vector H consists of augmented parameters. Conditioning on H, we can focus on the probability distribution
functions f (R|H, β) and f (H|ω) and the prior distribution p(β, ω). We assume
that the prior distribution can be partitioned as p(β, ω) = p(β)p(ω); that is, prior
distributions for the mean and volatility equations are independent. A Gibbs sampling approach to estimating the stochastic volatility in Eqs. (12.20) and (12.21)
then involves drawing random samples from the following conditional posterior
distributions:
f (β|R, X, H, ω),
f (H|R, X, β, ω),
f (ω|R, X, β, H).
In what follows, we give details of practical implementation of the Gibbs sampling
used.
12.7.1
Estimation of Univariate Models
Given H, the mean equation in (12.20) is a nonhomogeneous linear regression.
Dividing the equation by
√
ht, we can write the model as
ro,t = x′
o,tβ + ϵt,
t = 1, . . . , n,
(12.22)
--- page 665 ---

638
markov chain monte carlo methods with applications
where ro,t = rt/
√
ht and xo,t = xt/√ht, with xt = (1, x1t, . . . , xpt)′ being the vector of explanatory variables. Suppose that the prior distribution of β is multivariate
normal with mean βo and covariance matrix Ao. Then the posterior distribution of
β is also multivariate normal with mean β∗and covariance matrix A∗. These two
quantities can be obtained as before via Result 12.1a, and they are
A−1
∗
=
n

t=1
xo,tx′
o,t + A−1
o ,
β∗= A∗
 n

t=1
xo,tro,t + A−1
o βo

,
where it is understood that the summation starts with p + 1 if rt−p is the highest
lagged return used in the explanatory variables.
The volatility vector H is drawn element by element. The necessary conditional
posterior distribution is f (ht|R, X, H −t, β, ω), which is produced by the normal
distribution of at and the lognormal distribution of the volatility,
f (ht|R, X, β, H −t, ω)
∝f (at|ht, rt, xt, β)f (ht|ht−1, ω)f (ht+1|ht, ω)
∝h−0.5
t
exp[−(rt −x′
tβ)2/(2ht)]h−1
t
exp[−(ln ht −µt)2/(2σ 2)]
∝h−1.5
t
exp[−(rt −x′
tβ)2/(2ht) −(ln ht −µt)2/(2σ 2)],
(12.23)
where
µt = [α0(1 −α1) + α1(ln ht+1 + ln ht−1)]/(1 + α2
1)
and
σ 2 = σ 2
v /(1 +
α2
1). Here we have used the following properties: (a) at|ht ∼N(0, ht); (b) ln ht|
ln ht−1 ∼N(α0 + α1 ln ht−1, σ 2
v ); (c) ln ht+1| ln ht ∼N(α0 + α1 ln ht, σ 2
v ); (d)
d ln ht = h−1
t
dht, where d denotes differentiation; and (e) the equality
(x −a)2A + (x −b)2C = (x −c)2(A + C) + (a −b)2AC/(A + C),
where c = (Aa + Cb)/(A + C) provided that A + C̸ = 0. This equality is a scalar
version of Lemma 1 of Box and Tiao (1973, p. 418). In our application, A = 1, a =
α0 + ln ht−1, C = α2
1, and b = (ln ht+1 −α0)/α1. The term (a −b)2AC/(A + C)
does not contain the random variable ht and, hence, is integrated out in the derivation of the conditional posterior distribution. Jacquier, Polson, and Rossi (1994) use
the Metropolis algorithm to draw ht. We use Griddy Gibbs in this section, and the
range of ht is chosen to be a multiple of the unconditional sample variance of rt.
To draw random samples of ω, we partition the parameters as α = (α0, α1)′
and σ 2
v . The prior distribution of ω is also partitioned accordingly [i.e., p(ω) =
p(α)p(σ 2
v )]. The conditional posterior distributions needed are
• f (α|Y, X, H, β, σ 2
v ) = f (α|H, σ 2
v ): Given H, ln ht
follows an AR(1)
model. Therefore, the result of AR models discussed in the previous two
sections applies. Speciﬁcally, if the prior distribution of α is multivariate
--- page 666 ---

stochastic volatility models
639
normal with mean αo and covariance matrix Co, then f (α|H, σ 2
v ) is
multivariate normal with mean α∗and covariance matrix C∗, where
C−1
∗
=
n
t=2 ztz′
t
σ 2v
+ C−1
o ,
α∗= C∗
n
t=2 zt ln ht
σ 2v
+ C−1
o αo

,
where zt = (1, ln ht−1)′.
• f (σ 2
v |Y, X, H, β, α) = f (σ 2
v |H, α): Given H and α, we can calculate vt =
ln ht −α0 −α1 ln ht−1 for t = 2, . . . , n. Therefore, if the prior distribution
of σ 2
v is (mλ)/σ 2
v ∼χ2
m, then the conditional posterior distribution of σ 2
v is
an inverted chi-squared distribution with m + n −1 degrees of freedom; that
is,
mλ + n
t=2 v2
t
σ 2v
∼χ2
m+n−1.
Remark.
Formula (12.23) is for 1 < t < n, where n is the sample size. For
the two end data points h1 and hn, some modiﬁcations are needed. A simple
approach is to assume that h1 is ﬁxed so that the drawing of ht starts with t = 2.
For t = n, one uses the result ln hn ∼(α0 + α1 ln hn−1, σ 2
v ). Alternatively, one
can employ a forecast of hn+1 and a backward prediction of h0 and continue to
apply the formula. Since hn is the variable of interest, we forecast hn+1 by using
a 2-step-ahead forecast at the forecast origin n −1. For the model in Eq. (12.21),
the forecast of hn+1 is
hn−1(2) = α0 + α1(α0 + α1 ln hn−1).
The backward prediction of h0 is based on the time reversibility of the model
(ln ht −η) = α1(ln ht−1 −η) + vt,
where η = α0/(1 −α1) and |α1| < 1. The model of the reversed series is
(ln ht −η) = α1(ln ht+1 −η) + v∗
t ,
where {v∗
t } is also a Gaussian white noise series with mean zero and variance σ 2
v .
Consequently, the 2-step-backward prediction of h0 at time t = 2 is
h2(−2) = α2
1(ln h2 −η).
□
Remark.
Formula (12.23) can also be obtained by using results of a missing
value in an AR(1) model; see Section 12.6.1. Speciﬁcally, assume that ln ht is
missing. For the AR(1) model in Eq. (12.21), this missing value is related to
ln ht−1 and ln ht+1 for 1 < t < n. From the model, we have
ln ht = α0 + α1 ln ht−1 + at.
