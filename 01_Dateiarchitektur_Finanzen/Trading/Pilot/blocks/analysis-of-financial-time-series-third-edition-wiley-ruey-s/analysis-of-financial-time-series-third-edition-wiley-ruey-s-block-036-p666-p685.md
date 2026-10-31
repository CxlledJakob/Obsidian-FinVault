# Analysis of Financial Time Series, Third Edition (Wiley -- Ruey S_ Tsay -- Wiley series in probability and statistics, 3rd ed_, -- John Wiley & Sons, -- isbn13 9780470414354 -- 9f99b80c7b2dedd477f463dc5323f3b6 -- An.pdf — pages 666–685

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
--- page 667 ---

640
markov chain monte carlo methods with applications
Deﬁne yt = α0 + α1yt−1, xt = 1, and bt = −at. Then we obtain
yt = xt ln ht + bt.
(12.24)
Next, from
ln ht+1 = α0 + α1 ln ht + at+1,
we deﬁne yt+1 = ln ht+1 −α0, xt+1 = α1, and bt+1 = at+1 and obtain
yt+1 = xt+1 ln ht+1 + bt+1.
(12.25)
Now Eqs. (12.24) and (12.25) form a special simple linear regression with two
observations and an unknown parameter ln ht. Note that bt and bt+1 have the
same distribution because −at is also N(0, σ 2
v ). The least-squares estimate of ln ht
is then
)
ln ht = xtyt + xt+1yt+1
x2
t + x2
t+1
= α0(1 −α1) + α1(ln ht+1 + ln ht−1)
1 + α2
1
,
which is precisely the conditional mean of ln ht given in Eq. (12.23). In addition,
this estimate is normally distributed with mean ln ht and variance σ 2
v /(1 + α2
1). Formula (12.23) is simply the product of at ∼N(0, ht) and )
ln ht ∼N[ln ht, σ 2
v /(1 +
α2
1)] with the transformation d ln ht = h−1
t
dht. This regression approach generalizes easily to other AR(p) models for ln ht. We use this approach and assume that
{ht}p
t=1 are ﬁxed for a stochastic volatility AR(p) model.
□
Remark.
Starting value of ht can be obtained by ﬁtting a volatility model of
Chapter 3 to the return series.
□
Example 12.3.
Consider the monthly log returns of the S&P 500 index from
January 1962 to December 2009 for 575 observations. The returns are computed
using the ﬁrst adjusted closing index of each month, that is, the closing index
of the ﬁrst trading day of each month. Figure 12.4(a) shows the time plot of the
log level of the index, whereas Figure 12.4(b) shows the log returns measured in
percentage. If GARCH models are entertained for the series, we obtain a Gaussian
GARCH(1,1) model
rt = 0.552 + at,
at =

htϵt,
ht = 0.878 + 0.125a2
t−1 + 0.837ht−1,
(12.26)
where t ratios of the coefﬁcients are all greater than 2.56. The Ljung–Box statistics
of the standardized residuals and their squared series fail to indicate any model inadequacy. Speciﬁcally, we have Q(12) = 10.04(0.61) and 6.14(0.91), respectively,
for the standardized residuals and their squared series.
--- page 668 ---

stochastic volatility models
641
Year
lnsp5
1970
1980
1990
2000
2010
4
5
6
7
Year
(a)
(b)
Returns
1970
1980
1990
2000
2010
−20 −10
0
10
Figure 12.4
Time plot of monthly S&P 500 index from 1962 to 2009: (a) log level and (b) log return
in percentage.
Next, consider the stochastic volatility model
rt = µ + at,
at =

htϵt,
ln ht = α0 + α1 ln ht−1 + vt,
(12.27)
where the vt are iid N(0, σ 2
v ). To implement the Gibbs sampling, we use the prior
distributions
µ ∼N(0, 4),
α ∼N[αo, diag(0.25, 0.04)],
10 × 0.1
σ 2v
∼χ2
10,
where αo = (0, 0.6)′. For initial parameter values, we use the ﬁtted values of the
GARCH(1,1) model in Eq. (12.26) for {ht}, that is, h0t = ht, and set α and σ 2
v
to the least-squares estimate of ln(h0t). The initial value of µ is the sample mean
of the log returns. The volatility ht is drawn by the Griddy Gibbs with 400 grid
points. The possible range of ht for the jth Gibbs iteration is [η1t, η2t], where
η1t = 0.6 × max(hj−1,t, h0t) and η2t = 1.4 × min(hj−1,t, h0t), where hj−1,t and
h0t denote, respectively, the estimate of ht for the (j −1)th iteration and initial
value.
We ran the Gibbs sampling for 2500 iterations but discarded results of the ﬁrst
500 iterations. Figure 12.5 shows the density functions of the prior and posterior
--- page 669 ---

642
markov chain monte carlo methods with applications
−5
0
5
0
1
2
3
4
5
6
7
µ
Density
0
1
2
3
4
5
6
Density
−2
−1
0
2
1
α0
−0.5
0
0.5
1.0
1.5
0
5
10
15
α1
Density
0.0
0.2
0.4
0.6
0.8
1.0
0 10
30
50
σv
2
Density
Figure 12.5
Density functions of prior and posterior distributions of parameters in stochastic volatility
model for monthly log returns of S&P 500 index. Dashed line denotes prior density and solid line the
posterior density, which is based on results of Gibbs sampling with 2000 iterations. See text for more
details.
distributions of the four coefﬁcient parameters. The prior distributions used are
relatively noninformative. The posterior distributions are concentrated especially
for µ and σ 2
v . Figure 12.6 shows the time plots of ﬁtted volatilities. The upper
panel shows the posterior mean of ht over the 5000 iterations for each time point,
whereas the lower panel shows the ﬁtted values of the GARCH(1,1) model in Eq.
(12.26). The two plots exhibit a similar pattern.
The posterior mean and standard error of the four coefﬁcients are as follows:
Parameter
µ
α0
α1
σ 2
v
Mean
0.409
0.454
0.837
0.086
Standard error
0.157
0.068
0.025
0.007
The posterior mean of α1 is 0.837, conﬁrming strong serial dependence in the
volatility series. This value is smaller than that obtained by Jacquier, Polson, and
Rossi (1994) who used daily returns of the S&P 500 index. Finally, we have used
different initial values, priors, and numbers of iterations for the Gibbs sampler. The
--- page 670 ---

stochastic volatility models
643
Year
GARCH(1,1)
1970
1980
1990
2000
2010
20 40 60 80 100
sv-ht
Year
1970
1980
1990
2000
2010
20 40 60 80 100
Figure 12.6
Time plots of ﬁtted volatilities for monthly log returns of S&P 500 index from 1962 to
2009. Lower panel shows posterior means of a Gibbs sampler with 2000 iterations. Upper panel shows
results of a Gaussian GARCH(1,1) model.
results are stable. Of course, as expected, the results and efﬁciency of the Griddy
Gibbs algorithm depend on the speciﬁcation of the range for ht.
12.7.2
Multivariate Stochastic Volatility Models
In this section, we study multivariate stochastic volatility models using the Cholesky
decomposition of Chapter 10. We focus on the bivariate case, but the methods
discussed also apply to the higher dimensional case. Based on the Cholesky decomposition, the innovation at of a return series rt is transformed into bt such that
b1t = a1t,
b2t = a2t −q21,tb1t,
where b2t and q21,t can be interpreted as the residual and least-squares estimate of
the linear regression
a2t = q21,ta1t + b2t.
The conditional covariance matrix of at is parameterized by {g11,t, g22,t} and {q21,t}
as

 σ11,t
σ12,t
σ21,t
σ22,t

=

1
0
q21,t
1

 g11,t
0
0
g22,t

 1
q21,t
0
1

,
(12.28)
--- page 671 ---

644
markov chain monte carlo methods with applications
where gii,t = Var(bit|Ft−1) and b1t ⊥b2t. Thus, the quantities of interest are
g11,t, g22,t and q21,t.
A simple bivariate stochastic volatility model for the return rt = (r1t, r2t)′ is as
follows:
rt = β0 + β1xt + at,
(12.29)
ln gii,t = αi0 + αi1 ln gii,t−1 + vit,
i = 1, 2,
(12.30)
q21,t = γ0 + γ1q21,t−1 + ut,
(12.31)
where {at} is a sequence of serially uncorrelated Gaussian random vectors with
mean zero and conditional covariance matrix t given by Eq. (12.28), β0 is a
two-dimensional constant vector, xt denotes the explanatory variables, and {v1t},
{v2t}, and {ut} are three independent Gaussian white noise series such that Var(vit)
= σ 2
iv and Var(ut) = σ 2
u. Again log transformation is used in Eq. (12.30) to ensure
the positiveness of gii,t.
Let Gi = (gii,1, . . . , gii,n)′, G = [G1, G2], and Q = (q21,1, . . . , q21,n)′. The
“traditional” parameters of the model in Eqs. (12.29)–(12.31) are β = (β0, β1),
αi = (αi0, αi1)′, and σ 2
iv for i = 1, 2, and γ = (γ0, γ1)′ and σ 2
u. The augmented
parameters are Q, G1, and G2. To estimate such a bivariate stochastic volatility
model via Gibbs sampling, we use results of the univariate model in the previous
section and two additional conditional posterior distributions. Speciﬁcally, we can
draw random samples of
1. β0 and β1 row by row using the result (12.22)
2. g11,t using Eq. (12.23) with at being replaced by a1t
3. α1 and σ 2
1v using exactly the same methods as those of the univariate case
with at replaced by a1t
To draw random samples of α2, σ 2
2v, and g22,t, we need to compute b2t. But
this is easy because b2t = a2t −q21,ta1t given the augmented parameter vector Q.
Furthermore, b2t is normally distributed with mean 0 and conditional variance g22,t.
It remains to consider the conditional posterior distributions
f (γ |Q, σ 2
u),
f (σ 2
u|Q, γ ),
f (q21,t|A, G, Q−t, γ , σ 2
u),
where A denotes the collection of at, which is known if R, X, β0, and β1 are given.
Given Q and σ 2
u, model (12.31) is a simple Gaussian AR(1) model. Therefore, if
the prior distribution of γ is bivariate normal with mean γ o and covariance matrix
Do, then the conditional posterior distribution of γ is also bivariate normal with
mean γ ∗and covariance matrix D∗, where
D−1
∗
=
n
t=2 ztz′
t
σ 2u
+ D−1
o ,
γ ∗= D∗
n
t=2 ztq21,t
σ 2u
+ D−1
o γ o

