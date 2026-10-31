# Zero to Hero in Cryptocurrency Trading.pdf — pages 39–58

--- page 39 ---

Figure 2.3 – A candlestick chart
This chart is also called an open-high-low-close (OHLC) chart (because you can see these values for each candle
on the chart). To make it easier, we’re going to use the short forms for Open, High, Low, and Close (O, H, L, and
C).
Here, you can see how the white candles (or green candles) show rising prices (C > O, meaning that the close price is
greater than the open price; basically, it closes “higher”) and the black candles (or red candles) show falling prices (O
> C).
Each candle on this chart represents 1 hour of price movement, and we’ll find out in the next section what exactly
these timeframes are.
Timeframes
We know what a candlestick is and what a candlestick chart looks like, and now it’s time to understand how to
represent price movements over large (or small) periods. Have a look at the graph shown in Figure 2.4:
--- page 40 ---

Figure 2.4 – The Bitcoin Liquid Index (BLX); each candle is 1 month (logarithmic display)
In stocks, you can have gaps between candles because markets can open at different prices than when they’ve
closed, but this doesn’t normally happen in crypto. Here, the market trades 24/7, so when you trade you can expect the
close of one candle to be the price the next candle opens with.
Then, if a candlestick shows the OHLC values, the distance between the opening of one candle and the next opening
is the time length of the candle. Based on how we configure the chart, we can have anywhere from 1-second candles
to 1-month candles (and more).
A 1-hour candle starts at :00 (minute zero) and ends at :59 (minute 59), and these candles are displayed on the hourly
timeframe (also called the 1-hour timeframe or 1H). A 1-day candle starts at 00:00 and ends at 23:59 and is displayed
on the 1D timeframe.
So, 1 candle on 1D equals 24 candles on 1H because there are 24 hours in a day.
Let’s check this out:
--- page 41 ---

Figure 2.5 – A daily candle
The candle in the middle represents the price for BTC on July 7, 2022, in the BTCUSD market on Bitstamp. Its
values are O 20546, H 21847, L 20238, and C 21644 (as explained in the section titled A candlestick story).
Let’s look at this candle in the 4-hour timeframe:
--- page 42 ---

Figure 2.6 – A range of candles on the 4H timeframe
Here, the vertical bars show the start of each day. Starting from July 7, 2022, we have 6 4-hour candles until the next
day. The last candle (black) is at 20:00, signifying the range 20:00-23:59.
The opening of the 1D candle is the O of the first 4H candle, at 20546.
The L of the 1D candle (20238) can be found as the lowest point in the range, at the L of the second black candle.
The 1D H (21847) and 1D C (21644) are both in the last candle of the 4H range.
If we draw a 1D candle over its 4H range, the result looks like this:
--- page 43 ---

Figure 2.7 – The indicator used w as HTF Candles by Prosum Solutions (author prosum_solutions)
Now, it’s time for you to play with TradingView and make sure you understand the different timeframes and how a
higher timeframe (HTF) candle is composed of smaller lower timeframe (LTF) candles. In the next section, we’re
going to talk about identifying the three types of markets that drive the cryptoconomy.
Market participants
All right. We have basic knowledge regarding timeframes now. But how does that help us trade?
Let’s consider the following types of key market participants:
Commercials—insurance funds, pension funds, hedge funds, and institutions: Their main goal is protecting their capital using a
portfolio profile, and for this, they can go where the market goes. The current price doesn’t matter that much (for example, they need to have a
percentage of their portfolio in Bitcoin by the end of the quarter, no matter what happens to BTC). And their entries influence the price of the
cryptocurrency being traded.
Speculators—(manual) traders, algorithmic traders: The price matters; they consider the risk of their entries and trade market anomalies.
Their entries don’t usually influence the price.
High-frequency traders—bots and other automations: They do 90% of the trading, having well-defined entries and exits so that they can
get the highest profit with the least risk. These entries influence the speculators because they both have the same short-term objectives.
--- page 44 ---

The following are the types of traders:
Scalpers: Scalpers trade quickly, based on order flow. Trades can take seconds or minutes.
Day traders: They start and finish the day without an open position, trading based on technical analysis and order flows. They don’t care about
the fundamentals of the cryptocurrencies they trade because they exit quickly. The trades take minutes or hours.
Short-term traders: These traders use technical analysis, followed by some fundamental analysis, and their trades last for 3 to 5 days (for
instance, they trade breakouts).
Intermediate traders/swing traders: They use a combination of fundamental analysis and technical analysis to trade. Their trades take days,
weeks, or even months.
(Big) Long-term investors: They use fundamental analysis, and usually, filling their orders takes time (days even). Their moves influence the
market, and they start and stop trends with their entries and exits. They stay in trades for years.
In order to simplify the mentality we should have when trading, let’s imagine we have a smart opponent that we’re
trading against. When we win, they lose; when we lose, they win. They can wear different hats at different times—
sometimes the hat of a commercial; another time the hat of a day trader.
The question we should always be asking ourselves is this: Which of the hats are they wearing in the current
market conditions? Now, I’m going to give a few examples, but if you’re new to trading, feel free to skip them now
and come back later, after reading the book.
Here are some examples of situations, but remember that any interpretation is relative to the truth:
If we see a big upper wick on a 1-second timeframe on a specific exchange (and not on other exchanges), we can consider this to be a big onetime exit that reflects the needs of a commercial and doesn’t necessarily reflect a trend in the market. Basically, someone sold a lot of currency
there, and then the market participants corrected that move by buying the orders back. But if we see multiple wicks, we can presume someone is
continuously selling at that price a very large order by splitting it into small orders. There, we can expect more selling pressure than when a single
wick forms. Here’s an example:
--- page 45 ---

Figure 2.8 – Big upper w ick
If a cryptocurrency continuously trades in a price range, moving to the top, falling back, rinse, and repeat, that might be a situation where
automatic algorithms are feeding themselves in a loop. If we spot these in time, we can enter longs (long trades) when the price is low, sell at the
top of the range, and enter shorts (going short or shorting) until the price comes back down. Here is an example (but a low volume one) with an
8% increase and decrease in price, with each candle being 1 hour. Just imagine trading that:
--- page 46 ---

Figure 2.9 – Steady price range
Key news announcements in crypto create market volatility. A lot of speculators are trading at that point to profit from the volatility,
specifically commercials that want to execute big orders. They are trying to find the liquidity that they need to sell their orders to:
--- page 47 ---
--- page 48 ---

Figure 2.10 – Fed press conference impact
All of these moves are influencing the trend, making the markets go up, down, or sideways. Let’s see how that looks in
the next section.
Types of markets
Markets can go up or down or they can stay in a range. We call these markets a bull market, a bear market, and a
sideways (or ranging) market.
Here’s what they look like:
Figure 2.11 – A bull market
A bull market represents a period (months or years) when the price of an asset appreciates over its historical value.
If the period is smaller than a few months, it is named a bullish trend.
A bull market is characterized by the following:
Positive news (called bullish news)
A lot of big investments
--- page 49 ---

Money is thrown around (even in mediocre businesses)
You can’t usually identify the start of a bull market until you’re already in it.
Most people start trading during bull markets because that is the time when everybody is bombarded by optimistic
news and the economy is strong enough that everybody has some money left to invest. But the problem is that
latecomers are joining in right at the peak (or end) of the bull market.
And then, the bear market comes. Here’s how it looks:
Figure 2.12 – A bear market
A bear market represents a period (usually years) when the price of an asset depreciates over its historical value.
And, if the period is shorter, we can call it a bearish trend.
A bear market is characterized by the following:
Negative news (called bearish news)
Few investments
No money in the market or long periods without any big activity
After starting, newcomers are usually faced with a bear market where all the techniques that they’ve used to make
money suddenly stop working. This is the point where they usually lose money and, after a while, leave the market.
--- page 50 ---

When the new bull market comes, you will hear from them it’s all a lie, you’re gonna lose money, and other such
things.
A sideways market, also called a lateral market or a ranging market, is a period when the price stays within a
certain range. If the period is lower than a few months, we can call it a sideways trend. Here’s a sideways market
on the chart:
Figure 2.13 – A sidew ays market
People don’t usually talk about sideways markets, and that is mostly because there is either no particular activity there
or because the news is polarized, creating uncertainty. You can also see sideways trends during long bear markets
where a lot of market participants have left the field.
But why do we call them bull markets and bear markets? Imagine how these animals attack their opponents. The bull
thrusts its horns up, throwing its opponent in the air, while the bear swipes its paws down, pushing its opponent to the
ground. Here’s a depiction of this:
--- page 51 ---

