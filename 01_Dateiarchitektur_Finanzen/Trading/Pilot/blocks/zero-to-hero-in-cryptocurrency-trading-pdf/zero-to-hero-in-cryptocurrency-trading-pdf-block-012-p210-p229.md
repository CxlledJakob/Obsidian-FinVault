# Zero to Hero in Cryptocurrency Trading.pdf — pages 210–229

--- page 210 ---

We are running this strategy at a daily timeframe by default and using moving averages 9 and 21 for it. The last two
lines tell us that we need at least 21 candles loaded before we take any action and that this strategy can’t short:

    minimal_roi = {
        "0": 10.5
    }
    stoploss = -1.0
    trailing_stop = False
    process_only_new_candles = False
    use_exit_signal = True
    exit_profit_only = False
    ignore_roi_if_entry_signal = False
We don’t use minimal_roi, stoploss, trailing_stop, and so on. If you’re wondering how they work, all of these
parameters can be found on the Freqtrade website with detailed explanations and examples (http://freqtrade.io):

    order_types = {
        'entry': 'market',
        'exit': 'market',
        'stoploss': 'market',
        'stoploss_on_exchange': False
    }
    order_time_in_force = {
        'entry': 'gtc',
        'exit': 'gtc'
    }
    plot_config = {
        'main_plot': {
            f'sma_short_9': {'color': 'red'},
            f'sma_long_21': {'color': 'yellow'}
        }
    }
    def informative_pairs(self):
        return []
We left the defaults for the orders and added the moving averages to plot_config so that we can plot the entries if
we want to.
Next, we fill a dataframe with the values of the moving averages:

    def populate_indicators(self, dataframe: DataFrame, metadata: dict) -> DataFrame:
        dataframe['sma_short_9'] = ta.SMA(dataframe, timeperiod=self.ma_short)
        dataframe['sma_long_21'] = ta.SMA(dataframe, timeperiod=self.ma_long)
        return dataframe
    def populate_entry_trend(self, dataframe: DataFrame, metadata: dict) -> DataFrame:
        conditions_long = []
        conditions_long.append(qtpylib.crossed_above(
            dataframe[f'sma_short_9'].shift(1),
            dataframe[f'sma_long_21'].shift(1)
            ))
        if conditions_long:
            dataframe.loc[
                    reduce(lambda x, y: x & y, conditions_long),
                    'enter_long'] = 1
        return dataframe
populate_entry_trend() is the function that sets the buying conditions. Here, it will trigger a long every time MA 9
crosses MA 21:

    def populate_exit_trend(self, dataframe: DataFrame, metadata: dict) -> DataFrame:
        conditions_exit_long = []
        conditions_exit_long.append(qtpylib.crossed_above(
            dataframe[f'sma_long_21'],
            dataframe[f'sma_short_9']
            ))
        if conditions_exit_long:
--- page 211 ---

dataframe.loc[
                    reduce(lambda x, y: x & y, conditions_exit_long),
                    'exit_long'] = 1
        return dataframe
And finally, we exit when MA 9 crosses below MA 21.
You can find the code in the PrivateMACross.py file in the Chapter_08 folder on GitHub.
Basically, just as in our TradingView strategy, we buy every time SMA 9 crosses over SMA 21 in the time range 27
March 2020, 00:00 to 27 March 2021, 23:59 on BTCBUSD 1D and we sell when SMA 21 crosses over SMA 9.
Next, we backtest it:

docker-compose run --rm freqtrade backtesting --config user_data/config/config-backtestingbook.json --strategy PrivateMACross --timerange 20200327-20210328 --timeframe 1d -p BTC/BUSD
And here’s the output:
Figure 8.14 – Backtesting PrivateMACross in a bull market
We have 8 entries with a 62.5% win rate, a total profit of 25.36%, a cumulative profit of 253.35%, and a drawdown of
0.39%. That’s because we caught the entire bull run in our time range. Congratulations :)
--- page 212 ---

Looks like a good strategy, right?
But what would a bear market look like?

docker-compose run --rm freqtrade backtesting --config user_data/config/config-backtestingbook.json --strategy PrivateMACross --timerange 20210811-20220812 --timeframe 1d -p BTC/BUSD
Figure 8.15 – Backtesting PrivateMACross in a bear market
Here, we’ve still got 8 entries but with a total 25% win rate, a profit of -1.49%, and a cumulative profit of -14.93%.
(Note that if you want to go down the rabbit hole, just add --timeframe-detail 30m to the backtesting process.
Suddenly, the results vary. I’ll let you figure out why.)
So... in a bull market, this strategy provides a clear win, and in a bear market, a clear loss. Guess you’ll need to figure
out when they happen, right?
The core objective when developing your own strategy is to pinpoint a set of straightforward rules that yields solid
results without precipitating massive drawdowns. The trick is to analyze the trades that fail and devise additional rules
to filter those out while avoiding overfitting. Begin with a simple, profitable system and then backtest it and observe its
--- page 213 ---

performance in a paper-trading environment. Next, establish rules that the system must invariably follow or avoid. This
not only preserves the profitable strategy but also enhances its return on investment (ROI). Any objective input
added should be rigorously tested to confirm its positive impact before it’s permanently incorporated, as these are the
elements that can lead to overfitting during backtesting.
Crafting a strategy in Freqtrade entails considerable effort, including a command of Python, a deep understanding of
backtesting, and a touch of statistics. However, the more you immerse yourself in the process, the more
straightforward it becomes, to the point where you can swiftly evaluate strategies proposed by well-known Youtubers
and find amusement in their outcomes. The task of discovering your own effective strategy is an entirely different
story. It requires a fair share of sweat equity, but rest assured, it’s a form of toil that pays dividends.
In the subsequent section, I’ll share a few trading ideas and angles that you may consider researching and maybe
transforming into trading strategies.
Trading ideas
The following is a collection of trading concepts, presented without a particular sequence. Feel free to explore and
utilize any that appeal to you. However, bear in mind that you might come across some that are initially difficult to
comprehend and that might require further research:
Start easy. Learn about some good indicators for beginners such as the ones I mentioned in the indicators template provided in Chapter 4 (and
also found in the Chapter_04 directory on GitHub).
Most of the strategies that work in bull markets don’t work in bear markets and vice versa. Instead of creating a new strategy, why not dedicate
your time to defining a correct trend (bullish or bearish), maybe coding a TradingView indicator, and setting an alarm for when the trend changes?
Then, you can trade (automatically) using the proper strategies for the current market. (Technically, look into ADX, MA crosses and gaps,
Hidden Markov Models, and the Hurst exponent.)
If a strategy gives very bad results, try to inverse its conditions. It’s not that simple (there are other inconveniences such as fees), but see what
happens.
Many individuals, including novices and experienced traders alike, actively trade RSI divergences. Look further, maybe into indicators that work
with volume, as this is an area most traders ignore. Keywords are market profile, time-price-opportunity charts, and volume profile. One
of my ideas is that tokens with a normal trading volume move in the general market’s direction and are dominated by high-frequency algorithms
and institutional traders, so why not ignore them and check for a big change in volume before trading? Tokens with high volume relative to their
history might move independently of the market.
Study token launches. See how the token reacts in bull markets versus bear markets. Most tokens have a liquidity deposit at the listing, after
which their price drops (because the public round investors are selling the tokens), and then the price drops some more, regularly (when public,
private, and seed round investors are selling). After the coffers are dry, the token shows its potential by rising (or staying down). One of my best
(manual) strategies is figuring out when the token is drained enough and starting to rise.
Volatility trading is a good angle. Think something along the lines of if a system is X% volatile, exit after Y number of candles if at least Z%
profit is gained. Instead of identifying an exit condition, find the best entry and then exit when you are profitable enough due to volatility.
Think of BTC’s volatility and its general uptrend. Why not have a pseudo-grid bot that performs a martingale-style DCA during BTC’s
volatility? It would suffer from heavy drops (by running out of stake) but it would work in any uptrend or sideways market and even on slow
downtrend markets. Always take profit on the rise. Move it to other good coins for increased profits. (Technically, for BTC, you could use $500
buys in steps from 18k to 25k and when you successfully run this strategy, add other big tokens with good fundamentals).
I’m a technical trader and love the calculations involved there, but there are good fundamental traders and news-based traders out there. Figure out
a news source that powerfully impacts the market (such as the FED announcements or a very famous YouTuber) and backtest trades such as “buy
instantly on positive FED comment, sell after x%” or “wait for a YouTuber to release a video on a low cap coin and buy instantly, sell after x%.”
Make sure it works before you put it into practice. I did this from another angle: I’ve linked a bot to various launchpads’ Telegram announcement
--- page 214 ---

channels and bought the instant those launchpads announced they were providing a crypto project for investment to their token holders. Here,
the more creative you are, the better the returns are.
Create a graveyard for your strategies. I have over 100 strategies in my graveyard, sorted by indicator category (and trend). When I’m bored, I
venture there, feeling like Frankenstein, attempting to revive one of his creations. It sometimes works, and when it does, you have a strategy
that you are familiar with.
Modify the indicators that are already (kind of) working. Change their parameters. For example, most indicators are fit for trading the stock
market, which is closed during the weekends, so they are typically trading for 22 days. Crypto trades for 30-31 days so maybe by adding more
historical candles to the indicator, we can fit it into a particular cycle. That’s just an idea but play with it; who knows where it could lead you.
After a market crash, I trade a short-term mean reversion strategy around the lines of when the token falls by x% buy, sell after it gets back to
x%. This strategy works when the fundamentals of the token are sound, but it has limited upside and unlimited downside. You might find yourself
with a bag and you might run out of capital doing it if the market drops further. It also fails when the direction is more down than up. Think of
adding a martingale strategy to it and it could work. The strategy only works because of the volatility (which is pretty big in crypto).
Think of trading on decentralized exchanges (DEXes). There, you don’t always have Market Makers on the listed tokens (who play with
the price, affecting how the market looks) so trading is a bit more straightforward. Also, tokens that have not been listed on CEXes and that have
a low market cap have the potential of doubling and even tripling in price (or they can also go to 0). Higher risk, higher reward.
Test these scenarios: momentum strategies and the bull flag on small tokens (small caps or low volume ones), support and resistance strategies on
medium tokens, and moving averages and price reversal strategies on large tokens. I’m currently running an ATR-based strategy that’s focused on
volatility spikes on small caps and it’s pretty successful.
Check for power plays: use Crypto Pairs Screener to filter for Relative Volume of at least 1.5, high ATR, big volume, and a high % change.
Something big is happening there; figure out what and trade it.
I WANT TO LEARN MORE ABOUT ALGORITHMIC TRADING
I’ve mentioned that this book is not dedicated to algorithmic trading, I’m just scratching the surface, but Packt did release a relevant book:
Learn Algorithmic Trading – Build and deploy algorithmic trading systems and strategies using Python and advanced data analysis by
Sebastien Donadio and Sourav Gosh (https://amzn.eu/d/aUOx0Kv). It has over 350 pages talking about algorithmic trading
fundamentals, trading signals generation and strategies, algorithmic trading strategies, building a trading system, and
challenges in algorithmic trading, and I highly recommend it.
Summary
In this chapter, we explored the intersection of trading strategy and technology by touching on the learning aspect of
how to code a custom indicator on TradingView and an algorithmic trading strategy on Freqtrade. This process allows
us to convert our unique trading philosophies into precise, automated systems capable of continuously monitoring and
executing trades in the cryptocurrency market.
My goal here was to illustrate the potential of Pine Script and Freqtrade. This chapter was designed to ensure you’re
aware of these tools, to be revisited when you have your own manual strategy. Embracing the ability to automatically
test and deploy strategies 24/7 is a key advantage in trading.
The following is our final chapter in which we conclude our journey together and I will give you some further
resources for the road ahead.
Further reading
Pine Script V5 User Manual: https://www.tradingview.com/pine-script-docs/en/v5/Introduction.html
Pine Script V5 Reference Manual: https://www.tradingview.com/pine-script-reference/v5/
--- page 215 ---

Pine Script primer: https://www.tradingview.com/pine-script-docs/en/v5/primer/index.html
Community Scripts: https://www.tradingview.com/scripts/
(Free) Pine Script Basics Course: https://courses.theartoftrading.com/courses/pine-script-basics-course
Pine Script (TradingView) - A Step-by-step Guide: https://algotrading101.com/learn/pine-script-tradingview-guide/
Some public indicators and strategies I’ve posted on TradingView: https://www.tradingview.com/u/vaidab/#published-scripts
Python – a programming language that’s very easy to use: https://www.python.org/
pandas – data analysis and manipulation built on top of Python: https://pandas.pydata.org/
pandas-ta – a Python library with over 130 indicators: https://github.com/twopirllc/pandas-ta
Freqtrade’s website: https://www.freqtrade.io
Hummingbot, an alternative to Freqtrade: https://github.com/hummingbot/hummingbot/tree/development
NautilusTrader, another alternative to Freqtrade: https://github.com/nautechsystems/nautilus_trader
Cryptocurrency algorithmic trading with Python and Binance: https://www.udemy.com/course/cryptocurrency-algorithmic-trading-with-pythonand-binance
A list of Freqtrade strategies: https://github.com/freqtrade/freqtrade-strategies/tree/main/user_data/strategies
Backtesting traps when using Freqtrade: https://brookmiles.github.io/freqtrade-stuff/2021/04/12/backtesting-traps/
--- page 216 ---

9
What’s Next?
Congratulations – you’ve reached the final chapter. Even though the book ends here, your journey is just starting out.
If you’ve followed me closely, you’ve learned sufficient theory (which I hope you’ve put into practice) and you’ve
been able to develop a strategy that you trade manually or automatically.
What’s next?
I recommend following this short roadmap:
Trading technically: Learn about the tools used in Exocharts (http://exocharts.com) to become even more knowledgeable. Think volume
profiles, Bid-Ask, Delta, imbalances, CVD, tick charts, range charts, and footprint charts.
Trading strategically: Diversifying into stocks, bonds, or other investment vehicles, moving to different centralized exchanges (CEXs)
based on fee offers (yes, when you trade 1,000+ times a day, the fees add up), and trading on decentralized exchanges (DEXs) (I recommend,
I’ve also contributed to, and I’ve successfully traded with LimitSwap: https://github.com/tsarbuig/LimitSwap).
Trading the news: Learn how to trade by news. There are bigger gains if you can estimate how the price reacts to the Federal Reserve System
(Fed) announcements (you can even hedge on volatility, creating two trades in both directions that will close once the price decides where to go).
And other announcements can happen. I’ve successfully traded a “new coin listing on Binance” strategy where I bought when the price came out
of the initial dump hole and sold at 20%+. Other situations can’t be defined algorithmically. There, you can put your creativity to use.
Learn more about statistics: Learn how to properly test a strategy taking into account the alpha, the beta, the drawdown, the Sharpe ratio,
transaction costs, volatility, annualized returns, and a lot more. Welcome to math :)
Get a coach: If you want to accelerate your process, understand the steps, get answers to your questions, surpass the emotional difficulties, and
build your own strategy with someone, or if you just need someone to double-check your work, contact me. You can email me at
contact@vaidabogdan.com. Make sure your subject is “trading coach” so that I can quickly find your email, and expect a delay of around
48 hours until you get an answer (mailto:contact@vaidabogdan.com?subject=trading%20coach).
Take a vacation and take (real) breaks from trading: Even though it starts as a passion, seeing all the money coming in and following trades
at indecent hours adds up. You need to be able to separate this from your time dedicated to other things.
That’s it!
I wish you the best on your journey!
--- page 217 ---

10
BONUS – One Month of Trading
In the process of writing this book, I realized that while I fully believed in the materials I provided, there was a need
for something more to instill confidence in you. I pondered various approaches, ultimately concluding that nothing
motivates more than the prospect of success.
So, I’ve asked myself, what if I document a month of trading for you?
There will always be people that object to success, and they’ll have their own opinions, like so:
If I document 20+ trades, I choose the ones I won
If I document multiple trades of $1,000+, I already made a big amount of money; now, it’s easy
If I document myself starting out, I’m not a beginner; I already know how to trade
If I document a client’s progress, I’ve helped them (or chosen the client that made more money from multiple clients)
If I document myself during the bull market, of course, I’m making money – it’s the bull market
With all of these objections, what can I do to provide you with proof that the methods in this book work?
Nothing really – there are always people who will say it works, people who will say it doesn’t, echo chambers, and
whatnot.
At the time of writing, we’re in a bear market in crypto, and I love it. It’s the period when I can dedicate time to
writing and other leisurely activities, something I wouldn’t really be able to do in the bull market. This is the time when
projects build, investors protect their money, and traders lose some of theirs.
Yep, the bear market also has its downs – mainly, high spikes in volatility where trading goes against your well-defined
strategies, and it’s way harder to make money now than it is in the bull market.
So, even though we’re in the worst period for showing off, in this chapter, I’m going to document one month of trading
with a $10,000 account. I will show you what I’m doing, what my thought processes are, and how I adapt to this everchanging game.
As a disclaimer, don’t expect sensationalism. I’m 100% against that.
No, I won’t double this account in a month. Actually, if I doubled it, I would rather remove the chapter than publish it
because you wouldn’t believe me. And it wouldn’t be a normal month of trading.
I expect a conservative return of around 1–3%.
In the 3% scenario, that’s $300 in the first month, and ~$4,257 after 12 months ($10,000 * (1.03)^12 = $14,257).
In the 1% scenario, that’s $100 after one month and $1,268 after 12 months.
You can use this calculator to play with other figures:
https://www.thecalculatorsite.com/finance/calculators/compoundinterestcalculator.php.
--- page 218 ---

If that doesn’t seem much, that’s because I won’t trade with leverage, bots, or other hacks. I just want you to see the
process and the thinking behind it. You can always 10x this return with more trading (I only took 24 trades this month),
proper leverage (that comes with higher risk), and the compounding process will take care of the rest.
Note that black swan events can happen, tokens might get unlisted, and APIs might not work, and I will also document
those situations in which I might get a negative return. This can happen, and I did have one or two months a year
when this happened, usually when doing algorithmic trading.
Also, my trading day is actually boring. When I’m trading live, I’m searching for specific situations that I’ve worked
hard to define, situations that take into account a lot of things (including the S&P, the volume profile, the global trend,
BTC correlation, and more). I’m not studying all of them in every trade, but I have the background information when I
enter the trades, which adds to my chances. So, for example, even though I’ve suggested you should always check
using three indicators from different categories when trading, I usually have three results in my mind (and I’m always
biased regarding the direction of the trade). Also, I’m not a chart trader by default. I love trading on the chart, but I
don’t have the time to take into account all the info all the time. I love my life, I love traveling, and that’s why I actually
focus on algorithmic trading. Every few days, I run an idea through Freqtrade, and if it has merits, I go down the rabbit
hole, developing a theoretical trading system, backtesting it, modifying it, backtesting it again, backtesting it in-sample
and out-of-sample, and dry-running the result. I’m the type of guy who likes to have control over his own time, so this
suits me better than strategies that force me to devour the screen every day.
This is a bonus chapter, and I will trade using all my knowledge, not only what I’ve taught you in the previous chapters.
If you encounter a new terminology, a new indicator, or a different way of doing things, feel free to use Google,
YouTube, or ChatGPT to better understand how it works. I will try to teach you one thing at a time through each trade
I make, but make sure you understand every trade before you continue reading. I’m not asking you to do 100 trades
using an indicator I didn’t explain; instead, I’m asking you to read a bit about the indicator and what it does so that you
understand the idea behind the trade. Also, if you notice days I didn’t trade, I was either relaxing or busy with other
work. I try not to force myself and to keep it fun.
Preparing the tools
June 7, 2023
Tasks for today:
Create a Binance account (in my case, I just created a subaccount for this project in my main account; this feature is available for you after your
account grows a certain size and you reach the VIP level on the platform)
Create a 3Commas (3C) account
Create a TradingView account
Configure all the accounts
Link Binance’s API with 3C’s API
Set up the trading journal
Allocate $10,000 for the account
No trading for today
--- page 219 ---

June 8, 2023
Tasks for today:
Analyze BTC
Set up a trade on TradingView
Make a first trade on BTC
Note it in the journal
NOTE:
We also provide a PDF file that has color images of the screenshots and diagrams used in this book. You can download it here:
https://packt.link/pXrot.
Trading
June 8 – BTC analysis
The following is my monthly analysis of BTC, containing support and resistance (SR) lines, round numbers, the
Fibonacci Golden Channel (GC), and the Volume Point of Control (VPOC).
Figure B.1 – BTC analysis on the monthly chart
Here are some notes on the preceding chart:
I’m not including all possible SR lines but, rather, focusing on the main ones that are identified before and after significant price swings.
I also focus on the two lines before and after the current price; I don’t need to analyze a price range where BTC will not arrive for the next year.
--- page 220 ---

I’m not adding all the SR lines possible, only the main ones (found before and after big swings).
I’m not adding the line on the precise price. I’m just looking for the area where the price will react. And since I’ll be trading on the 4H and lower
timeframes, I will adjust the lines when I get there.
The only adjustment I made is a support line that I initially put at $19,960 and I’ve now moved to $20,000. I do this by double-clicking it, going
to the coordinates, and changing the price manually. The reason for this is that I prefer for the round number to stand out when I go on the lower
timeframe.
Here’s a close-up:
Figure B.2 – The zoomed-in image
If you want to learn more about the Fibonacci GC, you can check out
https://www.investopedia.com/articles/technical/04/033104.asp, and for the VPOC, check out this one:
https://phemex.com/academy/point-of-control-how-to-use-poc-in-crypto-trading.
Now, we will move on to my weekly analysis.
The first thing I will do is open the Object tree, located in the lower-right section of TradingView, and move all of my
charted objects into a folder, hiding monthly information until I chart the weekly info. It looks like this:
--- page 221 ---
--- page 222 ---

Figure B.3 – The object tree
After we’ve hidden the monthly objects, we will proceed with the weekly analysis.
Here’s what it looks like:
Figure B.4 – BTC analysis on the w eekly chart
Here are some notes:
I’ve only added the two closest support lines and the two closest resistance lines. I’m not interested in weekly price movements but in 4H ones,
so these are just for reference when we get to the 4H timeframe.
I placed the second line from the top on the last swing in May this year, but then I noticed there was resistance in that area during May last year,
so I moved it to the left to take that into account. I also adjusted it closer to the price, as mentioned before.
I experimented with the Volume Profile and observed significant trading activity during BTC’s fall from April to June 2022. However, I don’t
find its VPOC to be particularly relevant because it was a unique, singular situation. Charting the Volume Profile after the drop would position the
VPOC under the last two SR lines, making it irrelevant to our trading. As a result, I won’t include it in the weekly timeframe.
Now, I will move all the objects into a Weekly folder in the Object tree and then reveal the monthly objects. It looks
like this:
--- page 223 ---

Figure B.5 – Clutter
Next, I will adjust the following:
Hide the lines that are well over and under the price. I do this by right-clicking on them and clicking Hide.
I will delete the weekly resistance line at 29,998 because I have a stronger monthly line at 29,419. Remember, there are no exact prices in
trading, only areas where the price reacts, and here the area is somewhere around 29,400–31,100.
I will hide or delete the last three lines (19,960–21,471). If I hide them, when I redo the analysis, I will just unhide them and adjust the position.
If I delete them, I will just add them again. It’s your choice of how you prefer to work; I usually hide the monthly lines and delete the weekly and
lower ones. And to answer your unspoken question, I usually analyze BTC on a weekly basis when I’m actively trading.
There are situations where the close of a candle in a monthly chart is lower than the close of the candles it consists of
in a weekly chart, in which case I will have the monthly SR line closer to the price than the weekly SR line. I will
always prefer to keep the stronger and closer line on the chart because I want to identify the earliest moment when
the price reacts to that SR area. Remember, it’s never a specific price; it’s an area.
Here’s the uncluttered version:
--- page 224 ---

Figure B.6 – A w eekly uncluttered version
Now, I’ll quickly do the daily timeframe. I don’t like the daily that much; I’ve only used it effectively when trading a
modified TD Sequential strategy (originally created by Tom DeMark).
A NOTE ON WHY I DON’T TRADE THE DAILY TIMEFRAME
The fact that I don’t trade it doesn’t mean that you shouldn’t trade it. Still, take into consideration that trades on higher timeframes take a
longer time to end, freezing your capital and leaving you at the mercy of the market. Sometimes, sudden market events generate abnormal
behavior while you are still in trades, and even with a good strategy, you get stopped out.
On the daily timeframe, I add three lines that are actually close to the current price, and I’ll hide the GC lines. The GC
area typically serves as a potential bounce area when a price experiences a rapid decline. However, our price has
remained in that area for an extended period, making it less relevant for our current analysis.
Here’s our daily chart:
--- page 225 ---

Figure B.7 – The daily chart
I find the 4H chart, followed by the weekly and monthly charts, to be the best ones to look at. The M and W charts
provide strong SR areas, and the 4H chart is a great place to trade. The 1H -> 15m charts work too, usually on
Altcoins, as BTC is quite volatile, and it might just catch your stop loss before it goes toward your desired direction.
However, if your strategy is sound...
On the 4H chart, we can see some parallel channels:
--- page 226 ---

Figure B.8 – The 4H chart
The second channel is a continuation of the first.
And we actually have another channel, which is a bit harder to determine and not that fluid:
Figure B.9 – The “hidden” parallel channel
I love trading parallel channels; I already have some ideas in mind…
I will add the Volume indicator, find out the VPOC, and also keep on the chart the closest channels (they overlap a bit,
but I need to pay attention to them).
And with that, here’s the final version, the one I will use for trading this week:
--- page 227 ---

Figure B.10 – BTC/USD analysis
Note that I might readjust the SR lines if needed. The charting is not frozen in place, but the last figure provides me
with the information I need to propose some trades.
Also, if I don’t find anything to trade here, I will check lower timeframes or other tokens, but I won’t go into charting
again.
What are the conclusions here?
In the short term, I see BTC in a downward channel
There’s a lot of fighting (and volatility) in the 27,000 area
There’s strong support in the 23K area and good support in the 24K area
There’s strong resistance in the 29K area and not much trading between 28K and 29K (we can see this by the lack of volume on the Volume
Profile)
If BTC continues its downtrend, we can trade the parallel channel (with a higher emphasis on short trades)
If BTC takes off and gets out of the channel, we can expect a strong momentum until around 29K (a good long trade).
NOTE
Chart analysis can be self-fulfilling. Imagine all the traders putting support and resistance lines at theory-based levels, buying the double and
triple bottoms, buying the breakouts, and basically, forcing the price to react by doing exactly what the pattern says it would do.
June, 10 – Trade 1 BTC/BUSD
Since we know BTC trades in a channel, and because the price dropped to the lower channel support, an opportunity
for a long appeared. Here’s my setup:
--- page 228 ---

Figure B.11 – The trade setup for BTC/BUSD on 1D
I want to long BTC at 25,643 with a stop loss (SL) at 25,012 and a take profit (TP) at 27,271. I’m also adding a
partial TP at 26,277, just in case the price rejects the middle of the channel (in some cases, the middle line acts as
resistance and the price returns to the lower channel line). Note that these numbers (directly taken from TradingView)
might change slightly in my 3C screenshots because of slippage when entering at market price, the price difference
when switching tabs, fees, and so on.
Here’s the 3C version of TradingView:
Figure B.12 – 3C’s Trade Terminal
The following is a screenshot showing my trade setup. Note that I’ve checked the Move to Breakeven option,
which will move my SL to my entry price after 3C arrives at the first TP.
--- page 229 ---

Figure B.13 – 3C’s Trade Terminal
Now, we confirm the transaction:
