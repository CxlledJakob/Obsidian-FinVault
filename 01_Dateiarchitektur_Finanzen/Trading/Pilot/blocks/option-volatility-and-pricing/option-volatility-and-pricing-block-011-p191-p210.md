# Option Volatility and Pricing_ Advanced Trading Strategies -- Sheldon Natenberg -- 2nd ed, 2014 -- McGraw Hill Professional -- isbn13 9780071818773 -- 6a48d008bd9beef283debf7bad0b2e4a -- Anna’s Archive.pdf — pages 191–210

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
--- page 192 ---

V o l at i l i t y S p r e a d s 	 175
To understand these characteristics, let’s consider the value of a long butterfly at expiration:
Underlying Price at Expiration
80
100
120
+1 March 90 call
Position value
0
+10
+30
−2 March 100 calls
Position value
0
0
–20
+1 March 110 call
Position value
0
      0
+10
Total
0
+10
0
If the underlying price is below 90 at expiration, all the calls will expire
worthless, and the value of the position will be 0. If the underlying contract is
above 120 at expiration, the combined value of the 90 and 110 calls will equal
the value of the two 100 calls. Again, the value of the butterfly will be 0. Now
suppose that the underlying contract is between 90 and 110 at expiration, specifically, right at the inside exercise price of 100. The 90 call will be worth 10.00,
while the 100 and 110 calls will be worthless. The position will be worth exactly
10.00. If the underlying moves away from 100, the value of the butterfly will decline, but its value can never fall below 0. Summarizing, at expiration, a butterfly is worthless if the underlying contract is above or below the outside exercise
prices (sometimes referred to as the wings of the butterfly). It has its maximum
value at expiration when the underlying contract is right at the inside exercise
price (sometimes referred to as the body of the butterfly). And the maximum value
is always equal to the amount between exercise prices, in our example 10.00.
Because a butterfly at expiration always has a value between 0 and the
amount between exercise prices, in our example, a trader should be willing
to pay some amount between 0 and 10.00 for the position. The exact amount
depends on the likelihood of the underlying contract finishing close to the inside price at expiration. If there is a high probability of this occurring, a trader
might be willing to pay as much as 8.00 for the butterfly since it might very well
expand to its full value of 10.00. If, however, there is a low probability of this
occurring and, consequently, a high probability that the underlying contract
will finish outside the extreme exercise prices, a trader may only be willing to
pay 1.00 or 2.00 because he may very well lose his entire investment. This also
explains why our example position is a long butterfly. Because the position can
never be worth less than 0, a trader will always be required to pay some amount
for the position. Otherwise, there would be a riskless profit opportunity. When a
position requires an outlay of cash, a trader has bought, or is long, the position.
A butterfly will tend to be delta neutral when the inside exercise price is approximately at the money. Under these conditions, a long butterfly will tend to
act like a short straddle, while a short butterfly will tend to act like a long straddle. With either a long butterfly or a short straddle, a trader wants the underlying market to sit still (–gamma, +theta) and implied volatility to fall (–vega).
With either a short butterfly or a long straddle, a trader wants the underlying market to make a large move (+gamma, –theta) and implied volatility to
rise (+vega). But there is one important difference. While a straddle is openended in terms of either profit potential or risk, a butterfly is strictly limited.
--- page 193 ---

