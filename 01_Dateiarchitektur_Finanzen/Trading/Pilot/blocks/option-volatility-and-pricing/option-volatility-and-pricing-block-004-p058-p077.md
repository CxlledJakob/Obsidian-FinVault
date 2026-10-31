# Option Volatility and Pricing_ Advanced Trading Strategies -- Sheldon Natenberg -- 2nd ed, 2014 -- McGraw Hill Professional -- isbn13 9780071818773 -- 6a48d008bd9beef283debf7bad0b2e4a -- Anna’s Archive.pdf — pages 58–77

--- page 58 ---

E x p i r at i o n P r o f i t a n d L o s s
41
The slope of the graph is the change in value of the option position with respect
to changes in the price of the underlying contract, often expressed as a fraction
slope =
change in position value
change in underlying price
We can summarize the slopes of the basic positions as follows:
Position
Slope
Long or short any out-of-the-money option
0
Long an in-the-money call
+1
Short an in-the-money call
–1
Long an in-the-money put
–1
Short an in-the-money put
+1
In addition to parity graphs for individual options, we can also create parity graphs for positions consisting of multiple options by adding up the slopes
of the individual options. Figure 4-5 is the parity graph of a position consisting
of a long call and long put at the same exercise price. We can calculate the total slopes as follows:
Below the exercise price
Slope
Call is out of the money
0
Put is in the money
–1
Total slope below the exercise price
–1
Above the exercise price
Slope
Put is out of the money
0
Call is in the money
+1
Total slope above the exercise price
+1
The combined position will gain value if the underlying price moves in either
direction away from the exercise price. The position is typical of many option
strategies that may be sensitive to the magnitude of movement in the underlying contract rather than the direction of movement.
Many option strategies involve combining options with the underlying
contract, so we will also want to consider the slope of an underlying position.
As shown in Figure 4-6, the slope of a long underlying position is always +1,
and the slope of a short underlying position is always –1. The slopes are constant regardless of the underlying price. This is an important distinction between an option position and an underlying position. Because of the insurance
--- page 59 ---

42
O P T I O N V O L AT I L I T Y A N D P R I C I N G
Figure 4-6  Long and short underlying position.
Position value
0
Higher underlying prices
Lower underlying prices
Long an
underlying contract
Short an
underlying contract
–1
+1
+1
–1
–1
–1
–1
+1
Figure 4-5  (a ) Long call and long put at the same exercise price. (b ) Combined position.
Exercise
price
Higher underlying prices
Lower underlying prices
–1
+1
+1
+1
Long call
Long put
Position value
0
Exercise
price
Higher underlying prices
Lower underlying prices
–1
+1
+1
+1
Long call
Position value
0
(a)
(b)
--- page 60 ---

E x p i r at i o n P r o f i t a n d L o s s
43
feature of an option, the parity graph of an option position will always bend at
the exercise price.
Figure 4-7 shows the parity graph of a position that combines two long
call options at the same exercise price and with a short underlying contract.
Below the exercise price, the total slope is –1 (0 for the out-of-the-money calls,
–1 for the short underlying). Above the exercise price, the total slope is +1 (+2
for the in-the-money calls, –1 for the short underlying contract). This parity
graph is identical to the position in Figure 4-5, which must mean that the same
option strategy can be constructed in more than one way. This is an important characteristic of options that we will look at in more detail in Chapter 14.
Note also that the location of the underlying position is irrelevant to the parity
graph. Regardless of the price of the underlying, the slope is always either +1
for a long underlying position or –1 for a short underlying position.
Figure 4-7  (a ) Long two calls and short an underlying contract. (b ) Combined position.
Higher underlying prices
Exercise
price
Lower underlying prices
+1
+2
+1
–1
Long 2 calls
Short underlying
Position value
0
Higher underlying prices
Lower underlying prices
+1
Exercise
price
+1
–1
+1
Position value
0
(a)
(b)
--- page 61 ---