,
--- page 672 ---

stochastic volatility models
645
where zt = (1, q21,t−1)′. Similarly, if the prior distribution of σ 2
u is (mλ)/σ 2
u ∼χ2
m,
then the conditional posterior distribution of σ 2
u is
mλ + n
t=2 u2
t
σ 2u
∼χ2
m+n−1,
where ut = q21,t −γ0 −γ1q21,t−1. Finally,
f (q21,t|A, G, Q−t, σ 2
u, γ )
∝f (b2t|g22,t)f (q21,t|q21,t−1, γ , σ 2
u)f (q21,t+1|q21,t, γ , σ 2
u)
∝g−0.5
22,t exp[−(a2t −q21,ta1t)2/(2g22,t)] exp[−(q21,t −µt)2(2σ 2)],
(12.32)
where µt = [γ0(1 −γ1) + γ1(q21,t−1 + q21,t+1)]/(1 + γ 2
1 ) and σ 2 = σ 2
u/(1 + γ 2
1 ).
In general, µt and σ 2 can be obtained by using the results of a missing value in an
AR(p) process. It turns out that Eq. (12.32) has a closed-form distribution for q21,t.
Speciﬁcally, the ﬁrst term of Eq. (12.32), which is the conditional distribution of
q21,t given g22,t and at, is normal with mean a2t/a1t and variance g22,t/(a1t)2. The
second term of the equation is also normal with mean µt and variance σ 2. Consequently, by Result 12.1, the conditional posterior distribution of q21,t is normal
with mean µ∗and variance σ 2
∗, where
1
σ 2∗
= a2
1t
g22,t
+ 1 + γ 2
1
σ 2u
,
µ∗= σ 2
∗

1 + γ 2
1
σ 2u
× µt + a2
1t
g22,t
× a2t
a1t

where µt is deﬁned in Eq. (12.32).
Example 12.4.
In this example, we study bivariate volatility models for the
monthly log returns of IBM stock and the S&P 500 index from January 1962
to December 2009. This is an expanded version of Example 12.3 by adding the
IBM returns. Figure 12.7 shows the time plots of the two return series. Let rt =
(IBMt, SPt)′. If time-varying correlation GARCH models with Cholesky decomposition of Chapter 10 are entertained, we obtain the model
rt = β0 + at,
(12.33)
g11,t = α10 + α11g11,t−1 + α12a2
1,t−1,
(12.34)
g22,t = α20 + α22b2
2,t−1,
(12.35)
q21,t = γ0,
(12.36)
where b2t = a2t −q21,ta1t and the estimates and their standard errors are given in
Table 12.2(a). For comparison purpose, we also ﬁt a BEKK(1,1) model and obtain
β0 = (0.70, 0.54)′ and the coefﬁcient matrices
A =

 0.80
0.83
0.01

,
A1 =

0.07
0.33
−0.06
0.43

,
B1 =

 1.00
−0.12
0.01
0.90

,
where the matrices are deﬁned in Eq. (10.6) of Chapter 10.
--- page 673 ---

646
markov chain monte carlo methods with applications
Year
(a)
Log returns
1970
1980
1990
2000
2010
−30
−10 0 10 20 30
Log returns
−20 −10
0
10
Year
(b)
1970
1980
1990
2000
2010
Figure 12.7
Time plots of monthly log returns of (a) IBM stock and (b) S&P 500 index from 1962
to 2009.
For stochastic volatility model, we employ the same mean equation in Eq.
(12.33) and a stochastic volatility model similar to that in Eqs. (12.34)–(12.36).
The volatility equations are
ln g11,t = α10 + α11 ln g11,t−1 + v1t,
Var(v1t) = σ 2
1v,
(12.37)
ln g22,t = α20 + α21 ln g22,t−1 + v2t,
Var(v2t) = σ 2
2v,
(12.38)
q21,t = γ0 + ut,
Var(ut) = σ 2
u.
(12.39)
The prior distributions used are
βi0 ∼N(0, 4),
αi ∼N[(0, 0.7)′, diag(0.25, 0.04)],
γ0 ∼N(0, 1),
10 × 0.1
σ 2
iv
∼χ2
10,
5 × 0.2
σ 2u
∼χ2
5,
where i = 1 and 2. These prior distributions are relatively noninformative. We
obtained the initial values of {g11,t, g22,t, q21,t} from the results of the BEKK(1,1)
model. In addition, we set the values of quantities at t = 1 as given. We then
ran the Gibbs sampling for 2500 iterations but discarded results of the ﬁrst 500
iterations. The random samples of gii,t were drawn by Griddy Gibbs with 500 grid
points in the intervals [ηi,1t, ηi,2t] where the lower and upper bounds are set by
--- page 674 ---

