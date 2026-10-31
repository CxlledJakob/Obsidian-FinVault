# Analysis of Financial Time Series, Third Edition (Wiley -- Ruey S_ Tsay -- Wiley series in probability and statistics, 3rd ed_, -- John Wiley & Sons, -- isbn13 9780470414354 -- 9f99b80c7b2dedd477f463dc5323f3b6 -- An.pdf — pages 153–172

--- page 153 ---

126
conditional heteroscedastic models
Lag
(b)
ACF
0
10
15
20
25
0.0
0.4
0.8
Year
Stres
1980
1990
2000
2010
−4
−2
0
2
4
5
Lag
(a)
ACF
0
10
15
20
25
0.0
0.4
0.8
5
Lag
(c)
(d)
ACF
0
10
15
20
25
0.0
0.4
0.8
5
Figure 3.5
Model checking statistics of Gaussian ARCH(1) model in Eq. (3.12) for monthly log
returns of Intel stock from January 1973 to December 2008: Parts (a), (b), and (c) show sample ACF
of standardized residuals, their squared series, and absolute series, respectively; part (d) is time plot of
standardized residuals.
where the standard errors of the parameters are 0.0053, 0.0017, and 0.1120, respectively. The estimated degrees of freedom is 6.01 with standard error 1.50. All the
estimates are signiﬁcant at the 5% level. The unconditional standard deviation
of at is √0.0120/(1 −0.2845) ≈0.1295, which is close to that obtained under
normality. The Ljung–Box statistics of the standardized residuals give Q(12) =
14.88 with a p value of 0.25, conﬁrming that the mean equation is adequate.
However, the Ljung–Box statistics for the squared standardized residuals show
Q(12) = 35.42 with a p value of 0.0004. The volatility equation is inadequate
at the 1% level. Further analysis shows that Q(10) = 15.90 with a p value
of 0.10 for the squared standardized residuals. The inadequancy of the volatility
equation is due to a large lag-12 ACF (ρ12 = 0.188) of the squared standardized
residuals.
Comparing models (3.12) and (3.13), we see that (a) using a heavy-tailed distribution for ϵt reduces the ARCH coefﬁcient, and (b) the difference between the two
models is small for this particular instance. Finally, a more appropriate conditional
heteroscedastic model for the monthly log returns of Intel stock is a GARCH(1,1)
model, which is discussed in the next section.
--- page 154 ---

the arch model
127
S-Plus Demonstration
Note the following output with t innovations:
> arch1t=garch(intc∼1,∼garch(1,0),cond.dist="t")
> summary(arch1t)
Call:
garch(formula.mean=intc∼1,formula.var=∼garch(1,0),
cond.dist="t")
Mean Equation: structure(.Data = intc ∼1, class = "formula")
Cond. Variance Equation:structure(.Data=∼garch(1,0), ...)
Cond. Distribution:
t
with estimated parameter 6.012769 and standard error 1.502179
--------------------------------------------------------------
Estimated Coefficients:
--------------------------------------------------------------
Value Std.Error t value
Pr(>|t|)
C 0.01688
0.005288
3.193 1.512e-03
A 0.01195
0.001667
7.169 3.345e-12
ARCH(1) 0.28445
0.111998
2.540 1.145e-02
--------------------------------------------------------------
AIC(4) = -597.3379, BIC(4) = -581.0642
Ljung-Box test for standardized residuals:
--------------------------------------------------------------
Statistic P-value Chi^2-d.f.
14.88
0.2482
12
Ljung-Box test for squared standardized residuals:
--------------------------------------------------------------
Statistic
P-value Chi^2-d.f.
35.42 0.0004014
12
Remark.
In S-Plus, the command garch allows for several conditional distributions. They are speciﬁed by cond.dist = ‘‘t’’ or ‘‘ged’’. The default
is Gaussian. The R output is given below. The estimates are close to those of
S-Plus.
□
R Demonstration
The following output uses the fGarch package with command garchFit and %
denotes explanation:
> da=read.table("m-intc7308.txt",header=T)
> library(fGarch)
% Load the package
> intc=log(da[,2]+1)
> m1=garchFit(intc∼garch(1,0),data=intc,trace=F)
> summary(m1)
% Obtain results
--- page 155 ---

128
conditional heteroscedastic models
Title:
GARCH Modelling
Call:
garchFit(formula=intc∼garch(1,0), data=intc, trace=F)
Mean and Variance Equation: data ∼garch(1, 0) [data = intc]
Conditional Distribution: norm
Coefficient(s):
mu
omega
alpha1
0.012637
0.011195
0.379492
Std. Errors:
based on Hessian
Error Analysis:
Estimate
Std. Error
t value Pr(>|t|)
mu
0.012637
0.005428
2.328
0.01990 *
omega
0.011195
0.001239
9.034
< 2e-16 ***
alpha1
0.379492
0.115534
3.285
0.00102 **
---
Log Likelihood:
288.0589
normalized:
0.6668031
Standardised Residuals Tests:
%Model checking
Statistic p-Value
Jarque-Bera Test
R
Chi^2
137.919
0
Shapiro-Wilk Test
R
W
0.9679255 4.025172e-08
Ljung-Box Test
R
Q(10)
12.54002
0.2505382
Ljung-Box Test
R
Q(15)
21.33508
0.1264607
Ljung-Box Test
R
Q(20)
23.19679
0.2792354
Ljung-Box Test
R^2
Q(10)
16.0159
0.09917815
Ljung-Box Test
R^2
Q(15)
36.08022
0.001721296
Ljung-Box Test
R^2
Q(20)
37.43683
0.01036728
LM Arch Test
R
TR^2
26.57744
0.008884587
Information Criterion Statistics:
AIC
BIC
SIC
HQIC
-1.319717 -1.291464 -1.319813 -1.308563
> predict(m1,5)
% Obtain 1 to 5-step predictions
meanForecast meanError standardDeviation
1
0.01263656 0.1278609
0.1098306
2
0.01263656 0.1278609
0.1255897
3
0.01263656 0.1278609
0.1310751
4
0.01263656 0.1278609
0.1330976
5
0.01263656 0.1278609
0.1338571
--- page 156 ---

the arch model
129
% The next command fits a GARCH(1,1) model
> m2=garchFit(intc∼garch(1,1),data=intc,trace=F)
> summary(m2) % output edited.
Coefficient(s):
mu
omega
alpha1
beta1
0.01073352
0.00095445
0.08741989
0.85118414
Error Analysis:
Estimate
Std. Error
t value Pr(>|t|)
mu
0.0107335
0.0055289
1.941
0.05222 .
omega
0.0009544
0.0003989
2.392
0.01674 *
alpha1 0.0874199
0.0269810
3.240
0.00120 **
beta1
0.8511841
0.0393702
21.620
< 2e-16 ***
---
Standardised Residuals Tests:
Statistic p-Value
Jarque-Bera Test
R
Chi^2
165.5740
0
Shapiro-Wilk Test
R
W
0.9712087 1.626824e-07
Ljung-Box Test
R
Q(10)
8.267633
0.6027128
Ljung-Box Test
R
Q(15)
14.42612
0.4934871
Ljung-Box Test
R
Q(20)
15.13331
0.7687297
Ljung-Box Test
R^2
Q(10)
0.9891848 0.9998363
Ljung-Box Test
R^2
Q(15)
11.36596
0.7262473
Ljung-Box Test
R^2
Q(20)
12.68143
0.8906302
LM Arch Test
R
TR^2
10.70199
0.5546164
% The next command fits an ARCH(1) model with Student-t dist.
> m3=garchFit(intc∼garch(1,0),data=intc,trace=F,
cond.dist=’std’)
> summary(m3) % Output shortened.
Call:
garchFit(formula=intc∼garch(1,0), data=intc, cond.dist="std",
trace = F)
Mean and Variance Equation: data ∼garch(1, 0) [data = intc]
Conditional Distribution:
std
% Student-t distribution
Coefficient(s):
mu
omega
alpha1
shape
0.016731
0.011939
0.285320
6.015195
Error Analysis:
Estimate
Std. Error
t value Pr(>|t|)
mu
0.016731
0.005302
3.155 0.001603 **
omega
0.011939
0.001603
7.449
9.4e-14 ***
alpha1
0.285320
0.110607
2.580 0.009892 **
shape
6.015195
1.562620
3.849 0.000118 ***
% Degrees of freedom
--- page 157 ---

130
conditional heteroscedastic models
% The next command fits an ARCH(1) model with skew
%Student-t dist.
> m4=garchFit(intc∼garch(1,0),data=intc,cond.dist=’sstd’,
trace=F)
% Next, fit an ARMA(1,0)+GARCH(1,1) model with
% Gaussian noises.
> m5=garchFit(intc∼arma(1,0)+garch(1,1),data=intc,trace=F)
R Demonstration
The following output was generated with Ox and G@RCH4.2 package and %
denotes explanation:
> source("garchoxfit_R.txt")
% In G@RCH package, an ARCH(1) model is specified as
% GARCH(0,1).
> m1=garchOxFit(formula.mean=∼arma(0,0),
formula.var=∼garch(0,1), series=intc)
% ** SPECIFICATIONS **
Dependent variable : X
Mean Equation : ARMA (0, 0) model.
No regressor in the mean
Variance Equation : GARCH (0, 1) model.
No regressor in the variance
The distribution is a Gauss distribution.
Maximum Likelihood Estimation(Std.Errors based on 2nd deriv.)
Coefficient
Std.Error
t-value
t-prob
Cst(M)
0.012630
0.0054130
2.333
0.0201
Cst(V)
0.011129
0.0012355
9.007
0.0000
ARCH(Alpha1)
0.387223
0.11688
3.313
0.0010
% ** TESTS **
Q-Statistics on Standardized Residuals
Q(10)=12.4952 [0.2532785],
Q(20)=23.1210 [0.2828934]
H0: No serial correlation ==> Accept H0 when prob. is High.
------------
Q-Statistics on Squared Standardized Residuals
--> P-values adjusted by 1 degree(s) of freedom
Q(10)=15.7849 [0.0715122], Q( 20)=37.0238 [0.0078807]
------------
ARCH 1-10 test:
F(10,410)=
1.4423 [0.1592]
------------
% Apply Student-t distribution
> m2=garchOxFit(formula.mean=∼arma(0,0),
formula.var=∼garch(0,1),
series=intc,cond.dist="t")
% ** SPECIFICATIONS **
--- page 158 ---

