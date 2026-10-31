# Analysis of Financial Time Series, Third Edition (Wiley -- Ruey S_ Tsay -- Wiley series in probability and statistics, 3rd ed_, -- John Wiley & Sons, -- isbn13 9780470414354 -- 9f99b80c7b2dedd477f463dc5323f3b6 -- An.pdf — pages 77–96

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
--- page 78 ---

simple ar models
51
model is found to be inadequate, it must be reﬁned. For instance, if some of the
estimated AR coefﬁcients are not signiﬁcantly different from zero, then the model
should be simpliﬁed by trying to remove those insigniﬁcant parameters. If residual
ACF shows additional serial correlations, then the model should be extended to
take care of those correlations.
Remark.
Most time series packages do not adjust the degrees of freedom when
applying the Ljung–Box statistics Q(m) to a residual series. This is understandable
when m ≤g.
□
Consider the residual series of the ﬁtted AR(3) model for the monthly valueweighted simple returns. We have Q(12) = 16.35 with a p value 0.060 based on
its asymptotic chi-squared distribution with 9 degrees of freedom. Thus, the null
hypothesis of no residual serial correlation in the ﬁrst 12 lags is barely not rejected
at the 5% level. However, since the lag-2 AR coefﬁcient is not signiﬁcant at the
5% level, one can reﬁne the model as
rt = 0.0088 + 0.114rt−1 −0.106rt−3 + at,
ˆσa = 0.0536,
where all the estimates are now signiﬁcant at the 1% level. The residual series
gives Q(12) = 16.83 with a p value 0.078 (based on χ2
10). The model is adequate
in modeling the dynamic linear dependence of the data.
R Demonstration
In the following R demonstration, % denotes an explanation:
> vw=read.table(’m-ibm3dx2608.txt’,header=T)[,3]
> m3=arima(vw,order=c(3,0,0))
> m3
Call:
arima(x = vw, order = c(3, 0, 0))
Coefficients:
ar1
ar2
ar3
intercept
0.1158
-0.0187
-0.1042
0.0089
s.e.
0.0315
0.0317
0.0317
0.0017
sigma^2 estimated as 0.002875: log likelihood=1500.86,
aic=-2991.73
> (1-.1158+.0187+.1042)*mean(vw) % Compute
the intercept phi(0).
[1] 0.00896761
> sqrt(m3$sigma2)
% Compute standard error of residuals
[1] 0.0536189
> Box.test(m3$residuals,lag=12,type=’Ljung’)
--- page 79 ---

52
linear time series analysis and its applications
Box-Ljung test
data: m3$residuals
% R uses 12 degrees of freedom
X-squared = 16.3525, df = 12, p-value = 0.1756
> pv=1-pchisq(16.35,9) % Compute p-value using 9 degrees
of freedom
> pv
[1] 0.05992276
% To fix the AR(2) coef to zero:
> m3=arima(vw,order=c(3,0,0),fixed=c(NA,0,NA,NA))
% The subcommand ’fixed’ is used to fix parameter values,
% where NA denotes estimation and 0 means fixing the
parameter to 0.
% The ordering of the parameters can be found using m3$coef.
> m3
Call:
arima(x = vw, order = c(3, 0, 0), fixed = c(NA, 0, NA, NA))
Coefficients:
ar1
ar2
ar3
intercept
0.1136
0
-0.1063
0.0089
s.e.
0.0313
0
0.0315
0.0017
sigma^2 estimated as 0.002876: log likelihood=1500.69,
aic=-2993.38
> (1-.1136+.1063)*.0089 % Compute phi(0)
[1] 0.00883503
> sqrt(m3$sigma2)
% Compute residual standard error
[1] 0.05362832
> Box.test(m3$residuals,lag=12,type=’Ljung’)
Box-Ljung test
data: m3$residuals
X-squared = 16.8276, df = 12, p-value = 0.1562
> pv=1-pchisq(16.83,10)
> pv
[1] 0.0782113
S-Plus Demonstration
The following S-Plus output has been edited:
> vw=read.table(’m-ibm3dx2608.txt’,header=T)[,3]
> ar3=OLS(vw ar(3))
--- page 80 ---

simple ar models
53
> summary(ar3)
Call:
OLS(formula = vw
~ ar(3))
Residuals:
Min
1Q
Median
3Q
Max
-0.2863
-0.0263
0.0034
0.0297
0.3689
Coefficients:
Value
Std. Error t value Pr(>|t|)
(Intercept)
0.0091
0.0018
5.1653
0.0000
lag1
0.1148
0.0316
3.6333
0.0003
lag2
-0.0188
0.0318
-0.5894
0.5557
lag3
-0.1043
0.0318
-3.2763
0.0011
Regression Diagnostics:
R-Squared 0.0246
Adjusted R-Squared 0.0216
Durbin-Watson Stat 1.9913
Residual Diagnostics:
Stat
P-Value
Jarque-Bera 1656.3928
0.0000
Ljung-Box
50.1279
0.0087
Residual standard error: 0.05375 on 989 degrees of freedom
> autocorTest(ar3$residuals,lag=12)
Test for Autocorrelation: Ljung-Box
Null Hypothesis: no autocorrelation
Test Statistics:
Test Stat 16.5668
p.value
0.1666
% S-Plus uses 12 degrees of freedom
Dist. under Null: chi-square with 12 degrees of freedom
Total Observ.: 993
> 1-pchisq(16.57,9) % Compute p-value with 9 degrees
of freedom
[1] 0.05589128
2.4.3
Goodness of Fit
A commonly used statistic to measure goodness of ﬁt of a stationary model is the
R square (R2) deﬁned as
R2 = 1 −residual sum of squares
total sum of squares
.
--- page 81 ---

