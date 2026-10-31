# Quantitative Risk Management_ Concepts, Techniques, and -- Alexander J_ McNeil, Rüdiger Frey, Paul Embrechts -- Princeton series in finance, -- isbn13 9780691122557 -- 478a0059673fecd0c76229cd3d8884e7 -- Anna’s Arc.pdf — pages 115–134

--- page 115 ---

3.3. Spherical and Elliptical Distributions
99
3.3.5
Testing for Elliptical Symmetry
The general problem of this section is to test whether a sample of identically distributed data vectors X1, . . . , Xn has an elliptical distribution Ed(µ, Σ, ψ) for some
µ, Σ and generator ψ. In all of the methods we require estimates of µ and Σ and
these can be obtained using approaches discussed in Section 3.3.4, such as ﬁtting
t distributions, calculating M-estimates or perhaps using (3.56) in the bivariate case.
We denote the estimates simply by ˆµ and ˆΣ.
Generally in ﬁnance we cannot assume that the observations are of iid random
vectors, but we assume that they at least have an identical distribution. Note that,
even if the data were independent, the fact that we generally estimate µ and Σ from
the whole dataset would introduce dependence in the procedures that we describe
below.
Stable correlation estimates: an exploratory method.
An easy exploratory graphical method can be based on Proposition 3.29. We could attempt to estimate
ρ(X | h(X) ⩾c),
h(x) = (x −ˆµ)′ ˆΣ−1(x −ˆµ)
for various values of c ⩾0. We expect that for elliptically distributed data the
estimates will remain roughly stable over a range of different c values. Of course
the estimates of this correlation should again be calculated using some method that
is more efﬁcient than the standard correlation estimator for heavy-tailed data. The
method is most natural as a bivariate method and in this case the correlation of
X | h(X) ⩾c can be estimated by applying the Kendall’s tau transform method to
those data points Xi which lie outside the ellipse deﬁned by h(x) = c. In Figure 3.6
we give an example with both simulated and real data, neither of which show any
marked departure from the assumption of stable correlations. The method is of
course exploratory and does not allow us to come to any formal conclusion.
QQplots.
The remaining methods that we describe rely on the link (3.48) between
non-singular elliptical and spherical distributions. If µ and Σ were known, then we
wouldtestforellipticalsymmetrybytestingthedata{Σ−1/2(Xi−µ) : i = 1, . . . , n}
for spherical symmetry. Replacing these parameters by estimates as above we consider whether the data
{Yi = ˆΣ−1/2(Xi −ˆµ) : i = 1, . . . , n}
(3.57)
are consistent with a spherical distribution, while ignoring the effect of estimation
error.
Some graphical methods based on QQplots have been suggested by Li, Fang and
Zhu (1997) and these are particularly useful for large d. These rely essentially on
the following result.
Lemma 3.32. Suppose that T (Y) is a statistic such that, almost surely,
T (aY) = T (Y)
for every a > 0.
(3.58)
Then T (Y) has the same distribution for every spherical vector Y ∼S+
d (ψ).
--- page 116 ---

100
3. Multivariate Models
•
•
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
••
•
•
•
•
•
•
•
• •
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
••
•
•
•••
••
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
••
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
••
•••••
•
•
•
•
•
•
•
•
•
•
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
• • ••
•
•
••
•
X2
X1
−5
−5
5
5
10
10
0.10
0.10
0.05
0
0
0
−0.05
−0.10
−0.10
−1.0
−0.5
0.5
1.0
• • ••
• • • • • • •
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
•
•••
•
•
•• •
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
••
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
• •
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
•
•
•
•
•
INTC
• • • • • • • • • • •
Outside ellipse
Outside ellipse
1500 800 400 160
80
40
0
0
MSFT
estimate
ρ
0
−1.0
−0.5
0.5
1.0
estimate
ρ
1500 800 400 160
80
40
(a)
(b)
(c)
(d)
Figure 3.6.
Correlations are estimated using the Kendall’s tau method for points lying
outside ellipses of progressively larger size (as shown in (a) and (c)). (a), (b) Two thousand
t-distributed data with four degrees of freedom and ρ = 0.5. (c), (d) Two thousand daily
log-returns on Microsoft and Intel. Dashed lines and points show estimates for an ellipse
that is allowed to grow until there are only 40 points outside; dotted lines show estimates of
correlation for all data.
Proof. From Theorem 3.22 we have T (Y) d= T (RS) and T (RS) a.s.
= T (S) follows
from (3.58). Since the distribution of T (Y) only depends on S and not R it must be
the same for all Y ∼S+
d (ψ).
We exploit this result by looking for statistics T (Y) with the property (3.58) whose
distribution we know when Y ∼Nd(0, Id). Two examples are
T1(Y) =
d1/2 ¯Y

(1/(d −1)) d
i=1(Yi −¯Y)2
,
¯Y = 1
d
d

i=1
Yi,
T2(Y) =
k
i=1 Y 2
i
d
i=1 Y 2
i
.
⎫
⎪⎪⎪⎪⎪⎬
⎪⎪⎪⎪⎪⎭
(3.59)
For Y ∼Nd(0, Id), and hence for Y ∼S+
d (ψ), we have T1(Y) ∼td−1 and
T2(Y) ∼Beta( 1
2k, 1
2(d −k)).
Our experience suggests that the beta-plot is the more revealing of the resulting
QQplots. Li, Fang and Zhu (1997) suggest choosing k such that it is roughly equal to
d −k. In Figure 3.7 we show examples of the QQplots obtained for 2000 simulated
data from a 10-dimensional t distribution with four degrees of freedom and for
the daily, weekly and monthly return data on 10 Dow Jones 30 stocks analysed
in Example 3.3 and Section 3.2.5. The curvature in the plots for daily and weekly
returns seems to be evidence against the elliptical hypothesis.
--- page 117 ---