176
O P T I O N V O L AT I L I T Y A N D P R I C I N G
It can never be worth less than 0 nor more than the amount between exercise
prices. This is important for a trader who might want to sell straddles but who is
uncomfortable with the possibility of unlimited loss. Of course, there is always
a risk-reward tradeoff. If a long butterfly has reduced risk when the trader is
wrong, it will also have increased profit when the trader is right. For this reason,
butterflies tend to be executed in much larger sizes than straddles. A trader may
find that buying 300 butterflies (300 × 600 × 300) is actually less risky than selling 100 straddles. In option trading, size and risk do not always correlate. Some
strategies done in large sizes can have a relatively small risk, while other strategies, even when done in small sizes, can have a relatively large risk. Risk depends
not only on the size in which a strategy is executed but also on the characteristics of the strategy.
We know that a butterfly at expiration is worth its maximum when the underlying contract is right at the inside exercise price. If we assume that all options are European, with no possibility of early exercise, both a call and a put
butterfly with the same exercise prices and the same expiration dates desire exactly the same outcome and therefore have identical characteristics. Both the
March 90/100/110 call butterfly and the March 90/100/110 put butterfly will
be worth a maximum of 10.00 with the underlying price exactly at 100 at expiration and a minimum of 0 with the underlying price below 90 or above 110. If
both butterflies are not trading at the same price, there is a sure profit opportunity available by purchasing the cheaper and selling the more expensive.1
Condor
Just as a butterfly can be thought of as a straddle with limited risk or reward,
a condor can be thought of as a strangle with limited risk or reward. A condor
consists of four options, two inside exercise prices (the body of the condor) and
two outside exercise prices (the wings of the condor).2 The ratio of a condor
is always 1 × 1 × 1 × 1. Although the amount between the two inside exercise
prices can vary, there must be an equal amount between the two lowest exercise
prices and the two highest exercise prices. As with a butterfly, all options must
expire at the same time and be of the same type (either all calls or all puts). In
a long condor, the two outside exercise prices are purchased and the two inside exercise prices are sold, and vice versa for a short condor. Typical long and
short condors are shown in Figures 11-7 and 11-8.
The value of a condor at expiration can never be less than 0 nor more
than the amount between the two higher or the two lower exercise prices. A
trader who buys a condor will pay some amount between these values, expecting that the underlying contract will finish between the two intermediate exercise prices, where the condor will be worth its maximum. A trader who sells a
condor will take in some amount, expecting that the underlying contract will
finish outside the extreme exercise prices, where the condor will be worthless.
1 This is not necessarily true for butterflies consisting of American options, where early exercise is a possibility.
A sure profit would exist only if one could be certain of carrying the position to expiration.
2 Butterflies and condors fall under the general category of strategies known as wingspreads.
--- page 194 ---

V o l at i l i t y S p r e a d s 	 177
Figure 11-7  Long condor as time passes or volatility declines.
+1 March 90 call
–1 March 95 call
–1 March 105 call
+1 March 110 call
There must be an equal
amount between the
two higher and the two
lower exercise prices
+1 June 35 put
–1 June 40 put
–1 June 45 put
+1 June 50 put
Buy a call (put)
at a higher
exercise price
Buy a call (put)
at a lower
exercise price
All options must
have the same
expiration date
Sell a call (put)
at a higher
intermediate
exercise price
Sell a call (put)
at a lower
intermediate
exercise price
Value at expiration
Lower underlying prices
Higher underlying prices
Position value
Figure 11-8  Short condor as time passes or volatility declines.
All options must
have the same
expiration date
Buy a call (put)
at a lower
exercise price
Buy a call (put)
at a higher
exercise price
–1 June 35 put
+1 June 40 put
+1 June 45 put
–1 June 50 put
–1 March 90 call
+1 March 95 call
+1 March 105 call
–1 March 110 call
There must be an equal
amount between the
two higher and the two
lower exercise prices
Sell a call (put)
at a higher
intermediate
exercise price
Sell a call (put)
at a lower
intermediate
exercise price
Value at expiration
Lower underlying prices
Higher underlying prices
Position value
--- page 195 ---

178
O P T I O N V O L AT I L I T Y A N D P R I C I N G
A condor will be approximately delta neutral when the underlying contract is midway between the two inside exercise prices. When all options are
European, the value and characteristics of a call condor and put condor will
be identical.
The four volatility spreads that we just described—straddles, strangles, butterflies, and condors—all have symmetrical P&L graphs. When executed delta
neutral, as is most common, these strategies have no preference as to the direction of movement in the underlying market. Long straddles and strangles and
short butterflies and condors prefer movement in the underlying market and
an increase in implied volatility (+gamma, –theta , +vega). Short straddles and
strangles and long butterflies and condors prefer no movement in the underlying market and a decline in implied volatility (–gamma, +theta, –vega). These
characteristics are summarized in Figure 11-9.
Figure 11-9  Symmetrical strategies.
Long straddle
+gamma / –theta / +vega
Short straddle
–gamma / +theta / –vega
Long strangle
+gamma / –theta / +vega
Short strangle
–gamma / +theta / –vega
Short butterfly
+gamma / –theta / +vega
Long butterfly
–gamma / +theta / –vega
Short condor
+gamma / –theta / +vega
Long condor
–gamma / +theta / –vega
--- page 196 ---

