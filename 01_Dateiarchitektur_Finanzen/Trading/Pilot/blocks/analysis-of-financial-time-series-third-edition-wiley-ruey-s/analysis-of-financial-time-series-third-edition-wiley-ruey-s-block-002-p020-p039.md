# Analysis of Financial Time Series, Third Edition (Wiley -- Ruey S_ Tsay -- Wiley series in probability and statistics, 3rd ed_, -- John Wiley & Sons, -- isbn13 9780470414354 -- 9f99b80c7b2dedd477f463dc5323f3b6 -- An.pdf — pages 20–39

--- page 20 ---

Preface
As many countries struggle to recover from the recent global ﬁnancial crisis, one
thing clear is that we do not want to suffer another crisis like this in the future.
We must study the past in order to prevent future ﬁnancial crisis. Financial data
of the past few years thus become important in empirical study. The primary
objective of the revision is to update the data used and to reanalyze the examples
so that one can better understand the properties of asset returns. At the same time,
we also witness many new developments in ﬁnancial econometrics and ﬁnancial
software packages. In particular, the Rmetrics now has many packages for analyzing
ﬁnancial time series. The second goal of the revision is to include R commands and
demonstrations, making it possible and easier for readers to reproduce the results
shown in the book.
Collapses of big ﬁnancial institutions during the crisis show that extreme events
occur in clusters; they are not independent. To deal with dependence in extremes,
I include the extremal index in Chapter 7 and discuss its impact on value at risk.
I also rewrite Chapter 7 to make it easier to understand and more complete. It
now contains the expected shortfall, or conditional value at risk, for measuring
ﬁnanical risk.
Substantial efforts are made to draw a balance between the length and coverage of the book. I do not include credit risk or operational risk in this revision
for three reasons. First, effective methods for assessing credit risk require further
study. Second, the data are not widely available. Third, the length of the book is
approaching my limit.
A brief summary of the added material in the third edition is:
1. To update the data used throughout the book.
2. To provide R commands and demonstrations. In some cases, R programs are
given.
3. To reanalyze many examples with updated observations.
4. To introduce skew distributions for volatility modeling in Chapter 3.
5. To investigate properties of recent high-frequency trading data and to add
applications of nonlinear duration models in Chapter 5.
xvii
--- page 21 ---

xviii
preface
6. To provide a uniﬁed approach to value at risk (VaR) via loss function, to
discuss expected shortfall (ES), or equivalently the conditional value at risk
(CVaR), and to introduce extremal index for dependence data in Chapter 7.
7. To discuss application of cointegration to pairs trading in Chapter 8.
8. To study applications of dynamic correlation models in Chapter 10.
I beneﬁt greatly from constructive comments of many readers of the second
edition, including students, colleagues, and friends. I am indebted to them all. In
particular, I like to express my sincere thanks to Spencer Graves for creating the
FinTS package for R and Tom Doan of ESTIMA and Eugene Gath for careful
reading of the text. I also thank Kam Hamidieh for suggestions concerning new
topics for the revision. I also like to thank colleagues at Wiley, especially Jackie
Palmieri and Stephen Quigley, for their support. As always, the revision would not
be possible without the constant encouragement and unconditional love of my wife
and children. They are my motivation and source of energy. Part of my research
is supported by the Booth School of Business, University of Chicago.
Finally, the website for the book is:
http://faculty.chicagobooth.edu/ruey.tsay/teaching/fts3.
Ruey S. Tsay
Booth School of Business, University of Chicago
Chicago, Illinois
--- page 22 ---

Preface to the Second Edition
The subject of ﬁnancial time series analysis has attracted substantial attention in
recent years, especially with the 2003 Nobel awards to Professors Robert Engle and
Clive Granger. At the same time, the ﬁeld of ﬁnancial econometrics has undergone
various new developments, especially in high-frequency ﬁnance, stochastic volatility, and software availability. There is a need to make the material more complete
and accessible for advanced undergraduate and graduate students, practitioners, and
researchers. The main goals in preparing this second edition have been to bring the
book up to date both in new developments and empirical analysis, and to enlarge
the core material of the book by including consistent covariance estimation under
heteroscedasticity and serial correlation, alternative approaches to volatility modeling, ﬁnancial factor models, state-space models, Kalman ﬁltering, and estimation
of stochastic diffusion models.
The book therefore has been extended to 12 chapters and substantially revised
to include S-Plus commands and illustrations. Many empirical demonstrations and
exercises are updated so that they include the most recent data.
The two new chapters are Chapter 9, Principal Component Analysis and Factor
Models, and Chapter 11, State-Space Models and Kalman Filter. The factor models discussed include macroeconomic, fundamental, and statistical factor models.
They are simple and powerful tools for analyzing high-dimensional ﬁnancial data
such as portfolio returns. Empirical examples are used to demonstrate the applications. The state-space model and Kalman ﬁlter are added to demonstrate their
applicability in ﬁnance and ease in computation. They are used in Chapter 12 to
estimate stochastic volatility models under the general Markov chain Monte Carlo
(MCMC) framework. The estimation also uses the technique of forward ﬁltering
and backward sampling to gain computational efﬁciency.
A brief summary of the added material in the second edition is:
1. To update the data used throughout the book.
2. To provide S-Plus commands and demonstrations.
xix
--- page 23 ---

