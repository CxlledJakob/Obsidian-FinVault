# Analysis of Financial Time Series, Third Edition (Wiley -- Ruey S_ Tsay -- Wiley series in probability and statistics, 3rd ed_, -- John Wiley & Sons, -- isbn13 9780470414354 -- 9f99b80c7b2dedd477f463dc5323f3b6 -- An.pdf — pages 685–704

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
--- page 686 ---

new approach to sv estimation
659
TABLE 12.4
Estimation of Stochastic Volatility Model in Eq. (12.54) for Monthly
Log Returns of S&P 500 Index from January 1962 to November 2004 Using Gibbs
Sampling with FFBS Algorithma
Parameter
µ
σo
α
ση
ρ
With Leverage Effect
Estimate
0.0081
0.0764
−0.0616
2.5639
−0.3892
Standard error
0.0274
0.0255
0.1186
0.3924
0.0292
Without Leverage Effect
Estimate
0.0080
0.0775
−0.0613
2.5827
Standard error
0.0279
0.0266
0.1164
0.3783
aThe results are based on 2000+8000 iterations with the ﬁrst 2000 iterations as burn-ins.
We estimate the models via the FFBS procedure using a program written in
Matlab. The Gibbs sampling was run for 2000+8000 iterations with the ﬁrst 2000
iterations as burn-ins. Table 12.4 gives the posterior means and standard errors of
the parameter estimates. In particular, we have ˆρ = −0.39, which is close to the
value commonly seen in the literature. Figure 12.13 shows the time plots of the
posterior means of the estimated volatility. As expected, the two volatility series
are very close. Compared with the results of Example 12.3, which uses a shorter
Year
(a)
Volatility
1970
1980
1990
2000
0.05
0.15
0.25
Year
(b)
Volatility
1970
1980
1990
2000
0.05
0.15
0.25
Figure 12.13
Estimated volatility of monthly log returns of S&P 500 index from January 1962 to
November 2004 using stochastic volatility models: (a) with leverage effect and (b) without leverage
effect.
--- page 687 ---

660
markov chain monte carlo methods with applications
series, the estimated volatility series exhibit similar patterns and are in the same
magnitude. Note that the volatility shown in Figure 12.6 is conditional variance
of percentage log returns whereas the volatility in Figure 12.13 is the conditional
standard error of log returns.
12.9
MARKOV SWITCHING MODELS
The Markov switching model is another econometric model for which MCMC
methods enjoy many advantages over the traditional likelihood method. McCulloch
and Tsay (1994b) discuss a Gibbs sampling procedure to estimate such a model
when the volatility in each state is constant over time. These authors applied the
procedure to estimate a Markov switching model with different dynamics and mean
levels for different states to the quarterly growth rate of U.S. real gross national
product, seasonally adjusted, and obtained some interesting results. For instance, the
dynamics of the growth rate are signiﬁcantly different between periods of economic
“contraction” and “expansion.” Since this chapter is concerned with asset returns,
we focus on models with volatility switching.
Suppose that an asset return rt follows a simple two-state Markov switching
model with different risk premiums and different GARCH dynamics:
rt =



β1
√ht +
√
htϵt,
ht = α10 + α11ht−1 + α12a2
t−1
if st = 1,
β2
√ht + √htϵt,
ht = α20 + α21ht−1 + α22a2
t−1
if st = 2,
(12.55)
where at = √htϵt, {ϵt} is a sequence of Gaussian white noises with mean zero
and variance 1, and the parameters αij satisfy some regularity conditions so that
the unconditional variance of at exists. The probability transition from one state to
another is governed by
P (st = 2|st−1 = 1) = e1,
P (st = 1|st−1 = 2) = e2,
(12.56)
where 0 < ei < 1. A small ei means that the return series has a tendency to stay
in the ith state with expected duration 1/ei. For the model in Eq. (12.55) to be
identiﬁable, we assume that β2 > β1 so that state 2 is associated with higher risk
premium. This is not a critical restriction because it is used to achieve uniqueness
in labeling the states. A special case of the model results if α1j = α2j for all j
so that the model assumes a GARCH model for all states. However, if βi
√ht is
replaced by βi, then model (12.55) reduces to a simple Markov switching GARCH
model.
Model (12.55) is a Markov switching GARCH-M model. For simplicity, we
assume that the initial volatility h1 is given with value equal to the sample variance
of rt. A more sophisticated analysis is to treat h1 as a parameter and estimate it
jointly with other parameters. We expect the effect of ﬁxing h1 will be negligible
in most applications, especially when the sample size is large. The “traditional”
--- page 688 ---

