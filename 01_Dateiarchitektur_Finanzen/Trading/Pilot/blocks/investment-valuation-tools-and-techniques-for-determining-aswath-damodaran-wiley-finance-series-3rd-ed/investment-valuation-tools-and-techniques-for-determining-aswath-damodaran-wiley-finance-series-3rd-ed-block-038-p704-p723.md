# INVESTMENT VALUATION TOOLS AND TECHNIQUES FOR DETERMINING -- Aswath Damodaran -- Wiley finance series, 3rd ed_, Hoboken, N_J, New Jersey, -- John -- isbn13 9781118011522 -- f84d1622bdc2de526da0dda803c52830 -- Anna’s.pdf — pages 704–723

--- page 704 ---

by a publicly traded company, but not registered with the SEC, that can be sold
through private placements to investors but cannot be resold in the open market
for a one-year holding period, and only limited amounts can be sold after that.
When this stock is issued, the issue price is set much lower than the prevailing
market price,  and the difference is viewed as a discount for illiquidity. The results of three studies that have looked at the magnitude of this discount are listed
below:
1. Maher (1976) examined restricted stock purchases made by four mutual funds
in the period 1969 to 1973 and concluded that they traded at an average discount of 35.43 percent on publicly traded stock in the same companies.
2. Moroney (1973) reported a mean discount of 35 percent for acquisitions of
146 restricted stock issues by 10 investment companies, using data from
1970.
3. Silber (1991) examined restricted stock issues from 1984 to 1989 and found
that the median discount for restricted stock was 33.75 percent.
In summary, then, there seems to be a substantial discount attached, at least on average, when an investment is not liquid. Much of the practice of estimating illiquidity discounts seems to build on these averages. For instance, rules of thumb often
set the illiquidity discount at 20 to 30 percent of estimated value, and there seems
to be little or no variation across ﬁrms.
Silber (1991) also examined factors that explained differences in discounts
across different restricted stocks by relating the size of the discount to observable
ﬁrm characteristics including revenues and the size of the restricted stock offering.
He reported the following regression:
ln(RPRS) = 4.33 + 0.036 ln(REV) −0.142 ln(RBRT)
+ 0.174 DERN + 0.332 DCUST
where
RPRS = Restricted stock price/Unrestricted stock price = 1 −Illiquidity
discount
REV = Revenues of the private ﬁrm (in millions of dollars)
RBRT = Restricted block relative to total common stock in %
DERN = 1 if earnings are positive; 0 if earnings are negative
DCUST = 1 if there is a customer relationship with the investor; 0 otherwise
The illiquidity discount tends to be smaller for ﬁrms with higher revenues, decreases as the block offering decreases, and is lower when earnings are positive and
when the investor has a customer relationship with the ﬁrm.
These ﬁndings are consistent with some of the determinants that we identiﬁed
in the previous section for the illiquidity premium. In particular, the discounts
tend to be smaller for large ﬁrms (at least as measured by revenues) and for
healthy ﬁrms (with positive earnings being the measure of ﬁnancial health). This
would suggest that the conventional practice of using constant discounts across
private ﬁrms is wrong and that we should be adjusting for differences across
ﬁrms.
Estimating the Illiquidity Discount
If we do decide to adjust the illiquidity discount
to reﬂect the differences across private ﬁrms, we are faced with an estimation
question. How are we going to measure these differences and build them into an
Estimating Valuation Inputs at Private Firms
685
--- page 705 ---

estimate? There are two ways of doing this. The ﬁrst is to extend the analysis done
for restricted securities into the illiquidity discount; in other words, we could adjust the discount factor for the magnitude of a ﬁrm’s revenues and whether it has
positive earnings. The second is to extend some of the empirical work that has
been done examining the magnitude of the bid-ask spread for publicly traded ﬁrms
to estimating illiquidity discounts.
Adjusted Discount Factors
Consider again the regression that Silber presents on
restricted stock. Not only does it yield a result speciﬁc to restricted stock, but it also
provides a measure of how much lower the discount should be as a function of revenues. A ﬁrm with revenue of $20 million should have a illiquidity discount that is
1.19 percent lower than a ﬁrm with revenues of $10 million. Thus we could establish a benchmark discount for a proﬁtable ﬁrm with speciﬁed revenues (say $10
million) and adjust this benchmark discount for individual ﬁrms that have revenues
much higher or lower than this number. The regression can also be used to differentiate between proﬁtable and unproﬁtable ﬁrms. Figure 24.1 presents the difference
in illiquidity discounts across both proﬁtable and unproﬁtable ﬁrms with different
revenues, using a benchmark discount of 25 percent for a ﬁrm with positive earnings and $10 million in revenues.
There are clearly dangers associated with extending a regression run on a small
number of restricted stock to estimating discounts for private ﬁrms, but it does provide at least a road map for adjusting discount factors.
Bid-Ask Spread Approach
The biggest limitation of using studies based on restricted stock is that the samples are small. We would be able to make far more
FIGURE 24.1
Illiquidity Discounts: Base Discount of 25 Percent for Proﬁtable Firm with
$10 Million in Revenues
686
VALUING PRIVATE FIRMS
--- page 706 ---

