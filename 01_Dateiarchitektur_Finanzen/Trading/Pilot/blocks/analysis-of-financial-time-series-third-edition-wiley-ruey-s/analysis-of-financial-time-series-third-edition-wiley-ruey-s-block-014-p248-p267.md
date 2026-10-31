# Analysis of Financial Time Series, Third Edition (Wiley -- Ruey S_ Tsay -- Wiley series in probability and statistics, 3rd ed_, -- John Wiley & Sons, -- isbn13 9780470414354 -- 9f99b80c7b2dedd477f463dc5323f3b6 -- An.pdf — pages 248–267

--- page 248 ---

application
221
TABLE 4.4
Out-of-Sample Forecast Comparison among Linear, TAR, and MSA
Models for the U.S. Quarterly Unemployment Ratea
Relative MSE of Forecast
Model
1-step
2-step
3-step
4-step
5-step
Overall Comparison
Linear
1.00
1.00
1.00
1.00
1.00
TAR
1.00
1.04
0.99
0.98
1.03
MSA
1.19
1.39
1.40
1.45
1.61
MSE
0.08
0.31
0.67
1.13
1.54
Forecast Origins in Economic Contractions
Linear
1.00
1.00
1.00
1.00
1.00
TAR
0.85
0.91
0.83
0.72
0.72
MSA
0.97
1.03
0.96
0.86
1.02
MSE
0.22
0.97
2.14
3.38
3.46
Forecast Origins in Economic Expansions
Linear
1.00
1.00
1.00
1.00
1.00
TAR
1.06
1.13
1.10
1.15
1.17
MSA
1.31
1.64
1.73
1.84
1.87
MSE
0.06
0.21
0.45
0.78
1.24
Mean of Forecast Errors
Model
1-step
2-step
3-step
4-step
5-step
Overall Comparison
Linear
0.03
0.09
0.17
0.25
0.33
TAR
−0.10
−0.02
−0.03
−0.03
−0.01
MSA
0.00
−0.02
−0.04
−0.07
−0.12
Forecast Origins in Economic Contractions
Linear
0.31
0.68
1.08
1.41
1.38
TAR
0.24
0.56
0.87
1.01
0.86
MSA
0.20
0.41
0.57
0.52
0.14
Forecast Origins in Economic Expansions
Linear
−0.01
0.00
0.03
0.08
0.17
TAR
−0.05
−0.11
−0.17
−0.19
−0.14
MSA
−0.03
−0.08
−0.13
−0.17
−0.16
aThe starting forecast origin is 1968.II, where the row marked by MSE shows the MSE of the benchmark
linear model.
--- page 249 ---

222
nonlinear models and their applications
2. For forecast origins in economic contractions, the TAR model shows
improvements over the linear model both in MSE and bias. The MSA model
also shows some improvement over the linear model, but the improvement
is not as large as that of the TAR model.
3. For forecast origins in economic expansions, the linear model outperforms
both nonlinear models.
The results suggest that the contributions of nonlinear models over linear ones in
forecasting the U.S. quarterly unemployment rate are mainly in the periods when
the U.S. economy is in contraction. This is not surprising because, as mentioned
before, it is during the economic contractions that government interventions and
industrial restructuring are most likely to occur. These external events could introduce nonlinearity in the U.S. unemployment rate. Intuitively, such improvements
are important because it is during the contractions that people pay more attention
to economic forecasts.
APPENDIX A: SOME RATS PROGRAMS FOR NONLINEAR
VOLATILITY MODELS
Program Used to Estimate an AR(2)–TAR–GARCH(1,1) Model for Daily Log
Returns of IBM Stock
Assume that the data ﬁle is d-ibmln03.txt.
all 0 10446:1
open data d-ibmln03.txt
data(org=obs) / rt
set h = 0.0
nonlin mu p2 a0 a1 b1 a2 b2
frml at = rt(t)-mu-p2*rt(t-2)
frml gvar = a0 + a1*at(t-1)**2+b1*h(t-1) $
+ % if(at(t-1) < 0,a2*at(t-1)**2+b2*h(t-1),0)
frml garchln = -0.5*log(h(t)=gvar(t))-0.5*at(t)**2/h(t)
smpl 4 10446
compute mu = 0.03, p2 = -0.03
compute a0 = 0.07, a1 = 0.05, a2 = 0.05, b1 = 0.85, b2 = 0.05
maximize(method=simplex,iterations=10) garchln
smpl 4
10446
maximize(method=bhhh,recursive,iterations=150) garchln
set fv = gvar(t)
set resid = at(t)/sqrt(fv(t))
set residsq = resid(t)*resid(t)
cor(qstats,number=20,span=10) resid
cor(qstats,number=20,span=10) residsq
--- page 250 ---

appendix b: r and s-plus commands for neural network
223
Program Used to Estimate a Smooth TAR Model for the Monthly Simple
Returns of 3M Stock
The data ﬁle is m-3m4608.txt.
all 0 755:1
open data m-3m4608.txt
data(org=obs) / date mmm
set h = 0.0
nonlin a0 a1 a2
a00 a11 mu
frml at = mmm(t) - mu
frml var1 =
a0+a1*at(t-1)**2+a2*at(t-2)**2
frml var2 = a00+a11*at(t-1)**2
frml gvar = var1(t)+var2(t)/(1.0+exp(-at(t-1)*1000.0))
frml garchlog = -0.5*log(h(t)=gvar(t))-0.5*at(t)**2/h(t)
smpl 3 623
compute a0 = .01, a1 = 0.2, a2 = 0.1
compute a00 = .01, a11 = -.2, mu = 0.02
maximize(method=bhhh,recursive,iterations=150) garchlog
set fv = gvar(t)
set resid = at(t)/sqrt(fv(t))
set residsq = resid(t)*resid(t)
cor(qstats,number=20,span=10) resid
cor(qstats,number=20,span=10) residsq
APPENDIX B: R AND S-PLUS COMMANDS FOR NEURAL NETWORK
The following commands are used in R or S-Plus to build the 3–2–1 skip-layer
feed-forward network of Example 4.7. A line starting with # denotes a comment.
The data ﬁle is m-ibmln.txt. The library used is nnet.
# load the data into R or S-Plus workspace.
x_scan(file=’m-ibmln.txt’)
# select the output: r(t)
y_x[4:864]
# obtain the input variables: r(t-1), r(t-2), and r(t-3)
ibm.x_cbind(x[3:863]_,x[2:862],x[1:861])
# build a 3-2-1 network with skip layer connections
# and linear output.
ibm.nn_nnet(ibm.x,y,size=2,linout=T,skip=T,maxit=10000,
decay=1e-2,reltol=1e-7,abstol=1e-7,range=1.0)
# print the summary results of the network
summary(ibm.nn)
# compute \& print the residual sum of squares.
sse_sum((y-predict(ibm.nn,ibm.x))^2)
print(sse)
--- page 251 ---

224
nonlinear models and their applications
#eigen(nnet.Hess(ibm.nn,ibm.x,y),T)$values
# setup the input variables in the forecasting subsample
ibm.p_cbind(x[864:887],x[863:886],x[862:885])
# compute the forecasts
yh_predict(ibm.nn,ibm.p)
# The observed returns in the forecasting subsample
yo_x[865:888]
# compute \& print the sum of squares of forecast errors
ssfe_sum((yo-yh)^2)
print(ssfe)
# quit S-Plus or R
q()
EXERCISES
4.1. Consider the daily simple returns of Johnson & Johnson stock from January
1998 to December 2008. The data are in the ﬁle d-jnj9808.txt or can be
obtained from CRSP. Convert the returns into log returns in percentage. (a)
Build a GJR model for the log return series. Write down the ﬁtted model. Is
the leverage effect signiﬁcant at the 1% level? (b) Build a general threshold
volatility model for the log return series. (c) Compare the two TGARCH
models.
4.2. Consider the monthly simple returns of General Electric (GE) stock from
January 1926 to December 2008 with 996 observations. You may download
the data from CRSP or use the ﬁle m-ge2608.txt on the Web. Convert
the returns into log returns in percentages. Build a TGARCH model with
GED innovations for the series using at−1 as the threshold variable with zero
threshold, where at−1 is the shock at time t −1. Write down the ﬁtted model.
Is the leverage effect signiﬁcant at the 5% level?
4.3. Suppose that the monthly log returns of GE stock, measured in percentages,
follow a smooth threshold IGARCH(1,1) model. For the sampling period from
January 1926 to December 2008, the ﬁtted model is
rt = 1.14 + at,
at = σtϵt
σ 2
t = 0.119a2
t−1 + 0.881σ 2
t−1 +
1
1 + exp(−10at−1)(4.276 −0.084σ 2
t−1),
where all of the estimates are highly signiﬁcant, the coefﬁcient 10 in the
exponent is ﬁxed a priori to simplify the estimation, and {ϵt} are iid N(0, 1).
Assume that a996 = −5.06 and σ 2
996 = 50.5. What is the 1-step-ahead volatility
forecast σ996(1)? Suppose instead that a996 = 5.06. What is the 1-step-ahead
volatility forecast σ996(1)?
--- page 252 ---

exercises
225
4.4. Suppose that the monthly log returns, in percentages, of a stock follow the
following Markov switching model:
rt = 1.25 + at,
at = σtϵt,
σ 2
t =

0.10a2
t−1 + 0.93σ 2
t−1
if st = 1,
4.24 + 0.10a2
t−1 + 0.78σ 2
t−1
if st = 2,
where the transition probabilities are
P (st = 2|st−1 = 1) = 0.15,
P (st = 1|st−1 = 2) = 0.05.
Suppose that a100 = 6.0, σ 2
100 = 50.0, and s100 = 2 with probability 1.0. What
is the 1-step-ahead volatility forecast at the forecast origin t = 100? Also, if
the probability of s100 = 2 is reduced to 0.8, what is the 1-step-ahead volatility
forecast at the forecast origin t = 100?
4.5. Consider the monthly simple returns of GE stock from January 1926 to December 2008. Use the last three years of data for forecasting evaluation.
(a) Using lagged returns rt−1, rt−2, rt−3 as input, build a 3–2–1 feed-forward
network to forecast 1-step-ahead returns. Calculate the mean squared error
of forecasts.
(b) Again, use lagged returns rt−1, rt−2, rt−3 and their signs (directions) to
build a 6–5–1 feed-forward network to forecast the 1-step ahead direction
of GE stock price movement with 1 denoting upward movement. Calculate
the mean squared error of forecasts.
Note: Let rtn denote a time series in R or S-Plus. To create a direction
variable for rtn, use the command
drtn = ifelse(rtn > 0, 1, 0)
4.6. Because of the existence of inverted yield curves in the term structure of
interest rates, the spread of interest rates should be nonlinear. To verify this,
consider the weekly U.S. interest rates of (a) Treasury 1-year constant maturity
rate and (b) Treasury 3-year constant maturity rate. As in Chapter 2, denote
the two interest rates by r1t and r3t, respectively, and the data span is from
January 5, 1962, to April 10, 2009. The data are in ﬁles w-gs3yr.txt and
w-gs1yr.txt on the Web and can be obtained from the Federal Reserve
Bank of St. Louis.
(a) Let st = r3t −r1t be the spread in log interest rates. Is {st} linear? Perform
some nonlinearity tests and draw the conclusion using the 5% signiﬁcance
level.
--- page 253 ---

