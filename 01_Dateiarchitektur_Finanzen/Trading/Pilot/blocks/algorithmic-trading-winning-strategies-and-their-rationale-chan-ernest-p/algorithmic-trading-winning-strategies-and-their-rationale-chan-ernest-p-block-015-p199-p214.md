# Algorithmic Trading (Winning Strategies and Their Rationale) -- Chan, Ernest P_ -- 2013 may 22 -- John Wiley & Sons, Inc_ -- doi 10_1002_9781118676998 -- e374e4354dcd660c7bc666e0297a580b -- Anna’s Archive.pdf — Chapter 8: Chapter 8 (pages 199–214)

--- page 199 ---

188
CONCLUSION
cointegrating in 2008 (see Chapter 4). A hypothesis was formed that had
to do with the high crude oil price. When oil price was added to the input
variables, the cointegration model started to work again. This scientifi c process is most helpful when a strategy underperforms the backtest, and we
wanted to know why. Instead of blindly adding more rules, more indicators,
to the model and hoping that they miraculously improve the model performance, we should look for a fundamental reason and then quantitatively test
whether this fundamental reason is valid.
Despite the eff orts to make the trading process scientifi c and rule based,
there are still areas where subjective judgment is important. For example,
when there is a major event looming, do you trust that your model will behave as your backtest predicted, or do you lower your leverage or even temporarily shut down the model in anticipation? Another example is off ered
by the application of the Kelly formula to a portfolio of strategies. Should
we allocate capital among these strategies based on the equity of the whole
portfolio, so that the good performance of some strategies is subsidizing
the poor performance of others in the short term? Or should we apply the
Kelly formula to each strategy on its own, so that we quickly deleverage
those strategies that perform poorly recently? Mathematics tells us that the
former solution is optimal, but that’s assuming the expected returns and
volatilities of the strategies are unchanging. Can one really say that such expectations are unchanged given a recent period of severe drawdown?
(On the fi rst judgment call, my experience has been that if your model
has survived the backtest during prior stressful periods, there is no reason
to lower its leverage in the face of coming crisis. It is much better to start off
with a more conservative leverage during good times than to have to lower
it in bad ones. As Donald Rumsfeld once said, it is the “unknown unknowns”
that will harm us, not the “known unknowns.” Unfortunately, we can’t shut
down our models before the unknown unknowns strike. On the second
judgment call, my experience has been that applying Kelly to each strategy
independently so as to allow each one to wither and die quickly when it
underperforms is more practical than applying Kelly asset allocation across
all strategies.)
As these examples show, subjective judgment is often needed because
the statistical properties of fi nancial time series are not stationary, and science can really only deal with stationary statistics. (I am using stationary in
a sense diff erent from the stationarity of time series in Chapter 2. Here, it
means the probability distribution of prices remains unchanged throughout time.) Often, when we fi nd that our live trading experience diverges
--- page 200 ---

189
CONCLUSION
from the backtest, it is not because we committed any of the pitfalls during
backtesting. It is because there has been a fundamental change in the market
structure, a regime shift, due to government regulatory or macroeconomic
changes. So the fund managers still have an active ongoing role even if the
strategy is supposedly algorithmic and automated—their role is to make judicious high-level judgment calls based on their fundamental understanding
of the markets on whether the models are still valid.
However, the fact that judgment is sometimes needed doesn’t mean
that developing quantitative rules is useless or algorithmic traders are less
“smart” than discretionary traders. As the oft-quoted Daniel Kahneman
wrote, experts are uniformly inferior to algorithms in every domain that has a
signifi cant degree of uncertainty or unpredictability, ranging from deciding
winners of football games to predicting longevity of cancer patients. One
can hope that the fi nancial market is no exception to this rule.
--- page 201 ---

