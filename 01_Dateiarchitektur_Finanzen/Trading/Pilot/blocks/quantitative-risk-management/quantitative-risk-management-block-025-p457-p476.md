# Quantitative Risk Management_ Concepts, Techniques, and -- Alexander J_ McNeil, Rüdiger Frey, Paul Embrechts -- Princeton series in finance, -- isbn13 9780691122557 -- 478a0059673fecd0c76229cd3d8884e7 -- Anna’s Arc.pdf — pages 457–476

--- page 457 ---

9.7. Copula Models
441
conditionally independent doubly stochastic random times with (Ft)-adapted
hazard-rate processes (γt,1), . . . , (γt,m), we can ﬁnd a random vector E with independent, unit exponentially distributed components, independent of F∞, such that
τi = inf{t ⩾0 : Γt,i ⩾Ei}. We may rewrite this as
τi = inf{t ⩾0 : 1 −exp(−Γt,i) ⩾˜Ui := 1 −exp(−Ei)}.
(9.62)
Note that ˜U = ( ˜U1, . . . , ˜Um)′ is a vector of m independent rvs with uniform margins,
so that its joint df is the m-dimensional independence copula (see Section 5.1.2).
In the copula models we generalize this construction and replace the independence
copula with some other copula; obviously, this allows for a richer dependence structure of the τi than in the case of conditionally independent default times. Deﬁning
Ui := 1 −˜Ui we may rewrite (9.62) as τi = inf{t ⩾0 : exp(−Γt,i) ⩽Ui}. To be
in line with the literature we work with this description of the τi and deﬁne copula
models in terms of the copula C of U (or equivalently the survival copula ˆC of ˜U
introduced in Section 5.1.5). We call C the conditional survival copula of the ﬁrms;
this terminology will be justiﬁed below.
Deﬁnition 9.41 (copula model for default times). Let (γt,i), . . . , (γt,m) be nonnegative, (Ft)-adapted processes such that Γt,i < ∞for all t > 0, and let C be an
m-dimensional copula. Then the random times τ1, . . . , τm follow a copula model
with marginal hazard-rate processes (γt,i), i = 1, . . . , m, and conditional survival
copula C, if there is an m-dimensional random vector U ∼C, independent of F∞,
such that
τi = inf{t ⩾0 : exp(−Γt,i) ⩽Ui},
1 ⩽i ⩽m.
(9.63)
Note that Deﬁnition 9.41 provides an obvious way to simulate a copula model of
default, provided we know how to simulate the copula C. To simulate a realization of
τ1, . . . , τm we generate a realization of the hazard-rate processes (γt,1), . . . , (γt,m)
and, independently, a realization of the random vector U; the τi are then constructed
according to (9.63).
The crucial part in setting up a copula model is the choice of the threshold copula C. Useful copulas and the resulting copula models will be discussed in the next
subsection; for the moment we merely recall that we obtain conditionally independent default times if and only if we take C to be the independence copula.
We now collect some elementary consequences of Deﬁnition 9.41. Since Ei :=
−ln(1 −Ui) ∼Exp(1), Lemma 9.12, together with (9.63), immediately yields that
each of the τi is a doubly stochastic random time with (Ft)-conditional hazard-rate
process (γt,i). Hence Mt,i := Yt,i −Γi(t ∧τi) is a martingale with respect to the
ﬁltration {Gi
t} := (Ft) ∨{Hi
t }. Unless C is the independence copula, it is, however,
not true that Mt,i is also a martingale with respect to the ﬁltration (Gt), i.e. given
default information for other obligors as well (see Section 9.8.1 for details).
At time t = 0 the marginal distribution of the τi can be computed as in the
single-ﬁrm case. We have, using iterated conditional expectations,
P(τi ⩽T ) = E(P(τi ⩽T | F∞)) = 1 −E

exp

−
 T
0
γs,i ds

.
(9.64)
--- page 458 ---

442
9. Dynamic Credit Risk Models
In particular, at time t = 0 it is possible to calibrate the model to a given term
structure of credit or CDS spreads by calibrating each of the marginal hazard-rate
processes (γs,i) using methods for the single-ﬁrm case. This is an important feature
of the model in practical applications. Note, however, that for t > 0 the conditional
distribution of τi given the default history of all obligors in the portfolio generally
differs from the conditional distribution of τi given that τi > t, so for t > 0 the
single-ﬁrm and the portfolio versions of the model differ. We discuss this point in
more detail in Section 9.8.1 below.
Next we show that the threshold copula C is in fact the survival copula of the τi
conditional on F∞. By deﬁnition we have
¯Fτi|F∞(t) := P(τi > t | F∞) = exp

−
 t
0
γs,i ds

.
Moreover, according to (9.63), τi > t if and only if Ui < ¯Fτi|F∞(t). Hence we
obtain, using the independence of U and F∞,
P(τ1 > t1, . . . , τm > tm | F∞) = P(U1 < ¯Fτ1|F∞(t1), . . . , Um < ¯Fτm|F∞(tm))
= C( ¯Fτ1|F∞(t1), . . . , ¯Fτm|F∞(tm)).
(9.65)
By Sklar’s identity for survival functions (see (5.13)), C is thus the conditional
survival copula of the τi given F∞.
Models with deterministic hazard rates.
From now on we concentrate on models
where the marginal hazard rate γi(s) is deterministic. Since dependence between
the τi can be introduced via the threshold copula C, this gives rise to interesting models. In fact, the literature on copula models focuses almost exclusively on models
with deterministic marginal hazard rates. Moreover, understanding the properties
of models with deterministic hazard rates is an important step in the analysis of
more general models with stochastic hazard rates. These models are usually studied ﬁrst under the artiﬁcial ﬁltration ( ˜Gt), with ˜Gt = F∞∨Ht, t ⩾0, for which
hazard rates are deterministic; pricing formulas with respect to the smaller ﬁltration
Gt = Ft ∨Ht, t ⩾0, are then derived using the theorem of iterated conditional
expectations.
With deterministic marginal hazard rates γi(t), the default times τi are independent of the background ﬁltration (Ft), and we may restrict our attention to the
ﬁltration (Ht), which is generated by the default indicators. Moreover, in that case
the conditional survival function with respect to F∞and the unconditional survival
functions obviously coincide: we have ¯Fi(t) = ¯Fτi|F∞(t) = exp(−Γi(t)). Hence
relation (9.65) yields
¯Fi(t1, . . . , tm) = C( ¯F1(t1), . . . , ¯Fm(tm))
(9.66)
= C

exp

−
 t
0
γ1(s) ds

, . . . , exp

−
 t
0
γm(s) ds

.
(9.67)
Relation (9.66) shows that with deterministic marginal hazard rates the conditional
survival copula C is the survival copula of the default times; (9.67) shows how this
--- page 459 ---

