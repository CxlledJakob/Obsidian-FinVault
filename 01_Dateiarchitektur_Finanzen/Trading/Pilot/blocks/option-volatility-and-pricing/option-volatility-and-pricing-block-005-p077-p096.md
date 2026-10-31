# Option Volatility and Pricing_ Advanced Trading Strategies -- Sheldon Natenberg -- 2nd ed, 2014 -- McGraw Hill Professional -- isbn13 9780071818773 -- 6a48d008bd9beef283debf7bad0b2e4a -- Anna’s Archive.pdf — pages 77–96

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
--- page 78 ---

T h e o r e t i c a l P r i c i n g M o d e l s
61
there were only five possible price outcomes. In the real world, however, there
are an infinite number of possibilities. To enable our model to more closely approximate the real world, we would like to construct a probability distribution
with every possible price outcome together with its associated probability. This
may seem an insurmountable obstacle, but we will see in subsequent chapters
how we might approximate such a probability distribution.
We can now summarize the necessary steps in developing a model:
1.	 Propose a series of possible prices at expiration for the underlying
contract.
2.	 Assign a probability to each possible price with the restriction that the
underlying market is arbitrage-free—the expected value for the underlying contract must be equal to the forward price.
3.	 From the prices and probabilities in steps 1 and 2, and from the chosen exercise price, calculate the expected value of the option.
4.	 Lastly, depending on the option’s settlement procedure, calculate the
present value of the expected value.
The Black-Scholes Model
One of the first attempts to describe traded options in detail was a pamphlet
written by Charles Castelli and published in London in 1877, “The Theory of
Options in Stocks and Shares.”4 This pamphlet included a description of some
commonly used hedging and trading strategies such as the “call-of-more” and the
“call-and-put.” Today, these strategies are known as a covered-write and a straddle.
The origins of modern option pricing theory are most often ascribed to the
year 1900, when French mathematician Louis Bachelier published The Theory
4 A photocopy of the Castelli pamphlet, which is now in the public domain, is available at books.google.com.
Figure 5-5
83
90
99
110
123
Underlying price:
Value of 100 call:
+1
+1
33%
39%
15%
6%
7%
0
0
0
10
23
--- page 79 ---

62
O P T I O N V O L AT I L I T Y A N D P R I C I N G
of Speculation, the first attempt to use higher mathematics to price option contracts.5 Although Bachelier’s treatise was an interesting academic study, it resulted in little practical application because there were no organized option
markets at that time. However, in 1973, concurrent with the opening of the
Chicago Board Options Exchange, Fischer Black, at the time associated with the
University of Chicago, and Myron Scholes, associated with the Massachusetts Institute of Technology, built on the work of Bachelier and other academics to introduce the first practical theoretical pricing model for options.6 The Black-Scholes
model,7 with its relatively simple arithmetic and limited number of inputs, most of
which were easily observable, proved an ideal tool for traders in the newly opened
U.S. option market. Although other models have subsequently been introduced to
overcome some of its original weaknesses, the Black-Scholes model remains the
most widely used of all option pricing models.
In its original form, the Black-Scholes model was intended to evaluate
European options (no early exercise permitted) on non-dividend-paying stocks.
Shortly after its introduction, realizing that many stocks pay dividends, Black
and Scholes added a dividend component. In 1976, Fischer Black made slight
modifications to the model to allow for the evaluation of options on futures
contracts.8 In 1983, Mark Garman and Steven Kohlhagen of the University of
California at Berkeley made additional modifications to allow for the evaluation of options on foreign currencies.9 The futures version and the foreign-currency version are known formally as the Black model and the Garman-Kohlhagen
model, respectively. However, the evaluation method in each variation, whether
the original Black-Scholes model for stock options, the Black model for futures
options, or the Garman-Kohlhagen model for foreign currency options, is so
similar that they have all come to be known simply as the Black-Scholes model.
The various forms of the model differ only in how they calculate the forward
price of the underlying contract and the settlement procedure for the options.
An option trader will simply choose the form appropriate to the options and
underlying instrument in which he is interested.
Given its widespread use and its importance in the development of other
pricing models, we will, for the moment, restrict ourselves to a discussion of
the Black-Scholes model and its various forms. In later chapters we will consider the question of early exercise. We will also look at alternative methods for
pricing options when we question some of the basic assumptions in the Black-
Scholes model.
5 See Louis Bachelier’s Theory of Speculation, Mark Davis and Alison Etheridge, trans. (Princeton, NJ: Princeton
University Press, 2006). A translation of Bachelier’s treatise also appears in The Random Character of Stock Market
Prices, Paul Cootner, ed. (Cambridge, MA: MIT Press, 1964).
6 Fischer Black and Myron Scholes, “The Pricing of Options and Corporate Liabilities,” Journal of Political
Economy 81(3):637–654, 1973.
7 Robert Merton, who, at the time, was, like Myron Scholes, associated with MIT, is also credited with some
of the same work that led to the development of the original Black-Scholes model. His paper, “The Rational
Theory of Option Pricing,” appeared in the Bell Journal of Economics and Management Science 4(Spring):141–183,
1973. In recognition of Merton’s contribution, the model is sometimes referred to as the Black-Scholes-Merton
model. Scholes and Merton were awarded the Nobel Prize in Economic Sciences in 1997; Fischer Black, unfortunately, died in 1995.
8 Fischer Black, “The Pricing of Commodity Contracts,” Journal of Financial Economics 3:167–179, 1976.
9 Mark B. Garman and Steven W. Kohlhagen, “Foreign Currency Option Values,” Journal of International Money
and Finance 2(3):239–253, 1983. We are speaking here of options on a physical foreign currency rather than options
on a foreign-currency futures contract. The latter may be evaluated using the Black model for futures options.
--- page 80 ---

T h e o r e t i c a l P r i c i n g M o d e l s
63
The reasoning that led to the development of the Black-Scholes model is
similar to the simple approach we took earlier in this chapter for evaluating options. Black and Scholes worked originally with call values, but put values can
be derived in much the same way. Alternatively, we will see later that for European options there is a unique pricing relationship between an underlying contract and a call and put with the same exercise price and expiration date. This
relationship will enable us to derive a put value from the companion call value
or a call value from the companion put value.
To calculate an option’s theoretical value using the Black-Scholes model,
we need to know, at a minimum, five characteristics of the option and its underlying contract:
1.	 The option’s exercise price
2.	 The time remaining to expiration
3.	 The current price of the underlying contract
4.	 The applicable interest rate over the life of the option
5.	 The volatility of the underlying contract
The last input, volatility, may be unfamiliar to a new trader. While we will
put off a detailed discussion of this input to Chapter 6, from our previous discussion, we can reasonably infer that volatility is related to either the speed of
the underlying market or the probabilities of different price outcomes.
If we know each of the required inputs, we can feed them into the theoretical pricing model and thereby generate a theoretical value (see Figure 5-6).
Black and Scholes also incorporated into their model the concept of a riskless hedge. For every option position, there is a theoretically equivalent position
in the underlying contract such that, for small price changes in the underlying
contract, the option position will gain or lose value at exactly the same rate as
the underlying position. To take advantage of a theoretically mispriced option,
Figure 5-6
Exercise price
Time to expiration
Underlying price
Interest rate
Volatility
Pricing
model
Theoretical
value
--- page 81 ---

64
O P T I O N V O L AT I L I T Y A N D P R I C I N G
it is necessary to establish this riskless hedge by offsetting the option position
with a theoretically equivalent underlying position. That is, whatever option
position we take, we must take an opposing market position in the underlying
contract. The correct proportion of underlying contracts needed to establish
this riskless hedge is determined by the option’s hedge ratio.
Why is it necessary to establish a riskless hedge? Recall that in our simplified approach, an option’s theoretical value depended on the probability of
various price outcomes for the underlying contract. As the price of the underlying contract changes, the probability of each outcome will also change. If the
underlying price is currently $100 and we assign a 25 percent probability to
$120, we might drop the probability for $120 to 10 percent if the price of the
underlying contract falls to $90. By initially establishing a riskless hedge and
then adjusting the hedge as market conditions change, we are taking into consideration these changing probabilities.
In this sense, an option can be thought of as a substitute for a position in
the underlying contract. A call is a substitute for a long position; a put is a substitute for a short position. Whether the substitute position is better than an
outright position in the underlying contract depends on the theoretical value
of the option compared with its price in the marketplace. If a call can be purchased for less than its theoretical value or a put can be sold for more than its
value, in the long run, it will be more profitable to take a long market position
by purchasing calls or selling puts than by purchasing the underlying contract.
In the same way, if a put can be purchased for less than its theoretical value or
a call can be sold for more than its value, in the long run, it will be more profitable to take a short market position by purchasing puts or selling calls than by
selling the underlying contract.
In later chapters we will discuss the concept of a riskless hedge in greater
detail. For now, we simply summarize the four basic option positions, their corresponding market positions, and the appropriate hedges:
Option Position
Corresponding Market Position
Appropriate Hedge
Buy call(s)
Long
Sell underlying
Sell call(s)
Short
Buy underlying
Buy put(s)
Short
Buy underlying
Sell put(s)
Long
Sell underlying
For new traders, it may be helpful to point out that we are always doing
the opposite with calls and the underlying (i.e., buy calls, sell the underlying;
sell calls, buy the underlying) and doing the same with puts and the underlying
(i.e., buy puts, buy the underlying; sell puts, sell the underlying). Especially with
puts, more than a few new traders have initially done it backwards, buying puts
and selling the underlying or selling puts and buying the underlying. This, of
course, is no hedge at all.
Because the theoretical value obtained from a theoretical pricing model is
no better than the inputs into the model, a few comments on each of the inputs
will be worthwhile.
--- page 82 ---

