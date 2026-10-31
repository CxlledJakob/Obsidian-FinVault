# Analysis of Financial Time Series, Third Edition (Wiley -- Ruey S_ Tsay -- Wiley series in probability and statistics, 3rd ed_, -- John Wiley & Sons, -- isbn13 9780470414354 -- 9f99b80c7b2dedd477f463dc5323f3b6 -- An.pdf — pages 115–134

--- page 115 ---

88
linear time series analysis and its applications
The ﬁtted model is Rt = 0.0029 + 0.1253Jant + et, where the standard errors of
the estimates are 0.0033 and 0.0115, respectively. The right panel of Figure 2.16
shows the time plot and sample ACF of the residual series of the prior simple linear
regression. From the sample ACF, serial correlations at lags 12, 24, and 36 largely
disappear, suggesting that the seasonal pattern of the Decile 1 returns has been
successfully removed by the January dummy variable. Consequently, the seasonal
behavior in the monthly simple return of Decile 1 is mainly due to the January
effect.
R Demonstration
The following output has been edited and % denotes explanation:
> da=read.table("m-deciles08.txt",header=T)
> d1=da[,2]
> jan=rep(c(1,rep(0,11)),39) % Create January dummy.
> m1=lm(d1 jan)
> summary(m1)
Call:
lm(formula = d1
~ jan)
Coefficients:
Estimate Std. Error t value Pr(>|t|)
(Intercept) 0.002864
0.003333
0.859
0.391
jan
0.125251
0.011546
10.848
<2e-16 ***
---
Residual standard error: 0.06904 on 466 degrees of freedom
Multiple R-squared: 0.2016,
Adjusted R-squared: 0.1999
> m2=arima(d1,order=c(1,0,0),seasonal=list(order=c(1,0,1),
+ period=12))
> m2
Coefficients:
ar1
sar1
sma1
intercept
0.1769
0.9882
-0.9144
0.0118
s.e. 0.0456
0.0093
0.0335
0.0129
sigma^2 estimated as 0.004717: log likelihood=584.07,
aic=-1158.14
> tsdiag(m2,gof=36)
% plot not shown.
> m2=arima(d1,order=c(1,0,0),seasonal=list(order=c(1,0,1),
+ period=12),include.mean=F)
> m2
Call:
arima(x=d1,order=c(1,0,0),seasonal=list(order=c(1,0,1),
period=12),include.mean = F)
--- page 116 ---

seasonal models
89
Coefficients:
ar1
sar1
sma1
0.1787 0.9886 -0.9127 % Slightly differ from those of SCA.
s.e. 0.0456 0.0089
0.0335
sigma^2 estimated as 0.00472: log likelihood=583.68,
aic=-1159.36
SCA Demonstration
The following output has been edited:
input date,dec1,d2,d9,d10. file ’m-deciles08.txt’.
--
tsm m1. model (1)(12)dec1=(12)noise.
--
estim m1. hold resi(r1).
% Conditional MLE estimation
SUMMARY FOR UNIVARIATE TIME SERIES MODEL --
M1
--------------------------------------------------------------
VAR
TYPE OF
ORIGINAL
DIFFERENCING
VARIABLE OR CENTERED
DEC1 RANDOM
ORIGINAL
NONE
--------------------------------------------------------------
PAR.
VAR.
NUM./
FACTOR
ORDER CONS-
VALUE
STD
T
LABEL
NAME
DENOM.
TRAINT
ERROR
VALUE
1
D1
MA
1
12
NONE
.7388
.0488
15.14
2
D1
AR
1
1
NONE
.1765
.0447
3.95
3
D1
AR
2
12
NONE
.8698
.0295
29.49
EFFECTIVE NUMBER OF OBSERVATIONS . .
455
R-SQUARE . . . . . . . . . . . . . .
0.199
RESIDUAL STANDARD ERROR. . . . . . .
0.689906E-01
RESIDUAL STANDARD ERROR. . . . . . .
0.705662E-01
– –
estim m1. method exact. hold resi(r1)
% Exact MLE estimation
SUMMARY FOR UNIVARIATE TIME SERIES MODEL --
M1
--------------------------------------------------------------
VAR.
TYPE OF
ORIGINAL
DIFFERENCING
VAR.
OR CENTERED
DEC1
RANDOM
ORIGINAL
NONE
--------------------------------------------------------------
PAR.
VARI.
NUM./
FACTOR ORDER CONS-
VALUE
STD
T
LABEL
NAME
DENOM.
TRAINT
ERROR
VALUE
1
D1
MA
1
12
NONE
.9968
.0150
66.31
--- page 117 ---

