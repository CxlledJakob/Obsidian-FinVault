# Quantitative Risk Management_ Concepts, Techniques, and -- Alexander J_ McNeil, Rüdiger Frey, Paul Embrechts -- Princeton series in finance, -- isbn13 9780691122557 -- 478a0059673fecd0c76229cd3d8884e7 -- Anna’s Arc.pdf — pages 343–362

--- page 343 ---

8
Credit Risk Management
Credit risk is the risk that the value of a portfolio changes due to unexpected changes
in the credit quality of issuers or trading partners. This subsumes both losses due to
defaults and losses caused by changes in credit quality, such as the downgrading of
a counterparty in an internal or external rating system. Credit risk is omnipresent
in the portfolio of a typical ﬁnancial institution. To begin with, the lending and corporate bond portfolios are obviously affected by credit risk. Perhaps less obviously,
credit risk accompanies any OTC (over-the-counter, i.e. non-exchange-guaranteed)
derivative transaction such as a swap, because the default of one of the parties
involved may substantially affect the actual pay-off of the transaction. Moreover,
in recent years a specialized market for credit derivatives has emerged in which
ﬁnancial institutions are active players (see Section 9.1 for details).
This brief list should convince the reader that credit risk is a highly relevant risk
category indeed, as it relates to the core activities of most banks. Credit risk is also
at the heart of many recent developments on the regulatory side, such as the new
Basel II Capital Accord discussed in Chapter 1. We devote two chapters to this
important risk category. In the present chapter we focus on static models and credit
risk management; dynamic models and credit derivatives are discussed in Chapter 9.
8.1
Introduction to Credit Risk Modelling
In this section we provide a brief overview of the various model types that are used
in credit risk before discussing some of the main challenges that are encountered in
credit risk management.
8.1.1
Credit Risk Models
The development of the market for credit derivatives and the Basel II process has
generated a lot of interest in quantitative credit risk models in industry, academia and
among regulators, so that credit risk modelling is at present a very active subﬁeld of
quantitative ﬁnance and risk management. In this context it is interesting that parts
of the new minimum capital requirements for credit risk are closely linked to the
structure of existing credit portfolio models, as will be explained in more detail in
Section 8.4.5.
There are two main areas of application for quantitative credit risk models: credit
risk management and the analysis of credit-risky securities. Credit risk management
models are used to determine the loss distribution of a loan or bond portfolio over
--- page 344 ---

328
8. Credit Risk Management
a ﬁxed time period (typically at least one year), and to compute loss-distributionbased risk measures or to make risk-capital allocations of the kind discussed in
Section 6.3. Hence these models are typically static, meaning that the focus is on the
loss distribution for the ﬁxed time period rather than a stochastic process describing
the evolution of risk in time.
For the analysis of credit-risky securities, on the other hand, dynamic models
(generally in continuous time) are needed, because the pay-off of most products
depends on the exact timing of default. Moreover, in building a pricing model one
often works directly under an equivalent martingale or risk-neutral probability measure (as opposed to the real-world probability measure). Issues related to dynamic
credit risk models and risk-neutral and real-world measures will be studied in detail
in Chapter 9.
Depending on their formulation, credit risk models can be divided into structural
or ﬁrm-value models on the one hand and reduced-form models on the other; this
division cuts across that of dynamic and static models. The progenitor of all ﬁrmvalue models is the model of Merton (1974), which postulates a mechanism for the
default of a ﬁrm in terms of the relationship between its assets and the liabilities
that it faces at the end of a given time period. More generally, in ﬁrm-value models
default occurs whenever a stochastic variable (or in dynamic models a stochastic
process) generally representing an asset value falls below a threshold representing
liabilities. For this reason static structural models are referred to in this book as
threshold models, particularly when applied at portfolio level. The general structural
model approach is discussed in Section 8.2 (where the emphasis is on modelling the
default of a single ﬁrm). In Section 8.3 we look at threshold models for portfolios;
in particular we show that copulas play an important role in understanding the
multivariate nature of these models.
In reduced-form models the precise mechanism leading to default is left unspeciﬁed. The default time of a ﬁrm is modelled as a non-negative rv, whose distribution
typically depends on economic covariables. The mixture models that we treat in
Section 8.4 can be thought of as static portfolio versions of reduced-form models.
More speciﬁcally, a mixture model assumes conditional independence of defaults
given common underlying stochastic factors.
It is important to realize that mixture models are not a new class of models;
on the contrary, the most useful static threshold models all have mixture model
representations, as will be shown in Section 8.4.4. In continuous time a similar
mapping between ﬁrm-value and reduced-form models is also possible if one makes
the realistic assumption that assets and/or liabilities are not perfectly observable (see
Notes and Comments).
From a practical point of view, mixture models represent perhaps the most useful way of analysing and comparing one-period portfolio credit risk models. For
these models, Monte Carlo techniques from the area of importance sampling can
be used to approximate risk measures for the portfolio loss distribution, and to calculate associated capital allocations, as will be shown in Section 8.5. Moreover, it
is possible to devise efﬁcient methods of statistical inference for portfolio models
--- page 345 ---

8.1. Introduction to Credit Risk Modelling
329
using historical default data. These models exploit the connection between mixture
models and the well-known class of generalized linear mixed models in statistics;
this is the topic of Section 8.6.
8.1.2
The Nature of the Challenge
Credit risk management poses certain speciﬁc challenges for quantitative modelling,
which are less relevant in the context of market risk.
Lack of public information and data.
Publicly available information regarding the
credit quality of corporations is typically scarce. This creates problems for corporate
lending, as the management of a ﬁrm is usually better informed about the true
economic prospects of the ﬁrm and hence about default risk than are prospective
lenders. The implications of this informational asymmetry are widely discussed
in the microeconomics literature (see Notes and Comments). The lack of publicly
available credit data is also a substantial obstacle to the use of statistical methods
in credit risk, a problem that is compounded by the fact that in credit risk the riskmanagement horizon is usually at least one year. It is fair to say that data problems
are the main obstacle to the reliable calibration of credit models.
Skewed loss distributions.
Typical credit loss distributions are strongly skewed
with a relatively heavy upper tail. Over the years a typical credit portfolio will
produce frequent small proﬁts accompanied by occasional large losses. A fairly
large amount of risk capital is therefore required to sustain such a portfolio: the
economic capital required for a loan portfolio (the risk capital deemed necessary
by shareholders and the board of directors of a ﬁnancial institution, independent
of the regulatory environment) is often equated to the 99.97% quantile of the loss
distribution (see Section 1.4.3).
The role of dependence modelling.
A major cause for concern in managing the
credit risk in a given loan or bond portfolio is the occurrence in a particular time
period of disproportionately many defaults of different counterparties. This risk is
directly linked to the dependence structure of the default events. In fact, default
dependence has a crucial impact on the upper tail of a credit loss distribution for a
large portfolio. This is illustrated in Figure 8.1, where we compare the loss distribution for a portfolio of 1000 ﬁrms that default independently (portfolio 1) with a
more realistic portfolio of the same size where defaults are dependent (portfolio 2).
In portfolio 2 defaults are weakly dependent, in the sense that the correlation between
default events (see Section 8.3.1) is approximately 0.5%. In both cases the default
probability is approximately 1% so that on average we expect 10 defaults. As will
be seen in Section 8.6, portfolio 2 can be viewed as a realistic model for the loss
distribution generated by a homogeneous portfolio of 1000 loans with a Standard
& Poor’s rating of BB. We clearly see from Figure 8.1 that the loss distribution of
portfolio 2 is skewed and that its right tail is substantially heavier than the right
tail of the loss distribution of portfolio 1, illustrating the drastic impact of default
dependence on credit loss distributions. Typically, more dependence is reﬂected in
the loss distribution by a shift of the mode to the left and a longer right tail. For this
--- page 346 ---