T h e o r e t i c a l P r i c i n g M o d e l s
65
Exercise Price
There should never be any doubt about the exercise price of an option because
it is fixed under the terms of the contract and does not vary over the life of the
option.10 A March 60 call cannot suddenly turn into a March 55 call. A September 100 put cannot turn into a September 110 put.
Time to Expiration
As with the exercise price, an option’s expiration date is fixed and will not vary.
A March 60 call will not suddenly turn into an April 60 call, nor will a September 100 put turn into an August 100 put. Of course, each day that passes brings
us closer to expiration, so in this sense the time to expiration is constantly growing shorter. However, the expiration date, like the exercise price, is fixed by the
exchange and will not change.
In financial models, one year is typically the standard unit of time.
Therefore, time to expiration is entered into the Black-Scholes model as an
annualized number. If we express time in terms of days, we must make the
appropriate adjustment by dividing the number of days to expiration by 365.
However, most option-evaluation computer programs already have this transformation incorporated into the software, so we need only enter the correct
number of days remaining to expiration.
It may seem that we have a problem in deciding what number of days to
enter into the model. We need the amount of time remaining to expiration
for two purposes: (1) to determine the likelihood of price movement in the
underlying contract and (2) to make interest calculations. For the former, we
are only interested in days on which the price of the underlying contract can
change. For exchange-traded contracts, this can only occur on business days.
This might lead us to drop weekends and holidays from our calculations. On
the other hand, for interest-rate purposes, we must include every day. If we
borrow or lend money, we expect interest to accrue every day, no matter that
some of those days are not business days.
However, this is not really a problem. In determining the likelihood of
price movement in the underlying contract, we observe only business days
because these are the only days on which price changes can occur. Then we
scale these values to an annualized number before feeding it into the theoretical pricing model. The result is that we can feed into our model the actual number of days remaining to expiration, knowing that the model will
interpret all inputs correctly.
Although traders typically express time to expiration in days, a trader may
want to use a different measure. Especially as expiration approaches, a trader
may prefer to use hours or even minutes. In theory, finer time increments should
yield more accurate values. But there is a practical limitation to using very small
increments of time. As time passes, the discrete increments of time we feed into
a theoretical pricing model may not accurately represent the continuous passage
10 An exchange may adjust the exercise price of a stock option as the result of a stock split or in the case of an
extraordinary dividend. In practical terms, this is only an accounting change. The characteristics of the option
contract remain essentially unchanged.
--- page 83 ---

66
O P T I O N V O L AT I L I T Y A N D P R I C I N G
of time in the real world. Most traders have learned through experience that as
expiration approaches, the use of a theoretical pricing model becomes less reliable because the inputs become less reliable. Indeed, very close to expiration,
many traders stop using model-generated values altogether.
Underlying Price
Unlike the exercise price and time to expiration, the correct price of the underlying contract is not always obvious. At any one time, there is a bid price and
an ask price (the bid-ask spread), and it may not be clear whether we ought to use
one or the other of these prices or perhaps some price in between.
Consider an underlying market where the last trade price was 75.25 but
that is currently displaying the following bid-ask spread:
75.20–75.40
If a trader is using a theoretical pricing model to evaluate options on this market,
what price should he feed into the model? One possibility is 72.25, the last trade
price. Another possibility might be 75.30, the midpoint of the bid-ask spread.
Even though we are focusing on the use of theoretical pricing models, we
should emphasize that there is no law that says a trader must make any decisions
based on or consistent with a theoretical pricing model. A trader can simply
buy or sell options and hope that the trade turns out favorably. But a disciplined
trader who uses a pricing model knows that he is required to hedge the option position by taking an opposing market position in the underlying contract.
Therefore, the underlying price that he feeds into the theoretical pricing model
ought to be the price at which he believes he can make the opposing trade. If
the trader intends to purchase calls or sell puts, both of which are long market
positions, he will hedge by selling the underlying contract. In this case, he will
want to use something close to the bid price because that is the price at which he
can probably sell the underlying. On the other hand, if the trader intends to sell
calls or buy puts, both of which are short market positions, he will hedge by purchasing the underlying contract. Now he will want to use something close to the
ask price because that is the price at which he can probably buy the underlying.
In practice, if the underlying market is very liquid, with a narrow bid-ask
spread and many contracts available at each price, a trader who must make a
quick decision may very well use a price close to the midpoint because that probably represents a reasonable estimate of where the underlying can be bought
or sold. But in an illiquid market, with a very wide bid-ask spread and only a few
contracts available at each price, the trader must give extra thought to the appropriate underlying price. In such a market, particularly if the prices are changing
rapidly, it may be difficult to execute even a small order at the quoted prices.
Interest Rates
Because an option trade may result in either a cash credit or debit to a trader’s
account, the interest considerations resulting from this cash flow must also play
a role in option evaluation. This is a function of interest rates over the life of
the option.
--- page 84 ---

T h e o r e t i c a l P r i c i n g M o d e l s
67
Interest rates play two roles in the theoretical evaluation of options. First,
they may affect the forward price of the underlying contract. If the underlying
contract is subject to stock-type settlement, as we raise interest rates, we raise
the forward price, increasing the value of calls and decreasing the value of puts.
Second, interest rates may affect the present value of the option. If the option is
subject to stock-type settlement, as we raise interest rates, we reduce the present
value of the option. Although interest rates may affect both the forward price
and the present value, in most cases, the same rate is applicable, and we need
only input one interest rate into the model. If, however, different rates are applicable, as would be the case with foreign-currency options (the foreign-currency
interest rate plays one role, and the domestic-currency interest rate plays a different role), the model will require the input of two interest rates. This is the
case with the Garman-Kohlhagen version of the Black-Scholes model.
What interest rate should a trader use when evaluating options? Textbooks
often suggest using the risk-free rate, the rate that applies to the most creditworthy
borrower. In most markets, the government is considered the most secure borrower of funds, so the yield on a government security with a maturity equivalent to the life of the option is the general benchmark. For a 60-day option
denominated in dollars, we might use the yield on a 60-day U.S. Treasury bill;
for a 180-day option, we might use the yield on a 180-day U.S. Treasury bill.
In practice, no individual can borrow or lend at the same rate as the government, so it seems  unrealistic to use the risk-free rate. To determine a more
realistic rate, a trader might look to a freely traded market in interest-rate contracts. In this respect, traders often use either the London Interbank Offered Rate
(LIBOR)11 or the Eurocurrency markets to determine the applicable rate. For
dollar-denominated options, Eurodollar futures traded at the Chicago Mercantile Exchange are often used to determine a benchmark interest rate.
The situation is further complicated by the fact that most traders do not borrow and lend at the same rate, so the correct interest rate will, in theory, depend
on whether the trade will create a credit or a debit. In the former case, the trader
will be interested in the borrowing rate; in the latter case, he will be interested in
the lending rate. However, among the inputs into the model—the underlying
price, time to expiration, interest rates, and volatility—interest rates tend to play
the least important role. Using a rate that “makes sense” is usually a reasonable
solution. Of course, for very large positions or for very long-term options, small
changes in the interest rate can have a large impact. But for most traders, getting
the interest rate exactly right is usually not a major consideration.
Dividends
We did not list dividends as a model input in Figure 5-5 because they are only
a factor in the theoretical evaluation of stock options and then only if the stock
is expected to pay a dividend over the life of the option. In order to evaluate a
stock option, the model must accurately calculate the forward price for the stock.
11 The London Interbank Offered Rate (LIBOR) is the rate paid by the London banks on dollar deposits. As such, it reflects the free-market interest rate for dollars. LIBOR is the underlying for Eurodollar futures traded at the Chicago Mercantile Exchange. The value of these contracts at maturity is determined by the average three-month
LIBOR rate quoted by the largest London banks.
--- page 85 ---

68
O P T I O N V O L AT I L I T Y A N D P R I C I N G
This requires us to estimate both the amount of the dividend and the date on
which the dividend will be paid. In practice, rather than using the date of dividend payment, an option trader is likely to focus on the ex-dividend date, the date
on which the stock is trading without the rights to the dividend. The exact dividend payment date is important in calculating the interest that can be earned on
the dividend payment and thereby calculating a more accurate forward price.
But for a trader ownership of the stock in order to receive the dividend is the primary consideration. A deeply in-the-money option may have many of the same
characteristics as stock, but only ownership of the stock carries with it the rights
to the dividend.
In the absence of other information, most traders assume that a company
is likely to continue its past dividend policy. If a company has been paying a
75-cent dividend each quarter, it will probably continue to do so. However, until the company officially declares the dividend, this is not a certainty. A company may increase or reduce its dividend or omit it completely. If there is the
possibility of a change in a company’s dividend policy, a trader must consider
its impact on option values. Additionally, if the ex-dividend date is expected
just prior to expiration, a delay of several days will cause the ex-dividend date
to fall after expiration. For purposes of option evaluation, this is the same as
eliminating the dividend entirely. In such a situation, a trader will need to make
a special effort to ascertain the exact ex-dividend date.
Volatility
Of all the inputs required for option evaluation, volatility is the most difficult
for traders to understand. At the same time, volatility often plays the most important role in actual trading decisions. Changes in our assumptions about
volatility can have a dramatic effect on an option’s value. And the manner in
which the marketplace assesses volatility can have an equally dramatic effect on
an option’s price. For these reasons, we will begin a detailed discussion of volatility in Chapter 6.
--- page 86 ---

69
Volatility
What is volatility, and why is it so important in option evaluation? The option
trader, like a trader in the underlying instrument, is interested in the direction
of the market. But unlike a trader in the underlying, an option trader is also
sensitive to the speed of the market. If the market for an underlying contract
fails to move at a sufficient speed, options on that contract will have less value
because of the reduced likelihood of the market going through an option’s
exercise price. In a sense, volatility is a measure of the speed of the market.
Markets that move slowly are low-volatility markets; markets that move quickly
are high-volatility markets.
One might guess intuitively that some markets are more volatile than
others. During 2008, the price of crude oil began the year at $99 per barrel,
reached a high of $144 per barrel in July, and finished the year at $45 per barrel. The price rose 58 percent and then dropped 69 percent. Yet few traders
could imagine a major stock index such as the Standard and Poor’s (S&P) 500
Index exhibiting similar fluctuations over a single year.
If we know whether a market will be relatively volatile or relatively quiet
and can convey this information to a theoretical pricing model, any evaluation
of options on that market will be more accurate than if we simply ignore volatility. Because option models are based on mathematical formulas, we will need
some method of quantifying this volatility component so that we can feed it
into the model in numerical form.
Random Walks and Normal Distributions
Consider for a moment the pinball maze pictured in Figure 6-1. When a ball is
dropped into the maze at the top, it falls downward, pulled by gravity through
a series of nails. When the ball encounters each nail, there is a 50 percent
chance that the ball will move to the left and a 50 percent chance that it will
move to the right. The ball then falls down a level where it encounters another
nail. Finally, at the bottom of the maze, the ball falls into one of the troughs.
6
--- page 87 ---

70
O P T I O N V O L AT I L I T Y A N D P R I C I N G
As the ball falls down through the maze, it follows a random walk. Once the
ball enters the maze, nothing can be done to artificially alter its course, nor can
one predict the path that the ball will follow through the maze.
As more balls are dropped into the maze, they might begin to form a distribution similar to that in Figure 6-2. Most of the balls tend to cluster near the
center of the maze, with a decreasing number of balls ending up in troughs
farther away from the center. If many balls are dropped into the maze, they will
begin to form a bell-shaped or normal distribution.
If an infinite number of balls were dropped into the maze, the resulting
distribution might be approximated by a normal distribution curve such as the one
overlaid on the distribution in Figure 6-2. Such a curve is symmetrical (if we flip
it from right to left, it looks the same), it has its peak in the center, and its tails
always move down and away from the center.
Normal distribution curves are used to describe the likely outcomes of
random events. For example, the curve in Figure 6-2 might also represent the
results of flipping a coin 15 times. Each outcome, or trough, represents the
number of heads that occur from each 15 flips. An outcome in trough 0 represents 0 heads and 15 tails; an outcome in trough 15 represents 15 heads and 0
tails. Of course, we would be surprised to flip a coin 15 times and get all heads
or all tails. Assuming that the coin is perfectly balanced, some outcome in between, perhaps 8 heads and 7 tails, or 9 heads and 6 tails, seems more likely.
Suppose that we rearrange the nails in our maze so that each time a ball
encounters a nail and moves either left or right, it must drop down two levels
before it encounters another nail. If we drop enough balls into the maze, we
may end up with a distribution similar to the curve in Figure 6-3. Because the
Figure 6-1  Random walk.
. . . . . . . . . . . . . . . .
. . . . . . . . . . . . . . .
. . . . . . . . . . . . . .
. . . . . . . . . . . . .
. . . . . . . . . . . .
. . . . . . . . . . .
. . . . . . . . . .
. . . . . . . . .
. . . . . . . .
. . . . . . .
. . . . . .
. . . . .
. . . .
. . .
. .
. . . . . . . . . . . . . . . .
.
Random
walk
--- page 88 ---

V o l at i l i t y
71
Figure 6-2  Normal distribution.
. . . . . . . . . . . . . . . .
. . . . . . . . . . . . . . .
. . . . . . . . . . . . . .
. . . . . . . . . . . . .
. . . . . . . . . . . .
. . . . . . . . . . .
. . . . . . . . . .
. . . . . . . . .
. . . . . . . .
. . . . . . .
. . . . . .
. . . . .
. . . .
. . .
. .
. . . . . . . . . . . . . . . .
.
Normal
distribution
0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15
Figure 6-3
--- page 89 ---

72
O P T I O N V O L AT I L I T Y A N D P R I C I N G
sideways movement of the balls is restricted, the curve will have a higher peak
and narrower tails than the curve in Figure 6-2. In spite of its altered shape, the
distribution is still normal, although one with slightly different characteristics.
Finally, we might again rearrange the nails so that each time a ball drops
down a level, it must move two nails left or right before it can drop down to a
new level. If we drop enough balls into the maze, we may get a distribution that
resembles the curve in Figure 6-4. This distribution, although still normal, will
have a much lower peak and spread out much more quickly than the distributions in either Figure 6-2 or Figure 6-3.1
Suppose that we now think of the ball’s sideways movement as the up
and down price movement of an underlying contract and the ball’s downward
movement as the passage of time. If the price movement of an underlying
contract follows a random walk, the curves in Figures 6-2 through 6-4 might
represent possible price distributions in a moderate-, low-, and high-volatility
market, respectively.
Earlier in this chapter we suggested that the theoretical pricing of options
begins by assigning probabilities to the various underlying prices. How should
these probabilities be assigned? One possibility is to assume that, at expiration, the
underlying prices are normally distributed. Given that there are many different
normal distributions, how will our choice of distribution affect option evaluation?
Because all normal distributions are symmetrical, it may seem that the choice
of distribution is irrelevant. Increased volatility may increase the likelihood of
large upward movement, but this should be offset by the greater likelihood of
large downward movement. However, there is an important distinction between
1 The pinball maze, or quincunx (sometimes also called a Galton board), pictured in these examples is often used to
demonstrate basic probability theory. Examples of a quincunx in action can be found at the following websites:

http://www.teacherlink.org/content/math/interactive/flash/quincunx/quincunx.html

http://www.mathsisfun.com/data/quincunx.html

http://www.jcu.edu/math/isep/Quincunx/Quincunx.html
Figure 6-4
--- page 90 ---