44
O P T I O N V O L AT I L I T Y A N D P R I C I N G
Figure 4-8 is the parity graph of a long call and short put at the same exercise price. Below the exercise price, the total slope is +1 (0 for the long out-ofthe-money call, +1 for the short in-the-money put). Above the exercise price,
the total slope is also +1 (+1 for the in-the-money call, 0 for the out-of-themoney put). The slope of the entire position is always +1, exactly the same as a
long underlying contract.
If a position consists of many different contracts, including underlying
contracts and calls and puts over a wide range of exercise prices, the parity
graph for the position may be quite complex. But the procedure for constructing the graph is always the same: determine the slopes of the graph below the
lowest exercise price, above the highest exercise price, and between all the intermediate exercise prices, and then connect all the line segments.
Figure 4-8  (a ) Long call and short put at the same exercise price. (b ) Combined position.
Higher underlying prices
Exercise
price
Lower underlying prices
+1
–1
–1
+1
Long call
Short put
Position value
0
(a)
Higher underlying prices
Exercise
price
Lower underlying prices
+1
+1
–1
–1
Position value
0
(b)
--- page 62 ---

E x p i r at i o n P r o f i t a n d L o s s
45
Consider this position:
–4  	underlying contracts
+3  65 calls

+2  65 puts
+2  70 calls

–4  70 puts
–6  75 calls

+3  75 puts
+4  80 calls

–2  80 puts
What should the parity graph look like?
To determine the slopes of a complex position, it may be helpful to construct a table showing the slopes of the individual contracts over all intervals. We
can then add up the individual slopes to get the total slope over each interval.
Contract
Below 65
65–70
70–75
75–80
Above 80
+3  65 calls
0
+3
+3
+3
+3
+2  65 puts
–2
0
0
0
0
+2  70 calls
0
0
+2
+2
+2
–4  70 puts
+4
+4
0
0
0
–6  75 calls
0
0
0
–6
–6
+3  75 puts
–3
–3
–3
0
0
+4  80 calls
0
0
0
0
+4
–2  80 puts
+2
+2
+2
+2
0
–4  Underlying contracts
–4
–4
–4
–4
–4
Total 
–3
+2
0
–3
–1
The entire parity graph is shown in Figure 4-9. Note that for this graph
there is no y-axis. For complex graphs where options are bought and sold at
Figure 4-9 
65
Slope = –3 Slope = +2
70
75
80
Slope = 0 Slope = –3 Slope = –1
–1
–4 underlying contracts
+3 65 calls
+2 65 puts
+2 70 calls
–4 70 puts
–6 75 calls
+3 75 puts
+4 80 calls
–2 80 puts
Position
Below 65
–3
Between 65 and 70
+2
Between 70 and 75
0
Between 75 and 80
–3
Above 80
–1
Slopes
+1
+2
+3
–1
–1
+1
+3
--- page 63 ---

46
O P T I O N V O L AT I L I T Y A N D P R I C I N G
many different exercise prices, it may not be possible to position the graph
along the y-axis. Nevertheless, the parity graph tells us something about the
characteristics of the position. Here we can see that the potential profit on
the downside, as well as the potential loss on the upside, is unlimited.
Expiration Profit and Loss
A parity graph may tell us the characteristics of an option position at expiration, but an equally important consideration will be the profit or loss that
results from the position. Whether the position makes or loses money will depend on the prices at which the contracts are bought and sold. The purchase
of options will create a debit, whereas the sale of options will create a credit.
For a simple option position, the expiration profit and loss (P&L) graph will be
the parity graph shifted downward by the amount of any debit or upward by
the amount of any credit.
Consider the following option prices with the underlying contract trading
at a price of 98.00:
85
90
95
100
105
110
115
Calls
14.25
9.75
6.25
3.50
1.75
0.75
0.25
Puts
0.25
1.00
2.25
4.50
7.75
11.75
16.25
Figure 4-10 shows the parity graph of a long 100 call position. If the
option is purchased at a price of 3.50, we can construct the expiration P&L
Figure 4-10  Long a 100 call at a price of 3.50.
+1
+1
Breakeven
103.50
–3.50
100
Parity graph
Expiration P&L graph
0
Profit or loss at expiration
0
--- page 64 ---

E x p i r at i o n P r o f i t a n d L o s s
47
graph by shifting the entire parity graph down by this amount. If the underlying is anywhere below 100 at expiration, the option will be worthless, and
the position will lose 3.50. With the underlying above 100, the slope of the
graph is +1; the option will gain one point in value for each point increase
in the price of the underlying. We can also see that there is a breakeven price at
which the option position will be worth exactly 3.50. Logically, this must occur at an underlying price of 103.50.
Figure 4-11 shows the parity graph of a short 95 put position. If the option is sold at a price of 2.25, we can construct the expiration P&L graph by
shifting the entire graph up by this amount. With an underlying price anywhere above 95 at expiration, the option will be worthless, and the position
will show a profit of 2.25. With an underlying price below 95, the slope of the
graph is +1; the position will lose one point for each point decline in the price
of the underlying. The breakeven price for the position is 92.75, the price at
which the 95 put will be worth exactly 2.25.
The relative expiration value of long option positions at different exercise
prices—95, 100, and 105—is shown in Figure 4-12. The same relative value
for long put positions is shown in Figure 4-13. Calls with lower exercise prices
have greater values (i.e., they enable the holder to buy at a lower price), whereas
puts with higher exercise prices have greater values (i.e., they enable the holder
to sell at a higher price).
For more complex positions, it may not be immediately clear whether
the position will result in a credit or debit. In this case, we can construct an
expiration P&L graph by first determining the slopes of the graph over all
the intervals. Then we can calculate the P&L at one point, and from this
one P&L point, we can use the slopes to determine the P&L at all other
points.
Figure 4-11  Short a 95 put at a price of 2.25.
Breakeven
92.75
95
+2.25
Parity graph
–1
–1
Expiration P&L graph
Profit or loss at expiration
0
--- page 65 ---

48
O P T I O N V O L AT I L I T Y A N D P R I C I N G
Figure 4-12  Long a 95 call –6.25; long a 100 call –3.50; long a 105 call –1.75.
100
–6.25
95 call
105 call
100 call
Long a 95 Call –6.25
Long a 100 Call –3.50
Long a 105 Call –1.75
95
–1.75
–3.50
105
106.75
103.50
101.25
Breakeven prices
Profit or loss at expiration
0
Figure 4-13  Long a 95 put –2.25; long a 100 put –4.50; long a 105 put –7.75.
Profit or loss at expiration
0
100
–7.75
95 put
105 put
Long a 95 Put –2.25
Long a 100 Put –4.50
Long a 105 Put –7.75
100 put
95
–4.50
–2.25
105
92.75
97.25
Breakeven prices
95.50
--- page 66 ---

E x p i r at i o n P r o f i t a n d L o s s
49
Consider the following position
Position
Contract Price
+1  95 call
6.25
–1  105 call
1.75
–2  105 puts
7.75
–2  Underlying contracts
98.00
The slopes of the position are
Contract
Below 95
95–105
Above 105
+1  95 call
0
+1
+1
–1  105 call
0
0
–1
–2  105 puts
+2
+2
0
–2  Underlying contracts
–2
–2
–2
Total
0
+1
–2
It is usually easiest to determine the P&L at an exercise price, so let’s use
95. The P&L at an underlying price of 95 is
Position
Contract
Price
Contract
Value at 95
Contract P&L
at 95
Total
Contract P&L
+1  95 call
6.25
0
–6.25
–6.25
–1  105 call
1.75
0
+1.75
+1.75
–2  105 puts
7.75
10.00
–2.25
–4.50
–2  Underlying contracts
98.00
95.00
+3.00
+6.00
Total P&L at 95.00
–3.00
Figure 4-14 shows the entire expiration P&L graph for the position. Below
95, the slope of the graph is 0, so the P&L is always –3.00. Between 95 and 105,
the slope is +1, so the P&L at 105 (10 points higher) is –3.00 + 10.00 = +7.00.
Above 105, the slope is –2, with the position losing one point for each point increase in the price of the underlying.
The position has two breakeven prices, one between 95 and 105 and one
above 105. With a P&L of –3.00 at 95 and a slope of +1 between 95 and 105,
the first breakeven is
95.00 + (3.00/1) = 98.00
--- page 67 ---

50
O P T I O N V O L AT I L I T Y A N D P R I C I N G
With a P&L of +7.00 at 105 and a slope above 105 of –2, the second breakeven is
105.00 + (7.00/2) = 108.50
Finally, let’s go back to the parity-graph position shown in Figure 4-9.
Suppose that we are told that at expiration with an underlying price of 62.00
the position will show a profit of 2.10. What will be the P&L at expiration if
the underlying price is 81.50? Using the slopes, we can work our way from
62.00 to 81.50
Interval
Beginning P&L
Slope
Ending P&L
62.00–65.00
+2.10
–3
+2.10 – (3 × 3) = –6.90
65.00–70.00
–6.90
+2
–6.90 + (2 × 5) = +3.50
70.00–75.00
+3.10
0
                                   +3.50
