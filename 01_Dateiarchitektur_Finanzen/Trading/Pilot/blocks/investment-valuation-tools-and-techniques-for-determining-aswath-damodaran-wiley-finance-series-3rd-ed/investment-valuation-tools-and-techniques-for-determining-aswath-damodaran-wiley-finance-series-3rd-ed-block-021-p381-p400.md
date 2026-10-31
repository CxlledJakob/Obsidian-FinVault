# INVESTMENT VALUATION TOOLS AND TECHNIQUES FOR DETERMINING -- Aswath Damodaran -- Wiley finance series, 3rd ed_, Hoboken, N_J, New Jersey, -- John -- isbn13 9781118011522 -- f84d1622bdc2de526da0dda803c52830 -- Anna’s.pdf — pages 381–400

--- page 381 ---

Two-Stage FCFE Model
The two-stage FCFE model is designed to value a ﬁrm that is expected to grow
much faster than a stable ﬁrm in the initial period and at a stable rate after that.
The Model
The value of any stock is the present value of the FCFE per year for the
extraordinary growth period plus the present value of the terminal price at the end
of the period.
Value = PV of FCFE + PV of terminal price
=
where FCFEt = Free cash ﬂow to equity in year t
Pn = Price at the end of the extraordinary growth period
ke = Cost of equity in high growth (hg) and stable growth (st) periods
The terminal price is generally calculated using the inﬁnite growth rate model:
Pn = FCFEn+1/(ke,st −gn)
where gn = Growth rate after the terminal year forever
Calculating the Terminal Price
The same caveats that apply to the growth rate
for the stable growth rate model, described in the previous section, apply here as
well. In addition, the assumptions made to derive the free cash ﬂow to equity after the terminal year have to be consistent with this assumption of stability. For
instance, while capital spending may be much greater than depreciation in the
initial high-growth phase, the difference should narrow as the ﬁrm enters its
stable growth phase. We can use the two approaches described for the stable
growth model—industry average capital expenditure requirements or the fundamental growth equation (equity reinvestment rate = g/ROE)—to make this
estimate.
The beta and debt ratio may also need to be adjusted in stable growth to reﬂect
the fact that stable growth ﬁrms tend to have average risk (betas closer to 1) and
use more debt than high-growth ﬁrms.
ILLUSTRATION 14.3:
Capital Expenditure, Depreciation, and Growth Rates
Assume you have a ﬁrm that is expected to have earnings growth of 20% for the next ﬁve years and
5% thereafter. The current earnings per share is $2.50. Current capital spending is $2.00, and current
depreciation is $1.00. If we assume that capital spending and depreciation grow at the same rate as
earnings and there are no working capital requirements or debt:
Earnings in year 5 = 2.50 × (1.20)5
$6.22
Capital spending in year 5 = 2.00 × (1.20)5
$4.98
Depreciation in year 5 = 1.00 × (1.20)5
$2.49
Free cash ﬂow to equity in year 5 = $6.22 + $2.49 −$4.98
$3.73
If we use the perpetual growth rate model, but fail to adjust the imbalance between capital expenditures and depreciation, the free cash ﬂow to equity in the terminal year is:
Free cash ﬂow to equity in year 6 = 3.73 × 1.05 = $3.92
362
FREE CASH FLOW TO EQUITY DISCOUNT MODELS
FCFEt
t=1
t=n
Pn
+
∑
ke,hg
t
+
(
)
1
ke,hg
n
+
(
)
1
--- page 382 ---

This free cash ﬂow to equity can then be used to compute the value per share at the end of year 5,
but it will understate the true value. There are two ways in which you can adjust for this:
1. Adjust capital expenditures in year 6 to reﬂect industry average capital expenditure needs: Assume, for instance, that capital expenditures are 150% of depreciation for the industry in
which the ﬁrm operates. You could compute the capital expenditures in year 6 as follows (EPS
in year 6 = $6.21 × 1.05 = $6.53):
Depreciation in year 6 = 2.49(1.05) = $2.61
Capital expenditures in year 6 = Depreciation in year 6
× Industry average capital expenditures as % of depreciation
= $2.61 × 1.50 = $3.92
FCFE in year 6 = $6.53 + $2.61 −$3.92 = $5.23
2. Estimate the equity reinvestment rate in year 6, based on expected growth and the ﬁrm’s return
on equity. For instance, if we assume that this ﬁrm’s return on equity will be 15% in stable
growth, the equity reinvestment rate would need to be:
Equity reinvestment rate = g/ROE = 5%/15% = 33.33%
Equity Reinvestment in year 6 = Equity reinvestment rate × Earnings per share
= .3333 × $6.53 = $2.18
FCFE in year 6 = $6.53 −$2.18 = $4.35
Firms Model Works Best For
This model makes the same assumptions about
growth as the two-stage dividend discount model (i.e., that growth will be high and
constant in the initial period and drop abruptly to stable growth after that). It is
different because of its emphasis on FCFE rather than dividends. Consequently, it
provides much better results than the dividend discount model when valuing ﬁrms
which either have dividends which are unsustainable (because they are higher than
FCFE) or which pay less in dividends than they can afford to (i.e., dividends are less
than FCFE).
ILLUSTRATION 14.4:
Two-Stage FCFE Model: Nestlé in 2001
Nestlé has operations all over the world, with 97% of its revenues coming from markets outside
Switzerland, where it is headquartered. The ﬁrm, like many large European corporations, has a weak
corporate governance system, and stockholders have little power over managers.
RATIONALE FOR USING THE MODEL
■Why two-stage? Nestlé has a long and impressive history of growth, and while we believe
that its growth will be moderate, we assume that it will be able to maintain high growth for
10 years.
■Why FCFE? Given its weak corporate governance structure and a history of accumulating
cash, the dividends paid by Nestlé bear little resemblance to what the firm could have
paid out.
FCFE Valuation Models
363
--- page 383 ---

BACKGROUND INFORMATION
Current net income = Sfr 5,763 million
Earnings per share = Sfr 148.33
Current capital spending = Sfr 5,058 million
Capital expenditures/share = Sfr 130.18
Current depreciation = Sfr 3,330 million
Depreciation/share = Sfr 85.71
Current revenues = Sfr 81,422 million
Revenue/share = Sfr 2,095.64
Noncash working capital = Sfr 5,818 million
Working capital/share = Sfr 149.74
Change in working capital = Sfr 368 million
Change in working capital/share = Sfr 9.47
Net debt issues = Sfr 272 million
ESTIMATES
We will begin by estimating the cost of equity for Nestlé during the high growth period in Swiss
francs. We will use the 10-year Swiss government Sfr bond rate of 4% as the risk-free rate. To estimate the risk premium, we used the breakdown of Nestlé’s revenues by region:
Revenues
Region
(in Billions Sfr)
Weight
Risk Premium
North America
20.21
24.82%
4.00%
South America
4.97
6.10%
12.00%
Switzerland
1.27
1.56%
4.00%
Germany/France/United Kingdom
21.25
26.10%
4.00%
Italy/Spain
7.39
9.08%
5.50%
Asia
6.70
8.23%
9.00%
Rest of Western Europe
15.01
18.44%
4.00%
Eastern Europe
4.62
5.67%
8.00%
Total
81.42
100.00%
5.26%
The risk premiums for each region represent an average of the risk premiums of the countries in the
region. Using a bottom-up beta of 0.85 for Nestlé, we estimated a cost of equity of:
Cost of equity = 4% + 0.85(5.26%) = 8.47%
We will assume that this cost of equity will remain unchanged in perpetuity. To estimate the expected
growth rate in free cash ﬂows to equity, we ﬁrst computed the free cash ﬂows to equity in the current year:
FCFE = Net income −(Cap ex −Depreciation) −Change in working capital + Net debt issues
= 5,763 −(5,058 −3,330) −368 + 272 = Sfr 3,939 million
The equity reinvestment rate can be estimated from this value:
Equity reinvestment rate = 1 −FCFE/Net income = 1 −3,939/5,763 = 31.65%
The return on equity in 2000 was estimated using the net income from 2000 and the book value of equity from the end of the previous year:
Return on equity = 5,763/25,078 = 22.98%
The expected growth rate in FCFE is a product of the equity reinvestment rate and the return on equity:
Expected growth in FCFE = Equity reinvestment rate × Return on equity = .3165 × .2298 = 7.27%
We will assume that net capital expenditures and working capital will grow at the same rate as
earnings for the high growth period and that the ﬁrm will raise 33.92% of its reinvestment needs from
debt (which is its current book value debt-to-capital ratio).
364
FREE CASH FLOW TO EQUITY DISCOUNT MODELS
--- page 384 ---

In stable growth, we assume a growth rate of 4%. We also assume that the cost of equity remains unchanged but that the return on equity drops to 15%. The equity reinvestment rate in stable
growth can be estimated as follows:
Equity reinvestment in stable growth = g/ROE = 4%/15% = 26.67%
VALUATION
The ﬁrst component of value is the present value of the expected FCFE during the high-growth period,
(see table) assuming earnings, net capital expenditures, and working capital grow at 7.27% and
33.92% of reinvestment needs come from debt (in Sfr):
Note that the change in working capital each year is computed based on the existing working capital of Sfr 149.74 per share, and that the present value is computed using the cost of equity of
8.47%.
To estimate the terminal value, we ﬁrst estimate the free cash ﬂows to equity in year 11:
Expected earnings per share in year 11 = EPS10(1 + g) = 299.32(1.04) = 311.30
Equity reinvestment in year 11 = EPS11 × Stable equity reinvestment rate = 311.30 × .2667 = 83.02
Expected FCFE in year 11 = EPS11 −Equity reinvestment11 = 311.30 −83.02 = 228.28
Terminal value of equity per share = FCFE11/(Cost of equity11 −g) = 228.28/(.0847 −.04) = 5,105.88
The value per share can be estimated as the sum of the present value of FCFE during the high growth
phase and the present value of the terminal value of equity:
Value per share = PV of dividend during high growth phase + Terminal price/(1 + ke)n
= 1,056.34 + 5,105.88/1.084710 = 3,320.65 Sfr
The stock was trading at 3,390 Sfr per share in May 2001 at the time of this valuation, making the
stock slightly under valued.
FCFE Valuation Models
365
Change in
Net
Working
Equity
Earnings
Cap Ex
Capital
Reinvestment
Reinvestment
FCFE
per
per
per
per
per
per
Present
Year
Share
Share
Share
Share
Share
Share
Value
1
159.12
47.71
10.89
58.60
38.72
120.39
110.99
2
170.69
51.18
11.68
62.86
41.54
129.15
109.76
3
183.10
54.90
12.53
67.44
44.56
138.54
108.55
4
196.42
58.90
13.44
72.34
47.80
148.62
107.35
5
210.71
63.18
14.42
77.60
51.28
159.43
106.17
6
226.03
67.77
15.47
83.25
55.01
171.02
105.00
7
242.47
72.70
16.60
89.30
59.01
183.46
103.84
8
260.11
77.99
17.80
95.80
63.30
196.81
102.69
9
279.03
83.67
19.10
102.76
67.91
211.12
101.56
10
299.32
89.75
20.49
110.24
72.85
226.48
100.44
Sum of present value of FCFE
1,056.34
FCFE2st.xls: This spreadsheet allows you to value a ﬁrm with a temporary period of
high growth in FCFE, followed by stable growth.
--- page 385 ---

E Model—A Three-Stage FCFE Model
The E model is designed to value ﬁrms that are expected to go through three stages
of growth—an initial phase of high growth rates, a transitional period in which the
growth rate declines, and a steady-state period in which growth is stable.
The Model
The E model calculates the present value of expected free cash ﬂow to
equity over all three stages of growth:
where
P0 = Value of the stock today
FCFEt = FCFE in year t
ke = Cost of equity
Pn2 = Terminal price at the end of transitional period = FCFEn2+1/(ke −gn)
n1 = End of initial high growth period
n2 = End of transition period
Caveats in Using Model
Since the model assumes that the growth rate goes through
three distinct phases—high growth, transitional growth, and stable growth—it is
important that assumptions about other variables are consistent with these assumptions about growth.
Capital Spending versus Depreciation
It is reasonable to assume that as the ﬁrm
goes from high growth to stable growth, the relationship between capital spending and depreciation will change. In the high-growth phase, capital spending is
likely to be much larger than depreciation. In the transitional phase, the
P
FCFE
k
FCFE
k
P
k
0
t
e
t
t=1
t=n1
t
e
t
t=n1+1
t=n2
n2
e
n2
=
+
(
)
+
+
(
)
+
+
(
)
∑
∑
1
1
1
366
FREE CASH FLOW TO EQUITY DISCOUNT MODELS
REINVESTMENT ASSUMPTIONS, TERMINAL VALUE, AND EQUITY VALUE
We have repeatedly emphasized the importance of linking growth assumptions to assumptions about reinvestment, and especially so in stable growth.
A very common assumption in many discounted cash ﬂow valuations is that
capital expenditures offset depreciation in stable growth. When combined
with the assumption of no working capital changes, this translates into zero
reinvestment. While this may be a reasonable assumption for a year or two,
it is not consistent with the assumption that operating income will grow in
perpetuity. How much of a difference can one assumption make? In the
Nestlé valuation, we reestimated terminal value of equity per share assuming no reinvestment:
Estimated terminal value of equity per share = 311.30/(.0847 −.04) = 6,962.57
Keeping all of our other assumptions intact, this results in a value of equity per
share of 4,144 Sfr per share—an increase in value of approximately 22 percent.
--- page 386 ---

