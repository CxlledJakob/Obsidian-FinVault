# Option Volatility and Pricing_ Advanced Trading Strategies -- Sheldon Natenberg -- 2nd ed, 2014 -- McGraw Hill Professional -- isbn13 9780071818773 -- 6a48d008bd9beef283debf7bad0b2e4a -- Anna’s Archive.pdf — pages 343–362

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
--- page 344 ---

H e d g i n g w i t h O p t i o n s 	 327
Figure 17-3  Long an underlying position and short a covered call.
Exercise
price
Long
underlying
Short call
Combined position
(synthetic short put)
Higher underlying prices
Lower underlying prices
Current
underlying
price
Premium received for the call
Figure 17-4  Short an underlying position and short a covered put.
Exercise
price
Short
underlying
Short put
Combined position
(synthetic short put)
Higher underlying prices
Lower underlying prices
Current
underlying
price
Premium received for the put
Selling a covered call against a long stock position is one of the most popular hedging strategies in equity option markets. When executed all at one
time—buying stock and simultaneously selling a call on the stock—the strategy
is referred to as a buy/write. The December 105 buy/write consists of buying
--- page 345 ---

328
O P T I O N V O L AT I L I T Y A N D P R I C I N G
one stock contract (usually 100 shares) and simultaneously selling a December
105 call. As with any spread, it can be quoted as a single price (the stock price –
the call price) and executed with a single counterparty. With a stock trading at
100 and the December 105 call trading at 2.00, the December 105 buy/write is
trading at 98.00. The price quoted by a market maker might be 97.90 – 98.10.
In total, the market maker is willing to buy the stock and sell the call for 97.90.
He is willing to sell the stock and buy the call for 98.10.
Buy/writes are such common strategies that some exchanges publish indexes reflecting the performance of the strategy, usually against a major
stock index. The Chicago Board Options Exchange BuyWrite Index (BXM)
reflects the performance of a strategy consisting of buying a Standard and
Poor’s (S&P) 500 Index (SPX) portfolio and each month selling a slightly outof-the-money one-month S&P 500 Index call option.1
A covered write can also be used to set a target price for either buying or
selling an underlying instrument. An investor who owns a stock may decide
that if the stock reaches a certain price, he will be willing to sell. By selling a
call with an exercise price equal to the target price, the investor has effectively
locked in the sale if the stock reaches the exercise price. If the stock does not
reach the exercise price, the investor still gets to keep the premium received
from the sale of the call.
Similarly, an investor who is willing to buy stock if the price declines by
some given amount can sell a put with an exercise price equal to the target purchase price. If the stock falls below the exercise price, the investor will be assigned on the put, forcing him to purchase the stock. But that was his original
intention. If the stock fails to fall below the exercise price, the investor gets to
keep the premium received from the sale of the put. This strategy of selling
puts to trigger the purchase of stock is often used by companies that want to
initiate a buy-back program for their stock. By selling puts with exercise prices
equal to the target buy-back price, the company either buys back its own stock
or profits by the amount of the put premium.
The primary difference between selling a call to set a sale price and selling
a put to set a purchase price is the way in which the trade is secured. The sale
of a call is secured with ownership of the stock. But the sale of the put must be
secured with enough cash to support the purchase of the stock should the put
be exercised. The sale of a cash-secured put requires the investor to keep on deposit cash equal to the exercise price of the put. If the put is European with no
possibility of early exercise, the investor can keep on deposit cash equal to the
present value of the exercise price
+ ×
X
r
t
1
The purchase of a protective option and the sale of a covered option are the
two most common hedging strategies involving options. If given a choice between
these strategies, which one should a hedger choose? In theory, the hedger ought to
base his decision on the same criteria used by a trader: price versus value. If option
1 A complete description of the CBOE Buy/Write Index, as well as its historical performance, can be found at
http://www.cboe.com/micro/bxm/.
--- page 346 ---

