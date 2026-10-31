# Option Volatility and Pricing_ Advanced Trading Strategies -- Sheldon Natenberg -- 2nd ed, 2014 -- McGraw Hill Professional -- isbn13 9780071818773 -- 6a48d008bd9beef283debf7bad0b2e4a -- Anna’s Archive.pdf — pages 248–267

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
--- page 249 ---

232
O P T I O N V O L AT I L I T Y A N D P R I C I N G
Theoretical edge is only an indication of what we expect to earn if we are
right about market conditions. Because there is no guarantee that we will be
right, we must give at least as much consideration to the question of risk. If we
are wrong about market conditions, how badly might we be hurt?
In order to focus on the risk considerations, let’s change the size of Spreads 2
and 3 so that their theoretical edge is approximately equal to that of Spread 1.
We can achieve this by increasing the size of Spread 2 to 35 × 70 and increasing
the size of Spread 3 to 100 × 200 × 100. The spreads in their new sizes with
their total theoretical edge and risk sensitivities are shown in Figure 13-3. With
all three spreads having a similar theoretical edge, we can now focus on the
risks associated with each spread.
As with all volatility positions, one consideration is the possibility of a large
price move in the underlying contract. Because each strategy has a negative
gamma, any large move will hurt the position. But will each spread be hurt to
the same degree? Because Spread 2 has the smallest negative gamma (–165.5),
we might conclude that it has the smallest risk with respect to a large move. But
this is true only under current market conditions. As market conditions change,
all risk measures, including the gamma, will almost certainly change. If the underlying contract makes a very large move such that current market conditions
no longer apply, it may not be clear what will happen to the risks associated
with each spread.
It will be easier to analyze the relative risks of the spreads if we construct a
graph of the theoretical profit or loss with respect to movement in the underlying contract. This has been done in Figure 13-4. We can see that each spread
does indeed lose value as the underlying price moves either up or down.3 However, we can also see that if there is a very large move, the spread characteristics
begin to diverge. On both the upside and downside, the losses from Spread 1,
the short straddle, continue to increase, resulting in potentially unlimited risk in
either direction. Spread 2, the ratio spread, has unlimited upside risk. On the
downside, though, it flattens out and eventually results in a very small profit.
Spread 3, the long butterfly, flattens out on both the upside and downside, so its
risk is limited regardless of direction.
3 Spreads 1 and 2, with their slightly positive delta, initially show a small gain as the market rises. Spread 3, with
its slight negative delta, initially shows a small gain as the market falls.
Theoretical
Edge
Delta
Gamma
Theta
Vega
Spread 1:
−15 May 48 calls
−20 May 48 puts
15 x +0.19
20 x +0.19
+6.65
−15 x +56
−20 x −44
+40
−15 x 11.6
−20 x 11.6
−406.0
−15 x −0.0121
−20 x −0.0121
+0.4235
−15 x 0.075
−20 x 0.075
−2.625
Spread 2:
+35 May 50 calls
−70 May 52 calls
35 x −.20
70 x +0.19
+6.30
+35 x +34
−70 x +16
+70
+35 x 10.7
−75 x 7.2
−165.5
+35 x −0.0111
−70 x −0.0075
+0.1365
+35 x 0.069
−70 x 0.047
−0.875
Spread 3:
+100 May 46 puts
−200 May 48 puts
+100 May 50 puts
100 x −0.12
200 x +0.19
100 x −0.20
+6.00
+100 x −22
−200 x −44
+100 x −67
−100
+100 x 8.8
−200 x 11.6
+100 x 10.7
−370.0
+100 x −0.0091
−200 x −0.0121
+100 x −0.0111
+0.4000
+100 x 0.057
−200 x 0.075
+100 x 0.069
−2.400
Figure 13-3
--- page 250 ---

R i s k C o n s i d e r at i o n s 	 233
Which spread is best? That depends on what the trader is worried about. If
the trader is oblivious to the risk, it won’t matter which spread he chooses. On
average, each position will show a profit of approximately 6.00. If, however, the
trader is more worried about a large downward move in the market, then perhaps Spread 2 is best. And if the trader is unwilling to accept the risk of unlimited loss in either direction, then perhaps Spread 3 is best.
In addition to the possibility of a large move, all three positions are exposed
to the risk of an incorrect volatility estimate. Because each spread has a negative vega, there will be no problem if, over the life of the option, volatility turns
out to be lower than 18 percent. In such a case, the spreads will show a profit
greater than originally expected. On the other hand, if volatility turns out to be
greater than 18 percent, this could present a problem. What will happen if volatility turns out to be 20 or 25 percent or some higher number? Each spread will
be hurt because of the negative vega, but will they be hurt to the same degree?
Because Spread 2 has the smallest vega (–.875), we might initially conclude
that it has the smallest volatility risk. But the vega, like the gamma, changes
as market conditions change. If we raise volatility, the vega of Spread 1, the
short straddle, will remain essentially unchanged because the vega of an at-themoney option is constant with respect to changes in volatility. But the vega of
Spread 3, the long butterfly, will decline because the vega of in-the-money and
out-of-the-money options (the May 46 and May 50 puts) will tend to increase as
volatility rises. With Spread 2, the vega of both options, the May 50 call and the
May 52 call, will begin to increase, so it’s not immediately clear what will happen if we increase volatility.
Figure 13-4
At an underlying price of
48.40, all three spreads
show approximately the
same theoretical profit.
Theoretical profit or loss
Underlying price
–40
–35
–30
–25
–20
–15
–5
0
+10
+5
–10
38
42
44
46
58
50
52
54
48
40
56
–45
–50
Spread 1 (short straddle)
Spread 2 (ratio spread)
Spread 3 (long butterfly)
--- page 251 ---

