# Quantitative Trading_ How to Build Your Own Algorithmic -- Ernest P_ Chan -- Wiley Trading, 1, 2008 -- John Wiley & Sons, Ltd_ -- isbn13 9780470284889 -- e4d660df1c1a75e8676a28ff4f852fa7 -- Anna’s Archive.pdf — Chapter 2: Fishing for Ideas Where Can We Find (pages 31–50)

--- page 31 ---

C H A P T E R 2
Fishing for Ideas
Where Can We Find
Good Strategies?
T
his is the surprise: Finding a trading idea is actually not the
hardest part of building a quantitative trading business. There
are hundreds, if not thousands, of trading ideas that are in
the public sphere at any time, accessible to anyone at little or no
cost. Many authors of these trading ideas will tell you their complete methodologies in addition to their backtest results. There are
ﬁnance and investment books, newspapers and magazines, mainstream media web sites, academic papers available online or in the
nearest public library, trader forums, blogs, and on and on. Some of
the ones I ﬁnd valuable are listed in Table 2.1, but this is just a small
fraction of what is available out there.
In the past, because of my own academic bent, I regularly
perused the various preprints published by business school professors or downloaded the latest online ﬁnance journal articles
to scan for good prospective strategies. In fact, the ﬁrst strategy
I traded when I became independent was based on such academic
research. (It was a version of the PEAD strategy referenced in
Chapter 7.) Increasingly, however, I have found that many strategies described by academics are either too complicated, out of date
(perhaps the once-proﬁtable strategies have already lost their power
due to competition), or require expensive data to backtest (such as
historical fundamental data). Furthermore, many of these academic
9
--- page 32 ---

10
QUANTITATIVE TRADING
TABLE 2.1
Sources of Trading Ideas
Type
URL
Academic
Business schools’ ﬁnance professors’ web
sites
www.hbs.edu/research/research
.html
Social Science Research Network
www.ssrn.com
National Bureau of Economic Research
www.nber.org
Business schools’ quantitative ﬁnance
seminars
www.ieor.columbia.edu/seminars/
ﬁnancialengineering
Mark Hulbert’s column in the New York
Times’ Sunday business section
www.nytimes.com
Buttonwood column in the Economist
magazine’s ﬁnance section
www.economist.com
Financial web sites and blogs
Yahoo! Finance
ﬁnance.yahoo.com
TradingMarkets
www.TradingMarkets.com
Seeking Alpha
www.SeekingAlpha.com
TheStreet.com
www.TheStreet.com
The Kirk Report
www.TheKirkReport.com
Alea Blog
www.aleablog.com
Abnormal Returns
www.AbnormalReturns.com
Brett Steenbarger Trading Psychology
www.brettsteenbarger.com
My own!
epchan.blogspot.com
Trader forums
Elite Trader
www.Elitetrader.com
Wealth-Lab
www.wealth-lab.com
Newspaper and magazines
Stocks, Futures and Options magazine
www.sfomag.com
strategies work only on small-cap stocks, whose illiquidity may render actual trading proﬁts far less impressive than their backtests
would suggest.
This is not to say that you will not ﬁnd some gems if you are
persistent enough, but I have found that many traders’ forums or
blogs may suggest simpler strategies that are equally proﬁtable. You
might be skeptical that people would actually post truly proﬁtable
strategies in the public space for all to see. After all, doesn’t this
disclosure increase the competition and decrease the proﬁtability
of the strategy? And you would be right: Most ready-made strategies
that you may ﬁnd in these places actually do not withstand careful
--- page 33 ---