H e d g i n g w i t h O p t i o n s 	 329
prices seem low, the purchase of a protective option makes sense. If option prices
seem high, the sale of a covered option makes sense. From a trader’s point of
view, low or high is typically expressed in terms of implied volatility. By comparing
implied volatility with the expected volatility over the life of the option, a hedger
ought to be able to make a sensible determination as to whether he wants to buy
or sell options. Of course, he is still left with the question of which exercise price
to choose. This will depend on the amount of adverse or favorable movement the
hedger foresees, as well as the risk he is willing to accept if he is wrong.
While theoretical considerations often play a role in a hedger’s decision,
these may be less important than practical considerations. If a hedger knows
that a move in the underlying contract beyond a certain price will represent a
threat to his business, then the purchase of a protective option at that exercise
may be the most sensible strategy regardless of whether the option is theoretically overpriced.2
Many hedgers seem to have an aversion to buying protective options. “Why
should I pay for an option when I will probably lose the premium?” This is, indeed, true. Most protective options do expire out of the money. The reasoning,
however, seems illogical when one considers that most people willingly purchase
insurance to protect their personal property. And the great majority of insurance policies expire without claims ever being made against them: houses do not
burn down; people do not die; and cars are not stolen. This is the reason insurance companies make a profit. But most people do not buy insurance to make
a profit. They do so for the peace of mind that the insurance policy affords.
The same philosophy ought to apply to the purchase of options. If a hedger
needs well-defined protection, the purchase of an option may be the best choice
regardless of the fact that the option will most often expire worthless.
Collars
A hedger may want the limited risk afforded by the purchase of a protective
option but may also be reluctant to pay the premium associated with such a
strategy. What can he do? A collar involves simultaneously purchasing a protective option and selling a covered option against a position in an underlying
contract.3 Collars are popular hedging tools because they offer known protection at a low cost. At the same time, they still allow a hedger to participate, at
least partially, in favorable market movement. With an underlying stock trading
at 100, a hedger with a long position might choose to buy a 95 put and at the
same time sell a 105 call. The hedger is insulated from any fall in price below
95 because he can then exercise his put. At the same time, he can participate in
any upward move up to 105.
The terms long and short, when applied to collars, typically refer to the
underlying position. A long underlying position together with a protective put
2 Of course, if options seem wildly overpriced, a hedger may be reluctant to buy a protective option. But this is
an unlikely scenario. If option prices are high, there is usually a valid reason.
3 The collar strategy goes by a wide variety of names, including fence, tunnel, cylinder, range forward, or split-strike
conversion.
--- page 347 ---

330
O P T I O N V O L AT I L I T Y A N D P R I C I N G
and covered call is a long collar. A short underlying position together with a
protective call and covered put is a short collar. The characteristics of a collar
are shown in Figures 17-5 and 17-6. Because every contract can be expressed
as a synthetic equivalent, we can see that a long collar (Figure 17-5) is simply a
bull vertical spread, while a short collar (Figure 17-6) is simply a bear vertical
spread. Both strategies have limited risk and limited reward.
Because a collar is a vertical spread, it will have the risk characteristics
described in Chapter 12. A long collar will always have a positive delta; a
short collar will always have a negative delta.  The gamma, theta, and vega
will be determined by the choice of exercise prices. If the underlying price
is closer to the protective option, the position will usually have a positive
gamma, negative theta, and positive vega. If the underlying price is closer to
the covered option, the position will usually have a negative gamma, positive
theta, and negative vega. Unless one option is much further out of the money
than the other, these risk measures are likely to be similar, resulting in only a
small gamma, theta, and vega position. A hedger might also choose exercise
prices such that the collar will be approximately neutral with respect to the
gamma, theta, or vega.
Collars are also popular because the sale of the covered option may offset some or all of the cost of the protective option. When the price of the protective option is greater than the price of the covered option, as it is in Figure
17-5, the midsection of the combined position will fall below the profit and
loss (P&L) graph for the underlying position. When the price of the protective
Figure 17-5  Long collar (long an underlying contract, long a protective put, short a
covered call).
Long
underlying
Long put
Short call
Higher
exercise
price
Lower
exercise
price
Put price
Call price
Combined position
(synthetic short put)
Higher underlying prices
Lower underlying prices
Current
underlying
price
--- page 348 ---

H e d g i n g w i t h O p t i o n s 	 331
option is less than the price of the covered option, as it is in Figure 17-6, the
midsection of the combined position will be above the P&L graph for the underlying position. If the price of the protective option and the covered option
are the same, the strategy becomes a zero-cost collar. A summary of basic hedging strategies is given in Figure 17-7.
position
hedging strategy
advantages
disadvantages
long underlying sell a future or forward no downside risk
no upside profit potential
buy a protective put
limited downside risk;
unlimited upside profit potential
cost of the option
sell a covered call
partial downside protection
equal to the price of the call
unlimited downside risk;
limited upside profit
potential
long collar
(long a protective put/
short a covered call)
limited downside risk
limited upside profit
potential
short underlying buy a future or forward no upside risk
no downside profit potential
buy a protective call
limited upside risk;
unlimited upside profit potential
cost of the option
sell a covered put
partial upside protection
equal to the cost of the put
unlimited upside risk;
limited downside profit
potential
short collar
(long a protective call/
short a covered put)
limited upside risk
limited downside profit
potential
Figure 17-7  Summary of basic hedging strategies.
Figure 17-6  Short collar (short an underlying contract, long a protective call, short a
covered put).
Short
underlying
Short put
Long call
Higher
exercise
price
Lower
exercise
price
Put price
Call price
Combined position
(bear vertical spread)
Higher underlying prices
Lower underlying prices
Current
underlying
price
--- page 349 ---