226
nonlinear models and their applications
(b) Let s∗
t = (r3t −r3,t−1) −(r1t −r1,t−1) = st −st−1 be the change in interest rate spread. Is {s∗
t } linear? Perform some nonlinearity tests and draw
the conclusion using the 5% signiﬁcance level.
(c) Build a threshold model for the st series and check the ﬁtted model.
(d) Build a threshold model for the s∗
t series and check the ﬁtted model.
REFERENCES
Akaike, H. (1974). A new look at the statistical model identiﬁcation. IEEE Transactions on
Automatic Control AC-19: 716–723.
Andrews, D. W. K. and Ploberger, W. (1994). Optimal tests when a nuisance parameter is
present only under the alternative. Econometrica 62: 1383–1414.
Brock, W., Dechert, W. D., and Scheinkman, J. (1987). A test for independence based on
the correlation dimension. Working paper, Department of Economics, University of
Wisconsin, Madison.
Brock, W., Hsieh, D. A., and LeBaron, B. (1991). Nonlinear Dynamics, Chaos and Instability: Statistical Theory and Economic Evidence. MIT Press, Cambridge, MA.
Bryson, A. E. and Ho, Y. C. (1969). Applied Optimal Control. Blaisdell, New York
Cai, Z., Fan, J., and Yao, Q. (2000). Functional-coefﬁcient regression models for nonlinear
time series. Journal of the American Statistical Association 95: 941–956.
Carlin, B. P., Polson, N. G., and Stoffer, D. S. (1992). A Monte Carlo approach to nonnormal
and nonlinear state space modeling. Journal of the American Statistical Association 87:
493–500.
Chan, K. S. (1991). Percentage points of likelihood ratio tests for threshold autoregression.
Journal of the Royal Statistical Society Series B 53: 691–696.
Chan, K. S. (1993). Consistency and limiting distribution of the least squares estimator of a
threshold autoregressive model. Annals of Statistics 21: 520–533.
Chan, K. S. and Tong, H. (1986). On estimating thresholds in autoregressive models. Journal
of Time Series Analysis 7: 179–190.
Chan, K. S. and Tsay, R. S. (1998). Limiting properties of the conditional least squares
estimator of a continuous TAR model. Biometrika 85: 413–426.
Chen, C., McCulloch, R. E., and Tsay, R. S. (1997). A uniﬁed approach to estimating and
modeling univariate linear and nonlinear time series. Statistica Sinica 7: 451–472.
Chen, R. and Tsay, R. S. (1991). On the ergodicity of TAR(1) processes. Annals of Applied
Probability 1: 613–634.
Chen, R. and Tsay, R. S. (1993a). Functional-coefﬁcient autoregressive models. Journal of
the American Statistical Association 88: 298–308.
Chen, R. and Tsay, R. S. (1993b). Nonlinear additive ARX models. Journal of the American
Statistical Association 88: 955–967.
Chen, R., Liu, J., and Tsay, R. S. (1995). Additivity tests for nonlinear autoregressive models.
Biometrika (1995) 82: 369–383.
Chen, T. and Chen, H. (1995). Universal approximation to nonlinear operators by neural
networks with arbitrary activation functions and its application to dynamical systems.
IEEE Transactions on Neural Networks 6: 911–917.
--- page 254 ---

references
227
Cheng, B. and Titterington, D. M. (1994). Neural networks: A review from a statistical
perspective. Statistical Science 9: 2–54.
Clements, M. P. and Hendry, D. F. (1993). On the limitations of comparing mean square
forecast errors. Journal of Forecasting 12: 617–637.
Cleveland, W. S. (1979). Robust locally weighted regression and smoothing scatterplots.
Journal of the American Statistical Association 74: 829–836.
Dahl, C. M. and Hylleberg, S. (1999). Specifying nonlinear econometric models by ﬂexible
regression models and relative forecast performance. Working paper, Department of
Economics, University of Aarhus, Denmark.
Davis, R. B. (1987). Hypothesis testing when a nuisance parameter is present only under
the alternative. Biometrika 74: 33–43.
Engle, R. F. (1982). Autoregressive conditional heteroscedasticity with estimates of the
variance of United Kingdom inﬂations. Econometrica 50: 987–1007.
Epanechnikov, V. (1969). Nonparametric estimates of a multivariate probability density.
Theory of Probability and Its Applications 14: 153–158.
Fan, J. (1993). Local linear regression smoother and their minimax efﬁciencies. Annals of
Statistics 21: 196–216.
Fan, J. and Yao, Q. (2003). Nonlinear Time Series: Nonparametric and Parametric Methods.
Springer, New York.
Gelfand, A. E. and Smith, A. F. M. (1990). Sampling-based approaches to calculating
marginal densities. Journal of the American Statistical Association 85: 398–409.
Granger, C. W. J. and Andersen, A. P. (1978). An Introduction to Bilinear Time Series
Models. Vandenhoek and Ruprecht, Gottingen.
Hamilton, J. D. (1989). A new approach to the economic analysis of nonstationary time
series and the business cycle. Econometrica 57: 357–384.
Hamilton, J. D. (1990). Analysis of time series subject to changes in regime. Journal of
Econometrics 45: 39–70.
Hamilton, J. D. (1994). Time Series Analysis. Princeton University Press, Princeton, NJ.
Hansen, B. E. (1997). Inference in TAR models. Studies in Nonlinear Dynamics and Econometrics 1: 119–131.
H¨ardle, W. (1990). Applied Nonparametric Regression. Cambridge University Press, New
York.
Hinich, M. (1982). Testing for Gaussianity and linearity of a stationary time series. Journal
of Time Series Analysis 3: 169–176.
Hornik, K. (1993). Some new results on neural network approximation. Neural Networks 6:
1069–1072.
Hornik, K., Stinchcombe, M., and White, H. (1989). Multilayer feedforward networks are
universal approximators. Neural Networks 2: 359–366.
Hsieh, D. A. (1989). Testing for nonlinear dependence in daily foreign exchange rates.
Journal of Business 62: 339–368.
Keenan, D. M. (1985). A Tukey non-additivity-type test for time series nonlinearity.
Biometrika 72: 39–44.
Kitagawa, G. (1998). A self-organizing state space model. Journal of the American Statistical
Association 93: 1203–1215.
--- page 255 ---

