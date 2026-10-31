# Option Volatility and Pricing_ Advanced Trading Strategies -- Sheldon Natenberg -- 2nd ed, 2014 -- McGraw Hill Professional -- isbn13 9780071818773 -- 6a48d008bd9beef283debf7bad0b2e4a -- Anna’s Archive.pdf — pages 533–552

--- page 533 ---

516
O P T I O N V O L AT I L I T Y A N D P R I C I N G
In the early days of exchange-traded options, the concept of implied volatility was not well understood, at least not among most nonprofessional traders.
However, as option trading increased in popularity, all market participants, both
professional and nonprofessional, began to pay closer attention to the implied
volatility in option markets. As a means of promoting a better understanding
of options and as an aid to both traders and end users, exchanges began disseminating implied volatility data. With growing public interest in options, these
numbers began to appear with increasing frequency in financial news reports.
There are, of course, many different implied volatilities. Not only are there
many different underlying markets, but for each underlying, there are many different exercise prices and expiration months. What exchanges wanted was one
number that reflected the general implied volatility environment. This led the
Chicago Board Options Exchange (CBOE) to focus on the implied volatility of
a broad-based index, specifically its most actively traded product, the Options
Exchange Index, with ticker symbol OEX. In 1993, the CBOE began disseminating values for the volatility index (VIX), a theoretical 30-day implied volatility calculated from the prices of options on the OEX. The VIX eventually
developed into a widely recognized financial indicator not only in the option
community but also in the financial world in general. Other exchanges have
followed suit by creating volatility indexes of their own, but the VIX remains
the best known of all implied volatility indexes.
As the VIX became more widely recognized, the CBOE began to consider the possibility of creating a tradable contract based on the VIX. This
necessitated two major changes in the index. The first change had to do with
the underlying contract. Initially, VIX values disseminated by the CBOE were
derived from the prices of OEX options. However, the CBOE subsequently
introduced options on the Standard and Poor’s (S&P) 500 Index, with ticker
symbol SPX, and these eventually replaced the OEX as the exchange’s most
actively traded index product. That, combined with the fact that the S&P 500
was a much more widely followed index than the OEX, led the exchange in
2003 to begin calculating the VIX from the prices of S&P 500 options rather
than OEX options.
The second change had to do with the calculation method. The original
VIX was calculated from calls and puts at the two exercise prices that bracketed the index price—essentially the at-the-money options. For a given expiration month, the call and put implied volatilities at each exercise price were
averaged, and these were then weighted by the difference between the exercise price and the index price to yield an implied volatility for that expiration
month. In order to determine a theoretical 30-day implied volatility, the two
near-term expiration months were weighted to derive a final value.2 An example may help to clarify the methodology.
Assume that the index price is 863.40 and that the two exercise prices that
bracket this number are 860 and 870. Assume also that the nearest option contract, Month 1, has 14 days remaining to expiration and that the second option
2 For a description of the original VIX methodology, see Robert Whaley, “Derivatives on Market Volatility:
Hedging Tools Long Overdue,” Journal of Derivatives, Fall 1993, pp. 71–84.
--- page 534 ---

V o l at i l i t y C o n t r a c t s 	 517
contract, Month 2, has 42 days remaining. Implied volatilities for the two exercise prices in each month are as follows:
Month 1
Month 2
860
870
860
870
Call
22.16
21.48
20.13
19.93
Put
22.21
21.44
20.17
19.94
The average implied volatilities for each exercise price and month are

Month 1:
860
(22.16 + 22.21)/2 = 22.185

870
(21.48 + 21.44)/2 = 21.46

Month 2:
860
(20.13 + 20.17)/2 = 20.15

870
(19.93 + 19.94)/2 = 19.935
The implied volatility in each month is the interpolated implied volatility between the two exercise prices—the implied volatilities weighted by their distance from the index price. The closer the exercise price is to the index price,
the greater is the weighting:

Month 1:
 22.185 × (870 – 863.40)/10 + 21.46 × (863.40 – 860)/10
= 22.185 × 0.66 + 21.46 × 0.34 = 14.6421 + 7.2964
= 21.9835

Month 2:
 20.15 × (870 – 863.40)/10 + 19.935 × (863.40 – 860)/10
= 20.15 × 0.66 + 19.935 × 0.34 = 13.299 + 6.7779
= 20.0769
The VIX value is the interpolated implied volatility between the two expiration
months—the implied volatilities weighted by how close their expirations are to
30 days. The closer to 30, the greater the weighting. With expirations of 14 and
42 days, the final VIX value is
20.0769 × (30 – 14)/28 + 22.2785 × (42 – 30)/28
= 20.0769 × 0.5714 + 22.2785 × 0.4286

