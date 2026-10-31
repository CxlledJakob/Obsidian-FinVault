# Option Volatility and Pricing_ Advanced Trading Strategies -- Sheldon Natenberg -- 2nd ed, 2014 -- McGraw Hill Professional -- isbn13 9780071818773 -- 6a48d008bd9beef283debf7bad0b2e4a -- Anna’s Archive.pdf — pages 286–305

--- page 286 ---

O p t i o n A r b i t r a g e 	 269
and
3.75 ≠ 4.00
Everyone will want to execute a reverse conversion by buying the less expensive synthetic (buy the call, sell the put) and selling the more expensive underlying (the futures contract). Ignoring transaction costs, if all trades actually can
be done at these prices, the strategy will result in an arbitrage profit of .25, the
amount of the mispricing.
What will be the result of everyone attempting to do a reverse conversion?
Because everyone wants to buy the call, there will be upward pressure on the
call price. If the call price rises to 5.50 while all other prices remain unchanged,
put-call parity is maintained because
5.50 – 1.50 = 104.00 – 100
Alternatively, as part of the reverse conversion, everyone wants to sell the put.
This will put downward pressure on the put price. If the put price falls to 1.25,
put-call parity is again maintained because
5.25 – 1.25 = 104.00 – 100
Finally, everyone wants to sell the futures contract, putting downward pressure on the futures price. If the futures contract falls to 103.75, put-call parity
is again maintained because
5.25 – 1.50 = 103.75 – 100
Whether the call price rises, the put price falls, the futures price falls, or some
combination of all three, the final result must be
C – P = F – X
This application of put-call parity, where all contracts are subject
to futures-type settlement, is typically used for options traded on futures
exchanges outside North America. When an exchange settles option prices at
the end of the trading day, there may be inconsistencies having to do with the
volatility value of an option. But the exchange will always try to assign settlement prices that are consistent with put-call parity. A table of settlement prices
for Euro-bund options traded on Eurex is shown in Figure 15-2.2 Note that in
every case, put-call parity is maintained.
Put-call parity calculations become slightly more complicated when
options on futures are subject to stock-type settlement, as they are on most
futures exchanges in North America. Now we must discount by the interestrate component
−
=
−
+ ×
C
P
F
X
r
t
1
2 The options in Figure 15-2 are in fact American and therefore entail the possibility of early exercise. However,
when options on futures are subject to futures-type settlement, as they are on Eurex, we will see in Chapter 16
that there is effectively no difference between a European and an American option.
--- page 287 ---

270
O P T I O N V O L AT I L I T Y A N D P R I C I N G
With six months remaining to expiration and an annual interest rate of
6.00 percent, a December 100 call is trading for 4.90. What should be the price
of the December 100 put if the underlying December futures contract is trading at 97.25? We know that
−
=
−
+
×
≈−
C
P
97.25 100
1
0.06
6/12
2.67
The difference between the call price and put price must be 2.67, with the negative sign indicating that the put price is greater than the call price
C – P = –2.67
P = C – (–2.67) = 4.90 + 2.67 = 7.57
The put must be trading for 7.57.
Locked Futures Markets
Many futures traders prefer not to become involved in options markets because
of the apparent complexity of options. There is, however, one situation in which
a futures trader ought to become familiar with basic option characteristics.
Figure 15-2  Settlement prices for Euro-bund options on May 25, 2010
Settlement prices for Euro-bund options on 25 May 2010.
The settlement prices reflect put-call parity in its simplest form.  In every case:
call price – put price  =  futures price – exercise price
June Futures = 129.38
September Futures = 128.90
exercise
price
June
calls
June
puts
July*
calls
July*
puts
Aug.*
calls
Aug.*
puts
Sep.
calls
Sep.
puts
126.00
3.39
.01
3.16
.26
3.45
.55
3.76
.86
126.50
2.89
.01
2.75
.35
3.07
.67
3.42
1.02
127.00
2.41
.03
2.37
.47
2.73
.83
3.09
1.19
127.50
1.93
.05
2.02
.62
2.40
1.00
2.78
1.38
128.00
1.48
.10
1.70
.80
2.10
1.20
2.50
1.60
128.50
1.06
.18
1.41
1.01
1.83
1.43
2.23
1.83
129.00
.71
.33
1.16
1.26
1.59
1.69
1.99
2.09
129.50
.43
.55
.94
1.54
1.37
1.97
1.76
2.36
130.00
.23
.85
.76
1.86
1.17
2.27
1.56
2.66
130.50
.12
1.24
.60
2.20
1.00
2.60
1.37
2.97
131.00
.05
1.67
.48
2.58
.85
2.95
1.21
3.31
131.50
.02
2.14
.37
2.97
.72
3.32
1.06
3.66
132.00
.01
2.63
.29
3.39
.61
3.71
.92
4.02
*July and August are serial months with no corresponding July or August futures.  The underlying contract for July,
August, and September options is the September futures contract.
--- page 288 ---

O p t i o n A r b i t r a g e 	 271
If a futures trader wants to make a trade but is prevented from doing so because
the futures market has reached its daily limit, he may be able to trade futures
synthetically by using options. The price at which the synthetic futures contact is
trading can be determined through put-call parity.
Consider a futures market that has a daily up or down limit of 5.00. The
futures contract closed the previous day at 126.75 but is now up limit at 131.75.
No further futures trading can take place unless someone is willing to sell at a
price of 131.75 or less. If, however, the options market is still open, a trader can
buy or sell futures synthetically, even if this price is beyond the daily limit. He
can either buy a call and sell a put (buying the futures contract) or sell a call and
buy a put (selling the futures contract) with the same exercise price and expiration date. The price of the call and put, together with the exercise price, will
determine the price at which the synthetic futures contract is trading.
Below is a hypothetical table of call and put prices together with the resulting synthetic futures price. For simplicity, we assume that there are no interest
considerations. Because C – P = F – X, we can calculate the equivalent futures
price F = C – P + X.
Exercise Price
Call Price
Put Price
Equivalent Synthetic Futures Price
(C – P + X  )
120
13.60
.35
133.25
125
9.35
1.05
133.30
130
5.75
2.55
133.20
135
3.15
4.95
133.20
140
1.55
8.30
133.25
145
0.70
12.40
133.30
There is some variation in the equivalent synthetic prices, possibly because
the prices do not reflect the bid-ask spread or perhaps because the option prices
have not been quoted contemporaneously. However, one can see that if the
futures contract were still open for trading, its price would probably be somewhere in the range of 133.20 to 133.30. If a futures trader wants to buy or sell
futures synthetically in the option market, he can expect to trade at a price
within this range.
Options on Stock
Calculating put-call parity for stock options entails an additional step because
we must first calculate the forward price for the stock. With six months remaining to expiration and an annual interest rate of 4.00 percent, a December 65 call
is trading for 8.00. If the underlying stock is trading at 68.50 and total dividends
of .45 are expected prior to expiration, what should be the price of the 65 put?
We begin with the forward price
F = 68.50 × (1 + 0.04 × 6/12) – 0.45 = 69.42
--- page 289 ---

272
O P T I O N V O L AT I L I T Y A N D P R I C I N G
Then
−
=
−
+
×
≈
C
P
69.42
65
1
0.04
6/12
4.33
The put price must be
8.00 – 4.33 = 3.67
An Approximation for Stock Options
When exchanges first began trading options, all activity took place in an openoutcry environment. Traders often had to make pricing decisions quickly and
without the aid of computers. As a result, they often sought shortcuts by which
they could more easily approximate prices. Even if the shortcut resulted in
small errors, the value of being able to make faster decisions more than offset
the small loss in accuracy.
Let’s go back to basic put-call parity for stock options and replace the forward price F with the actual forward price for the stock
−
=
−
+ ×
≈
×
+ ×
−
−
+ ×
C
P
F
X
r
t
S
r
t
D
X
r
t
1
[
(1
)
]
1
How might we simplify this calculation?
Note that we are multiplying the stock price by the interest-rate component and then dividing the stock price, the dividend, and the exercise price by
the same interest-rate component. We end up with the stock price itself less the
discounted values of the dividend and exercise price
C
P
S
D
r
t
X
r
t
(1
)
(1
)
−
=
−
+ ×
−
+ ×
Dividends are typically small compared with the stock price and exercise price,
so a reasonable approximation for the discounted value of the dividend is simply the dividend D itself. We might approximate the discounted value of the
exercise price and eliminate the need to do any division by subtracting the interest on the exercise price from the exercise price itself
D
r
t
D
X
r
t
X
X
r
t
1
1
+ ×
≈
+ ×
≈
−
× ×
Substituting our approximations into the put-call parity equation, we have
C – P ≈ S – (X – X × r × t ) – D = S – X + X × r × t – D
The difference between the call price and put price is approximately equal to
the stock price minus the exercise price plus interest on the exercise price minus
expected dividends.
How good an approximation is this? Clearly, if interest rates are very high,
the dividend is very large, or we are dealing with long-term options, the errors
will begin to increase. But for short-term options our approximation often represents a reasonable tradeoff between speed and accuracy.
--- page 290 ---

O p t i o n A r b i t r a g e 	 273
Let’s go back to our previous stock option example:
Stock price = 68.50
Time to expiration = 6 months
Interest rate = 4.00 percent
Expected dividends = .45
We calculated the value of the 65 combo (C – P) as 4.33. How will our approximation compare?

C – P ≈ S – X + X × r × t – D

= 68.50 – 65 + 65 × .04 × 6/12 – .45

= 4.35
Our approximation differs by .02 from the true value. Depending on market
conditions, this might be an acceptable margin of error in return for being able
to make a faster trading decision.
All experienced traders are familiar with put-call parity, so any price imbalances are likely to be very short-lived. If the combo is overpriced compared
with the underlying, all traders will want to execute a conversion (i.e., buy the
underlying, sell the call, buy the put). If the combo is underpriced, all traders
will want to execute a reversal (i.e., sell the underlying, buy the call, sell the put).
Such activity, where everyone is attempting to do the same thing, will quickly
force prices back into equilibrium. Indeed, price imbalances in the synthetic
relationship are usually small and rarely last for more than a few seconds.
When imbalances do occur, an option trader is usually willing to execute conversions or reversals in very large size because of the low risk associated with
such strategies.
Put-call parity specifies the price relationship between three contracts—
a call, a put, and an underlying contract. If the price of any two contracts is
known, it should be possible to calculate the price of the third contract. If the
prices in the marketplace do not seem to be consistent with this relationship,
what might a trader infer?
Consider this stock option situation:

90 call = 7.20

90 put = 1.40

Time to expiration = 3 months

Interest rate = 8.00 percent

Expected dividends = .47
What should be the price of the underlying stock?
Using our stock option approximation for put-call parity, we know that
C – P ≈ S – X + X × r × t – D
Therefore,

S ≈ C – P + X – X × r × t + D

S ≈ 7.20 – 1.40 + 90 – 90 × 0.08 × 3/12 + 0.47 = 94.47
--- page 291 ---

