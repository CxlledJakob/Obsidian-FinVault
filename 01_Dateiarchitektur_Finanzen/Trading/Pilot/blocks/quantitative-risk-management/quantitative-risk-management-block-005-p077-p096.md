# Quantitative Risk Management_ Concepts, Techniques, and -- Alexander J_ McNeil, Rüdiger Frey, Paul Embrechts -- Princeton series in finance, -- isbn13 9780691122557 -- 478a0059673fecd0c76229cd3d8884e7 -- Anna’s Arc.pdf — pages 77–96

--- page 77 ---

3
Multivariate Models
Financial risk models, whether for market or credit risks, are inherently multivariate.
The value change of a portfolio of traded instruments over a ﬁxed time horizon
depends on a random vector of risk-factor changes or returns. The loss incurred by
a credit portfolio depends on a random vector of losses for the individual counterparties in the portfolio. In this chapter we consider some models for random vectors
that are particularly useful for ﬁnancial data. We do this from a static, distributional
point of view without considering time series aspects, which are introduced later in
Chapter 4.
A stochastic model for a random vector can be thought of as simultaneously providing probabilistic descriptions of the behaviour of the components of the random
vector and of their dependence or correlation structure. The issue of modelling
dependent risk factors is by no means straightforward, particularly when we move
away from the multivariate normal distribution and simple generalizations thereof.
We provide a more in-depth discussion of some of the subtler issues surrounding
dependence in Chapter 5, where we introduce the subject of copulas.
The ﬁrst section of this chapter reviews basic ideas in multivariate statistics and
discusses the multivariate normal (or Gaussian) distribution and its deﬁciencies as
a model for empirical return data.
In Section 3.2 we consider a generalization of the multivariate normal distribution
known as a multivariate normal mixture distribution, which shares much of the
structure of the multivariate normal and retains many of its properties. We treat
both variance mixtures, which belong to the wider class of elliptical distributions,
and mean-variance mixtures, which allow asymmetry. Concrete examples include
t distributions and generalized hyperbolic distributions and we show in empirical
examples that these models provide a better ﬁt than a Gaussian distribution to asset
return data. In some cases multivariate return data are not strongly asymmetric and
models from the class of elliptical distributions are good enough; in Section 3.3 we
review the elegant properties of these distributions.
In the ﬁnal section we discuss the important issue of dimension reduction techniques for reducing large sets of risk factors to smaller subsets of essential risk
drivers. The key idea here is that of a factor model, and we also review the principal
components method of constructing factors.
3.1
Basics of Multivariate Modelling
This ﬁrst section reviews important basic material from multivariate statistics, which
will be known to many readers. The main topic of the section is the multivariate
--- page 78 ---

62
3. Multivariate Models
normal distribution and its properties; this distribution is central to much of classical
multivariate analysis and was the starting point for attempts to model market risk
(the variance–covariance method of Section 2.3.1).
3.1.1
Random Vectors and Their Distributions
Joint and marginal distributions.
Consider a general d-dimensional random vector
of risk-factor changes (or so-called returns) X = (X1, . . . , Xd)′. The distribution
of X is completely described by the joint distribution function (df)
FX(x) = FX(x1, . . . , xd) = P(X ⩽x) = P(X1 ⩽x1, . . . , Xd ⩽xd).
Where no ambiguity arises we simply write F, omitting the subscript.
The marginal distribution function of Xi, written FXi or often simply Fi, is the
df of that risk factor considered individually and is easily calculated from the joint
df. For all i we have
Fi(xi) = P(Xi ⩽xi) = F(∞, . . . , ∞, xi, ∞, . . . , ∞).
(3.1)
If the marginal df Fi(x) is absolutely continuous, then we refer to its derivative fi(x)
as the marginal density of Xi. It is also possible to deﬁne k-dimensional marginal
distributions of X for 2 ⩽k ⩽d −1. Suppose we partition X into (X′
1, X′
2)′, where
X1 = (X1, . . . , Xk)′ and X2 = (Xk+1, . . . , Xd)′, then the marginal distribution
function of X1 is
FX1(x1) = P(X1 ⩽x1) = F(x1, . . . , xk, ∞, . . . , ∞).
For bivariate and other low-dimensional margins it is convenient to have a simpler alternative notation in which, for example, Fij(xi, xj) stands for the marginal
distribution of the components Xi and Xj.
The df of a random vector X is said to be absolutely continuous if
F(x1, . . . , xd) =
 x1
−∞
· · ·
 xd
−∞
f (u1, . . . , ud) du1 · · · dud
for some non-negative function f , which is then known as the joint density of X.
Note that the existence of a joint density implies the existence of marginal densities
for all k-dimensional marginals. However, the existence of a joint density is not
necessarily implied by the existence of marginal densities (counterexamples can be
found in Chapter 5 on copulas).
In some situations it is convenient to work with the survival function of X deﬁned
by
¯FX(x) = ¯FX(x1, . . . , xd) = P(X > x) = P(X1 > x1, . . . , Xd > xd),
and written simply as ¯F when no ambiguity arises. The marginal survival function
of Xi, written ¯FXi or often simply ¯Fi, is given by
¯Fi(xi) = P(Xi > xi) = ¯F(−∞, . . . , −∞, xi, −∞, . . . , −∞).
--- page 79 ---

3.1. Basics of Multivariate Modelling
63
Conditional distributions and independence.
If we have a multivariate model for
risks in the form of a joint df, survival function or density, then we have implicitly
described their dependence structure. We can make conditional probability statements about the probability that certain components take certain values given that
other components take other values. For example, consider again our partition of X
into (X′
1, X′
2)′ and assume absolute continuity of the df of X. Let fX1 denote the
joint density of the k-dimensional marginal distribution FX1. Then the conditional
distribution of X2 given X1 = x1 has density
fX2|X1(x2 | x1) = f (x1, x2)
fX1(x1) ,
(3.2)
and the corresponding df is
FX2|X1(x2 | x1)
=
 xk+1
uk+1=−∞
· · ·
 xd
ud=−∞
f (x1, . . . , xk, uk+1, . . . , ud)
fX1(x1)
duk+1 · · · dud.
If the joint density of X factorizes into f (x) = fX1(x1)fX2(x2), then the conditional distribution and density of X2 given X1 = x1 are identical to the marginal
distribution and density of X2: in other words, X1 and X2 are independent.We recall
that X1 and X2 are independent if and only if
F(x) = FX1(x1)FX2(x2),
∀x,
or, in the case where X possesses a joint density, f (x) = fX1(x1)fX2(x2).
The components of X are mutually independent if and only if F(x) = d
i=1Fi(xi)
for all x ∈Rd or, in the case where X possesses a density, f (x) = d
i=1fi(xi).
Moments and characteristic function.
The mean vector of X, when it exists, is
given by
E(X) := (E(X1), . . . , E(Xd))′.
The covariance matrix, when it exists, is the matrix cov(X) deﬁned by
cov(X) := E((X −E(X))(X −E(X))′),
where the expectation operator acts componentwise on matrices. If we write Σ for
cov(X), then the (i, j)th element of this matrix is
σij = cov(Xi, Xj) = E(XiXj) −E(Xi)E(Xj),
the ordinary pairwise covariance between Xi and Xj. The diagonal elements
σ11, . . . , σdd are the variances of the components of X.
The correlation matrix of X, denoted by ρ(X), can be deﬁned by introducing a
standardized vector Y such that Yi = Xi/√var(Xi) for all i and taking ρ(X) :=
cov(Y). If we write P for ρ(X), then the (i, j)th element of this matrix is
ρij = ρ(Xi, Xj) =
cov(Xi, Xj)

