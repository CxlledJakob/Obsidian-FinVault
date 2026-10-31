# Zero to Hero in Cryptocurrency Trading.pdf — pages 115–134

--- page 115 ---

Here’s what it means:
PrevATR: The ATR of the previous period.
n: The period of time over which the ATR is calculated. Typically, this is set to 14 periods.
TR: The true range for the current period. It’s the greatest of the following values:
The current high (H) minus the current low (L)
The absolute value of the current H minus the previous close (C)
The absolute value of the current L minus the previous C
Here are the three methods for calculating TR:
Figure 4.6 – The three w ays to calculate true range
Note that when you have volatility and a 24-hour trading exchange, you won’t need to calculate the last two situations
for TR because the previous C is the current open (O), basically already between H and L. So, if you’re trading on
Binance, the TR formula is H - L.
The first ATR = (1/n) * Σ(TRi) for i = 1 to n.
You can find the whole method for calculating the ATR on Investopedia at
https://www.investopedia.com/terms/a/atr.asp, and you can go to StockCharts for an example:
https://school.stockcharts.com/doku.php?id=technical_indicators:average_true_range_atr.
As previously suggested, I recommend you go through these resources so that you really understand the intricacies of
the indicator. In short, ATR is the average of the highs minus the lows but smoothed so that it gives more importance
to recent values. Additionally, it shows the fluctuation between those two. Imagine a trading rule where you exit the
--- page 116 ---

trade at a loss whenever the price falls below the entry point by twice the average true range. This is called setting a
stop at 2 ATRs, and it is a technique used by traders when exiting a trade.
In the following figure, I’ve added two indicators: the default ATR indicator (the red line in the lower part of the
screen), and ATR trailing stops colored by HPotter, an indicator that applies the ATR values on the main chart,
showing you where a stop loss could be placed based on ATR multiples:
Figure 4.7 – TradingView ’s average true range
Activities
1. Go to https://www.investopedia.com/ and search for Average True Range.
2. Read all about it.
3. Understand the mathematical formula behind it.
4. Add the ATR indicator on TradingView on BTCUSD 1m.
5. Set the indicator length to 3.
6. Calculate the ATR for the last three candles.
--- page 117 ---

7. Set the Smoothing setting to SMA and check the result again. Notice how Smoothing impacts the formula and remember this for when you use
an external ATR indicator (using Python libraries), where you won’t apply Smoothing to the result.
8. Let the price run for 10 more minutes (10 candles) and see how the ATR evolves.
9. Imagine drawing a line at 2.5 ATRs under the price. How often would that line be touched? Does the ATR help protect your trade from normal
price fluctuations?
Volume - market volume
The market volume, also called the trading volume, the volume, or the volume indicator, measures how much the token
has traded during each candle.
The higher the volume was, the more intense the battle in that candle was.
A high volume on a big white (or green) candle means that the battle was intense, yet the bulls had a clear win. It also
means that during that period, the token was very interesting for the traders and that there was high liquidity in play
there. This means that there are both buyers and sellers in play, so it’s easy to trade the token.
When the volume rises together with the price, we say that the price is sustained. This means that even when the
battle is fierce (high volume), the token rises in price (bulls win). It’s considered a healthy rise. Here’s what it looks
like on a chart:
--- page 118 ---

Figure 4.8 – Volume rising w ith price
When the volume falls while the price rises, the rise is not supported by the volume. Even though the token rises (bulls
win), there’s not that much interest (not many bears have entered the fight), so, when they enter, the outcome might be
different. It’s considered an unhealthy rise:
--- page 119 ---

Figure 4.9 – Volume decreasing as prices rise
I’m curious if you’ve noticed a difference between the two charts in the way the volume indicator is displayed. If you
haven’t, stop right here and check the images again.
Maybe you noticed the MA line moving on the volume chart in the first image, which didn’t exist in the second. I
usually use MA30 when checking the volume so that I have information regarding the historical direction of the volume
rather than just the last few candles.
The purpose of this brief exercise is to illustrate a scenario in which a trader may advocate for a specific trading
technique. However, without using the precise settings that the trader has adjusted on their particular indicator,
replicating the same results becomes unfeasible. In this case, I’m also taking into account the direction of MA30 when
trading the volume. This example underscores the importance of understanding not only the trading method but also the
precise configuration of the tools being utilized.
When the volume rises while the price falls again, the volume sustains the price and the bears are winning:
--- page 120 ---

