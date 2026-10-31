# Option Volatility and Pricing_ Advanced Trading Strategies -- Sheldon Natenberg -- 2nd ed, 2014 -- McGraw Hill Professional -- isbn13 9780071818773 -- 6a48d008bd9beef283debf7bad0b2e4a -- Anna’s Archive.pdf — pages 229–248

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
--- page 230 ---

B u l l a n d B e a r S p r e a d s 	 213
on the market, we can choose a butterfly in which the inside exercise price is
above the current price of the underlying contract. If the underlying is currently at 100, we might choose to buy the June 105/110/115 call butterfly. Because this position wants the underlying contract to be at the inside exercise
price of 110 at expiration and it is currently at 100, the position is a bullish butterfly. This will be reflected in the position having a positive delta.
Unfortunately, if the underlying market moves up too far, say, to 120, the
butterfly will invert from a positive to a negative delta position. Now we want
the market to fall back from 120 to 110. Whenever the underlying market is below 110, the position will be bullish; whenever the underlying market is above
110, the position will be bearish.
Conversely, if we are bearish, we can choose to buy a butterfly in which the inside exercise price is below the current price of the underlying market. But again,
if the market moves down too quickly and goes through the inside exercise price,
the position will invert from a negative to a positive delta. The delta position of a
butterfly with respect to changes in the underlying price is shown in Figure 12-3.
We can also choose a bullish or bearish calendar spread. A long calendar
spread always wants the short-term option to expire exactly at the money. A
long calendar spread will be initially bullish if the exercise price is above the
current price of the underlying contract.2 With the underlying at 100, the June/
2 In the futures market, the situation may be complicated by the fact that different futures months may be trading at different prices. Instead of choosing a traditional calendar spread, where both options have the same exercise price, the trader may have to choose a diagonal spread to ensure that the position is either bullish (delta
positive) or bearish (delta negative).
Figure 12-2  Delta of a ratio spread as time passes.
Position delta
Time to expiration (weeks)
–60
–50
–40
–30
–20
–10
0
+10
+20
–1 × +2 ratio spread
–1 × +3 ratio spread
+30
–70
1
2
3
4
5
6
7
8
9
10
0
--- page 231 ---

214
O P T I O N V O L AT I L I T Y A N D P R I C I N G
April 110 calendar spread (buy the June 110 option, sell the April 110 option of
the same type) will be bullish because the trader will want the underlying price
to rise to 110 by April expiration. The June/April 90 calendar spread (buy the
June 90 option, sell the April 90 option of the same type) will be bearish because the trader will want the underlying price to fall to 90 by April expiration.
But like a long butterfly, a long calendar spread has a negative gamma. If the
underlying contract moves through the exercise price, the delta will invert. If
the market moves from 100 to 120, the June/April 110 calendar spread, which
was initially bullish, will become bearish. If the market moves from 100 to 80,
the June/April 90 calendar spread, which was bearish initially, will become
bullish. The delta values of long calendar spreads with respect to changes in the
underlying price are shown in Figure 12-4.3
Vertical Spreads
Although we may take a bullish or bearish position by choosing an appropriate
ratio spread, butterfly, or calendar spread, in each of these positions, volatility
is still the primary concern. We can be right about market direction, but if we
are wrong about volatility, the spread may not retain the directional characteristics that we originally intended.
3 Figures 12-3 and 12-4 are very similar, and one might conclude that the characteristics of butterflies and calendar spreads are similar. But this is only true with respect to changes in the underlying price, as reflected in the
delta. The spreads will react quite differently to the passage of time and changes in implied volatility.
Figure 12-3  Delta of a long butterfly as the underlying price changes.
Positive delta
Inside
exercise price
Higher underlying prices
0
Lower underlying prices
Negative delta
When the underlying price is
below the inside exercise
price, a long butterfly is
bullish (delta positive).
When the underlying price is
above the inside exercise
price, a long butterfly is
bearish (delta negative).
--- page 232 ---

B u l l a n d B e a r S p r e a d s 	 215
If we want to focus primarily on the direction of the underlying market, we
might look for a spread in which the directional characteristics are the primary
concern and the volatility characteristics are only of secondary importance.
We would like to be certain that if the spread is initially bullish (delta positive), it
will remain bullish under all possible market conditions, and if it is initially bearish (delta negative), it will remain bearish under all possible market conditions.
The most common class of spreads that meet these requirements are simple call and put spreads. One option is purchased and one option is sold, where
both options are the same type (either both calls or both puts) and expire at the
same time. The options are distinguished only by their different exercise prices.
Such spreads may also be referred to as credit and debit spreads or vertical spreads.4
Typical spreads of this type might be

Buy 1 June 100 call

Sell 1 June 105 call
or

Buy 1 December 105 put

Sell 1 December 95 put
Simple call and put spreads are initially either bullish or bearish, and they
remain bullish or bearish no matter how market conditions change. Two options
that have different exercise prices but that are otherwise identical cannot have
identical deltas. In the first example, where the trader is long a June 100 call
and short a June 105 call, the June 100 call will always have a delta greater than
4 In the early days of trading on option exchanges, exercise prices were listed vertically on the exchange display boards—hence the term vertical spread for strategies consisting of options with difference exercise prices.
Figure 12-4  Delta of a long calendar spread as the underlying price changes.
Positive delta
Exercise
price
Higher underlying prices
0
Lower underlying prices
Negative delta
When the underlying price is
below the exercise price, a
long calendar spread is
bullish (delta positive).
When the underlying price is
below the exercise price, a
long calendar spread is
bearish (delta negative).
--- page 233 ---

216
O P T I O N V O L AT I L I T Y A N D P R I C I N G
the June 105 call. If both options are deeply in the money or very far out of the
money, the deltas may tend toward 100 or 0. But even then, the June 100 call
will have a delta that is slightly greater than that of the June 105 call. In the second example, no matter how market conditions change, the December 105 put
will always have a greater negative delta than the December 95 put.
At expiration, a call or put vertical spread will have a minimum value of 0
if both options are out of the money and a maximum value of the amount between exercise prices if both options are in the money. If the underlying contract is below 100 at expiration, the June 100/105 call spread will be worthless
because both options will be worthless. If the underlying contract is above 105,
the spread will be worth 5.00 because the June 100 call will be worth exactly
five points more than the June 105 call. Similarly, the March 95/105 put spread
will be worthless if the underlying market is above 105 at expiration, and it will
be worth 10.00 if the market is below 95.
Because a vertical spread at expiration will always have a value between 0
and the amount between exercise prices, a trader can expect the price of such
a spread to be somewhere within this range. A 100/105 call vertical spread
will trade for some amount between 0 and 5.00; a 95/105 put vertical spread
will trade for some amount between 0 and 10.00. The exact value will depend
on the likelihood of the underlying market finishing below the lower exercise
price, above the higher exercise price, or somewhere in between. If the market
is currently at 80 and gives little indication of rising, the price of the 100/105
call vertical spread will be close to 0, while the price of the 95/105 put vertical
spread will be close to 10.00. If the market is currently at 120 with little likelihood that it will fall, the price of the 100/105 call vertical spread will be close
to 5.00, while the price of the 95/105 put vertical spread will be close to 0.
If we want to do a simple bull or bear vertical spread, we have essentially
four choices. If we are bullish, we can choose a bull call spread or a bull put
spread; if we are bearish, we can choose a bear call spread or a bear put spread.
For example,

Bull call spread:
Buy a June 100 call

Sell a June 105 call

Bull put spread:
Buy a June 100 put

Sell a June 105 put

Bear call spread:
Sell a June 100 call

Buy a June 105 call

Bear put spread:
Sell a June 100 put

Buy a June 105 put
If we are bullish, we can buy a 100 call and sell a 105 call, or buy a 100 put
and sell a 105 put (in both cases, buy the lower exercise price and sell the higher).
If we are bearish, we can buy a 105 call and sell a 100 call, or buy a 105 put and
sell and 100 put (in both cases, sell the lower exercise price and buy the higher).
This may seem counterintuitive because one expects spreads that consist of puts
to have characteristics that are the opposite of those that consist of calls. But
regardless of whether a spread consists of calls or puts, whenever a trader buys the
lower exercise price and sells the higher exercise price, the position is bullish, and whenever a
trader buys the higher exercise price and sells the lower exercise price, the position is bearish.
--- page 234 ---

B u l l a n d B e a r S p r e a d s 	 217
We can see why this is true by considering either the deltas of the position
or the potential profit and loss (P&L) for the position. Consider the two example bull spreads:
Bull call spread:
Buy a June 100 call

Sell a June 105 call
Bull put spread:
Buy a June 100 put

Sell a June 105 put
Both spreads must have a positive delta. The June 100 call has a greater positive
delta than the June 105 call. The June 105 put has a greater negative delta than
the June 100 put. Multiplying with a positive sign for a purchase and a negative
sign for a sale and adding up the deltas give a total positive delta in each case.
In terms of potential profit or loss, the call spread will be done for a debit
(the June 100 call will cost more than the June 105 call) and will expand to its
maximum value of 5.00 if the underlying contract is above 105 at expiration.
The put spread will be done for a debit (the June 100 put will cost less than the
June 105 put) but will collapse to 0 if the underlying contract is above 105 at
expiration. Each spread wants the underlying to rise above 105, so each spread
must be bullish.
Not only will the total delta be very similar for call and put spreads that expire at the same time and that consist of the same exercise prices, but the profit
or loss potential for each spread, whether a call spread or put spread, will be
approximately the same.5 The expiration P&L profiles for simple bull and bear
spreads are shown in Figures 12-5 and 12-6.
5 We are assuming for the moment that all options are European, with no possibility of early exercise.
Figure 12-5  Bull spread.
Profit or loss at expiration
0
Buy the lower
exercise price
Sell the higher
exercise price
Buy an option at a lower exercise price and sell an option at a
higher exercise price, where both options are the same type (both
calls or both puts) and expire at the same time
--- page 235 ---

218
O P T I O N V O L AT I L I T Y A N D P R I C I N G
Given the many different exercise prices and expiration months available,
how can we choose the bull or bear spread that best reflects our directional expectations and that gives us the best chance to profit from those expectations?
Because options have fixed expiration dates, a trader who wants to use options to take advantage of an expected market move must first determine his
time horizon. Is the movement likely to occur in the next month? In the next
three months? In the next nine months? If it is currently May and the trader
foresees upward movement but believes that the movement is unlikely to occur
within the next two months, it does not make much sense to take a position in
June or July options. If his expectations are long term, he may have to take his
position in September or even December options. Of course, as he moves farther out in time, market liquidity may become a problem. This is a factor that
he will have to take into consideration.
Next, a trader will have to decide just how bullish or bearish he is. Is he
very confident and therefore willing to take a very large directional position?
Or is he less certain and willing to take only a limited position? Two factors determine the total directional characteristics of the position:
1.	 The delta of the selected spread
2.	 The size in which the spread is executed
A trader who wants to take a position that is 500 deltas long (equivalent to
purchasing five underlying contracts) can choose a spread that is 50 deltas long
and execute it 10 times. Or the trader can choose a different spread that is only
Figure 12-6  Bear spread.
Profit or loss at expiration
0
Sell the lower
exercise price
Buy the higher
exercise price
Buy an option at a higher exercise price and sell an option at a
lower exercise price, where both options are the same type (both
calls or both puts) and expire at the same time
--- page 236 ---

B u l l a n d B e a r S p r e a d s 	 219
25 deltas long but execute it 20 times. Both strategies result in a position that is
long 500 deltas.
In general, if all options expire at the same time and are close to at the money,
the greater the amount between exercise prices, the greater will be the delta value
of the spread. A 95/110 bull spread will be more bullish than a 95/105 bull
spread, which will, in turn, be more bullish than a 95/100 bull spread.6 Moreover,
increasing the amount between exercise prices will also increase the spread’s maximum potential profit or loss. This is shown in Figure 12-7.
Once a trader decides on the option expiration in which to take his directional position, he must decide which specific spread is best. That is, he must
decide which exercise prices to use. Consider the following table of theoretical
values and deltas:
Time to expiration = 8 weeks
Volatility = 25 percent
95 call
100 call
105 call
Theoretical value
6.82
3.91
1.99
Delta
72
52
32
Suppose that we want to do a bull call spread with these options. One choice
is to buy the 95 call and sell the 100 call. A second choice is to buy the 100 call
and sell the 105 call. Which spread is best?
6 This is not necessarily true for very deeply in-the-money spreads or very far out-of-the-money spreads. In such
cases, the deltas of both options may be very close to 100 or 0, so separating the exercise prices will have little
effect on the total delta of the spread.
Figure 12-7  As the exercise prices become farther apart, the spread takes on greater
bullish or bearish characteristics.
Profit or loss at expiration
0
Slightly bullish
Moderately bullish
Very bullish
Higher
exercise prices
Lower
exercise price
--- page 237 ---

