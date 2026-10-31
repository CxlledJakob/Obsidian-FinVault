# Option Volatility and Pricing_ Advanced Trading Strategies -- Sheldon Natenberg -- 2nd ed, 2014 -- McGraw Hill Professional -- isbn13 9780071818773 -- 6a48d008bd9beef283debf7bad0b2e4a -- Anna’s Archive.pdf — pages 419–438

--- page 419 ---

402
O P T I O N V O L AT I L I T Y A N D P R I C I N G
In order to accurately assess implied-volatility risk, a trader will need some
method of determining how implied volatilities are likely to change across multiple expirations. This usually takes the form of an implied-volatility termstructure model. There is no single model that all traders use. Models are often
“home grown,” with a trader trying to develop a model that is consistent with his
mathematical sophistication, as well as his experience in the marketplace. Whatever the model, it will usually require at least three inputs: a primary month against
which all other months will be compared, a mean volatility to which implied
volatility tends to revert, and a “whippiness” factor that specifies how implied
volatility changes across other expirations with respect to changes in the primary
month. The primary month will often be the front month, where trading activity tends to be concentrated. But this is not always the case. In agricultural markets, trading activity is often concentrated in expiration months that fall close to
either the planting or harvesting calendar. If this is the case, one of these months
may be a better choice as the primary month. Additionally, implied volatility in
the front month can be unstable, especially as expiration approaches. It often
changes in ways that are inconsistent with the term structure of other expiration
months. As a result, many traders evaluate their position in front-month contracts separately from their positions in other months, with the volatility termstructure model applying to all months except the front month. The primary
month chosen in this approach will be something other than the front month.
Figure 20-14 shows how the term structure of implied volatility can evolve
over time. The values represent the implied volatilities during 2010 of atthe-money options on the EuroStoxx 50 Index for expirations extending out
24 months. Values were calculated at two-month intervals, on the first Friday
of February, April, June, August, October, and December. The reader may
find it useful to compare the changes in the term-structure graphs with the
30-day historical volatility of the EuroStoxx 50 Index during this period,
shown in Figure 20-15. In early February, the term-structure graph was downward sloping: long-term options were trading at lower implied volatilities than
short-term options. By April, as a result of declining index volatility, not only
had implied volatility declined, but the term-structure graph had inverted and
was upward sloping: long-term options were trading at higher implied volatilities than short-term options. After a dramatic increase in index volatility, the
June term-structure graph again became downward sloping. Finally, after declining index volatility in the last half of 2010, implied volatilities seemed to
settle into a middle area, with a relatively flat term structure.
Note one other important point: the disconnect between the front-month
implied volatility and the remainder of the term-structure graph in December.
The graph is generally upward sloping, but the front-month implied volatility
is still much higher than all other months. This is a common characteristic in
many option markets. The front-month implied volatility can often trade in a
way that is inconsistent with the term structure of other months.
The term structure in Figure 20-12 is typical of markets where the only
factors that tend to affect implied volatility are the recent volatility of the underlying contract and the mean volatility. However, in some markets, there may
also be a seasonal volatility factor.
--- page 420 ---

V o l at i l i t y R e v i s i t e d 	 403
Figure 20-14  Implied-volatility term structure for EuroStoxx 50 Index options during 2010.
Implied volatility
34%
0
3
9
6
15
18
12
Months to expiration
21
24
32%
30%
28%
26%
24%
22%
20%
18%
16%
14%
February 5, 2010
April 1, 2010
June 4, 2010
August 6, 2010
October 1, 2010
December 3, 2010
Figure 20-15  EuroStoxx 50 Index 30-day historical volatility during 2010.
Volatility
60%
Jan
Feb
Mar
Apr
May
Jun
Aug
Jul
Sep
Oct
Nov
Dec
50%
40%
30%
20%
10%
--- page 421 ---

