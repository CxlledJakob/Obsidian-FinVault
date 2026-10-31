# Option Volatility and Pricing_ Advanced Trading Strategies -- Sheldon Natenberg -- 2nd ed, 2014 -- McGraw Hill Professional -- isbn13 9780071818773 -- 6a48d008bd9beef283debf7bad0b2e4a -- Anna’s Archive.pdf — pages 153–172

--- page 153 ---

136
O P T I O N V O L AT I L I T Y A N D P R I C I N G
an in-the-money call has a greater likelihood of going out of the money. Consequently, the deltas of both options will move toward 50.
Note that the delta of an at-the-money option tends to remain close to
50 regardless of volatility. This is true in general, although changing interest
rates or, in the case of stock options, changing dividends may alter the forward
price. Because theoretical pricing models evaluate options in relation to the forward price, the delta of an at-the-money call may in fact be either more or less
than 50. Even if the option is exactly at the forward (the exercise price and forward price are the same), a call will still have a delta that is slightly greater than
50 because of the lognormal distribution used to evaluate the option. This is
evident in Figure 9-1, where the delta of an at-the-money call tends to increase
slightly as volatility increases.
Because an option’s delta changes as volatility changes, no trader can be
certain that a position is really delta neutral. The delta depends on the volatility of the underlying contract, and this is something that will occur in the future
over the life of the option. The volatility we use to calculate the delta is a guess.
We might guess right, but we also might guess wrong. And if we guess wrong,
our delta values will be wrong.
Rather than try to guess the future volatility, many traders use the implied delta, the delta that results from using the implied volatility. Using this
approach, the delta will change as implied volatility changes, even if the
underlying contract remains the same. Consider a trader who owns 40 call
Figure 9-1  Call delta values as volatility changes.
In-the-money call
100
50
0
Out-of-the-money call
At-the-money call
Lower volatility
Higher volatility
Delta
--- page 154 ---

R i s k M e a s u r e m e n t I I 	 137
options with an implied volatility of 32 percent and a corresponding implied
delta of 25 each. Because 40 × 25 = 1,000, to hedge the position delta neutral, the trader will sell 10 underlying contracts. If, however, implied volatility rises to 36 percent, the delta of the options will tend toward 50. If the new
implied delta is 30, the trader’s delta position is now (40 × 30) – (10 × 100) =
+200. The trader’s position changed from neutral to bullish even though no
other market conditions changed.
Because the delta depends on the volatility, but volatility is an unknown
factor, calculation of the delta can pose a major problem for a trader, especially
for a large option position. Using the implied volatility to calculate the delta is
only one possible approach.
Figure 9-2 shows what happens to call deltas as time passes. Note the
similarities to Figure 9-1. Delta values move toward 50 if we increase either
time to expiration or volatility and move away from 50 if we reduce either
of these inputs. In many situations, time and volatility will have a similar
effect on options. More time, like higher volatility, increases the likelihood
of large price changes. Less time, like lower volatility, reduces the likelihood
of large price changes. If a trader cannot immediately determine the effect
on an option’s value or sensitivity of changing time, he might instead consider the effect of changing volatility. Conversely, if he cannot determine the
effect of changing volatility, he might consider the effect of changing time.
Both effects are likely to be similar.
Figure 9-2  Call delta values as time passes.
100
50
0
In-the-money call
At-the-money call
Out-of-the-money call
Less time to expiration
More time to expiration
Delta
--- page 155 ---

138
O P T I O N V O L AT I L I T Y A N D P R I C I N G
Figure 9-3  Put delta values as volatility changes.
0
–50
–100
Out-of-the-money put
At-the-money call
In-the-money call
Lower volatility
Higher volatility
Delta
Figure 9-4  Put delta values as time passes.
0
–50
–100
At-the-money put
In-the-money put
Out-of-the-money put
Less time to expiration
More time to expiration
Delta
The effects of volatility and time on put deltas are the same as those on call
deltas, except that put deltas tend toward 0 and –100 as volatility falls or time
passes and toward –50 as volatility rises. This is shown in Figures 9-3 and 9-4.
--- page 156 ---

R i s k M e a s u r e m e n t I I 	 139
An alternative method of displaying the effects of changing time and volatility on delta values is shown in Figure 9-5. This is similar to Figure 7-6 except
that we have varied time and volatility. As we lower time or reduce volatility,
delta values for calls move very quickly toward either 0 for out-of-the-money
options or 100 for in-the-money options.
Because delta values are affected by the passage of time, a position that is
delta neutral today may not be delta neutral tomorrow, even if all other market conditions remain unchanged. Of course, with many months remaining to
expiration, the passage of even several days may have little effect on the delta.
If, however, expiration is quickly approaching, the passage of just one day,
because it represents a large portion of the option’s remaining life, can have a
dramatic effect on the delta.
As option traders have become more aware of the importance of risk management, they have begun to pay closer attention to changes in the sensitivities
themselves as market conditions change. In some cases, they have also begun
to attach names (although not necessarily Greek letters) to these higher-order
sensitivities. The sensitivity of the delta to a change in volatility is sometimes
referred to as the option’s vanna. The sensitivity of the delta to the passage of
time is sometimes referred to as the option’s delta decay or its charm.1
Which delta values are the most sensitive to changes in volatility (vanna)
and time (charm)? We know that delta values will tend either toward 50 as
1 In mathematics, the “sensitivity of a sensitivity” is a second-order sensitivity. The gamma, vanna, and charm
are all second-order sensitivities (the sensitivity of the delta to a change in underlying price, volatility, and time
to expiration, respectively).
Figure 9-5  Call delta values as time passes or volatility declines.
100
50
0
Lower underlying prices
Higher underlying prices
Exercise
price
Delta
--- page 157 ---

140
O P T I O N V O L AT I L I T Y A N D P R I C I N G
we increase volatility or time, or away from 50 (toward 0 or 100) as we reduce
volatility or time. Logically, delta values that are already close to 0, 50, or 100
are the least likely to change. At the same time, delta values that are approximately midway between these numbers are most likely to change. This is borne
out by Figures 9-6 and 9-7, the vanna and charm for options with different
deltas. Note that the shapes of the graphs are identical for calls and puts, with
the vanna and charm approximately 0 around a delta of 50 or –50.2 We can
also see that vanna and charm are greatest for call delta values close to 20 and
80 and put delta values close to –20 and –80. Options with these deltas will
move the most quickly toward 50 if we raise volatility or away from 50 if we
lower volatility or reduce time to expiration.
The three vanna graphs also show that the vanna moves in the opposite direction of volatility, falling as we raise volatility and rising as we reduce volatility. The
graphs of the charm exhibit similar characteristics with respect to the passage of
time, falling with more time to expiration and rising with less time to expiration.
In Figures 9-6 and 9-7, we have ignored the effect of changing time on
the vanna and the effect of changing volatility on the charm. From previous
discussions, we might expect time and volatility to have the same effect on
both these values. However, whereas vanna values are affected by changes in
volatility, they are not significantly affected by changes in time to expiration.
Whereas charm values are affected by time to expiration, they are not significantly affected by changes in volatility.
2 The vanna is actually 0 for delta values slightly larger than 50 and smaller than –50. This is due to the nonsymmetrical characteristic of the lognormal distribution.
Figure 9-6  Vanna of an option.
Put deltas
Call deltas
0
50
100
–50
–100
Lower volatility
Higher volatility
Vanna–sensitivity of the delta to a change in volatility
Lower volatility
Higher volatility
0
--- page 158 ---

R i s k M e a s u r e m e n t I I 	 141
Theta
The theta of an option, the rate at which it decays, will vary depending not
only on market conditions but also on whether an option is in the money, at
the money, or out of the money. In Figure 9-8, we can see that the theta of an
option is greatest when it is at the money. As the option moves either into or out
of the money, its theta declines. Because the theta of an option is a function of
its time value, and because very deeply in the money options and very far out of
the money options have very little time value, it is logical that such options have a
very low theta.
Note also that when all other conditions are the same, an at-the-money
option at a higher underlying price has a greater theta value than an at-themoney option with lower underlying price. To understand why, consider two
calls, one with an exercise price of 10 and one with an exercise price of 1,000,
where both options are at the money and both calls have the same amount
of time to expiration and the same implied volatility. Which option will be
worth more? Clearly, the 1,000 call will be worth more because it represents the
right to buy a more valuable asset.3 Because both options are at the money and
therefore consist solely of time value, the theta of the 1,000 call must be greater
than the theta of the 10 call.
3 In fact, the theoretical value and theta of two otherwise identical at-the-money options are proportional to
their exercise prices. In this example, the 1,000 call will be worth exactly 100 times more than the 10 call, and
its theta will be exactly 100 times greater.
Figure 9-7  Charm of an option.
Put deltas
Call deltas
0
50
100
–50
–100
Charm – sensitivity of the delta to a change in time
Less time
to expiration
Less time
to expiration
More time
to expiration
0
More time
to expiration
--- page 159 ---

142
O P T I O N V O L AT I L I T Y A N D P R I C I N G
Figure 9-8  Theta of an option as the underlying price changes.
Lower underlying prices
Lower
exercise price
Intermediate
exercise price
Higher
exercise price
Higher underlying prices
*Although it is common to express theta as a negative number, the theta values
in Figures 9-8, 9-10, and 9-11 are expressed in terms of absolute value.
Theta*
Figure 9-9 shows the theoretical value of an in-the-money, at-themoney, and out-of-the-money option as time passes. Early in the option’s
life, the rate of decay (the slope of the theoretical-value graph) is similar for
each option. But late in the option’s life, as expiration approaches, the rate
of decay slows for in-the-money and out-of-the-money options, whereas it
accelerates for an at-the-money option, approaching infinity at the moment
of expiration. These characteristics, which apply to both calls and puts, are
shown in Figure 9-10.4
The effect on the theta of changing volatility is shown in Figure 9-11. If
we ignore interest, with a 0 volatility, the theta of any option will be 0. As we
increase volatility, we increase the time premium, at the same time increasing the theta.
Note that the graph of the at-the-money option is essentially a straight line,
with the theta being directly proportional to the volatility. For an at-the-money
option, the theta at a volatility of 20 percent is exactly double the theta at a volatility of 10 percent. The same is not necessarily true for higher exercise prices
(out-of-the-money calls and in-the-money puts) or lower exercise prices (in-themoney calls and out-of-the-money puts). The theta tends to decline as volatility
declines but may become 0 well before the volatility is 0.
4 The theta values for in-the-money and out-of-the-money options are actually slightly different. However, the
values are so close that in Figure 9-10 we use one line to represent both options.
--- page 160 ---

R i s k M e a s u r e m e n t I I 	 143
Figure 9-9  Theoretical value of an option as time passes.
Time to expiration
(Expiration)
0
In the money
At the money
% out of the money
Option value
Figure 9-10  Theta of an option as time passes.
Time to expiration
At the money
In the money
or
out of the money
(Expiration)
0
Theta
--- page 161 ---

