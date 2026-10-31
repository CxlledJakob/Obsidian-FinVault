# Quantitative Risk Management_ Concepts, Techniques, and -- Alexander J_ McNeil, Rüdiger Frey, Paul Embrechts -- Princeton series in finance, -- isbn13 9780691122557 -- 478a0059673fecd0c76229cd3d8884e7 -- Anna’s Arc.pdf — pages 39–58

--- page 39 ---

1.5. Quantitative Risk Management
23
A speculative view of where these developments may lead is given by Shiller
(2003), who argues that the proliferation of RM thinking coupled with the technological sophistication of the twenty-ﬁrst century will allow any agent in society,
from a company to a country to an individual, to apply QRM methodology to the
risks they face. In the case of an individual this may be the risk of unemployment,
depreciation in the housing market or the investment in the education of children.
Notes and Comments
The language of probability and statistics plays a fundamental role throughout the
book and readers are expected to have a good knowledge of these subjects. At the
elementary level, Rice (1995) gives a good ﬁrst introduction to both of these. More
advanced texts in probability and stochastic processes are Williams (1991), Resnick
(1992) and Rogers and Williams (1994); the full depth of these texts is certainly not
required for the understanding of this book, though they provide excellent reading
material for the mathematically more sophisticated reader who also has an interest
in mathematical ﬁnance. Further recommended texts on statistical inference include
Casella and Berger (2002), Bickel and Doksum (2001), Davison (2003) and Lindsey
(1996).
An excellent text on the history of risk and probability with ﬁnancial applications
in mind is Bernstein (1998). Additional useful material on the history of the subject
is to be found in Field (2003).
For the mathematical reader looking to acquire more knowledge of relevant
economics we recommend Mas-Colell, Whinston and Green (1995) for microeconomics; Campbell, Lo and MacKinlay (1997) or Gourieroux and Jasak (2001)
for econometrics; and Brealey and Myers (2000) for corporate ﬁnance. From the
vast literature on options, an entry-level text for the general reader is Hull (1997).
At a more mathematical level we like Bingham and Kiesel (1998) and Musiela and
Rutkowski (1997). One of the most readable texts on the basic notion of options is
Cox and Rubinstein (1985). For a rather extensive list of the kind of animals to be
found in the zoological garden of derivatives, see, for example, Haug (1998).
There are several texts on the spectacular losses due to speculative trading and
careless use of derivatives. The LTCM case is well documented in Dunbar (2000),
Lowenstein (2000) and Jorion (2000), the latter particularly for the technical riskmeasurement issues involved. Boyle and Boyle (2001) give a very readable account
of the Orange County, Barings and LTCM stories. A useful website on RM, containing a growing collection of industry case studies, is www.erisk.com.
An overview of options embedded in life insurance products is given in Dillmann
(2002), guarantees are discussed in detail in Hardy (2003), and Briys and deVarenne
(2001) contains an excellent account of RM issues facing the (life) insurance industry.
The historical development of banking regulation is well described in Crouhy,
Galai and Mark (2001) and Steinherr (1998). For details of the current rules and
regulations coming from the Basel Committee, see its website at www.bis.org/bcbs.
--- page 40 ---

24
1. Risk in Perspective
Besides copies of the various accords, one also ﬁnds useful working papers, publications and comments written by stakeholders on the various consultative packages.
For Solvency 2, many documents are being prepared, and the Web is the best place
to start looking; a forthcoming text is Sandstr¨om (2005). The complexity of RM
methodology in the wake of Basel II is critically addressed by Hawke (2003), in his
capacity as US Comptroller of the Currency.
For a very detailed overview of relevant practical issues underlying RM we again
strongly recommend Crouhy, Galai and Mark (2001).A text stressing the use ofVaR
as a risk measure and containing several worked examples is Jorion (2001), who also
has a useful teaching manual on the same subject (Jorion 2002a). Insurance-related
issues in RM are well presented in Doherty (2000).
For a comprehensive discussion of the management of bank capital given regulatory constraints see Matten (2000). Graham and Rogers (2002) contains a discussion
of RM and tax incentives. A formal account of the Modigliani–Miller Theorem and
its implication can be found in many textbooks on corporate ﬁnance: a standard
reference is Brealey and Myers (2000); de Matos (2001) gives a more theoretical
account from the perspective of modern ﬁnancial economics. Both texts also discuss
the implications of informational asymmetries between the various stakeholders in
a corporation. Formal models looking at RM from a corporate ﬁnance angle are to
be found in Froot and Stein (1998), Froot, Scharfstein and Stein (1993) and Stulz
(1996, 2002). For a speciﬁc discussion on corporate ﬁnance issues in insurance see
Froot (2005) and Hancock, Huber and Koch (2001).
There are several studies on the use of RM techniques for non-ﬁnancial ﬁrms
(see, for example, Bodnar, Hyat and Marston 1999; Geman 2005). Two references
in the area of reliability of industrial processes are Bedford and Cooke (2001) and
Does, Roes and Trip (1999). An interesting edited volume on alternative risk transfer (ARTs) is Shimpi (1999); a detailed study of model risk in the ART context is
Schmock (1999).An area we have not mentioned so far in our discussion of QRM in
the future is that of real options. A real option is the right, but not the obligation, to
take an action (e.g. deferring, expanding, contracting or abandoning) at a predetermined cost called the exercise price for a predetermined period of time—the life of
the option. This deﬁnition is taken from Copeland and Antikarov (2001). Examples
of real options discussed in the latter are the valuation of an internet project and of
a pharmaceutical research and development project. A further useful reference is
Brennan and Trigeorgis (2000).
--- page 41 ---