Fishing for Ideas
11
backtesting. Just like the academic studies, the strategies from
traders’ forums may have worked only for a little while, or they
work for only a certain class of stocks, or they work only if you
don’t factor in transaction costs. However, the trick is that you
can often modify the basic strategy and make it proﬁtable. (Many
of these caveats as well as a few common variations on a basic
strategy will be examined in detail in Chapter 3.)
For example, someone once suggested a strategy to me that was
described in Wealth-Lab (see Table 2.1), where it was claimed that it
had a high Sharpe ratio. When I backtested the strategy, it turned out
not to work as well as advertised. I then tried a few simple modiﬁcations, such as decreasing the holding period and entering and exiting
at different times than suggested, and was able to turn this strategy
into one of my main proﬁt centers. If you are diligent and creative
enough to try the multiple variations of a basic strategy, chances are
you will ﬁnd one of those variations that is highly proﬁtable.
When I left the institutional money management industry to
trade on my own, I worried that I would be cut off from the ﬂow
of trading ideas from my colleagues and mentors. But then I found
out that one of the best ways to gather and share trading ideas is
to start your own trading blog—for every trading “secret” that you
divulge to the world, you will be rewarded with multiple ones from
your readers. (The person who suggested the Wealth-Lab strategy to
me was a reader who works 12 time zones away. If it weren’t for my
blog, there was little chance that I would have met him and bene-
ﬁted from his suggestion.) In fact, what you thought of as secrets
are more often than not well-known ideas to many others! What
truly make a strategy proprietary and its secrets worth protecting
are the tricks and variations that you have come up with, not the
plain vanilla version.
Furthermore, your bad ideas will quickly get shot down by your
online commentators, thus potentially saving you from major losses.
After I glowingly described a seasonal stock-trading strategy on
my blog that was developed by some ﬁnance professors, a reader
promptly went ahead and backtested that strategy and reported that
it didn’t work. (See my blog entry, “Seasonal Trades in Stocks,”
at epchan.blogspot.com/2007/11/seasonal-trades-in-stocks.html and
--- page 34 ---

12
QUANTITATIVE TRADING
the reader’s comment therein. This strategy is described in more detail in Example 7.6.) Of course, I would not have traded this strategy
without backtesting it on my own anyway, and indeed, my subsequent backtest conﬁrmed his ﬁndings. But the fact that my reader
found signiﬁcant ﬂaws with the strategy is important conﬁrmation
that my own backtest is not erroneous.
All in all, I have found that it is actually easier to gather and
exchange trading ideas as an independent trader than when I was
working in the secretive hedge fund world in New York. (When I
worked at Millennium Partners—a multibillion-dollar hedge fund on
Fifth Avenue—one trader ripped a published paper out of the hands
of his programmer, who happened to have picked it up from the
trader’s desk. He was afraid the programmer might learn his “secrets.”) That may be because people are less wary of letting you
know their secrets when they think you won’t be obliterating their
proﬁts by allocating $100 million to that strategy.
No, the difﬁculty is not the lack of ideas. The difﬁculty is to develop a taste for which strategy is suitable for your personal circumstances and goals, and which ones look viable even before you devote the time to diligently backtest them. This taste for prospective
strategies is what I will try to convey in this chapter.
HOW TO IDENTIFY A STRATEGY THAT
SUITS YOU
Whether a strategy is viable often does not have anything to do with
the strategy itself—it has to do with you. Here are some considerations.
Your Working Hours
Do you trade only part time? If so, you would probably want to consider only strategies that hold overnight and not the intraday strategies. Otherwise, you may have to fully automate your strategies (see
Chapter 5 on execution) so that they can run on autopilot most of
the time and alert you only when problems occur.
--- page 35 ---

