# Algorithmic Trading_ Winning Strategies and Their Rationale.pdf — Chapter 2: The Basics of Mean Reversion (pages 76–80)

--- page 76 ---

58
ALGORITHMIC TRADING
the “strongest”; that is, have the shortest half-life for mean reversion.
Naturally, we pick this eigenvector to form our stationary portfolio
(the eigenvector determines the shares of each ETF), and we can fi nd
its half-life by the same method as before when we were dealing with
a stationary price series. The only diff erence is that we now have to
compute the T × 1 array yport, which represents the net market value
(price) of the portfolio, which is equal to the number of shares of
each ETF multiplied by the share price of each ETF, then summed
over all ETFs. yport takes the role of y in Example 2.4.
yport=smartsum(repmat(results.evec(:, 1)’, [size(y3, 1) ...
1]).*y3, 2);
% Find value of lambda and thus the half-life of mean
 % reversion by linear regression fit
ylag=lag(yport, 1);  % lag is a function in the jplv7
 % (spatial-econometrics.com) package.
deltaY=yport-ylag;
deltaY(1)=[]; % Regression functions cannot handle the NaN
 % in the first bar of the time series.
ylag(1)=[];
regress_results=ols(deltaY, [ylag ones(size(ylag))]);
halflife=-log(2)/regress_results.beta(1);
The half-life of 23 days is considerably shorter than the 115 days for
USD.CAD, so we expect a mean reversion trading strategy to work
better for this triplet.
Example 2.7 (Continued)
Linear Mean-Reverting Trading on a Portfolio
In Example 2.7 we determined that the EWA-EWC-IGE portfolio formed
with the “best” eigenvector from the Johansen test has a short half-life. We
can now confi dently proceed to backtest our simple linear mean-reverting
strategy on this portfolio. The idea is the same as before when we own a
number of units in USD.CAD proportional to their negative normalized deviation from its moving average (i.e., its Z-Score). Here, we also accumulate
units of the portfolio proportional to the negative Z-Score of the “unit” portfolio’s price. A unit portfolio is one with shares determined by the Johansen
eigenvector. The share price of a unit portfolio is like the share price of a
--- page 77 ---

59
THE BASICS OF MEAN REVERSION
mutual fund or ETF: it is the same as its market value. When a unit portfolio
has only a long and a short position in two instruments, it is usually called a
spread. (We express this in more mathematical form in Chapter 3.)
Note that by a “linear” strategy we mean only that the number of units
invested is proportional to the Z-Score, not that the market value of our
investment is proportional.
This linear mean-reverting strategy is obviously not a practical strategy, at
least in its simplest version, as we do not know the maximum capital required
Example 2.8: Backtesting a Linear Mean-Reverting
Strategy on a Portfolio
The yport is a Tx1 array representing the net market value of the
“unit” portfolio calculated in the preceding code fragment. numUnits
is a Tx1 array representing the multiples of this unit portfolio we
wish to purchase. (The multiple is a negative number if we wish
to short the unit portfolio.) All other variables are as previously
calculated. The positions is a Tx3 array representing the position
(market value) of each ETF in the portfolio we have invested in.
(This code fragment is part of cointegrationTests.m.)
%  Apply a simple linear mean reversion strategy to EWA-EWC-
 % IGE
lookback=round(halflife); % setting lookback to the halflife
 % found above
numUnits =-(yport-movingAvg(yport, lookback))...
  ./movingStd(yport, lookback); % multiples of unit
% portfolio .  movingAvg and movingStd are functions from
% epchan.com/book2
positions=repmat(numUnits,  [1 size(y3,  2)]).*repmat(results. ...
  evec(:, 1)’, [size(y3, 1) 1]).*y3;
% results.evec(:, 1)’ is the shares allocation, while
% positions is the capital (dollar)
% allocation in each ETF.
pnl=sum(lag(positions, 1).*(y3-lag(y3, 1))./lag(y3, 1), 2);
 % daily P&L of the strategy
ret=pnl./sum(abs(lag(positions, 1)), 2); % return is P&L
 % divided by gross market value of portfolio
 Figure 2.7 displays the cumulative returns curve of this linear meanreverting strategy for a stationary portfolio of EWA, EWC, and IGE.
(Continued )
--- page 78 ---

60
ALGORITHMIC TRADING
FIGURE 2.7 Cumulative Returns of a Linear Trading
Strategy on EWA-EWC-IGE Stationary Portfolio
We fi nd that APR = 12.6 percent with a Sharpe ratio of 1.4 for the
strategy.
Example 2.8 (Continued)
at the outset and we cannot really enter and exit an infi nitesimal number of
shares whenever the price moves by an infi nitesimal amount. Despite such
impracticalities, the importance of backtesting a mean-reverting price series
with this simple linear strategy is that it shows we can extract profi ts without any data-snooping bias, as the strategy has no parameters to optimize.
(Remember that even the look-back is set equal to  the half-life, a quantity that
depends on the properties of the price series itself, not our specifi c trading
strategy.) Also, as the strategy continuously enters and exits positions, it is
likely to have more statistical signifi cance than any other trading strategies that
have more complicated and selective entry and exit rules.

■Pros and Cons of Mean-Reverting Strategies
It is often fairly easy to construct mean-reverting strategies because we are
not limited to trading instruments that are intrinsically stationary. We can
pick and choose from a great variety of cointegrating stocks and ETFs to
create our own stationary, mean-reverting portofolio. The fact that every
--- page 79 ---

61
THE BASICS OF MEAN REVERSION
year there are new ETFs created that may be just marginally diff erent from
existing ones certainly helps our cause, too.
Besides the plethora of choices, there is often a good fundamental story
behind a mean-reverting pair. Why does EWA cointegrate with EWC? That’s
because both the Canadian and the Australian economies are dominated by
commodities. Why does GDX cointegrate with GLD? That’s because the
value of gold-mining companies is very much based on the value of gold.
Even when a cointegrating pair falls apart (stops cointegrating), we can often still understand the reason. For example, as we explain in Chapter 4,
the reason GDX and GLD fell apart around the early part of 2008 was high
energy prices, which caused mining gold to be abnormally expensive. We
hope that with understanding comes remedy. This availability of fundamental reasoning is in contrast to many momentum strategies whose only justifi cation is that there are investors who are slower than we are in reacting to
the news. More bluntly, we must believe there are greater fools out there.
But those fools do eventually catch up to us, and the momentum strategy in
question may just stop working without explanation one day.
Another advantage of mean-reverting strategies is that they span a great
variety of time scales. At one extreme, market-making strategies rely on
prices that mean-revert in a matter of seconds. At the other extreme, fundamental investors invest in undervalued stocks for years and patiently wait
for their prices to revert to their “fair” value. The short end of the time scale
is particularly benefi cial to traders like ourselves, since a short time scale
means a higher number of trades per year, which in turn translates to higher
statistical confi dence and higher Sharpe ratio for our backtest and live trading, and ultimately higher compounded return of our strategy.
Unfortunately, it is because of the seemingly high consistency of meanreverting strategy that may lead to its eventual downfall. As Michael
Dever pointed out, this high consistency often lulls traders into overconfi dence and overleverage as a result (Dever, 2011). (Think Long Term
Capital Management.) When a mean-reverting strategy suddenly breaks
down, perhaps because of a fundamental reason that is discernible only
in hindsight, it often occurs when we are trading it at maximum leverage
after an unbroken string of successes. So the rare loss is often very painful
and sometimes catastrophic. Hence, risk management for mean reverting
is particularly important, and particularly diffi  cult since the usual stop
losses cannot be logically deployed. In Chapter 8, I discuss why this is the
case, as well as techniques for risk management that are suitable for meanreverting strategies.
--- page 80 ---

62
ALGORITHMIC TRADING
• Mean reversion means that the change in price is proportional to the
difference between the mean price and the current price.
• Stationarity means that prices diffuse slower than a geometric random walk.
• The ADF test is designed to test for mean reversion.
• The Hurst exponent and Variance Ratio tests are designed to test for
stationarity.
• Half-life of mean reversion measures how quickly a price series reverts to its
mean, and is a good predictor of the profi tability or Sharpe ratio of a meanreverting trading strategy when applied to this price series.
• A linear trading strategy here means the number of units or shares of a unit
portfolio we own is proportional to the negative Z-Score of the price series
of that portfolio.
• If we can combine two or more nonstationary price series to form a
stationary portfolio, these price series are called cointegrating.
• Cointegration can be measured by either CADF test or Johansen test.
• The eigenvectors generated from the Johansen test can be used as hedge
ratios to form a stationary portfolio out of the input price series, and the one
with the largest eigenvalue is the one with the shortest half-life.
KEY POINTS
