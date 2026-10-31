# Quantitative Risk Management_ Concepts, Techniques, and -- Alexander J_ McNeil, Rüdiger Frey, Paul Embrechts -- Princeton series in finance, -- isbn13 9780691122557 -- 478a0059673fecd0c76229cd3d8884e7 -- Anna’s Arc.pdf — pages 172–191

--- page 172 ---

156
4. Financial Time Series
−4
−2
0
2
4
6
−6
−4
−2
0
6
Quantiles of t distribution
Standardized residuals
2
4
Figure 4.11.
Microsoft log-returns 1997–2000; QQplot of residuals from a GARCH(1, 1)
model with leverage against a Student t distribution with 6.30 degrees of freedom.
Table 4.2.
Analysis of Microsoft log-returns for the period 1997–2000; ML estimates of
parameters and standard errors for a GARCH(1, 1) model with a leverage term under the
assumption of t innovations.
Parameter
Estimate
Standard error
Ratio
µ
9.35 × 10−4
7.21 × 10−4
1.30
α0
7.79 × 10−5
3.07 × 10−5
2.54
α1
0.108
0.0369
2.91
β
0.778
0.0673
11.57
δ
−0.178
0.123
−1.45
t distribution is 6.30 (the standard error is 1.07) and a QQplot of the residuals against
this reference distribution reveals a satisfactory correspondence (see Figure 4.11).
The estimates of the remaining parameters (with standard errors) in this model are
given in Table 4.2.
Notes and Comments
The ARCH process was originally proposed by Engle (1982), and the GARCH
process by Bollerslev (1986), who gave the condition for covariance stationarity.
Overview texts on GARCH models include the book by Gourieroux (1997) and
a number of useful review articles including Bollerslev, Chou and Kroner (1992),
Bollerslev, Engle and Nelson (1994) and Shephard (1996). There are also substantial
sections on GARCH models in the books by Alexander (2001), Tsay (2002) and
--- page 173 ---

4.3. GARCH Models for Changing Volatility
157
Zivot and Wang (2003). The IGARCH model was ﬁrst discussed by Engle and
Bollerslev (1986).
The condition for strict stationarity of GARCH models was derived by Nelson
(1990) in the case of the GARCH(1, 1) model and Bougerol and Picard (1992) for
GARCH(p, q). The necessary theory involves the study of stochastic recurrence
relations and goes back to Kesten (1973); Brandt (1986) is also a useful reference.
Readable accounts of this theory may be found in Embrechts, Kl¨uppelberg and
Mikosch (1997), Mikosch and St˘aric˘a (2000) and Mikosch (2003).
For more on the derivation of conditional likelihood functions for ARCH and
GARCH models see Hamilton (1994) and Tsay (2002). The BHHH algorithm
(Berndt et al. 1974) is the most commonly used approach to numerically maximizing the likelihood. For an informative general discussion of numerical optimization
procedures in the context of maximum likelihood see Hamilton (1994, pp. 133–142).
Standard general references on the QML approach areWhite (1981) and Gourieroux,
Montfort and Trognon (1984).
The essential asymptotic properties of MLEs and QMLEs in GARCH models
are described in many publications, but the detailed mathematical proof has often
lagged behind the assertions. Early papers appealed to regularity conditions for conditionally speciﬁed models such as those of Crowder (1976), which are essentially
unveriﬁable. Lee and Hansen (1994) and Lumsdaine (1996) proved consistency and
asymptotic normality of QMLEs in the GARCH(1, 1) model. More recently, Berkes,
Horv´ath and Kokoszka (2003) have extended this to the GARCH(p, q) model under
minimal assumptions, and Mikosch and Straumann (2005) and Straumann (2003)
have given similar results for a wide variety of ﬁrst-order models.
From a more practical point-of-view, it is not easy to estimate GARCH model
parameters to a high degree of accuracy because of the ﬂatness of the typical likelihoods and the non-negligible inﬂuence of starting values in ﬁnite samples. Readers
who write their own code may wish to compare their estimates with benchmark
studies by McCullough and Renfro (1999) and Brooks, Burke and Persand (2001).
Alternative innovation distributions to the Gaussian and scaled t distributions that
have been considered include the generalized error distribution (GED) in Nelson
(1991) and the normal inverse Gaussian (NIG) in Venter and de Jongh (2001); the
latter authors present extensive evidence that the NIG is a good choice of innovation
distribution for practical work and that GARCH inference based on the NIG is
relatively robust to misspeciﬁcation of the distribution.
A great many extensions to the GARCH class have been proposed and thorough surveys may be found in Bollerslev, Engle and Nelson (1994) and Shephard
(1996). Leverage effects in the GARCH model and the more general PGARCH
(power GARCH) model are examined in Ding, Granger and Engle (1993). Various
threshold GARCH models have been suggested; the model (4.32) is of the type suggested by Glosten, Jagannathan and Runkle (1993), while (4.33) is the switchingvolatility GARCH (SV-GARCH) model of Fornari and Mele (1997). There have
been proposals for non-parametric ARCH and GARCH modelling, including the
--- page 174 ---

158
4. Financial Time Series
multiplicative ARCH(p)-model of Yang, H¨ardle and Nielsen (1999) and the nonparametric GARCH procedure of B¨uhlmann and McNeil (2002).
4.4
Volatility Models and Risk Estimation
In this section we elaborate on some issues raised in the discussion of standard
methods for market risks in Section 2.3. At that point the discussion of dynamic
risk estimation procedures was kept relatively vague, but now, armed with more
knowledge of time series models in general and GARCH in particular, we can give
some more detail. The main issues are the estimation of conditional risk measures
like VaR and expected shortfall and the backtesting of such estimates. Estimating
VaR for a future time period requires us to be able to forecast volatility and we start
with this topic.
4.4.1
Volatility Forecasting
As in our earlier discussion of time series prediction in Section 4.2.5, we describe a
model-based strategy using a GARCH-type model, before presenting the more ad
hoc technique of exponentially weighted moving-average (EWMA) prediction.
GARCH-based volatility prediction.
Suppose that the return data Xt−n+1, . . . , Xt
follow a particular model in the GARCH family.We want to forecast future volatility,
i.e. to predict the value of σt+h for h ⩾1. This is closely related to the problem of
predicting X2
t+h and uses an analogous method to that used for prediction inARMA
models in Section 4.2.5. We again assume that we have access to the inﬁnite history
of the process up to time t, represented by Ft = σ({Xs : s ⩽t}), and then adapt
our prediction formula to take account of the ﬁniteness of the sample.
Assume that the GARCH model has been ﬁtted and its parameters estimated; we
will suppress estimator notation for the parameters in the remainder of the section.
We make calculations for simple models, from which the general procedure for more
complex models should be clear.
Example 4.25 (prediction in the GARCH(1, 1) model). Suppose that we use
a pure GARCH(1, 1) model conforming to Deﬁnition 4.20. Assume the model is
covariance stationary so that E(X2
t ) = E(σ 2
t ) < ∞. Since (Xt)t∈Z is a martingale
difference, optimal predictions of Xt+h are zero.A natural prediction of X2
t+1 based
on Ft is its conditional mean σ 2
t+1 given by
E(X2
t+1 | Ft) = σ 2
t+1 = α0 + α1X2
t + βσ 2
t ,
and if E(X4
t ) < ∞, then this is the optimal squared error prediction. Note that the
prediction of the random variable X2
t+1 based on the information Ft is the value of
σ 2
t+1, which is known at time t, being a function of the inﬁnite history of the process.
(The process (σt)t∈Z is said to be previsible.)
In practice we have to make an approximation based on this formula because the
inﬁnite series of past values that would allow us to calculate σ 2
t is not available to us.
A natural approach in applications is to approximate σ 2
t by an estimate of squared
--- page 175 ---

4.4. Volatility Models and Risk Estimation
159
volatility ˆσ 2
t calculated from the residual equations (4.42). Our approximate forecast
of X2
t+1 also functions as an estimate of the squared volatility at time t + 1 and is
given by
ˆσ 2
t+1 = ˆE(X2
t+1 | Ft) = α0 + α1X2
n + β ˆσ 2
t .
(4.43)
Thus equation (4.43) can be thought of as a recursive scheme for estimating volatility
one step ahead.
When we look h > 1 steps ahead given the information at time t, both X2
t+h and
σ 2
t+h are rvs. Their predictions coincide and are
E(X2
t+h | Ft) = E(σ 2
t+h | Ft)
= α0 + α1E(X2
t+h−1 | Ft) + βE(σ 2
t+h−1 | Ft)
= α0 + (α1 + β)E(X2
t+h−1 | Ft),
so that a general formula is
E(X2
t+h | Ft) = α0
h−1

i=0
(α1 + β)i + (α1 + β)h−1(α1X2
t + βσ 2
t ),
and we obtain a practical formula by substituting an estimate of squared volatility ˆσ 2
t as before. As h →∞we observe that E(σ 2
t+h | Ft) →α0/(1 −α1 −β1),
almost surely, so that the prediction of squared volatility converges to the unconditional variance of the process. A concrete example of volatility prediction in a
GARCH(1, 1) model is given in Figure 4.12 for the Microsoft data analysed in
Example 4.24.
We now consider a second example, which combines what we know about prediction in ARMA and GARCH models.
Example 4.26 (prediction in an ARMA(1, 1)–GARCH(1, 1) model). Consider
a process of the form Xt −µt = εt = σtZt, where µt and σt are Ft−1-measurable
rvs describing, respectively, an ARMA(1, 1) model and a GARCH(1, 1) model as in
Deﬁnition4.22.PredictionformulasforthismodelfolloweasilyfromExamples4.15
and 4.25. We calculate that
E(Xt+h | Ft) = µ + φh(Xt −µ) + φh−1θεt,
(4.44)
var(Xt+h | Ft) = α0
h−1

i=0
(α1 + β)i + (α1 + β)h−1(α1ε2
t + βσ 2
t ),
(4.45)
and these are approximated by substituting inferred values for εt and σt obtained
from the residual equations (4.42). Equation (4.44) yields predictions of µt+h or
Xt+h, and equation (4.45) yields predictions of ε2
t+h or σ 2
t+h.
Exponential smoothing for volatility.
Suppose we believe our return data follow
some kind of underlying time series model in which a volatility (conditional standard
deviation) is deﬁned, but that we do not wish to specify the exact parametric model.
--- page 176 ---

160
4. Financial Time Series
04.12
11.12
18.12
25.12
01.01
08.01
15.01
2000
2001
0.030
0.035
0.040
0.045
0.050
Estimated volatility
Forecast of volatility
Estimated unconditional volatility
Figure 4.12.
Estimate of volatility for the ﬁnal days of the year 2000 and predictions of
volatility for the ﬁrst 10 days of 2001 based on a GARCH(1, 1) model (without leverage)
ﬁtted to the Microsoft return data in Example 4.24.
We can apply exponential smoothing as in (4.16) to the squared observations to get
a procedure that follows the updating scheme
PtX2
t+1 = αX2
t + (1 −α)Pt−1X2
t ,
(4.46)
for some value of α.
Since the expectations of X2
t+1 and σ 2
t+1 coincide, we could alternatively
regard (4.46) as an exponential smoothing scheme for the unobserved squared
volatility. We could deﬁne a recursive scheme for one-step-ahead volatility forecasting by
ˆσ 2
t+1 = αX2
t + (1 −α)ˆσ 2
t .
(4.47)
This is the essential idea of the EWMA approach to volatility forecasting.
If we compare (4.47) with the one-step-ahead volatility estimation scheme deﬁned
by a GARCH(1, 1) model in (4.43), it is tempting to say that EWMA corresponds to
estimatingvolatilityusingaconditional-expectation-basedtechniqueinanIGARCH
model where the parameter α0 equals zero, although this analogy should be used
with care. GARCH and IGARCH models with α0 = 0 are not well deﬁned and the
solution of the stochastic recurrence relation in (4.29) vanishes. Moreover, IGARCH
is not covariance stationary. It is better to regard EWMA as a sensible model-free
approach to volatility forecasting based on the classical technique of exponential
smoothing.
4.4.2
Conditional Risk Measurement
We now return to the conditional risk-measurement problem discussed in Chapter 2
and consider the situation where we wish to measure risk for an investment in a
--- page 177 ---

4.4. Volatility Models and Risk Estimation
161
single stock, index or currency. On day t the value of the position is Vt and the
log-return for the next day is Xt+1, so the (linearized) loss over the next day is
Lt+1 = l
[t](Xt+1) = −VtXt+1. We require risk-measure estimates, such as VaR
and ES, for the conditional distribution FLt+1|Ft , where Ft = σ({Xs : s ⩽t}). We
set Vt = 1 for all t and write Lt = −Xt, so (Lt) is the process of negative log-returns.
Remark 4.27. Although we consider a simple univariate situation, the methodology
ofthissectioncanbeappliedtoportfoliolossesinthecontextofhistoricalsimulation.
Suppose we have constructed historical-simulation data ( ˜Lt) using the approach
described in Section 2.3.2. Writing Lt+1 = l[t](Xt+1) for our loss over the next day,
where l[t] is the loss operator and Xt+1 the vector of risk-factor changes, we wish
to calculate risk-measure estimates for the conditional distribution FLt+1|Gt , where
Gt = σ({ ˜Ls : s ⩽t}). We simply apply the methodology of this section to the time
series ( ˜Lt); this strategy was used in Section 2.3.6.
To calculate conditional risk measures we make the following assumption.
Assumption 4.28. The process of losses (Lt)t∈Z is adapted to the ﬁltration (Ft)t∈Z
and follows a stationary model of the form Lt = µt + σtZt, where µt and σt are
Ft−1-measurable and the (Zt) are SWN(0, 1) innovations.
A concrete example of a model satisfying Assumption 4.28 would be an (invertible)ARMA process with GARCH errors of the kind analysed in this chapter. Under
the assumption, if we write G for the df of (Zt), we can easily calculate that
FLt+1|Ft (l) = P(µt+1 + σt+1Zt+1 ⩽l | Ft) = G((l −µt+1)/σt+1).
(4.48)
Thus calculation of risk measures for the conditional one-period loss distribution
amounts to calculating risk measures for the innovation distribution G. Using the
approach of Examples 2.14 and 2.18 we easily obtain
VaRt
α = µt+1 + σt+1qα(Z),
(4.49)
ESt
α = µt+1 + σt+1 ESα(Z),
(4.50)
where Z is a generic rv with df G. In general, to estimate the risk measures (4.49)
and(4.50),werequireestimatesofµt+1 andσt+1,theconditionalmeanandvolatility
of the loss process. We also require the quantile and expected shortfall of the innovation df G. In a model with Gaussian innovations the latter are qα(Z) = Φ−1(α)
and ESα(Z) = φ(Φ−1(α))/(1 −α). In a model with non-Gaussian innovations,
qα(Z) and ESα(Z) depend on any further parameters of the innovation distribution.
For example, we might assume (scaled) t innovations; in this case the quantile and
expected shortfall of a standard univariate t distribution (the latter given in (2.27))
would have to be scaled by the factor √(ν −2)/ν to take account of the fact that
the innovation distribution is scaled to have variance one.
Concrete estimation strategies we might adopt, in order of decreasing sophistication, include the following.
--- page 178 ---

162
4. Financial Time Series
(1) Fit an ARMA–GARCH model with an appropriate innovation distribution
to the data Lt−n+1, . . . , Lt by ML and use the prediction methodology discussed in Section 4.4.1 to estimate σt+1 and µt+1. Any further parameters of
the innovation distribution would be estimated simultaneously in the model
ﬁtting.
(2) Fit an ARMA–GARCH model by QML and use prediction methodology as
in strategy (1) to estimate σt+1 and µt+1. In a separate second step we use the
model residuals to ﬁnd an appropriate innovation distribution and estimate its
parameters.
(3) Use EWMA to estimate σt+1 and set µt+1 to zero (as it is less important).
In conjunction with an assumption of Gaussian innovations this is essentially
the RiskMetrics method. Instead of making the Gaussian assumption, we
could standardize each of the losses Lt−n+1, . . . , Lt by dividing by volatility
estimates ˆσt−n+1, . . . , ˆσt calculated using EWMA. This would yield a set of
residuals, from which the innovation distribution could be estimated as in
strategy (2).
4.4.3
Backtesting
Backtesting VaR.
Using the notation of the previous section, we ﬁrst observe that
if we deﬁne indicator variables It+1 = I{Lt+1>VaRtα}, indicating violations of the
quantiles of the conditional loss distribution, then the process (It)t∈Z is a process of iid Bernoulli variables with success (i.e. violation) probability 1 −α. This
property is certainly true under Assumption 4.28, since it follows from (4.49) that
It+1 = I{Lt+1>VaRtα} = I{Zt+1>qα(Z)} and the innovations (Zt) are themselves iid.
However, it is also more generally true, as the following lemma shows.
Lemma 4.29. Let (Yt)t∈Z be a sequence of Bernoulli indicator variables adapted
to a ﬁltration (Ft)t∈Z and satisfying E(Yt | Ft−1) = p > 0 for all t. Then (Yt) is a
process of iid Bernoulli variables.
Proof. The process (Yt −p)t∈Z has the martingale-difference property (see Deﬁnition 4.6). Moreover, var(Yt −p) = E(E((Yt −p)2 | Ft−1)) = p(1 −p) for all t.
Therefore (Yt −p) and hence (Yt) are white noise processes of uncorrelated variables. It is easily shown that identically distributed uncorrelated Bernoulli variables
are iid.
In practice, we make one-step-ahead conditional VaR estimates
VaRt
α and consider the violation indicators
ˆIt+1 := I{Lt+1>
VaRt
α}.
(4.51)
If we are successful in estimating conditional quantiles, we would expect that the
empirical violation indicators would behave like realizations of iid Bernoulli trials
with success probability (1 −α).
Checking for iid Bernoulli violations of the one-step-ahead VaR has two aspects:
checking that the number of violations is correct on average; checking that the
--- page 179 ---

4.4. Volatility Models and Risk Estimation
163
pattern of violations is consistent with iid behaviour. Certainly, if we calculate VaR
estimates for times t = 1, . . . , m, we expect that m
t=1 ˆIt ∼B(m, 1 −α), and this
is easily addressed with a standard two-sided binomial test (see, for example, Casella
and Berger 2002, pp. 493–495). Departures from the null hypothesis would suggest
either systematic underestimation or overestimation of VaR.
To check for independence of the Bernoulli indicators one possibility is to perform
a runs test of the kind described by David (1947), which involves counting runs of
successive zeros or ones in the realizations of the indicator variables and comparing
the realized number of runs with the known sampling distribution of the number of
runs in iid Bernoulli data (see also Notes and Comments).
The backtesting of conditional VaR estimates for the h-period loss distribution
is more complicated. To use the kind of ideas above we would have to base our
backtestsonnon-overlappingperiods.Forexample,ifwecalculatedtwo-weekVaRs,
we could make a comparison of the VaR estimate and the realized loss every two
weeks, which would clearly lead to a relatively small amount of violation data with
which to monitor the performance of the model. If we used overlapping periods, for
example by recording the violation indicator value every day for the loss incurred
over the previous two weeks, we would create a series of dependent Bernoulli trials
for which formal inference would be difﬁcult.
Backtesting expected shortfall.
We begin by observing that if ESt
α is the expected
shortfall of the (continuous) conditional loss distribution FLt+1|Ft and we deﬁne
St+1 = (Lt+1 −ESt
α)It+1, then for an arbitrary loss process (Lt)t∈Z the process
(St)t∈Z forms a martingale difference series satisfying E(St+1 | Ft) = 0. Moreover,
under Assumption 4.28 and using (4.49) and (4.50), we have
St+1 = σt+1(Zt+1 −ESα(Z))I{Zt+1>qα(Z)},
which takes the form of a volatility times a zero-mean iid sequence of innovation
variables ((Zt+1 −ESα(Z))I{Zt+1>qα(Z)}). This suggests that, in practice, when the
risk measures and volatility are estimated, we could form violation residuals of the
form
ˆRt+1 := ˆSt+1/ˆσt+1,
ˆSt+1 := (Lt+1 −
ESt
α) ˆIt+1,
(4.52)
where ˆIt+1 is the violation indicator deﬁned in (4.51). We expect these to behave
like realizations of iid variables from a distribution with mean zero and an atom of
probability mass of size α at zero. To test for mean-zero behaviour we could perform
a bootstrap test on the non-zero violation residuals that makes no assumption about
their distribution. See Efron and Tibshirani (1994, p. 224) for a description of such
a test.
Backtesting the predictive distribution.
As well as backtesting VaR and expected
shortfall we can also devise tests that assess the overall quality of the estimated
conditional loss distributions from which the risk-measure estimates are derived. Of
course, our primary interest focuses on the measures of tail risk, but it is still useful
to backtest our estimates of the whole predictive distribution to obtain additional
conﬁrmation of the risk-measure estimation procedure.
--- page 180 ---

164
4. Financial Time Series
Suppose we deﬁne the process (Ut)t∈Z by setting Ut+1 := FLt+1|Ft (Lt+1). Under
Assumption 4.28 it follows easily from (4.48) that Ut+1 = GZ(Zt+1), so (Ut) is
a strict white noise process. Moreover, if GZ is continuous, then the stationary
or unconditional distribution of (Ut) must be standard uniform (see, for example,
Proposition 5.2).
In actual applications we estimate FLt+1|Ft from data up to time t and we backtest our estimates by forming ˆUt+1 := ˆFLt+1|Ft (Lt+1) on day t + 1. Suppose we
estimate the predictive distribution on days t = 0, . . . , m −1 and form backtesting
data ˆU1, . . . , ˆUm; we expect these to behave like a sample of iid uniform data. The
distributional assumption can be assessed by standard goodness-of-ﬁt tests like the
chi-squared test or Kolmogorov–Smirnov test (see Section 3.3.5 for references). It
is also possible to form the data Φ−1( ˆU1), . . . , Φ−1( ˆUm), where Φ is the standard
normal df; these should behave like iid standard normal data (see again Proposition 5.2) and this can be tested as in Section 3.1.4. The strict white noise assumption
can be tested using the approach described in Section 4.2.3.
Notes and Comments
The backtesting material is mainly taken from McNeil and Frey (2000), where examples of the binomial test for violation counts and the test of expected shortfall using
exceedance residuals can be found. Use of the runs test for testing the randomness
of VaR violations is suggested by Christoffersen, Diebold and Schuermann (1998).
This test is shown to be uniformly most powerful against Markovian alternatives by
Lehmann (1986). Christoffersen, Diebold and Schuermann also suggest the use of
a further test for randomness based on the non-trivial eigenvalue of the transition
matrix in a Markov chain model for the violation indicator variables.
The idea of testing the estimate of the predictive distribution may be found in
Berkowitz (2001, 2002). See also Berkowitz and O’Brien (2002) for a more general
article on testing the accuracy of the VaR models of commercial banks.
4.5
Fundamentals of Multivariate Time Series
The presentation of the basic concepts of multivariate time series in this section
closely parallels the presentation of the corresponding ideas for univariate time
series in Section 4.2. Again the approach is similar to that of Brockwell and Davis
(1991, 2002).
4.5.1
Basic Deﬁnitions
A multivariate time series model for multiple risk factors is a stochastic process
(Xt)t∈Z, i.e. a family of random vectors, indexed by the integers and deﬁned on
some probability space (Ω, F , P).
Moments of a multivariate time series.
Assuming they exist, we deﬁne the mean
function µ(t) and the covariance matrix function Γ (t, s) of (Xt)t∈Z by
µ(t) = E(Xt),
t ∈Z,
Γ (t, s) = E((Xt −µ(t))(Xs −µ(s))′),
t, s ∈Z.
--- page 181 ---

4.5. Fundamentals of Multivariate Time Series
165
Analogously to the univariate case, we have Γ (t, t) = cov(Xt). By observing that
the elements γij(t, s) of Γ (t, s) satisfy
γij(t, s) = cov(Xt,i, Xs,j) = cov(Xs,j, Xt,i) = γji(s, t),
(4.53)
it is clear that Γ (t, s) = Γ (s, t)′ for all t, s. However, the matrix Γ need not be
symmetric, so in general Γ (t, s)̸ = Γ (s, t), which is in contrast to the univariate
case. Lagged values of one of the component series can be more strongly correlated
with future values of another component series than vice versa. This property, when
observed in empirical data, is known as a lead-lag effect and is discussed in more
detail in Example 4.36.
Stationarity.
Again the concrete multivariate models we consider will be stationary
in one or both of the following senses.
Deﬁnition 4.30 (strict stationarity). The multivariate time series (Xt)t∈Z is strictly
stationary if
(X′
t1, . . . , X′
tn) d= (X′
t1+k, . . . , X′
tn+k),
for all t1, . . . , tn, k ∈Z and for all n ∈N.
Deﬁnition 4.31 (covariance stationarity). The multivariate time series (Xt)t∈Z is
covariance stationary (or weakly or second-order stationary) if the ﬁrst two moments
exist and satisfy
µ(t) = µ,
t ∈Z,
Γ (t, s) = Γ (t + k, s + k),
t, s, k ∈Z.
Astrictlystationarymultivariatetimeserieswithﬁnitecovariancematrixiscovariance stationary, but we again note that it is possible to deﬁne inﬁnite-variance processes (including certain multivariateARCH and GARCH processes) that are strictly
stationary but not covariance stationary.
Serial and cross-correlation in stationary multivariate time series.
The deﬁnition
of covariance stationarity implies that for all s, t we have Γ (t −s, 0) = Γ (t, s), so
that the covariance between Xt and Xs only depends on their temporal separation
t −s, which is known as the lag. In contrast to the univariate case, the sign of
the lag is important. For a covariance-stationary multivariate process we write the
covariance matrix function as a function of one variable: Γ (h) := Γ (h, 0), ∀h ∈Z.
Noting that Γ (0) = cov(Xt), ∀t, we can now deﬁne the correlation matrix function
of a covariance-stationary process.
Deﬁnition 4.32 (correlation matrix function). Writing  := (Γ (0)), where
(·) is the operator deﬁned in (3.4), the correlation matrix function P(h) of a
covariance-stationary multivariate time series (Xt)t∈Z is
P(h) := −1Γ (h)−1,
∀h ∈Z.
(4.54)
--- page 182 ---