difference is likely to narrow and the difference between capital spending and depreciation will be lower still in stable growth, reﬂecting the lower expected
growth rate. (See Figure 14.3.)
Risk
As the growth characteristics of a ﬁrm change, so do its risk characteristics.
In the context of the CAPM, as the growth rate declines the beta of the ﬁrm can be
expected to change. The tendency of betas to converge toward one in the long term
has been conﬁrmed by empirical observation of portfolios of ﬁrms with high betas.
Over time, as these ﬁrms get larger and more diversiﬁed, the average betas of these
portfolios move toward 1.
Firms Model Works Best For
Since the model allows for three stages of growth and
for a gradual decline from high to stable growth, it is the appropriate model to use
to value ﬁrms with very high growth rates currently. The assumptions about
FCFE Valuation Models
367
A TROUBLESHOOTING GUIDE: WHAT IS WRONG WITH THIS VALUATION?
(TWO-STAGE FCFE MODEL)
If This Is Your Problem
This May Be the Solution
• If you get a extremely low value
from the two-stage FCFE, the
likely culprits are:
Earnings are depressed due to
Use normalized earnings.
some reason (economy, etc.).
Capital expenditures are
Reduce the difference for stable
signiﬁcantly higher than
growth period. (Compute the
depreciation in stable
appropriate reinvestment rate—
growth phase.
you might need a higher ROE.)
The beta in the stable period
Use a beta closer to 1.
is too high for a stable ﬁrm.
Working capital as percent
Use a working capital ratio closer to
of revenue is too high to
industry.
sustain.
The use of the two-stage
Use a three-stage model.
model when the three-stage
model is more appropriate.
• If you get an extremely high value:
Earnings are inﬂated above
Use normalized earnings.
normal levels.
Capital expenditures offset
Compute the appropriate reinvestment
or lag are lower than
rate = g/ROE.
depreciation during
high growth period.
The growth rate in the stable
Use a growth rate closer to GNP
growth period is too high for
growth (risk free rate).
stable ﬁrm.
--- page 387 ---

growth are similar to the ones made by the three-stage dividend discount model,
but the focus is on FCFE instead of dividends, making it more suited to value ﬁrms
whose dividends are signiﬁcantly higher or lower than the FCFE.
ILLUSTRATION 14.5:
Three-Stage FCFE Model: Tsingtao Breweries (China) in 2001
Tsingtao Breweries produces and distributes beer and other alcoholic beverages in China and around
the world under the Tsingtao brand name. The ﬁrm has 653.15 million shares listed on the Shanghai
and Hong Kong exchanges.
RATIONALE FOR USING THE THREE-STAGE FCFE MODEL
■Why three-stage? Tsingtao is a small ﬁrm serving a huge and growing market—China, in particular, and the rest of Asia in general. The ﬁrm’s current return on equity is low, and we anticipate
that it will improve over the next ﬁve years. As it increases, earnings growth will be pushed up.
368
FREE CASH FLOW TO EQUITY DISCOUNT MODELS
FIGURE 14.3
Three-Stage FCFE Model: Reinvestment Needs
--- page 388 ---

■Why FCFE? Corporate governance in China tends to be weak and dividends are unlikely to reﬂect
free cash ﬂow to equity. In addition, the ﬁrm consistently funds a portion of its reinvestment
needs with new debt issues.
BACKGROUND INFORMATION
In 2000, Tsingtao Breweries earned 72.36 million CY (Chinese yuan) in net income on a book value of
equity of 2,588 million CY, giving it a return on equity of 2.80%. The ﬁrm had capital expenditures of
335 million CY and depreciation of 204 million CY during the year, and noncash working capital
dropped by 1.2 million CY during the year. The total reinvestment in 2000 was therefore:
Total reinvestment = Capital expenditures −Depreciation + Change in noncash working capital
= 335 −204 −1.2 = 129.8 million
The working capital changes over the past four years have been volatile, and we normalize the change
using noncash working capital as a percent of revenues in 2000:
Normalized change in noncash working capital = (Noncash working capital2000 /Revenues2000)
× (Revenues2000 −Revenues1999)
= (180/2,253) × (2,253 −1,598) = 52.3 million CY
The normalized reinvestment in 2000 can then be estimated as follows:
Normalized reinvestment = Capital expenditures −Depreciation
+ Normalized change in noncash working capital
= 335 −204 + 52.3 = 183.3 million CY
As with working capital, debt issues have been volatile. We estimate the ﬁrm’s book debt to capital ratio of 40.94% at the end of 2000 and use it to estimate the normalized equity reinvestment in 2000:
Equity reinvestment in 2000 = Reinvestment(1 −Debt ratio) = 183.3(1 −.4094) = 108.27 million CY
As a percent of net income,
Equity rate in 2000 = 108.27/72.36 = 149.97%
ESTIMATION
To estimate free cash ﬂows to equity for the high-growth period, we make the assumption that the return on equity, which is 2.80% today, will drift up to 12% by the ﬁfth year. In addition, we will assume
that new investments from now on will earn a return on equity of 12%. Finally, we will assume that the
equity reinvestment rate will remain at its current level (149.97%) each year for the next ﬁve years.
The expected growth rate over the next ﬁve years can then be estimated as follows:
Expected growth rate—next ﬁve years = Equity reinvestment rate × ROEnew
+ [(ROEnew −ROEtoday)/ROEtoday]1/5 −1
= 1.4997 × .12 + {[(.12 −.028)/.028]1/5 −1} = 44.91%
After year 5, we will assume that the expected growth rate declines linearly each year from year 6
through 10 to reach a stable growth rate of 10% in year 10. (Note that the growth rate is in nominal
CY; the higher stable growth rate reﬂects the higher expected inﬂation in that currency.) As the growth
rate declines, the equity reinvestment rate also drops off to a stable period equity reinvestment rate of
50%, estimated using the 10% stable growth rate and an assumed return on equity in stable growth
of 20%.
Stable period equity reinvestment rate = g/ROE = 10%/20% = 50%
FCFE Valuation Models
369
--- page 389 ---

