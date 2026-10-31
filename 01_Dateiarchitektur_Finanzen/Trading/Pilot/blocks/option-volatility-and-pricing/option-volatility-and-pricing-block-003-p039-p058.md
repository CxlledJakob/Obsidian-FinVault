# Option Volatility and Pricing_ Advanced Trading Strategies -- Sheldon Natenberg -- 2nd ed, 2014 -- McGraw Hill Professional -- isbn13 9780071818773 -- 6a48d008bd9beef283debf7bad0b2e4a -- Anna’s Archive.pdf — pages 39–58

--- page 39 ---

22
O P T I O N V O L AT I L I T Y A N D P R I C I N G
Dividends
In order to evaluate derivative contracts on stock, a trader may be required to
make an estimate of a stock’s future dividend flow. A trader will usually need to
estimate the amount of the dividend and the date on which the dividend will be
paid. To better understand dividends, it may be useful to define some important terms in the dividend process.
Declared Date.  The date on which a company announces both the
amount of the dividend and the date on which the dividend will be paid. Once
the company declares the dividend, the dividend risk is eliminated, at least until
the next dividend payment.
Record Date.  The date on which the stock must be owned in order to receive the dividend. Regardless of the date on which the stock is purchased,
ownership of the stock does not become official until the settlement date, the date
on which the purchaser of the stock officially takes possession. In the United
States, the settlement date for stock is normally three business days after the
trade is made (sometimes referred to as T + 3).
Trade date
Settlement date
Ex-Dividend Date (Ex-Date).  The first day on which a stock is trading
without the rights to the dividend. In the United States, the last day on which
a stock can be purchased in order to receive the dividend is three business days
prior to the record date. The ex-dividend date is two business days prior to the
record date.
Ex-dividend date
Trade date
(Ex-date)
Record date
Two business days
Three business days
On the ex-dividend date, quotes for the stock will indicate that the stock is trading ex-div, and all quotes will be posted with the amount of the dividend deducted from the stock price. If a stock closes on the day prior to the ex-dividend
date at a price of $67.50 and opens the following day (the ex-dividend date) at
a price of $68.25, and the amount of the dividend is $0.40, the price of the
stock will read
68.25 + 1.15 ex-div 0.40
--- page 40 ---

F o r w a r d P r i c i n g
23
If the stock had opened unchanged, the price would have been the previous
day’s price of $67.50 less the dividend of $0.40, or $67.10. With the stock at
$68.25, its price increase is $1.15.
Payable Date.  The date on which the dividend will be paid to qualifying
shareholders (those owning shares on the record date).
The amount of the dividend can often be estimated from the company’s
past dividend payments. If a company pays quarterly dividends, as is common
in the United States, and has paid a dividend of 25 cents for the last 10 quarters, then it is reasonable to assume that in the future the company will continue to pay 25 cents.
We have generally ignored the interest that can be earned on dividends, so
it may seem that the date on which the dividend will be paid is not really important. If, however, the date on which the dividend will be paid is expected to fall
close to the maturity date of a derivative contract, a slight miscalculation of the
dividend date can significantly alter the value of the derivative.
Short Sales
Many derivatives strategies involve buying and selling either stock or futures
contracts. Except for the situation when a market is locked,8 there are no restrictions on the buying or selling of futures contracts. There are also no restrictions
on the purchase of stock or on the sale of stock that is already owned. However,
there may be situations in which a trader will want to sell stock short, that is, sell
stock that he does not already own. The trader hopes to buy back the stock at a
later date at a lower price.
Depending on the exchange or local regulatory authority, there may be
special rules specifying the conditions under which stock can be sold short. In
all cases, however, a trader who wants to sell stock short must first borrow the
stock. This is possible because many institutions that hold stock may be willing
to lend out the stock to facilitate a short sale. A brokerage firm holding a client’s stock may be permitted under its agreement with the client to lend out the
stock. This does not mean that one can always borrow stock. Sometimes it will
be difficult or even impossible to borrow stock, resulting in a short-stock squeeze.
But most actively traded stocks can be borrowed with relative ease, with the
borrowing usually facilitated by the trader’s clearing firm.
Consider a trader who borrows 900 shares of stock from a brokerage
firm in order to sell the stock short at a price of $68 per share. The purchaser will pay the trader $68 × 900, or $61,200, and the trader will deliver
the borrowed stock. The purchaser of the stock does not care whether the
stock was sold short or long (whether the seller borrowed the stock or actually owned it). As far as the purchaser is concerned, he is now the owner of
record of the stock.
8 Some futures exchanges have daily price limits for futures contracts. When a futures contract reaches this
limit, the market is said to be locked or  locked limit. If the market is either limit up or limit down, no further trading
may take place until the price comes off the limit (someone is willing to sell at a price equal to or less than the
up limit or buy at a price equal to or higher than the down limit).
--- page 41 ---

24
O P T I O N V O L AT I L I T Y A N D P R I C I N G
Borrowed stock must eventually be returned to the lender, in this case the
brokerage firm. As security against this obligation, the brokerage firm will hold
the $61,200 proceeds from the sale. Because the $61,200, in theory, belongs
to the trader, the firm will pay the trader interest on this amount. At the same
time, the trader is obligated to pay the brokerage firm any dividends that accrue
over the short-sale period.
How does the brokerage firm as the lender profit from this transaction?
The lending firm profits because it pays the trader only a portion of the full
interest on the $61,200. The exact amount paid to the trader will depend on
how difficult it is to borrow the stock. If the stock is easy to borrow, the trader
may receive only slightly less than the rate he would expect to receive on any
ordinary cash credit. However, if relatively few shares are available for lending,
the trader may receive only a fraction of the normal rate. In the most extreme
case, where the stock is very difficult to borrow, the trader may receive no
interest at all. The rate that the trader receives on the short sale of stock is
sometimes referred to as the short-stock rebate.
We can make a distinction between the long rate rl that applies to ordinary
borrowing and lending and the short rate rs that applies to the short sale of stock.
The difference between the long and short rates represents the borrowing costs rbc
rl – rs = rbc
In a previous example we determined the forward price for a stock

Stock price S = $67.00

Time to maturity t = 8 months

Interest rate r = 6.00 percent

Expected dividend payment D = $0.66
Ignoring interest on the dividends, the eight-month forward price is
67.00 × (1 + 0.06 × 8/12) – 0.66 = 69.02
If the price of an eight-month forward contract is $69.50, there is an arbitrage
opportunity by selling the forward contract and purchasing the stock. Suppose
that instead the eight-month forward contract is trading at a price of $68.75.
Now there seems to be an arbitrage opportunity by purchasing the forward contract and selling the stock. Indeed, if a trader already owns the stock, this will result in a profit of $69.02 – $68.75 = $0.27. If, however, the trader does not own
stock and must sell the stock short in order to execute the strategy, he will not
receive the full interest of 6 percent. If the lending firm will retain 2 percent in
borrowing costs, the trader will only receive the short rate of 4 percent. The forward price is now
67.00 × (1 + 0.04 × 8/12) – 0.66 = 68.13
If the trader attempts to execute the arbitrage by selling the stock short, he will
lose money because
68.13 – 68.75 = –0.62
--- page 42 ---

F o r w a r d P r i c i n g
25
A trader who does not own the stock can only profit if the forward price is
less than $68.13 or more than $69.02. Between these prices, no arbitrage is
possible.
What interest rate should apply to option transactions? Unlike stock, an option
is not a deliverable security. It is a contract that is created between a buyer and a
seller. Even if a trader does not own a specific option, he need not “borrow” the
option in order to sell it. For this reason, we always apply the ordinary long rate
to the cash flow resulting from either the purchase or sale of an option.
--- page 43 ---

26
3
Contract Specifications
and Option Terminology
Every option market brings together traders and investors with different expectations and goals. Some enter the market with an opinion on which direction prices will move. Some intend to use options to protect existing positions
against adverse price movement. Some hope to take advantage of price discrepancies between similar or related products. Some act as middlemen, buying and selling as an accommodation to other market participants and hoping
to profit from the difference between the bid price and ask price.
Even though expectations and goals differ, every trader’s education must
include an understanding of option contract specifications and a mastery of
the terminology used in option markets. Without a clear understanding of the
terms of an option contract and the rights and responsibilities under that contract, a trader cannot hope to make the best use of options, nor will he be prepared for the very real risks of trading. Without a facility in the language of
options, a trader will find it impossible to communicate his desire to buy or sell
in the marketplace.
Contract Specifications
There are several aspects to contract specifications.
Type
In Chapter 1, we introduced the two types of options. A call option is the right
to buy or take a long position in an asset at a fixed price on or before a specified
date. A put option is the right to sell or take a short position in an asset.
Note the difference between an option and a futures contract. A futures
contract requires delivery at a fixed price. The buyer and seller of a futures
contract both have clearly defined obligations that they must meet. The seller
--- page 44 ---

