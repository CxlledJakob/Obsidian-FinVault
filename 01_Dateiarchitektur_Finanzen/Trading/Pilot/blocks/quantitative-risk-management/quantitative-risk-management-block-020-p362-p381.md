# Quantitative Risk Management_ Concepts, Techniques, and -- Alexander J_ McNeil, Rüdiger Frey, Paul Embrechts -- Princeton series in finance, -- isbn13 9780691122557 -- 478a0059673fecd0c76229cd3d8884e7 -- Anna’s Arc.pdf — pages 362–381

--- page 362 ---

346
8. Credit Risk Management
We now give a simple criterion for equivalence of two threshold models in terms of
the marginal distributions of the state vector S and the copula of X.While straightforward from a mathematical viewpoint, the result is useful for studying the structural
similarities between various industry models for portfolio credit risk management.
For the necessary background information on copulas we refer to Chapter 5.
Lemma 8.5. Let (X, D) and ( ˜X, ˜D) be a pair of threshold models with state vectors
S = (S1, . . . , Sm)′ and ˜S = ( ˜S1, . . . , ˜Sm)′, respectively. The models are equivalent
if the following conditions hold.
(i) The marginal distributions of the random vectors S and ˜S coincide, i.e.
P(Si = j) = P( ˜Si = j),
j ∈{1, . . . , n}, i ∈{1, . . . , m}.
(ii) X and ˜X admit the same copula C.
Proof. According to Deﬁnition 8.4, S d= ˜S if and only if, for all j1, . . . , jm ∈
{1, . . . , n},
P(d1j1 < X1 ⩽d1(j1+1), . . . , dmjm < Xm ⩽dm(jm+1))
= P( ˜d1j1 < ˜X1 ⩽˜d1(j1+1), . . . , ˜dmjm < ˜Xm ⩽˜dm(jm+1)).
By standard measure-theoretic arguments this holds if, for all j1, . . . , jm
∈
{1, . . . , n},
P(X1 ⩽d1j1, . . . , Xm ⩽dmjm) = P( ˜X1 ⩽˜d1j1, . . . , ˜Xm ⩽˜dmjm).
By Sklar’s theorem (Theorem 5.3) this is equivalent to
C(F1(d1j1), . . . , Fm(dmjm)) = C( ˜F1( ˜d1j1), . . . , ˜Fm( ˜dmjm)),
where C is the copula of X and ˜X (using condition (ii)). Condition (i) implies that
Fi(dij) = ˜Fi( ˜dij) for all j ∈{1, . . . , n}, i ∈{1, . . . , m}, and the claim follows.
The copula in a threshold model determines the link between marginal probabilities of migration for individual ﬁrms and joint probabilities of migration for groups
of ﬁrms. Consider for simplicity a two-state model for default and non-default and
a subgroup of k companies {i1, . . . , ik} ⊂{1, . . . , m} with individual default probabilities ¯pi1, . . . , ¯pik. Then
P(Yi1 = 1, . . . , Yik = 1) = P(Xi1 ⩽di11, . . . , Xik ⩽dik1)
= Ci1···ik( ¯pi1, . . . , ¯pik),
(8.23)
where Ci1···ik denotes the corresponding k-dimensional margin of C. As a special
case consider now a model for a single homogeneous group.We assume that X has an
exchangeable copula (i.e. a copula of the form (5.18)) and that all individual default
probabilities are equal to some constant π so that the default indicator vector Y is
exchangeable. The formula (8.23) reduces to the useful formula
πk = C1···k(π, . . . , π),
2 ⩽k ⩽m,
(8.24)
which will be used for the calibration of some copula models later on.
--- page 363 ---

8.3. Threshold Models
347
8.3.3
Industry Examples
As we have remarked, a number of popular industry models ﬁt into the general
framework of threshold models and we give some more detail in this section.
Example 8.6 (CreditMetrics and KMV models). The portfolio versions of the
KMV and CreditMetrics models introduced in Section 8.2.5 use a similar mechanism to model the joint distribution of defaults; they differ only with respect to the
approach used for the determination of individual default probabilities.
In both models the vector of critical variables X is assumed to have a multivariate
normal distribution and Xi can be interpreted as a change in asset value for obligor i
over the time horizon of interest; di1 is chosen so that the probability that Xi ⩽
di1 matches the given default probability ¯pi for company i. Obviously, both the
CreditMetrics and KMV models work with a Gauss copula for the critical variables
X and are hence structurally similar. In particular, by Proposition 8.5 the twostate versions of the models are equivalent, provided that the individual default
probabilities ¯p1, . . . , ¯pm and the correlation matrix P of X are identical.
In both models the covariance matrix of X is calibrated using a factor model of
the kind described in Section 3.4.1. Assume that we have transformed the critical
variables and thresholds in such a way that the margins of X are standard normal.
It is assumed that X can be written as
X = BF + ε
(8.25)
for a p-dimensional random vector of common factors F ∼Np(0, Ω) with p < m,
a loading matrix B ∈Rm×p, and an m-dimensional vector of independent univariate
normally distributed errors ε, which are also independent of F. Here the random vector F represents country and industry effects. Obviously, the factor structure (8.25)
implies that the covariance matrix P of X (which will be a correlation matrix due to
our assumptions on the marginal distributions of X) is of the form P = BΩB′ +Υ ,
where Υ is the diagonal covariance matrix of ε.
Writing bi = (bi1, . . . , bip)′ for the ith row of B, the ith critical variable has the
structure Xi = b′
iF + εi. Recalling that var(Xi) = 1, it follows that
βi := b′
iΩbi
(8.26)
can be viewed as the systematic risk of Xi: that is, the part of the variance of Xi
which is explained by the common factors F. The idiosyncratic risk not explained
by the common factors is var(εi) = 1 −βi.
In the factor model employed by KMV the factors are assumed to be observable,
and a time series of factor returns is constructed by forming appropriate indices
of asset values of publicly traded companies. The factor weights comprising B are
determined using non-quantitative economic arguments combined with regression
techniques; some details can be found in Kealhofer and Bohn (2001).
Example 8.7 (Li’s model). This model, proposed in Li (2001), is a simple dynamic
model used by practitioners to price basket credit derivatives. The author interprets
the critical variable Xi as the default time of company i and assumes that Xi is
--- page 364 ---