stochastic volatility models
647
TABLE 12.2
Estimation of Bivariate Volatility Models for Monthly Log Returns of
IBM Stock and S&P 500 Index from January 1962 to December 2009a
(a) Bivariate GARCH(1,1) Model With Time-Varying Correlations
Parameter
β01
β02
α10
α11
α12
α20
α22
γ0
Estimate
0.69
0.49
3.98
0.80
0.12
10.67
0.12
0.37
Standard error
0.30
0.18
1.22
0.04
0.03
0.53
0.04
0.01
(b) Stochastic Volatility Model
Parameter
β01
β02
α10
α11
σ 2
1v
α20
α21
σ 2
2v
γ0
σ 2
u
Posterior mean
0.53
0.51
0.75
0.80
0.07
0.43
0.81
0.07
0.38
0.07
Standard error
0.26
0.17
0.11
0.03
0.01
0.06
0.03
0.01
0.03
0.01
aThe stochastic volatility models are based on the last 2000 iterations of a Gibbs sampling with 2500
total iterations.
the same method as those of Example 12.3. Posterior means and standard errors of
the “traditional” parameters of the bivariate stochastic volatility model are given
in Table 12.2(b).
To check for convergence of the Gibbs sampling, we ran the procedure several
times with different starting values and numbers of iterations. The results are stable.
For illustration, Figure 12.8 shows the scatterplots of various quantities for two
different Gibbs samples. The ﬁrst Gibbs sample is based on 500 + 2000 iterations,
and the second Gibbs sample is based on 500 + 1000 iterations, where M + N
denotes that the total number of Gibbs iterations is M + N, but results of the
ﬁrst M iterations are discarded. The scatterplots shown are posterior means of
g11,t, g22,t, g21,t, σ22,t, σ21,t, and the correlation ρ21,t. The line y = x is added to
each plot to show the closeness of the posterior means. The stability of the Gibbs
sampling results is clearly seen.
It is informative to compare the BEKK model and the GARCH model with timevarying correlations in Eqs. (12.33)–(12.36) with the stochastic volatility model.
First, as expected, the mean equations of the three models are essentially identical. Second, Figure 12.9 shows the time plots of the conditional variance for
IBM stock return. Figure 12.9(a) is for the GARCH model, Figure 12.9(b) is from
the BEKK model, and Figure 12.9(c) shows the posterior mean of the stochastic volatility model. The three models show similar volatility characteristics; they
exhibit volatility clustering and indicate an increasing trend in volatility. However, the GARCH model produces higher peak volatility values and an additional
peak in 1993. Third, Figure 12.10 shows the time plots of conditional variance
for the S&P 500 index return. The GARCH model produces an extra volatility
peak around 1993. This additional peak does not appear in the univariate analysis shown in Figure 12.6. It seems that for this particular instance the bivariate
GARCH model produces a spurious volatility peak. This spurious peak is induced
by its dependence on IBM returns and does not appear in the stochastic volatility
model or the BEKK model. Indeed, the ﬁtted volatilities of the S&P 500 index
--- page 675 ---

648
markov chain monte carlo methods with applications
g11
1000 iterations
20
40
60
80 100
20
40
60
80
100
g22
1000 iterations
5
10
15
20
25
5
10
15
20
25
q21
1000 iterations
0.0 0.2 0.4 0.6 0.8
0.0
0.2
0.4
0.6
0.8
σ21
1000 iterations
0
10 20 30 40 50
0
10 20 30 40 50
σ22
1000 iterations
10
20
30
40
10
20
30
40
ρ
1000 iterations
0.0 0.2 0.4 0.6 0.8
0.0 0.2 0.4 0.6 0.8
Figure 12.8
Scatterplots of posterior means of various statistics of two different Gibbs samples for
bivariate stochastic volatility model for monthly log returns of IBM stock and S&P 500 index. The x
axis denotes results based on 500 + 2000 iterations and the y axis denotes results based on 500 + 1000
iterations. Notation is deﬁned in text.
return by the bivariate stochastic volatility model are similar to that of the univariate analysis. Fourth, Figure 12.11 shows the time plots of ﬁtted conditional
correlations. Here the three models differ substantially. The correlations of the
GARCH model with Cholesky decomposition are relatively smooth and always
positive with mean value 0.59 and standard deviation 0.07. The range of the correlations is (0.411,0.849). The correlations of the BEKK(1,1) model assume small
negative values around 1993 and are more variable with mean 0.59, standard deviation 0.13 and range (−0.020, 0.877). However, the correlations produced by the
stochastic volatility model vary markedly from one month to another with mean
value 0.60, standard deviation 0.14, and range (−0.161, 0.839). Furthermore, the
negative correlations occur in several isolated periods. The difference is understandable because q21,t contains the random shock ut in the stochastic volatility
model.
Remark.
The Gibbs sampling estimation applies to other bivariate stochastic volatility models. The conditional posterior distributions needed require some
extensions of those discussed in this section, but they are based on the same ideas.
The BEKK model is estimated by using Matlab.
□
--- page 676 ---

