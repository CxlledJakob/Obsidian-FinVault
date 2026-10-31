# Analysis of Financial Time Series, Third Edition (Wiley -- Ruey S_ Tsay -- Wiley series in probability and statistics, 3rd ed_, -- John Wiley & Sons, -- isbn13 9780470414354 -- 9f99b80c7b2dedd477f463dc5323f3b6 -- An.pdf — pages 476–495

--- page 476 ---

pairs trading
449
• Buy a share of stock 1 and short γ shares of stock 2 at time t if wt =
p1t −γp2t = µw −
.
• Unwind the position at time t + i (i > 0) if wt+i = p1,i+i −γp2,t+i = µw +

.
One can identify the time point t so long as
 is not too large compared with
the standard deviation of wt. The time point t + i will occur because of the mean
reverting of the spread series. In this particular instance, the return of the portfolio
wt+i −wt = 2
 and the net proﬁt of the trade is 2
 −η > 0.
Discussion.
The aforementioned trading strategy is just one of many possibilities. For instance, if
 > η, one can unwind the position when wt+i = µw. The
net proﬁt of the pairs trading then is
 −η > 0. This may result in more transactions and trading costs, but it shortens the holding period of the portfolio. If
is negative, then one can short one share of stock 1 and buy γ shares of stock 2
to make a net proﬁt −2
 −η. The quantity η is the threshold for trading and is
likely to depend on several factors such as transaction fees and bid–ask spreads of
the two stocks.
□
8.8.3
Simple Illustration
To demonstrate pairs trading, we consider two stocks traded on the New York
Stock Exchange. The two companies are the Billiton Ltd. of Australia and the
Vale S.A. of Brazil with stock symbols BHP and VALE, respectively. BHP of
Australia is a natural resources company with business in Australia, the Americans,
and Southern Africa. Vale of Brazil is a worldwide metals and mining company.
Thus, both multinational companies belong to the natural resources industry and
encounter similar risk factors. The daily prices of the two stocks were downloaded
from Yahoo Finance, and we employ adjusted closing prices from July 1, 2002, to
March 31, 2006, in our study.
Figure 8.17 shows the time plots of the daily log prices of the two stocks
(adjusted closing prices). The upper plot is for the BHP stock. From the plots, the
prices of the two stocks exhibit certain characteristics of comovement. Let p1t and
p2t be the daily log closing prices of BHP and VALE, respectively. We analyze
the series using both the least-squares and maximum-likelihood methods.
Least-Squares Estimation
A simple way to verify that the two stocks are suitable for pairs trading is to check
the cointegration of their log stock prices. To this end, we consider the simple
linear regression p1t = β0 + β1p2t + wt, where wt denotes the residual series. For
the BHP and VALE stocks, we have
p1t = 1.823 + 0.717p2t + ˆwt,
σw = 0.044.
--- page 477 ---

450
multivariate time series analysis and its applications
Year
Log price
2003
2004
2005
2006
0
1
2
3
4
Figure 8.17
Daily log (adjusted) closing prices of BHP and VALE stocks from July 1, 2002, to March
31, 2006. Upper plot is for BHP stock.
Figure 8.18(a) shows the time plot of the residual series ˆwt. The plot shows that the
residual series has certain characteristics of a stationary time series. In particular, it
has mean zero and ﬂuctuates around its mean within a ﬁxed range. Figure 8.18(b)
gives the sample ACF of ˆwt. The ACFs decay exponentially, supporting that ˆwt
is indeed stationary. To further conﬁrm the stationarity assertion, we ﬁt an AR(2)
model to ˆwt and obtain
(1 −0.805B −0.122B2) ˆwt = at,
σa = 0.018.
Following the discussion of Chapter 2, we can obtain the two characteristic
roots of the ﬁtted AR(2) model. Indeed, the model can be rewritten as
(1 −0.935B)(1 −0.130B) ˆwt = at. Hence, ˆwt is stationary. Finally, we conduct
an augmented Dickey–Fuller unit-root test on ˆwt using an AR(2) model and ﬁnd
that the test statistic is −6.04 with a p value of 0.01. The unit-root hypothesis is
clearly rejected.
Maximum-Likelihood Estimation
A formal approach to verify the cointegration of the two log stock prices is to perform a cointegration test. Let xt = (p1t, p2t)′. Using information criteria, a VAR(1)
model is speciﬁed for xt. We then conduct cointegration tests with restricted and
unrestricted constant. Both tests give similar results so that we only report the
results for the case of restricted constant.
--- page 478 ---

pairs trading
451
Year
(a)
Spread
2003
2004
2005
2006
−0.15 −0.05 0.05
0.15
Lag
(b)
ACF
0
5
10
15
20
0.0 0.2 0.4 0.6 0.8 1.0
Figure 8.18
Results of least-squares estimation: (a) Time plot of the estimated spread between BHP
and VALE daily log stock prices. (b) Sample autocorrelation functions of estimated spread.
> coint2=coint(xx,trend="rc")
> coint2
coint(Y = xt, trend = "rc")
Trend Specification:
H1*(r): Restricted constant
Trace tests signif. at the 5% level are flagged by ’ +’.
Trace tests signif. at the 1% level are flagged by ’++’.
Max Eigenvalue tests signif. at the 5% level are
flagged by ’ *’.
Max Eigenvalue tests signif. at the 1% level are
flagged by ’**’.
Tests for Cointegration Rank:
Eigenvalue TraceSt
95%-CV 99%-CV Max-St 95%-CV 99%-
CV
H(0)++**
0.0415
47.7400
19.960 24.600 39.965 15.670 20.200
H(1)
0.0082
7.7748
9.240 12.970
7.774
9.240 12.970
The test conﬁrms that xt is cointegrated. Next, we perform the maximumlikelihood estimation of the error correction model. The results are given below:
> n3=VECM(coint2)
> summary(n3)
--- page 479 ---

452
multivariate time series analysis and its applications
VECM(test = coint2)
Cointegrating Vectors:
coint.1
1.0000
vale
-0.7177
(std.err)
0.0112
(t.stat)
-64.0913
Intercept*
-1.8144
(std.err)
0.0169
(t.stat) -107.0430
VECM Coefficients:
bhp
vale
coint.1 -0.0671
0.0263
(std.err)
0.0145
0.0168
(t.stat) -4.6462
1.5659
bhp.lag1 -0.1119
0.0659
(std.err)
0.0366
0.0425
(t.stat) -3.0596
1.5516
vale.lag1
0.0732
0.0445
(std.err)
0.0320
0.0371
(t.stat)
2.2920
1.1986
Regression Diagnostics:
bhp
vale
R-squared 0.0370 0.0104
Adj. R-squared 0.0350 0.0083
Resid. Scale 0.0193 0.0224
Based on the estimation result, we have the model

xt =

 −0.067
0.026

(wt−1 −1.81) +

 −0.11
0.07
0.07
0.04


xt−1 + at,
where the estimated standard errors of ait are 0.019 and 0.022, respectively. In
addition, the spread series is wt = p1t −0.718p2t, which is stationary with mean
1.81. Clearly, the result is very close to that of the least-squares estimation. In
particular, the γ parameter for the pairs trading is ˆγ = 0.718. Also, as expected,
α1 is negative whereas α2 is positive.
Trading Strategy
Since the standard error of the spread series wt is 0.044, we can select
 = 0.045,
which is slightly greater than one standard error of wt, for pairs trading. This choice
--- page 480 ---

pairs trading
453
Year
Spread
2003
2004
2005
2006
1.65
1.70
1.75
1.80
1.85
1.90
1.95
Figure 8.19
Time plot of ﬁtted spread series between daily log prices of BHP and VALE stocks.
Three horizontal lines denotes µw, µw + 0.045, and µw −0.045 with µw = E(wt).
of
 ensures that the probability for the spread wt to deviate
 away from its mean
is not small. In fact, under the normality assumption, the probability is about 30%.
Figure 8.19 shows the time plot of the spread series wt of the ﬁtted error correction
model. Three horizontal lines are imposed on the plot. They are µw, µw + 0.045,
and µw −0.045 with the latter two serving as boundaries for pairs trading. Since
wt varies from the lower boundary to the upper one (or from the upper boundary
to the lower one) several times, there are many pairs-trading opportunities. From
the discussion of Section 8.8.2, the log return of each pairs trading is 2
 = 0.09,
which is not small. A more realistic demonstration is to implement the trading in
a out-of-sample period. However, the example shows that pairs trading is feasible.
Finally, an important question in pairs trading is to identify the cointegrated
pairs of stocks. There are some procedures available in the literature. It seems
reasonable to consider pairs of stocks that have similar risk factors. In other words,
one should make use of ﬁnance theory to guide the selection.
R Demonstration
The following output has been edited:
> library(urca)
> help(ca.jo)
> da=read.table("d-bhp0206.txt",header=T)
> da1=read.table("d-vale0206.txt",header=T)
> bhp=log(da[,9])
--- page 481 ---

