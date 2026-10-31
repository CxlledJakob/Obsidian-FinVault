# Quantitative Risk Management_ Concepts, Techniques, and -- Alexander J_ McNeil, Rüdiger Frey, Paul Embrechts -- Princeton series in finance, -- isbn13 9780691122557 -- 478a0059673fecd0c76229cd3d8884e7 -- Anna’s Arc.pdf — pages 514–533

--- page 514 ---

498
Appendix
A.2.7
Negative Binomial
The rv N has a negative binomial distribution with parameters α > 0 and 0 < p < 1,
written X ∼NB(α, p), if its probability mass function is
P(N = k) =
α + k −1
k

pα(1 −p)k,
k = 0, 1, 2, . . . ,
(A.12)
where
+x
k
,
for x ∈R and k ∈N0 denotes an extended binomial coefﬁcient deﬁned
by
+x
0
,
= 1 and
x
k

= x(x −1) · · · (x −k + 1)
k!
,
k > 0.
The moments of this distribution are
E(N) = α(1 −p)/p
and
var(N) = α(1 −p)/p2.
For α = r ∈N the rv N + r represents the waiting time until the rth success
in independent Bernoulli trials with success probability p, i.e. the total number of
trials that are required until we have r successes. For α = 1 the rv N + 1 is said to
have a geometric distribution.
A.2.8
Pareto
The rv X has a Pareto distribution, written X ∼Pa(α, κ), if its df is
F(x) = 1 −

κ
κ + x
α
,
α, κ > 0, x ⩾0.
(A.13)
Provided that α > n, the moments of this distribution are given by
E(Xn) =
κnn!
n
i=1(α −i).
A.2.9
Stable
The rv X has an α-stable distribution, written X ∼St(α, β, γ, δ), if its characteristic
function is
φ(t) = E exp(itX) =

exp(−γ α|t|α(1 −iβ sign(t) tan(π/2)α) + iδt),
α̸ = 1,
exp(−γ |t|(1 + iβ sign(t)(2/π) ln |t|) + iδt),
α = 1,
(A.14)
where α ∈(0, 2], β ∈[−1, 1], γ > 0 and δ ∈R. Note that there are various
alternative parametrizations of the stable distributions and we use a parametrization
of Nolan (2005, Deﬁnition 1.8). The case X ∼St(α, 1, γ, 0) for α < 1 gives a distribution on the positive half-axis, which we refer to as a positive stable distribution.
A simulation algorithm for a standardized variate Z ∼St(α, β, 1, 0) is given
in Nolan (2005, Theorem 1.19). In the case where α̸ = 1, X = δ + γ Z has a
St(α, β, γ, δ) distribution; the case α = 1 is more complicated.
--- page 515 ---

A.3. Likelihood Inference
499
A.3
Likelihood Inference
This appendix summarizes the mechanics of performing likelihood inference, but
omits theoretical details. A good starting reference for the theory is Casella and
Berger (2002), which we refer to in this appendix where relevant. Other useful books
include Serﬂing (1980), Lehmann (1983), Schervish (1995) and Stuart, Ord and
Arnold (1999), all of which give details concerning the famous regularity conditions
that are required for the asymptotic statements.
A.3.1
Maximum Likelihood Estimators
Suppose that the random vector X = (X1, . . . , Xn)′ has joint probability density (or
mass function) in some parametric family fX(x; θ), indexed by a parameter vector
θ = (θ1, . . . , θp)′ in a parameter space Θ. We consider our data to be a realization
of X for some unknown value of θ.
The likelihood function for the parameter vector θ given the data is L(θ; X) =
fX(X; θ) and the maximum likelihood estimator (MLE) ˆθ is the value of θ maximizing L(θ; X), or equivalently the value maximizing the log-likelihood function
l(θ; X) = ln L(θ; X). We will also write this estimator as ˆθn when we want to
emphasize its dependence on the sample size n.
For large n we expect that the estimate ˆθn should be close to the true value θ,
and various well-known asymptotic results give information about the quality of
the estimator in large samples. In describing these results we consider the classical
situation where X is assumed to be a vector of iid components with univariate density
f so that
ln L(θ; X) = ln
n
!
i=1
f (Xi; θ) =
n

i=1
ln L(θ; Xi).
A.3.2
Asymptotic Results: Scalar Parameter
We consider the case when p = 1 and we have a single parameter θ. Under suitable
regularity conditions (see, for example, Casella and Berger 2002, p. 516), ˆθn may be
shown to be a consistent estimator of θ (i.e. tending to θ in probability as the sample
size n is increased). Notable among the regularity conditions are that θ should be an
identiﬁable parameter (θ̸ = ˜θ ⇒f (x; θ)̸ = f (x; ˜θ)), the true parameter θ should
be an interior point of the parameter space Θ, and that the support of f (x; θ) should
not depend on θ.
Under stronger regularity conditions (see again Casella and Berger 2002, p. 516),
ˆθn may be shown to be an asymptotically efﬁcient estimator of θ, so it satisﬁes
√n( ˆθn −θ)
d−→N(0, I(θ)−1),
(A.15)
where I(θ) denotes the Fisher information of an observation, deﬁned by
I(θ) = E
 ∂
∂θ ln L(θ; X)
2
.
(A.16)
--- page 516 ---

500
Appendix
Under the regularity conditions, the Fisher information can generally also be calculated as
I(θ) = −E
 ∂2
∂θ2 ln L(θ; X)

.
(A.17)
Asymptotic efﬁciency entails both asymptotic normality and consistency. Moreover, it implies that, in a large enough sample, var( ˆθ) ≈1/(nI(θ)), where the righthand side is the so-called Cram´er–Rao lower bound, which is a lower bound for the
variance of an unbiased estimator of θ constructed from an iid sample X1, . . . , Xn.
The MLE is efﬁcient in the sense that it attains this lowest possible bound asymptotically.
A.3.3
Asymptotic Results: Vector of Parameters
When p > 1 and we have a vector of parameters to estimate, similar results apply.
The ML estimator ˆθn of θ is asymptotically efﬁcient in the sense that, as n →∞
and under suitable regularity conditions,
√n( ˆθn −θ)
d−→Np(0, I(θ)−1),
(A.18)
where I(θ) denotes the expected Fisher information matrix for a single observation,
given, in analogy to (A.16) and (A.17), by
I(θ) = E
 ∂
∂θ ln L(θ; X) ∂
∂θ′ ln L(θ; X)

= −E

∂2
∂θ∂θ′ ln L(θ; X)

.
The notation employed here should be taken to mean a matrix with components
I(θ)ij = E
 ∂
∂θi
ln L(θ; X) ∂
∂θj
ln L(θ; X)

= −E

∂2
∂θi∂θj
ln L(θ; X)

.
The convergence result (A.18) implies that, for n sufﬁciently large, we have
ˆθn ∼Np(θ, n−1I(θ)−1),
(A.19)
and this can be used to construct asymptotic conﬁdence regions for θ or intervals
for any component θj. In practice, it is often easier to approximate I(θ) with the
observed Fisher information matrix
¯I(θ) = −1
n
n

i=1
∂2
∂θ∂θ′ ln L(θ; Xi)
forwhateverrealizationofX hasbeenobtained.Thisshouldconvergetotheexpected
information matrix by the law of large numbers and it has been suggested that in
some situations this may even lead to more accurate inference (Efron and Hinkley
1978). In either case, the information matrices depend on the unknown parameters
of the model and are usually estimated by taking I( ˆθ) or ¯I( ˆθ).
--- page 517 ---

A.3. Likelihood Inference
501
A.3.4
Wald Test and Conﬁdence Intervals
From (A.19) we have that, for n sufﬁciently large,
Z :=
ˆθj −θj
se( ˆθj)
∼N(0, 1),
(A.20)
where se( ˆθj) denotes an asymptotic standard error (estimate of the asymptotic
standard deviation) for ˆθj, given by
se( ˆθj) =

n−1I( ˆθ)−1
jj or

