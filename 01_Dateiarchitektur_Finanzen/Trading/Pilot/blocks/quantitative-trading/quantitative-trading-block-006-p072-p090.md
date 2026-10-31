# Quantitative Trading_ How to Build Your Own Algorithmic -- Ernest P_ Chan -- Wiley Trading, 1, 2008 -- John Wiley & Sons, Ltd_ -- isbn13 9780470284889 -- e4d660df1c1a75e8676a28ff4f852fa7 -- Anna’s Archive.pdf — Chapter 3: Backtesting (pages 72–90)

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
--- page 73 ---

Backtesting
51
however, other common pitfalls related to how the backtest program is written, or more fundamentally, to how you construct your
trading strategy. I will describe two of the most common ones here,
with tips on how to avoid them.
Look-Ahead Bias
This error refers to the situation when you are using information
that was available only at a time ahead of the instant the trade was
made. For example, if your trade entry rule reads: “Buy when the
stock is within 1 percent of the day’s low,” you have introduced a
look-ahead bias in your strategy, because you could not possibly
have known what the day’s low was until the market closed that
day. Another example: Suppose a model involves a linear regression
ﬁt of two price series. If you use the regression coefﬁcients obtained
from the entire data set to determine your daily trading signals, you
have again introduced look-ahead bias.
How do we avoid look-ahead bias? Use lagged historical data
for calculating signals at every opportunity. Lagging a series of data
means that you calculate all the quantities like moving averages,
highs and lows, or even volume, based on data up to the close of the
previous trading period only. (Of course, you needn’t lag the data if
your strategy enters only at the close of the period.)
Look-ahead bias is easier to avoid using Excel or other WYSI-
WYG programs than using MATLAB. This is because it is easy to
align all the different columns of data in Excel and ensure that the
formula in each cell is computed based on the rows above the current row. It would be visually obvious when one is using current
day’s data in generating signals, given the cell-highlighting functionality in Excel. (Double-clicking a cell with a formula will highlight
the cells of data this formula utilizes.) With MATLAB, you have to
be more careful and remember to run a lag function on certain series used for signal generation.
Even with all the care and caution that goes into creating a
backtest program without look-ahead bias, sometimes we may
still let some of it slip in. Some look-ahead bias is quite subtle in
nature and not easy to avoid, especially if you are using MATLAB.
--- page 74 ---

52
QUANTITATIVE TRADING
It is best to do a ﬁnal checkup of your MATLAB backtest program
using this method: Run the program using all your historical data;
generate and save the resulting position ﬁle to ﬁle A (position ﬁle
is the ﬁle that contains all the recommended positions generated
by the program on each day). Now truncate your historical data so
that the most recent portion (say N days) is removed. So if the last
day in the original data is T, then the last day in the truncated data
should be T-N. N could be 10 days to 100 days. Now run the backtest program again using the truncated data and save the resulting
positions into a new ﬁle B. Truncate the most recent N rows of the
positions ﬁle A so that both A and B have the same number of rows
(days) in them, and the last day in both ﬁle A and B should be T-N.
Finally, check if A and B are identical in their positions. If not, you
have a look-ahead bias in your backtest program that you must ﬁnd
and correct, because the discrepancies in positions mean that you
are inadvertently using the truncated part of the historical data (the
part that lies ahead of day T-N) in determining the positions in ﬁle
A. I will illustrate this somewhat convoluted procedure at the end of
Example 3.6.
Data-Snooping Bias
In Chapter 2, I mentioned data-snooping bias—the danger that backtest performance is inﬂated relative to the future performance of
the strategy because we have overoptimized the parameters of the
model based on transient noise in the historical data. Data snooping bias is pervasive in the business of predictive statistical models
of historical data, but is especially serious in ﬁnance because of the
limited amount of independent data we have. High-frequency data,
while in abundant supply, is useful only for high-frequency models.
And while we have stock market data stretching back to the early
parts of the twentieth century, only data within the past 10 years
are really suitable for building predictive model. Furthermore, as
discussed in Chapter 2, regime shifts may render even data that are
just a few years old obsolete for backtesting purposes. The less independent data you have, the fewer adjustable parameters you should
employ in your trading model.
--- page 75 ---