To estimate the cost of equity, we used a risk-free rate of 10% (in nominal CY), a risk premium of
6.28% (4% for mature market risk and 2.28% as the country risk premium for China), and a beta of
0.75 (reﬂecting the bottom-up beta for breweries):
Cost of equity = 10% + 0.75(6.28%) = 14.71%
In stable growth, we assume that the beta will drift up to 0.80 and that the country risk premium will
drop to 0.95%:
Cost of equity = 10% + 0.80(4.95%) = 13.96%
The cost of equity adjusts in linear increments from 14.71% in year 5 to 13.96% in year 10.
VALUATION
To value Tsingtao, we will begin by projecting the free cash ﬂows to equity during the high growth and
transition phases, using an expected growth rate of 44.91% in net income and an equity reinvestment
rate of 149.97% for the ﬁrst ﬁve years. The next ﬁve years represent a transition period, where the
growth drops in linear increments from 44.91% to 10% and the equity reinvestment rate drops from
149.97% to 50%. The resulting free cash ﬂows to equity are shown in the following table:
Equity
Expected
Net
Reinvestment
Cost
Year
Growth
Income
Rate
FCFE
of Equity
Present Value
Current
CY      72.36
149.97%
1
44.91%
CY    104.85
149.97%
−CY   52.40
14.71%
−CY   45.68
2
44.91%
CY    151.93
149.97%
−CY   75.92
14.71%
−CY   57.70
3
44.91%
CY    220.16
149.97%
−CY 110.02
14.71%
−CY   72.89
4
44.91%
CY    319.03
149.97%
−CY 159.43
14.71%
−CY   92.08
5
44.91%
CY    462.29
149.97%
−CY 231.02
14.71%
−CY 116.32
6
37.93%
CY    637.61
129.98%
−CY 191.14
14.56%
−CY   84.01
7
30.94%
CY    834.92
109.98%
CY   83.35
14.41%
−CY  32.02)
8
23.96%
CY 1,034.98
89.99%
CY 103.61
14.26%
CY   34.83
9
16.98%
CY 1,210.74
69.99%
CY 363.29
14.11%
CY 107.04
10
10.00%
CY 1,331.81
50.00%
CY 665.91
13.96%
CY 172.16
Sum of the present values of FCFE during high growth = −$186.65
To estimate the terminal value of equity, we use the net income in the year 11, reduce it by the
equity reinvestment needs in that year, and then assume a perpetual growth rate to get to a value.
Expected stable growth rate = 10%
Equity reinvestment rate in stable growth = 50%
Cost of equity in stable growth = 13.96%
Expected FCFE in year 11 = Net income11 × (1 −Stable period equity reinvestment rate)
= CY1,331.81(1.10)(1 −.5) = CY732.50 million
Terminal value of equity in Tsingtao Breweries = FCFE11/(Stable period cost of equity
−Stable growth rate) = 732.5/(.1396 −.10)
= CY18,497 million
To estimate the value of equity today, we sum up the present value of the FCFE over the high
growth period and add to it the present value of the terminal value of equity:
Value of equity = PV of FCFE during the high growth period + PV of terminal value
= −CY186.65 + CY18,497/(1.14715 × 1.1456 × 1.1441 × 1.1426
× 1.1411 × 1.1396) = CY4,596 million
Value of equity per share = Value of equity/Number of shares = CY4,596/653.15 = CY7.04 per share
The stock was trading at 10.10 yuan per share, which would make it overvalued based on this valuation.
370
FREE CASH FLOW TO EQUITY DISCOUNT MODELS
--- page 390 ---

FCFE Valuation Models
371
NEGATIVE FCFE, EQUITY DILUTION, AND VALUE PER SHARE
Unlike dividends, free cash ﬂows to equity can be negative. This can occur either
because net income is negative or because a ﬁrm’s reinvestment needs are signiﬁ-
cant; this is the case with Tsingtao in Illustration 14.5. The resulting net capital
expenditure and working capital needs are much larger than the net income. In
fact, this is likely to occur fairly frequently with high-growth ﬁrms.
The FCFE model is ﬂexible enough to deal with this issue. The free cash
ﬂows to equity will be negative as the ﬁrm reinvests substantial amounts to
generate high growth. As the growth declines, the reinvestment needs also
drop off and free cash ﬂows to equity turn positive.
Intuitively, though, consider what a negative free cash ﬂow to equity implies.
It indicates that the ﬁrm does not generate enough equity cash ﬂows from current
operations to meet its equity reinvestment needs. Since the free cash ﬂow to equity
is after net debt issues, the ﬁrm will have to issue new equity in years when the
cash ﬂow is negative. This expected dilution in future years will reduce the value
of equity per share today. In the FCFE model, the negative free cash ﬂows to equity in the earlier years will reduce the estimated value of equity today. Thus the
dilution effect is captured in the present value, and no additional consideration is
needed of new stock issues in future years and the effect on value per share today.
A TROUBLESHOOTING GUIDE: WHAT IS WRONG WITH THIS VALUATION?
(THREE-STAGE FCFE MODEL)
If This Is Your Problem
This May Be the Solution
• If you get an extremely low value
from the three-stage FCFE, the
likely culprits are:
Capital expenditures are
Reduce net cap ex in stable growth.
signiﬁcantly higher than
Cap ex grows slower than
depreciation in stable
depreciation during transition
growth phase.
period.
The beta in the stable period
Use a beta closer to 1.
is too high for a stable ﬁrm.
Working capital as percent of
Use working capital ratio closer to
revenue is too high to sustain.
industry average.
• If you get an extremely high value:
Capital expenditures offset
Capital expenditures should be set
depreciation during highhigher.
growth period.
Capital expenditures are less
Calculate reinvestment rate
than depreciation.
= g/ROC
Growth period (high growth
Use a shorter growth period.
and transition) is too long.
The growth rate in the
Use a growth rate lower than or
stable growth period is too
equal to GNP growth
high for stable ﬁrm.
(riskfree rate).
--- page 391 ---

