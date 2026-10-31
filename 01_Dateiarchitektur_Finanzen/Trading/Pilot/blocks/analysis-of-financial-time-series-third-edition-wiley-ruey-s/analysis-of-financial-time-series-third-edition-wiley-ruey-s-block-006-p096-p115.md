# Analysis of Financial Time Series, Third Edition (Wiley -- Ruey S_ Tsay -- Wiley series in probability and statistics, 3rd ed_, -- John Wiley & Sons, -- isbn13 9780470414354 -- 9f99b80c7b2dedd477f463dc5323f3b6 -- An.pdf — pages 96–115

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
--- page 97 ---

70
linear time series analysis and its applications
For the other two representations, we use long division of two polynomials.
Given two polynomials φ(B) = 1 −p
i=1 φiBi and θ(B) = 1 −q
i=1 θiBi, we
can obtain, by long division, that
θ(B)
φ(B) = 1 + ψ1B + ψ2B2 + · · · ≡ψ(B)
(2.29)
and
φ(B)
θ(B) = 1 −π1B −π2B2 −· · · ≡π(B).
(2.30)
For instance, if φ(B) = 1 −φ1B and θ(B) = 1 −θ1B, then
ψ(B) = 1 −θ1B
1 −φ1B = 1 + (φ1 −θ1)B + φ1(φ1 −θ1)B2 + φ2
1(φ1 −θ1)B3 + · · · ,
π(B) = 1 −φ1B
1 −θ1B = 1 −(φ1 −θ1)B −θ1(φ1 −θ1)B2 −θ2
1 (φ1 −θ1)B3 −· · · .
From the deﬁnition, ψ(B)π(B) = 1. Making use of the fact that Bc = c for any
constant (because the value of a constant is time invariant), we have
φ0
θ(1) =
φ0
1 −θ1 −· · · −θq
and
φ0
φ(1) =
φ0
1 −φ1 −· · · −φp
.
AR Representation
Using the result of long division in Eq. (2.30), the ARMA(p, q) model can be
written as
rt =
φ0
1 −θ1 −· · · −θq
+ π1rt−1 + π2rt−2 + π3rt−3 + · · · + at.
(2.31)
This representation shows the dependence of the current return rt on the past
returns rt−i, where i > 0. The coefﬁcients {πi} are referred to as the π weights of
an ARMA model. To show that the contribution of the lagged value rt−i to rt is
diminishing as i increases, the πi coefﬁcient should decay to zero as i increases. An
ARMA(p, q) model that has this property is said to be invertible. For a pure AR
model, θ(B) = 1 so that π(B) = φ(B), which is a ﬁnite-degree polynomial. Thus,
πi = 0 for i > p, and the model is invertible. For other ARMA models, a sufﬁcient
condition for invertibility is that all the zeros of the polynomial θ(B) are greater
than unity in modulus. For example, consider the MA(1) model rt = (1 −θ1B)at.
The zero of the ﬁrst-order polynomial 1 −θ1B is B = 1/θ1. Therefore, an MA(1)
model is invertible if |1/θ1| > 1. This is equivalent to |θ1| < 1.
From the AR representation in Eq. (2.31), an invertible ARMA(p, q) series rt
is a linear combination of the current shock at and a weighted average of the past
values. The weights decay exponentially for more remote past values.
--- page 98 ---

unit-root nonstationarity
71
MA Representation
Again, using the result of long division in Eq. (2.29), an ARMA(p, q) model can
also be written as
rt = µ + at + ψ1at−1 + ψ2at−2 + · · · = µ + ψ(B)at,
(2.32)
where µ = E(rt) = φ0/(1 −φ1 −· · · −φp). This representation shows explicitly
the impact of the past shock at−i (i > 0) on the current return rt. The coefﬁcients
{ψi} are referred to as the impulse response function of the ARMA model. For
a weakly stationary series, the ψi coefﬁcients decay exponentially as i increases.
This is understandable as the effect of shock at−i on the return rt should diminish
over time. Thus, for a stationary ARMA model, the shock at−i does not have
a permanent impact on the series. If φ0̸ = 0, then the MA representation has a
constant term, which is the mean of rt [i.e., φ0/(1 −φ1 −· · · −φp)].
The MA representation in Eq. (2.32) is also useful in computing the variance
of a forecast error. At the forecast origin h, we have the shocks ah, ah−1, . . ..
Therefore, the ℓ-step-ahead point forecast is
ˆrh(ℓ) = µ + ψℓah + ψℓ+1ah−1 + · · · ,
(2.33)
and the associated forecast error is
eh(ℓ) = ah+ℓ+ ψ1ah+ℓ−1 + · · · + ψℓ−1ah+1.
Consequently, the variance of ℓ-step-ahead forecast error is
Var[eh(ℓ)] = (1 + ψ2
1 + · · · + ψ2
ℓ−1)σ 2
a ,
(2.34)
which, as expected, is a nondecreasing function of the forecast horizon ℓ.
Finally, the MA representation in Eq. (2.32) provides a simple proof of mean
reversion of a stationary time series. The stationarity implies that ψi approaches
zero as i →∞. Therefore, by Eq. (2.33), we have ˆrh(ℓ) →µ as ℓ→∞. Because
ˆrh(ℓ) is the conditional expectation of rh+ℓat the forecast origin h, the result
says that in the long term the return series is expected to approach its mean,
that is, the series is mean reverting. Furthermore, using the MA representation in
Eq. (2.32), we have Var(rt) = (1 + ∞
i=1 ψ2
i )σ 2
a . Consequently, by Eq. (2.34), we
have Var[eh(ℓ)] →Var(rt) as ℓ→∞. The speed by which ˆrh(ℓ) approaches µ
determines the speed of mean reverting.
2.7
UNIT-ROOT NONSTATIONARITY
So far we have focused on return series that are stationary. In some studies, interest
rates, foreign exchange rates, or the price series of an asset are of interest. These
series tend to be nonstationary. For a price series, the nonstationarity is mainly
--- page 99 ---

