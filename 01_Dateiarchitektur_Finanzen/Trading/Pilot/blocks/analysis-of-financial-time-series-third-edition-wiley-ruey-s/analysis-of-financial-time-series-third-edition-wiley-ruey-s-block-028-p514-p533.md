# Analysis of Financial Time Series, Third Edition (Wiley -- Ruey S_ Tsay -- Wiley series in probability and statistics, 3rd ed_, -- John Wiley & Sons, -- isbn13 9780470414354 -- 9f99b80c7b2dedd477f463dc5323f3b6 -- An.pdf — pages 514–533

--- page 514 ---

principal component analysis
487
TABLE 9.3
Results of Principal Component Analysis for Monthly Log Returns,
Including Dividends of Stocks of IBM, Hewlett-Packard, Intel, J.P. Morgan Chase,
and Bank of America from January 1990 to December 2008a
Using Sample Covariance Matrix
Eigenvalue
284.17
112.93
57.43
46.81
29.87
Proportion
0.535
0.213
0.108
0.088
0.056
Cumulative
0.535
0.748
0.856
0.944
1.000
Eigenvector
0.330
0.139
−0.264
0.895
−0.014
0.483
0.279
−0.701
−0.430
−0.116
0.581
0.478
0.652
−0.096
−0.016
0.448
−0.550
0.013
−0.064
0.702
0.347
−0.610
0.119
−0.009
−0.702
Using Sample Correlation Matrix
Eigenvalue
2.607
1.072
0.569
0.451
0.301
Proportion
0.522
0.214
0.114
0.090
0.060
Cumulative
0.522
0.736
0.850
0.940
1.000
Eigenvector
0.428
0.341
0.837
−0.002
0.008
0.460
0.356
−0.380
0.704
0.145
0.451
0.385
−0.389
−0.704
0.022
0.479
−0.469
−0.046
0.052
−0.739
0.416
−0.623
0.035
−0.073
0.658
aThe eigenvectors are in columns.
explained by the principal components. Consider the correlation matrix and denote
the sample eigenvalues and eigenvectors by ˆλi and ei. We have
ˆλ1 = 2.608,
e1 = (0.428, 0.460, 0.451, 0.479, 0.416)′,
ˆλ2 = 1.072,
e2 = (0.341, 0.356, 0.385, −0.469, −0.623)′
for the ﬁrst two principal components. These two components explain about 74%
of the total variability of the data, and they have interesting interpretations. The ﬁrst
component is a roughly equally weighted linear combination of the stock returns.
This component might represent the general movement of the stock market and
hence is a market component. The second component represents the difference
between the two industrial sectors—namely, technologies versus ﬁnancial services.
It might be an industrial component. Similar interpretations of principal components
can also be found by using the covariance matrix of r.
An informal but useful procedure to determine the number of principal components needed in an application is to examine the scree plot, which is the time plot of
the eigenvalues ˆλi ordered from the largest to the smallest (i.e., a plot of ˆλi versus
i). Figure 9.5(a) shows the scree plot for the ﬁve stock returns of Example 9.1. By
looking for an elbow in the scree plot, indicating that the remaining eigenvalues
--- page 515 ---

488
principal component analysis and factor models
Component
(a)
(b)
Eigenvalue
1
2
3
4
5
0.5
1.0
1.5
2.0
2.5
Component
Eigenvalue
1
2
3
4
5
0
1
2
3
4
Figure 9.5
Scree plots for two 5-dimensional asset returns: (a) series of Example 9.1 and (b) bond
index returns of Example 9.3.
are relatively small and all about the same size, one can determine the appropriate
number of components. For both plots in Figure 9.5, two components appear to be
appropriate. Finally, except for the case in which λj = 0 for j > i, selecting the
ﬁrst i principal components only provides an approximation to the total variance
of the data. If a small i can provide a good approximation, then the simpliﬁcation
becomes valuable.
Remark.
The R and S-Plus commands used to perform the PCA are given
below. The command princomp gives the square root of the eigenvalue and
denotes it as standard deviation.
> rtn=read.table(‘‘m-5clog-9008.txt’’),header=T)
> pca.cov = princomp(rtn)
> names(pca.cov)
> summary(pca.cov)
> pca.cov$loadings
> screeplot(pca.cov)
> pca.corr=princomp(rtn,cor=T)
> summary(pac.corr)
□
--- page 516 ---