FCFE VALUATION VERSUS DIVIDEND DISCOUNT
MODEL VALUATION
The discounted cash ﬂow model that uses FCFE can be viewed as an alternative to
the dividend discount model. Since the two approaches sometimes provide different
estimates of value, it is worth examining when they provide similar estimates of
value, when they provide different estimates of value, and what the difference tells
us about the ﬁrm.
When They Are Similar
There are two conditions under which the value from using the FCFE in discounted
cash ﬂow valuation will be the same as the value obtained from using the dividend
discount model. The ﬁrst is the obvious one, where the dividends are equal to the
FCFE. The second condition is more subtle, where the FCFE is greater than dividends, but the excess cash (FCFE minus dividends) is invested in projects with net
present value of zero. (For instance, investing in ﬁnancial assets that are fairly
priced should yield a net present value of zero.)
When They Are Different
There are several cases where the two models will provide different estimates of
value. First, when the FCFE is greater than the dividend and the excess cash either earns below-market interest rates or is invested in negative net present value
projects, the value from the FCFE model will be greater than the value from the
dividend discount model. There is reason to believe that this is not as unusual as
it would seem at ﬁrst glance. There are numerous case studies of ﬁrms that, having accumulated large cash balances, by paying out low dividends relative to
FCFE, have chosen to use this cash to ﬁnance unwise takeovers (where the price
paid is greater than the value received from the takeover). Second, the payment
of smaller dividends than can be afforded to be paid out by a ﬁrm may lead to a
lower debt ratio and a higher cost of capital, causing a loss in value.
In the cases where dividends are greater than FCFE, the ﬁrm will have to issue
either new stock or new debt to pay these dividends leading to at least three negative consequences for value. One is the issuance cost on these security issues, which
can be substantial for equity issues, creates an unnecessary expenditure that decreases value. Second, if the ﬁrm borrows the money to pay the dividends, the ﬁrm
may become overlevered (relative to the optimal), exposing itself to distress/default
and leading to a loss in value. Finally, paying too much in dividends can lead to
capital rationing constraints where good projects are rejected, resulting in a loss of
value.
372
FREE CASH FLOW TO EQUITY DISCOUNT MODELS
FCFE3st.xls: This spreadsheet allows you to value a ﬁrm with a temporary period of
high growth in FCFE, followed by a transition period, followed by stable growth.
--- page 392 ---

There is a third possibility and it reﬂects different assumptions about reinvestment and growth in the two models. If the same growth rate is used in the
dividend discount and FCFE models, the FCFE model will give a higher value
than the dividend discount model whenever FCFE is higher than dividends and a
lower value when dividends exceed FCFE. In reality, the growth rate in FCFE
should be different from the growth rate in dividends, because the free cash ﬂow
to equity is assumed to be paid out to stockholders. This will affect the reinvestment rate of the ﬁrm. In addition, the return on equity used in the FCFE model
should reﬂect the return on equity on noncash investments, whereas the return on
equity used in the dividend discount model should be the overall return on equity.
Table 14.1 summarizes the differences in assumptions between the two models.
In general, when ﬁrms pay out much less in dividends than they have available
in FCFE, the expected growth rate and terminal value will be higher in the dividend
discount model, but the year-to-year cash ﬂows will be higher in the FCFE model.
The net effect on value will vary from company to company.
What Does It Mean When They Are Different?
When the value using the FCFE model is different from the value using the dividend
discount model, with consistent growth assumptions, there are two questions that
need to be addressed: What does the difference between the two models tell us?
Which of the two models is the appropriate one to use in evaluating the market price?
FCFE Valuation versus Dividend Discount Model Valuation
373
TABLE 14.1
Differences between DDM and FCFE Models
Dividend Discount Model
FCFE Model
Implicit assumption Only dividends are paid.
The FCFE is paid out to
Remaining portions of earnings
stockholders. The remaining
are invested back into the ﬁrm,
earnings are invested only in
some in operating assets and
operating assets.
some in cash and marketable
securities.
Expected growth
Measures growth in income
Measures growth only in
from both operating and cash
income from operating assets.
assets. In terms of fundamentals,
In terms of fundamentals, it is the
it is the product of the retention
product of the equity reinvestment
ratio and the return on equity.
rate and the noncash return on
equity.
Dealing with cash
The income from cash and
You have two choices:
and marketable
marketable securities is built
1. Build income from cash and
securities
into earnings and ultimately
marketable securities into
into dividends. Therefore, cash
projections of income, and
and marketable securities do not
estimate the value of equity.
need to be added in.
2. Ignore income from cash and
marketable securities, and add
their value to equity value in
model.
--- page 393 ---

The less frequent scenario is that the dividend discount model yields a higher
value than the FCFE model, largely because dividends exceed FCFE. In this case, it
is best to go with the FCFE model because the dividends are not sustainable. The
more common occurrence is for the value from the FCFE model to exceed the value
from the dividend discount model. The difference between the value from the FCFE
model and the value using the dividend discount model can be considered one component of the value of controlling a ﬁrm—it measures the value of controlling dividend policy. In a hostile takeover, the bidder can expect to control the ﬁrm and
change the dividend policy (to reﬂect FCFE), thus capturing the higher FCFE value.
As for which of the two values is the more appropriate one for use in evaluating the market price, the answer lies in the openness of the market for corporate
control. If there is a sizable probability that a ﬁrm can be taken over or its management changed, the market price will reﬂect that likelihood, and the appropriate
benchmark to use is the value from the FCFE model. As changes in corporate control become more difﬁcult because of a ﬁrm’s size and/or legal or market restrictions on takeovers, the value from the dividend discount model will provide the
appropriate benchmark for comparison.
ILLUSTRATION 14.6:
Valuing Coca-Cola with a Three-Stage FCFE Model
In Chapter 13, we valued Coca-Cola using a three-stage dividend discount model and estimated a
value of $67.15 per share, a tad under the market price of $68.22. Implicitly, we were assuming that
Coca-Cola’s managers are paying out what they can afford to in dividends and that there will be no
cash buildup in the company. To test the proposition, we will now value Coca-Cola using a three-stage
FCFE model.
We begin by ﬁrst separating the after-tax interest income of $105.32 million earned by Coca-Cola
from its net income of $11,809 million and computing a noncash net income:
Net income from noncash assets = $11,809 −$105 = $11,704
To compute the noncash return on equity, we modify the return on equity computation by netting cash
($7.021 million) out of book value of equity ($25,346 million):
As in the three-stage dividend discount model, we assume a much lower noncash return on equity of
30% going forward (which is higher than the 25% return on equity we assumed in the dividend discount model, because of our exclusion of cash). Rather than use the retention ratio to estimate reinvestment, we computed an equity reinvestment rate (ERR), using the net capital expenditures and
working capital investment made by Coca-Cola in 2010:
Since Coca-Cola has done acquisitions over time, its equity reinvestment rate has been volatile, and
the average over the past ﬁve years has been approximately 25%.
(Capital expenditures −Depreciation + Change in WC −Net debt issued)
ERR =
Noncash net income
2,215 −1,443 + 335 −150
Value
=
11,809 −105
= 8.19%
(11,809 −105)
ValueNoncash ROE in 2010 =
25,346 −7,021
= 63.87%
374
FREE CASH FLOW TO EQUITY DISCOUNT MODELS
--- page 394 ---

Assuming a noncash ROE of 30% and an equity reinvestment rate of 25% for the next ﬁve years
yields an expected growth rate in noncash net income of 7.5%:
Expected growth rate = ROE × Equity reinvestment rate = 30% × 25% = 7.5%
During this high growth period, we will assume that Coca-Cola will have a beta of 0.90 (the same beta
that we used in the dividend discount model). With a risk-free rate of 3.5% and an equity risk premium
of 5.5%, we arrive at the same cost of equity of 8.45% that we used in the dividend discount model:
Cost of equity = 3.5% = 0.90(5.5%) = 8.45%.
Applying the growth to net income and netting out the equity reinvestment rate yields the free cash
ﬂows to equity for the next ﬁve years, with present values computed using the cost of equity:
1
2
3
4
5
Expected growth rate
7.50%
7.50%
7.50%
7.50%
7.50%
Net income
$12,581.46
$13,525.07
$14,539.45
$15,629.91
$16,802.15
Equity reinvestment rate
25.00%
25.00%
25.00%
25.00%
25.00%
FCFE
$9,436.10
$10,143.80
$10,904.59
$11,722.43
$12,601.62
Cost of equity
8.45%
8.45%
8.45%
8.45%
8.45%
Present value
$8,700.87
$8,624.65
$8,549.10
$8,474.22
$8,399.98
As in the dividend discount model, we will assume that the ﬁrm will be in stable growth 10 years forward, with the following assumptions:
■The growth rate in perpetuity after year 10 will be 3% and the noncash ROE is expected to be
15%. The resulting equity reinvestment rate in stable growth is:
Equity reinvestment rate = g/ROE = 3%/15% = 20%
■The beta for the company will rise to 1, causing the cost of equity to increase to 9%.
The transition period from year 6 to 10 is again used to adjust the growth rate, equity reinvestment
rate, and cost of equity from high growth values to stable growth levels. The resulting FCFE are shown
in the following table, with the present value computed using the cumulated cost of equity (since the
cost of equity changes from period to period).
6
7
8
9
10
Expected growth rate
6.60%
5.70%
4.80%
3.90%
3.00%
Net income
$17,911.10
$18,932.03
$19,840.77
$20,614.56
$21,232.99
Equity reinvestment rate
24.00%
23.00%
22.00%
21.00%
20.00%
FCFE
$13,612.43
$14,577.66
$15,475.80
$16,285.50
$16,986.39
Cost of equity
8.56%
8.67%
8.78%
8.89%
9.00%
Cumulative cost of equity
1.6286
1.7698
1.9252
2.0964
2.2850
Present value
$8,358.30
$8,236.84
$8,038.53
$7,768.49
$7,433.79
At the end of year 10, the terminal value of equity is computed using the stable growth inputs:
Expected FCFE in year 11
Value of equity at end of year 10 = Stable cost of equity −Stable growth rate
$21,233(1.03)(.80)
V
=
.09 −.03
= $291,600
FCFE Valuation versus Dividend Discount Model Valuation
375
--- page 395 ---

Discounting the terminal value back at the cumulated cost of equity for year 10 and adding to the
present value of FCFE over the next 10 years yields an overall value for equity from operating assets.
Note, though, that cash has been set apart in this model and needs to be added back at this stage to
get to the value of equity for Coca-Cola.
Value of equity today = PV of FCFE + PV of Terminal value + Cash
= $82,285 + $291,600/2.2850 + $8,517
= $218,715
Dividing by the number of shares outstanding today (2,289.254 million) yields a value per share of  $95.54.
Value per share = $218,715/ 2,289.254 = $95.54
The FCFE model suggests that Coca-Cola is signiﬁcantly undervalued at $68.22 a share.
So, why are they different? The FCFE model does use a lower growth rate than
the dividend discount model, but it allows for more cash to be returned to stockholders. In effect, we are incorporating the fact that Coca-Cola does not pay out its FCFE
as dividends. The net effect, at least in this case, is an increase in value per share. For
companies that pay out more dividends than they have available in FCFE, the value
per share might drop with the FCFE model. In either case, we would argue that the
FCFE estimate of value per share is a more realistic one than the dividend discount
model estimate of value per share.
CONCLUSION
The primary difference between the dividend discount models described in the previous
chapter and the free cash ﬂow to equity models described in this one lies in the deﬁnition of cash ﬂows; the dividend discount model uses a strict deﬁnition of cash ﬂow to
equity (i.e., the expected dividends on the stock), while the FCFE model uses an expansive deﬁnition of cash ﬂow to equity as the residual cash ﬂow after meeting all ﬁnancial
obligations and investment needs. When dividends are different from the FCFE, the values from the two models will be different. In valuing ﬁrms for takeovers or in valuing
ﬁrms where there is a reasonable chance of changing corporate control, the value from
the FCFE model provides the better estimate of value.
QUESTIONS AND SHORT PROBLEMS
In the problems following, use an equity risk premium of 5.5 percent if none is
speciﬁed.
1. Respond true or false to the following statements relating to the calculation and
use of FCFE:
a. The free cash ﬂow to equity will generally be more volatile than dividends.
True ____
False ____
b. The free cash ﬂow to equity will always be higher than dividends.
True ____
False ____
c. The free cash ﬂow to equity will always be higher than net income.
True ____
False ____
d. The free cash ﬂow to equity can never be negative.
True ____
False ____
376
FREE CASH FLOW TO EQUITY DISCOUNT MODELS
--- page 396 ---

2. Kimberly-Clark, a household product manufacturer, reported earnings per
share of $3.20 in 1993 and paid dividends per share of $1.70 in that year. The
ﬁrm reported depreciation of $315 million in 1993 and capital expenditures of
$475 million. (There were 160 million shares outstanding, trading at $51 per
share.) This ratio of capital expenditures to depreciation is expected to be
maintained in the long term. The working capital needs are negligible.
Kimberly-Clark had debt outstanding of $1.6 billion, and intended to maintain
its current ﬁnancing mix (of debt and equity) to ﬁnance future investment
needs. The ﬁrm was in steady state and earnings were expected to grow 7% a
year. The stock had a beta of 1.05. (The Treasury bond rate was 6.25%, and
the risk premium was 5.5%.)
a. Estimate the value per share, using the dividend discount model.
b. Estimate the value per share, using the FCFE model.
c. How would you explain the difference between the two models, and which
one would you use as your benchmark for comparison to the market
price?
3. Ecolab Inc. sells chemicals and systems for cleaning, sanitizing, and maintenance.
It reported earnings per share of $2.35 in 1993, and expected earnings growth of
15.5% a year from 1994 to 1998 and 6% a year after that. The capital expenditure per share was $2.25, and depreciation was $1.125 per share in 1993. Both
were expected to grow at the same rate as earnings from 1994 to 1998. Working
capital was expected to remain at 5% of revenues, and revenues, which were $1
billion in 1993, were expected to increase 6% a year from 1994 to 1998, and 4%
a year after that. The ﬁrm had has a debt ratio [D/(D + E)] of 5%, but planned to
ﬁnance future investment needs (including working capital investments) using a
debt ratio of 20%. The stock was expected to have a beta of 1 for the period of
the analysis, and the Treasury bond rate was 6.50%. (There were 63 million
shares outstanding, and the market risk premium was 5.5%.)
a. Assuming that capital expenditures and depreciation offset each other after
1998, estimate the value per share. Is this a realistic estimate?
b. Assuming that capital expenditures continue to be 200% of depreciation
even after 1998, estimate the value per share.
c. What would the value per share have been, if the ﬁrm had continued to ﬁnance
new investments with its old ﬁnancing mix (5%)? Is it fair to use the same beta
for this analysis?
4. Dionex Corporation, a leader in the development and manufacture of ion chromography systems (used to identify contaminants in electronic devices), reported
earnings per share of $2.02 in 1993, and paid no dividends. These earnings were
expected to grow 14% a year for ﬁve years (1994 to 1998) and 7% a year after
that. The ﬁrm reported depreciation of $2 million in 1993 and capital spending
of $4.20 million, and had 7 million shares outstanding. The working capital was
expected to remain at 50% of revenues, which were $106 million in 1993, and
were expected to grow 6% a year from 1994 to 1998 and 4% a year after that.
The ﬁrm was expected to ﬁnance 10% of its capital expenditures and working
capital needs with debt. Dionex had a beta of 1.20 in 1993, and this beta was
expected to drop to 1.10 after 1998. (The Treasury bond rate was 7%, and the
market risk premium was 5.5%.)
a. Estimate the expected free cash ﬂow to equity from 1994 to 1998, assuming
that capital expenditures and depreciation grow at the same rate as earnings.
Questions and Short Problems
377
--- page 397 ---

b. Estimate the terminal price per share (at the end of 1998). Stable ﬁrms in this
industry have capital expenditures that are 150% of revenues, and maintain
working capital at 25% of revenues.
c. Estimate the value per share today, based on the FCFE model.
5. Biomet Inc., which designs, manufactures, and markets reconstructive and
trauma devices, reported earnings per share of $0.56 in 1993, on which it
paid no dividends (it had revenues per share in 1993 of $2.91). It had capital
expenditures of $0.13 per share in 1993, and depreciation in the same year of
$0.08 per share. The working capital was 60% of revenues in 1993 and was
expected to remain at that level from 1994 to 1998, while earnings and revenues were expected to grow 17% a year. The earnings growth rate was expected to decline linearly over the following ﬁve years to a rate of 5% in
2003. During the high growth and transition periods, capital spending and
depreciation were expected to grow at the same rate as earnings, but capital
spending would be 120% of depreciation when the ﬁrm reaches steady state.
Working capital was expected to drop from 60% of revenues during the
1994–1998 period to 30% of revenues after 2003. The ﬁrm had no debt currently, but planned to ﬁnance 10% of its net capital investment and working
capital requirements with debt.
The stock was expected to have a beta of 1.45 for the high growth period
(1994 to 1998), and the beta was expected to decline to 1.10 by the time the
ﬁrm goes into steady state (in 2003). The Treasury bond rate is 7%, and the
market risk premium is 5.5%.
a. Estimate the value per share, using the FCFE model.
b. Estimate the value per share, assuming that working capital stays at 60% of
revenues forever.
c. Estimate the value per share, assuming that the beta remains unchanged at
1.45 forever.
6. Will the following ﬁrms be likely to have a higher value from the dividend discount
model, a higher value from the FCFE model, or the same value from both models?
a. A ﬁrm that pays out less in dividends than it has available in FCFE, but
invests the balance in Treasury bonds.
b. A ﬁrm that pays out more in dividends than it has available in FCFE, and
then issues stock to cover the difference.
c. A ﬁrm that pays out, on average, its FCFE as dividends.
d. A ﬁrm that pays out less in dividends that it has available in FCFE, but uses
the cash at regular intervals to acquire other ﬁrms with the intent of diversifying.
e. A ﬁrm that pays out more in dividends than it has available in FCFE, but borrows money to cover the difference. (The ﬁrm is overlevered to begin with.)
7. You have been asked to value Oneida Steel, a midsize steel company. The ﬁrm
reported $80 million in net income, $50 million in capital expenditures, and
$20 million in depreciation in the just-completed ﬁnancial year. The ﬁrm reported that its noncash working capital increased by $20 million during the year
and that total debt outstanding increased by $10 million during the year. The
book value of equity at Oneida Steel at the beginning of the last ﬁnancial year
was $400 million. The cost of equity is 10%.
a. Estimate the equity reinvestment rate, return on equity, and expected
growth rate for Oneida Steel. (You can assume that the ﬁrm will continue
378
FREE CASH FLOW TO EQUITY DISCOUNT MODELS
--- page 398 ---

to maintain the same debt ratio that it used last year to ﬁnance its reinvestment needs.)
b. If this growth rate is expected to last ﬁve years and then drop to a 4% stable
growth rate after that and the return on equity after year 5 is expected to be
12%, estimate the value of equity today, using the projected free cash ﬂows
to equity.
8. Luminos Corporation, a manufacturer of lightbulbs, is a ﬁrm in stable growth.
The ﬁrm reported net income of $100 million on a book value of equity of $1
billion. However, the ﬁrm also had a cash balance of $200 million on which it
earned after-tax interest income of $10 million last year. (This interest income is
included in the net income, and the cash is part of the book value of equity.) The
cost of equity for the ﬁrm is 9%.
a. Estimate the noncash return on equity at Luminos Corporation.
b. If you expect the cash ﬂows from the operating assets of Luminos to increase
3% a year in perpetuity, estimate the value of equity at Luminos.
Questions and Short Problems
379
--- page 399 ---

CHAPTER 15
Firm Valuation: Cost of Capital and
Adjusted Present Value Approaches
T
he preceding two chapters examined two approaches to valuing the equity in the
ﬁrm—the dividend discount model and the free cash ﬂow to equity (FCFE) valuation model. This chapter examines approaches to valuation in which the entire
ﬁrm is valued, by either discounting the cumulated cash ﬂows to all claim holders
in the ﬁrm by the weighted average cost of capital (the cost of capital approach) or
by adding the marginal impact of debt on value to the unlevered ﬁrm value—the
adjusted present value (APV) approach.
In the process of looking at ﬁrm valuation, we also look at how leverage may
or may not affect ﬁrm value. We note that in the presence of default risk, taxes, and
agency costs, increasing leverage can sometimes increase ﬁrm value and sometimes
decrease it. In fact, we argue that the optimal ﬁnancing mix for a ﬁrm is the one
that maximizes ﬁrm value.
FREE CASH FLOW TO THE FIRM
The free cash ﬂow to the ﬁrm (FCFF) is the sum of the cash ﬂows to all claim holders in the ﬁrm, including common stockholders, bondholders, and preferred stockholders. There are two ways of measuring the free cash ﬂow to the ﬁrm.
One is to add up the cash ﬂows to the claim holders, which would include
cash ﬂows to equity (deﬁned either as free cash ﬂow to equity or as dividends);
cash ﬂows to lenders (which would include principal payments, interest expenses, and new debt issues); and cash ﬂows to preferred stockholders (usually
preferred dividends):
FCFF = Free cash ﬂow to equity + Interest expense(1 −Tax rate)
+ Principal repayments −New debt issues + Preferred dividends
Note, however, that we are reversing the process that we used to get to free cash
ﬂow to equity, where we subtracted out payments to lenders and preferred stockholders to estimate the cash ﬂow left for stockholders. A simpler way of getting
to free cash ﬂow to the ﬁrm is to estimate the cash ﬂows prior to any of these
claims. Thus we could begin with the earnings before interest and taxes, net out
380
--- page 400 ---

taxes and reinvestment needs, and arrive at an estimate of the free cash ﬂow to
the ﬁrm:
FCFF = EBIT(1 −Tax rate) + Depreciation −Capital expenditure −Δ Working capital
Since this cash ﬂow is prior to debt payments, it is often referred to as an unlevered
cash ﬂow. Note that this free cash ﬂow to the ﬁrm does not incorporate any of the
tax beneﬁts due to interest payments. This is by design, because the use of the aftertax cost of debt in the cost of capital already considers this beneﬁt, and including it
in the cash ﬂows would double count it.
FCFF and Other Cash Flow Measures
The differences between FCFF and FCFE arise primarily from cash ﬂows associated
with debt—interest payments, principal repayments, and new debt issues—and
other nonequity claims, such as preferred dividends. For ﬁrms at their desired debt
level, which ﬁnance their capital expenditures and working capital needs with this
mix of debt and equity and use new debt issues to ﬁnance principal repayments, the
free cash ﬂow to the ﬁrm will exceed the free cash ﬂow to equity.
One metric that is widely used in valuation is the earnings before interest,
taxes, depreciation, and amortization (EBITDA), a rough measure of cash ﬂows
form operations. The free cash ﬂow to the ﬁrm is a related concept but it is more
complete because it takes into account the potential tax liability from the earnings as well as capital expenditures and working capital requirements.
Some analysts also use after-tax operating income as a proxy for free cash ﬂow
to the ﬁrm, with alternative deﬁnitions of operating income. The ﬁrst, earnings before interest and taxes (EBIT) or operating income, comes directly from a ﬁrm’s income statements. Adjustments to EBIT yield the net operating proﬁt or loss after
taxes (NOPLAT) or the net operating income (NOI). The net operating income is
deﬁned to be the income from operations prior to taxes and nonoperating expenses.
Each of these measures is used in valuation models, and each can be related to
the free cash ﬂow to the ﬁrm. Each, however, makes some assumptions about the
relationship between depreciation and capital expenditures that are made explicit
in Table 15.1.
Growth in FCFE versus Growth in FCFF
Will equity cash ﬂows and ﬁrm cash ﬂows grow at the same rate? Consider the
starting point for the two cash ﬂows. Equity cash ﬂows are based on net income or
earnings per share—measures of equity income. Firm cash ﬂows are based on operating income (i.e., income prior to debt payments). As a general rule, you would expect growth in operating income to be lower than growth in net income, because
ﬁnancial leverage can augment the latter. To see why, let us go back to the fundamental growth equations laid out in Chapter 11:
Expected growth in net income = Equity reinvestment rate × Return on equity
Expected growth in operating income = Reinvestment rate × Return on capital
Free Cash Flow to the Firm
381
