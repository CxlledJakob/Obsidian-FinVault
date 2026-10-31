# Algorithmic Trading (Winning Strategies and Their Rationale) -- Chan, Ernest P_ -- 2013 may 22 -- John Wiley & Sons, Inc_ -- doi 10_1002_9781118676998 -- e374e4354dcd660c7bc666e0297a580b -- Anna’s Archive.pdf — Chapter 1: Chapter 1 (pages 33–51)

--- page 33 ---

20
ALGORITHMIC TRADING
Example 1.1 (Continued)
pos_sim=zeros(length(cl_sim), 1);
for h=0:holddays-1
long_sim_lag=backshift(h, longs_sim);
long_sim_lag(isnan(long_sim_lag))=false;
long_sim_lag=logical(long_sim_lag);
short_sim_lag=backshift(h, shorts_sim);
short_sim_lag(isnan(short_sim_lag))=false;
short_sim_lag=logical(short_sim_lag);
pos_sim(long_sim_lag)=pos_sim(long_sim_lag)+1;
pos_sim(short_sim_lag)=pos_sim(short_sim_lag)-1;
end
ret_sim=backshift(1, pos_sim).*marketRet_sim/holddays;
ret_sim(~isfinite(ret_sim))=0;
if (mean(ret_sim)>= mean(ret))
numSampleAvgretBetterOrEqualObserved=numSampleAvgret
 BetterOrEqualObserved+1;
end
end
We found that out of 10,000 random returns sets, 1,166 have
average strategy return greater than or equal to the observed average
return. So the null hypothesis can be rejected with only 88 percent
probability. Clearly, the shape of the returns distribution curve has
something to do with the success of the strategy. (It is less likely that
the success is due to the mean of the distribution since the position
can be long or short at diff erent times.)
The third hypothesis test involves randomizing the long and short
entry dates, while keeping the same number of long trades and short
trades as the ones in the backtest, respectively. We can accomplish
this quite easily by the MATLAB function randperm:
numSampleAvgretBetterOrEqualObserved=0;
for sample=1:100000
P=randperm(length(longs));
--- page 34 ---

21
BACKTESTING AND AUTOMATED EXECUTION
Example 1.1 (Continued)
longs_sim=longs(P);
shorts_sim=shorts(P);
pos_sim=zeros(length(cl), 1);
for h=0:holddays-1
long_sim_lag=backshift(h, longs_sim);
long_sim_lag(isnan(long_sim_lag))=false;
long_sim_lag=logical(long_sim_lag);
short_sim_lag=backshift(h, shorts_sim);
short_sim_lag(isnan(short_sim_lag))=false;
short_sim_lag=logical(short_sim_lag);
pos(long_sim_lag)=pos(long_sim_lag)+1;
pos(short_sim_lag)=pos(short_sim_lag)-1;
end
ret_sim=backshift(1, pos_sim).*marketRet/holddays;
ret_sim(isnan(ret_sim))=0;
if (mean(ret_sim)>= mean(ret))
numSampleAvgretBetterOrEqualObserved=...
 numSampleAvgretBetterOrEqualObserved+1;
end
end
There is not a single sample out of 100,000 where the average
strategy return is greater than or equal to the observed return.
Clearly, the third test is much weaker for this strategy.
The fact that a null hypothesis is not unique and diff erent null hypotheses can give rise to diff erent estimates of statistical signifi cance is one
reason why many critics believe that hypothesis testing is a fl awed methodology (Gill, 1999). The other reason is that we actually want to know
the conditional probability that the null hypothesis is true given that we
--- page 35 ---

22
ALGORITHMIC TRADING
have observed the test statistic R: P(H0|R). But the procedure we outlined
previously actually just computed the conditional probability of obtaining
a test statistic R given that the null hypothesis is true: P(R|H0). Rarely is
P(R|H0) = P(H0|R).
Even though hyp othesis testing and the rejection of a null hypothesis
may not be a very satisfactory way to estimate statistical signifi cance, the
failure to reject a null hypothesis can inspire very interesting insights. Our
Example 1.1 shows that any random returns distribution with high kurtosis
can be favorable to momentum strategies.