166
4. Financial Time Series
The diagonal entries ρii(h) of this matrix-valued function give the autocorrelation
function of the ith component series (Xt,i)t∈Z. The off-diagonal entries give socalled cross-correlations between different component series at different times. It
follows from (4.53) that P(h) = P(−h)′, but P(h) need not be symmetric, and in
general P(h)̸ = P(−h).
White noise processes.
As in the univariate case, multivariate white noise processes
are building blocks for more interesting classes of time series model.
Deﬁnition 4.33 (multivariate white noise). (Xt)t∈Z is multivariate white noise if
it is covariance stationary with correlation matrix function given by
P(h) =

P,
h = 0,
0,
h̸ = 0,
for some positive-deﬁnite correlation matrix P.
A multivariate white noise process with mean zero and covariance matrix
Σ = cov(Xt) will be denoted WN(0, Σ). Such a process has no cross-correlation
between component series, except for contemporaneous cross-correlation at lag
zero. A simple example is a series of iid random vectors with ﬁnite covariance
matrix, and this is known as a multivariate strict white noise.
Deﬁnition 4.34 (multivariate strict white noise). (Xt)t∈Z is multivariate strict
white noise if it is a series of iid random vectors with ﬁnite covariance matrix.
A strict white noise process with mean zero and covariance matrix Σ will be
denoted SWN(0, Σ).
The martingale-difference noise concept may also be extended to higher dimensions.As before we assume that the time series (Xt)t∈Z is adapted to some ﬁltration
(Ft), typically the natural ﬁltration (σ({Xs : s ⩽t})), which represents the information available at time t.
Deﬁnition 4.35 (multivariate martingale difference). (Xt)t∈Z has the multivariate martingale-difference property with respect to the ﬁltration (Ft) if E|Xt| <
∞and
E(Xt | Ft−1) = 0,
∀t ∈Z.
The unconditional mean of such a process is obviously also zero and, if cov(Xt) <
∞for all t, the covariance matrix function satisﬁes Γ (t, s) = 0 for t̸ = s. If the
covariance matrix is also constant for all t, then a process with the multivariate
martingale-difference property is also a multivariate white noise process.
4.5.2
Analysis in the Time Domain
We now assume that we have a random sample X1, . . . , Xn from a covariancestationary multivariate time series model (Xt)t∈Z. In the time domain we construct
empirical estimators of the covariance matrix function and the correlation matrix
function from this random sample.
--- page 183 ---

4.5. Fundamentals of Multivariate Time Series
167
The sample covariance matrix function is calculated according to
ˆΓ (h) = 1
n
n−h

t=1
(Xt+h −¯X)(Xt −¯X)′,
0 ⩽h < n,
where ¯X = n
t=1 Xt/n is the sample mean, which estimates µ, the mean of the
time series. Writing ˆ := ( ˆΓ (0)), where (·) is the operator deﬁned in (3.4), the
sample correlation matrix function is
ˆP(h) = ˆ−1 ˆΓ (h) ˆ−1,
0 ⩽h < n.
The information contained in the elements ˆρij(h) of the sample correlation matrix
function is generally displayed in the cross-correlogram, which is a d × d matrix
of plots (see Figure 4.13 for an example). The ith diagonal plot in this graphic
display is the correlogram of the ith component series, given by {(h, ˆρii(h)) : h =
0, 1, 2, . . . }. For the off-diagonal plots containing the estimates of cross-correlation
there are various possible presentations and we will consider the following convention: for i < j we plot {(h, ˆρij(h)) : h = 0, 1, 2, . . . }; for i > j we plot
{(−h, ˆρij(h)) : h = 0, 1, 2, . . . }. An interpretation of the meaning of the offdiagonal pictures is given in Example 4.36.
It can be shown that for causal processes driven by multivariate strict white noise
innovations (see Section 4.5.3) the estimates that comprise the components of the
sample correlation matrix function ˆP(h) are consistent estimates of the underlying
theoretical quantities. For example, if the data themselves are from an SWN, then
the cross-correlation estimators ˆρij(h) for h̸ = 0 converge to zero as the sample
size is increased. However, results concerning the asymptotic distribution of crosscorrelation estimates are, in general, more complicated than the univariate result for
autocorrelation estimates given in Theorem 4.13. Some relevant theory is found in
Chapter 11 of Brockwell and Davis (1991) and Chapter 7 of Brockwell and Davis
(2002). It is standard to plot the off-diagonal pictures with Gaussian conﬁdence
bands at (−1.96√n, 1.96√n), but these bands should be used as rough guidance
for the eye and not relied upon too heavily to draw conclusions.
Example 4.36 (cross-correlogram of trivariate index returns). In Figure 4.13
the cross-correlogram of daily log-returns is shown for the Dow Jones, Nikkei and
Swiss Market indices for 26 July 1996 to 25 July 2001. Although every vector
observation in this trivariate time series relates to the same trading day, the returns
are of course not properly synchronized due to time zones; nonetheless, this picture
shows interpretable lead-lag effects which help us to understand the off-diagonal
pictures in the cross-correlogram.
Part (b) of the ﬁgure shows estimated correlations between the Dow Jones index
return on day t + h and the Nikkei index return on day t, for h ⩾0; clearly these estimates are small and lie mainly within the conﬁdence band, with the obvious exception of the correlation estimate for returns on the same trading day ˆP12(0) ≈0.14.
Part (d) shows estimated correlations between the Dow Jones index return on day
t + h and the Nikkei index return on day t, for h ⩽0; the estimate corresponding to
--- page 184 ---

168
4. Financial Time Series
 DJInd
ACF
0
10
15
20
25
0
0.2
0.4
0.6
0.8
1.0
 DJInd and Nikkei
−0.05
0
0.05
0.10
0.15
 DJInd and SMI
0
0.1
0.2
0.3
0.4
 Nikkei and DJInd
ACF
25
20
15
10
5
0
0
0.1
0.2
 Nikkei
0
0.2
0.4
0.6
0.8
1.0
 Nikkei and SMI
0
0.1
0.2
0.3
 SMI and DJInd
Lag
ACF
0
0.1
0.2
0.3
0.4
 SMI and Nikkei
Lag
−0.1
0
0.1
0.2
0.3
 SMI
Lag
0
0.2
0.4
0.6
0.8
1.0
5
(e)
(f)
(g)
(h)
(a)
(b)
(c)
(d)
(i)
0
10
15
20
25
5
0
10
15
20
25
5
0
10
15
20
25
5
0
10
15
20
25
5
0
10
15
20
25
5
25
20
15
10
5
0
25
20
15
10
5
0
Figure 4.13.
Cross-correlogram of daily log-returns of Dow Jones, Nikkei and Swiss
Market indices for 26 July 1996 to 25 July 2001 (see Example 4.36 for commentary).
h = −1 is approximately 0.28 and can be interpreted as showing how the American
market leads the Japanese market. Comparing parts (c) and (g) we see, unsurprisingly, that the American market also leads the Swiss market, so that returns on day
t −1 in the former are quite strongly correlated with returns on day t in the latter.
4.5.3
Multivariate ARMA Processes
We provide a brief excursion into multivariate ARMA models to indicate how
the ideas of Section 4.2.2 generalize to higher dimensions. For daily data, capturing multivariate ARMA effects is much less important than capturing multivariate
volatility effects (and dynamic correlation effects) through multivariate GARCH
modelling, but, for longer-period returns, the more traditional ARMA processes
become increasingly useful. In the econometrics literature they are more commonly
known as vector ARMA (or VARMA) processes.
Deﬁnition 4.37 (VARMA process). Let (εt)t∈Z be WN(0, Σε). The process
(Xt)t∈Z is a zero-mean VARMA(p, q) process if it is a covariance-stationary process satisfying difference equations of the form
Xt −Φ1Xt−1 −· · · −ΦpXt−p = εt + Θ1εt−1 + · · · + Θqεt−q,
∀t ∈Z
for parameter matrices Φi and Θj in Rd×d. (Xt) is a VARMA process with mean
µ if the centred series (Xt −µ)t∈Z is a zero-mean VARMA(p, q) process.
--- page 185 ---

4.5. Fundamentals of Multivariate Time Series
169
For practical applications we again consider only causal VARMA processes,
which are processes where the solution of the deﬁning equations has a representation
of the form
Xt =
∞

i=0
Ψiεt−i,
(4.55)
where (Ψi)i∈N0 is a sequence of matrices in Rd×d with absolutely summable components, meaning that, for any j and k,
∞

i=0
|ψi,jk| < ∞.
(4.56)
As in the univariate case (see Proposition 4.9), it can be veriﬁed by direct calculation
that such linear processes are covariance stationary. Obviously, for all t, we have
E(Xt) = µ. For h ⩾0 the covariance matrix function is given by
Γ (t + h, t) = cov(Xt + h, Xt) = E
 ∞

i=0
Ψiεt+h−i
∞

j=0
ε′
t−jΨ ′
j

.
Arguing much as in the univariate case it is easily shown that this depends only on
h and not on t and that it is given by
Γ (h) =
∞

i=0
Ψi+hΣεΨ ′
i ,
h = 0, 1, 2, . . . .
(4.57)
The correlation matrix function is easily derived from (4.57) and (4.54).
The requirement that a VARMA process be causal imposes conditions on the
values that the parameter matrices Φi (in particular) and Θj may take. The theory
is remarkably similar to univariate ARMA theory. We will give a single useful
example from the VARMA class; this is the ﬁrst-order vector autoregressive (or
VAR(1)) model.
Example 4.38 (VAR(1) process). The ﬁrst-order VAR process satisﬁes the set of
vector difference equations
Xt = ΦXt−1 + εt,
∀t.
(4.58)
It is possible to ﬁnd a causal process satisfying (4.55) and (4.56) that is a solution
of (4.58) if and only if all eigenvalues of the matrix Φ are less than one in absolute
value. The causal process
Xt =
∞

i=0
Φiεt−i
(4.59)
is then the unique solution. This solution can be thought of as an inﬁnite-order vector moving-average process, a so-called VMA(∞) process. The covariance matrix
function of this process follows from (4.55) and (4.57) and is
Γ (h) =
∞

i=0
Φi+hΣεΦi′ = ΦhΓ (0),
h = 0, 1, 2, . . . .
--- page 186 ---

170
4. Financial Time Series
In practice, full VARMA models are less common than models from the VAR
and VMA subfamilies, one reason being that identiﬁability problems arise when
estimating parameters. For example, we can have situations where the ﬁrst-order
VARMA(1, 1)modelXt−ΦXt−1 = εt+Θεt−1 canberewrittenasXt−Φ∗Xt−1 =
εt+Θ∗εt−1 for completely different parameter matrices Φ∗and Θ∗(seeTsay (2002,
p. 323) for an example). Of the two subfamilies, VAR models are easier to estimate.
Fitting options for VAR models range from multivariate least-squares estimation
without strong assumptions concerning the distribution of the driving white noise,
to full maximum likelihood estimation; models combining VAR and multivariate
GARCH features can be estimated using a conditional ML approach in a very similar
manner to that described for univariate models in Section 4.3.4.
Notes and Comments
Many standard texts on time series also handle the multivariate theory (see, for
example, Brockwell and Davis (1991, 2002) or Hamilton (1994)). A key reference
aimed at an econometrics audience is L¨utkepohl (1993). For examples, in the area
of ﬁnance see Tsay (2002) and Zivot and Wang (2003).
4.6
Multivariate GARCH Processes
4.6.1
General Structure of Models
Deﬁnition 4.39. Let (Zt)t∈Z be SWN(0, Id). The process (Xt)t∈Z is said to be a
multivariate GARCH process if it is strictly stationary and satisﬁes equations of the
form
Xt = Σ1/2
t
Zt,
t ∈Z,
(4.60)
where Σ1/2
t
∈Rd×d is the Cholesky factor of a positive-deﬁnite matrix Σt which is
measurable with respect to Ft−1 = σ({Xs : s ⩽t −1}), the history of the process
up to time t −1.
Conditional moments.
It is easily calculated that a covariance-stationary process
of this type has the multivariate martingale-difference property
E(Xt | Ft−1) = E(Σ1/2
t
Zt | Ft−1) = Σ1/2
t
E(Zt) = 0,
and must therefore be a multivariate white noise process, as argued in Section 4.5.
Moreover, Σt will be the conditional covariance matrix since
cov(Xt | Ft−1) = E(XtX′
t | Ft−1) = Σ1/2
t
E(ZtZ′
t)(Σ1/2
t
)′ = Σ1/2
t
(Σ1/2
t
)′ = Σt.
(4.61)
The conditional covariance matrix Σt in a multivariate GARCH model corresponds
to the squared volatility σ 2
t in a univariate GARCH model. The use of the Cholesky
factor of Σt to describe the relationship to the driving noise in (4.60) is not important,
and in fact any type of “square root” of Σt could be used (such as the root derived
from a symmetric decomposition). (The only implication is the way we construct
residuals when ﬁtting the model in practice.) We denote the elements of Σt by σt,ij
--- page 187 ---