75.00–80.00
+3.10
–3
+3.50 – (3 × 5) = –11.90
80.00–81.50
–11.90
–1
–11.90 – (1 × 1.50) = –13.40
Figure 4-14
Profit or loss at expiration
0
Breakeven
108.50
+1 95 call –6.25
–1 105 call –1.75
–2 105 puts –7.75
–2 underlying contracts –98.00
Breakeven
98.00
+1
+1
+1
–2
–3.00
105
95
+7.00
--- page 68 ---

E x p i r at i o n P r o f i t a n d L o s s
51
At an underlying price of 81.50, the position will show a loss of 13.40. We can
also see that there are three breakeven prices for the position:
Between 62.00 and 65.00
62.00 + 2.10/3 = 62.70
Between 65.00 and 70.00
65.00 + 6.90/2 = 68.45
Between 75.00 and 80.00
75.00 + 3.10/3 ≈ 76.03
All critical points for the position are shown in Figure 4-15.
Figure 4-15
–4 underlying contracts
+3 65 calls
+2 65 puts
+2 70 calls
–4 70 puts
–5 75 calls
+3 75 puts
+3 80 calls
–2 80 puts
Below 65
–3
Between 65 and 70
+2
Between 70 and 75
0
Between 75 and 80
–3
Above 80
–1
+3
+2
–6.90
+1
–1
+3
–1
65
70
75
80
Slope = 0 Slope = –3
Slope = –1
Slope = +2
Slope = –3
+2.10
+3.10
+3.10
Breakeven
68.45
Breakeven
76.03
Breakeven
62.70
62
–11.90
–13.40
–1
+1
81.50
Position
Slopes
--- page 69 ---

52
5
Theoretical
Pricing Models
In  Chapter 4, we considered the value of an option and the profit or loss resulting from an option strategy at the moment of expiration. From the expiration
profit and loss (P&L) graphs, we can see clearly that the direction in which an
underlying contract moves can be an important consideration in choosing an
option strategy. A trader who believes that the underlying market will rise will
be more inclined either to buy calls or sell puts. A trader who believes that the
underlying market will fall will be more inclined either to buy puts or sell calls.
In each case, the directional movement in the underlying market will increase
the likelihood that the strategy will be profitable.
However, an option trader has an additional problem that we might call
the “speed” of the market. If we ignore interest and dividend considerations,
a trader who believes that a stock will rise in price within a specified period can
be reasonably certain of making a profit if he is right.  He can simply buy the
stock, wait for it to reach his target price, and then sell the stock at a profit.
The situation is not quite so simple for an option trader. Suppose that a
trader believes that a stock will rise in price from $100, its present price, to $115
within the next five months. Suppose also that a $110 call expiring in three
months is available at a price of $2. If the stock rises to $115 by expiration, the
purchase of the $110 call will result in a profit of $3 ($5 intrinsic value minus
the $2 cost of the option). But is this profit a certainty? What will happen if
the price of the stock remains below $110 for the next three months and only
reaches $115 after the option expires? Then the option will expire worthless,
and the trader will lose his $2 investment.
Perhaps the trader would do better to purchase a $110 call that expires in
six months rather than three months. Now he can be certain that when the stock
reaches $115, the call will be worth at least $5 in intrinsic value. But what if the
price of the six-month option is $6? In this case, the trader still might show a
loss. Even if the underlying stock reaches the target price of $115, there is no
guarantee that the $110 call will ever be worth more than its $5 intrinsic value.
--- page 70 ---

T h e o r e t i c a l P r i c i n g M o d e l s
53
A trader in an underlying market is interested almost exclusively in the direction in which the market will move. Although an option trader is also sensitive to directional considerations, he must also give some thought to how fast the
market is likely to move. If a trader in the underlying stock and an option trader
in the same market take long market positions in their respective instruments
and the market does in fact move higher, the stock trader is assured of a profit,
while the option trader may show a loss. If the market fails to move sufficiently
fast, the favorable directional move may not be enough to offset the option’s loss
in time value. A speculator will often buy options for their seemingly favorable
risk-reward characteristics (limited risk, unlimited reward), but if he purchases
options, not only must he be right about market direction, he must also  be right
about market speed. Only if he is right on both counts can he expect to make a
profit. If predicting the correct market direction is difficult, correctly predicting
direction and speed is probably beyond most traders’ capabilities.
The concept of speed is crucial in trading options. Indeed, many option
strategies depend only on the speed of the underlying market and not at all on
its direction. If a trader is highly proficient at predicting directional moves in
the underlying market, he is probably better advised to trade the underlying instrument. Only when a trader has some feel for the speed component can he
hope to successfully enter the option market.
The Importance of Probability
One can never be certain about future market conditions, so almost all trading
decisions are based on some estimate of probability. We often express our opinions about probability using words such as likely, good chance, possible, and probable. But in an option evaluation we need to be more specific. We need to define
probability in way that will enable us to do the types of calculations required
to make intelligent decisions in the marketplace. If we can do this, we will find
that probability and the choice of strategy go hand in hand. If a trader believes
that a strategy has a very high probability of profit and a very low probability of loss, he will be satisfied with a small potential profit because the profit is
likely to be quite secure. On the other hand, if the probability of profit is very
low, the trader will demand a large profit when market conditions develop favorably. Because of the importance of probability in the decision-making process, it will be worthwhile to consider some simple probability concepts.
Expected Value
Suppose that we are given the opportunity to roll a six-sided die, and each time
we roll, we will be paid a dollar amount equal to the number that comes up. If we
roll a one, we are paid $1; if we roll a two, we are paid $2; and so on up to six, in
which case we are paid $6. If we are given the opportunity to roll the die an infinite number of times, on average, how much do we expect to receive per roll?
We can calculate the answer using some simple arithmetic. There are six
possible numbers, each with equal probability. If we add up the six possible
outcomes 1 + 2 + 3 + 4 + 5 + 6 = 21 and divide this by the six faces on the die,
--- page 71 ---

54
O P T I O N V O L AT I L I T Y A N D P R I C I N G
we get 21/6 = 3½. That is, on average, we can expect to get back $3½ each
time we roll the die. This is the average payback, or expected value. If we must
pay for the privilege of rolling the die, what is a reasonable price? If we purchase the chance to roll the die for less than $3½, in the long run, we expect to
show a profit. If we pay more than $3½, in the long run, we expect to show a
loss. And if we pay exactly $3½, we expect to break even. Note the qualifying
phrase in the long run. The expected value of $3½ is realistic only if we are allowed to roll the die many, many times. If we are allowed to roll only once, we
cannot be certain of getting back $3½. Indeed, on any one roll, it is impossible
to get back $3½ because no face of the die has exactly 3½ spots. Nevertheless,
if we pay less than $3½ for even one roll of the die, the laws of probability are
on our side because we have paid less than the expected value.
In a similar vein, consider a roulette bet. The roulette wheel has 38 slots,
numbers 1 through 36 and 0 and 00.1 Suppose that a casino allows a player to
choose a number. If the player’s number comes up, he receives $36; if any other
number comes up, he receives nothing. What is the expected value for this proposition? There are 38 slots on the roulette wheel, each with equal probability, but
only one slot will return $36 to the player. If we divide the one outcome where
the player wins $36 by the 38 slots on the wheel, the result is $36/38 = $0.9474,
or about 95 cents. A player who pays 95 cents for the privilege of picking a number at the roulette table can expect to approximately break even in the long run.
Of course, no casino will let a player buy such a bet for 95 cents. Under
those conditions, the casino would make no profit. In the real world, a player
who wants to purchase such a bet will have to pay more than the expected return, typically $1. The 5-cent difference between the $1 price of the bet and
the 95-cent expected value represents the profit potential, or edge, to the casino.
In the long run, for every dollar bet at the roulette table, the casino can expect
to keep about 5 cents.
Given the preceding conditions, any player interested in making a profit
would rather switch places with the casino. Then he would have a 5-cent edge
on his side by selling bets worth 95 cents for $1. Alternatively, the player would
like to find a casino where he could purchase the bet for less than its expected
value of 95 cents, perhaps 88 cents. Then the player would have a 7-cent edge
over the casino.
Theoretical Value
The theoretical value of a proposition is the price one would be willing to pay now
to just break even in the long run. Thus far, the only factor we have considered
in determining the value of a proposition is the expected value. We used this
concept to calculate the 95-cent fair price for the roulette bet.
Suppose that in our roulette example the casino decides to change the conditions slightly. The player may now purchase the roulette bet for its expected
value of 95 cents, and as before, if he loses, the casino will immediately collect
1 We assume a roulette wheel with 38 slots, as is customary in the United States. In some parts of the world, a
roulette wheel may have no slot numbered 00. This, of course, changes the probabilities.
--- page 72 ---

T h e o r e t i c a l P r i c i n g M o d e l s
55
his 95 cents. Under the new conditions, however, if the player wins, the casino
will send him his $36 winnings in two months. Will both the player and the casino still break even on the proposition?
Where did the player get the 95 cents that he bet at the roulette wheel? In
the immediate sense, he may have taken it out of his pocket. But a closer examination may reveal that he withdrew the money from his bank prior to visiting
the casino. Because he won’t receive his winnings for two months, he will have
to take into consideration the two months of interest he would have earned had
he left the 95 cents in the bank. The theoretical value of the bet is really the present value of its expected value, the 95 cents expected value discounted by interest. If interest rates are 12 percent annually, the theoretical value is
95 cents/(1 + 0.12 × 2/12) ≈ 93 cents
Even if the player purchases the bet for its expected return of 95 cents, he
will still lose 2 cents because of the interest that he could have earned for two
months if he had left his money in the bank. The casino, on the other hand, will
take the 95 cents, put it in an interest-bearing account, and at the end of two
months collect 2 cents in interest. Under the new conditions, if a player pays 93
cents for the roulette bet today and receives his winnings in two months, neither
he nor the casino can expect to make any profit in the long run.
The two most common considerations in option evaluation are the
expected return and interest. There may, however, be other considerations.
Suppose that the player is a good client, and the casino decides to send him
a 1-cent bonus a month from now. He can add this additional payment to
the previous theoretical value of 93 cents to get a new theoretical value of
94 cents. This is similar to the dividend paid to owners of stock in a company.
In fact, dividends can be an additional consideration in evaluating both stock
and options on stock.
If a casino is selling roulette bets that have an expected value of 95 cents for
a price of $1, does this guarantee that the casino will make a profit? It does if
the casino can be certain of staying in business for the “long run” because over
long periods of time the good and bad luck will tend to even out. Unfortunately,
before the casino reaches the long run, it must survive the short run. It’s possible
that someone can walk up to the roulette wheel, make a series of bets, and have
their number come up 20 times in succession. Clearly, this is very unlikely, but
the laws of probability say that it could happen. If the player’s good luck results
in the casino going out of business, the casino will never reach the long run.
The goal of option evaluation is to determine, through the use of a theoretical pricing model, the theoretical value of an option. The trader can then
make an intelligent decision whether the price of the option in the marketplace
is either too low or too high and whether the theoretical edge is sufficient to justify making a trade. But determining the theoretical value is only half the problem. Because an option’s theoretical value is based on the laws of probability,
which are only reliable in the long run, the trader must also consider the question of risk. Even if a trader has correctly calculated an option’s theoretical
value, how will he control the short-term bad luck that goes with any probability calculation? We shall see that in the real world, an option’s theoretical value
--- page 73 ---

56
O P T I O N V O L AT I L I T Y A N D P R I C I N G
is always open to question. For this reason, a trader’s ability to manage risk is at
least as important as his ability to calculate a theoretical value.
A Word on Models
What is a model? We can think of a model as a scaled-down or more easily managed representation of the real world. The model may be a physical one, such as
a model airplane or architectural model, or it may be a mathematical one, such as
a formula. In each case, we use the model to better understand the world around
us. However, it is unwise, and sometimes dangerous, to assume that the model
and the real world that it represents are identical in every way. We may have an
excellent model, but it is unlikely to be an exact replica of the real world.
All models, if they are to be effective, require us to make certain prior
assumptions about the real world. Mathematical models require the input
of numbers that quantify these assumptions. If we feed incorrect data into a
model, we can expect an incorrect representation of the real world. As every
model user knows, “Garbage in, garbage out.”
These general observations about models are no less true for option pricing models. An option model is only someone’s idea of how an option might
be evaluated under certain conditions. Because either the model itself or the
data that we feed into the model might be incorrect, there is no guarantee that
model-generated values will be accurate. Nor can we be sure that these values
will bear any logical resemblance to actual prices in the marketplace.
A new option trader is like someone entering a dark room for the first time.
Without any guidance, he may grope around, hoping that he eventually finds
what he is looking for. The trader who is armed with a basic understanding of
theoretical pricing models enters the same room with a candle. He can make out
the general layout of the room, but the dimness of the candle prevents him from
distinguishing every detail. Moreover, some of what he sees may be distorted by
the flickering of the candle. In spite of these limitations, a trader is more likely to
find what he is looking for with a small candle than with no illumination at all.2
The real problems with theoretical pricing models arise after the trader
has acquired some sophistication. As he gains confidence, he may begin to
increase the size of his trades. When this happens, his inability to make out
every detail in the room, as well as the distortions caused by the flickering candle flame, take on increased importance. Now a misinterpretation of what he
thinks he sees can lead to financial disaster because any error in judgment will
be greatly magnified.
The sensible approach is to make use of a model, but with a full awareness
of what it can and cannot do. Option traders will find that a theoretical pricing
model is an invaluable tool to understanding the pricing of options. Because of
the insights gained from a model, the great majority of successful option traders rely on some type of theoretical pricing model. However, an option trader,
if he is to make the best use of a theoretical pricing model, must be aware of its
2 One might also argue that a trader with a candle (i.e., theoretical pricing model) might drop the candle and burn
down the entire building. Financial crises seem to occur when many traders drop their candles at the same time.
--- page 74 ---

