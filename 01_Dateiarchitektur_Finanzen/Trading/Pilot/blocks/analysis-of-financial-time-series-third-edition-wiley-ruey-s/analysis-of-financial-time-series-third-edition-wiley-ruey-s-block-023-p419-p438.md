# Analysis of Financial Time Series, Third Edition (Wiley -- Ruey S_ Tsay -- Wiley series in probability and statistics, 3rd ed_, -- John Wiley & Sons, -- isbn13 9780470414354 -- 9f99b80c7b2dedd477f463dc5323f3b6 -- An.pdf — pages 419–438

--- page 419 ---

392
multivariate time series analysis and its applications
8.1.2
Linear Dependence
Considered jointly, the cross-correlation matrices {ρℓ|ℓ= 0, 1, . . .} of a weakly
stationary vector time series contain the following information:
1. The diagonal elements {ρii(ℓ)|ℓ= 0, 1, . . .} are the autocorrelation function
of rit.
2. The off-diagonal element ρij(0) measures the concurrent linear relationship
between rit and rjt.
3. For ℓ> 0, the off-diagonal element ρij(ℓ) measures the linear dependence of
rit on the past value rj,t−ℓ.
Therefore, if ρij(ℓ) = 0 for all ℓ> 0, then rit does not depend linearly on any
past value rj,t−ℓof the rjt series.
In general, the linear relationship between two time series {rit} and {rjt} can be
summarized as follows:
1. rit and rjt have no linear relationship if ρij(ℓ) = ρji(ℓ) = 0 for all ℓ≥0.
2. rit and rjt are concurrently correlated if ρij(0)̸ = 0.
3. rit and rjt have no lead–lag relationship if ρij(ℓ) = 0 and ρji(ℓ) = 0 for all
ℓ> 0. In this case, we say the two series are uncoupled.
4. There is a unidirectional relationship from rit to rjt if ρij(ℓ) = 0 for all
ℓ> 0, but ρji(v)̸ = 0 for some v > 0. In this case, rit does not depend on
any past value of rjt, but rjt depends on some past values of rit.
5. There is a feedback relationship between rit and rjt if ρij(ℓ)̸ = 0 for some
ℓ> 0 and ρji(v)̸ = 0 for some v > 0.
The conditions stated earlier are sufﬁcient conditions. A more informative approach
to study the relationship between time series is to build a multivariate model for
the series because a properly speciﬁed model considers simultaneously the serial
and cross correlations among the series.
8.1.3
Sample Cross-Correlation Matrices
Given the data {rt|t = 1, . . . , T }, the cross-covariance matrix
ℓcan be estimated by

ℓ= 1
T
T

t=ℓ+1
(rt −¯r)(rt−ℓ−¯r)′,
ℓ≥0,
(8.5)
where ¯r = (T
t=1 rt)/T is the vector of sample means. The cross-correlation matrix
ρℓis estimated by
ρℓ= 
D
−1
ℓ
D
−1,
ℓ≥0,
(8.6)
--- page 420 ---

weak stationarity and cross-correlation matrices
393
where 
D is the k × k diagonal matrix of the sample standard deviations of the
component series.
Similar to the univariate case, asymptotic properties of the sample crosscorrelation matrix ρℓhave been investigated under various assumptions; see, for
instance, Fuller (1976, Chapter 6). The estimate is consistent but is biased in a
ﬁnite sample. For asset return series, the ﬁnite sample distribution of ρℓis rather
complicated partly because of the presence of conditional heteroscedasticity and
high kurtosis. If the ﬁnite-sample distribution of cross correlations is needed,
we recommend that proper bootstrap resampling methods be used to obtain
an approximate estimate of the distribution. For many applications, a crude
approximation of the variance of ˆρij(ℓ) is sufﬁcient.
Example 8.1.
Consider the monthly log returns of IBM stock and the S&P 500
index from January 1926 to December 2008 with 996 observations. The returns
include dividend payments and are in percentages. Denote the returns of IBM
stock and the S&P 500 index by r1t and r2t, respectively. These two returns form a
bivariate time series rt = (r1t, r2t)′. Figure 8.1 shows the time plots of rt. Figure 8.2
shows some scatterplots of the two series. The plots show that the two return series
are concurrently correlated. Indeed, the sample concurrent correlation coefﬁcient
between the two returns is 0.65, which is statistically signiﬁcant at the 5% level.
However, the cross correlations at lag 1 are weak if any.
1940
1960
1980
2000
−30
0
20
40
Year
(a)
IBM
−30
0
20
S&P 500
1940
1960
1980
2000
Year
(b)
Figure 8.1
Time plots of monthly log returns, in percentages, for (a) IBM stock and (b) the S&P 500
index from January 1926 to December 2008.
--- page 421 ---

394
multivariate time series analysis and its applications
*
*
*
*
* *
*
*
*
* **
*
*
*
*
*
*
*
*
*
*
*
*
**
*
**
* *
*
**
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
* *
*
*
*
*
*
* *
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
* *
*
*
*
*
*
*
*
*
*
*
**
*
* **
** *
**
*
*
*
**
*
**
*
*
* *
*
*
*
*
*
*
*
* *
*
*
* *
*
*
*
*
*
* *
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
**
*
*
**
*
*
* *
* **
*
* **
**
* **
*
*
**
*
*
*
** *
*
*
*
**
* *
*
*
**
*
*
*
**
*
* **
* ***
*
*
*
*
*
*
*
**
**
*
* *
*
*
*
*
**
*
*
** **
**
*
*
**
** *
* *
*
*
*
* *
*
*
*
*
*
*
*
*
*
*
** *
*
*
*
*
*
*
*
**
**
*
*
*
*
** **
*
*
*
**
*
*
**
*
*
*
*
*
*
**
*
*** **
***
*
*
*
*
*
* *
** *
*
*
*
*
*
*
*
*
*
*
*
**
* *
*
*
*
**
*
*
*
*
*
*
*
*
*
*
**
**
*
** *
**
*
*
** * *
*
*
* ***
*
*
*
*
**
*
*
**
*
*
* *
*
* *
*
*
*
*
**
*
*
* *
*
*
***
**
**
*
**
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
**
*
*
* *
*
*
*
****
*
*
**
* *
***
*
**
*
*
*
****
***
**
*
* *
*
*
*
*
*
*
* **
*
* *
*
*
* **
**
*
*
*
*
* * *
*
*
* *
*
**
*
*
*
*
*
*
**
*
*
*
*
**
*
**
* ***
* *
*
*
*
*
*
*
* *
*
*
****
** *
**
*
*
*
* *
*** *
*
*
*
*
*
*****
*
**
*
*
* *
*
*
*
**
*
*
**
*
*
*
*
* *
*
*
*
** *
**
*
* **
*
*
*
***
*
*
*
* * *
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*** *
**
*
*
**
**
*
***
**
*
*
*
*
* *
*
**
*
*
*
*
*
*
***
*
*
*
* *
*
*
*
*
*
*
**
*
*
*
*
*** *
*
**
* *
*
*
*
*
***
*
**
*
*
*
*
*
*
*
*
*
*
**
*
* **
*
*
*
*
*
*
*
*
*
*
*
*
*
**
*
* *
* *
*
*
*
*
*
**
**
*
**
*
*
**
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
* *
*
*
*
*
*
* *
*
*
*
**
*
*
*
**
*
*
*
*
**
*
*
**
*
*
*
*
*
*
*
*
**
*
**
*
* *
* *
*
*
*
*
**
*
*
* *
*
*
*
*
*
*
*
**
*
*
*
*
*
**
*
*
*
* *
*
*
***
*
*
*
*
*
*
* *
*
*
* *
*
*
*
**
*
*
*
* *
*
*
*
*
*
*
*
*
*
**
*
*
*
**
*
*
*
*
*
*
*
*
*
*
***
*
*
*
**
*
*
* *
*
*
** **
* *****
* *
*
*
*
*
*
**
*
*
*
*
***
* ****
*
*
**
*
*
**
*
* **
*
*
*
*
*
* *
*
*
*
*
*
*
*
*
−30
−10
0
10
20
30
−30
−10
10
30
S&P 500
(a)
IBM
**
*
*
* *
*
*
**
* *
*
*
*
* *
*
*
*
*
*
*
*
**
*
*
*
**
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
* *
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
**
*
*
*
* *
*
*
* *
*
** ***
*
*
*
**
*
*
*
*
*
*
* *
*
*
*
*
*
* **
*
**
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*****
*
*
*
*
*
*
*
* *
*
*
**
* *
*
***
*
*
*
*
* *
* *
*
* **
*
*
*
**
*
**
***
*
*
*
*
*
*
*
**
*
** *
**
*
*
**
*
*
* *
*
*
*
** *
* *
*
**
*
*** *
*
*
*
*
*
*
*
*
*
*
*
*
**
*
**
*
*
*
*
* *
*
*
*
* *
*
*
**
*
*
***
*
*
*
**
*
*
*
*
*
*
*
*
*
*
*
* *
*** * **
* **
*
*
*
*
*
* *****
*
*
*
*
*
*
*
*
*
* *
*
**
**
*
**
*
**
*
*
*
*
*
*
*
*
*
**
*
*
* ***
*
*
** *
*
*
*
* *
**
*
**
*
*
*
*
*
*
* *
*
** *
**
*
*
*
* **
*
*
*
*
* *
*
***
***
* * *
* *
**
*
*
*
**
*
*
*
*
*
*
*
*
*
* *
*
*
*
**
*
*
****
*
*
*
** *
***
*
*
*
*
*
*
****
*
* * *
*
*
**
*
*
* *
*
*
**
*
*
*
*
*
*
**
*
*
* *
*
*
*
*
* **
*
*
**
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
* * *
* *****
*
* *
*
*
**
*
**
* *
**
* **
*
*
** *
**
** *
*
*
*
*
*
*
***
*
*
*
**
*
*
*
*
* *
*
**
*
*
*
*
*
*
*
*
* *
*
* *
* **
*
*
*
* **
*
*
*
**
*
* *
*
**
*
*
*
*
*
*
*
*
*
*
*
*
*
*
***
*
*
*
*
*
*
*
*
* * *
*
*
*
*
*
*
*
*
*
*
*
*
* *
*
*
*
*
*
*
*
*
**
*
*
*
***
***
*
*
*
*
*
*
*
*
*
*
*
*
* *
*
*
**
* *
*
*
*
* *
*
*
*
*
* * *
* *
*
*
*
*
*
*
*
*
*
*
****
**
*
*
*
*
*
*
*
*
*
*
*
*
*
*
* *
*
*
*
*
*
*
*
*
**
**
*
*
**
*
*
*
*
*
*
*
*
*
*
*
*
**
*
*
*
*
*
*
*
* *
**
*
*
*
*
**
*
*
*
* *
**
*
*
*
*
*
*
*
*
*
*
** *
*
*
*
*
*
*
*
*
* * *
* *
*
*
*
*
*
*
*
*
*
* *
*
***
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
**
**
*
*
*
*
*
*
**
*
*
*
**
*
*
**
*
*
*
*
*
*
*
*
*
*
*
* *
**
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
**
*
*
*
* * *
*
*** *
*
** *
*** * **
*
* **
*
**
*
* *
*
*
*
** *
*
** * *
*
*
*
*
*
*
*
*
*
*
**
*
*
*
*
*
*
* *
*
*
*
*
*
*
*
−30
−10
0
10
20
30
40
−30
−10
10
30
IBM 1
S&P 500
*
*
*
**
*
**
* **
*
*
*
*
*
*
*
**
*
*
*
**
*
**
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
**
*
*
* **
** *
**
*
*
*
*
*
*
*
**
*
** *
*
*
*
*
*
*
*
*
*
* *
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
**
*
*
*
*
*
* *
* *
* *
*
*
* **
*
*
* *
*
*
*
**
*
**
** *
*
*
***
* *
*
*
**
*
*
*
*
*
*
* **
* **
*
* *
*
*
*
*
***
*
**
*
* *
*
*
*
*
*
*
*
*
** *
*
*
*
* *
**
** *
*
*
**
*
* *
*
*
*
*
*
*
*
*
*
*
**
*
*
*
*
*
*
*
**
* *
*
*
*
**
** *
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*** *
*
**
*
*
*
* *
*
* *
** *
*
*
**
* *
*
*
*
*
*
*
**
*
*
*
*
**
*
*
*
*
*
*
*
*
*
*
*
* *
*
*
**
**
*
*
*
** * *
*
*
* **
*
**
* *
*
*
*
**
*
*
*
* *
*
*
*
*
*
*
*
*
*
**
*
*
*
* ***
*
*
*
*
**
*
**
*
* *
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
** *
*
*
* ***
*
*
***
* *
**
*
*
*
*
*
*
*
***
*
***
*
*
*
* **
*
*
*
*
*
*
* *
*
*
* *
* *
* *
*
*
* *
*
**
* *
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
* *
*
*
*
*
* ***
*
*
*
*
*
*
*
*
*
*
*
*****
** *
*
* *
*
*
*
*
*** *
*
*
*
*
*
****
*
*
*
*
*
*
*
*
*
*
**
*
*
* *
*
*
*
*
*
*
*
*
*
*
**
*
**
*
* *
**
*
*
***
**
*
* *
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
* *
*
*
*
*
*
*
*
***
*
*
**
*
*
*
**
****
**
**
*
*
*
*
*
*
*
*
*
*
*
***
*
*
*
*
*
*
*
*
*
**
* **
*
*
*
*
***
*
*
*
**
*
*
**
*
**
*
*
**
*
*
*
*
*
*
*
*
*
*
**
** *
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
* *
*
*
*
**
*
*
*
*
* *
*
*
**
*
*
**
*
*
*
*
*
*
*
*
*
*
*
*
*
* *
*
*
* *
*
*
*
* *
*
*
*
*
**
**
*
*
*
*
*
*
*
**
*
**
*
*
*
*
*
*
*
*
*
**
*
**
*
*
*
*
*
*
**
*
**
*
*
*
*
*
*
*
*
*
*
*
**
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
***
*
*
*
*
*
*
*
* *
*
*
* *
*
*
*
*
* *
*
*
*
*
*
*
*
*
*
*
*
**
*
*
* *
*
*
*
*
*
*
*
*
*
*
*
*
* **
*
*
*
**
*
*
*
* *
**
** **
* ****
*
* *
*
* *
*
*
**
*
*
**
***
* ***
*
*
**
*
*
* *
*
** **
*
* *
*
* * *
*
*
**
*
*
*
*
*
*
** **
*
*
* **
*
*
**
*
*
**
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
**
*
*
*
*
*
*
*
*
* *
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
* *
*
*
*
*
*
*
*
*
*
**
*
*
* *
*
** *
** *
*
*
*
**
*
*
*
*
** *
*
*
*
*
*
*
*
* *
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
* **
*
*
*
***
*
* *
* *
*
*
* *
*
*
*
* *
*
*
*
*
*
*
**
**
*
*
****
* *
*
*
**
*
*
*
***
* *
*
* *** *
*
*
*
*
**
*
****
*
*
*
**
*
**
*
*
*
* **
**
*
*
*
*
** *
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
**
*
*
***
* *
*** *
*
*
***
** *
*
*
*
*
*
*
*
*
*** *
*
*
*
*
**
*
*** **
******
*
*
* *
** *
* ***
*
*
*
*
*
*
*
*** *
*
*
*
**
*
*
*
*
*
*
*
*
*
*
*
* **
*
*
* ***
*
*
** *
*
*
*
* *****
* *
** *
** **
* *
*
* **
*
*
*
** **
*
*
*
* ***
**
**
*
**
* **
*
* *
*
*
*
*
*
*
*
*
*
*
*
*
**
*
*
*
*
* *
* ********
* *
*** *
** *
*
*
****
***
**
*
* *
*
*
* *
*
*
*
* *
*
*
*
*
*
*
* *
*
**
*
*
**
* * *
*
*
* *
*
**
*
*
*
*
*
*
*
*
*
*
*
* *
*
*
**
* ***
* *
*
* *
*
*
*
*
*
*
*****
** *
** *
*
*
* *
***
*
*
*
*
*
*
*****
*
**
*
*
*
*
*
*
**
*
* *
*
*
*
*
*
* *
*
* *
** *
*
*
*
* ***
*
*
***
*
*
*
* *
*
*
*
*
*
*
*
*
**
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
***
*
**
*
*
*
*
*
*
***
*
*
*
*
*
**
* *
*
**
*
*
*
*
*
****
*
*
*
* **
* *
**
* *
*
*
*
*
*
*** *
*
**
* *
***
*
***
*
*
*
*
*
*
*
*
*
*
*
*
*
**
** **
*
*
*
*
*
*
*
* ** *
*
*
**
*
*
*
* * **
*
*
*
** *
*
*
*
*
*
*
*
*
* *
*
*
***
*
*
*
*
*
*
*
*
*
*
* *
* *
*
*
*
* ** ****
* *
** *
* *
**
*
*
*
**
*
*
*
*
*
* ********
* *
* *
**
***
*
*
* *
*
*
*
*
*
*
***
*
*
*
*
*
*
* **
*
* *
*
*
****
*
*
*
*
*
*
* *
*
*
*
*
*
*
*
** *
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
* **
*
*
*
***
*
*
* *
**
** *
*
* ****
*
* *
** *
* *
**
* *
**
***
* *******
* * **
** **
*
*
*
* *
* *
*
*
*
*
*
*
*
−30
−10
10
30
S&P 500
−30
−10
10
30
IBM
−30
−10
0
10
20
30
S&P 500—Lag 1
(c)
−30
−10
0
10
20
30
S&P 500—Lag 1
(d)
(b)
Figure 8.2
Some scatterplots for monthly log returns of IBM stock and S&P 500 index: (a) concurrent
plot of IBM vs. S&P 500, (b) S&P 500 vs. lag-1 IBM, (c) IBM vs. lag-1 S&P 500, and (d) S&P 500
vs. lag-1 S&P 500.
Table 8.1 provides some summary statistics and cross-correlation matrices of the
two series. For a bivariate series, each CCM is a 2 × 2 matrix with four correlations.
Empirical experience indicates that it is rather hard to absorb simultaneously many
cross-correlation matrices, especially when the dimension k is greater than 3. To
overcome this difﬁculty, we use the simplifying notation of Tiao and Box (1981)
and deﬁne a simpliﬁed cross-correlation matrix consisting of three symbols “+,”
“−,” and “.” where they have the following meaning:
1. Plus sign (+) means that the corresponding correlation coefﬁcient is greater
than or equal to 2/
√
T .
2. Minus sign (−) means that the corresponding correlation coefﬁcient is less
than or equal to −2/
√
T .
3. Period (.) means that the corresponding correlation coefﬁcient is between
−2/
√
T and 2/
√
T .
And 1/
√
T is the asymptotic 5% critical value of the sample correlation under the
assumption that rt is a white noise series.
--- page 422 ---

