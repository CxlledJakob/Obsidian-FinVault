# Volatility Trading_ Sinclair_Volatility Trading -- Euan Sinclair(auth_) -- Wiley Trading, 1, 2013 -- John Wiley & Sons, Incorporated -- isbn13 9781118347133 -- 2634a86bfed8248fa7ba3fb72595bbbc -- Anna’s Archive.pdf — Chapter 2: Volatility Measurement (pages 32–51)

--- page 32 ---

13
C H A P T E R 2
Volatility
Measurement
W
e have seen that to ﬁnd an edge in option trading, we need an
estimate of future realized volatility to trade against that implied
by the options. But before we can forecast future volatility we need to
be able to measure what it has been in the past. In this chapter we
look at methods of historical volatility measurement including close/close
volatility, Parkinson volatility, Rogers/Satchell volatility, Garman/Klass
volatility, and Yang/Zhang volatility. We discuss the efﬁciency (how
quickly our estimated value converges to the true value) and bias (whether
our method systematically estimates above or below the true value) of each
estimator and also how each is perturbed by different aspects of real markets
such as fat tails in returns, trends, and microstructure noise. We discuss
different frequencies of measurement. Once we understand what is meant
by historical volatility we can look at its properties. We demonstrate mean
reversion, volatility clustering, and seasonality effects.
■Defining and Measuring Volatility
For trading we need more than a point estimate of future volatility, we need
some estimate of possible range of volatilities. To ﬁnd this we examine the
constructionandsamplingpropertiesofvolatilitycones.Measuringvolatility
and having a forecast of its distribution are essential for successfully trading
options. Sadly it is not sufﬁcient. Buying volatility because it is ‘‘cheap’’
or selling because it is ‘‘rich’’ is seldom a good idea. Often, things will
be cheap for a reason. Any forecast we make has to be supplemented
Volatility Trading,   Second Edition.    Euan Sinclair
© 2013 Euan Sinclair. Published 2013 by John Wiley & Sons, Inc.
--- page 33 ---

VOLATILITY MEASUREMENT
14
by our fundamental analysis (e.g., What catalyst will appear to cause the
volatility to rise? Or what are we hoping will not happen if we are short?).
The markets are very complex and interrelated and all measurements and
forecasts must be placed in the context of the current trading environment.
Measuring volatility is not like measuring price. Instantaneous volatility
is unobservable. It needs time to manifest itself. Measuring it is something
of an art form and we need to choose between various statistical estimators.
In fact, Poon (2005) lists more than 100 references on volatility forecasting,
which gives some idea of the difﬁculty of the problem. We do not attempt to
ﬁnd a deﬁnitive answer. Instead we look at a number of different estimators,
learn their strengths and deﬁciencies and where each should best be applied.
■Definition of Volatility
The standard deﬁnition of volatility is the square root of the variance. And
variance is deﬁned as
s2 = 1
N
N

i=1
(xi −x)2
(2.1a)
where, for our purposes, xi are the logarithmic returns, x is the mean return
in the sample and N is the sample size. To express the variance in annualized
terms we would need to multiply the raw variance by the annualization
factor given by N, the number of trading periods in a year: for example,
252 if using daily data, as this is the number of trading days in a year (at least
in the United States).
If the historical price series includes the payment of a dividend (or a stock
split) we must adjust the price series. The effect of a stock going ex-dividend
makes it look like there was volatility even though there was none. If this
adjustment is not done our volatility estimate may well be wrong by several
percentage points. For example if we have a 3 percent price drop due to the
stock going ex-dividend, it looks like a 48 percent move on an annualized
basis (i.e.,0.03√252). Obviously this is very signiﬁcant.
There are several different ways of making this adjustment. The ﬁrst
is to simply subtract the dividend from the price before the ex-dividend
date. This leaves the absolute values of the day-to-day changes before the
ex-dividend date unchanged, but if we have enough dividends in the series
this process can lead to negative stock ‘‘prices.’’
A better method is to multiply by an adjustment factor that leaves the
percentage changes unaffected. This factor is
1 −dividend
price
--- page 34 ---

