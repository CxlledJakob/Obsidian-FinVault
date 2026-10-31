# Analysis of Financial Time Series, Third Edition (Wiley -- Ruey S_ Tsay -- Wiley series in probability and statistics, 3rd ed_, -- John Wiley & Sons, -- isbn13 9780470414354 -- 9f99b80c7b2dedd477f463dc5323f3b6 -- An.pdf — pages 533–552

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
--- page 534 ---

exponentially weighted estimate
507
where 0 < λ < 1 and the weights (1 −λ)λj−1/(1 −λt−1) sum to one. For a suf-
ﬁciently large t such that λt−1 ≈0, the prior equation can be rewritten as
t = (1 −λ)at−1a′
t−1 + λt−1.
Therefore, the covariance estimate in Eq. (10.2) is referred to as the exponentially
weighted moving-average (EWMA) estimate of the covariance matrix.
Suppose that the return data are {r1, . . . , rT }. For a given λ and initial estimate
1, t can be computed recursively. If one assumes that at = rt −µt follows a
multivariate normal distribution with mean zero and covariance matrix t, where
µt is a function of parameter , then λ and  can be estimated jointly by the
maximum-likelihood method because the log-likelihood function of the data is
ln L(, λ) ∝−1
2
T

t=1
|t| −1
2
T

t=1
(rt −µt)′−1
t (rt −µt),
which can be evaluated recursively by substituting t for t.
Example 10.1.
To illustrate, consider the daily log returns of the Hang Seng
index of Hong Kong and the Nikkei 225 index of Japan from January 4, 2006, to
December 30, 2008, for 713 observations. The indexes were obtained from Yahoo
Finance. For simplicity, we only employ data when both markets were open to
calculate the log returns, which are in percentages. Figure 10.1 shows the time
plots of the two index returns. The effect of recent global ﬁnancial crisis is clearly
seen from the plots. Let r1t and r2t be the log returns of the Hong Kong and
Japanese markets, respectively. If univariate GARCH models are entertained, we
obtain the models
r1t = 0.109 + a1t,
a1t = σ1tϵ1t,
σ 2
1t = 0.038 + 0.143a2
1,t−1 + 0.855σ 2
1,t−1,
(10.3)
r2t = 0.003 + a2t,
a2t = σ2tϵ2t,
σ 2
2t = 0.044 + 0.127a2
2,t−1 + 0.861σ 2
2,t−1,
(10.4)
where all of the parameter estimates are signiﬁcant at the 5% level except for
the constant term of the mean equation for the Nikkei 225 index returns. The
Ljung–Box statistics of the standardized residuals and their squared series of the
two univariate models fail to indicate any model inadequacy. The two volatility
equations are close to an IGARCH(1,1) model. This is reasonable because of the
increased volatility caused by the subprime ﬁnancial crisis. Figure 10.2 shows
the estimated volatilities of the two univariate GARCH(1,1) models. Indeed, the
volatility series conﬁrm that both markets were more volatile than usual in 2008.
Turn to bivariate modeling. We apply the EWMA approach to obtain volatility
estimates, using the command mgarch in S-Plus FinMetrics:
--- page 535 ---

508
multivariate volatility models and their applications
Year
(a)
Log returns
2006.0
2006.5
2007.0
2007.5
2008.0
2008.5
2009.0
−10 −5
0
5
10
Year
(b)
Log returns
2006.0
2006.5
2007.0
2007.5
2008.0
2008.5
2009.0
−10 −5
0
5
10
Figure 10.1
Time plots of daily log returns in percentages of stock market indexes for Hong Kong and
Japan from January 4, 2006, to December 30, 2008: (a) Hong Kong market and (b) Japanese market.
Year
(a)
σt
σt
2006.0
2006.5
2007.0
2007.5
2008.0
2008.5
2009.0
2
6
4
8
1
2
3
4
5
6
7
Year
(b)
2006.0
2006.5
2007.0
2007.5
2008.0
2008.5
2009.0
Figure 10.2
Estimated volatilities (standard error) for daily log returns in percentages of stock market
indexes for Hong Kong and Japan from January 4, 2006, to December 30, 2008: (a) Hong Kong market
and (b) Japanese market. Univariate models are used.
--- page 536 ---

exponentially weighted estimate
509
> m3=mgarch(formula.mean=∼arma(0,0),formula.var=∼ewma1,
series=rtn,trace=F)
> summary(m3)
Call:
mgarch(formula.mean =∼arma(0,0), formula.var=∼ewma1,
series=rtn,trace = F)
Mean Equation: structure(.Data = ∼arma(0,0), class="formula")
Conditional Var. Eq.: structure(.Data=∼ewma1,class="formula")
Conditional Distribution:
gaussian
--------------------------------------------------------------
Estimated Coefficients:
--------------------------------------------------------------
Value Std.Error
t value Pr(>|t|)
C(1)
0.082425
0.030900
2.6675 0.007816
C(2) -0.006849
0.030093
-0.2276 0.820020
ALPHA
0.069492
0.004945
14.0517 0.000000
The estimate of λ is 1 −ˆα = 1 −0.0695 ≈0.9305, which is in the typical range
commonly seen in practice. Figure 10.3 shows the estimated volatility series by the
Year
(a)
σt
2006.0
2006.5
2007.0
2007.5
2008.0
2008.5
2009.0
2
4
6
σt
1
2
3
4
5
6
Year
(b)
2006.0
2006.5
2007.0
2007.5
2008.0
2008.5
2009.0
Figure 10.3
Estimated volatilities (standard error) for daily log returns in percentages of stock market
indices for Hong Kong and Japan from January 4, 2006, to December 30, 2008: (a) Hong Kong market
and (b) Japanese market. Exponentially weighted moving-average approach is used.
--- page 537 ---

510
multivariate volatility models and their applications
EWMA approach. Compared with those in Figure 10.2, the EWMA approach produces smoother volatility series, even though the two plots show similar volatility
patterns.
10.2
SOME MULTIVARIATE GARCH MODELS
Many authors have generalized univariate volatility models to the multivariate case.
In this section, we discuss some of the generalizations. For more details, readers
are referred to the survey article of Bauwens, Laurent, and Rombouts (2004).
10.2.1
Diagonal Vectorization (VEC) Model
Bollerslev, Engle, and Wooldridge (1988) generalize the exponentially weighted
moving-average approach to propose the model
t = A0 +
m

i=1
Ai ⊙(at−ia′
t−i) +
s

j=1
Bj ⊙t−j,
(10.5)
where m and s are nonnegative integers, Ai and Bj are symmetric matrices, and ⊙
denotes the Hadamard product, that is, element-by-element multiplication. This is
referred to as the diagonal VEC(m, s) model or DVEC(m, s) model. To appreciate
the model, consider the bivariate DVEC(1,1) case satisfying

 σ11,t
σ21,t
σ22,t

=

 A11,0
A21,0
A22,0

+

 A11,1
A21,1
A22,1

⊙

 a2
1,t−1
a1,t−1a2,t−1
a2
2,t−1

+

 B11,1
B21,1
B22,1

⊙

 σ11,t−1
σ21,t−1
σ22,t−1

,
where only the lower triangular part of the model is given. Speciﬁcally, the model is
σ11,t = A11,0 + A11,1a2
1,t−1 + B11,1σ11,t−1,
σ21,t = A21,0 + A21,1a1,t−1a2,t−1 + B21,1σ21,t−1,
σ22,t = A22,0 + A22,1a2
2,t−1 + B22,1σ22,t−1,
where each element of t depends only on its own past value and the corresponding
product term in at−1a′
t−1. That is, each element of a DVEC model follows a
GARCH(1,1)-type model. The model is, therefore, simple. However, it may not
produce a positive-deﬁnite covariance matrix. Furthermore, the model does not
allow for dynamic dependence between volatility series.
--- page 538 ---

some multivariate garch models
511
Year
(a)
Returns
1970
1980
1990
2000
2010
−0.2
0.0
0.2
Returns
−0.2
0.0
0.2
0.4
Year
(b)
1970
1980
1990
2000
2010
Figure 10.4
Time plot of monthly simple returns, including dividends, for Pﬁzer and Merck stocks
from January 1965 to December 2008: (a) Pﬁzer stock and (b) Merck stock.
Example 10.2.
For illustration, consider the monthly simple returns, including
dividends, of two U.S. major drug companies from January 1965 to December 2008
for 528 observations. Let r1t and r2t be the monthly returns of Pﬁzer and Merck
stock, respectively. The bivariate return series rt = (r1t, r2t)′, shown in Figure 10.4,
has no signiﬁcant serial correlations with Q(10) being 10.48(0.40) and 11.42(0.33),
respectively, for the two series. Therefore, the mean equation of rt consists of a
constant term only. We ﬁt a DVEC(1,1) model to the series using the command
mgarch in FinMetrics of S-Plus:
> rtn=cbind(pfe,mrk)
% Output edited.
> mdvec=mgarch(rtn∼1,∼dvec(1,1))
> summary(mdvec)
Call:
mgarch(formula.mean=rtn ∼1, formula.var= ∼dvec(1, 1))
Mean Equation: structure(.Data =rtn ∼1, class="formula")
Conditional Var. Eq.: structure(.Data=∼dvec(1,1),
class="formula")
Conditional Distribution:
gaussian
--------------------------------------------------------------
Estimated Coefficients:
--------------------------------------------------------------
Value Std.Error t value
Pr(>|t|)
C(1) 1.350e-02 3.149e-03
4.285 2.174e-05
--- page 539 ---

