# Evidence-based Technical Analysis_ Applying the Scientific Method and Statistical Inference to Trading Signals.pdf — pages 419–438

--- page 419 ---

Case Study of Rule Data Mining for the S&P 500
423
TABLE 8.3
The 12 E-Rule Types Deﬁned in Terms of Threshold Crossing Events
E-Rule Types
Long Entry/Short Exit
Short Entry/Long Exit
1
Event 1
Event 2
2
Event 1
Event 3
3
Event 1
Event 4
4
Event 2
Event 3
5
Event 2
Event 4
6
Event 3
Event 4
7
Event 2
Event 1
8
Event 3
Event 1
9
Event 4
Event 1
10
Event 3
Event 2
11
Event 4
Event 2
12
Event 4
Event 3
Upper
Threshold
Lower
Threshold
Time
0
100
50
2
1
2
1
+1
–1
Rule
Output
0
L
S
L
S
FIGURE 8.12
Extreme value and transition rule: Type 1.
--- page 420 ---

424
CASE STUDY: SIGNAL RULES FOR THE S&P 500 INDEX
Upper
Threshold
Lower
Threshold
Time
0
100
50
1
1
+1
–1
Rule
Output
0
L
S
L
S
3
3
FIGURE 8.13
Extreme value and transition rule: Type 2.
Upper
Threshold
Lower
Threshold
Time
0
100
50
1
1
+1
–1
Rule
Output
0
L
S
L
S
4
4
FIGURE 8.14
Extreme value and transition rule: Type 3.
--- page 421 ---

Case Study of Rule Data Mining for the S&P 500
425
Upper
Threshold
Lower
Threshold
Time
0
100
50
+1
–1
Rule
Output
0
L
S
L
S
2
2
3
3
FIGURE 8.15
Extreme value and transition rule: Type 4.
Upper
Threshold
Lower
Threshold
Time
0
100
50
+1
–1
Rule
Output
0
L
S
L
S
2
2
4
4
FIGURE 8.16
Extreme value and transition rule: Type 5.
--- page 422 ---

426
CASE STUDY: SIGNAL RULES FOR THE S&P 500 INDEX
Upper
Threshold
Lower
Threshold
Time
0
100
50
+1
–1
Rule
Output
0
L
S
L
S
3
3
4
4
FIGURE 8.17
Extreme value and transition rule: Type 6.
Upper
Threshold
Lower
Threshold
Time
0
100
50
+1
–1
Rule
Output
0
L
S
L
S
1
2
1
2
FIGURE 8.18
Extreme value and transition rule: Type 7.
--- page 423 ---

Case Study of Rule Data Mining for the S&P 500
427
Upper
Threshold
Time
0
100
50
+1
–1
Lower
Threshold
Rule
Output
0
L
S
L
S
1
1
3
3
FIGURE 8.19
Extreme value and transition rule: Type 8.
Upper
Threshold
Time
0
100
50
+1
–1
Lower
Threshold
Rule
Output
0
L
S
L
S
1
1
4
4
FIGURE 8.20
Extreme value and transition rule: Type 9.
--- page 424 ---

428
CASE STUDY: SIGNAL RULES FOR THE S&P 500 INDEX
Upper
Threshold
Time
0
100
50
+1
–1
Lower
Threshold
Rule
Output
0
L
S
L
S
2
2
3
3
FIGURE 8.21
Extreme value and transition rule: Type 10.
Upper
Threshold
Time
0
100
50
+1
–1
Lower
Threshold
Rule
Output
0
L
S
L
S
2
2
4
4
FIGURE 8.22
Extreme value and transition rule: Type 11.
--- page 425 ---