VOLATILITY MEASUREMENT
15
Prices before the ex-dividend date are multiplied by this factor. This is
backwardadjustment.Alternatively,itispossibletoforwardadjustprices,which
would mean that the current price won’t be the same as the adjusted price.
Equation 2.1 makes no assumptions about the distribution, other than
that the sum converges. All ﬁnite samples have variance. However, to
use volatility for pricing options, we need to make assumptions about the
process generating the returns. As mentioned in the previous chapter, the
BSM model assumed that the returns were normally distributed. In this case
variance completely characterizes the shape of the distribution. We know
this isn’t true but we still expect variance (and hence volatility) to be an
important parameter, indeed the dominant parameter, for describing the
width of the return distribution.
In ﬁnance it is difﬁcult to distinguish mean returns (drift) from variance
(this is a central problem in many arguments about trading methods and
results) and estimates of the mean return are notoriously noisy especially for
small samples. So we generally set the mean return in Equation 2.1a to zero.
This increases accuracy of measurement by removing a source of noise.
s2 = 1
N
N

i=1
(xi)2
(2.1b)
To estimate the population variance from this sample variance, we need
to make the conversion (Kenney and Keeping 1951).
σ2 =
N
N −1s2
(2.2)
Unfortunately, some authorities choose to avoid this step by directly
deﬁning the sample variance to be
s2 =
1
N −1
N

i=1
(xi −x)2
(2.3)
so that is already an unbiased estimator for the population variance. It
is important to know exactly which deﬁnition you are dealing with and
this seems to be a recurring source of confusion. Always check for the
N −1 factor in the denominator. The Excel function VaR uses this second
convention.
Equations 2.2 or 2.3 give unbiased estimates of variance, but simply
taking the square root gives an estimate of volatility that is biased low. This
is because of Jensen’s inequality. This states that the average of a square
root is always less than the square root of the average. Speciﬁcally
E(s) = E(
√
s2) <

E(s2) =
√
σ2 = σ
This needs to be corrected for.
--- page 35 ---

VOLATILITY MEASUREMENT
16
If we assume that the true process is a normal distribution of returns, we
can use the fact that the distribution of the sample standard deviation as a
function of the length of the sample is given by
fN(s) = 2
 N
2σ2
 N−1
2

N −1
2
 exp
−Ns2
2σ2

sN−2
(2.4)
where s is the sample standard deviation, σ is the population standard
deviation and (x) is the gamma function deﬁned by (n) = (n −1)!. This
is plotted in Figure 2.1.
We see that increasing the sample size, N, shifts the peak of the
distribution to the right, toward the population standard deviation. So a
larger sample is less biased. The extent of this bias can be exactly quantiﬁed
by the relationship
s = b(N)σ
(2.5)
where
b(N) =

2
N

N
2


N −1
2

(2.6)
■s/b is an unbiased estimator of the population standard deviation.
Table 2.1 gives the size of b for various sample sizes.
This corrects the bias. This means that it will not systematically overor
underestimate the true volatility. However, this estimator converges to the
true volatility slowly.
0
0.2
0.4
0.6
0.8
1
1.2
1.4
1.6
1.8
2
0.5
0
1.5
1
2.5
2
s
f(s)
N = 5
N = 10
FIGURE 2.1
The Distribution of the Sample Standard Deviation
--- page 36 ---

VOLATILITY MEASUREMENT
17
TABLE 2.1
Correction Factor as a
Function of Sample Size
Sample Size
b(N)
5
0.840749
10
0.922746
20
0.961945
50
0.984912
100
0.992478
200
0.996245
Technically, this is referred to as being inefﬁcient. The variance of the
estimator is given by
var(s) = 1
N

N −1 −2
2
N
2

2
N −1
2


σ2
(2.7)
Figure 2.2 shows the dependence on the variance (of the sample variance)
of various sample sizes.
Mental arithmetic involving the gamma function can be tricky. A simpler
approximation to this equation would be more useful. First we note that


k + 1
2

(k)
=
√
k

1 −1
8k +
1
128k2 + · · ·

(2.8)
0
0.01
0.02
0.03
0.04
0.05
0.06
0.07
0.08
0.09
0.1
0
20
40
60
80
100
120
N
Variance of Sample/True Variance
FIGURE 2.2
The Convergence of the Variance (of the Sample Variance) to the True
Population Variance as a Function of the Sample Size, N
--- page 37 ---