■When Not to Backtest a Strategy
We have spent much eff ort earlier convincing you that you should backtest
every strategy that comes your way before trading it. Why would we recommend against backtesting some strategies? The fact is that there are some
published strategies that are so obviously fl awed it would be a waste of time
to even consider them. Given what you know now about common pitfalls of
backtesting, you are in a good position to judge whether you would want to
backtest a strategy without even knowing the details. We will look at a few
examples here.
Example 1: A strategy that has a backtest annualized return of 30 percent and a Sharpe ratio of 0.3, and a maximum drawdown duration of
two years.
Very few traders (as opposed to “investors”) have the stomach for a strategy that remains “under water” for two years. The low Sharpe ratio coupled
with the long drawdown duration indicates that the strategy is not consistent. The high average return may be just a fl uke, and it is not likely to repeat itself when we start to trade the strategy live. Another way to say this
is that the high return is likely the result of data-snooping bias, and the long
drawdown duration will make it unlikely that the strategy will pass a crossvalidation test. Do not bother to backtest high return but low Sharpe ratio
strategies. Also, do not bother to backtest strategies with a maximum drawdown duration longer than what you or your investors can possibly endure.
Example 2: A long-only crude oil futures strategy returned 20 percent
in 2007, with a Sharpe ratio of 1.5.
A quick check of the total return of holding the front-month crude oil futures in 2007 reveals that it was 47 percent, with a Sharpe ratio of 1.7. Hence,
this trading strategy is not in any way superior to a simple buy-and-hold
--- page 36 ---

23
BACKTESTING AND AUTOMATED EXECUTION
strategy! Moral of the story: We must always choose the appropriate benchmark to measure a trading strategy against. The appropriate benchmark of
a long-only strategy is the return of a buy-and-hold position—the information ratio rather than the Sharpe ratio.
Example 3: A simple “buy-low-sell-high” strategy picks the 10 lowestpriced stocks at the beginning of the year and holds them for a year.
The backtest return in 2001 is 388 percent.
The fi rst question that should come to mind upon reading this strategy is:
Was the strategy backtested using a survivorship-bias-free stock database?
In other words, does the stock database include those stocks that have since
been delisted? If the database includes only stocks that have survived until
today, then the strategy will most likely pick those lucky survivors that happened to be very cheap at the beginning of 2001. With the benefi t of hindsight, the backtest can, of course, achieve a 388 percent return. In contrast,
if the database includes delisted stocks, then the strategy will most likely
pick those stocks to form the portfolio, resulting in almost 100 percent
loss. This 100 percent loss would be the realized return if we had traded
the strategy back in 2001, and the 388 percent return is an infl ated backtest
return that can never be realized. If the author did not specifi cally mention
that the data used include delisted stocks, then we can assume the backtest
suff ers from survivorship bias and the return is likely to be infl ated.
Example 4: A neural net trading model that has about 100 nodes generates a backtest Sharpe ratio of 6.
My alarms always go off whenever I hear the term neural net trading model, not to mention one that has 100 nodes. All you need to
know about the nodes in a neural net is that the number of parameters to be fitted with in-sample training data is proportional to the
number of nodes. With at least 100 parameters, we can certainly fit the
model to any time series we want and obtain a fantastic Sharpe ratio.
Needless to say, it will have little or no predictive power going forward
due to data-snooping bias.
Example 5: A high-frequency E-mini S&P 500 futures trading strategy
has a backtest annual average return of 200 percent and a Sharpe ratio
of 6. Its average holding period is 50 seconds.
Can we really backtest a high-frequency trading strategy? The performance of a high-frequency trading strategy depends on the order types
used and the execution method in general. Furthermore, it depends crucially on the market microstructure. Even if we have historical data of the
entire order book, the profi t from a high-frequency strategy is still very
--- page 37 ---

24
ALGORITHMIC TRADING
dependent on the reactions of other market participants. One has to question whether there is a “Heisenberg uncertainty principle” at work: The
act of placing or executing an order might alter the behavior of the other
market participants. So be very skeptical of a so-called backtest of a highfrequency strategy.
Life is too short to backtest every single strategy that we read about, so
we hope awareness of the common pitfalls of backtesting will help you select what strategies to backtest.

■Will a Backtest Be Predictive of
Future Returns?
Even if we manage to avoid all the common pitfalls outlined earlier and there
are enough trades to ensure statistical signifi cance of the backtest, the predictive power of any backtest rests on the central assumption that the statistical properties of the price series are unchanging, so that the trading rules
that were profi table in the past will be profi table in the future. This assumption is, of course, invalidated often in varying degrees: A country’s economic
prospect changes, a company’s management changes, and a fi nancial market’s
structure changes. In the past decade in the United States, we have witnessed
numerous instances of the last category of changes. Among them:

■Decimalization of U.S. stock quotes on April 9, 2001. (Prior to this date,
U.S. stocks were quoted in one-eighth or one-sixteenth of a penny.) This
caused bid-ask spreads to decrease, but also caused the “displayed liquidity”
at the best bid and ask prices to decrease (Arnuk and Saluzzi, 2012). This in
turn caused profi tability of many statistical arbitrage strategies to decrease
while increasing the profi tability of many high-frequency strategies.

■The 2008 fi nancial crisis that induced a subsequent 50 percent collapse of
average daily trading volumes (Durden, 2012). Retail trading and ownership of common stock is particularly reduced. This has led to decreasing
average volatility of the markets, but with increasing frequency of sudden
outbursts such as that which occurred during the fl ash crash in May 2010 and
the U.S. federal debt credit rating downgrade in August 2011. The overall
eff ect has been a general decrease in profi ts for mean-reverting strategies,
which thrive on a high but constant level of volatility.

■The same 2008 fi nancial crisis, which also initiated a multiyear bear
market in momentum strategies, as discussed in Chapter 6.
--- page 38 ---

25
BACKTESTING AND AUTOMATED EXECUTION

■The SEC’s Regulation NMS implemented in July 2007, which also
contributed to the drastic decrease in the average trade sizes and the obsolescence of the NYSE block trade (Arnuk and Saluzzi, 2012).

■The removal of the old uptick rule for short sales in June 2007 and the
reinstatement of the new Alternative Uptick Rule in 2010.
Strategies that performed superbly prior to each of these “regime shifts”
may stop performing and vice versa. Backtests done using data prior to
such regime shifts may be quite worthless, while backtests done using
recent data may be no more indicative of future profi ts if and when a future regime shift is to occur. The general point of this is that algorithmic
trading is not just about algorithms, programming, and mathematics: An
awareness of such fundamental market and economic issues is also needed
to inform us on whether a backtest is predictive and will continue to be
predictive.

■Choosing a Backtesting and Automated
Execution Platform
Software companies have worked very hard to provide traders with a wide
variety of backtesting and automated execution platforms that cater to every possible level of programming skills. We are faced with two basic choices
when it comes to deciding on a trading platform:
 1. Buying a special-purpose backtesting and execution platform, and
implementing your strategy using that platform’s special-purpose
graphical user interface (GUI) or programming language.
 2. Writing your own backtest and execution program in a generic
programming language such as C++, either in a completely standalone manner with piecemeal purchases of software libraries to make
the task easier or within an integrated development environment
(IDE) that comes with a comprehensive library catering to algorithmic trading.
We consider some criteria for making this choice next.
How Good Is Your Programming Skill?
If you have little skill in programming, then the only choice is to pick a
special-purpose trading platform. These platforms unburden the user from
--- page 39 ---

26
ALGORITHMIC TRADING
having to learn a programming language by presenting a graphical “dragand-drop” user interface for building a trading strategy. Examples of these
products are Deltix and Progress Apama. However, I have found that these
GUIs can be quite limiting in the variety of strategies that you can build,
and in the long run, it is far more effi  cient to become adept in a programming language in order to express your strategy. (Note that Deltix and
Progress Apama also allow other ways to specify a strategy, as explained
below.)
Traders possessing the next level of programming skill should consider
implementing both backtesting and automated execution using one of the
scripting languages. These languages do not require compilation, and you
can instantly see the results the moment you fi nish typing in the mathematical or logical expressions. Many traders’ favorite backtesting platform,
Microsoft Excel, perhaps used in conjunction with Visual Basic (VB) macros,
belongs to this category. But it is actually quite hard to build a reasonably
complicated strategy in Excel, and even harder to debug it. Excel also is not
a particularly high-performance language, so if your strategy is very computationally intensive, it is not going to work. If you use Excel for automated
executions, you may fi nd that you have to use DDE links provided by your
brokerage for market data updates, and you will likely need to add Visual
Basic macros to handle more complicated trading logic, which is quite ineffi  cient. (However, see Box 1.1 for an Excel-like trading platform that is
supercharged for effi  ciency.)
BOX 1.1
Excel on Steroids—The FXone Automated Execution Platform
There is a currency trading platform called FXone that looks like Excel, but the
underlying computational engine is written in a high-performance language
like C++ instead of relying on VB macros. It is a true tick-driven application:
Every tick (in the FX case, a tick is a new quote) triggers a recalculation of
all the values in all of the cells of the spreadsheet. Furthermore, it has an
internal cache for real-time data so that different cells that require the same
data to compute can simply retrieve it from the cache, instead of duplicating
subscriptions of the same data. It is also a true multithreaded platform at two
different levels. First, different strategies written on different Excel workbooks
can get market data updates and submit orders simultaneously. Second,
different cells within the same workbook can also get updates and act on
new data simultaneously. That is to say, even if the calculation in one cell
happens to take very long to complete, it will not prevent other cells from
responding to a new tick by, say, submitting an order. A screenshot of FXone
is shown in Figure 1.1.
--- page 40 ---

27
BACKTESTING AND AUTOMATED EXECUTION
BOX 1.1 (Continued )
FIGURE 1.1 Screenshot of FXone.
--- page 41 ---

