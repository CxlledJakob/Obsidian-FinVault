# Analysis of Financial Time Series, Third Edition (Wiley -- Ruey S_ Tsay -- Wiley series in probability and statistics, 3rd ed_, -- John Wiley & Sons, -- isbn13 9780470414354 -- 9f99b80c7b2dedd477f463dc5323f3b6 -- An.pdf — pages 286–305

--- page 286 ---

duration models
259
0
2
4
6
8
10
0
20
40
60
80
100
120
Z
(a)
(b)
0
20
40
60
80
0
100
200
300
X
Figure 5.11
Histograms of simulated duration processes with 500 observations: (a) WACD(1,1) model
and (b) GACD(1,1) model.
Lag
(a)
ACF
0
5
10
15
20
25
30
−0.2
0.0
0.2
0.4
Lag
(b)
ACF
0
5
10
15
20
25
30
−0.2
0.0
0.2
0.4
Figure 5.12
Sample autocorrelation function of simulated WACD(1,1) series with 500 observations:
(a) original series and (b) standardized residual series.
--- page 287 ---

260
high-frequency data analysis and market microstructure
Lag
(a)
ACF
0
5
10
15
20
25
30
−0.1
0.1
0.3
0.5
Lag
(b)
ACF
0
5
10
15
20
25
30
−0.1
0.1
0.3
0.5
Figure 5.13
Sample autocorrelation function of simulated GACD(1,1) series with 500 observations:
(a) original series and (b) standardized residual series.
5.5.3
Estimation
For an ACD(r, s) model, let io = max(r, s) and xt = (x1, . . . , xt)′. The likelihood
function of the durations x1, . . . , xT is
f (xT |θ) =


T
i=io+1
f (xi|Fi−1, θ)

× f (xio|θ),
where θ denotes the vector of model parameters, and T is the sample size. The
marginal probability density function f (xio|θ) of the previous equation is rather
complicated for a general ACD model. Because its impact on the likelihood function
is diminishing as the sample size T increases, this marginal density is often ignored,
resulting in use of the conditional-likelihood method. For a WACD model, we use
the probability density function (pdf) of Eq. (5.56) and obtain the conditional
log-likelihood function
ℓ(x|θ, xio) =
T

i=i0+1
α ln



1 + 1
α
	
+ ln
 α
xi

+ α ln
 xi
ψi

−

(1 + 1/α)xi
ψi
α
,
(5.41)
--- page 288 ---

duration models
261
TABLE 5.7
Estimation Results for Simulated ACD(1,1) Series with 500
Observations: For WACD(1,1) Series and GACD(1,1) Series
WACD(1,1) Model
Parameter
ω
γ1
ω1
α
True
0.3
0.2
0.7
1.5
Estimate
0.364
0.100
0.767
1.477
Standard Error
(0.139)
(0.025)
(0.060)
(0.052)
GACD(1,1) Model
Parameter
ω
γ1
ω1
α
κ
True
0.3
0.2
0.7
0.5
1.5
Estimate
0.401
0.343
0.561
0.436
2.077
Standard Error
(0.117)
(0.074)
(0.065)
(0.078)
(0.653)
where ψi =ω + r
j=1 γjxi−j + s
j=1 ωjψi−j, θ =(ω, γ1, . . . , γr, ω1, . . . , ωs, α)′,
and x = (xio+1, . . . , xT )′. When α = 1, the (conditional) log-likelihood function
reduces to that of an EACD(r, s) model.
For a GACD(r, s) model, the conditional log-likelihood function is
ℓ(x|θ, xio) =
T

i=io+1
ln

α
(κ)

+ (κα −1) ln(xi) −κα ln(λψi) −
 xi
λψi
	α
,
(5.42)
where λ = (κ)/ (κ + 1/α) and the parameter vector θ now also includes κ. As
expected, when κ = 1, λ = 1/ (1 + 1/α) and the log-likelihood function in Eq.
(5.42) reduces to that of a WACD(r, s) model in Eq. (5.41). This log-likelihood
function can be rewritten in many ways to simplify the estimation.
Under some regularity conditions, the conditional maximum-likelihood estimates
are asymptotically normal; see Engle and Russell (1998) and the references therein.
In practice, simulation can be used to obtain ﬁnite-sample reference distributions
for the problem of interest once a duration model is speciﬁed.
Example 5.3.
(Simulated ACD(1,1) series, continued). Consider the simulated WACD(1,1) and GACD(1,1) series of Eq. (5.40). We apply the conditionallikelihood method and obtain the results in Table 5.7. The estimates appear to be
reasonable. Let ˆψi be the 1-step-ahead prediction of ψi and ˆϵi = xi/ ˆψi be the standardized series, which can be regarded as standardized residuals of the series. If
the model is adequately speciﬁed, {ˆϵi} should behave as a sequence of independent
and identically distributed random variables. Figures 5.9(b) and 5.10(b) show the
time plot of ˆϵi for both models. The sample ACF of ˆϵi for both ﬁtted models are
shown in Figures 5.12(b) and 5.13(b), respectively. It is evident that no signiﬁcant
serial correlations are found in the ˆϵi series.
Example 5.4.
As an illustration of duration models, we consider the transaction durations of IBM stock on ﬁve consecutive trading days from November 1
--- page 289 ---

262
high-frequency data analysis and market microstructure
Sequence
(a)
Adjusted duration
0
1000
2000
3000
0
10
20
30
40
Normalized duration
0 2 4 6 8 10 12 14
Sequence
(b)
0
1000
2000
3000
Figure 5.14
Time plots of durations for IBM stock traded in ﬁrst ﬁve trading days of November 1990:
(a) adjusted series and (b) normalized innovations of an WACD(1,1) model. There are 3534 nonzero
durations.
to November 7, 1990. Focusing on positive transaction durations, we have 3534
observations. In addition, the data have been adjusted by removing the deterministic component in Eq. (5.32). That is, we employ 3534 positive adjusted durations
as deﬁned in Eq. (5.31).
Figure 5.14(a) shows the time plot of the adjusted (positive) durations for the
ﬁrst ﬁve trading days of November 1990, and Figure 5.15(a) gives the sample ACF
of the series. There exist some serial correlations in the adjusted durations. We ﬁt
a WACD(1,1) model to the data and obtain the model
xi = ψiϵi,
ψi = 0.169 + 0.064xi−1 + 0.885ψi−1,
(5.43)
where {ϵi} is a sequence of independent and identically distributed random variates
that follow the standardized Weibull distribution with parameter ˆα = 0.879(0.012),
where 0.012 is the estimated standard error. Standard errors of the estimates in
Eq. (5.43) are 0.039, 0.010, and 0.018, respectively. All t ratios of the estimates
are greater than 4.2, indicating that the estimates are signiﬁcant at the 1% level.
Figure 5.14(b) shows the time plot of ˆϵi = xi/ ˆψi, and Figure 5.15(b) provides the
sample ACF of ˆϵi. The Ljung–Box statistics show Q(10) = 4.96 and Q(20) =
10.75 for the ˆϵi series. Clearly, the standardized innovations have no signiﬁcant
serial correlations. In fact, the sample autocorrelations of the squared series {ˆϵ2
i }
--- page 290 ---

duration models
263
Lag
(a)
ACF
0
10
20
30
−0.10
0.0
0.10
0.20
Lag
(b)
ACF
0
10
20
30
−0.10
0.0
0.10
0.20
Figure 5.15
Sample autocorrelation function of adjusted durations for IBM stock traded in ﬁrst ﬁve
trading days of November 1990: (a) adjusted series and (b) normalized innovations for WACD(1,1)
model.
are also small with Q(10) = 6.20 and Q(20) = 11.16, further conﬁrming lack of
serial dependence in the normalized innovations. In addition, the mean and standard
deviation of a standardized Weibull distribution with α = 0.879 are 1.00 and 1.14,
respectively. These numbers are close to the sample mean and standard deviation
of {ˆϵi}, which are 1.01 and 1.22, respectively. The ﬁtted model seems adequate.
In model (5.43), the estimated coefﬁcients show ˆγ1 + ˆω1 ≈0.949, indicating
certain persistence in the adjusted durations. The expected adjusted duration is
0.169/(1 −0.064 −0.885) = 3.31 seconds, which is close to the sample mean 3.29
of the adjusted durations. The estimated α of the standardized Weibull distribution
is 0.879, which is less than but close to 1. Thus, the conditional hazard function is
monotonously decreasing at a slow rate.
If a generalized gamma distribution function is used for the innovations, then
the ﬁtted GACD(1,1) model is
xi = ψiϵi,
ψi = 0.141 + 0.063xi−1 + 0.897ψi−1,
(5.44)
where {ϵi} follows a standardized, generalized gamma distribution in Eq. (5.57)
with parameters κ = 4.248(1.046) and α = 0.395(0.053), where the number in
parentheses denotes estimated standard error. Standard errors of the three parameters in Eq. (5.44) are 0.041, 0.010, and 0.019, respectively. All of the estimates are
--- page 291 ---

264
high-frequency data analysis and market microstructure
statistically signiﬁcant at the 1% level. Again, the normalized innovational process
{ˆϵi} and its squared series have no signiﬁcant serial correlation, where ˆϵi = xi/ ˆψi
based on model (5.44). Speciﬁcally, for the ˆϵi process, we have Q(10) = 4.95 and
Q(20) = 10.28. For the ˆϵ2
i series, we have Q(10) = 6.36 and Q(20) = 10.89.
The expected duration of model (5.44) is 3.52, which is slightly greater than
that of the WACD(1,1) model in Eq. (5.43). Similarly, the persistence parameter
ˆγ1 + ˆω1 of model (5.44) is also slightly higher at 0.96.
Remark.
Estimation of EACD models can be carried out by using programs
for ARCH models with some minor modiﬁcation; see Engle and Russell (1998). In
this book, we use either the RATS program or some Fortran programs developed
by the author to estimate the duration models. Limited experience indicates that it
is harder to estimate a GACD model than an EACD or a WACD model. RATS
programs used to estimate WACD and GACD models are given in Appendix C.
□
5.6
NONLINEAR DURATION MODELS
Nonlinear features are also commonly found in high-frequency data. As an illustration, we apply some nonlinearity tests discussed in Chapter 4 to the normalized
innovations ˆϵi of the WACD(1,1) model for the IBM transaction durations in
Example 5.4; see Eq. (5.43). Based on an AR(4) model, the test results are given
in part (a) of Table 5.8. As expected from the model diagnostics of Example 5.4,
the Ori-F test indicates no quadratic nonlinearity in the normalized innovations.
However, the TAR-F test statistics suggest strong nonlinearity.
Based on the test results in Table 5.8, we entertain a threshold duration model
with two regimes for the IBM intraday durations. The threshold variable is xt−1
(i.e., lag-1 adjusted duration). The estimated threshold value is 3.79. The ﬁtted
threshold WACD(1,1) model is xi = ψiϵi, where
ψi =