T h e o r e t i c a l P r i c i n g M o d e l s
57
limitations as well as its strengths. Otherwise, he may be no better off than the
trader groping in the dark.3
A Simple Approach
How might we adapt the concepts of expected value and theoretical value to
the pricing of options? Consider an underlying contract that at expiration can
take on one of five different prices: $80, $90, $100, $110, or $120. Assume,
moreover, that each of the five prices is equally likely with 20 percent probability. The prices and probabilities are shown Figure 5-1.
What will be the expected value for this contract at expiration? Twenty
percent of the time, the contract will be worth $80; 20 percent of the time,
the contract will be worth $90; and so on, up to the 20 percent of the time, the
contract is worth $120:

(20% × $80) + (20% × $90) + (20% × 100) + (20% × $110)

+ (20% × $120) = $100
At expiration, the expected value for the contract is $100.
Now consider the expected value of a 100 call using the same underlying
prices and probabilities. We can more easily see the value of the call by overlaying the parity graph for the call on our probability distribution. This has been
done in Figure 5-2. If the underlying contract is at $80, $90, or $100, the call
is worthless. If, however, the underlying contract is at $110 or $120, the option
will be worth its intrinsic value of $10 and $20, respectively:
(20% × 0) + (20% × 0) + (20% × 0) + (20% × $10) + (20% × $20) = $6
If we want to develop a theoretical pricing model using this approach, we
might propose a series of possible prices and probabilities for the underlying
contract at expiration. Then, given an exercise price, we can calculate the intrinsic value of the option at each underlying price, multiply this value by its associated probability, add up all these numbers, and thereby obtain an expected
value for the option. The expected value for a call at expiration is
p
S
X
max(
,0)
i
i
n
i
1∑
−
=
where each Si is a possible underlying price at expiration, and pi is the probability associated with that price. The expected value for a put is
p
X
S
max(
,0)
i
i
n
i
1∑
−
=
3 Some interesting discussion on the limitations of models: Fischer Black, “The Holes in Black Scholes,”
Risk 1(4):30–33, 1988; Stephen Figlewski, “What Does an Option Pricing Model Tell Us about Option Prices?”
Financial Analysts Journal, September–October 1989, pp. 12–15; Fischer Black, “Living Up to the Model,”
Risk 3(3):11–13, 1990; and Emanuel Derman and Paul Wilmott, “The Financial Modelers’ Manifesto”
( January 2009), http://www.wilmott.com/blogs/paul/index.cfm/2009/1/8/Financial-Modelers-Manifesto.
--- page 75 ---