VOLATILITY MEASUREMENT
18
So to leading order in N we eventually get
b(N)2 ≈1 −3
2N
(2.9)
So Equations 2.6 and 2.7 give us
var(s) ≈σ2
2N
(2.10)
This gives a simpler expression for levels of the conﬁdence interval of the
measured volatility. Table 2.2 shows how the conﬁdence interval varies as
we change N, the sample size. We can see that this is generally an excellent
approximation to the exact result (Equation 2.7).
So using more data would get us closer to the true result in this case.
Although this is no problem if we are measuring the volatility of an
unchanging process, it is problematic for ﬁnancial markets. If we use too
little data we will have a noisy measurement of volatility that due to sampling
error might not be close to the true volatility, but if we use too much data
we will be using information that is no longer relevant to the current state
of the market. Choosing the right compromise is something of an art and the
most appropriate solution will be dependent on current market conditions.
However, it is obvious that the commonly used method of measuring
volatility from the last 30 closing prices gives an unacceptably large sampling
error. The 95 percent conﬁdence interval of two standard deviations means
that we could be off by as much as 25 percent of the true value!
Sampling error is not the same as measurement error. In a physics
experiment, we might only be able to measure a certain quantity to a limited
degree of precision, due to the limitations of the measuring device or the
experimental setup. But if we ignore the bid/ask spread, the price of a stock
is an exact number. So the historical volatility is an exact number. There is
no uncertainty due to measurement. But there is uncertainty over whether
the measure number is truly representative of the underlying reality. The
TABLE 2.2
Conﬁdence Intervals for Volatility
Sample
Size
True
Volatility
Standard
Deviation
Approximate
Standard Deviation
5
0.3
0.091557
0.094868
10
0.3
0.066096
0.067082
20
0.3
0.047113
0.047434
30
0.3
0.03856
0.038730
50
0.3
0.029923
0.030000
100
0.3
0.021186
0.021213
--- page 38 ---

VOLATILITY MEASUREMENT
19
situation has an analogy in baseball. When a player goes ﬁve for ﬁve, he has
hit 1.000. That is beyond dispute. But no one would claim he is truly a 1.000
hitter. We have just been lucky enough to see the portion of his career when
he hit well. There will be other days when he goes hitless. Similarly we need
to remember that like hitting ability, volatility is an unobservable quantity
that we can only estimate. Our measurements are distorted reﬂections of
the true volatility in the same way that a handful of plate appearances can
only give a partial picture of a baseball player’s true ability.
Before addressing this, let’s note that another reason that the close-toclose estimator is useful is because it can be rewritten in a form that allows
us to easily relate typical average stock moves to volatility, which is useful
for traders.
The deﬁnition of the standard deviation involves the square root of an
average of squares and we typically don’t have good intuition about how
these behave. So instead we will look at an estimator based on the ‘‘typical
stock move.’’ This is
σ = 19.896

1
N
N

t=1
|Rt|

(2.11)
This is because the average absolute return is
E[|Rt|] =

2
πσ
(2.12)
This means that
averagemove = 0.04986σS ≈σS
20
(2.13)
This allows a simple translation between daily returns and annualized
volatility. Traders often think that 16 percent annualized volatility corresponds to a daily return of 1 percent. But this is due to confusing the
square root of average squared returns with the daily return. To translate
between daily return size and annualized volatility we need to divide the
volatility by 20.
Multiplying the daily return by 20 gives a useful ‘‘quick and dirty’’
estimate of annualized volatility.
There are two basic ways of addressing the problem of the large sampling
error. We can use the close-to-close estimator with higher frequency data,
or we can use another estimator that doesn’t throw away all data points
other than closing prices. Each has limitations. First we try to develop better
estimators. This approach is also more generally applicable. If we can ﬁnd a
better estimator we could always apply this to higher frequency data.
--- page 39 ---

VOLATILITY MEASUREMENT
20
■Alternative Volatility Estimators
The ﬁrst such estimator was developed by Parkinson (1980). His estimator is
σ =




1
4N ln 2
N

i=1

ln hi
li
2
(2.14)
where hi is the high price in the trading period and li is the low price. As
before, this would need to be annualized by multiplying it by the square
root of the number of trading periods in a year. It makes sense that the
range could give an estimate of volatility. That is generally what traders
perceive volatility to be. It also seems likely that this estimate would need
fewer time periods to converge to the true volatility as it uses two prices
from each period instead of just one as with the close to close estimator.
This is true. The Parkinson estimator is about ﬁve times more efﬁcient at
estimating volatility than the close-to-close estimator when it is tested on
artiﬁcially generated geometric Brownian motion (efﬁciency is deﬁned as
the ratio of the variance of the close-to-close estimator to the range-based
estimator).
If prices are continuous, the Parkinson estimate of variance is unbiased
(but remember that there is a bias introduced by Jensen’s inequality when
we convert any variance estimate to a volatility estimate). However, prices
are only sampled discretely. This is true because markets only trade in
discrete units, but more importantly, because markets are only open for
part of the day. This means that the unobservable true price may not make
a high or a low when we can actually measure it. So we will systematically
underestimate volatility by using an estimator based on the observed range.
Garman and Klass (1980) showed by simulation that underestimation
due to discrete sampling as a function of sample size was given by Table 2.3.
TABLE 2.3
Sampling Error in
Parkinson Variance
Sample Size
Parkinson Variance/
True Variance
5
0.55
10
0.65
20
0.74
50
0.82
100
0.86
200
0.92
--- page 40 ---

VOLATILITY MEASUREMENT
21
The fact that this biases the estimates of volatility low comes as a surprise
to some. There is a pervasive misunderstanding that the Parkinson estimator
is biased high as it is impossible to actually trade at the extremes. This is
true but irrelevant. Parkinson makes no claims about being able to trade at
the extremes of the range, just that the range is related to the volatility. It
is an estimator of volatility not of tradability.
This bias is clearly a signiﬁcant issue. As a practical matter the variance
estimate can be unbiased by dividing by these correction factors as we did
in the case of the close-to-close estimator. But this does not address the fact
that opening jumps exist in the price series.
It is intuitively clear that the range has a relationship to the volatility of a
security. This idea can be extended to consider estimates of ‘‘range’’ other
than the difference between high and low.
The other well-known volatility estimator was developed by Garman
and Klass. It is
σ =



 1
N
N

i=1
1
2

ln hi
li
2
−1
N
N

i=1
(2 ln 2 −1)

ln
ci
ci−1
2
(2.15)
where ci is the closing price in the trading period. This estimator is up to
eight times as efﬁcient as the close-to-close estimator (the exact efﬁciency
improvement is dependent on the sample size) but is also biased due to the
discrete sampling leading to a low estimate of the range. Its bias is actually
worse than the Parkinson estimator.This is shown in Table 2.4.
If we know what the bias is, it can be corrected. More problematically,
the studies that show improved efﬁciency of these estimators rely on
assumptions that do not apply to real markets. In particular they assume
that the underlying follows a driftless geometric Brownian motion (GBM)
and trades continuously. Rogers, Satchell, and Yoon (Rogers and Satchell
TABLE 2.4
Sampling Error in Garman-
Klass Variance
Sample Size
Garman-Klass Variance/
True Variance
5
0.38
10
0.51
20
0.64
50
0.73
100
0.80
200
0.85
Source: Garman and Klass, 1980.
--- page 41 ---

VOLATILITY MEASUREMENT
22
1991; Rogers, Satchell, and Yoon 1994) relax this restriction and introduce
an estimator that outperforms the others when a drift term is introduced.
σ =



 1
N
N

i=1

ln hi
ci
 
ln hi
oi

+

ln li
ci
 
ln li
oi

(2.16)
where oi is the closing price in the trading period. More recently, Yang and
Zhang (2000) derive an estimator that also allows for opening jumps. It is
basically a weighted average of the Rogers, Satchell, and Yoon estimator, the
close-to-open volatility and the open-to-close volatility. In some simulations
it can have efﬁciency 14 times greater than the close-to-close volatility. But
this is highly dependent on the proportion of volatility cause by opening
jumps. If these jumps dominate, the estimator performs no better than the
close-to-close estimator. It is
σ =

σ2o + kσ2c + (1 −k)σ2rs
(2.17a)
where
σ2
o =
1
N −1
N

i=1

ln
 oi
oi−1

−1
N
N

i=1
ln
 oi
oi−1

2
(2.17b)
σ2
c =
1
N −1
N

i=1

ln
 ci
ci−1

−1
N
N

i=1
ln
 ci
ci−1

2
(2.17c)
σ2
rs = 1
N
N

