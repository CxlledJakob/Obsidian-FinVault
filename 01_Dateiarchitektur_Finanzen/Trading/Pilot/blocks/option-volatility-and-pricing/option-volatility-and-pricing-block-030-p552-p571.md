# Option Volatility and Pricing_ Advanced Trading Strategies -- Sheldon Natenberg -- 2nd ed, 2014 -- McGraw Hill Professional -- isbn13 9780071818773 -- 6a48d008bd9beef283debf7bad0b2e4a -- Anna’s Archive.pdf — pages 552–571

--- page 552 ---

V o l at i l i t y C o n t r a c t s 	 535
Replicating a Volatility Contract
Even though replication of a realized variance or VIX position is not a practical choice for most traders, in theory, it is possible to create such a position.
How can this be done?
Suppose that a trader sells a realized variance contract at a volatility of 20
(percent), equal to a variance of 202 = 400. If the actual realized volatility over
the life of the contract is greater than 20 percent, the trader will lose money; if
the actual realized volatility is less than 20 percent, the trader will make money.
How can a trader hedge this position? A variance position can be replicated by
purchasing a strip of options across all exercise prices. To create a position with
a constant-variance exposure, it is necessary to purchase 1/X2 (where X is the
exercise price) of each option. Then, by dynamically hedging the entire position in order to remain delta neutral throughout the life of the variance swap,
the total value of the strategy will exactly match the actual realized variance of
the variance contract.
It may seem that a volatility position can be replicated using the same approach. But the fact that volatility is the square root of variance means that if
the variance exposure is constant, the volatility exposure cannot be constant.
Let’s return to an earlier example where a realized volatility contract with a
vega exposure of $10,000 was purchased at a price of 20. We can compare the
outcomes in two different cases. In the first case, the contract is settled in variance points, with each point having a value equal to the notional vega divided
by twice the volatility price: $10,000/(2 × 20) = $250. In the second case, the
contract is settled in volatility points with each point have a value of $10,000.
Realized
Variance
Variance P&L
Realized
Volatility
Volatility P&L
250
−$37,500
15.81
−$41,900
300
−$25,000
17.32
−$26,800
350
−$12,500
18.71
−$12,900
400
0
20
0
450
+$12,500
21.21
+$12,100
500
+$25,000
22.36
+$23,600
550
+$37,500
23.45
+$34,500
At a realized variance of 400 (a realized volatility of 20), the variance P&L and
the volatility P&L are the same. However, as the difference between the contract variance price of 400 (a volatility price of 20) and the realized variance increases, the difference between the variance P&L and volatility P&L increases.
A strip of options done in the correct proportion of 1/X 2 yields a constant
exposure to variance. But the same strip of options does not yield a constant exposure to volatility. As realized volatility rises or falls, a trader who uses a strip
--- page 553 ---

536
O P T I O N V O L AT I L I T Y A N D P R I C I N G
of options to hedge a volatility position cannot be certain that the strip will exactly offset his position. This uncertainty makes it difficult to hedge volatility
exposure, which is why such contracts are usually settled in variance points.
In our example, if the trader can create the hedge that replicates a long
volatility position at a price of 19 (percent), the trader will have a certain profit
in the form of an arbitrage. He has a short volatility position at a price of 20
(a variance of 400) and a long variance position at a price 19 (a variance of
361). If the contract is settled in variance points, he must show a profit of 39 ×
$250 = $9,750.
If a trader buys the entire strip of options in order to achieve a constantvariance exposure, how can he determine the volatility value of the strip? Did
he buy the strip at a volatility of 19 percent, or 20 percent, or 21 percent, or
some other volatility? The methodology used by the CBOE to calculate the
VIX is essentially a way of turning the cost of the strip into a volatility value.
This is analogous to taking the price of an option and turning it into an implied
volatility. The VIX methodology takes the prices of all the options in the strip
and turns them into an implied volatility position, but one with constant-variance exposure.
At expiration, the value of a VIX contract is determined by a single strip
of SPX options that expire 30 days in the future. But the VIX represents a
constant 30-day implied volatility, and prior to expiration, there are no options
that expire in exactly 30 days. Consequently, two strips of options that bracket
30 days are required to calculate the VIX, with appropriate weighting of each
strip to yield a 30-day implied volatility. In theory, each strip must be dynamically hedged to remain delta neutral. But VIX replication requires the purchase
of one strip and the sale of the one strip, and it turns out that gamma values of
each strip will approximately offset each other. With a total gamma close to 0,
no delta-neutral rehedging is necessary. The position can be carried to expiration of the VIX contract, at which time the long-term strip can be closed out at
the option market prices that will determine the expiration value of the VIX.
Unfortunately, there are several problems with this strategy. When the
long-term strip is closed, a trader will also want to close the short-term strip.
However, while the long-term strip is closed by the special opening rotation on
VIX expiration Wednesday, the short-term strip actually expires on either the
Friday immediately preceding or immediately following VIX expiration. If the
options that make up the short-term strip expire on the Friday after Wednesday VIX expiration, the trader can try to close the short-term strip himself on
expiration Wednesday. But in order to do so, he will have to give up the bidask spread on every option, and this can be costly. If the options that make up
the short-term strip expire on the Friday prior to Wednesday VIX expiration,
the trader will have to carry a naked position in the long-term strip for an additional five days. This can also be costly. How can the trader deal with the risk
that the shortand long-term strips do not expire at the same time? Unfortunately, there is no good solution to this problem, which is one reason why replicating the VIX is so difficult.
An additional problem arises because the value of the VIX is calculated
from the prices of out-of-the-money options. If a trader replicates the VIX
--- page 554 ---

