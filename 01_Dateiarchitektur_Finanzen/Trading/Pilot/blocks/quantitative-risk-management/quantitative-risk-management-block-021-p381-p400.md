# Quantitative Risk Management_ Concepts, Techniques, and -- Alexander J_ McNeil, Rüdiger Frey, Paul Embrechts -- Princeton series in finance, -- isbn13 9780691122557 -- 478a0059673fecd0c76229cd3d8884e7 -- Anna’s Arc.pdf — pages 381–400

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
--- page 382 ---

366
8. Credit Risk Management
Clearly, this calls for the inclusion of systematic recovery risk in standard credit risk
models. The challenge is not in building models allowing for systematic recovery
risk—this can be accomplished easily in the framework of Section 8.4.3—but in
estimating the dependence of the loss given default δi on the economic factors. At
present there are few empirical studies dealing with recovery risk; a good survey is
Schuermann (2003).
Notes and Comments
The logit-normal mixture model can be thought of as a one-factor version of the
CreditPortfolioView model of Wilson (1997a,b). Details of this model can be found
in Section 5 of Crouhy, Galai and Mark (2000). Further details of the beta binomial
distribution can be found in Joe (1997).
The rating agency Moody’s uses a so-called binomial expansion technique to
model default dependence in a simplistic way. The method, which is very popular
with practitioners, is not based on a formal default risk model, but is related to
binomial distributions. The basic idea is to approximate a portfolio of m dependent
counterparties by a homogeneous portfolio of d < m independent counterparties
with adjusted exposures and identical default probabilities; the index d is called the
diversity score and is chosen according to rules deﬁned by Moody’s. For further
information we refer to Davis and Lo (2001) and Section 9.2.7 of Lando (2004).
A comprehensive description of CreditRisk+ is given in the original manual for
CreditRisk+ (Credit Suisse Financial Products 1997). An excellent discussion of
the model structure from a more academic viewpoint is provided in Gordy (2000).
Both sources also provide further information on the calibration of the factor variances σi and factor weights wij. The derivation of recursion formulas for the probabilities P( ˜M = k), k = 0, 1, . . . , via Panjer recursion is given in Appendix A10
of CreditRisk+ (Credit Suisse Financial Products 1997). In Gordy (2002) an alternative approach to the computation of the loss distribution in CreditRisk+ is
proposed—one which uses the saddle-point approximation (see, for instance, Jensen
1995). Further numerical work for CreditRisk+ can be found in papers by Kurth
and Tasche (2003), Glasserman (2003b) and Haaf, Reiss and Schoenmakers (2004).
Importance-sampling techniques for CreditRisk+ are discussed in Glasserman and
Li (2003b). In Frey and McNeil (2002) it is shown that the Bernoulli mixture model
corresponding to a one-factor exchangeable version of CreditRisk+ is very close to
an exchangeable Bernoulli mixture model with beta mixing distribution.
The results in Section 8.4.3 are taken from Frey and McNeil (2003); related results
have been derived by Gordy (2001). The ﬁrst limit result for large portfolios was
obtained in Vasicek (1997) for a probit-normal mixture model equivalent to the
KMV model. Asymptotic results for credit portfolios related to the theory of large
deviations are discussed in Dembo, Deuschel and Dufﬁe (2004).
The equivalence between threshold models and mixture models has been observed
by Koyluoglu and Hickman (1998) and Gordy (2000) for the special case of Credit-
Metrics and CreditRisk+. Applications of Proposition 5.46 to credit risk modelling
--- page 383 ---

8.5. Monte Carlo Methods
367
are also discussed in Sch¨onbucher (2002). It is of course possible to develop multistate mixture models to describe credit migrations as well as defaults and to derive
equivalence results between multi-state latent threshold models and multi-state mixture models; see, for instance, Section 4.4 of Frey and McNeil (2001) for an application to credit risk and Joe (1997) for mathematical background information. The
study of mixture representations for sequences of exchangeable Bernoulli rvs is
related to a well-known result of de Finetti, which states that any inﬁnite sequence
Y1, Y2, . . . of exchangeable Bernoulli rvs has a representation as an exchangeable
Bernoulli mixture; see, for instance, Theorem 35.10 in Billingsley (1995) for a
precise statement. Hence any exchangeable model for Y that can be extended to
arbitrary portfolio size m has a representation as an exchangeable Bernoulli mixture
model.
For details of the IRB approach, and the Basel II Capital Accord in general, we
refer to the website of the Basel Committee: www.bis.org/bcbs. Our discussion in
Section 8.4.5 is related to the analysis by Gordy (2001).
8.5
Monte Carlo Methods
In this section we consider a Bernoulli mixture model for a loan portfolio and assume
that the overall loss is of the form L = m
i=1 Li, where the Li are conditionally independent given some economic factor vector Ψ . A possible method for calculating
risk measures and related quantities such as capital allocations is to use Monte Carlo
(MC) simulation, although the problem of rare-event simulation arises. Suppose,
for example, that we wish to compute expected shortfall and expected shortfall
contributions at the conﬁdence level α for our portfolio. We need to evaluate the
conditional expectations
E(L | L ⩾qα(L))
and
E(Li | L ⩾qα(L)).
(8.51)
If α = 0.99, say, then only 1% of our standard Monte Carlo draws will lead to a portfolio loss higher than q0.99(L). The standard MC estimator of (8.51), which consists
of averaging the simulated values of L or Li over all draws leading to a simulated
portfolio loss L ⩾qα(L), will be unstable and subject to high variability, unless the
number of simulations is very large. The problem is of course that most simulations
are “wasted”, in that they lead to a value of L which is smaller than qα(L). Fortunately, there exists a variance-reduction technique known as importance sampling
(IS), which is well suited to such problems.
8.5.1
Basics of Importance Sampling
Consider an rv X on some probability space (Ω, F , P) and assume that it has an
absolutely continuous df with density f . A generalization to general probability
spaces is discussed below. The problem we consider is the computation of the
expected value
θ = E(h(X)) =
 ∞
−∞
h(x)f (x) dx
(8.52)
--- page 384 ---