new approach to sv estimation
649
Year
(a)
s11.t
1970
1980
1990
2000
2010
50
100 150 200
s11.t
20 40 60 80 100120140
s11.t
20
40
60
80 100
Year
(b)
1970
1980
1990
2000
2010
Year
(c)
1970
1980
1990
2000
2010
Figure 12.9
Time plots of ﬁtted conditional variance for monthly log returns of IBM stock from 1962
to 2009: (a) GARCH model with time-varying correlations, (b) BEKK(1,1) model, and (c) bivariate
stochastic volatility model estimated by Gibbs sampling with 500 + 2000 iterations.
12.8
NEW APPROACH TO SV ESTIMATION
In this section, we discuss an alternative procedure to estimate stochastic volatility
(SV) models. This approach makes use of the technique of forward ﬁltering and
backward sampling (FFBS) within the Kalman ﬁlter framework to improve the
efﬁciency of Gibbs sampling. It can dramatically reduce the computing time by
drawing the volatility process jointly with the help of a mixture of normal distributions. In fact, the approach can be used to estimate many stochastic diffusion
models with leverage effects and jumps.
For ease in presentation, we reparameterize the univariate stochastic volatility
model in Eqs. (12.20) and (12.21) as
rt = x′
tβ + σ0 exp
zt
2

ϵt,
(12.40)
zt+1 = αzt + ηt,
(12.41)
--- page 677 ---

650
markov chain monte carlo methods with applications
Year
(a)
s22.t
1970
1980
1990
2000
2010
20 40 60 80 100
Year
(b)
s22.t
1970
1980
1990
2000
2010
20 40 60 80 100
Year
(c)
s22.t
1970
1980
1990
2000
2010
20 40 60 80 100
Figure 12.10
Time plots of conditional variance for monthly log returns of S&P 500 index from 1962
to 2009: (a) GARCH model with time-varying correlations, (b) BEKK(1,1) model, and (c) bivariate
stochastic volatility model estimated by Gibbs sampling with 500 + 2000 iterations.
where xt = (1, x1t, . . . , xpt)′, β = (β0, β1, . . . , βp)′, σ0 > 0, {zt} is a zero-mean
log volatility series, and {ϵt} and {ηt} are bivariate normal distributions with mean
zero and covariance matrix
 =

1
ρση
ρση
σ 2
η

.
The parameter ρ is the correlation between ϵt and ηt and represents the leverage
effect of the asset return rt. Typically, ρ is negative signifying that a negative return
tends to increase the volatility of an asset price.
Compared with the model in Eqs. (12.22) and (12.20), we have zt =
ln(ht) −ln(σ 2
0 ) and σ 2
0 = exp{E[ln(ht)]}. That is, zt is a mean-adjusted log volatility series. This new parameterization has some nice characteristics. For example,
the volatility series is σ0 exp(zt/2), which is always positive. More importantly, ηt
is the innovation of zt+1 and is independent of zt. This simple time shift enables
us to handle the leverage effect. If one postulates zt = αzt−1 + ηt for Eq. (12.41),
then ηt and ϵt cannot be correlated because a nonzero correlation implies that zt
and ϵt are correlated in Eq. (12.40), which would lead to some identiﬁability issues.
--- page 678 ---

new approach to sv estimation
651
Year
(a)
corr
1970
1980
1990
2000
2010
−0.20.0 0.2 0.4 0.6 0.8 1.0
Year
(b)
corr
1970
1980
1990
2000
2010
−0.20.0 0.2 0.4 0.6 0.8 1.0
Year
(c)
corr
1970
1980
1990
2000
2010
−0.20.0 0.2 0.4 0.6 0.8 1.0
Figure 12.11
Time plots of ﬁtted correlation coefﬁcients between monthly log returns of IBM stock
and S&P 500 index from 1962 to 2009: (a) GARCH model with time-varying correlations, (b)
BEKK(1,1) model, and (c) bivariate stochastic volatility model estimated by Gibbs sampling with
500 + 2000 iterations.
Remark.
Alternatively, one can write the stochastic volatility model as
rt = x′
tβ + σ0 exp
zt−1
2

ϵt,
zt = αzt−1 + ηt,
where (ϵt, ηt)′ is a bivariate normal distribution as before. Yet another equivalent
parameterization is
rt = x′
tβ + exp
z∗
t−1
2

ϵt,
z∗
t = α0 + αz∗
t−1 + ηt,
where E(z∗
t ) = α0/(1 −α) is not zero.
□
Parameters of the stochastic volatility model in Eqs. (12.40) and (12.41) are
β, σ0, α, ρ, ση, and z = (z1, . . . , zn)′, where n is the sample size. For simplicity, we
--- page 679 ---

