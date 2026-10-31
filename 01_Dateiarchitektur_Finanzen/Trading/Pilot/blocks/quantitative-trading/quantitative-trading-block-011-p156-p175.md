# Quantitative Trading_ How to Build Your Own Algorithmic -- Ernest P_ Chan -- Wiley Trading, 1, 2008 -- John Wiley & Sons, Ltd_ -- isbn13 9780470284889 -- e4d660df1c1a75e8676a28ff4f852fa7 -- Anna’s Archive.pdf — Chapter 7: Special Topics in Quantitative Trading (pages 156–175)

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
--- page 157 ---

Special Topics in Quantitative Trading
135
that small-cap stocks usually outperform large-cap stocks), and the
book-to-price ratio factor return is usually positive (meaning value
stocks usually outperform growth stocks). And since most stocks
are positively correlated with the market index, the beta factor return is positive as well.
The Fama-French model has no monopoly on the choice of
factors. In fact, you can construct as many factors as creativity
and rationality allow. For example, you can choose return on equity as a factor exposure, or the correlation of the stock return
with the prime rate as another. You can choose any number of
other economic, fundamental, or technical factors. Whether the
factor exposures you have chosen are sensible or not will determine whether the factor model explains the excess returns of the
stocks adequately. If the factor exposures (and consequently the
model as a whole) are poorly chosen, the linear regression ﬁt will
produce speciﬁc returns of signiﬁcant sizes, and the R2 statistic
of the ﬁt will be small. According to experts (Grinold and Kahn,
1999), the R2 statistic of a good factor model with monthly returns of 1,000 stocks and 50 factors is typically about 30 percent to
40 percent.
It may appear that these factor models are only explanatory in
retrospect—that is, given historical returns and factor exposures,
we can compute the factor returns of those historical periods. But
what good are those historical factor returns for our trading? It turns
out that often factor returns are more stable than individual stock
returns. In other words, they have momentum. You can therefore
assume that their values remain unchanged from the current period
(known from the regression ﬁt) to the next time period. If this is
the case, then, of course, you can also predict the excess returns,
as long as the factor exposures are well chosen and therefore the
time-varying speciﬁc returns are not signiﬁcant.
Let me clarify one point of potential confusion. Even though
I stated that factor models can be useful as a predictive model
(and therefore for trading) only if we assume the factor returns
have momentum, it does not mean that factor models cannot capture mean reversion of stock returns. You can, in fact, construct a
--- page 158 ---

136
QUANTITATIVE TRADING
factor exposure that captures mean reversion, such as the negative
of the previous period return. If stock returns are indeed mean reverting, then the corresponding factor return will be positive.
If you are interested in building a trading model based on fundamental factors, there are a number of vendors from whom you can
obtain historical factor data:
r Capital IQ: www.capitaliq.com
r Compustat: www.compustat.com
r MSCI Barra: www.mscibarra.com
r Northﬁeld Information Services: www.northinfo.com
r Quantitative Services Group: www.qsg.com
Example 7.4: Principal Component Analysis as an Example of
Factor Model
The examples of factor exposures I described above are typically economic
(e.g., interest rates), fundamental (e.g., book-to-price ratio), or technical
(e.g., previous period’s return). To obtain historical values of these factor
exposures for a large portfolio of stocks so as to backtest a factor model
is usually quite expensive and not very practical to an independent trader.
(For those who are ﬁscally prepared to purchase such data, see the list in
the main text.) However, there is one kind of factor model that relies on
nothing more than historical returns to construct. This method is the socalled principal component analysis (PCA).
If we use PCA to construct the factor exposures and factor returns, we
must assume that the factor exposures are constant (time independent)
over the estimation period. (This rules out factors that represent mean reversion or momentum, since these factor exposures depend on the prior
period returns.) More importantly, we assume that the factor returns are
uncorrelated; that is to say, their covariance matrix ⟨bbT⟩is diagonal. If we
use the eigenvectors of the covariance matrix ⟨RRT⟩as the columns of the
matrix X in the APT equation R = X b + u above, we will ﬁnd via elementary
linear algebra that ⟨bbT⟩is indeed diagonal; and furthermore, the eigenvalues of ⟨RRT⟩are none other than the variances of the factor returns b. But
of course, there is no point to use factor analysis if the number of factors
is the same as the number of stocks—typically, we can just pick the eigenvectors with the top few eigenvalues to form the matrix X. The number of
eigenvectors to pick is a parameter that you can adjust to optimize your
trading model.
--- page 159 ---

Special Topics in Quantitative Trading
137
In the following MATLAB program (epchan.com/book/example7 4.m),
I illustrate a possible trading strategy applying PCA to S&P 600 small-cap
stocks. It is a strategy based on the assumption that factor returns have
momentum: They remain constant from the current time period to the next.
Hence, we can buy the stocks with the highest expected returns based on
these factors, and short the ones with the lowest expected returns. You will
ﬁnd that the average return of this strategy is negative, indicating that this
assumption may be quite inaccurate, or that speciﬁc returns are too large
for this strategy to work.
clear;
% use lookback days as estimation (training) period
% for determining factor exposures.
lookback=252;numFactors=5; % Use only 5 factors
% for trading strategy, long stocks with topN expected
1-day returns.
topN=50;
% test on SP600 smallcap stocks. (This MATLAB binary
% input file contains tday, stocks, op, hi, lo, cl
% arrays.)
load(’IJR 20080114’);
mycls=fillMissingData(cl);
positionsTable=zeros(size(cl));
% note the rows of dailyret are the observations at
% different time periods
dailyret= (mycls-lag1(mycls))/lag1(mycls);
for t=lookback+1:length(tday)
% here the columns of R are the different
% observations.
R=dailyret(t-lookback+1:t,:)’;
% avoid any stocks with missing returns
hasData=find(all(isfinite(R), 2));
R=R(hasData,:);
avgR=smartmean(R, 2);
% subtract mean from returns
R=R-repmat(avgR, [1 size(R, 2)]);
% compute covariance matrix, with observations in
% rows.
covR=smartcov(R’);
% X is the factor exposures matrix, B the
--- page 160 ---

138
QUANTITATIVE TRADING
% variances of factor returns.
Use the
% eigenvectors of covR as column vectors
% for X.
[X, B]=eig(covR);
% Retain only numFactors
X(:, 1:size(X, 2)-numFactors)=[];
% b are the factor returns for time period t-1
% to t.
results=ols(R(:, end), X);
b=results.beta;
% Rexp is the expected return for next period
% assuming factor returns remain constant.
Rexp=avgR+X*b;
[foo idxSort]=sort(Rexp, ’ascend’);
% short topN stocks with lowest expected returns
positionsTable(t, hasData(idxSort(1:topN)))=-1;
% buy topN stocks with highest expected returns
positionsTable(t, ..
hasData(idxSort(end-topN+1:end)))=1;
end
% compute daily returns of trading strategy
ret=..
smartsum(backshift(1, positionsTable).*dailyret, 2);
% compute annualized average return of
% trading strategy
avgret=smartmean(ret)*252;% A very poor return!
% avgret =
%
%
-1.8099
This program made use of a function smartcov, which computes a covariance matrix based on the daily return vectors of many stocks. In contrast to the MATLAB built-in function cov, it ignores days with no returns
(i.e., those with NaN values.)
function y = smartcov(x)
% Covariance n of finite elements.
% Rows of observations, columns of variables
%
Normalizes by N, not N-1
y=NaN(size(x, 2), size(x, 2));
xc=NaN(size(x));
goodstk=find(˜all(isnan(x), 1));
--- page 161 ---

Special Topics in Quantitative Trading
139
xc(:, goodstk)=..
x(:, goodstk)-repmat(smartmean(x(:, goodstk),1), ..
[size(x, 1) 1]);
% Remove mean
for m=1:length(goodstk)
for n=m:length(goodstk)
y(goodstk(m), goodstk(n))=..
smartmean(xc(:, goodstk(m)).*..
xc(:, goodstk(n)));
y(goodstk(n), goodstk(m))=..
y(goodstk(m), goodstk(n));
end
end
How good are the performances of factor models in real trading? Naturally, it mostly depends on which factor model we are
looking at. But one can make a general observation that factor models that are dominated by fundamental and macroeconomic factors
have one major drawback—they depend on the fact that investors
persist in using the same metric to value companies. This is just another way of saying that the factor returns must have momentum for
factor models to work.
For example, even though the value (book-to-price ratio) factor
returns are usually positive, there are periods of time when investors
prefer growth stocks such as during the Internet bubble in the late
1990s, and in August and December of 2007. As The Economist
noted, one reason growth stocks were back in favor in 2007 is the
simple fact that their price premium over value stocks has narrowed
signiﬁcantly (Economist, 2007b). Another reason is that as the U.S.
economy slowed, investors increasingly opted for companies that
still managed to generate increasing earnings instead of those that
were hurt by the recessionary economy.
Therefore, it is not uncommon for factor models to experience steep drawdown during the times when investors’ valuation
method shifts, even if only for a short duration. But then, this problem is common to practically any trading model that holds stocks
overnight.
--- page 162 ---

140
QUANTITATIVE TRADING
WHAT IS YOUR EXIT STRATEGY?
While entry signals are very speciﬁc to each trading strategy, there
isn’t usually much variety in the way exit signals are generated. They
are based on one of these:
r A ﬁxed holding period
r A target price or proﬁt cap
r The latest entry signals
r A stop price
A ﬁxed holding period is the default exit strategy for any trading strategy, whether it is a momentum model, a reversal model, or
some kind of seasonal trading strategy, which can be either momentum or reversal based. (More on this later.) I said before that one of
the ways momentum is generated is the slow diffusion of information. In this case, the process has a ﬁnite lifetime. The average value
of this ﬁnite lifetime determines the optimal holding period, which
can usually be discovered in a backtest.
One word of caution on determining the optimal holding period
of a momentum model: As I said before, this optimal period typically
decreases due to the increasing speed of the diffusion of information
and the increasing number of traders who catch on to this trading
opportunity. Hence, a momentum model that has worked well with a
holding period equal to a week in the backtest period may work only
with a one-day holding period now. Worse, the whole strategy may
become unproﬁtable a year into the future. Also, using a backtest of
the trading strategy to determine holding period can be fraught with
data-snooping bias, since the number of historical trades may be
limited. Unfortunately, for a momentum strategy where the trades
are triggered by news or events, there are no other alternatives. For
a mean-reverting strategy, however, there is a more statistically robust way to determine the optimal holding period that does not depend on the limited number of actual trades.
The mean reversion of a time series can be modeled by an
equation called the Ornstein-Uhlenbeck formula (Unlenbeck, 1930).
Let’s say we denote the mean-reverting spread (long market value
--- page 163 ---

Special Topics in Quantitative Trading
141
minus short market value) of a pair of stocks as z(t). Then we can
write
dz(t) = −θ(z(t) −µ)dt + dW
where µ is the mean value of the prices over time, and dW is simply some random Gaussian noise. Given a time series of the daily
spread values, we can easily ﬁnd θ (and µ) by performing a linear
regression ﬁt of the daily change in the spread dz against the spread
itself. Mathematicians tell us that the average value of z(t) follows
an exponential decay to its mean µ, and the half-life of this exponential decay is equal to ln(2)/θ, which is the expected time it takes
for the spread to revert to half its initial deviation from the mean.
This half-life can be used to determine the optimal holding period
for a mean-reverting position. Since we can make use of the entire
time series to ﬁnd the best estimate of θ, and not just on the days
where a trade was triggered, the estimate for the half-life is much
more robust than can be obtained directly from a trading model. In
Example 7.5, I demonstrate this method of estimating the half-life of
mean reversion using our favorite spread between GLD and GDX.
Example 7.5: Calculation of the Half-Life of a Mean-Reverting
Time Series
We can use the mean-reverting spread between GLD and GDX in Example
7.2 to illustrate the calculation of the half-life of its mean reversion. The
MATLAB code is available at epchan.com/book/example7 5.m. (The ﬁrst
part of the program is the same as example7 2.m.)
% === Insert example7 2.m in the beginning here ===
prevz=backshift(1, z); % z at a previous time-step
dz=z-prevz;
dz(1)=[];
prevz(1)=[];
% assumes dz=theta*(z-mean(z))dt+w,
% where w is error term
results=ols(dz, prevz-mean(prevz));theta=results.beta;
halflife=-log(2)/theta
--- page 164 ---

