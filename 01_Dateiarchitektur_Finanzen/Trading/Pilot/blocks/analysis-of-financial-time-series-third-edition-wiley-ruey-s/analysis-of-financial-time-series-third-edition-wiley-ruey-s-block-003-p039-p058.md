# Analysis of Financial Time Series, Third Edition (Wiley -- Ruey S_ Tsay -- Wiley series in probability and statistics, 3rd ed_, -- John Wiley & Sons, -- isbn13 9780470414354 -- 9f99b80c7b2dedd477f463dc5323f3b6 -- An.pdf — pages 39–58

--- page 39 ---

12
ﬁnancial time series and their characteristics
R Demonstration
In the following program code > is the prompt character and % denotes explanation:
> library(fBasics)
% Load the package fBasics.
> da=read.table("d-ibm3dx7008.txt",header=T)
% Load the data.
% header=T means 1st row of the data file contains
% variable names. The default is header=F, i.e., no names.
> dim(da)
% Find size of the data: 9845 rows and 5 columns.
[1] 9845
5
> da[1,]
% See the first row of the data
Date
rtn
vwretd
ewretd
sprtrn % column names
1 19700102 0.000686 0.012137 0.03345 0.010211
> ibm=da[,2]
% Obtain IBM simple returns
> sibm=ibm*100
% Percentage simple returns
> basicStats(sibm)
% Compute the summary statistics
sibm
nobs
9845.000000 % Sample size
NAs
0.000000 % Number of missing values
Minimum
-22.963000
Maximum
13.163600
1. Quartile
-0.857100 % 25th percentile
3. Quartile
0.883300 % 75th percentile
Mean
0.040161 % Sample mean
Median
0.000000 % Sample median
Sum
395.387600 % Sum of the percentage simple returns
SE Mean
0.017058 % Standard error of the sample mean
LCL Mean
0.006724 % Lower bound of 95% conf.
% interval for mean
UCL Mean
0.073599 % Upper bound of 95% conf.
% interval for mean
Variance
2.864705 % Sample variance
Stdev
1.692544 % Sample standard error
Skewness
0.061399 % Sample skewness
Kurtosis
9.916359 % Sample excess kurtosis.
% Alternatively, one can use individual commands as follows:
> mean(sibm)
[1] 0.04016126
> var(sibm)
[1] 2.864705
> sqrt(var(sibm)) % Standard deviation
[1] 1.692544
> skewness(sibm)
[1] 0.06139878
attr(,"method")
--- page 40 ---

distributional properties of returns
13
[1] "moment"
> kurtosis(sibm)
[1] 9.91636
attr(,"method")
[1] "excess"
% Simple tests
> s1=skewness(sibm)
> t1=s1/sqrt(6/9845) % Compute test statistic
> t1
[1] 2.487093
> pv=2*(1-pnorm(t1)) % Compute p-value.
> pv
[1] 0.01287919
% Turn to log returns in percentages
> libm=log(ibm+1)*100
> t.test(libm)
% Test mean being zero.
One Sample t-test
data:
libm
t = 1.5126, df = 9844, p-value = 0.1304
alternative hypothesis: true mean is not equal to 0
95 percent confidence interval:
-0.007641473
0.059290531
% The result shows that the hypothesis of zero expected return
% cannot be rejected at the 5% or 10% level.
> normalTest(libm,method=’jb’) % Normality test
Title:
Jarque - Bera Normality Test
Test Results:
STATISTIC:
X-squared: 60921.9343
P VALUE:
Asymptotic p Value: < 2.2e-16
% The result shows the normality for log-return is rejected.
S-Plus Demonstration
In the following program code > is the prompt character and % marks explanation:
> module(finmetrics) % Load the Finmetrics module.
> da=read.table("d-ibm3dx7008.txt",header=T) % Load data.
> dim(da)
% Obtain the size of the data set.
[1] 9845
5
> da[1,]
% See the first row of the data
Date
rtn
vwretd
ewretd
sprtrn
1 19700102 0.000686 0.012137 0.03345 0.010211
--- page 41 ---