652
markov chain monte carlo methods with applications
assume z1 is known. To estimate these parameters via MCMC methods, we need
their conditional posterior distributions. In what follows, we discuss the needed
conditional posterior distributions.
1. Given z and σ0 and a normal prior distribution, β has the same conditional
posterior distribution as that in Section 12.7.1 with √ht replaced by σ0 exp(zt/2);
see Eq. (12.22).
2. Given z and σ 2
η , α is a simple AR(1) coefﬁcient. Thus, with an approximate
normal prior, the conditional posterior distribution of α is readily available; see
Section 12.7.1.
3. Given β and z, we deﬁne vt = (rt −x′
tβ) exp(−zt/2) = σ0ϵt. Thus, {vt}
is a sequence of iid normal random variables with mean zero and variance σ 2
0 .
If the prior distribution of σ 2
0 is (mλ)/σ 2
0 ∼χ2
m, then the conditional posterior
distribution of σ 2
0 is an inverted chi-squared distribution with m + n degrees of
freedom; that is,
mλ + n
t=1 v2
t
σ 2
0
∼χ2
m+n.
4. Given β, σ0, z, and α, we can easily obtain the bivariate innovation bt =
(ϵt, ηt)′ for t = 2, . . . , n. The likelihood function of (ρ, σ 2
η ) is readily available as
ℓ(ρ, σ 2
η ) =
n

t=2
f (bt|) ∝||−(n−1)/2 exp

−1
2
n

t=2
b′
t−1bt

∝||−(n−1)/2 exp

−1
2tr

−1
n

t=2
btb′
t

,
where tr(A) denotes trace of the matrix A. However, this joint distribution is
complicated because one cannot separate ρ and σ 2
η . We adopt the technique of
Jacquier, Polson, and Rossi (2004) and reparameterize the covariance matrix as
 =

1
ρση
ρση
σ 2
η

=

 1
ϕ
ϕ
ω + ϕ2

,
where ω = σ 2
η (1 −ρ2). It is easy to see that || = ω and
−1 = 1
ω

ϕ2
−ϕ
−ϕ
1

+

 1
0
0
0

≡1
ωS +

 1
0
0
0

,
where S contains ϕ only. Let e = (ϵ2, . . . , ϵn)′ and η = (η2, . . . , ηn)′ be the innovations of the model in Eqs. (12.40) and (12.41). The likelihood function then
becomes (keeping terms related to parameters only)
ℓ(ϕ, ω) ∝ω−(n−1)/2 exp

−1
2ωtr(SR)

,
--- page 680 ---

new approach to sv estimation
653
where R = n
t=2 btb′
t = (e, η)′(e, η), which is the 2 × 2 cross-product matrix of
the innovations. For simplicity, we use conjugate priors such that ω is inverse
gamma (IG) with hyperparameters (γ0/2, γ1/2); that is, ω ∼IG(γ0/2, γ1/2), and
ϕ|ω ∼N(0, ω/2). Then, after some algebraic manipulation, the joint posterior
distribution of (ϕ, ω) can be decomposed into a normal and an inverse gamma
distribution. Speciﬁcally,
ϕ ∼N

˜ϕ,
ω
(2 + e′e)

,
where ˜ϕ = e′η/(2 + e′e), and
ω ∼IG

1
2 (n + 1 + γ0) , 1
2

γ1 + η′η −(e′η)2
2 + e′e
	
.
In Gibbs sampling, once ϕ and ω are available, we can obtain ρ and σ 2
η easily
because σ 2
η = ω + ϕ2 and ρ = ϕ/ση. Note that the probability density function of
an IG(α, β) random variable ω is
f (ω|α, β) =
βα
(α)ω−(α+1) exp

−β
ω

,
for ω > 0,
where α > 2 and β > 0.
5. Finally, we consider the joint distribution of the log volatility z given the
data and other parameters. From Eq. (12.40), we have
(rt −x′
tβ)2
σ 2
0
= exp(zt)ϵ2
t .
Therefore, letting yt = ln[(rt −x′
tβ)2/σ 2
0 ], we obtain
yt = zt + ϵ∗
t ,
(12.42)
where ϵ∗
t = ln(ϵ2
t ). Since ϵ2
t ∼χ2
1, ϵ∗
t is not normally distributed. Treating Eq.
(12.42) as an observation equation and Eq. (12.40) as the state equation, we have
the form of a state-space model except that ϵ∗
t is not Gaussian; see Eqs. (11.26) and
(11.27). To overcome the difﬁculty associated with nonnormality, Kim, Shephard,
and Chib (1998) use a mixture of seven normal distributions to approximate the
distribution of ϵ∗
t . Speciﬁcally, we have
f (ϵ∗
t ) ≈
7

i=1
piN(µi, ω2
i ),
where pi, µi, and ϖ 2
i are given in Table 12.3. See also Chib, Nardari, and Shephard
(2002).
--- page 681 ---

654
markov chain monte carlo methods with applications
TABLE 12.3
Seven Components of Normal Distributions
Component i
Probability pi
Mean µi
var. ω2
i
1
0.00730
−11.4004
5.7960
2
0.10556
−5.2432
2.6137
3
0.00002
−9.8373
5.1795
4
0.04395
1.5075
0.1674
5
0.34001
−0.6510
0.6401
6
0.24566
0.5248
0.3402
7
0.25750
−2.3586
1.2626
x
Density
−25
 −20
 −15
−10
 −5