0.020 + 0.257xi−1 + 0.847ψi−1,
ϵi ∼w(0.901)
if xi−1 ≤3.79,
1.808 + 0.027xi−1 + 0.501ψi−1,
ϵi ∼w(0.845)
if xi−1 > 3.79,
(5.45)
where w(α) denotes a standardized Weibull distribution with parameter α. The
number of observations in the two regimes are 2503 and 1030, respectively. In Eq.
(5.45), the standard errors of the parameters for the ﬁrst regime are 0.043, 0.041,
0.024, and 0.014, whereas those for the second regime are 0.526, 0.020, 0.147, and
0.020, respectively.
Consider the normalized innovations ˆϵi = xi/ ˆψi of the threshold WACD(1,1)
model in Eq. (5.45). We obtain Q(12) = 9.8 and Q(24) = 23.9 for ˆϵi and Q(12) =
8.0 and Q(24) = 16.7 for ˆϵ2
i . Thus, there are no signiﬁcant serial correlations in
the ˆϵi and ˆϵ2
i series. Furthermore, applying the same nonlinearity tests as before
to this newly normalized innovational series ˆϵi, we detect no nonlinearity; see part
--- page 292 ---

bivariate models for price change and duration
265
TABLE 5.8
Nonlinearity Tests for IBM Transaction Durations from November 1 to
November 7, 1990a
(a) Normalized Innovations of a WACD(1,1) Model
Type
Ori-F
TAR-F(1)
TAR-F(2)
TAR-F(3)
TAR-F(4)
Test
0.343
3.288
3.142
3.128
0.297
p Value
0.969
0.006
0.008
0.008
0.915
(b) Normalized Innovations of a Threshold WACD(1,1) Model
Test
0.163
0.746
1.899
1.752
0.270
p Value
0.998
0.589
0.091
0.119
0.929
aOnly intraday durations are used. The number in parentheses of TAR-F tests denotes time delay.
(b) of Table 5.8. Consequently, the two-regime threshold WACD(1,1) model in Eq.
(5.45) is adequate.
If we classify the two regimes as heavy and thin trading periods, then the threshold model suggests that the trading dynamics measured by intraday transaction
durations are different between heavy and thin trading periods for IBM stock even
after the adjustment of diurnal pattern. This is not surprising as market activities
are often driven by the arrival of news and other information.
The estimated threshold WACD(1,1) model in Eq. (5.45) contains some insignificant parameters. We reﬁne the model and obtain the result:
ψi =

0.225xi−1 + 0.867ψi−1,
ϵi ∼w(0.902)
if xi−1 ≤3.79,
1.618 + 0.614ψi−1,
ϵi ∼w(0.846)
if xi−1 > 3.79.
All of the estimates of the reﬁned model are highly signiﬁcant. The Ljung–Box
statistics of the standardized innovations ˆϵi = xi/ ˆψi show Q(10) = 5.91(0.82)
and Q(20) = 16.04(0.71) and those of ˆϵ2
i give Q(10) = 5.35(0.87) and Q(20) =
15.20(0.76), where the number in parentheses is the p value. Therefore, the reﬁned
model is adequate. The RATS program used to estimate the prior model is given
in Appendix C.
5.7
BIVARIATE MODELS FOR PRICE CHANGE AND DURATION
In this section, we introduce a model that considers jointly the process of price
change and the associated duration. As mentioned before, many intraday transactions of a stock result in no price change. Those transactions are highly relevant
to trading intensity, but they do not contain direct information on price movement.
Therefore, to simplify the complexity involved in modeling price change, we focus
on transactions that result in a price change and consider a price change and duration (PCD) model to describe the multivariate dynamics of price change and the
associated time duration.
--- page 293 ---

