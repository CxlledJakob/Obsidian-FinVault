# Quantitative Risk Management_ Concepts, Techniques, and -- Alexander J_ McNeil, Rüdiger Frey, Paul Embrechts -- Princeton series in finance, -- isbn13 9780691122557 -- 478a0059673fecd0c76229cd3d8884e7 -- Anna’s Arc.pdf — pages 419–438

--- page 419 ---

9.3. Financial and Actuarial Pricing
403
frequentlyappliedinpracticetogofromphysicaltorisk-neutraldefaultprobabilities.
Note, however, that (9.10) is only justiﬁed, strictly speaking, in the narrow context
of the Merton model.
In standard reduced-form models the default time is modelled as a doubly stochastic random time with hazard rate γ P
t
= hP (Ψt) (under the physical measure P) and
γ Q
t
= hQ(Ψt) (under a risk-neutral measure Q). Here (Ψt) is some d-dimensional
process representing economic factors, which is adapted to the background ﬁltration (Ft); hP and hQ are functions from Rd to R+. In this context arbitrage theory
alone gives little guidance on the form of the ratio hQ/hP , the only restriction being
that hQ must be chosen so that the model is consistent with observed prices of traded
credit-risky securities. Recent research has therefore tried to derive further restrictions on the ratio hQ/hP by bringing in economic arguments (see, for example,
Jarrow, Lando and Yu 2005).
In practice, one usually postulates that hP and hQ belong to a given parametric
family of functions from Rd to R+. For instance, one might assume that hQ = νhP
for some scaling factor ν > 0. The function hP can be determined by ﬁtting the
model to historical default probabilities; ν is found by ﬁtting the model to observed
prices of corporate bonds or credit default swaps. Alternatively, the model is set up
directly under Q and one restricts oneself to determining hQ from observed market
prices of corporate bonds or credit default swaps; this is the martingale-modelling
approach discussed in Section 9.3.3 below.
Empirical evidence.
As discussed above, the risk-neutral default probability of
a corporation can be estimated from credit-spread data for bonds issued by that
corporation. By comparing these estimates with estimates for the physical default
probability—obtained, for instance, from the KMV model introduced in Section 8.2.3—it is possible to gain some empirical evidence on the relationship of
physical and risk-neutral default probabilities in real markets. Understanding this
relationship is important, as it enables market participants to use information on historical default probabilities in pricing credit-risky securities, and conversely to use
prices of defaultable bonds or market quotes for credit default swaps as additional
input in determining historical default probabilities.
An extensive empirical study of the relationship between physical and historical
default probabilities is Berndt et al. (2004). In this study market quotes for fair
CDS spreads (instead of credit spreads of corporate bonds) are used to infer riskneutral default probabilities. In this way, problems related to the differing taxation
of corporate and treasury bonds can be circumvented. The authors ran regression
analyses of the observed spreads for ﬁve-year CDSs against ﬁve-year EDFs for a
large pool of ﬁrms. The ﬁve-year EDF of a ﬁrm with publicly traded stock is an
annualized estimate of the physical ﬁve-year default probability. The computation of
EDFs is described in detail in Section 8.2.3, and annualization is a way of expressing
EDFs for different time horizons on a common yearly scale. A formal treatment of
CDS pricing is given below in Section 9.3.3 (for models where the default time τ
has a deterministic risk-neutral hazard rate) and in Section 9.4.3 (for the case of a
doubly stochastic default time).
--- page 420 ---

404
9. Dynamic Credit Risk Models
For the interpretation of the regression results, it sufﬁces to know that, in an
environment where the default-free interest rate (rt) and the risk-neutral hazard rate
(γ Q
t,i) of some ﬁrm i do not ﬂuctuate too much, we have an approximate relationship
between the risk-neutral hazard rate γ Q
t,i, the fair CDS spread x∗
i observed at time t
and the percentage loss given default δi (assumed deterministic) of the form
γ Q
t,i ≈x∗
i /δi
(9.11)
(see Section 9.3.3 for details). Moreover, it is an immediate consequence of (9.7)
that in models with a doubly stochastic default time the risk-neutral hazard rate γ Q
t,i
is approximately equal to the conditional risk-neutral one-year default probability
¯qt,i of ﬁrm i at time t.
Berndt et al. (2004) began by estimating the following simple linear model for
the relationship between the observed swap spread x∗
i of ﬁrm i and the ﬁve-year
EDF, labelled EDFi, on the same day, both measured in basis points (one basis point
equals 0.01%):
x∗
i = 52.26 + 1.627 EDFi +εi.
(9.12)
The model (9.12) was estimated using a large sample of more than 18 000 CDS–EDF
observations from September 2000 toAugust 2003 for ﬁrms from three industry sectors (NorthAmerican Oil and Gas, NorthAmerican Healthcare and NorthAmerican
Broadcasting and Entertainment). The authors propose the following interpretation
of this regression result. Under the model (9.12) the fair swap spread x∗
i increases
by approximately 16 basis points for every 10 basis point increase in the ﬁveyear EDF; neglecting the intercept, which is small, we have approximately that
x∗
i / EDFi ≈1.6. Assuming that the risk-neutral loss given default, δ, equals, say,
0.75, and that risk-neutral and physical default intensities are relatively stable over
time, this would imply a ratio of risk-neutral to physical default intensity of
γ Q
γ P ≈x∗
i /δ
EDFi
= 1
δ
x∗
i
EDFi
≈
1
0.75 · 1.6 = 2.13.
As explained above, γ Q/γ P ≈¯q/ ¯p, so these numbers also relate to the ratio of
risk-neutral and physical default probabilities. A loss given default of δ = 0.75 is
a very conservative (high) estimate. If we take a lower value for δ, say δ = 0.5, we
obtain a ratio of ¯q/ ¯p ≈
1
0.5 · 1.6 = 3.2, i.e. the ratio of risk-neutral to actual default
probability gets even higher.
A careful inspection of the CDS–EDF relationship shows that the simple linear
model (9.12) might not be appropriate for a number of reasons. First, the high
intercept of 52.26 basis points is implausible, as it would imply that even for a ﬁrm
with historical default probability ¯p close to zero the swap spread is still of the
order of 50 basis points. Second, Berndt et al. (2004) found that the ratio x∗
i / EDFi
varies between industry sectors—reﬂecting different recovery rates for different
industries—and over time, as is illustrated in Figure 9.6. Third, there seems to be
some concavity in the relationship between swap spreads and EDFs; in particular,
the ratio x∗
i / EDFi is higher for high-quality ﬁrms with low EDF values than for
--- page 421 ---

