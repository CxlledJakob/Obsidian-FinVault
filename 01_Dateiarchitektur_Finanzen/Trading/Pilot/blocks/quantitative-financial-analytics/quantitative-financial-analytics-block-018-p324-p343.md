# Quantitative financial analytics_ the path to investment profits.pdf — pages 324–343

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
--- page 325 ---

302
Quantitative Financial Analytics
be a mixture of the two with parts of the return stream being
independent and other parts being perfectly correlated. In this more
realistic case, the present value of the stream would still be given by
Equation (7.23), but the overall standard deviation would be much
more complex:
σ =





 n

t=0
(Dσ
t )2
(1 + i)2t +
(P σ
n )2
(1 + i)2n

+
m

k=1

 n

t=0
(Dσ
t )(k)
(1 + i)t

+ (P σ
n )(k)
(1 + i)n
2
,
(7.25)
where Dσ
t and P σ
n are the dividend-price standard deviations for the
independent portion of the ﬂow returns; and (Dσ
t )k and (P σ
n )k are
the dividend-price standard deviations for stream k of a perfectly
correlated portion of the ﬂow returns.
Reconsidering our example, suppose it can be determined that
the dividend stream is perfectly correlated. That is, poor corporate
performance in period t = 1 that results in a lower dividend payment
than the expected value would also mean poor performance in period
t = 2 and t = 3. Because the stock price at period t = 3 depends
on future dividends (beyond t = 3), and these dividends would
also be inﬂuenced by the poor performance of earlier years, at least
part of the variation in stock price for t = 3 would be perfectly
correlated with dividend-stream variations. Nevertheless, there may
be other factors inﬂuencing stock prices (such as the overall level of
interest rates or simply random events) so that part of the variation
in stock price is also independent. Assume that we can determine
that about 80 percent of the stock price variation in period t = 3
is traceable to the riskiness of the dividend stream, and 20 percent
results from other (independent) factors. Given this information, we
could reformulate Equation (7.25) to get the overall deviation for the
investment:
σ =




(P σ
3 )2
(1 + 0.10)6 +

 3

t=1
(Dσ
t )(1)
(1 + 0.10)t +
(P σ(1)
3
)
(1 + 0.10)3
2
--- page 326 ---

Analysis of Common Stocks
303
=



(2.10)2(0.564) + [(0.58)(0.909) + (0.64)(0.826)
+(0.76)(0.751) + (8.40)(0.751)]2
= $8.09.
Notice that the overall riskiness of the mixed case lies between the
extremes of perfect correlation and independence.
The above formulations can also be used to generate a distribution of rates of return. The following steps should be employed:
1. Compute Vµ and σ for an initial value of i.
2. Determine the number of standard deviations that would equalize
the present price of the stock and Vµ (that is, solve Vµ + Zσ = P0
for Z).
3. Find P(X|X ≤Vµ + Zσ) from Appendix C. This will be the
probability that Vµ will be less than the present price of the stock
at the given i and is, in turn, the probability that the rate of
return will be less than i.
4. Plot the probability determined above on a cumulative probability
distribution.
5. Iterate steps 1–4 above varying i in order to generate a complete
cumulative probability distribution.
6. Convert the cumulative distribution to a discrete probability
distribution of rates of return.
7. For a two-parameter description, the 15th percentile of the
cumulative probability distribution will provide an estimate of the
mean (expected) rate of return. Dividing the interquartile range
by 1.35 will provide an estimate of σ.
Thus, the analyst would have a percentage rate of return expected
from the purchase of a stock and the standard deviation around that
percentage. There are other approaches to the problem of generating
µ and σ statistics of rates of return. Below we consider one such
method in detail. When the analyst has speciﬁed distributions with
many more possible outcomes than we have dealt with above, manual
calculations are not feasible and a computer must be employed. It is,
--- page 327 ---

