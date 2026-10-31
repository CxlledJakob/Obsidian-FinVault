# Analysis of Financial Time Series, Third Edition (Wiley -- Ruey S_ Tsay -- Wiley series in probability and statistics, 3rd ed_, -- John Wiley & Sons, -- isbn13 9780470414354 -- 9f99b80c7b2dedd477f463dc5323f3b6 -- An.pdf — pages 628–647

--- page 628 ---

forecasting
601
11.6
FORECASTING
Suppose that the forecast origin is t and we are interested in predicting yt+j
for j = 1, . . . , h, where h > 0. Also, we adopt the minimum mean-squared error
forecasts. Similar to the ARMA models, the j-step-ahead forecast yt(j) turns out to
be the expected value of yt+j given Ft and the model. That is, yt(j) = E(yt+j|Ft).
In what follows, we show that these forecasts and the covariance matrices of the
associated forecast errors can be obtained via the Kalman ﬁlter in Eq. (11.64) by
treating {yt+1, . . . , yt+h} as missing values, that is, the ﬁrst case in Section 11.5.
Consider the 1-step-ahead forecast. From Eq. (11.27),
yt(1) = E(yt+1|Ft) = ct+1 + Zt+1st+1|t,
where st+1|t is available via the Kalman ﬁlter at the forecast origin t. The associated
forecast error is
et(1) = yt+1 −yt(1) = Zt+1(st+1 −st+1|t) + et+1.
Therefore, the covariance matrix of the 1-step-ahead forecast error is
Var[et(1)] = Zt+1t+1|tZ′
t+1 + H t+1.
This is precisely the covariance matrix V t+1 of the Kalman ﬁlter in Eq. (11.64).
Thus, we have showed the case for h = 1.
Now, for h > 1, we consider 1-stepto h-step-ahead forecasts sequentially. From
Eq. (11.27), the j-step-ahead forecast is
yt(j) = ct+j + Zt+jst+j|t,
(11.83)
and the associated forecast error is
et(j) = Zt+j(st+j −st+j|t) + et+j.
Recall that st+j|t and t+j|t are, respectively, the conditional mean and covariance
matrix of st+j given Ft. The prior equation says that
Var[et(j)] = Zt+jt+j|tZ′
t+j + H t+j.
(11.84)
Furthermore, from Eq. (11.26),
st+j+1|t = dt+j + T t+jst+j|t,
which in turn implies that
st+j+1 −st+j+1|t = T t+j(st+j −st+j|t) + Rt+jηt+j.
--- page 629 ---

602
state-space models and kalman ﬁlter
Consequently,
t+j+1|t = T t+jt+j|tT ′
t+j + Rt+jQt+jR′
t+j.
(11.85)
Note that Var[et(j)] = V t+j and Eqs. (11.83) and (11.85) are the recursion of
the Kalman ﬁlter in Eq. (11.64) for t + j with j = 1, . . . , h when vt+j = 0 and
Kt+j = 0. Thus, the forecast yt(j) and the covariance matrix of its forecast error
et(j) can be obtained via the Kalman ﬁlter with missing values.
Finally, the prediction error series {vt} can be used to evaluate the likelihood
function for estimation and the standardized prediction errors D−1/2
t
vt can be used
for model checking, where Dt = diag{V t(1, 1), . . . , V t(k, k)} with V t(i, i) being
the (i, i)th element of V t.
11.7
APPLICATION
In this section, we consider some applications of the state-space model in ﬁnance
and business. Our objectives are to highlight the applicability of the model and to
demonstrate the practical implementation of the analysis in S-Plus with SsfPack.
Example 11.2.
Consider the CAPM for the monthly simple excess returns of
General Motors (GM) stock from January 1990 to December 2003; see Chapter 9.
We use the simple excess returns of the S&P 500 composite index as the market
returns. The returns are in percentages. Our illustration starts with a simple market
model
rt = α + βrM,t + et,
et ∼N(0, σ 2
e ),
(11.86)
for t = 1, . . . , 168. This is a ﬁxed-coefﬁcient model and can easily be estimated
by the ordinary least-squares (OLS) method. Denote the GM stock return and the
market return by gm and sp, respectively. The result follows:
> da=read.table(‘‘m-gmsp-excess-9003.txt’’,header=F)
> gm=da[,1]
> sp=da[,2]
> fit=OLS(gm∼sp)
> summary(fit)
Call:
OLS(formula = gm∼sp)
Coefficients:
Value Std. Error t value Pr(>|t|)
(Intercept) 0.1982 0.6302
0.3145
0.7535
sp 1.0457 0.1453
7.1962
0.0000
Regression Diagnostics:
--- page 630 ---