274
O P T I O N V O L AT I L I T Y A N D P R I C I N G
Suppose, however, that the stock is actually trading at 94.30. Does this mean
that there is an arbitrage opportunity?
The stock price calculation depended on assumptions about interest and
dividends. Are we sure that those assumptions are correct? One possibility is
that the interest rate we are using, 8 percent, is too low. If we assume that the
contract prices and dividends are correct, we can calculate the implied interest rate
=
−
−
+
+
=
−
−
+
+
=
r
C
P
S
X
D
X
t
(
)/
(7.20
1.40
94.30
90
0.47)/90
3/12
0.0875 (8.75%)
Another possibility is that the dividend we are using, .47, is too high. If we
assume that the contract prices and interest are correct, we can calculate the
implied dividend

D = S – C + P – X + X × r × t

              = 94.30 – 7.20 + 1.40 – 90 + 90 × .08 × 3/12

              = .30
The marketplace seems to be expecting a dividend of only .30. If our original
calculation was based on an estimate of the expected divided, we ought to consider the possibility that the company will cut the dividend prior to expiration.
Arbitrage Risk
New traders who are learning to trade options professionally are often encouraged to focus on conversions and reversals because, they are told, these strategies, once executed, are essentially riskless. A word of warning: very few strategies
are truly riskless. Some strategies entail greater risk, while others entail lesser risk.
Rarely, however, does a strategy entail no risk. The risks of doing conversions
or reversals may not be immediately apparent, but they exist nonetheless.
Execution Risk
Because no one wants to give away money, a trader is unlikely to be offered a
profitable conversion or reversal all at one time. Consequently, a trader who
focuses on these strategies will have to begin by executing one or two legs and
then hope to execute the final leg(s) at a later time. He may, for example, initially purchase puts together with underlying contracts and hope to later complete the conversion by selling calls. However, if call prices begin to fall, he may
never be able to profitably complete the conversion. Even a professional trader
on an exchange, who would seem to be in a good position to know the prices of
all three contracts, can be mistaken. He may create a long synthetic underlying
position by purchasing a call and selling a put at what he believes are favorable
--- page 292 ---

O p t i o n A r b i t r a g e 	 275
prices. However, when he tries to sell the underlying contract to complete the
reversal, he may find that the price is lower than he expected. Whenever a strategy is executed one leg at a time, there is always the risk of an adverse change
in prices before the strategy can be completed.
Pin Risk
When we introduced the concept of a synthetic position, we assumed that at
expiration, the underlying market would be either above the exercise price, in
which case the call would be exercised, or below the exercise price, in which
case the put would be exercised. But what will happen if the underlying market
is exactly equal to, or pinned to, the exercise price at the moment of expiration?
Suppose that a trader has executed a June 100 conversion: he is short a
June 100 call, long a June 100 put, and long the underlying contract. If the underlying contract is above or below 100 at expiration, there is no problem. Either he will be assigned on the call or he will exercise the put. In either case, the
long underlying position will be offset, and he will have no market position on
the day following expiration.
But suppose that at the moment of expiration, the underlying market is
right at 100. The trader would like to be rid of his underlying position. If he
is not assigned on the call, he can exercise his put; if he is assigned on the call,
he can let the put expire. In order to make a decision, he must know whether
the call will be exercised. But he won’t know this until the day after expiration,
when he either does or does not receive an assignment notice. If he finds out
that he was not assigned on the call, it will be too late to exercise the put because it will have expired.
It may seem that an option that is exactly at the money at expiration will
never be exercised because, in theory, it has no value. In fact, many at-themoney options are exercised. Even though the option has no theoretical value,
it does have some practical value. For example, suppose that the owner of a
call that is exactly at the money at expiration wants to take a long position in
the underlying contract. He has two choices. He can either exercise the call or
buy the underlying contract. Because an exchange-traded option typically includes the right of exercise in the original transaction cost, it is almost always
cheaper to exercise the call. Even if there is a small transaction cost to exercise, an option, it will almost always be less than the cost of trading the underlying contract. Anyone owning an at-the-money option and choosing to take
a long or short position at expiration will find that it is cheaper to exercise the
option than to buy or sell the underlying contract.
Clearly, a trader who is short an at-the-money option at expiration has a
problem. What can he do? One possibility is to make an educated guess as to
whether the at-the-money option will be exercised. If the market appears to
be strong on the last trading day, the trader might assume that it will continue
higher following expiration. If the holder of the call sees the situation similarly, it is logical to assume that the call will be exercised. Hence the trader will
choose not to exercise his put. Unfortunately, if the trader is wrong and he does
not get assigned on the call, he will find himself with a long underlying position
--- page 293 ---

276
O P T I O N V O L AT I L I T Y A N D P R I C I N G
that he would rather not have. Conversely, if the market appears to be weak on
the last trading day, the trader might make the assumption that he will not be
assigned on the call. He will therefore choose to exercise the put. But, again, if
he is wrong and does get an assignment notice, he will find himself with an unwanted short underlying position on the day following expiration.
The risk of a wrong guess can be further compounded by the fact that conversions and reversals, because of their low risk, are often done in large size.
If the trader guesses wrong, he may find that on the day after expiration, he is
naked long or short not one or two but many underlying contracts.
There can be no certain solution to the problem of pin risk. With many,
perhaps thousands, of open contracts outstanding, some at-the-money options
will be exercised and some won’t. If the trader lets the position go to expiration and relies on luck, he is at the mercy of the fates, and this is a position that
an intelligent option trader prefers to avoid. The practical solution is to avoid
carrying a short at-the-money option position to expiration when there is a
real possibility of expiration right at the exercise price. If the trader has a large
number of June 100 conversions or reversals and expiration is approaching
with the underlying market close to 100, the sensible course is to reduce the pin
risk by reducing the size of the position. If the trader doesn’t reduce the size,
he may find that he is under increasing pressure to get out of a large number of
risky contracts as expiration approaches.
Sometimes even a careful trader will find that he still has some outstanding
at-the-money conversions or reversals as expiration approaches. If he is very
concerned with the potential pin risk, he might simply liquidate the position at
the prevailing market prices. Unfortunately, this is likely to result in a loss because the trader will be forced to trade each contract at an unfavorable price,
either buying at the offer or selling at the bid. Fortunately, it is often possible to
trade out of such a position all at once at a fair price.
Because conversions and reversals are common strategies, a trader who has
an at-the-money conversion and is worried about pin risk can be fairly certain
that there are also traders in the market who have at-the-money reversals and
are worried about the same pin risk. If the trader with the conversion could
find a trader with a reversal and cross positions with him, both traders would
eliminate the pin risk associated with their positions. This is why on option exchanges one often finds traders looking for other traders who want to trade
conversions or reversals at even money. This simply means that a trader wants
to trade out of his position at a price that is fair to everyone involved so that everyone can avoid the problem of pin risk. Whatever profit a trader expected to
make from the conversion or reversal presumably resulted from the opening
trade, not from the closing trade.
Pin risk only occurs in option markets where exercise results in a long or
short position in the underlying contract. In some markets, such as stock indexes, options are settled at expiration in cash rather than with the delivery of
an underlying contract. When the option expires, there is a cash payment equal
to the difference between the exercise price and underlying price, but no underlying position results. Consequently, there is no pin risk associated with this
type of settlement.
--- page 294 ---

O p t i o n A r b i t r a g e 	 277
Settlement Risk
Let’s go back to our December 100 conversion example. But now let’s assume
that the underlying is a December futures contract

–1 December 100 call

+1 December 100 put

+1 December futures contract
If the December futures contract is trading at 102.00, there are three months
remaining to December expiration, interest rates are 8.00 percent, and all
options are subject to stock-type (cash) settlement, the value of the December
100 synthetic combination (the difference between the December 100 call and
the December 100 put) should be
−
+
×
=
102 100
1
8%
3/12
1.96
Suppose that a trader is able to sell a December 100 call for 5.00, buy a
December 100 put for 3.00, and sell a December futures contract for 102.00.
At expiration, the trader should realize a profit of .04 because he has done the
December 100 conversion at .04 better than its value.
Shortly after the trader executes the conversion, the underlying December futures contract falls to 98.00. What will be the cash flow? The synthetic
position will show a profit of approximately 4.00; the short call and long put
together, because they make up a short underlying position, will appreciate by
4.00. But because the options are settled like stock, the profit on the synthetic
position will be unrealized—there will be no cash credited to the trader’s account. On the other hand, the trader is also long a December futures contract,
and this contract, because it is subject to futures-type settlement, will result
in an immediate debit of 4.00 when the market drops to 98.00. To cover this
debit, the trader must either borrow the money or take the money out of an
interest-bearing account. In either case, there will be a loss in interest, and this
interest loss will not be offset by the unrealized profit from the option position.
If the loss in interest is great enough, it may more than offset the profit of .04
that the trader originally expected from the position. In the most extreme case,
where the trader does not have access to the funds required to cover the variation on the futures position, he may be forced to liquidate the position. Needless
to say, forced liquidations are never profitable.
Of course, this works both ways. A rise in the price of the underlying futures contract to 106.00 will result in a loss of 4.00 on the synthetic option
position; the short call and long put together will decline by 4.00. But this loss
is unrealized—no money will actually be debited from the trader’s account.3
On the other hand, the rise in the futures contract will result in an immediate
cash credit on which the trader can earn interest. This interest will increase
the potential profit beyond the expected amount of .04.
3 There may be a margin requirement associated with changes in the option prices. But, as discussed in
Chapter 1, margin deposits, in theory, belong to the trader and therefore entail no loss of interest.
--- page 295 ---

278
O P T I O N V O L AT I L I T Y A N D P R I C I N G
Option traders tend to assume that conversions and reversals are deltaneutral strategies. But this is not always true. An exactly delta-neutral position
has no preference as to the direction of movement in the underlying contract.
In our example, we can see that the trader prefers upward movement because
he can earn interest on the variation credited to his account. With the underlying futures contract at 102, the deltas in our example might be
Contract Position
Delta Position
Short December 100 call
   –57
Long December 100 put
   –41
Long December futures contact
+100
Total
    +2
The two extra deltas reflect the fact that the trader prefers the market to rise
rather than fall so that cash will flow into his account from the futures position.
The interest from this cash flow can result in an unexpected profit. A decline
in the futures price will have the opposite effect and can result in an unexpected loss.
Under normal circumstances, few traders will concern themselves with the
risk of being two deltas long or short. But conversions and reversals, because
they are low-risk strategies, are often done in very large size. A trader who executes 300 of our sample conversions has a delta risk of 300 × +2 = +600. This
is the same as being long an extra six futures contracts. The risk comes from the
interest that can be earned on any cash credit or that must be paid on any cash
debit resulting from movement in the underlying futures contract.
The amount by which the delta of a synthetic futures position will differ
from 100 depends on the interest risk associated with the position. This, in turn,
depends on two factors—the general level of interest rates and the amount of
time remaining to expiration. The higher the interest rate and the more time
remaining to expiration, the greater the risk. The lower the interest rate and
the less time remaining to expiration, the less the risk. A 10 percent interest rate
with nine months remaining to expiration represents a much greater risk than
a 4 percent interest rate with one month remaining to expiration. In the former
case, the deltas of a synthetic position may add up to 93, while in the latter case
the deltas may add up to 99. In general, the total delta for a synthetic futures
contract, where the options are subject to stock-type settlement, is
+ ×
r
t
100
1
where r is the interest rate and t is the time to maturity of the options.
This type of settlement risk occurs only when the options and the underlying
contract are subject to different settlement procedures.4 There is no settlement
4 A similar type of settlement risk occurs when a futures contract is used to hedge a physical commodity or
security position. When the value of the physical commodity or security rises or falls, any profit or loss is unrealized. But the profit or loss on the futures position is immediately realized in the form of variation. The
correct hedge is therefore not one to one but is determined by the interest on the variation from the futures
position. Hedgers sometime refer to this risk as tailing.
--- page 296 ---

O p t i o n A r b i t r a g e 	 279
risk when both contracts are subject to the same settlement procedure. If all
contracts are subject to stock-type settlement, as they are in a typical stock option market, no cash flow results from fluctuations in the prices of the contracts
prior to expiration. If all contracts are subject to futures-type settlement, as
they are on most futures exchanges outside the United States, any cash flow resulting from changes in the price of the underlying futures contract will exactly
offset the cash flow resulting from changes in prices of the option contracts.
Interest and Dividend Risk
Let’s again go back to our December 100 conversion, but now let’s assume that
the underlying contract is stock.

–1 December 100 call

+1 December 100 put

+1 stock contract
What are the risks of holding this position?
The stock price will always be greater than the option prices, so the entire position will be done for a debit approximately equal to the option’s exercise price. Because the trader will have to borrow this amount, there will be
an interest cost associated with the position. If interest rates rise over the life
of the position, the interest costs will also rise, increasing the cost of holding
the position and, consequently, reducing the potential profit. If interest rates
fall, the potential profit will increase because the costs of carrying the position
will decline.5
The opposite is true of a reverse conversion:

+1 December 100 call

–1 December 100 put

–1 stock contract
Because the trader will receive cash from the sale of the stock, the position will
earn interest over time. If interest rates rise, the interest earnings will also rise,
increasing the value of the position. If interest rates fall, the interest earnings
will fall, reducing the value of the position.
Clearly, conversions and reverse conversions are sensitive to changes in
interest rates. This is reflected in their rho values. In the stock option market,
a conversion has a negative rho, indicating a desire for interest rates to fall. A
reverse conversion has a positive rho, indicating a desire for interest rates to
rise. This is logical when we recall that in the stock option market calls have
positive rho values and puts have negative rho values. In a conversion or reverse conversion, the signs of the call and the put rho positions will be the
same, either both positive or both negative, because we are buying one option
and selling the other.
5 In theory, a trader can borrow money at a fixed rate, eliminating any interest-rate risk. In practice, however,
traders usually finance their trading activities through their broker or clearing firm at a variable rate. The cost
of borrowing or lending changes daily as interest rates rise or fall.
--- page 297 ---

280
O P T I O N V O L AT I L I T Y A N D P R I C I N G
The fact that a conversion or reverse conversion includes a stock position
also means that there is the risk of rising or falling dividends. In a conversion,
we are long stock, so any increase in dividends will increase the value of the position, and any cut in dividends will reduce the value. In a reverse conversion,
the opposite is true.
Even though there is no Greek letter used to represent dividend risk, we
might say that a conversion has positive dividend risk and a reverse conversion has
negative dividend risk. The former will be helped by any increase in dividends,
while the latter will be hurt.
We can see the effect of changing interest and dividends by recalling our
earlier example:

Stock price = 68.50

Time to expiration = 6 months

Interest rate = 4.00 percent

Expected dividend = .45
We calculated the approximate value of the combo (C – P) as 4.35

C – P ≈ S – X + X × r × t – D

                    = 68.50 – 65 + 65 × .04 × 6/12 – .45

                    = 4.35
If interest rates rise to 5.00 percent, the value will now be
68.50 – 65 + 65 × .05 × 6/12 – .45 ≈ 4.68
If, on the other hand, the dividend is increased to .65, the value will be
68.50 – 65 + 65 × .04 × 6/12 – .35 = 4.15
A conversion or reversal entails risk because these strategies combine a
synthetic underlying position, which is composed of options, with an actual position in the underlying contract. The risk arises because a synthetic position
and the actual position, while very similar, can still have different characteristics, either in terms of settlement procedure, as in the futures option market, or
in terms of interest or dividends, as in the stock option market. Is there any way
to eliminate this risk?
One way to eliminate this risk is to eliminate the position in the underlying
contract. Consider a conversion:

Short a call

Long a put

Long an underlying contract
If we want to maintain this position but would also like to eliminate the risk of
holding an underlying position, we might replace the long underlying position
with something that acts like an underlying contract but that isn’t an underlying contract. One possibility is to replace the long underlying position with a
deeply in-the-money call:
--- page 298 ---

O p t i o n A r b i t r a g e 	 281

Short a call

Long a put

Long a deeply in-the-money call
If the deeply in-the-money call has a delta of 100 and therefore acts like a long
underlying contract, the position will have the same characteristics as the conversion.
In the same way, instead of buying a deeply in-the-money call, we can sell
a deeply in-the-money put:

Short a call

Long a put

Short a deeply in-the-money put
This type of position, where the underlying instrument in a conversion or reversal is replaced with a deeply in-the-money option, is known as a three-way.
Although it eliminates some risks, a three-way is not without its own problems.
If a trader sells a deeply in-the-money option to complete a three-way, he still
has the risk of the market going through the exercise price. Indeed, as the underlying market moves closer and closer to the exercise price of the deeply inthe-money option, that option will act less and less like an underlying contract,
and the entire position will act less and less like a true conversion or reversal.
Boxes
What else acts like an underlying contract but isn’t an underlying contract? Another possibility is to replace the underlying position with a synthetic position,
but a synthetic with a different exercise price. For example, suppose that we
have a June 100 conversion:

–1 June 100 call

+1 June 100 put

+1 underlying contract
At the same time, we also execute a June 90 reversal. The combined position is

+1 June 90 call
–1 June 100 call

–1 June 90 put
+1 June 100 put

–1 underlying contract
+1 underlying contract
The long and short underlying contracts cancel out, leaving

+1 June 90 call
–1 June 100 call

–1 June 90 put
+1 June 100 put
We have a synthetic long underlying position at the 90 exercise price and a
synthetic short underlying position at the 100 exercise price. This position,
known as a box, is similar to a conversion or reversal except that we have eliminated the risk associated with holding a position in the underlying contract. A
trader is long the box when he is synthetically long at the lower exercise price
and synthetically short at the higher exercise price. He is short the box when
--- page 299 ---

282
O P T I O N V O L AT I L I T Y A N D P R I C I N G
he is synthetically short at the lower exercise price and synthetically long at the
higher exercise price. The example position is long a June 90/100 box.
Like a conversion or reversal, a box is an arbitrage—we are buying and
selling the same contract but in different markets. In our example, we are buying the underlying contract in the 90 exercise price market and selling the same
underlying contract in the 100 exercise price market.
How much is a box worth? Ignoring pin risk, at expiration, a trader who
has a box will simultaneously buy the underlying contract at one exercise price
and sell the underlying contract at the other exercise price. The value of the
box at expiration will be exactly the amount between exercise prices. In our example, at expiration, the 90/100 box will be worth exactly 10.00 because the
trader will simultaneously buy the underlying contract at 90 (exercise the 90
call or be assigned on the 90 put) and sell the underlying contract at 100 (exercise the 100 put or be assigned on the 100 call). If the box is worth 10.00 at expiration, how much is it worth today? If the options are subject to futures-type
settlement, the value today is the same as the value at expiration. If, however,
the options are subject to stock-type settlement, the value of the box today will
be the present value of the amount between exercise prices. If our 90/100 box
expires in three months with interest rates at 8 percent, the value today is
+
×
≈
10.00
1 3/12
8%
9.80
Because a box eliminates the risk associated with carrying a position in the
underlying contract, boxes are even less risky than conversions and reversals,
which are themselves low-risk strategies. When all options are European (there is
no risk of early exercise) and the options are settled in cash rather than through
delivery of the underlying contract (there is no pin risk), the purchase or sale of a
box is identical to lending or borrowing funds over the life of the options. In our
example, a trader who sells the 90/100 box for 9.80 has essentially borrowed
funds from the buyer of the box for three months at an interest rate of 8 percent.
Selling the box at a lower price is equivalent to borrowing funds at a higher interest rate. If the trader sells the three-month box at a price of 9.70, he has, in
effect, agreed to borrow at an annual interest rate of 12 percent.
When no other method is available, a trading firm may be able to raise
needed short-term cash by selling boxes. Because the firm will probably have
to sell the boxes at a price lower than the theoretical value, this will increase the
firm’s borrowing costs. Moreover, there will still margin requirements and transaction costs associated with this strategy, increasing the borrowing costs further.
We originally introduced a box as a conversion at one exercise price and a
reversal at a different exercise price. With the long and short underlying positions canceling out, we are left with two synthetic underlying positions:

+1 June 90 call
–1 June 100 call

–1 June 90 put
+1 June 100 put
The left side of the box is a synthetic long position at 90, and the right side is
a synthetic short position at 100. Instead of dividing the box into a right side
and a left side, suppose that we divide it into upper portion and a lower portion:
--- page 300 ---

O p t i o n A r b i t r a g e 	 283

+1 June 90 call/–1 June 100 call

–1 June 90 put/+1 June 100 put
The strategy on the top is a bull vertical call spread (i.e., long June 90 call, short
June 100 call), whereas the strategy on the bottom is a bear vertical put spread
(i.e., long June 100 put, short June 90 put). Because a box is a combination of
two vertical spreads, the combined prices of the vertical spreads must equal the
value of the box.
With three months remaining to expiration and interest rates at 8 percent,
the value of our June 90/100 box is 9.80. Suppose that a trader knows that the
June 90/100 call spread is trading for 6.00. The trader can estimate the fair
market price for the June 90/100 put spread because he knows that the 90/100
box is worth 9.80 and that the value of a call and put spread must add up to the
value of the box. The price of the put spread must therefore be
9.80 – 6.00 = 3.80
If the trader believes that he can either buy or sell the call spread for 6.00 and
he is asked for a market in the put spread, he will make his market around
an assumed value of 3.80. He might, for example, make a market of 3.70
bid/3.90 ask. If he is able to buy the put spread for 3.70, he can then try to buy
the call spread for 6.00. If he is successful, he will have paid a total of 9.70 for
a box with a theoretical value of 9.80. Conversely, if he is able to sell the put
spread for 3.90, he can then try to sell the call vertical for 6.00. If he is successful, he will have sold a box with a theoretical value of 9.80 for a price of 9.90.
Rolls
In a box, the risk of holding the underlying contract is offset by combining a
conversion and reversal in the same month but at different exercise prices:

+1 June 90 call
–1 June 100 call

–1 June 90 put
+1 June 100 put

–1 underlying contract
+1 underlying contract
Suppose that we instead combine a conversion and reversal, not at different
exercise prices, but in different expiration months:

+1 June 90 call
–1 August 90 call

–1 June 90 put
+1 August 90 put

–1 underlying contract
+1 underlying contract
If the long and short underlying positions cancel out, we are left with a roll:

+1 June 90 call
–1 August 90 call

