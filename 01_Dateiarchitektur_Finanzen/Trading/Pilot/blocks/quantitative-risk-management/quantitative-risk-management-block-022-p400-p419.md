# Quantitative Risk Management_ Concepts, Techniques, and -- Alexander J_ McNeil, Rüdiger Frey, Paul Embrechts -- Princeton series in finance, -- isbn13 9780691122557 -- 478a0059673fecd0c76229cd3d8884e7 -- Anna’s Arc.pdf — pages 400–419

--- page 400 ---

384
8. Credit Risk Management
There is a huge amount of literature on the estimation of models for pricing creditrisky securities that uses mainly data on corporate bond prices as input: Chapter 7
of Dufﬁe and Singleton (2003) is a good starting point. Empirical work on the
calibration of credit risk models to loan data, on the other hand, is relatively sparse,
which is probably related to data problems. An example of the latter type of work
is Altman and Suggitt (2000).
--- page 401 ---

9
Dynamic Credit Risk Models and
Credit Derivatives
In this chapter we study credit risk models in continuous time and consider the pricing of credit derivatives in the framework of reduced-form models (see Section 8.1
for an overview of model types). Reduced-form models are popular in practice, since
they lead to tractable formulas explaining the price of credit-risky securities in terms
of economic covariates, which facilitates estimation. Moreover, with reduced-form
models it is possible to apply the well-developed pricing machinery for default-free
term structure models to the analysis of defaultable securities.
We begin with a brief introduction to credit derivatives in Section 9.1. These
products have become indispensable tools for the management of credit risk, and
the corresponding markets have seen a massive growth in recent years. We continue with two preparatory sections: Section 9.2 contains mathematical tools for
reduced-form models; Section 9.3 brieﬂy introduces key concepts from mathematical ﬁnance, thereby providing the methodological basis for our analysis. Particular attention will be given to the distinction between real-world and risk-neutral
default probabilities. Sections 9.4 and 9.5 review standard but indispensable material on the pricing of defaultable securities in reduced-form models; in particular,
the relationship between pricing problems for defaultable and default-free securities is discussed. Sections 9.6–9.8 are devoted to reduced-form models for credit
portfolios. We begin with models with conditionally independent defaults. In this
model class, default times are independent given the realization of some observable
economic background process, making these models a straightforward extension
of the static Bernoulli mixture models discussed in Chapter 8. More sophisticated
models, where there is interaction between defaults in the sense that the default of
one ﬁrm inﬂuences the conditional survival probability of the remaining ﬁrms in the
portfolio, are discussed thereafter.
In this book we have so far concentrated on static or discrete-time models and
risk-management issues; continuous-time models and the pricing of derivatives have
played only a minor role. In this chapter we make an exception for a number of
reasons. First, credit risk management and credit derivatives are intimately linked.
In fact, the quest of ﬁnancial institutions for better tools to manage and diversify
the credit risk in their portfolios and the recent developments in the regulation of
credit risk are the main drivers of the tremendous growth of the credit derivatives
market that we are currently witnessing. Since the pay-off of most credit derivatives
--- page 402 ---

386
9. Dynamic Credit Risk Models
depends on the timing of default, dynamic credit risk models are clearly needed to
analyse these products. Second, the pricing of portfolio credit derivatives is a key
area of application for many of the concepts for modelling dependent risks discussed
in this book; in particular, copulas play a prominent role. Third, dynamic models
of portfolio credit risk have recently generated a lot of interest in academia and in
industry, and we want to offer our readership an introduction to the ﬁeld.
Credit risk modelling is a large area that cannot be covered in a few chapters, and
consequently we have had to omit a lot of interesting and relevant material. Important
omissions include advanced ﬁrm-value models (other than Merton); continuoustime models for rating transitions; an analysis of credit risk in interest-rate swaps;
and forward-rate models of Heath–Jarrow–Morton type for corporate bonds. The
main reason for these omissions is our decision to focus on the growing ﬁeld of
dynamic portfolio credit risk models. Much of the material in this area is of recent
vintage and to our knowledge has not been discussed extensively at textbook level
before.
There are several full textbook treatments of dynamic credit risk models including
Bielecki and Rutkowski (2002), Bluhm, Overbeck and Wagner (2002), Dufﬁe and
Singleton (2003), Lando (2004) and Sch¨onbucher (2003). Excellent survey articles
include Schmidt and Stute (2004) and Giesecke (2004). While each text has a different focus, some overlap with the material treated here is unavoidable and will be
indicated, together with suggestions for further reading, in Notes and Comments of
the respective sections.
9.1
Credit Derivatives
9.1.1
Overview
We ﬁnd it convenient to divide the universe of credit-risky securities into three
different types: vulnerable claims, single-name credit derivatives, and portfoliorelated credit derivatives. Vulnerable claims are securities whose promised pay-off
is not linked to credit events, but whose issuer may default. Hence the actual pay-off
received by the buyer of the security (for instance, a counterparty in a swap transaction) is adversely affected by the default of the issuer. Important examples include
corporate bonds and interest-rate swaps. While the pricing of certain vulnerable
claims raises challenging issues, these products are of no concern to us here, as
credit risk is not their primary focus; some references can be found in Notes and
Comments.
Credit derivatives are securities which are primarily used for the management and
trading of credit risk. In the case of a single-name credit derivative the promised
pay-off depends on the occurrence of a credit event affecting a single ﬁnancial
entity; otherwise the pay-off is related to credit events in a whole portfolio. Credit
derivatives are a fairly young asset class and the market continues to evolve, with
new products appearing frequently. Credit derivatives are traded over the counter,
so the precise pay-off speciﬁcation may vary a lot between contracts of similar
type. Nonetheless, due to efforts of bodies such as the International Swap Dealers
--- page 403 ---

9.1. Credit Derivatives
387
Association (ISDA), in recent years some standardization has taken place. Credit
derivatives have become popular because they help ﬁnancial ﬁrms to manage the
credit risk on their books by dispersing parts of it through the wider ﬁnancial sector, thereby reducing concentration of risk. In fact, the widespread use of these
instruments may have enhanced the resilience of the overall ﬁnancial system. In this
context the following remarks made by Alan Greenspan in his speech before the
Council on Foreign Relations in November 2002 (see Section 1.4.1) are of interest.
More recently, instruments . . . such as credit default swaps, collateralized debt obligations and credit-linked notes have been developed and
their use has grown rapidly in recent years. The result? Improved credit
risk management together with more and better risk-management tools
appear to have signiﬁcantly reduced loan concentrations in telecommunications and, indeed, other areas and the associated stress on banks
and other ﬁnancial institutions.
More generally, such instruments appear to have effectively spread
losses from defaults by Enron, Global Crossing, Railtrack, WorldCom,
Swissair, and sovereignArgentinian credits over the past year to a wider
set of banks than might previously have been the case in the past, and
from banks, which have largely short-term leverage, to insurance ﬁrms,
pension funds or others with diffuse long-term liabilities or no liabilities at all. Many sellers of credit risk protection, as one might presume,
have experienced large losses, but because of signiﬁcant capital, they
were able to avoid the widespread defaults of earlier periods of stress.
It is noteworthy that payouts in the still relatively small but rapidly
growing market in credit derivatives have been proceeding smoothly
for the most part. Obviously this market is still too new to have been
tested in a widespread down-cycle for credit, but, to date, it appears to
have functioned well.
Major participants in the market for credit derivatives are banks, insurance companies and investment funds. Banks are typically net buyers of protection against credit
events; insurance companies and other investors are net sellers of credit protection.
9.1.2
Single-Name Credit Derivatives
Credit default swaps.
Credit default swaps (CDSs) are the workhorse of the credit
derivatives market; according to a study by Patel (2002), in 2002 the market share
of CDSs in the credit derivatives market was approximately 67%. Hence the market
for CDSs written on larger corporations is fairly liquid. Moreover, in contrast to
corporate bonds, the proﬁtability of CDSs is barely affected by tax issues. For these
reasons CDSs are the natural underlying security for many more complex credit
derivatives, and models for pricing portfolio-related credit derivatives are usually
calibrated to quoted CDS spreads (see Section 9.3.3 below for details).
The basic structure of a CDS is depicted in Figure 9.1. There are three parties
involved in a CDS: the reference entity, the protection buyer and the protection
--- page 404 ---

388
9. Dynamic Credit Risk Models
C
B
A
Premium payments until default or maturity
Default of C occurs?
yes: default payment
no: no payment
Figure 9.1.
The basic structure of a CDS. Firm C is the reference entity,
ﬁrm A is the protection buyer, and ﬁrm B is the protection seller.
seller. If the reference entity experiences a default event before the maturity date T
of the contract, the protection seller makes a default payment to the protection buyer,
which mimics the loss on a security issued by the reference entity (often a corporate
bond) due to the default; this part of a CDS is called the default payment leg. In this
way the protection buyer has acquired ﬁnancial protection against the loss on the
reference asset he would incur in case of a default; note, however, that the protection
buyer is not obliged to hold the reference asset. As a compensation the protection
buyer makes a periodic premium payment (typically quarterly or semiannually) to
the protection seller (the premium payment leg); after the default of the reference
entity, premium payments stop. There is no initial payment. The premium payments
are quoted in the form of an annualized percentage x∗of the notional value of
the reference asset; x∗is termed the (fair or market quoted) CDS spread. For a
mathematical description of the payments, see Section 9.3.3 below.
There are a number of technical and legal issues in the speciﬁcation of a CDS.
In particular, the parties have to agree on the precise deﬁnition of a default event
and on a procedure to determine the size of the default payment in case a default
event of the reference entity occurs. Note that a CDS is traded over the counter and
is not guaranteed by some clearing house. Hence it is possible that the protection
seller itself defaults before the maturity of the contract, in which case the default
protection acquired by the protection buyer becomes worthless.
Credit-linked notes.
A credit-linked note is a combination of a credit derivative and
a coupon bond that is sold as a ﬁxed package. The coupon payments (and sometimes
also the repayment of the principal) are reduced if a third party (the reference entity)
experiences a default event during the lifetime of the contract, so the buyer of a
credit-linked note is providing credit protection for the seller. Credit-linked notes
are issued essentially for two reasons. First, from a legal point of view, a credit-linked
note is treated as a ﬁxed-income investment, so that investors who are unable to enter
into a transaction involving credit derivatives directly may nonetheless sell credit
protection by buying credit-linked notes. Second, an investor buying a credit-linked
note pays the price up front, so that the credit protection sale is fully collaterized,
i.e. the protection buyer (the issuer of the credit-linked note) is protected against
losses caused by the default of the protection seller.
--- page 405 ---

9.1. Credit Derivatives
389
9.1.3
Portfolio Credit Derivatives
Notation.
In order to describe the pay-off of portfolio credit derivatives we introduce some notation. We consider a portfolio with m ﬁrms. The random vector
Yt = (Yt,1, . . . , Yt,m)′ describes the state of our portfolio at time t ⩾0. In keeping with the notation introduced in Chapter 8, Yt,i = 1 if ﬁrm i has defaulted
up to time t, and Yt,i = 0 otherwise; (Yt,i) is termed the default indicator process of ﬁrm i. The default time of ﬁrm i is denoted by τi > 0. Assuming that
there are no simultaneous defaults in our portfolio, we may deﬁne the ordered
default times T0 < T1 < · · · < Tm recursively by T0 = 0 and, for 1 ⩽n ⩽m,
Tn = min{τi : τi > Tn−1, 1 ⩽i ⩽m}. By ξn ∈{1, . . . , m} we denote the identity
of the ﬁrm defaulting at time Tn, i.e. ξn = i if τi = Tn.As in Chapter 8, the exposure
to reference entity i is denoted by ei; the percentage loss given default of ﬁrm i is
denoted by δi ∈[0, 1]. The cumulative loss of the portfolio up to time t is thus given
by Lt = m
i=1 δieiYt,i.
Basket default swaps.
Basket default swaps, or, more technically, kth-to-default
swaps, offer protection against the kth default in a portfolio with m > k obligors
(the basket). As in the case of an ordinary CDS the premium payments on a kthto-default swap take the form of a periodic payment stream, which stops at the kth
default time Tk. The default payment is triggered if Tk is smaller than the maturity
date of the swap; the size of the default payment may depend on the identity ξk of the
kth defaulting ﬁrm. While ﬁrst-to-default swaps are traded frequently, higher-order
default swaps are encountered only occasionally in real markets. We discuss the
pricing of ﬁrst-to-default swaps in Sections 9.6.3 and 9.8.1 below.
Collaterized debt obligations (CDOs).
CDOs are, at the time of writing, the most
important class of portfolio credit derivatives. A CDO is a ﬁnancial instrument for
the securitization of credit-risky securities related to a pool of reference entities such
as bonds, loans or protection-seller positions in single-name CDSs; these securities
form the asset side of the CDO. While many different types of CDO exist, the basic
structure is the same. The assets are sold to a so-called special-purpose vehicle
(SPV), a company that has been set up with the single purpose of carrying out
the securitization deal. To ﬁnance the acquisition of the assets, the SPV issues
notes belonging to tranches of different seniorities, which form the liability side
of the structure. This amounts to a repackaging of the assets. The tranches of the
liability side are called (in order of increasing seniority) equity, mezzanine and
senior (sometimes also super-senior) tranches. In this way most of the losses on the
asset side generated by credit events are borne by the equity tranche, so the notes
issued by the SPV belonging to the more senior tranches have a credit rating which
is substantially higher than the average credit quality of the asset pool. This makes
the notes attractive to certain investor classes.
If the asset side consists mainly of bonds and loans, one speaks of asset-based
structures; if the underlying asset pool consists mainly of protection-seller positions
in single-name CDSs, the structure is termed synthetic CDO. The cash-ﬂows of a
synthetic CDO are slightly different from those of an asset-based CDO: on the asset
--- page 406 ---