234
O P T I O N V O L AT I L I T Y A N D P R I C I N G
We can analyze the volatility characteristics of each spread by constructing
a graph of each spread’s value with respect to changing volatility. This is shown
in Figure 13-5. With a large change in volatility, the values of the three positions begin to diverge. If volatility rises, the spreads begin to lose value until, at
some point, the potential profit becomes a loss. In terms of volatility risk, we
might logically ask, how high can volatility rise before we begin to lose money?
That is, we might want to determine the breakeven volatility, or implied volatility,
for each spread. This is simply an extension of the general definition of implied
volatility: the volatility over the life of an option, or options, at which the position will, in theory, show neither a profit nor a loss. In Figure 13-5, we can see
that the breakeven volatility for Spread 1 (the short straddle) is approximately
21 percent, for Spread 2 (the ratio spread) approximately 23 percent, and for
Spread 3 (the long butterfly) approximately 21.5 percent. This seems to confirm that Spread 2, the ratio spread, is the least risky with respect to volatility.
However, if volatility turns out to be higher than expected, why should it
stop at 23 percent? What will happen if volatility turns out to be much higher,
perhaps 30 percent or even 40 percent? Eventually, Spread 2, the ratio spread,
which initially seemed to carry the least volatility risk, will begin to lose value
at almost the same rate as Spread 1, the short straddle. On the other hand, at
higher volatilities, the graph of Spread 3, the long butterfly, begins to flatten
out, suggesting that there is a limit to how much it can lose. Of course, we know
this because a butterfly has both limited profit potential and limited risk.
Although we might worry that volatility will increase to some value greater
than 18 percent, we might also consider what will happen if volatility turns out
to be less than 18 percent. For the same reason that rising volatility will hurt,
Figure 13-5
Volatility
Theoretical profit or loss
+40
40%
Spread 1 (short straddle)
Spread 2 (ratio spread)
Spread 3 (long butterfly)
5%
10%
15%
20%
0
+20
+30
+10
25%
30%
35%
–30
–20
–10
–40
At a volatility of 18%,
all three spreads show
approximately the same
theoretical profit.
Breakeven
volatilities
--- page 252 ---

R i s k C o n s i d e r at i o n s 	 235
falling volatility should help. In Figure 13-5, we can see that as volatility falls
below 18 percent, the profit resulting from each spread does indeed increase.
However, as volatility falls well below 18 percent, the profit from Spread 2
begins to decline, eventually falling to almost 0. On the other hand, the profit
from Spread 3 begins to accelerate.
The shapes of the graphs in Figure 13-5 are a result of each position’s
volga—the sensitivity of the vega to a change in volatility. (For a discussion of
the volga, see Chapter 9, specifically Figure 9-15.) Spread 1 has a volga close
to 0; its vega remains constant regardless of changes in volatility. Spread 2 has
a negative volga. As volatility rises, the vega becomes more negative; as volatility falls, the vega becomes less negative. This means that as volatility rises or falls,
changes in volatility work against the position, accelerating the rate of loss as volatility rises and reducing the rate of profit as volatility falls. In contrast, Spread 3
has positive volga. Changes in volatility work in favor of the position, reducing
the rate of loss as volatility rises and increasing the rate of profit as volatility falls.
Although Figure 13-5 can be interpreted as the risk of using an incorrect volatility over the life of the options, it can also be interpreted as the risk of a sudden
change in implied volatility. In terms of implied volatility risk, Spread 3 probably
represents the best value. If implied volatility begins to rise, Spread 3 will initially
lose money more quickly than Spread 2, but if implied volatility rises dramatically, Spread 3 will begin to outperform both Spreads 1 and 2 because the rate
of loss will decline. And if implied volatility falls, Spread 3 will outperform both
Spreads 1 and 2, increasing in value more quickly at lower volatilities.
Why are risk considerations so important? Every trader knows that there
are times when a strategy will result in a profit and times when it will result in
a loss. No one wins all the time. In the long run, however, a good trader’s profits will more than offset his losses. For example, suppose that a trader chooses
a strategy that will show a profit of $7,000 half the time and will show a loss
of $5,000 the other half of the time. In the long run, the trader will show an
average profit of $1,000. Suppose, though, that the first time that the trader
executes the strategy, she loses $5,000, and the trader only has $3,000? Now
the trader will not be able to stay in business for all those times when he is fortunate enough to show a profit of $7,000. Every trader knows that it is only over
long periods of time that good luck and bad luck even out. Hence no trader
will initiate a strategy where short-term bad luck might end his trading career.
Financial officers at large firms know that it is much easier to manage a
steady cash flow than one that swings wildly. In a sense, every trader is his own
financial officer. He  must sensibly manage his finances so that he can avoid being ruined by the periods of back luck that will inevitably occur, no matter how
skillfully he trades.
Practical Considerations
Considering only the gamma and vega risk, Spread 3 probably has the best
risk characteristics. It has limited risk if there is a large move in either direction and performs better than either Spread 1 or Spread 2 if there is a dramatic
change in volatility. This does not mean that Spread 3 performs better under
--- page 253 ---