3.3. Spherical and Elliptical Distributions
101
•••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••
•••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••
•••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••
Theoretical    (2.5,2.5)
•••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••
β
Theoretical    (2.5,2.5)
β
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
0.2
0.4
0.6
0.8
1.0
0
0.2
0.4
0.6
0.8
1.0
0
0.2
0.4
0.6
0.8
0.2
0.4
0.6
0.8
0.2
0.4
0.6
0.8
1.0
0
0.2
0.4
0.6
0.8
0
Empirical
Empirical
(a)
(c)
(d)
(b)
Figure 3.7.
QQplots of the beta-statistic (3.59) for four datasets with dimension d = 10;
we have set k = 5. (a) Two thousand simulated observations from t distribution with four
degrees of freedom. (b) Daily, (c) weekly and (d) monthly returns on Dow Jones stocks as
analysed in Example 3.3 and Section 3.2.5. Daily and weekly returns show evidence against
elliptical symmetry.
Numerical tests.
We restrict ourselves to simple ideas for bivariate tests; references
to more general test ideas are found in Notes and Comments. If we neglect the
error involved in estimating location and dispersion, testing for elliptical symmetry
amounts to testing the Yi data in (3.57) for spherical symmetry. For i = 1, . . . , n,
if we set Ri = ∥Yi∥and Si = Yi/∥Yi∥, then under the null hypothesis the Si data
should be uniformly distributed on the unit sphere Sd−1, and the paired data (Ri, Si)
should form realizations of independent pairs.
In the bivariate case, testing for uniformity on the unit circle S1 amounts to a
univariate test of uniformity on [0, 2π] for the angles Θi described by the points
Si = (cos Θi, sin Θi)′ on the perimeter of the circle; equivalently, we may test the
data {Ui := Θi/(2π) : i = 1, . . . , n} for uniformity on [0, 1]. Neglecting issues
of serial dependence in the data, this may be done, for instance, by a standard chisquared goodness-of-ﬁt test (see Rice 1995, p. 241) or a Kolmogorov–Smirnov test
(see Conover 1999).Again neglecting issues of serial dependence, the independence
of the components of the pairs {(Ri, Ui) : i = 1, . . . , n} could be examined by
performing a test of association with Spearman’s rank correlation coefﬁcient (see,
for example, Conover 1999, pp. 312–328).
We have performed these tests for the two datasets used in Figure 3.6, these being
2000 simulated bivariate t data with four degrees of freedom and 2000 daily logreturns for Intel and Microsoft. In Figure 3.8 the transformed data on the unit circle
Si and the implied angles Ui on the [0, 1] scale are shown; the dispersion matrices
--- page 118 ---

102
3. Multivariate Models
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
..
.
.
.
.
.
.
.
.
.
.
.
.
.
.
..
.
.
.
.
..
.
.
.
.
.
..
.
.
.
.
.
.
.
.
.
.
.
.
..
.
.
.
.
.
.
.
..
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
..
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
. .
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
..
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
. .
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
. .
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
. .
.
.
.
.
.
.
.
.
.
.
.
.
..
.
.
.
.
.
.
.
.
.
. .
.
.
..
.
.
.
.
.
.
.
.
.
. .
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
...
.
.
.
.
.
.
. .
.
.
.
.
.
.
..
.
.
.
.
..
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
..
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
..
.
.
.
.
.
.
.
.
.
.
.
.
..
.
.
.
.
.
.
.
.
.
.
.
.
.
..
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
..
.
.
.
.
.
.
.
.
.
.
..
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
. .
.
.
. .
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
..
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
..
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
..
..
.
.
.
.
.
.
..
.
.
.
.
.
.
.
.
.
.
.
.
.
.
..
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
..
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
..
.
.
.
.
.
.
.
.
.
.
.
.
..
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
. .
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
..
.
..
.
.
.
.
.
.
. .
.
.
.
.
. .
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
...
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
..
.
.
.
.
..
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
..
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
..
.
.
.
.
..
.
.
.
.
.
..
.
.
.
. .
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
..
.
..
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
..
.
.
.
.
.
.
.
.
.
.
.
.
. .
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
. .
.
.
.
.
..
.
.
.
.
.
.
.
.
.
.
.
.
..
.
.
.
.
.
.
. .
.
.
.
.
.
.
.
.
..
.
.
.
..
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
..
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
..
.
. .
.
.
.
.
.
.
.
.
.
.
.
.
. .
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
...
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
. .
.
.
.
.
.
.
.
.
.
.
.
.
.
...
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
..
.
.
.
.
.
.
.
.
.
.
..
.
.
..
...
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
..
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
..
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
..
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
..
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
..
.
.
.
.
.
.
.
..
.
.
.
.
.
.
.
.
.
.
. .
.
. .
.
.
.
.
..
.
.
.
.
.
.
.
.
.
.
. ..
.
..
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
..
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
..
.
.
.
.
.
.
.
.. .
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
...
.
.
.
.
.
.
..
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
. .
.
.
.
.
.
.
.
.
..
.
.
.
.
.
.
.
.
. .
.
.
.
.
.
.
...
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
..
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
..
..
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
. .
.
.
.
.
.
.
.
.
.
.
.
.
.
.
..
.
.
.
.
. .
.
.
. .
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
..
.
.
.
.
.
.
.
.
. .
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
..
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
. . . .
.
...
.
.
.
.
.
..
.
.
.
..
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
0
100
150
200
.
.
.
.
.
.
.
.
..
.
.
.
.
.
.
.
.
.
.
.
.
.
..
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
..
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
. .
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
..
.
.
.
.
.
.
.
.
.
.
.
.
..
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
...
.
. .
.
.
.
.
.
.
.
. .
.
.
.
..
.
.
.
.
.
.
. .
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
..
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
..
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
..
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
. .
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
..
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
..
.
.
.
.
.
.
.
.
.
.
.
.
.
..
. .
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
..
.
..
.
.
.
.
.
.
.
.
.
.
.
..
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
..
.
.
.
.
.
.
.
..
.
.
.
.
.
.
.
.
.
.
.
..
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
..
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.. ..
..
.
.
.
.
.
.
.
.
.
.
.
.
. .
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
..
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
. .
.
.
.
.
.
.
.
.
.
. .
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
..
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
. .
.
.
.
.
.
.
.
.
.
.
.
.
.
.
..
.
.
.
.
.
.
.
.
.
.
..
..
.
.
.
.
.
.
.
.
.
.
.
.
.
..
.
.
.
.
.
.
.
.
.
.
.
.
.
.
..
.
.
.
.
.
.
.
.
.
.
.
.
. .
.
..
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
..
.
.
.
.
.
.
.
.
.
.
.
.
.
. .
.
.
.
..
.
.
.
..
.
.
.
.
.
.
.
.
.
.
..
.
.
.
.
.
.
.
. .
.
.
.
.
.
.
.
.
.
.
.
..
.
.
.
..
.
.
.
.
.
.
.
.
.
.
..
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
. .
.
.
.
.
.
.
.
.
.
..
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
. .
.
..
.
..
.
.
.
.
.
.
.
.
.
..
.
.
.
.
.
.
.
.
.
.
.
.
.
..
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
..
.
.
.
.
.
.
.
.
.
.
.
. .
..
.
.
.
.
.
.
..
.
.
.
.
..
.
.
.
.
.
.
..
.
.
.
.
.
.
.
.
.
.
.
..
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
. .
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
..
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
. .
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
..
. .
.
..
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
..
.
.
.
.
.
.
.
.
.
.
.
. .
.
.
.
..
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
..
.
.
..
.
.
..
.
.
.
..
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
..
.
.
.
.
.
.
.
.
.
.
.
.
..
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
. .
.
.
.
. .
.
.
.
.
.
.
. .
..
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
..
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
..
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
..
.
.
.
.
.
.
..
.
.
.
.
.
.
.
.
.
.
.
.
.
.
..
.
.
.
.
.
.
.
.
.
.
.
.
..
.
.
.
.
.
..
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
..
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
..
.
.
. .
.
.
.
.
.
.
.
.
.
.
.
.
.
.
..
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
. .
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
..
.
.
. .
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
. .
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
. .
.
..
.
..
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
..
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
. .
.
.
.
.
.
..
.
.
..
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
. .
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
..
.
.
.
.
.
.
.
.
.
. .
.
. .
.
.
.
.
.
.
.
.
.
.
.
.
.
.
..
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
. .
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
..
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
...
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
..
.
.
.
.
.
.
.
.
.
.
.
.
.
.
0
100
150
200
50
50
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
−1.0
−0.5
0
0.5
1.0
0
0.2
0.4
0.6
0.8
1.0
S2
S1
S2
U
(a)
(b)
Figure 3.8.
Illustration of the transformation of bivariate data to points on the unit circle
S1 using the transformation Si = Yi/∥Yi∥, where the Yi data are deﬁned in (3.57); the
angles of these points are then transformed on to the [0, 1] scale, where they can be tested for
uniformity. (a) Two thousand simulated t data with four degrees of freedom. (b) Two thousand
Intel and Microsoft log-returns. Neither show strong evidence against elliptical symmetry.
have been estimated using the construction (3.56) based on Kendall’s tau. Neither
of these datasets shows signiﬁcant evidence against the elliptical hypothesis. For the
bivariate t data the p-values for the chi-squared and Kolmogorov–Smirnov tests of
uniformity and the Spearman’s rank test of association are, respectively, 0.99, 0.90
and 0.10. For the stock-return data they are 0.08, 0.12 and 0.19. Note that simulated
data from lightly skewed members of the generalized hyperbolic family often do
fail these tests.
Notes and Comments
AcomprehensivereferenceforsphericalandellipticaldistributionsisFang,Kotzand
Ng (1987); we have based our brief presentation of the theory on this account. Other
references for the theory are Kelker (1970), Cambanis, Huang and Simons (1981)
and Bingham and Kiesel (2002), the latter in the context of ﬁnancial modelling. The
original reference for Theorem 3.22 is Schoenberg (1938). Frahm (2004) suggests
a generalization of the elliptical class to allow asymmetric models while preserving
many of the attractive properties of the elliptical distributions.
There is a vast literature on alternative estimators of dispersion and correlation
matrices, particularly with regard to better robustness properties.Textbooks with relevant sections include Huber (1981), Hampel et al. (1986), Marazzi (1993), Wilcox
--- page 119 ---