390
9. Dynamic Credit Risk Models
Assets
SPV
Liabilities
Senior
Mezzanine
Equity
Interest and
 principal
Interest and
 principal
Initial
investment
Proceeds of
 note sale
CDS premiums
Default payments
of CDS
Protection
fee
Default payments
of tranches
Figure 9.2.
Schematic representation of the payments in a CDO structure.
Payments corresponding to synthetic CDOs are indicated in italics.
side the SPV receives the premium payments on the CDSs in the asset pool and
makes the corresponding default payments; on the liability side the SPV receives
default payments from the noteholders, which are triggered by credit events in the
asset pool, and makes periodic premium payments as a compensation. The payments
associated with a typical CDO are depicted schematically in Figure 9.2.
Asset-based structures where the asset pool consists mainly of bonds are known
as collaterized bond obligation (CBO); if the asset side consists mainly of loans, a
CDO is termed collaterized loan obligation (CLO). If the underlying asset pool is
actively traded with the goal of enhancing its value, a CDO structure is known as
an arbitrage CDO; if the asset side remains relatively constant during the lifetime
of the structure, one speaks of a balance-sheet CDO. Necessarily the asset pool of
an arbitrage CDO consists of tradable securities such as bonds or CDSs.
There are a number of economic motivations for arranging a CDO transaction.
• The proceeds from the sale of the notes issued by the SPV are often higher
than the initial value of the asset side of the structure, as the risk–return proﬁle
of the notes is more favourable for investors. Similarly, in a synthetic CDO
the present value of the premium payments received by the SPV may exceed
the present value of the premium payments the SPV has to make. Arbitrage
CDOs are set up with the explicit purpose of exploiting this difference.
• Balance-sheet CDOs are often set up by banks who want to sell some of the
credit-risky securities on their balance sheet in order to reduce their regulatory
capital requirements; this is the typical motivation for arranging a balancesheet CLO transaction. In this way a bank can free up regulatory capital.
Stylized CDOs.
Existing CDO contracts can be quite complicated. We therefore
discuss only stylized CDOs, as this allows us to gain a better understanding of
the main qualitative features of these products without getting bogged down in
institutional details.We consider a portfolio of m different ﬁrms with cumulative loss
Lt = m
i=1 δieiYt,i.We consider a CDO with k tranches, indexed by κ ∈{1, . . . , k},
and characterized by attachment points 0 = K0 < K1 < · · · < Kk ⩽m
i=1 ei. The
valueofthenotional correspondingtotrancheκ canbedescribedasfollows.Initially,
the notional is equal to Kκ −Kκ−1; it is reduced whenever there is a default event
--- page 407 ---

9.1. Credit Derivatives
391
such that the cumulative loss falls in the layer [Kκ−1, Kκ]. In mathematical terms,
Nκ(t), the notional of tranche κ at time t, is given by
Nκ(t) = fκ(Lt)
with fκ(l) =
⎧
⎪⎨
⎪⎩
Kκ −Kκ−1,
for l < Kκ−1,
Kκ −l,
for l ∈[Kκ−1, Kκ],
0,
for l > Kκ.
(9.1)
Note that fκ can be written more succinctly as fκ(l) = (Kκ −l)+ −(Kκ−1 −l)+,
i.e. the notional is equal to the sum of a long position in a put option on Lt with
strike price Kκ and a short position in a put with strike price Kκ−1. Such positions
are sometimes called a put spread.
In a stylized CDO with maturity T as considered here, the pay-off of tranche κ is
equal to Nκ(T ). In Figure 9.3 we have graphed the pay-off for a stylized CDO with
three tranches (equity, mezzanine, senior) on a homogeneous portfolio of m = 1000
ﬁrms, each with exposure one unit. The attachment points are K1 = 20, K2 = 40,
K3 = 60, corresponding to 2%, 4% and 6% of the overall exposure; tranches with
higher attachment points are ignored. Assuming that T equals one year and that
we have a homogeneous portfolio with δi = 0.5 for all ﬁrms, we have plotted two
distributions for L1: ﬁrst, a loss distribution corresponding to a one-year default
probability of 0.5% and a default correlation of 2%; second, a loss distribution with
a one-year default probability of 0.5% but with independent defaults. In both cases
the expected loss is given by E(L1) = 25. Figure 9.3 illustrates how the value of
different CDO-tranches depends on the nature of the dependence between default
events.
• For independent defaults, L1 is typically close to its mean due to diversiﬁ-
cation effects within the portfolio. Hence it is quite unlikely that a tranche
κ with lower attachment point Kκ−1 substantially larger than E(L1) (such
as the senior tranche in Figure 9.3) suffers a loss, so the value of such a
tranche is quite high. On the other hand, since the attachment point K1 of the
equity tranche is typically lower than E(L1), it is quite unlikely that L1 is
substantially smaller than K1, and the value of the equity tranche is low.
• If defaults are (strongly) dependent, diversiﬁcation effects in the portfolio
are less pronounced. Realizations with L1 bigger than the lower attachment
point K2 of the senior tranche are more likely, as are realizations with L1
smaller than the upper attachment point K1 of the equity tranche. This reduces
the value of tranches with high seniority and increases the value of the equity
tranche compared with the case with (almost) independent defaults.
The impact of changing default correlations on mezzanine tranches is unclear and
cannot be predicted up front. The relationship between default dependence and the
value of CDO tranches carries over to the more complex structures that are actually
traded, so dependence modelling is a key issue in any model for pricing CDO
tranches.
--- page 408 ---