368
8. Credit Risk Management
for some known function h. To calculate the probability of an event we consider
a function of the form h(x) = I{x∈A} for some set A ⊂R; for expected shortfall
computation we consider functions of the form h(x) = xI{x⩾c} for some c ∈R.
Where the analytical evaluation of (8.52) is difﬁcult, due to the complexity of the
distribution of X, we can resort to an MC approach, for which we only have to be
able to simulate variates from the distribution with density f .
Algorithm 8.23 (Monte Carlo integration).
(1) Generate X1, . . . , Xn independently from density f .
(2) Compute the standard MC estimate ˆθMC
n
= (1/n) n
i=1 h(Xi).
The MC estimator converges to θ by the strong law of large numbers, but the
speed of convergence may not be particularly fast, particularly when we are dealing
with rare-event simulation.
Importance sampling is based on an alternative representation of the integral
in (8.52). Consider a second probability density g (whose support should contain
that of f ) and deﬁne the likelihood ratio r(x) by r(x) := f (x)/g(x) whenever
g(x) > 0, and r(x) = 0 otherwise. The integral (8.52) may be written in terms of
the likelihood ratio as
θ =
 ∞
−∞
h(x)r(x)g(x) dx = Eg(h(X)r(X)),
(8.53)
where Eg denotes expectation with respect to the density g. Hence we can approximate the integral with the following algorithm.
Algorithm 8.24 (importance sampling).
(1) Generate X1, . . . , Xn independently from density g.
(2) Compute the IS estimate ˆθIS
n = (1/n) n
i=1 h(Xi) r(Xi).
The density g is often termed the importance-sampling density. The art (or science) of importance sampling is in choosing an importance-sampling density such
that, for ﬁxed n, the variance of the IS estimator is considerably smaller than that of
the standard Monte Carlo estimator. In this way we can hope to obtain a prescribed
accuracy in evaluating the integral of interest using far fewer random draws than are
required in standard Monte Carlo simulation. The variances of the estimators are
given by
varg( ˆθIS
n ) = (1/n)(Eg(h(X)2r(X)2) −θ2),
var( ˆθMC
n
) = (1/n)(E(h(X)2) −θ2),
so that the aim is to make Eg(h(X)2r(X)2) small compared with E(h(X)2). In
theory, the variance of ˆθIS can be reduced to zero by choosing an optimal g. To see
this, suppose for the moment that h is non-negative and set
g∗(x) = f (x)h(x)/E(h(X)).
(8.54)
--- page 385 ---

8.5. Monte Carlo Methods
369
With this choice, the likelihood ratio becomes r(x) = E(h(X))/h(x). Hence
ˆθIS
1 = h(X1)r(X1) = E(h(X)), and the IS estimator gives the correct answer in
a single draw. In practice, it is of course impossible to choose an IS density of the
form (8.54), as this requires knowledge of the quantity E(h(X)) that one wants to
compute; nonetheless, (8.54) can provide useful guidance in choosing an IS density,
as we will see in the next section.
Consider the case of estimating a rare-event probability corresponding to
h(x) = I{x⩾c} for c signiﬁcantly larger than the mean of X. Then we have that
E(h(X)2) = P(X ⩾c) and, using (8.53), that
Eg(h(X)2r(X)2) = Eg(r(X)2; X ⩾c) = E(r(X); X ⩾c).
(8.55)
Clearly, we should try to choose g such that the likelihood ratio r(x) = f (x)/g(x)
is small for x ⩾c; in other words, we should make the event {X ⩾c} more likely
under the IS density g than it is under the original density f .
Exponential tilting.
We now describe a useful way of ﬁnding IS densities when
X is light tailed. For t ∈R we write MX(t) = E(etX) =
 ∞
−∞etxf (x) dx for the
moment-generating function of X, which we assume is ﬁnite for t ∈R. If MX(t) is
ﬁnite, we can deﬁne an IS density by gt(x) := etxf (x)/MX(t). The likelihood ratio
is rt(x) = f (x)/gt(x) = MX(t)e−tx. Deﬁne µt to be the mean of X with respect
to the density gt, i.e.
µt := Egt (X) = E(X exp(tX))/MX(t).
(8.56)
How can we choose t optimally for a particular importance-sampling problem?
We consider the case of tail probability estimation and recall from (8.55) that the
objective is to make
E(r(X); X ⩾c) = E(I{X⩾c}MX(t)e−tX)
(8.57)
small. Now observe that e−tx ⩽e−tc for x ⩾c and t ⩾0, so
E(I{X⩾c}MX(t)e−tX) ⩽MX(t)e−tc.
Instead of solving the (difﬁcult) problem of minimizing (8.57) over t, we choose
t so that this bound becomes minimal. Equivalently, we try to ﬁnd t minimizing
ln MX(t) −tc. Using (8.56) we obtain that
d
dt ln MX(t) −tc = E(X exp(tX))
MX(t)
−c = µt −c,
which suggests choosing t = t(c) as the solution of the equation µt = c, so that the
rare event {X ⩾c} becomes a normal event if we compute probabilities using the
density gt(c). A unique solution of the equation µt = c exists for all relevant values
of c. In the cases that are of interest to us this is immediately obvious from the form
of the exponentially tilted distributions, so we omit a formal proof.
Example 8.25 (exponential tilting for normal distribution). We illustrate the
concept of exponential tilting in the simple case of a standard normal rv. Suppose
--- page 386 ---

370
8. Credit Risk Management
that X ∼N(0, 1) with density φ(x). Using exponential tilting we obtain the new
density gt(x) = exp(tx)φ(x)/MX(t). The moment-generating function of X is
known to be MX(t) = exp( 1
2t2). Hence
gt(x) =
1
√
2π
exp(tx −1
2(t2 + x2)) =
1
√
2π
exp( 1
2(x −t)2),
so that, under the tilted distribution, X ∼N(t, 1). Note that in this case exponential
tilting corresponds to changing the mean of X.
An abstract view of importance sampling.
To handle the more complex application
to portfolio credit risk in the next section it helps to consider importance sampling
from a slightly more general viewpoint. Given densities f and g as above, deﬁne
probability measures P and Q by
P(A) =

A
f (x) dx
and
Q(A) =

A
g(x) dx,
A ⊂R.
With this notation, (8.53) becomes θ = EP (h(X)) = EQ(h(X)r(X)), so that r(X)
equals dP/dQ, the (measure-theoretic) density of P with respect to Q. Using this
more abstract view, exponential tilting can be applied in more general situations:
given an rv X on (Ω, F , P) such that MX(t) = EP (exp(tX)) < ∞, deﬁne the
measure Qt on (Ω, F ) by
dQt
dP = exp(tX)
MX(t) ,
i.e. Qt(A) = EP
exp(tX)
MX(t) ; A

,
and note that (dQt/dP)−1 = MX(t) exp(−tX) = rt(X). The IS algorithm remains
essentially unchanged: simulate independent realizations Xi under the measure Qt
and set ˆθIS = (1/n) n
i=1 Xirt(Xi) as before.
8.5.2
Application to Bernoulli-Mixture Models
In this section we return to the subject of credit losses and consider a portfolio loss
of the form L = m
i=1 eiYi, where the ei are deterministic, positive exposures and
the Yi are default indicators with default probabilities ¯pi. We assume that Y follows
a Bernoulli mixture model in the sense of Deﬁnition 8.10 with factor vector Ψ
and conditional default probabilities pi(Ψ ). We study the problem of estimating
exceedance probabilities θ = P(L ⩾c) for c substantially larger than E(L) using
importance sampling. This is useful for risk-management purposes, as, for c ≈
qα(L), a good importance-sampling distribution for the computation of P(L ⩾c)
also yields a substantial variance reduction for computing expected shortfall or
expected shortfall contributions.
We consider ﬁrst the situation where the default indicators Y1, . . . , Ym are independent and discuss subsequently the extension to the case of conditionally independent default indicators. Our exposition is based on Glasserman and Li (2003a).
--- page 387 ---

8.5. Monte Carlo Methods
371
Independent default indicators.
Here we use the more general IS approach outlined at the end of the previous section. Set Ω= {0, 1}m, the state space of Y. The
probability measure P is given by
P({y}) =
m
!
i=1
¯pyi
i (1 −¯pi)1−yi,
y ∈{0, 1}m.
We need to understand how this measure changes under exponential tilting using L.
The moment-generating function of L is easily calculated to be
ML(t) = E

exp

t
m

i=1
eiYi

=
m
!
i=1
E(eteiYi) =
m
!
i=1
(etei ¯pi + 1 −¯pi).
The measure Qt is given by Qt({y}) = EP (etL/ML(t); Y = y) and hence
Qt({y}) = exp(t m
i=1 eiyi)
ML(t)
P({y}) =
m
!
i=1
exp(teiyi)
exp(tei) ¯pi + 1 −¯pi
¯pyi
i (1 −¯pi)1−yi.
Deﬁnenewdefaultprobabilitiesby ¯qt,i := exp(tei) ¯pi/(exp(tei) ¯pi + 1 −¯pi).Itfollows that Qt({y}) = m
i=1 ¯qyi
t,i(1 −¯qt,i)1−yi, so that after exponential tilting the
default indicators remain independent but with new default probability ¯qt,i. Note
that ¯qt,i tends to one for t →∞and to zero for t →−∞, so that we can shift the
mean of L to any point in (0, m
i=1 ei).
In analogy with our previous discussion, for IS purposes, the optimal value of t
is chosen such that EQt (L) = c, leading to the equation m
i=1 ei ¯qt,i = c.
Conditionally independent default indicators.
The ﬁrst step in the extension of
the importance-sampling approach to conditionally independent defaults is obvious:
given a realization ψ of the economic factors, the conditional exceedance probability
θ(ψ) := P(L ⩾c | Ψ = ψ) is estimated using the approach for independent
default indicators described above. We have the following algorithm.
Algorithm 8.26 (IS for conditional loss distribution).
(1) Given ψ, calculate the conditional default probabilities pi(ψ) according to
the particular model, and solve the equation
m

i=1
ei
exp(tei)pi(ψ)
exp(tei)pi(ψ) + 1 −pi(ψ) = c;
the solution t = t(c, ψ) gives the optimal degree of tilting.
(2) Generate n1 conditional realizations of the default vector (Y1, . . . , Ym). The
defaults of the companies are simulated independently, with the default probability of the ith company given by
exp(t(c, ψ)ei)pi(ψ)
exp(t(c, ψ)ei)pi(ψ) + 1 −pi(ψ).
--- page 388 ---

372
8. Credit Risk Management
(3) Denote by ML(t, ψ) := m
i=1{exp(tei)pi(ψ) + 1 −pi(ψ)} the conditional
moment-generating function of L. From the simulated default data construct
n1 conditional realizations of L = m
i=1 eiYi and label these L(1), . . . , L(n1).
Determine the IS estimator for the conditional loss distribution:
ˆθIS,1
n1 (ψ) = ML(t(c, ψ), ψ) 1
n1
n1

j=1
I{L(j)⩾c} exp(−t(c, ψ)L(j)).
In principle, the approach discussed above also applies in the more general situation where the loss given default is random; all we need to assume is that the Li
are conditionally independent given Ψ , as in Assumption (A1) of Section 8.4.3.
However, the actual implementation can become quite involved.
IS for the distribution of the factor variables.
Suppose we now want to estimate the
unconditional probability θ = P(L ⩾c). A naive approach would be to generate
realizations of the factor vector Ψ and to estimate θ by averaging the IS estimator of
Algorithm 8.26 over these realizations. As is shown in Glasserman and Li (2003a),
this is not the best solution for large portfolios of dependent credit risks. Intuitively,
this is due to the fact that for such portfolios most of the variation in L is caused by
ﬂuctuationsoftheeconomicfactors,andwehavenotyetappliedIStothedistribution
of Ψ . For this reason we now discuss a full IS algorithm that combines IS for the
economic factor variables with Algorithm 8.26.
We consider the important case of a Bernoulli mixture model with multivariate
Gaussian factors and conditional default probabilities pi(Ψ ) for Ψ ∼Np(0, Ω),
such as the probit-normal Bernoulli mixture model described by (8.45). In this context it is natural to choose an importance-sampling density such that Ψ ∼Np(µ, Ω)
for a new mean vector µ ∈Rp, i.e. we take g as the density of Np(µ, Ω). For a
good choice of µ we expect to generate realizations of Ψ leading to high conditional
default probabilities more frequently. The corresponding likelihood ratio rµ(Ψ ) is
given by the ratio of the respective multivariate normal densities, so that
rµ(Ψ ) =
exp(−1
2Ψ ′Ω−1Ψ )
exp(−1
2(Ψ −µ)′Ω−1(Ψ −µ))
= exp(−µ′Ω−1Ψ + 1
2µ′Ω−1µ).
Essentially, this is a multivariate analogue of the exponential tilting applied to a
univariate normal distribution in Example 8.25.
Now we can describe the algorithm for full IS. At the outset we have to choose
the overall number of simulation rounds, n, the number of repetitions of conditional
IS per simulation round, n1, and the mean of the IS distribution for the factors, µ.
Whereas the value of n depends on the desired degree of precision and is best
determined in a simulation study, n1 should be taken to be fairly small.An approach
to determine a sensible value of µ is discussed below.
Algorithm 8.27 (full IS for mixture models with Gaussian factors).
(1) Generate Ψ1, . . . , Ψn ∼N(µ, Ip).
(2) For each Ψi calculate ˆθIS,1
n1 (Ψi) as in Algorithm 8.26.
--- page 389 ---

8.5. Monte Carlo Methods
373
(3) Determine the full IS estimator:
ˆθIS
n = 1
n
n

i=1
rµ(Ψi) ˆθIS,1
n1 (Ψi).
Choosing µ.
A key point in the full IS approach is the determination of a good
value for µ, which leads to a low variance of the importance-sampling estimator. Here we sketch the solution proposed by Glasserman and Li (2003a). Since
ˆθIS,1
n1 (ψ) ≈P(L ⩾c | Ψ = ψ), applying IS to the factors essentially amounts to
ﬁnding a good importance-sampling density for the function ψ →P(L ⩾c |
Ψ = ψ). Now recall from our discussion in the previous section that the optimal IS
density g∗satisﬁes
g∗(ψ) ∝P(L ⩾c | Ψ = ψ) exp(−1
2ψ′Ω−1ψ),
(8.58)
“∝” standing for “proportional to”. Sampling from that density is obviously not
feasible, as the normalizing constant involves the exceedance probability P(L ⩾c)
that we are interested in. In this situation the authors suggest using a multivariate
normal density with the same mode as g∗as an approximation to the optimal IS
density. Since a normal density attains its mode at the mean µ, this amounts to
choosing µ as the solution to the optimization problem
max
ψ
P(L ⩾c | Ψ = ψ) exp(−1
2ψ′Ω−1ψ).
(8.59)
An exact (numerical) solution of (8.59) is difﬁcult because the function P(L ⩾c |
Ψ = ψ) is usually not available in closed form. Glasserman and Li (2003a) discuss
several approaches to overcoming this difﬁculty; see their paper for details.
Notes and Comments
Our discussion of IS for credit portfolios follows Glasserman and Li (2003a) closely.
Theoretical results on the asymptotics of the IS estimator for large portfolios and
numerical case studies contained in Glasserman and Li (2003a) indicate that full
IS is a very useful tool for dealing with large Bernoulli mixture models. Merino
and Nyfeler (2003) and Kalkbrener, Lotter and Overbeck (2004) undertook related
work—the latter paper gives an interesting alternative solution to ﬁnding a reasonable IS mean µ for the factors.
For a general introduction to importance sampling we refer to the excellent textbook by Glasserman (2003a) (see also Robert and Casella 1999). For applications
of importance sampling to heavy-tailed distributions, where exponential families
cannot be applied directly, see Asmussen, Binswanger and Højgaard (2000) and
Glasserman, Heidelberger and Shahabuddin (1999).
As an alternative to simulation one can try to determine analytic approximations
for the loss distributions.Applications of the saddle-point approximation (see Jensen
1995) are discussed in Martin, Thompson and Browne (2001) and Gordy (2002).
--- page 390 ---

374
8. Credit Risk Management
8.6
Statistical Inference for Mixture Models
In this section we consider the statistical estimation of model parameters from
historical default data for the kind of mixture models described in Section 8.4. This
is quite a speciﬁc issue in the general area of statistical inference for credit risk
models and the reader seeking more general literature should consult Notes and
Comments. Before turning to statistical methods we provide a word of motivation
for the approach we take in this section.
8.6.1
Motivation
The calibration of portfolio credit risk models used in industry (such as KMV,
CreditMetrics or CreditRisk+) has, in general, not relied on the formal statistical
estimation of model parameters from historical default and migration data. There
are good reasons for this, the main one being that, particularly for higher-rated
companies, there are simply not enough relevant data on historical defaults to obtain
reliable parameter estimates by formal inference alone.
Industry approaches generally separate the problems of estimating (i) default
probabilities and (ii) additional model parameters describing the dependence of
defaults. The default probability of an individual company is usually estimated by
an appropriate historical default rate for “similar companies”, where the similarity
metric may be based on a credit-rating system (CreditMetrics) or a proprietary
measure like distance-to-default (DD) in the case of KMV.
It is in the determination of other model parameters that current industry models
are much less “formally statistical”. While most industry models postulate plausible factor-model structures for the mechanism generating default dependence, the
parameters of these factor models are very often either simply “assigned” by economic arguments or determined by auxiliary factor analyses of proxy variables. To
give an example of the latter, some threshold models that equate the critical variable
with a change in asset value (in the style of Merton’s model) calibrate the factor
model by taking equity returns as a proxy for asset-value changes and ﬁtting a factor
model to equity returns.
The ad hoc nature of such approaches raises the question of how much conﬁdence
can be placed in the model parameters thus derived, and how much model risk
remains? For example, in a model of KMV/CreditMetrics type, how conﬁdent are
wethatwehavecorrectlydeterminedthesizeofthesystematicriskcomponent(8.26)
due to the factors? In Section 8.3.5 we showed that there is considerable model risk
associated with the size of the speciﬁc risk component, particularly when the tail of
a credit loss distribution is of central importance.
In this ﬁnal section of this chapter we describe methods for the pure statistical
estimation of all model parameters from default data. Currently, such an approach is
perhaps only feasible for lower-grade credit risks where historical databases contain
sufﬁcient material to estimate parameters relating to default probability as well as
parameters relating to default dependence. This picture may change as data become
more plentiful over the years. Moreover, someone who grasps the principles of
--- page 391 ---

8.6. Statistical Inference for Mixture Models
375
model ﬁtting in this section will see that current industry approaches could even be
combined with the approach of this section to yield a hybrid methodology. More
explicitly, components of the factor-model structure could be based on external
inputs from industry models, while key parameters, such as parameters governing
the overall sensitivity to systematic effects, could be statistically estimated from
historical data.
Themodelswedescribearemotivatedbytheformatofthedataweconsider,which
can be described as repeated cross-sectional data. This kind of data, comprising
observations of the default or non-default of groups of monitored companies in a
number of time periods, is readily available from rating agencies. Since the group of
companies may differ from period to period, as new companies are rated and others
default or cease to be rated, we have a cross-section of companies in each period, but
the cross-section may change from period to period. A different kind of data that we
do not consider would be panel data or repeated-measures data (particularly panels
of ratings) for individual companies that are actively followed over time.
Our examples are relatively simple, but illustrate the main ideas. In Section 8.6.2
we discuss the estimation of default probabilities and default correlations for homogeneous groups, e.g. groups with the same credit rating. In Section 8.6.3 we consider
more complicated one-factor models allowing more heterogeneity and make a link
to the important class of generalized linear mixed models (GLMMs) used in many
statistical applications; an example is given in Section 8.6.4.
8.6.2
Exchangeable Bernoulli-Mixture Models
Suppose that we observe historical default numbers over n periods of time for a
homogeneous group; typically these might be yearly data. For t = 1, . . . , n, let
mt denote the number of observed companies at the start of period t and let Mt
denote the number that defaulted during the period; the former will be treated as
ﬁxed at the outset of the period and the latter as an rv. Suppose further that within
a time period these defaults are generated by an exchangeable Bernoulli mixture
model of the kind described in Section 8.4.1. In other words, assume that, given
some mixing variable Qt taking values in (0, 1) and the cohort size mt, the number
of defaults Mt is conditionally binomially distributed and satisﬁes Mt | Qt =
q ∼B(mt, q). Further assume that the mixing variables Q1, . . . , Qn are identically
distributed. We consider two methods for estimating the fundamental parameters
of the mixing distribution π = π1, π2 and ρY (default correlation); these are the
method of moments and the maximum likelihood method.
A simple moment estimator.
For 1 ⩽t ⩽n, let Yt,1, . . . , Yt,mt be default indicators
for the mt companies in the cohort. Suppose we deﬁne the rv
Mt
k

:=

{i1,...,ik}⊂{1,...,mt}
Yt,i1 · · · Yt,ik;
(8.60)
this represents the number of possible subgroups of k obligors among the defaulting
obligors in period t (and takes the value zero when k > Mt). By taking expectations
--- page 392 ---

376
8. Credit Risk Management
in (8.60) we get
E
Mt
k

=
mt
k

πk
and hence
πk = E
Mt
k
-mt
k

.
We estimate the unknown theoretical moment πk by taking a natural empirical
average (8.61) constructed from the n years of data:
ˆπk = 1
n
n

t=1
+Mt
k
,
+mt
k
, = 1
n
n

t=1
Mt(Mt −1) · · · (Mt −k + 1)
mt(mt −1) · · · (mt −k + 1) .
(8.61)
For k = 1 we get the standard estimator of default probability
ˆπ = 1
n
n

t=1
Mt
mt
,
and ρY can obviously be estimated by taking ˆρY = ( ˆπ2 −ˆπ2)/( ˆπ −ˆπ2). The estimator is unbiased for πk and consistent as n →∞(for more details see Frey and
McNeil (2001)). Note that, for Qt random, consistency requires observations for a
large number of years; it is not sufﬁcient to observe a large pool in a single year.
Maximum likelihood estimators.
To implement a maximum likelihood (ML) procedure we assume a simple parametric form for the density of the Qt (such as beta,
logit-normal or probit-normal). The joint probability function of the default counts
M1, . . . , Mn given the cohort sizes m1, . . . , mn can then be calculated using (8.33),
under the assumption that the Qt variables in different years are independent. This
expression is then maximized with respect to the natural parameters of the mixing
distribution (i.e. a and b in the case of beta and µ and σ for the logit-normal and
probit-normal). Of course, independence may be an unrealistic assumption for the
mixing variables, due to the phenomenon of economic cycles, but the method could
then be regarded as a quasi-maximum likelihood (QML) procedure, which misspeciﬁes the serial dependence structure but correctly speciﬁes the marginal distribution
of defaults in each year and still gives reasonable parameter estimates.
In practice, it is easiest to use the beta mixing distribution, since, in this case,
given the group size mt in period t, the rv Mt has a beta-binomial distribution with
probability function given in (8.35). The likelihood to be maximized thus takes the
form
L(a, b; data) =
n
!
t=1
mt
Mt
β(a + Mt, b + mt −Mt)
β(a, b)
,
and maximization can be performed numerically with respect to a and b. For further
information about the ML method consult, as usual, Section A.3. The ML estimates
of π = π1, π2 and ρY are calculated by evaluating moments of the ﬁtted distribution
using (8.34); the formulas are given in Example 8.13.
--- page 393 ---

8.6. Statistical Inference for Mixture Models
377
A comparison of moment estimation and ML estimation.
To compare these two
approaches we conduct a simulation study summarized in Table 8.7. To generate
data in the simulation study we consider the beta, probit-normal and logit-normal
mixture models of Section 8.4.1. In any single experiment we generate 20 years of
data using parameter values that roughly correspond to one of the Standard & Poor’s
credit ratings CCC, B or BB (see Table 8.6 for the parameter values). The number of
ﬁrms mt in each of the years is generated randomly using a binomial-beta model to
give a spread of values typical of real data; the defaults are then generated using one
of the Bernoulli mixture models and estimates of π, π2 and ρY are calculated. The
experiment is repeated 5000 times and a relative root mean square error (RRMSE)
is estimated for each parameter and each method: that is, we take the square root of
the estimated MSE and divide by the true parameter value. Methods are compared
by calculating the percentage increase of the estimated RRMSE with respect to the
better method (i.e. the RRMSE minimizing method) for each parameter.
It may be concluded from Table 8.7 that the ML method is better in all but one
experiment. Surprisingly, it is better even in the experiments when it is misspeciﬁed
and the true mixing distribution is either probit-normal or logit-normal; in fact,
in these cases, it offers more of an improvement than in the beta case. This can
partly be explained by the fact that when we constrain well-behaved, unimodal
mixing distributions with densities to have the same ﬁrst and second moments,
these distributions are very similar (see Figure 8.3). Finally, we observe that the
ML method tends to outperform the moment method more as we increase the credit
quality, so that defaults become rarer.
8.6.3
Mixture Models as GLMMs
A one-factor Bernoulli mixture model.
Recall the simple one-factor model (8.36)
generalizing the exchangeable model in Section 8.4.1. Rewriting slightly, this has
the form
pi(Ψ ) = h(µ + β′xi + Ψ ),
(8.62)
where h is a link function, the vector xi contains covariates for the ith ﬁrm, such
as indicators for group membership or key balance sheet ratios, and β and µ are
model parameters. Examples of link functions include the standard normal df Φ(x)
and the logistic df (1 + exp(−x))−1. The scale parameter σ has been subsumed in
the normally distributed random variable Ψ ∼N(0, σ 2), representing a common
or systematic factor.
This model can be turned into a multiperiod model for default counts in different
periods, by considering that a series of mixing variables Ψ1, . . . , Ψn generate default
dependence in each time period t = 1, . . . , n. The default indicator Yt,i for the ith
company in time period t is assumed to be Bernoulli with default probability pt,i(Ψt)
depending on Ψt according to
pt,i(Ψt) = h(µ + x′
t,iβ + Ψt),
(8.63)
--- page 394 ---

378
8. Credit Risk Management
Table 8.7.
Each part of the table relates to a block of 5000 simulations using a particular
exchangeable Bernoulli mixture model with parameter values roughly corresponding to a
particular S&P rating class. For each parameter of interest, an estimated RRMSE is tabulated
for both estimation methods: moment estimation using (8.61) and ML estimation based on the
beta model. Methods can be compared by using , the percentage increase of the estimated
RRMSE with respect to the better method (i.e. the RRMSE minimizing method) for each
parameter. Thus, for each parameter the better method has  = 0. The table clearly shows
that MLE is better in all but one case.
Moment
MLE-beta






Group
True model
Parameter
RRMSE

RRMSE

CCC
Beta
π
0.101
0
0.101
0
CCC
Beta
π2
0.202
0
0.201
0
CCC
Beta
ρY
0.332
5
0.317
0
CCC
Probit-normal
π
0.100
0
0.100
0
CCC
Probit-normal
π2
0.205
1
0.204
0
CCC
Probit-normal
ρY
0.347
11
0.314
0
CCC
Logit-normal
π
0.101
0
0.101
0
CCC
Logit-normal
π2
0.209
1
0.208
0
CCC
Logit-normal
ρY
0.357
11
0.320
0
B
Beta
π
0.130
0
0.130
0
B
Beta
π2
0.270
0
0.269
0
B
Beta
ρY
0.396
8
0.367
0
B
Probit-normal
π
0.130
0
0.130
0
B
Probit-normal
π2
0.286
3
0.277
0
B
Probit-normal
ρY
0.434
19
0.364
0
B
Logit-normal
π
0.131
0
0.132
0
B
Logit-normal
π2
0.308
7
0.289
0
B
Logit-normal
ρY
0.493
26
0.392
0
BB
Beta
π
0.199
0
0.199
0
BB
Beta
π2
0.435
0
0.438
1
BB
Beta
ρY
0.508
7
0.476
0
BB
Probit-normal
π
0.197
0
0.197
0
BB
Probit-normal
π2
0.492
10
0.446
0
BB
Probit-normal
ρY
0.607
27
0.480
0
BB
Logit-normal
π
0.196
0
0.196
0
BB
Logit-normal
π2
0.572
24
0.462
0
BB
Logit-normal
ρY
0.752
45
0.517
0
where Ψt ∼N(0, σ 2) and xt,i are covariates for the ith company in time period t.
Moreover, the default indicators Yt,1, . . . , Yt,mt in period t are assumed to be conditionally independent given Ψt.
To complete the model we need to specify the joint distribution of Ψ1, . . . , Ψn,
and it is easiest to assume that these are iid mixing variables. To capture possible
economic cycle effects causing dependence between numbers of defaults in successive time periods one could either enter covariates at the level of xti that are known
--- page 395 ---

8.6. Statistical Inference for Mixture Models
379
to be good proxies for “state of the economy”, such as changes in GDP over the time
period, or an index like the Chicago Fed NationalActivity Index (CFNAI) in the US,
or one could consider a serially dependent time series structure for the systematic
factors (Ψt).
A one-factor Poisson mixture model.
When considering higher-grade portfolios
of companies with relatively low default risk, there may sometimes be advantages
(particularly in the stability of ﬁtting procedures) in formulating Poisson mixture
models instead of Bernoulli mixture models.A multiperiod mixture model based on
Deﬁnition 8.11 can be constructed by assuming that the default count variable ˜Yt,i for
the ith company in time period t is conditionally Poisson with rate parameter λt,i(Ψt)
depending on Ψt according to
λt,i(Ψt) = exp(µ + x′
t,iβ + Ψt),
(8.64)
with all other elements of the model as in (8.63). Again the variables ˜Yt,1, . . . , ˜Yt,mt
are assumed to be conditionally independent given Ψt.
GLMMs.
Both the multiperiod Bernoulli and Poisson mixture models in (8.63)
and (8.64) belong to a family of widely used statistical models known as generalized
linear mixed models (GLMMs). The three basic elements of such a model are as
follows.
(1) The vector of random effects. In our examples this is the vector (Ψ1, . . . , Ψn)
containing the systematic factors for each time period.
(2) A distribution from the exponential family for the conditional distribution of
the responses (Yt,i or ˜Yt,i) given the random effects. Responses are assumed to
be conditionally independent given the random effects. The Bernoulli, binomial and Poisson distributions all belong to the exponential family (see, for
example, McCullagh and Nelder 1989, p. 28).
(3) A link function relating E(Yt,i | Ψt), the mean response conditional on the
random effects, to the so-called linear predictor. In our examples the linear
predictor for Yt,i is
ηt,i(Ψt) = µ + x′
t,iβ + Ψt.
(8.65)
We have considered the so-called probit and logit link functions in the
Bernoulli case and the log-link function in the Poisson case. (Note that it
is usual in GLMMs to write the model as g(E(Yt,i | Ψt)) = ηt,i(Ψt) and to
refer to g as the link function; hence the probit link function is the quantile
function of standard normal and the link in the Poisson case (8.64) is referred
to as “log” rather than “exponential”.)
When no random effects are modelled in a GLMM, the model is simply known as a
generalized linear model or GLM. The role of the random effects in the GLMM is,
in a sense, to capture patterns of variability in the responses that cannot be explained
by the observed covariates alone, but which might be explained by additional unobserved factors. In our case, these unobserved factors are bundled into a time-period
--- page 396 ---

380
8. Credit Risk Management
effect that we loosely describe as the state of the economy in that time period;
alternatively, we refer to it as the systematic risk.
The GLMM framework allows models of much greater complexity. We can
add further random effects to obtain multi-factor mixture models. For example,
we might know the industry sector of each ﬁrm and wish to include a random
effect for sector nested inside the year effect; in this way we might capture additional variability associated with economic effects in different sectors over and
above the global variability associated with the year effect. Such models can be
considered in the GLMM framework by allowing the linear predictor in (8.65) to
take the form ηt,i(Ψt) = µ + x′
t,iβ + z′
t,iΨt for some vector of random effects
Ψt = (Ψt,1, . . . , Ψt,p)′; the vector zt,i is a known design element of the model that
picks out the random effects that are relevant to the response Yt,i. We would then
have a total of p × n random effects in the model. We may or may not want to model
serial dependence in the time series Ψ1, . . . , Ψn.
Inference for GLMMs.
Full ML inference for a GLMM is only a viable option
for the simplest models. Consider the form of the likelihood for the one-factor
models in (8.63) and (8.64). If we write pYt,i|Ψt (y | ψ) for the conditional probability
mass function of the response Yt,i (or ˜Yt,i) given Ψt, we have, for data {Yt,i : t =
1, . . . , n, i = 1, . . . , mt},
L(β, σ; data) =

· · ·
  n
!
t=1
mt
!
i=1
pYt,i|Ψt (Yt,i | ψt)

f (ψ1, . . . , ψn) dψ1 · · · dψn,
(8.66)
where f denotes the assumed joint density of the random effects. If we do not assume
independent random effects from time period to time period, then we are faced
with an n-dimensional integral (or an (n × p)-dimensional integral in multi-factor
models).Assuming iid Gaussian random effects with marginal Gaussian density fΨ ,
the likelihood (8.66) becomes
L(β, σ; data) =
n
!
t=1
 
mt
!
i=1
pYt,i|Ψt (Yt,i | ψt)fΨ (ψt) dψt

,
(8.67)
so that we have a product of one-dimensional integrals and this can be easily evaluated numerically and maximized over the unknown parameters.Alternatively, faster
approximate likelihood methods, such as penalized quasi-likelihood (PQL) and
marginal quasi-likelihood (MQL), can be used (see Notes and Comments).
Another attractive possibility is to treat inference for these models from a Bayesian
point of view and to use Markov Chain Monte Carlo (MCMC) methods to make
inference about parameters. We believe that this holds particular promise for two
main reasons. First, a Bayesian MCMC approach allows us to work with much
more complex models than can be handled in the likelihood framework, such as a
model with serially dependent random effects. Second, the Bayesian approach may
be ideal for handling the considerable parameter uncertainty that we are currently
faced with in portfolio credit risk, particularly in models for higher-rated counterparties where default data are scarce. In the Bayesian approach, prior distributions
--- page 397 ---

8.6. Statistical Inference for Mixture Models
381
are used to express opinions about parameters before data analysis; these opinions
are then updated with the help of the data and Bayes’ theorem to arrive at a posterior distribution for the parameters. This mechanism could be used to combine
the parameter information coming from non-statistical industry models with the
evidence in historical data to achieve improved model calibration.
8.6.4
One-Factor Model with Rating Effect
In this section we ﬁt a Bernoulli mixture model to annual default count data from
Standard & Poor’s for the period 1981–2000; these data may be easily reconstructed
from published default rates in Brand and Bahr (2001, Table 13, pp. 18–21). Standard & Poor’s uses the ratings AAA, AA, A, BBB, BB, B, CCC, but because the
observed one-year default rates for AAA-rated and AA-rated ﬁrms are mostly zero,
we concentrate on the rating categories A to CCC.
In our model we assume a single yearly random effect representing “state of the
economy” and treat rating category as an observed covariate for each ﬁrm in each
time period. Our model is a particular instance of the single-factor Bernoulli mixture
model in (8.63) and a multiperiod extension of the model described in Example 8.14.
We assume for simplicity that random effects in each year are iid normal, which
allows us to use the likelihood (8.67).
Since we are able to pool companies into groups by year and rating category, we
note that it is possible to reformulate the model as a binomial mixture model. Let
r = 1, . . . , 5 index the ﬁve rating categories in our study and write mt,r for the
number of followed companies in year t with rating r, and Mt,r for the number of
these that default. Our model assumption is that, conditional on Ψt (and the group
sizes), the default counts Mt,1, . . . , Mt,5 are independent and distributed in such a
way that Mt,r | Ψt = ψ ∼B(mt,r, pr(ψ)). Using the probit link the conditional
default probability of an r-rated company in year t is given by
pr(Ψt) = Φ(µr + Ψt).
(8.68)
The model may be ﬁtted under the assumption of iid random effects in each year by
straightforward maximization of the likelihood in (8.67). The parameter estimates
and obtained standard errors are given in Table 8.8, together with the estimated
default probabilities ˆπ(r) for each rating category and estimated default correlations
ˆρ(r1,r2)
Y
implied by the parameter estimates. Writing Ψ for a generic random effect
variable, the default probability for rating category r is given by
ˆπ(r) = E( ˆpr(Ψ )) =
 ∞
−∞
Φ( ˆµr + ˆσz)φ(z) dz,
1 ⩽r ⩽5,
where φ is the standard normal density. The default correlation for two ﬁrms with
ratingsr1 andr2 inthesameyeariscalculatedeasilyfromthejointdefaultprobability
for these two ﬁrms, which is
ˆπ(r1,r2)
2
= E( ˆpr11(Ψ ) ˆpr2(Ψ )) =
 ∞
−∞
Φ( ˆµr1 + ˆσz)Φ( ˆµr2 + ˆσ)φ(z) dz.
--- page 398 ---

382
8. Credit Risk Management
Table 8.8.
Maximum likelihood parameter estimates and standard errors (se) for a
one-factor Bernoulli mixture model ﬁtted to historical Standard & Poor’s one-year default
data, together with the implied estimates of default probabilities ˆπ(r) and default correlations
ˆρ(r1,r2)
Y
. The MLE of the scaling parameter σ is 0.24 with standard error 0.05. Note that we
have tabulated default correlation in absolute terms and not in percentage terms.
Parameter
A
BBB
BB
B
CCC
µr
−3.43
−2.92
−2.40
−1.69
−0.84
se (µr)
0.13
0.09
0.07
0.06
0.08
π(r)
0.000 4
0.002 3
0.009 7
0.050 3
0.207 8
ρ(r1,r2)
Y
0.000 40
0.000 77
0.001 30
0.002 19
0.003 04
A
0.000 77
0.001 49
0.002 55
0.004 35
0.006 15
BBB
0.001 30
0.002 55
0.004 40
0.007 63
0.010 81
BB
0.002 19
0.004 35
0.007 63
0.013 28
0.019 06
B
0.003 04
0.006 15
0.010 81
0.019 06
0.027 88
CCC
The default correlation is then
ˆρ(r1,r2)
Y
=
ˆπ(r1,r2)
2
−ˆπ(r1) ˆπ(r2)

( ˆπ(r1) −( ˆπ(r1))2)( ˆπ(r2) −( ˆπ(r2))2)
.
Note that the default correlations are correlations between event indicators for very
low probability events and are necessarily very small.
The model in (8.68) assumes that the variance of the systematic factor Ψt is the
same for all ﬁrms in all years. When compared with the very general Bernoulli mixture model corresponding to CreditMetrics/KMV in (8.45), we might be concerned
that the simple model considered in this section does not allow for enough heterogeneity in the variance of the systematic risk. A simple extension of the model is to
allow the variance to be different for different rating categories, that is to ﬁt a model
where pr(Ψt) = Φ(µr + σrΨt) and Ψt is a standard normally distributed random
effect. This increases the number of parameters in the model by four, but is no more
difﬁcult to ﬁt than the basic model. The maximized value of the log-likelihood in
the model with heterogeneous scaling is −2557.4, and the value in the model with
homogeneous scaling is −2557.7; a likelihood ratio test suggests that no signiﬁ-
cant improvement results from allowing heterogeneous scaling. If rating is the only
categorical variable, the simple model seems adequate but, if we had more information on the industrial and geographical sectors to which the companies belonged, it
would be natural to introduce further random effects for these sectors and to allow
more heterogeneity in the model in this way.
The implied default probability and default correlation estimates in Table 8.8 can
be a useful resource for calibrating simple credit models to homogeneous groups
deﬁned by rating. For example, to calibrate a Clayton copula to group BB we use
the inputs π(3) = 0.0097 and ρ(3,3)
Y
= 0.004 40 to determine the parameter θ of the
Clayton copula (see Example 8.22). Note also that we can now immediately use
the scaling results of Section 8.4.3 to calculate approximate risk measures for large
--- page 399 ---

8.6. Statistical Inference for Mixture Models
383
portfolios of companies that have been rated with the Standard & Poor’s system (see
Example 8.17).
Notes and Comments
The estimator (8.61) for joint default probabilities is also used in Lucas (1995) and
Nagpal and Bahar (2001), although de Servigny and Renault (2002) suggest there
may be problems with this estimator for groups with low default rates. A related
moment-style estimator has been suggested by Gordy (2000) but it appears to have
a similar performance to (8.61) (see Frey and McNeil 2003). A further paper on
default correlation estimation is Gordy and Heitﬁeld (2002).
A good overview article on generalized linear mixed models is Clayton (1996).
For generalized linear models a standard reference is McCullagh and Nelder (1989)
(see also Fahrmeir and Tutz 1994).
The analysis of Section 8.6.4 is very similar to the analysis in Frey and McNeil
(2003) (where heterogeneous variances for each rating category were assumed).
While the results reported in this book were obtained by full maximization of the
likelihood with our own code, we could also have used a number of existing software
packages for GLMMs. For example, we have veriﬁed that the glme function in the
S-PLUS correlated data library gives very similar results using the default penalized
quasi-likelihood method; for more information about penalized quasi-likelihood and
the related marginal quasi-likelihood method, see Breslow and Clayton (1993). For a
Bayesian approach to ﬁtting the model using Markov chain Monte Carlo techniques,
see McNeil and Wendin (2003); this approach allows fairly complicated models to
be ﬁtted, including models where the random effects have an autoregressive time
series structure.
Although we have only described default models it is also possible to analyse
ratingmigrationsinthegeneralizedlinearmodelframework(withorwithoutrandom
effects).A standard model is the ordered probit model, which is used without random
effects in Nickell, Perraudin andVarotto (2000) to provide evidence of time variation
in default rates attributable to macroeconomic factors; a similar message is found
in Bangia et al. (2002). Wendin and McNeil (2004) show how random effects may
be included in such models and discuss Bayesian inference.
A further strand of the literature is the modelling of rating-transition data with
Markov chain methods. Lando and Skodeberg (2002) estimate Markov chains in
continuous time from Standard & Poor’s data giving the exact dates of ratings
transitions. They ﬁnd evidence of non-Markovian behaviour in the data and raise the
issue of “ratings momentum”, whereby information about the previous rating history
of a company beyond its current rating is predictive of the risk of downgrading. See
also Chapter 4 of Lando (2004) for more information on the Markov chain approach
as well as the application of survival analysis methodology to default data.
A number of authors have looked at models with latent structure to capture the
dynamics of systematic risk; an example is Crowder, Davis and Giampieri (2005),
who use a two-state hidden Markov structure to capture periods of high and low
default risk (see also Gagliardini and Gourieroux 2005).
--- page 400 ---

384
8. Credit Risk Management
There is a huge amount of literature on the estimation of models for pricing creditrisky securities that uses mainly data on corporate bond prices as input: Chapter 7
of Dufﬁe and Singleton (2003) is a good starting point. Empirical work on the
calibration of credit risk models to loan data, on the other hand, is relatively sparse,
which is probably related to data problems. An example of the latter type of work
is Altman and Suggitt (2000).