markov switching models
661
parameters of the Markov switching GARCH-M model are β = (β1, β2)′, αi =
(αi0, αi1, αi2)′ for i = 1 and 2, and the transition probabilities e = (e1, e2)′. The
state vector S = (s1, s2, . . . , sn)′ contains the augmented parameters. The volatility
vector H = (h2, . . . , hn)′ can be computed recursively if h1, αi, and the state
vector S are given.
Dependence of the return on volatility in model (12.55) implies that the return
is also serially correlated. The model thus has some predictability in the return.
However, states of the future returns are unknown and a prediction produced by
the model is necessarily a mixture of those over possible state conﬁgurations. This
often results in high uncertainty in point prediction of future returns.
Turn to estimation. The likelihood function of model (12.55) is complicated as it
is a mixture over all possible state conﬁgurations. Yet the Gibbs sampling approach
only requires the following conditional posterior distributions:
f (β|R, S, H, α1, α2),
f (αi|R, S, H, αj̸=i),
P (S|R, h1, α1, α2),
f (ei|S),
i = 1, 2,
where R is the collection of observed returns. For simplicity, we use conjugate
prior distributions discussed in Section 12.3—that is,
βi ∼N(βio, σ 2
io),
ei ∼Beta(γi1, γi2).
The prior distribution of parameter αij is uniform over a properly speciﬁed interval.
Since αij is a nonlinear parameter of the likelihood function, we use the Griddy
Gibbs to draw its random realizations. A uniform prior distribution simpliﬁes the
computation involved. Details of the prior conditional posterior distributions follow:
1. The posterior distribution of βi only depends on the data in state i. Deﬁne
rit =

rt/√ht
if st = i,
0
otherwise.
Then we have
rit = βi + ϵt,
for
st = i.
Therefore, information of the data on βi is contained in the sample mean of rit. Let
¯ri = (
st=i rit)/ni, where the summation is over all data points in state i and ni
is the number of data points in state i. Then the conditional posterior distribution
of βi is normal with mean β∗
i and variance σ 2
i∗, where
1
σ 2
i∗
= ni + 1
σ 2
io
,
β∗
i = σ 2
i∗

ni ¯ri + βio/σ 2
io

,
i = 1, 2.
--- page 689 ---

662
markov chain monte carlo methods with applications
2. Next, the parameters αij can be drawn one by one using the Griddy Gibbs
method. Given h1, S, αv̸=i, and αiv with v̸ = j, the conditional posterior distribution function of αij does not correspond to a well-known distribution, but it can
be evaluated easily as
f (αij|.) ∝−1
2

ln ht + (rt −βi
√ht)2
ht

,
if
st = i,
where ht contains αij. We evaluate this function at a grid of points for αij over a
properly speciﬁed interval. For example, 0 ≤α11 < 1 −α12.
3. The conditional posterior distribution of ei only involves S. Let ℓ1 be the
number of switches from state 1 to state 2 and ℓ2 be the number of switches from
state 2 to state 1 in S. Also, let ni be the number of data points in state i. Then
by Result 12.3 of conjugate prior distributions, the posterior distribution of ei is
Beta(γi1 + ℓi, γi2 + ni −ℓi).
4. Finally, elements of S can be drawn one by one. Let S−j be the vector
obtained by removing sj from S. Given S−j and other information, sj can assume
two possibilities (i.e., sj = 1 or sj = 2), and its conditional posterior distribution is
P (sj|.) ∝
n

t=j
f (at|H)P (sj|S−j).
The probability
P (sj = i|S−j) = P (sj = i|sj−1, sj+1),
i = 1, 2
can be computed by the Markov transition probabilities in Eq. (12.56). In addition,
assuming sj = i, one can compute ht for t ≥j recursively. The relevant likelihood
function, denoted by L(sj), is given by
L(sj = i) ≡
n

t=j
f (at|H) ∝exp(fji),
fji =
n

t=j
−1
2

ln(ht) + a2
t
ht

,
for i = 1 and 2, where at = rt −β1
√ht if st = 1 and at = rt −β2
√ht otherwise.
Consequently, the conditional posterior probability of sj = 1 is
P (sj = 1|·) =
P (sj = 1|sj−1, sj+1)L(sj = 1)
P (sj = 1|sj−1, sj+1)L(sj = 1) + P (sj = 2|sj−1, sj+1)L(sj = 2).
The state sj can then be drawn easily using a uniform distribution on the unit
interval [0, 1].
--- page 690 ---

markov switching models
663
Remark.
Since sj and sj+1 are highly correlated when e1 and e2 are small, it
is more efﬁcient to draw several sj jointly. However, the computation involved in
enumerating the possible state conﬁgurations increases quickly with the number of
states drawn jointly.
□
Example 12.6.
In this example, we consider the monthly log stock returns of
General Electric Company from January 1926 to December 1999 for 888 observations. The returns are in percentages and shown in Figure 12.14(a). For comparison
purposes, we start with a GARCH-M model for the series and obtain
rt = 0.182

ht + at,
at =

htϵt,
ht = 0.546 + 1.740ht−1 −0.775ht−2 + 0.025a2
t−1,
(12.57)
where rt is the monthly log return and {ϵt} is a sequence of independent Gaussian
white noises with mean zero and variance 1. All parameter estimates are highly
signiﬁcant with p values less than 0.0006. The Ljung–Box statistics of the standardized residuals and their squared series fail to suggest any model inadequacy. It
Year
(a)
Returns
1940
1960
1980
2000
−40 −20
0
20
40
Probability
0.0 0.2 0.4 0.6 0.8 1.0
Year
(b)
1940
1960
1980
2000
···
······
···
··
············
····
·
·
·
·
·
····
·
·····
········
·····
··
·
···
·····
·····
····
····
····
··
·
·
··
·
·
················
·
··
·········
·
···
·····
·····
···
·
·
······
·············
·
··
·
·········
·
··
·
·········
·
········
····
·
····
···
··
····
·
····
·······
··
·····
···
···
·
·
·
·
···
·······
·····
·
··
·
··
·
····
··
·····
··
····
·····
··
····
···
·
·····
······
··········
···
·
·
···
·
·
··
·
Figure 12.14
(a) Time plot of monthly log returns, in percentages, of GE stock from 1926 to 1999.
(b) Time plot of the posterior probability of being in state 2 based on results of last 2000 iterations
of Gibbs sampling with 5000 + 2000 total iterations. Model used is two-state Markov switching
GARCH-M model.
--- page 691 ---

664
markov chain monte carlo methods with applications
is reassuring to see that the risk premium is positive and signiﬁcant. The GARCH
model in Eq. (12.57) can be written as
(1 −1.765B + 0.775B2)a2
t = 0.546 + (1 −0.025B)ηt,
where ηt = a2
t −ht and B is the back-shift operator such that Ba2
t = a2
t−1. As
discussed in Chapter 3, the prior equation can be regarded as an ARMA(2,1) model
with nonhomogeneous innovations for the squared series a2
t . The AR polynomial
can be factorized as (1 −0.945B)(1 −0.820B), indicating two real characteristic
roots with magnitudes less than 1. Consequently, the unconditional variance of rt
is ﬁnite and equal to 0.546/(1 −1.765 + 0.775) ≈49.64.
Turn to Markov switching models. We use the following prior distributions:
β1 ∼N(0.3, 0.09),
β2 ∼N(1.3, 0.09),
ϵi ∼Beta(5, 95).
The initial parameter values used are (a) ei = 0.1, (b) s1 is a Bernoulli trial with
equal probabilities and st is generated sequentially using the initial transition probabilities, and (c) α1 = (1.0, 0.6, 0.2)′ and α2 = (2, 0.7, 0.1)′. Gibbs samples of αij
are drawn using the Griddy Gibbs with 400 grid points, equally spaced over the
following ranges: αi0 ∈[0, 6.0], αi1 ∈[0, 1], and αi2 ∈[0, 0.5]. In addition, we
implement the constraints αi1 + αi2 < 1 for i = 1, 2. The Gibbs sampler is run
for 5000 + 2000 iterations, but only results of the last 2000 iterations are used to
make inference.
Table 12.5 shows the posterior means and standard deviations of parameters
of the Markov switching GARCH-M model in Eq. (12.55). In particular, it also
contains some statistics showing the difference between the two states such as
θ = β2 −β1. The difference between the risk premiums is statistically signiﬁcant
at the 5% level. The differences in posterior means of the volatility parameters
between the two states appear to be insigniﬁcant. Yet the posterior distributions of
volatility parameters show some different characteristics. Figures 12.15 and 12.16
show the histograms of all parameters in the Markov switching GARCH-M model.
They exhibit some differences between the two states. Figure 12.17 shows the
time plot of the persistent parameter αi1 + αi2 for the two states. It shows that the
persistent parameter of state 1 reaches the boundary 1.0 frequently, but that of state
2 does not. The expected durations of the two states are about 11 and 9 months,
respectively. Figure 12.14(b) shows the posterior probability of being in state 2 for
each observation.
Finally, we compare the ﬁtted volatility series of the simple GARCH-M model
in Eq. (12.57) and the Markov switching GARCH-M model in Eq. (12.55). The two
ﬁtted volatility series (Figure 12.18) show similar patterns and are consistent with
the behavior of the squared log returns. The simple GARCH-M model produces a
smoother volatility series with lower estimated volatilities.
--- page 692 ---

markov switching models
665
TABLE 12.5
Fitted Markov Switching GARCH-M Model for Monthly Log Returns
of GE Stock from January 1926 to December 1999a
State 1
Parameter
β1
e1
α10
α11
α12
Posterior mean
0.111
0.089
2.070
0.844
0.033
Posterior standard error
0.043
0.012
1.001
0.038
0.033
State 2
Parameter
β2
e2
α20
α21
α22
Posterior mean
0.247
0.112
2.740
0.869
0.068
Posterior standard Error
0.050
0.014
1.073
0.031
0.024
Difference Between States
Parameter
β2 −β1
e2 −e1
α20 −α10
α21 −α11
α22 −α12
Posterior mean
0.135
0.023
0.670
0.026
−0.064
Posterior standard error
0.063
0.019
1.608
0.050
0.043
aThe numbers shown are the posterior means and standard deviations based on a Gibbs sampling with
5000 + 2000 iterations. Results of the ﬁrst 5000 iterations are discarded. The prior distributions and
initial parameter estimates are given in the text.
−0.1
0.0
0.1
0.2
0
100
200
300
β1
0.1
0.2
0.3
0.4
0
50 100
200
300
β2
0.06
0.08
0.10
0.12
0.14
0 100
300
500
ε1
0.06
0.08
0.10
0.12
0.14
0.16
0 100 200 300 400 500
ε2
Figure 12.15
Histograms of risk premium and transition probabilities of a two-state Markov switching
GARCH-M model for monthly log returns of GE stock from 1926 to 1999. Results based on last 2000
iterations of Gibbs sampling with 5000 + 2000 total iterations.
--- page 693 ---