404
O P T I O N V O L AT I L I T Y A N D P R I C I N G
Given the possibility of extremely hot temperatures, as well as droughts,
summer expiration months in agricultural markets typically trade at higher
implied volatilities than other months, regardless of the time of year. In
energy markets where fuel is needed for heating in the winter and cooling in
the summer, the possibility of very cold winters and very hot summers may
result in some months trading at persistently higher implied volatilities than
other months. In such markets, it can be difficult to create a reliable termstructure model.
Figure 20-16 shows the changing term structure of implied volatility for
options on natural gas futures during 2009. Although not as obvious as the Eurostox 50 Index in Figure 20-14, we can still detect the tendency of long-term
implied volatility to revert to a mean, perhaps around 40 percent. But in addition, there is also a seasonal volatility factor. Note the implied volatility of the
October option contract, which has been highlighted with a circle. Regardless of the term structure, October options always seem to trade at an inflated
implied volatility. This is perhaps easier to see in Figure 20-17, which shows
the average implied volatility of each expiration month during 2009. October
clearly carries a higher implied volatility than any other month. The reason
for this has to do primarily with the Atlantic hurricane season, which extends
from approximately early June to late November, with the height of the season
falling in August and September. During this period, any major hurricane can
Figure 20-16  Implied-volatility term structure for options on natural gas futures during 2009.
Implied volatility
85%
1
3
2
5
6
4
Months to expiration
7
8
9
10
11
12
80%
75%
70%
65%
60%
55%
50%
45%
40%
35%
February 6, 2009
April 3, 2009
June 5, 2009
August 7, 2009
October 2, 2009
December 4, 2009
=  October implied volatility
--- page 422 ---

V o l at i l i t y R e v i s i t e d 	 405
disrupt natural gas operations, which in the United States are concentrated
along the northern coast of the Gulf of Mexico. October options, which expire
toward the end of September, will capture any volatility occurring during the
height of the hurricane season. Consequently, October options tend to trade at
consistently higher implied volatilities than other months.
Forward Volatility
Let’s return to the term-structure graphs of implied volatilities across expiration months shown in Figure 20-14. Can we identify any trading opportunities
from these graphs? We might simply decide that implied volatility is either too
high, in which case we will prefer to sell options, or too low, in which case we
will prefer to buy options. In either case, we can, in theory, capture a perceived
mispricing by dynamically hedging the position with the underlying contract.
But we might also ask a different question: are any expiration months mispriced
with respect to other expiration months? Should we consider some type of calendar spread, selling options in one month and buying options in a different
month?
Figure 20-17  Average implied volatility by expiration month of options on natural gas
futures during 2009.
Average implied volatility
62%
Jan
Feb
Mar
Apr
May
Jun
Aug
Jul
Sep
Oct
Nov
Expiration month
Dec
60%
58%
56%
50%
52%
54%
44%
46%
48%
--- page 423 ---

406
O P T I O N V O L AT I L I T Y A N D P R I C I N G
Let’s focus on one graph from Figure 20-14, the term structure of Eurostoxx
50 Index options on February 5, 2010. This is shown in Figure 20-18. The large
dots represent the at-the-money implied volatilities, with the solid black line representing the best fit generated by a term-structure model. We can see that some
contract months seem to deviate from the best-fit line. June 2010 implied volatility falls below the line, whiles September and December 2010 fall above the line.
Assuming that each month is in fact trading at the indicated implied volatility,9
do these deviations represent a trading opportunity? Should we be buying   June
options and selling September or December options?
One method that traders use to determine the mispricing of a calendar
spread is to consider the spread’s implied volatility. That is, what single volatility
applied to both expiration months will cause the value of the spread to be equal
to its price in the marketplace? To better understand this, let’s use the volatilities
in Figure 20-18 to calculate the prices of several calendar spreads. For simplicity, we will assume that the underlying contract is trading at 100 and that there
are no interest-rate considerations. The relevant data is shown in Figure 20-19.
Looking at the February/March calendar spread, the implied volatilities for
the two months are 29.61 percent for February and 28.06 percent for March.
9 We make this proviso because option settlement prices do not necessarily reflect actual trading activity. When
this happens, anyone using settlement prices as a guide to potential trading strategies may be disappointed to
find that the settlement price is not an accurate reflection of where an option can actually be traded.
Figure 20-18  Implied volatility for at-the-money EuroStoxx 50 Index options on February
5, 2010.
Implied volatility
30%
0
3
9
6
12
15
18
Months to expiration
21
24
29%
28%
27%
24%
25%
26%
20%
21%
22%
23%
February 2010 – 29.61%
March 2010 – 28.01%
April 2010 – 27.15%
June 2010 – 25.61%
September 2010 – 25.08%
December 2010 – 24.71%
June 2011 – 23.99%
December 2011 – 23.80%
--- page 424 ---

