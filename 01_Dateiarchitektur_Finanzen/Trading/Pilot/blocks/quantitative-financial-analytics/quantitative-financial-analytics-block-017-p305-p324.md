# Quantitative financial analytics_ the path to investment profits.pdf — pages 305–324

--- page 305 ---

282
Quantitative Financial Analytics
approximate growth rate of dividends over time. Given an expected
dividend growth rate g, we may revise Equation (7.1) to the following:
P0 = D(1 + g)0
(1 + i)0
+ D(1 + g)1
(1 + i)1
+ · · · + D(1 + g)∞
(1 + i)∞
P0 =
∞

t=0
D(1 + g)t
(1 + i)t .
(7.14)
In this instance, D0 = D(1 + g)0, D1 = D(1 + g)1, and so on. Under
conditions of continuous compounding, Equation (7.14) becomes:
P0 =
 ∞
0
Degte−itdt.
(7.15)
Which may be integrated, assuming g and i are constant and g<i,
as follows:
P0 =
 ∞
0
Degte−itdt =
 ∞
0
De−t(i−g)dt
= D

−
1
i −ge−t(i−g)

−D

−
1
i −ge−t(i−g)

= D

−
1
i −ge−∞

−D

−
1
i −ge−0

=
D
i −g.
(7.16)
Equation (7.16) is a useful summary of the variables determining
the price of a growth stock. It can be rewritten in an even more
informative way:
i = D
P0
+ g.
(7.17)
This, in eﬀect, tells us that the two components of the return on
a growth stock are the dividend yield (D/P0) and the growth in
expected dividends. When the ﬁrm’s retention rate (b) is expected to
be constant, the dividend growth must equal the growth in earnings.
Under these assumptions, the shares will sell at a constant P/E
multiple (assuming interest rates also remain constant), and the
--- page 306 ---

Analysis of Common Stocks
283
earnings growth must equal the growth in share price. Thus, if D/E
and P/E are constant, then Equation (7.17) indicates the total return
to stockholders from dividends (D/P0) and from capital gains (g).
The factors that determine the rate g are very important and
should be understood by the analyst. Foremost in importance is the
rate of return that the ﬁrm generates on its investment in assets.
A broad indication of this rate may be obtained from examining
the earning power of total investment ratio over time (EBIT/total
assets). This ratio is the best single measure of the pretax return that
the ﬁrm generates on its assets and should be scrutinized carefully
for every growth stock. A second factor is the degree of ﬁnancial
leverage assumed by the ﬁrm and the spread between payments
to bondholders and the earning power of total investment. The
size of this spread will determine the residual return remaining for
stockholders. A third factor that is also of crucial importance is the
retention ratio b(1−the dividend payout ratio). Every dollar retained
and reinvested should be reﬂected in the growth rate.
We may be somewhat more speciﬁc about the determinants
of g. Suppose a corporation is entirely ﬁnanced by equity capital.
Moreover, suppose that increases in equity come about solely from
the retention of earnings. In this case, growth in earnings (dividends)
before tax would be given by:
g = br.
(7.18)
where
b is the rate of earning retention
r is the return on assets (EBIT to total assets)
On an after-tax basis, 7.18 would become:
g = b(1 −t)r.
(7.19)
This would follow because the growth in assets would be determined
by b and the return on assets would be r. The after-tax return on
assets would be (1−t)r. Multiplying (1−t)r times the rate of growth
of the asset base would produce the rate of growth of earnings. We
may consider an example. Suppose International Copy Machines is
--- page 307 ---

284
Quantitative Financial Analytics
a growth company. It now has the following income statement and
balance sheet (simpliﬁed):
Income Statement Period t = 0
Balance Sheet As of t = 0
Sales
$1,000,000
Assets
$1,000,000
Expenses
750,000
EBIT
250,000
Bonds
– 0 –
Taxes
125,000
Equity
1,000,000
N.I.
$125,000
$1,000,000
In the steady state (all things remaining the same), the ﬁrm would
have a return on its asset base (EBIT to total assets) of 0.25. The
ﬁrm ﬁnances entirely by retaining earnings. If it elected to retain no
earnings (pay out all earnings in dividends), the asset base could not
grow, sales would not increase, and net income would remain the
same over time (that is, the ﬁrm would not be a growth company).
This can be veriﬁed through the use of Equation (7.6).
g = (0)(1 −0.5)(0.25) = 0.
On the other hand, if the ﬁrm decided to retain, say, 40 percent of its
earnings, the asset base would increase by (0.4)(125,000) = $50,000.
The new asset base would be $1,050,000. Given the extra assets, and
assuming the return on investment continued at 0.25, the new income
statement generated in period t = 1 would be:
Income Statement Period t = 1
EBIT
$262,500∗
Taxes
131,250
N.I.
$131,250
∗(0.25) ($1,050,000)
--- page 308 ---

Analysis of Common Stocks
285
This would represent a growth in net income of [(131,250 −
125,000)/125,000] = 5.0 percent. Equation (7.6) would give us the
same result:
g = (0.4)(1 −0.5)(0.25) = 0.05.
Suppose the ﬁrm retained all its earnings. The growth rate would be:
g = (1.0)(1 −0.5)(0.25) = 0.125.
Of course, to use Equation (7.19) to determine corporate earnings
growth rates, it must be assumed: (1) that the ﬁrm ﬁnances entirely
with retained earnings; and (2) that the tax rate and the rate of
return on investment remain constant. Neither of these assumptions
may hold in the real world, although this fact should not be terribly
important. Assumption (1) can be relaxed easily enough, and a
revised equation can be formulated for a ﬁrm that employs debt
as well as equity ﬁnance. The revised equation is:
G = [(1 −t)(b)][L(r −c) + r].
(7.20)
where
L is the leverage ratio (debt to equity) employed by the ﬁrm
c is the average coupon rate of interest paid on
corporate debt.
(Note that Equation (7.20) will be developed in the “Growth Rate
Equations” section below.)
If it may be assumed that the tax rate, interest cost, and
debt-equity ratio will be constant over time, then we may deﬁne
R = (1 −t)[L(r −c) + r] as the after-tax return on equity and,
furthermore, Equation (7.20) may be restated as g = bR. If we may
further assume, as is often done in the case of regulated utilities, that
earnings retained will earn at the required return on equity (i), then
R = i. Solving Equation (7.17), we obtain:
i = D
P0
+ g
i = D
P0
+ bR
--- page 309 ---

286
Quantitative Financial Analytics
i = (1 −b)E0
P0
+ bi
i −bi = (i −b)E0
P0
(1 −b)i = (1 −b)E0
P0
i = E0P0.
Thus, in this special case, the inverse of the P/E ratio will provide
the expected return on the stock.
The only diﬀerence between Equations (7.20) and (7.19) is that
any extra return on investment above the interest payments made to
bondholders is shown to inﬂuence the stockholders’ earnings growth
rate. Thus, if International ﬁnances half with bonds and half with
equity (L = 1), it would earn (1 −t)r on the asset investment made
possible by equity sources (for example, 0.5×0.25 = 12.5 percent). If
it retained b percent of its earnings, the growth produced by equity
sources would be b(1 −t)r. If b = 0.4 (60 percent dividend payout),
g = 0.4 × 12.5 = 5.0 percent. Bond ﬁnancing would produce another
(r −c) return on the assets ﬁnanced with debt sources. If c = 6
percent, r−c would be 0.25−0.06 = 0.19. Thus, the earnings growth
resulting from debt ﬁnance would be b(1 −t)L(r −c), or (0.4) (0.5)
(1) (0.19) = 3.8 percent. The total growth rate would be 5.0 percent
(from equity sources) plus 3.8 percent (debt sources), or 8.8 percent.
This example is presented numerically in Table 7.1.
Equation (7.20) can be used by the analyst to determine whether
the ﬁrm is getting favorable or unfavorable leverage. If r > c,
leverage would be favorable, and debt ﬁnancing would improve the
shareholders’ net rate of return (net income to stockholders’ equity)
and earnings growth rate. If r < c, leverage would be unfavorable,
and debt ﬁnancing would reduce the return to shareholders and the
earnings growth rate. In the case of International (above), suppose
r = 0.05 and c = 0.08. If the ﬁrm retained all its earnings, but had
no bond ﬁnance, the after-tax growth rate would be:
g = (1)(0.5)(0.05) = 0.025.
--- page 310 ---

Analysis of Common Stocks
287
If the ﬁrm ﬁnanced half with bonds and half with equity, however,
the growth rate would be:
g = [(0.5)(1)][(1)(−0.03) + (0.05)]
= (0.5)(0.02)
= 0.01.
Thus, the rate of growth would be reduced from 2.5 percent to
1.0 percent.
Although Equation (7.20) is an improvement over Equation
(7.19) in that debt ﬁnance is included as a variable, it still harbors
the assumptions of a constant rate of taxation and a constant rate
of return on investment. To the extent that tax rates fall, it should
be obvious that earnings growth rates should improve. Similarly, if
better cost controls (margins) or improved sales-asset relationships
(turnovers) can be eﬀected, higher growth rates could be obtained.
The analyst should be very careful to use existing EBIT/total asset
ratios as a surrogate for return on investment only if that relationship
is expected to hold in the future. Equations (7.19) and (7.20) also
assume that the only source of equity ﬁnance is the retention of
earnings. Empirically, this is not a bad assumption because the sale
of additional shares by existing (non-IPO) publicly held companies
now account for only a negligible part of the total ﬁnancing arranged
by major U.S. corporations in any one year. Otherwise, pro forma
expected ratios should be used.
Mergers and Growth
In many cases, it is possible for a company to grow and acquire assets
over time by the acquisition of other ﬁrms (see Chapter 6). The
attractiveness of such an acquisition is a function of the proﬁtability
of the assets (both tangible and intangible) to be acquired and the
form and amount of payment to be made.
Mergers may occur for any number of reasons. Perhaps the
oldest and strongest motivation is the simple desire to increase
power over the market. The increased market power resulting from
--- page 311 ---

288
Quantitative Financial Analytics
a merger may raise proﬁts through “operating economies,” such as
bulk purchases, reciprocal purchases, advertising discounts, better
channels of distribution (everything from more freight cars when
needed to more shelf space), and better access to and bargaining
position for external funds. Merger also allows a ﬁrm to acquire
large numbers of talented management and research personnel and
at the same time to gain increased market power to sell whatever
they produce.
In other cases, mergers may occur because the acquired company
is a bargain; poor management, inadequate capital, stock market
disfavor, a poor year, or other factors may reduce the price of
the stock to the point that the ﬁrm is worth a great deal more
than the cost of acquiring it. The acquired ﬁrm may have liquid
assets, such that the acquiring ﬁrm could raise more money by
merging with it than by selling securities on the market. It is further
possible that the acquired ﬁrm would have tax-loss carry-forwards
that could be used to reduce future tax liabilities of the merged
company.
There are two remaining arguments for merger that must be
examined rather closely. The ﬁrst is diversiﬁcation. If a ﬁrm is able
to acquire other ﬁrms whose earnings do not correlate very closely
with its own (coeﬃcient of correlation less than +1, and the closer to
−1 the better), the probability distribution for earnings of the new
ﬁrm should show less dispersion (be less risky) than for the old ﬁrm.
If one dollar of earnings for the merged ﬁrm is less risky, it should be
discounted at a lower rate in imperfect markets. This would result
in an increase in the price of the stock and shareholder well-being.
The merger would thus serve a valid economic function. It should be
pointed out, however, that such diversiﬁcation could also be achieved
by shareholders in their own portfolios.
Much is written about the growth resulting from mergers. To the
extent that the merged ﬁrms are able to interact and combine their
talents to do things that neither could do before (the synergism or
“2 + 2 = 5” eﬀect), a valid justiﬁcation for the merger, and perhaps
an increase in stock price, may exist. On the other hand, the merger
of ﬁrms in totally diﬀerent lines of business with no subsequent
--- page 312 ---

Analysis of Common Stocks
289
Table 7.1. Growth and the Levered Firm
International Copy
International Copy
International Copy
Machines Balance Sheet
Machines Income Statement
Machines Sources and Uses
Beginning Period t = 0
For Period t = 0
of Funds For Period t = 0
Assets
$1,000,000
EBIT
$250,000
Retained Earnings
$44,000
Interest
30,000
Bond Sale
44,000
Bonds (6%)
$ 500,000
EBT
$220,000
$88,000
Equity
500,000
Taxes
110,000
$1,000,000
N.I.
$110,000
Asset Purchases
$88,000
Dividends
66,000
Retained Earnings
$ 44.000
International Copy
International Copy
Machines Balance Sheet
Machines Income Statement
Beginning Period t = 1
For Period t = 1
Growth in Net Income
Assets
$1,088,000
EBIT
$272,000∗
119,680 −110,000
110,000
= 8.8%
Interest
32,640
Bonds (6%)
$ 544,000
EBT
$239,360
Equity
544,000
Taxes
119,680
$1,088,000
N.l.
$119,680
∗(.25 × 1,088,000).
--- page 313 ---

290
Quantitative Financial Analytics
interaction may create value through diversiﬁcation but not through
real growth, although growth may appear to occur. Consider the
following:
Ming-Trico-Vaugn (MTV) is a conglomerate. It has 5 million shares
outstanding and earns $6 per share. Because of MTV’s growth
characteristics, it sells at 40 times current earnings ($240 per share).
The Stagnant Steel Co. has 4 million shares outstanding and earns
$2 per share. Because of its poor growth prospects and inherent risk,
the market will only pay 10 times current earnings ($20) for Stagnant
stock. MTV has proposed a merger with Stagnant. No changes will
take place in Stagnant’s operations and the current management
will remain intact. The merger will merely make Stagnant one of
a growing list of companies controlled by MTV. A merger oﬀer has
been tendered giving Stagnant holders one new MTV share for each
10 Stagnant shares outstanding. Because this amounts to an oﬀer of
$240 for $200, virtually every Stagnant shareholder has accepted the
proposal.
In contemplation of the merger, the chairman of MTV has his
accountants prepare a new consolidated pro forma statement of
income. In order to purchase Stagnant, 400,000 additional MTV
shares will be issued. Thus, the new capitalization of the company
should be 5,400,000 shares. Upon consolidating the net income of the
two ﬁrms, the accountants report a revised total income of:
(6.00)(5,000,000) + (3.00)(4,000,000) = $38,000,000.
Dividing this ﬁgure by the new capitalization of 5,400,000 shares
produces an earning per share of:
($38,000,000/5,400,000) = $7.04.
Thus, without changing operations at all, MTV has been able to show
a fantastic increase in earnings of [(7.04−6.00/(6.00)] = 17.3 percent!
Of course, an eﬃcient and rational market would realize that the
above transactions were merely ﬁnancial, and unless the merger
reduced the riskiness of MTV there should be no increase in the price
of MTV shares. In fact, because MTV paid a premium of 20 percent
--- page 314 ---

Analysis of Common Stocks
291
above the value of Stagnant shares, it might be argued that the price
of MTV shares should fall. Unfortunately, a few decades ago these
transactions took place regularly (disproving once again the eﬃcient
market hypothesis) and it took a few years for the investors to realize
that a conglomerate composed of no-growth organic components was
not really a growth company.
Suppose that MTV and Stagnant had perfectly positive (+1)
earnings correlations. Suppose further that rational markets prevailed and MTV stock did not increase after the “new” EPS had been
announced. What would have happened to the earnings multiplier
(P/E) of MTV stock?
$240/$7.04 = 34 times.
Thus, the multiple would have fallen from 40X to 34X. Of course,
this would be quite rational, because the merged company would
be riskier than the premerger MTV (Stagnant was riskier than
MTV) and the future earnings growth rate from operations would
be reduced (Stagnant had very poor earnings growth prospects).
In a less “eﬃcient” market, the old multiple of 40X might hold
(or even a higher one given the new “growth” in earnings). If this
were the case, MTV common would advance to:
(40)($7.04) = $281.60.
Assume that this did indeed happen, and MTV set about to ﬁnd
yet another merger partner. Suppose it found a company, call it
Stagnant II, and consummated a merger on the same terms as with
Stagnant I. What would be the eﬀect on MTV earnings?
a. Price of Stagnant II stock: $20
b. Price markup given to eﬀect merger: 20 percent
c. Price oﬀer to Stagnant II: $24
d. Price of MTV stock: $281.60
e. Number of MTV shares given for each Stagnant II share:
24.00/281.60 = 0.085
f. Number of new MTV shares issued: (0.085) (4,000,000) = 340,000
g. New total earnings: $38 million + $8 million = $46 million
--- page 315 ---

292
Quantitative Financial Analytics
h. New earnings per share: 46,000,000/5,740,000 = $8.01
i. Earnings growth: [(8.01 −7.04)/(7.04)] = 13.8 percent.
We see in this example how it is possible to combine companies
without growth in order to produce a “growth” company. As
indicated in the discussion above, a company must ﬁnd ever-larger
merger partners if the apparent growth rate is not to decline. In
addition, the market must be willing to assign a constant P/E ratio
to earnings of ever-declining quality. On the other hand, if companies
can be bought with convertible securities, warrants, or other kinds
of “funny money,” the apparent growth rate can be made even more
spectacular.
The analyst should be aware of the diﬀerence between growth
achieved from improved operations (“organic” growth) and growth
induced from merger. Although the theoretical distinction between
buying individual assets to increase output (and hopefully proﬁts)
and purchasing other ﬁrms to accomplish the same ends are not
great, the practical diﬀerences may be enormous. Purely ﬁnancial
transactions (such as those illustrated in the example above) should
be viewed with suspicion by the analyst unless there are clear-cut,
real economic beneﬁts accruing to the merging enterprise. Operating
economies, improved market position, better managerial talent,
and so on are all justiﬁable grounds for a merger. Unfortunately,
these elements have not always been ingredients in the business
combinations of recent years.
After-tax returns and growth
The after-tax return on an investment in common stock will depend
on the tax position of the investor and the taxation climate in which
he ﬁnds himself. For growth stocks, capital gains taxation becomes
relatively more important than taxes levied on dividends. Employing
the symbols of Equation (7.8), the after-tax dividend received in each
period t is (1 −mt)Dt where mt is the marginal income tax bracket
of the investor in period t. The capital gain secured by the investor
--- page 316 ---

Analysis of Common Stocks
293
is simply Pn −P0. His tax on the gain is kn(Pn −P0) where kn is
the capital gains tax rate the investor is subject to at period n. His
after-tax capital ﬂow is thus: Pn −[(kn) (Pn −P0)]. His after-tax
return would be given by i in the following equation.
P0 =
n

t=0
(1 −mt)Dt
(1 + i)t
+ Pn −[kn(Pn −P0)]
(1 + t)n
.
(7.21)
An investor purchases a stock that pays a dividend of two dollars
per year. He plans to hold the stock for ﬁve years. The stock now
sells at 18X earnings of ﬁve dollars per share. It is expected that this
multiple will apply in ﬁve years when EPS will be six dollars. The
aftertax dividend return that the investor would get in periods t = 1
through t = 5 (the dividend in t = 0 has just been paid) depends
upon his marginal tax bracket. If this is 40 percent, his after-tax
return would be:
(1 −0.4)($2) = $1.20.
Suppose the investor pays capital gains taxes at one-half his marginal
rate (this set of facts applied for many years prior to the passage of
the Tax Reform Act of 1986); his after-tax capital ﬂow would be:
$108 −[(0.2)(108 −90)] = $104.40.
The investor’s after-tax rate of return would be:
at 5 percent,
(4.329) (1.20) = $5.19
(0.784) (104.40) = 81.85
$87.04
at 4 percent,
(4.452) (1.20) = $5.34
(0.822) (104.40) = 85.82
$91.16
Or about 4.3 percent.
--- page 317 ---

294
Quantitative Financial Analytics
Notice how the diﬀering tax rates on dividends and capital gains
inﬂuence the results. In 1986, the rules changed such that all income
was taxed at 28 percent. A few years later, rates advanced (under
Presidents George H.W. Bush and Bill Clinton). Presently, both
dividends (with certain exceptions) and capital gains are taxed at
lower rates than other income; but all this will most likely change
many times in the future. Readers are cautioned that politicians are
ﬁckle (and often stupid) and change the rules just to show they are
“doing something” to deserve the money they are paid!
Riskiness of Stocks
In addition to the expected return estimate that the analyst has
made, he needs to have some basic measure of the riskiness of
the security he is analyzing. In the material to follow, we shall be
attempting to measure the “absolute” or “total” risk associated
with a common stock. Nevertheless, the important risk variable is
the “non-diversiﬁable” or “systematic” element — that risk that
cannot be diversiﬁed away in an eﬃcient portfolio. When we begin
constructing optimal portfolios in Chapter 9, the reader will observe
that there are two parameters required for evaluation: (1) the
expected return from holding a security; and (2) the covariances
among returns of all securities in the portfolio. At this point, however,
it should be noted that the variance is required before covariances
may be estimated. Many analysts rely entirely on agency ratings
to determine risk, and others use ratio analysis to discern the
overall liquidity, proﬁtability, leverage, and so on of the ﬁrm whose
common stock is being considered. These methods are useful, but by
themselves are inadequate. If the analyst has prepared probability
distributions in estimating the expected return from the investment,
he may use these distributions to determine the deviations around
the expected values. A simple example will serve to explain. Suppose
an analyst has speciﬁed a probability distribution for the sales of the
Ace Co. He has also determined a conditional distribution of costs
given each level of sales. (A more complicated set of conditional
probability distributions could be prepared to take into account
--- page 318 ---

Analysis of Common Stocks
295
various categories of expenses.) Finally, he has calculated an overall
distribution of net income and dividend payments.
Sales in (millions)
Total Expenses
Net Income
70 (.2)
30 (.06)
100 (.3)
80 (.6)
20 (.18)
90 (.2)
10 (.06)
65 (.1)
25 (.05)
90 (.5)
75 (.7)
15 (.35)
85 (.2)
5 (.10)
60 (.2)
20 (.04)
80 (.2)
70 (.5)
10 (.10)
80 (.3)
0 (.06)
If the ﬁrm has 10 million shares outstanding, the data may be
grouped into a distribution of EPS:
EPS
Probability
$3.00
0.06
2.50
0.05
2.00
0.22
1.50
0.35
1.00
0.16
0.50
0.10
0.00
0.06
1.00
From this, the analyst may construct a dividend payment distribution. Suppose he believes that management will pay a maximum
dividend of two dollars but will distribute less if earnings are low.
Within the range of EPS from one dollar to two dollars, he believes a
0.75 payout will take place. Below earnings of one dollar, no dividend
--- page 319 ---

296
Quantitative Financial Analytics
will be paid. The DPS distribution would be:
DPS
Probability
$2.00
0.11
1.50
0.22
1.121/2
0.35
0.75
0.16
0.00
0.16
1.00
The expected value of EPS and DPS and their standard deviations
may be computed. They equal:
EPS
DPS
µ = $1.50
$1.06
σ = 0.72.
0.58
The analyst may repeat the above process for each year in the
anticipated holding period of the security. Suppose he obtained the
following:
Year
EPS
DPS
1
µ = $1.50
$1.06
σ = 0.72
0.58
2
µ = 1.80
1.20
σ = 0.85
0.64
3
µ = 2.00
1.40
σ = 0.95
0.76.
Thus, he would have expected values and deviations for EPS and
DPS over the three-year holding period. He could next determine
a distribution of multiples to get the expected price in three years.
--- page 320 ---

Analysis of Common Stocks
297
Assume he forecasts the following:
P/E Multiple
Probability
10×
0.6
12×
0.4
This distribution could be combined with the earnings distribution
for year three to obtain a distribution of prices. Ideally, each multiple
should be combined with each EPS to get the distribution. If the EPS
distribution were:
EPS
Probability
$3.50
0.2
2.00
0.6
0.50
0.2
and if it were assumed that the P/E multiple was independent from
the forecasted EPS (an assumption that may not hold), the price
distribution would be:
Multiple
×
EPS
=
Price
$3.50 (.2)
$35.00 (.12)
10×(.6)
2.00 (.6)
20.00 (.36)
.50 (.2)
5.00 (.12)
3.50 (.2)
42.00 (.08)
10×(.4)
2.00 (.6)
24.00 (.24)
.50 (.2)
6.00 (.08)
Grouping the data:
Price
Probability
$42.00
0.08
35.00
0.12
24.00
0.24
(Continued )
--- page 321 ---

298
Quantitative Financial Analytics
Price
Probability
20.00
0.36
6.00
0.08
5.00
0.12
1.00
The expected price and its standard deviation would be: µ = $21.60,
σ = $10.50.
In the example presented above, all the separate return distributions were assumed to be independent. Most likely, they will not be.
Generally, if a ﬁrm does poorly in the early years of an investmentholding period, it will continue to do poorly. Thus, the dividend
distributions of later years may well depend upon the outcomes in
previous years. Furthermore, the EPS distribution in the terminal
year will almost always be correlated with the dividend distribution
of that year. Finally, the value of the P/E multiple in the terminal
year will most likely be inﬂuenced by the earnings and dividend
performance in earlier years. Thus, the analyst should attempt to
construct conditional probabilities, where appropriate, for all the
distributions involved.
Suppose an analyst has projected the following distributions for
a stock that is to be held for two years:
Year 
P/E=10(.5)
D2=$.40(.4); EPS=$.80
P/E=11(.5)
D1=$.50(.4)
P/E=11(.5)
D2=$.50(.6); EPS=$1.00
P/E=12(.5)
P/E=12(.5)
D2=$.60(.5); EPS=$1.20
P/E=13(.5)
D1=$.60(.6)
P/E=13(.5)
D2=$.80(.5); EPS=$1.60
P/E=14(.5)
Year 
--- page 322 ---

Analysis of Common Stocks
299
Eight outcomes (with associated probabilities) would be possible:
D1
D2
Pn
Prob.
a.
$0.50
$0.40
$8.00
0.08
b.
0.50
0.40
8.80
0.08
c.
0.50
0.50
11.00
0.12
d.
0.50
0.50
12.00
0.12
e.
0.60
0.60
14.40
0.15
f.
0.60
0.60
15.60
0.15
g.
0.60
0.80
20.80
0.15
h.
0.60
0.80
22.40
0.15
1.00
The yield from each combination (a–h) can be computed, given the
current market price of the security, which is assumed to be $8, and
placed in a probability distribution.
Combination
Yield (percent)
Probability
A
5.6
0.08
B
10.4
0.08
C
23.1
0.12
D
28.2
0.12
E
40.7
0.15
F
46.1
0.15
G
68.1
0.15
H
74.1
0.15
The expected yield from this distribution is 41.8 percent with a
standard deviation of 22.6 percent.
For situations where more outcomes are designated (and where
the time span is longer) many combinations are possible. In these
--- page 323 ---

300
Quantitative Financial Analytics
instances, hand calculation becomes exceedingly tedious, and again
the analyst must rely on the computer to do the computational work.
Risk Measures for Common Stock Returns
Once the analyst has speciﬁed his DPS and terminal price distributions for each year, he may compute an overall return-risk measure for
the equity under investigation. If it is assumed that all distributions
are independent, the following equations may be employed:
Vµ =
n

t=0
¯Dt
(1 + i)t +
¯Pn
(1 + i)n ,
(7.22)
and,
σ =




n

t=0
( ¯Dσ
t )2
(1 + i)2t +
( ¯P σ
n )2
(1 + i)2n .
(7.23)
where
Vµ
is the present value of the dividend stream and terminal
selling price.
¯Dt
is the expected dividend in period t.
¯Pn
is the expected terminal price at period n.
i
is the rate of return from the investment.
σ
is the overall standard deviation around the present value.
Dσ
t
is the standard deviation of dividends in period t.
P σ
n
is the standard deviation around the expected market
price at period n.
Referring back to the ﬁrst example constructed in the previous
section (the Ace Co.), we may solve for Vµ and σ. Suppose an investor
wished to determine the probability of earning at least 10 percent on
the purchase of the stock. The present value of his projected return
stream would be:
Vµ = (1.06)
(1.10)1 + (1.20)
(1.10)2 + (1.40)
(1.10)3 + (21.60)
(1.10)3 = $19.13.
--- page 324 ---

Analysis of Common Stocks
301
If the current market price of the stock were $19.13, the investor
would expect to obtain the 10 percent return. If the current market
price were lower, he would expect a larger return. If it were higher,
he would expect a lower return.
The risk from purchasing the stock would be:
σ =

(0.58)2
(1 + 0.10)2 +
(0.64)2
(1 + 0.10)4 +
(0.76)2
(1 + 0.10)6 +
(10.50)2
(1 + 0.10)6
= $7.94.
If the stock were selling at $11.19 (that is, $19.13 −$7.94) and the
underlying distributions were normal, the investor would determine
the probability that he would earn less than 10 percent:
P(X|X ≤Vµ −1σ) ≈0.16.
At the opposite extreme from having completely independent
ﬂows is the case of perfectly correlated returns. In this instance, any
deviation from the mean value of a ﬂow in any particular period
would be matched by deviations in all other periods in exactly the
same manner. The present value of the dividend stream and terminal
selling price would be the same as in the independent case (Equation
(7.22)), but the overall standard deviation around the present value
would be given by:
σ =
n

t=0
Dσ
t
(1 + i)t +
P σ
n
(1 + i)n .
(7.24)
If the ﬂows in the above example were perfectly correlated, the risk
from purchasing the stock would be:
σ =
0.58
(1 + 0.10)1 +
0.64
(1 + 0.10)2 +
0.76
(1 + 0.10)3 +
10.50
(1 + 0.10)3
= $9.52.
Not surprisingly, the overall risk is greater when returns are perfectly
correlated than when returns are independent.
In the real world, it will be unusual for returns to be either
perfectly correlated or independent. A more likely situation would
