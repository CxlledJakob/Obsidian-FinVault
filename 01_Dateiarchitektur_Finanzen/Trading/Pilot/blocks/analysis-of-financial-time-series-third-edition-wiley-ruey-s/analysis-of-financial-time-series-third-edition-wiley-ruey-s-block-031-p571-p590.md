# Analysis of Financial Time Series, Third Edition (Wiley -- Ruey S_ Tsay -- Wiley series in probability and statistics, 3rd ed_, -- John Wiley & Sons, -- isbn13 9780470414354 -- 9f99b80c7b2dedd477f463dc5323f3b6 -- An.pdf — pages 571–590

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
--- page 572 ---

factor–volatility models
545
••
•
•••••••••
••••
•
•••
•
••
•••••••
•••
•
••••
•
•
•
••
•
••
•
•••
••
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
•
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
••
•
•
•
•
•••
•
••••
•
••••••
••
•
•••••
••••••
•
••••
•••
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
•
•
••
••
•
•••
•
•••••••••
•
•••
•••••••
••••••••••••••
•••
•
•
•
••••••
•••
•
•
••••••
••
•
•••
••
••
•••
•••
••••••
•
••••••
•
•
•
•
••
•
••••
•
•••
•
•
•••••
••
••••••
•••
••••••
••
••
••
•••••
••••
•••
••••••
•
•••
•
••
•
•••••
••
•••
••
•
•
•
•
•
••
••
••
•••••••
••••
••••••••
•••
•
•
••••
••••••
•
•••
••••
••
•••••••
•••••••
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
•
•••
•
•••••
••••••••
•
••
•
••
•••••••
•
•••
•••
•
•••
•
•••
•••
••
•
•
•••••
•
•
•••
••••
•
•
••
••
•
••
•••
•••
•••••
•••
••••
••••••••••••••
••••••••
•
•••••••
•
•
•
••
••
••••
•
••
••
•
•
•••••
••••••
•••
•
•••
••
•••
•
•
••
••
•••
•
•••••
••
•
••
•
•
•
••••
••••
••
•••••••
•••
••
•
•••
•
•
•••••
•
•
•
••••••
••
•••••
•
•••
•
••••••••
•••
•••••
•
•
•••
•
••••••••
•
•
•
•••
•
••
•
•
•
••
•••
•
•••••
••
••••••
•
••
•
••
•
•
••
•
•
•
•••
••
•••
••••••
•
•
•
••
•
•
••
•
•
••
••
••••
•
••
••
•
•••••
••
•
•••
••
••••
••••
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
••
•••
•
•
•
•••
•
•
•
•
••
•••
•
••
Year
(a)
1940
1960
1980
2000
−40 −20
0
PCA
20
40
•••••••••••••••••••••••••
•
•
••••••••••••••
••••
••
••
•••
•
•
•
•
•
••
••
•
••
•
••
••••••••••••••••••••••••••••••••••••••
••••••••••••••••••••
•••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••
•
•••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••
•••••••••••••••••••••••••••••••••••••••••
•••••••••••••••••••••••••
••••••••••••••
•••••••••••••
100 200
Volatilities
300 400
Year
(b)
1940
1960
1980
2000
Figure 10.17
(a) Time plot of ﬁrst principal component of monthly log returns of IBM stock and S&P
500 index. (b) Fitted volatility process based on a GARCH(1,1) model.
is 0.165. The conditional variance equation is

 σ11,t
σ22,t

=


19.08
(3.70)
−5.62
(2.36)

+


0.098
(0.044)
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
0.333
(0.076)
0.596
(0.050)

σ 2
t ,
(10.39)
where, as before, standard errors are in parentheses, and σ 2
t is obtained from model
(10.38). The conditional correlation equation is
ρt =
exp(qt)
1 + exp(qt),
qt = −2.098 + 4.120ρt−1 + 0.078
a1,t−1a2,t−1
√σ11,t−1σ22,t−1
,
(10.40)
where standard errors of the three parameters are 0.025, 0.038, and 0.015,
respectively.
Deﬁning
the
standardized
residuals
as
before,
we
obtain
Q2(4) = 15.37(0.29) and Q2(8) = 34.24(0.23), where the number in parentheses
denotes the p value. Therefore, the standardized residuals have no serial
--- page 573 ---

546
multivariate volatility models and their applications
correlations. Yet we have Q∗
2(4) = 20.25(0.09) and Q∗
2(8) = 61.95(0.0004) for
the squared standardized residuals. The volatility model in Eq. (10.39) does not
adequately handle the conditional heteroscedasticity of the data especially at
higher lags. This is not surprising as the single common factor only explains about
82.5% of the generalized variance of the data.
Comparing the factor model in Eqs. (10.39) and (10.40) with the time-varying
correlation model in Eqs. (10.26) and (10.27), we see that (a) the correlation
equations of the two models are essentially the same, (b) as expected the factor
model uses fewer parameters in the volatility equation, and (c) the commonfactor model provides a reasonable approximation to the volatility process of
the data.
Remark.
In Example 10.8, we used a two-step estimation procedure. In the
ﬁrst step, a volatility model is built for the common factor. The estimated volatility
is treated as given in the second step to estimate the multivariate volatility model.
Such an estimation procedure is simple but may not be efﬁcient. A more efﬁcient
estimation procedure is to perform a joint estimation. This can be done relatively
easily provided that the common factors are known. For example, for the monthly
log returns of Example 10.8, a joint estimation of Eqs. (10.38)–(10.40) can be performed if the common factor xt = 0.769r1t + 0.605r2t is treated as given.
□
10.7
APPLICATION
We illustrate the application of multivariate volatility models by considering the
value at risk (VaR) of a ﬁnancial position with multiple assets. Suppose that an
investor holds a long position in the stocks of Cisco Systems and Intel Corporation each worth $1 million. We use the daily log returns for the two stocks from
January 2, 1991, to December 31, 1999, to build volatility models. The VaR is
computed using the 1-step-ahead forecasts at the end of data span and 5% critical
values.
Let VaR1 be the value at risk for holding the position on Cisco Systems stock
and VaR2 for holding Intel stock. Results of Chapter 7 show that the overall daily
VaR for the investor is
VaR =

VaR2
1 + VaR2
2 + 2ρVaR1VaR2.
In this illustration, we consider three approaches to volatility modeling for calculating VaR. For simplicity, we do not report standard errors for the parameters
involved or model checking statistics. Yet all of the estimates are statistically signiﬁ-
cant at the 5% level, and the models are adequate based on the Ljung–Box statistics
of the standardized residual series and their squared series. The log returns are in
percentages so that the quantiles are divided by 100 in VaR calculations. Let r1t
be the return of Cisco stock and r2t the return of Intel stock.
--- page 574 ---

application
547
Univariate Models
This approach uses a univariate volatility model for each stock return and uses the
sample correlation coefﬁcient of the stock returns to estimate ρ. The univariate
volatility models for the two stock returns are
r1t = 0.380 + 0.034r1,t−1 −0.061r1,t−2 −0.055r1,t−3 + a1t,
σ 2
1t = 0.599 + 0.117a2
1,t−1 + 0.814σ 2
1,t−1
and
r2t = 0.187 + a2t,
σ 2
2t = 0.310 + 0.032a2
2,t−1 + 0.918σ 2
2,t−1.
The sample correlation coefﬁcient is 0.473. The 1-step-ahead forecasts needed in
VaR calculation at the forecast origin t = 2275 are
ˆr1 = 0.626,
ˆσ 2
1 = 4.152,
ˆr2 = 0.187,
ˆσ 2
2 = 6.087,
ˆρ = 0.473.
The 5% quantiles for both daily returns are
q1 = 0.626 −1.65
√
4.152 = −2.736,
q2 = 0.187 −1.65
√
6.087 = −3.884,
where the negative sign denotes loss. For the individual stocks, VaR1 =
$1000000q1/100 = $27,360andVaR2 = $1000000q2/100 = $38,840.
Consequently, the overall VaR for the investor is VaR = $57,117.
Constant-Correlation Bivariate Model
This approach employs a bivariate GARCH(1,1) model for the stock returns. The
correlation coefﬁcient is assumed to be constant over time, but it is estimated jointly
with other parameters. The model is
r1t = 0.385 + 0.038r1,t−1 −0.060r1,t−2 −0.047r1,t−3 + a1t,
r2t = 0.222 + a2t,
σ11,t = 0.624 + 0.110a2
1,t−1 + 0.816σ11,t−1,
σ22,t = 0.664 + 0.038a2
2,t−1 + 0.853σ22,t−1,
and ˆρ = 0.475. This is a diagonal bivariate GARCH(1,1) model. The 1-step-ahead
forecasts for VaR calculation at the forecast origin t = 2275 are
ˆr1 = 0.373,
ˆσ 2
1 = 4.287,
ˆr2 = 0.222,
ˆσ 2
2 = 5.706,
ˆρ = 0.475.
Consequently, we have VaR1 = $30,432 and VaR2 = $37,195. The overall 5%
VaR for the investor is VaR = $58,180.
--- page 575 ---

548
multivariate volatility models and their applications
Time-Varying Correlation Model
Finally, we allow the correlation coefﬁcient to evolve over time by using the
Cholesky decomposition. The ﬁtted model is
r1t = 0.355 + 0.039r1,t−1 −0.057r1,t−2 −0.038r1,t−3 + a1t,
r2t = 0.206 + a2t,
g11,t = 0.420 + 0.091b2
1,t−1 + 0.858g11,t−1,
q21,t = 0.123 + 0.689q21,t−1 −0.014a2,t−1,
g22,t = 0.080 + 0.013b2
2,t−1 + 0.971g22,t−1,
where b1t = a1t and b2t = a2t −q21,ta1t. The 1-step-ahead forecasts for VaR calculation at the forecast origin t = 2275 are
ˆr1 = 0.352,
ˆr2 = 0.206,
ˆg11 = 4.252,
ˆq21 = 0.421,
ˆg22 = 5.594.
Therefore, we have ˆσ 2
1 = 4.252, ˆσ21 = 1.791, and ˆσ 2
2 = 6.348. The correlation
coefﬁcient is ˆρ = 0.345. Using these forecasts, we have VaR1 = $30,504, VaR2 =
$39,512, and the overall VaR = $57,648.
The estimated VaR values of the three approaches are similar. The univariate
models give the lowest VaR, whereas the constant-correlation model produces the
highest VaR. The range of the difference is about $1100. The time-varying volatility
model seems to produce a compromise between the two extreme models.
10.8
MULTIVARIATE t DISTRIBUTION
Empirical analysis indicates that the multivariate Gaussian innovations used in the
previous sections may fail to capture the kurtosis of asset returns. In this situation,
a multivariate Student-t distribution might be useful. There are many versions of
the multivariate Student-t distribution. We give a simple version here for volatility
modeling.
A k-dimensional random vector x = (x1, . . . , xk)′ has a multivariate Studentt distribution with v degrees of freedom and parameters µ = 0 and  = I (the
identity matrix) if its probability density function (pdf) is
f (x|v) = [(v + k)/2]
(πv)k/2(v/2)(1 + v−1x′x)−(v+k)/2,
(10.41)
where (y) is the gamma function; see Mardia, Kent, and Bibby (1979, p. 57). The
variance of each component xi in Eq. (10.41) is v/(v −2), and hence we deﬁne
ϵt = √(v −2)/vx as the standardized multivariate Student-t distribution with v
degrees of freedom. By transformation, the pdf of ϵt is
f (ϵt|v) =
[(v + k)/2]
[π(v −2)]k/2(v/2)[1 + (v −2)−1ϵ′
tϵt]−(v+k)/2.
(10.42)
--- page 576 ---

appendix: some remarks on estimation
549
For volatility modeling, we write at = 1/2
t
ϵt and assume that ϵt follows the
multivariate Student-t distribution in Eq. (10.42). By transformation, the pdf of
at is
f (at|v, t) =
[(v + k)/2]
[π(v −2)]k/2(v/2)|t|1/2 [1 + (v −2)−1a′
t−1
t at]−(v+k)/2.
Furthermore, if we use the Cholesky decomposition of t, then the pdf of the
transformed shock bt becomes
f (bt|v, Lt, Gt) =
[(v + k)/2]
[π(v −2)]k/2(v/2) k
j=1 g1/2
jj,t
×

1 + (v −2)−1
k

j=1
b2
jt
gjj,t


(v+k)/2
,
where at = Ltbt and gjj,t is the conditional variance of bjt. Because this pdf does
not involve any matrix inversion, the conditional-likelihood function of the data is
easy to evaluate.
APPENDIX: SOME REMARKS ON ESTIMATION
The estimation of multivariate ARMA models in this chapter is done by using
the time series program SCA of Scientiﬁc Computing Associates. The estimation
of multivariate volatility models is done by using either the S-Plus package with
FinMetrics or the Regression Analysis for Time Series (RATS) program or Matlab.
Below are some run streams for estimating multivariate volatility models using the
RATS program. A line starting with * means “comment” only.
Estimation of the Diagonal Constant-Correlation AR(2)–GARCH(1,1) Model
for Example 10.5
The program includes some Ljung–Box statistics for each component and some
ﬁtted values for the last few observations. The data ﬁle is m-ibmspln.txt, which
has two columns, and there are 888 observations.
all 0 888:1
open data m-ibmspln.txt
data(org=obs) / r1 r2
set h1 = 0.0
set h2 = 0.0
nonlin a0 a1 b1 a00 a11 b11 rho c1 c2 p1
frml a1t = r1(t)-c1-p1*r2(t-1)
frml a2t = r2(t)-c2
frml gvar1 = a0+a1*a1t(t-1)**2+b1*h1(t-1)
--- page 577 ---

550
multivariate volatility models and their applications
frml gvar2 = a00+a11*a2t(t-1)**2+b11*h2(t-1)
frml gdet = -0.5*(log(h1(t)=gvar1(t))+log(h2(t)=gvar2(t)) $
+log(1.0-rho**2))
frml gln = gdet(t)-0.5/(1.0-rho**2)*((a1t(t)**2/h1(t)) $
+(a2t(t)**2/h2(t))-2*rho*a1t(t)*a2t(t)/sqrt(h1(t)*h2(t)))
smpl 3 888
compute c1 = 1.22, c2 = 0.57, p1 = 0.1, rho = 0.1
compute a0 = 3.27, a1 = 0.1, b1 = 0.6
compute
a00 = 1.17, a11 = 0.13, b11 = 0.8
maximize(method=bhhh,recursive,iterations=150) gln
set fv1 = gvar1(t)
set resi1 = a1t(t)/sqrt(fv1(t))
set residsq = resi1(t)*resi1(t)
* Checking standardized residuals *
cor(qstats,number=12,span=4) resi1
* Checking squared standardized residuals *
cor(qstats,number=12,span=4) residsq
set fv2 = gvar2(t)
set resi2 = a2t(t)/sqrt(fv2(t))
set residsq = resi2(t)*resi2(t)
* Checking standardized residuals *
cor(qstats,number=12,span=4) resi2
* Checking squared standardized residuals *
cor(qstats,number=12,span=4) residsq
* Last few observations needed for computing forecasts *
set shock1 = a1t(t)
set shock2 = a2t(t)
print 885
888 shock1 shock2 fv1 fv2
Estimation of the Time-Varying Coefﬁcient Model in Example 10.5
all 0 888:1
open data m-ibmspln.txt
data(org=obs) / r1 r2
set h1 = 45.0
set h2 = 31.0
set rho = 0.8
nonlin
a0 a1 b1 f1 a00 a11 b11 d11 f11 c1 c2 p1 p3 q0 q1 q2
frml a1t = r1(t)-c1-p1*r1(t-1)-p3*r2(t-2)
frml a2t = r2(t)-c2
frml gvar1 = a0+a1*a1t(t-1)**2+b1*h1(t-1)+f1*h2(t-1)
frml gvar2 = a00+a11*a2t(t-1)**2+b11*h2(t-1)+f11*h1(t-1) $
+d11*a1t(t-1)**2
frml rh1 = q0 + q1*rho(t-1) $
+ q2*a1t(t-1)*a2t(t-1)/sqrt(h1(t-1)*h2(t-1))
frml rh = exp(rh1(t))/(1+exp(rh1(t)))
frml gdet = -0.5*(log(h1(t)=gvar1(t))+log(h2(t)=gvar2(t)) $
+log(1.0-(rho(t)=rh(t))**2))
frml gln = gdet(t)-0.5/(1.0-rho(t)**2)*((a1t(t)**2/h1(t)) $
--- page 578 ---

appendix: some remarks on estimation
551
+(a2t(t)**2/h2(t))-2*rho(t)*a1t(t)*a2t(t)/sqrt(h1(t)*h2(t)))
smpl 4 888
compute c1 = 1.4, c2 = 0.7, p1 = 0.1,
p3 = -0.1
compute a0 = 2.95, a1 = 0.08, b1 = 0.87, f1 = -.03
compute a00 = 2.05, a11 = 0.05
compute
b11 = 0.92, f11=-.06, d11=.04, q0 = -2.0
compute
q1 = 3.0, q2 = 0.1
nlpar(criterion=value,cvcrit=0.00001)
maximize(method=bhhh,recursive,iterations=150) gln
set fv1 = gvar1(t)
set resi1 = a1t(t)/sqrt(fv1(t))
set residsq = resi1(t)*resi1(t)
* Checking standardized residuals *
cor(qstats,number=16,span=4) resi1
* Checking squared standardized residuals *
cor(qstats,number=16,span=4) residsq
set fv2 = gvar2(t)
set resi2 = a2t(t)/sqrt(fv2(t))
set residsq = resi2(t)*resi2(t)
* Checking standardized residuals *
cor(qstats,number=16,span=4) resi2
* Checking squared standardized residuals *
cor(qstats,number=16,span=4) residsq
* Last few observations needed for computing forecasts *
set rhohat = rho(t)
set shock1 = a1t(t)
set shock2 = a2t(t)
print 885
888 shock1 shock2 fv1 fv2 rhohat
Estimation of the Time-Varying Coefﬁcient Model in Example 10.5 Using
Cholesky Decomposition
all 0 888:1
open data m-ibmspln.txt
data(org=obs) / r1 r2
set h1 = 45.0
set h2 = 20.0
set q = 0.8
nonlin
a0 a1 b1 a00 a11 b11 d11 f11 c1 c2 p1 p3 t0 t1 t2
frml a1t = r1(t)-c1-p1*r1(t-1)-p3*r2(t-2)
frml a2t = r2(t)-c2
frml v1 = a0+a1*a1t(t-1)**2+b1*h1(t-1)
frml qt = t0 + t1*q(t-1) + t2*a2t(t-1)
frml bt = a2t(t) - (q(t)=qt(t))*a1t(t)
frml v2 = a00+a11*bt(t-1)**2+b11*h2(t-1)+f11*h1(t-1) $
+d11*a1t(t-1)**2
frml gdet = -0.5*(log(h1(t) = v1(t))+ log(h2(t)=v2(t)))
frml garchln = gdet-0.5*(a1t(t)**2/h1(t)+bt(t)**2/h2(t))
smpl 5 888
--- page 579 ---

552
multivariate volatility models and their applications
compute c1 = 1.4, c2 = 0.7, p1 = 0.1, p3 = -0.1
compute a0 = 1.0, a1 = 0.08, b1 = 0.87
compute a00 = 2.0, a11 = 0.05, b11 = 0.8
compute
d11=.04, f11=-.06, t0 =0.2, t1 = 0.1, t2 = 0.1
nlpar(criterion=value,cvcrit=0.00001)
maximize(method=bhhh,recursive,iterations=150) garchln
set fv1 = v1(t)
set resi1 = a1t(t)/sqrt(fv1(t))
set residsq = resi1(t)*resi1(t)
* Checking standardized residuals *
cor(qstats,number=16,span=4) resi1
* Checking squared standardized residuals *
cor(qstats,number=16,span=4) residsq
set fv2 = v2(t)+qt(t)**2*v1(t)
set resi2 = a2t(t)/sqrt(fv2(t))
set residsq = resi2(t)*resi2(t)
* Checking standardized residuals *
cor(qstats,number=16,span=4) resi2
* Checking squared standardized residuals *
cor(qstats,number=16,span=4) residsq
* Last few observations needed for forecasts *
set rhohat = qt(t)*sqrt(v1(t)/fv2(t))
set shock1 = a1t(t)
set shock2 = a2t(t)
set g22 = v2(t)
set q21 = qt(t)
set b2t = bt(t)
print 885
888 shock1 shock2 fv1 fv2 rhohat g22 q21 b2t
Estimation of Three-Dimensional Time-Varying Correlation Volatility Model in
Example 10.7 Using Cholesky Decomposition
Initial estimates are obtained by a sequential modeling procedure.
all 0 2275:1
open data d-cscointc.txt
data(org=obs) / r1 r2 r3
set h1 = 1.0
set h2 = 4.0
set h3 = 3.0
set q21 = 0.8
set q31 = 0.3
set q32 = 0.3
nonlin
c1 c2 c3 p3 p21 p22 p31 p33 a0 a1 a2 t0 t1 t2 b0 b1 $
b2 u0 u1 u2 w0 w1 w2 d0 d1 d2 d5
frml a1t = r1(t)-c1-p3*r1(t-3)
frml a2t = r2(t)-c2-p21*r1(t-2)-p22*r2(t-2)
frml a3t = r3(t)-c3-p31*r1(t-1)-p33*r3(t-1)
frml v1 = a0+a1*a1t(t-1)**2+a2*h1(t-1)
--- page 580 ---

appendix: some remarks on estimation
553
frml q1t = t0 + t1*q21(t-1) + t2*a2t(t-1)
frml bt = a2t(t) - (q21(t)=q1t(t))*a1t(t)
frml v2 = b0+b1*bt(t-1)**2+b2*h2(t-1)
frml q2t = u0 + u1*q31(t-1) + u2*a3t(t-1)
frml q3t = w0 + w1*q32(t-1) + w2*a2t(t-1)
frml b1t = a3t(t)-(q31(t)=q2t(t))*a1t(t)-(q32(t)=q3t(t))*bt(t)
frml v3 = d0+d1*b1t(t-1)**2+d2*h3(t-1)+d5*h2(t-1)
frml gdet = -0.5*(log(h1(t) = v1(t))+ log(h2(t)=v2(t)) $
+log(h3(t)=v3(t)))
frml garchln = gdet-0.5*(a1t(t)**2/h1(t)+bt(t)**2/h2(t) $
+b1t(t)**2/h3(t))
smpl 8 2275
compute c1 = 0.07, c2 = 0.33, c3 = 0.19, p1 = 0.1, p3 = -0.04
compute p21 =0.2, p22 = -0.1, p31 = -0.26, p33 = 0.06
compute a0 = .01, a1 = 0.05, a2 = 0.94
compute t0 = 0.28, t1 =0.82, t2 = -0.035
compute b0 = .17, b1 = 0.08, b2 = 0.89
compute u0= 0.04, u1 = 0.97, u2 = 0.01
compute
w0 =0.006, w1=0.98, w2=0.004
compute d0 =1.38, d1 = 0.06, d2 = 0.64, d5 = -0.027
nlpar(criterion=value,cvcrit=0.00001)
maximize(method=bhhh,recursive,iterations=250) garchln
set fv1 = v1(t)
set resi1 = a1t(t)/sqrt(fv1(t))
set residsq = resi1(t)*resi1(t)
* Checking standardized residuals *
cor(qstats,number=12,span=4) resi1
* Checking squared standardized residuals *
cor(qstats,number=12,span=4) residsq
set fv2 = v2(t)+q1t(t)**2*v1(t)
set resi2 = a2t(t)/sqrt(fv2(t))
set residsq = resi2(t)*resi2(t)
* Checking standardized residuals *
cor(qstats,number=12,span=4) resi2
* Checking squared standardized residuals *
cor(qstats,number=12,span=4) residsq
set fv3 = v3(t)+q2t(t)**2*v1(t)+q3t(t)**2*v2(t)
set resi3 = a3t(t)/sqrt(fv3(t))
set residsq = resi3(t)*resi3(t)
* Checking standardized residuals *
cor(qstats,number=12,span=4) resi3
* Checking squared standardized residuals *
cor(qstats,number=12,span=4) residsq
* print standardized residuals and correlation-coefficients
set rho21 = q1t(t)*sqrt(v1(t)/fv2(t))
set rho31 = q2t(t)*sqrt(v1(t)/fv3(t))
set rho32 = (q2t(t)*q1t(t)*v1(t) $
+q3t(t)*v2(t))/sqrt(fv2(t)*fv3(t))
print 10
2275 resi1 resi2 resi3
--- page 581 ---

554
multivariate volatility models and their applications
print 10 2275 rho21 rho31 rho32
print 10 2275 fv1 fv2 fv3
EXERCISES
10.1. Consider the monthly simple returns, including dividends, of IBM stock,
Hewlett-Packard (HPQ) stock, and the S&P composite index from January
1962 to December 2008 for 564 observations. The returns are in the ﬁle
m-ibmhpqsp6208.txt. Transform into log returns in percentages. Use the
exponentially weighted moving-average method to obtain a multivariate
volatility series for the three return series. What is the estimated λ? Plot the
three volatility series.
10.2. Focus on the monthly log returns of IBM and HPQ stocks from January
1962 to December 2008. Fit a DVEC(1,1) model to the bivariate return
series. Is the model adequate? Plot the ﬁtted volatility series and the timevarying correlations.
10.3. Focus on the monthly log returns of the S&P composite index and HPQ
stock. Build a BEKK model for the bivariate series. What is the ﬁtted
model? Plot the ﬁtted volatility series and the time-varying correlations.
10.4. Build a constant-correlation volatility model for the three monthly log
returns of IBM stock, HPQ stock, and S&P composite index. Write down
the ﬁtted model. Is the model adequate? Why?
10.5. The ﬁle m-geibmsp2608.txt contains the monthly simple returns of General Electric stock, IBM stock, and the S&P composite index from January
1926 to December 2008. The returns include dividends. Transform into log
returns in percentages. Focus on the monthly log returns in percentages of
GE stock and the S&P 500 index. Build a constant-correlation GARCH
model for the bivariate series. Check the adequacy of the ﬁtted model, and
obtain the 1-step-ahead forecast of the covariance matrix at the forecast
origin December 2008.
10.6. Again, consider the monthly log returns of GE, IBM, and S&P composite
index from January 1926 to December 2008. Build a dynamic correlation model for the three-dimensional series. For simplicity, use the sample
correlation matrix for ρ in Eq. (10.32).
10.7. The ﬁle m-spibmge.txt contains the monthly log returns in percentages
of the S&P composite index, IBM stock, and GE stock from January 1926
to December 1999. Focus on GE stock and the S&P 500 index. Build a
time-varying correlation GARCH model for the bivariate series using a
logistic function for the correlation coefﬁcient. Check the adequacy of the
ﬁtted model, and obtain the 1-step-ahead forecast of the covariance matrix
at the forecast origin December 1999.
10.8. Focus on the monthly log returns in percentages of GE stock and the S&P
500 index from January 1926 to December 1999. Build a time-varying
--- page 582 ---

references
555
correlation GARCH model for the bivariate series using the Cholesky
decomposition. Check the adequacy of the ﬁtted model, and obtain the
1-step-ahead forecast of the covariance matrix at the forecast origin
December 1999. Compare the model with the other model built in the
previous exercise.
10.9. Consider the three-dimensional return series of the previous exercise jointly.
Build a multivariate time-varying volatility model for the data, using the
Cholesky decomposition. Discuss the implications of the model and compute the 1-step-ahead volatility forecast at the forecast origin t = 888.
10.10. An investor is interested in daily value at risk of his position on holding
long $0.5 million of Dell stock and $1 million of Cisco Systems stock.
Use 5% critical values and the daily log returns from February 20, 1990,
to December 31, 1999, to do the calculation. The data are in the ﬁle ddellcsco9099.txt. Apply the three approaches to volatility modeling in
Section 10.7 and compare the results.
REFERENCES
Bauwens, L., Laurent, S., and Rombouts, J. V. K. (2004). Multivariate GARCH models: A
survey. Journal of Applied Econometrics 21:79–109.
Bollerslev, T. (1990). Modeling the coherence in short-term nominal exchange rates: A multivariate generalized ARCH approach. Review of Economics and Statistics 72:498–505.
Bollerslev, T., Engle, R. F., and Wooldridge, J. M. (1988). A capital-asset pricing model
with time-varying covariances. Journal of Political Economy 96:116–131.
Chib, S., Nardari, F. and Shephard, N. (1999). Analysis of high dimensional multivariate
stochastic volatility models. Working paper, Washington University, St. Louis.
Engle, R. F. (2002). Dynamic conditional correlation: A simple class of multivariate GARCH
models. Journal of Business and Economic Statistics 20:339–350.
Engle, R. F. and Kroner, K. F. (1995). Multivariate simultaneous generalized ARCH. Econometric Theory 11:122–150.
Harvey, A, Ruiz, E., and Shephard, N. (1994). Multivariate stochastic variance models.
Review of Economic Studies 62:247–264.
Li, W. K. (2004). Diagnostic Checks in Time Series. Chapman and Hall, London.
Mardia, K. V., Kent, J. T., and Bibby, J. M. (1979). Multivariate Analysis. Academic, New
York.
Pourahmadi, M. (1999). Joint mean-covariance models with applications to longitudinal data:
Unconstrained parameterization. Biometrika 86:677–690.
Tsay, R. S. (2006). Multivariate volatility models in H. C. Ho, C. K. Ing, and T. L. Lai (eds.).
Time Series and Related Topics in memory of C.Z. Wei, Lecture Notes Monograph
Series, Institute of Mathematical Statistics. Beachwood, Ohio.
Tse, Y. K. (2000). A test for constant correlations in a multivariate GARCH model. Journal
of Econometrics 98:107–127.
Tse, Y. K. and Tsui, A. K. C. (2002). A multivariate GARCH model with time-varying
correlations. Journal of Business & Economic Statistics 20:351–362.
--- page 583 ---
--- page 584 ---

C H A P T E R
11
State-Space Models
and Kalman Filter
The state-space model provides a ﬂexible approach to time series analysis, especially for simplifying maximum-likelihood estimation and handling missing values.
In this chapter, we discuss the relationship between the state-space model and the
ARIMA model, the Kalman ﬁlter algorithm, various smoothing methods, and some
applications. We begin with a simple model that shows the basic ideas of the statespace approach to time series analysis before introducing the general state-space
model. For demonstrations, we use the model to analyze realized volatility series of
asset returns, the time-varying coefﬁcient market models, and the quarterly earnings
per share of a company.
There are many books on statistical analysis using the state-space model. Durbin
and Koopman (2001) provide a recent treatment of the approach, Kim and Nelson
(1999) focus on economic applications and regime switching, and Anderson and
Moore (1979) give a nice summary of theory and applications of the approach for
engineering and optimal control. Many time series textbooks include the Kalman
ﬁlter and state-space model. For example, Chan (2002), Shumway and Stoffer
(2000), Hamilton (1994), and Harvey (1993) all have chapters on the topic. West
and Harrison (1997) provide a Bayesian treatment with emphasis on forecasting,
and Kitagawa and Gersch (1996) use a smoothing prior approach.
The derivation of Kalman ﬁlter and smoothing algorithms necessarily involves
heavy notation. Therefore, Section 11.4 could be dry for readers who are interested
mainly in the concept and applications of state-space models and can be skipped
on the ﬁrst read.
Analysis of Financial Time Series, Third Edition, By Ruey S. Tsay
Copyright 2010 John Wiley & Sons, Inc.
557
--- page 585 ---

558
state-space models and kalman ﬁlter
11.1
LOCAL TREND MODEL
Consider the univariate time series yt satisfying
yt = µt + et,
et ∼N(0, σ 2
e ),
(11.1)
µt+1 = µt + ηt,
ηt ∼N(0, σ 2
η ),
(11.2)
where {et} and {ηt} are two independent Gaussian white noise series and t =
1, . . . , T . The initial value µ1 is either given or follows a known distribution, and
it is independent of {et} and {ηt} for t > 0. Here µt is a pure random walk of
Chapter 2 with initial value µ1, and yt is an observed version of µt with added
noise et. In the literature, µt is referred to as the trend of the series, which is not
directly observable, and yt is the observed data with observational noise et. The
dynamic dependence of yt is governed by that of µt because {et} is not serially
correlated.
The model in Eqs. (11.1) and (11.2) can readily be used to analyze realized
volatility of an asset price; see Example 11.1. Here µt represents the underlying
log volatility of the asset price and yt is the logarithm of realized volatility. The
true log volatility is not directly observed but evolves over time according to a
random-walk model. On the other hand, yt is constructed from high-frequency
transactions data and subjected to the inﬂuence of market microstructure noises.
The standard deviation of et denotes the scale used to measure the impact of market
microstructure noises.
The model in Eqs. (11.1) and (11.2) is a special linear Gaussian state-space
model. The variable µt is called the state of the system at time t and is
not directly observed. Equation (11.1) provides the link between the data yt
and the state µt and is called the observation equation with measurement
error et. Equation (11.2) governs the time evolution of the state variable
and is the state equation (or state transition equation) with innovation ηt.
The model is also called a local-level model in Durbin and Koopman (2001,
Chapter 2), which is a simple case of the structural time series model of
Harvey (1993).
Relationship to ARIMA Model
If there is no measurement error in Eq. (11.1), that is, σe = 0, then yt = µt, which
is an ARIMA(0,1,0) model. If σe > 0, that is, there exist measurement errors, then
yt is an ARIMA(0,1,1) model satisfying
(1 −B)yt = (1 −θB)at,
(11.3)
where {at} is a Gaussian white noise with mean zero and variance σ 2
a . The values
of θ and σa are determined by σe and ση. This result can be derived as follows.
From Eq. (11.2), we have
(1 −B)µt+1 = ηt
or
µt+1 =
1
1 −B ηt.
--- page 586 ---

local trend model
559
Using this result, Eq. (11.1) can be written as
yt =
1
1 −B ηt−1 + et.
Multiplying by (1 −B), we have
(1 −B)yt = ηt−1 + et −et−1.
Let (1 −B)yt = wt. We have wt = ηt−1 + et −et−1. Under the model assumptions, it is easy to see that (a) wt is Gaussian, (b) Var(wt) = 2σ 2
e + σ 2
η , (c)
Cov(wt, wt−1) = −σ 2
e , and (d) Cov(wt, wt−j) = 0 for j > 1. Consequently, wt
follows an MA(1) model and can be written as wt = (1 −θB)at. By equating
the variance and lag-1 autocovariance of wt = (1 −θB)at = ηt−1 + et −et−1, we
have
(1 + θ2)σ 2
a = 2σ 2
e + σ 2
η ,
(11.4)
θσ 2
a = σ 2
e .
(11.5)
For given σ 2
e and σ 2
η , one considers the ratio of the prior two equations to form a
quadratic function of θ. This quadratic form has two solutions so one should select
the one that satisﬁes |θ| < 1. The value of σ 2
a can then be easily obtained. Thus,
the state-space model in Eqs. (11.1) and (11.2) is also an ARIMA(0,1,1) model,
which is the simple exponential smoothing model of Chapter 2.
On the other hand, for an ARIMA(0,1,1) model with positive θ, one can use
the prior two identities to solve for σ 2
e and σ 2
η , and obtain a local trend model.
If θ is negative, then the model can still be put in a state-space form without
the observational error, that is, σe = 0. In fact, as will be seen later, an ARIMA
model can be transformed into state-space models in many ways. Thus, the linear
state-space model is closely related to the ARIMA model.
In practice, what one observes is the yt series. Thus, based on the data alone,
the decision of using ARIMA models or linear state-space models is not critical.
Both model representations have pros and cons. The objective of data analysis, substantive issues, and experience all play a role in choosing a statistical
model.
Example 11.1.
To illustrate the ideas of the state-space model and Kalman
ﬁlter, we consider the intradaily realized volatility of Alcoa stock from January 2,
2003, to May 7, 2004, for 340 observations. The daily realized volatility used is
the sum of squares of intraday 10-minute log returns measured in percentage. No
overnight returns or the ﬁrst 10-minute intraday returns are used. See Chapter 3 for
more information about realized volatility. The series used in the demonstration is
the logarithm of the daily realized volatility.
Figure 11.1 shows the time plot of the logarithms of the realized volatility of
Alcoa stock from January 2, 2003, to May 7, 2004. The transactions data are
obtained from the TAQ database of the NYSE. If ARIMA models are entertained,
--- page 587 ---

560
state-space models and kalman ﬁlter
Day
Realized volatility
0
100
200
300
−1
0
1
2
3
Figure 11.1
Time plot of logarithms of intradaily realized volatility of Alcoa stock from January 2,
2003, to May 7, 2004. Realized volatility is computed from intraday 10-minute log returns measured
in percentage.
we obtain an ARIMA(0,1,1) model
(1 −B)yt = (1 −0.858B)at,
ˆσa = 0.5184,
(11.6)
where yt is the log realized volatility, and the standard error of ˆθ is 0.028. The
residuals show Q(12) = 12.4 with a p value of 0.33, indicating that there is
no signiﬁcant serial correlation in the residuals. Similarly, the squared residuals
give Q(12) = 8.2 with a p value of 0.77, suggesting no ARCH effects in the
series.
Since ˆθ is positive, we can transform the ARIMA(0,1,1) model into a local
trend model in Eqs. (11.1) and (11.2). The maximum-likelihood estimates (MLE)
of the two parameters are ˆση = 0.0735 and ˆσe = 0.4803. The measurement errors
have a larger variance than the state innovations, conﬁrming that intraday highfrequency returns are subject to measurement errors. Details of estimation will be
discussed in Section 11.1.7. Here we treat the two estimates as given and use the
model to demonstrate application of the Kalman ﬁlter. Note that using the model
in Eq. (11.6) and the relation in Eqs. (11.4) and (11.5), we obtain σe = 0.480 and
ση = 0.0736. These values are close to the MLE shown above.
--- page 588 ---

local trend model
561
11.1.1
Statistical Inference
Return to the state-space model in Eqs. (11.1) and (11.2). The aim of the analysis
is to infer properties of the state µt from the data {yt|t = 1, . . . , T } and the model.
Three types of inference are commonly discussed in the literature. They are ﬁltering, prediction, and smoothing. Let Ft = {y1, . . . , yt} be the information available
at time t (inclusive) and assume that the model is known, including all parameters.
The three types of inference can brieﬂy be described as follows:
• Filtering.
Filtering means to recover the state variable µt given Ft, that is,
to remove the measurement errors from the data.
• Prediction.
Prediction means to forecast µt+h or yt+h for h > 0 given Ft,
where t is the forecast origin.
• Smoothing.
Smoothing is to estimate µt given FT , where T > t.
A simple analogy of the three types of inference is reading a handwritten note.
Filtering is ﬁguring out the word you are reading based on knowledge accumulated
from the beginning of the note, predicting is to guess the next word, and smoothing
is deciphering a particular word once you have read through the note.
To describe the inference more precisely, we introduce some notation. Let
µt|j = E(µt|Fj) and t|j = Var(µt|Fj) be, respectively, the conditional mean and
variance of µt given Fj. Similarly, yt|j denotes the conditional mean of yt given
Fj. Furthermore, let vt = yt −yt|t−1 and Vt = Var(vt|Ft−1) be the 1-step-ahead
forecast error and its variance of yt given Ft−1. Note that the forecast error vt is
independent of Ft−1 so that the conditional variance is the same as the unconditional
variance; that is, Var(vt|Ft−1) = Var(vt). From Eq. (11.1),
yt|t−1 = E(yt|Ft−1) = E(µt + et|Ft−1) = E(µt|Ft−1) = µt|t−1.
Consequently,
vt = yt −yt|t−1 = yt −µt|t−1
(11.7)
and
Vt = Var(yt −µt|t−1|Ft−1) = Var(µt + et −µt|t−1|Ft−1)
= Var(µt −µt|t−1|Ft−1) + Var(et|Ft−1) = t|t−1 + σ 2
e .
(11.8)
It is also easy to see that
E(vt) = E[E(vt|Ft−1)] = E[E(yt −yt|t−1|Ft−1)] = E[yt|t−1 −yt|t−1] = 0,
Cov(vt, yj) = E(vtyj) = E[E(vtyj|Ft−1)] = E[yjE(vt|Ft−1)] = 0,
j < t.
--- page 589 ---

562
state-space models and kalman ﬁlter
Thus, as expected, the 1-step-ahead forecast error is uncorrelated (hence, independent) with yj for j < t. Furthermore, for the linear model in Eqs. (11.1) and (11.2),
µt|t = E(µt|Ft) = E(µt|Ft−1, vt) and t|t = Var(µt|Ft) = Var(µt|Ft−1, vt). In
other words, the information set Ft can be written as Ft = {Ft−1, yt} = {Ft−1, vt}.
The following properties of multivariate normal distribution are useful in studying the Kalman ﬁlter under normality. They can be shown via the multivariate linear
regression method or factorization of the joint density. See, also, Appendix B of
Chapter 8. For random vectors w and m, denote the mean vectors and covariance
matrix as E(w) = µw, E(m) = µm, and Cov(m, w) = mw, respectively.
Theorem 11.1.
Suppose that x, y, and z are three random vectors such that
their joint distribution is multivariate normal. In addition, assume that the diagonal block covariance matrix ww is nonsingular for w = x, y, z, and yz = 0.
Then,
1. E(x|y) = µx + xy−1
yy (y −µy).
2. Var(x|y) = xx−xx−1
yy yx.
3. E(x|y, z) = E(x|y) + xz−1
zz (z −µz).
4. Var(x|y, z) = Var(x|y) −xz−1
zz zx.
11.1.2
Kalman Filter
The goal of the Kalman ﬁlter is to update knowledge of the state variable recursively when a new data point becomes available. That is, knowing the conditional
distribution of µt given Ft−1 and the new data yt, we would like to obtain the conditional distribution of µt given Ft, where, as before, Fj = {y1, . . . , yj}. Since Ft
= {Ft−1, vt}, giving yt and Ft−1 is equivalent to giving vt and Ft−1. Consequently,
to derive the Kalman ﬁlter, it sufﬁces to consider the joint conditional distribution
of (µt, vt)′ given Ft−1 before applying Theorem 11.1.
The conditional distribution of vt given Ft−1 is normal with mean zero and
variance given in Eq. (11.8), and that of µt given Ft−1 is also normal with mean
µt|t−1 and variance t|t−1. Furthermore, the joint distribution of (µt, vt)′ given
Ft−1 is also normal. Thus, what remains to be solved is the conditional covariance
between µt and vt given Ft−1. From the deﬁnition,
Cov(µt, vt|Ft−1) = E(µtvt|Ft−1) = E[µt(yt −µt|t−1)|Ft−1]
[by Eq. (11.7)]
= E[µt(µt + et −µt|t−1)|Ft−1]
= E[µt(µt −µt|t−1)|Ft−1] + E(µtet|Ft−1)
= E[(µt −µt|t−1)2|Ft−1] = Var(µt|Ft−1) = t|t−1,
(11.9)
where we have used the fact that E[µt|t−1(µt −µt|t−1)|Ft−1] = 0. Putting the
results together, we have
--- page 590 ---

local trend model
563

 µt
vt

Ft−1
∼N

 µt|t−1
0

,

 t|t−1
t|t−1
t|t−1
Vt

.
By Theorem 11.1, the conditional distribution of µt given Ft is normal with mean
and variance
µt|t = µt|t−1 + t|t−1vt
Vt
= µt|t−1 + Ktvt,
(11.10)
t|t = t|t−1 −
2
t|t−1
Vt
= t|t−1(1 −Kt),
(11.11)
where Kt = t|t−1/Vt is commonly referred to as the Kalman gain, which is the
regression coefﬁcient of µt on vt. From Eq. (11.10), Kalman gain is the factor that
governs the contribution of the new shock vt to the state variable µt.
Next, one can make use of the knowledge of µt given Ft to predict µt+1 via
Eq. (11.2). Speciﬁcally, we have
µt+1|t = E(µt + ηt|Ft) = E(µt|Ft) = µt|t,
(11.12)
t+1|t = Var(µt+1|Ft) = Var(µt|Ft) + Var(ηt) = t|t + σ 2
η .
(11.13)
Once the new data yt+1 is observed, one can repeat the above procedure to update
knowledge of µt+1. This is the famous Kalman ﬁlter algorithm proposed by Kalman
(1960).
In summary, putting Eqs. (11.7) and (11.13) together and conditioning on the
initial assumption that µ1 is distributed as N(µ1|0, 1|0), the Kalman ﬁlter for the
local trend model is as follows:
vt = yt −µt|t−1,
Vt = t|t−1 + σ 2
e ,
Kt = t|t−1/Vt,
(11.14)
µt+1|t = µt|t−1 + Ktvt,
t+1|t = t|t−1(1 −Kt) + σ 2
η ,
t = 1, . . . , T.
There are many ways to derive the Kalman ﬁlter. We use Theorem 11.1, which
describes some properties of multivariate normal distribution, for its simplicity. In
practice, the choice of initial values 1|0 and µ1|0 requires some attention and we
shall discuss it later in Section 11.1.6. For the local trend model in Eqs. (11.1) and
(11.2), the two parameters σe and ση can be estimated via the maximum-likelihood
method. Again, the Kalman ﬁlter is useful in evaluating the likelihood function of
the data in estimation. We shall discuss estimation in Section 11.1.7.