precise estimates if we could obtain a large sample of ﬁrms with illiquidity discounts. We would argue that such a sample exists, if we consider the fact that an
asset that is publicly traded is not completely liquid. In fact, liquidity varies widely
across publicly traded stock. A small company listed over-the-counter is much less
liquid than a company listed on the New York Stock Exchange, which in turn is
much less liquid than a large-capitalization company that is widely held. In fact, the
difference between the bid price and the ask price that we observe on publicly
traded assets can be viewed as a measure of the cost of instant liquidity. An investor
who buys an asset, changes his or her mind, and decides to sell the asset immediately will pay the bid-ask spread.
While the bid-ask spread might only be a quarter or half a dollar, it looms as a
much larger cost when it is stated as a percent of the price per unit. For a stock that
is trading at $2, with a bid-ask spread of 1/4, this cost is 12.5 percent. For higherprice and very liquid stocks, the illiquidity discount may be less than 0.5 percent of
the price, but it is not zero.
What relevance does this have for illiquidity discounts on private companies?
Think of equity in a private company as a stock that never trades. On the continuum
just described, you would expect the bid-ask spread to be high for such a stock, and
this would essentially measure the illiquidity discount.
To make estimates of the illiquidity discounts using the bid-ask spread as the
measure, you would need to relate the bid-ask spread of publicly traded stocks to
variables that can be measured for a private business. For instance, you could
regress the bid-ask spread against the revenues of the ﬁrm and a dummy variable
reﬂecting whether the ﬁrm is proﬁtable, and extend the regression done on restricted stocks to a much larger sample. You could even consider the trading volume for publicly traded stocks as an independent variable and set it to zero for a
private ﬁrm. Using data from the end of 2000, for instance, we regressed the bidask spread for Nasdaq stocks against revenues, a dummy variable for positive earnings, cash as a percent of ﬁrm value, and trading volume.
Spread = 0.145 −0.0022 ln(Annual revenues) −0.015(DERN)
−0.016(Cash/Firm value) −0.11($ Monthly trading volume/Firm value)
Plugging in the corresponding values—with a trading volume of zero—for a private
ﬁrm should yield an estimate of the bid-ask spread for the ﬁrm.
ILLUSTRATION 24.10:
Estimating the Illiquidity Discount for Chez Pierre
Since Chez Pierre is being valued for a private transaction, it is appropriate to consider an illiquidity
discount. We can use both approaches described earlier to estimate the magnitude of that discount
1. Restricted stock approach: To estimate the illiquidity discount for Chez Pierre, we assume that
the base discount for a ﬁrm with $10 million in revenues would be 25%. Chez Pierre’s revenues
of $1.2 million, being smaller than the typical ﬁrm, should result in a higher discount on their
value. We estimate the difference in the illiquidity discount between a ﬁrm with $10 million in
revenue and $1.2 million in revenue to be 3.75%. To do this, we ﬁrst estimated the illiquidity discount in the Silber equation for a ﬁrm with $10 million in revenues.
100 −exp[4.33 + 0.036ln(10) −0.142ln(l00) + 0.174(1)]
Iliquidity discountbase =
100
= 48.94%
Estimating Valuation Inputs at Private Firms
687
--- page 707 ---

We then reestimated the illiquidity discount with revenues of $ 1.2 million:
Difference in discount = 52.69% −48.94% = 3.75%
The estimated illiquidity discount for Chez Pierre would therefore be 28.75%, which is the base
discount of 25% adjusted for the additional discount to reﬂect smaller revenues that the ﬁrm
possesses.
2. Bid-ask spread approach: We could substitute in the revenues of Chez Pierre the fact that it has
positive earnings and the cash as a percent of revenues held by the ﬁrm (1%):
Spread = 0.145 −0.0022 ln(Annual revenues) −0.015(DERN)
−0.016 (Cash/ﬁrm value) −0.11($ Monthly trading volume/Firm value)
= 0.145 −0.0022 ln(1.2) −0.015(1) −0.016(.03) −0.11(0) = .1294 or 12.94%
Based on this approach, we would estimate an illiquidity discount of 12.94%.
VALUATION MOTIVES AND VALUE ESTIMATES
In the preceding section, we considered how best to estimate the inputs to use in
valuing a private ﬁrm. As we considered each input, though, we noted that the
process of estimation might be different depending on the potential buyer of the
ﬁrm. With betas, for instance, we argued that the market beta should be used if
the potential buyer is a publicly traded ﬁrm or a stock market investor (in an initial public offering) and that a total beta should be used if the potential buyer is a
private party. We made similar arguments about the cost of debt and cash ﬂows.
Table 24.2 summarizes the differences in the way we estimate the inputs to valuation for different valuation motives.
The results of using different approaches to estimating discount rates and
cash ﬂows, depending on the potential buyer, can have signiﬁcant effects on
value. In general, a private business that is up for sale will be valued much more
highly by a publicly traded ﬁrm than by a private entity. This can be traced to the
fact that the discount rates are higher when we assume that the buyer is not diversiﬁed. Thus the owners of private businesses who are interested in selling their
businesses will be well served looking for potential buyers who are publicly
traded ﬁrms. While they might not be able to extract the entire value, they can try
to obtain at least a share of the additional value created because the marginal investors are diversiﬁed.
The same implications arise when looking at the alternative of going public.
The value that a ﬁrm can obtain from a public offering will exceed the value that
it will receive from a private entity. The values obtained from an initial public
100 −exp[4.33 + 0.036ln(1.2) −0.142ln(l00) + 0.174(1)]
Illiquidity discountChez Pierre =
100
= 52.69%
688
VALUING PRIVATE FIRMS
liqdisc.xls: This spreadsheet allows you to estimate the illiquidity discount for private
ﬁrms using both the restricted stock approach and the bid-ask spread approach.
--- page 708 ---

offering and sale to a publicly traded ﬁrm will be based on similar discount rates,
but may vary because of cost and revenue synergies. If the potential for these synergies is large, selling to a publicly traded ﬁrm may result in a higher value than
going public.
ILLUSTRATION 24.11:
Valuing Chez Pierre for a private sale
To value Chez Pierre for a private sale, we draw on the inputs that we have estimated in prior illustrations:
After-tax operating income in most recent year = $319,620 (1 – .40) = $191,770
(from illustration 24.7)
Cost of capital = 15.27% (from illustration 24.6)
Expected Growth rate = 2% a year for the next 12 years (from illustration 24.8)
Reinvestment rate = 0% (from illustration 24.8)
Pre-tax operating income in most recent year = $319,620 (from illustration 24.7)
FCFF in most recent year = $319,620 (1 – .40) (1 – 0) = $191,770
At the end of year 12, we assume that the restaurant will be closed and that the liquidation proceeds
will be $500,000. (from illustration 24.9)
The present value of the operating cash ﬂows over the next 12 years is estimated ﬁrst:
PV of FCFF for next 12 years =
.1527 – .O2
= $1,134,121
1.0212
1 – 1.152712
$191,770
TABLE 24.2
Estimation of Inputs for Valuation: Valuation Motives
Valuation for Sale to a
Valuation for Sale to
Publicly Traded Firm or for
a Private Entity
an Initial Public Offering
Cost of equity
Based on total beta, with
Based on market beta, since
correlation reﬂecting
marginal investor is
diversiﬁcation of potential
diversiﬁed
buyer
Cost of debt
May reﬂect additional spread
Based on synthetic rating,
associated with being a
estimated by looking at
private business
publicly traded ﬁrms
Operating cash ﬂows
Private business tax rate used
Corporate marginal tax rates
in valuation
used in valuation
Firm life
Finite life terminal value or
Perpetual life when
liquidation value
estimating terminal value
Illiquidity discount
Value discounted for
No illiquidity discount
illiquidity
Valuation Motives and Value Estimates
689
--- page 709 ---

Adding the present value of the liquidation proceeds (discounted back 12 years at 15.27%) and subtracting out the present value of lease commitments yields the value of equity:
PV of operating cash ﬂows for next 12 years
= $1,134,121
+ PV of liquidation value = $500,000/1.152710
= $     90,821
– PV of operating lease commitments
= $   928,333
Value of equity
= $   296,709
Based on our estimates for growth and cost of capital, the value of the equity in Chez Pierre is
$296,709.
ILLUSTRATION 24.12:
Valuing Infosoft for an initial public offering
To value Infosoft for an initial public offering, we gather the inputs that we have already estimated for
the company:
a. Cost of capital: In illustration 24.6, we use a bottom-up market beta  for Infosoft and estimated a
cost of equity and capital of 11.50%:
Cost of equity = 3.5% + 1.60 (5%) = 11.50%
Cost of capital = Cost of equity = 11.50%
In the terminal value computation (in illustration 24.9), we argued for a decrease in beta of
1.20 and an increase in the debt ratio to 10%, leading to a cost of capital of 8.85% in stable
growth.
b. Cash ﬂows and growth rates: In illustration 24.7, we presented the current income statement
for Infosoft, with pre-tax operating income of $1.5 million and a tax rate of 40%. In illustration
24.8, we estimated a return on capital of 20% and a reinvestment rate of 90% for Infosoft,
which we assumed would be maintained for the next 5 years, allowing for expected growth of
18% in earnings.
c. Terminal value: In illustration 24.9, we assumed that the ﬁrm would be in stable growth after
year 10, growing 3% a year, while maintaining a return on capital of 12%.  The ﬁve years between the high growth period (lasting 5 years) and the stable growth (after year 10) represent a
transition phase, where growth rates, reinvestment rates and costs of capital all change from
high growth levels to stable growth levels. The table below summarizes the cash ﬂows and the
present value (in ‘000s).
Cumulated
EBIT
Expected Reinvestment
Cost of
cost of
Year
(1 – t)
growth
Rate
FCFF
capital
capital
PV
Current
$900
1
$1,062
18.00%
90.00%
$106
11.50%
1.1150
$95
2
$1,253
18.00%
90.00%
$125
11.50%
1.2432
$101
3
$1,479
18.00%
90.00%
$148
11.50%
1.3862
$107
4
$1,745
18.00%
90.00%
$174
11.50%
1.5456
$113
5
$2,059
18.00%
90.00%
$206
11.50%
1.7234
$119
6
$2,368
15.00%
77.00%
$545
10.97%
1.9124
$285
7
$2,652
12.00%
64.00%
$955
10.44%
2.1121
$452
8
$2,891
9.00%
51.00%
$1,416
9.91%
2.3214
$610
9
$3,064
6.00%
38.00%
$1,900
9.38%
2.5391
$748
10
$3,156
3.00%
25.00%
$2,367
8.85%
2.7638
$856
Sum
$3,487
690
VALUING PRIVATE FIRMS
--- page 710 ---

At the end of year 10, the firm is in stable growth and the terminal value is estimated as
follows:
Discounting the terminal value back, adding it to the present value of cash ﬂows during the
high growth period and subtracting out debt (zero) yields a value of $19.065 million for the
equity.
Value of equity = $3,487 + $41,675/2.7638 + 500 = $19,066
d. Getting to value of equity per share: To get to value of equity per share, we value the 100,000 equity options that are held by managers and venture capitalists in the company, subtract the value
from the value of equity, before dividing by the 1 million shares outstanding.
Value of management options (in ‘000s) = $1,161
Value of equity = ($19,066 – $1,161)/1000 = $17.90/share
Control Issues
When valuing a ﬁrm, you need to consider the competence and strengths of the
management of the ﬁrm. With private ﬁrms, where the owner is also the manager,
this consideration carries special weight, since the owner has absolute control. In
a publicly traded ﬁrm, in contrast, incompetent management can often be replaced, if enough stockholders can be convinced that it is in their best interests to
do so.
There are implications for valuation if a portion of a private ﬁrm is offered for
sale. If that portion provides a controlling interest (i.e., the right to pick the ﬁrm’s
management), it should have a substantially higher value than if it does not provide
this power. Normally, this would mean that 51 percent of a private ﬁrm’s equity
should trade at a substantial premium over 49 percent. This applies whether a ﬁrm
is being sold to a private entity or a publicly traded ﬁrm, and may arise in an initial
public offering. If, for instance, only nonvoting shares or shares with diluted voting
rights are offered to investors in the public offering, they should trade at a discount
on shares with full voting rights.
While the intuition about the value of control is simple, estimating how much
it is worth is a little more difﬁcult. We will defer a full discussion of the topic until
the next chapter, on acquisitions, but we will value it as the difference between two
values—the value of the ﬁrm run optimally and the value of the ﬁrm with the incumbent management. For instance, if the value of a private ﬁrm run by incumbent
management is $100 million and the value of the ﬁrm run optimally is $150 million, the difference in values between the 51 percent and 49 percent shares can be
computed as follows:
Value of controlling interest = 51% of optimal value = .51 × 150 = $76.5 million
Value of noncontrolling interest = 49% of status quo value = .49 × 100 = $49 million
EBIT(1 −tax rate)10 (1 + g) (1 −Reinvestment Rate)
Terminal value (000s) =
(Cost of capital – g)
$3,156(1.03)(1 −.25)
=
(.0885 −.03)
= $41,675
Valuation Motives and Value Estimates
691
--- page 711 ---