266
high-frequency data analysis and market microstructure
We continue to use the same notation as before, but the deﬁnition is changed to
transactions with a price change. Let ti be the calendar time of the ith price change
of an asset. As before, ti is measured in seconds from midnight of a trading day. Let
Pti be the transaction price when the ith price change occurred and
ti = ti −ti−1
be the time duration between price changes. In addition, let Ni be the number of
trades in the time interval (ti−1, ti) that result in no price change. This new variable
is used to represent trading intensity during a period of no price change. Finally,
let Di be the direction of the ith price change with Di = 1 when price goes up
and Di = −1 when the price comes down, and let Si be the size of the ith price
change measured in ticks. Under the new deﬁnitions, the price of a stock evolves
over time by
Pti = Pti−1 + DiSi,
(5.46)
and the transactions data consist of {
ti, Ni, Di, Si} for the ith price change. The
PCD model is concerned with the joint analysis of (
ti, Ni, Di, Si).
Remark.
Focusing on transactions associated with a price change can reduce
the sample size dramatically. For example, consider the intraday data of IBM stock
from November 1, 1990 to January 31, 1991. There were 60,265 intraday trades,
but only 19,022 of them resulted in a price change. In addition, there is no diurnal
pattern in time durations between price changes.
□
To illustrate the relationship among the price movements of all transactions
and those of transactions associated with a price change, we consider the intraday
tradings of IBM stock on November 21, 1990. There were 726 transactions on that
day during normal trading hours, but only 195 trades resulted in a price change.
Figure 5.16 shows the time plot of the price series for both cases. As expected, the
price series are the same.
The PCD model decomposes the joint distribution of (
ti, Ni, Di, Si) given
Fi−1 as
f (
ti, Ni, Di, Si|Fi−1)
= f (Si|Di, Ni,
ti, Fi−1)f (Di|Ni,
ti, Fi−1)f (Ni|
ti, Fi−1)f (
ti|Fi−1).
(5.47)
This partition enables us to specify suitable econometric models for the conditional distributions and, hence, to simplify the modeling task. There are many
ways to specify models for the conditional distributions. A proper speciﬁcation
might depend on the asset under study. Here we employ the speciﬁcations used by
McCulloch and Tsay (2000), who use generalized linear models for the discretevalued variables and a time series model for the continuous variable ln(
ti).
For the time duration between price changes, we use the model
ln(
ti) = β0 + β1 ln(
ti−1) + β2Si−1 + σϵi,
(5.48)
--- page 294 ---

bivariate models for price change and duration
267
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
••••
•
•
••
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
••
••••
•
•
••••
••
•••• •
••
•
••
•
••
•
•
•••
•
•
••
•
•
•
••
•
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
••••
•
•••
•
•
•
•
•
••••••
•••
•
•••••
• •
•
••
•
•
•••••
•
••
••
•
••••
•
••••
•
•
•••••
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
•••
••
••
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
••••
•
•
••
••
•
•
•••
•
•
•••• •
••
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
•••
•
••
•
•••
••
•
••
•
••
••
•
••
•
•
•
•
•
••
••
•••
•
•
•
•
•
•
••
•
•••
•
•
•
•
•
•••
••••
•
••
•
Seconds
(a)
Price
35000
40000
45000
50000
55000
112.5113.0113.5114.0
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
•
•
•
•
Seconds
(b)
Price
35000
40000
45000
50000
55000
112.5113.0113.5114.0
Figure 5.16
Time plots of intraday transaction prices of IBM stock on November 21, 1990: (a) all
transactions and (b) transactions that resulted in price change.
where σ is a positive number and {ϵi} is a sequence of iid N(0, 1) random variables.
This is a multiple linear regression model with lagged variables. Other explanatory
variables can be added if necessary. The log transformation is used to ensure the
positiveness of time duration.
The conditional model for Ni is further partitioned into two parts because empirical data suggest a concentration of Ni at 0. The ﬁrst part of the model for Ni is
the logit model
p(Ni = 0|
ti, Fi−1) = logit[α0 + α1 ln(
ti)],
(5.49)
where logit(x) = exp(x)/[1 + exp(x)], whereas the second part of the model is
Ni|(Ni > 0,
ti, Fi−1) ∼1 + g(λi),
λi =
exp[γ0 + γ1 ln(
ti)]
1 + exp[γ0 + γ1 ln(
ti)],
(5.50)
where ∼means “is distributed as,” and g(λ) denotes a geometric distribution with
parameter λ, which is in the interval (0, 1).
The model for direction Di is
Di|(Ni,
ti, Fi−1) = sign(µi + σiϵ),
(5.51)
--- page 295 ---

268
high-frequency data analysis and market microstructure
where ϵ is a N(0, 1) random variable, and
µi = ω0 + ω1Di−1 + ω2 ln(
ti),
ln(σi) = β
******
4

