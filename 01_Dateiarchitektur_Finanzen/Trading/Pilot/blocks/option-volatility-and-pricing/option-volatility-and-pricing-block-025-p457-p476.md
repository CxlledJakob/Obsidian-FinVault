# Option Volatility and Pricing_ Advanced Trading Strategies -- Sheldon Natenberg -- 2nd ed, 2014 -- McGraw Hill Professional -- isbn13 9780071818773 -- 6a48d008bd9beef283debf7bad0b2e4a -- Anna’s Archive.pdf — pages 457–476

--- page 457 ---

440
O P T I O N V O L AT I L I T Y A N D P R I C I N G
Underlying contract:
Unchanged (100 shares)
New delta position:
Old delta position × Y/X
New gamma position:
Old gamma position × (X/Y)2
These calculations hold true as long as the split is Y for 1, where Y is a whole
number (e.g., 2 for 1, 3 for 1, 4 for 1, etc.). If Y is not a whole number, the number of shares in the underlying contract may have to be adjusted. For example,
using our stock price of 60, what will happen if the stock is split 3 for 2? Now Y is
not a whole number because the split is equivalent to 1½ to 1. If we own a May
60 call, we can make the following calculations:
New stock price

60 × 2/3 = 40
New exercise price
60 × 2/3 = 40
New option position
+1 × 3/2 = +1½ May 40 calls
Underlying contract
Unchanged (100 shares)
New delta position
+50 × 3/2 = 75
New gamma position
+5 × (3/2)2 = +11.25
The problem here is that the clearinghouse does not allow fractional
option positions (+1½ May 40 calls). In order to eliminate the fraction, the
clearinghouse will replace each May 60 call before the split with one May
40 call after the split. At the same time, the underlying contract will be adjusted
so that the new underlying contract is equal to the old underlying contract
multiplied by the split ratio
100 shares × 3/2 = 150 shares
Using these adjustments, the delta and gamma now make sense. The option
is at the money, so it should be equivalent to approximately 50 percent of the
underlying contract, or 75 shares. If the stock price rises to 41, equal to a price
of 61½ before the split, the old delta would have been
50 + (1.5 × 5) = 57.5
The option would have been equivalent to 57.5 percent of the underlying contract. Therefore, the new option (the 40 call) should be equivalent to
0.575 – 150 shares = 86.25 shares
As expected, this is the same as the delta (75) plus the gamma (11.25).
What happens to the other risk measures—theta, vega, and rho—if a
stock splits? These numbers remain unchanged. The passage of time, changes
in volatility, and changes in interest rates have the same effect on a position
after a split as before a split. Only the delta and gamma must be adjusted.
Indeed, assuming that all other conditions remain unchanged, a stock split has
no real effect on a trader’s position. It simply results in an accounting change in
such a way that equity is maintained. Of course, all other conditions may not
--- page 458 ---

P o s i t i o n A n a ly s i s 	 441
remain unchanged. When a stock splits, we might assume that the dividend
also will be split proportionally. But this is not necessarily the case. A stock split
often indicates that a company is doing well, and it is not unusual for the split
to be accompanied by an increase in the dividend. Any change in the expected
dividend will change the value of an option position. Figure 21-21 shows the
characteristics of our original position after a 2-for-1 stock split with no change
in the expected dividend.
Figure 21-21  The effect of a 2-for-1 stock split.
Underlying share price = 34.38
Interest rate = 4.95%
Expected dividend = 0.29 in 10 weeks
Time to April expiration = 4 weeks
April implied volatility = 34.27%
Time to June expiration = 13 weeks
 June implied volatility = 32.95%
Time to August expiration = 21 weeks
August implied volatility = 31.64%
April
June
August
Exercise
Price
Calls
Puts
Calls
Puts
Calls
Puts
27½
154
+94
–206
+64
30
–324
+222
+6
162
+48
–92
32½
+26
–154
+184
–50
35
+212
–38
–220
–98
–52
–40
37½
–16
+122
+172
–4
+16
–50
40
–62
–36
+42
+60
42½
 –270
+92
–50
+14
 –144
Calls
Puts
Delta
Gamma
Theta
Adjusted
Vega
Rho
April
–280
+424
–25,230
+2,016
–2.51
+6.26
–7.50
June
+134
–182
+12,186
+52
–0.62
+0.36
+9.75
August
–72
–118
+6,850
–1,008
+1.25
–11.19
+10.45
Shares
+6,600
+6,600
Totals
+406
+1,060
–1.88
–4.57
+12.70
--- page 459 ---

442
Stock Index Futures
and Options
Because stock index futures and options are among the most actively traded
of all derivatives, it will be worthwhile to take a closer look at these contracts.
Even though the focus of this book is primarily options, stock index futures and
options are so closely related, and so many strategies involve both contracts,
that it is almost impossible to discuss one without discussing the other. We will
therefore include both instruments in our discussion.
What Is an Index?
An index is a number that represents the composite value of a group of items.
In the case of a stock index, the value of the index is determined by the market prices of the stocks that make up the index. As the stocks in the index rise
in price, the value of the index rises; as the stocks fall in price, the value of the
index falls. If some stocks in the index rise while others fall, the offsetting
changes in stock prices may result in the index itself remaining unchanged,
even though the price of every stock in the index may have changed. Although
the index is made up of individual stocks, the value of the index always reflects
the total value of the stocks that make up the index.
Stock indexes are often classified as being either broad based or narrow based.
A broad-based index is usually made up of a large number of stocks and is
intended to represent the value of the market as a whole or at least a large portion of the market. Below are some widely followed broad-based indexes.
Index
Country or Region
Number of Stocks in the Index
S&P 500
United States
   500