512
multivariate volatility models and their applications
C(2) 1.313e-02 3.043e-03
4.314 1.921e-05
A(1, 1) 7.544e-04 3.939e-04
1.916 5.597e-02
A(2, 1) 7.543e-05 3.468e-05
2.175 3.010e-02
A(2, 2) 7.941e-05 3.871e-05
2.051 4.072e-02
ARCH(1; 1, 1) 7.078e-02 2.757e-02
2.568 1.051e-02
ARCH(1; 2, 1) 2.513e-02 8.492e-03
2.960 3.220e-03
ARCH(1; 2, 2) 4.095e-02 1.213e-02
3.375 7.939e-04
GARCH(1; 1, 1) 7.858e-01 9.055e-02
8.677 0.000e+00
GARCH(1; 2, 1) 9.499e-01 1.671e-02
56.831 0.000e+00
GARCH(1; 2, 2) 9.454e-01 1.469e-02
64.358 0.000e+00
--------------------------------------------------------------
Ljung-Box test for standardized residuals:
--------------------------------------------------------------
Statistic P-value Chi^2-d.f.
pfe
9.531
0.6570
12
mrk
12.349
0.4181
12
Ljung-Box test for squared standardized residuals:
--------------------------------------------------------------
Statistic P-value Chi^2-d.f.
pfe
22.077 0.03666
12
mrk
6.437 0.89246
12
> names(mdvec)
[1] "residuals"
"sigma.t"
"df.residual"
"coef"
[5] "model"
"cond.dist"
"likelihood"
"opt.index"
[9] "cov"
"std.residuals" "R.t"
"S.t"
[13] "prediction"
"call"
"series"
From the output, all parameter estimates, but A(1,1), are signiﬁcant at the 5% level,
and the ﬁtted volatility model is
σ11,t = 0.00075 + 0.071a2
1,t−1 + 0.786σ11,t−1,
σ21,t = 0.00008 + 0.025a1,t−1a2,t−1 + 0.950σ21,t−1,
σ22,t = 0.00008 + 0.041a2
2,t−1 + 0.945σ22,t−1.
The output also provides some model checking statistics for individual stock
returns. For instance, the Ljung–Box statistics for the standardized residual
series and its squared series of Pﬁzer stock returns give Q(12) = 9.53(0.66) and
Q(12) = 12.35(0.42), respectively, where the number in parentheses denotes
the p value. Thus, checking the ﬁtted model individually, one cannot reject the
DVEC(1,1) model. A more informative model-checking approach is to apply
the multivarite Q statistics to the bivariate standardized residual series and its
squared process. Details are omitted. Interested readers are referred to Li (2004).
Figure 10.5 shows the ﬁtted volatility and correlation series. These series are
stored in “sigma.t” and “R.t”, respectively. The correlations range from 0.37
to 0.83.
--- page 540 ---

some multivariate garch models
513
Year
(a)
1970
1980
1990
2000
2010
0.06 0.08 0.10 0.12
0.060.070.080.090.10
Correlations
0.4 0.5 0.6 0.7 0.8
Year
(b)
1970
1980
1990
2000
2010
Year
(c)
1970
1980
1990
2000
2010
σt
σt
Figure 10.5
Estimated volatilities (standard error) and time-varying correlations of DVEC(1,1) model
for monthly simple returns of two major drug companies from January 1965 to December 2008: (a)
Pﬁzer stock volatility, (b) Merck stock volatility, and (c) time-varying correlations.
10.2.2
BEKK Model
To guarantee the positive-deﬁnite constraint, Engle and Kroner (1995) propose the
Baba-Engle-Kraft-Kroner (BEKK) model,
t = AA′ +
m

i=1
Ai(at−ia′
t−i)A′
i +
s

j=1
Bjt−jB′
j,
(10.6)
where A is a lower triangular matrix and Ai and Bj are k × k matrices. Based
on the symmetric parameterization of the model, t is almost surely positive definite provided that AA′ is positive deﬁnite. This model also allows for dynamic
dependence between the volatility series. On the other hand, the model has several
disadvantages. First, the parameters in Ai and Bj do not have direct interpretations
concerning lagged values of volatilities or shocks. Second, the number of parameters employed is k2(m + s) + k(k + 1)/2, which increases rapidly with m and s.
--- page 541 ---

