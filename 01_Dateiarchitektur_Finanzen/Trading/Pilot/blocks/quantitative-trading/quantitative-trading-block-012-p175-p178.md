# Quantitative Trading_ How to Build Your Own Algorithmic -- Ernest P_ Chan -- Wiley Trading, 1, 2008 -- John Wiley & Sons, Ltd_ -- isbn13 9780470284889 -- e4d660df1c1a75e8676a28ff4f852fa7 -- Anna’s Archive.pdf — Chapter 7: Special Topics in Quantitative Trading (pages 175–178)

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
--- page 176 ---

154
QUANTITATIVE TRADING
is proportional to the Sharpe ratio squared, and not to the average
return. So if the two hypothetical portfolios have the same average
return, then we would prefer the one that has the smaller risk or
standard deviation. Empirical studies have found that a portfolio
that consists of low-beta stocks generally has lower risk and thus
a higher Sharpe ratio.
For example, in a paper titled “Risk Parity Portfolios” (not publicly distributed), Dr. Edward Qian at PanAgora Asset Management
argued that a typical 60–40 asset allocation between stocks and
bonds is not optimal because it is overweighted with risky assets
(stocks in this case). Instead, to achieve a higher Sharpe ratio while
maintaining the same risk level as the 60–40 portfolio, Dr. Qian recommended a 23–77 allocation while leveraging the entire portfolio
by 1.8.
Somehow, the market is chronically underpricing high-beta
stocks. Hence, given a choice between a portfolio of high-beta
stocks and a portfolio of low-beta stocks, we should prefer the lowbeta one, which we can then leverage up to achieve the maximum
compounded growth rate.
There is one usual caveat, however. All this is based on the Gaussian assumption of return distributions. (See discussions in Chapter
6 on this issue.) Since the actual returns distributions have fat tails,
one should be quite wary of using too much leverage on normally
low-beta stocks.
SUMMARY
This book has been largely about a particular type of quantitative
trading called statistical arbitrage in the investment industry. Despite this fancy name, statistical arbitrage is actually far simpler
than trading derivatives (e.g., options) or ﬁxed-income instruments,
both conceptually and mathematically. I have described a large part
of the statistical arbitrageur’s standard arsenal: mean reversion and
momentum, regime switching, stationarity and cointegration, arbitrage pricing theory or factor model, seasonal trading models, and,
ﬁnally, high-frequency trading.
--- page 177 ---

Special Topics in Quantitative Trading
155
Some of the important points to note can be summarized here:
r Mean-reverting regimes are more prevalent than trending
regimes.
r There are some tricky data issues involved with backtesting
mean-reversion strategies: Outlier quotes and survivorship bias
are among them.
r Trending regimes are usually triggered by the diffusion of new
information, the execution of a large institutional order, or
“herding” behavior.
r Competition between traders tends to reduce the number of
mean-reverting trading opportunities.
r Competition between traders tends to reduce the optimal holding period of a momentum trade.
r Regime switching can sometimes be detected using a dataminingx approach with numerous input features.
r A stationary price series is ideal for a mean-reversion trade.
r Two or more nonstationary price series can be combined to
form a stationary one if they are “cointegrating.”
r Cointegration and correlation are different things: Cointegration
is about the long-term behavior of the prices of two or more
stocks, while correlation is about the short-term behavior of
their returns.
r Factor models, or arbitrage pricing theory, are commonly used
for modeling how fundamental factors affect stock returns linearly.
r One of the most well-known factor models is the Fama-French
Three-Factor model, which postulates that stock returns are
proportional to their beta and book-to-price ratio, and negatively
to their market capitalizations.
r Factor models typically have a relatively long holding period and
long drawdowns due to regime switches.
r Exit signals should be created differently for mean-reversion
versus momentum strategies.
r Estimation of the optimal holding period of a mean-reverting
strategy can be quite robust, due to the Ornstein-Uhlenbeck formula.
--- page 178 ---

156
QUANTITATIVE TRADING
r Estimation of the optimal holding period of a momentum strategy can be error prone due to the small number of signals.
r Stop loss can be suitable for momentum strategies but not reversal strategies.
r Seasonal trading strategies for stocks (i.e., calendar effect) have
become unproﬁtable in recent years.
r Seasonal trading strategies for commodity futures continue to
be proﬁtable.
r High-frequency trading strategies rely on the “law of large numbers” for their high Sharpe ratios.
r High-frequency trading strategies typically generate the highest
long-term compounded growth due to their high Sharpe ratios.
r High-frequency trading strategies are very difﬁcult to backtest
and very technology reliant for their execution.
r Holding a highly leveraged portfolio of low-beta stocks should
generate higher long-term compounded growth than holding unleveraged portfolio of high-beta stocks.
Most statistical arbitrage trading strategies are some combination of these effects or models: Whether they are proﬁtable or not
is more of an issue of where and when to apply them than whether
they are theoretically correct or not.