xx
preface to the second edition
3. To consider unit-root tests and methods for consistent estimation of the
covariance matrix in the presence of conditional heteroscedasticity and serial
correlation in Chapter 2.
4. To describe alternative approaches to volatility modeling, including use of
high-frequency transactions data and daily high and low prices of an asset in
Chapter 3.
5. To give more applications of nonlinear models and methods in Chapter 4.
6. To introduce additional concepts and applications of value at risk in
Chapter 7.
7. To discuss cointegrated vector AR models in Chapter 8.
8. To cover various multivariate volatility models in Chapter 10.
9. To add an effective MCMC method for estimating stochastic volatility models
in Chapter 12.
The revision beneﬁts greatly from constructive comments of colleagues, friends,
and many readers of the ﬁrst edition. I am indebted to them all. In particular, I
thank J. C. Artigas, Spencer Graves, Chung-Ming Kuan, Henry Lin, Daniel Pe˜na,
Jeff Russell, Michael Steele, George Tiao, Mark Wohar, Eric Zivot, and students
of my MBA classes on ﬁnancial time series for their comments and discussions
and Rosalyn Farkas for editorial assistance. I also thank my wife and children for
their unconditional support and encouragements. Part of my research in ﬁnancial
econometrics is supported by the National Science Foundation, the High-Frequency
Finance Project of the Institute of Economics, Academia Sinica, and the Graduate
School of Business, University of Chicago.
Finally, the website for the book is:
gsbwww.uchicago.edu/fac/ruey.tsay/teaching/fts2.
Ruey S. Tsay
University of Chicago
Chicago, Illinois
--- page 24 ---

Preface to the First Edition
This book grew out of an MBA course in analysis of ﬁnancial time series that I have
been teaching at the University of Chicago since 1999. It also covers materials of
Ph.D. courses in time series analysis that I taught over the years. It is an introductory
book intended to provide a comprehensive and systematic account of ﬁnancial
econometric models and their application to modeling and prediction of ﬁnancial
time series data. The goals are to learn basic characteristics of ﬁnancial data,
understand the application of ﬁnancial econometric models, and gain experience in
analyzing ﬁnancial time series.
The book will be useful as a text of time series analysis for MBA students with
ﬁnance concentration or senior undergraduate and graduate students in business,
economics, mathematics, and statistics who are interested in ﬁnancial econometrics.
The book is also a useful reference for researchers and practitioners in business,
ﬁnance, and insurance facing value at risk calculation, volatility modeling, and
analysis of serially correlated data.
The distinctive features of this book include the combination of recent developments in ﬁnancial econometrics in the econometric and statistical literature. The
developments discussed include the timely topics of value at risk (VaR), highfrequency data analysis, and Markov chain Monte Carlo (MCMC) methods. In
particular, the book covers some recent results that are yet to appear in academic
journals; see Chapter 6 on derivative pricing using jump diffusion with closed-form
formulas, Chapter 7 on value at risk calculation using extreme value theory based on
a nonhomogeneous two-dimensional Poisson process, and Chapter 9 on multivariate
volatility models with time-varying correlations. MCMC methods are introduced
because they are powerful and widely applicable in ﬁnancial econometrics. These
methods will be used extensively in the future.
Another distinctive feature of this book is the emphasis on real examples and
data analysis. Real ﬁnancial data are used throughout the book to demonstrate
applications of the models and methods discussed. The analysis is carried out by
using several computer packages; the SCA (the Scientiﬁc Computing Associates)
for building linear time series models, the RATS (regression analysis for time series)
xxi
--- page 25 ---

xxii
preface to the ﬁrst edition
for estimating volatility models, and the S-Plus for implementing neural networks
and obtaining postscript plots. Some commands required to run these packages
are given in appendixes of appropriate chapters. In particular, complicated RATS
programs used to estimate multivariate volatility models are shown in Appendix
A of Chapter 9. Some Fortran programs written by myself and others are used
to price simple options, estimate extreme value models, calculate VaR, and carry
out Bayesian analysis. Some data sets and programs are accessible from the World
Wide Web at http://www.gsb.uchicago.edu/fac/ruey.tsay/teaching/fts.
The book begins with some basic characteristics of ﬁnancial time series data in
Chapter 1. The other chapters are divided into three parts. The ﬁrst part, consisting
of Chapters 2 to 7, focuses on analysis and application of univariate ﬁnancial time
series. The second part of the book covers Chapters 8 and 9 and is concerned with
the return series of multiple assets. The ﬁnal part of the book is Chapter 10, which
introduces Bayesian inference in ﬁnance via MCMC methods.
A knowledge of basic statistical concepts is needed to fully understand the book.
Throughout the chapters, I have provided a brief review of the necessary statistical
concepts when they ﬁrst appear. Even so, a prerequisite in statistics or business
statistics that includes probability distributions and linear regression analysis is
highly recommended. A knowledge of ﬁnance will be helpful in understanding the
applications discussed throughout the book. However, readers with advanced background in econometrics and statistics can ﬁnd interesting and challenging topics in
many areas of the book.
An MBA course may consist of Chapters 2 and 3 as a core component, followed
by some nonlinear methods (e.g., the neural network of Chapter 4 and the applications discussed in Chapters 5–7 and 10). Readers who are interested in Bayesian
inference may start with the ﬁrst ﬁve sections of Chapter 10.
Research in ﬁnancial time series evolves rapidly and new results continue to
appear regularly. Although I have attempted to provide broad coverage, there are
many subjects that I do not cover or can only mention in passing.
I sincerely thank my teacher and dear friend, George C. Tiao, for his guidance, encouragement, and deep conviction regarding statistical applications over the
years. I am grateful to Steve Quigley, Heather Haselkorn, Leslie Galen, Danielle
LaCouriere, and Amy Hendrickson for making the publication of this book possible, to Richard Smith for sending me the estimation program of extreme value
theory, to Bonnie K. Ray for helpful comments on several chapters, to Steve Kou
for sending me his preprint on jump diffusion models, to Robert E. McCulloch for
many years of collaboration on MCMC methods, to many students in my courses
on analysis of ﬁnancial time series for their feedback and inputs, and to Jeffrey
Russell and Michael Zhang for insightful discussions concerning analysis of highfrequency ﬁnancial data. To all these wonderful people I owe a deep sense of
gratitude. I am also grateful for the support of the Graduate School of Business,
University of Chicago and the National Science Foundation. Finally, my heartfelt
--- page 26 ---

preface to the ﬁrst edition
xxiii
thanks to my wife, Teresa, for her continuous support, encouragement, and understanding; to Julie, Richard, and Vicki for bringing me joy and inspirations; and to
my parents for their love and care.
R. S. T.
Chicago, Illinois
--- page 27 ---
--- page 28 ---

C H A P T E R
1
Financial Time Series
and Their Characteristics
Financial time series analysis is concerned with the theory and practice of asset
valuation over time. It is a highly empirical discipline, but like other scientiﬁc
ﬁelds theory forms the foundation for making inference. There is, however, a
key feature that distinguishes ﬁnancial time series analysis from other time series
analysis. Both ﬁnancial theory and its empirical time series contain an element of
uncertainty. For example, there are various deﬁnitions of asset volatility, and for a
stock return series, the volatility is not directly observable. As a result of the added
uncertainty, statistical theory and methods play an important role in ﬁnancial time
series analysis.
The objective of this book is to provide some knowledge of ﬁnancial time
series, introduce some statistical tools useful for analyzing these series, and gain
experience in ﬁnancial applications of various econometric methods. We begin
with the basic concepts of asset returns and a brief introduction to the processes
to be discussed throughout the book. Chapter 2 reviews basic concepts of linear
time series analysis such as stationarity and autocorrelation function, introduces
simple linear models for handling serial dependence of the series, and discusses
regression models with time series errors, seasonality, unit-root nonstationarity, and
long-memory processes. The chapter also provides methods for consistent estimation of the covariance matrix in the presence of conditional heteroscedasticity and
serial correlations. Chapter 3 focuses on modeling conditional heteroscedasticity
(i.e., the conditional variance of an asset return). It discusses various econometric
models developed recently to describe the evolution of volatility of an asset return
over time. The chapter also discusses alternative methods to volatility modeling,
including use of high-frequency transactions data and daily high and low prices of
an asset. In Chapter 4, we address nonlinearity in ﬁnancial time series, introduce
test statistics that can discriminate nonlinear series from linear ones, and discuss
several nonlinear models. The chapter also introduces nonparametric estimation
Analysis of Financial Time Series, Third Edition, By Ruey S. Tsay
Copyright 2010 John Wiley & Sons, Inc.
1
--- page 29 ---

2
ﬁnancial time series and their characteristics
methods and neural networks and shows various applications of nonlinear models
in ﬁnance. Chapter 5 is concerned with analysis of high-frequency ﬁnancial data, the
effects of market microstructure, and some applications of high-frequency ﬁnance.
It shows that nonsynchronous trading and bid–ask bounce can introduce serial correlations in a stock return. It also studies the dynamic of time duration between
trades and some econometric models for analyzing transactions data. In Chapter 6,
we introduce continuous-time diffusion models and Ito’s lemma. Black–Scholes
option pricing formulas are derived, and a simple jump diffusion model is used
to capture some characteristics commonly observed in options markets. Chapter 7
discusses extreme value theory, heavy-tailed distributions, and their application to
ﬁnancial risk management. In particular, it discusses various methods for calculating value at risk and expected shortfall of a ﬁnancial position. Chapter 8 focuses
on multivariate time series analysis and simple multivariate models with emphasis on the lead–lag relationship between time series. The chapter also introduces
cointegration, some cointegration tests, and threshold cointegration and applies the
concept of cointegration to investigate arbitrage opportunity in ﬁnancial markets,
including pairs trading. Chapter 9 discusses ways to simplify the dynamic structure of a multivariate series and methods to reduce the dimension. It introduces
and demonstrates three types of factor model to analyze returns of multiple assets.
In Chapter 10, we introduce multivariate volatility models, including those with
time-varying correlations, and discuss methods that can be used to reparameterize
a conditional covariance matrix to satisfy the positiveness constraint and reduce the
complexity in volatility modeling. Chapter 11 introduces state-space models and
the Kalman ﬁlter and discusses the relationship between state-space models and
other econometric models discussed in the book. It also gives several examples
of ﬁnancial applications. Finally, in Chapter 12, we introduce some Markov chain
Monte Carlo (MCMC) methods developed in the statistical literature and apply
these methods to various ﬁnancial research problems, such as the estimation of
stochastic volatility and Markov switching models.
The book places great emphasis on application and empirical data analysis.
Every chapter contains real examples and, in many occasions, empirical characteristics of ﬁnancial time series are used to motivate the development of econometric
models. Computer programs and commands used in data analysis are provided
when needed. In some cases, the programs are given in an appendix. Many real
data sets are also used in the exercises of each chapter.
1.1
ASSET RETURNS
Most ﬁnancial studies involve returns, instead of prices, of assets. Campbell, Lo,
and MacKinlay (1997) give two main reasons for using returns. First, for average
investors, return of an asset is a complete and scale-free summary of the investment
opportunity. Second, return series are easier to handle than price series because
the former have more attractive statistical properties. There are, however, several
deﬁnitions of an asset return.
--- page 30 ---

asset returns
3
Let Pt be the price of an asset at time index t. We discuss some deﬁnitions of
returns that are used throughout the book. Assume for the moment that the asset
pays no dividends.
One-Period Simple Return
Holding the asset for one period from date t −1 to date t would result in a simple
gross return:
1 + Rt =
Pt
Pt−1
or
Pt = Pt−1(1 + Rt).
(1.1)
The corresponding one-period simple net return or simple return is
Rt =
Pt
Pt−1
−1 = Pt −Pt−1
Pt−1
.
(1.2)
Multiperiod Simple Return
Holding the asset for k periods between dates t −k and t gives a k-period simple
gross return:
1 + Rt[k] =
Pt
Pt−k
=
Pt
Pt−1
× Pt−1
Pt−2
× · · · × Pt−k+1
Pt−k
= (1 + Rt)(1 + Rt−1) · · · (1 + Rt−k+1)
=
k−1

j=0
(1 + Rt−j).
Thus, the k-period simple gross return is just the product of the k one-period simple
gross returns involved. This is called a compound return. The k-period simple net
return is Rt[k] = (Pt −Pt−k)/Pt−k.
In practice, the actual time interval is important in discussing and comparing
returns (e.g., monthly return or annual return). If the time interval is not given,
then it is implicitly assumed to be one year. If the asset was held for k years, then
the annualized (average) return is deﬁned as
Annualized {Rt[k]} =


k−1

j=0
(1 + Rt−j)


1/k
−1.
This is a geometric mean of the k one-period simple gross returns involved and
can be computed by
Annualized {Rt[k]} = exp

1
k
k−1

j=0
ln(1 + Rt−j)

−1,
--- page 31 ---

4
ﬁnancial time series and their characteristics
where exp(x) denotes the exponential function and ln(x) is the natural logarithm
of the positive number x. Because it is easier to compute arithmetic average than
geometric mean and the one-period returns tend to be small, one can use a ﬁrst-order
Taylor expansion to approximate the annualized return and obtain
Annualized {Rt[k]} ≈1
k
k−1

j=0
Rt−j.
(1.3)
Accuracy of the approximation in Eq. (1.3) may not be sufﬁcient in some applications, however.
Continuous Compounding
Before introducing continuously compounded return, we discuss the effect of compounding. Assume that the interest rate of a bank deposit is 10% per annum and
the initial deposit is $1.00. If the bank pays interest once a year, then the net value
of the deposit becomes $1(1 + 0.1) = $1.1 one year later. If the bank pays interest semiannually, the 6-month interest rate is 10%/2 = 5% and the net value is
$1(1 + 0.1/2)2 = $1.1025 after the ﬁrst year. In general, if the bank pays interest
m times a year, then the interest rate for each payment is 10%/m and the net value
of the deposit becomes $1(1 + 0.1/m)m one year later. Table 1.1 gives the results
for some commonly used time intervals on a deposit of $1.00 with interest rate of
10% per annum. In particular, the net value approaches $1.1052, which is obtained
by exp(0.1) and referred to as the result of continuous compounding. The effect of
compounding is clearly seen.
In general, the net asset value A of continuous compounding is
A = C exp(r × n),
(1.4)
where r is the interest rate per annum, C is the initial capital, and n is the number
of years. From Eq. (1.4), we have
C = A exp(−r × n),
(1.5)
TABLE 1.1
Illustration of Effects of Compounding: Time Interval Is 1 Year and
Interest Rate Is 10% per Annum
Type
Number of Payments
Interest Rate per Period
Net Value
Annual
1
0.1
$1.10000
Semiannual
2
0.05
$1.10250
Quarterly
4
0.025
$1.10381
Monthly
12
0.0083
$1.10471
Weekly
52
0.1/52
$1.10506
Daily
365
0.1/365
$1.10516
Continuously
∞
$1.10517
--- page 32 ---

asset returns
5
which is referred to as the present value of an asset that is worth A dollars n
years from now, assuming that the continuously compounded interest rate is r per
annum.
Continuously Compounded Return
The natural logarithm of the simple gross return of an asset is called the continuously compounded return or log return:
rt = ln(1 + Rt) = ln Pt
Pt−1
= pt −pt−1,
(1.6)
where pt = ln(Pt). Continuously compounded returns rt enjoy some advantages
over the simple net returns Rt. First, consider multiperiod returns. We have
rt[k] = ln(1 + Rt[k]) = ln[(1 + Rt)(1 + Rt−1) · · · (1 + Rt−k+1)]
= ln(1 + Rt) + ln(1 + Rt−1) + · · · + ln(1 + Rt−k+1)
= rt + rt−1 + · · · + rt−k+1.
Thus, the continuously compounded multiperiod return is simply the sum of continuously compounded one-period returns involved. Second, statistical properties
of log returns are more tractable.
Portfolio Return
The simple net return of a portfolio consisting of N assets is a weighted average
of the simple net returns of the assets involved, where the weight on each asset is
the percentage of the portfolio’s value invested in that asset. Let p be a portfolio
that places weight wi on asset i. Then the simple return of p at time t is Rp,t =
N
i=1 wiRit, where Rit is the simple return of asset i.
The continuously compounded returns of a portfolio, however, do not have the
above convenient property. If the simple returns Rit are all small in magnitude, then
we have rp,t ≈N
i=1 wirit, where rp,t is the continuously compounded return of
the portfolio at time t. This approximation is often used to study portfolio returns.
Dividend Payment
If an asset pays dividends periodically, we must modify the deﬁnitions of asset
returns. Let Dt be the dividend payment of an asset between dates t −1 and t and Pt
be the price of the asset at the end of period t. Thus, dividend is not included in Pt.
Then the simple net return and continuously compounded return at time t become
Rt = Pt + Dt
Pt−1
−1,
rt = ln(Pt + Dt) −ln(Pt−1).
Excess Return
Excess return of an asset at time t is the difference between the asset’s return and
the return on some reference asset. The reference asset is often taken to be riskless
--- page 33 ---

6
ﬁnancial time series and their characteristics
such as a short-term U.S. Treasury bill return. The simple excess return and log
excess return of an asset are then deﬁned as
Zt = Rt −R0t,
zt = rt −r0t,
(1.7)
where R0t and r0t are the simple and log returns of the reference asset, respectively.
In the ﬁnance literature, the excess return is thought of as the payoff on an arbitrage
portfolio that goes long in an asset and short in the reference asset with no net
initial investment.
Remark.
A long ﬁnancial position means owning the asset. A short position
involves selling an asset one does not own. This is accomplished by borrowing the
asset from an investor who has purchased it. At some subsequent date, the short
seller is obligated to buy exactly the same number of shares borrowed to pay back
the lender. Because the repayment requires equal shares rather than equal dollars,
the short seller beneﬁts from a decline in the price of the asset. If cash dividends are
paid on the asset while a short position is maintained, these are paid to the buyer
of the short sale. The short seller must also compensate the lender by matching
the cash dividends from his own resources. In other words, the short seller is also
obligated to pay cash dividends on the borrowed asset to the lender.
□
Summary of Relationship
The relationships between simple return Rt and continuously compounded (or log)
return rt are
rt = ln(1 + Rt),
Rt = ert −1.
If the returns Rt and rt are in percentages, then
rt = 100 ln

1 + Rt
100

,
Rt = 100

ert/100 −1

.
Temporal aggregation of the returns produces
1 + Rt[k] = (1 + Rt)(1 + Rt−1) · · · (1 + Rt−k+1),
rt[k] = rt + rt−1 + · · · + rt−k+1.
If the continuously compounded interest rate is r per annum, then the relationship
between present and future values of an asset is
A = C exp(r × n),
C = A exp(−r × n).
Example 1.1.
If the monthly log return of an asset is 4.46%, then the corresponding monthly simple return is 100[exp(4.46/100) −1] = 4.56%. Also, if the
monthly log returns of the asset within a quarter are 4.46%, −7.34%, and 10.77%,
respectively, then the quarterly log return of the asset is (4.46 −7.34 + 10.77)% =
7.89%.
--- page 34 ---

distributional properties of returns
7
1.2
DISTRIBUTIONAL PROPERTIES OF RETURNS
To study asset returns, it is best to begin with their distributional properties.
The objective here is to understand the behavior of the returns across assets
and over time. Consider a collection of N assets held for T time periods, say,
t = 1, . . . , T . For each asset i, let rit be its log return at time t. The log returns
under study are {rit; i = 1, . . . , N; t = 1, . . . , T }. One can also consider the simple returns {Rit; i = 1, . . . , N; t = 1, . . . , T } and the log excess returns {zit; i =
1, . . . , N; t = 1, . . . , T }.
1.2.1
Review of Statistical Distributions and Their Moments
We brieﬂy review some basic properties of statistical distributions and the
moment equations of a random variable. Let Rk be the k-dimensional Euclidean
space. A point in Rk is denoted by x ∈Rk. Consider two random vectors
X = (X1, . . . , Xk)′ and Y = (Y1, . . . , Yq)′. Let P (X ∈A, Y ∈B) be the probability that X is in the subspace A ⊂Rk and Y is in the subspace B ⊂Rq. For
most of the cases considered in this book, both random vectors are assumed to be
continuous.
Joint Distribution
The function
FX,Y (x, y; θ) = P (X ≤x, Y ≤y; θ),
where x ∈Rp, y ∈Rq, and the inequality ≤is a component-by-component operation, is a joint distribution function of X and Y with parameter θ. Behavior of X
and Y is characterized by FX,Y (x, y; θ). If the joint probability density function
fx,y(x, y; θ) of X and Y exists, then
FX,Y (x, y; θ) =
 x
−∞
 y
−∞
fx,y(w, z; θ) dz dw.
In this case, X and Y are continuous random vectors.
Marginal Distribution
The marginal distribution of X is given by
FX(x; θ) = FX,Y (x, ∞, · · · , ∞; θ).
Thus, the marginal distribution of X is obtained by integrating out Y. A similar
deﬁnition applies to the marginal distribution of Y.
If k = 1, X is a scalar random variable and the distribution function becomes
FX(x) = P (X ≤x; θ),
--- page 35 ---

8
ﬁnancial time series and their characteristics
which is known as the cumulative distribution function (CDF) of X. The CDF of a
random variable is nondecreasing [i.e., FX(x1) ≤FX(x2) if x1 ≤x2] and satisﬁes
FX(−∞) = 0 and FX(∞) = 1. For a given probability p, the smallest real number
xp such that p ≤FX(xp) is called the 100pth quantile of the random variable X.
More speciﬁcally,
xp = inf
x {x|p ≤FX(x)}.
We use the CDF to compute the p value of a test statistic in the book.
Conditional Distribution
The conditional distribution of X given Y ≤y is given by
FX|Y≤y(x; θ) = P (X ≤x, Y ≤y; θ)
P (Y ≤y; θ)
.
If the probability density functions involved exist, then the conditional density of
X given Y = y is
fx|y(x; θ) = fx,y(x, y; θ)
fy(y; θ)
,
(1.8)
where the marginal density function fy(y; θ) is obtained by
fy(y; θ) =
 ∞
−∞
fx,y(x, y; θ) dx.
From Eq. (1.8), the relation among joint, marginal, and conditional distributions is
fx,y(x, y; θ) = fx|y(x; θ) × fy(y; θ).
(1.9)
This identity is used extensively in time series analysis (e.g., in maximumlikelihood estimation). Finally, X and Y are independent random vectors if and
only if fx|y(x; θ) = fx(x; θ). In this case, fx,y(x, y; θ) = fx(x; θ)fy(y; θ).
Moments of a Random Variable
The ℓth moment of a continuous random variable X is deﬁned as
m′
ℓ= E(Xℓ) =
 ∞
−∞
xℓf (x) dx,
where E stands for expectation and f (x) is the probability density function of X.
The ﬁrst moment is called the mean or expectation of X. It measures the central
location of the distribution. We denote the mean of X by µx. The ℓth central
moment of X is deﬁned as
mℓ= E[(X −µx)ℓ] =
 ∞
−∞
(x −µx)ℓf (x) dx
--- page 36 ---

distributional properties of returns
9
provided that the integral exists. The second central moment, denoted by σ 2
x , measures the variability of X and is called the variance of X. The positive square root,
σx, of variance is the standard deviation of X. The ﬁrst two moments of a random
variable uniquely determine a normal distribution. For other distributions, higher
order moments are also of interest.
The third central moment measures the symmetry of X with respect to its mean,
whereas the fourth central moment measures the tail behavior of X. In statistics,
skewness and kurtosis, which are normalized third and fourth central moments
of X, are often used to summarize the extent of asymmetry and tail thickness.
Speciﬁcally, the skewness and kurtosis of X are deﬁned as
S(x) = E

(X −µx)3
σ 3x

,
K(x) = E

(X −µx)4
σ 4x

.
The quantity K(x) −3 is called the excess kurtosis because K(x) = 3 for a normal distribution. Thus, the excess kurtosis of a normal random variable is zero.
A distribution with positive excess kurtosis is said to have heavy tails, implying
that the distribution puts more mass on the tails of its support than a normal distribution does. In practice, this means that a random sample from such a distribution
tends to contain more extreme values. Such a distribution is said to be leptokurtic. On the other hand, a distribution with negative excess kurtosis has short tails
(e.g., a uniform distribution over a ﬁnite interval). Such a distribution is said to be
platykurtic.
In application, skewness and kurtosis can be estimated by their sample counterparts. Let {x1, . . . , xT } be a random sample of X with T observations. The sample
mean is
ˆµx = 1
T
T

t=1
xt,
(1.10)
the sample variance is
ˆσ 2
x =
1
T −1
T

t=1
(xt −ˆµx)2,
(1.11)
the sample skewness is
ˆS(x) =
1
(T −1)ˆσ 3x
T

t=1
(xt −ˆµx)3,
(1.12)
and the sample kurtosis is
ˆK(x) =
1
(T −1)ˆσ 4x
T

t=1
(xt −ˆµx)4.
(1.13)
--- page 37 ---

10
ﬁnancial time series and their characteristics
Under the normality assumption, ˆS(x) and
ˆK(x) −3 are distributed asymptotically as normal with zero mean and variances 6/T and 24/T , respectively; see
Snedecor and Cochran (1980, p. 78). These asymptotic properties can be used to
test the normality of asset returns. Given an asset return series {r1, . . . , rT }, to
test the skewness of the returns, we consider the null hypothesis H0 : S(r) = 0
versus the alternative hypothesis Ha : S(r)̸ = 0. The t-ratio statistic of the sample
skewness in Eq. (1.12) is
t =
ˆS(r)
√6/T .
The decision rule is as follows. Reject the null hypothesis at the α signiﬁcance
level, if |t| > Zα/2, where Zα/2 is the upper 100(α/2)th quantile of the standard
normal distribution. Alternatively, one can compute the p value of the test statistic
t and reject H0 if and only if the p value is less than α.
Similarly, one can test the excess kurtosis of the return series using the hypotheses H0 : K(r) −3 = 0 versus Ha : K(r) −3̸ = 0. The test statistic is
t =
ˆK(r) −3
√24/T ,
which is asymptotically a standard normal random variable. The decision rule is to
reject H0 if and only if the p value of the test statistic is less than the signiﬁcance
level α. Jarque and Bera (1987) (JB) combine the two prior tests and use the test
statistic
JB =
ˆS2(r)
6/T + [ ˆK(r) −3]2
24/T
,
which is asymptotically distributed as a chi-squared random variable with 2 degrees
of freedom, to test for the normality of rt. One rejects H0 of normality if the p
value of the JB statistic is less than the signiﬁcance level.
Example 1.2.
Consider the daily simple returns of the International Business
Machines (IBM) stock used in Table 1.2. The sample skewness and kurtosis of
the returns are parts of the descriptive (or summary) statistics that can be obtained
easily using various statistical software packages. Both R and S-Plus are used in
the demonstration, where d-ibm3dx7008.txt is the data ﬁle name. Note that in
R the kurtosis denotes excess kurtosis. From the output, the excess kurtosis is high,
indicating that the daily simple returns of IBM stock have heavy tails. To test the
symmetry of return distribution, we use the test statistic
t =
0.0614
√6/9845 = 0.0614
0.0247 = 2.49,
which gives a p value of about 0.013, indicating that the daily simple returns of
IBM stock are signiﬁcantly skewed to the right at the 5% level.
--- page 38 ---

distributional properties of returns
11
TABLE 1.2
Descriptive Statistics for Daily and Monthly Simple and Log Returns of
Selected Indexes and Stocksa
Standard
Excess
Security
Start
Size
Mean Deviation Skewness Kurtosis Minimum Maximum
Daily Simple Returns (%)
SP
70/01/02
9845 0.029
1.056
−0.73
22.81
−20.47
11.58
VW
70/01/02
9845 0.040
1.004
−0.62
18.02
−17.13
11.52
EW
70/01/02
9845 0.076
0.814
−0.77
17.08
−10.39
10.74
IBM
70/01/02
9845 0.040
1.693
0.06
9.92
−22.96
13.16
Intel
72/12/15
9096 0.108
2.891
−0.15
6.13
−29.57
26.38
3M
670/01/02 9845 0.045
1.482
−0.36
13.34
−25.98
11.54
Microsoft
86/03/14
5752 0.123
2.359
−0.13
9.92
−30.12
19.57
Citi-Grp
86/10/30
5592 0.067
2.602
1.80
55.25
−26.41
57.82
Daily Log Returns (%)
SP
70/01/02
9845 0.023
1.062
−1.17
30.20
−22.90
10.96
VW
70/01/02
9845 0.035
1.008
−0.94
21.56
−18.80
10.90
EW
70/01/02
9845 0.072
0.816
−1.00
17.76
−10.97
10.20
IBM
70/01/02
9845 0.026
1.694
−0.27
12.17
−26.09
12.37
Intel
72/12/15
9096 0.066
2.905
−0.54
7.81
−35.06
23.41
3M
70/01/02
9845 0.034
1.488
−0.78
20.57
−30.08
10.92
Microsoft
86/03/14
5752 0.095
2.369
−0.63
14.23
−35.83
17.87
Citi-Grp
86/10/30
5592 0.033
2.575
0.22
33.19
−30.66
45.63
Monthly Simple Returns (%)
SP
26/01
996 0.58
5.53
0.32
9.47
−29.94
42.22
VW
26/01
996 0.89
5.43
0.15
7.69
−29.01
38.37
EW
26/01
996 1.22
7.40
1.52
14.94
−31.28
66.59
IBM
26/01
996 1.35
7.15
0.44
3.43
−26.19
47.06
Intel
73/01
432 2.21
12.85
0.32
2.70
−44.87
62.50
3M
46/02
755 1.24
6.45
0.22
0.98
−27.83
25.80
Microsoft
86/04
273 2.62
11.08
0.66
1.96
−34.35
51.55
Citi-Grp
86/11
266 1.17
9.75
−0.47
1.77
−39.27
26.08
Monthly Log Returns (%)
SP
26/01
996 0.43
5.54
−0.52
7.93
−35.58
35.22
VW
26/01
996 0.74
5.43
−0.58
6.85
−34.22
32.47
EW
26/01
996 0.96
7.14
0.25
8.55
−37.51
51.04
IBM
26/01
996 1.09
7.03
−0.07
2.62
−30.37
38.57
Intel
73/01
432 1.39
12.80
−0.55
3.06
−59.54
48.55
3M
46/02
755 1.03
6.37
−0.08
1.25
−32.61
22.95
Microsoft
86/04
273 2.01
10.66
0.10
1.59
−42.09
41.58
Citi-Grp
86/11
266 0.68
10.09
−1.09
3.76
−49.87
23.18
aReturns are in percentages and the sample period ends on December 31, 2008. The statistics are deﬁned
in eqs. (1.10)–(1.13), and VW, EW and SP denote value-weighted, equal-weighted, and S&P composite
index.
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
