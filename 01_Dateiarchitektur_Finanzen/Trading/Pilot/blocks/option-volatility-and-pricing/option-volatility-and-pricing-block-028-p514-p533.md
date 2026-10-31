# Option Volatility and Pricing_ Advanced Trading Strategies -- Sheldon Natenberg -- 2nd ed, 2014 -- McGraw Hill Professional -- isbn13 9780071818773 -- 6a48d008bd9beef283debf7bad0b2e4a -- Anna’s Archive.pdf — pages 514–533

--- page 514 ---

V o l at i l i t y S k e w s 	 497
Figure 24-9  Skewness.
Negative skewness
(lower exercise prices carry
higher implied volatilities)
Positive skewness
(higher exercise prices carry
higher implied volatilities)
Zero skewness
(the volatility skew is
symmetrical)
Higher exercise prices
Implied volatility
Lower exercise prices
At the money
Figure 24-10  Kurtosis.
The implied volatility of both lower
and higher exercise prices increases.
As kurtosis increases, the volatility
skew becomes more curved.
Zero kurtosis
(the volatility skew
is a straight line)
Higher exercise prices
Implied volatility
Lower exercise prices
At the money
We might think of the skew as an input into a theoretical pricing model
(Figure 24-11), but the skew is input into the model as a formula rather than as
--- page 515 ---

498
O P T I O N V O L AT I L I T Y A N D P R I C I N G
Figure 24-11  The skew as a model input.
Time to expiration
Exercise price
Theoretical
pricing model
Theoretical
value
Underlying price
Interest rate
Volatility
Skew
a single number. As with any input, it will be useful to determine how sensitive
an option value or option position is to changes in the shape of the skew.
The sensitivities associated with a skew will depend on the skew model
that is used. For example, let’s assume a very simple second-degree-polynomial
model where the volatility y at an exercise price x is given by
y = a + bx + cx2
In this model, the value of a is the base volatility, usually the implied volatility
of the at-the-money options. The values of b and c represent the skewness and
kurtosis, respectively, of the volatility skew. We can raise or lower the value of
a as implied volatility rises or falls. We can raise or lower the value of b to increase or decrease the skewness. And we can raise or lower the value of c to increase or decrease the kurtosis. b can be either positive or negative depending
on whether higher or lower exercise prices are inflated. For exchange-traded
markets, the value of c is almost always positive because the probability distributions of these markets always exhibit some fat-tail characteristics.
The sensitivity of an option’s theoretical value to a change in skewness or
kurtosis will depend on how the option’s value changes as we raise or lower the
value of b and c. If raising the value of b by one unit will cause the option to fall
by 0.15, then the option has a skewness sensitivity of –0.15. If raising the value of
c by one unit will cause the option to rise by 0.08, the option has a kurtosis sensitivity of 0.08. For active traders who carry very large option positions, the skewness and kurtosis sensitivities can represent significant risks and, as with all risks,
must be monitored to ensure that that they remain within acceptable bounds.
The units used to express skewness and kurtosis sensitivity will depend on
how the skew model has been constructed. Most traders choose a unit that represents a common change in the skewness and kurtosis values. For example, if
the value of b commonly ranges from 0.20 to 0.40, a logical unit for b might be
0.01. If the unit value is an unwieldy number, the value can be adjusted by including a multiplier. If the unit value for b is 0.001 but we wish to express the
--- page 516 ---