9.3. Financial and Actuarial Pricing
405
Aug Oct Dec Feb Apr Jun Aug Oct Dec Feb Apr
2001
2002
2003
1.5
2.5
3.5
2.0
3.0
Ratio
Figure 9.6.
Ratio of one-year risk-neutral and historical default probabilities for
Vintage Petroleum, as estimated by Berndt et al. (2004).
low-quality ﬁrms. For these reasons the authors go on to consider a more reﬁned
logarithmic regression model, which ﬁts the data signiﬁcantly better.
The analysis of Berndt et al. (2004) is corroborated by other empirical work on
default risk premiums mentioned in Notes and Comments. This empirical research
clearly shows that physical and risk-neutral default probabilities can differ substantially, and care must be taken to distinguish between the two concepts.
9.3.2
Risk-Neutral Pricing and Market Completeness
It is a fundamental insight of modern mathematical ﬁnance that in a complete market
the price of derivative securities can be computed as the mathematical expectation
of the discounted pay-off under a risk-neutral measure. In this section we explain
the idea underlying this important result and discuss its applicability to the pricing
of credit derivatives. We refrain from a general analysis; instead we use variants of
the simple static model introduced in Example 9.17 as a vehicle for our discussion.
Consider, in the context of Example 9.17, an investor, for example an investment bank, who plans to sell credit derivatives on the zero-coupon bond with
price p1(· , T ). In particular, consider a default put option with maturity date T = 1.
This contract pays one unit if the bond defaults and zero otherwise; it can be thought
of as a simpliﬁed version of a CDS. Obviously, the pay-off of the default put is
unknown at date t = 0 and thus constitutes a risk. Therefore, two questions arise
for our investor: how should the option be priced, and how should the risk incurred
by selling it be dealt with? The answer given by the modern theory of mathematical
ﬁnance goes back to the seminal papers of Black and Scholes (1973) and Merton
(1973), who showed that it is often possible to replicate the pay-off of a derivative security by (dynamic) trading in the underlying assets. It follows that the risk
incurred by the seller can be eliminated; moreover, the fair price of the derivative is
given by the initial price of the replicating portfolio.
Let us apply this insight to the default put. We form a portfolio in the defaultable
bond and cash, with value at time t = 1 equal to the pay-off of the put. At time
--- page 422 ---

406
9. Dynamic Credit Risk Models
t = 0 we go short 2.5 units of the bond and hold 50
21 ≈2.38 units of cash. At time
t = 1 there are two possibilities for the value V1 of this portfolio.
• Default occurs: in which case V1 = (−2.5) · 0.6 + 50
21 · 1.05 = 1.
• No default: in which case V1 = (−2.5) · 1 + 50
21 · 1.05 = 0.
In either case the value V1 of the hedge portfolio equals the pay-off of the option.
Hence the fair price at t = 0 of the option should equal the value of the hedge
portfolio at t = 0 given by V0 = (−2.5) · 0.941 + 50
21 ≈0.0285; otherwise either
the buyer or the seller could make some riskless proﬁt. To construct the portfolio in
this simple one-period, two-state setting we have to consider two linear equations.
Denote by ξ1 and ξ2 the units of the defaultable bond and the amount of cash in our
portfolio. At time t = 1 we must have ξ1 · 0.6 + ξ2 · 1.05 = 1 (the default case),
and ξ1 · 1 + ξ2 · 1.05 = 0 (the no-default case), which leads to the above values of
ξ1 = −2.5 and ξ2 = 50
21.
In mathematical ﬁnance a derivative security is called attainable if there is a
(dynamic) portfolio strategy in traded underlying assets that replicates the pay-off
of the derivative. The above argument shows that in our simple one-period two-state
model every derivative security is attainable. Such models are termed complete.
Note that the physical default probability ¯p did not enter the pricing argument. It is nonetheless possible to compute the fair price of the default put as the
expected value of the discounted pay-off, if the risk-neutral measure Q is used
instead of the physical measure P. Recall that the risk-neutral default probability is given by ¯q = 0.03. The expected discounted pay-off under Q is given by
(1.05)−1(0.97 · 0 + 0.03 · 1) = 0.0285 and is thus equal to the fair price V0. This is,
of course, not a lucky coincidence. In fact, a basic result from mathematical ﬁnance,
the so-called risk-neutral pricing rule, states that the fair price of any attainable
claim can be computed as the expected value of the discounted pay-off under a riskneutral measure. Armed with this result, one typically ﬁrst computes the candidate
price (the expected value of the discounted pay-off under a risk-neutral measure)
and second determines the replicating strategy. For this reason a lot of research
focuses on the problem of computing prices. However, one should bear in mind
that the main economic justiﬁcation for computing prices as expected discounted
value under a risk-neutral measure stems from the hedging argument, and is therefore strictly speaking only justiﬁed for attainable claims. This issue has, to a large
extent, been neglected in the literature on the pricing of credit-risky securities. The
next example illustrates some of the difﬁculties arising in incomplete markets, where
most derivatives are not attainable.
Example 9.18 (a model with random recovery). As there is a substantial amount
of randomness in real recovery rates (see Section 8.4.6), it is interesting to study
the impact of random recovery rates on the validity of the above pricing arguments.
Consider the following variant of Example 9.17 with random recovery: the loss given
default may be either 30% or 50%, p1(0, 1) = 0.941, and the riskless interest-rate
equals 5%. The price evolution of p1(· , 1) is illustrated in Figure 9.7. We leave
--- page 423 ---

9.3. Financial and Actuarial Pricing
407
.
.
.
.
0.941
1.0 (no default)
0.7 (default,     = 30%)
0.5 (default,     = 50%)
δ
δ
Figure 9.7.
Evolution of the price of p1(· , 1) in Example 9.18.
the physical measure unspeciﬁed—we assume only that all three possible outcomes
have strictly positive probability.
We begin our analysis of this model by determining the equivalent martingale
measures. Put q1 := Q(p1(1, 1) = 0.5), q2 := Q(p1(1, 1) = 0.7) and q3 :=
Q(p1(1, 1) = 1), so that q3 = 1 −q1 −q2. We obtain the following equation for
q1 and q2,
p1(0, 1) = 1.05−1(q1 · 0.5 + q2 · 0.7 + (1 −q1 −q2) · 1),
(9.13)
and the restrictions q1 > 0, q2 > 0, 1 −q1 −q2 > 0. Obviously, Q is no longer
unique. It is easily seen from (9.13) that the set Q of equivalent martingale measures
is given by
Q = {q ∈R3 : q1 ∈(0, 0.024), q2 = 10
3 (1 −1.05 · p1(0, 1) −0.5 · q1),
q3 = 1 −(q1 + q2)}. (9.14)
It is interesting to look at the boundary cases. For q1 = 0 we obtain q2 = 4%,
q3 = 96%; this is the scenario where the risk-neutral default probability ¯q = q1 + q2
is maximized. For q1 = 2.4% we obtain q2 = 0, q3 = 97.6%; this is the scenario
where ¯q is minimized. Note, however, that the measures q0 := (0.024, 0, 0.976) and
q1 := (0, 0.04, 0.96) do not belong to Q, as they are not equivalent to the physical
measure P.
Consider a derivative security with pay-off H and maturity T = 1, such as the
default put with H = 0 if p1(1, 1) = 1 and H = 1 otherwise. Every price of the
form H0 = EQ(1.05−1H) for some Q ∈Q is consistent with no arbitrage and will
therefore be called an admissible value for the derivative. If Q contains more than
one element, as in our case, there is typically more than one admissible value. For
instance, we obtain for the default put option that
inf
Q∈Q EQ
 H
1.05

≈0.023
and
sup
Q∈Q
EQ
 H
1.05

≈0.038;
(9.15)
obviously, the inﬁmum and supremum in (9.15) correspond to the measures q0
and q1, where ¯q is minimized and maximized, respectively. This non-uniqueness of
admissible values reﬂects the fact that in our three-state model the put is no longer
attainable. In fact, the hedging portfolio (ξ1, ξ2) now has to solve the following three
--- page 424 ---

408
9. Dynamic Credit Risk Models
equations:
ξ1 · 0.5 + ξ2 · 1.05 = 1
(default, low recovery),
ξ1 · 0.7 + ξ2 · 1.05 = 1
(default, high recovery),
ξ1 · 1 + ξ2 · 1.05 = 0
(no default).
⎫
⎪⎬
⎪⎭
(9.16)
It is immediately seen that the system (9.16) of three equations and only two
unknowns has no solution, so that the default put is not attainable. This illustrates
two fundamental results from modern mathematical ﬁnance: a claim with bounded
pay-off is attainable if and only if the set of admissible values consists of a single number; an arbitrage-free market is complete if and only if there is exactly
one equivalent martingale measure Q. The second result is known as the second
fundamental theorem of asset pricing.
Example 9.18 shows that in an incomplete market conceptual issues arise which
are not present in models for complete markets. In particular, it is not obvious how
to choose the correct price of a derivative security from the range of admissible
values or how to deal with the risk incurred by selling a derivative security. This is
unfortunate, as realistic models, which capture the dynamics of ﬁnancial time series,
are typically incomplete. In recent years a number of interesting concepts for the risk
management of derivative securities in incomplete markets have been developed.
These approaches typically propose mitigating the risk by an appropriate trading
strategy and often suggest a pricing formula for the remaining risk. However, the
systematic application of these approaches to the pricing and the hedging of creditrisky securities is currently still in its infancy, and we refrain from further discussion.
A brief overview of the existing work on incomplete markets is given in Notes and
Comments.
9.3.3
Martingale Modelling
Recall that, according to the ﬁrst fundamental theorem of asset pricing, a model
for security prices is arbitrage free if and (essentially) only if it admits at least one
equivalent martingale measure Q. Moreover, in a complete market, the only thing
that matters for the pricing of derivative securities is the Q-dynamics of the traded
underlying assets. When building a model for pricing derivatives it is therefore
a natural shortcut to model the objects of interest—such as interest rates, default
times and the price processes of traded bonds—directly, under some exogenously
speciﬁed martingale measure Q. In the literature this approach is termed martingale
modelling.
Martingale modelling is particularly convenient if the value of the underlying
assets at some maturity date T is exogenously given, as in the case of zero-coupon
bonds. In that case the price of the underlying asset at time t < T can be computed
as the conditional expectation under Q of the discounted value at maturity. Formally, denoting by B(t) > 0 the so-called num´eraire (often the default-free savings
account) and by Gt the information available to investors at time t, we have the
following formula for the price at time t of a security, whose value at T is given by
--- page 425 ---

9.3. Financial and Actuarial Pricing
409
the FT -measurable rv H ⩾0:
Ht = B(t)EQ(B(T )−1H | Gt),
t ⩽T.
(9.17)
Model parameters are then determined using the requirement that at time t = 0 the
price of traded securities as computed from the model using (9.17) should coincide with the price of these securities as observed in the market; this is known as
calibration of the model to market data.
Martingale modelling ensures that the resulting model is arbitrage free, which is
advantageous if one has to model the prices of many different securities simultaneously. Therefore the approach is frequently adopted in default-free term structure
models and in reduced-form models for credit-risky securities. Martingale modelling has two drawbacks. First, historical information is, to a large extent, useless
in estimating model parameters, as these may change in the transition from the realworld measure to the equivalent martingale measure. For instance, as explained
above, physical and risk-neutral default probabilities and default intensities may
differ substantially. Second, as illustrated in Example 9.18, realistic models for
pricing credit derivatives are typically incomplete, so that one cannot eliminate all
risk by dynamic hedging. In those situations one is interested in the distribution of
the remaining risk under the actual risk measure P, so martingale modelling alone
is not sufﬁcient. In summary, the martingale-modelling approach is most suitable in
situations where the market for underlying securities is relatively liquid. In that case
we have sufﬁcient price information to calibrate our models, and issues of market
completeness become less relevant.
Martingale modelling with given CDS spreads.
We now use the martingalemodelling approach to construct a simple reduced-form pricing model with deterministic hazard rate for credit derivatives on a given reference entity. We assume
that market information consists of quotes for fair spreads for CDSs of varying
maturities on this entity. This example illustrates the model-building process if martingale modelling is used. Moreover, the example is of practical relevance: since the
CDS market is among the most liquid markets for credit-risky securities, the task of
building a model using CDS spreads as input is frequently encountered in practice.
Using martingale modelling we model the objects of interest directly under
some martingale measure Q. We assume that under Q the default time τ is
a random time with deterministic risk-neutral hazard rate γ Q(t). For simplicity we take interest rates and recovery rates (or equivalently loss given default)
to be deterministic. The percentage loss given default is denoted by δ ∈(0, 1).
The continuously compounded interest rate at time t is denoted by r(t) ⩾0, so
p0(0, t) = exp(−
 t
0 r(s) ds) is the price of the default-free zero-coupon bond with
maturity t. This is the simplest type of model that can be calibrated to a given term
structure of default-free interest rates and CDS spreads; generalizations allowing
for stochastic interest rates, recovery rates and hazard rates will be discussed in
Section 9.4.3 below.
We consider the following CDS. We take the notional to be one, so that percentage loss given default and absolute loss given default are the same. The premium
--- page 426 ---

410
9. Dynamic Credit Risk Models
payments are due at N points in time 0 < t1 < · · · < tN. If τ > tk, the protection buyer pays in tk a premium of size x∗(tk −tk−1), where x∗denotes the swap
spread. After default, no premium payments are made. If default occurs before the
maturity date tN of the swap, the protection seller makes a default payment of size δ
to the buyer at the default time τ. In a standard CDS the protection buyer pays the
protection seller at default the part of the premium which has accrued since the last
regular premium payment date; here we ignore these accrued premium payments to
simplify the exposition.
Given the risk-neutral hazard rate γ Q and a generic spread x, we now price the
payments made by the protection buyer (the so-called premium payment leg of the
swap) and the payments made by the protection seller (the default payment leg)
separately. The price of the premium payment leg at t = 0 (the expected discounted
value of the payments) is given by
V prem(x; γ Q) = EQ
 N

k=1
exp

−
 tk
0
r(u) du

x(tk −tk−1)I{tk<τ}

= x
N

k=1
p0(0, tk)(tk −tk−1)Q(τ > tk),
(9.18)
which is easily computed using the fact that Q(τ > tk) = exp(−
 tk
0 γ Q(s) ds). The
expected discounted value of the default payment leg equals
V def(γ Q) = EQ

exp

−
 τ
0
r(u) du

δI{τ<tN}

.
Since τ has density fτ(t) = γ Q(t) exp(−
 t
0 γ Q(u) du), deﬁning R(u) := r(u) +
γ Q(u), we get
V def(γ Q) = δ
 tN
0
exp

−
 t
0
r(s) ds

fτ(t) dt
= δ
 tN
0
γ Q(t) exp

−
 t
0
R(s) ds

dt.
(9.19)
According to market convention there are no payments when two parties enter into
a CDS agreement. This implies that the fair CDS spread x∗has to be chosen such
that the value of the contract at t = 0 is equal to zero. Hence x∗is deﬁned by the
relation V prem(x∗; γ Q) = V def(γ Q), which is easily solved for x∗. Obviously, x∗
depends on the intensity function γ Q, as V prem and V def depend on γ Q. Note that in
our pricing argument we have neglected the possibility of default for the protection
seller. More sophisticated CDS-pricing approaches would take this possibility into
account (see Notes and Comments).
Assume now that we observe spreads quoted in the market for one or more CDSs
on the same reference entity. Under the martingale-modelling approach we have to
calibrate our model to the available market information. In the context of our simple
default model we hence have to determine the implied risk-neutral hazard rate γ Q,
--- page 427 ---

9.3. Financial and Actuarial Pricing
411
which ensures that the fair CDS spreads implied by the model equal the spreads
which are quoted in the market.
We consider the following simple example: market information consists of the fair
spread x∗of one CDS with maturity tN; the risk-neutral hazard rate γ Q is constant,
i.e. γ Q(t) = ¯γ Q for some ¯γ Q > 0. In this context, by (9.18) and (9.19), the implied
risk-neutral hazard rate ¯γ Q satisﬁes the equation
x∗
N

k=1
p0(0, tk)(tk −tk−1)e−¯γ Qtk = δ ¯γ Q
 tN
0
p0(0, t)e−¯γ Qt dt.
(9.20)
Now, the left-hand side of this equation (the value of the premium payments) is
decreasing in ¯γ Q, whereas the right-hand side (the value of the default payments) is
increasing in ¯γ Q. Therefore, in this example there is a unique implied risk-neutral
hazard rate, which is easily computed numerically.
If we observe spreads for several CDSs on the same reference entity but with
different maturities, a time-independent risk-neutral hazard rate is generally not
sufﬁcient to calibrate the model to the observed swap spreads. Instead one typically
uses hazard-rate functions γ Q(t) that are piecewise constant or piecewise linear.An
exception occurs in the special case where the spread curve is ﬂat (i.e. all CDSs on
the reference entity have the same spread x∗, independent of the maturity), where
the risk-free interest rate is constant and where the time points tk are equally spaced
(i.e. tk −tk−1 = t for all t). In that case the implied risk-neutral hazard rate ¯γ Q is
given as the solution to the following equation (equation (9.20) for the case N = 1):
x∗tp0(0, t)e−¯γ Qt = δ ¯γ Q
 t
0
p0(0, t) exp(−¯γ Qt) dt.
(9.21)
For t relatively small (quarterly or semiannual spread payments) a good approximation to the solution of (9.21) is given by ¯γ Q ≈x∗/δ, i.e. by the ratio of the fair
swap spread and the percentage loss given default. This approximation is frequently
used in practice.
Remark 9.19. Recall that in reduced-form models historical default information
is of no use in determining the form of the risk-neutral hazard rate. For our simple
example it follows that the hypothesis of a constant risk-neutral hazard rate cannot
be tested by looking at historical default patterns: it is perfectly possible that under
the historical measure P default intensities are time dependent, but that under a
risk-neutral measure Q they are constant, and vice versa. The only way of testing
the assumption that γ Q(t) is a constant or has any other functional form would be to
test the implications of this assumption on the dynamics of observable CDS spreads
or prices of other traded credit-risky securities.
9.3.4
The Actuarial Approach to Credit Risk Pricing
The actuarial approach is mainly used for the pricing of loans and related products,
which are relatively illiquid. Under the actuarial approach the total spread a loan
should earn (the difference between the interest rate which should be charged for
--- page 428 ---

412
9. Dynamic Credit Risk Models
the loan and the interest rate on a default-free bond with similar characteristics) is
computed according to the following schematic formula:
total spread = administrative cost + expected loss + risk premium.
(9.22)
Administrative cost is of no concern to us here. Expected loss refers to expected
loss under the physical probability measure and, assuming independence between
default and recovery rates, it is given by the product of the annual default probability
and the expected percentage loss given default. The determination of an appropriate
risk premium is more involved from a methodological viewpoint and is discussed
below. Formula (9.22) for the total spread has the same structure as the standard
actuarial premium principles, hence the name actuarial approach to pricing credit
risk. Of course, in practice a formal loan-pricing rule of the form (9.22) is not applied
rigorously across the board; other factors, such as competitive pressure from other
lenders or a long-standing business relationship between borrower and lender, play
an important role in determining the yield spread for a loan.
Risk premiums and economic capital.
In modern loan-pricing systems the risk
premium of a loan is computed by applying a target interest rate or hurdle rate to the
economic capital required as buffer against losses from the deal. Hurdle rates are set
by management; they reﬂect the return on equity aspired to by a ﬁnancial institution.
Under a modern economic capital framework, the economic capital required for a
particular loan is determined in two steps. First, the economic capital of the entire
credit portfolio is determined. Here the ﬁnancial industry typically distinguishes
between the so-called expected loss, given by the expected value E(L), and the socalled unexpected loss, given by UL := L −E(L). Usually, the economic capital
for the entire loan portfolio is determined by applying a risk measure such as VaR
or expected shortfall to UL, whereas the expected loss is charged directly to the
borrower according to the general actuarial loan-pricing formula (9.22).
In a second step the total economic capital needs to be allocated to the individual
loans in the portfolio, a process called economic capital allocation. A fair economic
capital allocation has to reﬂect the contributions of the individual loans to the total
risk of the portfolio. For instance, a large loan, which is (almost) independent of the
overall portfolio, might contribute less to total risk than a smaller loan, which is likely
to default in circumstances where the portfolio produces large losses. Formally,
economic capital allocation is done using a capital allocation principle such as
standard deviation contributions or expected shortfall contributions (see Section 6.3
for details).
Financial and actuarial pricing compared.
We conclude this section with a brief
comparison of the two pricing methodologies. The ﬁnancial-pricing approach is a
relative pricing theory, which explains prices of credit products in terms of observable prices of other securities. If properly applied, it leads to arbitrage-free prices of
credit-risky securities, which are consistent with prices quoted in the market. These
features make the ﬁnancial-pricing approach the method of choice in an environment
where credit risk is actively traded and, in particular, for valuing credit instruments
--- page 429 ---

9.3. Financial and Actuarial Pricing
413
when the market for related products is relatively liquid. On the other hand, since
ﬁnancial-pricing models have to be calibrated to prices of traded credit instruments,
they are difﬁcult to apply when we lack sufﬁcient market information. Moreover, in
such cases prices quoted using an ad hoc choice of some risk-neutral measure are
more or less “plucked out of thin air”.
The actuarial pricing approach is an absolute pricing approach, based on the
paradigm of risk bearing: a credit product such as a loan is taken on the balance
sheet if the spread earned on the loan is deemed by the lender to be a sufﬁcient
compensation for the risk contribution of the loan to the total risk of the lending
portfolio. Moreover, the approach relies mainly on historical default information.
Therefore, the actuarial approach is well suited to situations where the market for
related credit instruments is relatively illiquid, such that little or no price information
is available; loans to medium or small businesses are a prime case in point. On the
other hand, the approach does not necessarily lead to prices that are consistent (in
the sense of absence of arbitrage) across products or that are compatible with quoted
market prices for credit instruments, so it is less suitable for a trading environment.
As markets for credit products become more and more liquid, the ﬁnancialvaluation paradigm is gaining in importance. This transition poses a challenge for
risk management in ﬁnancial institutions, since it may well be that a particular
credit risk is priced differently by different parts of an institution, such as the loan
department and a trading desk for credit derivatives. It is the task of a sound riskmanagement process to ensure that these inconsistencies are kept to a minimum; a
profound understanding of the differences between ﬁnancial and actuarial valuation
is an important prerequisite for that.
Notes and Comments
Theoretical results on the relationship between physical and risk-neutral default
probabilities were obtained by Artzner and Delbaen (1995), Jarrow, Lando and Yu
(2005), Giesecke and Goldberg (2005) and others. General mathematical results
for the behaviour of point processes (such as default indicators) under a change
of measure (Girsanov-type theorems) can be found in Br´emaud (1981) or Jacod
and Shiryaev (1987). Empirical studies on the relationship between actual and riskneutral default probabilities include Fons (1994), Bohn (2000), Driessen (2005),
Huang and Huang (2003) and Berndt et al. (2004). In their paper, Berndt et al. go
beyond the regression analysis presented in our text and estimate a full time series
model for the joint evolution of risk-neutral and actual default intensities.
The fundamental theorems of asset pricing are discussed in most textbooks on
mathematical ﬁnance (see, for example, Bingham and Kiesel 1998; Dufﬁe 2001;
Shreve 2004). In recent years a number of interesting approaches to the risk management of derivative securities in incomplete markets have been developed. Quadratic
hedging approaches were ﬁrst developed by F¨ollmer and Sondermann (1986) and
F¨ollmer and Schweizer (1991); Schweizer (2001b) is an excellent survey. The theory of superhedging is developed in El Karoui and Quenez (1995) and Kramkov
(1996); the related idea of quantile hedging is explored in F¨ollmer and Leukert
--- page 430 ---

414
9. Dynamic Credit Risk Models
(1999). Utility-based approaches to pricing and hedging in incomplete markets are
discussed in Delbaen et al. (2002) and Becherer (2004); the latter paper explicitly
considers applications of utility-based hedging strategies to credit risk models. A
discussion of incomplete-market models in discrete time can be found in F¨ollmer
and Schied (2004). Early papers dealing with market incompleteness in credit risk
models include Becherer (2004), Becherer and Schweizer (2005) and Bielecki, Jeanblanc and Rutkowski (2004).
The term martingale modelling was coined by Bj¨ork (1998) in the context of
default-free short-rate models (see also Baxter and Rennie 1996). The pricing of
CDSsisdiscussedinmoststandardtextbooksoncreditriskmodels(see,forexample,
Bielecki and Rutkowski 2002; Bluhm, Overbeck and Wagner 2002; Dufﬁe and
Singleton 2003; Lando 2004; Sch¨onbucher 2003). For results on CDS pricing with
possible default of protection seller see, for example, Hull and White (2001).
The relationship between actuarial and ﬁnancial-pricing approaches is discussed
byJensenandNielsen(1996),Embrechts(2000),Schweizer(2001a)andEmbrechts,
Frey and Furrer (2001), among others.
9.4
Pricing with Doubly Stochastic Default Times
The main result of this section concerns the pricing of two types of contingent
claims that can be used as building blocks for constructing the pay-off of many
important credit-risky securities. We will show that, for a default time which is
doubly stochastic, the computation of prices for these claims can be reduced to a
pricing problem for a corresponding default-free claim if we adjust the interest rate
and replace the default-free interest rate rt by the sum Rt = rt + γt of the defaultfree interest rate and the hazard rate of the default time.
9.4.1
Recovery Payments of Corporate Bonds
To clarify the form of our building blocks we brieﬂy survey different models for the
recovery of corporate zero-coupon bonds. As in previous sections, we denote the
price at time t of a corporate zero-coupon bond with maturity T ⩾t by p1(t, T );
p0(t, T ) denotes the price of the corresponding default-free zero-coupon bond. The
face value of these bonds is always taken to be one. The following three recovery
models are frequently used in the literature.
Recovery of Treasury (RT).
The RT model was proposed by Jarrow and Turnbull (1995). Under RT, if default occurs at some point in time τ
⩽T , the
owner of the defaulted bond receives (1 −δτ) units of the default-free zerocoupon bond p0(· , T ) at time τ, where the rv δτ models the loss given default.
At maturity T the holder of the defaultable bond therefore receives the payment
p1(T, T ) = I{τ>T } + (1 −δτ)I{τ⩽T }. In particular, if δτ = δ for some constant
δ ∈(0, 1), we get p1(T, T ) = (1 −δ) + δI{τ>T }, so the price of the corporate bond
at time t < T equals the sum of (1 −δ)p0(t, T ) and δ times the price of the
claim I{τ>T }.
--- page 431 ---

9.4. Pricing with Doubly Stochastic Default Times
415
RecoveryofFaceValue(RF).
UnderRF,ifdefaultoccursatτ ⩽T ,theholderofthe
bond receives a (possibly random) recovery payment of size (1 −δτ) immediately
at the default time τ. The value at maturity T is therefore given by
p1(T, T ) = I{τ>T } + 1 −δτ
p0(τ, T )I{τ⩽T }.
Even with deterministic loss given default δτ ≡δ and deterministic interest rates,
the value at maturity of the recovery payment is random as it depends on the exact
timing of default. This makes the pricing of recovery payments under RF more
difﬁcult than under RT.
RecoveryofMarketValue(RM).
Thisrecoveryassumptionhasbeenputforwardby
Dufﬁe and Singleton (1999a); its main virtue is the fact that it leads to particularly
simple pricing formulas for corporate bonds. Under RM it is assumed that the
recovery payment at the default-time τ ⩽T is given by a fraction (1 −δτ) of the predefault value of the bond. Obviously, this is a recursive deﬁnition, as the pre-default
value depends on the recovery payment. Nonetheless, under some assumptions it is
possible to obtain a unique price for corporate bonds, where recovery is modelled
using the RM assumption (see Proposition 9.24 below).
In real markets recovery is a complex issue with many legal and institutional
features, and all three recovery models are at best a crude approximation of reality.
The RF-assumption comes closest to legal practice, as debt with the same seniority
is assigned the same (fractional) recovery, independent of the maturity. On the other
hand, for “extreme” parameter values (long maturities and high risk-free interest
rate), RF may lead to negative credit spreads, as we will see in Section 9.5.3 below.
Moreover, the RF model leads to slightly more involved pricing formulas for corporate bonds than the RM and RT models. Empirical evidence on recovery rates for
loans and corporate bonds is discussed in Section 8.4.6.
9.4.2
The Model
We consider a ﬁrm whose default time is given by a doubly stochastic random time
as in Section 9.2.3. The economic background ﬁltration represents the information
generated by an arbitrage-free and complete model for non-defaultable security
prices.Moreprecisely,let(Ω, F , (Ft), Q)denoteaﬁlteredprobabilityspace,where
Q is already the equivalent martingale measure. Prices of default-free securities such
as default-free bonds are (Ft)-adapted processes. By (rt) we denote the default-free
rate of interest; Bt = exp(
 t
0 rs ds) models the default-free savings account.
Let τ be the default time of some company under consideration and let Yt = I{τ⩽t}
be the associated default indicator process. As in Section 9.2.2 we set Ht = σ({Ys :
s ⩽t}) and Gt = Ft ∨Ht; we assume that default is observable and that investors
have access to the information contained in the background ﬁltration (Ft), so that
the information available to investors at time t is given by Gt. We consider a market
for credit products which is liquid enough that we may use the martingale-modelling
approach, and we use Q as the pricing measure for defaultable securities. Finally,
we assume that, under Q, the default time τ is a doubly stochastic random time with
--- page 432 ---

416
9. Dynamic Credit Risk Models
background ﬁltration (Ft) and hazard-rate process (γt). This latter assumption is
crucial for the results that follow.
9.4.3
Pricing Formulas
Deﬁnition 9.20. We introduce the following building blocks.
(i) A vulnerable claim, i.e. an FT -measurable promised payment X which is
made at time T if there is no default; the actual payment of the vulnerable
claim equals XI{τ>T }.
(ii) A recovery payment at the time of default of the form ZτI{τ⩽T }, where
Z = (Zt)t⩾0 is an (Ft)-adapted stochastic process and where Zτ is short
for Zτ(ω)(ω). T is the maturity of the recovery payment.
Example 9.21 (corporate bonds). The actual payments of a corporate zero-coupon
bond can be represented as a combination of a vulnerable claim and a recovery
payment. Suppose that the loss given default is given by some (Ft)-adapted process
(δt) with values in (0, 1). Under the RT hypothesis the actual payments are given by
the vulnerable claim I{τ>T } and the recovery payment (1 −δτ)p0(τ, T )I{τ⩽T }. In
the case where δτ = δ for some δ ∈(0, 1), the pay-off at maturity simpliﬁes further
to the sum of the deterministic payment (1 −δ) and the vulnerable claim δI{τ>T }.
Under RF the actual payment of the bond consists of the vulnerable claim I{τ>T }
and the recovery payment (1 −δτ)I{τ⩽T }. Obviously, since coupon-paying corporate bonds can be represented as a portfolio of zero-coupon bonds issued by a
corporation, coupon-paying bonds can also be constructed from building blocks (i)
and (ii). However, see Remark 9.25 for a word of warning on the validity of linear
pricing rules in reduced-form models.
Example 9.22 (vulnerable option). Consider a call option with exercise price K
and maturity T on some default-free security (St), and assume that the writer of the
option may default. Assume that in case of default of the writer at time τ < T the
owner of the option receives a fraction (1 −δτ) of the intrinsic value of the option at
the time of default. This can be modelled as a combination of the vulnerable claim
(ST −K)+I{τ>T } and the recovery payment (1 −δτ)(Sτ −K)+I{τ⩽T }.
Credit default swaps can also be viewed as a combination of vulnerable claims
and a recovery payment (see Section 9.4.4 below).
According to (9.17), we obtain the following formula for the price at time t of an
arbitrary, non-negative, GT -measurable contingent claim H:
Ht = EQ

exp

−
 T
t
rs ds

H
				 Gt

.
(9.23)
Consider a default-free claim with FT -measurable pay-off X. Since τ is a doubly
stochastic random time, the additional information about the default history contained in (Gt) is of no use in computing the conditional expectation (9.23), and we
have
EQ

exp

−
 T
t
rs ds

X
				 Gt

= EQ

exp

−
 T
t
rs ds

X
				 Ft

.
(9.24)
--- page 433 ---

9.4. Pricing with Doubly Stochastic Default Times
417
A formal proof of this equality can be based on the representation of τ obtained
in Lemma 9.13; we omit the details. Relation (9.24) shows that we may write the
price of a non-negative default-free claim X as Xt = EQ(exp(−
 T
t rs ds)X | Ft),
which is obviously an (Ft)-adapted process. In particular, it does not matter if we
model default-free security prices using (Ft) or the larger ﬁltration (Gt). In the
following theorem we show that, in a similar vein, the pricing of the building blocks
introduced in Deﬁnition 9.20 can be reduced to a pricing problem in a default-free
security market model with adjusted default-free interest rate.
Theorem 9.23. Suppose that, under Q, τ is doubly stochastic with background
ﬁltration (Ft) and hazard-rate process (γt). Deﬁne Rs := rs + γs. Assume that the
rvs exp(−
 T
t rs ds)|X| and
 T
t |Zsγs| exp(−
 s
t Ru du) ds are all integrable with
respect to Q. Then the following identities hold:
EQ

exp

−
 T
t
rs ds

I{τ>T }X
				 Gt

= I{τ>t}EQ

exp

−
 T
t
Rs ds

X
				 Ft

,
(9.25)
EQ

I{τ>t} exp

−
 τ
t
rs ds

ZτI{τ⩽T }
				 Gt

= I{τ>t}EQ
  T
t
Zsγs exp

−
 s
t
Ru du

ds
				 Ft

. (9.26)
Proof. The integrability conditions ensure that all conditional expectations are well
deﬁned. We start with the pricing formula (9.25) for the vulnerable claim. Deﬁne the
FT -measurable rv ˜X := exp(−
 T
t rs ds)X. We obtain, using Corollary 9.10 with
s = T and Γt =
 t
0 γs ds, that
EQ( ˜XI{τ>T } | Gt) = I{τ>t}EQ(exp(−(ΓT −Γt)) ˜X | Ft).
Using the relation ΓT −Γt =
 T
t γs ds and the deﬁnition of ˜X, we immediately
obtain that the right-hand side equals I{τ>t}EQ(exp(−
 T
t Rs ds)X | Ft). Next we
turn to (9.26). We obtain from Lemma 9.9 that
EQ

I{τ>t} exp

−
 τ
t
rs ds

ZτI{τ⩽T }
				 Gt

= I{τ>t}
EQ(I{τ>t} exp(−
 τ
t rs ds)ZτI{τ⩽T } | Ft)
P(τ > t | Ft)
.
(9.27)
Now note that
P(τ ⩽t | FT ) = 1 −exp

−
 t
0
γs ds

,
--- page 434 ---

418
9. Dynamic Credit Risk Models
so the conditional density of τ given FT equals fτ|FT (t) = γt exp(−
 t
0 γs ds).
Hence
EQ

I{τ>t} exp

−
 τ
t
rs ds

ZτI{τ⩽T }
				 FT

=
 T
t
exp

−
 s
t
ru du

Zsγs exp

−
 s
0
γu du

ds
= exp

−
 t
0
γu du
  T
t
Zsγs exp

−
 s
t
Ru du

ds.
Hence we obtain, using iterated conditional expectations, that
EQ

I{τ>t} exp

−
 τ
t
rs ds

ZτI{τ⩽T }
				 Ft

= exp

−
 t
0
γu du

EQ
 T
t
Zsγs exp

−
 s
t
Ru du

ds
				 Ft

;
the identity (9.26) follows because of (9.27).
9.4.4
Applications
Credit default swaps.
We extend our analysis of Section 9.3.3 and discuss the
pricing of CDSs in the model introduced in Section 9.4.2. This allows us to incorporate stochastic interest rates, recovery rates and hazard rates into our analysis.
As in our previous analysis, the premium payments are due at N points in time
0 < t1 < · · · < tN; at a pre-default date tk, the protection buyer pays a premium of
size x(tk −tk−1), where x denotes the swap spread in percentage points (again we
take the nominal of the swap to be one). Moreover, if τ ⩽tN, there is an accrued
premium payment of size x(τ −tk−1), provided that tk−1 < τ ⩽tk. If τ ⩽tN, the
protection seller makes the default payment of size δτ to the buyer at the default
time τ, where the percentage loss given default is now a general (Ft)-adapted process. Using Theorem 9.23, both legs of the swap can be priced. The regular premium
payments constitute a sequence of vulnerable claims. Using (9.25), we obtain, for
the fair price in t = 0,
V prem,1 =
N

k=1
EQ

exp

−
 tk
0
ru du

x(tk −tk−1)I{tk<τ}

= x
N

k=1
(tk −tk−1)EQ

exp

−
 tk
0
Ru du

.
The accrued premium payments constitute a recovery payment, where Z is given
by Zs = x N
k=1(s −tk−1)I{tk−1<s⩽tk}; by (9.26) the fair price in t = 0 is given by
V prem,2 = x
N

k=1
EQ
  tk
tk−1
(s −tk−1)γs exp

−
 s
0
Ru du

ds

.
The default payments also form a recovery payment, this time with Zs = δs and
maturity tN, so their value is given by V def = EQ(
 tN
0
δsγs exp(−
 s
0 Ru du) ds).
--- page 435 ---

9.4. Pricing with Doubly Stochastic Default Times
419
Hence we have reduced the pricing of credit default swaps to a pricing problem in
the default-free world. Methods for solving this problem will be discussed in the
next section.
Recovery of market value.
Next we turn to the pricing of credit-risky securities whose recovery payment is described by the RM assumption introduced in
Section 9.4.1. More precisely, we consider a claim whose pay-off consists of the
vulnerable claim X and a recovery-payment of size (1 −δτ)VτI{τ⩽T }, where the
(Ft)-adapted process (δt) ∈(0, 1) gives the percentage loss given default of the
claim and where the (Ft)-adapted process (Vt) gives the pre-default value of the
claim. Note that this is a recursive deﬁnition, as the pre-default value at time t also
depends on the form of the future recovery payments in the time-period (t, T ].
Nonetheless, we have the following result.
Proposition 9.24. Suppose that, under Q, τ is doubly stochastic with hazard-rate
process (γt), that X is integrable, and that the RM assumption holds. Then the
pre-default value process (Vt) is uniquely determined and is given by
Vt = EQ

exp

−
 T
t
rs + δsγs ds

X
				 Ft

,
0 ⩽t ⩽T.
(9.28)
Note that for δt ≡1 the claim is a standard vulnerable claim; in that case,
(9.28) reduces to the formula (9.25). On the other hand, for δt ≡0 the claim is
essentially default free; in that case, (9.28) reduces to the standard pricing formula
for the claim X in a default-free security market model. For a formal proof of
Proposition 9.24 we refer to the references given in Notes and Comments.
Credit spreads and hazard rates.
With doubly stochastic default times the riskneutral hazard-rate process (γt) and the credit spread
c(t, T ) = −
1
T −t (ln p1(t, T ) −ln p0(t, T ))
of defaultable bonds are closely related. Analytic results are most easily derived for
the instantaneous credit spread given by
c(t, t) = lim
T →t c(t, T ) = −∂
∂T

T =t
(ln p1(t, T ) −ln p0(t, T )).
(9.29)
Assume that τ > t, so that p1(t, t) = p0(t, t) = 1. Hence we get
∂
∂T

T =t
ln p1(t, T ) = ∂
∂T

T =t
p1(t, T ),
(9.30)
and similarly for p0(t, T ). To compute the derivative in (9.30) we need to distinguish
between the different recovery models. Under RM, we have, from Proposition 9.24,
exchanging expectation and differentiation,
−∂
∂T

T =t
p1(t, T ) = −EQ
 ∂
∂T

T =t
exp

−
 T
t
rs + δsγs ds
 				 Ft

= rt + δtγt.
(9.31)
--- page 436 ---

420
9. Dynamic Credit Risk Models
Applying (9.31) with δt ≡0 yields
−∂
∂T

T =t
p0(t, T ) = rt,
so that c(t, t) = δtγt, i.e. the instantaneous credit spread equals the product of hazard
rate and percentage loss given default, which is quite intuitive from an economic
point of view. Under RF, p1(t, T ) is given by the sum of the price of the vulnerable
claim I{τ>T } and the recovery payment (1 −δ)τ. Relation (9.31) with δt ≡0 shows
that the derivative with respect to T of the vulnerable claim at T = t is equal to
−(rt + γt). For the recovery payment we get
∂
∂T

T =t
E
  T
t
γs(1 −δs) exp

−
 s
t
Ru du

ds
				 Ft

= (1 −δt)γt.
Hence
−∂
∂T

T =t
p1(t, T ) = rt + γt −(1 −δt)γt = rt + δtγt,
so that c1(t, t) is again equal to δtγt. An analogous computation shows that we also
have c1(t, t) = δtγt under RT. However, for T −t > 0 the credit spread corresponding to the different recovery models differs, as is illustrated in Section 9.5.3
below.
Remark 9.25 (limitations of reduced-form models). The analogy with defaultfree term structure models makes the reduced-form models with doubly stochastic
default times relatively easy to apply. However, in interpreting the results some care
is required. In particular, one must bear in mind that in these models the default
intensity does not explicitly take into account the structure of a ﬁrm’s outstanding
risky debt. This can lead to nonsensical results, as is illustrated in the following
simple example. Consider a ﬁrm whose risky debt consists of a single bond with
maturity ¯T . Suppose that the ﬁrm raises new funds by issuing another zero-coupon
bond with maturity T < ¯T . In order to value this new debt, in a naive application of
the reduced-form approach, one would set up a model with doubly stochastic default
time τ and calibrate the risk-neutral hazard rate to the price of the existing debt (the
bond with maturity ¯T ). This model would then be used to price the zero-coupon
bond with the short maturity. If the face value of the new debt is large relative to the
value of the ﬁrm, the price obtained in this way is out of line with economic reality.
As an extreme case, suppose that the ﬁrm uses the funds raised by the bond issue to
buy back a some of its own shares. Clearly, this makes the ﬁrm riskier and raises the
probability that the ﬁrm defaults on the new issue. This should be reﬂected in the
default intensity and, in fact, since T < ¯T , in the price of the existing debt. More
generally, these considerations show that the validity of the linear pricing rules for
corporate debt implied by the reduced-form approach must be interpreted with care.
A formal analysis of these issues is best carried out in ﬁrm-value models, where
the default is explicitly modelled in terms of fundamental economic quantities. An
excellent discussion can be found in Chapter 2 of Lando (2004).
--- page 437 ---

9.5. Afﬁne Models
421
Notes and Comments
The results of this section, and in particular Theorem 9.23, are originally due to
Lando (1998); related results were obtained by Jarrow and Turnbull (1995) and
Jarrow, Lando and Turnbull (1997). An alternative treatment at the textbook level
(including a more detailed discussion of the RM recovery model) is given in Chapter 5 of Lando (2004). Proposition 9.24 is due to Dufﬁe and Singleton (1999a);
extensions are discussed in Becherer and Schweizer (2005). For a generalization of
Theorem 9.23 to reduced-form models where the default time is not doubly stochastic we refer to Dufﬁe, Schroder and Skiadas (1996) and Collin-Dufresne, Goldstein
and Hugonnier (2004).
9.5
Afﬁne Models
In order to apply the pricing formulas for doubly stochastic random times obtained
in Theorem 9.23 we need effective ways to evaluate the conditional expectations on
the right-hand side of equations (9.25) and (9.26). In most models, where default is
modelled by a doubly stochastic random time, (rt) and (γt) are modelled as functions
of some p-dimensional Markovian state variable process (Ψt) with state space given
by the domain D ⊂Rp, so that Rt := rt + γt is of the form Rt = R(Ψt) for some
function R : D ⊆Rp →R+, and thus the natural background ﬁltration is given by
(Ft) = σ({Ψs : s ⩽t}). We hence have to compute conditional expectations of the
form E(exp(−
 T
t R(Ψs) ds)g(ΨT ) | Ft) for generic g : D ⊂Rp →R+. Since
(Ψt) is a Markov process, this conditional expectation is given by some function
f (t, Ψt) of time and current value Ψt of the state variable process. It is well known
that the function f can be characterized in terms of a parabolic PDE—this is the
celebrated Feynman–Kac formula.
This yields an approach to determine f using analytical or numerical techniques
for PDEs. In particular, it is known that in the case where (Ψt) belongs to the
class of afﬁne jump diffusions (see below), where R is an afﬁne function and where
g(ψ) = exp(u′ψ) for some u ∈Rp, the function f is of the form
f (t, ψ) = exp(α(t, T ) + β(t, T )′ψ)
(9.32)
for deterministic functions α : [0, T ] →R and β : [0, T ] →Rp; moreover, α and
β are determined by a (p + 1)-dimensional ordinary differential equation (ODE)
system that is easily solved numerically. A relationship of the form (9.32) is often
termed an afﬁne term structure, as it implies that continuously compounded yields
of bonds at time t are afﬁne functions of Ψt. Because of the ease of implementation,
most reduced-form models used in practice work with afﬁne jump diffusions as state
variable process.
In this section we discuss these results. We concentrate on the case where the state
variable process is given by a one-dimensional diffusion; extensions to processes
with jumps will be considered brieﬂy at the end.
--- page 438 ---

422
9. Dynamic Credit Risk Models
9.5.1
Basic Results
The PDE characterization of f .
We assume that the state variable process (Ψt) is
the unique solution of the SDE
dΨt = µ(Ψt) dt + σ(Ψt) dWt,
Ψ0 = ψ ∈D,
(9.33)
with state space given by the domain D ⊆R. Here (Wt) is a standard, onedimensional Brownian motion on some ﬁltered probability space (Ω, F , P, (Ft)),
and µ and σ are continuous functions from D to R, respectively R+. Consider functions R, g : D →R+. Since (Ψt) is Markovian, given the present value Ψt, the
future evolution (Ψs)s⩾t of the state variable process is independent of Ft, and we
obtain
E

exp

−
 T
t
R(Ψs) ds

g(ΨT )
				 Ft

= f (t, Ψt)
(9.34)
for some function f : [0, T ]×D →R+. The next lemma gives the characterization
of f in terms of a parabolic PDE announced above.
Lemma 9.26 (Feynman–Kac). If f is once continuously differentiable in t and
twice continuously differentiable in ψ, it solves the terminal-value problem
ft + µ(ψ)fψ + 1
2σ 2(ψ)fψψ = R(ψ)f,
(t, ψ) ∈[0, T ) × D,
f (T, ψ) = g(ψ),
ψ ∈D,
'
(9.35)
where lower indices denote partial derivatives. Conversely, suppose that the function
g is bounded, that R(ψ) ⩾0 for all ψ ∈D, and that ˜f : [0, T ] × D →R+ is a
bounded solution of the terminal value problem (9.35). Let (Ψt) be a solution of the
SDE (9.33). Then E(exp(−
 T
t R(Ψs) ds)g(ΨT ) | Ft) = ˜f (t, Ψt).
The Feynman–Kac formula is a standard result of stochastic calculus and it is
discussed in many textbooks on stochastic processes and ﬁnancial mathematics, so
we omit the proof (references are given in Notes and Comments).
Afﬁne term structure.
The following assumption ensures that the solution of the
PDE (9.35), with terminal condition g(ψ) = exp(uψ), uψ ⩽0 for ψ ∈D, is of
the form (9.32), so that we have an afﬁne term structure. Note that g ≡1 for u = 0;
this is the appropriate terminal condition for pricing zero-coupon bonds.
Assumption 9.27. R, µ and σ 2 are afﬁne functions of ψ, i.e. there are constants
ρ0, ρ1, k0, k1, h0 and h1 such that R(ψ) = ρ0 + ρ1ψ, µ(ψ) = k0 + k1ψ and
σ 2(ψ) = h0 + h1ψ. Moreover, for all ψ ∈D we have h0 + h1ψ ⩾0 and
ρ0 + ρ1ψ ⩾0.
Fix some T > 0. We try to ﬁnd a solution of (9.35) of the form ˜f (t, ψ) =
exp(α(t, T ) + β(t, T )ψ) for continuously differentiable functions α(· , T ) and
β(· , T ). As ˜f (T, ψ) = exp(uψ), we immediately obtain the terminal condition
α(T, T ) = 0, β(T, T ) = u. Denote by α′(· , T ) and β′(· , T ) the derivative of α and
β with respect to t. Using the special form of ˜f we obtain that
˜ft = (α′ + β′ψ) ˜f ,
˜fψ = β ˜f
and
˜fψψ = β2 ˜f .
