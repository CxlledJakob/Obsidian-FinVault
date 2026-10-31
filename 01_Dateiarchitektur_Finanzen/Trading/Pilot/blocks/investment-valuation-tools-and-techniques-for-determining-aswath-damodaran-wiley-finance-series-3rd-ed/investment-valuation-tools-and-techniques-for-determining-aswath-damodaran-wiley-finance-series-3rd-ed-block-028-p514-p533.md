# INVESTMENT VALUATION TOOLS AND TECHNIQUES FOR DETERMINING -- Aswath Damodaran -- Wiley finance series, 3rd ed_, Hoboken, N_J, New Jersey, -- John -- isbn13 9781118011522 -- f84d1622bdc2de526da0dda803c52830 -- Anna’s.pdf — pages 514–533

--- page 514 ---

In running the regression, especially when the sample contains ﬁrms with very
different levels of growth, you could transform the growth rate to make the relationship more linear. A scatter plot of PEG ratios against the natural log of the expected
growth rate, for instance, yields a much more linear relationship, as evidenced in
Figure 18.12.
The results of the regression of PEG ratios against ln(expected growth),
beta, and payout ratio are reported here for the entire market in January 2011.
Entire Market
PEG ratio = –1.07 – 1.18 ln(Growth) + 0.57 (Beta) + 0.54 (Payout)
[6.53] [18.51]
[8.55]
[3.57]
R-squared = 25.1%
Number of ﬁrms = 1608
The low R-squared is indicative of the problems with this multiple and the difﬁculties you will run into in using it in comparisons across ﬁrms.
ILLUSTRATION 18.11:
Revising the Beverage Sector in 2001—PEG Ratio
In the preceding chapter, we looked at the PE ratios for beverage companies and evaluated
whether Andres Wine was cheap because it traded at a low PE ratio. Since there are signiﬁcant differences in expected growth rates across the sector, we computed the PEG ratios for the ﬁrms and
The PEG Ratio
495
FIGURE 18.12
PEG Ratios versus ln(Expected Growth)—January 2011
−5.00
−4.00
−3.00
−2.00
−1.00
1.00
.00
In (Expected Growth)
.059367
.888694
1.095510
1.257847
1.418994
1.565581
1.755333
1.907545
2.084334
2.486799
2.281747
2.772748
3.165498
3.572789
4.274466
5.147534
8.255795
PEG Ratio
.580044
--- page 515 ---

report these along with the annualized standard deviations of stock prices over the previous two
years:
Trailing
Expected
Standard
Company Name
PE
Growth
Deviation
PEG
Coca-Cola Bottling
29.18
9.50%
20.58%
3.07
Molson Inc. Ltd. “A”
43.65
15.50%
21.88%
2.82
Anheuser-Busch
24.31
11.00%
22.92%
2.21
Corby Distilleries Ltd.
16.24
7.50%
23.66%
2.16
Chalone Wine Group
21.76
14.00%
24.08%
1.55
Andres Wines Ltd. “A”
8.96
3.50%
24.70%
2.56
Todhunter Int’l
8.94
3.00%
25.74%
2.98
Brown-Forman “B”
10.07
11.50%
29.43%
0.88
Coors (Adolph) “B”
23.02
10.00%
29.52%
2.30
PepsiCo, Inc.
33.00
10.50%
31.35%
3.14
Coco-Cola
44.33
19.00%
35.51%
2.33
Boston Beer “A”
10.59
17.13%
39.58%
0.62
Whitman Corp.
25.19
11.50%
44.26%
2.19
Mondavi (Robert) “A”
16.47
14.00%
45.84%
1.18
Coca-Cola Enterprises
37.14
27.00%
51.34%
1.38
Hansen Natural Corp.
9.70
17.00%
62.45%
0.57
Average
22.66
13.00%
0.33%
2.00
Note that Andres Wine is no longer looking cheap, if you compare that PEG ratio to the average; its
low growth rate translates into a higher PEG ratio. Hansen Natural still looks like a bargain, trading at
a PEG ratio of 0.57, well below the average for the sector.
Hansen is still riskier (its standard deviation is almost twice that of the sector) and has higher
growth than other ﬁrms in the sector, both of which can contribute to a lower PEG ratio. Regressing
the PEG ratios for ﬁrms in the sector, we obtain the following:
PEG = 3.61 −2.86 Expected growth rate −3.38 (Standard deviation)
[6.86] [0.75]
[2.04]
Using this regression to obtain a predicted value for Hansen Natural, we get:
PEGHansen = 3.61 −2.86(.1700) −3.38(.6245) = 1.01
At a PE ratio of 0.57, the ﬁrm remains signiﬁcantly undervalued.
496
EARNINGS MULTIPLES
Mreg.xls: This dataset on the Web summarizes the results of the most recent
regression of PEG ratios against fundamentals for U.S. stocks.
WHOSE GROWTH RATE?
In computing PEG ratios, we are often faced with the question of whose growth
rate we will use in estimating the PEG ratios. If the number of ﬁrms in the sample
is small, you could estimate expected growth for each ﬁrm yourself. If the number of ﬁrms increases, you will have no choice but to use analyst estimates of expected growth for the ﬁrms. Will this expose your analyses to all of the biases in
these estimates? Not necessarily. If the bias is uniform—for instance, analysts
overestimate growth for all of the ﬁrms in the sector—you will still be able to
make comparisons of PEG ratios across ﬁrms and draw reasonable conclusions.
--- page 516 ---

