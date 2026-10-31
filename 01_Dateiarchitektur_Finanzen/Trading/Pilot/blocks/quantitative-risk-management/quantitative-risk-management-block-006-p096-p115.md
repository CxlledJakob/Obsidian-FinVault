# Quantitative Risk Management_ Concepts, Techniques, and -- Alexander J_ McNeil, Rüdiger Frey, Paul Embrechts -- Princeton series in finance, -- isbn13 9780691122557 -- 478a0059673fecd0c76229cd3d8884e7 -- Anna’s Arc.pdf — pages 96–115

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
--- page 97 ---

3.2. Normal Mixture Distributions
81
3.2.4
Fitting Generalized Hyperbolic Distributions to Data
While univariate generalized hyperbolic models have been ﬁtted to return data in
many empirical studies, there has been relatively little applied work with the multivariate distributions. However, normal mixture distributions of the kind we have
described may be ﬁtted with algorithms of the EM (expectation–maximization)
type. In this section we present an algorithm for that purpose and sketch the ideas
behind it. Similar methods have been developed independently by other authors and
references may be found in Notes and Comments. Readers who are not particularly
interested in getting an idea of how the estimation works may skip this section, while
noting the existence of Algorithm 3.14.
Assume we have iid data X1, . . . , Xn and wish to ﬁt the multivariate generalized hyperbolic, or one of its special cases. Summarizing the parameters by
θ = (λ, χ, ψ, µ, Σ, γ )′, the problem is to maximize
ln L(θ; X1, . . . , Xn) =
n

i=1
ln fX(Xi; θ),
(3.33)
where fX(x; θ) denotes the generalized hyperbolic density in (3.30).
This problem is not particularly easy at ﬁrst sight due to the number of parameters
and the necessity of maximizing over covariance matrices Σ. However, if we were
able to “observe” the latent mixing variables W1, . . . , Wn coming from the mixture
representation in (3.25), it would be much easier. Since the joint density of any pair
Xi and Wi is given by
fX,W(x, w; θ) = fX|W(x | w; µ, Σ, γ )hW(w; λ, χ, ψ),
(3.34)
we could construct the likelihood
ln ˜L(θ; X1, . . . , Xn, W1, . . . , Wn)
=
n

i=1
ln fX|W(Xi | Wi; µ, Σ, γ ) +
n

i=1
ln hW(Wi; λ, χ, ψ),
(3.35)
where the two terms could be maximized separately with respect to the parameters
they involve. The apparently more problematic parameters of Σ and γ are in the
ﬁrst term of the likelihood and estimates are relatively easy to derive due to the
Gaussian form of this term.
To overcome the latency of the Wi data the EM algorithm is used. This is an
iterative procedure consisting of an E-step, or expectation step (where essentially Wi
is replaced by an estimate given the observed data and current parameter estimates),
and an M-step, or maximization step (where the parameter estimates are updated).
Suppose at the beginning of step k we have parameter estimates θ[k]. We proceed
as follows.
E-step. We calculate the conditional expectation of the so-called augmented likelihood (3.35) given the data X1, . . . , Xn using the parameter values θ[k]. This
results in the objective function
Q(θ; θ[k]) = E(ln ˜L(θ; X1, . . . , Xn, W1, . . . , Wn) | X1, . . . , Xn; θ[k]).
--- page 98 ---

82
3. Multivariate Models
M-step. We maximize the objective function with respect to θ to obtain the next
set of estimates θ[k+1].
Alternating between these steps, the EM algorithm produces improved parameter
estimates at each step (in the sense that the value of the original likelihood (3.33) is
continually increased) and we converge to the maximum likelihood (ML) estimates.
In practice, performing the E-step amounts to replacing any functions g(Wi) of the
latent mixing variables which arise in (3.35) by the quantities E(g(Wi) | Xi; θ[k]).
To calculate these quantities we can observe that the conditional density of Wi given
Xi satisﬁes fW|X(w | x; θ) ∝fW,X(w, x; θ), up to some constant of proportionality. Thus it may be deduced from (3.34) that
Wi | Xi ∼N−(λ −1
2d, (Xi −µ)′ ˜Σ−1(Xi −µ) + χ, ψ + γ ′Σ−1γ ).
(3.36)
If we write out the likelihood (3.35) using (3.26) for the ﬁrst term and the GIG
density (A.8) for the second term, we ﬁnd that the functions g(Wi) arising in (3.35)
are g1(w) = w, g2(w) = 1/w and g3(w) = ln(w). The conditional expectation of
these functions in model (3.36) may be evaluated using information about the GIG
distribution in Section A.2.5; note that E(ln(Wi) | Xi; θ[k]) involves derivatives of
a Bessel function with respect to order and must be approximated numerically. We
will introduce the notation
δ[·]
i
= E(W −1
i
| Xi; θ[·]),
η[·]
i
= E(Wi | Xi; θ[·]),
ξ[·]
i
= E(ln(Wi) | Xi; θ[·]),
(3.37)
which allows us to describe the basic EM scheme as well as a variant below.
In the M-step there are two terms to maximize, coming from the two terms
in (3.35); we write these as Q1(µ, Σ, γ ; θ[k]) and Q2(λ, χ, ψ; θ[k]). To address the
identiﬁability issue mentioned in Section 3.2.3 we constrain the determinant of Σ
to be some ﬁxed value (in practice we take the determinant of the sample covariance
matrix S) in the maximization of Q1. The maximizing values of µ, Σ and γ may
then be derived analytically by calculating partial derivatives and setting these equal
to zero; the resulting formulas are embedded in Algorithm 3.14 below (see steps (3)
and (4)). The maximization of Q2(λ, χ, ψ; θ[k]) with respect to the parameters of
the mixing distribution is performed numerically; the function Q2(λ, χ, ψ; θ[·]) is
(λ −1)
n

i=1
ξ[·]
i
−1
2χ
n

i=1
δ[·]
i −1
2ψ
n

i=1
η[·]
i
−1
2nλ ln(χ) + 1
2nλ ln(ψ) −n ln(2Kλ(

χψ)).
(3.38)
This would complete one iteration of a standard EM algorithm. However, there are
a couple of variants on the basic scheme; both involve modiﬁcation of the ﬁnal step
described above, namely the maximization of Q2.
Assuming the parameters µ, Σ and γ have been updated ﬁrst in iteration k, we
deﬁne
θ[k,2] = (λ[k], χ[k], ψ[k], µ[k+1], Σ[k+1], γ [k+1])′,
--- page 99 ---

3.2. Normal Mixture Distributions
83
recalculate the weights δ[k,2]
i
, η[k,2]
i
and ξ[k,2]
i
in (3.37), and then maximize the
function Q2(λ, η, ξ; θ[k,2]) in (3.38). This results in a so-called MCECM algorithm
(multi-cycle, expectation, conditional maximization), which is the one we present
below.
Alternatively, instead of maximizing Q2 we may maximize the original likelihood (3.33) with respect to λ, χ and ψ with the other parameters held ﬁxed at the
values µ[k], Σ[k] and γ [k]; this results in an ECME algorithm.
Algorithm 3.14 (EM estimation of generalized hyperbolic distribution).
(1) Set iteration count k = 1 and select starting values for θ[1]. In particular,
reasonable starting values for µ, γ and Σ, respectively, are the sample mean,
the zero vector and the sample covariance matrix S.
(2) Calculate weights δ[k]
i
and η[k]
i
using (3.37), (3.36) and (A.9). Average the
weights to get
¯δ[k] = n−1
n

i=1
δ[k]
i
and
¯η[k] = n−1
n

i=1
η[k]
i .
(3) For a symmetric model set γ [k+1] = 0. Otherwise set
γ [k+1] = n−1 n
i=1 δ[k]
i ( ¯X −Xi)
¯δ[k] ¯η[k] −1
.
(4) Update estimates of the location vector and dispersion matrix by
µ[k+1] = n−1 n
i=1 δ[k]
i Xi −γ [k+1]
¯δ[k]
,
Ψ = 1
n
n

i=1
δ[k]
i (Xi −µ[k+1])(Xi −µ[k+1])′ −¯η[k]γ [k+1]γ [k+1]′,
Σ[k+1] = |S|1/dΨ
|Ψ |1/d .
(5) Set
θ[k,2] = (λ[k], χ[k], ψ[k], µ[k+1], Σ[k+1], γ [k+1])′.
Calculate weights δ[k,2]
i
, η[k,2]
i
and ξ[k,2]
i
using (3.37), (3.36) and information
in Section A.2.5.
(6) Maximize Q2(λ, χ, ψ; θ[k,2]) in (3.38) with respect to λ, χ and ψ to complete
the calculation of θ[k,2]. Increment iteration count k →k+1 and go to step (2).
This algorithm may be easily adapted to ﬁt special cases of the generalized hyperbolic distribution. This involves holding certain parameters ﬁxed throughout and
maximizing with respect to the remaining parameters: for the hyperbolic distribution we set λ = 1; for the NIG distribution λ = −1
2; for the t distribution ψ = 0; for
the VG distribution χ = 0. In the case of t and VG in step (6) we have to work with
the function Q2 that results from assuming an inverse gamma or gamma density
for hW.
--- page 100 ---

84
3. Multivariate Models
3.2.5
Empirical Examples
In this section we ﬁt the multivariate generalized hyperbolic (GH) distribution to real
data and examine which of the subclasses—such as t, hyperbolic or NIG—are most
useful; we also explore whether the general mean-variance mixture models can be
replaced by (elliptically symmetric) variance mixtures. Our ﬁrst example prepares
the ground for multivariate examples by looking brieﬂy at univariate models.
Example 3.15 (univariate stock returns). In the literature the NIG, hyperbolic
and t models have been particularly popular special cases. We ﬁt symmetric and
asymmetric cases of these distributions to the data used in Example 3.3, restricting
attention to daily and weekly returns, where the data are more plentiful (n = 2020
and n = 468, respectively). Models are ﬁtted using maximum likelihood under
the simplifying assumption that returns form iid samples; a simple quasi-Newton
method provides a viable alternative to the EM algorithm in the univariate case.
In the upper two panels of Table 3.3 we show results for symmetric models. The
t, NIG and hyperbolic models may be compared directly using the log-likelihood
at the maximum, since all have the same number of parameters: for daily data we
ﬁnd that eight out of 10 stocks prefer the t distribution to the hyperbolic and NIG
distributions; for weekly returns the t distribution is favoured in six out of 10 cases.
Overall, the second best model appears to be the NIG distribution. The mixture
models ﬁt much better than the Gaussian model in all cases, and it may be veriﬁed
easily using the Akaike information criterion (AIC) that they are preferred to the
Gaussian model in a formal comparison (see Section A.3.6 for more on the AIC).
For the asymmetric models, we only show cases where at least one of the asymmetric t, NIG or hyperbolic models offered a signiﬁcant improvement (p < 0.05)
on the corresponding symmetric model according to a likelihood ratio test. This
occurred for weekly returns on Citigroup (C) and Intel (INTC) but for no daily
returns. For Citigroup the p-values of the tests were, respectively, 0.06, 0.04 and
0.04 for the t, NIG and hyperbolic cases; for Intel the p-values were 0.01 in all
cases, indicating quite strong asymmetry.
In the case of Intel we have superimposed the densities of various ﬁtted asymmetric distributions on a histogram of the data in Figure 3.4. A plot of the log densities
shown alongside reveals the differences between the distributions in the tail area.
The left tail (corresponding to losses) appears to be heavier for these data and the
best-ﬁtting distribution according to the likelihood comparison is the asymmetric
t distribution.
Example 3.16 (multivariate stock returns). We ﬁtted multivariate models to the
full 10-dimensional dataset of log-returns used in the previous example. The resulting values of the maximized log-likelihood are shown in Table 3.4 along with pvalues for a likelihood ratio test of all special cases against the (asymmetric) generalized hyperbolic (GH) model. The number of parameters in each model is also given;
note that the general d-dimensional GH model has 1
2d(d + 1) dispersion parameters, d location parameters, d skewness parameters and three parameters coming
--- page 101 ---

3.2. Normal Mixture Distributions
85
Table 3.3.
Comparison of univariate models in the generalized hyperbolic family, showing estimates of selected parameters and the value of the log-likelihood at the maximum;
bold numbers indicate the models that give the largest values of the log-likelihood. See
Example 3.15 for commentary.
Gauss
t model
NIG model
Hyperbolic model









Stock
ln L
ν
ln L
√χψ
ln L
√χψ
ln L
Daily returns: symmetric models
AXP
4945.7
5.8
5001.8
1.6
5002.4
1.3
5002.1
EK
5112.9
3.8
5396.2
0.8
5382.5
0.6
5366.0
BA
5054.9
3.8
5233.5
0.8
5229.1
0.5
5221.2
C
4746.6
6.3
4809.5
1.9
4806.8
1.7
4805.0
KO
5319.6
5.1
5411.0
1.4
5407.3
1.3
5403.3
MSFT
4724.3
5.8
4814.6
1.6
4809.5
1.5
4806.4
HWP
4480.1
4.5
4588.8
1.1
4587.2
0.9
4583.4
INTC
4392.3
5.4
4492.2
1.5
4486.7
1.4
4482.4
JPM
4898.3
5.1
4967.8
1.3
4969.5
0.9
4969.7
DIS
5047.2
4.4
5188.3
1
5183.8
0.8
5177.6
Weekly returns: symmetric models
AXP
719.9
8.8
724.2
3.0
724.3
2.8
724.3
EK
718.7
3.6
765.6
0.7
764.0
0.5
761.3
BA
732.4
4.4
759.2
1.0
758.3
0.8
757.2
C
656.0
5.7
669.6
1.6
669.3
1.3
669
KO
757.1
6.0
765.7
1.7
766.2
1.3
766.3
MSFT
671.5
6.3
683.9
1.9
683.2
1.8
682.9
HWP
627.1
6.0
637.3
1.8
637.3
1.5
637.1
INTC
595.8
5.2
611.0
1.5
610.6
1.3
610
JPM
681.7
5.9
693.0
1.7
692.9
1.5
692.6
DIS
734.1
6.4
742.7
1.9
742.8
1.7
742.7
Weekly returns: asymmetric models
C
NA
6.1
671.4
1.7
671.3
1.3
671.2
INTC
NA
6.3
614.2
1.8
613.9
1.7
613.3
from the GIG mixing distribution, but is subject to one identiﬁability constraint; this
gives 1
2(d(d + 5) + 4) free parameters.
For the daily data the best of the special cases is the skewed t distribution, which
gives a value for the maximized likelihood that cannot be discernibly improved
by the more general model with its additional parameter. All other non-elliptically
symmetric submodels are rejected in a likelihood ratio test. Note, however, that the
elliptically symmetric t distribution cannot be rejected when compared with the
most general model, so that this seems to offer a simple parsimonious model for
these data (the estimated degree of freedom is 6.0).
For the weekly data the best special case is the NIG distribution, followed closely
by the skewed t; the hyperbolic and variance gamma are rejected. The best elliptically symmetric special case seems to be the t distribution (the estimated degree of
freedom being, this time, 6.2).
--- page 102 ---

