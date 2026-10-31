# Option Volatility and Pricing_ Advanced Trading Strategies -- Sheldon Natenberg -- 2nd ed, 2014 -- McGraw Hill Professional -- isbn13 9780071818773 -- 6a48d008bd9beef283debf7bad0b2e4a -- Anna’s Archive.pdf — pages 324–343

--- page 324 ---

E a r ly E x e r c i s e o f A m e r i c a n   O p t i o n s 	 307
the price of the option is equal to its intrinsic value, the credit and debit will
cancel out, resulting in no cash flow. Because there is no cash flow, there can be
no advantage to early exercise. If, however, the option is subject to stock-type
settlement, as is the practice on futures exchanges in the United States, there
is no cash flow when the option position disappears. The only cash flow is the
variation credit on the futures position, a credit on which we can earn interest.
For a futures option to be an early exercise candidate, the option must be
subject to stock-type settlement, and the interest that can be earned on the intrinsic value must be greater than the volatility value that we are giving up
Interest value > volatility value
The interest on the option’s intrinsic value is either
(F – X) × r × t
for calls or
(X – F) × r × t
for puts.
As with stock options, we can estimate the volatility value of an option by
looking at the price of the companion out-of-the-money option. Suppose that
we have the following:

Futures price = 100

Time to expiration = 3 months

Interest rate = 8.00 percent
Is the 80 call an early exercise candidate if the price of the 80 put is 0.15?
The interest we can earn through early exercise is
(100 – 80) × 0.08 × 3/12 = 0.40
Because this is greater than the volatility value of .15, the option is an early exercise candidate. If given the choice between exercising now and holding the
position to expiration, we will come out ahead by 0.25 if we exercise now. For
the option to be an immediate early exercise candidate, it must also meet the
early exercise criteria over the next day. One day’s worth of interest must be
greater than one day’s worth of volatility value.
We can easily calculate one day’s worth of interest
(100 – 80) × .08/365 = 0.0044
How can we calculate one day’s worth of volatility value? We know that the
price of the companion option, in this case, the 80 put, is almost all volatility
value. As each day passes, the value of the option will fall by one day’s worth
of volatility value. This daily loss in value is simply the option’s theta. By determining the theta of the companion out-of-the-money option, we can estimate
one day’s worth of volatility value. Unlike the other calculations, this will require the use of a theoretical pricing model.
--- page 325 ---

308
O P T I O N V O L AT I L I T Y A N D P R I C I N G
Using the Black-Scholes model, we find that the implied volatility of the
80 put is 24.68 percent. At this implied volatility, the option’s theta is –0.0046,
slightly greater (in absolute value) than the daily interest. If we exercise the 80
call today instead of tomorrow, we will gain 0.0044 in interest, but we will lose
0.0046 in volatility value. Because we will lose more than we gain, the option is
not an immediate early exercise candidate.
When should we exercise the 80 call? Assuming that the early exercise criteria are met over the entire life of the option, we will want to exercise when the
daily volatility value is less than the daily interest. In our example, we will want
to exercise when the option’s theta is less than .0044. Using the Black-Scholes
model, we can estimate that this will occur in four days, at which time the theta
of the 80 put will be –0.0043.4
Not exercising an option to retain the theta value may seem counterintuitive. If we do not exercise the 80 call and the price of the futures contract does not move, we not only lose one day’s worth of interest, but we
also lose one day’s worth of theta. But this is true only if the price of the
futures contract does not move. If the futures contract does move, the fact
that we have a positive gamma position will work in our favor. If the movement is large enough, we will prefer to hold the option position rather than
a futures position. In an extreme case, if the futures contract were to fall
below 80, we would clearly prefer the option position because of the protective value offered by the 80 call. How likely is it that we will get sufficient
movement in the futures price over the next day to justify holding the 80
call rather than exercising it? This is one day’s worth of volatility value—
the theta of the 80 put.
For an American option that might be an early exercise candidate, we have
considered two choices—hold the option or exercise the option. There is also
a third choice—sell the option and replace it with a position in the underlying
contract. The result is equivalent to exercising the option because both strategies result in the option position being replaced by an underlying position.
When does selling an option rather than exercising make sense? When we
decide to exercise an American option prior to expiration, we have, in effect,
concluded that the value of the option is equal to its intrinsic value. If the price
of the option in the marketplace is exactly  intrinsic value, there is no difference
between exercising the option or selling the option and replacing it with an underlying position. If, however, the option is trading at a price greater than  intrinsic value, and transaction costs are not a factor, the best choice will always
be to sell the option and replace it with a position in the underlying contract.
As a practical matter, however, selling an option that is an early exercise candidate will usually not be a viable alternative. If the option is deeply enough in
the money to justify early exercise, the market for the option will be relatively
illiquid. Under these conditions, the bid-ask spread is likely to be so wide that
any sale will almost certainly have to be done at a price that is no greater than
intrinsic value.
4 The term fugit is sometimes used to refer to the number of days remaining until an option becomes an immediate early exercise candidate.
--- page 326 ---