The additional 2 percent interest (from 49 to 51 percent) has a disproportionate
effect on value because of control. This value of control will be greatest for private
ﬁrms that are poorly run and will be close to zero for well-run ﬁrms.
As we noted in chapter 16, the same approach can be used to compute the
discount that nonvoting shares will trade at relative to voting shares in initial
public offerings.
The values of the two classes can be estimated as follows:
ILLUSTRATION 24.13:
Valuing Voting and Non voting Shares: Infosoft
In the last illustration, we valued the equity in InfoSoft at $17.904 million. Based upon the 1 million
shares oustanding, we estimated a value per share of $17.90. Assume that the ﬁrm decides to create
.9 million nonvoting shares and .1 million voting shares. In the initial offering, only the nonvoting
shares will be sold to the public, and the current owners will retain all of the voting shares.
To value the voting and nonvoting shares, we need to value InfoSoft under optimal management.
Assume that the ﬁrm would be worth $20 million under optimal management.4 The value of the voting
and nonvoting shares can then be computed.
Assume that the fact that incumbent managers will retain the voting shares reduces the probability of
management change to 25%.
$17.904
= .1 + .9
Status quo value
Value per voting share =
# Voting shares + # Nonvoting shares
= $23.14
(Optimal −Status quo value) × Probability of change
+
# Voting Shares
($20 −$17.904)(0.25)
.1
+
$17.904
= .1 + .9
Status quo value
Value per nonvoting share =
# Voting shares + # Nonvoting shares
= $17.90
692
VALUING PRIVATE FIRMS
4InfoSoft was revalued at its optimal debt ratio. We assumed that the existing investment policy was optimal.
Value per nonvoting share
Status quo value
 Number of voting shares + Nonvoting shares
Value per voting share
Status quo value
Number of voting shares + Nonvoting shares
(Optimal value − Status quo value) × Probability of change
Number of voting shares
=
=
+
--- page 712 ---

VALUING VENTURE CAPITAL AND PRIVATE EQUITY STAKES
In the previous illustrations we looked at two extremes in the private company valuation spectrum: a private-to-private transaction, where the buyer and the seller
were completely undiversiﬁed (and thus exposed to total risk) and a private-topublic transaction, an IPO, or sale of a private to a public company, where more
conventional valuation approaches work.
There is an intermediate case, where venture capitalists and private equity investors
take stakes in private businesses, with the intent of cashing out when the company goes
public or is sold to a public entity. Venture capitalists and private equity investors are
more diversiﬁed than private owners, but they are not as diversiﬁed as investors in public markets are for two reasons. The ﬁrst is that they specialize in a few businesses: Many
venture capitalists invest only in biotechnology companies or software businesses. The
second is that the size of their positions (which tend to be large) and the need for oversight restrict them from having more than a handful of open positions at any time.
In a sense, if you think of total beta as the appropriate measure for the completely undiversiﬁed end of the spectrum and market beta as the right risk measure
for the completely diversiﬁed buyer, venture capitalists and private equity investors
fall in the middle of the spectrum. In fact, we can modify the total beta equation to
reﬂect these differences:
Thus, we are replacing the correlation of the private ﬁrm with the market with
the correlation of the investor’s portfolio. At the limit, a private equity investor like
Blackstone or KKR may have so many holdings spread over so many different businesses that the correlation of their portfolios with the market will approach 1 and
the beta that they should use is a market beta.
To see how this will play out, assume that you are valuing a private business
operating in a sector where publicly traded companies have an average beta of 1
and where the average correlation of ﬁrms with the market is 0.25. Assume that
this company will be fully owned by its current owner for two years, will raise capital from a technology venture capitalist at the start of year 3, and is expected to either go public or be sold to a publicly traded ﬁrm at the end of year 5. We estimate
the cost of equity at three stages (Risk-free rate = 4%; Equity risk premium = 5%):
Stage 1: The nascent business, with a private owner who is fully invested in that business.
Perceived beta = 1/ 0.25 = 4
Cost of equity = 4% + 4(5%) = 24%
Stage 2: Angel ﬁnancing provided by specialized venture capitalist who holds multiple investments, in high-technology companies. (Correlation of portfolio
with market is 0.5.)
Perceived beta = 1/0.5 = 2
Cost of equity = 4% + 2(5%) = 14%
Stage 3: Public offering, where investors are retail and institutional investors with
diversiﬁed portfolios:
Perceived beta = 1
Cost of equity = 4% + 1(5%) = 9%
Market beta
VC or private equity beta = Correlation of VC or PE investor’s
portfolio with market
Valuing Venture Capital and Private Equity Stakes
693
--- page 713 ---