V o l at i l i t y
73
an option position and an underlying position. The expected value for an underlying contract depends on all possible price outcomes. The expected value for
an option depends only on the outcomes that result in the option finishing in the
money. Everything else is zero.
In Figure 6-5, we have three possible price distributions centered around
the current price of an underlying contract. Suppose that we want to evaluate a call at a higher exercise price. The value of the call will depend on the
amount of the distribution to the right of the exercise price. We can see that as
we move from a low-volatility distribution, to a moderate-volatility distribution,
to a high-volatility distribution, a greater portion of the possible price distribution lies to the right of the exercise price. Consequently, the option takes on an
increasingly greater value.
We might also consider the value of a put at a lower exercise price. If we
assume that movement is random, the same high-volatility distribution that will
cause the call to take on greater value will also cause the put to take on greater
value. In the case of the put, more of the distribution will lie to the left of the
exercise price. Because our distributions are symmetrical, in a high-volatility
market, all options, whether calls or puts, higher or lower exercise prices, take
on greater value. For the same reason, in a low-volatility market, all options
take on reduced values.
Mean and Standard Deviation
If we assume a normal distribution of prices, we will need a method of describing the appropriate normal distribution to the theoretical pricing
model. Fortunately, all normal distributions can be fully described with two
Figure 6-5
Current
underlying
price
Exercise
price
Call value
Low-volatility
distribution
Moderate-volatility
distribution
High-volatility
distribution
Price distribution at expiration
--- page 91 ---

74
O P T I O N V O L AT I L I T Y A N D P R I C I N G
numbers—the mean and the standard deviation. If we know that a distribution is
normal, and we also know the mean and standard deviation, then we know all
the characteristics of the distribution.
Graphically, we can interpret the mean as the location of the peak of the
distribution and the standard deviation as a measure of how fast the distribution spreads out. Distributions that spread out very quickly, such as the one in
Figure 6-4, have a high standard deviation. Distributions that spread out very
slowly, such as the one in Figure 6-3, have a low standard deviation.
Numerically, the mean is simply the average outcome, a concept familiar
to most traders. To calculate the mean, we add up all the results and divide by
the total number of occurrences. Calculation of the standard deviation is not
quite so simple and will be discussed later. What is important at this point is
the interpretation of these numbers, in particular, what a mean and standard
deviation suggest in terms of likely price movement.
Let’s go back to Figure 6-2 and consider the troughs numbered 0 to 15 at
the bottom. We suggested that these numbers might represent the number of
heads resulting from 15 flips of a coin. Alternatively, they might represent the
number of times a ball goes to the right at each nail as it drops down through
the maze. The first trough is assigned 0 because any ball that ends there must
go left at every nail. The last trough is assigned 15 because any ball that ends
there must go right at every nail.
Suppose that we are told that the mean and standard deviation in Figure 6-2
are 7.50 and 3.00, respectively.2 What does this tell us about the distribution?
The mean tells us the average outcome. If we add up all the outcomes and
divide by the number of occurrences, the result will be 7.50. In terms of the
troughs, the average result will fall halfway between troughs 7 and 8. (Of course,
this is not an actual possibility. However, we noted in Chapter 5 that the average
outcome does not have to be an actual possibility for any one outcome.)
The standard deviation determines not only how fast the distribution
spreads out, but it also tells us something about the likelihood of a ball ending up in a specific trough or group of troughs. In particular, the standard deviation tells us the probability of a ball ending up in a trough that is a specified
distance from the mean. For example, we may want to know the likelihood of a
ball falling down through the maze and ending up in a trough lower than 5 or
higher than 10. The answer to this question depends on the number of standard
deviations the ball must move away from the mean. If we know this, we can determine the probability associated with that number of standard deviations.
The exact probability associated with any specific number of standard deviations can be found in most texts on statistics or probability. Alternatively,
such probabilities can be easily calculated in most commonly used computer
spreadsheet programs. For option traders, the following approximations will
be useful:

±1 standard deviation takes in approximately 68.3 percent (about
2/3) of all occurrences.
2 The reader who is familiar with the mean and standard deviation and who would like to check the arithmetic
will find that the actual mean and standard deviation are 7.49 and 3.02. For simplicity, we have rounded these to
7.50 and 3.00.
--- page 92 ---

V o l at i l i t y
75

±2 standard deviations takes in approximately 95.4 percent (about
19/20) of all occurrences.

±3 standard deviations takes in approximately 99.7 percent (about
369/370) of all occurrences.
Note that each number of standard deviations is preceded by a plus or
minus sign. Because normal distributions are symmetrical, the likelihood of
up movement and down movement is identical. The probability associated
with each number of standard deviations is usually given as a decimal value,
but a fractional approximation is often useful to traders, and this appears in
parentheses.
Now let’s try to answer our question about the likelihood of getting a
ball in a trough lower than 5 or higher than 10. We can designate the divider
between troughs 7 and 8 as the mean, 7½. If the standard deviation is 3, what
troughs are within one standard deviation of the mean? One standard deviation from the mean is 7½ ± 3, or 4½ to10½. Interpreting ½ as the divider
between troughs, we can see that troughs 5 through 10 fall within 1 standard
deviation of the mean. We know that one standard deviation takes in about
two-thirds of all occurrences, so we can conclude that out of every three balls
we drop into the maze, two should end up in troughs 5 through 10. Whatever is left over, one out of every three balls, will end up in one of the remaining troughs, 0 through 4 and 11 through 15. Hence, the answer to our
original question about the likelihood of getting a ball in a trough lower than
5 or higher than 10 is about 1 chance in 3, or about 33 percent. (The exact
answer is 100% – 68.3% = 31.7%.) This is shown in Figure 6-6.
Let’s try another calculation, but this time we can think of the problem as a
wager. Suppose that someone offers us 30 to 1 odds against dropping a ball into
the maze and having it end up specifically in troughs 14 or 15. Is this bet worth
making? One characteristic of standard deviations is that they are additive. In
our example, if one standard deviation is 3, then two standard deviations are
6. Two standard deviations from the mean is therefore 7½ ± 6, or 1½ to 13½.
We can see in Figure 6-6 that troughs 14 and 15 lie outside two standard deviations. Because the probability of getting a result within two standard deviations
is approximately 19 out of 20, the probability of getting a result beyond two
standard deviations is 1 chance in 20. Therefore, 30 to 1 odds may seem very
favorable. Recall, however, that beyond two standard deviations also includes
troughs 0 and 1. Because normal distributions are symmetrical, the chances of
getting a ball specifically in troughs 14 or 15 must be half of 1 chance in 20, or
about 1 chance in 40. At 30 to 1 odds, the bet must be a bad one because the
odds do not sufficiently compensate us for the risk involved.
In Chapter 5, we suggested that a truly accurate theoretical pricing model
would require us to assign probabilities to an infinite number of possible price
outcomes for an underlying contract. Then, if we multiply each price outcome
by its associated probability, we can use the results to calculate an option’s theoretical value. The problem is that an infinite number of anything is not easy to
work with. Fortunately, the characteristics of normal distributions are so well
known that formulas have been developed that facilitate the computation of
both the probabilities associated with every point along a normal distribution
--- page 93 ---

