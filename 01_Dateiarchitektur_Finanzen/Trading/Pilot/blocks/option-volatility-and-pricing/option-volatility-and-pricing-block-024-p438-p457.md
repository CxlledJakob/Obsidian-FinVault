# Option Volatility and Pricing_ Advanced Trading Strategies -- Sheldon Natenberg -- 2nd ed, 2014 -- McGraw Hill Professional -- isbn13 9780071818773 -- 6a48d008bd9beef283debf7bad0b2e4a -- Anna’s Archive.pdf — pages 438–457

--- page 438 ---

P o s i t i o n A n a ly s i s 	 421
normally allows. For this reason, many exchanges permit options to trade at a
cabinet bid, a bid usually made at a price of one currency unit. For example, if
the minimum price for an option on a U.S. exchange is $5.00, an exchange may
permit options to trade at a cabinet bid of $1.00. This will allow traders who
are either long or short options that they believe to be worthless to remove them
from their accounts. The conditions under which cabinet bids are permissible
are specified by each exchange.
Now let’s consider the more complex position shown in Figure 21-9. The
position consists of options that all expire at the same time, but it includes calls
Figure 21.9 
Underlying price = 101.25
Time to expiration = 6 weeks
Volatility = 27.00%
Interest rate = 0%
Calls
Puts
Exercise
Price

Delta

Gamma
Theta
Vega
Delta
Gamma
Theta
Vega
   90
90.9
1.77
–0.0181
0.056
–9.1
1.77
–0.0181
0.056
   95
77.1
3.27
–0.0335
0.104
–22.9
3.27
–0.0335
0.104
100
57.2
4.23
–0.0433
0.135
–42.8
4.23
–0.0433
0.135
105
36.3
4.04
–0.0414
0.129
–63.7
4.04
–0.0414
0.129
110
19.5
2.97
–0.0304
0.095
–80.5
2.97
–0.0304
0.095
Option
Position
Delta
Position
Gamma
Position
Theta
Position
Vega
Position
90 C
–4
–363.6
–7.08
+0.0724
–0.224
95 C
–12
–925.2
–39.24
+0.4020
–1.248
100 C
+14
+800.8
+59.22
–0.6062
+1.890
105 C
–17
–617.1
–68.68
+0.7038
–2.193
110 C
Call totals
 +12
         –7
+234.0
       –871.1
+35.64
      –20.14
–0.3648
        +.2072
+1.140
        –0.635
90 P
+13
–118.3
+23.01
–0.2353
+0.728
95 P
–20
+458.0
–65.40
+0.6700
–2.080
100 P
–8
+342.4
–33.84
+0.3464
–1.080
105 P
+12
–764.4
+48.48
–0.4968
+1.548
110 P
Put totals
 +8
         +5
–644.0
       –726.3
+23.76
         –3.99
–0.2432
      +0.0411
+0.760
       –0.124
Underlying contracts
+13
1,300
0
0
0
Totals
–297.4
–24.13
+0.2483
–0.759
--- page 439 ---

422
O P T I O N V O L AT I L I T Y A N D P R I C I N G
and puts at five different exercise prices, together with a position in the underlying contract. As before, we assume that the position has some positive theoretical edge. Otherwise, the immediate goal would be to liquidate the position in
order to avoid a loss or to alter it in order to create a positive theoretical edge.
What are the risks of holding this position?
Beginning with a quick look at the sensitivities, we can see that we are at
risk from a decline in the underlying market (negative delta), from an increase
in realized volatility (negative gamma), and from an increase in implied volatility (negative vega). Looking only at the delta and gamma, the most favorable
outcome seems to be a slow downward move in the underlying market. The
least favorable outcome seems to be a swift upward move.
What else can we say about this position? From the negative delta, it’s clear
that we would like downward movement in the underlying price. But how far
down? The current price is 101.25. Do we want the market to fall to 100?
To 95? To 90? Perhaps we want an unlimited decline. However, the negative
gamma indicates that a swift and violent downward move cannot be good for
this position. Taken together with the delta, we can approximate just how far
we want the underlying to fall if we realize that a negative gamma position always
wants to become delta neutral. The profit resulting from a negative gamma position
will tend to be maximized when it is delta neutral.
Where will our position be delta neutral if the market starts to fall? For
each point decline in the underlying market, we must subtract the gamma,
–25.8, from our delta. By dividing the current delta by the gamma, we can estimate that the position is approximately delta neutral at an underlying price of
101.25 – (297.4/24.13) = 101.25 – 12.32 = 88.93
Of course, this is only an approximation because we are assuming that the
gamma is constant, which it is not. An increasing or declining gamma as the
underlying price changes will alter our conclusion. However, if we have to
make a quick estimate of what we would like to occur, a slow downward move
to around 89.00 seems best.
We have also surmised that a swift upward move will hurt this position.
Now both the delta and gamma are working against the position. Suppose that
the worst happens—the underlying contract suddenly leaps to 150. Will the
result be disastrous for us? Here we return to the net contract position: if
the market makes a dramatic move such that all contracts move into or out
of the money, what are we left with? In a large upward move, all the puts will
collapse to 0, while all the calls will eventually begin to act like underlying
contracts. Our position is net short a total of 7 calls. But we are also long 13
underlying contracts. This gives us a net upside contract position of +6. If the
market makes a really big upward move, we will have a position that is long 6
underlying contracts, giving us a potentially unlimited profit. We can conclude
that as the market moves up, at some point our gamma must turn positive,
causing the delta to eventually become positive.
The downside contract position is not so favorable. Now all the calls will
collapse to 0, while all the puts will act like short underlying contracts. We are
net long 5 puts, but we are also long the same 13 underlying contracts. Our
--- page 440 ---

