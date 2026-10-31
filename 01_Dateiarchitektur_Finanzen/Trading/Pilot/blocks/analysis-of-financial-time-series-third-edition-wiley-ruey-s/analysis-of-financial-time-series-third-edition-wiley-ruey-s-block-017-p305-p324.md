# Analysis of Financial Time Series, Third Edition (Wiley -- Ruey S_ Tsay -- Wiley series in probability and statistics, 3rd ed_, -- John Wiley & Sons, -- isbn13 9780470414354 -- 9f99b80c7b2dedd477f463dc5323f3b6 -- An.pdf — pages 305–324

--- page 305 ---

278
high-frequency data analysis and market microstructure
Weibull Distribution
A random variable X has a Weibull distribution with parameters α and β (α > 0,
β > 0) if its pdf is given by
f (x|α, β) =



α
βα xα−1e−(x/β)α
if x ≥0,
0
if x < 0,
where β and α are the scale and shape parameters of the distribution. The mean
and variance of X are
E(X) = β

1 + 1
α

,
Var(X) = β2



1 + 2
α

−



1 + 1
α
	2+
,
and the CDF of X is
F(x|α, β) =

0
if x < 0,
1 −e−(x/β)α
if x ≥0.
When α = 1, the Weibull distribution reduces to an exponential distribution.
Deﬁne Y = X/[β(1 + 1/α)]. We have E(Y) = 1 and the pdf of Y is
f (y|α) =



α



1 + 1
α
	α
yα−1 exp

−



1 + 1
α

y
α"
if y ≥0,
0
otherwise,
(5.56)
where the scale parameter β disappears due to standardization. The CDF of the
standardized Weibull distribution is
F(y|α) =



0
if y < 0,
1 −exp

−



1 + 1
α

y
α"
if y > 0,
and we have E(Y) = 1 and Var(Y) = (1 + 2/α)/[(1 + 1/α)]2 −1. For a duration model with Weibull innovations, the pdf in Eq. (5.56) is used in the maximumlikelihood estimation.
Generalized Gamma Distribution
A random variable X has a generalized gamma distribution with parameter α, β, κ
(α > 0, β > 0, and κ > 0) if its pdf is given by
f (x|α, β, κ) =



αxκα−1
βκα(κ) exp

−
 x
β
	α
if x ≥0,
0
otherwise,
--- page 306 ---

appendix b: hazard function
279
where β is a scale parameter, and α and κ are shape parameters. This distribution
can be written as
G =
X
β
	α
,
where G is a standard gamma random variable with parameter κ. The pdf of X
can be obtained from that of G by the technique of changing variables. Similarly,
the moments of X can be obtained from that of G in Eq. (5.55) by
E(Xm) = E[(βG1/α)m] = βmE(Gm/α) = βm (κ + m/α)
(κ)
= βm(κ + m/α)
(κ)
.
When κ = 1, the generalized gamma distribution reduces to that of a Weibull
distribution. Thus, the exponential and Weibull distributions are special cases of
the generalized gamma distribution.
The expectation of a generalized gamma distribution is E(X) = β(κ + 1/α)/
(κ). In duration models, we need a distribution with unit expectation. Therefore,
deﬁning a random variable Y = λX/β, where λ = (κ)/ (κ + 1/α), we have
E(Y) = 1 and the pdf of Y is
f (y|α, κ) =



αyκα−1
λκα(κ) exp

−
y
λ
α!
if y > 0,
0
otherwise,
(5.57)
where again the scale parameter β disappears and λ = (κ)/ (κ + 1/α).
APPENDIX B: HAZARD FUNCTION
A useful concept in modeling duration is the hazard function implied by a distribution function. For a random variable X, the survival function is deﬁned as
S(x) ≡P (X > x) = 1 −P (X ≤x) = 1 −CDF(x),
x > 0,
which gives the probability that a subject, which follows the distribution of X,
survives at the time x. The hazard function (or intensity function) of X is then
deﬁned by
h(x) = f (x)
S(x) ,
(5.58)
where f (·) and S(·) are the pdf and survival function of X, respectively.
--- page 307 ---

280
high-frequency data analysis and market microstructure
Example 5.6.
For the Weibull distribution with parameters α and β, the survival function and hazard function are
S(x|α, β) = exp

−
 x
β
	α
,
h(x|α, β) = α
βα xα−1,
x > 0.
In particular, when α = 1, we have h(x|β) = 1/β. Therefore, for an exponential
distribution, the hazard function is constant. For a Weibull distribution, the hazard is a monotone function. If α > 1, then the hazard function is monotonously
increasing. If α < 1, the hazard function is monotonously decreasing. For the generalized gamma distribution, the survival function and, hence, the hazard function
involve the incomplete gamma function. Yet the hazard function may exhibit various patterns, including U shape or inverted U shape. Thus, the generalized gamma
distribution provides a ﬂexible approach to modeling the duration of stock transactions.
For the standardized Weibull distribution, the survival and hazard functions are
S(y|α) = exp

−



1 + 1
α

y
α"
,
h(y|α) = α



1 + 1
α
	α
yα−1,
y > 0.
APPENDIX C: SOME RATS PROGRAMS FOR DURATION MODELS
The data used are adjusted time durations of intraday transactions of IBM stock
from November 1 to November 9, 1990. The ﬁle name is ibm1to5.txt and it has
3534 observations.
Program for Estimating a WACD(1,1) Model
all 0
3534:1
open data ibm1to5.txt
data(org=obs) / x r1
set psi = 1.0
nonlin a0 a1 b1 al
frml gvar = a0+a1*x(t-1)+b1*psi(t-1)
frml gma = %LNGAMMA(1.0+1.0/al)
frml gln =al*gma(t)+log(al)-log(x(t)) $
+al*log(x(t)/(psi(t)=gvar(t)))-(exp(gma(t))*x(t)/psi(t))**al
smpl 2 3534
compute a0 = 0.2, a1 = 0.1, b1 = 0.1, al = 0.8
maximize(method=bhhh,recursive,iterations=150) gln
set fv = gvar(t)
set resid = x(t)/fv(t)
set residsq = resid(t)*resid(t)
--- page 308 ---

appendix c: some rats programs for duration models
281
cor(qstats,number=20,span=10) resid
cor(qstats,number=20,span=10) residsq
Program for Estimating a GACD(1,1) Model
all 0
3534:1
open data ibm1to5.txt
data(org=obs) / x r1
set psi = 1.0
nonlin a0 a1 b1 al ka
frml cv = a0+a1*x(t-1)+b1*psi(t-1)
frml gma = %LNGAMMA(ka)
frml lam = exp(gma(t))/exp(%LNGAMMA(ka+(1.0/al)))
frml xlam = x(t)/(lam(t)*(psi(t)=cv(t)))
frml gln =-gma(t)+log(al/x(t))+ka*al*log(xlam(t))
-(xlam(t))**al
smpl 2 3534
compute a0 = 0.238, a1 = 0.075, b1 = 0.857, al = 0.5, ka = 4.0
nlpar(criterion=value,cvcrit=0.00001)
maximize(method=bhhh,recursive,iterations=150) gln
set fv = cv(t)
set resid = x(t)/fv(t)
set residsq = resid(t)*resid(t)
cor(qstats,number=20,span=10) resid
cor(qstats,number=20,span=10) residsq
Program for Estimating a TAR-WACD(1,1) Model
The threshold 3.79 is prespeciﬁed.
all 0 3534:1
open data ibm1to5.txt
data(org=obs) / x rt
set psi = 1.0
nonlin a1 a2 al b0 b2 bl
frml u = ((x(t-1)-3.79)/abs(x(t-1)-3.79)+1.0)/2.0
frml cp1 = a1*x(t-1)+a2*psi(t-1)
frml gma1 = %LNGAMMA(1.0+1.0/al)
frml cp2 = b0+b2*psi(t-1)
frml gma2 = %LNGAMMA(1.0+1.0/bl)
frml cp = cp1(t)*(1-u(t))+cp2(t)*u(t)
frml gln1 =al*gma1(t)+log(al)-log(x(t)) $
+al*log(x(t)/(psi(t)=cp(t)))-(exp(gma1(t))*x(t)/psi(t))**al
frml gln2 =bl*gma2(t)+log(bl)-log(x(t)) $
+bl*log(x(t)/(psi(t)=cp(t)))-(exp(gma2(t))*x(t)/psi(t))**bl
frml gln = gln1(t)*(1-u(t))+gln2(t)*u(t)
smpl 2 3534
compute a1 = 0.2, a2 = 0.85, al = 0.9
--- page 309 ---

282
high-frequency data analysis and market microstructure
compute b0 = 1.8, b2 = 0.5, bl = 0.8
maximize(method=bhhh,recursive,iterations=150) gln
set fv = cp(t)
set resid = x(t)/fv(t)
set residsq = resid(t)*resid(t)
cor(qstats,number=20,span=10) resid
cor(qstats,number=20,span=10) residsq
EXERCISES
5.1. Let rt be the log return of an asset at time t. Assume that {rt} is a Gaussian
white noise series with mean 0.05 and variance 1.5. Suppose that the probability of a trade at each time point is 40% and is independent of rt. Denote
the observed return by ro
t . Is ro
t serially correlated? If yes, calculate the ﬁrst
three lags of autocorrelations of ro
t .
5.2. Let Pt be the observed market price of an asset, which is related to the fundamental value of the asset P ∗
t via Eq. (5.9). Assume that
P ∗
t = P ∗
t −P ∗
t−1
forms a Gaussian white noise series with mean zero and variance 1.0. Suppose that the bid–ask spread is two ticks. What is the lag-1 autocorrelation of the price change series
Pt = Pt −Pt−1 when the tick size is $ 1
8?
What is the lag-1 autocorrelation of the price change when the tick size
is $ 1
16?
5.3. The ﬁle ibm-d2-dur.txt contains the adjusted durations between trades of
IBM stock on November 2, 1990. The ﬁle has three columns consisting of
day, time of trade measured in seconds from midnight, and adjusted durations.
(a) Build an EACD model for the adjusted duration and check the ﬁtted
model.
(b) Build a WACD model for the adjusted duration and check the ﬁtted
model.
(c) Build a GACD model for the adjusted duration and check the ﬁtted
model.
(d) Compare the prior three duration models.
5.4. The ﬁle mmm9912-dtp.txt contains the transactions data of the stock of 3M
Company in December 1999. There are three columns: day of the month, time
of transaction in seconds from midnight, and transaction price. Transactions
that occurred after 4:00 pm Eastern time are excluded.
(a) Is there a diurnal pattern in 3M stock trading? You may construct a time
series nt, which denotes the number of trades in a 5-minute time interval
to answer this question.
(b) Use the price series to conﬁrm the existence of a bid–ask bounce in
intraday trading of 3M stock.
--- page 310 ---

exercises
283
(c) Tabulate the frequencies of price change in multiples of tick size $ 1
16.
You may combine changes with 5 ticks or more into a category and those
with −5 ticks or beyond into another category.
5.5. Consider again the transactions data of 3M stock in December 1999.
(a) Use the data to construct an intraday 5-minute log return series. Use the
simple average of all transaction prices within a 5-minute interval as the
stock price for the interval. Is the series serially correlated? You may use
Ljung–Box statistics to test the hypothesis with the ﬁrst 10 lags of the
sample autocorrelation function.
(b) There are seventy-seven 5-minute returns in a normal trading day. Some
researchers suggest that the sum of squares of the intraday 5-minute
returns can be used as a measure of daily volatility. Apply this approach
and calculate the daily volatility of the log return of 3M stock in December 1999. Discuss the validity of such a procedure to estimate daily
volatility.
5.6. The ﬁle mmm9912-adur.txt contains an adjusted intraday trading duration
of 3M stock in December 1999. There are thirty-nine 10-minute time intervals
in a trading day. Let di be the average of all log durations for the ith 10-
minute interval across all trading days in December 1999. Deﬁne an adjusted
duration as tj/ exp(di), where j is in the ith 10-minute interval. Note that
more sophisticated methods can be used to adjust the diurnal pattern of
trading duration. Here we simply use a local average.
(a) Is there a diurnal pattern in the adjusted duration series? Why?
(b) Build a duration model for the adjusted series using exponential innovations. Check the ﬁtted model.
(c) Build a duration model for the adjusted series using Weibull innovations.
Check the ﬁtted model.
(d) Build a duration model for the adjusted series using generalized gamma
innovations. Check the ﬁtted model.
(e) Compare and comment on the three duration models built before.
5.7. To gain experience in analyzing high-frequency ﬁnancial data, consider the
trade data of Boeing stock from December 1 to December 5, 2008. The data
are in ﬁve ﬁles: taq-td-ba12012008.txt to taq-td-ba12052008.txt.
Each ﬁle has ﬁve columns, namely hour, minute, second, price, and volume. Only transactions within the normal trading hours (9:30 am to 4:00 pm
Eastern time) are kept. Construct a time series of the number of trades in an
intraday 5-minute time interval. Is there any diurnal pattern in the constructed
series? You can simply compute the sample ACF of the series to answer this
question.
5.8. Again, consider the high-frequency data of Boeing stock from December 1
to December 5, 2008. Construct an intraday 5-minute return series. Note that
--- page 311 ---

284
high-frequency data analysis and market microstructure
the price of the stock in a 5-minute interval (e.g., 9:30 to 9:35 am) is the last
transaction price within the time interval. For simplicity, ignore overnight
returns. Are there serial correlations in the 5-minute return series? Use 10
lags of the ACF and 5% signiﬁcance level to perform of test.
5.9. Consider the same problem as in Exercise 5.8, but use 10-minute time intervals.
5.10. Again, consider the high-frequency data of Boeing stock. Compute the percentage of consecutive transactions without price change in the sample.
REFERENCES
Box, G. E. P. and Cox, D. R. (1964). An analysis of transformations (with discusions).
Journal of the Royal Statistical Society, Series B 26: 211–246.
Box, G. E. P. and Tiao, G. C. (1975). Intervention analysis with applications to economic and
environmental problems. Journal of the American Statistical Association 70: 70–79.
Campbell, J. Y., Lo, A. W., and MacKinlay, A. C. (1997). The Econometrics of Financial
Markets. Princeton University Press, Princeton, NJ.
Cho, D., Russell, J. R., Tiao, G. C., and Tsay, R. S. (2003). The magnet effect of price limits:
Evidence from high frequency data on Taiwan stock exchange. Journal of Empirical
Finance 10: 133–168.
Chou, R. Y. (2005). Forecasting ﬁnancial volatilities with extreme values: The conditional autoregressive range (CARR) model. Journal of Money, Credit and Banking 37:
561–582.
Engle, R. F. and Russell, J. R. (1998). Autoregressive conditional duration: A new model
for irregularly spaced transaction data. Econometrica 66: 1127–1162.
Ghysels, E. (2000). Some econometric recipes for high-frequency data cooking. Journal of
Business and Economic Statistics 18: 154–163.
Hasbrouck, J. (1992). Using the TORQ Database. Stern School of Business, New York
University, New York.
Hasbrouck, J. (1999). The dynamics of discrete bid and ask quotes. Journal of Finance 54:
2109–2142.
Hauseman, J., Lo, A., and MacKinlay, C. (1992). An ordered probit analysis of transaction
stock prices. Journal of Financial Economics 31: 319–379.
Lo, A. and MacKinlay, A. C. (1990). An econometric analysis of nonsynchronous trading.
Journal of Econometrics 45: 181–212.
McCulloch, R. E. and Tsay, R. S. (2000). Nonlinearity in high frequency data and hierarchical
models. Studies in Nonlinear Dynamics and Econometrics 5: 1–17.
Roll, R. (1984). A simple implicit measure of the effective bid-ask spread in an efﬁcient
market. Journal of Finance 39: 1127–1140.
Rydberg, T. H. and Shephard, N. (2003). Dynamics of trade-by-trade price movements:
Decomposition and models. Journal of Financial Econometrics 1: 2–25.
Stoll, H. and Whaley, R. (1990). Stock market structure and volatility. Review of Financial
Studies 3: 37–71.
--- page 312 ---