666
markov chain monte carlo methods with applications
0
1
3
4
5
2
6
0
100
200
300
400
α10
0
1
2
3
4
5
6
0
100
200
300
α20
0.75 0.80 0.85 0.90 0.95
0
100
200
300
400
α11
0.70 0.75 0.80 0.85 0.90 0.95
0
100
200
300
400
500
α21
0.05 0.10 0.15 0.20 0.25
0
100
200
300
400
α12
0.0 0.05 0.10 0.15 0.20
0
100 200 300 400 500 600
α22
Figure 12.16
Histograms of volatility parameters of two-state Markov switching GARCH-M model
for monthly log returns of GE stock from 1926 to 1999. Results based on last 2000 iterations of Gibbs
sampling with 5000 + 2000 total iterations.
12.10
FORECASTING
Forecasting under the MCMC framework can be done easily. The procedure is
simply to use the ﬁtted model in each Gibbs iteration to generate samples for
the forecasting period. In a sense, forecasting here is done by using the ﬁtted
model to simulate realizations for the forecasting period. We use the univariate
stochastic volatility model to illustrate the procedure; forecasts of other models
can be obtained by the same method.
Consider the stochastic volatility model in Eqs. (12.20) and (12.21). Suppose that
there are n returns available and we are interested in predicting the return rn+i and
volatility hn+i for i = 1, . . . , ℓ, where ℓ> 0. Assume that the explanatory variables
xjt in Eq. (12.20) are either available or can be predicted sequentially during the
forecasting period. Recall that estimation of the model under the MCMC framework
is done by Gibbs sampling, which draws parameter values from their conditional
posterior distributions iteratively. Denote the parameters by βj = (β0,j, . . . , βp,j)′,
αj = (α0,j, α1,j)′, and σ 2
v,j for the jth Gibbs iteration. In other words, at the jth
--- page 694 ---

forecasting
667
Iterations
(a)
(b)
Sum of coefficients
0
500
1000
1500
2000
0.80 0.85 0.90 0.95 1.00
Iterations
Sum of coefficients
0
500
1000
1500
2000
0.80 0.85 0.90 0.95 1.00
Figure 12.17
Time plots of persistent parameter αi1 + αi2 of two-state Markov switching GARCH-M
model for monthly log returns of GE stock from 1926 to 1999. Results based on last 2000 iterations of
Gibbs sampling with 5000 + 2000 total iterations.
Gibbs iteration, the model is
rt = β0,j + β1,jx1t + · · · + βp,jxpt + at,
(12.58)
ln ht = α0,j + α1,j ln ht−1 + vt,
Var(vt) = σ 2
v,j.
(12.59)
We can use this model to generate a realization of rn+i and hn+i for i = 1, . . . , ℓ.
Denote the simulated realizations by rn+i,j and hn+i,j, respectively. These realizations are generated as follows:
• Draw a random sample vn+1 from N(0, σ 2
v,j) and use Eq. (12.59) to compute
hn+1,j.
• Draw a random sample ϵn+1 from N(0, 1) to obtain an+1,j = hn+1,jϵn+1
and use Eq. (12.58) to compute rn+1,j.
• Repeat the prior two steps sequentially for n + i with i = 2, . . . , ℓ.
If we run a Gibbs sampling for M + N iterations in model estimation, we only
need to compute the forecasts for the last N iterations. This results in a random
--- page 695 ---

668
markov chain monte carlo methods with applications
Year
(a)
Returns squared
1940
1960
1980
2000
0
500 100015002000
GARCH
0
200
400
600
MSW
0
200
400
600
Year
(b)
1940
1960
1980
2000
Year
(c)
1940
1960
1980
2000
Figure 12.18
Fitted volatility series for monthly log returns of GE stock from 1926 to 1999: (a) squared
log returns, (b) GARCH-M model in Eq. (12.59), and (c) two-state Markov switching GARCH-M model
in Eq. (12.57).
sample for rn+i and hn+i. More speciﬁcally, we obtain
{rn+1,j, . . . , rn+ℓ,j}N
j=1,
{hn+1,j, . . . , hn+ℓ,j}N
j=1.
These two random samples can be used to make inference. For example, point
forecasts of the return rn+i and volatility hn+i are simply the sample means of the
two random samples. Similarly, the sample standard deviations can be used as the
variances of forecast errors. To improve the computational efﬁciency in volatility
forecast, importance sampling can be used; see Gelman, Carlin, Stern, and Rubin
(2003).
Example 12.7.
(Example 12.3 continued) As a demonstration, we consider the
monthly log return series of the S&P 500 index from 1962 to 1999. Table 12.6
gives the point forecasts of the return and its volatility for ﬁve forecast horizons
starting with December 1999. Both the GARCH model in Eq. (12.26) and the
--- page 696 ---

