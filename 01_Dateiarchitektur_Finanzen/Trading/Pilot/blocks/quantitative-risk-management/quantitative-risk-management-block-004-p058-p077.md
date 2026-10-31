# Quantitative Risk Management_ Concepts, Techniques, and -- Alexander J_ McNeil, Rüdiger Frey, Paul Embrechts -- Princeton series in finance, -- isbn13 9780691122557 -- 478a0059673fecd0c76229cd3d8884e7 -- Anna’s Arc.pdf — pages 58–77

--- page 58 ---

42
2. Basic Concepts in Risk Management
on such elusive factors as market mood or the distribution of economic information
among investors. Moreover, in illiquid markets traders are forced to close their
position gradually over time to minimize the price impact of their transactions.
Obviously, this liquidation has to be done on a different timescale depending on the
size of the position to be liquidated relative to the market. This in turn would lead to
different time horizons  for different positions, rendering the aggregation of risk
measures across portfolios impossible. In many practical situations the risk manager
can therefore do no better than ignore the effect of market liquidity in computing
VaR numbers or related risk measures and be aware of the ensuing problems in
interpreting the results. See Notes and Comments for pointers to further theoretical
and empirical studies of these issues.
Choice of VaR parameters.
Whenever we work with risk measures based on the
loss distribution we have to choose an appropriate horizon ; in the case of VaR we
also have to decide on the conﬁdence level α. There is of course no single optimal
value for these parameters, but there are some considerations which might inﬂuence
our choice.
The risk-management horizon  should reﬂect the time period over which a
ﬁnancial institution is committed to hold its portfolio. This period is affected by
contractual and legal constraints, and by liquidity considerations. It will typically
vary across markets; in choosing a horizon for enterprise-wide risk management, a
ﬁnancial institution or corporation has little choice but to use the horizon appropriate for the market in which its core business activities lie. For instance, insurance
companies are typically bound to hold their portfolio of claims for one year, say; in
this time they can neither alter the portfolio by a substantial amount nor renegotiate
the premiums they receive. Hence, in ﬁrm-wide risk management, one year is also
the appropriate horizon for measuring the market risk of the investment portfolios
of such companies.
As mentioned earlier, even in the absence of contractual constraints, a ﬁnancial
institution can be forced to hold a loss-making position in a risky asset if the market
for that asset is not very liquid. For such positions a relatively long horizon may be
appropriate. Again, liquidity does vary across markets, and for overall risk management an institution has to choose a horizon which best reﬂects its main exposures.
There are other, more practical considerations which suggest that  should be
relatively small: the use of the linearized loss operator, which simpliﬁes many computations, is justiﬁed only if the risk-factor changes are relatively small, which is
more likely for small . Similarly, the assumption that the composition of the portfolio remains unchanged is tenable only for a small holding period. Moreover, the
calibration and testing of statistical models for the risk-factor changes (Xt)t∈N are
easier if  is small, since this typically means that we have more data at our disposal.
Concerning the choice of the conﬁdence level α it is again difﬁcult to give a
clear-cut recommendation, since different values of α are appropriate for different purposes. Fortunately, once we have an estimate for the loss distribution, it is
easy to compute quantiles at different conﬁdence levels simultaneously. For capitaladequacy purposes a high conﬁdence level is certainly called for in order to have a
--- page 59 ---

2.2. Risk Measurement
43
sufﬁcient safety margin. For instance, the Basel Committee proposes the use of VaR
at the 99% level and  equal to 10 days for market risk. In order to set limits for
traders, a bank would typically take 95% and  equal to one day. The backtesting
of models producing VaR ﬁgures should also be carried out at lower conﬁdence
levels in order to have more observations where the realized loss is higher than the
predicted VaR.
TransformingVaR into regulatory capital.
For banks using the internal model (IM)
approach for market risk (MR), the following risk-capital formula results:
RCt
IM(MR) = max

VaRt,10
0.99, k
60
60

i=1
VaRt−i+1,10
0.99

+ CSR,
(2.21)
where VaRj,10
0.99 stands for a 10-day VaR at the 99% conﬁdence level, calculated
on day j, and t represents today. The stress factor 3 ⩽k ⩽4 is determined as
a function of the overall quality of the bank’s internal model. The component CSR
stands for speciﬁc risk, i.e. the risk that is due to issuer-speciﬁc price movements after
accounting for general market factors. A speciﬁc risk component should be added
to all VaR numbers (see, for example, Crouhy, Galai and Mark 2001, Section 2.2).
A comment on VaR terminology.
In practice the term “VaR” is used in various
ways. In its most narrow sense the term Value-at-Risk refers to a quantile of the
loss distribution as deﬁned in Deﬁnition 2.10. Often risk managers refer to “VaR
procedures” such as “delta-normalVaR” (see Section 2.3.1 below).AVaR procedure
refers to a statistical approach to estimating a model for the loss distribution. Clearly,
aVaR procedure could also be used to estimate some other risk measure based on the
loss distribution. Finally, the term “VaR approach to risk management” is frequently
used and usually refers to the way VaR ﬁgures are used in steering a company. In
this book we use the term VaR only in the ﬁrst sense.
2.2.4
Other Risk Measures Based on Loss Distributions
The purpose of this section is to discuss a few other statistical summaries of the
loss distribution which are frequently used as risk measures in ﬁnance, insurance
and risk management. As in the previous two sections we assume that a certain loss
distribution FL has been ﬁxed at the outset of the analysis.
Variance.
Historically the variance of the P&L distribution has been the dominating risk measure in ﬁnance. To a large extent this is due to the huge impact that the
portfolio theory of Markowitz, which uses variance as a measure of risk, has had
on theory and practice in ﬁnance (see, for example, Markowitz 1952). Variance is a
well-understood concept which is easy to use analytically. However, as a risk measure it has two drawbacks. On the technical side, if we want to work with variance,
we have to assume that the second moment of the loss distribution exists. While
unproblematic for most return distributions in ﬁnance this can cause problems in
certain areas of non-life insurance or for the analysis of operational losses (see Section 10.1.4). On the conceptual side, since it makes no distinction between positive
--- page 60 ---