86
3. Multivariate Models
−0.2
0
0.2
0
6
x
f (x)
x
f (x) (logarithmic)
−0.2
0
0.2
t
NIG
hyperbolic
Gaussian
8
4
2
101
100
10−1
10−5
10−4
10−3
10−2
Figure 3.4.
Models for weekly returns on Intel (INTC).
Example 3.17 (multivariate exchange-rate returns). We ﬁtted the same multivariate models to a four-dimensional dataset of exchange-rate log-returns, these
being GB pound, euro, Japanese yen and Swiss franc against the US dollar for
the period January 2000 to the end of March 2004 (1067 daily returns and 222
weekly returns). The resulting values of the maximized log-likelihood are shown in
Table 3.5.
For the daily data the best of the special cases (in general and also if we restrict
ourselves to symmetric models) is the NIG distribution, followed by the hyperbolic,
t and variance-gamma (VG) distributions in that order. In a likelihood ratio test of
the special cases against the general GH distribution only the VG model is rejected
at the 5% level; the skewed t model is rejected at the 10% level. When tested against
the full model, certain elliptical models could not be rejected, the best of these being
the NIG.
For the weekly data the best special case is the t distribution, followed by the
NIG, hyperbolic and variance gamma; none of the special cases can be rejected in a
test at the 5% level although the VG model is rejected at the 10% level. Among the
elliptically symmetric distributions the Gauss distribution is clearly rejected, and
the VG is again rejected at the 10% level, but otherwise the elliptical special cases
are accepted; the best of these seems to be the t distribution, which has an estimated
degrees-of-freedom parameter of 5.99.
--- page 103 ---