j=1
Di−j
******
= β|Di−1 + Di−2 + Di−3 + Di−4|.
In other words, Di is governed by the sign of a normal random variable with mean
µi and variance σ 2
i . A special characteristic of the prior model is the function
for ln(σi). For intraday transactions, a key feature is the price reversal between
consecutive price changes. This feature is modeled by the dependence of Di on
Di−1 in the mean equation with a negative ω1 parameter. However, there exists
an occasional local trend in the price movement. The previous variance equation
allows for such a local trend by increasing the uncertainty in the direction of price
movement when the past data showed evidence of a local trend. For a normal
distribution with a ﬁxed mean, increasing its variance makes a random draw have
the same chance to be positive and negative. This in turn increases the chance for
a sequence of all positive or all negative draws. Such a sequence produces a local
trend in price movement.
To allow for different dynamics between positive and negative price movements,
we use different models for the size of a price change. Speciﬁcally, we have
Si|(Di = −1, Ni,
ti, Fi−1) ∼p(λd,i) + 1,
with
(5.52)
ln(λd,i) = ηd,0 + ηd,1Ni + ηd,2 ln(
ti) + ηd,3Si−1
Si|(Di = 1, Ni,
ti, Fi−1) ∼p(λu,i) + 1,
with
(5.53)
ln(λu,i) = ηu,0 + ηu,1Ni + ηu,2 ln(
ti) + ηu,3Si−1,
where p(λ) denotes a Poisson distribution with parameter λ, and 1 is added to the
size because the minimum size is 1 tick when there is a price change.
The speciﬁed models in Eqs. (5.48)–(5.53) can be estimated jointly by either
the maximum-likelihood method or the Markov chain Monte Carlo methods. Based
on Eq. (5.47), the models consist of six conditional models that can be estimated
separately.
Example 5.5.
Consider the intraday transactions of IBM stock on November
21, 1990. There are 194 price changes within normal trading hours. Figure 5.17
shows the histograms of ln(
ti), Ni, Di, and Si. The data for Di are about equally
distributed between “upward” and “downward” movements. Only a few transactions resulted in a price change of more than 1 tick; as a matter of fact, there were
7 changes with 2 ticks and 1 change with 3 ticks. Using Markov chain Monte Carlo
(MCMC) methods (see Chapter 12), we obtained the following models for the data.
The reported estimates and their standard deviations are the posterior means and
--- page 296 ---

bivariate models for price change and duration
269
0
2
4
6
0
10 20 30 40 50
log(duration)
(a)
(c)
−1.0
−0.5
0.0
0.5
1.0
0
20 40 60 80 100
Direction
(b)
1.0
1.5
2.0
2.5
3.0
0
50
100 150
Size, in ticks
0
5
10
15
20
0 20 40 60 80
120
Number of trades
(d)
Figure 5.17
Histograms of intraday transactions data for IBM stock on November 21, 1990: (a) log
durations between price changes, (b) direction of price movement, (c) size of price change measured in
ticks, and (d) number of trades without price change.
standard deviations of MCMC draws with 9500 iterations. The model for the time
duration between price changes is
ln(
ti) = 4.023 + 0.032 ln(
ti−1) −0.025Si−1 + 1.403ϵi,
where standard deviations of the coefﬁcients are 0.415, 0.073, 0.384, and 0.073,
respectively. The ﬁtted model indicates that there was no dynamic dependence in
the time duration. For the Ni variable, we have
Pr(Ni > 0|
ti, Fi−1) = logit[−0.637 + 1.740 ln(
ti)],
where standard deviations of the estimates are 0.238 and 0.248, respectively. Thus,
as expected, the number of trades with no price change in the time interval (ti−1, ti)
depends positively on the length of the interval. The magnitude of Ni when it is
positive is
Ni|(Ni > 0,
ti, Fi−1) ∼1 + g(λi),
λi =
exp[0.178 −0.910 ln(
ti)]
1 + exp[0.178 −0.910 ln(
ti)],
where standard deviations of the estimates are 0.246 and 0.138, respectively. The
negative and signiﬁcant coefﬁcient of ln(
ti) means that Ni is positively related
to the length of the duration
ti because a large ln(
ti) implies a small λi, which
--- page 297 ---

270
high-frequency data analysis and market microstructure
in turn implies higher probabilities for larger Ni; see the geometric distribution in
Eq. (5.27).
The ﬁtted model for Di is
µi = 0.049 −0.840Di−1 −0.004 ln(
ti),
ln(σi) = 0.244|Di−1 + Di−2 + Di−3 + Di−4|,
where standard deviations of the parameters in the mean equation are 0.129, 0.132,
and 0.082, respectively, whereas the standard error for the parameter in the variance
equation is 0.182. The price reversal is clearly shown by the highly signiﬁcant
negative coefﬁcient of Di−1. The marginally signiﬁcant parameter in the variance
equation is exactly as expected. Finally, the ﬁtted models for the size of a price
change are
ln(λd,i) = 1.024 −0.327Ni + 0.412 ln(
ti) −4.474Si−1,
ln(λu,i) = −3.683 −1.542Ni + 0.419 ln(
ti) + 0.921Si−1,
where standard deviations of the parameters for the “down size” are 3.350, 0.319,
0.599, and 3.188, respectively, whereas those for the “up size” are 1.734, 0.976,
0.453, and 1.459. The interesting estimates of the prior two equations are the
negative estimates of the coefﬁcient of Ni. A large Ni means there were more
transactions in the time interval (ti−1, ti) with no price change. This can be taken
as evidence of no new information available in the time interval (ti−1, ti). Consequently, the size for the price change at ti should be small. A small λu,i or λd,i for
a Poisson distribution gives precisely that.
In summary, granted that a sample of 194 observations in a given day may not
contain sufﬁcient information about the trading dynamics of IBM stock, but the
ﬁtted models appear to provide some sensible results. McCulloch and Tsay (2000)
extend the PCD model to a hierarchical framework to handle all the data of the
63 trading days between November 1, 1990, and January 31, 1991. Many of the
parameter estimates become signiﬁcant in this extended sample, which has more
than 19,000 observations. For example, the overall estimate of the coefﬁcient of
ln(
ti−1) in the model for time duration ranges from 0.04 to 0.1, which is small,
but signiﬁcant.
Finally, using transactions data to test microstructure theory often requires a
careful speciﬁcation of the variables used. It also requires a deep understanding of
the way by which the market operates and the data are collected. However, ideas of
the econometric models discussed in this chapter are useful and widely applicable
in analysis of high-frequency data.
5.8
APPLICATION
In this section we apply the ACD model to stock volatility modeling. Consider the
daily range of the log price of Apple stock from January 4, 1999, to November 20,
--- page 298 ---