191
B I B L I O G R A P H Y
Arnuk, Sal L., and Joseph C. Saluzzi. Broken Markets: How High Frequency
Trading and Predatory Practices on Wall Street Are Destroying Investor Confi -
dence and Your Portfolio. Upper Saddle River, NJ: FT Press, 2012.
Beckert, Walter. Course notes on Financial Econometrics, Birkbeck
University of London, 2011. Available at www.ems.bbk.ac.uk/for
_students/bsc_FinEcon/fi n_economEMEC007U/adf.pdf.
Bernard, Victor L., and Jacob K. Thomas. “Post-Earnings-Announcement
Drift: Delayed Price Response or Risk Premium?” Journal of Accounting
Research 27 (1989): 1–36.
Berntson, M. “Steps in Signifi cance/Hypothesis Testing Using the Normal
Distribution.” Course notes for Introduction to Sociology, Grinnell
College, 2002. Available at http://web.grinnell.edu/courses/sst/s02
/sst115-03/practice/hypothesisteststeps1.pdf.
Bollen, Johan, Huina Mao, and Xiao-Jun Zeng. “Twitter Mood Predicts the
Stock Market,” 2010.  Available at http://arxiv.org/pdf/1010.3003.pdf.
Bryant, Martin. “Investment Fund Set to Use Twitter to Judge Emotion in
the Market,” The Next Web, December 16, 2010. Available at http://
thenextweb.com/uk/2010/12/16/investment-fund-set-to-use
-twitter-to-judge-emotion-in-the-market/.
Buy the Hype, “The ‘Twitter Hedge Fund’ Has an Out-of-Sample Experience,” Buy the Hype (blog), May 3, 2012. Available at http://sellthenews
.tumblr.com/post/22334483882/derwents-performance.
Chan, Ernest. Quantitative Trading: How to Build Your Own Algorithmic Trading
Business. Hoboken, NJ: John Wiley & Sons, 2009.
Algorithmic Trading: Winning Strategies and Their Rationale. Ernest P. Chan.
© 2013 Ernest P. Chan. Published 2013 by John Wiley & Sons, Inc.
--- page 202 ---

192
BIBLIOGRAPHY
Cheng, Minder, and Ananth Madhavan. “The Dynamics of Leveraged and Inverse Exchange-Traded Funds.” Journal of Investment Management, Winter
2009. Available at SSRN: http://ssrn.com/abstract=1393995.
Clare, Andrew, and Roger Courtenay. “What Can We Learn about Monetary
Policy Transparency from Financial Market Data?” Economic Research
Centre of the Deutsche Bundesbank, 2001. Available at www.olsen
.ch/fi leadmin/Publications/Client_Papers//200102-ClareCourtenay
-WhatLearnMonetaryPolTransparencyFinMkts.pdf.
Coval, Joshua, and Erik Staff ord. “Asset Fire Sales (and Purchases) in Equity
Markets.” Journal of Financial Economics 86 (2007): 479–512. Available at
www.people.hbs.edu/estaff ord/Papers/AFS.pdf.
Daniel, Ken, and Tobias Moskowitz. “Momentum Crashes.” Preprint,
2011. Available at www.columbia.edu/~kd2371/papers/unpublished
/mom4.pdf.
Dever, Michael. Jackass Investing. Thornton, PA: Ignite LLC, 2011.
Dueker, Michael J., and Christophe r J. Neely. “Can Markov Switching Models
Predict Excess Foreign Exchange Returns?” Federal Reserve Bank of
St. Louis Working Paper 2001-021F, 2001. Available at http://research
.stlouisfed.org/wp/2001/2001-021.pdf.
Dupoyet, Brice, Robert T. Daigler, and Zhiyao Chen. “A Simplifi ed Pricing
Model for Volatility Futures.” Journal of Futures Markets 31, no. 4 (2011):
307–339. Available at www2.fi u.edu/~dupoyetb/vix_futures.pdf.
Durbin, Michael. All About High-Frequency Trading. New York: McGraw-Hill,
2010.
Durden, Tyler. “Why the Market Is Slowly Dying,” Zero Hedge (blog), April
14, 2012, www.zerohedge.com/news/why-market-slowly-dying.
Engle, R. F., and C. W. Granger.  “Co-integration and Error-Correction: Representation, Estimation, and Testing.” Econometrica 55 (1987): 251–276.
Erb, Claude B., and Campbell R. Harvey. “The Strategic and Tactical Value
of Commodity Futures.” Financial Analysts Journal 62, no. 20 (2006):
69. Available at http://ciber.fuqua.duke.edu/~charvey/Research
/Published_Papers/P91_The_strategic_and.pdf.
Falkenberry, Thomas N. “High Frequency Data Filtering,” 2002. Available at
www.tickdata.com/pdf/Tick_Data_Filtering_White_Paper.pdf.
Fama, Eugene F., and Marshall E. Blume. “Filter Rules and Stock-Market
Trading.” Journal of Business 39, no. 1 (1966): 226–231. Available at
www.e-m-h.org/FaBl66.pdf.
Friedman, Thomas. “A Good Question.” New York Times Op-ed, February
25, 2012.
--- page 203 ---