application
603
R-Squared 0.2378
Adjusted R-Squared 0.2332
Durbin-Watson Stat 2.0290
Residual Diagnostics:
Stat P-Value
Jarque-Bera
2.5348
0.2816
Ljung-Box 24.2132
0.3362
Residual standard error: 8.13 on 166 degrees of freedom
Thus, the ﬁtted model is
rt = 0.20 + 1.0457rM,t + et,
ˆσe = 8.13.
Based on the residual diagnostics, the model appears to be adequate for the GM
stock returns with adjusted R2 = 23.3%.
As shown in Section 11.3, model (11.86) is a special case of the state-space
model. We then estimate the model using SsfPack. The result is as follows:
> reg.m=function(parm,mX=NULL){
+ parm=exp(parm)
% log(sigma.e) is used to ensure
positiveness.
+ ssf.reg=GetSsfReg(mX)
+ ssf.reg$mOmega[3,3]=parm[1]
+ CheckSsf(ssf.reg)
+ }
> c.start=c(10)
> X.mtx=cbind(rep(1,168),sp)
> reg.fit=SsfFit(c.start,gm,"reg.m",mX=X.mtx)
RELATIVE FUNCTION CONVERGENCE
> names(reg.fit)
[1] "parameters" "objective" "message" "grad.norm"
"iterations"
[6] "f.evals"
"g.evals"
"hessian" "scale"
"aux"
[11] "call"
"vcov"
> sqrt(exp(reg.fit$parameters))
[1] 8.130114
> ssf.reg$mOmega[3,3]=exp(reg.fit$parameters)
> reg.s=SsfMomentEst(gm,ssf.reg,task="STSMO")
> reg.s$state.moment[10,]
state.1
state.2
0.1982025 1.045702
> sqrt(reg.s$state.variance[10,])
state.1
state.2
0.6302091 0.1453139
As expected, the result is in total agreement with that of the OLS method.
--- page 631 ---

604
state-space models and kalman ﬁlter
Finally, we entertain the time-varying CAPM of Section 11.3.1. The estimation
result, including time plot of the smoothed response variable, is given below. The
command SsfCondDens is used to compute the smoothed estimates of the state
vector and observation without variance estimation.
> tv.capm =function(parm,mX=NULL){ %setup model for estimation
+ parm=exp(parm)
%parameterize in log for positiveness.
+ Phi.t = rbind(diag(2),rep(0,2))
+ Omega=diag(parm)
+ JPhi=matrix(-1,3,2)
+ JPhi[3,1]=1
+ JPhi[3,2]=2
+ Sigma=-Phi.t
+ ssf.tv=list(mPhi=Phi.t,
+ mOmega=Omega,
+ mJPhi=JPhi,
+ mSigma=Sigma,
+ mX=mX)
+ CheckSsf(ssf.tv)
+ }
> tv.start=c(0,0,0)
% starting values
> tv.mle=SsfFit(tv.start,gm,"tv.capm",mX=X.mtx)
% estimation
> sigma.mle=sqrt(exp(tv.mle$parameters))
> sigma.mle
[1] 4.907845e-05 1.219885e-02 8.125213e+00
% Smoothing
> smoEst.tv=SsfCondDens(gm,tv.capm(tv.mle$parameters,mX=X.
mtx),
+ task="STSMO")
> names(smoEst.tv)
[1] "state"
"response" "task"
> par(mfcol=c(2,2))
% plotting
> plot(gm,type=’l’,ylab=’excess return’)
> title(main=’(a) Monthly simple excess returns’)
> plot(smoEst.tv$response,type=’l’,ylab=’rtn’)
> title(main=’(b) Expected returns’)
> plot(smoEst.tv$state[,1],type=’l’,ylab=’value’)
> title(main=’(c) Alpha(t)’)
> plot(smoEst.tv$state[,2],type=’l’,ylab=’value’)
> title(main=’(d) Beta(t)’)
Note that estimates of ση and σε are 4.91 × 10−5 and 1.22 × 10−2, respectively.
These estimates are close to zero, indicating that αt and βt of the time-varying
market model are essentially constant for the GM stock returns. This is in agreement
with the fact that the ﬁxed-coefﬁcient market model ﬁts the data well. Figure 11.5
shows some plots for the time-varying CAPM ﬁt. Part (a) is the monthly simple
excess returns of GM stock from January 1990 to December 2003. Part (b) is the
expected returns of GM stock, that is, rt|T , where T = 168 is the sample size. Parts
--- page 632 ---

application
605
Excess return
0
50
100
(a)
(b)
(d)
(c)
150
−20−10 0
10 20
Returns
−15−10 −5
0
5
10
Value
0.20643
0.20643
Value
1.02
1.04
1.06
0
50
100
150
0
50
100
150
0
50
100
150
Figure 11.5
Time plots of some statistics for time-varying CAPM applied to monthly simple excess
returns of General Motors stock. S&P 500 composite index return is used as market return: (a) monthly
simple excess return, (b) expected returns rt|T , (c) αt estimate, and (d) βt estimate.
(c) and (d) are the time plots of the estimates of αt and βt. Given the tightness in
the vertical scale, these two time plots conﬁrm the assertion that a ﬁxed-coefﬁcient
market model is adequate for the monthly GM stock return.
Example 11.3.
In this example we reanalyze the series of quarterly earnings
per share of Johnson & Johnson from 1960 to 1980 using the unobserved component model; see Chapter 2 for details of the data. The model considered is
yt = µt + γt + et,
et ∼N(0, σ 2
e ),
(11.87)
where yt is the logarithm of the observed earnings per share, µt is the local trend
component satisfying
µt+1 = µt + ηt,
ηt ∼N(0, σ 2
η ),
and γt is the seasonal component that satisﬁes
(1 + B + B2 + B3)γt = ωt,
ωt ∼N(0, σ 2
ω),
that is, γt = −3
j=1 γt−j + ωt. This model has three parameters—σe, ση, and
σω —and is a simple unobserved component model. It can be put in a state-space
--- page 633 ---

