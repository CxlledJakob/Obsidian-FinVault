# Option Volatility and Pricing_ Advanced Trading Strategies -- Sheldon Natenberg -- 2nd ed, 2014 -- McGraw Hill Professional -- isbn13 9780071818773 -- 6a48d008bd9beef283debf7bad0b2e4a -- Anna’s Archive.pdf — pages 476–495

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
--- page 477 ---

460
O P T I O N V O L AT I L I T Y A N D P R I C I N G
Now consider what will happen at expiration to a trader who owns a
March 1,000 call in the same index futures market. Unlike the February
option, which is subject to PM expiration (the option essentially expires at the
close of business on expiration Friday), the March option is subject to AM
expiration because the March future is subject to AM expiration. The value
of the March future will be determined by the opening prices of all the component stocks on expiration Friday, and this, in turn, will determine the value
of the March 1,000 call. If the call is out of the money, it will expire worthless. If the call is in the money, the exchange will automatically settle all
expiring in-the-money options in cash. The trader who owns the call will
be credited with an amount equal to the difference between the exercise
price and the opening index value times the index multiplier. If the opening
index value is 1,040 and the multiplier is again $100, the trader who is long the
option will be credited with $4,000. At the same time, the trader who is short
the option will be debited by an equal amount. Moreover, once this cash
transfer takes place, both traders are out of the market. Whether the index
subsequently rises or falls is of no consequence because no market position
results from the cash settlement.
Options on stock index futures, like most futures options, are American
and therefore carry the right of early exercise. If the options are subject to
stock-type settlement, as they are in the United States, there may be some
early exercise value over an equivalent European option, as described in
Chapter 16, although this extra value will usually be small. If the options are
subject to futures-type settlement, as they are on most exchanges in Europe
and the Far East, there is effectively no additional value over an equivalent
European option.
Options on a Cash Index
The first cash options on a stock index began trading at the Chicago Board
Options Exchange (CBOE) in March 1983. The exchange had wanted to
list options on one of the widely followed indexes, such as the S&P 500 or
Dow Jones Industrials Average, but was initially unable to obtain the rights to
trade any of these indexes. As a result, the CBOE decided to create its own
Options Exchange Index (with ticker symbol OEX) made up of 100 of the largest
U.S. companies.5 Because all individual equity options traded at the CBOE
at that time were American, with the right of early exercise, it seemed logical to make OEX options American as well. However, once trading began,
it became obvious that the early exercise feature resulted in additional and
unforeseen risks and also greatly complicated theoretical evaluation. As a
result, all exchange-traded cash index options are now European, with no
possibility of early exercise.
5 The CBOE subsequently reached an agreement with Standard and Poor’s allowing the exchange to trade
options on the S&P 500 Index. As part of the agreement, Standard and Poor’s assumed the responsibility for
calculating and disseminating OEX values. At the same time, the OEX was renamed the S&P 100 Index,
although it still retains its original ticker symbol OEX.
--- page 478 ---

S t o c k I n d e x F u t u r e s a n d   O p t i o n s 	 461
For stock index options on a cash index,6 no underlying position results
from exercise. At expiration, the exchange automatically settles all options in
cash, with a cash credit to the purchaser of an in-the-money option equal to
the difference between the exercise price and index price and cash debit of an
equal amount to the seller of the option. This is the same procedure used to settle expiring futures options when the underlying contract for the option is the
expiring futures month. Cash index options are typically subject to AM expiration, with the value of the index, and consequently the value of the options,
being determined by the opening prices of all the index components.
How should a trader hedge a position in cash index options? In theory, one
might buy or sell all the stocks in the index in the right proportion to hedge such
a position. However, this would require trades in many different stocks and, in
theory, might require the purchase or sale of fractional shares. Moreover, as
the delta of the option position changed, the trader would have to periodically
adjust the stock holdings. Given these drawbacks, hedging a position with a
basket of component stocks is impractical for most traders. What most traders
want is a hedging instrument that is easily traded and correlates closely with the
cash index. The contract that meets these requirements is a futures contract on
the same stock index as the cash options.
Assuming that futures contracts on an index are available, a trader in a
cash index option market will hedge his position with the futures contract that
expires at the same time as the options. If no corresponding futures month is
available, the nearest futures contract beyond the option expiration is used as
the hedging instrument. For index futures trading on the quarterly cycle, we
can summarize the underlying hedging instrument as follows:
Cash Index Option Expiration
Hedging Instrument
January, February, March
March futures
April, May, June
June futures
July, August, September
September futures
October, November, December
December futures
Clearly, this is not a perfect solution to the hedging problem because the
futures contract and the cash index are not identical. Indeed, a futures contract
may trade at a price above or below its theoretical value compared with the
cash index. But for most traders, using the futures contract represents a practical solution to the hedging problem.
Even if we use an index futures contract as the hedging instrument, we still
need an underlying price to evaluate options. For March, June, September, and
December options, if a position is carried to expiration, a trader can be certain
6 Ticker symbols for cash indexes very often end with the letter X, for example, SPX (Standard and Poors 500
Index), DJX (Dow Jones Industrial Index), DAX (Deutsche Aktien Index—the German Stock Index), AEX
(Amsterdam Exchange Index), OMX 30 (Stockholm Options Market Index), and ASX 200 (Australian Stock
Exchange Index).
--- page 479 ---