V o l at i l i t y C o n t r a c t s 	 537
by buying one strip and selling another, some of the options that were previously out of the money will almost certainly go into the money over the life
of the strip. To have a position that is equal to the VIX value at expiration,
the in-the-money options must be converted to out-of-the-money options. We
know from synthetics that an in-the-money option hedged with an underlying contract is equivalent to an out-of-the-money option of the opposite type.
Therefore, for each option that is in the money, a trader can buy or sell, as
necessary, one underlying contract. When the entire position, including the
underlying contracts, is closed at expiration, it will exactly equal the expiration value of the VIX. The only problem with this approach is that there is
no easily traded underlying for SPX options because the underlying consists
of a basket of the 500 stocks that make up the S&P 500. If there are S&P 500
futures available that expire at the same time as the VIX, the futures can be
used as a proxy for the underlying contract. Otherwise, a trader may have
to create a proxy underlying, perhaps in the form of combos (i.e., long call/
short put or short call/long put, with the same exercise price) expiring at the
same time as the short-term strip.
While a professional derivatives trading firm might in some cases seek to replicate a realized variance or VIX contract in the option market, for most traders, given the complexities, replicating these contracts is not a realistic possibility.
Volatility Contract Applications
Certainly the most common use of VIX and variance contracts is to speculate on
volatility. A trader who has an opinion on whether realized volatility will rise or fall
can speculate by buying or selling a variance swap. A trader who has an opinion
on whether implied volatility will rise or fall can speculate by buying or selling a
VIX contract. In the latter case, a trader can speculate directly on implied volatility by trading VIX futures or speculate on VIX volatility by trading VIX options.
Volatility contracts can also be used as a hedging instrument. Market makers and hedge fund managers sometimes acquire volatility positions, perhaps
unintentionally, as a result of their market activities. If they want to hedge away
some of this volatility risk, variance and VIX contracts offer a simple way of
doing this. A trader who has a realized volatility position, either a positive or
negative gamma, can trade variance contracts to hedge his realized volatility
risk. A trader who has an implied volatility position, either a positive or negative vega, can trade VIX contracts to hedge his implied volatility risk.
In addition to hedging a volatility position, VIX contracts can sometimes
be used as a hedge against a market position, especially a market position that
approximates a broad-based portfolio. Because there is an inverse correlation
between movement in the stock market and changes in implied volatility (see
Figures 25-4 and 25-5), a portfolio manager who is long equities might take a
long position in the VIX by either buying VIX futures, buying VIX calls, or
selling VIX puts. If stock prices decline, there is an expectation that implied
volatility will rise, and the resulting increase in value of the VIX position will
offset at least some of the losses in the stock market.
--- page 555 ---

538
O P T I O N V O L AT I L I T Y A N D P R I C I N G
Although volatility contracts are used most often to address direct volatility
concerns, market participants sometimes take on indirect volatility positions,
positions that have volatility implications that are not immediately apparent.
For example, an option market maker typically profits from higher option trading volume. But higher volume is often the result of higher volatility. When
there is greater volatility, there is greater demand for options. As such, the market maker has an indirect long volatility position. He would like volatility to
increase not because he has intentionally taken a long volatility position but because he is in a business where higher volatility tends to result in higher profits.
To hedge this indirect long volatility position, market makers sometimes take
a short volatility position in volatility contracts, most commonly the VIX. Of
course, the market maker is really hedging trading volume, and he should not
take such a large VIX position that his attention is diverted from his primary
market-making activities.
Another type of indirect volatility position is one in which a portfolio manager is required to periodically rebalance a portfolio. There is a cost to the rebalancing process, and the cost is typically higher in times of high volatility
when bid-ask spreads tend to widen. The portfolio manager therefore takes on
a short volatility position as the rebalancing period approaches. He can hedge
this short volatility position by taking a long volatility position in the VIX.
Finally, there are some positions that are taken in the option market that
are not usually thought of as volatility positions but that have volatility implications. Perhaps the most common option hedging strategy is the covered call,
the sale of call options against a long underlying position. Consider a portfolio
manager who sells index calls against a broad-based portfolio of stocks. What
are his goals? First, he wants the value of his portfolio to increase. Second, he
wants to outperform some benchmark against which his performance is measured, perhaps a broad-based index such as the S&P 500.
If the manager sells calls against his portfolio holdings and the market
rises, he will achieve his first goal because the portfolio will increase in value.
But, if the market rises too far, eventually the calls he sold will be exercised, limiting the upside profit potential. If the market continues to rise, he will fail in
his second goal because the benchmark index will eventually outperform the
portfolio.
If the manager sells calls against his portfolio and the market declines, he
will achieve his second goal of outperforming the index because he will have
taken in premium through the sale of calls. But, if the decline is great enough,
he will fail in his first goal because the covered calls offer only a partial hedge
against a declining market.
From the portfolio manager’s point of view, the covered call strategy will
perform best, and he will achieve both his goals when the market either doesn’t
move or moves very little. The portfolio will increase in value as a result of the
premium received for the covered calls. And the portfolio will outperform a
benchmark index that consists only of stocks. If the portfolio manager wants
the market to sit still, he has a short volatility position. He can hedge away some
of the risk of a short volatility position by taking a long VIX position, usually
by buying VIX futures.
--- page 556 ---