236
O P T I O N V O L AT I L I T Y A N D P R I C I N G
all conditions. If the underlying market makes any downward move or there
is a small to moderate upward move, Spread 2 outperforms Spreads 1 and 3.
Spread 2 also has an advantage if there is a moderate increase in volatility.
Even if we assume that Spread 3, the long butterfly, offers the best theoretical risk-reward tradeoff, it may have some practical drawbacks. Butterflies are
actively traded in many markets, but Spread 3 is a three-sided spread, as opposed to Spreads 1 and 2, which are two-sided spreads. A three-sided spread
may be more difficult to execute in the marketplace and also may cost more in
terms of the bid-ask spread. If a trader wants to execute the complete spread
at one time, he may not be able to do so at his target prices. And if he tries to
execute one leg at a time, he will be at risk from adverse changes in the market
until the other legs can be executed.
Additionally, there is the question of market liquidity. In order to obtain a
theoretical edge commensurate with Spreads 1 and 2, it was necessary to increase
the size of the butterfly to 100 × 200 × 100. If there is insufficient liquidity in the
May 46, 48, and 50 puts to support this size, it may not be possible to execute the
butterfly in the size required to meet the trader’s profit objective. Alternatively, it
may be possible to execute part of the spread at favorable prices, but as the size
increases, the prices may become less satisfactory. Moreover, for a retail customer,
the increased size may entail greater transaction costs.
If trading considerations make Spread 3 impractical, a trader may have to
choose between Spreads 1 (short straddle) and 2 (ratio spread). If this happens,
Spread 2 is the clear winner. It allows for a much greater margin for error in
both underlying price change (gamma risk) and volatility (vega risk). A trader
who is given a choice between these two spreads will strongly prefer Spread 2.
In the real world, the choice of spreads is not always clear. One spread may
be superior with respect to one type of risk, while a different spread may be
superior with respect to a different risk. The ease with which a spread can be
executed, as well as the cost of execution, will also play a role.
Let’s consider three new spreads—Spread 4 (a short put calendar spread),
Spread 5 (a diagonal call spread), and Spread 6 (a put diagonal ratio spread). In
order to again focus on risk, the size of each spread has been adjusted so that
the theoretical edge of all three spreads is similar. The total theoretical edge
and risk sensitivities of each spread (all taken from the theoretical evaluation
table in Figure 13-1) are shown in Figure 13-6.
Theoretical
Edge
Delta
Gamma
Theta
Vega
Spread 4:
+85 May 48 puts
−85 July 48 puts
85 x −0.19
85 x +0.26
+5.95
+85 x −44
−85 x −45
+85
+85 x 11.6
−85 x 8.2
+289.0
+85 x −0.0121
−85 x −0.0085
−0.3060
+85 x 0.075
−85 x 0.106
−2.635
Spread 5:
+100 May 52 calls
−100 July 54 calls
100 x −0.19
100 x +0.25
+6.00
+100 x +16
−100 x +15
+100
+100 x 7.2
−100 x 4.8
+240.0
+100 x −0.0075
−100 x −0.0050
−0.2500
+100 x 0.047
−100 x 0.062
−1.500
Spread 6:
+30 May 48 puts
−80 July 44 puts
30 x −0.19
80 x +0.14
+5.50
+30 x −44
−80 x +16
−40
+30 x 11.6
−80 x 5.0
−52.0
+30 x −0.0121
−80 x −0.0052
+0.0530
+30 x 0.075
−80 x 0.064
−2.870
Figure 13-6
--- page 254 ---

R i s k C o n s i d e r at i o n s 	 237
Because each spread has a negative vega, we will again want to consider the
risk that volatility will turn out to be greater than our estimate of 18 percent. The
sensitivity of each spread to increasing volatility is shown in Figure 13-7. We can
see that Spread 4 has an implied volatility of approximately 20.5 percent, Spread
5 approximately 22 percent, and Spread 6 approximately 20 percent. If rising
volatility is our primary concern, Spread 5, the diagonal call spread, seems to entail the lowest risk. However, although Spread 5 loses the least in a rising-volatility
market, it also shows a smaller profit in a falling-volatility market. This may seem
like a reasonable tradeoff, except that with Spread 5, the positive effects of falling volatility begin to decline very quickly. This is due to the negative volga associated with the position. As volatility falls, the vega becomes less negative until,
at a volatility of approximately 10 percent, the vega falls to 0. Spread 6, the put
diagonal ratio spread, has an even larger negative volga; its vega turns positive if
volatility falls below 11 percent. In contrast to both Spreads 4 and 6, Spread 5,
the short calendar spread, has a volga of 0. Its vega remains constant regardless
of whether volatility rises or falls. It offers an equal tradeoff between losses when
volatility rises and profits when volatility falls.
What about the gamma risk of each spread? Here we have a situation
where not all the spreads have a gamma with the same sign. Spread 6, the
diagonal ratio spread, has a negative gamma, so it should be hurt by a large
move in the underlying. Spreads 4 and 5, however, have a positive gamma and
should profit from a large move. The graphs of the positions with respect to
changes in the underlying price are shown in Figure 13-8.
We can see in Figure 13-8 that although Spread 6, the diagonal ratio
spread, will be hurt by a move in the price of the underlying contract, the degree
Figure 13-7
Theoretical profit or loss
5%
10%
15%
20%
40%
Volatility
0
+20
+30
+40
+10
25%
30%
35%
–30
–20
–10
–40
Breakeven
volatilities
At a volatility of 18%, all
three spreads show
approximately the same
theoretical profit.
Spread 4 (short calendar spread)
Spread 5 (diagonal call spread)
Spread 6 (diagonal ratio spread)
--- page 255 ---