220
O P T I O N V O L AT I L I T Y A N D P R I C I N G
The theoretical value and delta for each spread are
95/100 Spread
100/105 Spread
Theoretical value
6.82 – 3.91 = 2.91
3.91 – 1.99 = 1.92
Delta
72 – 52 = 20
52 – 32 = 20
In theory, both spreads seem to be equally bullish because they are both long 20
deltas. But the 100/105 spread, with a value of 1.92, appears to be cheaper than
the 95/100 spread, with a value of 2.91. From this we might conclude that the
100/105 spread represents the better value. But is the spread’s value the only
consideration? The value of a strategy is only important if we can compare it
with the price of the strategy. But nowhere have we said anything about price.
From an option trader’s point of view, the price of an option or strategy is
determined by the implied volatility in the marketplace. In this example, our
best estimate of volatility over the life of the options may be 25 percent, but
what will be the prices of the options if the implied volatility is either higher or
lower than 25 percent? Let’s expand our table to include option values at volatilities of 20 and 30 percent (delta values are in parentheses).
Volatility
95 Call
95/100 Spread
100 Call
100/105 Spread
105 Call
20%
6.18
3.06
3.12
1.82
1.30
25%
6.82 (72)
2.91 (20)
3.91 (52)
1.92 (20)
1.99 (32)
30%
7.50
2.81
4.69
1.98
2.71
If implied volatility in the marketplace is 20 percent, the prices of the 95/100
spread and the 100/105 spread will be 3.06 and 1.82, respectively. If our best volatility estimate is 25 percent, we have a choice. We can pay 3.06 for a spread that
we believe is worth 2.91 (the 95/100 spread), or we can pay 1.82 for a spread that
we believe is worth 1.92 (the 100/105 spread). If creating a positive theoretical
edge is our goal, the 100/105 spread, with a theoretical edge of .10, makes more
sense than the 95/100 spread with its negative theoretical edge of –.15.
Now suppose that implied volatility in the marketplace is 30 percent. The
prices of the 95/100 spread and the 100/105 spread are 2.81 and 1.98, respectively. Again we have a choice. We can pay 2.81 for a spread that is worth 2.91
(the 95/100 spread), or we can pay 1.98 for a spread that is worth 1.92 (the
100/105 spread). The 95/100 spread, with its positive theoretical edge of .10,
is now the better choice.
Even though both spreads have the same delta values, under one volatility
scenario, we seem to prefer the 95/100 spread, while under a different scenario,
we seem to prefer the 100/105 spread. The reason becomes clear if we recall
one of the basic characteristics of option evaluation introduced in Chapter 6:
If we consider three options—in the money, at the money, and out of the money—
option that are identical except for their exercise prices, the at-the-money option is
always the most sensitive in total points to a change in volatility.
--- page 238 ---

B u l l a n d B e a r S p r e a d s 	 221
If all options appear overpriced because we believe that implied volatility is too
high, in total points, the at-the-money option will be the most overpriced. If all
options appear underpriced because we believe that implied volatility is too low,
in total points, the at-the-money option will be the most underpriced. This characteristic leads to a very simple rule for choosing bull and bear vertical spreads:
If implied volatility is low, the choice of spreads should focus on purchasing the atthe-money option. If implied volatility is high, the choice should focus on selling the
at-the-money option.
Now we can see why the 100/105 call spread is a better value if implied
volatility is 20 percent, whereas the 95/100 spread is a better value if implied
volatility is 30 percent. If implied volatility is low (20 percent), we prefer to buy
the at-the-money (100) call. Having done this, we have only one choice if we
want to create a bull spread—we must sell the out-of-the-money (105) call. On
the other hand, if implied volatility is high (30 percent), we want to sell the atthe-money (100) call. Having done this, we again have only one choice if we
want to create a bull spread—we must buy the in-the-money (95) call.
The same principle is equally true for bull and bear put spreads. We always
want to focus on the at-the-money option, buying the at-the-money put when
implied volatility is low and selling the at-the-money put when implied volatility
is high. This is confirmed in the following table (delta values are in parentheses):
Volatility
95 Put
95/100
Spread
100 Put
100/105 Spread
105 Put
20%
1.18
1.94
3.12
3.18
6.30
25%
1.82 (–28)
2.09 (20)
3.91 (–48)
3.08 (20)
6.99 (–68)
30%
2.50
2.19
4.69
3.02
7.71
Suppose that we want to do a bear put spread when implied volatility is
low. In this case, we want to buy the at-the-money (100) put. Having done this,
we are forced to sell the out-of-the-money (95) put to create our bear spread
(buy the higher exercise price, sell the lower). We will pay 1.94 for the spread,
but the spread is worth 2.09. The result will be a delta position of –20 and a
positive theoretical edge of .15.
Notice that in every case, whether in a low-volatility or high-volatility environment, the spread that includes the in-the-money option always has a higher
price than the spread that includes the out-of-the-money option. To understand why, consider the result of choosing between a 95/100 and a 100/105
bull call spread under three different scenarios. In scenario 1, the market rises
and is at 110 at expiration. If this happens, both spreads will show a profit because they will both widen to their maximum value of 5.00. In scenario 2, the
market drops and is at 90 at expiration. Now both spreads will show a loss because they will both collapse to 0. Finally, consider the case where the underlying market fails to rise but also does not fall. It simply remains at 100 until
expiration. If this happens, the 100/105 spread will collapse to 0, while the
--- page 239 ---