606
state-space models and kalman ﬁlter
form as


µt+1
γt+1
γt
γt−1

=


1
0
0
0
0
−1
−1
−1
0
1
0
0
0
0
1
0




µt
γt
γt−1
γt−2

+


1
0
0
1
0
0
0
0



 ηt
ωt

,
where the covariance matrix of (ηt, ωt)′ is diag{σ 2
η , σ 2
ω}, and yt = [1, 1, 0, 0]st + et;
see Section 11.3. This is a special case of the structural time series in SsfPack and
can easily be speciﬁed using the command GetSsfStsm. Performing the maximumlikelihood estimation, we obtain (ˆσe, ˆση, ˆσω) = (2.04 × 10−6, 7.27 × 10−2, 2.93 ×
10−2).
> jnj=scan(file=’q-jnj.txt’)
> y=log(jnj)
% Estimation
> jnj.m=function(parm){
+ parm=exp(parm)
+ jnj.sea=GetSsfStsm(irregular=parm[1],level=parm[2],
+ seasonalDummy=c(parm[3],4))
+ CheckSsf(jnj.sea)
+ }
>
> c.start=c(0,0,0)
% Starting values
> jnj.est=SsfFit(c.start,y,"jnj.m")
> names(jnj.est)
[1] "parameters" "objective" "message"
"grad.norm" "iterations"
[6] "f.evals"
"g.evals"
"hessian"
"scale"
"aux"
[11] "call"
> jnjest=exp(jnj.est$parameters)
> jnjest
% estimates
[1] 2.044516e-06 7.269655e-02 2.931691e-02
> jnj.ssf=GetSsfStsm(irregular=jnjest[1],level=jnjest[2],
+ seasonalDummy=c(jnjest[3],4)) % specify the model with estimates
> CheckSsf(jnj.ssf)
$mPhi:
[,1] [,2] [,3] [,4]
[1,]
1
0
0
0
[2,]
0
-1
-1
-1
[3,]
0
1
0
0
[4,]
0
0
1
0
[5,]
1
1
0
0
--- page 634 ---

application
607
$mOmega:
[,1]
[,2] [,3] [,4]
[,5]
[1,] 0.005284788 0.000000000
0
0 0.000000e+00
[2,] 0.000000000 0.000859481
0
0 0.000000e+00
[3,] 0.000000000 0.000000000
0
0 0.000000e+00
[4,] 0.000000000 0.000000000
0
0 0.000000e+00
[5,] 0.000000000 0.000000000
0
0 4.180047e-12
$mSigma:
[,1] [,2] [,3] [,4]
[1,]
-1
0
0
0
[2,]
0
-1
0
0
[3,]
0
0
-1
0
[4,]
0
0
0
-1
[5,]
0
0
0
0
$mDelta:
[,1]
[1,]
0
[2,]
0
[3,]
0
[4,]
0
[5,]
0
$mJPhi:
[1] 0
$mJOmega:
[1] 0
$mJDelta:
[1] 0
$mX:
[1] 0
$cT:
[1] 0
$cX:
[1] 0
$cY:
[1] 1
$cSt:
[1] 4
attr(, "class"):
[1] "ssf"
% below: smoothed components
> jnj.smo=SsfMomentEst(y,jnj.ssf,task="STSMO")
> up1=jnj.smo$state.moment[,1]+
+ 2*sqrt(jnj.smo$state.variance[,1])
> lw1=jnj.smo$state.moment[,1]-
+ 2*sqrt(jnj.smo$state.variance[,1])
> max(up1)
% obtain the range for plotting
--- page 635 ---

608
state-space models and kalman ﬁlter
[1] 2.795702
> min(lw1)
[1] -0.5948943
> up=jnj.smo$state.moment[,2]+
+ 2*sqrt(jnj.smo$state.variance[,2])
> lw=jnj.smo$state.moment[,2]-
+ 2*sqrt(jnj.smo$state.variance[,2])
> max(up)
[1] 0.3788652
> min(lw)
[1] -0.3552441
> par(mfcol=c(2,1)) % plotting
> plot(tdx,jnj.smo$state.moment[,1],type=’l’,xlab=’year’,
+ ylab=’value’,ylim=c(-1,3))
> lines(tdx,up1,lty=2)
> lines(tdx,lw1,lty=2)
> title(main=’(a) Trend component’)
> plot(tdx,jnj.smo$state.moment[,2],type=’l’,xlab=’year’,
+ ylab=’value’,ylim=c(-.5,.5))
> lines(tdx,up,lty=2)
> lines(tdx,lw,lty=2)
> title(main=’(b) Seasonal component’)
% Filtering and smoothing
> jnj.fil=KalmanFil(y,jnj.ssf,task="STFIL")
> jnj.smo1=KalmanSmo(jnj.fil,jnj.ssf)
> plot(tdx,jnj.fil$mOut[,1],type=’l’,xlab=’year’,ylab=’resi’)
> title(main=’(a) 1-Step forecast error’)
> plot(tdx,jnj.smo1$response.residuals[2:85],type=’l’,
+ xlab=’year’,ylab=’resi’)
> title(main=’(b) Smoothing residual’)
Figure 11.6 shows the smoothed estimates of the trend and seasonal components, that is, µt|T and γt|T with T = 84, of the data. Of particular interest is that
the seasonal pattern seems to evolve over time. Also shown are 95% pointwise
conﬁdence regions of the unobserved components. Figure 11.7 shows the residual
plots, where part (a) gives the 1-step-ahead forecast errors computed by Kalman
ﬁlter and part (b) is the smoothed response residuals of the ﬁtted model. Thus,
state-space modeling provides an alternative approach for analyzing seasonal time
series. It should be noted that the estimated components in Figure 11.6 are not
unique. They depend on the model speciﬁed and constraints used. In fact, there
are inﬁnitely many ways to decompose an observed time series into unobserved
components. For instance, one can use a different speciﬁcation for the seasonal
component, for example, sesonalTrig in SsfPack, to obtain another decomposition for the earnings series of Johnson & Johnson. Thus, care must be exercised
in interpreting the estimated components. However, for forecasting purposes, the
choice of decomposition does not matter provided that the chosen one is a valid
decomposition.
--- page 636 ---

exercises
609
Year
(a)
Value
1960
1965
1970
1975
1980
−1
0
1
2
3
Value
−0.4
0.0 0.2 0.4
Year
(b)
1960
1965
1970
1975
1980
Figure 11.6
Smoothed components of ﬁtting model (11.87) to logarithm of quarterly earnings per
share of Johnson & Johnson from 1960 to 1980: (a) trend component and (b) seasonal component.
Dotted lines indicate pointwise 95% conﬁdence regions.
EXERCISES
11.1. Consider
the
ARMA(1,1)
model
yt −0.8yt−1 = at + 0.4at−1
with
at ∼N(0, 0.49). Convert the model into a state-space form using (a)
Akaike’s method, (b) Harvey’s approach, and (c) Aoki’s approach.
11.2. The ﬁle aa-rv-20m.txt contains the realized daily volatility series of Alcoa
stock returns from January 2, 2003, to May 7, 2004; see the example in
Section 11.1. The volatility series is constructed using 20-minute intradaily
log returns.
(a) Fit an ARIMA(0,1,1) model to the log volatility series and write down
the model.
(b) Estimate the local trend model in Eqs. (11.1) and (11.2) for the log
volatility series. What are the estimates of σe and ση? Obtain time plots
for the ﬁltered and smoothed state variables with pointwise 95% conﬁ-
dence interval.
11.3. Consider the monthly simple excess returns of Pﬁzer stock and the S&P 500
composite index from January 1990 to December 2003. The excess returns
are in m-pfesp-ex9003.txt with Pﬁzer stock returns in the ﬁrst column.
--- page 637 ---

610
state-space models and kalman ﬁlter
Year
(a)
Residuals
1960
1965
1970
1975
1980
−0.1 0.0 0.1 0.2 0.3
Residuals
−30
−10 0 10 20 30
Year
(b)
1960
1965
1970
1975
1980
Figure 11.7
Residual series of ﬁtting model (11.87) to logarithm of quarterly earnings per share of
Johnson & Johnson from 1960 to 1980: (a) 1-step-ahead forecast error vt and (b) smoothed residuals
of response variable.
(a) Fit a ﬁxed-coefﬁcient market model to the Pﬁzer stock return. Write
down the ﬁtted model.
(b) Fit a time-varying CAPM to the Pﬁzer stock return. What are the estimated standard errors of the innovations to the αt and βt series? Obtain
time plots of the smoothed estimates of αt and βt.
11.4. Consider the AR(3) model
xt = φ1xt−1 + φ2xt−2 + φ3xt−3 + at,
at ∼N(0, σ 2
a ),
and suppose that the observed data are
yt = xt + et,
et ∼N(0, σ 2
e ),
where {et} and {at} are independent and the initial values of xj with j ≤0
are independent of et and at for t > 0.
(a) Convert the model into a state-space form.
(b) If E(et) = c, which is not zero, what is the corresponding state-space
form for the system?
--- page 638 ---

references
611
11.5. The ﬁle m-ppiaco4709.txt contains year, month, day, and U.S. producer
price index (PPI) from January 1947 to November 2009. The index is for all
commodities and not seasonally adjusted. Let zt = ln(Zt) −ln(Zt−1), where
Zt is the observed monthly PPI. It turns out that an AR(3) model is adequate
for zt if the minor seasonal dependence is ignored. Let yt be the sample
mean-corrected series of zt.
(a) Fit an AR(3) model to yt and write down the ﬁtted model.
(b) Suppose that yt has independent measurement errors so that yt = xt + et,
where xt is a zero-mean AR(3) process and Var(et) = σ 2
e . Use a statespace form to estimate parameters, including the innovational variances
to the state and σ 2
e . Write down the ﬁtted model and obtain a time plot of
the smoothed estimate of xt. Also, show the time plot of ﬁltered response
residuals of the ﬁtted state-space model.
REFERENCES
Akaike, H. (1975). Markovian representation of stochastic processes by canonical variables.
SIAM Journal on Control 13: 162–173.
Aoki, M. (1987). State Space Modeling of Time Series. Springer, New York.
Anderson, B. D. O. and Moore, J. B. (1979). Optimal Filtering. Prentice-Hall, Englewood
Cliffs, NJ.
Chan, N. H. (2002). Time Series: Applications to Finance. Wiley, Hoboken, NJ.
de Jong, P. (1989). Smoothing and interpolation with the state space model. Journal of the
American Statistical Association 84: 1085–1088.
Durbin, J. and Koopman, S. J. (2001). Time Series Analysis by State Space Methods. Oxford
University Press, Oxford, UK.
Hamilton, J. (1994). Time Series Analysis. Princeton University Press, Princeton, NJ.
Harvey, A. C. (1993). Time Series Models, 2nd ed. Harvester Wheatsheaf, Hemel Hempstead,
UK.
Kalman, R. E. (1960). A new approach to linear ﬁltering and prediction problems. Journal
of Basic Engineering, Transactions ASMA, Series D 82: 35–45.
Kim, C. J. and Nelson, C. R. (1999). State Space Models with Regime Switching. Academic,
New York.
Kitagawa, G. and Gersch, W. (1996). Smoothness Priors Analysis of Time Series. Springer,
New York.
Koopman, S. J. (1993). Disturbance smoother for state space models. Biometrika 80:
117–126.
Koopman, S. J., Shephard, N., and Doornik, J. A. (1999). Statistical algorithms for models in
state-space form using SsfPack 2.2. Econometrics Journal 2: 113–166. Also available
at http://www.ssfpack.com/.
Shumway, R. H. and Stoffer, D. S. (2000). Time Series Analysis and Its Applications.
Springer, New York.
West, M. and Harrison, J. (1997). Bayesian Forecasting and Dynamic Models, 2nd ed.
Springer, New York.
--- page 639 ---
--- page 640 ---

C H A P T E R
12
Markov Chain Monte Carlo Methods
with Applications
Advances in computing facilities and computational methods have dramatically
increased our ability to solve complicated problems. The advances also extend the
applicability of many existing econometric and statistical methods. Examples of
such achievements in statistics include the Markov chain Monte Carlo (MCMC)
method and data augmentation. These techniques enable us to make some statistical
inference that was not feasible just a few years ago. In this chapter, we introduce
the ideas of MCMC methods and data augmentation that are widely applicable
in ﬁnance. In particular, we discuss Bayesian inference via Gibbs sampling and
demonstrate various applications of MCMC methods. Rapid developments in the
MCMC methodology make it impossible to cover all the new methods available in
the literature. Interested readers are referred to some recent books on Bayesian and
empirical Bayesian statistics (e.g., Carlin and Louis, 2000; Gelman, Carlin, Stern,
and Rubin, 2003).
For applications, we focus on issues related to ﬁnancial econometrics. The
demonstrations shown in this chapter represent only a small fraction of all possible
applications of the techniques in ﬁnance. As a matter of fact, it is fair to say that
Bayesian inference and the MCMC methods discussed here are applicable to most,
if not all, of the studies in ﬁnancial econometrics.
We begin the chapter by reviewing the concept of a Markov process. Consider
a stochastic process {Xt}, where each Xt assumes a value in the space . The
process {Xt} is a Markov process if it has the property that, given the value of Xt,
the values of Xh, h > t, do not depend on the values Xs, s < t. In other words,
{Xt} is a Markov process if its conditional distribution function satisﬁes
P (Xh|Xs, s ≤t) = P (Xh|Xt),
h > t.
Analysis of Financial Time Series, Third Edition, By Ruey S. Tsay
Copyright 2010 John Wiley & Sons, Inc.
613
--- page 641 ---

614
markov chain monte carlo methods with applications
If {Xt} is a discrete-time stochastic process, then the prior property becomes
P (Xh|Xt, Xt−1, . . .) = P (Xh|Xt),
h > t.
Let A be a subset of . The function
Pt(θ, h, A) = P (Xh ∈A|Xt = θ),
h > t
is called the transition probability function of the Markov process. If the transition probability depends on h −t, but not on t, then the process has a stationary
transition distribution.
12.1
MARKOV CHAIN SIMULATION
Consider an inference problem with parameter vector θ and data X, where θ ∈.
To make inference, we need to know the distribution P (θ|X). The idea of Markov
chain simulation is to simulate a Markov process on , which converges to a
stationary transition distribution that is P (θ|X).
The key to Markov chain simulation is to create a Markov process whose stationary transition distribution is a speciﬁed P (θ|X) and run the simulation sufﬁciently
long so that the distribution of the current values of the process is close enough to
the stationary transition distribution. It turns out that, for a given P (θ|X), many
Markov chains with the desired property can be constructed. We refer to methods
that use Markov chain simulation to obtain the distribution P (θ|X) as MCMC
methods.
The development of MCMC methods took place in various forms in the statistical literature. Consider the problem of “missing value” in data analysis. Most
statistical methods discussed in this book were developed under the assumption of
“complete data” (i.e., there is no missing value). For example, in modeling daily
volatility of an asset return, we assume that the return data are available for all
trading days in the sample period. What should we do if there is a missing value?
Dempster, Laird, and Rubin (1977) suggest an iterative method called the
Expectation-Maximization (EM) algorithm to solve the problem. The method
consists of two steps. First, if the missing value were available, then we could use
methods of complete-data analysis to build a volatility model. Second, given the
available data and the ﬁtted model, we can derive the statistical distribution of the
missing value. A simple way to ﬁll in the missing value is to use the conditional
expectation of the derived distribution of the missing value. In practice, one can
start the method with an arbitrary value for the missing value and iterate the
procedure for many many times until convergence. The ﬁrst step of the prior
procedure involves performing the maximum-likelihood estimation of a speciﬁed
model and is called the M-step. The second step is to compute the conditional
expectation of the missing value and is called the E-step.
Tanner and Wong (1987) generalize the EM algorithm in two ways. First, they
introduce the idea of iterative simulation. For instance, instead of using the conditional expectation, one can simply replace the missing value by a random draw
--- page 642 ---

