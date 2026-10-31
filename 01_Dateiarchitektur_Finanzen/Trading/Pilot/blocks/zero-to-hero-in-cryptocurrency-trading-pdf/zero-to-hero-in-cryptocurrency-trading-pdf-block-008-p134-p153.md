# Zero to Hero in Cryptocurrency Trading.pdf — pages 134–153

--- page 134 ---

Conversion, which will tell you how many tokens you’ll receive before converting. Note that you can also use Limit
orders here (to only convert at a certain price).
Figure 5.2 – Binance Convert
In the Trade | Spot menu, you’ll find the interface for spot trading. Trading on the spot allows you to buy and sell
tokens at the current market rate (which is known as the spot price). The trade usually happens immediately, as the
order gets fulfilled.
Trade | Margin Trading allows you to borrow tokens so that you can sell tokens you don’t have. Imagine you want
to short the token (to bet that it will go down). What you actually do is borrow the token from the exchange and
immediately sell it to get the funds at its market price. When the token goes down to your target price, you rebuy the
token (but at a lower price now) and give the token back to the exchange, while retaining the funds that remained after
buying it.
Derivates | USDⓈ-M Futures are perpetual or quarterly contracts settled in USDT or BUSD, or, in simpler
terms, futures trading. This is what I’m usually trading and here’s where we will trade (either directly or through
intermediaries).
Long versus short
--- page 135 ---

When we open a position that we expect to rise in value, we do it by opening a long position, going long or
“longing.”
When we open a position that we expect to fall in value, we open a short position, go short, or just short (a token).
Even though, theoretically, we can go in both directions at the same time (and some risk management strategies do
this, for example, hedging), we usually go either long or short.
When we issue a long order, the CEX buys the token for our account. For example, we can send a market order to
buy one BTC at market value and, after execution, we’ll be owning (or rather our account on the CEX will be
owning) one BTC.
When we open a short position at market value, what the CEX actually does is buy the token, and then instantly sell it
at the price it bought it. When we close the short, the CEX rebuys the token at the new price, and we get the
difference.
For example, we short 1 BTC at market value, let’s say $42,000, and we close our short when BTC falls to $40,000.
What happened was that there was 1 BTC bought at 42K and then sold instantly; then, when the price lowered to
40K, 1 BTC was bought again and the debt of 1 BTC was repaid.
Shorting is riskier because if the trade goes against us, we risk losing our collateral.
The following are a few activities I recommend you go through in order to better understand this topic. They will help
you when you start trading on the exchange.
Activities
1. Watch the spot and margin tutorials on Binance. They are located here: https://www.binance.com/en/support/faq/spot-margin-trading?
c=3&navId=3.
2. Understand the concepts of borrowing and repaying when using margin trading: https://www.binance.com/en/support/faq/spot-margin-trading?
c=3&navId=3#16-182.
3. Go to Trade | Spot and watch the chart for BTC/BUSD on 4H. Note that you can change the chart type from Original (Binance’s version) to
TradingView, which is an embedded version of the chart on TradingView.
Even though there’s a TradingView chart inside Binance, I definitely recommend you stick with
https://www.tradingview.com/ for your charting purposes. As a trader, you’ll do some advanced charting and add
custom indicators that you won’t find there.
Types of orders
There are numerous types of orders on Binance (and other CEXs) but I’m going to limit myself to the most important
ones that are also supported by Binance, such as the following:
Market orders
Limit orders
Stop limit orders
Stop market orders (futures only)
--- page 136 ---

One-Cancels-the-Other (OCO) orders (spot and margin only)
Trailing stop orders
Let’s dive in!
Market orders
With market orders, you are buying at the current price, no matter what it is. A market order guarantees that the
order gets executed because it will accept the price the token has at that moment. The following diagram shows how it
works:
Figure 5.3 – A market order
Limit orders
Limit orders are instructions positioned in the order book that are only executed when the market price meets or
surpasses the established limit price. You can use limit orders to purchase at a reduced price or sell at a higher price,
contingent on the price reaching the desired point. See how it works in the following figure:
--- page 137 ---

Figure 5.4 – A limit order
When you set a limit order, you’re fundamentally determining the maximum amount you’re prepared to spend when
buying a cryptocurrency, or conversely, the minimum amount you’re willing to accept when selling it.
Stop limit orders
A stop limit order has a stop price and a limit price. It’s basically a limit order that only gets triggered when the price
reaches the stop price.
For example, the price has reached a support line and you only want to buy if it tries to rise from there, but you still
want the price near the support. So, you put a stop limit order, with the stop above the support line (when you judge
that there’s a tendency for the price to rise) and the limit at the support line. If the price falls through the support line,
the stop limit order doesn’t get triggered, but if it tries to bounce from support to your chosen stop price, then a limit
order will be put near the support, for when the price gets there.
Another example is to buy when a token shows momentum. If ETH is at $1,100 and you put a stop limit with the stop
at $1,150 and the limit at $1,200, the limit order will be placed once the price reaches $1,150, basically allowing you to
buy up until the $1,200 limit.
One other example would be to sell your token if the price drops too much. When prices fall too quickly, big sell limit
orders might not get filled entirely because the price falls over your limit too quickly and limit orders only sell at your
limit price or better. So, if you’ve bought at 42k, you put a stop at 40.5k and a limit at 40.4k. Essentially, your limit sell
order set at 40.4k only activates when the price drops to 40.5k, enabling you to sell as the price continues to decrease,
up until it hits the 40.4k mark. Here’s what it looks like:
--- page 138 ---

Figure 5.5 – A stop limit order
On some CEXs, you can place a time limit for your stop orders (both stop limit and stop market) or mark them as
good-till-canceled (GTC), meaning that they will remain active until you cancel them manually.
Stop market orders (only available in the futures markets)
Stop market orders are just like stop limit orders but instead of a limit order being placed when the price reaches the
stop price, a market order is being placed there. So, in the previous example, if the price is falling and there’s a stop
market order, you’ll sell starting at the stop price at market price, up until you’ve sold your whole position. The
following figure shows how it works:
Figure 5.6 – A stop market order
--- page 139 ---

OCO orders (spot and margin markets only)
OCO orders combine a stop limit and a limit order in which if one is triggered (even if not filled), the other is canceled.
For example, if ETH is trading in a support range between $1,100 and $1,200, and you want to trade the range and the
breakout, you can put an OCO buy order like this:
The limit order is at $1,100 (basically you buy low in order to sell at the end of the range, at around $1,200)
The stop limit order has its stop at $1,210, with the limit at $1,220 (buying when you consider the price breaks away from the trading range)
Basically, you buy either if it’s too low or if it’s too high, but you don’t want to buy both and your OCO will cancel the second buy order once the
first is filled
Here’s what it looks like:
Figure 5.7 – An OCO order
Another example is when you want to limit your risks. Let’s say you’ve bought ETH at $1,100, estimating it will
increase in price up to $1,200. Still, in case you are wrong, it’s better to protect your money by also selling if it arrives
at $1,050. So here’s the OCO order that you create on the exchange:
The (sell) limit order is at $1,200.
The (sell) stop limit order has its stop at $1,050 and the limit at $1,050 (selling when you reach that point).
Note that the stop and the limit are identical. The limit order will sell at any price >= $1,050, so putting the stop order at $1,050 will trigger a
sale at that price.
In both examples, the OCO orders will make sure that once you do one action, the other is canceled and you don’t
forget about an order that might lose you money.
Trailing stop orders
--- page 140 ---

