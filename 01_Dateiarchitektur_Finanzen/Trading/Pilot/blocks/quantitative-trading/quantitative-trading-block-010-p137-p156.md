# Quantitative Trading_ How to Build Your Own Algorithmic -- Ernest P_ Chan -- Wiley Trading, 1, 2008 -- John Wiley & Sons, Ltd_ -- isbn13 9780470284889 -- e4d660df1c1a75e8676a28ff4f852fa7 -- Anna’s Archive.pdf — Chapter 7: Special Topics in Quantitative Trading (pages 137–156)

--- page 137 ---

C H A P T E R 7
Special Topics in
Quantitative
Trading
T
he ﬁrst six chapters of this book covered most of the basic knowledge needed to research, develop, and execute your
own quantitative strategy. This chapter explains important
themes in quantitative trading in more detail. These themes form the
bases of statistical arbitrage trading, and most quantitative traders
are conversant in some if not most of these topics. They are also
very helpful in informing our intuition about trading.
I will describe the two basic categories of trading strategies:
mean-reverting versus momentum strategies. Periods of meanreverting and trending behaviors are examples of what some traders
call regimes, and the switch between different regimes is a topic of
discussion here. Mean-reverting strategies derive their mathematical justiﬁcation from the concepts of stationarity and cointegration
of time series, which I will cover next. Then I will describe a theory that many hedge funds use to manage large portfolios and one
that has caused much turmoil in their performances: namely, factor
models. Other categories of strategies that traders frequently discuss are seasonal trading and high-frequency strategies. All trading
strategies require a way to exit their positions; I will describe the different logical ways to do this. Finally, I ponder the question of how
to best enhance the returns of a strategy: through higher leverage or
trading higher-beta stocks?
115
--- page 138 ---

116
QUANTITATIVE TRADING
MEAN-REVERTING VERSUS
MOMENTUM STRATEGIES
Trading strategies can be proﬁtable only if securities prices are
either mean-reverting or trending. Otherwise, they are randomwalking, and trading will be futile. If you believe that prices are mean
reverting and that they are currently low relative to some reference
price, you should buy now and plan to sell higher later. However, if
you believe the prices are trending and that they are currently low,
you should (short) sell now and plan to buy at an even lower price
later. The opposite is true if you believe prices are high.
Academic research has indicated that stock prices are on average very close to random walking. However, this does not mean
that under certain special conditions, they cannot exhibit some degree of mean reversion or trending behavior. Furthermore, at any
given time, stock prices can be both mean reverting and trending
depending on the time horizon you are interested in. Constructing a
trading strategy is essentially a matter of determining if the prices
under certain conditions and for a certain time horizon will be mean
reverting or trending, and what the initial reference price should be
at any given time. (When the prices are trending, they are also said
to have “momentum,” and thus the corresponding trading strategy
is often called a momentum strategy.)
Some people like to describe the phenomenon that prices can
be both mean reverting and trending at the same time as the “fractal” nature of stock prices. Technical analysts or chartists like to
use the so-called Elliott wave theory to analyze such phenomena.
Still others like to use the discipline of machine learning or artiﬁ-
cial intelligence (in particular, techniques such as hidden Markov
models, Kalman ﬁlter, neural networks, etc.) to discover whether
the prices are in a mean-reverting or trending “regime.” I personally have not found such general theories of mean reversion or momentum particularly useful. (See, however, the section on regime
switching, which describes an apparently successful attempt to predict regime switch for one particular stock.) Rather, I ﬁnd it is usually safe to assume that, unless the expected earnings of a company
--- page 139 ---

Special Topics in Quantitative Trading
117
have changed, stock prices will be mean reverting. In fact, ﬁnancial
researchers (Khandani and Lo, 2007) have constructed a very simple
short-term mean reversal model that is proﬁtable (before transaction costs) over many years. Of course, whether the mean reversion
is strong enough and consistent enough such that we can trade profitably after factoring in transaction costs is another matter, and it is
up to you, the trader, to ﬁnd those special circumstances when it is
strong and consistent.
Though mean reversion is quite prevalent, backtesting a profitable mean-reverting strategy can be quite perilous.
Many historical ﬁnancial databases contain errors in price
quotes. Any such error tends to artiﬁcially inﬂate the performance
of mean-reverting strategies. It is easy to see why: a mean-reverting
strategy will buy on a ﬁctitious quote that is much lower than some
moving average and sell on the next correct quote that is in line with
the moving average and thus makes a proﬁt. One must make sure the
data is thoroughly cleansed of such ﬁctitious quotes before one can
completely trust your backtesting performance on a mean-reverting
strategy.
Survivorship bias also affects the backtesting of mean-reverting
strategies disproportionately, as I discussed in Chapter 3. Stocks
that went through extreme price actions are likely to be either acquired (the prices went very high) or went bankrupt (the prices
went to zeros). A mean-reverting strategy will short the former and
buy the latter, losing money in both cases. However, these stocks
may not appear at all in your historical database if it has survivorship bias, thus artiﬁcially inﬂating your backtest performance. You
can look up Table 3.1 to ﬁnd out which database has survivorship bias.
Momentum
can
be
generated
by
the
slow
diffusion
of
information—as more people become aware of certain news, more
people decide to buy or sell a stock, thereby driving the price in
the same direction. I suggested earlier that stock prices may exhibit momentum when the expected earnings have changed. This
can happen when a company announces its quarterly earnings, and
investors either gradually become aware of this announcement or
--- page 140 ---

118
QUANTITATIVE TRADING
they react to this change by incrementally executing a large order (so as to minimize market impact). And indeed, this leads to
a momentum strategy called post earnings announcement drift, or
PEAD. (For a particularly useful article with lots of references on
this strategy, look up quantlogic.blogspot.com/2006/03/pocket-phdpost-earning-announcment.html.) Essentially, this strategy recommends that you buy a stock when its earnings exceed expectations,
and short a stock when it falls short. More generally, many news announcements have the potential of altering expectations of a stock’s
future earnings, and therefore have the potential to trigger a trending period. As to what kind of news will trigger this, and how long
the trending period will last, it is again up to you to ﬁnd out.
Besides the slow diffusion of information, momentum can be
caused by the incremental execution of a large order due to the liquidity needs or private investment decisions of a large investor.
This cause probably accounts for more instances of short-term momentum than any other causes. With the advent of increasingly sophisticated execution algorithms adopted by the large brokerages, it
is, however, increasingly difﬁcult to ascertain whether a large order
is behind the observed momentum.
Momentum can also be generated by the herdlike behavior of investors: investors interpret the (possibly random and meaningless)
buying or selling decisions of others as the sole justiﬁcations of their
own trading decisions. As Yale economist Robert Schiller said in the
New York Times (Schiller, 2008), nobody has all the information
they need in order to make a fully informed ﬁnancial decision. One
has to rely on the judgment of others. There is, however, no sure
way to discern the quality of the judgment of others. More problematically, people make their ﬁnancial decisions at different times, not
meeting at a town hall and reaching a consensus once and for all.
The ﬁrst person who paid a high price for a house is “informing”
the others that houses are good investments, which leads another
person to make the same decision, and so on. Thus, a possibly erroneous decision by the ﬁrst buyer is propagated as “information” to a
herd of others.
Unfortunately, momentum regimes generated by these two
causes (private liquidity needs and herdlike behavior) have highly
--- page 141 ---

Special Topics in Quantitative Trading
119
unpredictable time horizons. How could you know how big an order an institution needs to execute incrementally? How do you predict when the “herd” is large enough to form a stampede? Where is
the infamous tipping point? If we do not have a reliable way to estimate these time horizons, we cannot execute a momentum trade
proﬁtably based on these phenomena. In a later section on regime
switch, I will examine some attempts to predict these tipping or
“turning” points.
There is one last contrast between mean-reverting and momentum strategies that is worth pondering. What are the effects
of increasing competition from traders with the same strategies?
For mean-reverting strategies, the effect typically is the gradual
elimination of any arbitrage opportunity, and thus gradually diminishing returns down to zero. When the number of arbitrage opportunities has been reduced to almost zero, the mean-reverting
strategy is subject to the risk that an increasing percentage of
trading signals are actually due to fundamental changes in stocks’
valuation and thus is not going to mean revert. For momentum
strategies, the effect of competition is often the diminishing of the
time horizon over which the trend will continue. As news disseminates at a faster rate and as more traders take advantage of this
trend earlier on, the equilibrium price will be reached sooner. Any
trade entered after this equilibrium price is reached will be unprofitable.
REGIME SWITCHING*
The concept of regimes is most basic to ﬁnancial markets. What
else are “bull” and “bear” markets if not regimes? The desire to predict regime switches, which are also commonly known as turning
points, is also as old as ﬁnancial markets themselves.
If our attempts to predict the switching from a bull to a
bear market were even slightly successful, we could focus our
*This section was adapted from an article I published in Automated Trader
magazine.
--- page 142 ---