2
Basic Concepts in Risk Management
In this chapter we discuss essential concepts in quantitative risk management. We
begin by introducing a probabilistic framework for modelling ﬁnancial risk and we
give formal deﬁnitions for notions such as risk, proﬁt and loss, risk factors and
mapping. Moreover, we discuss a number of examples from the areas of market and
credit risk, illustrating how typical risk-management problems ﬁt into the general
framework.
A central issue in modern risk management is the measurement of risk. As
explained in Chapter 1, the need to quantify risk arises in many different contexts. For instance, a regulator measures the risk exposure of a ﬁnancial institution
in order to determine the amount of capital that institution has to hold as a buffer
against unexpected losses. Similarly, the clearing house of an exchange needs to set
margin requirements for investors trading on that exchange. In Section 2.2 we give
an overview of the existing approaches to measuring risk and discuss their strengths
and weaknesses. Particular attention will be given to Value-at-Risk and the related
notion of expected shortfall.
In Section 2.3 we present some standard methods used in the ﬁnancial industry
for measuring market risk over a short horizon, such as the variance–covariance
method, the historical-simulation method and methods based on Monte Carlo simulation.We consider the use of scaling rules for transforming one-period risk-measure
estimates into estimates for longer time horizons and give a short discussion of backtesting approaches for monitoring the performance of risk-measurement systems.
We conclude with an example of the application of standard methodology.
2.1
Risk Factors and Loss Distributions
2.1.1
General Deﬁnitions
We represent the uncertainty about future states of the world by a probability space
(Ω, F , P), which is the domain of all random variables (rvs) we introduce below.
Consider a given portfolio such as a collection of stocks or bonds, a book of derivatives, a collection of risky loans or even a ﬁnancial institution’s overall position in
risky assets. We denote the value of this portfolio at time s by V (s) and assume that
the rv V (s) is observable at time s. For a given time horizon , such as 1 or 10 days,
the loss of the portfolio over the period [s, s + ] is given by
L[s,s+] := −(V (s + ) −V (s)).
--- page 42 ---

26
2. Basic Concepts in Risk Management
While L[s,s+] is assumed to be observable at time s+, it is typically random from
the viewpoint of time s. The distribution of L[s,s+] is termed the loss distribution.
We distinguish between the conditional loss distribution, i.e. the distribution of
L[s,s+] given all available information up to and including time s, and the unconditional loss distribution; this issue is taken up in more detail below.
Remark 2.1. Practitioners in risk management are often concerned with the socalled proﬁt-and-loss (P&L) distribution. This is the distribution of the change in
value V (s + ) −V (s), i.e. of the rv −L[s,s+]. However, in risk management
we are mainly concerned with the probability of large losses and hence with the
upper tail of the loss distribution. Hence we often drop the P from P&L, both in
notation and language. It is a standard convention in statistics to present results on
tail estimation for the upper tail of distributions. Moreover, actuarial risk theory is a
theory of positive rvs. Hence our focus on loss distributions facilitates the application
of techniques from these ﬁelds.
In most parts of the book we consider a ﬁxed horizon . In that case it will be convenient to measure time in units of  and to introduce a time series notation, where
we move from a generic process Y(s) to the time series (Yt)t∈N with Yt := Y(t).
Using this notation the loss is written as
Lt+1 := L[t,(t+1)] = −(Vt+1 −Vt).
(2.1)
For instance, in market risk management we often work with ﬁnancial models where
the calendar time s is measured in years and interest rates and volatilities are quoted
on an annualized basis. If we are interested in daily losses we set  = 1/365 or
 ≈1/250; the latter convention is mainly used in markets for equity derivatives
since there are approximately 250 trading days per year. The rvs Vt and Vt+1 then
represent the portfolio value on days t and t + 1, respectively, and Lt+1 is the loss
from day t to day t + 1.
Following standard risk-management practice the value Vt is modelled as a function of time and a d-dimensional random vector Zt = (Zt,1, . . . , Zt,d)′ of risk factors, i.e. we have the representation
Vt = f (t, Zt)
(2.2)
for some measurable function f : R+ ×Rd →R. Risk factors are usually assumed
to be observable so that Zt is known at time t. The choice of the risk factors and
of f is of course a modelling issue and depends on the portfolio at hand and on
the desired level of precision. Frequently used risk factors are logarithmic prices
of ﬁnancial assets, yields and logarithmic exchange rates. A representation of the
portfolio value in the form (2.2) is termed a mapping of risks. Some examples of
the mapping of standard portfolios are provided below.
It will be convenient to deﬁne the series of risk-factor changes (Xt)t∈N by Xt :=
Zt −Zt−1; they are the objects of interest in most statistical studies of ﬁnancial time
series. Using the mapping (2.2) the portfolio loss can be written as
Lt+1 = −(f (t + 1, Zt + Xt+1) −f (t, Zt)).
(2.3)
--- page 43 ---

2.1. Risk Factors and Loss Distributions
27
Since Zt is known at time t, the loss distribution is determined by the distribution
of the risk-factor change Xt+1. We therefore introduce another piece of notation,
namely the loss operator l[t] : Rd →R, which maps risk-factor changes into losses.
It is deﬁned by
l[t](x) := −(f (t + 1, Zt + x) −f (t, Zt)),
x ∈Rd,
(2.4)
and we obviously have Lt+1 = l[t](Xt+1).
If f is differentiable, we consider a ﬁrst-order approximation L
t+1 of the loss in
(2.3) of the form
L
t+1 := −

ft(t, Zt) +
d

i=1
fzi(t, Zt)Xt+1,i

,
(2.5)
where the subscripts to f denote partial derivatives. The notation L stems from the
standard delta terminology in the hedging of derivatives (see Example 2.5 below).
The linearized loss operator corresponding to (2.5) is given by
l
[t](x) := −

ft(t, Zt) +
d

i=1
fzi(t, Zt)xi

.
(2.6)
The ﬁrst-order approximation is convenient as it allows us to represent the loss as
a linear function of the risk-factor changes. The quality of the approximation (2.5)
is obviously best if the risk-factor changes are likely to be small (i.e. if we are
measuring risk over a short horizon) and if the portfolio value is almost linear in the
risk factors (i.e. if the function f has small second derivatives).
Remark 2.2. In developing formulas (2.2)–(2.6) we have assumed that time is
measured in units of the horizon . In order to be in line with market convention
in our examples it will sometimes be convenient to consider mappings of the form
g(s, Z), where time s is measured in years; in that case, equations (2.2) and (2.3)
become, respectively, Vt = f (t, Zt) = g(t, Zt) and
Lt+1 = −(g((t + 1), Zt + Xt+1) −g(t, Zt)),
where  gives the length of the risk-management horizon in years. Care must be
taken with the linearized version of the loss in (2.5), which becomes
L
t+1 := −

gs(t, Zt) +
d

i=1
gzi(t, Zt)Xt+1,i