E a r ly E x e r c i s e o f A m e r i c a n   O p t i o n s 	 309
Protective Value and Early Exercise
When we exercise an option prior to expiration, we are giving up the protective
value afforded by the option’s exercise price. If the price of the underlying contract were to fall through the exercise price in the case of a call or rise through
the exercise price in the case of a put, we would always prefer the option position to an underlying position. To better understand the consequences of giving up this protective value, let’s go back to an earlier stock option example, but
with the dividend payable tomorrow:

Stock price = 100

Time to expiration = 1 month

Interest rate = 6.00 percent

Dividend = 0.75, payable tomorrow
If the 90 put is trading at 0.20, we know that the 90 call is an immediate early
exercise candidate because
Dividend value > volatility value + interest value
.75 > 0.20 + .45 = .65
If we exercise the 90 call, the result is that we will have no option position, but
we will have a long position in the underlying stock. This is the same position
that would result had we sold the option and bought the stock. However, if we
sell a call and buy the underlying, this is synthetically equivalent to selling a
put. In a sense, exercising the 90 call is the same as selling the 90 put. What will
cause us to regret selling the 90 put? Whether we sell the 90 put or exercise the
90 call early, in both cases, we will regret our choice if the stock price is below
90 at expiration.
If exercising the 90 call is the same as selling the 90 put, we might ask, if
we exercise the 90 call, at what price are we selling the 90 put? Because
.75 > 0.20 + 0.45 = 0.65
we can see that we will gain .10 by exercising the 90 call. This must mean that we
have sold the 90 put at a price that is .10 better than its market price of 0.20. Therefore, exercising the 90 call is equivalent to selling the 90 put at a price of 0.30.
How can a trader who believes that early exercise is indicated protect himself from the possibility of the underlying contract going through the exercise
price? The solution is simple: at the same time the trader exercises an option,
he can purchase the companion out-of-the-money option. In our example, if
the trader exercises the 90 call and simultaneously buys the 90 put at a price
of 0.20, he will have the same protection afforded by the 90 call, but at a cost
that is 0.10 lower. Whether the trader actually chooses to purchase the 90 put
is a decision that he will have to make based on his assessment of market conditions. If the trader believes that implied volatility is low, a price of 0.20 will
seem cheap, and he ought to be happy to purchase the 90 put. If implied volatility is high, a price of 0.20 will seem expensive, and the trader will look for
some other way of controlling his downside risk.
--- page 327 ---

310
O P T I O N V O L AT I L I T Y A N D P R I C I N G
Pricing of American Options
Our discussion thus far has focused on why and when an American option
might be exercised prior to expiration. But we also want to consider the question
of pricing. How much is an American option worth? Unless interest rates are 0
and there are no dividend considerations, an American option should always be
worth more than an equivalent European option. But how much more?
The Black-Scholes model makes no attempt to evaluate American options
because it is a European pricing model. When the Chicago Board Options Exchange opened in 1973, the first listed stock options were American. In spite of
this, traders continued to use the Black-Scholes model for several years because no
model of equal simplicity existed for American options. Traders tried to approximate American values by making adjustments to Black-Scholes–generated values.
For example, when a stock is expected to pay a dividend, an American call
value can be approximated by comparing the Black-Scholes value of the call
option under two circumstances:
1.	 The call expires the day before the stock goes ex-dividend.
2.	 The call expires on its customary date, but the underlying stock price
used to evaluate the call is the current price less the expected dividend.
Whichever value is greater is the pseudo-American call value.
In the case of options on futures or put options on stock, traders used
Black-Scholes–generated values but raised any option with a theoretical value
less than parity to exactly parity. Unfortunately, neither of these methods resulted in a truly accurate value for an American option.
The first widely used model to evaluate American options was introduced
in 1979 by John Cox of the Massachusetts Institute of Technology, Stephen
Ross of Yale University, and Mark Rubinstein of the University of California at Berkeley.5 Unlike the Black-Scholes model, which is closed form and
therefore returns a single option value, the Cox-Ross-Rubinstein, or binomial, model
is an algorithm or loop. The more times the model passes through the loop,
the closer it comes to the true value of an American option. The Cox-Ross-
Rubinstein model is relatively easy to understand, both intuitively and mathematically, and is the most common method by which students are introduced
to option pricing theory. (We will take a closer look at binomial option pricing
in Chapter 19.) However, in terms of computation, the model may require
numerous passes through the loop to generate an acceptable value. In an effort to reduce the computational time required by the Cox-Ross-Rubinstein
model, in 1987, Giovanni Barone-Adesi of the University of Alberta and Robert Whaley of Duke University introduced an alternative model for pricing
American options.6 Although the Barone-Adesi-Whaley, or quadratic, model is more
5 John C. Cox, Stephen A. Ross, and Mark Rubinstein, “Option Pricing: A Simplified Approach,” Journal of
Financial Economics 7:229–263, 1979.
6 Giovanni Baron-Adesi and Robert Whaley, “Efficient Analytic Approximation of American Option Values,”
Journal of Finance 42(2):301–320, 1987.
--- page 328 ---

E a r ly E x e r c i s e o f A m e r i c a n   O p t i o n s 	 311
complex mathematically, it converges to an acceptable value for American options much more quickly than the Cox-Ross-Rubinstein model. The Barone-
Adesi-Whaley model has the limitation of treating all cash flows as if they were
interest payments that accumulate at a constant rate. Dividends, however, are
paid all in one lump sum, and for this reason, the Cox-Ross-Rubinstein model
is more often used to evaluate options on dividend-paying stocks.
In addition to generating values for American options, both the Cox-Ross-Rubinstein and Barone-Adesi-Whaley models specify when early exercise of an American option is optimal. Although we were somewhat subjective on this point in our
earlier discussion, using a true American pricing model, an option is optimally exercised early when its theoretical value is exactly to parity and its delta is exactly 100.
The extent to which American and European option values differ depends
on many factors, including time to expiration, volatility, interest rates, and, in
the case of stock options, the amount of the dividend. The likelihood of early
exercise will increase, and with it the difference between American and European values, as the option goes more deeply into the money. We can see this in
Figure 16-8, the value of a 90 call on stock where

Time to expiration = 7 weeks

Interest rate = 6.00 percent

Dividend = 1.00, payable in 4 weeks

Volatility = 25 percent
As the underlying stock price rises from 90 to 110, the call moves from out of
the money, with a very small likelihood of early exercise, to in the money, with
Figure 16-8  Theoretical value of a 90 call.
Underlying stock price
Call value
4
6
8
10
12
14
16
18
20
22
90
92
94
96
98
100
102
104
106
108
110
European value
American value
Time to expiration = 7 weeks
Interest rate = 6.00%
Dividend = 1.00, payable in 4 weeks
Volatility = 25%
--- page 329 ---

312
O P T I O N V O L AT I L I T Y A N D P R I C I N G
a very high likelihood. Figure 16-9 shows the net difference in values not only
at a volatility of 25 percent but also at volatilities of 15 and 35 percent. At a
higher volatility, the difference in values is smaller because the American call is
less likely to be exercised early. At a lower volatility, the difference is greater because the call is more likely to be exercised early. In all cases, as the option goes
more deeply into the money, the difference approaches 0.67, the amount of the
dividend less the interest cost of purchasing the stock at 90 the day before the
dividend is paid and carrying the position to expiration
1.00 – (90 × 0.06 × 22/365) ≈ 0.67
Now consider the value of a 110 put under the same conditions. As with a
call, the more deeply the put goes into the money, the greater the difference between the American value and the European value. This can be seen in Figure
16-10. The net difference under three volatility assumptions is shown in Figure 16-11. At a higher volatility, the difference in values is smaller because the
American put is less likely to be exercised early. At a lower volatility, the difference is greater because the put is more likely to be exercised early. In all cases,
as the option goes more deeply into the money, the difference approaches 0.38,
the amount of interest that can be earned on the exercise price for the three
weeks remaining to expiration following payment of the dividend
110 × 0.06 × 21/365 ≈ 0.38
Figure 16-9  Difference between the theoretical value of an American and European 90 call
(American value less European value).
Difference
.50
.40
.30
.20
.10
0
.60
.70
Underlying stock price
90
92
94
96
98
100
102
104
106
108
110
Volatility = 25%
Volatility = 15%
Volatility = 35%
Time to expiration = 7 weeks
Interest rate = 6.00%
Dividend = 1.00, payable in 4 weeks
--- page 330 ---

E a r ly E x e r c i s e o f A m e r i c a n   O p t i o n s 	 313
Figure 16-10  Theoretical value of a 110 put.
Underlying stock price
Put value
4
6
8
10
12
14
16
18
20
22
90
92
94
96
98
100
102
104
106
108
110
European value
Time to expiration = 7 weeks
Interest rate = 6.00%
Dividend = 1.00, payable in 4 weeks
Volatility = 25%
American value
Figure 16-11  Difference between the theoretical value of an American and European 110
put (American value less European value).
Difference
.10
.20
.30
.40
0
Underlying stock price
90
92
94
96
98
100
102
104
106
108
110
Time to expiration = 7 weeks
Interest rate = 6.00%
Dividend = 1.00, payable in 4 weeks
Volatility = 25%
Volatility = 15%
Volatility = 35%
--- page 331 ---

314
O P T I O N V O L AT I L I T Y A N D P R I C I N G
In our discussion of synthetics, we noted that for European stock options,
the delta values of a call and put with the same exercise price and expiration
date always add up to 100. But, for American options, the deltas can add up
to more than 100. This is because the delta of an in-the-money American option goes to 100 more quickly than an equivalent European option. At the same
time, the companion out-of-the-money option still retains some delta value. As
a result, if we calculate the delta of the synthetic underlying (long call and short
put) by adding the American call delta and subtracting the American put delta,
we find that the deltas add up to more than 100. Figure 16-12 shows the American delta values for the 100 synthetic under the same conditions as in our preceding example:

Time to expiration = 7 weeks

Interest rate = 6.00 percent

Dividend = 1.00, payable in 4 weeks

Volatility = 25 percent
Higher volatility tends to reduce the differences between American and European options, so the delta of the synthetic will remain closer to 100.
Because delta values are affected by the likelihood of early exercise, arbitrage strategies such as conversions and reversals, boxes, and rolls, which may
be delta neutral if all options are European, may not be delta neutral if the options are American. Although these strategies may deviate from delta neutral
Figure 16-12  Delta of the 100 synthetic (100 call delta – 100 put delta) if all options are American.
Delta
101
102
103
104
105
106
100
Underlying stock price
105
100
95
90
85
80
110
115
120
Time to expiration = 7 weeks
Interest rate = 6.00%
Dividend = 1.00, payable in 4 weeks
Volatility = 25%
Volatility = 15%
Volatility = 35%
--- page 332 ---

E a r ly E x e r c i s e o f A m e r i c a n   O p t i o n s 	 315
only by a small amount, the fact that they are often done in large sizes can result
in additional risk that a trader should not ignore.
An American pricing model is necessary to evaluate individual American
options, but it may still be possible to estimate the value of some strategies without the use of a pricing model. For example, suppose we know the following:

Time to expiration = 24 days

Interest rate = 6.00 percent

Dividend = 0.60, payable in 9 days
What should be the value of a 100/110 box if all options are American? To answer this question, we can first evaluate an equivalent European box. Then we
can adjust the box value depending on which options might be exercised early.
The value of the European box is simply the present value of the amount
between exercise prices
−
+
×
≈
110
100
1
0.06
24/265
9.96
Now we can consider the various possibilities for early exercise:

Case 1: Both the 100 and 110 put are exercised early. The puts will be exercised the day the dividend is paid. The box value will increase by the
interest earned on 10.00 for 15 days

9.96 + (10 × 0.06 × 15/365) = 9.96 + 0.025 = 9.985

Case 2: Both the 100 and 110 call are exercised early. The calls will be exercised the day before the dividend is paid. The box value will increase
by the interest earned on 10.00 for 16 days

9.96 + (10 × 0.06 × 16/365) = 9.96 +  0.026 = 9.986

Case 3: Only the 110 put is exercised early. The box value will increase by
the interest earned on 110 for 15 days

9.96 + (110 × 0.06 × 15/365) = 9.96 + 0.271 = 10.231

Case 4: Only the 100 call is exercised early. The box value will increase by
the amount of the dividend less the interest cost on 100 for 16 days

9.96 + 0.60 – (100 × 0.06 × 16/365) = 9.96 + 0.60 – 0.263 = 10.297

Case 5: Both the 100 call and 110 put are exercised early. The box value will
increase by the amount of the dividend plus the interest earned on
110 for 15 days less the interest cost on 100 for 16 days
9.96 + 0.60 + (110 × 0.06 × 15/365) – (100 × 0.06 × 16/365)

= 9.96 + 0.60 + 0.271 – 0.263 = 10.568
At very low stock prices, where both puts are early exercise candidates, and
at very high stock prices, where both calls are early exercise candidates, the box
will have a value close to 9.99. If one option, either the 100 call or 110 put, is
--- page 333 ---

316
O P T I O N V O L AT I L I T Y A N D P R I C I N G
an early exercise candidate, the value of the box will be somewhere between
10.23 and 10.30. Finally, the box will have its maximum value of approximately 10.57 if both the 100 call and the 110 put are early exercise candidates.
This will occur if both options are in the money, most likely with the stock price
close to 105. Volatility must also be low because in a high-volatility market,
no one will want to give up an option’s volatility value by exercising early. The
value of the 100/110 box at different stock prices and under three different volatility assumptions is shown in Figure 16-13.
The difference between European and American values is usually greatest for options on dividend-paying stocks. But even futures options, if the options are subject to stock-type settlement, have some additional early exercise
value. We can see this in Figure 16-14, the value of a 90 call on a futures contract, where

Time to expiration = 3 months

Interest rate = 8.00 percent

Volatility = 25 percent
The difference between the European and American option values is shown in
Figure 16-15. Unlike a stock option, where there is a maximum difference, the
difference for options on futures continues to increase as the option goes further
into the money. This is because the early exercise value depends on the interest
that can be earned on the option’s intrinsic value. And the more deeply in the
Figure 16-13  Value of a 100/110 box if all options are American.
Box value
10.00
10.10
10.20
10.30
10.40
10.50
10.60
9.90
Underlying stock price
85
90
95
100
105
110
115
120
125
European value
Volatility = 20%
Volatility = 15%
Volatility = 10%
Time to expiration = 24 days
Interest rate = 6.00%
Dividend = 0.60, payable in 9 days
--- page 334 ---