references
285
Tsay, R. S. (2009). Autoregressive conditional duration models. In Applied Econometrics,
Palgrave Handbook of Econometrics, Vol. 2, T. C. Mills and K. Patterson (eds.), Basingstoke, Hampshire, UK.
Wood, R. A. (2000). Market microstructure research databases: History and projections.
Journal of Business & Economic Statistics 18: 140–145.
Zhang, M. Y., Russell, J. R., and Tsay, R. S. (2001). A nonlinear autoregressive conditional
duration model with applications to ﬁnancial transaction data. Journal of Econometrics
104: 179–207.
Zhang, M. Y., Russell, J. R., and Tsay, R. S. (2008). Determinants of bid and ask quotes
and implications for the cost of trading. Journal of Empirical Finance 15: 656–678.
--- page 313 ---
--- page 314 ---

C H A P T E R
6
Continuous-Time Models
and Their Applications
The price of a ﬁnancial asset evolves over time and forms a stochastic process,
which is a statistical term used to describe the evolution of a random variable over
time. The observed prices are a realization of the underlying stochastic process. The
theory of stochastic process is the basis on which the observed prices are analyzed
and statistical inference is made.
There are two types of stochastic process for modeling the price of an asset. The
ﬁrst type is called the discrete-time stochastic process, in which the price changes at
discrete time points. All the processes discussed in the previous chapters belong to
this category. For example, the daily closing price of IBM stock on the New York
Stock Exchange forms a discrete-time stochastic process. Here the price changes
only at the closing of a trading day. Price movements within a trading day are
not necessarily relevant to the observed daily price. The second type of stochastic
process is the continuous-time process, in which the price changes continuously,
even though the price is only observed at discrete time points. One can think of
the price as the “true value” of the stock that always exists and is time varying.
For both types of process, the price can be continuous or discrete. A continuous
price can assume any positive real number, whereas a discrete price can only
assume a countable number of possible values. Assume that the price of an asset is
a continuous-time stochastic process. If the price is a continuous random variable,
then we have a continuous-time continuous process. If the price itself is discrete,
then we have a continuous-time discrete process. Similar classiﬁcations apply to
discrete-time processes. The series of price change in Chapter 5 is an example of
a discrete-time discrete process.
In this chapter, we treat the price of an asset as a continuous-time continuous
stochastic process. Our goal is to introduce the statistical theory and tools needed
to model ﬁnancial assets and to price options. We begin the chapter with some
terminologies of stock options used in the chapter. In Section 6.2, we provide a brief
Analysis of Financial Time Series, Third Edition, By Ruey S. Tsay
Copyright 2010 John Wiley & Sons, Inc.
287
--- page 315 ---

288
continuous-time models and their applications
introduction of Brownian motion, which is also known as a Wiener process. We
then discuss some diffusion equations and stochastic calculus, including the wellknown Ito lemma. Most option pricing formulas are derived under the assumption
that the price of an asset follows a diffusion equation. We use the Black–Scholes
formula to demonstrate the derivation. Finally, to handle the price variations caused
by rare events (e.g., a proﬁt warning), we also study some simple diffusion models
with jumps.
If the price of an asset follows a diffusion equation, then the price of an option
contingent to the asset can be derived by using hedging methods. However, with
jumps the market becomes incomplete and there is no perfect hedging of options.
The price of an option is then valued either by using diversiﬁability of jump risk
or deﬁning a notion of risk and choosing a price and a hedge that minimize this
risk. For basic applications of stochastic processes in derivative pricing, see Cox
and Rubinstein (1985) and Hull (2007).
6.1
OPTIONS
A stock option is a ﬁnancial contract that gives the holder the right to trade a certain
number of shares of a speciﬁed common stock by a certain date for a speciﬁed
price. There are two types of options. A call option gives the holder the right to
buy the underlying stock; see Chapter 3 for a formal deﬁnition. A put option gives
the holder the right to sell the underlying stock. The speciﬁed price in the contract
is called the strike price or exercise price. The date in the contract is known as the
expiration date or maturity. American options can be exercised at any time up to
the expiration date. European options can be exercised only on the expiration date.
The value of a stock option depends on the value of the underlying stock. Let
K be the strike price and P be the stock price. A call option is in-the-money when
P > K, at-the-money when P = K, and out-of-the-money when P < K. A put
option is in-the-money when P < K, at-the-money when P = K, and out-of-themoney when P > K. In general, an option is in-the-money when it would lead to
a positive cash ﬂow to the holder if it were exercised immediately. An option is
out-of-the-money when it would lead to a negative cash ﬂow to the holder if it
were exercised immediately. Finally, an option is at-the-money when it would lead
to zero cash ﬂow if it were exercised immediately. Obviously, only in-the-money
options are exercised in practice. For more information on options, see Hull (2007).
6.2
SOME CONTINUOUS-TIME STOCHASTIC PROCESSES
In mathematical statistics, a continuous-time continuous stochastic process is
deﬁned on a probability space (, F, P), where  is a nonempty space, F is a σ
ﬁeld consisting of subsets of , and P is a probability measure; see Chapter 1 of
Billingsley (1986). The process can be written as {x(η, t)}, where t denotes time
and is continuous in [0, ∞). For a given t, x(η, t) is a real-valued continuous
--- page 316 ---

some continuous-time stochastic processes
289
random variable (i.e., a mapping from  to the real line), and η is an element of
. For the price of an asset at time t, the range of x(η, t) is the set of nonnegative
real numbers. For a given η, {x(η, t)} is a time series with values depending on
the time t. For simplicity, we write a continuous-time stochastic process as {xt}
with the understanding that, for a given t, xt is a random variable. In the literature,
some authors use x(t) instead of xt to emphasize that t is continuous. However,
we use the same notation xt, but call it a continuous-time stochastic process.
6.2.1
Wiener Process
In a discrete-time econometric model, we assume that the shocks form a white
noise process, which is not predictable. What is the counterpart of shocks in a
continuous-time model? The answer is the increments of a Wiener process, which
is also known as a standard Brownian motion. There are many ways to deﬁne a
Wiener process {wt}. We use a simple approach that focuses on the small change

wt = wt+
t −wt associated with a small increment
t in time. A continuoustime stochastic process {wt} is a Wiener process if it satisﬁes
1.
wt = ϵ
√

t, where ϵ is a standard normal random variable; and
2.
wt is independent of wj for all j ≤t.
The second condition is a Markov property saying that conditional on the present
value wt, any past information of the process, wj with j < t, is irrelevant to the
future wt+ℓwith ℓ> 0. From this property, it is easily seen that for any two nonoverlapping time intervals
1 and
2, the increments wt1+
1 −wt1 and wt2+
2 −wt2
are independent. In ﬁnance, this Markov property is related to a weak form of
efﬁcient market.
From the ﬁrst condition,
wt is normally distributed with mean zero and variance
t. That is,
wt ∼N(0,
t), where ∼denotes probability distribution.
Consider next the process wt. We assume that the process starts at t = 0 with
initial value w0, which is ﬁxed and often set to zero. Then wt −w0 can be treated
as a sum of many small increments. More speciﬁcally, deﬁne T = t/
t, where
t
is a small positive increment. Then
wt −w0 = wT
t −w0 =
T

i=1

wi =
T

i=1
ϵi
√

t,
where
wi = wi
t −w(i−1)
t. Because the ϵi are independent, we have
E(wt −w0) = 0,
Var(wt −w0) =
T

i=1

t = T
t = t.
Thus, the increment in wt from time 0 to time t is normally distributed with
mean zero and variance t. To put it formally, for a Wiener process wt, we have
--- page 317 ---

290
continuous-time models and their applications
Time
W
0.0
0.2
0.4
0.6
0.8
1.0
−0.4
0.0 0.2 0.4 0.6
W
−0.6
−0.2
0.2
W
−1.5 −1.0 −0.5 0.0 0.5
W
−0.4
0.0 0.2 0.4
Time
0.0
0.2
0.4
0.6
0.8
1.0
Time
0.0
0.2
0.4
0.6
0.8
1.0
Time
0.0
0.2
0.4
0.6
0.8
1.0
Figure 6.1
Four simulated Wiener processes.
that wt −w0 ∼N(0, t). This says that the variance of a Wiener process increases
linearly with the length of time interval.
Figure 6.1 shows four simulated Wiener processes on the unit time interval [0, 1].
They are obtained by using a simple version of Donsker’s theorem in the statistical
literature with n = 3000; see Donsker (1951) or Billingsley (1968). The four plots
start with w0 = 0 but drift apart as time increases, illustrating that the variance of
a Wiener process increases with time. A simple time transformation from [0, 1) to
[0, ∞) can be used to obtain simulated Wiener processes for t ∈[0, ∞).
Donsker’s Theorem
Assume that {zi}n
i=1 is a sequence of independent standard normal random variates.
For any t ∈[0, 1], let [nt] be the integer part of nt. Deﬁne wn,t = (1/√n) [nt]
i=1 zi.
Then wn,t converges in distribution to a Wiener process wt on [0, 1] as n goes to
inﬁnity.
R or S-Plus Commands for Generating a Wiener Process
n = 3000
epsi = rnorm(n,0,1)
w=cumsum(epsi)/sqrt(n)
plot(w,type=’l’)
Remark.
A formal deﬁnition of a Brownian motion wt on a probability space
(, F, P) is that it is a real-valued, continuous stochastic process for t ≥0 with
independent and stationary increments. In other words, wt satisﬁes the following:
--- page 318 ---

some continuous-time stochastic processes
291
1. Continuity: The map from t to wt is continuous almost surely with respect
to the probability measure P.
2. Independent increments: If s ≤t, wt −ws is independent of wv for all v ≤s.
3. Stationary increments: If s ≤t, wt −ws and wt−s −w0 have the same probability distribution.
It can be shown that the probability distribution of the increment wt −ws is normal with mean µ(t −s) and variance σ 2(t −s). Furthermore, for any given time
indexes 0 ≤t1 < t2 < · · · < tk, the random vector (wt1, wt2, . . . , wtk) follows a
multivariate normal distribution. Finally, a Brownian motion is standard if w0 = 0
almost surely, µ = 0, and σ 2 = 1.
□
Remark.
An important property of Brownian motions is that their paths are
not differentiable almost surely. In other words, for a standard Brownian motion
wt, it can be shown that dwt/dt does not exist for all elements of  except for
elements in a subset 1 ⊂ such that P (1) = 0. As a result, we cannot use
the usual integration in calculus to handle integrals involving a standard Brownian
motion when we consider the value of an asset over time. Another approach must be
sought. This is the purpose of discussing Ito’s calculus in the next section.
□
6.2.2
Generalized Wiener Process
The Wiener process is a special stochastic process with zero drift and variance
proportional to the length of the time interval. This means that the rate of change
in expectation is zero and the rate of change in variance is 1. In practice, the mean
and variance of a stochastic process can evolve over time in a more complicated
manner. Hence, further generalization of a stochastic process is needed. To this
end, we consider the generalized Wiener process in which the expectation has a
drift rate µ and the rate of variance change is σ 2. Denote such a process by xt and
use the notation dy for a small change in the variable y. Then the model for xt is
dxt = µ dt + σ dwt,
(6.1)
where wt is a Wiener process. If we consider a discretized version of Eq. (6.1),
then
xt −x0 = µt + σϵ
√
t
for increment from 0 to t. Consequently,
E(xt −x0) = µt,
Var(xt −x0) = σ 2t.
The results say that the increment in xt has a growth rate of µ for the expectation
and a growth rate of σ 2 for the variance. In the literature, µ and σ of Eq. (6.1)
are referred to as the drift and volatility parameters of the generalized Wiener
process xt.
--- page 319 ---

292
continuous-time models and their applications
6.2.3
Ito Process
The drift and volatility parameters of a generalized Wiener process are time invariant. If one further extends the model by allowing µ and σ to be functions of the
stochastic process xt, then we have an Ito process. Speciﬁcally, a process xt is an
Ito process if it satisﬁes
dxt = µ(xt, t) dt + σ(xt, t) dwt,
(6.2)
where wt is a Wiener process. This process plays an important role in mathematical
ﬁnance and can be written as
xt = x0 +
 t
0
µ(xs, s) ds +
 t
0
σ(xs, s) dws,
where x0 denotes the starting value of the process at time 0 and the last term on the
right-hand side is a stochastic integral. Equation (6.2) is referred to as a stochastic
diffusion equation with µ(xt, t) and σ(xt, t) being the drift and diffusion functions,
respectively.
The Wiener process is a special Ito process because it satisﬁes Eq. (6.2) with
µ(xt, t) = 0 and σ(xt, t) = 1.
6.3
ITO’S LEMMA
In ﬁnance, when using continuous-time models, it is common to assume that the
price of an asset is an Ito process. Therefore, to derive the price of a ﬁnancial
derivative, one needs to use Ito’s calculus. In this section, we brieﬂy review Ito’s
lemma by treating it as a natural extension of the differentiation in calculus. Ito’s
lemma is the basis of stochastic calculus.
6.3.1
Review of Differentiation
Let G(x) be a differentiable function of x. Using the Taylor expansion, we have

G ≡G(x +
x) −G(x) = ∂G
∂x
x + 1
2
∂2G
∂x2 (
x)2 + 1
6
∂3G
∂x3 (
x)3 + · · · .
Taking the limit as
x →0 and ignoring the higher order terms of
x, we have
dG = ∂G
∂x dx.
When G is a function of x and y, we have

G = ∂G
∂x
x + ∂G
∂y
y + 1
2
∂2G
∂x2 (
x)2 + ∂2G
∂x∂y
x
y + 1
2
∂2G
∂y2 (
y)2 + · · · .
--- page 320 ---

ito’s lemma
293
Taking the limit as
x →0 and
y →0, we have
dG = ∂G
∂x dx + ∂G
∂y dy.
6.3.2
Stochastic Differentiation
Turn next to the case in which G is a differentiable function of xt and t, and xt is
an Ito process. The Taylor expansion becomes

G = ∂G
∂x
x + ∂G
∂t
t + 1
2
∂2G
∂x2 (
x)2 + ∂2G
∂x ∂t
x
t + 1
2
∂2G
∂t2 (
t)2 + · · · .
(6.3)
A discretized version of the Ito process is

x = µ
t + σϵ
√

t,
(6.4)
where, for simplicity, we omit the arguments of µ and σ, and
x = xt+
t −xt.
From Eq. (6.4), we have
(
x)2 = µ2(
t)2 + σ 2ϵ2
t + 2µσϵ(
t)3/2 = σ 2ϵ2
t + H(
t),
(6.5)
where H(
t) denotes higher order terms of
t. This result shows that (
x)2
contains a term of order
t, which cannot be ignored when we take the limit as

t →0. However, the ﬁrst term on the right-hand side of Eq. (6.5) has some nice
properties:
E(σ 2ϵ2
t) = σ 2
t,
Var(σ 2ϵ2
t) = E[σ 4ϵ4(
t)2] −[E(σ 2ϵ2
t)]2 = 2σ 4(
t)2,
where we use E(ϵ4) = 3 for a standard normal random variable. These two properties show that σ 2ϵ2
t converges to a nonstochastic quantity σ 2
t as
t →0.
Consequently, from Eq. (6.5), we have
(
x)2 →σ 2 dt
as

t →0.
Plugging the prior result into Eq. (6.3) and using Ito’s equation of xt in Eq. (6.2),
we obtain
dG = ∂G
∂x dx + ∂G
∂t dt + 1
2
∂2G
∂x2 σ 2 dt
=
∂G
∂x µ + ∂G
∂t + 1
2
∂2G
∂x2 σ 2

dt + ∂G
∂x σ dwt,
which is the well-known Ito lemma in stochastic calculus.
Recall that we suppressed the argument (xt, t) from the drift and volatility terms
µ and σ in the derivation of Ito’s lemma. To avoid any possible confusion in the
future, we restate the lemma as follows.
--- page 321 ---

294
continuous-time models and their applications
Ito’s Lemma
Assume that xt is a continuous-time stochastic process satisfying
dxt = µ(xt, t) dt + σ(xt, t) dwt,
where wt is a Wiener process. Furthermore, G(xt, t) is a differentiable function of
xt and t. Then,
dG =

∂G
∂x µ(xt, t) + ∂G
∂t + 1
2
∂2G
∂x2 σ 2(xt, t)

dt + ∂G
∂x σ(xt, t) dwt.
(6.6)
Example 6.1.
As a simple illustration, consider the square function G(wt, t) =
w2
t of the Wiener process. Here we have µ(wt, t) = 0, σ(wt, t) = 1, and
∂G
∂wt
= 2wt,
∂G
∂t = 0,
∂2G
∂w2
t
= 2.
Therefore,
dw2
t = (2wt × 0 + 0 + 1
2 × 2 × 1) dt + 2wt dwt = dt + 2wt dwt.
(6.7)
6.3.3
An Application
Let Pt be the price of a stock at time t, which is continuous in [0, ∞). In the
literature, it is common to assume that Pt follows the special Ito process
dPt = µPt dt + σPt dwt,
(6.8)
where µ and σ are constant. Using the notation of the general Ito process in
Eq. (6.2), we have µ(xt, t) = µxt and σ(xt, t) = σxt, where xt = Pt. Such a special process is referred to as a geometric Brownian motion. We now apply Ito’s
lemma to obtain a continuous-time model for the logarithm of the stock price Pt.
Let G(Pt, t) = ln(Pt) be the log price of the underlying stock. Then we have
∂G
∂Pt
= 1
Pt
,
∂G
∂t = 0,
1
2
∂2G
∂P 2
t
= 1
2
−1
P 2
t
.
Consequently, via Ito’s lemma, we obtain
d ln(Pt) =
 1
Pt
µPt + 1
2
−1
P 2
t
σ 2P 2
t

dt + 1
Pt
σPt dwt
=

µ −σ 2
2

dt + σ dwt.
This result shows that the logarithm of a price follows a generalized Wiener process
with drift rate µ −σ 2/2 and variance rate σ 2 if the price is a geometric Brownian
--- page 322 ---

ito’s lemma
295
motion. Consequently, the change in logarithm of price (i.e., log return) between
current time t and some future time T is normally distributed with mean (µ −
σ 2/2)(T −t) and variance σ 2(T −t). If the time interval T −t =
 is ﬁxed and
we are interested in equally spaced increments in log price, then the increment
series is a Gaussian process with mean (µ −σ 2/2)
 and variance σ 2
.
6.3.4
Estimation of µ and σ
The two unknown parameters µ and σ of the geometric Brownian motion in
Eq. (6.8) can be estimated empirically. Assume that we have n + 1 observations of
stock price Pt at equally spaced time interval
 (e.g., daily, weekly, or monthly).
We measure
 in years. Denote the observed prices as {P0, P1, . . . , Pn} and let
rt = ln(Pt) −ln(Pt−1) for t = 1, . . . , n.
Since Pt = Pt−1 exp(rt), rt is the continuously compounded return in the tth time
interval. Using the result of the previous section and assuming that the stock price
Pt follows a geometric Brownian motion, we obtain that rt is normally distributed
with mean (µ −σ 2/2)
 and variance σ 2
. In addition, the rt are not serially
correlated.
For simplicity, deﬁne µr = E(rt) = (µ −σ 2/2)
 and σ 2
r = var(rt) = σ 2
.
Let ¯r and sr be the sample mean and standard deviation of the data—that is,
¯r =
n
t=1 rt
n
,
sr =
-
.
.
/
1
n −1
n

t=1
(rt −¯r)2.
As mentioned in Chapter 1, ¯r and sr are consistent estimates of the mean and
standard deviation of ri, respectively. That is, ¯r →µr and sr →σr as n →∞.
Therefore, we may estimate σ by
ˆσ =
sr
√

.
Furthermore, it can be shown that the standard error of this estimate is approximately ˆσ/
√
2n. From ˆµr = ¯r, we can estimate µ by
ˆµ = ¯r

 + ˆσ 2
2 = ¯r

 + s2
r
2
.
When the series rt is serially correlated or when the price of the asset does not
follow the geometric Brownian motion in Eq. (6.8), then other estimation methods
must be used to estimate the drift and volatility parameters of the diffusion equation.
We return to this issue later.
Example 6.2.
Consider the daily log returns of IBM stock in 1998.
Figure 6.2(a) shows the time plot of the data, which have 252 observations.
Figure 6.2(b) shows the sample autocorrelations of the series. It is seen that
--- page 323 ---

296
continuous-time models and their applications
··
···
·
·
·
···
·
·
····
····
··
·
·
·
··
········
·
··
·
·
·
···
···
·
·
···
··
··
···
···
·
·
··
·
·
··
·
·
·
·
·
·
·
·
······
··
·
··
·
·
···
·
·
····
·
···
··
··
···
·
·
·
··
·
·
······
··
······
·
···
·
·
·
···
·
·
··
·
··
··
·····
·
·
·
···
·
·
·
·
·
··
·
·
··
··
··
··
·
·
·
·
·
·
···
·
·
·
····
·
·
·
·
·
·
·
······
·······
·
···
·
·
···
·
·
··
·
·
··
·
···
·
·
·
·
·
·
···
···
···
Days
Log returns
0
50
100
150
200
250
−0.08−0.04 0.0 0.04
Lag
ACF
0
5
10
15
20
0.0
0.4
0.8
Figure 6.2
Daily returns of IBM stock in 1998: (a) log returns and (b) sample autocorrelations.
the log returns are indeed serially uncorrelated. The Ljung–Box statistic
gives Q(10) = 4.9, which is highly insigniﬁcant compared with a chi-squared
distribution with 10 degrees of freedom.
If we assume that the price of IBM stock in 1998 follows the geometric Brownian
motion in Eq. (6.8), then we can use the daily log returns to estimate the parameters
µ and σ. From the data, we have ¯r = 0.002276 and sr = 0.01915. Since 1 trading
day is equivalent to
 = 1/252 year, we obtain that
ˆσ =
sr
√

= 0.3040,
ˆµ = ¯r

 + ˆσ 2
2 = 0.6198.
Thus, the estimated expected return was 61.98% and the standard deviation was
30.4% per annum for IBM stock in 1998.
The normality assumption of the daily log returns may not hold, however. In this
particular instance, the skewness −0.464(0.153) and excess kurtosis 2.396(0.306)
raise some concern, where the number in parentheses denotes asymptotic standard
error.
Example 6.3.
Consider the daily log return of the stock of Cisco Systems, Inc.
in 2007. There are 251 observations, and the sample mean and standard deviation
are −3.81 × 10−5 and 0.0174, respectively. The log return series also shows no
serial correlation with Q(12) = 12.30 with a p value of 0.42. Therefore, we have
ˆσ =
sr
√

=
0.0174
√1.0/251.0 = 0.275,
ˆµ = ¯r

 + ˆσ 2
2 = −0.0094.
--- page 324 ---

distributions of stock prices and log returns
297
Consequently, the estimated expected log return for Cisco Systems’ stock was
−0.94% per annum, and the estimated standard deviation was 27.5% per annum
in 2007.
6.4
DISTRIBUTIONS OF STOCK PRICES AND LOG RETURNS
The result of the previous section shows that if one assumes that price of a stock
follows the geometric Brownian motion
dPt = µPt dt + σPt dwt,
then the logarithm of the price follows a generalized Wiener process
d ln(Pt) =

µ −σ 2
2

dt + σ dwt,
where Pt is the price of the stock at time t and wt is a Wiener process. Therefore,
the change in log price from time t to T is normally distributed as
ln(PT ) −ln(Pt) ∼N


µ −σ 2
2

(T −t), σ 2(T −t)

.
(6.9)
Consequently, conditional on the price Pt at time t, the log price at time T > t is
normally distributed as
ln(PT ) ∼N

ln(Pt) +

µ −σ 2
2

(T −t), σ 2(T −t)

.
(6.10)
Using the result of lognormal distribution discussed in Chapter 1, we obtain the
(conditional) mean and variance of PT as
E(PT ) = Pt exp[µ(T −t)],
Var(PT ) = P 2
t exp[2µ(T −t)]{exp[σ 2(T −t)] −1}.
Note that the expectation conﬁrms that µ is the expected rate of return of the stock.
The prior distribution of stock price can be used to make inferences. For
example, suppose that the current price of stock A is $50, the expected return of the
stock is 15% per annum, and the volatility is 40% per annum. Then the expected
price of stock A in 6 months (0.5 year) and the associated variance are given by
E(PT ) = 50 exp(0.15 × 0.5) = 53.89,
Var(PT ) = 2500 exp(0.3 × 0.5)[exp(0.16 × 0.5) −1] = 241.92.
The standard deviation of the price 6 months from now is
√
241.92 = 15.55.