OTHER VARIANTS ON THE PE RATIO
While the PE ratio and the PEG ratio may be the most widely used earnings multiples, there are other equity earnings multiples that are also used by analysts. In this
section, three variants are considered. The ﬁrst is the relative PE ratio, the second is
a multiple of price to earnings in a future year (say 5 or 10 years from now), and
the third is a multiple of price to earnings prior to R&D expenses (used primarily
for technology ﬁrms).
Relative PE Ratios
Relative price earnings ratios measure a ﬁrm’s PE ratio relative to the market average. It is obtained by dividing a ﬁrm’s current PE ratio by the average for the
market:
Relative PE = Current PE ratioﬁrm/Current PE ratiomarket
Not surprisingly, the distribution of relative PE ratios mimics the distribution of the
actual PE ratios, with one difference—the average relative PE ratio is 1.
To analyze relative PE ratios, we will draw on the same model that we used to
analyze the PE ratio for a ﬁrm in high growth, but we will use a similar model to estimate the PE ratio for the market. Brought together, we obtain the following:
(j: ﬁrm
m: market)
Note that the relative PE ratio is a function of all of the variables that determine the
PE ratio—the expected growth rate, the risk of the ﬁrm, and the payout ratio—but
stated in terms relative to the market. Thus, a ﬁrm’s relative PE ratio is a function of
its relative growth rate in earnings per share (growth rateﬁrm/growth ratemarket), its relative cost of equity (cost of equityﬁrm/cost of equitymarket), and its relative return on
equity (ROEﬁrm/ROEmarket). Firms with higher relative growth, lower relative costs of
equity, and higher relative returns on equity should trade at higher relative PE ratios.
There are two ways in which relative PEs are used in valuation. One is to compare a ﬁrm’s relative PE ratio to its historical norms; Ford, for instance, may be
viewed as undervalued because its relative PE ratio of 0.24 today is lower than the
relative PE that it has historically traded at. The other is to compare relative PE ratios
of ﬁrms in different markets; this allows comparisons when PE ratios in different
markets vary signiﬁcantly. For instance, we could have divided the PE ratios for each
telecom ﬁrm in Illustration 18.8 by the PE ratio for the market in which this ﬁrm
trades locally to estimate relative PE ratios and could have compared those ratios.
Other Variants on the PE Ratio
497
Relative PE
Payout ratio
g
g
r
r
g
Payout ratio
g
g
(r
g
r
Payout ratio
g
g
r
r
g
j
j
j
j
n
j
n
j
j
j,n
j
n
j,n
j
j,n
j
n
m
m
m
n
m
n
m
m
=
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
+
×
+
×
+
−
+
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
)(
)
(
)
(
)
(
)
1
1
1
1
1
1
1
1
1
1
1
+
×
+
×
+
−
+
Payout ratio
g
g
(r
g
r
m,n
m
n
m,n
m
m,n
m
n
(
)
(
)
)(
)
1
1
1
--- page 517 ---

ILLUSTRATION 18.12:
Relative PE Ratios—Automobile Stocks in May 2011
In the following table, we list all automobile companies with a market cap greater than $10 billion in
May 2011. Since these ﬁrms are listed on different markets, we divide the PE ratio for each company
by the aggregate PE ratio for the primary market in which each one trades.
Pimary
PE for
Relative
Company
PE
Market
Market
PE
SAIC Motor Corporation
9.69
China
20.66
0.47
Dongfeng Motor Group Co.
9.01
China
20.66
0.44
Renault SA
3.25
France
15.86
0.21
Volkswagen AG
6.71
Germany
16.82
0.40
Daimler AG
10.37
Germany
16.82
0.62
BMW Group
9.29
Germany
16.82
0.55
Porsche Automobile Holding SE
2.81
Germany
16.82
0.17
Audi AG
10.32
Germany
16.82
0.61
Astra International tbk PT
15.63
Indonesia
21.82
0.72
Fiat S.p.A
14.64
Italy
15.02
0.97
Honda Motor Co., Ltd.
10.55
Japan
17.5
0.60
Toyota Motor Corp.
26.10
Japan
17.5
1.49
Nissan Motor Co. Ltd.
10.63
Japan
17.5
0.61
Suzuki Motor Corp.
22.42
Japan
17.5
1.28
Hyundai Motor Co.
8.50
South Korea
16.98
0.50
Kia Motors Corp.
11.64
South Korea
16.98
0.69
General Motors Co.
5.65
U.S.
19.16
0.30
Ford Motor Co.
7.87
U.S.
19.16
0.41
Porsche and Renault remain the cheapest ﬁrms on both a PE ratio and a relative PE basis, and Toyota
and Suzuki are the most expensive ﬁrms, on both a PE and relative PE basis. In fact, the differences in
PE ratios across markets are small enough that the rankings on a relative PE basis are very close to
those on a PE basis. That would not have been true a decade ago, when Japanese stocks traded at
much higher PE ratios than ﬁrms in other markets.
The average relative PE for Ford (to the U.S. market) has been 0.50 over the past four decades.
At its current relative PE of 0.41, Ford looks cheap. GM also looks cheap, making the same type of
comparison, but GM in 2011, after its near-death experience, is a very different company from the one
that existed in previous decades.
Price to Future Earnings
The price-earnings ratio cannot be estimated for ﬁrms with negative earnings per
share. While there are other multiples, such as the price-to-sales ratio, that can still be
estimated for these ﬁrms, there are analysts who prefer the familiar ground of PE ratios. One way in which the price-earnings ratio can be modiﬁed for use in these ﬁrms
is to use expected earnings per share in a future year in computing the PE ratio. For instance, assume that a ﬁrm has negative earnings per share currently of –$2.00 but is
expected to report earnings per share in ﬁve years of $1.50 per share. You could divide
the price today by the expected earnings per share in ﬁve years to obtain a PE ratio.
How would such a PE ratio be used? The PE ratio for all of the comparable
ﬁrms would also have to be estimated using expected earnings per share in ﬁve
years, and the resulting values can be compared across ﬁrms. Assuming that all of
the ﬁrms in the sample share the same risk, growth, and payout characteristics after
year 5, ﬁrms with low price-to-future-earnings ratios will be considered undervalued. An alternative approach is to estimate a target price for the negative-earnings
498
EARNINGS MULTIPLES
--- page 518 ---