238
O P T I O N V O L AT I L I T Y A N D P R I C I N G
to which the move will hurt depends on the direction. With an upward move,
the potential profit will decline. But even with a very large upward move, the
spread will always retain some profit. On the downside, however, the spread’s
profit rapidly disappears, turning into a potentially unlimited loss if the downward move is large enough.
Spread 4, the short put calendar spread, and Spread 5, the diagonal call
spread, both have positive gamma and will profit from a large move. Unlike
Spread 4, though, which shows approximately equal profit in either direction,
Spread 5 shows a greater profit in an upward move and a smaller profit in a
downward move.4
There is, of course, a tradeoff between gamma and theta. If movement
in the underlying price will increase the value of Spreads 4 and 5 (positive
gamma), the passage of time with no movement will reduce the value (negative theta). It may be worthwhile to look at how much time can pass before each
spread loses its theoretical edge. This is shown in Figure 13-9.
In Figure 13-9, Spread 4 exhibits the typical decay profile for a short calendar spread that is approximately at the money. As time passes, the position loses
value at an increasingly greater rate. Spread 5, the diagonal call spread, also
loses value as time passes. But after five weeks the decay turns positive, so that
if nothing happens in the underlying market the position will eventually show a
small profit. Spread 6, the diagonal ratio spread, initially shows a small increase
in value as time passes. Eventually, though, this position is also subject to decay.
After seven weeks, its potential profit disappears completely.
4 It may appear from Figure 13-8 that Spread 5 has unlimited upside profit potential. In reality, the profit is limited by the fact that the spread between the value of the May 52 call and the July 54 call can never be greater
than 2.00. This will occur if both options go very deeply into the money.
Figure 13-8
Theoretical profit or loss
Underlying price
–20
–10
0
+10
+20
+40
+50
+60
+30
38
42
44
46
58
50
52
54
48
40
56
–30
At an underlying price of
48.40, all three spreads
show approximately the
same theoretical profit.
Spread 4 (short calendar spread)
Spread 5 (diagonal call spread)
Spread 6 (diagonal ratio spread)
--- page 256 ---

R i s k C o n s i d e r at i o n s 	 239
As must be obvious by now, the choice of spreads is never simple. As with
all trading decisions, it is a question of risk and reward. Although there are
many risks with which an option trader must deal, he will often have to ask himself which risk represents the greatest threat. Sometimes, in order to avoid one
type of risk, he will be forced to accept a different risk. Even if the trader is willing to accept some risk in a certain area, he may decide that he will only do so
to a limited degree. Then he may have to accept increased risks in other areas.
If given the choice between several different strategies, a trader can use a computer to determine the risk characteristics of the strategies under different market
conditions. Unfortunately, it may not always be possible to analyze the choices in
such detail. A trader may not have immediate access to the necessary computer
support, or market conditions may be changing so rapidly that if he fails to make an
immediate decision, opportunity may quickly pass him by. In such cases, the trader
will often have to rely on his instincts in choosing a strategy. Although there is no
substitute for experience, most traders quickly learn an important rule: straddles and
strangles are the riskiest of all spreads. This is true whether one buys or sells these strategies. New traders sometimes assume that the purchase of straddles and strangles is
not especially risky because the risk is limited. However, it can be just as painful to
lose money day after day when one buys a straddle or strangle and the market fails
to move as it is to lose the same amount of money all at once when one sells a straddle and the market makes a violent move. Of course, a trader who is right about
volatility can reap large rewards from straddles and strangles. But an experienced
trader knows that such strategies offer the least margin for error and will therefore
prefer strategies with more desirable risk characteristics.
Figure 13-9
Spread 4 (short calender spread)
Spread 5 (diagonal call spread)
Spread 6 (diagonal ratio spread)
Theoretical profit or loss
Time to May expiration (days)
–20
–15
0
–5
+5
+10
–10
7
21
28
35
49
42
14
56
–25
--- page 257 ---

240
O P T I O N V O L AT I L I T Y A N D P R I C I N G
How Much Margin for Error?
What is a reasonable margin for error in assessing the risk of a position, particularly when it comes to volatility risk? There is no clear answer because it will
usually depend on the volatility characteristics of a particular market, as well as
the trader’s experience in that market. In some cases, 5 percentage points may
be an extremely large margin for error, and the trader will feel very confident
with any strategy passing such a test. In other cases, 5 percentage points may
be almost no margin for error at all, and the trader will find that the strategy is
a constant source of worry.
Rather than focusing on margin for error, a better approach might be to
focus on the correct size in which to do a spread given a known margin for
error. Practical trading considerations aside, a trader should always choose the
spread with the best risk-reward characteristics. But sometimes even the best
spread will have only a small margin for error and consequently will entail significant risk. In such a case, a trader, if he wants to make a trade, ought to do so
in small size. If, however, a trader can execute a spread with a very large margin
for error, he ought to be willing to do the spread in a much larger size.
Consider a trader whose best estimate of volatility in a certain market is
25 percent. If implied volatility is lower than 25 percent, the trader will look
for positions with a positive vega. If the best positive-vega strategy the trader
can find is a 2 × 1 ratio spread with an implied volatility of 23 percent (only
a 2-percentage-point margin for error), he will almost certainly keep the size
of his strategy small, perhaps executing the spread only 10 times (20 × 10).
If, however, the same spread has an implied volatility of 18 percent
(a 7-percentage-point margin for error) and the trader believes that such a low
volatility is extremely rare, he may have the confidence to execute the spread in
a much larger size, perhaps 100 × 50.5 The size of a trader’s positions should
depend on the riskiness of the positions, and this, in turn, depends on how
much can go wrong before the strategy turns against the trader.
Dividends and Interest
In addition to the delta, gamma, theta, and vega risks that apply to all traders,
stock option traders may also have to consider the risk of changes in interest rates
and dividends.6 When all options expire at the same time, the risk associated with
changes in interest rates and dividends tends to be relatively small. Straddles,
strangles, ratio spreads, and butterflies may change slightly because a change in
interest rates or dividends will raise or lower the forward price. But all options are
evaluated using one and the same forward price. For calendar spreads, however,
where the options are evaluated using two different forward prices, long-term
and short-term options can react differently to changes in these inputs.
5 Size, of course, is relative. To a well-capitalized, experienced trader, even 100 × 50 may be a small trade.
6 Depending on the settlement procedure, changes in interest rates can also affect futures options. But the effect,
as discussed in Chapter 7, is usually quite small. Changes in interest rates can also affect futures options because
they may change the price of the underlying futures contract. But this can be assessed as the risk of a change in
the underlying price, not a change in interest rates.
--- page 258 ---

R i s k C o n s i d e r at i o n s 	 241
Consider the evaluation table for stock options shown in Figure 13-10. With
implied volatilities below the forecast of 29 percent, it makes sense to look for
spreads with positive vegas. Suppose that we focus on the four spreads shown in
Figure 13-11. Spreads 7 and 8 are long calendar spreads, while Spreads 9 and
10 are diagonal spreads. What are the relative merits of each spread?
Because all four spreads fall into the long calendar spread category, they
all have the typical negative-gamma and positive-vega characteristics associated with such spreads. This is shown in Figures 13-12 and 13-13. Movement
in the price of the underlying contract or falling volatility will reduce the value
of the spread. Rising volatility will increase the value of the spread. (Spreads 7
and 8 have essentially identical volatility characteristics and are almost indistinguishable from each other in Figure 13-13.) Initially, the choice of spreads will
depend on the risk of movement in the underlying contract as well as the risk
of changes in implied volatility.
Because we are dealing with stock options, there are two additional risks—
the risk of changing interest rates and the risk of changing dividends, assuming that at least one dividend payment falls between expirations. We know
from Chapter 7 that stock option calls and puts react in just the opposite
way to changes in interest rates and dividends. Rising interest rates or falling dividends cause calls to rise in value and puts to fall; falling interest rates
and rising dividends cause calls to fall in value and puts to rise. Moreover, the
impact of a change in either of these inputs will be greater for long-term
options than for short-term options. We can measure the risk of changing interest rates by determining the total rho value for each spread. Even though
there is no Greek for the dividend sensitivity, we can still use a computer to determine the dividend risk associated with each spread. The sensitivities for the
individual options, as well as the total spread sensitivities, to changing interest
rates and dividends are shown in Figure 13-14.
The call spreads (Spreads 7 and 9) have a positive rho and negative dividend sensitivity. The put spreads (Spreads 8 and 10) have a negative rho and
positive dividend sensitivity. The value of each spread with respect to changes
in these inputs is shown in Figures 13-15 and 13-16.
The interest-rate and dividend risk associated with volatility spreads is usually small compared with the volatility (gamma and vega) risk. Nonetheless, a
trader ought to be aware of these risks, especially when a position is large and
there is significant risk of a change in either interest rates or dividends.
What Is a Good Spread?
Option traders, being human, would rather talk about their successes than
their disasters. If one were to eavesdrop on conversations among traders, it
would probably seem that no one ever made a losing trade. Disasters, when
they do occur, only happen to other traders. The fact is that every successful
option trader has had his share of disasters. What separates successful traders
from the unsuccessful ones is the ability to survive such occurrences.
Consider the trader who initiates a spread with a good theoretical edge
and a large margin for error in almost every risk category. If the trader still
--- page 259 ---

242
O P T I O N V O L AT I L I T Y A N D P R I C I N G
Stock price = 99.25
Expected dividend = 0.50 in 4 weeks and every 13 weeks thereafter
Time to March expiration = 8 weeks
Volatility = 29%
Interest rate = 6%
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
85
14.90
10.91
93
1.2
−0.0264
0.053
28.82%
0.37
0.38
−7
1.2
−0.0125
0.053
28.84%
90
10.51
10.65
83
2.3
−0.0371
0.098
27.53%
0.94
1.07
−17
2.3
−0.0224
0.098
27.61%
95
6.74
7.06
68
3.2
−0.0457
0.138
26.64%
2.11
2.44
−32
3.2
−0.0316
0.138
26.59%
100
3.85
4.32
51
3.6
−0.0477
0.154
25.98%
4.18
4.65
−49
3.6
−0.0314
0.154
25.97%
105
1.95
2.42
34
3.3
−0.0421
0.142
25.62%
7.23
7.71
−66
3.3
−0.0250
0.142
25.58%
110
0.88
1.25
21
2.6
−0.0319
0.111
25.47%
11.12
11.49
−79
2.6
−0.0140
0.111
25.47%
Time to June expiration = 21 weeks
Volatility = 29%
Interest rate = 6%
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
85
16.70
16.90
84
1.3
−0.0256
0.149
27.64%
1.40
1.61
−16
1.3
−0.0120
0.149
27.58%
90
12.85
13.25
76
1.7
−0.0293
0.195
26.92%
2.44
2.84
−24
1.7
−0.0149
0.195
26.93%
95
9.52
10.11
66
2.0
−0.0316
0.229
26.41%
3.99
4.58
−34
2.0
−0.0164
0.229
26.41%
100
6.78
7.51
55
2.2
−0.0320
0.247
26.04%
6.13
6.86
−45
2.2
−0.0085
0.247
26.04%
105
4.64
5.44
45
2.2
−0.0306
0.246
25.76%
8.87
9.67
−55
2.2
−0.0138
0.246
25.76%
110
3.06
3.84
35
2.0
−0.0278
0.231
25.58%
12.18
12.95
−65
2.0
−0.0101
0.231
25.61%
Figure 13-10
e Polytechnic Library 192.99.6.125] at [07/06/16]. Copyright © McGraw-Hill Global Education Holdings, LLC. Not to be redistributed or modified in a
--- page 260 ---

R i s k C o n s i d e r at i o n s 	 243
ends up losing money on the spread, does this mean that the trader has made
a poor choice of spreads? Maybe a similar spread, but one with less margin for
error, would have resulted in an even greater loss, perhaps a loss from which the
trader could not recover.
It is impossible to take into consideration every possible risk. A spread that
passed every risk test would probably have so little theoretical edge that it would
not be worth doing. But the trader who allows himself a reasonable margin for
error will find that even his losses will not lead to financial ruin. A good spread
is not necessarily the one that shows the greatest profit when things go well; it
Theoretical
Edge
Delta
Gamma
Theta
Vega
Spread 7:
+20 June 100 calls
−20 March 100 calls
20 x +0.73
20 x −0.47
+5.40
+20 x +55
−20 x +51
+80
+20 x 2.2
−20 x 3.6
−28.0
+20 x −0.0320
−20 x −0.0477
+0.3140
+20 x 0.247
−20 x 0.154
+1.860
Spread 8:
+20 June 95 puts
−20 March 95 puts
20 x +0.59
20 x −0.33
+5.20
+20 x −34
−20 x −32
−40
+20 x 2.0
−20 x 3.2
−20.0
+20 x −0.0164
−20 x −0.0316
+0.3030
+20 x 0.229
−20 x 0.138
+1.820
Spread 9:
+17 June 110 calls
−17 March 105 calls
17 x +0.78
17 x −0.47
+5.27
+17 x +35
−17 x +34
+17
+17 x 2.0
−17 x 3.3
−22.1
+17 x −0.0278
−17 x −0.0421
+0.2431
+17 x 0.231
−17 x 0.142
+1.513
Spread 10:
+65 June 85 puts
−65 March 90 puts
65 x +0.21
65 x −0.13
+5.20
+65 x −16
−65 x −17
+65
+65 x 1.3
−65 x 2.3
−65.0
+65 x −0.0120
−65 x −0.0224
+0.6760
+65 x 0.149
−65 x 0.098
+3.315
Figure 13-11
Figure 13-12
Theoretical profit or loss
Underlying price
85
90
95
115
105
100
110
–10
0
+5
+10
–5
–25
–20
–15
–30
Spread 7 (call calendar spread)
Spread 8 (put calendar spread)
Spread 9 (call diagonal spread)
Spread 10 (put diagonal spread)
--- page 261 ---

244
O P T I O N V O L AT I L I T Y A N D P R I C I N G
Figure 13-13
Spread 7 (call calendar spread)
Spread 8 (put calendar spread)
Spread 9 (call diagonal spread)
Spread 10 (put diagonal spread)
Theoretical profit or loss
Volatility
20%
22%
38%
32%
24%
34%
0
+10
+15
+20
+5
–15
–10
–5
–20
26%
28%
30%
36%
March Options
Exercise
Price
Call
Rho*
Put
Rho*
Call Dividend
Sensitivity†
Put Dividend
Sensitivity†
85
0.118
−0.012
−0.924
0.072
90
0.109
−0.027
−0.826
0.169
95
0.093
−0.052
−0.681
0.315
100
0.071
−0.081
−0.509
0.487
105
0.048
−0.111
−0.342
0.653
110
0.030
−0.138
−0.208
0.788
June Options
Exercise
Price
Call
Rho*
Put
Rho*
Call Dividend
Sensitivity†
Put Dividend
Sensitivity†
85
0.266
−0.068
−1.668
0.308
90
0.247
−0.107
−1.498
0.478
95
0.220
−0.154
−1.300
0.676
100
0.188
−0.205
−1.089
0.887
105
0.154
−0.258
−0.880
1.096
110
0.122
−0.310
−0.688
1.288
*The interest-rate sensitivity is given as the point change in option value for each one-percentage-point (1.00%)
change in interest rates.
†The dividend sensitivity is given as the point change in option value for each point change in the dividend.
Figure 13-14  Interest-rate and dividend sensitivity.
(continued)
--- page 262 ---

R i s k C o n s i d e r at i o n s 	 245
Figure 13-15  Interest-rate sensitivity.
Spread 7 (call calendar spread)
Spread 8 (put calendar spread)
Spread 9 (call diagonal spread)
Spread 10 (put diagonal spread)
Theoretical profit or loss
Interest rate
0%
1%
12%
8%
2%
9%
0
+10
+15
+20
+5
–10
–5
4%
6%
7%
11%
3%
5%
10%
may be the one that shows the least loss when things go badly. Winning trades
always take care of themselves. Losing trades that do not give back all the profits from the winning ones are just as important.
Efficiency
One method that traders sometimes use to compare the relative riskiness of
potential strategies focuses on the risk-reward ratio, or efficiency, of the strategies. Suppose that a trader is considering two possible spreads, both with
a positive gamma and a negative theta. The reward is represented by the
Total
Rho
Total Dividend
Sensitivity
Spread 7:
+20 June 100 calls
−20 March 100 calls
+20 x +0.188
−20 x +0.071
+2.340
+20 x −1.089
−20 x −0.509
−11.600
Spread 8:
+20 June 95 puts
−20 March 95 puts
+20 x −0.154
−20 x −0.052
−2.040
+20 x +0.676
−20 x +0.315
+7.220
Spread 9:
+17 June 110 calls
−17 March 105 calls
+17 x +0.122
−17 x +0.048
+1.258
+17 x −0.688
−17 x −0.342
−5.882
Spread 10:
+65 June 85 puts
−65 March 90 puts
+65 x −0.068
−65 x −0.027
−2.665
+65 x +0.308
−65 x +0.169
+9.035
Figure 13-14  (continued)
--- page 263 ---

246
O P T I O N V O L AT I L I T Y A N D P R I C I N G
gamma, the potential profit when the underlying market moves. The risk is
the theta, the money that will be lost through the passage of time if the underlying market fails to make sufficiently large moves. The trader would like
the reward (the gamma) to be as large as possible compared with the risk (the
theta). We might express this relationship as a ratio
gamma/theta
The larger the absolute value of this ratio, the more efficient the position.
In the same way, a trader who has a negative gamma and a positive theta
wants the risk (the gamma) to be as small as possible compared with the reward
(the theta). He therefore wants the absolute value of the gamma/theta ratio to
be as large as possible.
For example, we might go back and calculate the efficiency of Spreads 1
through 3 in Figure 13-3. The efficiencies are
Gamma/Theta
Efficiency
Spread 1
−406.0/0.4235
959
Spread 2
−165.5/0.1365
1,212
Spread 3
−370.0/0.4000
925
Because each spread has a negative gamma and positive theta, we want the efficiency to be as small as possible. We can see that Spread 3 is best, which is consistent with our previous analysis of each spread.
Assuming that all strategies have approximately the same theoretical edge,
the efficiency can be a reasonable method of quickly comparing strategies
where all options expire at the same time. In such cases, the gamma and theta
Figure 13-16  Dividend sensitivity.
Theoretical profit or loss
Expected quarterly dividend
0
1.00
.60
.70
+4
+8
+10
+12
+6
0
+2
.20
.40
.50
.90
.10
.30
.80
Spread 7 (call calendar spread)
Spread 8 (put calendar spread)
Spread 9 (call diagonal spread)
Spread 10 (put diagonal spread)
--- page 264 ---

R i s k C o n s i d e r at i o n s 	 247
are the primary risks to the position. If a strategy consists of options that expire
at different times, the efficiency is only one consideration, and the sensitivity of
the positions to changes in implied volatility (the vega) may also become important, as they were in our other spread examples. In such cases, a more detailed
risk analysis will be necessary.
Adjustments
In Chapter 11, we considered the question of when a trader should adjust a position to remain delta neutral. In addition to deciding when to adjust, the trader
also must consider how best to adjust because there are many different ways to
adjust the total delta position. An adjustment to a trader’s delta position may
reduce his directional risk, but if he simultaneously increases his gamma, theta,
or vega risk, he may inadvertently be exchanging one type of risk for another.
A delta adjustment made with the underlying contract is essentially a riskneutral adjustment. The gamma, theta, and vega of an underlying contract are
0, so an adjustment made with the underlying contract will not change any of
these risks. If a trader wants to adjust his delta position but wants to leave the
other characteristics of the position unaffected, he can do so by purchasing or
selling an appropriate number of underlying contracts.
An adjustment made with options will also reduce the delta risk, but at
the same time, it will change the other risk characteristics. Because every
option has not only a delta but also a gamma, theta, and vega, when an option
is added to or subtracted from a position, it necessarily changes the total delta,
gamma, theta, and vega of the position. This is something that new traders
sometimes forget.
Consider a stock option market where the underlying contract is trading
at 99.25 and all options appear to be overpriced. Suppose that a trader decides
to sell the 95/105 strangle (sell the 95 put, sell the 105 call), with put and call
deltas of –32 and 34, respectively. If the trader sells 20 strangles, the position is
initially slightly delta negative because
(–20 × +34) + (–20 × –32) = –40
Suppose that a week passes and the underlying market has fallen to 97.00,
with new delta values for the 95 put and 105 call of –39 and +25. Assuming
that no adjustments have been made, the trader’s delta position is now
(–20 × –39) + (–20 × +25) = +280
If the trader wants to hold the position but also wants to remain approximately delta neutral, he has three basic choices:
1.	 Sell underlying contracts.
2.	 Sell calls.
3.	 Buy puts.
Which method is best?
--- page 265 ---

248
O P T I O N V O L AT I L I T Y A N D P R I C I N G
All other considerations being equal, whenever a trader makes an adjustment, she should do so with the intention of improving the risk-reward characteristics of the position. If the trader decides to adjust his delta position by
purchasing puts, he also reduces his other risks because the gamma, theta, and
vega associated with the put purchase are opposite in sign to the gamma, theta,
and vega associated with the existing short strangle position.
Unfortunately, all other considerations may not be equal. Because implied
volatility can remain high or low for long periods of time, it is quite likely that if
all options were overpriced when the trader initiated his position, they will still
be overpriced when he goes back into the market to make his adjustment. Even
though the purchase of puts to become delta neutral will also reduce his other
risks, such an adjustment will have the effect of reducing the theoretical edge.
On the other hand, if all options are overpriced and the trader decides to sell
additional calls to reduce the delta, the sale of the overpriced calls will have the
effect of increasing the theoretical edge. If the trader decides that adding to his
theoretical edge is of primary importance, he may decide to sell 11 additional
105 calls, leaving him approximately delta neutral because
(–20 × –39) + (–31 × +25) = –5
Now suppose that another week passes and the market has rebounded to
101.00, with new delta values for the 95 put and 105 call of –24 and +37. The
position delta is now
(–20 × –24) + (–31 × +37) = –667
Again, if the trader wants to adjust, he has three basic choices—buy
underlying contracts, buy calls, or sell puts. Assuming that all options are still
overpriced and that the trader wants to continue to increase his theoretical
edge, he may decide to sell an additional 28 of the 95 puts. The new total delta
position is
(–48 × –24) + (–31 × +37) = +5
It should be clear what will result from these adjustments. If all options
remain overpriced and the trader focuses solely on increasing his theoretical
edge, he will continue to make whatever adjustments are necessary by selling
overpriced options. This method of adjusting may indeed result in the greatest profit to the trader, but the strangle, which the trader was initially prepared to sell 20 times, now has increased in size to 48 × 31. If the market now
makes a violent move in either direction, the adverse consequences will be
greatly magnified. The new trader, overly concerned with always increasing
his theoretical edge, often finds himself in just such a position. If the market
makes a very swift move, the trader may not survive. For this reason, a new
trader is usually well advised to avoid making adjustments that increase the
size of a position.
No trader can afford to ignore the effect that adjustments will have on
the total risk to a position. If he has a positive gamma or vega position, buying any additional options will increase his gamma or vega risk; if he has a
--- page 266 ---