332
O P T I O N V O L AT I L I T Y A N D P R I C I N G
Complex Hedging Strategies
Because most hedgers are not professional option traders and have neither the
time nor the desire to carefully analyze option prices, simple hedging strategies
involving the purchase or sale of single options are the most widely used. However, if one is willing to do a more detailed analysis of options, it is possible to
construct a wide variety of hedging strategies that involve both volatility and
directional considerations. To do this, a hedger must be familiar with volatility
and its impact on option values, as well as the delta as a measure of directional
risk. The hedger can then combine his knowledge of options with the practical
considerations of hedging.
As a first step in choosing a strategy, a hedger might consider the following:
1.	 Does the hedge need to offer protection against a worst-case scenario?
2.	 How much of the current directional risk should the hedge eliminate?
3.	 What additional risks is the hedger willing to accept?
A hedger who needs disaster insurance to protect against a worst-case scenario
only has a choice of which option(s) to buy. Even so, he still needs to decide
which exercise price to purchase and how many options. With a long position in an underlying contract currently trading at 100, a hedger decides to
buy a put because he needs to limit the downside risk to some known and fixed
amount. Which put should he buy?
If the hedger has determined that options are generally overpriced (i.e.,
implied volatility seems high), any option purchase will clearly be to the hedger’s disadvantage. If his sole purpose is to hedge his downside risk without regard to upside profit potential, he ought to avoid options and hedge his position
in the futures or forward market. If, however, he still wants upside profit potential, he must ask himself how much of a long position he wants to retain. If he
is willing to retain 50 percent of his current long position, he ought to purchase
puts with a total delta of –50. He can do this by purchasing one at-the-money
put with a delta of –50 or several out-of-the-money puts whose deltas add up
to –50. In a high-implied-volatility market, however, it is usually best to buy as
few options as possible and sell as many options as possible. (This is analogous
to constructing a ratio spread.) Hence, purchasing one put with a delta of –50
will be less costly, theoretically, than purchasing several puts with a total delta
of –50. If the hedger wants to eliminate even more of the directional risk, say,
75 percent, under these circumstances, he will be better off purchasing one put
with a delta of –75.
All other factors being equal, in a high-implied-volatility market, a hedger should
buy as few options as possible and/or sell as many options as possible. Conversely,
in a low-implied-volatility market, a hedger should buy as many options as possible
and/or sell as few options as possible.
This means that if all options are overpriced (i.e., implied volatility seems
high) and the hedger decides that he is willing to accept the unlimited downside
--- page 350 ---

H e d g i n g w i t h O p t i o n s 	 333
risk that goes with the sale of a covered call, in theory, he ought to sell as many
calls as possible to reach his hedging objectives. If he is trying to hedge 50 percent
of his long underlying position, he can do a ratio write by selling several out-of-themoney calls with a total delta of 50 rather than selling a single at-the-money call
with a delta of 50.
There is an obvious disadvantage if one sells multiple calls against a single
long underlying position. Now the hedger not only has the unlimited downside risk that goes with a covered call position, but he also has unlimited upside
risk because he has sold more calls than he can cover with the underlying. If
the market moves up enough, he will be assigned on all the calls. Most hedgers want to restrict their unlimited risk to one direction, usually the direction of
their natural position. A hedger with a long underlying position may be willing
to accept unlimited downside risk, but he is probably unwilling to accept unlimited upside risk. A hedger with a short underlying position may be willing to
accept unlimited upside risk, but he is probably unwilling to accept unlimited
downside risk. A hedger who constructs a position with unlimited risk in either
direction is presumably taking a volatility position. There is nothing wrong with
this because volatility trading can be highly profitable. But a true hedger ought
not lose sight of what his ultimate goal is—to protect an existing position and to
keep the cost of this protection as low as possible.
A hedger can also protect a position by constructing one-to-one volatility
spreads with deltas that yield the desired amount of protection. A hedger who
wants to protect 50 percent of a short underlying position can buy or sell calendar spreads or butterflies with a total delta of +50. Such spreads offer partial protection within a range. The entire position still has unlimited upside risk
but also retains unlimited downside profit potential. Such volatility spreads also
give the hedger the choice of buying or selling volatility. If implied volatility is
generally low, with the underlying market currently at 100, the hedger might
protect a short underlying position by purchasing a 110 call calendar spread
(i.e., purchase a long-term 110 call, sell a short-term 110 call). This spread has
a positive delta and is also theoretically attractive because the low implied volatility makes a long calendar spread relatively inexpensive. If the 110 call calendar spread has a delta of +25, to hedge 50 percent of his directional risk, the
hedger can buy two spreads for each short underlying position. Conversely, if
implied volatility is high, the hedger can consider selling calendar spreads. Now
he will have to choose a lower exercise price to achieve a positive delta. If he
sells the 90 call calendar spread (i.e., purchase a short-term 90 call, sell a longterm 90 call), he will have a position with a positive delta and a positive theoretical edge. If he wants to protect 75 percent of his position and the spread has
a delta of +25, he can sell the spread three times for each underlying position.
(See Chapter 11 for characteristics of calendar spreads and butterflies.)
A hedger can also buy or sell vertical spreads to achieve a desired amount
of protection. Depending on whether options are generally underpriced or
overpriced (i.e., implied volatility is excessively low or high), the hedger will
work around the at-the-money option. With the underlying market currently
at 100, the hedger who wants to protect a long position can execute a bear vertical spread (i.e., sell the lower exercise price, buy the higher exercise price).
--- page 351 ---

