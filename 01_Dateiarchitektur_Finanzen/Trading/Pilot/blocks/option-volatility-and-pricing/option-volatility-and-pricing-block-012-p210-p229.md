# Option Volatility and Pricing_ Advanced Trading Strategies -- Sheldon Natenberg -- 2nd ed, 2014 -- McGraw Hill Professional -- isbn13 9780071818773 -- 6a48d008bd9beef283debf7bad0b2e4a -- Anna’s Archive.pdf — pages 210–229

--- page 210 ---

V o l at i l i t y S p r e a d s 	 193
Figure 11-27  Long time butterfly as volatility declines.
Sell one long-term
and one short-term
option, and buy two
intermediate-term options
All options must be
the same type (all
calls or all puts) and
have the same
exercise price
Exercise
price
Lower underlying prices
Higher underlying prices
Position value
Figure 11-26  Long time butterfly as time passes.
Sell one long-term
and one short-term
option, and buy two
intermediate-term options
–1 May 100 call
+2 June 100 calls
–1 July 100 call
–1 February 25 put
+2 June 25 puts
–1 October 25 put
All options must be
the same type (all
calls or all puts) and
have the same
exercise price
Exercise
price
Lower underlying prices
Higher underlying prices
Position value
--- page 211 ---

194
O P T I O N V O L AT I L I T Y A N D P R I C I N G
Because there is no carrying cost associated with the purchase or sale of a
futures contract, interest rates have only a minor impact on futures options and,
consequently, a relatively minor effect on the value of all futures option volatility spreads.8 However, in a stock option market, a change in interest rates will
cause the forward price of stocks to change. If all options in a spread expire at
the same time, the change in forward price is likely to affect all options equally,
causing only small changes in the value of the spread. However, if we have a
stock option position involving two different expiration dates, we must consider
two different forward prices. And these two forward prices may not be equally
sensitive to a change in interest rates.
Consider the following situation:
Stock price = 100 interest rate = 8.00% dividend = 0
Suppose that a trader buys a call calendar spread:

+10 June 100 calls

–10 March 100 calls
If there are three months remaining to March expiration and six months remaining to June expiration, the forward prices for March stock and June stock
are 102.00 and 104.00, respectively. If interest rates rise to 10 percent, the forward price for March will be 102.50 and the forward price for June will be 105.
With more time remaining to June expiration, the June forward price is more
sensitive to a change in interest rates. Assuming that the deltas of both options
are approximately equal, the June option will be more affected by the increase
in interest rates than the March option, and the calendar spread will expand. In
the same way, if interest rates decline, the calendar spread will narrow because
the June forward price will fall more quickly than the March forward price. A
long call calendar spread in the stock option market must therefore have a positive rho, and a short call calendar spread must have a negative rho.
Changes in interest rates have the opposite effect on stock option puts. In
our example, if interest rates rise from 8 to 10 percent, the June forward price
will rise more than the March forward price. If we assume, again, that the deltas of both options are approximately equal, and recalling that puts have negative deltas, the June put will show a greater decline in value than the March put.
The put calendar spread will therefore narrow. In the same way, if interest rates
decline, the put calendar spread will expand. A long put calendar spread in the
stock option market must therefore have a negative rho, and a short put calendar spread must have a positive rho.
The degree to which stock option calendar spreads are affected by changes
in interest rates depends primarily on the amount of time between expirations.
If there are six months between expirations (e.g., March/September), the effect will be much greater than if there is only one month between expirations
(e.g., March/April).
8 Interest rates can, of course, affect the relative value of different futures months. As noted, we can offset this
risk by trading a futures spread along with the futures option calendar spread.
--- page 212 ---

V o l at i l i t y S p r e a d s 	 195
Figure 11-28  Effect of changing interest rates and changing dividends on stock option
calendar spreads.
Stock price = 100  Volatility = 20%  Dividend = 0
Time to March expiration = 3 months
Time to June expiration = 6 months
If the interest
rate is…
0 percent
3 percent
6 percent
9 percent
12 percent
June 100 call
5.64
6.37
7.16
7.99
8.87
March 100 call
3.99
4.36
4.75
5.16
5.58
Call spread value
1.65
2.01
2.41
2.83
3.29
June 100 put
5.64
4.88
4.20
3.59
3.05
March 100 put
3.99
3.61
3.26
2.93
2.63
Put spread value
1.65
1.27
0.94
0.66
0.42
Changes in dividends can also affect the value of stock option calendar
spreads because it may change the forward price of the stock. Dividends, however, have the opposite effect on stock options as changes in interest rates. An
increase in the dividend lowers the forward price of stock, while a cut in the
dividend raises the forward price. If all options expire at the same time, the
change in the forward price for the stock will have an equal effect on all options, and the change in the value of a spread will be negligible. But in a calendar spread, if at least one dividend payment is expected between the expiration
dates, an increase in dividends will cause a call calendar spread to narrow and
put calendar spread to expand. A decrease in dividends will have the opposite
effect, causing a call calendar spread to widen and a put calendar spread to
narrow. Even though there is no Greek letter associated with dividend risk, we
might say that a call calendar spread has negative dividend risk (its value falls
as dividends rise) and a put calendar spread has positive dividend risk (its value
rises as dividends rise). Examples of the effects of changing interest rates and
dividends on stock option calendar spreads are shown in Figure 11-28.
In Figure 11-28, we can see that an increase in interest rates will reduce the
value of a put calendar spread and an increase in dividends will reduce the value
of a call calendar spread. Indeed, if we raise interest rates high enough, the put
calendar spread can take on a negative value, with the long-term put having a
lower value than the short-term put. The same will be true for a call calendar
spread if we increase dividends enough. If a stock pays no dividends, the value
of a call calendar spread should always have some value greater than 0. Even
if volatility is very low, the spread should still be worth a minimum of the cost
of carry on the stock between expiration months. This is only true, however, if
a trader can carry a short stock position between expiration months. If a situation arises where no stock can be borrowed, the trader who owns a call calendar
spread may be forced to exercise his long-term option, thereby losing the time
value associated with the option. This is sometimes referred to as a short squeeze.
(continued)
--- page 213 ---

196
O P T I O N V O L AT I L I T Y A N D P R I C I N G
Diagonal Spreads
A diagonal spread is similar to a calendar spread except that the options have different exercise prices. Although many diagonal spreads are executed one to one
(one long-term option for each short-term option), diagonal spreads can also
be ratioed, with unequal numbers of long and short market contracts. With the
large number of variations in diagonal spreads, it is almost impossible to generalize about their characteristics. Each diagonal spread must be analyzed separately to determine the risks and rewards associated with the spread.
There is, however, one type of diagonal spread about which we can generalize. If a diagonal spread is done one to one and both options are of the same
type and have approximately the same delta, the diagonal spread will act very
much like a conventional calendar spread. Examples of this type of diagonal
spread are shown in Figure 11-29 (delta values are in parentheses).
Even though there are many different volatility spreads, traders tend to
classify spreads in terms of their basic volatility characteristics. While some volatility spreads may prefer movement in one direction rather than the other, a
Figure 11-29  Diagonal spreads.
Time to June expiration = 4 months
Time to April expiration = 2 months
Underlying price = 100
Volatility = 30%
+1 June 115 call
2.20 (23)
–1 April 110 call
1.60 (23)
+1 June 80 put
0.72 (–8)
–1 April 85 put
0.48 (–8)
Stock price = 100  Volatility = 20%  Interest rate = 6.00%
Time to March expiration = 3 months
Time to June expiration = 6 months
If quarterly
dividend is…
0
0.50
1.00
1.50
2.00
June 100 call
7.16
6.57
6.00
5.47
4.96
March 100 call
4.75
4.46
4.19
3.93
3.68
Call spread value
2.41
2.11
1.81
1.54
1.28
June 100 put
4.20
4.60
5.02
5.47
5.95
March 100 put
3.26
3.47
3.70
3.93
4.17
Put spread value
0.94
1.13
1.32
1.54
1.78
Figure 11-28  (continued )
--- page 214 ---