weak stationarity and cross-correlation matrices
395
TABLE 8.1
Summary Statistics and Cross-Correlation Matrices of Monthly Log
Returns of IBM Stock and S&P 500 Index: January 1926 to December 2008
(a) Summary Statistics
Standard
Excess
Ticker
Mean
Error
Skewness
Kurtosis
Minimum
Maximum
IBM
1.089
7.033
−0.068
2.622
−30.37
38.57
SP5
0.430
5.537
−0.521
7.927
−35.59
35.22
(b) Cross-Correlation Matrices
Lag 1
Lag 2
Lag 3
Lag 4
Lag 5
0.04
0.10
0.00
−0.08
−0.01
−0.06
−0.03
−0.03
0.02
0.08
0.04
0.08
0.02
−0.02
−0.06
−0.10
0.04
0.03
0.00
0.09
(c) Simpliﬁed notation

·
+
·
+


·
−
·
·


·
·
·
−


·
·
·
·


·
+
·
+

Table 8.1(c) shows the simpliﬁed CCM for the monthly log returns of IBM
stock and the S&P 500 index. It is easily seen that signiﬁcant cross correlations at
the approximate 5% level appear mainly at lags 1 and 3. An examination of the
sample CCMs at these two lags indicates that (a) S&P 500 index returns have some
marginal autocorrelations at lags 1, 2, 3, and 5 and (b) IBM stock returns depend
weakly on the previous returns of the S&P 500 index. The latter observation is
based on the signiﬁcance of cross correlations at the (1, 2)th element of lag-1, lag-2
and lag-5 CCMs.
Figure 8.3 shows the sample autocorrelations and cross correlations of the two
series. The upper-left plot is the sample ACF of IBM stock returns and the upperright plot shows the dependence of IBM stock returns on the lagged S&P 500 index
returns. The dashed lines in the plots are the asymptotic two standard error limits
of the sample autoand cross-correlation coefﬁcients. From the plots, the dynamic
relationship is weak between the two return series, but their contemporaneous
correlation is statistically signiﬁcant.
Example 8.2.
Consider the simple returns of monthly indexes of U.S. government bonds with maturities in 30 years, 20 years, 10 years, 5 years, and 1 year.
The data obtained from the CRSP database have 696 observations starting from
January 1942 to December 1999. Let rt = (r1t, . . . , r5t)′ be the return series with
decreasing time to maturity. Figure 8.4 shows the time plots of rt on the same scale.
The variability of the 1-year bond returns is much smaller than that of returns with
longer maturities. The sample means and standard deviations of the data are µ =
10−2(0.43, 0.45, 0.45, 0.46, 0.44)′
and
σ = 10−2(2.53, 2.43, 1.97, 1.39, 0.53)′.
--- page 423 ---

396
multivariate time series analysis and its applications
0
2
4
6
8
10
12
−1.0
0.0
0.5
1.0
Lag
CCF
0
2
4
6
8
10
12
−1.0
0.0
0.5
1.0
Lag
CCF
0
2
4
6
8
10
12
−1.0
0.0
0.5
1.0
Lag
CCF
0
2
4
6
8
10
12
−1.0
0.0
0.5
1.0
Lag
CCF
Figure 8.3
Sample autoand cross-correlation functions (CCF) of two monthly log return series:
(a) sample ACF of IBM stock returns, (b) cross-correlations between S&P 500 index and lagged IBM
stock returns (lower left), (c) cross correlations between IBM stock and lagged S&P 500 index returns,
and (d) sample ACF of S&P 500 index returns. Dashed lines denote 95% limits.
The concurrent correlation matrix of the series is
ρ0 =


1.00
0.98
0.92
0.85
0.63
0.98
1.00
0.91
0.86
0.64
0.92
0.91
1.00
0.90
0.68
0.85
0.86
0.90
1.00
0.82
0.63
0.64
0.68
0.82
1.00


.
It is not surprising that (a) the series have high concurrent correlations, and (b) the
correlations between long-term bonds are higher than those between short-term
bonds.
Table 8.2 gives the lag-1 and lag-2 cross-correlation matrices of rt and the
corresponding simpliﬁed matrices. Most of the signiﬁcant cross correlations are at
lag 1, and the ﬁve return series appear to be intercorrelated. In addition, lag-1 and
lag-2 sample ACFs of the 1-year bond returns are substantially higher than those
of other series with longer maturities.
--- page 424 ---

weak stationarity and cross-correlation matrices
397
Year
(a)
Returns
1940
1950
1960
1970
1980
1990
2000
−10
0 510
Returns
−10 0 510
Returns
−10 0 510
Returns
−10 0 510
Returns
−10 0 510
Year
(b)
1940
1950
1960
1970
1980
1990
2000
Year
(c)
1940
1950
1960
1970
1980
1990
2000
Year
(d)
1940
1950
1960
1970
1980
1990
2000
Year
(e)
1940
1950
1960
1970
1980
1990
2000
Figure 8.4
Time plots of monthly simple returns of ﬁve indexes of U.S. government bonds with
maturities in (a) 30 years, (b) 20 years, (c) 10 years, (d) 5 years, and (e) 1 year. Sample period is from
January 1942 to December 1999.
8.1.4
Multivariate Portmanteau Tests
The univariate Ljung–Box statistic Q(m) has been generalized to the multivariate
case by Hosking (1980, 1981) and Li and McLeod (1981). For a multivariate
series, the null hypothesis of the test statistic is H0 : ρ1 = · · · = ρm = 0, and the
alternative hypothesis Ha : ρi̸ = 0 for some i ∈{1, . . . , m}. Thus, the statistic is
used to test that there are no autoand cross correlations in the vector series rt.
The test statistic assumes the form
Qk(m) = T 2
m

ℓ=1
1
T −ℓtr(
′
ℓ
−1
0 
ℓ
−1
0 ),
(8.7)
where T is the sample size, k is the dimension of rt, and tr(A) is the trace of
the matrix A, which is the sum of the diagonal elements of A. Under the null
--- page 425 ---

398
multivariate time series analysis and its applications
TABLE 8.2
Sample Cross-Correlation Matrices of Monthly Simple Returns of Five
Indexes of U.S. Government Bonds: January 1942 to December 1999
Lag 1
Lag 2
Cross-Correlations
0.10
0.08
0.11
0.12
0.16
−0.01
0.00
0.00
−0.03
0.03
0.10
0.08
0.12
0.14
0.17
−0.01
0.00
0.00
−0.04
0.02
0.09
0.08
0.09
0.13
0.18
0.01
0.01
0.01
−0.02
0.07
0.14
0.12
0.15
0.14
0.22
−0.02
−0.01
0.00
−0.04
0.07
0.17
0.15
0.21
0.22
0.40
−0.02
0.00
0.02
0.02
0.22
Simpliﬁed Cross-Correlation Matrices


+
+
+
+
+
+
+
+
+
+
+
+
+
+
+
+
+
+
+
+
+
+
+
+
+




·
·
·
·
·
·
·
·
·
·
·
·
·
·
·
·
·
·
·
·
·
·
·
·
+


hypothesis and some regularity conditions, Qk(m) follows asymptotically a chisquared distribution with k2m degrees of freedom.
Remark.
The Qk(m) statistics can be rewritten in terms of the sample crosscorrelation matrices ρℓ. Using the Kronecker product ⊗and vectorization of matrices discussed in Appendix A of this chapter, we have
Qk(m) = T 2
m

ℓ=1
1
T −ℓb′
ℓ(ρ−1
0
⊗ρ−1
0 )bℓ,
where bℓ= vec(ρ′
ℓ). The test statistic proposed by Li and McLeod (1981) is
Q∗
k(m) = T
m

ℓ=1
b′
ℓ(ρ−1
0
⊗ρ−1
0 )bℓ+ k2m(m + 1)
2T
,
which is asymptotically equivalent to Qk(m).
□
Applying the Qk(m) statistics to the bivariate monthly log returns of IBM stock
and the S&P 500 index of Example 8.1, we have Q2(1) = 9.81, Q2(5) = 47.06,
and Q2(10) = 71.65. Based on asymptotic chi-squared distributions with degrees
of freedom 4, 20, and 40, the p values of these Q2(m) statistics are 0.044, 0.001,
and 0.002, respectively. The portmanteau tests thus conﬁrm the existence of serial
dependence in the bivariate return series at the 5% signiﬁcance level. For the ﬁvedimensional monthly simple returns of bond indexes in Example 8.2, we have
Q5(5) = 1065.63, which is highly signiﬁcant compared with a chi-squared distribution with 125 degrees of freedom.
--- page 426 ---

vector autoregressive models
399
The Qk(m) statistic is a joint test for checking the ﬁrst m cross-correlation matrices of rt being zero. If it rejects the null hypothesis, then we build a multivariate
model for the series to study the lead–lag relationships between the component
series. In what follows, we discuss some simple vector models useful for modeling
the linear dynamic structure of a multivariate ﬁnancial time series.
8.2
VECTOR AUTOREGRESSIVE MODELS
A simple vector model useful in modeling asset returns is the vector autoregressive
(VAR) model. A multivariate time series rt is a VAR process of order 1, or VAR(1)
for short, if it follows the model
rt = φ0 + rt−1 + at,
(8.8)
where φ0 is a k-dimensional vector,  is a k × k matrix, and {at} is a sequence of
serially uncorrelated random vectors with mean zero and covariance matrix . In
application, the covariance matrix  is required to be positive deﬁnite; otherwise,
the dimension of rt can be reduced. In the literature, it is often assumed that at is
multivariate normal.
Consider the bivariate case [i.e., k = 2, rt = (r1t, r2t)′, and at = (a1t, a2t)′]. The
VAR(1) model consists of the following two equations:
r1t = φ10 + 11r1,t−1 + 12r2,t−1 + a1t,
r2t = φ20 + 21r1,t−1 + 22r2,t−1 + a2t,
where ij is the (i, j)th element of  and φi0 is the ith element of φ0. Based on
the ﬁrst equation, 12 denotes the linear dependence of r1t on r2,t−1 in the presence
of r1,t−1. Therefore, 12 is the conditional effect of r2,t−1 on r1t given r1,t−1. If
12 = 0, then r1t does not depend on r2,t−1, and the model shows that r1t only
depends on its own past. Similarly, if 21 = 0, then the second equation shows
that r2t does not depend on r1,t−1 when r2,t−1 is given.
Consider the two equations jointly. If 12 = 0 and 21̸ = 0, then there is a
unidirectional relationship from r1t to r2t. If 12 = 21 = 0, then r1t and r2t are
uncoupled. If 12̸ = 0 and 21̸ = 0, then there is a feedback relationship between
the two series.
8.2.1
Reduced and Structural Forms
In general, the coefﬁcient matrix  of Eq. (8.8) measures the dynamic dependence
of rt. The concurrent relationship between r1t and r2t is shown by the off-diagonal
element σ12 of the covariance matrix  of at. If σ12 = 0, then there is no concurrent linear relationship between the two component series. In the econometric
literature, the VAR(1) model in Eq. (8.8) is called a reduced-form model because it
--- page 427 ---