n−1 ¯I( ˆθ)−1
jj .
Equation (A.20) can be used to test the null hypothesis H0 : θj = θj,0 for some
value of interest θj,0 against the alternative H1 : θj̸ = θj,0. For an asymptotic test
of size α we would reject H0 if |Z| ⩾Φ−1(1 −1
2α).
An asymptotic 100(1 −α)% conﬁdence interval for θj consists of those values
θj,0 for which the null hypothesis is not rejected and it is given by
( ˆθj −se( ˆθj)Φ−1(1 −1
2α), ˆθj + se( ˆθj)Φ−1(1 −1
2α)).
(A.21)
A.3.5
Likelihood Ratio Test and Conﬁdence Intervals
Now consider testing the null hypothesis H0 : θ ∈Θ0 against the alternative
H1 : θ ∈Θc
0, where Θ0 ⊂Θ. We consider the likelihood ratio test statistic
λ(X) = supθ∈Θ0 L(θ; X)
supθ∈Θ L(θ; X)
and assume, as before, that X1, . . . , Xn are iid and that appropriate regularity
conditions apply. Under the null hypothesis it can be shown that, as n →∞,
−2 ln λ(X) ∼χ2
ν , where the degrees-of-freedom parameter ν of the chi-squared
distribution is essentially given by the number of free parameters speciﬁed by Θ
minus the number of free parameters speciﬁed by the null hypothesis θ ∈Θ0.
For example, suppose that we partition θ so that θ′ = (θ′
1, θ′
2), where θ1 has
dimension q and θ2 has dimension p −q. We wish to test H0 : θ1 = θ1,0 against
H1 : θ1̸ = θ1,0. Writing the likelihood as L(θ1, θ2), the likelihood ratio test statistic
satisﬁes
−2 ln λ(X) = −2(ln L(θ1,0, ˆθ2,0; X) −ln L( ˆθ1, ˆθ2; X)) ∼χ2
q ,
asymptotically, where ˆθ1 and ˆθ2 are the unconstrained MLEs of θ1 and θ2, and ˆθ2,0
is the constrained MLE of θ2 under the null hypothesis. We would reject H0 if
−2 ln λ(X) > cq,1−α, where cq,1−α is the (1 −α)-quantile of the χ2
q distribution.
An asymptotic 100(1 −α)% conﬁdence set for θ1 consists of the values θ1,0 for
which the null hypothesis H0 : θ1 = θ1,0 is not rejected, that is
{θ1,0 : ln L(θ1,0, ˆθ2,0; x) ⩾ln L( ˆθ1, ˆθ2; x) −0.5cq,1−α}.
In particular, if q = 1, so that we are interested only in θ1, we get the conﬁdence
interval
{θ1,0 : ln L(θ1,0, ˆθ2,0; x) ⩾ln L( ˆθ1, ˆθ2; x) −0.5c1,1−α}.
(A.22)
--- page 518 ---

502
Appendix
Note that such an interval will, in general, be asymmetric about the MLE ˆθ1, in the
sense that the distance from the MLE to the upper and lower bounds will be different.
This is in contrast to the Wald interval in (A.21), which is rigidly symmetric.
The curve (θ1,0, ln L(θ1,0, ˆθ2,0; x)) is sometimes known as the proﬁle log-likelihood curve for θ1 and attains its maximum at ˆθ1.
A.3.6
Akaike Information Criterion
The likelihood ratio test is applicable to the comparison of nested models, i.e. situations where one model forms a special case of a more general model when certain
parameter values are constrained.We often encounter situations where we would like
to compare non-nested models with possibly quite different numbers of parameters.
Suppose we have m models M1, . . . , Mm and that model j has kj parameters
denoted by θj = (θj1, . . . , θjkj )′ and a likelihood function Lj(θj; X). In Akaike’s
approach we choose the model minimizing
AIC(Mj) = −2 ln Lj( ˆθj; X) + 2kj,
where ˆθj denotes the MLE of θj. The AIC number essentially imposes a penalty
equal to the number of model parameters kj on the value of the log-likelihood at the
maximum. The model favoured is the one for which the penalized log-likelihood
ln Lj( ˆθj; X) −kj is largest. There are alternatives to the AIC, such as the Bayesian
information criterion (BIC) of Schwartz, which impose different penalties for the
number of parameters. See Burnham and Anderson (2002) for more about model
comparison using these criteria.
--- page 519 ---

References
Abdous, B., K. Ghoudi and A. Khoudraji. 1999. Non parametric estimation of the limit
dependence function of multivariate extremes. Extremes 2(3):245–268.
Abraham, B. and J. Ledolter. 1983. Statistical Methods for Forecasting. Wiley.
Abramowitz, M. and I. A. Stegun (eds). 1965. Handbook of Mathematical Functions. New
York: Dover.
Acerbi, C. 2002. Spectral measures of risk: a coherent representation of subjective risk aversion. Journal of Banking and Finance 26(7):1505–1518.
Acerbi, C. and D. Tasche. 2002. On the coherence of expected shortfall. Journal of Banking
and Finance 26:1487–1503.
Albanese, C. 1997. Credit exposure, diversiﬁcation risk and coherent VaR. Preprint, Department of Mathematics, University of Toronto.
Alexander, C. 2001. Market Models: A Guide to Financial Data Analysis. Wiley.
Allen, F. and D. Gale. 2000. Financial contagion. Journal of Political Economy 108:1–33.
Almgren, R. and N. Chriss. 2001. Optimal execution of portfolio transactions. Journal of Risk
3(2):5–39.
Alsina, C., M. J. Frank and B. Schweizer. 2005. Associative Functions on Intervals: A Primer
of Triangular Norms. Forthcoming.
Altman, E. L. 1993. Corporate Financial Distress and Bankruptcy. Wiley.
Altman, E. L. and H. Suggitt. 2000. Default rates in the syndicated loan market: a mortality
analysis. Journal of Banking and Finance 24:229–253.
Andersen, L. and J. Sidenius. 2004. Extensions to the Gaussian copula: random recovery and
random factor loadings. Journal of Credit Risk 1:29–70.
Andersen, P. K., Ø. Borgan, R. Gill and N. Keiding. 1993. Statistical Models Based on
Counting Processes. Springer.
An´e, T. and H. Geman. 2000. Order ﬂow, transaction clock, and normality of asset returns.
Journal of Finance 55:2259–2284.
Artzner, P. and F. Delbaen. 1995. Default risk insurance and incomplete markets. Mathematical Finance 5:187–195.
Artzner, P., F. Delbaen, J. M. Eber and D. Heath. 1997. Thinking coherently. Risk 10(11):68–
71.
. 1999. Coherent measures of risk. Mathematical Finance 9:203–228.
Artzner, P., F. Delbaen, J.-M. Eber, D. Heath and H. Ku. 2005. Coherent multiperiod riskadjusted values and Bellman’s principle. Annals of Operations Research. Forthcoming.
Asmussen, S. 2000. Ruin Probabilities. World Scientiﬁc.
Asmussen, S., K. Binswanger and B. Højgaard. 2000. Rare events simulation for heavy-tailed
distributions. Bernoulli 6(2):303–322.
Atkinson,A. C. 1982. The simulation of generalized inverse Gaussian and hyperbolic random
variables. SIAM Journal on Scientiﬁc Computing 3(4):502–515.
Attanasio, O. P. 1991. Risk, time varying second moments and market efﬁciency. Review of
Economic Studies 58:479–494.
Aubin, J.-P. 1979. Mathematical Methods of Game and EconomicTheory.Amsterdam: North-
Holland.
--- page 520 ---

504
References
Bailey,A. L. 1945.A generalized theory of credibility. Proceedings of the Casualty Actuarial
Society 32:13–20.
Balkema, A. A. and P. Embrechts. 2004. Multivariate excess distributions. Preprint, ETH
Zurich.
Balkema, A. A. and L. de Haan. 1974. Residual life time at great age. Annals of Probability
2:792–804.
Balkema, A. A. and S. I. Resnick. 1977. Max-inﬁnite divisibility. Journal of Applied Probability 14:309–319.
Bangia, A., F. X. Diebold, A. Kronimus, C. Schlagen and T. Schuermann. 2002. Ratings
migration and the business cycle, with application to credit portfolio stress testing. Journal
of Banking and Finance 26:445–474.
Bank, P. and D. Baum. 2004. Hedging and portfolio optimization in ﬁnancial markets with a
large trader. Mathematical Finance 14:1–18.
Baringhaus, L. 1991. Testing for spherical symmetry of a multivariate distribution. Annals of
Statistics 19(2):899–917.
Barndorff-Nielsen, O. E. 1978. Hyperbolic distributions and distributions on hyperbolae.
Scandinavian Journal of Statistics 5:151–157.
. 1997. Normal inverse Gaussian distributions and stochastic volatility modelling. Scandinavian Journal of Statistics 24:1–13.
Barndorff-Nielsen, O. E. and P. Blæsild. 1981. Hyperbolic distributions and ramiﬁcations:
contributions to theory and application. In Statistical Distributions in Scientiﬁc Work (ed.
C. Taillie, G. Patil and B. Baldessari), vol. 4, pp. 19–44. Dordrecht: Reidel.
Barndorff-Nielsen, O. E. and N. Shephard. 2005. Continuous Time Approach to Financial
Volatility. Cambridge University Press. Forthcoming.
Barone-Adesi, G., F. Bourgoin and K. Giannopoulos. 1998. Don’t look back. Risk 11(8):100–
103.
Basak, S. and A. Shapiro. 2001. Value-at-Risk based risk management: optimal policies and
asset prices. Review of Financial Studies 14(2):371–405.
Basel Committee on Banking Supervision. 2003. The 2002 loss data collection exercise
for operational risk: summary of the data collected. Risk Management Group, Bank of
International Settlements. (Available from www.bis.org/bcbs/.)
. 2004. International convergence of capital measurement and capital standards.
A revised framework. Bank of International Settlements. (Available from www.bis.org/
bcbs/.)
Bauwens, L., S. Laurent and J.V. K. Rombouts. 2005. Multivariate GARCH models: a survey.
Journal of Applied Economics. Forthcoming.
Baxter, M. and A. Rennie. 1996. Financial Calculus. Cambridge University Press.
Becherer, D. 2004. Utility indifference hedging and valuation via reaction–diffusion systems.
Proceedings of the Royal Society of London, Series A 460:27–51.
Becherer, D. and M. Schweizer. 2005. Classical solutions to reaction diffusion systems for
hedging problems with interacting Itˆo and point processes. Annals of Applied Probability
15(2). Forthcoming.
Bedford, T. and R. Cooke. 2001. Probabilistic Risk Analysis: Foundations and Methods.
Cambridge University Press.
Beirlant, J., Y. Goegebeur, T. Segers and J. L. Teugels. 2004. Statistics of Extremes: Theory
and Applications. Wiley.
B´elanger, A., S. Shreve and D. Wong. 2004. A general framework for pricing credit risk.
Mathematical Finance 14:317–350.
Bening, V. E. and V. Yu. Korolev. 2002. Generalized Poisson Models and Their Applications
in Insurance and Finance. Utrecht: VSP.
--- page 521 ---