454
multivariate time series analysis and its applications
> vale=log(da1[,9])
> m1=lm(bhp~vale)
> summary(m1)
Call:
lm(formula = bhp ~ vale)
Coefficients:
Estimate Std. Error t value Pr(>|t|)
(Intercept) 1.822648
0.003662
497.7
>2e-16 ***
vale
0.716664
0.002354
304.4
>2e-16 ***
---
Residual standard error: 0.04421 on 944 degrees of freedom
Multiple R-squared: 0.9899,
Adjusted R-squared: 0.9899
F-statistic: 9.266e+04 on 1 and 944 DF,
p-value: < 2.2e-16
> wt=m1$residuals
> m3=arima(wt,order=c(2,0,0),include.mean=F)
> m3
Call:
arima(x = wt, order = c(2, 0, 0), include.mean = F)
Coefficients:
ar1
ar2
0.8051
0.1219
s.e.
0.0322
0.0325
sigma^2 estimated as 0.0003326: log likelihood=2444.76
> p1=c(1,-m3$coef)
> x=polyroot(p1)
> x
[1]
1.069100+0i -7.675365-0i
> 1/Mod(x)
[1] 0.9353661 0.1302870
> xt=cbind(bhp,vale)
> mm=ar(xt)
> mm$order
[1] 2
> cot=ca.jo(xt,ecdet="const",type=’trace’,K=2,
spec=’transitory’)
> summary(cot)
######################
# Johansen-Procedure #
######################
Test type: trace statistic, without linear trend and
constant in cointegration
Eigenvalues (lambda):
--- page 482 ---

pairs trading
455
[1]
4.148282e-02
8.206470e-03 -4.610389e-18
Values of teststatistic and critical values of test:
test 10pct
5pct
1pct
r <= 1 |
7.78
7.52
9.24 12.97
r = 0
| 47.77 17.85 19.96 24.60
Eigenvectors, normalised to first column:
(These are the cointegration relations)
bhp.l1
vale.l1
constant
bhp.l1
1.000000
1.0000000
1.000000
vale.l1
-0.717704 -0.7327542
2.047274
constant -1.828460 -1.5411890 -5.712629
Weights W:
(This is the loading matrix)
bhp.l1
vale.l1
constant
bhp.d
-0.06731196 0.004568985 9.341093e-18
vale.d
0.02545606 0.007541565 1.015639e-18
> co1=ca.jo(xt,ecdet="const",type=’eigen’,K=2,
spec=’transitory’)
> summary(co1)
######################
# Johansen-Procedure #
######################
Test type: maximal eigenvalue statistic (lambda max), without
linear trend and constant in cointegration
Eigenvalues (lambda):
[1]
4.148282e-02
8.206470e-03 -4.610389e-18
Values of teststatistic and critical values of test:
test 10pct
5pct
1pct
r <= 1 |
7.78
7.52
9.24 12.97
r = 0
| 40.00 13.75 15.67 20.20
Eigenvectors, normalised to first column:
(These are the cointegration relations)
bhp.l1
vale.l1
constant
bhp.l1
1.000000
1.0000000
1.000000
vale.l1
-0.717704 -0.7327542
2.047274
constant -1.828460 -1.5411890 -5.712629
--- page 483 ---

456
multivariate time series analysis and its applications
Weights W:
(This is the loading matrix)
bhp.l1
vale.l1
constant
bhp.d
-0.06731196 0.004568985 9.341093e-18
vale.d
0.02545606 0.007541565 1.015639e-18
APPENDIX A: REVIEW OF VECTORS AND MATRICES
In this appendix, we brieﬂy review some algebra and properties of vectors and
matrices. No proofs are given as they can be found in standard textbooks on
matrices (e.g., Graybill, 1969).
An m × n real-valued matrix is an m × n array of real numbers. For example,
A =

2
5
8
−1
3
4

is a 2 × 3 matrix. This matrix has two rows and three columns. In general, an
m × n matrix is written as
A ≡[aij] =


a11
a12
· · ·
a1,n−1
a1n
a21
a22
· · ·
a2,n−1
a2n
...
...
...
...
am1
am2
· · ·
am,n−1
amn

.
(8.46)
The positive integers m and n are the row dimension and column dimension of A.
The real number aij is referred to as the (i, j)th element of A. In particular, the
elements aii are the diagonal elements of the matrix.
An m × 1 matrix forms an m-dimensional column vector, and a 1 × n matrix
is an n-dimensional row vector. In the literature, a vector is often meant to be a
column vector. If m = n, then the matrix is a square matrix. If aij = 0 for i̸ = j
and m = n, then the matrix A is a diagonal matrix. If aij = 0 for i̸ = j and aii = 1
for all i, then A is the m × m identity matrix, which is commonly denoted by I m
or simply I if the dimension is clear.
The n × m matrix
A′ =


a11
a21
· · ·
am−1,1
am1
a12
a22
· · ·
am−1,2
am2
...
...
...
...
a1n
a2n
· · ·
am−1,n
amn


is the transpose of the matrix A. For example,


2
−1
5
3
8
4


is the transpose of

2
5
8
−1
3
4

.
--- page 484 ---

appendix a: review of vectors and matrices
457
We use the notation A′ = [a′
ij] to denote the transpose of A. From the deﬁnition,
a′
ij = aji and (A′)′ = A. If A′ = A, then A is a symmetric matrix.
Basic Operations
Suppose that A = [aij]m×n and C = [cij]p×q are two matrices with dimensions
given in the subscript. Let b be a real number. Some basic matrix operations are
deﬁned next:
• Addition: A + C = [aij + cij]m×n if m = p and n = q.
• Subtraction: A −C = [aij −cij]m×n if m = p and n = q.
• Scalar multiplication: bA = [baij]m×n.
• Multiplication: AC = [n
v=1 aivcvj]m×q provided that n = p.
When the dimensions of matrices satisfy the condition for multiplication to
take place, the two matrices are said to be conformable. An example of matrix
multiplication is

 2