348
8. Credit Risk Management
exponentially distributed with parameter λi so that Fi(t) = 1 −exp(−λit). Obviously, company i defaults by time T if and only if Xi ⩽T , so ¯pi = Fi(T ). To
determine the multivariate distribution of X, Li assumes that X has the Gauss copula CGa
P for some correlation matrix P (see, for example, (5.9) in Section 5.1.2)
so that P(X1 ⩽t1, . . . , Xm ⩽tm) = CGa
P (F1(t1), . . . , Fm(tm)). It is immediate
from Lemma 8.5 that in Li’s model the distribution of the default indicators at some
ﬁxed horizon T is equivalent to a model of CreditMetrics/KMV type, provided that
individual default probabilities coincide and that the correlation matrix of the assetvalue change X in the KMV-type model equals P. This equivalence is often used
to calibrate Li’s model. We will have a closer look at the model in our analysis of
dynamic copula models in Section 9.7.
8.3.4
Models Based on Alternative Copulas
While most threshold models used in industry are based explicitly or implicitly on
the Gauss copula, there is no reason why we have to assume a Gauss copula. In fact,
simulations presented in Section 8.3.5 show that the choice of copula may be very
critical to the tail of the distribution of the number of defaults M. We now look at
threshold models based on alternative copulas.
The ﬁrst class of model attempts to preserve some of the ﬂexibility of models of
KMV/CreditMetrics type, which do have the appealing feature that they can accommodate a wide range of different correlation structures for the critical variables. This
is clearly an advantage in modelling a portfolio where obligors are exposed to several risk factors and where the exposure to different risk factors differs markedly
across obligors, such as a portfolio of loans to companies from different industry
sectors or countries.
Example 8.8 (normal mean-variance mixtures). For the distribution of the critical
variables we consider the kind of model described in Section 3.2.2. We start with
an m-dimensional multivariate normal vector Z ∼Nm(0, Σ) and a positive, scalar
rv W, which is independent of Z. The vector of critical variables X is assumed to
have the structure
X = m(W) +
√
WZ,
(8.27)
where m : [0, ∞) →Rm is a measurable function. In the special case where m(W)
takes a constant value µ not depending on W, the distribution is called a normal
variance mixture.
An important example of a normal variance mixture is the multivariate t distribution, as discussed in Example 3.7, which is obtained when W has an inverse gamma
distribution, W ∼Ig( 1
2ν, 1
2ν), or equivalently when ν/W ∼χ2
ν . An example of a
general mean-variance mixture is the generalized hyperbolic distribution discussed
in Section 3.2.3.
In a normal mean-variance mixture model the default condition may be written
as
Xi ⩽di1 ⇐⇒Zi ⩽di1
√
W
−mi(W)
√
W
=: ˜Di,
(8.28)
--- page 365 ---

8.3. Threshold Models
349
where mi(W) is the ith component of m(W). A possible economic interpretation of
the model (8.27) is to consider Zi as the asset value of company i and di1 as an a
priori estimate of the corresponding default threshold. The actual default threshold
is stochastic and is represented by ˜Di, which is obtained by applying a multiplicative
and an additive shock to the estimate di1. If we interpret this shock as a stylized
representation of global factors such as the overall liquidity and risk appetite in the
banking system, it makes sense to assume that the shocks to the default thresholds
of different obligors are driven by the same rv W.
Normal variance mixtures, such as the multivariate t, provide the most tractable
examples of normal mean-variance mixtures; they admit a similar calibration
approach using linear factor models to models based on the Gauss copula. In normal variance mixture models the correlation matrices of X (when deﬁned) and Z
coincide. Moreover, if Z follows a linear factor model (8.25), then X inherits the
linear factor structure from Z. Note however, that the systematic factors
√
WF and
the idiosyncratic factors
√
Wε are no longer independent but merely uncorrelated.
A threshold model based on the t copula can be thought of as containing the
standard KMV/CreditMetrics model based on the Gauss copula as a limiting case
as ν →∞. However, the additional parameter ν adds a great deal of ﬂexibility to
the model. We will come back to this point in Section 8.3.5.
Another class of parametric copulas that could be used in threshold models is the
Archimedean family of Section 5.4.
Example 8.9 (Archimedean copulas). Recall that an Archimedean copula is the
distribution function of a uniform random vector of the form
C(u1, . . . , um) = φ−1(φ(u1) + · · · + φ(um)),
(8.29)
where φ : [0, 1] →[0, ∞] is a continuous, strictly decreasing function, known as
thecopulagenerator,andφ−1 isitsinverse.Weassumethatφ(0) = ∞,φ(1) = 0 and
that φ−1 is completely monotonic (see equation (5.39) and surrounding discussion).
As explained in Section 5.4, these conditions ensure that (8.29) deﬁnes a copula for
any portfolio size m. Our main example in this chapter will be Clayton’s copula.
Recall from Section 5.4 that the Clayton copula has generator φθ(t) = t−θ −1,
where θ > 0, leading to the copula
CCl
θ (u1, . . . , um) = (u−θ
1
+ · · · + u−θ
m + 1 −m)−1/θ.
(8.30)
As discussed in Section 5.4, exchangeable Archimedean copulas suffer from the
deﬁciency that they are not rich in parameters and can model only exchangeable
dependence and not a fully ﬂexible dependence structure for the critical variables.
Nonetheless, they yield useful parsimonious models for relatively small homogeneous portfolios, which are easy to calibrate and simulate, as we discuss in more
detail in Section 8.4.4.
Suppose that X is a random vector with anArchimedean copula and with marginal
distributions Fi, 1 ⩽i ⩽m, so that (X, D) speciﬁes a threshold model with individual default probabilities Fi(di1). As a particular example consider the Clayton
--- page 366 ---

350
8. Credit Risk Management
copula and assume a homogeneous situation where all individual default probabilities are identical to π. Using relation (8.23), we can calculate that the probability
that an arbitrarily selected group of k obligors from a portfolio of m such obligors
defaults over the time horizon is given by πk = (kπ−θ −k + 1)−1/θ. Essentially,
the dependent default mechanism of the homogeneous group is now determined
by this equation and the parameters π and θ. We study this Clayton copula model
further in Example 8.22.
8.3.5
Model Risk Issues
Recall from Chapter 2 that model risk may be roughly deﬁned as the risk associated
with working with misspeciﬁed models—in our case, models which are a poor
representation of the true mechanism governing defaults and migrations in a credit
portfolio. For example, if we intend to use our models to estimate measures of tail
risk, like VaR and expected shortfall, then we should be particularly concerned with
the possibility that they might underestimate the tail of the portfolio loss distribution.
As we have seen, a threshold model essentially consists of a collection of default
(and migration) probabilities for individual ﬁrms and a copula that describes the
dependence of certain critical variables. In discussing model risk in this context we
will concentrate on models for default only and assume that individual default probabilities have been satisfactorily determined. It is much more difﬁcult to determine
the copula describing default dependence and we will look at model risk associated
with the misspeciﬁcation of this component of the threshold model.
The impact of the choice of copula.
Since most threshold models used in industry
use the Gauss copula, we are particularly interested in the sensitivity of the distribution of the number of defaults M with respect to the assumption of Gaussian
dependence. Our interest is motivated by the observation made in Section 5.3.1 that,
by assuming a Gaussian dependence structure, we may underestimate the probability of joint large movements of risk factors, with potentially drastic implications for
the performance of risk-management models.
We compare a model with multivariate normal critical variables and a model
where the critical variables are multivariate t. For simplicity we consider a homogeneous group model with factor structure, which we now describe. Given a standard
normal rv F, an iid sequence ε1, . . . , εm of standard normal variates independent
of F and an asset correlation parameter ρ ∈[0, 1], we deﬁne a random vector Z by
Zi = √ρF + √1 −ρεi. Observe that this vector follows the so-called equicorrelation factor model described in Example 3.34 and equation (3.63).
In the t copula case we deﬁne the critical variables Xi :=
√
WZi, where
W ∼Ig( 1
2ν, 1
2ν) is independent of Z, so that X has a multivariate t distribution.
In the Gauss copula case we simply set X := Z. In both cases we choose thresholds
so that P(Yi = 1) = π for all i and for some π ∈(0, 1). Note that the correlation
matrix P of X (the asset correlation matrix) is identical in both models and is given
by an equicorrelation matrix with off-diagonal element ρ. However, the copula of
X differs, and we expect more joint defaults in the t model due to the higher level
of dependence in the joint tail of the t copula.
--- page 367 ---