14
ﬁnancial time series and their characteristics
> sibm=da[,2]*100
% Obtain percentage simple returns of
% IBM stock.
> summaryStats(sibm) % Obtain summary statistics
Sample Quantiles:
min
1Q median
3Q
max
-22.96 -0.8571
0 0.8833 13.16
Sample Moments:
mean
std skewness kurtosis
0.04016 1.693
0.06141
12.92
Number of Observations:
9845
% simple tests
> s1=skewness(sibm) % Compute skewness
> t=s1/sqrt(6/9845) % Perform test of skewness
> t
[1] 2.487851
> pv=2*(1-pnorm(t)) % Calculate p-value.
> pv
[1] 0.01285177
> libm=log(da[,2]+1)*100 % Turn to log-return
> t.test(libm)
% Test expected return being zero.
One-sample t-Test
data:
libm
t = 1.5126, df = 9844, p-value = 0.1304
alternative hypothesis:
mean is not equal to 0
95 percent confidence interval:
-0.007641473
0.059290531
> normalTest(libm,method=’jb’) % Normality test
Test for Normality: Jarque-Bera
Null Hypothesis: data is normally distributed
Test Stat 60921.93
p.value
0.00
Dist. under Null: chi-square with 2 degrees of freedom
Total Observ.: 9845
Remark.
In S-Plus, kurtosis is the regular kurtosis, not excess kurtosis. That
is, S-Plus does not subtract 3 from the sample kurtosis. Also, in many cases R and
S-Plus use the same commands.
□
1.2.2
Distributions of Returns
The most general model for the log returns {rit; i = 1, . . . , N; t = 1, . . . , T } is its
joint distribution function:
Fr(r11, . . . , rN1; r12, . . . , rN2; . . . ; r1T , . . . , rNT ; Y; θ),
(1.14)
--- page 42 ---

distributional properties of returns
15
where Y is a state vector consisting of variables that summarize the environment
in which asset returns are determined and θ is a vector of parameters that uniquely
determines the distribution function Fr(·). The probability distribution Fr(·) governs the stochastic behavior of the returns rit and Y. In many ﬁnancial studies, the
state vector Y is treated as given and the main concern is the conditional distribution of {rit} given Y. Empirical analysis of asset returns is then to estimate the
unknown parameter θ and to draw statistical inference about the behavior of {rit}
given some past log returns.
The model in Eq. (1.14) is too general to be of practical value. However, it
provides a general framework with respect to which an econometric model for
asset returns rit can be put in a proper perspective.
Some ﬁnancial theories such as the capital asset pricing model (CAPM) of
Sharpe (1964) focus on the joint distribution of N returns at a single time index
t (i.e., the distribution of {r1t, . . . , rNt}). Other theories emphasize the dynamic
structure of individual asset returns (i.e., the distribution of {ri1, . . . , riT } for a
given asset i). In this book, we focus on both. In the univariate analysis of Chapters
2–7, our main concern is the joint distribution of {rit}T
t=1 for asset i. To this end,
it is useful to partition the joint distribution as
F(ri1, . . . , riT ; θ) = F(ri1)F(ri2|ri1) · · · F(riT |ri,T −1, . . . , ri1)
= F(ri1)
T
t=2
F(rit|ri,t−1, . . . , ri1),
(1.15)
where, for simplicity, the parameter θ is omitted. This partition highlights the
temporal dependencies of the log return rit. The main issue then is the speciﬁcation
of the conditional distribution F(rit|ri,t−1, ·), in particular, how the conditional
distribution evolves over time. In ﬁnance, different distributional speciﬁcations
lead to different theories. For instance, one version of the random-walk hypothesis
is that the conditional distribution F(rit|ri,t−1, . . . , ri1) is equal to the marginal
distribution F(rit). In this case, returns are temporally independent and, hence, not
predictable.
It is customary to treat asset returns as continuous random variables, especially
for index returns or stock returns calculated at a low frequency, and use their
probability density functions. In this case, using the identity in Eq. (1.9), we can
write the partition in Eq. (1.15) as
f (ri1, . . . , riT ; θ) = f (ri1; θ)
T
t=2
f (rit|ri,t−1, . . . , ri1; θ).
(1.16)
For high-frequency asset returns, discreteness becomes an issue. For example, stock
prices change in multiples of a tick size on the New York Stock Exchange (NYSE).
The tick size was 1
8 of a dollar before July 1997 and was
1
16 of a dollar from July
1997 to January 2001. Therefore, the tick-by-tick return of an individual stock listed
--- page 43 ---

16
ﬁnancial time series and their characteristics
on the NYSE is not continuous. We discuss high-frequency stock price changes
and time durations between price changes later in Chapter 5.
Remark.
On August 28, 2000, the NYSE began a pilot program with 7 stocks
priced in decimals and the American Stock Exchange (AMEX) began a pilot program with 6 stocks and two options classes. The NYSE added 57 stocks and 94
stocks to the program on September 25 and December 4, 2000, respectively. All
NYSE and AMEX stocks started trading in decimals on January 29, 2001.
□
Equation (1.16) suggests that conditional distributions are more relevant than
marginal distributions in studying asset returns. However, the marginal distributions
may still be of some interest. In particular, it is easier to estimate marginal distributions than conditional distributions using past returns. In addition, in some cases,
asset returns have weak empirical serial correlations, and, hence, their marginal
distributions are close to their conditional distributions.
Several statistical distributions have been proposed in the literature for the
marginal distributions of asset returns, including normal distribution, lognormal distribution, stable distribution, and scale mixture of normal distributions. We brieﬂy
discuss these distributions.
Normal Distribution
A traditional assumption made in ﬁnancial study is that the simple returns {Rit|t =
1, . . . , T } are independently and identically distributed as normal with ﬁxed mean
and variance. This assumption makes statistical properties of asset returns tractable.
But it encounters several difﬁculties. First, the lower bound of a simple return is
−1. Yet the normal distribution may assume any value in the real line and, hence,
has no lower bound. Second, if Rit is normally distributed, then the multiperiod
simple return Rit[k] is not normally distributed because it is a product of one-period
returns. Third, the normality assumption is not supported by many empirical asset
returns, which tend to have a positive excess kurtosis.
Lognormal Distribution
Another commonly used assumption is that the log returns rt of an asset are independent and identically distributed (iid) as normal with mean µ and variance σ 2.
The simple returns are then iid lognormal random variables with mean and variance
given by
E(Rt) = exp

µ + σ 2
2

−1,
Var(Rt) = exp(2µ + σ 2)[exp(σ 2) −1].
(1.17)
These two equations are useful in studying asset returns (e.g., in forecasting using
models built for log returns). Alternatively, let m1 and m2 be the mean and variance
of the simple return Rt, which is lognormally distributed. Then the mean and
--- page 44 ---

distributional properties of returns
17
variance of the corresponding log return rt are
E(rt) = ln

m1 + 1

1 + m2/(1 + m1)2

,
Var(rt) = ln

1 +
m2
(1 + m1)2

.
Because the sum of a ﬁnite number of iid normal random variables is normal,
rt[k] is also normally distributed under the normal assumption for {rt}. In addition,
there is no lower bound for rt, and the lower bound for Rt is satisﬁed using
1 + Rt = exp(rt). However, the lognormal assumption is not consistent with all
the properties of historical stock returns. In particular, many stock returns exhibit
a positive excess kurtosis.
Stable Distribution
The stable distributions are a natural generalization of normal in that they are stable under addition, which meets the need of continuously compounded returns rt.
Furthermore, stable distributions are capable of capturing excess kurtosis shown
by historical stock returns. However, nonnormal stable distributions do not have
a ﬁnite variance, which is in conﬂict with most ﬁnance theories. In addition, statistical modeling using nonnormal stable distributions is difﬁcult. An example of
nonnormal stable distributions is the Cauchy distribution, which is symmetric with
respect to its median but has inﬁnite variance.
Scale Mixture of Normal Distributions
Recent studies of stock returns tend to use scale mixture or ﬁnite mixture of normal
distributions. Under the assumption of scale mixture of normal distributions, the log
return rt is normally distributed with mean µ and variance σ 2 [i.e., rt ∼N(µ, σ 2)].
However, σ 2 is a random variable that follows a positive distribution (e.g., σ −2
follows a gamma distribution). An example of ﬁnite mixture of normal distributions is
rt ∼(1 −X)N(µ, σ 2
1 ) + XN(µ, σ 2
2 ),
where X is a Bernoulli random variable such that P (X = 1) = α and P (X = 0) =
1 −α with 0 < α < 1, σ 2
1 is small, and σ 2
2 is relatively large. For instance, with
α = 0.05, the ﬁnite mixture says that 95% of the returns follow N(µ, σ 2
1 ) and 5%
follow N(µ, σ 2
2 ). The large value of σ 2
2 enables the mixture to put more mass at the
tails of its distribution. The low percentage of returns that are from N(µ, σ 2
2 ) says
that the majority of the returns follow a simple normal distribution. Advantages
of mixtures of normal include that they maintain the tractability of normal, have
ﬁnite higher order moments, and can capture the excess kurtosis. Yet it is hard to
estimate the mixture parameters (e.g., the α in the ﬁnite-mixture case).
Figure 1.1 shows the probability density functions of a ﬁnite mixture of normal,
Cauchy, and standard normal random variable. The ﬁnite mixture of normal is
(1 −X)N(0, 1) + X × N(0, 16) with X being Bernoulli such that P (X = 1) =
--- page 45 ---

18
ﬁnancial time series and their characteristics
x
f(x)
−4
−2
0
2
4
0.0
0.1
0.2
0.3
0.4
Normal
Cauchy
Mixture
Figure 1.1
Comparison of ﬁnite mixture, stable, and standard normal density functions.
0.05, and the density function of Cauchy is
f (x) =
1
π(1 + x2),
−∞< x < ∞.
It is seen that the Cauchy distribution has fatter tails than the ﬁnite mixture of
normal, which, in turn, has fatter tails than the standard normal.
1.2.3
Multivariate Returns
Let rt = (r1t, . . . , rNt)′ be the log returns of N assets at time t. The multivariate
analyses of Chapters 8 and 10 are concerned with the joint distribution of {rt}T
t=1.
This joint distribution can be partitioned in the same way as that of Eq. (1.15).
The analysis is then focused on the speciﬁcation of the conditional distribution
function F(rt|rt−1, . . . , r1, θ). In particular, how the conditional expectation and
conditional covariance matrix of rt evolve over time constitute the main subjects
of Chapters 8 and 10.
The mean vector and covariance matrix of a random vector X = (X1, . . . , Xp)
are deﬁned as
E(X) = µx = [E(X1), . . . , E(Xp)]′,
Cov(X) = x = E[(X −µx)(X −µx)′],
--- page 46 ---

distributional properties of returns
19
provided that the expectations involved exist. When the data {x1, . . . , xT } of X
are available, the sample mean and covariance matrix are deﬁned as
µx = 1
T
T

t=1
xt,
x =
1
T −1
T

t=1
(xt −µx)(xt −µx)′.
These sample statistics are consistent estimates of their theoretical counterparts provided that the covariance matrix of X exists. In the ﬁnance literature, multivariate
normal distribution is often used for the log return rt.
1.2.4
Likelihood Function of Returns
The partition of Eq. (1.15) can be used to obtain the likelihood function of the
log returns {r1, . . . , rT } of an asset, where for ease in notation the subscript i is
omitted from the log return. If the conditional distribution f (rt|rt−1, . . . , r1, θ) is
normal with mean µt and variance σ 2
t , then θ consists of the parameters in µt and
σ 2
t , and the likelihood function of the data is
f (r1, . . . , rT ; θ) = f (r1; θ)
T
t=2
1
√
2πσt
exp

−(rt −µt)2
2σ 2
t

,
(1.18)
where f (r1; θ) is the marginal density function of the ﬁrst observation r1. The value
of θ that maximizes this likelihood function is the maximum-likelihood estimate
(MLE) of θ. Since the log function is monotone, the MLE can be obtained by
maximizing the log-likelihood function,
ln f (r1, . . . , rT ; θ) = ln f (r1; θ) −1
2
T

t=2

ln(2π) + ln(σ 2
t ) + (rt −µt)2
σ 2
t

,
which is easier to handle in practice. The log-likelihood function of the data can
be obtained in a similar manner if the conditional distribution f (rt|rt−1, . . . , r1; θ)
is not normal.
1.2.5
Empirical Properties of Returns
The data used in this section are obtained from the Center for Research in Security Prices (CRSP) of the University of Chicago. Dividend payments, if any, are
included in the returns. Figure 1.2 shows the time plots of monthly simple returns
and log returns of IBM stock from January 1926 to December 2008. A time plot
shows the data against the time index. The upper plot is for the simple returns.
Figure 1.3 shows the same plots for the monthly returns of value-weighted market
index. As expected, the plots show that the basic patterns of simple and log returns
are similar.
--- page 47 ---

20
ﬁnancial time series and their characteristics
Year
Simple return
1940
1960
1980
2000
−0.2 0.0
0.2
0.4
Year
Log return
1940
1960
1980
2000
−0.2
0.0
0.2
0.4
Figure 1.2
Time plots of monthly returns of IBM stock from January 1926 to December 2008. Upper
panel is for simple returns, and lower panel is for log returns.
Year
Simple return
1940
1960
1980
2000
−0.2
0.0
0.2
0.4
Year
Log return
1940
1960
1980
2000
−0.2
0.0
0.2
Figure 1.3
Time plots of monthly returns of value-weighted index from January 1926 to December
2008. Upper panel is for simple returns, and lower panel is for log returns.
--- page 48 ---

distributional properties of returns
21
Table 1.2 provides some descriptive statistics of simple and log returns for
selected U.S. market indexes and individual stocks. The returns are for daily and
monthly sample intervals and are in percentages. The data spans and sample sizes
are also given in Table 1.2. From the table, we make the following observations.
(a) Daily returns of the market indexes and individual stocks tend to have high
excess kurtoses. For monthly series, the returns of market indexes have higher
excess kurtoses than individual stocks. (b) The mean of a daily return series is close
to zero, whereas that of a monthly return series is slightly larger. (c) Monthly returns
have higher standard deviations than daily returns. (d) Among the daily returns,
market indexes have smaller standard deviations than individual stocks. This is in
agreement with common sense. (e) The skewness is not a serious problem for both
daily and monthly returns. (f) The descriptive statistics show that the difference
between simple and log returns is not substantial.
Figure 1.4 shows the empirical density functions of monthly simple and log
returns of IBM stock from 1926 to 2008. Also shown, by a dashed line, in each
graph is the normal probability density function evaluated by using the sample
mean and standard deviation of IBM returns given in Table 1.2. The plots indicate
that the normality assumption is questionable for monthly IBM stock returns. The
empirical density function has a higher peak around its mean, but fatter tails than
that of the corresponding normal distribution. In other words, the empirical density
Simple return
−0.4
−0.2
0.0
0.2
0.4
0.6
Log return
Density
−0.4
−0.2
0.0
0.2
0.4
0
1
3
4
5
2
Density
0
1
3
4
5
2
6
Figure 1.4
Comparison of empirical and normal densities for monthly simple and log returns of IBM
stock. Sample period is from January 1926 to December 2008. Left plot is for simple returns and right
plot for log returns. Normal density, shown by the dashed line, uses sample mean and standard deviation
given in Table 1.2.
--- page 49 ---

22
ﬁnancial time series and their characteristics
function is taller and skinnier, but with a wider support than the corresponding
normal density.
1.3
PROCESSES CONSIDERED
Besides the return series, we also consider the volatility process and the behavior of
extreme returns of an asset. The volatility process is concerned with the evolution
of conditional variance of the return over time. This is a topic of interest because, as
shown in Figures 1.2 and 1.3, the variabilities of returns vary over time and appear
in clusters. In application, volatility plays an important role in pricing options and
risk management. By extremes of a return series, we mean the large positive or
negative returns. Table 1.2 shows that the minimum and maximum of a return series
can be substantial. The negative extreme returns are important in risk management,
whereas positive extreme returns are critical to holding a short position. We study
properties and applications of extreme returns, such as the frequency of occurrence,
the size of an extreme, and the impacts of economic variables on the extremes, in
Chapter 7.
Other ﬁnancial time series considered in the book include interest rates, exchange
rates, bond yields, and quarterly earning per share of a company. Figure 1.5 shows
the time plots of two U.S. monthly interest rates. They are the 10-year and 1-year
Year
Rate
1960
1970
1980
1990
2000
2010
10
8
6
4
2
12 14
Rate
0
5
10
15
(a)
Year
1960
1970
1980
1990
2000
2010
(b)
Figure 1.5
Time plots of monthly U.S. interest rates from April 1953 to February 2009: (a) 10-year
Treasury constant maturity rate and (b) 1-year maturity rate.
--- page 50 ---

processes considered
23
Year
Yens
2000
2002
2004
2006
2008
90 100 110 120 130
Change
−4
−2
0
2
(a)
Year
2000
2002
2004
2006
2008
(b)
Figure 1.6
Time plot of daily exchange rate between U.S. dollar and Japanese yen from January 4,
2000, to March 27, 2009: (a) exchange rate and (b) changes in exchange rate.
Treasury constant maturity rates from April 1954 to February 2009. As expected,
the two interest rates moved in unison, but the 1-year rates appear to be more
volatile. Figure 1.6 shows the daily exchange rate between the U.S. dollar and the
Japanese yen from January 4, 2000, to March 27, 2009. From the plot, the exchange
rate encountered occasional big changes in the sampling period. Table 1.3 provides
some descriptive statistics for selected U.S. ﬁnancial time series. The monthly bond
returns obtained from CRSP are Fama bond portfolio returns from January 1952 to
December 2008. The interest rates are obtained from the Federal Reserve Bank of
St. Louis. The weekly 3-month Treasury bill rate started on January 8, 1954, and
the 6-month rate started on December 12, 1958. Both series ended on March 27,
2009. For the interest rate series, the sample means are proportional to the time to
maturity, but the sample standard deviations are inversely proportional to the time
to maturity. For the bond returns, the sample standard deviations are positively
related to the time to maturity, whereas the sample means remain stable for all
maturities. Most of the series considered have positive excess kurtoses.
With respect to the empirical characteristics of returns shown in Table 1.2,
Chapters 2–4 focus on the ﬁrst four moments of a return series and Chapter 7 on
the behavior of minimum and maximum returns. Chapters 8 and 10 are concerned
with moments of and the relationships between multiple asset returns, and Chapter 5
addresses properties of asset returns when the time interval is small. An introduction
to mathematical ﬁnance is given in Chapter 6.
--- page 51 ---