gibbs sampling
615
from its derived conditional distribution. Second, they extend the applicability of
the EM algorithm by using the concept of data augmentation. By data augmentation, we mean adding auxiliary variables to the problem under study. It turns out
that many of the simulation methods can often be simpliﬁed or speeded up by data
augmentation; see the application sections of this chapter.
12.2
GIBBS SAMPLING
Gibbs sampling (or Gibbs sampler) of Geman and Geman (1984) and Gelfand and
Smith (1990) is perhaps the most popular MCMC method. We introduce the idea
of Gibbs sampling by using a simple problem with three parameters. Here the word
parameter is used in a very general sense. A missing data point can be regarded
as a parameter under the MCMC framework. Similarly, an unobservable variable
such as the “true” price of an asset can be regarded as N parameters when there
are N transaction prices available. This concept of parameter is related to data
augmentation and becomes apparent when we discuss applications of the MCMC
methods.
Denote the three parameters by θ1, θ2, and θ3. Let X be the collection of available
data and M the entertained model. The goal here is to estimate the parameters so
that the ﬁtted model can be used to make inference. Suppose that the likelihood
function of the model is hard to obtain, but the three conditional distributions of
a single parameter given the others are available. In other words, we assume that
the following three conditional distributions are known:
f1(θ1|θ2, θ3, X, M),
f2(θ2|θ3, θ1, X, M),
f3(θ3|θ1, θ2, X, M),
(12.1)
where fi(θi|θj̸=i, X, M) denotes the conditional distribution of the parameter θi
given the data, the model, and the other two parameters. In application, we do not
need to know the exact forms of the conditional distributions. What is needed is the
ability to draw a random number from each of the three conditional distributions.
Let θ2,0 and θ3,0 be two arbitrary starting values of θ2 and θ3. The Gibbs sampler
proceeds as follows:
1. Draw a random sample from f1(θ1|θ2,0, θ3,0, X, M). Denote the random draw
by θ1,1.
2. Draw a random sample from f2(θ2|θ3,0, θ1,1, X, M). Denote the random draw
by θ2,1.
3. Draw a random sample from f3(θ3|θ1,1, θ2,1, X, M). Denote the random draw
by θ3,1.
This completes a Gibbs iteration and the parameters become θ1,1, θ2,1, and θ3,1.
Next, using the new parameters as starting values and repeating the prior iteration of random draws, we complete another Gibbs iteration to obtain the updated
--- page 643 ---

616
markov chain monte carlo methods with applications
parameters θ1,2, θ2,2, and θ3,2. We can repeat the previous iterations for m times to
obtain a sequence of random draws:
(θ1,1, θ2,1, θ3,1), . . . , (θ1,m, θ2,m, θ3,m).
Under some regularity conditions, it can be shown that, for a sufﬁciently large
m, (θ1,m, θ2,m, θ3,m) is approximately equivalent to a random draw from the joint
distribution f (θ1, θ2, θ3|X, M) of the three parameters. The regularity conditions
are weak; they essentially require that for an arbitrary starting value (θ1,0, θ2,0, θ3,0),
the prior Gibbs iterations have a chance to visit the full parameter space. The actual
convergence theorem involves using the Markov chain theory; see Tierney (1994).
In practice, we use a sufﬁciently large n and discard the ﬁrst m random draws
of the Gibbs iterations to form a Gibbs sample, say,
(θ1,m+1, θ2,m+1, θ3,m+1), . . . , (θ1,n, θ2,n, θ3,n).
(12.2)
Since the previous realizations form a random sample from the joint distribution
f (θ1, θ2, θ3|X, M), they can be used to make inference. For example, a point
estimate of θi and its variance are
θi =
1
n −m
n

j=m+1
θi,j,
σ 2
i =
1
n −m −1
n

j=m+1
(θi,j −θi)2.
(12.3)
The Gibbs sample in Eq. (12.2) can be used in many ways. For example, if
we are interested in testing the null hypothesis H0 : θ1 = θ2 versus the alternative
hypothesis Ha : θ1̸ = θ2, then we can simply obtain the point estimate of θ =
θ1 −θ2 and its variance as
θ =
1
n −m
n

j=m+1
(θ1,j −θ2,j),
σ 2 =
1
n −m −1
n

j=m+1
(θ1,j −θ2,j −θ)2.
The null hypothesis can then be tested by using the conventional t-ratio statistic
t = θ/σ.
Remark.
The ﬁrst m random draws of a Gibbs sampling, which are discarded,
are commonly referred to as the burn-in sample. The burn-ins are used to ensure
that the Gibbs sample in Eq. (12.2) is indeed close enough to a random sample
from the joint distribution f (θ1, θ2, θ3|X, M).
□
Remark.
The method discussed before consists of running a single long chain
and keeping all random draws after the burn-ins to obtain a Gibbs sample. Alternatively, one can run many relatively short chains using different starting values
and a relatively small n. The random draw of the last Gibbs iteration in each chain
is then used to form a Gibbs sample.
□
--- page 644 ---

bayesian inference
617
From the prior introduction, Gibbs sampling has the advantage of decomposing
a high-dimensional estimation problem into several lower dimensional ones via
full conditional distributions of the parameters. At the extreme, a high-dimensional
problem with N parameters can be solved iteratively by using N univariate conditional distributions. This property makes the Gibbs sampling simple and widely
applicable. However, it is often not efﬁcient to reduce all the Gibbs draws into a
univariate problem. When parameters are highly correlated, it pays to draw them
jointly. Consider the three-parameter illustrative example. If θ1 and θ2 are highly
correlated, then one should employ the conditional distributions f (θ1, θ2|θ3, X, M)
and f3(θ3|θ1, θ2, X, M) whenever possible. A Gibbs iteration then consists of (a)
drawing jointly (θ1, θ2) given θ3, and (b) drawing θ3 given (θ1, θ2). For more information on the impact of parameter correlations on the convergence rate of a Gibbs
sampler, see Liu, Wong, and Kong (1994).
In practice, convergence of a Gibbs sample is an important issue. The theory only
states that the convergence occurs when the number of iterations m is sufﬁciently
large. It provides no speciﬁc guidance for choosing m. Many methods have been
devised in the literature for checking the convergence of a Gibbs sample. But there
is no consensus on which method performs best. In fact, none of the available
methods can guarantee 100% that the Gibbs sample under study has converged for
all applications. Performance of a checking method often depends on the problem
at hand. Care must be exercised in a real application to ensure that there is no
obvious violation of the convergence requirement; see Carlin and Louis (2000)
and Gelman et al. (2003) for convergence checking methods. In application, it is
important to repeat the Gibbs sampling several times with different starting values
to ensure that the algorithm has converged.
12.3
BAYESIAN INFERENCE
Conditional distributions play a key role in Gibbs sampling. In the statistical
literature, these conditional distributions are referred to as conditional posterior
distributions because they are distributions of parameters given the data, other
parameter values, and the entertained model. In this section, we review some wellknown posterior distributions that are useful in using MCMC methods.
12.3.1
Posterior Distributions
There are two approaches to statistical inference. The ﬁrst approach is the classical
approach based on the maximum-likelihood principle. Here a model is estimated by
maximizing the likelihood function of the data, and the ﬁtted model is used to make
inference. The other approach is Bayesian inference that combines prior belief with
data to obtain posterior distributions on which statistical inference is based. Historically, there were heated debates between the two schools of statistical inference.
Yet both approaches have proved to be useful and are now widely accepted. The
methods discussed so far in this book belong to the classical approach. However,
--- page 645 ---

618
markov chain monte carlo methods with applications
Bayesian solutions exist for all of the problems considered. This is particularly so in
recent years with the advances in MCMC methods, which greatly improve the feasibility of Bayesian analysis. Readers can revisit the previous chapters and derive
MCMC solutions for the problems considered. In most cases, the Bayesian solutions are similar to what we had before. In some cases, the Bayesian solutions might
be advantageous. For example, consider the calculation of value at risk in Chapter
7. A Bayesian solution can easily take into consideration the parameter uncertainty
in VaR calculation. However, the approach requires intensive computation.
Let θ be the vector of unknown parameters of an entertained model and X
be the data. Bayesian analysis seeks to combine knowledge about the parameters
with the data to make inference. Knowledge of the parameters is expressed by
specifying a prior distribution for the parameters, which is denoted by P (θ). For
a given model, denote the likelihood function of the data by f (X|θ). Then by the
deﬁnition of conditional probability,
f (θ|X) = f (θ, X)
f (X)
= f (X|θ)P (θ)
f (X)
,
(12.4)
where the marginal distribution f (X) can be obtained by
f (X) =

f (X, θ) dθ =

f (X|θ)P (θ) dθ.
The distribution f (θ|X) in Eq. (12.4) is called the posterior distribution of θ. In
general, we can use Bayes’s rule to obtain
f (θ|X) ∝f (X|θ)P (θ),
(12.5)
where P (θ) is the prior distribution and f (X|θ) is the likelihood function. From
Eq. (12.5), making statistical inference based on the likelihood function f (X|θ)
amounts to using a Bayesian approach with a constant prior distribution.
12.3.2
Conjugate Prior Distributions
Obtaining the posterior distribution in Eq. (12.4) is not simple in general, but there
are cases in which the prior and posterior distributions belong to the same family
of distributions. Such a prior distribution is called a conjugate prior distribution.
For MCMC methods, use of conjugate priors means that a closed-form solution
for the conditional posterior distributions is available. Random draws of the Gibbs
sampler can then be obtained by using the commonly available computer routines
of probability distributions. In what follows, we review some well-known conjugate
priors. For more information, readers are referred to textbooks on Bayesian statistics
(e.g., DeGroot 1970, Chapter 9).
Result 12.1. Suppose that x1, . . . , xn form a random sample from a normal
distribution with mean µ, which is unknown, and variance σ 2, which is known
--- page 646 ---