.
(2.7)
Note that, when working with a short time horizon , the term gs(t, Zt) in (2.7)
is very small and is therefore often dropped in practice.
Remark 2.3. Note that our deﬁnition of the portfolio loss implicitly assumes that
the composition of the portfolio remains unchanged over the time horizon . While
unproblematic for daily losses this assumption becomes increasingly unrealistic for
longer time horizons. This is a problem for non-ﬁnancial corporations like insurance
companies;suchcompaniesmayprefertomeasuretheriskoftheirﬁnancialportfolio
--- page 44 ---

28
2. Basic Concepts in Risk Management
over a one-year horizon, which is the appropriate horizon for dealing with their usual
business risks. We note also that in the context of the Basel Accords, discussed in
Chapter 1, it is formally required that calculations for banks be made under the
assumption that the portfolio composition remains unchanged over a holding period
 (10 days in the case of market risk).
2.1.2
Conditional and Unconditional Loss Distribution
As mentioned earlier, in risk management we often have to decide if we are interested
in the conditional or the unconditional distribution of losses. Both are relevant for
risk-management purposes, but it is important to be aware of the distinction between
the two concepts.
The differences between conditional and unconditional loss distributions are
strongly related to time series properties of the series of risk-factor changes (Xt)t∈N.
Suppose that the risk-factor changes form a stationary time series with stationary
distribution FX on Rd. Essentially, this means that the distribution of (Xt)t∈N is
invariant under shifts of time (see Chapter 4 for details) and most time series models
used in practice for the modelling of risk-factor changes satisfy this property. Now
ﬁx a point in time t (current time), and denote by Ft the sigma ﬁeld representing
the publicly available information at time t. Typically, Ft = σ({Xs : s ⩽t}), the
sigma ﬁeld generated by past and present risk-factor changes, often called the history, up to and including time t. Denote by FXt+1|Ft the conditional distribution of
Xt+1 given current information Ft. In most stationary time series models relevant
for risk management, FXt+1|Ft is not equal to the stationary distribution FX. An
important example is provided by the popular models from the GARCH family (see
Section 4.3). In this class of model the variance of the conditional distribution of
Xt+1 is a function of past risk-factor changes and possibly of its own lagged values.
On the other hand, if (Xt)t∈N is an independent and identically distributed (iid)
series, we obviously have FXt+1|Ft = FX.
Fix the loss operator l[t] corresponding to the portfolio currently under consideration. The conditional loss distribution FLt+1|Ft is deﬁned as the distribution of the
loss operator l[t](·) under FXt+1|Ft . Formally we have, for l ∈R,
FLt+1|Ft (l) = P(l[t](Xt+1) ⩽l | Ft) = P(Lt+1 ⩽l | Ft),
i.e. the conditional loss distribution gives the conditional distribution of the loss Lt+1
in the next time period given current information Ft. Conditional distributions are
particularly relevant in market risk management.
The unconditional loss-distribution FLt+1 on the other hand is deﬁned as the
distribution of l[t](·) under the stationary distribution FX of risk-factor changes. It
gives the distribution of the portfolio loss if we consider a generic risk-factor change
X with the same distribution as X1, . . . , Xt. The unconditional loss distribution is
of particular interest if the time horizon over which we want to measure our losses
is relatively large, as is frequently the case in credit risk management and insurance.
To deﬁne conditional and unconditional distributions of linearized losses we simply replace l[t] by l
[t]. Of course, if the risk-factor changes form an iid sequence,
conditional and unconditional loss distributions coincide.
--- page 45 ---

2.1. Risk Factors and Loss Distributions
29
Risk-management techniques based on the conditional loss distribution are often
termed conditional or dynamic risk management; techniques based on the unconditional loss distribution are often referred to as static risk management. In Section 2.3.6 we illustrate the difference between the two approaches.
2.1.3
Mapping of Risks: Some Examples
We now consider a number of examples from the area of market and credit risk,
illustrating how typical risk-management problems ﬁt into the framework of the previous section. Altogether there are ﬁve examples in this section. While we strongly
encourage the reader to study at least two or three of them to develop intuition for
the mapping of risks, it is possible to skip some of the examples at ﬁrst reading.
Example 2.4 (stock portfolio). Consider a ﬁxed portfolio of d stocks and denote
by λi the number of shares of stock i in the portfolio at time t. The price process
of stock i is denoted by (St,i)t∈N. Following standard practice in ﬁnance and risk
management we use logarithmic prices as risk factors, i.e. we take Zt,i := ln St,i,
1 ⩽i ⩽d. The risk-factor changes Xt+1,i = ln St+1,i −ln St,i then correspond
to the log-returns of the stocks in the portfolio. We get Vt = d
i=1 λi exp(Zt,i) and
hence
Lt+1 = −(Vt+1 −Vt) = −
d

i=1
λiSt,i(exp(Xt+1,i) −1).
The linearized loss L
t+1 is then given by
L
t+1 = −
d

i=1
λiSt,iXt+1,i = −Vt
d

i=1
wt,iXt+1,i,
(2.8)
where the weight wt,i := (λiSt,i)/Vt gives the proportion of the portfolio value
invested in stock i at time t. The corresponding linearized loss operator is given
by l
[t](x) = −Vtw′
tx := −Vt
d
i=1 wt,ixi. Given the mean vector and covariance
matrix of the distribution of the risk-factor changes it is very easy to compute the ﬁrst
two moments of the distribution of the linearized loss L. Suppose that the random
vector X follows a distribution with mean vector µ and covariance matrix Σ. Using
general rules for the mean and variance of linear combinations of a random vector
(see also equations (3.7) and (3.8)) we immediately get
E(l
[t](X)) = −Vtw′µ
and
var(l
[t](X)) = V 2
t w′Σw.
(2.9)
Applied to the mean vector µt and the covariance matrix Σt of the conditional
distribution FXt+1|Ft of the risk-factor changes, (2.9) yields the ﬁrst two moments
of the conditional loss distribution; applied to the mean vector µ and the covariance
matrix Σ of the unconditional distribution FX of the risk-factor changes, (2.9) yields
the ﬁrst two moments of the unconditional loss distribution.
Example 2.5 (European call option). We now consider a simple example of a
portfolioofderivativesecurities,namelyastandardEuropeancallonanon-dividendpaying stock S with maturity date T and exercise price K. We use the Black–Scholes
--- page 46 ---