58
O P T I O N V O L AT I L I T Y A N D P R I C I N G
In the foregoing example, we used a simple scenario with only five possible
price outcomes, each with identical probability. Obviously, this is not very realistic. What changes might we make to develop a model that more accurately reflects the real world? For one thing, we need to know the settlement procedure
for the option. If the option is subject to stock-type settlement, we must pay the
full price of the option. If the 100 call has an expected value of $6 at expiration, the theoretical value will be the present value of this amount. If interest
rates are 12 percent annually (1 percent per month) and the option will expire
in two months, the theoretical value of the option is
$6.00
1
(0.12
2/12)
$6.00
1.02
$5.88
+
×
=
≈
What other factors might we consider? We assumed that all five price outcomes were equally likely. Is this a realistic assumption? Suppose that you were
told that only two prices were possible at expiration, $110 and $250. If the current price of the underlying contract is close to $100, which do you think is more
likely? Experience suggests that extreme price changes that are far away from today’s price are less likely than small changes that remain close to today’s price. For
this reason, $110 is more likely than $250. Perhaps our probability distribution
ought to reflect this by concentrating the probabilities around the current price of
Figure 5-2
80
90
100
110
120
Underlying price:
Value of 100 call:
+1
+1
0
0
0
10
20
20%
20%
20%
20%
20%
Figure 5-1
80
90
100
110
120
Underlying price:
20%
20%
20%
20%
20%
--- page 76 ---

T h e o r e t i c a l P r i c i n g M o d e l s
59
the underlying contract. One possible distribution is shown in Figure 5-3. Using
these new probabilities, the expected value for the 100 call is now
(0% × 0) + (20% × 0) + (0% × 0) + (20% × $10) + (10% × $20) = $4
If, as before, the option is subject to stock-type settlement, the theoretical value is
$4.00
1.02
$3.92
≈
Note that the new probabilities did not change the expected value for the underlying contract. Because the probabilities are symmetrical around $100, the
expected value for the underlying contract at expiration is still $100.
No matter how we assign probabilities, we will want to do so in such a way
that the expected value for the underlying contract represents the most likely,
or average, value at expiration. What is the most likely future value for the underlying contract? In fact, there is no way to know. But we might ask what the
marketplace thinks the most likely value is. Recall what would happen if the
theoretical forward price were different from the actual price of a forward contract in the marketplace. Everyone would execute an arbitrage by either buying
or selling the forward contract and taking the opposite position in the cash market. In a sense, the marketplace must think that the forward price is the most
likely future value for the underlying contract. If we assume that the underlying
market is arbitrage-free, the expected value for the underlying contract must be
equal to the forward price.
Suppose in our example that the underlying contract is a stock that is currently trading at $100 and that pays no dividend prior to expiration. The twomonth forward price for the stock is
$100 × [1 + (0.12 × 2/12) ] = $100 × 1.02 = $102
If $102 is the expected value for the stock, instead of assigning the probabilities symmetrically around $100, we may want to assign them symmetrically
Figure 5-3
80
90
100
110
120
Underlying price:
Value of 100 call:
+1
+1
20%
40%
20%
10%
10%
0
0
0
10
20
--- page 77 ---

60
O P T I O N V O L AT I L I T Y A N D P R I C I N G
around $102. This distribution is shown in Figure 5-4. Now the expected value
for the 100 call is
(10% × 0) + (20% × 0) + (40% × $2) + (20% × $12) + (10% × $22) = $5.40
and the theoretical value is
$5.40
1.02
$5.29
≈
In the examples thus far, we have assumed a symmetrical probability distribution. But as long as the expected value is equal to the forward price, there
is no requirement that the probabilities be assigned symmetrically. Figure 5-5
shows a distribution where the price outcomes are neither centered around the
forward price nor are the probabilities symmetrical. Nonetheless, the expected
value for the underlying contract is still equal to $102
(6% × 83) + (15% × 90) + (39% × $99) + (33% × $110) + (7% × $123)
= 4.98 + 13.5 + 38.61 + 36.30 + 8.61 = $102
Using these probabilities, the theoretical value of the 100 call is
(33%
$10)
(7%
$23)
1.02
3.30
1.61
1.02
4.91
1.02
$4.81
×
+
×
=
+
=
≈
The forward price of the underlying contract plays a central role in all option pricing models. For European options, the current price of the underlying
contract is important only insofar as it can be turned into a forward price. Because of this, traders sometimes make the distinction between options that are
at the money (the exercise price is equal to the current underlying price) and
options which are at the forward (the exercise price is equal to the forward price
at expiration). In many markets, at-the-forward options are the most actively
traded, and such options are often used by traders as a benchmark for evaluating and trading other options.
Even if we assume an arbitrage-free market in the underlying contract, we
still have a major hurdle to overcome. In our simplified model, we assumed that
Figure 5-4
82
92
102
112
122
Underlying price:
Value of 100 call:
+1
+1
20%
40%
20%
10%
10%
0
0
2
12
22