142
QUANTITATIVE TRADING
% halflife =
%
%
10.0037
The program ﬁnds that the half-life for mean reversion of the GLD-GDX is
about 10 days, which is approximately how long you should expect to hold
this spread before it becomes proﬁtable.
If you believe that your security is mean reverting, then you also
have a ready-made target price—the mean value of the historical
prices of the security, or µ in the Ornstein-Uhlenbeck formula. This
target price can be used together with the half-life as exit signals
(exit when either criterion is met).
Target prices can also be used in the case of momentum models
if you have a fundamental valuation model of a company. But as
fundamental valuation is at best an inexact science, target prices
are not as easily justiﬁed in momentum models as in mean-reverting
models. If it were that easy to proﬁt using target prices based on
fundamental valuation, all investors have to do is to check out stock
analysts’ reports every day to make their investment decisions.
Suppose you are running a trading model, and you entered into
a position based on its signal. Some time later, you run this model
again. If you ﬁnd that the sign of this latest signal is opposite to your
original position (e.g., the latest signal is “buy” when you have an
existing short position), then you have two choices. Either you simply use the latest signal to exit the existing position and become ﬂat
or you can exit the existing position and then enter into an opposite
position. Either way, you have used a new, more recent entry signal
as an exit signal for your existing position. This is a common way
to generate exit signals when a trading model can be run in shorter
intervals than the optimal holding period.
Notice that this strategy of exiting a position based on running
an entry model also tells us whether a stop-loss strategy is recommended. In a momentum model, when a more recent entry signal
is opposite to an existing position, it means that the direction of
momentum has changed, and thus a loss (or more precisely, a drawdown) in your position has been incurred. Exiting this position now
--- page 165 ---

Special Topics in Quantitative Trading
143
is almost akin to a stop loss. However, rather than imposing an arbitrary stop-loss price and thus introducing an extra adjustable parameter, which invites data-snooping bias, exiting based on the most
recent entry signal is clearly justiﬁed based on the rationale for the
momentum model.
Consider a parallel situation when we are running a reversal
model. If an existing position has incurred a loss, running the reversal model again will simply generate a new signal with the same
sign. Thus, a reversal model for entry signals will never recommend
a stop loss. (On the contrary, it can recommend a target price or
proﬁt cap when the reversal has gone so far as to hit the opposite
entry threshold.) And, indeed, it is much more reasonable to exit
a position recommended by a mean-reversal model based on holding period or proﬁt cap than stop loss, as a stop loss in this case
often means you are exiting at the worst possible time. (The only
exception is when you believe that you have suddenly entered into
a momentum regime because of recent news.)
SEASONAL TRADING STRATEGIES
This type of trading strategy is also called the calendar effect. Generally, these strategies recommend that you buy or sell certain securities at a ﬁxed date of every year, and close the position at another
ﬁxed date. These strategies have been applied to both equity and
commodity futures markets. However, from my own experience,
much of the seasonality in equity markets has weakened or even
disappeared in recent years, perhaps due to the widespread knowledge of this trading opportunity, whereas some seasonal trades in
commodity futures are still proﬁtable.
The most famous seasonal trade in equities is called the January
effect. There are actually many versions of this trade. One version states that small-cap stocks that had the worst returns in the
previous calendar year will have higher returns in January than
small-cap stocks that had the best returns (Singal, 2006). The rationale for this is that investors like to sell their losers in December to beneﬁt from tax losses, which creates additional downward
--- page 166 ---