var(Xi) var(Xj),
(3.3)
--- page 80 ---

64
3. Multivariate Models
the ordinary pairwise linear correlation of Xi and Xj. To express the relationship
between correlation and covariance matrices in matrix form it is useful to introduce
operators on a covariance matrix Σ as follows:
(Σ) := diag(√σ11, . . . , √σdd),
(3.4)
℘(Σ) := ((Σ))−1Σ((Σ))−1.
(3.5)
Thus (Σ) extracts from Σ a diagonal matrix of standard deviations, and ℘(Σ)
extracts a correlation matrix. The covariance and correlation matrices Σ and P of
X are related by
P = ℘(Σ).
(3.6)
Mean vectors and covariance matrices are manipulated extremely easily under
linear operations on the vector X. For any matrix B ∈Rk×d and vector b ∈Rk we
have
E(BX + b) = BE(X) + b,
(3.7)
cov(BX + b) = B cov(X)B′.
(3.8)
Covariance matrices (and hence correlation matrices) are therefore positive semideﬁnite; writing Σ for cov(X) we see that (3.8) implies that var(a′X) = a′Σa ⩾0
for any a ∈Rd. If we have that a′Σa > 0 for any a ∈Rd \ {0}, we say that Σ
is positive deﬁnite; in this case the matrix is invertible. We will make use of the
well-known Cholesky factorization of positive-deﬁnite covariance matrices at many
points; it is well known that such a matrix can be written as Σ = AA′ for a lower
triangular matrix A with positive diagonal elements. The matrix A is known as the
Cholesky factor. It will be convenient to denote this factor by Σ1/2 and its inverse by
Σ−1/2. Note that there are other ways of deﬁning the “square root” of a symmetric,
positive-deﬁnite matrix (such as the symmetric decomposition) but we will always
use Σ1/2 to denote the Cholesky factor.
In this chapter many properties of the multivariate distribution of a vector X are
demonstrated using the characteristic function, which is given by
φX(t) = E(exp(it′X)) = E(eit′X),
t ∈Rd.
3.1.2
Standard Estimators of Covariance and Correlation
Suppose we have n observations of a d-dimensional risk-factor return vector denoted
X1, . . . , Xn.Typically, these would be daily, weekly, monthly or yearly observations
forming a multivariate time series. We will assume throughout this chapter that the
observations are identically distributed in the window of observation and either
independent or at least serially uncorrelated (also known as a multivariate white
noise).As we discuss in Chapter 4, the assumption of independence may be roughly
tenable for longer time intervals such as months or years. For shorter time intervals
independence may be a less appropriate assumption (due to a phenomenon known
as volatility clustering, discussed in Chapter 4) but serial correlation of returns is
often quite weak.
--- page 81 ---

3.1. Basics of Multivariate Modelling
65
We assume that the observations X1, . . . , Xn come from a distribution with mean
vector µ, ﬁnite covariance matrix Σ and correlation matrix P.We now brieﬂy review
the standard estimators of these vector and matrix parameters.
Standard method-of-moments estimators of µ and Σ are given by the sample
mean vector ¯X and the sample covariance matrix S. These are deﬁned by
¯X := 1
n
n

i=1
Xi,
S := 1
n
n

i=1
(Xi −¯X)(Xi −¯X)′,
(3.9)
where arithmetic operations on vectors and matrices are performed componentwise.
¯X is an unbiased estimator but S is biased; an unbiased version may be obtained by
taking Su := nS/(n −1), as may be seen by calculating
nE(S) = E

n

i=1
(Xi −µ)(Xi −µ)′ −n( ¯X −µ)( ¯X −µ)′

=
n

i=1
cov(Xi) −n cov( ¯X) = nΣ −Σ,
since cov( ¯X) = n−1Σ when the data vectors are iid, or identically distributed and
uncorrelated.
The sample correlation matrix R may be easily calculated from the sample covariance matrix; its (j, k)th element is given by rjk = sjk/√sjjskk, where sjk denotes
the (j, k)th element of S. Or, using the notation introduced in (3.5), we have
R = ℘(S),
which is the analogous equation to (3.6) for estimators.
Further properties of the estimators ¯X, S and R will depend very much on the true
multivariate distribution of the observations. These quantities are not necessarily
the best estimators of the corresponding theoretical quantities in all situations. This
point is often forgotten in ﬁnancial risk management, where sample covariance
and correlation matrices are routinely calculated and interpreted with little critical
consideration of underlying models.
If our data X1, . . . , Xn are iid multivariate normal, then ¯X and S are the maximum
likelihood estimators (MLEs) of the mean vector µ and covariance matrix Σ. Their
behaviour as estimators is well understood and statistical inference for the model
parameters is described in all standard texts on multivariate analysis.
However, the multivariate normal is certainly not a good description of ﬁnancial
risk factor returns over short time intervals, such as daily data, and is often not good
over longer time intervals either. Under these circumstances the behaviour of the
standard estimators in (3.9) is often less well understood and other estimators of
the true mean vector µ and covariance matrix Σ may perform better in terms of
efﬁciency and robustness. Roughly speaking, by a more efﬁcient estimator we mean
an estimator with a smaller expected estimation error; by a more robust estimator
we mean an estimator whose performance is not so susceptible to the presence of
outlying data values.
--- page 82 ---

66
3. Multivariate Models
3.1.3
The Multivariate Normal Distribution
Deﬁnition 3.1. X = (X1, . . . , Xd)′ has a multivariate normal or Gaussian distribution if
X d= µ + AZ,
where Z = (Z1, . . . , Zk)′ is a vector of iid univariate standard normal rvs (mean
zero and variance one), and A ∈Rd×k and µ ∈Rd are a matrix and a vector of
constants, respectively.
It is easy to verify, using (3.7) and (3.8), that the mean vector of this distribution is
E(X) = µ and the covariance matrix is cov(X) = Σ, where Σ = AA′ is a positive
semideﬁnite matrix. Moreover, using the fact that the characteristic function of
a standard univariate normal variate Z is φZ(t) = exp(−1
2t2), the characteristic
function of X may be calculated to be
φX(t) = E(exp(it′X)) = exp(it′µ −1
2t′Σt),
t ∈Rd.
(3.10)
Clearly, the distribution is characterized by its mean vector and covariance matrix,
and hence a standard notation is X ∼Nd(µ, Σ). Note that the components of X are
mutually independent if and only if Σ is diagonal. For example, X ∼Nd(0, Id) if
and only if X1, . . . , Xd are iid N(0, 1), the standard univariate normal distribution.
We concentrate on the non-singular case of the multivariate normal when
rank(A) = d ⩽k. In this case the covariance matrix Σ has full rank d and is
therefore invertible (non-singular) and positive deﬁnite. Moreover, X has an absolutely continuous distribution function with joint density given by
f (x) =
1
(2π)d/2|Σ|1/2 exp{−1
2(x −µ)′Σ−1(x −µ)},
x ∈Rd,
(3.11)
where |Σ| denotes the determinant of Σ.
The form of the density clearly shows that points with equal density lie on ellipsoids determined by equations of the form (x −µ)′Σ−1(x −µ) = c, for constants
c > 0. In two dimensions the contours of equal density are ellipses, as illustrated
in Figure 3.1. Whenever a multivariate density f (x) depends on x only through
the quadratic form (x −µ)′Σ−1(x −µ), it is the density of a so-called elliptical
distribution, as discussed in more detail in Section 3.3.
Deﬁnition 3.1 is essentially a simulation recipe for the multivariate normal distribution. To be explicit, if we wished to generate a vector X with distribution
Nd(µ, Σ), where Σ is positive deﬁnite, we would use the following algorithm.
Algorithm 3.2 (simulation of multivariate normal distribution).
(1) Perform a Cholesky decomposition of Σ (see, for example, Press et al. 1992)
to obtain the Cholesky factor Σ1/2.
(2) Generate a vector Z = (Z1, . . . , Zd)′ of independent standard normal variates.
(3) Set X = µ + Σ1/2Z.
--- page 83 ---