304
Quantitative Financial Analytics
of course, possible to attempt a deterministic solution on a computer
that would merely compute a probability distribution of returns
employing all observations from all distributions. Greater ﬂexibility
at less cost can usually be obtained by employing a Monte Carlo
simulation. This method often provides an approximate solution
when a deterministic solution is not possible by employing techniques
of random sampling from the distributions of variables.
Monte Carlo simulation can perhaps best be explained by the
case in which all variables are assumed to be independent of each
other. The steps are as follows:
1. Determine a probability distribution for each variable (see
Figure 7.1).
2. Transform any continuous distributions into discrete distributions, with each discrete interval representing 1 percent (or
0.1 percent or some other convenient interval) of the distribution.
3. Determine the midpoint of each interval in each discrete distribution.
4. Assign a number from 1 to n (where n represents the number of
intervals into which each distribution was divided) to each interval. For example, if a distribution were divided into 100 intervals,
the ﬁrst percentile would be assigned the number 1, the second
would be assigned 2, and the hundredth, 100.
5. The distribution of returns should also be divided into intervals (say, whole percentages) and counters deﬁned (for example,
0.5 percent ≤i1
< 1.5 percent; 1.5 percent ≤i2 < 2.5
percent, and so on) which are initialized at zero (that is i1 =
i2 = . . . in = 0).
6. Generate from the computer, or select from a table, a two-digit
(if fewer than 101 intervals are employed) random number for
the ﬁrst independent distribution.
7. Determine the interval on the distribution that was assigned
a number corresponding to the random number generated and
select the midpoint.
8. Repeat steps 6 and 7 for the remaining distributions such that
there is one observation for each variable.
--- page 328 ---

Analysis of Common Stocks
305
9. Compute the rate of return for this set of observations. For
the example given, this would require inputting the simulated
variables to the formula:
P0 =
6

t=1
Dt
(1 + i)t +
P6
(1 + i)6 ,
and solving for i.
10. The i computed in step 9 would then be assigned to the
appropriate interval in the return distribution and the counter
for that interval would be incremented by one. For example, if
the ﬁrst computation yielded an i = 5.7 percent, then i6 would be
incremented and, at the end of the ﬁrst iteration, i1−5 = i7−n = 0
and i6 = 1.
11. Repeat steps 6–10 a large number of (N) times in order to
generate a frequency distribution of i’s.
12. Each counter can then be normalized to provide a distribution
[for example, i1/N = P(i | .5 percent ≤i < 1.5 percent)].
13. From this distribution, µi, σi, or any other desired statistic may
be computed. The larger N is, the better will be the resulting
estimate (as in any random sampling situation).
Dependent relationships among variables may also be simulated.
If two variables are perfectly correlated (positively or negatively)
with each other, the distributions may simply be combined and
simulated as one variable; the same result is obtained if the same
random number is used for both distributions on each iteration.
Growth-rate equations for the levered ﬁrm
Here we further develop Equation (7.20). If a ﬁrm had debt as
well as equity in its structure according to some optimal (or at
least constant) combination, asset growth would result from earnings
retention (and possibly stock sales, which we shall ignore) and bond
ﬂotations. Thus, asset growth would be dependent upon b (the
retention rate) and the relationship between debt (B) and equity
(S). We shall assume that earning assets (A) equal debt plus equity,
--- page 329 ---

306
Quantitative Financial Analytics
that is,
A = B + S.
(7.26)
If the ﬁrm earns r on its asset base, then EBIT would be:
EBIT = rA.
(7.27)
From EBIT, interest c is paid to bondholders, leaving for common
shareholders before taxes:
Eb = EBIT −cB.
(7.28)
After-tax earnings are given by:
E = (1 −t)(EBIT −cB).
(7.29)
If dividends (D) are paid to shareholders, E −D is left to the ﬁrm
for reinvestment in assets.
Now, we know that asset growth is:
∆A = ∆B + ∆S.
(7.30)
Furthermore, retaining earnings will increase S such that:
∆S = E −D.
(7.31)
If there is an optimal relationship (L) between the ﬁrm’s debt and
equity,
∆B = L∆S.
(7.32)
We wish to know by how much earnings (E) will grow if
earnings are retained and bonds are sold to maintain an optimal
B/S combination. Let the growth rate in earnings be:
g = ∆E/E.
(7.33)
We have established the relationship between E and EBIT, thus:
∆E = (1 −t)(∆EBIT −c∆B).
(7.34)
Furthermore, we know from 7.27 that EBIT is simply the return on
assets times the asset base. Extra EBIT resulting from expanding
--- page 330 ---

Analysis of Common Stocks
307
the asset base would thus be:
∆EBIT = r∆A.
(7.35)
Now, if we substitute (7.34) into (7.33), we ﬁnd:
∆E = [(1 −t)][(r∆A) −(c∆B)].
(7.36)
We know ∆A from 7.30. Thus, by substituting that equation into
7.36, we ﬁnd:
∆E = [(1 −t)][r(∆B + ∆S) −c∆B].
(7.37)
This equation may be expanded,
∆E = [(1 −t)][r∆B + r∆S −c∆B].
(7.38)
Rewriting,
∆E = [(1 −t)][r∆B −c∆B + r∆S].
(7.39)
Factoring within the second term of the right-hand member of the
expression, we ﬁnd:
∆E = [(1 −t)][(r −c)(∆B) + (r∆S)].
(7.40)
We know ∆B from Equation (7.32) and ∆S from 7.30. Substituting these equations into 7.40, we ﬁnd:
∆E = [(1 −t)][(r −c)L(E −D) + (E −D)].
(7.41)
Factoring within the second term of the right-hand member of the
expression once again, we ﬁnd:
∆E = [(1 −t)][(E −D)][(r −c)L + r].
(7.42)
Thus, the growth rate (Equation (7.33)) would be:
g = ∆E/E = [(1 −t)][(E −D)][L(r −c) + r]
E
,
(7.43)
which may also be written as:
g = [(1 −t)]

1 −D
E

[L(r −c) + r].
(7.44)
--- page 331 ---

308
Quantitative Financial Analytics
Because b equals (1 −D/E), we can simplify to produce:
g = [(1 −t)(b)][L(r −c) + r],
(7.45)
which is also Equation (7.20) in the text.
Common stocks: Further considerations
Throughout the previous discussion of common stock returns, the
focus was on the dividend paying ability of the equity and its possible
price appreciation. Under very special circumstances, however, the
analyst may wish to consider assets as well as earnings in computing
the yield equation. There are instances in which a substantial volume
of assets may not produce a large future earnings stream. If it is
possible that these assets will be transformed into another form of
higher yielding asset, or if it is conceivable that the assets will be
distributed to stockholders, then the value of such assets should be
assessed.
Firms that maintain large cash balances or that hold substantial
amounts of liquid securities will often show a poor earnings record.
If it appears possible that the liquidity of these ﬁrms will be reduced
through the purchase of earning assets, the analyst should take
this into account in projecting the future earnings stream for the
ﬁrm. Also, if it is possible that the ﬁrm will pay a liquidating (or
partially liquidating) cash dividend to shareholders, the amount of
this distribution should be included in the analyst’s yield equation.
If a ﬁrm maintains its liquidity at the expense of earning assets and
it appears that none of this surplus liquidity will be distributed to
shareholders, the analyst should not consider the extra liquidity in
evaluation except to the extent that substantial liquidity may reduce
the riskiness of the ﬁrm. Note that high levels of liquidity frequently
prompt tender oﬀers to purchase controlling interest in the ﬁrm. The
eﬀect of these oﬀers is usually to increase the price of the company’s
shares. If the probability of a tender oﬀer looms signiﬁcant, the
analyst should attempt to quantify its expected value.
Financial companies (banks, insurance companies, and so on)
frequently hold large volumes of liquid assets (cash, marketable
--- page 332 ---

Analysis of Common Stocks
309
securities). On occasion, a ﬁnancial company will have a poor
earnings record for this reason. Such ﬁrms oﬀer an opportunity
for an imaginative management to increase the ﬁrm’s return on
investment by reducing liquidity (switching from cash into mortgages
or even consumer loans). When the analyst believes there is a strong
chance for such a policy change, he should attempt to quantify the
possible results. This is a very diﬃcult task, and it sometimes requires
assumptions about management behavior that are always diﬃcult
to make. Nevertheless, the analyst who can shrewdly make such
judgments is often rewarded highly.
Certain non-ﬁnancial concerns will have book values that exceed
the market price of the ﬁrm’s shares. Such ﬁrms rarely oﬀer good
investment returns to investors because their asset holdings are
generally worth much less than the stated book values. Historically,
American railroads sold at large discounts from book value. They
did so because the earning power of their asset holdings was low.
Furthermore, the possibility of converting into more proﬁtable assets
(or liquidating) was very small because of regulatory constraints.
As the railroads consolidated into a few large concerns and as
they were basically deregulated, they became very proﬁtable. The
surviving roads (especially Union Paciﬁc and BNSF) have produced
excellent returns for investors. Indeed, Warren Buﬀett’s Berkshire
Hathaway bought the BNSF because its asset values were converted
to substantial earning power.
Manufacturing concerns that have substantial assets that produce little cash ﬂow frequently cannot liquidate these assets, except
at distress prices. Hence, for all practical purposes, their asset
“values” have no real signiﬁcance. An exception is the ﬁrm that
generates a large cash ﬂow but that shows negligible net income
(perhaps due to substantial depreciation charges). Such a ﬁrm can
use its cash ﬂow to reinvest in more proﬁtable ventures, or it can
pay out partial liquidating dividends to shareholders. If it is likely
that either of these events will transpire, the analyst should include
the possibility in his appraisal. Firms that do not have a large cash
ﬂow but do have large working capital positions (particularly cash)
may also have the option of converting into higher yielding assets
--- page 333 ---

310
Quantitative Financial Analytics
or paying a liquidating dividend. It usually requires a change in
management for this to occur, however.
Example
1. An analyst has projected the EPS stream for the Leafy Tobacco
Co. for the next ﬁve years:
2015
$0.30
2016
0.28
2017
0.26
2018
0.28
2019
0.30
The ﬁrm pays a $0.24 dividend per year and has done so for
10 years. The stock now sells for $3 per share, and the current
P/E multiple is expected to be maintained in the future. The
yield from purchasing Leafy shares for a ﬁve-year holding period
would be, at 8 percent,
(3.99)($0.24) + (0.681)($3) = $3.00.
2. Leafy (above) has a book value of $5 per share and a net cash
value (cash minus all liabilities) of $1.50 per share. The analyst
feels that Leafy could pay out a partial liquidating dividend, but
management shows no disposition toward this idea. Furthermore,
there appears to be no chance that a new management team will
take over in the near future. More likely, current management has
shown some interest in diversifying into the manufacture of candy
where it is felt that a return of at least 10 percent could be earned
(net). Suppose the diversiﬁcation took place in two years and the
current net cash value per share were invested. Reprojected EPS
would be:
(0.10)($1.50) = $0.15
--- page 334 ---

Analysis of Common Stocks
311
2015
$0.30
2016
0.28
2017
0.41
2018
0.43
2019
0.45
3. The analyst believes Leafy would increase its dividend to $0.30 per
share in 2018 if the diversiﬁcation plan were accepted. Furthermore, he believes the market would value Leafy at 12Xearnings
in 2019 if the ﬁrm diversiﬁed. Projected dividends and the 2019
market price given these assumptions would be:
DPS
Market Price
2015
$0.30
2016
0.28
2017
0.26
2018
0.28
2019
0.30
(12) ($0.45) = $5.40
4. The return earned on Leafy stock if the diversiﬁcation plan were
adopted and the analyst’s assumptions proved to be correct would
be, at 20 percent:
(0.833) ($0.24) = $0.20
(0.694) (0.24) =
0.17
(0.579) (0.24) =
0.14
The return would be just
(0.482) (0.30) =
0.14
under 20 percent.
(0.402) (0.30) =
0.12
(0.402) (5.40) =
2.17
$2.94
--- page 335 ---

312
Quantitative Financial Analytics
5. The analyst believes the probability that the ﬁrm will diversify is
0.2. The expected return and the standard deviation of the two
possible outcomes would be:
(0.8) (8.0) = 6.4
8.0 −10.4 = (−2.4)2 = 5.76(0.8) = 4.61
(0.2) (20.0) = 4.0
20.0 −10.4 = (9.6)2 = 92.16(0.2) = 18.43
10.4
23.04
µ = 10.4%
σ =
√
23.04 = 4.8%.
Stock Prices and the Issuance of New Shares
The dynamic aspects of common stock analysis pose some of the more
perilous problems for the analyst. This is particularly true because
many analysts think in static terms and ﬁnd it hard to cope with
the secondary and tertiary eﬀects of a change in a variable. Perhaps
the greatest confusion is evidenced over the subject of issuing new
shares. When a ﬁrm goes to the market to sell additional shares,
the obvious short-run consequence is a reduction of current earnings
per share. Dilution is the term applied to this phenomenon, and
many analysts feel that the eﬀect of issuing new shares (and the
subsequent dilution) will depress share prices. Thus, if XYZ has
1 million shares outstanding selling at $20 per share and it sells
another 100,000 shares, one might suppose that the price per share
would fall (see Figure 7.1). Suppose XYZ earned $1.00 per share
($1 million). If another 100,000 shares were issued, the adjusted EPS
would be:
1, 000, 000/1, 100, 000 = $0.91.
If a multiple of 20X were applied to the adjusted earnings, a price of
(20) (0.91) = $18.20 would prevail. Thus, the shift in the XYZ share
supply curve from S to S′ would tend to depress the stock’s price.
Of course, only part of the story has been told. It is usually the
case that the secondary eﬀects of selling new shares are very positive,
and the real position of the ﬁrm may improve rather than deteriorate
--- page 336 ---

Analysis of Common Stocks
313
as a result of the issue. The sale of new shares may allow the ﬁrm to
raise needed capital to expand facilities, improve sales, and increase
long-run proﬁts. If long-run EPS increase by an amount larger than
the short-run dilution produced by the creation of new shares, the
price of the ﬁrm’s stock should rise rather than fall. Suppose XYZ
earnings increased to a long-run EPS of $1.05 as a result of the new
share issue. It might be expected here that demanders would begin
bidding up share prices given these improved expectations.
In fact, if the multiplier of 20X held, we might expect the stock
price to rise to: (20) ($1.05) = $21. This would be aﬀected by a
shift in the demand curve from D to D′ (see Figure 7.1). Although it
cannot be argued that every new issue of shares will produce increases
in long-run earnings suﬃcient to oﬀset the dilution eﬀect, one should
not merely assume that a new issue will depress prices. Rather, one
should attempt to assess the long-run impact on earnings resulting
from raising new capital.
S
S’
D
D’
SHARES OUT STANDING
PRICE PER SHARE
21.00
20.00
18.20
1,000,000
1,100,000
XYZ Co.
Figure 7.1. Price Eﬀect of New Share Issue
--- page 337 ---

314
Quantitative Financial Analytics
Example
Cameo, Ltd. has 10 million shares outstanding. An analyst has
forecasted revenues, EPS, and DPs for the next four years under
the assumption that the ﬁrm’s asset investment will grow only by
the amount of earnings retained. His projections are given below:
Year
Revenue
Total Expenses
EPS
DPS
(000)
(000)
2015
$100,000
$80,000
$2.00
$1.00
2016
120,000
90,000
3.00
1.50
2017
150,000
105,000
4.50
2.00
2018
200,000
130,000
7.00
3.00
The ﬁrm has an asset investment of $50 million in 2015. Retained
earnings for 2015 are projected at $10 million. Thus, the asset
investment for 2016 is forecasted at $60 million. Retained earnings
for 2016 are expected to be $15 million. The asset investment for 2017
is thus projected to be $75 million. Retained earnings are projected
at $25 million for 2017. The asset investment for 2018 is forecasted
to be $100 million. Notice that the analyst is assuming a constant
asset turnover for each year:
Year
Revenue
Total Assets
Turnover
(000)
(000)
2015
$100,000
$50,000
2X
2016
120,000
60,000
2X
2017
150,000
75,000
2X
2018
200,000
100,000
2X
He is also using the following net income equation:
Net income = sales −(30, 000, 000 + 0.5 sales).
--- page 338 ---

Analysis of Common Stocks
315
Now, suppose Cameo sells at $105 per share. The analyst believes
the current P/E multiple is high but justiﬁable in light of the earnings
pattern predicted for 2015–2018. He does not feel the expected
growth rate beyond 2018 will match the 50 percent compounded
annual rate of earnings-per-share growth forecasted for 2015–2018,
however. Thus, he expects the multiple to fall to about 20 times
earnings in 2018. Given the analyst’s expectations, the stock would
yield: At 9 percent,
(0.917)(1.00) + (0.842)(1.50) + (0.772)(2.00)
+ (0.708)(3.00) + (0.70)(140.00) = $104.96.
Cameo has announced an oﬀering of 500,000 new shares to
current stockholders at $100 per share. The dilution of projected
EPS resulting from the oﬀering would be:
EPS
2015
20,000,000/10,500,000 =
$1.90
2016
30,000,000/10,500,000 =
2.86
2017
45,000,000/10,500,000 =
4.28
2018
70,000,000/10,500,000 =
6.67
Cameo plans to expand immediately with the $50 million it has
raised. The analyst feels that the ﬁrm will have excess capacity for a
while. He projects an asset turnover of 1.8X in 2015 and 2016, 1.9X
in 2017, and 2.0X in 2018. His new net income equation is:
Net income = sales −(60, 000, 000 + 0.5 sales).
Re-projected total assets, revenues, total expenses, EPS and DPS
for Cameo over 2015–2018 assuming dividends are about one-half
--- page 339 ---

316
Quantitative Financial Analytics
earnings would be:
Total Assets
Revenues
Expenses
Year
(000)
(000)
(000)
EPS
DPS
2015
$100,000
$180,000
$150,000
$2.86
$1.43
2016
115,000
207,000
163,500
4.14
2.12
2016
136,750
259,825
189,913
6.66
3.33
2018
171,706
343,412
231,706
10.64
5.32
Suppose the market felt that the risk oﬀered by investing in
Cameo had not changed and that 9 percent was still an adequate
return from the security. What price should the stock advance to at
the time of the new oﬀering, given the above forecast?
(0.917)(1.43) + (0.843)(2.12) + (0.772)(3.33) + (0.708)(5.32)
+ (0.708)(212.80) = $160.10.
Thus, rather than declining, Cameo stock should in fact rise as a
result of the new share oﬀering.
Another area that presents problems for many analysts is the
evaluation of common stock dividends and stock splits. The payment
of a stock dividend is merely a method by which the ﬁrm “capitalizes”
retained earnings into the permanent capital accounts (common
stock, and common stock excess over par). For some ﬁrms, such as
commercial banks, the transfer of retained earnings into permanent
capital may be required by law. For most ﬁrms, however, the payment
of a stock dividend is simply a way of distributing more shares to
the existing stockholders. No real economic change occurs from the
distribution. The net worth of the ﬁrm does not alter, and shareholders maintain the same percentage ownership in the ﬁrm after
the declaration of a stock dividend that they had before it. The only
real diﬀerence is that shareholders have a greater number of shares,
which, of course, should be worth proportionately less per share.
Although there is no economic reason for most ﬁrms to pay
stock dividends, many do pay them. Some managements believe they
--- page 340 ---

Analysis of Common Stocks
317
can fool shareholders by paying out stock rather than cash. Others
contend that investors in high tax brackets prefer stock dividends
to cash dividends because the extra stock accruing from a stock
dividend may be sold if funds are needed. Nevertheless, it would
not be necessary that a stock dividend be paid for the investor to
obtain funds. He could simply sell some of his original holding of
shares. Even if the stock had appreciated in value since his purchase,
he would be equally well oﬀby selling a percentage of his original
holding as by receiving an equivalent percentage as a stock dividend
which he would liquidate.
Splitting a ﬁrm’s stock is similar to a stock dividend in that the
real economic position of the investor does not change. He has more
pieces of paper, but his percentage ownership in the ﬁrm is the same.
The stock split does have an accounting eﬀect in that the par value
of the stock is reduced by the inverse of the split (a 2:1 split reduces
the par value by one half), but this change is not terribly important.
Par value has absolutely no meaning in terms of stock price value
(except when a ﬁrm issues shares below their par value), and many
companies no longer assign par values to their stock.
Three arguments are made to justify splits economically. The
ﬁrst is that splits are an omen of growth (or at least a “signal”
that the ﬁrm’s board of directors expects such). The second is that
cash dividends may increase after a split. The third is that investors
prefer shares selling in some optimal price range (usually $20 to
$80). The ﬁrst argument is without merit because the rate of sales
and earnings growth will be the same regardless of the number of
shares the ﬁrm has outstanding. Only the sale of new shares, which
brings in added capital for investment, can aﬀect sales and earnings
growth. The second argument is behaviorally correct in that many
ﬁrms do increase their dividend payout after a split. Nevertheless, an
increase in payout can be accomplished without a split. Furthermore,
if the ﬁrm is growing rapidly, a better policy would be to reduce
the payout and reinvest in proﬁtable projects. This might positively
aﬀect the well-being of shareholders more than the payment of a cash
dividend! The third argument is the only real justiﬁcation for a split.
If investors really do prefer stocks selling in some given range, when a
--- page 341 ---

318
Quantitative Financial Analytics
stock price advances out of that range it should be split. It is hard to
imagine, however, that many investors would rather have 100 shares
at $50 per share than 10 shares at $500. The investment is $5,000
regardless. Many of today’s popular growth issues such as Google,
Apple, Netﬂix, Baidu, and Berkshire Hathaway, trade at prices well
over $100 per share, and the brokerage commission may be actually
less for the same dollar investment in higher-priced shares than lowerpriced ones. Of course, at very high prices (one share at $5,000, for
example), share divisibility becomes impossible, and some investors
are priced out of the market. There is little argument that shares
selling at these prices should be split, unless management wishes to
keep the shares out of the hands of small investors. The latter policy
will undoubtedly produce a lower total market value for the ﬁrm.
Although the accounting and economic eﬀects of the stock split
are of questionable signiﬁcance, many analysts and investors alike
greet the news of a pending split enthusiastically. Of course, this
fact in itself may justify the decision of a ﬁrm to split its shares by
producing a self-fulﬁlling prophecy. Nevertheless, the only real eﬀect
of a split is the creation of more shares, which should sell at lower
prices. It seems obvious that an investor who owns 100 shares of a
stock selling at $10 per share, earning $1, and paying $0.50 in cash
dividends would be no better oﬀowning 200 shares of the same stock
selling at $5 per share, earning $0.50, and paying $0.25 in dividends.
Example
1. A ﬁrm has the following capital structure:
Common stock ($10 par, one million shares)
$10,000,000
Common stock, excess over par
20,000,000
Retained earnings
70,000,000
$100, 000, 000
The ﬁrm declares a 10 percent stock dividend. For stock dividends
less than 20–25 percent, market price rather than book value is
used to determine the recapitalization. The ﬁrm’s market price
is $150 per share. The transfer of the dividend from retained
--- page 342 ---

Analysis of Common Stocks
319
earnings into permanent capital is thus:
(0.10)(150,000,000) = $15,000,000.
The new structure would be:
Common stock ($10 par, 1.1 million shares)
$11,000,000
Common stock, excess over par
34,000,000
Retained earnings
55,000,000
$100,000,000
2. Suppose the ﬁrm above declared a 3:1 split. The capital structure
would become:
Common stock ($3.33 1/3 par, 3 million shares)
$10,000,000
Common stock, excess over par
20,000,000
Retained earnings
70,000,000
$100,000,000
Financial Analysis and Accounting Data
In this section, we issue a caveat to the analyst about the data that he
has at his disposal for analysis. The historical numbers that he uses
to prepare ratios and forecasting equations are generally based on
ﬁgures that have been taken from the published ﬁnancial statements
of the ﬁrm being analyzed. Although these statements may have been
prepared “according to generally accepted accounting principles,”
there may be signiﬁcant variation in the real economic meaning
of ﬁnancial reports. Obvious inconsistencies in the methodology
of preparation (for example, when a ﬁrm switches from LIFO
to FIFO inventory valuation, or from accelerated depreciation to
straight-line) require adjustments to the documents prepared by the
accounting community (see Chapter 4). More subtle problems may
exist, however, which cannot easily be handled by making simple
adjustments.
One of the more plaguing diﬃculties with ﬁnancial statements is
that they are prepared on the assumption of stable prices. To the
extent that prices change over time, the reported asset values on the
ﬁrm’s balance sheet (and perhaps the liability values as well) will be
--- page 343 ---

320
Quantitative Financial Analytics
inaccurate. Further, because accounting costs are usually based on
historical prices, a misstatement about the value of an asset may well
result in an inaccurate depiction of net income. Moreover, net income
in one period may not be equivalent to an identical net income in
another if the aggregate level of prices has changed. If a ﬁrm earns
$1.00 per share in 2014 and $1.05 in 2015, it really has shown no
improvement if the overall price level has also risen by 5 percent.
Another problem is that the market values of a ﬁrm’s assets
may have no relationship to their book values. Price-level changes,
variances from depreciation estimates, and the insistence of accountants upon valuing assets at the lower of cost or market (an
example of the doctrine of “conservatism”) make the balance sheet
an unreliable statement about the value of the enterprise. Of course,
the accountants themselves beg oﬀ, claiming that ﬁnancial analysts
expect too much from published statements. One respected former
practitioner (Howard Ross, see references) has observed:
“. . . accountants in their most solemn pronouncements have made it
quite clear that the ﬁnancial statements they prepare do not even
purport to provide information about solvency and proﬁtability.
For instance, anyone might be pardoned for thinking that a conventional balance sheet is prepared to show the ﬁnancial strength
of a company by listing its obligations against its resources and to
establish its net value. But this not at all how a balance sheet is
deﬁned in accounting texts” (p. 9).
Thus, when the analyst ﬁnds that return on total investment has
increased from 20 percent to 21 percent, it is not clear that an
improvement has taken place. Earnings ﬁgures from one year to the
next (and across ﬁrms for any given year) are not strictly comparable,
and total investment can become completely incomparable over time.
What is the unfortunate analyst to do under such circumstances?
The answer, of course, is to make the best of the situation.
Adjustments to published statements should be made whenever there
is good justiﬁcation to do so. Otherwise, the analyst should always
bear in mind the limitations of the data that are being used in
making an appraisal. A report based on less-than-perfect data is
better than no report at all. Security analysis has always been a