334
O P T I O N V O L AT I L I T Y A N D P R I C I N G
If implied volatility is high, he will prefer to sell an at-the-money option and
buy an option at a higher exercise price. If implied volatility is low, he will prefer to buy an in-the-money option and sell an option at a lower exercise price.
Each spread will have a negative delta but will also have a positive theoretical
edge because the at-the-money option is the most sensitive to changes in volatility. (See Chapter 12 for characteristics of vertical spreads.)
As is obvious, using options to hedge a position can be just as complex as
using options to construct trading strategies. Many factors go into the decisionmaking process. When a potential hedger is confronted for the first time with
the multitude of possible strategies, he can understandably feel overwhelmed,
to the point where he decides to abandon options completely. Perhaps a better approach is to consider a limited number of strategies (perhaps four or five)
that make sense and compare the various risk-reward characteristics of the
strategies. Given the hedger’s general market outlook and his willingness or
unwillingness to accept certain risks, it should then be possible to make an informed decision.
Hedging to Reduce Volatility
In addition to protecting a position against an adverse move in the underlying contract, hedging strategies have an additional important advantage—
they tend to reduce the volatility of a position. To understand why this may be
important, consider a portfolio manager who generates the following annual
returns over a period of five years:
+19%  –14%  +27%  –9%  +22%
His average annual return is
(19% – 14% + 27% – 9% + 22%)/5 = +9%
Now consider a second portfolio manager who generates these annual returns:
+25%  –20%  –23%  +44  +24
His average annual return is
(25% – 20% – 23% + 44% + 24%)/5 = +10%
Finally, a third portfolio manager generates these returns:
+35%    +15    –35    +65%    –20%
His average annual return is
(35% + 15% – 35% + 65% – 20%)/5 = +12%
Portfolio Manager 3 trumpets his average annual return of 12 percent compared with Portfolio Managers 1 and 2, with returns of only 9 and 10 percent.
Clearly, we ought to invest our money with Portfolio Manager 3. Or should we?
--- page 352 ---

H e d g i n g w i t h O p t i o n s 	 335
Perhaps we should consider not only what is happening each year but also how
each portfolio performs over the entire five-year period. We can do this by taking the product of all the annual changes for each portfolio:

Portfolio 1:	 1.19 × 0.86 × 1.27 × 0.91 × 1.22 = 1.4429 (up 44.29%)

Portfolio 2:	 1.25 × 0.80 × 0.77 × 1.44 × 1.24 = 1.3749 (up 37.49%)

Portfolio 3:	 1.35 × 1.15 × 0.65 × 1.65 × 0.80 = 1.3320 (up 33.20%)
Even though Portfolio Manager 3 had the best average annual return, his
portfolio fared the worst. Portfolio Manager 1, with the lowest annual return,
fared the best, making 11 percent more over the five-year period than Portfolio Manager 3.
The explanation for this seemingly unexpected result has to do with the
volatility, or standard deviation, of the returns. The returns for Portfolio Manager 3 fluctuated wildly from a high of +65 percent to a low of –35 percent.
The returns for Portfolio Manger 1 fluctuated much less, between +27 percent
and –14 percent. The greater volatility seemed to reduce the total return.
The results for each portfolio manager are summarized in Figure 17-8. We
have also added a very boring Portfolio Manager 4, who plods along with a return of exactly 8 percent each year for the five-year period. In spite of having
the lowest average return, his portfolio performed the best, gaining 46.93 percent over the entire period.
Our example does not mean that high volatility is unacceptable. A portfolio
manager with highly volatile returns may still be preferable if his average return
is also commensurably higher. This tradeoff between returns and volatility is often expressed by the Sharpe ratio, originally suggested by William Sharpe in 19664
Average return/standard deviation of returns
The greater the Sharpe ratio, the more favorable the tradeoff between risk (volatility) and reward (returns). The standard deviation and the Sharpe ratio for
all four portfolio managers are also given in Figure 17-8.
4 The returns used to calculate the Sharpe ratio are sometimes expressed as the returns in excess of some
benchmark, such as a risk-free Treasury instrument.
year 1
returns
year 2
returns
year 3
returns
year 4
returns
year 5
returns
average
annual
return
total
5-year
return
standard
deviation
Sharpe
ratio
Portfolio Manager 1:
+19%
−14%
+27%
−9%
+22%
+9%
+44.29%
+17.01%
.5291
Portfolio Manager 2:
+25%
−20%
−23%
+44%
+24%
+10%
+37.49%
+26.71%
.3744
Portfolio Manager 3:
+35%
+15%
−35%
+65%
−20%
+12%
+33.20%
+36.28%
.3308
Portfolio Manager 4:
+8%
+8%
+8%
+8%
+8%
+8%
+46.93%
0
----
Figure 17-8  The greater the volatility, the lower the total return.
--- page 353 ---

336
O P T I O N V O L AT I L I T Y A N D P R I C I N G
Portfolio Insurance
Imagine that we hold a long position in an underlying asset such as stock and
that we would like to protect our position against a possible decline in price
over some period of time. One possible strategy is to purchase a protective put.
Unfortunately, when we go into the market to purchase the put, we find that no
market exists for options on our stock. What can we do?
If we were really able to purchase a put, our position would be
Long stock + long put
But we know that a long underlying position together with a long put is equivalent to a long call. What we really want is a long call position with the same
exercise price and expiration date as the put that we wanted but were unable
to buy.
What would be the characteristics of this call? We can determine this by
using a theoretical pricing model. To do this, we need the basic inputs into the
theoretical pricing model:

Exercise price

Time to expiration

Underlying stock price

Interest rate

Volatility
Because we are not dependent on listed exercise prices and expiration dates
(because none exist), the exercise price and expiration date can be of our own
choosing. We can determine the stock price and interest rate from current market conditions. Only the volatility cannot be directly observed in the marketplace. But, if we have a database of historical price changes for the stock, we
may be able to make a reasonable estimate of the stock’s volatility.
Suppose that we feed all the inputs into a theoretical pricing model and
determine that our intended call has a delta of 75. To replicate the call position, we need to own 75 percent of the underlying contract. We can achieve
this by selling off 25 percent of our holdings in the stock. If we originally
owned 1,000 shares, we need to sell 250 shares, leaving us with a long position
of 750 shares.
Now suppose that at some later date we look at the new market conditions, recalculate the delta of the call, and find that it is now 60. To achieve the
desired delta position, we must now sell off an additional 15 percent of our
original holdings, or 150 shares. We are now long 600 shares of stock.
Suppose that we continue this process of periodically calculating the
delta from current market conditions and buying or selling some percentage of our original holding in the underlying stock to achieve a position with
the same delta as the presumed call option. Finally, suppose that at the target
expiration date we buy back a sufficient amount of the stock so that we have
100 percent of our original holding. What should be the result of this entire
process?
--- page 354 ---

H e d g i n g w i t h O p t i o n s 	 337
We are essentially going through the dynamic hedging process described in
Chapter 8. Whereas in Chapter 8 we used dynamic hedging to capture the difference between an option’s price in the marketplace and its theoretical value,
in our current example, we cannot profit from a mispriced option because no
option exists. But we can replicate the characteristics of the option to achieve a
desired option position.
In Chapter 8 we presented a stock option example and a futures option
example. In the stock option example, we bought a call at a price that was less
than its theoretical value and then sold the call, through the dynamic hedging
process, at a price that was equal to its theoretical value. In the futures option
example, we sold a put at a price that was greater than its theoretical value and
then bought the put, through the dynamic hedging process, at a price that was
equal to its theoretical value. In both examples, we ended up with a profit equal
to the difference between the option’s price and its theoretical value.
Portfolio insurance, or option replication, is a method by which the dynamic
hedging process is used to create a position with the same characteristics as an
option. In theory, the method should achieve the same results as buying a protective option but without actually purchasing the option. Portfolio insurance
can be used by a fund manager to insure the value of the securities in a portfolio against a drop in value. If a manager has a portfolio of securities currently
valued at $100 million and wants to insure the value of the portfolio against
a drop in value below $90 million, he can either buy a $90 million put or replicate the characteristics of a $90 million call. If he is unable to find someone
willing to sell him a $90 million put, he can evaluate the characteristics of the
$90 million call and continuously buy or sell a portion of his portfolio required
to replicate the call position. In effect, he has created his own put.
Portfolio insurance strategies were widely used by fund managers prior
to the stock market crash of 1987, especially by managers with a portfolio that tended to track a major index. If the portfolio manager wanted to
buy protective puts but also believed that the prices of puts were inflated, he
could create the puts himself at the “correct” theoretical value through the
dynamic hedging process. Instead of buying or selling a portion of the portfolio, which could be expensive in terms of transaction costs, the portfolio
manager could mimic the delta adjustments by buying or selling index futures to increase or reduce the total value of the portfolio. In return for a fee,
firms that marketed portfolio insurance strategies assumed the responsibility
of determining the characteristics of the option that the portfolio manager
wanted to purchase by estimating the correct volatility and choosing the most
appropriate option pricing model.5 Some portfolio insurance firms generated
additional fees by acting as a broker and executing the necessary adjustments
in the index futures market.
Unfortunately, following the crash of 1987, practitioners came to realize
that portfolio insurance would only achieve the desired results if the inputs into
5 The firm most closely associated with portfolio insurance prior to the crash of 1987 was Los Angeles–based
Leland, O’Brien, Rubinstein (with principals Hayne Leland, John O’Brien, and Mark Rubinstein).
--- page 355 ---