other applications
669
TABLE 12.6
Volatility Forecasts for Monthly Log Return of S&P 500 Indexa
Horizon
1
2
3
4
5
Log Return
GARCH
0.66
0.66
0.66
0.66
0.66
SVM
0.53
0.78
0.92
0.88
0.84
Volatility
GARCH
17.98
18.12
18.24
18.34
18.42
SVM
19.31
19.36
19.35
19.65
20.13
aThe data span is from January 1962 to December 1999 and the forecast origin is December 1999.
Forecasts of the stochastic volatility model are obtained by a Gibbs sampling with 2000 + 2000
iterations.
stochastic volatility model in Eq. (12.27) are used in the forecasting. The volatility
forecasts of the GARCH(1,1) model increase gradually with the forecast horizon
to the unconditional variance 3.349/(1 −0.086 −0.735) = 18.78. The volatility
forecasts of the stochastic volatility model are higher than those of the GARCH
model. This is understandable because the stochastic volatility model takes into
consideration the parameter uncertainty in producing forecasts. In contrast, the
GARCH model assumes that the parameters are ﬁxed and given in Eq. (12.26).
This is an important difference and is one of the reasons that GARCH models tend
to underestimate the volatility in comparison with the implied volatility obtained
from derivative pricing.
Remark.
Besides the advantage of taking into consideration parameter uncertainty in forecast, the MCMC method produces in effect a predictive distribution
of the volatility of interest. The predictive distribution is more informative than a
simple point forecast. It can be used, for instance, to obtain the quantiles needed
in value at risk calculation.
□
12.11
OTHER APPLICATIONS
The MCMC method is applicable to many other ﬁnancial problems. For example,
Zhang, Russell, and Tsay (2008) use it to analyze information determinants of
bid and ask quotes, McCulloch and Tsay (2001) use the method to estimate a
hierarchical model for IBM transaction data, and Eraker (2001) and Elerian, Chib,
and Shephard (2001) use it to estimate diffusion equations. The method is also
useful in value at risk calculation because it provides a natural way to evaluate
predictive distributions. The main question is not whether the methods can be used
in most ﬁnancial applications, but how efﬁcient the methods can become. Only
time and experience can provide an adequate answer to the question.
--- page 697 ---

670
markov chain monte carlo methods with applications
EXERCISES
12.1. Suppose that x is normally distributed with mean µ and variance 4. Assume
that the prior distribution of µ is also normal with mean 0 and variance 25.
What is the posterior distribution of µ given the data point x?
12.2. Consider the linear regression model with time series errors in Section 12.5.
Assume that zt is an AR(p) process (i.e., zt = φ1zt−1 + · · · + φpzt−p + at).
Let φ = (φ1, . . . , φp)′ be the vector of AR parameters. Derive the conditional posterior distributions of f (β|Y, X, φ, σ 2), f (φ|Y, X, β, σ 2), and
f (σ 2|Y, X, β, φ) using the conjugate prior distributions, that is, the priors are
β ∼N(βo, o),
φ ∼N(φo, Ao),
(vλ)/σ 2 ∼χ2
v .
12.3. Consider the linear AR(p) model in Section 12.6.1. Suppose that xh and
xh+1 are two missing values with a joint prior distribution being multivariate
normal with mean µo and covariance matrix o. Other prior distributions
are the same as that in the text. What is the conditional posterior distribution
of the two missing values?
12.4. Consider the monthly log returns of Ford Motors stock from January 1965
to December 2008: (a) Build a GARCH model for the series, (b) build
a stochastic volatility model for the series, and (c) compare and discuss
the two volatility models. The simple returns of the stock are in the ﬁle
m-fsp6508.txt.
12.5. Build a stochastic volatility model for the daily log return of Cisco Systems
stock from January 2001 to December 2008. You may download the simple
return of the stock from the CRSP database or the ﬁle d-csco0108.txt.
Transform the data into log returns in percentage. Use the model to obtain
a predictive distribution for 1-step-ahead volatility forecast at the forecast
origin December 31, 2008. Finally, use the predictive distribution to compute the value at risk of a long position worth $1 million with probability
0.01 for the next trading day.
12.6. Build a bivariate stochastic volatility model for the monthly log returns of
Ford Motors stock and the S&P composite index for the sample period from
January 1965 to December 2008. Discuss the relationship between the two
volatility processes and compute the time-varying beta for the Ford stock.
12.7. Consider the monthly log returns of Procter & Gamble stock and the valueweighted index from January 1965 to December 2008. The simple returns
are given in the ﬁle m-pgvw6508.txt. Transform the data into log returns
in percentages. (a) Build a bivariate stochastic volatility model for the two
return series. (b) Build a BEKK(1,1) model for the two series. (c) Compare
and discuss the two models.
12.8. Consider the monthly data of 30-year mortgage rate and the 3-month Treasury Bill rate of the secondary market from April 1971 to September 2009.
--- page 698 ---