228
nonlinear models and their applications
Lewis, P. A. W. and Stevens, J. G. (1991). Nonlinear modeling of time series using multivariate adaptive regression spline (MARS). Journal of the American Statistical Association
86: 864–877.
Liu, J. and Brockwell, P. J. (1988). On the general bilinear time-series model. Journal of
Applied Probability 25: 553–564.
Luukkonen, R., Saikkonen, P., and Ter¨asvirta (1988). Testing linearity against smooth transition autoregressive models. Biometrika 75: 491–499.
McCulloch, R. E. and Tsay, R. S. (1993). Bayesian inference and prediction for mean
and variance shifts in autoregressive time series. Journal of the American Statistical
Association 88: 968–978.
McCulloch, R. E. and Tsay, R. S. (1994). Statistical inference of macroeconomic time series
via Markov switching models. Journal of Time Series Analysis 15: 523–539.
McLeod, A. I. and Li, W. K. (1983). Diagnostic checking ARMA time series models using
squared-residual autocorrelations. Journal of Time Series Analysis 4: 269–273.
Montgomery, A. L., Zarnowitz, V., Tsay, R. S., and Tiao, G. C. (1998). Forecasting the U.S.
unemployment rate, Journal of the American Statistical Association 93: 478–493.
Nadaraya, E. A. (1964). On estimating regression. Theory and Probability Application 10:
186–190.
Petruccelli, J. and Woolford, S. W. (1984). A threshold AR(1) model. Journal of Applied
Probability 21: 270–286.
Potter, S. M. (1995). A nonlinear approach to U.S. GNP. Journal of Applied Econometrics
10: 109–125.
Priestley, M. B. (1980). State-dependent models: A general approach to nonlinear time series
analysis. Journal of Time Series Analysis 1: 47–71.
Priestley, M. B. (1988). Non-linear and Non-stationary Time Series Analysis, Academic
Press, London, UK.
Ramsey, J. B. (1969). Tests for speciﬁcation errors in classical linear least squares regression
analysis. Journal of the Royal Statistical Society Series B 31: 350–371.
Ripley, B. D. (1993). Statistical aspects of neural networks. In O. E. Barndorff-Nielsen, J.
L. Jensen, and W. S. Kendall (eds.). Networks and Chaos—Statistical and Probabilistic
Aspects, pp. 40–123. Chapman and Hall, London, UK.
Subba Rao, T. and Gabr, M. M. (1984). An Introduction to Bispectral Analysis and Bilinear
Time Series Models, Lecture Notes in Statistics, vol. 24. Springer, New York.
Ter¨asvirta, T. (1994). Speciﬁcation, estimation, and evaluation of smooth transition autoregressive models. Journal of the American Statistical Association 89: 208–218.
Tiao, G. C. and Tsay, R. S. (1994). Some advances in nonlinear and adaptive modeling in
time series. Journal of Forecasting 13: 109–131.
Tong, H. (1978). On a threshold model. In C. H. Chen (ed.). Pattern Recognition and Signal
Processing. Sijhoff & Noordhoff, Amsterdam.
Tong, H. (1983). Threshold Models in Nonlinear Time Series Analysis, Lecture Notes in
Statistics, Springer, New York.
Tong, H. (1990). Non-Linear Time Series: A Dynamical System Approach, Oxford University
Press, Oxford, UK.
Tsay, R. S. (1986). Nonlinearity tests for time series. Biometrika 73: 461–466.
--- page 256 ---

references
229
Tsay, R. S. (1989). Testing and modeling threshold autoregressive processes. Journal of the
American Statistical Association 84: 231–240.
Tsay, R. S. (1998). Testing and modeling multivariate threshold models. Journal of the
American Statistical Association 93: 1188–1202.
Venables, W. N. and Ripley, B. D. (1999). Modern Applied Statistics with S-Plus, 3rd edn.
Springer, New York.
Watson, G. S. (1964). Smooth regression analysis. Sankhya Series A 26: 359–372.
--- page 257 ---
--- page 258 ---