144
QUANTITATIVE TRADING
pressure on their prices. When this pressure disappeared in January, the prices recovered somewhat. This strategy did not work
in 2006–07, but worked wonderfully in January 2008, which was a
spectacular month for mean-reversal strategies. (That January was
the one that saw a major trading scandal at Soci´et´e G´en´erale, which
indirectly may have caused the Federal Reserve to have an emergency 75-basis-point rate cut before the market opened. The turmoil
slaughtered many momentum strategies, but mean-reverting strategies beneﬁted greatly from the initial severe downturn and then dramatic rescue by the Fed.) The codes for backtesting this January
effect strategy is given in Example 7.6.
Example 7.6: Backtesting the January Eﬀect
Here is the MATLAB code to compute the returns of a strategy applied to
S&P 600 small-cap stocks based on the January eﬀect. (The source codes
can be found at epchan.com/book/example7 6.m, and the input data is
also available there.)
clear;
load(’IJR 20080131’);
onewaytcost=0.0005; % 5bp one way transaction cost
years=..
year(cellstr(datestr(datenum(cellstr(..
num2str(tday)), ’yyyymmdd’))));
months=..
month(cellstr(datestr(datenum(cellstr(..
num2str(tday)), ’yyyymmdd’))));
nextdayyear=fwdshift(1, years);
nextdaymonth=fwdshift(1, months);
lastdayofDec=find(months==12 & nextdaymonth==1);
lastdayofJan=find(months==1 & nextdaymonth==2);
% lastdayofDec starts in 2004,
% so remove 2004 from lastdayofJan
lastdayofJan(1)=[];% Ensure each lastdayofJan date
after each
% lastdayofDec date
--- page 167 ---

Special Topics in Quantitative Trading
145
assert(all(tday(lastdayofJan) > tday(lastdayofDec)));
eoy=find(years∼=nextdayyear); % End Of Year indices
eoy(end)=[]; % last index is not End of Year
% Ensure eoy dates match lastdayofDec dates
assert(all(tday(eoy)==tday(lastdayofDec)));
annret=..
(cl(eoy(2:end),:)-cl(eoy(1:end-1),:))./..
cl(eoy(1:end-1),:); % annual returns
janret=..
(cl(lastdayofJan(2:end),:)-
cl(lastdayofDec(2:end),:))./cl(lastdayofDec(2:end),:);
% January returns
for y=1:size(annret, 1)
% pick those stocks with valid annual returns
hasData=..
find(isfinite(annret(y,:)));
% sort stocks based on prior year’s returns
[foo sortidx]=sort(annret(y, hasData), ’ascend’);
% buy stocks with lowest decile of returns,
% and vice versa for highest decile
topN=round(length(hasData)/10);
% portfolio returns
portRet=..
(smartmean(janret(y, hasData(sortidx(1:topN))))-..
smartmean(janret(y, hasData(..
sortidx(end-topN+1:end)))))/2-2*onewaytcost;
fprintf(1,’Last holding date %i: Portfolio
return=%7.4f\n’, tday(lastdayofDec(y+1)), portRet);
end
% These should be the output
% Last holding date 20051230: Portfolio return=-0.0244
% Last holding date 20061229: Portfolio return=-0.0068
% Last holding date 20071231: Portfolio return= 0.0881
This program uses a number of utility programs. The ﬁrst one is the assert function, which is very useful for ensuring the program is working as
expected.
function assert(pred, str)
% ASSERT Raise an error if the predicate is not true.
% assert(pred, string)
if nargin<2, str = ’’; end
--- page 168 ---

146
QUANTITATIVE TRADING
if ∼pred
s = sprintf(’assertion violated: %s’, str);
error(s);
end
The second one is the fwdshift function, which works in the opposite way
to the lag1 function: It shifts the time series one step forward.
function y=fwdshift(day,x)
assert(day>=0);
y=[x(day+1:end,:,:); ..
NaN*ones(day,size(x,2), size(x, 3))];
Another seasonal strategy in equities was proposed more
recently (Heston and Sadka, 2007; available at lcb1.uoregon.
edu/rcg/seminars/seasonal072604.pdf). This strategy is very simple:
each month, buy a number of stocks that performed the best in the
same month a year earlier, and short the same number of stocks
that performed poorest in that month a year earlier. The average
annual return before 2002 was more than 13 percent before transaction costs. However, I have found that this effect has disappeared
since then, as you can check for yourself in Example 7.7. (See
the readers’ comments to my blog post epchan.blogspot.com/2007/
11/seasonal-trades-in-stocks.html.)
Example 7.7: Backtesting a Year-on-Year
Seasonal Trending Strategy
Here is the MATLAB code for the year-on-year seasonal trending strategy
I quoted earlier. (The source code can be downloaded from epchan.com/
book/example7 7.m. The data is also available at that site.) Note that the
data contains survivorship bias, as it is based on the S&P 500 index on
November 23, 2007.
clear;
load(’SPX 20071123’, ’tday’, ’stocks’, ’cl’);
--- page 169 ---

Special Topics in Quantitative Trading
147
% find the indices of the days that are at month ends.
monthEnds=find(isLastTradingDayOfMonth(tday));
monthlyRet=..
(cl(monthEnds,:)-lag1(cl(monthEnds,:)))./..
lag1(cl(monthEnds,:));
mycl=fillMissingData(cl);
% sort stocks by monthly returns in ascending order
[monthlyRetSorted sortIndex]=sort(monthlyRet, 2);
% these are the sorted monthly returns of the
previous year
prevYearMonthlyRetSorted=backshift(12,
monthlyRetSorted);% the sort index of the
previous year
prevYearSortIndex=backshift(12, sortIndex);
positions=zeros(size(monthlyRet));
for m=13:size(monthlyRet, 1)
hasReturns=. . .
isfinite(prevYearMonthlyRetSorted(m,:)) & ..
isfinite(cl(monthEnds(m-1),:));
mySortIndex=prevYearSortIndex(m, hasReturns);
% take top decile of stocks as longs,
% bottom decile as shorts
topN=floor(length(mySortIndex)/10);
positions(m-1, mySortIndex(1:topN))=-1;
positions(m-1, ..
mySortIndex(end-topN+1:end))=1;
end
ret=smartsum(lag1(positions).*monthlyRet, 2);
avgannret=12*smartmean(ret);
sharpe=sqrt(12)*smartmean(ret)/smartstd(ret);
fprintf(1, ..
’Avg ann return=%7.4f Sharpe ratio=%7.4f\n’, ..
avgannret, sharpe);
% Output should be
% Avg ann return=-0.9167 Sharpe ratio=-0.1055
This program contains a few utility functions. The ﬁrst one is LastTrading-
DayOfMonth, which returns a logical array of 1s and 0s, indicating whether
a month in a trading-date array is the last trading day of a month.
--- page 170 ---

148
QUANTITATIVE TRADING
function isLastTradingDayOfMonth=..
isLastTradingDayOfMonth(tday)
% isLastTradingDayOfMonth=
% isLastTradingDayOfMonth(tday) returns a logical
% array. True if tday(t) is last trading day of month.
tdayStr=datestr(datenum(num2str(tday), ’yyyymmdd’));
todayMonth=month(tdayStr);
tmrMonth=fwdshift(1, todayMonth); % tomorrow’s month
isLastTradingDayOfMonth=false(size(tday));
isLastTradingDayOfMonth(todayMonth˜=tmrMonth & ..
isfinite(todayMonth) & isfinite(tmrMonth))=true;
Another is the backshift function, which is like the lag1 function except that
one can shift any arbitrary number of periods instead of just 1.
function y=backshift(day,x)
% y=backshift(day,x)
assert(day>=0);
y=[NaN(day,size(x,2), size(x, 3));x(1:end-day,:,:)];
You can try the most recent ﬁve years instead of the entire data period, and
you will ﬁnd that the average returns are even worse.
In contrast to equity seasonal strategies, commodity futures’
seasonal strategies are alive and well. That is perhaps because seasonal demand for certain commodities is driven by “real” economic
needs rather than speculations.
One of the most intuitive commodity seasonal trades is the
gasoline future trade: Simply buy the gasoline future contract that
expires in May near the middle of April, and sell it by the end
of April. This trade has been proﬁtable for the last 11 years, as
of this writing in April 2008. (See the sidebar for details.) It appears that one can always depend on approaching summer driving seasons in North America to drive up gasoline futures prices in
the spring.
--- page 171 ---