A trailing stop order shares similarities with a stop limit order, with one crucial distinction: the trailing stop order
adjusts with the market, maintaining a set percentage distance from the current market price, thereby trailing the
price in the direction you desire. This means it continually adjusts to stay the same distance away as the price moves
favorably. However, when the market price moves against your desired direction, the trailing stop order remains static.
It ceases to trail the price, thus creating an opportunity for your trade to be executed when the price hits the
established stop level.
For example, when you want to follow a rising market, you can enter a trade with a trailing stop 2% from the price.
When the price rises by 5%, the trailing stop will follow, keeping your exit 2% from the new (risen) price. It follows it
until the price starts to fall when it catches the fall at 2% from the highest point it reached.
Check how the trailing order follows the price in the following figure:
Figure 5.8 – A trailing stop order
Other types of orders
There are more types of orders (depending on the exchange) but I don’t use them and I’m only listing them here for
your information:
Post-only orders post the orders in the order book without trying to match them with an existing order first. This decreases the fees as you are
a market maker (you put orders in the order book), not a market taker (you fill orders from the order book).
Reduce-only orders are not found on Binance. They help you reduce your position without having to cancel it.
Iceberg orders are used when you have a very large sum, and you don’t want to affect the market. What it does is place a limit order of a
smaller value and, every time the order is taken, places another limit order at the same value.
Hidden orders are limit orders that are not placed in the order book.
Time in force orders:
--- page 141 ---

GTC – These orders don’t expire
Immediate-Or-Cancel (IOC) – This order executes immediately and, even if only partly filled, is canceled if it cannot be instantly
fulfilled
Fill-Or-Kill (FOK) – This order executes immediately in full and gets canceled if cannot be fully filled (so you don’t get a partial
fill)
Time-Weighted Average Price (TWAP) orders are used when you want to spread the order in time to prevent a bad purchase (by averaging the
entries) or when entering the market with a large sum (so you don’t kill the liquidity).
There are more types of orders, but you won’t necessarily need them, and I wanted to present to you the main ones
found on the top crypto CEXs.
In the upcoming section, we will delve into a discussion about the spot market and the futures market, highlighting the
differences between the two.
Spot versus futures
A financial instrument is a contract or a document that represents a legal agreement involving monetary value. It
can include assets, such as stocks and bonds, or contractual rights to receive or deliver cash, such as bank deposits,
loans, and derivatives.
A spot market is a market where the financial instrument being traded is immediately delivered.
A futures market is a market where the financial instrument is being delivered at a later date. You buy (and sell)
derivative contracts that represent the value of the asset.
Futures trading is typically the choice for traders, thanks to its unique advantage of enabling profits from any market
direction. On the other hand, spot trading is a popular choice among investors due to its simplicity. It enables them to
easily buy and hold tokens.
Here is a table with the main differences between spot and futures trading:
Spot
Futures
You own the token (and can use it for staking and with
other instruments)
You do not own the token
You are betting on rising prices
You can profit from either direction.
You pay the price of the asset
You can use leverage to pay less (or buy more)
You pay the normal fees
You pay fees and a (small) difference, which can also
be negative
Table 5.1 – Differences betw een spot and futures trading
Let me explain some of the benefits of futures trading:
--- page 142 ---