C H A P T E R
5
High-Frequency Data Analysis
and Market Microstructure
High-frequency data are observations taken at ﬁne time intervals. In ﬁnance, they
often mean observations taken daily or at a ﬁner time scale. These data have
become available primarily due to advances in data acquisition and processing
techniques, and they have attracted much attention because they are important in
empirical study of market microstructure and realized volatility. The ultimate highfrequency data in ﬁnance are the transaction-by-transaction or trade-by-trade data in
security markets. Here time is often measured in seconds. The Trades and Quotes
(TAQ) database of the New York Stock Exchange (NYSE) contains all equity
transactions reported on the Consolidated Tape from 1992 to the present, which
includes transactions on the NYSE, AMEX, NASDAQ, and the regional exchanges.
The Berkeley Options Data Base provides similar data for options transactions
from August 1976 to December 1996. More high-frequency options data are also
available; see the website of Chicago Board Options Exchange. Transactions data
for many other securities and markets, both domestic and foreign, are continuously
collected and processed. Wood (2000) provides some historical perspective of highfrequency ﬁnancial study.
High-frequency ﬁnancial data are important in studying a variety of issues related
to the trading process and market microstructure. They can be used to compare the
efﬁciency of different trading systems in price discovery (e.g., the open out-cry
system of the NYSE and the computer trading system of NASDAQ). They can
also be used to study the dynamics of bid-and-ask quotes of a particular stock (e.g.,
Hasbrouck, 1999; Zhang, Russell, and Tsay, 2008). In an order-driven stock market
(e.g., the Taiwan Stock Exchange), high-frequency data can be used to study the
order dynamics and, more interesting, to investigate the question of “who provides
the market liquidity.” Cho, Russell, Tiao, and Tsay (2003) use intraday 5-minute
returns of more than 340 stocks traded on the Taiwan Stock Exchange to study the
Analysis of Financial Time Series, Third Edition, By Ruey S. Tsay
Copyright 2010 John Wiley & Sons, Inc.
231
--- page 259 ---

232
high-frequency data analysis and market microstructure
impact of daily stock price limits and ﬁnd signiﬁcant evidence of magnet effects
toward the price ceiling.
However, high-frequency data have some unique characteristics that do not
appear in lower frequencies. Analysis of these data thus introduces new challenges
to ﬁnancial economists and statisticians. In this chapter, we study these special
characteristics, consider methods for analyzing high-frequency data, and discuss
implications of the results obtained. In particular, we discuss nonsynchronous
trading, bid–ask spread, duration models, price movements, and bivariate models for price changes and time durations between transactions associated with price
changes. The models discussed are also applicable to other scientiﬁc areas such as
telecommunications and environmental studies.
5.1
NONSYNCHRONOUS TRADING
We begin with nonsynchronous trading. Stock tradings such as those on the NYSE
do not occur in a synchronous manner; different stocks have different trading
frequencies, and even for a single stock the trading intensity varies from hour to
hour and from day to day. Yet we often analyze a return series in a ﬁxed time
interval such as daily, weekly, or monthly. For daily series, the price of a stock is
its closing price, which is the last transaction price of the stock in a trading day. The
actual time of the last transaction of the stock varies from day to day. As such we
incorrectly assume daily returns as an equally spaced time series with a 24-hour
interval. It turns out that such an assumption can lead to erroneous conclusions
about the predictability of stock returns even if the true return series are serially
independent.
For daily stock returns, nonsynchronous trading can introduce (a) lag-1 cross
correlation between stock returns, (b) lag-1 serial correlation in a portfolio return,
and (c) in some situations negative serial correlations of the return series of a single
stock. Consider stocks A and B. Assume that the two stocks are independent, and
stock A is traded more frequently than stock B. For special news affecting the
market that arrives near the closing hour on one day, stock A is more likely than
B to show the effect of the news on the same day simply because A is traded
more frequently. The effect of the news on B will eventually appear, but it may be
delayed until the following trading day. If this situation indeed happens, return of
stock A appears to lead that of stock B. Consequently, the return series may show
a signiﬁcant lag-1 cross correlation from A to B even though the two stocks are
independent. For a portfolio that holds stocks A and B, the prior cross correlation
would become a signiﬁcant lag-1 serial correlation.
In a more complicated manner, nonsynchronous trading can also induce erroneous negative serial correlations for a single stock. There are several models
available in the literature to study this phenomenon; see Campbell, Lo, and MacKinlay (1997) and the references therein. Here we adopt a simpliﬁed version of the
model proposed in Lo and MacKinlay (1990). Let rt be the continuously compounded return of a security at the time index t. For simplicity, assume that {rt}
--- page 260 ---

nonsynchronous trading
233
is a sequence of independent and identically distributed random variables with
mean E(rt) = µ and variance Var(rt) = σ 2. For each time period, the probability that the security is not traded is π, which is time invariant and independent
of rt. Let ro
t be the observed return. When there is no trade at time index t, we
have ro
t = 0 because there is no information available. Yet when there is a trade at
time index t, we deﬁne ro
t as the cumulative return from the previous trade (i.e.,
ro
t = rt + rt−1 + · · · + rt−kt, where kt is the largest nonnegative integer such that
no trade occurred in the periods t −kt, t −kt + 1, . . . , t −1). Mathematically, the
relationship between rt and ro
t is
ro
t =