statistical factor analysis
489
9.5
STATISTICAL FACTOR ANALYSIS
We now turn to statistical factor analysis. One of the main difﬁculties in multivariate statistical analysis is the “curse of dimensionality.” For serially correlated
data, the number of parameters of a parametric model often increases dramatically
when the order of the model or the dimension of the time series is increased. Simplifying methods are often sought to overcome the curse of dimensionality. From
an empirical viewpoint, multivariate data often exhibit similar patterns indicating
the existence of common structure hidden in the data. Statistical factor analysis is
one of those simplifying methods available in the literature. The aim of statistical
factor analysis is to identify, from the observed data, a few factors that can account
for most of the variations in the covariance or correlation matrix of the data.
Traditional statistical factor analysis assumes that the data have no serial correlations. This assumption is often violated by ﬁnancial data taken with frequency
less than or equal to a week. However, the assumption appears to be reasonable
for asset returns with lower frequencies (e.g., monthly returns of stocks or market
indexes). If the assumption is violated, then one can use the parametric models
discussed in this book to remove the linear dynamic dependence of the data and
apply factor analysis to the residual series.
In what follows, we discuss statistical factor analysis based on the orthogonal
factor model. Consider the return rt = (r1t, . . . , rkt)′ of k assets at time period t and
assume that the return series rt is weakly stationary with mean µ and covariance
matrix r. The statistical factor model postulates that rt is linearly dependent on
a few unobservable random variables f t = (f1t, . . . , fmt)′ and k additional noises
ϵt = (ϵ1t, . . . , ϵkt)′. Here m < k, fit are the common factors, and ϵit are the errors.
Mathematically, the statistical factor model is also in the form of Eq. (9.1) except
that the intercept α is replaced by the mean return µ. Thus, a statistical factor
model is in the form
rt −µ = βf t + ϵt,
(9.16)
where β = [βij]k×m is the matrix of factor loadings, βij is the loading of the ith
variable on the jth factor, and ϵit is the speciﬁc error of rit. A key feature of
the statistical factor model is that the m factors fit and the factor loadings βij are
unobservable. As such, Eq. (9.16) is not a multivariate linear regression model,
even though it has a similar appearance. This special feature also distinguishes a
statistical factor model from other factor models discussed earlier.
The factor model in Eq. (9.16) is an orthogonal factor model if it satisﬁes the
following assumptions:
1. E(f t) = 0 and Cov(f t) = I m, the m × m identity matrix.
2. E(ϵt) = 0 and Cov(ϵt) = D = diag{σ 2
1 , . . . , σ 2
k } (i.e., D is a k × k diagonal
matrix).
3. f t and ϵt are independent so that Cov(f t, ϵt) = E(f tϵ′
t) = 0m×k.
--- page 517 ---

490
principal component analysis and factor models
Under the previous assumptions, it is easy to see that
r = Cov(rt) = E[(rt −µ)(rt −µ)′]
= E[(βf t + ϵt)(βf t + ϵt)′]
= ββ′ + D
(9.17)
and
Cov(rt, f t) = E[(rt −µ)f ′
t] = βE(f tf ′
t) + E(ϵtf ′
t) = β.
(9.18)
Using Eqs. (9.17) and (9.18), we see that for the orthogonal factor model in Eq.
(9.16)
Var(rit) = β2
i1 + · · · + β2
im + σ 2
i ,
Cov(rit, rjt) = βi1βj1 + · · · + βimβjm,
Cov(rit, fjt) = βij.
The quantity β2
i1 + · · · + β2
im, which is the portion of the variance of rit contributed
by the m common factors, is called the communality. The remaining portion σ 2
i
of the variance of rit is called the uniqueness or speciﬁc variance. Let c2
i = β2
i1 +
· · · + β2
im be the communality, which is the sum of squares of the loadings of the
ith variable on the m common factors. The variance of component rit becomes
Var(rit) = c2
i + σ 2
i .
In practice, not every covariance matrix has an orthogonal factor representation.
In other words, there exists a random variable rt that does not have any orthogonal
factor representation. Furthermore, the orthogonal factor representation of a random
variable is not unique. In fact, for any m × m orthogonal matrix P satisfying P P ′
= P ′P = I, let β∗= βP and f ∗
t = P ′f t. Then
rt −µ = βf t + ϵt = βP P ′f t + ϵt = β∗f ∗
t + ϵt.
In addition, E(f ∗
t ) = 0 and Cov(f ∗
t ) = P ′Cov(f t)P = P ′P = I. Thus, β∗and
f ∗
t form another orthogonal factor model for rt. This nonuniqueness of orthogonal
factor representation is a weakness as well as an advantage for factor analysis. It
is a weakness because it makes the meaning of factor loading arbitrary. It is an
advantage because it allows us to perform rotations to ﬁnd common factors that
have nice interpretations. Because P is an orthogonal matrix, the transformation
f ∗
t = P ′f t is a rotation in the m-dimensional space.
9.5.1
Estimation
The orthogonal factor model in Eq. (9.16) can be estimated by two methods.
The ﬁrst estimation method uses the principal component analysis of the previous section. This method does not require the normality assumption of the data nor
--- page 518 ---

statistical factor analysis
491
the prespeciﬁcation of the number of common factors. It applies to both the covariance and correlation matrices. But as mentioned in PCA, the solution is often an
approximation. The second estimation method is the maximum-likelihood method
that uses normal density and requires a prespeciﬁcation for the number of common
factors.
Principal Component Method
Again let (ˆλ1,e1), . . . , (ˆλk,ek) be pairs of the eigenvalues and eigenvectors of the
sample covariance matrix r, where ˆλ1 ≥ˆλ2 ≥· · · ≥ˆλk. Let m < k be the number
of common factors. Then the matrix of factor loadings is given by
β ≡[ ˆβij] =


ˆλ1e1 |

ˆλ2e2 | · · · |

ˆλmem

.
(9.19)
The estimated speciﬁc variances are the diagonal elements of the matrix r −ββ
′.
That is, 
D = diag{ˆσ 2
1 , . . . , ˆσ 2
k }, where ˆσ 2
i = ˆσii,r −m
j=1 ˆβ2
ij, where ˆσii,r is the
(i, i)th element of r. The communalities are estimated by
ˆc2
i = ˆβ2
i1 + · · · + ˆβ2
im.
The error matrix caused by approximation is
r −(ββ
′ + 
D).
Ideally, we would like this matrix to be close to zero. It can be shown that the
sum of squared elements of r −(ββ
′ + 
D) is less than or equal to ˆλ2
m+1 + · · · +
ˆλ2
k. Therefore, the approximation error is bounded by the sum of squares of the
neglected eigenvalues.
From the solution in Eq. (9.19), the estimated factor loadings based on the
principal component method do not change as the number of common factors m
is increased.
Maximum-Likelihood Method
If the common factors f t and the speciﬁc factors ϵt are jointly normal, then rt
is multivariate normal with mean µ and covariance matrix r = ββ′ + D. The
maximum-likelihood method can then be used to obtain estimates of β and D under
the constraint β′D−1β = , which is a diagonal matrix. Here µ is estimated by
the sample mean. For more details of this method, readers are referred to Johnson
and Wichern (2007).
In using the maximum-likelihood method, the number of common factors must
be given a priori. In practice, one can use a modiﬁed likelihood ratio test to check
the adequacy of a ﬁtted m-factor model. The test statistic is
LR(m) = −
0
T −1 −1
6(2k + 5) −2
3m
1 
ln |r| −ln |ββ
′ + 
D|

,
(9.20)
--- page 519 ---

492
principal component analysis and factor models
which, under the null hypothesis of m factors, is asymptotically distributed as a
chi-squared distribution with 1
2[(k −m)2 −k −m] degrees of freedom. We discuss
some methods for selecting m in Section 9.6.1.
9.5.2
Factor Rotation
As mentioned before, for any m × m orthogonal matrix P ,
rt −µ = βf t + ϵt = β∗f ∗
t + ϵt,
where β∗= βP and f ∗
t = P ′f t. In addition,
ββ′ + D = βP P ′β′ + D = β∗(β∗)′ + D.
This result indicates that the communalities and the speciﬁc variances remain
unchanged under an orthogonal transformation. It is then reasonable to ﬁnd an
orthogonal matrix P to transform the factor model so that the common factors
have nice interpretations. Such a transformation is equivalent to rotating the common factors in the m-dimensional space. In fact, there are inﬁnite possible factor
rotations available. Kaiser (1958) proposes a varimax criterion to select the rotation
that works well in many applications. Denote the rotated matrix of factor loadings
by β∗= [β∗
ij] and the ith communality by c2
i . Deﬁne ˜β∗
ij = β∗
ij/ci to be the rotated
coefﬁcients scaled by the (positive) square root of communalities. The varimax
procedure selects the orthogonal matrix P that maximizes the quantity
V = 1
k
m

j=1


k

i=1
( ˜β∗
ij)4 −1
k
 k

i=1
˜β∗2
ij
2
.
This complicated expression has a simple interpretation. Maximizing V corresponds
to spreading out the squares of the loadings on each factor as much as possible.
Consequently, the procedure is to ﬁnd groups of large and negligible coefﬁcients
in any column of the rotated matrix of factor loadings. In a real application, factor
rotation is used to aid the interpretations of common factors. It may be helpful in
some applications, but not informative in others. There are many criteria available
for factor rotation.
9.5.3
Applications
Given the data {rt} of asset returns, the statistical factor analysis enables us to
search for common factors that explain the variabilities of the returns. Since factor
analysis assumes no serial correlations in the data, one should check the validity of
this assumption before using factor analysis. The multivariate portmanteau statistics
can be used for this purpose. If serial correlations are found, one can build a
VARMA model to remove the dynamic dependence in the data and apply the factor
--- page 520 ---

statistical factor analysis
493
analysis to the residual series. For many returns series, the correlation matrix of
the residuals of a linear model is often very close to the correlation matrix of the
original data. In this case, the effect of dynamic dependence on factor analysis is
negligible.
We consider three examples in this section. The ﬁrst and third examples use the
R or S-Plus to perform the analysis and the second example uses Minitab. Other
packages can also be used.
Example 9.2.
Consider again the monthly log stock returns of IBM, Hewlett-
Parkard, Intel, J.P. Morgan Chase, and Bank of America used in Example 9.1.
To check the assumption of no serial correlations, we compute the portmanteau
statistics and obtain Q5(1) = 39.99, Q5(5) = 160.60, and Q5(10) = 293.04. Compared with chi-squared distributions with 25, 125, and 250 degrees of freedom, the
p values of these test statistics are 0.029, 0.017, and 0.032, respectively. Therefore,
there exists some minor serial dependence in the returns, but the dependence is not
signiﬁcant at the 1% level. For simplicity, we ignore the serial dependence in factor
analysis.
Table 9.4 shows the results of factor analysis based on the correlation matrix
using the maximum-likelihood method. We assume that the number of common
factors is 2, which is reasonable according to the principal component analysis of
Example 9.1. From the table, the factor analysis reveals several interesting ﬁndings:
• The two factors identiﬁed by the maximum-likelihood method explain about
60% of the variability of the stock returns.
• Based on the rotated factor loadings, the two common factors have some
meaningful interpretations. The technology stocks (IBM, Hewlett-Packard,
TABLE 9.4
Factor Analysis of Monthly Log Stock Returns of IBM,
Hewlett-Packard, Intel, J.P. Morgan Chase, and Bank of Americaa
Estimates of
Rotated
Factor Loadings
Factor Loadings
Communalities
Variable
f1
f2
f ∗
1
f ∗
2
1 −σ 2
i
Maximum-Likelihood Method
IBM
0.327
0.530
0.593
0.189
0.387
HPQ
0.348
0.669
0.733
0.177
0.568
INTC
0.337
0.647
0.709
0.171
0.531
JPM
0.734
0.186
0.358
0.667
0.573
BAC
0.960
−0.111
0.124
0.958
0.934
Variance
1.801
1.193
1.535
1.459
2.994
Proportion
0.360
0.239
0.307
0.292
0.599
aThe returns include dividends and are from January 1990 to December 2008. The analysis is based on
the sample cross-correlation matrix and assumes two common factors.
--- page 521 ---

494
principal component analysis and factor models
and Intel) load heavily on the ﬁrst factor, whereas the ﬁnancial stocks (J.P.
Morgan Chase and Bank of America) load highly on the second factor. These
two rotated factors jointly differentiate the industrial sectors.
• In this particular instance, the varimax rotation seems to alter the ordering of
the two common factors.
• The speciﬁc variance of IBM stock returns is relatively large, indicating that
the stock has its own features that are worth further investigation.
Example 9.3.
In this example, we consider the monthly log returns of U.S.
bond indexes with maturities in 30 years, 20 years, 10 years, 5 years, and 1 year.
The data are described in Example 8.2 but have been transformed into log returns.
There are 696 observations. As shown in Example 8.2, there is serial dependence
in the data. However, removing serial dependence by ﬁtting a VARMA(2,1) model
has hardly any effects on the concurrent correlation matrix. As a matter of fact, the
correlation matrices before and after ﬁtting a VARMA(2,1) model are
ρo =


