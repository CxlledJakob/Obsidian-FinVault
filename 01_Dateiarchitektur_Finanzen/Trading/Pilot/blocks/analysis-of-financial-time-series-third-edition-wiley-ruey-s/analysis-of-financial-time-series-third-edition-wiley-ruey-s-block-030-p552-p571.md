# Analysis of Financial Time Series, Third Edition (Wiley -- Ruey S_ Tsay -- Wiley series in probability and statistics, 3rd ed_, -- John Wiley & Sons, -- isbn13 9780470414354 -- 9f99b80c7b2dedd477f463dc5323f3b6 -- An.pdf — pages 552–571

--- page 552 ---

garch models for bivariate returns
525
where the numbers in parentheses are standard errors. The constant correlation
coefﬁcient is 0.614 with standard error 0.020. Using the standardized residuals, we
obtain the Ljung–Box statistics Q2(4) = 16.77(0.21) and Q2(8) = 32.40(0.30),
where the p values shown in parentheses are obtained from chi-squared distributions with 13 and 29 degrees of freedom, respectively. Here the degrees of
freedom have been adjusted because the mean equations contain three lagged predictors. For the squared standardized residuals, we have Q∗
2(4) = 18.00(0.16) and
Q∗
2(8) = 39.09(0.10). Therefore, at the 5% signiﬁcance level, the standardized
residuals ˜at have no serial correlations or conditional heteroscedasticities. This
bivariate GARCH(1,1) model shows a feedback relationship between the volatilities
of the two monthly log returns.
10.4.2
Time-Varying Correlation Models
A major drawback of the constant-correlation volatility models is that the correlation coefﬁcient tends to change over time in a real application. Consider the
monthly log returns of IBM stock and the S&P 500 index used in Example 10.5.
It is hard to justify that the S&P 500 index return, which is a weighted average, can maintain a constant-correlation coefﬁcient with IBM return over the past
70 years. Figure 10.8 shows the sample correlation coefﬁcient between the two
monthly log return series using a moving window of 120 observations (i.e., 10
years). The correlation changes over time and appears to be decreasing in recent
years. The decreasing trend in correlation is not surprising because the ranking of
IBM market capitalization among large U.S. industrial companies has changed in
recent years. A Lagrange multiplier statistic was proposed recently by Tse (2000)
to test constant-correlation coefﬁcients in a multivariate GARCH model.
A simple way to relax the constant-correlation constraint within the GARCH
framework is to specify an exact equation for the conditional correlation coefﬁ-
cient. This can be done by two methods using the two reparameterizations of t
discussed in Section 10.3. First, we use the correlation coefﬁcient directly. Because
the correlation coefﬁcient between the returns of IBM stock and S&P 500 index is
positive and must be in the interval [0, 1], we employ the equation
ρ21,t =
exp(qt)
1 + exp(qt),
(10.25)
where
qt = ω0 + ω1ρ21,t−1 + ω2
a1,t−1a2,t−1
√σ11,t−1σ22,t−1
,
where σii,t−1 is the conditional variance of the shock ai,t−1. We refer to this equation
as a GARCH(1,1) model for the correlation coefﬁcient because it uses the lag-1
cross correlation and the lag-1 cross product of the two shocks. If ϖ1 = ϖ2 = 0,
then model (10.25) reduces to the case of constant correlation.
--- page 553 ---

526
multivariate volatility models and their applications
••••••••••••••••••••••••••••••••••
•••••••
•••••
••
••••••••••••••••••••••••
••••••••••••
••••
•••••••••••••
•••••
•
•
•••••••
••••••
••••••••••••••••••
••••••••
•••••
••••••
••••••••••••••••••••
•••••••••••
•••••••••
•••••••••••••••••
•
•
•••••••••••••••••••••••
•••••••••••••••••••••
•••••••••••••
••••••
•••••••••••••••••••
••••
••
••••••
•••••••
•
•••••••••••••••••••••••••••••••••••••••••••••••••••••••••
••••••••••••••
••••••••••
•
••••••••
•••••
••••••••
•••••••••
•••••••••••
•••••••
•
••••••••••••••
•••••••••
•
•••••••
••••••••••••••••••••
••••
•••
•••
••
••••••••
•
••••••••••••
••
Year
ρt
1940
1950
1960
1970
1980
1990
2000
0.4
0.5
0.6
0.7
0.8
Figure 10.8
Sample correlation coefﬁcient between monthly log returns of IBM stock and S&P 500
index. Correlation is computed by a moving window of 120 observations. Sample period is from January
1926 to December 1999.
In summary, a time-varying correlation bivariate GARCH(1,1) model consists
of two sets of equations. The ﬁrst set of equations consists of a bivariate
GARCH(1,1) model for the conditional variances, and the second set of equation
is a GARCH(1,1) model for the correlation in Eq. (10.25). In practice, a negative
sign can be added to Eq. (10.25) if the correlation coefﬁcient is negative.
In general, when the sign of correlation is unknown, we can use the Fisher
transformation for correlation
qt = ln
1 + ρ21,t
1 −ρ21,t

or
ρ21,t = exp(qt) −1
exp(qt) + 1
and employ a GARCH model for qt to model the time-varying correlation between
two returns.
Example 10.5 (Continued).
Augmenting Eq. (10.25) to the GARCH(1,1)
model in Eq. (10.24) for the monthly log returns of IBM stock and the S&P
500 index and performing a joint estimation, we obtain the following model for
the two series:
r1t = 1.318 + 0.076r1,t−1 −0.068r2,t−2 + a1t,
r2t = 0.673 + a2t,
--- page 554 ---

garch models for bivariate returns
527
where standard errors of the three parameters in the ﬁrst equation are 0.215, 0.026,
and 0.034, respectively, and standard error of the parameter in the second equation
is 0.151. The volatility equations are

 σ11,t
σ22,t

=


2.80
(0.58)
1.71
(0.40)

+


0.084
(0.013)
0.037
0.054
(0.009)
(0.010)



 a2
1,t−1
a2
2,t−1

+


0.864
−0.020
(0.021)
(0.009)
−0.058
0.914
(0.014)
(0.013)



 σ11,t−1
σ22,t−1

,
(10.26)
where, as before, standard errors are in parentheses. The conditional correlation
equation is
ρt =
exp(qt)
1 + exp(qt),
qt = −2.024 + 3.983ρt−1 + 0.088
a1,t−1a2,t−1
√σ11,t−1σ22,t−1
,
(10.27)
where standard errors of the estimates are 0.050, 0.090, and 0.019, respectively.
The parameters of the prior correlation equation are highly signiﬁcant. Applying the Ljung–Box statistics to the standardized residuals ˜at, we have Q2(4) =
20.57(0.11) and Q2(8) = 36.08(0.21). For the squared standardized residuals, we
have Q∗
2(4) = 16.69(0.27) and Q∗
2(8) = 36.71(0.19). Therefore, the standardized
residuals of the model have no signiﬁcant serial correlations or conditional heteroscedasticities.
It is interesting to compare this time-varying correlation GARCH(1,1) model
with the constant-correlation GARCH(1,1) model in Eq. (10.24). First, the mean
and volatility equations of the two models are close. Second, Figure 10.9 shows
the ﬁtted conditional correlation coefﬁcient between the monthly log returns of
IBM stock and the S&P 500 index based on model (10.27). The plot shows that
the correlation coefﬁcient ﬂuctuated over time and became smaller in recent years.
This latter characteristic is in agreement with that of Figure 10.8. Third, the average of the ﬁtted correlation coefﬁcients is 0.612, which is essentially the estimate
0.614 of the constant-correlation model in Eq. (10.24). Fourth, using the sample
variances of rit as the starting values for the conditional variances and the observations from t = 4 to t = 888, the maximized log-likelihood function is −3691.21
for the constant-correlation GARCH(1,1) model and −3679.64 for the time-varying
correlation GARCH(1,1) model. Thus, the time-varying correlation model shows
some signiﬁcant improvement over the constant-correlation model. Finally, consider the 1-step-ahead volatility forecasts of the two models at the forecast origin
h = 888. For the constant-correlation model in Eq. (10.24), we have a1,888 = 3.075,
--- page 555 ---

528
multivariate volatility models and their applications
Year
ρt
1940
1960
1980
2000
0.4
0.5
0.6
0.7
0.8
Figure 10.9
Fitted conditional correlation coefﬁcient between monthly log returns of IBM stock and
S&P 500 index using time-varying correlation GARCH(1,1) model of Example 10.5. Horizontal line
denotes average of 0.612 of correlation coefﬁcients.
a2,888 = 4.931, σ11,888 = 77.91, and σ22,888 = 21.19. Therefore, the 1-step-ahead
forecast for the conditional covariance matrix is
888(1) =

 71.09
21.83
21.83
17.79

,
where the covariance is obtained by using the constant-correlation coefﬁcient 0.614.
For the time-varying correlation model in Eqs. (10.26) and (10.27), we have
a1,888 = 3.287, a2,888 = 4.950, σ11,888 = 83.35, σ22,888 = 28.56, and ρ888 = 0.546.
The 1-step-ahead forecast for the covariance matrix is
888(1) =

 75.15
23.48
23.48
24.70

,
where the forecast of the correlation coefﬁcient is 0.545.
In the second method, we use the Cholesky decomposition of t to model
time-varying correlations. For the bivariate case, the parameter vector is t =
(g11,t, g22,t, q21,t)′; see Eq. (10.18). A simple GARCH(1,1) type model for at is
g11,t = α10 + α11b2
1,t−1 + β11g11,t−1,
q21,t = γ0 + γ1q21,t−1 + γ2a2,t−1,
(10.28)
g22,t = α20 + α21b2
1,t−1 + α22b2
2,t−1 + β21g11,t−1 + β22g22,t−1,
--- page 556 ---

garch models for bivariate returns
529
where
b1t = a1t
and
b2t = a2t −q21,ta1t.
Thus,
b1t
assumes
a
univariate
GARCH(1,1) model, b2t uses a bivariate GARCH(1,1) model, and q21,t is
autocorrelated and uses a2,t−1
as an additional explanatory variable. The
probability density function relevant to maximum-likelihood estimation is given
in Eq. (10.20) with k = 2.
Example 10.5 (Continued).
Again we use the monthly log returns of IBM
stock and the S&P 500 index to demonstrate the volatility model in Eq. (10.28).
Using the same speciﬁcation as before, we obtain the ﬁtted mean equations as
r1t = 1.364 + 0.075r1,t−1 −0.058r2,t−2 + a1t,
r2t = 0.643 + a2t,
where standard errors of the parameters in the ﬁrst equation are 0.219, 0.027, and
0.032, respectively, and the standard error of the parameter in the second equation
is 0.154. These two mean equations are close to what we obtained before. The
ﬁtted volatility model is
g11,t = 3.714 + 0.113b2
1,t−1 + 0.804g11,t−1,
q21,t = 0.0029 + 0.9915q21,t−1 −0.0041a2,t−1,
(10.29)
g22,t = 1.023 + 0.021b2
1,t−1 + 0.052b2
2,t−1 −0.040g11,t−1 + 0.937g22,t−1,
where b1t = a1t, and b2t = a2t −q21,tb1t. Standard errors of the parameters in the
equation of g11,t are 1.033, 0.022, and 0.037, respectively; those of the parameters
in the equation of q21,t are 0.001, 0.002, and 0.0004; and those of the parameters in
the equation of g22,t are 0.344, 0.007, 0.013, and 0.015, respectively. All estimates
are statistically signiﬁcant at the 1% level.
The conditional covariance matrix t can be obtained from model (10.29)
by using the Cholesky decomposition in Eq. (10.12). For the bivariate case, the
relationship is given speciﬁcally in Eq. (10.13). Consequently, we obtain the timevarying correlation coefﬁcient as
ρt =
σ21,t
√σ11,tσ22,t
=
q21,t√g11,t

g22,t + q2
21,tg11,t
.
(10.30)
Using the ﬁtted values of σ11,t and σ22,t, we can compute the standardized residuals
to perform model checking. The Ljung–Box statistics for the standardized residuals of model (10.29) give Q2(4) = 19.77(0.14) and Q2(8) = 34.22(0.27). For
the squared standardized residuals, we have Q∗
2(4) = 15.34(0.36) and Q∗
2(8) =
31.87(0.37). Thus, the ﬁtted model is adequate in describing the conditional mean
and volatility. The model shows a strong dynamic dependence in the correlation;
see the coefﬁcient 0.9915 in Eq. (10.29).
--- page 557 ---

530
multivariate volatility models and their applications
Year
ρt
1940
1960
1980
2000
0.2
0.4
0.6
0.8
Figure 10.10
Fitted conditional correlation coefﬁcient between monthly log returns of IBM stock and
S&P 500 index using time-varying correlation GARCH(1,1) model of Example 10.5 with Cholesky
decomposition. Horizontal line denotes average of 0.612 of the estimated coefﬁcients.
Figure 10.10 shows the ﬁtted time-varying correlation coefﬁcient in Eq. (10.30).
It shows a smoother correlation pattern than that of Figure 10.9 and conﬁrms
the decreasing trend of the correlation coefﬁcient. In particular, the ﬁtted correlation coefﬁcients in recent years are smaller than those of the other models. The
two time-varying correlation models for the monthly log returns of IBM stock
and the S&P 500 index have comparable maximized-likelihood functions of about
−3672, indicating the ﬁts are similar. However, the approach based on the Cholesky
decomposition may have some advantages. First, it does not require any parameter
constraint in estimation to ensure the positive deﬁniteness of t. If one also uses
log transformation for gii,t, then no constraints are needed for the entire volatility
model. Second, the log-likelihood function becomes simple under the transformation. Third, the time-varying parameters qij,t and gii,t have nice interpretations.
However, the transformation makes inference a bit more complicated because the
ﬁtted model may depend on the ordering of elements in at; recall that a1t is not
transformed. In theory, the ordering of elements in at should have no impact on
volatility.
Finally, the 1-step-ahead forecast of the conditional covariance matrix at the
forecast origin t = 888 for the new time-varying correlation model is
888(1) =

 73.45
7.34
7.34
17.87

.
--- page 558 ---

garch models for bivariate returns
531
The correlation coefﬁcient of the prior forecast is 0.203, which is substantially
smaller than those of the previous two models. However, forecasts of the conditional variances are similar as before.
10.4.3
Dynamic Correlation Models
Using the parameterization in Eq. (10.7), several authors have proposed parsimonious models for ρt to describe the time-varying correlations. We refer to those
models as the dynamic conditional correlation (DCC) models.
For k-dimensional returns, Tse and Tsui (2002) assume that the conditional
correlation matrix ρt follows the model
ρt = (1 −θ1 −θ2)ρ + θ1ρt−1 + θ2ψt−1,
where θ1 and θ2 are scalar parameters, ρ is a k × k positive-deﬁnite matrix with unit
diagonal elements, and ψt−1 is the k × k sample correlation matrix using shocks
from t −m, . . . , t −1 for a prespeciﬁed m. Typically, one assumes that 0 ≤θi < 1
and θ1 + θ2 < 1 so that the resulting correlation matrix ρt is positive deﬁnite for
all t. For a given ρ, the model is parsimonious. In applications, the choice of ρ
and m deserves a careful investigation. One possibility is to let ρ be the sample
correlation matrix of the returns. The correlation equation then only employs two
parameters.
Engle (2002) proposes the model
ρt = J tQtJ t,
where Qt = (qij,t)k×k is a positive-deﬁnite matrix, J t = diag{q−1/2
11,t , . . . , q−1/2
kk,t },
and Qt satisﬁes
Qt = (1 −θ1 −θ2) ¯Q + θ1ϵt−1ϵ′
t−1 + θ2Qt−1,
where ϵt is the standardized innovation vector with elements ϵit = ait/√σii,t, ¯Q
is the unconditional covariance matrix of ϵt, and θ1 and θ2 are nonnegative scalar
parameters satisfying 0 < θ1 + θ2 < 1. The J t matrix is a normalization matrix to
guarantee that Rt is a correlation matrix.
An obvious drawback of the prior two models is that θ1 and θ2 are scalar so
that all the conditional correlations have the same dynamics. This might be hard
to justify in real applications, especially when the dimension k is large.
Tsay (2006) extends the previous DCC models in two ways. First, the standardized innovations are assumed to follow a multivariate Student-t distribution of Eq.
(10.42). Second, the marginal volatility models have leverage effects. Speciﬁcally,
the volatility equation for rt is
D2
t = 0 + 1D2
t−1 + 2A2
t−1 + 3L2
t−1,
(10.31)
--- page 559 ---