application
271
2007. The data are obtained from Yahoo Finance and consist of 2235 observations.
This series was analyzed in Tsay (2009). The range of daily log prices has been
used in the literature as a robust alternative to volatility modeling; see Chapter 3
and Chou (2005) and the references therein. Apple stock had two-for-one splits on
June 21, 2000, and February 28, 2005, during the sample period, but no adjustments
are needed for the splits because we use daily range of log price. As mentioned
before, stock prices in the U.S. markets switched from the tick size
1
16 of a dollar
to the decimal system on January 29, 2001. Such a change affected the bid–ask
spread of stock prices. We shall employ intervention analysis to study the impact
of such a policy change on the stock volatility.
The sample mean, standard deviation, minimum, and maximum of the range
of log prices are 0.0407, 0.0218, 0.0068, and 0.1468, respectively. The sample
skewness and excess kurtosis are 1.3 and 2.13, respectively. Figure 5.18(a) shows
the time plot of the range series. The volatility seems to be increasing from 2000
to 2001, then decreasing to a stable level after 2002. It seems to increase somewhat
at the end of the series. Figure 5.19(a) shows the sample ACF of the daily range
series. The sample ACFs are highly signiﬁcant and decay slowly.
We ﬁt EACD(1,1), WACD(1,1), and GACD(1,1) models to the daily range
series. The estimation results, along with the Ljung–Box statistics for the standardized residual series and its squared process, are given in Table 5.9. The parameter
estimates for the duration equation are stable for all three models, except for the
Time
(a)
Range
2000
2002
2004
2006
2008
0.02 0.06 0.10 0.14
ε
1
2
3
4
Time
(b)
2000
2002
2004
2006
2008
Figure 5.18
Time plots of daily range of log price of Apple stock from January 4, 1999, to November
20, 2007: (a) observed daily range and (b) standardized residuals of a GACD(1,1) model.
--- page 299 ---

272
high-frequency data analysis and market microstructure
Lag
(a)
ACF
0
10
20
30
40
0.0
0.2
0.4
0.6
ACF
−0.2 −0.1 0.0
0.1
0.2
Lag
(b)
0
10
20
30
40
Figure 5.19
Sample autocorrelation function of daily range of log prices of Apple stock from January
4, 1999, to November 20, 2007: (a) ACF of daily range and (b) ACF of standardized residual series of
GACD(1,1) model.
TABLE 5.9
Estimation Results of EACD(1,1), WACD(1,1), and GACD(1,1) Models
for Daily Range of Log Prices of Apple Stock from January 4, 1999 to November 20,
2007a
Parameters
Checking
Model
α0
α1
β1
α
κ
Q(10)
Q∗(10)
EACD
0.0007
0.133
0.849
16.65
12.12
(0.0005)
(0.036)
(0.044)
(0.082)
(0.277)
WACD
0.0013
0.131
0.835
2.377
13.66
9.74
(0.0003)
(0.015)
(0.021)
(0.031)
(0.189)
(0.464)
GACD
0.0010
0.133
0.843
1.622
2.104
14.62
11.21
(0.0002)
(0.015)
(0.019)
(0.029)
(0.040)
(0.147)
(0.341)
aThe standard errors of the estimates and the p values of the Ljung–Box statistics are in parentheses,
where Q(10) and Q∗(10) are for standardized residual series and its squared process, respectively.
constant term of the EACD model, which appears to be statistically insigniﬁcant
at the usual 5% level. Indeed, in this particular instance, the EACD(1,1) model
fares slightly worse than the other two ACD models. Between the WACD(1,1) and
GACD(1,1) models, we slightly prefer the GACD(1,1) model because it ﬁts the
data better and is more ﬂexible.
--- page 300 ---