222
O P T I O N V O L AT I L I T Y A N D P R I C I N G
95/100 spread will widen to its maximum value of 5.00. The 95/100 spread is
always more valuable than the 100/105 spread because it profits in more cases.
The 100/105 spread needs the market to rise to show a profit. The 95/100
spread does not need the market to rise; it just needs for the market not to
fall. Because the 100/105 spread requires movement, it has a positive gamma
and, consequently, a negative theta. It will decline in value as time passes. The
95/100 spread will profit even if the market sits still. It has a positive theta and,
consequently, a negative gamma.
Note also the results if the market does move. If the market rises to 110,
both spreads will show a profit, but the 100/105 spread will show a greater
profit because it was purchased at a lower price. If the market falls to 90, both
spreads will show a loss, but the 100/105 spread, because of its lower price, will
show a smaller loss. If there is a greater likelihood that the market will move,
we will always prefer the 100/105 spread. We will maximize our profits when
we are right, and we will minimize our losses when we are wrong. The likelihood of movement will depend on our estimate of volatility. If our estimate is
higher than the implied volatility, we are saying that there is a greater likelihood
of movement, so we prefer the 100/105 spread. If our estimate of volatility is
lower than the implied volatility, we are saying that there is a lower likelihood
of movement, so we prefer the 95/100 spread.
Even though we have focused on the at-the-money option, a trader is
not required to execute a bull or bear spread by first buying or selling the atthe-money option. Such spreads always involve two options, and a trader can
choose to either execute the complete spread in one transaction or leg into the
spread by trading one option at a time. In the latter case, a trader may decide to
trade the in-the-money or out-of-the-money option first and trade the at-themoney option at a later time. This is a decision that a trader must make based
on practical considerations. But regardless of how the spread is executed, the
trader should focus on the at-the-money option, either buying it when implied
volatility is low or selling it when implied volatility is high.
In practice, it is unlikely that one option will be exactly at the money. If
there is no exactly at-the-money option, a trader can focus on an option that
is closer to at the money. If the underlying market is at 103, with 95, 100, 105,
and 100 calls available, it is logical to focus on the 105 call because it is closest to
at the money. If implied volatility is low, a trader will want to buy the 105 call;
if implied volatility is high, a trader will want to sell the 105 call. He can then
trade a different option in order to create a bull or bear vertical spread.
Nor does a trader have to include the option that is closest to the money as
part of his spread. A trader who has a strong directional opinion can choose a
spread where both options are very far out of the money or very deeply in the
money. The delta values of such spreads will be very low, but the trader can create a highly leveraged position by executing each spread many times. For example, with the underlying market at 100, a trader who is strongly bullish might
buy the 115/120 call spread (assuming that such exercise prices are available).
The cost of this spread will be very low because there is a high probability that
the spread will expire worthless. But the trader will also be able to execute the
spread many times because of its low cost. If he is right and the market does
rise above 120, the spread will widen to its maximum value of 5.00, resulting
--- page 240 ---

