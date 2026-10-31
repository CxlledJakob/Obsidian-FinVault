# Option Volatility and Pricing_ Advanced Trading Strategies -- Sheldon Natenberg -- 2nd ed, 2014 -- McGraw Hill Professional -- isbn13 9780071818773 -- 6a48d008bd9beef283debf7bad0b2e4a -- Anna’s Archive.pdf — pages 172–191

--- page 172 ---

R i s k M e a s u r e m e n t I I 	 155
Figure 9-23  Lambda of a call as time passes or volatility changes.
Lambda
Lower underlying prices
Higher underlying prices
More time to expiration
or higher volatility
Less time to expiration
or lower volatility
0
Figure 9-24  Lambda of a put as time passes or volatility changes.
Lambda
Lower underlying prices
Higher underlying prices
Less time to expiration
or lower volatility
More time to expiration
or higher volatility
0
--- page 173 ---

156
O P T I O N V O L AT I L I T Y A N D P R I C I N G
and put lambda values rise (they take on large negative values). Lambda values are also sensitive to changes in time and volatility. If we increase volatility, lambda values for both calls and puts fall. If we reduce volatility or as time
passes, lambda values for both calls and puts rise.
A trader who wants the biggest possible return on his investment, in percentage terms, compared with an equal investment in the underlying contract
can maximize his lambda by trading out-of-the-money options close to expiration in a low-volatility environment. Of course, this is true only in theory.
There may be other considerations, such as the bid-ask spread and liquidity of
the option market, that might make a large lambda position impractical compared with a similar position in the underlying market.
It may seem that we have gone into undue detail in our examination
of the option risk measures. Although it is certainly true that not every risk
is important in every situation, experienced traders have learned that it is
almost impossible to overemphasize the importance of risk management
in option trading. Because options are affected by so many different market
forces, unless a trader is aware of and understands the many ways in which
option values change, he cannot hope to successfully manage the very real
risks that option trading entails.
A summary of the primary risk characteristics discussed in this chapter is
given in Figures 9-25 and 9-26.
C = call theoretical value  P = put theoretical value  S = underlying price or spot price
t = time to expiration  σ = annual volatility  r = domestic interest rate  rf = foreign interest rate
Risk Name
Sensitivity of the
To a Change in
Math
Maximized
Delta (Δ)
Theoretical value
(in points)
Underlying price
(in points)
∂C/∂S ≈ ∂P/∂S + 1
Deeply in the money
Lambda (Λ)
[omega (Ω)]
elasticity
Theoretical value
(in percent)
Underlying price
(in percent)
Δc*(S/C)
Δp*(S/P)
Out of the money
Close to expiration
Low volatility
Gamma (Γ)
curvature
Delta
Underlying price
∂2C/∂S2 =
∂2P/∂S2
∂Δ/∂S
At the money
Close to expiration
Low volatility
Theta (Θ)
time decay
Theoretical value
Time to expiration
∂C/∂t
∂P/∂t
At the money
Close to expiration
Low volatility
Vega
Theoretical value
Volatility
∂C/∂σ = ∂P/∂σ
At the money
Long term
Rho (Ρ)
Theoretical value
Interest rate
∂C/∂r
∂P/∂r
Deeply in the money
Long term
Rhof or phi (Φ)
Theoretical value
Foreign interest
rate or dividend
yield
∂C/∂rf
∂P/∂rf
Deeply in the money
Long term
Figure 9-25  Traditional risk measures.
--- page 174 ---

R i s k M e a s u r e m e n t I I 	 157
Risk Name
Sensitivity of the
To a Change in
Math
Maximized
Vanna
Delta
Vega
Volatility
Underlying price
∂2C/∂S∂σ
∂2P/∂S∂σ
15-20, 80-85 delta
Low volatility
Charm
delta decay
Delta
Theta
Time
Underlying price
∂2C/∂S∂t
∂2P/∂S∂t
15-20, 80-85 delta
Close to expiration
Speed
Gamma
Underlying price
∂3C/∂S3 = ∂3P/∂S
∂2Δ/∂S2   ∂Γ/∂S
15-20, 80-85 delta
Low volatility
Close to expiration
Color
gamma decay
Gamma
Charm
Time to expiration
Underlying price
∂3C/∂S2∂t
∂3P/∂S2∂t
∂Γ/∂t
At the money
Close to expiration
Low volatility
Volga
(vomma)
Vega
Volatility
∂2C/∂σ2 =
∂2P/∂σ2
10, 90 delta
Long term
Low volatility
Vega decay
Vega
Time
∂2C/∂σ∂t
∂2P/∂σ∂t
20, 80 delta
Close to expiration
Zomma
Gamma
Vanna
Volatility
Underlying price
∂3C/∂S2∂σ =
∂3P/∂S2∂σ
∂Γ/∂σ
At the money
Close to expiration
Low volatility
Figure 9-26  Nontraditional higher-order risk measures.
--- page 175 ---

158
10
Introduction to
Spreading
In option markets, as in all markets, there are many different approaches to
trading. At one time, scalping was a popular strategy among traders on the floors
of futures exchanges. By observing the activity in a particular market, a scalper
would try to determine an equilibrium price that reflected a balance between
buyers and sellers. The scalper would then quote a bid-ask spread around
this equilibrium price, attempting to buy at the bid price and sell at the offer
price as often as possible without taking either a long or short position for any
extended period of time. The scalper made no attempt to determine the theoretical value of the contract. Although the profit from each trade might be
small, if a trader was able to trade often enough, he expected to show a reasonable profit. Scalping, however, requires a highly liquid market, and option markets are rarely sufficiently liquid to support this type of trading.
A different type of trading strategy involves speculating on the direction in
which the underlying contract will move. The directional position can be taken
in a variety of ways—in the cash market, in the futures market, or in the option
market. Unfortunately, even when an underlying market moves in the expected
direction, taking a directional position in an option market will not necessarily be profitable. Many different forces, including changes in volatility and the
passage of time, can affect an option’s price. If a trader’s sole consideration
is direction, he is usually better advised to take the position in the underlying
market. If he does and he is right, he is assured of making a profit.
Most successful option traders are spread traders. Because option evaluation
is based on the laws of probability and the laws of probability can be expected
to even out only over long periods of time, option traders must often hold positions for extended periods. Over short periods of time, while the trader is waiting for an option position to move toward theoretical value, the position may
be affected by a variety of changes in market conditions that threaten its potential profit. Indeed, over short periods of time, there is no guarantee that an option position will react in a manner consistent with a theoretical pricing model.
--- page 176 ---

I n t r o d u c t i o n t o S p r e a d i n g 	 159
Spreading enables an option trader to take advantage of theoretically mispriced
options while at the same time reducing the effects of short-term “bad luck.”
What Is a Spread?
A spread is a strategy that involves taking opposing positions in different but
related instruments. Most commonly, a spread will consist of positions that
move in the opposite direction with respect to changes in market conditions.
When market conditions change, one position is likely to gain value, while the
other position is likely to lose value. Of course, if the values change at the same
rate, the value of the spread will never change. A profitable spreading strategy
is predicated on the assumption that the values of the positions will change at
different rates.
Many common spreading strategies are based on arbitrage relationships,
buying and selling the same or very closely related instruments in different markets to profit from a mispricing. The cash-and-carry strategy common in commodity markets is an example of this type of spread. Given the current cash price,
interest rate, and storage and insurance costs, a commodity trader can calculate the value of a forward contract. If the actual market price of the forward
contract is higher than the calculated value, the trader will create a spread by
purchasing the commodity, selling the overpriced forward contract, and carrying the position to maturity.1
Consider a commodity trading at a price of $700. If interest rates are 6
percent annually and storage and insurance costs combined are $5 per month,
what should be the value of a two-month forward contract?
Forward price = cash price + interest + storage and insurance

= $700 + ($700 × 0.06 × 2/12) + (2 × $5)

= $717
If the actual price of the two-month forward contract is $725, the trader
might buy the commodity for $700, sell the forward contract for $725, and
carry the position to maturity. The total cash flow in terms of debits (–) and
credits (+) will be

Cost of borrowing $700 for two months at 6.00 percent
–$7

Cost of buying the commodity
–$700

Cost of storing and insuring the commodity for two months
–$10

Amount received for the commodity at maturity
+$725
The total profit resulting from this strategy is
–$7 – $700 – $10 + $725 = +$8
This is exactly the amount by which the forward contract was mispriced. The
resulting profit will be unaffected by fluctuations in the price of either the
1 The opposite type of arbitrage, selling the commodity and buying a forward contract, is not usually possible
in commodity markets because commodities, unlike financial instruments, cannot be borrowed and sold short.
--- page 177 ---

160
O P T I O N V O L AT I L I T Y A N D P R I C I N G
commodity itself or the forward contract because all cash flows were determined at the time the strategy was initiated. Whether the commodity rises to
$800 or falls to $600, the profit is still $8.
Another type of spreading strategy involves buying and selling futures contracts of different maturities on the same underlying commodity. In the preceding example, we calculated the value of a two-month forward contract on a
commodity at $717. We can do a similar calculation for a four-month forward
contract. Here, however, the cost of borrowing will be compounded because
we will need to borrow $700 for the first two-month period at 6 percent and
then borrow $717 for the second two-month period, also at 6 percent.2

Cost of borrowing $700 for two months at 6.00 percent and then

borrowing $717 for another two months at 6.00 percent:

–(700 × 0.06/6) – (717 × 0.06/6) = 7.00 +7.17
–$14.17

Cost of buying the commodity
–$700.00

Cost of storing and insuring the commodity for four months	 –$20.00
The value of the four-month forward contract ought to be
Four-month forward price = $700.00 + $14.17 + $20.00

= $734.17
If there are two-monthand four-month exchange-traded futures contracts on
this commodity, there should be a $17.17 difference, or spread, between the
prices of the two contracts. If the spread between months is actually $20, a
trader might buy the two-month contract and sell the four-month contract. The
trader cannot tell whether either contract individually is overpriced or underpriced. But he knows that at a price of $20, the spread is $2.83 too expensive.
Assuming that the trader has accurately evaluated the spread, how will he
make this $2.83 profit? One possibility is that the price of the futures spread
will return to its expected value of $17.17. Having sold the spread (sell the fourmonth futures contract, buy the two-month futures contract), the trader can
close out the position by purchasing the spread (buy the four-month futures
contract, sell the two-month futures contract).
If the price of the spread does not return to its expected value, the trader
can carry the entire position to maturity. Suppose that the spread was originally
created by purchasing the two-month forward contract at a price of $717 and
selling the four-month forward contract at a price of $737. If carried to maturity, the cash flow from the entire position will be as follows:

At the maturity of the two-month futures contract:

  Borrow $717 for two months at 6.00 percent
–$7.17

  Buy the commodity at the agreed-on two-month

  forward price
–$717.00

  Store and insure the commodity for the two months

  to maturity of the four-month futures contract
–$10.00
2 For simplicity, we have assumed a constant interest rate. In fact, the cost of borrowing money for the second
two-month period may be different from the cost of borrowing for the first two-month period. We have also
ignored the cost of borrowing money to pay for storage and insurance. This will add a very small additional
cost to the strategy.
--- page 178 ---

I n t r o d u c t i o n t o S p r e a d i n g 	 161

At maturity of the four-month futures contract:

  Deliver the commodity and receive the agreed-on

  four-month forward price
+$737.00

Total profit
+$2.83
Of course, the trader could have achieved the same result by simply selling the four-month forward contract and buying the commodity. However,
although a trader may have easy access to a futures exchange, he may find that
his access to the physical commodity market is limited because such markets
are typically dominated by large corporations. In such a case, he may find that
it is both simpler and cheaper to execute the spread in the futures market.
Spreading strategies are often done to reduce one or more risks. In a cashand-carry strategy, much of the directional risk is eliminated because the value
of the long cash contract and the value of the short forward contract will tend
to move in opposite directions. But a spreading strategy will not necessarily eliminate all risks. In our example, we assumed that we were able to borrow money at a fixed rate, thereby eliminating any interest-rate risk. We also
assumed that storage and insurance costs were fixed when the strategy was initiated. If we are dealing only with futures contracts, changes in interest rates, as
well as changes in storage and insurance costs, may affect the price relationship
between futures months. If the changes are large enough, a seemingly profitable spreading strategy may in fact become unprofitable. In the preceding
example, if interest rates and storage costs rise after the strategy has been initiated, the spread between the two-month and four-month futures contract will
widen, resulting in a smaller profit to the trader or perhaps even a loss.
Our examples thus far were both intramarket commodity spreads, with
all contract values based on the same underlying commodity. However, if a
trader can identify a price relationship between two different commodities or
two different financial instruments, he might consider an intermarket spread,
buying in one market and selling in a different market. As with all spreads, the
strategy is based on the assumption that there is an identifiable relationship
between the prices of different contracts. When the price spread between the
two contracts appears to violate this relationship, it represents an opportunity
for the trader.
In the fixed-income markets, a common strategy involves buying or selling short-term interest-rate instruments and taking an opposing position in
long-term interest-rate instruments. The value of the spread depends on
changes in the yield curve—the relationship between shortand long-term
interest rates.
Consider two futures contracts with the same time to maturity, a 10-year
Treasury note future trading at price of 116 14/32 and a 30-year Treasury bond
future trading at a price of 118 27/32.3 The spread between the two is
118 27/32 – 116 14/32 = 2 13/32
The prices of Treasury contracts move in the opposite direction of interest
rates. If interest rates rise, Treasury prices will fall; if interest rates fall, Treasury
3 Treasury note and bond prices are typically quoted in points and 32nds of par value.
--- page 179 ---

162
O P T I O N V O L AT I L I T Y A N D P R I C I N G
prices will rise. If a trader believes that interest rates will rise but that long-term
rates will rise more quickly than short-term rates, he might sell the 10-year/30-
year spread.4 If he is correct, the spread will narrow, perhaps at a later date
trading at
11510/32 – 1137/32 = 23/32
If the trader originally sold the spread at 213/32 and later buys the spread back
at 23/32, he will show a profit of
213/32 – 23/32 = 10/32
As a somewhat different intermarket spread, suppose that a trader observes
the prices of two commodities, Commodity A and Commodity B, over an
extended period and concludes that Commodity B tends to trade at a price that
is three times greater than that of Commodity A. That is,
Price of Commodity B = 3 × price of Commodity A
If the price of Commodity A is 50, the price of Commodity B ought to be 150.
If the price of Commodity A is 200, the price of Commodity B ought to be
600. Although prices may occasionally deviate from this, they eventually seem
to revert to this 3:1 relationship. Given this relationship, what will a trader do if
the current prices of the commodities are

Price of Commodity A = 120

Price of Commodity B = 390
With prices of 120 and 390, Commodity B is trading at a multiple of 3.25
times Commodity A. Given the historical relationship, Commodity B seems
to be trading at a price that is too high compared with Commodity A. Either
Commodity A ought to be trading at 360 (3 × 120) or Commodity B ought to
be trading at 130 (390/3).
If the trader believes that the prices are likely to return to their 3:1 historical relationship, he might purchase three contracts of Commodity A for 120
each and sell one contract of Commodity B at a price of 390

+3 Commodity A for 120
–360

–1 Commodity B at 390
+390

Total credit
        +30
If at a later date the contract prices return to their 3:1 relationship, the trader
can close out the position at no cost, leaving him with the expected profit of 30.
This profit will be independent of the actual prices of the two commodities as
long as the 3:1 relationship is maintained.
The strategy that we have just described involves buying and selling unequal numbers of contracts, sometimes referred to as a ratio strategy. It is common in markets where there is a perceived relationship between products with
similar characteristics but that trade at different prices. In the precious metals
4 Traders refer to this as the NOB spread (notes over bonds).
--- page 180 ---

I n t r o d u c t i o n t o S p r e a d i n g 	 163
market, a trader might spread gold against silver, even though gold trades at
a price many times that of silver. In the agricultural market, a trader might
spread corn against soybeans, even though soybean prices are always greater
than corn prices. In the stock index market, a trader might spread the Standard
and Poor’s (S&P) 500 Index against the Dow Jones Industrial Average Index.
All these spreads differ from previous strategies in that they depend on an observed and perhaps less well-defined relationship than that between the cash
price and the futures price or between the prices of different futures months.
Because the relationship is less reliable, these types of spreads carry greater uncertainty and therefore greater risk. Nonetheless, if a trader believes that his
analysis of a price relationship is accurate, the strategy may be worth pursuing.
Thus far, all our spreading examples have consisted of two sides, or legs. In
the first example, one leg consisted of a physical commodity and one leg consisted of a forward contract. In the second example, the legs consisted of two
different futures contracts. In the third example, the legs consisted of two different commodities. But spreading strategies may consist of many legs as long as a
price relationship between the different legs can be identified.
In energy markets, a common spreading strategy consists of buying or selling crude oil futures and taking an opposing position in futures in products that
are made from crude oil—gasoline and heating oil. The value of this crack spread
depends on the cost of refining, or cracking, crude oil into its derivative products, as well as the demand for these products relative to the cost of crude oil.
If the costs of refining rise or the demand for refined products rises, the value
of the spread will widen. If costs fall or demand falls, the value of the spread
will narrow.5
There are a number of ratios in which the crack spread can be traded, but
one common ratio is the 3:2:1—3 gallons of crude oil to yield 2 gallons of gasoline and 1 gallon of heating oil. Because the value of the refined products is
greater than that of crude oil, a trader is said to buy the spread when he buys
the products and sells crude oil.
Price of the 3:2:1 crack spread = (2 × gasoline) +
(1 × heating oil) – (3 × crude oil)
A trader who believes that the demand for refined products will fall can sell
the crack spread. A trader who believes that demand will rise can buy the
spread.
In some markets, it may be necessary to execute each leg of a spread
separately because there may be no counterparty willing to execute the
entire spread at one time. If the spread consists of multiple legs and the
trader has only been able to execute one leg, he will be at risk until he completes the spread by executing the remaining legs. If the trader must execute
the spread one leg at a time, he needs to consider the risk resulting from this
piecemeal execution. Determining how best to execute a spread is usually a
matter of experience.  It is often true that some legs, owing to the liquidity in
5 A similar type of three-sided spread is available in the soybean market. The crush spread consists of buying or
selling soybean futures and taking an opposing futures position in the products that are made from soybeans—
soybean oil and soybean meal.
--- page 181 ---

164
O P T I O N V O L AT I L I T Y A N D P R I C I N G
the respective markets, will be more difficult to execute than other legs. As a
consequence, most traders learn that it is usually best to execute the more difficult leg first. If a trader does this, he will find that execution risk is reduced
because he will be able to more easily complete the spread. If, on the other
hand, a trader executes the easier leg first, he may be left with a naked position if he is unable to execute the remaining legs in a timely manner or at a
reasonable price.
Fortunately, in many markets, spreads are traded all at one time as if they
are one contract. A quote for the spread will typically consist of one bid price
and one offer price, no matter how complex the spread. Consider a spread that
consists of buying Contract A and selling Contracts B and C with the following bid-ask quotes:
Contract
Bid
Ask
A
128
131
B
47
49
C
68
70
From the bid-ask quotes for each of the individual contracts, the current market for the spread is

Bid:
128 – 49 – 70 = 9 (buy Contract A, sell Contracts B and C)

