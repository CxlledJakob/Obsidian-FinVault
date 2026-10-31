# Zero to Hero in Cryptocurrency Trading.pdf — pages 153–172

--- page 153 ---

Figure 5.16 – Connecting to Binance
SmartTrade
The SmartTrade terminal is the main reason I use 3Commas:
--- page 154 ---

Figure 5.17 – SmartTrade section
It consists of four sections:
TradingView is a direct connection to TradingView, allowing you to use the charting tools while in 3Commas without paying for a subscription
there. On its right, you can also see its bid-ask spread.
Signals are buy and sell signals 3Commas offers for various trading pairs. I don’t use this at all. It basically lets somebody else (usually an
algorithm) suggest trades, which 3Commas can take.
Trade terminal, or the smart trading terminal, is a terminal for issuing advanced orders to your connected exchanges, orders they might not
even have in their own terminals. Don’t confuse this with the Terminal section on the left of the page.
Orders and positions shows your open positions and what you can do with them (edit, close, add funds, etc.).
Here’s a picture of the Trade Terminal (the tools at the bottom of the previous figure):
--- page 155 ---

Figure 5.18 – SmartTrade view
The Trade terminal section has the following SmartTrade tools:
Buy/Sell, which is used to quickly buy and sell at Limit or Market. The Terminal section on the left has the same tools.
Smart Trade can be used to buy at Limit, Market, or Cond. (Stop Limit or Stop Market). You can also use the Trailing buy option there
(which is the trailing stop mentioned at the beginning of the chapter, in Types of orders). It also has a Take Profit section with a limit order or
market order that supports split targets (you take profit multiple times), including a trailing take profit (similar to the trailing stop). And, did I
say that it also has a Stop Loss section, which uses a conditional limit or market order with Stop Loss timeout (in case there’s a sudden spike or
liquidity grab, which is quickly corrected), Trailing Stop Loss, and... wait for it... Move to Breakeven (which will move the stop loss to break
even after you hit your first profit target) options? You can do all of this manually, but 3Commas (3C) will allow you to automate everything
under one roof.
Smart Sell is used to get rid of tokens you already own. It uses most of the tools that Smart Trade uses to do that. Note that there are links to
more information under each section giving you details and ways to use each tool.
Smart Cover is useful when you want to sell your tokens now and buy them again at a better price. It can be used as a classical short tool, where
you want to make a profit from a downtrend, or it can be used to repurchase tokens after you got a successful long and you’re waiting for a quick
drop in price before bouncing up again.
Smart Buy is the opposite of Smart Sell and it’s generally used when you have open short positions in Futures. You basically use Smart Buy
to take control of the open shorts (that you’ve created either outside of 3C or using bots inside 3C).
From here, we’ll use Smart Trade for longing and Smart Cover for shorting.
--- page 156 ---

You see that our terminology suddenly changed. Stop Limit orders became Conditional Limit orders, Trailing Stop
became Trailing buy…. Well, this happens when you hop from exchange to exchange, each having its own slightly
changed naming conventions and interface. Where 3C shines is in the way it unifies all the exchanges you’re trading
on under one roof that has the same set of (advanced) features.
Paper trading/demo account
After creating your 3C account, you’ll see Paper Trading balance in the top section.
Figure 5.19 – Top view
Clicking on it will switch to an environment that you can use to test your trading skills. You’ll be able to trade here
safely, without using real money, so that you can hone your skills until you become profitable.
Your first (demo) trade
Let’s say I see this situation: BTC/USDT at 26766.66 in a downtrend.
Figure 5.20 – TradingView on 3Commas
--- page 157 ---

I want to short the market BTC/USDT so I go to Smart Cover | Units and use $2,482 to short, at the market price
(currently 26759). I also enable Take Profit and Stop Loss:
Figure 5.21 – Smart Cover
Now I have three lines (or four if I’ve enabled an additional take profit) on my graph, which I can move manually or
edit using the fields from the previous figure:
--- page 158 ---

Figure 5.22 – Four new lines
I then create the trade:
Figure 5.23 – Trade confirmation
Now I’m monitoring the trade. I love the Status section and the Profit/Loss section from which I can quickly find out
how my trades behave:
--- page 159 ---

