# Algorithmic Trading (Winning Strategies and Their Rationale) -- Chan, Ernest P_ -- 2013 may 22 -- John Wiley & Sons, Inc_ -- doi 10_1002_9781118676998 -- e374e4354dcd660c7bc666e0297a580b -- Anna’s Archive.pdf — Chapter 1: Chapter 1 (pages 14–33)

--- page 14 ---

1
Backtesting
and Automated
Execution
C H A P T E R 1
W
hile the focus of this book is on specifi c categories of strategies and
not on general techniques of backtesting, there are a number of important considerations and common pitfalls to all strategies that need to
be addressed fi rst. If one blithely goes ahead and backtests a strategy without taking care to avoid these pitfalls, the backtesting will be useless. Or
worse—it will be misleading and may cause signifi cant fi nancial losses.
Since backtesting typically involves the computation of an expected return and other statistical measures of the performance of a strategy, it is
reasonable to question the statistical signifi cance of these numbers. We will
discuss various ways of estimating statistical signifi cance using the methodologies of hypothesis testing and Monte Carlo simulations. In general, the
more round trip trades there are in the backtest, the higher will be the statistical signifi cance. But even if a backtest is done correctly without pitfalls
and with high statistical signifi cance, it doesn’t necessarily mean that it is
predictive of future returns. Regime shifts can spoil everything, and a few
important historical examples will be highlighted.
The choice of a software platform for backtesting is also an important
consideration and needs to be tackled early on. A good choice not only will
vastly increase your productivity, it will also allow you to backtest the broadest possible spectrum of strategies in the broadest variety of asset classes.
Algorithmic Trading: Winning Strategies and Their Rationale. Ernest P. Chan.
© 2013 Ernest P. Chan. Published 2013 by John Wiley & Sons, Inc.
--- page 15 ---

2
ALGORITHMIC TRADING
And it will reduce or eliminate the chances of committing the aforementioned pitfalls. We will also explain why the choice of a good backtesting
platform is often tied to the choice of a good automated execution platform:
often, the best platform combines both functions.

■The Importance of Backtesting
Backtesting is the process of feeding historical data to your trading strategy
to see how it would have performed. The hope is that its historical performance tells us what to expect for its future performance. The importance of
this process is obvious if you have developed a strategy from scratch, since
you would certainly want to know how it has performed. But even if you
read about a strategy from a publication, and you trust that the author did
not lie about its stated performance, it is still imperative that you independently backtest the strategy. There are several reasons for this.
Often, the profi tability of a strategy depends sensitively on the details
of implementation. For example, are the stock orders supposed to be sent
as market-on-open orders or as market orders just after the open? Are we
supposed to send in an order for the E-mini Standard & Poor’s (S&P) 500
future just before the 4:00 p.m. stock market closing time, or just before
the 4:15 p.m. futures market closing time? Are we supposed to use the bid
or ask price to trigger a trade, or are we supposed to use the last price? All
these details tend to be glossed over in a published article, often justifi ably
so lest they distract from the main idea, but they can aff ect the profi tability of a live-traded strategy signifi cantly. The only way to pin down these
details exactly, so as to implement them in our own automated execution
system, is to backtest the strategy ourselves. In fact, ideally, our backtesting program can be transformed into an automated execution program by
the push of a button to ensure the exact implementation of details.
Once we have implemented every detail of a strategy as a backtest program, we can then put them under the microscope and look for pitfalls in
the backtesting process or in the strategy itself. For example, in backtesting
a stock portfolio strategy with both long and short positions, have we taken
into account the fact that some stocks were hard to borrow and cannot easily
be shorted at any reasonable size? In backtesting an intermarket pair-trading
strategy in futures, have we made sure that the closing prices of the two
markets occur at the same time? The full list of pitfalls is long and tedious,
but I will highlight a few common ones in the section “Common Pitfalls of
--- page 16 ---

3
BACKTESTING AND AUTOMATED EXECUTION
Backtesting.” Often, each market and each strategy presents its own very
specifi c set of pitfalls. Usually, a pitfall tends to infl ate the backtest performance of a strategy relative to its actual performance in the past, which is
particularly dangerous.
Even if we have satisfi ed ourselves that we have understood and implemented every detail of a strategy in a backtesting program, and that there is
no pitfall that we can discover, backtesting a published strategy can still yield
important benefi ts.
Backtesting a published strategy allows you to conduct true out-of-sample
testing in the period following publication. If that out-of-sample performance
proves poor, then one has to be concerned that the strategy may have worked
only on a limited data set. This is actually a more important point than people
realize. Many authors will claim in their articles that the backtest results were
“verifi ed with out-of-sample data.” But, actually, if the out-of-sample testing
results were poor, the authors could have just changed some parameters, or
they could have tweaked the model substantially so that the results look good
with the “out-of-sample” data. Hence, true out-of-sample testing cannot really begin until a strategy is published and cast in stone.
Finally, by backtesting a strategy ourselves, we often can fi nd ways to
refi ne and improve the strategy to make it more profi table or less risky.
The backtesting process in trading should follow the “scientifi c method.”  We
should start with a hypothesis about an arbitrage opportunity, maybe based
on our own intuition about the market or from some published research.
We then confi rm or refute this hypothesis by a backtest. If the results of the
backtest aren’t good enough, we can modify our hypothesis and repeat the
process.
As I emphasized earlier, performance of a strategy is often very sensitive
to details, and small changes in these details can bring about substantial improvements. These changes can be as simple as changing the look-back time
period for determining the moving average, or entering orders at the open
rather than at the close. Backtesting a strategy allows us to experiment with
every detail.

■Common Pitfalls of Backtesting
Although almost every strategy allows for unique opportunities in committing errors in backtesting, there are a number of common themes, some
generally applicable to all markets, others pertain to specifi c ones.
--- page 17 ---

4
ALGORITHMIC TRADING
Look-ahead Bias
As its name implies, look-ahead bias means that your backtest program is using tomorrow’s prices to determine today’s trading signals. Or, more generally, it is using future information to make a “prediction” at the current time.
A common example of look-ahead bias is to use a day’s high or low price to
determine the entry signal during the same day during backtesting. (Before
the close of a trading day, we can’t know what the high and low price of the
day are.) Look-ahead bias is essentially a programming error and can infect
only a backtest program but not a live trading program because there is no
way a live trading program can obtain future information. This diff erence
between backtesting and a live trading program also points to an obvious
way to avoid look-ahead bias. If your backtesting and live trading programs
are one and the same, and the only diff erence between backtesting versus
live trading is what kind of data you are feeding into the program (historical
data in the former, and live market data in the latter), then there can be no
look-ahead bias in the program. Later on in this chapter, we will see which
platforms allow the same source code to be used for both backtest and live
execution.
Data-Snooping Bias and the Beauty of Linearity
Data-snooping bias is caused by having too many free parameters that are
fi tted to random ethereal market patterns in the past to make historical performance look good. These random market patterns are unlikely to recur
in the future, so a model fi tted to these patterns is unlikely to have much
predictive power.
The way to detect data-snooping bias is well known: We should test the
model on out-of-sample data and reject a model that doesn’t pass the out-ofsample test. But this is easier said than done. Are we really willing to give up
on possibly weeks of work and toss out the model completely? Few of us are
blessed with such decisiveness. Many of us will instead tweak the model this
way or that so that it fi nally performs reasonably well on both the in-sample
and the out-of-sample result. But voilà! By doing this we have just turned
the out-of-sample data into in-sample data.
If you are unwilling to toss out a model because of its performance on
a fi xed out-of-sample data set (after all, poor performance on this out-ofsample data may just be due to bad luck), or if you have a small data set
to start with and really need to tweak the model using most of this data,
you should consider the idea of cross-validation. That is, you should select a
--- page 18 ---

5
BACKTESTING AND AUTOMATED EXECUTION
number of diff erent subsets of the data for training and tweaking your model
and, more important, making sure that the model performs well on these
diff erent subsets. One reason why we prefer models with a high Sharpe ratio
and short maximum drawdown duration is that this almost automatically
ensures that the model will pass the cross-validation test: the only subsets
where the model will fail the test are those rare drawdown periods.
There is a general approach to trading strategy construction that can minimize data-snooping bias: make the model as simple as possible, with as few
parameters as possible. Many traders appreciate the second edict, but fail
to realize that a model with few parameters but lots of complicated trading
rules are just as susceptible to data-snooping bias. Both edicts lead to the
conclusion that nonlinear models are more susceptible to data-snooping bias
than linear models because nonlinear models not only are more complicated
but they usually have more free parameters than linear models.
Suppose we attempt to predict price by simple extrapolation of the historical price series. A nonlinear model would certainly fi t the historical data
better, but that’s no guarantee that it can predict a future value better. But
even if we fi x the number of parameters to be the same for a nonlinear
model versus its linear contender, one has to remember that we can usually
approximate a nonlinear model by Taylor-series expansion familiar from
calculus. That means that there is usually a simpler, linear approximation
corresponding to every nonlinear model, and a good reason has to be given
why this linear model cannot be used. (The exceptions are those singular
cases where the lower-order terms vanish. But such cases seldom describe
realistic fi nancial time series.)
An equivalent reasoning can be made in the context of what probability distributions we should assume for returns. We have heard often that the
Gaussian distribution fails to capture extreme events in the fi nancial market.
But the problem with going beyond the Gaussian distribution is that we will
be confronted with many choices of alternative distributions. Should it be a
Student’s t-distribution that allows us to capture the skew and kurtosis of the
returns, or should it be a Pareto distribution that dispenses with a fi nite second
moment completely? Any choice will have some element of arbitrariness, and
the decision will be based on a fi nite number of observations. Hence, Occam’s
razor dictates that unless there are strong theoretical and empirical reasons
to support a non-Gaussian distribution, a Gaussian form should be assumed.
Linear models imply not only a linear price prediction formula, but also
a linear capital allocation formula. Let’s say we are considering a meanreverting model for a price series such that the change in the price dy in
--- page 19 ---

6
ALGORITHMIC TRADING
the next time period dt is proportional to the diff erence between the mean
price and the current price: dy(t) = (λy(t − 1) + μ)dt + dε, the so-called
“Ornstein-Uhlenbeck” formula, which is explained and examined in greater
detail in Chapter 2. Often, a trader will use a Bollinger band model to capture profi ts from this mean-reverting price series, so that we sell (or buy)
whenever the price exceeds (or falls below) a certain threshold. However, if
we are forced to stick to linear models, we would be forced to sell (or buy)
at every price increment, so that the total market value is approximately
proportional to the negative deviation from the mean. In common traders’
parlance, this may be called “averaging-in,” or “scaling-in,” a technique that
is discussed in Chapter 3.
You will fi nd several examples of linear trading models in this book because the simplicity of this technique lets us illustrate the point that profi ts
are not derived from some subtle, complicated cleverness of the strategy
but from an intrinsic ineffi  ciency in the market that is hidden in plain sight.
The impatient reader can look ahead to Example 4.2, which shows a linear
mean-reverting strategy between an exchange-traded fund (ETF) and its
component stocks, or Examples 4.3 and 4.4, showing two linear long-short
statistical arbitrage strategies on stocks.
The most extreme form of linear predictive models is one in which
all the coefficients are equal in magnitude (but not necessarily in sign).
For example, suppose you have identified a number of factors (  f ’s) that
are useful in predicting whether tomorrow’s return of a stock index is
positive. One factor may be today’s return, with a positive today’s return predicting a positive future return. Another factor may be today’s
change in the volatility index (VIX), with a negative change predicting
positive future return. You may have several such factors. If you normalize these factors by turning them first into Z-scores (using in-sample
data!):

z(i) = (  f(i) − mean(  f  ))/std(  f  ),
(1.1)
where f (i) is the ith factor, you can then predict tomorrow’s return R by

∑
)
(
=
+
R
mean R
std R
sign i z i
n
( )
( ) ( )/
i
n
.
(1.2)
The quantities mean(  f  ) and std(  f  ) are the historical average and standard
deviation of the various f(i), sign(i) is the sign of the historical correlation
between f(i) and R, and mean(R) and std(R) are the historical average and
--- page 20 ---

7
BACKTESTING AND AUTOMATED EXECUTION
standard deviation of one-day returns, respectively. Daniel Kahneman, the
Nobel Prize-winning economist, wrote in his bestseller Thinking, Fast and
Slow that “formulas that assign equal weights to all the predictors are often
superior, because they are not aff ected by accidents of sampling” (Kahneman,
2011). Equation 1.2 is a simplifi ed version of the usual factor model used in
stock return prediction. While its prediction of the absolute returns may or
may not be very accurate, its prediction of relative returns between stocks
is often good enough. This means that if we use it to rank stocks, and then
form a long-short portfolio by buying the stocks in the top decile and shorting those in the bottom decile, the average return of the portfolio is often
positive.
Actually, if your goal is just to rank stocks instead of coming up with an
expected return, there is an even simpler way to combine the factors f ’s
without using Equations 1.1 and 1.2. We can fi rst compute the ranks(i) of a
stock s based on a factor f(i). Then we multiply these ranks by the sign of the
correlation between f(i) and the expected return of the stock. Finally, we
sum all these signed ranks to form the rank of a stock:

∑
)
(
=
rank
sign i rank i( )
s
s
i
n
.
(1.3)
As an example, Joel Greenblatt has famously used a two-factor model as a
“magic formula” to rank stocks: f(1) = return on capital and f(2) = earnings
yield (Greenblatt, 2006). We are supposed to buy the top 30 ranked stocks
and hold them for a year. The annual percentage rate (APR) for this strategy
was 30.8 percent from 1988 to 2004, compared with 12.4 percent for the
S&P 500. Quite a triumph of linearity!
In the end, though, no matter how carefully you have tried to prevent
data-snooping bias in your testing process, it will somehow creep into your
model. So we must perform a walk-forward test as a fi nal, true out-ofsample test. This walk-forward test can be conducted in the form of paper trading, but, even better, the model should be traded with real money
(albeit with minimal leverage) so as to test those aspects of the strategy that
eluded even paper trading. Most traders would be happy to fi nd that live
trading generates a Sharpe ratio better than half of its backtest value.
Stock Splits and Dividend Adjustments
Whenever a company’s stock has an N-to-1 split, the stock price will be divided by N times. However, if you own a number of shares of that company’s
--- page 21 ---

8
ALGORITHMIC TRADING
stock before the split, you will own N times as many shares after the split,
so there is in fact no change in the total market value. But in a backtest,
we typically are looking at just the price series to determine our trading
signals, not the market-value series of some hypothetical account. So unless
we back-adjust the prices before the ex-date of the split by dividing them by
N, we will see a sudden drop in price on the ex-date, and that might trigger
some erroneous trading signals. This is as true in live trading as in backtesting, so you would have to divide the historical prices by N just before the
market opens on the ex-date during live trading, too. (If it is a reverse 1-to-
N split, we would have to multiply the historical prices before the ex-date
by N.)
Similarly, when a company pays a cash (or stock) dividend of $d per
share, the stock price will also go down by $d (absent other market movements). That is because if you own that stock before the dividend ex-date,
you will get cash (or stock) distributions in your brokerage account, so
again there should be no change in the total market value. If you do not
back-adjust the historical price series prior to the ex-date, the sudden drop
in price may also trigger an erroneous trading signal. This adjustment, too,
should be applied to any historical data used in the live trading model just
before the market opens on an ex-date. (This discussion applies to ETFs as
well. A slightly more complicated treatment needs to be applied to options
prices.)
You can fi nd historical split and dividend information on many websites,
but I fi nd that earnings.com is an excellent free resource. It not only records
such historical numbers, but it shows the announced split and dividend
amounts and ex-dates in the future as well, so we can anticipate such events
in our automated trading software. If you are interested in historical stock
data that are already adjusted for stock splits and dividends, and are easy to
download, try csidata.com.
Survivorship Bias in Stock Database
If you are backtesting a stock-trading model, you will suff er from survivorship bias if your historical data do not include delisted stocks. Imagine
an extreme case: suppose your model asks you to just buy the one stock
that dropped the most in the previous day and hold it forever. In actuality,
this strategy will most certainly perform poorly because in many cases the
company whose stock dropped the most in the previous day will go on to
bankruptcy, resulting in 100 percent loss of the stock position. But if your
--- page 22 ---

9
BACKTESTING AND AUTOMATED EXECUTION
historical data do not include delisted stocks—that is, they contain only
stocks that survive until today—then the backtest result may look excellent.
This is because you would have bought a stock when it was beaten down
badly but subsequently survived, though you could not have predicted its
eventual survival if you were live-trading the strategy.
Survivorship bias is more dangerous to mean-reverting long-only stock
strategies than to mean-reverting long-short or short-only strategies. This is
because, as we saw earlier, this bias tends to infl ate the backtest performance
of a long-only strategy that fi rst buys low and then sells high, whereas it will
defl ate the backtest performance of a short-only strategy that fi rst sells high
and then buys low. Those stocks that went to zero would have done very well
with a short-only strategy, but they would not be present in backtest data
with survivorship bias. For mean-reverting long-short strategies, the two
eff ects are of opposite signs, but infl ation of the long strategy return tends
to outweigh the defl ation of the short portfolio return, so the danger is reduced but not eliminated. Survivorship bias is less dangerous to momentum
models. The profi table short momentum trade will tend to be omitted in
data with survivorship bias, and thus the backtest return will be defl ated.
You can buy reasonably priced historical data that are free of survivorship bias from csidata.com (which provides a list of delisted stocks). Other
vendors include kibot.com, tickdata.com, and crsp.com. Or you can in fact
collect your own survivorship bias–free data by saving the historical prices
of all the stocks in an index every day. Finally, in the absence of such survivorship bias–free data, you can limit yourself to backtesting only the most
recent, say, three years of historical data to reduce the damage.
Primary versus Consolidated Stock Prices
Many U.S. stocks are traded on multiple exchanges, electronic communication networks (ECNs), and dark pools: The New York Stock Exchange
(NYSE), NYSE Arca, Nasdaq, Island, BATS, Instinet, Liquidnet, Bloomberg
Tradebook, Goldman Sachs’ Sigma X, and Credit Suisse’s CrossFinder are
just some of the example markets. When you look up the historical daily
closing price of a stock, it refl ects the last execution price on any one of
these venues during regular trading hours. Similarly, a historical daily opening price refl ects the fi rst execution price on any one of these venues. But
when you submit a market-on-close (MOC) or market-on-open (MOO)
order, it will always be routed to the primary exchange only. For example,
an MOC order on IBM will be routed to NYSE, an MOC order on SPY
--- page 23 ---

10
ALGORITHMIC TRADING
will be routed to NYSE Arca, and an MOC order on Microsoft (MSFT) will
be routed to Nasdaq. Hence, if you have a strategy that relies on marketon-open or market-on-close orders, you need the historical prices from
the primary exchange to accurately backtest your model. If you use the
usual consolidated historical prices for backtesting, the results can be quite
unrealistic. In particular, if you use consolidated historical prices to backtest a mean-reverting model, you are likely to generate infl ated backtest
performance because a small number of shares can be executed away from
the primary exchange at a price quite diff erent from the auction price on
the primary exchange. The transaction prices on the next trading day will
usually mean-revert from this hard-to-achieve outlier price. (The close and
open prices on the U.S. primary exchanges are always determined by an
auction, while a transaction at the close on a secondary exchange is not the
result of an auction.)
A similar consideration applies to using high or low prices for your strategy. What were recorded in the historical data are usually the consolidated
highs or lows, not that of the primary exchange. They are often unrepresentative, exaggerated numbers resulting from trades of small sizes on secondary exchanges. Backtest performance will also be infl ated if these historical
prices are used.
Where can we fi nd historical prices from the primary exchanges? Bloomberg users have access to that as part of their subscription. Of course, just as
in the case of storing and using survivorship bias–free data discussed earlier,
we can also subscribe to direct live feeds from the (primary) exchanges and
store those prices into our own databases in real time. We can then use these
databases in the future as our source of primary exchange data. Subscribing
to such feeds independently can be an expensive proposition, but if your
broker has such subscriptions and it redistributes such data to its clients that
colocate within its data center, the cost can be much lower. Unfortunately,
most retail brokers do not redistribute direct feeds from the exchanges, but
institutional brokers such as Lime Brokerage often do.
If we don’t have access to such data, all we can do is to entertain a healthy
skepticism of our backtest results.
Venue Dependence of Currency Quotes
Compared to the stock market, the currency markets are even more fragmented and there is no rule that says a trade executed at one venue has to be
at the best bid or ask across all the diff erent venues. Hence, a backtest will
--- page 24 ---

11
BACKTESTING AND AUTOMATED EXECUTION
be realistic only if we use historical data extracted from the same venue(s)
as the one(s) we expect to trade on.
There are quotes aggregators such as Streambase that consolidate data
feeds from diff erent venues into one order book. In this case, you may use
the consolidated historical data for backtesting, as long as you can execute
on the venue that formed part of the consolidated order book.
Another feature of currency live quotes and historical data is that trade
prices and sizes, as opposed to bid and ask quotes, are not generally available, at least not without a small delay. This is because there is no regulation that says the dealer or ECN must report the trade price to all market
participants. Indeed, many dealers view transaction information as proprietary and valuable information. (They might be smart to do that because
there are high-frequency strategies that depend on order fl ow information and that require trade prices, as mentioned in Chapter 7. The banks’
forex proprietary trading desks no doubt prefer to keep this information
to themselves.) But using bid-ask quotes for backtesting forex strategies
is recommended anyway, since the bid-ask spreads for the same currency
pair can vary signifi cantly between venues. As a result, the transaction costs
are also highly venue dependent and need to be taken into account in a
backtest.
Short-Sale Constraints
A stock-trading model that involves shorting stocks assumes that those
stocks can be shorted, but often there are diffi  culties in shorting some
stocks. To short a stock, your broker has to be able to “locate” a quantity of
these stocks from other customers or other institutions (typically mutual
funds or other asset managers that have large long positions in many stocks)
and arrange a stock loan to you. If there is already a large short interest out
there so that a lot of the shares of a company have already been borrowed,
or if the fl oat of the stock is limited, then your stock can be “hard to borrow.” Hard to borrow may mean that you, as the short seller, will have to
pay interest to the stock lender, instead of the other way around in a normal
situation. In more extreme cases, hard to borrow may mean that you cannot
borrow the stock in the quantity you desire or at all. After Lehman Brothers
collapsed during the fi nancial crisis of 2008–2009, the U.S. Securities and
Exchange Commission (SEC) banned short sales in all the fi nancial industry stocks for several months. So if your backtesting model shorts stocks
that were hard or impossible to borrow, it may show a wonderful return
--- page 25 ---

12
ALGORITHMIC TRADING
because no one else was able to short the stock and depress its price when
your model shorted it. But this return is completely unrealistic. This renders
short-sale constraints dangerous to backtesting. It is not easy, though, to fi nd
a historically accurate list of hard-to-borrow stocks for your backtest, as this
list depends on which broker you use. As a general rule, small-cap stocks are
aff ected much more by short-sale constraint than are large-cap stocks, and
so the returns of their short positions are much more suspect. Bear in mind
also that sometimes ETFs are as hard to borrow as stocks. I have found, for
example, that I could not even borrow SPY to short in the months after the
Lehman Brothers’ collapse!
An additional short-sale constraint is the so-called “uptick rule” imposed
by the SEC. The original uptick rule was in eff ect from 1938 to 2007, where
the short sale had to be executed at a price higher than the last traded price,
or at the last traded price if that price was higher than the price of the trade
prior to the last. (For Nasdaq stocks, the short sale price must be higher
than the last bid rather than the last trade.) The Alternative Uptick Rule that
took eff ect in 2010 also requires a short sale to have a trade price higher than
the national best bid, but only when a circuit breaker has been triggered. A
circuit breaker for a stock is triggered when that stock traded at 10 percent
lower than its previous close. The circuit breaker is in eff ect for the following day after the initial trigger as well. This eff ectively prevents any short
market orders from being fi lled. So, again, a really accurate backtest that
involves short sales must take into account whether these constraints were
in eff ect when the historical trade was supposed to occur. Otherwise, the
backtest performance will be infl ated.
Futures Continuous Contracts
Futures contracts have expiry dates, so a trading strategy on, say, crude oil
futures, is really a trading strategy on many diff erent contracts. Usually,
the strategy applies to front-month contracts. Which contract is the “front
month” depends on exactly when you plan to “roll over” to the next month;
that is, when you plan to sell the current front contract and buy the contract
with the next nearest expiration date (assuming you are long a contract to
begin with). Some people may decide to roll over 10 days before the current
front contract expires; others may decide to roll over when there is an “open
interest crossover”; that is, when the open interest of the next contract exceeds that of the current front contract. No matter how you decide your
rollover date, it is quite an extra bother to have to incorporate that in your
--- page 26 ---

13
BACKTESTING AND AUTOMATED EXECUTION
trading strategy, as this buying and selling is independent of the strategy and
should result in minimal additional return or profi t and loss (P&L). (P&L, or
return, is certainly aff ected by the so-called “roll return,” but as we discuss
extensively in Chapter 5, roll return is in eff ect every day on every contract
and is not a consequence of rolling over.) Fortunately, most futures historical data vendors also recognize this, and they usually make available what is
known as “continuous contract” data.
We won’t discuss here how you can go about creating a continuous contract yourself because you can read about that on many futures historical
data vendors’ websites. But there is a nuance to this process that you need
to be aware of. The fi rst step in creating a continuous contract is to concatenate the prices of the front-month contract together, given a certain set of
rollover dates. But this results in a price series that may have signifi cant price
gaps going from the last date before rollover to the rollover date, and it will
create a false return or P&L on the rollover date in your backtest.
To see this, let’s say the closing price of the front contract on date T is
p(T ), and the closing price of this same contract on date T + 1 is p(T + 1).
Also, let’s say the closing price of the next nearby contract (also called the
“back” contract) on date T + 1 is q(T + 1). Suppose T + 1 is the rollover date,
so if we are long the front contract, we should sell this contract at the close
at p(T + 1), and then buy the next contract at q(T + 1). What’s the P&L (in
points, not dollars) and return of this strategy on T + 1? The P&L is just
p(T + 1) − p(T ), and the return is ( p(T + 1) − p(T ))/p(T ). But the unadjusted continuous price series will show a price of p(T ) at T, and q(T + 1) at
T + 1. If you calculate P&L and return the usual way, you would have calculated the erroneous values of q(T + 1) − p(T ) and (q(T + 1) − p(T ))/p(T ),
respectively. To prevent this error, the data vendor can typically back-adjust
the data series to eliminate the price gap, so that the P&L on T + 1 is p(T + 1)
− p(T ). This can be done by adding the number (q(T + 1) − p(T + 1)) to
every price p(t) on every date t on or before T, so that the price change and
P&L from T to T + 1 is correctly calculated as q(T + 1) − ( p(T ) + q(T + 1)
− p(T + 1)) = p(T + 1) − p(T ). (Of course, to take care of every rollover,
you would have to apply this back adjustment multiple times, as you go back
further in the data series.)
Is our problem solved? Not quite. Check out what the return is at T + 1
given this adjusted price series: ( p(T + 1) − p(T ))/( p(T ) + q(T + 1) − p(T +
1)), not ( p(T + 1) − p(T))/p(T ). If you back-adjust to make the P&L calculation correct, you will leave the return calculation incorrect. Conversely,
you can back-adjust the price series to make the return calculation correct
--- page 27 ---

14
ALGORITHMIC TRADING
(by multiplying every price p(t) on every date t on or before T by the number q(T + 1)/p(T + 1)), but then the P&L calculation will be incorrect. You
really can’t have both. As long as you want the convenience of using a continuous contract series, you have to choose one performance measurement
only, P&L or return. (If you bother to backtest your strategy on the various
individual contracts, taking care of the rollover buying and selling yourself,
then both P&L and return can be correctly calculated simultaneously.)
An additional diffi  culty occurs when we choose the price back-adjustment
instead of the return back-adjustment method: the prices may turn negative
in the distant past. This may create problems for your trading strategy, and
it will certainly create problems in calculating returns. A common method
to deal with this is to add a constant to all the prices so that none will be
negative.
This subtlety in picking the right back-adjustment method is more important when we have a strategy that involves trading spreads between
diff erent contracts. If your strategy generates trading signals based on the
price diff erence between two contracts, then you must choose the price
back-adjustment method; otherwise, the price diff erence may be wrong and
generate a wrong trading signal. When a strategy involves calendar spreads
(spreads on contracts with the same underlying but diff erent expiration
dates), this back adjustment is even more important. This is because the
calendar spread is a small number compared to the price of one leg of the
spread, so any error due to rollover will be a signifi cant percentage of the
spread and very likely to trigger a wrong signal both in backtest and in live
trading. However, if your strategy generates trading signals based on the
ratio of prices between two contracts, then you must choose the return
back-adjustment method.
As you can see, when choosing a data vendor for historical futures prices,
you must understand exactly how they have dealt with the back-adjustment
issue, as it certainly impacts your backtest. For example, csidata.com uses
only price back adjustment, but with an optional additive constant to prevent prices from going negative, while tickdata.com allows you the option
of choosing price versus return back-adjustment, but there is no option for
adding a constant to prevent negative prices.
Futures Close versus Settlement Prices
The daily closing price of a futures contract provided by a data vendor
is usually the settlement price, not the last traded price of the contract
--- page 28 ---

15
BACKTESTING AND AUTOMATED EXECUTION
during that day. Note that a futures contract will have a settlement price
each day (determined by the exchange), even if the contract has not traded
at all that day. And if the contract has traded, the settlement price is in
general diff erent from the last traded price. Most historical data vendors
provide the settlement price as the daily closing price. But some, such as
vendors that provide tick-by-tick data, may provide actual transaction price
only, and therefore the close price will be the last traded price, if there has
been a transaction on that day. Which price should we use to backtest our
strategies?
In most cases, we should use the settlement price, because if you had
traded live near the close, that would have been closest to the price of your
transaction. The last recorded trade price might have occurred several hours
earlier and bear little relation to your transaction price near the close. This
is especially important if we are constructing a pairs-trading strategy on
futures. If you use the settlement prices to determine the futures spreads,
you are guaranteed to be using two contemporaneous prices. (This is true
as long as the two futures contracts have the same underlying and therefore
have the same closing time. If you are trading intermarket spreads, see the
discussion at the end of this section.) However, if you use the last traded
prices to determine the spread, you may be using prices generated at two
very diff erent times and therefore incorrect. This incorrectness may mean
that your backtest program will be generating erroneous trades due to an
unrealistically large spread, and these trades may be unrealistically profi table in backtest when the spreads return to a correct, smaller value in the
future, maybe when near-simultaneous transactions occur. As usual, an infl ated backtest result is dangerous.
If you have an intraday spread strategy or are otherwise using intraday
futures prices for backtesting a spread strategy, you will need either historical data with bid and ask prices of both contracts or the intraday data on
the spread itself when it is native to the exchange. This is necessary because
many futures contracts are not very liquid. So if we use the last price of every bar to form the spread, we may fi nd that the last prices of contract A and
contract B of the same bar may actually refer to transactions that are quite
far apart in time. A spread formed by asynchronous last prices could not in
reality be bought or sold at those prices. Backtests of intraday spread strategies using the last price of each leg of the spread instead of the last price
of the spread itself will again infl ate the resulting returns. One vendor that
sells intraday historical calendar spread data (both quote and trade prices) is
cqgdatafactory.com.
--- page 29 ---

16
ALGORITHMIC TRADING
There is one general detail in backtesting intermarket spreads that should
not be overlooked. If the contracts are traded on diff erent exchanges, they
are likely to have diff erent closing times. So it would be wrong to form an
intermarket spread using their closing prices. This is true also if we try to
form a spread between a future and an ETF. The obvious remedy of this is
to obtain intraday bid-ask data so that synchronicity is assured. The other
possibility is to trade an ETF that holds a future instead of the future itself.
For example, instead of trading the gold future GC (settlement price set
at 1:30 p.m. ET) against the gold-miners ETF GDX, we can trade the gold
trust GLD against GDX instead. Because both trade on Arca, their closing
prices are set at the same 4:00 p.m. ET.

■Statistical Signiﬁ cance of Backtesting:
Hypothesis Testing
In any backtest, we face the problem of fi nite sample size: Whatever statistical measures we compute, such as average returns or maximum drawdowns,
are subject to randomness. In other words, we may just be lucky that our
strategy happened to be profi table in a small data sample. Statisticians have
developed a general methodology called hypothesis testing to address this
issue.
The general framework of hypothesis testing as applied to backtesting
follows these steps:
 1. Based on a backtest on some fi nite sample of data, we compute a certain statistical measure called the test statistic. For concreteness, let’s say
the test statistic is the average daily return of a trading strategy in that
period.
 2. We suppose that the true average daily return based on an infi nite data
set is actually zero. This supposition is called the null hypothesis.
 3. We suppose that the probability distribution of daily returns is
known. This probability distribution has a zero mean, based on the
null hypothesis. We describe later how we determine this probability
distribution.
 4. Based on this null hypothesis probability distribution, we compute the
probability p that the average daily returns will be at least as large as
the observed value in the backtest (or, for a general test statistic, as
extreme, allowing for the possibility of a negative test statistic). This
probability p is called the p-value, and if it is very small (let’s say smaller
--- page 30 ---

17
BACKTESTING AND AUTOMATED EXECUTION
than 0.01), that means we can “reject the null hypothesis,” and conclude
that the backtested average daily return is statistically signifi cant.
The step in this procedure that requires most thought is step 3. How do
we determine the probability distribution under the null hypothesis? Perhaps we can suppose that the daily returns follow a standard parametric
probability distribution such as the Gaussian distribution, with a mean of
zero and a standard deviation given by the sample standard deviation of the
daily returns. If we do this, it is clear that if the backtest has a high Sharpe
ratio, it would be very easy for us to reject the null hypothesis. This is because the standard test statistic for a Gaussian distribution is none other than
the average divided by the standard deviation and multiplied by the square
root of the number of data points (Berntson, 2002). The p-values for various
critical values are listed in Table 1.1. For example, if the daily Sharpe ratio
multiplied by the square root of the number days ( n) in the backtest is
greater than or equal to the critical value 2.326, then the p-value is smaller
than or equal to 0.01.
This method of hypothesis testing is consistent with our belief that high-
Sharpe-ratio strategies are more statistically signifi cant.
Another way to estimate the probability distribution of the null hypothesis is to use Monte Carlo methods to generate simulated historical
price data and feed these simulated data into our strategy to determine
the empirical probability distribution of profits. Our belief is that the
profitability of the trading strategy captured some subtle patterns or
correlations of the price series, and not just because of the first few
moments of the price distributions. So if we generate many simulated
price series with the same first moments and the same length as the
actual price data, and run the trading strategy over all these simulated
price series, we can find out in what fraction p of these price series
are the average returns greater than or equal to the backtest return.
TABLE 1.1
Critical Values for
×
n Daily Sharpe Ratio
p-value
Critical values
0.10
1.282
0.05
1.645
0.01
2.326
0.001
3.091
Source: Berntson (2002).
--- page 31 ---

18
ALGORITHMIC TRADING
Ideally, p will be small, which allows us to reject the null hypothesis.
Otherwise, the average return of the strategy may just be due to the
market returns.
A third way to estimate the probability distribution of the null hypothesis is suggested by Andrew Lo and his collaborators (Lo, Mamaysky, and
Wang, 2000). In this method, instead of generating simulated price data,
we generate sets of simulated trades, with the constraint that the number
of long and short entry trades is the same as in the backtest, and with the
same average holding period for the trades. These trades are distributed
randomly over the actual historical price series. We then measure what
fraction of such sets of trades has average return greater than or equal to
the backtest average return.
In Example 1.1, I compare these three ways of testing the statistical signifi cance of a backtest on a strategy. We should not be surprised that they
give us diff erent answers, since the probability distribution is diff erent in
each case, and each assumed distribution compares our strategy against a
diff erent benchmark of randomness.
Example 1.1: Hypothesis Testing on a Futures
Momentum Strategy
We apply the three versions of hypothesis testing, each with
a diff erent probability distribution for the null hypothesis, on
the backtest results of the TU momentum strategy described in
Chapter 6. That strategy buys (sells) the TU future if it has a positive
(negative) 12-month return, and holds the position for 1 month. We
pick this strategy not only because of its simplicity, but because it has
a fi xed holding period. So for version 3 of the hypothesis testing, we
need to randomize only the starting days of the long and short trades,
with no need to randomize the holding periods.
The fi rst hypothesis test is very easy. We assume the probability
distribution of the daily returns is Gaussian, with mean zero as
befi tting a null hypothesis, and with the standard deviation given by
the standard deviation of the daily returns given by our backtest. So
if ret is the Tx1 MATLAB© array containing the daily returns of the
strategy, the test statistic is just
mean(ret)/std(ret)*sqrt(length(ret))
--- page 32 ---

19
BACKTESTING AND AUTOMATED EXECUTION
Example 1.1 (Continued)
which turns out to be 2.93 for our data set. Comparing this test
statistic with the critical values in Table 1.1 tells us that we can reject
the null hypothesis with better than 99 percent probability.
The second hypothesis test involves generating a set of random,
simulated daily returns data for the TU future (not the daily returns
of the strategy) for the same number of days as our backtest. These
random daily returns data will have the same mean, standard
deviation, skewness, and kurtosis as the observed futures returns,
but, of course, they won’t have the same correlations embedded
in them. If we fi nd there is a good probability that the strategy can
generate an as good as or better return on this random returns series
as the observed returns series, it would mean that the momentum
strategy is not really capturing any momentum or serial correlations
in the returns at all and is profi table only because we were lucky that
the observed returns’ probability distribution has a certain mean and
a certain shape. To generate these simulated random returns with the
prescribed moments, we use the pearsrnd function from the MATLAB
Statistics Toolbox. After the simulated returns marketRet_sim are
generated, we then go on to construct a simulated price series cl_sim
using those returns. Finally, we run the strategy on these simulated
prices and calculate the average return of the strategy. We repeat
this 10,000 times and count how many times the strategy produces
an average return greater than or equal to that produced on the
observed data set.
Assuming that marketRet is the Tx1 array containing the
observed daily returns of TU, the program fragment is displayed
below. (The source codes for these tests can be downloaded as
TU_mom_hypothesisTest.m from www.wiley.com/go/algotrading.)
moments={mean(marketRet), std(marketRet), ...
 skewness(marketRet), kurtosis(marketRet)};
numSampleAvgretBetterOrEqualObserved=0;
for sample=1:10000
marketRet_sim=pearsrnd(moments{:}, length(marketRet), 1);
cl_sim=cumprod(1+marketRet_sim)-1;
longs_sim=cl_sim > backshift(lookback, cl_sim) ;
shorts_sim=cl_sim < backshift(lookback, cl_sim) ;
(Continued )
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
