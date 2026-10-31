# Quantitative Risk Management_ Concepts, Techniques, and -- Alexander J_ McNeil, Rüdiger Frey, Paul Embrechts -- Princeton series in finance, -- isbn13 9780691122557 -- 478a0059673fecd0c76229cd3d8884e7 -- Anna’s Arc.pdf — pages 476–495

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
--- page 477 ---

9.8. Default Contagion in Reduced-Form Models
461
Table 9.3.
Default correlation and quantiles of ¯M1 in a homogeneous model with
interacting intensities for m = 500 ﬁrms and varying interaction a1.
a1
P (Y1,i = 1)
ρY
q0.9
q0.95
q0.975
q0.99
0
0.031 99
0.000 415 79
0.044
0.046
0.05
0.054
1
0.031 98
0.005 075 3
0.052
0.058
0.066
0.072
3
0.031 99
0.058 283
0.096
0.128
0.156
0.19
the case m = 500. We see that the default correlation ρ(Y1,i, Y1,j), i̸ = j, and
the quantiles of the distribution of ¯M1 increase substantially as a1 increases. This
makes perfect sense: for a1 > 0 a higher (lower) than usual number of defaults in
the portfolio leads to an increase (decrease) in the default intensity of the remaining
ﬁrms in the portfolio and thus to a further increase (decrease) in the ratio of realized
versus expected defaults, so the resulting distribution of ¯M1 will have more mass in
the tails.
Notes and Comments
Theorem 9.46 is taken from Br´emaud but is originally due to Jacod (1975). Both texts
are excellent references that study point processes from the viewpoint of stochastic
calculus.DynamicpropertiesofcopulamodelswereﬁrststudiedinSch¨onbucherand
Schubert (2001). The pricing of ﬁrst-to-default swaps follows Laurent and Gregory
(2003).
The techniques used in Section 9.8.2 are popular in survival analysis (see, for
example, Chapter 10 of Andersen et al. 1993); in the context of portfolio credit
risk, related ideas can be found in Sch¨onbucher (2004). Collin-Dufresne, Goldstein
and Helwege (2003) propose a model for information-based default contagion that
starts from the mixture representation (9.69) of the survival function. Giesecke and
Goldberg (2004) study information-based default contagion in a structural multi-
ﬁrm model with incomplete information about the default thresholds.
Our presentation of models with interacting intensities is based on Frey and Backhaus (2004). The ﬁrst model with interacting intensities is due to Jarrow and Yu
(2001). Davis and Lo (2001) pointed out the link between models with interacting intensities and ﬁnite-state Markov chains. Mathematical aspects of the Jarrow–
Yu model are discussed in Kusuoka (1999), Bielecki and Rutkowski (2002) and
Collin-Dufresne, Goldstein and Hugonnier (2004). Yu (2005b) provides an alternative construction of the Jarrow–Yu model using the general hazard construction
from survival analysis. Moreover, certain features of the model are studied using
simulation. The pricing of portfolio credit derivatives in models with interacting
intensities is discussed in Frey and Backhaus (2004); this paper also contains an
analysis of the asymptotic behaviour of the homogeneous model (9.94) for large
portfolios. Credit risk models with explicitly speciﬁed interaction between default
intensities are conceptually and mathematically close to models for interacting particle systems developed in statistical physics. F¨ollmer (1994) contains an inspiring
discussion of the relevance of ideas from the interacting-particle-systems literature
--- page 478 ---

462
9. Dynamic Credit Risk Models
for ﬁnancial modelling; the link to credit risk is explored by Giesecke and Weber
(2004, 2005), Horst (2004) and Focardi and Fabozzi (2004). Egloff, Leippold and
Vanini (2004) study credit contagion in a ﬁrm-value model. Allen and Gale (2000)
discuss ﬁnancial contagion from a ﬁnancial economics viewpoint; an interesting
analysis of systemic risk in ﬁnancial networks in general can be found in Eisenberg
and Noe (2001).
Many textbooks on stochastic processes contain an introduction to continuoustime Markov chains. Excellent texts are Resnick (1992), Davis (1993) and Norris
(1997); a good summary is given in Appendix C of Lando (2004). Continuous-time
Markov chains are frequently used to build dynamic models for rating-transitions
(see, for example, Jarrow, Lando and Turnbull (1997) or Chapter 6 of Lando (2004)).
--- page 479 ---

10
Operational Risk and Insurance Analytics
Wehavesofarconcentratedonthemodellingofmarketandcreditrisk,whichreﬂects
the historical development of quantitative risk management in the banking context.
Some of the techniques we have discussed are also relevant in operational risk
modelling, in particular the techniques of extreme value theory (EVT) in Chapter 7
and the aggregation methodology of Chapter 6. But we also need other techniques
tailored speciﬁcally to operational risk, and we believe that actuarial models used
in non-life insurance are particularly relevant.
In the ﬁrst half of this chapter (Section 10.1) we examine the Basel II requirements for the quantitative modelling of operational risk, discussing various potential
approaches. On the basis of some industry data we highlight the possibilities and
limitations of existing tools for the calculation of an operational risk-capital charge.
In Section 10.2 we summarize the techniques from actuarial modelling that are
relevant to operational risk, under the heading of insurance analytics. Our discussion
in that section, though motivated by quantitative modelling of operational risk, has
a much wider applicability in quantitative risk management. For example, some
techniques have implicitly been used in the credit risk chapters. The Notes and
Comments section at the end of the chapter gives an overview of further techniques
from insurance mathematics that we feel will become useful in the years to come.
10.1
Operational Risk in Perspective
10.1.1
A New Risk Class
In our overview of Basel II, in Section 1.3.1, we introduced operational risk as
a new risk class for which ﬁnancial institutions, bound by the Basel Committee
rules (Basel II) and to some extent also by Solvency 2 (Section 1.3.2), are required
to put aside regulatory capital. We ﬁrst recall the Basel II deﬁnition as it appears in
the ﬁnal document (Basel Committee on Banking Supervision 2004).
Operational risk is deﬁned as the risk of loss resulting from inadequate or failed internal processes, people and systems or from external
events. This deﬁnition includes legal risk, but excludes strategic and
reputational risk.
Examples of losses falling within this category are, for instance, fraud (internal
as well as external), losses due to IT failures, errors in settlements of transactions,
litigation and losses due to external events like ﬂooding, ﬁre, earthquake or terrorism.
--- page 480 ---