bayesian inference
619
and positive. Suppose that the prior distribution of µ is a normal distribution with
mean µo and variance σ 2
o . Then the posterior distribution of µ given the data and
prior is normal with mean µ∗and variance σ 2
∗given by
µ∗= σ 2µo + nσ 2
o ¯x
σ 2 + nσ 2o
and
σ 2
∗=
σ 2σ 2
o
σ 2 + nσ 2o
,
where ¯x = n
i=1 xi/n is the sample mean.
In Bayesian analysis, it is often convenient to use the precision parameter η =
1/σ 2 (i.e., the inverse of the variance σ 2). Denote the precision parameter of the
prior distribution by ηo = 1/σ 2
o and that of the posterior distribution by η∗= 1/σ 2
∗.
Then Result 12.1 can be rewritten as
η∗= ηo + nη
and
µ∗= ηo
η∗
× µo + nη
η∗
× ¯x.
For the normal random sample considered, data information about µ is contained in
the sample mean ¯x, which is the sufﬁcient statistic of µ. The precision of ¯x is n/σ 2
= nη. Consequently, Result 12.1 says that (a) precision of the posterior distribution
is the sum of the precisions of the prior and the data, and (b) the posterior mean is
a weighted average of the prior mean and sample mean with weight proportional
to the precision. The two formulas also show that the contribution of the prior
distribution is diminishing as the sample size n increases.
A multivariate version of Result 12.1 is particularly useful in MCMC methods
when linear regression models are involved; see Box and Tiao (1973).
Result 12.1a. Suppose that x1, . . . , xn form a random sample from a multivariate normal distribution with mean vector µ and a known covariance matrix
. Suppose also that the prior distribution of µ is multivariate normal with mean
vector µo and covariance matrix o. Then the posterior distribution of µ is also
multivariate normal with mean vector µ∗and covariance matrix ∗, where
−1
∗
= −1
o
+ n−1
and
µ∗= ∗(−1
o µo + n−1 ¯x),
where ¯x = n
i=1 xi/n is the sample mean, which is distributed as a multivariate
normal with mean µ and covariance matrix /n. Note that n−1 is the precision
matrix of ¯x and −1
o
is the precision matrix of the prior distribution.
A random variable η has a gamma distribution with positive parameters α and
β if its probability density function is
f (η|α, β) =
βα
(α)ηα−1e−βη,
η > 0,
where (α) is a gamma function. For this distribution, E(η) = α/β and Var(η) =
α/β2.
--- page 647 ---

620
markov chain monte carlo methods with applications
Result 12.2. Suppose that x1, . . . , xn form a random sample from a normal
distribution with a given mean µ and an unknown precision η. If the prior distribution of η is a gamma distribution with positive parameters α and β, then the
posterior distribution of η is a gamma distribution with parameters α + (n/2) and
β + n
i=1(xi −µ)2/2.
A random variable θ has a beta distribution with positive parameters α and β
if its probability density function is
f (θ|α, β) = (α + β)
(α)(β)θα−1(1 −θ)β−1,
0 < θ < 1.
The mean and variance of θ are E(θ) = α/(α + β) and Var(θ) = αβ/[(α + β)2(α +
β + 1)].
Result 12.3. Suppose that x1, . . . , xn form a random sample from a Bernoulli
distribution with parameter θ. If the prior distribution of θ is a beta distribution
with given positive parameters α and β, then the posterior of θ is a beta distribution
with parameters α + n
i=1 xi and β + n −n
i=1 xi.
Result 12.4. Suppose that x1, . . . , xn form a random sample from a Poisson
distribution with parameter λ. Suppose also that the prior distribution of λ is a
gamma distribution with given positive parameters α and β. Then the posterior
distribution of λ is a gamma distribution with parameters α + n
i=1 xi and β + n.
Result 12.5. Suppose that x1, . . . , xn form a random sample from an exponential
distribution with parameter λ. If the prior distribution of λ is a gamma distribution
with given positive parameters α and β, then the posterior distribution of λ is a
gamma distribution with parameters α + n and β + n
i=1 xi.
A random variable X has a negative binomial distribution with parameters m
and λ, where m > 0 and 0 < λ < 1, if X has a probability mass function
p(n|m, λ) =



 m + n −1
n

λm(1 −λ)n
if n = 0, 1, . . . ,
0
otherwise.
A simple example of negative binomial distribution in ﬁnance is how many MBA
graduates a ﬁrm must interview before ﬁnding exactly m “right candidates” for its
m openings, assuming that the applicants are independent and each applicant has
a probability λ of being a perfect ﬁt. Denote the total number of interviews by Y.
Then X = Y −m is distributed as a negative binomial with parameters m and λ.
Result 12.6. Suppose that x1, . . . , xn form a random sample from a negative
binomial distribution with parameters m and λ, where m is positive and ﬁxed. If
