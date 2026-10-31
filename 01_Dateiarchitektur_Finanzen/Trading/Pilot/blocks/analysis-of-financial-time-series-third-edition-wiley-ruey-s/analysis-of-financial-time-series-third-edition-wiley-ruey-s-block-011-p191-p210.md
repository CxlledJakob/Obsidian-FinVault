# Analysis of Financial Time Series, Third Edition (Wiley -- Ruey S_ Tsay -- Wiley series in probability and statistics, 3rd ed_, -- John Wiley & Sons, -- isbn13 9780470414354 -- 9f99b80c7b2dedd477f463dc5323f3b6 -- An.pdf — pages 191–210

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
--- page 192 ---

kurtosis of garch models
165
3.16
KURTOSIS OF GARCH MODELS
Uncertainty in volatility estimation is an important issue, but it is often overlooked. To assess the variability of an estimated volatility, one must consider the
kurtosis of a volatility model. In this section, we derive the excess kurtosis of a
GARCH(1,1) model. The same idea applies to other GARCH models, however.
The model considered is
at = σtϵt,
σ 2
t = α0 + α1a2
t−1 + β1σ 2
t−1,
where α0 > 0, α1 ≥0, β1 ≥0, α1 + β1 < 1, and {ϵt} is an iid sequence satisfying
E(ϵt) = 0,
Var(ϵt) = 1,
E(ϵ4
t ) = Kϵ + 3,
where Kϵ is the excess kurtosis of the innovation ϵt. Based on the assumption, we
have the following:
• Var(at) = E(σ 2
t ) = α0/[1 −(α1 + β1)].
• E(a4
t ) = (Kϵ + 3)E(σ 4
t ) provided that E(σ 4
t ) exists.
Taking the square of the volatility model, we have
σ 4
t = α2
0 + α2
1a4
t−1 + β2
1σ 4
t−1 + 2α0α1a2
t−1 + 2α0β1σ 2
t−1 + 2α1β1σ 2
t−1a2
t−1.
Taking expectation of the equation and using the two properties mentioned earlier,
we obtain
E(σ 4
t ) =
α2
0(1 + α1 + β1)
[1 −(α1 + β1)][1 −α2
1(Kϵ + 2) −(α1 + β1)2],
provided that 1 > α1 + β1 ≥0 and 1 −α2
1(Kϵ + 2) −(α1 + β1)2 > 0. The excess
kurtosis of at, if it exists, is then
Ka =
E(a4
t )
[E(a2
t )]2 −3
=
(Kϵ + 3)[1 −(α1 + β1)2]
1 −2α2
1 −(α1 + β1)2 −Kϵα2
1
−3.
This excess kurtosis can be written in an informative expression. First, consider
the case that ϵt is normally distributed. In this case, Kϵ = 0, and some algebra
shows that
K(g)
a
=
6α2
1
1 −2α2
1 −(α1 + β1)2 ,
--- page 193 ---

166
conditional heteroscedastic models
where the superscript (g) is used to denote Gaussian distribution. This result has
two important implications: (a) the kurtosis of at exists if 1 −2α2
1 −(α1 + β1)2 > 0,
and (b) if α1 = 0, then K(g)
a
= 0, meaning that the corresponding GARCH(1,1)
model does not have heavy tails.
Second, consider the case that ϵt is not Gaussian. Using the prior result, we
have
Ka = Kϵ −Kϵ(α1 + β1) + 6α2
1 + 3Kϵα2
1
1 −2α2
1 −(α1 + β1)2 −Kϵα2
1
= Kϵ[1 −2α2
1 −(α1 + β1)2] + 6α2
1 + 5Kϵα2
1
1 −2α2
1 −(α1 + β1)2 −Kϵα2
1
= Kϵ + K(g)
a
+ 5
6KϵK(g)
a
1 −1
6KϵK(g)
a
.
This result was obtained originally by George C. Tiao; see Bai, Russell, and Tiao
(2003). It holds for all GARCH models provided that the kurtosis exists. For
instance, if β1 = 0, then the model reduces to an ARCH(1) model. In this case, it
is easy to verify that K(g)
a
= 6α2
1/(1 −3α2
1) provided that 1 > 3α2
1 and the excess
kurtosis of at is
Ka = (Kϵ + 3)(1 −α2
1)
1 −(Kϵ + 3)α2
1
−3 = Kϵ + 2Kϵα2
1 + 6α2
1
1 −3α2
1 −Kϵα2
1
= Kϵ(1 −3α2
1) + 6α2
1 + 5Kϵα2
1
1 −3α2
1 −Kϵα2
1
= Kϵ + K(g)
a
+ 5
6KϵK(g)
a
1 −1
6KϵK(g)
a
.
The prior result shows that for a GARCH(1,1) model the coefﬁcient α1 plays
a critical role in determining the tail behavior of at. If α1 = 0, then K(g)
a
= 0
and Ka = Kϵ. In this case, the tail behavior of at is similar to that of the standardized noise ϵt. Yet if α1 > 0, then K(g)
a
> 0 and the at process has heavy
tails.
For a (standardized) Student-t distribution with v degrees of freedom, we have
E(ϵ4
t ) = 6/(v −4) + 3 if v > 4. Therefore, the excess kurtosis of ϵt is Kϵ =
6/(v −4) for v > 4. This is part of the reason that we used t5 in the chapter when
the degrees of freedom of a t-distribution are prespeciﬁed. The excess kurtosis
of at becomes Ka = [6 + (v + 1)K(g)
a ]/[v −4 −K(g)
a ] provided that 1 −2α2
1(v −
1)/(v −4) −(α1 + β1)2 > 0.
--- page 194 ---