330
8. Credit Risk Management
Number of losses
Probability
0
0.06
0.10
0.12
20
40
60
0
50
30
10
0.08
0.04
0.02
Dependent defaults
Independent defaults
Figure 8.1.
Comparison of the loss distribution of two homogeneous portfolios of
1000 loans with a default probability of 1% and different dependence structure. In portfolio 1 defaults are assumed to be independent; in portfolio 2 we assume a default correlation
of 0.5%. Portfolio 2 can be considered as representative for BB-rated loans. We clearly see
that the default dependence generates a loss distribution with a heavier right tail.
reason we devote a large part of our exposition to the analysis of credit portfolio
models and dependent defaults.
There are sound economic reasons for expecting default dependence. To begin
with, the ﬁnancial health of a ﬁrm varies with randomly ﬂuctuating macroeconomic
factors, such as changes in economic growth. Since different ﬁrms are affected
by common macroeconomic factors, we have dependence between their defaults.
Moreover, default dependence is caused by direct economic links between ﬁrms,
such as a strong borrower–lender relationship. Given the enormous size of typical
loan portfolios it can be argued that, in credit risk management, direct business
relations play a less prominent role in explaining default dependence. Dependence
due to common factors, on the other hand, is of crucial importance and will be
a recurring theme in our analysis. In the pricing of portfolio credit derivatives, the
portfolios of interest are smaller, so modelling direct business relationships becomes
more relevant (see Section 9.8 for models of this kind).
Notes and Comments
Chapter 2 of Dufﬁe and Singleton (2003) contains a good discussion of the economic
principles of credit risk management, elaborating on some of the issues discussed
above. For a microeconomic analysis of the functioning of credit markets in the
presence of informational asymmetries between borrowers and lenders we refer to
the seminal paper by Stiglitz and Weiss (1981).
Dufﬁe and Lando (2001) established a relationship between ﬁrm-value models
and reduced-form models in continuous time. Essentially, they showed that, from
the perspective of investors with incomplete accounting information (i.e. incomplete
information about assets or liabilities of a ﬁrm), a ﬁrm-value model becomes a
reduced-form model. A less technical discussion of these issues can be found in
Jarrow and Protter (2004).
--- page 347 ---

8.2. Structural Models of Default
331
The available empirical evidence for the existence of macroeconomic common
factors is surveyed in Section 3.1 of Dufﬁe and Singleton (2003). Without going into
details, it seems that a substantial amount of the variation over time in empirical
default rates (the proportion of ﬁrms with a given credit rating that actually defaulted
in a given year) can be explained by ﬂuctuations in GDP growth rates, with empirical
default rates going up in recessions and down in periods of economic recovery.
8.2
Structural Models of Default
A model of default is known as a structural or ﬁrm-value model when it attempts to
explain the mechanism by which default takes place. Because the kind of thinking
embodied in these models has been so inﬂuential in the development of the study of
credit risk and the emergence of industry solutions (like the KMV model discussed
in Section 8.2.3), we consider this to be the best starting point for a treatment of
credit risk models.
From now on we denote a generic stochastic process in continuous time by (Xt);
the value of the process at time t ⩾0 is given by the rv Xt.
8.2.1
The Merton Model
The model proposed in Merton (1974) is the prototype of all ﬁrm-value models.
Many extensions of this model have been developed over the years, but Merton’s
original model remains an inﬂuential benchmark and is still popular with practitioners in credit risk analysis.
Consider a ﬁrm whose asset value follows some stochastic process (Vt). The ﬁrm
ﬁnances itself by equity (i.e. by issuing shares) and by debt. In Merton’s model
debt has a very simple structure: it consists of one single debt obligation or zerocoupon bond with face value B and maturity T . The value at time t of equity and
debt is denoted by St and Bt and, if we assume that markets are frictionless (no
taxes or transaction costs), the value of the ﬁrm’s assets is simply the sum of these,
i.e. Vt = St +Bt, 0 ⩽t ⩽T . In the Merton model it is assumed that the ﬁrm cannot
pay out dividends or issue new debt. Default occurs if the ﬁrm misses a payment to
its debt holders, which in the Merton model can occur only at the maturity T of the
bond. At maturity we have to distinguish between two cases.
(i) VT > B: the value of the ﬁrm’s assets exceeds the liabilities. In that case
the debtholders receive B, the shareholders receive the residual value ST =
VT −B, and there is no default.
(ii) VT ⩽B: the value of the ﬁrm’s assets is less than its liabilities and the ﬁrm
cannot meet its ﬁnancial obligations. In that case shareholders have no interest
in providing new equity capital, which would go immediately to the bondholders. Instead they “exercise their limited-liability option” and hand over
control of the ﬁrm to the bondholders, who liquidate the ﬁrm and distribute
the proceeds among themselves. Shareholders pay and receive nothing, so
that we have BT = VT , ST = 0.
--- page 348 ---