It allows you to profit regardless of the market direction, as you can choose to go long or short. This versatility paves the way for sophisticated
strategies such as hedging, where you counterbalance risk in one direction by taking a position in another, and arbitrage among others.
Futures trading enables you to trade with leverage, allowing you to hold more tokens for a lower initial outlay. While this approach is capitalefficient, it also heightens the risk to your portfolio. In spot trading, $100 equates to $100; however, in futures trading on platforms such as
Binance, leverage of up to 125x can be utilized, potentially commanding a position around $11,660, although this is slightly less due to associated
fees.
Futures trading also boasts higher liquidity, thanks to traders operating with leverage, which facilitates larger and more frequent transactions. This
dynamic ensures traders can have their orders filled more swiftly compared to the spot market.
The fee structures also vary between spot and futures trading. In spot trading, you pay for the token price, which is determined by supply and
demand, along with taxes. In futures trading, you incur the carrying cost of the futures contract, which can sometimes be negative, implying that
you get paid. In addition, an overnight fee may apply if you hold your futures contract over an extended period. However, Binance does not
impose this fee for perpetual futures, which is our focus in this discussion.
There are disadvantages to futures trading, which can be summed up as a higher risk of losing money.
The main disadvantage is the risk associated with the exchange selling your position (because your trade went the
other way while using high leverage with small collateral). Imagine opening a position of 11k with $100 in your futures
account, leaving $1 as collateral. You will get liquidated when the price drops by 0.86% because your collateral cannot
sustain your position.
Binance supports perpetual futures, which allows you to trade without a period of expiration on your contracts, which
is the easiest route to understand and trade futures. I will not go into delivery trading in this book, we’ll only use
perpetual futures.
When you first enter your Binance Futures account, you’ll get a video with step-by-step information on how to open
the account, and a quiz that you need to complete accurately to get access to the trading interface. Do your
homework, take the quiz, and voila! You now have access to futures trading and can begin transferring assets to your
Futures account.
Before we go to the next section, Leverage and liquidation, I recommend a few activities for you to better
understand futures trading.
Activities
1. In the Futures interface, in the upper tab, you also have Information | Guide (https://www.binance.com/en/support/faq/crypto-derivatives?
c=4&navId=4), which describes each setting in detail. Go through it and learn more about the Futures interface on Binance.
2. Read all about (crypto) futures on Investopedia.
3. Binance provides a simple calculator for futures trading for profit and loss (PNL), target price, liquidation price, max open, and open
price. Get familiar with it. The calculator is at https://www.binance.com/en/futures/BTCUSDT_PERPETUAL/calculator and its instructions are
here: https://www.binance.com/en/support/faq/how-to-use-binance-futures-calculator-360036498511.
Leverage and liquidation
When we talk about leverage (in crypto), we refer to trading using borrowed money to increase your potential for
profits (and losses).
Leverage is shown in ratios such as 1:2 (2x), 1:5 (5x), 1:50 (50x), and up to 100x (on most CEXs).
--- page 143 ---