C o n t r a c t S p e c i f i c at i o n s a n d O p t i o n T e r m i n o l o g y
27
must make delivery, and the buyer must take delivery. The buyer of an option,
however, has a choice. He can choose to take delivery (a call) or make delivery (a
put). If the buyer of an option chooses to either make or take delivery, the seller
of the option is obligated to take the other side. In option trading, all rights lie
with the buyer and all obligations with the seller.
Underlying
The underlying asset or, more simply, the underlying is the security or commodity to be
bought or sold under the terms of the option contract. If an option is purchased
directly from a bank or other dealer, the quantity of the underlying can be tailored
to meet the buyer’s individual requirements. If the option is purchased on an exchange, the quantity of the underlying is set by the exchange. On stock option exchanges, the underlying is typically 100 shares of stock.1 The owner of a call has
the right to buy 100 shares; the owner of a put has the right to sell 100 shares. If,
however, the price of an underlying stock is either very low or very high, an exchange may adjust the number of shares in the underlying contract in order to
create a contract size that is deemed reasonable for trading on the exchange.2
On all futures options exchanges, the underlying is uniformly one futures
contract. The owner of a call has the right to buy one futures contract; the
owner of a put has the right to sell one futures contract. Most often, the underlying for an option on a futures contract is the futures month that corresponds to
the expiration month of the option. The underlying for an April futures option
is an April futures contract; the underlying for a November futures option is a
November futures contract. However, an exchange may also choose to list serial
options on futures—option expirations where there is no corresponding futures
month. When a futures option has no corresponding futures month, the underlying contract is the nearest futures contract beyond expiration of the option.
For example, many financial futures are listed on a quarterly cycle, with
trading in March, June, September, and December futures. The underlying for
a March option is a March futures contract; the underlying for a June option is
a June futures contract. If there are also serial options, then

The underlying for a January or February option is a March futures
contract.

The underlying for an April or May option is a June futures contract.

The underlying for a July or August option is a September futures
contract.

The underlying for an October or November option is a December
futures contract.
Some interest-rate futures markets [e.g., Eurodollars at the Chicago
Mercantile Exchange, Short Sterling and Euribor at the London International Financial Futures Exchange], in addition to listing long-term options
on a long-term futures contract, may also  list short-term options on the same
1 One hundred shares is sometimes referred to as a round lot. An order to buy or sell fewer than 100 shares is an
odd lot.
2 Many exchanges also permit trading in flex options, where the buyer and seller may negotiate the contract specifications, including the quantity of the underlying, the expiration date, the exercise price, and the exercise style.
--- page 45 ---

28
O P T I O N V O L AT I L I T Y A N D P R I C I N G
long-term futures contract. A March futures contract maturing in two years
may be the underlying for a March option expiring in two years. But the same
futures contract may also be the underlying for a March option expiring in one
year. Short-term options on long-term futures are listed as midcurve options. The
options can be one-year midcurve (a short-term option on a futures contract
with at least one year to maturity), two-year midcurve (a short-term option on
a futures contract with at least two years to maturity), or five-year midcurve
(a short-term option on a futures contract with at least five years to maturity).
Expiration Date or Expiry
The expiration date is the date on which the owner of an option must make the
final decision whether to buy, in the case of a call, or to sell, in the case of a put.
After expiration, all rights and obligations under the option contract cease to exist.
On many stock option exchanges, the expiration date for stock and stock
index options is the third Friday of the expiration month.3 Of more importance to most traders is the last trading day, the last business day prior to expiration on which an option can be bought or sold on an exchange. For most stock
options, expiration day and the last trading day are the same, the third Friday
of the month. However, Good Friday, a legal holiday in many countries, occasionally falls on the third Friday of April. When this occurs, the last trading day
is the preceding Thursday.
When stock options were introduced in the United States, trading in expiring contracts ended at the close of business on the third Friday of the month.
However, many derivative strategies require carrying an offsetting stock position to expiration, at which time the stock position is liquidated. Consequently,
stock exchanges found that as the close of trading approached on expiration
Friday, they were faced with large orders to buy or sell stock. These large orders often had the effect of disrupting trading or distorting prices at expiration.
To alleviate the problem of large order imbalances at expiration, some
derivative exchanges, working with the stock exchanges on which the underlying stocks were traded, agreed to establish an expiration value for a derivatives
contract based on the opening price of the underlying contract rather than the
closing price on the last trading day. This AM expiration is commonly used for
stock index contracts. Options on individual stocks are still subject to the traditional PM expiration, where the value of an option is determined by the underlying stock price at the close of trading on the last trading day.
Although the expiration date for stock options is relatively uniform,  the
expiration date for futures options can vary, depending on the underlying commodity or financial instrument. For futures on physical commodities, such as
agricultural or energy products, delivery at maturity may take several days. As
a consequence, options on futures for physical commodities will often expire
several days or even weeks prior to the maturity of the futures contract, most
commonly in the month prior to the futures month. An option on a March futures contract will expire in February; an option on a July futures contract will
3 In the early days of option trading, exchange-traded options often expired on a nonbusiness day, typically on a
Saturday. This gave the exchange an extra day to process the paperwork associated with expiring options.
--- page 46 ---