P o s i t i o n A n a ly s i s 	 423
net downside contract position is +8. If the market makes a violent downward
move, we will have a position that is long 8 underlying contracts, with potentially disastrous results.
Because we are focusing on the risk characteristics of our position, no
prices or theoretical values are given for the options in Figure 21-9. We have
simply made the assumption that the position has some positive theoretical edge. However, the size of the theoretical edge—how much, in theory,
we expect to make with the position if our volatility estimate of 27 percent
is correct—can be an important consideration in analyzing the risk of the
position. For example, let’s assume that the position has a positive theoretical edge of 6.00. If 27 percent turns out to be the correct volatility over the
six-week life of the position and we go through the delta-neutral dynamic
hedging process,3 we expect to show a profit of 6.00.
The theoretical edge and vega can help us estimate our volatility risk.
From the vega position of –0.759, we know that any increase in volatility will
hurt. Consequently, we might ask this question: how much can volatility rise
before our potential profit turns into a potential loss? For each percentage point
increase in volatility our potential profit will be reduced by the amount of the
vega. By dividing the theoretical edge by the vega, we can estimate that the
position will break even at a volatility of approximately
27.00 + (6.00/0.759) = 27.00 + 7.90 = 34.90 (%)
Assuming a theoretical edge of 6.00, if volatility turns out to be no higher than
34.90 percent, the position will do no worse than break even. Above 34.90 percent, the position will begin to show a loss. We discussed this concept—the
breakeven volatility of a position—in Chapter 7. This can be thought of as
the implied volatility of the entire position. It tells us that we have a margin for
error of 7.90 volatility points in our volatility estimate. Whether this represents
a small or large margin of error depends on the volatility characteristics of this
particular market.
How can we increase the margin for error in our volatility estimate? We
can do so by either increasing the theoretical edge (without increasing the vega)
or by reducing the vega (without reducing the theoretical edge). If we can
increase the theoretical edge to 8.00 without increasing the vega, the implied
volatility of the position will be
27.00 + (8.00/0.759) = 27.00 + 10.54 = 37.54 (%)
Alternatively, if we can reduce the vega to –0.65, the implied volatility will be
27.00 + (6.00/0.65) = 27.00 + 9.23 = 36.23 (%)
Unfortunately, it may not be possible to do either. In this case, we will have to
decide whether the vega risk of –0.759 is reasonable given the potential profit
of 6.00.
3 The position is, of course, not currently delta neutral. If we want to dynamically hedge the position, we must
begin by offsetting the current delta of –297, perhaps by purchasing three underlying contracts.
--- page 441 ---

424
O P T I O N V O L AT I L I T Y A N D P R I C I N G
We know that the risk sensitivities of the position—delta, gamma, theta,
and vega—are likely to change as market conditions change. It is almost
impossible to do a detailed analysis of these changes without computer support. However, we may be able to say something about how the delta changes
as time and volatility change if we recall that delta values move either toward
50 or away from 50 with changes in time to expiration and volatility.
Consider what will happen if volatility begins to rise. All call deltas will
move toward 50 and put deltas toward –50. Because we are net short 7 calls
and net long 5 puts, in the extreme, the call delta position will be
–7 × 50 = –350
and the put delta position will be
5 × –50 = –250
Together with the 13 long underlying contracts, the total delta will be
–350 – 250 + 1,300 = +700
Of course, we would have to raise volatility dramatically for all the deltas to actually approach 50. But, as we begin to raise volatility, the current
delta of –297 will become less negative and eventually will turn positive. In
a high-volatility market, we will prefer upward movement in the underlying
contract.
What about a decline in volatility or the passage of time, both of which will
cause delta values to move away from 50? The delta values of out-of-the-money
options will move toward 0, while the delta values of in-the-money options will
move toward 100. Because we are currently net short 2 in-the-money calls (the
90, 95, and 100 calls) and net long 20 in-the-money puts (the 105 and 110 puts),
in the extreme, our total delta will be
–200 – 2,000 + 1,300 = –900
If we reduce volatility or time passes, we will prefer downward movement in
the underlying contract.
For a new trader, using a basic knowledge of delta, gamma, theta, and vega
characteristics to analyze the risk of a position can be a useful exercise. However, when computer support is available, it is almost always easier and more
efficient to look at graphs of the position’s risk. This has been done for the current position in Figures 21-10 through 21-13.
In Figure 21-10, we can see that at a volatility of 27 percent, the maximum
profit on the downside will occur at a price of approximately 95.00, at which
point the position delta is 0. This differs considerably from our estimate of 88.93
because the gamma, which was initially –24.13, becomes a much larger negative
number as the market drops. The negative delta of –297 is more rapidly offset by
the increasing gamma. In Figure 21-12, we see that on the downside, the gamma
reaches its maximum of approximately –80 at an underlying price of 93.
If the market moves up, we will initially lose money. But, at an underlying
price of 104, the gamma becomes positive. Our negative delta begins to turn
--- page 442 ---

P o s i t i o n A n a ly s i s 	 425
around and at a price of 112 actually becomes positive (Figure 21-11). We will
continue to lose money above 112, but at some point the position will begin
to show a profit. Figure 21-10 only goes up to an underlying price of 120, but
a more extensive analysis would show that at an underlying price of 124, the
position will begin to show a profit.
Figure 21-10  Position value as the underlying price and volatility change.
Underlying price
80
85
95
100
110
115
120
90
105
Theoretical P&L
–40
–20
0
–60
20
40
–80
101.25
Volatility = 27%
Volatility = 22%
Volatility = 32%
Time to expiration = 6 weeks
Figure 21-11  Position delta as the underlying price and volatility change.
Underlying price
80
85
95
100
110
115
120
90
105
Position delta
–200
0
200
–400
400
600
800
1,000
–600
101.25
Volatility = 27%
Volatility = 22%
Volatility = 32%
Time to expiration = 6 weeks
--- page 443 ---

426
O P T I O N V O L AT I L I T Y A N D P R I C I N G
In Chapter 9, we looked at some of the nontraditional higher-order risk
measures. Figure 21-12 shows that between the underlying prices of 93 and
114, the position has a positive speed; as the price rises, the gamma increases.
Below 93 and above 114, the position has a negative speed; as the price rises,
the gamma declines. We can also see that changing the volatility causes the
gamma and, consequently, the delta to change at a different rate. Lowering
volatility causes the speed to increase, while raising volatility causes the speed
to decline.
Figure 21-13 shows the sensitivity of the position to changes in implied
volatility, assuming a constant underlying price of 101.25. The position clearly
has a negative vega. Any decline in implied volatility will help the position; any
increase in implied volatility will hurt the position. Given a theoretical edge,
we can estimate the breakeven (implied) volatility for the entire position by
dividing the total theoretical edge by the vega. If, for example, we have a
total edge of 6.00, we estimated that the position has an implied volatility of
approximately 34.90 percent. In fact, we can see in Figure 21-13 that the implied
volatility is somewhat higher than 34.90 percent. The six-week graph crosses
–6.00, which would exactly offset a theoretical edge of +6.00, at a volatility of
approximately 36 percent. The reason the breakeven volatility is greater than
our estimate is that the six-week graph has a positive volga—it curves upward
slightly. As volatility rises, the vega becomes more positive or less negative. As
volatility falls, the vega becomes more negative or less positive. Even though the
current volga is positive, we can see that as time passes, the volga of the position
becomes slightly negative. The four-week graph is approximately a straight
line, while the two-week graph curves slightly downward.
Figure 21-12  Position gamma as the underlying price and volatility change.
Underlying price
80
85
95
100
110
115
120
90
105
Position gamma
–40
0
40
80
–80
–20
20
60
–60
–100
–120
101.25
Volatility = 27%
Volatility = 22%
Volatility = 32%
Time to expiration = 6 weeks
--- page 444 ---

P o s i t i o n A n a ly s i s 	 427
What should we conclude about the position in Figure 21-9? The reason for
doing an analysis is to help us determine beforehand what actions to take to either
maximize our profits if conditions move in our favor or minimize losses if conditions move against us. We currently have a negative delta. If we wish to maintain
a downward bias, then no action is necessary. If, however, we are trading from a
purely theoretical standpoint, then perhaps we ought to buy the 297 deltas that we
are short. The easiest way to do this is to buy three underlying contracts.
If we maintain our current position and the market begins to decline, what
action should we take? If the decline is slow (clearly a very good outcome given
our delta and gamma) and there is no increase in implied volatility, perhaps
we ought to consider buying puts at lower exercise prices. This will have the
effect of offsetting our downside net contract risk and reducing our negative
vega while locking in some of the theoretical edge. If, however, the decline
is swift, we may have to ignore theoretical considerations and buy puts at the
market price. This may be the cost of having a bad position, something that
will inevitably occur at some point in every trader’s career. If we are forced to
buy puts at inflated prices, especially if there is an increase in implied volatility,
we may lose money. But if the decline is very swift, the primary objective may
be survival. And in the long run, simply surviving, in order to be able to take
advantage of those subsequent occasions when conditions work in our favor,
can mean the difference between success and failure in option trading.
What action should we take if the market begins to rise? We ought to
be prepared for one course of action if the move is slow (the delta is working
against us, while the gamma is working for us), but a different course of action if
the move is swift (the delta and gamma are initially working against us, but if the
upward move is large enough, these numbers may eventually work in our favor).
Figure 21-13  Position value as volatility changes and time passes.
Volatility
–8
17%
19%
21%
23%
25%
27%
29%
31%
33%
35%
37%
Theoretical P&L
–6
–4
–2
0
2
4
6
8
10
12
14
4 weeks to expiration
6 weeks to expiration
2 weeks to expiration
Underlying price = 101.25
--- page 445 ---