392
9. Dynamic Credit Risk Models
Cumulative loss
Probability
0
0
0.02
0.04
0.06
0.08
0.10
0.12
10
15
20
25
30
Pay-off of tranches
Equity
Mezzanine
Senior
20
40
60
80
100
5
Dependence
Independence
Figure 9.3.
Pay-off of a stylized CDO contract and distribution of the one-year loss L1
for a default probability of 0.5% and different default correlations. Detailed explanations are
given in the text.
Notes and Comments
In this brief introduction we have discussed a few essential features of credit derivatives, but have omitted the rather involved regulatory, legal and accounting issues
related to these instruments. Reader interested in these topics are referred to the
book by Tavakoli (2001) or the recent paper collections edited by Gregory (2003)
and Perraudin (2004); the last two references also discuss pricing issues. An excellent treatment of credit derivatives at textbook level is Sch¨onbucher (2003). The
pricing of interest swaps in the presence of default risk is discussed, for example,
in Chapter 7 of Lando (2004); a good starting point for tackling the rich literature
on pricing convertible bonds with credit risk is Chapter 9 of Dufﬁe and Singleton
(2003).
The credit derivatives market is evolving rapidly and new publications on these
instruments appear on a regular basis. The excellent website www.defaultrisk.com,
maintained by Greg Gupton, is a good place to look for new developments.
9.2
Mathematical Tools
In this section we present some mathematical tools for the analysis of reducedform credit risk models. In particular, we discuss random times (in applications,
usually the default time of a ﬁrm), hazard rates and martingale intensities. We start
with random times with deterministic hazard rates or, alternatively, with a situation
where the only observable quantity is the default time itself. This forms the basis
for an analysis of a more realistic situation where additional information, generated
for instance by economic background processes, is available, so the hazard rate will
typically be stochastic. We give a detailed treatment of doubly stochastic random
times. Doubly stochastic random times are the simplest example of random times
with stochastic hazard rates and are thus frequently used in dynamic credit risk
models.
--- page 409 ---

9.2. Mathematical Tools
393
Inouranalysisweinevitablyhavetousebasicnotionsfromthetheoryofstochastic
processes, such as ﬁltrations, stopping times or basic martingale theory. These issues
are covered in many standard textbooks on mathematical ﬁnance and probability
theory. For our purposes the technical level of Williams (1991) is sufﬁcient.
In this chapter we use the following notational convention. A generic stochastic
process in continuous time is denoted by (Xt); the rv Xt gives the value of the
process at time t ⩾0. Deterministic functions of time are denoted f (t) for t ⩾0. For
typographical reasons the notation X(t) is occasionally used for random quantities
as well. While this notation differs slightly from the conventions introduced in
Chapter 2, no confusion can arise, as we are dealing exclusively with continuoustime processes.
9.2.1
Random Times and Hazard Rates
We consider a probability space (Ω, F , P) and a random time τ deﬁned on this
space, i.e. an F -measurable rv taking values in [0, ∞], to be interpreted as the
default time of some company. By F(t) = P(τ ⩽t) we denote the df of τ and
by ¯F(t) := 1 −F(t) the tail or survival function of τ; we assume that P(τ =
0) = F(0) = 0, and that ¯F(t) > 0 for all t < ∞. We deﬁne the jump or default
indicator process (Yt) associated with τ by Yt = I{τ⩽t} for t ⩾0. Note that (Yt) is
a right-continuous process which jumps from 0 to 1 at the default time τ and that
1 −Yt = I{τ>t}.
A ﬁltration (Ft) on (Ω, F ) is an increasing family {Ft : t ⩾0} of sub-σ-algebras
of F : Ft ⊂Fs ⊂F for 0 ⩽t ⩽s < ∞. For a generic ﬁltration (Ft) we set
F∞= σ(.
t⩾0 Ft).Filtrationsareusedtomodeltheﬂowofinformationinarandom
system. Ft represents the state of knowledge of an observer at time t, and A ∈Ft
is taken to mean that at time t the observer is able to determine if the event A has
occurred. In this section we assume that the only observable quantity is the random
time τ or, equivalently, the associated jump indicator process (Yt). The appropriate
ﬁltration is therefore given by (Ht) with
Ht = σ({Yu : u ⩽t}),
(9.2)
the history of the default information up to and including time t. By deﬁnition, τ is
an (Ht)-stopping time, as {τ ⩽t} = {Yt = 1} ∈Ht for all t ⩾0; moreover, (Ht)
is obviously the smallest ﬁltration with this property.
Deﬁnition 9.1 (cumulative hazard function and hazard rate). The function
Γ (t) := −ln( ¯F(t)) is called the cumulative hazard function of the random time τ. If
F is absolutely continuous with density f , the function γ (t) := f (t)/(1 −F(t)) =
f (t)/ ¯F(t) is called the hazard rate of τ.
By deﬁnition we have F(t) = 1 −e−Γ (t) and Γ ′(t) = f (t)/ ¯F(t) = γ (t), so
Γ (t) =
 t
0 γ (s) ds. The hazard rate γ (t) can be interpreted as the instantaneous
chance of default at t, given survival up to time t. In fact, for h > 0 we have
P(τ ⩽t + h | τ > t) = (F(t + h) −F(t))/ ¯F(t). Hence we obtain
lim
h→0
1
hP(τ ⩽t + h | τ > t) =
1
¯F(t) lim
h→0
F(t + h) −F(t)
h
= γ (t).
--- page 410 ---

394
9. Dynamic Credit Risk Models
Example 9.2. Consider two popular distributions for survival times: the exponential distribution and the Weibull distribution. Recall that the df of the exponential
distribution with parameter λ equals F(t) = 1 −e−λt, so that γ (t) = λ for all
t > 0. The df of the Weibull distribution is given by F(t) = 1 −exp(−λtα) for
parameters λ, α > 0. This yields f (t) = λαtα−1 exp(−λtα) and γ (t) = λαtα−1,
which is decreasing in t if α < 1 and increasing if α > 1. For α = 1 we have the
special case of the exponential distribution.
Next we discuss conditional expectations with respect to the σ-algebra Ht. We
need the following auxiliary result on the structure of Ht-measurable rvs.
Lemma 9.3. Every Ht-measurable rv H is of the form H = h(τ)I{τ⩽t} + cI{τ>t}
for a measurable function h : [0, t] →R and some constant c ∈R.
Proof. Intuitively the result is obvious, since Ht-measurable rvs can be expressed
as functions of events related to the default history at t. More formally, we argue as
follows. The σ-algebra Ht is generated by the events {Yu = 1} = {τ ⩽u}, u < t,
and {Yt = 0} = {τ > t}, and hence by the rvs min{τ, t} =: (τ ∧t) and I{τ>t}. This
implies that any Ht-measurable rv H can be written as H = g(τ ∧t, I{τ>t}) for
some measurable function g : [0, t] × {0, 1} →R. The claim follows if we deﬁne
h(u) := g(u, 0), u ⩽t, and c := g(t, 1).
Lemma 9.4. Let τ be a random time with jump indicator process Yt = I{τ⩽t} and
natural ﬁltration (Ht). Then, for any integrable rv X and any t ⩾0, we have
E(I{τ>t}X | Ht) = I{τ>t}
E(X; τ > t)
P(τ > t) .
(9.3)
Proof. Since E(I{τ>t}X | Ht) is Ht-measurable and zero on {τ
⩽t}, we
obtain from Lemma 9.3 that E(I{τ>t}X | Ht) = I{τ>t}c for some constant c.
Taking expectations yields E(X; τ
> t) = cP(τ
> t) and hence c
=
E(X; τ > t)/P(τ > t).
As an example we compute conditional survival probabilities. Taking X := I{τ>s}
for s > t in (9.3), we get
P(τ > s | Ht) = E(X | Ht) = E(I{τ>t}X | Ht) = I{τ>t}
¯F(s)
¯F(t) .
(9.4)
The next proposition contains the ﬁrst result on the stochastic-process properties
of the jump indicator process of a random time τ. Let (Ft) be a generic ﬁltration.An
(Ft)-adapted and integrable process (Mt) is called an (Ft)-martingale if E(Ms |
Ft) = Mt for all 0 ⩽t ⩽s, i.e. if the current value Mt is the best prediction (in the
mean square sense) of the future value Ms.
Proposition 9.5. Let τ be a random time with absolutely continuous df F(t)
and hazard-rate function γ (t). Then Mt := Yt −
 t∧τ
0
γ (s) ds, t ⩾0, is an (Ht)-
martingale.
--- page 411 ---

9.2. Mathematical Tools
395
Here and below τ ∧t is short for min{τ, t}. In Section 9.2.3 we extend this
result to doubly stochastic random times and discuss its ﬁnancial and mathematical
relevance.
Proof. Let s > t. We have to show that E(Ms −Mt | Ht) = 0, i.e. that
E(Ys −Yt | Ht) = E(
 s
t γ (u)I{u<τ} du | Ht). Using (9.4), we get
E(Ys −Yt | Ht) = I{τ>t}P(τ ⩽s | Ht) = I{τ>t}

1 −
¯F(s)
¯F(t)

= I{τ>t}
¯F(t) −¯F(s)
¯F(t)
.
Note that X :=
 s
t γ (u)I{u<τ} du is zero on {τ ⩽t}, so X = XI{τ>t}. Hence
we obtain from Lemma 9.4, Fubini’s Theorem and the identity ¯F ′(t) = −f (t) =
−γ (t) ¯F(t) that
E(X | Ht) = I{τ>t}
E(X)
¯F(t) = I{τ>t}
 s
t γ (u) ¯F(u) du
¯F(t)
= I{τ>t}
¯F(t) −¯F(s)
¯F(t)
,
and the result follows.
9.2.2
Modelling Additional Information
We now consider a situation where additional information affecting the distribution
of τ is available. In the context of credit risk models this information is typically
generated by background processes, often modelled as diffusions or continuoustime Markov chains, representing, for instance, economic activity in a country or in
an industry sector, risk-free interest rates or rating transitions between non-default
states. Formally, we represent this additional information by some ﬁltration (Ft)
on (Ω, F , P).
Deﬁnition 9.6 (cumulative hazard and hazard-rate processes). Let τ be a random time on the ﬁltered probability space (Ω, F , (Ft), P) with P(τ > 0) = 1.
Let Ft = P(τ ⩽t | Ft) and ¯Ft = 1 −Ft. If Ft < 1 for all t ⩾0, the (Ft)-
conditional cumulative hazard process (Γt) is deﬁned by Γt := −ln( ¯Ft). If (Γt)
is strictly increasing and absolutely continuous, i.e. Γt =
 t
0 γs ds for some a.s.
strictly positive, (Ft)-adapted process (γt), then we call (γt) the (Ft)-conditional
hazard-rate process of τ.
Recall the deﬁnition of the ﬁltration (Ht) in (9.2) and introduce a new ﬁltration
(Gt) by
Gt = Ft ∨Ht,
t ⩾0,
(9.5)
meaning that Gt is the smallest σ-algebra that contains Ft and Ht. Obviously τ is
an (Ht) stopping time and hence also a (Gt)-stopping time. In the context of credit
risk models the ﬁltration (Gt) contains information about the background processes
and the occurrence or non-occurrence of default up to time t, and thus typically
corresponds to the information available to investors.
--- page 412 ---