C o n t r a c t S p e c i f i c at i o n s a n d O p t i o n T e r m i n o l o g y
29
expire in June; an option on a November futures contract will expire in October. A trader will need to consult the exchange calendar to determine the exact
expiration date, which is set by each individual exchange.
Exercise Price or Strike Price
The exercise or strike price is the price at which the underlying will be delivered
should the holder of an option choose to exercise his right to buy or sell. If the
option is exercised, the owner of a call will pay the exercise price; the owner of
a put will receive the exercise price.
The exercise prices available for trading on an option exchange are set by
the exchange, usually at equal intervals and bracketing the current price of the
underlying contract. If the price of the underlying contract is 62 when options
are introduced, the exchange may set exercise prices of 50, 55, 60, 65, 70, and
75. At a later date, as the price of the underlying moves up or down, the exchange can add additional exercise prices. If the price of the underlying rises to
70, the exchange may add exercise prices of 80, 85, and 90. Additionally, if the
exchange feels that it will further facilitate trading, it can introduce intermediate exercise prices—52½, 57½, 62½, 67½.
As an example of an exchange-traded option, the buyer of a crude oil October 90 call on the New York Mercantile Exchange has the right to take a long
position in one October crude oil futures contract for 1,000 barrels of crude oil
(the underlying) at a price of $90 per barrel (the exercise price) on or before the
October expiration (the expiration date). The buyer of a General Electric March
30 put on the Chicago Board Options Exchange has the right to take a short position in 100 shares of General Electric stock (the underlying) at a price of $30
per share (the exercise price) on or before  March expiration (the expiration date).
Option contract specifications are further outlined in Figure 3-1.
Exercise and Assignment
The buyer of a call or a put option has the right to exercise that option prior to
its expiration date, thereby converting the option into a long underlying position in the case of a call or a short underlying position in the case of a put. A
trader who exercises a crude oil October 90 call has chosen to take a long position in one October crude oil futures contract at $90 per barrel. A trader who
Figure 3-1  Option contract specifications.
Crude Oil
October
90
Call
underlying
contract
expiration
date
exercise
price
type
GE
March
30
Put
--- page 47 ---

30
O P T I O N V O L AT I L I T Y A N D P R I C I N G
exercises a GE March 30 put has chosen to take a short position in 100 shares
of GE stock at $30 per share. Once an option is exercised, the rights and
obligations associated with the option cease to exist, just as if the option had
been allowed to expire.
A trader who intends to exercise an option must submit an exercise notice
to either the seller of the option, if purchased from a dealer, or to the exchange,
if the option was purchased on an exchange. When a valid exercise notice is
submitted, the seller of the option has been assigned. Depending on the type of
option, the seller will be required to take a long or short position in the underlying contract at the option’s exercise price.
Once a contract has been traded on an exchange, the link between buyer
and seller is broken, with the exchange becoming the counterparty to all trades.
Still, when a trader exercises an option, the exchange must assign someone to
either buy or sell the underlying contract at the exercise price. How does the
exchange make this decision? The party who is assigned must be someone who
has sold the option and has not closed out the position through an offsetting
trade. Beyond this, the exchange’s decision on who will be assigned is essentially random, with no trader having either a greater or lesser probability of
being assigned.
New traders sometimes become confused about whether the exercise and
assignment result in a long position (buying the underlying contract) or a short
position (selling the underlying contract). The following summary may help: if you
Exercise a call

You choose to buy at the exercise price.
Are assigned on a call
You are required to sell at the exercise price.
Exercise a put

You choose to sell at the exercise price.
Are assigned on a put
You are required to buy at the exercise price
Depending on the underlying contract, when an exchange-traded option
is exercised, it can settle into
1.	 The physical underlying
2.	 A futures position
3.	 Cash
Settlement into the Physical Underlying
If a call option settles into the physical underlying, the exerciser pays the exercise price and in return receives the underlying. If a put option settles into the
physical underlying, the exerciser receives the exercise price and in return must
deliver the underlying. Stock options always settle into the physical underlying.
You exercise one January 110 call on stock.
  You must pay 100 × $110 = $11,000.
  You receive 100 shares of stock.
You are assigned on six April 40 calls on stock.
  You receive 600 × $40 = $24,000.
  You must deliver 600 shares of stock.
--- page 48 ---