428
O P T I O N V O L AT I L I T Y A N D P R I C I N G
A detailed position analysis will help us prepare for a variety of changes
in market conditions. But no matter how detailed our analysis, we may still
encounter situations where we are in uncharted territory. When conditions do
change, we can never know for certain how the marketplace will react. If the
underlying price begins to rise or fall, depending on the specific market, we
may expect implied volatility to change in a certain way. But we may find that it
has changed in a completely different way. We may have to accept the fact that
our analysis was incorrect and take whatever action we can to reduce our losses
or maximize our profits under these new and unexpected conditions.
Some Thoughts on Market Making
In order to ensure liquidity in a market, exchanges may appoint one or more
market makers in a product. A market maker guarantees that he will continuously
quote both a price at which he is willing to buy and a price at which he is willing
to sell. As a consequence, a buyer or seller can always be certain that there will
be someone in the marketplace willing to take the opposite side of the trade.
This does not mean that a customer is required to trade with a market maker.
If other market participants are willing to buy at a higher price or sell at a lower
price, the customer is always free to trade at the best available price. But by continuously quoting a bid-ask spread,  the market maker fulfills his role as the buyer
or seller of last resort
A market maker must comply with rules established by the exchange concerning the width of the bid-ask spread as well as the minimum number of
contracts that the market maker must be willing to trade. If exchange rules
dictate that a market maker may quote a bid-ask spread no wider than 2.00, then
a bid price of 63.00 for a contract implies an offer price that is no higher than
65.00. Similarly, an offer price of 47.00 implies a bid price that is no lower
than 45.00. The market maker may quote a tighter bid-ask spread, for example, 63.50–64.50 in the former case or 45.75–46.25 in the latter, but the spread
may be no wider than that specified under the exchange rules.
In addition to quoting a bid-ask spread, a market maker must be willing
to trade a minimum number of contracts at the quoted prices. If the exchange
minimum is 100 contracts, the market maker must be willing to buy or sell a
minimum of 100 contracts at his quoted prices. He may offer to trade more
than the minimum, in which case he will usually quote his size along with the
bid-ask spread, for example,
63.50–64.50
200 × 200
The market maker is willing to buy at least 200 contracts at a price of 63.50 or sell
at least 200 contracts at a price of 64.50. The quoted size need not be balanced:
63.50–64.50
500 × 200
Here the market maker is willing to buy 500 contracts but only willing to sell
200 contracts.
--- page 446 ---

P o s i t i o n A n a ly s i s 	 429
Rules governing the width of a market maker’s bid-ask spread usually
apply only to the minimum size that the market maker must be prepared to
do. If a customer wants to trade a very large number of contracts, a market
maker is permitted to widen the spread because of the increased risk associated with the trade. In response to a customer who wants to trade 1,000
contracts, a market maker might quote a spread of 62.00–66.00. To facilitate trading, when a customer has a large order, he will usually indicate that
he wants a quote for size.
In return for fulfilling his obligations, a market maker will receive special
considerations from the exchange. These may come in the form of very low
exchange fees or preferential treatment when competing against other market
participants. If a customer is willing to sell at the market maker’s bid price and
two other market participants are also quoting the same bid price, the market
maker may be entitled to 50 percent of the order, while the other two bidders
may onlybe entitled to 25 percent each.
Unlike investors, speculators, or hedgers, who can choose the strategies
that best fit their needs and who can also determine when to enter and exit a
market, a market maker has less control over the positions he takes. This does
not mean that a market maker is totally at the mercy of his customers. He may
be forced to take on a position, but he at least has some choice as to the price
at which he does so. Moreover, by adjusting his bid-ask spread, he can to some
extent determine the types of positions he acquires. But having done so,  he
may still find that he has taken on a position that he would prefer not to have.
Although market makers typically represent only a small percentage of
option market participants, they can play a crucial role in trading, often determining the success or failure of an exchange-listed product.4 For this reason, it
may be useful to take a closer look at how an option market maker goes about
his business.
A successful market maker must ask three questions:
1.	 What does the marketplace think an option is worth?
2.	 What do I (the market maker) think the option is worth?
3.	 What positions am I currently carrying?
The answers to these questions will determine how a market maker prices
options and how he manages risk.
The answer to the first question—what does the marketplace think an
option is worth?—is the basis for the simplest of all market-making techniques.
In this approach, the market maker attempts to profit solely from the bid-ask
spread, constantly buying at the bid price and selling at the offer price. No special knowledge of option pricing theory is required, but in order to succeed, the
market maker must be able to identify an equilibrium price around which there
4 Customers sometimes believe that market makers “fix” the prices of exchange-traded contracts. This may be
true for short periods of time, usually at the beginning of the trading day when very little information is available. Ultimately, however, a market maker’s quotes reflect current market activity. A market maker does not set
prices any more than a thermometer sets the temperature.
--- page 447 ---