514
multivariate volatility models and their applications
Limited experience shows that many of the estimated parameters are statistically
insigniﬁcant, introducing additional complications in modeling.
Example 10.3.
To illustrate, we consider the monthly simple returns of Pﬁzer
and Merck stocks of Example 10.2 and employ a BEKK(1,1) model. Again, S-Plus
is used to perform the estimation:
> mbekk=mgarch(rtn∼1,∼bekk(1,1))
> summary(mbekk)
Call:
mgarch(formula.mean = rtn ∼1, formula.var = ∼bekk(1, 1))
Mean Equation: structure(.Data = rtn ∼1, class = "formula")
Conditional Var. Eq.: structure(.Data=∼bekk(1,1),
class="formula")
Conditional Distribution:
gaussian
--------------------------------------------------------------
Estimated Coefficients:
--------------------------------------------------------------
Value
Std.Error
t value
Pr(>|t|)
C(1)
1.329e-02
0.003247
4.094e+00 4.907e-05
C(2)
1.269e-02
0.003095
4.100e+00 4.792e-05
A(1, 1)
2.505e-02
0.008382
2.988e+00 2.938e-03
A(2, 1)
1.349e-02
0.004979
2.710e+00 6.946e-03
A(2, 2)
3.272e-06
8.453262
3.870e-07 1.000e+00
ARCH(1; 1, 1)
2.129e-01
0.084340
2.524e+00 1.190e-02
ARCH(1; 2, 1)
9.963e-02
0.072156
1.381e+00 1.680e-01
ARCH(1; 1, 2)
6.336e-02
0.076065
8.330e-01 4.052e-01
ARCH(1; 2, 2)
1.824e-01
0.062133
2.936e+00 3.467e-03
GARCH(1; 1, 1)
9.090e-01
0.063239
1.437e+01 0.000e+00
GARCH(1; 2, 1) -5.888e-02
0.047766 -1.233e+00 2.182e-01
GARCH(1; 1, 2) -8.231e-03
0.031512 -2.612e-01 7.940e-01
GARCH(1; 2, 2)
9.824e-01
0.022587
4.349e+01 0.000e+00
--------------------------------------------------------------
Ljung-Box test for standardized residuals:
--------------------------------------------------------------
Statistic P-value Chi^2-d.f.
pfe
9.465
0.6628
12
mrk
11.591
0.4791
12
Ljung-Box test for squared standardized residuals:
--------------------------------------------------------------
Statistic P-value Chi^2-d.f.
pfe
21.55 0.04291
12
mrk
9.19 0.68664
12
Model-checking statistics based on the individual residual series and provided
by S-Plus fail to suggest any model inadequacy of the ﬁtted BEKK(1,1) model.
Figure 10.6 shows the ﬁtted volatilities and the time-varying correlations of the
--- page 542 ---

some multivariate garch models
515
Year
(a)
1970
1980
1990
2000
2010
0.06 0.08 0.10 0.12
0.06 0.08 0.10 0.12
0.4 0.5 0.6 0.7 0.8
Year
(b)
1970
1980
1990
2000
2010
Year
(c)
1970
1980
1990
2000
2010
Correlations
σt
σt
Figure 10.6
Estimated volatilities (standard error) and time-varying correlations of BEKK(1,1) model
for monthly simple returns of two major drug companies from January 1965 to December 2008: (a)
Pﬁzer stock volatility, (b) Merck stock volatility, and (c) time-varying correlations.
BEKK(1,1) model. Compared with Figure 10.5, there are some differences between
the two ﬁtted volatility models. For instance, the time-varying correlations of the
BEKK(1,1) model appear to be more volatile.
The volatility equation of the ﬁtted BEKK(1,1) model is

 σ11,t
σ12,t
σ21,t
σ22,t

=

 0.025
0
0.013
3 × 10−6

 0.025
0.013
0
3 × 10−6

+

 0.213
0.063
0.100
0.182

 a2
1,t−1
a1,t−1a2,t−1
a2,t−1a1,t−1
a2
2,t−1


 0.213
0.100
0.063
0.182

+

0.901
−0.008
−0.059
0.982


 σ11,t−1
σ12,t−1
σ21,t−1
σ22,t−1

0.901
−0.059
−0.008
0.982

,
--- page 543 ---

516
multivariate volatility models and their applications
where three estimates are insigniﬁcant at the 5% level. In general, the BEKK model
tends to contain some insigniﬁcant parameter estimates, and one needs to perform
matrix multiplication to decipher the ﬁtted model.
10.3
REPARAMETERIZATION
A useful step in multivariate volatility modeling is to reparameterize t by making
use of its symmetric property. We consider two reparameterizations.
10.3.1
Use of Correlations
The ﬁrst reparameterization of t is to use the conditional correlation coefﬁcients
and variances of at. Speciﬁcally, we write t as
t ≡[σij,t] = DtρtDt,
(10.7)
where ρt is the conditional correlation matrix of at, and Dt is a k × k diagonal
matrix consisting of the conditional standard deviations of elements of at (i.e.,
Dt = diag{√σ11,t, . . . , √σkk,t}).
Because ρt is symmetric with unit diagonal elements, the time evolution of t
is governed by that of the conditional variances σii,t and the elements ρij,t of ρt,
where j < i and 1 ≤i ≤k. Therefore, to model the volatility of at, it sufﬁces to
consider the conditional variances and correlation coefﬁcients of ait. Deﬁne the
k(k + 1)/2-dimensional vector
t = (σ11,t, . . . , σkk,t, ϱ′
t)′,
(10.8)
where ϱt is a k(k −1)/2-dimensional vector obtained by stacking columns of the
correlation matrix ρt, but using only elements below the main diagonal. Speciﬁ-
cally, for a k-dimensional return series,
ϱt = (ρ21,t, . . . , ρk1,t|ρ32,t, . . . , ρk2,t| · · · |ρk,k−1,t)′.
To illustrate, for k = 2, we have ϱt = ρ21,t and
t = (σ11,t, σ22,t, ρ21,t)′,
(10.9)
which is a three-dimensional vector, and for k = 3, we have ϱt = (ρ21,t, ρ31,t,
ρ32,t)′ and
t = (σ11,t, σ22,t, σ33,t, ρ21,t, ρ31,t, ρ32,t)′,
(10.10)
which is a six-dimensional random vector.
--- page 544 ---

reparameterization
517
If at is a bivariate normal random variable, then t is given in Eq. (10.9) and
the conditional density function of at given F t−1 is
f (a1t, a2t|t) =
1
2π

σ11,tσ22,t(1 −ρ2
21,t)
exp

−Q(a1t, a2t, t)
2(1 −ρ2
21,t)

,
where
Q(a1t, a2t, t) = a2
1t
σ11,t
+ a2
2t
σ22,t
−2ρ21,ta1ta2t
√σ11,tσ22,t
.
The log probability density function of at relevant to the maximum-likelihood
estimation is
ℓ(a1t, a2t, t) = −1
2

ln[σ11,tσ22,t(1 −ρ2
21,t)]
+
1
1 −ρ2
21,t

a2
1t
σ11,t
+ a2
2t
σ22,t
−2ρ21,ta1ta2t
√σ11,tσ22,t
+
. (10.11)
This reparameterization is useful because it models covariances and correlations
directly. Yet the approach has several weaknesses. First, the likelihood function
becomes complicated when k ≥3. Second, the approach requires a constrained
maximization in estimation to ensure the positive deﬁniteness of t. The constraint
becomes complicated when k is large.
10.3.2
Cholesky Decomposition
The second reparameterization of t is to use the Cholesky decomposition; see
Appendix A of Chapter 8. This approach has some advantages in estimation as it
requires no parameter constraints for the positive deﬁniteness of t; see Pourahmadi (1999). In addition, the reparameterization is an orthogonal transformation so
that the resulting likelihood function is extremely simple. Details of the transformation are given next.
Because t is positive deﬁnite, there exist a lower triangular matrix Lt with
unit diagonal elements and a diagonal matrix Gt with positive diagonal elements
such that
t = LtGtL′
t.
(10.12)
This is the well-known Cholesky decomposition of t. A feature of the decomposition is that the lower off-diagonal elements of Lt and the diagonal elements of Gt
--- page 545 ---

518
multivariate volatility models and their applications
have nice interpretations. We demonstrate the decomposition by studying carefully
the bivariate and three-dimensional cases. For the bivariate case, we have
t =

 σ11,t
σ21,t
σ21,t
σ22,t

,
Lt =

 1
0
q21,t
1

,
Gt =

 g11,t
0
0
g22,t

,
where gii,t > 0 for i = 1 and 2. Using Eq. (10.12), we have
t =

 σ11,t
σ12,t
σ12,t
σ22,t

=

g11,t
q21,tg11,t
q21,tg11,t
g22,t + q2
21,tg11,t

.
Equating elements of the prior matrix equation, we obtain
σ11,t = g11,t,
σ21,t = q21,tg11,t,
σ22,t = g22,t + q2
21,tg11,t.
(10.13)
Solving the prior equations, we have
g11,t = σ11,t,
q21,t = σ21,t
σ11,t
,
g22,t = σ22,t −
σ 2
21,t
σ11,t
.
(10.14)
However, consider the simple linear regression
a2t = βa1t + b2t,
(10.15)
where b2t denotes the error term. From the well-known least-squares theory, we
have
β = Cov(a1t, a2t)
Var(a1t)
= σ21,t
σ11,t
,
Var(b2t) = Var(a2t) −β2Var(a1t) = σ22,t −
σ 2
21,t
σ11,t
.
Furthermore, the error term b2t is uncorrelated with the regressor a1t. Consequently,
using Eq. (10.14), we obtain
g11,t = σ11,t,
q21,t = β,
g22,t = Var(b2t),
b2t⊥a1t,
where ⊥denotes no correlation. In summary, the Cholesky decomposition of the
2 × 2 matrix t amounts to performing an orthogonal transformation from at to
bt = (b1t, b2t)′ such that
b1t = a1t
and
b2t = a2t −q21,ta1t,
where q21,t = β is obtained by the linear regression (10.15) and Cov(bt) is a diagonal matrix with diagonal elements gii,t. The transformed quantities q21,t and gii,t
can be interpreted as follows:
--- page 546 ---

reparameterization
519
1. The ﬁrst diagonal element of Gt is simply the variance of a1t.
2. The second diagonal element of Gt is the residual variance of the simple
linear regression in Eq. (10.15).
3. The element q21,t of the lower triangular matrix Lt is the coefﬁcient β of
the regression in Eq. (10.15).
The prior properties continue to hold for the higher dimensional case. For example,
consider the three-dimensional case in which
Lt =


1
0
0
q21,t
1
0
q31,t
q32,t
1

,
Gt =


g11,t
0
0
0
g22,t
0
0
0
g3,t

.
From the decomposition in Eq. (10.12), we have


σ11,t
σ21,t
σ31,t
σ21,t
σ22,t
σ32,t
σ31,t
σ32,t
σ33,t


=


g11,t
q21,tg11,t
q31,tg11,t
q21,tg11,t
q2
21,tg11,t + g22,t
q31,tq21,tg11,t + q32,tg22,t
q31,tg11,t
q31,tq21,tg11,t + q32,tg22,t
q2
31,tg11,t + q2
32,tg22,t + g33,t

.
Equating elements of the prior matrix equation, we obtain
σ11,t = g11,t,
σ21,t = q21,tg11,t,
σ22,t = q2
21,tg11,t + g22,t,
σ31,t = q31,tg11,t,
σ32,t = q31,tq21,tg11,t + q32,tg22,t,
σ33,t = q2
31,tg11,t + q2
32,tg22,t + g33,t
or, equivalently,
g11,t = σ11,t,
q21,t = σ21,t
σ11,t
,
g22,t = σ22,t −q2
21,tg11,t,
q31,t = σ31,t
σ11,t
,
q32,t =
1
g22,t

σ32,t −σ31,t
σ
21,tσ11,t

,
g33,t = σ33,t −q2
31,tg11,t −q2
32,tg22,t.
These quantities look complicated, but they are simply the coefﬁcients and residual
variances of the orthogonal transformation
b1t = a1t,
b2t = a2t −β21b1t,
b3t = a3t −β31b1t −β32b2t,
--- page 547 ---

520
multivariate volatility models and their applications
where βij are the coefﬁcients of least-squares regressions
a2t = β21b1t + b2t,
a3t = β31b1t + β32b2t + b3t.
In other words, we have qij,t = βij, gii,t = V ar(bit) and bit⊥bjt for i̸ = j.
Based on the prior discussion, using Cholesky decomposition amounts to doing
an orthogonal transformation from at to bt, where b1t = a1t, and bit, for 1 < i ≤k,
is deﬁned recursively by the least-squares regression
ait = qi1,tb1t + qi2,tb2t + · · · + qi(i−1),tb(i−1)t + bit,
(10.16)
where qij,t is the (i, j)th element of the lower triangular matrix Lt for 1 ≤j < i.
We can write this transformation as
bt = L−1
t at,
or
at = Ltbt,
(10.17)
where, as mentioned before, L−1
t
is also a lower triangular matrix with unit diagonal
elements. The covariance matrix of bt is the diagonal matrix Gt of the Cholesky
decomposition because
Cov(bt) = L−1
t t(L−1
t )′ = Gt.
The parameter vector relevant to volatility modeling under such a transformation
becomes
t = (g11,t, . . . , gkk,t, q21,t, q31,t, q32,t, . . . , qk1,t, . . . , qk(k−1),t)′,
(10.18)
which is also a k(k + 1)/2-dimensional vector.
The previous orthogonal transformation also dramatically simpliﬁes the likelihood function of the data. Using the fact that |Lt| = 1, we have
|t| = |LtGtL′
t| = |Gt| =
k
i=1
gii,t.
(10.19)
If the conditional distribution of at given the past information is multivariate normal N(0, t), then the conditional distribution of the transformed series bt is
multivariate normal N(0, Gt), and the log-likelihood function of the data becomes
extremely simple. Indeed, we have the log probability density of at as
ℓ(at, t) = ℓ(bt, t) = −1
2
k

i=1

ln(gii,t) + b2
it
gii,t

,
(10.20)
where for simplicity the constant term is omitted and gii,t is the variance of bit.
--- page 548 ---

garch models for bivariate returns
521
Using the Cholesky decomposition to reparameterize t has several advantages.
First, from Eq. (10.19), t is positive deﬁnite if gii,t > 0 for all i. Consequently,
the positive-deﬁnite constraint of t can easily be achieved by modeling ln(gii,t)
instead of gii,t. Second, elements of the parameter vector t in Eq. (10.18) have
nice interpretations. They are the coefﬁcients and residual variances of multiple
linear regressions that orthogonalize the shocks to the returns. Third, the correlation
coefﬁcient between a1t and a2t is
ρ21,t =
σ21,t
√σ11,tσ22,t
= q21,t ×
√σ11,t
√σ22,t
,
which is time varying if q21,t̸ = 0. In particular, if q21,t = c̸ = 0, then ρ21,t =
c√σ11,t/√σ22,t, which continues to be time-varying provided that the variance ratio
σ11,t/σ22,t is not a constant. This time-varying property applies to other correlation
coefﬁcients when the dimension of rt is greater than 2 and is a major difference
between the two approaches for reparameterizing t.
Using Eq. (10.16) and the orthogonality among the transformed shocks bit, we
obtain
σii,t = Var(ait|Ft−1) =
i
v=1
q2
iv,tgvv,t,
i = 1, . . . , k,
σij,t = Cov(ait, ajt|Ft−1) =
j