9.7. Copula Models
443
copula and the marginal hazard rates determine the joint survival function of the
default times. We will use both relations frequently below. From a mathematical
point of view it makes no difference whether we specify the copula and marginal
hazard rates or the joint survival function ¯F directly, because every joint survival
function ¯F with absolutely continuous marginal distributions has a unique representation of the form (9.67) (put γi(t) = −(∂/∂t) ln ¯Fi(t) and deﬁne C using Sklar’s
identity for survival functions). When deriving mathematical results we will therefore work directly with ¯F. The representation (9.67) is, however, convenient for the
calibration of the model, as will be discussed below.
Finally, a word of warning is in order: for models with stochastic hazard rates,
the unconditional survival copula of (τ1, . . . , τm) is different from the conditional
survival copula given F∞; for example, in models with conditionally independent
defaults but dependent hazard-rate processes the conditional survival copula given
F∞is the independence copula, but (τ1, . . . , τm) is obviously not a vector of independent rvs.
Static version.
It is interesting to link copula models to the static threshold models
considered in Section 8.3. Fix some horizon T > 0. Obviously, YT,i = 1 if and
only τi ⩽T , so YT follows a threshold model in the sense of Deﬁnition 8.4 with
critical variables X = (τ1, . . . , τm) and default threshold T . By (9.66) the survival
copula of (τ1, . . . , τm) equals C; if C is radially symmetric (see Deﬁnition 5.13),
C is also the copula of (τ1, . . . , τm). This is true, in particular, if C is an elliptical
copula such as the Gauss copula or the t copula. The ﬁndings of Section 8.3.5 on
the implications of the choice of C for the portfolio loss distribution thus carry
over to dynamic models. In particular, if C is an elliptical copula, increasing the
degree of dependence in the tail of C or choosing higher asset correlations leads to
a heavier-tailed distribution for MT = m
i=1 YT,i.
On calibration.
The calibration of a copula model with deterministic marginal
hazard rates for pricing purposes proceeds in two steps. Marginal risk-neutral hazard
rates are calibrated to a given term structure of credit spreads from defaultable bonds
or CDS spreads, as described in Section 9.3.3. If there is a liquid market for portfoliorelated credit derivatives, the parameters of the threshold copula C can be calibrated
to the observed prices of these products. While this is a straightforward concept, the
technical details of this procedure can be quite involved (see Notes and Comments
for references).
Otherwise one typically calibrates the copula to estimates of default correlation
over the maturity of the products to be priced; such estimates are either obtained
using asset correlations in conjunction with the multivariate version of the Merton
model introduced in Section 8.2.4, or via one of the statistical procedures described
in Section 8.6. Note that in this approach it is implicitly assumed that risk-neutral
and historical default correlations are equal, which is a strong assumption. When we
calibrate a copula model under the real-world probability measure, hazard rates are
calibrated to estimates of historical default probabilities; parameters of the copula
are again calibrated to estimates of historical default correlations.
--- page 460 ---

444
9. Dynamic Credit Risk Models
9.7.2
Factor Copula Models
In this section we consider models where the threshold vector U has a conditional
independence structure in the sense of Deﬁnition 8.18, i.e. where there is a pdimensional random vector V , p < m, such that, conditional on V , the Ui are
independent. These models are sometimes called factor copula models. Under our
assumption of deterministic marginal hazard rates γi(t), we get from (9.63) and the
conditional independence of the Ui given V that
¯F(t1, . . . , tm) = E(P(U1 ⩽¯F1(t1), . . . , Um ⩽¯Fm(tm) | V ))
= E
 m
!
i=1
P(Ui ⩽¯Fi(ti) | V )

.
(9.68)
Denote by ¯Fτi|V (t | v) the conditional survival function of τi given V = v and note
that, by construction, ¯Fτi|V (t | v) = P(Ui < ¯Fi(t) | V = v). Hence
¯F(t1, . . . , tm) = E
 m
!
i=1
¯Fτi|V (ti | V )

.
(9.69)
Denoting by GV the df of V and by gV the density (if it exists), we will sometimes
write (9.69) more explicitly as
¯F(t1, . . . , tm) =

Rp
m
!
i=1
¯Fτi|V (ti | v)GV (dv) =

Rp
m
!
i=1
¯Fτi|V (ti | v)gV (v) dv.
Note that the representation (9.69) is analogous to the representation of static
one-period threshold models with conditional independence structure as Bernoulli
mixture models, obtained in Section 8.4.4. In particular, (9.69) shows that for T
ﬁxed the default indicators follow a Bernoulli mixture model with factor vector V
and conditional default probabilities Qi(v) = 1 −¯Fτi|V (t | v). Following standard
terminology from survival analysis the unobservable vector V is sometimes termed
the frailty of the default times. As in the case of static models, the mixture-model
representation of a factor copula model is very useful. It leads to a natural interpretation of default contagion in terms of incomplete information (see Section 9.8.2
below for details). Moreover, it can be used for simulation purposes; we sketch the
algorithm below.
Algorithm 9.42 (simulation of factor copula models).
(1) Generate a realization of V .
(2) Generate independent rvs τi with df 1 −¯Fτi|V (t | V ), 1 ⩽i ⩽m. In order to
generate a sequence (Tn, ξn), Tn ⩽T , of default times up to some maturity
date, one might use recursive generation of default times (Algorithm 9.38).
The importance-sampling techniques discussed in Section 8.5 in the context of
static Bernoulli mixture models can be employed to improve the performance of
Algorithm 9.42. These techniques are particularly useful if one deals with rare-event
simulation, such as in the pricing of CDO tranches with high attachment points.
--- page 461 ---

9.7. Copula Models
445
At ﬁrst sight, the mathematical structure of factor copula models looks very similar to the structure of models with conditionally independent defaults; in particular,
the static versions of both model classes are Bernoulli mixture models. However,
the model classes differ with respect to the way information is revealed to investors
over time, which leads to completely different dynamic behaviour. In the models
with conditionally independent defaults it is assumed that the economic factor process (Ψt) is (Ft)-adapted, i.e. that its current value is known to investors at time t.
Hence a default event does not convey additional information for predicting the
default of other obligors.
In the factor copula models, on the other hand, the threshold U and the frailty V
are assumed to be unobservable. Since default probabilities depend on V , default
information such as the news that a particular obligor j has defaulted at a given
point in time t does convey additional information about the distribution of V . The
survival probabilities of the remaining obligors i̸ = j change, as they are computed
as the average of the conditional survival function ¯Fτi|V (t | v) with respect to the
conditional distribution of V given the default history Ht. The updating of the
distribution of the unobservable random vector V can lead to default contagion, as
will be discussed in more detail in Section 9.8.2 below. This comparison between
factor copula models and models with conditionally independent defaults shows
that dynamic models do possess a much richer structure than static models.
Below we consider speciﬁc examples of factor copula models. Obviously, every
continuous multivariate distribution with p-dimensional conditional independence
structure can be used to construct a factor copula model. Practically important examples include the Gauss copula CGa
P , the t copula Ct
ν,P (provided that the correlation
matrix P corresponds to a factor model, as explained in Section 3.4.1), and the LT-
Archimedean copulas discussed in Section 5.4.2. We consider certain special cases;
in particular, we derive the dynamic version of the two most important mixture models from Section 8.4, namely the probit-normal mixture model and CreditRisk+.
Example 9.43 (one-factor Gauss copula). Factor copula models based on a Gauss
copula CGa
P are frequently employed in practice. The static version of these models
corresponds to the popular CreditMetrics/KMV-type models discussed in Example 8.6. Here we compute the conditional survival functions for the one-factor case.
Let Xi = √ρiV + √1 −ρiεi, where ρi ∈(0, 1) and V , (εi)1⩽i⩽m are iid standard
normal rvs, so X ∼Nm(0, P), with (i, j)th element of P given by ρij = √ρiρj. Set
Ui = Φ(Xi), i.e. U ∼CGa
P . The conditional survival function is easy to compute.
With di(t) := Φ−1( ¯Fi(t)), we have that
¯Fτi|V (t | v) = P(Ui ⩽¯Fi(t) | V = v) = P