400
multivariate time series analysis and its applications
does not show explicitly the concurrent dependence between the component series.
If necessary, an explicit expression involving the concurrent relationship can be
deduced from the reduced-form model by a simple linear transformation. Because
 is positive deﬁnite, there exists a lower triangular matrix L with unit diagonal elements and a diagonal matrix G such that  = LGL′; see Appendix A on
Cholesky decomposition. Therefore, L−1(L′)−1 = G.
Deﬁne bt = (b1t, . . . , bkt)′ = L−1at. Then
E(bt) = L−1E(at) = 0,
Cov(bt) = L−1(L−1)′ = L−1(L′)−1 = G.
Since G is a diagonal matrix, the components of bt are uncorrelated. Multiplying
L−1 from the left to model (8.8), we obtain
L−1rt = L−1φ0 + L−1rt−1 + L−1at = φ∗
0 + ∗rt−1 + bt,
(8.9)
where φ∗
0 = L−1φ0 is a k-dimensional vector and ∗= L−1 is a k × k matrix.
Because of the special matrix structure, the kth row of L−1 is in the form
(wk1, wk2, . . . , wk,k−1, 1). Consequently, the kth equation of model (8.9) is
rkt +
k−1

i=1
wkirit = φ∗
k,0 +
k

i=1
∗
kiri,t−1 + bkt,
(8.10)
where φ∗
k,0 is the kth element of φ∗
0 and ∗
ki is the (k, i)th element of ∗. Because
bkt is uncorrelated with bit for 1 ≤i < k, Eq. (8.10) shows explicitly the concurrent
linear dependence of rkt on rit, where 1 ≤i ≤k −1. This equation is referred to
as a structural equation for rkt in the econometric literature.
For any other component rit of rt, we can rearrange the VAR(1) model so that
rit becomes the last component of rt. The prior transformation method can then be
applied to obtain a structural equation for rit. Therefore, the reduced-form model
(8.8) is equivalent to the structural form used in the econometric literature. In time
series analysis, the reduced-form model is commonly used for two reasons. The
ﬁrst reason is ease in estimation. The second and main reason is that the concurrent
correlations cannot be used in forecasting.
Example 8.3.
To illustrate the transformation from a reduced-form model to
structural equations, consider the bivariate AR(1) model

r1t
r2t

=

0.2
0.4

+

 0.2
0.3
−0.6
1.1

r1,t−1
r2,t−1

+

a1t
a2t

,
 =

2
1
1
1

.
For this particular covariance matrix , the lower triangular matrix
L−1 =

1.0
0.0
−0.5
1.0

--- page 428 ---

vector autoregressive models
401
provides a Cholesky decomposition [i.e., L−1(L′)−1 is a diagonal matrix]. Premultiplying L−1 to the previous bivariate AR(1) model, we obtain

1.0
0.0
−0.5
1.0

 r1t
r2t

=

 0.2
0.3

+

0.2
0.3
−0.7
0.95

 r1,t−1
r2,t−1

+

 b1t
b2t

,
G =

 2
0
0
0.5

,
where G = Cov(bt). The second equation of this transformed model gives
r2t = 0.3 + 0.5r1t −0.7r1,t−1 + 0.95r2,t−1 + b2t,
which shows explicitly the linear dependence of r2t on r1t.
Rearranging the order of elements in rt, the bivariate AR(1) model becomes

 r2t
r1t

=

 0.4
0.2

+

 1.1
−0.6
0.3
0.2

 r2,t−1
r1,t−1

+

 a2t
a1t

,
 =

 1
1
1
2

.
The lower triangular matrix needed in the Cholesky decomposition of  becomes
L−1 =

1.0
0.0
−1.0
1.0

.
Premultiplying L−1 to the earlier rearranged VAR(1) model, we obtain

1.0
0.0
−1.0
1.0

 r2t
r1t

=

0.4
−0.2

+

1.1
−0.6
−0.8
0.8

 r2,t−1
r1,t−1

+

 c1t
c2t

,
G =

 1
0
0
1

,
where G = Cov(ct). The second equation now gives
r1t = −0.2 + 1.0r2t −0.8r2,t−1 + 0.8r1,t−1 + c2t.
Again this equation shows explicitly the concurrent linear dependence of r1t on r2t.
8.2.2
Stationarity Condition and Moments of a VAR(1) Model
Assume that the VAR(1) model in Eq. (8.8) is weakly stationary. Taking expectation
of the model and using E(at) = 0, we obtain
E(rt) = φ0 + E(rt−1).
Since E(rt) is time invariant, we have
µ ≡E(rt) = (I −)−1φ0
--- page 429 ---

402
multivariate time series analysis and its applications
provided that the matrix I − is nonsingular, where I is the k × k identity matrix.
Using φ0 = (I −)µ, the VAR(1) model in Eq. (8.8) can be written as
(rt −µ) = (rt−1 −µ) + at.
Let ˜rt = rt −µ be the mean-corrected time series. Then the VAR(1) model
becomes
˜rt = ˜rt−1 + at.
(8.11)
This model can be used to derive properties of a VAR(1) model. By repeated
substitutions, we can rewrite Eq. (8.11) as
˜rt = at + at−1 + 2at−2 + 3at−3 + · · · .
This expression shows several characteristics of a VAR(1) process. First, since
at is serially uncorrelated, it follows that Cov(at, rt−1) = 0. In fact, at is not
correlated with rt−ℓfor all ℓ> 0. For this reason, at is referred to as the shock or
innovation of the series at time t. It turns out that, similar to the univariate case, at
is uncorrelated with the past value rt−j (j > 0) for all time series models. Second,
postmultiplying the expression by a′
t, taking expectation, and using the fact of no
serial correlations in the at process, we obtain Cov(rt, at) = . Third, for a VAR(1)
model, rt depends on the past innovation at−j with coefﬁcient matrix j. For such
dependence to be meaningful, j must converge to zero as j →∞. This means
that the k eigenvalues of  must be less than 1 in modulus; otherwise, j will
either explode or converge to a nonzero matrix as j →∞. As a matter of fact, the
requirement that all eigenvalues of  are less than 1 in modulus is the necessary
and sufﬁcient condition for weak stationarity of rt provided that the covariance
matrix of at exists. Notice that this stationarity condition reduces to that of the
univariate AR(1) case in which the condition is |φ| < 1. Furthermore, because
|λI −| = λk | I −1
λ |,
the eigenvalues of  are the inverses of the zeros of the determinant |I −B|.
Thus, an equivalent sufﬁcient and necessary condition for stationarity of rt is that all
zeros of the determinant |(B)| are greater than one in modulus; that is, all zeros are
outside the unit circle in the complex plane. Fourth, using the expression, we have
Cov(rt) =
0 =  + ′ + 2(2)′ + · · · =
∞

i=0
i(i)′,
where it is understood that 0 = I, the k × k identity matrix.
--- page 430 ---

vector autoregressive models
403
Postmultiplying ˜r′
t−ℓto Eq. (8.11), taking expectation, and using the result
Cov(at, rt−j) = E(at ˜r′
t−j) = 0 for j > 0, we obtain
E(˜rt ˜r′
t−ℓ) = E(˜rt−1˜rt−ℓ)′,
ℓ> 0.
Therefore,

ℓ= 
ℓ−1,
ℓ> 0,
(8.12)
where
j is the lag-j cross-covariance matrix of rt. Again this result is a generalization of that of a univariate AR(1) process. By repeated substitutions, Eq. (8.12)
shows that

ℓ= ℓ
0,
for
ℓ>0.
Preand postmultiplying Eq. (8.12) by D−1/2, we obtain
ρℓ= D−1/2
ℓ−1D−1/2 = D−1/2D1/2D−1/2
ℓ−1D−1/2 = ϒρℓ−1,
where ϒ = D−1/2D1/2. Consequently, the CCM of a VAR(1) model satisﬁes
ρℓ= ϒℓρ0,
for
ℓ>0.
8.2.3
Vector AR(p) Models
The generalization of VAR(1) to VAR(p) models is straightforward. The time series
rt follows a VAR(p) model if it satisﬁes
rt = φ0 + 1rt−1 + · · · + prt−p + at,
p>0,
(8.13)
where φ0 and at are deﬁned as before, and j are k × k matrices. Using the
back-shift operator B, the VAR(p) model can be written as
(I −1B −· · · −pBp)rt = φ0 + at,
where I is the k × k identity matrix. This representation can be written in a compact
form as
(B)rt = φ0 + at,
where (B) = I −1B −· · · −pBp is a matrix polynomial. If rt is weakly
stationary, then we have
µ = E(rt) = (I −1 −· · · −p)−1φ0 = [(1)]−1φ0
--- page 431 ---

404
multivariate time series analysis and its applications
provided that the inverse exists. Let ˜rt = rt −µ. The VAR(p) model becomes
˜rt = 1˜rt−1 + · · · + p ˜rt−p + at.
(8.14)
Using this equation and the same techniques as those for VAR(1) models, we
obtain that
• Cov(rt, at) = , the covariance matrix of at.
• Cov(rt−ℓ, at) = 0 for ℓ> 0.
•
ℓ= 1
ℓ−1 + · · · + p
ℓ−p for ℓ> 0.
The last property is called the moment equations of a VAR(p) model. It is a
multivariate version of the Yule–Walker equation of a univariate AR(p) model. In
terms of CCM, the moment equations become
ρℓ= ϒ1ρℓ−1 + · · · + ϒpρℓ−p
for ℓ>0,
where ϒi = D−1/2iD1/2.
A simple approach to understanding properties of the VAR(p) model in Eq.
(8.13) is to make use of the results of the VAR(1) model in Eq. (8.8). This can be
achieved by transforming the VAR(p) model of rt into a kp-dimensional VAR(1)
model. Speciﬁcally, let xt = (˜r′
t−p+1, ˜r′
t−p+2, . . . , ˜r′
t)′ and bt = (0, . . . , 0, a′
t)′ be
two kp-dimensional processes. The mean of bt is zero and the covariance matrix
of bt is a kp × kp matrix with zero everywhere except for the lower right corner,
which is . The VAR(p) model for rt can then be written in the form
xt = ∗xt−1 + bt,
(8.15)
where ∗is a kp × kp matrix given by
∗=


0
I
0
0
· · ·
0
0
0
I
0
· · ·
0
...
...
...
...
0
0
0
0
· · ·
I
p
p−1
p−2
p−3
· · ·
1


,
where 0 and I are the k × k zero matrix and identity matrix, respectively. In
the literature, ∗is called the companion matrix of the matrix polynomial
(B).
Equation (8.15) is a VAR(1) model for xt, which contains rt as its last k components. The results of a VAR(1) model shown in the previous section can now be
used to derive properties of the VAR(p) model via Eq. (8.15). For example, from
the deﬁnition, xt is weakly stationary if and only if rt is weakly stationary. Therefore, the necessary and sufﬁcient condition of weak stationarity for the VAR(p)
--- page 432 ---

vector autoregressive models
405
model in Eq. (8.13) is that all eigenvalues of ∗in Eq. (8.15) are less than 1 in
modulus. It is easy to show that |I −∗B| = |(B)|. Therefore, similar to the
VAR(1) case, the necessary and sufﬁcient condition is equivalent to all zeros of
the determinant |(B)| being outside the unit circle.
Of particular relevance to ﬁnancial time series analysis is the structure of the
coefﬁcient matrices ℓof a VAR(p) model. For instance, if the (i, j)th element
ij(ℓ) of ℓis zero for all ℓ, then rit does not depend on the past values of rjt. The
structure of the coefﬁcient matrices ℓthus provides information on the lead–lag
relationship between the components of rt.
8.2.4
Building a VAR(p) Model
We continue to use the iterative procedure of order speciﬁcation, estimation, and
model checking to build a vector AR model for a given time series. The concept of
partial autocorrelation function of a univariate series can be generalized to specify
the order p of a vector series. Consider the following consecutive VAR models:
rt = φ0 + 1rt−1 + at
rt = φ0 + 1rt−1 + 2rt−2 + at
...
rt = φ0 + 1rt−1 + · · · + irt−i + at
(8.16)
...
Parameters of these models can be estimated by the ordinary least-squares (OLS)
method. This is called the multivariate linear regression estimation in multivariate
statistical analysis; see Johnson and Wichern (1998).
For the ith equation in Eq. (8.16), let 
(i)
j
be the OLS estimate of j and φ
(i)
0
be the estimate of φ0, where the superscript (i) is used to denote that the estimates
are for a VAR(i) model. Then the residual is
a(i)
t
= rt −φ
(i)
0 −
(i)
1 rt−1 −· · · −
(i)
i rt−i.
For i = 0, the residual is deﬁned as r(0)
t
= rt −¯r, where ¯r is the sample mean of
rt. The residual covariance matrix is deﬁned as
i =
1
T −2i −1
T

t=i+1
a(i)
t (a(i)
t )′,
i ≥0.
(8.17)
To specify the order p, one can test the hypothesis H0 : ℓ= 0 versus the alternative hypothesis Ha : ℓ̸ = 0 sequentially for ℓ= 1, 2, . . .. For example, using
--- page 433 ---

406
multivariate time series analysis and its applications
the ﬁrst equation in Eq. (8.16), we can test the hypothesis H0 : 1 = 0 versus the
alternative hypothesis Ha : 1̸ = 0. The test statistic is
M(1) = −

T −k −5
2

ln

|1|
|0|

