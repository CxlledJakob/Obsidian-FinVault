# Zero to Hero in Cryptocurrency Trading.pdf — pages 229–248

--- page 229 ---

Figure B.13 – 3C’s Trade Terminal
Now, we confirm the transaction:
--- page 230 ---

Figure B.14 – The transaction confirmation
Since BTC is currently trading at 25,656 and my buy limit price is at 25,643, I’ll have to wait until it arrives at my trade.
Never run for the trade; doing market orders to catch a price usually means that you have a fear of missing out
(FOMO). Do limit orders and just accept it if they don’t get triggered; there’s always another trade to make. If you
see me doing market orders, I’m usually doing that because of a running trend that I do want to catch, but I don’t
recommend you trade in the spur of the moment. I invite you to do the calculations and figure out how much I’ve lost
(or won) by using market orders instead of limit orders. Alternatively, you can just use limit orders.
All right, let’s look at the trade:
Figure B.15 – Trade #1
We’ll usually start on minus because of the transaction fees.
Here’s how it went:
Figure B.16 – Trade #1 – ended
The trade ended in a SL but with a profit. How is this possible?
Well, it is, because we’ve set two TPs and a move to breakeven. Basically, it took TP1 and then it returned to the
entry price. On TradingView, it looks like this:
--- page 231 ---

Figure B.17 – TradingView ’s view
And on 3C it looks like this:
Figure B.18 – Trade #1 – the TP1 hit and then SL
It would’ve worked better if I’d added an SL timeout to prevent that short drop under the channel, which was
actually pretty visible in the past. I’ve noted that down as a learning point.
A SHORT NOTE ABOUT RISK MANAGEMENT AND THE TRADING JOURNAL
Risk management and the trading journal were presented in Chapter 6. I think I included enough examples there, so we can skip them in this
section. Journaling entries now would increase the size of the chapter quite a lot and would distract you from following the trades and the
thinking behind them. Because of this, I will use $880 to enter each trade, with a few exceptions (where I’ll show you the when, why, and how to
add funds to a trade that goes against you). The fixed sum will allow you to compare the trades and their results over different timeframes.
Adding other coins to watch
Since I already have TradingView open, I will add a few other coins from https://www.sandwich.finance/ | BUSD
perpetual futures. That link gets me a .txt file, which I import from Trading View | Watchlist and details. Then, I
--- page 232 ---

click on the arrow down next to the current list name and then click on Import list and rename it Binance Futures
BUSD (I’ll leave the location of the rename button to you).
Note that even when I’m trading spontaneously, I like to trade tokens that hold some value, and those are usually the
tokens that have made it to the perpetual futures market.
June, 10 – Trade 2 ETH/BUSD
After BTC, I usually look at ETH. It was trading in a parallel channel, but I found increasing volume in a break from
that channel, so I wanted to trade that. It was also a hedge against the trend, as I was already long on BTC.
This is what I wanted to catch:
Figure B.19 – Trade setup for ETH/BUSD on 1H
And here’s my setup in 3C
--- page 233 ---

Figure B.20 – 3C’s TradingView view
And here’s my order:
--- page 234 ---

Figure B.21 – The 3C order
But the gods of trading wanted to humble me and I had to cancel my trade... because I didn’t catch the train:
--- page 235 ---

Figure B.22 – The trade ran from me
Using ATR bands
Let’s introduce a new indicator to our trading. It’s called ATR Bands by TheTrdFloor, and what it does is draw two
bands, one above and one below the price based on the Average True Range (ATR).
A trick when searching for an indicator or a strategy is to look at the number to the right of its creator:
Figure B.23 – ATR Bands by TheTrdFloor
In this case, it’s 3467. This represents the number of people who have added the indicator, and the bigger it is, the
better the indicator is (usually). With a low number, you can find some gems out there, but you’ll mostly find indicators
with mistakes in them.
These are the settings that I’ve changed:
--- page 236 ---

Figure B.24 – The ATR Bands settings
Basically, it’s calculating the ATR over 14 candles, and that result is multiplied by 2 and plotted on both sides of the
close. There are additional settings, such as displaying a TP band based on the ATR, which is intriguing, but for now,
this is sufficient.
June, 10 – Trade 3 DATA/BUSD
Now, I’m scrolling through my watchlist, which contains all the BUSD pairs listed on Binance. I usually work with a
smaller watchlist, featuring the top coins I trade daily, but I wanted to identify where the ATR Bands indicator could
best fit. I do this by searching for RSI divergences or oversold signals. This serves more like a filter to determine
which coins I should consider for entries. Here’s what I’ve found:
--- page 237 ---

Figure B.25 – The DATA/BUSD entry
This is an interesting trade. RSI shows oversold. There’s also an RSI divergence from the latest oversold section, but
the volume is rising on a price decline.
In this game, you can always find valid reasons to contradict the arguments to enter a trade. What is important is to
balance those reasons until you find one set is sufficiently bigger than the other to act upon. And if it isn’t, it’s always
safer to protect your capital by staying out of that trade.
Normally, what other more cautious traders do is wait for the price to recover instead of trying to catch a falling
sword. I agree with this, but there’s also a potential pullback that I can take advantage of, even if the price continues
to fall.
One thing to note is that the volume increases on smaller and smaller candles with lower wicks that get rejected. With
BTC on the lower side of the channel, I expect a reversal here.
The arguments pro trade are as follows:
Oversold RSI
BTC on a support line (of the parallel channel) with a good probability of rising
RSI divergence (though far apart and indicating a longer-term potential for reversal)
Trend weakening due to smaller candles on higher volume with rejection wicks
The arguments against the trade are as follows:
Rising volume on a price decline
A falling sword (no confirmation of reversal)
It’s a risky trade, but I like it.
--- page 238 ---

The ATR bands help me when placing the SL. I am going for a risk/reward ratio of 1.6 (the distance from TP to entry
price (EP), divided by the distance from EP to SL), making sure my SL is at least double the ATR volatility band.
Figure B.26 – The trade confirmation
Note that I’m trading with half the sum I would usually commit ($440). This is due to the higher risk. If BTC creates a
lower wick mirrored by DATA’s price movement and my confidence increases due to the nature of the price action, I
might contribute the remaining amount later.
Six days later, still in trade:
--- page 239 ---

Figure B.27 – DATA/BUSD 6 days later
I advise against holding onto any trade for an extended period (unless you’re employing a trend-following system). The
key reason is the risk of price fluctuations due to unforeseen events such as wars, US presidential elections, and
pandemics. These could significantly impact your trade if it’s held for too long. On a more immediate scale, consider
an FTC hearing occurring on day three of your trade. The resulting volatility might trigger your SL (or TP). Even with
a 50–50 outcome, such an event can influence your returns.
A NOTE ABOUT PRICE SHOCKS
Price shocks are very hard to identify even when backtesting. Imagine that you overfit your strategy on a particular timeframe with two price
shocks, catching both. You would think it’s a very good strategy, but you actually catch the profit of a volatile situation that is unrelated to your
indicators. What this means is that you might just as well catch the other end when trading with real capital.
Trade ended 10 days later. We can also see how the RSI gave an overbought signal.
--- page 240 ---

Figure B.28 – DATA/BUSD 10 days later
And here’s our profit:
Figure B.29 – The end result
June, 10 – Trade 4 GRT/BUSD
GRT/BUSD is a similar trade to DATA/BUSD, and taking the trade usually means that you are doubling the money on
the same event, not that you’ve found another opportunity.
Here’s my entry for GRT/BUSD:
--- page 241 ---

Figure B.30 – The GRT/BUSD entry
Note that there’s a white (green) candle forming, so the price is trying to pull back.
The same conditions as DATA/BUSD and the same arguments for trading versus not trading apply. As I’ve
mentioned, this is just doubling down on a (risky) trade:
--- page 242 ---

Figure B.31 – Trade confirmation
This is the result:
--- page 243 ---

Figure B.32 – GRT/BUSD
And here’s the profit:
Figure B.33 – The end result
I did this second, almost identical, trade to illustrate a case. When you trade identical patterns that mirror BTC’s move,
on the same timeframes, around the same time, you just double down your money on your strategy. If you haven’t
tested it properly, this can lead to loss of capital. So, why not invest more time in thoroughly researching a potential
trade and leverage your risk management strategy to determine the right amount to stake?
A NOTE ON THE CORRELATION OF MARKETS
An important thing to understand, when trading, is that most tokens on CEXes follow BTC. There are many reasons for this, such as market
makers, arbitrage, correlation trading, and high-frequency algorithms.
--- page 244 ---

When you trade, it’s important to hone your skills on BTC and then go for the altcoins. Altcoins provide you with bigger rewards, but they are
more volatile and have increased risk. For example, if BTC drops, they drop further; if BTC recovers, they recover better, and sometimes they
don’t correlate with BTC as you’d expect.
June, 12 – Trade 5 POLS/BUSD
Where are my mistakes?
Where are the losing trades?
I had four wins, right?
Wrong!
I actually had a partial TP for trade 1, BTC/BUSD, and then I couldn’t catch the second trade, so that’s a neutral
outcome. Then, there are two trades that mirror each other, which could’ve been two losses.
So, it’s two risky wins and one partial win.
I would’ve preferred to lose a bit at first, as this doesn’t sound that realistic, but it actually is. It happens because I’ve
analyzed the trend on BTC and I’ve followed the price action. And it also happens because of luck, as well as
statistics and game theory (I’m in the lucky part of the month!).
Let’s see how the story continues.
POLS is one of the tokens I usually watch. It is a launchpad that was very successful during the last bull market;
taking a long there is also fundamentally safe (as there are a lot of buyers who intend to buy at lower prices).
Figure B.34 – The POLS/BUSD entry
This looks nice. We have a bullish divergence there, a resistance line, and a downtrend on a lower volume.
--- page 245 ---

A trick I use to speed up my trading is to take the values from TradingView’s long (or short) position inputs, after I put
them on the chart, and paste the TP and SL directly into 3C
By clicking on the long or short position drawing in TradingView, you get this screenshot:
--- page 246 ---

Figure B.35 – Taking values from TradingView
--- page 247 ---

We confirm the trade:
Figure B.36 – The trade confirmation
And it’s a win.
Ignore the /USDT pairing; the pair was starred in my 3C account, and I traded it by mistake in my main account. I
also entered the trade with $850 instead of $880. What can I say? It was a busy day, and I was multitasking.
--- page 248 ---

Figure B.37 – POLS/BUSD
Here’s the end result:
Figure B.38 – The end result
June, 14 – Trade 6 XVS/BUSD
I think you’ve got the gist of it. Now, let’s move faster:
