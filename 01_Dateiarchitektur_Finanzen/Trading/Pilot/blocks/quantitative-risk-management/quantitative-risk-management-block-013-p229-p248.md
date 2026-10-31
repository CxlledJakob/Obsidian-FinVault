# Quantitative Risk Management_ Concepts, Techniques, and -- Alexander J_ McNeil, Rüdiger Frey, Paul Embrechts -- Princeton series in finance, -- isbn13 9780691122557 -- 478a0059673fecd0c76229cd3d8884e7 -- Anna’s Arc.pdf — pages 229–248

--- page 229 ---

5.3. Normal Mixture Copulas
213
−4
−4
−2
−2
0
0
2
2
4
4
−4
−2
0
2
4
−20
−20
−10
−10
0
0
10
10
20
20
−20
−10
0
10
20
−20
−10
0
10
20
−4
−2
0
2
4
X2
X2
X1
X1
(a)
(b)
(c)
(d)
Figure 5.9.
Five thousand simulated points from four distributions. (a) Standard bivariate
normal with correlation parameter ρ = 0.5. (b) Meta-Gaussian distribution with copula CGa
ρ
and Student t margins with four degrees of freedom. (c) Meta-t distribution with copula
Ct
4,ρ and standard normal margins. (d) Standard bivariate t distribution with four degrees of
freedom and correlation parameter ρ = 0.5. Horizontal and vertical lines mark the 0.005 and
0.995 quantiles. See Section 5.3.1 for a commentary.
thanforthemeta-Gaussiandistributions,andthiscanbeexplainedbythetaildependence of the t copula. The true theoretical ratio by which the number of these joint
exceedances in the meta-t models should exceed the number in the meta-Gaussian
models is 2.79, as may be read from Table 5.2, whose interpretation we now discuss.
In Table 5.2 we have calculated values of CGa
ρ (u, u)/Ct
ν,ρ(u, u) for various ρ
and ν and u = 0.05, 0.01, 0.005, 0.001. The rows marked Gauss contain values of
CGa
ρ (u, u), which is the probability that two rvs with this copula are below their
u-quantiles; we term this event a joint quantile exceedance (thinking of exceedance
in the downwards direction). Obviously it is identical to the probability that both rvs
arelargerthantheir(1 −u)-quantiles.Theremainingrowsgivethevaluesoftheratio
and thus express the amount by which the joint quantile exceedance probabilities
must be inﬂated when we move from models with a Gauss copula to models with a
t copula.
In Table 5.3 we extend Table 5.2 to higher dimensions. We now focus only on
joint exceedances of the 1% (or 99%) quantile(s). We tabulate values of the ratio
CGa
P (u, . . . , u)/Ct
ν,P(u, . . . , u), where P is an equicorrelation matrix with all correlations equal to ρ. It is noticeable that not only do these values grow as the corre-
--- page 230 ---

214
5. Copulas and Dependence
Table 5.2.
Joint quantile exceedance probabilities for bivariate Gauss and t copulas with
correlation parameter values of 0.5 and 0.7. For Gauss copulas the probability of joint quantile
exceedance is given; for the t copulas the factors by which the Gaussian probability must be
multiplied are given.
Quantile



ρ
Copula
ν
0.05
0.01
0.005
0.001
0.5
Gauss
1.21 × 10−2
1.29 × 10−3
4.96 × 10−4
5.42 × 10−5
0.5
t
8
1.20
1.65
1.94
3.01
0.5
t
4
1.39
2.22
2.79
4.86
0.5
t
3
1.50
2.55
3.26
5.83
0.7
Gauss
1.95 × 10−2
2.67 × 10−3
1.14 × 10−3
1.60 × 10−4
0.7
t
8
1.11
1.33
1.46
1.86
0.7
t
4
1.21
1.60
1.82
2.52
0.7
t
3
1.27
1.74
2.01
2.83
Table 5.3.
Joint 1% quantile exceedance probabilities for multivariate Gaussian and t
equicorrelation copulas with correlation parameter values of 0.5 and 0.7. For Gauss copulas the probability of joint quantile exceedance is given; for the t copulas the factors by
which the Gaussian probability must be multiplied are given.
Dimension d



ρ
Copula
ν
2
3
4
5
0.5
Gauss
1.29 × 10−3
3.66 × 10−4
1.49 × 10−4
7.48 × 10−5
0.5
t
8
1.65
2.36
3.09
3.82
0.5
t
4
2.22
3.82
5.66
7.68
0.5
t
3
2.55
4.72
7.35
10.34
0.7
Gauss
2.67 × 10−3
1.28 × 10−3
7.77 × 10−4
5.35 × 10−4
0.7
t
8
1.33
1.58
1.78
1.95
0.7
t
4
1.60
2.10
2.53
2.91
0.7
t
3
1.74
2.39
2.97
3.45
lation parameter or number of degrees of freedom falls, but they also grow with the
dimension of the copula. The next example gives an interpretation of one of these
numbers.
Example 5.34 (joint quantile exceedances: an interpretation). Consider daily
returns on ﬁve stocks. Suppose we are unsure about the best multivariate elliptical
model for these data returns, but we believe that the correlation between any two
returns on the same day is 50%. If returns follow a multivariate Gaussian distribution, then the probability that on any day all returns are below the 1% quantiles of
their respective distributions is 7.48 × 10−5. In the long run such an event will happen once every 13 369 trading days on average, that is roughly once every 51.4 years
(assuming 260 trading days in a year). On the other hand, if returns follow a multivariate t distribution with four degrees of freedom, then such an event will happen
--- page 231 ---

5.3. Normal Mixture Copulas
215
7.68 times more often, that is roughly once every 6.7 years. In the life of a risk
manager, 50-year events and 7-year events have a very different signiﬁcance.
5.3.2
Rank Correlations
To calculate rank correlations for normal variance mixture copulas we use the following preliminary result for elliptical distributions.
Proposition 5.35. Let X ∼E2(0, Σ, ψ) and ρ = ℘(Σ)12, where ℘denotes the
correlation operator in (3.5). Assume P(X = 0) = 0. Then
P(X1 > 0, X2 > 0) = 1
4 + arcsin ρ
2π
.
Proof. First we make a standardization of the variables and observe that if Y ∼
E2(0, P, ψ) and P = ℘(Σ), then P(X1 > 0, X2 > 0) = P(Y1 > 0, Y2 > 0).
Now introduce a pair of spherical variates Z ∼S2(ψ); it follows that
(Y1, Y2) d= (Z1, ρZ1 +

1 −ρ2Z2)
d= R(cos Θ, ρ cos Θ +

1 −ρ2 sin Θ),
where R is a positive radial rv and Θ is an independent, uniformly distributed angle
on [−π, π) (see Section 3.3.1 and Theorem 3.22). Let φ = arcsin ρ and observe that
sin φ = ρ and cos φ =

1 −ρ2. Since P(R = 0) = P(X = 0) = 0 we conclude
that
P(X1 > 0, X2 > 0) = P(cos Θ > 0, sin φ cos Θ + cos φ sin Θ > 0)
= P(cos Θ > 0, sin(Θ + φ) > 0).
The angle Θ must jointly satisfy Θ ∈(−1
2π, 1
2π) and Θ + φ ∈(0, π) and it is
easily seen that for any value of φ this has probability ( 1
2π + φ)/(2π), which gives
the result.
Theorem 5.36 (rank correlations for Gauss copula). Let X have a bivariate meta-
Gaussian distribution with copula CGa
ρ
and continuous margins. Then the rank correlations are
ρτ(X1, X2) = 2
π arcsin ρ,
(5.32)
ρS(X1, X2) = 6
π arcsin 1
2ρ.
(5.33)
Proof. Since rank correlation is a copula property we can of course simply assume
that X ∼N2(0, P), where P is a correlation matrix with off-diagonal element ρ;
the calculations are then easy. For Kendall’s tau, formula (5.26) implies
ρτ(X1, X2) = 4P(Y1 > 0, Y2 > 0) −1,
where Y = ˜X −X and ˜X is an independent copy of X. Since Y ∼N2(0, 2P),
by the convolution property of multivariate normal in Section 3.1.3, we have that
--- page 232 ---

216
5. Copulas and Dependence
ρ
Rank correlation
−1.0
−0.5
0
0.5
1.0
−1.0
−0.5
0
0.5
1.0
Figure 5.10.
The solid line shows the relationship between Spearman’s rho and the correlation parameter ρ of the Gauss copula CGa
ρ
for meta-Gaussian rvs with continuous dfs; this
is very close to the line y = x, which is just visible as a dotted line. The dashed line shows
the relationship between Kendall’s tau and ρ; this relationship holds for the copulas of other
normal variance mixture distributions with correlation parameter ρ, such as the t copula Ctν,ρ.
ρ(Y1, Y2) = ρ and formula (5.32) follows from Proposition 5.35. For Spearman’s
rho we observe that (5.25) implies
ρS(X1, X2) = 12
 1
0
 1
0
P(Φ(X1) ⩽u1, Φ(X2) ⩽u2) du1 du2 −3
= 3

4
 1
0
 1
0
P(X1 ⩽Φ−1(u1), X2 ⩽Φ−1(u2)) du1 du2 −1

= 3

4
 ∞
−∞
 ∞
−∞
P(X1 ⩽x1, X2 ⩽x1)φ(x1)φ(x2) dx1 dx2 −1

,
where xi := Φ−1(ui) and φ is the standard normal density. Now let Z1 and Z2
denote two standard normal variates, independent of X and of each other. We see
that
ρS(X1, X2) = 3(4E(P(X1 < Z1, X2 < Z2 | Z1, Z2)) −1)
= 3(4P(X1 < Z1, X2 < Z2) −1)
= 3(4P(Y1 > 0, Y2 > 0) −1),
where Y = Z −X. Since Y ∼N2(0, (P + I2)), the formula (5.33) follows from
Proposition 5.35.
These relationships between the rank correlations and ρ are illustrated in Figure 5.10. Note that the right-hand side of (5.33) may be approximated by the value
ρ itself. This approximation turns out to be very accurate, as shown in the ﬁgure;
the error bounds are |6 arcsin(ρ/2)/π −ρ| ⩽(π −3)|ρ|/π ⩽0.0181.
--- page 233 ---

5.3. Normal Mixture Copulas
217
The relationship between Kendall’s tau and the correlation parameter of the Gauss
copula CGa
ρ
expressed by (5.32) holds more generally for the copulas of essentially
all normal variance mixture distributions, such as the t copula Ct
ν,ρ. This is implied
by the following general result for elliptical distributions, which was used to derive
an alternative correlation estimator for bivariate distributions in Section 3.3.4.
Proposition 5.37. LetX ∼E2(0, P, ψ)foracorrelationmatrixP withoff-diagonal
element ρ, and assume that P(X = 0) = 0. Then the relationship ρτ(X1, X2) =
(2/π) arcsin ρ holds.
Proof. The result relies on the convolution property of elliptical distributions
in (3.54). Setting Y = ˜X −X, where ˜X is an independent copy of X, we note
that Y ∼E2(0, P, ˜ψ) for some characteristic generator ˜ψ. We need to evaluate
ρτ(X1, X2) = 4P(Y1 > 0, Y2 > 0) −1 as in the proof of Theorem 5.36, but
Proposition 5.35 shows that P(Y1 > 0, Y2 > 0) takes the same value whenever Y
is elliptical.
Remark 5.38. The relationship (5.33) between Spearman’s rho and linear correlation does not hold for all elliptical distributions. A counterexample is found in
Hult and Lindskog (2002). Simple formulas for elliptical distributions other than
the Gaussian, such as the multivariate t, are not known to us.
5.3.3
Skewed Normal Mixture Copulas
A skewed normal mixture copula is the copula of any normal mixture distribution
that is not elliptically symmetric. An example is provided by the skewed t copula,
which is the copula of the distribution whose density is given in (3.32).
A random vector X with a skewed t distribution and ν degrees of freedom is
denoted X ∼GHd(−1
2ν, ν, 0, µ, Σ, γ ) in the notation of Section 3.2.3. Its marginal
distributions satisfy Xi ∼GH1(−1
2ν, ν, 0, µi, Σii, γi) (from Proposition 3.13) and
its copula depends on ν, P = ℘(Σ) and γ and will be denoted by Ct
ν,P,γ or, in the
bivariate case, Ct
ν,ρ,γ1,γ2. Random sampling from the skewed t copula follows the
same approach as for the t copula in Algorithm 5.10.
Algorithm 5.39 (simulation of skewed t copula).
(1) Generate X ∼GHd(−1
2ν, ν, 0, 0, P, γ ) using Algorithm 3.10.
(2) Return U = (F1(X1), . . . , Fd(Xd))′, where Fi is the distribution function of
a GH1(−1
2ν, ν, 0, 0, 1, γi) distribution. The random vector U has df Ct
ν,P,γ .
Note that the evaluation of Fi requires the numerical integration of the density of a
skewed univariate t density.
To appreciate the ﬂexibility of the skewed t copula it sufﬁces to consider the
bivariate case for different values of the skewness parameters γ1 and γ2. In Figure 5.11 we have plotted simulated points from nine different examples of this
copula. Part (e) corresponds to the case when γ1 = γ2 = 0 and is thus the ordinary
t copula. All other pictures show copulas which are non-radially symmetric (see
--- page 234 ---

218
5. Copulas and Dependence
1.0
0.2 0.4 0.6 0.8
0
1.0
0.2 0.4 0.6 0.8
0
1.0
0.2 0.4 0.6 0.8
0
1.0
0.2
0.4
0.6
0.8
0
1.0
0.2
0.4
0.6
0.8
0
1.0
0.2
0.4
0.6
0.8
0
U2
U2
U2
U1
U1
U1
(a)
(b)
(c)
(d)
(e)
(f)
(g)
(h)
(i)
Figure 5.11.
Ten thousand simulated points from bivariate skewed t copula Ctν,ρ,γ1,γ2
for ν = 5, ρ = 0.8 and various values of the parameters (γ1, γ2): (a) γ = (0.8, −0.8);
(b) γ = (0.8, 0); (c) γ = (0.8, 0.8); (d) γ = (0, −0.8); (e) γ = (0, 0); (f) γ = (0, 0.8);
(g) γ = (−0.8, −0.8); (h) γ = (−0.8, 0); and (i) γ = (−0.8, 0.8).
Section 5.1.5), as is obvious by rotating each picture 180◦about the point ( 1
2, 1
2);
(c), (e) and (g) show exchangeable copulas satisfying (5.18), while the remaining
six are non-exchangeable.
Obviously the main advantage of the skewed t copula over the ordinary t copula is
that its asymmetry allows us to have different levels of tail dependence in “opposite
corners” of the distribution. In the context of market risk it is often claimed that joint
negative returns on stocks show more tail dependence than joint positive returns.
5.3.4
Grouped Normal Mixture Copulas
Technically speaking, a grouped normal mixture copula is not itself the copula of a
normal mixture distribution, but rather a way of attaching together a set of normal
mixture copulas. We will illustrate the idea by considering the grouped t copula.
Here, the basic idea is to construct a copula for a random vector X such that certain
subvectors of X have t copulas but quite different levels of tail dependence.
--- page 235 ---

5.3. Normal Mixture Copulas
219
We create a distribution using a generalization of the variance-mixing construction X =
√
WZ in (3.19). Rather than multiplying all components of a correlated
Gaussian vector Z with the root of a single inverse-gamma-distributed variate W,
as in Example 3.7, we instead multiply different subgroups with different variates
Wj, where Wj ∼Ig( 1
2νj, 1
2νj) and the Wj are themselves comonotonic (see Section 5.1.6). Thus we create subgroups whose dependence properties are described
by t copulas with different νj parameters.
Like the t copula, the skewed t copula and anything based on a mixture of multivariate normals, a grouped t copula is easy to simulate and thus to use in Monte
Carlo risk studies—this has been a major motivation for its development. We formally deﬁne the grouped t copula by explaining in more detail how to generate a
random vector U with that distribution.
Algorithm 5.40 (simulation of grouped t copula).
(1) Generate independently Z ∼Nd(0, P) and U ∼U(0, 1).
(2) Partition {1, . . . , d} into m subsets of sizes s1, . . . , sm, and for k = 1, . . . , m
let νk be the degrees-of-freedom parameter associated with group k.
(3) Set Wk = G−1
νk (U), where Gν is the df of the univariate Ig( 1
2ν, 1
2ν) distribution, so that W1, . . . , Wm are comonotonic and inverse-gamma-distributed
variates.
(4) Construct vectors X and U by
X = (

W1Z1, . . . ,

W1Zs1,

W2Zs1+1, . . . ,

W2Zs1+s2, . . . ,

WmZd)′,
U = (tν1(X1), . . . , tν1(Xs1), tν2(Xs1+1), . . . , tν2(Xs1+s2), . . . , tνm(Xd))′.
The former has a grouped t distribution and the latter is distributed according
to a grouped t copula.
If we have an a priori idea of the desired group structure, we can calibrate the
grouped t copula to data using a method based on Kendall’s tau rank correlations.
The use of this method for the ordinary t copula is described later in Section 5.5.1
and Example 5.54.
Notes and Comments
The coefﬁcient of tail dependence for the t copula was ﬁrst derived in Embrechts,
McNeil and Straumann (2002). A more general result for the copulas of elliptical
distributions is given in Hult and Lindskog (2002) and will be discussed in Section 7.3.3. The formula for Kendall’s tau for elliptical distributions can be found in
Lindskog, McNeil and Schmock (2003) and Fang and Fang (2002).
The skewed t copula was introduced in Demarta and McNeil (2005), which also
describes the grouped t copula. The grouped t copula and a method for its calibration
was ﬁrst proposed in Daul et al. (2003).
--- page 236 ---

220
5. Copulas and Dependence
Table 5.4.
Table summarizing the generators, permissible parameter values and limiting
special cases for four selectedArchimedean copulas. The case θ = 0 should be taken to mean
the limit limθ→0 φθ(t). For the Clayton and Frank copulas this limit is −ln t, which is the
generator of the independence copula.
Copula
Generator φ(t)
Parameter range
Strict
Lower
Upper
CGu
θ
(−ln t)θ
θ ⩾1
Yes
Π
M
CCl
θ
1
θ (t−θ −1)
θ ⩾−1
θ ⩾0
W
M
CFr
θ
−ln
e−θt −1
e−θ −1

θ ∈R
Yes
W
M
CGC
θ,δ
θ−δ(t−θ −1)δ
θ ⩾0, δ ⩾1
Yes
N/A
N/A
5.4
Archimedean Copulas
The Gumbel copula (5.11) and the Clayton copula (5.12) belong to the family of socalled Archimedean copulas, which has been very extensively studied. This family
has proved useful for modelling portfolio credit risk, as will be seen in Example 8.9.
In this section we look at the simple structure of these copulas and establish some
of the properties that we will need.
5.4.1
Bivariate Archimedean Copulas
As well as the Gumbel and Clayton copulas, two further examples we consider are
the Frank copula
CFr
θ (u1, u2) = −1
θ ln

1 + (exp(−θu1) −1)(exp(−θu2) −1)
exp(−θ) −1