193
BIBLIOGRAPHY
Gill, Jeff . “The Insignifi cance of Null Hypothesis Signifi cance Testing.” Political Research Quarterly 52, no. 3 (1999): 647–674. Available at
www.artsci.wustl.edu/~jgill/papers/hypo.pdf.
Greenblatt, Joel. The Little Book that Beats the Market. Hoboken, NJ: John
Wiley & Sons, 2006. Also see magicformulainvesting.com.
Hafez, Peter A. “Event Trading Using Market Response,” July 22, 2011,
www.ravenpack.com/research/marketresponsepaperform.htm.
Hafez, Peter A., and Junqiang Xie. “Short-Term Stock Selection Using
News Based Indicators,” May 15, 2012, www.ravenpack.com/research
/shorttermstockselectionpaperform.htm.
Harris, Larry. Trading and Exchanges. New York: Oxford University Press,
2003.
Hellström, Jörgen, and Ola Simonsen. “Does the Open Limit Order Book
Reveal Information About Short-run Stock Price Movements?” Umeå
Economic Studies, 2006.
Hull, John C. Options, Futures, and Other Derivatives, 3rd ed. Upper Saddle
River, NJ: Prentice-Hall, 1997.
Johnson, Barry. Algorithmic Trading & DMA. London: 4Myeloma Press,
2010.
Kahneman, Daniel. Thinking, Fast and Slow. New York: Farrar, Straus and
Giroux. 2011.
Khandani, Amir, and Andrew Lo. “What Happened to the Quants in August
2007?” Preprint, 2007. Available at http://web.mit.edu/alo/www
/Papers/august07.pdf.
Kleeman, Lindsay. “Understanding and Applying Kalman Filtering.” Course
notes on Robotic Motion Planning, Carnegie Mellon University, 2007.
Available at www.cs.cmu.edu/~motionplanning/papers/sbp_papers
/integrated3/kleeman_kalman_basics.pdf.
Kozola, Stuart. “Automated Trading with MATLAB-2012.” Webinar, 2012.
www.mathworks.com/matlabcentral/fi leexchange/37932-automated
-trading-with-matlab-2012.
Kuznetsov, Jev. “ActiveX vs Java API What’s the Diff erence?” Quantum blog,
November 25, 2010, http://matlab-trading.blogspot.ca/2010/11
/activex-vs-java-api-whats-diff erence.html.
LeSage, James P. “Spatial Econometrics,” 1998. Available at www.spatialeconometrics.com/html/wbook.pdf.
Lo, Andrew W., and A. Craig MacKinlay. A Non-Random Walk Down Wall Street.
Princeton, NJ: Princeton University Press, 2001.
--- page 204 ---

194
BIBLIOGRAPHY
Lo, Andrew W., Harry Mamaysky, and Jiang Wang. “Foundations of Technical
Analysis: Computational Algorithms, Statistical Inference, and Empirical Implementation.” Journal of Finance 55, no. 4 (2000): 1705–1770.
Available at http://ideas.repec.org/p/nbr/nberwo/7613.html.
Lyons, Richard. The Microstructure Approach to Exchange Rates. Cambridge,
MA: MIT Press, 2001.
Malkiel, Burton. A Random Walk Down Wall Street: The Time-Tested Strategy for
Successful Investing. New York: W. W. Norton, 2008.
Maslov, Sergei, and Mark Mills. “Price Fluctuations from the Order Book
Perspective: Empirical Facts and a Simple Model.” Physica A 299, no.
1–2 (2001): 234–246.
Montana, Giovanni, Kostas Triantafyllopoulos, and Theodoros Tsagaris.
“Flexible Least Squares for Temporal Data Mining and Statistical
Arbitrage.” Expert Systems with Applications 36 (2009): 2819–2830. Available
at
www2.econ.iastate.edu/tesfatsi/FLSTemporalDataMining
.GMontana2009.pdf.
Moskowitz, Tobias, Hua Ooi Yao, and Lasse Heje Pedersen. “Time Series
Momentum.” Journal of Financial Economics 104, no. 2 (2012): 228–250.
Osler, Carol. “Support for Resistance: Technical Analysis and Intraday Exchange Rates.” Federal Reserve Bank of New York Economic Policy Review 6
(July 2000): 53–65.
Osler, Carol. “Currency Orders and Exchange-Rate Dynamics: An Explanation for the Predictive Success of Technical Analysis,” 2001. Forthcoming, Journal of Finance. Available at http://newyorkfed.org/research
/staff _reports/sr125.pdf.
Patterson, Scott. The Quants. New York: Crown Business, 2010.
Philips, Matthew. “Unlocking the Crude Oil Bottleneck at Cushing.”
Bloomberg Business Week, May 16, 2012. Available at www.businessweek
.com/articles/2012-05-16/unlocking-the-crude-oil-bottleneck-atcushing#p1.
Rajamani, Murali. “Data-Based Techniques to Improve State Estimation
in Model Predictive Control.” PhD thesis, University of Wisconsin-
Madison, 2007.
Rajamani, Murali R., and James B. Rawlings.  “Estimation of the Disturbance
Structure from Data Using Semidefi nite Programming and Optimal
Weighting. Automatica 45 (2009): 142–148.
Reverre, Stephane. The Complete Arbitrage Deskbook. New York: McGraw-Hill,
2001.
--- page 205 ---

195
BIBLIOGRAPHY
Rodier, Arthur, Edgar Haryanto, Pauline M. Shum, and Walid Hejazi.  “Intraday Share Price Volatility and Leveraged ETF Rebalancing.”  October
2012. Available at SSRN: http://ssrn.com/abstract=2161057.
Schoenberg, Ron, and Alan Corwin. “Does Averaging-in Work?” 2010.
www.optionbots.com/DOE/does_averaging_in_work.pdf. Accessed
January 10, 2010.
Serge, Andrew. “Where Have All the Stat Arb Profi ts Gone?” Columbia University Financial Engineering Practitioners Seminars, January 2008.
Shankar, S. Gowri, and James M. Miller. “Market Reaction to Changes in the
S&P SmallCap 600 Index.” Financial Review 41, no. 3 (2006): 339–360.
Available at SSRN: http://papers.ssrn.com/sol3/papers.cfm?abstract
_id=886141.
Simon, David P., and Jim Campasano. “The VIX Futures Basis: Evidence and Trading Strategies,” 2012. Available at SSRN: http://papers.ssrn.com/sol3
/papers.cfm?abstract_id=2094510.
Sinclair, Euan. Option Trading: Pricing and Volatility Strategies and Techniques.
Hoboken, NJ: John Wiley & Sons, 2010.
Snider, Connan Andrew, and Thomas Youle. “Does the LIBOR Refl ect
Banks’ Borrowing Costs?” 2010.  Available at SSRN: http://papers
.ssrn.com/sol3/papers.cfm?abstract_id=1569603.
Sorensen, Bent E. Course notes on Economics. University of Houston,
2005. Available at www.uh.edu/~bsorense/coint.pdf.
“The Wacky World of Gold.” The Economist, June 2011.
Thorp, Edward.  “The Kelly Criterion in Blackjack, Sports Betting, and the
Stock Market,” 1997. Available at www.EdwardOThorp.com.
--- page 206 ---

197
A B O U T T H E A U T H O R
E
rnest Chan is the managing member of QTS Capital Management, LLC,
a commodity pool operator. Ernie has worked for various investment
banks (Morgan Stanley, Credit Suisse, Maple) and hedge funds (Mapleridge,
Millennium Partners, MANE) since 1997. He received his PhD in physics from Cornell University and was a member of IBM’s Human Language
Technologies group before joining the fi nancial industry. He was a cofounder and principal of EXP Capital Management, LLC, a Chicago-based investment fi rm. He is also the author of Quantitative Trading: How to Build  Your Own
Algorithmic Trading Business, published by John Wiley & Sons in 2009, and a
popular fi nancial blogger at http://epchan.blogspot.com. Find out more
about Ernie at www.epchan.com.
Algorithmic Trading: Winning Strategies and Their Rationale. Ernest P. Chan.
© 2013 Ernest P. Chan. Published 2013 by John Wiley & Sons, Inc.
--- page 207 ---

199
A B O U T T H E W E B S I T E
A
ll of the examples in this book are built around MATLAB codes,
and they are all available for download from www.wiley.com/go
/algotrading (password: chan2E). Once redirected to the website with the
codes, you will be asked for another username and password—use “kelly”
for both. Readers unfamiliar with MATLAB may want to study the tutorial
in Quantitative Trading, or watch the free webinars on www.mathworks.com.
Furthermore, the MATLAB Statistics Toolbox was occasionally used. (All
MATLAB products are available as free trials from MathWorks.)
For more from the author on the topic of algorithmic trading and more,
go to www.epchan.com or http://epchan.blogspot.com.
Algorithmic Trading: Winning Strategies and Their Rationale. Ernest P. Chan.
© 2013 Ernest P. Chan. Published 2013 by John Wiley & Sons, Inc.
--- page 208 ---

201
I N D E X
Accenture, 183
ADF (augmented Dickey-Fuller) test, 41,
42–44
Alexander Filter, 140
Alternative Uptick Rule, 12, 90, 92
APIs (application programming interfaces)
for automatic execution, 29
for news-driven trading, 36
Arbitrage
between ETF and component stocks, 96–102
future and ETF, extracting roll returns
through, 141–144
Asset classes supported by special-purpose
platforms, 31–36
Augmented Dickey-Fuller (ADF) test, 41,
42–44
Automated execution platform
backtesting with, 30–31
choosing, 25
FXone, 26–27
high-frequency trading and, 32, 34–35
news-driven trading and, 35–36
programming skill and choice of, 25–29
Averaging-in, 48, 72–74
Back-adjustment methods, 14
Backtesting
currency arbitrage strategies, 112–113
danger of data errors to, 83–84
deciding not to use, 22–24
dividend adjustments and, 7–8
futures and, 12–16, 100
high-frequency strategies, 23–24, 30, 32,
34–35
IDEs for, 29, 31
importance of, 2–3
intermarket spread strategies, 129
intraday spread strategies, 15
leading risk indicators, 186
linear mean-reverting strategies, 59–60
live trading experience diverging from,
188–189
post-earnings announcement drift strategies,
160–161
predictive power of, 24–25
software platform for, 1–2
stationarity tests compared to, 50
statistical signifi cance of, 1, 16–22
tick-based strategies, 30
See also Pitfalls of backtesting; Software
platform for backtesting
Backwardation, 115–122
Bamberger, Gerry, 89
Base currency, 108
Beckert, Walter, 41
Bias
data-snooping, 4–7, 60, 186
look-ahead, 4
survivorship, 8–9, 23, 88, 183
Black swan events and momentum strategies,
153
Bloomberg Event-Driven Trading, 148–149
Bollinger bands, 70–72
Breakout strategies, 155
Algorithmic Trading: Winning Strategies and Their Rationale. Ernest P. Chan.
© 2013 Ernest P. Chan. Published 2013 by John Wiley & Sons, Inc.
--- page 209 ---

202
INDEX
Brokerage order confi rmation latency, 32, 34
Buy-on-gap model, 92–96
CADF (cointegrated augmented Dickey-Fuller)
test, 51–54
Calendar spreads, trading
mean reversion trading, 123–127
roll returns, backwardation, and contango,
115–122
Calendar spreads and back adjustment, 14
Center for Research in Security Prices (CRSP),
150
Closing prices of futures contracts, 14–16
Cointegrated augmented Dickey-Fuller (CADF)
test, 51–54
Cointegration and mean reversion
Johansen test, 54–58
linear mean-reverting trading strategy, 58–60
overview, 50–51
Colocation of trading programs, 33–34
Commodities, normal, 117
Commodity currencies, 108
Commodity ETFs, cointegration of, 91
Complex event processing, 36
Compounded growth rate, computing optimal
leverage to maximize, 170–171
Constant leverage requirement, implications
of, 171
Constant proportion portfolio insurance
(CPPI), 180–182
Constant returns model for estimating spot and
roll returns, 119–122
Constrained optimization method, 101–102
Constraints
maximum leverage, optimal capital allocation
under, 174–175
short-sale, 11–12, 89–90, 102
Contango, 115–122
Continuous contracts, 13–14
Correlation coeffi  cient for time series
momentum, 134, 135–136
Country ETFs, cointegration of, 91
CPPI (constant proportion portfolio insurance),
180–182
Cqgdatafactory.com website, 15
Crack spread portfolio, 128
Cross-sectional mean reversion, 41, 88,
102–105
Cross-sectional momentum, defi ned, 133–134
Cross-sectional momentum strategies
mutual funds asset fi re sale and forced
purchases, 149–151
news sentiment as fundamental factor,
148–149
overview, 144–145, 147–148
for stocks, 146–147
CRSP (Center for Research in Security Prices),
150
Crsp.com website, 9
Csidata.com website, 9, 14
Currencies
opening gap strategy for, 156, 157
pairs trading strategy for, 66
Currencies, mean reversion of
overview, 107–108
rollover interests in, 113–115
trading cross-rates, 108–113
Currency quotes, venue dependence of,
10–11
Data errors, danger of to backtesting and meanreversion strategies, 83–84
Data-snooping bias, 4–7, 60, 186
Delisted stocks, 9
Deltix, 26, 28, 29, 35
Dever, Michael, 61, 140–141
Dividend adjustments and backtesting, 7–8
Dow Jones
Elementized News Feeds, 149
newswire, 162
STOXX 50 index futures (FSTX), opening
gap strategy for, 156–157
Drift
due to other events, 162–163
post-earnings announcement, 153, 158–162
Dynamic linear regression, Kalman fi lter as,
74–82
Earnings announcements, price momentum
generated by, 153, 158–162
Earnings.com website
function for retrieving earnings calendar
from, 158–160
information available of, 8
Eigen statistic, 55
EMA (exponential moving average), 75
Equity index futures, 129–131, 143–144
Excess return, 113
--- page 210 ---

203
INDEX
Exchange-traded funds (ETFs)
composition changes in, 162–163
extracting roll returns through arbitrage,
141–144
leveraged ETF strategy, 163–164
Exchange-traded funds (ETFs), mean reversion
of
arbitrage between ETF and component
stocks, 96–102
overview, 87–88
trading currency pairs compared to, 108
trading ETF pairs and triplets, 91–92
Exit strategies for momentum strategies, 153
Expected growth rate, optimization of using
simulated returns, 173–177
Exponential moving average (EMA), 75
Falkenberry, Thomas, 84
Financial Information eXchange (FIX) protocol,
29, 31
Flash crash, 183
Flipping strategy, 166
Forced purchases, 149–151, 162–163
Front-month contracts, 12
Front-running strategy for mutual funds, 150
FSTX, opening gap strategy for, 156–157
Futures
extracting roll returns through arbitrage,
141–144
hypothesis testing on momentum strategy
for, 18–21
opening gap strategy for, 156–157
time series momentum strategy for,
139–140
See also Futures and backtesting
Futures, mean reversion of
overview, 107–108
trading calendar spreads, 115–127
trading intermarket spreads, 127–131
Futures and backtesting
close compared to settlement prices, 14–16,
100
continuous contracts, 12–14
FXone automated execution platform, 26–27
Gaussian assumption and Kelly formula, 172–173
Gaussian distribution, 5, 17
Geometric random walk, 89
Greenblatt, Joel, 7
Half-Kelly leverage, 172
Hard-to-borrow stocks, 11–12
Hedge ratio
of asset, 51
dynamic daily recalculation of, 67
for pair of cointegrating price series, 74
for pair of real price series, 74–75
Heisenberg uncertainty principle, 24, 35
Hicks, John, 117
High-frequency strategies
backtesting, 23–24, 30, 32, 34–35
index arbitrage, 97
intraday momentum, 164–168
Historical growth rate, optimization of,
177–178
Hurst exponent
for time series momentum, 134, 135
Variance Ratio Test and, 41, 44–46
Hypothesis testing
as approach to trading, 92, 187–188
statistical signifi cance of backtesting, 16–22
IDEs (integrated development environments)
for backtesting, 29, 31
complex event processing and, 36
for news-driven trading, 35
Imbalance of bid and ask sizes, 164
Index arbitrage, 87–88, 96–102
Index funds, composition changes in, 162–163
Integrated development environments.
See IDEs
Interday momentum strategies
cross-sectional, 144–151
extracting roll returns through future and
ETF arbitrage, 141–144
overview, 133–134
pros and cons of, 151–154
tests for time series momentum, 134–137
time series, 137–141
Intermarket spread strategies
backtesting, 129
futures, 127–131
Intraday mean reversion, 92–96
Intraday momentum strategies
high-frequency, 164–168
leveraged ETF, 163–164
news-driven, 157–163
opening gap, 156–157
overview, 155–156
--- page 211 ---

204
INDEX
Intraday spread strategies, backtesting, 15
Intraday trading of stock pairs, 90
Johansen eigenvector, pair trading currencies
using, 110–112
Johansen test
for creating long-only portfolio, 101
mean reversion and, 54–58
trading cross-rates and, 109
Judgment, importance of, 188–189
Kahneman, Daniel
on experts compared to algorithms, 189
on Sports Illustrated jinx, 39
Thinking, Fast and Slow, 7
Kalman fi lter
as dynamic linear regression, 74–77, 78–82
iterative equations of, 77–78
as market-making model, 82–83
Kelly formula, 172–173
Keynes, John Maynard, 117
Kibot.com website, 9
Lagged roll returns, 140
Leading risk indicators, 184–186
Leverage and risk management, 170–171
Leveraged ETF strategy, 163–164
Linear mean-reverting trading strategies
described, 48–50
limitations of, 70
long-short, 102–105
on portfolio, 58–60
Linear trading models and data-snooping bias,
4–7
Live bid/ask quotes, erroneous, 84
Live market data latency, 32
Lo, Andrew, 18, 103
Log future prices and trading calendar spreads,
116–117
Log price spreads, trading pairs using, 64–70
Look-ahead bias, 4
Market-making model, Kalman fi lter as,
82–83
Markets, ineffi  ciencies of, 187
MATLAB scripting language, 28–29, 35
Maximum drawdown, 179–180
Maximum leverage constraint, optimal capital
allocation under, 174–175
Mean reversion
augmented Dickey-Fuller test, 42–44
cointegrated augmented Dickey-Fuller test,
51–54
cointegration, 50–51
half-life of, 46–48
Hurst exponent and Variance Ratio test,
44–46
Johansen test, 54–58
linear mean-reverting trading strategy,
48–50, 58–60
overview, 39–41
stationarity and, 41
See also Exchange traded funds (ETFs), mean
reversion of; Mean-reversion strategies;
Stocks, mean reversion of
Mean-reversion strategies
Bollinger bands, 70–72
danger of data errors, 83–84
implementing, 63–64
Kalman fi lter as dynamic linear regression,
74–82
Kalman fi lter as market-making model,
82–83
pros and cons of, 60–61, 153
scaling-in, 72–74
stop loss for, 183–184
trading pairs using price spreads, log price
spreads, or ratios, 64–70
Microsoft Excel, 26
Mnemonic for backwardation, 117
Modifi cation of strategies after hypothesis
testing, 92
Momentum, causes of, 133
Momentum fi lter for mean-reversion strategies,
93
Momentum ignition, 166
Momentum strategies
data errors and, 84
fundamental reasoning and, 61
pros and cons of, 151–154
stop loss for, 184
survivorship bias and, 9
See also Interday momentum strategies;
Intraday momentum strategies
Monte Carlo methods
for optimization of expected growth rate,
175–177
for statistical signifi cance, 17–18
--- page 212 ---

205
INDEX
Moving average for mean-reverting strategies,
48–49, 66
Multithreading and high-frequency trading of
multiple symbols, 35
Mutual funds
asset fi re sale, 149–151
composition changes in, 162–163
National best bid and off er (NBBO) quote sizes
for stocks, 90, 166–167
Neural net trading model, 23
News-driven momentum strategies
drift due to other events, 162–163
overview, 157–158
post-earnings announcement drift, 158–162
News-driven trading and special-purpose
platforms, 35–36
News sentiment as fundamental factor,
148–149
Newsware, 148, 162
Nonlinear trading models, approximating, 5
Normal commodities, 117
Null hypothesis, 16
Opening gap strategy, 156–157
Optimal leverage
Kelly formula, 172–173
maximum drawdown, 179–180
optimization of expected growth rate using
simulated returns, 173–177
optimization of historical growth rate,
177–178
overview, 170–171
Order fl ow, ignition of price momentum due
to, 149
Order fl ow information, access to, 167–168, 185
Ornstein-Uhlenbeck formula, 6, 46
Out-of-sample cointegrating stock pairs, 89
Out-of-sample data and data-snooping bias,
4–5, 7
Out-of-sample testing, 187
Overnight, holding position, 113
Overnight gap, 157
Pairs trading strategies
cointegration and, 51
currencies, 66, 108
currencies with rollover interests, 114–115
ETFs, 91–92
intraday, 90
price spreads, log price spreads, and ratios
for, 64–70
stocks, 89–91, 102
Pearson system, 176
P/E (price-earnings) ratio, ranking stocks
using, 104–105
Pitfalls
of mean-reversion strategies, 60–61, 83–84,
153
of momentum strategies, 151–154
of strategies in general, 1, 187
Pitfalls of backtesting
data-snooping bias, 4–7, 60, 186
futures close compared to settlement prices,
14–16, 100
futures continuous contracts, 12–14
look-ahead bias, 4
primary compared to consolidated stock
prices, 9–10
short-sale constraints, 11–12, 89–90, 102
stock splits and dividend adjustments, 7–8
survivorship bias, 8–9, 88
venue dependence of currency quotes, 10–11
Post-earnings announcements, price
momentum generated by, 153,
158–162
Predictive power of backtesting, 24–25
“Prefabricated” fi nancial price series, 39–40, 50
Price-earnings (P/E) ratio, ranking stocks
using, 104–105
Price spreads, trading pairs using, 64–70
Primary exchanges
fi nding historical prices from, 9–10
orders fi lled at, 88
Principal Component Analysis, 147–148
Profi ts from pair trading of stocks, 90–91,
102
Programming skill and choice of software
platform, 25–29
Progress Apama, 26, 28, 29, 35
P-value, 16–17
Python scripting language, 28, 29, 35
QuantHouse, 28, 29
Quantitative Trading (Chan), 147, 172, 173
Quote currency, 108
Quote matching strategy, 165–166
Quotes aggregators, 11
--- page 213 ---

206
INDEX
Ranking stocks
cross-sectional mean reversion and, 104–105
by factors, 7, 147
Ratio trading, 64–70, 165
RavenPack Sentiment Index, 148
Read-Eval-Print-Loop (REPL) languages, 28
Recorded Future, 148
Regime shifts
judgment and, 189
predictive power of backtesting and, 24–25
stop losses and, 183
REPL (Read-Eval-Print-Loop) languages, 28
Returns of diff erent time frames, fi nding
correlations between, 135–137
Risk indicators, 184–186
Risk management
constant proportion portfolio insurance,
180–182
Kelly formula, 172–173
maximum drawdown and, 179–180
for mean-reversion strategies, 61
for momentum strategies, 153–154
optimal leverage and, 170–180
optimization of expected growth rate using
simulated returns, 173–177
optimization of historical growth rate, 177–178
overview, 169
stop losses, 182–184
Rollover dates and futures continuous
contracts, 12–13
Rollover interests in currency trading, 110,
113–115
Roll returns
cross-sectional momentum strategies and, 144
extracting through future and ETF arbitrage,
141–144
futures calendar spread and, 115–122
time series momentum strategies and,
139–140
R scripting language, 28, 29
RTD Tango, 28, 29
Scaling-in, 48, 72–74
Scripting languages, 28–29, 35
Seasonal mean reversion, 63, 87, 92–96
SEC (Securities and Exchange Commission)
short sale ban by, 11
uptick rule of, 12, 90, 92
Sector ETFs, cointegration of, 91
Selling into losses feature of risk management,
171
Sentiment scores from news feeds, 148–149
Settlement prices of futures contracts, 14–16
Sharpe ratio
calculating, 113
long holding periods and, 155
momentum strategies and, 151
statistical signifi cance and, 17
Short-sale constraints
backtesting and, 11–12
index arbitrage and, 102
trading stock pairs and, 89–90
Short squeeze, 90
Signal noise, 95
Simulated returns, optimization of expected
growth rate using, 173–177
Software platform for backtesting
asset classes and strategies supported by,
31–36
choosing, 1–2, 25
complex event processing and, 36
programming skill and choice of, 25–29
special-purpose execution platforms and,
30–31
Spot returns, estimating, 118–122
Spread, 59
SPY ETF, index arbitrage example using,
97–102, 143
Standard deviation for mean-reverting
strategies, 48–49, 66
Standard & Poor’s Diversifi ed Trends Indicator,
140–141, 151, 152
State transition model, 76
Stationarity and mean reversion
augmented Dickey-Fuller test, 42–44
half-life of mean reversion, 46–48
Hurst exponent and Variance Ratio test, 44–46
linear mean-reverting trading strategy, 48–50
overview, 41
Statistical arbitrageurs, 88
Statistical signifi cance
of backtesting, 1, 16–22
long holding periods and, 155
Stocks
arbitrage between ETF and component,
96–102
cross-sectional momentum strategies for,
146–147
--- page 214 ---

207
INDEX
delisted, 9
hard-to-borrow, 11–12
mutual funds asset fi re sales and, 149–151
national best bid and off er quote sizes for, 90,
166–167
prices of, primary compared to consolidated,
9–10
ranking, 7, 104–105, 147
Stocks, mean reversion of
intraday mean reversion, 92–96
linear long-short model on, 102–105
overview, 87–88
trading stock pairs, 89–91, 102
Stock splits and backtesting, 7–8
Stop hunting strategy, 167
Stop losses, 153, 182–184
Strategies
breakout, 155
common pitfalls to, 1, 187
supported by special-purpose platforms,
31–36
tick-based, backtesting, 30
See also High-frequency strategies; Meanreversion strategies; Momentum
strategies; Pairs trading strategies
Streambase, 11
Subjective judgment, importance of, 188–189
Survivorship bias
databases for backtests free of, 23, 88
described, 8–9
stop losses and, 183
Test statistic, 16
Thestocksonar.com website, 148
Thomson Reuters
Machine Readable News, 149
News Analytics, 148
Thorp, Edward, 172
Tick-based strategies, backtesting, 30
Tickdata.com website, 9, 14
Ticking strategy, 165–166
Time-based exit strategies for momentum
strategies, 153
Time series mean reversion, 40–41, 88. See also
Mean reversion
Time series momentum
described, 133
strategies for, 137–141
tests for, 134–137
Trace statistic, 55
Transaction costs, 88, 108, 150
Triggering of stops and breakout strategies, 155
TU momentum strategy, 18–21, 137–141
Unit portfolio, 58–59
Uptick rule of SEC, 12, 90, 92
Variance Ratio test
for mean reversion, 41, 44–46
for time series momentum, 134, 135
Venue dependence of currency quotes, 10–11
Virtual private server (VPS), colocation of
trading programs in, 33–34
VIX index, as mean reverting, 122
Volatility, as mean reverting, 122
Volatility futures, 129–131, 143–144
Volume-weighted average price (VWAP)
approach, 83
VPS (virtual private server), colocation of
trading programs in, 33–34
VWAP (volume-weighted average price)
approach, 83
VX, 122
VX calendar spreads, 126–127
VX-ES roll return strategy, 143–144
VX-ES spread, 127–131
Weekend gap, 157
XLE-USO arbitrage, 142