C o n t r a c t S p e c i f i c at i o n s a n d O p t i o n T e r m i n o l o g y
31
You exercise two July 60 puts on stock.
  You receive 200 × $60 = $12,000.
  You must deliver 200 shares of stock.
You are assigned on three October 95 puts on stock.
  You must pay 300 × $95 = $28,500.
  You receive 300 shares of stock.
Note that the cash flow resulting from settlement into the physical underlying depends only on the exercise price. In our examples, whether the price of
the stock at exercise is $10 or $1,000, the exerciser of a call pays only the exercise price, not the stock price. The exerciser of a put receives only the exercise
price. Of course, the profit or loss resulting from the option trade will depend
on both the stock price and the price originally paid for the option. But the cash
flow when the option is exercised is independent of these.
Settlement into a Futures Position
If an option settles into a futures position, it is just as if the exerciser is buying
or selling the futures contract at the exercise price. The position is immediately
subject to futures-type settlement, requiring a margin deposit and accompanied by a variation payment.
An underlying futures contract is currently trading at 85.00 with a point
value of $1,000. Margin requirements are $3,000 per contract.
You exercise one February 80 call.
  You immediately become long one futures contract at a price of 80.
  You must deposit with the exchange the required margin of $3,000.
  You will receive a variation credit of (85 – 80) × $1,000 = $5,000.
You are assigned on six May 75 calls.
  You immediately become short six futures contracts at a price of 75.
  You must deposit with the exchange the required margin of 6 × $3,000
= $18,000.
  You will have a variation debit of (75 – 85) × $1,000 × 6 = –$60,000
You exercise four August 100 puts.
  You immediately become short four futures contracts at a price of 100.
  You must deposit with the exchange the required margin of 4 × $3,000
= $12,000.
  You will receive a variation credit of (100 – 85) × $1,000 × 4 = $60,000.
You are assigned on two November 95 puts.
  You immediately become long two futures contracts at a price of 95.
  You must deposit with the exchange the required margin of 2 × $3,000
= $6,000.
  You will have a variation debit of (85 – 95) × $1,000 × 2 = –$20,000.
Settlement into Cash
This type of settlement is used primarily for index contracts where delivery
of the underlying contract is not practical. If exercise of an option settles into
cash, no underlying position results. There is a cash payment equal to the difference between the exercise price and the underlying price at the end of the
trading day.
--- page 49 ---

32
O P T I O N V O L AT I L I T Y A N D P R I C I N G
An underlying index is fixed at the end of the trading day at 300. The exchange has assigned a value of $500 to each index point.
You exercise three March 250 calls.
  You have no underlying position.
  Your account will be credited with (300 – 250) × $500 × 3 = $75,000.
You are assigned on seven June 275 calls.
  You have no underlying position.
  Your account will be debited by (275 – 300) × $500 × 7 = $87,500.
You exercise two September 320 puts.
  You have no underlying position.
  Your account will be credited with (320 – 300) × $500 × 2 = $20,000.
You are assigned on four December 340 puts.
  You have no underlying position.
  Your account will be debited by (300 – 340) × $500 × 4 = $80,000.
Exercise Style
In addition to the underlying contract, exercise price, expiration date, and
type, an option is further identified by its exercise style, either European or
American. A European option can only be exercised at expiration. In practice,
this means that the holder of a European option must make the final decision whether to exercise or not on the last business day prior to expiration.
In contrast, an American option can be exercised on any business day prior
to expiration.
The designation of an option’s exercise style as either European or American has nothing to do with geographic location. Many options traded in the
United States are European, and many options traded in Europe are American.4 Generally, options on futures and options on individual stocks tend to be
American. Options on indexes tend to be European.
Option Price Components
As in any competitive market, an option’s price, or premium, is determined by
supply and demand. Buyers and sellers make competitive bids and offers in the
marketplace. When a bid and offer coincide, a trade is made.
The premium paid for an option can be separated into two components—
the intrinsic value and the time value. An option has intrinsic value if it enables the
holder of the option to buy low and sell high or sell high and buy low, with the
intrinsic value being equal to the difference between the buying price and the
selling price. With an underlying contract trading at $435, the intrinsic value
of a 400 call is $35. By exercising the option, the holder of the 400 call can buy
at $400. If he then sells at the market price of $435, $35 will be credited to his
account. With an underlying contract trading at $62, the intrinsic value of a 70
4 It does appear that the first options traded in the United States carried with them the right of early exercise—
hence the term American option.
--- page 50 ---