ﬁrm in ﬁve years, dividing that price by earnings in that year and comparing this PE
ratio to the PE ratio of comparable ﬁrms today.
While this modiﬁed version of the PE ratio increases the reach of PE ratios to
cover many ﬁrms that have negative earnings today, it is difﬁcult to control for differences between the ﬁrm being valued and the comparable ﬁrms, since you are
comparing ﬁrms at different points in time.
Price to Earnings before R&D Expenses
In the discussion of cash ﬂows and capital expenditures in Chapter 4, it was argued
that research and development expenses should be capitalized, since they represent investments for the future. Since accounting standards require that R&D be expensed,
rather than capitalized, the earnings of high-growth ﬁrms with substantial research expenses are likely to be understated, and the PE ratio is, therefore, likely to be overstated. This will especially be true if you are comparing technology ﬁrms, which have
substantial research expenditures, to nontechnology ﬁrms, which usually do not. Even
when comparing only across technology stocks, ﬁrms that are growing faster with
larger R&D expenses will end up with lower earnings and higher PE ratios than more
stable ﬁrms in the sector with lower R&D expenses. There are some analysts who argue that the PE ratio should be estimated using earnings prior to R&D expenses:
PEpre-R&D = Market value of equity/(Net income + R&D expenses)
The PE ratios that emerge from this calculation are likely to be much lower than
the PE ratios using conventional deﬁnitions of earnings per share.
While the underlying logic behind this approach is sound, adding back R&D
to earnings represents only a partial adjustment. To complete the adjustment, you
would need to capitalize R&D expenses and compute the amortization of R&D expenses, as was done in Chapter 9. The adjusted PE would then be:
PER&D adjusted = Market value of equity/(Net income + R&D expenses
−Amortization of R&D)
These adjusted PE ratios can then be computed across ﬁrms in the sample.
This adjustment to the PE ratio, while taking care of one problem—the expensing of R&D—will still leave you exposed to all of the other problems associated
Other Variants on the PE Ratio
499
RELATIVE PE RATIOS AND MARKET GROWTH
As the expected growth rate on the market increases, the divergence in PE ratios increases, resulting in a bigger range for relative PE ratios. This can be illustrated very simply, if you consider the relative PE for a company that grows
at half the rate of the market. When the market growth rate is 4 percent, this
ﬁrm will trade at a PE that is roughly 80 percent of the market PE. When the
market growth rate increases to 10 percent, the ﬁrm will trade at a PE that is
60 percent of the market PE.
This has consequences for analysts who use relative PE ratios. Stocks of
ﬁrms whose earnings grow at a rate much lower than the market growth rate
will often look cheap on a relative PE basis when the market growth rate is
high and expensive when the market growth rate is low.
--- page 519 ---

with PE ratios. Earnings will continue to be volatile and affected by accounting
choices, and differences in growth, risk, and cash ﬂow characteristics will still cause
price-earnings ratios to be different across ﬁrms. In addition, you will also have to
estimate expected growth in earnings (pre-R&D) on your own, since consensus estimates from analysts will not be available for growth in this variable.
ILLUSTRATION 18.13:
Forward PE Ratios—Amylin Pharmaceuticals in May 2011
In May 2011, there were dozens of biotechnology ﬁrms that were traded on the U.S. exchanges, but
many of these ﬁrms were reporting losses, either because they had no commercial products yet or
because the earnings were being outstripped by signiﬁcant R&D expenses. We consider one such
company: Amylin Pharmaceuticals, which was trading at $13.28 in May 2011. In the trailing 12
months leading into the valuation, the company reported a loss of  –$1.05 and analysts were projecting losses of roughly 90 cents a share for both 2011 and 2012.
While conventional PE ratios cannot be estimated with negative earnings, there are two ways in
which we can still employ PE ratios to analyze Amylin:
1. Forward PE: Analysts expect the ﬁrm’s products to start generating signiﬁcant proﬁts in 2013
and the ﬁrm to generate earnings per share of $1.25 in 2016. Dividing the price today by the expected earnings per share in 2016 yields a value of 10.62:
Forward PE = Price today/EPS in 2016 = $13.28/ $1.25 = 10.62
Note that this PE ratio cannot be compared to the current PE ratios of other traded companies
today. For instance, arguing that Amylin is cheap because the forward PE of 10.62 is less than
Amgen’s current PE of 12.42 does not stand up to scrutiny because Amgen’s earnings are in
2010 and not in 2016. Consequently, to use the forward PE, you would have to obtain forecasted
EPS in 2016 for each ﬁrm in the sector and compute the forward PE for each one. (Amgen’s PE
based on forecasted EPS in 2016 is 7.45, for instance.)
2. P/E before R&D: A signiﬁcant reason for Amylin’s losses is the substantial R&D expense incurred by the ﬁrm. If you add back the R&D to the reported net loss and compute the per share
value, you get earnings per share before R&D of about $0.15. The price-earnings ratio can be
computed using this estimated earnings per share:
Price/EPS before R&D = $13.28/$0.15 = 88.53
Here again, you have to be consistent and compute PE ratios based on earnings per share before
R&D expenses for all of the ﬁrms in the sector.
ENTERPRISE VALUE TO EBITDA MULTIPLE
Unlike the earnings multiples discussed so far in this chapter, the enterprise value to
EBITDA multiple is a ﬁrm value multiple. In the past two decades, this multiple has
acquired a number of adherents among analysts for several reasons. First, there are
far fewer ﬁrms with negative EBITDA than there are ﬁrms with negative earnings
per share, and thus fewer ﬁrms are lost from the analysis. Second, differences in depreciation methods across different companies—some might use straight-line while
others use accelerated depreciation—can cause differences in operating income or
net income but will not affect EBITDA. Third, this multiple can be compared far
more easily than other earnings multiples across ﬁrms with different ﬁnancial leverage (the numerator is ﬁrm value and the denominator is a predebt earnings). For all
of these reasons, this multiple is particularly useful for ﬁrms in sectors that require
large investments in infrastructure with long gestation periods. Telecom companies
or companies involved in airport or toll road construction would be good examples.
500
EARNINGS MULTIPLES
--- page 520 ---

Definition
The enterprise value to EBITDA multiple relates the total market value of the ﬁrm, net
of cash, to the earnings before interest, taxes, depreciation, and amortization of the ﬁrm:
EV/EBITDA = (Market value of equity −Market value of debt −Cash)/EBITDA
Why is cash netted out of ﬁrm value for this calculation? Since the interest income
from the cash is not counted as part of the EBITDA, not netting out the cash will
result in an overstatement of the EV-to-EBITDA multiple.
The enterprise value to EBITDA multiple can be difﬁcult to estimate for ﬁrms
with cross holdings. To see why, note that cross holdings can be categorized as either majority active, minority active, or minority passive holdings. When a holding
is categorized as a minority holding, the operating income of a ﬁrm does not reﬂect
the income from the holding. The numerator, on the other hand, includes the market value of equity, which should incorporate the value of the minority holdings.
Consequently, the value to EBITDA multiple will be too high for these ﬁrms, leading a casual observer to conclude that they were overvalued. When a holding is categorized as a majority holding, a different problem arises. The EBITDA includes
100 percent of the EBITDA of the holding, but the numerator reﬂects only the portion of the holding that belongs to the ﬁrm. Thus the value to EBITDA multiple will
be too low, leading it to be categorized as an undervalued stock.
The correction for cross holdings is tedious and difﬁcult to do when the holdings are in private ﬁrms. With minority holdings, you can either subtract the estimated value of the holdings from the numerator or add the portion of the EBITDA
of the subsidiary to the denominator. With consolidated holdings, you can subtract
the proportional share of the value of the holding from the numerator and the entire EBITDA of the holding from the denominator.
ILLUSTRATION 18.14:
Estimating Value to EBITDA with Cross Holdings
In Illustration 16.6, we estimated a discounted cash ﬂow value for Segovia, a ﬁrm with two holdings—a 51% stake in Seville Televison and a 15% stake of LatinWorks, a record and CD company.
The ﬁrst holding was categorized as a majority active holding (resulting in consolidation) and the second as a minority passive holding. Here, we will try to estimate an enterprise value to EBITDA multiple
for Seville, using the following information:
■The market value of equity at Segovia is $1,529 million and the consolidated debt outstanding at
the ﬁrm is $500 million. The ﬁrm reported $500 million in EBITDA on its consolidated income
statement. A portion of the EBITDA ($180 million) and debt outstanding ($150 million) represent
Segovia’s holdings in Seville Televison.
■Seville Television is a publicly traded ﬁrm with a market value of equity of $459 million.
■LatinWorks is a private ﬁrm with an EBITDA of $120 million on capital invested of $250 million in
the current year; the ﬁrm has $100 million in debt outstanding.
■None of the ﬁrms have signiﬁcant cash balances.
If we estimate an enterprise value to EBITDA multiple for Segovia using its consolidated ﬁnancial
statements, we would obtain the following:
EV/EBITDA = (Market value of equity + Value of debt −Cash)/EBITDA
= (1,529 + 500 −0)/500 = 4.06
This multiple is contaminated by the cross holdings. There are three ways you can correct for these holdings. One is to net out from the market value of equity of Segovia the value of the equity in the holdings
and the debt of the consolidated holding from Segovia’s debt, and then divide by the EBITDA of just the
Enterprise Value to EBITDA Multiple
501
--- page 521 ---

parent company. To do this, you would ﬁrst need to estimate the market value of equity in LatinWorks,
which is a private company. We will use the estimate of equity value that we obtained in Illustration 16.6:
Value of equity in LatinWorks = 370.25 million
This will yield a EV/EBITDA for just the parent company. The alternative is to adjust just the denominator
to make it consistent with the numerator. In other words, the EBITDA should include only 51% of the
majority active holding’s EBITDA and should add in the 15% of the EBITDA in the minority holdings:
In the third approach, you estimate the EV-to-EBITDA multiple for the consolidated ﬁrm, correcting
for just the minority holding. To accomplish this, you need to add the estimated value of the equity in
the subsidiary that  you have consolidated (since the market value of equity of the parent company re-
ﬂects only the 51% of the subsidiary that you own) to the numerator and subtract the estimated value
of equity in the minority holding in Latin Works from that value. The denominator can be left untouched since it already includes 100% of the EBITDA from the consolidated subsidiary; the same
argument applies to the cash and debt items in Segovia:
Note that 49% of the market value of equity in Seville is added back to the numerator, to stay consistent
with equity value being measured in market terms. In practice, though, many analysts would have used the
minority interests on Segovia’s balance sheet, which is the book value measure of the 49% of Seville, to get
to enterprise value. While this may be convenient, it does introduce an inconsistency into the estimate.
Since the approaches yield very different values, you may wonder which one is correct. Since the
only reason we compute the multiple is to compare it to values computed for similar companies, the
answer depends on that comparison. If each of the three companies is in a different sector, it is best
to use the ﬁrst approach and get EV/EBITDA multiples for each company separately and compare that
company to other companies in its sector. If you can ﬁnd consolidated companies that look just like
Segovia, in terms of both minority and majority holdings, you can use the second approach. If
Segovia and Seville are both in the same sector, you can use the third approach, since you can compare the consolidated value to the values that other companies in the sector trade at.
Description
Figure 18.13 summarizes the enterprise value to EBITDA multiples for U.S. ﬁrms in
January 2011. As with the price-earnings ratio, you have a heavily skewed distribution. The average EV/EBITDA multiple across U.S. ﬁrms in January 2011 was 54.8,
while the median value is closer to 10. To illustrate that these distributional characteristics are not unique to the United States, we compare the distributions of EV/EBITDA
multiples globally in Figure 18.14. The European, emerging market, and Japanese
ﬁrms all have skewed distributions, with positive outliers pushing the average well
above the median.
Analysis
To analyze the determinants of enterprise value to EBITDA multiples, we will revert back to a free cash ﬂow to the ﬁrm valuation model that we developed in
EV/EBITDAConsolidated =
=
1529 + 0.49 × 459 + 500 − 150
500
4 21
.
EV/EBITDAholdings =
−
×
+
×
=
500
49
180
15
120
4.37
1,529 + 500 − 150
.
.
EV/EBITDAno holdings =
−
×
−
×
+
−
−
=
( ,
.
.
.
)
(
)
.
1529
51
459
15
370 25
500
150
500
180
5 70
502
EARNINGS MULTIPLES
--- page 522 ---

Enterprise Value to EBITDA Multiple
503
FIGURE 18.14
EV/EBITDA Multiples: Global Comparison in January 2011
0.00%
5.00%
10.00%
15.00%
20.00%
25.00%
Up To 2
2–4
4–6
6–8
8–10
10–12
12–16
16–20
20–25
25–30
30–35
35–40
40–45
45–50
50–75
75–100
More
U.S.
Europe
Emerging Markets
Japan
Australia, NZ, and Canada
Developed Europe
Emerging markets
Japan
U.S.
Mean
26.94
37.25
40.59
26.54
54.80
Median
10.17
10.28
10.04
9.93
10.04
25th
6.07
6.08
6.12
6.02
6.22
75th
18.45
19.26
18.54
19.04
19.29
FIGURE 18.13
EV/EBITDA Multiples: U.S. Companies in January 2011
0
100
200
300
400
500
600
700
800
900
1,000
Up To 2
2–4
4–6
6–8
8–10
10–12
12–16
16–20
20–25
25–30
30–35
35–40
40–45
45–50
50–75
75–100
More
EV/EBIT
EV/EBITDA
--- page 523 ---

