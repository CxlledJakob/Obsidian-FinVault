# Quantitative Risk Management_ Concepts, Techniques, and -- Alexander J_ McNeil, Rüdiger Frey, Paul Embrechts -- Princeton series in finance, -- isbn13 9780691122557 -- 478a0059673fecd0c76229cd3d8884e7 -- Anna’s Arc.pdf — pages 248–267

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
--- page 249 ---

5.5. Fitting Copulas to Data
233
0.4
0.8
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
0.2
0.6
1.0
0.4
0.8
0 0.2
0.6
1.0
0.4
0.8
0 0.2
0.6
1.0
INTC
MSFT
GE
Figure 5.14.
Pairwise scatterplots of pseudo-sample from copula for trivariate Intel,
Microsoft and General Electric log-returns (see Example 5.57).
which differs from the usual empirical df by the use of the denominator n + 1
rather than n. This guarantees that the pseudo-copula data in (5.51) lie strictly
in the interior of the unit cube; to implement ML we must be able to evaluate
the copula density at each ˆUi, and in many cases this density is inﬁnite on the
boundary of the cube.
(3) Extreme value theory for the tails. Empirical distribution functions are known
to be poor estimators of the underlying distribution in the tails.An alternative is to
use a technique from extreme value theory, described in Section 7.2.6, whereby
the tails are modelled semiparametrically using a generalized Pareto distribution
(GPD); the body of the distribution may be modelled empirically.
Example 5.57. We analyse ﬁve years of daily log-return data (1996–2000)
for Intel, Microsoft and General Electric stocks. The marginal distributions are
estimated empirically (method (2)) and the pseudo-sample from the copula is
shown in Figure 5.14. Essentially, the points are plotted at the coordinates
(rank(Xt,i)/(n + 1), rank(Xt,j)/(n + 1)), where rank(Xt,i) denotes the rank of
Xt,i in the sample X1,i, . . . , Xn,i.
--- page 250 ---

234
5. Copulas and Dependence
5.5.3
Maximum Likelihood Estimation
Let Cθ denote a parametric copula, where θ is the vector of parameters to be estimated. The MLE is obtained by maximizing
ln L(θ; ˆU1, . . . , ˆUn) =
n

t=1
ln cθ( ˆUt)
(5.53)
with respect to θ, where cθ denotes the copula density as in (5.16) and ˆUt denotes
a pseudo-observation from the copula.
Obviously the statistical quality of the estimates of the copula parameters depends
very much on the quality of the estimates of the marginal distributions used in
the formation of the pseudo-sample from the copula. The properties of estimates
derived using the marginal estimation methods (1) and (2) in Section 5.5.2 have both
been studied in more theoretical detail. When margins are estimated parametrically
(method (1)), inference about the copula using (5.53) amounts to what has been
termed the inference-functions for margins (IFM) approach by Joe (1997). When
margins are estimated non-parametrically (method (2)), the estimates of the copula
parameters may be regarded as semiparametric and the approach has been labelled
pseudo-maximum likelihood by Genest and Rivest (1993) (see Notes and Comments
for more references). One could envisage using the two-stage method to decide on
the most appropriate copula family and then estimating all parameters (marginal
and copula) in a ﬁnal fully parametric round of estimation.
In practice, to implement the ML method we need to derive the copula density.
This is straightforward, if tedious, for the exchangeable Archimedean copulas of
Section 5.4, and these have been popular models in bivariate and trivariate applications to insurance loss data. For implicit copulas like the Gaussian and t copulas we
use (5.17). The MLE is generally found by numerical maximization of the resulting
log-likelihood (5.53).
Example 5.58 (ﬁtting the Gauss copula). In the case of a Gauss copula we
use (5.17) to see that the log-likelihood (5.53) becomes
ln L(P; ˆU1, . . . , ˆUn)
=
n

t=1
ln fP(Φ−1( ˆUt,1), . . . , Φ−1( ˆUt,d)) −
n

t=1
d

j=1
ln φ(Φ−1( ˆUt,j)),
where fΣ will be used to denote the joint density of a random vector with Nd(0, Σ)
distribution. It is clear that the second term is not relevant in the maximization with
respect to P, and the MLE is given by
ˆP = arg max
Σ∈P
n

t=1
ln fΣ(Yt),
(5.54)
where Yt,j = Φ−1( ˆUt,j) for j = 1, . . . , d and P denotes the set of all possible
linear correlation matrices. To perform this maximization in practice, note that the
--- page 251 ---

5.5. Fitting Copulas to Data
235
set P can be constructed as
P = {P = ℘(Q) : Q = AA′, A lower triangular with ones on the diagonal},
where ℘is deﬁned in (3.5). In other words, we can search over the set of unrestricted lower-triangular matrices with ones on the diagonal. This search is feasible
in low dimensions but very slow in high dimensions, since the number of parameters
is O(d2).
An approximate solution to the maximization may be obtained easily as follows.
Suppose that instead of maximizing over P as in (5.54) we maximize over the set
of all covariance matrices. This maximization problem has the analytical solution
ˆΣ = (1/n) n
t=1 YtY ′
t , which is the MLE of the covariance matrix Σ for iid normal
data with Nd(0, Σ) distribution. In practice, ˆΣ is likely to be close to being a
correlation matrix. As an approximate solution to the original problem we could
take the correlation matrix ˜P = ℘( ˆΣ).
When a Gauss copula is ﬁtted to the trivariate data in Example 5.57 by full ML,
the estimated correlation matrix has entries 0.58 (INTC-MSFT), 0.34 (INTC-GE)
and 0.40 (MSFT-GE); the value of the log-likelihood at the maximum is 376.65.
Using the alternative method gives estimates that are identical to two signiﬁcant
ﬁgures and that yield a log-likelihood value of 376.62.
A further alternative would be to use the estimation procedure in Example 5.53,
based on Spearman’s rank correlations. Using the Spearman method we get, respectively, 0.57, 0.34 and 0.40 for the parameter estimates; the value of the log-likelihood
at this value of P is 376.50, which is also not so far from the maximum.
Example 5.59 (ﬁtting the t copula). In the case of the t copula, (5.17) implies that
the log-likelihood (5.53) is
ln L(ν, P; ˆU1, . . . , ˆUn)
=
n

t=1
ln gν,P(t−1
ν ( ˆUt,1), . . . , t−1
ν ( ˆUt,d)) −
n

t=1
d