0
5
0.0
0.05
0.10
0.15
0.20
Figure 12.12
Density functions of log(χ2
1 ), solid line, and that of a mixture of seven normal distributions, dashed line. Results are based on 100,000 observations.
To demonstrate the adequacy of the approximation, Figure 12.12 shows the
density function of ϵ∗
t (solid line) and that of the mixture of seven normals (dashed
line) in Table 12.3. These densities are obtained using simulations with 100,000
observations. From the plot, the approximation by the mixture of seven normals is
very good.
Why is it important to have a Gaussian state-space model? The answer is that
such a Gaussian model enables us to draw the log volatility series z jointly and
efﬁciently. To see this, consider the following special Gaussian state-space model,
--- page 682 ---

new approach to sv estimation
655
where ηt and et are uncorrelated (i.e., no leverage effects):
zt+1 = αzt + ηt,
ηt ∼iid N(0, σ 2
η ),
(12.43)
yt = ct + zt + et,
et ∼ind. N(0, Ht),
(12.44)
where, as will be seen later, (ct, Ht) assumes the value (µi, ϖ 2
i ) of Table 12.3 for
some i. For this special state-space model, we have the Kalman ﬁlter algorithm
vt = yt −yt|t−1 = yt −ct −zt|t−1,
Vt = t|t−1 + Ht,
zt|t = zt|t−1 + t|t−1V −1
t
vt,
(12.45)
t|t = t|t−1 −t|t−1V −1
t
t|t−1,
zt+1|t = αzt|t,
t+1|t = α2t|t + σ 2
η ,
where Vt = Var(vt) is the variance of the 1-step-ahead prediction error vt of yt
given Ft−1 = (y1, . . . , yt−1), and zj|i and j|i are, respectively, the conditional
expectation and variance of the state variable zj given Fi. See the Kalman ﬁlter
discussion of Chapter 11.
Forward Filtering and Backward Sampling
Let p(z|Fn) be the joint conditional posterior distribution of z given the return
data and other parameters, where for simplicity the parameters are omitted from
the condition set. We can partition the distribution as
p(z|Fn) = P (z2, z3, . . . , zn|Fn)
= p(zn|Fn)p(zn−1|zn, Fn)p(zn−2|zn−1, zn, Fn) · · · p(z2|z3, . . . , zn, Fn)
= p(zn|Fn)p(zn−1|zn, Fn)p(zn−2|zn−1, Fn) · · · p(z2|z3, Fn),
(12.46)
where the last equality holds because zt in Eq. (12.43) is a Markov process so that
conditioned on zt+1, zt is independent of zt+j for j > 1.
From the Kalman ﬁlter in Eq. (12.45), we obtain that p(zn|Fn) is normal with
mean zn|n and variance n|n. Next, consider the second term p(zn−1|zn, Fn) of Eq.
(12.46). We have
p(zn−1|zn, Fn) = p(zn−1|zn, Fn−1, yn) = p(zn−1|zn, Fn−1, vn),
(12.47)
where vn = yn −yn|n−1 is the 1-step-ahead prediction error of yn. From the statespace model in Eqs. (12.43) and (12.44), zn−1 is independent of vn. Therefore,
p(zn−1|zn, Fn) = p(zn−1|zn, Fn−1).
(12.48)
--- page 683 ---

656
markov chain monte carlo methods with applications
This is an important property because it implies that we can derive the posterior distribution p(zn−1|zn, Fn) from the joint distribution of (zn−1, zn) given Fn−1
via Theorem 11.1. First, the joint distribution is bivariate normal under the Gaussian assumption. Second, the conditional mean and covariance matrix of (zn−1, zn)
given Fn−1 are readily available from the Kalman ﬁlter algorithm in Eq. (12.45).
Speciﬁcally, we have

 zn−1
zn

Fn−1
∼N

 zn−1|n−1
zn|n−1

,

n−1|n−1
αn−1|n−1
αn−1|n−1
n|n−1

,
(12.49)
where the covariance is obtained by (i) multiplying zn−1 by Eq. (12.43) and (ii)
taking conditional expectation. Note that all quantities involved in Eq. (12.49) are
available from the Kalman ﬁlter. Consequently, by Theorem 11.1, we have
p(zn−1|zn, Fn) ∼N(µ∗
n−1, ∗
n−1),
(12.50)
where
µ∗
n−1 = zn−1|n−1 + αn−1|n−1−1
n|n−1(zn −zn|n−1),
∗
n−1 = n−1|n−1 −α22
n−1|n−1−1
n|n−1.
Next, for the conditional posterior distribution p(zn−2|zn−1, Fn), we have
p(zn−2|zn−1, Fn) = p(zn−2|zn−1, Fn−2, yn−1, yn)
= p(zn−2|zn−1, Fn−2, vn−1, vn)
= p(zn−2|zn−1, Fn−2).
Consequently, we can obtain p(zn−2|zn−1, Fn) from the bivariate normal distribution of p(zn−2, zn−1|Fn−2) as before. In general, we have
p(zt|zt+1, Fn) = p(zt|zt+1, Ft),
for 1 < t < n.
Furthermore, from the Kalman ﬁlter, p(zt, zt+1|Ft) is bivariate normal as

zt
zt+1

Ft
∼N

zt|t
zt+1|t

,

t|t
αt|t
αt|t
t+1|t

.
(12.51)
Consequently,
p(zt|zt+1, Ft) ∼N(µ∗
t , ∗
t ),
where
µ∗
t = zt|t + αt|t−1
t+1|t(zt+1 −zt+1|t),
∗
t = t|t −α22
t|t−1
t+1|t.
--- page 684 ---

new approach to sv estimation
657
The prior derivation implies that we can draw the volatility series z jointly
by a recursive method using quantities readily available from the Kalman ﬁlter
algorithm. That is, given the initial values z1|0 and 1|0, one uses the Kalman
ﬁlter in Eq. (12.45) to process the return data forward, then applies the recursive
backward method to draw a realization of the volatility series z. This scheme is
referred to as forward ﬁltering and backward sampling (FFBS); see Carter and
Kohn (1994) and Fr¨uhwirth-Schnatter (1994). Because the volatility {zt} is serially
correlated, drawing the series jointly is more efﬁcient.
Remark.
The FFBS procedure applies to general linear Gaussian state-space
models. The main idea is to make use of the Markov property of the model and
the structure of the state transition equation so that
p(St|St+1, Fn) = p(St|St+1, Ft, vt+1, . . . , vn) = p(St|St+1, Ft),
where St denotes the state variable at time t and vj is the 1-step-ahead prediction
error. This identity enables us to apply Theorem 11.1 to derive a recursive method
to draw the state vectors jointly.
□
Return to the estimation of the SV model. As in Eq. (12.42), let yt = ln[(rt −
x′
tβ)2/σ 2
0 ]. To implement FFBS, one must determine ct and Ht of Eq. (12.44)
so that the mixture of normals provides a good approximation to the distribution
of ϵ∗
t . To this end, we augment the model with a series of independent indicator
variables {It}, where It assumes a value in {1, . . . , 7} such that P (It = i) = pit
with 7
i=1 pit = 1 for each t. In practice, conditioned on {zt}, we can determine
ct and Ht as follows. Let
qit = [(yt −zt −µi)/ϖi],
for i = 1, . . . , 7,
where µi and ϖi are the mean and standard error of the normal distributions given
in Table 12.3 and (·) denotes the cumulative distribution function of the standard
normal random variable. These probabilities qit are the likelihood function of It
given yt and zt. The probabilities pi of Table 12.3 form a prior distribution of It.
Therefore, the posterior distribution of It is
pit =
piqit
7
j=1 pjqjt
,
i = 1, . . . , 7.
We can draw a realization of It using this posterior distribution. If the random
draw is It = j, then we deﬁne ct = µj and Ht = ϖ 2
j . In summary, conditioned
on the return data and other parameters of the model, we employ the approximate
linear Gaussian state-space model in Eqs. (12.43) and (12.44) to draw jointly the
log volatility series z. It turns out that the resulting Gibbs sampling is efﬁcient in
estimating univariate stochastic volatility models.
--- page 685 ---

658
markov chain monte carlo methods with applications
On the other hand, the square transformation involved in Eq. (12.42) fails to
retain the correlation between ηt and ϵt if it exists, making the approximate statespace model in Eqs. (12.43) and (12.44) incapable of estimating the leverage effect.
To overcome this inadequacy, Artigas and Tsay (2004) propose using a time-varying
state-space model that maintains the leverage effect. Speciﬁcally, when ρ̸ = 0, we
have
ηt = ρσηϵt + η∗
t ,
where η∗
t is a normal random variable independent of ϵt and Var(η∗
t ) = σ 2
η (1 −ρ2).
The state transition equation of Eq. (12.43) then becomes
zt+1 = αzt + ρσηϵt + η∗
t .
Substituting ϵt = (1/σ0)(rt −x′
tβ) exp(−zt/2), we obtain
zt+1 = αzt + ρση(rt −x′
tβ)
σ0
exp
−zt
2

+ η∗
t
= G(zt) + η∗
t
(12.52)
where G(zt) = αzt + ρση(rt −x′
tβ) exp(−zt/2)/σ0. This is a nonlinear transition
equation for the state variable zt. The Kalman ﬁlter in Eq. (12.45) is no longer
applicable. To overcome this difﬁculty, Artigas and Tsay (2004) use a time-varying
linear Kalman ﬁlter to approximate the system. Speciﬁcally, the last two equations
of Eq. (12.45) are modiﬁed as
zt+1|t = G(zt|t),
t+1|t = g(zt|t)2t|t + σ 2
η (1 −ρ2),
(12.53)
where g(zt|t) = ∂G(x)/∂x|x=zt|t is the ﬁrst-order derivative of G(zt) evaluated at
the smoothed state zt|t.
Example 12.5.
To demonstrate the FFBS procedure, we consider the monthly
log returns of the S&P 500 index from January 1962 to November 2004 for 515
observations. This is a subseries of the data used in Example 12.3. See Figure 12.4
for time plots of the index and its log return. We consider two stochastic volatility
models in the form:
rt = µ + σo exp(zt/2)ϵt,
ϵt ∼iid N(0, 1),
(12.54)
zt+1 = αzt + ηt,
ηt ∼iid N(0, σ 2
η ).
In model 1, {ϵt} and {ηt} are two independent Gaussian white noise series. That
is, there is no leverage effect in the model. In model 2, we assume that corr(ϵt, et)
= ρ, which denotes the leverage effect.