References
505
Beran, J. 1979. Testing for ellipsoidal symmetry of a multivariate density. Annals of Statistics
7(1):150–162.
Berk, J. B. 1997. Necessary conditions for the CAPM. Journal of Economic Theory 73:245–
257.
Berkes, I., L. Horv´ath and P. Kokoszka. 2003. GARCH processes: structure and estimation.
Bernoulli 9:201–228.
Berkowitz,J.2001.Testingtheaccuracyofdensityforecasts,applicationstoriskmanagement.
Journal of Business and Economic Statistics 19:465–474.
. 2002. Testing distributions. Risk 15(6):77–80.
Berkowitz, J. and J. O’Brien. 2002. How accurate are Value-at-Risk models at commercial
banks? Journal of Finance 57:1093–1112.
Berndt, A., R. Douglas, D. Dufﬁe, F. Ferguson and D. Schranz. 2004. Measuring default risk
premia from default swap rates and EDFs. Preprint, Stanford University.
Berndt, E. K., B. H. Hall, R. E. Hall and J. A. Hausman. 1974. Estimation and inference in
nonlinear structural models. Annals of Economic and Social Measurement 3:653–665.
Bernstein, P. L. 1998. Against the Gods: The Remarkable Story of Risk. Wiley.
Bibby, B. M. and M. Sørensen. 2003. Hyperbolic processes in ﬁnance. In Handbook of Heavy
Tailed Distributions in Finance (ed. S. T. Rachev), pp. 211–248. Amsterdam: Elsevier.
Bickel, P. J. and K. A. Doksum. 2001. Mathematical Statistics: Basic Ideas and Selected
Topics, 2nd edn, vol. 1. Upper Saddle River, NJ: Prentice Hall.
Bielecki, T. and M. Rutkowski. 2002. Credit Risk: Modeling, Valuation, and Hedging.
Springer.
Bielecki, T., M. Jeanblanc and M. Rutkowski. 2004. Hedging of defaultable claims. In Paris–
Princeton Lectures on Mathematical Finance, 2003 (ed. R. A. Carmona et al.). Springer.
Billingsley, P. 1995. Probability and Measure, 3rd edn. Wiley.
Bingham, N. H. and R. Kiesel. 1998. Risk-Neutral Valuation. Springer.
. 2002. Semi-parametric modelling in ﬁnance: theoretical foundations. Quantitative
Finance 2:241–250.
Bingham, N. H., C. M. Goldie and J. L. Teugels. 1987. Regular Variation. Cambridge University Press.
Bj¨ork, T. 1998. Arbitrage Theory in Continuous Time. Oxford University Press.
Black, F. and J. Cox. 1976. Valuing corporate securities: some effects of bond indenture
provisions. Journal of Finance 31(2):351–367.
Black, F. and M. Scholes. 1973. The pricing of options and corporate liabilities. Journal of
Political Economy 81(3):637–654.
Blæsild, P. 1981. The two-dimensional hyperbolic distribution and related distributions, with
an application to Johannsen’s bean data. Biometrika 68(1):251–263.
Blæsild, P. and J. L. Jensen. 1981. Multivariate distributions of hyperbolic type. In Statistical
Distributions in ScientiﬁcWork (ed. C.Taillie, G. Patil and B. Baldessari), vol. 4, pp. 45–66.
Dordrecht: Reidel.
Bluhm, C., L. Overbeck and C. Wagner. 2002. An Introduction to Credit Risk Modeling.
London: Chapman & Hall.
Blum, P. 2005. On some mathematical aspects of dynamic ﬁnancial analysis. PhD thesis,
ETH Zurich.
Blum, P. and M. Dacorogna. 2004. DFA—dynamic ﬁnancial analysis. In Encyclopedia of
Actuarial Science (ed. J. L. Teugels and B. Sundt), pp. 505–519. Wiley.
Bodnar, G. M., G. Hyat and R. Marston. 1999. Wharton 1998 survey of risk management by
US non-ﬁnancial ﬁrms. Financial Management 27(4): 70–91.
Bohn, J. R. 2000. An empirical assessment of a simple contingent-claims model for the
valuation of risky debt. Journal of Risk Finance 1(4):55–77.
--- page 522 ---

506
References
Bollerslev, T. 1986. Generalized autoregressive conditional heteroskedasticity. Journal of
Econometrics 31:307–327.
. 1990. Modelling the coherence in short-run nominal exchange rates: a multivariate
generalized ARCH approach. Review of Economics and Statistics 72:498–505.
Bollerslev, T., T. Chou and K. Kroner. 1992. ARCH modelling in ﬁnance: a selective review
of theory and empirical evidence. Journal of Econometrics 52:201–224.
Bollerslev, T., R. F. Engle and D. B. Nelson. 1994. ARCH models. In Handbook of Econometrics (ed. R. F. Engle and D. L. McFadden), vol. 4, pp. 2959–3038. Amsterdam: North-
Holland.
Bollerslev, T., R. F. Engle and J. M. Wooldridge. 1988. A capital-asset pricing model with
time-varying covariances. Journal of Political Economy 96:116–131.
Bougerol, P. and N. Picard. 1992. Stationarity of GARCH processes and of some non-negative
time series. Journal of Econometrics 52:115–127.
Bowers, N. L., H. U. Gerber, J. C. Hickman, D. A. Jones and C. J. Nesbitt. 1986. Actuarial
Mathematics. Itasca, IL: Society of Actuaries.
Box, G. E. P. and G. M. Jenkins. 1970. Time Series Analysis: Forecasting and Control. San
Francisco, CA: Holden-Day.
Box, G. E. P. and D. A. Pierce. 1970. Distribution of residual autocorrelations in autoregressive-integrated moving average time series models. Journal of the American Statistical
Association 65:1509–1526.
Boyle, P. and F. Boyle. 2001. Derivatives. The Tools that Changed Finance. London: Risk
Waters Group.
Brand, L. and R. Bahr. 2001. Ratings performance 2000: default, transition, recovery, and
spreads. New York: Standard & Poor’s.
Brandt, A. 1986. The stochastic equation yn+1 = anyn + bn with stationary coefﬁcients.
Advances in Applied Probability 18:211–220.
Brealey, R. and S. Myers. 2000. Principles of Corporate Finance, 6th edn. New York:
McGraw-Hill.
Breiman, L. 1965. On some limit theorems similar to the arc-sin law. Theory of Probability
and Its Applications 10:323–331.
Br´emaud, P. 1981. Point Processes and Queues: Martingale Dynamics. Springer.
Brennan, M. J. and L. Trigeorgis. 2000. Project Flexibility, Agency, and Competition. Oxford
University Press.
Breslow, N. and D. G. Clayton. 1993. Approximate inference in generalized linear mixed
models. Journal of the American Statistical Association 88:9–25.
Breymann, W.,A. Dias and P. Embrechts. 2003. Dependence structures for multivariate highfrequency data in ﬁnance. Quantitative Finance 3:1–14.
Briys, E. and F. de Varenne. 2001. Insurance. From Underwriting to Derivatives. Asset Liabilitiy Management in Insurance Companies. Wiley.
Brockwell, P. J. and R. A. Davis. 1991. Time Series: Theory and Methods, 2nd edn. Springer.
. 2002. Introduction to Time Series and Forecasting, 2nd edn. Springer.
Brooks, C., S. P. Burke and G. Persand. 2001. Benchmarks and the accuracy of GARCH
model estimation. International Journal of Forecasting 17:45–56.
Brummelhuis, R. G. M. and R. Kaufmann. 2004. Time scaling for GARCH(1,1) and AR(1)–
GARCH(1,1) processes. Preprint, ETH Zurich.
B¨uhlmann, H. 1967. Experience rating and credibility. ASTIN Bulletin 4(3):199–207.
. 1968. Experience rating and credibility. ASTIN Bulletin 5(2):157–165.
. 1970. Mathematical Methods in Risk Theory. Springer.
. 1971. Credibility procedures. In Proceedings of the 6th Berkeley Symposium on Probability and Statistics, vol. 1, pp. 515–525. Berkeley, CA: University of California Press.
--- page 523 ---