appendix: some rats programs for estimating volatility models
167
APPENDIX: SOME RATS PROGRAMS FOR ESTIMATING VOLATILITY
MODELS
The data ﬁle used in the illustration is sp500.txt, which contains the monthly
excess returns of the S&P 500 index with 792 observations. Comments in a RATS
program start with *.
A Gaussian GARCH(1,1) Model with a Constant Mean Equation
all 0
792:1
open data sp500.txt
data(org=obs) / rt
*** initialize the conditional variance function
set h = 0.0
*** specify the parameters of the model
nonlin mu a0 a1 b1
*** specify the mean equation
frml at = rt(t)-mu
*** specify the volatility equation
frml gvar = a0+a1*at(t-1)**2+b1*h(t-1)
*** specify the log likelihood function
frml garchln = -0.5*log(h(t)=gvar(t))-0.5*at(t)**2/h(t)
*** sample period used in estimation
smpl 2 792
*** initial estimates
compute a0 = 0.01, a1 = 0.1, b1 = 0.5, mu = 0.1
maximize(method=bhhh,recursive,iterations=150) garchln
set fv = gvar(t)
set resid = at(t)/sqrt(fv(t))
set residsq = resid(t)*resid(t)
*** Checking standardized residuals
cor(qstats,number=20,span=10) resid
*** Checking squared standardized residuals
cor(qstats,number=20,span=10) residsq
A GARCH(1,1) Model with Student-t Innovation
all 0
792:1
open data sp500.txt
data(org=obs) / rt
set h = 0.0
nonlin mu a0 a1 b1 v
frml at = rt(t)-mu
frml gvar = a0+a1*at(t-1)**2+b1*h(t-1)
frml tt = at(t)**2/(h(t)=gvar(t))
frml tln = %LNGAMMA((v+1)/2.)-%LNGAMMA(v/2.)-0.5*log(v-2.)
frml gln = tln-((v+1)/2.)*log(1.0+tt(t)/(v-2.0))-0.5*log(h(t))
smpl
2 792
--- page 195 ---

168
conditional heteroscedastic models
compute a0 = 0.01, a1 = 0.1, b1 = 0.5, mu = 0.1, v = 10
maximize(method=bhhh,recursive,iterations=150) gln
set fv = gvar(t)
set resid = at(t)/sqrt(fv(t))
set residsq = resid(t)*resid(t)
cor(qstats,number=20,span=10) resid
cor(qstats,number=20,span=10) residsq
An AR(1)−EGARCH(1,1) Model for Monthly Log Returns of IBM Stock
all 0
864:1
open data m-ibm.txt
data(org=obs) / rt
set h = 0.0
nonlin c0 p1 th ga a0 a1
frml at = rt(t)-c0-p1*rt(t-1)
frml epsi = at(t)/(sqrt(exp(h(t))))
frml g = th*epsi(t)+ga*(abs(epsi(t))-sqrt(2./% PI))
frml gvar = a1*h(t-1)+(1-a1)*a0+g(t-1)
frml garchln = -0.5*(h(t)=gvar(t))-0.5*epsi(t)**2
smpl 3
864
compute c0 = 0.01, p1 = 0.01, th = 0.1, ga = 0.1
compute a0 = 0.01, a1 = 0.5
maximize(method=bhhh,recursive,iterations=150) garchln
set fv = gvar(t)
set resid = epsi(t)
set residsq = resid(t)*resid(t)
cor(qstats,number=20,span=10) resid
cor(qstats,number=20,span=10) residsq
EXERCISES
3.1. Derive multistep-ahead forecasts for a GARCH(1,2) model at the forecast
origin h.
3.2. Derive multistep-ahead forecasts for a GARCH(2,1) model at the forecast
origin h.
3.3. Suppose that r1, . . . , rn are observations of a return series that follows the
AR(1)-GARCH(1,1) model
rt = µ + φ1rt−1 + at,
at = σtϵt,
σ 2
t = α0 + α1a2
t−1 + β1σ 2
t−1,
where ϵt is a standard Gaussian white noise series. Derive the conditional
log-likelihood function of the data.
3.4. In the equation in Exercise 3.3, assume that ϵt follows a standardized Studentt distribution with v degrees of freedom. Derive the conditional log-likelihood
function of the data.
--- page 196 ---