references
671
The data are in m-mort3mtb7109.txt. (a) Build a regression model with
time series error to study the effect of 3-month Treasury Bill rate on the
mortgage rate. (b) Reestimate the model using MCMC method. (c) Compare
and discuss the two ﬁtted models.
REFERENCES
Artigas, J. C. and Tsay, R. S. (2004). Effective estimation of stochastic diffusion models with
leverage effects and jumps. Working paper, Graduate School of Business, University
of Chicago.
Box, G. E. P. and Tiao, G. C. (1973). Bayesian Inference in Statistical Analysis. Addison-
Wesley, Reading, MA.
Carlin, B. P. and Louis, T. A. (2000). Bayes and Empirical Bayes Methods for Data Analysis,
2nd ed. Chapman and Hall, London.
Carter, C. K. and Kohn, R. (1994). On Gibbs sampling for state space models. Biometrika
81: 541–553.
Chang, I., Tiao, G. C., and Chen, C. (1988). Estimation of time series parameters in the
presence of outliers. Technometrics 30: 193–204.
Chib, S., Nardari, F., and Shephard, N. (2002). Markov chain Monte Carlo methods for
stochastic volatility models. Journal of Econometrics 108: 281–316.
DeGroot, M. H. (1970). Optimal Statistical Decisions. McGraw-Hill, New York.
Dempster, A. P., Laird, N. M., and Rubin, D. B. (1977). Maximum likelihood from incomplete data via the EM algorithm (with discussion). Journal of the Royal Statistical
Society Series B 39: 1–38.
Elerian, O., Chib, S. and Shephard, N. (2001). Likelihood inference for discretely observed
nonlinear diffusions. Econometrica 69: 959–993.
Eraker, B. (2001). Markov Chain Monte Carlo analysis of diffusion with application to
ﬁnance. Journal of Business & Economic Statistics 19: 177–191.
Fr¨uhwirth-Schnatter, S. (1994). Data augmentation and dynamic linear models. Journal of
Time Series Analysis 15: 183–202.
Gelfand, A. E. and Smith, A. F. M. (1990). Sampling-based approaches to calculating
marginal densities. Journal of the American Statistical Association 85: 398–409.
Gelman, A., Carlin, J. B., Stern, H. S., and Rubin, D. B. (2003). Bayesian Data Analysis,
2nd ed. Chapman and Hall/CRC, London.
Geman, S. and Geman, D. (1984). Stochastic relaxation, Gibbs distributions, and the
Bayesian restoration of images. IEEE Transactions on Pattern Analysis and Machine
Intelligence 6: 721–741.
Hasting, W. K. (1970). Monte Carlo sampling methods using Markov chains and their
applications. Biometrika 57: 97–109.
Jacquier, E., Polson, N. G., and Rossi, P. E. (1994). Bayesian analysis of stochastic volatility
models (with discussion). Journal of Business & Economic Statistics 12: 371–417.
Jacquier, E., Polson, N. G., and Rossi, P. E. (2004). Bayesian analysis of stochastic volatility
models with fat-tails and correlated errors. Journal of Econometrics 122: 185–212.
--- page 699 ---

672
markov chain monte carlo methods with applications
Jones, R. H. (1980). Maximum likelihood ﬁtting of ARMA models to time series with
missing observations. Technometrics 22: 389–395.
Justel, A., Pe˜na, D., and Tsay, R. S. (2001). Detection of outlier patches in autoregressive
time series. Statistica Sinica 11: 651–673.
Kim, S., Shephard, N., and Chib, S. (1998). Stochastic volatility: Likelihood inference and
comparison with ARCH models. Review of Economic Studies 65: 361–393.
Liu, J., Wong, W. H., and Kong, A. (1994). Correlation structure and convergence rate of
the Gibbs samplers. I. Applications to the comparison of estimators and augmentation
schemes. Biometrika 81: 27–40.
McCulloch, R. E. and Tsay, R. S. (1994a). Bayesian analysis of autoregressive time series
via the Gibbs sampler. Journal of Time Series Analysis 15: 235–250.
McCulloch, R. E. and Tsay, R. S. (1994b). Statistical analysis of economic time series via
Markov switching models. Journal of Time Series Analysis 15: 523–539.
McCulloch, R. E. and Tsay, R. S. (2001). Nonlinearity in high-frequency ﬁnancial data and
hierarchical models. Studies in Nonlinear Dynamics and Econometrics 5: 1–17.
Metropolis, N. and Ulam, S. (1949). The Monte Carlo method. Journal of the American
Statistical Association 44: 335–341.
Metropolis, N., Rosenbluth, A. W., Rosenbluth, M. N., Teller, A. H., and Teller, E. (1953).
Equation of state calculations by fast computing machines. Journal of Chemical Physics
21 1087–1092.
Tanner, M. A. (1996). Tools for Statistical Inference: Methods for the Exploration of Posterior
Distributions and Likelihood Functions, 3rd ed. Springer, New York.
Tanner, M. A. and Wong, W. H. (1987). The calculation of posterior distributions by data
augmentation (with discussion). Journal of the American Statistical Association 82:
528–550.
Tierney, L. (1994). Markov chains for exploring posterior distributions (with discussion).
Annals of Statistics 22: 1701–1762.
Tsay, R. S. (1988). Outliers, level shifts, and variance changes in time series. Journal of
Forecasting 7: 1–20.
Tsay, R. S., Pe˜na, D., and Pankratz, A. (2000). Outliers in multivariate time series. Biometrika
87: 789–804.
Zhang, M. Y., Russell, J. R., and Tsay, R. S. (2008). Determinants of bid and ask quotes
and implications for the cost of trading. Journal of Empirical Finance 15: 656–678.
--- page 700 ---