application
273
Figure 5.19(b) shows the sample ACFs of the standardized residuals of the
ﬁtted GACD(1,1) model. From the plot, the standardized residuals do not have
signiﬁcant serial correlations, even though the lag-1 sample ACF is slightly above
its two standard error limit. The lag-1 serial correlation is removed when we use
nonlinear ACD models later. Figure 5.18(b) shows the time plot of the standardized
residuals of the GACD(1,1) model. The residuals do not show any pattern of
model inadequacy. The mean, standard deviation, minimum, and maximum of the
standardized residuals are 0.203, 4.497, 0.999, and 0.436, respectively.
It is interesting to see that the estimates of the shape parameter α are greater
than 1 for both WACD(1,1) and GACD(1,1) models, indicating that the hazard
function of the daily range is monotonously increasing. This is consistent with the
idea of volatility clustering, for large volatility tends to be followed by another
large volatility.
Threshold ACD model
To reﬁne the GACD(1,1) model for the daily range of log prices of Apple stock,
we employ a two-regime threshold WACD(1,1) model. Some preliminary analysis
of the threshold WACD models indicates that the major difference in the parameter
estimates between the two regimes is the shape parameter of the Weibull distribution. Thus, we focus on a TWACD(2;1,1) model with different shape parameters
for the two regimes.
Table 5.10 gives the maximized log-likelihood value of a TWACD(2;1,1) model
with delay d = 1 and threshold r ∈{x(q)|q = 60, 65, . . . , 95}, where x(q) denotes
the sample qth percentile. From the table, the threshold 0.04753 is selected, which
is the 70th percentile of the data. The ﬁtted model is
xi = ψiϵi,
ψi = 0.0013 + 0.1539xi−1 + 0.8131ψi−1,
where the standard errors of the coefﬁcients are 0.0003, 0.0164, and 0.0215, respectively, and ϵi follows the standardized Weibull distribution as
ϵi ∼

W(2.2756)
if xi−1 ≤0.04753,
W(2.7119)
otherwise,
where the standard errors of the two shape parameters are 0.0394 and 0.0717,
respectively.
TABLE 5.10
Selection of Threshold of TWACD(2;1,1) Model for Daily Range of
Log Prices of Apple Stock from January 4, 1999, to November 20, 2007a
Quantile
60
65
70
75
80
85
90
95
r × 100
4.03
4.37
4.75
5.15
5.58
6.16
7.07
8.47
ℓ(r) × 103
6.073
6.076
6.079
6.076
6.078
6.074
6.072
6.066
aThe threshold variable is xi−1.
--- page 301 ---

274
high-frequency data analysis and market microstructure
Time
(a)
E(range)
2000
2002
2004
2006
2008
0.02 0.04 0.06 0.08
Lag
(b)
r0$acf[2:41]
0
10
20
30
40
−0.2 −0.1 0.0
0.1
0.2
Figure 5.20
Model ﬁtting for daily range of log price of Apple stock from January 4, 1999, to
November 20, 2007: (a) conditional expected durations of ﬁtted TWACD(2;1,1) model and (b) sample
ACF of standardized residuals.
Figure 5.20(a) shows the time plot of the conditional expected duration for
the ﬁtted TWACD(2;1,1) model, that is, ˆψi, whereas Figure 5.20(b) gives the
residual ACFs for the ﬁtted model. All residual ACFs are within the two standard error limits. Indeed, we have Q(1) = 4.01(0.05) and Q(10) = 9.84(0.45) for
the standardized residuals and Q∗(1) = 0.83(0.36) and Q∗(10) = 9.35(0.50) for
the squared series of the standardized residuals, where the number in parentheses
denotes p value. Note that the threshold variable xi−1 is also selected based on the
value of the log-likelihood function. For instance, the log-likelihood function of
the TWACD(2;1,1) model assumes the value 6.069×103 and 6.070 × 103, respectively, for d = 2 and 3 when the threshold is 0.04753. These values are lower than
that when d = 1.
Intervention Analysis
High-frequency ﬁnancial data are often inﬂuenced by external events, for example,
an increase or drop in interest rates by the U.S. Federal Open Market Committee
or a jump in the oil price. Applications of ACD models in ﬁnance are often faced
with the problem of outside interventions. To handle the effects of external events,
the intervention analysis of Box and Tiao (1975) can be used. Here we apply the
analysis to the daily range series of Apple stock to study the impact of change in
tick size on the stock volatility.
--- page 302 ---

application
275
Let to be the time of intervention. For the Apple stock, to = 522, which corresponds to January 26, 2001, the last trading day before the change in tick size.
Since more observations in the sample are after the intervention, we deﬁne the
indicator variable
I (to)
i
=

1
if i ≤to,
0
otherwise,
to signify the absence of intervention. Since a larger tick size tends to increase the
observed daily price range, it is reasonable to assume that the conditional expected
range would be higher before the intervention. A simple intervention model for the
daily range of Apple stock is then given by
xi = ψi

ϵ1i
if xi−1 ≤0.04753,
ϵ2i
otherwise,
where ψi follows the model
ψi = α0 + γ I (to)
i
+ α1xi−1 + β1ψi−1,
(5.54)
where γ denotes the decrease in expected duration due to the decimalization of
stock prices. In other words, the expected durations before and after the intervention
are
α0 + γ
1 −α1 −β1
and
α0
1 −α1 −β1
,
respectively. We expect γ > 0.
The ﬁtted duration equation for the intervention model is
ψi = 0.0021 + 0.0011I (522)
i
+ 0.1595xi−1 + 0.7828ψi−1,
where the standard errors of the estimates are 0.0004, 0.0003, 0.0177, and 0.0264,
respectively. The estimate ˆγ is signiﬁcant at the 1% level. For the innovations, we
have
ϵi ∼