120
QUANTITATIVE TRADING
discussion to this one type of switching and call it a day. If only
it were that easy. The difﬁculty with predicting this type of switching encourages researchers to look more broadly at other types of
regime switching in the ﬁnancial markets, hoping to ﬁnd some that
may be more amenable to existing statistical tools.
I have already described two regime switches (or “shifts,” for
these two examples did not switch back to their former regimes)
that are due to changes in market and regulatory structures: decimalization of stock prices in 2003 and the elimination of the shortsale plus-tick rule in 2007. (See Chapter 5 for details.) These regime
shifts are preannounced by the government, so no predictions of
the shifts are necessary, though few people can predict the exact
consequences of the regulatory changes.
Some of the other most common ﬁnancial or economic regimes
studied are inﬂationary vs. recessionary regimes, highvs. lowvolatility regimes, and mean-reverting vs. trending regimes. Among
these, volatility regime switching seems to be most amenable to
classical econometric tools such as the generalized autoregressive conditional heteroskedasticity (GARCH) model (See Klaassen,
2002). That is not surprising, as there is a long history of success
among ﬁnancial economists in modeling volatilities as opposed to
the underlying stock prices themselves. While such predictions of
volatility regime switches can be of great value to options traders,
they are unfortunately of no help to stock traders.
Academic attempts to model regime switches in stock prices
generally proceed along these lines:
1. Propose that the two (or more) regimes are characterized by
different probability distributions of the prices. In the simplest
cases, the log of the prices of both regimes may be represented
by normal distributions, except that they have different means
and/or standard deviations.
2. Assume that there is some kind of transition probability among
the regimes.
3. Determine the exact parameters that specify the regime probability distributions and the transition probabilities by ﬁtting the
--- page 143 ---

Special Topics in Quantitative Trading
121
model to past prices, using standard statistical methods such as
maximum likelihood estimation.
4. Based on the ﬁtted model above, ﬁnd out the expected regime
of the next time step and, more importantly, the expected stock
price.
This type of approach is usually called Markov regime switching or hidden Markov models, and it is generally based on a
Bayesian probabilistic framework. Readers who are interested in
reading more about some of these approaches may peruse Nielsen
and Olesen (2000), van Norden and Schaller (1993), or Kaufmann
and Scheicher (1996).
Despite the elegant theoretical framework, such Markov regimeswitching models are generally useless for actual trading purposes.
The reason for this weakness is that they assume constant transition probabilities among regimes at all times. In practice, this
means that at any time (as illustrated by the Nielsen and Olesen paper), there is always a very small probability for the stock to transition from a normal, quiescent regime to a volatile regime. But this
is useless to traders who want to know when—and under what precise conditions—the transition probability will suddenly peak. This
question is tackled by the turning points models.
Turning points models take a data mining approach (Chai, 2007):
Enter all possible variables that might predict a turning point or
regime switch. Variables such as current volatility; last-period return; or changes in macroeconomic numbers such as consumer con-
ﬁdence, oil price changes, bond price changes, and so on can all
be part of this input. In fact, in a very topical article about turning
points in the real estate market by economist Robert Schiller (2007),
it was suggested that the crescendo of media chatter about impending boom or bust may actually be a good predictor of a coming turning point.
In Example 7.1, I illustrate how we might detect turning points
using a data-mining approach with just simple technical indicators
built on stock price series as inputs while using stock returns of
multiple holding periods as outputs.
--- page 144 ---