V o l at i l i t y S p r e a d s 	 179
Ratio Spread
In a volatility spread, a trader need not be totally indifferent to the direction of
movement in the underlying market. The trader may believe that movement
in one direction is more likely than movement in the other direction. Given
this, the trader may wish to construct a spread that either maximizes his profit
or minimizes his loss when movement occurs in one direction rather than the
other. In order to achieve this, a trader can construct a ratio spread—buying and
selling unequal numbers of options where all options are the same type and
expire at the same time. As with other volatility positions, the spread is typically delta neutral.
Consider the following delta-neutral position with the underlying contract
trading at 100 (delta values are in parentheses):
Contract Position
Price per Contract
+3 October 105 call (25)
1.00
–1 October 95 call (75)
6.00
Now let’s consider three possible prices for the underlying contract at expiration:
Underlying Price
95 Call P&L
105 Call P&L
Total P&L
80
+6.00 – 0 = +6.00
3 × (–1.00 + 0) = –3.00
+3.00
120
+6.00 – 25.00 = –19.00
3 × (–1.00 + 15.00) = +42.00
+23.00
100
+6.00 – 5.00 = +1.00
3 × (–1.00 + 0) = –3.00
–2.00
If the underlying contract makes a very big move in either direction, the
position will show a profit. Of course, the profit will be much larger if the move
is upward. If the underlying sits at 100 until expiration, the position will show
a loss. This call ratio spread, where more calls are purchased than sold, wants
movement in the underlying contract but clearly prefers upward movement,
where the potential profit is unlimited. The P&L diagram for this type of strategy is shown in Figure 11-10.
The same type of position can be created using puts. A put ratio spread,
where more puts are purchased than sold, also prefers movement in the underlying contract. But now there is a preference for downward movement because the profit potential on the downside will be unlimited. This is shown in
Figure 11-11.
A ratio spread where more options are purchased than sold is sometimes
referred to as backspread. Regardless of whether the spread consists of calls or
puts, this type of spread always wants movement in the underlying market
(+gamma, –theta) and/or an increase in implied volatility (+vega).
In a ratio spread where more options are purchased than sold, the spread
will be worthless if the underlying contract makes a large enough downward
move in the case of calls or a large enough upward move in the case of puts. For
either spread to result in a profit, it must be executed initially for a credit, and
this is a typical characteristic of these types of spreads. Indeed, under the assumptions of a traditional theoretical pricing model, a delta-neutral ratio spread
where more options are purchased than sold should always result in a credit.
--- page 197 ---

180
O P T I O N V O L AT I L I T Y A N D P R I C I N G
Figure 11-10  Call ratio spread (buy more than sell) as time passes or volatility declines.
+3 October 105 calls
–1 October 95 call
+2 April 45 calls
–1 April 40 call
Buy multiple
calls at a higher
exercise price
Sell a call
at a lower
exercise price
All options must
have the same
expiration date
Value at expiration
Lower underlying prices
Higher underlying prices
Position value
Figure 11-11  Put ratio spread (buy more than sell) as time passes or volatility declines.
Buy multiple
puts at a lower
exercise price
Value at expiration
All options must
have the same
expiration date
Sell a put
at a higher
exercise price
+4 October 90 puts
–1 October 100 put
+3 April 35 puts
–2 April 40 puts
Lower underlying prices
Higher underlying prices
Position value
Ratio spreads are often used to limit the risk in one direction. If we sell
more calls than we buy, the spread will act like a short straddle (–gamma,
+theta, –vega) but with limited downside risk. If we sell more puts than we buy,
--- page 198 ---

V o l at i l i t y S p r e a d s 	 181
Figure 11-12  Call ratio spread (sell more than buy) as time passes or volatility declines.
+1 October 95 call
–3 October 105 calls
Buy a call
at a lower
exercise price
+1 April 40 call
–2 April 45 calls
Sell multiple
calls at a higher
exercise price
All options must
have the same
expiration date
Value at expiration
Lower underlying prices
Higher underlying prices
Position value
Figure 11-13  Put ratio spread (sell more than buy) as time passes or volatility declines.
+1 October 100 put
–4 October 90 puts
+2 April 40 puts
–3 April 35 puts
Sell multiple
puts at a lower
exercise price
Buy a put
at a higher
exercise price
All options must
have the same
expiration date
Value at expiration
Lower underlying prices
Higher underlying prices
Position value
the spread will have limited upside risk. The P&L diagrams for these types of
spreads are shown Figures 11-12 and 11-13.
--- page 199 ---

182
O P T I O N V O L AT I L I T Y A N D P R I C I N G
A ratio spread where more options are sold than purchased is sometimes referred to as frontspread .3 Using calls, the position will be worthless at expiration if
the underlying contract is below the lower exercise price. Using puts, the position will be worthless at expiration if the underlying contract is above the higher
exercise price. The fact that the value of the position cannot fall below 0 limits the downside risk if more calls are sold than purchased and the upside risk if
more puts are sold than purchased.
When executed as a single trade, ratio spreads are usually submitted using
simple ratios, the most common being 2 to 1. However, other ratios—3 to 1, 4
to 1, or 3 to 2—are also relatively common.
Christmas Tree
Ratio spreads tend to mimic straddles, but with the risk or reward limited in
one direction. We can also construct strategies that mimic strangles, but again
with limited risk or reward in one direction. Such spreads are known as either
Christmas trees or ladders.4
A call Christmas tree involves buying (selling) a call at a lower exercise
price and selling (buying) one call each at two higher exercise prices. A put
Christmas tree involves buying (selling) a put at a higher exercise price and selling (buying) one put each at two lower exercise prices. All options must be the
same type and expire at the same time, with exercise prices most often chosen
so that the entire position is delta neutral. When one option is bought and two
options sold (a long Christmas tree), the position acts like a short strangle but
with limited risk in one direction. When one option is sold and two options
bought (a short Christmas tree), the position acts like a long strangle but with
limited profit potential in one direction. P&L diagrams for typical Christmas
trees are shown in Figures 11-14 through 11-17.
Although ratio spreads and Christmas trees have nonsymmetrical P&L
graphs, their volatility characteristics tend to mimic straddles and strangles. A
spread in which more options are purchased than sold will prefer movement
in the underlying market and/or an increase in implied volatility (+gamma,
–theta, +vega). A spread in which more options are sold than purchased will
prefer no movement in the underlying market and/or a decline in implied volatility (–gamma, +theta, –vega). The characteristics of nonsymmetrical spreads
are summarized in Figure 11-18.
Calendar Spread
If all options in a spread expire at the same time, the value of the spread at expiration depends solely on the underlying price. If, however, the spread consists
of options that expire at different times, the spread’s value depends not only on
3 The terms backspread and frontspread date from the early days of option trading in the United States but
are now used infrequently except by some older traders. Most traders simply refer to these strategies as ratio
spreads, specifying whether more options are purchased or sold and the ratio of long to short options.
4 The term ladder may also refer to a type of exotic option.
--- page 200 ---