24
ﬁnancial time series and their characteristics
TABLE 1.3
Descriptive Statistics of Selected U.S. Financial Time Seriesa
Standard
Excess
Maturity
Mean
Deviation
Skewness
Kurtosis
Minimum
Maximum
Monthly Bond Returns: Jan. 1952 to Dec. 2008, T = 684
1–12 months
0.45
0.35
2.47
13.14
−0.40
3.52
12–24 months
0.49
0.67
1.88
15.44
−2.94
6.85
24–36 months
0.52
0.98
1.37
12.92
−4.90
9.33
48–60 months
0.53
1.40
0.60
4.83
−5.78
10.06
61–120 months
0.55
1.69
0.65
4.79
−7.35
10.92
Monthly Treasury Rates: April 1953 to February 2009, T = 671
1 year
5.59
2.98
1.02
1.32
0.44
16.72
3 years
5.98
2.85
0.95
0.95
1.07
16.22
5 years
6.19
2.77
0.97
0.82
1.52
15.93
10 years
6.40
2.69
0.95
0.61
2.29
15.32
Weekly Treasury Bill Rates: End on March 27, 2009.
3 months
5.07
2.82
1.08
1.80
0.02
16.76
6 months
5.52
2.73
0.99
1.53
0.20
15.76
aThe data are in percentages. The weekly 3-month Treasury bill rate started from January 8, 1954, and
the 6-month rate started from December 12, 1958. The sample sizes for Treasury bill rates are 2882
and 2625, respectively. Data sources are given in the text.
APPENDIX: R PACKAGES
R is a free software available from http://www.r-project.org. One can click CRAN
on its Web page to select a nearby CRAN Mirror to download and install the
software and selected packages. For ﬁnancial time series analysis, the Rmetrics of
Diethelm Wuertz and his associates have produced many useful packages, including
fBasics, timeSeries, fGarch, etc. We use many functions of these packages in
this book. Further information concerning installing R and the commands used can
be found either on the Web page of this book or on the author’s teaching Web page.
R and S-Plus are objective-oriented software. They enable users to create many
objects. For instance, one can use the command ts to create a time series object.
Treating time series data as a time series object in R has some advantages, but
it requires some learning to get used to it. It is, however, not necessary to create
a time series object in R to perform the analyses discussed in this book. As an
illustration, consider the monthly simple returns to the General Motors stock from
January 1975 to December 2008; see Exercise 1.2. The data have 408 observations.
The following R commands are used to illustrate the points:
> da=read.table("m-gm3dx7508.txt",header=T)
% Load data
> gm=da[,2]
% Column 2 contains GM stock returns
> gm1=ts(gm,frequency=12,start=c(1975,1))
% Creates a ts object.
> par(mfcol=c(2,1))
% Put two plots on a page.
--- page 52 ---

exercises
25
Index
(a)
(b)
gm
0
100
200
300
400
−0.4 −0.2
0.0
0.2
Time
gm1
1980
1990
2000
2010
−0.4 −0.2
0.0
0.2
Figure 1.7
Time plots of monthly simple returns to General Motors stock from January 1975 to
December 2008: (a) and (b) are without and with time series object, respectively.
> plot(gm,type=’l’)
> plot(gm1,type=’l’)
> acf(gm,lag=24)
> acf(gm1,lag=24)
In the ts command, frequency = 12 says that the time unit is year and there
are 12 equally spaced observations in each time unit, and start = c(1975,1) means
the starting time is January 1975. Frequency and start are the two basic arguments
needed in R to create a time series object. For further details, please use help(ts)
in R to obtain details of the command. Here gm1 is a time series object in R, but
gm is not. Figures 1.7 and 1.8 show, respectively, the time plot and autocorrelation
function (ACF) of the returns of GM stock. In each ﬁgure, the upper plot is produced without using time series object, whereas the lower plot is produced by a
time series object. The upper and lower plots are identical except for the horizontal
label. For the time plot, the time series object uses calendar time to label the x
axis, which is preferred. On the other hand, for the ACF plot, the time series object
uses fractions of time unit in the label, not the commonly used time lags.
EXERCISES
1.1. Consider the daily stock returns of American Express (AXP), Caterpillar
(CAT), and Starbucks (SBUX) from January 1999 to December 2008. The
--- page 53 ---

26
ﬁnancial time series and their characteristics
Lag
(a)
ACF
0
5
10
15
20
0.0
0.4
0.8
Lag
(b)
ACF
0.0
0.5
1.0
1.5
2.0
0.0
0.4
0.8
Series : gm 1
Series : gm
Figure 1.8
Sample ACFs of the monthly simple returns to General Motors stock from January 1975
to December 2008: (a) and (b) are without and with time series object, respectively.
data are simple returns given in the ﬁle d-3stocks9908.txt (date, axp, cat,
sbux).
(a) Express the simple returns in percentages. Compute the sample mean,
standard deviation, skewness, excess kurtosis, minimum, and maximum
of the percentage simple returns.
(b) Transform the simple returns to log returns.
(c) Express the log returns in percentages. Compute the sample mean, standard deviation, skewness, excess kurtosis, minimum, and maximum of the
percentage log returns.
(d) Test the null hypothesis that the mean of the log returns of each stock is
zero. That is, perform three separate tests. Use 5% signiﬁcance level to
draw your conclusion.
1.2. Answer the same questions as in Exercise 1.1 but using monthly stock returns
for General Motors (GM), CRSP value-weighted index (VW), CRSP equalweighted index (EW), and S&P composite index from January 1975 to December 2008. The returns of the indexes include dividend distributions. Data ﬁle
is m-gm3dx7508.txt (date, gm, vw, ew, sp).
1.3. Consider the monthly stock returns of S&P composite index from January
1975 to December 2008 in Exercise 1.2. Answer the following questions:
(a) What is the average annual log return over the data span?
--- page 54 ---

references
27
(b) Assume that there were no transaction costs. If one invested $1.00 on the
S&P composite index at the beginning of 1975, what was the value of the
investment at the end of 2008?
1.4. Consider the daily log returns of American Express stock from January 1999
to December 2008 as in Exercise 1.1. Use the 5% signiﬁcance level to perform
the following tests: (a) Test the null hypothesis that the skewness measure of
the returns is zero. (b) Test the null hypothesis that the excess kurtosis of the
returns is zero.
1.5. Daily foreign exchange rates (spot rates) can be obtained from the Federal
Reserve Bank in Chicago. The data are the noon buying rates in New York City
certiﬁed by the Federal Reserve Bank of New York. Consider the exchange
rates between the U.S. dollar and the Canadian dollar, euro, U.K. pound, and
the Japanese yen from January 4, 2000, to March 27, 2009. The data are
also on the Web. (a) Compute the daily log return of each exchange rate.
(b) Compute the sample mean, standard deviation, skewness, excess kurtosis,
minimum, and maximum of the log returns of each exchange rate. (c) Discuss
the empirical characteristics of the log returns of exchange rates. (d) Obtain a
density plot of the daily long returns of dollar–euro exchange rate.
REFERENCES
Campbell, J. Y., Lo, A. W., and MacKinlay, A. C. (1997). The Econometrics of Financial
Markets. Princeton University Press, Princeton, NJ.
Jarque, C. M. and Bera, A. K. (1987). A test of normality of observations and regression
residuals. International Statistical Review 55: 163–172.
Sharpe, W. (1964). Capital asset prices: A theory of market equilibrium under conditions of
risk. Journal of Finance 19: 425–442.
Snedecor, G. W. and Cochran, W. G. (1980). Statistical Methods, 7th ed. Iowa State University Press, Ames, IA.
--- page 55 ---
--- page 56 ---

C H A P T E R
2
Linear Time Series Analysis
and Its Applications
In this chapter, we discuss basic theories of linear time series analysis, introduce
some simple econometric models useful for analyzing ﬁnancial data, and apply the
models to ﬁnancial time series such as asset returns. Discussions of the concepts are
brief with emphasis on those relevant to ﬁnancial applications. Understanding the
simple time series models introduced here will go a long way to better appreciate
the more sophisticated ﬁnancial econometric models of the later chapters. There
are many time series textbooks available. For basic concepts of linear time series
analysis, see Box, Jenkins, and Reinsel (1994, Chapters 2 and 3) and Brockwell
and Davis (1996, Chapters 1–3).
Treating an asset return (e.g., log return rt of a stock) as a collection of random
variables over time, we have a time series {rt}. Linear time series analysis provides
a natural framework to study the dynamic structure of such a series. The theories
of linear time series discussed include stationarity, dynamic dependence, autocorrelation function, modeling, and forecasting. The econometric models introduced
include (a) simple autoregressive (AR) models, (b) simple moving-average (MA)
models, (b) mixed autoregressive moving-average (ARMA) models, (c) seasonal
models, (d) unit-root nonstationarity, (e) regression models with time series errors,
and (f) fractionally differenced models for long-range dependence. For an asset
return rt, simple models attempt to capture the linear relationship between rt and
information available prior to time t. The information may contain the historical
values of rt and the random vector Y in Eq. (1.14), which describes the economic environment under which the asset price is determined. As such, correlation
plays an important role in understanding these models. In particular, correlations
between the variable of interest and its past values become the focus of linear
time series analysis. These correlations are referred to as serial correlations or
autocorrelations. They are the basic tool for studying a stationary time series.
Analysis of Financial Time Series, Third Edition, By Ruey S. Tsay
Copyright 2010 John Wiley & Sons, Inc.
29
--- page 57 ---