Chapter 15. Speciﬁcally, we estimated the value of the operating assets (or enterprise value) of a ﬁrm to be:
We can write the free cash ﬂow to the ﬁrm in terms of the EBITDA:
FCFF = EBIT(1 −t) −(Cap ex −DA + Δ Working capital)
= (EBITDA −DA)(1 −t) −(Cap ex −DA + Δ Working capital)
= EBITDA(1 −t) −DA(1 −t) −Reinvestment
Substituting back into the equation, we get:
Dividing both sides by the EBITDA and removing the subscripts yields the following:
The ﬁve determinants of the enterprise value to EBITDA multiple are visible in this
equation:
1. Tax rate. Other things remaining equal, ﬁrms with lower tax rates should command higher enterprise value to EBITDA multiples than otherwise similar ﬁrms
with higher tax rates.
2. Depreciation and amortization. Other things remaining equal, ﬁrms that derive
a greater portion of their EBITDA from depreciation and amortization should
trade at lower multiples of EBITDA than otherwise similar ﬁrms.
3. Reinvestment requirements. Other things remaining equal, the greater the portion of the EBITDA that needs to be reinvested to generate expected growth,
the lower the value to EBITDA will be for ﬁrms.
4. Cost of capital. Other things remaining equal, ﬁrms with lower costs of capital
should trade at much higher multiples of EBITDA.
5. Expected growth. Other things remaining equal, ﬁrms with higher expected
growth should trade at much higher multiples of EBITDA.
This can be generalized to consider ﬁrms in high growth. The variables will remain
unchanged but will need to be estimated for each phase of growth.
ILLUSTRATION 18.15:
Analyzing Value to EBITDA Multiples
Castillo Cable is a cable and wireless ﬁrm with the following characteristics:
■The ﬁrm has a cost of capital of 10% and faces a tax rate of 36% on its operating income.
■The ﬁrm has capital expenditures that amount to 45% of EBITDA and depreciation that amounts
to 20% of EBITDA. There are no working capital requirements.
■The ﬁrm is in stable growth and its operating income is expected to grow 5% a year in perpetuity.
EV
EBITDA
t
DA
EBITDA
t
Reinvestment
EBITDA
WACC
g
=
−
−
−
−
−
(
)
(
)
1
1
EV
EBITDA
t
DA
t
Reinvestment
WACC
g
1
1
1
=
−
−
−
−
−
(
)
(
)
1
1
EV
FCFF
WACC
g
1
=
−
504
EARNINGS MULTIPLES
--- page 524 ---

Enterprise Value to EBITDA Multiple
505
FIGURE 18.15
EV/EBITDA Multiples and Tax Rates
FIGURE 18.16
EV/EBITDA and Net Capital Expenditure Ratios
--- page 525 ---

To estimate the enterprise value to EBITDA, we ﬁrst estimate the reinvestment needs as a percent of
EBITDA:
Reinvestment/EBITDA = Cap ex/EBITDA −Depreciation/EBITDA + Δ Working capital/EBITDA
= .45 −.20 −0 = .25
This multiple is sensitive to the tax rate, as evidenced in Figure 18.15. It is also sensitive to the reinvestment rate (stated as a percent of EBITDA), as shown in Figure 18.16. However, changing the reinvestment rate while keeping the growth rate ﬁxed is the equivalent of changing the return on capital. In
fact, at the existing reinvestment rate and growth rate, we are assuming a return on capital of 10.24%:
g = ROC × Reinvestment rate
.05 = ROC × Net cap ex/EBIT(1 −t)
= ROC × (.45 −.20)/[(1 −.2)(1 −.36)]
Solving for the return on capital yields 10.24%. Figure 18.17 looks at the enterprise value to EBITDA
multiple as a function of the return on capital.
In short, ﬁrms with low returns on capital and high reinvestment rates should trade at low multiples of EBITDA.
Application
Having established the fundamentals that determine the enterprise value to EBITDA
multiple, we can now examine how best to apply the multiple. The multiple is most
widely used in capital-intensive ﬁrms with heavy infrastructure investments. The
EV
EBITDA =
−
−
−
−
−
=
(
.
)
( . )(
.
)
.
.
.
.
1
36
0 2 1
36
0 25
10
05
5 24
506
EARNINGS MULTIPLES
FIGURE 18.17
EV/EBITDA and Net Cap Ex Ratios
ﬁrmmult.xls: This spreadsheet allows you to estimate ﬁrm value multiples for a
stable-growth or high-growth ﬁrm, given its fundamentals.
--- page 526 ---