30
2. Basic Concepts in Risk Management
option-pricing formula for the valuation of our portfolio. Deﬁne the function CBS
by
CBS(s, S; r, σ, K, T ) := SΦ(d1) −Ke−r(T −s)Φ(d2),
(2.10)
where Φ denotes the standard normal distribution function (df), r represents the
continuously compounded risk-free interest rate, σ denotes the annualized volatility
of the underlying stock, and where
d1 = ln(S/K) + (r + 1
2σ 2)(T −s)
σ√T −s
and
d2 = d1 −σ
√
T −s.
(2.11)
Following market convention, time in (2.10) is measured in years so that Remark 2.2
applies. We are interested in daily losses and set  = 1/250.
An obvious risk factor to choose for this portfolio is the log-price of the underlying stock. While in the Black–Scholes option-pricing model the interest rate and
volatility are assumed to be constant, in real markets interest rates change constantly as do the implied volatilities that practitioners tend to use as inputs for the
volatility parameter. Hence we take Zt = (ln St, rt, σt)′ as the vector of risk factors.
According to the Black–Scholes formula the value of the call option on day t equals
Vt = CBS(t, St; rt, σt, K, T ). The risk-factor changes are given by
Xt+1 = (ln St+1 −ln St, rt+1 −rt, σt+1 −σt),
so that the linearized loss is given by
L
t+1 = −(CBS
s  + CBS
S StXt+1,1 + CBS
r Xt+1,2 + CBS
σ Xt+1,3),
where the subscripts denote partial derivatives. Note that we have omitted the arguments of CBS to simplify the notation. The derivatives of the Black–Scholes optionpricing function are often referred to as the Greeks: CBS
S
(the partial derivative
with respect to the stock price S) is called the delta of the option; CBS
s
(the partial
derivative with respect to calendar time s) is called the theta of the option; CBS
r
(the
partial derivative with respect to the interest rate r) is called the rho of the option;
in a slight abuse of the Greek language, CBS
σ
(the partial derivative with respect to
volatility σ) is called the vega of the option. The Greeks play an important role in
the risk management of derivative portfolios.
The reader should keep in mind that for portfolios with derivatives the linearized
loss can be a rather poor approximation of the true loss, since the portfolio value is
often a highly nonlinear function of the risk factors. This has led to the development
of higher-order approximations such as the delta–gamma approximation, where
ﬁrstand second-order derivatives are used. (The second derivative CBS
SS is called
the gamma of an option.) In Notes and Comments we provide a number of further
references dealing with this issue.
Example 2.6 (bond portfolio). Next we consider a portfolio of d default-free zerocoupon bonds with maturity Ti and price p(s, Ti), 1 ⩽i ⩽d (again time is measured
in years, so Remark 2.2 applies). By λi we denote the number of bonds with maturity
--- page 47 ---

2.1. Risk Factors and Loss Distributions
31
Ti in the portfolio. While zero-coupon bonds of longer maturities are relatively rare
in practice, our example is relevant, since many ﬁxed-income instruments such as
coupon bonds or standard swaps can be viewed as portfolios of zero-coupon bonds.
We follow a standard convention in modern interest-rate theory and normalize
the face value p(T, T ) of the bond to one. Recall that the continuously compounded
yield of a zero-coupon bond is deﬁned as y(s, T ) := −(1/(T −s)) ln p(s, T ),
i.e. we have
p(s, T ) = exp(−(T −s)y(s, T )).
The mapping T →y(s, T ) is referred to as the continuously compounded yield
curve at time s. In a detailed analysis of the change in value of a bond portfolio one
takes all yields y(s, Ti), 1 ⩽i ⩽d, as risk factors. The value of the portfolio at
time s is then given by V (s) = d
i=1 λip(s, Ti), and in our mapping notation (2.2)
we have
Vt =
d

i=1
λip(t, Ti) =
d

i=1
λi exp(−(Ti −t)y(t, Ti)).
(2.12)
From this formula the loss Lt+1 is easily computed. Taking derivatives and using
the deﬁnition of the linearized loss L
t+1 in (2.5) we also get
L
t+1 = −
d

i=1
λip(t, Ti)(y(t, Ti) −(Ti −t)Xt+1,i),
(2.13)
where the risk-factor changes are Xt+1,i = y((t + 1), Ti) −y(t, Ti).
This formula is closely related to the classical concept of duration. Suppose
that the yield curve is ﬂat, i.e. y(s, T ) = y(s) independently of T and that the
only possible changes in interest rates are parallel shifts of the yield curve so that
y(s + , T ) = y(s) + δ for all T . These assumptions are clearly unrealistic but
frequently made in practice. Then L
t+1 can be written as
L
t+1 = −Vt

yt −
d

i=1
λip(t, Ti)
Vt
(Ti −t)δ

= −Vt(yt −Dδ),
where
D :=
d

i=1
λip(t, Ti)
Vt
(Ti −t)
is a weighted sum of the times to maturity of the different cash ﬂows in the portfolio,
the weights being proportional to the discounted value of the cash ﬂows. D is usually
called the duration of a bond portfolio.The duration is an important tool in traditional
bond-portfolio or asset-liability management. The standard duration-based strategy
to manage the interest risk of a bond portfolio is called immunization. Under this
strategy an asset manager, who has a certain amount of funds to invest in various
bonds and who needs to make certain known payments in the future, allocates these
funds to various bonds in such a way that the duration of the overall portfolio
consisting of bond investment and liabilities is equal to zero. As we have just seen,
--- page 48 ---

