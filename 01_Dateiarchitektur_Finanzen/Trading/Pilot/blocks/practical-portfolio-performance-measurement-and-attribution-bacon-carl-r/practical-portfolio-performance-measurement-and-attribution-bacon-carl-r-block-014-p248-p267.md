# Practical Portfolio Performance Measurement and Attribution -- Bacon, Carl R_ -- 10_1002_9781119206309, 2012 jan 02 -- John Wiley & Sons, Inc_ -- doi 10_1002_9781119206309 -- bc9440f8ca87cf4e34d9c3fda66edb46 -- Anna.pdf — pages 248–267

--- page 248 ---

JWBK178-10
JWBK178-Bacon
July 30, 2008
7:5
Char Count= 0
238
Practical Portfolio Performance Measurement and Attribution
The time value reﬂects the possibility that the option may be “in the money” before expiry
and is a function of time and volatility. Time value peaks around the exercise price; for a low
underlying price well below the exercise price there is no intrinsic value and little time value.
If the option is deeply in the money it is virtually certain to be exercised and time value will
also be low.
Option price sensitivity (the Greeks)
Options can be valued using the Black–Scholes model which requires:
(1) The price of the underlying asset.
(2) The strike or exercise price of the option.
(3) Time to expiry.
(4) The variability (or volatility) of the underlying asset.
(5) The cost of carry.
The price sensitivities of options are measured by the “Greeks”: delta, gamma, theta, vega and
rho:
Delta (
or ). Delta is the change in value of an option for a small change in underlying
asset price.
Gamma (
or
). Gamma measures the change in delta for a small change in underlying
asset price.
Theta (theta). Theta is the change in value of an option as time elapses, all other factors
remaining constant.
Vega (sometimes called kappa ( )). Vega is the change in value of an option for a given
change in volatility. Unlike the other Greeks vega is not a Greek letter.
Rho ( ). The change in value of an option for a given change in interest rates.
The impact of the change in price of an option for a positive change in each of the Greeks is
summarised in Table 10.5.
Delta is the most important Greek from the point of view of performance measurement and
attribution analysis. If a long call option is out of the money the delta will be less than 50% and
converges to zero the more deeply out of the money it becomes. If the long call option is at the
money the delta is approximately 50%; there is a 50%:50% change of the price moving either
way. If the long call option is in the money the delta will be greater than 50% and converges
to 100% if the option is deeply in the money, moving in line with the price of the underlying
asset.
Table 10.5
Impact of positive change in Greek sensitivity
Option type
Delta
Gamma
Vega
Rho
Theta
Long call
ve
ve
ve
ve
ve
Long put
ve
ve
ve
ve
ve
Short call
ve
ve
ve
ve
ve
Short put
ve
ve
ve
ve
ve
--- page 249 ---

JWBK178-10
JWBK178-Bacon
July 30, 2008
7:5
Char Count= 0
Performance Measurement for Derivatives
239
Underlying price
Option price
Strike price
Figure 10.2
Option convexity
The delta is a ﬁrst-order approximation of the change of price of the option; the actual
relationship is convex as shown in Figure 10.2. The option delta is the slope of the line at a
tangent to the curve at the strike price.
Delta works well for small change in value of underlying. Gamma measures the rate of
change of this delta. For long calls the delta underestimates the gain in option price and
overestimates the loss. For short calls and puts convexity is negative, overestimating gains and
underestimating losses; clearly not a desirable situation.
WARRANTS
A warrant is a time-limited right to subscribe for shares, debentures, loan stock or government
securities and is exercisable against the original issuer of the underlying securities. Some other
instruments are also called warrants but are actually options; for example, a right to acquire
securities, which is exercisable against someone other than the original issuer of the securities,
is often called a covered warrant.
Convertible bonds
A convertible bond is a type of bond which can be converted into stock of the issuing company.
In effect, a convertible is a bond with an embedded long call option and from the perspective
of performance measurement and attribution analysis it is appropriate to separate the two types
of exposure if consistent with the investment decision process.
Buyers of convertible bonds might be seeking both to arbitrage by selling the underlying
security and to take advantage of pricing anomalies, or in a similarly way might be seeking to
syntheticallycreatetheunderlyingsecuritybybuyingtheconvertiblebutholdinganappropriate
amount of equitised cash to replicate the overall exposure of the desired asset at a cheaper
price. This equitised cash, which may or may not be adjusted in line with the delta of the
embedded option in the convertible, should be included as appropriate notional equity and
notional (negative) cash assets for the purposes of attribution.
--- page 250 ---

JWBK178-10
JWBK178-Bacon
July 30, 2008
7:5
Char Count= 0
240
Practical Portfolio Performance Measurement and Attribution
The participation rate of a convertible bond unlike delta describes the entire instrument’s
exposure to price changes in the underlying asset. Because much of the combined valuation is
derived from the bond element it is likely that the upside participation will be greater than the
downside participation – say, for example, 75% upside capture but only 65% participation on
the downside.
Attribution analysis using options, warrants and convertible bonds
The key to attribution analysis with options is to include the appropriate economic exposure
for which we can use the option’s delta. The option itself will provide part of the valuation;
the remainder of the option’s economic value must be achieved again by using notional assets.
The fundamentals of generating notional assets for options are laid out by Stannard (1996):
Option economic exposure
number of options
stock price
option valuation
notional exposure
(10.3)
The delta and hence the exposure is continuously changing. However, if the notional asset
exposures are recalculated on a daily basis the impact of gamma can be signiﬁcantly reduced.
Return calculations and attribution analysis for a portfolio with a single option plus cash are
shown in Exhibits 10.12 and 10.13.
Exhibit 10.12
Performance measurement for options
Type of option
Long call
Underlying
Massive Firm Inc.
Current share price
$ 100
Exercise price
$ 100
Current option price
$ 10
Option delta
50%
Share end price
$ 102
Option end price
$ 11
Libor for period of measurement
0.1%
Return
SMV
EMV
(%)
Options
1000
1100
10.0
Cash
9000
9009
0.1
Total
10 000
10 109
1.09
Option economic value
0 5
100
100
5000
Notional cash asset required
5000
1000
4000
Return
SMV
EMV
(%)
Options
1000
1100
10.0
Notional exposure
4000
4004
0.1
Combined
5000
5104
2.08
Cash
9000
9009
0.1
Notional cash
(4000)
(4004)
0.1
Combined
5000
5005
0.1
Total
10 000
10 109
1.09
(Note that 5000
10 000
2 08%
5000
10 000
0 1%
1 09%)
--- page 251 ---