338
O P T I O N V O L AT I L I T Y A N D P R I C I N G
the model were correct and the model itself was based on realistic assumptions.6
No one foresaw the dramatic increase in volatility resulting from the crash, so
the volatility input that was being used was clearly incorrect. At the same time,
many of the model assumptions about dynamic hedging seemed to be violated
in the real world. The upshot was that the cost of replicating an option through
the dynamic hedging process became much more expensive than anyone had
anticipated. As a result, portfolio insurance strategies fell out of favor with most
fund managers.
6 Some studies have suggested that the dynamic hedging required to implement portfolio insurance exacerbated the stock market crash of October 19, 1987. Because of the dramatic drop in the stock market, portfolio insurers were required to sell ever larger numbers of index futures contracts, creating a cascading effect in
the market.
--- page 356 ---

339
The Black-Scholes
Model
Because of its importance as a foundation of option pricing theory, as well as
its widespread use by traders, it will be worthwhile to take a closer look at the
Black-Scholes model.1 The discussion in this chapter is not meant to be a rigorous or detailed derivation of the model, which is better suited to a university
textbook or to a class in financial engineering. Rather, we hope to present a
more intuitive discussion of the workings of the model, as well as some observations on the values generated by the model.
Initially, rather than calculating the theoretical value of an option, Black
and Scholes tried to answer this question: if the stock price moves randomly
over time, but in a manner that is consistent with a constant interest rate and
volatility, what must be the option price after each moment in time such that an
option position that is correctly hedged will just break even? The answer to this
question resulted in rather intimidating-looking equation
rS C
S
S
C
S
C
t
rC
1
2
2
2
2
2
σ
∂
∂
+
∂
∂
+ ∂
∂
=
Although this equation might look mysterious to many readers, it is just a mathematician’s way of expressing how changes in one set of variables—stock price
S and time t—affect the value of something else, a call C. To determine the exact effect caused by changes in the variables, one must solve the equation.
Note that we did not refer to the volatility σ and interest rate r as variables.
In the Black-Scholes equation, only the stock price and time are changing. As
inputs into the model, the volatility and interest rate will affect the value of the
1 The Black-Scholes model is sometimes referred to as the Black-Scholes-Merton model because Robert Merton,
originally associated with the Massachusetts Institute of Technology, contributed significantly to the theory of
option pricing. Merton and Scholes were jointly awarded the Nobel Prize in Economics in 1997 for their work
on option pricing. Fischer Black, sadly, died in 1995.
18
--- page 357 ---

340
O P T I O N V O L AT I L I T Y A N D P R I C I N G
option. But once they have been chosen, they are assumed to remain constant
over the life of the option. This is consistent with the dynamic hedging examples in Chapter 8. Over the life of an option, we assumed that only the underlying price and time were changing. Everything else remained constant.
We have already encountered several of the components of the Black-
Scholes equation in slightly different form. The terms
C
S
C
S
C
t
,
,
and
2
2
∂
∂
∂
∂
∂
∂
are the more formal mathematical notation for the option’s delta (Δ), gamma
( Γ ), and theta (Θ). The Black-Scholes equation states that changes in an option’s value depend on the sensitivity of the option to changes in the stock price
(the delta), the sensitivity of the option’s delta to changes in the stock price (the
gamma), and the sensitivity of the option to the passage of time (the theta).
Of course, the equation also includes volatility and interest-rate components. The interest-rate component plays two roles. First, because the Black-
Scholes model values options from the forward price, the interest rate takes us
from the spot price to the forward price (assuming that the stock pays no dividend). This spot-to-forward relationship appears in the equation as
rS
Second, the Black-Scholes equation initially gives us the expected value
of the option as time passes. If we want to determine the option’s theoretical
value, we must discount the expected value backwards to get its present value.
This expected-value-to-present-value relationship appears in the equation as
rC
Finally, there is a volatility component. The rate at which the delta changes
depends not only on the gamma but on the speed at which the stock price is
changing. The speed is expressed as a volatility or standard deviation σ. The volatility component and its effect on the gamma appear in the Black-Scholes equation as
S
C
S
S
1
2
1
2
2
2
2
2
2
2
σ
σ
∂
∂
=
Γ
We will not go into the formal derivation of the Black-Scholes equation in this
text because it can be mathematically complex. But we might note that there
is some similarity between the Black-Scholes equation and the method used in
Chapter 7 to estimate the change in an option’s value as the underlying price
changes from S1 to S2. To approximate this change, we used the average delta
over the price range
(S1 – S2) × Δ + (S1 – S2)2 × Γ/2 = (S1 – S2) × Δ + ½ (S1 – S2)2 × Γ
Recalling that
C
S
C
S
and
2
2
∂
∂
∂
∂
--- page 358 ---

T h e B l a c k - S c h o l e s M o d e l 	 341
represent the delta and gamma, we can see that there is a similarity between
this relationship and the first two terms of the Black-Scholes equation.
(S1 – S2) × Δ + ½(S1 – S2)2 × Γ
rS C
S
S
C
S
1
2
2
2
2
2
σ
∂
∂
+
∂
∂
The primary differences are the interest-rate component attached to S (the
stock price must move from spot to forward) and the volatility component attached to the gamma. Although we assumed a discrete price change from S1
to S2, the Black-Scholes equation assumes an infinitesimally small, or instantaneous, price change.
This is, admittedly, a very simplistic attempt to explain the roles played by
the various components in the Black-Scholes equation. However, even for someone who fully understands the model, being able to write out the equation does
not necessarily yield a value. The real goal is to solve the equation so that it is possible to calculate the exact value of an option.
The solution to the Black-Scholes equation yields the well-known Black-
Scholes model: if

C = theoretical value of a European call

S = the price of a non-dividend-paying stock

X = exercise price

t = time to expiration, in years

σ = annual standard deviation (volatility) of the stock price, in percent

r = annual interest rate

ln = the natural logarithm

e = the exponential function

N = the cumulative normal distribution function
then
C = SN(d1) –Xe–rtN(d2)
where
d
S X
r
t
t
ln( /
)
/2
1
2
σ
σ
(
)
=
+
+


and
d
S X
r
t
t
d
t
ln( /
)
/2
2
2
1
σ
σ
σ
(
)
=
+
+

=
−
It may not be immediately apparent what the values in the Black-Scholes
model represent, but one starting point is put-call parity, discussed in Chapter 15
C
P
F
X
r
t
1
−
=
−
+ ×
If the underlying contract is a non-dividend-paying stock, the forward price is
F = S × (1 + r × t)
--- page 359 ---

342
O P T I O N V O L AT I L I T Y A N D P R I C I N G
Substituting this into the put-call parity relationship gives us
−
=
+ ×
−
+ ×
=
−+ ×
C
P
S
r
t
X
r
t
S
X
r
t
(1
)
1
1
In our examples thus far, we have used simple interest. If, instead, we use
continuous interest, rather than dividing by 1 + r × t, we can multiply by e–rt.
This gives us
C – P = S – Xe–rt
Because a put can never be worth less than 0, we know from Chapter 16 that
the lower arbitrage boundary for a European call option on stock is the greater
of either 0 or
S – Xe–rt
This expression looks similar to the Black-Scholes value for a call option, but
without the terms N(d1) and N(d2) attached to S and Xe–rt, respectively. What do
N(d1) and N(d2) represent?
In Chapter 5, we proposed a very simple method for evaluating options by
considering a series of underlying prices at expiration and assigning probabilities to each of those prices. Using this approach, the expected value for a call
option is the sum of the intrinsic values multiplied by the probability associated
with each underlying price
p
S
X
max(
,0)
i
i
i
n
1∑
−
=
To determine the option’s intrinsic value, we combined the underlying price
and exercise price into one expression (Si – X ).
The Black-Scholes model takes a slightly different approach by separating
the underlying price and exercise price into two distinct components and then
asking two questions:
1.	 If held to expiration, what is the average value of all the stock above
the exercise price?
2.	 If held to expiration, what is the likelihood that the owner of an option
will end up paying the exercise price?
If we can answer these questions, the difference between the average value
of the stock above the exercise price and the likelihood of paying the exercise
price should equal the option’s expected value.
To help explain the approach taken by Black and Scholes, let’s consider a
discrete distribution of stock prices at expiration, but one that more closely resembles a lognormal distribution with an extended right tail. Such a distribution,
resulting from a total of 153 occurrences, is shown in Figure 18-1. Using this distribution, how might we evaluate a call option with an exercise price of 12½?
First, we must determine the value of all stock above 12½, that is, the value
resulting from all occurrences that fall into troughs 13 through 27. The number
of occurrences and the value of the occurrences in each trough are as follows:
--- page 360 ---

T h e B l a c k - S c h o l e s M o d e l 	 343
Trough
Number of Occurrences
Stock Value
13
11
143
14
  9
126
15
  8
120
16
  7
113
17
  6
102
18
  5
  90
19
  4
  76
20
  3
  60
21
  2
  42