v=1
qiv,tqjv,tgvv,t,
j < i,
i = 2, . . . , k,
where qvv,t = 1 for v = 1, . . . , k. These equations show the parameterization of
t under the Cholesky decomposition.
10.4
GARCH MODELS FOR BIVARIATE RETURNS
Since the same techniques can be used to generalize many univariate volatility models to the multivariate case, we focus our discussion on the multivariate GARCH
model. Other multivariate volatility models can also be used.
For a k-dimensional return series rt, a multivariate GARCH model uses “exact
equations” to describe the evolution of the k(k + 1)/2-dimensional vector t over
time. By exact equation, we mean that the equation does not contain any stochastic
shock. However, the exact equation may become complicated even in the simplest
case of k = 2 for which t is three dimensional. To keep the model simple, some
restrictions are often imposed on the equations.
10.4.1
Constant-Correlation Models
To keep the number of volatility equations low, Bollerslev (1990) considers the
special case in which the correlation coefﬁcient ρ21,t = ρ21 is time invariant, where
--- page 549 ---

522
multivariate volatility models and their applications
|ρ21| < 1. Under such an assumption, ρ21 is a constant parameter and the volatility
model consists of two equations for ∗
t , which is deﬁned as ∗
t = (σ11,t, σ22,t)′.
A GARCH(1,1) model for ∗
t becomes
∗
t = α0 + α1a2
t−1 + β1∗
t−1,
(10.21)
where a2
t−1 = (a2
1,t−1, a2
2,t−1)′, α0 is a two-dimensional positive vector, and α1 and
β1 are 2 × 2 nonnegative deﬁnite matrices. More speciﬁcally, the model can be
expressed in detail as

 σ11,t
σ22,t

=

 α10
α20

+

 α11
α12
α21
α22

 a2
1,t−1
a2
2,t−1

+

 β11
β12
β21
β22

 σ11,t−1
σ22,t−1

,
(10.22)
where αi0 > 0 for i = 1 and 2. Deﬁning ηt = a2
t −∗
t , we can rewrite the prior
model as
a2
t = α0 + (α1 + β1)a2
t−1 + ηt −β1ηt−1,
which is a bivariate ARMA(1,1) model for the a2
t process. This result is a direct
generalization of the univariate GARCH(1,1) model of Chapter 3. Consequently,
some properties of model (10.22) are readily available from those of the bivariate
ARMA(1,1) model of Chapter 8. In particular, we have the following results:
1. If all of the eigenvalues of α1 + β1 are positive, but less than 1, then the
bivariate ARMA(1,1) model for a2
t is weakly stationary and, hence, E(a2
t )
exists. This implies that the shock process at of the returns has a positivedeﬁnite unconditional covariance matrix. The unconditional variances of the
elements of at are (σ 2
1 , σ 2
2 )′ = (I −α1 −β1)−1φ0, and the unconditional
covariance between a1t and a2t is ρ21σ1σ2.
2. If α12 = β12 = 0, then the volatility of a1t does not depend on the past
volatility of a2t. Similarly, if α21 = β21 = 0, then the volatility of a2t does
not depend on the past volatility of a1t.
3. If both α1 and β1 are diagonal, then the model reduces to two univariate GARCH(1,1) models. In this case, the two volatility processes are not
dynamically related.
4. Volatility forecasts of the model can be obtained by using forecasting methods
similar to those of a vector ARMA(1,1) model; see the univariate case in
Chapter 3. The 1-step-ahead volatility forecast at the forecast origin h is
∗
h(1) = α0 + α1a2
h + β1∗
h.
For the ℓ-step-ahead forecast, we have
∗
h(ℓ) = α0 + (α1 + β1)∗
h(ℓ−1),
ℓ> 1.
--- page 550 ---

garch models for bivariate returns
523
These forecasts are for the marginal volatilities of ait. The ℓ-step-ahead forecast of the covariance between a1t and a2t is ˆρ21[σ11,h(ℓ)σ22,h(ℓ)]0.5, where
ˆρ21 is the estimate of ρ21 and σii,h(ℓ) are the elements of ∗
h(ℓ).
Example 10.4.
Again, consider the daily log returns of Hong Kong and
Japanese markets of Example 10.1. Using a bivariate GARCH model, we obtain a
constant correlation model that ﬁts the data reasonably well. The mean equations
of the bivariate model are
r1t = 0.101 + a1t,
r2t = 0.002 + a2t,
where the standard errors of the two estimates are 0.050 and 0.048, respectively.
The volatility equations are

 σ11,t
σ22,t

=


0.079
(0.019)
0.054
(0.019)

+


0.145
·
(0.022)
0.105
(0.014)



 a2
1,t−1
a2
2,t−1

+


0.833
(0.023)
0.875
(0.020)



 σ11,t−1
σ22,t−1

,
(10.23)
where the numbers in parentheses are standard errors. The estimated constant correlation between the two returns is 0.668.
Let ˜at = (˜a1t, ˜a2t)′ be the standardized residuals, where ˜ait = ait/√σii,t. The
Ljung–Box statistics of ˜at give Q2(4) = 17.29(0.37) and Q2(12) = 48.21(0.46),
where the number in parentheses denotes the p value. Here the p values are
based on chi-squared distributions with 16 and 48 degrees of freedom, respectively. The Q statistics of individual series ˜ait shown in S-Plus output also fail
to indicate any model inadequancy. Consequently, the constant correlation model
in Eq. (10.23) ﬁts the data reasonably well. Figure 10.7 shows the ﬁtted volatility processes of model (10.23), which can be compared with those of Example
10.1.
The model in Eq. (10.23) shows two uncoupled volatility equations, indicating that the volatilities of the two markets are not dynamically related, but they
are contemporaneously correlated. We refer to the model as a bivariate diagonal
constant-correlation model. In practice, this type of models might not be suitable
because there exists the possibility of dynamic dependence in volatility among
markets, that is, the spillover effect in volatility. Finally, the constant-correlation
model can easily be estimated using S-Plus:
--- page 551 ---