i=1

ln hi
ci
 
ln hi
oi

+

ln li
ci
 
ln li
oi

(2.17d)
k =
0.34
1.34 + N + 1
N −1
(2.17e)
Brandt and Kinlay (2005) show that both of these estimators are
downward biased. This should not be a surprise as both are dependent on
extreme prices and continuity was still assumed.
At this point we have ﬁve estimators, each constructed to address a
shortcoming of the last. So each iteration should be better. Is our choice
of which estimator to use obvious? Not really. When Brandt and Kinlay
performed tests on more realistic simulated data (discretely sampled, with
driftandjumps),thedifferencesbetweentheestimatorsbecamelessdistinct.
Under these circumstances, the Garman-Klass and Yang-Zhang estimators
are biased slightly high and all of the nonclassical estimators have similar
efﬁciencies. Further, the correlation between the estimators is much higher
--- page 42 ---

VOLATILITY MEASUREMENT
23
TABLE 2.5a
Correlations between the Volatility Estimators for Simulated Data
Close-to-Close Parkinson Garman-Klass Rogers-Satchell Yang-Zhang
Close-to-Close
1.00
0.7
0.689
0.394
0.693
Parkinson
1.00
0.768
0.745
0.777
Garman-Klass
1.00
0.804
0.995
Rogers-Satchell
1.00
0.813
Yang-Zhang
1.00
The data were sampled at ﬁve-minute intervals for a 25-day period. The volatility was stochastic
with a mean of 14 percent and a drift of 8 percent.
Source: Brandt and Kinlay, 2005.
TABLE 2.5b
Correlations between the Volatility Estimators for S&P 500
Market Data
Close-to-Close Parkinson Garman-Klass Rogers-Satchell Yang-Zhang
Close-to-Close
1.00
0.975
0.944
0.911
0.942
Parkinson
1.00
0.991
0.976
0.99
Garman-Klass
1.00
0.994
0.999
Rogers-Satchell
1.00
0.996
Yang-Zhang
1.00
The data were sampled at ﬁve-minute intervals from January 4, 1988, to December 31, 2003.
Source: Brandt and Kinlay, 2005.
when tested on real market data than on simulated data (correlations are
shown in Table 2.5).
Each of the estimators discussed so far has been based on ﬁrst partitioning
time into a given interval. We then look at speciﬁc prices (open, high, low,
close, etc.) within that interval. In a sense, these estimators are based on
the question: How far did the price move? We can also turn the estimation
problem on its side. Instead of asking, ‘‘How far did the price move?’’ we
can ask, ‘‘How fast did the price move?’’ This alternative viewpoint was
ﬁrst studied by Cho and Frees (1988).
Deﬁne a logarithmic price corridor by forming a double barrier, ∆up
and ∆down from the initial spot price. When the barrier is touched, we
note the exit time, τ1, and reset the barrier around the current price. This
generates a sequence of exit times τ1, τ2, . . . , τn from which we want to
estimate volatility.
The choice of ∆here is analogous to the choice of the ﬁxed time interval
in the close-to-close method, but our series now consists of a random
sequence of times when the price has moved by a ﬁxed amount. This
contrast is illustrated in Figure 2.3, which also shows why it is apt to think
of the ﬁrst exit time method as ‘‘turning close to close on its side.’’
--- page 43 ---

VOLATILITY MEASUREMENT
24
–0.05
0
0.05
0.1
0.15
0.2
0.25
0.3
7/19/2010
8/19/2010
9/19/2010
10/19/2010
11/19/2010
12/19/2010
1/19/2011
2/19/2011
3/19/2011
4/19/2011
5/19/2011
6/19/2011
Date
Total Log Return
FIGURE 2.3
The Logarithmic Returns for SPY Sampled Each Time It Crosses a
Corridor of 0.05. In this example we have a sequence of crossing times (in days) of 13,
14, 17, 24, 39, 32, 65, 27, 23
Assuming Brownian motion for the log-price process, and making the
standard assumption that the drift rate is negligible for typical τ, we can
derive the elegant result:
E[τ] = ∆2
σ2
(2.18)
(For details of the derivation refer to Borodin and Salminen 2002.)
This can be inverted to obtain the following estimate for the volatility of
the security.
σ =
∆
√E[τ]
(2.19)
where E[τ] is the sample mean of the hitting times after n observations.
However, this estimate is signiﬁcantly biased unless n is very large. We
don’t know the true value of E[τ]: We can only make estimates based on
the observed data. So the sampling distribution of τ is important. The true
value will be slightly lower than the naive estimate of Equation 2.19 due to
Jensen’s inequality. That is,
E
1
τ