30
linear time series analysis and its applications
2.1
STATIONARITY
The foundation of time series analysis is stationarity. A time series {rt} is said to
be strictly stationary if the joint distribution of (rt1, . . . , rtk) is identical to that of
(rt1+t, . . . , rtk+t) for all t, where k is an arbitrary positive integer and (t1, . . . , tk) is
a collection of k positive integers. In other words, strict stationarity requires that the
joint distribution of (rt1, . . . , rtk) is invariant under time shift. This is a very strong
condition that is hard to verify empirically. A weaker version of stationarity is often
assumed. A time series {rt} is weakly stationary if both the mean of rt and the
covariance between rt and rt−ℓare time invariant, where ℓis an arbitrary integer.
More speciﬁcally, {rt} is weakly stationary if (a) E(rt) = µ, which is a constant,
and (b) Cov(rt, rt−ℓ) = γℓ, which only depends on ℓ. In practice, suppose that we
have observed T data points {rt|t = 1, . . . , T }. The weak stationarity implies that
the time plot of the data would show that the T values ﬂuctuate with constant
variation around a ﬁxed level. In applications, weak stationarity enables one to
make inference concerning future observations (e.g., prediction).
Implicitly, in the condition of weak stationarity, we assume that the ﬁrst two
moments of rt are ﬁnite. From the deﬁnitions, if rt is strictly stationary and its
ﬁrst two moments are ﬁnite, then rt is also weakly stationary. The converse is
not true in general. However, if the time series rt is normally distributed, then
weak stationarity is equivalent to strict stationarity. In this book, we are mainly
concerned with weakly stationary series.
The covariance γℓ= Cov(rt, rt−ℓ) is called the lag-ℓautocovariance of rt. It has
two important properties: (a) γ0 = Var(rt) and (b) γ−ℓ= γℓ. The second property
holds because Cov(rt, rt−(−ℓ)) = Cov(rt−(−ℓ), rt) = Cov(rt+ℓ, rt) = Cov(rt1, rt1−ℓ),
where t1 = t + ℓ.
In the ﬁnance literature, it is common to assume that an asset return series is
weakly stationary. This assumption can be checked empirically provided that a
sufﬁcient number of historical returns are available. For example, one can divide
the data into subsamples and check the consistency of the results obtained across
the subsamples.
2.2
CORRELATION AND AUTOCORRELATION FUNCTION
The correlation coefﬁcient between two random variables X and Y is deﬁned as
ρx,y =
Cov(X, Y)
√Var(X)Var(Y) =
E[(X −µx)(Y −µy)]

E(X −µx)2E(Y −µy)2 ,
where µx and µy are the mean of X and Y, respectively, and it is assumed that the
variances exist. This coefﬁcient measures the strength of linear dependence between
X and Y, and it can be shown that −1 ≤ρx,y ≤1 and ρx,y = ρy,x. The two random
variables are uncorrelated if ρx,y = 0. In addition, if both X and Y are normal
random variables, then ρx,y = 0 if and only if X and Y are independent. When the
--- page 58 ---

correlation and autocorrelation function
31
sample {(xt, yt)}T
t=1 is available, the correlation can be consistently estimated by
its sample counterpart
ˆρx,y =
T
t=1(xt −¯x)(yt −¯y)
T
t=1(xt −¯x)2 T
t=1(yt −¯y)2
,
where ¯x = T
t=1 xt/T and ¯y = T
t=1 yt/T are the sample mean of X and Y,
respectively.
Autocorrelation Function (ACF)
Consider a weakly stationary return series rt. When the linear dependence between
rt and its past values rt−i is of interest, the concept of correlation is generalized
to autocorrelation. The correlation coefﬁcient between rt and rt−ℓis called the
lag-ℓautocorrelation of rt and is commonly denoted by ρℓ, which under the weak
stationarity assumption is a function of ℓonly. Speciﬁcally, we deﬁne
ρℓ=
Cov(rt, rt−ℓ)

Var(rt)Var(rt−ℓ)
= Cov(rt, rt−ℓ)
Var(rt)
= γℓ
γ0
,
(2.1)
where the property Var(rt) = Var(rt−ℓ) for a weakly stationary series is used. From
the deﬁnition, we have ρ0 = 1, ρℓ= ρ−ℓ, and −1 ≤ρℓ≤1. In addition, a weakly
stationary series rt is not serially correlated if and only if ρℓ= 0 for all ℓ> 0.
For a given sample of returns {rt}T
t=1, let ¯r be the sample mean (i.e., ¯r =
T
t=1 rt/T ). Then the lag-1 sample autocorrelation of rt is
ˆρ1 =
T
t=2(rt −¯r)(rt−1 −¯r)
T
t=1(rt −¯r)2
.
Under some general conditions, ˆρ1 is a consistent estimate of ρ1. For example, if
{rt} is an independent and identically distributed (iid) sequence and E(r2
t ) < ∞,
then ˆρ1 is asymptotically normal with mean zero and variance 1/T ; see Brockwell
and Davis (1991, Theorem 7.2.2). This result can be used in practice to test the
null hypothesis H0 : ρ1 = 0 versus the alternative hypothesis Ha : ρ1̸ = 0. The test
statistic is the usual t ratio, which is
√
T ˆρ1 and follows asymptotically the standard
normal distribution. The null hypothesis H0 is rejected if the t ratio is large in
magnitude or, equivalently, the p value of the t ratio is small, say less than 0.05.
In general, the lag-ℓsample autocorrelation of rt is deﬁned as
ˆρℓ=
T
t=ℓ+1(rt −¯r)(rt−ℓ−¯r)
T
t=1(rt −¯r)2
,
0 ≤ℓ< T −1.
(2.2)
If {rt} is an iid sequence satisfying E(r2
t ) < ∞, then ˆρℓis asymptotically normal
with mean zero and variance 1/T for any ﬁxed positive integer ℓ. More generally,
if rt is a weakly stationary time series satisfying rt = µ + q
i=0 ψiat−i, where