Index
D(un) condition, 378, 379
ACD model, 255
exponential, 256
generalized Gamma, 257
threshold, 264
Weibull, 256
Activation function, see Neural network,
200
Airline model, 84
Akaike information criterion (AIC), 48,
406
Arbitrage, 443
ARCH effect, 114
ARCH model, 115
estimation, 120
t distribution, 121
GED innovation, 122
normal, 120
Arranged autoregression, 212
Augmented Dickey–Fuller test, 77
Autocorrelation function (ACF), 31
Autocovariance, 30
Autoregressive integrated moving-average
(ARIMA) model, 76
Autoregressive model, 37
estimation, 49
forecasting, 54
order, 47
stationarity, 46
Autoregressive moving-average (ARMA)
model, 64
forecasting, 68
Analysis of Financial Time Series, Third Edition, By Ruey S. Tsay
Copyright 2010 John Wiley & Sons, Inc.
Back propagation
neural network, 203
Back-shift operator, 41
Bartlett’s formula, 32
Bayesian information criterion (BIC), 48
Bid–ask bounce, 236
Bid–ask spread, 236
Bilinear model, 177
Black–Scholes
differential equation, 299
Black–Scholes formula
European call option, 301, 109
European put option, 302
Brownian motion, 290
geometric, 294
standard, 289
Business cycle, 42
Canonical correlation analysis, 437
Characteristic equation, 46
Characteristic root, 42, 46
CHARMA model, 150
Cholesky decomposition, 400, 458,
517
Cointegration, 91, 428
Cointegration test
maximum eigenvalue, 437
trace, 437
Common factor, 543
Common trend, 430
Companion matrix, 404
Compounding, 4
Conditional distribution, 8
673
--- page 701 ---

674
index
Conditional forecast, 55
Conditional heteroscedasticity, 97
HAC covariance estimator, 98
Conditional-likelihood method, 61
Conjugate prior, see Distribution, 618
Correlation
coefﬁcient, 30
constant, 522
time-varying, 525
Cost-of-carry model, 443
Covariance matrix, 390
Cross-correlation matrix, 390, 391
Cross-validation, 193
CVaR
Conditional value at risk, 328
Data
3M stock return, 21, 67, 74, 185
Bank of America stock return, 485
BHP daily price, 449
Cisco stock return, 296, 538, 546
Citi-Group stock return, 21
Civilian employment number, 475
Consumer price index, 475
equal-weighted index, 21, 60, 61, 102, 178,
213
GE stock return, 663
Hewlett-Packard stock return, 485
Hong Kong market index, 507
IBM stock return, 21, 33, 145, 154, 155, 182,
203, 213, 295, 330, 334, 338, 340, 348,
355, 364, 393, 485, 524, 544, 645
IBM transactions, 238, 241, 246, 250, 262, 268
Intel stock return, 21, 111, 123, 339, 485, 538,
546
J.P. Morgan Chase stock return, 485
Japan market index, 507
Johnson & Johnson’s earnings, 81
Mark/dollar exchange rate, 116
Microsoft sock return, 21
SP 500 excess return, 134, 151
SP 500 index futures, 443, 445
SP 500 index return, 154, 158, 160, 393, 524,
538, 544, 640, 645, 658
SP 500 spot price, 445
U.S. 3-month Treasury bill rate, 196
U.S. government bond, 23, 395, 494
U.S. interest rate, 23, 90, 627, 635
U.S. monthly unemployment rate, 181
U.S. real GNP, 42, 188
U.S. unemployment rate, 218
Vale daily price, 449
value-weighted index, 21, 145
value-weighted index, 34, 47, 102, 213
Data augmentation, 615
Decomposition model, 248
Descriptive statistics, 21
Diagonal VEC model, 510
Dickey–Fuller test, 77
Differencing 76
seasonal, 84
Distribution
beta, 620
double exponential, 312
Frechet family, 344
gamma, 277, 619
generalized error, 122
generalized extreme value, 343
Generalized gamma, 278
generalized Pareto, 361, 373
inverted chi-squared, 621
Laplacian, 312
multivariate t, 548
multivariate normal, 460, 619
negative binomial, 620
Poisson, 620
posterior, 618
prior, 618
conjugate, 618
skew-Student-t, 122
Weibull, 278
Diurnal pattern, 238
Donsker’s theorem, 290
Duration
between trades, 239
model, 253
Durbin-Watson statistic, 97
Dynamic conditional correlation model, 531
EGARCH model, 143
forecasting, 147
Eigenvalue, 457
Eigenvector, 457
EM algorithm, 614
Error correction model, 431
Estimation
extreme value parameter, 345
Exact-likelihood method, 61
Exceedance, 359
Exceeding times, 359
Excess return, 5
Expected shortfall, 333
Extended autocorrelation function, 66
Extremal index, 377, 380
Extreme value theory, 342
Factor analysis, 489
Factor mimicking portfolio, 482
--- page 702 ---