122
QUANTITATIVE TRADING
Example 7.1: Using a Machine Learning Tool to Proﬁt from
Regime Switching in the Stock Market
As I discussed in the main text, I believe that regime switching can be most
easily discovered by using a data-mining approach: examining a massive
number of indicators to see which one might predict a switch. This is normally a very onerous task, even with MATLAB. But, luckily, a recent machine
learning program has enabled this discovery process to be done in a matter
of hours.
I shall employ a tool here called Alphacet Discovery, which is an integrated backtesting and execution platform recently launched by Alphacet,
Inc. (www.alphacet.com. Full disclosure: Alphacet is a client of my ﬁrm.)
This platform not only integrates all historical and real-time data needed
for rapid strategy prototyping, backtesting, analysis, and real-time deployment; it also contains an expanding array of machine learning programs
such as neural networks and genetic algorithms that are well suited to data
mining for the kind of relationships we are seeking.
I will pick a prominent brokerage stock—GS—as a proxy for the ﬁnancial sector. My objective is to ﬁnd out if I can detect turning points in this
sector where it goes from bull to bear and back. My initial hypothesis is that
major shifts of interest rates, a release of government macroeconomic data,
or earnings announcements are likely triggers of turning points. At the time
of this writing, Alphacet had not yet completed integration of macroeconomic or company news data into its database, so I will use a large percent
change in GS as proxy for such news releases. Furthermore, I believe that
whenever GS reaches an N-day high or low just before this large drop or
rise in prices occurs is a good signal that a previous regime is close to an
end. So I shall use this condition as an additional input as well.
The search problem we face is: How large a percent change is suﬃcient
to trigger a regime switch? What should N be in the N-day high/low condition? And how long does the new regime generally last? (In other words,
what is the optimal holding period?) To answer these questions in the oldfashioned, manual way is very time consuming, as one has to run multiple simulations with diﬀerent thresholds for the independent variables and
multiple return horizons for the dependent variables. Let’s see if Alphacet
Discovery can help us automate this process.
The independent variables of the model are just the one-day returns
of GS. The dependent variables are the future returns of GS within various
holding periods. Discovery can easily ﬁnd an optimal rule, or an optimal
combination of rules, which will lead to the best backtest performance. In
our case, each percent-change threshold can be encapsulated as a rule. I
entered two thresholds for buys and two for shorts: −1 percent, −3 percent,
--- page 145 ---

Special Topics in Quantitative Trading
123
1 percent, and 3 percent. Similarly, each holding period can be encapsulated
as a rule, too, and I entered six such periods: 1, 5, 10, 20, 40, and 60 days.
To prepare the price, percent-change, and 10-day high/low time series
for this search is very easy: most things can be done by drag and drop,
using a mouse, in Discovery. (For simplicity, I ﬁx N to 10 for the strategy
here, but this parameter can be optimized as well.) I just dragged a GS
price series into the strategy editor and speciﬁed a 1-day frequency with
the available controls. (The price series started around December 2006.)
See box S1 in Figure 7.1. Then I dragged several prepackaged “Rules” that
compute the 1-day percent change, and simple 10-day moving highs and
lows of a series to the strategy editor (box I2 in Figure 7.1.). And I feed
the original price series into the Program Group box by directing an arrow
from the Symbol Group box to the Program Group box.
FIGURE 7.1
Strategy Editor Showing Data and Rules Represented by Boxes
Now I can create the entry rules by using the drop-down menus and
typing into the textboxes inside a new Rule box’s editor. Figure 7.2 shows
what’s inside Rule box R3 for the buy-and-sell rule based on a change of
±1 percent. I have created a similar Rule box for ±3 percent. Note that,
by default, subsequent entry signals will override positions established by
previous signals.
--- page 146 ---