396
9. Dynamic Credit Risk Models
Remark 9.7. The notion of an (Ft)-conditional hazard-rate process is most useful
for the doubly stochastic random times discussed in Section 9.2.3 below. Note that if
we assume that Ft < 1 for all t > 0 so that (Γt) is well deﬁned, τ cannot be an (Ft)-
stopping time. Otherwise we would have Ft = P(τ ⩽t | Ft) = I{τ⩽t} ∈{0, 1}, as
{τ ⩽t} ∈Ft by the deﬁnition of a stopping time.An important example of a random
time, which does not admit a conditional cumulative hazard process, is provided by
the ﬁrst exit time of Brownian motion from some layer. More precisely, let (Wt) be
standard Brownian motion and let (Ft) be the ﬁltration generated by (Wt). Consider
some threshold a < 0 and deﬁne τa = inf{t ⩾0 : Wt ⩽a}. It is well known that τa
is an (Ft)-stopping time, so the (Ft)-conditional cumulative hazard process is not
well deﬁned. A similar argument shows that the default time in a ﬁrst-passage-time
model (see Section 8.2) does not admit a cumulative hazard process (with respect to
the ﬁltration generated by the ﬁrm-value process); hence the results derived below
do not apply to those models.
Conditional expectations.
Next we extend the results of Section 9.2.1 and discuss the structure of conditional expectations with respect to the full-information
σ-algebra Gt. We need the following auxiliary result on the relationship between
the σ-algebras Ft and Gt.
Lemma 9.8. For every Gt-measurable rv X there is some Ft-measurable rv ˜X such
that XI{τ>t} = ˜XI{τ>t}.
In economic terms this result tells us that before default all information is generated by the background ﬁltration (Ft); we omit a formal proof. Now we turn to
conditional expectations with respect to Gt.
Lemma 9.9. For every integrable rv X we have
E(I{τ>t}X | Gt) = I{τ>t}
E(I{τ>t}X | Ft)
P(τ > t | Ft) .
Note that Lemma 9.9 allows us to replace certain conditional expectations with
respect to Gt by conditional expectations with respect to the background information Ft.
Proof. E(I{τ>t}X | Gt) is Gt-measurable and zero on {τ ⩽t}. By Lemma 9.8 there
is therefore an Ft-measurable rv ˜Z such that E(I{τ>t}X | Gt) = I{τ>t} ˜Z. Taking
conditional expectations with respect to Ft yields, as Ft ⊂Gt,
E(I{τ>t}X | Ft) = P(τ > t | Ft) ˜Z.
Hence ˜Z = E(I{τ>t}X | Ft)/P(τ > t | Ft), which proves the lemma.
Corollary 9.10. Let s > t. If ˜X is integrable and Fs-measurable, we have
E(I{τ>s} ˜X | Gt) = I{τ>t}E(e−(Γs−Γt) ˜X | Ft).
--- page 413 ---

9.2. Mathematical Tools
397
Proof. Let X := I{τ>s} ˜X. Since X = I{τ>t}X (as s > t), Lemma 9.9 yields
E(I{τ>s} ˜X | Gt) = E(I{τ>t}X | Gt) = I{τ>t}eΓt E(I{τ>s} ˜X | Ft),
where we have used the fact that P(τ > t | Ft) = e−Γt . Since ˜X is Fs-measurable,
E(I{τ>s} ˜X | Ft) = E( ˜XP(τ > s | Fs) | Ft) = E( ˜Xe−Γs | Ft),
and the result follows.
Corollary 9.10 will be useful in the pricing of corporate bonds. Suppose that the
default time τ admits the conditional hazard-rate process (γt), that the default-free
interest rate (rt) is adapted to the background ﬁltration (Ft), and that P represents
the probability measure used for pricing (to be explained in Section 9.3). Consider
a corporate zero-coupon bond with zero recovery and maturity T > t; at maturity
its value is given by I{τ>T }. Deﬁne ˜X := exp(−
 T
t rs ds); the price at time t of our
bond is hence given by E(I{τ>T } ˜X | Gt). We get, from Corollary 9.10,
E(I{τ>T } ˜X | Gt) = I{τ>t}E

exp

−
 T
t
(rs + γs) ds
 				 Ft

.
Expressions of this type are often easily computed using techniques from standard
default-free term structure models (for details we refer to Sections 9.4.3 and 9.5
below).
Corollary 9.10 moreover implies that in the above setting γt gives a good approximation of the one-year default probability in the following sense. We have
P(τ > t + 1 | Gt) = I{τ>t}E

exp

−
 t+1
t
γs ds
 				 Ft

.
(9.6)
Suppose now that the hazard rate remains relatively stable over time so that P(γs ≈
γt for all s ∈[t, t + 1]) is close to one and that τ > t. Under these assumptions, the
right-hand side of (9.6) is approximated reasonably well by exp(−γt). If γt is not
too large, we thus get on {τ > t} for the one-year default probability
P(τ < t + 1 | Gt) ≈1 −exp(−γt) ≈γt.
(9.7)
9.2.3
Doubly Stochastic Random Times
Doubly stochastic random times—also called conditional Poisson or Cox random
times in the literature—are the main example of random times with a stochastic
hazard rate. For our analysis of these random times we use the framework introduced
in the previous section. In particular, (Ft) denotes the background ﬁltration, (Ht) is
the ﬁltration generated by the jump indicator process associated with the random
time τ, and the ﬁltration (Gt) is deﬁned by Gt = Ft ∨Ht.
Deﬁnition 9.11 (doubly stochastic random time). A random time τ is called
doubly stochastic with respect to the background ﬁltration (Ft) if τ admits the (Ft)-
conditional hazard-rate process (γt), if Γt =
 t
0 γs ds is strictly increasing, and if,
for all t > 0,
P(τ ⩽t | F∞) = P(τ ⩽t | Ft).
(9.8)
--- page 414 ---

398
9. Dynamic Credit Risk Models
Condition (9.8) is most easily interpreted if we assume that the background ﬁltration is generated by some stochastic state variable process (Ψt), i.e. if Ft = σ({Ψu :
u ⩽t}). In that case (9.8) states that, given past values (Ψu)u⩽t of the state variable, the future (Ψs)s>t does not contain any extra information for predicting the
probability that τ occurs before time t. Obviously, (9.8) excludes models where the
probability that τ ⩽t depends on the future evolution (Ψs)s>t of the state variable.
Construction and simulation via thresholds.
In the next lemma we give an explicit
construction of a doubly stochastic random time. This construction is very useful
for simulation purposes.
Lemma 9.12. Let E be a standard exponentially distributed rv on (Ω, F , P) independent of F∞, i.e. P(E ⩽t | F∞) = 1 −e−t for all t ⩾0. Let (γt) be a positive
(Ft)-adapted process such that Γt =
 t