4.6. Multivariate GARCH Processes
171
and also use the notation σt,i = √σt,ii to denote the conditional standard deviation
(or volatility) of the ith component series (Xt,i)t∈Z.
We recall that we can write Σt = tPtt, where
t = (Σt) = diag(σt,1, . . . , σt,d),
Pt = ℘(Σt),
(4.62)
using the operator notation deﬁned in (3.5). The diagonal matrix t will be known
as the volatility matrix and Pt is known as the conditional correlation matrix. The
art of building multivariate GARCH models is to specify the dependence of Σt (or
of t and Pt) on the past in such a way that Σt always remains symmetric and
positive deﬁnite. A covariance matrix must of course be symmetric and positive
semideﬁnite, and in practice we restrict our attention to the positive-deﬁnite case
(which facilitates ﬁtting, since the conditional distribution of Xt | Ft−1 never has a
singular covariance matrix).
Unconditional moments.
The unconditional covariance matrix Σ of a process of
this type is given by
Σ = cov(Xt) = E(cov(Xt | Ft−1)) + cov(E(Xt | Ft−1)) = E(Σt),
from which it can be calculated that the unconditional correlation matrix P has
elements
ρij =
E(σt,ij)

E(σt,ii)E(σt,jj) = E(ρt,ijσt,iσt,j)

E(σ 2
t,i)E(σ 2
t,j)
,
(4.63)
which is in general difﬁcult to evaluate and is usually not simply the expectation of
the conditional correlation matrix.
Innovations.
In practical work the innovations are generally taken to be from
either a multivariate Gaussian distribution (Zt ∼Nd(0, Id)) or, more realistically for daily returns, an appropriately scaled spherical multivariate t distribution
(Zt ∼td(ν, 0, (ν −2)Id/ν)). Any distribution with mean zero and covariance
matrix Id is permissible, and appropriate members of the normal mixture family
of Section 3.2 or the spherical family of Section 3.3.1 may be considered.
Presentation of models.
In the following sections we present some of the more
important multivariate GARCH speciﬁcations. In doing this we concentrate on the
following aspects of the models.
• The form of the dynamic equations, with economic arguments and criticisms
where appropriate.
• The conditions required to guarantee that the conditional covariance matrix
Σt remains positive deﬁnite. Other mathematical properties of these models, such as conditions for covariance stationarity, are difﬁcult to derive with
full mathematical rigour; references in Notes and Comments contain further
information.
--- page 188 ---

172
4. Financial Time Series
• The parsimoniousness of the parametrization. A major problem with most
multivariate GARCH speciﬁcations is that the number of parameters tends to
explode with the dimension of the model, making them unsuitable for analyses
of many risk factors.
• Simple intuitive ﬁtting methods where available.All models can be ﬁtted by a
general global-maximization approach described in Section 4.6.4 but certain
models lend themselves to estimation in stages, particularly the models of
Section 4.6.2.
4.6.2
Models for Conditional Correlation
In this section we present models which focus on specifying the conditional correlation matrix Pt while allowing volatilities to be described by univariate GARCH
models; we begin with a popular and relatively parsimonious model where Pt is
assumed to be constant for all t.
Constant conditional correlation (CCC).
Deﬁnition 4.40. The process (Xt)t∈Z is a CCC-GARCH process if it is a process with the general structure given in Deﬁnition 4.39 such that the conditional
covariance matrix is of the form Σt = tPct, where
(i) Pc is a constant, positive-deﬁnite correlation matrix; and
(ii) t is a diagonal volatility matrix with elements σt,k satisfying
σ 2
t,k = αk0 +
pk

i=1
αkiX2
t−i,k +
qk

j=1
βkjσ 2
t−j,k,
k = 1, . . . , d,
(4.64)
where αk0 > 0, αki ⩾0, i = 1, . . . , pk, βkj ⩾0, j = 1, . . . , qk.
The CCC-GARCH speciﬁcation represents a simple way of combining univariate
GARCH processes. This can be seen by observing that in a CCC-GARCH model
observations and innovations are connected by equations Xt = tP1/2
c
Zt, which
may be rewritten as Xt = t ˜Zt for an SWN(0, Pc) process ( ˜Zt)t∈Z. Clearly, the
component processes are univariate GARCH.
Proposition 4.41. The CCC-GARCH model is well deﬁned in the sense that Σt is
almost surely positive deﬁnite for all t. Moreover, it is covariance stationary if and
only if pk
i=1 αki + qk
j=1 βkj < 1 for k = 1, . . . , d.
Proof. For a vector v̸ = 0 in Rd we have
v′Σtv = (tv)′Pc(tv) > 0,
since Pc is positive deﬁnite and the strict positivity of the individual volatility processes ensures that tv̸ = 0 for all t.
If (Xt)t∈Z is covariance stationary, then each component series (Xt,k)t∈Z is a
covariance-stationary GARCH process for which a necessary and sufﬁcient condition is pk
i=1 αki + qk
j=1 βkj < 1 by Proposition 4.21. Conversely, if the component
--- page 189 ---

4.6. Multivariate GARCH Processes
173
series are covariance stationary, then for all i and j the Cauchy–Schwarz inequality
implies
σij = E(σt,ij) = ρijE(σt,iσt,j) ⩽ρij

E(σ 2
t,i)