430
O P T I O N V O L AT I L I T Y A N D P R I C I N G
are an equal number of buyers and sellers.5 If he can correctly determine this
equilibrium price, he is in a position to act as a middleman, showing a small
profit on each trade while carrying positions for only short periods of time. Of
course, the equilibrium price is constantly changing as new buyers and sellers
enter the market. Although a market maker will constantly monitor market
activity to determine changes in buying and selling pressure, even an experienced market maker will sometimes find, especially in a very fast-moving
market, that he has the wrong equilibrium price. When this occurs, he may find
that he has either bought or sold many more contracts than he desires.
In addition to profiting from the bid-ask spread, by answering the second
question—what do I think the option is worth?—an option market maker will
also try to profit from a theoretically mispriced option. The mispricing may be
the result of an unbalanced arbitrage relationship, in which case the market
maker will attempt to “lock in” the profit by completing the arbitrage. Or the
mispricing may be the result of using a theoretical pricing model. In this case,
if the market maker buys at a price below or sells at a price above his presumed
theoretical value, he can dynamically hedge the position to expiration or until
the option is again trading at theoretical value. If his theoretical value is correct, the dynamic hedging process should, in theory, result in a profit.
Once the market maker begins to acquire positions, he must consider the
possibility that market conditions might move against him. This brings us to
the final question—what positions am I currently carrying? Although there
is some risk associated with every position, if the risk becomes too great, an
adverse change in market conditions might put the market maker in a situation where he is unable to freely trade and therefore unable to benefit from his
position as a market maker. In an extreme case, he may be forced out of business because he is no longer able to fulfill his obligations as a market maker.
A market maker must consider a variety of risks. Initially, he will probably
determine a maximum risk he is willing to carry under current market conditions. This may mean limiting the size of his position with respect to the various
risk parameters—delta, gamma, theta, vega, and rho. When a limit is reached,
the market maker will begin to focus on making markets that will have the effect
of reducing his risk. If a market maker is approaching the maximum negative
gamma position that he is willing to accept, as he gets closer to this limit, he will
increasingly focus on reducing or at least limiting this risk. As a market maker,
he still must quote both a bid price and an offer price, but he would much prefer
to buy options because this will have the effect of reducing his negative gamma
position. Under normal conditions, if asked to make a market, he will likely do
so around the presumed theoretical value. If the value of the option is 64.00,
he might quote a market of 63.00–65.00, but if the market maker is intent on
reducing his negative gamma risk, he will clearly prefer to buy options rather
than sell. To reflect this preference, he can adjust his bid-ask spread, perhaps
quoting a market of 63.50–65.50. The fact that he has raised both his bid and
offer makes it more likely that he will buy options rather than sell. Of course, he
5 A trader who tries to profit solely from the bid-ask spread, buying at the bid price and selling at the ask price
without regard to theoretical value, is sometimes referred to as a scalper. Scalping is a common trading technique in open-outcry markets.
--- page 448 ---

P o s i t i o n A n a ly s i s 	 431
may still be required to sell if the offer of 65.50 is accepted. But at least he has
done so at a more advantageous price.
A market maker must consider not only the risks under current market
conditions but also how those risks might change as market conditions change.
Suppose that in a rising market the market maker has reached the maximum
negative gamma he is willing to accept. However, in analyzing the position, he
has also noted that if the underlying contract continues to rise, the gamma risk
will begin to decline.6 If the underlying does move, the market maker may still
be hurt because he has a negative gamma position. But he may decide that he
can live with this risk because the gamma risk will begin to decline.
In addition to monitoring the various risk sensitivities, a market maker
must also intelligently manage his inventory. As conditions change, a position
that includes a concentrated risk may evolve into a serious threat to the market
maker. Consider a market maker who has the following gamma position spread
out over 10 different exercise prices:
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
+110
+425
+300
+68
–2,388
+92
+244
+616
+338
+195
Even if the total gamma risk is relatively small (indeed, the total gamma in
this case is 0), the fact that such a large negative gamma is concentrated at one
exercise price, 95, is likely to be of concern to the market maker. If these are longterm options, the situation may not be critical today. But as time passes, if the
underlying market approaches 95, the position will take on increasingly greater
risk. Rather than let this risk increase, an intelligent market maker will focus on
spreading out his risk more evenly across exercise prices. In the same way that
a wise investor will seek to diversify his risk, a market maker will strive for a similar goal.
In this example, the risk was concentrated at one exercise price. But any
concentration of risk at a specific exercise price or expiration date or in terms
of a single large risk sensitivity should be a cause for concern. It may not
always be feasible because market conditions do not always cooperate, but a
market maker’s ultimate objective should be to diversify his position as much
as possible.
Consider the stock option position shown in Figure 21-14. This position
does not fall into any easily recognizable category and represents the type of
mixed collection of options that a market maker might accumulate over time
as a result of buying and selling by customers.7 The current market conditions
(i.e., underlying share price, time to expiration, implied volatility, and expected
dividends) are also shown in Figure 21-14.
To fully analyze the position, we will need to make some assumptions
about the term structure of implied volatility. Here we will assume that April
6 In this case, the market maker has a positive speed position. His gamma position becomes more positive or less
negative as the price of the underlying contract rises.
7 An active market maker’s position is likely to be much larger than the position shown, with hundreds or even
thousands of options at each exercise price. For simplicity, the position shown has been scaled down. But the
risk-analysis process will be the same.
--- page 449 ---

432
O P T I O N V O L AT I L I T Y A N D P R I C I N G
Figure 21-14 
Underlying share price = 68.76        Interest rate = 4.95%  Expected dividend = 0.58 in 10 weeks
Time to April expiration = 4 weeks
April implied volatility = 34.27%
Time to June expiration = 13 weeks
June implied volatility = 33.20%
Time to August expiration = 21 weeks
August implied volatility = 32.14%
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
55
+77
+47
–103
+32
60
–162
+111
+3
+81
+24
–46
65
+13
–77
+92
–25
70
+106
–19
–110
–49
–26
–20
75
–8
+122
+86
–2
+8
–25
80
–31
–18
+21
+30
85
–135
+46
–25
+7
–72
Calls
Puts
Delta
Gamma
Theta
Adjusted Vega
Rho
April
–140
+212
–12,615
+504
–2.51
+6.26
–7.50
June
+67
–91
+6,093
+13
–0.62
+0.36
+9.75
August
–36
–59
+3,425
–252
+1.25
–11.19
+10.45
Shares
+3,300
+3,300
Totals
+203
+265
–1.88
–4.57
+12.70
is the primary month and that the mean volatility for this market is 30 percent.
We will also assume that the implied volatility for June changes at 75 percent
of the rate of change in April and the implied volatility for August changes at
50 percent of the rate of change in April.8 We can see that the current implied
volatilities are consistent with this term structure:
April (primary month) implied volatility = 34.27%
  Difference from the mean = 34.27% – 30.00% = 4.27%