124
QUANTITATIVE TRADING
R3
BuySellAt0.1After10DayLowHigh
IF
–
IF
12-Percent-Change.3.0 >= 1
12-Percent-Change.3.0 >= −1
12-Moving-Low-10.2.0 >= TALT.NYSE.ESXXXX.GS.Last.Low
12-Moving-High-10.1.0 <= TALT.NYSE.ESXXXX.GS.Last.High
AND
AND
THEN
THEN
ELSE
1
−1
FIGURE 7.2
Inside a Rule Box
We can specify the holding periods using the prepackaged program
called “Holding Period” with diﬀerent parameters. (In fact, you can easily
create such programs yourself if you know the programming language Lisp.)
These are all encapsulated in the box I5 (and I6 for the ±2 percent rule
separately). We feed the output of the boxes R3 to I5 by drawing an arrow,
and similarly R4 to I9.
Finally, we run a perceptron learning algorithm on the outputs of I7 and
I9 (a perceptron is a type of neural network). This algorithm will ﬁnd out the
best weights for the diﬀerent rules with diﬀerent holding periods (among
other parameters) based on a moving window of historical training data
with the objective of maximizing the total proﬁt in this window. Based on
these optimized weights, the perceptron will trigger a buy-and-sell decision
at the end of each period. (Examples of other algorithms that you can select
are genetic algorithm and a K-nearest-neighbor clustering technique.)
Interestingly, the perceptron will not force us to hold a position for
exactly N days, even though that was what the component rule was constructed to do so in the moving window. Every day, the strategy will decide
whether to buy, sell, or do nothing, based on the latest parameter optimization using the latest data in the moving window and the resulting linearly
weighted decisions from the diﬀerent rules.
--- page 147 ---

Special Topics in Quantitative Trading
125
Now we are ready to look at the performance results of this strategy.
We can bring up Discovery’s charting application for this. In Figure 7.3, I
have shown three of the best equity curves that come from the perceptron
optimization. The best curve belongs to a model using a 50-day moving
window for the optimization. (The length of the moving window can itself
be an object of optimization, but we will skip that step here.) On the sidebar of the charting application, we can see that this strategy has a 37.93
percent gross cumulative return over a six-month backtest period, with 89
round-trip trades. (This is to be compared with a 15.77 percent return of a
buy-and-hold strategy on GS, with a 14 percent drawdown.) We have also
shown the best equity curve from the various holding period routines to
quantify the improvement from optimization (holding period of 10 days in
I5 on the 1 percent rule at R3), which has a gross cumulative return of 18.55
percent over the period.
Though the backtest period is short, this return looks very impressive.
Can something be wrong? In particular, what about the much-feared datasnooping bias that seems to creep into every strategy that is based on machine learning or artiﬁcial intelligence? The basic philosophy of Alphacet
FIGURE 7.3
Charting Application Showing Equity Curves and Performance
Statistics in the Sidebar
--- page 148 ---

126
QUANTITATIVE TRADING
Discovery is to prevent this kind of bias from happening. In theory, though
not in our particular illustration here, optimization over all rules and all
parameters can be done in a backward-looking moving window, so that we
are using absolutely no unseen future data for the backtest. Of course, datasnooping bias can still creep in because we can abandon a whole category
of models when the performance is poor and try one new category after
another until it improves. But then, this is unavoidable whenever we are in
the business of backtesting.
One should also note that the parameters that the search engine is
allowed to optimize over in this case are actually quite limited: They are
just the diﬀerent holding periods. This further reduces the danger of datasnooping bias.
Since the backtest looks good, I can immediately press a single button
and have this strategy run against real-time data and generate orders in
either a paper or a real trading account.
As you can see, it may not be hard to create a regime-switching model
with the simplest of technical indicators as long as one is able to eﬃ-
ciently optimize over a large number of parameters, conducted strictly
in a backward-looking moving window. (See my sidebar on “Parameterless Trading Models” in Chapter 3.) The performance may even be better if we can conﬁrm the price moves with macroeconomic or companyspeciﬁc news. I believe that this same technique can be applied proﬁtably
to many exchange-traded funds (ETFs), futures, or even currency trading
as well.
I would like to thank Rosario Ingargiola, chief technology oﬃcer of Alphacet, Inc., for
his help in using Alphacet Discovery to develop the strategy shown here.
STATIONARITY AND COINTEGRATION
A time series is “stationary” if it never drifts farther and farther away
from its initial value. In technical terms, stationary time series are
“integrated of order zero,” or I(0). (See Alexander, 2001.) It is obvious that if the price series of a security is stationary, it would be a
great candidate for a mean-reversion strategy. Unfortunately, most
stock price series are not stationary—they exhibit a geometric random walk that gets them farther and farther away from their starting (i.e., initial public offering) values. However, you can often ﬁnd
--- page 149 ---