32
2. Basic Concepts in Risk Management
duration measures the sensitivity of the portfolio value with respect to parallel shifts
of the yield curve. Hence a zero duration means that the position has been immunized
against these type of yield-curve changes. However, the portfolio is still exposed to
other types of yield-curve changes.
If we consider large portfolios of ﬁxed-income instruments, such as the overall
ﬁxed-income position of a major bank, choosing the yield of every bond in the portfolio as a risk factor becomes impractical: one ends up with too many risk factors,
whichrenderstheestimationofthedistributionoftherisk-factorchangesimpossible.
To overcome this problem one therefore picks a few benchmark yields per country and uses a more-or-less ad hoc procedure to map cash ﬂows at days between
benchmark points to the two nearest benchmark points. We refer to Section 6.2 of
the RiskMetrics technical document (JPMorgan 1996) for details.
Example 2.7 (currencyforwards). Wenowconsiderthemappingofalongposition
in a currency forward.A currency or foreign exchange (FX) forward is an agreement
between two parties to buy/sell a pre-speciﬁed amount ¯V of foreign currency at a
future time point T > s at a pre-speciﬁed exchange rate ¯e. The future buyer is said
to hold a long position, the other party is said to hold a short position in the contract.
To map this position we use the fact that a long position in the forward is equivalent
to a long position in a foreign and a short position in a domestic zero-coupon
bond. For illustration think of a euro investor holding a long position of size ¯V in
a currency forward on the USD/euro exchange rate. Denote by pf(s, T ) the USD
price of anAmerican (foreign) zero-coupon bond and by pd(s, T ) the corresponding
euro (domestic) zero-coupon bond; the USD/euro spot exchange rate is denoted by
e(s). Then the value in euro at time T of a portfolio consisting of λ1 := ¯V foreign
and λ2 := −¯e ¯V domestic zero-coupon bonds equals VT = ¯V (eT −¯e), which is
obviously equal to the pay-off of the long position in the forward.
The short position in the domestic zero-coupon bond can be dealt with as in
Example 2.6. Hence it remains to consider the position in theAmerican zero-coupon
bond. Obvious risk factors to choose are the logarithmic exchange rate and the yield
of the US zero-coupon bond, i.e. Zt = (ln et, yf(t, T ))′. The value of the position
in the foreign bond then equals
Vt = ¯V exp(Zt,1 −(T −t)Zt,2),
and we get
L
t+1 = −Vt(Zt,2 + Xt+1,1 −(T −t)Xt+1,2),
where as usual Xt+1 represents the risk-factor changes.
Example 2.8 (stylized portfolio of risky loans). In our ﬁnal example, which comes
from the area of credit risk management, we show how losses from a portfolio
of loans ﬁt into our general framework; a detailed discussion of models for loan
portfolios will be presented in Chapter 8. A loan portfolio is subject to many risks.
The most important ones are default risk, i.e. the risk that some counterparties cannot
repay their loans; interest-rate risk, i.e. the risk that the present value of the future
--- page 49 ---

2.1. Risk Factors and Loss Distributions
33
cash ﬂows from the portfolio is diminished due to rising interest rates; and, ﬁnally,
the risk of losses caused by rising credit spreads.
We consider a portfolio of loans to m different counterparties; the size of the
exposure to counterparty i is denoted by ei. Following standard practice in credit
risk management, our risk-management horizon  is taken to be one year so that
there is no need to distinguish between the two timescales (i.e. t and s). For simplicity
we assume that all loans are repaid at the same date T > t and that there are no
payments prior to T . We introduce an rv Yt,i that represents the default state of
counterparty i at t; we set Yt,i = 1 if counterparty i defaults in the time period [0, t]
and Yt,i = 0 otherwise. Again for simplicity we assume a recovery rate of zero,
i.e. we assume that upon default of obligor i the whole exposure ei is lost.
In valuing a risky loan we have to take the possibility of default into account.
Typically, this is done by discounting the cash ﬂow ei at a higher rate than the yield
y(t, T ) of a default-free zero-coupon bond. More precisely, we model the value at
time t of such a loan as
exp(−(T −t)(y(t, T ) + ci(t, T )))ei;
ci(t, T ) is then referred to as the credit spread of company i corresponding to the
maturity T . Credit spreads are often determined from the prices of traded corporate
bonds issued by companies with a similar credit quality to the counterparty under
consideration. Alternatively, a formal pricing model using, for instance, the market value of the counterparty’s stock as main input can be used (see Chapter 8, in
particular Section 8.2, for more information). Again for simplicity we ignore variations in credit quality and assume that ci(t, T ) = c(t, T ) for all i. Under all these
simplifying assumptions the value at time t of our loan portfolio equals
Vt =
m

i=1
(1 −Yt,i) exp(−(T −t)(y(t, T ) + c(t, T )))ei.
(2.14)
This suggests the following (m + 2)-dimensional random vector of risk factors
Zt = (Yt,1, . . . , Yt,m, y(t, T ), c(t, T ))′.
(2.15)
Lt+1 and l[t] are now easy to compute using (2.14). Due to the discrete nature
of the default indicators and the long time horizon, linearized losses are of little
importance in credit risk management. It is apparent from (2.14) and (2.15) that the
main difﬁculty in modelling the loss distribution of loan portfolios is in ﬁnding and
calibrating a good model for the joint distribution of the default indicators Yt+1,i,
1 ⩽i ⩽m; this issue is taken up in Chapter 8.
Notes and Comments
The framework introduced in this section is a stylized version of the model introduced by the RiskMetrics Group. A summary of the earlier work of the RiskMetrics Group is the RiskMetrics Technical Document (JPMorgan 1996); an excellent
updated summary, which also discusses some recent developments on the academic
side, is Mina and Xiao (2001). The mapping of positions is also discussed in Jorion
--- page 50 ---

34
2. Basic Concepts in Risk Management
(2001) and Dowd (1998). The differences between conditional and unconditional
risk management are highlighted in McNeil and Frey (2000).
While not very satisfactory from a theoretical point of view, duration-based hedging remains popular with practitioners. For a detailed discussion of duration and its
use in the management of interest-rate risk we refer the reader to standard ﬁnance
textbooks such as Jarrow and Turnbull (1999) or Hull (1997).
The mapping of derivative portfolios using ﬁrstand second-order approximations
to the portfolio value (the so-called delta–gamma approximation) is discussed in
Dufﬁe and Pan (1997) and Rouvinez (1997) (see also Dufﬁe and Pan 2001).
2.2
Risk Measurement
In this section we give an overview of existing approaches to measuring risk in
ﬁnancial institutions. In discussing strengths and weaknesses of these approaches
we focus on practical aspects and postpone a proper discussion of the theoretical
properties of the risk measures (issues such as subadditivity and coherence) until
Chapter 6.
In practice risk measures are used for a variety of purposes. Among the most
important are the following.
Determination of risk capital and capital adequacy. As discussed in Chapter 1,
one of the principal functions of risk management in the ﬁnancial sector is to
determine the amount of capital a ﬁnancial institution needs to hold as a buffer
against unexpected future losses on its portfolio in order to satisfy a regulator, who
is concerned with the solvency of the institution. A related problem is the determination of appropriate margin requirements for investors trading at an organized
exchange, which is typically done by the clearing house of the exchange.
Management tool. Risk measures are often used by management as a tool for
limiting the amount of risk a unit within a ﬁrm may take. For instance, traders in
a bank are often constrained by the rule that the daily 95% Value-at-Risk of their
position should not exceed a given bound.
Insurance premiums. Insurance premiums compensate an insurance company for
bearing the risk of the insured claims.The size of this compensation can be viewed
as a measure of the risk of these claims.
2.2.1
Approaches to Risk Measurement
Existing approaches to measuring the risk of a ﬁnancial position can be grouped into
four different categories: the notional-amount approach; factor-sensitivity measures;
risk measures based on the loss distribution; risk measures based on scenarios.
Notional-amount approach.
This is the oldest approach to quantifying the risk of
a portfolio of risky assets. In the notional-amount approach the risk of a portfolio is
deﬁned as the sum of the notional values of the individual securities in the portfolio,
where each notional value may be weighted by a factor representing an assessment
of the riskiness of the broad asset class to which the security belongs. Variants of
--- page 51 ---