Nasdaq 100
United States
   100
Russell 2000
United States
2,000
22
(continued)
--- page 460 ---

S t o c k I n d e x F u t u r e s a n d   O p t i o n s 	 443
Index
Country or Region
Number of Stocks in the Index
FTSE 100
United Kingdom
   100
Nikkei 225
Japan
   225
ASX 200
Australia
   200
KOSPI 200
South Korea
   200
BOVESPA
Brazil
     67
TSE
Canada
     60
MSCI EAFE
Australia, Europe, and Far East
1,500
CSI 300
China
   300
The designation of an index as broad based can be somewhat subjective.
Even if an index is composed of a smaller number of stocks, it may still be considered broad based if the companies that make up the index represent a wide
cross section of the economy in a country or region.
Index
Country or Region
Number of Stocks in the Index
Dow Jones Industrials
United States
30
DAX
Germany
30
CAC 40
France
40
Eurostoxx 50
Europe
50
OMX 30
Sweden
30
FTSE MIB
Italy
40
AEX
Netherlands
25
Hang Seng
Hong Kong
30
Sensex 30
India
30
IPC
Mexico
35
Tel Aviv 25
Israel
25
Straits Times
Singapore
30
Swiss Market
Switzerland
20
A narrow-based index is usually composed of a small number of stocks
and reflects the value of a particular market segment.
Index
Markey Segment
Number of Stocks
in the Index
Dow Jones Transportation
U.S. Transportation Companies
20
S&P Utilities
U.S. Electrical Energy Companies
31
(continued)
--- page 461 ---

444
O P T I O N V O L AT I L I T Y A N D P R I C I N G
Index
Markey Segment
Number of Stocks
in the Index
Bank Index
U.S. Banks and Financial Institutions
24
Semiconductor Index
U.S. Semiconductor Companies
30
Oil Service
U.S. Oil Service Companies
15
UK Homebuilders
U.K. Housing Construction
6
EuroStoxx Technology
European Technology Companies
16
FTSE Mining
Worldwide Mining Companies
24
Calculating an Index
There are several methods that can be used to calculate the value of a stock
index, but the most common methods focus on either the prices of the stocks in
the index or the capitalization of the companies that make up the index. To see
how these methods work, consider the ABC Index composed of the following
three stocks:
Stock
Price
Total Shares Outstanding
Market Capitalization
A
80
   100
  8,000
B
 20
2,000
 40,000
C
 50
   400
 20,000
The market capitalization of each company is equal to the stock price multiplied by the number of outstanding shares. This represents the total value of
all stock in the company.
If an index is price weighted, the value of the index is the sum of the individual stock prices
ABC Index (price weighted) = ∑ pricei = 80 + 20 + 50 = 150
If an index is capitalization weighted (cap weighted for short), the value of the index
is the sum of the individual capitalizations
ABC Index (cap weighted) = ∑ (pricei × sharesi) = 8,000 + 40,000
              + 20,000 = 68,000
Suppose that the price of Stock A rises 10 percent to 88. How will the
value of the ABC Index change if the index is price weighted? The new index
value will be
88 + 20 + 50 = 158
--- page 462 ---

S t o c k I n d e x F u t u r e s a n d   O p t i o n s 	 445
In percent terms, this is an increase of
8/150 = 5.33%
We can make the same calculation for the price-weighted index if Stock B rises
10 percent to 22 or if Stock C rises 10 percent to 55. The percent increases in
the index are
Stock B: 2/150 = 1.33%
Stock C: 5/150 = 3.33%
In percent terms, changes in the highest-priced stock, Stock A, have the greatest effect on the value of the index. Stock A has the greatest index weighting—
it accounts for the largest portion of the index. We can calculate the role that
each stock plays in the index by calculating the individual weightings:
Stock A: 	 80/150 = 53.33%
Stock B:
20/150 = 13.33%
Stock C: 	 50/150 = 33.33%
We can also calculate the weightings for each stock (with small rounding
errors) if the ABC Index is capitalization weighted:
Stock A: 	 8,000/68,000 = 11.76%
Stock B:
40,000/68,000 = 58.82%
Stock C: 	 20,000/68,000 = 29.41%
Now Stock B, the stock with the greatest capitalization, has the greatest index
weighting.
In a price-weighted index, stocks with the highest price have the greatest
index weighting. In a capitalization-weighted index, stocks with the greatest
capitalization (stocks with a large number of outstanding shares) have the greatest weighting.
We can also create an equal-weighted index where, in percent terms, each
stock plays exactly the same role in the index. We can do this by making the initial contribution of each stock to the index identical. For example, suppose that
initially the value of our index is
∑ (pricei/pricei) = 1 + 1 + 1 = 3
Here each stock contributes exactly 33.33 percent to the index. Of course, if
we always divide each stock by itself, the value of the index will never change.
But this is only the value when the index is first introduced. Subsequently, as the
price of each stock changes, the new price is divided by the old price to determine the new value of the index. If any one stock in the index rises 10 percent,
the effect on the index will be the same because
88/80 = 22/20 = 55/50
If all three stocks rise 10 percent, the new value of the index will be
88/80 + 22/20 + 55/50 = 1.10 + 1.10 + 1.10 = 3.30
--- page 463 ---

446
O P T I O N V O L AT I L I T Y A N D P R I C I N G
The index will rise exactly 10 percent.1
As time passes and some stocks in an equal-weighted index outperform
other stocks, the weighting of the stocks will change so that the index will
no longer be equal weighted. In order to ensure that each stock in the index
accounts for approximately the same value, equal-weighted indexes are periodically rebalanced.
Suppose that at a later date the prices of Stocks A, B, and C are 76, 25, and
51, respectively. The value of the equal-weighted index now will be
76/80 + 25/20 + 51/50 = 0.95 + 1.25 + 1.02 = 3.22
Stock B now accounts for a greater portion of the index than either Stock A or
Stock C. To ensure that all stocks again have an equal weighting, the index is
now rebalanced
76/76 + 25/25 + 51/51 = 3.00
Of course, the index value of 3.00 seems inconsistent with the preceding index
value of 3.22. In order to generate a continuous index value, the index value
after the rebalancing must be multiplied by the percent increase in the index
during the previous rebalancing period. In our example, the index after the
rebalancing, we must multiply the index value by
3.22/3.00 = 1.0733
because the index rose by 7.33 percent over the last rebalancing period.
It is a relatively easy task to add up a list of individual stock prices. Consequently, the earliest indexes were price weighted. The Dow Jones Industrial
Average, introduced in 1896, is probably the best known of all price-weighted
indexes. However, a capitalization-weighted index gives a more accurate picture of each company’s value. With the advent of computer technology to
make the calculations, most widely followed indexes are now capitalization
weighted.
The total capitalization of a company depends on the number of outstanding shares in the company. However, company restrictions may prevent
some of these shares from being available for trading. Shares held in the company treasury, by company officers, or in employee investment plans may not
be available to the public. The shares that are available for trading are referred
to as the free float, and it is the number of shares in the free float that typically is
used to calculate the value of a capitalization-weighted index.
1 A less common variation on an equal-weighted index involves weighting the stocks geometrically rather than
arithmetically. The value of a geometric-weighted index made up of n stocks is the nth root of the product of the
price ratios. If our ABC Index is geometric weighted, the initial index value will be
(80/80 × 20/20 × 50/50)1/3 = 1.00
As the prices of the component stocks change, the value of the index will be
[Π(today’s pricei/yesterday’s pricei)]1/n
--- page 464 ---

S t o c k I n d e x F u t u r e s a n d   O p t i o n s 	 447
The Index Divisor
When an index is first introduced, it is common to set the value of the index
to some round number. Suppose that we initially want the value of the ABC
Index to be 100. To accomplish this, we must adjust the raw index price of either
150 (price weighted) or 68,000 (cap weighted) by using a divisor to achieve our
target value of 100. Because
Raw index value/divisor = target index value
the divisor must be
Divisor = target index value/raw index value
For our ABC Indexes, the respective divisors are
Price-weighted index:
150/100 = 1.50
Cap-weighted index:
68,000/100 = 680
Once the divisor has been determined, all subsequent index calculations
are made by dividing the raw index value by the divisor. If the price of Stock B
rises to 25, the price-weighted index value, which was initially 100, will now be
(80 + 25 + 50)/1.50 = 155/1.50 = 103.33
The capitalization of Company B will now be 25 × 2,000 = 50,000, and the
cap-weighted index value will be
(8,000 + 50,000 + 20,000)/680 = 78,000/680 = 114.71
It is sometimes necessary to adjust the divisor to ensure that the index
accurately reflects the performance of the component stocks. Consider what
will happen if Stock A, which was trading at 80, splits 2 for 1. The stock price is
now 40, but with 200 shares outstanding.
Stock
Price
Total Shares Outstanding
Market Capitalization
A
 40
   200
   8,000
B
 20
2,000
 40,000
C
 50
   400
20,000
If the ABC Index is price weighted, the index value, which was previously 100
(using our divisor of 1.50), will now be
(40 + 20 + 50)/1.50 = 110/1.50 = 73.33
But is this logical? From the point of view of an investor in Company A, the
value of his holdings has not changed, so why should the index value change?
--- page 465 ---

448
O P T I O N V O L AT I L I T Y A N D P R I C I N G
To generate a continuous and logical index value, the index divisor must be
adjusted. With a new raw index value of 110 and a target index value of 100
(assuming that no other price changes occurred), the new index divisor will be
New divisor = 110/100 = 1.10
When an index divisor is adjusted, the organization responsible for calculating
the index will typically issue a press release announcing the new divisor and the
reason for the adjustment: “The new ABC Index divisor is 1.10 as a result of
the 2 for 1 stock split of Company A.”
How will the 2 for 1 stock split affect the divisor in our cap-weighted ABC
Index? We can see that the capitalization of Stock A is unchanged at 8,000.
Therefore, no adjustment is required. The divisor is still 680.
The component stocks that make up an index are not permanent. A company may cease to exist because it has gone out of business or because it has
been taken over by another company. Or a company may no longer meet the
criteria for inclusion in an index because its price or capitalization has dropped
below some threshold. To maintain a constant number of index components, a
company that is removed from an index must be replaced with a new company.
This will require an adjustment to the divisor.
Suppose that Company C is replaced in the ABC Index with Company D,
currently trading at 75 with 500 shares outstanding:
Stock
Price
Total Shares Outstanding
Market Capitalization
A
 80
   100
   8,000
B
 20
2,000
 40,000
D
 75
   500
 37,500
The new divisors for ABC Index will be
Price-weighted index:
(80 + 20 + 75)/100 = 1.75
Cap-weighted index:
(8,000 + 40,000 + 37,500)/100 = 855
Total-Return Indexes
In a traditional stock index, when the price of a component stock falls, the price
of the index will fall. This is true even if the price decline is the result of a
dividend payout. In a total-return index, all dividends are assumed to be immediately reinvested in the index. Consequently, stock price declines resulting from
a dividend payout do not cause the index value to decline.
The value of the price-weighted ABC Index composed of our original
three stocks with a divisor of 1.50 is
(80 + 20 + 50)/1.50 = 100.00
--- page 466 ---

S t o c k I n d e x F u t u r e s a n d   O p t i o n s 	 449
If Stock A pays a dividend of 1.00 and opens at a price of 79 on the ex-dividend
day, the opening index value will be
(79 + 20 + 50)/1.50 = 99.33
But if the ABC Index is a total-return index, the opening index value will
remain at 100 because the 1.00 decline in Stock A was solely the result of the
dividend payout. To maintain an index value of 100, the index divisor must be
adjusted to 1.49 because
(79 + 20 + 50)/1.49 = 100.00
Whenever a component stock in a total-return index pays a dividend, the divisor will be adjusted to reflect the dividend payout.
Although they are less common than traditional indexes, there are some
widely followed total-return indexes. The best known of these is probably the
German DAX Index. Occasionally, an index, such as the Standard and Poor’s
(S&P) 500 Index, will be published in two versions, as both a traditional index
and a total-return index. The former, however, is much more widely followed.
Impact of Individual Stock Price Changes on an Index
If an individual component stock price changes, how will this affect the value
of an index? Suppose that the current value of the price-weighted ABC Index
is I. If the price of Stock A (price A) changes by an amount a, what will be the
new value of the index? The raw value of the index should rise by a because
(A + a) + B + C = I + a
In percent terms, the change in the index is a/I. Suppose that we rewrite a/I in
a slightly different form
a/I = (a/A) × (A/I)
a/A is the percent change in the stock price, while A/I is the stock’s weighting in
the index. The percent change in the index must therefore be equal to the percent change in the stock multiplied by the stock’s weighting in the index. This is
true regardless of whether the index is price weighted, cap weighted, or equal
weighted.
We can confirm this through an example. Suppose that Stock A in the
price-weighted ABC Index, currently trading at 100 with a divisor of 1.50, rises
one point. The new index value is
(81 + 20 + 50)/1.50 = 151/1.50 = 100.67
The weighting of Stock A (before its one-point rise) was 53.33 percent, so the
percent change in the index should be
0.5333 × (1/80) = 0.5333 × 0.0125 = 0.0067
--- page 467 ---

450
O P T I O N V O L AT I L I T Y A N D P R I C I N G
From this we get a new index value of
(1 + 0.0067) × 100 = 100.67
For the cap-weighted ABC Index, currently trading at 100 with a divisor of
680, the new index value will be
[(81 × 100) + 40,000 + 20,000]/680 = 68,100/680 = 100.147
The weighting of Stock A (before its one-point rise) was 11.76 percent, so the
percent change in the index should be
0.1176 × (1/80) = 0.1176 × 0.0125 = 0.00147
From this we get a new index value of
(1 + 0.00147) × 100 = 100.147
As the price of each stock changes, the new index price is
Old index price × (1 + ∑ percent changei × weighti)
For a price-weighted index, if we know the index divisor, we can simplify
this calculation by noting that the change in the index per one-point move in
any individual component is always given by
Change in stock price/divisor
Each 1.00 change in a stock in the price-weighted ABC Index will cause the
index to change by
1.00/1.50 = 0.67
It may seem odd that every point change in a component stock has the
same effect on an index. If a component stock rises one point and then rises a
second point, the second point will cause a smaller percent increase in the stock
price. One might therefore expect the second point to have a smaller effect
on the index. But this is offset by the fact that each point increase in the stock
also increases the stock’s weighting in the index. Taken together, the percent
change in the stock and its weighting combine to yield a constant point change
in the index.
A trader can occasionally use the foregoing calculations to make a more
accurate estimate of an index’s true value. Most indexes are calculated from the
last trade price of each component stock. But the last trade price may not be an
accurate reflection of where the stock is currently trading. Suppose that trading
in an index component stock  has been temporarily halted.2 The index value
2 Trading in a stock can be halted for a variety of reasons, but it occurs most often when there is important news
pending concerning the company. By halting trading, the exchange hopes to give investors time to absorb the
new information and thereby make a better assessment of its impact on the market.
--- page 468 ---

S t o c k I n d e x F u t u r e s a n d   O p t i o n s 	 451
will be based on the last trade price of the halted stock, but this last price may
differ significantly from the expected price when trading in the stock resumes.
Suppose that the current value of an index is 1,425.50 and that the last
trade price for a component stock is 63.00. However, trading in the stock
has been halted pending news that is expected to cause the stock price to rise
significantly. Although no one knows the exact price at which the stock will
reopen, the indication (very often disseminated by the exchange) is somewhere
between 67.50 and 68.00. If the weighting of the stock in the index is 2.5 percent, an index trader might use a price of 67.75 to estimate the new index price
when the stock reopens, that is,
1,425.50 × [1 + .025 × (67.75 – 63.00)/63.00] = 1,428.19
Alternatively, the trader may have already determined that each point change
in the stock price will cause a change of 0.57 in the index value, yielding a new
index estimate of
1,425.50 + (4.75 × .57) = 1,428.21
Either estimate will enable the trader to make a more informed decision.
Volume-Weighted Average Price
The index value at the end of a trading day is usually determined by the last
price of each component stock when trading closes. But the last trade price
may not accurately reflect trading activity in the stock. Suppose that at the
close of the trading day the quoted bid-ask spread for a stock is 43.10–43.30
and that the very last trade in the stock was for 300 shares at a price of 43.30.
Suppose, however, that just prior to the last trade, 2,400 shares traded at 43.15,
and just prior to that, another 1,800 shares traded at 43.10. The last trade
of 43.30 seems to be an anomaly, and logic suggests that perhaps one of the
other prices ought to be used for the index calculation. To solve this problem,
some exchanges use a volume-weighted average price (VWAP) over a designated
period prior to closing. In our example, if the last three trades during the VWAP
period are those just given, the closing price for the stock will be
[(300 × 43.30) + (2,400 × 43.15) + (1,800 × 43.10) ]/
                     (300 + 2,400 + 1,800) = 43.14
The volume-weighted average price of 43.14 will be used to calculate the
index value.
Stock Index Futures
In theory, one can create a futures contract on a stock index in exactly the same
way that futures contracts are created on traditional commodities. At expiration, the holder of a long stock index futures position will be required to take
delivery of all the stocks that make up the index in their correct proportions.
The holder of a short position will be required to make delivery of the stocks.
--- page 469 ---

452
O P T I O N V O L AT I L I T Y A N D P R I C I N G
In fact, no stock index futures contracts are settled through the physical
delivery of the stocks that make up the index. Such a process, requiring the
delivery of the correct number of shares of many different stocks, would be
unmanageable for most clearing organizations. Moreover, settlement might
require the delivery of fractional shares of stock, which is not possible. For
these reasons, exchanges typically settle stock index futures at expiration in cash
rather than through physical delivery of the component stocks.
As with all futures, stock index futures are subject to margin and variation, with a final cash payment equal to the difference between the expiration
value of the index and the previous day’s futures settlement price. If the index
value at the moment of expiration is 462.50 and the preceding day’s settlement price for the futures contract was 461.00, the holder of a long position
will be credited with a final payment of 1.50. If the value of each index point
is $100, the long futures position will be credited with $100 × 1.50 = $150,
and the short futures position will be debited by an equal amount. Once this
final payment has been made, both parties are out of the market and unaffected
by any subsequent index movement
What should be the fair price for a stock index forward contract? In
Chapter 2, we calculated the forward price for an individual stock by adding
the interest costs to the stock price (the cost of buying now) and subtracting
the expected dividends (the benefit of buying now)
F = S × (1 + r × t) – D
The forward price for the index can be calculated using the same procedure. We
add the interest cost to the current index price and subtract the total dividends
that the index components are expected to pay prior to maturity. But unlike an
individual stock, where dividends are paid in one lump sum, the dividend payments for an index are likely to be spread out over time. An exact forward price
calculation requires us to know the amount of the dividend for each stock, the
payment date, and the weighting of the stock in the index. From this, we can
calculate the total value of all the dividends, including the interest that can be
earned on each dividend payment from the payment date to maturity of the
forward contract.
Clearly, calculation of the dividend payout and, consequently, calculation
of the forward price can be rather complex. To simplify this calculation, many
traders use an approximation by treating the dividend flow as if it were a negative interest rate
F = S × [1 + (r – d) × t]
where d is the average annualized dividend, in percent terms, for the index. If
Current index price = 100.00
Time to maturity of the forward contract = 4 months
Interest rate = 6.00 percent
Average annualized dividend payout = 2.25 percent
the three-month forward price ought to be
100.00 × [1 + (0.06 – 0.0225) × 4/12] = 100.00 × 1.0125 = 101.25
--- page 470 ---

S t o c k I n d e x F u t u r e s a n d   O p t i o n s 	 453
For long-term forward contracts, this approximation represents a reasonable tradeoff between ease of calculation and accuracy. Unfortunately, for
short-term contracts, the fact that dividend payments come in discrete bundles
that are spread out unevenly over the life of the forward contract can result in
large errors. We can see this in Figure 22-1, which shows the daily dividend
payout of the Dow Jones Industrial Index over a three-month period. The total
annualized dividend is approximately 2.75 percent, but depending on the time
to maturity of a forward contract, this value can either overstate or understate
the true dividend payout.
Suppose that a forward contract matures at the end of the three-month
dividend cycle. If a position in the forward contract is taken at the beginning of
this period, the 2.75 percent estimate of the dividend flow is a reasonably accurate reflection of the actual dividend payout. However, if the position is taken
toward the end of the three-month period, after all the dividends have been
paid, 2.75 percent is a gross overstatement; the true dividend payout is close to
0. The dotted line in Figure 22-1 shows the true dividend payout, on an annualized basis, from that point in time to maturity. If a position is taken when the
dotted line is below 2.75 percent, this estimate overstates the true dividend payout. If a position is taken when the dotted line is above 2.75 percent, this estimate understates the true dividend payout.
Index Arbitrage
In February 1982, the Kansas City Board of Trade began trading futures on
the Value Line Stock Index. This was the first exchange-traded stock index
futures contract listed in the United States. Two months later, in April 1982, the
Chicago Mercantile Exchange began trading futures on the S&P 500 Index.
Figure 22-1  Dow Jones Industrial Index daily dividend payout,  October–December 2012.
Daily dividend payout in index points
Annualized dividend payout to maturity in percent
12
10
8
6
4
2
0
4.0%
3.5%
3.0%
2.5%
2.0%
1.5%
0.0%
0.5%
1.0%
Annualized dividend
payout to maturity
(right axis)
Daily dividend payouts
(Left axis)
Total annualized dividend – 2.75%
--- page 471 ---

454
O P T I O N V O L AT I L I T Y A N D P R I C I N G
In theory, the price of a futures contract should reflect the fair value of
holding the futures contract rather than holding the stocks making up the
index. If the futures contract is not trading at fair value, a trader can execute
an arbitrage by purchasing one asset, either the basket of stocks or the futures
contract, and selling the other. If there are no other considerations, the trader
should realize a profit equal to the mispricing of the futures contract. However, this profit will only be fully realized at expiration of the futures contract,
at which time the futures contract and index value will converge. At expiration,
the value of the futures contract will automatically be settled in cash, but the
trader will have to place an order to liquidate the stock position. He will want to
do this in such a way that the prices at which the basket of stocks are traded determine the value of the index at the moment of expiration. This can be done
by placing a market-on-close order, guaranteeing that the last trade price for each
stock, which determines the final index value, will be the liquidation price for
the trader’s stock holdings.
Index arbitrage entails risks similar to any stock futures arbitrage strategy.
If the trade has not been executed at a fixed interest rate, any change in rates
represents a risk to the position. If dividends have been incorrectly estimated,
this will also affect the profitability of the strategy. Moreover, if the strategy involves selling stock short, there may be restrictions that make the strategy impractical. And even if stock can be sold short, the short interest rate may make
the strategy unprofitable. This type of strategy, where a trader buys or sells a
mispriced stock index futures contract and takes an opposing position in the
underlying stocks, is often referred to as index arbitrage. Because computers can
be programmed to calculate the fair value of a futures contract and to execute
the arbitrage when the futures contract is mispriced, such strategies are also
known as program trading.
With the advent of computer-driven trading, index arbitrage has become
an increasingly popular strategy. When a computer detects an index futures
contract that is mispriced with respect to the index itself, the computer can
send orders to either sell futures contracts and buy the component stocks (a buy
program) or buy futures contracts and sell the component stocks (a sell program).
Once the strategy has been executed, it will usually be carried to expiration, at
which time the position will be liquidated through a market-on-close order to
either buy or sell the component stocks. Initially, exchanges were able to process market-on-close orders resulting from index arbitrage strategies without
significant problems. However, as the popularity of program trading increased,
exchanges found that as the close of business approached on the last day of
trading, they were receiving ever-larger market-on-close orders. These large
orders often caused disruptions in the normal trading process, with unexpected
jumps in the prices of component stocks. For this reason, many derivative
exchanges, at the behest of the relevant stock exchanges, agreed to settle index
futures contracts at expiration based on the opening prices of the component
stocks rather than the closing prices. This eliminated a last-minute rush to buy
or sell stock and enabled stock exchanges to more easily match up buy and sell
orders.
Settlement at expiration based on opening prices rather than closing prices
is now used for most stock index futures and option contracts. This settlement
--- page 472 ---

S t o c k I n d e x F u t u r e s a n d   O p t i o n s 	 455
procedure is sometimes referred to as AM expiration. PM expiration, where the settlement value is determined by closing prices at the end of the trading day, is
still used for a small number of stock index contracts.3
Replicating an Index
Sometimes a trader will want to create a holding of stocks that exactly replicates the value of the index. He can do this by holding an amount of each stock
in the exact proportion to the stock’s weight in the index.
Returning to our ABC Index, we had the following values:
Index Weightings
Stock
Price
Outstanding
Shares
Capitalization
Price Weighted
Cap Weighted
A
80
   100
  8,000
53.33%
11.76%
B
20
2,000
40,000
13.33%
58.82%
C
50
   400
20,000
33.33%
29.41%
If a trader wants to replicate the price-weighted ABC Index, 53.33 percent of his holdings should be in Stock A, 13.33 percent in Stock B, and 33.33
percent in Stock C. If a trader wants to replicate the capitalization-weighted
ABC Index, 11.76 percent of his holdings should be in Stock A, 58.82 percent
in Stock B, and 29.41 percent in Stock C. If the trader has $100,000 to invest,
he needs to hold the following number of shares in each stock:
Stock
Price-Weighted Holdings
Capitalization-Weighted Holdings
A
53.33% × $100,000/80 ≈ 667 shares
11.76% × $100,000/80 ≈ 147 shares
B
13.33% × $100,000/20 ≈ 667 shares
58.82% × $100,000/20 ≈ 2,941 shares
C
33.33% × $100,000/50 ≈ 667 shares
29.41% × $100,000/50 ≈ 588 shares
Because the weighting of each stock in a price-weighted index is proportional to its price, we can replicate a price-weighted index by purchasing an
equal number of shares of each component stock. The same, however, is not
true for the capitalization-weighted index, where the weighting of each stock
is proportional to its total capitalization. In both cases, however, we can confirm that the proper number of shares will replicate a $100,000 investment in
the index
(667 × 80) + (667 × 20) + (667 × 50) ≈ $100,000 (price weighted)
(147 × 80) + (2,941 × 20) + (588 × 50) ≈ $100,000 (capitalization weighted)
3 Options on exchange-traded funds, which are often designed to mimic a stock index, are subject to traditional PM
expiration. The value of the option depends on closing stock prices at the end of trading on expiration day.
--- page 473 ---

456
O P T I O N V O L AT I L I T Y A N D P R I C I N G
Why might someone want to replicate an index? An investor may want to
do so in order to earn a return equal to that of the index. This is a common
method of diversifying investments. Indeed, the investor may further diversify
by replicating several indexes representing various market segments. A trader
may also want to replicate an index in order to take advantage of a mispriced
arbitrage relationship. If a stock index futures contract is theoretically overpriced, the trader may seek to sell the futures contract and purchase all the
component stocks. He will need to do so in such a way that he exactly replicates
the index futures contract.
The amount of stock that the trader will need to purchase will depend
on the size, or notional value, of the futures contract. This, in turn, will depend
on the index multiplier that the exchange has assigned to the futures contract.
Suppose that our capitalization-weighted index with a divisor of 68,000 is currently trading at 100.00 and that the exchange has assigned a multiplier of
$1,000 to each point. The notional value of the futures contract is therefore
100.00 × $1,000 = $100,000. Given this, it may seem that a trader who is able
to sell an overpriced index futures contract can offset this position by purchasing 147 shares of Stock A, 2,941 shares of Stock B, and 588 shares of Stock C.
The problem with this approach is that the trader needs to replicate the futures
contract, not the actual index. And the futures contract and index may have
different characteristics.
To understand why replicating the index will not exactly offset the futures
position, consider what will happen over the life of the futures contract while
the trader is waiting for expiration, when the futures price and index price
will converge. The prices of the stocks will surely fluctuate, resulting in either
a profit or loss to his stock position. But this profit or loss will be unrealized
because the trader must hold the position to expiration to ensure an arbitrage
profit. At the same time, the profit or loss resulting from futures contract will be
immediately realized , resulting in a variation credit or debit each day. If there
is a variation credit, the trader will earn interest; if there is a variation debit,
the trader must pay interest. In either case, the resulting interest will change the
arbitrage profit that the trader originally expected. This is another example of
settlement risk, which we discussed in Chapter 15. A position that exactly replicates the index is an imperfect hedge against the futures contract because one
side is subject to stock-type settlement, while the other side is subject to futurestype settlement. Given this, what should be the correct hedge?
Ignoring dividends, the fair value of a stock index forward contract is
F = S × (1 + r × t)
For each point increase in the index, the index futures contract should rise by
1 + r × t. If we think of the cash index as the underlying contract, we can
apply the concept of the delta to the futures contract in much the same way we
do to an option contract. The delta is the rate at which the value of a contract
will change with respect to movement in the underlying contract. If the goal is
to be delta neutral, for each futures contract we hold, we must hold an opposing cash index position equal to 1 + r × t.
The magnitude of the futures delta will depend on both the amount of
time remaining to expiration and the level of interest rates. For a long-term
--- page 474 ---

S t o c k I n d e x F u t u r e s a n d   O p t i o n s 	 457
futures contract in a high-interest-rate environment, the required holdings in
the component stocks may be considerably greater than the equivalent futures
position. As expiration approaches or in a low-interest-rate environment, the
futures and stock holdings will be almost identical. Consequently, an index
arbitrage strategy requires an adjustment to the stock position as time passes or
interest rates change.
Suppose that there are four months to expiration of our ABC Index
futures contract and that the annual interest rate is 6.00 percent. If we sell an
overpriced futures contract, we must offset this with a long stock holding of
1 + 0.06 × 4/12 = 1.02, or 2 percent greater than the holding required for an exact index replication. If a month passes so that there are now only three months
to expiration, we should reduce our stock holding to 1 + 0.06 × 3/12 = 1.015, or
1½ percent greater than the shares required for an exact index replication. The
required holdings for the capitalization-weighted ABC Index are as follows:
Stock
Shares Required to
Replicate the Index
Shares Required to Offset a
4-Month Futures Contract
Shares Required to Offset a
3-Month Futures Contract
A
   147
1.02 × 147 ≈ 150
1.015 × 147 ≈ 149
B
2,941
1.02 × 2,941 ≈ 3,000
1,015 × 2,941 ≈ 2,985
C
   588
1.02 × 588 ≈600
1.015 × 588 ≈ 597
A change in interest rates will not  only affect the delta of the futures contract
but can also affect the profitability of an index arbitrage strategy. If a trader initiates a buy program (i.e., buy stocks, sell futures), he is effectively borrowing cash in
order to purchase the stocks. If the cost of funds is tied to a floating interest rate,
any rate increase will hurt his position, and any decrease will help. If he institutes
a sell program (i.e., sell stocks, buy futures), he is effectively lending cash. Now any
rate increase will help his position, and any decrease will hurt it. If the change in
interest rates is sufficiently large, an initially profitable strategy might become
unprofitable. This is especially true if the program trade consists of long-term
futures contracts. In such a case, the interest considerations are magnified
because of the greater costs of borrowing or lending over extended periods. In the
same way, because of reduced interest considerations, changes in interest rates are
unlikely to affect program trades consisting of short-term futures.
We have also assumed that the dividend payout of all the stocks in an index
remains constant. But this is not necessarily true. Companies can have good
years and bad years, and their dividend policies can change accordingly. In
a buy program (i.e., buy the stocks, sell the futures), any increase in dividends
will help the position, and any decrease will hurt. In a sell program (i.e., sell the
stocks, buy the futures), the opposite is true. In a broadly based index consisting of hundreds of stocks, it is unlikely that a change in the dividend policy of
any one company or even several companies will have a significant impact on
the profitability of a program trade. But in a narrow-based index consisting of
only a few stocks, a change in the expected dividend payout of even one firm
can alter the potential profitability of the trade. In such a case, the trader must
carefully consider beforehand the possibility of a dividend change for the companies that make up the index.
--- page 475 ---