>
1
√E[τ] = σ
∆
(2.20)
But it is possible to make a second order correction that adjusts for the
variance of τ (again see Borodin and Salminen 2002).
Var(τ) = 2∆2
3σ2 = 2
3E[τ]2
(2.21)
--- page 44 ---

VOLATILITY MEASUREMENT
25
If τ is the mean of the sample of the n ﬁrst exit times we have, by the
Central Limit Theorem,
E[τ] = E[τ]
(2.22)
Var(τ) = Var(τ)
n
(2.23)
Our goal is to derive an unbiased estimator of the population variance.
To do this we deﬁne a new random variable δτ by
δτ = τ −E[τ]
(2.24)
This is a random variable with zero mean and a variance, Var(τ)/n. Now
deﬁne a function, f.
f (τ) = ∆
√τ
(2.25)
We can solve for the true population volatility, σ, by expanding our
biased sample volatility, E[ f(τ)], to second order to capture the variance
term:
E[f (τ)] = E[f (E[τ] + δτ)]
= E

f (E [τ]) + f ′(E[τ])δτ + 1
2f ′(E[τ])δτ2 + · · ·

= f (E[τ]) + 1
2f ′(E[τ])E[δτ]2
= σ + 1
2
3
4
σ
E[τ]2Var(τ)
= σ

1 + 1
4n

(2.26)
So for a single observation we need to correct our observed volatility by
multiplying by 4/5. This is a substantial correction, but the bias decreases
quickly as n increases. This convergence is illustrated in Table 2.6.
It is difﬁcult to consistently compare the barrier estimator to the closeto-close estimator in terms of efﬁciency. The barrier estimator generally
TABLE 2.6
The Bias Correction Factor for the
Sample Volatility as a Function of
the Number of Observations
n
Bias Factor
1
0.800
5
0.952
10
0.976
50
0.995
--- page 45 ---

VOLATILITY MEASUREMENT
26
0
2,000
4,000
6,000
8,000
10,000
12,000
14,000
16,000
18,000
10
13
16
19
22
25
28
31
34
37
40
43
46
49
Frequency
Volatility Estimate
First Exit Sample Vol
FIGURE 2.4
The Distribution of Volatility Estimates Using the Barrier Method
uses a different amount of information; indeed, it is a natural ﬁt for online
estimation, which can be viewed as an almost inﬁnitely large information
set. However, most traders are now sitting in front of computers with this
data streaming past their eyes anyway. Why not use all of it?
To get a visual comparison of the relative convergence speeds, Merrill
(2011) simulated 100,000 20-day paths of a 0.30 volatility stock, with
observation barriers set at 0.01. The dispersion of the measured estimates
of volatility from the barrier method is shown in Figure 2.4. The standard
deviation of the estimates is 0.028.
He next used Equation 2.18 to obtain an estimate for τ of 0.28 days.
Then he ran another simulation, sampling the stock every 0.28 of a day.
This means that this close-to-close volatility estimate was using the same
amount of data on average as the barrier method. The dispersion of the
measured estimates of volatility from the close-to-close method is shown in
Figure 2.5. The standard deviation of the estimates is 0.048. So the barrier
method appears to be about 1.7 times more efﬁcient.
The ﬁrst exit time method for estimating volatility is a natural ﬁt for
online volatility estimation. It can be easily adapted to take into account
the stock’s bid-ask spread and discrete trading. It also converges to the true
volatility more quickly than the traditional close-to-close estimator.
Close-to-Close Estimator
Good Points
■It has well-understood sampling properties.
■It is easy to correct bias.
■It is easy to convert to a form involving ‘‘typical daily moves.’’
--- page 46 ---