exercises
169
3.5. Consider the monthly simple returns of Intel stock from January 1973 to
December 2008 in m-intc7308.txt. Transform the returns into log returns.
Build a GARCH model for the transformed series and compute 1-stepto
5-step-ahead volatility forecasts at the forecast origin December 2008.
3.6. The ﬁle m-mrk4608.txt contains monthly simple returns of Merck stock
from June 1946 to December 2008. The ﬁle has two columns denoting date
and simple return. Transform the simple returns to log returns.
(a) Is there any evidence of serial correlations in the log returns? Use autocorrelations and 5% signiﬁcance level to answer the question. If yes,
remove the serial correlations.
(b) Is there any evidence of ARCH effects in the log returns? Use the residual series if there are serial correlations in part (a). Use Ljung–Box
statistics for the squared returns (or residuals) with 6 and 12 lags of
autocorrelations and 5% signiﬁcance level to answer the question.
(c) Identify an ARCH model for the data and ﬁt the identiﬁed model. Write
down the ﬁtted model.
3.7. The ﬁle m-3m4608.txt contains two columns. They are date and the
monthly simple return for 3M stock. Transform the returns to log returns.
(a) Is there any evidence of ARCH effects in the log returns? Use Ljung–Box
statistics with 6 and 12 lags of autocorrelations and 5% signiﬁcance level
to answer the question.
(b) Use the PACF of the squared returns to identify an ARCH model. What
is the ﬁtted model?
(c) There are 755 data points. Reﬁt the model using the ﬁrst 750 observations
and use the ﬁtted model to predict the volatilities for t from 751 to 755
(the forecast origin is 750).
(d) Build an ARCH-M model for the log return series of 3M stock. Test the
hypothesis that the risk premium is zero at the 5% signiﬁcance level.
Draw your conclusion.
(e) Build an EGARCH model for the log return series of 3M stock using
the ﬁrst 750 observations. Use the ﬁtted model to compute 1-stepto
5-step-ahead volatility forecasts at the forecast origin h = 750.
3.8. The ﬁle m-gmsp5008.txt contains the dates and monthly simple returns of
General Motors stock and the S&P 500 index from 1950 to 2008.
(a) Build a GARCH model with Gaussian innovations for the log returns of
GM stock. Check the model and write down the ﬁtted model.
(b) Build a GARCH-M model with Gaussian innovations for the log returns
of GM stock. What is the ﬁtted model?
(c) Build a GARCH model with Student-t distribution for the log returns
of GM stock, including estimation of the degrees of freedom. Write
--- page 197 ---

170
conditional heteroscedastic models
down the ﬁtted model. Let v be the degrees of freedom of the Student-t
distribution. Test the hypothesis H0 : v = 6 versus Ha : v̸ = 6, using the
5% signiﬁcance level.
(d) Build an EGARCH model for the log returns of GM stock. What is the
ﬁtted model?
(e) Obtain 1-stepto 6-step-ahead volatility forecasts for all the models
obtained. Compare the forecasts.
3.9. Consider the monthly log returns of GM stock in m-gmsp5008.txt. Build
an adequate TGARCH model for the series. Write down the ﬁtted model and
test for the signiﬁcance of the leverage effect. Obtain 1-stepto 6-steps-ahead
volatility forecasts.
3.10. Again, consider the returns in m-gmsp5008.txt.
(a) Build a Gaussian GARCH model for the monthly log returns of the S&P
500 index. Check the model carefully.
(b) Is there a summer effect on the volatility of the index return? Use the
GARCH model built in part (a) to answer this question.
(c) Are lagged returns of GM stock useful in modeling the index volatility? Again, use the GARCH model of part (a) as a baseline model for
comparison.
3.11. The ﬁle d-gmsp9908.txt contains the daily simple returns of GM stock and
the S&P composite index from 1999 to 2008. It has three columns denoting
date, GM return, and S&P return.
(a) Compute the daily log returns of GM stock. Is there any evidence of
ARCH effects in the log returns? You may use 10 lags of the squared
returns and 5% signiﬁcance level to perform the test.
(b) Compute the PACF of the squared log returns (10 lags).
(c) Specify a GARCH model for the GM log return using a normal distribution for the innovations. Perform model checking and write down the
ﬁtted model.
(d) Find an adequate GARCH model for the series but using the generalized
error distribution for the innovations. Write down the ﬁtted model.
3.12. Consider the daily simple returns of the S&P composite index in the ﬁle
d-gmsp9908.txt.
(a) Is there any ARCH effect in the simple return series? Use 10 lags of the
squared returns and 5% signiﬁcance level to perform the test.
(b) Build an adequate GARCH model for the simple return series.
(c) Compute 1-stepto 4-step-ahead forecasts of the simple return and its
volatility based on the ﬁtted model.
3.13. Again, consider the daily simple returns of GM stock in the ﬁle
d-gmsp9908.txt.
--- page 198 ---

references
171
(a) Find an adequate GARCH-M model for the series. Write down the ﬁtted
model.
(b) Find an adequate EGARCH model for the series. Is the “leverage” effect
signiﬁcant at the 5% level?
3.14. Revisit the ﬁle d-gmsp9908.txt. However, we shall investigate the value
of using market volatility in modeling volatility of individual stocks. Convert
the two simple return series into percentage log return series.
(a) Build an AR(5)–GARCH(1,1) model with generalized error distribution
for the log S&P returns. The AR(5) contains only lags 3 and 5. Denote
the ﬁtted volatility series by spvol.
(b) Estimate a GARCH(1,1) model with spvol as an exogenous variable to
the log GM return series. Check the adequacy of the model, and write
down the ﬁtted model. In S-Plus, the command is
fit = garch(gm ∼1, ∼garch(1,1)+spvol, cond.dist=’ged’)
(c) Discuss the implication of the ﬁtted model.
3.15. Again, consider the percentage daily log returns of GM stock and the S&P
500 index from 1999 to 2008 as before, but we shall investigate whether
the volatility of GM stock has any contribution in modeling the S&P index
volatility. Follow the steps below to perform the analysis.
(a) Fit a GARCH(1,1) model with generalized error distribution to the percentage log returns of GM stock. Denote the ﬁtted volatility by gmvol.
Build an adequate GARCH model plus gmvol as the exogenous variable
for the log S&P return series. Write down the ﬁtted model.
(b) Is the volatility of GM stock returns helpful in modeling the volatility
of the S&P index returns? Why?
REFERENCES
Alizadeh, S., Brandt, M., and Diebold, F. X. (2002). Range-based estimation of stochastic
volatility models. Journal of Finance 57: 1047–1092.
Andersen, T. G. and Bollerslev, T. (1998). Answering the skeptics: Yes, standard volatility
models do provide accurate forecasts. International Economic Review 39: 885–905.
Andersen, T. G., Bollerslev, T., Diebold, F. X., and Labys, P. (2001a). The distribution of
realized exchange rate volatility. Journal of the American Statistical Association 96:
42–55.
Andersen, T. G., Bollerslev, T., Diebold, F. X., and Labys, P. (2001b). The distribution of
realized stock return volatility. Journal of Financial Economics 61: 43–76.
Bai, X., Russell, J. R., and Tiao, G. C. (2003). Kurtosis of GARCH and stochastic volatility
models with non-normal innovations. Journal of Econometrics 114: 349–360.
--- page 199 ---

172
conditional heteroscedastic models
Bai, X., Russell, J. R., and Tiao, G. C. (2004). Effects of non-normality and dependence
on the precision of variance estimates using high-frequency ﬁnancial data. Revised
working paper, Graduate School of Business, University of Chicago.
Barndorff-Nielsen, O. E. and Shephard, N. (2004). Power and bi-power variations with
stochastic volatility and jumps (with discussion). Journal of Financial Econometrics 2:
1–48.
Bollerslev, T. (1986). Generalized autoregressive conditional heteroskedasticity. Journal of
Econometrics 31: 307–327.
Bollerslev, T. and Jubinski, D. (1999). Equality trading volume and volatility: Latent information arrivals and common long-run dependencies. Journal of Business & Economic
Statistics 17: 9–21.
Bollerslev, T., Chou, R. Y., and Kroner, K. F. (1992). ARCH modeling in ﬁnance. Journal
of Econometrics 52: 5–59.
Bollerslev, T., Engle, R. F., and Nelson, D. B. (1994). ARCH model. In R. F. Engle and D.
C. McFadden (eds.). Handbook of Econometrics IV , pp. 2959–3038. Elsevier Science,
Amsterdam.
Breidt, F. J., Crato, N., and de Lima, P. (1998). On the detection and estimation of long
memory in stochastic volatility. Journal of Econometrics 83: 325–348.
Cao, C. and Tsay, R. S. (1992). Nonlinear time series analysis of stock volatilities. Journal
of Applied Econometrics 7: s165–s185.
Ding, Z., Granger, C. W. J., and Engle, R. F. (1993). A long memory property of stock
returns and a new model. Journal of Empirical Finance 1: 83–106.
Engle, R. F. (1982). Autoregressive conditional heteroscedasticity with estimates of the
variance of United Kingdom inﬂations. Econometrica 50: 987–1007.
Fern´andez, C. and Steel, M. F. J. (1998). On Bayesian modelling of fat tails and skewness.
Journal of the American Statistical Association 93: 359–371.
French, K. R., Schwert, G. W., and Stambaugh, R. F. (1987). Expected stock returns and
volatility. Journal of Financial Economics 19: 3–29.
Garman, M. B. and Klass, M. J. (1980). On the estimation of security price volatilities from
historical data. Journal of Business 53: 67–78.
Glosten, L. R., Jagannathan, R., and Runkle, D. E. (1993). On the relation between the
expected value and the volatility of nominal excess return on stocks. Journal of Finance
48: 1779–1801.
Harvey, A. C., Ruiz, E., and Shephard, N. (1994). Multivariate stochastic variance models.
Review of Economic Studies 61: 247–264.
Jacquier, E., Polson, N. G., and Rossi, P. (1994). Bayesian analysis of stochastic volatility
models (with discussion). Journal of Business & Economic Statistics 12: 371–417.
Lambert, P. and Laurent, S. (2001). Modelling ﬁnancial time series using GARCH-type
models and a skewed Student density. Working paper, Universit´e de Li`ege.
McLeod, A. I. and Li, W. K. (1983). Diagnostic checking ARMA time series models using
squared-residual autocorrelations. Journal of Time Series Analysis 4: 269–273.
Melino, A. and Turnbull, S. M. (1990). Pricing foreign currency options with stochastic
volatility. Journal of Econometrics 45: 239–265.
Nelson, D. B. (1990). Stationarity and persistence in the GARCH(1,1) model. Econometric
Theory 6: 318–334.
--- page 200 ---

references
173
Nelson, D. B. (1991). Conditional heteroskedasticity in asset returns: A new approach.
Econometrica 59: 347–370.
Nicholls, D. F. and Quinn, B. G. (1982). Random Coefﬁcient Autoregressive Models: An
Introduction, Lecture Notes in Statistics, 11. Springer, New York.
Parkinson, M. (1980). The extreme value method for estimating the variance of the rate of
return. Journal of Business 53: 61–65.
Ray, B. K. and Tsay, R. S. (2000). Long-range dependence in daily stock volatilities. Journal
of Business & Economic Statistics 18: 254–262.
Rogers, L. C. G. and Satchell, S. E. (1991). Estimating variance from high, low and closing
prices. Annals of Applied Probability 1: 504–512.
Taylor, S. J. (1994). Modeling stochastic volatility: A review and comparative study. Mathematical Finance 4: 183–204.
Tong, H. (1978). On a threshold model. In C. H. Chen (Ed.). Pattern Recognition and Signal
Processing. Sijhoff & Noordhoff, Amsterdam.
Tong, H. (1990). Non-Linear Time Series: A Dynamical System Approach. Oxford University
Press, Oxford, UK.
Tsay, R. S. (1987). Conditional heteroscedastic time series models. Journal of the American
Statistical Association, 82: 590–604.
Yang, D. and Zhang, Q. (2000). Drift-independent volatility estimation based on high, low,
open, and close prices. Journal of Business 73: 477–491.
Zakoian, J. M. (1994). Threshold heteroscedastic models. Journal of Economic Dynamics
and Control 18: 931–955.
--- page 201 ---
--- page 202 ---

C H A P T E R
4
Nonlinear Models
and Their Applications
This chapter focuses on nonlinearity in ﬁnancial data and nonlinear econometric
models useful in analysis of ﬁnancial time series. Consider a univariate time series
xt, which, for simplicity, is observed at equally spaced time points. We denote
the observations by {xt|t = 1, . . . , T }, where T is the sample size. As stated in
Chapter 2, a purely stochastic time series xt is said to be linear if it can be written as
xt = µ +
∞

i=0
ψiat−i,
(4.1)
where µ is a constant, ψi are real numbers with ψ0 = 1, and {at} is a sequence of
independent and identically distributed (iid) random variables with a well-deﬁned
distribution function. We assume that the distribution of at is continuous and
E(at) = 0. In many cases, we further assume that Var(at) = σ 2
a or, even stronger,
that at is Gaussian. If σ 2
a
∞
i=1 ψ2
i < ∞, then xt is weakly stationary (i.e., the ﬁrst
two moments of xt are time invariant). The ARMA process of Chapter 2 is linear
because it has an MA representation in Eq. (4.1). Any stochastic process that does
not satisfy the condition of Eq. (4.1) is said to be nonlinear. The prior deﬁnition
of nonlinearity is for purely stochastic time series. One may extend the deﬁnition
by allowing the mean of xt to be a linear function of some exogenous variables,
including the time index and some periodic functions. But such a mean function
can be handled easily by the methods discussed in Chapter 2, and we do not discuss
it here. Mathematically, a purely stochastic time series model for xt is a function
of an iid sequence consisting of the current and past shocks—that is,
xt = f (at, at−1, . . .).
(4.2)
Analysis of Financial Time Series, Third Edition, By Ruey S. Tsay
Copyright 2010 John Wiley & Sons, Inc.
175
--- page 203 ---

176
nonlinear models and their applications
The linear model in Eq. (4.1) says that f (·) is a linear function of its arguments.
Any nonlinearity in f (·) results in a nonlinear model. The general nonlinear model
in Eq. (4.2) is not directly applicable because it contains too many parameters.
To put nonlinear models available in the literature in a proper perspective, we
write the model of xt in terms of its conditional moments. Let Ft−1 be the σ
ﬁeld generated by available information at time t −1 (inclusive). Typically, Ft−1
denotes the collection of linear combinations of elements in {xt−1, xt−2, . . .} and
{at−1, at−2, . . .}. The conditional mean and variance of xt given Ft−1 are
µt = E(xt|Ft−1) ≡g(Ft−1),
σ 2
t = Var(xt|Ft−1) ≡h(Ft−1),
(4.3)
where g(·) and h(·) are well-deﬁned functions with h(·) > 0. Thus, we restrict the
model to
xt = g(Ft−1) +

h(Ft−1)ϵt,
where ϵt = at/σt is a standardized shock (or innovation). For the linear series xt
in Eq. (4.3), g(·) is a linear function of elements of Ft−1 and h(·) = σ 2
a . The
development of nonlinear models involves making extensions of the two equations
in Eq. (4.3). If g(·) is nonlinear, xt is said to be nonlinear in mean. If h(·) is time
variant, then xt is nonlinear in variance. The conditional heteroscedastic models of
Chapter 3 are nonlinear in variance because their conditional variances σ 2
t evolve
over time. In fact, except for the GARCH-M models, in which µt depends on σ 2
t
and hence also evolves over time, all of the volatility models of Chapter 3 focus
on modiﬁcations or extensions of the conditional variance equation in Eq. (4.3).
Based on the well-known Wold decomposition, a weakly stationary and purely
stochastic time series can be expressed as a linear function of uncorrelated shocks.
For stationary volatility series, these shocks are uncorrelated but dependent. The
models discussed in this chapter represent another extension to nonlinearity derived
from modifying the conditional mean equation in Eq. (4.3).
Many nonlinear time series models have been proposed in the statistical literature, such as the bilinear models of Granger and Andersen (1978), the threshold
autoregressive (TAR) model of Tong (1978), the state-dependent model of Priestley (1980), and the Markov switching model of Hamilton (1989). The basic idea
underlying these nonlinear models is to let the conditional mean µt evolve over
time according to some simple parametric nonlinear function. Recently, a number
of nonlinear models have been proposed by making use of advances in computing facilities and computational methods. Examples of such extensions include the
nonlinear state-space modeling of Carlin, Polson, and Stoffer (1992), the functional
coefﬁcient autoregressive model of Chen and Tsay (1993a), the nonlinear additive
autoregressive model of Chen and Tsay (1993b), and the multivariate adaptive
regression spline of Lewis and Stevens (1991). The basic idea of these extensions
is either using simulation methods to describe the evolution of the conditional distribution of xt or using data-driven methods to explore the nonlinear characteristics
of a series. Finally, nonparametric and semiparametric methods such as kernel
--- page 204 ---

nonlinear models
177
regression and artiﬁcial neural networks have also been applied to explore the nonlinearity in a time series. We discuss some nonlinear models in Section 4.1 that
are applicable to ﬁnancial time series. The discussion includes some nonparametric
and semiparametric methods.
Apart from the development of various nonlinear models, there is substantial
interest in studying test statistics that can discriminate linear series from nonlinear
ones. Both parametric and nonparametric tests are available. Most parametric tests
employ either the Lagrange multiplier or likelihood ratio statistics. Nonparametric
tests depend on either higher order spectra of xt or the concept of dimension
correlation developed for chaotic time series. We review some nonlinearity tests
in Section 4.2. Sections 4.3 and 4.4 discuss modeling and forecasting of nonlinear
models. Finally, an application of nonlinear models is given in Section 4.5.
4.1
NONLINEAR MODELS
Most nonlinear models developed in the statistical literature focus on the conditional
mean equation in Eq. (4.3); see Priestley (1988) and Tong (1990) for summaries
of nonlinear models. Our goal here is to introduce some nonlinear models that are
applicable to ﬁnancial time series.
4.1.1
Bilinear Model
The linear model in Eq. (4.1) is simply the ﬁrst-order Taylor series expansion of
the f (·) function in Eq. (4.2). As such, a natural extension to nonlinearity is to
employ the second-order terms in the expansion to improve the approximation.
This is the basic idea of bilinear models, which can be deﬁned as
xt = c +
p

i=1
φixt−i −
q

j=1
θjat−j +
m

i=1
s

j=1
βijxt−iat−j + at,
(4.4)
where p, q, m, and s are nonnegative integers. This model was introduced by
Granger and Andersen (1978) and has been widely investigated. Subba Rao and
Gabr (1984) discuss some properties and applications of the model, and Liu and
Brockwell (1988) study general bilinear models. Properties of bilinear models such
as stationarity conditions are often derived by (a) putting the model in a statespace form (see Chapter 11) and (b) using the state transition equation to express
the state as a product of past innovations and random coefﬁcient vectors. A special
generalization of the bilinear model in Eq. (4.4) has conditional heteroscedasticity.
For example, consider the model
xt = µ +
s

i=1
βiat−iat + at,
(4.5)
--- page 205 ---

178
nonlinear models and their applications
where {at} is a white noise series. The ﬁrst two conditional moments of xt are
E(xt|Ft−1) = µ,
Var(xt|Ft−1) =

1 +
s

i=1
βiat−i
2
σ 2
a ,
which are similar to that of the RCA or CHARMA model of Chapter 3.
Example 4.1.
Consider the monthly simple returns of the CRSP equalweighted index from January 1926 to December 2008 for 996 observations.
Denote the series by Rt. The sample PACF of Rt shows signiﬁcant partial
autocorrelations at lags 1 and 3 so that an AR(3) model is used. The squared
series of the AR(3) residuals suggests that the conditional heteroscedasticity might
depend on lags 1, 3, and 8 of the residuals. Therefore, we employ the special
bilinear model
Rt = µ + φ1Rt−1 + φ3Rt−3 + (1 + β1at−1 + β3at−3)at
for the series, where at = β0ϵt with ϵt being an iid series with mean zero and
variance 1. Note that lag 8 is omitted for simplicity. Assuming that the conditional
distribution of at is normal, we use the conditional maximum-likelihood method
and obtain the ﬁtted model
Rt = 0.0114 + 0.167Rt−1 −0.095Rt−3
+ 0.071(1 + 0.377at−1 −0.646at−3)ϵt,
(4.6)
where the standard errors of the parameters are, in the order of appearance, 0.0023,
0.032, 0.027, 0.002, 0.147, and 0.136, respectively. All estimates are signiﬁcantly
different from zero at the 5% level. Deﬁne
ˆϵt = Rt −0.0114 −0.167Rt−1 + 0.095Rt−3
0.071(1 + 0.377ˆat−1 −0.646ˆat−3)
,
where ˆϵt = 0 for t ≤3, as the standardized residual series of the model. The sample
ACF of ˆϵt shows no signiﬁcant serial correlations, but the series is not independent
because the squared series ˆϵ2
t has signiﬁcant serial correlations. The validity of
model (4.6) deserves further investigation. For comparison, we also consider an
AR(3)–ARCH(3) model for the series and obtain
Rt = 0.013 + 0.223Rt−1 + 0.006Rt−2 −0.013Rt−3 + at,
σ 2
t = 0.002 + 0.185a2
t−1 + 0.301a2
t−2 + 0.197a2
t−3,
(4.7)
where all estimates but the coefﬁcients of Rt−2 and Rt−3 are highly signiﬁcant.
The standardized residual series of the model shows no serial correlations, but the
squared residuals show Q(10) = 19.78 with a p value of 0.031. Models (4.6) and
(4.7) appear to be similar, but the latter seems to ﬁt the data better. Further study
shows that an AR(1)–GARCH(1,1) model ﬁts the data well.
--- page 206 ---

nonlinear models
179
4.1.2
Threshold Autoregressive (TAR) Model
This model is motivated by several nonlinear characteristics commonly observed
in practice such as asymmetry in declining and rising patterns of a process. It uses
piecewise linear models to obtain a better approximation of the conditional mean
equation. However, in contrast to the traditional piecewise linear model that allows
for model changes to occur in the “time” space, the TAR model uses threshold
space to improve linear approximation. Let us start with a simple 2-regime AR(1)
model:
xt =

−1.5xt−1 + at
if xt−1 < 0,
0.5xt−1 + at
if xt−1 ≥0,
(4.8)
where the at are iid N(0, 1). Here the threshold variable is xt−1 so that the delay
is 1, and the threshold is 0. Figure 4.1 shows the time plot of a simulated series
of xt with 200 observations. A horizontal line of zero is added to the plot, which
illustrates several characteristics of TAR models. First, despite the coefﬁcient −1.5
in the ﬁrst regime, the process xt is geometrically ergodic and stationary. In fact,
the necessary and sufﬁcient condition for model (4.8) to be geometrically ergodic
is φ(1)
1
< 1, φ(2)
1
< 1, and φ(1)
1 φ(2)
1
< 1, where φ(i)
1
is the AR coefﬁcient of regime
i; see Petruccelli and Woolford (1984) and Chen and Tsay (1991). Ergodicity is
an important concept in time series analysis. For example, the statistical theory
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
••
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
••
•
•••
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
••
••
•
••••••
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
•
•
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
•
••
•••••
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
••
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
•
••
•
••
•
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
•
•
•
•
••
•••
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
Time index
Observations
0
50
100
150
200
−2
0
2
4
Figure 4.1
Time plot of simulated 2-regime TAR(1) series.
--- page 207 ---

180
nonlinear models and their applications
showing that the sample mean ¯x = (T
t=1 xt)/T of xt converges to the mean of xt
is referred to as the ergodic theorem, which can be regarded as the counterpart of
the central limit theory for the iid case. Second, the series exhibits an asymmetric
increasing and decreasing pattern. If xt−1 is negative, then xt tends to switch to a
positive value due to the negative and explosive coefﬁcient −1.5. Yet when xt−1 is
positive, it tends to take multiple time indexes for xt to reduce to a negative value.
Consequently, the time plot of xt shows that regime 2 has more observations than
regime 1, and the series contains large upward jumps when it becomes negative.
The series is therefore not time reversible. Third, the model contains no constant
terms, but E(xt) is not zero. The sample mean of the particular realization is
0.61 with a standard deviation of 0.07. In general, E(xt) is a weighted average
of the conditional means of the two regimes, which are nonzero. The weight for
each regime is simply the probability that xt is in that regime under its stationary
distribution. It is also clear from the discussion that, for a TAR model to have
zero mean, nonzero constant terms in some of the regimes are needed. This is very
different from a stationary linear model for which a nonzero constant implies that
the mean of xt is not zero.
A time series xt is said to follow a k-regime self-exciting TAR (SETAR) model
with threshold variable xt−d if it satisﬁes
xt = φ(j)
0
+ φ(j)
1 xt−1 −· · · −φ(j)
p xt−p + a(j)
t
,
if
γj−1 ≤xt−d < γj,
(4.9)
where k and d are positive integers, j = 1, . . . , k, γi are real numbers such that
−∞= γ0 < γ1 < · · · < γk−1 < γk = ∞, the superscript (j) is used to signify the
regime, and {a(j)
t
} are iid sequences with mean 0 and variance σ 2
j and are mutually
independent for different j. The parameter d is referred to as the delay parameter
and γj are the thresholds. Here it is understood that the AR models are different
for different regimes; otherwise, the number of regimes can be reduced. Equation
(4.9) says that a SETAR model is a piecewise linear AR model in the threshold
space. It is similar in spirit to the usual piecewise linear models in regression
analysis, where model changes occur in the order in which observations are taken.
The SETAR model is nonlinear provided that k > 1.
Properties of general SETAR models are hard to obtain, but some of them
can be found in Tong (1990), Chan (1993), Chan and Tsay (1998), and the references therein. In recent years, there is increasing interest in TAR models and their
applications; see, for instance, Hansen (1997), Tsay (1998), and Montgomery et
al. (1998). Tsay (1989) proposed a testing and modeling procedure for univariate
SETAR models. The model in Eq. (4.9) can be generalized by using a threshold
variable zt that is measurable with respect to Ft−1 (i.e., a function of elements of
Ft−1). The main requirements are that zt is stationary with a continuous distribution
function over a compact subset of the real line and that zt−d is known at time t.
Such a generalized model is referred to as an open-loop TAR model.
Example 4.2.
To demonstrate the application of TAR models, consider the
U.S. monthly civilian unemployment rate, seasonally adjusted and measured in
--- page 208 ---

nonlinear models
181
1950
1960
1970
1980
1990
2000
2010
4
6
8
10
Year
Rate
*
***
********
***
**
***
*
*****
***
*
****
********
*******************
*
*
**
******
*
******
***************
***********
**
*
**
*****
*
****
********
**
*
*******
*
******
***
*********************************
**********************************
**********
*********************************
**
*
*
*
***************************
*********************
*
**************
***********
*
****
***
********************
*******************************************************************************
**********
****************
*************************************************************************************
***
*
**
*
*
*
*
Figure 4.2
Time plot of monthly U.S. civilian unemployment rate, seasonally adjusted, from January
1948 to March 2009.
percentage, from January 1948 to March 2009 for 735 observations. The data
are obtained from the Bureau of Labor Statistics, Department of Labor, and are
shown in Figure 4.2. The plot shows two main characteristics of the data. First,
there appears to be a slow but upward trend in the overall unemployment rate.
Second, the unemployment rate tends to increase rapidly and decrease slowly.
Thus, the series is not time reversible and may not be unit-root stationary,
either.
Because the sample autocorrelation function decays slowly, we employ the ﬁrst
differenced series yt = (1 −B)ut in the analysis, where ut is the monthly unemployment rate. Using univariate ARIMA models, we obtain the model
(1 −1.13B + 0.27B2)(1 −0.51B12)yt = (1 −1.12B + 0.44B2)(1 −0.82B12)at,
(4.10)
where ˆσa = 0.187 and all estimates but the AR(2) coefﬁcient are statistically signiﬁcant at the 5% level. The t ratio of the estimate of AR(2) coefﬁcient is −1.66.
The residuals of model (4.10) give Q(12) = 12.3 and Q(24) = 25.5, respectively.
The corresponding p values are 0.056 and 0.11, respectively, based on χ2 distributions with 6 and 18 degrees of freedom. Thus, the ﬁtted model adequately
describes the serial dependence of the data. Note that the seasonal AR and MA
coefﬁcients are highly signiﬁcant with standard error 0.049 and 0.035, respectively, even though the data were seasonally adjusted. The adequacy of seasonal
adjustment deserves further study. Using model (4.10), we obtain the 1-step-ahead
forecast of 8.8 for the April 2009 unemployment rate, which is close to the actual
data of 8.9.
--- page 209 ---

182
nonlinear models and their applications
To model nonlinearity in the data, we employ TAR models and obtain the
model
yt =

0.083yt−2 + 0.158yt−3 + 0.118yt−4 −0.180yt−12 + a1t
if yt−1 ≤0.1,
0.421yt−2 + 0.239yt−3 −0.127yt−12 + a2t
if yt−1 > 0.1,
(4.11)
where the standard errors of ait are 0.180 and 0.217, respectively, the standard
errors of the AR parameters in regime 1 are 0.046, 0.043, 0.042, and 0.037, whereas
those of the AR parameters in regime 2 are 0.054, 0.057, and 0.075, respectively.
The number of data points in regimes 1 and 2 are 460 and 262, respectively. The
standardized residuals of model (4.11) only shows some minor serial correlation at
lag 12. Based on the ﬁtted TAR model, the dynamic dependence in the data appears
to be stronger when the change in monthly unemployment rate is greater than
0.1%. This is understandable because a substantial increase in the unemployment
rate is indicative of weakening in the U.S. economy, and policy makers might be
more inclined to take action to help the economy, which in turn may affect the
dynamics of the unemployment rate series. Consequently, model (4.11) is capable
of describing the time-varying dynamics of the U.S. unemployment rate.
The MA representation of model (4.10) is
ψ(B) ≈1 + 0.01B + 0.18B2 + 0.20B3 + 0.18B4 + 0.15B5 + · · · .
It is then not surprising to see that no yt−1 term appears in model (4.11).
As mentioned in Chapter 3, threshold models can be used in ﬁnance to handle
the asymmetric responses in volatility between positive and negative returns. The
models can also be used to study arbitrage tradings in index futures and cash prices;
see Chapter 8 on multivariate time series analysis. Here we focus on volatility
modeling and introduce an alternative approach to parameterization of TGARCH
models. In some applications, this new general TGARCH model fares better than
the GJR model of Chapter 3.
Example 4.3.
Consider the daily log returns, in percentage and including
dividends, of IBM stock from July 3, 1962, to December 31, 2003, for 10,446
observations. Figure 4.3 shows the time plot of the series, which is one of the
longer return series analyzed in the book. The volatility seems to be larger in the
latter years of the data. Because general TGARCH models are used in the analysis,
we use the SCA package to perform estimation in this example.
If GARCH models of Chapter 3 are entertained, we obtain the following
AR(2)–GARCH(1,1) model for the series:
rt = 0.062 −0.024rt−2 + at,
at = σtϵt,
σ 2
t = 0.037 + 0.077a2
t−1 + 0.913σ 2
t−1,
(4.12)
where rt is the log return, {ϵt} is a Gaussian white noise sequence with mean
zero and variance 1.0, the standard errors of the parameters in the mean equation
--- page 210 ---

nonlinear models
183
Year
Log return
1970
1980
1990
2000
20
10
0
10
Figure 4.3
Time plot of daily log returns for IBM stock from July 3, 1962, to December 31, 2003.
are 0.015 and 0.010, and those of the volatility equation are 0.004, 0.003, and
0.003, respectively. All estimates are statistically signiﬁcant at the 5% level.
The Ljung–Box statistics of the standardized residuals give Q(10) = 5.19(0.82)
and Q(20) = 24.38(0.18), where the number in parentheses denotes the p value
obtained using χ2
m−1 distribution because of the estimated AR(2) coefﬁcient.
For the squared standardized residuals, we obtain Q(10) = 11.67(0.31) and
Q(20) = 18.25(0.57). The model is adequate in modeling the serial dependence
and conditional heteroscedasticity of the data. But the unconditional mean for
rt of model (4.12) is 0.060, which is substantially larger than the sample mean
0.039, indicating that the model might be misspeciﬁed.
Next, we employ the TGARCH model of Chapter 3 and obtain
rt = 0.014 −0.028rt−2 + at,
at = σtϵt,
σ 2
t = 0.075 + 0.081Pt−1a2
t−1 + 0.157Nt−1a2
t−1 + 0.863σ 2
t−1,
(4.13)
where Pt−1 = 1 −Nt−1, Nt−1 is the indicator for negative at−1 such that Nt−1 = 1
if at−1 < 0 and = 0 otherwise, the standard errors of the parameters in the mean
equation are 0.013 and 0.009, and those of the volatility equation are 0.007,
0.008, 0.010, and 0.010, respectively. All estimates except the constant term of
the mean equation are signiﬁcant. Let ˜at be the standardized residuals of model
(4.13). We have Q(10) = 2.47(0.98) and Q(20) = 25.90(0.13) for the {˜at} series