V o l at i l i t y S p r e a d s 	 197
trader who initiates a volatility spread is concerned primarily with the magnitude of movement in the underlying contract and only secondarily with the direction of movement. Therefore, all volatility spreads tend to be approximately
delta neutral. If a trader has a large positive or negative delta such that directional considerations become more important than volatility considerations,
the position can no longer be considered a volatility spread.
All spreads that are helped by movement in the underlying market have
a positive gamma. All spreads that are hurt by movement in the underlying
market have a negative gamma. A trader who has a positive gamma position
is said to be long premium and is hoping for a volatile market with large moves
in the underlying contract. A trader who has a negative gamma is said to be
short premium and is hoping for a quiet market with only small moves in the underlying market.
Because the effect of market movement and the effect of time decay always
work in opposite directions, any spread with a positive gamma will necessarily
have a negative theta, and any spread with a negative gamma will necessarily
have a positive theta. If market movement helps, the passage of time hurts, and
if market movement hurts, the passage of time helps. An option trader cannot
have it both ways.
Finally, spreads that are helped by rising volatility have a positive vega.
Spreads that are helped by falling volatility have a negative vega. In theory, the
vega refers to the sensitivity of a theoretical value to a change in the volatility of the underlying contract over the life of the option. In practice, however,
traders associate the vega with the sensitivity of an option’s price to a change
in implied volatility. Spreads with a positive vega will be helped by any increase
in implied volatility and hurt by any decline; spreads with a negative vega will
be helped by any decline in implied volatility and hurt by any increase. The
delta, gamma, theta, and vega characteristics of the primary types of volatility
spreads are summarized in Figure 11-30.
Because volatility spreads tend to be delta neutral and the theta and
gamma are always of opposite sign, we can place volatility spreads into one of
four categories depending on the effect of movement in the underlying contract (positive or negative gamma) and the effect of changes in implied volatility (positive or negative vega):
Gamma
Vega
Conditions that Will Help the Position
+
+
More volatile underlying contract; rising implied volatility
–
–
Less volatile underlying contract; falling implied volatility
+
–
More volatile underlying contract; falling implied volatility
–
+
Less volatile underlying contract; rising implied volatility
Of course, within each of these categories, some spreads will have larger
gamma or vega values and some spreads will have smaller values. Of these,
straddles and strangles tend to have the largest gamma and vega values and
therefore the greatest risk. They will result in the greatest profit when the trader
is correct in his assessment of market conditions, but they will result in the
--- page 215 ---

198
O P T I O N V O L AT I L I T Y A N D P R I C I N G
greatest loss when the trader is wrong. Butterflies and condors are at the other
end of the spectrum. These spreads yield smaller profits when the trader is
right but also result in smaller losses when the trader is wrong. Ratio spreads
and Christmas trees fall somewhere in between.
Volatility spreads can be further distinguished by their limited or unlimited risk-reward characteristics, both on the upside and on the downside. These
characteristics are also summarized in Figure 11-30.
Figure 11-31 is an evaluation table with the theoretical value, delta,
gamma, theta, vega, and rho of several different options. Following this table
are examples of volatility spreads of the types discussed in this chapter, along
with their total delta, gamma, theta, vega, and rho. (Although the examples in
Figure 11-31 assume that the underlying is stock, except for the rho, the characteristics of each type of spread will tend to be the same for options on futures.)
The reader will see that each spread does indeed have the positive or negative
sensitivities summarized in Figure 11-30. Note also that a volatility spread need
not be exactly delta neutral. (Indeed, as we saw in Chapter 7, no trader can say
with absolute certainty whether a position is really delta neutral.) In practice,
a volatility spread should have a delta that is small enough that the directional
considerations are less important than the volatility considerations. This is often a subjective judgment.
Also included in Figure 11-31 is the theoretical value of each spread. This
is simply the cash flow that results if each spread is executed at theoretical
value. Purchases of options result in a cash debit (indicated with a negative
sign), and sales represent a cash credit (indicated with a positive sign). In common terminology, a trader is said to be long the spread if it results in a cash
debit and short the spread if it results in a cash credit.
Figure 11-30  Summary of common volatility spreads.
Spread
Delta*
Gamma
Theta
Vega
Downside
Risk/Reward
Upside
Risk/Reward
Long straddle
Long strangle
Short butterfly
Short condor
Call ratio spread
  (buy more than sell)
Put ratio spread
  (buy more than sell)
0
0
0
0
0
0
+
+
+
+
+
+
–
–
–
–
–
–
+
+
+
+
+
+
Unlimited reward
Unlimited reward
Limited reward
Limited reward
Limited reward†
Unlimited reward†
Unlimited reward
Unlimited reward
Limited reward
Limited reward
Unlimited reward†
Limited reward†
Short straddle
Short strangle
Long butterfly
Long condor
Call ratio spread
  (sell more than buy)
Put ratio spread
  (sell more than buy)
0
0
0
0
0
0
–
–
–
–
–
–
+
+
+
+
+
+
–
–
–
–
–
–
Unlimited risk
Unlimited risk
Limited risk
Limited risk
Limited risk†
Unlimited risk†
Unlimited risk
Unlimited risk
Limited risk
Limited risk
Unlimited risk†
Limited risk†
Long calendar spread
Short calendar spread
0
0
–
+
+
–
+
–
Limited risk
Limited reward
Limited risk
Limited reward
*We assume that initially all spreads are approximately delta neutral.
† We refer here to the great majority of delta-neutral ratio spreads, which result in a credit when buying more than
selling and which result in a debit when selling more than buying.
--- page 216 ---

V o l at i l i t y S p r e a d s 	 199
Note that no price is given for any of the option contracts in Figure 11-31,
and therefore, no theoretical edge can be calculated for any of the spreads. The
prices at which a spread is executed may be good or bad, resulting in a positive or negative theoretical edge. But, once the spread has been established, the
market conditions that will help or hurt the spread are determined by its characteristics, not by the initial prices. Like all traders, an option trader must not
let his previous trading activity affect his current judgment. A trader’s primary
concern should not be what happened yesterday but what can be done today to
make the most of the current situation, whether attempting to maximize a potential profit or minimize a potential loss.
Choosing an Appropriate Strategy
With so many spreads available, how can we decide which type of spread is
best? First and foremost, we will want to choose spreads that have a positive
theoretical edge to ensure that if we are right about market conditions, we have
a reasonable expectation of showing a profit. Ideally, we want to construct a
spread by purchasing options that are underpriced (too cheap) and selling options that are overpriced (too expensive). If we can do this, the resulting spread,
whatever its type, will always have a positive theoretical edge.
More often, however, our opinion about volatility will result in all options
appearing either overpriced or underpriced. When this happens, it will be impossible to both buy and sell options at advantageous prices. Such a market
can be easily identified by comparing our volatility estimate with the implied
volatility in the option marketplace. If implied volatility is lower than the volatility estimate, options will be underpriced. If implied volatility is higher than
our estimate, options will be overpriced. This leads to the following principle:
If implied volatility is low, such that options generally appear underpriced, look for
spreads with a positive vega. If implied volatility is high, such that options generally
appear overpriced, look for spreads with a negative vega.
The theoretical values and deltas in Figure 11-31 have been reproduced in
Figures 11-32 and 11-33, but now prices have been included, reflecting implied
volatilities that differ from the volatility input of 20 percent. The prices in Figure 11-32 reflect an implied volatility of 17 percent. In this case, only spreads
with a positive vega will have a positive theoretical edge:

Long straddles and strangles

Short butterflies and condors

Ratio spreads—long more than short (including short Christmas trees)

Long calendar spreads
The prices in Figure 11-33 reflect an implied volatility of 23 percent. Now only
spreads with a negative vega will have a positive theoretical edge:

Short straddles and strangles

Long butterflies and condors

Ratio spreads—short more than long (including long Christmas trees)

Short calendar spreads
--- page 217 ---

200
O P T I O N V O L AT I L I T Y A N D P R I C I N G
Figure 11-31  Examples of common volatility spreads.
Stock price = 100          Time to April expiration = 2 months          Volatility = 20%          Interest rate = 6.00%          Dividend = 0
Calls
Puts
Exercise
Price
Theoretical
Value
Delta
Gamma
Theta
Vega
Rho
Theoretical
Value
Delta
Gamma
Theta
Vega
Rho
April 90
11.17
93
1.7
−0.023
0.06
0.136
.27
−7
1.7
−0.008
0.06
−0.013
April 95
6.98
79
3.6
−0.031
0.12
0.119
1.04
−21
3.6
−0.016
0.12
−0.037
April 100
3.76
56
4.8
−0.035
0.16
0.088
2.77
−44
4.8
−0.019
0.16
−0.077
April 105
1.71
33
4.4
−0.030
0.15
0.052
5.67
−67
4.4
−0.013
0.15
−0.121
April 110
0.65
16
3.0
−0.019
0.10
0.025
9.56*
−84
3.0
−0.001
0.10
−0.156
Stock price = 100          Time to June expiration = 4 months          Volatility = 20%          Interest rate = 6.00%          Dividend = 0
Calls
Puts
Exercise
Price
Theoretical
Value
Delta
Gamma
Theta
Vega
Rho
Theoretical
Value
Delta
Gamma
Theta
Vega
Rho
June 90
12.55
87
1.8
−0.022
0.12
0.249
.76
−13
1.8
−0.008
0.12
−0.045
June 95
8.71
75
2.8
−0.026
0.18
0.221
1.83
−25
2.8
−0.011
0.18
−0.089
June 100
5.62
59
3.4
−0.027
0.22
0.178
3.64
−41
3.4
−0.011
0.22
−0.148
June 105
3.36
42
3.4
−0.025
0.23
0.130
6.28
−58
3.4
−0.008
0.23
−0.213
June 110
1.85
28
2.9
−0.020
0.19
0.086
9.68*
−72
2.9
−0.002
0.19
−0.274
*The options in this table are assumed to be European, so some values may be less than intrinsic value.
e Polytechnic Library 192.99.6.125] at [07/06/16]. Copyright © McGraw-Hill Global Education Holdings, LLC. Not to be redistributed or modified in a
--- page 218 ---

V o l at i l i t y S p r e a d s 	 201
It may seem that if one encounters a market where all options are either
underpriced or overpriced, the sensible strategies are either long straddles and
strangles or short straddles and strangles. Such strategies will enable a trader
to take a position with a positive theoretical edge on both sides of the spread.
Straddles and strangles are certainly possible strategies when all options are too
cheap or too expensive. But we will see in Chapter 13 that straddles and strangles, while often having a large positive theoretical edge, can also be among
the riskiest of all strategies. For this reason, a trader will often want to consider
other spreads such as ratio spreads and butterflies, even if such spreads entail
buying some overpriced options or selling some underpriced options.
An important assumption in traditional theoretical pricing models is that
volatility is constant over the life of an option. The volatility input into the
model is assumed to be the one volatility that best describes price fluctuations in
the underlying instrument over the life of the option. When all options expire
at the same time, it is this one volatility that will, in theory, determine whether
a spread is profitable or unprofitable. But a trader may also believe that implied
volatility will rise or fall over time.
Because calendar spreads are particularly sensitive to changes in implied
volatility, rising or falling implied volatility will often affect the profitability of
calendar spreads. Consequently, we can add this corollary to the other spread
guidelines:
Long calendar spreads are likely to be profitable when implied volatility is low but is
expected to rise; short calendar spreads are likely to be profitable when implied volatility is high but is expected to fall.
These are only general guidelines, and an experienced trader may decide
to violate them if he has reason to believe that the implied volatility will not
correlate with the volatility of the underlying contract. A long calendar spread
might still be desirable in a high-implied-volatility market, but the trader must
make a prediction of how implied volatility might change with changes in realized volatility. If the market stagnates, with no movement in the underlying
contract, but the trader feels that implied volatility will remain high, a long calendar spread is a sensible strategy. The short-term option will decay, while the
long-term option will retain its value. In the same way, a short calendar spread
might still be desirable in a low-implied-volatility market if the trader feels that
the underlying contract is likely to make a large move with no commensurate
increase in implied volatility.
Adjustments
A volatility spread may be delta neutral initially, but the delta of the position
will change as market conditions change—as the price of the underlying contract rises or falls, as volatility changes, and as time passes. A spread that is delta
neutral today is unlikely to be delta neutral tomorrow. The use of a theoretical
pricing model requires a trader to continuously maintain a delta-neutral position throughout the life of the spread. Continuous adjustments are neither
--- page 219 ---

202
O P T I O N V O L AT I L I T Y A N D P R I C I N G
possible nor practical in the real world of trading, so when a trader initiates
a spread, he ought to give some thought as to how he will adjust the position.
There are essentially four possibilities:
1.	 Adjust at regular intervals. In theory, the adjustment process is assumed to
be continuous because volatility is assumed to be a continuous measure of the speed of the market. In practice, however, volatility is measured over regular time intervals, so a reasonable approach is to adjust
a position at similar regular intervals. If a trader’s volatility estimate
is based on daily price changes, the trader might adjust daily. If the
estimate is based on weekly price changes, he might adjust weekly. By
doing this, the trader is making the best attempt to emulate the assumptions built into the theoretical pricing model.
2.	 Adjust when the position becomes a predetermined number of deltas long or short.
Very few traders insist on being delta neutral all the time. Most traders accept that this is not a realistic approach both because a continuous adjustment process is physically impossible and because no one
can be certain that all the assumptions and inputs in a theoretical pricing model, from which the delta is calculated, are correct. Even if one
could be certain that all delta calculations were accurate, a trader might
still be willing to take on some directional risk. But a trader ought to
know just how much directional risk he is willing to accept. If he wants
to pursue delta-neutral strategies but believes that he can comfortably
live with a position that is up to 500 deltas long or short, then he can adjust the position any time his delta position reaches this limit. Unlike the
trader who adjusts at regular intervals, a trader who adjusts based on a
fixed number of deltas cannot be sure how often he will need to adjust
his position. In some cases, he may have to adjust very frequently; in
other cases, he may go for long periods of time without adjusting.

  The number of deltas, either long or short, that a trader is willing
to accept without adjusting depends on many factors—the typical size
of the trader’s positions, his capitalization, and his trading experience.
A new independent trader may find that he is uncomfortable with a
position that is only 200 deltas long or short. A large trading firm may
consider a position that is several thousand deltas long or short as being approximately delta neutral.
3.	 Adjust by feel. This suggestion is not made facetiously. Some traders
have good market feel. They can sense when the market is about to
move in one direction or another. If a trader has this ability, there is
no reason why he shouldn’t make use of it. Suppose that the underlying market is at 50.00 and a trader is delta neutral with a gamma of
–200. If the market falls to 48.00, the trader can estimate that he is
approximately 400 deltas long. If 400 deltas is the limit of the risk he
is willing to accept, he might decide to adjust at this point. If, however,
he is also aware that 48.00 represents strong support for the market,
--- page 220 ---

V o l at i l i t y S p r e a d s 	 203
he might choose not to adjust under the assumption that the market
is likely to rebound from the support level. If he is right, he will have
avoided an unprofitable adjustment. Of course, if he is wrong and the
market continues downward through the support level, he will regret
not having adjusted. But if the trader is right more often than not,
there is no reason why he shouldn’t take advantage of this skill.
4.	 Don’t adjust at all. This is really an extension of the second possibility, adjusting by the number of deltas. A trader who does not adjust
at all is willing to accept a directional risk equal to the maximum
number of deltas that the position can take on. If the trader sells five
straddles, the position can take on a maximum delta of ±500. The
appeal of this approach is that it eliminates all subsequent transaction costs. But, if the position takes on a large delta, the directional
considerations may become more important than the volatility considerations. If the position was initiated because of an opinion about
volatility, does it make sense for a trader to subsequently change to
an opinion about direction? Usually not. If the trader does not want
to adjust the position but he also does not want directional considerations to dominate, the only choice left is to close out the position.
If the trader decides not to adjust, when he initiates the position, he
must decide under what conditions he will be willing to hold the position and under what conditions he will close the position.
Submitting a Spread Order
We noted in Chapter 10 that a spread order can often be executed all at one
time and at one single price. This is particularly common in option markets,
where spreads are quoted with a single bid price and a single offer price regardless of the complexity of the spread. Suppose that a trader is interested in buying a straddle and receives a quote from a market maker of 6.25/6.75. If the
trader wants to sell the straddle, he will have to do so at a price of 6.25 (the bid
price); if he wants to buy the straddle, he will have to pay 6.75 (the ask price).
If the trader decides that he is willing to pay 6.75, neither he nor the market
maker really cares whether the trader pays 3.75 for the call and 3.00 for the put
or 2.00 for the call and 4.75 for the put or some other combination of call and
put prices. The only consideration is that the prices of the call and put taken
together add up to 6.75.
A market maker will always endeavor to give one bid price and one ask
price for an entire spread. If the spread is a common type, such as a straddle,
strangle, butterfly, or calendar spread, a bid and ask can usually be given very
quickly. But market makers are only human. If a spread is very complex, involving several different options in unusual ratios, it may take a market maker
several minutes to calculate the value of the spread. Regardless of the complexity of a spread, however, the market maker will make an effort to give his best
two-sided (bid and ask) market.
--- page 221 ---

204
O P T I O N V O L AT I L I T Y A N D P R I C I N G
Spread orders are common in almost all option markets, whether electronic or open outcry. Depending on the trading platform, an electronic
exchange will usually allow traders to submit bids or offers for the most common types of spreads—simple call or put spreads, straddles, strangles, and
calendar spreads. More complex spreads—butterflies, Christmas trees, and
spreads with unusual ratios—must either be executed piecemeal or submitted to a broker for execution on an open-outcry exchange where an exact description of the spread can be communicated directly to one or more market
makers.
Option spread orders may often be submitted with specific instructions as
to how the spread is to be executed. Most commonly, a spread will be submitted as either a market order (an order to be filled at the current market price)
or a limit order (an order to be filled only at a specified price). But the spread
may also be submitted as a contingency order with special execution instructions.
The following contingency orders, all of which are defined in Appendix A, are
often used in option markets:

All or none

Fill or kill

Immediate or cancel

Market if touched

Market on close

Not held

One cancels the other

Stop limit order

Stop loss order
A broker executing a spread order is responsible for adhering to any special instructions that accompany the order. Unless a trader is fully knowledgeable about market conditions or has a great deal of confidence in the broker
who will be executing the order, it may be wise to submit specific instructions
with the order as to how it is to be executed. Additionally, when one considers all the information that must be communicated with a spread order (i.e.,
the quantity, the expiration months, the exercise prices, the type of option,
and whether the order is a buy or sell), it is easy to see how incorrect information might inadvertently be transmitted with the order. For this reason, it
is also wise to double-check all orders before submitting them for execution.
Option trading can be difficult enough without the additional problems of
miscommunication.
--- page 222 ---