8.3. Threshold Models
351
Table 8.4.
Results of simulation study. We tabulate the estimated 95th and 99th percentiles
of the distribution of M in an exchangeable model with 10 000 ﬁrms. The values for the
default probability π and the asset correlation ρ corresponding to the three groups A, B and
C are given in the text.
q0.95(M)
q0.99(M)






Group
ν = ∞
ν = 50
ν = 10
ν = ∞
ν = 50
ν = 10
A
14
23
24
21
49
118
B
109
153
239
157
261
589
C
1618
1723
2085
2206
2400
3067
We deﬁne three groups of decreasing credit quality, labelled A, B and C. These
groups do not correspond exactly to the A, B and C rating categories used by any
of the well-known rating agencies, but they are nonetheless realistic values for
Gaussian threshold models for real obligors. In group A we set π = 0.06% and
ρ = 2.58%; in group B we set π = 0.50% and ρ = 3.80%; in group C we set
π = 7.50% and ρ = 9.21%. We consider a portfolio of size m = 10 000. For each
group we vary the degrees-of-freedom parameter ν. In order to represent the tail
of the number of defaults M, we use simulations to determine (approximately) the
95% and 99% quantiles, q0.95(M) and q0.99(M), and tabulate them in Table 8.4.
The actual simulation was performed using a representation of threshold models as
Bernoulli mixture models that is discussed later in Section 8.4.4.
Table 8.4 shows that ν clearly has a massive inﬂuence on the high quantiles.
For the important 99% quantile the impact is most pronounced for group A, where
q0.99(M) is increased by a factor of almost six when we go from a Gaussian model
to a model with ν = 10.
The impact of changing asset correlation.
Here we stick to the assumption that X
has a Gauss copula and study the impact of the factor structure of the asset returns
on joint default events and hence on the tail of M. More speciﬁcally, we increase the
systematic risk component of the critical variables for the obligors in our portfolio
(see equation (8.26)) and analyse how this affects the tail of M. We use the homogeneous group model introduced above as a vehicle for our analysis. We ﬁx the default
probability at π = 0.50% (the value for group B above) and vary the asset correlation ρ, which gives the systematic risk for all obligors in the homogeneous group
model, using the values ρ = 2.58%, ρ = 3.80% and ρ = 9.21%. In Table 8.5 we
tabulate q0.95(M) and q0.99(M) for a portfolio with 10 000 counterparties. Clearly,
varying ρ also has a sizeable effect on the quantiles of M. However, this effect is
less drastic and, in particular, less surprising than the impact of varying the copula
in our previous experiment.
Commentary.
Both simulation experiments indicate that attempts to calibrate
threshold models using estimates of marginal default probabilities and crude estimates of the factor structure of the critical variables obtained from asset return data
are prone to substantial model risk. Ideally, historical default data should also be
--- page 368 ---

352
8. Credit Risk Management
Table 8.5.
Results of simulation study. Estimated 95th and 99th percentiles of the
distribution of M in an exchangeable model for varying values of asset correlation ρ.
Quantile
ρ = 2.58%
ρ = 3.80%
ρ = 9.21%
q0.95(M)
98
109
148
q0.99(M)
133
157
250
used to estimate parameters describing default dependence; indeed, the best strategy might involve combining factor models for asset-value returns with statistical
estimation of some of the key parameters (such as the systematic risk parameter β
in (8.26)) using historical default data.
Notes and Comments
Our presentation of threshold models is based, to a large extent, on Frey and McNeil
(2001, 2003). In those papers we referred to the models as “latent variable” models, because of structural similarities with statistical models of that name (see Joe
1997). However, whereas in statistical latent variable models the critical variables
are treated as unobserved, in credit models they are often formally identiﬁed, for
example, as asset values or asset-value returns.
The ﬁrst systematic study of model risk for credit portfolio models is Gordy
(2000). Our analysis of the impact of the copula of X on the tail of M follows Frey,
McNeil and Nyfeler (2001). For an excellent discussion of various aspects of model
risk in risk management in general we refer to Gibson (2000).
8.4
The Mixture Model Approach
In a mixture model the default risk of an obligor is assumed to depend on a set
of common economic factors, such as macroeconomic variables, which are also
modelled stochastically. Given a realization of the factors, defaults of individual
ﬁrms are assumed to be independent. Dependence between defaults stems from the
dependence of individual default probabilities on the set of common factors. We
start with general deﬁnitions of Bernoulli and Poisson mixture models before going
on to speciﬁc examples.
Deﬁnition 8.10 (Bernoulli mixture model). Given some p < m and a p-dimensional random vector Ψ = (Ψ1, . . . , Ψp)′, the random vector Y = (Y1, . . . , Ym)′
follows a Bernoulli mixture model with factor vector Ψ if there are functions pi :
Rp →[0, 1], 1 ⩽i ⩽m, such that conditional on Ψ the components of Y are
independent Bernoulli rvs satisfying P(Yi = 1 | Ψ = ψ) = pi(ψ).
For y = (y1, . . . , ym)′ in {0, 1}m we have that
P(Y = y | Ψ = ψ) =
m
!
i=1
pi(ψ)yi(1 −pi(ψ))1−yi,
(8.31)
--- page 369 ---

8.4. The Mixture Model Approach
353
and the unconditional distribution of the default indicator vector Y is obtained by
integrating over the distribution of the factor vector Ψ . In particular, the default
probability of company i is given by ¯pi = P(Yi = 1) = E(pi(Ψ )).
Since default is a rare event, we also explore the idea of approximating Bernoulli
rvs with Poisson rvs in Poisson mixture models. Here a company may potentially
“default more than once” in the period of interest, albeit with a very low probability;
we will use the notation ˜Yi ∈{0, 1, 2, . . . } for the counting rv giving the number of
“defaults” of company i. The formal deﬁnition parallels the deﬁnition of a Bernoulli
mixture model.
Deﬁnition 8.11 (Poisson mixture model). Given p and Ψ as in Deﬁnition 8.10, the
random vector ˜Y = ( ˜Y1, . . . , ˜Ym)′ follows a Poisson mixture model with factors Ψ
if there are functions λi : Rp →(0, ∞), 1 ⩽i ⩽m, such that conditional on
Ψ = ψ the random vector ˜Y is a vector of independent Poisson distributed rvs with
rate parameter λi(ψ).
CreditRisk+, which is discussed in Section 8.4.2, is an industry example of a
Poisson mixture model. Poisson mixture models also play an important role in
actuarial mathematics (see Section 10.2.4).
We deﬁne the rv ˜M = m
i=1 ˜Yi and observe that, for small Poisson parameters λi,
˜M is approximately equal to the number of defaulting companies. Given the factors, it is the sum of conditionally independent Poisson variables and therefore its
distribution satisﬁes
P( ˜M = k | Ψ = ψ) = exp