Fishing for Ideas
13
When I was working full time for others and trading part time
for myself, I traded a simple strategy in my personal account that
required entering or adjusting limit orders on a few exchange-traded
funds (ETFs) once a day, before the market opened. Then, when I
ﬁrst became independent, my level of automation was still relatively
low, so I considered only strategies that require entering orders once
before the market opens and once before the close. Later on, I added
a program that can automatically scan real-time market data and
transmit orders to my brokerage account throughout the trading day
when certain conditions are met. So trading remains a “part-time”
pursuit for me, which is partly why I want to trade quantitatively in
the ﬁrst place.
Your Programming Skills
Are you good at programming? If you know some programming
languages such as Visual Basic or even Java, C#, or C++, you can
explore high-frequency strategies, and you can also trade a large
number of securities. Otherwise, settle for strategies that trade only
once a day, or trade just a few stocks, futures, or currencies. (This
constraint may be overcome if you don’t mind the expense of hiring
a software contractor. Again, see Chapter 5 for more details.)
Your Trading Capital
Do you have a lot of capital for trading as well as expenditure on
infrastructure and operation? In general, I would not recommend
quantitative trading for an account with less than $50,000 capital. Let’s say the dividing line between a highversus low-capital
account is $100,000. Capital availability affects many choices; the
ﬁrst is whether you should open a retail brokerage account or a
proprietary trading account (more on this in Chapter 4 on setting
up your business). For now, I will consider this constraint with
strategy choices in mind.
With a low-capital account, we need to ﬁnd strategies that can
utilize the maximum leverage available. (Of course, getting a higher
leverage is beneﬁcial only if you have a consistently proﬁtable
--- page 36 ---

14
QUANTITATIVE TRADING
strategy.) Trading futures, currencies, and options can offer you
higher leverage than stocks; intraday positions allow a Regulation
T leverage of 4, while interday (overnight) positions allow only a
leverage of 2, requiring double the amount of capital for a portfolio of the same size. Finally, capital (or leverage) availability determines whether you should focus on directional trades (long or
short only) or dollar-neutral trades (hedged or pair trades). A dollarneutral portfolio (meaning the market value of the long positions
equals the market value of the short positions) or market-neutral
portfolio (meaning the beta of the portfolio with respect to a market index is close to zero, where beta measures the ratio between
the expected returns of the portfolio and the expected returns of
the market index) require twice the capital or leverage of a longor
short-only portfolio. So even though a hedged position is less risky
than an unhedged position, the returns generated are correspondingly smaller and may not meet your personal requirements.
Capital availability also imposes a number of indirect constraints. It affects how much you can spend on various infrastructure, data, and software. For example, if you have low trading capital, your online brokerage will not be likely to supply you with realtime market data for too many stocks, so you can’t really have a
strategy that requires real-time market data over a large universe of
stocks. (You can, of course, subscribe to a third-party market data
vendor, but then the extra cost may not be justiﬁable if your trading capital is low.) Similarly, clean historical stock data with high
frequency costs more than historical daily stock data, so a highfrequency stock-trading strategy may not be feasible with small capital expenditure. For historical stock data, there is another quality
that may be even more important than their frequencies: whether
the data are free of survivorship bias. I will deﬁne survivorship bias
in the following section. Here, we just need to know that historical
stock data without survivorship bias are much more expensive than
those that have such a bias. Yet if your data have survivorship bias,
the backtest result can be unreliable.
The same consideration applies to news—whether you can afford a high-coverage, real-time news source such as Bloomberg determines whether a news-driven strategy is a viable one. Same for
--- page 37 ---

Fishing for Ideas
15
fundamental (i.e., companies’ ﬁnancial) data—whether you can afford a good historical database with fundamental data on companies
determines whether you can build a strategy that relies on such data.
Table 2.2 lists how capital (whether for trading or expenditure)
constraint can inﬂuence your many choices.
This table is, of course, not a set of hard-and-fast rules, just some
issues to consider. For example, if you have low capital but opened
an account at a proprietary trading ﬁrm, then you will be free of
many of the considerations above (though not expenditure on infrastructure). I started my life as an independent quantitative trader
with $100,000 at a retail brokerage account (I chose Interactive Brokers), and I traded only directional, intraday stock strategies at ﬁrst.
But when I developed a strategy that sometimes requires much more
leverage in order to be proﬁtable, I signed up as a member of a proprietary trading ﬁrm as well. (Yes, you can have both, or more, accounts simultaneously. In fact, there are good reasons to do so if
only for the sake of comparing their execution speeds and access to
liquidity. See “Choosing a Brokerage or Proprietary Trading Firm”
in Chapter 4.)
Despite my frequent admonitions here and elsewhere to beware
of historical data with survivorship bias, when I ﬁrst started I downloaded only the split-and-dividend-adjusted Yahoo! Finance data
TABLE 2.2
How Capital Availability Aﬀects Your Many Choices
Low Capital
High Capital
Proprietary trading ﬁrm’s membership
Retail brokerage account
Futures, currencies, options
Everything, including stocks
Intraday
Both intraand interday (overnight)
Directional
Directional or market neutral
Small stock universe for intraday
trading
Large stock universe for intraday
trading
Daily historical data with survivorship
bias
High-frequency historical data,
survivorship bias–free
Low-coverage or delayed news source
High-coverage, real-time news source
No historical news database
Survivorship bias–free historical news
database
No historical fundamental data on
stocks
Survivorship bias–free historical
fundamental data on stocks
--- page 38 ---