458
O P T I O N V O L AT I L I T Y A N D P R I C I N G
Bias in the Futures Market
Stock index futures are among the most liquid and actively traded of all futures
contracts. These markets enable all types of traders to make decisions based on
general market conditions rather than on unique conditions that might affect
an individual stock. Most traders believe that the general market is less subject
to manipulation than individual stocks and that index markets offer a more
level playing field.
One especially active participant in the stock index market is the portfolio
manager whose goal is typically to generate a maximum return on capital with
a minimum amount of risk. Historically, a portfolio manager has achieved this
goal in the equity markets by maintaining a portfolio of stocks that the manager believes will outperform the general market. As the manager identifies
new stocks that meet this criterion, he adds them to the portfolio while at the
same time selling off stocks that have either met his performance goals or have
ceased to perform as expected.
Occasionally, a manager with an equity portfolio may want to protect his
holding against an expected short-term decline in the general market. Prior
to the introduction of index futures, the only way to do this was to sell off the
stocks in the portfolio and then buy them back at a later date. Not only was this
time consuming but the transaction costs also tended to reduce the expected
profits from the position. But with the introduction of index futures a manager
with a broadly based portfolio may decide that his holdings tend to mimic an
index on which futures are available. If the manager believes that the characteristics of his portfolio are sufficiently similar to the index, index futures offer a
method of hedging the stocks in the portfolio without the time-consuming and
costly process of selling each individual stock in the portfolio.
The effect of portfolio hedging strategies on stock index futures tends to
result in a one-sided market because the vast majority of equity portfolio managers take long positions in equities. Even if a manager believes that a stock
will underperform the market, it is much less common for a manager to sell
stock short (sell stock that he does not own) as part of his investment program.
Hence, a portfolio manager is almost always trying to hedge a long position in
the market. To achieve this, a portfolio manager is most often selling futures
contracts. This constant selling pressure tends to depress the price of futures
contracts compared with theoretical value.
If there were a sure way to profit from this downward bias in the market,
arbitrageurs would take the opposite position in the underlying index. But we
have seen that replicating an index with a basket of stocks is not always possible. Moreover, when the portfolio manager protects his long equity position
by selling futures, a market maker or arbitrageur ends up taking the opposite
position; he is buying futures. If he wants to hedge his position with an underlying basket of stocks, he must sell stocks short. In some markets, the short sale
of stock may be prohibited, but even if short sales are permitted, selling stocks
short is never as easy as buying stocks. Moreover, the short sale of a stock, as
discussed in Chapter 2, may not earn full interest.
Given all these factors, buying and selling pressure in the stock index
futures market is not symmetrical. Many more factors seem to result in down-
--- page 476 ---

S t o c k I n d e x F u t u r e s a n d   O p t i o n s 	 459
ward pressure on futures prices than upward pressure. This does not mean
that such markets can never become inflated, with futures contracts trading
at prices greater than fair value, but this is by far the exception. In stock index
markets around the world, there tends to be constant downward pressure on
futures prices.
Stock Index Options
There are really two types of stock index options—those where the underlying is an index futures contract and those where the underlying is a cash index.
Although they are alike in many respects, they also have unique characteristics
that set them apart from each other.4
Options on Stock Index Futures
Exchange-traded options on stock index futures were first listed in the United
States in January 1983, when the Chicago Mercantile Exchange began trading options on S&P 500 futures contracts. Options on stock index futures are
evaluated in the same way as any other futures option. Exercise or assignment
results in a futures position, which is immediately subject to margin and variation. The only time exercise or assignment does not result in a futures position
is when the options and the underlying futures contract expire at the same time.
Because most stock index futures trade on the March-June-September-December
quarterly cycle, there are four times each year when stock index futures, options
on futures, and options on the cash index all expire at the same time. This triple
witching typically occurs on the third Friday of the contract month, when all
expiring stock index contracts, both futures and options, are settled in cash.
Consider a trader who owns a February 1,000 call on a stock index futures
contract. Because February is a serial month (there are no February futures),
the underlying contract is the March future. If the March future is trading
at 1,025 at February expiration, the trader will exercise the February 1,000
call, resulting in a long March futures position. Unless the trader immediately
sells the March future, the position will be subject to a margin requirement
that the trader must deposit with the clearinghouse. At the same time, the
trader, through exercise, will buy a March futures contract at 1,000. With the
futures contract now trading at 1,025, the trader’s account will be credited with
25.00 points times the index point value. If the point value is $100, the trader’s
account will be credited with 25 × $100 = $2,500. In the same way, a trader
who is assigned on a February 1,000 call will have a short March futures position. Unless the trader buys back the March future, he will also be required to
post margin, and his account will be debited by $2,500. Both the trader who
exercises and the trader who is assigned still have market positions. One trader
has a long futures position and therefore wants the market to rise. The other
trader has a short futures position and therefore wants the market to decline.
4 We might also include options on exchange-traded funds. However, exchange-traded funds are issued in shares
and therefore tend to trade like individual equity options.