Figure 4.10 – The volume rises w hile the price decreases
And when the volume falls while the price falls, the fall is not supported because the bulls were not there for the fight:
--- page 121 ---

Figure 4.11 – The volume decreases w hile the price decreases
When the price reaches a new (local) high or low on decreasing volume, a reversal might be expected. You can see in
Figure 4.11 how the low was touched on decreasing volume at 13:00, then again at 15:00, and then it reversed on
increasing volume.
Here’s an image that summarizes how volume usually works:
--- page 122 ---

Figure 4.12 – The relationship betw een price and volume
There are more things to notice with volume. Various chart patterns can be confirmed with this indicator, and price
stories can be explained. Let me outline a few situations:
Trend confirmation: I’ve mentioned a few examples in which a price rise supported by a rise in volume is bullish, while a fall in volume during a
price rise would be an unsupported rise (indicative of a trend reversal) and vice versa. When volume is low, the signal is weak. Pullbacks (shortterm drops in price) are confirmed when they have a lower volume. Otherwise, they might turn into trend reversals (more permanent changes in
the trend).
Pattern confirmations: Chart patterns can have their structure confirmed by volume. Imagine a triangle pattern where a breakout occurs on a
high volume. The volume means there is an increase in trading happening there, so there is more potential for the move. The same thing
happening on a low volume means no one is looking. When they look, a reversal may occur.
Exhaustion moves: When the market rises and you see a sudden sharp rise in both volume and price, it might mean that the trend is ending and
there’s potential for a reversal. That’s because everyone joined in the move (afraid of missing out), and now there are not that many buyers left.
This also applies to a market drop.
Liquidity potential: Where there is volume, big orders can be taken. With a lot of trading in the area, banks, funds, and other big players can
add their bigger orders.
--- page 123 ---

Volume history: Don’t look at one volume bar. Look at the local range of bars. This is why I’ve added MA30 to the volume indicator. Was the
volume high 20 candles ago and now it’s very low? It seems that the pattern we’ve identified is not yet interesting for the traders. Is the volume
starting to rise, compared to the last period, on a bearish pattern? We might see a market decline.
I use volume mostly in manual trading and ignore it in automatic trading. That is because I prefer very clear numbers
and conditions in automatic trading, which I don’t usually get from volume. I recommend you read A Complete Guide
To Volume Price Analysis: Read the book then read the market by Anna Coulling to know more about how to trade
based on volume.
Activities
1. Go to https://www.investopedia.com/ and search for Volume.
2. Read all about it.
3. Understand the mathematical formula behind it.
4. Add the volume indicator in TradingView on BTCUSD 1H.
5. In the indicator configuration, set the MA length to 30 and check Volume MA in Style.
6. Identify three chart patterns and see how the volume confirms or invalidates them.
7. Go to https://www.investopedia.com/ and search for On-Balance Volume (OBV).
8. Read all about it, add it as an indicator, and play with it a bit. Understand the differences between OBV and volume. OBV is my second go-to
indicator in the volume category, and I would definitely recommend you add it to your repertoire.
Trend analysis - divergences
Divergences are among the most powerful tools in trading, but they are often misunderstood. Most traders trade with
them, but when they try to automate the trading, the process becomes elusive.
A divergence can be considered an imbalance between what the price chart shows us and what an indicator shows,
with the presumption that this will lead to a trend reversal. The indicator is usually an oscillator, as they are particularly
suited to showing overbought or oversold conditions, but they can also be other types of indicators, such as OBV.
Let’s consider the four divergences in the following figure:
--- page 124 ---

Figure 4.13 – Class A divergences
In Figure 4.13, we have the following:
Regular bullish divergence: The price has lower lows, and the oscillator has higher lows
Hidden bullish divergence: The price has higher lows, and the oscillator has lower lows
Regular bearish divergence: The price has higher highs, and the oscillator has lower highs
Hidden bullish divergence: The price has lower highs, and the oscillator has higher highs
These are called Class A (Strong) divergences. Class B (Medium) divergences have the price at a resistance line
(bullish, think double-top) or support line (bearish, like in a double-bottom), and Class C divergences have the oscillator
at a resistance line (bullish) or support line (bearish). They are weaker, and I don’t usually trade with them, but it’s
better to notice them on the chart when they happen:
--- page 125 ---

Figure 4.14 – Divergence types
Also, here’s an easy way to remember divergences: look at the lows for bullish divergences and look at the highs for
the bearish divergences.
Regular divergences are reverse signals, with the bearish one pointing to a local top and the bullish one to a local
bottom. Hidden divergences are continuation signals, and they occur during an existing trend (usually when a pullback
has finished inside that trend).
Divergences have an advantage over other indicators out there in that they are predictive in nature. They are basically
leading indicators (the opposite of the common lagging indicators traders usually use).
Their disadvantage is that you don’t actually know how long it takes for the price to do what the divergence suggests.
To make it easy, we’ll look at the RSI divergences, since we’ve already covered the RSI indicator.
If you look at the four following diagrams, you’ll notice that Figure 4.15 is a regular bullish divergence, suggesting a
price reversal. But in Figure 4.16, the price continues to fall, providing an extended divergence. Then it continues
again, in Figure 4.17, at which point the price rises (shown in Figure 4.18):
--- page 126 ---

Figure 4.15 – Divergence
--- page 127 ---

Figure 4.16 – Divergence (extension)
--- page 128 ---

Figure 4.17 – Divergence (still extending)
--- page 129 ---

Figure 4.18 – And finally, the bullish trend reversal I w as expecting
So how do we know when the price follows the prediction? We can’t just wait for it indefinitely.
Let’s define a trend by the general direction over a sufficiently long period of time and momentum as a shortterm burst that can happen against the current trend.
Since RSI is a momentum oscillator, and it’s, by default, based on the last 14 candles, its memory is quite short. So, we
can expect it to work in the range of 15 to 30 candles. We can’t call it an RSI divergence if it started 50 candles ago
on a 14-candle RSI momentum oscillator, but we can modify the indicator to use more historical candles and see
what’s there. I personally know a trader who trades a longer RSI thinking it will get him ahead of the general
population of traders. I haven’t looked over his tests, so I don’t know how well he puts everything into practice, but my
personal opinion is that modifying indicators to better suit you is a good direction. In this way, you’re frontrunning a lot
of bots and newbie traders.
--- page 130 ---

Professional traders also use the rate of change (RoC) indicator to pinpoint when the momentum will change
direction. I recommend you learn more at https://www.investopedia.com/terms/r/rateofchange.asp.
Activities
1. Go to https://www.investopedia.com/ and search for Divergences.
2. Read all about them. There are multiple articles, but here are three I recommend: https://www.investopedia.com/articles/trading/04/012804.asp,
https://www.investopedia.com/terms/d/divergence.asp, https://www.investopedia.com/articles/forex/07/divergence.asp
3. Understand the advantages and drawbacks of using them.
4. Add the Divergence indicator in TradingView on ETHUSD 4H. You can also use one from Community Scripts. Also, add the RSI oscillator to
your chart.
5. Identify all of the divergences mentioned, including types B and C. You can change the time frame to find more opportunities.
6. When you notice a divergence, try to identify the point at which you would have entered the market if you had not known the outcome in
advance. Then, determine whether the price moved in the anticipated direction or whether the divergence continued. Count the candles, and if it
extends over too many, change the indicator length/history to take more candles into account. See how it behaves then.
7. Go to https://www.investopedia.com/ and search for Rate of Change.
8. Read all about it, add it as an indicator, and play with it a bit. Use it with the divergences indicator and see if it helps or hinders.
9. (Advanced) Now remove all indicators from TradingView and try to spot the divergences without the indicator. How do you do it? You know that
the RSI formula tells you that the indicator drops when the price loses its power. Check for good upward momentum in an uptrend followed by a
peak and then weak upward momentum. If you add the indicator, you’ll notice that the weak upward momentum (after the strong momentum)
creates a divergence. Understand this well and you won’t need the oscillator to spot the RSI divergences.
10. (Advanced) Tell the story of these elements that generate the divergences: fear, greed, momentum, oscillator, and price. What are they telling
you right before the divergence happens?
Moving averages, the relative strength index, the average true range, the market volume, and divergences are the
basic tools every trader should know. By learning them and understanding how they work, you’re actually getting
ahead of all the traders who add an indicator to the chart and expect it to just point to the winning trade. Make sure
you go through all of the activities mentioned and ask ChatGPT to explain the terms of the mathematics that you are
still struggling with.
A template is available on GitHub, which features 36 indicators broken down into the aforementioned five categories.
This template comes with my suggested settings and includes a sheet dedicated to testing purposes.
Summary
I hope I haven’t scared you with all of the mathematics and other extra information. I’d like to balance it by promising
you that, by the end of the book, you’ll also get a tool that takes into account all of this (fees, repainting, intra-day
candles) when doing the backtesting and forward testing for your strategy. But, in order for you to use it, you need to
understand what you’re trying to accomplish and why you need to take all of this into consideration.
My goal in this chapter was for you to understand the story of the price told through indicators and to start seeing
through the different lenses the indicators provide so that you’ll be able to use them to predict the direction of the
price.
--- page 131 ---

In the next chapter, we’re going to talk about the centralized exchange and how we can trade there.
--- page 132 ---

5
The Centralized Exchange
In this chapter, I’m going to present how the centralized exchange (CEX) works and how to trade there, as well as
discuss a tool that connects to these CEXs and allows you to trade with an easier-to-understand yet more advanced
interface.
My goal for this chapter is for you to understand the types of orders you can issue on an exchange, how they behave
there, and what actually happens when they get executed.
One of the main differences between good traders and bad ones is that good traders know in detail what they are
doing and base their trades on a good analysis while bad traders trade emotionally, hoping the price will increase
because of <insert any invalid reason here!>.
Here are the topics we’ll cover:
The CEX
Long versus short
Types of orders
Spot versus futures
Leverage and liquidation
The order book, market depth, commissions, spreads, and slippage
A metaphor for it all – 3Commas
What is the CEX?
CEXs are platforms that act as an intermediary to facilitate the buying and selling of cryptocurrencies (and other
assets). They are also custodians of your funds and wallets.
The term centralized refers to the fact that there’s an entity controlling these exchanges and, by trading there, you are
placing a lot of trust in that entity, including trusting it with your money.
In crypto, we also have decentralized exchanges (DEXs) that use peer-to-peer systems to facilitate exchanges
without the user ceding a lot of control to the entity.
A list of CEXs can be found here: https://coinmarketcap.com/rankings/exchanges/, with Binance being currently at the
top. There’s also a list of DEXs, though we won’t use them for trading just yet:
https://coinmarketcap.com/rankings/exchanges/dex/.
As you can see in the first list, Binance is at the top, so I’m going to use screenshots from this exchange in this section
of the book. Here’s how the main page looks:
--- page 133 ---

Figure 5.1 – A first look at Binance
I also recommend you check Binance’s FAQ, which includes a guide on how to best use the exchange (as well as
video and text guides for most of its functions, including trading): https://www.binance.com/en/support/faq/. There’s
also Binance Academy and Binance Learn & Earn found in the menu (the nine dots in the top left), where you can
learn more about the various features available and more about crypto in general.
For the purpose of this book, I’m going to focus on the relevant section of the exchange, and I won’t bother you with
tools such as NFTs, farming, earning, and the launchpad.
Depositing money
Depositing money on Binance (and other CEXs) is quite simple:
1. You create an account there (on Binance, you do this by clicking on the yellow Register button). If you’re from the US, use
https://www.binance.us. Otherwise, please use https://www.binance.com.
2. Choose Buy Crypto from the top menu via Bank Deposit (usually the most advantageous in terms of fees, but not the quickest), Credit/Debit
Card (usually the quickest but with some additional fees), or the other alternatives.
3. The next steps are pretty straightforward. You select the currency you want to deposit and send it to their bank account (read everything they
show you as you might need to add a specific keyword in the bank transfer details field). If you’ve chosen to deposit via credit or debit card, you
just fill in your card details.
4. Your money should arrive in the specified currency (usually BUSD if you’ve transferred USD).
Trading sections
From the Trade menu, you can use Binance Convert to quickly convert your deposited funds into another token. For
example, you might need USDT, so you select BUSD in your first field, USDT in your second, and click on Preview
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