V o l at i l i t y S k e w s 	 499
unit value as a whole number, we can use a multiplier of 0.001 to yield a unit
value of 1. The model will then be expressed as
y = a + 0.001bx + cx2
If we raise the skew value of b by 1, we are really raising it by 0.001. The same
approach can also be used to express c in simple units.5
In most skew models, the at-the-money exercise price acts as a pivot point
so that an option that is exactly at the money has a skewness and kurtosis sensitivity of 0. Options that are in the money or out of the money can have either
a positive or a negative skewness sensitivity. If we increase the skewness input,
the volatility of higher exercise prices will rise, whiles the volatility of lower
exercise prices will fall. Consequently, higher exercise prices will have positive skewness sensitivity values, and lower exercise prices will have negative
sensitivity. If we increase the kurtosis input, the volatility of options at both
higher and lower exercise prices will rise. Consequently, any option that is not
exactly at the money will have a positive kurtosis sensitivity.
Which options are the most sensitive to changes in skewness and kurtosis?
There is no definitive answer because it depends on the volatility characteristics
of the market as well as the skew model that is used. But in many skew models
puts with deltas of –25 and calls with deltas of +25 tend to have the greatest
skewness sensitivity. For this reason, a common measure of skewness is the difference between the implied volatility of the –25 delta put and the +25 delta
call. There is no similar benchmark for kurtosis, but for many models, puts with
deltas of approximately –5 and calls with deltas of +5 tend to have the greatest
sensitivity to a change in kurtosis.
Skewed Risk Measures
How we model the volatility skew also will affect the risk measures generated by
a model—the delta, gamma, theta, and vega. Look again at Figure 24-4a, where
the floating skew is shifted either right or left as the underlying price rises or falls.
As the skew is shifted, the volatility at some exercise prices will rise, while the
volatility at other exercise prices will fall. This change in volatility can cause an
option’s value and its risk sensitivities to change either more or less than expected
if there were no skew.
For example, consider an out-of-the-money put with a delta of –20. Ignoring the gamma, if the underlying price rises 1.00, we expect the option value to
decline by 0.20. But in an investment skew, such as in Figure 24-4a, as the underlying price rises, the volatility of an out-of-the-money put will rise as it moves further out of the money. If the option has a vega of 0.10 and the shift in the skew
causes the implied volatility of the option to rise 0.5 percent, the higher volatility
5 When traders use the terms skewness and kurtosis (or skew and kurt for short), it is not always clear whether they
are referring to the inputs into the model (the values of b and c in our example) or the sensitivity of the option’s
value to a change in these inputs. Typically, a trader will refer to the sensitivities as the option’s skewness or kurtosis. Or the trader will refer to his skewness and kurtosis position: the sensitivity of his entire position to a oneunit change in the skewness or kurtosis inputs.
--- page 517 ---

500
O P T I O N V O L AT I L I T Y A N D P R I C I N G
will cause the option’s value to rise by 0.5 × 0.10 = 0.05. Consequently, the option
will only decline by 0.15, a decline of 0.20 due to a change in the underlying price
combined with an increase of 0.05 due to the increase in implied volatility. The
option has a skewed or adjusted delta of –15.
The inclusion of a volatility skew in a pricing model will affect the calculation of all option risk measures and can greatly complicate a trader’s ability
to manage risk. For many traders, it may be best to keep things simple, perhaps using a skew model to generate theoretical values while using a traditional
model to calculate the delta, gamma, theta, and vega. For an active trader who
carries large option positions, calculating accurate skewed sensitivities becomes
much more important because the total value of the position can change very
quickly as market conditions change. Financial engineers at professional option
trading firms are often responsible for developing methods to accurately calculate theoretical values and risk sensitivities using a volatility skew model. But
even the most sophisticated model is unlikely to generate values that exactly
model option prices under all market conditions. A model can help, but it will
always have limitations.
By combining the volatility term structure across expiration dates with the
volatility skew across exercise prices, we can form a volatility surface. While sometimes difficult to visualize, a volatility surface may enable a trader to more easily see
the basic volatility characteristics of an option market. The more exercise prices
and expiration dates that are available, the more accurate will be the volatility surface. Sample volatility surfaces for the FTSE 100 options and wheat options are
shown in Figures 24-12 and 24-13. At the time, the FTSE 100 Index was trading
at 5,966, and the front-month wheat futures contract was trading at 647.
Figure 24-12  FTSE 100 volatility surface, March 16, 2012.
3
5
7
9
11 13 15 17
10%
15%
20%
25%
30%
35%
40%
45%
4000
4200
4400
4600
4800
5000
5200
5400
5600
5800
6000
6200
6400
6600
6800
7000
7200
7400
7600
7800
8000
Implied volatility
Exercise price
Months to expiration
--- page 518 ---

V o l at i l i t y S k e w s 	 501
Shifting the Volatility
Traders have long noted that in many option markets, implied volatility tends
to change as the price of the underlying contract changes. Some markets exhibit a direct relationship between movement in the underlying price and
changes in implied volatility: when the underlying price rises, implied volatility tends to rise; when the underlying price falls, implied volatility tends to fall.
This is typical of markets with a demand skew, such as agricultural and energy
products. Other markets may exhibit an inverse relationship: when the underlying price rises, implied volatility tends to fall; when the underlying price falls,
implied volatility tends to rise. This is typical of markets with an investment
skew, such as stock and stock index markets.
For purposes of both option evaluation and risk management, many traders will attempt to incorporate this characteristic into an option pricing model.
One possible theoretical solution is the CEV model referred to in Chapter 23.
But this model can be mathematically complex and requires additional inputs,
all of which make it difficult to use. Alternatively, many traders simply use a
“home grown” model that shifts the volatility up or down in a way that is consistent with the observed volatility characteristics of a market. However, no
model will generate accurate values under all conditions because implied volatility often changes in ways that seem to defy even the best model.
Figure 24-13  Wheat volatility surface, January 27, 2012.
1
3
5
7
9
1112
25%
20%
30%
35%
40%
45%
400
420
440
460
480
500
520
540
560
580
600
620
640
660
680
700
720
740
760
780
800
820
840
860
880
900
920
940
960
980
1000
Implied volatility
Exercise price
Months to expiration
--- page 519 ---

502
O P T I O N V O L AT I L I T Y A N D P R I C I N G
A shift in volatility can also affect the risks associated with a position. Consider a trader who buys an at-the-money straddle. Ignoring interest considerations and slight adjustments for a lognormal distribution, the trader’s position
is approximately delta neutral: the call has a delta of 50, and the put has a
delta of –50. But delta neutral means that the trader has no particular preference for market movement in one direction or the other. Is this really true? If
this position is taken in a stock index market, the trader actually has a preference for downward movement because he prefers higher volatility, something
that is more likely to occur in a falling market. Even though the position may be
delta neutral in a theoretical world, in the real world, it is delta negative. On the
other hand, if this position is taken in a commodity market, where the market
is likely to become more volatile when prices rise, the trader really has a positive
delta position. Of course, it may be difficult to determine the real-world delta
of either position. That will depend on how fast volatility rises or falls as the
underlying price changes. But in neither case is the position truly delta neutral.
Skewness and Kurtosis Strategies
Just as a trader may have an opinion about the direction of movement in a market
(delta strategies) or about implied and realized volatility (vega and gamma strategies), a trader may also have an opinion about the shape of the volatility skew. We
can see in Figure 24-14 that, depending on the type of skew and whether a trader
expects the skew to become steeper or flatter, the trader will want to buy lower
Figure 24-14  (a ) Declining skewness. (b ) Increasing skewness.
In an investment skew, if the skew
is expected to become flatter, a trader
will want to sell lower exercise prices
and buy higher exercise prices.
In a demand skew, if the skew
is expected to become flatter, a trader
will want to sell higher exercise prices
and buy lower exercise prices.
Higher exercise prices
Implied volatility
Lower exercise prices
At the money
(a )
(continued)
--- page 520 ---

V o l at i l i t y S k e w s 	 503
exercise prices and sell higher exercise prices, or vice versa. This is most commonly
done using out-of-the-money options, very often 25 delta calls and –25 delta puts
because these options tend to be most sensitive to changes in the slope of the skew.
If a skew trade is not hedged, the position will clearly have a positive delta
(long calls and short puts) or negative delta (long puts and short calls). A trader
who wants to focus solely on “buying skew” or “selling skew” must offset the
delta position, most commonly with an opposing delta position in the underlying contract. When this is done, the entire strategy is usually referred to as a risk
reversal. With the underlying contract trading at a price close to 100, the following are typical risk reversals (delta values are in parentheses):

+10 June 95 puts (–25)

–10 June 105 calls (+25)

+5 underlying contracts
or

–30 December 90 puts (–15)

+30 December 110 calls (+15)

–9 underlying contracts
In these examples, the calls and puts have the same delta, but this is not a
requirement. More commonly, calls and puts are chosen with the same vega
values.6 This ensures that the position is vega neutral at inception and therefore primarily sensitive to changes in the slope of the skew rather than changes
in overall implied volatility. Of course, as market conditions change, the delta,
6 A risk reversal that is vega neutral will tend to be gamma neutral, although this will not always be the case. A trader
may have to decide whether it is more important for the risk reversal to be vega neutral or gamma neutral.
In an investment skew, if the skew
is expected to become steeper, a trader
will want to buy lower exercise prices
and sell higher exercise prices.
In a demand skew, if the skew
is expected to become steeper, a trader
will want to buy higher exercise prices
and sell lower exercise prices.
Higher exercise prices
Implied volatility
Lower exercise prices
At the money
(b )
Figure 24-14  (continued )
--- page 521 ---

504
O P T I O N V O L AT I L I T Y A N D P R I C I N G
gamma, and vega of the position will almost certainly change. When this
occurs, a trader will have to decide whether to maintain the position and, if so,
how best to manage the delta, gamma, and vega risk. The risk characteristics
of a typical risk reversal were discussed in Chapter 21.
Just as a trader may have an opinion about skewness, the slope of a volatility
skew, a trader may also have an opinion about kurtosis, the curvature of a volatility skew. If the kurtosis is expected to increase, the prices of options at both lower
and higher exercise prices will increase. A trader will therefore want to buy strangles by purchasing both out-of-the-money calls and out-of-the-money puts. If the
kurtosis is expected to decrease, option prices at both lower and higher exercise
prices will decline. A trader will then want to sell strangles by selling both out-ofthe-money calls and out-of-the-money puts. This is shown in Figure 24-15.
If a trader “buys” kurtosis by purchasing strangles or “sells” kurtosis by
selling strangles, the position will also be sensitive to overall changes in volatility because the position will have a very pronounced positive or negative vega.
Even if the trader is correct in his assessment of kurtosis, the position can be
negatively affected by overall changes in implied volatility. If the trader wishes
to focus solely on kurtosis, he will need to neutralize his vega position without
changing the kurtosis of the position. Because at-the-money options are neutral
with respect to kurtosis, a trader can achieve this by taking an offsetting vega
position in at-the-money straddles. Assuming that the selected strangles and
straddles are delta neutral, the entire position will also be delta neutral. With
the underlying contract trading at a price close to 100, the following are typical
kurtosis positions (vega values are in parentheses):
Figure 24-15  Rising and falling kurtosis.
If the skew is expected to become
more curved (greater kurtosis), a
trader will want to buy both lower and
higher exercise prices (buy strangles).
If the skew is expected to become
less curved (lower kurtosis), a
trader will want to sell both lower and
higher exercise prices (sell strangles).
Higher exercise prices
Implied volatility
Lower exercise prices
At the money
--- page 522 ---

V o l at i l i t y S k e w s 	 505

Long strangles:
+35 June 90 puts (0.11)

+35 June 110 calls (0.12)

Short straddles:
–20 June 100 calls (0.20)

–20 June 100 puts (0.20)
or

Short strangles:
–26 December 80 puts (0.08)

–26 December 120 calls (0.09)

Long straddles:
+10 December 100 calls (0.22)

+10 December 100 puts (0.22)
If a kurtosis position is made up of a strangle that has exactly half the vega of the
straddle, a vega-neutral position will consist of two strangles for each straddle.
When done in this 2 × 1 ratio, the position is sometimes referred to as a dragonfly.
An opinion about skew and kurtosis can also be incorporated into other
strategies. Consider the skews in Figure 24-16 on the same underlying product but for different expiration months. If a trader has no opinion on whether
either skew is mispriced individually but believes that the skews are mispriced
with respect to each other, a logical strategy might be to take a skew position
in one expiration month and an opposing skew position in the other month.
For example, a trader might buy out-of-the-money puts in June and sell out-ofthe-money puts in March. At the same time, the trader might sell out-of-themoney calls in June and buy out-of-the-money calls in March. The trader has,
in effect, bought put calendar spreads and sold call calendar spreads. If the
skew is the only consideration (the trader has no opinion on whether implied
Figure 24-16  Buying and selling skew in different expiration months.
Buy out-of-the-money June puts
Sell out-of-the-money March puts
and
Sell out-of-the-money June calls
Buy out-of-the-money March calls
Higher exercise prices
Implied volatility
Lower exercise prices
At the money
March skew
June skew
--- page 523 ---

506
O P T I O N V O L AT I L I T Y A N D P R I C I N G
volatility is high or low), the trader will try to take a position that is vega neutral by choosing calendar spreads that have approximately the same vega. Any
residual deltas can be hedged away with the underlying contract.
If, in addition to an opinion about the skew, a trader also has an opinion about
the relative implied volatility in different expiration months, he can take this into
consideration when choosing a strategy. If a trader believes that implied volatility in
June is low compared with implied volatility in March, the trader will consider buying calendar spreads—buy June options and sell March options. If, at the same time,
the trader also believes that the skews are mispriced with respect to each other, as in
Figure 24-16, he will choose calendar spreads that take both relationships into consideration. Now he will want to buy put calendar spreads—buy out-of-the-money
June puts and sell out-of-the-money March puts. By doing so, the trader takes advantage of both implied volatility and skew. Note that the trader will avoid call calendar spreads because the volatility and skew will tend to offset each other. The June
calls are too expensive with respect to skew, but the March calls are too expensive
with respect to implied volatility. If the trader believes that June implied volatility is
high compared with March, now he will choose to sell call calendar spreads because
the June calls are too expensive with respect to both implied volatility and skew.
The same approach can be used when kurtosis in two different expiration
months seems to be mispriced, as shown in Figure 24-17. Now a trader might consider buying June strangles and selling March strangles. If this is a simple kurtosis strategy within a single expiration month, it will be necessary to offset the vega
by purchasing at-the-money straddles. But a trader can avoid this complication
by choosing strangles in the two different expiration months that have approximately the same vega values. This ensures that the entire strategy is sensitive only
Figure 24-17  Buying and selling kurtosis in different expiration months.
Buy June strangles
and
Sell March strangles
Higher exercise prices
Implied volatility
Lower exercise prices
At the money
March skew
June skew
--- page 524 ---

V o l at i l i t y S k e w s 	 507
to changes in kurtosis. If, at the same time, June implied volatility seems low compared with March, the strategy has an added advantage. June options are cheap
compared with March options with respect to both volatility and kurtosis.
Implied Distributions
In a perfect Black-Scholes world, the prices of the underlying contract are
assumed to be lognormally distributed at expiration, and every option with the
same expiration date ought to have the same implied volatility. The fact that
options across different exercise prices have different implied volatilities must
mean that the marketplace believes that the distribution of underlying prices at
expiration is not lognormal. Exactly what probability distribution is the marketplace implying to the underlying contract at expiration? We can estimate this
implied distribution by looking at the prices of butterflies in the marketplace.
At expiration, a butterfly has a minimum value of 0 if the underlying price
is at or outside the wings and a maximum value of the amount between exercise prices if the underlying price is exactly at the body, or midpoint, of the butterfly. At expiration, the 95/100/105 butterfly (i.e., buy a 95 call, sell two 100
calls, buy a 105 call) will have a minimum value of 0 if the underlying price is
at or below 95 or at or above 105, a maximum value of 5.00 if the underlying price is exactly 100, or some amount between 0 and 5.00 if the underlying
price is between 95 and 100 or between 100 and 105.
Suppose that exercise prices at five-point intervals are available extending
from 0 to infinity:
…, 70, 75, 80, 85, 90, 95, 100, 105, 110, 115, 120, 125, 130,…
What will be the value of the position at expiration if we buy every five-point
butterfly?
…  +1 70 call  +1 75 call  …  +1 115 call  +1 120 call  …
…  –2 75 calls  –2 80 calls  …  –2 120 calls  –2 125 calls  …
…  +1 80 call  +1 85 call  …  +1 125 call  +1 130 call  …
Regardless of the underlying price at expiration, the entire position will always
have a value of exactly 5.00. As a result, if we add up the prices of all the butterflies, the total value must be 5.00.7
Suppose that we make the assumption that the only prices that are possible
at expiration are prices that are equal to an exercise price
…, 70, 75, 80, 85, 90, 95, 100, 105, 110, 115, 120, 125, 130,…
The probability of each underlying price occurring must be equal to the price
of that butterfly, where the inside exercise price is equal to the underlying price
divided by 5.00. If the price of the 75/80/85 butterfly is 0.15, the probability
of an underlying price of 80 at expiration must be
0.15/5.00 = 0.03 (3%)
7If we include interest rates, and the options are subject to stock-type settlement, the total will be the present value
of 5.00.
--- page 525 ---

508
O P T I O N V O L AT I L I T Y A N D P R I C I N G
If the price of the 90/95/100 butterfly is 0.50, the probability of an underlying
price of 95 at expiration must be
0.50/5.00 = 0.10 (10%)
Figure 24-18 shows a series of call values together with the resulting butterfly values for our series of exercise prices.8 The probability associated with each underlying price is determined by dividing the butterfly value by the total value of all
butterflies, which we know must be 5.00. (The reader may wish to confirm that
all the butterfly values do indeed sum to 5.00 and that the probabilities sum to
1.00, or 100 percent.) The underlying prices and their associated probabilities are
shown in Figure 24-19. Note that these values form a probability distribution that
is skewed to the right. This should come as no surprise because the values were
derived from the Black-Scholes model, which assumes a lognormal distribution
of underlying prices.
8The values in Figure 24-18 correspond, approximately, to Black-Scholes values using an underlying price of 100,
three months to expiration, a volatility of 20 percent, and an interest rate of 0.
Exercise price:
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
135
Call value:
25.00 20.04 15.20 10.71
6.88
3.98
2.06
0.95
0.39
0.15
0.05
0.01
0
Butterfly value:
0.04
0.12
0.35
0.66
0.93
0.98
0.81
0.55 0.32
0.14
0.06
0.03
0.01
Price probability:
0.008 0.024 0.070 0.132 0.186 0.196 0.162 0.110 0.064 0.028 0.012 0.006 0.002
Figure 24-18  Butterfly values and probabilities.
Figure 24-19  A discrete probability distribution implied from the prices of butterflies.
Probability
20%
18%
16%
14%
12%
10%
8%
6%
4%
2%
Underlying price
0%
60
115
110
105
100
95
90
85
80
70
75
65
120 125 130 135 140
--- page 526 ---

V o l at i l i t y S k e w s 	 509
Figure 24-20  A continuous lognormal probability distribution implied from the prices of
butterflies.
Probability
0.0045
0.004
0.0035
0.003
0.0025
0.002
0.0015
0.001
0.0005
60
115
110
105
100
95
90
85
80
70
75
65
120 125 130 135
Underlying price
140
0
Of course, the distribution in Figure 24-19 is only an approximation
because it includes a limited number of underlying prices. A more exact distribution requires us to consider more and more exercise prices. We can do this by
reducing the width of the butterflies. Instead of using increments of 5.00, we
might use increments of 2.00, 1.00, or 0.50. Indeed, if we use increments that are
infinitesimally small, the butterfly values will enable us to construct a continuous
probability distribution. Figure 24-20 shows the probability distribution with
the increment between exercise prices reduced to 0.10. With such a small increment, the distribution appears almost continuous.
How does the distribution implied by option prices compare with a traditional lognormal distribution? The implied distribution will change as option
prices change, so there cannot be one implied distribution under all market
conditions. But we might get some sense of the distribution that the marketplace is implying by using the prices of butterflies generated by a volatility
skew to derive a distribution and comparing it with a Black-Scholes distribution with a constant volatility. In Figure 24-21, we have taken the volatility
skew for the FTSE 100 options shown in Figure 24-3 and created two distributions, one from the prices generated from the skew and one from prices generated from a constant volatility across every exercise price. What can we infer
from Figure 24-21?
--- page 527 ---

510
O P T I O N V O L AT I L I T Y A N D P R I C I N G
Compared with a traditional lognormal distribution, the marketplace
seems to be implying the following:
1.	 A greater probability of a small to intermediate upward move
2.	 A greater probability of a large downward move
3.	 A smaller probability of a small to intermediate downward move
4.	 A smaller probability of a large upward move
This implied distribution is typical of most stock index markets, and many of
these points seem to be consistent with the S&P 500 histogram in Figure 23-8a.
There do seem to be more small moves in the real world than is predicted by
a theoretical distribution. There also seem to be more large downward moves
and fewer intermediate downward moves. But the histogram also shows more
big upward moves, which is not consistent with the implied distribution.
Figure 24-22 shows the three-month distribution implied from the prices
of options on wheat futures on January 27, 2012. This implied distribution
seems to conform more closely to a theoretical lognormal distribution than
Figure 24-21  Three-month price distribution implied from FTSE 100 option prices, March
16, 2012 (FTSE 100 Index = 5,965.58).
Probability
3,000
3,500
4,000
4,500
5,000
5,500
6,000
6,500
7,000
7,500
Index price
8,000
Theoretical (lognormal) distribution
Distribution implied from market prices
--- page 528 ---

V o l at i l i t y S k e w s 	 511
does the distribution in the FTSE 100 example. However, the marketplace is
still implying more small moves, slightly fewer intermediate upward moves, and
slightly more large upward moves than a true lognormal distribution.
Of course, Figures 24-21 and 24-22 are snapshots of markets at one
moment in time, and it would be unwise to draw any sweeping conclusions
from these examples. Nonetheless, it can often be useful for a trader to compare
his opinions about a probability distribution with that implied by prices in the
marketplace. If there is a clear disagreement, it may point the way to a potentially profitable strategy.
Figure 24-22  Three-month price distribution implied from wheat option prices, January
27, 2012 (with three-month wheat futures at 661.75).
Probability
300
400
500
600
700
800
900
1,000
1,100
Futures price
1,200
Theoretical (lognormal) distribution
Distribution implied from market prices
--- page 529 ---

512
Volatility Contracts
Volatility contracts have been one of the major success stories in the derivatives
market. They enable market participants to pursue strategies that were previously either impossible or, even under the best conditions, difficult to execute. But
volatility contracts have unusual characteristics, and any trader hoping to make
the best use of these contracts must be fully familiar with these characteristics.
Prior to the introduction of options and option pricing models, there was
no effective way for a trader to capture volatility value or to profit from a perceived mispricing of volatility in the marketplace. Once listed options were introduced, however, it became possible to use the implied volatility in an option
market to determine how the marketplace was pricing volatility. In Chapter 8,
we showed that a trader could then capture a volatility mispricing by either
buying or selling options and dynamically hedging the position over the life of
the option.
This all sounds very good in theory, but in the real world, things are not
so simple. Even if we are somehow able to look into the future and determine
the true volatility of the underlying contract over the life of the option, the actual results of any single dynamic hedging strategy will almost certainly differ
from the results predicted by the theoretical pricing model. This is often due
to the weaknesses in traditional theoretical pricing models, many of which we
touched on in Chapter 23:

The order in which price changes occur can affect the results of a
dynamic hedging strategy.

If gaps occur in the underlying price, it may not be possible to buy
or sell the underlying contract in a way that is consistent with the
dynamic hedging process.

The returns for an underlying contract may not be normally
distributed.
In addition to weakness in the model, the costs of dynamically hedging a position may be significant. Each time the position is rehedged, a trader may have
to give up the bid-ask spread, and there will also be brokerage and exchange fees.
These costs will certainly reduce, and may even erase, any expected profit.
25
--- page 530 ---

V o l at i l i t y C o n t r a c t s 	 513
Even if one is interested in trading volatility, the drawbacks of using a dynamic hedging approach will often deter a trader from using options to trade
volatility. To overcome this obstacle, traders have sought a less complicated
method of implementing volatility strategies. This has led to the development
of volatility contracts, contracts that enable a trader to take a position on volatility without going through a complex and costly dynamic hedging process. At
expiration, the value of these contracts depends solely on a relatively straightforward volatility calculation.
There are two primary types of volatility—realized volatility and implied
volatility. Consequently, there are two types of volatility contracts. Realized volatility contracts settle into the realized volatility of an underlying contract over a
specified period of time. Implied volatility contracts settle into the implied volatility
of options on an underlying contract on a specified date.
Realized Volatility Contracts
At expiration, the value of a realized volatility contract is equal to the annualized standard deviation of logarithmic price returns over the life of the contract. The returns are typically calculated from daily settlement prices on the
primary exchange on which the contract is traded. This means that the annualization factor will depend on the number of trading days in a year on that particular exchange. If there are 252 trading days, the settlement volatility will be
∑
−
x
n
252
ln(
)
i
i
n
2
1
where each data point xi is equal to the daily price returns pi/pi–1 (today’s settlement price divided by yesterday’s settlement price), and n is the number of
trading days in the calculation period.
There are two points of particular note. First, the expiration value represents the true volatility over the calculation period rather than a volatility estimate. We therefore use the population standard deviation rather than the
sample standard deviation, dividing by n rather than n – 1. Second, the volatility calculation is independent of any trend in prices. We therefore assume a 0
mean, using ln(xi) for each data point rather than ln(xi) – µ. These calculation
conventions are common to most realized volatility contracts.
The profit or loss at expiration for a realized volatility contract will depend on
the price at which the initial trade was made, the notional amount of the trade,
and the value of the contract at expiration. If the buyer of a realized volatility
contract enters into the trade at a price of 20 percent with an agreed-on notional
amount equal to $1,000 per volatility point and the realized volatility over the calculation period turns out to be 23.75 percent, the buyer will show a profit of
$1,000 × (23.75 – 20.00) = $3,750
If the realized volatility turns out to be 18.60 percent, the buyer will show a
loss of
$1,000 × (18.60 – 20.00) = –$1,400
--- page 531 ---

514
O P T I O N V O L AT I L I T Y A N D P R I C I N G
Realized volatility contracts are most often traded in the off-exchange market, with banks and proprietary trading firms acting as market makers.1 Quotes
for realized volatility contracts typically include a price, quoted in volatility
points, and a volatility exposure, quoted as notional vega. A market maker who
offers a quote for realized volatility of 19.50 –20.50 for $10,000 notional vega
is willing to buy the contract at a volatility of 19.50 percent and sell the contract at a volatility of 20.50 percent, with every volatility point having a value
of $10,000. In the same way, a client may put in an order to buy $25,000 notional vega at 30. The client is prepared to pay a volatility of 30 percent, with
every volatility point having a value of $25,000.
In these examples, the price of the volatility contract was quoted in volatility points and settled in volatility points. In fact, most realized volatility contracts
are settled in variance points, where variance is equal to the square of volatility
variance = volatility2  and,  conversely,  volatility = variance
For this reason, realized volatility contracts are often referred to as variance contracts or, more commonly, variance swaps.
Why settle a volatility contract in variance points rather than volatility
points? As we shall see later, for purposes of hedging a volatility contract,
it is much easier to replicate a variance position than a volatility position.
Additionally, the reader may recall from the discussion of forward volatility in
Chapter 20 that variance has the very desirable characteristic that it is proportional to time. If the variance over some time period t1 is equal to σ1
2 and the
variance over a second successive time period t2 is equal to σ 2
2, then the variance over the combined time periods is
σ
σ
(
)
(
)
×
+
×
+
t
t
t
t
1
1
2
2
2
2
1
2
This means that variance contracts can be easily combined to cover consecutive time periods, even if the time periods are not of equal length.
For example, if the annualized volatility over a two-month time period is
25 (expressing the volatility in points) and the annualized volatility over the following one-month time period is 22, the annualized variance over the entire
three-month period is
(
) (
)
(
) (
)
×
+
×
=
×
+
×
=
2/12
25
1/12
22
3/12
2/12
625
1/12
484
3/12
578
2
2
If a volatility contract is quoted in volatility points with a notional vega
amount, but settlement is in variance points, how much is each variance point
worth? Without going into the mathematics, by convention, each variance
point is equal to the notional amount divided by twice the volatility price
=
×
Value per variance point
vega notational
2
volatility price
1 When a contract is traded between private parties without an exchange as an intermediary, the possibility of
one party defaulting on its obligations adds an additional risk dimension to the trade. Counterparty risk can be
an important consideration in the off-exchange market.
--- page 532 ---

V o l at i l i t y C o n t r a c t s 	 515
If the buyer of a volatility contract pays 20 for $10,000 vega notional, but the
contract is settled in variance points, each variance point has a value of
$10,000/2 × 20 = $250
If the realized volatility over the life of the contract turns out to be 19 percent,
the buyer will show a loss of
$250 × (192 – 202) = $250 × (361 – 400) = $9,750
If the realized volatility over the life of the contract turns out to be 23 percent,
the buyer will show a profit of
$250 × (232 – 202) = $250 × (529 – 400) = $32,250
Because variance is the square of volatility, if a contract is settled in variance points, the value at settlement can quickly escalate with higher volatilities.
If a single dramatic event occurs that causes the underlying contract to make
an unexpectedly large move, resulting in a volatility over the calculation period
of 50, the profit to the buyer in our example will be
$250 × (502 – 202) = $250 × (2,500 – 400) = $525,000
Of course, the seller will have an equal loss. Indeed, the seller of a variance swap
may not be willing to take on the risk of a one-time dramatic event that causes
volatility to skyrocket. Many variance swaps therefore have a cap that limits the
expiration value of the contract. If the contract trades at a price of 20 and has
a volatility cap of 40 (equal to a variance of 1,600), no matter how high volatility goes, the profit to the buyer and risk to the seller can never be greater than
$250 × (402 – 202) = $250 × (1,600 – 400) = $300,000
Caps are most common for variance swaps on individual stocks, where
a one-time event can result in a dramatic increase in volatility. Caps are less
common for variance swaps on broad-based indexes, where a one-time event
affecting one index component is unlikely to have a correspondingly large
effect on the volatility of the entire index. Of course, variance swaps are primarily an off-exchange product. The buyer and seller of the swap are free to
negotiate any contract specifications, including a cap, that are mutually agreeable to both parties.
Implied Volatility Contracts
Realized volatility is an important consideration in option pricing, but it is
something that cannot be directly observed, at least at any given moment in
time. When option traders talk about volatility, they are most often referring to
implied volatility, which is something that can be observed. The implied volatility is a consensus, derived from the prices of options in the marketplace, of
what the volatility of the underlying contract will be over some period in the
future. Because option prices can be observed at any moment in time, implied
volatility at any moment can likewise be observed.
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