0 γs ds is strictly increasing and ﬁnite for
every t > 0. Deﬁne the random time τ by
τ := Γ −1(E) = inf{t ⩾0 : Γt ⩾E}.
(9.9)
Then τ is doubly stochastic with (Ft)-conditional hazard-rate process (γt).
Proof. We have, by deﬁnition,
P(τ ⩽t | F∞) = P(Γt ⩾E | F∞) = 1 −exp(−Γt),
since Γt is F∞-measurable and E is independent of F∞. Moreover, since 1 −
exp(−Γt) is Ft-measurable, we get, using iterated conditional expectations,
P(τ ⩽t | Ft) = E(P(τ ⩽t | F∞) | Ft) = 1 −exp(−Γt),
which proves the claim.
Lemma 9.12 has a converse, which is presented next.
Lemma 9.13. Let τ be a doubly stochastic random time with (Ft)-conditional
hazard-rate process (γt). Denote by Γt =
 t
0 γs ds the conditional cumulative hazard
process of τ and put E := Γτ. Then the rv E is standard exponentially distributed
and independent of F∞, and τ = Γ −1(E) almost surely.
Proof. Since (Γt) is strictly increasing by assumption, the relation τ = Γ −1(E) is
clear from the deﬁnition of E. To prove that E has the correct distribution we argue
as follows:
P(E ⩽t | F∞) = P(Γτ ⩽t | F∞) = P(τ ⩽Γ −1(t) | F∞).
Since τ is doubly stochastic, the last expression equals 1 −exp(−Γ (Γ −1(t))) =
1 −e−t, which shows that E is independent of F∞and that it is standard exponentially distributed.
Lemma 9.12 forms the basis for the following algorithm for the simulation of
doubly stochastic random times.
--- page 415 ---

9.2. Mathematical Tools
399
10
0
0
0.2
0.4
0.6
0.8
E
Γ
τ
2
4
6
8
Time
Figure 9.4.
A graphical illustration of Algorithm 9.14: E ≈0.44, τ ≈6.59.
Algorithm 9.14 (univariate threshold simulation).
(1) Generate a trajectory of the hazard-rate process (γt). References for suitable
simulation approaches are given in Notes and Comments.
(2) Generate a unit exponential rv E independent of (γt) (the threshold) and set
τ = Γ −1(E); this step is illustrated in Figure 9.4.
Moreover, Lemmas 9.12 and 9.13 provide an interesting interpretation of doubly stochastic random times in terms of operational time: for a given (Ft)-adapted
hazard-rate process (γt), deﬁne a new timescale (operational time) by the associated
cumulative hazard process Γt =
 t
0 γs ds, so that c units of operational time correspond to Γ −1(c) units of real time. Take a standard exponential rv E independent of
F∞and measure time in units of operational time. Then the associated calendar time
τ := Γ −1(E) is doubly stochastic by Lemma 9.12. Conversely, by Lemma 9.13, if
we take a doubly stochastic random time τ, the associated operational time E := Γτ
is standard exponential, independent of F∞. The notion of operational time plays
an important role in insurance mathematics (see Section 10.2.7).
Martingale intensity of doubly stochastic random times.
We have seen in Proposition 9.5 that the jump indicator process (Yt) can be turned into an (Ht)-martingale
if we subtract the process
 t∧τ
0
γ (s) ds. Here we generalize this result to doubly
stochastic random times.
Proposition 9.15. Let τ be a doubly stochastic random time with (Ft)-conditional
hazard-rate process (γt). Then Mt := Yt −
 t∧τ
0
γs ds is a (Gt)-martingale.
Proof. Deﬁne a new artiﬁcial ﬁltration ( ˜Gt) by ˜Gt = F∞∨Ht; in particular, ˜G0 =
F∞and Gt ⊂˜Gt for all t. Conditioning on ˜G0 turns τ into a random time with
deterministic hazard rate γ (s): we have
P(τ ⩽t | ˜G0) = 1 −exp

−
 t
0
γs ds

,
--- page 416 ---

400
9. Dynamic Credit Risk Models
and γ is known given ˜G0. Hence Proposition 9.5 implies that Mt := Yt −
 t∧τ
0
γs ds
is a martingale with respect to ( ˜Gt). Since (Mt) is (Gt)-adapted and Gt ⊂˜Gt, (Mt) is
also a martingale with respect to (Gt).
We conclude with a brief discussion on Proposition 9.15 from the viewpoint of
stochastic calculus.
Deﬁnition 9.16. Given the set-up of Section 9.2.2, a non-negative (Gt)-adapted
process (λt) is called a (Gt)-martingale intensity process of the random time τ if
Mt := Yt −
 t∧τ
0
λs ds is a (Gt)-martingale.
In reduced-form credit risk models, (λt) is usually called the default intensity of
the default time τ. It is well known that the martingale intensity (λt) is uniquely
deﬁned on {t < τ}. This is an immediate consequence of general results from
stochastic calculus concerning the uniqueness of semimartingale decompositions
(see, for example, Chapter 2 of Protter (1992)). Martingale intensities are important
tools in the analysis of jump indicators and random times from the viewpoint of
stochastic calculus. In credit risk, martingale default intensities and credit spreads
of defaultable bonds are closely related, as will be discussed in Section 9.4 below.
Using the terminology of Deﬁnition 9.16, we may restate Proposition 9.15 in
the form “the (Gt)-martingale intensity of a doubly stochastic random time τ is
given by its (Ft)-conditional hazard-rate process (γt)”. Outside the realm of doubly
stochastic random times, the relationship between martingale default intensities and
hazard-rate processes becomes more subtle. In fact, in the analysis of reduced-form
credit portfolios one naturally encounters random times which admit a martingale
intensity process in the sense of Deﬁnition 9.16, but whose conditional cumulative
hazard process Γt is not absolutely continuous, for instance because it has jumps.
In that case Proposition 9.15 obviously no longer holds.
Notes and Comments
The material discussed in this section is treated in various sources; our presentation
is based on the book by Bielecki and Rutkowski (2002), where many extensions of
our results can also be found. In particular, Bielecki and Rutkowski discuss various
probabilistic characterizations of doubly stochastic random times. The thresholdsimulation approach for doubly stochastic random times requires the simulation of
trajectories of the hazard-rate process.An excellent source for simulation techniques
for stochastic processes is Glasserman (2003a).
Moregeneralreduced-formmodelswherethedefaulttimeτ isnotdoublystochastic are discussed, for example, in Kusuoka (1999), Elliot, Jeanblanc andYor (2000),
B´elanger, Shreve and Wong (2004), Collin-Dufresne, Goldstein and Hugonnier
(2004) and in Chapter 7 of Bielecki and Rutkowski (2002).
9.3
Financial and Actuarial Pricing of Credit Risk
Essentially, two approaches are used for the pricing of credit-risky securities: the
ﬁnancial or risk-neutral pricing approach on the one hand, and the actuarial pricing
--- page 417 ---