3.2. Normal Mixture Distributions
87
Table 3.4.
A comparison of models in the GH family for 10-dimensional stock-return data.
For each model, the table shows the value of the log-likelihood at the maximum (ln L), the
numbers of parameters (# par.) and the p-value for a likelihood ratio test against the general
GH model. The log-likelihood values for the general model, the best special case and the best
elliptically symmetric special case are in bold type. See Example 3.16 for details.
GH
NIG
Hyperbolic
t
VG
Gauss
Daily returns: asymmetric models
ln L
52 174.62
52 141.45
52 111.65
52 174.62
52 063.44
# par.
77
76
76
76
76
p-value
0.00
0.00
1.00
0.00
Daily returns: symmetric models
ln L
52 170.14
52 136.55
52 106.34
52 170.14
52 057.38
50 805.28
# par.
67
66
66
66
66
65
p-value
0.54
0.00
0.00
0.63
0.00
0.00
Weekly returns: asymmetric models
ln L
7 639.32
7 638.59
7 636.49
7 638.56
7 631.33
p-value
0.23
0.02
0.22
0.00
Weekly returns: symmetric models
ln L
7 633.65
7 632.68
7 630.44
7 633.11
7 625.4
7 433.77
p-value
0.33
0.27
0.09
0.33
0.00
0.00
Table 3.5.
A comparison of models in the GH family for four-dimensional exchange-rate
return data. For each model, the table shows the value of the log-likelihood at the maximum
(ln L), the numbers of parameters (# par.) and the p-value for a likelihood ratio test against
the general GH model. The log-likelihood values for the general model, the best special case
and the best elliptically symmetric special case are in bold type. See Example 3.17 for details.
GH
NIG
Hyperbolic
t
VG
Gauss
Daily returns: asymmetric models
ln L
17 306.44
17 306.43
17 305.61
17 304.97
17 302.5
# par.
20
19
19
19
19
p-value
0.85
0.20
0.09
0.00
Daily returns: symmetric models
ln L
17 303.10
17 303.06
17 302.15
17 301.85
17 299.15
17 144.38
# par.
16
15
15
15
15
14
p-value
0.15
0.24
0.13
0.10
0.01
0.00
Weekly returns: asymmetric models
ln L
2 890.65
2 889.90
2 889.65
2 890.65
2 888.98
p-value
0.22
0.16
1.00
0.07
Weekly returns: symmetric models
ln L
2 887.52
2 886.74
2 886.48
2 887.52
2 885.86
2 872.36
p-value
0.18
0.17
0.14
0.28
0.09
0.00
--- page 104 ---

88
3. Multivariate Models
Notes and Comments
Important early papers on multivariate normal mixtures are Kelker (1970) and Cambanis, Huang and Simons (1981). See also Bingham and Kiesel (2002), which
contains an overview of the connections between normal mixture, elliptical and
hyperbolic models, and discusses their role in ﬁnancial modelling. Fang, Kotz and
Ng (1987) discuss the symmetric normal mixture models as special cases in their
account of the more general family of spherical and elliptical distributions.
The generalized hyperbolic distributions (univariate and multivariate) were introduced in Barndorff-Nielsen (1978) and further explored in Barndorff-Nielsen and
Blæsild (1981). Useful references on the multivariate distribution are Blæsild (1981)
and Blæsild and Jensen (1981). Generalized hyperbolic distributions (particularly
in the univariate case) have been popularized as models for ﬁnancial returns in
recent papers by Eberlein and Keller (1995) and Eberlein, Keller and Prause (1998)
(see also Bibby and Sørensen 2003). The PhD thesis of Prause (1999) is also a
compendium of useful information in this context.
The reasons for their popularity in ﬁnancial applications are both empirical and
theoretical: they appear to provide a good ﬁt to ﬁnancial return data (again mostly in
univariate investigations); they are consistent with continuous-time models, where
logarithmic asset prices follow univariate or multivariate L´evy processes (thus
generalizing the Black–Scholes model, where logarithmic prices follow Brownian
motion) (see Eberlein and Keller 1995).
For the NIG special case see Barndorff-Nielsen (1997), who discusses both univariate and multivariate cases and argues that the NIG is slightly superior to the
hyperbolic as a univariate model for return data, a claim that our analyses support
for stock-return data. Kotz, Kozubowski and Podg´orski (2001) is a useful reference
for the variance-gamma special case; the distribution appears here under the name
generalized Laplace distribution and a (univariate or multivariate) L´evy process with
variance-gamma-distributed increments is called a Laplace motion. The univariate
Laplace motion is essentially the model proposed by Madan and Seneta (1990),
who derived it as a Brownian motion under a stochastic time change and referred
to it as the variance-gamma model (see also Madan, Carr and Chang 1998). The
multivariate t distribution is discussed in Kotz and Nadarajah (2004); the asymmetric or skewed t distribution presented in this chapter is also discussed in Bibby and
Sørensen (2003). For alternative skewed extensions of the multivariate t, see Kotz
and Nadarajah (2004) and Genton (2004).
EM algorithms for the multivariate generalized hyperbolic distribution have been
independently proposed by Protassov (2004) and Barndorff-Nielsen and Shephard (2005). Our approach is based on EM-type algorithms for ﬁtting the multivariate t distribution with unknown degrees of freedom. A good starter reference
on this subject is Liu and Rubin (1995), where the use of the MCECM algorithm
of Meng and Rubin (1993) and the ECME algorithm proposed in Liu and Rubin
(1994) is discussed. Further reﬁnements of these algorithms are discussed in Liu
(1997) and Meng and van Dyk (1997).
--- page 105 ---

3.3. Spherical and Elliptical Distributions
89
3.3
Spherical and Elliptical Distributions
In the previous section we observed that elliptical distributions—in particular the
multivariate t and symmetric multivariate NIG—provided far superior models to
the multivariate normal for daily and weekly US stock-return data. The more general asymmetric versions of these distributions did not seem to offer much of an
improvement on the symmetric models. While this was a single example, other
investigations suggest that multivariate return data for groups of returns of a similar
type often look roughly elliptical.
In this section we look more closely at the theory of elliptical distributions. To do
this we begin with the special case of spherical distributions.
3.3.1
Spherical Distributions
The spherical family constitutes a large class of distributions for random vectors
with uncorrelated components and identical, symmetric marginal distributions. It is
important to note that within this class, Nd(0, Id) is the only model for a vector of
mutually independent components. Many of the properties of elliptical distributions
can best be understood by beginning with spherical distributions.
Deﬁnition 3.18. A random vector X = (X1, . . . , Xd)′ has a spherical distribution
if, for every orthogonal map U ∈Rd×d (i.e. maps satisfying UU′ = U′U = Id),
UX d= X.
Thussphericalrandomvectorsaredistributionallyinvariantunderrotations.There
are a number of different ways of deﬁning distributions with this property, as we
demonstrate below.
Theorem 3.19. The following are equivalent.
(1) X is spherical.
(2) There exists a function ψ of a scalar variable such that, for all t ∈Rd,
φX(t) = E(eit′X) = ψ(t′t) = ψ(t2
1 + · · · + t2
d).
(3.39)
(3) For every a ∈Rd,
a′X d= ∥a∥X1,
(3.40)
where ∥a∥2 = a′a = a2
1 + · · · + a2
d.
Proof. (1) ⇒(2). If X is spherical, then for any orthogonal matrix U we have
φX(t) = φUX(t) = E(eit′UX) = φX(U′t).
This can only be true if φX(t) only depends on the length of t, i.e. if φX(t) = ψ(t′t)
for some function ψ of a non-negative scalar variable.
--- page 106 ---

90
3. Multivariate Models
(2) ⇒(3). First observe that φX1(t) = E(eitX1) = φX(te1) = ψ(t2), where e1
denotes the ﬁrst unit vector in Rd. It follows that for any a ∈Rd,
φa′X(t) = φX(ta) = ψ(t2a′a) = ψ(t2∥a∥2) = φX1(t∥a∥) = φ∥a∥X1(t).
(3) ⇒(1). For any orthogonal matrix U we have
φUX(t) = E(ei(U′t)′X) = E(ei∥U′t∥X1) = E(ei∥t∥X1) = E(eit′X) = φX(t).
Part (2) of Theorem 3.19 shows that the characteristic function of a spherically
distributed random vector is fully described by a function ψ of a scalar variable. For
this reason ψ is known as the characteristic generator of the spherical distribution
and the notation X ∼Sd(ψ) is used. Part (3) of Theorem 3.19 shows that linear
combinations of spherical random vectors always have a distribution of the same
type, so that they have the same distribution up to changes of location and scale
(see Section A.1.1). This important property will be used in Chapter 6 to prove the
subadditivity of Value-at-Risk for linear portfolios of elliptically distributed risk
factors. We now give examples of spherical distributions.
Example 3.20 (multivariate normal). A random vector X with the standard uncorrelated normal distribution Nd(0, Id) is clearly spherical. The characteristic function
is
φX(t) = E(exp(it′X)) = exp(−1
2t′t),
so that, using part (2) of Theorem 3.19, X ∼Sd(ψ) with characteristic generator
ψ(t) = exp(−1
2t).
Example 3.21 (normal variance mixtures). A random vector X with a standardized, uncorrelated normal variance mixture distribution Md(0, Id, ˆH) also has a
spherical distribution. Using (3.21), we see that φX(t) = ˆH( 1
2t′t), which obviously satisﬁes (3.39), and the characteristic generator of the spherical distribution is
related to the Laplace–Stieltjes transform of the mixture distribution function of W
by ψ(t) = ˆH( 1
2t). Thus X ∼Md(0, Id, ˆH(·)) and X ∼Sd( ˆH( 1
2·)) are two ways
of writing the same mixture distribution.
A further, extremely important way of characterizing spherical distributions is
given by the following result.
Theorem 3.22. X has a spherical distribution if and only if it has the stochastic
representation
X d= RS,
(3.41)
where S is uniformly distributed on the unit sphere Sd−1 = {s ∈Rd : s′s = 1} and
R ⩾0 is a radial rv, independent of S.
--- page 107 ---

3.3. Spherical and Elliptical Distributions
91
Proof. First we prove that if S is uniformly distributed on the unit sphere and R ⩾0
is an independent scalar variable, then RS has a spherical distribution. This is seen
by considering the characteristic function
φRS(t) = E(eiRt′S) = E(E(eiRt′S | R)).
Since S is itself spherically distributed, its characteristic function has a characteristic
generator, which is usually given the special notation Ωd.Thus, byTheorem 3.19 (2),
we have that
φRS(t) = E(Ωd(R2t′t)) =

Ωd(r2t′t) dF(r),
(3.42)
where F is the df of R. Since this is a function of t′t, it follows, again from Theorem 3.19 (2), that RS has a spherical distribution.
We now prove that if the random vector X is spherical, then it has the representation (3.41). For any arbitrary s ∈Sd−1 the characteristic generator ψ of X must
satisfy ψ(t′t) = φX(t) = φX(∥t∥s). It follows that, if we introduce a random vector
S that is uniformly distributed on the sphere Sd−1, we can write
ψ(t′t) =

Sd−1 φX(∥t∥s) dFS(s) =

Sd−1 E(ei∥t∥s′X) dFS(s).
Interchanging the order of integration and using the Ωd notation for the characteristic
generator of S we have
ψ(t′t) = E(Ωd(∥t∥2∥X∥2)) =

Ωd(t′tr2) dF∥X∥(r),
(3.43)
where F∥X∥is the df of ∥X∥. By comparison with (3.42) we see that (3.43) is the
characteristic function of RS, where R is an rv with df F∥X∥that is independent
of S.
We often exclude from consideration distributions which place point mass at
the origin; that is we consider spherical rvs X in the subclass S+
d (ψ) for which
P(X = 0) = 0.A particularly useful corollary ofTheorem 3.22 is then the following
result, which is used in Section 3.3.5 to devise tests for spherical and elliptical
symmetry.
Corollary 3.23. Suppose X d= RS ∼S+
d (ψ). Then

∥X∥, X
∥X∥

d= (R, S).
(3.44)
Proof. Let f1(x) = ∥x∥and f2(x) = x/∥x∥. It follows from (3.41) that

∥X∥, X
∥X∥

= (f1(X), f2(X)) d= (f1(RS), f2(RS)) = (R, S).
--- page 108 ---

92
3. Multivariate Models
Example 3.24 (working with R and S). Suppose X ∼Nd(0, Id). Since X′X ∼
χ2
d , a chi-squared distribution with d degrees of freedom, it follows from (3.44) that
R2 ∼χ2
d .
We can use this fact to calculate E(S) and cov(S), the ﬁrst two moments of a
uniform distribution on the unit sphere. We have that
0 = E(X) = E(R)E(S) ⇒E(S) = 0,
Id = cov(X) = E(R2) cov(S) ⇒cov(S) = Id/d,
(3.45)
since E(R2) = d when R2 ∼χ2
d .
Now suppose that X has a spherical normal variance mixture distribution X ∼
Md(0, Id, ˆH) and we wish to calculate the distribution of R2 d= X′X in this case.
Since X d=
√
WY, where Y ∼Nd(0, Id) and W is independent of Y, it follows that
R2 d= W ˜R2, where ˜R2 ∼χ2
d and W and ˜R are independent. If we can calculate the
distribution of the product of W and an independent chi-squared variate, then we
have the distribution of R2.
For a concrete example suppose that X ∼td(ν, 0, Id). For a multivariate t distribution we know from Example 3.7 that W ∼Ig( 1
2ν, 1
2ν), which means that
ν/W ∼χ2
ν . Using the fact that the ratio of independent chi-squared distributions divided by their degrees of freedom is F-distributed, it may be calculated
that R2/d ∼F(d, ν), the F distribution on d and ν degrees of freedom (see SectionA.2.3). Since an F(d, ν) distribution has mean ν/(ν −2), it follows from (3.45)
that
cov(X) = E(cov(RS | R)) = E(R2Id/d) = (ν/(ν −2))Id.
The normal mixtures with µ = 0 and Σ = Id represent an easily understood
subgroup of the spherical distributions. There are other spherical distributions which
cannot be represented as normal variance mixtures; an example is the distribution
of the uniform vector S on Sd−1 itself. However, the normal mixtures have a special
role in the spherical world, as summarized by the following theorem.
Theorem 3.25. Denote by Ψ∞the set of characteristic generators that generate a
d-dimensional spherical distribution for arbitrary d ⩾1. Then X ∼Sd(ψ) with
ψ ∈Ψ∞if and only if X d=
√
WZ, where Z ∼Nd(0, Id) is independent of W ⩾0.
Proof. This is proved in Fang, Kotz and Ng (1987, pp. 48–51).
Thus, the characteristic generators of normal mixtures generate spherical distributions in arbitrary dimensions, while other spherical generators may only be used
in certain dimensions. A concrete example is given by the uniform distribution on
the unit sphere. Let Ωd denote the characteristic generator of the uniform vector
S = (S1, . . . , Sd)′ on Sd−1. It can be shown that Ωd((t1, . . . , td+1)′(t1, . . . , td+1))
is not the characteristic function of a spherical distribution in Rd+1 (for more details
see Fang, Kotz and Ng (1987, pp. 70–72)).
--- page 109 ---

3.3. Spherical and Elliptical Distributions
93
If a spherical distribution has a density f , then, by using the inversion formula
f (x) =
1
(2π)d
 ∞
−∞
· · ·
 ∞
−∞
e−it′xφX(t) dt1 · · · dtd,
it is easily inferred from Theorem 3.19 that f (x) = f (Ux) for any orthogonal
matrix U, so that the density must be of the form
f (x) = g(x′x) = g(x2
1 + · · · + x2
d)
(3.46)
for some function g of a scalar variable, which is referred to as the density generator.
Clearly, the joint density is constant on hyperspheres {x : x2
1 +· · ·+x2
d = c} in Rd.
To give a single example, the density generator of the multivariate t (i.e. the model
X ∼td(ν, 0, Id) of Example 3.7) is
g(x) = Γ ( 1
2(ν + d))
Γ ( 1
2ν)(πν)d/2

1 + x
ν
−(ν+d)/2
.
3.3.2
Elliptical Distributions
Deﬁnition 3.26. X has an elliptical distribution if
X d= µ + AY,
where Y ∼Sk(ψ) and A ∈Rd×k and µ ∈Rd are a matrix and vector of constants,
respectively.
In other words, elliptical distributions are obtained by multivariate afﬁne transformations of spherical distributions. Since the characteristic function is
φX(t) = E(eit′X) = E(eit′(µ+AY)) = eit′µE(ei(A′t)′Y ) = eit′µψ(t′Σt),
where Σ = AA′, we denote the elliptical distributions by
X ∼Ed(µ, Σ, ψ),
and refer to µ as the location vector, Σ as the dispersion matrix and ψ as the
characteristic generator of the distribution.
Remark 3.27. Knowledge of X does not uniquely determine its elliptical representation Ed(µ, Σ, ψ). Although µ is uniquely determined, Σ and ψ are only
determined up to a positive constant. For example, the multivariate normal distribution Nd(µ, Σ) can be written as Ed(µ, Σ, ψ(·)) or Ed(µ, cΣ, ψ(·/c)) for
ψ(u) = exp(−1
2u) and any c > 0. Provided that variances are ﬁnite, then an elliptical distribution is fully speciﬁed by its mean vector, covariance matrix and characteristic generator and it is possible to ﬁnd an elliptical representation Ed(µ, Σ, ψ)
such that Σ is the covariance matrix of X, although this is not always the standard
representation of the distribution.
We now give an alternative stochastic representation for the elliptical distributions
that follows directly from Deﬁnition 3.26 and Theorem 3.22.
--- page 110 ---

94
3. Multivariate Models
Proposition 3.28. X ∼Ed(µ, Σ, ψ) if and only if there exist S, R and A satisfying
X d= µ + RAS,
(3.47)
with
(i) S uniformly distributed on the unit sphere Sk−1 = {s ∈Rk : s′s = 1};
(ii) R ⩾0, a radial rv, independent of S, and
(iii) A ∈Rd×k with AA′ = Σ.
For practical examples we are most interested in the case where Σ is positive
deﬁnite. The relation between the elliptical and spherical cases is then clearly
X ∼Ed(µ, Σ, ψ) ⇐⇒Σ−1/2(X −µ) ∼Sd(ψ).
(3.48)
In this case, if the spherical vector Y has density generator g, then X = µ + Σ1/2Y
has density
f (x) =
1
|Σ|1/2 g((x −µ)′Σ−1(x −µ)).
The joint density is always constant on sets of the form {x : (x −µ)′Σ−1(x −µ) =
c}, which are ellipsoids in Rd. Clearly, the full family of multivariate normal variance
mixtures with general location and dispersion parameters µ and Σ are elliptical,
since they are obtained by afﬁne transformations of the spherical special cases
considered in the previous section.
It follows from (3.44) and (3.48) that for a non-singular elliptical variate X ∼
Ed(µ, Σ, ψ) with no point mass at µ we have

(X −µ)′Σ−1(X −µ),
Σ−1/2(X −µ)

(X −µ)′Σ−1(X −µ)

d= (R, S),
(3.49)
where S is uniformly distributed on Sd−1 and R is an independent scalar rv. This
forms the basis of a test of elliptical symmetry described in Section 3.3.5.
The following proposition shows that a particular conditional distribution of an
elliptically distributed random vector X has the same correlation matrix as X and
can also be used to test for elliptical symmetry.
Proposition 3.29. Let X ∼Ed(µ, Σ, ψ) and assume Σ is positive deﬁnite and
cov(X) is ﬁnite. For any c ⩾0 such that P((X −µ)′Σ−1(X −µ) ⩾c) > 0 we
have
ρ(X | (X −µ)′Σ−1(X −µ) ⩾c) = ρ(X).
(3.50)
Proof. It follows easily from (3.49) that
X | (X −µ)′Σ−1(X −µ) ⩾c d= µ + RΣ1/2S | R2 ⩾c,
where R d=

(X −µ)′Σ−1(X −µ) and S is independent of R and uniformly distributed on Sd−1. Thus we have
X | (X −µ)′Σ−1(X −µ) ⩾c d= µ + ˜RΣ1/2S,
where ˜R d= R | R2 ⩾c. It follows from Proposition 3.28 that the conditional distribution remains elliptical with dispersion matrix Σ and (3.50) holds.
--- page 111 ---

3.3. Spherical and Elliptical Distributions
95
3.3.3
Properties of Elliptical Distributions
We now summarize some of the properties of elliptical distributions in a format that
allows their comparison with the properties of multivariate normal distributions in
Section 3.1.3. Many properties carry over directly and others need only be slightly
modiﬁed. These parallels emphasize that it would be fairly easy to base many standard procedures in risk management on an assumption that risk-factor changes have
an approximately elliptical distribution, rather than the patently false assumption
that they are multivariate normal.
Linear combinations.
If we take linear combinations of elliptical random vectors,
then these remain elliptical with the same characteristic generator ψ. Let X ∼
Ed(µ, Σ, ψ) and take any B ∈Rk×d and b ∈Rd. Then it is easily shown, using a
similar argument to that in Proposition 3.9, that
BX + b ∼Ek(Bµ + b, BΣB′, ψ).
(3.51)
As a special case, if a ∈Rd, then
a′X ∼E1(a′µ, a′Σa, ψ).
(3.52)
Marginal distributions.
It follows from (3.52) that marginal distributions of X
must be elliptical distributions with the same characteristic generator. Using the X =
(X1, X2)′ notation from Section 3.1.1 and again extending this notation naturally
to µ and Σ:
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
we have that X1 ∼Ek(µ1, Σ11, ψ) and X2 ∼Ed−k(µ2, Σ22, ψ).
Conditional distributions.
The conditional distribution of X2 given X1 may also
be shown to be elliptical, although in general with a different characteristic generator
˜ψ. For details of how the generator changes see Fang, Kotz and Ng (1987, pp. 45, 46).
In the special case of multivariate normality the generator remains the same.
Quadratic forms.
If X ∼Ed(µ, Σ, ψ) with Σ non-singular, then we observed
in (3.49) that
Q := (X −µ)′Σ−1(X −µ) d= R2,
(3.53)
where R is the radial rv in the stochastic representation (3.41). As we have seen
in Example 3.24, for some particular cases the distribution of R2 is well known: if
X ∼Nd(µ, Σ), then R2 ∼χ2
d ; if X ∼td(ν, µ, Σ), then R2/d ∼F(d, ν). For all
elliptical distributions Q must be independent of Σ−1/2(X −µ)/√Q.
Convolutions.
The convolution of two independent elliptical vectors with the same
dispersion matrix Σ is also elliptical. If X and Y are independent d-dimensional
random vectors satisfying X ∼Ed(µ, Σ, ψ) and Y ∼Ed( ˜µ, Σ, ˜ψ), then we may
take the product of characteristic functions to show that
X + Y ∼Ed(µ + ˜µ, Σ, ¯ψ),
(3.54)
where ¯ψ(u) = ψ(u) ˜ψ(u).
--- page 112 ---

96
3. Multivariate Models
If the dispersion matrices of X and Y differ by more than a constant factor, then
the convolution will not necessarily remain elliptical, even when the two generators
ψ and ˜ψ are identical.
3.3.4
Estimating Dispersion and Correlation
Suppose we have risk-factor return data X1, . . . , Xn that we believe come from some
elliptical distribution Ed(µ, Σ, ψ) with heavier tails than the multivariate normal.
We recall from Remark 3.27 that the dispersion matrix Σ is not uniquely determined,
but rather is only ﬁxed up to a constant of proportionality; when covariances are
ﬁnite the covariance matrix is proportional to Σ.
In this section we consider brieﬂy the problem of estimating the location parameter µ, a dispersion matrix Σ and the correlation matrix P, assuming ﬁniteness of
second moments. We could use the standard estimators of Section 3.1.2. Under an
assumption of iid or uncorrelated vector observations we observed that ¯X and S
in (3.9) are unbiased estimators of the mean vector and covariance matrix, respectively. They will also be consistent under quite weak assumptions. However, this
does not necessarily mean they are the best estimators of location and dispersion
for any given ﬁnite sample of elliptical data. There are many alternative estimators
that may be more efﬁcient for heavy-tailed data and may enjoy better robustness
properties for contaminated data.
One strategy would be to ﬁt a number of normal variance mixture models, such
as the t and normal inverse Gaussian, using the approach of Section 3.2.5. From
the best-ﬁtting model we would obtain an estimate of the mean vector and could
easily calculate the implied estimates of the covariance and correlation matrices. In
this section we give simpler, alternative methods that do not require a full ﬁtting of
a multivariate distribution; consult Notes and Comments for further references to
robust dispersion estimation.
M-estimators.
Maronna’s M-estimators (Maronna 1976) of location and dispersion are a relatively old idea in robust statistics, but they have the virtue of
being particularly simple to implement. Let ˆµ and
ˆΣ denote estimates of the
mean vector and dispersion matrix. Suppose for every observation Xi we calculate D2
i = (Xi −ˆµ)′ ˆΣ−1(Xi −ˆµ). If we wanted to calculate improved estimates
of location and dispersion, particularly for heavy-tailed data, it might be expected
that this could be achieved by reducing the inﬂuence of observations for which Di
is large, since these are the observations that might tend to distort the parameter
estimates most. M-estimation uses decreasing weight functions wj : R+ →R+,
j = 1, 2, to downweight observations with large Di values. This can be turned
into an iterative procedure that converges to so-called M-estimates of location and
dispersion; the dispersion matrix estimate is in general a biased estimate of the true
covariance matrix.
Algorithm 3.30 (M-estimators of location and dispersion).
(1) As starting estimates take ˆµ[1] = ¯X and ˆΣ[1] = S, the standard estimators
in (3.9). Set iteration count k = 1.
--- page 113 ---

3.3. Spherical and Elliptical Distributions
97
(2) For i = 1, . . . , n set D2
i = (Xi −ˆµ[k])′ ˆΣ[k] −1(Xi −ˆµ[k]).
(3) Update the location estimate using
ˆµ[k+1] =
n
i=1 w1(Di)Xi
n
i=1 w1(Di) ,
where w1 is a weight function, as discussed below.
(4) Update the dispersion matrix estimate using
ˆΣ[k+1] = 1
n
n

i=1
w2(D2
i )(Xi −ˆµ[k])(Xi −ˆµ[k])′,
where w2 is a weight function.
(5) Set k = k + 1 and repeat steps (2)–(4) until estimates converge.
Popular choices for the weight functions w1 and w2 are the decreasing functions
w1(x) = (d + ν)/(x2 + ν) = w2(x2), for some positive constant ν. Interestingly,
use of these weight functions in Algorithm 3.30 corresponds exactly to ﬁtting a
multivariate td(ν, µ, Σ) distribution with known degrees of freedom ν using the
EM algorithm (see, for example, Meng and van Dyk 1997).
There are many other possibilities for the weight functions. For example, the
observations in the central part of the distribution could be given full weight and
only the more outlying observations downweighted. This can be achieved by setting w1(x) = 1 for x ⩽a, w1(x) = a/x for x > a, for some value a, and
w2(x2) = (w1(x))2.
Correlation estimates via Kendall’s tau.
A method for estimating correlation that
is particularly easy to carry out is based on Kendall’s rank correlation coefﬁcient and
will turn out to be related to a method for estimating the parameters of certain copulas
in Chapter 5. The theoretical version of Kendall’s rank correlation (also known as
Kendall’s tau) for two rvs X1 and X2 is denoted ρτ(X1, X2) and is deﬁned formally
in Section 5.2.2; it is shown in Proposition 5.37 that if (X1, X2) ∼E2(µ, Σ, ψ),
then
ρτ(X1, X2) = 2
π arcsin(ρ),
(3.55)
where ρ = σ12/(σ11σ22)1/2 is the pseudo-correlation coefﬁcient of the elliptical
distribution, which is always deﬁned (even when correlation coefﬁcients are unde-
ﬁned because variances are inﬁnite). This relationship can be inverted to provide a
method for estimating ρ from data; we simply replace the left-hand side of (3.55)
by the standard textbook estimator of Kendall’s tau, which is given in (5.50), to
get an estimating equation that is solved for ˆρ. This method estimates correlation
by exploiting the geometry of an elliptical distribution and does not require us to
estimate variances and covariances.
The method can be used to estimate a correlation matrix of a higher-dimensional
elliptical distribution, by applying the technique to each bivariate margin. This does,
however, result in a matrix of pairwise correlation estimates that is not necessarily positive deﬁnite; this problem does not always arise and if it does, a matrix
--- page 114 ---

98
3. Multivariate Models
•
•
••••
••
•••
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
•••••
•
••
•••••
•
•
•
••
•
••••
••
•
•
••
•
•
•
•••
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
••••
•
••••
•
•
•
•
••••
•••••••••••
••••••
•
••
•
••
••
•
••
••
•
•
•
•••••
•
•••
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
•••••
•
•
•
••
•
•
•••
•
•••
•
••
•
•
•
•
•
•
•••
••••••
•
•
••
•
••
•
•••
••
•
••
••
•
•
•
•••
•
•••
•••
••
••
•
•
••••
•
•
•
••••
•
•
•
•
•
••••
•
•
•
•••
•••
•
••
•••
•
•
•
••
••
••
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
•••
•
•••••
••
•
•
•
•
•••
••
•
•
•••••
•
•
•••••
•
•
••
••••
••
•••
•
•
•••
•
•
••
•
•
•••••
••
•
••••
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
••
•
•••
•
••••
•
•
•
••
•••
•••
•••
••
••
•
•••
•
••
•
••
•
•
••••
•••
•
•
•••••
•••
•
•
•
••
•
•
•
•
••
••••
•
•
•
•
•
••
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
•
•
••
•••
•
••
•
•
•••
•
•
••
•
•
•
•
•
•••••
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
••
•••••
•
•••
••
••
••
•
•
•
•
•
••
•••
•
••
•
••
•
•
•
•
••
•
••
•
••
•
•
•
••••
•
•••
•
•
•••
•
••
•
•
•
•
•••
•
••••••
•
•
•
•••
•••
•
•
••
•
••
••
•
•
••••
••
•
•
••
•
••
•
•
•
••
•
•
••
•
•••
•
•
•
••
•
••
•••••
•
•
••
•
•
•••
•
•••
•
•
•
••
••••••
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
••
••••••
••
••
•
•
•
•
•••••
••
•
••
•
•••
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
•••
•
•
••
••
••••••••
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
••
•
•
••
•
•
••
••
•••
•
••
•
•
•
•••
•••••
•
•
•••
••••
•
•
•
•
•••
•
••
•
••
•
•
•
••
••
•
•••••
••
•
•
••
•
•
•
•••
•
•
••••
•
••
••••••
•
••••
•
•••
•
•••••
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
••
•
•
•••
•
••
•
•
•
••••••
•
•
••
•
••
•
•
•
•••
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
•
•••
•
•
•
•
•••
•
••••••
•
•
•
••
••••
••
•••
••••
•
•
••
•
•
•
••
•
•
•••
•••
•
•••
•
•
•
•••
•
•
••
••
••
•
••
•
•
•
••
••
•
•
•
••••
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
••
•
•
••
•
••
••
•
••
•••
••
•
•
••
•
•
•
••
•
•
••••
•
•
•
•••
••
•••
•
••
•
•
••
•
•
•••••
•
•
•
•••
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
•••
•
••••
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
••
••••
•
•
•••
•
•
•••
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
••
••••
••
••
•
•
•
•
••••
•••
•
•••
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
•••
•
••
•••
•
•
•
•
••••••
•••
••
••
•
•
••••••
•
••
•
••
•
••
•
•
••
•
•
••
•••
•
••
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
••••••
••
••
•
••
•
•
•
•
•
•
•••••
•
•
•
•••
•
•
•••
•
•••••••••
•
•••
••
•
••
•
•
•
••
••
••
•
•
•
••
•
••
•
•••
•
•
•
•••••
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
•••
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
••
••••
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
••
•
••
•
••
•
••
••
••
•
•
•
••
•••
•
•••
•
••
•
•
•
••
•
•
•••
•
••
••
•
•
•••
•
•••
•
•
•
•••
••
••
••
•
•
•••••
•
•
•
••
••
•••
•
••••
••••
•
•
•
•
•••
••••
•
••
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
••
•
••
•
••
••••
•
•
•
•
•
••••
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
•
•
••
••
•
•
••
•
••
••••
•
•
•
•
•
••
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
•
••••
••
•
••
••••
•
•
•
•
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
••
••
••
•
•••
••
•••
••
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
•••
•
•••••••
•
••
••••
••
•••
••
•
•
••••
•
•••
•••
•
••
••
•
•
•
••
•
•••
••••
••
•
•
•
•
••
•
•
•
•••••
•
••
•
•
•••
••
••••
•
•
••••••
•
••
•
••
•
•
•
••
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
•••
•
••
•••
•••••••
•
•
•
•
•
•
••
••
•
•••
••
•
•
•
•••
•
••
•••
•
••••
••
•
•••
•
•••
••
•
•
•••••
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
•
••
••
•
•
•
••
•
••
••••
•
••
•••••
•••
•••
•
•••
•
•
••
•
••••••
•
•
••
•••
•
•
•••••
•
••••
•
•••
•
••
•
•••
•
•
•••
•
•••
•••
•
•
••••
•
•
•
•
•
•••
•
•
••••
••••
•
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
•
•
•••
••
•
•••
•
•
•
•••
•
••••
•
•
•
•
•
••
•
•
••
••
••••
••
•••
•
••••••
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
••
••
••
••
•••
•
•
•
•
•
•
••••
•
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
•••
••••
•
•
•
•••
•
•
•••
•
•
•••
•
•
••
•
•••••
•
•••••
••
••
••
•
•
•
•
•••
•
••
••
•
•
••
•••
•
•
•••
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
•
•
••••
•
•
•
••
•••
•
•
•
•
•
••••
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
••••
•
•
•••
•••
•
•••
•••
•
•
•
•••••
•
••
••
•••
••
•
•
•
•
•
•
••
•••
•
••••••
••
••
••••
•
••
•
••
•
•
••
••••
•
•
••••
•
••
•
•••••
•
•
•••
•
•
•
••
•
•
••
•
••
•••
•
••
••••
••
•••
•
••
•
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
•••••
•
•
•
•
•••
•
•
••
••
••
•
••
•
••
•
••
•
•
•
•
••••
•
••
••
•
•
••
•
•
••
•
••
•
•
•
•••
•
•
•
•
•••
••
•
•
•••••
•
•
•••••
•
••
•
•••
•
••
••••
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
••
•
•
•
•
•
•••
•
•
•
••••
•
•
•
••
•
•
•••
•
•
•
•
••
•
•
••
•
••
•
•
••
•
•••
•
•••••
•
•
•
•
•
••
•
•
•
•••••••
••
•
•
•
••
•
••
••
•
•
••
•••
••
•
•
••
•
•
••
•••
•••
•
•••
•••
•
•
•
•
•
•
•••••
•
•••
•••
•••
•
••
•
••••••
•
•
•
•
•
••••
•
••
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
•••
••
•
•
•
••
••
•••••
•
••
•
••••
•
•
•
•
•
••
•
•
•••
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
••••
•
•••
•
••••
••
••••
••
•
•
••
•••••••
•
•
•
•••
••
•
••
••••
••
•
••••
•
•
••
•
•
••
•
•••••
•
•••••••••
•
•
•
•
••••••••
•
•
•
•
•••
••
•
••
•
•
•
•••
••
•
••
•
••
•
•••
•
••
•••
••••••
•••••
•
•••
•
•
••
•
•
•••
••••
•
•
•
•••
••
•••••
•••
••••
•
••
•
••
•
••••
•
•••••••
•••••
••
•
••
•
•
•
•
••
•
•
••••
•
•
•
•••
•
•••••
•
••••
•••
•
•
•••
•
•
•••
•
•
••
••
•
•
••
••••
••
•••
••
•
•
•
••••
••
•
•••
••
•
•
•
•
•
•
•
••
••
••
•••
••••••
•
••••••••
•
•••
••••
•••
••••••••
•
•
•
••••
•
•
••
••••
•
••
•
•
•••••
••••••
•
•••••
•••••••
•
•
•
•••••
••••
•
••
•••
•
••••••••••
•
••
•
•••••
••
••
•
•
•
••
••
•
••
•
•
•
••••
••••
••••••
•
•
•
•••
••••
•
•••
•
••
••••
••••••••••
•
•••••••
•
•
•
••
••
•
•
••
•••
••
•
•••
••
•
•
•
••••••••
•
••
••
•
•••••••
••
•
•••••
••
•
•••
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
••
•
•
••
••
•••
•••••
••••
•••••
••
•••••
••••••
•
•
•••••••
•
•••••••
•••••
•
•••••
•••
•••
•
•
•
•
••
••
••••••
•
••••••••
•
••••••
••
•
•
•
••
•
•••••
••
•••
•••
•
••••
•
••
•••
••••
•
•
•
••••••••
••••••••
••••
•
•
•
••••••
•••••
•
•••
•••••••
•
••
••••••••
•
•
•••
•
•
•••••••
•
•
•••
•
•••
•
•
•••••
••
•
•
••••
••
•
••
•
•••••
•••
••••••••
•
•••
•
••
••
•
••
•
•
••••••
•••
•
•
•
•
••••
•
••
•••
••••
••
••••
•••
•••••••
•
••••••
••
•
•
•••••
•
•
••••
•
••
••••••••
•
••
••••
•
••••
•
•
•
••••••
••••
•••
•
•••
•
••
•
••
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
••••
•
••••
••
••••
•
•
•••
••
•
•
•
•
•
••••
•
•••
•
••••••••
•
•
•
•
•••••••
•••••••
•
•••
•••••
•
•••
••
•
•••••
•••
•
••
••••
••
•
••••
••
•••••
•
••••
•
•••••••••
•
•
•
•
•
••
•
••
••
•
•
•••••••
•
••
••
•
•
••••
•••
•
•
•
•
•
••
••
•••••
••
•••••
•
••
•
••
•
••
•
•••
•
•••••••••
•
•••
•
•••
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
••
•
•••
••
•
•
•
•
•
••••
•
••••
••
•
••••••
•
••••••••
•
••
•
•
••••
••
•
•••••
••
•••
•••
•
•
••
•
••••
•
•
•
•
••
•
••
•••
••••••••••
••••••••
•••••
••
••••
••
•
•
•
•••
•
•
•
•
••
••••••••
••••
•
•
•
••
•
••••
•
•
•
••
•
•••
••
•
•
•••
•
••
•••••
•••
•
•
••••••
•••
•
•••
•••••
•
••
••••••
•
•
•
•••
••
•
••
•
••••••••
•
•••••••
•
•
••••
•
•
••••
•
•
••••••••
•••
•
•••
••
•
••
••
••
•
••
•••
•••
•••••••
•
•
•••
••••••••
•
••••
••••••
•
•••••••
•
••
•
•••••
•
•
••••
••••
•
••••••••
•
••••••
••
•••••••••
•••••••
•
•••••••
•
••
••••
••
•
••
•
•
•
••••••
••
•••••••••••••••
•
•••••
••••••••••
••
••••
••
•
•
•
••••
•
•••
•••
•
•
•
•
•
•
•
••••
•••
•
•
•••
•
••••
••
•
•••••••••••
••
•
•
•••
•
••••••••
•
••
•
•••
•
••••
•
••
•••
•••
•
••
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
••••
••
••••
•
••
••••••••
••
••••••••
•
••
••
•••••••••••••••
•
•
••
•
••••••
•••••••
••••
•••
•
•••
•
•
•
•••••••
•••
•••
•
•
•
••
•••
••••••
••
•
•
••••
•
•
••
•••••••
•
•
•••••
•••
••••
••
••
••
•••••
••
••
•
•••
•
••••••
•
•••
••
•
••
•
••
•••
••••
•••••••
•••
•
•••••
•
••••
•
•
•••
•
•••••••••
•••••
•••••
•
•••
••
•
•
•
•••••
•
••
•
•
••
•••
••••
••
••••
•
•••
••••••••
••
•
•••••••
••
••
••
•••••••
•••••
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
••••
••
•
•
•••
•••
•••
••••
••
•
•
•••••••
•
••••••
••••••
••
••••••••••
•
•••
••
•
•
•
•••••
•••••
••
••
•
•••••••••
••
•
•
•
•
••••
••
•••
•••••
•
•
•••
••••
••••••
•
•••••
•
•••
•
•••
•
••
••••••
••
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
••
••••••
••••••••
•
•
•
•••
•••
•••••
•
•
•
•••
•
•
••
••••
•
•••
•
•
•
•
•••••
••••
•
•
•
••
•••••
•
••
••••••••••
•••
••
•••
•
•••••••••••••
•
••••••
•
••
••
•••••
••
••
•
•
••••
•••
•
••
•
•
•••
•••••
•
••
•
••••
•
•
•
•••
••••
•
•••
•
•••••
•••
•
••••••••••
•
•••
•
•••
•
••
••
•
••
•••
••
•
•
•
••
•
•
•
••
••••
••
••
•
••••
•
••••••
•
•••
•••••••••
•
•••
••••••
•
••
••
•
•
•••••••••••
•••••
••••
•
•••
•
•••
•
•
•
•
•
•
•••••••
••••••••••
••••
••••
••
•••
•
••
••
••
••
••
•
••
•
•
•
••••
•
••
••
•
•••
••••••
•
••
••
•
••
•••
•
••
••••
••
•
•
•
•
•••••••••••
•
•••
•••
•
•
•
•
•
••••
•
••••••
••
•
•
••
••
••••••
•••••••
•
••
•
•
•••
••
•
•
•
•
•
•••••
•
•
•
••
••••
•
•
•••
•••••
••••
•
•
•
••••••
••
•
••••
•
•••
••
••••••••
•••
••
•
••
•
•
••
•••••••••
•••••
•
••
••••••••
••••
•
••••
0
500
1000
1500
2000
2500
3000
1.0
0.5
−0.5
0
−1.0
1.0
0.5
−0.5
0
−1.0
(a)
(b)
Figure 3.5.
For 3000 independent samples of size 90 from a bivariate t distribution with
three degrees of freedom and linear correlation 0.5: (a) the standard (Pearson) estimator of
correlation; (b) the Kendall’s tau transform estimator. See Example 3.31 for commentary.
adjustment method can be used, such as the eigenvalue method of Rousseeuw and
Molenberghs (1993), which is given in Algorithm 5.55.
Note that, to turn an estimate of a bivariate correlation matrix into a robust estimate of a dispersion matrix we could estimate the ratio of standard deviations
λ = (σ22/σ11)1/2, for example by using a ratio of trimmed sample standard deviations; in other words, we leave out an equal number of outliers from each of the
univariate datasets X1,i, . . . , Xn,i for i = 1, 2 and calculate the sample standard
deviations with the remaining observations. This would give us the estimate
ˆΣ =

1
ˆλ ˆρ
ˆλ ˆρ
ˆλ2

.
(3.56)
Example 3.31 (efﬁcient correlation estimation for heavy-tailed data). Suppose
we calculate correlations of asset or risk-factor returns based on 90 days (somewhat
more than three trading months) of data; it would seem that this ought to be enough
data to allow us to accurately estimate the “true” underlying correlation under an
assumption that we have identically distributed data for that period.
Figure3.5displaystheresultsofasimulationexperimentwherewehavegenerated
3000 bivariate samples of iid data from a t distribution with three degrees of freedom
and correlation ρ = 0.5; this is a heavy-tailed elliptical distribution. The distribution
of the values of the standard correlation coefﬁcient (also known as the Pearson
correlation coefﬁcient) is not particularly closely concentrated around the true value
and produces some very poor estimates for a number of samples. On the other hand
the Kendall’s tau transform method produces estimates that are in general much
closer to the true value, and thus provides a more efﬁcient way of estimating ρ.
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