532
multivariate volatility models and their applications
where Dt is the diagonal matrix of volatilities as deﬁned in Eq. (10.7), Aj =
diag{a1j, . . . , akj}, i = diag{ℓ1i, . . . , ℓki} are k × k diagonal matrices of parameters and Lt−1 = diag{L1,t−1, . . . , Lk,t−1} is also a k × k diagonal matrix with
diagonal elements
Li,t−1 =

ai,t−1
if ai,t−1 < 0,
0
otherwise.
In
Eq.
(10.31),
the
parameters
ℓij
satisfy
0 ≤3
j=1 ℓij < 1,
ℓi0 > 0
for
i = 1, . . . , k, and ℓji ≥0 for all positive i and j. The constraint ensures that the
volatilities exist. Of course, if 3 = 0, then there is no leverage effect.
The correlation equation is
ρt = (1 −θ1 −θ2)ˆρ + θ1ψt−1 + θ2ρt−1,
(10.32)
where ˆρ is the sample correlation matrix of the returns and 0 ≤θ1 + θ2 < 1 with
θi ≥0 for i = 1, 2.
Example 10.6.
To illustrate the DCC model, we consider the daily exchange
rates between U.S. dollar versus European euro and Japanese yen and the stock
prices of IBM and Dell from January 1999 to December 2004. The exchange rates
are the noon spot rate obtained from the Federal Reserve Bank of St. Louis and
the stock returns are from the Center for Research in Security Prices (CRSP). We
compute the simple returns of the exchange rates and remove returns for those
days when one of the markets was not open. This results in a four-dimensional
return series with 1496 observations. The return vector is rt = (r1t, r2t, r3t, r4t)′
with r1t and r2t being the returns of euro and yen exchange rate, respectively, and
r3t and r4t are the returns of IBM and Dell stock, respectively. All returns are
in percentages. Figure 10.11 shows the time plot of the return series. From the
plot, equity returns have higher variability than the exchange rate returns, and the
variability of equity returns appears to be decreasing in latter years. Table 10.1
provides some descriptive statistics of the return series. As expected, the means of
the returns are essentially zero and all four series have heavy tails with positive
excess kurtosis.
The equity returns have some serial correlations, but the magnitude is small. If
multivariate Ljung–Box statistics are used, we have Q(3) = 59.12 with a p value
of 0.13 and Q(5) = 106.44 with a p value of 0.03. For simplicity, we use the
sample mean as the mean equation and apply the proposed multivariate volatility
model to the mean-corrected data. In estimation, we start with a general model, but
add some equality constraints as some estimates appear to be close to each other.
The results are given in Table 10.2 along with the value of likelihood function
evaluated at the estimates.
For each estimated multivariate volatility model in Table 10.2, we compute the
standardized residuals as
ˆϵt = 
−1/2
t
at,
--- page 560 ---

garch models for bivariate returns
533
(a)
USEU
1999
2000
2001
2002
2003
2004
2005
−2 −1
1
0
2
USJP
−3 −2 −1
1 2
0
3
IBM
−15
−5 0
5 10
Dell
−20−10 0 10 20
(b)
1999
2000
2001
2002
2003
2004
2005
(c)
1999
2000
2001
2002
2003
2004
2005
(d)
1999
2000
2001
2002
2003
2004
2005
Figure 10.11
Time plots of daily simple return series from January 1999 to December 2004:
(a) dollar–euro exchange rate, (b) dollar–yen exchange rate, (c) IBM stock, and (d) Dell stock.
TABLE 10.1
Descriptive Statistics of Daily Returns of Example 10.6.a
Asset
USEU
JPUS
IBM
DELL
Mean
0.0091
−0.0059
0.0066
0.0028
Standard error
0.6469
0.6626
5.4280
10.1954
Skewness
0.0342
−0.1674
−0.0530
−0.0383
Excess kurtosis
2.7090
2.0332
6.2164
3.3054
Box–Ljung Q(12)
12.5
6.4
24.1
24.1
aThe returns are in percentages, and the sample period is from January 1999 to December 2004 for
1496 observations.
where 
1/2
t
is the symmetric square root matrix of the estimated volatility matrix
t. We apply the multivariate Ljung–Box statistics to the standardized residuals ˆϵt
and its squared process ˆϵ2
t of a ﬁtted model to check model adequacy. For the full
model in Table 10.2(a), we have Q(10) = 167.79(0.32) and Q(10) = 110.19(1.00)
for ˆϵt and ˆϵ2
t , respectively, where the number in parentheses denotes p value.
Clearly, the model adequately describes the ﬁrst two moments of the return series.
For the model in Table 10.2(b), we have Q(10) = 168.59(0.31) and Q(10) =
109.93(1.00). For the ﬁnal restricted model in Table 10.2(c), we obtain Q(10) =
--- page 561 ---

534
multivariate volatility models and their applications
TABLE 10.2
Estimation Results of Multivariate Volatility Models for Example 10.6a
(a) Full Model Estimation with Lmax = −9175.80
0
1
2
(v, θ1, θ2)′
0.0041(0.0033)
0.9701(0.0114)
0.0214(0.0075)
7.8729(0.4693)
0.0088(0.0038)
0.9515(0.0126)
0.0281(0.0084)
0.9808(0.0029)
0.0071(0.0053)
0.9636(0.0092)
0.0326(0.0087)
0.0137(0.0025)
0.0150(0.0136)
0.9531(0.0155)
0.0461(0.0164)
(b) Restricted Model with Lmax = −9176.62
0
1 = λ × I
2
(v, θ1, θ2)′
0.0066(0.0028)
0.9606(0.0068)
0.0255(0.0068)
7.8772(0.7144)
0.0066(0.0023)
0.0240(0.0059)
0.9809(0.0042)
0.0080(0.0052)
0.0355(0.0068)
0.0137(0.0025)
0.0108(0.0086)
0.0385(0.0073)
(c) Final Restricted Model with Lmax = −9177.44
0(λ1, λ1, λ3, λ4)
1 = λ × I
2(b1, b1, b2, b2)
(v, θ1, θ2)′
0.0067(0.0021)
0.9603(0.0063)
0.0248(0.0048)
7.9180(0.6952)
0.0067(0.0021)
0.0248(0.0048)
0.9809(0.0042)
0.0061(0.0044)
0.0372(0.0061)
0.0137(0.0028)
0.0148(0.0084)
0.0372(0.0061)
(d) Model with Leverage Effects, Lmax = −9169.04
0(λ1, λ2, λ3, λ4)
1 = λ × I
2(b1, b2, b3, b4)
(v, θ1, θ2)′
0.0064(0.0027)
0.9600(0.0065)
0.0254(0.0063)
8.4527(0.7556)
0.0066(0.0023)
0.0236(0.0054)
0.9810(0.0044)
0.0128(0.0055)
0.0241(0.0056)
0.0132(0.0027)
0.0210(0.0099)
0.0286(0.0062)
aLmax denotes the value of likelihood function evaluated at the estimates, v is the degrees of freedom of
the multivariate Student-t distribution, and the numbers in parentheses are asymptotic standard errors.
168.50(0.31) and Q(10) = 111.75(1.00). Again, the restricted models are capable
of describing the mean and volatility of the return series.
From Table 10.2, we make the following observations. First, using the likelihood
ratio test, we cannot reject the ﬁnal restricted model compared with the full model.
This results in a very parsimonious model consisting of only 9 parameters for the
time-varying correlations of the four-dimensional return series. Second, for the two
stock return series, the constant terms in 0 are not signiﬁcantly different from zero,
and the sum of GARCH parameters is 0.0372 + 0.9603 = 0.9975, which is very
close to unity. Consequently, the volatility series of the two equity returns exhibit
IGARCH behavior. On the other hand, the volatility series of the two exchange rate
returns appear to have a nonzero constant term and high persistence in GARCH
--- page 562 ---

garch models for bivariate returns
535
(a)
USEU
1999
2000
2001
2002
2003
2004
2005
0.0 0.4 0.8 1.2
JPUS
0.0 0.4 0.8 1.2
IBM
0
10
5
15 20
Dell
0 10 20 30 40
(b)
1999
2000
2001
2002
2003
2004
2005
(c)
1999
2000
2001
2002
2003
2004
2005
(d)
Year
1999
2000
2001
2002
2003
2004
2005
Figure 10.12
Time plots of estimated volatility series of four asset returns. Solid line is from proposed
model and dashed line is from a rolling estimation with window size 69: (a) dollar–euro exchange rate,
(b) dollar–yen exchange rate, (c) IBM stock, and (d) Dell stock.
parameters. Third, to better understand the efﬁcacy of the proposed model, we
compare the results of the ﬁnal restricted model with those of rolling estimates.
The rolling estimates of covariance matrix are obtained using a moving window of
size 69, which is the approximate number of trading days in a quarter. Figure 10.12
shows the time plot of estimated volatility. The solid line is the volatility obtained
by the proposed model and the dashed line is for volatility of the rolling estimation.
The overall pattern seems similar, but, as expected, the rolling estimates respond
more slowly than the proposed model to large innovations. This is shown by the
faster rise and decay of the volatility obtained by the proposed model. Figure 10.13
shows the time-varying correlations of the four asset returns. The solid line denotes
correlations obtained by the ﬁnal restricted model of Table 10.2, whereas the dashed
line is for rolling estimation. The correlations of the proposed model seem to be
smoother.
Table 10.2(d) gives the results of a ﬁtted integrated GARCH-type model with
leverage effects. The leverage effects are statistically signiﬁcant for equity returns
only and are in the form of an IGARCH model. Speciﬁcally, the 3 matrix of the
--- page 563 ---

536
multivariate volatility models and their applications
Correlations
1999
2000
2001
2002
2003
2004
2005
−1.0 −0.5 0.0
0.5
1.0
(a) USEU vs JPUS
(b) IBM vs USEU
(c) IBM vs JPUS
(d) Dell vs USEU
(e)
Year
(f) Dell vs IBM
Correlations
1999
2000
2001
2002
2003
2004
2005
−1.0 −0.5 0.0
0.5
1.0
Correlations
1999
2000
2001
2002
2003
2004
2005
−1.0 −0.5 0.0
0.5
1.0
Correlations
1999
2000
2001
2002
2003
2004
2005
−1.0 −0.5 0.0
0.5
1.0
Correlations
1999
2000
2001
2002
2003
2004
2005
−1.0 −0.5 0.0
0.5
1.0
Correlations
1999
2000
2001
2002
2003
2004
2005
−1.0 −0.5 0.0
0.5
1.0
Figure 10.13
Time plots of time-varying correlations between percentage simple returns of four assets
from January 1999 to December 2004. Solid line is from the proposed model, whereas dashed line is
from a rolling estimation with window size 69.
--- page 564 ---

higher dimensional volatility models
537
correlation equation in Eq. (10.31) is
3 = diag {0, 0, (1 −0.96 −0.0241), (1 −0.96 −0.0286)}
= diag{0, 0, 0.0159, 0.0114}.
Although the magnitudes of the leverage parameters are small, they are statistically
signiﬁcant. This is shown by the likelihood ratio test. Speciﬁcally, comparing the
ﬁtted models in Table 10.2(b) and (d), the likelihood ratio statistic is 15.16, which
has a p value of 0.0005 based on the chi-squared distribution with 2 degrees of
freedom.
10.5
HIGHER DIMENSIONAL VOLATILITY MODELS
In this section, we make use of the sequential nature of Cholesky decomposition to
suggest a strategy for building a high-dimensional volatility model. Again write the
vector return series as rt = µt + at. The mean equations for rt can be speciﬁed
by using the methods of Chapter 8. A simple vector AR model is often sufﬁcient.
Here we focus on building a volatility model using the shock process at.
Based on the discussion of Cholesky decomposition in Section 10.3, the orthogonal transformation from ait to bit only involves bjt for j < i. In addition, the
time-varying volatility models built in Section 10.4 appear to be nested in the sense
that the model for gii,t depends only on quantities related to bjt for j < i. Consequently, we consider the following sequential procedure to build a multivariate
volatility model:
1. Select a market index or a stock return that is of major interest. Build a
univariate volatility model for the selected return series.
2. Augment a second return series to the system, perform the orthogonal transformation on the shock process of this new return series, and build a bivariate
volatility model for the system. The parameter estimates of the univariate
model in step 1 can be used as the starting values in bivariate estimation.
3. Augment a third return series to the system, perform the orthogonal transformation on this newly added shock process, and build a three-dimensional
volatility model. Again parameter estimates of the bivariate model can be
used as the starting values in the three-dimensional estimation.
4. Continue the augmentation until a joint volatility model is built for all the
return series of interest.
Finally, model checking should be performed in each step to ensure the adequacy
of the ﬁtted model. Experience shows that this sequential procedure can simplify substantially the complexity involved in building a high-dimensional volatility
model. In particular, it can markedly reduce the computing time in estimation.
--- page 565 ---

538
multivariate volatility models and their applications
Year
(a)
Log returns
1992
1994
1996
1998
2000
−6 −4 −2 0
2
4
Log returns
−20
−10
0
10
Log returns
−15−10 −5
0
5
10
Year
(b)
1992
1994
1996
1998
2000
Year
(c)
1992
1994
1996
1998
2000
Figure 10.14
Time plots of daily log returns in percentages of (a) S&P 500 index and stocks of (b)
Cisco Systems and (c) Intel Corporation from January 2, 1991, to December 31, 1999.
Example 10.7.
We demonstrate the proposed sequential procedure by building
a volatility model for the daily log returns of the S&P 500 index and the stocks
of Cisco Systems and Intel Corporation. The data span is from January 2, 1991,
to December 31, 1999, with 2275 observations. The log returns are in percentages
and shown in Figure 10.14. Components of the return series are ordered as rt =
(SP5t, CSCOt, INTCt)′. The sample means, standard errors, and correlation matrix
of the data are
µ =


0.066
0.257
0.156

,


ˆσ1
ˆσ2
ˆσ3

=


0.875
2.853
2.464

,
ρ =


1.00
0.52
0.50
0.52
1.00
0.47
0.50
0.47
1.00

.
Using the Ljung–Box statistics to detect any serial dependence in the return
series, we obtain Q3(1) = 26.20, Q3(4) = 79.73, and Q3(8) = 123.68. These test
statistics are highly signiﬁcant with p values close to zero as compared with
--- page 566 ---

higher dimensional volatility models
539
TABLE 10.3
Sample Cross-Correlation Matrices of Daily Log Returns of S&P 500
Index and Stocks of Cisco Systems and Intel Corporation from January 2, 1991, to
December 31, 1999
Lag
1
2
3
4
5
6
·
·
·
·
·
·
–
·
·
·
·
·
·
–
·
·
·
·
–
·
·
·
·
·
·
·
·
·
·
·
·
·
·
·
·
·
–
·
·
–
·
·
–
·
·
·
·
·
·
–
·
·
·
·
chi-squared distributions with degrees of freedom 9, 36, and 72, respectively.
There is indeed some serial dependence in the data. Table 10.3 gives the ﬁrst
ﬁve lags of sample cross-correlation matrices shown in the simpliﬁed notation of
Chapter 8. An examination of the table shows that (a) the daily log returns of
the S&P 500 index does not depend on the past returns of Cisco or Intel, (b) the
log return of Cisco stock has some serial correlations and depends on the past
returns of the S&P 500 index (see lags 2 and 5), and (c) the log return of Intel
stock depends on the past returns of the S&P 500 index (see lags 1 and 5). These
observations are similar to those between the returns of IBM stock and the S&P
500 index analyzed in Chapter 8. They suggest that returns of individual largecap companies tend to be affected by the past behavior of the market. However,
the market return is not signiﬁcantly affected by the past returns of individual
companies.
Turning to volatility modeling and following the suggested procedure, we start
with the log returns of the S&P 500 index and obtain the model
r1t = 0.078 + 0.042r1,t−1 −0.062r1,t−3 −0.048r1,t−4 −0.052r1,t−5 + a1t,
σ11,t = 0.013 + 0.092a2
1,t−1 + 0.894σ11,t−1,
(10.33)
where standard errors of the parameters in the mean equation are 0.016, 0.023,
0.020, 0.022, and 0.020, respectively, and those of the parameters in the volatility
equation are 0.002, 0.006, and 0.007, respectively. Univariate Ljung–Box statistics
of the standardized residuals and their squared series fail to detect any remaining
serial correlation or conditional heteroscedasticity in the data. Indeed, we have
Q(10) = 7.38(0.69) for the standardized residuals and Q(10) = 3.14(0.98) for the
squared series.
Augmenting the daily log returns of Cisco stock to the system, we build a
bivariate model with mean equations given by
r1t = 0.065 −0.046r1,t−3 + a1t,
r2t = 0.325 + 0.195r1,t−2 −0.091r2,t−2 + a2t,
(10.34)
--- page 567 ---

540
multivariate volatility models and their applications
where all of the estimates are statistically signiﬁcant at the 1% level. Using the
notation of Cholesky decomposition, we obtain the volatility equations as
g11,t = 0.006 + 0.051b2
1,t−1 + 0.943g11,t−1,
q21,t = 0.331 + 0.790q21,t−1 −0.041a2,t−1,
(10.35)
g22,t = 0.177 + 0.082b2
2,t−1 + 0.890g22,t−1,
where b1t = a1t, b2t = a2t −q21,tb1t, standard errors of the parameters in the
equation of g11,t are 0.001, 0.005, and 0.006, those of the parameters in the
equation of q21,t are 0.156, 0.099, and 0.011, and those of the parameters in
the equation of g22,t are 0.029, 0.008, and 0.011, respectively. The bivariate
Ljung–Box statistics of the standardized residuals fail to detect any remaining
serial dependence or conditional heteroscedasticity. The bivariate model is
adequate. Comparing with Eq. (10.33), we see that the difference between the
marginal and univariate models of r1t is small.
The next and ﬁnal step is to augment the daily log returns of Intel stock to the
system. The mean equations become
r1t = 0.065 −0.043r1,t−3 + a1t,
r2t = 0.326 + 0.201r1,t−2 −0.089r2,t−1 + a2t,
(10.36)
r3t = 0.192 −0.264r1,t−1 + 0.059r3,t−1 + a3t,
where standard errors of the parameters in the ﬁrst equation are 0.016 and 0.017,
those of the parameters in the second equation are 0.052, 0.059, and 0.021, and
those of the parameters in the third equation are 0.050, 0.057, and 0.022, respectively. All estimates are statistically signiﬁcant at about the 1% level. As expected,
the mean equations for r1t and r2t are essentially the same as those in the bivariate
case.
The three-dimensional time-varying volatility model becomes a bit more complicated, but it remains manageable as
g11,t = 0.006 + 0.050b2
1,t−1 + 0.943g11,t−1,
q21,t = 0.277 + 0.824q21,t−1 −0.035a2,t−1,
g22,t = 0.178 + 0.082b2
2,t−1 + 0.889g22,t−1,
q31,t = 0.039 + 0.973q31,t−1 + 0.010a3,t−1,
(10.37)
q32,t = 0.006 + 0.981q32,t−1 + 0.004a2,t−1,
g33,t = 1.188 + 0.053b2
3,t−1 + 0.687g33,t−1 −0.019g22,t−1,
where b1t = a1t, b2t = a2t −q21,tb1t, b3t = a3t −q31,tb1t −q32,tb2t, and standard
errors of the parameters are given in Table 10.4. Except for the constant
term of the q32,t equation, all estimates are signiﬁcant at the 5% level. Let
--- page 568 ---

higher dimensional volatility models
541
TABLE 10.4
Standard Errors of Parameter Estimates of Three-Dimensional
Volatility Model for Daily Log Returns in Percentages of S&P 500 Index and Stocks
of Cisco Systems and Intel Corporation from January 2, 1991, to December 31, 1999a
Equation
Standard Error
Equation
Standard Error
g11,t
0.001
0.005
0.006
q21,t
0.135
0.086
0.010
g22,t
0.029
0.009
0.011
q31,t
0.017
0.012
0.004
g33,t
0.407
0.015
0.100
0.008
q32,t
0.004
0.013
0.001
aThe ordering of the parameter is the same as appears in Eq. (10.37).
˜at = (a1t/ˆσ1t, a2t/ˆσ2t, a3t/ˆσ3t)′
be
the
standardized
residual
series,
where
ˆσit =

ˆσii,t is the ﬁtted conditional standard error of the ith return. The
Ljung–Box statistics of ˜at give Q3(4) = 34.48(0.31) and Q3(8) = 60.42(0.70),
where the degrees of freedom of the chi-squared distributions are 31 and
67, respectively, after adjusting for the number of parameters used in the
mean equations. For the squared standardized residual series ˜a2
t , we have
Q∗
3(4) = 28.71(0.58) and Q∗
3(8) = 52.00(0.91). Therefore, the ﬁtted model
appears to be adequate in modeling the conditional means and volatilities.
The three-dimensional volatility model in Eq. (10.37) shows some interesting features. First, it is essentially a time-varying correlation GARCH(1,1) model
because only lag-1 variables are used in the equations. Second, the volatility of
the daily log returns of the S&P 500 index does not depend on the past volatilities of Cisco or Intel stock returns. Third, by taking the inverse transformation
of the Cholesky decomposition, the volatilities of daily log returns of Cisco and
Intel stocks depend on the past volatility of the market return; see the relationships
between elements of t, Lt, and Gt given in Section 10.3. Fourth, the correlation
quantities qij,t have high persistence with large AR(1) coefﬁcients.
Figure 10.15 shows the ﬁtted volatility processes of the model (i.e., ˆσii,t) for
the data. The volatility of the index return is much smaller than those of the two
individual stock returns. The plots also show that the volatility of the index return
has increased in recent years, but this is not the case for the return of Cisco Systems.
Figure 10.16 shows the time-varying correlation coefﬁcients between the three
return series. Of particular interest is to compare Figures 10.15 and 10.16. They
show that the correlation coefﬁcient between two return series increases when the
returns are volatile. This is in agreement with the empirical study of relationships
between international stock market indexes for which the correlation between two
markets tends to increase during a ﬁnancial crisis.
The volatility model in Eq. (10.37) consists of two sets of equations. The ﬁrst
set of equations describes the time evolution of conditional variances (i.e., gii,t),
and the second set of equations deals with correlation coefﬁcients (i.e., qij,t with
i > j). For this particular data set, an AR(1) model might be sufﬁcient for the
correlation equations. Similarly, a simple AR model might also be sufﬁcient for
the conditional variances. Deﬁne vt = (v11,t, v22,t, v33,t)′, where vii,t = ln(gii,t),
and qt = (q21,t, q31,t, q32,t)′. The previous discussion suggests that we can use the
--- page 569 ---

542
multivariate volatility models and their applications
Year
Volatilities
1992
1994
1996
1998
2000
1
2
3
4
5
(a)
Volatilities
10 20 30 40 50
Volatilities
4 6 8 101214
Year
1992
1994
1996
1998
2000
(b)
Year
1992
1994
1996
1998
2000
(c)
Figure 10.15
Time plots of ﬁtted volatilities for daily log returns, in percentages, of (a) S&P 500
index and stocks of (b) Cisco Systems and (c) Intel Corporation from January 2, 1991, to December
31, 1999.
simple lag-1 models
vt = c1 + β1vt−1,
qt = c2 + β2qt−1
as exact functions to model the volatility of asset returns, where ci are constant
vectors and βi are 3 × 3 real-valued matrices. If a noise term is also included in
the above equations, then the models become
vt = c1 + β1vt−1 + e1t,
qt = c2 + β2qt−1 + e2t,
where eit are random shocks with mean zero and a positive-deﬁnite covariance
matrix, and we have a simple multivariate stochastic volatility model. In a recent
manuscript, Chib, Nardari, and Shephard (1999) use Markov chain Monte Carlo
(MCMC) methods to study high-dimensional stochastic volatility models. The
model considered there allows for time-varying correlations, but in a relatively
restrictive manner. Additional references of multivariate volatility model include
--- page 570 ---

factor–volatility models
543
Year
Correlation
1992
1994
1996
1998
2000
0.2
0.4
0.6
0.8
(a) S&P 500 Index and Cisco
Correlation
0.2 0.3 0.4 0.5 0.6 0.7 0.8
Correlation
0.3 0.4 0.5 0.6 0.7 0.8
Year
1992
1994
1996
1998
2000
(b) S&P 500 Index and Intel
Year
1992
1994
1996
1998
2000
(c) Cisco and Intel
Figure 10.16
Time plots of ﬁtted time-varying correlation coefﬁcients between daily log returns of
S&P 500 index and stocks of Cisco Systems and Intel Corporation from January 2, 1991, to December
31, 1999.
Harvey, Ruiz, and Shephard (1994). We discuss MCMC methods in volatility modeling in Chapter 12.
10.6
FACTOR–VOLATILITY MODELS
Another approach to simplifying the dynamic structure of a multivariate volatility
process is to use factor models. In practice, the “common factors” can be determined
a priori by substantive matter or empirical methods. As an illustration, we use the
factor analysis of Chapter 8 to discuss factor–volatility models. Because volatility
models are concerned with the evolution over time of the conditional covariance
matrix of at, where at = rt −µt, a simple way to identify the “common factors”
in volatility is to perform a principal component analysis (PCA) on at; see the
PCA of Chapter 8. Building a factor–volatility model thus involves a three-step
procedure:
• Select the ﬁrst few principal components that explain a high percentage of
variability in at.
--- page 571 ---

544
multivariate volatility models and their applications
• Build a volatility model for the selected principal components.
• Relate the volatility of each ait series to the volatilities of the selected principal
components.
The objective of such a procedure is to reduce the dimension but maintain an
accurate approximation of the multivariate volatility.
Example 10.8.
Consider again the monthly log returns, in percentages, of IBM
stock and the S&P 500 index of Example 10.5. Using the bivariate AR(3) model
of Example 8.4, we obtain an innovational series at. Performing a PCA on at
based on its covariance matrix, we obtained eigenvalues 63.373 and 13.489. The
ﬁrst eigenvalue explains 82.2% of the generalized variance of at. Therefore, we
may choose the ﬁrst principal component xt = 0.797a1t + 0.604a2t as the common
factor. Alternatively, as shown by the model in Example 8.4, the serial dependence
in rt is weak and, hence, one can perform the PCA on rt directly. For this particular
instance, the two eigenvalues of the sample covariance matrix of rt are 63.625 and
13.513, which are essentially the same as those based on at. The ﬁrst principal
component explains approximately 82.5% of the generalized variance of rt, and
the corresponding common factor is xt = 0.796r1t + 0.605r2t. Consequently, for
the two monthly log return series considered, the effect of the conditional mean
equations on PCA is negligible.
Based on the prior discussion and for simplicity, we use xt = 0.796r1t +
0.605r2t as a common factor for the two monthly return series. Figure 10.17(a)
shows the time plot of this common factor. If univariate Gaussian GARCH models
are entertained, we obtain the following model for xt:
xt = 1.317 + 0.096xt−1 + at,
at = σtϵt,
σ 2
t = 3.834 + 0.110a2
t−1 + 0.825σ 2
t−1.
(10.38)
All parameter estimates of the previous model are highly signiﬁcant at the 1% level,
and the Ljung–Box statistics of the standardized residuals and their squared series
fail to detect any model inadequacy. Figure 10.17(b) shows the ﬁtted volatility of
xt [i.e., the sample σ 2
t series in Eq. (10.38)].
Using σ 2
t of model (10.38) as a common volatility factor, we obtain the following
model for the original monthly log returns. The mean equations are
r1t = 1.140 + 0.079r1,t−1 + 0.067r1,t−2 −0.122r2,t−2 + a1t,
r2t = 0.537 + a2t,
where standard errors of the parameters in the ﬁrst equation are 0.211, 0.030, 0.031,
and 0.043, respectively, and standard error of the parameter in the second equation