462
O P T I O N V O L AT I L I T Y A N D P R I C I N G
that at the moment of expiration the cash value of the index and the value
of the corresponding futures contract will converge. Consequently, a trader can
treat the futures contract as the underlying contract. Not only does this make
practical sense, but it also makes theoretical sense because option values are
derived from the forward price of the underlying contract, and the futures contract is simply the traded form of the forward price. Moreover, if both cash
options and futures options are available on an index and all options expire at
the same time, there is effectively no difference between the options. They will
essentially trade at the same prices.7
The question of what underlying price to use when evaluating a cash
index option is somewhat more complex for serial month options, where there
is no corresponding futures month. If December futures are available, we can
always price December options using the December futures price. We may
also use the December futures contract to hedge an October or November
option position if no corresponding October or November futures contract
is available. But the October or November forward price will differ from the
December forward price, so using the December futures price as the underlying price cannot be correct.
If we assume that the December futures contract represents the correct
December forward price, what should be the correct November forward price?
We might work backwards because
FDec = FNov × (1 + r × t) – D
Then
F
F
D
r
t
1
Nov
Dec
=
+
+ ×
However, this requires us to estimate the dividends expected between November and December expirations. An easier method used by most traders is to
determine the November forward price implied by option prices in the marketplace. We can do this by observing the prices of a November call and put that
are close to at the money and whose prices will consequently be similar and
then use put-call parity to calculate the implied forward price. For example,
November 1,000 call = 34.85
November 1,000 put = 29.90
Time to November expiration = 2 months
Annual interest rate = 6.00 percent
Because
C
P
F
X
r
t
1
−
=
−
+ ×
7 For deeply in-the-money options on futures, which are typically American, there may be a very slight additional early exercise value.
--- page 480 ---

S t o c k I n d e x F u t u r e s a n d   O p t i o n s 	 463
then
F = (C – P) × (1 + r × t) + X
FNov = (34.80 – 29.85) × 1.01 + 1,000 = 1,005
The implied November forward price is 1,005.00.
Now suppose that when we calculate the implied November forward price,
the December futures price is 1,010.00. This means that there should be a difference between the November forward price and the December forward price
of 5.00. As the price of the December futures contract fluctuates, if we want
to calculate theoretical values for November cash options, we can use as the
underlying price, the December futures price, less 5.00.
We might also use put-call parity to calculate the implied December
forward price. But this is not really necessary because we have the implied
December forward price in the form of a December futures contract. Still, we
might check to see if December option prices are consistent with the December
futures price. If
December futures price = 1,010
Time to December expiration = 3 months
Annual interest rate = 6.00 percent
from put-call-parity we know that the December 1,000 combo (the difference
between the prices of the December 1,000 call and 1,000 put) should be
C
P
F
X
r
t
1
10
1.015
9.85
−
=
−
+ ×
=
=
If the December 1,000 call is trading at a price of 44.60, the December 1,000
put should be trading at a price of 44.60 – 9.85 = 34.75.
November
December
1,000 call
34.80
44.60
1,000 put
29.85
34.75
The price of the November/December 1,000 roll (i.e., the difference between
the December and November 1,000 synthetics) is
(44.60 – 34.75) – (34.80 – 29.85) = 9.85 – 4.95 = 4.90
--- page 481 ---

464
Models and the
Real World
A trader who uses a theoretical pricing model is exposed to two types of risk—
the risk that the trader has the wrong inputs into the model and the risk that
the model itself is wrong because it is based on false or unrealistic assumptions.
Thus far we have focused primarily on the first area, the risk associated with the
inputs into the model. A trader will typically deal with this risk by paying close
attention to the sensitivities of an option position (i.e., delta, gamma, theta,
vega, and rho), thereby preparing to take protective action when market conditions move against him. While any of the inputs into the model may represent
a risk, we have placed special emphasis on volatility because it is the one input
that cannot be directly observed in the marketplace.
However, an active option trader cannot afford to ignore the second type of
risk, the possibility that the assumptions on which the model is based are inaccurate or unrealistic. Some of these assumptions pertain to the way business is transacted in the marketplace, while others pertain to the mathematics of the model.
To begin, we might list the most important assumptions built into traditional
pricing models1:
1.	 Markets are frictionless.
A.	The underlying contract can be freely bought or sold, without
restriction.
B.	Unlimited money can be borrowed or lent, and the same interest
rate applies to all transactions.
C.	There are no transaction costs.
D.	There are no tax consequences.
1 By traditional pricing model we mean those that are most commonly used: the Black-Scholes model and its variations or the Cox-Ross-Rubinstein model.
23
--- page 482 ---