Special Topics in Quantitative Trading
127
a pair of stocks such that if you long one and short the other, the
market value of the pair is stationary. If this is the case, then the
two individual time series are said to be cointegrated. They are so
described because a linear combination of them is integrated of order zero. Typically, two stocks that form a cointegrating pair are
from the same industry group. Traders have long been familiar with
this so-called pair-trading strategy. They buy the pair portfolio when
the spread of the stock prices formed by these pairs is low, and
sell/short the pair when the spread is high—in other words, a classic
mean-reverting strategy.
An example of a pair of cointegrating price series is the gold
ETF GLD versus the gold miners ETF, GDX, which I discussed
in Example 3.6. If we form a portfolio with long 1 share of GLD
and short 1.6766 share of GDX, the prices of the portfolio form a
stationary time series (see Figure 7.4). The exact number of shares
of GLD and GDX can be determined by a regression ﬁt of the two
component time series (see Example 7.2).
Spread between GLD and GDX
Long 1 share of GLD
Short 1.6766 share of GDX
10
8
6
4
2
Spread (in $)
−2
−4
−6
0
Date
20060523
20061012
20070309
20070801
20071221
FIGURE 7.4
A Stationary Time Series Formed by the Spread between GLD and
GDX
--- page 150 ---

128
QUANTITATIVE TRADING
Example 7.2: How to Form a Good Cointegrating
(and Mean-Reverting) Pair of Stocks
As I explained in the main text, if you long one security and short
another one in the same industry group and in the right proportion,
sometimes the combination (or “spread”) becomes a stationary series.
A stationary series is an excellent candidate for a mean-reverting strategy. This example teaches you how to use a free MATLAB package
downloadable at www.spatial-econometrics.com to determine if two price
series are cointegrated and, if so, how to ﬁnd the optimal “hedge ratio” (i.e.,
the number of shares of the second security versus one share of the ﬁrst
security).
The main method used to test for cointegration is called the cointegrating augmented Dickey-Fuller test, hence the function name cadf. A detailed
description of this method can be found in the manual also available on the
same web site mentioned earlier.
The following program is available online as epchan.com/book/ example7 2.m:
% make sure previously defined variables are erased.
clear;
% read a spreadsheet named "GLD.xls" into MATLAB.
[num, txt]=xlsread(’GLD’);
% the first column (starting from the second row) is
% the trading days in format mm/dd/yyyy.
tday1=txt(2:end, 1);
% convert the format into yyyymmdd.
tday1=..
datestr(datenum(tday1, ’mm/dd/yyyy’), ’yyyymmdd’);
% convert the date strings first into cell arrays and
% then into numeric format.
tday1=str2double(cellstr(tday1));
% the last column contains the adjusted close prices.
adjcls1=num(:, end);
% read a spreadsheet named "GDX.xls" into MATLAB.
[num2, txt2]=xlsread(’GDX’);
% the first column (starting from the second row) is
% the trading days in format mm/dd/yyyy.
tday2=txt2(2:end, 1);
% convert the format into yyyymmdd.
tday2=..
datestr(datenum(tday2, ’mm/dd/yyyy’), ’yyyymmdd’);
--- page 151 ---

