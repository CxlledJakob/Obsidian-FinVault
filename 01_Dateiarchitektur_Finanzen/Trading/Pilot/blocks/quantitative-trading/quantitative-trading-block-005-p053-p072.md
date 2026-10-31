# Quantitative Trading_ How to Build Your Own Algorithmic -- Ernest P_ Chan -- Wiley Trading, 1, 2008 -- John Wiley & Sons, Ltd_ -- isbn13 9780470284889 -- e4d660df1c1a75e8676a28ff4f852fa7 -- Anna’s Archive.pdf — Chapter 3: Backtesting (pages 53–72)

--- page 53 ---

C H A P T E R 3
Backtesting
A key difference between a traditional investment management process and a quantitative investment process is the possibility of backtesting a quantitative investment strategy to see how it would have
performed in the past. Even if you found a strategy described in
complete detail with all the historical performance data available,
you would still need to backtest it yourself. This exercise serves
several purposes. If nothing else, this replication of the research will
ensure that you have understood the strategy completely and have
reproduced it exactly for implementation as a trading system. Just
as in any medical or scientiﬁc research, replicating others’ results
also ensures that the original research did not commit any of the
common errors plaguing this process. But more than just performing due diligence, doing the backtest yourself allows you to experiment with variations of the original strategy, thereby reﬁning and
improving the strategy.
In this chapter, I will describe the common platforms that can
be used for backtesting, various sources of historical data useful for
backtesting, a minimal set of standard performance measures that a
backtest should provide, common pitfalls to avoid, and simple re-
ﬁnements and improvements to strategies. A few fully developed
backtesting examples will also be presented to illustrate the principles and techniques described.
31
--- page 54 ---

32
QUANTITATIVE TRADING
COMMON BACKTESTING PLATFORMS
There are numerous commercial platforms that are designed for
backtesting, some of them costing tens of thousands of dollars. In
keeping with the focus on start-ups in this book, I start with those
with which I am familiar and that can be purchased economically
and are widely used.
Excel
This is the most basic and most common tool for traders, whether
retail or institutional. You can enhance its power further if you can
write Visual Basic macros. The beauty of Excel is “What you see
is what you get” (or WYSIWYG in computing parlance). Data and
program are all in one place so that nothing is hidden. Also, a common backtesting pitfall called “look-ahead bias,” which will be explained later, is unlikely to occur in Excel (unless you use macros,
which renders it no longer WYSIWYG) because you can easily align
the dates with the various data columns and signals on a spreadsheet. Another advantage of Excel is that often backtesting and live
trade generation can be done from the same spreadsheet, eliminating any duplication of programming efforts. The major disadvantage
of Excel is that it can be used to backtest only fairly simple models.
But, as I explained in the previous chapter, simple models are often
the best!
MATLAB
MATLAB R⃝(www.mathworks.com) is one of the most common
backtesting platforms used by quantitative analysts and traders in
large institutions. It is ideal for testing strategies that involve a
large portfolio of stocks. (Imagine backtesting a strategy involving
1,500 symbols on Excel—it is possible, but quite painful.). It has numerous advanced statistical and mathematical modules built in, so
traders do not have to reinvent the wheel if their trading algorithms
involve some sophisticated but common mathematical concepts.
--- page 55 ---

Backtesting
33
(A good example is principal component analysis—often used in
factor models in statistical arbitrage trading, and a hassle to implement in other programming languages. See Example 7.4.) There
is also a large number of third-party freeware available for download from the Internet, many of them very useful for quantitative
trading purposes (an example is the cointegration package used in
Example 7.2). Finally, MATLAB is very useful in retrieving web
pages with ﬁnancial information and parsing it into a useful form
(so-called web scraping). Example 3.1 shows how this can be done.
Despite the seeming sophistication of the platform, it is actually
very easy to learn (at least for basic usage) and it is very quick to
write a complete backtest program using this language. The main
drawback of MATLAB is that it is relatively expensive: it costs over
$1,000 to acquire a license. However, there are several clones of
MATLAB on the market where you can write and use codes that
are very similar to MATLAB:
r O-Matrix (www.omatrix.com)
r Octave (www.gnu.org/software/octave)
r Scilab (www.scilab.org)
These clones may cost only several hundred dollars, or may be
entirely free. Not surprisingly, the more expensive the clone is, the
more compatible it is with programs written in MATLAB. (Of course,
if you intend to write all the programs yourself and not use any third
party’s codes, compatibility is not an issue. But then you would be
forfeiting one of the main beneﬁts of using this language.) The other
drawback of MATLAB is that it is very useful for backtesting but
clumsy to use as an execution platform. So, often, you will need
to build a separate execution system in another language once you
have backtested your strategy. Despite these drawbacks, MATLAB
has found widespread use within the quantitative trading community. I will include MATLAB codes for all the backtesting examples
in this book as well as provide a quick survey of the MATLAB language itself in the appendix.
--- page 56 ---

34
QUANTITATIVE TRADING
Example 3.1: Using MATLAB to Scrape Web Pages
for Financial Data
MATLAB is not only useful for numerical computations, but also for text
parsing. Following is an example of using MATLAB to retrieve a stock’s
historical price information from Yahoo! Finance:
clear; % make sure previously defined variables are
%erased.
symbol=‘IBM’; % the stock of interest
% retrieving a webpage
historicalPriceFile =...
urlread([‘http://finance.yahoo.com/q/hp?s=’, symbol]);
% extracting the date field to a cell array of cells
dateField=...
regexp(historicalPriceFile, ...
’<td class="yfnc tabledata1" nowrap align="right">...
([\d\w-]+)</td>’, ‘tokens’);
% extracting the numbers field to a cell array of cells
numField=regexp(historicalPriceFile, ...
’<td class="yfnc tabledata1" align="right">...
([\d\.,]+)</td>’, ‘tokens’);
% convert to cell array of strings
dates=[dateField{:}]’;
% convert to cell array of strings
numField=[numField{:}]’;
% convert to doubles array
op=str2double(numField (1:6:end)); % open
hi=str2double(numField (2:6:end)); % high
lo=str2double(numField (3:6:end)); % low
cl=str2double(numField (4:6:end)); % close
vol=str2double(numField (5:6:end)); % volume
adjCl=str2double(numField (6:6:end)); % adjusted close
This
program
ﬁle
is
available
for
download
as
epchan.com/book/
example3 1.m, with “sharperatio” as both username and password. There is
one limitation to this web-scraping script: It can retrieve only one web page
at a time. Because Yahoo! displays its historical data over many pages, it is
not really useful for retrieving the entire price history of IBM. Nevertheless,
it is a simple illustration of MATLAB’s text processing functions.
--- page 57 ---

Backtesting
35
TradeStation
TradeStation (www.tradestation.com) is familiar to many retail
traders as a brokerage that provides all-in-one backtesting and trade
execution platforms linked to the brokerage’s servers. The main advantages of this setup are:
r Most of the historical data necessary for backtesting is readily
available, whereas you have to download the data from somewhere else if you use Excel or MATLAB.
r Once you have backtested the program, you can immediately
generate orders using the same program and transmit them to
the brokerage.
The disadvantages of this approach are that once you have written the software for your strategy, you are tied to TradeStation as
your broker, and the proprietary language used by TradeStation is
not as ﬂexible as MATLAB and does not include some of the more
advanced statistical and mathematical functions some traders use.
Nevertheless, if you prefer the ease of use of an all-in-one system,
TradeStation may be a good choice.
Since I have not used TradeStation in my own work, I will not
include backtesting examples in TradeStation.
High-End Backtesting Platforms
In case you do have the ﬁnancial resources to purchase a high-end,
institutional-grade backtesting platform, here is a partial list:
r FactSet’s Alpha Testing (www.factset.com/products/directions/
qim/alphatesting)
r Clariﬁ’s
ModelStation
(www.clariﬁ.com/ModelStation-Overview.php)
r Quantitative Analytics’ MarketQA (www.qaisoftware.com)
r Barra’s Aegis System (www.mscibarra.com/products/analytics/
aegis)
r Logical Information Machines (www.lim.com)
r Alphacet’s Discovery (www.alphacet.com)
--- page 58 ---

36
QUANTITATIVE TRADING
Of all these, I have personal experience with only Logical Information Machines and Alphacet Discovery. Logical Information
Machines is excellent for testing futures trading strategies, but it is
weaker for equities strategies, based on my experience 10 years ago.
Alphacet Discovery is a new product that integrates data retrieval,
backtesting, optimization with machine learning algorithms, and automated execution. It is quite powerful for backtesting and trading a
range of markets including futures, equities, and currencies. Example 7.1 is a backtest example using the Discovery platform.
FINDING AND USING HISTORICAL
DATABASES
If you have a strategy in mind that requires a speciﬁc type of historical data, the ﬁrst thing to do is to Google that type of data. You
will be surprised how many free or low-cost historical databases
are available out there for many types of data. (For example, try
the search phrase “free historical intraday futures data.”) Table 3.1
includes a number of the databases that I have found useful over
the years, most of them either free or very low cost. I have deliberately left out the expensive databases from Bloomberg, Dow Jones,
FactSet, Thomson Reuters, or Tick Data. Though they have almost
every type of data imaginable for purchase, these data vendors cater
mostly to more established institutions and are typically not in the
price range of individuals or start-up institutions.
While ﬁnding sources of data on the Internet is even easier than
ﬁnding prospective strategies, there are a number of issues and pitfalls with many of these databases that I will discuss later in this section. These issues apply mostly to stock and exchange-traded fund
(ETF) data only. Here are the most important ones.
Are the Data Split and Dividend Adjusted?
When a company had its stocks split N to 1 (N is usually 2, but
can be a fraction like 0.5 as well. When N is smaller than 1, it is
--- page 59 ---

Backtesting
37
TABLE 3.1
Historical Databases for Backtesting
Source
Pros
Cons
Daily Stock Data
Finance.yahoo.com
Free. Split/dividend adjusted.
Has survivorship bias.
Can download only
one symbol at a
time.
HQuotes.com
Low cost. Same data as
ﬁnance.yahoo.com. Software
enables download of multiple
symbols.
Has survivorship bias.
Split but not
dividend adjusted.
CSIdata.com
Low cost. Source of Yahoo! and
Google’s historical data. Software
enables download of multiple
symbols.
Has survivorship bias.
TrackData.com
Low cost. Split/dividend adjusted.
Software enables download of
multiple symbols. Fundamental data
available.
Has survivorship bias.
CRSP.com
Survivorship bias free.
Expensive. Updated
only once a month.
Daily Futures Data
Quotes-plus.com
Low cost. Software enables download
of multiple symbols.
CSIdata.com
(See above.)
Daily Forex Data
Oanda.com
Free.
Intraday Stock Data
HQuotes.com
(See above.)
Short history for
intraday data.
Intraday Futures Data
DTN.com
Bid-ask data history available as part
of NxCore product.
Expensive: requires
subscription to live
datafeed.
Intraday Forex Data
GainCapital.com
Free. Long history.
--- page 60 ---

38
QUANTITATIVE TRADING
called a reverse split) with an ex-date of T, all the prices before T
need to be multiplied by 1/N. Similarly, when a company issued a
dividend $d per share with an ex-date of T, all the prices before T
need to be multiplied by the number (Close(T – 1) – d)/Close(T –
1), where Close(T – 1) is the closing price of the trading day before
T. Notice that I adjust the historical prices by a multiplier instead
of subtracting $d so that the historical daily returns will remain the
same preand postadjustment. This is the way Yahoo! Finance adjusts its historical data, and is the most common way. (If you adjust
by subtracting $d instead, the historical daily changes in prices will
be the same preand postadjustment, but not the daily returns.) If
the historical data are not adjusted, you will ﬁnd a drop in price
at the ex-date’s market open from previous day’s close (apart from
normal market ﬂuctuation), which may trigger an erroneous trading
signal.
I recommend getting historical data that are already split and
dividend adjusted, because otherwise you would have to ﬁnd a
separate historical database (such as earnings.com) of splits and
dividends and apply the adjustments yourself—a somewhat tedious and error-prone task, which I will describe in the following
example.
Example 3.2: Adjusting for Splits and Dividends
Here we look at IGE, an ETF that has had both splits and dividends in its
history. It had a 2:1 split on June 9, 2005 (the ex-date). Let’s look at the
unadjusted prices around that date (you can download the historical prices
of IGE from Yahoo! Finance into an Excel spreadsheet):
Date
Open
High
Low
Close
6/10/2005
73.98
74.08
73.31
74
6/9/2005
72.45
73.74
72.23
73.74
6/8/2005
144.13
146.44
143.75
144.48
6/7/2005
145
146.07
144.11
144.11
--- page 61 ---

Backtesting
39
We need to adjust the prices prior to 6/9/2005 due to this split. This
is easy: N = 2 here, and all we need to do is to multiply those prices by 1
2.
The following table shows the adjusted prices:
Date
Open
High
Low
Close
6/10/2005
73.98
74.08
73.31
74
6/9/2005
72.45
73.74
72.23
73.74
6/8/2005
72.065
73.22
71.875
72.24
6/7/2005
72.5
73.035
72.055
72.055
Now, the astute reader will notice that the adjusted close prices here
do not match the adjusted close prices displayed in the Yahoo! Finance
table. The reason for this is that there have been dividends distributed after 6/9/2005, so the Yahoo! prices have been adjusted for all those as
well. Since each adjustment is a multiplier, the aggregate adjustment is
just the product of all the individual multipliers. Here are the dividends
from 6/9/2005 to November 2007, together with the unadjusted closing
prices of the previous trading days and the resulting individual multipliers:
Ex-Date
Dividend
Prev Close
Multiplier
9/26/2007
0.177
128.08
0.998618
6/29/2007
0.3
119.44
0.997488
12/21/2006
0.322
102.61
0.996862
9/27/2006
0.258
91.53
0.997181
6/23/2006
0.32
92.2
0.996529
3/27/2006
0.253
94.79
0.997331
12/23/2005
0.236
89.87
0.997374
9/26/2005
0.184
89
0.997933
6/21/2005
0.217
77.9
0.997214
(Check out the multipliers yourself on Excel using the formula I gave
above to see if they agree with my values here.) So the aggregate multiplier for the dividends is simply 0.998618 × 0.997488 × · · · × 0.997214 =
0.976773. This multiplier should be applied to all the unadjusted prices
on or after 6/9/2005. The aggregate multiplier for the dividends and the
split is 0.976773 × 0.5 = 0.488386, which should be applied to all the
--- page 62 ---

40
QUANTITATIVE TRADING
unadjusted prices before 6/9/2005. So let’s look at the resulting adjusted
prices after applying these multipliers:
Date
Open
High
Low
Close
6/10/2005
72.26163
72.35931
71.6072
72.28117
6/9/2005
70.76717
72.02721
70.55228
72.02721
6/8/2005
70.39111
71.51929
70.20553
70.56205
6/7/2005
70.81601
71.33858
70.38135
70.38135
Now compare with the table from Yahoo! around November 1, 2007:
Date
Open
High
Low
Close
Volume
Adj Close
6/10/2005
73.98
74.08
73.31
74
179300
72.28
6/9/2005
72.45
73.74
72.23
73.74
853200
72.03
6/8/2005
144.13
146.44
143.75
144.48
109600
70.56
6/7/2005
145
146.07
144.11
144.11
58000
70.38
You can see that the adjusted closing prices from our calculations and
from Yahoo! are the same (after rounding to two decimal places). But, of
course, when you are reading this, IGE will likely have distributed more
dividends and may have even split further, so your Yahoo! table won’t look
like the one above. It is a good exercise to check that you can make further
adjustments based on those dividends and splits that result in the same
adjusted prices as your current Yahoo! table.
Are the Data Survivorship Bias Free?
We already covered this issue in Chapter 2. Unfortunately, databases
that are free from survivorship bias are quite expensive and may
not be affordable for a start-up business. One way to overcome this
problem is to start collecting point-in-time data yourself for the beneﬁt of your future backtest. If you save the prices each day of all the
stocks in your universe to a ﬁle, then you will have a point-in-time
or survivorship-bias-free database to use in the future. Another way
to lessen the impact of survivorship bias is to backtest your strategies on more recent data so that the results are not distorted by too
many missing stocks.
--- page 63 ---

Example 3.3: An Example of How Survivorship Bias Can
Artiﬁcially Inﬂate a Strategy’s Performance
Here is a toy “buy low-price stocks” strategy (Warning: This toy strategy is
hazardous to your ﬁnancial health!). Let’s say from a universe of the 1,000
largest stocks (based on market capitalization), we pick 10 that have the
lowest closing prices at the beginning of the year and hold them (with equal
initial capital) for one year. Let’s look at what we would have picked if we
had a good, survivorship-bias-free database:
Closing Price
Closing Price
SYMBOL
on 1/2/2001
on 1/2/2002
Terminal Price
ETYS
0.2188
NaN
0.125
MDM
0.3125
0.49
0.49
INTW
0.4063
NaN
0.11
FDHG
0.5
NaN
0.33
OGNC
0.6875
NaN
0.2
MPLX
0.7188
NaN
0.8
GTS
0.75
NaN
0.35
BUYX
0.75
NaN
0.17
PSIX
0.75
NaN
0.2188
All but MDM were delisted sometime between 1/2/2001 and 1/2/2002
(after all, the dot-com bubble was seriously bursting then!). The NaNs indicate those with nonexistent closing prices on 1/2/2002. The Terminal Price
column indicates the last prices at which the stocks were traded on or before
1/2/2002. The total return on this portfolio in that year was –42 percent.
Now, let’s look at what we would have picked if our database had survivorship bias and actually missed all those stocks that were delisted that
year. We would then have picked the following list instead:
SYMBOL
Closing Price on 1/2/2001
Closing Price on 1/2/2002
MDM
0.3125
0.49
ENGA
0.8438
0.44
NEOF
0.875
27.9
ENP
0.875
0.05
MVL
0.9583
2.5
URBN
1.0156
3.0688
FNV
1.0625
0.81
APT
1.125
0.88
FLIR
1.2813
9.475
RAZF
1.3438
0.25
41
--- page 64 ---

42
QUANTITATIVE TRADING
Notice that since we select only those stocks that “survived” until at
least 1/2/2002, they all have closing prices on that day. The total return on
this portfolio was 388 percent!
In this example, –42 percent was the actual return a trader would experience following this strategy, whereas 388 percent is a ﬁctitious return
that was due to survivorship bias in our database.
Does Your Strategy Use High and Low Data?
For almost all daily stock data, the high and low prices are far noisier
than the open and close prices. What this means is that even when
you had placed a buy limit order below the recorded high of a day, it
might not have been ﬁlled, and vice versa for a sell limit order. (This
could be due to the fact that a very small order was transacted at the
high, or the execution could have occurred on a market to which
your order was not routed. Sometimes, the high or low is simply
due to an incorrectly reported tick that was not ﬁltered out.) Hence,
a backtest that relies on high and low data is less reliable than one
that relies on the open and close.
Actually, sometimes even a market on open (MOO) or market
on close (MOC) order might not be ﬁlled at the historical open
and close prices shown in your data. This is due to the fact that
the historical prices shown may be due to the primary exchange
(e.g., New York Stock Exchange [NYSE]), or it may be a composite
price including all the regional exchanges. Depending on where your
order was routed, it may be ﬁlled at a different price from the historical opening or closing price shown in your dataset. Nevertheless, the discrepancies of the open and close prices usually have
less impact on backtest performance than the errors in the high
and low prices, since the latter almost always inﬂate your backtest
returns.
After retrieving the data from a database, it is often advisable to
do a quick error check. The simplest way to do this is to calculate
the daily returns based on the data. If you have open, high, low, and
close prices, you can calculate the various combinations of daily
returns such as from the previous high to today’s close as well. You
--- page 65 ---

Backtesting
43
can then examine closely those days with returns that are, say, 4
standard deviations away from the average. Typically, an extreme
return should be accompanied by a news announcement, or should
occur on a day when the market index also experienced extreme
returns. If not, then your data is suspect.
PERFORMANCE MEASUREMENT
Quantitative traders use a good variety of performance measures.
Which set of numbers to use is sometimes a matter of personal preference, but with ease of comparisons across different strategies and
traders in mind, I would argue that the Sharpe ratio and drawdowns
are the two most important. Notice that I did not include average annualized returns, the measure most commonly quoted by investors,
because if you use this measure, you have to tell people a number
of things about what denominator you use to calculate returns. For
example, in a long-short strategy, did you use just one side of capital
or both sides in the denominator? Is the return a leveraged one (the
denominator is based on account equity), or is it unleveraged (the
denominator is based on market value of the portfolio)? If the equity
or market value changes daily, do you use a moving average as the
denominator, or just the value at the end of each day or each month?
Most (but not all) of these problems associated with comparing returns can be avoided by quoting Sharpe ratio and drawdown instead
as the standard performance measures.
I introduced the concepts of the Sharpe ratio, maximum drawdown, and maximum drawdown duration in Chapter 2. Here, I will
just note a number of subtleties associated with calculating the
Sharpe ratio, and give some computational examples in both Excel
and MATLAB.
There is one subtlety that often confounds even seasoned portfolio managers when they calculate Sharpe ratios: should we or
shouldn’t we subtract the risk-free rate from the returns of a dollarneutral portfolio? The answer is no. A dollar-neutral portfolio is
--- page 66 ---

44
QUANTITATIVE TRADING
self-ﬁnancing, meaning the cash you get from selling short pays for
the purchase of the long securities, so the ﬁnancing cost (due to the
spread between the credit and debit interest rates) is small and can
be neglected for many backtesting purposes. Meanwhile, the margin balance you have to maintain earns a credit interest close to the
risk-free rate rF. So let’s say the strategy return (the portfolio return
minus the contribution from the credit interest) is R, and the riskfree rate is rF. Then the excess return used in calculating the Sharpe
ratio is R + rF – rF = R. So, essentially, you can ignore the risk-free
rate in the whole calculation and just focus on the returns due to
your stock positions.
Similarly, if you have a long-only day-trading strategy that does
not hold positions overnight, you again have no need to subtract the
risk-free rate from the strategy return in order to obtain the excess
returns, since you do not have ﬁnancing costs in this case, either. In
general, you need to subtract the risk-free rate from your strategy
returns in calculating the Sharpe ratio only if your strategy incurs
ﬁnancing cost.
To further facilitate comparison across strategies, most traders
annualize the Sharpe ratio. Most people know how to annualize the
average returns. For example, if you have been using monthly returns, then the average annual return is just 12 times the average
monthly return.
However, annualizing the standard deviation of returns is a bit
trickier. Here, based on the assumption that the monthly returns are
serially uncorrelated (Sharpe, 1994), the annual standard deviation
of returns is
√
12 times the monthly standard deviation. Hence, overall, the annualized Sharpe ratio would be
√
12 times the monthly
Sharpe ratio.
In general, if you calculate your average and standard deviation
of returns based on a certain trading period T, whether T is a month,
a day, or an hour, and you want to annualize these quantities, you
have to ﬁrst ﬁnd out how many such trading periods there are in a
year (call it NT). Then
Annualized Sharpe Ratio =

NT × Sharpe Ratio Based on T
--- page 67 ---

Backtesting
45
For example, if your strategy holds positions only during the NYSE
market hours (9:30–16:00 ET), and the average hourly returns is R,
and the standard deviation of the hourly returns is s, then the annualized Sharpe ratio is
√
1638 × R/s. This is because NT = (252 trading days) × (6.5 trading hours per trading day) = 1,638. (A common
mistake is to compute NT as 252 × 24 = 6,048.)
Example 3.4: Calculating Sharpe Ratio for Long-Only Versus
Market-Neutral Strategies
Let’s calculate the Sharpe ratio of a trivial long-only strategy for IGE: buying and holding a share since the close of November 26, 2001, and selling
it at close of November 14, 2007. Assume the average risk-free rate during this period is 4 percent per annum in this example. You can download
the daily prices from Yahoo! Finance, specifying the date range desired,
and store them as an Excel ﬁle (not the default comma-separated ﬁle),
which you can call IGE.xls. The next steps can be done in either Excel or
MATLAB:
Using Excel
1. The ﬁle should have columns A–G already from the download.
2. Sort all the columns in ascending order of Date (use the Data-Sort
function, choose the “Expand the selection” radio button, and choose
the “Ascending” as well as the “My data has Header row” radio
buttons).
3. In cell H3, type “=(G3-G2)/G2”. This is the daily return.
4. Double-clicking the little black dot at the lower right corner of the
cell H3 will populate the entire column H with daily returns of
IGE.
5. For clarity, you can type “Dailyret” in the header cell H1.
6. In cell I3, type “=H3-0.04/252”, which is the excess daily return, assuming a 4 percent per annum risk-free rate and 252 trading days in a
year.
7. Double-clicking the little black dot at the lower right corner of cell I3
will populate the entire column I with excess daily returns.
8. For clarity, type “Excess Dailyret” in the header cell I1.
--- page 68 ---

46
QUANTITATIVE TRADING
9. In
cell
I1506
(the
last
row
in
the
next
column),
type
“=SQRT(252)*AVERAGE(I3:I1505)/STDEV(I3:I1505)”.
10. The number displayed in cell I1505, which should be “0.789317538”,
is the Sharpe ratio of this buy-and-hold strategy.
The ﬁnished spreadsheet is available at my web site at epchan.com/
book/example3 4.xls.
Using MATLAB
% make sure previously defined variables are erased.
clear;
% read a spreadsheet named "IGE.xls" into MATLAB.
[num, txt]=xlsread(‘IGE’);
% the first column (starting from the second row)
% contains the trading days in format mm/dd/yyyy.
tday=txt(2:end, 1);
% convert the format into yyyymmdd.
tday=datestr(datenum(tday, ‘mm/dd/yyyy’), ‘yyyymmdd’);
% convert the date strings first into cell arrays and
% then into numeric format.
tday=str2double(cellstr(tday));
% the last column contains the adjusted close prices.
cls=num(:, end);
% sort tday into ascending order.
[tday sortIndex]=sort(tday, ‘ascend’);
% sort cls into ascending order of dates.
cls=cls(sortIndex);
% daily returns
dailyret=(cls(2:end)-cls(1:end-1))./cls(1:end-1);
% excess daily returns assuming risk-free rate of 4%
% per annum and 252 trading days in a year
excessRet=dailyret - 0.04/252;
% the output should be 0.7893
sharpeRatio=sqrt(252)*mean(excessRet)/std(excessRet)
This MATLAB code is also available for download at my web site
(epchan.com/book/example3 4.m).
Now let’s calculate the Sharpe ratio of a long-short market-neutral strategy. In fact, it is a very trivial twist of the buy-and-hold strategy above: at the
time we bought IGE, let’s suppose we just shorted an equal dollar amount
of Standard & Poor’s depositary receipts (SPY) as a hedge, and closed both
--- page 69 ---

Backtesting
47
positions at the same time in November 2007. You can also download SPY
from Yahoo! Finance and store it in a ﬁle SPY.xls. You can go through very
similar steps as above in both Excel and MATLAB, and I will leave it as an
exercise for the reader to perform the exact steps:
Using Excel
1. Sort the columns in SPY.xls in ascending order of date just like above.
2. Copy column G (Adj Close) in SPY.xls and paste it onto column J of
IGE.xls above.
3. Check that column J has the same number of rows as columns A–I. If
not, you have a diﬀerent set of dates—make sure you download the
matching date range from Yahoo!.
4. Perform the same steps as above to calculate the daily returns in column K.
5. For clarity, type “dailyretSPY” as the header in column K.
6. In column L, compute the net returns for the hedged strategy as the
diﬀerence between column H and K divided by 2. (Divide by 2 because
we now have twice the capital.)
7. In cell L1506, compute the Sharpe ratio of this hedged strategy. You
should get “0.783681”.
Using MATLAB
% Assume this is a continuation of the above MATLAB
%code.
% Insert your own code here to retrieve data from
% SPY.xls just as above.
% Name the array that contains the daily returns of
% SPY "dailyretSPY".
% net daily returns
(divide by 2 because we now have twice as much capital.)
netRet=(dailyret - dailyretSPY)/2;
% the output should be 0.7837.
sharpeRatio=sqrt(252)*mean(excessRet)/std(excessRet)
--- page 70 ---

48
QUANTITATIVE TRADING
Example 3.5: Calculating Maximum Drawdown and Maximum
Drawdown Duration
We shall continue the preceding long-short market-neutral example in order
to illustrate the calculation of maximum drawdown and maximum drawdown duration. The ﬁrst step in this calculation is to calculate the “high
watermark” at the close of each day, which is the maximum cumulative return of the strategy up to that time. (Using the cumulative return curve to
calculate high watermark and drawdown is equivalent to using the equity
curve, since equity is nothing more than initial investment times 1 plus the
cumulative return.) From the high watermark, we can calculate the drawdown, the maximum drawdown, and maximum drawdown duration.
Using Excel
1. In cell M3, type “=L3”.
2. In cell M4, type “=(1+M3)*(1+L4)-1”. This is the cumulative compounded return of the strategy up to that day. Populate the entire column M with the cumulative compounded returns of the strategy and
erase the last cell of the column. Name this column Cumret.
3. In cell N3, type “=M3”.
4. In cell N4, type “=MAX(N3, M4)”. This is the high watermark up to that
day. Populate the entire column N with the running high watermark of
the strategy and erase the last cell of the column. Name this column
High watermark.
5. In cell O3, type “=(1+N3)/(1+M3)-1”. This is the drawdown at that day’s
close. Populate the entire column O with the drawdowns of the strategy.
6. In cell O1506, type “=MAX(O3:O1505)”. This is the maximum drawdown of the strategy. It should have a value of about 0.1053, that is, a
maximum drawdown of 10.53 percent.
7. In cell P3, type “=IF(O3=0, 0, P2+1)”. This is the duration of the current
drawdown. Populate the entire column R with the drawdown durations
of the strategy and erase the last cell of the column.
8. In cell P1506, type “=MAX(P3:P1505)”. This is the maximum drawdown
duration of the strategy. It should have a value of 497, that is, a maximum drawdown duration of 497 trading days.
Using MATLAB
% Assume this is a continuation of the above MATLAB
% code.
% cumulative compounded returns
--- page 71 ---

Backtesting
49
cumret=cumprod(1+netRet)-1;plot(cumret);
[maxDrawdown maxDrawdownDuration]=...
calculateMaxDD(cumret);
[maxDrawdown maxDrawdownDuration]=...
calculateMaxDD(cumret);
% maximum drawdown. Output should be 0.1053
maxDrawdown
% maximum drawdown duration. Output should be 497.
maxDrawdownDuration
Notice the code fragment above calls a function “calculateMaxDrawdown,”
which I display below.
function [maxDD maxDDD]=calculateMaxDD(cumret)
% [maxDD maxDDD]=calculateMaxDD(cumret)
% calculation of maximum drawdown and maximum drawdown
% duration based on cumulative compounded returns.
% initialize high watermarks to zero.
highwatermark=zeros(size(cumret));
% initialize drawdowns to zero.
drawdown=zeros(size(cumret));
% initialize drawdown duration to zero.
drawdownduration=zeros(size(cumret));
for t=2:length(cumret)
highwatermark(t)=...
max(highwatermark(t-1), cumret(t));
% drawdown on each day
drawdown(t)=(1+highwatermark(t))/(1+cumret(t))-1;
if (drawdown(t)==0)
drawdownduration(t)=0;
else
drawdownduration(t)=drawdownduration(t-1)+1;
end
end
maxDD=max(drawdown); % maximum drawdown
% maximum drawdown duration
maxDDD=max(drawdownduration);
The ﬁle that contains this function is available as epchan.com/book/
calculateMaxDD.m. You can see where the maximum drawdown and
--- page 72 ---

50
QUANTITATIVE TRADING
maximum drawdown duration occurred in this plot of the cumulative returns in Figure 3.1.
0.6
0.5
0.4
0.3
0.2
0.1
0
0
200
400
600
800
1000
1200
1400
1600
Days
497 days max drawdown duration
10.53% max drawdown
−0.1
Cumulative Returns
FIGURE 3.1
Maximum
drawdown
and
maximum
drawdown
duration
for
Example 3.4
COMMON BACKTESTING PITFALLS
TO AVOID
Backtesting is the process of creating the historical trades given the
historical information available at that time, and then ﬁnding out
what the subsequent performance of those trades is. This process
seems easy given that the trades were made using a computer algorithm in our case, but there are numerous ways in which it can go
wrong. Usually, an erroneous backtest would produce a historical
performance that is better than what we would have obtained in actual trading. We have already seen how survivorship bias in the data
used for backtesting can result in inﬂated performance. There are,