Special Topics in Quantitative Trading
149
A
S E A S O N A L
T R A D E
I N
G A S O L I N E
F U T U R E S
Whenever the summer driving season comes up, it should not surprise us that
gasoline futures prices will be rising seasonally. The only question for the trader
is: which month contract to buy, and to hold for what period? After scanning the
literature, the best trade I have found so far is one where we buy 1 contract of
RB (the unleaded gasoline futures trading on the New York Mercantile Exchange
[NYMEX]) at the close of April 13 (or the following trading day if it is a holiday),
and sell it at the close of April 25 (or the previous trading day if it is a holiday).
Historically, we would have realized a proﬁt every year since 1995. Here is the
annual proﬁt and loss (P&L) and maximum drawdown (measured from day 1,
the entry point) experienced by this position (the 2007–08 numbers are from
actual trading):
Year
P&L in $
Maximum Drawdown in $
1995
1,037
0
1996
1,638
−2,226
1997
227
−664
1998
118
0
1999
197
−588
2000
735
−315
2001
1,562
0
2002
315
0
2003
1,449
−38
2004
361
−907
2005
6,985
−25
2006
890
0
2007*
2,286
−9,816
2008*
4,741
0
*Actual trading result expressed as 2 × QU.
For those who desire less risk, you can buy the mini gasoline futures QU at
NYMEX which trade at half the size of RB, though it is illiquid.
(This research has been inspired by the monthly seasonal trades published
by Paul Kavanaugh at PFGBest.com. You can read up on this and other seasonal
futures patterns in Fielden, 2005, or Toepke, 2004.)
Besides demand for gasoline, natural gas demand also goes up
as summer approaches due to increasing demand from power generators to provide electricity for air conditioning. Hence, another commodity seasonal trade that has been proﬁtable for 13 consecutive
--- page 172 ---

150
QUANTITATIVE TRADING
years as of this writing is the natural gas trade: Buy the natural gas
future contract that expires in June near the end of February, and
sell it by the middle of April. (Again, see sidebar for details.)
A
S E A S O N A L
T R A D E
I N
N A T U R A L
G A S
F U T U R E S *
Summer season is also when natural gas demand goes up due to the increasing
demand from power generators to provide electricity for air conditioning. This
suggests a seasonal trade in natural gas where we long a June contract of NYMEX
natural gas futures (Symbol: NG) at the close of February 25 (or the following
trading day if it is a holiday), and exit this position on April 15 (or the previous
trading day if it is a holiday). This trade has been proﬁtable for 14 consecutive
years at of this writing. Here is the annual P&L and maximum drawdown of this
trade, both in backtest and in actual trading:
Year
P&L in $
Maximum Drawdown in $
1995
1,970
0
1996
3,090
−630
1997
450
−430
1998
2,150
−1,420
1999
4,340
−370
2000
4,360
0
2001
2,730
−1,650
2002
9,860
0
2003
2,000
−5,550
2004
5,430
0
2005
2,380
−230
2006
2,250
−1,750
2007
800
−7,470
2008*
10,137
−1,604
*Actual trading results expressed as 4 × QG.
Natural gas futures are notoriously volatile, and we have seen big trading
losses for hedge funds (e.g., Amaranth Advisors, loss = $6 billion) and major
banks (e.g., Bank of Montreal, loss = $450 million). Therefore, one should be
cautious if one wants to try out this trade—perhaps at reduced capital using the
mini QG futures at half the size of the full NG contract.
*This article originally appeared in my subscription area epchan.com/subscription, and is
updated with the latest numbers. You can access that area using “sharperatio” as username
and password.
--- page 173 ---

Special Topics in Quantitative Trading
151
Commodity futures seasonal trades do suffer from one drawback despite their consistent proﬁtability: they typically occur only
once a year; therefore, it is hard to tell whether the backtest performance is a result of data-snooping bias. As usual, one way to
alleviate this problem is to try somewhat different entry and exit
dates to see if the proﬁtability holds up. In addition, one should
consider only those trades where the seasonality makes some economic sense. The gasoline and natural gas trades amply satisfy these
criteria.
HIGH-FREQUENCY TRADING
STRATEGIES
In general, if a high Sharpe ratio is the goal of your trading strategy
(as it should be, given what I said in Chapter 6), then you should be
trading at high frequencies, rather than holding stocks overnight.
What are high-frequency trading strategies, and why do they
have superior Sharpe ratios? Many experts in high-frequency trading
would not regard any strategy that holds positions for more than a
few seconds as high frequency, but here I would take a more pedestrian approach and include any strategy that does not hold a position overnight. Many of the early high-frequency strategies were
applied to the foreign exchange market, and then later on to the futures market, because of their abundance of liquidity. In the last six
or seven years, however, with the increasing liquidity in the equity
market, the availability of historical tick database for stocks, and
mushrooming computing power, this type of strategies has become
widespread for stock trading as well.
The reason why these strategies have Sharpe ratio is simple:
Based on the “law of large numbers,” the more bets you can place,
the smaller the percent deviation from the mean return you will
experience. With high-frequency trading, one can potentially place
hundreds if not thousands of bets all in one day. Therefore, provided the strategy is sound and generates positive mean return, you
can expect the day-to-day deviation from this return to be minimal.
With this high Sharpe ratio, one can increase the leverage to a much
--- page 174 ---

