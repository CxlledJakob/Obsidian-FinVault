# Analysis of Financial Time Series, Third Edition (Wiley -- Ruey S_ Tsay -- Wiley series in probability and statistics, 3rd ed_, -- John Wiley & Sons, -- isbn13 9780470414354 -- 9f99b80c7b2dedd477f463dc5323f3b6 -- An.pdf — pages 134–153

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
--- page 135 ---

108
linear time series analysis and its applications
Shumway, R. H. and Stoffer, D. S. (2000). Time Series Analysis and Its Applications.
Springer, New York.
Tiao, G. C. and Tsay, R. S. (1983). Consistency properties of least squares estimates of
autoregressive parameters in ARMA models. Annals of Statistics 11: 856–871.
Tsay, R. S. and Tiao, G. C. (1984). Consistent estimates of autoregressive parameters and
extended sample autocorrelation function for stationary and nonstationary ARMA models. Journal of the American Statistical Association 79: 84–96.
White, H. (1980). A heteroscedasticity consistent covariance matrix estimator and a direct
test for heteroscedasticity. Econometrica 48: 827–838.
--- page 136 ---

C H A P T E R
3
Conditional Heteroscedastic Models
The objective of this chapter is to study some methods and econometric models
available in the literature for modeling the volatility of an asset return. The models
are referred to as conditional heteroscedastic models.
Volatility is an important factor in options trading. Here volatility means the
conditional standard deviation of the underlying asset return. Consider, for example,
the price of a European call option, which is a contract giving its holder the right,
but not the obligation, to buy a ﬁxed number of shares of a speciﬁed common
stock at a ﬁxed price on a given date. The ﬁxed price is called the strike price
and is commonly denoted by K. The given date is called the expiration date. The
important time duration here is the time to expiration (measured in years), and we
denote it by ℓ. The well-known Black–Scholes option pricing formula states that
the price of such a call option is
ct = Pt(x) −Ke−rℓ(x −σt
√
ℓ),
and
x = ln(Pt/K) + rℓ
σt
√
ℓ
+ 1
2σt
√
ℓ,
(3.1)
where Pt is the current price of the underlying stock, r is the continuously compounded risk-free interest rate, σt is the annualized conditional standard deviation
of the log return of the speciﬁed stock, and (x) is the cumulative distribution
function of the standard normal random variable evaluated at x. A derivation of
the formula is given in Chapter 6. The formula has several nice interpretations,
but it sufﬁces to say here that the conditional standard deviation of the log return
of the underlying stock plays an important role. This volatility evolves over time.
If the holder can exercise her right any time on or before the expiration date, then
the option is called an American call option.
Volatility has many other ﬁnancial applications. As discussed in Chapter 7,
volatility modeling provides a simple approach to calculating value at risk of a
ﬁnancial position in risk management. It plays an important role in asset allocation
Analysis of Financial Time Series, Third Edition, By Ruey S. Tsay
Copyright 2010 John Wiley & Sons, Inc.
109
--- page 137 ---

110
conditional heteroscedastic models
under the mean-variance framework. Furthermore, modeling the volatility of a
time series can improve the efﬁciency in parameter estimation and the accuracy in
interval forecast. Finally, the volatility index of a market has recently become a
ﬁnancial instrument. The VIX volatility index compiled by the Chicago Board of
Option Exchange (CBOE) started to trade in futures on March 26, 2004.
The univariate volatility models discussed in this chapter include the autoregressive conditional heteroscedastic (ARCH) model of Engle (1982), the generalized
ARCH (GARCH) model of Bollerslev (1986), the exponential GARCH (EGARCH)
model of Nelson (1991), the threshold GARCH (TGARCH) model of Glosten,
Jagannathan, and Runkle (1993) and Zakoian (1994), the conditional heteroscedastic autoregressive moving-average (CHARMA) model of Tsay (1987), the random
coefﬁcient autoregressive (RCA) model of Nicholls and Quinn (1982), and the
stochastic volatility (SV) models of Melino and Turnbull (1990), Taylor (1994),
Harvey, Ruiz, and Shephard (1994), and Jacquier, Polson, and Rossi (1994). We
also discuss advantages and weaknesses of each volatility model and show some
applications of the models. Multivariate volatility models, including those with
time-varying correlations, are discussed in Chapter 10. The chapter also discusses
some alternative approaches to volatility modeling in Section 3.15, including use
of daily high and low prices of an asset.
3.1
CHARACTERISTICS OF VOLATILITY
A special feature of stock volatility is that it is not directly observable. For example,
consider the daily log returns of IBM stock. The daily volatility is not directly
observable from the return data because there is only one observation in a trading
day. If intraday data of the stock, such as 10-minute returns, are available, then one
can estimate the daily volatility. See Section 3.15. The accuracy of such an estimate
deserves a careful study, however. For example, stock volatility consists of intraday
volatility and overnight volatility with the latter denoting variation between trading
days. The high-frequency intraday returns contain only very limited information
about the overnight volatility. The unobservability of volatility makes it difﬁcult
to evaluate the forecasting performance of conditional heteroscedastic models. We
discuss this issue later.
In options markets, if one accepts the idea that the prices are governed by an
econometric model such as the Black–Scholes formula, then one can use the price
to obtain the “implied” volatility. Yet this approach is often criticized for using a
speciﬁc model, which is based on some assumptions that might not hold in practice.
For instance, from the observed prices of a European call option, one can use the
Black–Scholes formula in Eq. (3.1) to deduce the conditional standard deviation
σt. The resulting value of σt is called the implied volatility of the underlying stock.
However, this implied volatility is derived under the assumption that the price of
the underlying asset follows a geometric Brownian motion. It might be different
from the actual volatility. Experience shows that implied volatility of an asset return
tends to be larger than that obtained by using a GARCH type of volatility model.
--- page 138 ---