90
linear time series analysis and its applications
2
D1
AR
1
1
NONE
.1884
.0448
4.21
3
D1
AR
2
12
NONE
.9505
.0070
135.46
EFFECTIVE NUMBER OF OBSERVATIONS . .
455
R-SQUARE . . . . . . . . . . . . . .
0.328
RESIDUAL STANDARD ERROR. . . . . . . 0.631807E-01
2.9
REGRESSION MODELS WITH TIME SERIES ERRORS
In many applications, the relationship between two time series is of major interest.
An obvious example is the market model in ﬁnance that relates the excess return
of an individual stock to that of a market index. The term structure of interest rates
is another example in which the time evolution of the relationship between interest
rates with different maturities is investigated. These examples lead naturally to the
consideration of a linear regression in the form
yt = α + βxt + et,
(2.43)
where yt and xt are two time series and et denotes the error term. The leastsquares (LS) method is often used to estimate model (2.43). If {et} is a white noise
series, then the LS method produces consistent estimates. In practice, however, it
is common to see that the error term et is serially correlated. In this case, we have
a regression model with time series errors, and the LS estimates of α and β may
not be consistent.
A regression model with time series errors is widely applicable in economics
and ﬁnance, but it is one of the most commonly misused econometric models
because the serial dependence in et is often overlooked. It pays to study the model
carefully.
We introduce the model by considering the relationship between two U.S. weekly
interest rate series:
1. r1t: the 1-year Treasury constant maturity rate
2. r3t: the 3-year Treasury constant maturity rate
Both series have 2467 observations from January 5, 1962, to April 10, 2009,
and are measured in percentages. The series are obtained from the Federal
Reserve Bank of St Louis. Strictly speaking, we should model the two interest
series jointly using multivariate time series analysis in Chapter 8. However, for
simplicity, we focus here on regression-type analysis and ignore the issue of
simultaneity.
Figure 2.17 shows the time plots of the two interest rates with a solid line
denoting the 1-year rate and a dashed line the 3-year rate. Figure 2.18(a) plots r1t
versus r3t, indicating that, as expected, the two interest rates are highly correlated.
A naive way to describe the relationship between the two interest rates is to use
--- page 118 ---

regression models with time series errors
91
Year
Percent
1970
1980
1990
2000
2010
0
5
10
15
Figure 2.17
Time plots of U.S. weekly interest rates (in percentages) from January 5, 1962, to April
10, 2009. Solid line is Treasury 1-year constant maturity rate and dashed line Treasury 3-year constant
maturity rate.
the simple model r3t = α + βr1t + et. This results in a ﬁtted model
r3t = 0.832 + 0.930r1t + et,
ˆσe = 0.523
(2.44)
with R2 = 96.5% , where the standard errors of the two coefﬁcients are 0.024 and
0.004, respectively. Model (2.44) conﬁrms the high correlation between the two
interest rates. However, the model is seriously inadequate, as shown by Figure 2.19,
which gives the time plot and ACF of its residuals. In particular, the sample ACF
of the residuals is highly signiﬁcant and decays slowly, showing the pattern of
a unit-root nonstationary time series. The behavior of the residuals suggests that
marked differences exist between the two interest rates. Using the modern econometric terminology, if one assumes that the two interest rate series are unit-root
nonstationary, then the behavior of the residuals of Eq. (2.44) indicates that the two
interest rates are not cointegrated; see Chapter 8 for discussion of cointegration.
In other words, the data fail to support the hypothesis that there exists a long-term
equilibrium between the two interest rates. In some sense, this is not surprising
because the pattern of “inverted yield curve” did occur during the data span. By
inverted yield curve we mean the situation under which interest rates are inversely
related to their time to maturities.
The unit-root behavior of both interest rates and the residuals of Eq. (2.44) leads
to the consideration of the change series of interest rates. Let
--- page 119 ---

92
linear time series analysis and its applications
1-yr rate
3-yr rate
0
5
10
15
5
10
15
(a)
Change in 1-yr rate
Change in 3-yr rate
−1.5 −1.0 −0.5 0.0
0.5
1.0
1.5
−1.0
−0.5
0.0
0.5
1.0
1.5
(b)
Figure 2.18
Scatterplots of U.S. weekly interest rates from January 5, 1962, to April 10, 2009:
(a) 3-year rate vs. 1-year rate and (b) changes in 3-year rate vs. changes in 1-year rate.
1. c1t = r1t −r1,t−1 = (1 −B)r1t for t ≥2: changes in the 1-year interest rate
2. c3t = r3t −r3,t−1 = (1 −B)r3t for t ≥2: changes in the 3-year interest rate
and consider the linear regression c3t = βc1t + et. Figure 2.20 shows time plots of
the two change series, whereas Figure 2.18(b) provides a scatterplot between them.
The change series remain highly correlated with a ﬁtted linear regression model
given by
c3t = 0.792c1t + et,
ˆσe = 0.0690,
(2.45)
with R2 = 82.5%. The standard error of the coefﬁcient is 0.0073. This model
further conﬁrms the strong linear dependence between interest rates. Figure 2.21
shows the time plot and sample ACF of the residuals of Eq. (2.45). Once again,
the ACF shows some signiﬁcant serial correlations in the residuals, but magnitudes
of the correlations are much smaller. This weak serial dependence in the residuals
can be modeled by using the simple time series models discussed in the previous
sections, and we have a linear regression with time series errors.
The main objective of this section is to discuss a simple approach for building a
linear regression model with time series errors. The approach is straightforward. We
employ a simple time series model discussed in this chapter for the residual series
--- page 120 ---

regression models with time series errors
93
Year
Residuals
1970
1980
1990
2000
2010
−1.5
0.5
0.5
(a)
(b)
Lag
ACF
0
10
20
30
−0.2
0.2
0.6
1.0
Figure 2.19
Residual series of linear regression (2.44) for two U.S. weekly interest rates: (a) time
plot and (b) sample ACF.
and estimate the whole model jointly. For illustration, consider the simple linear
regression in Eq. (2.45). Because residuals of the model are serially correlated, we
shall identify a simple ARMA model for the residuals. From the sample ACF of
the residuals shown in Figure 2.21, we specify an MA(1) model for the residuals
and modify the linear regression model to
c3t = βc1t + et,
et = at −θ1at−1,
(2.46)
where {at} is assumed to be a white noise series. In other words, we simply use
an MA(1) model, without the constant term, to capture the serial dependence in
the error term of Eq. (2.45). The resulting model is a simple example of linear
regression with time series errors. In practice, more elaborated time series models
can be added to a linear regression equation to form a general regression model
with time series errors.
Estimating a regression model with time series errors was not easy before the
advent of modern computers. Special methods such as the Cochrane–Orcutt estimator have been proposed to handle the serial dependence in the residuals; see Greene
(2003, p. 273). By now, the estimation is as easy as that of other time series models. If the time series model used is stationary and invertible, then one can estimate
the model jointly via the maximum-likelihood method. This is the approach we
take by using either the SCA or R package. R and S-Plus demonstrations are given
--- page 121 ---

94
linear time series analysis and its applications
Year
Change
Change
1970
1980
1990
2000
2010
1970
1980
1990
2000
2010
−1.5
−0.5
0.5
1.5
(a)
Year
−1.0
0.0
1.0
(b)
Figure 2.20
Time plots of change series of U.S. weekly interest rates from January 12, 1962, to April
10, 2009: (a) changes in Treasury 1-year constant maturity rate and (b) changes in Treasury 3-year
constant maturity rate.
later. For the U.S. weekly interest rate data, the ﬁtted version of model (2.46) is
c3t = 0.794c1t + et,
et = at + 0.1823at−1,
ˆσa = 0.0678,
(2.47)
with R2 = 83.1%. The standard errors of the parameters are 0.0075 and 0.0196,
respectively. The model no longer has a signiﬁcant lag-1 residual ACF, even though
some minor residual serial correlations remain at lags 4, 6, and 7. The incremental
improvement of adding additional MA parameters at lags 4, 6, and 7 to the residual
equation is small and the result is not reported here.
Comparing the models in Eqs. (2.44), (2.45), and (2.47), we make the following
observations. First, the high R2 96.5% and coefﬁcient 0.930 of model (2.44) are
misleading because the residuals of the model show strong serial correlations.
Second, for the change series, R2 and the coefﬁcient of c1t of models (2.45) and
(2.47) are close. In this particular instance, adding the MA(1) model to the change
series only provides a marginal improvement. This is not surprising because the
estimated MA coefﬁcient is small numerically, even though it is statistically highly
signiﬁcant. Third, the analysis demonstrates that it is important to check residual
serial dependence in linear regression analysis.
--- page 122 ---

regression models with time series errors
95
Year
Residuals
1970
1980
1990
2000
2010
−0.4
0.0 0.2 0.4
(a)
(b)
Lag
ACF
0
10
20
30
0.0
0.4
0.8
Figure 2.21
Residual series of linear regression (2.45) for two change series of U.S. weekly interest
rates: (a) time plot and (b) sample ACF.
From Eq. (2.47), the model shows that the two weekly interest rate series are
related as
r3t = r3,t−1 + 0.794(r1t −r1,t−1) + at + 0.182at−1.
The interest rates are concurrently and serially correlated.
R Demonstration
The following output has been edited.
> r1=read.table("w-gs1yr.txt",header=T)[,4]
> r3=read.table("w-gs3yr.txt",header=T)[,4]
> m1=lm(r3 r1)
> summary(m1)
Call:
lm(formula = r3
~ r1)
Coefficients:
Estimate Std. Error t value Pr(>|t|)
(Intercept ) 0.83214
0.02417
34.43
<2e-16 ***
r1
0.92955
0.00357
260.40
<2e-16 ***
--- page 123 ---

96
linear time series analysis and its applications
---
Residual standard error: 0.5228 on 2465 degrees of freedom
Multiple R-squared: 0.9649,
Adjusted R-squared: 0.9649
> plot(m1$residuals,type=’l’)
> acf(m1$residuals,lag=36)
> c1=diff(r1)
> c3=diff(r3)
> m2=lm(c3 -1+c1)
> summary(m2)
Call:
lm(formula = c3
~ -1 + c1)
Coefficients:
Estimate Std. Error t value
Pr(>|t|)
c1
0.791935
0.007337
107.9
<2e-16 ***
---
Residual standard error: 0.06896 on 2465 degrees of freedom
Multiple R-squared: 0.8253,
Adjusted R-squared: 0.8253
> acf(m2$residuals,lag=36)
> m3=arima(c3,order=c(0,0,1),xreg=c1,include.mean=F)
> m3
Call:
arima(x = c3, order = c(0, 0, 1), xreg = c1, include.mean = F)
Coefficients:
ma1
c1
0.1823
0.7936
s.e.
0.0196
0.0075
sigma^2 estimated as 0.0046: log likelihood=3136.62,
aic=-6267.23
>
> rsq=(sum(c3^2)-sum(m3$residuals^2))/sum(c3^2)
> rsq
[1] 0.8310077
Summary
We outline a general procedure for analyzing linear regression models with time
series errors:
1. Fit the linear regression model and check serial correlations of the
residuals.
2. If the residual series is unit-root nonstationary, take the ﬁrst difference of
both the dependent and explanatory variables. Go to step 1. If the residual
series appears to be stationary, identify an ARMA model for the residuals
and modify the linear regression model accordingly.
--- page 124 ---

consistent covariance matrix estimation
97
3. Perform a joint estimation via the maximum-likelihood method and check
the ﬁtted model for further improvement.
To check the serial correlations of residuals, we recommend that the Ljung–Box
statistics be used instead of the Durbin–Watson (DW) statistic because the latter
only considers the lag-1 serial correlation. There are cases in which serial dependence in residuals appears at higher order lags. This is particularly so when the
time series involved exhibits some seasonal behavior.
Remark.
For a residual series et with T observations, the Durbin–Watson
statistic is
DW =
T
t=2(et −et−1)2
T
t=1 e2
t
.
Straightforward calculation shows that DW ≈2(1 −ˆρ1), where ˆρ1 is the lag-1 ACF
of {et}.
□
In S-Plus, regression models with time series errors can be analyzed by the
command OLS (ordinary least squares) if the residuals assume an AR model.
Also, to identify a lagged variable, the command is tslag, for example, y =
tslag(r,1). For the interest rate series, the relevant commands follow, where %
denotes explanation of the command:
> r1t=read.table("w-gs1yr.txt",header=T)[,4] %load data
> r3t=read.table("w-gs3yr.txt",header=T)[,4]
> fit=OLS(r3t~r1t)
% fit the first regression
> summary(fit)
> c3t=diff(r3t)
% take difference
> c1t=diff(r1t)
> fit1=OLS(c3t~c1t)
% fit second regression
> summary(fit1)
> fit2=OLS(c3t~c1t+tslag(c3t,1)+tslag(c1t,1), na.rm=T)
> summary(fit2)
See the output in the next section for more information.
2.10
CONSISTENT COVARIANCE MATRIX ESTIMATION
Consider again the regression model in Eq. (2.43). There may exist situations in
which the error term et has serial correlations and/or conditional heteroscedasticity,
but the main objective of the analysis is to make inference concerning the regression
coefﬁcients α and β. See Chapter 3 for discussion of conditional heteroscedasticity.
In situations under which the OLS estimates of the coefﬁcients remain consistent,
methods are available to provide consistent estimate of the covariance matrix of
--- page 125 ---

98
linear time series analysis and its applications
the coefﬁcient estimates. Two such methods are widely used. The ﬁrst method is
called the heteroscedasticity consistent (HC) estimator; see Eicker (1967) and White
(1980). The second method is called the heteroscedasticity and autocorrelation
consistent (HAC) estimator; see Newey and West (1987).
For ease in discussion, we shall rewrite the regression model as
yt = x′
tβ + et,
t = 1, . . . , T,
(2.48)
where yt is the dependent variable, xt = (x1t, . . . , xkt)′ is a k-dimensional vector
of explanatory variables including constant, and β = (β1, . . . , βk)′ is the parameter
vector. Here c′ denotes the transpose of the vector c. The LS estimate of β and
the associate covariance matrix are
ˆβ =
 T

t=1
xtx′
t
−1
T

t=1
xtyt,
Cov( ˆβ) = σ 2
e
 T

t=1
xtx′
t
−1
,
where σ 2
e is the variance of et and is estimated by the variance of the residuals of the
regression. In the presence of serial correlations or conditional heteroscedasticity,
the prior covariance matrix estimator is inconsistent, often resulting in inﬂating the
t ratios of ˆβ.
The estimator of White (1980) is
Cov( ˆβ)HC =
 T

t=1
xtx′
t
−1  T

t=1
ˆe2
t xtx′
t
  T

t=1
xtx′
t
−1
,
(2.49)
where ˆet = yt −x′
t ˆβ is the residual at time t. The estimator of Newey and West
(1987) is
Cov( ˆβ)HAC =
 T

t=1
xtx′
t
−1
CHAC
 T

t=1
xtx′
t
−1
,
(2.50)
where
CHAC =
T

t=1
ˆe2
t xtx′
t +
ℓ

j=1
wj
T