152
QUANTITATIVE TRADING
higher level than longer-term strategies can, and this high leverage
in turn boosts the return-on-equity of the strategy to often stratospheric levels.
Of course, the law of large numbers does not explain why a
particular high-frequency strategy has positive mean return in the
ﬁrst place. In fact, it is impossible to explain in general why highfrequency strategies are often proﬁtable, as there are as many such
strategies as there are fund managers. Some of them are mean reverting, while others are trend following. Some are market-neutral
pair traders, while others are long-only directional traders. In general, though, these strategies aim to exploit tiny inefﬁciencies in
the market or to provide temporary liquidity needs for a small fee.
Unlike betting on macroeconomic trends or company fundamentals
where the market environment can experience upheavals during the
lifetime of a trade, such inefﬁciencies and need for liquidity persist
day to day, allowing consistent daily proﬁts to be made. Furthermore, high-frequency strategies typically trade securities in modest sizes. Without large positions to unwind, risk management for
high-frequency portfolios is fairly easy: “Deleveraging” can be done
very quickly in the face of losses, and certainly one can stop trading and be completely in cash when the going gets truly rough. The
worst that can happen as these strategies become more popular is a
slow death as a result of gradually diminishing returns. Sudden drastic losses are not likely, nor are contagious losses across multiple
accounts.
Though successful high-frequency strategies have such numerous merits, it is not easy to backtest such strategies when the
average holding period decreases to minutes or even seconds.
Transaction costs are of paramount importance in testing such
strategies. Without incorporating transactions, the simplest strategies may seem to work at high frequencies. As a consequence, just
having high-frequency data with last prices is not sufﬁcient—data
with bid, ask, and last quotes is needed to ﬁnd out the proﬁtability
of executing on the bid versus the ask. Sometimes, we may even
need historical order book information for backtesting. Quite often,
the only true test for such strategies is to run it in real-time unless
one has an extremely sophisticated simulator.
--- page 175 ---

Special Topics in Quantitative Trading
153
Backtesting is only a small part of the game in high-frequency
trading. High-speed execution may account for a large part of the actual proﬁts or losses. Professional high-frequency trading ﬁrms have
been writing their strategies in C instead of other, more user-friendly
languages, and locating their servers next to the exchange or a major Internet backbone to reduce the microsecond delays. So even
though the Sharpe ratio is appealing and the returns astronomical,
truly high-frequency trading is not by any means easy for an independent trader to achieve in the beginning. But there is no reason
not to work toward this goal gradually as expertise and resources
accrue.
IS IT BETTER TO HAVE
A HIGH-LEVERAGE VERSUS
A HIGH-BETA PORTFOLIO?
In Chapter 6, I discussed the optimal leverage to apply to a portfolio based on the Kelly formula. In the section on factor models
earlier in this chapter, I discussed the Fama-French Three-Factor
model, which suggests that return of a portfolio (or a stock) is
proportional to its beta (if we hold the market capitalization and
book value of its stocks ﬁxed). In other words, you can increase
return on a portfolio by either increasing its leverage or increasing its beta (by selecting high-beta stocks.) Both ways seem commonsensical. In fact, it is clear that given a low-beta portfolio and
a high-beta portfolio, it is easy to apply a higher leverage on the
low-beta portfolio so as to increase its beta to match that of the
high-beta portfolio. And assuming that the stocks of two portfolios have the same average market capitalizations and book values, the average returns of the two will also be the same (ignoring speciﬁc returns, which will decrease in importance as long as
we increase the number stocks in the portfolios), according to the
Fama-French model. So should we be indifferent to which portfolio
to own?
The answer is no. Recall in Chapter 6 that the long-term compounded growth rate of a portfolio, if we use the Kelly leverage,