−
m

i=1
λi(ψ)
(m
i=1 λi(ψ))k
k!
.
(8.32)
If ˜Y follows a Poisson mixture model and we deﬁne the indicators Yi = I{ ˜Yi⩾1},
then Y follows a Bernoulli mixture model and the mixing variables are related by
pi(·) = 1 −exp(−λi(·)).
Note that the two-stage hierarchical structure of mixture models facilitates sampling from the models: ﬁrst we generate the economic factor realizations, and then
the pattern of defaults conditional on those realizations. The second step is easy
because of the conditional independence assumption.
8.4.1
One-Factor Bernoulli Mixture Models
In many practical situations it is useful to consider a one-factor model. The information may not always be available to calibrate a model with more factors, and
one-factor models may be ﬁtted statistically to default data without great difﬁculty
(see Section 8.6). Their behaviour for large portfolios is also particularly easy to
understand, as will be shown in Section 8.4.3.
Throughout this section, Ψ is an rv with values in R and pi(Ψ ) : R →[0, 1]
are functions such that, conditional on Ψ , the default indicator Y is a vector of
independent Bernoulli rvs with P(Yi = 1 | Ψ = ψ) = pi(ψ). We now consider a
variety of special cases.
--- page 370 ---

354
8. Credit Risk Management
Exchangeable Bernoulli mixture models.
A further simpliﬁcation occurs if the
functions pi are all identical. In this case the Bernoulli mixture model is termed
exchangeable, since the random vector Y is exchangeable. It is convenient to introduce the rv Q := p1(Ψ ) and to denote the distribution function of this mixing
variable by G(q). Conditional on Q = q the number of defaults M is the sum of m
independent Bernoulli variables with parameter q and hence has a binomial distribution with parameters q and m, i.e. P(M = k | Q = q) =
+m
k
,
qk(1 −q)m−k. The
unconditional distribution of M is obtained by integrating over q. We have
P(M = k) =
m
k
  1
0
qk(1 −q)m−k dG(q).
(8.33)
Using the notation of Section 8.3.1 we can calculate default probabilities and joint
default probabilities for the exchangeable group. Simple calculations give π =
E(Y1) = E(E(Y1 | Q)) = E(Q) and, more generally,
πk = P(Y1 = 1, . . . , Yk = 1) = E(E(Y1 · · · Yk | Q)) = E(Qk),
(8.34)
so that unconditional default probabilities of ﬁrst and higher order are seen to be
moments of the mixing distribution. Moreover, for i̸ = j, cov(Yi, Yj) = π2 −π2 =
var(Q) ⩾0, which means that in an exchangeable Bernoulli mixture model the
default correlation ρY deﬁned in (8.22) is always non-negative. Any value of ρY
in [0, 1] can be obtained by an appropriate choice of the mixing distribution G. In
particular, if ρY = var(Q) = 0, the rv Q has a degenerate distribution with all
mass concentrated on the point π and the default indicators are independent. The
case ρY = 1 corresponds to a model where π = π2 and the distribution of Q is
concentrated on the points 0 and 1.
Example 8.12 (beta, probit-normal and logit-normal mixtures). The following
mixing distributions are frequently used in Bernoulli mixture models.
Beta mixing distribution. Here we assume that Q ∼Beta(a, b) for some parameters a > 0 and b > 0. See Section A.2.1 for more details concerning the beta
distribution.
Probit-normal mixing distribution. Here Q = Φ(µ + σΨ ) for Ψ ∼N(0, 1),
µ ∈R and σ > 0, where Φ is the standard normal distribution function. It turns
out that this model can be viewed as a one-factor version of the CreditMetrics
and KMV-type models; this is a special case of a general result in Section 8.4.4
(see equation (8.45) in particular).
Logit-normal mixing distribution. Here Q = F(µ + σΨ ) for Ψ ∼N(0, 1),
µ ∈R and σ > 0, where F(x) = (1 + exp(−x))−1 is the df of a so-called
logistic distribution.
In the model with beta mixing distribution, the higher-order default probabilities
πk and the distribution of M can be computed explicitly (see Example 8.13 below).
Calculations for the logit-normal, probit-normal and other models generally require
numerical evaluation of the integrals in (8.33) and (8.34). If we ﬁx any two of
--- page 371 ---

8.4. The Mixture Model Approach
355
π, π2 and ρY in a beta, logit-normal or probit-normal model, then this ﬁxes the
parameters a and b or µ and σ of the mixing distribution and higher-order joint
default probabilities are automatic.
Example 8.13 (beta mixing distribution). By deﬁnition, the density of a beta
distribution is given by
g(q) =
1
β(a, b)qa−1(1 −q)b−1,
a, b > 0, 0 < q < 1,
where β(a, b) denotes the beta function. Below we use the fact that the beta function
satisﬁes the recursion formula β(a+1, b) = (a/(a+b))β(a, b); this is easily established from the representation of the beta function in terms of the gamma function
in Section A.2.1. Using (8.34) we obtain for the higher-order default probabilities
πk =
1
β(a, b)
 1
0
qkqa−1(1 −q)b−1 dq = β(a + k, b)
β(a, b)
,
k = 1, 2, . . . .
The recursion formula for the beta function yields πk = k−1
j=0(a + j)/(a + b + j);
in particular, π = a/(a + b), π2 = π(a + 1)/(a + b + 1) and ρY = (a + b + 1)−1.
The rv M has a so-called beta-binomial distribution. We obtain from (8.33) that
P(M = k) =
m
k

1
β(a, b)
 1
0
qk+a−1(1 −q)m−k+b−1 dq
=
m
k
β(a + k, b + m −k)
β(a, b)
.
(8.35)
One-factor models with covariates.
It is quite straightforward to construct Bernoulli mixture models that have a single common mixing variable Ψ but which allow
covariates for individual ﬁrms to inﬂuence the default probability; these covariates
might be indicators for group membership, such as rating class or industry sector,
or key ratios taken from a company’s balance sheet.
Writing xi ∈Rk for a vector of deterministic covariates, a typical model for the
conditional default probabilities pi(Ψ ) in (8.31) would be to assume that
pi(Ψ ) = h(µ + β′xi + σΨ ),
(8.36)
where h : R →(0, 1) is a strictly increasing link function, such as h(x) = Φ(x)
or h(x) = (1 + exp(−x))−1, the vector β = (β1, . . . , βk)′ contains regression
parameters, µ ∈R is an intercept parameter, and σ > 0 is a scaling parameter. Such
aspeciﬁcationiscommonlyusedintheclassofgeneralizedlinearmodelsinstatistics
(see Section 8.6.3). We could complete the mixture model by specifying that Ψ is
standard normally distributed, which would mean that the mixing distribution for the
conditional default probability of each individual ﬁrm was of either probit-normal
or logit-normal form.
Clearly, if xi = x for all i, so that all risks have the same covariates, then we are
back in the situation of full exchangeability. Note also that, since the function pi(Ψ )
is increasing in Ψ , the conditional default probabilities (p1(Ψ ), . . . , pm(Ψ )) form
--- page 372 ---

356
8. Credit Risk Management
a comonotonic random vector; hence, in a state of the world where the default probability is comparatively high for one counterparty, it is high for all counterparties.
For a discussion of comonotonicity we refer to Section 5.1.6.
Example 8.14 (model for several exchangeable groups). The regression structure
in(8.36)includespartiallyexchangeablemodelswherewedeﬁneanumberofgroups
within which risks are exchangeable. These groups might represent rating classes
according to some internal or rating-agency classiﬁcation.
If the covariates xi are simply k-dimensional unit vectors of the form xi = er(i),
wherer(i) ∈{1, . . . , k}indicates,say,theratingclassofﬁrmi,thenthemodel(8.36)
can be written in the form
pi(Ψ ) = h(µr(i) + σΨ )
(8.37)
for parameters µr := µ + βr for r = 1, . . . , k.
Inserting this speciﬁcation in (8.31) we can ﬁnd the conditional distribution of
the default indicator vector. Suppose there are mr obligors in rating category r for
r = 1, . . . , k, and write Mr for the number of defaults. The conditional distribution
of the vector M = (M1, . . . , Mk)′ is given by
P(M = l | Ψ = ψ) =
k!
r=1
mr
lr

(h(µr + σψ))lr(1 −h(µr + σψ))mr−lr, (8.38)
where l = (l1, . . . , lk)′. A model of precisely the form (8.38) will be ﬁtted to
Standard & Poor’s default data in Section 8.6.4. The asymptotic behaviour of such
a model (when m is large) is investigated in Example 8.17.
8.4.2
CreditRisk+
CreditRisk+ is an industry model for credit risk that was proposed by Credit Suisse
Financial Products in 1997 (see Credit Suisse Financial Products 1997). The model
has the structure of a Poisson mixture model, where the factor vector Ψ consists of p
independent, gamma-distributed rvs. The distributional assumptions and functional
forms imposed in CreditRisk+ make it possible to compute the distribution of M
fairly explicitly using techniques for mixture distributions that are well known in
actuarial mathematics and which are also discussed in Chapter 10.
The structure of CreditRisk+.
CreditRisk+ is a Poisson mixture model in the
sense of Deﬁnition 8.11.The (stochastic) parameter λi(Ψ ) of the conditional Poisson
distribution for ﬁrm i is given by λi(Ψ ) = kiw′
iΨ for a constant ki > 0, non-negative
factor weights wi = (wi1, . . . , wip)′ satisfying 
j wij = 1, and p independent
Ga(αj, βj)-distributedfactorsΨ1, . . . , Ψp withparameterssettobeαj = βj = σ −2
j
for some σj > 0. This parametrization of the gamma variables ensures that we
have E(Ψj) = 1, var(Ψj) = σ 2
j and E(λi(Ψ )) = kiE(w′
iΨ ) = ki. Observe that
in this model the default probability is given by P(Yi = 1) = P( ˜Yi > 0) =
E(P( ˜Yi > 0 | Ψ )). Since ˜Yi is Poisson given Ψ , we have that
E(P( ˜Yi > 0 | Ψ )) = E(1 −exp(−kiw′
iΨ )) ≈kiE(w′
iΨ ) = ki,
(8.39)
--- page 373 ---

8.4. The Mixture Model Approach
357
where the approximation holds because ki is typically small. Hence ki is approximately equal to the default probability for ﬁrm i.
Gamma–Poisson mixtures.
The distribution of ˜M = m
i=1 ˜Yi in CreditRisk+ is
conditionally Poisson and satisﬁes
˜M | Ψ = ψ ∼Poi
 m

i=1
kiw′
iψ

.
(8.40)
To compute the unconditional distribution of ˜M we require a well-known result on
mixed Poisson distributions, which appears as Proposition 10.20 in a discussion
of relevant actuarial methodology for quantitative risk management in Chapter 10.
This result says that if the rv N is conditionally Poisson with a gamma-distributed
rate parameter, Λ ∼Ga(α, β), then N has a negative binomial distribution, N ∼
Nb(α, β/(β + 1)).
In the case when p = 1 we may apply this result directly to (8.40) to deduce that
˜M has a negative binomial distribution (since a constant times a gamma variable
remains gamma distributed).
For arbitrary p we now show that
˜M is equal in distribution to a sum of p
independent negative binomial rvs. This follows by observing that
m

i=1
kiw′
iΨ =
m

i=1
ki
p

j=1
wijΨj =
p

j=1
Ψj
 m

i=1
kiwij

.
Now consider rvs ˜M1, . . . , ˜Mp such that ˜Mj is conditionally Poisson with mean
(m
i=1 kiwij)ψj conditional on Ψj = ψj. The independence of the components
Ψ1, . . . , Ψp implies that the
˜Mj are independent, and by construction we have
˜M d= p
j=1 ˜Mj. Moreover, the rvs (m
i=1 kiwij)Ψj are gamma distributed, so that
each of the ˜Mj has a negative binomial distribution by Proposition 10.20.
This observation is the starting point for the computation of the distribution of ˜M
in CreditRisk+. Using Panjer recursion (see Section 10.2.3), it is in fact possible to
derive simple recursion formulas for the probabilities P( ˜M = k).
8.4.3
Asymptotics for Large Portfolios
We now provide some asymptotic results for large portfolios in Bernoulli mixture
models. These results can be used to approximate the credit loss distribution and
associated risk measures in a large portfolio. Moreover, they are useful for identifying the crucial parts of a Bernoulli mixture model. In particular, we will see that
in one-factor models the tail of the loss distribution is essentially determined by the
tail of the mixing distribution, which has direct consequences for the analysis of
model risk in mixture models and for the setting of capital-adequacy rules for loan
books.
Since we are interested in asymptotic properties of the overall loss distribution, we
also consider exposures and losses given default. Let (ei)i∈N be an inﬁnite sequence
of positive deterministic exposures, let (Yi)i∈N be the corresponding sequence of
--- page 374 ---

358
8. Credit Risk Management
default indicators, and let (δi)i∈N be a sequence of rvs with values in (0, 1] representing percentage losses given that default occurs. In this setting the loss for a portfolio
of size m is given by L(m) = m
i=1 Li, where Li = eiδiYi are the individual losses.
We now make some technical assumptions for our model.
(A1) There is a p-dimensional random vector Ψ and functions ℓi : Rp →[0, 1]
such that, conditional on Ψ , the (Li)i∈N form a sequence of independent rvs
with mean ℓi(ψ) = E(Li | Ψ = ψ).
In this assumption the conditional independence structure is extended from the
default indicators to the losses. Note that it is not assumed that losses given default
δi and default indicators are independent, an assumption which is made in many
standard models. In particular, (A1) allows for the situation where Yi and δi are only
conditionally independent given Ψ , such that ℓi(ψ) = δi(ψ)pi(ψ), where δi(ψ)
gives the expected percentage loss given default, given Ψ = ψ. This extension
is relevant from an empirical viewpoint since evidence suggests that losses given
default tend to depend on the state of the underlying economy (see Notes and Comments).
(A2) There is a function ¯ℓ: Rp →R+ such that
lim
m→∞
1
mE(L(m) | Ψ = ψ) = lim
m→∞
1
m
m

i=1
ℓi(ψ) = ¯ℓ(ψ)
for all ψ ∈Rp. We call ¯ℓ(ψ) the asymptotic conditional loss function.
Assumption (A2) implies that we preserve the essential composition of the portfolio
as we allow it to grow (see, for instance, Example 8.17).
(A3) There is some C < ∞such that m
i=1(ei/i)2 < C for all m.
This assumption prevents exposures from growing systematically with portfolio
size.
The following result shows that under these assumptions the average portfolio
loss is essentially determined by the asymptotic conditional loss function ¯ℓand the
realization of the factor random vector Ψ . The proof is based on a suitable version
of the strong law of large numbers (see Frey and McNeil (2003) for details).
Proposition 8.15. Consider a sequence L(m) = m
i=1 Li satisfying Assumptions (A1)–(A3) above. Denote by P( · | Ψ = ψ) the conditional distribution of
the sequence (Li)i∈N given Ψ = ψ. Then
lim
m→∞
1
mL(m) = ¯ℓ(ψ),
P( · | Ψ = ψ) a.s.
Proposition 8.15 obviously applies to the number of defaults M(m) = m
i=1 Yi
if we set δi = ei ≡1. For a given sequence (Yi)i∈N following a p-factor Bernoulli
mixture model with default probabilities pi(ψ), Assumptions (A1) and (A3) are
automatically satisﬁed and (A2) becomes
lim
m→∞
1
m
m

i=1
pi(ψ) = ¯p(ψ)
for some function ¯p : Rp →[0, 1].
(8.41)
--- page 375 ---

8.4. The Mixture Model Approach
359
For one-factor Bernoulli mixture models we can obtain a stronger result which
links the quantiles of L(m) to quantiles of the mixing distribution. Again we refer to
Frey and McNeil (2003) for a proof.
Proposition 8.16. Consider a sequence L(m) = m
i=1 Li satisfying Assumptions (A1)–(A3) with a one-dimensional mixing variable Ψ with df G. Assume
that the conditional asymptotic loss function ¯ℓ(ψ) is strictly increasing and right
continuous and that G is strictly increasing at qα(Ψ ), i.e. that G(qα(Ψ ) + δ) > α
for every δ > 0. Then
lim
m→∞
1
mqα(L(m)) = ¯ℓ(qα(Ψ )).
(8.42)
Comments.
The assumption that ¯ℓis strictly increasing makes sense if it is assumed
that low values of Ψ correspond to good states of the world with lower conditional
default probabilities and lower losses given default than average, and that high values
of ψ correspond to bad states with correspondingly higher losses given default.
It follows from Proposition 8.16 that the tail of the credit loss in large one-factor
Bernoulli mixture models is essentially driven by the tail of the mixing variable Ψ .
Consider in particular two exchangeable Bernoulli mixture models with mixing distributions Gi(q) = P(Qi ⩽q), i = 1, 2. Suppose that the tail of G1 is heavier than
the tail of G2, i.e. that we have G1(q) < G2(q) for q close to 1. Then Proposition 8.16 implies that for large m the tail of M(m) is heavier in model 1 than in
model 2.
Example 8.17. Consider the one-factor Bernoulli mixture model for k exchangeable
groups deﬁned by (8.37). In this case equation (8.41) becomes
lim
m→∞
1
m
k

r=1
m(m)
r
h(µr + σψ) = ¯p(ψ)
for some function ¯p, which is fulﬁlled if the proportions of obligors in each
group, m(m)
r
/m, converge to ﬁxed constants λr as m →∞. Assuming unit exposures and 100% losses given default, our asymptotic conditional loss function is
¯ℓ(ψ) = ¯p(ψ) = k
r=1 λrh(µr + σψ). Since Ψ is assumed to have a standard normal distribution, (8.42) implies, for large m, that
qα(L(m)) ≈m
k

r=1
λrh(µr + σΦ−1(α)).
(8.43)
8.4.4
Threshold Models as Mixture Models
Although the mixture models of this section seem, at ﬁrst glance, to be different in
structure to the threshold models of Section 8.3, it is important to realize that the
majority of useful threshold models, including all the examples we have given, can
be represented as Bernoulli mixture models. This is a very useful insight, because
the Bernoulli mixture format has a number of advantages over the threshold format.
--- page 376 ---

360
8. Credit Risk Management
• Bernoulli mixture models lend themselves to Monte Carlo risk studies. From
the analyses of this section we obtain methods for sampling from many of
the models we have discussed, such as the t copula threshold model used in
Section 8.3.5.
• Mixture models are arguably more convenient for statistical ﬁtting purposes.
We show in Section 8.6.3 that statistical techniques for generalized linear
mixed models can be used to ﬁt mixture models to empirical default data
gathered over several time periods.
• The large-portfolio behaviour of Bernoulli mixtures can be understood in
terms of the behaviour of the distribution of the common economic factors,
as was shown in Section 8.4.3.
The following condition ensures that a threshold model can be written as a
Bernoulli mixture model.
Deﬁnition 8.18. A random vector X has a p-dimensional conditional independence
structure with conditioning variable Ψ if there is some p < m and a p-dimensional
random vector Ψ = (Ψ1, . . . , Ψp)′ such that, conditional on Ψ , the rvs X1, . . . , Xm
are independent.
Lemma 8.19. Let (X, D) be a threshold model for an m-dimensional random
vector X. If X has a p-dimensional conditional independence structure with conditioning variable Ψ , then the default indicators Yi = I{Xi⩽di1} follow a Bernoulli
mixture model with factor Ψ , where the conditional default probabilities are given
by pi(ψ) = P(Xi ⩽di1 | Ψ = ψ).
Proof. For y ∈{0, 1}m deﬁne the set B := {1 ⩽i ⩽m : yi = 1} and let
Bc = {1, . . . , m}\B. We have
P(Y = y | Ψ = ψ) = P
 %
i∈B
{Xi ⩽di1}
%
i∈Bc
{Xi > di1}
				 Ψ = ψ

=
!
i∈B
P(Xi ⩽di1 | Ψ = ψ)
!
i∈Bc
(1 −P(Xi ⩽di1 | Ψ = ψ)).
Hence, conditional on Ψ = ψ, the Yi are independent Bernoulli variables with
success probability pi(ψ) := P(Xi ⩽di1 | Ψ = ψ).
Application to normal mixtures with factor structure.
Suppose that the critical
variables X = (X1, . . . , Xm)′ have a normal mean-variance mixture distribution as
in Example 8.8 so that X = m(W) +
√
WZ for W independent of Z. Suppose also
that Z (and hence X) follows the linear factor model (8.25), so that Z = BF + ε
for a random vector F ∼Np(0, Ω), a loading matrix B ∈Rm×p, and independent,
normally distributed rvs ε1, . . . , εm, which are also independent of F. Then X has
a (p + 1)-dimensional conditional independence structure.
To see this, deﬁne the random vector Ψ = (F1, . . . , Fp, W)′ and observe that,
conditional on Ψ = ψ, X is Nm(m(w) + √wBf , wΥ )-distributed, where Υ is the
(diagonal) covariance matrix of ε. Since the covariance structure is diagonal, the
--- page 377 ---