332
8. Credit Risk Management
Summarizing, we have the relations
ST = max(VT −B, 0) = (VT −B)+,
(8.1)
BT = min(VT , B) = B −(B −VT )+.
(8.2)
Equation (8.1) implies that the value of the ﬁrm’s equity at time T equals the payoff of a European call option on VT , while (8.2) implies that the value of the ﬁrm’s
debt at maturity equals the nominal value of the liabilities minus the pay-off of a
European put option on VT with exercise price equal to B.
The above model is of course a stylized description of default. In reality the
structure of a company’s debt is much more complex, so that default can occur on
many different dates. Moreover, under modern bankruptcy code, default does not
automatically imply bankruptcy, i.e. liquidation of a ﬁrm. Nonetheless, Merton’s
model is a useful starting point for modelling credit risk and for pricing securities
subject to default.
Remark 8.1. The option interpretation of equity and debt is useful in explaining
potential conﬂicts of interest between shareholders and debtholders of a company. It
is well known that the value of an option increases if the volatility of the underlying
security is increased, provided of course that the mean is not adversely affected.
Hence shareholders have an interest in the ﬁrm taking on very risky projects. Bondholders, on the other hand, have a short position in a put option on the ﬁrm’s assets
and would therefore like to see the volatility of the asset value reduced.
In the Merton model it is assumed that under the real-world or physical probability
measure P the process (Vt) follows a diffusion model (known as Black–Scholes
model or geometric Brownian motion) of the form
dVt = µV Vt dt + σV Vt dWt
(8.3)
forconstantsµV ∈R,σV > 0,andastandardBrownianmotion(Wt).Equation(8.3)
implies that VT = V0 exp((µV −1
2σ 2
V )T + σV WT ), and, in particular, that ln VT ∼
N(ln V0 + (µV −1
2σ 2
V )T, σ 2
V T ). Under the dynamics (8.3) the default probability
of our ﬁrm is readily computed. We have
P(VT ⩽B) = P(ln VT ⩽ln B) = Φ
ln(B/V0) −(µV −1
2σ 2
V )T
σV
√
T

.
(8.4)
It is immediately seen from (8.4) that the default probability is increasing in B,
decreasing in V0 and µV and, for V0 > B, increasing in σV , which is all perfectly
in line with economic intuition.
8.2.2
Pricing in Merton’s Model
In the context of Merton’s model we can price securities whose pay-off depends
on the value VT of the ﬁrm’s assets at T . Prime examples are the ﬁrm’s debt (or,
equivalently, zero-coupon bonds issued by the ﬁrm) and the ﬁrm’s equity. We brieﬂy
explain the main results, since we need them in our treatment of the KMV model
--- page 349 ---

8.2. Structural Models of Default
333
in Section 8.2.3. The derivation of pricing formulas uses basic results from ﬁnancial mathematics. Readers not familiar with these results should simply accept the
valuation formulas we present in the remainder of this section as facts and proceed
quickly to Section 8.2.3; references to useful texts in ﬁnancial mathematics are given
in Notes and Comments.
We make the following assumptions.
Assumption 8.2.
(i) We have frictionless markets with continuous trading.
(ii) The risk-free interest rate is deterministic and equal to r ⩾0.
(iii) The ﬁrm’s asset-value process (Vt) is independent of the way the ﬁrm is
ﬁnanced, and in particular it is independent of the debt level B. Moreover,
(Vt) is a traded security with dynamics given in (8.3).
Assumption (iii) merits some comment. First, the independence of (Vt) from the
ﬁnancial structure of the ﬁrm is questionable, because a very high debt level and
hence a high default probability may adversely affect the capability of a ﬁrm to
generate business and hence affect the value of its assets. This is a special case of
the indirect bankruptcy costs discussed in Section 1.4.2. Second, while there are
many ﬁrms with traded equity, the value of the assets of a ﬁrm is usually neither
completely observable nor traded.We come back to this issue in Section 8.2.3 below.
General pricing results.
Consider a claim on the value of the ﬁrm with maturity T
and pay-off h(VT ), such as the ﬁrm’s equity and debt in (8.1) and (8.2), and suppose
that Assumption 8.2 holds. Standard derivative pricing theory offers two ways for
computing the fair value f (t, Vt) of this claim at time t ⩽T . Under the partial
differential equation (PDE) approach the function f (t, v) is computed by solving
the PDE (subscripts denote partial derivatives)
ft(t, v) + 1
2σ 2
V v2fvv(t, v) + rvfv(t, v) = rf (t, v)
for t ∈[0, T ),
(8.5)
with terminal condition f (T, v) = h(v) reﬂecting the exact form of the claim to be
priced. Equation (8.5) is the famous Black–Scholes PDE for terminal-value claims.
Alternatively, the value f (t, Vt) can be computed as the expectation of the discounted pay-off under the risk-neutral measure Q (the so-called risk-neutral pricing
approach). Under Q the process (Vt) satisﬁes the stochastic differential equation
(SDE) dVt = rVt dt + σV Vt d ˜Wt for a standard Q-Brownian motion ˜W; in particular, the drift µV in (8.3) has been replaced by the risk-free interest rate r. The
risk-neutral pricing rule now states that
f (t, Vt) = EQ(e−r(T −t)h(VT ) | Ft),
(8.6)
where EQ denotes expectation with respect to Q. For details we refer to the textbooks on ﬁnancial mathematics listed in Notes and Comments; the relationship
between physical probability measure P and risk-neutral measure Q and the economic foundations of the risk-neutral pricing rule will be discussed in more detail
in Section 9.3.
--- page 350 ---

334
8. Credit Risk Management
Application to equity and debt.
According to (8.1), the ﬁrm’s equity corresponds
to a European call on (Vt) with exercise price B and maturity T . The solution of the
PDE (8.5), or the risk-neutral value of equity obtained from (8.6), is simply given
by the Black–Scholes price CBS of a European call. This yields
St = CBS(t, Vt; r, σV , B, T ) := VtΦ(dt,1) −Be−r(T −t)Φ(dt,2),
dt,1 = ln Vt −ln B + (r + 1
2σ 2
V )(T −t)
σV
√T −t
and dt,2 = dt,1 −σV
√
T −t.
⎫
⎪⎬
⎪⎭
(8.7)
Note that under the risk-neutral measure Q the distribution of the logarithmic asset
value at maturity is given by ln VT ∼N(ln V0 + (r −1
2σ 2
V )T, σ 2
V T ). Hence we get
at time t = 0
Q(VT ⩽B) = Q
ln VT −(ln V0 + (r −1
2σ 2
V )T )
σV
√
T
⩽−d0,2