0
with probability π
rt
with probability (1 −π)2
rt + rt−1
with probability (1 −π)2π
rt + rt−1 + rt−2
with probability (1 −π)2π2
...
k
i=0 rt−i
with probability (1 −π)2πk
...
(5.1)
These probabilities are easy to understand. For example, ro
t = rt if and only if there
are trades at both t and t −1, ro
t = rt + rt−1 if and only if there are trades at t
and t −2, but no trade at t −1, and ro
t = rt + rt−1 + rt−2 if and only if there are
trades at t and t −3, but no trades at t −1 and t −2, and so on. As expected, the
total probability is 1 given by
π + (1 −π)2(1 + π + π2 + · · ·) = π + (1 −π)2
1
1 −π = π + 1 −π = 1.
We are ready to consider the moment equations of the observed return series
{ro
t }. First, the expectation of ro
t is
E(ro
t ) = (1 −π)2E(rt) + (1 −π)2πE(rt + rt−1) + · · ·
= (1 −π)2µ + (1 −π)2π2µ + (1 −π)2π23µ + · · ·
= (1 −π)2µ(1 + 2π + 3π2 + 4π3 + · · ·)
= (1 −π)2µ
1
(1 −π)2 = µ.
(5.2)
In the prior derivation, we use the result 1 + 2π + 3π2 + 4π3 + · · · = 1/(1 −π)2.
Next, for the variance of ro
t , we use Var(ro
t ) = E[(ro
t )2] −[E(ro
t )]2 and
E(ro
t )2 = (1 −π)2E[(rt)2] + (1 −π)2πE[(rt + rt−1)2] + · · ·
= (1 −π)2[(σ 2 + µ2) + π(2σ 2 + 4µ2) + π2(3σ 2 + 9µ2) + · · ·]
(5.3)
--- page 261 ---

234
high-frequency data analysis and market microstructure
= (1 −π)2[σ 2(1 + 2π + 3π2 + · · ·) + µ2(1 + 4π + 9π2 + · · ·)]
(5.4)
= σ 2 + µ2

2
1 −π −1

.
(5.5)
In Eq. (5.3), we use
E
 k

i=0
rt−i
2
= Var
 k

i=0
rt−i

+

E
 k

i=0
rt−i
2
= (k + 1)σ 2 + [(k + 1)µ]2
under the serial independence assumption of rt. Using techniques similar to that
of Eq. (5.2), we can show that the ﬁrst term of Eq. (5.4) reduces to σ 2. For the
second term of Eq. (5.4), we use the identity
1 + 4π + 9π2 + 16π3 + · · · =
2
(1 −π)3 −
1
(1 −π)2 ,
which can be obtained as follows. Let
H = 1 + 4π + 9π2 + 16π3 + · · ·
and
G = 1 + 3π + 5π2 + 7π3 + · · · .
Then (1 −π)H = G and
(1 −π)G = 1 + 2π + 2π2 + 2π3 + · · ·
= 2(1 + π + π2 + · · ·) −1 =
2
1 −π −1.
Consequently, from Eqs. (5.2) and (5.5), we have
Var(ro
t ) = σ 2 + µ2

2
1 −π −1

−µ2 = σ 2 + 2πµ2
1 −π .
(5.6)
Consider next the lag-1 autocovariance of {ro
t }. Here we use Cov(ro
t , ro
t−1) =
E(ro
t ro
t−1) −E(r0
t )E(ro
t−1) = E(ro
t ro
t−1) −µ2. The question then reduces to ﬁnding
E(ro
t ro
t−1). Notice that ro
t ro
t−1 is zero if there is no trade at t, no trade at t −1, or
no trade at both t and t −1. Therefore, we have
ro
t ro
t−1 =



0
with probability 2π −π2
rtrt−1
with probability (1 −π)3
rt(rt−1 + rt−2)
with probability (1 −π)3π
rt(rt−1 + rt−2 + rt−3)
with probability (1 −π)3π2
...
rt(k
i=1 rt−i)
with probability (1 −π)3πk−1
...
(5.7)
--- page 262 ---

bid–ask spread
235
Again the total probability is unity. To understand the prior result, notice that
ro
t ro
t−1 = rtrt−1 if and only if there are three consecutive trades at t −2, t −1, and
t. Using Eq. (5.7) and the fact that E(rtrt−j) = E(rt)E(rt−j) = µ2 for j > 0, we
have
E(ro
t ro
t−1)
= (1 −π)3

E(rtrt−1) + πE[rt(rt−1 + rt−2)] + π2E

rt
 3

i=1
rt−i

+ · · ·
+
= (1 −π)3µ2(1 + 2π + 3π2 + · · ·) = (1 −π)µ2.
The lag-1 autocovariance of {ro
t } is then
Cov(ro
t , ro
t−1) = −πµ2.
(5.8)
Provided that µ is not zero, the nonsynchronous trading induces a negative lag-1
autocorrelation in ro
t given by
ρ1(ro
t ) =
−(1 −π)πµ2
(1 −π)σ 2 + 2πµ2 .
In general, we can extend the prior result and show that
Cov(ro
t , ro
t−j) = −µ2πj,
j ≥1.
The magnitude of the lag-1 ACF depends on the choices of µ, π, and σ and can
be substantial. Thus, when µ̸ = 0, the nonsynchronous trading induces negative
autocorrelations in an observed security return series.
The previous discussion can be generalized to the return series of a portfolio
that consists of N securities; see Campbell et al. (1997, Chapter 3). In the time
series literature, effects of nonsynchronous trading on the return of a single security
are equivalent to that of random temporal aggregation on a time series, with the
trading probability π governing the mechanism of aggregation.
5.2
BID–ASK SPREAD
In some stock exchanges (e.g., NYSE), market makers play an important role in
facilitating trades. They provide market liquidity by standing ready to buy or sell
whenever the public wishes to buy or sell. By market liquidity, we mean the ability
to buy or sell signiﬁcant quantities of a security quickly, anonymously, and with
little price impact. In return for providing liquidity, market makers are granted
monopoly rights by the exchange to post different prices for purchases and sales of
a security. They buy at the bid price Pb and sell at a higher ask price Pa. (For the
--- page 263 ---

236
high-frequency data analysis and market microstructure
public, Pb is the sale price and Pa is the purchase price.) The difference Pa −Pb is
call the bid–ask spread, which is the primary source of compensation for market
makers. Typically, the bid–ask spread is small—namely, one or two cents.
The existence of a bid–ask spread, although small in magnitude, has several
important consequences in time series properties of asset returns. We brieﬂy discuss
the bid–ask bounce—namely, the bid–ask spread introduces negative lag-1 serial
correlation in an asset return. Consider the simple model of Roll (1984). The
observed market price Pt of an asset is assumed to satisfy
Pt = P ∗
t + It
S
2 ,
(5.9)
where S = Pa −Pb is the bid–ask spread, P ∗
t is the time-t fundamental value of
the asset in a frictionless market, and {It} is a sequence of independent binary
random variables with equal probabilities (i.e., It = 1 with probability 0.5 and
= −1 with probability 0.5). The It can be interpreted as an order-type indicator,
with 1 signifying buyer-initiated transaction and −1 seller-initiated transaction.
Alternatively, the model can be written as
Pt = P ∗
t +

+S/2
with probability 0.5,
−S/2
with probability 0.5.
If there is no change in P ∗
t , then the observed process of price changes is

Pt = (It −It−1)S
2 .
(5.10)
Under the assumption of It in Eq. (5.9), E(It) = 0 and Var(It) = 1, and we have
E(
Pt) = 0 and
Var(
Pt) = S2/2,
(5.11)
Cov(
Pt,
Pt−1) = −S2/4,
(5.12)
Cov(
Pt,
Pt−j) = 0,
j > 1.
(5.13)
Therefore, the autocorrelation function of
Pt is
ρj(
Pt) =

−0.5
if j = 1,
0
if j > 1.
(5.14)
The bid–ask spread thus introduces a negative lag-1 serial correlation in the series
of observed price changes. This is referred to as the bid–ask bounce in the ﬁnance
literature. Intuitively, the bounce can be seen as follows. Assume that the fundamental price P ∗
t is equal to (Pa + Pb)/2. Then Pt assumes the value Pa or Pb. If
the previously observed price is Pa (the higher value), then the current observed
price is either unchanged or lower at Pb. Thus,
Pt is either 0 or −S. However, if
--- page 264 ---

empirical characteristics of transactions data
237
the previous observed price is Pb (the lower value), then
Pt is either 0 or S. The
negative lag-1 correlation in
Pt becomes apparent. The bid–ask spread does not
introduce any serial correlation beyond lag 1, however.
A more realistic formulation is to assume that P ∗
t follows a random walk so that

P ∗
t = P ∗
t −P ∗
t−1 = ϵt, which forms a sequence of independent and identically
distributed random variables with mean zero and variance σ 2. In addition, {ϵt} is
independent of {It}. In this case, Var(
Pt) = σ 2 + S2/2, but Cov(
Pt,
Pt−j)
remains unchanged. Therefore,
ρ1(
Pt) =
−S2/4
S2/2 + σ 2 ≤0.
The magnitude of the lag-1 autocorrelation of
Pt is reduced, but the negative
effect remains when S = Pa −Pb > 0. In ﬁnance, it might be of interest to study
the components of the bid–ask spread. Interested readers are referred to Campbell
et al. (1997) and the references therein.
The effect of bid–ask spread continues to exist in portfolio returns and in multivariate ﬁnancial time series. Consider the bivariate case. Denote the bivariate
order-type indicator by It = (I1t, I2t)′, where I1t is for the ﬁrst security and I2t
for the second security. If I1t and I2t are contemporaneously positively correlated,
then the bid–ask spreads can introduce negative lag-1 cross correlations.
5.3
EMPIRICAL CHARACTERISTICS OF TRANSACTIONS DATA
Let ti be the calendar time, measured in seconds from midnight, at which the ith
transaction of an asset takes place. Associated with the transaction are several variables such as the transaction price, the transaction volume, the prevailing bid and
ask quotes, and so on. The collection of ti and the associated measurements are
referred to as the transactions data. These data have several important characteristics that do not exist when the observations are aggregated over time. Some of
the characteristics are given next.
1. Unequally Spaced Time Intervals. Transactions such as stock tradings on an
exchange do not occur at equally spaced time intervals. As such, the observed
transaction prices of an asset do not form an equally spaced time series. The
time duration between trades becomes important and might contain useful
information about market microstructure (e.g., trading intensity).
2. Discrete-Valued Prices. The price change of an asset from one transaction
to the next only occurred in multiples of tick size before January 29, 2001.
On the NYSE, the tick size was one-eighth of a dollar before June 24, 1997
and was one-sixteenth of a dollar before January 29, 2001. Therefore, the
price was a discrete-valued variable in transactions data. Although all equity
markets in the United States now use the decimal system, the price change in
consecutive trades tends to occur in multiples of one cent and can be treated
--- page 265 ---