76
O P T I O N V O L AT I L I T Y A N D P R I C I N G
curve and the area under various portions of the curve. If we assume that prices
of an underlying instrument are normally distributed, these formulas represent
a unique set of tools to help us solve for an option’s theoretical value.
Louis Bachelier was the first to make the assumption that the prices of an
underlying contract are normally distributed. As we shall see, there are logical
problems with this assumption. Consequently, over the years, the assumption
has been modified to make it more consistent with real-world conditions. In its
modified form, it is the basis for many theoretical pricing models, including the
Black-Scholes model.
Forward Price as the Mean of a Distribution
If we decide to assign probabilities that are consistent with a normal distribution, how do we feed this distribution into a theoretical pricing model? Because
all normal distributions can be described by a mean and a standard deviation,
in some way we must feed these two numbers into our pricing model.
In Chapter 5, we suggested that any distribution ought to be centered
around the most likely underlying price at expiration. Although we cannot
Figure 6-6
0
1
2
3
4
5
6
7
8
9 10 11 12 13 14 15
mean
7.50
–1
st. dev.
4.50
–2
st. dev.
1.50
+2
st. dev.
13.50
+1
st. dev.
10.50
68%
95%
mean  =  7.50
standard deviation  =  3.00
± 1 st. dev.  =  68.3% (approx. 2/3)
± 2 st. dev.  =  95.4% (approx. 19/20)
± 3 st. dev.  =  99.7% (approx. 369/370)
--- page 94 ---

V o l at i l i t y
77
know exactly what that price will be, if we assume that no arbitrage opportunity exists in the underlying contract, a logical guess is the forward price. If we
make the assumption that the forward price represents the mean of a distribution, then in the long run, any trade made at the current underlying price will
just break even. The various forms of the Black-Scholes model differ primarily
in how they calculate the forward price. Depending on the type of underlying
contract, whether a stock, a futures contract, or a foreign currency, the model
takes the current underlying price, the time to expiration, interest rates, and, in
the case of stocks, dividends to calculate the forward price. It then makes this
the mean of the distribution.
Volatility as a Standard Deviation
In addition to the mean, to fully describe a normal distribution, we also need
a standard deviation. When we input a volatility into a theoretical pricing
model, we are actually feeding in a standard deviation. Volatility is just a trader’s term for standard deviation. Because the Greek letter sigma (σ) is the
traditional notation for standard deviation, in this text we will use the same
notation for volatility.
At this point, it will help if we assign a working definition to volatility,
although we will later modify this definition slightly. For the present, we will assume that the volatility we feed into a pricing model represents a one standard
deviation price change, in percent, over a one-year period. For example, consider
a contract with a one-year forward price of 100 and that we are told has a volatility of 20 percent. (We’ll discuss later where this number might come from.) With
a mean of 100 and a standard deviation of 20 percent, if we come back one year
from now, there is a 68 percent probability that the contract will be trading between 80 and 120 (100 ± 20%), a 95 percent probability that the contract will be
trading between 60 and 140 (100 ± 2 × 20%), and a 99.7 percent probability that
the contract will be trading between 40 and 160 (100 ± 3 × 20%). These are the
probabilities associated with one, two, and three standard deviations.
Instead of specifying the forward price, suppose that we are dealing with
a stock that is currently trading at $100 and that has the same 20 percent
volatility. In order to determine the one-year probabilities, we must first determine the one-year forward price because this represents the mean of the
distribution. If interest rates are  8 percent and the stock pays no dividends,
the one-year forward price will be $108. Now, a one standard deviation price
change is 20% × $108 = $21.60. Thus, one year from now, we would expect
the same stock to be trading between $86.40 and $129.60 ($108 ± $21.60)
approximately 68 percent of the time, between $64.80 and $151.20 ($108 ±
2 × $21.60) approximately 95 percent of the time, and between $43.20 and
$172.80 ($108 ± 3 × $21.60) approximately 99.7 percent of the time.
Returning to our contract with a forward price of 100, suppose that we
come back at the end of one year and find that the contract, which we thought
had a volatility of 20 percent, is trading at 35. Does this mean that the volatility of 20 percent was wrong? A price change of more than three standard deviations may be unlikely, but one should not confuse unlikely with impossible.
--- page 95 ---