,
θ ∈R,
and a two-parameter copula that we refer to as a generalized Clayton copula:
CGC
θ,δ (u1, u2) = {((u−θ
1
−1)δ + (u−θ
2
−1)δ)1/δ + 1}−1/θ,
θ ⩾0, δ ⩾1.
It may be veriﬁed that, provided the parameter θ lies in the ranges we have speciﬁed
in the copula deﬁnitions, all four examples that we have met have the form
C(u1, u2) = φ−1(φ(u1) + φ(u2)),
(5.34)
where φ is a decreasing function from [0, 1] to [0, ∞], satisfying φ(0) = ∞,
φ(1) = 0, known as the generator of the copula, and φ−1 is its inverse. For example,
for the Gumbel copula φ(t) = (−ln t)θ for θ ⩾1, and for the other copulas the
generators φ(t) are given in Table 5.4.
When we introduced the Clayton copula in (5.12) we insisted that its parameter should be positive. Note that it is in fact possible to have a Clayton copula
with −1 ⩽θ < 0, although in this case the construction (5.34) must be generalized slightly. Suppose, for example, that θ = −1
2; the Clayton copula generator
φ(t) = θ−1(t−θ −1) is then a strictly decreasing function mapping [0, 1] into [0, 2].
If we attempt to evaluate (5.34) in, say, the point u1 = u2 = 0.16, we have a problem
since φ(u1) + φ(u2) = 2.4 and φ−1(2.4) is undeﬁned.
--- page 237 ---

5.4. Archimedean Copulas
221
To obtain a copula in a case when φ(0) < ∞we introduce a so-called pseudoinverse of the generator and give a theorem that explains exactly when a construction
resembling (5.34) yields a copula.
Deﬁnition 5.41 (pseudo-inverse). Suppose φ : [0, 1] →[0, ∞] is continuous and
strictly decreasing with φ(1) = 0 and φ(0) ⩽∞. We deﬁne a pseudo-inverse of φ
with domain [0, ∞] by
φ[−1](t) =

φ−1(t),
0 ⩽t ⩽φ(0),
0,
φ(0) < t ⩽∞.
(5.35)
Theorem 5.42 (bivariate Archimedean copula). Let φ : [0, 1] →[0, ∞] be
continuous and strictly decreasing with φ(1) = 0 and φ[−1](t) as in (5.35). Then
C(u1, u2) = φ[−1](φ(u1) + φ(u2))
(5.36)
is a copula if and only if φ is convex.
Proof. See Nelsen (1999, pp. 91, 92).
All copulas constructed according to (5.36) are called bivariate Archimedean
copulas. If φ(0) = ∞the generator is said to be strict and we may replace the
pseudo-inverse φ[−1] by the ordinary functional inverse φ−1 as in (5.34). In summary
we have the following.
Deﬁnition 5.43 (Archimedean copula generator). A continuous, strictly decreasing, convex function φ : [0, 1] →[0, ∞] satisfying φ(1) = 0 is known as an
Archimedean copula generator. It is known as a strict generator if φ(0) = ∞.
In Table 5.4 we indicate when the generators of the four Archimedean copulas
are strict and give the lower and upper limits of the families as the parameter θ goes
to the boundaries of the parameter space. Both the Frank and Clayton copulas are
known as comprehensive copulas, since they interpolate between a lower limit of
countermonotonicity and an upper limit of comonotonicity. For a more extensive
table of Archimedean copulas see Nelsen (1999).
Remark 5.44. Consider again the Clayton copula with θ = −1
2 and non-strict
generator φ(t) = −2(√t −1). The copula may be written as C(u1, u2)
=
max{(u0.5
1
+ u0.5
2
−1)2, 0} and this “maximum-with-zero” notation is the common
way of writing Archimedean copulas with non-strict generators. The countermonotonicity copula is a further example; it is an Archimedean copula with non-strict
generator φ(t) = 1 −t.
Kendall’s rank correlations can be calculated for Archimedean copulas directly
from the generator using Proposition 5.45 below. The formula obtained can be used
to calibrate Archimedean copulas to empirical data using the sample version of
Kendall’s tau, as we discuss in Section 5.5.
--- page 238 ---

222
5. Copulas and Dependence
Table 5.5.
Kendall’s rank correlations and coefﬁcients of tail dependence for the copulas
of Table 5.4. D1(θ) is the Debye function D1(θ) = θ−1  θ
0 t/(exp(t) −1) dt.
Copula
ρτ
λu
λl
CGu
θ
1 −1/θ
2 −21/θ
0
CCl
θ
θ/(θ + 2)
0

2−1/θ,
θ > 0,
0,
θ ⩽0,
CFr
θ
1 −4θ−1(1 −D1(θ))
0
0
CGC
θ,δ
(2 + θ)δ −2
(2 + θ)δ
2 −21/δ
2−1/(θδ)
Proposition 5.45. Let X1 and X2 be continuous rvs with unique Archimedean
copula C generated by φ. Then
ρτ(X1, X2) = 1 + 4
 1
0
φ(t)
φ′(t) dt.
(5.37)
Proof. See Nelsen (1999, p. 130).
For the closed-form copulas of theArchimedean class, coefﬁcients of tail dependence are easily calculated using methods of the kind used in Example 5.31. Values
for Kendall’s tau and the coefﬁcients of tail dependence for the copulas of Table 5.4
are given in Table 5.5. It is interesting to note that the generalized Clayton copula
CGC
θ,δ subsumes, in a sense, both Gumbel’s family and the strict part of Clayton’s
family, and thus succeeds in having tail dependence in both tails.
5.4.2
Multivariate Archimedean Copulas
It seems natural to attempt to construct a higher-dimensional Archimedean copula according to C(u1, . . . , ud) = φ[−1](φ(u1) + · · · + φ(ud)). However, this construction may fail to deﬁne a proper distribution function for arbitrary dimension d.
An example where this occurs is obtained if we take the generator φ(t) = 1 −t,
which is not strict. In this case we obtain the Fr´echet lower bound for copulas, which
is not itself a copula for d > 2.
A necessary condition for the d-dimensional construction to succeed in all dimensions is that φ should be a strict Archimedean copula generator, although this is not
sufﬁcient. It was shown by Kimberling (1974) that if φ : [0, 1] →[0, ∞] is a strict
Archimedean copula generator, then
C(u1, . . . , ud) = φ−1(φ(u1) + · · · + φ(ud))
(5.38)
givesacopulainanydimensiond ifandonlyifthegeneratorinverseφ−1 : [0, ∞] →
[0, 1] is completely monotonic.A decreasing function f (t) is completely monotonic
on an interval [a, b] if it satisﬁes
(−1)k dk
dtk f (t) ⩾0,
k ∈N, t ∈(a, b).
(5.39)
--- page 239 ---