structure of a model
111
This might be due to the risk premium for volatility or to the way daily returns are
calculated. The VIX of CBOE is an implied volatility.
Although volatility is not directly observable, it has some characteristics that are
commonly seen in asset returns. First, there exist volatility clusters (i.e., volatility
may be high for certain time periods and low for other periods). Second, volatility evolves over time in a continuous manner—that is, volatility jumps are rare.
Third, volatility does not diverge to inﬁnity—that is, volatility varies within some
ﬁxed range. Statistically speaking, this means that volatility is often stationary.
Fourth, volatility seems to react differently to a big price increase or a big price
drop, referred to as the leverage effect. These properties play an important role
in the development of volatility models. Some volatility models were proposed
speciﬁcally to correct the weaknesses of the existing ones for their inability to
capture the characteristics mentioned earlier. For example, the EGARCH model
was developed to capture the asymmetry in volatility induced by big “positive”
and “negative” asset returns.
3.2
STRUCTURE OF A MODEL
Let rt be the log return of an asset at time index t. The basic idea behind volatility
study is that the series {rt} is either serially uncorrelated or with minor lower order
serial correlations, but it is a dependent series. For illustration, consider the monthly
log stock returns of Intel Corporation from January 1973 to December 2008 shown
in Figure 3.1. Figure 3.2(a) shows the sample ACF of the log return series,
which suggests no signiﬁcant serial correlations except for a minor one at lag 7.
Figure 3.2(c) shows the sample ACF of the absolute log returns (i.e., |rt|), whereas
Figure 3.2(b) shows the sample ACF of the squared log returns r2
t . These two plots
clearly suggest that the monthly log returns are not serially independent. Combining the three plots, it seems that the log returns are indeed serially uncorrelated but
dependent. Volatility models attempt to capture such dependence in the return series.
To put the volatility models in proper perspective, it is informative to consider
the conditional mean and variance of rt given Ft−1; that is,
µt = E(rt|Ft−1),
σ 2
t = Var(rt|Ft−1) = E[(rt −µt)2|Ft−1],
(3.2)
where Ft−1 denotes the information set available at time t −1. Typically, Ft−1
consists of all linear functions of the past returns. As shown by the empirical
examples of Chapter 2 and Figure 3.2, serial dependence of a stock return series rt
is weak if it exists at all. Therefore, the equation for µt in (3.2) should be simple,
and we assume that rt follows a simple time series model such as a stationary
ARMA(p, q) model with some explanatory variables. In other words, we entertain
the model
rt = µt + at,
µt =
p

i=1
φiyt−i −
q

i=1
θiat−i,
yt = rt −φ0 −
k

i=1
βixit,
(3.3)
--- page 139 ---

112
conditional heteroscedastic models
Year
Log return
1980
1990
2000
2010
−0.6
−0.4
−0.2
0.0
0.2
0.4
Figure 3.1
Time plot of monthly log returns of Intel stock from January 1973 to December 2008.
Lag
(c)
ACF
5
10
15
20
Lag
(a)
5
10
15
20
−0.2
0.0
0.2
0.4
ACF
−0.2
0.0
0.2
0.4
Lag
(b)
5
10
15
20
ACF
−0.2
0.0
0.2
0.4
Lag
(d)
5
10
15
20
PACF
−0.2
0.0
0.2
0.4
Figure 3.2
Sample ACF and PACF of various functions of monthly log stock returns of Intel Corporation from January 1973 to December 2008: (a) ACF of the log returns, (b) ACF of the squared log
returns, (c) ACF of the absolute log returns, and (d) PACF of the squared log returns.
--- page 140 ---

model building
113
for rt, where k, p, and q are nonnegative integers, and xit are explanatory variables.
Here yt is simply a notation representing the adjusted return series after removing
the effect of explanatory variables.
Model (3.3) illustrates a possible ﬁnancial application of the regression model
with time series errors of Chapter 2. The order (p, q) of an ARMA model may
depend on the frequency of the return series. For example, daily returns of a market
index often show some minor serial correlations, but monthly returns of the index
may not contain any signiﬁcant serial correlation. The explanatory variables xt in
Eq. (3.3) are ﬂexible. For example, a dummy variable can be used for the Mondays
to study the effect of the weekend on daily stock returns. In the capital asset pricing
model (CAPM), the mean equation of rt can be written as rt = φ0 + βrm,t + at,
where rm,t denotes the market return.
Combining Eqs. (3.2) and (3.3), we have
σ 2
t = Var(rt|Ft−1) = Var(at|Ft−1).
(3.4)
The conditional heteroscedastic models of this chapter are concerned with the
evolution of σ 2
t . The manner under which σ 2
t evolves over time distinguishes one
volatility model from another.
Conditional heteroscedastic models can be classiﬁed into two general categories.
Those in the ﬁrst category use an exact function to govern the evolution of σ 2
t ,
whereas those in the second category use a stochastic equation to describe σ 2
t .
The GARCH model belongs to the ﬁrst category, whereas the stochastic volatility
model is in the second category.
Throughout the book, at is referred to as the shock or innovation of an asset
return at time t and σt is the positive square root of σ 2
t . The model for µt in Eq.
(3.3) is referred to as the mean equation for rt and the model for σ 2
t is the volatility
equation for rt. Therefore, modeling conditional heteroscedasticity amounts to augmenting a dynamic equation, which governs the time evolution of the conditional
variance of the asset return, to a time series model.
3.3
MODEL BUILDING
Building a volatility model for an asset return series consists of four steps:
1. Specify a mean equation by testing for serial dependence in the data and, if
necessary, building an econometric model (e.g., an ARMA model) for the
return series to remove any linear dependence.
2. Use the residuals of the mean equation to test for ARCH effects.
3. Specify a volatility model if ARCH effects are statistically signiﬁcant, and
perform a joint estimation of the mean and volatility equations.
4. Check the ﬁtted model carefully and reﬁne it if necessary.
--- page 141 ---

114
conditional heteroscedastic models
For most asset return series, the serial correlations are weak, if any. Thus,
building a mean equation amounts to removing the sample mean from the data if
the sample mean is signiﬁcantly different from zero. For some daily return series, a
simple AR model might be needed. In some cases, the mean equation may employ
some explanatory variables such as an indicator variable for weekend or January
effects.
In what follows, we use R (both with and without OX) and S-Plus in empirical
illustrations. Other software packages (e.g., Eviews, SCA, and RATS) can also be
used.
3.3.1
Testing for ARCH Effect
For ease in notation, let at = rt −µt be the residuals of the mean equation. The
squared series a2
t is then used to check for conditional heteroscedasticity, which
is also known as the ARCH effects. Two tests are available. The ﬁrst test is to
apply the usual Ljung–Box statistics Q(m) to the {a2
t } series; see McLeod and Li
(1983). The null hypothesis is that the ﬁrst m lags of ACF of the a2
t series are zero.
The second test for conditional heteroscedasticity is the Lagrange multiplier test
of Engle (1982). This test is equivalent to the usual F statistic for testing αi = 0
(i = 1, . . . , m) in the linear regression
a2
t = α0 + α1a2
t−1 + · · · + αma2
t−m + et,
t = m + 1, . . . , T,
where et denotes the error term, m is a prespeciﬁed positive integer, and T is
the sample size. Speciﬁcally, the null hypothesis is H0 : α1 = · · · = αm = 0. Let
SSR0 = T
t=m+1(a2
t −¯ω)2, where ¯ω = (1/T ) T
t=1 a2
t is the sample mean of a2
t ,
and SSR1 = T
t=m+1 ˆe2
t , where ˆet is the least-squares residual of the prior linear
regression. Then we have
F = (SSR0 −SSR1)/m
SSR1/(T −2m −1),
which is asymptotically distributed as a chi-squared distribution with m degrees of
freedom under the null hypothesis. The decision rule is to reject the null hypothesis
if F > χ2
m(α), where χ2
m(α) is the upper 100(1 −α)th percentile of χ2
m, or the
p value of F is less than α, type-I error.
To demonstrate, we consider the monthly log stock returns of Intel Corporation
from 1973 to 2008; see Example 3.1. The series does not have signiﬁcant serial
correlations so that it can be directly used to test for the ARCH effect. Indeed,
the Q(m) statistics of the return series give Q(12) = 18.26 with a p value of
0.11, conﬁrming no serial correlations in the data. On the other hand, the Lagrange
multiplier test shows strong ARCH effects with test statistic F ≈53.62, the p
value of which is close to zero. The Ljung–Box statistics of the at series also
shows strong ARCH effects with Q(12) = 89.85, the p value of which is close to
zero.
--- page 142 ---

the arch model
115
S-Plus Demonstration
Denote the return series by intc. Note that the command archTest applies
directly to the at series, not to a2
t .
> da=read.table("m-intc7308.txt",header=T)
> intc=log(da[,2]+1)
> autocorTest(intc,lag=12)
Test for Autocorrelation: Ljung-Box
Null Hypothesis: no autocorrelation
Test Statistics:
Test Stat 18.2635
p.value
0.1079
Dist. under Null: chi-square with 12 degrees of freedom
Total Observ.: 432
> archTest(intc,lag=12)
Test for ARCH Effects: LM Test
Null Hypothesis: no ARCH effects
Test Statistics:
Test Stat 53.6197
p.value
0.0000
Dist. under Null: chi-square with 12 degrees of freedom
R Demonstration
> da=read.table("m-intc7308.txt",header=T)
> intc=log(da[,2]+1)
> Box.test(intc,lag=12,type=’Ljung’)
Box-Ljung test
data:
intc
X-squared = 18.2635, df = 12, p-value = 0.1079
> at=intc-mean(intc)
> Box.test(at^2,lag=12,type=’Ljung’)
Box-Ljung test
data:
at^2
X-squared = 89.8509, df = 12, p-value = 5.274e-14
3.4
THE ARCH MODEL
The ﬁrst model that provides a systematic framework for volatility modeling
is the ARCH model of Engle (1982). The basic idea of ARCH models is that
(a) the shock at of an asset return is serially uncorrelated, but dependent, and
--- page 143 ---

116
conditional heteroscedastic models
(b) the dependence of at can be described by a simple quadratic function of its
lagged values. Speciﬁcally, an ARCH(m) model assumes that
at = σtϵt,
σ 2
t = α0 + α1a2
t−1 + · · · + αma2
t−m,
(3.5)
where {ϵt} is a sequence of independent and identically distributed (iid) random
variables with mean zero and variance 1, α0 > 0, and αi ≥0 for i > 0. The coefﬁ-
cients αi must satisfy some regularity conditions to ensure that the unconditional
variance of at is ﬁnite. In practice, ϵt is often assumed to follow the standard
normal or a standardized Student-t or a generalized error distribution.
From the structure of the model, it is seen that large past squared shocks {a2
t−i}m
i=1
imply a large conditional variance σ 2
t for the innovation at. Consequently, at tends
to assume a large value (in modulus). This means that, under the ARCH framework,
large shocks tend to be followed by another large shock. Here I use the word
tend because a large variance does not necessarily produce a large realization. It
only says that the probability of obtaining a large variate is greater than that of
a smaller variance. This feature is similar to the volatility clusterings observed in
asset returns.
The ARCH effect also occurs in other ﬁnancial time series. Figure 3.3 shows
the time plots of (a) the percentage changes in Deutsche mark/U.S. dollar exchange
rate measured in 10-minute intervals from June 5, 1989, to June 19, 1989, for 2488
observations, and (b) the squared series of the percentage changes. Big percentage
fx
0
500
1000
1500
2000
2500
−0.6
−0.2
0.2
Time index
(b)
(a)
sq−fx
0
500
1000
1500
2000
2500
0.0 0.1 0.2 0.3 0.4
Figure 3.3
(a) Time plot of 10-minute returns of exchange rate between Deutsche mark and U.S.
dollar from June 5, 1989, to June 19, 1989, and (b) the squared returns.
--- page 144 ---

the arch model
117
Lag
(a)
ACF
0
10
20
30
−0.10
0.0 0.05 0.10
Lag
(b)
PACF
0
10
20
30
−0.10
0.0 0.05 0.10
Figure 3.4
(a) Sample autocorrelation function of return series of mark/dollar exchange rate and (b)
sample partial autocorrelation function of squared returns.
changes occurred occasionally, but there were certain stable periods. Figure 3.4(a)
shows the sample ACF of the percentage change series. Clearly, the series has no
serial correlation. Figure 3.4(b) shows the sample PACF of the squared series of
percentage change. It is seen that there are some big spikes in the PACF. Such
spikes suggest that the percentage changes are not serially independent and have
some ARCH effects.
Remark.
Some authors use ht to denote the conditional variance in Eq. (3.5).
In this case, the shock becomes at = √htϵt.
□
3.4.1
Properties of ARCH Models
To understand the ARCH models, it pays to carefully study the ARCH(1) model
at = σtϵt,
σ 2
t = α0 + α1a2
t−1,
where α0 > 0 and α1 ≥0. First, the unconditional mean of at remains zero because
E(at) = E[E(at|Ft−1)] = E[σtE(ϵt)] = 0.
--- page 145 ---