Figure 2.14 – Bulls versus bears
If there’s an uptrend, we say that the bulls are in control, and when the prices are falling (there’s a downtrend), we say
that the bears have taken control.
There are tips and tricks to trade each market, but for now, let’s focus on learning how to identify them. At the end of
the chapter, there will be some exercises to help you do this.
Summary
In this chapter, I helped you identify your risk level and taught you about other market participants and how they
behave in the market. We also discussed a bit about cryptocurrencies and timeframes and started reading a chart.
My goal was for you to get to know your risk level and to find out more about the entities that trade alongside you.
In the next chapter, we’re going deep—right into technical analysis, talking about TradingView, candle patterns,
moving averages (MAs), the Relative Strength Index (RSI), and much, much more.
Exercises
1. After taking the risk assessment questionnaire, ask yourself (and write down) three things you’re doing to keep your emotions in check in real
life. I know a couple that say that when they want to fight, they speak in pirate English. Think: “Ye be mighty pushy! Belay that!” ... or just use
The Pirate Translator here: https://pirate.monkeyness.com/translate.
2. Identify 3 daily candles in TradingView, then go to the 4-hour and 1-hour timeframe and look at the candles that formed them. See how the low
of the bigger candle was formed using the low of the lowest candle in the group, how the high was formed, and so on. How does the price move
inside that big candle? Is it going directly to the close? Is it pushing toward the high, then dropping to the low, then jumping to the close?
3. Identify a big news event in crypto (which happened at a specific hour, on a specific day). Tip: You can look for big Fed announcements or a black
swan event (such as the crash of FTX). Check on the chart how the price reacted to the news and for how long. Imagine the market participants
--- page 52 ---

getting fueled by the news and trading during those times. Which market participants were involved? What was their thought process?
4. Go to TradingView and open the daily chart for BTCUSD. First, try to identify the periods I’ve shown you in the screenshots about the bear
market and the bull market, and then, go to a lower timeframe (4 hours or 1 hour) and identify 2 bullish trends, 2 bearish trends, and 2 sideways
trends.
--- page 53 ---

3
Technical Analysis – Candles and Patterns
In this chapter, you’ll lay the foundation for your career in trading. We’ll begin by introducing you to one of the most
effective charting tools available: TradingView. With this tool, you’ll be able to see on your screen what I like to call
the “story of the price.” Next, we’ll delve into candlestick patterns, which will help you understand the emotions
driving small price movements. After that, we’ll cover chart patterns for stronger and longer-lasting movements.
Finally, we’ll explore support and resistance areas and the laws that govern them. All of this will provide you with a
solid understanding of the fundamentals you need to succeed in your training career.
My goal for this chapter is for you to understand how to view the story and the emotions battling behind a price
movement.
Here are the topics that we’ll be covering:
TradingView
Market patterns
Candlestick patterns
Chart patterns
Supply and demand
Support and resistance
Let’s begin!
TradingView
“Check what the price is telling you” is something I so often tell my students. The price always has a story to tell—
a story of enthusiasm, one of disappointment, or one of indecision. That story is written in the chart, and it’s called
price action.
Wikipedia tells us, “At its most simplistic, it attempts to describe the human thought processes invoked by
experienced, non-disciplinary traders as they observe and trade their markets. Price action is simply how
prices change - the action of price. It is most noticeable in markets with high liquidity and price volatility, but
anything that is traded freely (in price) in a market will per se demonstrate price action.”
(https://en.wikipedia.org/wiki/Price_action_trading)
However, before we can fully understand the story, we need to learn the alphabet and how to read it from its canvas,
TradingView.
TradingView defines itself as follows: “Where the world charts, chats, and trades markets. We’re a supercharged
super-charting platform and social network for traders and investors.”
In essence, it’s a tool used for tracking prices that also has a social network feature. This allows you to follow other
traders to learn about their ideas, strategies, and indicators.
--- page 54 ---

Here’s how it looks at first glance:
Figure 3.1 – TradingView at a glance
You probably know the saying “A picture is worth a thousand words.” Well, let’s put it into practice. In this section,
I’m going to show you the basics of TradingView and, later in the book, you’ll learn how to use it to chart price action
and develop trading strategies with it.
In the upper-left section of the chart (Figure 3.2), you have the current market, Bitcoin / U.S. Dollar, the current
time frame, D (meaning daily), the exchange, BINANCE, and information regarding the current candle pinpointed by
the mouse cursor, its Open, High, Low, Close (OHLC) data:
Figure 3.2 – Upper-left section
As you can see in Figure 3.3, right under the chart, we have the time scale, which now shows dates from 2023 to
April 16. If we zoom out, it will also show the months, and if we zoom in, the hours or seconds:
--- page 55 ---

Figure 3.3 – Low er-right section
If we right-click on the time scale, we can change the time zone. My recommendation is to set it to UTC as most
traders are using that, so you will instantly see the correct time on your chart when watching a video on the internet.
Also, when explaining a trade to someone, you need to make sure they are using UTC too, or you’ll have different
hours at which the trade occurred.
In the same screenshot, on the right of the chart, we can see the price scale now ranging from 14,540 to 26,000. The
box at 30,099.74 shows the current price. The number under the 30,099.74 box shows how much time is left until the
current candle ends: 19 hours, 7 minutes, and 33 seconds.
--- page 56 ---

If you right-click on the price scale, you have the option to set it to Auto (to fit the current data on the screen), to
change from price to percentage or logarithmic, to disable some labels or lines, and much more. Try it!
Following that, we have the top-left part of the screen, as seen in the following screenshot:
Figure 3.4 – Top-left section
Here, in the top-left section, you have the menu (represented by your profile image), the symbol search, which is now
set to the Bitcoin / U.S. Dollar trading market (appearing as BTCUSD in the image), followed by the compare or
add symbol (the plus sign), which allows you to add another market over the current one so that you can compare
them.
After that there’s the Time Interval (or time frame) button, currently set to D (each candle represents one day now),
then the Candles button through which you can change the current candle format to Candles, Lines, Bars, Heikin
Ashi, or others.
After that, the Indicators, Metrics & Strategies symbol is the place from which you can add indicators, metrics, or
strategies to your chart.
The Indicators Templates symbol (four squares) allows you to save a combination of indicators on a symbol at a
specific interval so that you can change your view of the chart (and current strategy) at the click of a button. The B
and D symbols to its right are two of the templates I’ve created.
The Create Alert button allows you to add alerts that will trigger once certain conditions are met (the price reaches a
certain point, the indicator gives a signal, a value is in a certain range, and so on). Alerts can pop up on the phone app
or in a browser notification; they can be sent via email, or they can be connected via API to various services.
Bar Replay shows you how a chart looked at a certain point in time, simulating how the market (and the indicators)
behaved in the past. It’s a great tool for backtesting a strategy but it also has its flaws, which we will be talking about
in a later chapter on backtesting.
The left and right arrows allow you to undo and redo certain actions that you’ve made on a chart (such as drawing a
line).
The following screenshot shows the top-right section:
Figure 3.5 – Top-right section
It starts with the Select Layout icon (the square), which allows you to load different window positions (you can have
four charts up at the same time or one chart on different time frames). Programming is the name of my current
layout (I also have a Trading layout and a BTC High Timeframe Analysis layout).
When you click on the layout’s name, it saves it, or if you push the down arrow next to it, you’ll have some options
such as Save, Autosave, Rename, Make a copy, Load layout, Share layout, or Export data.
--- page 57 ---

The quick search tool is shown as a magnifying glass, and it allows you to search for drawings, functions, and settings.
I use it to quickly find a setting to turn on/off.
After that, we have the chart settings icon (the gear), which allows you to configure how a chart looks and behaves in
various situations. Here you can change the timezone or remove information that you don’t use, such as Open
market status (used in stocks) or maybe Bid and ask price, and you can also save the settings as a template to use
later.
Then, we have the fullscreen mode button (the interrupted square), followed by the take a snapshot button (the
camera icon), which allows you to copy, share, download, or tweet the current chart image.
There’s also a Publish button on the right of the camera from where you can publish an idea you might have (your
chart and a description under it) or record a video of that idea.
Let’s look at the left menu bar now. It shows quite a lot of icons; most of them are used to interact with charts
(drawing, measuring, zooming):
--- page 58 ---