June implied volatility = 33.20%
  Difference from the mean = 33.20% – 30.00% = 3.20% ≈ 0.75 × 4.27%
August implied volatility = 32.14%
  Difference from the mean = 32.14% – 30.00% = 2.14% ≈ 0.50 × 4.27%
8 We might also make assumptions about the term structure of interest rates, as well as how implied volatility
is distributed across exercise prices. In order not to overly complicate the current example, we will assume a
constant interest rate across expiration months, as well as uniform implied volatilities across exercise prices. We
leave the discussion of volatility skews to a later chapter.
--- page 450 ---

P o s i t i o n A n a ly s i s 	 433
The primary risk characteristics of the position9—theoretical profit and loss
(P&L), delta, gamma, and vega—are shown in Figures 21-15 through 21-18.10
From these graphs, it is evident that the risks of the position can change significantly as market conditions change, with the delta, gamma, and vega gyrating
between positive and negative. Given this, how should we analyze the position?
A market maker’s ultimate goal is to establish positions with a positive
profit expectation while intelligently managing risk. Indeed, were it not for the
complexities of the marketplace and the unique characteristics of options, a
market maker’s life might be thought of as quite boring because he is trying to
do the same thing over and over:
Get an edge….
Control the risk….
Get an edge….
Control the risk….
Get an edge….
Control the risk….
Get an edge….
Control the risk….
9 In this example, we have assumed that the options are European and have made all calculations using the
Black-Scholes model. The risk-analysis process would be the same if the options were American, although
the calculations necessarily would have to be made using an American pricing model.
10 Because of the term structure of volatility, the changes in volatility in Figures 21-15, through 21-18 are
expressed in percent terms rather than percentage points. Given our assumptions (i.e., mean volatility = 30 percent, June implied volatility changes 75 percent as fast as April, August implied volatility changes 50 percent as
fast as April), a 20 percent increase in volatility from the current levels results in

April:
1.20 × 34.27% ≈ 41.12%

June:
30.00% + 0.75 × (41.12% – 30.00%) ≈ 38.34%

August:
30.00% + 0.50 × (41.12% – 30.00%) ≈ 35.56%

while a 20 percent decline from the current levels results in

April:
0.80 × 34.27% ≈ 27.42%

June:
30.00% – 0.75 × (30.00% – 27.42%) ≈ 28.06%

August:
30.00% – 0.50 × (30.00% – 27.42%) ≈ 28.71%
Figure 21-15  Position value as the underlying price and volatility change.
Underlying price
45
50
60
70
95
55
0
+100
+200
+350
–100
+50
+150
+250
–50
–150
–200
68.76
Volatility down 20%
Current volatility
Volatility up 20%
65
75
85
80
90
Theoretical P&L
+300
--- page 451 ---

434
O P T I O N V O L AT I L I T Y A N D P R I C I N G
Once a position with a positive theoretical edge has been established, the
market maker ideally would like to reduce all risks to 0 without giving up any
potential profit. This would be identical to turning the graph in Figure 21-15
into a single horizontal line with a positive theoretical P&L. In reality, with a
large and complex position, it is virtually impossible to achieve such a goal.
Figure 21-17  Position gamma as the underlying price and volatility change.
Underlying price
45
50
60
70
95
55
–400
0
+400
+800
–200
+200
+600
–600
–800
68.76
Volatility down 20%
Current volatility
Volatility up 20%
65
75
85
80
90
Total gamma
Figure 21-16  Position delta as the underlying price and volatility change.
Underlying price
45
50
60
70
95
55
–3,000
–1,000
+1,000
+3,000
–5,000
–2,000
0
+2,000
–4,000
–6,000
68.76
Volatility down 20%
Current volatility
Volatility up 20%
65
75
85
80
90
Total delta
+4,000
--- page 452 ---

P o s i t i o n A n a ly s i s 	 435
A more practical approach is to ask what changes in market conditions represent the greatest immediate threat to the position and what steps can be taken
to mitigate those risks. Even this will depend on many subjective factors: the
trader’s appetite for risk, his capitalization, the extent of his trading experience,
and his familiarity with the market. Unfortunately, there are very few easy answers when it comes to risk analysis.
Some risk limitations will be set by the firm for which the trader works or
by the trader’s clearing firm. For example, a clearing firm may require that a
trader maintain enough capital to withstand a 20 percent move in the underlying contract in either direction. Or the firm may require enough capital to
withstand a doubling of implied volatility. If the trader currently has insufficient capital to meet these requirements, he must either deposit additional
money with the clearing firm or reduce the size of the position so that it falls
within the clearing firm’s guidelines.
How should we analyze the risk of the position in Figure 21-14? Risk analysis is important because it enables a trader to plan ahead—to decide what
course of action is best—given a change in market conditions. An option trader
may have to consider many different market scenarios, but it is often best to
begin with three basic questions:
1.	 What will I do if market conditions move against me?
2.	 What will I do if market conditions move in my favor? (Risk analysis
should focus not only on protecting against the bad things that might
occur but also on taking advantage of the good things.)
3.	 What can I do now to avoid the adverse effects of conditions moving
against me at a later time?
Figure 21-18  Position vega as the underlying price and volatility change.
Underlying price
45
50
60
70
95
55
–10
–5
0
+5
–15
–20
68.76
Volatility down 20%
Current volatility
Volatility up 20%
65
75
85
80
90
Total adjusted vega
--- page 453 ---