54
linear time series analysis and its applications
For a stationary AR(p) time series model with T observations {rt|t = 1, . . . , T },
the measure becomes
R2 = 1 −
T
t=p+1 ˆa2
t
T
t=p+1(rt −¯r)2 ,
where ¯r = T
t=p+1 rt/(T −p). It is easy to show that 0 ≤R2 ≤1. Typically, a
larger R2 indicates that the model provides a closer ﬁt to the data. However, this is
only true for a stationary time series. For the unit-root nonstationary series discussed
later in this chapter, R2 of an AR(1) ﬁt converges to one when the sample size
increases to inﬁnity, regardless of the true underlying model of rt.
For a given data set, it is well known that R2 is a nondecreasing function of
the number of parameters used. To overcome this weakness, an adjusted R2 is
proposed, which is deﬁned as
Adj −R2 = 1 −variance of residuals
variance of rt
= 1 −ˆσ 2
a
ˆσ 2r
,
where ˆσ 2
r is the sample variance of rt. This new measure takes into account the
number of parameters used in the ﬁtted model. However, it is no longer between
0 and 1.
2.4.4
Forecasting
Forecasting is an important application of time series analysis. For the AR(p)
model in Eq. (2.9), suppose that we are at the time index h and are interested
in forecasting rh+ℓ, where ℓ≥1. The time index h is called the forecast origin
and the positive integer ℓis the forecast horizon. Let ˆrh(ℓ) be the forecast of rh+ℓ
using the minimum squared error loss function. In other words, the forecast ˆrk(ℓ)
is chosen such that
E{[rh+ℓ−ˆrh(ℓ)]2|Fh} ≤min
g E[(rh+ℓ−g)2|Fh],
where g is a function of the information available at time h (inclusive), that is,
a function of Fh. We referred to ˆrh(ℓ) as the ℓ-step ahead forecast of rt at the
forecast origin h. Let Fh be the collection of information available at the forecast
origin h.
1-Step-Ahead Forecast
From the AR(p) model, we have
rh+1 = φ0 + φ1rh + · · · + φprh+1−p + ah+1.
--- page 82 ---

simple ar models
55
Under the minimum squared error loss function, the point forecast of rh+1 given
Fh is the conditional expectation
ˆrh(1) = E(rh+1|Fh) = φ0 +
p

i=1
φirh+1−i,
and the associated forecast error is
eh(1) = rh+1 −ˆrh(1) = ah+1.
Consequently, the variance of the 1-step-ahead forecast error is Var[eh(1)] =
Var(ah+1) = σ 2
a . If at is normally distributed, then a 95% 1-step-ahead interval
forecast of rh+1 is ˆrh(1) ± 1.96 × σa. For the linear model in Eq. (2.4), at+1 is also
the 1-step-ahead forecast error at the forecast origin t. In the econometric literature,
at+1 is referred to as the shock to the series at time t + 1.
In practice, estimated parameters are often used to compute point and interval
forecasts. This results in a conditional forecast because such a forecast does not
take into consideration the uncertainty in the parameter estimates. In theory, one
can consider parameter uncertainty in forecasting, but it is much more involved. A
natural way to consider parameter and model uncertainty in forecasting is Bayesian
forecasting with Markov chan Monte Carlo (MCMC) methods. See Chapter 12 for
further discussion. For simplicity, we assume that the model is given in this chapter.
When the sample size used in estimation is sufﬁciently large, then the conditional
forecast is close to the unconditional one.
2-Step-Ahead Forecast
Next consider the forecast of rh+2 at the forecast origin h. From the AR(p) model,
we have
rh+2 = φ0 + φ1rh+1 + · · · + φprh+2−p + ah+2.
Taking conditional expectation, we have
ˆrh(2) = E(rh+2|Fh) = φ0 + φ1ˆrh(1) + φ2rh + · · · + φprh+2−p
and the associated forecast error
eh(2) = rh+2 −ˆrh(2) = φ1[rh+1 −ˆrh(1)] + ah+2 = ah+2 + φ1ah+1.
The variance of the forecast error is Var[eh(2)] = (1 + φ2
1)σ 2
a . Interval forecasts
of rh+2 can be computed in the same way as those for rh+1. It is interesting to
see that Var[eh(2)] ≥Var[eh(1)], meaning that as the forecast horizon increases
the uncertainty in forecast also increases. This is in agreement with common sense
--- page 83 ---

56
linear time series analysis and its applications
that we are more uncertain about rh+2 than rh+1 at the time index h for a linear
time series.
Multistep-Ahead Forecast
In general, we have
rh+ℓ= φ0 + φ1rh+ℓ−1 + · · · + φprh+ℓ−p + ah+ℓ.
The ℓ-step-ahead forecast based on the minimum squared error loss function is the
conditional expectation of rh+ℓgiven Fh, which can be obtained as
ˆrh(ℓ) = φ0 +
p