VOLATILITY MEASUREMENT
27
Frequency
0
1,000
2,000
3,000
4,000
5,000
6,000
7,000
8,000
9,000
10
13
16
19
22
25
28
31
34
37
40
43
46
49
Volatility Estimate
Close-to-Close Sample Vol
FIGURE 2.5
The Distribution of Volatility Estimates Using the Close-to-Close Method
Bad Points
■It is an inefﬁcient use of data and converges very slowly.
Parkinson Estimator
Good Points
■Using daily range seems sensible and provides completely separate
information to using time-based samplings such as closing prices.
Bad Points
■It is really only appropriate for measuring the volatility of a GBM
process. In particular cannot handle trends and jumps.
■It systematically underestimates volatility.
Garman-Klass Estimator
Good Points
■It is up to eight times more efﬁcient than close-to-close estimator.
■It makes the best use of the commonly available price information.
Bad Points
■It is even more biased than the Parkinson estimator.
Rogers-Satchell Estimator
Good Points
■It allows for the presence of trends.
--- page 47 ---

VOLATILITY MEASUREMENT
28
Bad Points
■It still cannot deal with jumps.
Yang-Zhang Estimator
Good Points
■It is speciﬁcally designed to have minimum estimation error.
■It can handle both drift and jumps.
■It is the most efﬁcient in its use of available data.
Bad Points
■The performance degrades to that of close-to-close estimator when
process is dominated by jumps.
First Exit Time Estimator
Good Points
■It uses fundamentally different information to traditional time-series
methods.
■It is a natural estimator for online use.
■It converges relatively quickly.
■It is not affected by the presence of noisy data or jumps.
Bad Points
■It requires the use of high-frequency data.
The overall conclusion we need to draw is that there really is no indication
that any one estimator is best. All measures contain information. Given that
we are now unable to decide on purely mathematical grounds we should
consider what the various estimators are actually telling us and make our
choice based on this criterion. For example, if the Parkinson volatility is
40 percent and the close-to-close volatility is 20 percent, we can reasonably
conclude that much of the true volatility is being driven by large intraday
ranges and that the closing prices underrepresent the true volatility of
the process. This is useful knowledge when deciding how best to hedge
(Actually, it would have been useful knowledge. How useful it would be
going forward is another matter, but it seems reasonable that some classes of
stocks, such as American depository receipts (ADRs), will have somewhat
predictable Parkinson/close ratios, as much new information is revealed
when the stocks are not trading.)
--- page 48 ---

VOLATILITY MEASUREMENT
29
■Using Higher-Frequency Data
Having gone as far as we choose with estimator selection, we now look at
improving our estimates by using more data in our sample: higher frequency
data. The beneﬁts of doing so are fairly obvious. However we choose our
sampling period, things happen that are not captured by the extremes or
the closing prices. This is illustrated in Figure 2.6.
Clearly one path is more volatile than the other, but any estimator using
open, high, low, and close will give the same result. Using higher-frequency
data somewhat avoids this issue.
As we sample at higher frequencies, we generally improve the quality of
our measurement because we have increased the number of data points in
our sample without increasing the calendar time we are measuring over.
However, as we go to very high frequencies (exactly what this means is product speciﬁc, but we generally mean timescales of a minute or less) we lose
the ability to know what the true price actually is. Consider, for example, a
stock that has a true volatility of 30 percent. Using 15-minute prices, a 0.1
percent bid-ask spread can change our measurement by about 2 percent due
to our taking a noisy estimate of the true underlying price as our input. The
true price could be up to 0.1 percent away from our actual observation.
This problem becomes more acute as we increase the sampling frequency.
Finding optimal sampling frequencies in the presence of microstructure
noise was addressed by Ait-Sahalia, Mykland, and Zhang (2005), but the
econometric techniques necessary and the data storage required probably put such methods out of the reach of most option traders for the
near future.
0
0.5
1
1.5
2
2.5
Time
Price
FIGURE 2.6
Two Price Paths with the Same Open, High, Low, and Close
--- page 49 ---