Special Topics in Quantitative Trading
129
% convert the date strings first into cell arrays and
% then into numeric format.
tday2=str2double(cellstr(tday2));
adjcls2=num2(:, end);
% find all the days when either GLD or GDX has data.
tday=union(tday1, tday2);
[foo idx idx1]=intersect(tday, tday1);
% combining the two price series
adjcls=NaN(length(tday), 2);
adjcls(idx, 1)=adjcls1(idx1);
[foo idx idx2]=intersect(tday, tday2);
adjcls(idx, 2)=adjcls2(idx2);
% days where any one price is missing
baddata=find(any(˜isfinite(adjcls), 2));
tday(baddata)=[];
adjcls(baddata,:)=[];
vnames=strvcat(’GLD’, ’GDX’);
% run cointegration check using
% augmented Dickey-Fuller test
res=cadf(adjcls(:, 1), adjcls(:, 2), 0, 1);
prt(res, vnames);
% Output from cadf function:
%
Augmented DF test for co-integration variables:
GLD,GDX
% CADF t-statistic
# of lags
AR(1) estimate
%
-3.35698533
1
-0.060892
%
%
1% Crit Value
5% Crit Value
10% Crit Value
%
-3.819
-3.343
-3.042
% The t-statistic of -3.36 which is in between the
% 1% Crit Value of -3.819
% and the 5% Crit Value of -3.343 means that
% there is a better than 95%
% probability that these 2 time series are
% cointegrated.
--- page 152 ---

130
QUANTITATIVE TRADING
results=ols(adjcls(:, 1), adjcls(:, 2));
hedgeRatio=results.beta
z=results.resid;
% A hedgeRatio of 1.6766 was found.
% I.e. GLD=1.6766*GDX + z, where z can be
% interpreted as the
% spread GLD-1.6766*GDX and should be stationary.
% This should produce a chart similar to Figure 7.4.
plot(z);
In case you think that any two stocks in the same industry group
would be cointegrating, here is a counterexample: KO (Coca-Cola)
versus PEP (Pepsi). The same cointegration test as used in Example
7.1 tells us that there is a less than 90 percent probability that they
are cointegrated. (You should try it yourself and then compare with
my program epchan.com/book/example7 3.m.) If you use linear regression to ﬁnd the best ﬁt between KO and PEP, the plot of the time
series will resemble Figure 7.5.
50
40
30
20
10
0
−10
−20
−30
Long 1 share of KO
Short 1.01 share of PEP
Spread (in $)
Date
19770103
19841128
19921027
20000927
FIGURE 7.5
A Nonstationary Time Series Formed by the Spread between KO and
PEP
--- page 153 ---

Special Topics in Quantitative Trading
131
If a price series (of a stock, a pair of stocks, or, in general, a portfolio of stocks) is stationary, then a mean-reverting strategy is guaranteed to be proﬁtable, as long as the stationarity persists into the
future (which is by no means guaranteed). However, the converse is
not true. You don’t necessarily need a stationary price series in order
to have a successful mean-reverting strategy. Even a nonstationary
price series can have many short-term reversal opportunities that
one can exploit, as many traders have discovered.
Many pair traders are unfamiliar with the concepts of stationarity and cointegration. But most of them are familiar with correlation, which superﬁcially seems to mean the same thing as cointegration. Actually, they are quite different. Correlation between two
price series actually refers to the correlations of their returns over
some time horizon (for concreteness, let’s say a day). If two stocks
are positively correlated, there is a good chance that their prices
will move in the same direction most days. However, having a positive correlation does not say anything about the long-term behavior
of the two stocks. In particular, it doesn’t guarantee that the stock
prices will not grow farther and farther apart in the long run even
if they do move in the same direction most days. However, if two
stocks were cointegrated and remain so in the future, their prices
(weighted appropriately) will be unlikely to diverge. Yet their daily
(or weekly, or any other time horizon) returns may be quite uncorrelated.
As an artiﬁcial example of two stocks, A and B, that are cointegrated but not correlated, see Figure 7.6. Stock B clearly doesn’t
move in any correlated fashion with stock A: Some days they move
in the same direction, other days the opposite. Most days, stock B
doesn’t move at all. But notice that the spread in stock prices between A and B always returns to about $1 after a while.
Can we ﬁnd real-life example of this phenomenon? Well, KO
versus PEP is one. In the program example7 3.m I have shown
that they do not cointegrate. If, however, you test their daily returns for correlation, you will ﬁnd that their correlation of 0.4849
is indeed statistically signiﬁcant. The correlation test is presented
at the end of the example7 3.m program and shown here in
Example 7.3.
--- page 154 ---