V o l at i l i t y S p r e a d s 	 183
Figure 11-15  Short call Christmas tree as time passes or volatility declines.
–1 October 90 call
+1 October 95 call
+1 October 105 call
All options must
have the same
expiration date
Buy a call
at a higher
exercise price
Sell a call
at a lower
exercise price
Buy a call at
a still higher
exercise price
–1 April 80 call
+1 April 90 call
+1 April 110 call
Value at expiration
Lower underlying prices
Higher underlying prices
Position value
Figure 11-14  Long call Christmas tree as time passes or volatility declines.
Buy a call
at a lower
exercise price
+1 October 90 call
–1 October 95 call
–1 October 105 call
+1 April 80 call
–1 April 90 call
–1 April 110 call
All options must
have the same
expiration date
Sell a call
at a higher
exercise price
Sell a call at
a still higher
exercise price
Value at expiration
Lower underlying prices
Higher underlying prices
Position value
--- page 201 ---

184
O P T I O N V O L AT I L I T Y A N D P R I C I N G
Figure 11-17  Short put Christmas tree as time passes or volatility declines.
All options must
have the same
expiration date
–1 October 110 put
+1 October 105 put
+1 October 95 put
–1 April 120 put
+1 April 110 put
+1 April 90 put
Sell a put
at a higher
exercise price
Buy a put at
a still lower
exercise price
Value at expiration
Buy a put
at a lower
exercise price
Lower underlying prices
Higher underlying prices
Position value
Figure 11-16  Long put Christmas tree as time passes or volatility declines.
Sell a put at
a still lower
exercise price
All options must
have the same
expiration date
Sell a put
at a lower
exercise price
+1 October 110 put
–1 October 105 put
–1 October 95 put
Buy a put
at a higher
exercise price
+1 April 120 put
–1 April 110 put
–1 April 90 put
Value at expiration
Lower underlying prices
Higher underlying prices
Position value
--- page 202 ---

V o l at i l i t y S p r e a d s 	 185
where the underlying market is when the short-term option expires but also on
what will happen between that date and the date on which the long-term option expires. Calendar spreads, sometimes referred to as time spreads or horizontal
spreads,5 consist of option positions that expire in different months.
The most common type of calendar spread consists of opposing positions
in two options of the same type (either both calls or both puts) where both options have the same exercise price. When the long-term option is purchased
and the short-term option is sold, a trader is long the calendar spread; when the
short-term option is purchased and the long-term option is sold, the trader is
short the calendar spread. Because a long-term option will typically be worth
5 In the early days of floor trading on option exchanges, expiration months were listed horizontally on the exchange display boards—hence the term horizontal spread for strategies consisting of options with different expiration months.
Figure 11-18  Nonsymmetrical strategies.
+gamma / –theta / +vega
+gamma / –theta / +vega
Short call Christmas tree
+gamma / –theta / +vega
Short put Christmas tree
+gamma / –theta / +vega
–gamma / +theta / –vega
–gamma / +theta / –vega
Long call Christmas tree
–gamma / +theta / –vega
Long put Christmas tree
–gamma / +theta / –vega
Call ratio spread
(buy more than sell)
Call ratio spread
(sell more than sell)
Put ratio spread
(buy more than sell)
Put ratio spread
(sell more than sell)
--- page 203 ---

186
O P T I O N V O L AT I L I T Y A N D P R I C I N G
more than a short-term option, this is consistent with the practice of referring
to any strategy that is executed at a debit as a long position and any spread that
is executed for a credit as a short position.
Although calendar spreads are most commonly executed one to one (one
contract purchased for each contract sold), a trader may ratio a calendar spread
to reflect a bullish, bearish, or neutral market sentiment. For purposes of discussion, we will focus on one-to-one calendar spreads (one long-term option
for each short-term option) that are approximately delta neutral. Because atthe-money options have delta values close to 50, the most common calendar
spreads consist of long and short at-the-money options.6
The value of a calendar spread depends not only on movement in the underlying market but also on the marketplace’s expectations about future market movement as reflected in the implied volatility. Because of this, a calendar
spread has characteristics that differ from the other spreads we have discussed.
If we assume that the options making up a calendar spread are approximately
at the money, calendar spreads have two important characteristics:
1.	 A calendar spread will increase in value if time passes with no movement in the underlying contract.
2.	 A calendar spread will increase in value if implied volatility rises and
decline in value if implied volatility falls.
Why should a calendar spread become more valuable as time passes? Consider the following spread, where the underlying contract, which is currently
trading at 100, is the same for both options:

+1 June 100 call

–1 April 100 call
Suppose that there are four months remaining to June expiration and two
months remaining to April expiration. If we assume a constant underlying
price of 100 and a constant volatility of 20 percent, the value of the individual options as time passes, as well as the value of the spread, is shown in
Figure 11-19.
The spread is initially worth 1.34, but as time passes, both options begin to
decay. However the April option, with less time remaining to expiration, decays
more rapidly than the June option. Over the first month, the April option loses
0.96, while the June option loses only 0.61. The spread has increased to 1.69.
Over the next month, with the underlying contract still at 100, the April
option, because it is at the money, must give up its entire value of 2.30. The
June option will also continue to decay, and at a slightly greater rate, losing
0.73. But the calendar spread has still increased to 3.26.
The increase in value of the calendar spread as time passes is the result
of an important characteristic of theta that was noted in Chapter 8: as time
to expiration grows shorter, the theta of an at-the-money option increases.
6 To be more exact, at-the-forward options tend to have deltas closest to 50. For this reason, a trader might
prefer a calendar spread that consists of at-the-forward options.
--- page 204 ---

V o l at i l i t y S p r e a d s 	 187
A short-term at-the-money option decays more rapidly than a long-term atthe-money option.
What will happen if the underlying contract does not sit still but instead
makes a large upward or downward move? The value of a calendar spread depends on the long-term option retaining as much time value as possible while
the short-term option decays. This will be true if both options remain at the
money because an at-the-money option always has the greatest amount of
time value. As an option moves either into the money or out of the money, its
time value will disappear. A long-term option will always have greater time value
than a short-term option. But, if the movement in the underlying contract is
large enough and the option moves very deeply into the money or very far out
of the money, even a long-term option will eventually lose almost all or its time
value. This will cause the calendar spread to collapse, as shown in Figure 11-20.
Now let’s consider the effect of changing volatility on a calendar spread.
The value of the April/June 100 call calendar spread at different volatilities is
shown in Figure 11-21.
As we raise or lower volatility, both options rise or fall in value, but the June
option changes more quickly than the April option. We touched on this characteristic in Chapter 6, where we noted that a change in volatility will have
a greater effect on a long-term option than on an equivalent short-term option. In other words, long-term options have greater vega values than short-term
Figure 11-20  The value of a calendar spread as the underlying price changes.
Theoretical Value if the Underlying Price Is…
Option
80
90
100
110
120
June 100 call
0.10
1.07
4.60
11.39
20.31
April 100 call
0.01
0.36
3.26
10.51
20.04
Spread value
0.09
0.71
1.34
0.88
0.27
Figure 11-19  The value of a calendar spread as time passes.
Contract Month
Time to Expiration
June
4 months
3 months
2 months
April
2 months
1 month
0
Option
Value
June 100 call
4.60
3.99
3.26
April 100 call
3.26
2.30
0
Spread value
1.34
1.69
3.26
--- page 205 ---