1
1
1

1
2
3
−1
2
−4

=

 2 · 1 −1 · 1
2 · 2 + 1 · 2
2 · 3 −1 · 4
1 · 1 −1 · 1
1 · 2 + 1 · 2
1 · 3 −1 · 4

=

 1
6
2
0
4
−1

.
Important rules of matrix operations include (a) (AC)′ = C′A′ and (b) AC̸ = CA
in general.
Inverse, Trace, Eigenvalue, and Eigenvector
A square matrix Am×m is nonsingular or invertible if there exists a unique matrix
Cm×m such that AC = CA = I m, the m × m identity matrix. In this case, C is
called the inverse matrix of A and is denoted by C = A−1.
The trace of Am×m is the sum of its diagonal elements [i.e., tr(A) = m
i=1 aii].
It is easy to see that (a) tr(A + C) = tr(A) + tr(C), (b) tr(A) = tr(A′), and (c)
tr(AC) = tr(CA) provided that the two matrices are conformable.
A number λ and an m × 1 vector b, possibly complex valued, are a right eigenvalue and eigenvector pair of the matrix A if Ab = λb. There are m possible
eigenvalues for the matrix A. For a real-valued matrix A, complex eigenvalues
occur in conjugated pairs. The matrix A is nonsingular if and only if all of its
eigenvalues are nonzero. Denote the eigenvalues by {λi|i = 1, . . . , m}: We have
tr(A) = m
i=1 λi. In addition, the determinant of the matrix A can be deﬁned as
|A| = m
i=1 λi. For a general deﬁnition of determinant of a matrix, see a standard
textbook on matrices (e.g., Graybill, 1969).
Finally, the rank of the matrix Am×n is the number of nonzero eigenvalues of
the symmetric matrix AA′. Also, for a nonsingular matrix A, (A−1)′ = (A′)−1.
--- page 485 ---

458
multivariate time series analysis and its applications
Positive-Deﬁnite Matrix
A square matrix A (m × m) is a positive-deﬁnite matrix if (a) A is symmetric and
(b) all eigenvalues of A are positive. Alternatively, A is a positive-deﬁnite matrix
if for any nonzero m-dimensional vector b, we have b′Ab > 0.
Useful properties of a positive-deﬁnite matrix A include (a) all eigenvalues of
A are real and positive, and (b) the matrix can be decomposed as
A = PP ′,
where  is a diagonal matrix consisting of all eigenvalues of A and P is an m × m
matrix consisting of the m right eigenvectors of A. It is common to write the
eigenvalues as λ1 ≥λ2 ≥· · · ≥λm and the eigenvectors as e1, . . . , em such that
Aei = λiei and e′
iei = 1. In addition, these eigenvectors are orthogonal to each
other—namely, e′
iej = 0 if i̸ = j —if the eigenvalues are distinct. The matrix
P is an orthogonal matrix and the decomposition is referred to as the spectral
decomposition of the matrix A. Consider, for example, the simple 2 × 2 matrix
 =

 2
1
1
2

,
which is positive deﬁnite. Simple calculations show that

 2
1
1
2

 1
1

= 3

 1
1

,

 2
1
1
2

1
−1

=

1
−1

.
Therefore,
3
and
1
are
eigenvalues
of

with
normalized
eigenvectors
(1/
√
2, 1/
√
2)′ and (1/
√
2, −1/
√
2)′, respectively. It is easy to verify that the
spectral decomposition holds—that is,

1
√
2
1
√
2
1
√
2
−1
√
2

 2
1
1
2
 
1
√
2
1
√
2
1
√
2
−1
√
2

=

 3
0
0
1

.
For a symmetric matrix A, there exists a lower triangular matrix L with diagonal
elements being 1 and a diagonal matrix G such that A = LGL′; see Chapter 1
of Strang (1980). If A is positive deﬁnite, then the diagonal elements of G are
positive. In this case, we have
A = L
√
G
√
GL′ = (L
√
G)(L
√
G)′,
where L
√
G is again a lower triangular matrix and the square root is taken element
by element. Such a decomposition is called the Cholesky decomposition of A. This
decomposition shows that a positive-deﬁnite matrix A can be diagonalized as
L−1A(L′)−1 = L−1A(L−1)′ = G.
--- page 486 ---

appendix a: review of vectors and matrices
459
Since L is a lower triangular matrix with unit diagonal elements, L−1 is also lower
triangular matrix with unit diagonal elements. Consider again the prior 2 × 2 matrix
. It is easy to verify that
L =

 1.0
0.0
0.5
1.0

and
G =

 2.0
0.0
0.0
1.5

satisfy  = LGL′. In addition,
L−1 =

1.0
0.0
−0.5
1.0

and
L−1(L−1)′ = G.
Vectorization and Kronecker Product
Writing an m × n matrix A in its columns as A = [a1, . . . , an], we deﬁne the
stacking operation as vec(A) = (a′
1, a′
2, . . . , a′
m)′, which is an mn × 1 vector. For
two matrices Am×n and Cp×q, the Kronecker product between A and C is
A ⊗C =


a11C
a12C
· · ·
a1nC
a21C
a22C
· · ·
a2nC
...
...
...
am1C
am2C
· · ·
amnC


mp×nq
.
For example, assume that
A =

2
1
−1
3

,
C =

4
−1
3
−2
5
2

.
Then vec(A) = (2, −1, 1, 3)′, vec(C) = (4, −2, −1, 5, 3, 2)′, and
A ⊗C =


8
−2
6
4
−1
3
−4
10
4
−2
5
2
−4
1
−3
12
−3
9
2
−5
−2
−6
15
6

.
Assuming that the dimensions are appropriate, we have the following useful properties for the two operators:
1. A ⊗C̸ = C ⊗A in general.
2. (A ⊗C)′ = A′ ⊗C′.
3. A ⊗(C + D) = A ⊗C + A ⊗D.
4. (A ⊗C)(F ⊗G) = (AF) ⊗(CG).
5. If A and C are invertible, then (A ⊗C)−1 = A−1 ⊗C−1.
6. For square matrices A and C, tr(A ⊗C) = tr(A)tr(C).
--- page 487 ---

460
multivariate time series analysis and its applications
7. vec(A + C) = vec(A) + vec(C).
8. vec(ABC) = (C′ ⊗A) vec(B).
9. tr(AC) = vec(C′)′vec(A) = vec(A′)′vec(C).
10. tr(ABC) = vec(A′)′(C′ ⊗I)vec(B) = vec(A′)′(I ⊗B)vec(C)
= vec(B′)′(A′ ⊗I)vec(C) = vec(B′)′(I ⊗C)vec(A)
= vec(C′)′(B′ ⊗I)vec(A) = vec(C′)′(I ⊗A)vec(B).
In multivariate statistical analysis, we often deal with symmetric matrices. It
is therefore convenient to generalize the stacking operation to the half-stacking
operation, which consists of elements on or below the main diagonal. Speciﬁcally,
for a symmetric square matrix A = [aij]k×k, deﬁne
vech(A) = (a′
1., a′
2∗, . . . , a′
k∗)′,
where a1. is the ﬁrst column of A, and ai∗= (aii, ai+1,i, . . . , aki)′ is a (k −i + 1)-
dimensional vector. The dimension of vech(A) is k(k + 1)/2. For example, suppose
that k = 3. Then we have vech(A) = (a11, a21, a31, a22, a32, a33)′, which is a sixdimensional vector.
APPENDIX B: MULTIVARIATE NORMAL DISTRIBUTIONS
A k-dimensional random vector x = (x1, . . . , xk)′ follows a multivariate normal
distribution with mean µ = (µ1, . . . , µk)′ and positive-deﬁnite covariance matrix
 = [σij] if its probability density function (pdf) is
f (x|µ, ) =
1
(2π)k/2||1/2 exp

−1
2(x −µ)′−1(x −µ)

.
(8.47)
We use the notation x ∼Nk(µ, ) to denote that x follows such a distribution.
This normal distribution plays an important role in multivariate statistical analysis
and it has several nice properties. Here we consider only those properties that are
relevant to our study. Interested readers are referred to Johnson and Wichern (1998)
for details.
To gain insight into multivariate normal distributions, consider the bivariate case
(i.e., k = 2). In this case, we have
 =

 σ11
σ12
σ12
σ22

,
−1 =
1
σ11σ22 −σ 2
12

σ22
−σ12
−σ12
σ11

.
Using the correlation coefﬁcient ρ = σ12/(σ1σ2), where σi = √σii is the standard
deviation of xi, we have σ12 = ρ√σ11σ22 and || = σ11σ22(1 −ρ2). The pdf of x
then becomes
f (x1, x2|µ, ) =
1
2πσ1σ2

1 −ρ2 exp

−
1
2(1 −ρ2)[Q(x, µ, )]
"
,
--- page 488 ---

appendix c: some sca commands
461
where
Q(x, µ, ) =
x1 −µ1
σ1
	2
+
x2 −µ2
σ2
	2
−2ρ
x1 −µ1
σ1
	 x2 −µ2
σ2

.
Chapter 4 of Johnson and Wichern (1998) contains some plots of this pdf function.
Let c = (c1, . . . , ck)′ be a nonzero k-dimensional vector. Partition the random
vector as x = (x′
1, x′
2)′, where x1 = (x1, . . . , xp)′ and x2 = (xp+1, . . . , xk)′ with
1 ≤p < k. Also partition µ and  accordingly as

 x1
x2

∼N

 µ1
µ2

,

 11
12
21
22

.
Some properties of x are as follows:
1. c′x ∼N(c′µ, c′c). That is, any nonzero linear combination of x is univariate normal. The inverse of this property also holds. Speciﬁcally, if c′x is
univariate normal for any nonzero vector c, then x is multivariate normal.
2. The marginal distribution of xi is normal. In fact, xi ∼Nki(µi, ii) for i =
1 and 2, where k1 = p and k2 = k −p.
3. 12 = 0 if and only if x1 and x2 are independent.
4. The random variable y = (x −µ)′−1(x −µ) follows a chi-squared distribution with m degrees of freedom.
5. The conditional distribution of x1 given x2 = b is also normally distributed
as
(x1|x2 = b) ∼Np[µ1 + 12−1
22 (b −µ2), 11 −12−1
22 21].
The last property is useful in many scientiﬁc areas. For instance, it forms the
basis for time series forecasting under the normality assumption and for recursive
least-squares estimation.
APPENDIX C: SOME SCA COMMANDS
The following SCA commands are used in the analysis of Example 8.6:
input x1,x2. file ‘m-gs1n3-5301.txt’
% Load data
--
r1=ln(x1)
% Take log transformation
--
r2=ln(x2)
--
miden r1,r2. no ccm. arfits 1 to 8.
-- % Denote the model by v21.
mtsm v21. series r1,r2. model (i-p1*b-p2*b**2)series= @
--- page 489 ---

462
multivariate time series analysis and its applications
c+(i-t1*b)noise.
--
mestim v21.
% Initial estimation
--
p1(2,1)=0
% Set zero constraints
--
cp1(2,1)=1
--
p2(2,1)=0
--
cp2(2,1)=1
--
p2(2,2)=0
--
cp2(2,2)=1
--
t1(2,1)=0
--
ct1(2,1)=1
-- % Refine estimation and store residuals
mestim v21. method exact. hold resi(res1,res2)
--
miden res1,res2.
EXERCISES
8.1. Consider the monthly log stock returns, in percentages and including dividends, of Merck & Company, Johnson & Johnson, General Electric, General
Motors, Ford Motor Company, and value-weighted index from January 1960
to December 2008; see the ﬁle m-mrk2vw.txt.
(a) Compute the sample mean, covariance matrix, and correlation matrix of
the data.
(b) Test the hypothesis H0 : ρ1 = · · · = ρ6 = 0, where ρi is the lag-i crosscorrelation matrix of the data. Draw conclusions based on the 5% signiﬁ-
cance level.
(c) Is there any lead–lag relationship among the six return series?
8.2. The Federal Reserve Bank of St. Louis publishes selected interest rates and
U.S. ﬁnancial data on its website: http://research.stlouisfed.org/fred2/.
Consider the monthly 1-year and 10-year Treasury constant maturity rates from
April 1953 to October 2009 for 679 observations; see the ﬁle m-gs1n10.txt.
The rates are in percentages.
(a) Let ct = rt −rt−1 be the change series of the monthly interest rate rt.
Build a bivariate autoregressive model for the two change series. Discuss
the implications of the model. Transform the model into a structural form.
--- page 490 ---

exercises
463
(b) Build a bivariate moving-average model for the two change series. Discuss
the implications of the model and compare it with the bivariate AR model
built earlier.
8.3. Again consider the monthly 1-year and 10-year Treasury constant maturity
rates from April 1953 to October 2009. Consider the log series of the data
and build a VARMA model for the series. Discuss the implications of the
model obtained.
8.4. Again consider the monthly 1-year and 10-year Treasury constant maturity
rates from April 1953 to October 2009. Are the two interest rate series
threshold cointegrated? Use the interest spread st = r10,t −r1,t as the threshold variable, where rit is the i-year Treasury constant maturity rate. If they
are threshold cointegrated, build a multivariate threshold model for the two
series.
8.5. The bivariate AR(4) model xt −4xt−4 = φ0 + at is a special seasonal model
with periodicity 4, where {at} is a sequence of independent and identically
distributed normal random vectors with mean zero and covariance matrix .
Such a seasonal model may be useful in studying quarterly earnings of a
company. (a) Assume that xt is weakly stationary. Derive the mean vector
and covariance matrix of xt. (b) Derive the necessary and sufﬁcient condition
of weak stationarity for xt. (c) Show that
ℓ= 4
ℓ−4 for ℓ> 0, where
ℓ
is the lag-ℓautocovariance matrix of xt.
8.6. The bivariate MA(4) model xt = at −4at−4 is another seasonal model with
periodicity 4, where {at} is a sequence of independent and identically distributed normal random vectors with mean zero and covariance matrix .
Derive the covariance matrices
ℓof xt for ℓ= 0, . . . , 5.
8.7. Consider the monthly U.S. 1-year and 3-year Treasury constant maturity rates
from April 1953 to March 2004. The data can be obtained from the Federal
Reserve Bank of St. Louis or from the ﬁle m-gs1n3-5304.txt (1-year, 3-
year, dates). See also Example 8.6, which uses a shorter data span. Here we
use the interest rates directly without the log transformation and deﬁne xt =
(x1t, x2t)′, where x1t is the 1-year maturity rate and x2t is the 3-year maturity
rate.
(a) Identify a VAR model for the bivariate interest rate series. Write down the
ﬁtted model.
(b) Compute the impulse response functions of the ﬁtted VAR model. It suf-
ﬁces to use the ﬁrst 6 lags.
(c) Use the ﬁtted VAR model to produce 1-stepto 12-step-ahead forecasts
of the interest rates, assuming that the forecast origin is March 2004.
(d) Are the two interest rate series cointegrated, when a restricted constant
term is used? Use 5% signiﬁcance level to perform the test.
(e) If the series are cointegrated, build an ECM for the series. Write down
the ﬁtted model.
--- page 491 ---

464
multivariate time series analysis and its applications
(f) Use the ﬁtted ECM to produce 1-stepto 12-step-ahead forecasts of the
interest rates, assuming that the forecast origin is March 2004.
(g) Compare the forecasts produced by the VAR model and the ECM.
REFERENCES
Balke, N. S. and Fomby, T. B. (1997). Threshold cointegration. International Economic
Review 38: 627–645.
Box, G. E. P. and Tiao, G. C. (1977). A canonical analysis of multiple time series. Biometrika
64: 355–366.
Brenner, R. J. and Kroner, K. F. (1995). Arbitrage, cointegration, and testing the unbiasedness hypothesis in ﬁnancial markets. Journal of Financial and Quantitative Analysis
30: 23–42.
Cochrane, J. H. (1988). How big is the random walk in the GNP? Journal of Political
Economy 96: 893–920.
Dwyer, G. P. Jr., Locke, P., and Yu, W. (1996). Index arbitrage and nonlinear dynamics
between the S&P 500 futures and cash. Review of Financial Studies 9: 301–332.
Engle, R. F. and Granger, C. W. J. (1987). Cointegration and error correction representation,
estimation and testing. Econometrica 55: 251–276.
Forbes, C. S., Kalb, G. R. J., and Kofman, P. (1999). Bayesian arbitrage threshold analysis.
Journal of Business & Economic Statistics 17: 364–372.
Fuller, W. A. (1976). Introduction to Statistical Time Series. Wiley, New York.
Graybill, F. A. (1969). Introduction to Matrices with Applications in Statistics. Wadsworth,
Belmont, CA.
Hannan, E. J. and Quinn, B. G. (1979). The determination of the order of an autoregression.
Journal of the Royal Statistical Society Series B 41: 190–195.
Hillmer, S. C. and Tiao, G. C. (1979). Likelihood function of stationary multiple autoregressive moving average models. Journal of the American Statistical Association 74:
652–660.
Hosking, J. R. M. (1980). The multivariate portmanteau statistic. Journal of the American
Statistical Association 75: 602–608.
Hosking, J. R. M. (1981). Lagrange-multiplier tests of multivariate time series models.
Journal of the Royal Statistical Society Series B 43: 219–230.
Johansen, S. (1988). Statistical analysis of cointegration vectors. Journal of Economic
Dynamics and Control 12: 231–254.
Johansen, S. (1995). Likelihood Based Inference in Cointegrated Vector Error Correction
Models. Oxford University Press, Oxford, UK.
Johnson, R. A. and Wichern, D. W. (1998). Applied Multivariate Statistical Analysis, 4th
ed. Prentice Hall, Upper Saddle River, NJ.
Li, W. K. and McLeod, A. I. (1981). Distribution of the residual autocorrelations in multivariate ARMA time series models. Journal of the Royal Statistical Society Series B 43:
231–239.
L¨utkepohl, H. (2005). New Introduction to Multiple Time Series Analysis. Springer, Berlin.
Pole, A. (2007). Statistical Arbitrage. Wiley, Hoboken, NJ.
--- page 492 ---