132
QUANTITATIVE TRADING
Stock A
Stock B
73
72
71
70
69
68
Daily Prices
67
66
65
64
63
0
5
10
15
20
Days
25
30
35
40
45
FIGURE 7.6
Cointegration Is Not Correlation. Stocks A and B are cointegrated but
not correlated
Example 7.3: Testing the Cointegration versus Correlation
Properties between KO and PEP
The cointegration test for KO and PEP is the same as that for GDX and
GLD in Example 7.2, so it won’t be repeated here. (It is available from
epchan.com/book/example7 3.m) The cointegration result shows that the
t-statistic for the augmented Dicky-Fuller test is −2.14, larger than the 10
percent critical value of −3.038, meaning that there is a less than 90 percent
probability that these two time series are cointegrated.
The following code fragment, however, tests for correlation between
the two time series:
% A test for correlation.
dailyReturns=(adjcls-lag1(adjcls))./lag1(adjcls);
[R,P]=corrcoef(dailyReturns(2:end,:));
% R =
%
%
1.0000
0.4849
%
0.4849
1.0000
--- page 155 ---

Special Topics in Quantitative Trading
133
%
%
% P =
%
%
1
0
%
0
1
% The P value of 0 indicates that the two time series
% are significantly correlated.
Stationarity is not limited to the spread between stocks: it can
also be found in certain currency rates. For example, the Canadian dollar/Australian dollar (CAD/AUD) cross-currency rate is quite
stationary, both being commodities currencies. Numerous pairs of
futures as well as well as ﬁxed-income instruments can be found
to be cointegrating as well. (The simplest examples of cointegrating futures pairs are calendar spreads: long and short futures contracts of the same underlying commodity but different expiration
months. Similarly for ﬁxed-income instruments, one can long and
short bonds by the same issuer but of different maturities.)
FACTOR MODELS
Financial commentators often say something like this: “The current
market favors value stocks,” “The market is focusing on earnings
growth,” or “Investors are paying attention to inﬂation numbers.”
How do we quantify these and other common drivers of returns?
There is a well-known framework in quantitative ﬁnance called
factor models (also known as arbitrage pricing theory [APT]) that
attempts to capture the different drivers of returns such as earnings
growth rates, interest rate, or the market capitalization of a company. These drivers are called factors. Mathematically, we can write
the excess returns (returns minus risk-free rate) R of N stocks as
R = Xb + u
--- page 156 ---

134
QUANTITATIVE TRADING
where X is an N × N matrix of factor exposures (also known as
factor loadings), b is an N vector of factor returns, and u an N vector
of speciﬁc returns. (Every one of these quantities is time dependent,
but I suppress this explicit dependence for simplicity.)
The terms factor exposure, factor return, and speciﬁc return
are commonly used in quantitative ﬁnance, and it is well worth our
effort to understand their meanings. Factor returns are the common drivers of stock returns, and are therefore independent of a
particular stock. Factor exposures are the sensitivities to each of
these common drivers. Any part of a stock’s return that cannot be
explained by these common factor returns is deemed a speciﬁc return (i.e., speciﬁc to a stock and essentially regarded as just random
noise within the APT framework). Each stock’s speciﬁc return is assumed to be uncorrelated to another stock’s.
Let’s illustrate these using a simple factor model called the
Fama-French Three-Factor model (Fama and French, 1992). This
model postulates that the excess return of a stock depends linearly
on only three factor exposures: its beta (i.e., its sensitivity to the
market index), its market capitalization, and its book-to-price ratio.
These factor exposures are obviously different for each stock and
for each time period. (Factor exposures are often normalized such
that the average of the factor exposures within a universe of stocks
is zero, and the standard deviation is 1.)
Now that we know how to calculate the factor exposures, what
about the factor returns and speciﬁc returns? We cannot directly
compute the factor returns and speciﬁc returns—we have to infer
their values by running a multivariate linear regression of the excess
returns of stocks against the factor exposures. Note that each stock
represents one data point in this linear regression, and we have to
either run a separate linear regression for each time period or, if
we want an average value over many time periods, aggregate the
values from all these time periods into one training set and run one
regression against them all.
If you perform this linear regression ﬁt over many time periods for the Fama-French Three-Factor model, you will ﬁnd that
the market capitalization factor return is usually negative (meaning