144
O P T I O N V O L AT I L I T Y A N D P R I C I N G
Figure 9-11 was constructed with the higher and lower exercise prices
equally far away from the current underlying price. Note that the higher exercise price has a greater theta than the lower exercise price, with the difference
increasing with increasing volatility. We touched on the explanation for this
in Chapter 6. If a call and a put are both equally out of the money, under the
assumptions of a lognormal distribution, the out-of-the-money call (the higher
exercise price) will carry greater time premium than the out-of-the-money put
(the lower exercise price). If there is no movement in the price of the underlying contract, the option with more time premium (the higher exercise price)
must necessarily decay more quickly than the option with less time premium
(the lower exercise price).
If we know the value of an option today, is there any way to estimate the
option’s theta? There is no convenient method for estimating the theta of
in-the-money and out-of-the-money options, but for an at-the-money option,
we know that theta is directly proportional to volatility (Figure 9-11). We also
know from Chapter 6 that volatility is proportional to the square root of time
t
volatility
volatility
t
annual
=
×
The theta of an at-the-money option must therefore be proportional to the
square root of time. If TVt is an option’s theoretical value at time t (in days to
expiration), then the theoretical value one day later TVt–1 is
TV
TV
t
t
(
1)/
t
t
1 =
×
−
−
Figure 9-11  Theta of an option as volatility changes.
At the money
Higher
exercise price
Lower
exercise price
Theta
Lower volatility
Higher volatility
--- page 162 ---

R i s k M e a s u r e m e n t I I 	 145
The theta is therefore
TV
TV
t
t
TV
t
t
(
1)/
1
(
1)/
t
t
t
−
×
−
=
×
−
−


As time passes, the value of
t
t
1
(
1)/
−
−
 becomes increasingly large. Consequently, the theta of an at-the-money option will also become increasingly
large (Figure 9-7).
For example, consider an at-the-money option with a theoretical value
of 2.50 and 30 days remaining to expiration. The option’s theta will be
approximately
2.50
1
29/30
2.50
(1
0.9832)
0.042
(
)
×
−
=
×
−
≈
One day later, with 29 days remaining to expiration, the theta will be
(2.50
0.042)
1
28/29
2.458
(1
0.9826)
0.043
(
)
−
×
−
=
×
−
≈
Vega
Figure 9-12 shows the vega of an option as we change the underlying price.
Note that this figure is almost identical to Figure 9-8. As with the theta, the vega
is greatest when an option is at the money, and an at-the-money option with
Figure 9-12  Vega of an option as the underlying price changes.
Vega
Lower underlying prices
Lower
exercise price
Intermediate
exercise price
Higher
exercise price
Higher underlying prices
--- page 163 ---

146
O P T I O N V O L AT I L I T Y A N D P R I C I N G
a higher exercise price has a greater vega than an at-the-money option with a
lower exercise price. Moreover, the vega of an at-the-money option is proportional to its exercise price. Assuming that all other conditions are the same, an
at-the-money option with an exercise price of 100 will have a vega that is twice
that of an option with an exercise price of 50. Note that the term vanna, which
previously referred to the sensitivity of delta to a change in volatility, can also
refer to the sensitivity of the vega to a change in the underlying price. Both
interpretations are mathematically identical.
Figure 9-13 shows the theoretical value of an in-the-money, at-the-money,
and out-of-the-money option as we change volatility. Of particular note is the
fact that the value of an at-the-money option is essentially a straight line. Because the vega is the slope of the graph, we can conclude that the vega of an
at-the-money option is relatively constant with respect to changes in volatility.
Whether volatility is 20 percent, 30 percent, or some higher value, the vega of
an at-the-money option will be the same.
The effect on the vega of changing volatility is shown in Figure 9-14.
While the vega of the at-the-money option is relatively constant, the vega values of in-the-money and out-of-the-money options tend to rise with higher
volatility.5 This is logical when we recall that as we raise volatility, the deltas
of in-the-money and out-of-the-money options tend toward 50, causing the
options to act more and more as if they are at the money. Because at-themoney options have the greatest vega (see Figure 9-12), we would expect the
5 In fact, we can see from Figure 9-14 that the vega of an at-the-money option declines very slightly as we raise
volatility. This will be discussed in greater detail in Chapter 18.
Figure 9-13  Theoretical value of an option as volatility changes.
Option value
Lower volatility
Higher volatility
In the money
Out of the money
At the money
--- page 164 ---

R i s k M e a s u r e m e n t I I 	 147
vega values to rise. The sensitivity of vega to a change in volatility is sometimes referred to as either the volga or the vomma (both terms are a contraction
of volatility and gamma—either volatility gamma or volatility gamma).
Figure 9-15 shows volga values for calls and puts with varying deltas. We
have already noted that an at-the-money option with a delta of approximately
50 has a relatively constant vega and, consequently, a volga close to 0. However, as an option moves either into the money or out of the money, the volga
begins to increase, reaching its maximum for calls with deltas of approximately
10 and 90 and puts with deltas of approximately –10 and –90. Additionally, as
we increase time, volga values for in-the-money and out-of-the-money options
become more sensitive to the passage of time, with long-term options having
greater volga values than short-term options.
In Figure 9-16, we can see how vega values change as time changes,
rising as we increase time to expiration and falling as we reduce time. This
characteristic, that long-term options are always more sensitive to changes
in volatility than short-term options, was introduced in Chapter 6 (see
Figures 6-11 and 6-12).
The sensitivity of the vega to changes in time to expiration, sometimes
referred to as either vega decay or DvegaDtime, is shown in Figure 9-17. The vega
of options with delta values between 10 and 90 tends to be the most sensitive to
the passage of time. This sensitivity increases as we reduce time to expiration;
as time passes, the vega of short-term options will change more quickly than
the vega of long-term options.
Figure 9-14  Vega of an option as volatility changes.
Vega
Lower volatility
Higher volatility
At the money
Higher
exercise price
Lower
exercise price
--- page 165 ---

148
O P T I O N V O L AT I L I T Y A N D P R I C I N G
Figure 9-15  Volga (vomma) of an option.
Put deltas
Call deltas
0
50
100
–50
–100
Volga–sensitivity of the vega to a change in volatility
More time
to expiration
Less time
to expiration
0
Figure 9-16  Vega of an option as time passes.
Time to expiration
(Expiration)
0
Vega
At the money
Higher
exercise price
Lower
exercise price
--- page 166 ---

R i s k M e a s u r e m e n t I I 	 149
Gamma
The gamma measures the sensitivity of the delta to a change in the underlying
price. But the gamma itself is sensitive to changes in market conditions.6
In Figure 9-18, we can see that the gamma is greatest when an option is
at the money. This is similar to theta and vega, which are also greatest when
an option is at the money, and leads to an important principle of option trading: gamma, theta, and vega are greatest when an option is at the money. Because of this,
at-the-money options tend to be the most actively traded in most option markets. Such options have the characteristics that traders are looking for when
they go into an option market.
Unlike the theta and vega of at-the-money options, which increase at
higher exercise prices, the gamma of an at-the-money option declines at higher
exercise prices. To understand why, recall that the gamma is the change in
the delta per one-point change in the underlying price. But theoretical pricing models measure change in percentage terms. By this measure, a one-point
price change with the underlying at 50 (a 2 percent change) is greater than
6 Because the gamma is a second-order sensitivity—the sensitivity of the delta to a change in the underlying
price—the sensitivity of gamma to a change in market conditions is a third-order sensitivity. For a discussion
of some of the higher-order sensitivities, see Espen Gaarder Haug, The Complete Guide to Option Pricing Formulas
(New York: McGraw-Hill, 2007); Espen Gaarder Haug, “Know Your Weapon, Part 1,” Wilmott Magazine,
May 2003: 49–57, also available at http://www.wilmott.com/pdfs/050527_haug.pdf; and Espen Gaarder
Haug, “Know Your Weapon, Part 2,” Wilmott Magazine, July–August 2003:50–56, also available at http://www
.nuclearphynance.com/User percent20Files/2552/0307_haug.pdf.
Figure 9-17  Vega decay of an option.
Put deltas
Call deltas
0
50
100
–50
–100
Vega decay–sensitivity of the vega to
the passage of time
Less time
to expiration
More time
to expiration
0
--- page 167 ---