–1 June 90 put
+1 August 90 put
We have a synthetic long underlying position in June and a synthetic short underlying position in August, where both positions have the same exercise price.
Although it is always possible to combine a conversion in one month with a
reversal in a different month, in a roll, the underlying positions must cancel out.
--- page 301 ---

284
O P T I O N V O L AT I L I T Y A N D P R I C I N G
For example, in a futures option market, the underlying for June may be a June
futures contract and the underlying for August may be an August futures contract. Because they are different contracts, the long and short underlying positions will not offset each other. Hence the position is not a true roll.
Rolls are done most commonly in a stock option market, where the underlying contract for all expiration months is the same underlying stock. The long
stock position in one expiration month will always offset the short stock position
in the other expiration month.
What should be the value of a roll in the stock option market? The value of
the roll must be the difference in the values of the combos
(Cl – Pl) – (Cs – Ps)
where Cl and Pl are the long-term call and put, and Cs and Ps are the short-term
call and put.
For the moment, let’s assume that the stock pays no dividends. We know
the value of a combo
−
=
−
+ ×
C
P
S
X
r
t
1
The value of the roll should therefore be
−
+
×



−
−
+
×



=
+
×
−
+
×
S
X
r
t
S
X
r
t
X
r
t
X
r
t
(1
)
(1
)
(1
)
(1
)
l
l
s
s
s
s
s
s
Excluding dividends, the value of the roll is the difference between the discounted values of the exercise price. Note that the value of the roll depends
on two different interest rates—rs, the interest to short-term expiration, and rl,
the interest to long-term expiration. These rates are usually very similar, which
means that the preceding expression is almost always a positive number because the discounting on the short-term exercise price is less than the discounting on the long-term exercise price.
If the stock pays a dividend D between expirations, the value of the roll
should also include this amount. Ignoring interest on dividends, the roll value is
+
×
−
+
×
−
X
r
t
X
r
t
D
(1
)
(1
)
s
s
l
l
Consider our June/August 90 roll, with two months to June expiration and
four months to August expiration. If we assume a constant interest rate of 6
percent, and the stock is expected to pay a dividend of .40 between expirations,
the value of the 90 roll is
+
×
−+
×
−
=
−
−
=
90
1
0.06
2/12
90
1
0.06
4/12
0.40
89.11
88.24
0.40
0.47
A trader who needs to make calculations without computer supportmight,
as with conversions and reversals, might be willing to give up some accuracy in
return for greater speed. How might a trader simplify the calculation of a roll?
--- page 302 ---

O p t i o n A r b i t r a g e 	 285
A trader who is short a roll (i.e., long the short-term synthetic and short the
long-term synthetic) will buy stock at the short-term expiration and sell stock at
the long-term expiration, with both transactions taking place at the same exercise price. Additionally, because the trader will own the stock over the life of the
roll, he will receive any dividends paid out over this period. The value of the
roll should be approximately the cost of carrying the exercise price from one
expiration to the other less any dividends that accrue
X × r × t – D
where t is the time between expirations. In our example, we have
90 × .06 × 2/12 – .40 = .90 – .40 = .50
Depending on the trading environment and the trader’s ultimate goal, this error
of .03 may or may not be acceptable.
Instead of writing a roll as a combination of synthetic long and short
underlying positions, we can also write the roll as a combination of calendar
spreads:

–1 June 90 call/+1 August 90 call

+1 June 90 put/–1 August 90 put
The strategy on the top is a long call calendar spread; the strategy on the bottom is a short put calendar spread. If we buy the call calendar spread and sell
the put calendar spread, we have a roll. The value of the roll should therefore
be equal to the difference between the two calendar spreads.6
Because the interest component is almost always greater than dividends, a
long roll (i.e., buy the long-term synthetic, sell the short-term synthetic) will typically trade for a positive value, requiring an outlay of cash. Consequently, the
call calendar spread will be more valuable than the put calendar spread. However, if dividends are greater than interest, a roll can have a negative value.7
Then the normal relationship will be inverted: the put calendar spread will be
more valuable than the call calendar spread.
In our earlier example, we calculated the value of the June/August 90
roll as .47. Suppose that the June/August 90 call calendar spread is trading for
2.25. What should be the value of the June/August 90 put calendar spread? We
know that the difference between the spreads must be .47. The value of the put
spread ought to be
2.25 – .47 = 1.78
In the same way, if the put spread is trading for 1.50, the call spread ought to
be trading for
1.50 + .47 = 1.97
6 Note that the value of a box is equal to the sum of two spreads, a bull spread and a bear spread, while the
value of a roll is equal to the difference between two spreads, a call calendar spread and a put calendar spread.
7 Traders need to be careful about what they mean by buying and selling. Usually, buying means paying some
amount (a cash debit), while selling means receiving some amount (a cash credit). With some strategies, however, it may not be clear whether the trader is paying or receiving. Rolls are an example of this.
--- page 303 ---

286
O P T I O N V O L AT I L I T Y A N D P R I C I N G
Because dividends are discrete amounts that apply equally to all rolls with
the same expiration dates, the values of rolls with the same expiration date but
different exercise prices should differ by approximately the interest on exercise
prices. In our example, the value of the June/August 90 roll was .47. The value
of the June/August 80 roll should differ from the value of the 90 roll by the interest on the difference between 80 and 90
0.47 – (90 – 80) × .06 × 2/12 = .47 – .10 = 0.37
Whiles a trader may execute a roll with the intention of eliminating the
risk of holding the underlying contract, this risk is only eliminated up to the
short-term expiration. At that time, the trader will either buy or sell the underlying stock at the exercise price. The position is therefore sensitive to changes in
interest rates and dividends. Rolls fluctuate in value as interest rates rise or fall
and as dividends are raised or lowered. The more time between expirations,
the more sensitive a roll will be to these changes.
Time Boxes
A box or roll consists of long and short synthetic positions, either in the same
month but at different exercise prices (a box) or in different months but at the
same exercise price (a roll). We can also combine these strategies by taking synthetic positions at different exercise prices and in different months:

+1 June 90 call
–1 August 100 call

–1 June 90 put
+1 August 100 put
This position is usually referred to as either a time box or diagonal roll.
We can calculate the value of a time box in the same way we calculated the
value of a roll—by taking the difference between the discounted exercise prices
less expected dividends
+
×
−
+
×
−
X
r
t
X
r
t
D
(1
)
(1
)
s
s
s
l
l
l
where the subscripts s and l refer to short-term options and long-term options.
What should be the value of the June 90/August 100 time box if there are
two months to June expiration and four months to August expiration, interest
rates are a constant 6 percent, and the stock is expected to pay a dividend of
.40 over this period?
+
×
−
+
×
−
=
−
−
= −
X
r
t
X
r
t
D
(1
)
(1
)
90
1.01
100
1.02
0.40
9.33
s
s
s
l
l
l
The negative sign indicates that if a trader wants to put on this position, he
will have to pay 9.33. This is logical because the position consists of buying the
lower-exercise-price synthetic (i.e., buy the underlying at 90 at June expiration)
and selling the higher-exercise-price synthetic (i.e., sell the underlying at 100 at
August expiration).
--- page 304 ---

O p t i o n A r b i t r a g e 	 287
In the same way that boxes are made up of bull and bear spreads and rolls
are made up of calendar spreads, time boxes are made up of diagonal spreads.
We can write our time box as two diagonal spreads:

+1 June 90 call/–1 August 100 call

–1 June 90 put/+1 August 100 put
Are we paying or receiving money for each of these spreads? We are
clearly paying for the put spread because the August 100 put will always be
more valuable than the June 90 put. But it’s not clear what the cash flow is for
the call spread. The lower exercise price seems to imply that the June call will
be more valuable, but the greater amount of time might in fact make the August call more valuable. The values of the call options will depend on both the
underlying price and volatility. In some cases, we may pay for the call spread; in
other cases, we may be paid. Regardless of the prices of the individual spreads,
though, the total debit must be 9.33. If the call spread is trading for 3.50, the
put spread ought to be trading for 9.33 – 3.50 = 5.83. If the put spread is trading for 7.75, the call spread ought to be trading for 9.33 – 7.75 = 1.58.
Because a time box is a combination of a box and a roll, if we can value
a box and a roll, we ought to be able to value a time box. Suppose that we buy
the June 90/100 box

+1 June 90 call
–1 June 100 call

–1 June 90 put
+1 June 100 put
and at the same time sell the June/August 100 roll

+1 June 100 call
–1 August 100 call

–1 June 100 put
+1 August 100 put
The long and short June 100 synthetics cancel out, leaving the June 90/August
100 time box:

+1 June 90 call
–1 August 100 call

–1 June 90 put
+1 August 100 put
The time box must therefore be a combination of buying the June 90/100 box
and selling the June/August 100 roll.
Similarly, suppose that we buy the August 90/100 box

+1 August 90 call
–1 August 100 call

–1 August 90 put
+1 August 100 put
and at the same time sell the June/August 90 roll

+1 June 90 call
–1 August 90 call

–1 June 90 put
+1 August 90 put
The long and short August 90 synthetics cancel out, again leaving the June 90/
August 100 time box:

+1 June 90 call
–1 August 100 call

–1 June 90 put
+1 August 100 put
--- page 305 ---

288
O P T I O N V O L AT I L I T Y A N D P R I C I N G
In this case, the time box is a combination of buying the August 90/100 box
and selling the June/August 90 roll.
From the foregoing examples, we can see that if we buy a long-term box
and sell a lower-exercise-price roll or buy a short-term box and sell a higherexercise-price roll, both combinations result in the same time box. We can confirm this by calculating the value of the June and August 90/100 boxes as well
as the June/August 90 and 100 rolls
=
+
×
=
June 90/100 box
10
1
0.06
2/12
9.90
=
+
×
=
August 90/100 box
10
1
0.06
4/12
9.80
=
+
×
−+
×
−
=
June/August 90 roll
90
1
0.06
2/12
90
1
0.06
4/12
0.40
0.47
=
+
×
−+
×
−
=
June/August 100 roll
100
1
0.06
2/12
100
1
0.06
4/12
0.40
0.57
If we buy the June 90/100 box and sell the June/August 100 roll, the total
value is
–9.90 + .57 = –9.33
If we buy the August 90/100 box and sell the June/August 90 roll, the total
value is
–9.80 + .47 = –9.33
The total in both cases is equal to the value of the time box.
Using Synthetics in Volatility Spreads
Any mispriced arbitrage relationship will be quickly recognized by almost all
traders. Consequently, there are few opportunities to profit from a mispriced
conversion or reversal. When a mispricing does arise, it is likely to be small and
very short-lived. Only a professional trader, who has low transaction costs and
immediate access to markets, is likely to be able to profit from such a situation.
But even if a trader does not intend to execute an arbitrage,  he may be able to
use a knowledge of arbitrage pricing relationships to execute a strategy at more
favorable prices.
In Chapter 14, we noted that because there is a synthetic equivalent for
every contract, there are three ways to buy a straddle:
1.	 Buy a call, buy a put.
2.	 Buy a call, buy a put synthetically (buy two calls, sell an underlying
contract)
3.	 Buy a call synthetically, but a put (buy two puts, buy an underlying
contract)