Figure 5.24 – Monitoring the trade
If I want to add more funds, reduce funds, close at market price, share the trade with someone, or edit the trade
(modifying the take profit and stop loss conditions), I can do that in the right menu:
Figure 5.25 – Active trades – right menu
Here’s how it looks after a while:
--- page 160 ---

Figure 5.26 – Monitoring the trade again
And this is the final figure, with the trade results:
Figure 5.27 – The trade ended
The following exercises are designed to deepen your understanding of trading on 3C. It’s crucial that you engage with
them prior to beginning your trading journey.
Activities
1. In 3Commas, connect to your preferred exchange. You can use this tutorial for the process: https://help.3commas.io/en/articles/3109051-
binance-how-to-create-api-keys-fast-connect-also-explained?_ga=2.68036947.330265515.1672729298-379498444.1672729298.
2. Next, go to Paper Trading | SmartTrade | Trade terminal and click on the How does X work links for each of the smart trading tools (like in
Figure 5.28).
3. Go to Buy/Sell and create a buy market order (always in Paper Trading). Figure out what type of order was sent by 3Commas to the exchange
when it bought the token.
4. Now create a sell order.
5. Go through each section – Buy/Sell, Smart Trade, Smart Sell, Smart Cover, and Smart Buy – and create a trade on each one. Make sure
that you don’t enable any advanced options at first (such as trailings). Follow those trades until their completion and make sure you understand
what happened there (what order was sent to the exchange when it opened the trade, when it sent the order, what order 3C sent when it closed the
trade, and why it worked the way it worked).
6. Repeat until you are confident you understand how the Smart Trade section works. 3Commas provides you with enough examples to make
everything clear but it takes a while and you need to dedicate time to this.
7. Use the Paper Trading account to play with the tools. Initiate a few trades and see how they behave when the market moves in one direction or
the other. Edit trades, close trades, add funds to them, trade in different markets, and, all in all, learn how to use the 3Commas tools for trading.
--- page 161 ---

The following figure shows the location of the link to the 3Commas knowledge base:
Figure 5.28 – How does X w ork?
IMPORTANT
When creating the API in the exchange (e.g., Binance), don’t enable withdrawals. Give only the minimum access that 3Commas needs to do
its job.
Summary
This chapter went into depth regarding the various trading tools that you have at your disposal on the CEX.
My goal was for you to understand the types of orders you can issue on an exchange, how they behave there, and
what actually happens when they get executed. Basically, you got to know the tools you’ll be using in the later
chapters.
I left you with a lot of activities to do, but (I hope) you haven’t started trading just yet. That’s because in the next
chapter, we’ll cover risk management, which is a must-read before any money is involved.
--- page 162 ---

6
Money Management
In this chapter, we will delve into key aspects of effective trading strategy management. This includes understanding
how to limit losses, the importance of position sizing, the benefits of keeping a trading journal, the necessity of a welldefined trading plan, and the decision between trading in dollars or Bitcoin.
The goal of this chapter is to equip you with vital risk management tools that are crucial to any successful trading
journey.
Here are the specific topics we’ll cover:
Limiting losses
Position sizing
Keeping a trading journal
Your trading plan
Dollars or Bitcoin?
Limiting losses
Martingale is a gambling system in which the stakes are doubled after each loss.
--- page 163 ---

Figure 6.1 – Playing roulette
If you play roulette, bet $10 on red, and you get red, congrats, you’ve won $10. If you get black, you lose the initial
$10, then you double down, betting $20 on red. Black is the outcome again; you lose $20, and you bet $40 on red. Red
comes and you’ve won $40 minus the row of losses totaling $30, so you’ve actually won $10.
This might seem a smart system until you calculate the budget you need in order to win the $10 that you’ve bet on red
after getting black 10 consecutive times. That’s $20+$40+$80+$160+$320+$640+$1,280+$2,560+$5,120+$10,240 =
$20,460.
So, would you risk $20,460 to win $10?
What if there are 11 consecutive blacks?
You do the math.
Even though most traders started trading to gain profits, one of the most important aspects of trading and investing is
how to limit your losses.
In trading, even though you can theoretically gain a big amount of money in a short amount of time, you have a certain
amount of capital that you’re starting with and, if you’re not careful with it, you might lose it before you start winning,
as in the following example.
Let’s say you have $10,000 starting capital and you’re using a strategy backtested over a year and also over a bear
market, a sideways market, and a bull market that has a total profit of 13% a year with a win/loss ratio of 53% and a
--- page 164 ---

max drawdown (MDD) of -50%.
This means that you could get 13% a year with this strategy; that’s around $1,300 (assuming you’re all-in with the
strategy) but what happens if the drawdown starts when your strategy runs, bringing you to $5,000 total capital?
You’ve just started with a $5,000 loss. Getting 13% a year would net you around $650, taking you 5 and a half years to
recover your initial capital.
This example shows why we can’t look at a strategy from one angle only.
When a trader shows a strategy that they’ve been testing for the past month, that strategy might still have a big
chance of failing if it wasn’t properly (algorithmically) tested.
There are some key points I’d like to talk about here that will definitely prevent you from losing money but you also
need to use common sense and manage your feelings. Trading is not a get-rich-quick scheme.
Limiting losses strategically
From a strategic perspective, the solution lies in asset diversification. Subsequently, I’ll delve into three crucial
strategies that foster asset diversification: mixing up your investment types, operating across varied markets, and
mitigating overexposure in trades or on centralized exchanges (CEXs). However, if you spread yourself too thin,
you could be taking on more risk for smaller payoffs. So, nailing the sweet spot is pretty important.
Mix your investment types.
Depending on your capital, you can invest in different asset classes such as real estate, stocks, bonds, and crypto or
diversify across countries and industries. Make sure that the securities that you’re diversifying with are not too
correlated or you’ll risk fishing in the same pool of water.
Limiting losses in the trading account
Trade across different markets.
Use https://www.coingecko.com/ | Categories to check the various categories that exist. Categories such as
exchange tokens (such as BNB for Binance), Blockchain tokens (such as AVAX for Avalanche), meme coins (such
as DOGE), NFTs (maybe AXS and SAND), privacy coins, yield farming, decentralized exchanges (DEXs), and
gaming.
Or split by market cap, that is, large caps (think top coins), mid caps, and small caps (think low interest/volume).
There were low-cap coins that handled the 2022 bear market pretty well, but they weren’t traded on CEXs.
Still, the idea here is not to rush it by trading a lot of tokens over various categories. My suggestion for you is to start
trading BTC because most of the market is married to BTC. Once you know how to trade it, you’ll be able to trade
other tokens. Then, follow with ETH and a few other blockchain tokens. They are high-volume, so you’ll be able to
trade them easily. After you do this, start exploring.
Don’t be in trades or on CEXs with the majority of your portfolio.
--- page 165 ---

In 1697, Willem de Vlamingh, together with his crew of Dutch explorers, arrived in Western Australia, becoming the
first Europeans to see black swans with their own eyes. Before that time, all of Europe knew swans as only white and
there was an expression regarding black swans that referred to a thing being impossible. Yet the impossible happened
and Europe discovered black swans.
In trading, a black swan event refers to an event that is almost impossible to happen and yet happens. Imagine
somebody hacking Binance and taking all your money from there. Imagine a CEX becoming illiquid and filing for
bankruptcy.
If you think it’s rare, well, on the 11th of November 2022, FTX’s CEO stepped down from FTX and the company filed
for bankruptcy. A lot of people lost money there, money they were holding on a reputable exchange (found in the top
five in the world). And yes, I also lost part of my portfolio from that event, though luckily, most of it is on the chain, out
of any CEX’s reach.
This is what you (and I) can learn from this:
Don’t put all of your money on one particular exchange. Distribute money across different exchanges or, better yet, hold it in your on-chain
wallet and only send it to the exchange when you are trading. What this means is that in the case of a black swan event like the FTX collapse of
2022, you’d only lose the money you have on FTX, not your whole trading account.
I would recommend the “heat” on your total portfolio stays between 15% and 30%. That means that in the case of a sudden market crash, you’re
risking at most 30% of your account (in case everything goes bad and your trades don’t find liquidity to exit with a stop-loss order).
Limiting losses in trading
Next, I’ll discuss two strategies for limiting losses in trading: implementing position sizing when placing trades and
controlling your emotions effectively.
Use position sizing when deploying trades.
In traditional trading, one rule of thumb is to risk at most 2% of equity in any particular trade and a maximum of 6% of
your portfolio over a month.
For a 10K portfolio, that would be a $200 risk per trade with a total risk of $600/month. However, once your portfolio
increases (even during the same month), you can risk more, proportionately to the increase.
This can be achieved through Fixed Fractional Position Sizing, which we’ll discuss in the Position sizing section.
Handle your emotions.
This is one of the most important aspects of trading. If you can’t handle your emotions, in time, you will lose more than
you win.
A lot of people are posting high returns in leverage plays (a 50x leverage with $100 is $5,000). What they don’t do is
show you all the other money they’ve lost until that win and, maybe even more importantly, what they’ll do with their
winnings (lose them in 50x leverage $5,000 trades). Of course, statistically, there are always outliers who will win
despite gambling, but chances are you won’t find yourself there if you gamble.
Before we go any further, let me introduce to you the concept of R.
“R” is a standard unit for evaluating the potential reward and risk of trading strategies and individual trades.
--- page 166 ---

R represents your optimal risk amount. We define this as your “standard position” size in our trading plan.
R-Multiple is our profit or loss on a trade, divided by the amount we planned to risk. For instance, if we risk $500 and
earn $2,000 (2000/500), this is a 4R trade. If we forgo a stop loss and lose $750 when we intended to only risk $500,
that results in a -1.5R trade (750/500).
Calculating a risk/reward ratio for a trade is directly related to your emotions. Traders suggest an R of 1.5 to 2,
meaning a risk/reward ratio of 1.5x to 2x. This means that if you risk losing $200, you also have a chance of winning
$300-$400. This looks good and it feels good, but it actually has no impact on your profits. That’s because you can be
profitable with an R of 0.2 as well, meaning for every $200 you risk losing, the gain can be $40. If your strategy has a
very high win rate, this is perfectly acceptable. But if you’re trading it manually, you can go on a losing streak, lose a
few hundred bucks, and hate the strategy. What the 1.5x - 2x risk helps with is your emotions. Even if your trades
have a win rate of less than 50%, you still have a chance of making a profit.
The following are four activities to help you better understand and improve your ability to diversify and limit losses.
Activities
1. Read about diversification: https://www.investopedia.com/terms/d/diversification.asp .
2. Go to https://www.coingecko.com/ and find what the top 10 coins are by market cap. Go to TradingView and compare their charts on 1D. How
similar are they? Bonus task: find out where and why they diverged.
3. Go to https://coinmarketcap.com/ (an alternative to Coingecko) and repeat the process. On both platforms, you can create a portfolio that can
mirror your investment strategy and keep a balance of your holdings. I wouldn’t use it for trading, but it’s great for investing.
4. Value at Risk (VaR) calculates the potential loss (based on a specified probability) that a group of investments might experience during normal
market conditions over a defined time frame, such as a day. Read more about it here: https://www.investopedia.com/terms/v/var.asp,
https://www.investopedia.com/terms/v/var.asp.
5. Learn more about the R concept and dive into the fractional R trades and terminology such as R-Theoretical and R-Actual at
https://tradethatswing.com/what-r-means-in-trading-in-terms-of-risk-and-profit/.
Position sizing
In trading, we always want to increase returns and reduce risk, so we need to understand how much money to put in
our trades in order to have a good risk/reward balance.
--- page 167 ---

Figure 6.2 – Position sizing
There are various position sizing methods such as YOLO (no method); (addictive) gambling, also called emotion-driven
trading; fixed-size (0.05 BTC for each trade); fixed-value ($1,000 for each trade); a fixed amount of equity; a percent
of equity; percent volatility; the Kelly formula; the max drawdown method; fixed risk/fixed fractional; the profit-risk
method; margin target; leverage target; optimal f; and more.
I’m going to present to you two of those methods. I’ve used both at various times.
Method 1 – percent of equity (variation)
--- page 168 ---

With the percent of equity method, you make sure that the value of your position is equal to your chosen percent of
account equity. I’ve fine-tuned this method to crypto because of the various black swan events that happen here, so
you’ll see modifications from the standard method.
I use the max heat system as I find it applies better to crypto. In traditional trading, your broker is usually insured, and
the companies are a bit more stable, whereas in crypto, the risks are bigger, from the CEX disappearing overnight or
getting hacked to hackers getting access to your account and siphoning money to the dark web.
So, I prefer to know via the max heat method how much I always have in stake, between 15% and 30% of my equity.
That means that if my trades disappear (no liquidity, CEX hacks, or other issues), I would lose a maximum of 15 to
30% of what I have. I’m using this technique because I’m also trading via decentralized platforms, sometimes through
distributed exchanges (DEXs) that have anonymous teams behind them. If you are trading traditionally, on a CEX,
or just starting out, feel free to use my second method, presented next.
Besides max heat, I also use 3 fixed risks: a conservative 2.5% of my equity, a moderate 5%, and an aggressive 10%
risk, which I rarely use.
For a 10k portfolio with a max heat of 15%, that would be $1,500 in-game at any given time. A 2.5% conservative risk
of 10k equals $250, which would allow me 6 max positions ($1,500/$250). If I open 6 conservative trades of $250, I’m
risking 15% of my portfolio, which is the max I want to risk.
Note that using this method, the risk affects the initial sum, not the difference to the stop loss plus fees.
Here’s an example:
Initial deposit: $10,000 Current balance: $10,000
Max heat (%): 15%
Max heat ($): $1,500 Remaining heat ($): $1,500
Fixed risk (%): 2.5% Fixed risk ($): $250
Max positions: 6 Remaining positions: 6
The current balance excludes open trade.
Max heat ($) is calculated as the initial deposit * the max hit (%).
Fixed risk ($) is the current balance / the fixed risk (%).
The remaining positions are calculated as the remaining heat / the fixed risk ($).
I’m entering a trade with $250:
Current balance: $9,750
Remaining heat: $1,250
Fixed risk: $195
Remaining positions: 6
I’m entering another trade with $195:
--- page 169 ---

Current balance: $9,555
Remaining heat: $1,055
Fixed risk: $191.1
Remaining positions: 5
Then, I close the first trade, bringing back $695:
Current portfolio: $10,250
Remaining heat: $1,537.5
Fixed risk: $205
Remaining positions: 7
This is the first method. You can refer to the GitHub link for the spreadsheet.
Method 2 – fixed fractional position sizing (also known as fixed
risk position sizing)
What I love about fixed fractional position sizing is that it directly takes the risk of the trade into account, making it
ideal for futures trading. Note that the first method considers the risk of the whole environment of trading while this
method focuses on the trade risk (and can be used outside of crypto).
In fixed fractional position sizing, you take into account only how much you’d lose if the trade would stop in a loss (you
would sell with a stop loss).
For a 10k portfolio and a 2% (traditional) risk, that would be $200 at risk for the first trade. I recommend you start
with a 1% (conservative) risk and only increase it once you’re confident in your trading skills.
In addition to this, we’re also limiting the risk per month to around 6% of the portfolio, thus recommending you to be in
a maximum of 3 trades of $200 risk at any one time.
A short example: I want to go long on token CAS. It is currently trading at $10 and I’m setting my stop price at $9.
That means I can lose $1 per token bought. My portfolio is $50,000 and my fixed risk is at 1.5% ($750). That means I
can buy 750 CAS tokens (risking $1/CAS with a total of $750). My max loss is $750 or 1.5% of my portfolio value.
Let’s see the algorithm in action now:
Initial deposit: $10,000 Current balance: $10,000
Max heat (%): 6%
Max heat ($): $600 Remaining heat ($): $600
Fixed risk (%): 1.5% Fixed risk ($): $150
Max positions: 4 Remaining positions: 4
The max heat here is calculated using the current balance (not the initial deposit, as in the previous method).
The remaining heat is the max heat minus the risk that we are in trade with (the risk from all open trades).
--- page 170 ---