j=1
ln gν(t−1
ν ( ˆUt,j)),
where gν,P denotes the joint density of a random vector with td(ν, 0, P) distribution, P is a linear correlation matrix, gν is the density of a univariate t1(ν, 0, 1)
distribution, and t−1
ν
is the corresponding quantile function.
Again, in relatively low dimensions, we could search over the set of correlation
matrices P and degrees of freedom parameter ν for a global maximum. For higherdimensional work it would be easier to estimate P using Kendall’s tau estimates, as
in Example 5.54, and to estimate the single parameter ν by maximum likelihood.
When a t copula is ﬁtted to the trivariate data in Example 5.57 by full ML
the estimated matrix P has entries 0.59 (INTC-MSFT), 0.36 (INTC-GE) and 0.42
(MSFT-GE); the estimate of ν is 6.5 and the value of the log-likelihood at the maximum is 420.39. Using the simpler method based on Kendall’s tau gives identical
parameter estimates to two signiﬁcant ﬁgures and a log-likelihood value of 420.32.
Clearly, the t model ﬁts much better than a Gauss copula model; the log-likelihood
--- page 252 ---

236
5. Copulas and Dependence
is increased by over 40. This would be massively signiﬁcant in a likelihood ratio
test (although, strictly speaking, such a test introduces a technical difﬁculty, since
the Gauss copula represents a boundary case of the t copula model (ν = ∞), which
violates standard regularity conditions (see Notes and Comments)).
Notes and Comments
The copula estimation procedure based on empirical values of Kendall’s tau is discussed in detail for bivariate Archimedean copulas by Genest and Rivest (1993);
they explain why the procedure may be considered to be a method-of-moments
technique and show how conﬁdence intervals for the copula parameter (in the case
of single-parameter copulas) may be derived.
The method of calibrating the Gauss copula with Spearman’s rank correlation
in Example 5.53 is essentially due to Iman and Conover (1982). The use of this
calibration method to build meta-Gaussian models with prescribed margins and the
Monte Carlo simulation of data from these models is implemented in the @RISK
software (Palisade 1997), which is widely used in insurance. Our Example 5.54 is
intended to show that this approach can be extended to meta-t models, which may
well be more interesting due to their tail dependence.
The eigenvalue method for correcting the positive deﬁniteness of correlation
matrices given in Algorithm 5.55 is described by Rousseeuw and Molenberghs
(1993).Anempiricalcomparisonoftheeigenvaluemethodwithdifferentapproaches
to this problem, including so-called shrinkage methods, is found in Lindskog (2000).
The inference-functions for margins (IFM) approach to the estimation of copulas
(method (1) of Section 5.5.2 followed by maximization of (5.53)) is described by
Joe (1997), who gives asymptotic theory; the name of the approach (IFM) follows
terminology of McLeish and Small (1988).
The pseudo-likelihood approach to copula estimation (method (2) of Section 5.5.2
followed by maximization of (5.53)) is described in Genest and Rivest (1993), and
the consistency and asymptotic normality of the resulting parameter estimates are
demonstrated. In Monte Carlo simulations it is found that this method outperforms
the Kendall’s tau method for a bivariate Clayton copula (see also Genest, Ghoudi
and Rivest 1995).
Frees and Valdez (1997) discuss the relevance of copulas in actuarial applications
and give an example where copulas are ﬁtted to data using the Kendall’s tau method
and the IFM method. Also in an insurance context, Klugman and Parsa (1999)
discuss ML inference for copulas and bivariate goodness-of-ﬁt tests while Chen and
Fan (2005) describe a likelihood-ratio test for semiparametric copula selection.
The ﬁtting of the t copula to data and statistical aspects of testing this copula against the Gauss copula are discussed at length in Mashal and Zeevi (2002);
the technical problem that the Gauss copula is a boundary case of the t copula is
addressed in this paper and a correction is suggested. The authors provide a number
of ﬁnancial examples suggesting that extremal dependence is a feature of ﬁnancial data. Breymann, Dias and Embrechts (2003) ﬁt various bivariate copulas to
--- page 253 ---

5.5. Fitting Copulas to Data
237
high-frequency ﬁnancial return data at different timescales and provide extensive
comparisons with respect to goodness-of-ﬁt.
Papers developing dynamic time series models for ﬁnancial return data using
copulas include Chen and Fan (2005), Patton (2004, 2005) and Fortin and Kuzmics
(2002).
--- page 254 ---

6
Aggregate Risk
This chapter is devoted to a number of theoretical concepts in quantitative risk
management that fall under the broad heading of aggregate risk. We understand
aggregate risk as the risk of a portfolio, which could even be the entire position in
risky assets of a ﬁnancial enterprise. The material builds on general ideas in risk
measurement discussed in Section 2.2 and also uses in certain places the copula
theory of Chapter 5 and some facts about elliptical distributions from Section 3.3.
In Section 6.1 we treat the issue of measuring aggregate risk. We discuss properties that a good measure of risk should have with particular emphasis on aggregation
properties. This leads us to study the class of coherent risk measures. In Section 6.2
we consider the problem of bounding an aggregate risk if we know something about
the individual risks that contribute to the whole but have only limited information
about their dependence. We discuss speciﬁc difﬁculties that arise when risk is measured with a non-subadditive risk measure like VaR. Finally, in Section 6.3, we treat
the subject of allocating risk capital, i.e. of distributing the risk capital for a portfolio to the individual risks in the portfolio. This issue is relevant for purposes of
performance measurement, loan pricing and capital budgeting.
6.1
Coherent Measures of Risk
The premise of this section is the idea of approaching risk measurement by ﬁrst
writing down a list of properties that a good risk measure should have. Such a list
was proposed for applications in ﬁnancial risk management in the seminal paper by
Artzner et al. (1999). Using economic reasoning, they speciﬁed a number of axioms
that any so-called coherent risk measure should satisfy. Moreover, they studied the
coherence properties of widely used risk measures such asVaR or expected shortfall
and gave a characterization of all coherent risk measures in terms of generalized
scenarios. Our development of the subject will follow their approach. It should
be mentioned that the idea of axiomatic systems for risk measures bears some
relationship to similar systems for premium principles in the actuarial literature,
which have a long and independent history (see, for example, Goovaerts et al. (2003)
and further references in Notes and Comments).
6.1.1
The Axioms of Coherence
In order to introduce the axioms of coherence we have to give a formal deﬁnition
of risk measures. Fix some probability space (Ω, F , P) and a time horizon .
--- page 255 ---