44
2. Basic Concepts in Risk Management
and negative deviations from the mean, variance is a good measure of risk only for
distributions which are (approximately) symmetric around the mean, such as the
normal distribution or a (ﬁnite-variance) Student t distribution. However, in many
areas of risk management, such as in credit and operational risk management, we
deal with loss distributions which are highly skewed.
Lower and upper partial moments.
Partial moments are measures of risk based on
the lower or upper part of a distribution. In most of the literature on risk management
the main concern is with the risk inherent in the lower tail of a P&L distribution and
lower partial moments are used to measure this risk. Under our sign convention we
are concerned with the risk inherent in the upper tail of a loss distribution and we
focus on upper partial moments. Given an exponent k ⩾0 and a reference point q
the upper partial moment UPM(k, q) is deﬁned as
UPM(k, q) =
 ∞
q
(l −q)k dFL(l) ∈[0, ∞].
(2.22)
Some combinations of k and q have a special interpretation: for k = 0 we obtain
P(L ⩾q); for k = 1 we obtain E((L −q)I{L⩾q}); for k = 2 and q = E(L) we
obtain the upper semivariance of L. Of course, the higher the value we choose for
k, the more conservative our risk measure becomes since we give more and more
weight to large deviations from the reference point q.
Expected shortfall.
Expected shortfall is closely related toVaR. It is now preferred
toVaR by many risk managers in practice and will be seen in Section 6.1 to overcome
the conceptual deﬁciencies of the latter (related to subadditivity).
Deﬁnition 2.15 (expected shortfall). For a loss L with E(|L|) < ∞and df FL the
expected shortfall at conﬁdence level α ∈(0, 1) is deﬁned as
ESα =
1
1 −α
 1
α
qu(FL) du,
(2.23)
where qu(FL) = F ←
L (u) is the quantile function of FL.
Expected shortfall is thus related to VaR by
ESα =
1
1 −α
 1
α
VaRu(L) du.
Instead of ﬁxing a particular conﬁdence level α we average VaR over all levels
u ⩾α and thus “look further into the tail” of the loss distribution. Obviously ESα
depends only on the distribution of L and obviously ESα ⩾VaRα. See Figure 2.1
for a simple illustration of an expected shortfall value and its relationship to VaR.
The 95% expected shortfall value of 4.9 is at least double the 95% VaR value of 2.2
in this case.
For continuous loss distributions an even more intuitive expression can be derived
which shows that expected shortfall can be interpreted as the expected loss that is
incurred in the event that VaR is exceeded.
--- page 61 ---

2.2. Risk Measurement
45
Lemma 2.16. For an integrable loss L with continuous df FL and any α ∈(0, 1)
we have
ESα = E(L; L ⩾qα(L))
1 −α
= E(L | L ⩾VaRα),
(2.24)
where we have used the notation E(X; A) := E(XIA) for a generic integrable rv
X and a generic set A ∈F .
Proof. Denote by U an rv with uniform distribution on the interval [0, 1]. It is
a well-known fact from elementary probability theory that the rv F ←
L (U) has df
FL (see Proposition 5.2 for a proof). We have to show that E(L; L ⩾qα(L)) =
 1
α F ←
L (u) du. Now
E(L; L ⩾qα(L)) = E(F ←
L (U); F ←
L (U) ⩾F ←
L (α)) = E(F ←
L (U); U ⩾α);
in the last equality we used the fact that F ←
L is strictly increasing since FL is continuous (see Proposition A.3(iii)). Thus we get E(F ←
L (U); U ⩾α) =
 1
α F ←
L (u) du.
The second representation follows since for a continuous loss distribution FL we
have P(L ⩾qα(L)) = 1 −α.
Remark 2.17. For a discontinuous loss df FL, formula (2.24) does not hold for
all α; instead we have the more complicated expression
ESα =
1
1 −α (E(L; L ⩾qα) + qα(1 −α −P(L ⩾qα))).
(2.25)
For a proof see Proposition 3.2 of Acerbi and Tasche (2002).
We use Lemma 2.16 to calculate the expected shortfall for two common continuous distributions.
Example 2.18 (expected shortfall for Gaussian loss distribution). Suppose that
the loss distribution FL is normal with mean µ and variance σ 2. Fix α ∈(0, 1).
Then
ESα = µ + σ φ(Φ−1(α))
1 −α
,
(2.26)
where φ is the density of the standard normal distribution. The proof is elementary.
First note that
ESα = µ + σE
L −µ
σ

L −µ
σ
⩾qα
L −µ
σ

;
hence it sufﬁces to compute the expected shortfall for the standard normal rv
˜L := (L −µ)/σ. Here we get
ESα( ˜L) =
1
1 −α
 ∞
Φ−1(α)
lφ(l) dl =
1
1 −α [−φ(l)]∞
Φ−1(α) = φ(Φ−1(α))
1 −α
.
Example 2.19 (expected shortfall for Student t loss distribution). Suppose the
loss L is such that ˜L = (L −µ)/σ has a standard t distribution with ν degrees of
freedom, as in Example 2.14. Suppose further that ν > 1. By the reasoning of Example 2.18, which applies to any location-scale family, we have ESα = µ + σ ESα( ˜L).
--- page 62 ---

46
2. Basic Concepts in Risk Management
The expected shortfall of the standard t distribution is easily calculated by direct
integration to be
ESα( ˜L) = gν(t−1
ν (α))
1 −α
ν + (t−1
ν (α))2
ν −1

,
(2.27)
where tν denotes the df and gν the density of standard t.
The following lemma gives a kind of law of large numbers for expected shortfall
in terms of order statistics.
Lemma 2.20. For a sequence (Li)i∈N of iid rvs with df FL we have
lim
n→∞
[n(1−α)]
i=1
Li,n
[n(1 −α)]
= ESα
a.s.,
(2.28)
where L1,n ⩾· · · ⩾Ln,n are the order statistics of L1, . . . , Ln and where [n(1−α)]
denotes the largest integer not exceeding n(1 −α).
In other words, expected shortfall at conﬁdence level α can be thought of as
the limiting average of the [n(1 −α)] upper order statistics from a sample of size n
from the loss distribution. This representation suggests an obvious way of estimating
expected shortfall in the situation when we have large samples and [n(1 −α)] is a
relatively large number. This is generally not the case in practice, except perhaps
when the Monte Carlo approach to risk estimation is used (see Section 2.3.3). A
proof of Lemma 2.20 may be found in Proposition 4.1 of Acerbi and Tasche (2002).
Since ESα can be thought of as an average over all losses that are greater than
or equal to VaRα, it is sensitive to the severity of losses exceeding VaRα. This
advantage of expected shortfall is illustrated in the following example.
Example 2.21 (VaR and ES for stock returns). We consider daily losses on a
position in a particular stock; the current value of the position equals Vt = 10 000.
Recall from Example 2.4 that the loss for this portfolio is given by L
t+1 = −VtXt+1,
where Xt+1 represents daily log-returns of the stock. We assume that Xt+1 has mean
zero and standard deviation σ = 0.2/
√
250, i.e. we assume that the stock has an
annualized volatility of 20%. We compare two different models for the distribution,
namely (i) a normal distribution and (ii) a t distribution with ν = 4 degrees of
freedom scaled to have standard deviation σ. The t distribution is a symmetric
distribution with heavy tails, so that large absolute values are much more probable
than in the normal model; it is also a distribution that has been shown to ﬁt well in
many empirical studies (see Example 3.15). In Table 2.1 we present VaRα and ESα
for both models and various values of α. In case (i) these values have been computed
using (2.26); the expected shortfall for the t model has been computed using (2.27).
Most risk managers would argue that the t model is riskier than the normal model,
since under the t distribution large losses are more likely. However, if we use VaR at
the 95% or 97.5% conﬁdence level to measure risk, the normal distribution appears
to be at least as risky as the t model; only above a conﬁdence level of 99% does
the higher risk in the tails of the t model become apparent. On the other hand, if
--- page 63 ---

2.2. Risk Measurement
47
Table 2.1.
VaRα and ESα in normal and t model for different values of α.
α
0.90
0.95
0.975
0.99
0.995
VaRα (normal model)
162.1
208.1
247.9
294.3
325.8
VaRα (t model)
137.1
190.7
248.3
335.1
411.8
ESα (normal model)
222.0
260.9
295.7
337.2
365.8
ESα (t model)
223.4
286.3
356.7
465.8
563.5
we use expected shortfall, the risk in the tails of the t model is reﬂected in our risk
measurement for lower values of α. Of course, simply going to a 99% conﬁdence
level in quoting VaR numbers does not help to overcome this deﬁciency of VaR, as
there are other examples where the higher risk becomes apparent only for conﬁdence
levels beyond 99%.
Remark 2.22. It is possible to derive results on the asymptotics of the shortfallto-quantile ratio ESα / VaRα for α →1. For the normal distribution we have
limα→1 ESα / VaRα = 1; for the t distribution with ν > 1 degrees of freedom
we have limα→1 ESα / VaRα = ν/(ν −1) > 1. This shows that for a heavy-tailed
distribution the difference between ES and VaR is more pronounced than for the
normal distribution. We will take up this issue in more detail in Section 7.2.3.
Notes and Comments
An extensive discussion of different approaches to risk quantiﬁcation is given in
Crouhy, Galai and Mark (2001). Value-at-Risk was introduced by JPMorgan in the
ﬁrst version of its RiskMetrics system and was quickly accepted by risk managers
and regulators as industry standard. Expected shortfall was made popular byArtzner
et al. (1997, 1999). In the latter paper an important axiomatic approach to risk measures was developed; we will discuss their work in Section 6.1. There are a number
of variants on the expected shortfall risk measure with a variety of names, such as
tail conditional expectation (TCE), worst conditional expectation (WCE) and conditionalVaR (CVaR); all coincide for continuous loss distributions.Acerbi and Tasche
(2002) discuss the relationships between the various notions. Risk measures based
on loss distributions also appear in the literature under the (somewhat unfortunate)
heading of law-invariant risk measures.
A class of risk measures very much in use throughout the hedge fund industry is
basedonthepeak-to-bottomlossoveragivenperiodoftimeintheperformancecurve
of an investment. These measures are typically referred to as (maximal) drawdown
risk measures (see, for example, Chekhlov, Uryasev and Zabarankin 2005; Jaeger
2005).
The measurement of ﬁnancial risk and the computation of actuarial premiums are
at least conceptually closely related problems, so that the actuarial literature on premium principles is of relevance in ﬁnancial risk management. We refer to Chapter 3
of Rolski et al. (1999) for an overview; Goovaerts, De Vylder and Haezendonck
(1984) provide a specialist account.
--- page 64 ---

48
2. Basic Concepts in Risk Management
Model risk has become a central issue in modern risk management. The essays
collected in Gibson (2000) give a good overview of the academic research on this
issue.The problems faced by the hedge fund LTCM in 1998 provide a prime example
ofmodelriskinVaR-basedrisk-managementsystems.WhileLTCMhadaseemingly
sophisticated VaR system in place, errors in parameter estimation, unexpectedly
large market moves (heavy tails) and in particular vanishing market liquidity drove
the hedge fund into near-bankruptcy, causing major ﬁnancial turbulence around the
globe. Jorion (2000) contains an excellent discussion of the LTCM case, in particular
comparing a Gaussian-basedVaR model with a t-based approach.At a more general
level, Jorion (2002b) discusses the various fallacies surrounding VaR-based market
risk management systems.
Most of the academic literature on liquidity focuses on the determinants of bid–
ask spreads and/or transaction cost (see, for example, the survey by Stoll (2000)).
Risk-management and hedging issues in illiquid markets have received relatively
little attention: optimal strategies for unwinding a position in an illiquid market
are discussed in Almgren and Chriss (2001); the hedging of derivatives in illiquid
markets has been studied by Jarrow (1994), Frey (1998, 2000), Sch¨onbucher and
Wilmott (2000) and Bank and Baum (2004), among others.
2.3
Standard Methods for Market Risks
In the following sections we discuss some standard methods used in the ﬁnancial
industry for measuring market risk over short time intervals, such as a day or a
fortnight. In the formal framework of Section 2.1.1 this amounts to the problem
of estimating risk measures for the loss distribution of a loss Lt+1 = l[t](Xt+1),
where Xt+1 is the vector of risk-factor changes from time t to time t + 1 and l[t]
is the loss operator based on the portfolio at time t; the risk measures on which we
concentrate are VaR (Deﬁnition 2.10) and expected shortfall (Deﬁnition 2.15). We
recall from Section 2.1.2 that the issue of whether we base our risk measurement on
the unconditional loss distribution of Lt+1 or the conditional loss distribution based
on information denoted by Ft is relevant. In presenting the standard methods we
clarify which of these approaches is generally adopted.
2.3.1
Variance–Covariance Method
We present a generic version of this method which may be turned into an unconditional or conditional method by varying the procedure that is used to estimate certain
key inputs. The risk-factor changes Xt+1 are assumed to have a multivariate normal
distribution (either unconditionally or conditionally) denoted by Xt+1 ∼Nd(µ, Σ),
where µ is the mean vector and Σ the covariance (or variance–covariance) matrix of
the distribution. The properties of the multivariate normal distribution are discussed
in detail in Section 3.1.3.
We assume that the linearized loss in terms of the risk factors is a sufﬁciently
accurate approximation of the actual loss and simplify the problem by considering
the distribution of L
t+1 = l
[t](Xt+1) with l
[t] deﬁned in (2.6). The linearized loss
--- page 65 ---

2.3. Standard Methods for Market Risks
49
operator will be a function with general structure
l
[t](x) = −(ct + b′
tx)
(2.29)
for some constant ct and constant vector bt, which are known to us at time t. For
a concrete example, consider the stock portfolio of Example 2.4 where the loss
operator takes the form l
[t](x) = −Vtw′
tx and wt is the vector of portfolio weights
at time t.
An important property of the multivariate normal is that a linear function (2.29)
of Xt+1 must have a univariate normal distribution. From general rules on the mean
and variance of linear combinations of a random vector we obtain that
L
t+1 = l
[t](Xt+1) ∼N(−ct −b′
tµ, b′
tΣbt).
(2.30)
Value-at-Risk may be easily calculated for this loss distribution using (2.19) in
Example 2.14. Expected shortfall may be calculated using (2.26) in Example 2.18.
To turn this into a practical procedure we require estimates of µ and Σ based on
historical risk-factor change data Xt−n+1, . . . , Xt. If we simply estimate µ and Σ by
calculating the sample mean vector and sample covariance matrix, then this amounts
to an analysis of the unconditional loss distribution under the tacit assumption that
the risk-factor change data come from a stationary process. The standard sample
estimates of mean and covariance are reviewed in Section 3.1.2.
To obtain a conditional version of this method we treat the data as a realization
of a multivariate time series and assume that Xt+1 | Ft ∼Nd(µt+1, Σt+1), where
µt+1 and Σt+1 now denote the conditional mean and covariance matrix given information to time t. We obtain estimates of these moments for substitution in (2.30)
by forecasting. This might involve the formal estimation of a time series model,
such as a multivariate GARCH model, and the use of model-based prediction methods. Alternatively, a more informal forecasting technique, such as the exponentially
weighted moving-average (EWMA) procedure popularized in JPMorgan’s Risk-
Metrics, might be used. The use of these techniques is discussed in greater detail in
Chapter 4.
Weaknesses of the method.
The variance–covariance method offers a simple analytical solution to the risk-measurement problem but this convenience is achieved at
the cost of two crude simplifying assumptions. First, linearization may not always
offer a good approximation of the relationship between the true loss distribution and
the risk-factor changes, as discussed at the end of Section 2.1.1. Second, the assumption of normality is unlikely to be realistic for the distribution of the risk-factor
changes, certainly for daily data and probably also for weekly and even monthly data.
A stylized fact of empirical ﬁnance suggests that the distribution of ﬁnancial risk
factor returns is leptokurtic and heavier-tailed than the Gaussian distribution. Later,
in Example 3.3, we present evidence for this observation in an analysis of daily,
weekly, monthly and quarterly stock returns. The implication is that an assumption
of Gaussian risk factors will tend to underestimate the tail of the loss distribution
and measures of risk, like VaR and expected shortfall, that are based on this tail.
--- page 66 ---

50
2. Basic Concepts in Risk Management
This criticism also applies to the conditional version of the variance–covariance
method. Even when we attempt an explicit time series modelling of the return
data, analyses mostly suggest that the conditional distribution of risk-factor changes
for the next time period, given information up to the present, is not multivariate
Gaussian, but rather a distribution whose margins have heavier tails. Another way
of putting this is to say that the innovation distribution of the time series model is
generally heavier-tailed than normal (see Example 4.24).
Extensions of the method.
The convenience of the method relies on the fact that a
linear combination of a multivariate Gaussian vector has a univariate Gaussian distribution. However, there are other multivariate distribution families that are closed
under linear operations, and variance-covariance methods can also be developed
for these. Examples include multivariate t distributions and multivariate generalized
hyperbolic distributions, which we describe in detail in Chapter 3.
For example, suppose we model risk-factor changes (either unconditionally or
conditionally) with a multivariate t distribution denoted Xt+1 ∼td(ν, µ, Σ), where
this notation is explained in Example 3.7 and Section 3.4. Then the analogous
expression to (2.30) is
L
t+1 = l
[t](Xt+1) ∼t(ν, −ct −b′
tµ, b′
t ˜Σbt),
(2.31)
and risk measures can be calculated using (2.20) and (2.27).
2.3.2
Historical Simulation
Instead of estimating the distribution of L = l[t](Xt+1) under some explicit parametric model for Xt+1, the historical-simulation method can be thought of as estimating the distribution of the loss operator under the empirical distribution of data
Xt−n+1, . . . , Xt. The method can be concisely described using the loss-operator
notation; we construct a univariate dataset by applying the operator to each of our
historical observations of the risk-factor change vector to get a set of historically
simulated losses:
{ ˜Ls = l[t](Xs) : s = t −n + 1, . . . , t}.
(2.32)
The values ˜Ls show what would happen to the current portfolio if the risk-factor
changes on day s were to recur. We make inference about the loss distribution and
risk measures using these historically simulated loss data.
This is an unconditional method. If we assume that the process of risk-factor
changes is stationary with df FX, then (subject to further technical conditions) the
empirical df of the data is a consistent estimator of FX. Hence the empirical df of the
data ˜Lt−n+1, . . . , ˜Lt is a consistent estimator of the df of l[t](X) under FX. More
formally, an appropriate version of the strong law of large numbers for time series
can be used to show that, as n →∞,
Fn(l) := 1
n
t
s=t−n+1
I{ ˜Ls⩽l} = 1
n
t
s=t−n+1
I{l[t](Xs)⩽l}
→P(l[t](X) ⩽l) = FL(l),
--- page 67 ---