V o l at i l i t y S p r e a d s 	 205
Figure 11-33
Stock price = 100  Time to April expiration = 2 months  Volatility = 20%  Interest rate = 6.00%  Dividend = 0
Calls
Puts
Exercise
Price
Theoretical
Value
Price
(Implied Volatility = 23%)
Delta
Theoretical
Value
Price
(Implied Volatility = 23%)
Delta
April 90
11.17
11.36
93
.27
0.47
−7
April 95
6.98
7.35
79
1.04
1.41
−21
April 100
3.76
4.24
56
2.77
3.25
−44
April 105
1.71
2.16
33
5.67
6.12
−67
April 110
.65
0.97
16
9.56
9.87
−84
Stock price = 100  Time to June expiration = 4 months  Volatility = 20%  Interest rate = 6.00%  Dividend = 0
Calls
Puts
Exercise
Price
Theoretical
Value
Price
(Implied Volatility = 23%)
Delta
Theoretical
Value
Price
(Implied Volatility = 23%)
Delta
June 90
12.55
12.94
87
.76
1.15
−13
June 95
8.71
9.27
75
1.83
2.39
−25
June 100
5.62
6.29
59
3.64
4.31
−41
June 105
3.36
4.04
42
6.28
6.96
−58
June 110
1.85
2.45
28
9.68
10.27
−72
Long Straddle:    Buy calls and puts with the same expiration date and exercise price.
Theoretical Value
(Cash Flow)
Total
Delta
Total
Gamma
Total
Theta
Total
Vega
Total
Rho
+10 April 100 calls
+10 April 100 puts
10 x −3.76
10 x −2.77
−65.30
+10 x 56
+10 x −44
+120
+10 x 4.8
+10 x 4.8
+96.0
+10 x −.035
+10 x −.019
−.540
+10 x .16
+10 x .16
+3.20
+10 x .088
+10 x −.077
+.110
+10 June 95 calls
+30 June 95 puts
10 x −8.71
30 x −1.83
−142.00
+10 x 75
+30 x −25
0
+10 x 2.8
+30 x 2.8
+112.0
+10 x −.026
+30 x −.011
−.590
+10 x .18
+30 x .18
+7.20
+10 x .221
+30 x −.089
−.460
Figure 11-32
Stock price = 100  Time to April expiration = 2 months  Volatility = 20%  Interest rate = 6.00%  Dividend = 0
Calls
Puts
Exercise
Price
Theoretical
Value
Price
(Implied Volatility = 17%)
Delta
Theoretical
Value
Price
(Implied Volatility = 17%)
Delta
April 90
11.17
11.03
93
.27
0.13
−7
April 95
6.98
6.64
79
1.04
0.70
−21
April 100
3.76
3.28
56
2.77
2.29
−44
April 105
1.71
1.27
33
5.67
5.23
−67
April 110
.65
.38
16
9.56*
9.29
−84
Stock price = 100  Time to June expiration = 4 months  Volatility = 20%  Interest rate = 6.00%  Dividend = 0
Calls
Puts
Exercise
Price
Theoretical
Value
Price
(Implied Volatility = 17%)
Delta
Theoretical
Value
Price
(Implied Volatility = 17%)
Delta
June 90
12.55
12.22
87
0.76
0.44
−13
June 95
8.71
8.17
75
1.83
1.29
−25
June 100
5.62
4.95
59
3.64
2.97
−41
June 105
3.36
2.68
42
6.28
5.60
−58
June 110
1.85
1.30
28
9.68
9.12
−72
(continued)
--- page 223 ---

206
O P T I O N V O L AT I L I T Y A N D P R I C I N G
Long Butterfly:    Buy one option at a lower exercise price and one option at a higher exercise price, and sell
two options at an intermediate exercise price, where all options have the same expiration date and are the
same type (either all calls or all puts);  there must be an equal amount between exercise prices.
Theoretical Value
(Cash Flow)
Total
Delta
Total
Gamma
Total
Theta
Total
Vega
Total
Rho
+10 April 95 calls
−20 April 100 calls
+10 April 105 calls
10 x −6.98
20 x +3.76
10 x −1.71
−11.70
+10 x 79
−20 x 56
+10 x 33
0
+10 x 3.6
−20 x 4.8
+10 x 4.4
−16.0
+10 x −0.031
−20 x −0.035
+10 x −0.030
+0.090
+10 x 0.12
−20 x 0.16
+10 x 0.15
−0.50
+10 x 0.119
−20 x 0.088
+10 x 0.052
−0.050
+10 June 90 puts
−20 June 95 puts
+10 June 100 puts
10 x −0.76
20 x +1.83
10 x −3.64
−7.40
+10 x −13
−20 x −25
+10 x −41
−40
+10 x 1.8
−20 x 2.8
+10 x 3.4
−4.0
+10 x −0.008
−20 x −0.011
+10 x −0.011
+0.030
+10 x 0.12
−20 x 0.18
+10 x 0.22
−0.20
+10 x −0.045
−20 x −0.089
+10 x −0.148
−0.150
Short Butterfly:    Sell one option at a lower exercise price and one option at a higher exercise price, and buy
two options at an intermediate exercise price, where all options have the same expiration date and are the
same type (either all calls or all puts);  there must be an equal amount between exercise prices.
Theoretical Value
(Cash Flow)
Total
Delta
Total
Gamma
Total
Theta
Total
Vega
Total
Rho
−10 April 100 puts
+20 April 105 puts
−10 April 110 puts
10 x +2.77
20 x −5.67
10 x +9.56
+9.90
−10 x −44
+20 x −67
−10 x −84
−60
−10 x 4.8
+20 x 4.4
−10 x 3.0
+10.0
−10 x −0.019
+20 x −0.013
−10 x −0.001
−0.060
−10 x 0.16
+20 x 0.15
−10 x 0.10
+0.40
−10 x −0.077
+20 x −0.121
−10 x −0.156
−0.090
−10 June 90 calls
+20 June 95 calls
−10 June 100 calls
10 x +12.55
20 x +8.71
10 x −5.62
+7.50
−10 x 87
+20 x 75
−10 x 59
+40
−10 x 1.8
+20 x 2.8
−10 x 3.4
+4.0
−10 x −0.022
+20 x −0.026
−10 x −0.027
−0.030
−10 x 0.12
+20 x 0.18
−10 x 0.22
+0.20
−10 x 0.249
+20 x 0.221
−10 x 0.178
+0.150
(continued)
Short Straddle:     Sell calls and puts with the same expiration date and exercise price.
Theoretical value
(Cash Flow)
Total
Delta
Total
Gamma
Total
Theta
Total
Vega
Total
Rho
−20 April 105 calls
−10 April 105 puts
20 x +1.71
10 x +5.67
+90.90
−20 x 33
−10 x −67
+10
−20 x 4.4
−10 x 4.4
−132.0
−20 x −.030
−10 x −.013
+.730
−20 x .15
−10 x .15
−4.50
−20 x .052
−10 x −.121
−.170
−10 June 100 calls
−10 June 100 puts
10 x −5.62
10 x −3.64
+92.60
−10 x 59
−10 x −41
−180
−10 x 3.4
−10 x 3.4
−68.0
−10 x −.027
−10 x −.011
+.380
−10 x .22
−10 x .22
−4.40
−10 x .178
10 x −.148
−.300
Long Strangle:    Buy calls and puts with the same expiration date but different exercise prices.
Theoretical Value
(Cash Flow)
Total
Delta
Total
Gamma
Total
Theta
Total
Vega
Total
Rho
+10 April 95 puts
+10 April 110 calls
10 x −0.65
10 x −1.04
−16.90
+10 x −21
+10 x 16
−50
+10 x 3.6
+10 x 3.0
+66.0
+10 x −0.016
+10 x −0.019
−.350
+10 x 0.12
+10 x 0.10
+2.20
+10 x −0.037
+10 x 0.025
−0.120
+20 June 90 puts
+10 June 110 calls
20 x −0.76
10 x −1.85
−33.70
+20 x −13
+10 x 28
−20
+20 x 1.8
+10 x 2.9
+65.0
+20 x −0.008
+10 x −0.020
−0.360
+20 x 0.12
+10 x 0.19
+4.30
+20 x −0.045
+10 x 0.086
−0.040
Short Strangle:     Sell calls and puts with the same expiration date but different exercise prices.
Theoretical Value
(Cash Flow)
Total
Delta
Total
Gamma
Total
Theta
Total
Vega
Total
Rho
−30 April 100 puts
−40 April 105 calls
30 x +2.77
40 x +1.71
+151.50
−30 x −44
−40 x 33
0
−30 x 4.8
−40 x 4.4
−320.0
−30 x −0.019
−40 x −0.030
+1.770
−30 x 0.16
−40 x 0.15
−10.80
−30 x −0.077
−40 x 0.052
+.230
−10 June 100 calls
−10 June 105 puts
10 x +5.62
10 x +6.28
+119.00
−10 x 59
−10 x −58
−10
−10 x 3.4
−10 x 3.4
−68.0
−10 x −0.027
−10 x −0.008
+0.350
−10 x 0.22
−10 x 0.23
−4.50
−10 x 0.178
−10 x −0.213
+0.350
Figure 11-33  (continued )
--- page 224 ---