C o n t r a c t S p e c i f i c at i o n s a n d O p t i o n T e r m i n o l o g y
33
put is $8. By exercising the option, the holder of the put can sell at $70. If he
then buys at the market price of $62, he will show a total credit of $8.
A call will only have intrinsic value if its exercise price is less than the current market price of the underlying contract because no one would choose to
buy high and sell low. A put will only have intrinsic value if its exercise price is
greater than the current market price of the underlying contract because no
one would choose to sell low and buy high. The amount of intrinsic value is the
amount by which the exercise price is less than the current underlying price in
the case of a call or the amount by which the exercise price is greater than the
current underlying price in the case of a put. No option can have an intrinsic
value less than zero. If S is the spot price of the underlying contract and X is the
exercise price, then
Call intrinsic value = maximum of either 0 or S – X.
Put intrinsic value = maximum of either 0 or X – S.
Note that the intrinsic value is independent of the expiration date. With
the underlying contract at $83, a March 70 call and a September 70 call both
have an intrinsic value of $13. A June 90 put and a December 90 put both have
an intrinsic value of $7.
Usually, an option’s price in the marketplace will be greater than its intrinsic
value. The time value, sometimes also referred to as the option’s time premium or extrinsic value, is the additional amount of premium beyond the intrinsic value that
traders are willing to pay for an option. Market participants are willing to pay this
additional amount primarily because of the protective characteristics afforded
by an option over an outright long or short position in the underlying contract.
An option’s premium is always composed of precisely its intrinsic value
and its time value. Examples of intrinsic value and time value are shown in
Figure 3-2. If a $400 call is trading at $50 with the underlying trading at $435,
the time value of the call must be $15 because the intrinsic value is $35. The
two components must add up to the option’s total premium of $50. If a $70 put
on a stock is trading for $11 with the stock trading at $62, the time value of the
put must be $3 because the intrinsic value is $8. Again, the intrinsic value and
the time value must add up to the option’s premium of $11.
Even though an option’s premium is always composed of its intrinsic value
and its time value, one or both of these components can be zero. If the option
has no intrinsic value, its price in the marketplace will consist solely of time
value. If the option has no time value, its price will consist solely of intrinsic
value. In the latter case, traders say that the option is trading at parity.
Although an option’s intrinsic value can never be less than zero, it is possible for a European option to have a negative time value. (More about this in
Chapter 16 when we look at the early exercise of American options.) When this
happens, the option can trade for less than parity. Usually, however, an option’s
premium will reflect some nonnegative amount of time value.
In the Money, At the Money, and Out of the Money
Depending on the relationship between an option’s exercise price and the
price of the underlying contract, options are said to be in the money, at the
--- page 51 ---

34
O P T I O N V O L AT I L I T Y A N D P R I C I N G
money, and out of the money. Any option that has a positive intrinsic value
is said to be in the money by the amount of the intrinsic value. With a stock at
$44, a $40 call is in the money by $4. A $55 put on the same stock is in the
money by $11. An option with no intrinsic value is said to be out of the money,
and its price consists solely of time value. In order to be in the money, a call
must have an exercise price lower than the current price of the underlying
contract, and a put  must have an exercise price  higher than the current price
of the underlying contract. Note that if a call is in the money, a put with the
same exercise price and underlying contract must be out of the money. Conversely, if the put is in the money, a call with the same exercise price must be
out of the money. In our examples with the stock at $44, the $40 put is out of
the money by $4 and the $55 call is out of the money by $11.
Finally, an option whose exercise price is equal to the current price of the
underlying contract is said to be at the money. Technically, such an option is also
out of the money because it has no intrinsic value. Traders make the distinction
between at-the-money and out-of-the-money options because, as we shall see,
at-the-money options often have very specific and desirable characteristics, and
such options tend to be the most actively traded.
If we want to be very precise, for an option to be at the money, its exercise price must be exactly equal to the current price of the underlying contract. However, for exchange-traded options, the term is commonly applied
to the call and put whose exercise price is closest to the current price of the
underlying contract. With a stock at $74 and $5 between exercise prices ($65,
$70, $75, $80, etc.), the $75 call and the $75 put are the at-the-money options.
These are the call and put options with exercise prices closest to the current
price of the underlying contract. In-, at-, and out-of-the-money options are
outlined in Figure 3-3.
Figure 3-2  Intrinsic value and time value.
$50
$35
($435 – $400)
$15
($50 – $35)
=
+
Intrinsic
value
Time
value
Price
=
+
$11
=
$8
($70 – $62)
+
$3
($11 – $8)
Underlying contract trading at $435
April 400 call trading at $50
Underlying contract trading at $62
October 70 put trading at $11
--- page 52 ---