This is indicative of how much your initial entry is multiplied by. This means that if you have $100, with 2x leverage,
you can enter a position of $200. With 5x leverage, you’re entering a $500 position.
You enter these bigger positions by borrowing money against your balance, by leveraging your balance against your
position.
The money that you borrow from is called collateral, and before you can start trading using leverage, you need to
have collateral in your futures account. This account is usually separated from your spot account so only the money
transferred into it might get lost.
Margin trading is when you borrow money against your collateral and use that money to open a position. Margin
refers to the collateral you have or the difference between the total value purchased and the loan amount. Buying on
margin happens when you buy an asset (or open a position) using that collateral. Yes, I know it’s a bit confusing, and
several exchanges confuse it further by providing slightly different definitions, but you don’t actually need to have the
specific terminology here in order to understand how it is used. Let’s work through examples.
Say we want to open a position of $1,000 worth of BTC at 10x leverage. You need $100 ($1,000/10) in your account
as collateral for the funds you’ll be borrowing. That’s your margin, $100, and you have borrowed $900.
When using margin, you’ll need what we call a maintenance margin for your trades (Binance also calls it a margin
threshold). What happens is that if the market goes against your opened trades and the margin gets lower than your
margin threshold, you’ll have to add additional funds to your account.
Let’s say that you’ve opened that position of $1,000 with $100 (10x leverage) and your position is up 10%.
Congratulations, you’ve just made $100. If you wouldn’t have used leverage, you’d have made $10.
If the position is down 10%, you’ve (virtually) lost $100 from your collateral, but if you don’t have that $100 lost in
your collateral, and you only have $90 in your trade as margin, you will get liquidated (your balance will go to 0).
Before that happens though, you will get an email from the exchange (depending on the exchange, Binance does this)
to fund your account so that it can sustain this loss.
Let’s talk more about liquidation here. Liquidation in the crypto futures market represents a protection mechanism
against incurring (further) losses. It happens when losses exceed the maintenance margin.
If you open a position of $1,000 worth of BTC at 5x leverage, you need at least $200 as collateral in your account
($1,000/5).
If you have $1,000 in your account (including the open position), then there’s no liquidation because if your position
drops by the maximum amount, $1,000, you’ll lose the $1,000 you have in your account.
However, if you only have $200 and you use it to open the position, you’ll get liquidated when the price drops to
$803.21 (according to https://www.binance.com/en/futures/BTCUSDT_PERPETUAL/calculator). This is because a
~$200 drop in the position actually “eats” the money in your balance (the initial $200 you’ve used to open this position).
The $3.21 represents fees (including a liquidation fee).
Note that the process is a bit more complex, and it includes, on Binance, an insurance fund, a method to autodeleverage liquidations, a Unified Maintenance Margin Ratio, and various other calculations, but you don’t need all
these details at this stage of the game.
--- page 144 ---

I perceive leverage more as “amplifying spikes” rather than merely “investing less capital.” In fact, it can serve as
an effective insurance method to avoid storing large amounts, such as 50k, on an exchange. Many associate leverage
directly with multiplying their standard position size by 10x, which naturally leads to increased risks and higher fees.
However, it’s often overlooked that leverage can be used to achieve a desired position without committing as much
capital upfront. Positions of $300 at 10x leverage and $3,000 at 1x leverage are essentially equivalent.
A word of caution here: misuse of leverage can result in the loss of your entire balance within a span of just 10
seconds. Therefore, my advice is to initiate leverage trading only with small multipliers, say between 2x and 4x.
However, this step should be taken only after you’ve amassed substantial experience trading without leverage, and
you’re consistently making profitable trades. We’ll talk more about this in Chapter 6.
Next, I propose two activities regarding liquidation, which is an important part of futures trading. Make sure you
understand how liquidation works before you go to the next section.
Activities
1. Read about how liquidation works on the exchange you’ll be using. For Binance, read https://www.binance.com/en-ZA/support/faq/how-liquidationworks-in-futures-trading-7ba80e1b406f40a0a140a84b3a10c387, https://www.binance.com/en-ZA/support/faq/how-to-reduce-your-chances-ofgetting-liquidated-25edcd7fe0e544839d0847b8cbb2e400, https://www.binance.com/en/support/faq/liquidation-protocols-360033525271, and
https://www.binance.com/en/support/faq/how-does-liquidation-work-in-the-binance-portfolio-margin-accountff4b1ab6c27b4ed6b3ebe8e4ed1572f8.
2. Play with the Liquidation Price section (and the other sections) of the Binance calculator:
https://www.binance.com/en/futures/BTCUSDT_PERPETUAL/calculator.
The order book, market depth, commissions, spreads, and
slippage
In this section, we will delve into key elements of trading dynamics such as the order book, market depth, commissions,
spreads, and slippage. The order book is a vital tool, showing a list of buy and sell orders for an asset. Market
depth represents the volume of orders at different price levels, providing insights into supply and demand.
Commissions are fees paid to brokers for their services, while spreads denote the difference between the buying
and selling price. Lastly, we’ll look at slippage, a phenomenon that occurs when a trade is executed at a different
price than expected due to market volatility. Together, these components form the backbone of any successful trading
strategy.
I’ve mentioned the term “order book” before but I haven’t explained what it is yet. It’s a very complex topic (entire
books have been written about it) and knowing what it is and how it works will help you understand the subtleties of
trading.
So, what is an order book?
In short, it’s a list of orders that are sorted by the price they target.
When you post a limit order to buy BTC at $42,000, it gets posted in the order book.
Here’s what it looks like:
--- page 145 ---
--- page 146 ---

Figure 5.9 – The order book
As you can see in the figure, we have prices from low (at the bottom) to high (at the top). These are the closest orders
to the current price. The order book is bigger (it basically extends to the complete list of orders), but this is what’s
relevant now.
Each item in the order book has a price, an amount, a total, and a quantity (shown by the amount of green or red
background color). In the book, you will be able to see a light gray area over the prices, which represents the quantity,
but on Binance, it’s red in the upper part of the image and green in the lower part. Here's what the columns in Figure
5.9 mean:
Price: This is the price at which the limit orders were set.
Amount: It represents the total quantity of tokens within those limit orders.
Total: This is the combined value of all the tokens in that price range, indicating the price required to purchase all of them.
Additionally, when you hover over the table, it will display the total amount needed to raise the price to your desired
level by summing the totals up to the point you're hovering over.
Also, see the background color in the limit order. That visually represents the total.
The price in the middle is the last traded price, sometimes followed by an arrow indicating in which direction it traded
from the previous trade and then by the marked price (which is the global spot price index plus a decaying funding
basis rate, but let’s not go into that, unless you insist: https://www.binance.com/en/blog/futures/what-is-the-differencebetween-a-futures-contracts-last-price-and-mark-price-5704082076024731087).
We, as traders, can exploit the order book in various ways.
For example, when we see a lot of limit selling happening (big red background), we can quickly identify a local
resistance there and put our sell order right under it. That way, it will have a higher chance of getting filled.
There are other imbalances that we can look for, such as a limit order of a specific size that gets filled followed by
another one at the same price point and of the exact same size, which might show an Iceberg order being present
(indicative of a hidden support or resistance line at that point).
The market depth or depth of the market
The depth of the market (DOM) is the total volume of limit orders placed in the order book. It represents the ability
of the market to absorb large market orders without (significantly) impacting the price of the token. It’s also called the
DOM.
If we click on the Depth button on the interface, we’ll see the following figure:
--- page 147 ---

Figure 5.10 – DOM
It’s a real-time boxing match between the bulls and the bears. You can interpret this as two waves; the one on the left
(the green one on Binance) is the wave of buyers and the one on the right (the red one on this platform) is the wave of
sellers. When there’s a big wave on one side, it usually (and metaphorically) absorbs the smaller wave on the other
side, moving the price in that direction.
In the figure, you can see how the bulls are winning the battle with big orders under a certain price, absorbing the
sellers and driving the price up.
You can use this information to put a limit order before a big support (or resistance) block so that it will get executed
quicker or to see the real-time dynamics and predict the short-term price direction based on the price volatility. Here
are some other pictures of various DOMs:
--- page 148 ---

Figure 5.11 – Sellers w inning
Here, the sellers have a bigger wave and are catching all the orders. It’s hard for the price to move up past all of those
limit sales and I wouldn’t put a take profit order “that high on the wave.”
Figure 5.12 – Buyers w inning
Here, we have the opposite scenario. Buyers have strong limit buy orders in the order book and it is harder for the
price to be driven down (it needs extremely strong market orders).
--- page 149 ---

Figure 5.13 – Fight later
There is a fight, but it’s not now. We know from this DOM that there is a point that will block the bulls from pushing
the price up, but there’s balance until that point. The fight will happen later.
Liquidity
When we talk about liquidity, we talk about how easy it is for an order to get filled (or how active the order book is).
On smaller CEXs, for some tokens, we might see a static order book that has some buy orders at a low price, some
sell orders at a higher price, and no transactions happening. That’s a token without liquidity.
Think of the market as a vast ocean, with the price being a ship navigating its waters. The ship can move freely, but
sometimes its path is obstructed by icebergs. These icebergs represent “liquidity” in the form of limit orders. In this
vast ocean, some icebergs are gigantic and hard to bypass, while others are smaller and easier to navigate around.
To forge ahead, the ship needs to break through these icebergs. The force that allows the ship to break or melt away
the ice is akin to a “market order.” When a market order is placed, it chips away at the iceberg, thinning its mass.
Once the iceberg is completely shattered or melted, the ship can continue its journey, only to encounter the next
iceberg in its path.
The bid-ask spread
The difference between the highest bid price (the last green buy order) and the lowest ask price (the first red sell
order) is called the spread.
--- page 150 ---

Many brokers in traditional markets monetize the bid-ask spread (they are using market makers to provide liquidity on
their platform). In crypto, the clients usually have direct access to the order book, directly placing orders there so
exchanges don’t (usually) monetize the spread and, instead, they use trading fees.
Slippage
When we talk about slippage, we talk about a market order being filled at a price point other than the one requested.
This happens because there’s not enough liquidity to fill at that specific price (not enough limit orders there to cover
your order), because of the bid-ask spread, because the price has moved quickly from that point, or maybe because of
a delay between the time you submitted it and the time the order was executed. Limit orders do not suffer from
slippage, but they can be partially fulfilled for the same reasons as those mentioned previously. Slippage can also be
positive, as the price you get might be better than the one you initially requested.
Market makers
When we talk about market makers, we talk about companies that provide slippage to CEXs via automated algorithms
that submit limit orders in the order book. They, as market makers, provide liquidity so that market takers (traders who
use market orders) can get their orders executed.
A lot of companies that I’ve worked with needed a market maker, especially during the listing phase where there’s a
lot of buying pressure from fans and selling pressure from investors. That pressure needs to be handled so that the
token increases in price. The ones doing the handling are the market maker companies.
Note that there are market participants who want to trade a higher number of tokens than the usual traders who do so
outside the classical order book. For example, I’ve worked with an NFT marketplace that wanted to sell its business
and its tokens. The selling wouldn’t happen as a dump on the market but as a wallet-to-wallet transaction, without
impacting the order book. These situations are happening in dark pools, on private exchanges, or alternative trading
systems where investors can transact without impacting the price of the token. Imagine the impact it would have if the
NFT marketplace announced that it was going to sell. Instead, they announce that they have been acquired by a bigger
company (thus minimizing impact or even turning it into bullish news) and that is it.
The following is an indispensable tool I employ daily for my trading pursuits – 3Commas. This platform presents a
distinct approach to facilitating trading across a variety of CEXs. It cleverly bridges the gap between slight variances
in terminology and trading nuances, effectively bringing them all under one comprehensive umbrella.
A metaphor for it all – 3Commas
3Commas (https://3commas.io/) is a crypto trading bot platform that is very affordable for people starting out. It
features smart tools for trading, a TradingView subscription inside its platform, connections to multiple exchanges,
crypto signals, portfolio management, cryptocurrency trading, a trading terminal, and various bots: DCA, SMART,
Options, GRID, and HODL.
I mostly use it for its Smart Trade feature and its ability to connect to multiple exchanges (and to trade on them in
parallel). This is its main site where you can create a free account:
--- page 151 ---

Figure 5.14 – 3Commas site
After signing in, you are presented with an onboarding process where you can connect to an exchange and learn about
its interface. Alternatively, if you skip it, you are presented with this interface:
--- page 152 ---

Figure 5.15 – Main interface
The first step you have to take is to connect to an exchange such as Binance. Note that you can connect to multiple
exchanges at the same time and use 3Commas as a portfolio management system, checking, at a glance, all of your
balances across all exchanges.
On the left, you have an Introduction section where you can learn more about its Smart Trading feature, and the
Terminal section from which you can quickly trade on any connected exchange.
I won’t get into the other sections but feel free to use their academy to learn more about the platform:
https://3commas.io/crypto-trading-academy.
Connecting to an exchange
To connect to the exchange, you can go to Dashboard | Supported exchanges (or My Portfolio | Exchanges) and
click the Connect button of your preferred exchange, situated to the right of the exchange name.
--- page 153 ---

Figure 5.16 – Connecting to Binance
SmartTrade
The SmartTrade terminal is the main reason I use 3Commas:
