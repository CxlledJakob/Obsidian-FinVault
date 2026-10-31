# Analysis of Financial Time Series, Third Edition (Wiley -- Ruey S_ Tsay -- Wiley series in probability and statistics, 3rd ed_, -- John Wiley & Sons, -- isbn13 9780470414354 -- 9f99b80c7b2dedd477f463dc5323f3b6 -- An.pdf — pages 172–191

--- page 172 ---

the exponential garch model
145
3.8.2
Illustrative Example
Nelson (1991) applies an EGARCH model to the daily excess returns of the valueweighted market index from the Center for Research in Security Prices from July
1962 to December 1987. The excess returns are obtained by removing monthly
Treasury bill returns from the value-weighted index returns, assuming that the
Treasury bill return was constant for each calendar day within a given month.
There are 6408 observations. Denote the excess return by rt. The model used is as
follows:
rt = φ0 + φ1rt−1 + cσ 2
t + at,
(3.29)
ln(σ 2
t ) = α0 + ln(1 + wNt) +
1 + βB
1 −α1B −α2B2 g(ϵt−1),
where σ 2
t is the conditional variance of at given Ft−1, Nt is the number of nontrading days between trading days t −1 and t, α0 and w are real parameters, g(ϵt) is
deﬁned in Eq. (3.24), and ϵt follows a generalized error distribution in Eq. (3.10).
Similar to a GARCH-M model, the parameter c in Eq. (3.29) is the risk premium
parameter. Table 3.3 gives the parameter estimates and their standard errors of the
model. The mean equation of model (3.29) has two features that are of interest.
First, it uses an AR(1) model to take care of possible serial correlation in the excess
returns. Second, it uses the volatility σ 2
t as a regressor to account for risk premium.
The estimated risk premium is negative, but statistically insigniﬁcant.
3.8.3
Second Example
As another illustration, we consider the monthly log returns of IBM stock from
January 1926 to December 1997 for 864 observations. An AR(1)–EGARCH(1,1)
model is entertained and the ﬁtted model is
rt = 0.0105 + 0.092rt−1 + at,
at = σtϵt,
(3.30)
ln(σ 2
t ) = −5.496 +
g(ϵt−1)
1 −0.856B ,
g(ϵt−1) = −0.0795ϵt−1 + 0.2647

|ϵt−1| −

2/π

,
(3.31)
TABLE 3.3
Estimated AR(1)–EGARCH(2,2) Model for Daily Excess Returns of
Value-Weighted CRSP Market Index: July 1962–December 1987
Parameter
α0
w
γ
α1
α2
β
Estimate
−10.06
0.183
0.156
1.929
−0.929
−0.978
Error
0.346
0.028
0.013
0.015
0.015
0.006
Parameter
θ
φ0
φ1
c
v
Estimate
−0.118
3.5·10−4
0.205
−3.361
1.576
Error
0.009
9.9·10−5
0.012
2.026
0.032
--- page 173 ---

146
conditional heteroscedastic models
where {ϵt} is a sequence of independent standard Gaussian random variates. All
parameter estimates are statistically signiﬁcant at the 5% level. For model checking, the Ljung–Box statistics give Q(10) = 6.31(0.71) and Q(20) = 21.4(0.32)
for the standardized residual process ˜at = at/σt and Q(10) = 4.13(0.90) and
Q(20) = 15.93(0.66) for the squared process ˜a2
t , where again the number in
parentheses denotes p value. Therefore, there is no serial correlation or conditional heteroscedasticity in the standardized residuals of the ﬁtted model. The prior
AR(1)–EGARCH(1,1) model is adequate.
From the estimated volatility equation in (3.31) and using √2/π ≈0.7979, we
obtain the volatility equation as
ln(σ 2
t ) = −1.001 + 0.856 ln(σ 2
t−1) +
 0.1852ϵt−1
if ϵt−1 ≥0,
−0.3442ϵt−1
if ϵt−1 < 0.
Taking antilog transformation, we have
σ 2
t = σ 2×0.856
t−1
e−1.001 ×
 e0.1852ϵt−1
if ϵt−1 ≥0,
e−0.3442ϵt−1
if ϵt−1 < 0.
This equation highlights the asymmetric responses in volatility to the past positive
and negative shocks under an EGARCH model. For example, for a standardized
shock with magnitude 2 (i.e., two standard deviations), we have
σ 2
t (ϵt−1 = −2)
σ 2
t (ϵt−1 = 2) = exp[−0.3442 × (−2)]
exp(0.1852 × 2)
= e0.318 = 1.374.
Therefore, the impact of a negative shock of size 2 standard deviations is about
37.4% higher than that of a positive shock of the same size. This example clearly
demonstrates the asymmetric feature of EGARCH models. In general, the bigger
the shock, the larger the difference in volatility impact.
Finally, we extend the sample period to include the log returns from 1998 to
2003 so that there are 936 observations and use S-Plus to ﬁt an EGARCH(1,1)
model. The results are given below.
S-Plus Demonstration
The following output has been edited:
> ibm.egarch=garch(ibmln∼1,∼egarch(1,1),leverage=T,
+ cond.dist=’ged’)
> summary(ibm.egarch)
Call:
garch(formula.mean = ibmln ∼1, formula.var = ∼egarch(1, 1),
leverage = T,cond.dist = "ged")
Mean Equation: ibmln ∼1
--- page 174 ---

the exponential garch model
147
Conditional Variance Equation: ∼egarch(1, 1)
Conditional Distribution:
ged
with estimated parameter 1.5003 and standard error 0.09912
--------------------------------------------------------------
Estimated Coefficients:
--------------------------------------------------------------
Value Std.Error t value
Pr(>|t|)
C
0.01181
0.002012
5.870 3.033e-09
A -0.55680
0.171602
-3.245 6.088e-04
ARCH(1)
0.22025
0.052824
4.169 1.669e-05
GARCH(1)
0.92910
0.026743
34.742 0.000e+00
LEV(1) -0.26400
0.126096
-2.094 1.828e-02
--------------------------------------------------------------
Ljung-Box test for standardized residuals:
--------------------------------------------------------------
Statistic P-value Chi^2-d.f.
17.87
0.1195
12
Ljung-Box test for squared standardized residuals:
--------------------------------------------------------------
Statistic P-value Chi^2-d.f.
6.723
0.8754
12
The ﬁtted GARCH(1,1) model is
rt = 0.0118 + at,
at = σtϵt,
ln(σ 2
t ) = −0.557 + 0.220|at−1| −0.264at−1
σt−1
+ 0.929 ln(σ 2
t−1),
(3.32)
where ϵt follows a GED distribution with parameter 1.5. This model is adequate
and based on the Ljung–Box statistics of the standardized residual series and its
squared process. As expected, the output shows that the estimated leverage effect
is negative and is statistically signiﬁcant at the 5% level with a t ratio of −2.094.
3.8.4
Forecasting Using an EGARCH Model
We use the EGARCH(1,1) model to illustrate multistep-ahead forecasts of
EGARCH models, assuming that the model parameters are known and the
innovations are standard Gaussian. For such a model, we have
ln(σ 2
t ) = (1 −α1)α0 + α1 ln(σ 2
t−1) + g(ϵt−1),
g(ϵt−1) = θϵt−1 + γ (|ϵt−1| −

2/π).
Taking exponentials, the model becomes
σ 2
t = σ 2α1
t−1 exp[(1 −α1)α0] exp[g(ϵt−1)],
g(ϵt−1) = θϵt−1 + γ (|ϵt−1| −

2/π).
(3.33)
--- page 175 ---

148
conditional heteroscedastic models
Let h be the forecast origin. For the 1-step-ahead forecast, we have
σ 2
h+1 = σ 2α1
h
exp[(1 −α1)α0] exp[g(ϵh)],
where all of the quantities on the right-hand side are known. Thus, the 1-step-ahead
volatility forecast at the forecast origin h is simply ˆσ 2
h(1) = σ 2
h+1 given earlier. For
the 2-step-ahead forecast, Eq. (3.33) gives
σ 2
h+2 = σ 2α1
h+1 exp[(1 −α1)α0] exp[g(ϵh+1)].
Taking conditional expectation at time h, we have
ˆσ 2
h(2) = ˆσ 2α1
h
(1) exp[(1 −α1)α0]Eh{exp[g(ϵh+1)]},
where Eh denotes a conditional expectation taken at the time origin h. The prior
expectation can be obtained as follows:
E{exp[g(ϵ)]} =
 ∞
−∞
exp[θϵ + γ (|ϵ| −

2/π)]f (ϵ) dϵ
= exp

−γ

2/π

 ∞
0
e(θ+γ )ϵ
1
√
2π
e−ϵ2/2 dϵ
+
 0
−∞
e(θ−γ )ϵ
1
√
2π
e−ϵ2/2 dϵ

= exp

−γ

2/π

e(θ+γ )2/2(θ + γ ) + e(θ−γ )2/2(γ −θ)
!
,
where f (ϵ) and (x) are the probability density function and CDF of the standard normal distribution, respectively. Consequently, the 2-step-ahead volatility
forecast is
ˆσ 2
h(2) = ˆσ 2α1
h
(1) exp

(1 −α1)α0 −γ

2/π
!
×
'
exp[(θ + γ )2/2](θ + γ ) + exp[(θ −γ )2/2](γ −θ)
(
.
Repeating the previous procedure, we obtain a recursive formula for a j-step-ahead
forecast:
ˆσ 2
h(j) = )
σ 2α1
h
(j −1) exp(ω)
×
'
exp[(θ + γ )2/2](θ + γ ) + exp[(θ −γ )2/2](γ −θ)
(
,
where ω = (1 −α1)α0 −γ √2/π. The values of (θ + γ ) and (γ −θ) can be
obtained from most statistical packages. Alternatively, accurate approximations to
these values can be obtained by using the method in Appendix B of Chapter 6.
--- page 176 ---

the threshold garch model
149
For illustration, consider the AR(1)–EGARCH(1,1) model of the previous
section for the monthly log returns of IBM stock, ending December 1997. Using
the ﬁtted EGARCH(1,1) model, we can compute the volatility forecasts for the
series. At the forecast origin t = 864, the forecasts are ˆσ 2
864(1) = 6.05 × 10−3,
ˆσ 2
864(2) = 5.82 × 10−3, ˆσ 2
864(3) = 5.63 × 10−3, and ˆσ 2
864(10) = 4.94 × 10−3.
These forecasts converge gradually to the sample variance 4.37 × 10−3 of the
shock process at of Eq. (3.30).
3.9
THE THRESHOLD GARCH MODEL
Another volatility model commonly used to handle leverage effects is the threshold
GARCH (or TGARCH) model; see Glosten, Jagannathan, and Runkle (1993) and
Zakoian (1994). A TGARCH(m, s) model assumes the form
σ 2
t = α0 +
s

i=1
(αi + γiNt−i)a2
t−i +
m

j=1
βjσ 2
t−j,
(3.34)
where Nt−i is an indicator for negative at−i, that is,
Nt−i =
 1
if at−i < 0,
0
if at−i ≥0,
and αi, γi, and βj are nonnegative parameters satisfying conditions similar to those
of GARCH models. From the model, it is seen that a positive at−i contributes αia2
t−i
to σ 2
t , whereas a negative at−i has a larger impact (αi + γi)a2
t−i with γi > 0. The
model uses zero as its threshold to separate the impacts of past shocks. Other
threshold values can also be used; see Chapter 4 for the general concept of threshold
models. Model (3.34) is also called the GJR model because Glosten et al. (1993)
proposed essentially the same model.
For illustration, consider the monthly log returns of IBM stock from 1926 to
2003. The ﬁtted TGARCH(1,1) model with conditional GED innovations is
rt = 0.0121 + at,
at = σtϵt,
σ 2
t = 3.45 × 10−4 + (0.0658 + 0.0843Nt−1)a2
t−1 + 0.8182σ 2
t−1,
(3.35)
where the estimated parameter of the GED is 1.51 with standard error 0.099. The
standard error of the parameter for the mean equation is 0.002 and the standard
errors of the parameters in the volatility equation are 1.26×−4, 0.0314, 0.0395, and
0.049, respectively. To check the ﬁtted model, we have Q(12) = 18.34(0.106) for
the standardized residual ˜at and Q(12) = 5.36 (0.95) for ˜a2
t . The model is adequate
in modeling the ﬁrst two conditional moments of the log return series. Based on
the ﬁtted model, the leverage effect is signiﬁcant at the 5% level.
--- page 177 ---

150
conditional heteroscedastic models
S-Plus Commands Used
> ibm.tgarch = garch(ibmln∼1,∼tgarch(1,1),leverage=T,
+ cond.dist=’ged’)
> summary(ibm.tgarch)
> plot(ibm.tgarch)
It is interesting to compare the two models in Eqs. (3.32) and (3.35) for the
monthly log returns of IBM stock. Assume that at−1 = ±2σt−1 so that ϵt−1 = ±2.
The EGARCH(1,1) model gives
σ 2
t (ϵt−1 = −2)
σ 2
t (ϵt−1 = 2) = e0.22×2×0.632 ≈1.264.
On the other hand, ignoring the constant term 0.000345, the TGARCH(1,1) model
gives
σ 2
t (ϵt−1 = −2)
σ 2
t (ϵt−1 = 2) ≈[(0.0658 + 0.0843)4 + 0.8182]σ 2
t−1
(0.0658 × 4 + 0.8182)σ 2
t−1
= 1.312.
The two models provide similar leverage effects.
3.10
THE CHARMA MODEL
Many other econometric models have been proposed in the literature to describe the
evolution of the conditional variance σ 2
t in Eq. (3.2). We mention the conditional
heteroscedastic ARMA (CHARMA) model that uses random coefﬁcients to produce
conditional heteroscedasticity; see Tsay (1987). The CHARMA model is not the
same as the ARCH model, but the two models have similar second-order conditional
properties. A CHARMA model is deﬁned as
rt = µt + at,
at = δ1tat−1 + δ2tat−2 + · · · + δmtat−m + ηt,
(3.36)
where {ηt} is a Gaussian white noise series with mean zero and variance σ 2
η ,
{δt} = {(δ1t, . . . , δmt)′} is a sequence of iid random vectors with mean zero and
nonnegative deﬁnite covariance matrix , and {δt} is independent of {ηt}. In this
section, we use some basic properties of vector and matrix operations to simplify
the presentation. Readers may consult Appendix A of Chapter 8 for a brief review
of these properties. For m > 0, the model can be written as
at = a′
t−1δt + ηt,
where at−1 = (at−1, . . . , at−m)′ is a vector of lagged values of at and is available
at time t −1. The conditional variance of at of the CHARMA model in Eq. (3.36)
--- page 178 ---

the charma model
151
is then
σ 2
t = σ 2
η + a′
t−1Cov(δt)at−1
= σ 2
η + (at−1, . . . , at−m)(at−1, . . . , at−m)′.
(3.37)
Denote the (i, j)th element of  by ωij. Because the matrix is symmetric, we have
ωij = ωji. If m = 1, then Eq. (3.37) reduces to σ 2
t = σ 2
η + ω11a2
t−1, which is an
ARCH(1) model. If m = 2, then Eq. (3.37) reduces to
σ 2
t = σ 2
η + ω11a2
t−1 + 2ω12at−1at−2 + ω22a2
t−2,
which differs from an ARCH(2) model by the cross-product term at−1at−2. In
general, the conditional variance of a CHARMA(m) model is equivalent to that
of an ARCH(m) model if  is a diagonal matrix. Because  is a covariance
matrix, which is nonnegative deﬁnite, and σ 2
η is a variance, which is positive, we
have σ 2
t ≥σ 2
η > 0 for all t. In other words, the positiveness of σ 2
t is automatically
satisﬁed under a CHARMA model.
An obvious difference between ARCH and CHARMA models is that the latter
use cross products of the lagged values of at in the volatility equation. The crossproduct terms might be useful in some applications. For example, in modeling
an asset return series, cross-product terms denote interactions between previous
returns. It is conceivable that stock volatility may depend on such interactions.
However, the number of cross-product terms increases rapidly with the order m,
and some constraints are needed to keep the model simple. A possible constraint
is to use a small number of cross-product terms in a CHARMA model. Another
difference between the two models is that higher order properties of CHARMA
models are harder to obtain than those of ARCH models because it is in general
harder to handle multiple random variables.
For illustration, we employ the CHARMA model
rt = φ0 + at,
at = δ1tat−1 + δ2tat−2 + ηt
for the monthly excess returns of the S&P 500 index used before in GARCH
modeling. The ﬁtted model is
rt = 0.00635 + at,
σ 2
t = 0.00179 + (at−1, at−2)(at−1, at−2)′,
where
 =

0.1417(0.0333)
−0.0594(0.0365)
−0.0594(0.0365)
0.3081(0.0340)

,
where the numbers in parentheses are standard errors. The cross-product term of
 has a t ratio of −1.63, which is marginally signiﬁcant at the 10% level. If we
reﬁne the model to
rt = φ0 + at,
at = δ1tat−1 + δ2tat−2 + δ3tat−3 + ηt,
--- page 179 ---

152
conditional heteroscedastic models
but assume that δ3t is uncorrelated with (δ1t, δ2t), then we obtain the ﬁtted model
rt = 0.0068 + at,
σ 2
t = 0.00136 + (at−1, at−2, at−3)(at−1, at−2, at−3)′,
where the elements of  and their standard errors, shown in parentheses, are
 =


0.1212(0.0355)
−0.0622(0.0283)
0
−0.0622(0.0283)
0.1913(0.0254)
0
0
0
0.2988(0.0420)

.
All of the estimates are now statistically signiﬁcant at the 5% level. From the model,
at = rt −0.0068 is the deviation of the monthly excess return from its average.
The ﬁtted CHARMA model shows that there is some interaction effect between
the ﬁrst two lagged deviations. Indeed, the volatility equation can be written
approximately as
σ 2
t = 0.00136 + 0.12a2
t−1 −0.12at−1at−2 + 0.19a2
t−2 + 0.30a2
t−3.
The conditional variance is slightly larger when at−1at−2 is negative.
3.10.1
Effects of Explanatory Variables
The CHARMA model can easily be generalized so that the volatility of rt may
depend on some explanatory variables. Let {xit}m
i=1 be m explanatory variables
available at time t. Consider the model
rt = µt + at,
at =
m

i=1
δitxi,t−1 + ηt,
(3.38)
where δt = (δ1t, . . . , δmt)′ and ηt are random vector and variable deﬁned in Eq.
(3.36). Then the conditional variance of at is
σ 2
t = σ 2
η + (x1,t−1, . . . , xm,t−1)(x1,t−1, . . . , xm,t−1)′.
In application, the explanatory variables may include some lagged values of at.
3.11
RANDOM COEFFICIENT AUTOREGRESSIVE MODELS
In the literature, the random coefﬁcient autoregressive (RCA) model is introduced
to account for variability among different subjects under study, similar to the panel
data analysis in econometrics and the hierarchical model in statistics. We classify
the RCA model as a conditional heteroscedastic model, but historically it is used
to obtain a better description of the conditional mean equation of the process by
--- page 180 ---

stochastic volatility model
153
allowing for the parameters to evolve over time. A time series rt is said to follow
an RCA(p) model if it satisﬁes
rt = φ0 +
p

i=1
(φi + δit)rt−i + at,
(3.39)
where p is a positive integer, {δt} = {(δ1t, . . . , δpt)′} is a sequence of independent
random vectors with mean zero and covariance matrix δ, and {δt} is independent
of {at}; see Nicholls and Quinn (1982) for further discussions of the model. The
conditional mean and variance of the RCA model in Eq. (3.39) are
µt = E(rt|Ft−1) = φ0 +
p

i=1
φirt−i,
σ 2
t = σ 2
a + (rt−1, . . . , rt−p)δ(rt−1, . . . , rt−p)′,
which is in the same form as that of a CHARMA model. However, there is a subtle
difference between RCA and CHARMA models. For the RCA model, the volatility
is a quadratic function of the observed lagged values rt−i. Yet the volatility is a
quadratic function of the lagged innovations at−i in a CHARMA model.
3.12
STOCHASTIC VOLATILITY MODEL
An alternative approach to describe the volatility evolution of a ﬁnancial time
series is to introduce an innovation to the conditional variance equation of at; see
Melino and Turnbull (1990), Taylor (1994), Harvey, Ruiz, and Shephard (1994), and
Jacquier, Polson, and Rossi (1994). The resulting model is referred to as a stochastic
volatility (SV) model. Similar to EGARCH models, to ensure positiveness of the
conditional variance, SV models use ln(σ 2
t ) instead of σ 2
t . A SV model is deﬁned as
at = σtϵt,
(1 −α1B −· · · −αmBm) ln(σ 2
t ) = α0 + vt,
(3.40)
where the ϵt are iid N(0, 1), the vt are iid N(0, σ 2
v ), {ϵt} and {vt} are independent,
α0 is a constant, and all zeros of the polynomial 1 −m
i=1 αiBi are greater than
1 in modulus. Adding the innovation vt substantially increases the ﬂexibility of
the model in describing the evolution of σ 2
t , but it also increases the difﬁculty
in parameter estimation. To estimate an SV model, we need a quasi-likelihood
method via Kalman ﬁltering or a Monte Carlo method. Jacquier, Polson, and Rossi
(1994) provide some comparison of estimation results between quasi-likelihood and
Markov chain Monte Carlo (MCMC) methods. The difﬁculty in estimating an SV
model is understandable because for each shock at the model uses two innovations
ϵt and vt. We discuss an MCMC method to estimate SV models in Chapter 12.
For more discussions on stochastic volatility models, see Taylor (1994).
--- page 181 ---

154
conditional heteroscedastic models
The appendixes of Jacquier, Polson, and Rossi (1994) provide some properties
of the SV model when m = 1. For instance, with m = 1, we have
ln(σ 2
t ) ∼N

α0
1 −α1
,
σ 2
v
1 −α2
1

≡N(µh, σ 2
h),
and E(a2
t ) = exp(µh + σ 2
h/2), E(a4
t ) = 3 exp(2µ2
h + 2σ 2
h), and corr(a2
t , a2
t−i) =
[exp(σ 2
hαi
1) −1]/[3 exp(σ 2
h) −1]. Limited experience shows that SV models often
provided improvements in model ﬁtting, but their contributions to out-of-sample
volatility forecasts received mixed results.
3.13
LONG-MEMORY STOCHASTIC VOLATILITY MODEL
More recently, the SV model is further extended to allow for long memory in
volatility, using the idea of fractional difference. As stated in Chapter 2, a time
series is a long-memory process if its autocorrelation function decays at a hyperbolic, instead of an exponential, rate as the lag increases. The extension to longmemory models in volatility study is motivated by the fact that the autocorrelation
function of the squared or absolute-valued series of an asset return often decays
slowly, even though the return series has no serial correlation; see Ding, Granger,
and Engle (1993). Figure 3.10 shows the sample ACF of the daily absolute returns
for IBM stock and the S&P 500 index from July 3, 1962, to December 31, 2003.
These sample ACFs are positive with moderate magnitude but decay slowly.
A simple long-memory stochastic volatility (LMSV) model can be written as
at = σtϵt,
σt = σ exp(ut/2),
(1 −B)dut = ηt,
(3.41)
where σ > 0, the ϵt are iid N(0, 1), the ηt are iid N(0, σ 2
η ) and independent of ϵt,
and 0 < d < 0.5. The feature of long memory stems from the fractional difference
(1 −B)d, which implies that the ACF of ut decays slowly at a hyperbolic, instead
of an exponential, rate as the lag increases. For model (3.41), we have
ln(a2
t ) = ln(σ 2) + ut + ln(ϵ2
t )
= [ln(σ 2) + E(ln ϵ2
t )] + ut + [ln(ϵ2
t ) −E(ln ϵ2
t )]
≡µ + ut + et.
Thus, the ln(a2
t ) series is a Gaussian long-memory signal plus a non-Gaussian white
noise; see Breidt, Crato, and de Lima (1998). Estimation of the LMSV model is
complicated, but the fractional difference parameter d can be estimated by using
either a quasi-maximum-likelihood method or a regression method. Using the log
series of squared daily returns for companies in the S&P 500 index, Bollerslev and
Jubinski (1999) and Ray and Tsay (2000) found that the median estimate of d is
about 0.38. For applications, Ray and Tsay (2000) studied common long-memory
--- page 182 ---

application
155
Lag
(a)
ACF
0
50
100
150
200
−0.1
0.1 0.2 0.3 0.4
Lag
(b)
ACF
0
50
100
150
200
−0.1
0.1 0.2 0.3 0.4
Figure 3.10
Sample ACF of daily absolute log returns for (a) S&P 500 index and (b) IBM stock for
period from July 3, 1962, to December 31, 2003. Two horizontal lines denote asymptotic 5% limits.
components in daily stock volatilities of groups of companies classiﬁed by various
characteristics. They found that companies in the same industrial or business sector
tend to have more common long-memory components (e.g., big U.S. national banks
and ﬁnancial institutions).
3.14
APPLICATION
In this section, we apply the volatility models discussed in this chapter to investigate
some problems of practical importance. The data used are the monthly log returns
of IBM stock and the S&P 500 index from January 1926 to December 1999. There
are 888 observations, and the returns are in percentages and include dividends.
Figure 3.11 shows the time plots of the two return series. Note that the result of
this section was obtained by the RATS program.
Example 3.4.
The questions we address here are whether the daily volatility
of a stock is lower in the summer and, if so, by how much. Afﬁrmative answers
to these two questions have practical implications in stock option pricing. We use
the monthly log returns of IBM stock shown in Figure 3.11(a) as an illustrative
example.
--- page 183 ---

156
conditional heteroscedastic models
Year
(a)
Log return
1940
1960
1980
2000
−30
−10 0 10 20 30
Log return
−20
0
20
Year
(b)
1940
1960
1980
2000
Figure 3.11
Time plots of monthly log returns for (a) IBM stock and (b) S&P 500 index. Sample
period is from January 1926 to December 1999. Returns are in percentages and include dividends.
Denote the monthly log return series by rt. If Gaussian GARCH models are
entertained, we obtain the GARCH(1,1) model:
rt = 1.23 + 0.099rt−1 + at,
at = σtϵt,
σ 2
t = 3.206 + 0.103a2
t−1 + 0.825σ 2
t−1,
(3.42)
for the series. The standard errors of the two parameters in the mean equation
are 0.222 and 0.037, respectively, whereas those of the parameters in the volatility
equation are 0.947, 0.021, and 0.037, respectively. Using the standardized residuals
˜at = at/σt, we obtain Q(10) = 7.82(0.553) and Q(20) = 21.22(0.325), where the
p value is in parentheses. Therefore, there are no serial correlations in the residuals
of the mean equation. The Ljung–Box statistics of the ˜a2
t series show Q(10) =
2.89(0.98) and Q(20) = 7.26(0.99), indicating that the standardized residuals have
no conditional heteroscedasticity. The ﬁtted model seems adequate. This model
serves as a starting point for further study.
To study the summer effect on stock volatility of an asset, we deﬁne an indicator
variable
ut =
 1
if t is June, July, or August,
0
otherwise,
(3.43)
--- page 184 ---

application
157
and modify the volatility equation to
σ 2
t = α0 + α1a2
t−1 + β1σ 2
t−1 + ut(α00 + α10a2
t−1 + β10σ 2
t−1).
This equation uses two GARCH(1,1) models to describe the volatility of a stock
return; one model for the summer months and the other for the remaining months.
For the monthly log returns of IBM stock, estimation results show that the estimates
of α10 and β10 are statistically nonsigniﬁcant at the 10% level. Therefore, we reﬁne
the equation and obtain the model
rt = 1.21 + 0.099rt−1 + at,
at = σtϵt,
σ 2
t = 4.539 + 0.113a2
t−1 + 0.816σ 2
t−1 −5.154ut.
(3.44)
The standard errors of the parameters in the mean equation are 0.218 and 0.037,
respectively, and those of the parameters in the volatility equation are 1.071, 0.022,
0.037, and 1.900, respectively. The Ljung–Box statistics for the standardized residuals ˜at = at/σt show Q(10) = 7.66(0.569) and Q(20) = 21.64(0.302). Therefore,
there are no serial correlations in the standardized residuals. The Ljung–Box
statistics for ˜a2
t give Q(10) = 3.38(0.97) and Q(20) = 6.82(0.99), indicating
no conditional heteroscedasticity in the standardized residuals either. The reﬁned
model seems adequate.
Comparing the volatility models in Eqs. (3.42) and (3.44), we obtain the following conclusions. First, because the coefﬁcient −5.514 is signiﬁcantly different from
zero with a p value of 0.0067, the summer effect on stock volatility is statistically
signiﬁcant at the 1% level. Furthermore, the negative sign of the estimate conﬁrms
that the volatility of IBM monthly log stock returns is indeed lower during the
summer. Second, rewrite the volatility model in Eq. (3.44) as
σ 2
t =
 −0.615 + 0.113a2
t−1 + 0.816σ 2
t−1
if t is June, July,or August,
4.539 + 0.113a2
t−1 + 0.816σ 2
t−1
otherwise.
The negative constant term −0.615 = 4.539 −5.514 is counterintuitive. However,
since the standard errors of 4.539 and 5.514 are relatively large, the estimated
difference −0.615 might not be signiﬁcantly different from zero. To verify the
assertion, we reﬁt the model by imposing the constraint that the constant term of
the volatility equation is zero for the summer months. This can easily be done by
using the equation
σ 2
t = α1a2
t−1 + β1σ 2
t−1 + γ (1 −ut).
The ﬁtted model is
rt = 1.21 + 0.099rt−1 + at,
at = σtϵt,
σ 2
t = 0.114a2
t−1 + 0.811σ 2
t−1 + 4.552(1 −ut).
(3.45)
--- page 185 ---

158
conditional heteroscedastic models
The standard errors of the parameters in the mean equation are 0.219 and 0.038,
respectively, and those of the parameters in the volatility equation are 0.022, 0.034,
and 1.094, respectively. The Ljung–Box statistics of the standardized residuals
show Q(10) = 7.68 and Q(20) = 21.67, and those of the ˜a2
t series give Q(10) =
3.17 and Q(20) = 6.85. These test statistics are close to what we had before and
are not signiﬁcant at the 5% level.
The volatility Eq. (3.45) can readily be used to assess the summer effect on the
IBM stock volatility. For illustration, based on the model in Eq. (3.45) the medians
of a2
t and σ 2
t are 29.4 and 75.1, respectively, for the IBM monthly log returns
in 1999. Using these values, we have σ 2
t = 0.114 × 29.4 + 0.811 × 75.1 = 64.3
for the summer months and σ 2
t = 68.8 for the other months. The ratio of the two
volatilities is 64.3/68.8 ≈93%. Thus, there is a 7% reduction in the volatility of
the monthly log return of IBM stock in the summer months.
Example 3.5.
The S&P 500 index is widely used in the derivative markets.
As such, modeling its volatility is a subject of intensive study. The question we
ask in this example is whether the past returns of individual components of the
index contribute to the modeling of the S&P 500 index volatility in the presence
of its own returns. A thorough investigation on this topic is beyond the scope of
this chapter, but we use the past returns of IBM stock as explanatory variables to
address the question.
The data used are shown in Figure 3.11. Denote by rt the monthly log return
series of the S&P 500 index. Using the rt series and Gaussian GARCH models,
we obtain the following special GARCH(2,1) model:
rt = 0.609 + at,
at = σtϵt,
σ 2
t = 0.717 + 0.147a2
t−2 + 0.839σ 2
t−1.
(3.46)
The standard error of the constant term in the mean equation is 0.138, and those of
the parameters in the volatility equation are 0.214, 0.021, and 0.017, respectively.
Based on the standardized residuals ˜at = at/σt, we have Q(10) = 11.51(0.32) and
Q(20) = 23.71(0.26), where the number in parentheses denotes the p value. For
the ˜a2
t series, we have Q(10) = 9.42(0.49) and Q(20) = 13.01(0.88). Therefore,
the model seems adequate at the 5% signiﬁcance level.
Next, we evaluate the contributions, if any, of using the past returns of IBM
stock, which is a component of the S&P 500 index, in modeling the index volatility.
As a simple illustration, we modify the volatility equation as
σ 2
t = α0 + α2a2
t−2 + β1σ 2
t−1 + γ (xt−1 −1.24)2,
where xt is the monthly log return of IBM stock and 1.24 is the sample mean of
xt. The ﬁtted model for rt becomes
rt = 0.616 + at,
at = σtϵt,
σ 2
t = 1.069 + 0.148a2
t−2 + 0.834σ 2
t−1 −0.007(xt−1 −1.24)2.
(3.47)
--- page 186 ---

alternative approaches
159
TABLE 3.4
Fitted Volatilities for Monthly Log Returns of S&P 500 Index from July
to December 1999 Using Models with and without Past Log Return of IBM Stock
Month
7/99
8/99
9/99
10/99
11/99
12/99
Model (3.46)
26.30
26.01
24.73
21.69
20.71
22.46
Model (3.47)
23.32
23.13
22.46
20.00
19.45
18.27
The standard error of the parameter in the mean equation is 0.139 and the standard
errors of the parameters in the volatility equation are 0.271, 0.020, 0.018, and
0.002, respectively. For model checking, we have Q(10) = 11.39(0.33) and Q(20)
= 23.63(0.26) for the standardized residuals ˜at = at/σt and Q(10) = 9.35(0.50)
and Q(20) = 13.51(0.85) for the ˜a2
t series. Therefore, the model is adequate.
Since the p value for testing γ = 0 is 0.0039, the contribution of the lag-1
IBM stock return to the S&P 500 index volatility is statistically signiﬁcant at the
1% level. The negative sign is understandable because it implies that using the
lag-1 past return of IBM stock reduces the volatility of the S&P 500 index return.
Table 3.4 gives the ﬁtted volatility of the S&P 500 index from July to December
of 1999 using models (3.46) and (3.47). From the table, the past value of IBM log
stock return indeed contributes to the modeling of the S&P 500 index volatility.
3.15
ALTERNATIVE APPROACHES
In this section, we discuss two alternative methods to volatility modeling.
3.15.1
Use of High-Frequency Data
French, Schwert, and Stambaugh (1987) consider an alternative approach for
volatility estimation that uses high-frequency data to calculate volatility of
low-frequency returns. In recent years, this approach has attracted substantial
interest due to the availability of high-frequency ﬁnancial data; see Andersen,
Bollerslev, Diebold, and Labys (2001a, 2001b).
Suppose that we are interested in the monthly volatility of an asset for which
daily returns are available. Let rm
t
be the monthly log return of the asset at month
t. Assume that there are n trading days in month t and the daily log returns of the
asset in the month are {rt,i}n
i=1. Using properties of log returns, we have
rm
t =
n

i=1
rt,i.
Assuming that the conditional variance and covariance exist, we have
Var(rm
t |Ft−1) =
n

i=1
Var(rt,i|Ft−1) + 2

i<j
Cov[(rt,i, rt,j)|Ft−1],
(3.48)
--- page 187 ---

160
conditional heteroscedastic models
where Ft−1 denotes the information available at month t −1 (inclusive). The prior
equation can be simpliﬁed if additional assumptions are made. For example, if we
assume that {rt,i} is a white noise series, then
Var(rm
t |Ft−1) = nVar(rt,1),
where Var(rt,1) can be estimated from the daily returns {rt,i}n
i=1 by
ˆσ 2 =
n
i=1(rt,i −¯rt)2
n −1
,
where ¯rt
is the sample mean of the daily log returns in month t
[i.e.,
¯rt = (n
i=1 rt,i)/n]. The estimated monthly volatility is then
ˆσ 2
m =
n
n −1
n

i=1
(rt,i −¯rt)2.
(3.49)
If {rt,i} follows an MA(1) model, then
Var(rm
t |Ft−1) = nVar(rt,1) + 2(n −1)Cov(rt,1, rt,2),
which can be estimated by
ˆσ 2
m =
n
n −1
n

i=1
(rt,i −¯rt)2 + 2
n−1

i=1
(rt,i −¯rt)(rt,i+1 −¯rt).
(3.50)
The previous approach for volatility estimation is simple, but it encounters several
difﬁculties in practice. First, the model for daily returns {rt,i} is unknown. This
complicates the estimation of covariances in Eq. (3.48). Second, there are roughly
21 trading days in a month, resulting in a small sample size. The accuracy of
the estimates of variance and covariance in Eq. (3.48) might be questionable. The
accuracy depends on the dynamic structure of {rt,i} and their distribution. If the
daily log returns have high excess kurtosis and serial correlations, then the sample
estimates ˆσ 2
m in Eqs. (3.49) and (3.50) may not even be consistent; see Bai, Russell,
and Tiao (2004). Further research is needed to make this approach valuable.
Example 3.6.
Consider the monthly volatility of the log returns of the S&P
500 index from January 1980 to December 1999. We calculate the volatility by
three methods. In the ﬁrst method, we use daily log returns and Eq. (3.49) (i.e.,
assuming that the daily log returns form a white noise series). The second method
also uses daily returns but assumes an MA(1) model [i.e., using Eq. (3.50)]. The
third method applies a GARCH(1,1) model to the monthly returns from January
--- page 188 ---

alternative approaches
161
Year
(a)
Volume
1980
1985
1990
1995
2000
0
20
40
60
80
Year
(b)
Volume
1980
1985
1990
1995
2000
0
20
40
60
80
Year
(c)
Volume
1980
1985
1990
1995
2000
0
20
40
60
80
Figure 3.12
Time plots of estimated monthly volatility for log returns of S&P 500 index from January
1980 to December 1999: (a) assumes that daily log returns form a white noise series, (b) assumes that
daily log returns follow an MA(1) model, and (c) uses monthly returns from January 1962 to December
1999 and a GARCH(1,1) model.
1962 to December 1999. We use a longer data span to obtain a more accurate
estimate of the monthly volatility. The GARCH(1,1) model used is
rm
t = 0.658 + at,
at = σtϵt,
σ 2
t = 3.349 + 0.086a2
t−1 + 0.735σ 2
t−1,
where ϵt is a standard Gaussian white noise series. Figure 3.12 shows the time plots
of the estimated monthly volatility. Clearly the estimated volatilities based on daily
returns are much higher than those based on monthly returns and a GARCH(1,1)
model. In particular, the estimated volatility for October 1987 was about 680 when
daily returns are used. The plots shown were truncated to have the same scale.
In Eq. (3.49), if we further assume that the sample mean ¯rt is zero, then we have
ˆσ 2
m ≈n
i=1 r2
t,i. In this case, the cumulative sum of squares of daily log returns
in a month is used as an estimate of monthly volatility. This concept has been
generalized to estimate daily volatility of an asset by using intradaily log returns.
--- page 189 ---

162
conditional heteroscedastic models
Let rt be the daily log return of an asset. Suppose that there are n equally spaced
intradaily log returns available such that rt = n
i=1 rt,i. The quantity
RVt =
n

i=1
r2
t,i,
is called the realized volatility of rt; see Andersen et al. (2001a,b). Mathematically,
realized volatility is a quadratic variation of rt, and it assumes that {rt,i}n
i=1 forms
an iid sequence with mean zero and ﬁnite variance. Limited experience indicates
that ln(RVt) often follows approximately a Gaussian ARIMA(0,1,q) model, which
can be used to produce forecasts. See demonstration in Section 1.1 for further
information.
Advantages of realized volatility include simplicity and making use of intradaily
returns. Intuitively, one would like to use as much information as possible by
choosing a large n. However, when the time interval between rt,i is small, the
returns are subject to the effects of market microstructure, for example, bid–ask
bounce, which often results in a biased estimate of the volatility. The problem of
choosing an optimal time interval for constructing realized volatility has attracted
much research lately. For heavily traded assets in the United States, a time interval
of 4–15 minutes is often used. Another problem of using realized volatility for
stock returns is that the overnight return, which is the return from the closing price
of day t −1 to the opening price of t, tends to be substantial. Ignoring overnight
returns can seriously underestimate the volatility. On the other hand, our limited
experience shows that overnight returns appear to be small for index returns or
foreign exchange returns.
In a series of recent articles, Barndorff-Nielsen and Shephard (2004) have used
high-frequency returns to study bi-power variations of an asset return and developed
some methods to detect jumps in volatility.
3.15.2
Use of Daily Open, High, Low, and Close Prices
For many assets, daily opening, high, low, and closing prices are available. Parkinson (1980), Garman and Klass (1980), Rogers and Satchell (1991), and Yang and
Zhang (2000) showed that one can use such information to improve volatility estimation. Figure 3.13 shows a time plot of price versus time for the tth trading day,
assuming that time is continuous. For an asset, deﬁne the following variables:
• Ct = closing price of the tth trading day.
• Ot = opening price of the tth trading day.
• f = fraction of the day (in interval [0,1]) that trading is closed.
• Ht = highest price of the tth trading period.
• Lt = lowest price of the tth trading period.
• Ft−1 = public information available at time t −1.
--- page 190 ---

alternative approaches
163
Time
Price
0.0
0.2
0.4
0.6
0.8
1.0
30
31
32
33
34
35
Trading closed
Trading open
C(t−1)
C(t)
O(t)
H(t)
L(t)
f
Figure 3.13
Time plot of price over time: scale for price is arbitrary.
The conventional variance (or volatility) is σ 2
t = E[(Ct −Ct−1)2|Ft−1]. Garman
and Klass (1980) considered several estimates of σ 2
t assuming that the price follows
a simple diffusion model without drift; see Chapter 6 for more information about
stochastic diffusion models. The estimators considered include:
• ˆσ 2
0,t = (Ct −Ct−1)2.
• ˆσ 2
1,t = (Ot −Ct−1)2
2f
+ (Ct −Ot)2
2(1 −f ) ,
0 < f < 1.
• ˆσ 2
2,t = (Ht −Lt)2
4 ln(2)
≈0.3607(Ht −Lt)2.
• ˆσ 2
3,t = 0.17(Ot −Ct−1)2
f
+ 0.83
(Ht −Lt)2
(1 −f )4 ln(2),
0 < f < 1.
• ˆσ 2
5,t = 0.5(Ht −Lt)2 −[2 ln(2) −1](Ct −Ot)2, which is ≈0.5(Ht −Lt)2 −
0.386(Ct −Ot)2.
• ˆσ 2
6,t = 0.12(Ot −Ct−1)2
f
+ 0.88
ˆσ 2
5,t
1 −f ,
0 < f < 1.
A more precise, but complicated, estimator ˆσ 2
4,t was also considered. However, it
is close to ˆσ 2
5,t. Deﬁning the efﬁciency factor of a volatility estimator as
Eff(ˆσ 2
i,t) =
Var(ˆσ 2
0,t)
Var(ˆσ 2
i,t) ,
--- page 191 ---

164
conditional heteroscedastic models
Garman and Klass (1980) found that Eff(ˆσ 2
i,t) is approximately 2, 5.2, 6.2, 7.4,
and 8.4 for i = 1, 2, 3, 5, and 6, respectively, for the simple diffusion model
entertained. Note that ˆσ 2
2,t was derived by Parkinson (1980) with f = 0.
Turn to log returns. Deﬁne the following:
• ot = ln(Ot) −ln(Ct−1), the normalized open.
• ut = ln(Ht) −ln(Ot), the normalized high.
• dt = ln(Lt) −ln(Ot), the normalized low.
• ct = ln(Ct) −ln(Ot), the normalized close.
Suppose that there are n days of data available and the volatility is constant over
the period. Yang and Zhang (2000) recommend the estimate
ˆσ 2
yz = ˆσ 2
o + k ˆσ 2
c + (1 −k)ˆσ 2
rs
as a robust estimator of the volatility, where
ˆσ 2
o =
1
n −1
n

t=1
(ot −¯o)2
with
¯o = 1
n
n

t=1
ot,
ˆσ 2
c =
1
n −1
n

t=1
(ct −¯c)2
with
¯c = 1
n
n

t=1
ct,
ˆσ 2
rs = 1
n
n

t=1
[ut(ut −ct) + dt(dt −ct)],
k =
0.34
1.34 + (n + 1)/(n −1).
The estimate ˆσ 2
rs was proposed by Rogers and Satchell (1991), and the quantity
k is chosen to minimize the variance of the estimator of ˆσ 2
yz, which is a linear
combination of three estimates.
The quantity Ht −Lt is called the range of the price in the tth day. This
estimator has led to the use of range-based volatility estimates; see, for instance,
Alizadeh, Brandt, and Diebold (2002). In practice, stock prices are only observed
at discrete time points. As such, the observed daily high is likely lower than Ht
and the observed daily low is likely higher than Lt. Consequently, the observed
daily price range tends to underestimate the actual range and, hence, may lead
to underestimation of volatility. This bias in volatility estimation depends on the
trading frequency and tick size of the stocks. For intensively traded stocks, the bias
should be negligible. For other stocks, further study is needed to better understand
the performance of range-based volatility estimation.