Backtesting
53
As a rule of thumb, I would not employ more than ﬁve parameters, including quantities such as entry and exit thresholds, holding period, or the lookback period, in computing moving averages.
Furthermore, not all data-snooping bias is due to the optimization
of parameters. Numerous choices one makes in creating a trading model can be affected by repeated backtesting on the same
data set—decisions such as whether to enter at the open or close,
whether to hold the positions overnight, whether to trade large-cap
or mid-cap stocks. Often, these qualitative decisions are made to
optimize the backtest performance, but they may not be optimal going forward. It is almost impossible to completely eliminate datasnooping bias as long as we are building data-driven models. However, there are ways to mitigate the bias.
Sample Size
The most basic safeguard against data-snooping bias
is to ensure that you have a sufﬁcient amount of backtest data relative to the number of free parameters you want to optimize. As a
rule of thumb, let’s assume that the number of data points needed
for optimizing your parameters is equal to 252 times the number
of free parameters your model has. (This assumption of proportionality is not based on any survey of the vast statistical literature, but purely on experience.) So, for example, let’s assume you
have a daily trading model with three parameters. Then you should
have at least three years’ worth of backtest data with daily prices.
However, if you have a three-parameter trading model that updates
positions every minute, then you should have at least 252/390 year,
or about seven months, of one-minute backtest data. (Note that if
you have a daily trading model, then even if you have seven months
of minute-by-minute data points, effectively you only have about
7 × 21 = 147 data points, far from sufﬁcient for testing a threeparameter model.)
Out-of-Sample Testing
Divide your historical data into two parts.
Save the second (more recent) part of the data for out-of-sample
testing. When you build the model, optimize the parameters as well
as other qualitative decisions on the ﬁrst portion (called the training set), but test the resulting model on the second portion (called
--- page 76 ---

54
QUANTITATIVE TRADING
the test set). (The two portions should be roughly equal in size, but if
there is insufﬁcient training data, we should at least have one-third
as much test data as training data. The minimum size of the training
set is determined by the rule of thumb in the previous section.) Ideally, the set of optimal parameters and decisions for the ﬁrst part of
the backtest period is also the optimal set for the second period, but
things are rarely this perfect. The performance on the second part
of the data should at least be reasonable. Otherwise, the model has
data-snooping bias built into it, and one way to cure it is to simplify
the model and eliminate some parameters.
A more rigorous (albeit more computationally intensive)
method of out-of-sample testing is to use moving optimization of
the parameters. In this case, the parameters themselves are constantly adapting to the changing historical data, and data-snooping
bias with respect to parameters is eliminated. (See the sidebar on
parameterless trading models.)
P A R A M E T E R L E S S
T R A D I N G
M O D E L S *
A portfolio manager whom I used to work for liked to proudly proclaim that
his trading models have “no free parameters.” In keeping with the tradition of
secrecy in our industry, he would not divulge his technique further.
Lately, I have begun to understand what a trading model with no free parameters means. It doesn’t mean that it does not contain, for example, any
lookback period for calculating trends, or thresholds for entry or exit. I think
that would be impossible. It just means that all such parameters are dynamically optimized in a moving lookback window. This way, if you ask, “Does the
model have a ﬁxed proﬁt cap?,” the trader can honestly reply: “No, proﬁt cap is
not an input parameter. It is determined by the model itself.”
The advantage of a parameterless trading model is that it minimizes the
danger of overﬁtting the model to multiple input parameters (the so-called
“data-snooping bias”). So the backtest performance should be much closer to
the actual forward performance.
(Note that parameter optimization does not necessarily mean picking one
best set of parameters that give the best backtest performance. Often, it is
better to make a trading decision based on some kind of averages over diﬀerent
sets of parameters.)
Now, it is quite computationally challenging to optimize all these parameters just in time for your next order, but it is often even more diﬃcult to do that
in a backtest, given that a multidimensional optimization needs to be performed
--- page 77 ---

Backtesting
55
for each historical bar. As a result, I personally have seldom traded parameterless models, until I get to research my regime-switching model described in
Example 7.1. That model is almost parameterless (I left out a few parameters
from optimization because of a lack of time, not because of any technical dif-
ﬁculties). How was I able to perform backtest parameter optimization within a
few minutes in this case? I got to use a high-end backtesting platform (Alphacet
Discovery).
*This section was adapted from my blog article “Parameterless Trading Models,” which you
can ﬁnd at epchan.blogspot.com/2008/05/parameterless-trading-models.html.
The ultimate out-of-sample testing is familiar to many traders,
and it is called paper trading. Running the model on actual unseen
data is the most reliable way to test it (short of actually trading it).
Paper trading not only allows you to perform a truly honest outof-sample test; it often allows you to discover look-ahead errors in
your programs, as well as making you aware of various operational
issues. I will discuss paper trading in Chapter 5.
If the strategy that you are testing comes from a published
source, and you are just conducting a backtest to verify that the results are correct, then the entire period between the time of publication and the time that you tested the strategy is a genuine out-ofsample period. As long as you do not optimize the parameters of the
published model on the out-of-sample period, this period is as good
as paper trading the strategy.
Example 3.6: Pair Trading of GLD and GDX
This example will illustrate how to separate the data into a training set and a
test set. We will backtest a pair-trading strategy and optimize its parameters
on the training set and look at the eﬀect on the test set.
GLD versus GDX is a good candidate for pair trading because GLD
reﬂects the spot price of gold, and GDX is a basket of gold-mining
stocks. It makes intuitive sense that their prices should move in tandem.
I have discussed this pair of ETFs extensively on my blog in connection with cointegration analysis (see, e.g., epchan.blogspot.com/2006/11/
--- page 78 ---

56
QUANTITATIVE TRADING
reader-suggested-possible-trading.html). Here, however, I will defer until
Chapter 7 the cointegration analysis on the training set, which demonstrates that the spread formed by long GLD and short GDX is mean reverting. Instead, we will perform a regression analysis on the training set
to determine the hedge ratio between GLD and GDX, and then deﬁne entry
and exit thresholds for a pair-trading strategy. We will see how optimizing these thresholds on the training set changes the performance on the
test set. (This program is available as on epchan.com/book/example3 6.m.
The data ﬁles are available as GDX.xls and GLD.xls. This program uses
of a lag1 function will lag the time series by one time period. It is included at epchan.com/book as well. It also uses a function “ols” for linear regression, which is part of a free package downloaded from spatialeconometrics.com.)
Using MATLAB
% make sure previously defined variables are erased.
clear;
% read a spreadsheet named "GLD.xls" into MATLAB.
[num, txt]=xlsread(‘GLD’);
% the first column (starting from the second row) is
% the trading days in format mm/dd/yyyy.
tday1=txt(2:end, 1);
% convert the format into yyyymmdd.
tday1=...
datestr(datenum(tday1, ‘mm/dd/yyyy’), ‘yyyymmdd’);
% convert the date strings first into cell arrays and
% then into numeric format.
tday1=str2double(cellstr(tday1));
% the last column contains the adjusted close prices.
adjcls1=num(:, end);
% read a spreadsheet named "GDX.xls" into MATLAB.
[num, txt]=xlsread(‘GDX’);
% the first column (starting from the second row) is
% the trading days in format mm/dd/yyyy.
tday2=txt(2:end, 1);
% convert the format into yyyymmdd.
tday2=...
datestr(datenum(tday2, ‘mm/dd/yyyy’), ‘yyyymmdd’);
% convert the date strings first into cell arrays and
% then into numeric format.
tday2=str2double(cellstr(tday2));
--- page 79 ---

Backtesting
57
% the last column contains the adjusted close prices.
adjcls2=num(:, end);
% find the intersection of the two data sets,
% and sort them in ascending order
[tday, idx1, idx2]=intersect(tday1, tday2);
cl1=adjcls1(idx1);
cl2=adjcls2(idx2);
trainset=1:252; % define indices for training set
% define indices for test set
testset=trainset(end)+1:length(tday);
% determines the hedge ratio on the trainset
% use regression function
results=ols(cl1(trainset), cl2(trainset));
hedgeRatio=results.beta;
% spread = GLD - hedgeRatio*GDX
spread=cl1-hedgeRatio*cl2;
plot(spread(trainset));
figure;
plot(spread(testset));
figure;
% mean
of spread on trainset
spreadMean=mean(spread(trainset));
% standard deviation of spread on trainset
spreadStd=std(spread(trainset));
% z-score of spread
zscore=(spread - spreadMean)./spreadStd;
% buy spread when its value drops below 2 standard
deviations.
longs=zscore<=-2;
% short spread when its value rises above 2 standard
deviations.
shorts=zscore>=2;
% exit any spread position when its value is within 1
% standard deviation of its mean.
exits=abs(zscore)<=1;
% initialize positions array
positions=NaN(length(tday), 2);
--- page 80 ---