Now assume that you have projected cash ﬂows for this company for the next ﬁve
years and expect it to be a stable growth ﬁrm after it goes public in year 5, growing 2% a year in perpetuity. The value of the business can be estimated as follows:
Terminal
1
2
3
4
5
Year
Expected CF
$100
$125
$150
$165
$170
$175
Market beta
1
1
1
1
1
1
Correlation
0.25
0.25
0.5
0.5
0.5
1
Beta used
4.00
4.00
2.00
2.00
2.00
1.00
Cost of equity
24.00%
24.00% 14.00%
14.00%
14.00%
9.00%
Terminal value
$2,500
Cumulated COE 1.2400
1.5376
1.7529
1.9983
2.2780
2.4830
PV
$80.65
$81.30
$85.57
$82.57
$1,172.07
Value of ﬁrm
$1,502
Note that using the private owner’s cost of equity (24%) forever would have
yielded too low a value ($1,221) and using the market beta cost of equity (9%) forever would resulted in too high a value ($2,165).
694
VALUING PRIVATE FIRMS
PRECASH AND POSTCASH VALUATIONS
When valuing private companies, many analysts draw a distinction between
precash and postcash valuations. In general, this is done when an infusion of
cash is anticipated either from venture capitalists or from an initial public offering. The precash valuation values the ﬁrm before the cash inﬂux and the
postcash valuation values it after.
There are two reasons why the valuations may yield different values. The
ﬁrst is that the ﬁrm may face capital rationing constraints without the infusion
of the cash, resulting in a scaling down of how much it can reinvest  and consequently how quickly it can grow. If the ﬁrm’s return on capital is greater
than the cost of capital, this will cause the value to be lower before the cash
inﬂux. The second is that the value of cash and marketable securities is added
to the value of the operating assets to arrive at ﬁrm value. After a large cash
inﬂux, ﬁrms may have excess cash to invest in marketable securities, which
when added to the value of operating assets will increase value. If the cash is
taken out of the ﬁrm, though, by the existing owners, you should not add the
cash to the value.
Which of these two values should be used to estimate the value per share
in a public offering? Since stockholders in the ﬁrm will hold stock in the postcash ﬁrm, the postcash value should be used. In the case of a venture capitalist,
though, the answer may be different. If the venture capitalist has bargaining
power—she is the only person who is interested in providing venture capital—
she can ask for a share of the ﬁrm value based on the precash valuation, arguing that the increase in value is feasible only with the additional venture
capital. If two or more venture capitalists are interested in the ﬁrm, odds are
that the postcash valuations will be the basis for deciding how much of the
ﬁrm will be yielded to the venture capitalist.
--- page 714 ---

ILLUSTRATION 24.14:
Valuing a Private Equity Stake
Assume that you work for a publicly traded ﬁrm and have been asked to value a potential stake in a
small, privately held ﬁrm that wants you to invest $10 million in its equity, which it plans to use to expand operations.
First, you would value the private ﬁrm assuming that you do not invest the $10 million. Based on
the projected cash ﬂows, assume that you value the equity in the ﬁrm at $30 million:
Precash valuation = $30 million
Now assume that your investment of $10 million will allow the ﬁrm to grow faster and that the present
value of the expected cash ﬂows is $50 million for the equity. (This present value does not include the
cash inﬂow of $10 million from the private equity investment.)
Postcash valuation = $50 million + $10 million = $60 million
The key question, assuming that you decide to make this investment, is the percentage of the private
ﬁrm you should demand in return for the $10 million investment. At the minimum, you would demand
a share of the postcash valuation:
Share of ownershipminimum = Cash invested/Postcash valuation = 10/60 = 16.66%
However, you would bargain for a larger share. At the limit, you could argue for a share of the precash
valuation:
Share of ownershipmaximum = Cash investment/(Precash valuation + Cash investment)
= 10/(30 + 10) = 25%
RELATIVE VALUATION OF PRIVATE BUSINESSES
The essence of relative valuation is that you value a ﬁrm based on how much the
market is paying for similar ﬁrms. This premise is clearly more challenging for private businesses. Notwithstanding these problems, analysts have tried to extend the
relative valuation practices that have been developed for public companies into the
private business space. In general, there are two approaches used by analysts for
coming up with comparable ﬁrms in private company valuation. Some analysts focus on transaction prices paid for other private businesses, arguing that these businesses are likely to have more in common with the young business being valued.
Other analysts, distrustful of private transaction prices, draw on the market prices
of publicly traded companies in the same business, and try to adjust for differences
in fundamentals.
Private Transaction Multiples
Since you are valuing a young, private business, it
seems logical that you should look at what others have paid for similar businesses in the recent past. That is effectively the foundation on which private
transaction multiples are based. In theory, at least, you pull together a dataset of
other young, private businesses, similar to the one that we are valuing (same
business, similar size, and at the same stage in the life cycle), that have been
bought/sold and the transaction values. You then scale these values to a common
variable (revenues, earnings, or something even sector-speciﬁc) and compute a
Relative Valuation of Private Businesses
695
--- page 715 ---

typical multiple that acquirers have been willing to pay. Applying this multiple
to the same variable for the company being valued should yield an estimated
value for the company.
Potential Problems
The biggest problem used to be the absence of organized
databases of private business transactions, but that is no longer the case. Many
private services offer databases (for a price) that contain this data,5 but other
problems remain:
■Arms-length transactions. One of the perils of using prices from private transactions is that some of them are not arms’-length transactions, where the
price reﬂects just the value of business being sold. In effect, the price includes
other services and side factors that may be speciﬁc to the transaction. Thus, a
doctor selling a medical practice may get a higher price because he agrees to
stay on for a period of time after the transaction to ease the transition.
■Timing differences. Private business transactions are infrequent and reﬂect the
fact that the same private business will not be bought and sold dozens of times
during a particular period. Unlike public ﬁrms, where the current price can be
used to compute the multiples for all ﬁrms at the same point in time, private
transactions are often staggered across time. A database of private transactions can therefore include transactions from June 2008 and December 2008,
a period when the public markets lost almost 45 percent of their value.
■Scaling variable. To compare ﬁrms of different scale, we generally divide the
market price by a standardizing variable. With publicly traded ﬁrms, this can
take the form of revenues (price/sales, EV/sales), earnings (PE, EV/EBITDA), or
book value. While we could technically do the same with private transactions,
there is a potential roadblock. There are broad differences in accounting standards across private businesses and these differences can result in bottom lines
that are not quite equivalent.
■Nonstandardized equity. Equity claims in private businesses can vary widely in
terms of cash ﬂow, control claims, and illiquidity. The transaction price for equity in a private business will reﬂect the claims that are embedded in the equity
in that business and may not easily generalize to equity in another ﬁrm with
different characteristics.
■Non-U.S. ﬁrms. Most of the transaction databases that are available and accessible today are databases of transactions of private businesses in the United
States. As we are called upon increasingly to value businesses in other markets,
some of which are riskier, emerging markets, it is not clear how or even
whether this data can be used in that context.
Usefulness and Best Practices
So, when is it appropriate to use private transaction
data to value a private business? As a general rule, this approach works best for
small businesses that plan to stay small and private, rather than expand their reach
and perhaps go public. It also helps if the ﬁrm being valued is in a business where
there are not only a large number of other private businesses but also where transactions are common. For instance, this approach should work well for valuing a
696
VALUING PRIVATE FIRMS
5BIZCOMPS, IBA Market Data and Pratt Stats all provide transaction data for private businesses.
--- page 716 ---

medical/dental practice or a small, retail business. It will get more difﬁcult to apply
for ﬁrms that are in unique or unusual businesses.
If you decide to employ private company transactions to value a business, there
are ﬁve general practices that can help to deliver more dependable valuations:
1. Scale to variables that are less affected by discretionary choices: As a counter
to the problem of wide differences in accounting and operating standards
across private companies, can focus on variables where discretionary choice
matters less. For instance, multiples of revenues (which are more difﬁcult to
fudge or manipulate) should be preferred to multiples of earnings. You could
even scale value to units speciﬁc to the business being valued—number of patients for a general medical practice or the number of customers for a plumbing business.
2. Value businesses, not equity. In Chapter 16, we classiﬁed multiples into equity
multiples (where equity value is scaled to equity earnings or book value) and
enterprise value multiples (where the value of the business is scaled to operating earnings, cash ﬂows, or the book value of capital). Given the wide differences in equity claims and the use of debt across private businesses, it is better
to focus on enterprise value multiples rather than equity multiples. In other
words, it is better to value the entire business and then work out the value of
equity than it is to value equity directly.
3. Start with a large dataset: Since transactions with private businesses are infrequent, it is best to start with a large dataset of companies and collect all transaction data. This will then allow you to screen the data for transactions that look
suspicious (and are thus likely to fail the arm’s-length test).
4. Adjust for timing differences. Even with large datasets of private transactions,
there will timing differences across transactions. While this is not an issue in a
period where markets are stable, you should make adjustments to the value
(even if they are crude) to account for the timing differences. For instance, using June 2008 and December 2008 as the transaction dates, you would reduce
the transaction prices from June 2008 by the drop in the public market (a small
cap index like the Russell 5000 dropped by about 40 percent over that period)
to make the prices comparable.
5. Focus on differences in fundamentals. The notion that the value of a business depends on its fundamentals—growth, cash ﬂows, and risk—cannot be
abandoned just because you are doing relative valuation. The estimated
value is likely to be more reliable if you can collect other measures of the
transacted private businesses that reﬂect these fundamentals. For instance, it
would be useful to obtain not only the transaction prices of private businesses but also the growth in revenues recorded in these businesses in the period prior to the transactions and the age of the business (to reﬂect maturity
and risk). You can explore the data to see if there is a relationship between
transaction value and these variables, and if there is one, to build it into the
valuation.
Public Multiples
It is far easier to obtain timely data on pricing and multiples for
publicly traded ﬁrms. In fact, for those analysts who do not have access to private
transaction data, this is the only option when it comes to relative valuation. The
Relative Valuation of Private Businesses
697
--- page 717 ---

peril, though, is that you are extending the pricing lessons that you learn from
looking at more mature, publicly traded ﬁrms to a private business.
Problems
The issues we face in applying public market multiples to private businesses, especially early in the life cycle, are fairly obvious:
■Life cycle affects fundamentals. If you accept the premise that only those young
ﬁrms that make it through the early phase of the life cycle and succeed are
likely to go public, you also have to accept the reality that public ﬁrms will
have different fundamentals from private ﬁrms. Generally, public ﬁrms will be
larger, have less potential for growth, and have more established markets than
private businesses, and these differences will manifest themselves in the multiples investors pay for public companies.
■Diversiﬁed versus undiversiﬁed investors. When we discussed estimating risk
and discount rates for young, private businesses, we noted the different perspectives on risk that diversiﬁed investors in public companies have, relative to
equity investors in private businesses, and how that difference can manifest itself as higher costs of equity for the latter. When you use multiples of earnings
or revenues, obtained from a sample of publicly traded ﬁrms with diversiﬁed
investors, to value a private business with undiversiﬁed investors, you will
over-value the latter.
■Liquidity. Since equity in publicly traded companies is more liquid than equity in private businesses, the value obtained by using public multiples will
be too high if used for a private business. Just as we had to adjust for illiquidity in intrinsic valuation, we have to adjust for illiquidity with relative
valuation.
Usefulness and Best Practices
What types of private businesses are best valued using public company multiples? Generally, companies that aspire to reach a larger
market and either go public or be acquired by a public company are much better
candidates for this practice. In effect, you are valuing the company for what it
wants to be, rather than what it is today.
There are three simple practices that can not only prevent egregious valuation
errors but also lead to better valuations:
1. Adjust for survival. To the extent that private businesses have limited access to
capital, they are also more exposed to failure. When valuing private businesses,
using public company multiples, you have to adjust for this additional risk of
failure.
2. Adjust for nondiversiﬁcation. Earlier in the chapter, we developed the total
beta measure for undiversiﬁed investors and argued that the higher cost of equity that results from using it will lower intrinsic value. The same rationale
should be applied when doing relative valuation. If the average PE ratio for
publicly traded restaurants in 12, you would expect Chez Pierre to trade at a
lower PE ratio, even if it has the same characteristics.
3. Adjust for illiquidity. In the last section on intrinsic valuation, we presented
different ways of estimating illiquidity discounts for equity in private businesses. We could adopt the same techniques to adjust the public multiple value
for illiquidity.
698
VALUING PRIVATE FIRMS
--- page 718 ---

CONCLUSION
The value of a private ﬁrm is the present value of the cash ﬂows it is expected to
generate, discounted back at a rate that reﬂects both the risk in the private ﬁrm and
the mix of debt and equity it uses. While this statement is identical to the one used
to describe the value of a publicly traded ﬁrm, there are differences in the way we
estimate these inputs for private ﬁrms, and even among private ﬁrms, depending on
the motive for the valuation.
When valuing a private ﬁrm for sale to an individual or private entity, we have
to consider three speciﬁc issues. The ﬁrst is that the cost of equity, which we have
hitherto assumed to be determined purely by the risk that cannot be diversiﬁed,
might have to be adjusted for the fact that the potential buyer is not well diversi-
ﬁed. The second is that equity holdings in private businesses are illiquid, leading to
a discount on the estimated value. The discounts on restricted stock issues made by
publicly traded ﬁrms or the bid-ask spreads of these ﬁrms may provide us with useful information on how large this discount should be. The third is that a controlling
interest in equity of a private ﬁrm can trade at a signiﬁcant premium over a
minority interest.
The valuation of a private ﬁrm for sale to a publicly traded ﬁrm or initial public offering follows a much more conventional route. We can continue to assume
that the cost of equity should be based only on nondiversiﬁable risk and there is no
need for an illiquidity discount. There can still be a control value if less than a
controlling interest is sold to the publicly traded ﬁrm or if nonvoting shares are issued in the initial public offering.
QUESTIONS AND SHORT PROBLEMS
In the problems following, use an equity risk premium of 5.5 percent if none is
speciﬁed.
1. You have been asked to value Barrista Espresso, a chain of espresso coffee shops
that have opened on the East Coast of the United States.
■The company had earnings before interest and taxes of $10.50 million in the
most recent year on revenues of $50 million. However, the founders of the
company had never charged themselves a salary, which would have
amounted to $1 million if based on comparable companies.
■The tax rate is 36% for all ﬁrms, and working capital is 10% of revenues.
■The capital expenditures in the most recent year amounted to $4.5 million,
while depreciation was only $1 million.
■Earnings, revenues, and net capital expenditures are expected to grow 30% a
year for ﬁve years, and 6% after that forever.
■The comparable ﬁrms have an average beta of 1.3567 and an average D/E
ratio of 13.65%. The average correlation with the market is 0.50.
Barrista Espresso is expected to maintain a debt ratio of 12% and face a
cost of debt of 8.75%. The risk-free rate is 6%, and the market risk premium is 5.5%.
Questions and Short Problems
699
--- page 719 ---

a. Estimate the value of Barrista Espresso as a ﬁrm.
b. Estimate the value of equity in Barrista Espresso.
c. Would your valuation be different if you were valuing the ﬁrm for an
IPO?
2. You have valued a business, using discounted cash ﬂow models, at $250 million for a private sale. The business, which does make money, had revenues
of $200 million in the most recent year. (The average ﬁrm has revenues of
$10 million.) How much of a liquidity discount would you apply to this
ﬁrm:
a. Based on the Silber regression?
b. Based on correcting the average discount (25%) for the size of the ﬁrm?
3. You are valuing a bed-and-breakfast in Vermont with the following information:
■The business had pretax operating income of $100,000 in the most recent
year. This income has grown 5% a year for the past three years, and is expected to continue growing at that rate for the foreseeable future.
■About 40% of this operating income can be attributed to the fact that
the owner is a master chef. He does not plan to stay on if the business is
sold.
■The business is ﬁnanced equally with debt and equity. The pretax cost of borrowing is 8%. The beta for publicly traded ﬁrms in the hospitality business is
1.10. The Treasury bond rate is 7%, the market risk premium is 5.5%, and
the tax rate is 40%.
■The capital maintenance expenditure, net of depreciation, was $10,000 in
the most recent year, and it is expected to grow at the same rate as operating income.
■The business is expected to have an operating life of 10 years, after which the
building will be sold for $500,000, net of capital gains taxes.
a. Value the business for sale.
b. How much would the value change if the owner offered to stay on for the
next three years?
4. You have been asked by the owner of Tectonics Software, a small ﬁrm that produces and sells computer software, to come up with an estimate of value for the
ﬁrm for an initial public offering. The ﬁrm had revenues of $20 million in the
most recent year, on which it made earnings before interest and taxes of $2 million. The ﬁrm had debt outstanding of $10 million, on which pretax interest expenses amounted to $1 million. The book value of equity is $10 million. The
average unlevered beta of publicly traded software ﬁrms is 1.20, and the average
market value of equity of these ﬁrms is, on average, three times the book value of
equity. All ﬁrms face a 40% tax rate. Capital expenditures amounted to $1 million in the most recent year and were twice the depreciation charge in that year.
Both items are expected to grow at the same rate as revenues for the next ﬁve
years. The return on capital after year 5 is expected to be 15%. The revenues of
this ﬁrm are expected to grow 20% a year for the next ﬁve years and 5% after
that, and the operating margins will remain at existing levels. The Treasury bond
rate is 6%.
a. Estimate the cost of capital for the ﬁrm.
b. Estimate the value of the equity in the ﬁrm.
c. If the ﬁrm plans to issue 1 million shares, estimate the value per share.
700
VALUING PRIVATE FIRMS
--- page 720 ---

5. How would your answer to (4) change if you were valuing Tectonics Software
for sale to a private individual? The individual in question has a portfolio that is
not diversiﬁed and has a correlation of 0.60 with the market index. In addition,
use the following bid-ask spread equation to estimate the illiquidity discount:
Bid-ask spread = 0.14 −0.015 ln(Revenues)
Estimate the value of equity in the private transaction.
Questions and Short Problems
701
--- page 721 ---

CHAPTER 25
Aquisitions and Takeovers
F
irms are acquired for a number of reasons. In the 1960s and 1970s, ﬁrms such as
Gulf & Western and ITT built themselves into conglomerates by acquiring ﬁrms
in other lines of business. In the 1980s, corporate giants like Time Inc., Beatrice
Foods, and RJR Nabisco were acquired by other ﬁrms, their own management, or
wealthy raiders, who saw potential value in restructuring or breaking up these
ﬁrms. The 1990s saw a wave of consolidation in the media business as telecommunications ﬁrms acquired entertainment ﬁrms, and entertainment ﬁrms acquired cable businesses. Through time, ﬁrms have also acquired or merged with other ﬁrms
to gain the beneﬁts of synergy, in the form of either higher growth or lower costs.
Acquisitions seem to offer ﬁrms a shortcut to their strategic objectives, but the
process has its costs. This chapter examines the four basic steps in an acquisition,
starting with establishing an acquisition motive, continuing with the identiﬁcation
and valuation of a target ﬁrm, and following up with structuring and paying for the
deal. The ﬁnal, and often the most difﬁcult, step is making the acquisition work after the deal is consummated.
BACKGROUND ON ACQUISITIONS
When we talk about acquisitions or takeovers, we are talking about a number of
different types of transactions. These transactions can range from one ﬁrm merging
with another ﬁrm to create a new ﬁrm to managers of a ﬁrm acquiring the ﬁrm
from their own stockholders and creating a private ﬁrm. This section begins by
looking at the different forms taken by acquisitions, continues by providing an
overview on the acquisition process, and concludes by examining the history of the
acquisitions in the United States.
Classifying Acquisitions
There are several ways in which an acquisition can be structured. In a merger, the
boards of directors of two ﬁrms agree to combine and seek stockholder approval
for the combination. In most cases, at least 50 percent of the shareholders of the
target and the bidding ﬁrm have to agree to the merger. The target ﬁrm ceases to
exist and becomes part of the acquiring ﬁrm; Digital Equipment Corporation was
absorbed by Compaq after it was acquired in 1997. In a consolidation, a new ﬁrm
is created after the merger, and both the acquiring ﬁrm and target ﬁrm stockholders
receive stock in this ﬁrm; Citigroup, for instance, was the ﬁrm created after the consolidation of Citicorp and Travelers Group.
702
--- page 722 ---

In a tender offer, one ﬁrm offers to buy the outstanding stock of the other ﬁrm
at a speciﬁc price and communicates this offer in advertisements and mailings to
stockholders. By doing so, it bypasses the incumbent management and board of directors of the target ﬁrm. Consequently, tender offers are often used to carry out
hostile takeovers. The acquired ﬁrm will continue to exist as long as there are minority stockholders who refuse the tender. From a practical standpoint, however,
most tender offers eventually become mergers if the acquiring ﬁrm is successful in
gaining control of the target ﬁrm.
In a purchase of assets, one ﬁrm acquires the assets of another, though a formal
vote by the shareholders of the ﬁrm being acquired is still needed.
There is a one ﬁnal category of acquisitions that does not ﬁt into any of the
four described so far. Here, a ﬁrm is acquired by its own management or by a
group of investors, usually with a tender offer. After this transaction, the acquired
ﬁrm can cease to exist as a publicly traded ﬁrm and become a private business.
These acquisitions are called management buyouts if managers are involved, and
leveraged buyouts if the funds for the tender offer come predominantly from debt.
Figure 25.1 summarizes the various transactions and the consequences for the
target ﬁrm.
Process of an Acquisition
Acquisitions can be friendly or hostile events. In a friendly acquisition, the managers of the target ﬁrm welcome the acquisition and in some cases seek it out. In a
hostile acquisition, the target ﬁrm’s management does not want to be acquired.
The acquiring ﬁrm offers a price higher than the target ﬁrm’s market price prior to
Background on Acquisitions
703
FIGURE 25.1
Classiﬁcation of Acquisitions
Source: Corporate Finance: Theory and Practice, Second Edition, by Aswath Damodaran,
copyright © 2001 by John Wiley & Sons, Inc. This material is used by permission of John
Wiley & Sons, Inc.
A firm can be
acquired by
Another firm
Its own managers
and outside
investors
Merger
Consolidation
Tender offer
Acquisition of
assets
Buyout
Target firm becomes part of acquiring
firm; stockholder approval needed from
both firms.
Target firm and acquiring firm combine
to become new firm; stockholder
approval needed from both firms.
Target firm continues to exist as long
as there are dissident stockholders
holding out. Successful tender offers
ultimately become mergers. No
shareholder approval is needed for
a tender offer.

Target firm remains as a shell company,
but its assets are transferred to the
acquiring firm. Ultimately, target firm
is liquidated.
Target firm continues to exist, but as a
private business. It is usually
accomplished with a tender offer.
--- page 723 ---

the acquisition and invites stockholders in the target ﬁrm to tender their shares for
the price.
In both friendly and hostile acquisitions, the difference between the acquisition
price and the market price prior to the acquisition is called the acquisition premium. The acquisition price, in the context of mergers and consolidations, is the
price that will be paid by the acquiring ﬁrm for each of the target ﬁrm’s shares. In a
friendly merger, this price is usually based on negotiations between the acquiring
ﬁrm and the target ﬁrm’s managers. In a tender offer, it is the price at which the acquiring ﬁrm receives enough shares to gain control of the target ﬁrm. This price
may be higher than the initial price offered by the acquirer, if there are other ﬁrms
bidding for the same target ﬁrm or if an insufﬁcient number of stockholders tender
at that initial price. For instance, in 1991 AT&T initially offered to buy NCR for
$80 per share, a premium of $25 over the stock price at the time of the offer.
AT&T ultimately paid $110 per share to complete the acquisition.
There is one ﬁnal comparison that can be made, and that is between the price paid
on the acquisition and the accounting book value of the equity in the ﬁrm being
acquired. After the acquisition is complete, the target ﬁrm’s assets can be reappraised,
following strict accounting rules, to fair value to estimate the adjusted book value of
equity. Depending on how the acquisition is accounted for, the difference between the
acquisition price and the adjusted book value of equity will be recorded as goodwill on
the acquiring ﬁrm’s books or not be recorded at all. Figure 25.2 presents the breakdown
of the acquisition price into these component parts.
704
ACQUISITIONS AND TAKEOVERS
FIGURE 25.2
Breaking Down the Acquisition Price
Source: Corporate Finance: Theory and Practice, Second Edition, by Aswath Damodaran,
copyright © 2001 by John Wiley & Sons, Inc. This material is used by permission of John
Wiley & Sons, Inc.