464
10. Operational Risk and Insurance Analytics
Losses due to unfortunate management decisions, such as many of the mergers and
acquisitions of the 1990s or the launch of larger-scale bank-assurance projects, are
deﬁnitely not included.
A case that touched upon almost all aspects of the above deﬁnition was that of
Barings (see also Section 1.2.2). From insufﬁcient internal checks and balances
(processes), to fraud (human risk), to external events (the Kobe earthquake), many
operational risk factors contributed to the downfall of this once proud merchant bank.
Further examples include the $691 million rogue trading loss at Allﬁrst Financial,
the $484 million settlement due to misleading sales practices at Household Finance,
and the estimated $140 million loss for the Bank of New York stemming from the
September11attacks.Allexamplesofferaclearproofofthefundamentalimportance
of operational risk as a risk class to be monitored. Current estimates for capital
allocated to operational risk at large international banks are in the range $2–7 billion
(see deFontnouvelle et al. 2003).
An essential difference between operational risk, on the one hand, and market
and credit risk, on the other, is that operational risk has no upside for a bank. It
comes about through the malfunctioning of parts of daily business and hence is as
much a question of quality control as anything else. Clearly, banks try as hard as
possible to avoid operational risk but, despite their best efforts, operational losses
will continue to occur.
This has prompted the Basel Committee to decide that banks must set aside risk
capital under Pillar I of the three-pillar system (see Section 1.3.1). The Pillar II and
Pillar III proposals of the new accord imply that a supervisory review process for
operational risk must also be put in place and that an appropriate market discipline
with respect to public disclosure must be adhered to. The market has not been slow
to provide various ways of mitigating the effects of the new risk category, ranging
from IT solutions and data warehouses to improve the measurement of operational
risk, to insurance-type solutions for banks willing and able to enter into such deals.
Currently,andfortheforeseeablefuture,thelackofoperationallossdataisamajor
issue, and this is similar to the problem faced by underwriters of catastrophe insurance. The insurance industry’s answer to the problem has involved data-pooling
across industry participants and a similar discussion is now taking place in the
banking industry. Once representative data sources become available, the implementation of many of the methods discussed in this book (such as EVT in Chapter 7
and the insurance analytics of Section 10.2) will become increasingly feasible. Existing sources of data at present are the databases produced by the Quantitative Impact
Studies (QISs) of the Basel Committee and by the Federal Reserve Bank of Boston.
Moreover, some private companies are also providing data.
In Section 10.1.3 we discuss the kind of advanced-measurement (AM) approach
that an analysis of operational loss data allows. Before this we discuss so-called
elementary approaches to operational risk modelling. In these approaches, aimed
at smaller banks without extensive international activities, the detailed modelling
of loss distributions for different risk classes and risk types is not required; a fairly
simple volume-based capital charge is proposed.We note that, as in the case of credit
--- page 481 ---

10.1. Operational Risk in Perspective
465
risk, the approaches proposed by Basel II for the calculation of regulatory capital
represent a gradation in complexity. Recall that, for credit risk, banks must implement either the standardized approach or the internal-ratings-based (IRB) approach,
as discussed in Section 1.3.1 and Section 8.1.
10.1.2
The Elementary Approaches
There are two elementary approaches to operational risk measurement. Under the
basic-indicator (BI) approach, banks must hold capital for operational risk equal to
the average over the previous three years of a ﬁxed percentage (denoted by α) of
positiveannualgrossincome(GI).Figuresforanyyearinwhichannualgrossincome
is negative or zero should be excluded from both the numerator and denominator
when calculating the average. Hence the risk capital under the BI approach for
operational risk in year t is given by
RCt
BI(OR) = 1
Zt
3

i=1
α max(GIt−i, 0),
(10.1)
where Zt = 3
i=1 I{GIt−i>0} and GIt−i stands for gross income in year t −i.
Note that an operational risk-capital charge is calculated on a yearly basis. The
BI approach gives a fairly straightforward, volume-based, one-size-ﬁts-all capital
charge. Based on the various QISs, the Basel Committee suggests that α = 15%.
Under the standardized (S) approach, banks’activities are divided into eight business lines: corporate ﬁnance; trading & sales; retail banking; commercial banking;
payment & settlement; agency services; asset management; and retail brokerage.
Precise deﬁnitions of these business lines are to be found in the Basel Committee’s
ﬁnal document (Basel Committee on Banking Supervision 2004). Within each business line, gross income is a broad indicator that serves as a proxy for the scale of
business operations and thus the likely scale of operational risk exposure.The capital
charge for each business line is calculated by multiplying gross income by a factor
(denoted by β) assigned to that business line. As in (10.1), the total capital charge
is calculated as a three-year average over positive GIs, resulting in the following
capital charge formula:
RCt
S(OR) = 1
3
3

i=1
max
0 8