Ask:
131 – 47 – 68 = 16 (sell Contract A, buy Contracts B and C)
If a trader wants to buy the spread, he can immediately trade all three contracts
individually and pay a total of 16. If he wants to sell the spread, he can do so at
a price of 9. But a trader may take the position that because he is trading multiple contracts, he ought to get some discount. A market maker in this spread will
often take the view that because he has less risk when he executes all contracts
at one time, he is willing to do so at a price more favorable to the trader. If the
trader asks for a market for the entire spread, he will often find that the difference between the bid price and ask price is narrower than the sum of the bid-ask
prices, perhaps 11 bid, 14 offer. Executing the entire spread as one transaction
will clearly be better than executing the spread as three individual transactions.
Even if a spread is executed as one trade, many exchanges require that
parties trading a spread still report the prices of the individual contracts.
If this is the case, what prices should be reported if a trader buys the entire spread at a price of 14? In fact, the individual prices really don’t matter.
Whether the trader pays 129 for Contract A and sells Contracts B and C at 48
and 68 (129 – 47 – 68 = 14) or pays 131 for Contract A and sells Contracts B
and C at 48 and 69 (131 – 48 – 69 = 14), the total price is still 14. Indeed, the
parties could decide for whatever reason to trade Contract A at a price of 200
and Contracts B and C at prices of 86 and 100 (200 – 86  100 = 14). As far as
the parties to the trade are concerned, all that matters is that the individual
prices add up to the agreed-on spread price of 14.6
6 In practice, when reporting the price of a spread, exchanges prefer that the parties to the trade use prices for
the individual contracts that reflect current market conditions. Otherwise, it may appear that someone is engaging in unethical or illegal market activity. The exchange will not be happy if the parties report prices of 200,
86, and 100, even though these prices still add up to a total spread price of 14.
--- page 182 ---

I n t r o d u c t i o n t o S p r e a d i n g 	 165
Option Spreads
At the beginning of this chapter, we defined a spread as consisting of opposing positions in related instruments. But what do we mean by a position? In
the spread examples thus far, the positions were based on directional considerations. If the value of one position rises as a result of a directional move in the
underlying market, the value of the opposing position is expected to decline,
even though ultimately the price of the spread is expected to converge to some
projected value. We can also create directional spreads in the option market by
taking opposing but unequal delta positions in different contracts. As with our
other spreads, the value of such a spread will depend on directional movement
in the underlying contract.
While the prices of options are affected by directional moves in the underlying market, they can also be affected by other factors. In an option market,
we might create a spread by taking a long gamma position in one option and
a short gamma position in a different option, or by taking a long vega position
and a short vega position, or even a long and short rho position. The value of
each of these spreads will depend on factors other than directional moves in
the underlying market. The gamma spread will be sensitive to the volatility of
the underlying market. The vega spread will be sensitive to changes in implied
volatility. And the rho spread will be sensitive to changes in interest rates.
The dynamic hedging examples in Chapter 8 are typical gamma spreads. We
initiated the spreads by either purchasing or selling options and then offsetting
the option’s delta with an opposing delta position in the underlying contract.
However, although an underlying contract has no gamma, an option does have
a gamma. As a result, the entire position had either a positive or a negative
gamma. From this we demonstrated that the value of the position depended
not on the direction of movement in the underlying contract but on the volatility of the underlying contract.
Many option spreads are dynamic, requiring periodic adjustments. But a
spread can also be static. Once initiated, the spread is carried to expiration without adjustments. This is usually done only when the risk characteristics of the
spread are well defined and limited.
Perhaps in no other market are spreading strategies as widely employed as
they are in option markets. There are a number of reasons for this:
1.	 A trader might perceive a relative mispricing between contracts. Just as a trader
might calculate the value of a futures contract in relation to the price
of a cash contract, an option trader might try to identify the value of
one option contract in relation to another option. Although it may not
be possible to determine the exact value of either contract, the trader
might be able to estimate the relative value of the contracts. If prices
in the marketplace deviate from this relative value, a trader will try to
profit by either buying or selling the spread.
  In many markets, traders express a mispricing in terms of how
much the price of a contract differs from its value. In option markets,
the mispricing is often expressed in terms of volatility. Consider two
--- page 183 ---

166
O P T I O N V O L AT I L I T Y A N D P R I C I N G
options, one that has a theoretical value of 7.00 and is trading at a
price of 8.00 and another that has a theoretical value of 6.00 and is
trading at a price of 6.75. Which option represents a greater mispricing? Looking only at the option prices, the first option appears to be
overpriced by 1.00, whereas the second option appears to be overpriced by only 0.75. But suppose that the volatility used to calculate
the theoretical value is 23 percent. Because both options are overpriced, we know that their implied volatilities must be greater than
23 percent. If the implied volatility of the option trading at 8.00 is
26 percent, while the implied volatility of the option trading at 6.75
is 28 percent, an option trader is likely to conclude that in volatility
terms, the second option is more overpriced.
Option Theoretical Value
(Using a Volatility of 23%)
Option Price
Option Implied Volatility
7.00
8.00
26%
6.00
6.75
28%
2.	 A trader may want to construct a position that reflects a particular view of market conditions. Options can be combined in an almost infinite variety of
ways such that a position will yield a profit when market conditions
move favorably. At the same time, options can be combined in ways
that will limit loss when conditions turn unfavorable. We looked at
some examples of this in Chapter 4. Of course, even if a trader is able
to construct a position that exactly reflects his view of market conditions, he will have to decide whether the prices at which the trades can
be executed make the position worthwhile.
3.	 Spreading strategies help to control risk. This is particularly important for
someone who is making decisions based on a theoretical pricing
model. In Chapter 5, we stressed the fact that all commonly used pricing models are probability based and that outcomes predicated on
the laws of probability are only reliable in the long run. In the short run,
any one outcome can deviate from the expected outcome. If a trader
wants to be successful in options, he must ensure that he remains in
the game for the long run. If he is unlucky in the short run and must
leave the game, the long-term probability theory does him no good.
Spreading is the primary method by which traders limit the shortterm effects of “bad luck.”
In addition to reducing the effects of short-term bad luck, spreading strategies can also help protect a trader against incorrectly estimated inputs into
the theoretical pricing model. Suppose that a trader estimates that over the life
of an option, the volatility of an underlying contract will be 35 percent. Based
on this, he determines that a certain call option, which is currently trading at a
price of 4.00, has a theoretical value of 3.50. If the call has a delta of 25, the
trader might try to capture this mispricing by selling four calls at a price of 4.00
--- page 184 ---