V o l at i l i t y S p r e a d s 	 207
Long Condor:    Buy two options at two outside exercise prices and sell two options at two inside exercise
prices, where all options have the same expiration date and are the same type (either all calls or all puts);
there must be an equal amount between the two higher and two lower exercise prices.
Theoretical Value
(Cash Flow)
Total
Delta
Total
Gamma
Total
Theta
Total
Vega
Total
Rho
+10 April 90 calls
−10 April 95 calls
−10 April 105 calls
+10 April 110 calls
10 x −11.17
10 x +6.98
10 x +1.71
10 x −0.65
−31.30
+10 x 93
−10 x 79
−10 x 33
+10 x 16
−30
+10 x 1.7
−10 x 3.6
−10 x 4.4
+10 x 3.0
−33.0
+10 x −0.023
−10 x −0.031
−10 x −0.030
+10 x −0.019
+0.190
+10 x 0.06
−10 x 0.16
−10 x 0.15
+10 x 0.10
−1.10
+10 x 0.136
−10 x 0.119
−10 x 0.052
+10 x 0.025
−0.100
+10 June 95 puts
−10 June 100 puts
−10 June 105 puts
+10 June 110 puts
10 x −1.83
10 x +3.64
10 x +6.28
10 x −9.68
−15.90
+10 x −25
−10 x −41
−10 x −58
+10 x −72
+20
+10 x 2.8
−10 x 3.4
−10 x 3.4
+10 x 2.9
−11.0
+10 x −0.011
−10 x −0.011
−10 x −0.008
+10 x −0.002
+0.060
+10 x 0.18
−10 x 0.22
−10 x 0.23
+10 x 0.19
−0.80
+10 x −0.089
−10 x −0.148
−10 x −0.213
+10 x −0.274
−0.020
Short Condor:    Sell two options at two outside exercise prices and buy two options at two inside exercise
prices, where all options have the same expiration date and are the same type (either all calls or all puts);
there must be an equal amount between the two higher and two lower exercise prices.
Theoretical Value
(Cash Flow)
Total
Delta
Total
Gamma
Total
Theta
Total
Vega
Total
Rho
−10 April 90 puts
+10 April 95 puts
+10 April 100 puts
−10 April 105 puts
10 x +.27
10 x −1.04
10 x −2.77
10 x +5.66
+21.30
−10 x −7
+10 x −21
+10 x −44
−10 x −67
+90
−10 x 1.7
+10 x 3.6
+10 x 4.8
−10 x 4.4
+23.0
−10 x −0.008
+10 x −0.016
+10 x −0.019
−10 x −0.013
−0.140
−10 x 0.06
+10 x 0.12
+10 x 0.16
−10 x 0.15
+0.70
−10 x −0.013
+10 x −0.037
+10 x −0.077
−10 x −0.121
+0.200
+10 June 90 calls
−10 June 95 calls
−10 June 105 calls
+10 June 110 calls
10 x −1.83
10 x +3.64
10 x +6.28
10 x −9.68
+23.30
+10 x 87
−10 x 75
−10 x 42
+10 x 28
+20
+10 x 1.8
−10 x 2.8
−10 x 3.4
+10 x 2.9
+15.0
+10 x −0.008
−10 x −0.011
−10 x −0.008
+10 x −0.002
−0.090
+10 x 0.12
−10 x 0.18
−10 x 0.23
+10 x 0.19
+1.00
+10 x 0.249
−10 x 0.221
−10 x 0.130
+10 x 0.086
+0.160
Call Ratio Spread (long more than short):    Buy  more calls at a higher exercise price and sell fewer calls at a
lower exercise price where all options have the same expiration date.
Theoretical Value
(Cash Flow)
Total
Delta
Total
Gamma
Total
Theta
Total
Vega
Total
Rho
+20 April 110 calls
−10 April 105 calls
20 x −0.65
10 x +1.71
+4.10
+20 x 16
−10 x 33
−10
+20 x 3.0
−10 x 4.4
+16.0
+20 x −0.019
−10 x −0.030
−0.080
+20 x 0.10
−10 x 0.15
+0.50
+20 x 0.025
−10 x 0.052
−0.020
+30 June 110 calls
−10 June 90 calls
30 x −1.85
10 x +12.55
+70.00
+30 x 28
−10 x 87
−30
+30 x 2.9
−10 x 1.8
+69.0
+30 x −0.020
−10 x −0.022
−0.380
+30 x 0.19
−10 x 0.12
+4.50
+30 x 0.086
−10 x 0.249
+0.090
Call Ratio Spread (short more than long):    Sell  more calls at a higher exercise price and buy fewer calls at a
lower exercise price where all options have the same expiration date.
Theoretical Value
(Cash Flow)
Total
Delta
Total
Gamma
Total
Theta
Total
Vega
Total
Rho
+20 April 95 calls
−30 April 100 calls
20 x −6.98
30 x +3.76
−26.80
+20 x 79
−30 x 56
−100
+20 x 3.6
−30 x 4.8
−72.0
+20 x −0.031
−30 x −0.035
+0.430
+20 x 0.12
−30 x 0.16
−2.40
+20 x 0.119
−30 x 0.088
−0.260
+10 June 100 calls
−20 June 110 calls
10 x −5.62
20 x −1.85
−19.20
+10 x 59
−20 x 28
+30
+10 x 3.4
−20 x 2.9
−24.0
+10 x −0.027
−20 x −0.020
+0.130
+10 x 0.22
−20 x 0.19
−1.60
+10 x 0.178
−20 x 0.086
+0.060
(continued)
Figure 11-33  (continued )
--- page 225 ---

208
O P T I O N V O L AT I L I T Y A N D P R I C I N G
Put Ratio Spread (long more than short):    Buy  more puts at a lower exercise price and sell fewer puts at a
higher exercise price where all options have the same expiration date.
Theoretical Value
(Cash Flow)
Total
Delta
Total
Gamma
Total
Theta
Total
Vega
Total
Rho
+40 April 95 puts
−10 April 110 puts
40 x −1.04
10 x +9.56
+54.00
+40 x −21
−10 x −84
0
+40 x 3.6
−10 x 3.0
+114.0
+40 x −0.016
−10 x −0.001
−0.630
+40 x 0.12
−10 x 0.10
+3.80
+40 x −0.037
−10 x −0.156
+0.080
+50 June 95 puts
−20 June 105 puts
50 x −1.83
20 x +6.28
+34.10
+50 x −25
−20 x −58
−90
+50 x 2.8
−20 x 3.4
+72.0
+50 x −0.011
−20 x −0.008
−0.390
+50 x 0.18
−20 x 0.23
+4.40
+50 x −0.089
−20 x −0.213
−0.190
Put Ratio Spread (short more than long):    Sell  more puts at a lower exercise price and buy fewer puts at a
higher exercise price where all options have the same expiration date.
Theoretical Value
(Cash Flow)
Total
Delta
Total
Gamma
Total
Theta
Total
Vega
Total
Rho
+10 April 105 puts
−30 April 95 puts
10 x −5.67
30 x +1.04
−25.50
+10 x −67
−30 x −21
−40
+10 x 4.4
−30 x 3.6
−64.0
+10 x −0.013
−30 x −0.016
+0.350
+10 x 0.15
−30 x 0.12
−2.10
+10 x −0.121
−30 x −0.037
−0.100
+30 June 105 puts
−40 June 100 puts
30 x −6.28
40 x +3.24
−42.80
+30 x −58
−40 x −41
−100
+30 x 3.4
−40 x 3.4
−34.0
+30 x −0.008
−40 x −0.011
+0.020
+30 x 0.23
−40 x 0.22
−1.90
+30 x −0.213
−40 x −0.148
−0.470
Long Call Christmas Tree:    Buy a call at at a lower exercise price and sell one call each at two higher exercise
prices, where all options have the same expiration date.
Theoretical Value
(Cash Flow)
Total
Delta
Total
Gamma
Total
Theta
Total
Vega
Total
Rho
+10 April 100 calls
−10 April 105 calls
−10 April 110 calls
10 x −3.76
10 x +1.71
10 x +0.65
−14.00
+10 x 56
−10 x 33
−10 x 16
+70
+10 x 4.8
−10 x 4.4
−10 x 3.0
−26.0
+10 x −0.035
−10 x −0.030
−10 x −0.019
+0.140
+10 x 0.16
−10 x 0.15
−10 x 0.10
−0.90
+10 x 0.088
−10 x 0.052
−10 x 0.025
+0.110
+10 June 90 calls
−10 June 100 calls
−10 June 110 calls
10 x −12.55
10 x +5.62
10 x +1.85
−50.80
+10 x 87
−10 x 59
−10 x 28
0
+10 x 1.8
−10 x 3.4
−10 x 2.9
−45.0
+10 x −0.022
−10 x −0.027
−10 x −0.020
+0.250
+10 x 0.12
−10 x 0.22
−10 x 0.19
−2.90
+10 x 0.249
−10 x 0.178
−10 x 0.086
−0.150
Short Call Christmas Tree:    Sell  a call at at a lower exercise price and buy one call each at two higher exercise
prices, where all options have the same expiration date.
Theoretical Value
(Cash Flow)
Total
Delta
Total
Gamma
Total
Theta
Total
Vega
Total
Rho
−10 April 90 calls
+10 April 100 calls
+10 April 105 calls
10 x +11.17
10 x −3.76
10 x −1.71
+57.00
−10 x 93
+10 x 56
+10 x 33
−40
−10 x 1.7
+10 x 4.8
+10 x 4.4
+75.0
−10 x −0.023
+10 x −0.035
+10 x −0.030
−0.420
−10 x 0.06
+10 x 0.16
+10 x 0.15
+2.50
−10 x 0.136
+10 x 0.088
+10 x 0.052
+0.040
−10 June 95 calls
+10 June 105 calls
+10 June 110 calls
10 x +8.71
10 x −3.36
10 x +1.85
+35.00
−10 x 75
+10 x 42
+10 x 28
−50
−10 x 2.8
+10 x 3.4
+10 x 2.9
+35.0
−10 x −0.026
+10 x −0.025
+10 x −0.020
−0.190
−10 x 0.18
+10 x 0.23
+10 x 0.19
+2.40
−10 x 0.221
+10 x 0.130
+10 x 0.086
−0.050
(continued)
Figure 11-33  (continued )
--- page 226 ---

V o l at i l i t y S p r e a d s 	 209
Long Put Christmas Tree:    Sell one put each at two lower exercise prices and buy a put at higher exercise
price, where all options have the same expiration date.
Theoretical Value
(Cash Flow)
Total
Delta
Total
Gamma
Total
Theta
Total
Vega
Total
Rho
−10 April 95 puts
−10 April 100 puts
+10 April 105 puts
10 x +1.04
10 x +2.77
10 x −5.67
−18.60
−10 x −21
−10 x −44
+10 x −67
−20
−10 x 3.6
−10 x 3.8
+10 x 4.4
−30.0
−10 x −0.016
−10 x −0.019
+10 x −0.013
+0.220
−10 x 0.12
−10 x 0.16
+10 x 0.15
−1.30
−10 x −0.037
−10 x −0.077
+10 x −0.121
−0.070
−10 June 90 puts
−10 June 105 puts
+10 June 110 puts
10 x +.76
10 x +6.28
10 x −9.68
−26.40
−10 x −13
−10 x −58
+10 x −72
−10
−10 x 1.8
−10 x 3.4
+10 x 2.9
−23.0
−10 x −0.008
−10 x −0.008
+10 x −0.002
+0.140
−10 x 0.12
−10 x 0.23
+10 x 0.19
−1.60
−10 x −0.045
−10 x −0.213
+10 x −0.274
−0.160
Short Put Christmas Tree:    buy one put each at two lower exercise prices and sell  a put at a higher exercise
price, where all options have the same expiration date.
Theoretical Value
(Cash Flow)
Total
Delta
Total
Gamma
Total
Theta
Total
Vega
Total
Rho
+10 April 95 puts
+10 April 105 puts
−10 April 110 puts
10 x −1.04
10 x −5.67
10 x +9.56
+28.50
+10 x −21
+10 x −67
−10 x −84
−40
+10 x 3.6
+10 x 4.4
−10 x 3.0
+50.0
+10 x −0.016
+10 x −0.013
−10 x −0.001
−0.280
+10 x 0.12
+10 x 0.15
−10 x 0.10
+1.70
+10 x −0.037
+10 x −0.121
−10 x −0.156
−0.020
+10 June 90 puts
+10 June 95 puts
−10 June 100 puts
10 x −.76
10 x −1.83
10 x +3.64
+10.50
+10 x −13
+10 x −25
−10 x −41
+30
+10 x 1.8
+10 x 2.8
−10 x 3.4
+12.0
+10 x −0.008
+10 x −0.011
−10 x −0.011
−0.080
+10 x 0.12
+10 x 0.18
−10 x 0.22
+0.80
+10 x −0.045
+10 x −0.089
−10 x −0.148
+0.140
Long Calendar Spread:    Buy a long-term option and sell a short-term option where both options have the
same exercise price and are the same type (either both calls or both puts).
Theoretical Value
(Cash Flow)
Total
Delta
Total
Gamma
Total
Theta
Total
Vega
Total
Rho
+10 June 100 calls
−10 April 100 calls
10 x −5.62
10 x +3.76
−18.60
+10 x 59
−10 x 56
+30
+10 x 3.4
−10 x 4.8
−14.0
+10 x −0.027
−10 x −0.035
+0.080
+10 x 0.22
−10 x 0.16
+0.60
+10 x 0.178
−10 x 0.088
+0.900
+10 June 95 puts
−10 April 95 puts
10 x −1.83
10 x +1.04
−7.90
+10 x −25
−10 x −21
−40
+10 x 2.8
−10 x 3.6
−8.0
+10 x −0.011
−10 x −0.016
+0.050
+10 x 0.18
−10 x 0.12
+0.60
+10 x −0.089
−10 x −0.037
−0.520
Short Calendar Spread:    Buy a short-term option and sell a long-term option where both options have the
same exercise price and are the same type (either both calls or both puts).
Theoretical Value
(Cash Flow)
Total
Delta
Total
Gamma
Total
Theta
Total
Vega
Total
Rho
+10 April 105 calls
−10 June 105 calls
10 x −1.71
10 x +3.36
+16.50
+10 x 33
−10 x 42
−90
+10 x 4.4
−10 x 3.4
+10.0
+10 x −0.030
−10 x −0.025
−0.050
+10 x 0.15
−10 x 0.23
−0.80
+10 x 0.052
−10 x 0.130
−0.780
+10 April 100 puts
−10 June 100 puts
10 x −2.77
10 x −3.64
+8.70
+10 x −44
−10 x −41
−30
+10 x 4.8
−10 x 3.4
+14.0
+10 x −0.019
−10 x −0.011
−0.080
+10 x 0.16
−10 x 0.22
−0.60
+10 x −0.077
−10 x −0.148
+0.710
Figure 11-33  (continued )
--- page 227 ---