References
507
B¨uhlmann, H. 1984. Numerical evaluation of the compound Poisson distribution: recursion
or the fast Fourier transform? Scandinavian Actuarial Journal, pp. 116–126.
B¨uhlmann, H. and A. Gisler. 2005. A Course in Credibility Theory and its Applications.
Springer. Forthcoming.
B¨uhlmann, P. and A. J. McNeil. 2002. An algorithm for nonparametric GARCH modelling.
Journal of Computational Statistics and Data Analysis 40:665–683.
Burnham, K. P. and D. R. Anderson. 2002. Model Selection and Multimodel Inference: A
Practical Information-Theoretic Approach. Springer.
Burtschell, X., J. Gregory and J.-P. Laurent. 2005. A comparative analysis of CDO pricing
models. Working paper, BNP Paribas and ISFA, University of Lyon.
Cambanis, S., S. Huang and G. Simons. 1981. On the theory of elliptically contoured distributions. Journal of Multivariate Analysis 11:368–385.
Campbell, J.Y.,A.W. Lo andA. C. MacKinlay. 1997.The Econometrics of Financial Markets.
Princeton University Press.
Casella, G. and R. L. Berger. 2002. Statistical Inference. Paciﬁc Grove, CA: Duxbury.
Chamberlain, G. 1983.A characterization of the distributions that imply mean-variance utility
functions. Journal of Economic Theory 29:185–201.
Chatﬁeld, C. 1996. The Analysis of Time Series: An Introduction, 5th edn. London: Chapman
& Hall.
Chavez-Demoulin, V. and P. Embrechts. 2004. Smooth extremal models in insurance and
ﬁnance. Journal of Risk and Insurance 71(2):183–199.
Chavez-Demoulin, V., A. C. Davison and A. J. McNeil. 2005. A point process approach to
Value-at-Risk estimation. Quantitative Finance. Forthcoming.
Chavez-Demoulin, V., P. Embrechts and J. Neˇslehov´a. 2005. Quantitative models for operational risk: extremes, dependence and aggregation. Preprint, ETH Zurich.
Chekhlov, H., S. Uryasev and M. Zabarankin. 2005. Drawdown measure in portfolio optimization. International Journal of Theoretical and Applied Finance 8(1):13–58.
Chen, X. and Y. Fan. 2005. Estimation of copula-based semiparametric time series models.
Journal of Econometrics. Forthcoming.
. 2005. Pseudo-likelihood ratio tests for selecting semiparametric multivariate copula
models. Canadian Journal of Statistics 33(2). Forthcoming.
Cherubini, U., E. Luciano and W. Vecchiato. 2004. Copula Methods in Finance. Wiley.
Christoffersen, P. F., F. X. Diebold and T. Schuermann. 1998. Horizon problems and extreme
events in ﬁnancial risk management. Federal Reserve Bank of New York, Economic Policy
Review October 1998:109–118.
Clayton, D. G. 1978. A model for association in bivariate life tables and its application
in epidemiological studies of familial tendency in chronic disease incidence. Biometrika
65:141–151.
. 1996. Generalized linear mixed models. In Markov Chain Monte Carlo in Practice
(ed. W. R. Gilks, S. Richardson, and D. J. Spiegelhalter), pp. 275–301. London: Chapman
& Hall.
. 2002. Op risk modelling for extremes. Part 1. Small sample modelling. Operational
Risk 3(12):8–11.
. 2003. Op risk modelling for extremes. Part 2. Statistical methods. Operational Risk
4(1):6–9.
Coles, S. G. 2001. An Introduction to Statistical Modeling of Extreme Values. Springer.
Coles, S. G. and J. A. Tawn. 1991. Modelling extreme multivariate events. Journal of the
Royal Statistical Society: Series B (Statistical Methodology) 53(2):377–392.
Coles, S. G., J. Heffernan and J. A. Tawn. 1999. Dependence measures for extreme value
analyses. Extremes 2(4):339–365.
--- page 524 ---

508
References
Collin-Dufresne, P., R. Goldstein and J. Helwege. 2003. Is credit event risk priced? Modeling
contagion via the updating of beliefs. Preprint, Carnegie Mellon University.
Collin-Dufresne, P., R. Goldstein and J. Hugonnier. 2004. A general formula for valuing
defaultable securities. Econometrica 72:1377–1407.
Comte, F. and O. Lieberman. 2003. Asymptotic theory for multivariate GARCH processes.
Journal of Multivariate Analysis 84:61–84.
Connor, G. 1995. The three types of factor models: a comparison of their explanatory power.
Financial Analysts Journal 51(3):42–46.
Conover, W. J. 1999. Practical Nonparametric Statistics. Wiley.
Cont, R. 2005. Model uncertainty and its impact on the pricing of derivative instruments.
Mathematical Finance. Forthcoming.
Copeland, T. and V. Antikarov. 2001. Real Options. New York: Texere.
Cox, D. R. and V. Isham. 1980. Point Processes. London: Chapman & Hall.
Cox, J. C. and M. Rubinstein. 1985. Options markets. Englewood Cliffs, NJ: Prentice Hall.
Cox, J. C., J. E. Ingersoll and S.A. Ross. 1985.A theory of the term structure of interest rates.
Econometrica 53(2):385–407.
Cram´er, H. 1994a. Collected Works (ed. A. Martin-L¨of), vol. I. Springer.
. 1994b. Collected Works (ed. A. Martin-L¨of), vol. II. Springer.
Credit Suisse Financial Products. 1997. CreditRisk+: a credit risk management framework.
Technical Document. (Available from www.csfb.com/creditrisk.)
Crosbie, P. J. and J. R. Bohn. 2002. Modeling default risk. KMV working paper. (Available
from www.kmv.com.)
Crouhy, M., D. Galai and R. Mark. 2000.A comparative analysis of current credit risk models.
Journal of Banking and Finance 24:59–117.
. 2001. Risk Management. New York: McGraw-Hill.
Crowder, M. J. 1976. Maximum likelihood estimation for dependent observations. Journal
of the Royal Statistical Society: Series B (Statistical Methodology) 38:45–53.
Crowder, M. J., M. Davis and G. Giampieri. 2005. A hidden Markov model of default interaction. Quantitative Finance. Forthcoming.
Cruz, M. G. 2002. Modelling, Measuring and Hedging Operational Risk. Wiley.
Cruz, M. G. (ed.). 2004. Operational Risk Modelling and Analysis: Theory and Practice.
London: Risk Waters Group.
Dacorogna, M. M., R. Gen¸cay, U. M¨uller, R. B. Olsen and O. V. Pictet. 2001. An Introduction
to High-Frequency Finance. Academic Press.
Daley, D. J. and D.Vere-Jones. 2003. An Introduction to the Theory of Point Processes, vol. I:
Elementary Theory and Methods, 2nd edn. Springer.
Dan´ıelsson, J. and C. G. de Vries. 1997a. Tail index and quantile estimation with very high
frequency data. Journal of Empirical Finance 4:241–257.
. 1997b. Beyond the sample: extreme quantile and probability estimation. Preprint,
Tinbergen Institute, Rotterdam.
. 1997c. Value-at-Risk and extreme returns. In Extremes and Integrated Risk Management (ed. P. Embrechts), pp. 85–106. London: Risk Waters Group.
Dan´ıelsson, J., L. de Haan, L. Peng and C. G. de Vries. 2001. Using a bootstrap method to
choose the sample fraction in the tail index estimation. Journal of Multivariate Analysis
76:226–248.
Das, S. R., D. Dufﬁe and N. Kapadia. 2005. Common failings: how corporate defaults are
correlated. Preprint, Santa Clara University.
Daul, S., E. De Giorgi, F. Lindskog and A. J. McNeil. 2003. The grouped t-copula with an
application to credit risk. Risk 16(11):73–76.
David, F. N. 1947. A power function for tests of randomness in a sequence of alternatives.
Biometrika 34:335–339.
--- page 525 ---