rationale that is given for using the multiple—that EBITDA is the operating cash
ﬂow of the ﬁrm—does not really hold up, because many of these ﬁrms also tend to
have capital expenditure needs that drain cash ﬂows. There are, however, good reasons for using this multiple when depreciation methods vary widely across ﬁrms and
the bulk of the investment in infrastructure has already been made.
ILLUSTRATION 18.16:
Comparing the EV-to-EBITDA Multiples: Steel Companies in 2001
The following table summarizes the enterprise value to EBITDA multiples for steel companies in the
United States in March 2001:
Company Name
EV/EBITDA Tax Rate
ROC
Net Cap Ex/EBITDA DA/EBITDA
Ampco-Pittsburgh
2.74
26.21%
12.15%
15.72%
20.05%
Bayou Steel
5.21
0.00%
5.95%
12.90%
41.01%
Birmingham Steel
5.60
0.00%
6.89%
−28.64%
51.92%
Carpenter Technology
5.05
33.29%
9.16%
15.51%
28.87%
Castle (A.M.) & Co.
9.26
0.00%
8.92%
9.44%
27.22%
Cleveland-Cliffs
5.14
0.00%
7.65%
51.84%
26.33%
Commercial Metals
2.40
36.86%
16.60%
1.19%
26.44%
Harris Steel
4.26
37.18%
15.00%
3.23%
4.92%
Huntco Inc.
5.40
0.00%
4.82%
−48.84%
53.02%
IPSCO Inc.
5.06
23.87%
9.22%
50.57%
16.88%
Kentucky Elec. Steel Inc.
1.72
37.26%
6.75%
−25.51%
38.78%
National Steel
2.30
0.00%
8.46%
68.49%
53.84%
NN Inc.
6.00
34.35%
15.73%
−15.04%
24.80%
Northwest Pipe Co.
5.14
39.47%
9.05%
8.73%
17.22%
Nucor Corp.
3.88
35.00%
18.48%
15.66%
26.04%
Olympic Steel Inc.
4.46
37.93%
5.80%
−3.75%
26.62%
Oregon Steel Mills
5.32
0.00%
7.23%
−31.77%
49.57%
Quanex Corp.
2.90
34.39%
16.38%
−3.45%
29.50%
Ryerson Tull
7.73
0.00%
5.10%
3.50%
38.36%
Samuel Manu-Tech Inc.
3.13
31.88%
14.90%
−2.91%
21.27%
Schnitzer Steel Inds. “A”
4.60
8.70%
7.78%
−16.21%
38.74%
Slater STL Inc.
4.48
26.00%
11.25%
0.80%
27.96%
Steel Dynamics
5.83
36.33%
10.09%
33.13%
23.14%
Steel Technologies
3.75
36.87%
9.22%
11.95%
27.69%
Steel-General
4.14
38.37%
9.80%
21.69%
28.75%
Unvl. Stainless & Alloy Prods.
4.28
37.52%
14.51%
12.73%
15.15%
Worthington Inds.
4.80
37.50%
12.54%
0.16%
22.79%
The enterprise value to EBITDA multiples vary widely across these ﬁrms, and many of these ﬁrms have
negative net capital expenditures (depreciation > Cap Ex), partly reﬂecting the industry’s maturity and
partly the lumpy nature of reinvestments. Many of them also pay no taxes because they lose money.
We regressed the EV/EBITDA multiple against the tax rate and depreciation as a percent of EBITDA:
We did not use expected growth or cost of capital as independent variables because they are very
similar across these ﬁrms. Using this regression, the predicted value to EBITDA multiple for Birmingham Steel would be:
Predicted EV/EBITDA Birmingham Steel = 8.65 −7.20(0.00) −8.08(.5192) = 4.45
At 5.60 times EBITDA, the ﬁrm is overvalued.
EV/EBITDA
 Tax rate
DA
EBITDA
R
=
−
−
⎛
⎝⎜
⎞
⎠⎟
=
8 65
7 20
8 0
3
8
0
2
.
.
%
.
Enterprise Value to EBITDA Multiple
507
--- page 527 ---

CONCLUSION
The price-earnings ratio and other earnings multiples, which are widely used in valuation, have the potential to be misused. These multiples are ultimately determined by
the same fundamentals that determine the value of a ﬁrm in a discounted cash ﬂow
model—expected growth, risk, and cash ﬂow potential. Firms with higher growth,
lower risk, and higher payout ratios, other things remaining equal, should trade at
much higher multiples of earnings than other ﬁrms. To the extent that there are differences in fundamentals across countries, across time, and across companies, the multiples will also be different. A failure to control for these differences in fundamentals
can lead to erroneous conclusions based purely on a direct comparison of multiples.
There are several ways in which earnings multiples can be used in valuation. One
way is to compare earnings multiples across a narrowly deﬁned group of comparable
ﬁrms and to control for differences in growth, risk, and cash ﬂows subjectively. Another
is to expand the deﬁnition of a comparable ﬁrm to the entire sector (such as technology)
or the market, and to control for differences in fundamentals using statistical techniques.
In the last part of the chapter, we turned our attention from equity multiples to
multiples of operating earnings and cash ﬂows. As with the PE ratio, these multiples are a function of growth (in operating income), reinvestment, and risk.
QUESTIONS AND SHORT PROBLEMS
In the problems following, use an equity risk premium of 5.5 percent if none is speciﬁed.
1. National City Corporation, a bank holding company, reported earnings per share
of $2.40 in 1993, and paid dividends per share of $1.06. The earnings had grown
508
EARNINGS MULTIPLES
VALUE MULTIPLES: VARIANTS
While enterprise value to EBITDA may be the most widely used value multiple, there are close variants that are sometimes used by analysts—value/EBIT,
value/after-tax EBIT, and value/FCFF. Each of these multiples is determined by
many of the same variables that determine the EV/EBITDA multiple, but the
actual relationship is slightly different. In particular, note that for a stable
growth ﬁrm these multiples can be written as follows:
Value/FCFF = 1/(Cost of capital – Expected growth rate)
Value/EBIT(1 – t) = (1 – RIR)/(Cost of capital – Expected growth rate)
Value/EBIT = (1 – t)(1 – RIR)/(Cost of capital – Expected growth rate)
where RIR is the reinvestment rate and t is the tax rate.
In other words, higher costs of capital and lower expected growth decrease all of these multiples. A higher reinvestment rate lowers the last two
multiples but does not affect the multiple of FCFF (since FCFF is already after
reinvestment). A higher tax rate will affect just the last multiple, since the ﬁrst
two look at earnings after taxes.
vebitda.xls: This dataset on the Web summarizes value-to-earnings multiples and
fundamentals by industry group in the United States for the most recent year.
--- page 528 ---