The fixed risk is a percentage of the current balance.
The max position is calculated by dividing the fixed risk from the remaining heat.
Let’s say token DAB is trading at $230 and I’m shorting it with a stop loss at $240. I’m risking $10/token with a fixed
risk of $150 so I can buy 15 tokens. I’m entering a trade with $3,450 (ignoring taxes):
Current balance: $6,550
Max heat ($): $393
Remaining heat: $243
Fixed risk: $98.25
Remaining positions: 2
I’ll be rounding up to two decimals; it won’t impact the statistics (that much).
There’s a token CAF that is trading at $15 and I’m longing it with a stop at $13. I’m risking $2 and with a fixed risk of
$98.25 I can buy 49.13 pieces. That’s $736.95:
Current balance: $5,813.05
Max heat ($): $348.78
Remaining heat: $100.53 (348.78-150-98.25)
Fixed risk: $87.20
Remaining positions: 1
My first position closes with a profit of $600.95, totaling $4,050.95:
Current balance: $9,864
Max heat ($): $591.84
Remaining heat: $493.59 (591.84-98.25)
Fixed risk: $147.96
Remaining positions: 3
I’m currently using this method because I find it statistically relevant to my performance as a trader. Its only issue is
that you can find yourself with a lot of money in trade and on CEXs and you need to take this into consideration. This
method too can be found in the GitHub repository.
The following activities will help you better understand position sizing. I understand that there’s a bit of mathematics
involved, but this is the kind of mathematics that saves you money. It’s just like doing your taxes, hard at first, but once
you do it you see the value it brings.
Activities
1. Go to http://www.adaptrade.com/MSA/MSA3UsersGuide.pdf | Page 42 to read more about the different position sizing methods listed. Check the
Profit Risk Method as an alternative to fixed fractional position sizing (it’s the same as the initial method when it starts but it risks more when
--- page 171 ---

you’ve gained more).
2. Play with this calculator, which finds out the position size you can take based on your account value, percentage available to risk, entry price, and
initial protective stop: https://chartyourtrade.com/position-size-calculator/. Make sure you understand the process.
Keeping a trading journal
Robert Collier said, “Success is the sum of small efforts, repeated day in and day out.” Lao Tzu said, “The
journey of a thousand miles begins with one step.” Charles Atlas said, “Step by step, and the thing is done.”
Figure 6.3 – Trading journal
They all talk about success in steps, but the thing is, success is also a feeling – when you look back and see what
you’ve built. And once you’ve identified that feeling, it becomes easier and easier to build toward it.
Now, how can you look back if you’re trading without logging all of your trades, studying what you did well and what
you did wrong, and learning from it?
I would argue that a trading journal is a must for any person who calls themselves a trader. You need to have a
historical perspective on each trading method you’ve used, to know how good it is, how it behaved in past markets, and
also your overall performance.
Adjusting to the market
--- page 172 ---

When you look at your past trades, you might notice that one technique that works in bear markets might not work in
bull markets, and note it down. I have specific strategies for bull markets, bear markets, and side markets. For
example, it’s easier in a side market to trade a parallel channel, taking longs at the bottom and shorts at the top.
Some strategies “expire” after the market adapts to them. You might notice how their performance degrades over
time, modify to account for the market, or mark them as obsolete as something new works better.
Different timeframes offer different opportunities, volatility impacts stop-loss orders, and the trade duration might
indicate you should get out before it’s too late.
Handling emotions
Having a trading journal helps you handle your emotions. You might notice how you’re continuously ignoring the
starting point of your strategy, entering either too soon or too late, or maybe with a bigger amount than specified. By
having a clear account of what you did, you’ll be able to better organize your thoughts and handle your emotions while
riding the wave of the market. Profitability will begin to feel earned, not a random section of events, and losses will
have a reason attached, being considered in the bigger picture. You’ll also be able to feel better about what you do and
be able to prove your success to yourself.
Planning your trades
The best traders out there have a clear plan on how they trade. They know when to enter, when to exit, and in what
situations to change that. Most of them don’t follow their trades second by second and have either alarms, multiple
take profit orders, or stop losses to make sure everything is taken care of.
Before they enter the trade, they document everything about the situation they are trading in, including a picture of the
chart, so that when the trade ends, they can compare what they saw in the beginning to what happened in the end.
This, in time, will provide an intuitive feeling of how the market behaves. In my coaching sessions, I sometimes have a
bias toward the direction of the market even on lower timeframes. It’s an intuitive feeling that, even if it lacks clear
proof, it is more right than wrong.
Logging your trades in the trade journal also allows you to paper-trade. You can test a trading strategy without using
any money for a month or two, just by entering the trade in your journal and watching it on the chart as if it were a real
trade.
I’ve provided you with a Trading Journal in the GitHub link.
Next, we’ll explore your trading plan, discussing how to outline conditions for entering and exiting trades, determining
risk, and planning for profit.
Your trading plan
A trading plan means setting conditions for getting into and out of trades, establishing how much money to risk, and
preparing a path with an expectation of profit.