28
ALGORITHMIC TRADING
Many special-purpose trading platforms, including QuantHouse and
RTD Tango and the aforementioned Deltix and Progress Apama, also include ways for coding a strategy with their own proprietary programming
languages, which are usually quite simple and easy to learn, maybe as easy
as Visual Basic. Aside from the institutional platforms mentioned here,
many retail traders are familiar with MetaTrader, NinjaTrader, Trading
Blox, or TradeStation Easy Language. I have not tried all of these platforms
personally, but I have a lingering suspicion that despite the apparent ease of
use and other advantages I mention later, they all in some way place some
limitations on the type of strategies that can be backtested and executed.
Requiring just slightly more skills than programming in VB, traders will
fi nd the scripting languages of MATLAB, R, and Python off er vastly more
ease of debugging, much greater fl exibility in the type of strategies that can
be backtested, and higher effi  ciency in backtesting large data sets. These are
what we call “REPL” languages. REPL is programmer-speak for “Read-Eval-
Print-Loop.” That is, you can type in a mathematical expression, and the
program will immediately evaluate it and print out the answer, and get ready
for you to input the next expression. It works exactly like a handheld calculator, but better: You can also save all these expressions in a fi le, and have
the program automatically execute them sequentially. The syntax of these
languages is designed to be more intuitive and easier to understand than
conventional programming languages such as C++ and much more fl exible
in terms of the type of variables that can be used in a program. Scalars, arrays, and strings are all basically dealt with using a similar syntax and passed
along to functions in the same way.
MATLAB can also utilize Java, C++, or C# libraries or application programming interfaces (APIs) and call functions implemented in those libraries or APIs. This allows MATLAB to take advantage of the more effi  cient
implementations in those conventional languages when a task is particularly
computationally intensive. Also, there are far more libraries and APIs that
are written in those conventional languages than those written in MATLAB,
R, or Python, so this feature is often essential.
Many algorithmic traders are aware that MATLAB, R, and Python are
excellent languages for backtesting. But less well known is the fact that
they can be turned into execution platforms as well with the addition
of some toolboxes. Most brokerages have APIs written in Java, C++, or
C#; and, as I said earlier, MATLAB can call functions in APIs written in
such languages, though it does take some familiarity with these languages
--- page 42 ---

29
BACKTESTING AND AUTOMATED EXECUTION
to know how to call these functions. If you would prefer a solution that
obviates making “foreign-language” API calls in MATLAB, there are a
number of commercial products available. MATLAB’s own Datafeed Toolbox can send orders to Trading Technologies’ X_TRADER. To connect
MATLAB to Interactive Brokers, undocumentedmatlab.com has developed an API called IB-Matlab. Another vendor, www.exchangeapi.com,
has a similar API called quant2ib, as well as one called quant2tt for connecting MATLAB to Trading Technologies. For other brokerages, www.
pracplay.com off ers a bridge from MATLAB or R to 15 or more brokers
for a monthly fee. A free, open-source MATLAB API for connecting to
Interactive Brokers was developed by Jev Kuznetsov and is available for
download from MATLAB Central’s File Exchange. Meanwhile, the MAT-
FIX software from agoratron.com lets your MATLAB program send orders using the Financial Information eXchange (FIX) protocol to brokers
or exchanges. You can also use MATLAB to call the Java or .NET functions in QuickFIX, an open source FIX engine (Kozola, 2012). For Python users, the free, open-source software IbPy will connect your Python
trading program to Interactive Brokers. While these add-ons to MATLAB
and Python make it possible to connect to a broker, they nevertheless do
not shield you from all the complexity of such connections. And, more
important, it is cumbersome to use the same program for both backtesting and execution.
If you are a hard-core programmer, you will, of course, have no problem backtesting and automating execution directly in the most fl exible,
most effi  cient, and most robust of programming languages, such as aforementioned trio of Java, C++, or C#. As I said earlier, all brokerages or
exchanges that cater to algorithmic traders provide APIs in one or more
of these languages, or they allow you to submit orders using the FIX
messages, which in turn can be created and transmitted using a program
written in one of these languages. (For example, QuickFIX, mentioned
previously, is available in C++, C#, VB, Python, and Ruby.) But even
here the software industry has come to make our strategy implementation
easier and more robust by providing IDEs designed just for backtesting.
In fact, many of the special-purpose trading platforms (Deltix, Progress
Apama, QuantHouse, RTD Tango, etc.) include ways for coding strategies
using general-purpose, advanced programming languages that make them
resemble IDEs. There are also free, open-source class libraries or IDEs
that I describe in the next section.
--- page 43 ---

30
ALGORITHMIC TRADING
Can Backtesting and Execution Use
the Same Program?
Special-purpose execution platforms typically hide the complexity of connecting to a brokerage or exchange, receiving live market data, sending orders and receiving order confi rmations, updating portfolio positions etc.
from the programmer. Meanwhile, special-purpose backtesting platforms
typically come integrated with historical data. So for many special-purpose
trading platforms, the backtest program can be made the same as the live
execution program by factoring out the pure trading logic into a function,
unencumbered with details of how to retrieve data or where to submit orders, and switching between backtesting mode and live execution mode can
be done by pushing a button to switch between feeding in historical data
versus live market data.
This ease of switching between backtesting and live execution is more
than just convenience: It eliminates any possibility of discrepancies or errors in transcribing a backtest strategy into a live strategy, discrepancies that
often plague strategies written in a general programming language whether
it is C++ or MATLAB. Just as importantly, it eliminates the possibility of
look-ahead bias. As explained before, look-ahead bias means mistakenly incorporating future, unknowable information as part of the historical data
input to the backtest engine. Special-purpose platforms feed in historical
market data into the trade generating engine one tick or one bar at a time,
just as it would feeding in live market data. So there is no possibility that
future information can be used as input. This is one major advantage of using
a special-purpose trading platform.
There is one more advantage in using a platform where the backtesting
and live execution programs are one and the same—it enables true tickbased high-frequency trading strategies backtesting. This is because most industrial-strength live execution programs are “event-driven”; that is, a trade
is triggered by the arrival of a new tick, not the end of an arbitrary time
bar. So if the input historical data is also tick-based, we can also backtest a
high-frequency strategy that depends on the change of every tick or even
every change in the order book. (I said “in theory” assuming that your hardware is powerful enough. Otherwise, see the discussion later in this chapter
in the section “What Type of Asset Classes or Strategies Does the Platform
Support?”) Of course, we can backtest tick-based strategies in MATLAB by
feeding every tick into the program as well, though that is quite a cumbersome procedure.
--- page 44 ---

31
BACKTESTING AND AUTOMATED EXECUTION
If you are a competent programmer who prefers the fl exibility of a general
purpose programming language, yet you want to use the same program for
both backtesting and live trading because of the preceding considerations,
you can still use the institutional-grade special-purpose platforms as IDEs,
or you can use the many open-source IDEs available: Marketcetera, Trade-
Link, Algo-Trader, ActiveQuant. I call them IDEs, but they are more than
just a trading strategy development environment: They come with libraries
that deal with the nuts and bolts of connecting to and exchanging data with
your broker, much like a special-purpose platform does. Many of them are
also integrated with historical data, which is an important time saver. As
an added bonus, these open-source IDEs are either free or quite low-cost
compared to special-purpose platforms. I display in Table 1.2 the languages,
markets, and brokers that they support. (FIX as a broker means that the
system can directly access any execution venues via the FIX protocol, regardless of clearing broker.) I also indicate whether the IDE is tick based
(sometimes called event driven or stream based ).
One should note that Table 1.2 only compares features of open-source
IDEs. The institutional-grade special-purpose platforms typically have all of
these features.
What Type of Asset Classes or Strategies Does the
Platform Support?
While using a special-purpose platform for trading strategies has several
important advantages described earlier, few but the most high end of these
TABLE 1.2
Comparisons of Open-Source Integrated Development Environments
(IDEs) for Backtesting and Automated Execution
IDE
Language(s)
Asset
class(es)
Broker(s)
Tick
based?
CEP
enabled?
ActiveQuant
Java, MATLAB, R
Various
CTS, FIX, Trading
Technologiessupported brokers
Yes
No
Algo-Trader
Java
Various
Interactive Brokers,
FIX
Yes
Yes
Marketcetera
Java, Python, Ruby
Various
Various, FIX
Yes
Yes
OpenQuant
.NET (C#, VB)
Various
Various, FIX
?
No
TradeLink
.NET (C#, C++,
VB), Java, Pascal,
Python
Various
Various, FIX
Yes
No
--- page 45 ---

32
ALGORITHMIC TRADING
platforms support all possible asset classes, including stocks, futures, currencies, and options. For example, the popular MetaTrader is for currencies
trading only. It is especially diffi  cult for these platforms to trade strategies that involve arbitrage between diff erent asset classes, such as between
futures and stocks or currencies and futures. The open-source IDEs are better able to handle these situations. As Table 1.2 indicates, most IDEs can
trade a variety of asset classes. But, as usual, the most fl exible solution in this
respect is a stand-alone program written outside of any IDE.
Beyond asset classes, many special-purpose platforms also place restrictions on the type of strategies that they support even within one asset class.
Often, simple pairs trading strategies require special modules to handle. Most
lower-end platforms cannot handle common statistical arbitrage or portfolio
trading strategies that involve many symbols. Open-source IDEs do not have
such restrictions, and, of course, neither do stand-alone programs.
What about high(er)-frequency trading? What kind of platforms can support this demanding trading strategy? The surprising answer is that most
platforms can handle the execution part of high-frequency trading without
too much latency (as long as your strategy can tolerate latencies in the 1- to
10-millisecond range), and since special-purpose platforms as well as IDEs
typically use the same program for both backtesting and execution, backtesting shouldn’t in theory be a problem either.
To understand why most platforms have no trouble handling highfrequency executions, we have to realize that most of the latency that needs
to be overcome in high-frequency trading is due to live market data latency,
or brokerage order confi rmation latency.
 1. Live market data latency:
For your program to receive a new quote or trade price within 1 to
10 milliseconds (ms), you have to colocate your program at the exchange or in your broker’s data center (see Box 1.2); furthermore,
you have to receive a direct data feed from the exchanges involved, not
from a consolidated data feed such as SIAC’s Consolidated Tape System
(CTS). (For example, Interactive Brokers’ data feed only off ers snapshots of market data every 250 ms.)
 2. Brokerage order confi rmation latency:
If a strategy submits limit orders, it will depend on a timely order status confi rmation before it can decide what to do next. For some retail
brokerages, it can take up to six seconds between the execution of an
order and your program receiving the execution confi rmation, virtually
--- page 46 ---

33
BACKTESTING AND AUTOMATED EXECUTION
BOX 1.2
Colocation of Trading Programs
The general term colocation can mean several ways of physically locating
your trading program outside of your desktop computer. Stretching the
defi nition a bit, it can mean installing your trading program in a cloud server or
VPS (virtual private server) such as Amazon’s EC2, slicehost.com, or gogrid.
com. The advantage of doing so is to prevent power or Internet outages
that are more likely to strike a private home or offi ce than a commercial data
center, with its backup power supply and redundant network connectivity.
Colocating in a cloud server does not necessarily shorten the time data take
to travel between your brokerage or an exchange to your trading program,
since many homes or offi ces are now equipped with a fi ber optics connection
to their Internet service provider (e.g., Verizon’s FiOS in the United States, and
Bell’s Fibe Internet in Canada). To verify whether colocating in a virtual private
server (VPS) actually reduces this latency, you would need to conduct a test
yourself by “pinging” your broker’s server to see what the average round
trip time is. Certainly, if your VPS happens to be located physically close to
your broker or exchange, and if they are directly connected to an Internet
backbone, this latency will be smaller. (For example, pinging the Interactive
Brokers’ quote server from my home desktop computer produces an average
round trip time of about 55 ms, pinging the same server from Amazon’s EC2
takes about 25 ms, and pinging it from various VPSs located near Interactive
Brokers takes about 16 to 34 ms.)
I mention VPS only because many trading programs are not so computationally intensive as to require their own dedicated servers. But if they are,
you can certainly upgrade to such services at many of the hosting companies
familiar with the requirements of the fi nancial trading industry such as Equinix
and Telx, both of whom operate data centers in close proximity to the various
exchanges.
If your server is already in a secure location (whether that is your offi ce
or a data center) and is immune to power outage, then all you need is a
fast connection to your broker or the exchange. You can consider using
an “extranet,” which is like the Internet but operated by a private company,
which will guarantee a minimum communication speed. BT Radianz, Savvis,
and TNS are examples of such companies. If you have a large budget, you
can also ask these companies to build a dedicated communication line from
your server to your broker or exchange as well.
The next step up in the colocation hierarchy is colocating inside your
brokerage’s data center, so that quotes or orders confi rmation generated
by your broker are transmitted to your program via an internal network,
unmolested by the noise and vagaries of the public Internet. Various brokers
that cater to professional traders have made available colocation service:
examples are Lime Brokerage and FXCM. (Because of colocation, clients
of Lime Brokerage can even receive direct data feeds from the NYSE at a
(Continued )
--- page 47 ---

34
ALGORITHMIC TRADING
BOX 1.2 (Continued )
relatively low rate, which, as I mentioned before, is faster than the consolidated
SIAC CTS data feed.)
The ultimate colocation is, of course, situating your trading server at the
exchange or ECN itself. This is likely to be an expensive proposition (except
for forex ECNs), and useful only if you have a prime broker relationship, which
allows you to have “sponsored access” to connect to the exchange without
going through the broker’s infrastructure (Johnson, 2010). Such prime broker
relationships can typically be established only if you can generate institutionallevel commissions or have multimillion-dollar account. The requirements as
well as expenses to establish colocation are lower for forex prime brokers and
ECNs. Most forex ECNs including Currenex, EBS, FXall, and Hotspot operate
within large commercial data centers such as Equinix’s NY4 facility, and it is
not too expensive to colocate at that facility or sign up with a VPS that does.
Some traders have expressed concern that colocating their trading
programs on a remote server exposes them to possible theft of their
intellectual property. The simplest way is eliminate this risk is to just store
“executables” (binary computer codes that look like gibberish to humans)
on these remote servers, and not the source code of your trading algorithm.
(Even with a MATLAB program, you can convert all the .m fi les to .p fi les
before loading them to the remote server.) Without source codes, no one
can know the operating instructions of running the trading program, and no
one will be foolish enough to risk capital on trading a black-box strategy of
which they know little about. For the truly paranoid, you can also require an
ever-changing password that depends on the current time to start a program.
ensuring that no high-frequency trading can be done. Even if your brokerage has order confi rmation latency below 10 ms, or if they allow
you to have direct market access to the exchanges so you get your order
status confi rmation directly from the exchanges, you would still need
to colocate your program with either your broker in the former case,
or with the exchange in the latter case.
 Practically any software program (other than Excel running with a
VB macro) takes less than 10 ms to submit a new order after receiving
the latest market data and order status updates, so software or hardware
latency is usually not the bottleneck for high-frequency trading, unless
you are using one program to monitor thousands of symbols. (Concerning this last point, see Box 1.3 for issues related to multithreading.) But
backtesting a high-frequency strategy is entirely a diff erent matter. To do
this, you will be required to input many months of tick data (trades and
quotes), maybe on many symbols, into the backtesting platform. Worse,
sometimes you have to input level 2 quotes, too. Just the quantity of
--- page 48 ---

35
BACKTESTING AND AUTOMATED EXECUTION
data will overwhelm the memory of most machines, if they are not handled in special ways (such as using parallel computing algorithms). Most
special-purpose backtesting platforms are not designed to be especially
intelligent when handling this quantity of data, and most of them are not
equipped at all to backtest data with all of bid/ask/last tick prices (and
sizes) nor level 2 quotes either. So backtesting a high-frequency strategy
usually requires that you write your own stand-alone program with special customization. Actually, backtesting a high-frequency strategy may
not tell you much about its real-life profi tability anyway because of the
Heisenberg uncertainty principle that I mentioned before.
 Besides high-frequency trading, news-driven trading often causes all
but the top-end special-purpose platforms to stumble. News-driven
trading by defi nition requires as input a machine-readable news feed.
Most special-purpose platforms do not have this capability, and neither
do most open-source IDEs. Exceptions include Progress Apama, which
incorporates both Dow Jones and Reuters machine-readable news feed,
and Deltix, which integrates Ravenpack’s News Sentiment data feed.
Among IDE’s, Marketcetera off ers a newsfeed from benzinga.com
(which is unlikely to match the speed of delivery of Bloomberg, Dow
Jones, and Reuters). If you are writing your own stand-alone trading
BOX 1.3
Multithreading and High-Frequency Trading of Multiple Symbols
Multithreading for a trading platform means that it can respond to multiple
events (usually the arrival of a new tick) simultaneously. This is particularly
important if the program trades multiple symbols simultaneously, which is
often the case for a stock-trading program. You certainly don’t want your buy
order for AAPL to be delayed just because the program is deciding whether to
sell BBRY! If you write your own stand-alone trading program using a modern
programming language such as Java or Python, you won’t have any problem
with multithreading because this ability is native to such languages. However,
if you use MATLAB, you will need to purchase the Parallel Computing Toolbox
as well; otherwise, there is no multithreading. (Even if you purchase that
Toolbox, you are limited to 12 independent threads, hardly enough to trade
500 stocks simultaneously!) But do not confuse the lack of multithreading
in MATLAB with the “loss of ticks.” If you write two “listeners,” A and B, in
MATLAB to receive tick data from two separate symbols, because the fact
that listener A is busy processing a tick-triggered event doesn’t mean that
listener B is “deaf.” Once listener A has fi nished processing, listener B will
start to process those tick events that it has received while A was busy, with
no lost ticks (Kuznetsov, 2010).
--- page 49 ---

36
ALGORITHMIC TRADING
program, you have the fl exibility of connecting to these news feed either using the news provider’s API (e.g., both Dow Jones and Thomson
Reuters have made available their machine-readable news through an
API) or simply read a news XML fi le ftp’ed to your hard-drive periodically by the news provider. If you are news trading at high frequency, the
former expensive solution is an absolute necessity. Otherwise, there are
much more aff ordable solutions from vendors such as Newsware. I will
discuss more on the topic of event-driven trading in Chapter 7.
Does the Platform Have Complex
Event Processing?
Complex event processing (CEP) is a fashionable term to describe a program
responding to an event instantaneously and taking appropriate action. The
events that concern us are usually the arrival of a new tick, or the delivery
of a news item. For an algorithmic trader, one important point is that the
program is event driven, and not bar driven. That is, the program does not
go poll prices or news items at the end of each bar and then decide what to
do. Because CEP is event driven, there is no delay between the occurrence
of an event and the response to it.
If instantaneity is the only strength of CEP, then we can just use the socalled callback functions that almost every brokerage API provides. A callback function is also triggered whenever a new tick or news item arrives,
and based on this new data we can perform all kinds of computations and
determine whether to submit an order. This is easy when the rule required
is simply “moving average of the price over the last hour.”
But what if the rules are “complex,” such as “sell when the order fl ow in
the last half hour is positive, the price is above the moving average, the volatility is low, and an important news item just arrived”?
What if the rule involves many clauses like during, between, afterwards, in
parallel when applied to the sequence of events? According to CEP afi cionados,
it is much more succinct to express these complicated rules using a CEP language than a traditional programming language. But what about the argument
that trading rules should be simple to avoid data-snooping bias? Their answer
is that they are not data mining the data to fi nd arbitrary rules, but simply
implementing rules that seasoned traders already know are profi table. I am not
entirely convinced by their arguments, but if you are, you should know that
Progress Apama mentioned above is distinguished by their CEP technology.
Certain free, open-source IDEs have CEP, too, as you can see from Table 1.2.
--- page 50 ---

37
BACKTESTING AND AUTOMATED EXECUTION
• Backtesting is useless if it is not predictive of future performance of a
strategy, but pitfalls in backtesting will decrease its predictive power.
• Eliminating pitfalls:
• A platform that uses the same program for both backtesting and live
executions can eliminate look-ahead bias.
• Out-of-sample testing, cross-validation, and high Sharpe ratios are
all good practices for reducing data-snooping bias, but none is more
defi nitive than walk-forward testing.
• Simple models are a simple cure for data-snooping bias.
• “Why did my model generate a ‘short’ signal for THQI on 2012/7/9? Oh,
that’s because I forgot to adjust its historical prices for a 1:10 reverse
stock split!”
• “Did your model just buy the stock CMC? Are you sure it didn’t forget to
adjust its historical prices because today is its ex-date for dividends?”
• “I see that your model is long only. Did you make sure your data don’t
have survivorship bias?”
• “The backtest of your mean-reverting stock-trading model using closing
prices is excellent, but expect a defl ation of the results if you test it again
using primary exchange data.”
• “Your model performed brilliantly during November 2008. But did it short
a lot of fi nancial stocks back then? Don’t forget that short sales of those
stocks were banned.”
• “This high-frequency stock-trading model looks good on backtest, but I
wonder if it incorporated uptick rules for their short trades.”
• “Your futures calendar spread model uses the differences in price to form
the spread. Why are you back-adjusting your prices using returns gap?”
• “Why is it that my mean-reverting intraday futures spread performed so
well in backtest but so poorly in live trading? Oh, I should have used tickbased instead of bar-based data for my backtest.”
• “Your backtest of this momentum strategy seems to be without any
pitfalls. But just because it performed well before 2008 doesn’t mean it
will perform well afterward.”
• Statistical signifi cance of backtests:
• “What do you mean by saying that the expected APR of this strategy is
10 percent and is statistically signifi cant to within 1 percent?” Answer:
“It means by running the strategy on 10,000 simulated price series with
the same length and the same fi rst three moments as the historical price
series, there are only 100 sample series where the APR is equal to or
greater than 10 percent.”
KEY POINTS
(Continued )
--- page 51 ---

38
ALGORITHMIC TRADING
• “What do you mean by saying that the expected APR of this strategy is
10 percent and is statistically signifi cant to within 1 percent?” Alternative
answer: “It means by randomizing the entry dates of my trades, there is
only 1 in 100 random permutations where the APR is equal to or greater
than 10 percent.”
• Which backtest platform to pick?
• “I am a brilliant mathematician starting a fund with $50 million to invest,
but I don’t know how to program. What trading platform should I use?”
Pick an institutional special-purpose platform like Deltix, QuantHouse,
Progress Apama, or RTD Tango.
• “I am an experienced, discretionary, independent trader, and I want to
automate my strategies. What trading platform should I use?” Pick a retail
special-purpose platform like MetaTrader, NinjaTrader, Trading Blox, or
TradeStation.
• “I am a quant who is great with strategy research using MATLAB.
But how should I implement these strategies and go ‘live’?” Try
exchangeapi.com’s quant2ib API for Interactive Brokers, quant2tt for
Trading Technologies, www.pracplay.com for other brokers, or MATFIX for
FIX connections.
• “I am a good C++, C#, and Java programmer, but I hate dealing with
low-level connections to the brokerage, and I hate having to rewrite my
connections every time I change brokers.” Try one of the IDEs such as
Marketcetera, TradeLink, AlgoTrader, or ActiveQuant.
• Automating executions:
• “I want to colocate my trading program at a data center to reduce my
order confi rmation latency below 10 ms.” Are you sure your broker has an
order confi rmation latency shorter than 10 ms?
• “I am colocated at Amazon’s EC2. Market data fed to my trading
programs should be much more up-to-date than getting them at my
desktop PC.” Not necessarily: EC2’s server may be farther away (in
Internet distance) from your broker’s data server than your desktop PC.
• “I am using MATLAB’s Parallel Computing Toolbox, and I run my
program on a GPU. Therefore, I can trade all 500 stocks in the SPX
simultaneously.” Even with MATLAB’s Parallel Computing Toolbox, you
are limited to handling 12 stocks simultaneously. Writing your own Java
or Python program will allow true multithreading on a graphics processing
unit (GPU).
• “My IDE isn’t CEP enabled. I can’t really run a tick-based trading
strategy.” Even platforms that are not CEP enabled often have callback
functions that enable your program to be triggered by ticks.