118
conditional heteroscedastic models
Second, the unconditional variance of at can be obtained as
Var(at) = E(a2
t ) = E[E(a2
t |Ft−1)]
= E(α0 + α1a2
t−1) = α0 + α1E(a2
t−1).
Because at is a stationary process with E(at) = 0, Var(at) = Var(at−1) = E(a2
t−1).
Therefore, we have Var(at) = α0 + α1Var(at) and Var(at) = α0/(1 −α1). Since the
variance of at must be positive, we require 0 ≤α1 < 1. Third, in some applications,
we need higher order moments of at to exist and, hence, α1 must also satisfy some
additional constraints. For instance, to study its tail behavior, we require that the
fourth moment of at is ﬁnite. Under the normality assumption of ϵt in Eq. (3.5),
we have
E(a4
t |Ft−1) = 3[E(a2
t |Ft−1)]2 = 3(α0 + α1a2
t−1)2.
Therefore,
E(a4
t ) = E[E(a4
t |Ft−1)] = 3E(α0 + α1a2
t−1)2 = 3E

α2
0 + 2α0α1a2
t−1 + α2
1a4
t−1

.
If at is fourth-order stationary with m4 = E(a4
t ), then we have
m4 = 3[α2
0 + 2α0α1Var(at) + α2
1m4]
= 3α2
0

1 + 2
α1
1 −α1

+ 3α2
1m4.
Consequently,
m4 =
3α2
0(1 + α1)
(1 −α1)(1 −3α2
1).
This result has two important implications: (a) since the fourth moment of at
is positive, we see that α1 must also satisfy the condition 1 −3α2
1 > 0; that is,
0 ≤α2
1 < 1
3; and (b) the unconditional kurtosis of at is
E(a4
t )
[Var(at)]2 = 3
α2
0(1 + α1)
(1 −α1)(1 −3α2
1) × (1 −α1)2
α2
0
= 3 1 −α2
1
1 −3α2
1
> 3.
Thus, the excess kurtosis of at is positive and the tail distribution of at is heavier
than that of a normal distribution. In other words, the shock at of a conditional
Gaussian ARCH(1) model is more likely than a Gaussian white noise series to
produce “outliers.” This is in agreement with the empirical ﬁnding that “outliers”
appear more often in asset returns than that implied by an iid sequence of normal
random variates.
These properties continue to hold for general ARCH models, but the formulas
become more complicated for higher order ARCH models. The condition αi ≥0 in
--- page 146 ---

the arch model
119
Eq. (3.5) can be relaxed. It is a condition to ensure that the conditional variance σ 2
t
is positive for all t. In fact, a natural way to achieve positiveness of the conditional
variance is to rewrite an ARCH(m) model as
at = σtϵt,
σ 2
t = α0 + A′
m,t−1Am,t−1,
(3.6)
where Am,t−1 = (at−1, . . . , at−m)′ and  is an m × m nonnegative deﬁnite matrix.
The ARCH(m) model in Eq. (3.5) requires  to be diagonal. Thus, Engle’s model
uses a parsimonious approach to approximate a quadratic function. A simple way to
achieve Eq. (3.6) is to employ a random-coefﬁcient model for at; see the CHARMA
and RCA models discussed later.
3.4.2
Weaknesses of ARCH Models
The advantages of ARCH models include properties discussed in the previous
section. The model also has some weaknesses:
1. The model assumes that positive and negative shocks have the same effects
on volatility because it depends on the square of the previous shocks. In
practice, it is well known that the price of a ﬁnancial asset responds differently
to positive and negative shocks.
2. The ARCH model is rather restrictive. For instance, α2
1 of an ARCH(1) model
must be in the interval [0, 1
3] if the series has a ﬁnite fourth moment. The
constraint becomes complicated for higher order ARCH models. In practice,
it limits the ability of ARCH models with Gaussian innovations to capture
excess kurtosis.
3. The ARCH model does not provide any new insight for understanding the
source of variations of a ﬁnancial time series. It merely provides a mechanical
way to describe the behavior of the conditional variance. It gives no indication
about what causes such behavior to occur.
4. ARCH models are likely to overpredict the volatility because they respond
slowly to large isolated shocks to the return series.
3.4.3
Building an ARCH Model
Among volatility models, specifying an ARCH model is relatively easy. Details
are given below.
Order Determination
If an ARCH effect is found to be signiﬁcant, one can use the PACF of a2
t to
determine the ARCH order. Using PACF of a2
t to select the ARCH order can be
justiﬁed as follows. From the model in Eq. (3.5), we have
σ 2
t = α0 + α1a2
t−1 + · · · + αma2
t−m.
--- page 147 ---

120
conditional heteroscedastic models
For a given sample, a2
t is an unbiased estimate of σ 2
t . Therefore, we expect that a2
t
is linearly related to a2
t−1, . . . , a2
t−m in a manner similar to that of an autoregressive
model of order m. Note that a single a2
t is generally not an efﬁcient estimate of
σ 2
t , but it can serve as an approximation that could be informative in specifying
the order m.
Alternatively, deﬁne ηt = a2
t −σ 2
t . It can be shown that {ηt} is an uncorrelated
series with mean 0. The ARCH model then becomes
a2
t = α0 + α1a2
t−1 + · · · + αma2
t−m + ηt,
which is in the form of an AR(m) model for a2
t , except that {ηt} is not an iid series.
From Chapter 2, PACF of a2
t is a useful tool to determine the order m. Because
{ηt} are not identically distributed, the least-squares estimates of the prior model
are consistent but not efﬁcient. The PACF of a2
t may not be effective when the
sample size is small.
Estimation
Several likelihood functions are commonly used in ARCH estimation, depending on
the distributional assumption of ϵt. Under the normality assumption, the likelihood
function of an ARCH(m) model is
f (a1, . . . , aT |α) = f (aT |FT −1)f (aT −1|FT −2) · · · f (am+1|Fm)f (a1, · · · , am|α)
=
T
t=m+1
1

2πσ 2
t
exp

−a2
t
2σ 2
t

× f (a1, . . . , am|α),
where α = (α0, α1, . . . , αm)′ and f (a1, . . . , am|α) is the joint probability density
function of a1, . . . , am. Since the exact form of f (a1, . . . , am|α) is complicated,
it is commonly dropped from the prior likelihood function, especially when the
sample size is sufﬁciently large. This results in using the conditional-likelihood
function
f (am+1, . . . , aT |α, a1, . . . , am) =
T
t=m+1
1

2πσ 2
t
exp

−a2
t
2σ 2
t

,
where σ 2
t can be evaluated recursively. We refer to estimates obtained by maximizing the prior likelihood function as the conditional maximum-likelihood estimates
(MLEs) under normality.
Maximizing the conditional-likelihood function is equivalent to maximizing its
logarithm, which is easier to handle. The conditional log-likelihood function is
ℓ(am+1, . . . , aT |α, a1, . . . , am) =
T

t=m+1

−1
2 ln(2π) −1
2 ln(σ 2
t ) −1
2
a2
t
σ 2
t

.
--- page 148 ---

the arch model
121
Since the ﬁrst term ln(2π) does not involve any parameters, the log-likelihood
function becomes
ℓ(am+1, . . . , aT |α, a1, . . . , am) = −
T

t=m+1

1
2 ln(σ 2
t ) + 1
2
a2
t
σ 2
t

,
where σ 2
t = α0 + α1a2
t−1 + · · · + αma2
t−m can be evaluated recursively.
In some applications, it is more appropriate to assume that ϵt follows a
heavy-tailed distribution such as a standardized Student-t distribution. Let xv be a
Student-t distribution with v degrees of freedom. Then Var(xv) = v/(v −2) for
v > 2, and we use ϵt = xv/√v/(v −2). The probability density function of ϵt is
f (ϵt|v) =
[(v + 1)/2]
(v/2)√(v −2)π

1 +
ϵ2
t
v −2
	−(v+1)/2
,
v > 2,
(3.7)
where (x) is the usual gamma function (i.e., (x) =
 ∞
0 yx−1e−y dy). Using
at = σtϵt, we obtain the conditional-likelihood function of at as
f (am+1, . . . , aT |α, Am) =
T
t=m+1
[(v + 1)/2]
(v/2)√(v −2)π
1
σt

1 +
a2
t
(v −2)σ 2
t
−(v+1)/2
,
where v > 2 and Am = (a1, a2, . . . , am). We refer to the estimates that maximize the
prior likelihood function as the conditional MLEs under t distribution. The degrees
of freedom of the t distribution can be speciﬁed a priori or estimated jointly with
other parameters. A value between 4 and 8 is often used if it is prespeciﬁed.
If the degrees of freedom v of the Student-t distribution is prespeciﬁed, then
the conditional log-likelihood function is
ℓ(am+1, . . . , aT |α, Am) = −
T

t=m+1

v + 1
2
ln

1 +
a2
t
(v −2)σ 2
t

+ 1
2 ln(σ 2
t )

.
(3.8)
If one wishes to estimate v jointly with other parameters, then the log-likelihood
function becomes
ℓ(am+1, . . . , aT |α, v, Am) = (T −m)

ln


v + 1
2
	
−ln