B u l l a n d B e a r S p r e a d s 	 223
in a very large profit. Regardless of the exercise prices chosen, if implied volatility is low, the trader should buy an option that is closer to the money, and if
implied volatility is high, the trader should sell an option that is closer to the
money.
Our choice of bull or bear strategies has focused thus far on the at-themoney option, typically the option whose delta is closest to 50. This does indeed tend to be the case for options on futures. In other markets, though, the
at-the-money option may not be the option with a delta closest to 50 because,
as discussed in Chapter 5, the theoretical value of an option depends not on
the current price of the underlying contract but on the forward price. For this
reason, the choice of bull or bear spreads should really focus on the at-the-forward option. Especially in the stock option market, if interest rates are high and
there is a significant amount of time to expiration, the at-the-forward option
may have an exercise price that is considerably higher than the current stock
price. Having noted this distinction, for practical purposes, a trader will not go
too far wrong if he focuses on the at-the-money option, buying it when implied
volatility is low and selling it when implied volatility is high.
Before concluding our discussion of bull and bear spreads, it will be useful to look at graphs of the theoretical value, delta, gamma, vega, and theta
for a typical bull vertical spread, as shown in Figures 12-8 through 12-13. The
reader should take some time to look at these graphs not only because they
highlight some of the important characteristics of this very common class of
spreads but also because they serve as examples of some of the more important
characteristics of risk measurement discussed in Chapter 9. This will be especially helpful when we take a closer look at risk analysis in later chapters.
Figure 12-8  Value of a bull spread as time passes or volatility declines.
Higher underlying prices
Lower underlying prices
Position value
Value at expiration
Buy the lower
exercise price
Sell the higher
exercise price
--- page 241 ---

224
O P T I O N V O L AT I L I T Y A N D P R I C I N G
Figure 12-10  Gamma of a bull spread as time passes or volatility declines.
Position gamma
Higher underlying prices
Lower underlying prices
0
Lower
exercise
price
Higher
exercise
price
Figure 12-9  Delta of a bull spread as time passes or volatility declines.
Position delta
100
0
Higher underlying prices
Lower underlying prices
Lower
exercise price
Higher
exercise price
--- page 242 ---

B u l l a n d B e a r S p r e a d s 	 225
Figure 12-11  Vega of a bull spread as time passes or volatility declines.
Position vega
Higher underlying prices
Lower underlying prices
0
Lower
exercise price
Higher
exercise price
Figure 12-12  Theta of a bull spread as volatility declines.
Position theta
Higher underlying prices
Lower underlying prices
0
Lower
exercise
price
Higher
exercise
price
--- page 243 ---

226
O P T I O N V O L AT I L I T Y A N D P R I C I N G
For the graphs of theoretical value, delta, gamma, and vega (Figures 12-8
through 12-11), the effect of time passing or volatility declining is similar.
For the theta, however, there are slight differences, so separate theta graphs
for declining volatility (Figure 12-12) and the passage of time (Figure 12-13)
are shown. Note also that the maximum gamma, vega, and theta for vertical
spreads tend to occur when the underlying price is either just below the lowest
exercise price or just above the highest exercise price.
Finally, we might ask why a trader with a directional opinion might prefer
a vertical spread to an outright long or short position in the underlying instrument. For one thing, a vertical spread is much less risky than an outright position. A trader who wants to take a position that is 500 deltas long can either buy
5 underlying contracts or buy 25 vertical call spreads with a delta of 20 each.
The 25 vertical spreads may sound riskier than 5 underlying contracts, until we
remember that a vertical spread has limited risk, whereas the position in the
underlying has open-ended risk. Of course, greater risk also means greater reward. A trader with a long or short position in the underlying market can reap
huge rewards if the market makes a large move in his favor. By contrast, the
vertical spreader’s profits are limited, but he will also be much less bloodied if
the market makes an unexpected move in the wrong direction.
Ignoring interest considerations, the only way to profit from trading the
underlying contract is to be right about direction. If we buy the underlying
contract, the market must rise. If we sell the underlying, the market must fall.
But, with options, one need not necessarily be right about market direction.
Figure 12-13  Theta of a bull spread as time passes.
Position theta
Higher underlying prices
Lower underlying prices
0
Lower
exercise
price
Higher
exercise
price
--- page 244 ---

B u l l a n d B e a r S p r e a d s 	 227
Options also offer the additional dimension of volatility. Depending on the exercise prices that have been chosen, if the trader has correctly estimated volatility, a bull spread can be profitable if the market fails to rise or in some cases
even if it declines. A bear spread can be profitable even if the market fails
to fall. This flexibility is just one of the factors that has lead to the dramatic
growth in option markets.
--- page 245 ---

228
13
Risk Considerations
When choosing a strategy, a trader must always try to find a reasonable balance between two opposing considerations—reward and risk. Ideally, a trader
would like the greatest possible profit at the smallest possible risk. In the real
world, however, high profit usually goes hand in hand with high risk, while low
risk goes hand in hand with low profit. How should a trader balance these two
considerations? Certainly, a strategy should have an expected profit that makes
it worth executing. At the same time, the risk associated with the strategy must
be kept within reasonable bounds. And whatever the risk, it should never be
greater than what is commensurate with the potential reward.
In option trading, the reward is typically expressed in terms of theoretical
edge—the average profit resulting from a strategy, assuming that the trader’s
assessment of market conditions is correct. Unfortunately, although the theoretical edge can be expressed as one number, the risk associated with an option
position cannot be expressed in the same way. We know that options are subject
to many different risks. If we want to intelligently analyze a strategy, we may
be required to consider a variety of risks. A strategy may be reasonable with
respect to some risks but unacceptable with respect to others.
Before proceeding further in our discussion, let’s summarize the basic risks
associated with an option position:
Delta (Directional) Risk.  The risk that the underlying market will move
in one direction rather than another. When we create a position that is delta
neutral, we are trying to ensure that initially the position has no bias as to the
direction in which the underlying instrument will move. A delta-neutral position does not necessarily eliminate all directional risk, but the position is typically immune to directional risks within a limited range.
Gamma (Curvature) Risk.  The risk of a large move in the underlying contract, regardless of direction. The gamma position is a measure of how
sensitive a position is to such moves. A positive gamma position does not really
have gamma risk because such a position will, in theory, increase in value with
movement in the underlying contract. A negative gamma position, however,
--- page 246 ---

R i s k C o n s i d e r at i o n s 	 229
can quickly lose its theoretical edge with a large move in the underlying contract. The effect of such a move must always be a consideration when analyzing the relative merits of different positions.
Theta (Time Decay) Risk.  This is the opposite side of gamma risk. Positions
with positive gamma become more valuable with large moves in the underlying.
But if movement helps, the passage of time hurts. A positive gamma always goes
hand in hand with a negative theta; a negative gamma always goes hand in hand
with a positive theta. A trader with a negative theta must consider the risk in terms
of how much time can pass before the spread’s theoretical edge disappears. The
position wants movement, but if the movement fails to occur over the next day, next
week, or next month, will the spread, in theory, still be profitable?
Vega (Volatility) Risk.  The risk that the volatility that we input into the theoretical pricing model will be incorrect. If we use the wrong volatility, we have the
wrong probability distribution for the underlying contract. Because some positions have a positive vega and are hurt by declining volatility and some positions
have a negative vega and are hurt by rising volatility, vega represents a risk to
every position. A trader must always consider how much the volatility can move
against him before the potential profit from a position disappears. Most traders
prefer to interpret vega as the sensitivity of a position to a change in implied volatility. If implied volatility rises or falls, how will that change the prices of options
that make up a position? If the changes hurt the position, will the trader be able
to maintain the position in the face of adverse market conditions?
Rho (Interest-Rate) Risk.  The risk that the interest rate will change over
the life of the option. A position with a positive rho will be helped by rising interest rates and hurt by declining rates; a position with a negative rho has just
the opposite characteristics.1 Except for special situations, the interest rate is the
least important of the inputs into a theoretical pricing model. Consequently,
rho is usually considered the least important of the risk measures.
Let’s look at the relative importance of the various risks by considering several different option strategies.
Volatility Risk
For an option trader, volatility risk comes in two forms—the risk that he has
incorrectly estimated the realized volatility of the underlying contract over the
life of a strategy and the risk that implied volatility in the option market will
change. Any spread that has a nonzero gamma or vega has volatility risk.
Consider the prices and values in the theoretical evaluation table in Figure
13-1.2 What types of volatility strategies might be profitable under these conditions? Whether we compare option prices with their theoretical values or the
1 We are considering only the interest-rate risk as it applies to the evaluation of options. Changes in interest
rates can also affect the evaluation of an underlying contract, such as a bond, or even the shares in a company.
But that is a separate matter.
2 In order to focus only on volatility, we have assumed an interest rate of 0.
--- page 247 ---

230
O P T I O N V O L AT I L I T Y A N D P R I C I N G
Underlying price = 48.40
Time to May expiration = 56 days
Volatility = 18%
Interest rate = 0%
Calls
Puts
Exercise
Price
Price
Theoretical
Value
Delta
Gamma
Theta
Vega
Implied
Volatility
Price
Theoretical
Value
Delta
Gamma
Theta
Vega
Implied
Volatility
44
4.59
4.53
92
4.5
−0.0046
0.029
19.83%
0.20
0.13
−8
4.5
−0.0046
0.029
20.12%
46
2.99
2.86
78
8.8
−0.0091
0.057
20.25%
0.58
0.46
−22
8.8
−0.0091
0.057
20.09%
48
1.75
1.56
56
11.6
−0.0121
0.075
20.48%
1.35
1.16
−44
11.6
−0.0121
0.075
20.48%
50
0.93
0.73
33
10.7
−0.0111
0.069
20.88%
2.53
2.33
−67
10.7
−0.0111
0.069
20.88%
52
0.47
0.28
16
7.2
−0.0075
0.047
21.63%
4.06
3.88
−84
7.2
−0.0075
0.047
21.45%
54
0.23
0.09
6
3.7
−0.0038
0.024
22.46%
5.84
5.69
−94
3.7
−0.0038
0.024
22.73%

Time to July expiration = 112 days
Volatility = 18%
Interest rate = 0%
Calls
Puts
Price
Theoretical
Value
Delta
Gamma
Theta
Vega
Implied
Volatility
Price
Theoretical
Value
Delta
Gamma
Theta
Vega
Implied
Volatility
44
4.96
4.82
84
5.0
−0.0052
0.064
20.12%
0.56
0.42
−16
5.0
−0.0052
0.064
20.12%
46
3.52
3.32
71
7.1
−0.0074
0.091
20.21%
1.13
0.92
−29
7.1
−0.0074
0.091
20.31%
48
2.38
2.12
55
8.2
−0.0085
0.106
20.42%
1.98
1.72
−45
8.2
−0.0085
0.106
20.42%
50
1.55
1.24
39
8.0
−0.0083
0.103
20.80%
3.14
2.86
−61
8.0
−0.0083
0.103
20.71%
52
0.97
0.69
25
6.6
−0.0069
0.085
21.14%
4.58
4.29
−75
6.6
−0.0069
0.085
21.25%
54
0.60
0.35
15
4.8
−0.0050
0.062
21.64%
6.21
5.95
−85
4.8
−0.0050
0.062
21.78%
Figure 13-1
e Polytechnic Library 192.99.6.125] at [07/06/16]. Copyright © McGraw-Hill Global Education Holdings, LLC. Not to be redistributed or modified in a
--- page 248 ---

R i s k C o n s i d e r at i o n s 	 231
implied volatilities of the options with the volatility input of 18 percent, we will
reach the same conclusion: all options are overpriced. Recalling the general
guidelines in Chapter 11, under these conditions, a trader will want to consider
spreads with a negative vega:

Short straddles and strangles

Call or put ratio spreads—sell more than buy

Long butterflies

Short calendar spreads
Which of these categories is likely to represent the best spreading opportunity?
And within each category, which specific spread might represent the best riskreward tradeoff?
For the moment, let’s focus on May options. Having eliminated the possibility
of calendar spreads, any spread we choose will necessarily have a negative gamma
and negative vega. But with 12 different May options available (6 calls and 6 puts),
it’s possible to construct a number of spreads that fall into this category. How can
we make an intelligent decision about which spread might be best?
Initially, let’s consider the three strategies shown in Figure 13-2: a short
straddle that has been done in a 4:3 ratio to make it closer to delta neutral
(Spread 1), a ratio call spread (Spread 2), and a long put butterfly (Spread 3).
Each spread is approximately delta neutral and, as we would expect, has a positive theoretical edge. How can we evaluate the relative merits of each spread?
Initially, it may appear that Spread 1 is best because it has the greatest theoretical edge. If the volatility estimate of 18 percent turns out to be correct,
Spread 1 will show a profit of 6.65, Spread 2 a profit of 1.80, and Spread 3 a
profit of only .60.
But is theoretical edge our only concern? If this is true, we can simply do
each spread in larger and larger size to make the theoretical edge as big as we
want. Instead of doing Spread 2 in our original size of 10 × 20, we can increase
the size fivefold to 50 × 100. This will also increase the theoretical edge fivefold
to 9.00. This ostensibly makes Spread 2 a better strategy than Spreads 1 and 3.
Clearly, theoretical edge cannot be the only consideration.
Theoretical
Edge
Delta
Spread 1:
−15 May 48 calls
−20 May 48 puts
15 x +0.19
20 x +0.19
+6.65
−15 x +56
−20 x −44
+40
Spread 2:
+10 May 50 calls
−20 May 52 calls
10 x −0.20
20 x +0.19
+1.80
+10 x +34
−20 x +16
+20
Spread 3:
+10 May 46 puts
−20 May 48 puts
+10 May 50 puts
10 x −0.12
20 x +0.19
10 x −0.20
+0.60
+10 x −22
−20 x −44
+10 x −67
−10
Figure13-2