2.2. Risk Measurement
35
this approach are still in use in the standardized approach of the Basel Committee
rules on banking regulation; see, for example, Section 10.1.2 for operational risk,
or Chapter 2 of Crouhy, Galai and Mark (2001).
The advantage of the notional-amount approach is its apparent simplicity. However, as we recall from Chapter 1, from an economic viewpoint the approach is
ﬂawed for a number of reasons. To begin with, the approach does not differentiate between long and short positions and there is no netting. For instance, the risk
of a long position in foreign currency hedged by an offsetting short position in a
currency forward would be counted as twice the risk of the unhedged currency position. Moreover, the approach does not reﬂect the beneﬁts of diversiﬁcation on the
overall risk of the portfolio. For example, if we use the notional-amount approach,
it appears that a well-diversiﬁed credit portfolio consisting of loans to m companies
that default more or less independently has the same risk as a portfolio where the
whole amount is lent to a single company. Finally, the notional-amount approach
has problems in dealing with portfolios of derivatives, where the notional amount of
the underlying and the economic value of the derivative position can differ widely.
Factor-sensitivity measures.
Factor-sensitivity measures give the change in portfolio value for a given predetermined change in one of the underlying risk factors;
typically they take the form of a derivative (in the calculus sense). Important factorsensitivity measures are the duration for bond portfolios and the Greeks for portfolios
of derivatives. While these measures provide useful information about the robustness of the portfolio value with respect to certain well-deﬁned events, they cannot
measure the overall riskiness of a position. Moreover, factor-sensitivity measures
create problems in the aggregation of risks.
• For a given portfolio it is not possible to aggregate the sensitivity with respect
to changes in different risk factors. For instance, it makes no sense to simply
add the delta and the vega of a portfolio of options.
• Factor-sensitivity measures cannot be aggregated across markets to create a
picture of the overall riskiness of the portfolio of a ﬁnancial institution.
Hence these measures are not very useful for capital-adequacy decisions; used in
conjunction with other measures they can be useful for setting position limits.
Risk measures based on loss distributions.
Most modern measures of the risk in
a portfolio are statistical quantities describing the conditional or unconditional loss
distribution of the portfolio over some predetermined horizon . Examples include
the variance, theValue-at-Risk and the expected shortfall, which we discuss in more
detail in Sections 2.2.2–2.2.4. It is of course problematic to rely on any one particular
statistic to summarize the risk contained in a distribution. However, the view that
the loss distribution as a whole gives an accurate picture of the risk in a portfolio
has much to commend it:
• losses are the central object of interest in risk management and so it is natural
to base a measure of risk on their distribution;
--- page 52 ---

36
2. Basic Concepts in Risk Management
• the concept of a loss distribution makes sense on all levels of aggregation
from a portfolio consisting of a single instrument to the overall position of a
ﬁnancial institution;
• if estimated properly, the loss distribution reﬂects netting and diversiﬁcation
effects; and, ﬁnally,
• loss distributions can be compared across portfolios.
For instance, it makes perfect sense to compare the loss distribution of a book of
ﬁxed-income instruments and of a portfolio of equity derivatives, at least if the time
horizon  is the same in both cases.
There are two major problems when working with loss distributions. First, any
estimate of the loss distribution is based on past data. If the laws governing ﬁnancial
markets change, these past data are of limited use in predicting future risk. The
second, related problem is practical. Even in a stationary environment it is difﬁcult to
estimate the loss distribution accurately, particularly for large portfolios, and many
seemingly sophisticated risk-management systems are based on relatively crude
statistical models for the loss distribution (incorporating, for example, untenable
assumptions of normality).
However, this is not an argument against using loss distributions. Rather, it calls
for improvements in the way loss distributions are estimated and, of course, for
prudence in the practical application of risk-management models based on estimated loss distributions. In particular, risk measures based on the loss distribution
should be complemented by information from hypothetical scenarios. Moreover,
forward-looking information reﬂecting the expectations of market participants, such
as implied volatilities, should be used in conjunction with statistical estimates (which
are necessarily based on past information) in calibrating models of the loss distribution.
Scenario-based risk measures.
In the scenario-based approach to measuring the
risk of a portfolio one considers a number of possible future risk-factor changes
(scenarios): such as a 10% rise in key exchange rates or a simultaneous 20% drop
in major stock market indices or a simultaneous rise of key interest rates around
the globe. The risk of the portfolio is then measured as the maximum loss of the
portfolio under all scenarios, where certain extreme scenarios can be downweighted
to mitigate their effect on the result.
We now give a formal description. Fix a set X = {x1, . . . , xn} of risk-factor
changes (the scenarios) and a vector w = (w1, . . . , wn)′ ∈[0, 1]n of weights.
Consider a portfolio of risky securities and denote by l[t] the corresponding loss
operator. The risk of this portfolio is then measured as
ψ[X,w] := max{w1l[t](x1), . . . , wnl[t](xn)}.
(2.16)
Many risk measures used in practice are of the form (2.16). For instance, the Chicago
Mercantile Exchange (CME) uses a scenario-based approach to determine margin
requirements. To compute the initial margin for a simple portfolio consisting of a
--- page 53 ---