16
QUANTITATIVE TRADING
using the download program from HQuotes.com (more on the different databases and tools in Chapter 3). This database is not survivorship bias–free—but more than two years later, I am still using
it for most of my backtesting! In fact, a trader I know, who each
day trades more than 10 times my account size, typically uses such
biased data for his backtesting, and yet his strategies are still profitable. How can this be possible? Probably because these are intraday strategies. It seems that the only people I know who are willing
and able to afford survivorship bias–free data are those who work in
money management ﬁrms trading tens of millions of dollars or more
(that includes my former self). So, you see, as long as you are aware
of the limitations of your tools and data, you can cut many corners
and still succeed.
Though futures afford you high leverage, some futures contracts
have such a large size that it would still be impossible for a small account to trade. For instance, though the platinum future contract on
the New York Mercantile Exchange (NYMEX) has a margin requirement of only $8,100, its nominal value is currently about $100,000.
Furthermore, its volatility is such that a 6 percent daily move is
not too rare, which translates to a $6,000 daily proﬁt-and-loss (P&L)
swing in your account due to just this one contract. (Believe me,
I used to have a few of these contracts in my account, and it is a
sickening feeling when they move against you.) In contrast, ES, the
E-mini S&P 500 future on the Chicago Mercantile Exchange (CME,
soon to be merged with NYMEX), has a nominal value of about
$67,500, and a 6 percent or larger daily move happened only twice in
the last 15 years. That’s why its margin requirement is $4,500, only
55 percent that of the platinum contract.
Your Goal
Most people who choose to become traders want to earn a steady
(hopefully increasing) monthly, or at least quarterly, income. But
you may be independently wealthy, and long-term capital gain is all
that matters to you. The strategies to pursue for short-term income
versus long-term capital gain are distinguished mainly by their holding periods. Obviously, if you hold a stock for an average of one
--- page 39 ---

Fishing for Ideas
17
year, you won’t be generating much monthly income (unless you
started trading a while ago and have launched a new subportfolio
every month, which you proceed to hold for a year—that is, you
stagger your portfolios.) More subtly, even if your strategy holds a
stock only for a month on average, your month-to-month proﬁt ﬂuctuation is likely to be fairly large (unless you hold hundreds of different stocks in your portfolio, which can be a result of staggering
your portfolios), and therefore you cannot count on generating income on a monthly basis. This relationship between holding period
(or, conversely, the trading frequency) and consistency of returns
(that is, the Sharpe ratio or, conversely, the drawdown) will be discussed further in the following section. The upshot here is that the
more regularly you want to realize proﬁts and generate income, the
shorter your holding period should be.
There is a misconception aired by some investment advisers,
though, that if your goal is to achieve maximum long-term capital
growth, then the best strategy is a buy-and-hold one. This notion
has been shown to be mathematically false. In reality, maximum
long-term growth is achieved by ﬁnding a strategy with the maximum Sharpe ratio (deﬁned in the next section), provided that you
have access to sufﬁciently high leverage. Therefore, comparing a
short-term strategy with a very short holding period, small annual
return, but very high Sharpe ratio, to a long-term strategy with a
long holding period, high annual return, but lower Sharpe ratio, it is
still preferable to choose the short-term strategy even if your goal is
long-term growth, barring tax considerations and the limitation on
your margin borrowing (more on this surprising fact later in Chapter
6 on money and risk management).
A TASTE FOR PLAUSIBLE STRATEGIES
AND THEIR PITFALLS
Now, let’s suppose that you have read about several potential strategies that ﬁt your personal requirements. Presumably, someone else
has done backtests on these strategies and reported that they have
great historical returns. Before proceeding to devote your time to
--- page 40 ---

18
QUANTITATIVE TRADING
performing a comprehensive backtest on this strategy (not to mention devoting your capital to actually trading this strategy), there
are a number of quick checks you can do to make sure you won’t be
wasting your time or money.
How Does It Compare with a Benchmark and
How Consistent Are Its Returns?
This point seems obvious when the strategy in question is a stocktrading strategy that buys (but not shorts) stocks. Everybody seems
to know that if a long-only strategy returns 10 percent a year, it is
not too fantastic because investing in an index fund will generate as
much, if not better, return on average. However, if the strategy is a
long-short dollar-neutral strategy (i.e., the portfolio holds long and
short positions with equal capital), then 10 percent is quite a good
return, because then the benchmark of comparison is not the market
index, but a riskless asset such as the yield of the three-month U.S.
Treasury bill (which at the time of this writing is about 4 percent).
Another issue to consider is the consistency of the returns generated by a strategy. Though a strategy may have the same average
return as the benchmark, perhaps it delivered positive returns every
month while the benchmark occasionally suffered some very bad
months. In this case, we would still deem the strategy superior. This
leads us to consider the information ratio or Sharpe ratio (Sharpe,
1994), rather than returns, as the proper performance measurement
of a quantitative trading strategy.
Information ratio is the measure to use when you want to assess
a long-only strategy. It is deﬁned as
Information Ratio =
Average of Excess Returns
Standard Deviation of Excess Returns
where
Excess Returns = Portfolio Returns −Benchmark Returns
Now the benchmark is usually the market index to which the
securities you are trading belong. For example, if you trade only
--- page 41 ---

Fishing for Ideas
19
small-cap stocks, the market index should be the Standard & Poor’s
small-cap index or the Russell 2000 index, rather than the S&P 500.
If you are trading just gold futures, then the market index should be
gold spot price, rather than a stock index.
The Sharpe ratio is actually a special case of the information
ratio, suitable when we have a dollar-neutral strategy, so that the
benchmark to use is always the risk-free rate. In practice, most
traders use the Sharpe ratio even when they are trading a directional
(long or short only) strategy, simply because it facilitates comparison across different strategies. Everyone agrees on what the riskfree rate is, but each trader can use a different market index to come
up with their own favorite information ratio, rendering comparison
difﬁcult.
(Actually, there are some subtleties in calculating the Sharpe ratio related to whether and how to subtract the risk-free rate, how to
annualize your Sharpe ratio for ease of comparison, and so on. I will
cover these subtleties in the next chapter, which will also contain
an example on how to compute the Sharpe ratio for a dollar-neutral
and a long-only strategy.)
If the Sharpe ratio is such a nice performance measure across
different strategies, you may wonder why it is not quoted more often instead of returns. In fact, when a colleague and I went to SAC
Capital Advisors (assets under management: $14 billion) to pitch a
strategy, their then head of risk management said to us: “Well, a high
Sharpe ratio is certainly nice, but if you can get a higher return instead, we can all go buy bigger houses with our bonuses!” This reasoning is quite wrong: A higher Sharpe ratio will actually allow you
to make more proﬁts in the end, since it allows you to trade at a
higher leverage. It is the leveraged return that matters in the end,
not the nominal return of a trading strategy. For more on this, see
Chapter 6 on money and risk management.
(And no, our pitching to SAC was not successful, but for reasons quite unrelated to the returns of the strategy. In any case,
at that time neither my colleague nor I were familiar enough with
the mathematical connection between the Sharpe ratio and leveraged returns to make a proper counterargument to that head of risk
management.)
--- page 42 ---

20
QUANTITATIVE TRADING
Now that you know what a Sharpe ratio is, you may want to
ﬁnd out what kind of Sharpe ratio your candidate strategies have.
Often, they are not reported by the authors of that strategy, and you
will have to e-mail them in private for this detail. And often, they
will oblige, especially if the authors are ﬁnance professors; but if
they refuse, you have no choice but to perform the backtest yourself.
Sometimes, however, you can still make an educated guess based on
the ﬂimsiest of information:
r If a strategy trades only a few times a year, chances are its
Sharpe ratio won’t be high. This does not prevent it from being
part of your multistrategy trading business, but it does disqualify
the strategy from being your main proﬁt center.
r If a strategy has deep (e.g., more than 10 percent) or lengthy
(e.g., four or more months) drawdowns, it is unlikely that it will
have a high Sharpe ratio. I will explain the concept of drawdown
in the next section, but you can just visually inspect the equity
curve (which is also the cumulative proﬁt-and-loss curve, assuming no redemption or cash infusion) to see if it is very bumpy
or not. Any peak-to-trough of that curve is a drawdown. (See
Figure 2.1 for an example.)
Maximum
drawdown duration
3x104
2x104
1x104
Maximum
drawdown
2000
2001
2002
2003
Time
Equity in $
A drawdown
FIGURE 2.1
Drawdown, Maximum Drawdown, and Maximum Drawdown
Duration
--- page 43 ---

Fishing for Ideas
21
As a rule of thumb, any strategy that has a Sharpe ratio of less
than 1 is not suitable as a stand-alone strategy. For a strategy that
achieves proﬁtability almost every month, its (annualized) Sharpe
ratio is typically greater than 2. For a strategy that is proﬁtable almost every day, its Sharpe ratio is usually greater than 3. I will show
you how to calculate Sharpe ratios for various strategies in Examples 3.4, 3.6, and 3.7 in the next chapter.
How Deep and Long Is the Drawdown?
A strategy suffers a drawdown whenever it has lost money recently.
A drawdown at a given time t is deﬁned as the difference between
the current equity value (assuming no redemption or cash infusion)
of the portfolio and the global maximum of the equity curve occurring on or before time t. The maximum drawdown is the difference
between the global maximum of the equity curve with the global
minimum of the curve after the occurrence of the global maximum
(time order matters here: The global minimum must occur later
than the global maximum). The global maximum is called the “high
watermark.” The maximum drawdown duration is the longest it
has taken for the equity curve to recover losses.
More often, drawdowns are measured in percentage terms, with
the denominator being the equity at the high watermark, and the numerator being the loss of equity since reaching the high watermark.
Figure 2.1 illustrates a typical drawdown, the maximum drawdown, and the maximum drawdown duration of an equity curve.
I will include a tutorial in Example 3.5 on how to compute these
quantities from a table of daily proﬁts and losses using either Excel
or MATLAB. One thing to keep in mind: The maximum drawdown
and the maximum drawdown duration do not typically overlap over
the same period.
Deﬁned mathematically, drawdown seems abstract and remote.
However, in real life there is nothing more gut-wrenching and
emotionally disturbing to suffer than a drawdown if you’re a trader.
(This is as true for independent traders as for institutional ones.
When an institutional trading group is suffering a drawdown, everybody seems to feel that life has lost meaning and spend their days
--- page 44 ---

22
QUANTITATIVE TRADING
dreading the eventual shutdown of the strategy or maybe even the
group as a whole.) It is therefore something we would want to minimize. You have to ask yourself, realistically, how deep and how long
a drawdown will you be able to tolerate and not liquidate your portfolio and shut down your strategy? Would it be 20 percent and three
months, or 10 percent and one month? Comparing your tolerance
with the numbers obtained from the backtest of a candidate strategy determines whether that strategy is for you.
Even if the author of the strategy you read about did not publish the precise numbers for drawdowns, you should still be able to
make an estimate from a graph of its equity curve. For example, in
Figure 2.1, you can see that the longest drawdown goes from around
February 2001 to around October 2002. So the maximum drawdown
duration is about 20 months. Also, at the beginning of the maximum
drawdown, the equity was about $2.3 × 104, and at the end, about
$0.5 × 104. So the maximum drawdown is about $1.8 × 104.
How Will Transaction Costs Affect the Strategy?
Every time a strategy buys and sells a security, it incurs a transaction cost. The more frequent it trades, the larger the impact of
transaction costs will be on the proﬁtability of the strategy. These
transaction costs are not just due to commission fees charged by
the broker. There will also be the cost of liquidity—when you buy
and sell securities at their market prices, you are paying the bid-ask
spread. If you buy and sell securities using limit orders, however,
you avoid the liquidity costs but incur opportunity costs. This is because your limit orders may not be executed, and therefore you may
miss out on the potential proﬁts of your trade. Also, when you buy
or sell a large chunk of securities, you will not be able to complete
the transaction without impacting the prices at which this transaction is done. (Sometimes just displaying a bid to buy a large number
of shares for a stock can move the prices higher without your having
bought a single share yet!) This effect on the market prices due to
your own order is called market impact, and it can contribute to a
large part of the total transaction cost when the security is not very
liquid.
--- page 45 ---

Fishing for Ideas
23
Finally, there can be a delay between the time your program
transmits an order to your brokerage and the time it is executed
at the exchange, due to delays on the Internet or various softwarerelated issues. This delay can cause a “slippage,” the difference between the price that triggers the order and the execution price. Of
course, this slippage can be of either sign, but on average it will be
a cost rather than a gain to the trader. (If you ﬁnd that it is a gain on
average, you should change your program to deliberately delay the
transmission of the order by a few seconds!)
Transaction costs vary widely for different kinds of securities.
You can typically estimate it by taking half the average bid-ask
spread of a security and then adding the commission if your order size is not much bigger than the average sizes of the best bid
and offer. If you are trading S&P 500 stocks, for example, the average transaction cost (excluding commissions, which depend on your
brokerage) would be about 5 basis points (that is, ﬁve-hundredths of
a percent). Note that I count a round-trip transaction of a buy and
then a sell as two transactions—hence, a round trip will cost 10 basis points in this example. If you are trading ES, the E-mini S&P 500
futures, the transaction cost will be about 1 basis point. Sometimes
the authors whose strategies you read about will disclose that they
have included transaction costs in their backtest performance, but
more often they will not. If they haven’t, then you just to have to
assume that the results are before transactions, and apply your own
judgment to its validity.
As an example of the impact of transaction costs on a strategy,
consider this simple mean-reverting strategy on ES. It is based on
Bollinger bands: that is, every time the price exceeds plus or minus
2 moving standard deviations of its moving average, short or buy, respectively. Exit the position when the price reverts back to within 1
moving standard deviation of the moving average. If you allow yourself to enter and exit every ﬁve minutes, you will ﬁnd that the Sharpe
ratio is about 3 without transaction costs—very excellent indeed!
Unfortunately, the Sharpe ratio is reduced to –3 if we subtract 1 basis point as transaction costs, making it a very unproﬁtable strategy.
For another example of the impact of transaction costs, see
Example 3.7.
--- page 46 ---

24
QUANTITATIVE TRADING
Does the Data Suffer from Survivorship Bias?
A historical database of stock prices that does not include stocks
that have disappeared due to bankruptcies, delistings, mergers, or
acquisitions suffer from the so-called survivorship bias, because
only “survivors” of those often unpleasant events remain in the
database. (The same term can be applied to mutual fund or hedge
fund databases that do not include funds that went out of business.)
Backtesting a strategy using data with survivorship bias can be dangerous because it may inﬂate the historical performance of the strategy. This is especially true if the strategy has a “value” bent; that is,
it tends to buy stocks that are cheap. Some stocks were cheap because the companies were going bankrupt shortly. So if your strategy includes only those cases when the stocks were very cheap
but eventually survived (and maybe prospered) and neglects those
cases where the stocks ﬁnally did get delisted, the backtest performance will, of course, be much better than what a trader would actually have suffered at that time.
So when you read about a “buy on the cheap” strategy that has
great performance, ask the author of that strategy whether it was
tested on survivorship bias–free (sometimes called “point-in-time”)
data. If not, be skeptical of its results. (A toy strategy that illustrates
this can be found in Example 3.3.)
How Did the Performance of the Strategy
Change over the Years?
Most strategies performed much better 10 years ago than now, at
least in a backtest. There weren’t as many hedge funds running
quantitative strategies then. Also, bid-ask spreads were much wider
then: So if you assumed the transaction cost today was applicable
throughout the backtest, the earlier period would have unrealistically high returns.
Survivorship bias in the data might also contribute to the good
performance in the early period. The reason that survivorship bias
mainly inﬂates the performance of an earlier period is that the further back we go in our backtest, the more missing stocks we will
--- page 47 ---

Fishing for Ideas
25
have. Since some of those stocks are missing because they went
out of business, a long-only strategy would have looked better in
the early period of the backtest than what the actual proﬁt and loss
(P&L) would have been at that time. Therefore, when judging the
suitability of a strategy, one must pay particular attention to its performance in the most recent few years, and not be fooled by the
overall performance, which inevitably includes some rosy numbers
back in the old days.
Finally, “regime shifts” in the ﬁnancial markets can mean that
ﬁnancial data from an earlier period simply cannot be ﬁtted to the
same model that is applicable today. Major regime shifts can occur because of changes in securities market regulation (such as
decimalization of stock prices or the elimination of the short-sale
rule, which I allude to in Chapter 5) or other macroeconomic events
(such as the subprime mortgage meltdown).
This point may be hard to swallow for many statistically minded
readers. Many of them may think that the more data there is, the
more statistically robust the backtest should be. This is true only
when the ﬁnancial time series is generated by a stationary process.
Unfortunately, ﬁnancial time series is famously nonstationary, due
to all of the reasons given earlier.
It is possible to incorporate such regime shifts into a sophisticated “super”-model (as I will discuss in Example 7.1), but it is much
simpler if we just demand that our model deliver good performance
on recent data.
Does the Strategy Suffer from
Data-Snooping Bias?
If you build a trading strategy that has 100 parameters, it is very
likely that you can optimize those parameters in such a way that
the historical performance will look fantastic. It is also very likely
that the future performance of this strategy will look nothing like
its historical performance and will turn out to be very poor. By having so many parameters, you are probably ﬁtting the model to historical accidents in the past that will not repeat themselves in the
--- page 48 ---