238
high-frequency data analysis and market microstructure
approximately as a discrete-valued variable. In some markets, price change
may also be subject to limit constraints set by regulators.
3. Existence of a Daily Periodic or Diurnal Pattern. Under the normal trading
conditions, transaction activity can exhibit a periodic pattern. For instance,
on the NYSE, transactions are “heavier” at the beginning and closing of
the trading hours and “thinner” during lunch hour, resulting in a U-shaped
transaction intensity. Consequently, time durations between transactions also
exhibit a daily cyclical pattern.
4. Multiple Transactions within a Single Second. It is possible that multiple
transactions, even with different prices, occur at the same time. This is partly
due to the fact that time is measured in seconds, which may be too long a
time scale in periods of heavy trading.
To demonstrate these characteristics, we consider ﬁrst the IBM transactions data
from November 1, 1990, to January 31, 1991. These data are from the Trades,
Orders Reports, and Quotes (TORQ) data set; see Hasbrouck (1992). There are
63 trading days and 60,328 transactions. To simplify the discussion, we ignore the
price changes between trading days and focus on the transactions that occurred in
the normal trading hours from 9:30 am to 4:00 pm Eastern time. It is well known
that overnight stock returns differ substantially from intraday returns; see Stoll
and Whaley (1990) and the references therein. Table 5.1 gives the frequencies in
percentages of price change measured in the tick size of $ 1
8 = $0.125. From the
table, we make the following observations:
1. About two-thirds of the intraday transactions were without price change.
2. The price changed in one tick approximately 29% of the intraday transactions.
3. Only 2.6% of the transactions were associated with two-tick price changes.
4. Only about 1.3% of the transactions resulted in price changes of three ticks
or more.
5. The distribution of positive and negative price changes was approximately
symmetric.
Consider next the number of transactions in a 5-minute time interval. Denote
the series by xt. That is, x1 is the number of IBM transactions from 9:30 am to
9:35 am on November 1, 1990, Eastern time; x2 is the number of transactions from
9:35 am to 9:40 am; and so on. The time gaps between trading days are ignored.
Figure 5.1(a) shows the time plot of xt, and Figure 5.1(b) shows the sample ACF
TABLE 5.1
Frequencies of Price Change in Multiples of Tick Size for IBM Stock
from November 1, 1990, to January 31, 1991
Number (tick)
≤−3
−2
−1
0
1
2
≥3
Percentage
0.66
1.33
14.53
67.06
14.53
1.27
0.63
--- page 266 ---

empirical characteristics of transactions data
239
5-minute time intervals
(a)
n(trades)
0
1000
2000
3000
4000
5000
0 20406080
120
Lag
(b)
ACF
0
50
100
150
200
250
0.0 0.2 0.4 0.6 0.8 1.0
Figure 5.1
IBM intraday transactions data from 11/01/90 to 1/31/91: (a) number of transactions in
5-minute time intervals and (b) sample ACF of series in part (a).
of xt for lags 1–260. Of particular interest is the cyclical pattern of the ACF with
a periodicity of 78, which is the number of 5-minute intervals in a trading day.
The number of transactions thus exhibits a daily pattern. To further illustrate the
daily trading pattern, Figure 5.2 shows the average number of transactions within
5-minute time intervals over the 63 days. There are 78 such averages. The plot
exhibits a “smiling” or U shape, indicating heavier trading at the opening and
closing of the market and thinner trading during the lunch hours.
Since we focus on transactions that occurred during normal trading hours of
a trading day, there are 59,838 time intervals in the data. These intervals are
called the intraday durations between trades. For IBM stock, there were 6531
zero time intervals. That is, during the normal trading hours of the 63 trading
days from November 1, 1990, to January 31, 1991, multiple transactions in a
second occurred 6531 times, which is about 10.91%. Among these multiple transactions, 1002 of them had different prices, which is about 1.67% of the total
number of intraday transactions. Therefore, multiple transactions (i.e., zero durations) may become an issue in statistical modeling of the time durations between
trades.
Table 5.2 provides a two-way classiﬁcation of price movements. Here price
movements are classiﬁed into “up,” “unchanged,” and “down.” We denote them
by +, 0, and −, respectively. The table shows the price movements between two
--- page 267 ---

240
high-frequency data analysis and market microstructure
5-minute time intervals
Average
0
10
20
30
40
50
60
70
80
10
15
20
25
Figure 5.2
Time plot of average number of transactions in 5-minute time intervals. There are 78
observations, averaging over 63 trading days from 11/01/90 to 1/31/91 for IBM stock.
TABLE 5.2
Two-Way Classiﬁcation of Price Movements in Consecutive Intraday
Trades for IBM Stocka
ith Trade
(i −1)th trade
+
0
−
Margin
+
441
5498
3948
9887
0
4867
29779
5473
40119
−
4580
4841
410
9831
Margin
9888
40118
9831
59837
aThe price movements are classiﬁed into “up,” “unchanged,” and “down.” The data span is from
November 1, 1990, to January 31, 1991.
consecutive trades [i.e., from the (i −1)th to the ith transaction] in the sample.
From the table, trade-by-trade data show that:
1. Consecutive price increases or decreases are relatively rare, which are about
441/59837 = 0.74% and 410/59837 = 0.69%, respectively.
2. There is a slight edge to move from up to unchanged rather than to down;
see row 1 of the table.
3. There is a high tendency for the price to remain unchanged.