V o l at i l i t y R e v i s i t e d 	 407
The values of the at-the-money calls are 2.31 and 3.80, with a spread value of
1.49. If we evaluate these options using the same volatility, what single volatility
will yield a value equal to the price of 1.49? Logically, this volatility has to be less
than 28.06 percent because at this volatility the March option is fairly priced, but
the February option is too expensive. The entire spread will be worth more than
1.49. We need to reduce the volatility until we find the single volatility that will
cause the spread to be worth 1.49. Using a computer, we find that the February/
March calendar spread has an implied volatility of 25.94 percent.
We can go through this process for each successive calendar spread, calculating the implied volatility of each spread. These volatilities are shown at the
bottom of Figure 20-19. How will these calendar spread implied volatilities
look if we overlay them on Figure 20-18? This is shown in Figure 20-20. We
can see clearly that the June 2010 options are significantly underpriced in the
marketplace compared with nearby expirations, while the September 2010 options are significantly overpriced. If given a choice of strategies, it might make
sense to buy the April/June 2010 calendar spread and sell the June/September
2010 calendar spread. Together these spreads make up a time butterfly.
We use these implied volatilities not to determine whether implied volatility in the entire option complex is either too high or too low but rather to determine whether particular months are mispriced with respect to other months.
Figure 20-19  Calendar spread values using implied volatilities on February 5, 2010.
Expiration
Month
Time to
Expiration (days)
Implied
Volatility
Price of
the 100 Call
Vega of
the 100 Call
February 2010
14
29.61%
2.31
0.078
March 2010
42
28.06%
3.80
0.135
April 2010
70
27.15%
4.74
0.174
June 2010
133
25.61%
6.15
0.240
September 2010
224
25.08%
7.82
0.311
December 2010
315
24.71%
9.14
0.368
June 2011
497
23.99%
11.13
0.461
December 2011
679
23.80%
12.89
0.537
Calendar Spread
Spread Price
Spread Implied
Volatility
Spread Vega
February 2010 / March 2010
1.49
25.94%
0.057
March 2010 / April 2010
0.94
24.02%
0.039
April 2010 / June 2010
1.41
21.50%
0.066
June 2010 / September 2010
1.67
23.28%
0.071
September 2010 / December 2010
1.32
22.70%
0.071
December 2010 / June 2011
1.99
21.13%
0.093
June 2011 / December 2011
1.76
22.67%
0.076
--- page 425 ---

408
O P T I O N V O L AT I L I T Y A N D P R I C I N G
The implied-volatility graph acts as a magnifying glass, enabling us to more
easily determine which months are overpriced and which are underpriced.
When the term-structure graph is downward sloping, as it is in Figure
20-20, all calendar spread implied volatilities will fall below the term-structure
graph. Alternatively, if the term-structure graph is upward sloping, all calendar
spread implied volatilities will fall above the graph. If all implied volatilities fall
exactly along the best-fit graph, regardless of whether the graph is upward or
downward sloping, the implied-volatility curve will be smooth, suggesting that
there are no obviously mispriced calendar spreads.
Determining the exact implied volatility of a calendar spread usually requires a computer programmed with a pricing model. However, it is often possible to estimate the implied volatility of an at-the-money calendar spread if we
recall that the vega of an at-the-money option is relatively constant with respect
to changes in volatility. Suppose that we know both the prices O1 and O2 and the
vega values V1 and V2 of the two options that make up the calendar spread. The
price of the spread is O2 – O1, and the vega of the spread is V2 – V1. The implied
volatility of the spread, given as a whole number, is approximately equal to the
price of the spread divided by its vega
O
O
V
V
Spread implied volicity
2
1
2
1
=
−
−
Figure 20-20  EuroStoxx 50 Index calendar spread implied volatilities on February 5, 2010.
0
3
9
6
12
15
18
Months to expiration
21
24
February 2010
March 2010
April 2010
June 2010
September 2010
December 2010
June 2011
December 2011
Feb–Mar
Mar–Apr
Apr–Jun
Jun–Sep
Sep–Dec
Dec–Jun
Jun–Dec
Implied volatility
30%
29%
28%
27%
24%
25%
26%
20%
21%
22%
23%
--- page 426 ---

V o l at i l i t y R e v i s i t e d 	 409
This method is not exact because there is likely to be rounding error, and the
vega does change slightly as we change volatility. However, this approach may
be useful if a trader needs to make a quick estimate of whether a calendar
spread is overpriced or underpriced.
The vega values for the individual options, as well as for the various calendar spreads, are given in Figure 20-20. The reader may find it worthwhile to
estimate the implied volatility of each spread using this method and then compare the result with the true implied volatility of the spread.
Instead of analyzing the volatility term structure by looking at the implied
volatility of successive calendar spreads, we might take a slightly more theoretical approach. Suppose that we have two option expirations, a short-term
option expiring at t1 and a long-term option expiring at t2. If the implied volatility of the short-term expiration is σ1 and the implied volatility of the long-term
expiration is σ2, we might ask this question: what forward volatility σf is the marketplace implying between expiration of the short-term option and expiration
of the long-term option?

t1
t2
This is analogous to a forward rate in an interest-rate market. Given a short-term
interest rate and a long-term interest rate, what rate must apply between the
two maturities such that no arbitrage opportunity exists? Unlike interest rates,
which are directly proportional to time, volatility is proportional to the square
root of time. Using this, we can calculate the forward volatility10
t
t
t
t
(
)
(
)
f
2
2
2
1
2
1
2
1
σ
=
σ ×
−σ ×
−
We can expand this relationship to any number of volatilities over any
number of consecutive time periods. Given forward volatilities σi covering the
time from ti–1 to ti, the volatility over the entire time period from t0 to tn must be
t
t
t
t
(
)
t
t
t
t
i
i
n
i
n
(
1)
2
1
0
1
n
i
i
0
∑
σ
=
σ
×
−
−
−
−
−
−
=
10 Some readers may recognize that the forward volatility calculation results from the fact that the square of
volatility or variance σ2 is directly proportional to time
σf
2 × (t2 – t1) = (σ2
2 × t2) – (σ1
2 × t1)
--- page 427 ---

410
O P T I O N V O L AT I L I T Y A N D P R I C I N G
Suppose that we calculate the forward volatilities for the volatility term
structure in Figure 20-20. How would this compare with the implied volatilities of the calendar spreads? This is shown in Figure 20-21. The forward volatility graph has the same general structure as the calendar spread graph. Both
graphs serve the same purpose—to highlight any mispricing of a particular
expiration month.
Every experienced option trader knows that dealing with volatility can be
a difficult task. To facilitate the decision-making process, we have attempted to
make some generalizations about volatility characteristics. Even then, it may
not be clear what the right strategy is. Moreover, looking at a limited number of
examples makes the generalizations even less reliable. Every market has its own
characteristics, and understanding the volatility characteristics of a particular
market, whether interest rates, foreign currencies, stocks, or commodities, is at
least as important as knowing the technical characteristics of volatility. And this
knowledge can only come from careful study of a market combined with actual
trading experience.
Figure 20-21
0
3
9
6
12
15
18
Months to expiration
21
24
February 2010
March 2010
April 2010
June 2010
September 2010
December 2010
June 2011
December 2011
Implied volatility
30%
29%
28%
27%
24%
25%
26%
20%
21%
22%
23%
Expiration month implied volatilities
Calendar spread implied volatilities
Forward volatilities
--- page 428 ---

411
Position Analysis
Investors or speculators in option markets often have a particular view of market conditions in terms of either direction or volatility. They attempt to profit
from this view through the selection of spreading strategies such as those discussed in Chapters 11 and 12. In Chapter 13, we looked at the risk characteristics of some of these strategies under changing market conditions. Because
each spread consisted of a limited number of contracts, it was a relatively simple matter to determine the risks that each spread entailed.
An active option trader, such as a market maker, may build up much more
complex positions consisting of many different options across a wide range of
exercise prices and expiration months. Unlike simple strategies, where the risks
are relatively easy to identify, analysis of a complex position can be particularly
difficult because of the many ways in which risks can change as market conditions change. If a trader cannot determine the risks of a position, he will be
unprepared to take the necessary action to protect himself when market conditions move against him or to take advantage of his good fortune when market
conditions move in his favor.
Before theoretical pricing models came into widespread use, analyzing a
complex position made up of many different options was often an impossible
task. Even if a trader had some idea of how each option changed as market
conditions changed, combining many different options often caused the entire
position to change in unexpected ways. Still, if he expected to survive, an intelligent trader needed to make some effort to analyze the position.
In the early days of option trading, one common approach to analyzing
risk was to use synthetic relationships to rewrite a position in a more easily recognizable form. If the rewritten position conformed to a strategy with which
the trader was familiar, the trader might then be able to determine the risks of
the position.
For example, consider this position:
+29 underlying contracts
–44 March 65 calls
+44 March 65 puts
21
--- page 429 ---

412
O P T I O N V O L AT I L I T Y A N D P R I C I N G
–7 March 70 calls
+49 March 70 puts
–33 March 75 calls
–51 March 75 puts
+30 March 80 calls
+12 March 80 puts
Suppose that the underlying contract is trading at a price of 71.50. What
is the delta of this position—positive, negative, or neutral? Without a theoretical pricing model, this may look like an impossible question to answer. And,
indeed, without a model, there is no way of knowing the exact delta of the
position. But even if we cannot determine the exact delta, perhaps we can
determine the direction in which we want the underlying contract to move.
Using synthetic relationships, positions that consist of both calls and puts
can be rewritten so that they consist of a single type of option, either all calls or
all puts. This can sometimes make a position easier to analyze. Let’s take our
position and rewrite it so that it consists only of calls, rewriting each put as its
synthetic equivalent:
+29 underlying contracts
–19 March 65 calls
+19 March 65 puts +19 March 65 calls/–19 underlying contracts
–7 March 70 calls
+49 March 70 puts +49 March 70 calls/–49 underlying contracts
–33 March 75 calls
–51 March 75 puts –51 March 75 calls/+51 underlying contracts
+30 March 80 calls
+12 March 80 puts +12 March 80 calls/–12 underlying contracts
If we total all the contracts, what are we left with?
Underlying
contracts
+29
–19
–49
+51
–12
=
0
March 65 calls
+19
+19
=
0
March 70 calls
–7
+49
=
+42
March 75 calls –33
–51
=
–84
March 80 calls +30
+12
=
+42
We really have this position.
+42 March 70 calls
–84 March 75 calls
+42 March 65 calls
As complex as the position first appeared, it was simply a long butterfly.
And a long butterfly always wants the underlying contract to move toward the
--- page 430 ---

P o s i t i o n A n a ly s i s 	 413
inside exercise price, in this case, 75. With the underlying contract currently
trading at 71.50, the position must be delta positive. If we had rewritten the
position so that it consisted only of puts, the result would have been the same
because a call and put butterfly have essentially the same characteristics.
The foregoing example was admittedly created so that when the position was
rewritten in terms of synthetic equivalents, its risk characteristics were relatively
easy to identify. In reality, the risk characteristics of a complex position rarely fall
neatly into place. Analysis of a complex position will almost always require a theoretical pricing model. Even then, the model may not tell the entire story.
Suppose that we have the following market conditions:
Underlying price = 99.60
Time to September expiration = 9 weeks
Volatility = 18 percent
Interest rate1 = 0
The September 95 put and September 105 call have these risk characteristics:
Delta
Gamma
Theta
Vega
September 95 put
25
4.3
–0.019
0.132
September 105 call
–25
4.3
–0.019
0.132
What are the risks if we have the following position2:
Long 10 September 95 puts
Short 10 September 105 calls
Long 5 underlying contracts
The total risk sensitivities for the position are
Delta:
(10 × –25) – (10 × 25) + (5 – 100) = 0
Gamma:	 (10 × 4.3) – (10 × 4.3) = 0
Theta:
(10 × –0.019) – (10 × –0.019) = 0
Vega:
(10 × 0.132) – (10 × –0.132) = 0
It appears that we have no directional risk (delta is 0), no realized volatility risk
(gamma is 0), no risk with respect to the passage of time (theta is 0), and no
implied volatility risk (vega is 0). If the position was initiated with some positive
theoretical edge and the risk sensitivities associated with the position are all 0,
then the position is certain to show a profit. So what’s the problem?
The problem is that the delta, gamma, theta, and vega are only measures
of the position’s risk under current market conditions. But today’s market conditions may not be—in fact, cannot be—tomorrow’s conditions. Even if the
1 In order to focus on the volatility characteristics of the positions, we assume an interest rate of 0 in this and
other examples.
2 Some readers may recognize this position as a risk reversal or split strike conversion. More on this in Chapter 24.
--- page 431 ---

414
O P T I O N V O L AT I L I T Y A N D P R I C I N G
underlying price and volatility remain unchanged, time will pass. And we know
that the passage of time can change a position’s characteristics. Looking at a
position’s characteristics under current market conditions is only the first step
in analyzing risk. We need to ask not only what the risks are right now but also
what the risks might be under different market conditions. What will happen
if the underlying contract moves up or down in price? What will happen if
implied volatility rises or falls? What will happen as time passes?
We can expand our analysis by using what we already know about how
risk sensitivities change as market conditions change. Suppose that the underlying price begins to fall. How might our risk change? We know that gamma
is greatest for at-the-money options. As the underlying price begins to fall, it is
moving toward the lower exercise price, 95, and away from the higher exercise price, 105. The gamma of the September 95 put must be increasing, while
the gamma of the September 105 call must be declining. Because we are long
the 95 put and short the 105 call, the total gamma position is becoming positive.
Moreover, if we have a positive gamma, as the market falls, our position, which
was initially delta neutral, will become delta negative.
What if the underlying price begins to rise? Now the market is moving
away from 95 and toward 105: the gamma of the September 95 put is declining, and the gamma of the September 105 call is increasing. The entire position is now becoming gamma negative. Consequently, as the market rises, our
position will become delta negative.
This seems odd. The position becomes delta negative if the underlying
price falls or rises. The explanation is the changing gamma: the position becomes
gamma positive on the way down but gamma negative on the way up.
Now let’s consider what will happen if volatility rises. As volatility
increases, the delta of calls moves toward 50, and the delta of puts moves
toward –50, while the delta of the underlying contract remains constant at 100.
Because we are long puts, now with a delta greater (in absolute value) than –25,
and short calls, now with a delta greater than 25, the position is becoming delta
negative. If the delta of the September 95 put goes to –30 and the delta of the
105 call goes to +30, the total delta position will be
(10 × –30) – (10 × 30) + (5 × 100) = –100
In the same way, reducing volatility causes delta values to move away
from 50. If the delta of the September 95 put goes to –20 and the delta of the
105 call goes to +20, the total delta position would be
(10 × –20) – (10 × 20) + (5 × 100) = +100
Summarizing, if volatility rises, we want the underlying market to fall. If volatility falls, we want the underlying market to rise.
What will happen to the position as time passes? Reducing time, like
reducing volatility, causes delta values to move away from 50. With no change
in the underlying price as time passes, the call and put will move further out of
the money. The five underlying contracts will tend to dominate the position,
resulting in a positive delta.
--- page 432 ---

P o s i t i o n A n a ly s i s 	 415
We have initially focused on the delta and gamma, but we can also infer
what will happen to the theta and vega because these values, like the gamma,
are greatest for at-the-money options. If the underlying contract begins
to fall, our theta position will become negative (the passage of time will begin to
hurt), and our vega position will become positive (we will want implied volatility to increase). If the underlying contract begins to rise, our theta position will
become positive (the passage of time will begin to help), and our vega position
will become negative (we will want implied volatility to decline). If the underlying price does not change, the gamma, theta, and vega of the position are
unlikely to be significantly affected by changes in either time or volatility. We
can summarize the effect of changing market conditions on the risk characteristics of the position as follows:
Change in Market
Conditions
Resulting
Delta Position
Resulting Gamma
Position
Resulting Theta
Position
Resulting
Vega Position
Rising underlying
price
Negative
Positive
Negative
Positive
Falling underlying
price
Negative
Positive
Negative
Positive
Time passes
Positive
0
0
0
Volatility rises
Negative
0
0
0
Volatility falls
Positive
0
0
0
If a position is not overly complex, a trader may be able to do this type of
analysis, first looking at the initial risk sensitivities and then considering how the
sensitivities might change as market conditions change. However, a trader can get
a more complete picture of a position’s risk by looking at a graph of the position’s
value over a broad range of conditions. Let’s do this for the current position:
Long 10 September 95 puts
Short 10 September 105 calls
Long 5 underlying contracts
Figure 21-1 shows the value of the position with respect to movement in
the underlying contract. The three graphs represent the value at the current
volatility of 18 percent, as well as at volatilities of 14 and 22 percent. From
Figure 21-1, we can see the graphic interpretation of delta and gamma. For
a negative delta position, the graph extends from the upper left to the lower
right—as the underlying price rises, the position loses value. For a positive
delta position, the graph extends from the lower left to the upper right—as the
underlying price rises, the position gains value. In our example, the position is
always delta negative at higher volatilities. Around the current underlying price
of 99.60, the position is delta neutral—the graph is exactly horizontal. At lower
volatilities, the delta will become positive around the current underlying price.
For a negative gamma position, the graph curves downward, taking on the
shape of a frown; price movement in either direction decreases the value of
--- page 433 ---

416
O P T I O N V O L AT I L I T Y A N D P R I C I N G
the position. For a positive gamma position, the graph curves upward, taking
on the shape of a smile; price movement in either direction increases the value
of the position. Our position has a positive gamma below the current price of
99.60 and a negative gamma above 99.60. At lower volatilities, the gamma is
magnified (there is greater curvature), while at higher volatilities, the gamma
is muted (there is less curvature). The current underlying price of 99.60 is an
inflection point—the gamma is changing from positive to negative. At this price,
the graph is essentially a straight line. The graphic interpretations of a positive
and negative delta and gamma are shown in Figure 21-2.
Because gamma and theta are of opposite signs, a positive gamma position
will lose value as time passes with no movement in the underlying contract. A
negative gamma will gain value. This is shown in Figures 21-3 and 21-4.
Although gamma and theta are always of opposite signs, gamma and
vega may be either the same or the opposite. Regardless of whether we have
a positive gamma (we want the underlying contract to move) or a negative
gamma (we want the underlying contract to sit still), we  can have either a
positive vega (we want implied volatility to rise) or a negative vega (we want
implied volatility to fall). The graphic representations of these positions are
shown in Figures 21-5 and 21-6.
It may also be useful to look at graphs of the risk sensitivities as market conditions change. In Figure 21-7, we can see the changing delta as the underlying price and volatility change. Close to the current underlying price of 99.60,
raising volatility causes the delta to become negative, while lowering volatility
causes the delta to become positive. As we have already seen, if the underlying
Figure 21-1  Position value as the underlying price and volatility change.
–20
–10
0
Theoretical P&L
–30
10
20
30
40
85
90
95
100
105
110
115
Underlying price
–40
Volatility = 22%
Volatility = 18%
Volatility = 14%
99.60
Long 10 September 95 puts
Short 10 September 105 calls
Long 5 underlying contracts
--- page 434 ---

P o s i t i o n A n a ly s i s 	 417
contract either rises or falls, the delta becomes negative. In Figure 21-8, we can
see the changing gamma as the underlying price and volatility change. Close to
the current underlying price of 99.60, the gamma is unaffected by changes in
volatility. The gamma becomes positive if the underlying price falls or negative
if the underlying contract rises.
Figure 21-3  Positive gamma, negative theta position as time passes.
Theoretical P&L
Underlying price
With no movement in the underlying price,
the position loses value as time passes.
The graph is shifted downward.
Figure 21-2  Positive and negative delta and gamma.
Theoretical P&L
Underlying price
Positive gamma
(a “smile”)
Negative gamma
(a “frown”)
Positive delta
Positive delta
Negative delta
Negative delta
Delta neutral
--- page 435 ---

418
O P T I O N V O L AT I L I T Y A N D P R I C I N G
In addition to considering the risk sensitivities—delta, gamma, theta, and
vega—and the way in which these values change as market conditions change,
traders are well advised to look at the net contract position. If the market makes a
dramatic downward move such that all calls move far out of the money while
all puts go deeply into the money, or the market makes a dramatic upward
move such that all puts move far out of the money while all calls go deeply into
Figure 21-5  Positive gamma position as volatility changes.
Positive vega – the position loses value as volatility falls.
Negative vega – the position loses value as volatility rises.
In both cases, the graph is shifted downward.
Theoretical P&L
Underlying price
Positive vega – the position gains value as volatility rises.
Negative vega – the position gains value as volatility falls.
In both cases, the graph is shifted upward.
Figure 21-4  Negative gamma, positive theta position as time passes.
Theoretical P&L
Underlying price
With no movement in the underlying price,
the position gains value as time passes.
The graph is shifted upward.
--- page 436 ---

P o s i t i o n A n a ly s i s 	 419
the money, what will be the result? In other words, if the market falls and all
puts begin to act like short underlying contracts, or the market rises and all calls
begin to act like long underlying contracts, what is the trader left with? In our
position, the downside contract position is short five. At very low underlying prices,
the long 10 September 95 puts together combined with the long 5 underlying contracts will act like a position that is short 5 underlying contracts. The
Figure 21-6  Negative gamma position as volatility changes.
Theoretical P&L
Underlying price
Positive vega – the position loses value as volatility falls.
Negative vega – the position loses value as volatility rises.
In both cases, the graph is shifted downward.
Positive vega – the position gains value as volatility rises.
Negative vega – the position gains value as volatility falls.
In both cases, the graph is shifted upward.
Figure 21-7  Position delta as the underlying price and volatility change.
–400
–300
–200
–100
0
100
200
Position delta
85
90
95
100
105
110
115
–500
Underlying price
Volatility = 14%
Volatility = 18%
Volatility = 22%
99.60
Long 10 September 95 puts
Short 10 September 105 calls
Long 5 underlying contracts
--- page 437 ---

420
O P T I O N V O L AT I L I T Y A N D P R I C I N G
upside contract position is also short five. At very high underlying prices, the short
10 September 105 calls combined with the long 5 underlying contracts will
act like a position that is also short 5 underlying contracts. This is apparent in
Figure 21-7; the delta approaches –500 in either direction.
The net contract position may sometimes seem irrelevant, particularly if a
position consists of very far out-of-the-money options. After all, how likely is it
that they will go so deeply into the money that they will act like underlying contracts? But traders have learned, sometimes through painful experience, that
big moves occur more often in the real world than one might expect. Extraordinary and unpredictable events—political and economic upheavals, scientific
breakthroughs, natural disasters, corporate takeovers—can sometimes cause
markets to move dramatically. When this occurs, a trader may find that options
that “couldn’t possibly go into the money” have done just that.
A trader who is short very far out-of-the-money options may believe that
there is so little chance that the options will go into the money that there is no point
in buying them back. This may be true, but the clearinghouse will still require
a margin deposit for each short option. In order to eliminate this requirement,
and perhaps put the money to better use, the trader may want to buy back the
options. Of course, he will only want to do this if the price is reasonable. Certainly,
the price that the trader will be willing to pay ought to be less than the margin
requirement. In the same way, a trader who is long very far out-of-the-money
options that he believes are worthless will usually be happy to sell the options at
whatever price he can. After all, something is better than nothing, which is what
the options will be worth if they expire out of the money.
Very often the price at which traders are willing to buy or sell very far
out-of-the money options is less than the minimum price that the exchange
Figure 21-8  Position gamma as the underlying price and volatility change.
–40
–20
0
20
40
60
80
Position gamma
85
90
95
100
105
110
115
–60
Underlying price
Volatility = 18%
Volatility = 22%
99.60
Volatility = 14%
Long 10 September 95 puts
Short 10 September 105 calls
Long 5 underlying contracts
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