the garch model
131
Dependent variable : X
Mean Equation : ARMA (0, 0) model.
No regressor in the mean
Variance Equation : GARCH (0, 1) model.
No regressor in the variance
The distribution is a Student distribution, with 6.02272 df.
Maximum Likelihood Estimation(Std.Errors based on 2nd deriv.)
Coefficient
Std.Error
t-value
t-prob
Cst(M)
0.016702
0.0052934
3.155
0.0017
Cst(V)
0.011870
0.0015969
7.433
0.0000
ARCH(Alpha1)
0.292318
0.11223
2.605
0.0095
Student(DF)
6.022723
1.5663
3.845
0.0001
** TESTS **
Q-Statistics on Standardized Residuals
Q(10)=13.0837 [0.2190281],
Q(20)=24.0724 [0.2392436]
------------
Q-Statistics on Squared Standardized Residuals
--> P-values adjusted by 1 degree(s) of freedom
Q(10)=18.6982 [0.0278845], Q( 20)=41.7182 [0.0019343]
Example 3.2.
Consider the percentage changes of the exchange rate between
mark and dollar in 10-minute intervals. The data are shown in Figure 3.3(a). As
shown in Figure 3.4(a), the series has no serial correlations. However, the sample
PACF of the squared series a2
t shows some big spikes, especially at lags 1 and 3.
There are some large PACF at higher lags, but the lower order lags tend to be more
important. Following the procedure discussed in the previous section, we specify an
ARCH(3) model for the series. Using the conditional Gaussian likelihood function,
we obtain the ﬁtted model rt = 0.0018 + σtϵt and
σ 2
t = 0.22 × 10−2 + 0.322a2
t−1 + 0.074a2
t−2 + 0.093a2
t−3,
where all the estimates in the volatility equation are statistically signiﬁcant at the 5%
signiﬁcant level, and the standard errors of the parameters are 0.47 × 10−6, 0.017,
0.016, and 0.014, respectively. Model checking, using the standardized residual ˜at,
indicates that the model is adequate.
3.5
THE GARCH MODEL
Although the ARCH model is simple, it often requires many parameters to adequately describe the volatility process of an asset return. For instance, consider the
monthly excess returns of S&P 500 index of Example 3.3. An ARCH(9) model is
needed for the volatility process. Some alternative model must be sought. Bollerslev (1986) proposes a useful extension known as the generalized ARCH (GARCH)
model. For a log return series rt, let at = rt −µt be the innovation at time t. Then
--- page 159 ---

132
conditional heteroscedastic models
at follows a GARCH(m, s) model if
at = σtϵt,
σ 2
t = α0 +
m

i=1
αia2
t−i +
s

j=1
βjσ 2
t−j,
(3.14)
where again {ϵt} is a sequence of iid random variables with mean 0 and variance
1.0, α0 > 0, αi ≥0, βj ≥0, and max(m,s)
i=1
(αi + βi) < 1. Here it is understood that
αi = 0 for i > m and βj = 0 for j > s. The latter constraint on αi + βi implies
that the unconditional variance of at is ﬁnite, whereas its conditional variance σ 2
t
evolves over time. As before, ϵt is often assumed to follow a standard normal
or standardized Student-t distribution or generalized error distribution. Equation
(3.14) reduces to a pure ARCH(m) model if s = 0. The αi and βj are referred to
as ARCH and GARCH parameters, respectively.
To understand properties of GARCH models, it is informative to use the following representation. Let ηt = a2
t −σ 2
t so that σ 2
t = a2
t −ηt. By plugging σ 2
t−i =
a2
t−i −ηt−i (i = 0, . . . , s) into Eq. (3.14), we can rewrite the GARCH model as
a2
t = α0 +
max(m,s)

i=1
(αi + βi)a2
t−i + ηt −
s

j=1
βjηt−j.
(3.15)
It is easy to check that {ηt} is a martingale difference series [i.e., E(ηt) = 0 and
cov(ηt, ηt−j) = 0 for j ≥1]. However, {ηt} in general is not an iid sequence.
Equation (3.15) is an ARMA form for the squared series a2
t . Thus, a GARCH
model can be regarded as an application of the ARMA idea to the squared series
a2
t . Using the unconditional mean of an ARMA model, we have
E(a2
t ) =
α0
1 −max(m,s)
i=1
(αi + βi)
provided that the denominator of the prior fraction is positive.
The strengths and weaknesses of GARCH models can easily be seen by focusing
on the simplest GARCH(1,1) model with
σ 2
t = α0 + α1a2
t−1 + β1σ 2
t−1,
0 ≤α1, β1 ≤1, (α1 + β1) < 1.
(3.16)
First, a large a2
t−1 or σ 2
t−1 gives rise to a large σ 2
t . This means that a large a2
t−1 tends
to be followed by another large a2
t , generating, again, the well-known behavior
of volatility clustering in ﬁnancial time series. Second, it can be shown that if
1 −2α2
1 −(α1 + β1)2 > 0, then
E(a4
t )
[E(a2
t )]2 =
3[1 −(α1 + β1)2]
1 −(α1 + β1)2 −2α2
1
> 3.
--- page 160 ---

the garch model
133
Consequently, similar to ARCH models, the tail distribution of a GARCH(1,1)
process is heavier than that of a normal distribution. Third, the model provides a
simple parametric function that can be used to describe the volatility evolution.
Forecasts of a GARCH model can be obtained using methods similar to those
of an ARMA model. Consider the GARCH(1,1) model in Eq. (3.16) and assume
that the forecast origin is h. For 1-step-ahead forecast, we have
σ 2
h+1 = α0 + α1a2
h + β1σ 2
h,
where ah and σ 2
h are known at the time index h. Therefore, the 1-step-ahead forecast
is
σ 2
h(1) = α0 + α1a2
h + β1σ 2
h.
For multistep-ahead forecasts, we use a2
t = σ 2
t ϵ2
t and rewrite the volatility equation
in Eq. (3.16) as
σ 2
t+1 = α0 + (α1 + β1)σ 2
t + α1σ 2
t (ϵ2
t −1).
When t = h + 1, the equation becomes
σ 2
h+2 = α0 + (α1 + β1)σ 2
h+1 + α1σ 2
h+1(ϵ2
h+1 −1).
Since E(ϵ2
h+1 −1|Fh) = 0, the 2-step-ahead volatility forecast at the forecast origin
h satisﬁes the equation
σ 2
h(2) = α0 + (α1 + β1)σ 2
h(1).
In general, we have
σ 2
h(ℓ) = α0 + (α1 + β1)σ 2
h(ℓ−1),
ℓ> 1.
(3.17)
This result is exactly the same as that of an ARMA(1,1) model with AR polynomial
1 −(α1 + β1)B. By repeated substitutions in Eq. (3.17), we obtain that the ℓ-stepahead forecast can be written as
σ 2
h(ℓ) = α0[1 −(α1 + β1)ℓ−1]
1 −α1 −β1
+ (α1 + β1)ℓ−1σ 2
h(1).
Therefore,
σ 2
h(ℓ) →
α0
1 −α1 −β1
,
as
ℓ→∞
provided that α1 + β1 < 1. Consequently, the multistep-ahead volatility forecasts of
a GARCH(1,1) model converge to the unconditional variance of at as the forecast
horizon increases to inﬁnity provided that Var(at) exists.
--- page 161 ---

134
conditional heteroscedastic models
The literature on GARCH models is enormous; see Bollerslev, Chou, and Kroner
(1992), Bollerslev, Engle, and Nelson (1994), and the references therein. The model
encounters the same weaknesses as the ARCH model. For instance, it responds
equally to positive and negative shocks. In addition, recent empirical studies of
high-frequency ﬁnancial time series indicate that the tail behavior of GARCH
models remains too short even with standardized Student-t innovations. For further
information about kurtosis of GARCH models, see Section 3.16.
3.5.1
An Illustrative Example
The modeling procedure of ARCH models can also be used to build a GARCH
model. However, specifying the order of a GARCH model is not easy. Only
lower order GARCH models are used in most applications, say, GARCH(1,1),
GARCH(2,1), and GARCH(1,2) models. The conditional maximum-likelihood
method continues to apply provided that the starting values of the volatility {σ 2
t }
are assumed to be known. Consider, for instance, a GARCH(1,1) model. If σ 2
1 is
treated as ﬁxed, then σ 2
t can be computed recursively for a GARCH(1,1) model.
In some applications, the sample variance of at serves as a good starting value
of σ 2
1 . The ﬁtted model can be checked by using the standardized residual ˜at =
at/σt and its squared process.
Example 3.3.
In this example, we consider the monthly excess returns of
S&P 500 index starting from 1926 for 792 observations. The series is shown in
Figure 3.6. Denote the excess return series by rt. Figure 3.7 shows the sample ACF
Time index
Return
0
200
400
600
800
−0.2
0.0
0.2
0.4
Figure 3.6
Time series plot of monthly excess returns of S&P 500 index from 1926 to 1991.
--- page 162 ---

the garch model
135
Lag
(a)
(b)
ACF
0
5
10
15
20
25
30
Lag
0
5
10
15
20
25
30
−0.10
0.0 0.05
Partial ACF
−0.1 0.0 0.1 0.2 0.3
Figure 3.7
(a) Sample ACF of monthly excess returns of S&P 500 index and (b) sample PACF of
squared monthly excess returns. Sample period is from 1926 to 1991.
of rt and the sample PACF of r2
t . The rt series has some serial correlations at lags
1 and 3, but the key feature is that the PACF of r2
t shows strong linear dependence.
If an MA(3) model is entertained, we obtain
rt = 0.0062 + at + 0.0944at−1 −0.1407at−3,
ˆσa = 0.0576
for the series, where all of the coefﬁcients are signiﬁcant at the 5% level. However,
for simplicity, we use instead an AR(3) model
rt = φ1rt−1 + φ2rt−2 + φ3rt−3 + β0 + at.
The ﬁtted AR(3) model, under the normality assumption, is
rt = 0.088rt−1 −0.023rt−2 −0.123rt−3 + 0.0066 + at,
ˆσ 2
a = 0.00333. (3.18)
For the GARCH effects, we use the GARCH(1,1) model
at = σtϵt,
σ 2
t = α0 + β1σ 2
t−1 + α1a2
t−1.
A joint estimation of the AR(3)–GARCH(1,1) model gives
--- page 163 ---