78
O P T I O N V O L AT I L I T Y A N D P R I C I N G
Flipping a perfectly balanced coin 15 times may result in 15 heads, even though
the odds of this occurring are less than one chance in 32,000. If 20 percent
is the right volatility, the probability that the price will fall from 100 to 35 in
one year is less than one chance in 1,500. However, one chance in 1,500 is not
impossible, and perhaps this was the one time in 1,500 when the price did indeed end up at 35. Of course, it is also possible that we had the wrong volatility. But we can’t make that determination without looking at a large number of
price changes for the contract so that we have a representative price distribution.
Scaling Volatility for Time
Like interest rates, volatility is always expressed as an annualized number. If
someone says that interest rates are 6 percent, no one needs to ask whether that
means 6 percent per day, 6 percent per week, or 6 percent per month. Everyone
knows that it means 6 percent per year. The same is true of volatility.
We might logically ask what an annual volatility tells us about the likelihood of price changes over some shorter period of time. Although interest
rates are proportional to time (we simply multiply the rate by the amount of
time), volatility is proportional to the square root of time. To calculate a volatility, or standard deviation, over some period of time other than one year, we
must multiply the annual volatility be the square root of time, where the time
period t is expressed in years
t
Volatility
volatility
t
annual
=
×
Traders typically calculate volatility for an underlying contract by observing
price changes at regular intervals. Let’s begin by assuming that we plan to
observe price changes at the end of every day. Because there are 365 days
in a year, it might seem that prices can change 365 times per year. In this
text, though, we are focusing primarily on exchange-traded contracts. Because
most exchanges are closed on weekends and holidays, if we observe the price
of an underlying contract at the end of every day, prices cannot really change
365 times per year. Depending on the exchange, there are probably somewhere between 250 and 260 trading days in a year.3 Because we need the
square root of the number of trading days, for convenience, many traders
assume that there are 256 trading days in a year given that the square root of
256 is a whole number, 16. If we make this assumption, then
Volatility
volatility
1/256
volatility
1/16
volatility
16
daily
annual
annual
annual
=
×
=
×
=
To approximate a daily standard deviation, we can divide the annual volatility by 16.
Returning to our contract trading at 100 with a volatility of 20 percent,
what is a one standard deviation price change from one day to the next?
3 As markets around the world become more integrated, and with the advent of electronic trading, it may
become more difficult to determine exactly what fraction of a year one day represents. Depending on the
contract and exchange, in some cases it may be sensible to look at prices every day, 365 days per year.
--- page 96 ---

V o l at i l i t y
79
The answer is 20%/16 = 1¼%, so a one standard deviation daily price
change is 1¼% × 100 = 1.25. We expect to see a price change of 1.25 or less
approximately two trading days out of every three and a price change of 2.50
or less approximately 19 trading days out of every 20. Only one day in 20
would we expect to see a price change of more than 2.50.
We can do the same type of calculation for a weekly standard deviation.
Now we must ask how many times per year prices can change if we look at
prices once a week. There are no complete weeks when no trading takes place,
so we must make our calculations using all 52 trading weeks in a year. Therefore,
Volatility
volatility
1/52
volatility
1/7.2
volatility
7.2
weekly
annual
annual
annual
=
×
≈
×
=
To approximate a weekly standard deviation, we can divide the annual
volatility by 7.2. Dividing our annual volatility of 20 percent by the square
root of 52, or approximately 7.2, we get 20%/7.2 » 2.78. For our contract
trading at 100, we would expect to see a price change of 2.78 or less two weeks
out of every three, a price change of 5.56 or less 19 weeks out of every 20, and
only one week in 20 would we expect to see a price change of more than 5.56.
If we want to be as accurate as possible, when estimating a daily or weekly
standard deviation, we ought to begin by calculating the one-day or one-week
forward price. But for short periods of time, the forward price is so close to the
current price that most traders assume for convenience that a one-day or oneweek distribution is centered around the current price.
Suppose that a stock is trading at $45 per share and has an annual volatility
of 37 percent. What is an approximate one and two standard deviation price
range from one day to the next and from one week to the next? For one day, we
can divide the annual volatility by 16 (the square root of 256, the number of
trading days in a year)
$45
37%
16
$1.04
×
≈
A one and two standard deviation daily price range is approximately
$45 ± $1.04 ≈ $43.96 to $46.04  (one standard deviation)
$45 ± (2 × $1.04) ≈ $42.92 to $47.08  (two standard deviations)
For one week, we can divide the annual volatility by 7.2 (the square root of 52,
the number of trading weeks in a year)
$45
37%
7.2
$2.31
×
=
A one and two standard deviation weekly price range is approximately
$45 ± $2.31 ≈ $42.69 to $47.31  (one standard deviation)
$45 ± (2 × $2.31) ≈ $40.38 to $49.62  (two standard deviations)
When we scale volatility for time, the same probabilities still apply. Approximately
68 percent of the occurrences will fall within one standard deviation. Approximately 95 percent of the occurrences will fall within two standard deviations.