index
675
Factor model
common factor, 468
estimation, 491
factor loading, 468
speciﬁc factor, 468
Factor rotation
varimax, 492
Filtering, 561
Forecast
horizon, 54
origin, 54
Forecast updating formula, 581
Forecasting
MCMC method, 666
Forward ﬁltering and backward sampling, 655
Fractional differencing, 101
GARCH model, 131
Cholesky decomposition, 528
multivariate, 521
diagonal, 523
time-varying correlation, 526
GARCH-M model, 142, 660
Generalized least squares, 478
Generalized Pareto Distribution, 361
Geometric ergodicity, 179
Gibbs sampling, 615
Global minimum variance portfolio, 473
Griddy Gibbs, 623
Half-life, 56
Hazard function, 279
Hh function, 318
Hill estimator, 348
Hyperparameter, 625
Identiﬁability, 422
IGARCH model, 140, 329
Implied volatility, 110
Impulse response function, 71, 413
Innovation, 36
Inverted yield curve, 91
Invertibility, 60, 431
Invertible ARMA model, 70
Ito process, 292
Ito’s lemma, 294
multivariate, 310
Joint distribution function, 7
Jump diffusion, 311
Kalman ﬁlter, 563, 593
Kalman gain, 563, 593
Kernel, 190
bandwidth, 192
Epanechnikov, 191
Gaussian, 191
Kernel regression, 190
Kurtosis, 9
excess, 9
Lag operator, 41
Lead–lag relationship, 391
Leptokurtic, 9
Leverage effect, 111, 144, 650
Likelihood function, 19
Linear time series, 36
Liquidity, 235
Ljung–Box statistic, 114, 32
multivariate, 397
Local linear regression, 195
Local trend model, 558
Log return, 5
Logit model, 267
Long position, 6
Long-memory
stochastic volatility, 154
time series, 101
Marginal distribution, 7
Market model, 470
Markov process, 613
Markov property, 37
Markov switching model, 187, 660
Martingale difference, 132
Maximum-likelihood estimate
exact, 420
MCMC method, 199
Mean equation, 113
Mean excess function, 362
Mean excess plot, 362
Mean residual life plot, 363
Mean reversion, 56, 71
half-life, 56
Metropolis algorithm, 622
Metropolis–Hasting algorithm, 623
Missing value, 600, 628
Model checking, 51
Moment
of a random variable, 8
Moving-average model, 57
Nadaraya–Watson estimator, 191
Neural network, 199
activation function, 200
feed-forward, 200
--- page 703 ---

676
index
Neural network (Continued)
skip layer, 202
Neuron, see Neural network, 200
Node, see Neural network, 200
Nonlinearity test, 205
BDS, 208
bispectral, 207
F test, 211
Keenan, 210
RESET, 209
Tar-F, 213
Nonstationarity
unit-root, 72
Nonsynchronous trading, 232
Nuisance parameter, 211
Options
American, 288
at-the-money, 288
European call, 109
in-the-money, 288
out-of-the-money, 288
stock, 288
strike price, 109, 288
Order statistics, 339
Ordered probit model, 245
Orthogonal factor model, 489
Outlier
additive, 628
detection, 632
OX command
garchOxFit, 130
Pairs trading, 446
Parametric bootstrap, 215
Partial autoregressive function (PACF),
46
PCD model, 265
Peaks over Thresholds, 359
π weight, 70
Pickands estimator, 348
Platykurtic, 9
Poisson process, 311
inhomogeneous, 371
intensity function, 363
Portmanteau test 32, see Ljung–Box statistic,
397
Positive-deﬁnite matrix, 458
Prediction, 561
Present value, 5
Principal component analysis, 483, 543
ψ weight, 36
Put–call parity, 302
Quantile, 8
deﬁnition, 327
R command
ar, 49
exindex, 384
factanal, 495
garchFit, 127
gev, 351
glm, 252
gpd, 367
hill, 351
lowess, 196
meplot, 363
nnet, 223
optim, 186
pot, 366
princomp, 488
qt, 335
quantile, 341
read.table, 24
riskmeasures, 370
ts, 24
R package, 24
R-square, 54
Adjusted, 54
Random coefﬁcient (RCA) model, 153
Random walk, 72
with drift, 73
Realized volatility, 559, 162
Reduced–form model, 399
Regression
with time series errors, 90
Return level, 358
stress period, 358
RiskMetrics, 328
S-Plus command
archTest, 115
autocorTest, 115
coint, 439
ewma1, 331
garch, 124
mfactor, 500
mgarch, 507
OLS, 97
tslag, 97
VAR, 414
VECM, 439
Sample autocorrelation, 31
Scree plot, 488
Seasonal adjustment, 82
Seasonal model, 81
multiplicative, 84
--- page 704 ---

index
677
Shape parameter
of a distribution, 343
Shock, 36, 55, 113
Short position, 6
Simple return, 3
Skewness, 9
Smoothed disturbance, 597
Smoothing, 189, 561
Square root of time rule, 330
Standard Brownian motion, 77
State-space model, 576
nonlinear, 199
Stationarity, 30
weak, 390
Statistical arbitrage, 446
Steady state, 594
Stochastic diffusion equation, 292
Stochastic volatility model, 153, 637
multivariate, 643
Structural equation, 400
Structural form, 400
Structural Time Series, 590
Structural time series model, 558
Student-t distribution
standardized, 121
Survival function, 363
Tail index, 343
TGARCH model, 149
general form, 182
Threshold, 180
Threshold autoregressive model
multivariate, 444
self-exciting, 180
smooth, 184
Threshold cointegration, 444
Time plot, 19
Transactions data, 237
Trend stationary model, 75
Unit-root test, 76
Unit-root time series, 72
Unobserved component model, 590
Value at risk, 326, 546
VaR
econometric approach, 333
homogeneous Poisson process, 365
inhomogeneous Poisson process, 371
RiskMetrics, 329
traditional extreme value, 353
Vector AR model, 399
Vector ARMA model, 422
marginal models, 427
Vector MA model, 417
VIX Volatility Index, 110
Volatility, 109
Volatility equation, 113
Volatility model
factor, 543
Volatility smile, 311
Weighted least squares, 477
White noise, 36
Wiener process, 289
generalized, 291
Yule–Walker equation
multivariate, 404