,
where i is deﬁned in Eq. (8.17) and |A| denotes the determinant of the matrix
A. Under some regularity conditions, the test statistic M(1) is asymptotically a
chi-squared distribution with k2 degrees of freedom; see Tiao and Box (1981).
In general, we use the ith and (i −1)th equations in Eq. (8.16) to test H0 : i =
0 versus Ha : i̸ = 0; that is, testing a VAR(i) model versus a VAR(i −1) model.
The test statistic is
M(i) = −

T −k −i −3
2

ln

|i|
|i−1|

.
(8.18)
Asymptotically, M(i) is distributed as a chi-squared distribution with k2 degrees
of freedom.
Alternatively, one can use the Akaike information criterion (AIC) or its variants
to select the order p. Assume that at is multivariate normal and consider the ith
equation in Eq. (8.16). One can estimate the model by the maximum-likelihood
(ML) method. For AR models, the OLS estimates φ0 and j are equivalent to the
(conditional) ML estimates. However, there are differences between the estimates
of . The ML estimate of  is
˜i = 1
T
T

t=i+1
a(i)
t [a(i)
t ]′.
(8.19)
The AIC of a VAR(i) model under the normality assumption is deﬁned as
AIC(i) = ln(| ˜i|) + 2k2i
T
.
For a given vector time series, one selects the AR order p such that AIC(p) =
min0≤i≤p0 AIC(i), where p0 is a prespeciﬁed positive integer.
Other information criteria available for VAR(i) models are
BIC(i) = ln(| ˜i|) + k2i ln(T )
T
,
HQ(i) = ln(| ˜i|) + 2k2i ln[ln(T )]
T
.
The HQ criterion is proposed by Hannan and Quinn (1979).
--- page 434 ---

vector autoregressive models
407
Example 8.4.
Assuming that the bivariate series of monthly log returns of IBM
stock and the S&P 500 index discussed in Example 8.1 follows a VAR model, we
apply the M(i) statistics and AIC to the data. Table 8.3 shows the results of these
statistics. Both statistics indicate that a VAR(5) model might be adequate for the
data. The M(i) statistics are marginally signiﬁcant at lags 1, 3, and 5 at the 5%
level. The minimum of AIC occurs at order 5. For this particular instance, the M(i)
statistic is only marginally signiﬁcant at the 1% level when i = 2, conﬁrming the
previous observation that the dynamic linear dependence between the two return
series is weak.
Estimation and Model Checking
For a speciﬁed VAR model, one can estimate the parameters using either the OLS
method or the ML method. The two methods are asymptotically equivalent. Under
some regularity conditions, the estimates are asymptotically normal; see Reinsel
(1993). A ﬁtted model should then be checked carefully for any possible inadequacy. The Qk(m) statistic can be applied to the residual series to check the
assumption that there are no serial or cross correlations in the residuals. For a
ﬁtted VAR(p) model, the Qk(m) statistic of the residuals is asymptotically a chisquared distribution with k2m −g degrees of freedom, where g is the number of
estimated parameters in the AR coefﬁcient matrices; see L¨utkepohl (2005).
Example 8.4 (Continued).
Table 8.4(a) shows the estimation results of a
VAR(5) model for the bivariate series of monthly log returns of IBM stock and the
S&P 500 index. The speciﬁed model is in the form
rt = φ0 + 1rt−1 + 2rt−2 + 3rt−3 + 5rt−5 + at,
(8.20)
where the ﬁrst component of rt denotes IBM stock returns. For this particular
instance, we do not use AR coefﬁcient matrix at lag 4 because of the weak serial
dependence of the data. In general, when the M(i) statistics and the AIC criterion
specify a VAR(5) model, all ﬁve AR lags should be used. Table 8.4(b) shows the
estimation results after some statistically insigniﬁcant parameters are set to zero.
The Qk(m) statistics of the residual series for the ﬁtted model in Table 8.4(b)
give Q2(4) = 16.64 and Q2(8) = 31.55. Since the ﬁtted VAR(5) model has six
parameters in the AR coefﬁcient matrices, these two Qk(m) statistics are distributed
asymptotically as a chi-squared distribution with degrees of freedom 10 and 26,
TABLE 8.3
Order Speciﬁcation Statistics for Monthly Log Returns of IBM Stock
and S&P 500 Index from January 1926 to December 2008a
Order
1
2
3
4
5
6
M(i)
10.76
13.41
10.34
7.78
12.07
1.93
AIC
6.795
6.789
6.786
6.786
6.782
6.788
aThe 5% and 1% critical values of a chi-squared distribution with 4 degrees of freedom are 9.5 and 13.3.
--- page 435 ---

408
multivariate time series analysis and its applications
respectively. The p-values of the test statistics are 0.083 and 0.208, and hence the
ﬁtted model is adequate at the 5% signiﬁcance level. As shown by the univariate
analysis, the return series are likely to have conditional heteroscedasticity. We
discuss multivariate volatility in Chapter 10.
From the ﬁtted model in Table 8.4(b), we make the following observations:
(a) The concurrent correlation coefﬁcient between the two innovational series is
24/
√
48 × 30 = 0.63, which, as expected, is close to the sample correlation coefﬁ-
cient between r1t and r2t. (b) The two log return series have positive and signiﬁcant
means, implying that the log prices of the two series had an upward trend over the
data span. (c) The model shows that
IBMt = 1.0 + 0.13SP5t−1 −0.09SP5t−2 + 0.09SP5t−5 + a1t,
SP5t = 0.4 + 0.08SP5t−1 −0.06SP5t−3 + 0.09SP5t−5 + a2t.
Consequently, at the 5% signiﬁcance level, there is a unidirectional dynamic relationship from the monthly S&P 500 index return to the IBM return. If the S&P
500 index represents the U.S. stock market, then IBM return is affected by the past
movements of the market. However, past movements of IBM stock returns do not
signiﬁcantly affect the U.S. market, even though the two returns have substantial
concurrent correlation. Finally, the ﬁtted model can be written as

 IBMt
SP5t

=

 1.0
0.4

+

 0.13
0.08

SP5t−1 −

 0.09
0

SP5t−2 −

0
0.06

SP5t−3
+

 0.09
0.09

SP5t−5 +

 a1t
a2t

,
indicating that SP5t is the driving factor of the bivariate series.
TABLE 8.4
Estimation Results of a VAR(5) Model for the Monthly Log Returns, in
Percentages, of IBM Stock and S&P 500 Index from January 1926 to December 2008
Parameter
φ0
1
2
3
5

(a) Full Model
Estimate
1.0
−0.03
0.15
0.10
−0.17
0.05
−0.11
−0.06
0.14
48
24
0.4
−0.03
0.11
0.04
−0.04
0.02
−0.11
−0.07
0.15
24
30
Standard
error
0.23
0.04
0.05
0.04
0.05
0.04
0.05
0.04
0.05
0.18
0.03
0.04
0.03
0.04
0.03
0.04
0.03
0.04
(b) Simpliﬁed Model
Estimate
1.0
0
0.13
0
−0.09
0
0
0
0.09
48
24
0.4
0
0.08
0
0
0
−0.06
0
0.09
24
30
Standard
error
0.22
−
0.04
−
0.03
−
−
−
0.04
0.18
−
0.03
−
−
−
−0.06
−
0.03
--- page 436 ---

vector autoregressive models
409
Forecasting
Treating a properly built model as the true model, one can apply the same techniques
as those in the univariate analysis to produce forecasts and standard deviations of
the associated forecast errors. For a VAR(p) model, the 1-step-ahead forecast at the
time origin h is rh(1) = φ0 + p
i=1 irh+1−i, and the associated forecast error is
eh(1) = ah+1. The covariance matrix of the forecast error is . For 2-step-ahead
forecasts, we substitute rh+1 by its forecast to obtain
rh(2) = φ0 + 1rh(1) +
p

i=2
irh+2−i,
and the associated forecast error is
eh(2) = ah+2 + 1[rt −rh(1)] = ah+2 + 1ah+1.
The covariance matrix of the forecast error is  + 1′
1. If rt is weakly stationary, then the ℓ-step-ahead forecast rh(ℓ) converges to its mean vector µ as
the forecast horizon ℓincreases and the covariance matrix of its forecast error
converges to the covariance matrix of rt.
Table 8.5 provides 1-stepto 6-step-ahead forecasts of the monthly log returns,
in percentages, of IBM stock and the S&P 500 index at the forecast origin h =
996. These forecasts are obtained by the reﬁned VAR(5) model in Table 8.4(b).
As expected, the standard errors of the forecasts converge to the sample standard
errors 7.03 and 5.53, respectively, for the two log return series.
In summary, building a VAR model involves three steps: (a) Use the test statistic
M(i) or some information criterion to identify the order, (b) estimate the speciﬁed
model by using the least-squares method and, if necessary, reestimate the model
by removing statistically insigniﬁcant parameters, and (c) use the Qk(m) statistic
of the residuals to check the adequacy of a ﬁtted model. Other characteristics of
the residual series, such as conditional heteroscedasticity and outliers, can also be
checked. If the ﬁtted model is adequate, then it can be used to obtain forecasts and
make inference concerning the dynamic relationship between the variables.
We used SCA to perform the analysis in this section. The commands used include
miden, mtsm, mest, and mfore, where the preﬁx m stands for multivariate. Details
of the commands and output are shown below.
TABLE 8.5
Forecasts of a VAR(5) Model for Monthly Log Returns, in Percentages,
of IBM Stock and S&P 500 Index: Forecast Origin Is December 2008
Step
1
2
3
4
5
6
IBM forecast
1.95
0.30
−0.82
0.14
1.16
1.29
Standard error
6.95
6.99
7.00
7.00
7.00
7.00
SP forecast
1.70
0.17
−1.26
−0.49
0.41
0.65
Standard error
5.48
5.50
5.50
5.51
5.51
5.53
--- page 437 ---

410
multivariate time series analysis and its applications
SCA Demonstration
Output has been edited and % denotes explanation in the following:
input date, ibm, sp5. file ‘m-ibmsp2608.txt’.
--% compute percentage log returns.
ibm=ln(ibm+1)*100
--
sp5=ln(sp5+1)*100
--% model identification
miden ibm,sp5. arfits 1 to 12.
TIME PERIOD ANALYZED . . . . . . . . . . . .
1
TO
996
EFFECTIVE NUMBER OF OBSERVATIONS (NOBE). . .
996
SERIES
NAME
MEAN
STD. ERROR
1
IBM
1.0891
7.0298
2
SP5
0.4301
5.5346
NOTE: THE APPROX. STD. ERROR FOR THE ESTIMATED CORRELA-
TIONS BELOW
IS (1/NOBE**.5) =
0.03169
SAMPLE CORRELATION MATRIX OF THE SERIES
1.00
0.65
1.00
SUMMARIES OF CROSS CORRELATION MATRICES USING +,-,., WHERE
+ DENOTES A VALUE GREATER THAN 2/SQRT(NOBE)
- DENOTES A VALUE LESS THAN -2/SQRT(NOBE)
. DENOTES A NON-SIGNIFICANT VALUE BASED ON THE ABOVE
CRITERION
CROSS CORRELATION MATRICES IN TERMS OF +,-,.
LAGS
1 THROUGH
6
. +
. -
. .
. .
. +
. .
. +
. .
. -
. .
. +
. .
LAGS
7 THROUGH 12
. .
+ .
. .
. .
. .
. .
. .
+ .
. +
. .
. .
. .
========
STEPWISE AUTOREGRESSION SUMMARY
========
--------------------------------------------------------------
I RESIDUAL I EIGENVAL.I CHI-SQ
I
I SIGN.
LAG I VARIANCESI OF SIGMA I
TEST
I
AIC
I PAR. AR
----+----------+----------+---------+----------+--------------
1 I .492E+02 I .133E+02 I
10.76 I
6.795 I . +
I .306E+02 I .665E+02 I
I
I . +
----+----------+----------+---------+----------+--------------
2 I .486E+02 I .133E+02 I
13.41 I
6.789 I + -
--- page 438 ---

vector autoregressive models
411
I .306E+02 I .659E+02 I
I
I . .
----+----------+----------+---------+----------+--------------
3 I .484E+02 I .132E+02 I
10.34 I
6.786 I . .
I .303E+02 I .655E+02 I
I
I . -
----+----------+----------+---------+----------+--------------
4 I .484E+02 I .131E+02 I
7.78 I
6.786 I . .
I .302E+02 I .655E+02 I
I
I . .
----+----------+----------+---------+----------+--------------
5 I .480E+02 I .131E+02 I
12.07 I
6.782 I . +
I .299E+02 I .648E+02 I
I
I - +
----+----------+----------+---------+----------+--------------
6 I .479E+02 I .131E+02 I
1.93 I
6.788 I . .
I .298E+02 I .647E+02 I
I
I . .
----+----------+----------+---------+----------+--------------
7 I .479E+02 I .130E+02 I
2.68 I
6.793 I . .
I .298E+02 I .647E+02 I
I
I . .
----+----------+----------+---------+----------+--------------
8 I .477E+02 I .130E+02 I
7.09 I
6.794 I . .
I .296E+02 I .643E+02 I
I
I . .
----+----------+----------+---------+----------+--------------
9 I .476E+02 I .130E+02 I
5.23 I
6.797 I . .
I .295E+02 I .642E+02 I
I
I . .
----+----------+----------+---------+----------+--------------
10 I .476E+02 I .130E+02 I
1.43 I
6.803 I . .
I .295E+02 I .641E+02 I
I
I . .
----+----------+----------+---------+----------+--------------
11 I .475E+02 I .130E+02 I
1.81 I
6.809 I . .
I .294E+02 I .640E+02 I
I
I . .
----+----------+----------+---------+----------+--------------
12 I .475E+02 I .129E+02 I
1.88 I
6.815 I . .
I .294E+02 I .640E+02 I
I
I . .
----+----------+----------+---------+----------+--------------
NOTE:CHI-SQUARED CRITICAL VALUES WITH 4 DEGREES OF FREEDOM ARE
5 PERCENT:
9.5
1 PERCENT:
13.3
-- % model specification of a VAR(5) model without lag 4.
mtsm m1. series ibm, sp5. model @
(i-p2*b-p2*b**2-p3*b**3-p5*b**5)series=c+noise.
-- % estimation
mestim m1. hold resi(r1,r2).
-- % demonstration of setting zero constraint
p2(2,2)=0
--
cp2(2,2)=1
--
p3(1,2)=0
--
cp3(1,2)=1
--
mestim m1. hold resi(r1,r2)