58
QUANTITATIVE TRADING
% long entries
positions(shorts, :)=...
repmat([-1 1], [length(find(shorts)) 1]);
% short entries
positions(longs,
:)=repmat([1 -1],
[length(find(longs)) 1]);
% exit positions
positions(exits,
:)=zeros(length(find(exits)), 2);
% ensure existing positions are carried forward
unless there is an exit signal positions=
fillMissingData(positions);
cl=[cl1 cl2]; % combine the 2 price series
dailyret=(cl - lag1(cl))./lag1(cl);
pnl=sum(lag1(positions).*dailyret, 2);
% the Sharpe ratio on the training set should be about 2.3
sharpeTrainset=...
sqrt(252)*mean(pnl(trainset(2:end))).
/std(pnl(trainset(2:end)))
% the Sharpe ratio on the test set should be about 1.5
sharpeTestset=sqrt(252)*mean(pnl(testset)).
/std(pnl(testset))
plot(cumsum(pnl(testset)));
% save positions file for checking look-ahead bias.
save example3 6 positions positions;
In ﬁle lag1.m:
function y=lag1(x)
% y=lag(x)
if (isnumeric(x))
% populate the first entry with NaN
y=[NaN(1,size(x,2));x(1:end-1, :)];elseif (ischar(x))
% populate the first entry with "
y=[repmat(",[1 size(x,2)]);x(1:end-1, :)];else
error(‘Can only be numeric or char array’);
end
So this pair-trading strategy has excellent Sharpe ratios on both the
training set and the test set. Therefore, this strategy can be considered free
of data-snooping bias. However, there may be room for improvement. Let’s
--- page 81 ---

Backtesting
59
see what happens if we change the entry thresholds to 1 standard deviation
and exit threshold to 0.5 standard deviation. In this case, the Sharpe ratio
on the training set increases to 2.9 and the Sharpe ratio on the test set
increases to 2.1. So, clearly, this set of thresholds is better.
Often, however, optimizing the parameters on the training set may decrease the performance on the test set. In this situation, you should choose
a set of parameters that result in good (but may not be the best) performance on both training and test sets.
I have not incorporated transaction costs (which I discuss in the next
section) into this analysis. You can try to add that as an exercise. Since this
strategy doesn’t trade very frequently, transaction costs do not have a big
impact on the resulting Sharpe ratio.
To see why this strategy works, just take a look at the Figure 7.4 of the
spread, which I will discuss in connection with stationarity and cointegration
in Chapter 7. You can see that the spread behaves in a highly mean-reverting
manner. Hence, buying low and selling high over and over again works well
here.
One last check, though, that we should perform before calling this a
success: We need to check for any look-ahead bias in the backtest program.
Add the following code fragment to the MATLAB code above after the line
“cl2=adjcls2(idx2);”
% number of most recent trading days to cut off
cutoff=60;% remove the last cutoff number of days.
tday(end-cutoff+1:end, :)=[];
cl1(end-cutoff+1:end, :)=[];
cl2(end-cutoff+1:end, :)=[];
Add the following code fragment to the very end of the previous
MATLAB program, replacing the line “save example3 6 positions positions”.
% step two of look-forward-bias check
oldoutput=load(‘example3 6 positions’);
oldoutput.positions(end-cutoff+1:end, :)=[];
if (any(positions∼=oldoutput.positions))
fprintf(1, ‘Program has look-forward-bias!\n’);
end
Save this new program into ﬁle “example3 6 1.m” and run it. You
will ﬁnd that the sentence “Program has look-forward-bias” is not printed
out—this indicates that our algorithm passed our test.
--- page 82 ---

60
QUANTITATIVE TRADING
Sensitivity Analysis
Once you have optimized your parameters
as well as various features of your model and have veriﬁed that its
performance on a test set is still reasonable, vary these parameters
or make some small qualitative changes in the features of the model
and see how the performance changes on both the training and the
test sets. If the drop is so drastic that any parameter set other than
the optimal one is unacceptable, the model most likely suffers from
data-snooping bias.
There are some variations on your model that are particularly
important to try: the various ways to simplify the model. Do you
really need, say, ﬁve different conditions to determine whether
to make that trade? What if you eliminate the conditions one
by one—at what point does the performance on the training set
deteriorate to an unacceptable level? And more important: Is there
a corresponding decrease in performance on the test set as you
eliminate the conditions? In general, you should eliminate as many
conditions, constraints, and parameters as possible as long as
there is no signiﬁcant decrease in performance in the test set, even
though it may decrease performance on the training set. (But you
should not add conditions and parameters, or adjust the parameter
values, so as to improve performance on the test set: If you do, you
have effectively used the test set as your training set and possibly
reintroduce data-snooping bias to your model.)
When one has reduced the set of parameters and conditions that
trigger a trade to the minimum, and after one has ascertained that
small variations in these parameters and conditions do not drastically alter the out-of-sample performance, one should consider dividing the trading capital across the different parameter values and
sets of conditions. This averaging over parameters will further help
ensure that the actual trading performance of the model will not deviate too much from the backtest result.
TRANSACTION COSTS
No backtest performance is realistic without incorporating transaction costs. I discussed the various types of transactions costs
--- page 83 ---

Backtesting
61
(commission, liquidity cost, opportunity cost, market impact, and
slippage) in Chapter 2 and have given examples of how to incorporate transaction costs into the backtest of a strategy. It should not
surprise you to ﬁnd that a strategy with a high Sharpe ratio before
adding transaction costs can become very unproﬁtable after adding
such costs. I will illustrate this in Example 3.7.
Example 3.7: A Simple Mean-Reverting Model with and
without Transaction Costs
Here is a simple mean-reverting model that is due to Amir Khandani and Andrew Lo at MIT (available at web.mit.edu/alo/www/Papers/
august07.pdf). This strategy is very simple: Buy the stocks with the worst
previous one-day returns, and short the ones with the best previous oneday returns. Despite its utter simplicity, this strategy has had great performance since 1995, ignoring transaction costs (it has a Sharpe ratio of 4.47
in 2006). Our objective here is to ﬁnd out what would happen to its performance in 2006 if we assume a standard 5-basis-point-per-trade transaction
cost. (A trade is deﬁned as a buy or a short, not a round-trip transaction.)
This example strategy not only allows us to illustrate the impact of transaction costs, it also illustrates the power of MATLAB in backtesting a model
that trades multiple securities—in other words, a typical statistical arbitrage
model. Backtesting a model with a large number of symbols over multiple
years is often too cumbersome to perform in Excel. But even assuming that
you have MATLAB at your disposal, there is still the question of how to retrieve historical data for hundreds of symbols, especially survivorship-biasfree data. Here, we will put aside the question of survivorship bias because
of the expensive nature of such data and just bear in mind that whatever
performance estimates we obtained are upper bounds on the actual performance of the strategy.
Whenever one wants to backtest a stock selection strategy, the ﬁrst
question is always: Which universe of stocks? The typical starting point is
the S&P 500 stock universe, which is the most liquid set of stocks available. The current list of stocks in the S&P 500 is available for download at
the Standard & Poor’s website (www.standardandpoors.com). Since the constituents of this universe change constantly, the list that you download will
be diﬀerent from mine. For ease of comparison, you can ﬁnd my list saved
as epchan.com/book/SP500 20071121.xls. The easiest way to download
historical data for all these stocks is to buy a copy of the HQuote Pro software (referenced earlier in this chapter, available from HQuote.com.) This
--- page 84 ---

62
QUANTITATIVE TRADING
software conveniently allows you to cut and paste any list of symbols for
which you want data. Run an update on your list in the software so as to retrieve the data from January 1, 2000, to the present day and then export this
data to a single text ﬁle called “Export.txt,” choosing only columns Date,
Open, High, Low, Close, and Volume, without header. Now, use the following MATLAB program (epchan.com/book/retrieveHQuoteHistoricalPrice.m)
to parse this data into a form useful for our computation, and which saves
it to a binary ﬁle “SPX 20071123.mat” on your local directory:
clear;
inputFile=‘Export.txt’;
outputFile=‘SPX 20071123’;
[mysym, mytday, myop, myhi, mylo, mycl, myvol]=...
textread(inputFile, ‘%s %u %f %f %f %f %u’, ...
‘delimiter’, ‘,’);
% Since the single file consists of many symbols,
% we need to find the unique set of symbols.
stocks=unique(mysym);
% Since the single file consists of many repeating set
% of dates for different symbols, we need to find the
% unique set of dates.
tday=unique(mytday);
op=NaN(length(tday), length(stocks));
hi=NaN(length(tday), length(stocks));
lo=NaN(length(tday), length(stocks));
cl=NaN(length(tday), length(stocks));
vol=NaN(length(tday), length(stocks));
for s=1:length(stocks)
stk=stocks{s};
% find the locations (indices) of the data with
% the current symbol.
idxA=strmatch(stk, mysym, ‘exact’);
% find the
locations (indices) of the data with
% the current set of dates.
[foo, idxtA, idxtB]=intersect(mytday(idxA), tday);
% Extract the set of prices for the current symbol
--- page 85 ---

Backtesting
63
% from the downloaded data.
op(idxtB, s)=myop(idxA(idxtA));
hi(idxtB, s)=myhi(idxA(idxtA));
lo(idxtB, s)=mylo(idxA(idxtA));
cl(idxtB, s)=mycl(idxA(idxtA));
vol(idxtB, s)=myvol(idxA(idxtA));
end
save(outputFile,
‘tday’, ‘stocks’, ‘op’, ‘hi’, ...
‘lo’, ‘cl’, ‘vol’);
Next, we can use this historical data set to backtest the mean-reverting
strategy without transaction cost:
clear;
startDate=20060101;
endDate=20061231;
load(‘SPX 20071123’, ‘tday’, ‘stocks’, ‘cl’);
% daily returns
dailyret=(cl-lag1(cl))./lag1(cl);
% equal weighted market index return
marketDailyret=smartmean(dailyret, 2);
% weight of a stock is proportional to the negative
% distance to the market index.
weights=...
-(dailyret-repmat(marketDailyret,[1 size(dailyret,2)]))./
repmat(smartsum(isfinite(cl), 2), ...
[1 size(dailyret, 2)]);
% those stocks that do not have valid prices or
% daily returns are excluded.
weights(∼isfinite(cl) | ∼isfinite(lag1(cl)))=0;
dailypnl=smartsum(lag1(weights).*dailyret, 2);
% remove pnl outside of our dates of interest
dailypnl(tday < startDate | tday > endDate) = [];
% Sharpe ratio should be about 0.25
sharpe=...
sqrt(252)*smartmean(dailypnl, 1)/smartstd(dailypnl, 1)
This ﬁle was saved as epchan.com/book/example3 7.m on my web
site. Notice that the Sharpe ratio in 2006 is only 0.25, not 4.47 as stated
by the original authors. The reason for this drastically lower performance
--- page 86 ---

64
QUANTITATIVE TRADING
is due to the use of the large market capitalization universe of S&P 500 in
our backtest. If you read the original paper by the authors, you will ﬁnd that
most of the returns are generated by small and microcap stocks.
In this MATLAB program, I have used three new functions: “smartsum,” “smartmean,” and “smartstd.” They are very similar to the usual
“sum,” “mean,” and “std” functions, except they skip all the NaN entries
in the data. These functions are very useful in backtesting because price
series for stocks often starts and stops. These ﬁles are all available at
epchan.com/book.
function y = smartsum(x, dim)
%y = smartsum(x, dim)
%Sum along dimension dim, ignoring NaN.
hasData=isfinite(x);
x(∼hasData)=0;
y=sum(x,dim);
y(all(∼hasData, dim))=NaN;
"smartmean.m"
function y = smartmean(x, dim)
% y = smartmean(x, dim)
% Mean value along dimension dim, ignoring NaN.
hasData=isfinite(x);
x(∼hasData)=0;
y=sum(x,dim)./sum(hasData, dim);
y(all(∼hasData, dim))=NaN; % set y to NaN if all entries are NaN’s.
"smartstd.m"
function y = smartstd(x, dim)
%y = smartstd(x, dim)
% std along dimension dim, ignoring NaN and Inf
hasData=isfinite(x);
x(∼hasData)=0;
y=std(x);
y(all(∼hasData, dim))=NaN;
Now, continuing with our backtest, let’s see what happens if we deduct
a 5-basis-point transaction cost for every trade.
% daily pnl with transaction costs deducted
onewaytcost=0.0005; % assume 5 basis points
--- page 87 ---

Backtesting
65
% remove weights outside of our dates of interest
weights(tday < startDate | tday > endDate, :) = [];
% transaction costs are only incurred when
% the weights change
dailypnlminustcost=...
dailypnl - smartsum(abs(weights-lag1(weights)), 2).*
onewaytcost;
% Sharpe ratio should be about -3.19
sharpeminustcost=...
sqrt(252)*smartmean(dailypnlminustcost, 1)/...
smartstd(dailypnlminustcost, 1)
The strategy is now very unproﬁtable!
STRATEGY REFINEMENT
If a strategy does not deliver superb backtest performance on ﬁrst
trial, there are some common ways to improve it. How to reﬁne a
strategy without introducing data-snooping bias and to remain simple with few parameters is more of an art than a science. The guiding principle is the same as that of parameter optimization: Whatever changes you make to the strategy to improve its performance
on the training set, it must also improve the performance on the
test set.
Often, there are some very simple strategies that are fairly well
known in traders’ circles and are still somewhat proﬁtable, though
their returns seem to be diminishing. An example is the pair trading of stocks. The reason they are diminishing in returns is that too
many traders are taking advantage of this arbitrage opportunity and
gradually erasing the proﬁt margin. However, it is often possible to
introduce minor variations in the basic strategy, which will boost its
returns.
These minor variations are often far less well known than the
basic strategy, and therefore far less well exploited by traders.
Sometimes they involve excluding certain stocks or groups of stocks
from the universe. For example, traders often prefer to exclude
--- page 88 ---

66
QUANTITATIVE TRADING
pharmaceutical stocks from their technical trading program because of the dramatic impact of news on their prices, or else they
may exclude stocks that have pending merger or acquisition deals.
Other traders change the entry and exit timing or frequency of the
trades. Yet another variation concerns the selection of the stock universe: We saw in Example 3.7 that a strategy that has a very good
Sharpe ratio when it is applied to small-cap stocks becomes very
unproﬁtable when applied to large-cap stocks.
When introducing these reﬁnements to your strategy, it is
preferable that the reﬁnement has some basis in fundamental economics or a well-studied market phenomenon, rather than some
arbitrary rule based on trial and error. Otherwise, data-snooping
bias looms.
Example 3.8: A Small Variation on an Existing Strategy
Let’s reﬁne the mean-reverting strategy described above in Example 3.7.
Recall that strategy has a mediocre Sharpe ratio of 0.25 and a very unprofitable Sharpe ratio of –3.19 after transaction costs in 2006. The only change
we will make here is to update the positions at the market open instead of
the close. In the MATLAB code, simply replace “cl” with “op” everywhere.
Lo and behold, the Sharpe ratio before costs increases to 4.43, and
after costs, it increases to a proﬁtable 0.78! I will leave it as an exercise for
the reader to improve the Sharpe ratio further by testing the strategy on
the S&P 400 mid-cap and S&P 600 small-cap universes.
SUMMARY
Backtesting is about conducting a realistic historical simulation of
the performance of a strategy. The hope is that the future performance of the strategy will resemble its past performance, though as
your investment manager will never tire of telling you, this is by no
means guaranteed!
There are many nuts and bolts involved in creating a realistic historical backtest and in reducing the divergence of the future
--- page 89 ---

Backtesting
67
performance of the strategy from its backtest performance. Issues
discussed here include:
r Data: Split/dividend adjustments, noise in daily high/low, and
survivorship bias.
r Performance measurement: Annualized Sharpe ratio and maximum drawdown.
r Look-ahead bias: Using unobtainable future information for past
trading decisions.
r Data-snooping bias: Using too many parameters to ﬁt historical
data, and avoiding it using large enough sample, out-of-sample
testing, and sensitivity analysis.
r Transaction cost: Impact of transaction costs on performance.
r Strategy reﬁnement: Common ways to make small variations on
the strategy to optimize performance.
After going through this chapter and working through some of
the examples and exercises, you should have gained some hands-on
experience in how to retrieve historical data and backtest a strategy
with either Excel or MATLAB.
When one starts testing a strategy, it may not be possible to
avoid all these pitfalls due to constraints of time and other resources. In this case, it is okay to skip a few precautions to achieve
a quick sense of whether the strategy has potential and is worthy of
closer examination. Sometimes, even the most thorough and careful
backtest cannot reveal problems that would be obvious after a few
months of paper or real trading. One can always revisit each of these
issues after the model has gone live.
Once you have backtested a strategy with reasonable performance, you are now ready to take the next step in setting up your
trading business.
--- page 90 ---