5.4. Archimedean Copulas
223
All of the generators in Table 5.4 have inverses which are completely monotonic
on [0, ∞] (if we restrict to θ ⩾0 for the Clayton copula) and all extend to arbitrary
dimensions using the construction (5.38). For example, a d-dimensional Clayton
copula is
CCl
θ,δ(u) = (u−θ
1
+ · · · + u−θ
d
−d + 1)−1/θ,
θ ⩾0,
(5.40)
where the limiting case θ = 0 should be interpreted as the d-dimensional independence copula.
Another way of describing these Archimedean copulas which extend to arbitrary
dimensions is in terms of Laplace–Stieltjes transforms of dfs on R+, since every
completely monotonic function mapping from [0, ∞] to [0, 1] can be expressed in
terms of such transforms. Let G be a df on R+ satisfying G(0) = 0 with Laplace–
Stieltjes transform
ˆG(t) =
 ∞
0
e−tx dG(x),
t ⩾0.
(5.41)
If we deﬁne ˆG(∞) := 0, it is not difﬁcult to verify that ˆG : [0, ∞] →[0, 1] is a
continuous, strictly decreasing, function with the property of complete monotonicity (5.39). It therefore provides a candidate for an Archimedean generator inverse.
In the following result we show how Laplace–Stieltjes transforms are used to
construct random vectors whose distributions are multivariateArchimedean copulas.
In so doing, we also reveal how such copulas may be simulated.
Proposition 5.46. Let G be a df on R+ satisfying G(0) = 0 with Laplace–Stieltjes
transform ˆG as in (5.41) and set ˆG(∞) := 0. Let V be an rv with df G and let
U1, . . . , Ud be a sequence of rvs that are conditionally independent given V with
conditional distribution function given by FUi|V (u | v) = exp(−v ˆG−1(u)) for u ∈
[0, 1]. Then
P(U1 ⩽u1, . . . , Ud ⩽ud) = ˆG( ˆG−1(u1) + · · · + ˆG−1(ud)),
(5.42)
so that the df of U = (U1, . . . , Ud)′ is an Archimedean copula with generator
φ = ˆG−1.
Proof. We have
P(U1 ⩽u1, . . . , Ud ⩽ud) =
 ∞
0
P(U1 ⩽u1, . . . , Ud ⩽ud | V = v) dG(v)
=
 ∞
0
d!
i=1
FUi|V (ui | v) dG(v)
=
 ∞
0
exp(−x( ˆG−1(u1) + · · · + ˆG−1(ud))) dG(v)
= ˆG( ˆG−1(u1) + · · · + ˆG−1(ud)).
Because of the importance of such copulas, particularly in the ﬁeld of credit risk,
we will call these copulas LT-Archimedean (LT stands for “Laplace transform”) and
make the following deﬁnition.
--- page 240 ---

224
5. Copulas and Dependence
Deﬁnition 5.47 (LT-Archimedean copula). An LT-Archimedean copula is a copula
of the form (5.38), where φ is the inverse of the Laplace–Stieltjes transform of a df
G on R+ satisfying G(0) = 0.
In the following algorithm we explain how to sample from such copulas using
Proposition 5.46 and give explicit instructions for the Clayton, Gumbel and Frank
copulas.
Algorithm 5.48 (simulation of LT-Archimedean copulas).
(1) Generate a variate V with df G such that ˆG, the Laplace–Stieltjes transform
of G, is the inverse of the generator φ of the required copula.
(2) Generate independent uniform variates X1, . . . , Xd.
(3) Return U = ( ˆG(−ln(X1)/V ), . . . , ˆG(−ln(Xd)/V ))′.
(a) For the special case of the Clayton copula we generate a gamma variate V ∼
Ga(1/θ, 1) with θ > 0 (see SectionA.2.4). The df of V has Laplace transform
ˆG(t) = (1 + t)−1/θ. Note that the inverse ˆG−1(t) = t−θ −1 differs from the
generator in Table 5.4 by a constant factor that is unimportant.
(b) For the special case of the Gumbel copula we generate a positive stable variate V ∼St(1/θ, 1, γ, 0), where γ = (cos(π/(2θ)))θ and θ > 1 (see Section A.2.9 for more details and a reference to a simulation algorithm). This df
has Laplace transform ˆG(t) = exp(−t1/θ) as desired.
(c) For the special case of the Frank copula we generate a discrete rv V with
probability mass function p(k) = P(V = k) = (1 −exp(−θ))k/(kθ) for
k = 1, 2, . . . and θ > 0.This can be achieved by standard simulation methods
for discrete distributions (see Ripley 1987, p. 71).
See Figure 5.12 for an example of data simulated from a four-dimensional Gumbel
copula using this algorithm. Note the upper tail dependence in each bivariate margin
of this copula.
5.4.3
Non-exchangeable Archimedean Copulas
A copula obtained from construction (5.38) is obviously an exchangeable copula
conformingto(5.18).WhileexchangeablebivariateArchimedeancopulasarewidely
used in modelling applications, their exchangeable multivariate extensions represent
a very specialized form of dependence structure and have more limited applications.
An exception to this is in the area of credit risk, as will be seen in Chapter 8, although
even here more general models with group structures are also needed. It is certainly
natural to enquire whether there are extensions to the Archimedean class that are
not rigidly exchangeable, and we devote this section to a short discussion of some
possible extensions.
--- page 241 ---

5.4. Archimedean Copulas
225
Component 4
Component 3
Component 2
Component 1
0.4
0.8
0
0.4
0.8
0
0.4
0.4
0.8
0.8
0
0
0.4
0.8
0
0.2
0.6
1.0
0.4
0.8
0
0.2
0.6
1.0
0.4
0.8
0
0.2
0.6
1.0
0.4
0.8
0
0.2
0.6
1.0
Figure 5.12.
Pairwise scatterplots of 1000 simulated points from a four-dimensional
exchangeable Gumbel copula with θ = 2. Data are simulated using Algorithm 5.48.
Asymmetric bivariate copulas.
Let Cθ be any exchangeable bivariate copula. Then
a parametric family of asymmetric copulas Cθ,α,β is obtained by setting
Cθ,α,β(u1, u2) = u1−α
1
u1−β
2
Cθ(uα
1, uβ
2 ),
0 ⩽u1, u2 ⩽1,
(5.43)
where 0 ⩽α, β ⩽1. Only in the special case α = β is the copula (5.43) exchangeable. Note also that when both parameters are zero, Cθ,0,0 is the independence
copula, and when both parameters are one, Cθ,1,1 is simply Cθ. When Cθ is an
Archimedean copula, we refer to copulas constructed by (5.43) as asymmetric bivariate Archimedean copulas.
We check that (5.43) deﬁnes a copula by constructing a random vector with this
df and observing that its margins are standard uniform. Since the construction of a
random vector amounts to a simulation recipe, we present it as such.
Algorithm 5.49 (asymmetric bivariate Archimedean copula).
(1) Generate a random pair (V1, V2) with df Cθ.
(2) Generate, independently of V1, V2, two independent standard uniform variates
˜U1 and ˜U2.
(3) Return U1 = max{V 1/α
1
, ˜U1/(1−α)
1
} and U2 = max{V 1/β
2
, ˜U1/(1−β)
2
}.
--- page 242 ---

226
5. Copulas and Dependence
0.2
0.2
0.4
0.4
0.6
0.6
0.8
0.8
1.0
1.0
0
0
U2
U1
Figure 5.13.
Pairwise scatterplots of 10 000 simulated points from an extension of the
Gumbel copula CGu
4
given by C4,0.95,0.7 in (5.43). This is simulated using Algorithm 5.49.
It may be easily veriﬁed that (U1, U2) have the df (5.43). See Figure 5.13 for an
example of simulated data from an asymmetric copula based on Gumbel’s copula.
Note that an alternative copula may be constructed by taking (V1, V2) in Algorithm 5.49 to be distributed according to some copula other than the independence
copula.
Non-exchangeable, higher-dimensional Archimedean copulas.
Non-exchangeable, higher-dimensional Archimedean copulas with exchangeable bivariate margins can be constructed by recursive application of Archimedean generators and
their inverses, and we will give examples in this section. The biggest problem with
these constructions lies in checking that they lead to valid multivariate distributions
satisfying (5.1). The necessary theory is complicated and we will simply indicate the
nature of the conditions that are necessary without providing justiﬁcation; a comprehensive reference is Joe (1997). It turns out that with some care we can construct
situations of partial exchangeability. We give threeand four-dimensional examples
which indicate the pattern of construction.
Example 5.50 (three-dimensional non-exchangeable Archimedean copulas).
Suppose that φ1 and φ2 are two strict Archimedean generators and consider
C(u1, u2, u3) = φ−1
2 (φ2 ◦φ−1
1 (φ1(u1) + φ1(u2)) + φ2(u3)).
(5.44)
Conditions that ensure that this is a copula are that the generator inverses φ−1
1
and
φ−1
2
are completely monotonic decreasing functions, as in (5.39), and the composition φ2 ◦φ−1
1
: [0, ∞] →[0, ∞] is a completely monotonic increasing function,
i.e. a function g satisfying
(−1)k−1 dk
dtk g(t) ⩾0,
k ∈N.
Observe that when φ2 = φ1 = φ we are back in the situation of full exchangeability,
as in (5.38). Otherwise, if φ1̸ = φ2 and (U1, U2, U3) is a random vector with df given
--- page 243 ---

5.4. Archimedean Copulas
227
by (5.44), then only U1 and U2 are exchangeable, i.e. (U1, U2, U3) d= (U2, U1, U3),
but no other swapping of subscripts is possible. All bivariate margins of (5.44) are
themselves Archimedean copulas. The margins C13 and C23 have generator φ2 and
C12 has generator φ1.
Example 5.51 (four-dimensional non-exchangeable Archimedean copulas). A
possible four-dimensional construction is
C(u1, u2, u3, u4) = φ−1
3 (φ3◦φ−1
1 (φ1(u1)+φ1(u2))+φ3◦φ−1
2 (φ2(u3)+φ2(u4))),
(5.45)
where φ1, φ2 and φ3 are three distinct, strictArchimedean generators and we assume
that their inverses and the composite functions φ3 ◦φ−1
1
and φ3 ◦φ−1
2
are completely
monotonic to obtain a proper distribution function. This is not the only possible fourdimensional construction (Joe 1997), but it is a useful construction because it gives
two exchangeable groups. If (U1, U2, U3, U4) has the df (5.45), then U1 and U2 are
exchangeable, as are U3 and U4.
The same kinds of construction can be extended to higher dimensions, subject
again to complete monotonicity conditions on the compositions of generators and
generator inverses.
LT-Archimedean copulas with p-factor structure.
Recall from Deﬁnition 5.47 the
family of LT-Archimedean copulas. It follows easily from (5.42) that these have the
form
C(u1, . . . , ud) = E

exp

−V
d

i=1
ˆG−1(ui)

(5.46)
for strictly positive rvs V with Laplace–Stieltjes transform ˆG. It is possible to generalize the construction (5.46) to obtain a larger family of non-exchangeable copulas,
whichwillbeusefulinthecontextofdynamiccreditriskmodels(seeSection9.7).An
LT-Archimedean copula with p-factor structure is constructed from a p-dimensional
random vector V = (V1, . . . , Vp)′ with independent, strictly positive components
and a matrix A ∈Rd×p with elements aij > 0 as follows:
C(u1, . . . , ud) = E

exp

−
d

i=1
a′
iV ˆG−1
i (ui)

,
(5.47)
where ai is the ith row of A and ˆG−1
i
is the Laplace–Stieltjes transform of the strictly
positive rv a′
iV .
We can write (5.47) in a different way, which facilitates the computation of
C(u1, . . . , ud). Note that
d

i=1
a′
iV ˆG−1
i (ui) =
p

j=1
Vj
d

i=1
aij ˆG−1
i (ui).
--- page 244 ---

228
5. Copulas and Dependence
It follows from the independence of the Vj that
C(u1, . . . , ud) =
p
!
j=1
E

exp

−Vj
d

i=1
aij ˆG−1
i (ui)

=
p
!
j=1
ˆGVj

d

i=1
aij ˆG−1
i (ui)

.
(5.48)
Note that (5.48) is easy to evaluate when ˆGVj , the Laplace–Stieltjes transform of
the Vj, is available in closed form, because ˆGi(t) = p
j=1 ˆGVj (aijt) by the independence of the Vj.
Notes and Comments
The name Archimedean relates to an algebraic property of the copulas which resembles the Archimedean axiom for real numbers (see Nelsen 1999, p. 98). Clayton’s
copula was introduced in Clayton (1978), although it has also been called the Cook
and Johnson copula (see Genest and MacKay 1986) and the Pareto copula (see
Hutchinson and Lai 1990). For Frank’s copula see Frank (1979); this copula has
radial symmetry and is the only such Archimedean copula.
Theorem 5.42 is a result of Alsina, Frank and Schweizer (2005). The formula for Kendall’s tau in the Archimedean family is due to Genest and MacKay
(1986). The link between completely monotonic functions and generators which
give Archimedean copulas of the form (5.38) is found in Kimberling (1974). See
also Feller (1971) for more on the concept of complete monotonicity. For more
on the important connection between Archimedean generators and Laplace transforms, see Joe (1997). For a single reference containing most of the main theory
for bivariate Archimedean copulas and some of the results on higher-dimensional
exchangeable Archimedean copulas consult Nelsen (1999).
Proposition 5.46 and Algorithm 5.48 are due to Marshall and Olkin (1988). See
Frees and Valdez (1997), Sch¨onbucher (2002), Frey and McNeil (2003) and Chapters 8 and 9 of this book for further discussion of this technique.
For more details on the asymmetric bivariate copulas obtained from construction (5.43) and ideas for more general asymmetric copulas see Genest, Ghoudi and
Rivest (1998). These copula classes were introduced in the PhD thesis of Khoudraji
(1995). For additional theory concerning partially exchangeable higher-dimensional
Archimedean copulas with exchangeable bivariate margins, see Joe (1997). LT-
Archimedean copulas with p-factor structure have been proposed by Rogge and
Sch¨onbucher (2003) with applications in credit risk in mind.
Other copula families we have not considered include the Marshall–Olkin copulas
(Marshall and Olkin 1967a,b) and the extremal copulas in Tiit (1996).
5.5
Fitting Copulas to Data
We assume that we have data vectors X1, . . . , Xn with identical distribution
function F, describing ﬁnancial losses or ﬁnancial risk factor returns; we write
--- page 245 ---

5.5. Fitting Copulas to Data
229
Xt = (Xt,1, . . . , Xt,d)′ for an individual data vector and X = (X1, . . . , Xd)′ for
a generic random vector with df F. We assume further that this df F has continuous margins F1, . . . , Fd and thus, by Sklar’s Theorem, a unique representation
F(x) = C(F1(x1), . . . , Fd(xd)).
It is often very difﬁcult, particularly in higher dimensions and in situations where
we are dealing with skewed loss distributions or heterogeneous risk factors, to ﬁnd
a good multivariate model that describes both marginal behaviour and dependence
structure effectively. For multivariate risk-factor return data of a similar kind, such as
stock returns or exchange-rate returns, we have discussed useful overall models such
as the generalized hyperbolic family of Section 3.2.3, but even in these situations
there can be value in separating the marginal-modelling and dependence-modelling
issuesandlookingateachinmoredetail.Thecopulaapproachtomultivariatemodels
facilitates this approach and allows us to consider, for example, the issue of whether
tail dependence appears to be present in our data.
This section is thus devoted to the problem of estimating the parameters θ of
a parametric copula Cθ. The main method we consider is maximum likelihood
in Section 5.5.3. First we outline a simpler method-of-moments procedure using
sample rank correlation estimates. This method has the advantage that marginal
distributions do not need to be estimated, and consequently inference about the
copula is in a sense “margin-free”.
5.5.1
Method-of-Moments using Rank Correlation
Depending on which particular copula we want to ﬁt, it may be easier to use empirical
estimates of either Spearman’s or Kendall’s rank correlation to infer an estimate for
the copula parameter. We begin by discussing the standard estimators of both of
these rank correlations.
Deﬁnition 5.28 suggests that we could estimate ρS(Xi, Xj) by calculating the
usual correlation coefﬁcient for the pseudo-observations: {(Fi,n(Xt,i), Fj,n(Xt,j)) :
t = 1, . . . , n}, where Fi,n denotes the standard empirical df for the ith margin.
Equivalently, if we use rank(Xt,i) to denote the rank of Xt,i in X1,i, . . . , Xn,i (i.e. its
position in the ordered sample), we can calculate the correlation coefﬁcient for the
rank data {(rank(Xt,i), rank(Xt,j))}, and this gives us the Spearman’s rank correlation coefﬁcient:
12
n(n2 −1)
n

t=1
(rank(Xt,i) −1
2(n + 1))(rank(Xt,j) −1
2(n + 1)).
(5.49)
We will denote by RS the matrix of pairwise Spearman’s rank correlation coefﬁ-
cients; since this is the sample correlation matrix of the vectors of ranks it is clearly
a positive semideﬁnite matrix.
The standard estimator of Kendall’s tau ρτ(Xi, Xj) is Kendall’s rank correlation
coefﬁcient:
n
2
−1

1⩽t<s⩽n
sign((Xt,i −Xs,i)(Xt,j −Xs,j)).
(5.50)
--- page 246 ---

230
5. Copulas and Dependence
This is clearly the empirical analogue of the theoretical Kendall’s tau in Deﬁnition 5.27. Note that the actual evaluation of this estimator for large n is timeconsuming (in comparison with Spearman’s rank) because every pair of observations must be considered. Again we can collect pairwise Kendall’s rank correlation
coefﬁcients in a matrix Rτ; by observing that this matrix may be written as
Rτ =
n
2
−1

1⩽t<s⩽n
sign(Xt −Xs) sign(Xt −Xs)′,
it is again apparent that this gives a positive semideﬁnite matrix.
In a series of examples we show how these sample rank correlations can be used
to calibrate (or partially calibrate) various copulas. Obviously we assume that there
are a priori grounds for considering the chosen copula to be an appropriate model,
such as symmetry or the lack of it and the presence or absence of tail dependence.
The general method will always be similar: we look for a theoretical relationship
between one of the rank correlations and the parameters of the copula and substitute
empirical values of the rank correlation into this relationship to get estimates of
some or all of the copula parameters.
Example 5.52 (bivariate Archimedean copulas with a single parameter). Suppose our assumed model is of the form F(x1, x2) = Cθ(F1(x1), F2(x2)), where θ
is a single parameter to be estimated. For many such copulas a simple functional
relationship exists between either Kendall’s tau and θ or Spearman’s rho and θ. For
speciﬁc examples consider the Gumbel, Clayton and Frank copulas of Section 5.4;
in these cases we have simple relationships of the form ρτ(X1, X2) = f (θ), as
shown in Table 5.5. This suggests we can calibrate these copulas by ﬁrst calculating a sample value rτ for Kendall’s tau and then solving the equation rτ = f ( ˆθ)
for ˆθ, assuming that ˆθ is a valid value in the parameter space of the copula. For
example, Gumbel’s copula is calibrated by taking ˆθ = (1 −rτ)−1, provided that
rτ ⩾0. Clayton’s copula interpolates between perfect negative and perfect positive
dependence and can be calibrated to any sample Kendall’s tau value in (−1, 1).
Example 5.53 (calibrating Gauss copulas using Spearman’s rho). Suppose we
assume a meta-Gaussian model for X with copula CGa
P and we wish to estimate the
correlation matrix P. It follows from Theorem 5.36 that
ρS(Xi, Xj) = (6/π) arcsin 1
2ρij ≈ρij,
where the ﬁnal approximation is very accurate (see Figure 5.10). This suggests we
estimate P by the matrix of pairwise Spearman’s rank correlation coefﬁcients RS.
The method of Example 5.53 could be used to estimate P in a t copula model
Ct
ν,P(F1(x1), . . . , Fd(xd)), although the calibration would not be as accurate as in
the Gaussian case. The value of ρS(Xi, Xj) in terms of ρij is not known in closed
form but simulation studies suggest that the error |ρS(Xi, Xj) −ρij|, while still
modest, is larger than in the Gaussian case. Instead we propose a method based on
Kendall’s tau in the next example, which is based on Proposition 5.37 and could be
applied to all elliptical copulas.
--- page 247 ---

5.5. Fitting Copulas to Data
231
Example 5.54 (calibrating t copulas using Kendall’s tau). Suppose we assume
a meta-t model for X with copula Ct
ν,P and we wish to estimate the correlation
matrix P. It follows from Proposition 5.37 that
ρτ(Xi, Xj) = (2/π) arcsin ρij,
so that a possible estimator of P is the matrix R∗with components given by
r∗
ij = sin( 1
2πrτ
ij). However, there is no guarantee that this componentwise transformation of the matrix of Kendall’s rank correlation coefﬁcients will remain positive deﬁnite (although in our experience it very often does). In this case R∗can be
transformed by the eigenvalue method given in Algorithm 5.55 to obtain a positivedeﬁnite matrix that is close to R∗. The remaining parameter ν of the copula could
then be estimated by maximum likelihood, as discussed in Section 5.5.3.
Algorithm 5.55 (eigenvalue method). Let R∗be a so-called pseudo-correlation
matrix, i.e. a symmetric matrix of pairwise correlation estimates with unit diagonal
entries and off-diagonal entries in [−1, 1] that is not positive semideﬁnite.
(1) Calculate the spectral decomposition R∗= GLG′ as in (3.67), where L is
the matrix of eigenvalues and G is an orthogonal matrix whose columns are
eigenvectors of R∗.
(2) Replace all negative eigenvalues in L by small values δ > 0 to obtain ˜L.
(3) Calculate Q = G ˜LG′, which will be symmetric and positive deﬁnite but not
a correlation matrix, since its diagonal elements will not necessarily equal
one.
(4) Return the correlation matrix R = ℘(Q), where ℘denotes the correlation
matrix operator deﬁned in (3.5).
In Examples 5.53 and 5.54 we saw that it is relatively easy to calibrate the Gauss
copula and the correlation parameter matrix P of the t copula to sample rank correlations. This technique is particularly useful when we have limited multivariate
data and formal estimation of a full multivariate model is unrealistic. Consider the
following hypothetical example.
Example 5.56 (ﬁctitious risk integration situation). Suppose a company is
divided into a number of business units that function semiautonomously. The company management would like to calculate an enterprise-wide P&L distribution for
a one-month period. They have historical data on monthly results for each of the
business units for the last two years only, i.e. 24 observations. However, each business unit believes that through detailed knowledge of their own business going back
over a longer period they can specify their own P&L fairly accurately. Rather than
attempting to ﬁt a multivariate distribution to 24 observations, the risk-management
team decides to combine the individual marginal models provided by each of the
business units using a matrix of rank correlations estimated from the 24 data points.
In this situation we can build multivariate models by combining the known
marginal distributions using any copula that can be calibrated to the estimated rank
--- page 248 ---

232
5. Copulas and Dependence
correlations. The Gaussian and t copulas lend themselves to this purpose and can be
used to build meta-Gaussian and meta-t models that are consistent with the available
information.
Typically, these models could then be used in a Monte Carlo risk analysis; we have
seen in Section 5.1.4 that meta-Gaussian and meta-t models are particularly easy to
simulate. Because the approach is obviously prone to model risk (24 observations
provide very meagre multivariate data) it should be seen as a form of sensitivity
analysis performed using detailed marginal information and only vague dependence information; we might choose to compare a meta-Gaussian model with no tail
dependence and a meta-t model with, say, three degrees of freedom and very strong
tail dependence.
5.5.2
Forming a Pseudo-Sample from the Copula
We now turn to the estimation of parametric copulas by maximum likelihood (ML).
In practical situations we are seldom interested in the copula alone, but also require
estimates of the margins to form a full multivariate model; even when the copula is
of central interest, as it is for us in this chapter, we are forced to estimate margins in
order to estimate the copula, since copula data are almost never observed directly.
While we may attempt to estimate margins and copula in one single optimization, splitting the modelling into two steps can yield more insight and allow a more
detailed analysis of the different model components. In this section we describe
brieﬂy some general approaches to the ﬁrst step of estimating margins and constructing a pseudo-sample of observations from the copula. In the following section we
describe how the copula parameters are estimated by ML from the pseudo-sample.
Let ˆF1, . . . , ˆFd denote estimates of the marginal dfs (possible methods are
discussed below). The pseudo-sample from the copula consists of the vectors
ˆU1, . . . , ˆUn, where
ˆUt = (Ut,1, . . . , Ut,d)′ = ( ˆF1(Xt,1), . . . , ˆFd(Xt,d))′.
(5.51)
Observe that, even if the original data vectors X1, . . . , Xn are iid, the pseudo-sample
data are generally dependent, because the marginal estimates ˆFi will in most cases
be constructed from all of the original data vectors through the univariate samples
X1,i, . . . , Xn,i. Possible methods for obtaining the marginal estimate ˆFi include the
following.
(1) Parametric estimation. We choose an appropriate parametric model for the
data in question and ﬁt it by ML: for ﬁnancial risk factor return data we might
consider the generalized hyperbolic distribution, or one of its special cases such
as Student t or normal inverse Gaussian (NIG); for insurance or operational loss
data we might consider a standard actuarial loss distribution such as Pareto or
lognormal.
(2) Non-parametric estimation with variant of empirical df. We could estimate
Fj using
F ∗
i,n(x) =
1
n + 1
n

t=1
I{Xt,i⩽x},
(5.52)