8.4. The Mixture Model Approach
361
rvs Xi are conditionally independent. For a threshold model (X, D), the equivalent
Bernoulli mixture model is now easy to compute. The conditional default probabilities are
pi(ψ) = P(Xi ⩽di1 | Ψ = ψ) = Φ
di1 −mi(w) −√wb′
if
√wυi

,
(8.44)
where mi(w) is the ith component of m(w), bi is the ith row of B, and υi is the ith
diagonal element of Υ .
Example 8.20 (threshold model of KMV/CreditMetrics type). Consider the special case of Gaussian critical variables where X = Z and Ψ = F. If we standardize
the critical variables X1, . . . , Xn to have variance one and reparametrize the formula in terms of the individual default probabilities ¯pi and the systematic variance
component βi = b′
iΩbi = 1 −υi (see Example 8.6), we can infer from (8.44) that
pi(Ψ ) = Φ
Φ−1( ¯pi) −b′
iΨ
√1 −βi

.
(8.45)
By comparison with Example 8.12 we see that the individual stochastic default
probabilities pi(Ψ ) have a probit-normal distribution with parameters µi and σi
given by
µi = Φ−1( ¯pi)/

1 −βi
and
σ 2
i = βi/(1 −βi).
Example 8.21 (threshold model with Student t copula). Consider the special
case of multivariate t-distributed critical variables where X =
√
WZ and W ∼
Ig( 1
2ν, 1
2ν). Suppose that the margins of X1, . . . , Xm have been standardized to be
standard univariate t with ν degrees of freedom. Again writing βi for the proportion
of the variance of the critical variable Xi explained by the factors F, we infer
from (8.44) that
pi(Ψ ) = Φ
t−1
ν ( ¯pi)W −1/2 −b′
iF
√1 −βi

.
(8.46)
The formula (8.44) is the key to Monte Carlo simulation for threshold models
when the critical variables have a normal mixture distribution, particularly in a largeportfolio context. For example, rather than simulating an m-dimensional t distribution to implement the t model, one only needs to simulate a p-dimensional normal
vector F with p ≪m and an independent gamma-distributed variate V = W −1.
In the second step of the simulation one simply conducts a series of independent
Bernoulli experiments with default probabilities pi(Ψ ) to decide whether individual
companies default.
Application to Archimedean copula models.
Another class of threshold models
with an equivalent mixture representation is provided by models where the critical variables have an exchangeable LT-Archimedean copula in the sense of Definition 5.47. Consider a threshold model (X, D), where X has an exchangeable
LT-Archimedean copula C with generator φ such that φ−1 is the Laplace transform
of some df G on [0, ∞) with G(0) = 0. Let d = (d11, . . . , dm1)′ denote the ﬁrst
column of D containing the default thresholds and write (X, d) for a threshold
--- page 378 ---

362
8. Credit Risk Management
model of default with Archimedean copula dependence. Write ¯pi = P(Xi ⩽di1)
as usual and ¯p = ( ¯p1, . . . , ¯pm)′ for the vector of default probabilities.
Consider now a non-negative rv Ψ ∼G and rvs U1, . . . , Um that are conditionally
independent given Ψ with conditional distribution function P(Ui ⩽u | Ψ =
ψ) = exp(−ψφ(u)) for u ∈[0, 1]. Then Proposition 5.46 shows that U has df C.
Moreover, by Lemma 8.5, (X, d) and (U, ¯p) are two equivalent threshold models
for default. By construction U has a one-dimensional conditional independence
structure with conditioning variable Ψ and the conditional default probabilities are
given by
pi(ψ) = P(Ui ⩽¯pi | Ψ = ψ) = exp(−ψφ( ¯pi)).
(8.47)
In order to simulate from a threshold model based on an LT-Archimedean copula
we may therefore use the following efﬁcient and simple approach. In a ﬁrst step
we simulate a realization ψ of Ψ and then we conduct m independent Bernoulli
experiments with default probabilities pi(ψ) as in (8.47) to simulate a realization
of defaulting counterparties.
Example 8.22 (the Clayton copula). As an example consider the Clayton copula with generator φ(t) = t−θ −1. Suppose we wish to construct an exchangeable Bernoulli mixture model with default probability π and joint default probability π2 that is equivalent to a threshold model driven by the Clayton copula.
As mentioned in Algorithm 5.48, an rv Ψ ∼Ga(1/θ, 1) (see Section A.2.4) has
Laplace transform equal to the generator inverse φ−1(t) = (t + 1)−1/θ, so the mixing variable of the equivalent Bernoulli mixture model can be deﬁned by setting
Q = exp(−Ψ (π−θ −1)).
Using (8.23), the required value of θ to give the desired joint default probabilities
is the solution to the equation π2 = Cθ(π, π) = (2π−θ −1)−1/θ, θ > 0. It is
easily seen that π2 and, hence, the default correlation in our exchangeable Bernoulli
mixture model are increasing in θ; for θ →0 we obtain independent defaults and
for θ →∞defaults become comonotonic and default correlation tends to one.
8.4.5
Model-Theoretic Aspects of Basel II
In this section we examine how the considerations of Sections 8.4.3 and 8.4.4 have
inﬂuenced the new Basel II capital-adequacy framework, which was discussed in
more general terms in Section 1.3. Under this framework a bank is required to hold
8% of the so-called risk-weighted assets (RWA) of its credit portfolio as risk capital.
The RWA of a portfolio is given by the sum of the RWA of the individual risks in
the portfolio, i.e. RWAportfolio = m
i=1 RWAi. The quantity RWAi reﬂects exposure
size and riskiness of obligor i; it takes the form RWAi = wiei, where wi is a risk
weight and ei denotes exposure size.
Banks may choose between two options for determining the risk weight wi,
which must then be implemented for the entire portfolio. Under the simpler standardized approach, the risk weight wi is determined by the type (sovereign, bank
or corporation) and the credit rating of counterparty i. For instance, wi = 50% for
a corporation with a Moody’s rating in the range of A+ to A−. Under the more
--- page 379 ---

8.4. The Mixture Model Approach
363
advanced internal-ratings-based (IRB) approach, the risk weight takes the form
wi = (0.08)−1cδiΦ
Φ−1( ¯pi) + √ρΦ−1(0.999)
√1 −ρ