j=1
βjGIt−i
j
, 0
1
.
(10.2)
It is to be noted that in formula (10.2), in any given year t −i, negative capital
charges (resulting from negative gross income) in some business line j may offset
positive capital charges in other business lines (albeit at the discretion of the national
supervisor).This kind of “netting” should induce banks to go from the basic indicator
to the standardized approach; the word “netting” is of course to be used with care
here. Based on the QISs, the Basel Committee has set the beta coefﬁcients as in
Table 10.1. Moscadelli (2004) gives a critical analysis of these beta factors, based
on the full database of more than 47 000 operational losses of the second QIS of the
summer of 2002 (see also Section 10.1.4).
--- page 482 ---

466
10. Operational Risk and Insurance Analytics
Table 10.1.
Beta factors for the standardized approach.
Business line (j)
Beta factors (βj)
j = 1, corporate ﬁnance
18%
j = 2, trading & sales
18%
j = 3, retail banking
12%
j = 4, commercial banking
15%
j = 5, payment & settlement
18%
j = 6, agency services
15%
j = 7, asset management
12%
j = 8, retail brokerage
12%
Inbothapproaches(BI,S)theBaselCommitteeexpectsfurtherguidelines(mainly
under Pillars II and III) to be adhered to. Also, at national discretion, supervisors
may adopt slight (often more conservative) changes to aspects of the above rules, the
latter clearly with a level playing ﬁeld for the different market participants in mind.
Widely adopted risk-management rules should be formulated as much as possible in
such a way as to avoid regulatory arbitrage within and across national jurisdictions.
10.1.3
Advanced Measurement Approaches
Under an AM approach, the regulatory capital is determined by a bank’s own internal risk-measurement system according to a number of quantitative and qualitative
criteria set forth in documentation produced by the Basel Committee (Basel Committee on Banking Supervision 2004). We will not go into all relevant steps of the
procedure leading towards the acceptance of an AM approach for an internationally
active bank and its subsidiaries; the Basel Committee’s documents give a clear and
readable account of this. We focus instead on the methodological aspects of a full
quantitative approach to operational risk measurement. It should be stated, however, that, as in the case of market and credit risk, the adoption of an AM approach
to operational risk is subject to approval and continuing quality checking by the
national supervisor.
While the BI and S approaches prescribe the explicit formulas (10.1) and (10.2),
theAM approach lays down general guidelines. In the words of the Basel Committee
(Basel Committee on Banking Supervision 2004).
Given the continuing evolution of analytical approaches for operational
risk, the Committee is not specifying the approach or distributional
assumptions used to generate the operational risk measure for regulatory capital purposes. However, a bank must be able to demonstrate
that its approach captures potentially severe “tail” loss events. Whatever approach is used, a bank must demonstrate that its operational risk
measure meets a soundness standard comparable to that of the internal
ratings-based approach for credit risk (comparable to a one year holding
period and the 99.9 percent conﬁdence interval).
--- page 483 ---

10.1. Operational Risk in Perspective
467
In an AM approach, operational losses should be categorized according to the eight
business lines mentioned in Section 10.1.2 as well as the following seven loss-event
types: internal fraud; external fraud; employment practices & workplace safety;
clients, products & business practices; damage to physical assets; business disruption & system failures; and execution, delivery & process management. Banks are
expected to gather internal data on repetitive, high-frequency losses (three to ﬁve
years of data), as well as relevant external data on non-repetitive low-frequency
losses. Moreover, they must add stress scenarios both at the level of loss severity
(parameter shocks to model parameters) and correlation between loss types. In the
absence of detailed joint models for different loss types, risk measures for the aggregate loss should be calculated by summing across the different loss categories. In
general, both so-called expected and unexpected losses should be taken into account
(i.e. risk-measure estimates cannot be reduced by subtraction of an expected loss
amount).
We now describe a skeletal version of a typical AM solution for the calculation
of an operational risk charge for year t. We assume that historical loss data from
previous years have been collected in a data warehouse with the structure
{Xt−i,b,ℓ
k
: i = 1, . . . , T ; b = 1, . . . , 8; ℓ= 1, . . . , 7; k = 1, . . . , Nt−i,b,ℓ},
(10.3)
where Xt−i,b,ℓ
k
stands for the kth loss of type ℓfor business line b in year t −i;
Nt−i,b,ℓis the number of such losses and T ⩾5 years, say. Note that thresholds
may be imposed for each (i, b, ℓ) category and small losses less than the threshold
may be neglected; a threshold is typically of the order of €10 000.The total historical
loss amount for business line b in year t −i is obviously
Lt−i,b =
7

ℓ=1
Nt−i,b,ℓ

k=1
Xt−i,b,ℓ
k
,
(10.4)
and the total loss amount for year t −i is
Lt−i =
8

b=1
Lt−i,b.
(10.5)
The problem in the AM approach is to use the loss data to estimate the distribution
of Lt for year t and to calculate risk measures such as VaR or expected shortfall
(see Section 2.2) for the estimated distribution. Writing ϱα for the risk measure at a
conﬁdence level α, the regulatory capital is determined by
RCt
AM(OR) = ϱα(Lt),
(10.6)
where α would typically take a value in the range 0.99–0.999 imposed by the
local regulator. Because the joint distributional structure of the losses in (10.4)
and (10.5) for any given year is generally unknown, we would typically resort to
simple aggregation of risk measures across loss categories to obtain a formula of
the form
RCt
AM(OR) =
8

b=1
ϱα(Lt,b).
(10.7)
--- page 484 ---

468
10. Operational Risk and Insurance Analytics
In view of our discussions in Chapter 6, the choice of an additive rule in (10.7)
can be understood. Indeed, for any coherent risk measure ϱα, the right-hand side
of (10.7) yields an upper bound for the total risk ϱα(Lt). In the important case of
VaR, the right-hand side of (10.7) corresponds to the comonotonic scenario (see
Proposition 6.15). The optimization results of Section 6.2 can be used to calculate
bounds for ϱα(Lt) under different dependence scenarios for the business lines; see,
in particular, Example 6.23 and Table 6.1.
Reduced to its most stylized form in the case when ϱα = VaRα and α = 0.999,
a capital charge under the AM approach requires the calculation of a quantity of the
type
VaR0.999
 N

k=1
Xk

,
(10.8)
where (Xk) is some sequence of loss severities and N is an rv describing the frequency with which operational losses occur. Random variables of the type (10.8) are
one of the prime examples of the actuarial models that we treat in Section 10.2.2.
Before we move on to those models in the next section, we highlight some “stylized
facts” of operational loss data.
10.1.4
Operational Loss Data
In order to reliably estimate (10.6), (10.7) or, in a stylized version, a quantity
like (10.8), we need extensive data. The data situation for operational risk is much
worse than that for credit risk, and is clearly an order of magnitude worse than for
market risk, where vast quantities of data are publicly available. Banks have only
recently started gathering data and pooling initiatives are in their infancy, so, as far
as we know, no reliable publicly available data source on operational risk exists.
Our discussion below is based on some industry data we have been able to analyse
as well as on the ﬁndings in Moscadelli (2004) for the QIS database and the results
of the 2004 loss-data collection exercise by the Federal Reserve Bank of Boston
(see Federal Reserve System 2005). An excellent overview of some of the data
characteristics is to be found in the Basel Committee’s report (Basel Committee
on Banking Supervision 2003). From the latter report we quote:
Despite this progress, inferences based on the data should still be made
with caution. . . . In addition, the most recent data collection exercise
provides data for only one year and, even under the best of circumstances, a one-year collection window will provide an incomplete picture of the full range of potential operational risk events, especially of
rare but signiﬁcant “tail events”.
In Figure 10.1 we have plotted operational loss data obtained from several sources;
parts (a)–(c) show losses for three business lines for the period 1992–2001. It is less
important for the reader to know the exact loss type—it is sufﬁcient to accept that
the data are typical for (b, ℓ) categories in (10.3). In part (d), the data from the three
previous ﬁgures have been pooled.
--- page 485 ---

10.1. Operational Risk in Perspective
469
(a)
(b)
(c)
1992 1994 1996 1998 2000 2002
(d)
1992 1994 1996 1998 2000 2002
40
30
20
20
10
10
15
0
0
0
40
30
20
10
0
5
2
4
6
8
Figure 10.1.
Operational risk losses: (a) type 1, n = 162; (b) type 2, n = 80;
(c) type 3, n = 175; and (d) pooled losses n = 417.
Exploratory data analysis reveals the following stylized facts (conﬁrmed in several
other studies):
• loss severities have a heavy-tailed distribution;
• losses occur randomly in time;
• loss frequency may vary substantially over time.
The third observation is partly explained by the fact that banks have only recently
started gathering operational risk data prompted by Basel II. There is a considerable
amount of reporting bias resulting in fewer losses in the ﬁrst half of the 1990s and
more losses afterwards. Moreover, several classes of loss may have a considerable
cyclical component and/or may depend on changing economic covariables. For
instance, back-ofﬁce errors may depend on volume traded and fraud may be linked
to the overall level of the economy (depressions versus boom cycles). This clear
inhomogeneity in the loss frequency makes an immediate application of statistical
methodology difﬁcult. However, it may be reasonable to at least assume that the
(inﬂation-adjusted) loss sizes have a common severity distribution, which would
allow, for instance, the application of methods from Chapter 7.
In Figure 10.2 we have plotted the sample mean excess functions (7.16) for the
data in Figure 10.1. This ﬁgure clearly indicates the ﬁrst stylized fact of heavytailed loss severities. The mean excess plots in (a) and (b) are clearly increasing in
an approximately linear fashion, pointing to Pareto-type behaviour. This contrasts
with (c), where the plot appears to level off from a threshold of one. This hints at a
loss distribution with ﬁnite upper limit, but this could only be substantiated by more
detailed knowledge of the type of loss concerned. Pooling the data in (d) masks the
different kinds of behaviour, and perhaps illustrates the dangers of naive statistical
analyses that do not consider the data-generating mechanism.
Moscadelli (2004) performed a detailed EVT analysis (including a ﬁrst attempt to
solve the frequency problem) of the full QIS data set of more than 47 000 operational
--- page 486 ---

470
10. Operational Risk and Insurance Analytics
•••••••••••••••••••••••••••••••••
•
•
•
•
Mean excess
••••••••••••••••••••••••
••
••
•
•
•
•••••••••••••••••••••••••••••••••••••••••••••••••••••• •••• • •• • • •••
•
• •
0.5
1.0
1.5
2.0
2.5
Mean excess
•••••••••••••••••••••••••••••••••••• •••• • • ••• ••
• •
•
•
(a)
(b)
(c)
(d)
2
2
2
4
4
6
6
8
8
2
4
6
8
10
12
2
4
6
8
10
12
14
0
0
2
4
4
6
8
0
1
3
2
0
1
3
5
Threshold
Threshold
Figure 10.2.
Corresponding sample mean excess plots for the data in Figure 10.1:
(a) type 1; (b) type 2; (c) type 3; (d) pooled.
losses and concluded that the loss dfs are well ﬁtted by generalized Pareto distributions (GPDs) in the upper-tail area (see Section 7.2.2 for the necessary statistical
background). The estimated tail parameters (ξ in (7.14)) for the different business
lines range from 0.85 for asset management to 1.39 for commercial banking. Six
of the business lines have an estimate of ξ greater than one, corresponding to an
inﬁnite mean model! Based on these QIS data, the estimated RC/GI ratios (the β in
Table 10.1) range from 8.3% for retail banking to 33.3% for payment & settlement,
with an overall alpha value (see (10.1)) of 13.3%, slightly below the Basel II value
of 15% used in the BI approach. Note the much broader range of values of the β
emerging from the analysis of the QIS data compared with the prescribed range of
12–18% for the standardized approach in Table 10.1.
As more data become available, more conclusive analyses may be possible. It
is clear, however, from Moscadelli (2004) that the GPD method of Section 7.2
is one of the most useful statistical tools at our disposal and yields a ﬁt that is
superior to other loss distributions in the high-tail area; this has been corroborated by
several practitioners from the banking and insurance industry. In view of the heavytailedness of the data, and the necessity of calculating capital charges corresponding
to high quantiles, it seems very natural to use EVT methodology.
Notes and Comments
Several textbooks on operational risk have been published: see, for example, Cruz
(2002, 2004), King (2001), the Risk Books publication edited by Risk Books (2003)
and chapters in Ong (2004) and Crouhy, Galai and Mark (2001). In particular,
Chapter 4 of Cruz (2004), written by Carolyn Currie, gives an excellent overview
of the regulatory issues surrounding operational risk.
A practical implementation is discussed in Ebn¨other et al. (2003). Frachot,
Georges and Roncalli (2001) discuss the loss-distribution approach to operational
--- page 487 ---

10.2. Elements of Insurance Analytics
471
risk. D¨obeli, Leippold and Vanini (2003) elaborate on the way in which a good
operational risk framework may lead to an overall improvement in quality of the
business operations.
Figure 10.1 is taken from Embrechts, Kaufmann and Samorodnitsky (2004). The
latter paper also stresses the important difference between so-called repetitive and
non-repetitive losses. For the former (to some extent less important) losses, statistical modelling can be very useful. For non-repetitive, low-probability, high-severity
losses, much more care has to be taken before a statistical analysis can be performed
(see P´ezier 2002a,b).
EVT methods for operational risk quantiﬁcation have been used by numerous
authors (see, for example, Coleman 2002, 2003; Medova 2000a,b). Because of the
non-stationarityofoperationallossdataoverseveralyears,morereﬁnedEVTmodels
are called for. See, for example, Chavez-Demoulin and Embrechts (2004); Chavez-
Demoulin, Embrechts and Neˇslehov´a (2005) for some examples of such models. For
a critical article on the use of EVT for the calculation of an operational risk-capital
charge, see Embrechts, Furrer and Kaufmann (2003), which contains a simulation
study of the number of data needed to come up with a reasonable estimate of a high
quantile.The use of statistical methods other than EVT are discussed in the textbooks
referred to above. These methods include linear predictive models, Bayesian belief
networks and discriminant analysis. Excellent data-analytic papers using published
operational risk losses are deFontnouvelle et al. (2003) and Moscadelli (2004).
Finally, recall from Notes and Comments of Section 6.2 the paper by Rosenberg
and Schuermann (2004), which addresses the aggregation of market, credit and
operational risk measures.
10.2
Elements of Insurance Analytics
10.2.1
The Case for Actuarial Methodology
Actuarial tools and techniques for the modelling, pricing and reserving of insurance
products in the traditional ﬁelds of life, non-life and reinsurance have a long history
going back more than a century. More recently, the border between ﬁnancial and
insurance products has become blurred, examples of this process being equity-linked
life products and alternative risk-transfer vehicles (see Section 1.5.2 and Notes and
Comments of that chapter).
Whereas some of the combined bank-assurance products have not met with the
success that was originally hoped for, it remains true that there exists an increasing
need for ﬁnancial and actuarial professionals who can close the methodological gaps
between the two ﬁelds. In the sections that follow we discuss insurance analytical
tools that we believe the more traditional ﬁnance-oriented risk manager ought to be
aware of; the story behind the name insurance analytics can be found in Embrechts
(2002).
It is not only the occasional instance of joint product development between the
banking and insurance worlds that prompts us to make a case for actuarial methodology in QRM, but also the observation that many of the concepts and techniques
--- page 488 ---

472
10. Operational Risk and Insurance Analytics
of QRM described in the preceding chapters are in fact borrowed from the actuarial
literature.
• Risk measures like expected shortfall (Deﬁnition 2.15) have been studied in
a systematic way in the insurance literature. Expected shortfall is also the
standard risk measure to be used under the Solvency 2 guidelines.
• Many of the dependence modelling tools presented in Chapter 5 saw their ﬁrst
applications in the realm of insurance. Moreover, notions like comonotonicity
of risk factors have their origins in actuarial questions.
• In Section 6.1 we discussed the axiomatization of ﬁnancial risk measures and
pointed at the parallel development of insurance premium principles (often
with very similar goals and results).
• The statistical modelling of extremal events has been a bread-and-butter subject for actuaries since the start of insurance. Hence, many of the tools presented in Chapter 7 are well known to actuaries.
• Within the world of credit risk management, the industry model CreditRisk+
(Section 8.4.2) is known as an actuarial model.
• The actuarial approach to the modelling of operational risk is apparent in the
AM approach of Section 10.1.3.
In the sections that follow, we give a brief discussion of relevant actuarial techniques.
The material presented should enable the reader to transfer actuarial concepts to
QRM in ﬁnance more easily. We do not strive for a full treatment of relevant tools
as these could ﬁll a separate (voluminous) textbook (see, for example, Denuit and
Charpentier (2004), Mikosch (2004) and Partrat and Besson (2004) for excellent
accounts of many of the relevant techniques).
10.2.2
The Total Loss Amount
Reconsider formula (10.8), where a random number N of random losses or severities Xk occurring in a given time period are summed. To apply a risk measure like
VaR we need to make assumptions about the (Xk) and N, which leads us to one of
the fundamental concepts of (non-life) insurance mathematics.
Deﬁnition 10.1 (total loss amount and distribution). Denote by N(t) the (random) number of losses over a ﬁxed time period [0, t] and write X1, X2, . . . for the
individual losses. The total loss amount (or aggregate loss) is deﬁned as
SN(t) =
N(t)

k=1
Xk,
(10.9)
with df FSN(t)(x) = P(SN(t) ⩽x), the total (or aggregate) loss df. Whenever t is
ﬁxed, t = 1 say, we may drop the time index from the notation and simply write SN
and FSN .
Remark 10.2. The deﬁnition of (10.9) as an rv is to be understood as SN(t)(ω) =
N(t)(ω)
k=1
Xk(ω), ω ∈Ω, and is referred to as a random (or randomly indexed) sum.
--- page 489 ---

10.2. Elements of Insurance Analytics
473
A prime goal of this section will be the analytical and numerical calculation
of FSN , which requires further assumptions about (Xk) and N.
Assumption 10.3 (independence, compound sums). We assume that the rvs (Xk)
are iid with common df G, G(0) = 0. We further assume that the rvs N and (Xk)
are independent; in that case we refer to (10.9) as a compound sum. The probability
mass function of N is denoted by pN(k) = P(N = k), k = 0, 1, 2, . . . . The rv N
is referred to as the compounding rv.
Proposition 10.4 (compound distribution). Let SN be a compound sum and suppose that Assumption 10.3 holds. Then, for all x ⩾0,
FSN (x) = P(SN ⩽x) =
∞

k=0
pN(k)G(k)(x),
(10.10)
where G(k)(x) = P(Sk ⩽x), the kth convolution of G. Note that G(0)(x) = 1 for
x ⩾0, and G(0)(x) = 0 for x < 0.
Proof. Suppose x ⩾0. Then
FSN (x) =
∞

k=0
P(SN ⩽x | N = k)P(N = k) =
∞

k=0
pN(k)G(k)(x).
Although formula (10.10) is explicit, its actual calculation in speciﬁc cases is
difﬁcult because the convolution powers G(k) of a df G are in general not available in closed form. Hence, one resorts to (numerical) approximation methods.
A ﬁrst class of these uses the fact that the Laplace–Stieltjes transform of a convolution is the product of the Laplace–Stieltjes transforms. Using the usual notation
ˆF(s) =
 ∞
0
e−sx dF(x), where s ⩾0 for Laplace–Stieltjes transforms, we have
that
G(k)(s) = ( ˆG(s))k. It follows from Proposition 10.4 that
ˆFSN (s) =
∞

k=0
pN(k) ˆGk(s) = MN( ˆG(s)),
s ⩾0,
(10.11)
where MN denotes the moment-generating function of N.
Example 10.5 (the compound Poisson df). Suppose that N has a Poisson df with
intensity parameter λ > 0, denoted N ∼Poi(λ). In that case, pN(k) = e−λλk/k!,
k ⩾0, and, for s ∈R,
MN(s) =
∞

k=0
e−λ λk
k! sk = exp(−λ(1 −s)).
Hence from (10.11) it follows that, for s ⩾0,
ˆFSN (s) = exp(−λ(1 −ˆG(s))).
In this case, the df of SN is referred to as the compound Poisson df and we write
SN ∼CPoi(λ, G). Formula (10.11) facilitates the calculation of moments of SN
--- page 490 ---

474
10. Operational Risk and Insurance Analytics
and lends itself to numerical evaluation through Fourier inversion, known as the
fast Fourier transform (FFT) (see Notes and Comments for references on the latter).
For the calculation of moments, note that, under the assumption of the existence of
sufﬁciently high moments and hence differentiability of ˆG and MN, we obtain
dk
dsk MN(s)

s=1
= E(N(N −1) · · · (N −k + 1))
and
(−1)k dk
dsk ˆG(s)

s=0
= E(Xk
1) = µk.
Example 10.6 (continuation of Example 10.5). In the case of the compound Poisson df, one obtains
E(SN) = (−1) d
ds
ˆFSN (s)

s=0
= exp(−λ(1 −ˆG(0)))λ(−ˆG′(0))
= λµ1 = E(N)E(X1).
Similar calculations yield var(SN) = E(S2
N) −(E(SN))2 = λµ2.
For the general compound case one obtains the following useful result.
Proposition 10.7 (moments of compound dfs). Under Assumption 10.3 and
assuming that E(N) < ∞, µ2 < ∞, we have that
E(SN) = E(N)E(X1)
and
var(SN) = var(N)(E(X1))2 + E(N) var(X1).
(10.12)
Proof. This follows readily from (10.11), differentiating with respect to s. The
following direct proof avoids the use of transforms. Conditioning on N and using
Assumption 10.3, one obtains
E(SN) = E(E(SN | N)) = E

E
 N

k=1
Xk
				 N

= E
 N

k=1
E(Xk)

= E(N)E(X1)
and, similarly,
E(S2
N) = E

E
 N

k=1
Xk
2 				 N

= E

E
 N

k=1
N

ℓ=1
XkXℓ
				 N

= E(Nµ2 + N(N −1)µ2
1) = E(N)µ2 + (E(N2) −E(N))µ2
1
= E(N) var(X1) + E(N2)(E(X1))2,
so var(SN) = E(S2
N) −(E(SN))2 = E(N) var(X1) + var(N)(E(X1))2.
--- page 491 ---

