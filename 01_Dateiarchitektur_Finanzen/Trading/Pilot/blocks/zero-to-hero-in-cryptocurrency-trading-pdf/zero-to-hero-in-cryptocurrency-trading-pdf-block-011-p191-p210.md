# Zero to Hero in Cryptocurrency Trading.pdf — pages 191–210

--- page 191 ---

After you get confident in your strategy, this is the time for live action. Now you’re putting real money at stake.
Figure 7.8 – You, after a year of successful trades
Besides the lessons already learned about risk management, there is another safety tip I can give you. You can start by
putting a smaller amount, let’s say $15, when you enter the trade and continuously increase that sum up until your fixed
risk percentage (1.5%-2% of your capital).
Live action will bring up emotions that you didn’t have during testing. Emotions of thrill and euphoria, panic, and
addiction. You need to manage them while also staying on course and following your trading plan.
First, I recommend you go through all of these steps as I’ve shown them to you. Always backtest for at least 100
trades in each market, always forward-test for 100 trades, and then paper-trade for at least a month. After you
--- page 192 ---

develop three strategies that work and you’re confident in your ability to work through the method presented here, you
can skip a few steps. For example, you can paper-trade and forward-test at the same time (since you’ve already
processed your emotions and you’ve also worked through most of the forward trading challenges before). But I
strongly recommend you don’t do this for your first three strategies. Go through the process as you need to build that
mental fortitude and winning history that will help you succeed in the trading world.
Testing checklist
When testing strategies, run through this checklist to make sure you haven’t forgotten anything. Also, note that you
might not be able to manually test everything, and that’s all right. It’s okay to not be perfect and to have some
unknowns when you trade a strategy. But ideally, know the unknowns:
How many trades did you have? Testing over 3 months with 3 trades is different from testing over 1 week with 100 trades and they tell you
different things.
Did you test it through ascending, descending, and sideways trends? But did you also test it in the previous X days/weeks/months (depending on the
timeframe)? Did you test through a period where the market changed direction (situation: your filter identified a bull market, you trade it, but it
takes a while for the filter to identify that the market became bear while your strategy is still running)? Was the dataset detrended?
Are proper filters in place? Is it biased toward a certain condition/market direction/timeframe/market? When testing in different markets, did you
take into consideration that tokens might get unlisted or dumped? Does your filter take this into account (by trading large caps, for example)?
Does it take into account lower timeframes, intraday candles, repainting, slippage, fees, drawdown, and maybe even black swan events?
Do you take into account delays such as receiving the market data late, API delays if you’re using external tools, overfitting, and underfitting?
Did you account for the various situations that occur during live trading (as opposed to backtesting)?
Can it be tested automatically (for example, in a TradingView script)?
Can you give this strategy to a friend who is trading, and can they reproduce your results using your conditions?
Does it work in other markets (forex, stocks, etc.)?
A NOTE ON ADVANCED TESTING
There is more to testing a strategy than meets the eye, but I feel that what I’ve given you here is enough to develop your first productive
strategy. Still, I’d like to mention all the things that make testing an arduous process. Some keywords are alpha and beta
(https://www.investopedia.com/ask/answers/102714/whats-difference-between-alpha-and-beta.asp), Sortino/Calmar/Sharpe ratios
(https://towardsdatascience.com/sharpe-ratio-sorino-ratio-and-calmar-ratio-252b0cddc328), expectancy, total days in trade, drawdown,
overfitting, and more.
Here are some scenarios.
The strategy performs better than BTC (and the “buy & hold” enthusiasts), yet BTC is in a downtrend. Is it a good strategy?
Backtesting shows a profitable strategy with a huge drawdown. It might be that you live-trade exactly when the strategy has a string of losses
and you lose a very big percentage of your portfolio. (Then you’ll need 100% profit to recover from a 50% loss, or 400% profit to recover from
an 80% loss.)
How do you compare your strategies? Do you use a ratio such as Sharpe, VaR, total profit in percentage, or accumulated profit? What
happens if you have a strategy that’s better in one test and another that outperforms the first one in another test? (Tip: that’s when you start
learning statistics.)
If your strategy stays too many days in trade, it might catch market spikes/news/volatility grabs/SL hunting and act too random. This might
look good in backtesting, while the randomness might just as well prove to be bad during live runs.
I test my strategies with 60% training data, 20% validation data, and 20% test data. During the training, I use all my knowledge to develop the
strategy and make it beat the market as much as possible. Then, I test it on the next 20% of data (20% of a time range) and do some
--- page 193 ---

modifications or maybe hyperopt it better. The last 20% is tested only once, after I commit my strategy to my private repository. Making
modifications then would overfit my strategy to the final testing set. But what would happen if the 60% training data was during a downtrend and
the last 40% (validation and test data) was on an uptrend? A long-biased strategy might look better than it is. That’s why you can use
advanced models such as GroupTimeSeriesSplit to better distribute your data: https://www.kaggle.com/code/jorijnsmit/found-the-holy-grailgrouptimeseriessplit/notebook.
Summary
In this chapter, I helped you navigate through the complex landscape of developing and implementing a robust trading
strategy, right from understanding the system’s essentials to conducting backtests, forward tests, and even paper
trading before plunging into the live market scenario.
My goal for this chapter was to ensure you gain a comprehensive understanding of trading strategy development, with
a particular focus on identifying trading patterns, defining critical entry and exit points, evaluating strategies via
backtesting and forward testing, simulating real-time trading through paper trading, and finally, applying the tested
strategy in live action.
In the next chapter, we’re going deep, right into the art of coding and automating your strategy. Prepare for the geeky
part of the trading process.
--- page 194 ---

8
Automated Trading
In this chapter, we are going to delve into the technical side of trading strategies by focusing on the process of coding.
Our journey will begin with creating a custom indicator in TradingView, a platform renowned for its robust charting
capabilities and custom scripting language, Pine Script. Crafting your own indicator can empower you with the ability
to analyze markets in ways that align with your unique trading philosophy.
Following that, we will move on to the task of coding a strategy in Freqtrade, an open source algorithmic trading bot
that supports cryptocurrency trading. With Freqtrade, we can take our custom strategies and convert them into
algorithmic trading bots capable of executing trades 24/7 with precision and speed. This section is not merely about
writing code but also about combining your trading ideas with technical execution to create powerful, automated
trading systems.
Whether you are a seasoned coder or a novice in the field, my goal for this chapter is not to teach you how to code or
about the inner workings of Pine Script but to show you its potential and how you can take advantage of it later, after
you have your own working strategy that you trade manually. I’m not expecting you to understand all the coding that’s
happening here; this is not a book about coding, but as long as you know the tools presented here exist, you’ll be able
to come back to them when the time is right. Having a tool to test your strategies automatically and to deploy them
24/7 is a unique angle to trading and you should take advantage of it!
Here are the topics we’ll be covering:
Coding trading strategies – from Pine Script to Python and beyond
Coding an indicator in TradingView
Coding a strategy in Freqtrade
Trading ideas
Technical requirements
As Freqtrade uses Python, a basic understanding of Python is a prerequisite. This book does not cover Python
programming; however, I’ve provided a link to an Udemy course titled Cryptocurrency algorithmic trading with
Python and Binance that will expedite your Python learning journey, covering Python, Pandas, algorithmic trading,
and statistics.
Let’s start!
Coding trading strategies – from Pine Script to Python and
beyond
In the intermediate phase of my trading journey, I found myself crafting Pine Script indicators and strategies for
clients. Pine Script is the coding language used to create custom indicators on the TradingView platform. Initially, I
--- page 195 ---

began this journey by developing tools for my friends in our private trading circle. As my proficiency grew, my clientele
expanded through their endorsements.
Interestingly, many of the strategies proposed by my clients were not profitable. While these strategies had shown
promising results over one or two months during the manual development and backtesting stages, they often failed to
generate profits when deployed live. At times, any profits realized were more attributable to Bitcoin’s general bullish
trend rather than the efficacy of the strategy. However, amidst this sea of underperforming strategies, some stellar
performers sustained profitability over the years. The majority of the strategies found their niche in specific market
conditions, exhibiting profitability either during bull or bear markets, generating moderate returns monthly, or showing
high profitability with an inherent risk of significant initial drawdown (a drawdown is a decrease in the capital, which,
when it occurs right at the beginning of testing, reduces your starting balance, thus making recovery of losses more
challenging.).
The game-changer in my journey was the transition from Pine Script to Python. Python unlocked a universe of
advanced tools and techniques, including statistical analysis, correlation studies, and advanced mathematical models.
This level of sophistication facilitated the creation of highly accurate strategies and allowed for precise replication of
their results. However, Pine Script remains a highly accessible language for beginners and is widely adopted among
traders. Moreover, it offers a treasure trove of pre-built strategies ripe for tweaking and customization, making it an
excellent starting point for this journey.
We will commence with price-derived indicators and strategies, a common approach among trading coders. However,
I would like to challenge you to venture beyond the conventional. Once you gain confidence with price-based
indicators, consider exploring information not directly derived from price. We have an array of data streams at our
disposal, such as news, market sentiment, social media influence, economic calendars, announcements from the
Federal Reserve, and more. However, traders often limit themselves to Open, High, Low, Close (OHLC) data,
neglecting valuable insights from these additional sources.
Unlocking these alternative perspectives is akin to reaching a level-3 quest in algorithmic trading. However, let me
reassure you that this journey doesn’t demand deep coding expertise. Even creating a basic indicator that distinguishes
bullish, bearish, or sideways trends could be invaluable for your strategy. The consistency of applying the same code
across different strategies will lend a sense of stability in the unpredictable world of trading.
Many traders still follow traditional indicators, some dating back to the 1950s and even earlier. For instance, Ralph
Elliot’s Elliot Waves theory is still prevalent, despite its creator passing away in 1948 and the method’s statistical
shortcomings. Similarly, indicators such as the stochastic oscillator, the Relative Strength Index (RSI), the
Moving Average Convergence Divergence (MACD), and the On-Balance Volume (OBV), all developed
between the 1950s and 1970s, continue to be widely used.
In today’s world, the creation of new indicators is commonplace. However, like the underappreciation of contemporary
art in favor of classical masterpieces, the vast array of modern indicators often remains unexplored. The challenge lies
in sifting through the sea of indicators to find the one that truly adds value to your trading strategy.
Coding an indicator in TradingView
--- page 196 ---

Pine Script, the scripting language native to TradingView, allows users to construct their unique indicators and
strategies. It operates on TradingView’s servers, meaning it doesn’t burden your machine’s resources beyond
displaying data, and the scripts are stored on TradingView. Furthermore, TradingView offers access to over 100,000
community scripts.
As of the time of writing this book, Pine Script is in its fifth version, which will be the focus of our discussion.
Importantly, with each new version, backward compatibility is maintained, enabling the running of older scripts. While I
have updated some strategies from V3 to V4 and subsequently to V5, others remain in their V4 form.
However, it’s essential to clarify that this book will not delve deeply into Pine Script. My aim is to introduce you to Pine
Script, show you how to modify existing scripts to create your own, and provide resources for further learning. The
primary focus of this book isn’t on coding in Pine Script.
Editing existing indicators
Let’s go to TradingView and open an advanced chart for a market, let’s say BTCBUSD on 4H, and click on the Pine
Editor tab in the lower bar of the screen. On the right side, go to Open | Indicator, and you will get this output:
Figure 8.1 – Pine Editor | indicator template
This is the empty template of code found there:

// This source code is subject to the terms of the Mozilla Public License 2.0 at
https://mozilla.org/MPL/2.0/
// © vaidab
//@version=5
indicator("My script")
plot(close)
The code tells us that you’ll be using V5 of the scripting language and that the name of the indicator is My script and
it will plot the close of the candle.
Now click the Add to chart button on the left and voilá, you now have your script results displayed under your main
chart. You can close it with the X that appears when you hover over the chart or the other X that appears when you
hover over the script’s name. Let’s close it for now:
--- page 197 ---

Figure 8.2 – My script, added to the chart
Now, let’s say that you have an indicator such as Hull Moving Average (HMA) that you are using in your trading.
HMA is a type of moving average that was developed by Alan Hull. It is a highly effective tool in identifying the
current market trend more quickly than other moving averages, yet without sacrificing smoothness.
Add it with the Indicators button in the upper-right menu (or press the shortcut /). Then, go to its name in the upperleft part of the chart and click the {} button. This will open its code.
Figure 8.3 – HMA source code and X buttons
This is what its source code looks like:

//@version=5
indicator(title="Hull Moving Average", shorttitle="HMA", overlay=true, timeframe="",
timeframe_gaps=true)
length = input.int(9, minval=1)
src = input(close, title="Source")
hullma = ta.wma(2*ta.wma(src, length/2)-ta.wma(src, length), math.floor(math.sqrt(length)))
plot(hullma)
The title is Hull Moving Average and overlay=true means that it will be displayed on the main chart.
The indicator takes two inputs, a length value (integer), representing the historical candles taken into account, and a
Source value (which can be OHLC, open-only, close-only, or other combinations), which is used to take the values
from.
Then the value of each candle is calculated by a weighted moving average formula and the results are plotted.
NOTE
For a more in-depth understanding of each function, I encourage you to refer to the Pine Script Reference Manual (and User Manual). You’ll
find the links later in the chapter. For the time being, my aim is to provide a glimpse of the potential that Pine Script holds.
--- page 198 ---

You can use ChatGPT to walk you through an explanation of what the code does, like in this figure:
Figure 8.4 – Using ChatGPT to understand code
Next, remove the HMA indicator from the upper-left part of the chart but keep the code and make a copy by clicking
on its name, under the Pine Editor button. Rename it to Private HMA v1.
Change the line starting with length to the following:

length = input.int(12, minval=1)
Click Save and Add to chart.
This is how it will look:
--- page 199 ---

Figure 8.5 – HMA w ith modified defaults
Now you have your own HMA indicator which defaults to a length of 12 (it takes a larger period into consideration
when making the calculations).
You can use Pine Script to see how an indicator works “under the hood” and to go through the formula manually,
change default script settings, add alarms to indicators that you’re using, connect two or more indicators to one
indicator that’s fit for your trading style, and create strategies (indicators that have trading logic that allows them to be
backward-tested and forward-tested).
NOTE
I’m using the term strategy interchangeably to refer to a (1) trading strategy and (2) TradingView strategy. The first one represents the strategy
you’re developing for trading (the specific filters and entry and exit criteria), while the second one represents a way of writing scripts that can
show the results if you have entered and exited trades when the script told you so (all automated by TradingView). You’ll understand from the
context to which I’m referring.
Making your own indicator
Add the following code to a new script. You get a new script by deleting everything, clicking to the three dots on the
right of the Pine Script window, and clicking Save script as.... to give it a new name:

//@version=5
indicator("Private MA Cross Indicator")
shortLen = 9
longLen = 21
shortMA = ta.sma(close, shortLen)
longMA = ta.sma(close, longLen)
plot(shortMA, color = #9e2f24)
plot(longMA, color = #228227)
--- page 200 ---

isCross = ta.cross(shortMA, longMA)
plot(isCross ? shortMA : na, color=#144ce7, style = plot.style_cross, linewidth = 6)
This indicator will not be overlayed and, in its chart, it will put crosses on the intersection of MA 9 with MA 21.
Add this line at the end to be able to create a custom alert at the EMA intersection:

alertcondition(isCross, title="Enter trade")
That is it. Save it and you’ll be able to add the Enter trade custom alert when adding an alert on the chart. Note that
the final code can also be found in the PrivateMACrossIndicatorWithAlert.psl file on GitHub.
The next figure shows what everything looks like, in the end:
Figure 8.6 – Private MA cross indicator w ith alert
Of course, from here, things can get complicated, but if you code your indicators step by step, in no time, you’ll be able
to create the tools that can complement your trading.
Converting an indicator into a strategy
The beauty of TradingView is that we can quickly add trade logic to our indicator and transform it into a
(TradingView) strategy, which we can test.
In order to do that, we add a few lines of code to our previous indicator. Let’s say that we go long when the short
moving average crosses over the long moving average and we go short when it crosses under the long moving
average.
--- page 201 ---

In order to do this, we change from the indicator() function to the strategy() function and add the trading logic.
Here it is:

//@version=5
strategy("Private MA Cross Strategy")
shortLen = 9
longLen = 21
startDate = timestamp("01 Jan 2022 00:00")
endDate = timestamp("31 Dec 2022 23:59")
shortMA = ta.sma(close, shortLen)
longMA = ta.sma(close, longLen)
plot(shortMA, color = #9e2f24)
plot(longMA, color = #228227)
inDateRange = (time >= startDate) and (time < endDate)
if (ta.crossover(shortMA, longMA) and inDateRange)
    strategy.entry("long", strategy.long)
if (ta.crossunder(shortMA, longMA) and inDateRange)
    strategy.entry("short", strategy.short)
isCross = ta.cross(shortMA, longMA)
plot(isCross ? shortMA : na, color=#144ce7, style = plot.style_cross, linewidth = 6)
I added a time range for our strategy (so it can test a specific period) and the conditions for going long and going short.
When the short MA crosses over the long MA, it goes long, and when it crosses under, it switches to short. Since
we’re always either in a long or a short, we don’t need logic for closing trades; we’re just switching directions.
If we run this strategy on BTCBUSD 4H and go to the Strategy Tester tab, we’d get a -1% net profit. If we switch
to the 1H tab, we’d get a 0.02%-0.03% net profit:
Figure 8.7 – Strategy Tester results
So it’s not profitable, right?
Well… let me change that for you. Update the timestamps to the following:

startDate = timestamp("27 Mar 2020 00:00")
endDate = timestamp("27 Mar 2021 23:59")
Now, go to BTCBUSD 1D and you get a 2.61% net profit.
--- page 202 ---

Figure 8.8 – Strategy show ing profit
Next, comment out the lines where our strategy goes short and add an exit condition instead:

// if (ta.crossunder(shortMA, longMA) and inDateRange)
    // strategy.entry("short", strategy.short)
if (strategy.position_size > 0 and ta.crossunder(shortMA, longMA))
    strategy.exit(id="exit long", stop=close)
And voilá! A 3.74% profit in 1 year on BTCBUSD 4H. Take a look at the following graph for the output.
Note that percentages might differ lightly:
Figure 8.9 – Strategy show ing even more profit
That’s not much, but I can tweak the strategy to show you 20% or even 100% profitability.
... and I’d be lying.
Because what I’d do is just overfit the strategy to the specific market I’d be testing it in.
Change the first line in your strategy to this one:

strategy("Private MA Cross Strategy", default_qty_value=100000)
Now, it looks like this:

//@version=5
strategy("Private MA Cross Strategy", default_qty_value=100000)
shortLen = 9
longLen = 21
startDate = timestamp("27 Mar 2020 00:00")
endDate = timestamp("27 Mar 2021 23:59")
shortMA = ta.sma(close, shortLen)
longMA = ta.sma(close, longLen)
plot(shortMA, color = #9e2f24)
plot(longMA, color = #228227)
inDateRange = (time >= startDate) and (time < endDate)
if (ta.crossover(shortMA, longMA) and inDateRange)
    strategy.entry("long", strategy.long)
// if (ta.crossunder(shortMA, longMA) and inDateRange)
--- page 203 ---

// strategy.entry("short", strategy.short)
if (strategy.position_size > 0 and ta.crossunder(shortMA, longMA))
    strategy.exit(id="exit long", stop=close)
isCross = ta.cross(shortMA, longMA)
plot(isCross ? shortMA : na, color=#144ce7, style = plot.style_cross, linewidth = 6)
Compile it and... oh my god! It brings you a 374,353.5% net profit!!!!!! You must sell your apartment and bet
everything on these lines of code!
Here’s what it looks like visually:
Figure 8.10 – Are you really betting your house on this?
(And, of course, we ignore Max Drawdown, which shows how amateur our thinking is. We want followers, after all.)
I’ll leave you to understand for yourself what happened here and why this result was displayed. It’s your time to shine
now.
Note that you can also find the code in the PrivateMACrossStrategy.psl file at the GitHub link.
What I’m trying to say in this example is never trust results that somebody else shows you. Understand what they are
trying to do and try to recreate their strategies. Notice how they “forget” to test in specific market conditions or how
they “overlook” situations where the strategy drawdown would create enough loss for you to have to recover for
years before you got profitable. Remember the example in which I just added one option to a function and disguised a
strategy as being profitable?
You’ll need to do the work here, and this is what the work looks like:
--- page 204 ---

Figure 8.11 – “The w ork”
Caveats when coding Pine Script strategies
Here’s a list of issues and things to take into account when you use the Pine Script/Strategy Tester combination:
Conditions are calculated at bar close (so you will have situations when entries and exits would be triggered in real life but they wouldn’t be in the
script). This can be circumvented by forward-testing with calc_on_every_tick.
The lack of intrabar calculations (did the price go from Open to High or to Low first?).
The preceding situations lead to repainting (situations where the indicator showed a specific entry point and, after a while, it displayed another
entry point instead). It “looked into the future.”
Testing with other types of candles.
Peeking into the future: https://www.tradingview.com/support/solutions/43000614705-strategy-produces-unrealistically-good-results-by-peekinginto-the-future/.
Linking the strategy to a 3Commas bot
A nice feature that 3Commas offers us is the ability to connect to your TradingView indicator.
Here’s an article that provides step-by-step instructions on how to connect the Hash Ribbons indicator to 3Commas –
https://3commas.io/blog/using-the-hash-ribbon-to-start-bot-deals – and its knowledge base article that explains the
process in detail: https://help.3commas.io/en/articles/3108938-how-to-use-tradingview-custom-signals.
What this means is that once we figure out a profitable indicator, we can code it using Pine Script, add alerts to it that
trigger 3Commas signals, and we’ve just created an automated trading bot.
Some of my clients had strategies that they had been trading manually for years before I gave them this idea. You
know the kind, the old-school traders that had an edge figured out and then they stuck with it. Well... automating that
edge has now become simple to do, so why not have a bot trade for you while you sleep?
Now, let’s venture into the next phase of our journey – coding your strategy in Freqtrade, a toolkit that provides you
with an arsenal to fully backtest, automate, and deploy your trading strategy.
--- page 205 ---

Coding a strategy in Freqtrade
Having written numerous strategies for TradingView, I noticed a degree of dissatisfaction among some of my clients.
Their meticulously crafted strategies, once thought to be effective, fell short of expectations. While these strategies did
generate the anticipated entry and exit points, they invariably led to financial losses when tested over more substantial
periods and sample sizes.
They were losing due to statistics.
For instance, a strategy might show promising profitability, but if it’s accompanied by substantial drawdowns, its
practical implementation becomes exceedingly risky. Consider a scenario in which the strategy suffers a 25% loss in
the first month, reducing the capital from $10,000 to $7,500. In such a situation, it would need a 34% return just to
break even.
There are other issues such as days in drawdown or weeks with no trades, which can affect your psyche if you’re
live-trading.
Of course, every problem has a solution. For instance, if you’re using a trend trading algorithm, you can complement it
with a mean reversion strategy that exhibits a negative correlation to your initial trend trading approach. Alternatively,
you could sacrifice returns in order to reduce risk, or slowly close positions during drawdown. However, you might also
be overfitting. Overfitting means creating a trading strategy that performs very well on past data but fails to predict
future market performance due to its specificity to the historical dataset. Basically, you are tuning your strategy so that
your past results are good.
I personally keep the drawdown less than 20% during backtesting, which gives me a less than 30% drawdown during
live trades, but that is not a rule. There are other high-risk, high-reward strategies that have a bigger drawdown.
In order to understand all of this, I recommend you delve deeper into the world of statistics and finance fundamentals.
I have put some links in the Further reading section, that you might find helpful.
I could delve deeply into statistics, but I want this book to be concise and straightforward. Therefore, I’ll focus on
Freqtrade, an outstanding tool I’m highlighting here. Freqtrade not only allows you to develop and test trading
strategies but also facilitates in-depth analysis of the results. Moreover, it can automatically execute your strategies,
making it a complete environment for algorithmic trading.
Freqtrade intro
Freqtrade is a robust, open source trading bot specifically designed for cryptocurrency trading. It’s built using Python
and comes bundled with everything you need to craft a strategy from pandas and Jupyter Notebook to the libraries
required for backtesting, plotting entries, and interfacing with multiple crypto exchanges. Additionally, it offers
advanced features such as AI automation, parameter optimization, and various other modules.
Take note, Freqtrade is not a subscription-based service selling a “profitable” trading bot. I’ve extensively tested such
bots and, in my experience, their profitability is overhyped or context-dependent. In contrast, Freqtrade is a toolkit that
empowers traders with all the tools necessary to vet and deploy automated strategies for successfully trading crypto.
--- page 206 ---

Its official website, https://www.freqtrade.io, is rich with detailed information, as shown in the following screenshot. I
strongly recommend perusing it once before delving into this section. You may not grasp everything at first glance, but
revisiting relevant sections while reading this book will help you connect the dots.
Figure 8.12 – The Freqtrade w ebsite
If you find coding uncomfortable, feel free to skim through this chapter and revisit it when you’re ready to bring your
profitable strategies to life.
Directions for installation and configuration
Since the software is frequently updated, relying on its up-to-date online resources ensures you’re following the most
current installation process. Visit its GitHub page (https://github.com/freqtrade/freqtrade) for the latest release and
installation instructions and also use its Discord server (https://www.freqtrade.io/en/stable/#help-discord) if you need
assistance or have specific queries.
I strongly suggest setting up Freqtrade with Docker (https://www.docker.com/) on a remote virtual machine, which is
capable of running the bots continuously, 24/7. Many of my coaching clients have successfully utilized servers from
Amazon AWS (https://aws.amazon.com/), Oracle (https://www.oracle.com/), and Contabo (http://contabo.com).
--- page 207 ---

The 10 basic steps to get a Freqtrade instance running are as follows:
1. Get a remote server or virtual machine (optional).
2. Install Docker.
3. Download the latest stable Freqtrade version.
4. Configure Freqtrade.
5. Run it inside Docker.
6. Connect to the user interface.
7. Download data for the pairs and timeframes that you’ll be trading.
8. Create a strategy.
9. Backtest, plot results, update strategy, backtest, plot, optimize, backtest, and so on.
10. Run a live instance connected to Telegram to get notifications.
Here is an article detailing a quick-start installation via Docker: https://www.freqtrade.io/en/stable/docker_quickstart/.
A few quirks that need your attention (and that might be resolved by the time you’re reading this book) are these:
Read the docs on downloading data and download data for trading pairs in advance so that you can backtest your strategies quickly.
Hyperopt takes a lot of processing power; once you’re profitable, you might want to have a virtual machine with multiple cores that will
continuously run Hyperopt on your strategies and that you don’t use for anything else.
Always search GitHub and Discord for issues you encounter; most of them already have an answer there.
The indicators used are not always 100% correlated with TradingView’s indicators. Small differences in the algorithm might produce totally
different results, so I recommend you plot via Freqtrade if you trade via it.
Mastering this tool requires time and patience, so take it slow and do not rush through the process.
Creating your own strategy
You can find the strategies inside the Freqtrade directory, in user_data/strategies, with SampleStrategy
(sample_strategy.py) provided as an example.
--- page 208 ---
--- page 209 ---

Figure 8.13 – SampleStrategy
Here is also a list of strategies already coded for Freqtrade that you can take a look at and modify at your
convenience: https://github.com/freqtrade/freqtrade-strategies/tree/main/user_data/strategies. Remember the code that
gave us 374,353.5% net profit in Trading View? It functioned by purchasing at a moving average crossover and selling
when a crossover occurred in the reverse direction. It looked like this:

//@version=5
strategy("Private MA Cross", default_qty_value=100000)
shortLen = 9
longLen = 21
startDate = timestamp("27 Mar 2020 00:00")
endDate = timestamp("27 Mar 2021 23:59")
shortMA = ta.sma(close, shortLen)
longMA = ta.sma(close, longLen)
plot(shortMA, color = #9e2f24)
plot(longMA, color = #228227)
inDateRange = (time >= startDate) and (time < endDate)
if (ta.crossover(shortMA, longMA) and inDateRange)
    strategy.entry("long", strategy.long)
// if (ta.crossunder(shortMA, longMA) and inDateRange)
    // strategy.entry("short", strategy.short)
if (strategy.position_size > 0 and ta.crossunder(shortMA, longMA))
    strategy.exit(id="exit long", stop=close)
isCross = ta.cross(shortMA, longMA)
plot(isCross ? shortMA : na, color=#144ce7, style = plot.style_cross, linewidth = 6)
I’m going to transition this into Freqtrade. Bear in mind that there will be some variances, but my intention is to show
how it looks in Python and how the backtesting results appear. At this point in the chapter, I don’t expect you to grasp
every single detail (unlike in the earlier chapters). Rather, my aim here is for you to follow along, gaining an
understanding of the general concept and the direction we’re heading in.
The following is the Python code for Freqtrade. It’s pretty big, so I broke it down into sections:

# --- Do not remove these libs ---
import numpy as np  # noqa
import pandas as pd  # noqa
from pandas import DataFrame
from freqtrade.strategy import (BooleanParameter, CategoricalParameter, DecimalParameter,
                                IStrategy, IntParameter)
# --------------------------------
# Add your lib to import here
import talib.abstract as ta
import freqtrade.vendor.qtpylib.indicators as qtpylib
from functools import reduce
We can leave the initial imports as they are:

class PrivateMACross(IStrategy):
    INTERFACE_VERSION = 3
We’re using the latest version of the Freqtrade interface, v3. We will use the class name, PrivateMACross, to call the
strategy from the command line:

    timeframe = '1d'
    ma_short = 9
    ma_long = 21
    startup_candle_count: int = ma_long
    can_short: bool = False
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