2.2. Risk Measurement
37
position in a futures contract and call and put options on this contract, the CME
considers sixteen different scenarios. The ﬁrst fourteen consist of an up move or
a down move of volatility combined with no move, an up move or a down move
of the futures price by 1/3, 2/3 or 3/3 units of a speciﬁed range. The weights wi,
i = 1, . . . , 14, of these scenarios are equal to one. In addition there are two extreme
scenarios with weights w15 = w16 = 0.35. The amount of capital required by the
exchange as margin for a portfolio is then computed according to (2.16).
Remark 2.9. We can give a slightly different mathematical interpretation to formula (2.16), which will be useful in Section 6.1. Assume for the moment that
l[t](0) = 0, i.e. that the value of the position is unchanged if all risk factors stay
the same. This is reasonable, at least for a short risk-management horizon . In that
case the expression wil[t](xi) can be viewed as the expected value of l[t] under a
probability measure on the space of risk-factor changes; this measure associates a
mass of wi ∈[0, 1] to the point xi and a mass of 1 −wi to the point 0. Denote by
δx the probability measure associating a mass of one to the point x ∈Rd and by
P[X,w] the following set of probability measures on Rd:
P[X,w] = {w1δx1 + (1 −w1)δ0, . . . , wnδxn + (1 −wn)δ0}.
Then ψ[X,w] can be written as
ψ[X,w] = max{EP (l[t](X)) : P ∈P[X,w]}.
(2.17)
A risk measure of the form (2.17), where P[X,w] is replaced by some arbitrary subset
P of the set of all probability measures on the space of risk-factor changes, is termed
a generalized scenario. Generalized scenarios play an important role in the theory
of coherent risk measures (see Section 6.1).
Scenario-based risk measures are a very useful risk-management tool for portfolios exposed to a relatively small set of risk factors as in the CME example.
Moreover, they provide useful complementary information to measures based on
statistics of the loss distribution. The main problem is of course to determine an
appropriate set of scenarios and weighting factors. Moreover, comparison across
portfolios which are affected by different risk factors is difﬁcult.
2.2.2
Value-at-Risk
Value-at-Risk (VaR) is probably the most widely used risk measure in ﬁnancial institutions and has also made its way into the Basel II capital-adequacy framework—
hence it merits an extensive discussion. In this chapter we introduceVaR and discuss
practical issues surrounding its use; in Section 6.1 we examine VaR from the viewpoint of coherent risk measures and highlight certain theoretical deﬁciencies.
Consider some portfolio of risky assets and a ﬁxed time horizon , and denote
by FL(l) = P(L ⩽l) the df of the corresponding loss distribution. We do not
distinguish between L and L or between conditional and unconditional loss distributions; rather we assume that the choice has been made at the outset of the analysis
and that FL represents the distribution of interest. We want to deﬁne a statistic
--- page 54 ---

38
2. Basic Concepts in Risk Management
based on FL which measures the severity of the risk of holding our portfolio over
the time period . An obvious candidate is the maximum possible loss, given by
inf{l ∈R : FL(l) = 1}, a risk measure important in reinsurance. However, in most
models of interest the support of FL is unbounded so that the maximum loss is
simply inﬁnity. Moreover, by using the maximum loss we neglect any probability
information in FL. Value-at-Risk is a straightforward extension of maximum loss,
which takes these criticisms into account. The idea is simply to replace “maximum
loss” by “maximum loss which is not exceeded with a given high probability”, the
so-called conﬁdence level.
Deﬁnition 2.10 (Value-at-Risk). Given some conﬁdence level α ∈(0, 1). TheVaR
of our portfolio at the conﬁdence level α is given by the smallest number l such that
the probability that the loss L exceeds l is no larger than (1 −α). Formally,
VaRα = inf{l ∈R : P(L > l) ⩽1 −α} = inf{l ∈R : FL(l) ⩾α}.
(2.18)
In probabilistic terms, VaR is thus simply a quantile of the loss distribution.
Typical values for α are α = 0.95 or α = 0.99; in market risk management the
time horizon  is usually 1 or 10 days, in credit risk management and operational
risk management  is usually one year. Note that by its very deﬁnition the VaR at
conﬁdence level α does not give any information about the severity of losses which
occur with a probability less than 1 −α. This is clearly a drawback of VaR as a risk
measure. For a small case study that illustrates this problem numerically we refer
to Example 2.21 below.
Figure 2.1 illustrates the notion of VaR. The probability density function of a loss
distribution is shown with a vertical line at the value of the 95% VaR. Note that the
mean loss is negative (E(L) = −2.6), indicating that we expect to make a proﬁt,
but the right tail of the loss distribution is quite long in comparison with the left tail.
The 95% VaR value is approximately 2.2, indicating that there is a 5% chance that
we lose at least this amount.
Remark 2.11 (mean-VaR). Denote by µ the mean of the loss distribution. Sometimes the statistic VaRmean
α
:= VaRα −µ is used for capital-adequacy purposes
instead of ordinary VaR. If the time horizon  equals one day, VaRmean
α
is sometimes referred to as daily earnings at risk. The distinction between ordinaryVaR and
VaRmean
α
is of little relevance in market risk management, where the time horizon is
short and µ is close to zero. It becomes relevant in credit where the risk-management
horizon is longer. In particular, in loan pricing one uses VaRmean to determine the
economic capital needed as a buffer against unexpected losses in a loan portfolio
(see Section 9.3.4 for details). Taking the expectation of the P&L distribution into
account is also important in the growing ﬁeld of asset-management risk.
Since quantiles play an important role in risk management we recall the precise
deﬁnition.
--- page 55 ---

2.2. Risk Measurement
39
Loss
Probability density
0
0.05
0.10
0.15
0.20
0.25
5% probability
E(L)
VaR
ES
10
10
5
5
0
Figure 2.1.
An example of a loss distribution with the 95% VaR marked as a vertical line;
the mean loss is shown with a dotted line and an alternative risk measure known as the 95%
expected shortfall (see Section 2.2.4 and Deﬁnition 2.15) is marked with a dashed line.
Deﬁnition 2.12 (generalized inverse and quantile function).
(i) Given some increasing function T : R →R, the generalized inverse of T is
deﬁned by T ←(y) := inf{x ∈R : T (x) ⩾y}, where we use the convention
that the inﬁmum of an empty set is ∞.
(ii) Given some df F, the generalized inverse F ←is called the quantile function
of F. For α ∈(0, 1) the α-quantile of F is given by
qα(F) := F ←(α) = inf{x ∈R : F(x) ⩾α}.
For an rv X with df F we often use the alternative notation qα(X) := qα(F). If
F is continuous and strictly increasing, we simply have qα(F) = F −1(α), where
F −1 is the ordinary inverse of F. To compute quantiles in more general cases we
may use the following simple criterion.
Lemma 2.13. A point x0 ∈R is the α-quantile of some df F if and only if the
following two conditions are satisﬁed: F(x0) ⩾α; F(x) < α for all x < x0.
The lemma follows immediately from the deﬁnition of the generalized inverse
and the right-continuity of F. Examples for the computation of quantiles in certain
tricky cases and further properties of generalized inverses are given in SectionA.1.2.
Example 2.14 (VaR for normal and t loss distributions). Suppose that the loss
distribution FL is normal with mean µ and variance σ 2. Fix α ∈(0, 1). Then
VaRα = µ + σΦ−1(α)
and
VaRmean
α
= σΦ−1(α),
(2.19)
where Φ denotes the standard normal df and Φ−1(α) is the α-quantile of Φ. The
proof is easy: since FL is strictly increasing, by Lemma 2.13 we only have to show
--- page 56 ---