436
O P T I O N V O L AT I L I T Y A N D P R I C I N G
What are the bad things that can happen to the position? Clearly, the
greatest threat is a violent upward move. Above a stock price of 85, the position
will take on a negative delta and from that point on will continue to lose money
as the market rises (Figures 21-15 and 21-16). The upside contract position (the
sum of all calls and underlying contracts) is –76.
With a current delta of +203, there is also some risk of a declining stock
price. This may not be of immediate concern, but note that as the stock
price declines toward 62, the position takes on an increasingly negative vega
(Figure 21-18). This means that the position is at risk if the stock price falls
moderately while implied volatility rises.
In Figure 21-17, we can see that the position has a maximum positive gamma
at stock prices of approximately 53 and 72. If the market were to approach either
of these prices and remain there, the position would most likely take on its maximum negative theta and consequently begin to decay very rapidly.
Given the various risks, what should be the immediate concern? The
answer must necessarily be subjective and will depend on what this trader
knows about the characteristics of this stock. If there is some possibility of a
really large upward move, for example, the company is a takeover target, it is
incumbent on the trader to cover at least some of his upside risk, perhaps by
purchasing higher-exercise-price calls. Admittedly, if the prices of the upside
calls are inflated because the company is known to be a takeover target, the cost
of protecting the upside may be high. But, if a takeover could result in the trader’s demise, this may be a price that he will have to pay.
Of course, the trader may believe that a large upward move is so unlikely
that he is willing to accept the risk. Then he may want to focus on some of the
lesser threats to the position. If he is a disciplined theoretical trader, he may
want to cover his current delta position of +203, although this too may represent such a small risk that it is not of immediate concern. Otherwise, he may
want to sell approximately 200 deltas in some form—sell stock, sell calls, or buy
puts. The last choice, buying puts, especially those with exercise prices of 60 or
65, will have the effect not only of reducing the delta but also reducing the negative vega in the range of 60 to 65. If given the choice, the purchase of April
60 or 65 puts will probably show the greatest benefit to the position. If the stock
price does decline to between 60 and 65, these options will be at the money, and
at-the-money short-term options have the greatest gamma. As such, they will
do the most to offset the negative gamma in this range.
What changes in market conditions might help the position? Below a stock
price of 55, the position will take on a negative delta, so a collapse in the stock
price will obviously prove beneficial. The downside contract position (the sum
of all puts and underlying contracts) is –29. If the stock price should climb
toward 85, especially with falling implied volatility, this will also be very favorable. Indeed, almost any decline in implied volatility will help the position, as
shown by the vega in Figure 21-18.
Even though time decay may not be an immediate concern, it may still be
worth considering how the passage of time will affect the position. The position has a negative theta (consistent with a positive gamma), so the passage of
time will work against the position if there is no change in the underlying stock
price. The total theta of –1.90 may be small, but note that most of the theta is
--- page 454 ---

P o s i t i o n A n a ly s i s 	 437
concentrated in April. And the April position consists of a large long position
in April 70 calls. As time passes, the theta of these options, which are close to at
the money, will accelerate, causing the position to lose value at an increasingly
greater rate. If the market remains close to 70, it is also likely that there will be a
decline in implied volatility. Given the position’s negative vega, this will work in
the position’s favor. Still, it may be worth thinking about what action to take if
the stock price remains close to 70. The value of the position after the passage
of one and two weeks is shown in Figure 21-19.
What else might hurt this position? We have assumed that the stock will pay
a dividend of 0.58 in 10 weeks. If the company has not officially announced
the dividend, perhaps the actual dividend will be more than or less than this
amount. The April options, which expire in four weeks, will be unaffected by
a change in the dividend. But how will the overall position be affected? We
can run a computer simulation at higher or lower dividend amounts, but perhaps an easier approach is to note that the position is long 3,300 shares of
stock. Because we own stock and therefore receive the dividend, any increase
in the dividend will cause the position value to rise, and any decrease will cause
the position value to fall. The change in value will be approximately equal to
the change in the dividend multiplied by the number of shares of stock, in this
case, 3,300.
If there is a real possibility that the dividend will be reduced, one way to
eliminate the risk is to replace the long stock position with synthetic long stock:
sell the stock, and buy calls and sell puts at the same exercise price. This is similar to reducing the risk of a conversion or reverse conversion by turning the
position into a box (see Chapter 15).
Figure 21-19  Position value as the underlying price changes and time passes.
Underlying price
45
50
60
70
95
55
+50
+150
+250
+350
–50
+100
+200
+300
0
–100
68.76
After one week
Now
After two weeks
65
75
85
80
90
+400
Theoretical P&L
--- page 455 ---