3.1. Basics of Multivariate Modelling
67
−4
−4
−4
−4
−2
−2
−2
−2
0
0
0
0
2
2
2
2
4
4
4
−4
−2
0
2
4
4
−4
−2
0
2
4
0.1
0.1
0.2
0.3
0.3
0.4
0.5
0
0.2
0.4
0.5
0
x1
x1
−4
−2
0
2
4
x1
x2
x2
−4
−2
0
2
4
x2
x2
x1
f (x1, x2)
f (x1, x2)
(a)
(b)
Figure 3.1.
(a) Perspective and contour plots for the density of a bivariate normal distribution with standard normal margins and correlation −70%. (b) Corresponding plots for a
bivariate t density with four degrees of freedom (see Example 3.7 for details) and the same
mean vector and covariance matrix as the normal distribution. Contour lines are plotted at
the same heights for both densities.
We now summarize further useful properties of the multivariate normal. These
properties underline the attractiveness of the multivariate normal for computational
work in risk management. Note, however, that many of them are in fact shared by
the broader classes of normal mixture distributions and elliptical distributions (see
Section 3.3.3 for properties of the latter).
Linear combinations.
If we take linear combinations of multivariate normal random vectors, then these remain multivariate normal. Let X ∼Nd(µ, Σ) and take
any B ∈Rk×d and b ∈Rk. Then it is easily shown, for example using the characteristic function (3.10), that
BX + b ∼Nk(Bµ + b, BΣB′).
(3.12)
As a special case, if a ∈Rd, then
a′X ∼N(a′µ, a′Σa),
(3.13)
and this fact is used routinely in the variance–covariance approach to risk management, as discussed in Section 2.3.1.
In this context it is interesting to note the following elegant characterization of
multivariate normality. It is easily shown using characteristic functions that X is
multivariate normal if and only if a′X is univariate normal for all vectors a ∈
Rd \ {0}.
--- page 84 ---

68
3. Multivariate Models
Marginal distributions.
It is clear from (3.13) that the univariate marginal distributions of X must be univariate normal. More generally, using the X = (X′
1, X′
2)′
notation from Section 3.1.1 and extending this notation naturally to µ and Σ,
µ =

µ1
µ2

,
Σ =

Σ11
Σ12
Σ21
Σ22

,
property (3.12) implies that the marginal distributions of X1 and X2 are also multivariate normal and are given by X1 ∼Nk(µ1, Σ11) and X2 ∼Nd−k(µ2, Σ22).
Conditional distributions.
Assuming that Σ is positive deﬁnite, the conditional
distributionsofX2 givenX1 andofX1 givenX2 mayalsobeshowntobemultivariate
normal. For example, X2 | X1 = x1 ∼Nd−k(µ2.1, Σ22.1), where
µ2.1 = µ2 + Σ21Σ−1
11 (x1 −µ1)
and
Σ22.1 = Σ22 −Σ21Σ−1
11 Σ12
are the conditional mean vector and covariance matrix.
Quadratic forms.
If X ∼Nd(µ, Σ) with Σ positive deﬁnite, then
(X −µ)′Σ−1(X −µ) ∼χ2
d ,
(3.14)
a chi-squared distribution with d degrees of freedom. This is seen by observing that
Z = Σ−1/2(X −µ) ∼Nd(0, Id) and (X −µ)′Σ−1(X −µ) = Z′Z ∼χ2
d . This
property (3.14) is useful for checking multivariate normality (see Section 3.1.4).
Convolutions.
If X and Y are independent d-dimensional random vectors satisfying X ∼Nd(µ, Σ) and Y ∼Nd( ˜µ, ˜Σ), then we may take the product of characteristic functions to show that X + Y ∼Nd(µ + ˜µ, Σ + ˜Σ).
3.1.4
Testing Normality and Multivariate Normality
We now consider the issue of testing whether the data X1, . . . , Xn are observations
from a multivariate normal distribution.
Univariate tests.
If X1, . . . , Xn are iid multivariate normal, then for 1 ⩽j ⩽d
the univariate sample X1,j, . . . , Xn,j consisting of the observations of the jth component must be iid univariate normal; in fact any univariate sample constructed from
a linear combination of the data of the form a′X1, . . . , a′Xn must be iid univariate
normal. This can be assessed graphically with a QQplot against a standard normal
reference distribution or tested formally using one of the countless numerical tests
of normality.A QQplot (quantile–quantile plot) is a standard visual tool for showing
the relationship between empirical quantiles of the data and theoretical quantiles of a
reference distribution, with a lack of linearity showing evidence against the hypothesized reference distribution. In Figure 3.2 we show a QQplot of daily returns of
the Disney share price from 1993 to 2000 against a normal reference distribution;
the inverted “S-shaped” curve of the points suggests that the empirical quantiles of
the data tend to be larger than the corresponding quantiles of a normal distribution,
indicating that the normal distribution is a poor model for these returns.
--- page 85 ---

3.1. Basics of Multivariate Modelling
69
•
•
•
•
•
•
•
• •
•
•
•
•
••
•
•
•
• •
•
••
•
•
•
•
•
• •
•
•
•
•
•
•
•
••
•
•
•
•
•
••
•
•
•
•
••
•
•
••
•
•
•
•
• •
•
•
•
•
•
•
•
•
•
• •
•
•
••
•
•
•
•
•
•
•
•
••
•
•
•
•
•
•
•
•
•
•
•
•
•
•
•
•
•
•
•
•
•
•
•
•
•
•
•
•
•
••
•
•
•
•
•
•
•
•
•
•
•
•
•
•
•
•
•
••
•
•
•
•
•
•
•
•
•
•
•
•
••
•
• ••
•
•
•
•
•
•
•
•
•
•
• • •
•
•
• •
•
•
•
•
•
•
•
• •
•
•
• •
•
•
•
•
••
•
•
•
••
•
•••
•
•
•
•
•
•
•
• •
•
•
•
•
•
•
•
•
•
• •
•
•
•
•
•
• •
•
•
•
• •
••
•••
•
•
••
•
•
•
•
•
•
•
•
•
•
•
• ••
•
•
•
• •
•
•
•
••
•
•
•
•
•
•
•
•
• •
•
•
•
•
•
•
••
•
•
•
•
•
•
•
•
••
•
•
•
•
•
•
•
•
•
•
•
•
•
•
••
••
• • •
••
•
•
• •
•
•
•
•
•
•
•
•
•
•
• •
•
•
•
•
•
•
•
•
•
•
•
•
•
•
•
•
•
•
••
• • •
•
•
•
•
•
••
• ••
•
••
•
•
••
•
•
•
•
• •
•
••
••
••
•
•
•
••
•
•
•
•
•
•
•
•
•
•
•
•
•
•
•
•
•
•
•
•
•
•
•
•
•
•
•
•
•
•
•
•
•
•
•
•
•
•
•
•
•
•
•
•
•
•
•
•
•
•
•
• •
•
••
•
•
•
•
••
••
•
•
•
•
• •
•
• •
• •
•
••
•
•
•
•
•
•
•
•
•
•
•
•
• •
•
•
•
•
•
•
•
••
•
••
•
•
••
•
•
•
•
•
•
•
••
•
•
•
•
••
•
•
•
•
•
•
•• •
•
•
•
• •
•
•
•
•
• ••
•
•
•
•
••
•
••
•
•
••
•
•
•
•
• •
•
•
•
•
•
•
•
•
• ••
••
•
•
•
•
•
•
•
•
•
•
• •
•
•
•
•
• ••
•
•
•
• •
•
•
•
•
•
••
• • •
•
•
•
•
•
•• •
•
• •
•
•
•
•
••
•
••
•
•• •
••
•
•
•
•
•
••
•
••
•
•
•
•
•
•••• •
•
• •
•
• •
•
•
•
• ••
•
•
•
••
•
••
•
•
• •
•
•
•
••
•
•
•
•
• •
••
•
•
•
•
•
•
•
•
•
•
•
•
•
•
•
••
••
• •
•
•
•
•
•
•
•
•
•
•
• •
•
• •
• •
•
• •
•
•
•
•
••
•
•
••
• •
•
• •
•
•
•
•
• •
•
•
•
•
• •
••
•
• •
•
•
•
•
•
•
•
•
•
•
••
•
•
•
••
• •
•
•
•
•
•
••
•
•
•
•
• •
•
• •
•
•
•••••
•
•
•
•
•
•••
•
•
•
•
•
• •
•
•
•
•
•
•
•
•
•
•
•
•
•
•
•
•
•
•
•
•
•
•
•
•
•
•
•
•
•
•
•
•
•
•
• •
•
•
•
•
•
•
•
•
•
•
•
•
•
•
• •
•
•
•
•
••
•
•
•
•
•
•
•
•
•
•
•
•
•
•
•
•
••
•
•
• •• •
••
•
•
•
• •
•
•
•
•
•
• •
•
•
•
•
•
•
•
•
• •
•
• •
•
•
•
•
•
•
•
•
•
•
•
•
•
•
•
•
•
•
• •
•
•
• •
•
•
•
•
••
•
•
•
•
•
••
•
•
•
•
•
•
•
••
•
•
•
• •
••
•
•
•
•
•
•
•
• •
•
•
•
• •
•
•
••
•
•
•
••
•
•
•
•
•
•
•
••
•
•••
• •
•
•
•
•
•
•
•
•
•
•
•
••
•
•
•
••
•
•
•
•
•
•
•
•
•
•
•
•
•
•
•
•
•
•
•
•
•
•
•
•
•
•
•
•
•
••
•
•
•
•
•
•
•
•
•
•
• •
•
•
•
•
•
•
•
•• •
••
•
•
•
•
• •
•
•
•
•
•
•
•
•
•
•
•
•
••
•
•
•
•
•
•
•
•
•
•
•
• ••
•• •
•
• ••
• •
•
•
•
•
•
•
•
•
•
•
•
•
•
••
•
•
•
•
•
•
•
•
•
•
•
•
•
•
•••
•
•
•
•
•
•
•
•
•
•
••
••
•
•
•
•
•
•
•
•
•
•
•
•
•
•
• •
• • •
•
••
•
•
•
•
•
•
•
•
•
•
•
•
•
•
•
•••
•
•
•
•
•••
• •
•
•
•
•
•
•
•
•
•
•••
•
•
•
•
•
•
•
•
•
•
•
•
•
•
•
•
•
•
•
•
•
•
•
•
•
•
• •
•
•
•
••
•
•• ••
•
•
•
•
•
•
•
•
•
•
•
•
•
•
•
•
• •
•
•• •
•
•
•
•
• •
•
• •
•
•
••
•
•
•
•
•
•
•
•
•
• • ••
•
•
••
• •
•
•
•
•
••
•
•
•
•
•
•
•
•
•
•
•
•
•
•
•
•
•
•
•
••
•
•
•
•
•
•
•
•
•
•
•
•
••
•
•
•
•
•
•
•
• •
•
•
•
•
•
•
••
•
•
•
•
•
••
•
•
•
•
• •
•
•
•
•
•
•
•
•
•
•••
•
•
•
•
•
•
•
•
•
•
•
•
•
•
•
•
•
••
•
•
•
•
•
• •
•
•
•
•
•
•
••
•
•
•
•
•
•
•
•
•
•
•
•
•
•
•
•
•
•
•
•
•
• •
•
•
• •
•
•
•
•
•
••
•
•
•
•
•
• •
•
•
•
•
• •
•
•
•
•
•
•
•
•
•
•
•
•
•
• •
•
•
•
•
•
•
•
•
•
•
•
•
•
•
•••
•
•
•
•
•
•
•
•
••
•
• •
•
•
•
•
•
• •
•
• •
•
•
•
•
••
••
•
•
•
•
•
•
•
••
•
• •
•
••
•
•
••
•
•
•
•
•
•
•
•
•
•
•
•
••
•
•
•
•
•
•
•
•
•
•
•
•
•
•
•
•
•
•
•
•
•
• •
•
• •
•
••
•
•
•
•
•
•
•
•
•
•
•
•
•
•
•
•
••
•
•
•
•
•
•
•
•
•
• • •
•
•
•
•
•
•
•
•
•
•
•
•
•
•
•
• ••
••
•
•
•
•
•
•
•
•
••
••
•
•
•
•
•
•
•
•
•
•
•
•
•
•
• •
•
•
•
•
•• •
•
•
•
•
•
•
•
•
•
• •
•
•
•
•
•
•
•
•
•
•
•
•
•
•
•
•
•
•
•
•
•
•
•
•
•
•
•
•
•
•
•
•
•
•
• •
•
•
•
•
• •
•
•
•
•
•
•
•
•
•
•
••
•
•
••
•
•
•
•
•
•
••
••
•
•
•
•
•
•
••
•
•
•
• •
•
•
•
•
• •
•
•
•
•
•
•
•
•
••
•
•
•
•
•
•
••
• •
• •
•
•
••
• •
•
•
•
•
•
•
•
• •
•
•
•
•
• •
•
•
•
•
•
•
•
•
••
•
•
•
•
•
•
•
•
•
•
•
•
•
•
•
•
•
•
•
•
• •
•
•
•
•
•
•
•
•
• •
•
•
•
• ••••
•
••
•
•
•
•
•
• •
•
• •
•
•
•
•
•
•
•
•
•
•
•
•
•
•
•
•
•
•
•
•
•
•
•
•
•
Quantiles of standard normal
Disney
−2
0
−0.15
−0.10
−0.05
0
0.05
0.10
0.15
2
Figure 3.2.
QQplot of daily returns of the Disney share price from 1993 to 2000
against a normal reference distribution (see also Example 3.3).
Particularly useful numerical tests include those of Jarque and Bera, Anderson
and Darling, Shapiro and Wilk, and D’Agostino. The Jarque–Bera test belongs to
the class of omnibus moment tests, i.e. tests which assess simultaneously whether
the skewness and kurtosis of the data are consistent with a Gaussian model. The
sample skewness and kurtosis coefﬁcients of a univariate sample Z1, . . . , Zn are
deﬁned by
√
b =
(1/n) n
i=1(Zi −¯Z)3
((1/n) n
i=1(Zi −¯Z)2)3/2 ,
k =
(1/n) n
i=1(Zi −¯Z)4
((1/n) n
i=1(Zi −¯Z)2)2 .
(3.15)
These are designed to estimate the theoretical skewness and kurtosis, which are
deﬁned, respectively, by √β = E(Z −µ)3/σ 3 and κ = E(Z −µ)4/σ 4, where
µ = E(Z) and σ 2 = var(Z) denote mean and variance; √β and κ take the values
zero and three for a normal variate Z. The Jarque–Bera test statistic is
T = 1
6n(b + 1
4(k −3)2)
and has an asymptotic chi-squared distribution with two degrees of freedom under
the null hypothesis of normality; sample kurtosis values differing widely from three
and skewness values differing widely from zero may lead to rejection of normality.
Multivariate tests.
To test for multivariate normality it is not sufﬁcient to test that
the univariate margins of the distribution are normal. We will see in Chapter 5 that
it is possible to have multivariate distributions with normal margins that are not
themselves multivariate normal distributions. Thus we also need to be able to test
joint normality and a simple way of doing this is to exploit the fact that the quadratic
form in (3.14) has a chi-squared distribution. Suppose we estimate µ and Σ using
the standard estimators in (3.9) and construct the data
{D2
i = (Xi −¯X)′S−1(Xi −¯X) : i = 1, . . . , n}.
(3.16)
--- page 86 ---

70
3. Multivariate Models
Because the estimates of the mean vector and the covariance matrix are used in the
construction of each D2
i , these data are not independent, even if the original Xi data
were. Moreover, the marginal distribution of D2
i under the null hypothesis is not
exactly chi-squared; we have in fact that n(n −1)−2D2
i ∼Beta( 1
2d, 1
2(n −d −1)),
sothatthetruedistributionisascaledbetadistribution,althoughitturnsouttobevery
close to chi-squared for large n. We expect D2
1, . . . , D2
n to behave roughly like an
iid sample from a χ2
d distribution and for simplicity we construct QQplots against
this distribution. (It is also possible to make QQplots against the beta reference
distribution and these look very similar.)
Numerical tests of multivariate normality based on multivariate measures of skewness and kurtosis are also possible. Suppose we deﬁne, in analogy to (3.15),
bd = 1
n2
n

i=1
n

j=1
D3
ij,
kd = 1
n
n

i=1
D4
i ,
(3.17)
where Di is given in (3.16) and is known as the Mahalanobis distance between
Xi and ¯X, and Dij = (Xi −¯X)S−1(Xj −¯X) is known as the Mahalanobis angle
between Xi −¯X and Xj −¯X. These measures in fact reduce to the univariate measures b and k in the case d = 1. Under the null hypothesis of multivariate normality
the asymptotic distributions of these statistics as n →∞are
1
6nbd ∼χ2
d(d+1)(d+2)/6,
kd −d(d + 2)
√8d(d + 2)/n ∼N(0, 1).
(3.18)
Mardia’s test of multinormality involves comparing the skewness and kurtosis statistics with the above theoretical reference distributions. Since large values of the
statistics cast doubt on the multivariate normal model, one-sided tests are generally
performed. Usually the tests of kurtosis and skewness are performed separately,
although there are also a number of joint (or so-called omnibus) tests (see Notes and
Comments).
Example 3.3 (on the normality of returns on Dow Jones 30 stocks). We applied
tests of normality to an arbitrary subgroup of 10 of the stocks comprising the Dow
Jones index (seeTable 3.1 for the stock codes andTable 4.1 for names).We took eight
years of data spanning the period 1993–2000 and formed daily, weekly, monthly
and quarterly logarithmic returns. For each stock we calculated sample skewness
and kurtosis and applied the Jarque–Bera test to the univariate time series. The daily
and weekly return data fail all tests; in particular, it is notable that there are some
large values for the sample kurtosis. For the monthly data, the null hypothesis of
normality is not formally rejected (p-value greater than 0.05) for four of the stocks;
for quarterly data it is not rejected for ﬁve of the stocks, although here the sample
size is small.
We applied Mardia’s tests of multinormality based on both multivariate skewness
and kurtosis to the multivariate data for all 10 stocks. The results are shown in
Table 3.2. We also compared the D2
i data (3.16) to a χ2
10-distribution using a QQplot
(see Figure 3.3).
--- page 87 ---

3.1. Basics of Multivariate Modelling
71
Table 3.1.
Sample skewness (
√
b) and kurtosis (k) coefﬁcients as well as p-values for
Jarque–Bera tests of normality for an arbitrary set of 10 of the Dow Jones 30 stocks (see
Example 3.3 for details).
Stock
√
b
k
p-value
√
b
k
p-value
Daily returns, n = 2020
Weekly returns, n = 416






AXP
0.05
5.09
0.00
−0.01
3.91
0.00
EK
−1.93
31.20
0.00
−1.13
14.40
0.00
BA
−0.34
10.89
0.00
−0.26
7.54
0.00
C
0.21
5.93
0.00
0.44
5.42
0.00
KO
−0.02
6.36
0.00
−0.21
4.37
0.00
MSFT
−0.22
8.04
0.00
−0.14
5.25
0.00
HWP
−0.23
6.69
0.00
−0.26
4.66
0.00
INTC
−0.56
8.29
0.00
−0.65
5.20
0.00
JPM
0.14
5.25
0.00
−0.20
4.93
0.00
DIS
−0.01
9.39
0.00
0.08
4.48
0.00
Monthly returns, n = 96
Quarterly returns, n = 32






AXP
−1.22
5.99
0.00
−1.04
4.88
0.01
EK
−1.52
10.37
0.00
−0.63
4.49
0.08
BA
−0.50
4.15
0.01
−0.15
6.23
0.00
C
−1.10
7.38
0.00
−1.61
7.13
0.00
KO
−0.49
3.68
0.06
−1.45
5.21
0.00
MSFT
−0.40
3.90
0.06
−0.56
2.90
0.43
HWP
−0.33
3.47
0.27
−0.38
3.64
0.52
INTC
−1.04
6.50
0.00
−0.42
3.10
0.62
JPM
−0.51
5.40
0.00
−0.78
7.26
0.00
DIS
0.04
3.26
0.87
−0.49
4.32
0.16
Table 3.2.
Mardia’s tests of multivariate normality based on the multivariate measures of
skewness and kurtosis in (3.17) and the asymptotic distributions in (3.18) (see Example 3.3
for details).
Daily
Weekly
Monthly
Quarterly
n
2020
416
96
32
b10
9.31
9.91
21.10
50.10
p-value
0.00
0.00
0.00
0.02
k10
242.45
177.04
142.65
120.83
p-value
0.00
0.00
0.00
0.44
The daily, weekly and monthly return data fail the multivariate tests of normality. For quarterly return data the multivariate kurtosis test does not reject the null
hypothesis, but the skewness test does; the QQplot in Figure 3.3(d) looks slightly
more linear. Thus there is some evidence that returns over a quarter year are close to
beingnormallydistributed,whichmightindicateacentrallimittheoremeffecttaking
--- page 88 ---

72
3. Multivariate Models
•••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••
•
•
0
10
15
20
25
30
0
50
100
150
200
250
•••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••• •
•
5
10
15
20
25
30
0
20
40
60
•••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••
•••• •
•
•
5
10
15
20
25
10
20
30
40
• ••••••••••••••••••••••••
••
• •
• •
•
5
10
15
20
5
10
15
20
χ2
10 quantile
χ2
10 quantile
Ordered D2 data
Ordered D2 data
5
(a)
(b)
(c)
(d)
Figure 3.3.
QQplot of the D2
i data in (3.16) against a χ2
10 distribution for the datasets of
Example 3.3: (a) daily analysis; (b) weekly analysis; (c) monthly analysis; and (d) quarterly
analysis. Under the null hypothesis of multivariate normality these should be roughly linear.
place, although the sample size is too small to reach any more reliable conclusion.
The evidence against the multivariate normal distribution is certainly overwhelming
for daily, weekly and monthly data.
The results in Example 3.3 are fairly typical for ﬁnancial return data.This suggests
that in many risk-management applications the multivariate normal distribution is
not a good description of reality. It has three main defects that we will discuss at
various points in this book.
(1) The tails of its univariate marginal distributions are too thin; they do not assign
enough weight to extreme events.
(2) The joint tails of the distribution do not assign enough weight to joint extreme
outcomes.
(3) The distribution has a strong form of symmetry, known as elliptical symmetry.
In the next section we look at models that address some of these defects. We consider normal variance mixture models, which share the elliptical symmetry of the
multivariate normal, but have the ﬂexibility to address (1) and (2) above; we also
look at normal mean-variance mixture models, which introduce some asymmetry
and thus address (3).
--- page 89 ---

3.2. Normal Mixture Distributions
73
Notes and Comments
Much of the material covered brieﬂy in Section 3.1 can be found in greater detail
in standard texts on multivariate statistical analysis such as Mardia, Kent and Bibby
(1979), Seber (1984), Giri (1996) or Johnson and Wichern (2002).
There are countless possible tests of univariate normality and a good starting point
is the entry on “departures from normality, tests for” in volume 2 of the Encyclopedia
of Statistics (Kotz, Johnson and Read 1985). For an introduction to QQplots see Rice
(1995, pp. 353–357); for the widely applied Jarque–Bera test based on the sample
skewness and kurtosis, see Jarque and Bera (1987).
The true distribution of D2
i = (Xi −¯X)S−1(Xi −¯X) for iid Gaussian data was
shown by Gnanadesikan and Kettenring (1972) to be a scaled beta distribution
(see also Gnanadesikan 1997). The implications of this fact for the construction of
QQplots in small samples are considered by Small (1978). References for multivariate measures of skewness and kurtosis and Mardia’s test of multinormality are
Mardia (1970, 1974, 1975). See also Mardia, Kent and Bibby (1979), the entry on
“multivariate normality, testing for” in volume 6 of the Encyclopedia of Statistics
(Kotz, Johnson and Read 1985), and the entry on “Mardia’s test of multinormality”
in volume 5 of the same publication.
3.2
Normal Mixture Distributions
In this section we generalize the multivariate normal to obtain multivariate normal
mixture distributions. The crucial idea is the introduction of randomness into ﬁrst
the covariance matrix and then the mean vector of a multivariate normal distribution
via a positive mixing variable, which will be known throughout as W.
3.2.1
Normal Variance Mixtures
Deﬁnition 3.4. The random vector X is said to have a (multivariate) normal variance
mixture distribution if
X d= µ +
√
WAZ,
(3.19)
where
(i) Z ∼Nk(0, Ik);
(ii) W ⩾0 is a non-negative, scalar-valued rv which is independent of Z, and
(iii) A ∈Rd×k and µ ∈Rd are a matrix and vector of constants, respectively.
Such distributions are known as variance mixtures, since if we condition on the rv
W we observe that X | W = w ∼Nd(µ, wΣ), where Σ = AA′. The distribution
of X can be thought of as a composite distribution constructed by taking a set of
multivariate normal distributions with the same mean vector and with the same
covariance matrix up to a multiplicative constant w. The mixture distribution is
constructed by drawing randomly from this set of component multivariate normals
according to a set of “weights” determined by the distribution of W; the resulting
mixture is not itself a multivariate normal distribution. In the context of modelling
--- page 90 ---

74
3. Multivariate Models
risk-factor returns, the mixing variable W could be interpreted as a shock that arises
from new information and impacts the volatilities of all stocks.
As for the multivariate normal, we are most interested in the case where rank(A) =
d ⩽k and Σ is a full-rank, positive-deﬁnite matrix; this will give us a non-singular
normal variance mixture.
Provided that W has a ﬁnite expectation, we may easily calculate that
E(X) = E(µ +
√
WAZ) = µ + E(
√
W)AE(Z) = µ
and that
cov(X) = E((
√
WAZ)(
√
WAZ)′) = E(W)AE(ZZ′)A′ = E(W)Σ.
(3.20)
We refer to µ and Σ in general as the location vector and the dispersion matrix of
the distribution. Note that Σ (the covariance matrix of AZ) is only the covariance
matrix of X if E(W) = 1 and that µ is only the mean vector when E(X) is deﬁned,
which requires E(W 1/2) < ∞. The correlation matrices of X and Z are the same
when E(W) < ∞. Note also that these distributions provide good examples of
models where a lack of correlation does not necessarily imply independence of the
components of X; indeed we have the following simple result.
Lemma 3.5. Let (X1, X2) have a normal mixture distribution with A = I2 and
E(W) < ∞so that cov(X1, X2) = 0. Then X1 and X2 are independent if and only
if W is almost surely constant, i.e. (X1, X2) are normally distributed.
Proof. We calculate that
E(|X1||X2|) = E(W|Z1||Z2|) = E(W)E(|Z1|)E(|Z2|)
⩾(E(
√
W))2E(|Z1|)E(|Z2|) = E(|X1|)E(|X2|),
with equality throughout only when W is a constant.
Using (3.10), we can calculate that the characteristic function of a normal variance
mixture is given by
φX(t) = E(E(exp(it′X) | W)) = E(exp(it′µ −1
2Wt′Σt))
= exp(it′µ) ˆH( 1
2t′Σt).
(3.21)
where ˆH(θ) =
 ∞
0
e−θv dH(v) is the Laplace–Stieltjes transform of the df H of
W. Based on (3.21) we use the notation X ∼Md(µ, Σ, ˆH) for normal variance
mixtures.
Assuming that Σ is positive deﬁnite and that the distribution of W has no point
mass at zero, we may derive the joint density of a normal variance mixture distribution. Writing fX|W for the (Gaussian) conditional density of X given W, the density
of X is given by
f (x) =

fX|W(x | w) dH(w)
=

w−d/2
(2π)d/2|Σ|1/2 exp

−(x −µ)′Σ−1(x −µ)
2w

dH(w),
(3.22)
--- page 91 ---

3.2. Normal Mixture Distributions
75
in terms of the Lebesgue–Stieltjes integral; when H has density h we simply mean
the Riemann integral
 ∞
0
fX|W(x | w)h(w) dw.All such densities will depend on x
only through the quadratic form (x −µ)′Σ−1(x −µ) and this means they are the
densities of elliptical distributions, as will be discussed in Section 3.3.
Example 3.6 (multivariate two-point normal mixture distribution). Simple
examples of normal mixtures are obtained when W is a discrete rv. For example, the two-point normal mixture model is obtained by taking W in (3.19) to be a
discrete rv which assumes the distinct positive values k1 and k2 with probabilities p
and 1 −p, respectively. By setting k2 large relative to k1 and choosing p large, this
distribution might be used to deﬁne two regimes: an ordinary regime that holds most
of the time and a stress regime that occurs with small probability 1 −p. Obviously
this idea extends to k-point mixture models.
Example 3.7 (multivariate t distribution). If we take W in (3.19) to be an rv with
an inverse gamma distribution W ∼Ig( 1
2ν, 1
2ν) (which is equivalent to saying that
ν/W ∼χ2
ν ), then X has a multivariate t distribution with ν degrees of freedom
(see SectionA.2.6 for more details concerning the inverse gamma distribution). Our
notation for the multivariate t is X ∼td(ν, µ, Σ) and we note that Σ is not the
covariance matrix of X in this deﬁnition of the multivariate t. Since E(W) = ν/(ν−
2) we have cov(X) = (ν/(ν −2))Σ and the covariance matrix (and correlation
matrix) of this distribution are only deﬁned if ν > 2.
Using (3.22), the density can be calculated to be
f (x) =
Γ ( 1
2(ν + d))
Γ ( 1
2ν)(πν)d/2|Σ|1/2