40
2. Basic Concepts in Risk Management
that FL(VaRα) = α. Now
P(L ⩽VaRα) = P
L −µ
σ
⩽Φ−1(α)

= Φ(Φ−1(α)) = α.
This result is routinely used in the variance–covariance approach (also known as
the delta-normal approach) to computing risk measures, which we describe in Section 2.3.1 below; if we work with linearized losses, and assume that our risk-factor
changes are multivariate normal, then the resulting loss distribution is normal, and
we can compute VaR using (2.19).
Of course a similar result is obtained for any location-scale family and another
useful example is the Student t loss distribution. Suppose our loss L is such that
(L −µ)/σ has a standard t distribution with ν degrees of freedom; we denote this
loss model by L ∼t(ν, µ, σ 2) and note that the moments are given by E(L) = µ
and var(L) = νσ 2/(ν −2) when ν > 2, so that σ is not the standard deviation of
the distribution. We get
VaRα = µ + σt−1
ν (α),
(2.20)
where tν denotes the df of standard t, which is available in most statistical computer
packages along with its inverse.
2.2.3
Further Comments on VaR
Non-subadditivity.
VaR has been fundamentally criticized as a risk measure on the
grounds that is has poor aggregation properties. This critique has its origins in the
work of Artzner et al. (1997, 1999), who showed that VaR is not a coherent risk
measure, since it violates the property of subadditivity that they believe reasonable
risk measures should have.
We devote Section 6.1 to an in-depth discussion of this subject. At this point
we merely remark that non-subadditivity means that if we have two loss distributions FL1 and FL2 for two portfolios and we denote the overall loss distribution
of the merged portfolio L = L1 + L2 by FL, we do not necessarily have that
qα(FL) ⩽qα(FL1) + qα(FL2), so that the VaR of the merged portfolio is not necessarily bounded above by the sum of the VaRs of the individual portfolios. This
contradicts our notion that there should be a diversiﬁcation beneﬁt associated with
merging the portfolios; it also means that a decentralization of risk management
using VaR is difﬁcult since we cannot be sure that by aggregating VaR numbers for
different portfolios or business units we will obtain a bound for the overall risk of
the enterprise.
Model risk and market liquidity.
In practice VaR numbers are often given a very
literal interpretation, which is misleading and even dangerous; the statement that
the daily VaR at conﬁdence level α = 99% of a particular portfolio is equal to l is
understood as “with a probability of 99% the loss on this position will be smaller
than l”.
This interpretation is misleading for two reasons. To begin with, our estimate of
the loss distribution is subject to estimation error and the problem of model risk.
--- page 57 ---

2.2. Risk Measurement
41
Model risk can be deﬁned as the risk that a ﬁnancial institution incurs losses because
its risk-management models are misspeciﬁed or because some of the assumptions
underlying these models are not met in practice. For instance, we might work with
a normal distribution to model losses whereas the real distribution is heavy-tailed,
or we might fail to recognize the presence of volatility clustering or tail dependence
(see Section 4.1.1) in modelling the distribution of the risk-factor changes. Since
“any ﬁnancial model is by deﬁnition a simpliﬁed and thus imperfect representation
of the economic world and the ways in which economic agents perform investment,
trading or ﬁnancing decisions” (from the introduction of Gibson (2000)), it is fair
to say that any risk-management model is subject to model risk to some extent.
Of course, these problems are most pronounced if we try to estimate VaR at very
high conﬁdence levels such as α = 99.97%, as we might be required to do in the
determination of economic capital (see Section 1.4.3).
Moreover, the above interpretation ofVaR neglects any problems related to market
liquidity. Loosely speaking, a market for a security is termed liquid if investors can
buy or sell large amounts of the security in a short time without affecting its price
very much. Conversely, a market in which an attempt to trade has a large impact
on price, or where trading is impossible since there is no counterparty willing to
take the other side of the trade, is termed illiquid. The problem this poses for the
interpretation of VaR numbers was brought to the attention of professional risk
managers by Lawrence and Robinson (1995). To quote from their paper:
If we ask the question: “Can we be 98% conﬁdent that no more than an
amount l [the VaR estimate at α = 0.98] would be lost in liquidating
the position?” the answer must be “no”. To see why, consider what this
measure of VaR implies about the risk management process and the
nature of ﬁnancial markets. In the liquidation scenario we are considering the following sequence of events is implied: at time t it is decided
to liquidate the position; during the next 24 hours nothing is done . . . ;
after 24 hours of inaction the position is liquidated at prices which are
drawn from a [pre-speciﬁed] distribution unaffected by the process of
liquidation. This scenario is hardly credible. . . . In particular, the act
of liquidating itself would have the effect of moving the price against
the trader disposing of a long position or closing out a short position.
For large positions and illiquid instruments the costs of liquidation can
be signiﬁcant, in particular if speed is required.
They conclude that “any useful measures of VaR must take into account the costs
of liquidation on the prospective loss”. The events surrounding the near-bankruptcy
of the hedge fund LTCM in Summer 1998 clearly showed that these concerns are
more than justiﬁed. In fact, illiquidity of markets is nowadays regarded by many
risk managers as the most important source of model risk.
Ideally we should try to factor the effects of market illiquidity into formal models,
although this is difﬁcult for a number of reasons. First, the price impact of trading a
particular amount of a security at a given point in time is hard to measure; it depends
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
