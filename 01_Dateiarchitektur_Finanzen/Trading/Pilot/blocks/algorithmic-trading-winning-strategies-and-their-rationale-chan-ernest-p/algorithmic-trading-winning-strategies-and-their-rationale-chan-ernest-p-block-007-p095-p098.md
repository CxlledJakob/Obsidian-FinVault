# Algorithmic Trading (Winning Strategies and Their Rationale) -- Chan, Ernest P_ -- 2013 may 22 -- John Wiley & Sons, Inc_ -- doi 10_1002_9781118676998 -- e374e4354dcd660c7bc666e0297a580b -- Anna’s Archive.pdf — Chapter 3: Chapter 3 (pages 95–98)

--- page 95 ---

82
ALGORITHMIC TRADING

■Kalman Filter as Market-Making Model
There is another noteworthy application of Kalman fi lter to a meanreverting strategy. In this application we are concerned with only one
mean-reverting price series; we are not concerned with fi nding the hedge
ratio between two cointegrating price series. However, as before, we still
want to fi nd the mean price and the standard deviation of the price series
for our mean reversion trading. So the mean price m(t) is the hidden variable here, and the price y(t) is the observable variable. The measurement
equation in this case is trivial:

y(t) = m(t) +
∋
(t),
(“Measurement equation”) (3.14)
with the same state transition equation

m(t) = m(t − 1) + ω(t − 1).
(“State transition”) (3.15)
So the state update equation 3.11 is just

m(t | t) = m(t | t − 1) + K(t)(  y(t) − m(t | t − 1)). (“State update”) (3.16)
(This may be the time to review Box 3.1 if you skipped it on fi rst reading.)
The variance of the forecast error is

Q(t) = Var(m(t)) + Ve.
(3.17)
The Kalman gain is

K(t) = R(t | t − 1)/(R(t | t − 1) + Ve),
(3.18)
and the state variance update is

R(t | t) = (1 − K(t))R(t | t − 1).
(3.19)
Example 3.3 (Continued)
Instead of coding the Kalman fi lter yourself as we demonstrated,
you can also use many free open-source MATLAB codes available.
One such package can be found at www.cs.ubc.ca/~murphyk
/Software/Kalman/kalman.html. Kalman fi lters are also available
from MATLAB’s Control System Toolbox.
--- page 96 ---

83
IMPLEMENTING MEAN REVERSION STRATEGIES
Why are these equations worth highlighting? Because this is a favorite
model for market makers to update their estimate of the mean price of an
asset, as Euan Sinclair pointed out (Sinclair, 2010). To make these equations
more practical, practitioners make further assumptions about the measurement error Ve, which, as you may recall, measures the uncertainty of the observed transaction price. But how can there be uncertainty in the observed
transaction price? It turns out that we can interpret the uncertainty in such
a way that if the trade size is large (compared to some benchmark), then the
uncertainty is small, and vice versa. So Ve in this case becomes a function of t
as well. If we denote the trade size as T and the benchmark trade size as Tmax,
then Ve can have the form

Ve = R(t | t − 1)
−
⎛
⎝
⎜
⎞
⎠
⎟
T
T
1
max

(3.20)
So you can see that if T = Tmax, there is no uncertainty in the observed
price, and the Kalman gain is 1, and hence the new estimate of the mean
price m(t) is exactly equal to the observed price! But what should Tmax be? It
can be some fraction of the total trading volume of the previous day, for example, where the exact fraction is to be optimized with some training data.
Note the similarity of this approach to the so-called volume-weighted
average price (VWAP) approach to determine the mean price, or fair value
of an asset. In the Kalman fi lter approach, not only are we giving more
weights to trades with larger trade sizes, we are also giving more weights to
more recent trade prices. So one might compare this to volume and timeweighted average price.

■The Danger of Data Errors
Data errors have a particularly insidious eff ect on both backtesting and executing mean-reverting strategies.
If there are errors, or “outliers,” in the historical data used for backtesting, then these errors usually infl ate the backtest performance of
mean-reverting strategies. For example, if the actual trade prices of a
stock at 11:00, 11:01, and 11:02 were $100, $100, and $100, but the
historical data erroneously recorded them as $100, $110, $100, then
your mean-reverting strategy’s backtest is likely to have shorted the
stock at 11:01 ($110), and then covered the position at 11:02 ($100)
and made a tidy but fi ctitious profi t of $10. You can see that data quality
is particularly important for intraday data, because they present much
--- page 97 ---

84
ALGORITHMIC TRADING
more numerous opportunities for such errors. That’s why reputable data
vendors took great care in incorporating the exchange-provided canceland-correct codes to correct any trades that may have been canceled due
to transaction prices that are too far from “normal.” (What constitutes a
“normal” price is solely determined, sometimes on a case-by-case basis,
by the relevant exchange.) Thomas Falkenberry (2002) has written more
on data cleansing issues.
However, this type of data error will suppress the backtest performance
of momentum strategies, so it is not as dangerous. In the preceding example, a momentum strategy will likely buy the stock at 11:01 ($110) in
backtest, and may be stopped out at a loss at 11:02 ($100).
The same kind of errors will, of course, trigger wrong trades in live trading as well, often resulting in real-life losses. In the preceding example, if the
prices were bid prices, and we have the erroneous bid at $110 at 11:02, then
our execution program may have sent a short market sell order at that time,
which unfortunately will be fi lled at $100 instead since there was actually
no bid at $110.
This problem with erroneous live bid/ask quotes is particularly dangerous when trading pairs or other arbitrage strategies, because in these
strategies we often depend on the diff erences of the price quotes from
various instruments to trigger trading signals. The diff erence of a pair of
quotes is usually of much smaller magnitude than the quotes themselves,
so any error in the quotes results in a much bigger percentage error in the
spread. For example, if we are trading a pair of stocks X and  Y, and X has
a true bid price of $100 and Y has a true ask price of $105, so the spread
Y−X is $5, which may be too small to trigger an market order to buy X
and sell Y. But if data error causes Y to display an ask price of $106, then
the erroneous spread becomes $6, an increase of 20 percent over the real
spread of $5, and this may be enough to trigger an erroneous order to buy
X and sell Y.
I have seen this problem in live trading when I used a broker’s data feed
to drive an equities pair-trading strategy. That data feed quite regularly triggered losing trades that I could not explain, until I switched the data feed
to a third-party provider (nothing fancier than Yahoo! real-time quotes) and
the bad trades stopped. Later on, I had access to Bloomberg’s live data feed,
and it didn’t trigger any of these bad trades either.
Bad ticks in live data will also cause momentum strategies to send
wrong orders. So they are equally loss-inducing to the execution of those
strategies.
--- page 98 ---

85
IMPLEMENTING MEAN REVERSION STRATEGIES
• Do you want to construct a mean-reverting portfolio with a fi xed number
of shares during the duration of a trade? Use price series to determine the
hedge ratios.
• Do you want to construct a mean-reverting portfolio with fi xed market
values for each constituent during the duration of a trade? Use log price
series to determine the hedge ratios.
• Ratio, instead of spreads, is often a good indicator for trading currency
pairs.
• Afraid that the hedge ratio, mean, and standard deviation of a spread may
vary in the future? Use a moving look-back period or the Kalman fi lter.
• A practical implementation of a linear trading strategy is the Bollinger bands
with scaling-in.
• Scaling-in may not be optimal in backtests but is often useful for live trading
where volatilities and probabilities do change.
• Do you want to dynamically update the expected price of an instrument
based on its latest trade (price and size)? Use the Kalman fi lter.
• Data errors can infl ate the backtest results of mean-reverting strategies but
not momentum strategies.
• Strategies based on spreads are particularly sensitive to small data errors,
whether in backtest or live trading.
KEY POINTS
