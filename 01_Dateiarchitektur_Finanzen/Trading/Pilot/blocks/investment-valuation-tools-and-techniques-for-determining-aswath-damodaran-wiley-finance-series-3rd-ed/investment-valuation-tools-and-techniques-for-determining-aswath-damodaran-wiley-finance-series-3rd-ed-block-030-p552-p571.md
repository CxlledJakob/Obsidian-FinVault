# INVESTMENT VALUATION TOOLS AND TECHNIQUES FOR DETERMINING -- Aswath Damodaran -- Wiley finance series, 3rd ed_, Hoboken, N_J, New Jersey, -- John -- isbn13 9781118011522 -- f84d1622bdc2de526da0dda803c52830 -- Anna’s.pdf — pages 552–571

--- page 552 ---

Definition
The value-to-book ratio is obtained by dividing the market value of both debt and
equity by the book value of capital invested in a ﬁrm:
If the market value of debt is unavailable, the book value of debt can be used in
the numerator as well. Needless to say, debt has to be consistently deﬁned for both
the numerator and denominator. For instance, if you choose to convert operating
leases to debt for computing market value of debt, you have to add the present
value of operating leases to the book value of debt as well.
There are two common variants of this multiple that do not pass the consistency test. One uses the book value of assets, which will generally exceed the book
value of capital by the magnitude of current liabilities, in the denominator. This
will result in price-to-book ratios that are biased down for ﬁrms with substantial
current liabilities. The other uses the enterprise value in the numerator, with cash
netted from the market values of debt and equity. Since the book value of equity incorporates the cash holdings of the ﬁrm, this will also bias the multiple down. If
you decide to use enterprise value in the numerator, you would need to net cash out
of the denominator as well. Netting out cash from book capital creates a measure
called invested capital:
Invested capital = BV of equity + BV of debt – Cash
In addition, the multiple may need to be adjusted for a ﬁrm’s cross holdings
just as EV/EBITDA multiples were. The adjustment was described in detail for the
enterprise value to EBITDA multiple in Chapter 18 and will require that you net
out the portion of the market value and book value of equity that is attributable to
subsidiaries.
Description
The distribution of the value-to-book ratio resembles that of the price-to-book
ratio. Figure 19.9 presents the distributions for EV/invested capital and value/book
capital ratios for U.S. companies in January 2011. As with the other multiples, it is
a heavily skewed and the average values are much higher than the medians: The
median EV/Invested capital for U.S. ﬁrms in January 2011 was 1.68 while the
median value-to-book ratio was 1.53. Note that there are 102 ﬁrms where
enterprise value is negative (because cash exceeds the combined market values of
debt and equity).
Enterprise value to
Invested capital
= Market value of equity
Market value of debt
Cash
+
−
Book value of equity
Book value of debt
Cash
+
−
Value-to-book ratio = Market value of equity
Market value of debt
+
Book value of equity
Book value of debt
+
Value-to-Book Ratios
533
--- page 553 ---

One of the interesting by-products of switching from price-to-book ratios to
value-to-book ratios is that we lose no ﬁrms in the sample with value-to-book
ratios and only 102 ﬁrms with EV/invested capital.
Analysis
The value-to-book ratio is a ﬁrm value multiple. To analyze it, we go back to a free
cash ﬂow to the ﬁrm valuation model, and use it to value a stable growth ﬁrm:
Substituting in FCFF = EBIT1(1 – t)(1 – Reinvestment rate), we get:
Dividing both sides by the book value of capital, we get:2
Enterprise value
Invested capital
ROC(1
Reinvestment rate)
(Cost of capital
g)
=
−
−
 Enterprise value
EBIT
t
Reinvestment rate)
(Cost of capital
g)
1
=
−
−
−
(
)(
1
1
Enterprise value
FCFF
(Cost of capital
g)
1
=
−
534
BOOK VALUE MULTIPLES
FIGURE 19.9
EV/Invested Capital and Value to Book: U.S. Firms in January 2011
<0
0–0.01
0.01–0.25
0.25–0.5
0.5–0.75
0.75–1
1–1.25
1.25–1.5
1.5–1.75
1.75–2
2–2.25
2.25–2.5
2.5–2.75
2.75–3
3–3.5
3.5–4
4–4.5
4.5–5
5–10
>10
EV/Invested Capital
Value/Book
0
100
200
300
400
500
600
700
800
pbvdata.xls: This dataset on the Web summarizes value-to-book multiples and
fundamentals by industry group in the United States for the most recent year.
2As with the return on equity, if return on capital is deﬁned in terms of contemporaneous
earnings (ROC = EBIT0/Book capital), there will be an extra (1 + g) in the numerator.
--- page 554 ---

The value-to-book ratio is fundamentally determined by its return on capital—
ﬁrms with high returns on capital tend to have high value-to-book ratios. In fact, the
determinants of value-to-book mirror the determinants of price-to-book equity, but
we replace equity measures with ﬁrm value measures—the ROE with the ROC, the
cost of equity with the cost of capital, and the payout ratio with (1 – Reinvestment
rate). In fact, if we substitute in the fundamental equation for the reinvestment rate:
Reinvestment rate = g/ROC
The analysis can be extended to cover high-growth ﬁrms, with the value-to-book
capital ratio determined by the return on capital, cost of capital, growth rate, and
reinvestment—in the high growth and stable growth periods:
where ROC = Return on capital (hg: high-growth period; st: stable-growth period)
RIR = Reinvestment rate (hg: high-growth period; st: stable-growth period)
kc = Cost of capital (hg: high-growth period; st: stable-growth period)
ROC
RIR
g
g
k
k
g

RIR
g
g
k
g
k
Enterprise value0
hg
hg
n
c,hg
n
c,hg
st
n
n
c,st
n
c,hg
n
Invested capital0
1
1
1
1
1
1
1
1
1
=
×
−
×
+
×
−
+
+
⎡
⎣
⎢
⎢
⎤
⎦
⎥
⎥
−
+ ROChg ×
−
×
+
×
+
−
+
(
)
(
)
(
)
(
)
(
)
(
)
(
)
(
)(
)
Enterprise value
Invested capital
(ROC
g)
(Cost of capital
g)
=
−
−
Value-to-Book Ratios
535
ROC, ROIC, ROA, AND ROE
We have emphasized the importance of measuring the returns generated by a
ﬁrm on its investments through both the DCF and relative valuation sections,
but we have used different measures of accounting returns: return on equity, return on capital, and return on invested capital. In fact, there are many who also
compute return on assets as a measure. So, how do they relate to each other,
and which one should you use?
Let’s start with what they have in common. They all relate current earnings in the numerator to the book value in the denominator, but they measure
earnings and book value differently.
• With return on equity, we divide earnings to equity investors (net income)
by the book value of equity to get a measure of how much return is being
earned by equity investors. This is the measure we use when our comparison metric is the cost of equity and to get growth rates in equity earnings
(for the dividend discount and FCFE models).
ﬁrmmult.xls: This spreadsheet allows you to estimate ﬁrm value multiples for a
stable-growth or high-growth ﬁrm, given its fundamentals.
(continued)
--- page 555 ---

Application
The value-to-book ratios can be compared across ﬁrms just as the price-to-book
value of equity ratio was in the preceding section. The key variable to control for in
making this comparison is the return on capital. The value matrix developed for
price-to-book ratios can be adapted for the value-to-book ratio in Figure 19.10.
Firms with high return on capital will tend to have high value-to-book value ratios,
whereas ﬁrms with low return on capital will generally have lower value-to-book
ratios.
This matrix also yields an interesting link to a widely used value enhancement
measure—economic value added (EVA). One of the biggest sales pitches for EVA,
which is computed as the product of the return spread (ROC minus cost of capital)
and capital invested, is its high correlation with market value added (MVA) which
is deﬁned as the difference between market value and book value of capital. This is
not surprising, since MVA is a variant on the value-to-book ratio and EVA is a variant on the return spread.
Is the link between value-to-book and return on capital stronger or weaker
than the link between price-to-book and return on equity? To examine this question, we regressed the EV/invested capital (IC) against return on capital using data
on all U.S. ﬁrms from January 2011:
EV/IC = 1.48 + 7.20 Growth in revenue – 2.31 D/C + 6.99 ROIC
[13.04][7.96]
[12.32]
[23.55]
R2 = 57%
where D/C = Total debt/(Total debt + Market value of equity)
ROC = Return on capital
The regression yields results similar to those obtained for price-to-book ratios.
If the results from using value-to-book and price-to-book ratios parallel each
other, why would you choose to use one multiple over the other? The case for using
value-to-book ratios is stronger for ﬁrms that have high and/or shifting leverage.
536
BOOK VALUE MULTIPLES
• We use return on capital (ROC) and return on invested capital (ROIC)
interchangeably and obtain them by dividing operating income by the
book value of invested capital; this is the sum of the book value of
debt and equity with cash netted out. We compare this return to the
cost of capital and to derive growth rates in operating income (for
FCFF calculations).
• The return on assets is a mixed measure that really does not ﬁt in well.
Since it is obtained by dividing net income or operating income by total
assets, it is not directly comparable to either cost of equity or capital. We
would suggest that it not be used in valuation.
Finally, we prefer to compute all of these returns by taking the income in a
given year and dividing by the book value at the end of the prior year. There
are others who prefer to use the average over the year, and if that is the practice, it should be followed consistently.
--- page 556 ---

Firms can use leverage to increase their returns on equity, but in the process they
also increase the volatility in the measure: in good times they report very high
returns on equity, and in bad times, very low or negative returns on equity. For such
ﬁrms, the value-to-book ratio and the accompanying return on capital will yield
more stable and reliable estimates of relative value. In addition, the value-to-book
ratio can be computed even for ﬁrms that have negative book values of equity and
is thus less likely to be biased.
TOBIN’S Q: MARKET VALUE/REPLACEMENT COST
James Tobin presented an alternative to traditional ﬁnancial measures of value by
comparing the market value of an asset to its replacement cost. His measure, called
Tobin’s Q, has several adherents in academia but still has not broken through into
practical use, largely because of problems in getting the necessary information.
Tobin’s Q: Market Value/Replacement Cost
537
FIGURE 19.10
Valuation Matrix: Value to Book and Excess Returns
Return on Capital—Cost of Capital
High Value to Book
High Return Spread
Low Value to Book
Low Return Spread
Low Value to Book
High Return Spread
High Value to Book
Low Return Spread
Overvalued
Value/Book
Undervalued
pbvreg.htm: This dataset on the Web reports the results of the latest regression of PE
ratios against fundamentals, using all ﬁrms in the market.
--- page 557 ---

Definition
Tobin’s Q is estimated by dividing the market value of a ﬁrm’s assets by the replacement cost of these assets.
Tobin’s Q = Market value of assets in place/Replacement cost of assets in place
In cases where inﬂation has pushed up the replacement cost of the assets or
where technology has reduced the cost of the assets, this measure may provide a
more updated measure of the value of the assets than accounting book value. The
rationale for the measure is simple. Firms that earn negative excess returns and do
not utilize their assets efﬁciently will have a Tobin’s Q that is less than 1. Firms that
utilize their assets more efﬁciently will trade at a Tobin’s Q that exceeds 1.
While this measure has some advantages in theory, it does have some practical
problems. The ﬁrst is that the replacement value of some assets may be difﬁcult to
estimate, especially if assets are not traded on a market. The second is that even
where replacement values are available, substantially more information is needed
to construct this measure than the traditional price–book value ratio. In practice,
analysts often use shortcuts to arrive at Tobin’s Q, using book value of assets as a
proxy for replacement value and market value of debt and equity as a proxy for the
market value of assets. In these cases, Tobin’s Q resembles the value-to-book value
ratio described in the preceding section.
Description
If we use the strict deﬁnition of Tobin’s Q, we cannot get a cross-sectional distribution of the multiple because the information to estimate it is neither easily accessible
nor even available. This is a serious impediment to using the multiple because we
have no sense of what a high, low, or average number for the multiple would be. For
instance, assume that you ﬁnd a ﬁrm trading at 1.2 times the replacement cost of the
assets. You would have no way of knowing whether you were paying too much or
too little for this ﬁrm without knowing the summary statistics for the market.
Analysis
The value obtained from Tobin’s Q is determined by two variables—the market
value of the ﬁrm and the replacement cost of assets in place. In inﬂationary times,
when the cost of replacing assets increases over time, Tobin’s Q will generally be
lower than the unadjusted price–book value ratio, and the difference will increase
for ﬁrms with older assets. Conversely, if the cost of replacing assets declines much
faster than the book value (because of technological changes), Tobin’s Q will generally be higher than the unadjusted price–book value ratio.
Tobin’s Q is also determined by how efﬁciently a ﬁrm manages its assets
and extracts value from them relative to the next best bidder. To see why, note that
the market value of an asset will be equal to its replacement cost when assets earn
their required return. (If the return earned on capital is equal to the cost of capital,
investments have a zero net present value, and the present value of the cash ﬂows
from the investment will be equal to the replacement cost.) Carrying this logic forward, Tobin’s Q will be less than 1 if a ﬁrm earns less than its required return on investments, and more than 1 if it earns positive excess returns.
538
BOOK VALUE MULTIPLES
--- page 558 ---

Applications
Tobin’s Q is a practical measure of value for a mature ﬁrm with most or all of its
assets in place, where replacement cost can be estimated for the assets. Consider, for
example, a steel company with little or no growth potential. The market value of this
ﬁrm can be used as a proxy for the market value of its assets, and you could adjust
the book value of the assets owned by the ﬁrm for inﬂation. In contrast, estimating
the market value of assets owned would be difﬁcult for a high-growth ﬁrm, since the
market value of equity for this ﬁrm will include a premium for future growth.
Tobin’s Q is more a measure of the perceived quality of a ﬁrm’s management
than it is of misvaluation, with poorly managed ﬁrms trading at market values that
are lower than the replacement cost of the assets that they own. In fact, several
studies have examined whether such ﬁrms are more likely to be taken over. Lang,
Stulz, and Walkling (1991) concluded that ﬁrms with low Tobin’s Q are more likely
to be taken over for purposes of restructuring and increasing value. They also ﬁnd
that shareholders of high Tobin’s Q bidders gain signiﬁcantly more from successful
tender offers than shareholders of low Tobin’s Q bidders.
CONCLUSION
The relationship between price and book value is much more complex than most
investors realize. The price–book value ratio of a ﬁrm is determined by its expected
payout ratio, its expected growth rate in earnings, and its riskiness. The most important determinant, however, is the return on equity earned by the ﬁrm—higher
returns lead to higher price–book value ratios, and lower returns lead to lower PBV
ratios. The mismatch that should draw investor attention is the one between return
on equity and price–book value ratios—high price–book value ratios with low returns on equity (overvalued) and low price–book value ratios with high returns on
equity (undervalued).
The value-to-book ratio is the ﬁrm value analogue to the price-to-book ratio,
and it is a function of the return on capital earned by the ﬁrm, its cost of capital,
and the reinvestment rate. Again, though, ﬁrms with low value-to-book ratios and
high expected returns on capital can be viewed as undervalued.
QUESTIONS AND SHORT PROBLEMS
In the problems following, use an equity risk premium of 5.5 percent if none is
speciﬁed.
1. Answer true or false to the following statements, with a short explanation.
a. A stock that sells for less than book value is undervalued.
True ____
False ____
b. If a company’s return on equity drops, its price–book value ratio will generally drop more than proportionately (e.g., if the return on equity drops by
half, the price–book value ratio will drop by more than half).
True ____
False ____
c. A combination of a low price–book value ratio and a high expected return on
equity suggests that a stock is undervalued.
True ____
False ____
Questions and Short Problems
539
--- page 559 ---

d. Other things remaining equal, a higher-growth stock will have a higher price–
book value ratio than a lower-growth stock.
True ____
False ____
e. In the Gordon growth model, ﬁrms with higher dividend payout ratios will
have higher price–book value ratios.
True ____
False ____
2. NCH Corporation, which markets cleaning chemicals, insecticides, and other
products, paid dividends of $2 per share in 1993 on earnings of $4 per share.
The book value of equity per share was $40, and earnings were expected to
grow 6% a year in the long term. The stock had a beta of 0.85, and was selling
for $60 per share. (The Treasury bond rate was 7%, and the market risk premium was 5.5%.)
a. Based on these inputs, estimate the price–book value ratio for NCH.
b. How much would the return on equity have to increase to justify the
price–book value ratio at which NCH was selling for in 1993?
3. You are analyzing the price–book value ratios for ﬁrms in the trucking industry,
relative to returns on equity and required rates of return. The data on the companies is as follows:
Company
PBV
ROE
Beta
Builders Transport
2.00
11.5%
1.00
Carolina Freight
0.60
5.5%
1.20
Consolidated Freight
2.60
12.0%
1.15
J.B. Hunt
2.50
14.5%
1.00
M.S. Carriers
2.50
12.5%
1.15
Roadway Services
3.00
14.0%
1.15
Ryder System
2.25
13.0%
1.05
Xtra Corporation
2.80
16.5%
1.10
The Treasury bond rate is 7%, and the market risk premium is 5.5%.
a. Compute the average PBV ratio, return on equity, and beta for the industry.
b. Based on these averages, are stocks in the industry underor overvalued relative to book values?
4. United Healthcare, a health maintenance organization, is expected to have
earnings growth of 30% for the next ﬁve years and 6% after that. The dividend payout ratio will be only 10% during the high growth phase, but will
increase to 60% in steady state. The stock has a beta of 1.65 currently, but
the beta is expected to drop to 1.10 in steady state. (The Treasury bond rate is
7.25%.)
a. Estimate the price–book value ratio for United Healthcare, given the inputs
as given.
b. How sensitive is the price–book value ratio to estimates of growth during the
high growth period?
c. United Healthcare trades at a price–book value ratio of 7.00. How long
would extraordinary growth have to last (at a 30% annual rate) to justify
this PBV ratio?
5. Johnson & Johnson, a leading manufacturer of health care products, had a return on equity of 31.5% in 1993, and paid out 37% of its earnings as dividends.
The stock had a beta of 1.25. (The Treasury bond rate was 6%, and the risk premium was 5.5%.) The extraordinary growth was expected to last for 10 years,
540
BOOK VALUE MULTIPLES
--- page 560 ---

after which the growth rate was expected to drop to 6% and the return on
equity to 15% (the beta would move to 1).
a. Assuming the return on equity and dividend payout ratio continue at current levels for the high growth period, estimate the PBV ratio for Johnson &
Johnson.
b. If health care reform passes, it is believed that Johnson & Johnson’s return
on equity will drop to 20% for the high growth phase. If the company
chooses to maintain its existing dividend payout ratio, estimate the new
PBV ratio for Johnson & Johnson. (You can assume that the inputs for the
steady state period are unaffected.)
6. Assume that you have done a regression of PBV ratios for all ﬁrms on the New
York Stock Exchange, and arrived at the following result:
PBV = 0.88 + 0.82 Payout + 7.79 Growth – 0.41 Beta + 13.81 ROE
R2 = 0.65
where
Payout = Dividend payout ratio during most recent period
Growth = Projected growth rate in earnings over next ﬁve years
Beta = Beta of the stock in most current period
To illustrate, a ﬁrm with a payout ratio of 40%, a beta of 1.25, a ROE of
25%, and expected growth rate of 15% would have had a price–book value
ratio of:
PBV = 0.88 + 0.82(0.4) + 7.79(.15) – 0.41(1.25) + 13.81(.25) = 5.3165
a. What use, if any, would you put the R-squared of the regression to?
b. Assume that you have also run a sector regression on a company and estimated a price-to-book ratio based on that regression. Why might your result
from the market regression yield a different result from the sector regression?
7. SoftSoap Corporation is a large consumer product ﬁrm that reported after-tax
operating income of $600 million in a recent ﬁnancial year. At the beginning of
the year, the ﬁrm reported book value of equity of $4 billion and book value of
debt of $1 billion. The market value of equity was $8 billion, the market value
of debt was $1 billion, and the ﬁrm had a cost of equity of 11% and an aftertax cost of debt of 4%. If the ﬁrm is in stable growth, expecting to grow 4% a
year in perpetuity, estimate the correct value-to-book value ratio for the ﬁrm.
8. Lyondell Inc. is a conglomerate with a value-to-book capital ratio of 2.0. If the
ﬁrm is in stable growth, expecting to grow 4% a year in perpetuity, and has a
cost of capital of 10%, what return on capital is the market assuming in perpetuity for Lyondell?
9. Estimate the value-to-book capital ratio for Zapata Enterprises, a trading ﬁrm
in high growth, with the following characteristics:
High Growth
Stable Growth
After-tax return on capital
15%
12%
Expected growth rate
12%
4%
Cost of capital
10%
9%
If high growth is expected to last 10 years, estimate the correct value-to-book
ratio for Zapata.
10. If Tobin’s Q is computed by dividing the market value of traded equity and
debt by the book value of assets, you will overestimate the value for highgrowth ﬁrms. Explain why.
Questions and Short Problems
541
--- page 561 ---

542
CHAPTER 20
Revenue Multiples and
Sector-Speciﬁc Multiples
W
hile earnings and book value multiples are intuitively appealing and widely
used, analysts in recent years have increasingly turned to alternative multiples
to value companies. For young ﬁrms that have negative earnings, multiples of
revenues have replaced multiples of earnings. In addition, these ﬁrms are being
valued on multiples of sector-speciﬁc measures such as the number of customers,
subscribers, or even web site visitors (for new economy ﬁrms). In this chapter, the
reasons for the increased use of revenue multiples are examined ﬁrst, followed by
an analysis of the determinants of these multiples and how best to use them in
valuation. This is followed by a short discussion of the sector-speciﬁc multiples,
the dangers associated with their use and the adjustments that might be needed to
make them work.
REVENUE MULTIPLES
A revenue multiple measures the value of the equity or a business relative to the revenues that it generates. As with other multiples, other things remaining equal, ﬁrms
that trade at low multiples of revenues are viewed as cheap relative to ﬁrms that
trade at high multiples of revenues.
Revenue multiples have proved attractive to analysts for a number of reasons.
First, unlike earnings and book value ratios, which can become negative for many
ﬁrms and thus not meaningful, revenue multiples are available even for the most troubled ﬁrms and for very young ﬁrms. Thus, the potential for bias created by eliminating ﬁrms in the sample is far lower. Second, unlike earnings and book value, which
are heavily inﬂuenced by accounting decisions on depreciation, inventory, research
and development (R&D), acquisition accounting, and extraordinary charges, revenue
is relatively difﬁcult to manipulate. Third, revenue multiples are not as volatile as
earnings multiples, and hence are less likely to be affected by year-to-year swings in a
ﬁrm’s fortunes. For instance, the price-earnings ratio of a cyclical ﬁrm changes much
more than its price-sales ratios, because earnings are much more sensitive to economic
changes than revenues are.
The biggest disadvantage of focusing on revenues is that it can lull you into assigning high values to ﬁrms that are generating high revenue growth while losing
signiﬁcant amounts of money. Ultimately, a ﬁrm has to generate earnings and cash
ﬂows for it to have value. While it is tempting to use revenue multiples to value
--- page 562 ---

ﬁrms with negative earnings and book value, the failure to control for differences
across ﬁrms in costs and proﬁt margins can lead to misleading valuations.
Definition of Revenue Multiple
There are two basic revenue multiples in use. The ﬁrst, and more popular, one is the
multiple of the market value of equity to the revenues of a ﬁrm; this is termed the
price-to-sales ratio. The second, and more robust, ratio is the multiple of the value of
the operating assets to revenues; this is the EV-to-sales ratio.
As with the EBITDA multiple, we net cash out of ﬁrm value, because the income from cash is not part of revenue. The enterprise value-to-sales ratio is a more
robust multiple than the price-to-sales ratio because it is internally consistent. It divides the total value of the operating assets by the revenues generated by those assets. The price-to-sales ratio divides an equity value by revenues that are generated
for the ﬁrm. Consequently, it will yield lower values for more highly levered ﬁrms,
and may lead to misleading conclusions when price-to-sales ratios are compared
across ﬁrms in a sector with different degrees of leverage.
Accounting standards across different sectors and markets are fairly similar when it
comes to how revenues are recorded. There have been ﬁrms in recent years, though, that
have used questionable accounting practices in recording installment sales and
intracompany transactions to make their revenues higher. Notwithstanding these problems, revenue multiples suffer far less than other multiples from differences in accounting treatment  across ﬁrms.
Cross-Sectional Distribution
As with the earnings and book value multiples, the place to begin the examination
of revenue multiples is with the cross sectional distribution of price to sales and enterprise value to sales ratios across ﬁrms in the United States. Figure 20.1 summarizes this distribution in January 2011.
There are two things worth noting in this distribution. The ﬁrst is that revenue
multiples are skewed just like earnings or book value multiples. The second is that
the price-to-sales ratio is generally lower than the EV-to-sales ratio, which should
not be surprising since the former includes only equity while the latter considers
enterprise value.
Table 20.1 provides summary statistics on both the price to sales and the value
to sales ratios. The average values for both multiples are much higher than the median values, largely as the result of outliers—there are ﬁrms that trade at multiples
that exceed 100 or more.
Analysis of Revenue Multiples
The variables that determine the revenue multiples can be extracted by going back
to the appropriate discounted cash ﬂow models—dividend discount model (or an
FCFE valuation model) for price-to-sales ratios and a ﬁrm valuation model for
value-to-sales ratios.
Price-to-sales ratio
Market value of equity
Revenues

Value-to-sales ratio
Market value of equity + Market value of debt − Cash
Revenues
=
=
Revenue Multiples
543
--- page 563 ---

Price-to-Sales Ratios
The price-to-sales ratio for a stable ﬁrm can be extracted
from a stable growth dividend discount model:
where
P0 = Value of equity
DPS1 = Expected dividends per share next year
ke = Cost of equity
gn = Growth rate in dividends (forever)
P
DPS
k
g
0
1
e
n
=
−
544
REVENUE MULTIPLES AND SECTOR-SPECIFIC MULTIPLES
FIGURE 20.1
Revenue Multiples—U.S. ﬁrms in January 2011
0
100
200
300
400
500
600
0  To 0.01
0. 01 To 0.1
0.1 To 0.2
0.2 To 0.30
0.30 To 0.4
0.4 To 0.5
0.5 To 0.75
0.75 To 1
1 To 1.25
1.25 To 1.5
1.5 To 1.75
1.75 To 2
2 To 2.5
2.5 To 3
3 To 3.5
3.5 To 4
4 To 5
5 To 10
>10
PS Ratio
EV/Sales
TABLE 20.1
Price-to-sales and EV/Sales Multiples: Distributional
Statistics for U.S. ﬁrms in January 2011
PS Ratio
EV/Sales Ratio
Number of ﬁrms
4,766
4,766
Average
36.36
34.45
Median
1.30
1.48
25th percentile
0.55
0.32
75th percentile
3.10
3.29
psdata.xls: This dataset on the Web summarizes price-to-sales and value-to-sales
ratios and fundamentals by industry group in the United States for the most recent
year.
--- page 564 ---

Substituting in for DPS1 = EPS0(1 + gn)(Payout ratio), the value of the equity can be
written as:
Deﬁning the net proﬁt margin = EPS0/Sales per share, the value of equity can be
written as:
Rewriting in terms of the price-sales ratio,
The PS ratio is an increasing function of the proﬁt margin, the payout ratio, and the
growth rate, and a decreasing function of the riskiness of the ﬁrm.
The price-sales ratio for a high-growth ﬁrm can also be related to fundamentals. In the special case of the two-stage dividend discount model, this relationship can be made explicit fairly simply. With two stages of growth, a high-growth
stage and a stable-growth phase, the dividend discount model can be written as
follows:
where
g = Growth rate in the ﬁrst n years
ke,hg = Cost of equity in high growth
Payout = Payout ratio in the ﬁrst n years
gn = Growth rate after n years forever (stable growth rate)
ke,st = Cost of equity in stable growth
Payoutn = Payout ratio after n years for the stable ﬁrm
Rewriting EPS0 in terms of the proﬁt margin, EPS0 = Sales0 × Proﬁt margin, and
bringing Sales0 to the left-hand side of the equation, you get:
Price
Sales
Net margin
Payout ratio
g)
g)
(1+ k
g
k
Payout ratio
g
g)
(k
k
g
n
e,hg
n
e,hg
n
n
n
e,st
e,hg
n
n
×
=
+
×
×
−
+
⎡
⎣
⎢
⎢
⎤
⎦
⎥
⎥
−
+
+
×
+
×
+
−
⎧
⎨
⎪
⎪
⎪
⎩
⎪
⎪
⎪
⎫
⎬
⎪
⎪
⎪
⎭
⎪
⎪
⎪
(1
(1
)
(1
)
(1
)(1
)
1
P
EPS
Payout ratio
g)
g)
k
g
k
EPS
Payout ratio
g
g)
g
k
0
0
n
e,hg
n
e,hg
n
0
n
n
e,st
e,hg
n
n
=
×
×
×
+
−
+
+
⎡
⎣
⎢
⎢
⎤
⎦
⎥
⎥
−
+
×
×
×
+
+
+
−
(1
(1
)
(1
(1
)
(1
)(1
(k
)
1
P
Sales
PS
Net margin
Payout ratio
g
g
k
0
0
n
n
e
=
=
×
×
+
−
)
(1
P
Sales
Net margin
Payout ratio
g
g
k
0
n
0
n
e
=
×
×
+
×
−
)
(1
P
EPS
Payout ratio
g
g
k
0
n
0
n
e
=
×
×
+
−
)
(1
Revenue Multiples
545
--- page 565 ---

The left-hand side of the equation is the price-sales ratio. Holding all else constant, it is determined by:
■Net proﬁt margin: net income/revenues. The price-sales (PS) ratio is an increasing function of the net proﬁt margin. Firms with higher net margins, other
things remaining equal, should trade at higher price-to-sales ratios.
■Payout ratio during the high-growth period and in the stable period. The PS
ratio increases as the payout ratio increases, for any given growth rate.
■Riskiness (through the discount rate ke,hg in the high growth period and ke,st in
the stable period). The PS ratio becomes lower as riskiness increases, since
higher risk translates into a higher cost of equity.
■Expected growth rate in earnings, in both the high growth and stable phases. The
PS increases as the growth rate increases, in both the high-growth and stablegrowth periods.
As with the price-to-book ratio, you can substitute in the free cash ﬂows to equity for the dividends in making this estimate. Doing so will yield a more reasonable estimate of the price-to-sales ratio for ﬁrms that pay out dividends that are far
lower than they can afford to pay out.
As with the price-to-book ratio, the ﬁrm can have a different net margin during the
stable growth phase. That margin, though, will affect only the payout ratio during
the stable phase.
ILLUSTRATION 20.1:
Estimating the Price-to-Sales Ratio for a High-Growth Firm in the
Two-Stage Model
Assume that you have been asked to estimate the PS ratio for a ﬁrm that is expected to be in high
growth for the next ﬁve years. The following is a summary of the inputs for the valuation:
Growth rate in ﬁrst ﬁve years = 20%
Cost of equity = 6% + 1(5.5%) = 11.5%
Growth rate after ﬁve years = 8%
Payout ratio in ﬁrst ﬁve years = 20%
Beta = 1.0
Payout ratio after ﬁve years = 50%
Net proﬁt margin = 10%
Risk-free rate = T-bond rate = 6%
This ﬁrm’s price-to-sales ratio can be estimated as follows:
Based on this ﬁrm’s fundamentals, you would expect its equity to trade at 2.35 times revenues.
PS = 0.10×
×(
)×
⎡
⎣
⎢
⎤
⎦
⎥
+
×(1.08)
⎧
⎨
⎪0.2
⎪
⎩
⎪
⎪
⎫
⎬
⎪
⎪
⎭
⎪
⎪
= 2.35
1.20
1−
0.50×(1.20)
5
5
5
5
(1.20)
(1.115)
(.115−.20)
(.115−.08)(1.115)
Price
Sales
Net margin
FCFE
Earnings
g)
g)
k
g
k
FCFE
Earnings
g
g)
g
k
n
e,hg
n
e,hg
n
n
n
e,st
e,hg
n
n
×
=
⎛
⎝⎜
⎞
⎠⎟
+
×
×
−
+
+
⎡
⎣
⎢
⎢
⎤
⎦
⎥
⎥
−
+
⎛
⎝⎜
⎞
⎠⎟
+
×
+
×
+
−
⎧
⎨
⎪
⎪
⎪
⎪
⎩
⎪
⎪
⎪
⎪
⎫
⎬
⎪
⎪
⎪
⎪
⎭
⎪
⎪
⎪
⎪
(1
(1
)
(1
(1
)
(1
)(1
(k
)
1
546
REVENUE MULTIPLES AND SECTOR-SPECIFIC MULTIPLES
--- page 566 ---

ILLUSTRATION 20.2:
Estimating the Intrinsic Price-to-Sales Ratio for a High Growth Firm:
Whole Foods Markets in May 2011
Whole Foods Markets was founded as a grocery chain designed to provide alternatives for healthconscious shoppers, willing to pay a premium for organic food. The retailer grew signiﬁcantly between 2005 and 2010 and had more than 300 stores open by May 2011. The ﬁrm reported net income
of $246 million in 2010 on revenues of $9,006 million, giving it a net proﬁt margin of 2.73%:
Net proﬁt margin = Net income/Sales = $246/ $9,006 million = 2.73%
Based on its book value of equity of $1,628 million at the end of 2009, the ﬁrm generated a return on
equity of 15.11%:
We will assume that the ﬁrm will be able to maintain a growth rate in net income of 10% a year for the
next 10 years, while preserving its current net margin and return on equity. After the tenth year, we
will assume that the ﬁrm will be in stable growth, growing 3% a year in perpetuity, with a net margin
of 2.5% and a return on equity of 10%. To estimate the cost of equity, we will assume that the ﬁrm
has a beta of 1.00 for the high growth period and 0.90 in stable growth; the risk-free rate is 3.5% and
the equity risk premium is 5%. The inputs used in the estimation are summarized below:
High Growth
Stable Growth
Length of growth
10 years
Forever
Net margin
2.73%
2.50%
Sales/BV of equity
5.53
4.00
ROE
15.11%
10.00%
Payout ratio
1 −10%/15.11% = 33.82%
1 −3%/10% = 70%
Expected growth rate
10.00%
3.00%
Cost of equity
3.5% + 1(5%) = 8.50%
3.5% + .9(5%) = 8.00%
Note that we are backing out a payout ratio from the expected growth rate and ROE, rather than use
actual dividends paid. Consequently, we are effectively using FCFE instead of actual dividends. The
price-to-sales ratio, based on these inputs, is estimated here.
Whole Foods was trading at a price-to-sales ratio of 1.11 in May 2011, making it signiﬁcantly overvalued.
Value-to-Sales Ratios
To analyze the relationship between value and sales, consider the value of a stable-growth ﬁrm:
Enterprise value
EBIT(1 t)(1 Reinvestment rate)
Cost of capital
gn
=
−
−
−
1−(1.10)10
(1.085)10
0.085 − 0.10
(0.08 − 0.03)(1.10)10
+
(0.70)(1.10)10(1.03)
(0.3382)(1.10)
= 0.55
PS = 0.0273
Return on equity =
=
= 15.11%
Net income2010
Book value2009
$246
$1,628
Revenue Multiples
547
--- page 567 ---

Dividing both sides by the revenue, you get:
Just as the price-to-sales ratio is determined by net proﬁt margins, payout ratios, and costs of equity, the value-to-sales ratio is determined by after-tax operating margins, reinvestment rates, and the cost of capital. Firms with higher
operating margins (ATOM), lower reinvestment rates (for any given growth rate),
and lower costs of capital will trade at higher value-to-sales multiples.
This equation can be expanded to cover a ﬁrm in high growth by using a twostage ﬁrm valuation model:
where ATOM = After-tax operating margin = EBIT(1 −t)/Sales
RIR = Reinvestment rate (RIRn is for stable growth period)
kc = Cost of capital (hg: high growth and st: stable growth periods)
g = Growth rate in operating income in high growth and stable
growth periods
Note that the determinants of the EV-to-sales ratio remain the same as they were in
the stable growth model—the growth rate, the reinvestment rate, the operating
margin, and the cost of capital—but the number of estimates increases to reﬂect the
existence of a high growth period.
ILLUSTRATION 20.3:
Estimating the Intrinsic EV-to-Sales Ratio for a High Growth Firm: Coca-
Cola in May 2011
Coca-Cola has been successful in delivering high growth with impressive margins for decades. In
2010, Coca-Cola reported pretax operating income of $8,449 million on revenues of $35,119 million;
the tax rate for the company was approximately 40%. At the end of 2009, the ﬁrm had total capital invested of $31,679 million, leading to the following inputs:
Invested capital = BV of equity + BV of debt −Cash = 24,799 + 11,859 −4,979 = $31,679 million
After-tax operating margin = Operating income (1 −t)/ Revenues = 8,449/35,119 = 14.43%
Sales/capital = $35,119/$31,169 = 1.11
Return on invested capital = After-tax operating margin × Sales/Capital = 14.43% × 1.11 = 16%
EV/Sales = ATOM
RIR)
g)
g)
k
k
RIR
g)
g
g
k
n
c,hg
n
c,hg
n
n
n
c,st
c,hg
n
n
×
−
×
+
−
+
+
⎡
⎣
⎢
⎢
⎤
⎦
⎥
⎥
−
+
×
−
×
+
+
+
−
⎧
⎨
⎪
⎪
⎪
⎩
⎪
⎪
⎪
⎫
⎬
⎪
⎪
⎪
⎭
⎪
⎪
⎪
(1
(1
(1
)
(1
)
(1
(1
)
(1
)(1
(k
)
1
g
Enterprise value
Sales
[EBIT(1 t)/Sales](1
Reinvestment rate)
Cost of capital
g
Sales
After-tax operating margin(1
Reinvestment rate)
Cost of capital
g
n
Enterprise value0
n
=
−
−
−
=
−
−
548
REVENUE MULTIPLES AND SECTOR-SPECIFIC MULTIPLES
--- page 568 ---

We will assume that the ﬁrm will be able to maintain its current margin and return on capital for the
next 10 years, while reinvesting 60% of its after-tax operating income back into the business (the average over the past ﬁve years). During this period, we also assume that Coca-Cola will have a beta of
0.90 and a pretax cost of debt of 4.50%, and that it will remain at its existing debt-to-capital ratio of
7.23%, resulting in a cost of capital of 8.03% (the equity risk premium of 5.5% reﬂects Coca-Cola’s
exposure to emerging markets):
Cost of equity = Risk-free rate + Beta (Equity risk premium) = 3.5% + .9(5.5%) = 8.45%
Cost of capital = 8.45% (1 −.0723) + 4.5% (1 −.40) (.0723) = 8.03%
After year 10, we assume that Coca-Cola will be in stable growth, growing 3.5% a year, and that its
operating margin and sales-to-capital ratio will drop back toward (but not all the way to) industry averages (after-tax operating margin will be 12% and the sales-to-capital ratio will converge on 1). In stable
growth, we also assume that the beta for the company will be 1 and that the debt ratio will rise to 20%.
Cost of equity = 3.5% + 1 (5.5%) = 9%
Cost of capital = 9% (.80) + 4.5% (1 −.4) (.20) = 7.74%
The inputs that we will use to estimate the EV/Sales ratio for Coca-Cola are listed here:
High Growth
Stable Growth
Length of period
10
After year 5
After-tax operating margin
14.43%
12.00%
Sales/capital
1.11
1.00
Return on capital
16.00%
12%
Reinvestment rate
60%
3.5%/12% = 29.17%
Expected growth rate
9.60%
3.50%
Cost of capital
8.03%
7.74%
Plugging these numbers into the two-stage EV/Sales equation, we get:
Based on our inputs, the enterprise value for Coca-Cola should be 3.51 times revenues:
Expected enterprise value = $35,119 × 3.51 = $123,197 million
In May 2011, Coca-Cola’s market capitalization was $152,200 million. Incorporating the debt outstanding ($11,859 million) and the cash balance ($4,979 million) yields  an actual enterprise value of:
Actual enterprise value = $152,200 + $11,859 −$ 4,979 = $159,080 million
The company looks overvalued, based on our assumptions, by about 23%.
Revenue Multiples
549
ﬁrmmult.xls: This spreadsheet allows you to estimate the value-to-sales ratio for a
stable-growth or high-growth ﬁrm, given its fundamentals.
1−(1.096)10
(1.0803)10
0.09 − 0.10
+ (0.1443)
(1 − 0.60)(1.096)
= 0.55
EV/S = (0.1443)
(1 − 0.2917)(1.096)10 (1.035)
(0.0774 − 0.035)(1.0803)10
--- page 569 ---

Revenue Multiples and Profit Margins
The key determinant of revenue multiples is
the proﬁt margin—the net margin for price-to-sales ratios and operating margin for
value-to-sales ratios. Firms involved in businesses that have high margins can expect to sell for high multiples of sales. However, a decline in proﬁt margins has a
twofold effect. First, the reduction in proﬁt margins reduces the revenue multiple
directly. Second, the lower proﬁt margin can lead to lower growth and hence lead
to even lower revenue multiples.
The proﬁt margin can be linked to expected growth fairly easily if an additional term is deﬁned—the ratio of sales to book value (BV), which is also called a
turnover ratio. This turnover ratio can be deﬁned in terms of book equity (Equity
turnover = Sales/Book value of equity) or book capital (Capital turnover =
Sales/Book value of capital). Using a relationship developed between growth rates
and fundamentals, the expected growth rates in equity earnings can be written as a
function of net proﬁt margins and turnover ratios:
Expected growthequity = Retention ratio × Return on equity
= Retention ratio × (Net proﬁt/Sales) × (Sales/BV of equity)
= Retention ratio × Net margin × Sales/BV of equity
For example, in the valuation of Whole Foods in Illustration 20.2, the expected return on equity is 15.11%. This return on equity can be derived from Whole Foods’
net margin (2.73%) and sales-to-book value of equity ratio (5.53):
Net margin = 2.73%
Sales/BV of equity = $9,006/$1,628 = 5.53
Return on equity = 2.73% × 5.53 = 15.11%
For growth in operating income,
Expected growthﬁrm = Reinvestment rate × Return on capital
= Reinvestment rate × [EBIT(1 −t)/Sales]
× (Sales/BV of capital)
= Reinvestment rate × After-tax operating margin
× Sales/BV of capital
In the valuation of Coca-Cola in Illustration 20.3, the return on capital  is 16%.
This return on capital can be derived from Coca-Cola’s after-tax operating margin
(14.43%) and sales/capital ratio (1.11):
After-tax operating margin = 14.43%
Sales/invested capital = $35,119/$31,679 = 1.11
Return on capital = 14.43% × 1.11 = 16%
As the proﬁt margin is reduced, the expected returns on equity and capital will decrease, if the sales do not increase proportionately.
550
REVENUE MULTIPLES AND SECTOR-SPECIFIC MULTIPLES
--- page 570 ---

ILLUSTRATION 20.4:
Estimating the Effect of Lower Margins on Price-Sales Ratios
Consider again the ﬁrm analyzed in Illustration 20.1. If the ﬁrm’s proﬁt margin declines and total
revenue remains unchanged, the price-sales ratio for the ﬁrm will decline with it. For instance, if the
ﬁrm’s proﬁt margin declines from 10% to 5% and the sales/BV ratio remains unchanged:
New growth rate in ﬁrst ﬁve years = Retention ratio × Proﬁt margin × Sales/BV
= .8 × .05 × 2.50 = 10%
The new price-sales ratio can then be calculated as follows:
The relationship between proﬁt margins and the price-sales ratio is illustrated more comprehensively
in the Figure 20.2. The price-sales ratio is estimated as a function of the proﬁt margin, keeping the
sales/book value of equity ratio ﬁxed. This linkage of price-sales ratios and proﬁt margins can be utilized to analyze the value effects of changes in corporate strategy as well as the value of a brand
name.
PS = 0.05 ×
⎡
⎣
⎢
⎤
⎦
⎥
 +
 × 1.08
⎧
⎨
0.2 × 1.10 ×
⎪
⎪
⎩
⎪
⎪
⎫
⎬
⎪
⎪
⎭
⎪
⎪
= 0.77
1 −1.10
1.115
0.50 × 1.10
5
5
5
(.115 − .10)
5
(.115 − .08)(1.115)
Revenue Multiples
551
FIGURE 20.2
Price-to-Sales Ratios and Proﬁt Margins
--- page 571 ---

Marketing Strategy and Value
At the risk of oversimplifying pricing strategy, you can
argue that every ﬁrm has to decide whether it wants to go with a low-price, high-volume strategy (volume leader) or with a high-price, lower-volume strategy (price
leader). In terms of the variables that link growth to value, this choice will determine
the proﬁt margin and turnover ratio to use in valuation.
You could analyze the alternative pricing strategies that are available to a ﬁrm
by examining the impact that each strategy will have on margins and turnover, and
valuing the ﬁrm under each strategy. The strategy that yields the highest value for
the ﬁrm is, in a sense, the optimal strategy.
Note that the effect of price changes on turnover ratios will depend in large
part on how elastic or inelastic the demand for the ﬁrm’s products are. Increases in
the price of a product will have a minimal effect on turnover ratios if demand is
552
REVENUE MULTIPLES AND SECTOR-SPECIFIC MULTIPLES
MULTIPLES AND COMPANION VARIABLES
By this point in the relative valuation discussion, the process of deconstructing
multiples should no longer be a mystery. In fact, with each multiple, while we
have highlighted multiple variables that affect its value, there is one variable
that operates as a key driver. We call this variable the companion variable and
the table below lists it out for each multiple:
Multiple
Companion Variable
PE ratio
Expected growth rate in EPS
PBV
Return on equity
PS
Net margin
EV/EBITDA
Reinvestment rate
EV/Invested capital
Return on invested capital
EV/sales
After-tax operating margin
These variables matter for two reasons. The ﬁrst is that changes in the variables
have big effects on the multiples that they relate to. The second is that when a
stock looks cheap, because it has a low value on a multiple, the ﬁrst item to
check is the companion variable. Thus, if a stock trades at a low price-to-book
ratio, you should check its return on equity; most low price-to-book stocks have
low or negative returns on equity.
How do you ﬁnd the companion variable for a multiple? One way is to
run the market regression for the multiple against all of the independent variables that should determine it. The variable that has the most statistical signiﬁ-
cance (highest t statistic) is invariably the companion variable. The other, more
intuitive, approach is to do the following. If working with an equity multiple,
divide net income by the denominator of the multiple to get the companion
variable. With price-to-book value of equity, for instance, using this approach
would require dividing net income by the book value of equity, which would
yield the return on equity. With enterprise value multiples, dividing the aftertax operating income by the denominator should yield the companion variable. With EV-to-sales, for instance, dividing the after-tax operating income by
sales results in the after-tax operating margin.