M o d e l s a n d t h e R e a l W o r l d 	 465
2.	 Interest rates are constant over the life of an option.
3.	 Volatility is constant over the life of an option.
4.	 Trading is continuous, with no gaps in the price of an underlying
contract.
5.	 Volatility is independent of the price of the underlying contract.
6.	 Over small periods of time, the percent price changes in an underlying
contract are normally distributed, resulting in a lognormal distribution
of underlying prices at expiration.
The reader may already have an opinion about the validity of these assumptions, but let’s consider them one by one.
Markets Are Frictionless
In Chapter 8, we came to the obvious conclusion that markets are not frictionless. The underlying contract cannot always be freely bought or sold; there are
sometimes tax consequences; a trader cannot always borrow and lend money
freely, nor at the same rate; and there are always transaction costs.
In futures markets, the underlying cannot always be freely bought or sold
because an exchange may set a daily price limit beyond which a futures contract is not permitted to trade. When that limit is reached, the market it locked,
and trading is halted until the market comes off its limit. If it does not come off
its limit, trading does not resume until the next business day.
Even if a futures market is locked, it may be possible for a trader to circumvent the trading restriction. Instead of buying or selling futures contracts,
a trader might be able to trade in the cash market. Or the trader might be
able to trade a futures spread where one side of the spread is not locked.
For example, a trader who wants to buy a June futures contract that is up its
allowable limit may be able to buy a June/March spread (i.e., buy June, sell
March). If the March futures contract is still trading because it is not up its
limit, the trader can then go back into the market and buy back the March
futures contract. This leaves him long a June futures contract, which was his
original intention. If the underlying futures market is locked but the option
market is not locked, a trader might be able to buy or sell synthetic futures
contracts.
Trading can also be halted on a stock exchange if a designated stock index
either rises or falls during a trading day by a predetermined amount. When this
limit is reached, the exchange will halt trading for some period of time. The
exchange’s circuit breakers specify how long trading will be halted for a given percent change in a stock market index
In Chapter 2, we noted that an exchange or regulatory authority may
place restrictions on the short sale of stock—the sale of stock that a trader does
not actually own. Even if short sales are permitted, there may be restrictions on
--- page 483 ---

466
O P T I O N V O L AT I L I T Y A N D P R I C I N G
when such sales can be made. If a trader cannot freely sell stock, put prices will
tend to become inflated compared with call prices, and arbitrage relationships,
such as conversions and reversals, will appear to be mispriced. Many stock option traders, as a matter of good trading practice, will try to carry some long
stock so that they will always be in a position to sell stock if the need arises.
The assumption that a trader can always borrow or lend money freely is a
more serious weakness in pricing models. Even if a trader has sufficient funds
to initiate a trade, he may find at some later date that he needs additional funds
to meet increased margin requirements.2 If money were freely available, margin would never be a problem. A trader could always borrow margin money
and deposit the money with the clearinghouse. Because the borrowing and
lending rates are assumed to be the same, and because the clearinghouse, in
theory, pays interest on the margin deposit, there would never be a problem
obtaining margin money, nor would there ever be a cost associated with it.
In the real world, traders do not have unlimited borrowing capacity. If
a trader cannot meet a margin requirement, he may be forced to liquidate a
position prior to expiration. Because all models, even those that allow for early
exercise, assume that a trader will always have the choice of holding a position to expiration, the inability to meet margin requirements and therefore
maintain the position can make the values generated by the theoretical pricing model less reliable. An experienced trader should always consider the
risk of a position not only in terms of how much the position might lose in
total but also in terms of how much margin might be required to maintain the
position over time.
Even if a trader has unlimited borrowing capacity, the fact that for most
traders, borrowing and lending rates are not the same can also cause problems
with strategies based on model-generated values. A trader who borrows margin
money at one rate will almost certainly receive a lower rate when he deposits this
money with the clearinghouse. The difference between these rates is something
of which the model is unaware. And the greater the difference between borrowing and lending rates, the less reliable will be the values generated by the model.
Although there are occasionally tax considerations, for most traders,
these are usually secondary. For a given a strategy, a trader is unlikely to ask
himself, “If this trade is profitable or unprofitable, what will be the tax consequences?” Differences in tax consequences rarely make one strategy better
than another.3
Lastly, the assumption that there are no transaction costs is a serious flaw
in the frictionless markets hypothesis. While a strategy may or may not be
affected by tax or interest-rate considerations, there are always transaction
costs. These costs can come in the form of brokerage fees, clearing fees, or an
exchange membership. For some market participants, transaction costs may be
2 The possibility that a trader in a futures option market may also have to come up with additional variation
money, as opposed to margin money, after establishing an option position is incorporated into most models.
This is why a conversion or reversal in a futures option market may not be delta neutral.
3 This is not to say that tax consequences are always insignificant. Tax considerations can play a role in portfolio management or in option strategies involving dividends when the dividends are subject to tax rules different
from the gains or losses from stock or options.
--- page 484 ---