539
A Final Thought
Because the use of a theoretical pricing model requires a trader to make so
many different decisions with respect to both the inputs into the model and the
reliability of the assumptions on which the model is based, a new option trader
may feel that making the right decisions is either an impossible task or simply
a matter of luck. It is true that a trader using a model will almost certainly be
wrong about at least some of the inputs into the model, and luck undoubtedly
does play a role in the short run. But in the long run traders who are willing
to put in the effort required to understand how a model works, including its
strengths and weaknesses, always seem to come out ahead. Experienced traders
know that under most conditions, using a model, with all its problems, is still the
best way to evaluate options and manage risk.
Regardless of whether a model is simple or complex, a trader who uses
a model needs to have faith in the model. Otherwise, why use a model at all?
Indeed, for traders who are not mathematically proficient, using a model
is often a leap of faith. But having faith in a model does not mean having
blind, unquestioning faith. If a model returns values that are clearly inconsistent with common sense, or if market conditions are changing so quickly
that it is impractical to use the model in its current form, a trader may have to
decide whether to adjust the model, if that is possible, or simply to stop using
the model. Although we have emphasized the importance of models, trading is
both an art and a science. Experienced traders know that there are times when
it is perhaps best to put the model aside and make decisions based on other
intangible assets, whether intuition, “market feel,” or experience. A trader who
slavishly uses a model to make every trading decision is heading for disaster.
Only a trader who fully understands what a model can and cannot do will be
able to make the model his servant rather than his master.
--- page 557 ---

540
Glossary of Option
Terminology
This glossary includes option-related terms as they are most commonly used.
However, the reader should be aware that option terminology is not uniform.
Traders may sometimes refer to different strategies or option characteristics
with the same term. They may sometimes refer to the same strategy or characteristic with different terms.
All or None (AON) 
An order that must be filled in its entirety or not at all.
American Option 
An option that can be exercised at any time prior to
expiration.
Arbitrage 
The purchase and sale of the same or closely related products in
different markets to take advantage of a price disparity between the two markets.
Asian Option 
See Average Price Option.
Assignment 
The process by which the seller of an option is notified of the
buyer’s intention to exercise. The seller is required to take a short position in the
underlying position in the case of a call or a long position in the case of a put.
At the Forward 
An option whose exercise price is equal to the forward price
of the underlying contract. Sometimes referred to as At-the-Money Forward.
At the Money 
An option whose exercise price is equal to the current price
of the underlying contract. On listed option exchanges, the term is more commonly used  to refer to the option whose exercise price is closest to the current
price of the underlying contract.
Automatic Exercise 
The exercise by the clearinghouse of an in-the-money
option at expiration unless the holder of the option submits specific instructions
to the contrary.
A
--- page 558 ---

G l o s s a r y o f O p t i o n T e r m i n o l o g y 	 541
Average Price Option 
An option whose value at expiration is determined
by the average price of the underlying instrument over some period of time.
Also known as an Asian Option.
Backspread 
A spread, usually delta neutral, where more options are purchased than sold, where all options are the same type and expire at the same time.
Backward 
A futures market where the long-term delivery months trade at a
discount to the short-term delivery months.
Barrier Option 
A type of exotic option that will either become effective or
cease to exist if the underlying instrument trades at or beyond some predetermined price prior to expiration.
Bear Spread 
Any spread that will theoretically increase in value with a
decline in the price of the underlying contract.
Bermuda Option 
An option that can be exercised prior to expiration, but
only during a predetermined period or window. Also known as a Mid-Atlantic
Option.
Binary Option 
An option that, if in the money at expiration, makes one
predetermined payout. Also known as a Digital Option.
Box 
A long call and short put at one exercise price, together with a short call
and long put at a different exercise price. All options must have the same underlying contract and expire at the same time.
Bull Spread 
Any spread that will theoretically increase in value with a rise in
the price of the underlying contract.
Butterfly 
The sale (purchase) of two options with the same exercise price,
together with the purchase (sale) of one option with a lower exercise price and
one option with a higher exercise price. All options must be of the same type,
have the same underlying contract, and expire at the same time, and there must
be an equal increment between exercise prices.
Buy/Write 
The purchase of an underlying contract together with the sale of
a call option on that contract.
Cabinet Bid 
An option price that is smaller than the normally allowable
minimum price. On some exchanges, a cabinet bid is permissible between traders desiring to close out positions in very far out-of-the-money options.
Calendar Spread 
The purchase (sale) of one option expiring on one date and
the sale (purchase) of another option expiring on a different date. Typically, both
options are of the same type, have the same exercise price, and have the same
underlying stock or commodity. Also known as a Time Spread or Horizontal Spread.
Call Option 
A contract between a buyer and a seller whereby the buyer
acquires the right, but not the obligation, to purchase a specified underlying
--- page 559 ---