JWBK178-10
JWBK178-Bacon
July 30, 2008
7:5
Char Count= 0
Performance Measurement for Derivatives
241
Exhibit 10.13
Attribution for options
Using data from Exhibit 10.12 and assuming a benchmark consisting of 40% exposure to the underlying
asset of the option and 60% cash, attribution is calculated as follows:
Benchmark return 40%
2 0%
60%
0 1%
0 86%
Semi-notional return 50%
2 0%
50%
0 1%
1 05%
Geometric asset allocation:
(1
bS)
(1
b)
1
1 0105
1 0086
1
0 19%
Options
(50%
40%)
1 02
1 0086
1
0 11%
Cash
(50%
60%)
1 001
1 0086
1
0 08%
Geometric stock selection:
(1
r)
(1
bS)
1
1 0109
1 0105
1
0 04%
Options
50%
1 0208
1 02
1
1 02
1 0105
0 04%
Cash
50%
1 001
1 001
1
1 001
1 0105
0 00%
Correctly adjusting for the appropriate economic exposure the attribution analysis indicates
the portfolio manager is overweight the reference asset and underweight cash, generating an
added value of 19 basis points. Stock selection also made a small contribution of 4 basis points
to added value; this might come from any of the Greeks other than delta – no attempt is made to
identify which of the Greeks added the most value. For standard portfolios including options
this type of analysis is sufﬁcient to quantify the manager’s decision process; for option-only
portfolios more detailed analysis might be required.
MARKET NEUTRAL ATTRIBUTION
Market neutral funds as their name suggests are designed to be neutral against market movements. In theory, they consist of a 100% long allocation offset by a 100% short position in the
same market. The resultant exposure should be 100% cash plus the excess return from stock
selection on the long side and the excess return from the stock selection on the short side. Thus,
good stock pickers should be able to generate double the excess return without any market
exposure; a very attractive and easily understood absolute return strategy.
Attribution is relatively straightforward if the long and short parts of the portfolio are treated
as separate asset categories. It is essential that the performance of underlying assets retains
the appropriate sign. The proﬁts generated by assets that are falling in value are the result
of negative weights compounded with negative returns. Stock selection and asset allocation
effects are calculated for a market neutral portfolio using data from Table 10.6 in Exhibits 10.15
and 10.16, respectively. Returns for the portfolio, benchmark and semi-notional fund are as
before and shown in Exhibit 10.14.
--- page 252 ---

JWBK178-10
JWBK178-Bacon
July 30, 2008
7:5
Char Count= 0
242
Practical Portfolio Performance Measurement and Attribution
Table 10.6
Market Neutral Attribution
Stock selection
i
1
ri
1
bi
1
(1
bi)
(1
bS)
(%)
Asset
allocation
(
i
Wi)
1
bi
1
b
1
(%)
Portfolio
Benchmark Portfolio Benchmark
weight
i
weight Wi
return ri
return bi
(%)
(%)
(%)
(%)
Long UK equities
30
40
20.0
10.0
0.68
2.93
Long Japanese
70
60
5.0
4.0
0.68
0.68
equities
Short UK equities
30
40
6.0
10.0
0.68
1.17
Short Japanese
60
60
7.0
4.0
0.0
1.76
equities
Cash
90
100
3.0
3.0
0.0
0.0
Total
100
100
7.6
3.0
0.68
5.18
Exhibit 10.14
Return calculations
Using the data from Table 10.6 the portfolio return r
i
n
i
1
i
ri is:
r
30%
20%
70%
5%
30%
6%
60%
7%
90%
3%
7 6%
The benchmark return b
i
n
i
1
Wi
bi is:
b
40%
10%
60%
4%
40%
10%
60%
4%
100%
3%
3 0%
The semi-notional return bS
i
n
i
1
i
bi is:
bS
30%
10%
70%
4%
30%
10%
60%
4%
90%
3%
2 3%
Exhibit 10.15
Market neutral asset allocation
Geometric asset allocation for data in Table 10.6 is:
(1
bS)
(1
b)
1
1 023
1 03
1
0 68%
Individual country asset allocation effects are:
Long UK equities
(30%
40%)
1 10
1 03
1
0 68%
Long Japanese equities
(70%
60%)
0 96
1 03
1
0 68%
Short UK equities
( 30%
40%)
1 10
1 03
1
0 68%
Short Japanese equities
( 60%
60%)
0 96
1 03
1
0 0%
Cash
(90%
100%)
1 03
1 03
1
0 0%
Total
0 68%
0 68%
0 68%
0 0%
0 0%
0 68%
--- page 253 ---

JWBK178-10
JWBK178-Bacon
July 30, 2008
7:5
Char Count= 0
Performance Measurement for Derivatives
243
Exhibit 10.16
Market neutral stock selection
Geometric stock selection including interaction for data in Table 10.6 is:
(1
r)
(1
bS)
1
1 076
1 023
1
5 18%
Individual country stock selection effects are:
Long UK equities
30%
1 20
1 10
1
1 10
1 023
2 93%
Long Japanese equities
70%
0 95
0 96
1
0 96
1 023
0 68%
Short UK equities
30%
1 06
1 10
1
1 10
1 023
1 17%
Short Japanese equities
60%
0 93
0 96
1
0 96
1 023
1 76%
Cash
90%
1 03
1 03
1
1 03
1 023
0 0%
Total
2 93%
0 68%
1 17%
1 76%
0 0%
5 18%
Interpreting the attribution results the long and short UK positions cancel out leaving a
small negative allocation of
0.68% from a net 10% long position in Japanese equities. Asset
allocation from cash will always be zero regardless of the weight since the overall benchmark
return is also a cash benchmark. The excess return from this portfolio is derived from stock
selection, positive on long UK equities and negative on long Japanese equities. In the short UK
equity portion of the portfolio, although generating a positive return the portfolio manager has
selected stocks that have underperformed the benchmark resulting in a positive contribution.
In the short Japanese portfolio the manager again selected stocks that underperformed the
benchmark which when combined with the negative weight generated a positive contribution.
The stock selection from cash is unsurprisingly neutral; stock lending fees which are suffered
in order to generate the short positions can be charged either to the cash sector or to the
appropriate short equity sector as negative income.
Further variations of the market neutral strategies overlay the entire portfolio with index
futures of entirely different markets thus generating the desired market exposure while trapping
the excess return or alpha from different underlying marks where perhaps the portfolio manager
retains more expertise.
Attribution for 130/30 funds (or extended short funds)
130/30funds(includingotherweightingvariations,e.g.120/20,etc.)areamorerecentvariation
of market neutral funds with a 30% short position offset by a 130% long position, thus retaining
market exposure but allowing the manager to short a limited percentage of assets.
Attribution for a 130/30 fund is shown in Exhibits 10.17 and 10.18 based on data from
Table 10.7.
--- page 254 ---

JWBK178-10
JWBK178-Bacon
July 30, 2008
7:5
Char Count= 0
244
Practical Portfolio Performance Measurement and Attribution
Exhibit 10.17
130/30 fund asset allocation
Geometric asset allocation for data in Table 10.7 is:
(1
bS)
(1
b)
1
1 093
1 1
1
0 64%
Individual country asset allocation effects are:
UK equities
(120%
130%)
1 10
1 10
1
0 00%
Short UK equities
( 30%
30%)
1 10
1 10
1
0 00%
Cash
(10%
0%)
1 03
1 10
1
0 64%
Total
0 0%
0 0%
0 64%
0 64%
Exhibit 10.18
130/30 fund stock selection
Geometric stock selection including interaction for data in Table 10.7 is:
(1
r)
(1
bS)
1
1 144
1 93
1
4 67%
Individual country stock selection effects are:
UK equities
120%
1 14
1 10
1
1 10
1 093
4 39%
Short UK equities
30%
1 09
1 10
1
1 10
1 093
0 27%
Cash
10%
1 03
1 03
1
1 03
1 093
0 0%
Total
4 39%
0 27%
0 0%
4 67%
Table 10.7
130/30 fund attribution
Stock selection
i
1
ri
1
bi
1
(1
bi)
(1
bS)
(%)
Asset
allocation
(
i
Wi)
1
bi
1
b
1
(%)
Portfolio
Benchmark Portfolio Benchmark
weight
i
weight Wi
return ri
return bi
(%)
(%)
(%)
(%)
UK equities
120
130
14.0
10.0
0.00
4.39
Short UK equities
30
30
9.0
10.0
0.00
0.27
Cash
10
0
3.0
3.0
0.64
0.00
Total
100
100
14.4
10.0
0.64
4.67
--- page 255 ---

JWBK178-10
JWBK178-Bacon
July 30, 2008
7:5
Char Count= 0
Performance Measurement for Derivatives
245
It’s worth noting in this attribution that since the UK equity benchmark is equal to the
overall benchmark there are no asset allocation effects in the long or short positions, only from
any allocation to cash; in this case an overweight position leading to a negative allocation
of
0.64%. However, outperformance in the long sector is leveraged by 20% with a 120%
allocation and there is an additional contribution because the shorted stocks underperformed
the benchmark. Notice that the benchmark retained 100% allocation to UK equities.
--- page 256 ---

JWBK178-11
JWBK178-Bacon
March 18, 2008
17:50
Char Count= 0
11
Performance Presentation Standards
There are three ways of losing money – horses, women and taking the advice of experts,
Horses – that is the quickest
women – that is the most pleasant; but
taking the advice of experts – that is the most certain.
Apocryphally attributed to M. Pompidou
WHY DO WE NEED PERFORMANCE
PRESENTATION STANDARDS?
The CFA Institute (formally known as the Association for Investment Management and Research or AIMR) sponsored the creation of the Global Investment Performance Standards
(GIPS, 2005) to provide an ethical framework for the calculation and presentation of the performance history (or track record) of asset management ﬁrms. GIPS are voluntary standards based
on the fundamental principles of full disclosure and fair representation of performance returns.
The need for the standards ﬁrst became apparent in the United States in the mid-1980s.
Pension funds, in seeking ﬁrms to manage their assets, would obviously see a large number
of presentations from asset managers, the overwhelming majority of which presented above
average performance. This begged the question: “Where are the below average managers?”
The answer, unfortunately, was that some of the below average managers were presenting
above average returns.
Asset managers were very selective about the investment track records they presented to
potential clients. Most marketing managers would be well aware over which time period they
performed best and would consequently “cherry pick” the best period to show performance.
Often single representative accounts would be used to calculate the ﬁrm’s track record. Invariably, the representative account would be one of the better performing accounts for that
investment strategy. If the representative account performed badly a rationale would be found
to choose a new one. Managers might also be selective in the choice of calculation methodology as demonstrated in Chapter 2. Often the performance track records presented by assets
managers were not a fair and honest representation of the performance they had delivered to
their existing clients.
TheresultwasthecreationoftheAIMRPerformancePresentationStandards(1987)(AIMR-
PPS),voluntaryperformanceguidelinesfortheNorthAmericanmarket.IntheUnitedKingdom
the National Association of Pension Funds (NAPF, 1992) produced its own guidelines for balanced pension funds encouraged by one of the principal recommendations of a Committee of
Enquiry into Investment Performance Measurement also initiated by the NAPF (1990). My
interest in the standards developed at this time. I wished to bring my ﬁrm, a London-based
subsidiary of a large US bank, into compliance with both the AIMR-PPS and the NAPF guidelines, and it proved impossible to achieve both. The AIMR-PPS standards and the NAPF
guidelines shared the same ethical objectives yet in certain regards they were contradictory.
247
Practical Portfolio Performance Measurement
and Attribution, Second Edition
By Carl R. Bacon
Copyright © 2008 John Wiley & Sons Ltd.
--- page 257 ---

JWBK178-11
JWBK178-Bacon
March 18, 2008
17:50
Char Count= 0
248
Practical Portfolio Performance Measurement and Attribution
With responsibility for a variety of European ofﬁces I could envisage the nightmare scenario
of a separate set of contradictory standards in each European ofﬁce. It was clear a set of global
standards was required.
GLOBAL INVESTMENT PERFORMANCE STANDARDS (GIPS
R )
In 1995 the CFA Institute sponsored and funded the Global Investment Performance Standards
(GIPS R ) Committee to develop a single standard for presenting investment performance. The
objectives the committee set were to:
(1) Obtain worldwide acceptance of a standard for the calculation and presentation of investment performance in a fair, comparable format that provides full disclosure.
(2) Ensure accurate and consistent investment data for reporting, record keeping, marketing
and presentation.
(3) Promote fair, global competition among investment ﬁrms for all markets without creating
barriers to entry for new ﬁrms.
(4) Foster the notion of industry self-regulation on a global basis.
In a relatively short period this committee ﬁnalised the GIPS standards in February 1999 and,
having met its objectives, disbanded.
The GIPS committee was replaced by the Investment Performance Council (IPC) whose
principal goal was to have all countries adopt the GIPS standard.
To facilitate convergence the IPC promoted a transition from existing local standards to
GIPS by approving Country Versions of GIPS (CVGs) while updating the GIPS standards to
incorporate local best practice. The revised single standard was issued in February 2005 with
an effective start date of 1 January 2006.
This latest version of GIPS includes a number of improvements plus new sections on real
estate and private equity and effectively removes the need for CVGs. In 2006 the IPC was
transformed into the GIPS Executive Committee which now serves as the effective decisionmaking authority for the standards. The GIPS Executive Committee has created four permanent
standing subcommittees:
(1) GIPS Council.
(2) Interpretation subcommittee.
(3) Practitioners/Veriﬁers subcommittee.
(4) Investors/Consultants subcommittee.
The GIPS Council consists of country sponsors that have adopted the standards and provides
four members of the GIPS executive committee.
As at 30 November 2007 28 countries including all the major capital markets have adopted
GIPS, a full list is included in Table 11.1.
All subcommittee proposals are circulated for public comment (normally 60 days) prior to
their adoption and incorporation into the standards.
ADVANTAGES FOR ASSET MANAGERS
Theadvantagesofaglobalstandardforclientsareobvious;theycanselectassetmanagersbased
on good quality information with a certain level of conﬁdence that the numbers presented are a
fair and honest representation of that ﬁrm’s track record. For their own protection pension fund
--- page 258 ---

JWBK178-11
JWBK178-Bacon
March 18, 2008
17:50
Char Count= 0
Performance Presentation Standards
249
Table 11.1
GIPS Council country sponsors
Country
Sponsoring organization
Australia
Investment and Financial Services Association – Performance Analyst
Group
Austria
(1) ¨Osterreichischen Verreinigung f¨ur Finanzanalyse und Asset
Management and (2) Vereinigung ¨osterreichischer
Investmentgesellschaften
Denmark
The Danish Society of Financial Analysts and CFA Denmark
Belgium
Belgium Asset Managers Association
France
French Experts Group on Performance Presentation Standards
sponsored by (1) Soci´et´e Fran¸caise des Analystes Financiers and
(2) Association Fran¸caise de la Gestion Financi`ere
Germany
German Asset Management Standards Committee: (1) BVI
Bundesverband Investment und Asset Management e. V, (2) DVFA
Deutsche Vereinigung f¨ur Finanzanalys und Asset Management and
(3) German CFA Society
Hong Kong
The Hong Kong Society of Financial Analysts Limited
Hungary
CFA Society of Hungary
Ireland
Irish Association of Investment Managers
Italy
Italian Investment Performance Committee sponsored by:
(1) L’Associazione Bancaria Italiana, (2) L’Associazione Italiana
degli Analisti Finanziari, (3) Assogegtioni, (4) Sviluppo Mercato
Fondi Pensione, (5) Assirevi, (6) Italian CFA Society
Japan
The Security Analysts Association of Japan
Kazakhstan
Association of Financial and Investment Analysts
Korea
CFA Korea Society
Liechtenstein
Liechtenstein Bankers Association
Micronesian Region
Asia Paciﬁc Association for Fiduciary Studies
Netherlands
VBA – Beroepsvereniging van Beleggingsprofessionals
New Zealand
CFA Society of New Zealand
Norway
The Norwegian Society of Financial Analysts
Pakistan
CFA Association of Pakistan
Portugal
Associa¸c˜ao Portuguesa de Analista Financeiros
Singapore
Investment Management Association of Singapore
South Africa
Investment Management Association of South Africa
Spain
Asociaci´on Espa˜nola de Presentaci´on de Resultados de Gesti´on
Sweden
Swedish Society of Financial Analysts
Switzerland
Swiss Bankers Association
Ukraine
The Ukrainian Association of Investment Business
United Kingdom
UK Investment Performance Committee sponsored by: (1) Investment
Management Association (IMA), (2) Association of British Insurers,
and (3) The National Association of Pension Funds (NAPF)
United States and Canada
CFA Institute through its North American Investment Performance
Committee
--- page 259 ---

JWBK178-11
JWBK178-Bacon
March 18, 2008
17:50
Char Count= 0
250
Practical Portfolio Performance Measurement and Attribution
trustees should only hire asset managers that are compliant with the standards. Non-compliance
with the standards may suggest a weaker commitment to ethical standards or weak internal
controls insufﬁcient to claim compliance. If performance measurement controls are not best
practice, this may be an indication that other controls within the ﬁrm are weak.
For asset managers the advantages are less obvious and of course there is the cost of compliance to be offset; however, in my view the following advantages signiﬁcantly outweigh the
costs of compliance:
(1) Marketing advantage. Clearly, in the early stages of a standard an asset manager can gain
a marketing advantage by claiming compliance with a good quality standard. In the US it
has now become a marketing disadvantage not to be compliant, a situation that will arise
in Europe at some stage.
Many pension funds will not welcome ﬁrms into the selection process if they are not
compliant and in some circumstances if their claim of compliance is not independently
veriﬁed. Any trustee is taking the risk of future criticism or legal action by selecting an
asset manager that does not comply to performance presentation standards if subsequently
things go wrong and it is established that the original presentation was misleading.
(2) Level playing ﬁeld – international passport. The standards are designed to encourage
global competition and eliminate barriers to entry. In effect, GIPS allows asset managers
to market their track record worldwide with the knowledge that they are presenting to the
same standards as local competitors.
The pressure to present misrepresentative performance is not so great if asset managers
are conﬁdent that their competitors are operating to the same standard.
(3) Increased professionalism. To achieve compliance a ﬁrm must have good quality performance measurement processes and procedures in place and a commitment to the ethical
presentation of performance track records. This naturally increases the proﬁle and importance of performance measurers in the ﬁrm.
(4) Risk control. The standards require a basic level of risk control. Managers are required to
investigate outliers in their track record to justify that accounts are being managed within
the composite guidelines. This is good business practice, identifying poor performing
accounts early, ensuring good performance is real and ensuring the entire ﬁrm is aware
and understands the investment objectives and guidelines for each account.
(5) Business efﬁciency and data quality. Establishing effective procedures and improving performancemeasurementsystemsobviouslyrequiresinvestment;however,doingthingsright
ﬁrst time is obviously more efﬁcient than calculating performance incorrectly and wasting
time and resources investigating and correcting errors. Clearly, it’s very inefﬁcient if individual portfolio managers are wasting their time ensuring returns are calculated correctly.
THE STANDARDS
GIPS are ethical standards for investment performance presentation to ensure fair representation and full disclosure of a ﬁrm’s performance track record. The core of the standard is
reproduced in Appendix E.
Composites
GIPS require ﬁrms to include all discretionary portfolios in at least one “composite”, deﬁned
according to similar style or investment strategy. A composite should be representative of
--- page 260 ---

JWBK178-11
JWBK178-Bacon
March 18, 2008
17:50
Char Count= 0
Performance Presentation Standards
251
the ﬁrm’s performance with that investment strategy. All accounts managed to that strategy
including lost accounts must be included thus eliminating the practice of “cherry picking”
good performing accounts.
Initially, ﬁrms have complete ﬂexibility to deﬁne their own composites. This ﬂexibility
allows ﬁrms to differentiate their product offering and encourages the development of new
products.
The ﬁrm must decide between narrowly or widely deﬁned composites. Widely deﬁned
composites will include minor variations in strategy (for example, the ﬁrm might conclude
that the return series of a global equity account with a restriction disallowing investment in
Australia is very similar to an unrestricted global equity account and therefore both accounts
could coexist in a widely deﬁned global equity composite). Widely deﬁned composites are
easier to administer and allow the asset manager to present composites with larger assets under
management. Narrowly deﬁned composites are smaller and because small changes of strategy
must be closely monitored they are more difﬁcult to administer; however, the dispersion of
returns within the composite will be narrower indicating tighter investment controls.
Additional helpful guidance can be found in the Composite Construction Guidance Statement reproduced in Appendix F.
Presentation
GIPS require at least 5 years of performance history initially, presented annually, increasing to
10 years as the data becomes available. This avoids the “cherry picking” of time periods and
provides some information about the consistency of performance. I would recommend the presentation of quarterly performance information although this is not required. The standards also
require a number of disclosures designed to set the performance returns in their proper context.
By kind permission of GAM a typical GIPS performance presentation is shown in
Appendix G.
Calculation
Some ﬂexibility in the choice of calculation method is allowed but from 1 January 2001
portfolios must be valued at least monthly. From 1 January 2005 day-weighted cash ﬂow
(modiﬁed Dietz) methods must be used and from 1 January 2010 portfolios must be revalued
and the performance chain linked in the advent of a large cash ﬂow. The ﬁrm retains the
ﬂexibility to deﬁne what constitutes a large cash ﬂow. Returns can only be regarded as true
time-weighted if the portfolio is revalued for each cash ﬂow no matter how small. My strong
recommendation is to use true time-weighted returns to allow a fair comparison against other
managers and benchmarks.
To create composites returns for use in presentations, individual portfolio returns are combined using one of three asset-weighted methodologies:
(1) Beginning period weights.
(2) Beginning period weight plus cash ﬂows (in effect the denominator of the modiﬁed Dietz
method).
(3) Total aggregation (basically combining the assets of all the qualifying portfolios and calculating the return as a single portfolio).
These methodologies will lead to different results but there is no structural bias and all
are acceptable. For simplicity I would recommend beginning period weights. Clearly, larger
--- page 261 ---

JWBK178-11
JWBK178-Bacon
March 18, 2008
17:50
Char Count= 0
252
Practical Portfolio Performance Measurement and Attribution
portfolios have a more signiﬁcant inﬂuence on composite returns. Equal-weighted composites
were initially considered by the standard setters but declined because of the potential to “game”
results in small portfolios.
Composites must be asset-weighted at least quarterly from 1 January 2005 and monthly
from 1 January 2010. Monthly weighting is recommended.
More details are available in the Calculation Methodology Guidance Statement reproduced
in Appendix H.
Claim of compliance
Once a ﬁrm has met all of the required elements of GIPS the ﬁrm may claim compliance.
It is the ﬁrm that claims compliance; the claim is not speciﬁc to an individual presentation,
composite or client type.
Firms cannot pick and choose to whom they present compliant presentations. GIPS are
ethical standards, and in making a claim of compliance the ﬁrm is stating that all its performance
presentations are a fair and honest representation of historic performance.
Structure of the standards
The standards are divided into eight sections:
(1) Fundamentals of compliance. The ﬁrst section deals with the fundamentals of compliance, deﬁnition of the ﬁrm, documenting the ﬁrm’s policies and procedures, maintaining
compliance with updates to the standards and making a correct claim of compliance.
Firms must be deﬁned as an investment ﬁrm, subsidiary, or division held out to clients
as a distinct business entity, thus larger ﬁrms may include a number of GIPS deﬁned ﬁrms
although these ﬁrms should not overlap.
The ﬁrm’s policies and procedures with reference to the standards and performance
measurement are key documents required to achieve and maintain compliance.
(2) Input data. The Standards provide a blueprint for the consistency of input data crucial for
effective compliance and full and fair comparisons of investment performance.
(3) Calculation methodology. The standards mandate the use of certain calculation methodologies utilising the time-weighted approach. True time weighting and linked modiﬁed Dietz
are the two most common acceptable methodologies. Approximations using benchmarks
such as analyst’s test, index substitution and the regression method are not acceptable. Internal rates of return are only acceptable for venture capital/private equity. Valuations will
be required at the time of each cash ﬂow from 1 January 2010; in effect true time-weighted
returns.
Time-weighted returns are favoured in GIPS because of the need for comparability. For
fair comparison the impact of cash ﬂows must be removed. Requiring valuations at the point
of cash ﬂow increases the theoretical level of accuracy and removes the opportunity to game
returns by self-selecting the approximate methodology most advantageously impacted by
cash ﬂow. At present the standards require ﬁrms to adopt a policy for the treatment of
external cash ﬂow. For example, for managers using linked monthly modiﬁed Dietz as
standard, if the cash ﬂow is above a certain level, say 10% of portfolio assets, then managers
are required to change to a true time-weighted return by valuing the assets at the point of
cash ﬂow and chain linking the subperiod returns within the month.
--- page 262 ---

JWBK178-11
JWBK178-Bacon
March 18, 2008
17:50
Char Count= 0
Performance Presentation Standards
253
(4) Composite construction. A composite is an aggregation of a number of portfolios into a
single group that represents a particular investment strategy or objective.
Composite returns are asset-weighted using beginning period weights, beginning period
weights plus day-weighted cash ﬂows or simple aggregation. Equal weighting would allow
smaller portfolios (more easily manipulated) to disproportionably impact the performance
of the composite.
Appropriate documentation such as the investment management agreement or other
communication with the client must support the inclusion of any portfolio in a composite.
Every portfolio must belong to at least one composite (to avoid the performance record of
a poor performing account being lost), therefore composite deﬁnitions may overlap.
(5) Disclosures. Disclosures allow ﬁrms to provide more information relevant to the performance presentation. The standards include both required and recommended disclosures.
If in doubt the asset managers should add disclosure to assist the user of the performance
presentation.
(6) Presentation and reporting. Finally, after gathering input data, calculating returns, constructing composites and determining appropriate disclosures ﬁrms must present data
within the GIPS guidelines.
The standards are not so explicit at present but I would recommend all clients be provided
with a compliant presentation initially even if the client is not concerned by the standards.
A ﬁrm cannot pick and choose if it is compliant; the claim of compliance should mean
that all performance presentations are a fair and honest representation of performance.
(7) Real estate. The 1999 version of the standards did not include speciﬁc requirements for
real estate and private equity/venture capital asset categories. The 2005 version includes
real estate and private equity.
(8) Private equity. In addition to extensive additional disclosures and requirements private
equity is the only asset category allowed to use an internal rate of return methodology in
recognition of the lack of appropriate valuations at the time of external cash ﬂows.
VERIFICATION
Veriﬁcation is the review of the ﬁrm’s performance measurement processes and procedures by
an independent third party or “veriﬁer”.
Veriﬁcation tests:
(1) Whether the ﬁrm has complied with all the composite construction requirements ﬁrm wide.
(2) Whether the ﬁrm’s processes and procedures are designed to calculate and present performance in compliance with the GIPS standards.
Veriﬁcation is not yet mandatory but is strongly encouraged. Veriﬁcation not only brings
credibility to the claim of compliance but goes a long way to improve the performance
measurement process and provides assurance to the board that their claim of compliance is
accurate.
Compliance is non-trivial; claiming compliance without veriﬁcation is high risk. An erroneous claim of compliance could cause both signiﬁcant reputational damage and major
problems with regulators. I would recommend that veriﬁcation be undertaken at least annually.
The cost of veriﬁcation will be determined not only by the number of composites and
portfolios but also by the complexity of the business, the perceived quality of controls and
--- page 263 ---

JWBK178-11
JWBK178-Bacon
March 18, 2008
17:50
Char Count= 0
254
Practical Portfolio Performance Measurement and Attribution
the quality of performance measurement systems. Veriﬁcation can cost from as little as a few
thousand dollars to hundreds of thousands of dollars for large, complex businesses.
Veriﬁers need only be independent of the asset manager, and have a good understanding of
the standards and relevant practical experience. The asset manager must consider the quality
of the veriﬁer not only in terms of attaching their name to performance presentations but also in
the assurance given to the ﬁrm that the claim is accurate and the effectiveness of the veriﬁcation
process.
I see no conﬂict of interest in veriﬁcation ﬁrms providing pre-compliance consultancy; I
would certainly recommend that ﬁrms bring veriﬁers into the initial compliance process at a
very early stage.
Veriﬁcation/practitioners subcommittee
The veriﬁcation/practitioners subcommittee is composed of third-party service providers, including veriﬁers, software developers and custodians. They are in an excellent position to
identify areas of difﬁculty in the standards, misinterpretation (deliberate or otherwise) and
issues that add little value yet are expensive and troublesome to comply with.
Global veriﬁcation ﬁrms in particular are in a good position to ensure that there is no
divergence of practice worldwide and that the claim of compliance in one country means much
the same as the claim of compliance in another. Veriﬁers are able to identify areas in which
many ﬁrms are struggling to comply with the standards; if these areas do not add much value
then there is the opportunity to change the standards to encourage maximum uptake.
The writers of the standards face a constant dilemma between not making the standards too
onerous, encouraging ﬁrms to participate and providing sufﬁcient protection for the users of
the standards.
INTERPRETATIONS SUBCOMMITTEE
On publication the standards were well received; however, a standard can only be successful in
the long run if it is promoted and if it has the ability to respond to changes in market practice,
correct errors in the standards and to provide interpretation were required.
The interpretation subcommittee has the responsibility of ensuring the integrity, consistency
and applicability of the standards; in effect, it is the safety valve of standards. Errors, issues of
interpretation or responses to new developments or market trends can be addressed by issuing
“guidance statements”.
Guidance statements
Guidance statements are formal additions to the standards. Asset management ﬁrms and veri-
ﬁers are required to understand their content and keep up to date with the standards. The CFA
Institute provides an e-mail alert facility providing notiﬁcation of new guidance statements
(standards@cfainstitute.org). Information on GIPS, the GIPS Executive Committee and GIPS
Council, guidance statements and how to subscribe for the e-mail alert can be found on the CFA
Institute’s website at www.cfainstitute.org/standards. A selection of the more useful guidance
statements are discussed in more detail below.
--- page 264 ---

JWBK178-11
JWBK178-Bacon
March 18, 2008
17:50
Char Count= 0
Performance Presentation Standards
255
Deﬁnition of ﬁrm
The standards require ﬁrm-wide compliance to ensure poor performing accounts have not been
excluded from the performance track record. Once the ﬁrm has been deﬁned the exercise of
allocating accounts to composites can begin – it determines the universe of portfolios to be
allocated.
The ﬁrm deﬁnition must be meaningful, rational and fair. The deﬁnition cannot be used
narrowly to exclude poor performing product areas. The standards recommend the broadest,
most meaningful deﬁnition.
A ﬁrm may be deﬁned as an investment ﬁrm, subsidiary, or division held out to clients or
potential clients as a distinct business unit; or up to 1 January 2005 only, all assets managed
to one or more base currencies.
The currency option is a throwback to the original AIMR-PPS standards. UK ﬁrms keen
to participate in the AIMR standards successfully argued that they need only bring their US$
assets into compliance. This option is not available after 1 January 2005.
Although the broadest deﬁnition is recommended, it is acceptable to deﬁne a number of
ﬁrms within the same organization provided they meet the above criteria, with a view to
combining into one ﬁrm at a later date. Not all ﬁrms within a single organisation need be
compliant simultaneously, allowing part of the organisation time to work on bringing its ﬁrm
into compliance. This ﬂexibility is often used geographically although it should never be used
to exclude an underperforming part of the business.
The Deﬁnition of Firm Guidance Statement can be found in Appendix I.
Carve-outs
A carve-out is a subset of a portfolio’s assets used to create a track record for a narrower mandate
from a portfolio managed to a broader mandate. Carve-outs are permitted so that ﬁrms that
manage assets to a particular strategy in a broader portfolio can demonstrate competency in
that strategy even though they do not manage standalone portfolios in that strategy.
By their very nature carve-out returns offer greater potential to mislead than standalone
portfolios. Carve-outs by deﬁnition are portions of a larger portfolio the criteria for which are
determined by the ﬁrm. Because cash tends to act as a drag on performance (over the long
term we would expect markets to outperform cash) if cash is not included in the calculation
of the carve-out, the return may not be representative of what would have been achieved by
a standalone portfolio. The standards require that cash is allocated consistently to carve-outs
and at some future point will require that carve-outs be managed with their own cash balance.
Cash is one problem, there are others:
(1) Concentration. Because carve-outs are parts of larger portfolios they tend to contain a
smaller number of securities than a standalone portfolio and consequently are potentially
riskier.
(2) Currency. If the larger portfolio contains a currency overlay strategy it is very difﬁcult, if
not impossible, to isolate the currency allocation of the carve-out.
(3) Asset allocation. Within the larger portfolio, asset allocation “bets” are taken within the
context of the overall benchmark not the implied benchmark of the carve-out. In other
words, the carve-out may not be managed in the same way as a standalone portfolio.
(4) Bet size. Bet sizes are exaggerated with carve-outs – particularly if the carve-out is a small
percentage of the overall strategy.
--- page 265 ---

JWBK178-11
JWBK178-Bacon
March 18, 2008
17:50
Char Count= 0
256
Practical Portfolio Performance Measurement and Attribution
(5) Composite administration. Allocation of portfolios to composites becomes signiﬁcantly
more difﬁcult and expensive. For standalone portfolios it is easy to identify the number of
accounts and changes to investment guidelines. However, if carve-outs are used then all
carve-outs managed to that strategy must be allocated to that composite – the ﬁrm must
demonstrate that all carve-out strategies are included and that procedures are in place to
identify changes to carve-out strategies within larger portfolios.
I would strongly recommend that ﬁrms avoid the use of carve-outs and if absolutely required
only use if standalone portfolios are not available. I believe it is very difﬁcult to demonstrate that
the performance of a carve-out is representative of standalone performance. The Carve-outs
Guidance Statement can be found in Appendix J.
Signiﬁcant cash ﬂows
Signiﬁcant cash ﬂows, not to be confused with large cash ﬂows which are concerned with
performance measurement calculations, are external cash ﬂows of sufﬁcient size to cause the
portfolio not to be managed, for a temporary period, consistent with the investment objective
of the composite.
Given certain market conditions portfolio managers may not wish to invest new money
quickly particularly if they expect the market to fall. This may result in the portfolio not behaving in the same way as other existing portfolios in the composite, therefore it is logical to
remove such portfolios from the composite. If the portfolio manager’s timing decisions are
correct there will be a positive bias to the returns. The Signiﬁcant Cash Flow Guidance Statement, Appendix K, allows portfolios to be temporarily withdrawn. This is a sensible addition
to the standards; prior to 1 July 2002 this activity was speciﬁcally not allowed in the US CVG
because of the fear of the standard setters that such ﬂexibility was too easy to game, with the
result that it caused much confusion within the US.
Portability
The performance track record belongs to the ﬁrm not an individual. The standards take the
view that performance is generated by many factors (e.g. the support and guidance of senior
management, the research function, the dealing department, feedback from colleagues, the
performance team, the asset allocation committee, etc.) and therefore all the drivers of performance are not portable. The portfolio manager may be the major contributor, but could the
same performance have been delivered by that manager in a different environment?
In most cases the performance results of a prior ﬁrm cannot be used to represent the historical
record of a new afﬁliation or a new ﬁrm. Performance information of a prior ﬁrm can be shown
as supplemental information.
Prior performance can be linked with the performance of the new ﬁrm if all the following
conditions apply:
(1) Substantially all the investment decision makers are employed by the new ﬁrm.
(2) The staff and decision-making process remain intact.
(3) The new ﬁrm discloses that the performance results from the old ﬁrm are linked with
results from the new ﬁrm.
(4) The new ﬁrm has records that document and support the reported performance.
--- page 266 ---

JWBK178-11
JWBK178-Bacon
March 18, 2008
17:50
Char Count= 0
Performance Presentation Standards
257
(5) And with regard to a speciﬁc composite, substantially all the assets from the original ﬁrm’s
composite transfer to the new ﬁrm.
The standard is written to ensure that portability is difﬁcult to achieve and is most likely to occur
in the event of a merger or acquisition. The guidance statement is reproduced in Appendix L.
Supplemental information
Supplementalinformationisdeﬁnedasanyperformance-relatedinformationincludedaspartof
acompliantperformancepresentationthatsupplementsorenhancestherequired/recommended
disclosure and presentation provisions of GIPS.
Supplemental information is a powerful aid for ﬁrms that want to enhance the quality of their
presentation by providing more information. Supplemental information must satisfy the spirit
and principles of GIPS; it must not contradict a compliant presentation and must be clearly
labelled as supplemental since it is not covered by veriﬁcation.
Examples of supplemental information include attribution, ex ante risk analysis of a representative account and risk-adjusted performance.
Supplemental information must not be used to bypass the GIPS presentation standards,
although the standards in no way restrict any information being presented that is speciﬁcally
requested by the client. Given the opportunity to present potentially misleading supplemental
information asset managers should take great care with its use – the guidance statement can
be found in Appendix M.
Error correction
At the time of writing not all guidance statements had made their journey through the public
consultation and revision process, including the guidance statement on error correction.
Errors will occur, including but not restricted to:
(1) Valuation errors.
(2) Missed trades.
(3) Incorrectly timed cash ﬂows.
(4) Incorrect allocation of portfolios to composites.
(5) Missed or incorrect disclosures.
(6) Misprints.
Errors do not necessarily threaten the ﬁrm’s claim of compliance but they must be handled
correctly. Firms must decide whether previously reported returns should be recalculated and
whether or not clients should be informed of the error.
The draft guidance statement encourages the development of:
(1) Written policy and procedures for handling errors.
(2) A deﬁnition of materiality.
(3) An error correction process.
Clearly, materiality is an issue; no value is gained reissuing presentations if the error amounts
to one or two basis points but one or two whole percentage points might be a different matter.
Firms are free to deﬁne their own levels of materiality but are required to make available their
policies and procedures on error correction on request.
--- page 267 ---

JWBK178-11
JWBK178-Bacon
March 18, 2008
17:50
Char Count= 0
258
Practical Portfolio Performance Measurement and Attribution
The error correction process should:
(1) Recalculate returns.
(2) Determine if the error is material.
(3) Decide what action to take.
(4) Document the original presentation, the corrected presentation and the action taken.
MEASURES OF DISPERSION
In reviewing the performance of a composite it’s not only the asset-weighted returns that are
of interest but also the spread of returns within the composite, otherwise known as dispersion
or internal risk. A wide dispersion of returns might indicate weak investment controls within
the ﬁrm.
Thestandardsdonotmandateaparticularmeasureofdispersionandquiteafewareavailable.
Equal-weighted standard deviation
SD
Ri
¯R
2
n
(11.1)
where:
Ri
is the return on the ith portfolio
n
is the number of portfolios.
Asset-weighted dispersion
D
Wi
(Ri
R)2
(11.2)
where:
Wi
weight of the ith portfolio in the composite
R
composite return.
High–low
High–low is simply the highest and lowest returns within the composite for the period under
measurement. GIPS require a measure of dispersion for each year, therefore only the returns
of portfolios for the entire annual period should be included.
Interquartile range
Interquartile range is the difference between the 1st and 3rd quartiles (25th and 75th percentiles).
Both high–low and equal-weighted standard deviation are common measures. High–low is
too aggressive for me; either of the returns high or low might be outliers and hence not provide
a true measure of dispersion; interquartile range is a good alternative to high–low.
Dispersion measures are only relevant if there are sufﬁcient portfolios in the composite; for
ﬁve or fewer portfolios a dispersion measure need not be calculated.