26
QUANTITATIVE TRADING
future. Actually, this so-called data-snooping bias is very hard to
avoid even if you have just one or two parameters (such as entry and
exit thresholds), and I will leave the discussion on how to minimize
its impact to Chapter 3. But, in general, the more rules the strategy
has, and the more parameters the model has, the more likely it is going to suffer data-snooping bias. Simple models are often the ones
that will stand the test of time. (See the sidebar on my views on
artiﬁcial intelligence and stock picking.)
A R T I F I C I A L
I N T E L L I G E N C E
A N D
S T O C K
P I C K I N G *
There was an article in the New York Times a short while ago about a new hedge
fund launched by Mr. Ray Kurzweil, a pioneer in the ﬁeld of artiﬁcial intelligence.
(Thanks to my fellow blogger, Yaser Anwar, who pointed it out to me.) According
to Kurzweil, the stock-picking decisions in this fund are supposed to be made
by machines that “. . . can observe billions of market transactions to see patterns
we could never see” (quoted in Duhigg, 2006).
While I am certainly a believer in algorithmic trading, I have become a skeptic when it comes to trading based on “artiﬁcial intelligence.”
At the risk of oversimpliﬁcation, we can characterize artiﬁcial intelligence
(AI) as trying to ﬁt past data points into a function with many, many parameters. This is the case for some of the favorite tools of AI: neural networks,
decision trees, and genetic algorithms. With many parameters, we can for sure
capture small patterns that no human can see. But do these patterns persist?
Or are they random noises that will never replay again? Experts in AI assure
us that they have many safeguards against ﬁtting the function to transient
noise. And indeed, such tools have been very eﬀective in consumer marketing and credit card fraud detection. Apparently, the patterns of consumers and
thefts are quite consistent over time, allowing such AI algorithms to work even
with a large number of parameters. However, from my experience, these safeguards work far less well in ﬁnancial markets prediction, and overﬁtting to
the noise in historical data remains a rampant problem. As a matter of fact,
I have built ﬁnancial predictive models based on many of these AI algorithms in
the past. Every time a carefully constructed model that seems to work marvels
in backtest came up, they inevitably performed miserably going forward. The
main reason for this seems to be that the amount of statistically independent
ﬁnancial data is far more limited compared to the billions of independent consumer and credit transactions available. (You may think that there is a lot of tickby-tick ﬁnancial data to mine, but such data is serially correlated and far from
independent.)
--- page 49 ---

Fishing for Ideas
27
This is not to say that no methods based on AI will work in prediction. The
ones that work for me are usually characterized by these properties:
r They are based on a sound econometric or rational basis, and not on random discovery of patterns.
r They have few parameters that need to be ﬁtted to past data.
r They involve linear regression only, and not ﬁtting to some esoteric nonlinear functions.
r They are conceptually simple.
r All optimizations must occur in a lookback moving window, involving no future unseen data. And the eﬀect of this optimization must be continuously
demonstrated using this future, unseen data.
Only when a trading model is constrained in such a manner do I dare to
allow testing on my small, precious amount of historical data. Apparently, Occam’s razor works not only in science, but in ﬁnance as well.
*This section was adapted from my blog article “Artiﬁcial Intelligence and Stock Picking,” which you can ﬁnd at epchan.blogspot.com/2006/12/artiﬁcial-intelligence-andstock.html.
Does the Strategy “Fly under the Radar”
of Institutional Money Managers?
Since this book is about starting a quantitative trading business from
scratch, and not about starting a hedge fund that manages multiple
millions of dollars, we should not be concerned whether a strategy
is one that can absorb multiple millions of dollars. (Capacity is the
technical term for how much a strategy can absorb without negatively impacting its returns.) In fact, quite the opposite—you should
look for those strategies that ﬂy under the radar of most institutional
investors, for example, strategies that have very low capacities because they trade too often, strategies that trade very few stocks every day, or strategies that have very infrequent positions (such as
some seasonal trades in commodity futures described in Chapter 7).
Those niches are the ones that are likely still to be proﬁtable because
they have not yet been completely arbitraged away by the gigantic
hedge funds.
--- page 50 ---

28
QUANTITATIVE TRADING
SUMMARY
Finding prospective quantitative trading strategies is not difﬁcult.
There are:
r Business school and other economic research web sites.
r Financial web sites and blogs focusing on the retail investors.
r Trader forums where you can exchange ideas with fellow
traders.
After you have done a sufﬁcient amount of Net surﬁng or trading
magazine rifﬂing, you will ﬁnd a number of promising trading strategies. Whittle them down to just a handful based on your personal
circumstances and requirements, and by applying the screening criteria (more accurately described as healthy skepticism) that I listed
earlier:
r How much time do you have for baby-sitting your trading programs?
r How good a programmer are you?
r How much capital do you have?
r Is your goal to earn steady monthly income or to strive for a
large, long-term capital gain?
Even before doing an in-depth backtest of the strategy, you can
quickly ﬁlter out some unsuitable strategies if they fail one or more
of these tests:
r Does it outperform a benchmark?
r Does it have a high enough Sharpe ratio?
r Does it have a small enough drawdown and short enough drawdown duration?
r Does the backtest suffer from survivorship bias?
r Does the strategy lose steam in recent years compared to its earlier years?