C o n t r a c t S p e c i f i c at i o n s a n d O p t i o n T e r m i n o l o g y
35
Automatic Exercise
At expiration an in-the-money option will always have some intrinsic value. A
trader can capture this value by either selling the option in the marketplace prior
to expiration or exercising the option and immediately closing the underlying
position. When exchange-traded options were first introduced, anyone wishing to exercise an option was required to formally submit an exercise notice to the
exchange. If someone forgot to submit an exercise notice for an in-the-money
option, the option would expire unexercised, and the trader would lose the intrinsic value. This is an outcome that no rational person would accept. Unfortunately, in the early days of option trading, this occurred occasionally for various
reasons: perhaps the trader was unaware that he was required to submit an exercise notice, perhaps the trader was out of communication with the exchange
and was therefore unable to submit an exercise notice, or perhaps there was an
error on the part of the clearing firm in processing the exercise notice.
To avoid a situation where an in-the-money option expires unexercised,
which would be an embarrassment to both the individual trader and the exchange, most exchanges have instituted an automatic exercise policy. The exchange
will exercise on behalf of the option holder any in-the-money option at expiration, even if an exercise notice has not been submitted. The criteria for automatic exercise may vary from one exchange to another and may also vary
depending on who holds the option. For example, because of transaction costs,
it may not be economically worthwhile to exercise an option that is only very
slightly in the money. Therefore, the exchange may automatically exercise only
options that are in the money by some predetermined amount. If the automatic exercise threshold is 0.05, then an option must be in the money by at
least 0.05 in order for the exchange to exercise the option. If the option is in the
money by 0.03, a trader may still exercise the option but must do so by submitting an exercise notice. On the opposite side, if the option is in the money by
0.06, a trader who feels that the option is not worth exercising may submit a do
not exercise notice. Otherwise, the exchange will automatically exercise the option
on the trader’s behalf.
Because professional traders and retail customers have different cost
structures, the exchange may have a different automatic exercise threshold for
Figure 3-3  In-, at-, and out-of-the-money options.
Current underlying price
In-the-money calls
Out-of-the-money calls
Lower exercise prices
Higher exercise prices
Out-of-the-money puts
In-the-money puts
At-the-money calls and puts
--- page 53 ---

36
O P T I O N V O L AT I L I T Y A N D P R I C I N G
each party. The threshold may be 0.05 for retail customers but only 0.02 for
professionals. To determine who is a professional trader and who is not, an exchange will usually specify the criteria necessary for inclusion in each category.
Option Margining
Depending on the exchange and the type of underlying contract, options can
be subject to either stock-type settlement or futures-type settlement. However,
once an option trade is made, there are additional risks that the clearinghouse
must consider. Is the risk to an option position limited or unlimited? If unlimited, how should the clearinghouse protect itself?
When the risk of an option position is limited, the margin that must be deposited with the clearinghouse will never be greater than the maximum risk to
the position. The buyer of an option can never have risk greater than the premium paid for the option, and the clearinghouse will never require a margin
deposit greater than this amount. Even if an option position is very complex, as
long as there is a maximum risk to the position, there will also be a maximum
margin requirement.
Some option positions, however, have unlimited risk. For such positions,
the clearinghouse must consider the risk associated with a wide variety of outcomes. Once this is done, the clearinghouse can require a margin deposit commensurate with the perceived risk of the position. Unlike futures margining,
where the clearinghouse sets a fixed margin deposit for each open futures position, there is no single method of determining the margin for a complex option position. However, all methods are risk-based, requiring an analysis of the
position’s risk under a broad range of market conditions. In the United States,
the Options Clearing Corporation has developed its own risked-based margining system for stock and index options. The most widely used margining system on futures exchanges is the Standard Portfolio Analysis of Risk (SPAN) system
developed by the Chicago Mercantile Exchange. Both margining systems create an array of possible outcomes with respect to both the underlying price and
the perceived speed with which the underlying price can change. The clearinghouse then uses this array to determine a reasonable margin requirement.5
5 A description of SPAN margining can be found at http://www.cmegroup.com/clearing/risk-management. A
description of the risk-based margining system used by the Options Clearing Corporation can be found at http://
www.optionsclearing.com/risk-management/margins/.
--- page 54 ---