references
465
Reinsel, G. C. (1993). Elements of Multivariate Time Series Analysis. Springer, New York.
Reinsel, G. C. and Ahn, S. K. (1992). Vector autoregressive models with unit roots and
reduced rank structure: Estimation, likelihood ratio test, and forecasting. Journal of
Time Series Analysis, 13: 353–375.
Stock, J. H. and Watson, M. W. (1988). Testing for common trends. Journal of the American
Statistical Association 83: 1097–1107.
Strang, G. (1980). Linear Algebra and Its Applications, 2nd ed. Harcourt Brace Jovanovich,
Chicago.
Tiao, G. C. and Box, G. E. P. (1981). Modeling multiple time series with applications.
Journal of the American Statistical Association 76: 802–816.
Tiao, G. C. and Tsay, R. S. (1989). Model speciﬁcation in multivariate time series (with
discussions). Journal of the Royal Statistical Society Series B 51: 157–213.
Tiao, G. C., Tsay, R. S., and Wang, T. (1993). Usefulness of linear transformations in
multivariate time series analysis. Empirical Economics 18: 567–593.
Tsay, R. S. (1991). Two canonical forms for vector ARMA processes. Statistica Sinica 1:
247–269.
Tsay, R. S. (1998). Testing and modeling multivariate threshold models. Journal of the
American Statistical Association 93: 1188–1202.
Tsay, R. S. and Tiao, G. C. (1990). Asymptotic properties of multivariate nonstationary
processes with applications to autoregressions. Annals of Statistics 18: 220–250.
Vidyamurthy, G. (2004). Pairs Trading. Wiley, Hoboken, NJ.
Zivot, E. and Wang, J. (2003). Modeling Financial Time Series with S-Plus. Springer, New
York.
--- page 493 ---
--- page 494 ---

C H A P T E R
9
Principal Component Analysis
and Factor Models
Most ﬁnancial portfolios consist of multiple assets, and their returns depend concurrently and dynamically on many economic and ﬁnancial variables. Therefore, it
is important to use proper multivariate statistical analyses to study the behavior and
properties of portfolio returns. However, as demonstrated in the previous chapter,
analysis of multiple asset returns often requires high-dimensional statistical models
that are complicated and hard to apply. To simplify the task of modeling multiple
returns, we discuss in this chapter some dimension reduction methods to search
for the underlying structure of the assets. Principal component analysis (PCA) is
perhaps the most commonly used statistical method in dimension reduction, and
we start our discussion with the method. In practice, observed return series often
exhibit similar characteristics leading to the belief that they might be driven by
some common sources, often referred to as common factors. To study the common
pattern in asset returns and to simplify portfolio analysis, various factor models
have been proposed in the literature to analyze multiple asset returns. The second
goal of this chapter is to introduce some useful factor models and demonstrate their
applications in ﬁnance.
Three types of factor models are available for studying asset returns; see Connor
(1995) and Campbell, Lo, and MacKinlay (1997). The ﬁrst type is the macroeconomic factor models that use macroeconomic variables such as growth rate of GDP,
interest rates, inﬂation rate, and unemployment rate to describe the common behavior of asset returns. Here the factors are observable and the model can be estimated
via linear regression methods. The second type is the fundamental factor models
that use ﬁrm or asset speciﬁc attributes such as ﬁrm size, book and market values, and industrial classiﬁcation to construct common factors. The third type is the
statistical factor models that treat the common factors as unobservable or latent
variables to be estimated from the returns series. In this chapter, we discuss all
Analysis of Financial Time Series, Third Edition, By Ruey S. Tsay
Copyright 2010 John Wiley & Sons, Inc.
467
--- page 495 ---

468
principal component analysis and factor models
three types of factor models and their applications in ﬁnance. Principal component
analysis and factor models for asset returns are also discussed in Alexander (2001)
and Zivot and Wang (2003).
The chapter is organized as follows. Section 9.1 introduces a general factor
model for asset returns, and Section 9.2 discusses macroeconomic factor models
with some simple examples. The fundamental factor model and its applications are
given in Section 9.3. Section 9.4 introduces principal component analysis that serves
as the basic method for statistical factor analysis. The PCA can also be used to
reduce the dimension in multivariate analysis. Section 9.5 discusses the orthogonal
factor models, including factor rotation and its estimation, and provides several
examples. Finally, Section 9.6 introduces asymptotic principal component analysis.
9.1
A FACTOR MODEL
Suppose that there are k assets and T time periods. Let rit be the return of asset i
in the time period t. A general form for the factor model is
rit = αi + βi1f1t + · · · + βimfmt + ϵit,
t = 1, . . . , T ;
i = 1, . . . , k,
(9.1)
where αi is a constant representing the intercept, {fjt|j = 1, . . . , m} are m common
factors, βij is the factor loading for asset i on the jth factor, and ϵit is the speciﬁc
factor of asset i.
For asset returns, the factor f t = (f1t, . . . , fmt)′ is assumed to be an
m-dimensional stationary process such that
E(f t) = µf ,
Cov(f t) = f ,
an m × m matrix,
and the asset speciﬁc factor ϵit is a white noise series and uncorrelated with the
common factors fjt and other speciﬁc factors. Speciﬁcally, we assume that
E(ϵit) = 0
for all i and t,
Cov(fjt, ϵis) = 0
for all j, i, t and s,
Cov(ϵit, ϵjs) =

σ 2
i ,
if i = j and t = s,
0,
otherwise.
Thus, the common factors are uncorrelated with the speciﬁc factors, and the speciﬁc
factors are uncorrelated among each other. The common factors, however, need not
be uncorrelated with each other in some factor models.
In some applications, the number of assets k may be larger than the number
of time periods T . We discuss an approach to analyze such data in Section 9.6. It