1.0
0.98
1.0
0.92
0.91
1.0
0.85
0.86
0.90
1.0
0.63
0.64
0.67
0.81
1.0


,
ρ =


1.0
0.98
1.0
0.92
0.92
1.0
0.85
0.86
0.90
1.0
0.66
0.67
0.71
0.84
1.0


,
where ρo is the correlation matrix of the original log returns. Therefore, we apply
factor analysis directly to the return series.
Table 9.5 shows the results of statistical factor analysis of the data. For both
estimation methods, the ﬁrst two common factors explain more than 90% of the
total variability of the data. Indeed, the high communalities indicate that the speciﬁc
variances are very small for the ﬁve bond index returns. Because the results of the
two methods are close, we only discuss that of the principal component method.
The unrotated factor loadings indicate that (a) all ﬁve return series load roughly
equally on the ﬁrst factor, and (b) the loadings on the second factor are positively
correlated with the time to maturity. Therefore, the ﬁrst common factor represents
the general U.S. bond returns, and the second factor shows the “time-to-maturity”
effect. Furthermore, the loadings of the second factor sum approximately to zero.
Therefore, this common factor can also be interpreted as the contrast between
long-term and short-term bonds. Here a long-term bond means one with maturity
10 years or longer. For the rotated factors, the loadings are also interesting. The
loadings for the ﬁrst rotated factor are proportional to the time to maturity, whereas
the loadings of the second factor are inversely proportional to the time to maturity.
--- page 522 ---

statistical factor analysis
495
TABLE 9.5
Factor Analysis of Monthly Log Returns of U.S. Bond Indexes with
Maturities in 30 Years, 20 Years, 10 Years, 5 Years, and 1 Yeara
Estimates of
Rotated
Factor Loadings
Factor Loadings
Communalities
Variable
f1
f2
f ∗
1
f ∗
2
1 −σ 2
i
Principal Component Method
30 years
0.952
0.253
0.927
0.333
0.970
20 years
0.954
0.240
0.922
0.345
0.968
10 years
0.956
0.140
0.866
0.429
0.934
5 years
0.955
−0.142
0.704
0.660
0.931
1 year
0.800
−0.585
0.325
0.936
0.982
Variance
4.281
0.504
3.059
1.726
4.785
Proportion
0.856
0.101
0.612
0.345
0.957
Maximum-Likelihood Method
30 years
0.849
−0.513
0.895
0.430
0.985
20 years
0.857
−0.486
0.876
0.451
0.970
10 years
0.896
−0.303
0.744
0.584
0.895
5 years
1.000
0.000
0.547
0.837
1.000
1 year
0.813
0.123
0.342
0.747
0.675
Variance
3.918
0.607
2.538
1.987
4.525
Proportion
0.784
0.121
0.508
0.397
0.905
aThe data are from January 1942 to December 1999. The analysis is based on the sample crosscorrelation matrix and assumes two common factors.
Example 9.4.
Again, consider the monthly excess returns of the 10 stocks
in Table 9.2. The sample span is from January 1990 to December 2003 and the
returns are in percentages. Our goal here is to demonstrate the use of statistical
factor models using the R or S-Plus command factanal. We started with a twofactor model, but it is rejected by the likelihood ratio test of Eq. (9.20). The test
statistic is LR(2) = 72.96. Based on the asymptotic χ2
26 distribution, p value of
the test statistic is close to zero.
> rtn=read.table(‘‘m-barra-9003.txt’’,header=T)
> stat.fac=factanal(rtn,factors=2,method=’mle’)
> stat.fac
Sums of squares of loadings:
Factor1 Factor2
2.696479 2.19149
Component names:
"loadings" "uniquenesses" "correlation" "criteria"
"factors" "dof" "method" "center" "scale" "n.obs"
"scores" "call"
--- page 523 ---

496
principal component analysis and factor models
We then applied a three-factor model that appears to be reasonable at the 5%
signiﬁcance level. The p value of the LR(3) statistic is 0.0892.
> stat.fac=factanal(rtn,factor=3,method=’mle’)
> stat.fac
Test of the hypothesis that 3 factors are sufficient
versus the alternative that more are required:
The chi square statistic is 26.48 on 18 degrees of freedom.
The p-value is 0.0892
> summary(stat.fac)
Importance of factors:
Factor1
Factor2
Factor3
SS loadings
2.635
1.825
1.326
Proportion Var
0.264
0.183
0.133
Cumulative Var
0.264
0.446
0.579
Uniquenesses:
AGE
C
MWD
MER
DELL
HPQ
IBM
0.479 0.341 0.201 0.216 0.690 0.346 0.638
AA
CAT
PG
0.417 0.000 0.885
Loadings:
Factor1 Factor2 Factor3
AGE
0.678
0.217
0.121
C
0.739
0.259
0.213
MWD
0.817
0.356
MER
0.819
0.329
DELL 0.102
0.547
HPQ
0.230
0.771
IBM
0.200
0.515
0.238
AA
0.194
0.546
0.497
CAT
0.198
0.138
0.970
PG
0.331
The factor loadings can also be shown graphically using
> plot(loadings(stat.fac))
and the plots are in Figure 9.6. From the plots, factor 1 represents essentially the
ﬁnancial service sector, and factor 2 mainly consists of the excess returns from the
high-tech stocks and the Alcoa stock. Factor 3 depends heavily on excess returns
of CAT and AA stocks and, hence, represents the remaining industrial sector.
Factor rotation can be obtained using the command rotate, which allows for
many rotation methods, and factor realizations are available from the command
predict.
--- page 524 ---

statistical factor analysis
497
MER
MWD
C
AGE
PG
HPQ
0.0 0.2 0.4 0.6 0.8
Factor1
HPQ
DELL
AA
IBM
MWD
MER
0.0 0.2 0.4 0.6 0.8
Factor2
CAT
AA
IBM
C
AGE
HPQ
0.0 0.2 0.4 0.6 0.8 1.0
Factor3
Figure 9.6
Plots of factor loadings when a 3-factor statistical factor model is ﬁtted to 10 monthly
excess stock returns in Table 9.2.
> stat.fac2 = rotate(stat.fac,rotation=’quartimax’)
> loadings(stat.fac2)
Factor1 Factor2 Factor3
AGE
0.700
0.171
C
0.772
0.216
0.124
MWD
0.844
0.291
MER
0.844
0.264
DELL 0.144
0.536
HPQ
0.294
0.753
IBM
0.258
0.518
0.164
AA
0.278
0.575
0.418
CAT
0.293
0.219
0.931
PG
0.334
> factor.real=predict(stat.fac,type=’weighted.ls’)
Finally, we obtained the correlation matrix of the 10 excess returns based on the
ﬁtted three-factor statistical factor model. As expected, the correlations are closer to
their sample counterparts than those of the industrial factor model in Section 9.3.1.
--- page 525 ---

498
principal component analysis and factor models
One can also use GMVP to compare the covariance matrices of the returns and the
statistical factor model.
> corr.fit=fitted(stat.fac)
> print(corr.fit,digits=1,width=2)
AGE
C
MWD MER DELL HPQ IBM AA
CAT PG
AGE
1.0 0.6 0.6 0.6 0.19 0.3 0.3 0.3 0.3 0.2
C
0.6 1.0 0.7 0.7 0.22 0.4 0.3 0.4 0.4 0.3
MWD
0.6 0.7 1.0 0.8 0.28 0.5 0.4 0.4 0.3 0.3
MER
0.6 0.7 0.8 1.0 0.26 0.5 0.4 0.4 0.3 0.3
DELL 0.2 0.2 0.3 0.3 1.00 0.5 0.3 0.3 0.1 0.0
HPQ
0.3 0.4 0.5 0.4 0.45 1.0 0.5 0.5 0.2 0.1
IBM
0.3 0.3 0.4 0.3 0.31 0.5 1.0 0.4 0.3 0.1
AA
0.3 0.4 0.4 0.4 0.33 0.5 0.4 1.0 0.6 0.1
CAT
0.3 0.4 0.3 0.3 0.11 0.2 0.3 0.6 1.0 0.1
PG
0.2 0.3 0.3 0.3 0.03 0.1 0.1 0.1 0.1 1.0
9.6
ASYMPTOTIC PRINCIPAL COMPONENT ANALYSIS
So far, our discussion of PCA assumes that the number of assets is smaller than the
number of time periods, that is, k < T . To deal with situations of a small T and
large k, Conner and Korajczyk (1986, 1988) developed the concept of asymptotic
principal component analysis (APCA), which is similar to the traditional PCA but
relies on the asymptotic results as the number of assets k increases to inﬁnity. Thus,
the APCA is based on eigenvalue–eigenvector analysis of the T × T matrix
T = 1
k (R −1T ¯r′)(R −1T ¯r′)′,
where 1T is the T -dimensional vector of ones and ¯r = (¯r1, . . . , ¯rk)′ with ¯ri =
(1′
T Ri)/T being the sample mean of the ith return series. Conner and Korajczyk
(1988) showed that as k →∞eigenvalue–eigenvector analysis of T is equivalent
to the traditional statistical factor analysis. In other words, the APCA estimates of
the factors f t are the ﬁrst m eigenvectors of T . Let F t be the m × T matrix
consisting of the ﬁrst m eigenvectors of T . Then f t is the tth column of F t.
Using an idea similar to the estimation of BARRA factor models, Connor and
Korajczyk (1988) propose reﬁning the estimation of f t as follows:
1. Use the sample covariance matrix T to obtain an initial estimate of f t for
t = 1, . . . , T .
2. For each asset, perform the OLS estimation of the model
rit = αi + βif t + ϵit,
t = 1, . . . , T,
where βi = (βi1, . . . , βim) and compute the residual variance ˆσ 2
i .
--- page 526 ---

asymptotic principal component analysis
499
3. Form the diagonal matrix 
D = diag{ˆσ 2
1 , . . . , ˆσ 2
k } and rescale the returns as
R∗= R
D
−1/2.
4. Compute the T × T covariance matrix using R∗as
∗= 1
k (R∗−1T ¯r′
∗)(R∗−1T ¯r′
∗)′,
where ¯r∗is the k-dimensional vector of the column means of R∗, and perform
eigenvalue–eigenvector analysis of ∗to obtain a reﬁned estimate of f t.
9.6.1
Selecting the Number of Factors
Two methods are available in the literature to help select the number of factors
in factor analysis. The ﬁrst method proposed by Connor and Korajczyk (1993)
makes use of the idea that if m is the proper number of common factors, then
there should be no signiﬁcant decrease in the cross-sectional variance of the asset
speciﬁc error ϵit when the number of factors moves from m to m + 1. The second
method proposed by Bai and Ng (2002) adopts some information criteria to select
the number of factors. This latter method is based on the observation that the
eigenvalue–eigenvector analysis of T solves the least-squares problem
min
α,β,f t
1
kT
k

i=1
T

t=1
(rit −αi −βif t)2.
Assume that there are m factors so that f t is m-dimensional. Let ˆσ 2
i (m) be the
residual variance of the inner regression of the prior least-squares problem for
asset i. This is done by using f t obtained from the APCA analysis. Deﬁne the
cross-sectional average of the residual variances as
ˆσ 2(m) = 1
k
k

i=1
ˆσ 2
i (m).
The criteria proposed by Bai and Ng (2002) are
Cp1(m) = ˆσ 2(m) + mˆσ 2(M)
k + T
kT

ln
 kT
k + T

,
Cp2(m) = ˆσ 2(m) + mˆσ 2(M)
k + T
kT

ln(P 2
kT ),
where M is a prespeciﬁed positive integer denoting the maximum number of factors
and PkT = min(
√
k,
√
T ). One selects m that minimizes either Cp1(m) or Cp2(m)
for 0 ≤m ≤M. In practice, the two criteria may select different numbers of factors.
--- page 527 ---

500
principal component analysis and factor models
9.6.2
An Example
To demonstrate asymptotic principal component analysis, we consider monthly simple returns of 40 stocks from January 2001 to December 2003 for 36 observations.
Thus, we have k = 40 and T = 36. The tick symbols of stocks used are given in
Table 9.6. These stocks are among those heavily traded on NASDAQ and the NYSE
on a particular day of September 2004. The main S-Plus command used is mfactor.
To select the number of factors, we used the two methods discussed earlier.
The Connor–Korajczyk method selects m = 1, whereas the Bai–Ng method uses
m = 6. For the latter method, the two criteria provide different results.
> dim(rtn)
% rtn is the return data.
[1] 36 40
> nf.ck=mfactor(rtn,k=’ck’,max.k=10,sig=0.05)
> nf.ck
Call:
mfactor(x = rtn, k = "ck", max.k = 10, sig = 0.05)
Factor Model:
Factors Variables Periods
1
40
36
Factor Loadings:
Min. 1st Qu. Median
Mean 3rd Qu.
Max.
F.1
0.069
0.432
0.629
0.688
1.071
1.612
Regression R-squared:
Min. 1st Qu. Median
Mean 3rd Qu.
Max.
0.090
0.287
0.487
0.456
0.574
0.831
> nf.bn=mfactor(rtn,k=’bn’,max.k=10,sig=0.05)
Warning messages:
Cp1 and Cp2 did not yield same result. The smaller one
is used.
> nf.bn$k
[1] 6
TABLE 9.6
Tick Symbols of Stocks Used in Asymptotic Principal Component
Analysis for Sample Period from January 2001 to December 2003
Market
Tick Symbol
NASDAQ
INTC
MSFT
SUNW
CSCO
AMAT
ORCL
SIRI
COCO
CORV
SUPG
YHOO
JDSU
QCOM
CIEN
DELL
ERTS
EBAY
ADCT
AAPL
JNPR
NYSE
LU
PFE
NT
BAC
BSX
GE
TXN
XOM
FRX
Q
F
TWX
C
MOT
JPM
TYC
HPQ
NOK
WMT
AMD
--- page 528 ---

exercises
501
Using m = 6, we apply APCA to the returns. The scree plot and estimated factor
returns can also be obtained.
> apca = mfactor(rtn,k=6)
> apca
Call:
mfactor(x = rtn, k = 6)
Factor Model:
Factors Variables Periods
6
40
36
Factor Loadings:
Min
1st Qu. Median
Mean
3rd Qu.
Max.
F.1
0.048
0.349
0.561
0.643
0.952
2.222
F.2
-1.737
0.084
0.216
0.214
0.323
1.046
F.3
-1.512
0.002
0.076
0.102
0.255
1.093
F.4
-0.965
-0.035
0.078
0.048
0.202
0.585
F.5
-0.722
-0.008
0.056
0.066
0.214
0.729
F.6
-0.840
-0.088
0.003
0.003
0.071
0.635
Regression R-squared:
Min. 1st Qu. Median
Mean 3rd Qu.
Max.
0.219
0.480
0.695
0.651
0.801
0.999
> screeplot.mfactor(apca)
> fplot(factors(apca))
Figure 9.7 shows the scree plot of the APCA for the 40 stock returns. The 6
common factors used explain about 89.4% of the variability. Figure 9.8 gives the
time plots of the returns of the 6 estimated factors.
EXERCISES
9.1. Consider the monthly simple excess returns, in percentages and including
dividends, of 13 stocks and the S&P 500 composite index from January 1990
to December 2008. The monthly 3-month Treasury bill rate in the secondary
market is used as the risk-free interest rate to compute the excess returns. The
tick symbols for the stocks are AA, AXP, CAT, DE, F, FDX, HPQ, IBM, JNJ,
KMB, MMM, PG, and WFC. The data are in the ﬁle m-fac-ex-9008.txt.
Perform the market model analysis of Section 9.2.1 for the 13 stock returns
to obtain the estimates of βi, σ 2
i , and R2 for each stock return series.
9.2. Consider the monthly log stock returns, in percentages and including
dividends, of Merck & Company, Johnson & Johnson, General Electric,
General Motors, Ford Motor Company, and value-weighted index from
January 1960 to December 2008; see the ﬁle m-mrk2vw.txt of Exercise 8.1
of Chapter 8.
(a) Perform a principal component analysis of the data using the sample
covariance matrix.
--- page 529 ---

502
principal component analysis and factor models
F.1
F.2
F.3
F.4
F.5
F.6
F.7
0
20
40
60
80
100
Variances
0.446
0.648
0.779
0.829
0.865
0.894
0.909
Figure 9.7
Scree plot of asymptotic principal component analysis applied to monthly simple returns
of 40 stocks. Sample period is from January 2001 to December 2003.
(b) Perform a principal component analysis of the data using the sample correlation matrix.
(c) Perform a statistical factor analysis on the data. Identify the number of
common factors. Obtain estimates of factor loadings using both the principal component and maximum-likelihood methods.
9.3. The ﬁle m-excess-c10sp-9003.txt contains the monthly simple excess
returns of 10 stocks and the S&P 500 index. The 3-month Treasury bill rate
on the secondary market is used to compute the excess returns. The sample
period is from January 1990 to December 2003 for 168 observations. The 11
columns in the ﬁle contain the returns for ABT, LLY, MRK, PFE, F, GM,
BP, CVX, RD, XOM, and SP5, respectively. Analyze the 10 stock excess
returns using the single-factor market model. Plot the beta estimate and R2
for each stock, and use the global minimum variance portfolio to compare the
covariance matrices of the ﬁtted model and the data.
9.4. Again, consider the 10 stock returns in m-excess-c10sp-9003.txt. The
stocks are from companies in 3 industrial sectors. ABT, LLY, MRK, and PFE
are major drug companies, F and GM are automobile companies, and the rest
are big oil companies. Analyze the excess returns using the BARRA industrial
factor model. Plot the 3-factor realizations and comment on the adequacy of
the ﬁtted model.
9.5. Again, consider the 10 excess stock returns in the ﬁle m-excess-c10sp-
9003.txt. Perform a principal component analysis on the returns and obtain
--- page 530 ---

references
503
−0.2
0.0
0.2
0.4
F.1
−0.4
−0.2
0.0
0.2
0.4
0
10
20
30
F.2
−0.6−0.4−0.2 0.0 0.2 0.4
F.3
−0.2
0.0
0.2
0.4
0
10
20
30
F.4
−0.4 −0.2
0.0
0.2
0.4
F.5
−0.2
0.0
0.2
0.4
0
10
20
30
F.6
Factor returns
Figure 9.8
Time plots of factor returns derived from applying asymptotic principal component analysis
to monthly simple returns of 40 stocks. Sample period is from January 2001 to December 2003.
the scree plot. How many common factors are there? Why? Interpret the
common factors.
9.6. Again, consider the 10 excess stock returns in the ﬁle m-excess-c10sp-
9003.txt. Perform a statistical factor analysis. How many common factors
are there if the 5% signiﬁcance level is used? Plot the estimated factor loadings
of the ﬁtted model. Are the common factors meaningful?
9.7. The ﬁle m-fedip.txt contains year, month, effective federal funds rate,
and the industrial production index from July 1954 to December 2003. The
industrial production index is seasonally adjusted. Use the federal funds rate
and the industrial production index as the macroeconomic variables. Fit a
macroeconomic factor model to the 10 excess returns in m-excess-c10sp-
9003.txt. You can use a VAR model to obtain the surprise series of the
macroeconomic variables. Comment on the ﬁtted factor model.
REFERENCES
Alexander, C. (2001). Market Models: A Guide to Financial Data Analysis. Wiley, Hoboken,
NJ.
Bai, J. and Ng, S. (2002). Determining the number of factors in approximate factor models.
Econometrica 70: 191–221.
--- page 531 ---

504
principal component analysis and factor models
Campbell, J. Y., Lo, A. W., and MacKinlay, A. C. (1997). The Econometrics of Financial
Markets. Princeton University Press, Princeton, NJ.
Chen, N. F., Roll, R., and Ross, S. A. (1986). Economic forces and the stock market. Journal
of Business 59: 383–404.
Connor, G. (1995). The three types of factor models: A comparison of their explanatory
power. Financial Analysts Journal 51: 42–46.
Connor, G. and Korajczyk, R. A. (1986). Performance measurement with the arbitrage
pricing theory: A new framework for analysis. Journal of Financial Economics 15:
373–394.
Connor, G. and Korajczyk, R. A. (1988). Risk and return in an equilibrium APT: Application
of a new test methodology. Journal of Financial Economics 21: 255–289.
Connor, G. and Korajczyk, R. A. (1993). A test for the number of factors in an approximate
factor model. Journal of Finance 48: 1263–1292.
Fama, E. and French, K. R. (1992). The cross-section of expected stock returns. Journal of
Finance 47: 427–465.
Grinold, R. C. and Kahn, R. N. (2000). Active Portfolio Management: A Quantitative
Approach for Producing Superior Returns and Controlling Risk, 2nd ed. McGraw-Hill,
New York.
Johnson, R. A. and Wichern, D. W. (2007). Applied Multivariate Statistical Analysis, 6th
ed. Prentice Hall, Upper Saddle River, NJ.
Kaiser, H. F. (1958). The varimax criterion for analytic rotation in factor analysis. Psychometrika 23: 187–200.
Sharpe, W. (1970). Portfolio Theory and Capital Markets. McGraw-Hill, New York.
Zivot, E. and Wang, J. (2003). Modeling Financial Time Series with S-Plus. Springer New
York.
--- page 532 ---

C H A P T E R
10
Multivariate Volatility Models
and Their Applications
In this chapter, we generalize the univariate volatility models of Chapter 3 to
the multivariate case and discuss some simple methods for modeling the dynamic
relationships between volatility processes of multiple asset returns. By multivariate
volatility, we mean the conditional covariance matrix of multiple asset returns.
Multivariate volatilities have many important ﬁnancial applications. They play an
important role in portfolio selection and asset allocation, and they can be used to
compute the value at risk of a ﬁnancial position consisting of multiple assets.
Consider a multivariate return series {rt}. We adopt the same approach as the
univariate case by rewriting the series as
rt = µt + at,
where µt = E(rt|F t−1) is the conditional expectation of rt given the past information F t−1, and at = (a1t, · · · , akt)′ is the shock, or innovation, of the series at time
t. In addition, we assume that rt follows a multivariate time series model of Chapter
8 so that µt is the 1-step-ahead prediction of the model. For most return series, it
sufﬁces to employ a simple vector ARMA structure with exogenous variables for
µt —that is,
µt = ϒxt +
p

i=1
irt−i −
q

i=1
iat−i,
(10.1)
where xt denotes an m-dimensional vector of exogenous (or explanatory) variables
with x1t = 1, ϒ is a k × m matrix, and p and q are nonnegative integers. We refer
to Eq. (10.1) as the mean equation of rt.
Analysis of Financial Time Series, Third Edition, By Ruey S. Tsay
Copyright 2010 John Wiley & Sons, Inc.
505
--- page 533 ---

506
multivariate volatility models and their applications
The conditional covariance matrix of at given F t−1 is a k × k positive-deﬁnite
matrix t deﬁned by t = Cov(at|F t−1). Multivariate volatility modeling is concerned with the time evolution of t. We refer to a model for the {t} process as
a volatility model for the return series rt.
There are many ways to generalize univariate volatility models to the multivariate case, but the curse of dimensionality quickly becomes a major obstacle
in applications because there are k(k + 1)/2 quantities in t for a k-dimensional
return series. To illustrate, there are 15 conditional variances and covariances in
t for a ﬁve-dimensional return series. The goal of this chapter is to introduce
some relatively simple multivariate volatility models that are useful, yet remain
manageable in real application. In particular, we discuss some models that allow
for time-varying correlation coefﬁcients between asset returns. Time-varying correlations are useful in ﬁnance. For example, they can be used to estimate the
time-varying beta of the market model for a return series.
We begin by using an exponentially weighted approach to estimate the covariance matrix in Section 10.1. This estimated covariance matrix can serve as a
benchmark for multivariate volatility estimation. Section 10.2 discusses some generalizations of univariate GARCH models that are available in the literature. We
then introduce two methods to reparameterize t for volatility modeling in Section
10.3. The reparameterization based on the Cholesky decomposition is found to be
useful. We study some volatility models for bivariate returns in Section 10.4, using
the GARCH model as an example. In this particular case, the volatility model can
be bivariate or three dimensional. Section 10.5 is concerned with volatility models
for higher dimensional returns and Section 10.6 addresses the issue of dimension
reduction. We demonstrate some applications of multivariate volatility models in
Section 10.7. Finally, Section 10.8 gives a multivariate Student-t distribution useful
for volatility modeling.
10.1
EXPONENTIALLY WEIGHTED ESTIMATE
Given the innovations Ft−1 = {a1, . . . , at−1}, the (unconditional) covariance matrix
of the innovation can be estimated by
 =
1
t −1
t−1

j=1
aja′
j,
where it is understood that the mean of aj is zero. This estimate assigns equal
weight 1/(t −1) to each term in the summation. To allow for a time-varying
covariance matrix and to emphasize that recent innovations are more relevant, one
can use the idea of exponential smoothing and estimate the covariance matrix of
at by
t =
1 −λ
1 −λt−1
t−1

j=1
λj−1at−ja′
t−j,
(10.2)