150
O P T I O N V O L AT I L I T Y A N D P R I C I N G
a one-point price change with the underlying at 100 (a 1 percent change).
Although the theta and vega of at-the-money options are proportional to their
exercise prices, the gamma is inversely proportional. The gamma of an option
with an exercise price of 50 will be twice as large as the gamma of an option
with an exercise price of 100.
Because at-the-money options have the greatest gamma, as the underlying price moves toward the exercise price, the gamma of an option will rise,
and as the underlying price moves away from the exercise price, the gamma
will fall. The sensitivity of the gamma to a change in the underlying price,
sometimes referred to as the speed, is shown in Figure 9-19. The speed is greatest for out-of-the-money options with deltas close to 15 for calls and –15
for puts and for in-the-money options with deltas close to 85 for calls and
–85 for puts. As we increase time to expiration or volatility, the speed of an
option declines; as we reduce time to expiration or volatility, the speed rises.
The gamma is least sensitive to changes in the underlying price for at-themoney options (a delta close to 50 for calls or –50 for puts) or for very deeply
in-the-money or very far out-of-the-money options (deltas close to 0 and close
to 100 for calls or –100 for puts).
The gamma will also be sensitive to changes in time to expiration and volatility. This is shown in Figure 9-20. We know that gamma is greatest when an
option is at the money and declines as the option moves either into the money
or out of the money. Of particular importance is the fact that the gamma of an
at-the-money option rises as time passes or as we reduce volatility and falls as
we increase volatility. To see why, consider a 100 call with the market at 97.50.
Figure 9-18  Gamma of an option as the underlying price changes.
Lower
exercise price
Intermediate
exercise price
Higher
exercise price
Gamma
Lower underlying prices
Higher underlying prices
--- page 168 ---

R i s k M e a s u r e m e n t I I 	 151
Because the option is currently out of the money, its delta is less than 50. We
also know that as time passes or we reduce volatility, delta values move away
from 50. If we are close to expiration or in a very low-volatility market, the
delta of the option will be well below 50, perhaps 25. If the underlying market
should then rise 5 points to 102.50, the delta of the option will be greater than
50, perhaps 75. With the underlying market rising from 97.50 to 102.50 and
the delta rising from 25 to 75, the approximate gamma should be
10
75
25
102.50
97.50
50
5
−
−
=
=
If, however, expiration is far in the future or we are in a high-volatility market,
the delta of the 100 call will stay close to 50. With the underlying market at
97.50, the delta of the option may be 45. If the market then rises to 102.50, the
delta may be only 55. The approximate gamma is then
2
55
45
102.50
97.50
50
5
−
−
=
=
The effect is just the opposite for in-the-money and out-of-the-money
options. The gamma will fall if we reduce volatility and rise if we increase
volatility.7 Because gamma and theta are closely related, if we were to graph
7 This is a general rule. Sometimes an option that is only slightly in the money or out of the money will act like an
at-the-money option. Whether an option’s characteristics will resemble those of an at-the-money, in-the-money,
or out-of-the-money option will depend on a variety of factors, including volatility and time to expiration.
Figure 9-19  Speed of an option.
Put deltas
Call deltas
0
50
100
–50
–100
Speed – sensitivity of the gamma to a change
in underlying price
Less time to
expiration or
lower volatility
Less time to
expiration or
lower volatility
More time to
expiration or
higher volatility
More time to
expiration or
higher volatility
0
--- page 169 ---

152
O P T I O N V O L AT I L I T Y A N D P R I C I N G
the gamma of an option as time passes, the result would be very similar to
Figure 9-10, with the gamma instead of the theta along the y-axis.
The sensitivity of the gamma to the passage of time, sometimes referred
to as its color, is shown in Figure 9-21. The color is greatest for at-the-money
calls and puts, with gamma values becoming smaller as we increase time
to expiration and larger as we reduce time (hence a negative color value).
Calls with deltas close to 5 or 95 and puts with deltas close to –5 or –95 also
have large color values. Here, however, an increase in time causes gamma
values to rise, whereas the passage of time causes gamma values to fall
(a positive color). Moreover, reducing time or volatility will increase color
values, making an option’s gamma more sensitive to changes in the passage
of time. Increasing time or volatility will reduce color values, making an
option’s gamma less sensitive to the passage of time. Calls with deltas close to
15 or 85 and puts with deltas close to –15 and –85 tend to have color values
close to 0. The gamma values of such options will be relatively insensitive to
the passage of time.
The sensitivity of an option’s gamma to a change in volatility, sometimes
referred to as its zomma, is shown in Figure 9-22. Zomma characteristics are
similar to color characteristics. The zomma is large for at-the-money calls and
puts, with gamma values becoming smaller as volatility rises and larger as volatility falls (a negative zomma). Calls with deltas close to 5 or 95 and puts with
deltas close to –5 or –95 also have large zomma values. Here, however, an
Figure 9-20  Gamma of an option as time passes or volatility changes.
Lower underlying prices
Higher underlying prices
Exercise
price
Less time to expiration
or lower volatility
More time to expiration
or higher volatility
Gamma
--- page 170 ---

R i s k M e a s u r e m e n t I I 	 153
Figure 9-21  Color of an option.
Put deltas
Call deltas
0
50
100
–50
–100
Color–sensitivity of the gamma to
the passage of time
Less time to
expiration or
lower volatility
More time to
expiration or
higher volatility
Less time to
expiration or
lower volatility
More time to
expiration or
higher volatility
0
Figure 9-22  Zomma of an option.
Put deltas
Call deltas
0
50
100
–50
–100
Zomma–sensitivity of the gamma to a change in volatility
More time to
expiration or
higher volatility
Less time to
expiration or
lower volatility
More time to
expiration or
higher volatility
Less time to
expiration or
lower volatility
0
--- page 171 ---

154
O P T I O N V O L AT I L I T Y A N D P R I C I N G
increase in volatility causes gamma values to rise and a decline in volatility
causes gamma values to fall (a positive zomma). Moreover, reducing time or
volatility will increase the zomma, making an option’s gamma more sensitive to
changes in volatility. Increasing time or volatility will reduce the zomma, making an option’s gamma less sensitive to changes in volatility. Calls with deltas
close to 15 or 85 and puts with deltas close to –15 and –85 tend to have zomma
values close to 0. The gamma values of such options will be relatively insensitive to changes in volatility.
Given the fact that the gamma is greatest for at-the-money options and
that the gamma of an at-the-money option increases as time passes or volatility declines, experienced traders know that at-the-money options close to
expiration in a low-volatility environment are among the riskiest options that
one can trade. Although these gamma options initially have delta values close to
50, their deltas can change dramatically with only small moves in the price of
the underlying contract, moving very quickly toward 0 or 100.
Lambda (Λ)
The delta tells us the point change in an option’s value for a given point
change in the price of the underlying contract. But we might also ask how an
option’s value changes in percentage terms for a given percentage change in
the underlying price.
Consider a call option with a theoretical value of 4.00 and a delta of
20, with the underlying contract trading at a price of 100. If the underlying contract rises one point to 101, the new delta of the option (ignoring the
gamma) should be approximately 4.20. But how much are these changes in
percentage terms? The underlying changed by 1 percent (1/100), whereas
the option changed by 5 percent (0.20/4.00). The option has a lambda, or
elasticity, of 5. In percentage terms, it will change at five times the rate of the
underlying contract.
We can see that the lambda is simply the option’s delta (using the decimal
format) multiplied by the ratio of the underlying price S to the option’s theoretical value
Λ = Δ × (S/TV)
In our example, lambda is
0.20 × 100/4.00 = 5
Traders sometimes refer to the lambda as the option’s leverage value. Although
lambda is not a widely used risk measure, it may still be worth looking at
some basic lambda characteristics. These are shown in Figures 9-23 (call
lambda values) and 9-24 (put lambda values). Logically, because the lambda
is calculated from the delta, calls have positive lambda values and puts have
negative lambda values. We can see that the lambda is greatest for out-ofthe-money options—as the underlying price rises, call lambda values decline
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