136
conditional heteroscedastic models
rt = 0.0078 + 0.032rt−1 −0.029rt−2 −0.008rt−3 + at,
σ 2
t = 0.000084 + 0.1213a2
t−1 + 0.8523σ 2
t−1.
From the volatility equation, the implied unconditional variance of at is
0.000084
1 −0.8523 −0.1213 = 0.00317,
which is close to that of Eq. (3.18). However, t ratios of the parameters in the
mean equation suggest that all three AR coefﬁcients are insigniﬁcant at the 5%
level. Therefore, we reﬁne the model by dropping all AR parameters. The reﬁned
model is
rt = 0.0076 + at,
σ 2
t = 0.000086 + 0.1216a2
t−1 + 0.8511σ 2
t−1.
(3.19)
The standard error of the constant in the mean equation is 0.0015, whereas those
of the parameters in the volatility equation are 0.000024, 0.0197, and 0.0190,
respectively. The unconditional variance of at is 0.000086/(1 −0.8511 −0.1216)
= 0.00314. This is a simple stationary GARCH(1,1) model. Figure 3.8 shows the
estimated volatility process, σt, and the standardized shocks ˜at = at/σt for the
Year
(a)
(b)
σt
1940
1960
1980
0.05 0.10 0.15 0.20
Standard residual
−4
−2
0
2
Year
1940
1960
1980
Figure 3.8
(a) Time series plot of estimated volatility (σt) for monthly excess returns of S&P 500
index and (b) standardized shocks of monthly excess returns of S&P 500 index. Both plots are based
on GARCH(1,1) model in Eq. (3.19).
--- page 164 ---

the garch model
137
Lag
(a)
ACF
5
10
15
20
−0.2 −0.1 0.0
0.1
0.2
Lag
(b)
ACF
5
10
15
20
−0.2 −0.1 0.0
0.1
0.2
Figure 3.9
Model checking of GARCH(1,1) model in Eq. (3.19) for monthly excess returns of S&P
500 index: (a) Sample ACF of standardized residuals and (b) sample ACF of the squared standardized
residuals.
GARCH(1,1) model in Eq. (3.19). The ˜at series looks like a white noise process. Figure 3.9 provides the sample ACF of the standardized residuals ˜at and the
squared process ˜a2
t . These ACFs fail to suggest any signiﬁcant serial correlations
or conditional heteroscedasticity in the standardized residual series. More speciﬁ-
cally, we have Q(12) = 11.99(0.45) and Q(24) = 28.52(0.24) for ˜at, and Q(12)
= 13.11(0.36) and Q(24) = 26.45(0.33) for ˜a2
t , where the number in parentheses is the p value of the test statistic. Thus, the model appears to be adequate in
describing the linear dependence in the return and volatility series. Note that the
ﬁtted model shows ˆα1 + ˆβ1 = 0.9772, which is close to 1. This phenomenon is
commonly observed in practice and it leads to imposing the constraint α1 + β1 = 1
in a GARCH(1,1) model, resulting in an integrated GARCH (or IGARCH) model;
see Section 3.6.
Finally, to forecast the volatility of monthly excess returns of the S&P 500 index,
we can use the volatility equation in Eq. (3.19). For instance, at the forecast origin
h, we have σ 2
h+1 = 0.000086 + 0.1216a2
h + 0.8511σ 2
h. The 1-step-ahead forecast is
then
σ 2
h(1) = 0.000086 + 0.1216a2
h + 0.8511σ 2
h,
--- page 165 ---

138
conditional heteroscedastic models
TABLE 3.1
Volatility Forecasts for Monthly Excess Returns of S&P 500 Indexa
Horizon
1
2
3
4
5
∞
Return
0.0076
0.0076
0.0076
0.0076
0.0076
0.0076
Volatility
0.0536
0.0537
0.0537
0.0538
0.0538
0.0560
aThe forecast origin is h = 792, which corresponds to December 1991. Here volatility denotes conditional standard deviation.
where ah is the residual of the mean equation at time h and σh is obtained from the
volatility equation. The starting value σ 2
0 is ﬁxed at either zero or the unconditional
variance of at. For multistep-ahead forecasts, we use the recursive formula in Eq.
(3.17). Table 3.1 shows some mean and volatility forecasts for the monthly excess
return of the S&P 500 index with forecast origin h = 792 based on the GARCH(1,1)
model in Eq. (3.19).
Some S-Plus Commands Used in Example 3.3.
> fit=garch(sp∼ar(3),∼garch(1,1))
> summary(fit)
> fit=garch(sp∼1,∼garch(1,1))
> summary(fit)
> names(fit)
[1] "residuals" "sigma.t"
"df.residual" "coef" "model"
[6] "cond.dist" "likelihood" "opt.index"
"cov"
"prediction"
[11] "call"
"asymp.sd"
"series"
>
> stdresi=fit$residuals/fit$sigma.t
> autocorTest(stdresi,lag=24)
> autocorTest(stdresi^2,lag=24)
> predict(fit,5)
Note that in the prior commands the volatility series σt is stored in fit$sigma.t
and the residual series of the returns in fit$residuals.
t Innovation
Assuming that ϵt follows a standardized Student-t distribution with 5 degrees of
freedom, we reestimate the GARCH(1,1) model and obtain
rt = 0.0085 + at,
σ 2
t = 0.00012 + 0.1121a2
t−1 + 0.8432σ 2
t−1,
(3.20)
where the standard errors of the parameters are 0.0015, 0.51×10−4, 0.0296, and
0.0371, respectively. This model is essentially an IGARCH(1,1) model as ˆα1 + ˆβ1
≈0.95, which is close to 1. The Ljung–Box statistics of the standardized residuals
give Q(10) = 11.38 with a p value of 0.33 and those of the {˜a2
t } series give Q(10)
= 10.48 with a p value of 0.40. Thus, the ﬁtted GARCH(1,1) model with Student-t
distribution is adequate.
--- page 166 ---

the garch model
139
S-Plus Commands Used
> fit1 = garch(sp∼1,∼garch(1,1),cond.dist=’t’,cond.par=5,
+ cond.est=F)
> summary(fit1)
> stresi=fit1$residuals/fit1$sigma.t
> autocorTest(stresi,lag=10)
> autocorTest(stresi^2,lag=10)
Estimation of Degrees of Freedom
If we further extend the GARCH(1,1) model by estimating the degrees of freedom
of the Student-t distribution used, we obtain the model
rt = 0.0085 + at,
σ 2
t = 0.00012 + 0.1121a2
t−1 + 0.8432σ 2
t−1,
(3.21)
where the estimated degrees of freedom is 7.02. Standard errors of the estimates
in Eq. (3.21) are close to those in Eq. (3.20). The standard error of the estimated
degrees of freedom is 1.78. Consequently, we cannot reject the hypothesis of using a
standardized Student-t distribution with 5 degrees of freedom at the 5% signiﬁcance
level.
S-Plus Commands Used
> fit2 = garch(sp∼1,∼garch(1,1),cond.dist=’t’)
> summary(fit2)
R Commands Used in Example 3.3
> library(fGarch)
> sp5=scan(file=’sp500.txt’) % Load data
> plot(sp5,type=’l’)
% Below, fit an AR(3)+GARCH(1,1) model.
> m1=garchFit(∼arma(3,0)+garch(1,1),data=sp5,trace=F)
> summary(m1)
% Below, fit a GARCH(1,1) model with Student-t distribution.
> m2=garchFit(∼garch(1,1),data=sp5,trace=F,cond.dist="std")
> summary(m2)
% Obtain standardized residuals.
> stresi=residuals(m2,standardize=T)
> plot(stresi,type=’l’)
> Box.test(stresi,10,type=’Ljung’)
> predict(m2,5)
3.5.2
Forecasting Evaluation
Since the volatility of an asset return is not directly observable, comparing the
forecasting performance of different volatility models is a challenge to data analysts.
In the literature, some researchers use out-of-sample forecasts and compare the
--- page 167 ---

140
conditional heteroscedastic models
volatility forecasts σ 2
h(ℓ) with the shock a2
h+ℓin the forecasting sample to assess
the forecasting performance of a volatility model. This approach often ﬁnds a
low correlation coefﬁcient between a2
h+ℓand σ 2
h(ℓ), that is, low R2. However,
such a ﬁnding is not surprising because a2
h+ℓalone is not an adequate measure
of the volatility at time index h + ℓ. Consider the 1-step-ahead forecasts. From a
statistical point of view, E(a2
h+1|Fh) = σ 2
h+1 so that a2
h+1 is a consistent estimate
of σ 2
h+1. But it is not an accurate estimate of σ 2
h+1 because a single observation of a
random variable with a known mean value cannot provide an accurate estimate of
its variance. Consequently, such an approach to evaluate forecasting performance of
volatility models is strictly speaking not proper. For more information concerning
forecasting evaluation of GARCH models, readers are referred to Andersen and
Bollerslev (1998).
3.5.3
A Two-Pass Estimation Method
Based on Eq. (3.15), a two-pass estimation method can be used to estimate GARCH
models. First, ignoring any ARCH effects, one estimates the mean equation of a
return series using the methods discussed in Chapter 2 (e.g., maximum-likelihood
method). Denote the residual series by at. Second, treating {a2
t } as an observed
time series, one applies the maximum-likelihood method to estimate parameters
of Eq. (3.15). Denote the AR and MA coefﬁcient estimates by ˆφi and ˆθi. The
GARCH estimates are obtained as ˆβi = ˆθi and ˆαi = ˆφi −ˆθi. Obviously, such estimates are approximations to the true parameters and their statistical properties have
not been rigorously investigated. However, limited experience shows that this simple approach often provides good approximations, especially when the sample size
is moderate or large. For instance, consider the monthly excess return series of the
S&P 500 index of Example 3.3. Using the conditional MLE method in SCA, we
obtain the model
rt = 0.0061 + at,
a2
t = 0.00014 + 0.9583a2
t−1 + ηt −0.8456ηt−1,
where all estimates are signiﬁcantly different from zero at the 5% level. From
the estimates, we have ˆβ1 = 0.8456 and ˆα1 = 0.9583 −0.8456 = 0.1127. These
approximate estimates are very close to those in Eq. (3.19) or (3.21). Furthermore, the ﬁtted volatility series of the two-pass method is very close to that of
Figure 3.8(a).
3.6
THE INTEGRATED GARCH MODEL
If the AR polynomial of the GARCH representation in Eq. (3.15) has a unit root,
then we have an IGARCH model. Thus, IGARCH models are unit-root GARCH
models. Similar to ARIMA models, a key feature of IGARCH models is that the
impact of past squared shocks ηt−i = a2
t−i −σ 2
t−i for i > 0 on a2
t is persistent.
--- page 168 ---

the integrated garch model
141
An IGARCH(1,1) model can be written as
at = σtϵt,
σ 2
t = α0 + β1σ 2
t−1 + (1 −β1)a2
t−1,
where {ϵt} is deﬁned as before and 1 > β1 > 0. For the monthly excess returns of
the S&P 500 index, an estimated IGARCH(1,1) model is
rt = 0.0067 + at,
at = σtϵt,
σ 2
t = 0.000119 + 0.8059σ 2
t−1 + 0.1941a2
t−1,
where the standard errors of the estimates in the volatility equation are 0.0017,
0.000013, and 0.0144, respectively. The parameter estimates are close to those of
the GARCH(1,1) model shown before, but there is a major difference between
the two models. The unconditional variance of at, hence that of rt, is not deﬁned
under the above IGARCH(1,1) model. This seems hard to justify for an excess
return series. From a theoretical point of view, the IGARCH phenomenon might
be caused by occasional level shifts in volatility. The actual cause of persistence
in volatility deserves a careful investigation.
When α1 + β1 = 1, repeated substitutions in Eq. (3.17) give
σ 2
h(ℓ) = σ 2
h(1) + (ℓ−1)α0,
ℓ≥1,
(3.22)
where h is the forecast origin. Consequently, the effect of σ 2
h(1) on future volatilities
is also persistent, and the volatility forecasts form a straight line with slope α0.
Nelson (1990) studies some probability properties of the volatility process σ 2
t under
an IGARCH model. The process σ 2
t is a martingale for which some nice results
are available in the literature. Under certain conditions, the volatility process is
strictly stationary but not weakly stationary because it does not have the ﬁrst two
moments.
The case of α0 = 0 is of particular interest in studying the IGARCH(1,1) model.
In this case, the volatility forecasts are simply σ 2
h(1) for all forecast horizons;
see Eq. (3.22). This special IGARCH(1,1) model is the volatility model used in
RiskMetrics, which is an approach for calculating value at risk; see Chapter 7.
The model is also an exponential smoothing model for the {a2
t } series. To see this,
rewrite the model as
σ 2
t = (1 −β1)a2
t−1 + β1σ 2
t−1
= (1 −β1)a2
t−1 + β1[(1 −β)a2
t−2 + β1σ 2
t−2]
= (1 −β1)a2
t−1 + (1 −β1)β1a2
t−2 + β2
1σ 2
t−2.
By repeated substitutions, we have
σ 2
t = (1 −β1)(a2
t−1 + β1a2
t−2 + β2
1a3
t−3 + · · ·),
--- page 169 ---

142
conditional heteroscedastic models
which is the well-known exponential smoothing formation with β1 being the discounting factor. Exponential smoothing methods can thus be used to estimate such
an IGARCH(1,1) model.
3.7
THE GARCH-M MODEL
In ﬁnance, the return of a security may depend on its volatility. To model such
a phenomenon, one may consider the GARCH-M model, where M stands for
GARCH in the mean. A simple GARCH(1,1)-M model can be written as
rt = µ + cσ 2
t + at,
at = σtϵt,
σ 2
t = α0 + α1a2
t−1 + β1σ 2
t−1,
(3.23)
where µ and c are constants. The parameter c is called the risk premium parameter.
A positive c indicates that the return is positively related to its volatility. Other
speciﬁcations of risk premium have also been used in the literature, including
rt = µ + cσt + at and rt = µ + c ln(σ 2
t ) + at.
The formulation of the GARCH-M model in Eq. (3.23) implies that there are
serial correlations in the return series rt. These serial correlations are introduced
by those in the volatility process {σ 2
t }. The existence of risk premium is, therefore,
another reason that some historical stock returns have serial correlations.
For illustration, we consider a GARCH(1,1)-M model with Gaussian innovations for the monthly excess returns of the S&P 500 index from January 1926 to
December 1991. The ﬁtted model is
rt = 0.0055 + 1.09σ 2
t + at,
σ 2
t = 8.76 × 10−5 + 0.123a2
t−1 + 0.849σ 2
t−1,
where the standard errors for the two parameters in the mean equation are 0.0023
and 0.818, respectively, and those for the parameters in the volatility equation are
2.51×−5, 0.0205, and 0.0196, respectively. The estimated risk premium for the
index return is positive but is not statistically signiﬁcant at the 5% level. Here the
result is obtained using S-Plus. Other forms of GARCH-M speciﬁcation in S-Plus
are given in Table 3.2. The idea of risk premium applies to other GARCH models.
TABLE 3.2
GARCH-M Models Allowed in S-Plus:
Mean Equation Is rt = µ + cg(σt) + at
g(σt)
Command
σ 2
t
var.in.mean
σt
sd.in.mean
ln(σ 2
t )
logvar.in.mean
--- page 170 ---

the exponential garch model
143
S-Plus Demonstration
> sp.fit = garch(sp∼1+var.in.mean,∼garch(1,1))
> summary(sp.fit)
3.8
THE EXPONENTIAL GARCH MODEL
To overcome some weaknesses of the GARCH model in handling ﬁnancial time
series, Nelson (1991) proposes the exponential GARCH (EGARCH) model. In
particular, to allow for asymmetric effects between positive and negative asset
returns, he considered the weighted innovation
g(ϵt) = θϵt + γ [|ϵt| −E(|ϵt|)],
(3.24)
where θ and γ are real constants. Both ϵt and |ϵt| −E(|ϵt|) are zero-mean iid
sequences with continuous distributions. Therefore, E[g(ϵt)] = 0. The asymmetry
of g(ϵt) can easily be seen by rewriting it as
g(ϵt) =
 (θ + γ )ϵt −γ E(|ϵt|)
if ϵt ≥0,
(θ −γ )ϵt −γ E(|ϵt|)
if ϵt < 0.
Remark.
For the standard Gaussian random variable ϵt, E(|ϵt|) = √2/π. For
the standardized Student-t distribution in Eq. (3.7), we have
E(|ϵt|) = 2
√
v −2[(v + 1)/2]
(v −1)(v/2)√π
.
□
An EGARCH(m, s) model can be written as
at = σtϵt,
ln(σ 2
t ) = α0 + 1 + β1B + · · · + βs−1Bs−1
1 −α1B −· · · −αmBm
g(ϵt−1),
(3.25)
where α0 is a constant, B is the back-shift (or lag) operator such that Bg(ϵt) =
g(ϵt−1), and 1 + β1B + · · · + βs−1Bs−1 and 1 −α1B −· · · −αmBm are polynomials with zeros outside the unit circle and have no common factors. By outside
the unit circle we mean that absolute values of the zeros are greater than 1. Again,
Eq. (3.25) uses the usual ARMA parameterization to describe the evolution of the
conditional variance of at. Based on this representation, some properties of the
EGARCH model can be obtained in a similar manner as those of the GARCH
model. For instance, the unconditional mean of ln(σ 2
t ) is α0. However, the model
differs from the GARCH model in several ways. First, it uses logged conditional
variance to relax the positiveness constraint of model coefﬁcients. Second, the use
of g(ϵt) enables the model to respond asymmetrically to positive and negative
--- page 171 ---

144
conditional heteroscedastic models
lagged values of at. Some additional properties of the EGARCH model can be
found in Nelson (1991).
To better understand the EGARCH model, let us consider the simple model with
order (1,1):
at = σtϵt,
(1 −αB) ln(σ 2
t ) = (1 −α)α0 + g(ϵt−1),
(3.26)
where the ϵt are iid standard normal and the subscript of α1 is omitted. In this
case, E(|ϵt|) = √2/π and the model for ln(σ 2
t ) becomes
(1 −αB) ln(σ 2
t ) =
 α∗+ (γ + θ)ϵt−1
if ϵt−1 ≥0,
α∗+ (γ −θ)(−ϵt−1)
if ϵt−1 < 0,
(3.27)
where α∗= (1 −α)α0 −√2/πγ . This is a nonlinear function similar to that of the
threshold autoregressive (TAR) model of Tong (1978, 1990). It sufﬁces to say that
for this simple EGARCH model the conditional variance evolves in a nonlinear
manner depending on the sign of at−1. Speciﬁcally, we have
σ 2
t = σ 2α
t−1 exp(α∗)



exp

(γ + θ)at−1
σt−1

if at−1 ≥0,
exp

(γ −θ)|at−1|
σt−1

if at−1 < 0.
The coefﬁcients (γ + θ) and (γ −θ) show the asymmetry in response to positive and negative at−1. The model is, therefore, nonlinear if θ̸ = 0. Since negative shocks tend to have larger impacts, we expect θ to be negative. For higher
order EGARCH models, the nonlinearity becomes much more complicated. Cao
and Tsay (1992) use nonlinear models, including EGARCH models, to obtain
multistep-ahead volatility forecasts. We discuss nonlinearity in ﬁnancial time series
in Chapter 4.
3.8.1
Alternative Model Form
An alternative form for the EGARCH(m, s) model is
ln(σ 2
t ) = α0 +
s

i=1
αi
|at−i| + γiat−i
σt−i
+
m

j=1
βj ln(σ 2
t−j).
(3.28)
Here a positive at−i contributes αi(1 + γi)|ϵt−i| to the log volatility, whereas a
negative at−i gives αi(1 −γi)|ϵt−i|, where ϵt−i = at−i/σt−i. The γi parameter thus
signiﬁes the leverage effect of at−i. Again, we expect γi to be negative in real
applications. This is the model form used in S-Plus.
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