210
12
Bull and Bear Spreads
Although delta-neutral volatility trading is the foundation of theoretical option pricing, there is no law that requires a trader to initiate and maintain a
delta-neutral position. Many traders prefer to trade from a bullish or bearish perspective. The trader who wishes to take a directional position has the
choice of doing so in either the underlying instrument itself, buying or selling
a futures contract or stock, or by taking the position in the option market. If
the trader takes a directional position in the option market, he must still be
aware of the volatility implications. Otherwise, he may be no better off, and
perhaps even worse, than if he had taken an outright position in the underlying contract.
Naked Positions
Because the purchase of calls or the sale of puts will create a positive delta
position and the sale of calls or purchase of puts will create a negative delta
position, we can always take a directional position in a market by taking an appropriate naked position in either calls or puts. If implied volatility is high, we
can sell puts to create a bullish position or sell calls to create a bearish position.
If implied volatility is low, we can buy calls to create a bullish position or buy
puts to create a bearish position.
The problem with this approach is that there is very little margin for error. If we purchase options, we will lose money not only if the market moves
in the wrong direction but also if the market fails to move fast enough to
offset the option’s time decay. If we sell options, time will work in our favor, but we face the prospect of unlimited risk if the market moves violently
against us. An experienced trader will prefer a strategy that improves the
risk-reward tradeoff by looking for positions with the greatest possible margin for error. This philosophy applies no less to directional strategies than
to volatility strategies.
--- page 228 ---

B u l l a n d B e a r S p r e a d s 	 211
Bull and Bear Ratio Spreads
Consider a situation where we believe that implied volatility is too high. One
possible strategy is a ratio spread where more options are sold than purchased.
With the underlying market at 101, ten weeks remaining to June expiration,
and a volatility of 30 percent, a June 100 call has a delta of 56 and a June 110
call has a delta of 28.1 A delta-neutral spread might consist of

Buy 1 June 100 call (56)

Sell 2 June 110 calls (28)
Because the spread is delta neutral, it has no particular preference for upward or downward movement in the underlying market.
Now suppose that we believe that this ratio spread is a sensible strategy,
but at the same time, we are also bullish on the market. There is no law that requires us to do this spread in a delta-neutral ratio. If we want the spread to reflect a bullish sentiment, we might adjust the ratio slightly

Buy 2 June 100 calls (56)

Sell 3 June 110 calls (28)
We have essentially the same ratio spread, but with a bullish bias. This is reflected in the total delta of +28.
There is, however, an important limitation if we use a ratio strategy to create a
bullish or bearish position. In our example, we are initially bullish, but the position
is still a ratio spread with a negative gamma. If the underlying market moves up
too quickly, the spread can invert from a positive to a negative delta. If the market
rises far enough, to 130 or 140, eventually all options will go deeply into the money,
and the deltas of both the June 100 and June 110 calls will approach 100. We will
be left with a delta position of –100. Even though we may be correct in our bullish
sentiment, the volatility characteristics of the position will eventually outweigh any
considerations of market direction. The delta values of both ratios, 1 × 2 and 2 ×
3, with respect to changes in the underlying price, are shown in Figure 12-1.
The delta can also invert in a ratio spread in which more options are purchased than sold. Unlike a negative gamma position, where the inversion is
caused by swift price movement in the underlying contract, this type of ratio
spread can invert when volatility declines or time passes. Suppose that conditions are the same as in our preceding example, but we believe that implied volatility is too low. Now we might do the following delta-neutral strategy:

Buy 2 June 110 calls (28)

Sell 1 June 100 call (56)
However, if we are bullish on the market, we can, as in the preceding example, adjust the ratio to reflect this sentiment

Buy 3 June 110 calls (28)

Sell 1 June 100 call (56)
The delta position of +28 reflects this bullish bias.
1 To generalize this and subsequent examples and to eliminate the differences between stock options and futures
options, we will assume an interest rate of 0.
--- page 229 ---

212
O P T I O N V O L AT I L I T Y A N D P R I C I N G
We know from Chapter 9 that as time passes or as volatility declines, all deltas
move away from 50. If time passes with no movement in the underlying contract,
the delta of the June 100 call will tend to rise, while the delta of the June 110 call
will tend to decline. If, after a period of time, the delta of the June 100 call rises
to 70 and the delta of the June 110 call falls to 15, the delta of the position will no
longer be +28 but will instead be –25. Because this strategy is a volatility spread,
the primary consideration, as before, is the volatility of the market. Only secondarily are we concerned with the direction of movement. If we overestimate volatility and the market moves more slowly than expected, the spread, which is initially
delta positive, can instead become delta negative. The delta values of both positions with respect to the passage of time are shown in Figure 12-2.
Bull and Bear Butterflies and Calendar Spreads
Butterflies and calendar spreads can also be executed in a way that reflects a
bullish or bearish bias. As with ratio spreads, though, their delta characteristics
can invert as market conditions change.
With high implied volatility and the underlying contract at 100, we might
create a delta-neutral position by buying the June 95/100/105 call butterfly
(buy a 95 call, sell two 100 calls, buy a 105 call). We hope that the underlying
will stay close to 100 so that at expiration the butterfly will widen to its maximum value of 5.00. If, however, we want to buy a butterfly but are also bullish
Figure 12-1  Delta of a ratio spread as the underlying price changes.
80
Position delta
90
100
110
120
Underlying price
–60
–50
–40
–30
–20
–10
0
+10
+20
+40
+1 × –2 ratio spread
+2 × –3 ratio spread
+30