εi ⩽di(t) −√ρiV
√1 −ρi
				 V = v

,
leading to ¯Fτi|V (t | v) = Φ((di(t) −√ρiv)
/
(√1 −ρi)). Hence
¯F(t1, . . . , tm) =
1
√
2π

R
m
!
i=1
Φ
di(ti) −√ρiv
√1 −ρi

e−v2/2 dv,
(9.70)
--- page 462 ---

446
9. Dynamic Credit Risk Models
which is easily computed using one-dimensional numerical integration. The conditional survival functions for general mean-variance mixture copulas with factor
structure such as the t copula can be derived by an analogous computation.
In applications of a one-factor Gauss copula model to the pricing of portfolio
credit derivatives it is frequently assumed that ρi = ρ for all i. In that case the
dependence structure of the model is governed by the single parameter ρ, the copula
of (τ1, . . . , τm) is exchangeable and ρ = corr(Xi, Xj), so ρ is readily interpreted
in terms of asset correlation. This feature makes the exchangeable version of the
one-factor Gauss copula popular with practitioners. In fact, it is common practice
on CDO markets to quote prices for tranches of synthetic CDOs in terms of implied
asset correlation, i.e. to quote the value of ρ which, if plugged into an exchangeable
one-factor Gauss copula model with marginal survival probabilities calibrated to the
CDS spreads of the asset pool, yields the price of the tranche. References regarding
the technical details of this procedure can be found in Notes and Comments. In this
way, prices of CDO tranches can be made comparable across attachment points and
asset pools, in much the same way that implied volatilities are used as a common
yardstick on options markets. This is clearly convenient. Nonetheless, one should
bear in mind that the dependence structure of the default times in a portfolio is a
complex object which cannot, in general, be characterized by a single number (see,
for example, Dufﬁe (2004) for a discussion of this point).
Example 9.44 (LT-Archimedean copulas). Recall from Deﬁnition 5.47 in Chapter 5 that an LT-Archimedean copula is deﬁned in terms of a positive rv V with df
GV , Laplace–Stieltjes transform ˆGV and GV (0) = 0 using the relation
C(u1, . . . , um) = E

exp

−V
m

i=1
ˆG−1
V (ui)

.
As usual, denote by ¯Fi(ti) the marginal survival function of τi. We thus get the
following joint survival function of (τ1, . . . , τm):
¯F(t1, . . . , tm) = E
 m
!
i=1
exp{−V ˆG−1
V ( ¯Fi(ti))}

,
(9.71)
which is obviously of the general form (9.69). Recall that in the special case of
the Clayton copula with parameter θ we have V ∼Ga(1/θ, 1); explicit formulas
for ˆGV and ˆG−1
V for that case are given in Algorithm 5.48 for the simulation of LT-
Archimedean copulas. Note that LT-Archimedean copulas are in general not radially
symmetric, so the static version of a dynamic LT-Archimedean threshold copula
model with survival function (9.71) is not a threshold model with Archimedean
copula as discussed in Example 8.9. Nonetheless, default correlations in a dynamic
LT-Archimedean threshold copula model are easily computed using (9.58) and the
relation
P(τi > T, τj > T ) = ˆGV ( ˆG−1
V ( ¯Fi(T )) + ˆG−1
V ( ¯Fj(T ))),
i̸ = j.
--- page 463 ---

9.7. Copula Models
447
Example 9.45 (LT-Archimedean copulas with p-factor structure). As explained
in detail in Section 5.4.2, an LT-Archimedean copula with p-factor structure is constructed from a p-dimensional random vector V = (V1, . . . , Vp)′ with independent
strictly positive components and a matrix A ∈Rm×p with elements aij > 0 as
follows:
C(u1, . . . , um) = E
 m
!
i=1
exp(−a′
iV ˆG−1
i (ui))

,
(9.72)
where ai is the ith row of A and ˆG−1
i
is the Laplace–Stieltjes transform of the
strictly positive rv a′
iV . The joint survival function ¯F(t1, . . . , tm) of the τi is then
obtained from (9.72) by replacing ui with ¯Fi(ti). Expression (9.72) is fairly easy to
evaluate if the Laplace–Stieltjes transform of the Vi is available in closed form (see
Section 5.4.3 for details). LT-Archimedean copulas with p-factor structure are useful
factor copulas, since they allow for a more ﬂexible dependence structure between the
τi than the exchangeable standard LT-Archimedean copulas while retaining many
of the computational advantages of the latter class.
If the Vi follow a gamma distribution with mean one, the static version of a
generalized LT-Archimedean factor copula model is the popular CreditRisk+ model
discussed in Section 8.4.2. In fact, for T ﬁxed, the default indicators YT,i, 1 ⩽i ⩽m,
are conditionally independent given V with default probability
pi(V ) = 1 −¯Fτi|V (T | V ) = 1 −exp(−a′
iV ˆG−1
i ( ¯Fi(T ))).
This corresponds to the structure of CreditRisk+ as given in (8.39) with
wij :=
aij
p
j=1 aij
and
ki =

p

j=1
aij

ˆG−1
i ( ¯Fi(T )).
Notes and Comments
The ﬁrst copula model for portfolio credit risk was given by Li (2001); his model
is based on the Gauss copula. General copula models were introduced for the ﬁrst
time in Sch¨onbucher and Schubert (2001). Factor copula models for portfolio credit
risk have been studied by Laurent and Gregory (2003). Models where the threshold
copula is given by an LT-Archimedean copula with p-factor structure have been
developed by Rogge and Sch¨onbucher (2003).
We have not said much about the important topic of pricing portfolio-related
credit derivatives such as CDOs. This is mainly because, as this book goes to press,
the market for these products and the methodology for pricing them is in a state of
rapid development. Hence any summary of the current status of this topic is likely
to become outdated quickly. Given the practical relevance of the subject, we try to
compensate somewhat for this omission by brieﬂy discussing the available literature. For asset-based CDOs pricing is typically done using Monte Carlo simulation.
Semianalytic approaches for the pricing of synthetic CDOs in factor copula models
have been developed by Laurent and Gregory (2003), Hull and White (2004) and
Andersen and Sidenius (2004), among others. Laurent and Gregory exploit the conditional independence structure of factor copula models and develop methods based
--- page 464 ---

448
9. Dynamic Credit Risk Models
on Fourier analysis; Andersen and Sidenius and Hull and White propose recursive
methods.
The recent introduction of a quoted market for standardized synthetic CDO
tranches has made the calibration of copula models to observable market prices
an issue of high priority amongst ﬁnancial engineers working in credit markets.
In this context a deﬁciency of the exchangeable Gauss copula model has become
apparent: the value of the implied asset correlation ρ needed to explain observable
market quotes varies with the attachment points of the tranches; in particular, ρ is
quite high for senior mezzanine and senior tranches. This phenomenon, which is
frequently called base-correlation skew, bears some similarities to the well-known
smile and skew patterns of implied volatility on options markets (see, for example, Dumas, Fleming and Whaley 1998). Base-correlation skews on CDO markets
are discussed by McGinty et al. (2004), Andersen and Sidenius (2004) and others; the latter paper develops several extensions of the standard one-factor Gauss
copula model that can be used to explain the base-correlation skew. A comparative
analysis of copula-based CDO pricing models is done in Burtschell, Gregory and
Laurent (2005). As mentioned previously, the methodology for pricing CDOs and
related products is developing rapidly. A good place to monitor new developments
is www.defaultrisk.com/.
9.8
Default Contagion in Reduced-Form Models
In this section we discuss default contagion in reduced-form models. We begin with
a detailed analysis of default contagion in general models for dependent defaults;
information-based default contagion in factor copula models is discussed in Section 9.8.2. In Section 9.8.3 we brieﬂy look at models with interacting intensities,
where default contagion and counterparty risk are modelled explicitly.
9.8.1
Default Contagion and Default Dependence
Martingale intensities.
We start with a general result which characterizes the martingale default intensities of dependent default times. As we have seen before, when
discussing the martingale property of stochastic processes we have to be precise
about the information available to investors, or, in mathematical terms, the ﬁltration we use. Here we assume that investors only have access to the default history
of ﬁrms in the portfolio under consideration, i.e. we are interested in martingale
properties with respect to the internal ﬁltration (Ht) introduced in (9.50). Note that
Ht can be described as Ht = σ({(Tn, ξn) : Tn ⩽t}), as the sequence (Tn, ξn),
Tn ⩽t gives an alternative description of the default history up to time t. By HTn
we denote the σ-algebra of events observable up to and including the nth default
time Tn, i.e. HTn = σ({(Tj, ξj) : 1 ⩽j ⩽n}). (This coincides with the general
abstract deﬁnition of the σ-algebra of events observable up to some stopping time.)
Theorem 9.46. Consider default times τ1, . . . , τm and denote by (Ht) the corresponding internal ﬁltration. Suppose that for every 0 ⩽n ⩽m −1 and every
i ∈{1, . . . , m} there is a random mapping g(n)
i
: Ω× R+ →R+, measurable with
--- page 465 ---

9.8. Default Contagion in Reduced-Form Models
449
respect to the product σ-algebra HTn ⊗B(R+), such that
P(Tn+1−Tn ⩽s, ξn+1 = i | HTn)(ω) =
 s
0
g(n)
i
(ω, u) du,
1 ⩽i ⩽m. (9.73)
Then the martingale default intensity of (Yt,i) with respect to (Ht) is given by
λt,i(ω) =
g(n)
i
(ω, t −Tn)
P(Tn+1 > t | HTn)(ω),
Tn < t ⩽Tn+1.
(9.74)
The proof of this result is beyond the scope of this text. In Notes and Comments
we reference several texts in which a proof ofTheorem 9.46 and extensions to copula
models with stochastic marginal hazard rates can be found.
Comments.
The measurability requirement on the random function g(n)
i
simply
means that the functional form of g(n)
i
(ω, ·) depends only on the default history HTn.
We will see below that (9.73) is always satisﬁed if the vector (τ1, . . . , τm) admits a
joint density.
The form (9.74) for the martingale intensity is in fact quite natural. If investors
observe only past and present defaults, they obtain signiﬁcant new information only
at the time points T1(ω), . . . , Tm(ω). Hence we expect the martingale default intensity (λt,i) of some ﬁrm i ∈An (a surviving ﬁrm) to evolve in a deterministic fashion
for t ∈(Tn, Tn+1] and to change with the random arrival of new information at Tn+1.
Moreover, it is possible to derive a different expression for (λt,i) which resembles
more closely the common notion of an intensity as “the conditional probability of
default in the next instant”.Applying the fundamental theorem of calculus and (9.73)
we get, for t ∈[Tn, Tn+1) and arbitrary n < m,
g(n)
i
(ω, t −Tn) = lim
h→0
1
h
 t−Tn+h
t−Tn
g(n)
i
(ω, u) du
= lim
h→0
1
hP(Tn+1 ∈(t, t + h], ξn+1 = i | HTn)(ω).
Hence we get, for a surviving ﬁrm i ∈An, using (9.74),
λt,i = lim
h→0
1
hP(τi ⩽t + h | {τj > t for all j ∈An}, HTn).
(9.75)
Now note that at time t ∈[Tn, Tn+1) default information consists of HTn and the
atom B := {τj > t for all j ∈An}. If we denote by ¯Fτi|Ht (T ) := P(τi > T | Ht)
the conditional survival probability of ﬁrm i given the default history up to time t,
we thus get, on {τi > t},
λt,i = lim
h→0
1
hP(τi ⩽t + h | Ht) = −∂
∂T

T =t
¯Fτi|Ht (T ).
(9.76)
Hence λt,i gives the instantaneous conditional probability that a surviving ﬁrm
i ∈An defaults at time t given the default history of all ﬁrms in the portfolio up to
time t. Below we explain how the conditional survival ¯Fτi|Ht can be expressed in
terms of derivatives of the unconditional survival function of (τ1, . . . , τm).
--- page 466 ---

450
9. Dynamic Credit Risk Models
Remark 9.47 (martingale intensities and marginal hazard rates). Consider
random times τ1, . . . , τm following a threshold copula model with deterministic
marginal hazard rates γ1(t), . . . , γm(t) and a survival copula C admitting a density.
In this case the assumptions from Theorem 9.46 are satisﬁed. However, for t > 0 the
martingale intensity λt,i is in general different from the marginal hazard rate γi(t).
As explained earlier, this shows that Yt,i −
 t∧τ
0
γi(s) ds is an (Hi
t )-martingale but
not a martingale with respect to the full default information (Ht). To see that in
general, for t > 0, λt,i̸ = γi(t), recall from Section 9.2.1 that
γi(t) = lim
h→0
1
hP(τi ⩽t + h | τi > t).
(9.77)
Hence γi(t) gives the instantaneous default probability of ﬁrm i given τi > t,
whereas λt,i gives the instantaneous default probability given τi > t and the default
historyofallotherﬁrmsintheportfolio.Withdefaultdependencethetwoconditional
expectations will typically differ; a numeric illustration is given in Example 9.50
below. With (conditionally) independent defaults on the other hand, the additional
information about the default history of ﬁrms j̸ = i in the portfolio is of no use
in predicting the default time of ﬁrm i, and we have λt,i = γi(t), as was shown
formally in Proposition 9.39.
Conditional survival functions.
Let Tn ⩽t < Tn+1 for some 0 ⩽n ⩽m −1. We
want to compute the conditional survival function ¯Fτi|Ht for some ﬁrm i ∈An. To
simplify the notation we assume from now on that the indices have been permuted
in such a way that Ac
n = {1, . . . , n} and An = {n + 1, . . . , m}, i.e. the defaulted
ﬁrms correspond to the ﬁrst n ﬁrms in our index set. Put τ1 = (τ1, . . . , τn)′ and
τ2 = (τn+1, . . . , τm)′.Asanintermediatestepweconsider ¯Fτ2|τ1(t1, . . . , tm−n | τ1),
theconditionalsurvivalfunctionofthelastm −nﬁrmsgiventhevectorofthedefault
times of the ﬁrst n ﬁrms. We have the following lemma.
Lemma 9.48. Assume that the vector (τ1, . . . , τm) has a density. Then
¯Fτ2|τ1(t1, . . . , tm−n | τ1, . . . , τn) =
∂n
∂t1 · · · ∂tn
¯F(τ1, . . . , τn, t1, . . . , tm−n)
∂n
∂t1 · · · ∂tn
¯F(τ1, . . . , τn, 0, . . . , 0)
.
Proof. Recall that the joint density of (τ1, . . . , τm) is given by
(−1)m
∂m ¯F
∂t1 · · · ∂tm
.
Hence the result follows from the conditional density formula (3.2) for the conditional density of τ2 given τ1; we omit the details.
Finally, we turn to the conditional survival function ¯Fτi|Ht . At time t default
information consists of the vector τ1 of the default times of the ﬁrms from Ac
n and
--- page 467 ---

9.8. Default Contagion in Reduced-Form Models
451
of the atom B := {τ2 > t}. Hence we have, for i ∈{n + 1, . . . , m} and T ⩾t,
using the deﬁnition of elementary conditional expectation and Lemma 9.48, that
¯Fτi|Ht (T ) = P(τi > T | B, τ1) = P(τi > T, τ2 > t | τ1)
P(τ2 > t | τ1)
=
∂n
∂t1 · · · ∂tn
¯F(τ1, . . . , τn, t, . . . , T, . . . , t)
∂n
∂t1 · · · ∂tn
¯F(τ1, . . . , τn, t, . . . , t, . . . , t)
.
(9.78)
Combining (9.76) and (9.78) we can characterize martingale default intensities in
terms of the unconditional survival function of (τ1, . . . , τm).
Corollary 9.49. Suppose that the random vector (τ1, . . . , τm) admits a density. Let
Tn < t ⩽Tn+1, 0 ⩽n < m, and suppose that Ac
n = {1, . . . , n}. Then the martingale
default intensity of ﬁrm i ∈An with respect to (Ht) equals
λt,i = −
∂n+1
∂t1 · · · ∂tn∂ti
¯F(τ1, . . . , τn, t, . . . t)
∂n
∂t1 · · · ∂tn
¯F(τ1, . . . , τn, t, . . . , t)
.
If we have a closed-form expression for the unconditional survival function ¯F (or
equivalently for the survival copula C) of (τ1, . . . , τm), then it is straightforward,
in principle, to compute the martingale default intensities. However, Corollary 9.49
conveys little economic intuition, as it expresses martingale intensities and hence
default contagion in terms of purely mathematical objects, namely higher-order
derivatives of the unconditional survival function. Moreover, it seems difﬁcult to
use the corollary in order to build a model where default contagion follows a particular pattern. In Section 9.8.2 we will therefore study conditional survival functions
in factor copula models, where default contagion permits a natural economic interpretation in terms of incomplete information.
Applications to credit-risky securities.
It is interesting to investigate the implications of our general results for martingale intensities for the pricing of credit-risky
securities. Following the literature we use the martingale-modelling approach and
assume that under the risk-neutral measure Q used for pricing the default times,
τ1, . . . , τm follow a copula model with deterministic hazard rates γ1(t), . . . , γm(t)
and survival copula C. Moreover, we assume that the risk-free short rate r(t) ⩾0
is deterministic; B(t) = exp(
 t
0 r(s) ds) denotes the default-free savings account.
The assumption of deterministic interest rates is routinely made in the literature
on pricing portfolio credit derivatives, essentially because the impact of stochastic interest rates on prices is low compared with the impact of the assumptions on
default dependence.
We begin with the problem of pricing a ﬁrst-to-default swap.We consider a similar
contract as in Section 9.6.3. Premiums are due at times 0 < t1 < · · · < tN = T ,
provided that no default has yet occurred; if T1 < T and, moreover, ξ1 = i, there is
--- page 468 ---

452
9. Dynamic Credit Risk Models
a default payment equal to the constant li. In this set-up the value at time t = 0 of
the default payment leg equals
V def =
m

i=1
liEQ(B(τi)−1I{τi=T1}I{τi⩽T }).
If we condition on τi, we get, for a single term of this sum,
EQ(B(τi)−1I{T1=τi}I{τi⩽T }) =
 T
0
B(t)−1Q(τi = T1 | τi = t)fi(t) dt,
where fi(t) is the marginal density of τi. Now Lemma 9.48 yields
Q(τi = T1 | τi = t) = Q(τj > t for all j̸ = i | τi = t) = −
1
fi(t)
∂¯F
∂ti
(t, . . . , t),
and we obtain
V def = −
m

i=1
li
 T
0
B(t)−1 ∂¯F
∂ti
(t, . . . , t) dt.
If ¯F or, equivalently, the threshold copula C is known in closed form, this is straightforwardtocomputebyone-dimensional(numerical)integration.Notethat,bydeﬁnition, Q(T1 > t) = ¯F(tn, . . . , tn); hence the value in t = 0 of the premium payments
(assuming a generic swap spread x) is given by
V prem = x
N

n=1
B(tn)−1(tn −tn−1) ¯F(tn, . . . , tn).
Next we consider the relationship between the instantaneous credit spread and
martingale intensities. Denote by p1,i(t, T ) the price of a zero-coupon bond with
maturity T issued by ﬁrm i and assume that the recovery rate of this bond is equal
to zero. Hence the price of the bond at time t < τi is given by
p1,i(t, T ) = exp

−
 T
t
r(s) ds

Q(τi > T | Ht),
(9.79)
so that the credit spread is given by ci(t, T ) = −1/(T −t) ln Q(τi > T | Ht).
Since Q(τi > t | Ht) = 1 on {t < τi}, by (9.76), the instantaneous credit spread
ci(t) = limT →t ci(t, T ) is given by
ci(t, T ) = −∂
∂T

T =t
ln Q(τi > T | Ht) = −∂
∂T

T =t
Q(τi > T | Ht) = λt,i,
i.e. the martingale default intensity of τi under the equivalent martingale measure Q
is equal to the instantaneous credit spread of a zero-recovery bond issued by ﬁrm i.
Finally, we discuss issues related to dynamic consistency in the use of copula
models. In Section 9.7.1 we showed that at t = 0 pricing formulas for single-name
products remain valid in a portfolio model; we also mentioned that this is no longer
trueatt > 0.Herewetakeacloserlookatthisfact.Consideracorporatezero-coupon
bond with zero recovery. According to (9.79), the price of this security at t > 0 is
--- page 469 ---

9.8. Default Contagion in Reduced-Form Models
453
given by the discounted conditional survival probability of the ﬁrm given the default
history of all obligors up to time t. In a single-ﬁrm model, on the other hand, we have
p1,i(t, T ) = I{τi>t} exp(−
 T
t r(s) ds)Q(τi > T | τi > t), i.e. the price of the bond
equals the discounted conditional survival probability of ﬁrm i given only its own
default history.As discussed previously, these two conditional survival probabilities
generally differ for t > 0.
Note, however, that, while correct from a theoretical point of view, (9.79) does not
correspond to the way practitioners tend to use a copula model. In deriving (9.79)
we ﬁxed in t0 = 0 a model for the joint distribution of (τ1, . . . , τm), a model with
constant hazard rates and a Clayton survival copula with parameter θ0, say; at time
t1 > 0 we priced the bond using the conditional distribution of this model given
the default history Ht1. Practitioners typically proceed in a different way: at time t1
they calibrate a new model—in our case again a Clayton copula model but with
parameter θ1, which may be different from θ0—to the market information available
in t1 and use the new model to price the bond. In general, both approaches lead to
different distributions for the default times of surviving ﬁrms and hence to different
prices. Clearly, the second approach is inconsistent over time; however, it leads to
prices which are consistent with the available market information at any given point
in time—a property that practitioners regard as highly important.
9.8.2
Information-Based Default Contagion
Default contagion in factor copula models can be attributed to the fact that information about the default history alters the conditional distribution of the unobservable
factor vector V . In this section we make this statement precise and compute the
conditional distribution of V given the default history up to and including time t.
Moreover, we explain how the martingale default intensity at time t can be computed as expectations with respect to the conditional distribution of V . We assume
throughout that the conditional distribution of τj given V admits the density
fτj |V (t | V ) = −∂
∂t
¯Fτj |V (t | V ).
To simplify the exposition, we further assume that V admits the density gV (v). By
gV |Ht (v) we denote the conditional density of V given Ht.
Computation of gV |Ht (v).
We begin with the case t < T1. Using the deﬁnition of
elementary conditional expectation, we obtain for A ⊆Rp that
P(V ∈A | T1 > t) =
1
¯F(t, . . . , t)