E a r ly E x e r c i s e o f A m e r i c a n   O p t i o n s 	 317
Figure 16-14  Theoretical value of a 90 call on a futures contract where the option is subject
to stock-type settlement.
Underlying futures price
Call value
8
6
4
10
12
14
16
18
20
110
108
106
104
102
100
98
96
94
92
90
Time to expiration = 3 months
Interest rate = 8.00%
Volatility = 25%
European value
American value
Figure 16-15  Difference between the theoretical value of an American and European 90
call on a futures contract where the options are subject to stock-type settlement (American
value – European value).
Underlying futures price
Time to expiration = 3 months
Interest rate = 8.00%
Difference
.40
.30
.20
.10
0
110
108
106
104
102
100
98
96
94
92
90
Volatility = 25%
Volatility = 15%
Volatility = 35%
--- page 335 ---

318
O P T I O N V O L AT I L I T Y A N D P R I C I N G
money, the greater the intrinsic value. In our example, with the underlying futures contract trading at 110, the additional early exercise value for the 90 call
will approach the interest that can be earned on the intrinsic value
(110 – 90) × 0.08 × 3/12 = 0.40
Regardless of the model a trader chooses, the accuracy of model-generated
values will depend at least as much on the inputs into the model as on the theoretical accuracy of the model itself. If a trader evaluates an American option using an
incorrect volatility, an incorrect interest rate, or an incorrect underlying price, the
fact that he derives his values from an American rather than a European model is
likely to make little difference. Both models will generate incorrect values because
the inputs are incorrect. The American model may produce less error, but that will
be small consolation if the incorrect inputs lead to a large trading loss.
The importance of early exercise is greatest when there is a significant difference between the cost of carrying an option position and the cost of carrying a position in the underlying contract. This difference can be relatively large in the stock
option market, where the cash outlay required to buy stock is much greater than
the cash outlay required to buy options. Moreover, dividend considerations will
also affect the cost of carrying a stock position compared with the cost of carrying an option position. A trader in a stock option market will usually find that the
additional accuracy afforded by an American model will indeed be worthwhile.
In futures options markets, where the options are subject to futures-type
settlement, there is no cost of carry associated with either options or the underlying futures contract. In this case, a European pricing model will suffice because there is no difference between European and American option values.
Even if options on futures are subject to stock-type settlement, there is a relatively small cost associated with carrying an option position because the price
of the option is small compared with the price of the underlying futures contract. The additional value for early exercise is therefore small and is only likely
to be a consideration for very deeply in-the-money options. Practical considerations, such as the accuracy of the trader’s volatility estimate, his ability to anticipate directional trends in the underlying market, and his ability to control
risk through effective spreading strategies, will far outweigh any small advantage gained by using an American rather than a European model.7
Early Exercise Strategies
Early exercise of an option is a right rather than an obligation, and there are
strategies that depend on someone making an error and not exercising an option early when it ought to be exercised. For example, consider this situation:

Stock price = 98.75

Time to expiration = 5 days

Dividend = 1.00, payable tomorrow
7 Early exercise considerations may also be important in a foreign-exchange market if the interest rates associated
with the domestic currency (the currency in which the option is settled) and foreign currency (the currency to be
delivered in the event of exercise) are significantly different.
--- page 336 ---

E a r ly E x e r c i s e o f A m e r i c a n   O p t i o n s 	 319
Suppose that there is a 90 call that is American and ought to be exercised today
in order not to lose the dividend of 1.00. If this is true, the option ought to be
worth approximately parity, or 8.75. Suppose that a trader is able to sell a 90
call for 8.75 and at the same time buy 100 shares of stock for 98.75. Because
the 90 call ought to be exercised today, the trader probably will be assigned, requiring him to sell the stock at 90. If this occurs, excluding transaction costs,
the trader will break even:

Sell the 90 call
  +8.75

Buy stock
–98.75

On assignment, sell stock at 90
+90.00

          0
But suppose that the trader is not assigned on the 90 call. If the stock opens unchanged, its new price will be 97.75 (the stock price of 98.75 less the dividend
of 1.00). Because the call is trading at parity, it will open at approximately 7.75.
The trader will show a loss of 1.00 on the stock and a profit of 1.00 on the 90
call. But the trader, because he owns the stock, will also receive the dividend.
Excluding transaction costs, the profit for the entire position will be equal to the
dividend of 1.00.
In a dividend play, as the ex-dividend day approaches, a trader will try to
sell deeply in-the-money calls and simultaneously buy an equal amount of
stock. If the trader is assigned on the calls, as he should be, he will essentially
break even. But, if he is not assigned, he will show a profit approximately
equal to the amount of the dividend. What is the likelihood of the trader being assigned? Because assignment for most exchange-traded options is random, one determinant is the amount of open interest in the call that was sold.
The more outstanding call options, the lower the likelihood of assignment.
A second determinant is the relative sophistication of the market—whether
most market participants are familiar with the criteria for early exercise. Dividend plays were much more common in the early days of option trading when
the market was less sophisticated and many options that should have been exercised were not. As markets have become more efficient, only a professional
trader with very low transaction costs will try to take advantage of such a possibility. Even then, he may find that he is assigned on the great majority of
calls he has sold.
A trader also might attempt to execute an interest play by selling stock and
simultaneously selling deeply in-the-money American puts that ought to be exercised early. If the puts are not exercised, the trader will profit by the amount
of the interest he can earn on the exercise price (the proceeds of the stock sale
and the put sale combined). This profit will continue to accrue as long as the
puts remain unexercised. If the puts are exercised, the trader does no worse
than break even. Again, only a professional trader, with low transaction costs, is
likely to attempt such a strategy.
If options are subject to stock-type settlement, an interest play can also be
done in a futures option market by either purchasing a futures contract and simultaneously selling a deeply in-the-money call or selling a futures contract
and simultaneously selling a deeply in-the-money put. If the option is deeply
--- page 337 ---

320
O P T I O N V O L AT I L I T Y A N D P R I C I N G
enough in the money, it ought to be exercised early. But, if the option remains
unexercised, the trader will continue to earn interest on the proceeds from the
option sale. Because the amount on which the trader will earn interest is approximately the intrinsic value (the difference between the exercise price and
futures price), this will not be as profitable as a similar strategy in the stock option market where the trader will earn interest on the exercise price. Still, if the
transaction costs are low enough, it may be worthwhile.
Instead of entering into an early exercise strategy by selling options and
trading the underlying contract, a trader may also be able to execute the strategy by trading deeply in-the-money call or put spreads. In our dividend-play
example, the trader sold 90 calls and bought stock. Suppose that both the 85
call and the 90 call ought to be exercised to avoid losing the dividend. If this is
true, the 85/90 call spread ought to be worth 5.00, exactly the difference between exercise prices. One might assume that if requested, a market maker will
quote a bid price for this spread below 5.00, perhaps 4.90, and an ask price for
the spread above 5.00, perhaps 5.10. In fact, a market maker might quote an
identical bid and ask price of 5.00. This may seem illogical, quoting the same
bid and ask price, but consider what will happen if the market maker is able to
either buy or sell the spread at a price of 5.00.
If the market maker buys the spread (i.e., buy the 85 call, sell the 90 call),
he will immediately exercise the 85 call, thereby purchasing stock. He has effectively entered into the same dividend play that we originally described (i.e., short
call, long stock). If he is not assigned on the 90 call, he will again profit by the
amount of the dividend. If, instead, the market maker sells the spread (i.e., sell
the 85 call, buy the 90 call), he will immediately exercise the 90 call. Now he has
executed the dividend play by purchasing stock and selling the 85 call. If he is
not assigned on the 85 call, he will again profit by the amount of the dividend.
The market maker is willing to give up the edge on the bid-ask spread in return
for the potential profit that will result if the short options go unexercised.
Early Exercise Risk
How concerned should a trader be that an option that he has sold will be exercised early? “What will happen if I am suddenly assigned?” Early assignment can sometimes result in a loss. But there are many factors that can cause
a trader to lose money; early exercise is only one such factor. A trader should
be prepared to deal with the possibility of early exercise, just as he should be
prepared to deal with the possibility of movement in the price of the underlying contract or the possibility of changes in implied volatility. Margin requirements established by the clearinghouses often require a trader to keep
sufficient funds in his account to cover the possibility of early assignment. But
this is not always true. If the trader is short deeply in-the-money options, an
early assignment notice may cause a cash squeeze. If this happens, he will
need sufficient capital to cover the situation. Otherwise, he may be forced to
liquidate some or all of the remaining position. And forced liquidations are
invariably losing propositions.
--- page 338 ---

E a r ly E x e r c i s e o f A m e r i c a n   O p t i o n s 	 321
In spite of the risk of early assignment, it should rarely come as a surprise.
A trader need only ask himself, “If I owned this option, would I logically exercise it now?” If the answer is yes then the trader ought to be prepared for assignment. If the answer is no and the trader is still assigned, it is probably good
for the trader. It means that someone has mistakenly abandoned the option’s
interest or volatility value. When that happens, the trader who is assigned will
find that he is the recipient of an unexpected gift.
--- page 339 ---

322
17
Hedging with Options
Futures and options were originally introduced as insurance contracts, enabling
market participants to transfer the risk of holding a position in the underlying
instrument from one party to another. But unlike a futures contract, which
essentially transfers all the risk, an option transfers only part of the risk. In this
respect, an option acts much more like a traditional insurance policy than does
a futures contract.
Even though options were originally intended to function as insurance policies, option markets have evolved to the point where, in most markets, hedgers (those wanting to protect an existing position) make up only a small portion
of market participants. Other traders, including arbitrageurs, speculators, and
spreaders, typically outnumber true hedgers. Nevertheless, hedgers still represent an important force in the marketplace, and any active market participant
ought to be aware of the strategies a hedger might use to protect a position.
Many hedgers come to the marketplace as either natural longs or natural
shorts. Through the course of normal business activity, they will profit from
either a rise or fall in the price of some underlying instrument. The producer
of a commodity is a natural long; if the price of the commodity rises, the producer will receive more when he sells in the marketplace. The user of a commodity is a natural short; if the price of the commodity falls, the user will have
to pay less for it when he buys in the marketplace. In the same way, lenders and
borrowers are natural longs and shorts in terms of interest rates. A rise in interest rates will help lenders and hurt borrowers. A decline in interest rates will
have the opposite effect.
Other potential hedgers come to the marketplace because they have voluntarily chosen to take a long or short position and now wish to lay off part or all
of the risk of that position. A speculator in a commodity may have taken a long
or short position but wishes to temporarily reduce the risk associated with an
outright long or short position. A fund manager may hold a portfolio of stocks
but believes that the value of the portfolio may decline in the short term. If so,
it may be less expensive to temporarily hedge the stocks with options or futures
than to sell the stocks and buy them back at a later date.
--- page 340 ---

H e d g i n g w i t h O p t i o n s 	 323
As with insurance, there is a cost to hedging. The cost may be immediately
apparent in the form of a cash outlay. But the cost may also be more subtle,
either in terms of lost profit opportunity or in terms of additional risk under
some circumstances. Every hedging decision is a tradeoff: what is the hedger
willing to give up under one set of market conditions in return for protection
under a different set of market conditions. A hedger with a long position who
wants to protect his downside will almost certainly have to give up something
on the upside; a hedger with a short position who wants to protect his upside
will have to give up something on the downside.
Protective Calls and Puts
The simplest way to hedge an underlying position using options is to purchase
either a put to protect a long position or a call to protect a short position. In
each case, if the market moves adversely, the hedger is insulated from any loss
beyond the exercise price. The difference between the exercise price and the
current price of the underlying is similar to the deductible portion of an insurance policy. The price of the option is similar to the premium that one has to
pay for the insurance policy.
Consider an American firm that expects to take delivery of €1 million worth
of German goods in six months. If the contract requires payment in euros at the
time of delivery, the American firm has acquired a short position in euros against
U.S. dollars. If over the next six months the euro rises against the dollar, the goods
will cost more in dollars; if the euro falls, the goods will cost less. If the euro is currently trading at 1.35 ($1.35 per euro) and remains there for the next six months,
the cost to the American firm will be $1,350,000. If, however, at delivery the euro
has risen to 1.45 ($1.45 per euro), the cost to the American firm will be $1,450,000.
The American firm can offset the risk it has acquired by purchasing a call
option on euros, for example, a 1.40 call. For a complete hedge, the underlying
contract will be €1 million, and the option will have an expiration date corresponding to the date on which payment is required. If the value of the euro begins to rise against the U.S. dollar, the firm will have to pay a higher price than
expected when it takes delivery of the goods in six months. But the price it will
have to pay for euros can never be greater than 1.40. If the price is greater than
1.40 at expiration, the firm will simply exercise its call, effectively purchasing
euros at 1.40. If the price of euros is less than 1.40 at expiration, the firm will
let the option expire worthless because it will be cheaper to purchase euros in
the open market.
When used to hedge interest-rate risk, protective options are sometimes referred to as caps and floors. A firm that borrows funds at a variable interest rate
has a short interest-rate position—falling interest rates will reduce its cost of borrowing, while rising interest rates will increase its costs. To cap the upside risk, the
firm can purchase an interest-rate call, thereby establishing a maximum amount
it will have to pay for borrowed funds. No matter how high interest rates rise, the
borrower will never have to pay more than the cap’s exercise price.
An institution that lends funds at a variable interest rate has a long interestrate position—rising interest rates will increase its returns, while falling interest
--- page 341 ---

324
O P T I O N V O L AT I L I T Y A N D P R I C I N G
rates will reduce its returns. To set a floor on its downside risk, the institution can
purchase an interest-rate put, thereby establishing a minimum amount it will
receive for loaned funds. No matter how low interest rates fall, the lender will
never receive less than the floor’s exercise price.
A hedger who chooses to purchase a call to protect a short position or a
put to protect a long position has risk limited by the exercise price of the option. At the same time, the hedger still maintains open-ended profit potential.
If the underlying market moves in the hedger’s favor, he can let the option expire and take advantage of the position in the open market. If, in our example,
the euro falls to 1.25 at the time of delivery, the firm will simply let the 1.40
call expire unexercised. At the same time, the firm will purchase €1 million for
$1,250,000, resulting in a windfall of $100,000.
There is a cost involved in buying insurance in the form of a protective call
or put, namely, the price of the option. The cost of the insurance is commensurate with the amount of protection afforded by the option. If the price of a
six-month 1.40 call is 0.02, the firm will pay an extra $20,000 (0.02 × 1 million)
no matter what happens. A call option with a higher exercise price will cost less,
but it also offers less protection in the form of an additional deductible amount.
If the firm chooses to purchase a 1.45 call trading at .01, the cost for this insurance will only be $10,000 (0.01 × 1 million), but the firm will have to bear any
loss up to a euro price of 1.45. Only above 1.45 is the firm fully protected. In
the same way, a lower-exercise-price call will offer additional protection but at
a higher price. A 1.35 call will protect the firm against any rise above 1.35, but
if the price of the call is 0.04, the purchase of this protection will add an additional $40,000 (0.04 × 1 million) to the final cost.
The cost of purchasing a protective option and the insurance afforded by
the strategy are shown in Figures 17-1 (protective put) and 17-2 (protective call).
Figure 17-1  Long an underlying position and long a protective put.
Exercise
price
Long
underlying
Long put
Premium paid for the put
Combined position
(synthetic long call)
Higher underlying prices
Lower underlying prices
Current
underlying
price
--- page 342 ---