i=1
φi ˆrh(ℓ−i),
where it is understood that ˆrh(i) = rh+i if i ≤0. This forecast can be computed
recursively using forecasts ˆrh(i) for i = 1, . . . , ℓ−1. The ℓ-step-ahead forecast
error is eh(ℓ) = rh+ℓ−ˆrh(ℓ). It can be shown that for a stationary AR(p) model,
ˆrh(ℓ) converges to E(rt) as ℓ→∞, meaning that for such a series long-term point
forecast approaches its unconditional mean. This property is referred to as the mean
reversion in the ﬁnance literature. For an AR(1) model, the speed of mean reversion
is measured by the half-life deﬁned as ℓ= ln(0.5)/ ln(|φ1|). The variance of the
forecast error then approaches the unconditional variance of rt. Note that for an
AR(1) model in (2.8), let xt = rt −E(rt) be the mean-adjusted series. It is easy to
see that the ℓ-step-ahead forecast of xh+ℓat the forecast orign h is ˆxh(ℓ) = φℓ
1xh.
The half-life is the forecast horizon such that ˆxh(ℓ) = 1
2xh. That is, φℓ
1 = 1
2. Thus,
ℓ= ln(0.5)/ ln(|φ1|).
Table 2.2 contains the 1-stepto 12-step ahead forecasts and the standard errors
of the associated forecast errors at the forecast origin 984 for the monthly simple
return of the value-weighted index using an AR(3) model that was reestimated
using the ﬁrst 984 observations. The ﬁtted model is
rt = 0.0098 + 0.1024rt−1 −0.0201rt−2 −0.1090rt−3 + at,
where ˆσa = 0.054. The actual returns of 2008 are also given in Table 2.2. Because
of the weak serial dependence in the series, the forecasts and standard deviations
of forecast errors converge to the sample mean and standard deviation of the data
quickly. For the ﬁrst 984 observations, the sample mean and standard error are
0.0095 and 0.0540, respectively.
Figure 2.7 shows the corresponding out-of-sample prediction plot for the
monthly simple return series of the value-weighted index. The forecast origin
t = 984 corresponds to December 2007. The prediction plot includes the two
standard error limits of the forecasts and the actual observed returns for 2008.
The forecasts and actual returns are marked by ◦and •, respectively. From the
plot, except for the return of October 2008, all actual returns are within the 95%
prediction intervals.
--- page 84 ---

simple ma models
57
TABLE 2.2
Multistep Ahead Forecasts of an AR(3) Model for Monthly Simple
Returns of CRSP Value-Weighted Index
Step
1
2
3
4
5
6
Forecast
0.0076
0.0161
0.0118
0.0099
0.0089
0.0093
Std. Error
0.0534
0.0537
0.0537
0.0540
0.0540
0.0540
Actual
−0.0623
−0.0220
−0.0105
0.0511
0.0238
−0.0786
Step
7
8
9
10
11
12
Forecast
0.0095
0.0097
0.0096
0.0096
0.0096
0.0096
Std. Error
0.0540
0.0540
0.0540
0.0540
0.0540
0.0540
Actual
−0.0132
0.0110
−0.0981
−0.1847
−0.0852
0.0215
aThe forecast origin is h = 984.
Time
Simple return
2007.5
2008.0
2008.5
2009.0
−0.2
−0.1
0.0
0.1
0.2
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
Figure 2.7
Plot of 1- to 12-step-ahead out-of-sample forecasts for monthly simple returns of CRSP
value-weighted index. Forecast origin is t = 984, which is December 2007. Forecasts are denoted by
“o” and actual observations by “•”. Two dashed lines denote two standard error limits of the forecasts.
2.5
SIMPLE MA MODELS
We now turn to another class of simple models that are also useful in modeling return series in ﬁnance. These models are the moving-average (MA) models.
As is shown in Chapter 5, the bid–ask bounce in stock trading may introduce
an MA(1) structure in a return series. There are several ways to introduce MA
models. One approach is to treat the model as a simple extension of white noise
series. Another approach is to treat the model as an inﬁnite-order AR model with
some parameter constraints. We adopt the second approach.
--- page 85 ---

58
linear time series analysis and its applications
There is no particular reason, but simplicity, to assume a priori that the order
of an AR model is ﬁnite. We may entertain, at least in theory, an AR model with
inﬁnite order as
rt = φ0 + φ1rt−1 + φ2rt−2 + · · · + at.
However, such an AR model is not realistic because it has inﬁnite many parameters.
One way to make the model practical is to assume that the coefﬁcients φi’s satisfy
some constraints so that they are determined by a ﬁnite number of parameters. A
special case of this idea is
rt = φ0 −θ1rt−1 −θ2
1 rt−2 −θ3
1rt−3 −· · · + at,
(2.17)
where the coefﬁcients depend on a single parameter θ1 via φi = −θi
1 for i ≥1. For
the model in Eq. (2.17) to be stationary, θ1 must be less than 1 in absolute value;
otherwise, θi
1 and the series will explode. Because |θ1| < 1, we have θi
1 →0 as
i →∞. Thus, the contribution of rt−i to rt decays exponentially as i increases.
This is reasonable as the dependence of a stationary series rt on its lagged value
rt−i, if any, should decay over time.
The model in Eq. (2.17) can be rewritten in a rather compact form. To see this,
rewrite the model as
rt + θ1rt−1 + θ2
1rt−2 + · · · = φ0 + at.
(2.18)
The model for rt−1 is then
rt−1 + θ1rt−2 + θ2
1rt−3 + · · · = φ0 + at−1.
(2.19)
Multiplying Eq. (2.19) by θ1 and subtracting the result from Eq. (2.18), we obtain
rt = φ0(1 −θ1) + at −θ1at−1,
which says that except for the constant term rt is a weighted average of shocks at
and at−1. Therefore, the model is called an MA model of order 1 or MA(1) model
for short. The general form of an MA(1) model is
rt = c0 + at −θ1at−1
or
rt = c0 + (1 −θ1B)at,
(2.20)
where c0 is a constant and {at} is a white noise series. Similarly, an MA(2) model
is in the form
rt = c0 + at −θ1at−1 −θ2at−2,
(2.21)
and an MA(q) model is
rt = c0 + at −θ1at−1 −· · · −θqat−q,
(2.22)
or rt = c0 + (1 −θ1B −· · · −θqBq)at, where q > 0.
--- page 86 ---