A
m
!
j=1
¯Fτj |V (t | v)gV (v) dv.
Hence, for t < T1, the conditional density of V given Ht is given by
gV |Ht (v) =
m
j=1 ¯Fτj |V (t | v)
¯F(t, . . . , t)
gV (v),
t < T1.
(9.80)
--- page 470 ---

454
9. Dynamic Credit Risk Models
Now we turn to the case t ∈[T1, T2). As an intermediary step we determine the
conditional density gV |τj (v | τj). The conditional density formula (3.2) gives
gV |τj (v | τj) =
fτj |V (τj | v)gV (v)

Rp fj(τj | v)gV (v) dv =
fτj |V (τj | v)
fj(τj)
gV (v),
(9.81)
where fj(t) is the unconditional density of τj. To keep the notation simple, we
assume, as in the previous subsection, that ξ1 = 1. For t ∈[T1, T2), default information consists therefore of the default time τ1 and of the atom B := {τj > t, 2 ⩽
j ⩽m}. Now we get, for A ⊂Rp,
P(V ∈A | B, τ1) = P({V ∈A} ∩B | τ1)
P(B | τ1)
=

A
m
j=2 ¯Fτj |V (t | v)
P(B | τ1)
gV |τ1(v | τ1) dv
and
P(B | τ1) =

Rp
 m
!
j=2
¯Fτj |V (t | v)

gV |τ1(v | τ1) dv.
Hence
gV |Ht (v) =
n
j=2 ¯Fτj |V (t | v)
P(B | τ1)
fτ1|V (τ1 | v)
f1(τ1)
gV (v),
t ∈[T1, T2).
(9.82)
For t ⩾T2, the conditional density gV |Ht (v) can be determined analogously; we
omit the details. For models with Clayton threshold copula, explicit expressions for
gV |Ht (v) can be given (see Example 9.50 below).
Martingale default intensities.
In factor copula models we can give an intuitive explanation for the dynamics of martingale default intensities. Suppose for
the moment that the factor vector V is observable, so that the information available to investors is given by the artiﬁcial ﬁltration
˜
Ht = Ht ∨σ(V ), t ⩾0.
Since the τi are conditionally independent given V , by Proposition 9.39 the
martingale intensity of τi with respect to the large ﬁltration ( ˜
Ht) is given by
˜λi(t | V ) = fτi|V (t | V )/ ¯Fτi|V (t | V ). Now, it is well known that the martingale
intensity of τi with respect to the internal ﬁltration (Ht) can be computed by projection, i.e. λt,i = E(˜λi(t | V ) | Ht) (see, for example, Theorem 14 in Chapter 2 of
Br´emaud (1981)). Hence we get
λt,i :=

Rp
fτi|V (t | v)
¯Fτi|V (t | v)gV |Ht (v) dv.
(9.83)
Example 9.50 (Clayton copula model). For models with a Clayton threshold copula the conditional density gV |Ht (v) and the martingale default intensities (λt,i) can be computed explicitly. Recall that the Clayton copula with parameter θ > 0 is an LT-Archimedean copula model, as introduced in Example 9.44
with V ∼Ga(1/θ, 1). Fix θ > 0 and denote by ˆG and ˆG−1 the Laplace Stieltjes
transform of the Ga(1/θ, 1) distribution and its functional inverse. Recall that for
--- page 471 ---

9.8. Default Contagion in Reduced-Form Models
455
arbitrary α, β > 0 the density g(v; α, β) of the Ga(α, β) distribution satisﬁes
g(v; α, β) ∝vα−1 exp(−βv), where “∝” denotes “is proportional to”. As shown
in Example 9.44, in LT-Archimedean threshold copula models the conditional survival function ¯Fτi|V (t | v) equals exp(−v ˆG−1( ¯Fi(t))). Hence the density of τi given
V = v is given by
fτi|V (t | v) = −∂
∂t
¯Fτi|V (t | v) =
−fi(t)
ˆG′( ˆG−1( ¯Fi(t)))
v exp(−v ˆG−1( ¯Fi(t))).
We obtain, for t < T1, using (9.80),
gV |Ht (v) ∝v1/θ−1 exp

−v

1 +
m

i=1
ˆG−1( ¯Fi(t))

,
t < T1.
(9.84)
Hence, for t < T1, the conditional distribution of V given Ht is again a gamma
distribution but now with parameters α = 1/θ and β = 1 + m
i=1 ˆG−1( ¯Fi(t)).
Recall that the mean of a Ga(α, β) distributed rv equals α/β. Hence the conditional
mean of V given T1 > t is lower than the unconditional mean of V . This is in line
with economic intuition, since the fact that T1 > t is “good news” for the portfolio.
According to (9.81), the density of V given τ1 satisﬁes
gV |τ1(v | τ1) ∝v exp{−v ˆG−1( ¯F1(τ1))}g(v; 1/θ, 1)
= v1/θ exp{−v(1 + ˆG−1( ¯F1(τ1)))},
(9.85)
so, given τ1, V is gamma distributed with parameters α
=
1 + 1/θ and
β = 1 + ˆG−1( ¯F1(τ1)). It is instructive to look at the impact of τ1 on the mean of
the conditional distribution of V , given by (1/θ + 1)/ ˆG−1( ¯F1(τ1)). Suppose that τ1
occurs unusually early, i.e. that ¯F1(τ1) is close to one. This implies that ˆG−1( ¯F1(τ1))
is close to zero, and the mean of the conditional distribution is bigger than the
unconditional mean 1/θ. Since the conditional survival functions ¯Fτi|V (t | v) are
decreasing in v, the conditional survival probabilities of the remaining obligors are
thus decreased. A similar qualitative reasoning applies if τ1 occurs late in the sense
that ¯F1(τ1) is close to zero; obviously, in that case conditional survival probabilities
are increased.
Next we turn to the case t ∈[T1, T2). For notational simplicity again we assume
that ξ1 = 1. Using (9.82), it is easily seen that, given Ht, V follows a gamma distribution with parameters α = 1 + 1/θ and β = 1 + ˆG−1(τ1) + m
j=2 ˆG−1( ¯Fj(t)).
Note that, in T1, the conditional mean µV |Ht of V jumps upwards: we have
lim
t
<−→T1
µV |Ht =
1/θ
1 + m
j=1 ˆG−1( ¯Fj(T1))
,
µV |HT1 =
1 + 1/θ
1 + m
j=1 ˆG−1( ¯Fj(T1))
.
Finally, we compute the martingale intensity λt,i using (9.83). We obtain
˜λi(t, V ) =
−fi(t)V
ˆG′( ˆG−1( ¯Fi(t)))
so
λt,i = −fi(t)E(V | Ht)
ˆG′( ˆG−1( ¯Fi(t)))
.
--- page 472 ---