= 11.4725 + 9.5479 = 21.0204
The final VIX value disseminated by the exchange is the calculated VIX value
rounded to two decimal points, in this case 21.02.
When the exchange began planning for trading in VIX-related products,
there were two major objections to the original calculation methodology. First,
any exchange-traded product has to have a very well-defined value on which
everyone can agree. If there are significant disagreements as to the value of
a contract, especially at expiration, some traders will feel that they are being
treated unfairly. This will certainly inhibit trading in the product and might,
in some situations, lead to legal action against the exchange. The original VIX
calculation required a theoretical pricing model to determine implied volatilities. This in itself can result in disagreements. Which model should be used?
The Black-Scholes model? The binomial model? Some other more exotic
model? (Recall from Chapter 22 that the OEX is an American option, carrying
--- page 535 ---

518
O P T I O N V O L AT I L I T Y A N D P R I C I N G
with it the right of early exercise.) Even if there is general agreement on an appropriate model, there may be disagreements as to the inputs into the model.
What interest rate ought to be used? What dividend assumptions should be
made? The exchange concluded that if it wanted to introduce trading in VIXrelated products, it would be necessary to improve on the existing calculation
methodology.
The second objection had to do with the fact that only at-the-money options were used to calculate VIX values. As traders became more knowledgeable about options, the volatility skew, or smile, became increasingly important
in describing the volatility environment and in determining appropriate strategies. Traders wanted an implied volatility index that would encompass not only
the implied volatility of at-the-money options but also the implied volatility
across a broad range of exercise prices.
The VIX calculation methodology that was eventually chosen to replace
the old methodology was suggested in a research paper from Goldman Sachs
published in 1999.3 The paper essentially asked this question: is it possible to
create an option position that will capture the true volatility of the underlying
contract under all possible volatility scenarios?
In theory, if we want to take a volatility position, we can either buy options
(a long volatility position) or sell options (a short volatility position) and then dynamically hedge the position to expiration. For example, we might take a long
volatility position by purchasing one or more at-the-money options and selling
a delta-neutral amount of the underlying contract.4 By periodically rehedging
the position to remain delta neutral, we will capture the volatility value of the
underlying contract.
This all sounds very nice in theory, but it almost never works out exactly
as expected. Perhaps the greatest drawback to the strategy is the fact that exposure to the volatility of the underlying market, as measured by the vega,
will change over the life of the strategy. An option’s vega value is greatest
when the option is at the money, but even if we begin by purchasing at-themoney options, the options will almost certainly not remain at the money. As
the underlying price rises or falls, the options will either go into the money
or out of the money, and the vega of the position will decline. This was discussed in Chapter 9 and is shown again in Figure 25-1.
If we want to create a long volatility position, we want a constant exposure to volatility regardless of changes in the price of the underlying contract.
We might try to accomplish this by purchasing options across a broad range
of exercise prices. In this scenario, shown in Figure 25-2, one exercise price
will always be at the money. Unfortunately, this will still not result in a constant
vega exposure because at-the-money options with higher exercise prices have
greater vega values than at-the-money options with lower exercise prices. If we
add up all the vega values in Figure 25-2 at each underlying price, the total vega
will be lower at lower underlying prices and higher at higher underlying prices.
3 Kresimir Demeterfi, Emmanuel Derman, Michael Kamal, and Joseph Zou, “More than You Ever Wanted
to Know about Volatility Swaps,” Goldman Sachs Quantitative Strategies Research Notes, New York,
March 1999.
4 This is essentially equivalent to buying at-the-money straddles.
--- page 536 ---

V o l at i l i t y C o n t r a c t s 	 519
Figure 25-2  Volatility exposure if we purchase one option at each exercise price.
Higher underlying prices
Lower underlying prices
The volatility exposure if we
purchase one option at each
exercise price.
Total exposure
(sum of all the vega values)
Figure 25-1  The vega (volatility sensitivity) of an option.
Higher underlying prices
Lower underlying prices
Current
underlying price
The volatility exposure of an
option position, as measured
by the vega, declines as the
option moves away from
at-of-the-money
Exercise price
Vega
To achieve a constant volatility exposure, we need to buy more options
with lower exercise prices and fewer options with higher exercise prices. How
many options at each exercise price should we buy? It turns out that the proper
proportion of each exercise price needed to create a position with constant
volatility exposure is inversely proportional to the square of the exercise price
1/X2
The result of doing this is shown in Figure 25-3.
--- page 537 ---

520
O P T I O N V O L AT I L I T Y A N D P R I C I N G
Of course, to exactly replicate a volatility position, we would have to purchase options, in the correct proportion, at every possible exercise price—
essentially an infinite number of options. Exchanges, however, only list a finite
number of exercise prices. Still, it might be possible to use the exercise prices
that are listed to create a position that closely approximates a theoretically constant volatility position. This is the basis for the VIX calculation methodology
used by the CBOE.
Essentially, the value of the VIX is the cost of purchasing a strip consisting of options at every available exercise price. Because the VIX represents a
30-day implied volatility, the value of the VIX is derived from strips of options
in the two monthly expirations that bracket 30 days. The values of the strips
are then weighted by how close each expiration is to 30 days. Without going
into the complete derivation of the VIX,5 there are some important aspects
that are worth pointing out:
1.	 The value of the VIX is derived from the volatility value (time value)
of the options in the underlying index, not the intrinsic value. Therefore, only the prices of out-of-the-money options (compared with the
forward price) are used.
2.	 The (implied) forward price for the index is determined using put-call
parity for the closest-to-the-money exercise price.
3.	 The option value used at each exercise price is the average of the
quoted bid price and ask price.
5 For a detailed description of the VIX calculation methodology, see “The CBOE Volatility Index,” available
at: https://www.cboe.com/micro/vix/vixwhite.pdf.
Figure 25-3  Purchasing 1/X 2 options at each exercise price.
Higher underlying prices
Lower underlying prices
Total exposure
(sum of all the vega values)
--- page 538 ---

V o l at i l i t y C o n t r a c t s 	 521
4.	 When two exercise prices with a nonzero bid are encountered, no
lower exercise prices for puts or higher exercise prices for calls are included in the calculation
5.	 Because only a finite number of exercise prices are available, the contribution of each option to the final VIX calculation is adjusted based
on the distance between consecutive exercise prices. The greater the
distance between exercise prices, the greater is the weighting in the index for a specific option.
Note that the VIX calculation depends only on the prices of options—no
theoretical pricing model is required. Other than option prices, the only other
required input is an interest rate, which is necessary to determine the index forward price under put-call parity as well as the interest cost of purchasing the
options. For this, the CBOE uses the risk-free rate—the U.S. Treasury bill rate
with maturity closest to the option expiration. Otherwise, calculation of the
VIX is relatively straightforward.
Because the VIX represents a theoretical 30-day implied volatility, traded
contracts on the VIX typically expire 30 days prior to expiration of the options used to calculate VIX values, usually the third Wednesday of the previous
month. VIX January contracts expire 30 days prior to expiration of February
SPX options; VIX February contracts expire 30 days prior to expiration of
March SPX options; and so on.
With exactly 30 days remaining to expiration of SPX options, the value
of the VIX at expiration is determined solely by the prices of SPX options in
the expiration month. For purposes of settlement, rather than using the average of the bid and ask, the expiration value of the VIX is calculated from
the actual opening trade prices of SPX options on expiration Wednesday.
The trade prices are determined through a special opening rotation where standing buy and sell orders are automatically matched to determine one opening
trade price for each option. If no trade takes place for an option, the price
used for that option reverts to the average of the bid and ask. This procedure can sometimes cause unusual jumps in the VIX value at expiration. If
all options trade at the ask price on the opening (a buy print), the expiration
value is likely to be higher than expected. If all options trade at the bid price
on the opening (a sell print), the expiration value is likely to be lower than expected. Immediately after the VIX expiration value is determined by the special opening rotation, calculation reverts to its normal methodology using the
average of the bid-ask spread.
Some VIX Characteristics
While volatility is, in theory, independent of the direction in which the underlying contract is moving, in the real world, traders have long recognized
that some markets tend to become more volatile as the underlying price rises,
while other markets tend to become more volatile as the underlying price
falls. There is a widely held belief that stock index markets exhibit the latter
--- page 539 ---

522
O P T I O N V O L AT I L I T Y A N D P R I C I N G
Figure 25-4  S&P 500 and VIX prices: 2003–2012.
0
10
20
30
40
50
60
70
80
90
100
600
700
800
900
1,000
1,100
1,200
1,300
1,400
1,500
1,600
Dec-02 Dec-03 Dec-04 Dec-05 Dec-06 Dec-07 Dec-08 Dec-09 Dec-10 Dec-11 Dec-12
S&P 500
(left scale)
VIX
(right scale)
characteristic. It should therefore not come as a surprise that the VIX is generally negatively correlated with the S&P 500 Index. When the index falls,
the VIX tends to rise; when the index rises, the VIX tends to fall. This inverse correlation between changes in the S&P 500 and changes in the VIX
for the 10-year period from 2003 to 2012 can be seen in Figures 25-4 and
25-5. Figure 25-4 confirms the tendency of S&P 500 prices and VIX prices
to move in opposite directions. Figure 25-5 shows the strong inverse correlation value of –0.7444 between percent changes in the values of the two indexes. Figure 25-5 also includes a best-fit line for the two sets of values: the
percent change in the VIX is approximately 5.7 times greater than the percent change in the S&P 500, but in the opposite direction.
Given the apparent inverse correlation between the S&P 500 Index and
the VIX, one might wonder whether this is actually supported by market data.
If the VIX rises, will the S&P 500 Index become more volatile? If the VIX
falls, will the index become less volatile? Because the VIX represents a 30-day
implied volatility, if the marketplace is correct, whenever the VIX rises, the
next 30 days ought to be more volatile than the previous 30 days, and whenever the VIX falls, the next 30 days ought to be less volatile than the previous
30 days. The more the VIX rises or falls, the greater should be the change in
realized volatility. The actual results over the sample 10-year period are shown
in Figure 25-6.
If there is a correlation between changes in the VIX and changes in realized volatility, it is not apparent from the data. Sometimes the VIX rises and
sometimes it falls, but there is no obvious increase or decline in volatility over
--- page 540 ---

V o l at i l i t y C o n t r a c t s 	 523
Figure 25-6  Does a change in the VIX predict a change in realized volatility?
–50
–40
–30
–20
–10
0
10
20
30
40
50
60
–20
–15
–10
–5
0
5
10
15
20
Daily change in the VIX
Change in realized volatility:
next 30 days vs. previous 30 days
Correlation = +.1561
Figure 25-5  Daily S&P 500 Index changes versus daily VIX changes: 2003–2012.
–30%
–20%
–10%
0%
10%
20%
30%
40%
50%
60%
70%
–10%
–8%
–6%
–4%
–2%
0%
2%
4%
6%
8%
10%
12%
Correlation = –.7444
Daily percent change in the S&P 500 index
Daily percent change in the VIX
the following 30-day period. (There is a very small but probably insignificant
positive correlation of +0.1561.) Therefore, one might conclude that the VIX
has no predictive value as an indicator of rising or falling realized volatility. Perhaps what drives the VIX is not the expectation of future realized volatility, but
--- page 541 ---

524
O P T I O N V O L AT I L I T Y A N D P R I C I N G
the desire to buy protection in a falling stock market. In a falling market, more
hedgers enter the market, and they are often willing to pay higher prices for
protective options without regard to considerations of realized volatility. They
are driven by the fear of further declines in the market. For this reason, the
VIX is sometimes referred to as the fear index.
We have also noted the widely held belief that stock index markets tend to
become more volatile as the underlying price falls and less volatile as the underlying price rises. We might ask whether this assumption is borne out by the
available data. Figure 25-7 shows the change in the price of the S&P 500 Index
over a 30-day period compared with the realized volatility over the same period. If the conjecture is true, more data points ought to fall in both the upper
left portion (a falling index together with higher volatility) and the lower right
portion (a rising index together with lower volatility).
Here there is some reason to believe that falling stock markets do indeed
tend to be more volatile than rising stock markets. We can see from the sample period (2003–2012) that there are more high-volatility occurrences to the
left of the 0 line and more low-volatility occurrences to the right of the 0 line.
There is a moderate inverse correlation of –0.3895.
Trading the VIX
As with all indexes, the VIX is composed of components, with each component
having a weight within the index
∑
×
(weight
component )
i
i
Figure 25-7  Are falling stock markets more volatile than rising markets?
0%
10%
20%
30%
40%
50%
60%
70%
80%
90%
–35% –30% –25% –20% –15% –10% –5%
0%
5%
10% 15% 20% 25%
30-day index price change
30-day realized volatility
Correlation = –0.3895
Falling markets
high volatility
Rising markets
low volatility
--- page 542 ---

V o l at i l i t y C o n t r a c t s 	 525
An index can often be replicated by purchasing all or a large number of the index
components in the correct proportion. This is commonly done in the stock index
market to create a portfolio that tracks an index or as part of an arbitrage strategy. But unlike a stock index, it is not easy to replicate the VIX. As options go into
and out of the money, the index components and their weights within the index
are constantly changing. For most traders, the only practical method of buying or
selling the VIX is through its derivative products: futures and options or products
linked to these contracts. Because the VIX itself cannot be easily bought or sold,
VIX derivatives do not always track the index or perform as expected, and new
traders are often surprised by the results of VIX-related strategies.
VIX Futures
The CBOE began trading VIX futures contracts (with ticker symbol UX or
VX depending on the quote vendor) in 2004. The futures contracts settle into
the value of the VIX at the opening of trading on expiration Wednesday, with
each volatility point having a value of $1,000.
VIX futures have unusual characteristics when compared with more traditional futures markets, and traders who enter the VIX futures market for the
first time are often surprised and frequently disappointed at the results of a
VIX futures strategy. There are two primary reasons for this. First, VIX futures
exhibit a term structure, which can affect how futures prices change as market
conditions change. Second, unlike a position in other futures markets, an underlying position in the VIX cannot be easily replicated. In a stock index futures market, a trader can replicate an underlying index position by buying or
selling the component stocks. In a physical commodity futures market, a trader
can replicate a long underlying position by purchasing the commodity. But
for most traders, replicating an underlying VIX position directly using options
from which the index is calculated is usually not a practical choice.
VIX futures tend to reflect the term structure of implied volatility in the
S&P 500 discussed in Chapter 20 and shown in Figure 20-13. Most often
VIX futures exhibit a contango (upward-sloping) relationship, where longterm maturities trade at higher prices than short-term maturities. A typical
VIX contango structure, for futures during August 2012, is shown in Figure
25-8. Although less common, VIX futures can also exhibit a backward
(downward-sloping) relationship. Such a structure for futures prices one year
earlier, in August 2011, is shown in Figure 25-9. Figure 25-10 shows the VIX
moving from contango to backward during the financial crisis in the latter
half of 2008.
When VIX futures are in a normal contango relationship, as in Figure
25-8, if there is no change in market conditions, as time passes, the futures contract will move down the term-structure curve, gradually losing value as time
passes. How does this affect trading decisions in the VIX futures market?
Logically, a trader will want to buy a futures contract when he believes
that the futures price will rise and sell a futures contract when he believes that
the price will fall. Most traders assume that when an underlying index rises or
falls, futures contracts on that index will also rise or fall, and this is generally
--- page 543 ---

526
O P T I O N V O L AT I L I T Y A N D P R I C I N G
Figure 25-8  VIX futures in contango (upward sloping).
12
14
16
18
20
22
24
26
28
30
Index
value
1
2
3
4
5
6
7
8
9
Futures month
August 3, 2012
August 10, 2012
August 17, 2012
August 24, 2012
Figure 25-9  VIX futures in backwardation (downward sloping).
24
26
28
30
32
34
36
38
40
42
44
Index
value
1
2
3
4
5
6
7
8
9
Futures month
August 4, 2011
August 11, 2011
August 18, 2011
August 25, 2011
true of the VIX—when the index rises, VIX futures rise; when the index falls,
VIX futures fall. Most traders also assume that when an index rises or falls,
futures prices will rise or fall by approximately the same amount. But VIX futures prices reflect where the marketplace thinks SPX implied volatility will
be at maturity of the futures contract. Implied volatility, as reflected in the
--- page 544 ---

V o l at i l i t y C o n t r a c t s 	 527
index value, may be high or low today. If, however, the marketplace believes
that implied volatility will change between now and expiration of the futures
contract, the futures contract will be priced accordingly. A trader will be disappointed indeed if he buys a VIX futures contract, sees an increase in the index, but finds that there is no corresponding increase in the futures price.
Suppose that VIX futures are in a normal contango relationship and that
a trader believes that there is likely to be a rise in the value of the VIX in the
near future. If he buys a futures contract and the expected increase in the
VIX occurs, what will be the result? The trader might assume that the futures
price will increase by the same amount as the index, but this will not necessarily be true. If the increase in the VIX occurs well before expiration of the futures contract, the futures price may rise much less than the index price. Such
a scenario is shown in Figure 25-11. Over a four-day period in July 2011, the
index value rose from approximately 19.4 to 23.7, an increase of 4.4 index
points. But over the same period, the front-month August futures contract,
with approximately three weeks remaining to expiration, rose only 2.0, from
19.3 to 21.3. Indeed, over the last two days, even though the index rose from
23.0 to 23.8, futures prices hardly changed at all. A trader who owned an
August futures contract would have shown a profit because the futures price
rose. But seeing the increase in the VIX value without a similar increase in
the futures price, the trader would almost certainly have been disappointed
at the result.
A similar situation can occur if VIX futures are in a backward structure
and the index begins to fall. Figure 25-12 shows the change in VIX prices
over a four-day period in December 2008. During this period, the VIX fell
Figure 25-10  VIX futures moved dramatically from contango to backward during the
financial crisis in late 2008.
10
20
30
40
50
60
70
80
90
Index
value
1
2
3
4
5
6
7
8
9
Futures month
August 28, 2008
September 25, 2008
October 23, 2008
November 20, 2008
--- page 545 ---

528
O P T I O N V O L AT I L I T Y A N D P R I C I N G
Figure 25-11  VIX futures prices do not change as quickly as the index.
18
19
20
21
22
23
24
25
Index
value
1
2
3
4
5
6
7
8
9
Futures month
July 25, 2011
July 26, 2011
July 27, 2011
July 28, 2011
Figure 25-12  VIX futures prices do not change as quickly as the index.
36
38
40
42
44
46
48
50
52
54
Index
value
1
2
3
4
5
6
7
8
9
Futures month
December 16, 2008
December 17, 2008
December 18, 2008
December 19, 2008
from approximately 52.4 to 44.9, a decline of 7.5 index points. But the frontmonth January futures price fell only 5.0, from 52.4 to 47.4. A trader who
sold January futures would likewise be disappointed with the results.
In a traditional futures market, where it is usually possible to take a long
or short position in the underlying index or commodity, futures prices must
--- page 546 ---

V o l at i l i t y C o n t r a c t s 	 529
change at approximately the same rate as underlying prices. If this were not
true, there would be an arbitrage opportunity available. In a stock index
market, if the futures price rises faster than the index price, traders will sell the
futures contract and buy the component stocks; if the index rises faster than
the futures price, traders will buy the futures contract and sell the component
stocks. A trader can hold both positions to maturity, knowing that at maturity
the index and futures prices must converge. Unlike a stock index, though, the
VIX is not easily tradable. Consequently, VIX futures prices need not change
at the same rate as the index. If the index price rises or falls, VIX futures may
not rise or fall by the same amount. Indeed, futures prices might not change
at all.
At expiration, the price of a VIX futures contract will settle into the index
value regardless of any term-structure considerations. Therefore, the closer the
futures contract to expiration, the more closely it will respond to any change in
the index value. A change in the index value at expiration will be reflected immediately in the futures price.
Given the foregoing discussion, when choosing a simple futures strategy, a
trader should always keep the following in mind:
1.	 When the VIX term structure is contango, as time passes with
no change in the index value, VIX futures prices will inevitably
decline.
2.	 The price of a VIX futures contract will almost never change as
quickly as the index price.
3.	 Futures prices and index prices must converge at futures expiration.
4.	 For most traders, replicating the index is not a realistic choice. Therefore,
futures prices must often be evaluated independent of the index price.
Because of its unusual characteristics, trading VIX futures may sound
complex. But VIX futures are not necessarily more complex than other futures markets. They are simply different, and a trader must recognize these differences. Buying a VIX futures contract can be profitable if a trader believes
that an increase in the index value will occur, especially if the increase occurs
close to expiration, or if the trader believes that there will be a large increase
in the value of the index, perhaps resulting in an inversion of the term-structure curve from contango to backward. In the same way, selling a VIX futures
contract can be profitable if a trader believes that a decline in the index value
will occur close to expiration or if the trader believes that there will be a large
decline in the value of the index, perhaps resulting in an inversion of the term
structure from backward to contango. But in both cases the trader must also
temper his expectations, knowing that the change in the futures price will almost always be less than the change in the index price.
Instead of simply buying or selling a single futures month, a trader might
consider a futures spread, buying one futures month and selling a different
month. VIX futures spreads, like individual futures, are sensitive to the term
--- page 547 ---

530
O P T I O N V O L AT I L I T Y A N D P R I C I N G
structure of the futures market. In the unlikely situation where the term structure is a straight line with constant slope, regardless of whether futures prices
rise or fall, the spread value will remain unchanged. Even if both futures contracts lose value as time passes (a contango term structure) or gain value as
time passes (a backward term structure), their relationship will remain constant. They will lose or gain value at exactly the same rate. If, however, the term
structure is curved, a much more common situation, the short-term futures
contract will change value more quickly than the long-term futures contract.
Under these conditions, if the shape of the term structure remains unchanged,
the purchase of a long-term futures contract and the sale of a short-term future
contract will be profitable in a contango market, and the purchase of a shortterm futures contract and the sale of a long-term future contract will be profitable in a backward market. Examples of this are shown for a contango market
in Figure 25-13.
Of course, it is unlikely that the term structure will remain constant. As
market conditions change, the structure can alternate between contango and
backward, with varying degrees of curvature for each structure. Because a
short-term futures contract will almost always change more quickly than a
long-term contract, if a trader believes that a contango structure will become
less curved or will move toward a backward structure, the sale of a futures
spread (i.e., sell long term, buy short term) is likely to be profitable. If the
trader believes that a backward structure will become less curved or will move
toward a contango structure, the purchase of a futures spread (i.e., buy long
term, sell short term) is likely to be profitable. These two scenarios are shown
in Figures 25-14 and 25-15.
Figure 25-13  A futures spread in a contango market.
Straight line term structure
Curved term structure
--- page 548 ---

V o l at i l i t y C o n t r a c t s 	 531
VIX Options
The CBOE began trading VIX options in 2006. The options are European (no
early exercise) and settle into the value of the VIX at the opening of trading on
expiration Wednesday, with each volatility point having a value of $100.
Compared with other financial indexes, the VIX is highly volatile. From
Figure 25-4, it’s evident that the VIX can double or even triple in price over
short periods of time. The volatile nature of the VIX is confirmed in Figure
25-16, the 50- and 250-day volatilities of the VIX from 2003 to 2012. Over
the 10-year sample period, the 50-day volatility occasionally reached highs of
almost 200 percent, while it rarely fell below 50 percent. A trader might assume
that options on the VIX will be priced accordingly, with implied volatilities that
Figure 25-15  A futures spread when the term structure moves from backward toward contango.
If the term structure moves from backward toward contango, the
purchase of a futures spread is likely to be profitable. The short-term
contract will fall more quickly than the long-term contract.
Figure 25-14  A futures spread when the term structure moves from contango toward backward.
If the term structure moves from contango toward backward, the
sale of a futures spread is likely to be profitable. The short-term
contract will rise more quickly than the long-term contract.
--- page 549 ---

532
O P T I O N V O L AT I L I T Y A N D P R I C I N G
reflect the highly volatile nature of the index. This would be true if one could
hedge a VIX option position with the VIX. But because the index itself cannot
be easily bought or sold, the instrument that is most commonly used to hedge
a VIX option position is a VIX futures contract. VIX futures, however, are less
volatile than the index because futures prices tend to change at a slower rate
than the price of the index. Figure 25-17 shows the 50-day volatility of the index compared with the same 50-day volatility of the first three futures months.
Rarely is the front-month futures contract as volatile as the index. Moreover,
back months become progressively less volatile, reflecting the converging term
structure of the index.
Just as a VIX futures trader is likely to be disappointed when a futures contract fails to move as much as the index, a VIX options trader is likely to be disappointed when the value of an option does not react to the full volatility of the
index. For a theoretical trader who follows a dynamic hedging procedure, expectations about VIX volatility should focus on the volatility of the futures contract used to hedge the option position, not the volatility of the index.
Not only do VIX options tend to carry lower implied volatilities than one
would expect from the volatility of the index, but the distribution of implied
volatilities differs significantly from other option markets. The price of a traditional stock or commodity can, in theory, rise without limit. Moreover, over
long periods of time, there is an expectation that the prices of many traded
stocks and commodities will appreciate, with longer time periods accompanied by greater appreciation. This is the philosophy behind long-term investing. But, unlike the price of a stock or commodity, over any given period of
time, there are practical limits beyond which implied volatility is unlikely to go.
An option trader would be surprised indeed to see implied volatility in a stock
Figure 25-16  VIX 50- and 250-day historical volatility: 2003–2012.
25%
50%
75%
100%
125%
150%
175%
200%
Dec-02
Dec-03
Dec-04
Dec-05
Dec-06
Dec-07
Dec-08
Dec-09
Dec-10
Dec-11
Dec-12
250-day
volatility
50-day
volatility
--- page 550 ---

V o l at i l i t y C o n t r a c t s 	 533
index market fall below 5 percent, no matter how long he observed the market.
A trader would likewise be surprised to see implied volatility rise above 100 percent. Moreover, the value of the VIX is influenced by the mean reverting characteristics of volatility. When the VIX is at a very low level, there is a greater
likelihood that it will rise; when it is at a very high level, there is a greater likelihood that it will fall. Consequently, expectations about VIX prices will differ
from expectations about the price of traditional underlying contracts. These
expectations are reflected in the volatility skew, the distribution of implied volatilities for VIX options across exercise prices.
The volatility skews for VIX options on March 19, 2012, are shown in Figure
25-18. The shape of these skews is considerably different from the skew for a typical stock or commodity. With some variation, in most stock and commodity option
markets, exercise prices that are farther away from the current underlying price
tend to carry increasingly higher implied volatilities—hence the term volatility smile.
But, for VIX options, the implied volatility of lower exercise prices drops off very
quickly. While higher exercise prices carry higher implied volatilities, at some point
on the upside, implied volatilities stop increasing and tend to flatten out. Rather
than being a smile, the shape of the skew might be described as a half frown.
VIX options seem to be implying a price distribution that is different from a
traditional stock or commodity. Using option prices and the butterfly approach
described in Chapter 24, we can construct an implied price distribution for the
VIX. This distribution is shown in Figure 25-19 for June options on March 19,
2012 with approximately three months remaining to expiration. At the time,
June VIX futures were trading at 23.95. Compared with a traditional lognormal
distribution, the left tail is much more restricted, reflecting a belief that there is
almost no chance that the VIX will be below 10.00 at June expiration. The right
Figure 25-17  Fifty-day historical volatility of the VIX and the first three futures months.
0%
25%
50%
75%
100%
125%
150%
175%
200%
December-07
December-08
December-09
December-10
December-11
December-12
Index
1st futures
month
2nd futures
month
3rd futures
month
--- page 551 ---

534
O P T I O N V O L AT I L I T Y A N D P R I C I N G
Figure 25-18  VIX option implied volatility skews, March 19, 2012.
25%
50%
75%
100%
125%
150%
10
15
20
25
30
35
40
45
50
55
60
65
70
75
Exercise price
Implied volatility
April (1 month to expiration)
May (2 months to expiration)
June (3 months to expiration)
July (4 months to expiration)
August (5 months to expiration)
VIX = 15.04
Figure 25-19  Three-month price distribution implied from VIX option prices, March 19,
2012 [with the three-month (June) future at 23.95].
5
10
15
20
25
30
35
40
45
50
55
60
65
70
75
Underlying price
Probability
Theoretical (lognormal) distribution
Distribution implied from market prices
tail is also more restricted, perhaps reflecting a belief that large upward moves
are less likely than in a lognormal distribution. Although it may be difficult to
discern from the graph, the marketplace also seems to be implying a slightly better chance of a very large upward move at the far end of the right tail.
--- page 552 ---

V o l at i l i t y C o n t r a c t s 	 535
Replicating a Volatility Contract
Even though replication of a realized variance or VIX position is not a practical choice for most traders, in theory, it is possible to create such a position.
How can this be done?
Suppose that a trader sells a realized variance contract at a volatility of 20
(percent), equal to a variance of 202 = 400. If the actual realized volatility over
the life of the contract is greater than 20 percent, the trader will lose money; if
the actual realized volatility is less than 20 percent, the trader will make money.
How can a trader hedge this position? A variance position can be replicated by
purchasing a strip of options across all exercise prices. To create a position with
a constant-variance exposure, it is necessary to purchase 1/X2 (where X is the
exercise price) of each option. Then, by dynamically hedging the entire position in order to remain delta neutral throughout the life of the variance swap,
the total value of the strategy will exactly match the actual realized variance of
the variance contract.
It may seem that a volatility position can be replicated using the same approach. But the fact that volatility is the square root of variance means that if
the variance exposure is constant, the volatility exposure cannot be constant.
Let’s return to an earlier example where a realized volatility contract with a
vega exposure of $10,000 was purchased at a price of 20. We can compare the
outcomes in two different cases. In the first case, the contract is settled in variance points, with each point having a value equal to the notional vega divided
by twice the volatility price: $10,000/(2 × 20) = $250. In the second case, the
contract is settled in volatility points with each point have a value of $10,000.
Realized
Variance
Variance P&L
Realized
Volatility
Volatility P&L
250
−$37,500
15.81
−$41,900
300
−$25,000
17.32
−$26,800
350
−$12,500
18.71
−$12,900
400
0
20
0
450
+$12,500
21.21
+$12,100
500
+$25,000
22.36
+$23,600
550
+$37,500
23.45
+$34,500
At a realized variance of 400 (a realized volatility of 20), the variance P&L and
the volatility P&L are the same. However, as the difference between the contract variance price of 400 (a volatility price of 20) and the realized variance increases, the difference between the variance P&L and volatility P&L increases.
A strip of options done in the correct proportion of 1/X 2 yields a constant
exposure to variance. But the same strip of options does not yield a constant exposure to volatility. As realized volatility rises or falls, a trader who uses a strip