simple ma models
59
2.5.1
Properties of MA Models
Again, we focus on the simple MA(1) and MA(2) models. The results of MA(q)
models can easily be obtained by the same techniques.
Stationarity
Moving-average models are always weakly stationary because they are ﬁnite linear
combinations of a white noise sequence for which the ﬁrst two moments are time
invariant. For example, consider the MA(1) model in Eq. (2.20). Taking expectation
of the model, we have
E(rt) = c0,
which is time invariant. Taking the variance of Eq. (2.20), we have
Var(rt) = σ 2
a + θ2
1σ 2
a = (1 + θ2
1)σ 2
a ,
where we use the fact that at and at−1 are uncorrelated. Again, Var(rt) is time
invariant. The prior discussion applies to general MA(q) models, and we obtain
two general properties. First, the constant term of an MA model is the mean of the
series [i.e., E(rt) = c0]. Second, the variance of an MA(q) model is
Var(rt) = (1 + θ2
1 + θ2
2 + · · · + θ2
q)σ 2
a .
Autocorrelation Function
Assume for simplicity that c0 = 0 for an MA(1) model. Multiplying the model by
rt−ℓ, we have
rt−ℓrt = rt−ℓat −θ1rt−ℓat−1.
Taking expectation, we obtain
γ1 = −θ1σ 2
a
and
γℓ= 0,
for
ℓ> 1.
Using the prior result and the fact that Var(rt) = (1 + θ2
1 )σ 2
a , we have
ρ0 = 1,
ρ1 =
−θ1
1 + θ2
1
,
ρℓ= 0,
for
ℓ> 1.
Thus, for an MA(1) model, the lag-1 ACF is not zero, but all higher order ACFs
are zero. In other words, the ACF of an MA(1) model cuts off at lag 1. For the
MA(2) model in Eq. (2.21), the autocorrelation coefﬁcients are
ρ1 = −θ1 + θ1θ2
1 + θ2
1 + θ2
2
,
ρ2 =
−θ2
1 + θ2
1 + θ2
2
,
ρℓ= 0,
for
ℓ> 2.
Here the ACF cuts off at lag 2. This property generalizes to other MA models. For
an MA(q) model, the lag-q ACF is not zero, but ρℓ= 0 for ℓ> q. Consequently,
--- page 87 ---

60
linear time series analysis and its applications
an MA(q) series is only linearly related to its ﬁrst q-lagged values and hence is a
“ﬁnite-memory” model.
Invertibility
Rewriting a zero-mean MA(1) model as at = rt + θ1at−1, one can use repeated
substitutions to obtain
at = rt + θ1rt−1 + θ2
1rt−2 + θ3
1rt−3 + · · · .
This equation expresses the current shock at as a linear combination of the present
and past returns. Intuitively, θj
1 should go to zero as j increases because the remote
return rt−j should have very little impact on the current shock, if any. Consequently,
for an MA(1) model to be plausible, we require |θ1| < 1. Such an MA(1) model
is said to be invertible. If |θ1| = 1, then the MA(1) model is noninvertible. See
Section 2.6.5 for further discussion on invertibility.
2.5.2
Identifying MA Order
The ACF is useful in identifying the order of an MA model. For a time series rt
with ACF ρℓ, if ρq̸ = 0, but ρℓ= 0 for ℓ> q, then rt follows an MA(q) model.
Figure 2.8 shows the time plot of monthly simple returns of the CRSP equalweighted index from January 1926 to December 2008 and the sample ACF of the
series. The two dashed lines shown on the ACF plot denote the two standard error
Year
Simple return
1940
1960
1980
2000
−0.2
0.2 0.4 0.6
Lag
ACF
0
5
10
15
20
25
30
0.0
0.4
0.8
Figure 2.8
Time plot and sample autocorrelation function of monthly simple returns of CRSP equalweighted index from January 1926 to December 2008.
--- page 88 ---