VOLATILITY MEASUREMENT
30
To avoid these issues we need to choose a sampling period that is large
compared to the typical trade time. This will vary from product to product
but the 15 to 30 minutes should be a good place to start.
When analyzing daily returns, seasonality is not really a huge issue. There
is some evidence that stock volatilities are lower on Fridays and higher
on Mondays, but the differences are very small. However, there are two
importantseasonaleffectsinhigh-frequencydatathatweneedtobeawareof.
Early work on using high-frequency returns to estimate volatility studied
the foreign exchange markets. These trade continuously. Whether by design
or just good luck, this choice avoided a major issue: how to incorporate
the overnight returns. For other markets we need to account for this. In
the United States, equities trade on the exchanges for six and a half hours.
So the overnight return could clearly be different in magnitude. It is also
different in character. Most relevant news occurs during the trading day and
a signiﬁcant amount of volatility is driven by trading volume, practically all
of which occurs during public trading periods.
There are several ways to approach this problem. The ﬁrst is to simply
ignore the overnight return and only use intraday returns when estimating
volatility. This is similar in spirit to ignoring the jump in price due to a
company’s earnings announcement. But this has the fairly obvious drawback
that the overnight return is real and signiﬁcant, often of comparable
magnitude to the total intraday return.
Another method is to treat the overnight return as just another return in
the (otherwise) high-frequency series. However, treating a single 17.5-hour
return (in the case of the U.S. equities market) as equal with say 15-minute
returns doesn’t seem very natural.
My preferred method is to calculate the proportion of total variance that
the overnight return is responsible for. First, we just ignore the overnight
return and take the ﬁrst return of the day to be
x0 = ln
 Sopen
Sclose−1

(2.27)
Instead of
x0 = ln
 Sclose
Sclose−1

(2.28)
All other returns are calculated in the normal way. Now we just estimate
volatility as before and annualize the result with the appropriate factor (for
example, there are 13 half-hour periods in a trading day, so if we were
using 30-minute returns, we would multiply the result by the square root
of 13 times 252).
--- page 50 ---

VOLATILITY MEASUREMENT
31
Next we need to determine the amount of total variance that occurs
during the trading day. This can be estimated by calculating the normal
close-to-close volatility from daily data and comparing this with the volatility
calculated using the returns from the daily open to the daily close. For
most U.S. stocks, about 85 percent of the total volatility is due to activity
that occurs during the trading day. Indices are higher at around 90 percent
and ADRs are lower at around 60 to 70 percent. If we divide the raw
volatility estimate by this factor, we obtain the opening jump adjusted,
high-frequency volatility estimator. The great advantage of using more data
in this way is that a given time period contains more data points and thus
leads to a smaller sampling error. While using the last 250 trading days
to estimate current volatility seems somewhat inappropriate, 250 half-hour
trading periods only spans 20 trading days. Assuming that the true process
is stationary over such a period is far less optimistic.
The other aspect of seasonality to keep in mind is that the true volatility
varies wildly throughout the trading day, and the variation is rather
predictable. Figures 2.7, 2.8, and 2.9 show the intraday volatility calculated
as the average of the Parkinson volatility of 30-minute returns for the time
period from April 23, 2007, to June 4, 2007. We show the pattern for
Microsoft (MSFT), Citigroup (C), and Genentech (DNA). Each shows a
similar pattern where volatility peaks at the open, dies down during the
day and has a small resurgence toward the close. This pattern has also been
documented in currencies, bonds and equity indices (Lequex 1999).
This is interesting, but when trading options we are really interested in
the average volatility over a long period (known as integrated volatility in
the econometric literature). On timescales of longer than a few days the
0
0.05
0.1
0.15
0.2
0.25
0.3
8
9
10
11
12
13
14
15
16
Central Standard Time
MSFT Volatility
FIGURE 2.7
MSFT Intraday Volatility
--- page 51 ---

VOLATILITY MEASUREMENT
32
0
0.05
0.1
0.15
0.2
0.25
0.3
8
9
10
11
12
13
14
15
16
Central Standard Time
C Volatility
FIGURE 2.8
C Intraday Volatility
0
0.05
0.1
0.15
0.2
0.25
8
9
10
11
12
13
14
15
16
Central Standard Time
DNA Volatility
FIGURE 2.9
DNA Intraday Volatility
fast intraday seasonality will average out and for time periods shorter than
this, the effects of path dependency will massively overwhelm inaccuracies
in volatility prediction.
Using high-frequency data seems like an obvious thing to do. Using higher
frequency data allows us to use more data from a recent time period. This
should give convergence to the true, unobservable volatility while avoiding
the issue of using data from past periods that are now irrelevant. However,
there are some issues to consider.
First, traders who insist of sampling at very high frequencies will have
to deal seriously with the issues of microstructure. For example, bid/ask
bounce is an important feature that impacts prices but should not really be