= 1 −Φ(d0,2),
where we have used the fact that Φ(d) = 1 −Φ(−d). Hence 1 −Φ(d0,2) gives the
risk-neutral default probability. Similarly, 1 −Φ(dt,2) gives the risk-neutral default
probability given information up to time t.
Next we turn to the valuation of the risky debt issued by the ﬁrm. Note that by
Assumption 8.2(ii) the price at t ⩽T of a default-free zero coupon bond with
maturity T equals p0(t, T ) = exp(−r(T −t)). According to (8.2) we have
Bt = Bp0(t, T ) −P BS(t, Vt; r, σV , B, T ),
(8.8)
where P BS(t, V ; r, σV , B, T ) denotes the Black–Scholes price of a European put
with strike B, maturity T on (Vt) for given interest rate r, and volatility σV . It is
well known that
P BS(t, Vt; r, σV , B, T ) = Be−r(T −t)Φ(−dt,2) −VtΦ(−dt,1),
(8.9)
with dt,1 and dt,2 as in (8.7). Combining (8.8) and (8.9) we get
Bt = p0(t, T )BΦ(dt,2) + VtΦ(−dt,1).
(8.10)
Credit spread.
We may use (8.10) to infer the credit spread c(t, T ) implied by
Merton’s model. The credit spread measures the difference of the continuously
compounded yield to maturity of a default-free zero coupon bond p0(t, T ) and of a
defaultable zero coupon bond p1(t, T ) and is deﬁned by
c(t, T ) =
−1
T −t (ln p1(t, T ) −ln p0(T, t)) =
−1
T −t ln p1(t, T )
p0(t, T ).
(8.11)
In Merton’s model we obviously have p1(t, T ) = (1/B)Bt and hence
c(t, T ) =
−1
T −t ln

Φ(dt,2) +
Vt
Bp0(t, T )Φ(−dt,1)

.
(8.12)
--- page 351 ---

8.2. Structural Models of Default
335
Volatility
Credit spread (%)
Time to maturity
Credit spread (%)
0.1
0.2
0.3
0.4
0.5
1
2
3
4
5
0
0
0
2
4
6
0.4
0.8
1.2
(a)
(b)
Figure 8.2.
Credit spread c(t, T ) in per cent as a function of (a) the ﬁrm’s volatility σV and
(b) the time to maturity τ = T −t for ﬁxed leverage measure d = 0.6 (in (a) τ = 2 years; in
(b) σV = 0.25). Note that, for a time to maturity smaller than approximately three months,
the credit spread implied by Merton’s model is basically equal to zero. This is not in line with
most empirical studies of corporate bond spreads and has given rise to a number of extensions
of Merton’s model, which are listed in Notes and Comments. We will see in Section 9.4.4
that reduced-form models lead to a more reasonable behaviour of short-term credit spreads.
Since dt,1 can be rewritten as
dt,1 = −ln(Bp0(t, T )/Vt) + 1
2σ 2
V (T −t)
σV
√T −t
,
and similarly for dt,2, we conclude that, for a ﬁxed time to maturity T −t, the spread
c(t, T ) depends only on the volatility σV and on the ratio d := Bp0(t, T )/Vt, which
is the ratio of the present value of the ﬁrm’s debt to the value of the ﬁrm’s assets and
hence a measure of the relative debt level or leverage of the ﬁrm. As the price of a
European put is increasing in the volatility, it is immediate from (8.8) that c(t, T )
is increasing in σV . In Figure 8.2 we plot the credit-spread as a function of σV and
of the time to maturity τ = T −t.
Extensions.
Merton’s model is quite simplistic. Over the years this has given rise
to a rich literature on ﬁrm-value models. We brieﬂy comment on the most important
research directions (bibliographic references are given in Notes and Comments).
To begin with, the observation that, in reality, ﬁrms can default at essentially any
time (and not only at a deterministic point in time T ) has led to the development of
so-called ﬁrst-passage-time models. In this class of model default occurs when the
asset-value process crosses for the ﬁrst time a default threshold B, which is usually
interpreted as the average value of the liabilities. Formally, the default time τ is
deﬁned by τ = inf{t ⩾0 : Vt ⩽B}. Further technical developments include
models with stochastic default-free interest rates and models where the asset-value
process (Vt) is given by a diffusion with jumps.
Firm-value models with endogenous default threshold are an interesting economic extension of Merton’s model. Here the default boundary B is determined
--- page 352 ---

336
8. Credit Risk Management
endogenously by the strategic considerations of the shareholders and not ﬁxed a
priori by the modeller. Finally, structural models with incomplete information on
asset value and/or liabilities provide an important link between the structural and
the reduced-form approach to credit risk modelling.
8.2.3
The KMV Model
An important example of an industry model that descends from the Merton model
is the KMV model, which was developed by KMV (a private company named after
its founders Kealhofer, McQuown and Vasicek) in the 1990s and which is now
maintained by Moody’s KMV. The KMV model is widely used in industry: Berndt
et al. (2004) report that 40 out of the world’s largest 50 ﬁnancial institutions are
subscribers to the model. The major contribution of KMV is not the theoretical
development of the model, which is a relatively straightforward extension of the
Merton model, but its empirical testing and implementation using a huge proprietary
database. Our presentation of the KMV model follows Crosbie and Bohn (2002) and
Crouhy, Galai and Mark (2000). We have omitted certain details of the model, since
detailed information about actual implementation and calibration procedures is hard
to obtain; indeed, such procedures are likely to change as the model is developed
further.
Overview.
The key quantity of interest in the KMV model is the so-called expected
default frequency (EDF); this is simply the probability (under the physical probability measure P) that a given ﬁrm will default within one year as estimated using
the KMV methodology. Recall that in the classic Merton model the default probability of a given ﬁrm is given by the probability that the asset value in one year,
V1 say, lies below the threshold B representing the overall liabilities of the ﬁrm.
Under Assumption 8.2, the EDF is a function of the current asset value V0, the asset
value’s annualized mean µV and volatility σV and the threshold B; using (8.4) and
recalling that Φ(d) = 1 −Φ(−d), with T = 1, we get
EDFMerton = 1 −Φ
ln V0 −ln B + (µV −1
2σ 2
V )
σV

.
(8.13)
In the KMV model the EDF has a similar structure; however, 1 −Φ is replaced
by some decreasing function which is estimated empirically, B is replaced by a
new default threshold ˜B representing the structure of the ﬁrm’s liabilities more
closely, and the argument of the normal df in (8.13) is replaced by a slightly simpler
expression. Moreover, KMV does not assume that the asset value V0 of the ﬁrm is
directly observable. Rather, it uses an iterative technique to infer V0 from the value
of the ﬁrm’s equity.
Determination of the asset value.
Firm-value-based credit risk models usually take
the market value of the ﬁrm’s assets as a primitive. The market value reﬂects investor
expectations about the business prospects of the ﬁrm and is hence a good measure
of the value of its ongoing business. Unfortunately, the market value of a ﬁrm is
typically not fully observable for a number of reasons. To begin with, market value
--- page 353 ---

8.2. Structural Models of Default
337
can differ widely from the value of a company as measured by accountancy rules
(the book value) (see, for instance, Section 3.1.1 of Crouhy, Galai and Mark (2000)
for an example). Moreover, while the market value of the ﬁrm’s assets is simply
the sum of the market values of the ﬁrm’s equity and debt, only the equity and
parts of the debt, such as bonds issued by the ﬁrm, are actively traded, so that we
do not know the market value of the entire debt. For these reasons KMV relies on
an indirect approach and infers the asset value V0 from the more easily observed
value S0 of a ﬁrm’s equity.
We explain the approach in the context of the Merton model. Recall that under
Assumption 8.2 we have that
St = CBS(t, Vt; r, σV , B, T ).
(8.14)
Obviously, at a ﬁxed point in time, t = 0 say, (8.14) is an equation with two
unknowns, V0 and σV . To overcome this difﬁculty, KMV uses an iterative procedure. In step (1), (8.14) with some initial estimate σ (0)
V
is used to infer a time
series of asset values (V (0)
t
) from equity values. Then a new volatility estimate σ (1)
V
is constructed from this time series; a new time series (V (1)
t
) is then constructed
using (8.14) with σ (1)
V . This procedure is iterated several times (see Crosbie and
Bohn (2002) for details).
In the version of the model that is actually implemented, the capital structure
of the ﬁrm is modelled in a more sophisticated manner than in Merton’s model.
The equity value is thus no longer given by (8.14), but by some different function
f (t, Vt; r, σV , d, T, c), which has to be computed numerically. Here d represents
the leverage ratio of the ﬁrm and c is the average coupon paid by the long-term debt.
The philosophy of the approach is, however, exactly as described above.
Calculation of EDFs.
In the Merton model default, and hence bankruptcy, occurs
if the value of a ﬁrm’s assets falls below the value of its liabilities. With lognormally
distributed asset values, as implied for instance by Assumption 8.2, this leads to
default probabilities of the form (8.13). This relationship between asset value and
default probability may be too simplistic to be an accurate description of actual
default probabilities for a number of reasons: asset values are not necessary lognormal but might follow a distribution with heavy tails; our assumptions about
the capital structure of the ﬁrm are too simplistic; there might be payments due
at an intermediate point in time causing default at that date; ﬁnally, under modern
bankruptcy code, default need not automatically lead to bankruptcy, i.e. to liquidation of the ﬁrm.
To account for these factors, KMV introduces as an intermediary step a state
variable, the so-called distance to default (DD), given by
DD := (V0 −˜B)/(σV V0),
(8.15)
where ˜B represents the default threshold (often the liabilities payable within one
year). Sometimes practitioners call the distance to default the “number of standard
deviations a company is away from its default threshold ˜B”. Note that (8.15) is in
--- page 354 ---

338
8. Credit Risk Management
Table 8.1.
A summary of the KMV approach. The example is taken from Crosbie and Bohn
(2002); it is concerned with the situation of Philip Morris Inc. at the end of April 2001.
Financial quantities are in millions of US dollars.
Variable
Value
Notes
Market value of equity S0
110 688
Share price × shares outstanding
Overall book liabilities B
64 062
Determined from balance sheet
Market value of assets V0
170 558 
Determined from option-pricing model
Asset volatility σV
0.21
Default threshold ˜B
47 499
Liabilities payable within one year
DD
3.5
Given by the ratio (170 −47)/(0.21 × 170),
using relation (8.15)
EDF (one year)
0.25%
Determined using empirical mapping between
distance to default and default frequency
fact an approximation of the argument of (8.13), since µV and σ 2
V are small and
since ln V0 −ln ˜B ≈(V0 −˜B)/V0.
IntheKMVmodelitisassumedthatﬁrmswithequalDDhaveequaldefaultprobabilities. The functional relationship between DD and EDF is determined empirically.
Using a database of historical default events, KMV estimates for every horizon the
proportion of ﬁrms with DD in a given small range that defaulted within the given
horizon. This proportion is the empirically estimated EDF.As one would expect, the
empirically estimated EDF is a decreasing function; its precise form is proprietary
to Moody’s KMV.
In Table 8.1, we illustrate the computation of the EDF using the KMV approach
for Philip Morris Inc.
8.2.4
Models Based on Credit Migration
In this section we present models where the default probability of a given ﬁrm is
determined from an analysis of credit migration. The standard industry model in
this class is CreditMetrics, developed by JPMorgan and the RiskMetrics Group (see,
for instance, RiskMetrics Group 1997). We ﬁrst describe the basic idea of a creditmigration model and the kind of data that is used to calibrate such a model, before
showing how a migration model can be embedded in a ﬁrm-value model and thus
treated as a structural model.
Credit ratings and migration.
In the credit-migration approach each ﬁrm is
assigned to a credit-rating category at any given time point. There are a ﬁnite number
of such ratings and they are ordered by credit quality and include the category of
default. The probability of moving from one credit rating to another credit rating
over the given risk horizon (typically one year) is then speciﬁed.
Credit ratings for major companies or sovereigns and rating-transition matrices
are provided by rating agencies such as Moody’s or Standard & Poor’s (S&P);
alternatively, proprietary rating systems internal to a ﬁnancial institution can be
used. In the S&P rating system there are seven rating categories (AAA, AA, A,
--- page 355 ---

8.2. Structural Models of Default
339
Table 8.2.
Probabilities of migrating from one rating quality to another within one year.
Source: Standard & Poor’s CreditWeek (15 April 1996).
Rating at year-end (%)
Initial



rating
AAA
AA
A
BBB
BB
B
CCC
Default
AAA
90.81
8.33
0.68
0.06
0.12
0.00
0.00
0.00
AA
0.70
90.65
7.79
0.64
0.06
0.14
0.02
0.00
A
0.09
2.27
91.05
5.52
0.74
0.26
0.01
0.06
BBB
0.02
0.33
5.95
86.93
5.30
1.17
1.12
0.18
BB
0.03
0.14
0.67
7.73
80.53
8.84
1.00
1.06
B
0.00
0.11
0.24
0.43
6.48
83.46
4.07
5.20
CCC
0.22
0.00
0.22
1.30
2.38
11.24
64.86
19.79
BBB, BB, B, CCC) with AAA being the highest and CCC the lowest rating of
companies which have not defaulted; there is also a default state. Moody’s uses
seven pre-default rating categories labelled Aaa, Aa, A, Baa, Ba, B, C; a ﬁner alphanumeric system is also in use. Transition probabilities are typically presented in the
form of a rating-transition probability matrix; an example from Standard & Poor’s
is presented in Table 8.2. These transition matrices are determined from historical
default data.Approaches for estimating rating-transition matrices are listed in Notes
and Comments.
In the credit-migration approach one assumes that the current credit rating completely determines the default probability, so that this probability can be read off
from the transition matrix. For instance, if we use the transition matrix presented
in Table 8.2, we obtain that the one-year default probability of a company whose
current S&P credit rating is A is 0.06%, whereas the default probability of a CCCrated company is almost 20%. Rating agencies also produce cumulative default
probabilities over larger time horizons. In Table 8.3 we present estimates (due to
Standard & Poor’s) for cumulative default probabilities of companies with a given
current credit rating. For instance, according to this table the probability that a
company whose current credit rating is BBB defaults within the next four years
is 1.27%. These cumulative default probabilities have been estimated directly.Alternatively, we could have used the one-year transition matrix presented in Table 8.2
to estimate these numbers. If we assume that the credit-migration process follows a
time-homogeneous Markov chain, the n-year transition matrix is simply the n-fold
product of the one-year transition matrix, and the n-year default probabilities can be
read off from the last column of the n-year transition matrix. Of course, under the
Markov assumption, both approaches should produce roughly similar results. In the
BBB-case above, the four-year default probability under the Markov assumption
becomes 1.41%, whereas the cumulative default probability for a BBB company
according to Table 8.3 is 1.27%, which is relatively close. Nonetheless, the hypothesis that rating transitions occur in a Markovian way has been criticized heavily on
empirical grounds (see Notes and Comments).
--- page 356 ---

340
8. Credit Risk Management
Table 8.3.
Average cumulative default rates (%).
Source: Standard & Poor’s CreditWeek (15 April 1996).
Term
Initial



rating
1
2
3
4
5
7
10
15
AAA
0.00
0.00
0.07
0.15
0.24
0.66
1.40
1.40
AA
0.00
0.02
0.12
0.25
0.43
0.89
1.29
1.48
A
0.06
0.16
0.27
0.44
0.67
1.12
2.17
3.00
BBB
0.18
0.44
0.72
1.27
1.78
2.99
4.34
4.70
BB
1.06
3.48
6.12
8.68
10.97
14.46
17.73
19.91
B
5.20
11.00
15.95
19.40
21.88
25.14
29.02
30.65
CCC
19.79
26.92
31.63
35.97
40.15
42.64
45.10
45.10
Remark 8.3 (accounting for business cycles). As discussed in Section 8.1, empirical default rates tend to vary with the state of the economy, being high during
recessions and low during periods of economic expansion. Transition rates as estimated by Standard & Poor’s or Moody’s on the other hand are historical averages
over longer time horizons covering several business cycles. Moreover, rating agencies focus on the average credit quality “through the business cycle” when attributing a credit rating to a particular ﬁrm. Hence the default probabilities from the
credit-migration approach are estimates for the average default probability, independent of the current economic environment. In situations where we are interested
in “point-in-time” estimates of default probabilities reﬂecting the current macroeconomic environment, such as in the pricing of a short-term loan, adjustments to
the long-term average default probabilities from the credit-migration approach have
to be made. For instance, we could use equity prices as an additional source of
information, as is done in the KMV approach.
The KMV model and credit-migration approaches compared.
The KMV approach
has the following advantages.
• Rating agencies are typically slow in adjusting their credit ratings, so that the
current rating does not always reﬂect the economic condition of a ﬁrm. This
is particularly important if the credit quality of a ﬁrm deteriorates rapidly,
as is typically the case with companies which are close to default. The EDF
as estimated by KMV, on the other hand, reacts quickly to changes in the
economic prospects of a ﬁrm, as these tend to be reﬂected in the ﬁrm’s share
price and hence in the estimated distance to default. Examples that show that
the KMV approach often detects a deterioration in the credit quality of a
company prior to a downgrading by the rating agencies are given in Crosbie
and Bohn (2002).
• EDFs tend to reﬂect the current macroeconomic environment. The distance to
default is observed to rise in periods of economic expansion (essentially due
to higher share prices reﬂecting better economic conditions) and to decrease
in recession periods. The historical rating-transition probabilities provided by
--- page 357 ---

8.2. Structural Models of Default
341
Moody’s and Standard & Poor’s on the other hand are relatively insensitive
to the current macroeconomic environment. Hence KMV’s EDFs might be
better predictors of default probabilities over short time horizons.
The following points are drawbacks of the KMV methodology and can be viewed
as advantages of the credit-migration approach.
• The KMV methodology is quite sensitive to global overand underreaction
of equity markets. In particular, the breaking of a stock market bubble may
lead to drastically increased EDFs, even if the economic outlook for a given
corporation has not changed very much. This can be problematic if a KMVtype model is widely used to determine the regulatory capital that a bank
needs to support its loan book. The breaking of a stock market bubble might
lead to a substantial increase in the required regulatory capital. This limits the
ability of banks to supply new credit, which might have an adverse impact on
the real economy. This is a prime example of the potential negative-feedback
effects of risk management and regulation that we discussed in Section 1.3
under the label “the crocodile of risk management is (possibly) eating its own
tail”.
• Finally, the KMV methodology as presented here applies only to ﬁrms with
publicly traded stock, whereas a ratings-based approach can be applied to all
companies for which some internal rating is available.
Credit-migration models as ﬁrm-value models.
We now show how credit-migration models such as CreditMetrics can be embedded in a ﬁrm-value model of the
Merton type. We consider a ﬁrm which has been assigned to some rating category at
the outset of the time period of interest [0, T ] and for which transition probabilities
¯p(j), 0 ⩽j ⩽n, are available on the basis of that rating. These express the probability that the ﬁrm belongs to rating class j at the time horizon T and constitute a
row of some table similar to Table 8.2. In particular, ¯p(0) is the default probability
of the ﬁrm.
Suppose that the asset-value process (Vt) of the ﬁrm follows the model given
in (8.3), so that
VT = V0 exp((µV −1
2σ 2
V )T + σV WT )
(8.16)
is lognormally distributed. We can now choose thresholds
−∞= ˜d0 < ˜d1 < · · · < ˜dn < ˜dn+1 = ∞
(8.17)
such that P( ˜dj < VT ⩽˜dj+1) = ¯p(j) for j ∈{0, . . . , n}. Thus we have translated
the transition probabilities into a series of thresholds for an assumed asset-value process. The threshold ˜d1 is the default threshold; in the Merton model of Section 8.2.1,
˜d1 was interpreted as the value of the ﬁrm’s liabilities. The higher thresholds are the
asset-value levels that mark the boundaries of higher rating categories. The ﬁrmvalue model in which we have embedded the migration model can be summarized
by saying that the ﬁrm belongs to rating class j at the time horizon T if and only if
˜dj < VT ⩽˜dj+1.
--- page 358 ---