22
  2
  44
23
  1
  23
24
  1
  24
25
  1
  25
26
  0
   0
27
  0
   0
Total
60
987
The average value of all stock above the exercise price of 12½ is the total value,
987, divided by the total number of occurrences, 153
987/153 = 6.45
Figure 18-1
0
1
2
3
4
5
6
7
8
9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27
12½
0 1
1
2
4
6
8 10 12 13 13 12 11 11 9
8
7
6
5
4
3
2
2
1
1
1
0
0
Number of occurrences:
Total cumulative occurrences above 12½:
20
35
46
53
57
59
60
11
28
41
50
55
58
60
60
Value of occurrences above 12½:
(number of occurrences multiplied
by the trough number)
126
112
90
60
44
24
0
143
120
102
76
42
23
25
0
Total cumulative value above 12½:
269
501
703
839
925
972
997
143
389
613
779
881
948
997
997
--- page 361 ---

344
O P T I O N V O L AT I L I T Y A N D P R I C I N G
Next, we need to determine the likelihood that we will pay the exercise
price of 12½. There are 60 occurrences where the option is in the money (the
stock price is above 12½), but there are a total of 153 occurrences. The likelihood that we will pay the exercise price is
60/153 = 0.392
The average payout resulting from exercise of the option 0.392 × 12½ = 4.90.
In the Black-Scholes model, the average value of all stock above the exercise price is given by SertN(d1), where Sert is the forward price of the stock. The
average amount we will have to pay is given by XN(d2). The expected value for
a call option is the difference between these two numbers
SertN(d1) – XN(d2) = 6.45 – 4.90 = 1.55
These terms are slightly different from the terms that appear in the model,
SN(d1) and Xe–rtN(d2), but we will show shortly how SertN(d1) becomes SN(d1) and
how XN (d2) becomes Xe–rtN(d2).
We can confirm that 1.55 is the correct value (with slight rounding error)
by returning to our original approach of adding up the intrinsic values multiplied by their probabilities (the number of occurrences divided by 153).
Trough
Intrinsic Value of
the 12½ Call
Number of
Occurrences
Probability
Option Value
13
0.5
11
0.0719
0.0359
14
1.5
9
0.0588
0.0882
15
2.5
8
0.0523
0.1307
16
3.5
7
0.0458
0.1601
17
4.5
6
0.0392
0.1765
18
5.5
5
0.0327
0.1797
19
6.5
4
0.0261
0.1699
20
7.5
3
0.0196
0.1471
21
8.5
2
0.0131
0.1111
22
9.5
2
0.0131
0.1242
23
10.5
1
0.0065
0.0686
24
11.5
1
0.0065
0.0752
25
12.5
1
0.0065
0.0817
26
13.5
0
0
0
27
14.5
0
0
0
Total option
expected value:
1.5489
This is essentially the approach taken by the Black and Scholes. The primary
difference is that the Black-Scholes model, rather than using discrete outcomes
as we did, assumes a continuous lognormal distribution.
--- page 362 ---

T h e B l a c k - S c h o l e s M o d e l 	 345
n(x ) and N(x )
Before continuing, it will be useful to define two important probability functions—n(x) and N(x). In this chapter and in previous discussions of volatility, we
have often referred to the concept of a bell-shaped, or normal, distribution.
Depending on the mean and standard deviation, there can be many different
normal distributions, but n(x), the standard normal distribution, is perhaps the most
common. It has a mean of 0 and a standard deviation of 1. The standard normal distribution, shown in Figure 18-2, also has one very useful characteristic:
the total area under the curve adds up to exactly 1. That is, the curve represents
100 percent of all occurrences that form a true normal distribution.
Although the standard normal distribution takes in 100 percent of all occurrences, we may want to know what percent of the occurrences fall within a
specific portion of the standard normal distribution. This is given by N(x), the
standard cumulative normal distribution function. If x is some number of standard
deviations, N(x) returns the probability of getting an occurrence less than x by
calculating the area under the standard normal distribution curve between the
values of –∞ and x, as shown in Figure 18-3. That is, N(x) tells us what percentage of all possible occurrences fall between –∞ and x. Obviously, N(+∞) must
be 1.00 because 100 percent of all occurrences must fall between –∞ and +∞.
And N(–∞) must be 0 because there can be no occurrences to the left of –∞. Because the normal distribution curve is symmetrical, with 50 percent of the occurrences falling to the left of 0 and 50 percent falling to the right, N(0) must
equal 0.50. It also follows that the area under the curve between –∞ and x must
be equal to the area under the curve between –x and +∞, resulting in this useful relationship
N(x) = 1 – N(–x)
Figure 18-2  n(x )—the standard normal distribution curve with mean = 0 and standard
deviation = 1.
0
Standard deviations
–1
–2
–3
+3
+2
+1
0
.1
.2
.3
.4