6.1. Coherent Measures of Risk
239
Denote by L0(Ω, F , P) the set of all rvs on (Ω, F ), which are almost surely ﬁnite.
Financial risks are represented by a set M ⊂L0(Ω, F , P) of rvs, which we interpret
as portfolio losses over some time horizon . The time horizon is left unspeciﬁed
and will only enter when speciﬁc problems are considered. We often assume that
M is a convex cone, i.e. that L1 ∈M and L2 ∈M implies that L1 + L2 ∈M and
λL1 ∈M for every λ > 0. Risk measures are real-valued functions ϱ : M →R
deﬁned on such cones of rvs, satisfying certain properties.
We interpret ϱ(L) as the amount of capital that should be added to a position with
loss given by L, so that the position becomes acceptable to an external or internal
risk controller. Positions with ϱ(L) ⩽0 are acceptable without injection of capital;
if ϱ(L) < 0, capital may even be withdrawn. Note that our interpretation of L
differs from that in Artzner et al. (1999), where an rv L ∈M is interpreted as the
future value (instead of the loss) of a position currently held. This leads to some
sign changes in the discussion of the axioms of coherence compared with other
presentations in the literature. Also note that in order to simplify the presentation
we set interest rates equal to zero so that there is no discounting.
Now we can introduce the axioms that a risk measure ϱ : M →R on a convex
cone M should satisfy in order to be called coherent.
Axiom 6.1 (translation invariance). For all L ∈M and every l ∈R we have
ϱ(L + l) = ϱ(L) + l.
Axiom 6.1 states that by adding or subtracting a deterministic quantity l to a
position leading to the loss L we alter our capital requirements by exactly that
amount. The axiom is in fact necessary for the risk-capital interpretation of ϱ to
make sense. Consider a position with loss L and ϱ(L) > 0. Adding the amount
of capital ϱ(L) to the position leads to the adjusted loss ˜L = L −ϱ(L), with
ϱ( ˜L) = ϱ(L) −ϱ(L) = 0, so that the position ˜L is acceptable without further injection of capital.
Axiom 6.2 (subadditivity). For all L1, L2 ∈M we have ϱ(L1 + L2) ⩽ϱ(L1) +
ϱ(L2).
The rationale behind Axiom 6.2 is summarized by Arztner et al. in the statement that “a merger does not create extra risk” (ignoring of course any problematic
practical aspects of a merger!). Axiom 6.2 is the most debated of the four axioms
characterizing coherent risk measures, probably because it rules out VaR as a risk
measure in certain situations. We provide some arguments explaining why subadditivity is indeed a reasonable requirement.
• Subadditivity reﬂects the idea that risk can be reduced by diversiﬁcation, a
time-honoured principle in ﬁnance and economics. In particular, we will see
in Section 6.1.5 that the use of non-subadditive risk measures in a Markowitztype portfolio optimization problem may lead to optimal portfolios that are
very concentrated and that would be deemed quite risky by normal economic
standards.
--- page 256 ---

240
6. Aggregate Risk
• If a regulator uses a non-subadditive risk measure in determining the regulatory capital for a ﬁnancial institution, that institution has an incentive to legally
break up into various subsidiaries in order to reduce its regulatory capital
requirements. Similarly, if the risk measure used by an organized exchange
in determining the margin requirements of investors is non-subadditive, an
investor could reduce the margin he has to pay by opening a different account
for every position in his portfolio.
• Subadditivity makes decentralization of risk-management systems possible.
Consider as an example two trading desks with positions leading to losses
L1 and L2. Imagine that a risk manager wants to ensure that ϱ(L), the risk
of the overall loss L = L1 + L2, is smaller than some number M. If he
uses a risk measure ϱ, which is subadditive, he may simply choose bounds
M1 and M2 such that M1 + M2 ⩽M and impose on each of the desks the
constraint that ϱ(Li) ⩽Mi; subadditivity of ϱ then ensures automatically
that ϱ(L) ⩽M1 + M2 ⩽M.
Axiom 6.3 (positive homogeneity). For all L ∈M and every λ > 0 we have
ϱ(λL) = λϱ(L).
Axiom 6.3 is easily justiﬁed if we assume that Axiom 6.2 holds. Subadditivity
implies that, for n ∈N,
ϱ(nL) = ϱ(L + · · · + L) ⩽nϱ(L).
(6.1)
Since there is no netting or diversiﬁcation between the losses in this portfolio,
it is natural to require that equality should hold in (6.1), which leads to positive
homogeneity. Note that subadditivity and positive homogeneity imply that the risk
measure ϱ is convex on M.
Axiom 6.4 (monotonicity). For L1, L2 ∈M such that L1 ⩽L2 almost surely we
have ϱ(L1) ⩽ϱ(L2).
From an economic viewpoint this axiom is obvious: positions that lead to higher
losses in every state of the world require more risk capital.
For a risk measure satisfying Axioms 6.2 and 6.3, the monotonicity axiom is
equivalent to the requirement that ϱ(L) ⩽0 for all L ⩽0. To see this, observe
that Axiom 6.4 implies that if L ⩽0, then ϱ(L) ⩽ϱ(0) = 0; the latter equality
follows from Axiom 6.3 since ϱ(0) = ϱ(λ0) = λϱ(0) for all λ > 0. Conversely, if
L1 ⩽L2 and we assume that ϱ(L1 −L2) ⩽0, then ϱ(L1) = ϱ(L1 −L2 + L2) ⩽
ϱ(L1 −L2) + ϱ(L2) by Axiom 6.2, which implies that ϱ(L1) ⩽ϱ(L2).
Deﬁnition 6.5 (coherent risk measure). A risk measure ϱ whose domain includes
the convex cone M is called coherent (on M) if it satisﬁes Axioms 6.1–6.4.
Note that the domain is an integral part of the deﬁnition of a coherent risk measure.
We will often encounter functionals on L0(Ω, F , P), which are coherent only if
restricted to a sufﬁciently small convex cone M.
--- page 257 ---