M o d e l s a n d t h e R e a l W o r l d 	 467
prohibitive, and a strategy that looks sensible based on model-generated values
may not be worth doing when transaction costs are also taken into consideration. Moreover, transaction costs can accrue not only when the strategy is initiated or liquidated but also whenever an adjustment is made. If a strategy will
require many adjustments because it has a high gamma and the trader intends
to remain approximately delta neutral, the transaction costs can have a significant impact on model-generated values.
Interest Rates Are Constant over the Life of an Option
When a trader feeds an interest rate into a pricing model, the model assumes
that this one rate applies to all transactions over the entire life of the option.
Whatever cash flows result from an option trade will be either invested, if a
credit, or borrowed, if a debit, at one constant rate. In reality, very few traders initiate one trade and simply hold the position to expiration. As traders
initiate new positions or close out existing ones, they are constantly borrowing and lending money. Moreover, in futures options markets, traders are
subject to changing margin and variation requirements. For all these reasons,
most traders require a degree of cash liquidity that is incompatible with borrowing or lending at one fixed rate over long periods of time. To achieve the
required liquidity, traders commonly finance their trading activity by borrowing from or lending to their clearing firm at a variable rate. The clearing firm
acts as a bank, informing the trader of the effective rate or rates that apply on
any given day.
Even if a trader is able to negotiate a fixed rate over some period of time,
there is still the problem of determining which of the various rates apply: is the
trader borrowing money (a borrowing rate), lending money (a lending rate), or
receiving interest on a short stock position (a short stock rebate). In the last case,
the rate that the trader receives will often depend on the difficulty of borrowing
the stock.
Although changing interest rates will cause the value of a trader’s option
position to change, interest rates tend to be a lesser risk for most traders, at
least for short-term option strategies. The impact of changing interest rates is
a function of time to expiration. Because most actively traded options tend to
be short term, with expirations of less than one year, interest rates would have
to change dramatically to have an impact on any but the most deeply in-themoney options. Changing interest rates become even less of a concern when
one considers how much more sensitive option values are to changes in the
price of the underlying instrument or to changes in volatility.
This is not to say that a trader should completely ignore interest-rate risk.
For stock options especially, raising interest rates raises the forward price,
which raises the value of calls and lowers the value of puts. The options that
are most sensitive to this change are deeply in-the-money long-term options.
Such options will have the greatest interest-rate sensitivity, as reflected by
their high rho values. With many exchanges now listing long-term options,
--- page 485 ---

468
O P T I O N V O L AT I L I T Y A N D P R I C I N G
Figure 23-1  Theoretical values as interest rates change.
Theoretical value
20
30
40
10
50
Annual interest rate
0%
2%
6%
8%
12%
14%
16%
4%
10%
0
Stock price = 100
Time to expiration = 3 years
Volatility = 20%
Dividend = 0
110 put
100 put
100 call
110 call
90 call
90 put
Figure 23-2  Rho values as time to expiration changes.
–1.0
–0.5
0
0.5
1.0
1.5
2.0
Rho
0
6
12
18
24
30
36
–1.5
Time to expiration (months)
100 call 110 call
90 call
100 put 110 put
90 put
Stock price = 100
Volatility = 20%
Interest rate = 6%
Dividend = 0
a trader should be aware of the impact of changing rates on such options.
Figure 23-1 shows the effect of rising interest rates on long-term stock
options. Figure 23-2 shows the effect on rho values for stock options as we
increase time to expiration.
--- page 486 ---

M o d e l s a n d t h e R e a l W o r l d 	 469
Volatility Is Constant over the Life of the Option
When a trader feeds a volatility into a theoretical pricing model, he is specifying the magnitude and frequency of price changes that will occur over the life
of the option. Because these price changes are assumed to be normally distributed, the model recognizes that there will be some number of one, two,
three, and so on standard deviation occurrences and that these occurrences
will be evenly distributed over the life of the option. Two standard deviation
price changes will be evenly distributed among the one standard deviation
price changes; three standard deviation price changes will be evenly distributed
among the one and two standard deviation price changes; and so on.
In the real world, however, price changes are unlikely to be evenly distributed. Over the life of an option, a trader will encounter periods of high volatility,
where large price changes will dominate, together with periods of low volatility, where small price changes dominate. The combination of these highand
low-volatility periods will result in one volatility. But a theoretical pricing model
is indifferent as to how the volatility unfolds. The model sees one volatility and
evaluates options accordingly.
Figures 23-3 and 23-4 are daily high/low/close bar charts for a hypothetical underlying contract over a period of 80 trading days. Both bar charts
represent exactly the same close-to-close realized volatility over the period in
question, 28 percent. But the order in which the volatility unfolds is different.
In Figure 23-3, volatility is clearly declining, with larger price changes occurring early in the 80-day period and smaller price changes occurring later in
the period. In Figure 23-4, the opposite is true. Volatility is rising, with smaller
price changes occurring early and larger changes occurring later. The reader
may have already guessed that the charts are in fact mirror images of each
Figure 23-3  Falling volatility.
98
100
102
96
104
106
94
--- page 487 ---

470
O P T I O N V O L AT I L I T Y A N D P R I C I N G
other and therefore must represent the same volatility. Even though the volatility unfolded in two completely different scenarios, in both cases, a pricing
model will use the same volatility, 28 percent, to make all calculations.
In both Figures 23-3 and 23-4, the beginning and ending price is 100.
Suppose that a trader buys a 100 straddle and assumes, correctly, a volatility
of 28 percent. What should this straddle be worth? To simplify the example,
let’s assume that there are 80 calendar days to expiration and that every day
is a trading day (hence no weekends and holidays). To focus only on volatility,
let’s also assume that the interest rate is 0. Under these assumptions, the Black-
Scholes model will generate a value for both the 100 call and put of 5.23, for a
total straddle value of 10.46.
Alternatively, suppose that we calculate the value of the 100 call and put by
running a simulation of the dynamic hedging process. Using the closing price
each day, the number of days remaining to expiration, and a known volatility
of 28 percent, we can calculate the delta at the end of each trading day. We can
then buy or sell the required number of underlying contracts to remain delta
neutral. (This is the same approach used to explain the dynamic hedging process in Chapter 8.) The results of such a simulation show that if the volatility is
falling (Figure 23-3), the 100 call and put are worth 2.97 each, for a total straddle value of 5.94. But, if volatility is rising (Figure 23-4), the 100 call and put
are worth 6.41 each, for a total straddle value of 12.82. Why do these values
differ so dramatically from the Black-Scholes value of 10.46?
A strategy that will be helped by higher realized volatility, such as a long
straddle, will benefit most if periods of high in volatility occur when the gamma
is greatest. The high gamma will magnify the changes in the delta as the underlying price changes, resulting in greater profit from the dynamic hedging process. Because the 100 straddle is essentially at the money and the gamma of an
Figure 23-4  Rising volatility.
98
100
102
96
104
106
94
--- page 488 ---

M o d e l s a n d t h e R e a l W o r l d 	 471
at-the-money option increases as expiration approaches, any increase in volatility close to expiration will have a disproportionately greater impact on the
option’s value than a similar increase in volatility early in the option’s life. Consequently, the rising-volatility scenario increases the value of the 100 straddle well
above the Black-Scholes value. Of course, the higher gamma close to expiration
goes hand in hand with a higher theta. With no underlying movement close to
expiration, the option will decay at an accelerated rate. Therefore, the fallingvolatility scenario has an inordinately negative impact on the value of the 100
straddle, causing the value to fall below the Black-Scholes value.
For out-of-the-money options, the effect is just the opposite. The gamma
of an out-of-the-money option is largest early in its life, so a period of high
volatility early in the option’s life will increase its value. An out-of-the-money
option will be worth more than the predicted Black-Scholes value in a falling-volatility scenario and worth less in a rising-volatility scenario. This is confirmed by the results of a dynamic hedging simulation for the 80 put and 120
call. At a volatility of 28 percent, the Black-Scholes values are 0.21 for the 80
put and 0.54 for the 120 call. If, however, volatility is falling, the values are 0.44
and 0.89. If volatility is rising, the values are 0.05 and 0.14.
Option values under our three different volatility scenarios for exercise
prices from 70 to 130 are shown in Figure 23-5. With the price of the underlying remaining generally between 95 and 105, options with exercise prices of 95,
100, and 105 are worth more than the Black-Scholes value in a rising-volatility
Underlying price = 100
Time to expiration = 80 days
Interest rate = 0
Volatility = 28%
Exercise price:
70
75
80
85
90
95
100
105
110
115
120
125
130
Constant volatility
(Black-Scholes)
Calls:
30.01 25.06 20.21 15.62 11.48
7.98
5.23
3.22
1.87
1.03
0.54
0.27
0.13
Puts:
0.01
0.06
0.21
0.62
1.48
2.98
5.23
8.22 11.87 16.03 20.54 25.27 30.13
Straddle:
30.01 25.12 20.42 16.24 12.96 10.96 10.46 11.44 13.74 17.06 21.08 25.54 30.26
Falling volatility
(Figure 23-3)
Calls:
30.04 25.15 20.44 16.00 11.79
7.59
2.97
2.69
2.10
1.43
0.89
0.51
0.27
Puts:
0.04
0.15
0.44
1.00
1.79
2.59
2.97
7.69 12.10 16.43 20.89 25.51 30.27
Straddle:
30.08 25.30 20.88 17.00 13.58 10.18
5.94 10.38 14.20 17.86 21.78 26.02 30.54
Rising volatility
(Figure 23-4)
Calls:
30.00 25.01 20.05 15.21 10.75
8.97
6.41
3.36
1.29
0.41
0.14
0.05
0.02
Puts:
0
0.01
0.05
0.21
0.75
3.97
6.41
8.36 11.29 15.41 20.14 25.05 30.02
Straddle:
30.00 25.02 20.10 15.42 11.50 12.94 12.82 11.72 12.58 15.82 20.28 25.10 30.04
Using an interest rate of zero, the time premium for a call and put with the same exercise
price must be identical. The value of the call and put will differ only by intrinsic value.
Figure 23-5  Option values under three different volatility scenarios.
--- page 489 ---

472
O P T I O N V O L AT I L I T Y A N D P R I C I N G
market and less than the Black-Scholes value in a falling-volatility market. The
opposite is true for exercise prices below 90 or above 110. They are worth more
in a falling-volatility market and less in a rising-volatility market.
If an option is held to expiration with no accompanying dynamic delta hedging, the value of the option depends solely on the underlying price at expiration.
The option’s value is independent of the path by which the underlying contract
reaches its terminal value. But the preceding examples make it clear that in a
world where a trader dynamically hedges an option position, the value of the
option is in fact path dependent. Even if we assume a single volatility, the route that
the underlying takes can have a significant impact on the value of the option.
Because the value of an option seems to be path dependent, one might
conclude that the Black-Scholes model is unreliable. Indeed, for any one random-walk scenario, the value resulting from the dynamic hedging process will
almost certainly differ from a Black-Scholes value. But the Black-Scholes model
is a probabilistic model. A given volatility will, on average, result in a given value
for the option. In our example, we considered only two alternative volatility
scenarios, where volatility is either rising or falling. But there are an almost infinite number of paths that the underlying price might follow over the life of an
option. If we were to generate a large number of random price paths, all with
normally distributed price changes and with the same volatility of 28 percent
and if we were to then simulate the dynamic hedging process, we would find
that, on average, each exercise price is worth something very close to the value
predicted by the Black-Scholes model.
Although the Black-Scholes model assumes that prices follow a random
walk through time with constant volatility, we might instead assume that volatility is itself random. Several models that assume stochastic volatility have been
proposed and might, in some cases, be more suitable than a traditional pricing
model. At the same time, such models add an additional dimension of complexity to a trader’s life and for this reason are not widely used.
Some contracts, by their very nature, are known to change their volatility
characteristics over time. Interest-rate products in particular fall into this category. As a bond approaches maturity, the price of the bond moves inexorably toward par. At maturity, regardless of interest rates, the bond will have a
fixed and known value. Clearly, one cannot assume that the price of the bond
follows a random walk through time. Even if one assumes that interest rates
move randomly and that the volatility of interest rates is constant, interest-rate
instruments will change their volatility over time because instruments of different maturities have different sensitivities to changes in interest rates. If we take
into consideration the fact that interest rates also vary for different maturities,
a traditional Black-Scholes type model is obviously not well suited to the evaluation of such products. This has led to the development of special models to
evaluate interest-rate instruments.
Trading Is Continuous
To model option values, a model must make some assumptions about how the
price of an underlying contract changes over time. One possible assumption
is that prices follow a continuous diffusion process. Under this assumption, price
--- page 490 ---

M o d e l s a n d t h e R e a l W o r l d 	 473
changes are continuous, with no gaps permitted between consecutive prices.
An example of a typical continuous diffusion process might be the temperature readings in a specific location. Although the temperature can change very
quickly, there will never be any gaps. If the temperature is initially 25 degrees
but later drops to 22 degrees, then at some intermediate time, even if only very
briefly, the temperature must have also been 24 degrees and then 23 degrees.
The Black-Scholes model assumes that the underlying contract follows a
continuous diffusion process. Trading proceeds 24 hours per day, 7 days per
week, without interruption, and with no gaps in the price of the underlying
contract. If a contract trades at 46.05 and at some later time trades at 46.08,
then at some intermediate time it must also have traded, even if only briefly,
at 46.06 and 46.07. If one were to graph with pen and paper the prices of an
underlying contract that follow a continuous diffusion process, one would never
lift the pen from the paper. An example of this is shown in Figure 23-6a.
If we assume that the underlying contract follows a continuous diffusion
process, we can also assume that the dynamic hedging process can be carried out continuously. This is fundamental to capturing an option’s theoretical
value. The Black-Scholes model assumes that a position can be rehedged to
remain delta neutral at every possible moment in time.
A continuous diffusion process may be a reasonable approximation of how
prices change in the real world, but it is clearly not perfect. An exchange-traded
contract cannot follow a pure diffusion process if the exchange is not open
24 hours per day. At the end of the trading day, a contract may close at one
price and then open the next day at a different price. This causes a price gap,
something that a diffusion process does not permit. Even during normal
trading hours, news might be released, the impact of which can be almost
instantaneous, causing the price of a contract to gap either up or down.
Instead of a diffusion process, prices might follow a jump process. In a jump
process, the price of a contract remains fixed for a period of time and then
instantaneously jumps to a new price, where it again remains fixed until a new
jump occurs. The way in which central banks set interest rates is typical of
a jump process. In the United States, when the Federal Reserve sets the discount rate, it remains fixed until the Fed announces a change. The discount
rate then jumps to a new level. A typical jump process, shown in Figure 23-6b,
is a combination of fixed prices and instantaneous jumps.
In the real world, prices of most underlying contracts follow neither a pure
diffusion process nor a pure jump process. The real world seems to be a combination of the two—a jump-diffusion process. Most of the time, trading proceeds
normally with no price gaps. Occasionally, though, an unexpected change
in market conditions occurs that causes the underlying contract to instantaneously gap to a new price. Such a process is shown in Figure 23-6c.
If a theoretical pricing model assumes that prices follow a diffusion process when in fact they don’t, how is this likely to affect values generated by
the model? To understand the effect of a gap, consider a trader who sells an
at-the-money straddle with the underlying contract trading at 100. How will
the trader feel if the underlying contract suddenly gaps up to 105? Clearly,
this is not what the trader was hoping for. Such a large move might well be
accompanied by an increase in implied volatility, which will also hurt the
--- page 491 ---

474
O P T I O N V O L AT I L I T Y A N D P R I C I N G
trader’s position. But even if implied volatility does not change, because of
the negative gamma associated with the short straddle, the large move in the
underlying contract will clearly work against the trader. How bad will the
damage be? If the options are relatively long term, say, one year, the gap in
the underlying price is unlikely to be the end of the world. After all, with one
year remaining to expiration, the underlying market could certainly fall back
to 100. While the gap has hurt the trader, it is probably not disastrous. But,
if the gap occurs with only a very short time remaining to expiration, say,
one day, the trader is now in a much worse situation. With only one day to
Figure 23-6  (a) Diffusion process. (b) Jump process. (c) Jump-diffusion process.
(a)
(b)
(c)
--- page 492 ---

M o d e l s a n d t h e R e a l W o r l d 	 475
expiration, there is not enough time for the market to retrace its movement.
The 100 calls that the trader sold as part of the short straddle will immediately go deeply into the money, acting like short underlying contracts. The
straddle may have begun approximately delta neutral, but after the gap, the
trader will find himself naked short deeply in-the-money calls, each with a
delta of 100. The value of the one-day straddle will increase dramatically
compared with the value of the one-year straddle.
The reason the effect of the gap is much greater if the straddle is short
term rather than long term is a result of how the gamma changes over time.
We know that as expiration approaches, the gamma of an at-the-money option
increases, causing the delta to change much more rapidly when the underlying
price moves. The dynamic hedging process can reduce some of the damage if
the trader is able to buy underlying contracts as the underlying price rises. But a
gap is an instantaneous move; there is no opportunity to adjust. The very high
gamma, combined with an inability to make any adjustment, makes the consequences of the gap much more dramatic close to expiration.
Not only does the gamma of an at-the-money option increase as expiration approaches, but it also increases as we reduce volatility. Consequently, the
impact of a gap will be much greater in a low-volatility market than in a highvolatility market. If we consider these two traits together, we can conclude that
at-the-money options close to expiration in a low-volatility market are among
the riskiest of options.
Figure 23-7 shows the change in value for a 100 straddle if the market
should gap as expiration approaches. The chart shows the change under two
Underlying price = 100
Time to Expiration
1 Day
1 Week
1 Month
3 Months
6 Months
1 Year
Implied volatility = 15%
Initial straddle value
0.63
1.66
3.45
5.98
8.46
11.96
Straddle gamma
101
38
18
11
8
5
Straddle value after a
gap from 100 to 105
5.00
5.01
5.58
7.39
9.57
12.90
Increase in value
4.37
3.35
2.13
1.41
1.11
0.94
Implied volatility = 25%
Initial straddle value
1.04
2.76
5.76
9.97
14.09
19.90
Straddle gamma
61
23
11
6
4
3
Straddle value after a
gap from 100 to 105
5.00
5.25
7.20
10.98
14.98
20.78
Increase in value
3.96
2.49
1.44
1.01
0.89
0.88
Figure 23-7  Effect of a gap on the value of a 100 straddle.
--- page 493 ---

476
O P T I O N V O L AT I L I T Y A N D P R I C I N G
volatility scenarios, 15 and 25 percent. Note the greater change in the straddle
value close to expiration, as well as the greater change in a low-volatility market.
Options have the unique characteristic of automatically and continuously
rehedging themselves by changing their deltas as the price of the underlying
contract changes. It is this characteristic for which buyers of options are paying. A trader who uses a theoretical pricing model attempts to take advantage of a mispriced option by hedging the option position, delta neutral, with
the underlying contract and then manually performing the rehedging process
himself over the life of the option. If a model assumes that prices follow a diffusion process, the model also assumes that one can continuously maintain a
delta-neutral hedge. But when the market gaps, the assumptions on which the
model is based are violated. Consequently, the values generated by the model
are rendered invalid. This problem extends to any application that attempts
to replicate option characteristics through a continuous rehedging in the
underlying market. The proponents of portfolio insurance (see Chapter 17)
suffered their greatest setbacks on October 19 and 20, 1987, when the market
made several large-gap moves. Because of the gaps, the portfolio insurers were
unable to make continuous delta adjustments to their positions. As a consequence, they found that the cost of protection offered by portfolio insurance
was much greater than they had expected.
To more accurately evaluate options, a variation on the Black-Scholes
model has been proposed that includes the possibility of gaps in the price of
the underlying contract. This jump-diffusion model, in theory, generates values
that are more accurate than traditional Black-Scholes values,4 but the model
is considerably more complex mathematically and also requires two new
inputs—the average size of a jump in the underlying market and the frequency
with which jumps are likely to occur. Unless the user can accurately estimate
these new inputs, the values generated by a jump-diffusion model may be no
better—and might be worse—than those generated by a traditional model.
Many traders take the view that whatever weaknesses are encountered in a
traditional model can be best offset through intelligent decision making based
on actual trading experience rather than through the use of a more complex
jump-diffusion model.
Assuming that a trader has a delta-neutral position that he intends to
dynamically hedge, any gap will have a negative impact on a trader who has
a negative gamma position because the trader will not have an opportunity to
adjust as the market moves. The same gap will have a positive impact on a
trader with a positive gamma position because he will also not have an opportunity to adjust as the market moves. In the latter case, this works to the trader’s
advantage.
Because a gap in the market will have its greatest effect on high-gamma
options, and because at-the-money options close to expiration have the highest
4 A discussion of the jump-diffusion model can be found in most advanced texts on option pricing. For additional information, see Robert Merton, “Option Pricing when Underlying Stock Returns Are Discontinuous,” Journal of Financial Economics 3(March):125–144, 1976; Stan Beckers, “A Note on Estimating the
Parameters in the Jump-Diffusion Model of Stock Returns,” Journal of Financial and Quantitative Analysis, March
1981, pp. 127–140; and Espen Gaarder Haug, The Complete Guide to Option Pricing Formulas, 2nd ed. (New York:
McGraw-Hill, 2006).
--- page 494 ---

M o d e l s a n d t h e R e a l W o r l d 	 477
gamma, it is these options that are most likely to be mispriced by a traditional
theoretical pricing model. Consequently, as expiration approaches, experienced traders will tend to rely less and less on model-generated values and
more on their own experience and intuition. This is not to suggest that under
these circumstances a model is of no value, but one needs to make adjustments
when the model is known to be incorrect.
As a result of the gaps that occur in the real world, both a trader’s experience and empirical evidence seem to indicate that a traditional model, with
its built-in diffusion assumption, tends to undervalue options in the real world.
If one compares the average historical volatility of an underlying market with
the average implied volatility over long periods of time, the average implied
volatility is almost always greater. This seems to indicate that buyers of options are overpaying. Part of this may be due to hedgers willing to pay an additional premium for protective options. But the implied volatility is derived from
a theoretical pricing model that does not include the possibility of gaps in the
underlying price. The possibility of these gaps tends to indicate that perhaps
the values of options are in fact greater in the real world than is predicted by a
traditional theoretical pricing model.
We have seen that a gap will have the greatest impact on an option position
close to expiration, particularly for at-the-money options because these options
have the greatest gamma. From a risk standpoint, this means that it can be very
dangerous to sell a large number of at-the-money options close to expiration
because any gap in the underlying market can have devastating results. New
traders in particular are advised to avoid such positions. No risk manager will
appreciate even experienced traders being short large numbers of at-the-money
options as expiration approaches.
Expiration Straddles
If it is dangerous to sell at-the-money options close to expiration, perhaps
there is some sense in taking the opposite position by purchasing at-the-money
options as expiration approaches. This may seem to contradict conventional
option wisdom, which focuses on the rapid time decay associated with such
options. But there is always a tradeoff between risk and reward. If one sells
at-the-money options, the reward may be an accelerated profit if the market
doesn’t move (high positive theta), but the risk is an increased loss if the market
does move (high negative gamma). Because the model does not know about the
possibility of a gap in the underlying market, the risk is often greater than the
reward. If one sells at-the-money options, the losses from an unexpected gap
can more than offset the profits resulting from increased time decay. An experienced trader may therefore take the opposite position by purchasing at-themoney options close to expiration.
This is not to suggest that every time expiration approaches, a trader
should buy at-the-money options. As with any strategy, conditions must make
the strategy look attractive. But because many traders are intent on selling time premium as expiration approaches, it is often possible to find cheap
--- page 495 ---

478
O P T I O N V O L AT I L I T Y A N D P R I C I N G
at-the-money options. Suppose that with three days remaining to expiration,
the Black-Scholes model generates a value for an at-the-money call of 0.75.
What can we say about this call? Although we may not know the exact value
because we don’t know the true future volatility, there is high likelihood that in
the real world the call is worth more than 0.75 because the model doesn’t know
about the possibility of a gap in the market. If, on top of this, the call is trading
at a price below its model-generated value, say, 0.65, it is likely to be a good buy.
As with any strategy based on volatility, the trader who buys these calls will
try to establish a delta-neutral position. Because of the synthetic relationship, if
the calls are underpriced, the puts at the same exercise price will also be underpriced. Thus, a logical strategy might be the purchase of at-the-money straddles.
This enables a trader to buy both underpriced calls and underpriced puts and to
profit if the underlying market gaps either up or down.
In theory, all volatility strategies, including an expiration straddle, ought
to be adjusted periodically to remain delta neutral. However, with little time
remaining to expiration, the model is not only unreliable with respect to theoretical values, but also unreliable with respect to deltas. Because it is impossible
to say what the right delta is, it is also impossible to say what the correct adjustment is. For this reason, traders who buy expiration straddles often abandon
any attempt to remain delta neutral and simply sit on the position to expiration.
This may not be the theoretically correct way to manage a volatility position,
but given all the uncertainties associated with theoretical evaluation as expiration approaches, it may be a practical choice.
Even if a trader carefully chooses his expiration straddles, the great majority of time no gap will occur in the market. In any single case, the trader is more
likely to show a loss than a profit. But the primary concern is not the profit or
loss5 from any single trade, but what happens in the long run. Returning to the
roulette example in Chapter 5, a player who chooses a number at a roulette
table can expect to win on average only 1 time in 38. But, if the theoretical
value of the bet is 95 cents and the player can buy the bet for less than 95 cents,
he expects to be a winner in the long run. Even if he is able to pay a very low
price for the bet, say, 50 cents, he still expects to lose 37 times out of 38. But
now the bet is very attractive. Even if he only wins 1 time in 38, this will still
more than offset the small losses he takes each time he loses. The same logic
is true of expiration straddles. A trader may lose several times before winning.
But when he does win, he can expect a return that is great enough to more than
offset all the small losses.
The fact that an at-the-money straddle may be cheap does not mean
that a trader should buy these straddles in large numbers. Such strategies
are likely to result in a loss more often than a profit, so an intelligent trader
should only invest an amount that he can afford to lose. However, when conditions are right, a trader ought to be willing to make the investment. Even if
he loses several times in succession, in the long run, he will encounter gaps in
the market or large increases in volatility often enough to make such strategies profitable.
5 This assumes, of course, that the trader is able to absorb the loss and still stay in business for the long run.