10.2. Elements of Insurance Analytics
475
Remark 10.8. Formula(10.12)elegantlycombinestherandomnessofthefrequency
(var(N)) with that of the severity (var(X1)). In the compound Poisson case it reduces
to the formula var(SN) = λE(X2
1) = λµ2, as in Example 10.6. In the deterministicsum case, when P(N = n) = 1, say, we ﬁnd the well-known results E(SN) = nµ1
and var(SN) = n var(X1); indeed, in this degenerate case, var(N) = 0.
The compound Poisson model is a basic model for aggregate ﬁnancial or insurance risk losses. The ubiquitousness of the Poisson distribution in insurance can
be understood as follows. Consider a time interval [0, 1] and let N denote the total
number of losses in that interval. Suppose further that we have a number of potential loss generators (transactions, credit positions, insurance policies, etc.) that can
produce, with probability pn, one loss or, with probability 1 −pn, no loss in each
small subinterval ((k −1)/n, k/n] for k = 1, . . . , n. Moreover, suppose that the
occurrence or non-occurrence of a loss in any particular subinterval is not inﬂuenced by the occurrence of losses in other intervals. Then the number Nn of losses
has a binomial df with parameters n and pn, so
P(Nn = k) =
n
k

pk
n(1 −pn)n−k,
k = 0, . . . , n.
Combined with a loss-severity distribution this frequency distribution gives rise,
in (10.10), to the so-called binomial loss model. Next suppose that n →∞in such
a way that limn→∞npn = λ > 0. It follows from Poisson’s theorem of rare events
(see also Section 7.4.1) that
lim
n→∞P(Nn = k) = e−λ λk
k! ,
k = 0, 1, 2, . . . ,
i.e. N∞∼Poi(λ), explaining why the Poisson model assumption is very natural as
a frequency distribution and the compound Poisson model is a common aggregate
loss model. The compound Poisson model has several nice properties, one of which
concerns aggregation and is useful in the operational risk context in situations such
as (10.5).
Proposition 10.9 (sums of compound Poisson rvs). Suppose that the compound
sums SNi ∼CPoi(λi, Gi), i = 1, . . . , d, and that these rvs are independent, then
SN = d
i=1SNi ∼CPoi(λ, G), where λ = d
i=1 λi and G = d
i=1(λi/λ)Gi.
Proof. (For d = 2, the general case being similar.) Because of independence and
Example 10.5 we have, for the Laplace–Stieltjes transform of SN,
ˆFSN (s) = ˆFSN1(s) ˆFSN2 (s)
= exp

−(λ1 + λ2)

1 −
1
λ1 + λ2
(λ1 ˆG1(s) + λ2 ˆG2(s))

= exp(−λ(1 −ˆG(s))),
where λ = λ1 + λ2 and
G =
λ1
λ1 + λ2
G1 +
λ2
λ1 + λ2
G2.
--- page 492 ---

476
10. Operational Risk and Insurance Analytics
The result follows since the Laplace–Stieltjes transform uniquely determines the
underlying df.
Hence the new intensity λ is just the sum of the old ones, whereas the new severity
df G is a discrete mixture of the loss dfs Gi with weights λi/λ, i = 1, . . . , d. We
can easily simulate losses from such a model through a two-stage procedure: ﬁrst
draw i (i = 1, . . . , d) with probability λi/λ, and then draw a loss with df Gi.
Beyond the Poisson model.
The Poisson model can serve as a stylized representation of the loss-generating mechanism from which more realistic models can be
derived. For instance, we may wish to introduce a time parameter in N to capture different occurrence patterns over time (see Section 10.2.6). Also, the intensity
parameter λ may be assumed to be random (see Example 10.20). Indeed, a further step is to turn λ into a stochastic process, which gives rise to such models as
doubly stochastic (or Cox) processes (see Section 9.2.3) or self-exciting processes,
as encountered in Section 7.4.3. Furthermore, various forms of dependence among
the Xk rvs or between N and (Xk) could be modelled. Finally, multiline portfolios
require multivariate models for vectors of the type (SN1, . . . , SNd). An ultimate
goal of theAM approach to operational risk would be to model such random vectors
where where, for instance, d might stand for seven risk types, eight business lines,
or in total 56 loss category cells.
10.2.3
Approximations and Panjer Recursion
As mentioned in Section 10.2.2, the analytic calculation of FSN is not possible
for the majority of reasonable models, which has led actuaries to come up with
several numerical approximations. Below we review some of these approximations
and illustrate their use for several choices of the severity df G. The basic example
we look at is the compound Poisson case, SN ∼CPoi(λ, G), though most of the
approximations discussed can be adjusted to deal with other distributions for N.
Given λ and G we can easily simulate FSN and, by repeating this many times, we can
get an empirical estimate that is close to the true df. Figure 10.3 contains a simulation
of n = 100 000 realizations of SN ∼CPoi(100, Exp(1)). Although the histogram
exhibits mild skewness (which can easily be shown theoretically (see (10.15))),
a clear central limit effect takes place. This is used in the ﬁrst approximation below.
Normal approximation.
As the loss rvs Xi are iid (with ﬁnite second moment,
say) and SN is a (random) sum of the Xi variables, one can apply Theorem 2.5.16
in Embrechts, Kl¨uppelberg and Mikosch (1997) and Proposition 10.7 to obtain the
following approximation, for general N:
FSN (x) ≈Φ

x −E(N)E(X1)

var(N)(E(X1))2 + E(N) var(X1)

.
(10.13)
Here, and in the approximations below, “≈” has no speciﬁc mathematical interpretation beyond “there exists a limit result justifying the right-hand side to be used as
approximation of the left-hand side”. In particular, for the compound Poisson case
--- page 493 ---

10.2. Elements of Insurance Analytics
477
40
60
80
100
120
140
160
0
0.005
0.010
0.015
0.020
0.025
Figure 10.3.
Histogram of simulated compound loss data (n = 100 000) for
SN ∼CPoi(100, Exp(1)) together with normal approximation (10.14).
above, (10.13) reduces to
FSN (x) ≈Φ
x −100
√
200