2.3. Standard Methods for Market Risks
51
where X is a generic vector of risk-factor changes with distribution FX and
L := l[t](X).
In practice there are various ways we can use the historically simulated loss
data. It is common to estimate VaR using the method of empirical quantile estimation, whereby theoretical quantiles of the loss distribution are estimated by sample quantiles of the data. If we denote the ordered values of the data in (2.32)
by ˜Ln,n ⩽· · · ⩽˜L1,n, one possible estimator of VaRα(L) is ˜L[n(1−α)],n, where
[n(1 −α)] denotes the largest integer not exceeding n(1 −α). For example, if
n = 1000 and α = 0.99, we would estimate the VaR by taking the 10th largest
value. To estimate the associated expected shortfall an obvious empirical estimator
following from the representation (2.28) would be the average of the 10 largest
losses. As an alternative, particularly in situations where n is relatively modest in
size, we could ﬁt a parametric univariate distribution to the data (2.32) and calculate
risk measures analytically from this distribution.
Strengths and weaknesses of the method.
The historical-simulation method has
obvious attractions: it is easy to implement and reduces the risk-measure estimation
problem to a one-dimensional problem; no statistical estimation of the multivariate
distribution of X is necessary, and no assumptions about the dependence structure
of risk-factor changes are made.
However, the success of the approach is highly dependent on our ability to collect
sufﬁcient quantities of relevant, synchronized data for all risk factors. Whenever
there are gaps in the risk-factor history, or whenever new risk factors are introduced
into the modelling, there may be problems ﬁlling the gaps and completing the
historical record. These problems will tend to reduce the effective value of n and
mean that empirical estimates ofVaR and expected shortfall have very poor accuracy.
Ideally we want n to be fairly large since the method is an unconditional method
and we want a number of extreme scenarios in the historical record to provide more
informative estimates of the tail of the loss distribution. Indeed the method has
been referred to as “driving a car while looking through the rear view mirror”; this
obvious deﬁciency, which is shared by all purely statistical procedures, could be
compensated for by adding historical extreme events to the available database or by
formulating relevant extreme scenarios.
The fact that the method is an unconditional method could be seen as a further
weakness; we have remarked in Section 2.1.2 that the conditional approach is generally considered to be the more relevant for day-to-day market risk management.
Extensions of the method.
Simple empirical estimates of the VaR and especially
the expected shortfall are likely to be inaccurate, particularly in situations where n
is of modest size (say only a few years of daily data). Moreover, the approach of
ﬁtting parametric univariate distributions to the historically simulated losses may
not result in models that provide a particularly good ﬁt in the tail area where our
risk-measure estimates are calculated. A possible solution to this problem is to use
the techniques of extreme value theory (EVT) to provide estimates of the tail of
the loss distribution that are as faithful as possible to the most extreme data and
--- page 68 ---

52
2. Basic Concepts in Risk Management
that use parametric forms that are supported by theory. In Chapter 7 we describe a
standard EVT method based on the generalized Pareto distribution that is useful in
this context.
It is possible to develop conditional approaches based on the basic template of
historical simulation. One simple approach might be to model the historically simulated data in (2.32) with a univariate time series and to use this model to calculate
conditional estimates for the loss Lt+1 = l[t](Xt+1). Formally speaking, this is not
quite the conditional approach as we have previously deﬁned it: we do not consider
the conditional distribution of Lt+1 conditional on Ft, the sigma ﬁeld generated by
(Xs)s⩽t,butratherconditionalon,say,Gt,thesigmaﬁeldgeneratedby(l[t](Xs))s⩽t,
which is a less rich information set. In practice, however, this simple method may
often work well. See Notes and Comments for references to another conditional
version of historical simulation.
2.3.3
Monte Carlo
The Monte Carlo method is a rather general name for any approach to risk measurement that involves the simulation of an explicit parametric model for risk-factor
changes. As such, the method can be either conditional or unconditional depending
on whether the model adopted is a dynamic time series model for risk-factor changes
or a static distributional model.
The ﬁrst step of the method is the choice of the model and the calibration of this
model to historical risk-factor change data Xt−n+1, . . . , Xt. Obviously it should be
a model from which we can readily simulate, since in the second stage we generate
m independent realizations of risk-factor changes for the next time period, which
we denote by ˜X(1)
t+1, . . . , ˜X(m)
t+1.
In a similar fashion to the historical-simulation method, we apply the loss operator
to these simulated vectors to obtain simulated realizations { ˜L(i)
t+1 = l[t]( ˜X(i)
t+1) :
i = 1, . . . , m} from the loss distribution. These simulated loss data are used to
estimate risk measures; very often this is done by simple empirical quantile and
shortfall estimation, as described above, but it would again be possible to base the
inference on ﬁtted univariate distributions or to use an extreme value model to model
the tail of the simulated losses. Note that the use of Monte Carlo means that we are
free to choose the number of replications m ourselves, within the obvious constraints
of computation time. Generally m can be chosen to be much larger than n so that
we obtain more accuracy in empirical VaR and expected shortfall estimates than is
possible in the case of historical simulation.
Weaknesses of the method.
The method does not solve the problem of ﬁnding a
multivariate model for Xt+1 and any results that are obtained will only be as good
as the model that is used. In a market risk context a dynamic model seems desirable
and some kind of GARCH structure with a heavy-tailed multivariate conditional
distribution, such as multivariate t, might be considered. The models we describe
in Section 4.6 provide possible candidates.
For large portfolios the computational cost of the Monte Carlo approach can be
considerable, as every simulation requires the revaluation of the portfolio. This is
--- page 69 ---

2.3. Standard Methods for Market Risks
53
particularly problematic if the portfolio contains many derivatives which cannot be
priced in closed form. Variance-reduction techniques such as importance sampling
can be of help here. We discuss the application of importance sampling in models
for credit risk management in Section 8.5; further references on variance-reduction
techniques are given in Notes and Comments.
2.3.4
Losses over Several Periods and Scaling
So far we have considered one-period loss distributions and associated risk measures. It is often the case that we would like to infer risk measures for the loss
distribution over several periods from a model for single-period losses. For example, suppose that we work with a model for daily risk-factor changes which is set up
to allow calculations of a daily VaR and expected shortfall. We might want to also
obtain estimates of VaR and expected shortfall for the one-week or one-month loss
distribution assuming that the portfolio is held constant throughout that time.
Anobviousapproachistoaggregatedailyrisk-factorchangedatainordertoobtain
risk-factor change data at a lower frequency and to make a one-period estimation
using these data. Clearly, this results in a reduction in the number of data and
necessitates a new analysis of the aggregated data. The former problem can be
avoided by the formation of overlapping risk-factor returns (a construction that is
described in Section 4.1) but this is not really recommended as it introduces new
serial dependencies into the data that greatly complicate statistical modelling.
Scaling.
It would be far more attractive if we had simple rules for transforming
one-period risk measures into h-period risk measures for h > 1. Suppose we denote
the loss from time t over the next h periods by L(h)
t+h. Arguing as in (2.1) and (2.3)
we have
L(h)
t+h = −(Vt+h −Vt) = −(f (t + h, Zt+h) −f (t, Zt))
= −(f (t + h, Zt + Xt+1 + · · · + Xt+h) −f (t, Zt))
=: l(h)
[t]

h

i=1
Xt+i

,
where l(h)
[t] represents a loss operator at time t for the h-period loss. The general
question of interest is how risk measures applied to the distribution of L(h)
t+h scale
with h, and this has no simple answer except in special cases.
Note that the h-period loss operator differs from the one-period loss operator in
situations where the mapping depends explicitly on time (such as derivative portfolios). For simplicity let us consider the case in which the mapping does not depend
on calendar time, so that l(h)
[t] (x) = l[t](x). The linearized form of this operator will
be l
[t](x) = b′
tx for some vector bt which is known at time t. We look at the simpler
problem of scaling for risk measures applied to the linearized loss distribution:
L(h)
t+h = l
[t]

h

i=1
Xt+i

=
h

i=1
b′
tXt+i.
(2.33)
--- page 70 ---

54
2. Basic Concepts in Risk Management
The following example shows a special case where we do have a very simple scaling,
known as the square-root-of-time rule.
Example 2.23 (square-root-of-time scaling). Suppose the risk-factor change vectors are iid with distribution Nd(0, Σ). Then h
i=1 Xt+i ∼Nd(0, hΣ) and the
distribution of L(h)
t+h in (2.33) satisﬁes (both conditionally and unconditionally)
L(h)
t+h ∼N(0, hb′
tΣbt). It then follows easily from (2.19) and (2.26) that both quantiles and expected shortfalls for this distribution scale according to the square root
of time (
√
h). For example, writing ES(h)
α
for the expected shortfall, we have
ES(h)
α
=
√
hσ φ(Φ−1(α))
1 −α
,
where σ 2 = b′
tΣbt. Clearly, ES(h)
α
=
√
h ES(1)
α and, with similar notation, VaR(h)
α
=
√
h VaR(1)
α .
This scaling rule is quite commonly used in practice and is easily implemented
in the context of the variance–covariance method. However, empirical risk-factor
change data generally support neither a Gaussian distributional assumption nor an
iid assumption. It is a stylized fact of empirical ﬁnance that, although ﬁnancial
risk-factor changes possess low serial correlation, they show patterns of changing
volatility that are not consistent with an iid model (see Section 4.1). To obtain reasonable models for risk-factor change data we require dynamic time series models,
such as models from the GARCH family. However, relatively little is known about
the scaling of risk measures under such models.When considering the distribution of
the h-period loss L(h)
t+h (or its linearized form) we have to be aware that the scaling of
risk measures applied to this distribution will also depend on whether we consider
the unconditional distribution or the conditional distribution given Ft. Very little
theory exists for either question but empirical studies suggest that the true scaling
can be very different from square-root-of-time scaling (see Notes and Comments
for more on this).
Monte Carlo approach.
It is possible to use a Monte Carlo approach to the problem
of determining risk measures for the h-period loss distribution. Suppose we have
a model for risk-factor changes, either distributional or dynamic, depending on
whether we are performing an unconditional or conditional analysis.
In the dynamic case we simulate future paths of the process ˜X(j)
t+1, . . . , ˜X(j)
t+h
for j = 1, . . . , m, where m is a predetermined large number of replications. (In
the unconditional case we would simply simulate realizations from a multivariate
distribution.) We then apply the h-period loss operator to these simulated data to
obtain Monte Carlo simulated losses:
{ ˜L(h)(i)
t+h
= l(h)
[t] ( ˜X(i)
t+1 + · · · + ˜X(i)
t+h) : i = 1, . . . , m}.
These are used to make statistical inference about the loss distribution and associated
risk measures, as described in Section 2.3.3.
--- page 71 ---

2.3. Standard Methods for Market Risks
55
2.3.5
Backtesting
In the preceding sections we have considered standard methods for estimating risk
measures at a time t for the distribution of losses in the next period. When this
procedure is continually implemented over time we have the opportunity to monitor
the performance of methods and compare their relative performance. This process
of monitoring is known as backtesting.
Suppose that at time t we make estimates of both VaR and expected shortfall for
one period and h periods. We denote the true one-period risk measures by VaRt
α
and ESt
α and the true h-period measures by VaRt,h
α and ESt,h
α . These may be unconditional or conditional risk measures, but for the purposes of this section we leave
this unspeciﬁed. At time t + 1 we have the opportunity to compare our one-period
estimates with what actually happened; at time t + h we have the opportunity to do
the same for the h-period estimates.
By deﬁnition of VaR (and assuming a continuous loss distribution) we have that
P(Lt+h > VaRt,h
α ) = 1 −α so that the probability of a so-called violation of VaR is
1−α. In practice the risk measures have to be estimated from data and we introduce
an indicator notation for violations of the VaR estimates:
ˆIt+1 := I{Lt+1>
VaRt
α},
ˆI (h)
t+h := I{L(h)
t+h>
VaRt,h
α }.
(2.34)
We expect that if our estimation method is reasonable then these indicators should
behave like Bernoulli random variables with success (i.e. violation) probability close
to (1 −α). If we conduct multiple comparisons of VaR predictions and corresponding realized losses, then we expect the proportion of occasions on which VaR is
violated to be about 1 −α.
In more speciﬁc situations we can say more. For example, if we form one-stepahead estimates of a conditional one-period VaR using a dynamic approach, then
we expect that the violation indicators ˆIt in (2.34) should behave like iid Bernoulli
rvs with expectation (1 −α); the number of violations over m time periods should
be binomial with expected value m(1 −α). This will be discussed in more detail in
Section 4.4.3.
We would also like to be able to backtest the success of our expected shortfall
estimation. Considering, for simplicity, the one-period expected shortfall estimate,
it follows from Lemma 2.16 that for a continuous loss distribution the identity
E((Lt+1 −ESt
α)I{Lt+1>VaRtα}) = 0
is satisﬁed. This suggests we look at the discrepancy Lt+1 −
ESt
α on days when the
estimated VaR is violated. These should come from a distribution with mean zero.
Under further modelling assumptions we look at this idea in more detail in Section 4.4.3.
2.3.6
An Illustrative Example
We conclude the chapter by giving an example that illustrates some of the ideas
we have mentioned and which sets the scene for material presented in Chapters 3
--- page 72 ---

56
2. Basic Concepts in Risk Management
−0.04
0
0.04
0.04
−0.04
0.04
1992 1993 1994 1995 1996 1997 1998 1999 2000 2001 2002 2003 2004
−0.02
0.02
(a)
(b)
(c)
(d)
(e)
0
−0.02
0.02
0
0
−0.04
0
Figure 2.2.
Time series of risk-factor changes. These are log-returns on (a) the FTSE 100,
(b) the S&P 500 and (c) the SMI indexes, as well as log-returns for (d) the GBP/USD and
(e) the GBP/CHF exchange rates for the period 1992–2003.
and 4. We consider the application of methods belonging to the general categories of
variance–covarianceandhistorical-simulationmethodstotheportfolioofaninvestor
in international equity indexes. The investor is assumed to have domestic currency
sterling (GBP) and to invest in the FinancialTimes 100 Shares Index (FTSE 100), the
Standard & Poor’s 500 (S&P 500) and the Swiss Market Index (SMI). The investor
thus has currency exposure to US dollars (USD) and Swiss francs (CHF) and the
value of the portfolio is inﬂuenced by ﬁve risk factors (three log index values and
two log exchange rates). The corresponding risk-factor return time series for the
period 1992–2003 are shown in Figure 2.2.
On any day t we standardize the total portfolio value Vt in sterling to be one and
consider that the portfolio weights (the proportions of this total value invested in each
oftheindexesFTSE100,S&P500,SMI)are30%,40%and30%,respectively.Using
similar reasoning to that in Example 2.4, it may be veriﬁed that the loss operator is
l[t](x) = 1 −(0.3ex1 + 0.4ex2+x4 + 0.3ex3+x5),
and its linearized version is
l
[t](x) = −(0.3x1 + 0.4(x2 + x4) + 0.3(x3 + x5)),
--- page 73 ---

2.3. Standard Methods for Market Risks
57
where x1, x2 and x3 represent log-returns on the three indexes and x4 and x5 are
log-returns on the GBP/USD and GBP/CHF exchange rates.
Our objective is to calculate VaR estimates at the 95% and 99% levels for all
trading days in the period 1996–2003. Where local public holidays take place in
individual markets (e.g. the Fourth of July in the US) we record artiﬁcial zero
returns for the market in question, thus preserving around 260 days of risk-factor
return data in each year. We use the last 1000 days of historical data Xt−999, . . . , Xt
to make all VaR estimates for day t + 1 with the following methods.
VC. The standard unconditional variance–covariance method assuming multivariate Gaussian risk-factor changes as described in Section 2.3.1.
HS. The standard unconditional historical simulation method as described in Section 2.3.2.
VC-t. An unconditional variance–covariance method in which a multivariate t distribution is ﬁtted to the risk-factor change data (see Chapter 3, and Sections 3.2.4
and 3.2.5 in particular).
HS-GARCH. A conditional version of the historical simulation method in which
GARCH(1, 1) models with a constant conditional mean term and Gaussian innovations are ﬁtted to the historically simulated losses to estimate the volatility of
the next day’s loss (see Chapter 4, and Section 4.4.2 in particular).
VC-MGARCH. A conditional version of the variance–covariance method in which
a multivariate GARCH model (a ﬁrst-order constant conditional correlation
model) with multivariate normal innovations is used to estimate the conditional
covariance matrix of the next day’s risk-factor changes (see Chapter 4, and Section 4.6 in particular).
HS-EWMA. A conditional method, similar to HS-GARCH, in which the EWMA
method rather than a GARCH model is used to estimate volatility (see Sections 4.4.1 and 4.4.2).
VC-EWMA. A similar method to VC-MGARCH but a multivariate version of the
EWMA method is used to estimate the conditional covariance matrix of the next
day’s risk-factor changes (see Section 4.6.6).
HS-GARCH-t. A similar method to HS-GARCH but Student t innovations are
assumed in the GARCH model.
VC-MGARCH-t. A similar method to VC-MGARCH but multivariate t innovations are used in the MGARCH model.
HS-CONDEVT. A conditional method using a combination of GARCH modelling
and EVT (extreme value theory) (see Section 7.2.6).
This collection of methods is of course far from complete and is merely meant
as an indication of the kinds of strategies that are possible. In particular, we have
conﬁned our interest to rather simple GARCH models and not added, for example,
asymmetric innovation distributions or leverage effects (see Section 4.3.3), which
can often further improve the performance of such methods.
--- page 74 ---

58
2. Basic Concepts in Risk Management
Table 2.2.
Numbers of violations of the 95% and 99%VaR estimate calculated using various
methods, as described in Section 2.3.6. The error column shows for each method the average
absolute discrepancy per year between observed and expected numbers of violations.
Year
1996
1997
1998
1999
2000
2001
2002
2003
Trading days
261
260
259
260
259
260
260
260
error
Results for 95% VaR
Expected no.
13
13
13
13
13
13
13
13
of violations
VC
13
30
29
15
13
20
27
6
7.88
HS
14
30
31
16
14
20
26
8
8.12
VC-t
14
32
35
19
16
23
29
8
10.25
HS-GARCH
15
17
15
15
14
21
19
11
3.38
VC-MGARCH
16
19
19
15
15
21
21
12
4.50
HS-EWMA
16
14
15
15
17
23
18
11
3.62
VC-EWMA
15
13
15
14
18
22
17
9
3.38
HS-GARCH-t
16
18
16
15
15
21
19
12
3.75
VC-MGARCH-t
18
19
19
17
16
23
21
11
5.50
HS-CONDEVT
14
16
15
15
14
18
18
10
2.75
Results for 99% VaR
Expected no.
2.6
2.6
2.6
2.6
2.6
2.6
2.6
2.6
of violations
VC
5
11
20
5
2
6
12
2
5.58
HS
3
10
13
3
2
3
7
1
3.20
VC-t
3
11
15
4
2
4
9
1
4.08
HS-GARCH
10
7
7
6
5
4
5
3
3.27
VC-MGARCH
8
8
7
6
3
5
7
4
3.40
HS-EWMA
9
5
6
6
6
6
3
2
2.92
VC-EWMA
9
5
6
6
5
5
3
3
2.65
HS-GARCH-t
7
5
5
5
4
3
4
2
1.93
VC-MGARCH-t
7
5
6
4
2
1
4
1
2.10
HS-CONDEVT
5
4
5
5
2
2
3
2
1.35
From the results collected in Table 2.2 we conclude that the three unconditional
methods (VC, HS andVC-t) are generally outperformed by the conditional methods.
In particular, the years 1997, 1998 and 2002 are handled poorly by the unconditional
methods and give rise to too many violations of the 95% and 99% VaR estimates.
Historical simulation is preferred to variance–covariance at the 99% level but gives
a poor performance compared with variance–covariance at the 95% level. Basing
the unconditional variance–covariance method on a multivariate t distribution gives
an improvement at the 99% level but actually makes things worse at the 95% level.
The simple univariate GARCH procedures using the historically simulated data
work quite well; t innovations are preferred to Gaussian innovations at the 99%
level. The simpler method of volatility estimation using EWMA competes well with
--- page 75 ---

2.3. Standard Methods for Market Risks
59
02.01.02
02.05.02
02.09.02
−0.04
−0.02
0.02
0.04
0.06
0
−0.04
−0.02
0.02
0.04
0.06
0
(a)
(b)
Figure 2.3.
Daily losses for 2002 together with risk-measure estimates ((a) 95% VaR estimates, (b) 99% VaR estimates) and violations for the HS and HS-GARCH-t methods. The
HS VaR estimates are indicated by a solid line and violations are indicated by circles; the
HS-GARCH-t estimates are given by a dotted line with triangles for violations. For more
information see Section 2.3.6.
the full GARCH estimation. The best method of all is HS-CONDEVT, combining
extremevaluetheorywithGARCHmodelling.ThemultivariateGARCHprocedures
do not offer any improvement on the univariate procedures in this particular example.
In Figure 2.3 we have singled out the year 2002 and shown actual losses together
with risk-measure estimates and violations for two of the methods: HS and HS-
GARCH-t. In this volatile year, the standard historical-simulation method did not
perform well: there are 26 violations of the 95%VaR estimate and 7 violations of the
99%VaR estimate, or about twice as many as would be expected. The HS-GARCH-t
method, being a conditional method, is able to respond to the changes in volatility
throughout 2002 and consequently gives 19 and 4 violations; this is still a few more
than expected at the 95% level but is a good performance at the 99% level.
Notes and Comments
Standard methods for market risk are described in detail in Jorion (2001) and Crouhy,
Galai and Mark (2001). For the variance–covariance approach, particularly in a
dynamic form using EWMA, see Mina and Xiao (2001).
Another conditional version of historical simulation is used by Hull and White
(1998) and Barone-Adesi, Bourgoin and Giannopoulos (1998). To describe this
method succinctly we anticipate some of the notation used in Section 4.6. Suppose
that we consider a simple model of risk-factor changes of the form Xt = tZt,
where t is a diagonal matrix containing so-called volatilities and the Zt are iid
--- page 76 ---

60
2. Basic Concepts in Risk Management
vectors of innovations. We would like to apply historical simulation to the innovations but these are unobserved. Univariate time series models (typically GARCH
models) are applied to each time series of risk-factor changes; this effectively gives
us estimates of the volatility matrices { ˆs : s = t −n + 1, . . . , t} and allows us to
make a prediction ˆt+1 of the volatility matrix in the next time period. We then
construct residuals { ˆZs = ˆ−1
s Xs : s = t −n + 1, . . . , t}, which are treated like
observations of the unobserved innovations. To make statistical inference about the
distribution of Lt+1 = l[t](Xt+1) = l[t](t+1Zt+1) given Ft we use the historicalsimulation data {l[t]( ˆt+1 ˆZs) : s = t −n + 1, . . . , t}.
The book by Glasserman (2003a) is an excellent general introduction to simulation techniques in ﬁnance. Glasserman, Heidelberger and Shahabuddin (1999)
present efﬁcient numerical techniques (based on delta–gamma approximations and
advanced simulation techniques) for computing VaR for derivative portfolios in the
presence of heavy-tailed risk factors.
A useful summary of scaling results for market risk measures may be found in
Kaufmann (2004) (see also Brummelhuis and Kaufmann 2004; Embrechts, Kaufmann and Patie 2005). In these papers the message emerges that, for unconditional
VaR scaling over longer time horizons, the square-root-of-time rule often works well.
On the other hand, for conditionalVaR scaling over short time horizons, McNeil and
Frey (2000) present evidence against square-root-of-time scaling. For further comments on these and further scaling issues, see Diebold et al. (1998) and Dan´ıelsson
and de Vries (1997c). Literature on backtesting is given in the Notes and Comments
section of Section 4.4.
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