188
O P T I O N V O L AT I L I T Y A N D P R I C I N G
options. This difference in sensitivity to a change in volatility causes the calendar
spread to widen if we increase volatility and to narrow if we reduce volatility.
A trader who is long a calendar spread wants two apparently contradictory
conditions in the marketplace. First, he wants the underlying contract to sit still
in order to take advantage of the greater time decay for the short-term option.
Second, he wants everyone to think that the market is going to move so that
implied volatility will rise, causing the long-term option to rise in price more
quickly than the short-term option. Can this happen? Can the market remain
unchanged yet everyone think that it will move? In fact, it happens quite often
because events that do not have an immediate effect on the underlying contract
may be perceived to have a future effect on the underlying.
The most common example occurs when news is pending that is likely to
affect the underlying contract but whose exact effect is unknown. Consider a
company that announces that its CEO will make an important statement one
week from today. If no one knows the content of the statement, there is unlikely
to be any significant change in the company’s stock price prior to the statement.
But traders will assume that the statement, when it is made, will have an effect,
perhaps a dramatic one, on the stock price. The possibility of future movement
in the stock price will cause implied volatility to rise. This combination of conditions—the lack of movement in the underlying stock together with rising implied volatility—will cause calendar spreads to widen.
Of course, the assumption of future stock movement as a result of the
CEO’s statement is just that—an assumption. If the statement turns out to be
irrelevant to the company’s fortunes (the CEO wanted to announce that he
and his wife just became grandparents), any presumption of future volatility
is removed. The result will be a decline in implied volatility, causing calendar
spreads to narrow.
The effect of implied volatility is what distinguishes time spreads from the
other types of spreads we have discussed. Long straddles, long strangles, and
short butterflies all want the volatility of the underlying contract as well as implied volatility to rise (+gamma, +vega). Short straddles, short strangles, and
long butterflies all want the volatility of the underlying contract as well as implied volatility to fall (–gamma, –vega). But with calendar spreads underlying
volatility and implied volatility have opposite effects. A quiet market or an increase in implied volatility will help a long calendar spread (–gamma, +vega),
while a big move in the underlying market or a decline in implied volatility will
Figure 11-21  The value of a calendar spread as volatility changes.
Theoretical Value if Volatility Is …
Option
10 percent
15 percent
20 percent
25 percent
30 percent
June 100 call
2.30
3.45
4.60
5.75
6.90
April 100 call
1.63
2.44
3.26
4.07
4.88
Spread value
 0.67
1.01
1.34
1.68
2.02
--- page 206 ---

V o l at i l i t y S p r e a d s 	 189
Figure 11-22  Long calendar spread as time passes.
+1 December 100 call
–1 October 100 call
Value at expiration of
the short-term option
Buy a long-term
option and sell a
short-term option
Both options must
be the same type
(both calls or both puts)
and have the same
exercise price
+1 June 50 put
–1 March 50 put
Lower underlying prices
Higher underlying prices
Position value
Figure 11-23  Short calendar spread as time passes.
Buy a long-term
option and sell a
short-term option
Both options must
be the same type
(both calls or both puts)
and have the same
exercise price.
+1 October 100 call
−1 December 100 call
Value at expiration of
the short-term option
+1 March 50 put
−1 June 50 put
Lower underlying prices
Higher underlying prices
Position value
help a short calendar spread (+gamma, –vega). This opposite effect is what
gives calendar spreads their unique characteristics.
Figures 11-22 and 11-23 show the value of long and short calendar
spreads as time passes. Figures 11-24 and 11-25 show the value as volatility
changes.
--- page 207 ---

190
O P T I O N V O L AT I L I T Y A N D P R I C I N G
Figure 11-24  Long calendar spread as volatility declines.
Buy a long-term
option and sell a
short-term option
Lower underlying prices
Higher underlying prices
Position value
Figure 11-25  Short calendar spread as volatility declines.
Buy a short-term
option and sell a
long-term option
Lower underlying prices
Higher underlying prices
Position value
Although the effects of time and volatility apply to calendar spreads in all
markets, there may be other considerations, depending on the specific underlying market. In the foregoing examples, we assumed that the underlying contract for both the shortand long-term option was the same. In the stock option
--- page 208 ---