,
(10.14)
where Φ is the standard normal df, as usual. It is this normal approximation that is
superimposed on the histogram in Figure 10.3. Clearly, there are conditions underlying the approximation (10.13): for example, claims should not be too heavy-tailed
(see Theorem 10.21).
For CPoi(λ, G) it is not difﬁcult to show that the skewness parameter satisﬁes
E((SN −E(SN))3)
(var(SN))3/2
=
E(X3
1)

λ(E(X2
1))3
> 0
(10.15)
(note that X1 ⩾0 almost surely), so an approximation by a df with positive skewness
may improve the approximation (10.14), especially in the tail area. This is indeed
the case and leads to the next approximation.
Translated-gamma approximation.
We approximate SN by k + Y, where k is
a translation parameter and Y ∼Ga(α, β) has a gamma distribution (see Section A.2.4). The parameters (k, α, β) are found by matching the mean, the variance
and the skewness of k + Y and SN. It is not difﬁcult to check that the following
equations result:
k + α
β = λE(X1),
α
β2 = λE(X2
1),
2
√α =
E(X3
1)

λ(E(X2
1))3
.
In our case, where λ = 100 and X1 has a standard exponential distribution, these
yield the equations k +α/β = 100, α/β2 = 200 and 2/√α = 0.2121 with solution
α = 88.89, β = 0.67, k = −32.72.
Commentaryontheseapproximations.
Bothapproximationsworkreasonablywell
in the bulk of the data. However, for risk-management purposes, we are mainly
interested in upper tail risk; in Figure 10.4 we have therefore plotted both approximations for x ⩾120 on a log–log scale. This corresponds to the tail area beyond
--- page 494 ---

478
10. Operational Risk and Insurance Analytics
.......................................................................................................................................................................................... . . .
.
Sum of claims (log scale)
1 − F(x) (log scale)
120
140
160
180
200
Normal approx.
Gamma approx.
•
Simulated
143.7

148.0

10−1
10−2
10−3
10−4
10−5
Figure 10.4.
Simulated CPoi(100, Exp(1)) data together with normaland translatedgamma approximations (log–log scale). The 99.9% quantile estimates are also given.
the 90% quantile of FSN . Similar plots were routinely used in Chapter 7 on EVT
(see, for example, Figure 7.6). It becomes clear that, as can be expected, the gamma
approximation works better in this upper tail area where the normal approximation
underestimates the loss potential.
Of course, for loss data with heavier tails than exponential (lognormal or Pareto,
say),eventhetranslated-gammaapproximationwillbeinsufﬁcientandotherapproximations can be devised based on heavier-tailed distributions, such as translated F,
inverse gamma or generalized Pareto.
Another approach could be based on Monte Carlo simulation of aggregate losses
SN to which an appropriate heavy-tailed loss distribution could then be ﬁtted.
One possible approach would be to model the tail of these simulated compound
losses with the GPD using the methodology of Section 7.2.2. This is what has
been done in Figures 10.5 and 10.6, where we have plotted various approximations for CPoi(100, LN(1, 1)) and CPoi(100, Pa(4, 1)). The former corresponds to
a standard industry model for operational risk (see Frachot 2004). The latter corresponds to a class of operational risk models used in Moscadelli (2004). From these
ﬁgures the message is clear: if the data satisfy the compound Poisson assumption,
then the GPD yields a superior ﬁt for high quantiles.
We now turn to an important class of approximations based on recursive methods.
In the case where the loss sizes (Xi) are discrete and the distribution function of N
satisﬁes a speciﬁc condition (see Deﬁnition 10.10 below) a reliable recursive method
can be worked out.
Suppose that X1 has a discrete distribution so that P(X1 ∈N0) = 1 with gk =
P(X1 = k), pk = P(N = k) (for notational convenience we write pk for pN(k))
and sk = P(SN = k). For simplicity assume that g0 = 0 and let g(n)
k
= P(X1 +
· · · + Xn = k), the discrete convolution of the probability mass function gk. Note
that, by deﬁnition, g(n+1)
k
= k−1
i=1 g(n)
i
gk−i. We immediately obtain the following
--- page 495 ---

10.2. Elements of Insurance Analytics
479
...........................................................................................................................................................................................................
...
.
Sum of claims (log scale)
1 − F(x) (log scale)
600
700
800
900
1000
Normal approx.
Gamma approx
GPD fit (u = 650)
•
Simulated
735
10−1
10−2
10−3
10−4
10−5
Panjer recursion
Figure 10.5.
Simulated CPoi(100, LN(1, 1)) data (n = 100 000) with normal-, translated-gamma, GPD and Panjer recursion (see Example 10.17) approximations (on log–log
scale).
...................................................................................................................................................................................... .. .. ..... ..
. .
.
.
Sum of claims (log scale)
40
50
60
70
80
90
Normal approx.
Gamma approx.
GPD fit (u = 50)
•
Simulated
1 − F(x) (log scale)
10−1
10−2
10−3
10−4
10−5
Figure 10.6.
Simulated CPoi(100, Pa(4, 1)) data (n = 100 000) with normal-,
translated-gamma, and GPD approximations (on log–log scale).
identities:
s0 = P(SN = 0) = P(N = 0) = p0,
sn = P(SN = n) =
∞

k=1
pkg(k)
n ,
n ⩾1,
⎫
⎪⎪⎬
⎪⎪⎭
(10.16)
where the latter formula corresponds to Proposition 10.4 but now in the discrete
case. As in Proposition 10.4 we note that (10.16) is difﬁcult to calculate, mainly due