H e d g i n g w i t h O p t i o n s 	 325
Because each strategy combines an underlying position with a long option
position, it follows from Chapter 14 that the resulting protected position is a
synthetic long option
Short underlying + long call ≈ synthetic long put
Long underlying + long put ≈ synthetic long call
A hedger who buys a put to protect a long underlying position has effectively
created a long call position at the same exercise price. A hedger who buys a call
to protect a short underlying position has effectively created long put position.
In our example, if the firm purchases a 1.40 call to protect a short euro position, the combined position (i.e., short underlying, long call) is equivalent to
owning a 1.40 put.
Which protective option should a hedger buy? This depends on the amount
of risk the hedger is willing to bear, something that each hedger must determine
individually. One thing is certain: there will always be a cost associated with the
purchase of a protective option. If the insurance afforded by the option enables
the hedger to protect his financial position, the cost may be worthwhile.
Covered Writes
If a hedger is averse to paying for protective options, which offer limited and welldefined risk, the hedger may instead consider selling, or writing, an option against
an underlying position. This covered write (sometimes referred to as an overwrite)
does not offer the limited risk afforded by the purchase of a protective option
Figure 17-2  Short an underlying position and long a protective call.
Exercise
price
Short
underlying
Long call
Premium paid for the call
Combined position
(synthetic long put)
Higher underlying prices
Lower underlying prices
Current
underlying
price
--- page 343 ---

326
O P T I O N V O L AT I L I T Y A N D P R I C I N G
but does have the obvious advantage of creating an immediate cash credit. This
credit offers limited protection against an adverse move in the underlying market.
Consider an investor who owns stock but wants to protect against a shortterm decline in the stock price. He can, of course, buy a protective put. But if
he believes that any decline is likely to be only moderate, he might instead sell a
call option against the long stock position. The amount of protection the investor is seeking, as well as the potential upside appreciation, will determine which
call he sells, whether in the money, at the money, or out of the money. Selling
an in-the-money call offers a high degree of protection but will eliminate most
of the upside profit potential. Selling an out-of-the-money call offers less protection but leaves room for additional upside profit.
Suppose that an investor owns a stock that is currently trading at 100. If he
sells a 95 call at a price of 6.50, the sale of the call will offer a high degree of protection against a decline in the price of the stock. As long as the stock declines by
no more than 6.50 to 93.50, the investor will do no worse than break even. Unfortunately, if the stock begins to rise, there will be no opportunity to participate
in the rising stock price because the stock will be called away when the investor
is assigned on the 95 call. Still, even if the stock rises, the investor will at least
profit by the time premium of 1.50 that he received from the sale of the 95 call.
On the other hand, if the investor wants to participate in upside movement in the stock and is also willing to accept less protection on the downside,
he might sell a 105 call. If the 105 call is trading at a price of 2.00, the sale of
this option will only protect the investor down to a stock price of 98. But, if the
stock price rises, the investor will participate up to a price of 105. Above 105,
he can expect the stock to be called away, eliminating any further profit.
Which option should the investor sell? This is a subjective decision based
on how much risk the investor is willing to accept, as well as the amount of
upside appreciation in which he wants to participate. Many covered writes involve selling at-the-money options. Such options offer less protection than inthe-money calls and less profit potential than out-of-the-money options. But an
at-the-money option has the greatest amount of time premium. If the market
remains close to its current price, a position that is hedged by selling at-themoney options will show the greatest amount of appreciation.
The characteristics of a covered write and the protection afforded by
the strategy are shown in Figures 17-3 (covered call) and 17-4 (covered put).
Because each strategy combines an underlying position with a short option
position, it follows from Chapter 14 that the resulting protected position is a
synthetic short option:
Long underlying + short call ≈ synthetic short put
Short underlying + short put ≈ synthetic short call
A hedger who sells a call against a long underlying position has effectively
created a short put position at the same exercise price. A hedger who sells a
put to protect a short underlying position has effectively created short call put
position. In our example, if the hedger sells a 105 call to protect a long stock
position, the combined position (i.e., long underlying, short call) is equivalent
to selling a 105 put.