7.5% a year over the prior ﬁve years, and were expected to grow 6% a year in
the long term (starting in 1994). The stock had a beta of 1.05 and traded for 10
times earnings. The Treasury bond rate was 7%, and the risk premium is 5.5%.
a. Estimate the PE ratio for National City Corporation.
b. What long-term growth rate is implied in the ﬁrm’s current PE ratio?
2. On March 11, 1994, the New York Stock Exchange Composite was trading at
16.9 times earnings, and the average dividend yield across stocks on the exchange
was 2.5%. The Treasury bond rate on that date was 6.95%. The economy was expected to grow 2.5% a year, in real terms, in the long term, and the consensus estimate for inﬂation, in the long term, was 3.5%. (Market risk premium is 5.5%.)
a. Based on these inputs, estimate the appropriate PE ratio for the exchange.
b. What growth rate in dividends/earnings would justify the PE ratio on March
11, 1994?
c. Would it matter whether this higher growth comes from higher inﬂation or
higher real growth? Why?
3. International Flavors and Fragrances, a leading creator and manufacturer of ﬂavors and fragrances, paid out dividends of $0.91 per share on earnings per share
of $1.64 in 1992. The ﬁrm was expected to have a return on equity of 20% between 1993 and 1997, after which the ﬁrm was expected to have stable growth
of 6% a year. (The return on equity was expected to drop to 15% in the stable
growth phase.) The dividend payout ratio was expected to remain at the current
level from 1993 to 1997. The stock had a beta of 1.10, which was not expected
to change. The Treasury bond rate was 7%, and the risk premium is 5.5%.
a. Estimate the PE ratio for International Flavors based on fundamentals.
b. Estimate how much of this PE ratio can be ascribed to the extraordinary
growth in earnings that the ﬁrm expects to have between 1993 and 1997.
4. Cracker Barrel, which operates restaurants and gift shops, reported dramatic
growth in earnings and revenues between 1983 and 1992. During this period,
earnings grew from $0.08 per share in 1983 to $0.78 per share in 1993. The
dividends paid in 1993 amounted to only $0.02 per share. The earnings growth
rate was expected to ease to 15% a year from 1994 to 1998, and to 6% a year
after that. The payout ratio was expected to increase to 10% from 1994 to
1998, and to 50% after that. The beta of the stock was 1.55, but it was expected
to decline to 1.25 for the 1994–1998 time period and to 1.10 after that. (The
Treasury bond rate was 7%, and the risk premium is 5.5%.)
a. Estimate the PE ratio for Cracker Barrel.
b. Estimate how much higher the PE ratio would have been if it had been able
to maintain the growth rate in earnings that it had posted between 1983 and
1993. (Assume that the dividend payout ratios are unaffected.)
c. Now assume that disappointing earnings reports in the near future lower the
expected growth rate between 1994 and 1998 to 10%. Estimate the PE ratio.
(Again, assume that the dividend payout ratio is unaffected.)
5. The S&P 500 was trading at 21.2 times earnings on December 31, 1993. On the
same day, the dividend yield on the index was 2.74%, and the Treasury bond
rate was 6%. The expected growth rate in real GNP was 2.5%.
a. Assuming that the S&P 500 is correctly priced, what is the inﬂation rate implied in the PE ratio? (Assume stable growth and a 5.5% risk premium.)
b. By February 1994, Treasury bond rates had increased to 7%. If payout ratios and
expected growth remain unchanged, what would the effect on the PE ratio be?
Questions and Short Problems
509
--- page 529 ---

c. Does an increase in interest rates always imply lower prices (and PE ratios)?
6. The following were the PE ratios of ﬁrms in the aerospace/defense industry at
the end of December 1993, with additional data on expected growth and risk.
Expected
Company
PE Ratio
Growth
Beta
Payout
Boeing
17.3
3.5%
1.10
28%
General Dynamics
15.5
11.5%
1.25
40%
General Motors—Hughes
16.5
13.0%
0.85
41%
Grumman
11.4
10.5%
0.80
37%
Lockheed Corporation
10.2
9.5%
0.85
37%
Logicon
12.4
14.0%
0.85
11%
Loral Corporation
13.3
16.5%
0.75
23%
Martin Marietta
11.0
8.0%
0.85
22%
McDonnell Douglas
22.6
13.0%
1.15
37%
Northrop
9.5
9.0%
1.05
47%
Raytheon
12.1
9.5%
0.75
28%
Rockwell
13.9
11.5%
1.00
38%
Thiokol
8.7
5.5%
0.95
15%
United Industrial
10.4
4.5%
0.70
50%
a. Estimate the average and median PE ratios. What, if anything, would these
averages tell you?
b. An analyst concludes that Thiokol is undervalued, because its PE ratio is
lower than the industry average. Under what conditions is this statement
true? Would you agree with it here?
c. Using a regression, control for differences across ﬁrms on risk, growth, and
payout. Specify how you would use this regression to spot underand overvalued stocks. What are the limitations of this approach?
7. The following was the result of a regression of PE ratios on growth rates, betas,
and payout ratios for stocks listed on the Value Line Database in April 1993.
PE = 18.69 + 0.0695 Growth – 0.5082 Beta – 0.4262 Payout
R2 = 0.35
Thus a stock with an earnings growth rate of 20%, a beta of 1.15, and a payout
ratio of 40% would have had an expected PE ratio of:
PE = 18.69 + 0.0695 × 20 – 0.5082(1.15) – 0.4262 × 0.40 = 19.33
You are attempting to value a private ﬁrm with the following characteristics:
■The ﬁrm had net proﬁts of $10 million. It did not pay dividends, but had
depreciation allowances of $5 million and capital expenditures of $12 million in the most recent year. Working capital requirements were negligible.
■The earnings had grown 25% over the previous ﬁve years, and are expected to grow at the same rate over the next ﬁve years.
■The average beta of publicly traded ﬁrms, in the same line of business, is
1.15, and the average debt-equity ratio of these ﬁrms is 25%. (The tax rate
is 40%.) The private ﬁrm is an all-equity-ﬁnanced ﬁrm, with no debt.
a. Estimate the appropriate PE ratio for this private ﬁrm using the regression.
b. What would some of your concerns be in using this regression in valuation?
510
EARNINGS MULTIPLES
--- page 530 ---

CHAPTER 19
Book Value Multiples
T
he relationship between price and book value has always attracted the attention
of investors. Stocks selling for well below the book value of equity have generally
been considered undervalued, while those selling for more than book value have
been targeted as overvalued. This chapter begins by examining the price–book value
(PBV) ratio in more detail, the determinants of this ratio, and how best to evaluate
or estimate the ratio.
In the next part of the chapter, we turn our attention to variants of the price-tobook ratio. In particular, we focus on the value-to-book ratio and Tobin’s Q—a ratio of market value of assets to their replacement cost.
PRICE-TO-BOOK EQUITY
The market value of the equity in a ﬁrm reﬂects the market’s expectation of the
ﬁrm’s earning power and cash ﬂows. The book value of equity is the difference between the book value of assets and the book value of liabilities, a number that is
largely determined by accounting conventions. In the United States, the book value
of assets is the original price paid for the assets reduced by any allowable depreciation on the assets. Consequently, the book value of an asset generally decreases as it
ages. The book value of liabilities similarly reﬂects the at-issue values of the liabilities. Since the book value of an asset reﬂects its original cost, it might deviate significantly from market value if the earning power of the asset has increased or declined
signiﬁcantly since its acquisition.
Why Analysts Use Book Value and the Downside
There are several reasons why investors ﬁnd the price–book value ratio useful in investment analysis. The ﬁrst is that the book value provides a relatively stable, intuitive measure of value that can be compared to the market price. For investors who
instinctively mistrust discounted cash ﬂow estimates of value, the book value is a
much simpler benchmark for comparison. The second is that, given reasonably consistent accounting standards across ﬁrms, price–book value ratios can be compared
across similar ﬁrms for signs of underor overvaluation. Finally, even ﬁrms with
negative earnings, which cannot be valued using price-earnings ratios, can be evaluated using price–book value ratios; there are far fewer ﬁrms with negative book
value for equity than there are ﬁrms with negative earnings.
There are several disadvantages associated with measuring and using
price–book value ratios. First, book values, like earnings, are affected by accounting
511
--- page 531 ---

decisions on depreciation and other variables. When accounting standards vary
widely across ﬁrms, the price–book value ratios may not be comparable. A similar
statement can be made about comparing price–book value ratios across countries
with different accounting standards. Second, book value may not carry much
meaning for service and technology ﬁrms that do not have signiﬁcant tangible assets. Third, the book value of equity can become negative if a ﬁrm has a sustained
string of negative earnings reports, leading to a negative price–book value ratio.
Definition
The price-to-book ratio is computed by dividing the market price per share by the
current book value of equity per share.
While the multiple is fundamentally consistent—the numerator and denominator
are both equity values—there is a potential for inconsistency if you are not careful
about how you compute book value of equity per share. In particular,
■If there are multiple classes of shares outstanding, the price per share can be
different for different classes of shares, and it is not clear how the book equity
should be apportioned among shares.
■You should not include the portion of the equity that is attributable to preferred stock in computing the book value of equity, since the market value of
equity refers only to common equity.
Some of the problems can be alleviated by computing the price-to-book ratio using the total market value of equity and book value of equity, rather than pershare values.
The safest way to measure this ratio when there are multiple classes of equity is to
use the composite market value of all classes of common stock in the numerator
and the composite book value of equity in the denominator—you would still ignore
preferred stock for this computation.
There are two other measurement issues that you have to confront in computing this multiple. The ﬁrst relates to the book value of equity, which as an accounting measure gets updated infrequently—once every quarter for U.S. companies and
once every year for European companies. While most analysts use the most current
book value of equity, there are some who use the average over the previous year or
the book value of equity at the end of the latest ﬁnancial year. Consistency demands
that you use the same measure of book equity for all ﬁrms in your sample. The second and more difﬁcult problem concerns the value of options outstanding. Technically, you would need to compute the estimated market value of management
Price-to-book ratio
PBV
Market value of equity
Book value of equity
=
=
Price-to-book ratio
PBV
Price per share
Book value of equity per share
=
=
512
BOOK VALUE MULTIPLES
--- page 532 ---

options and conversion options (in bonds and preferred stock) and add them to the
market value of equity before computing the price to book value ratio.1 If you have
a small sample of comparable ﬁrms and options represent a large and variable portion of equity value, you should do this. With larger samples and less signiﬁcant option issues, you can stay with the conventional measure of market value of equity.
Accounting standards can affect book values of equity and price-to-book ratios
and skew comparisons made across ﬁrms. For instance, assume that you are comparing the price-to-book ratios of technology ﬁrms in two markets, and that one of
them allows research expenses to be capitalized and the other does not. You should
expect to see lower price-to-book value ratios in the former, since the book value of
equity will be augmented by the value of the research asset.
Price-to-Book Equity
513
1If you do not do this and compare price-to-book ratios across ﬁrms with widely different
amounts of options outstanding, you could misidentify ﬁrms with more options outstanding
as undervalued—the market value of traded common stock at these ﬁrms will be lower because of the option overhang.
ADJUSTING BOOK EQUITY FOR BUYBACKS AND ACQUISITIONS
In recent years, ﬁrms in the United States have increasingly turned to buying
back stock as a way of returning cash to stockholders. When a ﬁrm buys back
stock, the book equity of the ﬁrm declines by the amount of the buyback. Although this is precisely what happens when ﬁrms pay a cash dividend as well,
buybacks tend to be much larger than regular dividends and thus have a bigger impact on book equity. To illustrate, assume that you have a ﬁrm that has
a market value of equity of $100 million and a book value of equity of $50
million; its price-to-book ratio is 2.00. If the ﬁrm borrows $25 million and
buys back stock, its book equity will decline to $25 million and its market equity will drop to $75 million. The resulting price-to-book ratio is 3.
With acquisitions, the effect on price-to-book ratios can vary dramatically
depending on how the acquisition is accounted for. While all ﬁrms are now required to show goodwill as an asset, when they do acquisition, there is some
discretion in how the purchase price on an acquisition is allocated across the
target ﬁrm’s assets. Furthermore, the goodwill line item has to be revisited in
subsequent years and impaired, if the value of the target company has declined since the acquisition. Both actions can affect book value of equity and
the price-to-book ratio.
To compare price-to-book ratios across ﬁrms when some ﬁrms in the sample buy back stocks and some do not or when there are wide differences in
both the magnitude and the accounting for acquisitions can be problematic.
One way to adjust for the differences is to take out the goodwill from acquisitions and to add back the market value of buybacks to the book equity to
come up with an adjusted book value of equity. The price-to-book ratios can
then be computed based on this adjusted book value of equity.
--- page 533 ---

Description
To get a sense of what comprises a high, low, or average price to book value ratio, we
computed the ratio for every ﬁrm listed in the United States, and Figure 19.1 summarizes the distribution of price-to-book ratios in January 2011. Note that this distribution is heavily skewed, as is evidenced by the fact that the average price-to-book ratio
of ﬁrms is 4.59 while the median price-to-book ratio is much lower at 1.79.
Another point worth making about price-to-book ratios is that there are ﬁrms
with negative book values of equity—the result of continuously losing money—for
which price-to-book ratios cannot be computed. In this sample of 5,928 ﬁrms,
there were 843 ﬁrms where this occurred. In contrast, though, 2,512 ﬁrms had negative earnings and PE ratios could not be computed for them.
Analysis
The price–book value ratio can be related to the same fundamentals that determine
value in discounted cash ﬂow models. Since this is an equity multiple, we will use
an equity discounted cash ﬂow model—the dividend discount model—to explore
the determinants. The value of equity in a stable growth dividend discount model
can be written as:
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
514
BOOK VALUE MULTIPLES
FIGURE 19.1
Price to Book Value—U.S. Companies in January 2011
0
50
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
100
150
200
250
Count
300
350
400
450
pbvdata.xls: This dataset on the Web summarizes price-to-book ratios and
fundamentals by industry group in the United States for the most recent year.