37
4
Expiration Profit
and Loss
The trader who enters an option market for the first time may find himself subjected to a form of contract shock. Unlike a trader in equities or futures, whose
choices are limited to a small number of instruments, an option trader must often deal with a bewildering assortment of contracts. With several expiration
months, with multiple exercise prices available in each month, and with both
calls and puts at each exercise price, it is not unusual for an option trader to be
faced with what at first seems like an overwhelming number of different contracts. With so many choices available, a trader needs some logical method of
deciding which options actually represent profit opportunities. Which should he
buy? Which should he sell? Which should he avoid? The choices are so numerous that a prospective option trader might be inclined to give up in frustration.
To begin, a trader might ask a very obvious question: what is an option
worth? The question may be obvious, but the answer, unfortunately, is not, because option prices can be affected by many different market forces. However,
there is one time in an option’s life when everyone ought to be able to agree on
the option’s value. At expiration, an option is worth exactly its intrinsic value:
zero if it is out of the money or the difference between the underlying price and
the exercise price if it is in the money.
Following is a series of underlying prices and the value at expiration for
two options, a $95 call and $110 put:
Underlying Price
95 Call
110 Put
80
0
30
85
0
25
90
0
20
95
0
15
100
5
10
--- page 55 ---

38
O P T I O N V O L AT I L I T Y A N D P R I C I N G
Underlying Price
95 Call
110 Put
105
10
5
110
15
0
115
20
0
120
25
0
125
30
0
For the 95 call, if the underlying price at expiration is 95 or below, the call is
out of the money and therefore worthless. If, however, the underlying price rises
above 95, the 95 call will go into the money, gaining one point in value for each
point that the underlying price rises above 95. For the 110 put, if the underlying
price is 110 or above, the put is out of the money and therefore worthless. But
if the underlying price falls below 110, the 110 put goes into the money, gaining
one point in value for each point decline in the underlying price.
Parity Graphs
For someone who has bought an option, the intrinsic value represents a credit,
or positive value. The buyer of the option will be able to buy low and sell high.
For someone who has sold an option, the intrinsic value represents a debit, or
negative value. The seller of the option will be forced to buy high and sell low.
We can use an option’s intrinsic value to draw a graph of the value of an option position at expiration as a function of the price of the underlying contract.
Figure 4-1 shows such a graph for a long call position. Below the exercise price,
the option has no value. Above the exercise price, the option gains one point in
value for each point increase in the underlying price.
Figure 4-1  Long call.
+1
+1
Position value
0
Exercise
price
Higher underlying prices
Lower underlying prices
--- page 56 ---

E x p i r at i o n P r o f i t a n d L o s s
39
Figure 4-2 shows the value of a short call position at expiration. Now, if the
option is in the money, the value of the position is negative. For every point the
underlying rises above the exercise price, the position loses one point in value.
We can create the same type of expiration graphs for long and short put
positions, as shown in Figures 4-3 and 4-4. For a long or short put, the value of
the position is zero if the underlying price is above the exercise price. For a long
put, the position gains one point for each point decline in the underlying price.
For a short put, the position loses one point in value for each point decline in
the underlying price.
A parity graph represents the value of an option position at expiration,
parity being another name for intrinsic value. Because of their shapes, traders
Figure 4-2  Short call.
Higher underlying prices
Lower underlying prices
+1
–1
Exercise
price
Position value
0
Figure 4-3  Long put.
Exercise
price
Higher underlying prices
Lower underlying prices
–1
+1
Position value
0
--- page 57 ---

40
O P T I O N V O L AT I L I T Y A N D P R I C I N G
sometimes refer to the four basic parity graphs (long and short call and long
and short put) as the hockey-stick diagrams.
The four basic parity graphs highlight one of the most important characteristics of option trading. Buyers of options have limited risk (they can never
lose more than the price of the option) and unlimited profit potential. Sellers of
options have limited profit potential (they can never make more than the price
of the option) and unlimited risk.1
Given the apparently unbalanced risk-reward tradeoff, new option traders
tend to have the same reaction: why would anyone do anything other than buy
options? The purchase of an option results in a position with limited risk and unlimited profit, which certainly seems more desirable than the limited profit and
unlimited risk that result from the sale of an option. Yet, in every option market,
there are traders who are willing to sell options. Why are they willing to do this in
the face of this apparently unbalanced risk-reward tradeoff? The answer has to
do with not just the best and worst that can happen but also with the likelihood
of those occurrences. It’s true that someone who sells an option is exposed to unlimited risk, but if the amount received for the option is great enough and the
perceived risk is low enough, a trader might be willing to take that risk. In later
chapters we will see the very important role probability plays in option pricing.
Slope
From the parity graphs, we can see that if an option is out of the money, its value
is unaffected by changes in the price of the underlying contract. If the option
is in the money, it will either gain or lose value as the underlying price changes.
1 Admittedly, in traditional stock and commodity markets, a put does not represent unlimited profit potential to
the buyer nor unlimited risk to the seller because the underlying contract cannot fall below zero. But for practical purposes most traders think of both calls and puts as having unlimited potential value.
Figure 4-4  Short put.
Exercise
price
Higher underlying prices
Lower underlying prices
–1
–1
Position value
0
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