524
multivariate volatility models and their applications
Year
(a)
2006.0
2006.5
2007.0
2007.5
2008.0
2008.5
2009.0
2
4
6
8
σt
σt
1
2
3
4
5
6
Year
(b)
2006.0
2006.5
2007.0
2007.5
2008.0
2008.5
2009.0
Figure 10.7
Estimated volatilities for daily log returns in percentages of stock market indexes for
Hong Kong and Japan from January 4, 2006, to December 30, 2008: (a) Hong Kong market and (b)
Japanese market. Model used is Eq. (10.23).
> mccc = mgarch(rtn∼1,∼ccc(1,1),trace=F)
> summary(mccc)
Example 10.5.
As a second illustration, consider the monthly log returns, in
percentages, of IBM stock and the S&P 500 index from January 1926 to December
1999 used in Chapter 8. Let r1t and r2t be the monthly log returns for IBM stock
and the S&P 500 index, respectively. If a constant-correlation GARCH(1,1) model
is entertained, we obtain the mean equations
r1t = 1.351 + 0.072r1,t−1 + 0.055r1,t−2 −0.119r2,t−2 + a1t,
r2t = 0.703 + a2t,
where standard errors of the parameters in the ﬁrst equation are 0.225, 0.029, 0.034,
and 0.044, respectively, and the standard error of the parameter in the second
equation is 0.155. The volatility equations are

σ11,t
σ22,t

=


2.98
(0.59)
2.09
(0.47)

+


0.079
(0.013)
0.042
0.045
(0.009)
(0.010)



a2
1,t−1
a2
2,t−1

+


0.873
−0.031
(0.020)
(0.009)
−0.066
0.913
(0.015)
(0.014)



σ11,t−1
σ22,t−1

,
(10.24)
--- page 552 ---

garch models for bivariate returns
525
where the numbers in parentheses are standard errors. The constant correlation
coefﬁcient is 0.614 with standard error 0.020. Using the standardized residuals, we
obtain the Ljung–Box statistics Q2(4) = 16.77(0.21) and Q2(8) = 32.40(0.30),
where the p values shown in parentheses are obtained from chi-squared distributions with 13 and 29 degrees of freedom, respectively. Here the degrees of
freedom have been adjusted because the mean equations contain three lagged predictors. For the squared standardized residuals, we have Q∗
2(4) = 18.00(0.16) and
Q∗
2(8) = 39.09(0.10). Therefore, at the 5% signiﬁcance level, the standardized
residuals ˜at have no serial correlations or conditional heteroscedasticities. This
bivariate GARCH(1,1) model shows a feedback relationship between the volatilities
of the two monthly log returns.
10.4.2
Time-Varying Correlation Models
A major drawback of the constant-correlation volatility models is that the correlation coefﬁcient tends to change over time in a real application. Consider the
monthly log returns of IBM stock and the S&P 500 index used in Example 10.5.
It is hard to justify that the S&P 500 index return, which is a weighted average, can maintain a constant-correlation coefﬁcient with IBM return over the past
70 years. Figure 10.8 shows the sample correlation coefﬁcient between the two
monthly log return series using a moving window of 120 observations (i.e., 10
years). The correlation changes over time and appears to be decreasing in recent
years. The decreasing trend in correlation is not surprising because the ranking of
IBM market capitalization among large U.S. industrial companies has changed in
recent years. A Lagrange multiplier statistic was proposed recently by Tse (2000)
to test constant-correlation coefﬁcients in a multivariate GARCH model.
A simple way to relax the constant-correlation constraint within the GARCH
framework is to specify an exact equation for the conditional correlation coefﬁ-
cient. This can be done by two methods using the two reparameterizations of t
discussed in Section 10.3. First, we use the correlation coefﬁcient directly. Because
the correlation coefﬁcient between the returns of IBM stock and S&P 500 index is
positive and must be in the interval [0, 1], we employ the equation
ρ21,t =
exp(qt)
1 + exp(qt),
(10.25)
where
qt = ω0 + ω1ρ21,t−1 + ω2
a1,t−1a2,t−1
√σ11,t−1σ22,t−1
,
where σii,t−1 is the conditional variance of the shock ai,t−1. We refer to this equation
as a GARCH(1,1) model for the correlation coefﬁcient because it uses the lag-1
cross correlation and the lag-1 cross product of the two shocks. If ϖ1 = ϖ2 = 0,
then model (10.25) reduces to the case of constant correlation.