Parameter Sets and Total Number of E Rules.
An E rule is deﬁned
by four parameters: type (1 through 12), input series, displacement of the
thresholds form 50, and look-back span for the channel normalization. Because both the upper and lower thresholds are displaced equally from the
midvalue of 50, it is possible to specify them with a single number, their
displacement from 50. For example, a threshold-displacement 10 places
the upper threshold at 60 (50 + 10) and the lower threshold at 40 (50 – 10).
Two different values for the threshold displacement parameter were
tested: 10 and 20. The displacement value of 20 gave the upper threshold as
70 and the lower threshold as 30. Three different values were considered
for the channel normalization look-back span: 15, 30, and 60. All parameter
values were chosen without optimization on the basis of intuition.
Given 12 possible rule types, 39 possible candidate input series, 2 possible threshold displacements, and 3 possible channel normalization lookback spans, there were 2,808 E-type rules (12 × 39 × 2 × 3).
Naming Convention for Extreme Value and Transition Rules.
In
Chapter 9, the following naming convention will be used to report results
for E rules:
(E)-(type)-(Input Series)-(Threshold Displacement)-(Channel Normalization Look-Back Span)
Case Study of Rule Data Mining for the S&P 500
429
Upper
Threshold
Time
0
100
50
+1
–1
Lower
Threshold
Rule
Output
0
L
S
L
S
3
3
4
4
FIGURE 8.23
Extreme value and transition rule: Type 12.
--- page 426 ---

For example, E-4-30-20-60 would be: E rule, type 4, input series 30
(cumulative new highs/new lows ratio), a threshold displacement of 20
(upper = 70, lower = 30), and a channel normalization look-back span of
60 days.
Divergence Rules
Divergence analysis is a foundational concept of TA that concerns the relationship between a pair of time series. It is premised on the notion that,
under normal circumstances, certain pairs of market time series tend to
move up and down together, and when they fail to do so it conveys information. A divergence is said to occur when one member of the pair departs from their shared trend. Typically, a divergence manifests itself as
follows: both series have been trending in the same direction, but then
one series reverses its prior trend while its companion continues its prior
trend. This event, according to divergence analysis, is a potential signal
that the prior shared trend has weakened and may be about to reverse.
This is illustrated in Figure 8.24. Hussman contends that divergence signals are most informative when numerous time series are analyzed and a
signiﬁcant number begin to diverge.42
The Dow theory is based on divergence analysis. It asserts that
when an index of industrial stocks and an index of transportation
430
CASE STUDY: SIGNAL RULES FOR THE S&P 500 INDEX
Time Series
2
Time Series
1
Time
Divergence
Condition
Shared Trend
FIGURE 8.24
Divergence analysis.
--- page 427 ---

stocks are trending in the same direction, the trend they share is
healthy and likely to persist. However, if one series begins to diverge, it
is taken as preliminary evidence that the trend is weakening and may
reverse. Another application of divergence analysis considers the price
of an instrument as one time series and its rate of change or momentum
as the second series. Price/momentum divergence analysis is discussed
by Pring.43
A divergence leads to one of two outcomes: either the series, for
which the trend had remained undisturbed, will experience a reversal to
join its diverging companion or the diverging series will end its errant
ways and rejoin its companion. A completed signal of reversal is not presumed until both series have convincingly reversed and are again moving
in the same direction. Thus, the fundamental idea behind divergence
analysis is coherence, that is, the state of affairs when two waveforms
are in phase with each other (see Figure 8.25). When two series are coherent, their common trend is considered strong and expected to continue. However, when their trends become incoherent, or out of phase,
the future of the once shared trend is in question. Therefore, candidates
for divergence analysis are pairs of time series that are generally coherent, but when they do diverge, one particular member of the pair tends to
have leading information about the other. In other words, there is a
rather stable lead–lag relationship.
Case Study of Rule Data Mining for the S&P 500
431
Divergence
Trend
Uncertain
Time
Coherent
Downtrends
Trend Should
Persist
Coherent
Uptrends
Trend Should
Persist
FIGURE 8.25
Trend coherence and divergence.
--- page 428 ---

Subjective Divergence Analysis.
Subjective divergence analysis
typically involves comparing the peaks and troughs of the two time
series under consideration. A negative or bearish divergence is said to
occur if one series continues to register peaks at successively higher
levels while the other series begins forming peaks at lower levels.
The failure by the second series to form peaks at successively higher
levels is also termed a bearish nonconﬁrmation. This is illustrated in
Figure 8.26.
A positive or bullish divergence is said to occur when one series continues to register successively lower troughs in an established downtrend
while the second series begins to form troughs at higher levels. This is
also termed a bullish nonconﬁrmation. See Figure 8.27.
The problem with subjective divergence analysis, or any subjective
method for that matter, is that it the procedure is neither repeatable nor
testable. One issue requiring the analyst’s subjective judgment is the timing of peaks and troughs. Because the two time series may not peak and
trough at precisely the same time, it may be unclear which peaks and
troughs should be compared. Another issue is related to duration: How
long must the divergence be in existence before deciding that one has occurred? Still a third unresolved issue is how much upward (downward)
432
CASE STUDY: SIGNAL RULES FOR THE S&P 500 INDEX
Time
Series 1
Series 2
Diverging Peaks
Diverging Peaks
Confirmed Peaks
Confirmed Peaks
FIGURE 8.26
Negative divergence (peaks compared).
--- page 429 ---

movement in a series is required to establish that a new trough (peak)
has formed.
An Objective Measure of Divergence.
These problems can be addressed with objective divergence analysis. A method that objectiﬁes
peak and trough comparisons is discussed by Kaufman44 and he provides computer code. Kaufman also discusses a second method that
uses linear regression to estimate the slopes in the two time series
being compared. A divergence is deﬁned as the differences in their
slopes. Both methods look interesting but no performance statistics are
offered.
The divergence rules considered in this case study were inspired by
the objective divergence method discussed by Heiby45 in his book, Stock
Market Proﬁts through Dynamic Synthesis. The two series being examined by Heiby were ﬁrst detrended with channel normalization. He de-
ﬁned a divergence to be in effect if one series had a channel-normalized
value of 75 or greater while the other series had a value of 25 or less.
Thus, divergence was quantiﬁed in terms of the difference in channelnormalized values.
This suggested an initial formulation for a divergence indicator that is
deﬁned in the equation that follows. Note that one series is always the
S&P 500, the target market of the case study. The companion series, for
Case Study of Rule Data Mining for the S&P 500
433
Time
Series 2
Series 1
Confirmed Troughs
Diverging
Troughs
Diverging
Troughs
FIGURE 8.27
Positive (bullish) divergence: troughs compared.
--- page 430 ---

example the Dow Jones Transports, is the series with which the S&P 500
is compared. The case study compared the S&P 500 to all the time series
in Table 8.2, except the S&P 500 open price, which was excluded on
grounds of redundancy with the S&P 500 close.
Because the channel normalized value of each series can vary between 0 and 100, this divergence indicator has a potential range of –100 to
+100. For example, if the companion series is at the bottom of its channel
range (CN = 0) and the S&P 500 is at the top of its range (CN = 100), the divergence indicator would have a value of –100. It should be noted that this
quantiﬁcation of divergence is merely one approach among several possibilities that may prove superior.
Limitations of the Proposed Divergence Indicator.
The proposed
divergence indicator measures the degree to which two times series have
similar positions within their respective channels. In general, this will give
a reasonable quantiﬁcation of the degree to which the series are in phase
with one another. For example, when the indicator registers a value of
zero, it indicates that there is no divergence; both series have the same
channel normalized values and can be presumed to be trending together.
However, there can be cases for which a value of zero does not indicate
that the two series are in phase. For example, if two time series are negatively correlated, that is to say, they tend to move inversely with respect to
each other within their channels, the divergence indicator will assume a
value of zero as the series-normalized values cross paths. In this instance,
a value of zero would be an erroneous indication that the two series are
trending together. This is illustrated in Figure 8.28 and is clearly a limitation of the proposed divergence indicator.
This problem could have been avoided with a more complex formulation of divergence indicator based on cointegration,46 a concept developed in the ﬁeld of econometrics. Cointegration was proposed in 1987
by Engle and Granger.47 This more sophisticated and potentially more
Where:
CN = Channel normalization operator
n = Look-back span of the channel normalization
Divergence Indicator
(Initial Formulation)
= CN (Companion Series, n) – CN (S&P 500, n)
434
CASE STUDY: SIGNAL RULES FOR THE S&P 500 INDEX
--- page 431 ---

accurate way of measuring divergences uses regression analysis to determine if a linear relationship exists between two time series. Because
this method can easily accommodate the case in which the pair of series
are strongly negatively correlated (180 degrees out of phase), it solves
the problem discussed earlier that can occur with a divergence indicator
based on channel normalization. An additional advantage of cointegration analysis is that it ﬁrst applies a statistical test48 to determine if the
two series have related trends (i.e., that they are cointegrated). If the
test shows that they are cointegrated, a stationary divergence indicator49
naturally falls out of the analysis. In cointegration terminology, this indicator is referred to as the error-correction model. It measures the degree
to which one series has diverged from the typical linear relationship between the two series.
In most applications of cointegration, the error-correction model is
used to predict the behavior of the spread between the cointegrated time
series. In these applications, the divergence is predicted to revert back to
the normal state of a shared trend when the error-correction model becomes extremely positive or negative. In other words, when the error,
which is a departure from the normal linear relationship between the two
Case Study of Rule Data Mining for the S&P 500
435
0
100
50
Channel-Normalized Value Companion Series
+100
–100
0
Divergence Indicator
0
100
50
Channel-Normalized Value S&P 500
Erroneous Indications of In-Phase Behavior
Time
FIGURE 8.28
Erroneous indications of in-phase behavior.
--- page 432 ---

series, becomes extreme, it is predicted to correct back to its normal
value of zero.
A typical application of this analysis is pairs trading. For example, if
it has been determined that Ford and GM stocks are cointegrated time series and Ford has gotten high relative to GM, a short position would be
taken in Ford against a long position in GM. Thus, no matter how the divergence is corrected (Ford falls, GM rises, or some combination) the
pairs trade will generate a proﬁt.
Fosback50 made an innovative use of cointegration analysis to develop a
stock market predictor. His innovation was to use the measurement derived
from the error correction model as an indicator to predict the movement of a
third variable, the S&P 500, rather than predict the behavior of the spread between the cointegrated variables. The indicator, called the Fosback Index,
exploits the fact that interest rates and mutual fund cash levels are cointegrated time series. Fosback’s work is particularly noteworthy because it preceded the Engle and Granger publication on cointegration by over a decade.
The Fosback Index signals when the mutual fund cash level diverges signiﬁ-
cantly from a level predicted by its linear relationship with short-term interest rates. The premise is that when mutual fund managers are excessively
pessimistic about stock market prospects, they hold cash reserves that are
substantially higher than the that predicted by interest rates. Excessive optimism is the opposite situation. Fosback found that both excessive pessimism and excessive optimism, measured in this fashion, correlated with
future returns on the stock market. In effect, the Fosback Index removes the
inﬂuence of short-term interest rates from mutual fund cash levels, thus providing a purer measure of fund manager sentiment than that provided by the
raw cash level, which is contaminated by interest rates.
In the interests of simplicity, the cointegration technique was not used
for the divergence indicators in the case study. It was assumed that if a
companion series was not related to the S&P 500, it would be revealed by
the poor ﬁnancial performance of the divergence rule. However, I51 believe that the cointegration methodology warrants further investigation in
development of indicators.
Need for Double Channel Normalization.
A second problem with
the initially proposed version of the divergence indicator was more serious and had to be remedied. The divergence rules in the case study involved pairing the S&P 500 with 38 other time series. Given that these
series had varying degrees of co-movement with the S&P 500, the ﬂuctuation range of the divergence indicator would vary considerably from one
pair to the next. This would make it impractical to use the same threshold
for all pairings. This problem is illustrated in Figure 8.29. Note that the
high threshold displacement that would be suitable for a companion se-
436
CASE STUDY: SIGNAL RULES FOR THE S&P 500 INDEX
--- page 433 ---

ries with a low degree of co-movement with the S&P 500 would never produce a signal for a companion series with a high degree of co-movement
to the S&P 500. For this reason, the initial formulation of the divergence
indicator was deemed impractical.
This problem was addressed with a modiﬁed formulation of the divergence indicator illustrated in the equation that follows. It employs the
channel normalization operator twice. That is to say, the indicator is a
channel-normalized version of the initial divergence indicator.
Where:
CN = Channel normalization operator
Series 1 = Companion series
n = Look-back span of the first channel normalization
= CN {CN (Series 1, n) – CN (S&P 500, n), 10n}
Divergence Indicator
(Double Channel Normalization)
Case Study of Rule Data Mining for the S&P 500
437
+100
–100
0
Companion Series Has High Degree of Co-Movement with S&P 500
Time
+100
–100
0
Companion Series Has Low Degree of
Co-Movement with S&P 500
FIGURE 8.29
Divergence indicator: inconsistent volatility.
--- page 434 ---

The second layer of channel normalization takes into account the
ﬂuctuation range of the initial formulation of the divergence indicator.
This solves the problem of inconsistent ﬂuctuation ranges across the 38
pairs of time series. As a result, the modiﬁed version of the divergence indicator will have roughly the same ﬂuctuation range irrespective of the
particular pair of time series being used, making it practical to use uniform thresholds.
The look-back span for the second level of channel normalization was
set at 10 times the look-back interval used for ﬁrst level. Thus, if the channel normalization used a look-back span of 60 days, the second layer of
channel normalization used a look-back span of 600 days. It was assumed
that a 10-fold look-back span would be sufﬁcient to establish the ﬂuctuation range of the basic divergence indicator. Note that a modiﬁed divergence indicator has a potential ﬂuctuation range of 0 to 100, similar to any
channel-normalized variable. See Figure 8.30.
Divergence Rule Types.
Upper and lower threshold were applied to
the modiﬁed divergence indicator to generate signals. A positive or bullish divergence was in effect when the divergence indicator was above
its upper threshold. This occurred when the companion series was
moving up more or moving down less than the S&P 500. This was evidenced by the companion series having a higher relative position within
its channel than the S&P 500. Conversely, a negative or bearish divergence existed when the divergence indicator was below the lower
threshold. This occurred when the companion series was moving down
more or moving up less than the S&P 500, resulting in its having a lower
relative position within its channel than the S&P 500. This is illustrated
in Figure 8.30.
438
CASE STUDY: SIGNAL RULES FOR THE S&P 500 INDEX
0
100
50
Negative Divergences
Positive Divergences
Upper
Threshold
Lower
Threshold
FIGURE 8.30
Modiﬁed divergence indicator.
--- page 435 ---

The question was how to create signaling rules from the modiﬁed divergence indicator. Two rules seemed obvious: a bullish divergence rule,
which would call for long positions in the S&P 500 when the divergence
indicator was above the upper threshold, and a bearish divergence rule,
which would call for short positions in the S&P 500 when the divergence
indicator was below its lower threshold.
Both rules assumed that the companion series had leading information about the S&P 500. If the companion series was stronger than the
S&P 500 (positive divergence), then a long position would be justiﬁed,
whereas if the companion series was weak (negative divergence) a short
position would be justiﬁed. However, this assumption may be incorrect. It
may be the case that negative divergences are predictive of higher prices
for the S&P 500, whereas positive divergences are predictive of lower
prices. In other words, perhaps it is the S&P 500 that has the leading information. This suggests that inverse versions of each rule should be tried. In
the end, it was determined that there are 12 possible divergence rule
types, and all were tested.
These 12 rule types are exactly the same set used for the extreme
value and transition rules. This makes sense because the modiﬁed divergence indicator is similar to the indicator used for the E rules because it
has a ﬂuctuation range of 0 to 100 and has two thresholds.
The 12 divergence rule types, presented in Table 8.4, include the basic
bullish divergence (type 6), the bearish divergence (type 7) and their inversions (types 12 and 1). The 12 types are not illustrated because the illustrations would be redundant of those presented in the section on
Extreme and Transition Rules.
Parameter Combinations and Naming Convention for Divergence Rules.
Each divergence rule is deﬁned by four parameters:
type, companion series, threshold displacement, and channel normalization look-back span. There are 12 types of the divergence rules (see Table
8.4), 38 companion data series, 2 threshold displacement values—10 and
20, and 3 look-back spans—15, 30, and 60 days. This gives a total of 2,736
divergence rules (12 × 38 × 2 × 3)
The naming convention used for reporting results of divergence or
D rules in Chapter 9 is as follows: (D)-type-companion series-threshold
displacement-channel normalization look back span. Thus, a rule is
named
D-3-23-10-30
Divergence rule, type 3, companion series 23 (positive volume index 30-day moving average), threshold displacement = 10 (upper
Case Study of Rule Data Mining for the S&P 500
439
--- page 436 ---

threshold = 60, lower threshold = 40), 30-day channel normalization
look-back span.
This completes the description of the rules tested in the case study.
Results are presented in Chapter 9.
440
CASE STUDY: SIGNAL RULES FOR THE S&P 500 INDEX
TABLE 8.4
Divergence Rules and Associated Threshold Events
Divergence Rule Types
Long Entry/Short Exit
Short Entry/Long Exit
1
Down Cross
Upper Cross
Lower Threshold
Lower Threshold
Down Cross
Upper Cross
2
Lower Threshold
Upper Threshold
Down Cross
Down Cross
3
Lower Threshold
Upper Threshold
Up Cross
Up Cross
4
Lower Threshold
Upper Threshold
Up Cross
Down Cross
5
Lower Threshold
Upper Threshold
Up Cross
Down Cross
6
Upper Threshold
Upper Threshold
Up Cross
Down Cross
7
Lower Threshold
Lower Threshold
Up Cross
Down Cross
8
Upper Threshold
Lower Threshold
Down Cross
Down Cross
9
Upper Threshold
Lower Threshold
Up Cross
Up Cross
10
Upper Threshold
Lower Threshold
Down Cross
Up Cross
11
Upper Threshold
Lower Threshold
Down Cross
Up Cross
12
Upper Threshold
Upper Threshold
--- page 437 ---

Case Study
Results and the
Future of TA
PRESENTATION OF RESULTS
The primary objective of the case study was to demonstrate the application of two statistical inference methods suitable for the evaluation of
rules discovered by data mining. As explained in Chapter 6, traditional signiﬁcance tests are not suitable because they do not take into account the
biasing effect of data mining. The two methods used were White’s reality
check (WRC) and the Monte Carlo permutation (MCP).
A secondary objective of the case study was the possible discovery of
rules with statistically signiﬁcant returns when applied to the S&P 500 Index. Toward this end, a set of 6,402 rules described in Chapter 8 were
back tested and evaluated.
With respect to the primary objective, the case study resoundingly
demonstrated the importance of using signiﬁcance tests designed to cope
with data-mining bias. With respect to the second objective, no rules with
statistically signiﬁcant returns were found. Speciﬁcally, none of the 6,402
rules had a back-tested mean return that was high enough to warrant a rejection of the null hypothesis, at a signiﬁcance level of 0.05. In other
words, the evidence was insufﬁcient to reject a presumption that none of
the rules had predictive power.
The rule with the best performance, E-12-28-10-30,1 generated a mean
annualized return of 10.25 percent, on detrended market data. In Figure
9.1, the rule’s return is compared to the sampling distribution produced by
WRC. The p-value of the return is 0.8164, far above the 0.05 level set as the
signiﬁcance threshold. Figure 9.1 makes it clear that the performance of
--- page 438 ---

the best rule out of the 6,402 examined falls well within the range of ordinary sampling variability. In fact, it even falls below the sampling distribution’s central value of 11 percent. Quite disappointing!2
The sampling distribution was generated by 1,999 replications of the
bootstrap procedure. Had a larger number of replications been used, the
distribution’s shape would have been smoother, but the conclusion would
have been the same: the rule’s performance was not high enough to reject
the null hypothesis.
Figure 9.2 shows E-12-28-10-30 plotted on the sampling distribution
produced by MCP. It produced a similar p-value of 0.8194.
Note that both sampling distributions are centered at approximately
an 11 percent mean return. This particular value was a consequence of the
speciﬁcs of the case study; the particular set of 6,402 rules, their return
correlations, the number of observations used to compute their mean returns, and the particular set of S&P data. In other words, the expected return for the best rule of 6,402 competing rules with no predictive power
under these speciﬁc conditions is approximately 11 percent. It is not 0
percent.
To recap a point made in Chapter 6, the sampling distribution for the
mean return of the best-performing rule out of N rules (e.g., N = 6,402) is
442
CASE STUDY: SIGNAL RULES FOR THE S&P 500 INDEX
0.10
0.09
0.08
0.07
0.06
0.05
0.04
0.03
0.02
0.01
0
R
E
L

F
R
E
Q
Annualized Return
8%
10%
12%
14%
16%
P-value: 0.8164
P-value: 0.8164
Best Rule
Return 10.25%
Best Rule
Return 10.25%
FIGURE 9.1
Sampling distribution for best of 6,402 worthless rules using
White’s reality check.