342
8. Credit Risk Management
The migration probabilities in the ﬁrm-value model obviously remain invariant
under simultaneous strictly increasing transformations of VT and the thresholds ˜dj.
If we deﬁne
XT := ln VT −ln V0 −(µV −1
2σ 2
V )T
σV
√
T
,
(8.18)
dj := ln ˜dj −ln V0 −(µV −1
2σ 2
V )T
σV
√
T
,
(8.19)
then we can equivalently say that the ﬁrm belongs to rating class j at the time
horizon T if and only if dj < XT ⩽dj+1. Observe that XT is a standardized version
of the asset-value log-return ln VT −ln V0; we can easily verify that XT = WT /
√
T
and that it therefore has a standard normal distribution.
8.2.5
Multivariate Firm-Value Models
The ﬁrm-value models of this section, such as KMV and CreditMetrics, have been
discussed in relation to the default (or credit migration) risk of a single ﬁrm. In
order to apply these models at portfolio level we require a multivariate version of
Merton’s model.
Now assume that we have m companies and that the multivariate asset-value
process (Vt) with Vt = (Vt,1, . . . , Vt,m)′ follows an m-dimensional geometric
Brownian motion with drift vector µV = (µV 1, . . . , µV m)′, vector of volatilities
σV = (σV 1, . . . , σV m)′ and instantaneous correlation matrix P.
This implies that for all i the asset value VT,i is of the form (8.16), with µV =
µV i and σV = σV i and WT = WT,i. Moreover, WT := (WT,1, . . . , WT,m)′ is
a multivariate normal random vector satisfying WT ∼Nm(0, T P). The model
is completed by setting thresholds as in (8.17) for each ﬁrm: in a Merton-style
model each ﬁrm would have a default threshold corresponding to liabilities, and in
a CreditMetrics model the thresholds would be determined by the credit-migration
probabilities of the ﬁrms. Note that we could again transform asset values and
thresholds using transformations of the form (8.18) and (8.19). This would result in
variables XT,i = WT,i/
√
T satisfying XT = (XT,1, . . . , XT,m)′ ∼Nm(0, P) and
the model would have again been translated onto a standard Gaussian scale. Models
of this kind will studied in more detail in Section 8.3.
Notes and Comments
There are many excellent texts, at varying technical levels, in which the basic results
on mathematical ﬁnance used in Section 8.2.2 can be found. Models in discrete
time are discussed in Cox and Rubinstein (1985), Jarrow and Turnbull (1999) and
in the more advanced book by F¨ollmer and Schied (2004). Excellent introductions to continuous-time models include Baxter and Rennie (1996), Dufﬁe (2001),
Bj¨ork (1998), Bingham and Kiesel (1998) and Lamberton and Lapeyre (1996). More
advanced texts are Musiela and Rutkowski (1997) and Karatzas and Shreve (1998);
the technical level of the latter two volumes is not needed in this book.
--- page 359 ---

8.3. Threshold Models
343
Lando (2004) gives a good overview of the rich literature on ﬁrm-value models.
First-passage-time models have been considered by, among others, Black and Cox
(1976) and, including stochastic interest rates, by Longstaff and Schwartz (1995).
The problem of the unrealistically low credit spreads for small maturities τ = T −t,
which we pointed out in Figure 8.2, has also led to extensions of Merton’s model.
Partial remedies within the class of ﬁrm-value models include models with jumps
in the ﬁrm value, as in Zhou (2001), time-varying default thresholds, as in Hull
and White (2001), stochastic volatility models for the ﬁrm-value process with timedependent dynamics, as in Overbeck and Schmidt (2003), and incomplete information on ﬁrm value or default threshold, as in Dufﬁe and Lando (2001) and Giesecke
(2005). Models with endogenous default thresholds have been considered by, among
others, Leland (1994), Leland and Toft (1996) and Hilberink and Rogers (2002).
The original documentation for the KMV model is Crosbie and Bohn (2002) (for
the modelling of default of a single entity) and Kealhofer and Bohn (2001) (for
portfolio aspects of the model). Moreover, Moody’s KMV has recently developed
a private ﬁrm model, which provides EDFs for small-to-medium-size private ﬁrms
without publicly traded stock (see Nyberg, Sellers and Zhang 2001).
A good discussion of industry models for credit risk is given in Crouhy, Galai
and Mark (2000) (see also Chapters 8–10 of Crouhy, Galai and Mark (2001) for a
more detailed presentation). Chapter 7 of Crouhy, Galai and Mark (2001) contains
useful background information on credit-rating systems. Statistical approaches to
the estimation of rating-transition matrices are discussed in Hu, Kiesel and Perraudin
(2002) and in Lando and Skodeberg (2002). The latter paper also shows that there
is some momentum in rating-transition data, which contradicts the assumption that
rating transitions form a Markov chain. The literature on statistical properties of
ratingtransitionsissurveyedextensivelyinChapter4ofDufﬁeandSingleton(2003).
8.3
Threshold Models
The models of this section are one-period models for portfolio credit risk inspired by
the ﬁrm-value models of Section 8.2. Their deﬁning attribute is the idea that default
occurs for a company i when some critical rv Xi := XT,i lies below some critical
deterministic threshold di at the end of the time period [0, T ]. In Merton’s model Xi
is a lognormally distributed asset value and di represents liabilities; in CreditMetrics
Xi is a normally distributed rv, interpreted as a change in logarithmic asset value.
Portfolio extensions of ﬁrm-value models typically use multivariate lognormal or
normal distributions for the vector X = (X1, . . . , Xm)′. The dependence among
defaults stems from the dependence among the components of the vector X.
The very general set-up of the threshold models of this section will allow both
more general interpretations for the critical variable and more general distributional
models. For example, in Li’s model, discussed in Example 8.7, the critical variables
are the “times to default” of the ﬁrms, and the critical threshold is the time horizon T
itself. The distributions assumed for X can be completely general and indeed a major
issue of this section will be the inﬂuence of the copula of the multivariate distribution
of X on the risk of the portfolio.
--- page 360 ---

344
8. Credit Risk Management
8.3.1
Notation for One-Period Portfolio Models
It is convenient to introduce some notation for one-period portfolio models which
will be in force throughout the remainder of the chapter. We consider a portfolio of
m obligors and ﬁx a time horizon T . For 1 ⩽i ⩽m, we let the rv Si be a state
indicator for obligor i at time T and assume that Si := ST,i takes integer values
in the set {0, 1, . . . , n} representing, for example, rating classes; as in the previous
section, we interpret the value 0 as default and non-zero values as states of increasing
credit quality. At time t = 0 obligors are assumed to be in some non-default state.
Mostly we will concentrate on the binary outcomes of default and non-default
and ignore the ﬁner categorization of non-defaulted companies. In this case we write
Yi := YT,i for the default indicator variables so that Yi = 1
⇐⇒
Si = 0 and
Yi = 0 ⇐⇒Si > 0. The random vector Y = (Y1, . . . , Ym)′ is a vector of default
indicators for the portfolio and p(y) = P(Y1 = y1, . . . , Ym = ym), y ∈{0, 1}m,
is its joint probability function; the marginal default probabilities are denoted by
¯pi = P(Yi = 1), i = 1, . . . , m.
The default or event correlations will be of particular interest to us; they are
deﬁned to be the correlation of the default indicators. Because
var(Yi) = E(Y 2
i ) −¯p2
i = E(Yi) −¯p2
i = ¯pi −¯p2
i ,
we obtain for ﬁrms i and j, with i̸ = j,
ρ(Yi, Yj) =
E(YiYj) −¯pi ¯pj

( ¯pi −¯p2
i )( ¯pj −¯p2
j)
.
(8.20)
We count the number of defaulted obligors at time T with the rv M := m
i=1 Yi. The
actual loss if company i defaults—termed loss given default (LGD) in practice—is
modelled by the random quantity δiei, where ei represents the overall exposure to
company i and 0 ⩽δi ⩽1 represents a random proportion of the exposure which
is lost in the event of default. We will denote the overall loss by L := m
i=1 δieiYi
and make further assumptions about the ei and δi variables as and when we need
them.
It is possible to set up different credit risk models leading to the same multivariate
distribution of S or Y. Since this distribution is the main object of interest in the
analysis of portfolio credit risk, we call two models with state vectors S and ˜S (or
Y and ˜Y) equivalent if S d= ˜S (or Y
d= ˜Y).
The exchangeable special case.
To simplify the analysis we will often assume that
the state indicator S, and thus the default indicator Y, are exchangeable. This seems
the correct way to mathematically formalize the notion of homogeneous groups
that is used in practice. Recall that a random vector S is said to be exchangeable
if (S1, . . . , Sm) d= (SΠ(1), . . . , SΠ(m)) for any permutation (Π(1), . . . , Π(m)) of
(1, . . . , m). Exchangeability implies in particular that, for any k ∈{1, . . . , m −1},
all of the
+m
k
,
possible k-dimensional marginal distributions of S are identical.
In this situation we introduce a simple notation for default probabilities where
--- page 361 ---

8.3. Threshold Models
345
π := P(Yi = 1), i ∈{1, . . . , m}, is the default probability of any ﬁrm and
πk := P(Yi1 = 1, . . . , Yik = 1),
{i1, . . . , ik} ⊂{1, . . . , m}, 2 ⩽k ⩽m,
(8.21)
is the joint default probability for k ﬁrms. In other words, πk is the probability that
an arbitrarily selected subgroup of k companies defaults in [0, T ]. When default
indicators are exchangeable, we get
E(Yi) = E(Y 2
i ) = P(Yi = 1) = π,
∀i,
E(YiYj) = P(Yi = 1, Yj = 1) = π2,
∀i̸ = j,
so that cov(Yi, Yj) = π2 −π2; this implies that the default correlation in (8.20) is
given by
ρY := ρ(Yi, Yj) = π2 −π2
π −π2 ,
i̸ = j,
(8.22)
which is a simple function of the ﬁrstand second-order default probabilities.
8.3.2
Threshold Models and Copulas
We start with a general deﬁnition of a threshold model before discussing the link to
copulas.
Deﬁnition 8.4. Let X = (X1, . . . , Xm)′ be an m-dimensional random vector and
let D ∈Rm×n be a deterministic matrix with elements dij such that, for every i, the
elementsoftheithrowformasetofincreasingthresholdssatisfyingdi1 < · · · < din.
Augment these thresholds by setting di0 = −∞and di(n+1) = ∞for all obligors
and then set
Si = j ⇐⇒dij < Xi ⩽di(j+1),
j ∈{0, . . . , n}, i ∈{1, . . . , m}.
Then (X, D) is said to deﬁne a threshold model for the state vector S
=
(S1, . . . , Sm)′.
We refer to X as the vector of critical variables and denote its marginal dfs by
Fi(x) = P(Xi ⩽x). The ith row of D contains the critical thresholds for ﬁrm i.
By deﬁnition, default (corresponding to the event Si = 0) occurs if Xi ⩽di1 so that
the default probability of company i is given by ¯pi = Fi(di1).
In the context of such models it is important to distinguish the default correlation
ρ(Yi, Yj) of two ﬁrms i̸ = j from the so-called asset correlation (the correlation
of the critical variables Xi and Xj). For given default probabilities, ρ(Yi, Yj) is
determined by E(YiYj) according to (8.20), and in a threshold model E(YiYj) =
P(Xi ⩽di1, Xj ⩽dj1), so default correlation depends on the joint distribution of
Xi and Xj. If X is multivariate normal, as in the CreditMetrics/KMV-type models,
the correlation of Xi and Xj determines the copula of their joint distribution and
hence the default correlation (see Lemma 8.5 below). For general critical variables
outside the multivariate normal class, the correlation of the critical variables does
not fully determine the default correlation; this can have serious implications for the
tail of the distribution of M = m
i=1 Yi, as will be shown in Section 8.3.5.
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