.
(8.48)
Here c is a technical adjustment factor that is of minor interest to us, ¯pi represents the
marginal default probability, and δi is the percentage loss given default of obligor i.
The parameter ρ ∈(0.12, 0.24) can be viewed as an asset correlation, as will be
explained below. Estimates for ¯pi and (under the so-called advanced IRB approach)
for δi and ei are provided by the individual bank; the adjustment factor c and, most
importantly, the value of ρ are determined by ﬁxed rules within the Basel II Accord
independently of the structure of the speciﬁc portfolio under consideration. The risk
capital to be held for counterparty i is thus given by
RCi = 0.08RWAi = cδieiΦ
Φ−1( ¯pi) + √ρΦ−1(0.999)
√1 −ρ

.
(8.49)
The interesting part of equation (8.49) is, of course, the expression involving the
standard normal df, and we now give a derivation. Consider a one-factor threshold
model of KMV/CreditMetrics type with marginal default probabilities ¯p1, . . . , ¯pm
and critical variables given by
Xi = √ρF +

1 −ρεi
(8.50)
for iid standard normal rvs F, ε1, . . . , εm. It follows from Example 8.20 that
an equivalent Bernoulli mixture model can be constructed by setting Ψ = −F
(the sign change facilitates the derivation) and conditional default probabilities
pi(Ψ ) = Φ((Φ−1( ¯pi) + √ρΨ )/√1 −ρ). Assume, moreover, that the loss given
default of the ﬁrms is deterministic and equal to δiei and that exposures are relatively homogeneous. According to Proposition 8.16, under these assumptions the
quantiles of the portfolio loss L = m
i=1 δieiYi satisfy, for m large, the asymptotic
relation
qα(L) ≈
m

i=1
δieipi(qα(Ψ )) =
m

i=1
δieiΦ
Φ−1( ¯pi) + √ρΦ−1(α)
√1 −ρ

.
For c = 1, the risk capital RCi in (8.49) can thus be considered as the asymptotic
contribution of risk i to the 99.9% VaR of the overall portfolio in a one-factor
Gaussian threshold model with asset correlation ρ.
While formula (8.48) is inﬂuenced by portfolio-theoretic considerations, the new
Basel II framework falls short of reﬂecting the true dependence structure of a bank’s
credit portfolio for a number of reasons: ﬁrst, in the Basel II framework the correlation parameter ρ is speciﬁed ad hoc by regulatory rules irrespective of “true”
asset correlations; second, the simple one-factor model (8.50) is typically an oversimpliﬁed representation of the factor structure underlying default dependence, particularly for internationally active banks; third, the rule is based on an asymptotic
result. Moreover, historical default experience for the portfolio under consideration
has no formal role to play in setting capital-adequacy standards. For these reasons
--- page 380 ---

364
8. Credit Risk Management
q
P(Q > q)
0
0.1
0.2
0.3
10−6
10−5
10−4
10−3
10−2
10−1
100
Probit-normal
Beta
Logit-normal
Clayton
Figure 8.3.
Tail of the mixing distribution of Q in four different exchangeable Bernoullimixture models: beta; probit-normal (one-factor KMV/CreditMetrics); logit-normal (Credit-
PortfolioView); Clayton. In all cases the ﬁrst two moments have the values π = 0.049 and
π2 = 0.003 13, which correspond roughly to Standard & Poor’s rating category B; the actual
parameter values can be found in Table 8.6. The horizontal line at 10−2 shows that the models
only really start to differ around the 99th percentile of the mixing distribution.
the IRB approach is heavily debated in the risk-management community, and it is
widely expected that, with improved availability of credit loss data, in the long run
regulators will permit the use of internal portfolio models for capital-adequacy purposes for credit risk, as was allowed for market risk in the 1996 Amendment of the
ﬁrst Basel Accord (see Section 1.2.2).
8.4.6
Model Risk Issues
In this section, which is complementary to Section 8.3.5, we look brieﬂy at an
aspect of model risk for Bernoulli mixture models. We consider an exchangeable
Bernoulli mixture model for a homogeneous portfolio and investigate the risk related
to the choice of mixing distribution under the constraint that the default probability π and the default correlation ρY (or equivalently π and π2) are known and
ﬁxed.
According to Proposition 8.16, the tail of M is essentially determined by the tail
of the mixing variable Q. In Figure 8.3 we plot the tail function of the probit-normal
distribution (corresponding to a one-factor KMV/CreditMetrics model), the logitnormal distribution (corresponding to CreditPortfolioView), the beta distribution
(close to CreditRisk+) and the mixture distribution (corresponding to the Clayton
copula; see Example 8.22). The plots are shown on a logarithmic scale and in all
cases the ﬁrst two moments have the values π = 0.049 and π2 = 0.003 13, which
correspond roughly to Standard & Poor’s rating category B; the parameter values
for each of the models can be found in Table 8.6.
Inspection of Figure 8.3 shows that the tail functions differ signiﬁcantly only after
the 99% quantile, the logit-normal distribution being the one with the heaviest tail.
--- page 381 ---

8.4. The Mixture Model Approach
365
Table 8.6.
Parameter values for various exchangeable Bernoulli mixture models with identical values of π and π2 (and ρY ). The values of π and π2 correspond roughly to Standard &
Poor’s ratings CCC, B and BB (in fact, they have been estimated from 20 years of Standard
& Poor’s default data using the simple moment estimator in (8.61)). This table is used in the
model-risk study of Section 8.4.6 and the simulation study of Section 8.6.2.
Model
Parameter
CCC
B
BB
All models
π
0.188
0.049
0.011 2
π2
0.042
0.003 13
0.000 197
ρY
0.0446
0.015 7
0.006 43
Beta
a
4.02
3.08
1.73
b
17.4
59.8
153
Probit-normal
µ
−0.93
−1.71
−2.37
σ
0.316
0.264
0.272
Logit-normal
µ
−1.56
−3.1
−4.71
σ
0.553
0.556
0.691
Clayton
π
0.188
0.049
0.0112
θ
0.0704
0.032
0.0247
From a practical point of view this means that the particular parametric form of the
mixing distribution in a Bernoulli mixture model is of minor importance once π
and ρY have been ﬁxed. Of course this does not mean that Bernoulli mixtures are
immune to model risk; the tail of M is quite sensitive to π and in particular to ρY ,
and these parameters are not easily estimated (see Section 8.6.4 for a discussion of
statistical inference for mixture models).
Systematic recovery risk.
Another important source of model risk in credit risk
management models is the modelling of loss given default or equivalently of the
recovery rates. In standard portfolio risk models it is assumed that the loss given
default is independent of the default event. However, one expects the loss given
default to depend on the same risk factors as default probabilities; in that case
we speak of systematic recovery risk. The presence of systematic recovery risk is
conﬁrmed in a number of empirical studies. In particular, Frye (2000) has carried
out a formal empirical analysis using recovery data collected by Moody’s on rated
corporate bonds. He found that recovery rates are substantially lower than average
in times of economic recession. To quote from his paper:
Using that data [the Moody’s data] to estimate an appropriate credit
model, we can extrapolate that in a severe economic downturn recoveries might decline 20–25 percentage points from the normal-year average. This could cause loss given default to increase by nearly 100% and
to have a similar effect on economic capital. Such systematic recovery
risk is absent from ﬁrst-generation credit risk models. Therefore these
models may signiﬁcantly understate the capital required at banking
institutions.