456
9. Dynamic Credit Risk Models
0
0.2
0.4
0.6
0.8
1.0
0.010
0.015
0.020
0.025
0.030
Default correlation 2%
Default correlation 0.5%
λ
Time
Figure 9.12.
Paths of the default intensity (λt) in the Clayton copula model, assuming that
the ﬁrst default time T1 equals four months. The parameters are as follows: portfolio size
m = 100; marginal default intensity γ = 0.02; one-year default correlation 2% (alternatively,
0.5%). As one would expect, a higher default correlation implies a stronger contagion effect.
The martingale default intensity is thus proportional to E(V | Ht), the conditional
mean of V given Ht. In particular, λt,i jumps upward at each successive default
time Tn and decreases gradually between defaults. This is illustrated in Figure 9.12.
9.8.3
Interacting Intensities
In copula models the dependence structure of the default times is exogenously
speciﬁed; the form of the resulting default contagion can then be computed from the
modelprimitives.Inmodelswithinteractingintensities,ontheotherhand,theimpact
of defaults on the default intensities of surviving ﬁrms is exogenously speciﬁed; the
joint distribution of the default times is then endogenously derived. This leads to
a very intuitive parametrization of counterparty risk and default dependence. The
main drawback of models with interacting intensities is the fact that the marginal
distribution of individual default times is typically not available in closed form, so
the calibration of the model to defaultable term structure data is more evolved than
in copula models.
In models with interacting intensities the martingale default intensity of ﬁrm i
belonging to a given portfolio is given by an exogenously speciﬁed function λi(t, Yt)
of time and the current state Yt of the portfolio. The dependence on the current state
of the portfolio is the major innovation of the model; in this way, counterparty
risk can be modelled explicitly. Suppose, for instance, that ﬁrm i is a commercial
bank and that ﬁrm j is a major borrower from bank i, so that we expect the conditional default probability of ﬁrm i to increase given that ﬁrm j defaults. This
can be modelled by taking λi(t, y) = ai0(t) + ai1(t)I{yj =1}(y) for non-negative
and bounded functions ai0, ai1 : [0, ∞) →R+. It is straightforward to extend the
model to stochastic default intensities of the form λi(Ψt, Yt) for some observable
background process (Ψt) (references are given in Notes and Comments).
It is convenient to model the default indicator process (Yt) in a model with interacting intensities as a time-inhomogeneous continuous-time Markov chain. In this
--- page 473 ---

9.8. Default Contagion in Reduced-Form Models
457
way the computational tools from the theory of Markov chains can be used for the
analysis and simulation of the model. Below we summarize a few essential facts
about continuous-time Markov chains; several textbooks on stochastic processes
containing a detailed discussion of continuous-time Markov chains are listed in
Notes and Comments.
Continuous-time Markov chains.
A time-inhomogeneous continuous-time Markov chain (Xt) on a ﬁnite state space S is characterized by non-negative and bounded
transition rate functions λ(t, x, y), x, y ∈S, x̸ = y, t ⩾0, with the following
interpretation. Fix t ⩾0 and let T := inf{s ⩾t : Xs̸ = Xt}, i.e. T gives the time
of the ﬁrst jump of the chain after time t. Deﬁne, for x ∈S,
λ(t, x, x) := −

y∈S,y̸=x
λ(t, x, y),
t ⩾0,
and denote by Ht := σ({Xs : s ⩽t}) the internal ﬁltration of the chain. Then
P(T > s | Ht) = P(T > s | Xt) = exp
  s
t
λ(u, Xt, Xt) du

,
s ⩾t.
(9.86)
In the special case of a time-homogeneous Markov chain where the transition rate
functions are independent of time, given Ht, the rv (T −t) (the waiting time for the
next jump after time t) is thus Exp(−λ(Xt, Xt)) distributed. Moreover, we have,
for y ∈S and T as before,
P(XT = y | Ht, T ) = −λ(T, Xt, y)/λ(T, Xt, Xt);
(9.87)
given that the chain has a jump at time t, the probability of jumping to a particular
state y is thus proportional to the transition rate λ(t, Xt−, y), where Xt−denotes the
stateofthechainimmediatelybeforethejump.Nextweintroducethegenerator G[t],
t ⩾0, of the chain (Xt). For ﬁxed t the operator G[t] associates with every function
f : S →R a new function G[t]f : S →R with
G[t]f (x) =

y∈S, y̸=x
λ(t, x, y)(f (y) −f (x)).
(9.88)
The generator is a very useful mathematical object for a number of reasons. First, it
is a well-known result that, for any f : S →R, the process
Mf
t := f (Xt) −
 t
0
G[s]f (Xs) ds,
t ⩾0,
(9.89)
is an (Ht)-martingale. Second, as explained below, the generator appears in the
Kolmogorov equations, a system of ODEs characterizing the transition probabilities
of the chain (Xt).
Construction of interacting intensities via Markov chains.
Now we turn to the
formal construction of models with interacting intensities. Set S := {0, 1}m and
deﬁne, for y ∈S and i ∈{1, . . . , m}, the state yi by yi
j = yj for j ∈{1, . . . , m} \ i
and yi
i = 1 −yi, i.e. yi is constructed from y by ﬂipping the ith coordinate. Given,
--- page 474 ---

458
9. Dynamic Credit Risk Models
for 1 ⩽i ⩽m, non-negative and bounded functions λi : [0, ∞) × S →R+ (the
candidate martingale default intensities), we deﬁne the default indicator process
(Yt) as a time-inhomogeneous continuous-time Markov chain with state space S
and transition rates
λ(t, y, x) =

I{yi=0}λi(t, y),
if x = yi for some i ∈{1 . . . , m},
0,
otherwise.
(9.90)
Relation (9.90) implies that the chain can jump only to those neighbouring states Y i
t
that differ from the current state Yt by exactly one default; in particular, there are
no joint defaults. If Yt,i = 0, the probability that ﬁrm i defaults in the small time
interval [t, t+h), i.e. the probability of jumping to the neighbouring state Y i
t in [t, t+
h), is approximately equal to hλi(t, Yt). The generator of (Yt) is given by
G[t]f (y) =
m

i=1
I{yi=0}λi(t, y)(f (t, yi) −f (t, y)),
y ∈S.
(9.91)
The deﬁnition of (Yt) suggests that (λi(t, Yt)) is the martingale default intensity of
ﬁrm i. Using (9.89), a formal proof is easy. Let fi(y) = yi, so Yt,i = fi(Yt) and
G[t]fi(y) = I{yi=0}λi(t, y). Hence
Yt,i −
 t∧τi
0
λi(s, Ys) ds = Yt,i −
 t