v
2
!
−0.5 ln[(v −2)π]
"
+ ℓ(am+1, . . . , aT |α, Am),
where the second term is given in Eq. (3.8).
Besides fat tails, empirical distributions of asset returns may also be skewed.
To handle this additional characteristic of asset returns, the Student-t distribution
--- page 149 ---

122
conditional heteroscedastic models
has been modiﬁed to become a skew-Student-t distribution. There are multiple versions of skew-Student-t distribution, but we shall adopt the approach of Fern´andez
and Steel (1998), which can introduce skewness into any continuous unimodal and
symmetric (with respect to 0) univariate distribution. Speciﬁcally, for the innovation ϵt of an ARCH process, Lambert and Laurent (2001) apply the Fern´andez and
Steel method to the standardized Student-t distribution in Eq. (3.7) to obtain a standardized skew-Student-t distribution. The resulting probability density function is
g(ϵt|ξ, v) =



2
ξ + 1
ξ
ϱf [ξ(ϱϵt + ω)|v]
if ϵt < −ω/ϱ,
2
ξ + 1
ξ
ϱf [(ϱϵt + ω)/ξ|v]
if ϵt ≥−ω/ϱ,
(3.9)
where f (·) is the probability density function (pdf) of the standardized Student-t
distribution in Eq. (3.7), ξ is the skewness parameter, v > 2 is the degrees of
freedom, and the parameters ϱ and ω are given below:
ϖ = [(v −1)/2]
√
v −2
√π(v/2)
(ξ −1
ξ ),
ϱ2 = (ξ 2 + 1
ξ 2 −1) −ϖ 2.
In Eq. (3.9), ξ 2 is equal to the ratio of probability masses above and below the
mode of the distribution and, hence, it is a measure of the skewness.
Finally, ϵt may assume a generalized error distribution (GED) with probability
density function
f (x) = v exp(−1
2|x/λ|v)
λ2(1+1/v)(1/v) ,
−∞< x < ∞,
0 < v ≤∞,
(3.10)
where (·) is the gamma function and λ = [2(−2/v)(1/v)/(3/v)]1/2. This distribution reduces to a Gaussian distribution if v = 2, and it has heavy tails when
v < 2. The conditional log-likelihood function ℓ(am+1, . . . , aT |α, Am) can easily
be obtained.
Remark.
Skew Student-t, skew normal, and skew GED distributions are available in the fGarch package of Rmetrics. The commands are sstd, snorm, and
sged, respectively. See the R demonstration below for an example.
□
Model Checking
For a properly speciﬁed ARCH model, the standardized residuals
˜at = at
σt
form a sequence of iid random variables. Therefore, one can check the adequacy
of a ﬁtted ARCH model by examining the series {˜at}. In particular, the Ljung–Box
--- page 150 ---

the arch model
123
statistics of ˜at can be used to check the adequacy of the mean equation and that
of ˜a2
t can be used to test the validity of the volatility equation. The skewness,
kurtosis, and quantile-to-quantile plot (i.e., QQ plot) of {˜at} can be used to check
the validity of the distribution assumption. Many residual plots are available in
S-Plus for model checking.
Forecasting
Forecasts of the ARCH model in Eq. (3.5) can be obtained recursively as those
of an AR model. Consider an ARCH(m) model. At the forecast origin h, the
1-step-ahead forecast of σ 2
h+1 is
σ 2
h(1) = α0 + α1a2
h + · · · + αma2
h+1−m.
The 2-step-ahead forecast is
σ 2
h(2) = α0 + α1σ 2
h(1) + α2a2
h + · · · + αma2
h+2−m,
and the ℓ-step-ahead forecast for σ 2
h+ℓis
σ 2
h(ℓ) = α0 +
m

i=1
αiσ 2
h(ℓ−i),
(3.11)
where σ 2
h(ℓ−i) = a2
h+ℓ−i if ℓ−i ≤0.
3.4.4
Some Examples
In this section, we illustrate ARCH modeling by considering two examples.
Example 3.1.
We ﬁrst apply the modeling procedure to build a simple ARCH
model for the monthly log returns of Intel stock. The sample ACF and PACF
of the squared returns in Figure 3.2 clearly show the existence of conditional
heteroscedasticity. This is conﬁrmed by the ARCH test shown in Section 3.3.1,
and we proceed to identify the order of an ARCH model. The sample PACF in
Figure 3.2(d) indicates that an ARCH(3) model might be appropriate. Consequently,
we specify the model
rt = µ + at,
at = σtϵt,
σ 2
t = α0 + α1a2
t−1 + α2a2
t−2 + α3a2
t−3
for the monthly log returns of Intel stock. Assuming that ϵt are iid standard normal,
we obtain the ﬁtted model
rt = 0.0122 + at,
σ 2
t = 0.0106 + 0.2131a2
t−1 + 0.0770a2
t−2 + 0.0599a2
t−3,
where the standard errors of the parameters are 0.0057, 0.0010, 0.0757, 0.0480,
and 0.0688, respectively; see the output below. While the estimates meet the general requirement of an ARCH(3) model, the estimates of α2 and α3 appear to be
statistically nonsigniﬁcant at the 5% level. Therefore, the model can be simpliﬁed.
--- page 151 ---