9.3. Financial and Actuarial Pricing
401
.
.
.
0.941
1.0 (no default)
0.6 (default, recovery = 60%)
Figure 9.5.
Evolution of the price of p1(· , 1) in Example 9.17.
approach on the other. Under the risk-neutral pricing approach, prices are computed as expected discounted values under some equivalent martingale measure
(see below). This approach is based on the notions of absence of arbitrage and
dynamic hedging. Nowadays, the risk-neutral pricing approach is standard for pricing non-defaultable securities. In credit risk it is used for pricing traded securities
such as corporate bonds and credit default swaps and derivative securities related to
these products.
In the actuarial approach, prices are computed as the sum of the expected pay-off
under the physical measure and a risk premium. The size of the risk premium is
often related to the notion of economic capital. In credit risk, the actuarial approach
is applied mainly to the pricing of non-traded loans or structured products related
to illiquid securities.
In this section we discuss and compare both approaches with a view towards
pricing credit-risky securities. Our discussion provides the methodological basis for
the derivation of pricing formulas in subsequent sections.
9.3.1
Physical and Risk-Neutral Probability Measure
We begin with a discussion of the relationship between the real-world or physical
measure, which models the actual probability of default, and an equivalent martingale measure or risk-neutral measure. We use the following simple example as a
vehicle for our analysis.
Example 9.17 (the basic static model). We consider a defaultable zero-coupon
bond with maturity T equal to one year. We assume that the recovery rate 1 −δ is
deterministic and equal to 60%; that the real-world default probability is equal to
¯p = 1%; and that the risk-free simple interest rate equals 5%. Moreover, we assume
that the current (t = 0) price of the bond equals p1(0, 1) = 0.941; and that the price
of the corresponding default-free bond is p0(0, 1) = (1.05)−1 = 0.952. The price
evolution of the bond is depicted in Figure 9.5.
The expected discounted value of the bond equals (1.05)−1(0.99·1+0.01·0.6) =
0.949 > p1(0, 1). We see that the price p1(0, 1) is smaller than the expected discounted value of the claim. This is the typical situation in real markets for corporate
bonds, as investors demand a premium for bearing the default risk of the bond. In
real markets, the price of corporate bonds is also affected by tax issues (interest
income from corporate bonds is often taxed at a higher rate than interest income
on treasury bonds) and by liquidity issues; both factors tend to further decrease the
price of corporate bonds relative to treasury bonds. An equivalent martingale measure or risk-neutral measure is an artiﬁcial measure Q equivalent to the physical
probability measure P such that the discounted price process of any security is a
--- page 418 ---

402
9. Dynamic Credit Risk Models
Q-martingale.According to a standard result of mathematical ﬁnance (the so-called
ﬁrst fundamental theorem of asset pricing), a model for security prices is arbitrage
free if and, modulo technicalities, only if it admits at least one equivalent martingale measure Q. In our two-state model, Q is simply given by an artiﬁcial default
probability ¯q such that p1(0, 1) = (1.05)−1((1 −¯q) · 1 + ¯q · 0, 6); ¯q is uniquely
determined from this equation and is given by ¯q = 0.03. Note that in our example ¯q
is bigger than the physical default probability ¯p = 0.01; again this is typical for real
markets and reﬂects the risk premium demanded by buyers of defaultable bonds.
The risk-neutral default probability ¯q is closely related to the credit spread of
the defaultable bond (see (8.11)). Since c(0, 1) = −(ln p1(0, 1) −ln p0(0, 1)), we
obtain, in our two-state model,
c(0, 1) = −ln((1 −¯q) · 1 + ¯q · 0.6) = −ln(1 −¯q · 0.4) ≈¯q · 0.4,
i.e. the credit spread is approximately equal to the product of default probability and
(percentage) loss given default. Similar relationships hold in more general reducedform credit risk models (see Section 9.4.2 below). Hence spread data for corporate
bonds can be used to estimate risk-neutral default probabilities. This observation
forms the basis for many empirical studies on the relationship between physical and
risk-neutral default probabilities; we discuss the ﬁndings of a recent extensive study
below.
From physical to risk-neutral default probabilities.
How does the structure of
credit risk models and hence default probabilities change if we go from the physical
measure (labelled P) to a risk-neutral measure (labelled Q)? A concise mathematical answer to this question requires the use of sophisticated tools from stochastic
calculus (variants of Girsanov’s theorem for diffusions and point processes) and is
beyond the scope of this book. We therefore content ourselves with an informal
discussion of the transition from physical to risk-neutral probabilities in ﬁrm-value
and reduced-form models.
In ﬁrm-value models such as Merton’s model (see Section 8.2.1), when going
from P to Q the drift of the asset-value process V is changed from some arbitrary µ
to the default-free short rate of interest r. According to (8.4), in Merton’s model the
physical default probability over the interval [0, T ] is given by
¯p = P(VT ⩽F) = Φ
ln F −ln V0 −(µ −1
2σ 2)T
σ
√
T

;
the risk-neutral default probability over the same horizon is
¯q = Q(VT ⩽F) = Φ
ln F −ln V0 −(r −1
2σ 2)T
σ
√
T

.
We obtain from these equations that
¯q = Φ

Φ−1( ¯p) + µ −r
σ
√
T

.
(9.10)
Note that the correction term (µ −r)/σ equals the Sharpe ratio of V (a popular
measure of the risk premium earned by the ﬁrm). The transition formula (9.10) is
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