t=j+1
(xt ˆetet−jx′
t−j + xt−j ˆet−j ˆetx′
t),
where ℓis a truncation parameter and wj is a weight function such as the Bartlett
weight function deﬁned by
wj = 1 −
j
ℓ+ 1.
--- page 126 ---

consistent covariance matrix estimation
99
Other weight functions can also be used. Newey and West (1987) suggest choosing
ℓto be the integer part of 4(T /100)2/9. This estimator essentially uses a nonparametric method to estimate the covariance matrix of {T
t=1 ˆetxt}.
For illustration, we employ the ﬁrst differenced interest rate series in Eq. (2.45).
The t ratio of the coefﬁcient of c1t is 107.91 if both serial correlation and heteroscedasticity in the residuals are ignored, it becomes 48.44 when the HC estimator
is used, and it reduces to 39.92 when the HAC estimator is used. The S-Plus demonstration below also uses a regression that includes lagged values c1,t−1 and c3,t−1
as regressors to take care of serial correlations in the residuals. One can also apply
the HC or HAC estimator to the ﬁtted model to reﬁne the t ratios of the coefﬁcient
estimates.
S-Plus Demonstration
The following output has been edited and % denotes explanation:
> module(finmetrics)
> r1=read.table("w-gs1yr.txt",header=T)[,4] % Load data
> r3=read.table("w-gs3yr.txt",header=T)[,4]
> c1=diff(r1) % Take 1st difference
> c3=diff(r3)
> reg.fit=OLS(c3~c1) % Fit a simple linear regression.
> summary(reg.fit)
Call:
OLS(formula = c3
~ c1)
Residuals:
Min
1Q
Median
3Q
Max
-0.4246
-0.0358
-0.0012
0.0347
0.4892
Coefficients:
Value Std. Error
t value
Pr(>|t|)
(Intercept)
-0.0001
0.0014
-0.0757
0.9397
c1
0.7919
0.0073
107.9063
0.0000
Regression Diagnostics:
R-Squared 0.8253
Adjusted R-Squared 0.8253
Durbin-Watson Stat 1.6456
Residual Diagnostics:
Stat
P-Value
Jarque-Bera
1644.6146
0.0000
Ljung-Box
230.0477
0.0000
Residual standard error: 0.06897 on 2464 degrees of freedom
> summary(reg.fit,correction="white") % Use HC the estimator
--- page 127 ---

100
linear time series analysis and its applications
Coefficients:
Value Std. Error
t value
Pr(>|t|)
(Intercept)
-0.0001
0.0014
-0.0757
0.9396
c1
0.7919
0.0163
48.4405
0.0000
> summary(reg.fit,correction="nw") % Use the HAC estimator
Coefficients:
Value Std. Error
t value
Pr(>|t|)
(Intercept)
-0.0001
0.0016
-0.0678
0.9459
c1
0.7919
0.0198
39.9223
0.0000
% Below, fit a regression model with time series errors.
> reg.ts=OLS(c3~c1+tslag(c3,1)+tslag(c1,1),na.rm=T)
> summary(reg.ts)
Call:
OLS(formula = c3
~ c1 + tslag(c3, 1)+tslag(c1, 1), na.rm = T)
Residuals:
Min
1Q
Median
3Q
Max
-0.4481
-0.0355
-0.0008
0.0341
0.4582
Coefficients:
Value Std. Error
t value
Pr(>|t|)
(Intercept)
-0.0001
0.0014
-0.0636
0.9493
c1
0.7971
0.0077
103.6320
0.0000
tslag(c3, 1)
0.1766
0.0198
8.9057
0.0000
tslag(c1, 1)
-0.1580
0.0174
-9.0583
0.0000
Regression Diagnostics:
R-Squared 0.8312
Adjusted R-Squared 0.8310
Durbin-Watson Stat 1.9865
Residual Diagnostics:
Stat
P-Value
Jarque-Bera 1620.5090
0.0000
Ljung-Box
131.6048
0.0000
Residual standard error: 0.06785 on 2461 degrees of freedom
Let
ˆβj be the jth element of ˆβ. When k > 1, the HC variance of
ˆβj in
Eq. (2.49) can be obtained by using an auxiliary regression. Let x−j,t be the
(k −1)-dimensional vector obtained by removing the element xjt from xt.
Consider the auxiliary regression
xjt = x′
−j,tγ + vt,
t = 1, . . . , T.
(2.51)
--- page 128 ---

long-memory models
101
Let ˆvt be the least-squares residual of this auxiliary regression. It can be shown
that
Var( ˆβj)HC =
T
t=1 ˆe2
t ˆv2
t
T
t=1 ˆv2
t
2 ,
where ˆet is the residual of original regression in Eq. (2.48). The auxiliary regression
is simply a step taken to achieve orthogonality between ˆvt and the rest of the
regressors so that the formula in Eq. (2.49) can be simpliﬁed.
2.11
LONG-MEMORY MODELS
We have discussed that for a stationary time series the ACF decays exponentially to
zero as lag increases. Yet for a unit-root nonstationary time series, it can be shown
that the sample ACF converges to 1 for all ﬁxed lags as the sample size increases;
see Chan and Wei (1988) and Tiao and Tsay (1983). There exist some time series
whose ACF decays slowly to zero at a polynomial rate as the lag increases. These
processes are referred to as long-memory time series. One such example is the
fractionally differenced process deﬁned by
(1 −B)dxt = at,
−0.5 < d < 0.5,
(2.52)
where {at} is a white noise series. Properties of model (2.52) have been widely
studied in the literature (e.g., Hosking, 1981). We now summarize some of these
properties:
1. If d < 0.5, then xt is a weakly stationary process and has the inﬁnite MA
representation
xt = at +
∞

i=1
ψiat−i
with
ψk
= d(1 + d) · · · (k −1 + d)
k!
= (k + d −1)!
k!(d −1)! .
2. If d > −0.5, then xt is invertible and has the inﬁnite AR representation
xt =
∞

i=1
πixt−i + at
with
πk
= −d(1 −d) · · · (k −1 −d)
k!
= (k −d −1)!
k!(−d −1)! .
--- page 129 ---

102
linear time series analysis and its applications
3. For −0.5 < d < 0.5, the ACF of xt is
ρk = d(1 + d) · · · (k −1 + d)
(1 −d)(2 −d) · · · (k −d),
k = 1, 2, . . . .
In particular, ρ1 = d/(1 −d) and
ρk ≈
(−d)!
(d −1)!k2d−1
as
k →∞.
4. For −0.5 < d < 0.5, the PACF of xt is φk,k = d/(k −d) for k = 1, 2, . . . .
5. For −0.5 < d < 0.5, the spectral density function f (ω) of xt, which is the
Fourier transform of the ACF of xt, satisﬁes
f (ω) ∼ω−2d,
as
ω →0,
(2.53)
where ω ∈[0, 2π] denotes the frequency.
Of particular interest here is the behavior of ACF of xt when d < 0.5. The property
says that ρk ∼k2d−1, which decays at a polynomial, instead of exponential, rate.
For this reason, such an xt process is called a long-memory time series. A special
characteristic of the spectral density function in Eq. (2.53) is that the spectrum
diverges to inﬁnity as ω →0. However, the spectral density function of a stationary
ARMA process is bounded for all ω ∈[0, 2π].
Earlier we used the binomial theorem for noninteger powers
(1 −B)d =
∞

k=0
(−1)k
 d
k

Bk,
 d
k

= d(d −1) · · · (d −k + 1)
k!
.
If the fractionally differenced series (1 −B)dxt follows an ARMA(p, q) model,
then xt is called an ARFIMA(p, d, q) process, which is a generalized ARIMA
model by allowing for noninteger d.
In practice, if the sample ACF of a time series is not large in magnitude,
but decays slowly, then the series may have long memory. As an illustration,
Figure 2.22 shows the sample ACFs of the absolute series of daily simple returns
for the CRSP valueand equal-weighted indexes from January 2, 1970, to December 31, 2008. The ACFs are relatively small in magnitude but decay very slowly;
they appear to be signiﬁcant at the 5% level even after 300 lags. For more information about the behavior of sample ACF of absolute return series, see Ding, Granger,
and Engle (1993). For the pure fractionally differenced model in Eq. (2.52), one
can estimate d using either a maximum-likelihood method or a regression method
with logged periodogram at the lower frequencies. Finally, long-memory models
have attracted some attention in the ﬁnance literature in part because of the work
on fractional Brownian motion in the continuous-time models.
--- page 130 ---

appendix: some sca commands
103
Lag
ACF
0
50
100
150
200
250
300
−0.1
0.10.20.30.4
(a)
Lag
ACF
0
50
100
150
200
250
300
−0.1
0.10.20.30.4
(b)
Figure 2.22
Sample autocorrelation function of absolute series of daily simple returns for CRSP
valueand equal-weighted indexes: (a) value-weighted index return and (b) equal-weighted index return.
Sample period is from January 2, 1970, to December 31, 2008.
APPENDIX: SOME SCA COMMANDS
In this appendix, we give the SCA commands used in Section 2.9. The 1-year
maturity interest rates are in the ﬁle w-gs1yr.txt and the 3-year rates are in the
ﬁle w-gs3yr.txt.
-- load the data into SCA, denote the data by rate1 and rate3.
input year,mom,day,rate1. file ‘w-gs1yr.txt’
--
input year,mon,day,rate3. file ‘w-gs3yr.txt’
-- specify a simple linear regression model.
tsm m1. model rate3=b0+(b1)rate1+noise.
-- estimate the specified model and store residual in r1.
estim m1. hold resi(r1).
-- compute 10 lags of residual acf.
acf r1. maxl 10.
-- difference the two series, denote the new series by c1t
and c3t
diff old rate1,rate3. new c1t, c3t. compress.
-- specify a linear regression model for the differenced data
tsm m2. model c3t=h0+(h1)c1t+noise.
-- estimation
estim m2. hold resi(r2).
-- compute residual acf.
--- page 131 ---

104
linear time series analysis and its applications
acf r2. maxl 10.
-- specify a regression model with time series errors.
tsm m3. model c3t=g0+(g1)c1t+(1)noise.
-- estimate the model using the exact likelihood method.
estim m3. method exact. hold resi(r3).
-- compute residual acf.
acf r3. maxl 10.
-- refine the model to include more MA lags.
tsm m4. model c3t=g0+(g1)c1t+(1,4,6,7)noise.
-- estimation
estim m4. method exact. hold resi(r4).
-- compute residual acf.
acf r4. maxl 10.
-- exit SCA
stop
EXERCISES
If not speciﬁcally speciﬁed, use 5% signiﬁcance level to draw conclusions in the
exercises.
2.1. Suppose that the simple return of a monthly bond index follows the MA(1)
model
Rt = at + 0.2at−1,
σa = 0.025.
Assume that a100 = 0.01. Compute the 1-stepand 2-step-ahead forecasts
of the return at the forecast origin t = 100. What are the standard deviations of the associated forecast errors? Also compute the lag-1 and lag-2
autocorrelations of the return series.
2.2. Suppose that the daily log return of a security follows the model
rt = 0.01 + 0.2rt−2 + at,
where {at} is a Gaussian white noise series with mean zero and variance 0.02.
What are the mean and variance of the return series rt? Compute the lag-1
and lag-2 autocorrelations of rt. Assume that r100 = −0.01, and r99 = 0.02.
Compute the 1- and 2-step-ahead forecasts of the return series at the forecast
origin t = 100. What are the associated standard deviations of the forecast
errors?
2.3. Consider the monthly U.S. unemployment rate from January 1948 to March
2009 in the ﬁle m-unrate.txt. The data are seasonally adjusted and
obtained from the Federal Reserve Bank of St Louis. Build a time series
model for the series and use the model to forecast the unemployment rate
for the April, May, June, and July of 2009. In addition, does the ﬁtted
model imply the existence of business cycles? Why? (Note that there are
more than one model ﬁts the data well. You only need an adequate model.)
--- page 132 ---

exercises
105
2.4. Consider the monthly simple returns of the Decile 1, Decile 2, Decile 9, and
Decile 10 of NYSE/AMEX/NASDAQ based on market capitalization. The
data span is from January 1970 to December 2008, and the data are obtained
from CRSP.
(a) For the return series of Decile 2 and Decile 10, test the null hypothesis
that the ﬁrst 12 lags of autocorrelations are zero at the 5% level. Draw
your conclusion.
(b) Build an ARMA model for the return series of Decile 2. Perform model
checking and write down the ﬁtted model.
(c) Use the ﬁtted ARMA model to produce 1- to 12-step-ahead forecasts of
the series and the associated standard errors of forecasts.
2.5. Consider the daily simple returns of IBM stock from 1970 to 2008 in the
ﬁle d-ibm3dx7008.txt. Compute the ﬁrst 100 lags of ACF of the absolute
series of daily simple returns of IBM stock. Is there evidence of long-range
dependence? Why?
2.6. Consider the demand of electricity of a manufacturing sector in the United
States. The data are logged, denote the demand of a ﬁxed day of each month,
and are in power6.txt. Build a time series model for the series and use the
ﬁtted model to produce 1- to 24-step-ahead forecasts.
2.7. Consider the daily simple returns of IBM stock, CRSP value-weighted index,
CRSP equal-weighted index, and the S&P composite index from January
1980 to December 2008. The index returns include dividend distributions.
The data ﬁle is d-ibm3dxwkdays8008.txt, which has 12 columns. The
columns are (year, month, day, IBM, VW, EW, SP, M, T, W, H, F), where M,
T, W, R, and F denotes indicator variables for Monday to Friday, respectively.
Use a regression model to study the effects of trading days on the equalweighted index returns. What is the ﬁtted model? Are the weekday effects
signiﬁcant in the returns at the 5% level? Use the HAC estimator of the
covariance matrix to obtain the t ratio of regression estimates. Does the
HAC estimator change the conclusion of weekday effects? Are there serial
correlations in the regression residuals? If yes, build a regression model with
time series error to study weekday effects.
2.8. Consider the data set of the previous question, but focus on the daily simple
returns of the S&P composite index. Perform the necessary data analysis
and statistical tests using the 5% signiﬁcance level to answer the following
questions:
(a) Is there any weekday effect on the daily simple returns of the S&P composite index? You may employ a linear regression model to answer this
question. Estimate the model, check its validity, and test the hypothesis
that there is no Friday effect. Draw your conclusion.
(b) Check the residual serial correlations using Q(12) statistic. Are there any
signiﬁcant serial correlations in the residuals? If yes, build a regression
model with time series errors for the data.
--- page 133 ---

106
linear time series analysis and its applications
2.9. Now consider similar questions of the previous exercise for the IBM stock
returns.
(a) Is there any weekday effect on the daily simple returns of IBM stock?
Estimate your model and test the hypothesis that there is no Friday effect.
Draw your conclusion.
(b) Are there serial correlations in the residuals? Use Q(12) to perform the
test. Draw your conclusion.
(c) Reﬁne the above model by using the technique of regression model with
time series errors. In there a signiﬁcant weekday effect based on the
reﬁned model?
2.10. Consider the weekly yields of Moody’s Aaa and Baa seasoned bonds from
January 5, 1962, to April 10, 2009. The data are obtained from the Federal
Reserve Bank of St Louis. Weekly yields are averages of daily yields. Obtain
the summary statistics (sample mean, standard deviation, skewness, excess
kurtosis, minimum, and maximum) of the two yield series. Are the bond
yields skewed? Do they have heavy tails? Answer the questions using 5%
signiﬁcance level.
2.11. Consider the monthly Aaa bond yields of the prior problem. Build a time
series model for the series.
2.12. Again, consider the two bond yield series, that is, Aaa and Baa. What is the
relationship between the two series? To answer this question, build a time
series model using yields of Aaa bonds as the dependent variable and yields
of Baa bonds as independent variable.
2.13. Consider the monthly log returns of CRSP equal-weighted index from January 1962 to December 1999 for 456 observations. You may obtain the data
from CRSP directly or from the ﬁle m-ew6299.txt on the Web.
(a) Build an AR model for the series and check the ﬁtted model.
(b) Build an MA model for the series and check the ﬁtted model.
(c) Compute 1- and 2-step-ahead forecasts of the AR and MA models built
in the previous two questions.
(d) Compare the ﬁtted AR and MA models.
2.14. This problem is concerned with the dynamic relationship between the spot
and futures prices of the S&P 500 index. The data ﬁle sp5may.dat has
three columns: log(futures price), log(spot price), and cost-of-carry (×100).
The data were obtained from the Chicago Mercantile Exchange for the S&P
500 stock index in May 1993 and its June futures contract. The time interval
is 1 minute (intraday). Several authors used the data to study index futures
arbitrage. Here we focus on the ﬁrst two columns. Let ft and st be the
log prices of futures and spot, respectively. Consider yt = ft −ft−1 and
xt = st −st−1. Build a regression model with time series errors between {yt}
and {xt}, with yt being the dependent variable.
--- page 134 ---

references
107
2.15. The quarterly gross domestic product implicit price deﬂator is often used
as a measure of inﬂation. The ﬁle q-gdpdef.txt contains the data for the
United States from the ﬁrst quarter of 1947 to the last quarter of 2008. Data
format is year, month, day, and deﬂator. The data are seasonally adjusted
and equal to 100 for year 2000. Build an ARIMA model for the series and
check the validity of the ﬁtted model. Use the ﬁtted model to predict the
inﬂation for each quarter of 2009. The data are obtained from the Federal
Reserve Bank of St Louis.
REFERENCES
Akaike, H. (1973). Information theory and an extension of the maximum likelihood principle.
In B. N. Petrov and F. Csaki, (eds.). 2nd International Symposium on Information
Theory, pp. 267–281. Akademia Kiado, Budapest.
Box, G. E. P. and Pierce, D. (1970). Distribution of residual autocorrelations in
autoregressive-integrated moving average time series models. Journal of the American
Statistical Association 65: 1509–1526.
Box, G. E. P., Jenkins, G. M., and Reinsel, G. C. (1994). Time Series Analysis: Forecasting
and Control, 3rd ed. Prentice Hall, Englewood Cliffs, NJ.
Brockwell, P. J. and Davis, R. A. (1991). Time Series: Theory and Methods, 2nd ed. Springer,
New York.
Brockwell, P. J. and Davis, R. A. (1996). Introduction to Time Series and Forecasting.
Springer, New York.
Chan, N. H. and Wei, C. Z. (1988). Limiting distributions of least squares estimates of
unstable autoregressive processes. Annals of Statistics 16: 367–401.
Dickey, D. A. and Fuller, W. A. (1979). Distribution of the estimates for autoregressive time series with a unit root. Journal of the American Statistical Association 74:
427–431.
Ding, Z., Granger, C. W. J., and Engle, R. F. (1993). A long memory property of stock
returns and a new model. Journal of Empirical Finance 1: 83–106.
Eicker, F. (1967). Limit theorems for regression with unequal and dependent Errors. In L.
LeCam and J. Neyman (eds.). Proceedings of the 5th Berkeley Symposium on Mathematical Statistics and Probability. University of California Press, Berkeley.
Fuller, W. A. (1976). Introduction to Statistical Time Series, Wiley, New York.
Greene, W. H. (2003). Econometric Analysis, 5th ed. Prentice-Hall, Upper Saddle River,
NJ.
Hosking, J. R. M. (1981). Fractional differencing. Biometrika 68: 165–176.
Ljung, G. and Box, G. E. P. (1978). On a measure of lack of ﬁt in time series models.
Biometrika 66: 67–72.
Newey, W. and West, K. (1987). A simple positive semideﬁnite, heteroscedasticity and
autocorrelation consistent covariance matrix. Econometrica 55: 863–898.
Phillips, P. C. B. (1987). Time series regression with a unit root. Econometrica 55: 277–301.