V o l at i l i t y S p r e a d s 	 191
market, this will always be true. The underlying contract for General Electric
(GE) options, regardless of the expiration month, is always GE stock. And GE
stock can only have a single price at any one time. But in a futures market the
underlying for a futures option is a specific futures contract, and different option expirations can have different underlying futures contracts.
Consider a futures market where there are four futures months: March,
June, September, and December. If serial months are available, an April/June
calendar spread will have the same underlying contract, June futures. But a
March/June calendar spread will have one underlying contract for March options, a March future, and a different underlying contract for June options, a
June future. Although one might expect March futures and June futures to move
together, there is no guarantee that they will. Particularly in commodity markets, short-term supply and demand considerations can cause futures contracts
on the same commodity to move in different directions. In addition to volatility
considerations, a trader who buys a June/March call calendar spread must also
consider the possibility that March futures will rise relative to June futures.
In order to offset the risk of futures contracts moving against a calendarspread position, it is common in commodity futures markets for a trader to offset a calendar spread with an opposing position in the futures market. In our
example, if a trader buys the March/June call calendar spread, he can offset
the position by purchasing March futures and selling June futures.
How many futures spreads should the trader execute? If he wants a position that is sensitive only to volatility, he ought to trade the number of futures spreads required to be delta neutral. If both calls are at the money,
with deltas of approximately 50, a trader who buys 10 call calendar spreads
(buy 10 June calls, sell 10 March calls) will be long 500 deltas in June and
short 500 deltas in March. Therefore, he should buy 5 March futures contracts and sell 5 June futures contracts. The entire position will be (delta values are in parentheses)

+10 June calls (+500), – June futures (–500)

–10 March calls (–500),  +5 March futures (+500)
This type of balancing is not necessary—indeed, not possible—in stock options
because the underlying for all months is identical.
Time Butterfly
In futures markets, as opposed to option markets, a butterfly is a position in
three futures months. A trader will buy (sell) one each of a shortand longterm futures contract and sell (buy) two intermediate-term futures contracts.
A similar type of strategy can be done in option markets. A traditional option
butterfly consists of options at three different exercise prices but with the same
expiration date. A time butterfly (sometimes shortened to time fly) consists of
options at the same exercise price but with three different expiration dates. All
options must be the same type (either all calls or all puts), with approximately
the same amount of time between expirations. The outside expiration months
--- page 209 ---

192
O P T I O N V O L AT I L I T Y A N D P R I C I N G
are usually referred to as the wings and the inside expiration month as the body.
Some typical time butterflies might be

+1 May 100 call (wing)
–1 January 50 put (wing)

–2 June 100 calls (body)
+2 March 50 puts (body)

+1 July 100 call (wing)
–1 May 50 put (wing)

–1 March 70 call (wing)
+1 February 25 put (wing)

+2 June 70 calls (body)
–2 June 25 puts (body)

–1 September 70 call (wing)
+1 October 25 put (wing)
Note that a time butterfly consists of simultaneously buying or selling a
long-term calendar spread and taking an opposing position in a short-term
calendar spread, where each spread has one common expiration month.
The example May/June/July 100 call time butterfly consists of buying the
May 100 call and selling the June 100 call (selling the May/June calendar
spread) and simultaneously selling the June 100 call and buying the July 100
call (buying the June/July calendar spread).
If all options remain at the money, as time passes, the value of a calendar
spread will increase. The short-term spread must therefore be worth more than
the long-term spread. Consequently, if we buy the short-term calendar spread
and sell the long-term calendar spread (buying the body and selling the wings),
in total, we will pay more than we receive. Because the entire position will result
in a debit, we are long the time butterfly. If we do the opposite, selling the shortterm calendar spread and buying the long-term spread (selling the body and
buying the wings), we are short the time butterfly.7 This can be somewhat confusing because in a traditional butterfly consisting of different exercise prices,
the combination of buying the wings and selling the body results in a debit. But
in a time butterfly consisting of different expiration months,  buying the wings
and selling the body results in a credit.
The value of a long time butterfly as time passes and as volatility falls is
shown in Figures 11-26 and 11-27. The value of the spread will tend to collapse
as the underlying contract moves away from the exercise price, implying that
the spread has a negative gamma. Consequently, the spread must also have a
positive theta. Finally, the value of the spread falls as volatility declines, implying that the spread has a positive vega. In sum, a long time butterfly has characteristics similar to those of a long calendar spread.
Effect of Changing Interest Rates and Dividends
Thus far we have considered only the effects of changes in underlying price,
time, and volatility on the value of a volatility spread. What about changes in
interest rates and, in the case of stocks, dividends?
7 We are making the assumption here that the implied volatility of all expirations is the same. If the implied volatility differs across expiration months, a long time butterfly might in fact result in a credit.
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