E(σ 2
t,j) < ∞.
Since(Xt)t∈Z isamultivariatemartingaledifferencewithﬁnite,non-time-dependent
second moments σij, it is a covariance-stationary white noise.
The CCC model is often a useful starting point from which to proceed to more
complex models. In some empirical settings it gives an adequate performance, but
it is generally considered that the constancy of conditional correlation in this model
is an unrealistic feature and that the impact of news on ﬁnancial markets requires
modelsthatallowadynamicevolutionofconditionalcorrelationaswellasadynamic
evolution of volatilities. A further criticism of the model (which applies in fact to
the majority of MGARCH speciﬁcations) is the fact that the individual volatility
dynamics (4.64) do not allow for the possibility that large returns in one component
series at a particular point in time can contribute to increased volatility of another
component time series at future points in time.
To describe a simple method of ﬁtting the CCC model we introduce the notion of
a devolatized process. For any multivariate time series process Xt, the devolatized
process is the process Yt = −1
t
Xt, where t is, as usual, the diagonal matrix of
volatilities. In the case of a CCC model it is easily seen that the devolatized process
(Yt)t∈Z is an SWN(0, Pc) process.
This structure suggests a simple two-stage ﬁtting method in which we ﬁrst estimate the individual volatility processes for the component series by ﬁtting univariate
GARCH processes; note that, although we have speciﬁed in Deﬁnition 4.40 that the
individual volatilities should follow standard GARCH models, we could of course
extend the model to allow any of the univariate models in Section 4.3.3, such as
GARCH with leverage or threshold GARCH. In a second stage we construct an
estimate of the devolatized process by taking ˆYt = ˆ−1
t
Xt, where ˆ−1
t
is the estimate of t; in other words, we collect the standardized residuals from the univariate
GARCH models. If the CCC-GARCH model is adequate, then the ˆYt data should
behave like a realization from an SWN(0, Pc) process and this can be investigated
with the correlogram and cross-correlogram applied to raw and absolute values.
Assuming the adequacy of the model, the conditional correlation matrix Pc can then
be estimated from the standardized residuals using methods from Chapter 3.
A special case of CCC-GARCH which we call a pure diagonal model occurs when
Pc = Id. A covariance-stationary model of this kind is a multivariate white noise
where the contemporaneous components Xt,i and Xt,j are also uncorrelated for
i̸ = j. Whether they are independent or not depends on further assumptions about
the driving SWN(0, Id) process: if the innovations have independent components, as
would be the case if they were multivariate Gaussian, then the component series are
independent; however, if, for example, Zt ∼td(ν, 0, ((ν −2)/ν)Id), the component
processes are dependent.
--- page 190 ---

174
4. Financial Time Series
Dynamic conditional correlation (DCC).
This model generalizes the CCC model
to allow conditional correlations to evolve dynamically according to a relatively
parsimonious scheme, but is constructed in a way that still allows estimation in
stages using univariate GARCH models. Its formal analysis as a stochastic process
is difﬁcult due to the use of the correlation matrix extraction operator ℘in its
deﬁnition.
Deﬁnition 4.42. The process (Xt)t∈Z is a DCC-GARCH process if it is a process
with the general structure given in Deﬁnition 4.39, where the volatilities comprising t follow univariate GARCH speciﬁcations as in (4.64) and the conditional
correlation matrices Pt satisfy, for t ∈Z, the equations
Pt = ℘

1 −
p

i=1
αi −
q

j=1
βj

Pc +
p

i=1
αiYt−iY ′
t−i +
q

j=1
βjPt−j

,
(4.65)
where Pc is a positive-deﬁnite correlation matrix, ℘is the operator in (3.5), Yt =
−1
t
Xt denotes the devolatized process, and the coefﬁcients satisfy αi ⩾0, βj ⩾0
and p
i=1 αi −q
j=1 βj < 1.
Observe ﬁrst that if all the αi and βj coefﬁcients in (4.65) are zero, then the model
reduces to the CCC model. If one makes an analogy with a covariance-stationary
univariate GARCH model with unconditional variance σ 2, for which the volatility
equation can be written
σ 2
t =

1 −
p

i=1
αi −
q

j=1
βj

σ 2 +
p

i=1
αiXt−i +
q

j=1
βjσ 2
t−j,
then the correlation matrix Pc in (4.65) can be thought of as representing the longrun correlation structure. Although this matrix could be estimated by ﬁtting the
DCC model to data by ML estimation in one step, it is quite common to estimate it
using an empirical correlation matrix calculated from the devolatized data, as in the
estimation of the CCC model.
Observe also that the dynamic equation (4.65) preserves the positive deﬁniteness
of Pt. If we deﬁne
Qt :=

1 −
p

i=1
αi −
q

j=1
βj

Pc +
p

i=1
αiYt−iY ′
t−i +
q

j=1
βjPt−j,
and assume that Pt−q, . . . , Pt−1 are positive deﬁnite, then it follows that, for a vector
v̸ = 0 in Rd, we have
v′Qtv =

1 −
p

i=1
αi −
q

j=1
βj

v′Pcv +
p

i=1
αiv′Yt−iY ′
t−iv +
q

j=1
βjv′Pt−jv > 0,
since the ﬁrst term is strictly positive and the second and third terms are non-negative.
If Qt is positive deﬁnite, then so is Pt.
--- page 191 ---

4.6. Multivariate GARCH Processes
175
The usual estimation method for the DCC model is as follows.
(1) Fit univariate GARCH-type models to the component series to estimate the
volatility matrix t. Form an estimated realization of the devolatized process
by taking ˆYt = ˆtXt.
(2) Estimate Pc by taking the sample correlation matrix of the devolatized data
(or better still some robust estimator of correlation).
(3) Estimate the remaining parameters αi and βj in equation (4.65) by ﬁtting
a model with structure Yt = P1/2
t
Zt to the devolatized data. We leave this
step vague for the time being and note that this will be a simple application of the methodology for ﬁtting general multivariate GARCH models in
Section 4.6.4; in a ﬁrst-order model (p = q = 1), there will only be two
remaining parameters to estimate.
4.6.3
Models for Conditional Covariance
The models of this section specify explicitly a dynamic structure for the conditional
covariance matrix Σt. These models are not designed for multiple-stage estimation
based on univariate GARCH estimation procedures.
Vector GARCH Models (VEC and DVEC).
The most general vector GARCH
model—the VEC model—has too many parameters for practical purposes and our
task will be to simplify the model by imposing various restrictions on parameter
matrices.
Deﬁnition 4.43 (VEC model). The process (Xt)t∈Z is a VEC process if it has
the general structure given in Deﬁnition 4.39, and the dynamics of the conditional
covariance matrix Σt are given by the equations
vech(Σt) = a0 +
p

i=1
¯Ai vech(Xt−iX′
t−i) +
q

j=1
¯Bj vech(Σt−j),
(4.66)
for a vector a0 ∈Rd(d+1)/2 and matrices ¯Ai and ¯Bj in R(d(d+1)/2)×(d(d+1)/2).
In this deﬁnition “vech” denotes the vector half operator, which stacks the
columns of the lower triangle of a symmetric matrix in a single column vector
of length d(d + 1)/2. Thus (4.66) should be understood as specifying the dynamics for the lower-triangular portion of the conditional covariance matrix, and the
remaining elements of the matrix are determined by symmetry.
In this very general form the model has (1 + (p + q)d(d + 1)/2)d(d + 1)/2
parameters; this number grows rapidly with dimension so that even a trivariate model
has 78 parameters. The most common simpliﬁcation has been to restrict attention to
cases when ¯Ai and ¯Bj are diagonal matrices, which gives us the diagonal VEC or
DVEC model. This special case can be written very elegantly in terms of a different
kind of matrix product, namely the Hadamard product, denoted “◦”, which signiﬁes
element-by-element multiplication of two matrices of the same size. We obtain the