542
O P T I O N V O L AT I L I T Y A N D P R I C I N G
contract at a fixed price on or before a specified date. The seller of the call
option assumes the obligation of delivering the underlying contract should the
buyer wish to exercise his option.
Cap 
A contract between a borrower and a lender of floating-rate funds
whereby the borrower is assured of paying no more than some maximum interest rate for borrowed funds. This is analogous to a call option where the underlying instrument is an interest rate on borrowed funds.
Charm 
The sensitivity of an option’s delta to the passage of time.
Chooser Option 
A straddle where the owner must decide by some predetermined date whether to keep either the call or the put.
Christmas Tree 
A spread involving three exercise prices. One or more calls
(puts) are purchased at the lowest (highest) exercise price, and one or more calls
(puts) are sold at each of the higher (lower) exercise prices. All options must
expire at the same time, be of the same type, and have the same underlying
contract. Also known as a Ladder.
Class 
All options of the same type with the same expiration date and same
underlying instrument.
Clearinghouse 
The organization that guarantees the integrity of all trades
made on an exchange.
Clearing Member 
A member firm of an exchange that is authorized by the
clearinghouse to process trades for its customers and that guarantees, through
the collection of margin and variation, the integrity of its customers’ trades.
Collar 
A long (short) underlying position that is hedged with both a long (short)
out-of-the-money put and a short (long) out-of-the-money call. All options must
expire at the same time. Also known as a Cylinder, Fence, or Range Forward.
Color 
The sensitivity of an option’s gamma to the passage of time.
Combination (Combo) 
A two-sided option spread that does not fall into
any well-defined  category of spreads. Most commonly, it refers to a long call
and short put or short call and long put, which together make up a synthetic
position in the underlying contract.
Compound Option 
An option to purchase an option.
Condor 
The sale (purchase) of two options with different exercise prices,
together with the purchase (sale) of one option with a lower exercise price and
one option with a higher exercise price. All options must be of the same type,
have the same underlying contract, and expire at the same time, and there must
be an equal increment between exercise prices.
Contango 
A futures market where the long-term delivery months trade at a
premium to the short-term delivery months.
--- page 560 ---

G l o s s a r y o f O p t i o n T e r m i n o l o g y 	 543
Contingency Order 
An order that becomes effective only on the fulfillment
of some predetermined condition(s) in the marketplace.
Conversion 
A long underlying position together with a synthetic short
underlying position. The synthetic position consists of a short call and long
put, where both options have the same exercise price and expire at the same
time. Sometimes referred to as a Forward Conversion.
Covered Write 
The sale of a call (put) option against an existing long (short)
position in the underlying contract.
Cylinder 
See Collar.
Delta (Δ) 
The sensitivity of an option’s theoretical value to a change in the
price of the underlying contract. Also known as the Hedge Ratio.
Delta Neutral 
A position where the sum total of all the deltas add up to
approximately 0. Under current market conditions, the position has no preference as to the direction of movement in the underlying market.
Diagonal Roll 
See Time Box.
Diagonal Spread 
A long option at one exercise price and expiration date,
together with a short option at a different exercise price and expiration date. All
options must be the same type. This is the same as a calendar spread using different exercise prices.
Digital Option 
See Binary Option.
Dragonfly 
A long (short) straddle, together with two short (long) strangles at
the same exercise price, where all options expire at the same time and have the
same underlying contract. The exercise price of the straddle will usually fall as
close as possible to the midpoint between the exercise prices of the strangles.
Dynamic Hedging 
A process in which the underlying contract is periodically
bought or sold in order to maintain a desired position in a market. Dynamic
hedging is most often used to maintain a delta-neutral option position.
Efficiency 
A number that represents the relative risk and reward of a potential option strategy. The risk and reward are typically represented by the total
gamma, theta, and vega of the strategy. The efficiency is generated by dividing
one sensitivity by another.
Elasticity 
The percent change in an option’s value for a given percent
change in the value of the underlying instrument. Sometimes referred to as an
option’s Leverage Value. The elasticity is sometimes denoted by the Greek letter
Lambda (Λ).
Eurocurrency 
Currency deposited in a bank outside the currency’s home
country.
--- page 561 ---

