# Evidence-based Technical Analysis_ Applying the Scientific Method and Statistical Inference to Trading Signals.pdf — pages 381–400

--- page 381 ---

benchmarks.102 The MLM index provides some evidence that the futures
markets offer compensation in the form of systematic price movements.
If a risk-transfer premium is a valid explanation of trend-follower returns, then trend following in stocks should not be as rewarding as it is in
the commodity futures markets. A trend follower in stocks is not providing a risk-transfer service. There are data suggesting that trend following
in stocks is indeed a less rewarding enterprise.103 Lars Kestner compared
the performance of trend-following systems for a portfolio of futures and
a portfolio of stocks. The futures considered were 29 commodities in 8
different sectors.104 The stocks were represented by 31 large-cap stocks in
9 different industry sectors,105 and 3 stock indices. Risk-adjusted performance (Sharpe ratio) was computed for 5 different trend-following systems,106 over the period January 1, 1990 through December 31, 2001. The
Sharpe ratio averaged over the ﬁve trend-following systems in futures was
Theories of Nonrandom Price Motion
383
Annualized
Percent
Int.
Stocks
US
Stocks
T-Bills
Corp.
Bonds
MLM
Index
Return
Risk
18
16
14
12
10
8
6
4
2
0
FIGURE 7.13
Returns and standard deviations for ﬁve benchmarks.
Int.
Stocks
US
Stocks
T-Bills
Corp.
Bonds
MLM
Index
Risk-Adj. Return
0.7
0.6
0.5
0.4
0.3
0.2
0.1
0
FIGURE 7.14
Risk-adjusted excess returns.
--- page 382 ---

.604 versus .046 in stocks. These results support the notion that futures
trend followers are earning a risk premium that is not available to trend
followers in stocks. See Figure 7.15.
Liquidity Premium and the Gains
to Counter Trend Trading in Stocks
The stock market offers risk-taking stock traders a different form of compensation. They can earn a premium for providing liquidity to highly motivated sellers. In other words, there are systematic price movements in
stocks that can be exploited with countertrend strategies that buy stocks
that have been very weak over the recent past.
Owners of stock with an urgent need to liquidate their holdings need
buyers. This suggests that the market should offer compensation to
traders who are willing to meet unmet needs for liquidity. Evidence presented by Michael Cooper shows that buyers of oversold stocks can
earn above-average short-term returns.107 His study shows that stocks
that have displayed negative price momentum on declining trading volume earn excess returns. In other words, the pattern identiﬁes stocks
with distressed sellers in search of buyers. The excess returns appear to
be a liquidity premium. Cooper’s study showed that stocks that have declined sharply over the prior two weeks on declining volume display a
systematic tendency to rise over the following week. The declining volume aspect of this pattern is plausible because it can be interpreted to
mean that there are insufﬁcient buyers to meet the acute needs of the
sellers. To guard against the possibility of data mining, Cooper used a
walk-forward out-of-sample simulation to form portfolios of long and
short positions over the period 1978 to 1993. The long/short portfolios,
created from 300 large capitalization stocks, earned an annualized return of 44.95 percent versus a benchmark buy-and-hold return of 17.91
384 METHODOLOGICAL, PSYCHOLOGICAL, PHILOSOPHICAL, STATISTICAL FOUNDATIONS
Futures
Stocks
0.7
0.6
0.5
0.4
0.3
0.2
0.1
0
Sharpe
Ratio
FIGURE 7.15
Risk-adjusted returns to trend-following futures versus stocks.
--- page 383 ---

percent. Again, we see evidence of systematic price movements that can
be explained as a risk premium, in this case a liquidity premium, which
can be exploited with TA.
In the context of efﬁcient equity and futures markets, signals given by
TA methods can be viewed as identifying opportunities to ﬁll a market
need. In effect, they are want ads, “risk adopter for hire by hedgers,” or
“desperately seeking liquidity provider—will pay.” TA traders proﬁting
from these signals are not getting a free lunch. They are simply reading
the market’s Help Wanted advertisements.
CONCLUSION
In this chapter, I have made a case for the existence of nonrandom price
movements in ﬁnancial markets. Without them, there can be no justiﬁcation for technical analysis. With them, TA has an opportunity to capture
some portion of that nonrandom behavior. Ultimately, it is up to each
method of TA to prove that it can.
Theories of Nonrandom Price Motion
385
--- page 384 ---

PART II
Case Study:
Signal Rules
for the
S&P 500 Index
Evidence-Based Technical Analysis: Applying the Scientific
Method and Statistical Inference to Trading Signals
by David R. Aronson
Copyright © 2007 David R. Aronson
--- page 385 ---

Case Study
of Rule Data
Mining for
the S&P 500
T
his chapter describes a case study in rule data mining, the results
of which are reported in Chapter 9. The study evaluates the statistical signiﬁcance of 6,402 individual TA rules back tested on the
S&P 500 Index over the period from November 1, 1980 through July 1,
2005.
DATA MINING BIAS AND RULE EVALUATION
The primary purpose of the case study is to illustrate the application of
statistical methods that take into account the effects of data-mining bias.
To recap, data mining is a process in which the proﬁtability of many rules
is compared so that one or more superior rules can be selected. As
pointed out in Chapter 6, this selection process causes an upward bias in
the performance of the selected rule(s). In other words, the observed performance of the best rule(s) in the back test overstates its (their) expected performance in the future. This bias complicates the evaluation of
statistical signiﬁcance and may lead a data miner to select a rule with no
predictive power (i.e., its past performance was pure luck). This is the
fool’s gold of the objective technician.
This problem can be minimized by using specialized statisticalinference tests. The case study illustrates the application of two such
methods: an enhanced version of White’s reality check and Masters’s Monte-
Carlo permutation method. Both take advantage of a recent improvement,1
--- page 386 ---

which reduces the probability that a good rule will be overlooked (Type II
error). That is to say, the improvement increases the power of the tests.
A secondary purpose of the case study was the possible discovery of
one or more rules that generate statistically signiﬁcant proﬁts. However,
when the case study’s rules were proposed, it was unknown if any would
be found to be statistically signiﬁcant.
AVOIDANCE OF DATA SNOOPING BIAS
In addition to data mining bias, rule studies can also suffer from an even
more serious problem, the data-snooping bias. Data snooping refers to
using the results of prior rule studies reported by other researchers. Because these studies typically do not disclose the amount of data mining
that led to the discovery of whatever it was that was discovered, there is
no way to take its effects into account and hence no way to properly evaluate the statistical signiﬁcance of the results. As pointed out in Chapter 6,
depending on which method is being used—White’s Reality Check or the
Monte Carlo permutation method—information about each rule tested
must be available to construct the appropriate sampling distribution.
For example, suppose the case study in this book had included a rule
developed by Dr. Martin Zweig known as the double 9:1 upside/downside
volume rule. This rule signals long positions when the daily ratio of upside
to downside volume on the NYSE exceeds a threshold value of 9 on two
instances within a three-month time window. Note, this rule has three free
parameters: the threshold value on the ratio (9), the number of instances
on which the ratio exceeds the threshold (2), and the maximum time separation between the threshold violations (3 months). According to tests of
this rule conducted by students in my technical analysis class, the signal
does have predictive power over the following 3, 6, 9, and 12 months. In
other words, the rule is statistically signiﬁcant, but only under the assumption that Zweig did not engage in data mining to discover the parameter values he recommends: 9, 2, and 3. Zweig has not reported if he
tested other versions of the rule using different parameter combinations
or, if he did, how many combinations were tried to ﬁnd the speciﬁc set
that deﬁnes his rule. If Zweig’s rule were to be included in the case study
and it was selected as the best rule, it would be impossible to take into account the true amount of data mining that led to its discovery.
In an effort to avoid data-snooping bias, the case study did not explicitly include any rules discussed by other researchers. Even though it is
possible, perhaps even likely, that some of the study’s rules were similar
to those tested in prior rule studies, these similarities were by accident,
390
CASE STUDY: SIGNAL RULES FOR THE S&P 500 INDEX
--- page 387 ---

not by design. This precaution mitigated the data-snooping bias but could
not eliminate it entirely because, in proposing the 6,402 rules tested, I
could not help but be affected by rule studies I have previously read.
ANALYZED DATA SERIES
Although all rules were tested for their proﬁtability on the S&P 500 Index,
the vast majority of rules utilized data series other than the S&P 500 to
generate buy-and-sell signals. These other data series included: other market indices (e.g., transportation stocks), market breadth (e.g., upside and
downside volume), indicators that combine price and volume (e.g., onbalance volume), prices of debt instruments (e.g., BAA bonds), and interestrate spreads (duration spread between 10-year treasury notes and 90-day
treasury bills). This approach is in the spirit of intermarket analysis as discussed by Murphy.2 All series and rules are detailed below.
TECHNICAL ANALYSIS THEMES
The 6,402 rules tested were derived from three broad themes of TA: (1)
trends, (2) extremes and transitions, and (3) divergences. Trend rules generate long and short market positions based on the current trend of the
data series analyzed by the rule. Extreme and transition rules generate
long and short positions when the analyzed series reaches an extreme
high or low value or as it makes a transition between extreme values. Divergence rules generate signals when the S&P 500 Index trends in one direction while a companion data series trends in the other. The speciﬁc
data transformations and signal logic for each rule are described later in
this chapter.
The rules employ several common analysis methods including moving
averages, channel breakouts, and stochastics, which I refer to as channel
normalization.
PERFORMANCE STATISTIC: AVERAGE RETURN
The performance statistic used to evaluate each rule was its average return over the period (1980 to 2005) when back tested on detrended S&P
500 data. As pointed out in Chapter 1, detrending involves subtracting the
S&P 500’s average daily price change over the back-test period from each
Case Study of Rule Data Mining for the S&P 500
391
--- page 388 ---

day’s actual price change. This results in a new data series for which the
average daily change is equal to zero.
As discussed in Chapter 1, detrending eliminates any beneﬁt or detriment that would accrue to a rule’s performance as a result of either a long
or short position bias. A binary rule can be position biased if one of its
conditions (long or short) is restrictive relative to the other condition
(long or short). For example, if the long-position condition is more difﬁ-
cult to satisfy than the short-position condition, the rule will have a shortposition bias and tend to spend a majority of its time in short positions. If
such a rule were to be applied to market data with a positive trend (average daily price change > 0), its average return would be penalized. This reduction in the rule’s performance would have nothing to do with its
predictive power and thus cloud its evaluation.
NO COMPLEX RULES WERE EVALUATED
To keep the scope of the case study manageable, it was restricted to tests
of individual rules. Complex rules, which are derived by combining two or
more individual rules with mathematical and/or logical operators, were
not considered. The combining method can be as simple an unweighted
average or as complex as an arbitrarily nonlinear function derived with
sophisticated data-modeling software.
Limiting the case study to individual rules was detrimental for two
reasons. First, few practitioners rely on a single rule to make decisions.
Second, complex rules exploit informational synergies between individual
rules. It is not surprising, therefore, that complex rules have demonstrated
higher levels of performance. At least one study3 has shown that complex
rules can produce good performance, even when the simple rules combined to form the complex rule are individually unproﬁtable. Combining
rules intuitively is extremely difﬁcult, but there are now effective automated methods4 for synthesizing complex rules.
THE CASE STUDY DEFINED IN STATISTICAL TERMS
The following section deﬁnes the case study in terms of the key elements
of a statistical study: the population at issue, the parameter of interest,
sample data used, the statistic of interest, the null and alternative hypotheses considered, and the designated signiﬁcance level.
392
CASE STUDY: SIGNAL RULES FOR THE S&P 500 INDEX
--- page 389 ---

The Population
The population at issue is the set of daily returns that would be earned by
a rule if its signals were to be applied to the S&P 500 over all possible realizations of the immediate practical future.5 This is an abstract population, in the sense that its observations have not yet occurred and it is
inﬁnite in size.
Population Parameter
The population parameter is the rule’s expected average annualized return
in the immediate practical future.
The Sample
The sample consists of the daily returns earned by a rule applied to detrended S&P 500 Index prices over the back-test period from November 1,
1980 until July 1, 2005.
Sample Statistic (Test Statistic)
The sample statistic is the average annualized return earned by a rule
when applied to the detrended S&P 500 price data from November 1, 1980
until July 1, 2005.
The Null Hypothesis (H0)
The null hypothesis states that all 6,402 rules tested are without predictive
power. This implies that any observed proﬁts in a back test were due to
chance (sampling variability).
In reality, there are two version of the null hypothesis in the case
study. This stems from the fact that two different methods were used to
assess statistical signiﬁcance: White’s reality check and Masters’s Monte
Carlo permutation method. Although both methods assert that all rules
considered were devoid of predictive power, they implement this assumption differently. The null hypothesis tested by White’s reality check is that
all rules tested have expected returns equal to zero (or less). The null
tested by Masters’s Monte Carlo permutation is that all rules generated
their long and short positions in a random fashion. In other words, long
and short were randomly permuted with the market’s one-day-forward
price change.
Case Study of Rule Data Mining for the S&P 500
393
--- page 390 ---

The Alternative Hypothesis
This study’s alternative hypothesis asserts that a rule’s back-tested profitability stems from genuine predictive power. Again, the two methods
assert this in slightly different ways. In the case of White’s reality check,
the alternative hypothesis says that there is at least one rule within the
tested universe that has an expected return greater than zero. It should
be noted that White’s reality check does not assert that the rule with the
highest observed performance is necessarily that best rule (i.e., the rule
with the highest expected return). However, under fairly reasonable
conditions, they are one and the same.6 The alternative hypothesis declared by Masters’s method is that a rule’s back-tested proﬁtability is the
result of an informative pairing of its long and short positions with the
market’s one-day-forward price change. In other words, the rule has predictive power.
The Statistical Signiﬁcance Level
A 5 percent level of signiﬁcance was chosen as a threshold for rejection of
the null hypothesis. This means there was a 0.05 probability of rejecting
the H0 hypothesis when the H0 was, in fact, true.
Practical Signiﬁcance
The practical signiﬁcance of a result is different from its statistical signiﬁ-
cance. The latter is the probability that a rule that has no predictive power
(i.e., H0 is true) would earn a return as high as or higher than the return
produced by the rule in a back test by luck. In contrast, practical signiﬁ-
cance relates to the economic value of the observed rule return. When
sample sizes are large, as they are in the case study (i.e., over 6,000 days),
the H0 can be rejected even if a rule’s return is positive by a very minor
amount. In other words, a rule can be statistically signiﬁcant even though
its practical value is negligible. Practical signiﬁcance depends upon a
trader’s objectives. One trader may be satisﬁed with a rule for which expected return is 5 percent whereas another may reject any rule for which
expected return is less than 20 percent.
RULES: TRANSFORMING DATA SERIES
INTO MARKET POSITIONS
A rule is an input/output process. That is to say, it transforms input(s),
consisting of one or more time series, into an output, a new time series
394
CASE STUDY: SIGNAL RULES FOR THE S&P 500 INDEX
--- page 391 ---

consisting of +1’s and –1’s that indicate long and short positions in the
market being traded (i.e., S&P 500). This transformation is deﬁned by the
one or more mathematical,7 logical,8 or time series9 operators that are applied to the input time series. In other words, a rule is deﬁned by a set of
operations. See Figure 8.1.
Some rules utilize inputs that are raw time series. That is to say, the
one or more time series used as inputs to the rule are not transformed in
any way prior to the rule’s position logic being applied, for example the
S&P 500 closing price. This is illustrated in Figure 8.2.
Other rules utilize input series that have been derived from one or
more raw market series by applying various transformations to the market data. These preprocessed inputs are referred to as constructed data
series or indicators. An example of an indicator is the negative volume
index. It is derived from transformations of two raw data series; S&P 500
closing price and total NYSE daily volume. This is illustrated in Figure
8.3. The transformations used in the creation of the negative volume index and other indicators used in the case study are described in the following section.
Case Study of Rule Data Mining for the S&P 500
395
Time
Time
Etc.
Market
Time
Series
INPUT
Time Series
of
Market Position
OUTPUT
Mathematical,
Logical,
&
Time-Series
Operators
Rule
+1
–1
Time
FIGURE 8.1
TA rule transforms input into output.
--- page 392 ---

TIME-SERIES OPERATORS
This section describes the time-series operators used in the case study to
transform raw data series into indicators. Time-series operators are mathematical functions that transform a time series into a new time series. The
case study utilized several common time-series operators: channel breakout, moving average, and channel normalization. The channel breakout operator is used to identify trends in a time series for rules that are based on
396
CASE STUDY: SIGNAL RULES FOR THE S&P 500 INDEX
Input
Raw
S&P 500
Series
Output
Rule
+1
–1
FIGURE 8.2
Raw market time series as rule input.
Raw
Time Series
S&P 500
Raw
Time Series
NYSEP Volume
Indicator
(Negative Volume Index)
Rule Output
+1
–1
Rule
Negative Volume Index
Formula
FIGURE 8.3
Transformed market time series as rule input.
--- page 393 ---

trends. The moving-average operator, which can also identify trends, is used
in the case study for smoothing. The channel-normalization operator, or
stochastics, is used to eliminate the trend of a time series (i.e., detrending).
Channel Breakout Operator (CBO)
“The purpose of all trend identiﬁcation methods is to see past the underlying noise in a time series, those erratic moves that seem to be meaningless, and ﬁnd the current direction of the series.”10 One such method is the
n-period channel-breakout operator.11 Here, n refers to the number of
time periods (days, weeks, and such) into the past that are examined to
deﬁne the upper and lower channel boundaries that enclose the time series. The lower boundary is deﬁned by the minimum value of the time series over the past n-periods, not including the current period. The upper
boundary is deﬁned by the time series’ maximum value over the past
n-periods, not including the current period. Despite its extreme simplicity,
the channel-breakout operator has proven to be as effective as more complex trend-following methods.12
As conventionally interpreted, the channel breakout operator signals
long positions if the analyzed series exceeds its maximum value established over the past n-periods. Conversely, short positions are signaled
when the time series falls below its n-period minimum. This is illustrated
in Figure 8.4. In practice, the channel is redrawn as each new data point
Case Study of Rule Data Mining for the S&P 500
397
+1
–1
Rule
Output
Time
Series
Channel
Breakout
Channel
Breakout
Look-Back
Span
Time
FIGURE 8.4
Channel-breakout operator.
--- page 394 ---

becomes available, but in Figure 8.4 only several channels are shown to illustrate its function. Although the channel has a constant look-back span
with respect to the time axis, its vertical width with respect to the axis
that represents the value of the time series adjusts dynamically to the
range of the series over the past n-periods. This feature may explain the
effectiveness of the method. This is to say, the channel breakout’s dynamic range may reduce the likelihood of false signals caused by an increase in the series’ volatility rather than an actual change in its trend.
The n-period breakout operator has a single free parameter, its lookback span, the number of time periods into the past used to establish the
channel’s boundaries. In general, the larger the look-back span, the wider
the channel, and hence, the less sensitive the indicator. Thus, larger values
of n are used to identify larger trends. The case study tested 11 different
look-back spans for which lengths were separated by a factor of approximately 1.5. The speciﬁc spans used were: 3, 5, 8, 12, 18, 27, 41, 61, 91, 137,
and 205 days.
Moving-Average Operator (MA)
The moving average is one of the most widely used times-series operators
in TA. It clariﬁes trends by ﬁltering out high frequency (short-period) ﬂuctuations while passing through low frequency (long-period) components.
Thus, the moving-average operator is said to function as a low-pass ﬁlter.
This is illustrated in Figure 8.5, where the moving average has been centered13 (lagged by 0.5 × period –1). Note that the output of the movingaverage operator is essentially the trend of the original time series with
the high frequency oscillations about the trend removed.
The smoothing effect is accomplished by averaging the values of the
time series within a moving data window called the look-back span. This
eliminates or reduces the magnitude of ﬂuctuations with durations that are
equal to or less than the duration of the look-back span. Thus, a 10-day mov-
398
CASE STUDY: SIGNAL RULES FOR THE S&P 500 INDEX
Moving-
Average
Operator
Input:
Time Series
Time
Output:
Time Series
Time
Input
Series
MA
FIGURE 8.5
Moving-average operator: low-pass ﬁlter.
--- page 395 ---

ing average will reduce the amplitude of ﬂuctuations for which peak-to-peak
or trough-to-trough duration is less than 10 days, and it will completely eliminate a ﬂuctuation with a duration that is exactly equal to 10 days.
The beneﬁt of smoothing comes at a cost—lag. In other words, ﬂuctuations in the raw price that manifest in the smoothed version experience
some delay. Thus, a trough in the raw price does not produce a trough in
the moving average until some later date. The amount of lag depends
upon the length of the look-back span. A longer look-back span produces
more smoothing while producing more lag.
The lag induced by a simple moving average, which gives equal
weight to all elements in the window, is equal to one-half of the look-back
span minus one. Thus, the output of an 11-day simple moving average has
a lag of (11 – 1)/2 or 5 days. This means that trend reversals in the input
time series, which are of sufﬁcient duration to manifest in the moving average, will not show up until 5 days later.
There are many types of moving averages, from the simple moving average that gives equal weight to each element in the data window, to sophisticated smoothing methods that use complex data-weighting
functions. The beneﬁt conferred by a complex weighting is improved ﬁlter
performance—less lag for a given degree of smoothing. The ﬁeld of digital
signal processing is concerned with, among other things, the design of
weighting functions that maximize ﬁlter performance. Digital ﬁlters that
are relevant to TA are discussed in two books by Ehlers.14
The calculation for a simple moving average is given by the following
formula.15
Moving Average Operator
n
=
MAt =
Pt + Pt–1 + Pt–2 ... + Pt–n+1
n
Pt–i+1
n
i=1
Where:
Pt = Price at time t
MAt = Moving average at time t
n = Number of days used to compute moving average
∑
Case Study of Rule Data Mining for the S&P 500
399
--- page 396 ---

The lag of a simple moving average can be reduced while maintaining the same degree of smoothing by using a linearly weighted moving
average. As pointed out by Ehlers16 the lag of a linearly weighted moving
average with a look-back span of n days is (n – 1)/3 compared with (n –
1)/2 for a simple moving average. Thus, a linearly weighted moving average with a span of 10 days will have a lag of 3 days whereas a simple
moving average with the same span will have a lag of 4.5 days. The linear-weighting scheme applies a weight of n to the most recent data
point, where n is the number of days in the moving average look-back
span, and then the weight is decreased by one for each prior day. The
sum of the weights becomes the divisor. This is illustrated in the following equation:
The case study used a four-day linearly weighted moving average to
smooth indicators used in rules that signal when the indicator crosses
above or below a critical threshold. Smoothing mitigates the problem of
excessive signals that an unsmoothed version of the indicator wiggling
back and forth across the threshold would produce. The calculation of a
Linear Weighted Moving Average
WMAt  =
(n) × Pt + (n–1) × Pt–1 + ... + (n–(t–n+1)) × Pt–n+1
n + n–1 + ... + n–(t–n–1)
Where:
Pt = Price at time t
WMAt = Weighted moving average at time t
n = Number of days used to compute moving average
Sum of Weights
Weights
400
CASE STUDY: SIGNAL RULES FOR THE S&P 500 INDEX
--- page 397 ---

four-day linearly weighted moving average is illustrated in the following
equation:
Channel-Normalization Operator
(Stochastics): CN
The channel-normalization operator (CN) removes the trend in a time
series, thus clarifying short-term ﬂuctuations around the trend. Channel
normalization detrends the time series by measuring its current position within a moving channel. The channel is deﬁned by the maximum
and minimum values of the time series over a speciﬁed look-back span.
In this way it is similar to the channel breakout operator discussed
earlier.
The channel normalized version of a time series is scaled to the range
0 to 100. When the raw time series is at its maximum value within the
look-back span, CN assumes the value of 100. When the series is at the
minimum value within the look-back span the CN is equal to zero. A value
of 50 indicates the series is currently midway between its maximum and
minimum values.
Where:
Pt = Price at time t
WMAt = Weighted moving average at time t
n = Number of days used to compute moving average
WMAt  =
(4)×Pt0 + (3)×Pt–1 + (2)×Pt–2 + (1)×Pt–3
10
Sum of Weights
Weights
Four Day Linear Weighted Moving Average
Case Study of Rule Data Mining for the S&P 500
401
--- page 398 ---

The calculation of CN is illustrated in the following equation:
An example of the calculation is illustrated in Figure 8.6.
In terms of its ﬁltering properties, the CN operator functions as a
high-pass ﬁlter. In contrast to the moving average, a low-pass ﬁlter, CN expresses the short-period (high-frequency) oscillations in its output while
ﬁltering out the long-period ﬂuctuations or trend. This is illustrated in Figure 8.7. Note that the input series has a distinct upward trend, but the output series has no trend.
Where:
CNt = n day channel normalized value on day t
St = Value of time series at time t
Smin–n = Minimum value of time series, last n days
Smax–n = Maximum value of time series, last n days
n = Channel look-back span in days
CNt  =
St – Smin–n
Smax–n – Smin–n
 100
Channel Normalization Operator
402
CASE STUDY: SIGNAL RULES FOR THE S&P 500 INDEX
Input
Series
Look-Back Span
Channel Maximum: 83
Channel Minimum: 60
Current
75
Time
Channel Normalized Value = (75 – 60)/(83–60) = 0.65
FIGURE 8.6
Channel normalization.
--- page 399 ---

The CN operator has been known in TA at least as far back as 1965
when Heiby17 used it to formulate divergence rules. He measured divergences by comparing the channel normalized value of the S&P 500 with
the channel normalized value of a market breadth indicator. According to
Heiby, a divergence occurred when one series was in the upper quartile of
its 50-day range (CN > 74) while the other series was in the lower quartile
of its range (CN <26). Sometime in the early 1970s, a virtually identical operator was described by George Lane,18 who dubbed it stochastic. Unfortunately, the name is a misnomer. In reality, stochastic is a mathematical
term that refers to the evolution of a random variable through time. There
is nothing random about the CN operator, which is a completely deterministic data transformation. This text uses the term channel normalization
(CN) rather than Lane’s term, because it accurately describes what the operator does. Most TA writings continue use the term stochastics. The case
study utilizes the CN operator for two types of rules: (1) extremes and
transitions and (2) divergences. They are discussed in following sections.
Indicator Scripting
As discussed earlier, the time series that are used as inputs to the rules
may either be in raw form, just as they comes from the market, or in the
form of indicators—times series that have been created by applying one
or more mathematical, logical, or time-series operators to one or more
raw time series. The speciﬁcation of an indicator may require the application of several operators. For example, the raw time series might ﬁrst be
smoothed with a moving average and then channel normalization is applied to the smoothed version. When the creation of an indicator involves
multiple steps, it is convenient to express it in terms of an indicator
scripting language (ISL). An ISL expression succinctly depicts the set of
transformations used to create the indicator from raw time series.
Case Study of Rule Data Mining for the S&P 500
403
CN
Operator
Input:
Time Series
Time
Output:
Time Series
Time
FIGURE 8.7
Channel normalization operator: a high-pass ﬁlter.
--- page 400 ---

My ﬁrst exposure to an ISL was Gener, which was developed in 1983
for Raden Research Group by friend and colleague Professor John Wolberg. Today, ISLs are common. All rule back-testing platforms,19 such as
TradeStation, Wealth-Lab, Neuro-Shell, Financial Data Calculator, and so
forth have an ISL. Though each ISL has features unique to it, they share
similar syntaxes. The most basic ISL statement is a time-series operator
followed by a set of parentheses that contain the arguments of the operator. The arguments are the items that must be deﬁned for the operator to
do its thing. Operators differ in terms of the number of arguments required. For example, the moving-average operator requires two arguments: a data series to which the operator will be applied and the number
of periods in the look-back span. Thus a moving-average indicator would
be speciﬁed by a statement such as this:
Moving Average Indicator = MA (input series, N)
Where:
MA is the moving average operator
N is the number of days in the moving average.
The general form of an indicator expression in scripting language is:
Indicator = Operator (Argument1, Argument2, . . . , Argumenti)
Where:
i is the number of arguments required by the operator.
Figure 8.8 shows the ISL syntax for the operators deﬁned thus far:
channel breakout, moving average, and channel normalization.
A key beneﬁt of ISL is the ability to deﬁne complex indicators by nesting operators. In nesting, the output of one operator becomes an argument for a second operator and so on. For example, if one wanted to
deﬁne an indicator that is the 60-day channel normalization of another
time series that is a 10-day moving average of the Dow Jones Transportation Index, the expression for the indicator in ISL would look something
like this:
Indicator = CN [MA(DJTA, 10), 60]
404
CASE STUDY: SIGNAL RULES FOR THE S&P 500 INDEX