I n t r o d u c t i o n t o S p r e a d i n g 	 167
each and buying one underlying contract and dynamically hedging the position over the life of the option. The total theoretical edge for the position is
4 × 0.50 = 2.00. Of course, if the trader can make 2.00 with a 4 × 1 spread, it
may occur to him that he can make 20.00 if he increases the size of the spread
to 40 × 10. Why stop now? The trader can make 200.00 if he increases the size
to 400 × 100.
Even if the market is sufficiently liquid to absorb the increased size, is this
a reasonable approach to trading? Should a trader simply find a theoretically
profitable strategy and do it as many times as possible in order to maximize
the potential profit? At some point, the intelligent trader will have to consider
not only the potential profit of a strategy but also its risks. After all, the trader’s
volatility estimate of 35 percent is just that, an estimate. What will happen if
volatility actually turns out to be some higher number, perhaps 40 percent, or
45 percent? If the calls that the trader sold at 4.00 are worth 4.50 at a volatility
of 45 percent, and volatility actually turns out to be 45 percent, then the hopedfor profit of 200.00 (assuming a size of 400 × 100) will turn into a loss of 200.00.
A trader must always consider the effects of an incorrect estimate and then
decide how much risk he is willing to take. If the trader in this example decides
that he can survive if volatility goes no higher than 40 percent (a 5 percentage
point margin for error), he might only be willing to do the spread 40 × 10. But,
if there is some way to increase his breakeven volatility to 45 percent (a 10 percentage point margin for error), he might indeed be willing to do the spread
400 × 100. Option spreading strategies enable traders to profit under a wide
variety of market conditions by giving them an increased margin for error in
estimating the inputs into a theoretical pricing model. No trader will survive
very long if his livelihood depends on estimating each input with 100 percent
accuracy. But if he has constructed an intelligent spreading strategy that allows
for a large margin of error, the experienced trader can survive even when his
estimates of market conditions turn out to be incorrect.
To see how spreading strategies can be used to reduce risk, recall our example in Chapter 5 where a casino is selling a roulette bet with an expected
value of 95 cents for $1.00. The casino knows that based on the laws of probability, it has a 5 percent theoretical edge. Suppose that a customer comes into
the casino and proposes to bet $2,000 on one number at the roulette table.
Should the casino allow the bet? The casino owner knows that the odds are
on his side and that he will most likely get to keep the $2,000 bet, but there is
always a chance that the player’s number will come up. If it does, the casino
will lose $70,000 (the $72,000 payoff less the $2,000 cost of the bet). If the
casino is backed by millions of dollars, the loss of $70,000 will not severely
interfere with the casino’s continuing operations. If, however, the casino is only
backed by $50,000, the loss of $70,000 will put the casino out of business. And
if the casino goes out of business, it can no longer rely on its 5 percent edge because this is an expectation that is only reliable in the long run. And the long
run has just been eliminated.
Now consider a slight variation where two customers come into the casino
and propose to place bets of $1,000 each at the roulette table, but they also
agree not to bet on the same number. Whichever number one player chooses,
--- page 185 ---

168
O P T I O N V O L AT I L I T Y A N D P R I C I N G
the other will choose a different number. As with the first scenario, where one
player makes a single $2,000 bet, the casino’s potential reward in this new scenario is also $2,000. If neither number comes up, the casino gets to keep the
two $1,000 bets. But what is the risk to the casino now? In the worst case, the
casino can only lose $34,000, the $36,000 payoff if one player wins less the cost
of the two $1,000 bets. The two bets are mutually exclusive—if one player
wins, the other must lose.
In return for the reduced risk, it might seem that the casino must give up
some of its theoretical edge. We tend to assume that there is a tradeoff between risk and reward. But the edge to the casino in both cases is still the same
5 percent. Regardless of the amount wagered or the number of individual
bets, the laws of probability specify that in the long run the casino gets to keep
5 percent of everything that is bet at the roulette table. In the short run, however, the risk to the casino is greatly reduced with two $1,000 bets because the
bets have been spread around the table.
Casinos do not like to see an individual player wager a large amount of
money on one outcome, whether at roulette or any other casino game. This is
why casinos have betting limits. The laws of probability are still in the casino’s
favor, but if the bet is large enough and the bettor happens to win, the shortterm bad luck can overwhelm the casino. From the casino’s point of view, the
ideal scenario is for 38 players to place 38 bets of $1,000 each on all 38 numbers at the roulette table. Now the casino has a perfect spread position. One
player will collect $36,000, but with $38,000 on the table, the casino has a sure
profit of $2,000.
Looking at the situation from the player’s point of view, if the player knows
that the odds are against him and he wants the greatest chance of showing a
profit, his best course is to wager the maximum amount on one outcome and
hope that in the short run he gets lucky. If he continues to make bets over a long
period of time, the laws of probability eventually will catch up with him, and
the casino will end up with the player’s money.
An option trader prefers to spread for the same reason that the casino prefers the bets to be spread around the table: spreading maintains profit potential but reduces short-term risk. There is rarely a perfect spread position for an
option trader, but an intelligent option trader learns to spread off the risk in as
many different ways as possible to minimize the effects of short-term bad luck.
An important part of any serious option trader’s education consists of learning
a wide variety of spreading strategies.
New traders are sometimes astonished at the size of the trades an
experienced option trader is prepared to make. How can the trader afford
to do this? His financial resources certainly play a role in the risk he is willing to accept. But equally important is his ability to spread off risk. An
experienced trader may know many different ways to spread off the risk, using other options, futures contracts, cash contracts, or some combination of
these. While he may not be able to completely eliminate his risk, he may be
able to reduce it to such an extent that his risk is actually less than that of a
much smaller trader who does not know how to spread or knows only a limited number of spreading strategies.
--- page 186 ---

169
11
Volatility Spreads
In Chapter 8, we showed that it is possible, at least in theory, to capture an
option’s mispricing in the marketplace by employing a dynamic hedging
strategy. The first step in this process involves hedging the option position,
delta neutral, by taking an opposing market position in the underlying contract. But the underlying contract is not the only way in which we can hedge
an option position. We might instead take our opposing delta position with
other options.
Consider a call with a delta of 50 that appears to be underpriced in the
marketplace. If we buy 10 calls, resulting in a delta position of +500, we might
hedge the position in any of the following ways:

Sell five underlying contracts.

Buy puts with a total delta of –500.

Sell calls, different from those that we purchased, with a total delta of
–500.

Do a combination of any of the preceding such that we create a total
delta of –500.
There are clearly many different ways of hedging our 10 calls. Regardless
of which method we choose, each spread will have certain features in common:

Each spread will be approximately delta neutral.

Each spread will be sensitive to changes in the price of the underlying
instrument.

Each spread will be sensitive to changes in implied volatility.

Each spread will be sensitive to the passage of time.
Spreads with the foregoing characteristics fall under the general heading
of volatility spreads. In this chapter, we will look at the most common types of volatility spreads, initially by examining their expiration values and then by considering their delta, gamma, theta, vega, and rho characteristics.
--- page 187 ---

170
O P T I O N V O L AT I L I T Y A N D P R I C I N G
Straddle
A straddle consists of a call and a put where both options have the same exercise price and expiration date. In a straddle, both options are either purchased
(a long straddle) or sold (a short straddle). Examples of long and short straddles,
with their expiration profit-and-loss (P&L) graphs, are shown in Figures 11-1
and 11-2.
At expiration, the value of a straddle can be expressed as a simple parity
graph. But what about its value prior to expiration? As with all option positions,
some changes in market conditions will help the strategy and some changes will
hurt. From Figure 11-1, we can see that a long straddle becomes more valuable
when the underlying market moves away from the exercise price and less valuable as time passes if no movement occurs. At the same time, any increase in
volatility will help, while any decline will hurt. These characteristics are indicated by the risk measures associated with the position:

+Gamma (desire for movement in the underlying contract)

–Theta (the value of the position declines as time passes)

+Vega (the value of the position increases as implied volatility rises)
The characteristics of a short straddle are shown in Figure 11-2:

–Gamma (movement in the underlying contract will hurt the position)

+Theta (the value of the position increases as time passes)

–Vega (the value of the position increases as implied volatility falls)
Figure 11-1  Long straddle as time passes or volatility declines.
Lower underlying prices
Higher underlying prices
Position value
Buy calls and
puts at the same
exercise price
with the same
expiration date
+1 March 100 call
+1 March 100 put
Value at expiration
+1 June 40 call
+1 June 40 put
--- page 188 ---

V o l at i l i t y S p r e a d s 	 171
Straddles are most often executed one to one (one call for each put) using at-the-money options. When this is done, the spread will be approximately delta neutral because the delta values of the call and put will be close
to 50 and –50. A straddle can also be done with options that are either in
the money or out of the money. For example, with the underlying contract
trading at 100, we might buy the September 95 straddle. If the September
95 calls, which are in the money, have a delta of 75 and the September 95
puts, which are out of the money, have a delta of –25, the total delta will be
75 – 25 = 50, resulting in a bull straddle. If we want the straddle to be delta
neutral, we will need to adjust the number of contracts by purchasing three
puts for every call:

Buy 1 September 95 call (delta = 75).

Buy 3 September 95 puts (delta = –25).
This spread still qualifies as a straddle because we are buying calls and puts at
the same exercise price. But, more specifically, this is a ratio straddle because the
number of long market contracts (the calls) and the number of short market
contracts (the puts) are unequal.
Strangle
Like a straddle, a strangle consists of a long call and a long put (a long strangle)
or a short call and a short put (a short strangle), where both options expire
Figure 11-2  Short straddle as time passes or volatility declines.
Sell calls and
puts at the same
exercise price
with the same
expiration date
–1 March 100 call
–1 March 100 put
–1 June 40 call
–1 June 40 put
Value at expiration
Lower underlying prices
Higher underlying prices
Position value
--- page 189 ---

172
O P T I O N V O L AT I L I T Y A N D P R I C I N G
at the same time. But in a strangle the options have different exercise prices.
Typical long and short strangles are shown in Figures 11-3 and 11-4.
As with a straddle, strangles are most often done one to one (one call for
each put). In order to ensure that the position is delta neutral, exercise prices
are usually chosen so that the call and put deltas are approximately equal.
If a strangle is identified only by its expiration month and exercise prices,
there may be some confusion as to the specific options involved. A March
90/110 strangle might consist of a March 90 put and a March 110 call. But
it might also consist of a March 90 call and a March 110 put. Both strategies
are consistent with the definition of a strangle. To avoid confusion, a strangle is commonly assumed to consist of out-of-the-money options. If the underlying market is currently at 100 and a trader wants to purchase the March
90/110 strangle, everyone will assume that he wants to purchase a March 90
put and a March 110 call. Although both strangles have essentially the same
P&L profile, in-the-money options tend to be less actively traded than their outof-the-money counterparts. A strangle consisting of in-the-money options is
sometimes referred to as a guts.
Note that the risk characteristics of a strangle are similar to those of a
straddle:

Long strangle: +gamma/–theta/+vega

Short strangle: +gamma/–theta/+vega
A new option trader often finds long straddles and strangles attractive
because strategies with limited risk and unlimited profit potential offer great
appeal, especially when the profit is unlimited in both directions. However,
Figure 11-3  Long strangle as time passes or volatility declines.
+1 March 90 put
+1 March 110 call
Buy calls (puts)
at a higher
exercise price
Buy puts (calls)
at a lower
exercise price
All options must
have the same
expiration date
+1 June 35 put
+1 June 45 call
Value at expiration
Lower underlying prices
Higher underlying prices
Position value
--- page 190 ---

V o l at i l i t y S p r e a d s 	 173
if the hoped-for movement fails to materialize, a trader will find that losing
money, even a limited amount, can also be a painful experience. This is not
an endorsement of either long or short straddles. Under the right conditions,
either strategy may be sensible. But an intelligent trader needs to consider
not only whether the risk and reward is limited or unlimited but also the likelihood of the various outcomes. This, of course, is one important reason for
using a theoretical pricing model.
Butterfly
Thus far we have looked at spreads that involve buying or selling two different
option contracts. However, we can also construct spreads consisting of three,
four, or even more different options. A butterfly is a common three-sided spread
consisting of options with equally spaced exercise prices, where all options are
of the same type (either all calls or all puts) and expire at the same time. In a
long butterfly, the outside exercise prices are purchased and the inside exercise
price is sold, and vice versa for a short butterfly. Moreover, the ratio of a butterfly never varies. It is always 1 × 2 × 1, with two of each inside exercise price
traded for each one of the outside exercise prices. Typical long and short butterflies are shown in Figures 11-5 and 11-6.
To a new trader, a butterfly may look quite complex since it involves
three different options in different quantities. But butterflies have very simple
and well-defined characteristics that make them popular trading strategies.
Figure 11-4  Short strangle as time passes or volatility declines.
–1 March 90 put
–1 March 110 call
–1 June 35 put
–1 June 45 call
Sell puts (calls)
at a lower
exercise price
Sell calls (puts)
at a higher
exercise price
All options must
have the same
expiration date
Value at expiration
Lower underlying prices
Higher underlying prices
Position value
--- page 191 ---

174
O P T I O N V O L AT I L I T Y A N D P R I C I N G
Figure 11-5  Long butterfly as time passes or volatility declines.
+1 March 90 call (wing)
–2 March 100 calls (body)
+1 March 110 call (wing)
+1 June 35 put (wing)
–2 June 40 puts (body)
+1 June 45 put (wing)
Buy a call (put)
at a higher
exercise price
Buy a call (put)
at a lower
exercise price
All options must
have the same
expiration date
Sell two calls (puts)
at an intermediate
exercise price
There must be an equal
amount between
exercise prices
Value at expiration
Lower underlying prices
Higher underlying prices
Position value
Figure 11-6  Short butterfly as time passes or volatility declines.
Sell a call (put)
at a lower
exercise price
Sell a call (put)
at a higher
exercise price
All options must
have the same
expiration date
Buy two calls (puts)
at an intermediate
exercise price
–1 March 90 call (wing)
+2 March 100 calls (body)
–1 March 110 call (wing)
–1 June 35 put (wing)
+2 June 40 puts (body)
–1 June 45 put (wing)
Value at expiration
There must be an equal
amount between
exercise prices
Lower underlying prices
Higher underlying prices
Position value