6.1. Coherent Measures of Risk
241
Remark 6.6 (convex measures of risk). Axiom 6.3 (positive homogeneity) has
been criticized and, in particular, it has been suggested that for large values of the
multiplier λ we should have ϱ(λL) > λϱ(L) to penalize a concentration of risk and
the ensuing liquidity problems.As shown in (6.1), this is impossible for a subadditive
risk measure. This problem has led to the study of the larger class of convex risk
measures. In this class the conditions of subadditivity and positive homogeneity have
been relaxed; instead one requires only the weaker property of convexity, i.e. for all
L1, L2 ∈M:
ϱ(λL1 + (1 −λ)L2) ⩽λϱ(L1) + (1 −λ)ϱ(L2),
λ ∈[0, 1].
(6.2)
The economic justiﬁcation of (6.2) is again the idea that diversiﬁcation reduces
risk. Within the class of convex risk measures it is possible to ﬁnd risk measures
penalizing concentration of risk in the sense that ϱ(λL) ⩾ϱ(L) for λ > 1. Convex
risk measures have recently attracted a lot of attention: some references are provided
in Notes and Comments.
In the following sections we study the coherence properties of several popular
risk measures.
6.1.2
Value-at-Risk
It is immediately seen from the representation of VaR as a quantile of the loss
distribution in Section 2.2.2 that VaR is translation invariant, positive homogeneous
and monotone on L0(Ω, F , P). However, as the following example shows, the
subadditivity property (Axiom 6.2) fails to hold for VaR in general, so VaR is not a
coherent risk measure.
Example 6.7 (VaR for a portfolio of defaultable bonds). Consider a portfolio of
d = 100 defaultable corporate bonds. We assume that defaults of different bonds are
independent; the default probability is identical for all bonds and is equal to 2%. The
current price of the bonds is 100. If there is no default, a bond pays in t + 1 (one year
from now, say) an amount of 105; otherwise there is no repayment. Hence Li, the
loss of bond i, is equal to 100 when the bond defaults and to −5 otherwise. Denote by
Yi the default indicator of ﬁrm i, i.e. Yi is equal to one if bond i defaults in [t, t + 1]
and equal to zero otherwise. We get Li = 100Yi −5(1−Yi) = 105Yi −5. Hence the
Li form a sequence of iid rvs with P(Li = −5) = 0.98 and P(Li = 100) = 0.02.
We compare two portfolios, both with current value equal to 10 000. Portfolio A
is fully concentrated and consists of 100 units of bond one. Portfolio B is completely
diversiﬁed: it consists of one unit of each of the bonds. Economic intuition suggests
that portfolio B is less risky than portfolio A and hence should have a lower VaR.
Let us compute VaR at a conﬁdence level of 95% for both portfolios.
For portfolio A the portfolio loss is given by LA = 100L1, so VaR0.95(LA) =
100 VaR0.95(L1). Now P(L1 ⩽−5) = 0.98 ⩾0.95 and P(L1 ⩽l) = 0 < 0.95
for l < −5. Hence VaR0.95(L1) = −5, and therefore VaR0.95(LA) = −500. This
means that even after a withdrawal of a risk capital of 500 the portfolio is still
acceptable to a risk controller working with VaR at the 95% level.
--- page 258 ---

242
6. Aggregate Risk
For portfolio B we have
LB =
100

i=1
Li = 105
100

i=1
Yi −500,
and hence VaRα(LB) = 105qα(100
i=1 Yi) −500. The sum M := 100
i=1 Yi has a
binomial distribution M ∼B(100, 0.02). We get by inspection that P(M ⩽5) ≈
0.984 ⩾0.95 and P(M ⩽4) ≈0.949 < 0.95, so q0.95(M) = 5. Hence
VaR0.95(LB) = 525 −500 = 25. In this case a bank would need an additional
risk capital of 25 to satisfy a regulator working with VaR at the 95% level. Clearly,
the risk capital required for portfolio B is higher than for portfolio A.
This illustrates that measuring risk with VaR can lead to nonsensical results.
Moreover, our example shows that VaR is not subadditive in general. In fact, for any
coherent risk measure ϱ, which depends only on the distribution of L, we get
ϱ
 100

i=1
Li

⩽
100

i=1
ϱ(Li) = 100ϱ(L1) = ϱ(100L1).
Hence any coherent risk measure, which depends only on the loss distribution, will
lead to a higher risk-capital requirement for portfolio A than for portfolio B.
In Example 6.7 the non-subbaditivity of VaR is caused by the fact that the assets
making up the portfolio have very skewed loss distributions; such a situation can
clearly occur if we have defaultable bonds or options in our portfolio. Note, however,
that the assets in this example have an innocuous dependence structure because they
are independent. We will see in Example 6.22 in Section 6.2 that non-subadditivity
can also occur when the loss distributions of the individual assets are smooth and
symmetric, but their dependence structure or copula is of a special, highly asymmetric form. Finally, non-subadditivity of VaR also occurs when the underlying rvs
are independent but very heavy-tailed; see Example 7 in Embrechts, McNeil and
Straumann (2002) and Example 5.2.7 in Denuit and Charpentier (2004), which both
use inﬁnite-mean Pareto risks.
VaR is, however, subadditive in the idealized situation where all portfolios can
be represented as linear combinations of the same set of underlying elliptically
distributed risk factors. In this case both the marginal loss distributions of the risk
factors and the copula possess strong symmetry. We have seen in Chapter 3 that
an elliptical model may be a reasonable approximate model for various kinds of
risk-factor data, such as stock or exchange-rate returns.
Theorem 6.8 (subadditivity of VaR for elliptical risk factors). Suppose that X ∼
Ed(µ, Σ, ψ) and deﬁne the set M of linearized portfolio losses of the form
M =

L : L = λ0 +
d

i=1
λiXi, λi ∈R

.
Then for any two losses L1, L2 ∈M and 0.5 ⩽α < 1,
VaRα(L1 + L2) ⩽VaRα(L1) + VaRα(L2).
--- page 259 ---

6.1. Coherent Measures of Risk
243
Proof. Without any loss of generality we assume that λ0 = 0. For any L ∈M it
follows from Deﬁnition 3.26 that we can write L = λ′X d= λ′AY + λ′µ for a spherical random vector Y ∼Sk(ψ), a matrix A ∈Rd×k and a constant vector µ ∈Rd.
By part (3) of Theorem 3.19 we have
L d= ∥λ′A∥Y1 + λ′µ,
(6.3)
showing that every L ∈M is an rv of the same type. Moreover, the translation
invariance and homogeneity of VaR imply that, for L = λ′X,
VaRα(L) = ∥λ′A∥VaRα(Y1) + λ′µ.
(6.4)
Now set L1 = λ′
1X and L2 = λ′
2X. Since ∥(λ1 + λ2)′A∥⩽∥λ′
1A∥+ ∥λ′
2A∥and
since VaRα(Y1) ⩾0 for α ⩾0.5, the result follows.
6.1.3
Coherent Risk Measures Based on Loss Distributions
We give two examples of coherent risk measures that are based on loss distributions.
Expected shortfall.
A proof of the coherence of expected shortfall, deﬁned in
Deﬁnition 2.15, can be based on Lemma 2.20, which gives a representation of
expected shortfall as the limit of the averages of upper order statistics.
Proposition 6.9. Expected shortfall is a coherent risk measure.
Proof. The translation invariance, positive homogeneity and monotonicity properties follow easily from the representation ESα = (1/(1 −α))
 1
α VaRu(L) du and
the corresponding properties for quantiles. It remains to show subadditivity.
Consider a generic sequence of rvs L1, . . . , Ln with associated order statistics
L1,n ⩾· · · ⩾Ln,n and note that for arbitrary m satisfying 1 ⩽m ⩽n we have
m

i=1
Li,n = sup{Li1 + · · · Lim : 1 ⩽i1 < · · · < im ⩽m}.
Now consider two rvs L and ˜L with joint df F and a sequence of iid bivariate random
vectors (L1, ˜L1), . . . , (Ln, ˜Ln) with the same df F. Writing (L + ˜L)i := Li + ˜Li
and (L + ˜L)i,n for an order statistic of (L + ˜L)1, . . . , (L + ˜L)n, we observe that
we must have
m

i=1
(L + ˜L)i,n = sup{(L + ˜L)i1 + · · · + (L + ˜L)im : 1 ⩽i1 < · · · < im ⩽m}
⩽sup{Li1 + · · · + Lim : 1 ⩽i1 < · · · < im ⩽m}
+ sup{ ˜Li1 + · · · + ˜Lim : 1 ⩽i1 < · · · < im ⩽m}
=
m

i=1
Li,n +
m

i=1
˜Li,n.
By setting m = [n(1 −α)] and letting n →∞, we infer from Lemma 2.20 that
ESα(L + ˜L) ⩽ESα(L) + ESα( ˜L).
--- page 260 ---

244
6. Aggregate Risk
A coherent premium principle.
In Fischer (2003), a class of coherent risk measures
closely resembling certain actuarial premium principles is proposed. These risk
measures could be useful for an insurance company that wants to compute premiums
on a coherent basis without deviating too far from standard actuarial practice.
Given constants p > 1 and α ∈[0, 1), this coherent premium principle ϱ[α,p]
is deﬁned as follows. Let M := Lp(Ω, F , P), the space of all L with ∥L∥p :=
E(|L|p)1/p < ∞, and deﬁne, for L ∈M,
ϱ[α,p](L) = E(L) + α∥(L −E(L))+∥p.
(6.5)
Under (6.5) the risk of a loss L is measured by the sum of E(L), the actuarial value
of a loss, and a risk loading given by a fraction α of the Lp-norm of the positive
part of the centred loss L −E(L). This loading can be written more explicitly as
(
 ∞
E(L)(l −E(L))p dFL(l))1/p. The higher the values of α and p, the more conservative the risk measure ϱ[α,p] becomes.
The coherence of ϱ[α,p] is easy to check. Translation invariance and positive
homogeneity are immediate. To prove subadditivity observe that for any two rvs X
and Y we have (X + Y)+ ⩽X+ + Y +. Hence we get from Minkowski’s inequality
(the triangle inequality for the Lp-norm) for any two L1, L2 ∈M:
∥(L1 −E(L1) + L2 −E(L2))+∥p ⩽∥(L1 −E(L1))+ + (L2 −E(L2))+∥p
⩽∥(L1 −E(L1))+∥p + ∥(L2 −E(L2))+∥p,
which shows that ϱ[α,p] is subadditive. To verify monotonicity assume that L ⩽0
almost surely; in that case we have (L−E(L))+ ⩽−E(L) almost surely, and hence
∥(L −E(L))+∥p ⩽−E(L), so ϱ[α,p] ⩽0 since α < 1.
6.1.4
Coherent Risk Measures as Generalized Scenarios
In this section we present a general class of coherent risk measures based on the idea
of generalized scenarios; recall from Remark 2.9 that scenario-based risk measures
are used in practice at the Chicago Mercantile Exchange. We show that if we restrict
our attention to discrete probability spaces, then in fact all coherent risk measures
belong to this class. It is possible to extend the idea to general (inﬁnite) probability
spaces but the results become somewhat more technical (see Notes and Comments
for further references).
Deﬁnition 6.10. Denote by P a set of probability measures on our underlying
measurable space (Ω, F ), and set MP := {L : EQ(|L|) < ∞for all Q ∈P}.
Then the risk measure induced by the set of generalized scenarios P is the mapping
ϱP : MP →R such that ϱP (L) := sup{EQ(L) : Q ∈P}.
Proposition 6.11.
(i) For any set P of probability measures on (Ω, F ) the risk measure ϱP is
coherent on MP .
(ii) Suppose that Ωis a ﬁnite set {ω1, . . . , ωd} and let M = {L : Ω→R}.
Then, for any coherent risk measure ϱ on M, there is a set P of probability
measures on Ωsuch that ϱ = ϱP .
--- page 261 ---

6.1. Coherent Measures of Risk
245
Proof. The proof of (i) is straightforward. The properties of translation invariance,
positive homogeneity and monotonicity follow easily from Deﬁnition 6.10. For
subadditivity observe that
sup{EQ(L1 + L1) : Q ∈P } = sup{EQ(L1) + EQ(L2) : Q ∈P}
⩽sup{EQ(L1) : Q ∈P} + sup{EQ(L2) : Q ∈P}.
The proof of (ii) is more technical and can be skipped by a reader interested mainly in
applications. Essentially, the argument is an application of the separating hyperplane
theorem for convex sets.
We start with some notation. For l ∈Rd we write l ⩾0 if li ⩾0 for all 1 ⩽i ⩽d;
by 1 ∈Rd we denote the vector (1, . . . , 1)′. Since Ωis ﬁnite, we may identify M
with Rd by associating an rv L with the vector l ∈Rd with li = L(ωi), 1 ⩽i ⩽d.
Similarly, a linear functional λ on Rd with λ(l) ⩾0 for all l ⩾0 and λ(1) = 1 can
be identiﬁed with a probability measure Pλ on Ωvia Pλ(ωi) = λ(ei), ei the ith unit
vector. Below we will use these identiﬁcations freely.
We have proved claim (ii) if we can show that for every rv L0 ∈M there is a
probability measure Q = Q(L0) such that
EQ(L) ⩽ϱ(L)
for all L ∈M and EQ(L0) = ϱ(L0).
(6.6)
In fact, in that case we may take P = {Q(L0) : L0 ∈M}.
Now we turn to the proof of (6.6). If this relation holds for some L0 and some
Q, it holds simultaneously for Q and all rvs of the form aL0 + b, a ∈R+, b ∈R
(by translation invariance and positive homogeneity). We may therefore assume that
ϱ(L0) = 1. Deﬁne ˜U := {L ∈M : ϱ(L) < 1}. As explained above we can identify
˜U with a subset U ⊂Rd. The set U is open (as ϱ is continuous) and convex
(as ϱ is coherent and hence a convex functional on M); moreover, l0 (the vector
corresponding to the rv L0) does not belong to U. Using the separating hyperplane
theorem (see, for example, Rockafellar (1970) or Appendix B of Dufﬁe (2001)) we
conclude that there is a linear functional λ on Rd such that
λ(l) < λ(l0)
for all l ∈U.
(6.7)
Since 0 ∈U, it follows that 0 = λ(0) < λ(l0), and we may normalize λ(l0) to one.
We now check that λ induces a probability measure, i.e. that (a) λ(l) ⩾0 for all
l ⩾0 and (b) λ(1) = 1. Note that we may write (6.7) as
λ(l) < 1
for all L such that ϱ(L) < 1.
(6.8)
To prove (a) we use that for L < 0 we have ϱ(L) < 0 and hence λ(l) < 1.
This implies that for L ⩾0 and a > 0 we get, using the linearity of λ, aλ(l) =
−λ(−al) > −1, and hence λ(l) > −1/a. Letting a tend to ∞yields (a).
To prove (b) we ﬁrst note that for any constant a < 1 we have ϱ(a) = a < 1, and
hence by (6.8) we have λ(a1) < 1, so λ(1) ⩽1. On the other hand, we get for a > 1
that ϱ(2L0 −a) = 2ϱ(L0) −a = 2 −a < 1, hence 1 > λ(2l0 −a) = 2 −aλ(1),
and therefore aλ(1) > 1; this implies that λ(1) ⩾1, and hence (b).
--- page 262 ---

246
6. Aggregate Risk
We now show that Q := Pλ is the desired probability measure. For this we need
to verify (6.6), i.e. we have to show that Eλ(L) ⩽ϱ(L) for all L ∈M. This is
equivalent to the implication ϱ(L) < b ⇒λ(l) < b for all L ∈M, b ∈R. Now,
by translation invariance, ϱ(L) < b ⇐⇒ϱ(L −(b −1)) = ϱ(L) + 1 −b < 1.
Hence we get from (6.8) that 1 > Eλ(L −(b −1)) = Eλ(L) −b + 1, and therefore
Eλ(L) < b, as required.
6.1.5
Mean-VaR Portfolio Optimization
In this section we show what can happen if investors optimize the expected return
on their portfolios under some constraint on VaR in a situation where VaR is not
coherent—the portfolios resulting from such an optimization procedure exploit the
conceptual weaknesses of VaR and lead to highly risky, non-diversiﬁed allocations.
This is illustrated in the simplistic Example 6.12 below but we stress that the same
phenomenon can be observed in more realistic situations (see Notes and Comments).
At the end of this section we discuss again the idealized situation of linear portfolios
of elliptical risk factors, where VaR is coherent and where mean variance portfolio
optimization turns out to be equivalent to the standard Markowitz approach.
Example 6.12. Consider in the context of Example 6.7 a portfolio manager who
has an amount of capital V which can be invested in the d = 100 defaultable bonds
with current price 100. For simplicity we assume that it is not possible to borrow
additional money or to take short positions in the defaultable bonds. Denote by
ΛV := {λ ∈Rd : λ ⩾0, d
i=1100λi = V } the set of all admissible portfolios
with value V at time t. The loss of some portfolio λ ∈ΛV will be denoted by L(λ);
the expected proﬁt of a portfolio is thus given by E(−L(λ)). We assume that the
portfolio manager determines the portfolio using a mean-VaR optimality criterion,
as follows. Given some risk-aversion coefﬁcient β > 0, a portfolio λ∗is chosen in
order to maximize
E(−L(λ)) −β VaRα(L(λ))
(6.9)
over all λ ∈ΛV . Portfolio optimization problems of the form (6.9) are frequently
considered in practice. Moreover, optimization problems closely related to (6.9) do
arise implicitly in the context of risk-adjusted performance measurement; often the
performance of trading desks within a ﬁnancial institution is measured by the ratio
of proﬁts earned by the desk and risk capital needed as a backup against losses
from its operations. If this risk capital is determined using VaR, traders have similar
incentives in choosing their portfolios as if operating directly under the simple
criterion (6.9).
Next we determine the optimal portfolio λ∗. Since the Li are identically distributed, every admissible portfolio λ ∈ΛV has the same expected loss. Hence,
maximizing (6.9) over all admissible portfolios amounts to minimizing VaRα(L)
over ΛV . Consider the case where α = 0.95. In order to minimize VaRα(L) we
should invest all funds into one bond (for example the ﬁrst), as was shown in Example 6.7.
In our symmetric situation economic intuition suggests that the optimal portfolio
should be given by a mixture of an investment in the riskless asset and a portfolio
--- page 263 ---

6.1. Coherent Measures of Risk
247
consisting of an equal amount of each of the risky bonds. It can be shown that this is
indeed the case, if we replace VaR by a coherent risk measure which depends only
on the distribution of losses such as generalized expected shortfall (see Frey and
McNeil (2002) for details).
Portfolio optimization for elliptical risk factors.
In the elliptical world, the use of
any positive-homogeneous, translation-invariant measure of risk to rank risks or to
determine the optimal risk-minimizing portfolio under the condition that a certain
return is attained is equivalent to the Markowitz approach, where the variance is used
as the risk measure. Alternative risk measures, such as VaR or expected shortfall,
give different numerical values, but have no effect on the management of risk. We
make these assertions more precise in the next proposition.
Proposition 6.13. Suppose that X ∼Ed(µ, Σ, ψ), with var(Xi) < ∞for all i.
Denote by W = {w ∈Rd : d
i=1 wi = 1} the set of portfolio weights. Assume that
the current value of the portfolio is V and let L(w) = V d
i=1 wiXi be the (linearized) portfolio loss. Let ϱ be a real-valued risk measure depending only on the
distribution of a risk. Suppose ϱ is positive homogeneous and translation invariant.
Let E = {w ∈W : −w′µ = m} be the subset of portfolios giving expected return m.
Then argminw∈Eϱ(L(w)) = argminw∈E var(L(w)).
Proof. Recall from the proof of Theorem 6.8 that for every w ∈E the loss
L = L(w) is an rv of the same type, so ϱ((L + mV )/√var(L)) = k for some
constant k. From positive homogeneity and translation invariance it follows that
ϱ(L) = k√var(L) −mV , from which it is clear that the Markowitz portfolio also
minimizes ϱ.
Notes and Comments
The basic paper on coherent risk measures is Artzner et al. (1999); a non-technical
introduction by the same authors is Artzner et al. (1997). Technical extensions such
as the characterization of coherent risk measures on inﬁnite probability spaces are
given in Delbaen (2000, 2002). Example 6.7 is due to Albanese (1997) and Artzner
et al. (1999). Different existing notions of expected shortfall are discussed in the very
readable paper by Acerbi and Tasche (2002). Expected shortfall has been independently studied by Rockafellar and Uryasev (2000, 2002) under the name conditional
Value-at-Risk;inparticular,thesepapersshowthatexpectedshortfallcanbeobtained
as the value of a convex optimization problem.
The study of convex risk measures in the context of risk management and mathematical ﬁnance began with F¨ollmer and Schied (2002) (see also Frittelli and Rosazza
2002).A good treatment at advanced textbook level is given in Chapter 4 of F¨ollmer
and Schied (2004). Cont (2005) provides an interesting link between convex risk
measures and model risk in the pricing of derivatives.
Our exposition in Section 6.1.5 follows Frey and McNeil (2002) closely. Related
portfolio optimization problems have been studied in Basak and Shapiro (2001),
Krokhmal, Palmquist and Uryasev (2002) and Emmer, Kl¨uppelberg and Korn
--- page 264 ---

248
6. Aggregate Risk
(2001). Risk-adjusted performance measures are widely used in industry in the context of capital budgeting and performance measurement.A good overview of current
practice is given in Chapter 14 of Crouhy, Galai and Mark (2001); an analysis of
risk management and capital budgeting for ﬁnancial institutions from an economic
viewpoint is Froot and Stein (1998).
There is an extensive body of economic theory related to the use of elliptical
distributions in ﬁnance. The papers by Owen and Rabinovitch (1983), Chamberlain
(1983) and Berk (1997) provide an entry to the area. Landsman and Valdez (2003)
discuss the explicit calculation of the quantity E(L | L > qα(L)) for portfolios of
elliptically distributed risks. This coincides with expected shortfall for continuous
loss distributions (see Proposition 2.16).
There has been recent interest in the subject of multiperiod risk measures, which
take into account the evolution of the ﬁnal value of a position over several time
periods and consider the effect of intermediate information and actions. Important
papers in this area include Artzner et al. (2005), Riedel (2004) and Weber (2004).
6.2
Bounds for Aggregate Risks
In this section we consider the general problem of ﬁnding bounds for functionals of
aggregate risks when marginal information about the individual risks is available.
From a mathematical viewpoint this turns out to be a so-called Fr´echet problem.
We begin by presenting the general problem before concentrating on the problem
of bounding the VaR of an aggregate risk.
6.2.1
The General Fr´echet Problem
Consider a random vector L = (L1, . . . , Ld)′, representing losses associated with
various individual investments or risks, and a measurable function Ψ : Rd →R,
representing the operation of aggregation.The rv Ψ (L) is interpreted as an aggregate
ﬁnancial position and typical examples are
• the total loss Sd = d
k=1 Lk;
• the maximum loss Md = max(L1, . . . , Ld);
• the excess-of-loss treaty d
k=1(Li −ki)+ for thresholds ki ∈R+;
• the stop-loss treaty (d
i=1 Li −k)+ for a threshold k ∈R+; and
• a combined position MdI{Sd>qα}.
All of these examples have an immediate interpretation in insurance and ﬁnance.
For instance, in the context of credit risk, the last example might correspond to a
basket position paying out the largest loss Md, but only if the total loss Sd exceeds
its α-quantile qα(Sd) for α close to one.
Consider also a real-valued functional ϱ depending on the distribution of Ψ (L);
ϱ can be interpreted as a risk measure, premium principle or pricing function. Ideally
we would like to calculate ϱ(Ψ (L)), but, in order to do so, we need the df of Ψ (L)
and hence the joint distribution of the random vector L. Often we are required to
--- page 265 ---

6.2. Bounds for Aggregate Risks
249
work with much less information. Throughout Section 6.2 we assume that we know
the marginal dfs of the risks L1, . . . , Ld; we formalize this as Assumption (A1).
(A1) The marginal dfs Fi of Li, i = 1, . . . , d, are given.
Of course, in practice, this really means that we have sufﬁcient information concerning the marginal loss distributions that we can treat them as known. In the
absence of additional information concerning the dependence of L1, . . . , Ld we
cannot calculate ϱ(Ψ (L)), but we can look for numerical bounds on the risk subject
to (A1).
For a particular Ψ and ϱ the problem thus consists of ﬁnding lower and upper
bounds ϱmin and ϱmax such that, under (A1),
ϱmin ⩽ϱ(Ψ (L)) ⩽ϱmax.
(6.10)
We would like these bounds to be sharp, meaning that narrower bounds would be
violated by some random vector L whose distribution is consistent with (A1). When
Ψ (L) represents the aggregate loss of a ﬁnancial position and ϱ represents a risk
measure, the analysis of this problem can be thought of as a stress-testing exercise
for risk measures with respect to the dependence structure of the individual risks
involved. The value ϱmax represents the worst possible “riskiness” of the position.
The problem has a very rich history in the ﬁeld of probability, where it typically
appears under the name Fr´echet problem. Indeed, its mathematics is intimately
related to the Fr´echet bounds given in Theorem 5.7 and Remark 5.8. We shall sketch
a solution to the problem, give some examples and, in Notes and Comments, guide
the interested reader to the existing literature for more details.
The problem of ﬁnding the bounds in (6.10) assuming (A1) only can be reformulated as a pair of optimization problems. We are required to calculate
inf{ϱ(Ψ (L)) : Li ∼Fi, i = 1, . . . , d}
sup{ϱ(Ψ (L)) : Li ∼Fi, i = 1, . . . , d}
'
(6.11)
where F1, . . . , Fd are given dfs and Li ∼Fi means that Li has df Fi. The solutions
can be found analytically in some cases, but there also exist various numerical
techniques to solve the problems in general.
We have already encountered problems of the form (6.11) in our analysis of
attainable correlations (see H¨offding’s Theorem (Theorem 5.25)), and we revisit
this problem brieﬂy.
Example 6.14 (attainable correlations). Assume without loss of generality that
we have two risks which are standardized to have mean zero and variance one. The
problem of ﬁnding maximum and minimum correlations for ﬁxed margins can be
formulated as a Fr´echet problem in two dimensions, where Ψ (L1, L2) = L1L2
and ϱ(Ψ (L1, L2)) = E(Ψ (L1, L2)) = ρ(L1, L2), the linear correlation coefﬁcient
between L1 and L2.
Theorem 5.25 shows that the possible range of the correlations between L1 and
L2 over all possible bivariate models for the vector (L1, L2) is a closed interval
--- page 266 ---

250
6. Aggregate Risk
[ρmin, ρmax] ⊂[−1, 1], where possibly ρmin > −1 and/or ρmax < 1. An example
where the margins were taken to be lognormal and for which ρmin > −1 and
ρmax < 1 was given in Example 5.26. Furthermore, we showed that the boundary cases ρmin and ρmax are attained for countermonotonic and comonotonic risks,
respectively; this result is crucial for our discussion below. The case ρmax = 1 can
only occur when L1 and L2 are rvs of the same type, and the case ρmin = −1 can
only occur when L1 and −L2 are rvs of the same type (see Deﬁnition A.1).
Because of Sklar’s Theorem (Theorem 5.3), the inf and sup in (6.11) can be
interpreted as being taken over all copulas C on [0, 1]d. In some situations we may
have some information concerning the dependence structure of L, and it is natural to
translate this dependence information into constraints on C; for instance, we might
take inf and sup over all copulas C ⩾C0, for some ﬁxed copula C0. We discuss
speciﬁc examples below.
6.2.2
The Case of VaR
In this section we show the type of results that are obtained in the case when
ϱ = VaRα. We want to ﬁnd (sharp) bounds for VaRα(Ψ (L)) given the marginal
dfs Fi of Li, i = 1, . . . , d, and partial information on the dependence of the Li
variables, in particular when Ψ is the sum operator. For the interpretation of the
results it will be useful to ﬁrst consider the behaviour of the VaR risk measure for
comonotonic risks as deﬁned in Section 5.1.6.
Additivity of VaR for comonotonic risks.
The following result summarizes additivity of VaR.
Proposition 6.15. Let 0 < α < 1 and L1, . . . , Ld be comonotonic rvs with dfs
F1, . . . , Fd which are continuous and strictly increasing. Then
VaRα(L1 + · · · + Ld) = VaRα(L1) + · · · + VaRα(Ld).
(6.12)
Proof. For ease of notation take d = 2. From Proposition 5.16 we have that
(L1, L2) d= (F ←
1 (U), F ←
2 (U)) for some U ∼U(0, 1). It follows that
VaRα(L1 + L2) = VaRα(F ←
1 (U) + F ←
2 (U)) = F ←
T (U)(α),
where T is the strictly increasing continuous function given by T (x) = F ←
1 (x) +
F ←
2 (x). Now P(T (U) ⩽T (α)) = P(U ⩽α) = α, so the result follows by
observing that
F ←
T (U)(α) = T (α) = F ←
1 (α) + F ←
2 (α) = VaRα(L1) + VaRα(L2).
Remark 6.16 (extensions). A more general form of the above result can be found
in Embrechts, H¨oing and Juri (2003) and is as follows. Let Ψ : Rd →R be
increasing and left-continuous in each argument, 0 < α < 1, and let L1, . . . , Ld be
comonotonic rvs (not necessarily with continuous, strictly increasing dfs). Then
VaRα(Ψ (L1, . . . , Ld)) = Ψ (VaRα(L1), . . . , VaRα(Ld)).
--- page 267 ---

6.2. Bounds for Aggregate Risks
251
A third correlation fallacy.
Based on the above result we can highlight a third
important fallacy concerning correlation to add to the two in Section 5.2.1.
Fallacy 3. VaR for the sum of two risks is at its worst when these two risks have
maximal correlation, i.e. are comonotonic.
Any superadditive VaR example yields a correction to this statement; one such
case was shown in Example 6.7 and a further one is given below in Example 6.22. In
a superadditive VaR situation we have VaRα(L1 + L2) > VaRα(L1) + VaRα(L2)
for two risks L1 and L2 and some conﬁdence level α. By Proposition 6.15 and
Remark 6.16 the right-hand side VaRα(L1) + VaRα(L2) corresponds to the VaR of
L1 + L2 when L1 and L2 are comonotonic. Moreover, Theorem 5.25 and Example 6.14 imply that the correlation of L1 and L2 is maximal in the comonotonic case.
Hence the superadditive portfolio case must correspond to a smaller correlation. The
remainder of Section 6.2 is devoted to the issue of ﬁnding the worst case.
Remark 6.17. For expected shortfall the expression ϱ(L1 + L2) is maximized for
comonotonic losses. To see this, note that Proposition 6.15 together with (2.23)
imply that expected shortfall also has the comonotonic additivity property. Since
expected shortfall is coherent, we have ϱ(L1 + L2) ⩽ϱ(L1) + ϱ(L2), so that
comonotonicity is in fact the worst possible case. There exists a whole class of
coherent risk measures, known as spectral risk measures, which share this property
(see Notes and Comments). Note, also, that if we work with VaR but restrict our
attention to elliptical distributions for the vector L, then VaR is a coherent risk
measure (Theorem 6.8). Fallacy 3 is taken out of play and comonotonicity does
correspond to the worst case.
Restrictions on dependence using copulas.
Before discussing bounds on VaR we
need to formalize the restrictions we make on the dependence structure of the df
F of L. Recall that in the case of continuous marginal dfs Fi, there is a unique
copula C such that F = C(F1, . . . , Fd), and one possibility is to impose dependence
restrictions on L1, . . . , Ld through conditions on C. Recall from Theorem 5.7 that
W ⩽C ⩽M, where W and M denote the Fr´echet lower and upper bounds,
respectively.
We introduce dependence restrictions of the following type.
(A2) C ⩾C0 for a copula C0.
When d = 2 the case of unconstrained optimization can be treated as a special case of
restriction (A2) by setting C0 = W, since W is a proper copula in this case; however,
for d > 2 unconstrained optimization is not a special case of restriction (A2).
The case where C0 = Π, the independence copula in (5.6), corresponds to socalled positive lower orthant dependence (PLOD) (see M¨uller and Stoyan 2002,
Deﬁnition 3.10.1). In Theorem 3.10.4 of M¨uller and Stoyan (2002), it is shown that,
if cov(f (L), g(L)) ⩾0 for all increasing functions f, g : Rd →R, then L is
PLOD.
Note that the relation “⩾” in (A2) is not a complete ordering on the space of all
copulas, meaning that for any two copulas C1 and C2 it is not necessarily true that