124
conditional heteroscedastic models
S-Plus Demonstration
The following output has been edited and % marks explanation:
> module(finmetrics)
> da=read.table("m-intc7308.txt",header=T)
> intc=log(da[,2]+1)
> arch3.fit=garch(intc∼1,∼garch(3,0))
> summary(arch3.fit)
garch(formula.mean = intc ∼1, formula.var = ∼garch(3, 0))
Mean Equation: structure(.Data = intc ∼
1, class = "formula")
Conditional Variance Equation:structure(.Data=∼garch(3,0),..)
Conditional Distribution:
gaussian
--------------------------------------------------------------
Estimated Coefficients:
--------------------------------------------------------------
Value Std.Error t value Pr(>|t|)
C 0.01216 0.0056986
2.1341 0.033402
A 0.01058 0.0009643 10.9739 0.000000
ARCH(1) 0.21307 0.0756708
2.8157 0.005093
ARCH(2) 0.07698 0.0480170
1.6032 0.109638
ARCH(3) 0.05988 0.0688081
0.8703 0.384628
--------------------------------------------------------------
> arch1=garch(intc∼1,∼garch(1,0))
> summary(arch1)
garch(formula.mean = intc ∼1, formula.var = ∼garch(1, 0))
Conditional Distribution:
gaussian
--------------------------------------------------------------
Estimated Coefficients:
--------------------------------------------------------------
Value Std.Error t value
Pr(>|t|)
C 0.01261 0.0052624
2.397 1.695e-02
A 0.01113 0.0009971
11.164 0.000e+00
ARCH(1) 0.35602 0.0761267
4.677 3.912e-06
--------------------------------------------------------------
AIC(3) = -570.0179, BIC(3) = -557.8126
Ljung-Box test for standardized residuals:
--------------------------------------------------------------
Statistic P-value Chi^2-d.f.
14.26
0.2844
12
Ljung-Box test for squared standardized residuals:
--------------------------------------------------------------
Statistic
P-value Chi^2-d.f.
32.11 0.001329
12
> stres=arch1$residuals/arch1$sigma.t %standardized residuals
--- page 152 ---

the arch model
125
> autocorTest(stres,lag=10)
Test for Autocorrelation: Ljung-Box
Null Hypothesis: no autocorrelation
Test Statistics:
Test Stat 12.6386,
p.value
0.2446
Dist. under Null: chi-square with 10 degrees of freedom
> archTest(stres,lag=10)
Test for ARCH Effects: LM Test
Null Hypothesis: no ARCH effects
Test Statistics:
Test Stat 14.7481,
p.value
0.1415
Dist. under Null: chi-square with 10 degrees of freedom
> arch1$asymp.sd
%Obtain unconditional standard error
[1] 0.1314698
> plot(arch1)
% Obtain various plots, including the
% fitted volatility series.
Dropping the two nonsigniﬁcant parameters, we obtain the model
rt = 0.0126 + at,
σ 2
t = 0.0111 + 0.3560a2
t−1,
(3.12)
where the standard errors of the parameters are 0.0053, 0.0010, and 0.0761, respectively. All the estimates are highly signiﬁcant. Figure 3.5 shows the standardized
residuals {˜at} and the sample ACF of some functions of {˜at}. The Ljung–Box
statistics of standardized residuals give Q(10) = 12.64 with a p value of 0.24
and those of {˜a2
t } give Q(10) = 14.75 with a p value of 0.14. See the output.
Consequently, the ARCH(1) model in Eq. (3.12) is adequate for describing the
conditional heteroscedasticity of the data at the 5% signiﬁcance level.
The ARCH(1) model in Eq. (3.12) has some interesting properties. First, the
expected monthly log return for Intel stock is about 1.26%, which is remarkable,
especially since the data span includes the period after the Internet bubble. Second, ˆα2
1 = 0.3562 < 1
3 so that the unconditional fourth moment of the monthly
log return of Intel stock exists. Third, the unconditional standard deviation of rt
is √0.0111/(1 −0.356) ≈0.1315. Finally, the ARCH(1) model can be used to
predict the monthly volatility of Intel stock returns.
t Innovation
For comparison, we also ﬁt an ARCH(1) model with Student-t innovations to the
series. The resulting model is
rt = 0.0169 + at,
σ 2
t = 0.0120 + 0.2845a2
t−1,
(3.13)
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