simple ma models
61
limits. It is seen that the series has signiﬁcant ACF at lags 1, 3, and 9. There are
some marginally signiﬁcant ACF at higher lags, but we do not consider them here.
Based on the sample ACF, the following MA(9) model
rt = c0 + at −θ1at−1 −θ3at−3 −θ9at−9
is identiﬁed for the series. Note that, unlike the sample PACF, sample ACF provides
information on the nonzero MA lags of the model.
2.5.3
Estimation
Maximum-likelihood estimation is commonly used to estimate MA models. There
are two approaches for evaluating the likelihood function of an MA model. The
ﬁrst approach assumes that the initial shocks (i.e., at for t ≤0) are zero. As such,
the shocks needed in likelihood function calculation are obtained recursively from
the model, starting with a1 = r1 −c0 and a2 = r2 −c0 + θ1a1. This approach is
referred to as the conditional-likelihood method and the resulting estimates the
conditional maximum-likelihood estimates. The second approach treats the initial
shocks at, t ≤0, as additional parameters of the model and estimate them jointly
with other parameters. This approach is referred to as the exact-likelihood method.
The exact-likelihood estimates are preferred over the conditional ones, especially
when the MA model is close to being noninvertible. The exact method, however,
requires more intensive computation. If the sample size is large, then the two types
of maximum-likelihood estimates are close to each other. For details of conditionaland exact-likelihood estimates of MA models, readers are referred to Box, Jenkins,
and Reinsel (1994) or Chapter 8.
For illustration, consider the monthly simple return series of the CRSP equalweighted index and the speciﬁed MA(9) model. The conditional maximumlikelihood method produces the ﬁtted model
rt = 0.012 + at + 0.189at−1 −0.121at−3 + 0.122at−9,
ˆσa = 0.0714,
(2.23)
where standard errors of the coefﬁcient estimates are 0.003, 0.031, 0.031, and
0.031, respectively. The Ljung–Box statistics of the residuals give Q(12) = 17.5
with a p value 0.041, which is based on an asymptotic chi-squared distribution
with 9 degrees of freedom. The model needs some reﬁnements in modeling the
linear dynamic dependence of the data. The p value would be 0.132 if 12 degrees
of freedom are used. The exact maximum-likelihood method produces the ﬁtted
model
rt = 0.012 + at + 0.191at−1 −0.120at−3 + 0.123at−9,
ˆσa = 0.0714, (2.24)
where standard errors of the estimates are 0.003, 0.031, 0.031, and 0.031, respectively. The Ljung–Box statistics of the residuals give Q(12) = 17.6. The corresponding p values are 0.040 and 0.128, respectively, when the degrees of freedom
--- page 89 ---

62
linear time series analysis and its applications
are 9 and 12. Again, this ﬁtted model is only marginally adequate. Comparing
models (2.23) and (2.24), we see that for this particular instance, the difference
between the conditionaland exact-likelihood methods is negligible.
2.5.4
Forecasting Using MA Models
Forecasts of an MA model can easily be obtained. Because the model has ﬁnite
memory, its point forecasts go to the mean of the series quickly. To see this, assume
that the forecast origin is h and let Fh denote the information available at time h.
For the 1-step-ahead forecast of an MA(1) process, the model says
rh+1 = c0 + ah+1 −θ1ah.
Taking the conditional expectation, we have
ˆrh(1) = E(rh+1|Fh) = c0 −θ1ah,
eh(1) = rh+1 −ˆrh(1) = ah+1.
The variance of the 1-step-ahead forecast error is Var[eh(1)] = σ 2
a . In practice,
the quantity ah can be obtained in several ways. For instance, assume that a0 = 0,
then a1 = r1 −c0, and we can compute at for 2 ≤t ≤h recursively by using at =
rt −c0 + θ1at−1. Alternatively, it can be computed by using the AR representation
of the MA(1) model; see Section 2.6.5. Of course, at is the residual series of a
ﬁtted MA(1) model. Thus, ah is readily available from the estimation.
For the 2-step-ahead forecast from the equation
rh+2 = c0 + ah+2 −θ1ah+1,
we have
ˆrh(2) = E(rh+2|Fh) = c0,
eh(2) = rh+2 −ˆrh(2) = ah+2 −θ1ah+1.
The variance of the forecast error is Var[eh(2)] = (1 + θ2
1)σ 2
a , which is the variance
of the model and is greater than or equal to that of the 1-step-ahead forecast error.
The prior result shows that for an MA(1) model the 2-step-ahead forecast of the
series is simply the unconditional mean of the model. This is true for any forecast
origin h. More generally, ˆrh(ℓ) = c0 for ℓ≥2. In summary, for an MA(1) model,
the 1-step-ahead point forecast at the forecast origin h is c0 −θ1ah and the multistep
ahead forecasts are c0, which is the unconditional mean of the model. If we plot
the forecasts ˆrh(ℓ) versus ℓ, we see that the forecasts form a horizontal line after
one step. Thus, for MA(1) models, mean reverting only takes one time period.
Similarly, for an MA(2) model, we have
rh+ℓ= c0 + ah+ℓ−θ1ah+ℓ−1 −θ2ah+ℓ−2,
--- page 90 ---

simple ma models
63
from which we obtain
ˆrh(1) = c0 −θ1ah −θ2ah−1,
ˆrh(2) = c0 −θ2ah,
ˆrh(ℓ) = c0,
for
ℓ> 2.
Thus, the multistep-ahead forecasts of an MA(2) model go to the mean of the series
after two steps. The variances of forecast errors go to the variance of the series
after two steps. In general, for an MA(q) model, multistep-ahead forecasts go to
the mean after the ﬁrst q steps.
Table 2.3 gives some out-of-sample forecasts of an MA(9) model in the form of
Eq. (2.24) for the monthly simple returns of the equal-weighted index at the forecast
origin h = 986 (February 2008). The model parameters are reestimated using
the ﬁrst 986 observations. The sample mean and standard error of the estimation
subsample are 0.0128 and 0.0736, respectively. As expected, the table shows that
(a) the 10-step-ahead forecast is the sample mean, and (b) the standard deviations
of the forecast errors converge to the standard deviation of the series as the forecast
horizon increases. In this particular case, the point forecasts deviate substantially
from the observed returns because of the worldwide ﬁnancial crisis caused by the
subprime mortgage problem and the collapse of Lehman Brothers.
Summary
A brief summary of AR and MA models is in order. We have discussed the following properties:
• For MA models, ACF is useful in specifying the order because ACF cuts off
at lag q for an MA(q) series.
• For AR models, PACF is useful in order determination because PACF cuts
off at lag p for an AR(p) process.
• An MA series is always stationary, but for an AR series to be stationary, all
of its characteristic roots must be less than 1 in modulus.
TABLE 2.3
Out-of-Sample Forecast Performance of an MA(9) Model for Monthly
Simple Returns of CRSP Equal-Weighted Indexa
Step
1
2
3
4
5
Forecast
0.0043
0.0136
0.0150
0.0144
0.0120
Std. Error
0.0712
0.0724
0.0729
0.0729
0.0729
Actual
−0.0260
0.0312
0.0322
−0.0871
−0.0010
Step
6
7
8
9
10
Forecast
0.0019
0.0122
0.0056
0.0085
0.0128
Std. Error
0.0729
0.0729
0.0729
0.0729
0.0734
Actual
0.0141
−0.1209
−0.2060
−0.1366
0.0431
aThe forecast origin is February 2008 With h = 986. The model is estimated by the exact maximumlikelihood method.
--- page 91 ---

64
linear time series analysis and its applications
• For a stationary series, the multistep-ahead forecasts converge to the mean of
the series, and the variances of forecast errors converge to the variance of the
series as the forecast horizon increases.
2.6
SIMPLE ARMA MODELS
In some applications, the AR or MA models discussed in the previous sections
become cumbersome because one may need a high-order model with many parameters to adequately describe the dynamic structure of the data. To overcome this
difﬁculty, the autoregressive moving-average (ARMA) models are introduced; see
Box, Jenkins, and Reinsel (1994). Basically, an ARMA model combines the ideas
of AR and MA models into a compact form so that the number of parameters used
is kept small, achieving parsimony in parameterization. For the return series in
ﬁnance, the chance of using ARMA models is low. However, the concept of ARMA
models is highly relevant in volatility modeling. As a matter of fact, the generalized
autoregressive conditional heteroscedastic (GARCH) model can be regarded as an
ARMA model, albeit nonstandard, for the a2
t series; see Chapter 3 for details. In
this section, we study the simplest ARMA(1,1) model.
A time series rt follows an ARMA(1,1) model if it satisﬁes
rt −φ1rt−1 = φ0 + at −θ1at−1,
(2.25)
where {at} is a white noise series. The left-hand side of the Eq. (2.25) is the AR
component of the model and the right-hand side gives the MA component. The
constant term is φ0. For this model to be meaningful, we need φ1̸ = θ1; otherwise,
there is a cancellation in the equation and the process reduces to a white noise series.
2.6.1
Properties of ARMA(1,1) Models
Properties of ARMA(1,1) models are generalizations of those of AR(1) models
with some minor modiﬁcations to handle the impact of the MA(1) component. We
start with the stationarity condition. Taking expectation of Eq. (2.25), we have
E(rt) −φ1E(rt−1) = φ0 + E(at) −θ1E(at−1).
Because E(ai) = 0 for all i, the mean of rt is
E(rt) = µ =
φ0
1 −φ1
provided that the series is weakly stationary. This result is exactly the same as that
of the AR(1) model in Eq. (2.8).
Next, assuming for simplicity that φ0 = 0, we consider the autocovariance function of rt. First, multiplying the model by at and taking expectation, we have
E(rtat) = E(a2
t ) −θ1E(atat−1) = E(a2
t ) = σ 2
a .
(2.26)
--- page 92 ---

simple arma models
65
Rewriting the model as
rt = φ1rt−1 + at −θ1at−1
and taking the variance of the prior equation, we have
Var(rt) = φ2
1Var(rt−1) + σ 2
a + θ2
1σ 2
a −2φ1θ1E(rt−1at−1).
Here we make use of the fact that rt−1 and at are uncorrelated. Using Eq. (2.26),
we obtain
Var(rt) −φ2
1Var(rt−1) = (1 −2φ1θ1 + θ2
1)σ 2
a .
Therefore, if the series rt is weakly stationary, then Var(rt) = Var(rt−1) and we
have
Var(rt) = (1 −2φ1θ1 + θ2
1)σ 2
a
1 −φ2
1
.
Because the variance is positive, we need φ2
1 < 1 (i.e., |φ1| < 1). Again, this is
precisely the same stationarity condition as that of the AR(1) model.
To obtain the autocovariance function of rt, we assume φ0 = 0 and multiply the
model in Eq. (2.25) by rt−ℓto obtain
rtrt−ℓ−φ1rt−1rt−ℓ= atrt−ℓ−θ1at−1rt−ℓ.
For ℓ= 1, taking expectation and using Eq. (2.26) for t −1, we have
γ1 −φ1γ0 = −θ1σ 2
a ,
where γℓ= Cov(rt, rt−ℓ). This result is different from that of the AR(1) case for
which γ1 −φ1γ0 = 0. However, for ℓ= 2 and taking expectation, we have
γ2 −φ1γ1 = 0,
which is identical to that of the AR(1) case. In fact, the same technique yields
γℓ−φ1γℓ−1 = 0,
for
ℓ> 1.
(2.27)
In terms of ACF, the previous results show that for a stationary ARMA(1,1) model
ρ1 = φ1 −θ1σ 2
a
γ0
,
ρℓ= φ1ρℓ−1,
for
ℓ> 1.
--- page 93 ---

66
linear time series analysis and its applications
Thus, the ACF of an ARMA(1,1) model behaves very much like that of an AR(1)
model except that the exponential decay starts with lag 2. Consequently, the ACF
of an ARMA(1,1) model does not cut off at any ﬁnite lag.
Turning to PACF, one can show that the PACF of an ARMA(1,1) model does
not cut off at any ﬁnite lag either. It behaves very much like that of an MA(1)
model except that the exponential decay starts with lag 2 instead of lag 1.
In summary, the stationarity condition of an ARMA(1,1) model is the same as
that of an AR(1) model, and the ACF of an ARMA(1,1) exhibits a similar pattern
like that of an AR(1) model except that the pattern starts at lag 2.
2.6.2
General ARMA Models
A general ARMA(p, q) model is in the form
rt = φ0 +
p

i=1
φirt−i + at −
q

i=1
θiat−i,
where {at} is a white noise series and p and q are nonnegative integers. The AR
and MA models are special cases of the ARMA(p, q) model. Using the back-shift
operator, the model can be written as
(1 −φ1B −· · · −φpBp)rt = φ0 + (1 −θ1B −· · · −θqBq)at.
(2.28)
The polynomial 1 −φ1B −· · · −φpBp is the AR polynomial of the model. Similarly, 1 −θ1B −· · · −θqBq is the MA polynomial. We require that there are no
common factors between the AR and MA polynomials; otherwise the order (p, q)
of the model can be reduced. Like a pure AR model, the AR polynomial introduces the characteristic equation of an ARMA model. If all of the solutions of the
characteristic equation are less than 1 in absolute value, then the ARMA model is
weakly stationary. In this case, the unconditional mean of the model is E(rt) =
φ0/(1 −φ1 −· · · −φp).
2.6.3
Identifying ARMA Models
The ACF and PACF are not informative in determining the order of an ARMA
model. Tsay and Tiao (1984) propose a new approach that uses the extended autocorrelation function (EACF) to specify the order of an ARMA process. The basic
idea of EACF is relatively simple. If we can obtain a consistent estimate of the AR
component of an ARMA model, then we can derive the MA component. From the
derived MA series, we can use ACF to identify the order of the MA component.
The derivation of EACF is relatively involved; see Tsay and Tiao (1984) for
details. Yet the function is easy to use. The output of EACF is a two-way table,
where the rows correspond to AR order p and the columns to MA order q. The
theoretical version of EACF for an ARMA(1,1) model is given in Table 2.4. The
--- page 94 ---

simple arma models
67
TABLE 2.4
Theoretical EACF Table for an ARMA(1,1) Model, Where X Denotes
Nonzero, O Denotes Zero, and * Denotes Either Zero or Nonzeroa
MA
AR
0
1
2
3
4
5
6
7
0
X
X
X
X
X
X
X
X
1
X
O
O
O
O
O
O
O
2
*
X
O
O
O
O
O
O
3
*
*
X
O
O
O
O
O
4
*
*
*
X
O
O
O
O
5
*
*
*
*
X
O
O
O
aThis latter category does not play any role in identifying the order (1,1).
key feature of the table is that it contains a triangle of O with the upper left vertex
located at the order (1,1). This is the characteristic we use to identify the order of
an ARMA process. In general, for an ARMA(p, q) model, the triangle of O will
have its upper left vertex at the (p, q) position.
For illustration, consider the monthly log stock returns of the 3M Company from
February 1946 to December 2008. There are 755 observations. The return series
and its sample ACF are shown in Figure 2.9. The ACF indicates that there are
no signiﬁcant serial correlations in the data at the 1% level. Table 2.5 shows the
sample EACF and a corresponding simpliﬁed table for the series. The simpliﬁed
table is constructed by using the following notation:
1. X denotes that the absolute value of the corresponding EACF is greater than
or equal to 2/
√
T , which is twice of the asymptotic standard error of the
EACF.
2. O denotes that the corresponding EACF is less than 2/
√
T in modulus.
The simpliﬁed table exhibits a triangular pattern of O with its upper left vertex
at the order (p, q) = (0, 0). A few exceptions of X appear when q = 2, 5, 9, and
11. However, the EACF table shows that the values of sample ACF corresponding
to those X are around 0.08 or 0.09. These ACFs are only slightly greater than
2/
√
755 = 0.073. Indeed, if 1% critical value is used, those X would become O in
the simpliﬁed EACF table. Consequently, the EACF suggests that the monthly log
returns of 3M stock follow an ARMA(0,0) model (i.e., a white noise series). This
is in agreement with the result suggested by the sample ACF in Figure 2.9.
The information criteria discussed earlier can also be used to select ARMA(p, q)
models. Typically, for some prespeciﬁed positive integers P and Q, one computes
AIC (or BIC) for ARMA(p, q) models, where 0 ≤p ≤P and 0 ≤q ≤Q, and
selects the model that gives the minimum AIC (or BIC). This approach requires
maximum-likelihood estimation of many models and in some cases may encounter
the difﬁculty of overﬁtting in estimation.
--- page 95 ---

68
linear time series analysis and its applications
Year
Log return
1950
1960
1970
1980
1990
2000
2010
−0.3
−0.1
0.1
Lag
ACF
0
5
10
15
20
0.0 0.2 0.4 0.6 0.8 1.0
Figure 2.9
Time plot and sample autocorrelation function of monthly log stock returns of 3M Company
from February 1946 to December 2008.
Once an ARMA(p, q) model is speciﬁed, its parameters can be estimated by
either the conditional or exact-likelihood method. In addition, the Ljung–Box statistics of the residuals can be used to check the adequacy of a ﬁtted model. If the
model is correctly speciﬁed, then Q(m) follows asymptotically a chi-squared distribution with m −g degrees of freedom, where g denotes the number of AR or
MA coefﬁcients ﬁtted in the model.
2.6.4
Forecasting Using an ARMA Model
Like the behavior of ACF, forecasts of an ARMA(p, q) model have similar characteristics as those of an AR(p) model after adjusting for the impacts of the MA
component on the lower horizon forecasts. Denote the forecast origin by h and
the available information by Fh. The 1-step-ahead forecast of rh+1 can be easily
obtained from the model as
ˆrh(1) = E(rh+1|Fh) = φ0 +
p

i=1
φirh+1−i −
q

i=1
θiah+1−i,
and the associated forecast error is eh(1) = rh+1 −ˆrh(1) = ah+1. The variance of
1-step-ahead forecast error is Var[eh(1)] = σ 2
a . For the ℓ-step-ahead forecast, we
have
ˆrh(ℓ) = E(rh+ℓ|Fh) = φ0 +
p

i=1
φi ˆrh(ℓ−i) −
q

i=1
θiah(ℓ−i),
--- page 96 ---

simple arma models
69
TABLE 2.5
Sample Extended Autocorrelation Function and a Simpliﬁed Table for
the Monthly Log Returns of 3M Stock from February 1946 to December 2008
Sample Extended Autocorrelation Function
MA Order: q
p
0
1
2
3
4
5
6
7
8
9
10
11
12
0 −0.06 −0.04 −0.08 −0.00
0.02
0.08
0.01
0.01 −0.03 −0.08
0.05
0.09 −0.01
1 −0.47
0.01 −0.07 −0.02
0.00
0.08 −0.03
0.00 −0.01 −0.07
0.04
0.09 −0.02
2 −0.38 −0.35 −0.07
0.02 −0.01
0.08
0.03
0.01
0.00 −0.03
0.02
0.04
0.04
3 −0.18
0.14
0.38 −0.02
0.00
0.04 −0.02
0.02 −0.00 −0.03
0.02
0.01
0.04
4
0.42
0.03
0.45 −0.01
0.00
0.00 −0.01
0.03
0.01
0.00
0.02 −0.00
0.01
5 −0.11
0.21
0.45
0.01
0.20 −0.01 −0.00
0.04 −0.01 −0.01
0.03
0.01
0.03
6 −0.21 −0.25
0.24
0.31
0.17 −0.04 −0.00
0.04 −0.01 −0.03
0.01
0.01
0.04
Simpliﬁed EACF Table
MA Order: q
p
0
1
2
3
4
5
6
7
8
9
10
11
12
0
O
O
X
O
O
X
O
O
O
X
O
X
O
1
X
O
O
O
O
X
O
O
O
O
O
X
O
2
X
X
O
O
O
X
O
O
O
O
O
O
O
3
X
X
X
O
O
O
O
O
O
O
O
O
O
4
X
O
X
O
O
O
O
O
O
O
O
O
O
5
X
X
X
O
X
O
O
O
O
O
O
O
O
6
X
X
X
X
X
O
O
O
O
O
O
O
O
where it is understood that ˆrh(ℓ−i) = rh+ℓ−i if ℓ−i ≤0 and ah(ℓ−i) = 0 if
ℓ−i > 0 and ah(ℓ−i) = ah+ℓ−i if ℓ−i ≤0. Thus, the multistep-ahead forecasts
of an ARMA model can be computed recursively. The associated forecast error is
eh(ℓ) = rh+ℓ−ˆrh(ℓ),
which can be computed easily via a formula to be given in Eq. (2.34).
2.6.5
Three Model Representations for an ARMA Model
In this section, we brieﬂy discuss three model representations for a stationary
ARMA(p, q) model. The three representations serve three different purposes.
Knowing these representations can lead to a better understanding of the model. The
ﬁrst representation is the ARMA(p, q) model in Eq. (2.28). This representation
is compact and useful in parameter estimation. It is also useful in computing
recursively multistep-ahead forecasts of rt; see the discussion in the last section.