R i s k C o n s i d e r at i o n s 	 249
negative gamma or vega position, selling any additional options will likewise
increase his gamma or vega risk. A trader cannot afford to sell overpriced options or buy underpriced options ad infinitum. At some point, the size of the
spread will simply become too large, and any additional theoretical edge will
have to take a back seat to risk considerations. When this happens, there are
only two choices:
1.	 Decrease the size of the spread.
2.	 Adjust in the underlying market.
A disciplined trader knows that sometimes, because of risk considerations,
the best course is to reduce the size of the spread, even if it means giving up
some theoretical edge. When open-outcry markets were flourishing, this could
be particularly hard on a trader’s ego if the trader had to personally go back
into the market and either buy back options, that he originally sold, at a lower
price or sell out options, that he originally purchased, at a higher price. However, if a trader is unwilling to swallow his pride from time to time, his trading
career is likely to be a short one.
If a trader finds that any delta adjustment in the option market that
reduces his risk will also reduce his theoretical edge and he is unwilling to give
up any theoretical edge, his only recourse is to make adjustments in the underlying market. An underlying contract has no gamma, theta, or vega, so the risks
of the position will remain essentially the same.
A Question of Style
Because most option pricing models assume that movement in the underlying
contract is random, an option trader who trades purely from the theoretical
values generated by a model should not have any prior opinion about market direction. In practice, however, many option traders begin their trading
careers by taking positions in the underlying market, where direction is the primary consideration. Many traders therefore develop a style of trading based
on presumed directional moves in the underlying market. A trader might, for
example, be a trend follower, adhering to the philosophy that “the trend is
your friend.” Or he might be a contrarian, preferring to “buy weakness, sell
strength.”
Traders often try to incorporate their personal trading styles into their
option strategies. One way to do this is to consider beforehand the adjustments
that will be required for a certain strategy if the underlying market begins
to move. A trader who sells straddles knows that such spreads have negative
gamma. As the market moves higher, his delta position is becoming negative,
and as the market moves lower, his delta position is becoming positive. If this
trader likes to trade against the trend, he will avoid adjustments as much as possible because his position is automatically trading against the trend. Whichever
way the market moves, the position always wants a retracement of this movement. On the other hand, a trader who sells the same straddles but prefers to
--- page 267 ---

250
O P T I O N V O L AT I L I T Y A N D P R I C I N G
trade with the trend will adjust at every opportunity. In order to remain delta
neutral, he will be forced to buy underlying contracts as the market rises and
sell underlying contracts as the market falls.
The opposite is true for a trader who buys straddles. He has a positivegamma position. As the market rises, his delta position is becoming positive,
and as the market falls, his delta position is becoming negative. If this trader
likes to trade with the trend, he will adjust as little as possible in the belief that
the market is likely to continue in the same direction. If, however, he prefers
to trade against the trend, he will adjust as often as possible. Every adjustment will represent a profit opportunity if the market does in fact reverse its
direction.
A trader with a negative gamma is always adjusting with the trend of the
underlying market. A trader with a positive gamma is always adjusting against
the trend of the underlying market. If a trader prefers to trade with the trend
or against the trend, he should choose a strategy and an adjustment process
that are appropriate to his preference. A trader who prefers to trade with the
trend can choose a strategy with a positive gamma together with less frequent
adjustments or a strategy with a negative gamma with more frequent adjustments. A trader who prefers to trade against the trend can choose a strategy
with a negative gamma together with less frequent adjustments or a strategy
with a positive gamma with more frequent adjustments. The purely theoretical trader will not have to worry about this because for him there is no such
thing as a trend. However, for many traders, old habits, such as trading with or
against the trend, are hard to break.
Liquidity
Every open option position entails risk. Even if the risk is limited to the current
value of the options, by leaving the position open, the trader is risking the loss
of that value. If the trader wants to eliminate the risk, he will have to take some
action that will, in effect, close out the position. Sometimes this can be done
through early exercise or by taking advantage of an opposing position to create an arbitrage. More often, however, in order to close out an open position, a
trader must go into the marketplace and buy in any short options and sell out
any long options.
An important consideration in deciding whether to enter into a trade is
often the ease with which the trader can reverse the trade. Liquid option markets, where there are many buyers and sellers, are much less risky than illiquid
markets, where there are few buyers and sellers. In the same way, a spread that
consists of very liquid options is much less risky than a spread that consists of
one or more illiquid options. If a trader is considering entering into a spread
where the options are illiquid, he ought to ask himself whether he is willing to
live with that position until expiration. If the market is very illiquid, this may
be the only time that he will be able to get out of the position at anything resembling a fair price. If the spread consists of long-term options, the trader
may find himself married to the position for better or worse, in sickness and
in health, for what may seem like an eternity. If he is unwilling to commit his