W(2.2835)
if xi−1 ≤0.04753,
W(2.7322)
otherwise.
The standard errors of the two estimates of the shape parameter are 0.0413 and
0.0780, respectively. Figure 5.21(a) shows the expected durations of the intervention model, and Figure 5.21(b) shows the ACF of the standardized residuals.
All residual ACFs are within the two standard error limits. Indeed, for the standardized residuals, we have Q(1) = 2.37(0.12) and Q(10) = 6.24(0.79). For
the squared series of the standardized residuals, we have Q∗(1) = 0.34(0.56) and
Q∗(10) = 6.79(0.75). As expected, ˆγ > 0 so that the decimalization indeed reduces
the expected value of the daily range. This simple analysis shows that, as expected,
adopting the decimal system reduces the volatility of Apple stock.
--- page 303 ---

276
high-frequency data analysis and market microstructure
Time
(a)
E(duration)
2000
2002
2004
2006
2008
0.02 0.04 0.06 0.08
Lag
(b)
ACF
0
10
20
30
40
−0.2 −0.1 0.0
0.1
0.2
Figure 5.21
Model ﬁtting for daily range of log price of Apple stock from January 4, 1999, to
November 20, 2007: (a) conditional expected durations of ﬁtted TWACD(2;1,1) model with intervention
and (b) sample ACF of corresponding standardized residuals.
APPENDIX A: REVIEW OF SOME PROBABILITY DISTRIBUTIONS
Exponential Distribution
A random variable X has an exponential distribution with parameter β > 0 if its
probability density function (pdf) is given by
f (x|β) =



1
β e−x/β
if x ≥0,
0
otherwise.
Denoting such a distribution by X ∼exp(β), we have E(X) = β and Var(X) =
β2. The cumulative distribution function (CDF) of X is
F(x|β) =

0
if x < 0,
1 −e−x/β
if x ≥0.
When β = 1, X is said to have a standard exponential distribution.
--- page 304 ---

appendix a: review of some probability distributions
277
Gamma Function
For κ > 0, the gamma function (κ) is deﬁned by
(κ) =
 ∞
0
xκ−1e−x dx.
The most important properties of the gamma function are:
1. For any κ > 1, (κ) = (κ −1)(κ −1).
2. For any positive integer m, (m) = (m −1)!.
3. ( 1
2) = √π.
The integration
(y|κ) =
 y
0
xκ−1e−x dx,
y > 0
is an incomplete gamma function. Its values have been tabulated in the literature.
Computer programs are now available to evaluate the incomplete gamma function.
Gamma Distribution
A random variable X has a gamma distribution with parameter κ and β (κ > 0,
β > 0) if its pdf is given by
f (x|κ, β) =



1
βκ(κ)xκ−1e−x/β
if x ≥0,
0
otherwise.
By changing variable y = x/β, one can easily obtain the moments of X:
E(Xm) =
 ∞
0
xmf (x|κ, β) dx =
1
βκ(κ)
 ∞
0
xκ+m−1e−x/β dx
= βm
(κ)
 ∞
0
yκ+m−1e−y dy = βm(κ + m)
(κ)
.
In particular, the mean and variance of X are E(X) = κβ and Var(X) = κβ2. When
β = 1, the distribution is called a standard gamma distribution with parameter κ.
We use the notation G ∼gamma(κ) to denote that G follows a standard gamma
distribution with parameter κ. The moments of G are
E(Gm) = (κ + m)
(κ)
,
m > 0.
(5.55)
--- page 305 ---

278
high-frequency data analysis and market microstructure
Weibull Distribution
A random variable X has a Weibull distribution with parameters α and β (α > 0,
β > 0) if its pdf is given by
f (x|α, β) =



α
βα xα−1e−(x/β)α
if x ≥0,
0
if x < 0,
where β and α are the scale and shape parameters of the distribution. The mean
and variance of X are
E(X) = β

1 + 1
α

,
Var(X) = β2



1 + 2
α

−



1 + 1
α
	2+
,
and the CDF of X is
F(x|α, β) =

0
if x < 0,
1 −e−(x/β)α
if x ≥0.
When α = 1, the Weibull distribution reduces to an exponential distribution.
Deﬁne Y = X/[β(1 + 1/α)]. We have E(Y) = 1 and the pdf of Y is
f (y|α) =



α



1 + 1
α
	α
yα−1 exp

−



1 + 1
α

y
α"
if y ≥0,
0
otherwise,
(5.56)
where the scale parameter β disappears due to standardization. The CDF of the
standardized Weibull distribution is
F(y|α) =



0
if y < 0,
1 −exp

−



1 + 1
α

y
α"
if y > 0,
and we have E(Y) = 1 and Var(Y) = (1 + 2/α)/[(1 + 1/α)]2 −1. For a duration model with Weibull innovations, the pdf in Eq. (5.56) is used in the maximumlikelihood estimation.
Generalized Gamma Distribution
A random variable X has a generalized gamma distribution with parameter α, β, κ
(α > 0, β > 0, and κ > 0) if its pdf is given by
f (x|α, β, κ) =



αxκα−1
βκα(κ) exp

−
 x
β
	α
if x ≥0,
0
otherwise,