544
O P T I O N V O L AT I L I T Y A N D P R I C I N G
Eurocurrency rate 
The interest rate paid on currency deposited in a bank
outside the currency’s home country.
European Option 
An option that may only be exercised at expiration.
Exchange Option 
An option to exchange one asset for another asset.
Ex-Dividend 
The first day on which a dividend-paying stock is trading without the right to receive the dividend.
Exercise 
The process by which the holder of an option notifies the seller of
his intention to take a long position in the underlying contract in the case of a
call or a short position in  the underlying contract in the case of a put.
Exercise Price 
The price at which the underlying contract will be delivered
in the event an option is exercised. Also known as the Strike Price.
Expiration (Expiry) 
The date and time after which an option may no longer be exercised.
Exotic Option 
An option with nonstandard contract specifications. Sometimes referred to as a Second-Generation Option. Exotic options are usually traded
in the over-the-counter (off -exchange) market.
Extrinsic Value 
See Time Value.
Fair Value 
See Theoretical Value.
Fence 
See Collar.
Fill or Kill (FOK) 
An order that will automatically be canceled unless it can
be executed immediately and in its entirety.
Flex Option 
An exchange-traded option where the buyer and seller are
permitted to negotiate the exact terms of the option contract. Typically, this
includes the exercise price, the expiration date, and the exercise style (either
European or American).
Floor 
A contract between a borrower and a lender of floating-rate funds
whereby the lender is assured of receiving no less than some minimum interest
rate for loaned funds. This is analogous to a put option where the underlying
instrument is an interest rate on loaned funds.
Forward Contract 
An agreement between a buyer and a seller to exchange
money for goods at some later date. At maturity, the buyer is obligated to take
delivery and the seller is obligated to make delivery.
Forward Conversion 
See Conversion.
Forward Price 
The price that the buyer of a forward contract agrees to pay
at maturity of the contract.
--- page 562 ---

G l o s s a r y o f O p t i o n T e r m i n o l o g y 	 545
Forward Start Option 
An option that becomes effective only on some
future predetermined date.
Front Spread 
A spread, usually delta neutral, where more options are sold than
purchased, where all options are the same type, and all expire at the same time.
Fugit 
Assuming that all market conditions remain unchanged, the expected
amount of time remaining to optimal early exercise of an American option.
Futures Contract 
An exchange-traded forward contract.
Futures-Type Settlement 
A settlement procedure used by commodity exchanges whereby an initial margin deposit is made but under which no
immediate cash payment is made by the buyer to the seller. Cash settlement
takes place at the end of each trading day based on the difference between the
original trade price or the previous day’s settlement price and the current day’s
settlement price.
Gamma (Γ) 
The sensitivity of an option’s delta to a change in the price of
the underlying contract.
Good ‘til Canceled (GTC) 
An order that remains active until it can either
be executed or is canceled by the customer.
Guts 
A strangle where both the call and the put are in the money.
Haircut 
On a securities exchange, money that a professional trader is
required to keep in his account in order to cover the risk of his position. Haircut requirements are normally determined by the regulatory authority under
which the exchange operates.
Hedge Ratio 
See Delta.
Hedger 
A trader who enters the market with the specific intent of protecting
an existing position in an underlying contract.
Horizontal Spread 
See Calendar Spread.
Immediate or Cancel (IOC) 
An order that will automatically be canceled if
it cannot be executed immediately. An IOC order need not be filled in its entirety.
Implied Volatility 
Assuming that all other inputs are known, the volatility
that would have to be input into a theoretical pricing model to yield a theoretical value that is identical to the price of the option in the marketplace.
In-Option 
A barrier option that becomes effective only if the underlying
instrument trades at or through some predetermined price prior to expiration.
Also known as a Knock-In Option.
In-Price 
The price at which the underlying instrument must trade before an
in-option becomes effective.
--- page 563 ---

546
O P T I O N V O L AT I L I T Y A N D P R I C I N G
In the Money 
An option that has intrinsic value greater than 0. A call option
is in the money if its exercise price is lower than the current price of the underlying contract. A put option is in the money if its exercise price is higher than
the current price of the underlying contract. An option may also be In the Money
Forward if it has intrinsic value greater than 0 when compared with the forward
price of the underlying contract.
Index Arbitrage 
A strategy which attempts to profit from the relative mispricing of options, futures contracts, or the component stocks which make up
a stock index.
Intermarket Spread 
A spread consisting of opposing market positions in
two or more different underlying securities or commodities.
Intrinsic Value 
For an in-the-money option, the difference between the
exercise price and the underlying price. Out-of-the-money options have no
intrinsic value. An option whose price is equal to its intrinsic value is said to be
trading at Parity.
Iron Butterfly 
A long (short) straddle, together with a short (long) strangle,
where all options expire at the same time and have the same underlying contract. The exercise price of the straddle is located at the  midpoint between the
exercise prices of the strangle.
Iron Condor 
A long (short) strangle with narrower exercise prices, together
with a short (long) strangle with wider exercise prices, where all options expire
at the same time and have the same underlying contract. The narrower strangle is centered between the exercise prices of the wider strangle.
Jelly Roll 
See Roll.
Kappa (Κ) 
See Vega. The Greek letter kappa is sometimes used to denote an
option’s exercise price.
Knock-In Option 
See In-Option.
Knock-Out Option 
See Out-Option.
Ladder 
See Christmas Tree. Alternatively, a type of exotic option whose minimum value increases as the underlying contract goes through a series of predetermined prices, or rungs, over the life of the option.
Lambda (Λ) 
See Elasticity.
LEAP (Long-Term Equity Anticipation Security) 
A long-term (usually
more than one year) exchange-traded equity option.
Leg 
One side of a spread position.
Leverage Value 
See Elasticity.
--- page 564 ---

G l o s s a r y o f O p t i o n T e r m i n o l o g y 	 547
Limit 
The maximum allowable price movement over some time period for
an exchange-traded contract.
Limit Order 
An order to be executed at a specified price or better.
Local 
An independent trader on a commodity exchange. Locals perform
functions similar to market makers on stock and stock option exchanges.
Locked Market 
An exchange-traded market where trading has been halted
because prices have reached the limit permitted by the exchange.
Long 
A position resulting from the purchase of a contract. The term is also
used to describe a position that will theoretically increase (decrease) in value
should the price of the underlying contract rise (fall). Note that a long (short)
put position is a short (long) market position.
Long Premium 
A position that will theoretically increase in value should
the underlying contract make a large or swift move in either direction. The
position will theoretically decrease in value should the underlying market fail
to move or move very slowly. The term may also refer to a position that will
increase in value should implied volatility rise.
Long Ratio Spread 
A spread where more options are purchased than sold.
Lookback Option 
An exotic option whose exercise price will be equal to either
the lowest price of the underlying instrument in the case of a call or the highest
price of the underlying instrument in the case of a put over the life of the option.
A lookback option can also have a fixed strike, in which case its value at expiration
will be determined by the maximum underlying price in the case of a call or the
minimum underlying price in the case of a put over the life of the option.
Margin 
Money deposited by a trader with the clearing house to ensure the
integrity of his trades.
Market-if-Touched (MIT) 
A contingency order that becomes a market
order if the contract trades at or beyond a specified price.
Market maker 
An independent trader or trading firm, usually appointed
by an exchange, that is prepared to both buy and sell contracts in a designated
market. A market maker is required to quote both a bid and offer price in his
designated contract.
Market-on-Close (MOC) 
An order to be executed at the market price at
the close of that day’s trading.
Market Order 
An order to be executed immediately at the current market
price.
Mark-to-market 
A method of valuing a position based on the current market price of all contracts which make up the position.
--- page 565 ---

548
O P T I O N V O L AT I L I T Y A N D P R I C I N G
Married Put 
A long (short) put together with a long (short) underlying
position.
Mid-Atlantic Option 
See Bermuda Option.
Midcurve Option 
In futures option markets, a short-term option on a longterm futures contract. Midcurve options are most common in euro-currency
futures markets, such as Eurodollars and Euribor.
Naked 
A long (short) market position with no offsetting short (long)
market position.
Neutral Spread 
A spread that is neutral with respect to some risk measure,
most commonly the delta. A spread may also be lot neutral, where the total
number of long and short contracts of the same type are equal.
Not Held 
An order submitted to a broker but over which the broker has discretion as to when and how the order is executed.
Omega (Ω) 
The Greek letter sometimes used to denote an option’s elasticity.
An alternative to lambda (Λ).
One-Cancels-the-Other (OCO) 
Two orders submitted simultaneously,
either of which may be executed. If one order is executed, the other is automatically canceled.
Order Book Official (OBO) 
An exchange official responsible for executing
market or limit orders for public customers.
Out of the Money 
An option that currently has no intrinsic value. A call
is out of the money if its exercise price is more than the current price of the
underlying contract. A put is out of the money if its exercise price is less than
the current price of the underlying contract. An option may also be Out of the
Money Forward if it has no intrinsic value when compared with the forward price
of the underlying contract.
Out-Option 
A type of barrier option that is deemed to have expired if the
underlying instrument trades at some predetermined price prior to expiration.
Also known as a Knock-Out Option.
Out-Price 
The price at which the underlying instrument must trade before
an out-option is deemed to have expired.
Out-Trade 
A trade that cannot be processed by the clearinghouse due to
conflicting information reported by the two parties to the trade.
Overwrite 
The sale of an option against an existing position in the underlying contract.
Parity 
See Intrinsic Value.
--- page 566 ---