72
linear time series analysis and its applications
due to the fact that there is no ﬁxed level for the price. In the time series literature, such a nonstationary series is called unit-root nonstationary time series.
The best known example of unit-root nonstationary time series is the random-walk
model.
2.7.1
Random Walk
A time series {pt} is a random walk if it satisﬁes
pt = pt−1 + at,
(2.35)
where p0 is a real number denoting the starting value of the process and {at} is a
white noise series. If pt is the log price of a particular stock at date t, then p0 could
be the log price of the stock at its initial public offering (IPO) (i.e., the logged IPO
price). If at has a symmetric distribution around zero, then conditional on pt−1,
pt has a 50–50 chance to go up or down, implying that pt would go up or down
at random. If we treat the random-walk model as a special AR(1) model, then the
coefﬁcient of pt−1 is unity, which does not satisfy the weak stationarity condition
of an AR(1) model. A random-walk series is, therefore, not weakly stationary, and
we call it a unit-root nonstationary time series.
The random-walk model has widely been considered as a statistical model for
the movement of logged stock prices. Under such a model, the stock price is not
predictable or mean reverting. To see this, the 1-step-ahead forecast of model (2.35)
at the forecast origin h is
ˆph(1) = E(ph+1|ph, ph−1, . . .) = ph,
which is the log price of the stock at the forecast origin. Such a forecast has no
practical value. The 2-step-ahead forecast is
ˆph(2) = E(ph+2|ph, ph−1, . . .) = E(ph+1 + ah+2|ph, ph−1, . . .)
= E(ph+1|ph, ph−1, . . .) = ˆph(1) = ph,
which again is the log price at the forecast origin. In fact, for any forecast horizon
ℓ> 0, we have
ˆph(ℓ) = ph.
Thus, for all forecast horizons, point forecasts of a random-walk model are simply
the value of the series at the forecast origin. Therefore, the process is not mean
reverting.
The MA representation of the random-walk model in Eq. (2.35) is
pt = at + at−1 + at−2 + · · · .
--- page 100 ---

unit-root nonstationarity
73
This representation has several important practical implications. First, the ℓ-stepahead forecast error is
eh(ℓ) = ah+ℓ+ · · · + ah+1,
so that Var[eh(ℓ)] = ℓσ 2
a , which diverges to inﬁnity as ℓ→∞. The length of an
interval forecast of ph+ℓwill approach inﬁnity as the forecast horizon-increases.
This result says that the usefulness of point forecast ˆph(ℓ) diminishes as ℓincreases,
which again implies that the model is not predictable. Second, the unconditional
variance of pt is unbounded because Var[eh(ℓ)] approaches inﬁnity as ℓincreases.
Theoretically, this means that pt can assume any real value for a sufﬁciently large t.
For the log price pt of an individual stock, this is plausible. Yet for market indexes,
negative log price is very rare if it happens at all. In this sense, the adequacy of a
random-walk model for market indexes is questionable. Third, from the representation, ψi = 1 for all i. Thus, the impact of any past shock at−i on pt does not
decay over time. Consequently, the series has a strong memory as it remembers all
of the past shocks. In economics, the shocks are said to have a permanent effect
on the series. The strong memory of a unit-root time series can be seen from the
sample ACF of the observed series. The sample ACFs are all approaching 1 as the
sample size increases.
2.7.2
Random Walk with Drift
As shown by empirical examples considered so far, the log return series of a market
index tends to have a small and positive mean. This implies that the model for the
log price is
pt = µ + pt−1 + at,
(2.36)
where µ = E(pt −pt−1) and {at} is a zero-mean white noise series. The constant
term µ of model (2.36) is very important in ﬁnancial study. It represents the time
trend of the log price pt and is often referred to as the drift of the model. To see
this, assume that the initial log price is p0. Then we have
p1 = µ + p0 + a1,
p2 = µ + p1 + a2 = 2µ + p0 + a2 + a1,
...
pt = tµ + p0 + at + at−1 + · · · + a1.
The last equation shows that the log price consists of a time trend tµ and a
pure random-walk process t
i=1 ai. Because Var(t
i=1 ai) = tσ 2
a , where σ 2
a is the
variance of at, the conditional standard deviation of pt is √tσa, which grows at a
slower rate than the conditional expectation of pt. Therefore, if we graph pt against
--- page 101 ---

74
linear time series analysis and its applications
the time index t, we have a time trend with slope µ. A positive slope µ implies
that the log price eventually goes to inﬁnity. In contrast, a negative µ implies that
the log price would converge to −∞as t increases. Based on the above discussion,
it is then not surprising to see that the log return series of the CRSP valueand
equal-weighted indexes have a small, but statistically signiﬁcant, positive mean.
To illustrate the effect of the drift parameter on the price series, we consider the
monthly log stock returns of the 3M Company from February 1946 to December
2008. As shown by the sample EACF in Table 2.5, the series has no signiﬁcant
serial correlation. The series thus follows the simple model
rt = 0.0103 + at,
ˆσa = 0.0637,
(2.37)
where 0.0103 is the sample mean of rt and has a standard error 0.0023. The mean
of the monthly log returns of 3M stock is, therefore, signiﬁcantly different from
zero at the 1% level. As a matter of fact, the one-sample test of zero mean shows
a t ratio of 4.44 with a p value close to 0. We use the log return series to construct
two log price series, namely
pt =
t
i=1
ri
and
p∗
t =
t
i=1
ai,
where ai is the mean-corrected log return in Eq. (2.37) (i.e., at = rt −0.0103).
The pt is the log price of 3M stock, assuming that the initial log price is zero
(i.e., the log price of January 1946 was zero). The p∗
t is the corresponding log
price if the mean of log returns was zero. Figure 2.10 shows the time plots of
pt and p∗
t as well as a straight line yt = 0.0103 × t + 1946, where t is the time
sequence of the returns and 1946 is the starting year of the stock. From the plots,
the importance of the constant 0.0103 in Eq. (2.37) is evident. In addition, as
expected, it represents the slope of the upward trend of pt.
Interpretation of the Constant Term
From the previous discussions, it is important to understand the meaning of a
constant term in a time series model. First, for an MA(q) model in Eq. (2.22), the
constant term is simply the mean of the series. Second, for a stationary AR(p) model
in Eq. (2.9) or ARMA(p, q) model in Eq. (2.28), the constant term is related to
the mean via µ = φ0/(1 −φ1 −· · · −φp). Third, for a random walk with drift, the
constant term becomes the time slope of the series. These different interpretations
for the constant term in a time series model clearly highlight the difference between
dynamic and usual linear regression models.
Another important difference between dynamic and regression models is shown
by an AR(1) model and a simple linear regression model,
rt = φ0 + φ1rt−1 + at
and
yt = β0 + β1xt + at.
For the AR(1) model to be meaningful, the coefﬁcient φ1 must satisfy |φ1| ≤1.
However, the coefﬁcient β1 can assume any ﬁxed real number.
--- page 102 ---

unit-root nonstationarity
75
•••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••
•••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••
Year
ln(price)
1950
1960
1970
1980
1990
2000
2010
0
2
4
6
8
oooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo
oooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo
Figure 2.10
Time plots of log prices for 3M stock from February 1946 to December 2008, assuming
that log price of January 1946 was zero. The “o” line is for log price without time trend. Straight line
is yt = 0.0103 × t + 1946.
2.7.3
Trend-Stationary Time Series
A closely related model that exhibits linear trend is the trend-stationary time series
model,
pt = β0 + β1t + rt,
where rt is a stationary time series, for example, a stationary AR(p) series. Here pt
grows linearly in time with rate β1 and hence can exhibit behavior similar to that of
a random-walk model with drift. However, there is a major difference between the
two models. To see this, suppose that p0 is ﬁxed. The random-walk model with drift
assumes the mean E(pt) = p0 + µt and variance Var(pt) = tσ 2
a , both of them are
time dependent. On the other hand, the trend-stationary model assumes the mean
E(pt) = β0 + β1t, which depends on time, and variance Var(pt) = Var(rt), which
is ﬁnite and time invariant. The trend-stationary series can be transformed into a
stationary one by removing the time trend via a simple linear regression analysis.
For analysis of trend-stationary time series, see the method of Section 2.9.
2.7.4
General Unit-Root Nonstationary Models
Consider an ARMA model. If one extends the model by allowing the AR polynomial to have 1 as a characteristic root, then the model becomes the well-known
--- page 103 ---

76
linear time series analysis and its applications
autoregressive integrated moving-average (ARIMA) model. An ARIMA model is
said to be unit-root nonstationary because its AR polynomial has a unit root. Like
a random-walk model, an ARIMA model has strong memory because the ψi coef-
ﬁcients in its MA representation do not decay over time to zero, implying that the
past shock at−i of the model has a permanent effect on the series. A conventional
approach for handling unit-root nonstationarity is to use differencing.
Differencing
A time series yt is said to be an ARIMA(p, 1, q) process if the change series
ct = yt −yt−1 = (1 −B)yt follows a stationary and invertible ARMA(p, q) model.
In ﬁnance, price series are commonly believed to be nonstationary, but the log
return series, rt = ln(Pt) −ln(Pt−1), is stationary. In this case, the log price series
is unit-root nonstationary and hence can be treated as an ARIMA process. The
idea of transforming a nonstationary series into a stationary one by considering
its change series is called differencing in the time series literature. More formally,
ct = yt −yt−1 is referred to as the ﬁrst differenced series of yt. In some scientiﬁc
ﬁelds, a time series yt may contain multiple unit roots and needs to be differenced
multiple times to become stationary. For example, if both yt and its ﬁrst differenced
series ct = yt −yt−1 are unit-root nonstationary, but st = ct −ct−1 = yt −2yt−1 +
yt−2 is weakly stationary, then yt has double unit roots, and st is the second
differenced series of yt. In addition, if st follows an ARMA(p, q) model, then yt
is an ARIMA(p, 2, q) process. For such a time series, if st has a nonzero mean,
then yt has a quadratic time function and the quadratic time coefﬁcient is related
to the mean of st. The seasonally adjusted series of U.S. quarterly gross domestic
product implicit price deﬂator might have double unit roots. However, the mean
of the second differenced series is not signiﬁcantly different from zero; see the
Exercises of this chapter. Box, Jenkins, and Reinsel (1994) discuss many properties
of general ARIMA models.
2.7.5
Unit-Root Test
To test whether the log price pt of an asset follows a random walk or a random
walk with drift, we employ the models
pt = φ1pt−1 + et
(2.38)
pt = φ0 + φ1pt−1 + et,
(2.39)
where et denotes the error term, and consider the null hypothesis H0 : φ1 = 1
versus the alternative hypothesis Ha : φ1 < 1. This is the well-known unit-root
testing problem; see Dickey and Fuller (1979). A convenient test statistic is the
t ratio of the least-squares (LS) estimate of φ1 under the null hypothesis. For
Eq. (2.38), the LS method gives
ˆφ1 =
T
t=1 pt−1pt
T
t=1 p2
t−1
,
ˆσ 2
e =
T
t=1(pt −ˆφ1pt−1)2
T −1
,
--- page 104 ---

unit-root nonstationarity
77
where p0 = 0 and T is the sample size. The t ratio is
DF ≡t ratio =
ˆφ1 −1
std( ˆφ1)
=
T
t=1 pt−1et
ˆσe
T
t=1 p2
t−1
,
which is commonly referred to as the Dickey–Fuller (DF) test. If {et} is a white
noise series with ﬁnite moments of order slightly greater than 2, then the DF statistic
converges to a function of the standard Brownian motion as T →∞; see Chan and
Wei (1988) and Phillips (1987) for more information. If φ0 is zero but Eq. (2.39)
is employed anyway, then the resulting t ratio for testing φ1 = 1 will converge to
another nonstandard asymptotic distribution. In either case, simulation is used to
obtain critical values of the test statistics; see Fuller (1976, Chapter 8) for selected
critical values. Yet if φ0̸ = 0 and Eq. (2.39) is used, then the t ratio for testing
φ1 = 1 is asymptotically normal. However, large sample sizes are needed for the
asymptotic normal distribution to hold. Standard Brownian motion is introduced in
Chapter 6.
For many economic time series, ARIMA(p, d, q) models might be more appropriate than the simple model in Eq. (2.39). In the econometric literature, AR(p)
models are often used. Denote the series by xt. To verify the existence of a unit
root in an AR(p) process, one may perform the test H0 : β = 1 vs. Ha : β < 1
using the regression
xt = ct + βxt−1 +
p−1

i=1
φi
xt−i + et,
(2.40)
where ct is a deterministic function of the time index t and
xj = xj −xj−1 is the
differenced series of xt. In practice, ct can be zero or a constant or ct = ω0 + ω1t.
The t ratio of ˆβ −1,
ADF-test =
ˆβ −1
std( ˆβ)
,
where ˆβ denotes the least-squares estimate of β, is the well-known augmented
Dickey–Fuller (ADF) unit-root test. Note that because of the ﬁrst differencing,
Eq. (2.40) is equivalent to an AR(p) model with deterministic function ct. Equation
(2.40) can also be rewritten as

xt = ct + βcxt−1 +
p−1

i=1
φi
xt−i + et,
where βc = β −1. One can then test the equivalent hypothesis H0 : βc = 0 vs.
Ha : βc < 0.
--- page 105 ---

78
linear time series analysis and its applications
Year
ln(GDP)
1950 1960 1970 1980 1990 2000 2010
6
7
8
9
(a)
Lag
ACF
0
5
10
15
0.0
0.4
0.8
Year
diff(l-gdp)
1950 1960 1970 1980 1990 2000 2010
−0.02 0.0 0.02 0.04 0.06
(c)
(b)
Lag
0
5
10
15
(d)
Partial ACF
−0.1
0.1
0.3
Figure 2.11
Log series of U.S. quarterly GDP from 1947.I to 2008.IV: (a) time plot of logged GDP
series, (b) sample ACF of log GDP data, (c) time plot of ﬁrst differenced series, and (d) sample PACF
of differenced series.
Example 2.2.
Consider the log series of U.S. quarterly GDP from 1947.I to
2008.IV. The series exhibits an upward trend, showing the growth of the U.S.
economy, and has high sample serial correlations; see the lower left panel of
Figure 2.11. The ﬁrst differenced series, representing the growth rate of U.S.
GDP and also shown in Figure 2.11, seems to vary around a ﬁxed mean level,
even though the variability appears to be smaller in recent years. To conﬁrm the
observed phenomenon, we apply the ADF unit-root test to the log series. Based
on the sample PACF of the differenced series shown in Figure 2.11, we choose
p = 10. Other values of p are also used, but they do not alter the conclusion of
the test. With p = 10, the ADF test statistic is −1.701 with a p value 0.4297, indicating that the unit-root hypothesis cannot be rejected. From the attached S-Plus
output, ˆβ = 1 + ˆβc = 1 −0.0008 = 0.9992.
R Demonstration
> library(fUnitRoots)
> da=read.table("q-gdp4708.txt",header=T)
> gdp=log(da[,4])
> m1=ar(diff(gdp),method=’mle’)
> m1$order
[1] 10
> adfTest(gdp,lags=10,type=c("c"))
--- page 106 ---

unit-root nonstationarity
79
Title:
Augmented Dickey-Fuller Test
Test Results:
PARAMETER:
Lag Order: 10
STATISTIC:
Dickey-Fuller: -1.6109
P VALUE:
0.4569
S-Plus Demonstration
The following output has been edited:
> adft=unitroot(gdp,trend=’c’,method=’adf’,lags=10)
> summary(adft)
Test for Unit Root: Augmented DF Test
Null Hypothesis: there is a unit root
Type of Test: t-test
Test Statistic: -1.701
P-value: 0.4297
Coefficients:
Value Std. Error t value Pr(>|t|)
lag1 -0.0008
0.0005
-1.7006
0.0904
lag2
0.3799
0.0659
5.7637
0.0000
lag3
0.1883
0.0696
2.7047
0.0074
...
lag10 0.1784
0.0637
2.8023
0.0055
constant 0.0134
0.0045
2.9636
0.0034
Regression Diagnostics:
R-Squared 0.2877
Adjusted R-Squared 0.2564
Durbin-Watson Stat 1.9940
Residual standard error: 0.009318 on 234 degrees of freedom
As another example, consider the log series of the S&P 500 index from January 3, 1950, to April 16, 2008, for 14,462 observations. The series is shown in
Figure 2.12. Testing for a unit root in the index is relevant if one wishes to verify
empirically that the Index follows a random walk with drift. To this end, we use
ct = ω0 + ω1t in applying the ADF test. Furthermore, we choose p = 15 based
on the sample PACF of the ﬁrst differenced series. The resulting test statistic is
−1.998 with a p value 0.602. Thus, the unit-root hypothesis cannot be rejected
at any reasonable signiﬁcance level. The constant term is statistically signiﬁcant,
whereas the estimate of the time trend is not at the usual 5% level. The latter is
--- page 107 ---

80
linear time series analysis and its applications
Year
ln(SP5)
1950
1960
1970
1980
1990
2000
2010
3
4
5
6
7
Figure 2.12
Time plot of logarithm of daily S&P 500 index from January 3, 1950, to April 16, 2008.
signiﬁcant at the 10% level, however. In summary, for the period from January
1950 to April 2008, the log series of the S&P 500 index contains a unit root and
a positive drift, but there is no strong evidence of a time trend.
R Demonstration
> library(fUnitRoots)
> da=read.table("d-sp55008.txt",header=T)
> sp5=log(da[,7])
> m2=ar(diff(sp5),method=’mle’)
> m2$order
[1] 2
> adfTest(sp5,lags=2,type=("ct"))
Title:
Augmented Dickey-Fuller Test
Test Results:
PARAMETER:
Lag Order: 2
STATISTIC:
Dickey-Fuller: -2.0179
P VALUE: 0.5708
> adfTest(sp5,lags=15,type=("ct"))
--- page 108 ---

seasonal models
81
Title:
Augmented Dickey-Fuller Test
Test Results:
PARAMETER:
Lag Order: 15
STATISTIC:
Dickey-Fuller: -1.9946
P VALUE:
0.5807
S-Plus Demonstration
The following output has been edited:
> adft=unitroot(sp5,method=’adf’,trend=’ct’,lags=15)
> summary(adft)
Test for Unit Root: Augmented DF Test
Null Hypothesis: there is a unit root
Type of Test: t-test
Test Statistic: -1.998
P-value: 0.602
Coefficients:
Value Std. Error t value Pr(>|t|)
lag1 -0.0005
0.0003
-1.9977
0.0458
lag2
0.0722
0.0083
8.7374
0.0000
lag3 -0.0386
0.0083
-4.6532
0.0000
lag4 -0.0071
0.0083
-0.8548
0.3927
...
lag15
0.0133
0.0083
1.6122
0.1069
constant
0.0019
0.0008
2.3907
0.0168
time
0.0020
0.0011
1.8507
0.0642
Regression Diagnostics:
R-Squared 0.0081
Adjusted R-Squared 0.0070
Durbin-Watson Stat 1.9995
Residual standard error: 0.008981 on 14643 degrees of freedom
2.8
SEASONAL MODELS
Some ﬁnancial time series such as quarterly earnings per share of a company
exhibits certain cyclical or periodic behavior. Such a time series is called a seasonal time series. Figure 2.13(a) shows the time plot of quarterly earnings per share
of Johnson & Johnson from the ﬁrst quarter of 1960 to the last quarter of 1980.
--- page 109 ---

82
linear time series analysis and its applications
Year
Earning
1960
1965
1970
1975
1980
0
5
10
15
•••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••
•
•••
•
••••
•••
•
••
•
•
•
••
•
(a)
Year
1960
1965
1970
1975
1980
(b)
Log earning
0
1
2
•••
••••
••••
•••••••••••••••••••••••••••••••••••••••••••••••••••••••••
••••••••
•••
•
••••
Figure 2.13
Time plots of quarterly earnings per share of Johnson & Johnson from 1960 to 1980:
(a) observed earnings and (b) log earnings.
The data obtained from Shumway and Stoffer (2000) possess some special characteristics. In particular, the earnings grew exponentially during the sample period
and had a strong seasonality. Furthermore, the variability of earnings increased
over time. The cyclical pattern repeats itself every year so that the periodicity of
the series is 4. If monthly data are considered (e.g., monthly sales of Wal-Mart
stores), then the periodicity is 12. Seasonal time series models are also useful in
pricing weather-related derivatives and energy futures because most environmental
time series exhibit strong seasonal behavior.
Analysis of seasonal time series has a long history. In some applications, seasonality is of secondary importance and is removed from the data, resulting in a
seasonally adjusted time series that is then used to make inference. The procedure
to remove seasonality from a time series is referred to as seasonal adjustment. Most
economic data published by the U.S. government are seasonally adjusted (e.g., the
growth rate of gross domestic product and the unemployment rate). In other applications such as forecasting, seasonality is as important as other characteristics of
the data and must be handled accordingly. Because forecasting is a major objective
of ﬁnancial time series analysis, we focus on the latter approach and discuss some
econometric models that are useful in modeling seasonal time series.
2.8.1
Seasonal Differencing
Figure 2.13(b) shows the time plot of log earnings per share of Johnson & Johnson.
We took the log transformation for two reasons. First, it is used to handle the
--- page 110 ---

seasonal models
83
exponential growth of the series. Indeed, the plot conﬁrms that the growth is linear
in the log scale. Second, the transformation is used to stablize the variability of
the series. Again, the increasing pattern in variability of Figure 2.13(a) disappears
in the new plot. Log transformation is commonly used in analysis of ﬁnancial
and economic time series. In this particular instance, all earnings are positive so
that no adjustment is needed before taking the transformation. In some cases,
one may need to add a positive constant to every data point before taking the
transformation.
Denote the log earnings by xt. The upper left panel of Figure 2.14 shows the sample ACF of xt, which indicates that the quarterly log earnings per share has strong
serial correlations. A conventional method to handle such strong serial correlations
is to consider the ﬁrst differenced series of xt [i.e.,
xt = xt −xt−1 = (1 −B)xt].
The lower left plot of Figure 2.14 gives the sample ACF of
xt. The ACF is strong
when the lag is a multiple of periodicity 4. This is a well-documented behavior of sample ACF of a seasonal time series. Following the procedure of Box,
Jenkins, and Reinsel (1994, Chapter 9), we take another difference of the data,
that is,

4(
xt) = (1 −B4)
xt =
xt −
xt−4 = xt −xt−1 −xt−4 + xt−5.
Lag
ACF
0
5
10
15
−0.2
0.2
0.6
1.0
(a)
Lag
0
5
10
15
(c)
Lag
0
5
10
15
(b)
Lag
0
5
10
15
(d)
ACF
−0.5
0.0
0.5
1.0
ACF
−0.2
0.2
0.6
1.0
ACF
−0.4 0.0
0.4
0.8
Figure 2.14
Sample ACF of log series of quarterly earnings per share of Johnson & Johnson from
1960 to 1980. (a) log earnings, (b) ﬁrst differenced series, (c) seasonally differenced series, and (d)
series with regular and seasonal differencing.
--- page 111 ---

84
linear time series analysis and its applications
The operation
4 = (1 −B4) is called a seasonal differencing. In general, for a
seasonal time series yt with periodicity s, seasonal differencing means

syt = yt −yt−s = (1 −Bs)yt.
The conventional difference
yt = yt −yt−1 = (1 −B)yt is referred to as the
regular differencing. The lower right plot of Figure 2.14 shows the sample ACF
of
4
xt, which has a signiﬁcant negative ACF at lag 1 and a marginal negative
correlation at lag 4. For completeness, Figure 2.14 also gives the sample ACF of
the seasonally differenced series
4xt.
2.8.2
Multiplicative Seasonal Models
The behavior of the sample ACF of (1 −B4)(1 −B)xt in Figure 2.14 is common
among seasonal time series. It led to the development of the following special
seasonal time series model:
(1 −Bs)(1 −B)xt = (1 −θB)(1 −Bs)at,
(2.41)
where s is the periodicity of the series, at is a white noise series, |θ| < 1, and
|| < 1. This model is referred to as the airline model in the literature; see Box,
Jenkins, and Reinsel (1994, Chapter 9). It has been found to be widely applicable
in modeling seasonal time series. The AR part of the model simply consists of the
regular and seasonal differences, whereas the MA part involves two parameters.
Focusing on the MA part (i.e., on the model),
wt = (1 −θB)(1 −Bs)at = at −θat−1 −at−s + θat−s−1,
where wt = (1 −Bs)(1 −B)xt and s > 1. It is easy to obtain that E(wt) = 0 and
Var(wt) = (1 + θ2)(1 + 2)σ 2
a ,
Cov(wt, wt−1) = −θ(1 + 2)σ 2
a ,
Cov(wt, wt−s+1) = θσ 2
a ,
Cov(wt, wt−s) = −(1 + θ2)σ 2
a ,
Cov(wt, wt−s−1) = θσ 2
a ,
Cov(wt, wt−ℓ) = 0,
for
ℓ̸ = 0, 1, s −1, s, s + 1.
Consequently, the ACF of the wt series is given by
ρ1 =
−θ
1 + θ2 ,
ρs =
−
1 + 2 ,
ρs−1 = ρs+1 = ρ1ρs =
θ
(1 + θ2)(1 + 2),
--- page 112 ---

seasonal models
85
and ρℓ= 0 for ℓ> 0 and ℓ̸ = 1, s −1, s, s + 1. For example, if wt is a quarterly
time series, then s = 4 and for ℓ> 0, the ACF ρℓis nonzero at lags 1, 3, 4, and
5 only.
It is interesting to compare the prior ACF with those of the MA(1) model
yt = (1 −θB)at and the MA(s) model zt = (1 −Bs)at. The ACF of yt and zt
series are
ρ1(y) =
−θ
1 + θ2
and
ρℓ(y) = 0,
ℓ> 1,
ρs(z) =
−
1 + 2
and
ρℓ(z) = 0,
ℓ> 0,̸ = s.
We see that (i) ρ1 = ρ1(y), (ii) ρs = ρs(z), and (iii) ρs−1 = ρs+1 = ρ1(y) × ρs(z).
Therefore, the ACF of wt at lags (s −1) and (s + 1) can be regarded as the
interaction between lag-1 and lag-s serial dependence, and the model of wt is
called a multiplicative seasonal MA model. In practice, a multiplicative seasonal
model says that the dynamics of the regular and seasonal components of the series
are approximately orthogonal.
The model
wt = (1 −θB −Bs)at,
(2.42)
where |θ| < 1 and || < 1, is a nonmultiplicative seasonal MA model. It is easy
to see that for the model in Eq. (2.42), ρs+1 = 0. A multiplicative model is more
parsimonious than the corresponding nonmultiplicative model because both models
use the same number of parameters, but the multiplicative model has more nonzero
ACFs.
Example 2.3.
In this example we apply the airline model to the log series of
quarterly earnings per share of Johnson & Johnson from 1960 to 1980. Based on
the exact-likelihood method, the ﬁtted model is
(1 −B)(1 −B4)xt = (1 −0.678B)(1 −0.314B4)at,
ˆσa = 0.089,
where standard errors of the two MA parameters are 0.080 and 0.101, respectively.
The Ljung–Box statistics of the residuals show Q(12) = 10.0 with a p value of
0.44. The model appears to be adequate.
To illustrate the forecasting performance of the prior seasonal model, we reestimate the model using the ﬁrst 76 observations and reserve the last 8 data points
for forecasting evaluation. We compute 1-stepto 8-step-ahead forecasts and their
standard errors of the ﬁtted model at the forecast origin h = 76. An antilog transformation is taken to obtain forecasts of earnings per share using the relationship
between normal and lognormal distributions given in Chapter 1. Figure 2.15 shows
the forecast performance of the model, where the observed data are in solid line,
point forecasts are shown by dots, and the dashed lines show 95% interval forecasts. The forecasts show a strong seasonal pattern and are close to the observed
--- page 113 ---

86
linear time series analysis and its applications
Year
Earning
1978
1979
1980
1981
0
5
10
15
20
25
30
·
·
·
·
·
·
·
·
Figure 2.15
Out-of-sample point and interval forecasts for quarterly earnings of Johnson & Johnson.
Forecast origin is fourth quarter of 1978. In plot, solid line shows actual observations, dots represent
point forecasts, and dashed lines show 95% interval forecasts.
data. Finally, for an alternative approach to modeling the quarterly earnings data,
see Example 11.3.
When the seasonal pattern of a time series is stable over time (e.g., close to a
deterministic function), dummy variables may be used to handle the seasonality.
This approach is taken by some analysts. However, deterministic seasonality is a
special case of the multiplicative seasonal model discussed before. Speciﬁcally,
if  = 1, then model (2.41) contains a deterministic seasonal component. Consequently, the same forecasts are obtained by using either dummy variables or a
multiplicative seasonal model when the seasonal pattern is deterministic. Yet use of
dummy variables can lead to inferior forecasts if the seasonal pattern is not deterministic. In practice, we recommend that the exact-likelihood method should be
used to estimate a multiplicative seasonal model, especially when the sample size is
small or when there is the possibility of having a deterministic seasonal component.
Example 2.4.
To demonstrate deterministic seasonal behavior, consider the
monthly simple returns of the CRSP Decile 1 Index from January 1970 to December
2008 for 468 observations. The series is shown in Figure 2.16(a), and the time plot
does not show any clear pattern of seasonality. However, the sample ACF of the
return series shown in Figure 2.16(b) contains signiﬁcant lags at 12, 24, and 36 as
well as lag 1. If seasonal ARMA models are entertained, a model in the form
(1 −φ1B)(1 −φ12B12)Rt = (1 −θ12B12)at
--- page 114 ---

seasonal models
87
Year
Simple return
1970
1980
1990
2000
2010
−0.2 0.0 0.2 0.4
(a)
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
(b)
Lag
0
10
20
30
(d)
Year
Adjusted return
1970
1980
1990
2000
2010
−0.2
0.0
0.2
0.4
(c)
ACF
−0.2
0.2
0.6
1.0
Figure 2.16
Monthly simple returns of CRSP Decile 1 index from January 1970 to December 2008:
(a) time plot of the simple returns, (b) sample ACF of simple returns, (c) time plot of simple returns
after adjusting for January effect, and (d) sample ACF of adjusted simple returns.
is identiﬁed, where Rt denotes the monthly simple return. Using the conditionallikelihood method, the ﬁtted model is
(1 −0.18B)(1 −0.87B12)Rt = (1 −0.74B12)at,
˜σa = 0.069.
See the attached SCA (Scientiﬁc Computing Associates) output below. The estimates of the seasonal AR and MA coefﬁcients are of similar magnitude. If the
exact-likelihood method is used, we have
(1 −0.188B)(1 −0.951B12)Rt = (1 −0.997B12)at,
˜σa = 0.063.
The cancellation between seasonal AR and MA factors is clearly seen. This highlights the usefulness of using the exact-likelihood method and, the estimation result
suggests that the seasonal behavior might be deterministic. To further conﬁrm this
assertion, we deﬁne the dummy variable for January, that is,
Jant =

1
if t is January,
0
otherwise,
and employ the simple linear regression
Rt = β0 + β1Jant + et.
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