438
O P T I O N V O L AT I L I T Y A N D P R I C I N G
The total rho of +12.70 also indicates that there is some risk of falling
interest rates. For each full-point decline (100 basis points11) in interest rates, the
position value will fall by 12.70.
It is usually easiest to analyze risk by generating graphs of a position’s characteristics, as we have done in Figures 21-15 to 21-19. However, some traders prefer to create a table showing the risk sensitivities at various underlying
prices. This has been done in Figure 21-20, beginning with a stock price of
45 and continuing at five-point increments up to a stock price of 95. The
table includes not only the traditional risk measures but also the nontraditional
higher-order measures discussed in Chapter 9. These higher-order measures
can often give a trader a more complete picture of how the risks of his position
will change as market conditions change. For convenience, we list these measures below:
Vanna:
Sensitivity of the delta to a change in volatility
Charm:
Sensitivity of the delta to the passage of time
Speed:
Sensitivity of the gamma to a change in the underlying price
Color:
Sensitivity of the gamma to the passage of time
Volga:
Sensitivity of the vega to a change in volatility
Vega decay: 	Sensitivity of the vega to the passage of time
Zomma:
Sensitivity of the gamma to a change in volatility
11 Traders commonly express changes in interest rates in basis points. One basis point is equal to 1/100 of a percentage point, or 0.0001.
Stock price
45
50
55
60
65
70
75
80
85
90
95
Theoretical P&L
+179
+32
–25
–1
+4
+5
+74
+182
+221
+131
–76
Total delta
–3,206
–2,306
–14
+533
–232
+571
+2,083 +1,805
–439
–3,092
–5,046
Total gamma
+2
+391
+378
–134
–46
+325
+179
–292
–544
–479
–301
Total adjusted
vega
–0.94
+0.86
+0.81
–3.97
–4.01
+0.11
–2.09
–9.68
–14.84 –14.27
–10.70
Total theta
+0.61
–1.06
–1.53
+0.99
+0.51
–2.50
–1.74
+2.91
+6.50
+6.77
+5.18
Total rho
+19
+19
+18
+17
+15
+12
+10
+7
+3
–1
–4
Total vanna
–5
+28
–98
–115
+34
+16
–131
–149
–30
+74
+100
Total charm
–15
–41
+33
+39
–55
–38
+68
+98
+38
–21
–36
Total speed
+45
+77
–90
–63
+81
+34
–82
–84
–14
+32
+34
Total color
–8.00
–4.47
–16.60
–15.53 –12.74 +18.10
+17.62
–5.65
–14.77
–7.36
+.54
Total volga
–0.0004 –0.0008 –0.0023 –0.0005
0
–0.0015 –0.0015
0
+.0002 –0.0009 –0.0017
Total vega decay +0.037
+0.065
–0.030
+0.092 +0.134 –0.046 –0.0117 –0.035 –0.052 –0.179
–0.247
Total zomma
+10
–8
–28
+24
+21
–26
–22
+15
+27
+13
–1
Figure 21-20  Risk sensitivities as the underlying price changes
--- page 456 ---

P o s i t i o n A n a ly s i s 	 439
Stock Splits
To conclude our discussion, let’s consider one last change in market conditions—a stock split. This often happens when a company wants to reduce its
stock price to promote trading in the stock or to encourage wider ownership of
the stock. If the stock price remains high, trading activity tends to be limited,
with ownership of the stock concentrated in fewer hands.
Suppose that the stock in our example splits 2 for 1, resulting in a new stock
price of 68.76/2 = 34.38. What will happen to the position? Where the trader
previously owned 3,300 shares, he will now own 2 × 3,300 = 6,600 shares.
To maintain the same relationship between each exercise price and the stock
price, as a result of the split, the clearinghouse will divide all the exercise prices
by 2. The 55 exercise price will become 27½, the 60 exercise price will become
30, and so on. The underlying contract will remain 100 shares of stock, but in
order to maintain equity, the clearinghouse will double the trader’s position
at each exercise price. Instead of being long 77 April 55 calls, the trader will
now be long 154 April 27½ calls. Instead of being short 162 April 60 calls, the
trader will now be short 324 April 30 calls.
How will the trader’s risk position look now? In order to understand what
happens, let’s consider a simple example. With an underlying stock trading at
60.00, we own a May 60 call with a delta of 50 and a gamma of 5. If the stock
splits 2 for 1, our position will now be
Before Split
After Split
Stock price
60
30
Position
+1 May 60 call
+2 May 30 calls
Underlying contract
100 shares
100 shares
Delta position
+50
+100
Because the option is still at the money, the delta will be 50. But now we own
two calls, so our delta position will double to +100.
What about the gamma? Because the gamma is the change in delta per
point change in the underlying stock price, if we can determine the new delta
position at a stock price of 31, we will know the gamma. Suppose that the stock
price rises to 31. This is equivalent to the stock price rising to 62 prior to the
split. At a stock price of 62 (prior to the split), our delta position would have
been +50 + (2 × 5) = +60. But the stock split caused our delta to double, so
the new delta position at a stock price of 31 must be 2 × +60 = +120. If the
delta rises from 100 to 120 with a stock price change from 30 to 31, the gamma
of the position must be +20.
If a stock splits Y for X (each X number of shares will be replaced with Y
number of shares), we can summarize the new conditions as follows:
New stock price:

Old stock price × X/Y
New exercise price:
Old exercise price × X/Y
New option position:
Old option position × Y/X
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