3.4. Dimension Reduction Techniques
103
(1997) and Dell’Aquila and Ronchetti (2005); the latter book is recommended in
general for applications of robust statistics in econometrics and ﬁnance.
We have concentrated on M-estimation of dispersion matrices, since this is related
to the maximum likelihood estimation of alternative elliptical models. M-estimators
have a relatively long history and are known to have good local robustness properties (insensitivity to small data perturbations); they do, however, have relatively
low breakdown points in high dimensions, so their performance can be poor under
larger contaminations of the data. A small selection of papers on M-estimation
includes Maronna (1976), Devlin, Gnanadesikan and Kettenring (1975, 1981) and
Tyler (1983, 1987); see also Frahm (2004), in which an interesting alternative derivation of a Tyler estimator is given. The method based on Kendall’s tau was suggested
in Lindskog, McNeil and Schmock (2003).
The QQplots for testing spherical symmetry were suggested by Li, Fang and Zhu
(1997). There is a large literature on tests of spherical symmetry, including Smith
(1977), Kariya and Eaton (1977), Beran (1979) and Baringhaus (1991). This work
is also related to tests of uniformity for directional data: see Mardia (1972), Gin´e
(1975) and Prentice (1978).
3.4
Dimension Reduction Techniques
The techniques of dimension reduction, such as factor modelling and principal components, are central to multivariate statistical analysis and are widely used in econometric model building. In the high-dimensional world of ﬁnancial risk management
they are essential tools. For this reason, and also because we will build on the techniques in some of the multivariate time series models described in Chapter 4, we
include a concise summary of the more important information. For further reading and more detail it will be necessary to consult references listed in Notes and
Comments.
3.4.1
Factor Models
By using a factor model we attempt to explain the randomness in the components
of a d-dimensional vector X in terms of a smaller set of common factors. If the
components of X represent, for example, equity returns, it is clear that a large part
of their variation can be explained in terms of the variation of a smaller set of market
index returns. Formally we deﬁne a factor model as follows.
Deﬁnition 3.33 (linear factor model). The random vector X is said to follow a
p-factor model if it can be decomposed as
X = a + BF + ε,
(3.60)
where
(i) F = (F1, . . . , Fp)′ is a random vector of common factors with p < d and a
covariance matrix that is positive deﬁnite;
(ii) ε = (ε1, . . . , εd)′ is a random vector of idiosyncratic error terms, which are
uncorrelated and have mean zero;
--- page 120 ---

104
3. Multivariate Models
(iii) B ∈Rd×p is a matrix of constant factor loadings and a ∈Rd is a vector of
constants; and
(iv) cov(F, ε) = E((F −E(F))ε′) = 0.
The assumptions that the errors are uncorrelated with each other (ii) and also
with the common factors (iv) are an important part of this deﬁnition. We do not in
general require independence, only uncorrelatedness. However, if the vector X is
multivariate normally distributed and follows the factor model in (3.60), then it is
possible to ﬁnd a version of the factor model where F and ε are Gaussian and the
errors can be assumed to be mutually independent and independent of the common
factors. We elaborate on this assertion in Example 3.34 below.
It follows from the basic assumptions that factor models imply a special structure
for the covariance matrix Σ of X. If we denote the covariance matrix of F by Ω
and that of ε by the diagonal matrix Υ , it follows that
Σ = cov(X) = BΩB′ + Υ.
(3.61)
If the factor model holds, the common factors can always be transformed so that
they are mean zero and orthogonal. By setting F ∗= Ω−1/2(F −E(F)) and B∗=
BΩ1/2, we have a representation of the factor model of the form X = µ+B∗F ∗+ε,
where µ = E(X) as usual and Σ = B∗(B∗)′ + Υ .
Conversely, it can be shown that whenever a random vector X has a covariance
matrix which satisﬁes
Σ = BB′ + Υ
(3.62)
for some B ∈Rd×p with rank(B) = p < d and diagonal matrix Υ , then X
has a factor-model representation for some p-dimensional factor vector F and ddimensional error vector ε.
Example 3.34 (the equicorrelation model). Suppose X is a random vector with
standardized margins (zero mean and unit variance) and an equicorrelation matrix;
in other words, the correlation between each pair of components is equal to ρ > 0.
This means that the covariance matrix Σ can be written as Σ = ρJd + (1 −ρ)Id,
where Jd is the d-dimensional square matrix of ones and Id is the identity matrix,
so that Σ is obviously of the form (3.62) for the d-vector B = √ρ1.
To ﬁnd a factor decomposition of X take any zero-mean, unit-variance rv Y that
is independent of X and deﬁne a single common factor F and errors ε by
F =
√ρ
1 + ρ(d −1)
d

j=1
Xj +

1 −ρ
1 + ρ(d −1)Y,
εj = Xj −√ρF,
where we note that in this construction F also has mean zero and unit variance.
Thus we have the factor decomposition X = BF + ε and it may be veriﬁed by
calculation that cov(F, εj) = 0 for all j and cov(εj, εk) = 0 when j̸ = k, so
that the requirements of Deﬁnition 3.33 are satisﬁed. A random vector with an
equicorrelation matrix can be thought of as following a factor model with a single
common factor.
--- page 121 ---

3.4. Dimension Reduction Techniques
105
Since we can take any Y, the factors and errors in this decomposition are nonunique. Consider the case where the vector X is Gaussian; it is most convenient
to take Y to also be Gaussian, since in that case the common factor is normally
distributed, the error vector is multivariate normally distributed, Y is independent
of εj, for all j, and εj and εk are independent for j̸ = k. Since var(εj) = 1 −ρ, it
is most convenient to write the factor model implied by the equicorrelation model
as
Xj = √ρF +

1 −ρZj,
j = 1, . . . , d,
(3.63)
where F, Z1, . . . , Zd are mutually independent standard Gaussian rvs. This model
will be used in Section 8.3.5 in the context of modelling homogeneous credit portfolios. For the more general construction on which this example is based see Mardia,
Kent and Bibby (1979, Exercise 9.2.2).
3.4.2
Statistical Calibration Strategies
Now assume that we have data X1, . . . , Xn ∈Rd representing risk-factor returns.
Each vector observation Xt recorded at a time t is assumed to be generated by the
factor model (3.60) for some common-factor vector Ft and some error vector εt.
There are a number of different approaches to the practical calibration of a factor
model, depending on the situation and, in particular, on whether or not the factor is
also observable or considered to be unobservable or latent.
In an observable factor model we assume that appropriate factors for the return
series in question have been identiﬁed in advance and data on these factors have
been collected. A simple example would be a one-factor model where F1, . . . , Fn
are observations of the return on a market index and X1, . . . , Xn are individual
equity returns to be explained in terms of the market return (a model known in
econometrics as Sharpe’s single-index model). Fitting of the model (estimation of
B and a) is accomplished by regression techniques, and is described in Section 3.4.3.
In a latent factor model appropriate factors are themselves estimated from the
data X1, . . . , Xn. Here we envisage a situation where the Xt represent returns for
a set of disparate risk factors and it is not clear a priori what the best set of factors
might be. There are two general strategies for ﬁnding factors. The ﬁrst strategy,
which is quite common in ﬁnance, is to use the method of principal components to
construct factors. We note that the factors we obtain, while being explanatory in a
statistical sense, may not have any obvious interpretation.
In the second approach, classical statistical factor analysis, it is assumed that
the data are identically distributed with a distribution whose covariance matrix has
the factor structure (3.62). Various techniques are used to estimate B and Υ and
then these estimates are used in turn to construct factor data. We will not go into
the details of this method further—they are found in standard texts on multivariate
statistical analysis (see Notes and Comments).
In the context of risk management, the goal of all approaches to factor models is
to obtain factor data Ft and loading matrices B (and the constant vector a where
relevant). If this is achieved, we can then concentrate on modelling the distribution
or dynamics of F1, . . . , Fn, which is a lower-dimensional problem than modelling
--- page 122 ---

106
3. Multivariate Models
X1, . . . , Xn. The unobserved errors ε1, . . . , εn are of secondary importance. In
situations where we have many risk factors the risk embodied in the errors is partly
mitigated by a diversiﬁcation effect, whereas the risk embodied in the common
factors remains. The following simple example gives an idea why this is the case.
Example 3.35. We continue our analysis of the one-factor model in Example 3.34.
Suppose the random vector X in that example represents the return on d different
companies so that the rv Z(d) = (1/d) d
j=1 Xj can be thought of as the portfolio
return for an equal investment in each of the companies. We calculate that
Z(d) = 1
d 1′BF + 1
d 1′ε = √ρF + 1
d
d

j=1
εj.
The risk in the ﬁrst term is not affected by increasing the size of the portfolio d,
whereas the risk in the second term can be reduced. Suppose we measure risk by
simply calculating variances; we get
var(Z(d)) = ρ + 1 −ρ
d
→ρ,
d →∞,
so that the systematic factor is the main contributor to the risk in a large-portfolio
situation.
We now discuss in a little more detail the ﬁtting of observable factor models
by regression. The approach to factor models based on principal components is
described in Section 3.4.4. Principal component analysis is covered there in some
detail, since it is an important technique in its own right.
3.4.3
Regression Analysis of Factor Models
Two equivalent approaches may be used to estimate the model parameters. We write
the model as
Xt = a + BFt + εt,
t = 1, . . . , n,
(3.64)
where Xt and Ft are vectors of individual returns and factors (for example, index
returns) at time t, and a and B are parameters to be estimated. In the ﬁrst approach
we perform d univariate regression analyses, one for each component of the individual return series. In the second approach we estimate all parameters in a single
multivariate regression.
Univariate regression.
Writing Xt,j for the observation at time t of instrument j
we consider the univariate regression model
Xt,j = aj + b′
jFt + εt,j,
t = 1, . . . , n.
This is known as a time series regression, since the responses X1,j, . . . , Xn,j form a
univariate time series and the factors F1, . . . , Fn form a possibly multivariate time
series. Without going into technical details or anticipating any of the time series
material in Chapter 4 we simply remark that the parameters aj and bj are estimated
using the standard ordinary least-squares (OLS) method found in all textbooks on
--- page 123 ---

3.4. Dimension Reduction Techniques
107
linear regression. To justify the use of the method and to derive statistical properties of the method it is usually assumed that, conditional on the factors, the errors
ε1,j, . . . , εn,j are identically distributed and serially uncorrelated. (This means they
form what will be referred to in Chapter 4 as white noise.)
The estimate ˆaj obviously estimates the jth component of a, while ˆbj is an
estimate of the jth row of the matrix B. By performing a regression for each of the
univariate time series X1,j, . . . , Xn,j for j = 1, . . . , d, we complete the estimation
of the parameters a and B.
Multivariate regression.
To set the problem up as a multivariate linear-regression
problem, we construct a number of large matrices:
X =
⎛
⎜⎜⎝
X′
1...
X′
n
⎞
⎟⎟⎠
  
n×d
,
F =
⎛
⎜⎜⎝
1
F ′
1
...
...
1
F ′
n
⎞
⎟⎟⎠



n×(p+1)
,
B2 =

a′
B′

  
(p+1)×d
,
E =
⎛
⎜⎜⎝
ε′
1...
ε′
n
⎞
⎟⎟⎠
  
n×d
.
Each row of the data X corresponds to a vector observation at a ﬁxed time point t,
and each column corresponds to a univariate time series for one of the individual
returns. The model (3.64) can then be expressed by the matrix equation
X = FB2 + E,
(3.65)
where B2 is the matrix of regression parameters to be estimated.
If we assume that the unobserved error vectors ε1, . . . , εn comprising the rows of
E are identically distributed and serially uncorrelated, conditional on F1, . . . , Fn,
then the equation (3.65) deﬁnes a standard multivariate linear regression (see, for
example, Mardia, Kent and Bibby (1979) for the standard assumptions).An estimate
of B2 is obtained by multivariate OLS according to the formula
ˆB2 = (F ′F)−1F ′X.
(3.66)
The factor model is now essentially calibrated, since we have estimates for a
and B. The model can now be critically examined with respect to the original conditions of Deﬁnition 3.33. Do the errors vectors εt come from a distribution with
diagonal covariance matrix, and are they uncorrelated with the factors?
To learn something about the errors, we can form the model residual matrix
ˆE = X −F ˆB2. Each row of this matrix contains an inferred value of an error vector
ˆεt at a ﬁxed point in time. Examination of the sample correlation matrix of these
inferred error vectors will hopefully show that there is little remaining correlation in
the errors (or at least much less than in the original data vectors Xt). If this is the case,
then the diagonal elements of the sample covariance matrix of the ˆεt could be taken
as an estimator ˆΥ for Υ . It is sometimes of interest to form the covariance matrix
implied by the factor model and compare this with the original sample covariance
matrix S of the data. The implied covariance matrix is
ˆΣ(F) = ˆB ˆΩˆB′ + ˆΥ ,
where ˆΩ=
1
n −1
n

t=1
(Ft −¯F)(Ft −¯F)′.
--- page 124 ---

108
3. Multivariate Models
Table 3.6.
The ﬁrst line gives estimates of B for a multivariate regression model ﬁtted to
10 Dow Jones 30 stocks where the observed common factor is the return on the Dow Jones
30 index itself. The second row gives r2 values for a univariate regression model for each
individual time series. The next 10 lines of the table give the sample correlation matrix of the
data R, while the middle 10 lines give the correlation matrix implied by the factor model.
The ﬁnal 10 lines show the estimated correlation matrix of the residuals from the regression
model, with entries less than 0.1 in absolute value being omitted. See Example 3.36 for full
details.
MO
KO
EK
HWP
INTC
MSFT
IBM
MCD
WMT
DIS
ˆB
0.87
1.01
0.77
1.12
1.12
1.11
1.07
0.86
1.02
1.03
r2
0.17
0.33
0.14
0.18
0.17
0.21
0.22
0.23
0.24
0.26
MO
1.00
0.27
0.14
0.17
0.16
0.25
0.18
0.22
0.16
0.22
KO
0.27
1.00
0.17
0.22
0.21
0.25
0.18
0.36
0.33
0.32
EK
0.14
0.17
1.00
0.17
0.17
0.18
0.15
0.14
0.17
0.16
HWP
0.17
0.22
0.17
1.00
0.42
0.38
0.36
0.20
0.22
0.23
INTC
0.16
0.21
0.17
0.42
1.00
0.53
0.36
0.19
0.22
0.21
MSFT
0.25
0.25
0.18
0.38
0.53
1.00
0.33
0.22
0.28
0.26
IBM
0.18
0.18
0.15
0.36
0.36
0.33
1.00
0.20
0.20
0.20
MCD
0.22
0.36
0.14
0.20
0.19
0.22
0.20
1.00
0.26
0.26
WMT
0.16
0.33
0.17
0.22
0.22
0.28
0.20
0.26
1.00
0.28
DIS
0.22
0.32
0.16
0.23
0.21
0.26
0.20
0.26
0.28
1.00
MO
1.00
0.24
0.16
0.18
0.17
0.19
0.20
0.20
0.20
0.21
KO
0.24
1.00
0.22
0.24
0.23
0.26
0.27
0.28
0.28
0.29
EK
0.16
0.22
1.00
0.16
0.15
0.17
0.18
0.18
0.18
0.19
HWP
0.18
0.24
0.16
1.00
0.17
0.19
0.20
0.20
0.21
0.22
INTC
0.17
0.23
0.15
0.17
1.00
0.19
0.19
0.19
0.20
0.21
MSFT
0.19
0.26
0.17
0.19
0.19
1.00
0.22
0.22
0.22
0.23
IBM
0.20
0.27
0.18
0.20
0.19
0.22
1.00
0.23
0.23
0.24
MCD
0.20
0.28
0.18
0.20
0.19
0.22
0.23
1.00
0.23
0.24
WMT
0.20
0.28
0.18
0.21
0.20
0.22
0.23
0.23
1.00
0.25
DIS
0.21
0.29
0.19
0.22
0.21
0.23
0.24
0.24
0.25
1.00
MO
1.00
KO
1.00
−0.12
0.12
EK
1.00
HWP
1.00
0.30
0.24
0.20
INTC
0.30
1.00
0.43
0.20
MSFT
0.24
0.43
1.00
0.14
IBM
−0.12
0.20
0.20
0.14
1.00
MCD
0.12
1.00
WMT
DIS
1.00
We would hope that ˆΣ(F) captured much of the structure of S and that the correlation
matrix R(F) := ℘( ˆΣ(F)) captured much of the structure of the sample correlation
matrix R = ℘(S).
--- page 125 ---

3.4. Dimension Reduction Techniques
109
Example 3.36 (single-index model for Dow Jones 30 returns). As a simple example of the regression approach to ﬁtting factor models we have ﬁtted a single factor
model to a set of 10 Dow Jones 30 daily stock-return series from 1992 to 1998.
Note that these are different returns to those analysed in previous sections of this
chapter. They have been chosen to be of two types: technology-related titles like
Hewlett-Packard, Intel, Microsoft and IBM; and foodand consumer-related titles
like Philip Morris, Coca-Cola, Eastman Kodak, McDonald’s, Wal-Mart and Disney.
The factor chosen is the corresponding return on the Dow Jones 30 index itself.
The estimate of B implied by formula (3.66) is shown in the ﬁrst line of Table 3.6.
The highest values of B correspond to so-called high beta stocks; since a one-factor
model implies the relationship E(Xj) = aj + BjE(F), these stocks potentially
offer high expected returns relative to the market (but are often riskier titles); in
this case the four technology-related stocks have the highest beta values. In the
second row, values of r2, the so-called coefﬁcient of determination, are given for
each of the univariate regression models. This number measures the strength of the
regression relationship between Xj and F and can be interpreted as the proportion
of the variation of the stock return that is explained by variation in the market return;
the highest r2 corresponds to Coca-Cola (33%) and in general it seems that about
20% of individual stock-return variation is explained by market-return variation.
The next 10 lines of the table give the sample correlation matrix of the data R,
while the middle 10 lines give the correlation matrix implied by the factor model
(corresponding to ˆΣ(F)). The latter matrix picks up much, but not all, of the structure
of the former matrix. The ﬁnal 10 lines show the estimated correlation matrix of the
residuals from the regression model, but only those elements which exceed 0.1 in
absolute value. The residuals are indeed much less correlated than the original data,
but a few larger entries indicate imperfections in the factor-model representation
of the data, particularly for the technology stocks. The index return for the broader
market is clearly an important common factor but further systematic effects appear
to be present in these data that are not captured by the index.
3.4.4
Principal Component Analysis
The aim of principal component analysis (PCA) is to reduce the dimensionality of
highly correlated data by ﬁnding a small number of uncorrelated linear combinations
that account for most of the variability of the original data, in some appropriately
deﬁned sense. PCA is not itself a model, but rather a data-rotation technique. However, it can be used as a way of constructing appropriate factors for a factor model,
and this is the main application we consider in this section.
The key mathematical result behind the technique is the spectral decomposition
theorem of linear algebra, which says that any symmetric matrix A ∈Rd×d can be
written as
A = Γ ΛΓ ′,
(3.67)
where
(i) Λ = diag(λ1, . . . , λd) is the diagonal matrix of eigenvalues of A which,
without loss of generality, are ordered so that λ1 ⩾λ2 ⩾· · · ⩾λd, and
--- page 126 ---

110
3. Multivariate Models
(ii) Γ is an orthogonal matrix satisfying Γ Γ ′ = Γ ′Γ = Id whose columns are
standardized eigenvectors of A (i.e. eigenvectors with length 1).
Theoretical principal components.
Obviously we can apply this decomposition
to any covariance matrix Σ, and in this case the positive semideﬁniteness of Σ
ensures that λj ⩾0 for all j. Suppose the random vector X has mean vector µ
and covariance matrix Σ and we make the decomposition Σ = Γ ΛΓ ′ as in (3.67).
Then the principal components transform of X is deﬁned to be
Y = Γ ′(X −µ),
(3.68)
and can be thought of as a rotation and a recentring of X. The jth component of
the rotated vector Y is known as the jth principal component of X and is given by
Yj = γ ′
j(X −µ),
(3.69)
where γj is the eigenvector of Σ corresponding to the jth ordered eigenvalue; this
vector is also known as the jth vector of loadings.
Simple calculations reveal that
E(Y) = 0
and
cov(Y) = Γ ′ΣΓ = Γ ′Γ ΛΓ ′Γ = Λ,
so that the principal components of Y are uncorrelated and have variances
var(Yj) = λj, ∀j. The components are thus ordered by variance, from largest to
smallest. Moreover, the ﬁrst principal component can be shown to be the standardized linear combination of X which has maximal variance among all such
combinations; in other words,
var(γ ′
1X) = max{var(a′X) : a′a = 1}.
For j = 2, . . . , d, the jth principal component can be shown to be the standardized
linear combination of X with maximal variance among all such linear combinations
that are orthogonal to (and hence uncorrelated with) the ﬁrst j −1 linear combinations. The ﬁnal dth principal component has minimum variance among standardized
linear combinations of X.
To measure the ability of the ﬁrst few principal components to explain the variability in X we observe that
d

j=1
var(Yj) =
d

j=1
λj = trace(Σ) =
d

j=1
var(Xj).
If we interpret trace(Σ) = d
j=1 var(Xj) as a measure of the total variability in
X, then, for k ⩽d, the ratio k
j=1 λj/ d
j=1 λj represents the amount of this
variability explained by the ﬁrst k principal components.
Sampleprincipalcomponents.
Assumethatwehavemultivariatedataobservations
X1, . . . , Xn with identical distribution and unknown covariance matrix Σ, which
we estimate by the sample covariance matrix
Sx = 1
n
n

t=1
(Xt −¯X)(Xt −¯X)′.
--- page 127 ---

3.4. Dimension Reduction Techniques
111
We apply the spectral decomposition (3.67) to the symmetric, positive semideﬁ-
nite matrix Sx to get
Sx = GLG′,
where G is the eigenvector matrix, L = diag(l1, . . . , ld) is the diagonal matrix
consisting of ordered eigenvalues, and we switch to roman letters to emphasize that
these are now calculated from an empirical covariance matrix.
The eigenvectors, or loading vectors, gj making up the columns of G deﬁne the
empirical principal components transform and, by analogy with (3.69), the value
Yt,j given by
Yt,j = g′
j(Xt −¯X)
can be considered to be an observation of the jth sample principal component at
time t. The vectors Yt = (Yt,1, . . . , Yt,d)′ = G′(Xt −¯X) constitute rotations of the
original data vectors Xt. The rotated data vectors Y1, . . . , Yn have the property
that their sample covariance matrix is L = diag(l1, . . . , ld), the diagonal matrix of
eigenvalues of Sx, as is easily veriﬁed:
Sy = 1
n
n

t=1
(Yt −¯Y)(Yt −¯Y)′ = 1
n
n

t=1
YtY ′
t
= 1
n
n

t=1
G′(Xt −¯X)(Xt −¯X)′G = G′SxG = L.
Thus the rotated vectors show no correlation between components and the components are ordered by their sample variances, from largest to smallest.
Remark 3.37. In a situation where the different components of the data vectors
X1, . . . , Xn have very different sample variances (particularly if they are measured
on very different scales), it is to be expected that the component (or components)
with largest variance will dominate the ﬁrst loading vector g1 and dominate the
ﬁrst principal component. In these situations the data are often transformed to have
identical variances, which effectively means that principal components analysis
is applied to the sample correlation matrix Rx. Note also that we could derive
sample principal components from a robust estimate of the correlation matrix or a
multivariate dispersion matrix.
Principal components as factors.
The principal components transform in (3.68) is
invertible, giving us X = µ+Γ Y, where the random vector Y contains the principal
components ordered from top to bottom by their variance. Let us suppose that we
believe that the ﬁrst k components explain the most important portion of the total
variability of X. We could partition Y according to (Y ′
1, Y ′
2)′, where Y1 ∈Rk and
Y2 ∈Rd−k; similarly, we could partition Γ according to (Γ1, Γ2), where Γ1 ∈Rd×k
and Γ2 ∈Rd×(d−k). This yields the representation
X = µ + Γ1Y1 + Γ2Y2 = µ + Γ1Y1 + ε,
(3.70)
where Γ2Y2 can be regarded as an error since its covariance matrix contains very
small entries in comparison with the covariance matrix of Γ1Y1.
--- page 128 ---

112
3. Multivariate Models
10
12
Variances
0.352
0.468
0.56
0.637 0.712 0.786 0.848 0.907
8
6
4
2
0
F1
F2
F3
F4
F5
F6
F7
F8
Figure 3.9.
Barplot of the sample variances lj of the ﬁrst eight principal components; above
each bar the cumulative proportion of the total variance explained by the components is given
(k
j=1 lj/ 10
j=1 lj, k = 1, . . . , 8).
Equation (3.70) is reminiscent of the factor model (3.60), except that the errors
do not have a diagonal covariance matrix. Nevertheless, the principal components
approach to constructing a factor model is generally to equate the ﬁrst k principal
components Y1 with the factors F, to equate the matrix Γ1 containing the ﬁrst k
eigenvectors with the factor loading matrix B, and to ignore the errors entirely. The
factors are thus given by Ft = (γ ′
1X, . . . , γ ′
kX)′.
Example 3.38 (PCA-based factor model for Dow Jones 30 returns). We consider the data in Example 3.36 again. Principal components analysis is applied to
the sample covariance matrix of the return data and the results are summarized in
Figures 3.9 and 3.10. In the former we see a barplot of the sample variances of the
ﬁrst eight principal components lj; above each bar the cumulative proportion of
the total variance explained by the components is given; the ﬁrst two components
explain almost 50% of the variation. In the latter plot the ﬁrst two loading vectors
g1 and g2 are summarized.
The ﬁrst vector of loadings is positively weighted for all stocks and can be thought
of as describing a kind of index portfolio; of course the weights in the loading
vector do not sum to one, but they can be scaled to do so and this gives a so-called
principal-component-mimicking portfolio. The second vector has positive weights
for the consumer titles and negative weights for the technology titles; as a portfolio it
can be thought of as prescribing a programme of short-selling of technology to buy
the consumer titles. These ﬁrst two sample principal components loadings vectors
are used to deﬁne factors.
--- page 129 ---

3.4. Dimension Reduction Techniques
113
MO
KO
EK
INTC
MSFT
DIS
WMT
MCD
IBM
HWP
MO
KO
EK
INTC
MSFT
DIS
WMT
MCD
IBM
HWP
0.1 0.2 0.3 0.4 0.5
0
0.2
0.4
0
(a)
(b)
−0.2
−0.4
Figure 3.10.
Barplot summarizing the loadings vectors g1 and g2 deﬁning the ﬁrst two
principal components: (a) factor 1 loadings; and (b) factor 2 loadings.
In Table 3.7 the transpose of the matrix ˆB (containing the loadings estimates in the
factor model) is shown; the rows are merely the ﬁrst two loadings vectors from the
principal components analysis. In the third row, values of r2, the so-called coefﬁcient
of determination, are given for each of the univariate regression models and these
indicate that more of the variation in the data is explained by the two PCA-based
factors than was explained by the observed factor in Example 3.36; Intel returns
seem to be best explained by the model.
The next 10 lines give the correlation matrix implied by the factor model (corresponding to ˆΣ(F)). Compared with the true sample correlation matrix in Example 3.36
this seems to pick up more of the structure than did the correlation matrix implied
by the observed factor model.
The ﬁnal 10 lines show the estimated correlation matrix of the residuals from the
regression model, but only those elements which exceed 0.1 in absolute value. The
residuals are again less correlated than the original data, but there are quite a number
of larger entries, indicating imperfections in the factor-model representation of the
data. In particular, we have introduced a number of larger negative correlations into
the residuals; in practice, we seldom expect to ﬁnd a factor model where the residuals
have a covariance matrix that appears perfectly diagonal.
Notes and Comments
We have based our discussion of factor models, multivariate regression, statistical
factor models and principal components on Mardia, Kent and Bibby (1979). Statistical approaches to factor models are also treated in Seber (1984) and Johnson and
Wichern (2002).
--- page 130 ---

114
3. Multivariate Models
Table 3.7.
The ﬁrst two lines give estimates of the transpose of B for a factor model ﬁtted
to 10 Dow Jones 30 stocks, where the factors are constructed from the ﬁrst two sample
principal components. The third row gives r2 values for the univariate regression model for
each individual time series. The next 10 lines give the correlation matrix implied by the
factor model. The ﬁnal 10 lines show the estimated correlation matrix of the residuals from
the regression model, with entries less than 0.1 in absolute value omitted. See Example 3.38
for full details.
MO
KO
EK
HWP
INTC
MSFT
IBM
MCD
WMT
DIS
ˆB′
0.20
0.19
0.16
0.45
0.51
0.44
0.32
0.18
0.24
0.22
0.39
0.34
0.23 −0.26 −0.45
−0.10
−0.07
0.31
0.39
0.37
r2
0.35
0.42
0.18
0.55
0.75
0.56
0.35
0.34
0.42
0.41
MO
1.00
0.39
0.25
0.17
0.13
0.25
0.20
0.35
0.38
0.38
KO
0.39
1.00
0.28
0.21
0.17
0.29
0.23
0.38
0.42
0.42
EK
0.25
0.28
1.00
0.18
0.15
0.22
0.18
0.25
0.28
0.27
HWP
0.17
0.21
0.18
1.00
0.64
0.55
0.43
0.20
0.23
0.23
INTC
0.13
0.17
0.15
0.64
1.00
0.61
0.48
0.16
0.19
0.18
MSFT
0.25
0.29
0.22
0.55
0.61
1.00
0.44
0.27
0.31
0.30
IBM
0.20
0.23
0.18
0.43
0.48
0.44
1.00
0.21
0.25
0.24
MCD
0.35
0.38
0.25
0.20
0.16
0.27
0.21
1.00
0.38
0.37
WMT
0.38
0.42
0.28
0.23
0.19
0.31
0.25
0.38
1.00
0.41
DIS
0.38
0.42
0.27
0.23
0.18
0.30
0.24
0.37
0.41
1.00
MO
1.00 −0.19 −0.15
−0.19
−0.37
−0.26
KO
−0.19
1.00 −0.15
0.11
−0.16
−0.17
EK
−0.15 −0.15
1.00
−0.15
−0.16
−0.16
HWP
1.00 −0.63
−0.37
−0.14
INTC
0.11
−0.63
1.00
−0.24
−0.31
MSFT
−0.37 −0.24
1.00
−0.22
IBM
−0.14 −0.31
−0.22
1.00
MCD
−0.19
−0.15
1.00
−0.19
−0.19
WMT −0.37 −0.16 −0.16
−0.19
1.00
−0.23
DIS
−0.26 −0.17 −0.16
−0.19
−0.23
1.00
We have simply spoken of observed and unobserved or latent factor models, but in
the econometrics literature a classiﬁcation of factor models into three types is more
common; these are macroeconomic factor models, fundamental factor models and
statistical factor models. In this categorization our observable factor model would be
a macroeconomic factor model; index returns, along with other observables such as
interest rates or inﬂation, are the kind of macroeconomic variables that are typically
used as explanatory factors in such models. On the other hand, both approaches to
calibrating a latent factor model (classical factor analysis and principal components)
would fall under the heading of statistical factor models.
The fundamental factor models, which are not described in this book, relate to
the situation where factors are unobserved, but the loading matrix B is assumed to
be known. More precisely we consider a situation where we have clear ideas of how
to group returns by geographical or industrial sector, ﬁrm size or other important
--- page 131 ---