G l o s s a r y o f O p t i o n T e r m i n o l o g y 	 549
Phi (Ф) 
For foreign-currency options, the sensitivity of the option’s value to a
change in the foreign interest rate. Sometimes referred to as Rho2.
Pin Risk 
The risk to the seller of an option that at expiration will be
exactly at the money. The seller will not know whether the option will be
exercised.
Portfolio Insurance 
A process in which the quantity of holdings in an
underlying instrument is periodically adjusted to replicate the characteristics
of an option on the underlying instrument. This is similar to the delta-neutral
dynamic hedging process used to capture the value of a mispriced option.
Position 
The sum total of a trader’s open contracts in a particular underlying market.
Position Limit 
For an individual trader or firm, the maximum number of
open contracts in the same underlying market permitted by an exchange or
clearinghouse.
Premium 
The price of an option.
Program Trading 
An arbitrage strategy involving the purchase or sale of
a stock index futures contract against an opposing position in the component
stocks that make up the index.
Put Option 
A contract between a buyer and a seller whereby the buyer
acquires the right but not the obligation to sell a specified underlying contract at a fixed price on or before a specified date. The seller of the put option
assumes the obligation of taking delivery of the underlying contract should the
buyer wish to exercise his option.
Range Forward 
See Collar.
Ratchet Option 
A type of exotic option whose minimum value is determined by the underlying price at a series of predetermined time intervals over
the life of the option.
Ratio Spread 
Any spread where the number of long market contracts (long
underlying, long call, or short put) and short market contracts (short underlying, short call, or long put) are unequal.
Ratio Write 
The sale of multiple options against an existing position in an
underlying contract.
Reversal 
See Reverse Conversion.
Reverse Conversion 
A short underlying position together with a synthetic
long underlying position. The synthetic position consists of a long call and
short put, where both options have the same exercise price and expire at the
same time. Also known as a Reversal.
--- page 567 ---

550
O P T I O N V O L AT I L I T Y A N D P R I C I N G
Rho (Ρ) 
The sensitivity of an option’s theoretical value to a change in
interest rates.
Risk Reversal 
A long (short) underlying position together with a long (short)
out-of-the-money put and a short (long) out-of-the-money call. Both options
must expire at the same time. Also known as a Split-Strike Conversion. The position is equivalent to a Collar.
Roll 
A long call and short put with one expiration date, together with a short
call and long put with a different expiration date. All four options must have
the same exercise price and the same underlying stock or commodity. In slang
terms, sometimes referred to as a Jelly Roll.
Scalper 
A floor trader on an exchange who hopes to profit by continually
buying at the bid price and selling at the offer price in a specific market. Scalpers usually try to close out all positions at the end of each trading day.
Second-Generation Option 
See Exotic Option.
Serial Option 
On futures exchanges, an option expiration with no corresponding futures expiration. The underlying contract for a serial option is the
nearest futures contract beyond the option expiration.
Series 
All options with the same underlying contract, same exercise price,
and same expiration date.
Short 
A position resulting from the sale of a contract. The term is also used
to describe a position that will theoretically increase (decrease) in value should
the price of the underlying contract fall (rise). Note that a short (long) put position is a long (short) market position.
Short Premium 
A position that will theoretically increase in value should
the underlying contract fail to move or move very slowly. The position will
theoretically decrease in value should the underlying market make a large or
swift move in either direction. The term may also refer to a position that will
increase in value should implied volatility fall.
Short Ratio Spread 
A spread where more options are sold than purchased.
Short Squeeze 
A situation in the stock option market, usually resulting from
a partial tender offer, where no stock can be borrowed to maintain a short stock
position. If assigned on a short call position, a trader may be forced to exercise
a call early to fulfill his delivery obligations, even though the call still has some
time value remaining.
Sigma (σ) 
The commonly used notation for standard deviation. Because volatility is usually expressed as a standard deviation, the same notation is often
used to denote volatility.
--- page 568 ---

G l o s s a r y o f O p t i o n T e r m i n o l o g y 	 551
Specialist 
A market maker given exclusive rights by an exchange to make a
market in a specified contract or group of contracts. A specialist may buy or
sell for his own account or act as a broker for others. In return, a specialist is
required to maintain a fair and orderly market.
Speculator 
A trader who hopes to profit from a specific directional move in
an underlying contract.
Speed 
The sensitivity of an option’s gamma to a change in the underlying
price.
Spread 
A long market position and an offsetting short market position usually, but not always, in contracts with the same underlying market.
Split-Strike Conversion 
See Risk Reversal.
Stock-Type Settlement 
A settlement procedure in which the purchase of
a contract requires full and immediate payment by the buyer to the seller. All
profits or losses from the trade are unrealized until the position is liquidated.
Stop-Limit Order 
A contingency order that becomes a limit order if the
contract trades at a specified price.
Stop (Loss) Order 
A contingency order that becomes a market order if the
contract trades at a specified price.
Straddle 
A long (short) call and a long (short) put where both options have
the same underlying contract, the same expiration date, and the same exercise
price.
Strangle 
A long (short) call and a long (short) put where both options have
the same underlying contract, the same expiration date, but different exercise prices.
Strap 
An archaic term for a position consisting of two long (short) calls and
one long (short) put where all options have the same underlying contract, the
same expiration date, and the same exercise price.
Strike Price (Strike) 
See Exercise Price.
Strip 
An archaic term for a position consisting of one long (short) call and
two long (short) puts where all options have the same underlying contract, the
same expiration date, and the same exercise price. Alternatively, in Eurocurrency markets, a series of futures or futures options designed to replicate the
characteristics of a long-term interest-rate position.
Swap 
An agreement to exchange cash flows. Most commonly, a swap involves
exchanging variable-interest-rate payments for fixed-interest-rate payments.
--- page 569 ---

552
O P T I O N V O L AT I L I T Y A N D P R I C I N G
Swaption 
An option to enter into a swap agreement.
Synthetic 
A combination of contracts that together have approximately the
same characteristics as some other contract.
Synthetic Call  A long (short) underlying position together with a long (short) put.
Synthetic Put 
A short (long) underlying position together with a long
(short) call.
Synthetic Underlying 
A long (short) call and short (long) put where both
options have the same underlying contract, the same expiration date, and the
same exercise price.
Tau (τ) 
The commonly used notation for the amount of time remaining to
expiration. Some traders also use the term to refer to the sensitivity of an option’s
theoretical value to a change in volatility (equivalent to the vega)
Term Structure 
The distribution of implied volatilities across different expiration months in the same underlying market.
Theoretical Value 
An option value generated by a mathematical model given
certain prior assumptions about the terms of the option, the characteristics of the
underlying contract, and prevailing interest rates. Also known as Fair Value.
Theta (Θ) 
The sensitivity of an option’s theoretical value to a change in the
amount of time remaining to expiration.
Three-Way 
A position similar to a conversion or reversal but where the long or
short position in the underlying instrument has been replaced with a very deeply
in-the-money call or put.
Time Box 
A long call and short put with the same exercise price and expiration date together with a short call and long put at a different exercise price and
expiration date. This is simply a roll using different exercise prices. Also known as
a Diagonal Roll.
Time Premium 
See Time Value.
Time Value 
The price of an option less its intrinsic value. The price of an outof-the-money option consists solely of time value. Also known as Extrinisic Value
or Time Premium.
Time Spread 
See Calendar Spread.
Type 
The designation of an option as either a call or a put.
Underlying 
The instrument to be delivered in the event an option is exercised.
Vanilla Option 
An option, usually exchange traded, with standardized and
traditional contract specifications as opposed to an exotic option.
--- page 570 ---

G l o s s a r y o f O p t i o n T e r m i n o l o g y 	 553
Vanna 
The sensitivity of an option’s delta to a change in volatility.
Variation 
The daily cash flow resulting from changes in the settlement price
of a futures contract.
Vega. 
The sensitivity of an option’s theoretical value to a change in volatility.
Also known as Kappa.
Vega Decay 
The sensitivity of an option’s vega to the passage of time.
Vertical Spread 
The purchase of an option at one exercise price and the sale
of an option at a different exercise price where both options are of the same type,
have the same underlying contract, and expire at the same time.
Volatility 
The degree to which the price of a contract tends to fluctuate over
time.
Volatility Skew 
The tendency of options at different exercise prices to trade at
different implied volatilities. Also known as a Volatility Smile.
Volatility Smile 
See Volatility Skew.
Volga 
The sensitivity of an option’s vega to a change in volatility.  Also known
as Vomma.
Vomma 
See Volga.
Warrant 
A long-term call option. The expiration date of a warrant may under
some circumstances be extended by the issuer.
Write 
To sell an option.
Zero-Cost Collar 
A collar where the prices of the purchased and sold options
are equal.
Zomma 
The sensitivity of an option’s gamma to a change in volatility.
--- page 571 ---

554
B
Some Useful Math
The mathematical functions and calculations referred to in this text are
included in almost all commonly used spreadsheets, and for most traders,
it is not necessary to know exactly how the calculations are made. Of far
greater importance is the ability to interpret the numbers that result from
the calculations.
For the reader who is interested, a detailed discussion of these mathematical concepts can be found in any good statistics or finance textbook. For convenience, we include an overview of these concepts and applications.
Rate-of-Return Calculations
An interest rate is the most common rate of return. The total interest can be
computed in three ways: simple, compound, and continuous. If

r = annual interest rate

t = time to maturity, in years

n = number of compounding periods per year

PV = present value of an investment

FV = future value of an investment

ln(x) = natural logarithm

ex = exp(x) = exponential function [(note that the natural
exponential function and natural logarithm are inverses,
that is, ln(ex) = eln(x) = x)]
then, for simple interest,

FV = PV × (1 + r × t)

PV = FV/(1 + r × t)

r = (FV/PV – 1)/t

t = (FV/PV – 1)/r