References
509
Davis, M. H. A. 1993. Markov Models and Optimization. London: Chapman & Hall.
Davis, M. H. A. and V. Lo. 2001. Infectious defaults. Quantitative Finance 1(4):382–387.
Davison, A. C. 1984. Modelling excesses over high thresholds, with an application. In Statistical Extremes and Applications (ed. J. T. de Oliveira), pp. 461–482. Dordrecht: Reidel.
. 2003. Statistical Models. Cambridge University Press.
Davison, A. C. and R. L. Smith. 1990. Models for exceedances over high thresholds (with
discussion). Journal of the Royal Statistical Society: Series B (Statistical Methodology)
52:393–442.
deFontnouvelle, P., V. DeJesus-Rueff, J. Jordan and E. Rosengren. 2003. Using loss data to
quantify operational risk. Preprint, Federal Reserve Bank of Boston.
de la Vega, J. 1966. Confusi´on de confusiones. In Extraordinary Popular Delusions and the
Madness of Crowds & Confusi´on de Confusiones (ed. M. S. Fridson), pp. 125–211. Wiley.
de Matos, J. A. 2001. Theoretical Foundations of Corporate Finance. Princeton University
Press.
de Servigny,A. and O. Renault. 2002. Default correlation: empirical evidence.Working paper,
Standard & Poor’s, Risk Solutions.
DeVylder, F. 1996. Advanced Risk Theory. A Self-Contained Introduction. Brussels: Editions
de l’Universit´e de Bruxelles.
Deheuvels, P. 1980. The decomposition of inﬁnite order and extreme multivariate distributions. In Asymptotic Theory of Statistical Tests and Estimation (ed. I. M. Chakravarti),
pp. 259–286. Academic Press.
Dekkers, A. L. M. and L. de Haan. 1989. On the estimation of the extreme-value index and
large quantile estimation. Annals of Statistics 17(4):1795–1832.
. 1993. Optimal choice of sample fraction in extreme-value estimation. Journal of Multivariate Analysis 47:173–195.
Dekkers, A. L. M., J. H. J. Einmahl and L. de Haan. 1989. A moment estimator for the index
of an extreme-value distribution. Annals of Statistics 17:1833–1855.
Delbaen, F. 2000. Coherent Risk Measures. Pisa: Cattedra Galiliana, Scuola Normale Superiore.
. 2002. Coherent risk measures on general probability spaces. In Advances in Finance
and Stochastics (ed. K. Sandmann and P. J. Sch¨onbucher), pp. 1–37. Springer.
Delbaen, F., P. Grandits, T. Rheinl¨ander, D. Sampieri, M. Schweizer and C. Stricker. 2002.
Exponential hedging and entropic penalties. Mathematical Finance 12:99–123.
Dell’Aquila, R. and E. Ronchetti. 2005. Robust Statistics and Econometrics with Economic
and Financial Applications. Wiley. Forthcoming.
Demarta, S. andA. J. McNeil. 2005.The t copula and related copulas. International Statistical
Review 73(1):111–129.
Dembo, A., J.-D. Deuschel and D. Dufﬁe. 2004. Large portfolio losses. Finance Stochastics
8:3–16.
Denault, M. 2001. Coherent allocation of risk capital. Journal of Risk 4(1):7–21.
Denuit, M. and A. Charpentier. 2004. Math´ematiques de l’Assurance Non-Vie, vol. 1:
Principes Fondamentaux de Th´eorie de Risque. Paris: Economica.
Denuit, M., J. Dhaene, M. J. Goovaerts and R. Kaas. 2005. Actuarial Theory for Dependent
Risks. Wiley. Forthcoming.
Devlin, S. J., R. Gnanadesikan and J. R. Kettenring. 1975. Robust estimation and outlier
detection with correlation coefﬁcients. Biometrika 62(3):531–545.
. 1981. Robust estimation of dispersion matrices and principal components. Journal of
the American Statistical Association 76:354–362.
Diebold, F. X., T. Schuermann,A. Hickmann andA. Inoue. 1998. Scale models. Risk 11:104–
107.
--- page 526 ---

510
References
Dillmann, T. 2002. Modelle zur Bewertung von Optionen in Lebensversicherungsvertr¨agen.
Ulm: Ifa-Schriftenreihe.
Ding, Z. 1994. Time Series Analysis of Speculative Returns. PhD thesis, University of California, San Diego.
Ding, Z., C. W. Granger and R. F. Engle. 1993. A long memory property of stock market
returns and a new model. Journal of Empirical Finance 1:83–106.
D¨obeli, B., M. Leippold and P. Vanini. 2003. From operational risk to operational excellence.
In Advances in Operational Risk: Firm-Wide Issues for Financial Institutions, 2nd edn,
pp. 213–234. London: Risk Waters Group.
Does, R. J. M. M., K. C. B. Roes and A. Trip. 1999. Statistical Process Control in Industry:
Implementation and Assurance of SPC. Dordrecht: Kluwer.
Doherty, J. N.A. 2000. Integrated Risk Management. Techniques and Strategies for Reducing
Risk. New York: McGraw-Hill.
Dowd, K. 1998. Beyond Value at Risk: The New Science of Risk Management. Wiley.
Driessen, J. 2005. Is default event risk priced in corporate bonds? Review of Financial Studies
18(1):165–195.
Drzik, J., P. Nakada and T. Schuermann. 1998. Risk capital measurement in ﬁnancial institutions. Part 1: the debt-holder’s perspective. ERisk.com, 30 July, pp. 1–5.
Duffee, G. 1999. Estimating the price of default risk. Review of Financial Studies 12:197–226.
Dufﬁe, D. 2001. Dynamic Asset Pricing Theory, 3rd edn. Princeton University Press.
Dufﬁe, D. 2004. Time to adapt copula methods for modelling credit risk correlation. Risk
17(4):77.
Dufﬁe, D. and N. Gˆarleanu. 2001. Risk and valuation of collateralized debt obligations.
Financial Analysts Journal 57(1):41–59.
Dufﬁe, D. and R. Kan. 1996. A yield-factor model of interest rates. Mathematical Finance
6(4):921–950.
Dufﬁe, D. and D. Lando. 2001. Term structure of credit risk with incomplete accounting
observations. Econometrica 69:633–664.
Dufﬁe, D. and J. Pan. 1997. An overview of Value at Risk. Journal of Derivatives 4:7–49.
. 2001. Analytical Value-at-Risk with jumps and credit risk. Finance Stochastics 5:155–
180.
Dufﬁe, D. and K. Singleton. 1999a. Modeling term structures of defaultable bonds. Review
of Financial Studies 12:687–720.
. 1999b. Simulating correlated defaults. Preprint, Stanford University Graduate School
of Business.
. 2003. Credit Risk: Pricing, Measurement, and Management. Princeton University
Press.
Dufﬁe, D., D. Filipovic and W. Schachermayer. 2003. Afﬁne processes and applications in
ﬁnance. Annals of Applied Probability 13:984–1053.
Dufﬁe, D., J. Pan and K. Singleton. 2000. Transform analysis and asset pricing for afﬁne
jump diffusions. Econometrica 68:1343–1376.
Dufﬁe, D., M. Schroder and C. Skiadas. 1996. Recursive valuation of defaultable securities
and the resolution of uncertainty. Annals of Applied Probability 6:1075–1090.
Dumas, B., J. Fleming and R. E. Whaley. 1998. Implied volatility functions: empirical tests.
Journal of Finance 53(6):2059–2106.
Dunbar, N. 2000. Inventing Money. Wiley.
Eberlein, E. and U. Keller. 1995. Hyperbolic distributions in ﬁnance. Bernoulli 1:281–299.
Eberlein, E., U. Keller and K. Prause. 1998. New insights into smile, mispricing, and value
at risk: the hyperbolic model. Journal of Business 38:371–405.
Ebn¨other, S., P. Vanini, A. McNeil and P. Antolinez-Fehr. 2003. Operational risk: a practitioner’s view. Journal of Risk 5(3):1–15.
--- page 527 ---

References
511
Efron, B. F. and D. V. Hinkley. 1978. Assessing the accuracy of the maximum likelihood
estimator: observed versus expected Fisher information. Biometrika 65:457–487.
Efron, B. F. and R. J. Tibshirani. 1994. An Introduction to the Bootstrap. NewYork: Chapman
& Hall.
Egloff, D., M. Leippold and P. Vanini. 2004. A simple model of credit contagion. Preprint,
University of Zurich, Swiss Banking Institute.
Eisenberg, L. and T. H. Noe. 2001. Systemic risk in ﬁnancial systems. Management Science
47(2):236–249.
El Karoui, N. and M.-C. Quenez. 1995. Dynamic programming and pricing of contingent
claims in an incomplete market. SIAM Journal on Control and Optimization 33(1):27–66.
Elliot, R. J., M. Jeanblanc and M.Yor. 2000. On models of default risk. Mathematical Finance
10:179–195.
Embrechts, P. 2000.Actuarial versus ﬁnancial pricing of insurance. Risk Finance 1(4):17–26.
. 2002. Insurance analytics. British Actuarial Journal 8(IV):639–641.
Embrechts, P. and C. M. Goldie. 1980. On closure and factorization properties of subexponential and related distributions. Journal of the Australian Mathematical Society, Series A
29:243–256.
Embrechts, P. and G. Puccetti. 2005. Bounds for functions of dependent risks. Finance
Stochastics. Forthcoming.
Embrechts, P., R. Frey and H. Furrer. 2001. Stochastic processes in insurance and ﬁnance.
In Handbook of Statistics (ed. D. N. Shanbag and C. R. Rao), vol. 19, pp. 365–412.
Amsterdam: North-Holland.
Embrechts, P., H. Furrer and R. Kaufmann. 2003. Quantifying regulatory capital for operational risk. Derivatives Use, Trading & Regulation 9(3):217–233.
Embrechts, P., R. Gr¨ubel and S. Pitts. 1993. Some applications of the fast Fourier transform
algorithm in insurance mathematics. Statistica Neerlandica 47:59–75.
Embrechts, P., A. H¨oing and A. Juri. 2003. Using copulae to bound the Value-at-Risk for
functions of dependent risks. Finance Stochastics 7(2):145–167.
Embrechts, P.,A. H¨oing and G. Puccetti. 2005. WorstVaR scenarios. Insurance: Mathematics
and Economics. Forthcoming.
Embrechts, P., R. Kaufmann and P. Patie. 2005. Strategic long-term ﬁnancial risks: single
risk factors. Computational Optimization and Applications. Forthcoming.
Embrechts, P., R. Kaufmann and G. Samorodnitsky. 2004. Ruin theory revisited: stochastic
models for operational risk. In Risk Management for Central Bank Foreign Reserves (ed.
C. Bernadell et al.), pp. 243–261. Frankfurt: European Central Bank.
Embrechts, P., C. Kl¨uppelberg and T. Mikosch. 1997. Modelling Extremal Events for Insurance and Finance. Springer.
Embrechts, P., A. J. McNeil and D. Straumann. 2002. Correlation and dependency in risk
management: properties and pitfalls. In Risk Management: Value at Risk and Beyond (ed.
M. Dempster), pp. 176–223. Cambridge University Press.
Embrechts, P., J. L. Jensen, M. Maejima and J. L. Teugels. 1985. Approximations for compound Poisson and P´olya processes. Advances in Applied Probability 17:623–637.
Emmer, S., C. Kl¨uppelberg and R. Korn. 2001. Optimal portfolios with bounded capital at
risk. Mathematical Finance 11(4):365–384.
Engle,R.F.1982.Autoregressiveconditionalheteroskedasticitywithestimatesofthevariance
of UK inﬂation. Econometrica 50:987–1008.
. 2002. Dynamic conditional correlation—a simple class of multivariate GARCH models. Journal of Business and Economic Statistics 20:339–350.
Engle, R. F. and T. Bollerslev. 1986. Modeling the persistence of conditional variances.
Econometric Review 5:1–50.
--- page 528 ---

512
References
Engle, R. F. and K. F. Kroner. 1995. Multivariate simultaneous generalized ARCH. Econometric Theory 11:122–150.
Engle, R. F. and K. Sheppard. 2001. Theoretical and empirical properties of dynamic conditionalcorrelationmultivariateGARCH.TechnicalReport2001-15,UniversityofCalifornia
at San Diego.
Fahrmeir, L. and G. Tutz. 1994. Multivariate Statistical Modelling Based on Generalized
Linear Models. Springer.
Falk, M., J. H¨usler and R. D. Reiss. 1994. Laws of Small Numbers: Extremes and Rare Events.
Basel: Birkh¨auser.
Fang, H. B. and K. T. Fang. 2002. The meta-elliptical distributions with given marginals.
Journal of Multivariate Analysis 82:1–16.
Fang, K.-T., S. Kotz and K.-W. Ng. 1987. Symmetric Multivariate and Related Distributions.
London: Chapman & Hall.
FederalReserveSystem.2005.Resultsofthe2004lossdatacollectionexerciseforoperational
risk. Preprint, Federal Reserve Bank of Boston.
Feilmeier, M. and J. Bertram. 1987. Anwendung Numerischer Methoden in der Risikotheorie.
Karlsruhe: Versicherungswirtschaft.
Feller, W. 1971. An Introduction to Probability Theory and Its Applications, vol. II. Wiley.
Field, P. (ed.). 2003. Modern Risk Management: A History. London: Risk Waters Group.
Fischer, T. 2003. Risk capital allocation by coherent risk measures based on one-sided
moments. Insurance: Mathematics and Economics 32:135–146.
Fisher, R. A. and L. H. C. Tippett. 1928. Limiting forms of the frequency distribution of
the largest or smallest member of a sample. Proceedings of the Cambridge Philosophical
Society 24:180–190.
Focardi, F. J. and S. M. Fabozzi. 2004. A percolation approach to modeling credit loss distribution under contagion. Journal of Risk 7:75–94.
F¨ollmer, H. 1994. Stock price ﬂuctuation as a diffusion in a random environment. Philosophical Transactions of the Royal Society of London, Series A 347:471–483.
F¨ollmer, H. and P. Leukert. 1999. Quantile hedging. Finance Stochastics 3:251–273.
. 2002. Convex measures of risk and trading constraints. Finance and Stochastics 6:429–
447.
. 2004. Stochastic Finance: An Introduction in Discrete Time, 2nd edn. Berlin: Walter
de Gruyter.
F¨ollmer, H. and M. Schweizer. 1991. Hedging of contingent claims under incomplete information. In Applied Stochastic Analysis (ed. M. H. A. Davis and R. J. Elliot), pp. 389–414.
London: Gordon and Breach.
F¨ollmer, H. and D. Sondermann. 1986. Hedging of non-redundant contingent-claims. In Contributions to Mathematical Economics (ed. W. Hildenbrand and A. Mas-Colell), pp. 147–
160. Amsterdam: North-Holland.
Fons, J. S. 1994. Using default rates to model the term structure of credit risk. Financial
Analysts Journal 50:25–33.
Fornari, F. and A. Mele. 1997. Signa and volatility switching ARCH models. Journal of
Applied Econometrics 12:49–65.
Fortin, I. and C. Kuzmics. 2002. Tail-dependence in stock-return pairs. International Journal
of Intelligent Systems in Accounting, Finance & Management 11:89–107.
Frachot, A. 2004. Operational risk: from theory to practice. Presentation, The Three Way
Seminar, Versailles, 4 May 2004.
Frachot,A., P. Georges and T. Roncalli. 2001. Loss distribution approach for operational risk.
Working paper, Cr´edit Lyonnais, Groupe de Recherche Op´erationelle.
Frahm, G. 2004. Generalized Elliptical Distributions: Theory and Applications. PhD thesis, Faculty of Economics, Business Administration and Social Sciences, University of
Cologne.
--- page 529 ---

References
513
Frahm, G., M. Junker andA. Szimayer. 2003. Elliptical copulas: applicability and limitations.
Statistics & Probability Letters 63:275–286.
Frank, M. 1979. On the simultaneous additivity of f (x, y) and x +y −f (x, y). Aequationes
Mathematicae 19:194–226.
Frank, M., R. Nelsen and B. Schweizer. 1987. Best-possible bounds on the distribution of
a sum—a problem of Kolmogorov. Probability Theory and Related Fields 74:199–211.
Fr´echet, M. 1951. Sur les tableaux de corr´elation dont les marges sont donn´ees. Annales de
l’Universit´e de Lyon, S´erie A 9:53–77.
Frees, E. W. and E.A. Valdez. 1997. Understanding relationships using copulas. North American Actuarial Journal 2(1):1–25.
Frey, R. 1998. Perfect option replication for a large trader. Finance Stochastics 2:115–148.
. 2000. Market illiquidity as a source of model risk in dynamic hedging. In Model Risk
(ed. R. Gibson), pp. 125–136. London: Risk Waters Group.
Frey,R.andJ.Backhaus.2004.Portfoliocreditriskmodelswithinteractingdefaultintensities:
a Markovian approach. Preprint, University of Leipzig.
Frey, R. and A. J. McNeil. 2001. Modelling dependent defaults. ETH E-Collection, ETH
Zurich. (Available from www.e-collection.ethbib.ethz.ch/show?type=bericht&nr=273.)
. 2002. VaR and expected shortfall in portfolios of dependent credit risks: conceptual
and practical insights. Journal of Banking and Finance 26:1317–1344.
. 2003. Dependent defaults in models of portfolio credit risk. Journal of Risk 6(1):59–92.
Frey, R.,A. J. McNeil and M. Nyfeler. 2001. Copulas and credit models. Risk 14(10):111–114.
Frittelli, E., and M. Rosazza. 2002. Putting order in risk measures. Journal of Banking and
Finance 26:1473–1486.
Froot,K.A.2005.Riskmanagement,capitalbudgetingandcapitalstructurepolicyforinsurers
and reinsurers. Journal of Risk and Insurance. Forthcoming.
Froot, K. A. and J. C. Stein. 1998. Risk management, capital budgeting and capital structure
policy for ﬁnancial institutions: an integrated approach. Journal of Financial Economics
47:55–82.
Froot, K.A., D. S. Scharfstein and J. C. Stein. 1993. Risk management: coordinating corporate
investment and ﬁnancing policies. Journal of Finance 48:1629–1658.
Frye, J. 2000. Depressing recoveries. Preprint, Federal Reserve Bank of Chicago, 2000. A
short version appeared in Risk 13(11):106–111.
Gagliardini, P. and C. Gourieroux. 2005. Stochastic migration models with application to
corporate risk. Journal of Financial Econometrics 3(2):188–226.
Galambos, J. 1975. Order statistics of samples from multivariate distributions. Journal of the
American Statistical Association 70:674–680.
. 1987. The Asymptotic Theory of Extreme Order Statistics. Melbourne: Krieger.
Gardner Jr, E. S. 1985. Exponential smoothing: the state of the art. Journal of Forecasting
2:1–21.
Geffroy, J. 1958. Contributions `a la theorie des valeurs extr`emes. Publications de l’Institut
de Statistique de l’Universit´e de Paris 7–8:37–185.
Geman, H. 2005. Commodities and Commodity Derivatives: Modelling and Pricing for Agriculturals, Metals and Energy. Wiley.
Gen¸cay, R. and F. Sel¸cuk. 2004. Extreme value theory andValue-at-Risk: relative performance
in emerging markets. International Journal of Forecasting 20:287–303.
Gen¸cay, R., F. Sel¸cuk andA. Ulug¨ulyaˇgci. 2003. High volatility, thick tails and extreme value
theory in Value-at-Risk estimation. Insurance: Mathematics and Economics 33:337–356.
Genest, C. and J. MacKay. 1986. The joy of copulas: bivariate distributions with uniform
marginals. American Statistician 40:280–285.
Genest, C. and L. Rivest. 1993. Statistical inference procedures for bivariate archimedean
copulas. Journal of the American Statistical Association 88:1034–1043.
--- page 530 ---

514
References
Genest, C., K. Ghoudi and L. Rivest. 1995. A semi-parametric estimation procedure of
dependence parameters in multivariate families of distributions. Biometrika 82:543–552.
. 1998. Commentary on “Understanding relationships using copulas” by E. W. Frees
and E. A. Valdez. North American Actuarial Journal 2:143–149.
Genton, M. G. (ed.). 2004. Skew-Elliptical Distributions and Their Applications. Boca Raton,
FL: Chapman & Hall/CRC.
Gibson, R. (ed.). 2000. Model Risk, Concepts, Calibration and Pricing. London: Risk Waters
Group.
Giese, G. 2003. Enhancing CreditRisk+. Risk 16(4):73–77.
Giesecke,K.2004.Creditriskmodelingandvaluation:anintroduction.InCreditRisk:Models
and Management (ed. D. Shimko), vol. 2. London: Risk Waters Group. (Reprinted in 2004:
Journal of Financial Risk Management 2(1):1–40.)
. 2005. Default and information. Journal of Economic Dynamics and Control. Forthcoming.
Giesecke, K. and L. R. Goldberg. 2004. Sequential defaults and incomplete information.
Journal of Risk 7:1–26.
. 2005. The market price of credit risk. Preprint, Cornell University.
Giesecke, K. and S. Weber. 2004. Cyclical correlation, credit contagion and portfolio losses.
Journal of Banking and Finance 28:3009–3036.
. 2005. Credit contagion and aggregate losses. Journal of Economic Dynamics and
Control. Forthcoming.
Gin´e, E. M. 1975. Invariant tests for uniformity on compact Riemannian manifolds based on
Sobolev norms. Annals of Statistics 3(6):1243–1266.
Giri, N. C. 1996. Multivariate Statistical Analysis. New York: Marcel Dekker.
Glasserman, P. 2003a. Monte Carlo Methods in Financial Engineering. Springer.
. 2003b. Tail approximations for portfolio credit risk. Preprint, Columbia University,
Graduate School of Business.
Glasserman, P. and J. Li. 2003a. Importance sampling for portfolio credit risk. Preprint,
Columbia University, Graduate School of Business.
. 2003b. Importance sampling for a mixed Poisson model of portfolio credit risk. In Proceedings of the 2003 Winter Simulation Conference (ed. S. Chick, P. J. S´anchez, D. Ferrin,
and D. J. Morrice).
Glasserman, P., P. Heidelberger and P. Shahabuddin. 1999. Importance sampling and stratiﬁcation for Value at Risk. In Proceedings of the 6th International Conference on Computational Finance (ed. Y. S. Abu-Mostafa, B. LeBaron, A. W. Lo and A. S. Weigand).
Cambridge, MA: MIT Press.
Glosten, L. R., R. Jagannathan and D. E. Runkle. 1993. On the relation between the expected
value and the volatility of the nominal excess return on stocks. Journal of Finance
48(5):1779–1801.
Gnanadesikan, R. 1997. Methods for Statistical Data Analysis of Multivariate Observations,
2nd edn. Wiley.
Gnanadesikan,R.andJ.R.Kettenring.1972.Robustestimates,residuals,andoutlierdetection
with multiresponse data. Biometrics 28:81–124.
Gnedenko, B. V. 1941. Limit theorems for the maximal term of a variational series. Comptes
Rendus (Doklady) de L’Acad´emie des Sciences de l’URSS 32:7–9.
Gnedenko, B. V. 1943. Sur la distribution limite du terme maximum d’une s´erie al´eatoire.
Annals of Mathematics 44:423–453.
Goovaerts, M. J., F. De Vylder and J. Haezendonck. 1984. Insurance Premiums. Amsterdam:
North-Holland.
Goovaerts, M. J., J. Dhaene and R. Kaas. 2003. Capital allocation derived from risk measures.
North American Actuarial Journal 7:44–49.
--- page 531 ---

References
515
Goovaerts, M. J., E. van den Boor and R. J. A. Laeven. 2005. Managing economic and virtual economic capital within ﬁnancial conglomerates. North American Actuarial Journal.
Forthcoming.
Goovaerts, M. J., R. Kaas, J. Dhaene and Q. Tang. 2003. A uniﬁed approach to generate risk
measures. ASTIN Bulletin 33(2):173–191.
Gordy, M. B. 2000. A comparative anatomy of credit risk models. Journal of Banking and
Finance 24:119–149.
. 2001. A risk-factor model foundation for ratings-based capital rules. Journal of Financial Intermediation 12:199–232.
Gordy, M. B. 2002. Saddlepoint approximation of CreditRisk+. Journal of Banking and
Finance 26:1335–1353.
Gordy, M. B. and E. Heitﬁeld. 2002. Estimating default correlations from short panels of
credit rating performance data. Technical Report, Federal Reserve Board.
Gourieroux, C. 1997. ARCH-Models and Financial Applications. Springer.
Gourieroux, C. and J. Jasak. 2001. Financial Econometrics: Problems, Models, and Methods.
Princeton University Press.
Gourieroux, C. and O. Scaillet. 2000. Sensitivity analysis ofValues at Risk. Journal of Empirical Finance 7:225–245.
Gourieroux, C., A. Montfort and A. Trognon. 1984. Pseudo maximum likelihood methods:
theory. Econometrica 52:681–700.
Graham, J. R. and D. A. Rogers. 2002. Do ﬁrms hedge in response to tax incentives? Journal
of Finance 57(2):815–839.
Grandell, J. 1997. Mixed Poisson Processes. London: Chapman & Hall.
Greenspan,A. 2002. Speech before the Council on Foreign Relations. In International Financial Risk Management, Washington, DC, 19th November.
Gregory, J. (ed.). 2003. Credit Derivatives:The Deﬁnitive Guide. London: RiskWaters Group.
Gr¨ubel, R. and R. Hermesmeier. 1999. Computation of compound distributions. I. Aliasing
errors and exponential tilting. ASTIN Bulletin 29(2):197–214.
. 2000. Computation of compound distributions. II. Discretization errors and Richardson
extrapolation. ASTIN Bulletin 30(2):309–331.
Gumbel, E. J. 1958. Statistics of Extremes. New York: Columbia University Press.
Haaf, H., O. Reiss and J. Schoenmakers. 2004. Numerically stable computation of
CreditRisk+. Journal of Risk 6(4):1–10.
Haan, L. de. 1985. Extremes in higher dimensions: the model and some statistics. In Proceedings of the 45th Session International Statistical Institute, paper 26.3. The Hague:
International Statistical Institute.
Haan, L. de and S. I. Resnick. 1977. Limit theory for multivariate sample extremes. Zeitschrift
f¨ur Wahrscheinlichkeitstheorie und Verwandte Gebiete 40:317–337.
Haan, L. de and H. Rootz´en. 1993. On the estimation of high quantiles. Journal of Statistical
Planning and Inference 35:1–13.
Haan, L. de, S. I. Resnick, H. Rootz´en and C. G. de Vries. 1989. Extremal behaviour of solutions to a stochastic difference equation with applications to ARCH processes. Stochastic
Processes and Their Applications 32:213–224.
Hafner, C. M. and P. H. Franses. 2003. A generalized dynamic conditional correlation model
for many asset returns. Econometric Institute Report 323, Erasmus University, Rotterdam.
Hall, P. G. 1982. On some simple estimates of an exponent of regular variation. Journal of
the Royal Statistical Society: Series B (Statistical Methodology) 44:37–42.
. 1990. Using the bootstrap to estimate mean squared error and select smoothing parameter in nonparametric problems. Journal of Multivariate Analysis 32:177–203.
Hamilton, J. 1994. Time Series Analysis. Princeton University Press.
--- page 532 ---

516
References
Hampel, F. R., E. M. Ronchetti, P. J. Rousseeuw and W. A. Stahel. 1986. Robust Statistics:
The Approach Based on Inﬂuence Functions. Wiley.
Hancock, J., P. Huber and P. Koch. 2001. The economics of insurance: how insurers create
value for shareholders. Technical Report, Swiss Re, Zurich.
Hardy, M. 2003. Investment Guarantees. Wiley.
Haug, E. G. 1998. Option Pricing Formulas. New York: McGraw-Hill.
Hawke Jr, J. D. 2003. Remarks before the Institute of International Bankers, 3 March 2003,
Washington, DC. (Available from www.occ.treas.gov/ftp/release/2003-15a.pdf/.)
Hawkes, A. G. 1971. Point spectra of some mutually exciting point processes. Journal of the
Royal Statistical Society: Series B (Statistical Methodology) 33:438–443.
Heffernan, J. E. and J.A. Tawn. 2004.A conditional approach for multivariate extreme values.
Journal of the Royal Statistical Society: Series B (Statistical Methodology) 66(3):497–546.
Hesselager, O. 1996. Recursions for certain bivariate counting distributions and their compound distributions. ASTIN Bulletin 26(1):35–52.
Hilberink, B. and C. Rogers. 2002. Optimal capital structure and endogenous default. Finance
and Stochastics 6(2):237–263.
Hill, B. M. 1975. A simple general approach to inference about the tail of a distribution.
Annals of Statistics 3:1163–1174.
H¨offding, W. 1940. Massstabinvariante Korrelationstheorie. Schriften des Mathematischen
Seminars und des Instituts f¨ur Angewandte Mathematik der Universit¨at Berlin 5:181–233.
Hogg, R. V. and S. A. Klugman. 1984. Loss Distributions. Wiley.
Horst, U. 2004. Stochastic cascades, credit contagion and large portfolio losses. Preprint,
Humboldt Universit¨at, Berlin.
Hosking, J. R. M. 1985. Maximum likelihood estimation of the parameters of the generalized
extreme-value distribution. Applied Statistics 34:301–310.
Hosking, J. R. M. and J. R.Wallis. 1987. Parameter and quantile estimation for the generalized
Pareto distribution. Technometrics 29:339–349.
Hosking, J. R. M., J. R. Wallis and E. F. Wood. 1985. Estimation of the generalized extremevalue distribution by the method of probability-weighted moments. Technometrics 27:251–
261.
Hsing, T. 1991. On tail index estimation using dependent data. Annals of Statistics 19:1547–
1569.
Hu,Y.-T.,R.KieselandW.Perraudin.2002.Theestimationoftransitionmatricesforsovereign
credit ratings. Journal of Banking and Finance 26:1383–1406.
Huang, J. and M. Huang. 2003. How much of the corporate-treasury yield spread is due
to credit risk? Results from a new calibration approach. Preprint, Graduate School of
Business, Stanford University.
Huber, P. J. 1981. Robust Statistics. Wiley.
Hull,J.1997.Options,FuturesandOtherDerivatives,3rdedn.EnglewoodCliffs,NJ:Prentice
Hall.
Hull, J. and A. White. 1998. Incorporating volatility updating into the historical simulation
method for VaR. Journal of Risk 1(1):5–19.
. 2001. Valuing credit default swaps. II. Modelling default correlations. Journal of
Derivatives 8(3):12–22.
. 2004. Valuation of a CDO and an nth to default CDS without Monte Carlo simulation.
Journal of Derivatives 12:8–23.
Hult, H. and F. Lindskog. 2002. Multivariate extremes, aggregation and dependence in elliptical distributions. Advances in Applied Probability 34:587–608.
Hutchinson, T. P. and C. D. Lai. 1990. Continuous Bivariate Distributions, Emphasizing
Applications. Adelaide: Rumsby Scientiﬁc Publishing.
--- page 533 ---

References
517
Iman, R. L. and W. J. Conover. 1982. A distribution-free approach to inducing rank correlation among input variables. Communications in Statistics: Simulation and Computation
11:311–334.
Jacod, J. 1975. Multivariate point processes: predictable projection, Radon–Nikodym derivatives, representation of martingales. Zeitschrift f¨ur Wahrscheinlichkeitstheorie und Verwandte Gebiete 31:235–253.
Jacod, J. and A. S. Shiryaev. 1987. Limit Theorems for Stochastic Processes. Springer.
Jaeger, L. 2005. Through the Alpha Smoke Screens: A Guide to Hedge Fund Return Sources.
New York: Institutional Investor Books.
Jarque, C. M. and A. K. Bera. 1987. A test for normality of observations and regression
residuals. International Statistical Review 55(5):163–172.
Jarrow, R. A. 1994. Derivative securities markets, market manipulation and option pricing
theory. Journal of Financial and Quantitative Analysis 29:241–261.
Jarrow, R. A. and P. Protter. 2004. Structural versus reduced-form models: a new information
based perspective. Journal of Investment Management 2:1–10.
Jarrow, R. A. and S. M. Turnbull. 1995. Pricing derivatives on ﬁnancial securities subject to
credit risk. Journal of Finance 50(1):53–85.
. 1999. Derivative Securities, 2nd edn. Cincinnatti, OH: South Western Publishing.
Jarrow, R. A. and F. Yu. 2001. Counterparty risk and the pricing of defaultable securities.
Journal of Finance 53:2225–2243.
Jarrow, R. A., D. Lando and S. M. Turnbull. 1997. A Markov model for the term structure of
credit risk spreads. Review of Financial Studies 10:481–523.
Jarrow, R.A., D. Lando and F.Yu. 2005. Default risk and diversiﬁcation: theory and empirical
implications. Mathematical Finance 15:1–26.
Jeantheau, T. 1998. Strong consistency of estimators of multivariate ARCH models. Econometric Theory 14(1):70–86.
Jensen, B. A. and J. A. Nielsen. 1996. Pricing by no-arbitrage. In Time Series Models in
Econometrics, Finance and Other Fields (ed. D. R. Cox, D.V. Hinkley and O. E. Barndorff-
Nielsen). London: Chapman & Hall.
Jensen, J. L. 1995. Saddlepoint Approximations. Oxford: Clarendon.
Jewell, W. S. 1990. Credibility prediction of ﬁrst and second moments in the hierarchical
model. In Festgabe B¨uhlmann, pp. 81–110. Bern: St¨ampﬂi.
Joag-Dev, K. 1984. Measures of dependence. In Handbook of Statistics (ed. P. R. Krishnaiah),
vol. 4, pp. 79–88. New York: North-Holland/Elsevier.
Joe, H. 1993. Parametric family of multivariate distributions with given margins. Journal of
Multivariate Analysis 46:262–282.
. 1997. Multivariate Models and Dependence Concepts. London: Chapman & Hall.
Joe, H., R. L. Smith and I.Weissman. 1992. Bivariate threshold methods for extremes. Journal
of the Royal Statistical Society: Series B (Statistical Methodology) 54(1):171–183.
Johnson, N. L. and S. Kotz. 1969. Distributions in Statistics: Discrete Distributions. Boston,
MA: Houghton Mifﬂin.
Johnson, R. A. and D. W. Wichern. 2002. Applied Multivariate Statistical Analysis, 5th edn.
Upper Saddle River, NJ: Prentice Hall.
Jorion, P. 2000. Risk management lessons from Long-Term Capital Management. European
Financial Management 6:277–300.
. 2001. Value at Risk: The New Benchmark for Measuring Financial Risk, 2nd edn. New
York: McGraw-Hill.
. 2002a. Financial Risk Manager Handbook 2001–2002. Wiley.
. 2002b. Fallacies about the effects of market risk management systems. Journal of Risk
5(1):75–96.