3.4. Dimension Reduction Techniques
115
characteristics. For example, the return of a European technology company might
be expected to be explained by an unobserved factor representing the performance
of such companies, or perhaps by two unobserved factors representing European
and technology companies. Using data for many companies and regression methods
it is then possible to estimate the unobserved factors using the known classiﬁcation
information.
For a more detailed discussion of factor models see the paper by Connor (1995),
which provides a comparison of the three types of model, and the book of Campbell,
Lo and MacKinlay (1997). An excellent practical introduction to these models with
examples in S-Plus is Zivot and Wang (2003). Other accounts of factor models and
PCA in ﬁnance are found in Alexander (2001) and Tsay (2002).
--- page 132 ---

4
Financial Time Series
In this chapter we consider time series models for ﬁnancial risk-factor change data,
in particular differenced logarithmic price and exchange-rate series. We begin by
looking more systematically at the empirical properties of such data in a discussion
of so-called stylized facts.
In Section 4.2 we review essential concepts in the analysis of time series, such as
stationarity, autocorrelations and their estimation, white noise processes, andARMA
(autoregressive moving-average) processes. We then devote Section 4.3 to univariate ARCH and GARCH (generalized autoregressive conditionally heteroscedastic)
processes for capturing the important phenomenon of volatility, before showing how
such models are used in the context of quantitative risk management in Section 4.4.
A short introduction to concepts in the analysis of multivariate time series, such as
cross-correlation and multivariate white noise, is found in Section 4.5, while the
ﬁnal section presents multivariate GARCH-type models for multivariate risk-factor
change series.
Our focus on the GARCH paradigm in this chapter requires comment. As this
book goes to press these models have been with us for around two decades, and
modern econometrics and ﬁnance have continued to develop other kinds of model
for ﬁnancial return series.We think here of discrete-time stochastic volatility models,
long-memory GARCH models, continuous-time models ﬁtted to discrete data, and
models based on realized volatility calculated from high-frequency data; none of
these new developments are handled in this book.
Our emphasis on GARCH has two main motivations, the ﬁrst of these being
practical. We recall that in risk management we are typically dealing with very
large numbers of risk factors and our philosophy, expounded in Section 1.5, is that
broad-brush techniques that capture the main risk features of many time series are
more important than very detailed analyses of single series. The relatively simple
GARCH model lends itself to this approach and proves very easy to ﬁt.There are also
some multivariate extensions which build in fairly simple ways on the univariate
models and may be calibrated to a multivariate series in stages. This ease of use
contrasts with other models where even the ﬁtting of a single series presents a
challenging computational problem (e.g. estimation of a stochastic volatility model
via ﬁltering or Gibbs sampling), and multivariate extensions have not been widely
considered. Related to this is the likelihood that an average ﬁnancial enterprise will
collect, at best, daily data on its complete set of risk factors for the purposes of risk
--- page 133 ---

4.1. Empirical Analyses of Financial Time Series
117
management, and this will rule out some more sophisticated models that require
higher-frequency data.
Our second reason for concentrating on ARCH and GARCH models is didactic.
These models for volatile return series have a status akin toARMA models in classical time series; they belong, in our opinion, to the body of standard methodology to
which a student of the subject should be exposed. A quantitative risk manager who
understands GARCH has a good basis for understanding more complex models and
a good framework for talking about volatility in a rational way. He/she may also
appreciate more clearly the role of more ad hoc volatility estimation methods such
as the exponentially weighted moving-average (EWMA) procedure.
4.1
Empirical Analyses of Financial Time Series
4.1.1
Stylized Facts
The stylized facts of ﬁnancial time series are a collection of empirical observations,
and inferences drawn from these observations, that seem to apply to the majority of
daily series of risk-factor changes, such as log-returns on equities, indexes, exchange
rates and commodity prices; these observations are now so entrenched in econometric experience that they have been elevated to the status of facts. They often continue
to hold when we go to longer time intervals, such as weekly or monthly returns, or
to shorter time intervals, such as intra-daily returns. A version of the stylized facts
is as follows.
(1) Return series are not iid although they show little serial correlation.
(2) Series of absolute or squared returns show profound serial correlation.
(3) Conditional expected returns are close to zero.
(4) Volatility appears to vary over time.
(5) Return series are leptokurtic or heavy-tailed.
(6) Extreme returns appear in clusters.
In the following consider a sample of daily return data X1, . . . , Xn and assume that
these have been formed by logarithmic differencing of a price, index or exchangerate series (St)t=0,1,...,n, so that Xt = ln(St/St−1), t = 1, . . . , n.
Volatility clustering.
Evidence for the ﬁrst two stylized facts is collected in Figures 4.1 and 4.2. Figure 4.1(a) shows 2608 daily log-returns for the DAX index
spanning a decade from 2 January 1985 to 30 December 1994, a period including both the stock-market crash of 1987 and the reuniﬁcation of Germany. Parts (b)
and (c) show series of simulated iid data from a normal and Student t model, respectively; in both cases the model parameters have been set by ﬁtting the model to the
real return data using the method of maximum likelihood under the iid assumption.
In the normal case this means that we simply simulate iid data with distribution
N(µ, σ 2), where µ = ¯X = n−1 n
i=1 Xi and σ 2 = n−1 n
i=1(Xi −¯X)2. In the t
case the likelihood has been maximized numerically and the estimated degrees of
freedom parameter is ν = 3.8.
--- page 134 ---

118
4. Financial Time Series
−0.10
−0.05
0
0.05
02.01.85
02.01.86
02.01.87
02.01.88
02.01.89
02.01.90
02.01.91
02.01.92
02.01.93
02.01.94
−0.10
−0.05
0
0.05
Time
0
500
1000
1500
2000
2500
−0.10
−0.05
0
0.05
(a)
(b)
(c)
Figure 4.1.
(a) Log-returns for the DAX index from 2 January 1985 to 30 December 1994
compared with simulated iid data from (b) a normal and (c) a t distribution, where the
parameters have been determined by ﬁtting the models to the DAX data.
The simulated normal data are clearly very different from the DAX return data
and do not show the same range of extreme values, which does not surprise us given
our observations on the inadequacy of the Gaussian model in Chapter 3. While the
Student t model can generate comparable extreme values to the real data, more
careful observation reveals that the DAX returns exhibit a phenomenon known as
volatility clustering, which is not present in the simulated series.Volatility clustering
is the tendency for extreme returns to be followed by other extreme returns, although
not necessarily with the same sign. In the DAX data we see periods such as the stockmarket crash of October 1987 or the political uncertainty in the period between late
1989 and German reuniﬁcation in 1990 which are marked by large positive and
negative moves.
In Figure 4.2 the correlograms of the raw data and the absolute data for all three
datasets are shown. The correlogram is a graphical display for estimates of serial