1 + (x −µ)′Σ−1(x −µ)
ν
−(ν+d)/2
.
(3.23)
Clearly, the locus of points with equal density is again an ellipsoid with equation
(x −µ)′Σ−1(x −µ) = c, for some c > 0. A bivariate example with four degrees
of freedom is given in Figure 3.1. In comparison with the multivariate normal the
contours of equal density rise more quickly in the centre of the distribution and decay
more gradually on the “lower slopes” of the distribution. We will see later that, in
comparison with the multivariate normal, the multivariate t has heavier marginal
tails (Chapter 7) and a more pronounced tendency to generate simultaneous extreme
values (Section 5.3.1).
Example 3.8 (symmetric generalized hyperbolic distribution). A ﬂexible family
of normal variance mixtures is obtained by taking W in (3.19) to have a generalized
inverse Gaussian (GIG) distribution, W ∼N−(λ, χ, ψ) (see Section A.2.5). Using
(3.22), it can be shown that a normal variance mixture constructed with this mixing
density has the joint density
f (x) =
(√χψ)−λψd/2
(2π)d/2|Σ|1/2Kλ(√χψ)
Kλ−(d/2)(

(χ + (x −µ)′Σ−1(x −µ))ψ)
(

(χ + (x −µ)′Σ−1(x −µ))ψ)(d/2)−λ ,
(3.24)
where Kλ denotes a modiﬁed Bessel function of the third kind (see Section A.2.5
for more details). This distribution is a special case of the more general family of
--- page 92 ---

76
3. Multivariate Models
multivariate generalized hyperbolic distributions, which we will discuss in greater
detail in Section 3.2.2. The more general family can be obtained as mean-variance
mixtures of normals, which are not necessarily elliptical distributions.
The GIG mixing distribution is very ﬂexible and contains the gamma and inverse
gamma distributions as special boundary cases (corresponding, respectively, to λ >
0, χ = 0 and to λ < 0, ψ = 0). In these cases the density in (3.24) should be
interpreted as a limit as χ →0 or as ψ →0. (Information on the limits of Bessel
functions is found in Section A.2.5.) The gamma mixing distribution yields Laplace
distributions or so-called symmetric variance-gamma models and the inverse gamma
yields the t as in Example 3.7; to be precise the t corresponds to the case when λ =
−ν/2 and χ = ν. The special cases λ = −0.5 and λ = 1 have also had attention in
ﬁnancial modelling. The former gives rise to the symmetric normal inverse Gaussian
(NIG) distribution; the latter gives rise to a symmetric multivariate distribution
whose one-dimensional margins are known simply as hyperbolic distributions.
To calculate the covariance matrix of distributions in the symmetric generalized
hyperbolic family, we require the mean of the GIG distribution, which is given
in (A.9) for the case χ > 0 and ψ > 0. The covariance matrix of the multivariate
distribution in (3.24) follows from (3.20).
Normal variance mixture distributions are easy to work with under linear operations, as shown in the following simple proposition.
Proposition 3.9. If X ∼Md(µ, Σ, ˆH) and Y = BX + b, where B ∈Rk×d and
b ∈Rk, then Y ∼Mk(Bµ + b, BΣB′, ˆH).
Proof. The characteristic function in (3.21) may be used to show that
φY (t) = E(eit′(BX+b)) = eit′bφX(B′t) = eit′(Bµ+b) ˆH( 1
2t′BΣB′t).
Thus the subclass of mixture distributions speciﬁed by ˆH is closed under linear
transformations. For example, if X has a multivariate t distribution with ν degrees
of freedom, then so does any linear transformation of X; the linear combination a′X
would have a univariate t distribution with ν degrees of freedom (more precisely,
the distribution a′X ∼t1(ν, a′µ, a′Σa)).
Normal variance mixture distributions (and the mean-variance mixtures considered later in Section 3.2.2) are easily simulated, the method being obvious from
Deﬁnition 3.4. To generate a variate X ∼Md(µ, Σ, ˆH) with Σ positive deﬁnite we
use the following algorithm.
Algorithm 3.10 (simulation of normal variance mixtures).
(1) Generate Z ∼Nd(0, Σ) using Algorithm 3.2.
(2) Generate independently a positive mixing variable W with df H (corresponding to the Laplace–Stieltjes transform ˆH).
(3) Set X = µ +
√
WZ.
--- page 93 ---

3.2. Normal Mixture Distributions
77
To generate X ∼td(ν, µ, Σ), the mixing variable W should have an Ig( 1
2ν, 1
2ν) distribution; it is helpful to note that in this case ν/W ∼χ2
ν , a chi-squared distribution
on ν degrees of freedom. Sampling from a generalized hyperbolic distribution with
density (3.24) requires us to generate W ∼N−(λ, χ, ψ). Sampling from the GIG
distribution can be accomplished using a rejection algorithm proposed by Atkinson
(1982).
3.2.2
Normal Mean-Variance Mixtures
All of the multivariate distributions we have considered so far have elliptical symmetry and this may well be an oversimpliﬁed model for real risk-factor return data.
Among other things, elliptical symmetry implies that all one-dimensional marginal
distributions are rigidly symmetric, which contradicts the frequent observation for
stock returns that negative returns (losses) have heavier tails than positive returns
(gains). The models we now introduce attempt to add some asymmetry to the class
of normal mixtures by mixing normal distributions with different means as well
as different variances; this yields the class of multivariate normal mean-variance
mixtures.
Deﬁnition 3.11. The random vector X is said to have a (multivariate) normal meanvariance mixture distribution if
X d= m(W) +
√
WAZ,
(3.25)
where
(i) Z ∼Nk(0, Ik);
(ii) W ⩾0 is a non-negative, scalar-valued rv which is independent of Z;
(iii) A ∈Rd×k is a matrix; and
(iv) m : [0, ∞) →Rd is a measurable function.
In this case we have that
X | W = w ∼Nd(m(w), wΣ),
(3.26)
where Σ = AA′ and it is clear why such distributions are known as mean-variance
mixtures of normals. In general, such distributions are not elliptical.
A possible concrete speciﬁcation for the function m(W) in (3.26) is
m(W) = µ + Wγ ,
(3.27)
where µ and γ are parameter vectors in Rd. Since E(X | W) = µ + Wγ and
cov(X | W) = WΣ, it follows in this case by simple calculations that
E(X) = E(E(X | W)) = µ + E(W)γ ,
(3.28)
cov(X) = E(cov(X | W)) + cov(E(X | W))
= E(W)Σ + var(W)γ γ ′,
(3.29)
--- page 94 ---

78
3. Multivariate Models
when the mixing variable W has ﬁnite variance. We observe from (3.28) and (3.29)
that the parameters µ and Σ are not, in general, the mean vector and covariance
matrix of X (or a multiple thereof). This is only the case when γ = 0, so that the
distribution is a normal variance mixture and the simpler moment formulas given
in (3.20) apply.
3.2.3
Generalized Hyperbolic Distributions
In Example 3.8 we looked at the special subclass of the generalized hyperbolic distributions consisting of the elliptically symmetric normal variance mixture distributions. The full generalized hyperbolic family is obtained using the mean-variance
mixture construction (3.25) and the conditional mean speciﬁcation (3.27). For the
mixing distribution we assume that W ∼N−(λ, χ, ψ), a GIG distribution with
density (A.8).
Remark 3.12. This class of distributions has received a lot of attention in the
ﬁnancial-modelling literature, particularly in the univariate case. An important reason for this attention is their link to L´evy processes, i.e. processes with independent
and stationary increments (like Brownian motion) that are used to model price processes in continuous time. For every generalized hyperbolic distribution it is possible
to construct a L´evy process so that the value of the increment of the process over
a ﬁxed time interval has that distribution; this is only possible because the generalized hyperbolic law is a so-called inﬁnitely divisible distribution, a property that it
inherits from the GIG mixing distribution of W.
The joint density in the non-singular case (Σ has rank d) is
f (x) =
 ∞
0
e(x−µ)′Σ−1γ
(2π)d/2|Σ|1/2wd/2
× exp

−(x −µ)′Σ−1(x −µ)
2w
−γ ′Σ−1γ
2/w

h(w) dw,
where h(w) is the density of W. Evaluation of this integral gives the generalized
hyperbolic density
f (x) = cKλ−(d/2)(

(χ + (x −µ)′Σ−1(x −µ))(ψ + γ ′Σ−1γ ))e(x−µ)′Σ−1γ
(

(χ + (x −µ)′Σ−1(x −µ))(ψ + γ ′Σ−1γ ))(d/2)−λ
,
(3.30)
where the normalizing constant is
c = (√χψ)−λψλ(ψ + γ ′Σ−1γ )(d/2)−λ
(2π)d/2|Σ|1/2Kλ(√χψ)
.
Clearly, if γ = 0, the distribution reduces to the symmetric generalized hyperbolic
special case of Example 3.8. In general we have a non-elliptical distribution with
asymmetric margins. The mean vector and covariance matrix of the distribution
are easily calculated from (3.28) and (3.29) using the information on the GIG and
its moments given in Section A.2.5. The characteristic function of the generalized
--- page 95 ---

3.2. Normal Mixture Distributions
79
hyperbolic distribution may be calculated using the same approach as in (3.21) to
yield
φX(t) = E(eit′X) = eit′µ ˆH( 1
2t′Σt −it′γ ),
(3.31)
where ˆH is the Laplace–Stieltjes transform of the GIG distribution.
We adopt the notation X ∼GHd(λ, χ, ψ, µ, Σ, γ ). Note that the distributions GHd(λ, χ/k, kψ, µ, kΣ, kγ ) and GHd(λ, χ, ψ, µ, Σ, γ ) are identical for
any k > 0, which causes an identiﬁability problem when we attempt to estimate the
parameters in practice. This can be solved by constraining the determinant |Σ| to
be a particular value (such as one) when ﬁtting. Note that, while such a constraint
will have an effect on the values of χ and ψ that we estimate, it will not have an
effect on the value of χψ, so this product is a useful summary parameter for the GH
distribution.
Linear combinations.
The generalized hyperbolic class is closed under linear operations.
Proposition 3.13. If X ∼GHd(λ, χ, ψ, µ, Σ, γ ) and Y = BX + b, where B ∈
Rk×d and b ∈Rk, then Y ∼GHk(λ, χ, ψ, Bµ + b, BΣB′, Bγ ).
Proof. We calculate, using (3.31) and a similar method to Proposition 3.9, that
φY (t) = eit′(Bµ+b) ˆH( 1
2t′BΣB′t −it′Bγ ).
Thus the parameters inherited from the GIG mixing distribution remain unchanged under linear operations. This means, for example, that margins of X are
easy to calculate; we have that Xi ∼GH1(λ, χ, ψ, µi, Σii, γi). It also means that
it would be relatively easy to base a version of the variance-covariance method on
a generalized hyperbolic model for risk factors.
Parametrizations.
There is a bewildering array of alternative parametrizations for
the generalized hyperbolic distribution in the literature and it is more common
to meet this distribution in a reparametrized form. In one common version the
dispersion matrix we call Σ is renamed  and the constraint is imposed that || = 1;
thisaddressestheidentiﬁabilityproblemmentionedabove.Theskewnessparameters
γ are replaced by parameters β and the non-negative parameters χ and ψ are
replaced by the non-negative parameters δ and α according to
β = −1γ ,
δ = √χ,
α =

ψ + γ ′−1γ .
These parameters must satisfy the constraints δ ⩾0, α2 > β′β if λ > 0; δ >
0, α2 > β′β if λ = 0; and δ > 0, α2 ⩾β′β if λ < 0. Blæsild (1981)
uses this parametrization to show that generalized hyperbolic distributions form a
closed class of distributions under linear operations and conditioning. However, the
parametrization does have the problem that the important parameters α and δ are
not generally invariant under either of these operations.
--- page 96 ---

80
3. Multivariate Models
It is useful to be able to move easily between our χ–ψ–Σ–γ parametrization,
as in (3.30), and the α–δ––β parametrization; λ and µ are common to both
parametrizations. If the χ–ψ–Σ–γ parametrization is used, then the formulas for
obtaining the other parametrization are
 = |Σ|−1/dΣ,
β = Σ−1γ ,
δ =

χ|Σ|1/d,
α =

|Σ|−1/d(ψ + γ ′Σ−1γ ).
If the α–δ––β form is used, then we can obtain our parametrization by setting
Σ = ,
γ = β,
χ = δ2,
ψ = (α2 −β′β).
Special cases.
The multivariate generalized hyperbolic family is extremely ﬂexible
and, as we have mentioned, contains many special cases known by alternative names.
• If λ = 1
2(d + 1) we drop the word “generalized” and refer to the distribution
as a d-dimensional hyperbolic distribution. Note that the univariate margins
of this distribution also have λ =
1
2(d + 1) and are not one-dimensional
hyperbolic distributions.
• If λ = 1 we get a multivariate distribution whose univariate margins are
one-dimensional hyperbolic distributions. The one-dimensional hyperbolic
distribution has been widely used in univariate analyses of ﬁnancial return
data (see Notes and Comments).
• If λ = −1
2 then the distribution is known as an NIG distribution. In the univariate case, this model has also been used in analyses of return data; its
functional form is similar to the hyperbolic with a slightly heavier tail. (Note
that the NIG and the GIG are different distributions!)
• If λ > 0 and χ = 0 we get a limiting case of the distribution known variously
as a generalized Laplace, Bessel function or variance-gamma distribution.
• If λ = −1
2ν, χ = ν and ψ = 0 we get another limiting case which seems
to have been less well studied, but which could be called an asymmetric or
skewed t distribution. Evaluating the limit of (3.30) as ψ →0 yields the
multivariate density
f (x) = c K(ν+d)/2(

(ν + Q(x))γ ′Σ−1γ ) exp((x −µ)′Σ−1γ )
(

(ν + Q(x))γ ′Σ−1γ )−(ν+d)/2(1 + (Q(x)/ν))(ν+d)/2 , (3.32)
where Q(x) = (x −µ)′Σ−1(x −µ) and the normalizing constant is
c =
21−(ν+d)/2
Γ ( 1
2ν)(πν)d/2|Σ|1/2 .
This density reduces to the standard multivariate t density in (3.23) as γ →0.