0
G[s]fi(Ys) ds
is a martingale by (9.89).
Transition functions and Kolmogorov equations.
The transition probabilities of
the chain (Yt) are given by
p(t, s, x, y) := P(Ys = y | Yt = x),
x, y ∈S, 0 ⩽t ⩽s < ∞.
(9.92)
It is well known that the function p(t, s, x, y) satisﬁes the Kolmogorov backward
and forward equations. These equations are very useful numerical tools in the analysis of the model. The backward equation is a system of ODEs for the function
(t, x) →p(t, s, x, y), 0 ⩽t ⩽s; s and y are considered as parameters. The
general form of the equation is (∂/∂t)p(t, s, x, y) + G[t]p(t, s, x, y) = 0, with
terminal condition p(s, s, x, y) = I{y}(x). In our model this leads to the following
system of ODEs:
∂p(t, s, x, y)
∂t
+
m

i=1
(1 −xi)λi(t, x)(p(t, s, xi, y) −p(t, s, x, y)) = 0.
The forward equation is an ODE system for the function (s, y) →p(t, s, x, y),
s ⩾t, which is governed by the adjoint operator G∗
[t] of the generator G[t]. The
derivation of the precise form of the equation is slightly more involved and we refer
to Frey and Backhaus (2004) for details.
For m small, the ODE systems corresponding to the Kolmogorov backward (and
forward) equation are easily solved numerically. Note, however, that the cardinality
of the state space equals #S = 2m, so for m large the Kolmogorov equations are no
--- page 475 ---

9.8. Default Contagion in Reduced-Form Models
459
longer useful and one has to resort to simulation.A model with interacting intensities
is easily simulated using a variant of Algorithm 9.38 (recursive default time simulation) (see, for example, Appendix C of Lando (2004) for details). Alternatively, one
may reduce the size of the state space by considering a model with a homogeneous
group structure, as will be explained below.
Models for the default intensities.
The functions λi(t, y) are an essential ingredient
in any model with interacting intensities. We therefore discuss several speciﬁcations
proposed in the literature. Jarrow and Yu (2001) study a model with stochastic
background process (Ψt), but restrict themselves to a special form of interacting
intensities called the primary–secondary framework. In this framework ﬁrms are
divided into two classes: primary and secondary. The default intensity of primary
ﬁrms depends only on (Ψt); the default intensity of secondary ﬁrms depends on (Ψt)
and on the default state of the primary ﬁrms. This simplifying assumption facilitates
the mathematical analysis of the model. Below we present a speciﬁc example from
their paper. We let m = 2 and identify (Ψt) with the short rate of interest (rt). The
default intensities are then given by
λ1(rt, Yt) = a10 + a11rt
and
λ2(rt, Yt) = a20 + a21rt + a22I{Yt,1=1},
so company one is a primary ﬁrm and company two is a secondary ﬁrm. A typical
scenario for the primary–secondary framework is as follows: primary ﬁrms correspond to large corporations; secondary ﬁrms correspond to commercial banks which
have a major credit exposure to the primary ﬁrms. Note that, under the primary–
secondary framework, cyclical default dependence, such as a situation where the
default intensity of ﬁrm i is affected by the default of ﬁrm j̸ = i, and vice versa,
cannot be modelled.
Yu (2005b) analyses a model where the whole portfolio enters an “enhanced risk
state” after the ﬁrst default. Default intensities of the form
λi(t, Yt) = a0 + a1I{Yt̸ =0},
i ∈{1, . . . , m}, a0, a1 > 0
(9.93)
are used. Hence, at the ﬁrst default time T1, the default intensities of the surviving ﬁrms jump from a0 to a0 + a1. The assumption of identical default intensities
for all ﬁrms implies that the portfolio is homogeneous, i.e. that the default times
(τ1, . . . , τm) are exchangeable.Yu suggests that for a portfolio of high-quality credits a reasonable order of magnitude for the model parameters is a0 ≈1% and
a1 ≈0.1%. Simulation studies reported in his paper indicate that the model might
be able to explain certain features of credit spreads in the market for European
telecom bonds.
Frey and Backhaus (2004) study a model where the default intensity of a given
ﬁrm depends on the overall proportion of companies that have defaulted so far. The
homogeneous-portfolio version of the model can be described as follows. Denote the
proportion of defaulted companies in state y by ¯m(y) := 1/m m
i=1 yi, for y ∈S.
Then
λi(t, Yt) = h(t, ¯m(Yt))
(9.94)
--- page 476 ---

460
9. Dynamic Credit Risk Models
for some bounded function h : R+ × [0, 1] →R+ that is increasing in its second
argument. This type of interaction between default intensities makes immediate
sense: to begin with, if a ﬁnancial institution has incurred an unusually high number
of losses in its loan portfolio, it is less likely to extend credit lines if another obligor
experiences ﬁnancial distress. Obviously, this raises the default probability of the
remaining obligors. Moreover, an unusually small number of defaults might have
a negative impact on the overall business climate. From a mathematical point of
view, if we assume that the default times (τ1, . . . , τm) are exchangeable, the default
intensities are necessarily of the form (9.94). For instance, the default intensities in
the homogeneous model (9.93) are of the form (9.94) with h(t, l) = a0 + a1I{l>0}.
Exchangeable models.
We conclude with a few results for the exchangeable
case (9.94). For default intensities of the form (9.94), the process ( ¯Mt) with
¯Mt = ¯m(Yt) is itself a Markov chain with state space ¯S = {0, 1/m, . . . , 1}. In fact,
at time t the process ¯Mt can only jump to the state ¯Mt + 1/m, which happens with
intensity m
i=1(1 −Yi(t))λi(t, Yt) = m(1 −¯Mt)h(t, ¯Mt). This shows that ( ¯Mt) is
itself a Markov chain with generator
G ¯M
[t]f (l) = m(1 −l)h(t, l)(f (l + 1/m) −f (l)).
(9.95)
Note that the state space ¯S of ( ¯Mt) is of size m + 1, whereas the state space of (Yt) is
of size 2m. Hence, under the interaction (9.94), the distribution of ¯MT can be inferred
using analytical tools such as the Kolmogorov equations, even for m relatively large.
In the exchangeable model (9.94), many quantities of interest can be easily computed
from the distribution of MT . For instance, we obtain for the default probability π
of some ﬁrm i from our portfolio π = 1/mE(MT ), and similar expressions can be
obtained for the higher-order default probabilities πk introduced in Section 8.3.1.
Finally, we present some numerical results from Frey and Backhaus (2004) that
illustrate the impact of interacting intensities on default correlations and quantiles
of
¯MT . We consider a model with a stochastic background process given by a
one-dimensional CIR square-root diffusion, as in Section 9.5.2, with parameters
κ = 0.03, ¯θ = 0.005, σ = 0.016 and initial value Ψ0 = ¯θ. These values have been
taken from the empirical study by Driessen (2005). The default intensities are given
by
h(t, ψ, ¯m) = [α(0.004 + 5.707ψ) + a1( ¯m −(1 −e−¯λt))]+.
The interpretation of this model is as follows. The number 1 −e−¯λt measures the
expected proportion of defaulted ﬁrms at time t. For a1 > 0 the default intensity
of non-defaulted companies is increased (decreased) if the proportion of defaulted
companies is higher (lower) than the expected proportion 1 −e−¯λt and we have
interaction between default events. For a1 = 0, on the other hand, we are in a
standard model with conditionally independent defaults, as studied in Section 9.6.3.
We take the horizon to be T = 1 year. In the simulations, the parameter a1, which
controls the strength of the interaction, is increased from 0 to 3; the parameter α
is adjusted in order to ensure that the one-year default probabilities P(Y1,i = 1)
remain unchanged as we vary a1. Simulation results are presented in Table 9.3 for
