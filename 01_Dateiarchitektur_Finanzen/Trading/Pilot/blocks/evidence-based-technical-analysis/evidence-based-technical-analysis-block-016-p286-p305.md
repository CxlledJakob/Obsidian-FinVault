# Evidence-based Technical Analysis_ Applying the Scientific Method and Statistical Inference to Trading Signals.pdf — pages 286–305

--- page 286 ---

The Five Factors Deﬁned.
Five factors determine the degree of
data-mining bias. They are:
1. Number of rules back-tested: This refers to the total number of
rules back tested during the data-mining process en route to discovering the highest-performing rule. The larger the number of rules tested,
the larger the data-mining bias.
2. The number of observations used to compute the performance
statistic: The larger the number of observations, the smaller the
data-mining bias.
3. Correlation among rule returns: This refers to the degree to which
the performance histories of the rules tested are correlated with each
other. The less correlated they are, the larger the data-mining bias.
4. Presence of positive outlier returns: This refers to presence of
very large returns in a rule’s performance history, for example a very
large positive return on a particular day. When these are present, the
data-mining bias tends to be larger, although this effect is reduced
when the number of positive outliers is small relative to the total number of observations that are used to compute the performance statistic. In other words, more observations dilute the biasing effect of
positive outliers.
5. Variation in expected returns among the rules: This refers to the
variation in true merit (expected return) among the rules back tested.
The lower the variation, the greater the data-mining bias. In other
words, when the set of rules tested have similar degrees of predictive
power, the data-mining bias will be larger.
How Each Factor Impacts the Data-Mining Bias.
Figures 6.21
through 6.25 depict the relationships between each of the ﬁve factors and
288 METHODOLOGICAL, PSYCHOLOGICAL, PHILOSOPHICAL, STATISTICAL FOUNDATIONS
 Spectrum of Randomness
Data
Mining
Bias
Large
MERIT
LUCK
No Bias
FIGURE 6.20
Relationship of data-mining bias to degree of randomness.
--- page 287 ---

Data-Mining Bias: The Fool’s Gold of Objective TA
289
Log of Number of Rules Back-Tested
DM Bias
Large
0
1
Many
FIGURE 6.21
Number of rules back tested (1).
Number of Observations
DM Bias
Large
0
1
Many
FIGURE 6.22
Number of observations used to compute performance statistic (2).
DM Bias
Correlation Coeffient
Large
0
0.2
0.4
0.6
0.8
1.0
FIGURE 6.23
Correlation among rule returns (3).
--- page 288 ---

the magnitude of the data-mining bias. These relationships pertain speciﬁ-
cally to data mining ventures where the performance statistic being used
is the rule’s mean rate of return. Because the sampling distribution of
other performance statistics, such as the Sharpe ratio, will differ from the
distribution of the mean return, the relationships between the ﬁve factors
and the data mining bias may also be different.
The astute reader will wonder how such curves could have been developed, given that a rule’s expected performance is never known (it is a
population parameter) but must be known to measure the data-mining
bias. The reader is correct; the data-mining bias is never known for actual
rules. However, it can be known for artiﬁcial rules and can therefore be
investigated. An artiﬁcial rule is a computer-simulated trading signal
290 METHODOLOGICAL, PSYCHOLOGICAL, PHILOSOPHICAL, STATISTICAL FOUNDATIONS
DM Bias
Number & Magnitude of Outliers Relative to Number of Observations Used to
Compute Performance Statistic
Large
0
Low
High
FIGURE 6.24
Presence of positive outlier returns (4).
DM Bias
Low Variance
(All Rules   Merit)
~~
High Variance
(One Very Superior Rule)
Large
0
FIGURE 6.25
Variance in expected ROI—degree of difference in merit in rule
universe(5).
--- page 289 ---

whose accuracy (fraction of correct signals) can be set experimentally.
This makes it possible to know the expected return of the artiﬁcial rule.
The preceding curves were based on a set of tests done on artiﬁcial rules.
The results of these tests, which are described in the next section, show
how the ﬁve factors impact the data-mining bias.
EXPERIMENTAL INVESTIGATION
OF THE DATA-MINING BIAS
Scientists make observations and draw inferences from them. Sound inferences depend on accurate observations. Thus, a key task is determining the
accuracy of the procedure used to make observations. The process of measuring the random and systematic error that may be present in an observational procedure is called calibration. One way to calibrate the accuracy of
a procedure is to test it on a problem whose correct answer is known. This
makes it possible to measure its random and/or systematic errors.
Objective technicians are the scientists of the TA world. Their primary
procedure is rule back testing. The observable produced is a performance
statistic. On the basis of this statistic, an inference is made about a rule’s
predictive power or expected performance. Therefore, objective technicians are properly concerned with the random and or systematic error
that that may be present in performance statistics obtained by back testing. Chapter 4 showed that performance statistics are subject to random
error due to sampling variability. This chapter is concerned with a form of
systematic error that stems from data mining—the data-mining bias.
This section describes the results of experiments that investigate the
data-mining bias by examining how each of the ﬁve factors impacts the
size of the bias. This is done by data mining a universe of artiﬁcial trading
rules (ATRs). Unlike real TA rules, ATRs are ideal for this purpose because their expected return can be known because it is under experimental control. This allows us to measure the data-mining bias associated
with the rule that had the best-observed performance. This, in turn, tells
us how accurately its observed performance, a statistic which is known to
the data miner, portrays its expected performance, the population parameter the data miner wishes to know.
Artiﬁcial Trading Rules and
Simulated Performance Histories
The ATR performance histories produced in these experiments are composed of monthly returns. The expected return of an ATR is controlled
Data-Mining Bias: The Fool’s Gold of Objective TA
291
--- page 290 ---

by manipulating the probability of a proﬁtable monthly return. This
probability can be expected to manifest over a very large number of
months, a manifestation of the Law of Large Numbers. However, over
any small sample of months, the actual fraction of proﬁtable months will
vary randomly about the speciﬁed probability level. This variation introduces the crucial element of randomness into the experiments. An ATR
performance history can be generated for any speciﬁed number of
months (e.g., 24).
When the probability of a proﬁtable month is known, as it is with an
ATR, its expected return can be determined precisely. This, in turn, allows
the data-mining bias associated with the rule to be measured. The expected return of an ATR is given by the formula used to compute the expected value of a random variable:
EV = p(proﬁtable month) × average gain – p(losing month)
× average loss
The average gain and average loss are also known because the ATRs
were applied to the absolute monthly percentage changes for the S&P 500
over the period August 1928 through April 2003. The term absolute means
the sign of the S&P’s actual monthly change was ignored. In the ATR tests
the algebraic sign (+ or –) of the ATR’s monthly return was determined by
a random process that is described below. Over this time period, comprising nearly 900 monthly observations, the average absolute monthly return
for the S&P 500 was equal to 3.97 percent. Thus, the formula for calculating an ATR’s expected return is:
ER = ppm × 3.97 – (1 – ppm) × 3.97
Where ppm is deﬁned as the probability of a proﬁtable month.
ATR performance histories were generated by Monte Carlo simulation. Speciﬁcally, the absolute monthly changes in the S&P 500 were sampled with replacement from the 900-month history. A monthly return,
without its sign, was chosen at random, and a roulette wheel, simulated
by a computer, determined if that particular month was a gain or loss.
This represented one month of the ATR’s performance history. The probability of a proﬁtable month was set by the experimenter. A probability of
0.70 would be as if the roulette wheel had 100 slots with 70 designated as
proﬁt and 30 designated as loss. This procedure for generating monthly
ATR returns was repeated for a speciﬁed number of months, another variable under experimental control. The performance history is then summarized with a statistic—mean monthly return, annualized. This procedure is
illustrated in Figure 6.26.
292 METHODOLOGICAL, PSYCHOLOGICAL, PHILOSOPHICAL, STATISTICAL FOUNDATIONS
--- page 291 ---

Let’s consider what the expected return for an ATR would be under four
different settings for probability of a monthly gain: 1.0, 0.63, 0.50, and 0.0. An
ATR with p(gain) set at 1.0 (all months proﬁtable) would have an expected
monthly return equal to the S&P 500’s average absolute monthly return of
+3.97 percent per month or a 47.6 percent annualized noncompounded return. This value can be obtained by plugging into the formula for the expected value of a random variable. The same formula tells us that an ATR
with probability of a gain month set to 0.63 would have an expected return of
+12.4 percent. An ATR with probability of gain set to 0.50 would have an expected return of zero whereas a probability of gain equal to zero would earn
a return of –3.97 percent per month or –47.6 percent per year.
Bear in mind that these are expected values that would be earned
over a very large number of months. Over any small number of months,
the ATR’s observed mean return can vary from this value. The smaller the
number of months comprising the ATR’s performance history, the larger
will be the random variation from the expected mean return.
To simulate the effect of data mining, for example picking the bestperforming ATR of 10, 10 ATR performance histories were generated. The
one with highest mean return was selected, and its observed return was
noted. This process was repeated a total of 10,000 times. The 10,000 observations were used to form the sampling distribution for the statistic—
mean return of the highest performing ATR selected from 10.
Experiment Set 1: Data Mining ATRs of Equal Merit
In the ﬁrst set of experiments, all ATRs were speciﬁed to have equal predictive power. This was accomplished by setting p(gain) to 0.50 for all
ATRs, thus giving them all an expected return of zero.
Data-Mining Bias: The Fool’s Gold of Objective TA
293
Absolute
Monthly
Returns
S&P 500
1928 -2003
Random Device
With
Probability of
Profitable month
Set Experimentally
Random
Sampling
With
Replacement
$
ATR
Performance
History
Of
M months
n-month mean
Return = ?
FIGURE 6.26
Monte Carlo generation of ATR performance histories.
--- page 292 ---

Factor 1: Number of Rules Tested.
All else being equal, the more
rules back tested to ﬁnd the best rule, the larger the data-mining bias.
More monkeys dancing on keyboards increases the probability that one
will get lucky enough to type something that appears literate. Similarly,
back testing a larger number of rules increases the chance that one will
enjoy extraordinary luck.
In the tests that follow, each ATR was simulated over a 24-month period. First let’s look at the no-data-mining case—only one rule is back
tested. There is no data mining and no data-mining bias. Although an ATR
with p(gain) set at 0.50 has an expected return equal to zero, sampling
variability makes it possible for any given 24-month history to produce a
mean return that varies above and below zero.
To demonstrate this, 1,000 ATR performance histories, each of 24
months’ duration, were produced by computer simulation. The sampling
distribution for the statistic mean annualized return is shown in Figure
6.27. As expected, the distribution is centered at zero, which is indeed the
expected return of an ATR with p(gain) set 0.50. Also as expected, the
mean return displays a wide range of variation around zero because 24 observations is a relatively small sample size. A few ATRs, those out in the
right tail of the sampling distribution, had very good luck (more than 50
months wound up proﬁtable). In the left tail of the distribution, we ﬁnd
the performance histories with bad luck. However, it is the center of the
sampling distribution that tells the story. On average, under the condition
of no data mining, an ATR with no predictive power can be expected to
294 METHODOLOGICAL, PSYCHOLOGICAL, PHILOSOPHICAL, STATISTICAL FOUNDATIONS
250
200
150
100
50
-48
-38
-29
-19 -9.6
48
38
29
19
9.6
0
FIGURE 6.27
Mean annualized  percent return (single ATR, 24 month history,
1,000 replications).
--- page 293 ---

earn a mean return of zero. As the next tests will show, when a bestperforming ATR is picked from two or more ATRs, the best is likely to show
a return greater than zero, even though it has an expected return of zero.
Now we will be data mining by picking a best ATR from two or more.
To examine the relationship between the size of the data mining bias and
the number of rules from which the best is selected we will vary the size
of the ATR universe—the number from which the best is picked. Speciﬁ-
cally, the bias is measured for the best ATR of 2, 10, 50, and 400. For example, if the number of ATRs was set at 10, the best-performing one of 10
was picked, and its observed mean return was noted. This procedure was
repeated 10,000 times and the sampling distribution for the statistic (observed return of the best ATR) was plotted. All performance histories are
24 months, all rules are set to p(gain) = 0.50 (expected return = 0), and all
rules are set to have independent returns (no correlation). Because all
ATRs had expected returns equal to zero, the data-mining bias is simply
equal to the observed return of the best performer averaged over 10,000
replications.
Figure 6.28 shows the sampling distribution of observed performance for the best ATR out of two. The sampling distribution is centered
at +8.5 percent. In other words, when only two ATRs are tested and the
best is selected, the bias is a positive 8.5 percent. The data miner would
be expecting +8.5 percent in the future, but we know the true expected
return is 0 percent.
If the number of ATRs is increased to 10, and the best is selected, the
data-mining bias increases to +22 percent. However, we know that the
selected ATR has a p(gain) of 0.50 and an expected return of 0 percent.
Data-Mining Bias: The Fool’s Gold of Objective TA
295
70
60
50
40
30
20
10
8.5 %
-70 -60 -50 -40 -30 -20 -10 0
Expected
Return
Best
ATR
Observed
Return
Best
ATR
Of
2 Rules
Relative
Freq.
f
0 %
Data Mining
Bias
+8.5%
FIGURE 6.28
Sampling distribution —mean return best of two ATRs.
--- page 294 ---

Figure 6.29 is similar to 6.28, except it shows the sampling distribution for
the mean observed return for the best-of-10 ATRs. The observed performance of the best-of-10 ATRs is biased by +22 percent.
When the size of the data-mined universe is expanded to 50 ATRs the
bias increases to +33 percent. Figure 6.30 shows the sampling distribution
for the mean return of the best-of-50 ATRs.
A similar plot, in Figure 6.31, shows that the data-mining bias increases to a +48 percent for the best-of-400 ATRs.
The relationship between number of ATRs tested and the data-mining
bias can be seen in Figure 6.32. It summarizes the results obtained for
296 METHODOLOGICAL, PSYCHOLOGICAL, PHILOSOPHICAL, STATISTICAL FOUNDATIONS
70
60
50
40
30
20
10
22 %
-70 -60 -50 -40 -30 -20 -10 0
Expected
Return
Best
ATR
Observed
Return
Best
ATR
Of
10
Relative
Freq.
f
0 %
Data Mining
Bias
+22%
FIGURE 6.29
Sampling distribution—mean return best of 10 ATRs.
70
60
50
40
30
20
10
33 %
-70 -60 -50 -40 -30 -20 -10 0
Expected
Return
Best
ATR
Observed
Return
Best
ATR
Of
50
Relative
Freq.
f
0 %
Data Mining
Bias
+33%
FIGURE 6.30
Sampling distribution—mean return best of 50 ATRs.
--- page 295 ---

best-of 2, 10, 50, and 400 ATRs. The vertical axis represents the magnitude
of the data-mining bias—the differential between the observed returns for
the best performing ATR and its expected return. The horizontal axis represents the number of ATRs back tested to ﬁnd the best. The relationship
is summarized by ﬁtting a curve through the four data points. It is nearly
linear when number of rules tested is plotted in log terms—log (base10).
The main point to take away from these experiments is this: The larger the
number of rules tested to ﬁnd a best rule, the greater the data-mining bias.
Data-Mining Bias: The Fool’s Gold of Objective TA
297
70
60
50
40
30
20
10
48 %
-70 -60 -50 -40 -30 -20 -10 0
Expected
Return
Best
ATR
Observed
Return
Best
ATR
Of
400
Relative
Freq.
f
0 %
Data Mining
Bias
+48%
FIGURE 6.31
Sampling distribution—mean return best of 400 ATRs.
1
2
10
50
400
Number of Rules Tested (log scale)
D
M
B
I
A
S
10 %
20 %
30 %
40 %
50 %
60 %
FIGURE 6.32
Data-mining bias versus number of rules tested (annualized percent return): 24-month performance history.
--- page 296 ---

It should be pointed out that the particular magnitudes of data-mining
bias shown in the preceding tests are valid only for the particulars of this
test: a particular set of S&P 500 monthly returns, a 24-month performance history, all rules have independent returns, and all rules having an
expected return equal to zero. In a different data-mining venture, with
different particulars, the same principle would apply (more rules produce a bigger bias) but the speciﬁc levels of the data-mining bias would
be different.
For example, had a longer performance history been used to compute
mean return—48 months instead of 24—the distribution of mean ATR returns would have clustered more tightly around the expected return of
zero. This is merely a manifestation of the Law of Large Numbers. Consequently, the bias associated with the highest performing ATR would have
been less. This tells us that the number of observations used to compute
the performance statistic is an important factor in determining the magnitude of the data-mining bias.
Let’s consider what was said in the previous sentence. The greater the
number of monthly observations used to compute the performance statistic, the smaller the dispersion of the statistic’s sampling distribution. In
other words, the larger the sample size used to compute the performance
statistic, the less the degree of randomness in observed performance and
the less the opportunity for an extraordinarily lucky performance. Whatever reduces the degree of randomness in observed performance reduces
the data-mining bias.
The importance of sample size on data-mining bias can be seen in
Figure 6.33. It is similar to the preceding Figure 6.32. It is a plot of datamining bias, represented on the vertical axis, as a function of number of
ATR’s compared to ﬁnd the best one, on the horizontal axis. However, in
this plot there are four curves instead of one. Each curve is based on using a different number of monthly observations to compute each rule’s
mean return; 10, 24, 100, and 1,000 months. The dotted line for 24
months is the same curve seen in Figure 6.32. Two points are worthy of
note. First, all curves rise as the number of rules back tested is increased. This is consistent with the ﬁnding discussed in the preceding
section—the data-mining bias increases as the number of ATR’s tested is
increased. Second, and perhaps most important, is the fact that the magnitude of the bias is reduced by increasing the number of months used to
compute the mean return. For example, when only 10 months of data
are used, the bias for the best-of-1,024 ATRs is approximately 84 percent. When 1,000 months of data are used, the bias for the best of 1,024
rules shrinks to less than 12 percent. In the next section, we will see why
the number of observations is so important in determining the size of the
data-mining bias.
298 METHODOLOGICAL, PSYCHOLOGICAL, PHILOSOPHICAL, STATISTICAL FOUNDATIONS
--- page 297 ---

Factor 2: Number of Observations Used to Compute the Performance Statistic.
Figure 6.33 tells us that increasing the number
of observations used to compute the performance statistic reduces the
magnitude of the data-mining bias. In fact, of all the factors impacting the
size of the bias, sample size may be the most important. The more observations used, the less opportunity there is for a few lucky observations
(proﬁtable months) to result in a high mean return. We saw this in Chapter 4, where it was demonstrated that the sampling distribution is reduced in width when a larger number of observations are used to
compute the sample statistic. With only a few observations, a sample
mean can stray considerably above or below the true population mean.
The message conveyed by a wide sampling distribution is that there is a
greater opportunity for a rule to generate a very proﬁtable return in a
back test by luck rather than by predictive power. This is illustrated in
Figure 6.34, which shows two sampling distributions for the same rule,
for which expected return is zero. Note the sampling distribution based
on fewer observations is wider. A mean return computed from a short
performance history is more likely to produce a very lucky result than a
mean computed from a larger number of observations (i.e., a longer performance history).
The next set of experiments examine the effect of the number of
monthly observations used to compute mean ATR return on the size of
the data-mining bias. The number of months was varied from one month
to 1,000 months, in 50-month increments, with data-mining bias computed at each increment. This was done for two cases: the best-of-10 and
Data-Mining Bias: The Fool’s Gold of Objective TA
299
Number of ATR s (log scale)
10 mos.
100 mos.
1000 mos.
12
24
24
36
48
48
60
72
84
96
1024
256
64
16
4
1
24 mos.
D
M
B
I
A
S
%
Yr.
FIGURE 6.33
Data-mining bias versus number of ATRs tested for different sample sizes.
--- page 298 ---

the best-of-100 ATRs. As in prior experiments all ATRs were set to have
expected returns equal to zero.
Figure 6.35 shows the relationship between the data-mining bias on
the vertical axis versus the number of observations used to compute
ATR mean returns on the horizontal axis. Because the expected return
for all ATRs is equal to zero, the data-mining bias is equal to the average
observed performance of the best. Thus, the vertical axis, which is labeled data-mining bias, could as easily have been labeled average performance of the best rule. Note the steep decline in the magnitude of
300 METHODOLOGICAL, PSYCHOLOGICAL, PHILOSOPHICAL, STATISTICAL FOUNDATIONS
Sample Mean Computed From
Large Number of Observations
Lucky Rule
Appears
Highly Profitable
0
0
+10%
-10%
Sample Mean Computed from
Small Number of Observations
+10%
-10%
+30%
-30%
Lucky Rule
Appears
Modestly Profitable
FIGURE 6.34
Narrow versus wide sampling distributions.
12
24
36
48
48
60
72
84
96
1000
800
600
400
200
1
Observed Performance
Best-of-10 ATRs
Number of Months Used To Compute Mean ATR Return
Observed Performance
Observed Performance
Best-of-100 ATRs
D
M
B
I
A
S
%
Yr.
FIGURE 6.35
Data-mining bias versus number observations.
--- page 299 ---

the bias as the number of observations used to compute the mean return
is increased. This is the Law of Large Numbers working in favor of the
data miner.
The lesson here is this: Be very skeptical of performance statistics
computed from a small number of signals or time intervals. Another important message from Figure 6.35 is that when the number of observations (months) becomes quite large, 600 or so, the difference in the bias
between best-of-10 and the best-of-100 ATRs becomes tiny. This ﬁnding
has very important implications for the data miner—when the number of
observations is sufﬁcient, one can data mine a much larger number of
rules without signiﬁcantly increasing the data-mining bias. The Law of
Large Numbers rules!
Factor 3: Degree of Rule Correlation.
The third factor affecting
the size of the data-mining bias is the degree of similarity among the rules
tested. Rules are said to be similar when they generate performance histories that are strongly correlated. That is to say, their monthly or daily returns are correlated. The stronger the correlation between the rules
tested, the smaller will be the magnitude of the bias. Conversely, the lower
the correlation (i.e., the greater the degree of statistical independence) between rules returns, the larger will be the data-mining bias.
This makes sense because increased correlation among the rules has
the consequence of shrinking the effective number of rules being back
tested. Imagine a large set of rules that are completely identical. Naturally,
they will generate perfectly correlated performance histories. In effect,
this large set of rules is really just one rule, and we already know that the
data-mining bias shrinks to zero when only one rule is back tested. Backing off from this extreme case, when rules are highly similar, and thus
have highly correlated returns, the chance of an extraordinarily lucky performance is reduced. The more dissimilar the rules, the greater will be the
opportunity for one to have a great coincidental ﬁt to the historical data
and achieve high performance. So high correlation amongst the rules
shrinks the effective number of rules back tested and hence shrinks the
data-mining bias.
In practical terms, rule correlation is most likely to be high when data
mining involves optimizing the parameters of a speciﬁc rule form. Suppose a dual moving average crossover rule is being optimized. This means
that every rule tested is the same except for the parameter values—the
number of days used to compute the short-term and long-term moving averages. The rule using values of 26 days and 55 days will produce returns
that are highly correlated with a rule using values of 27 and 55.
Figure 6.36 shows the relationship between the magnitude of the datamining bias for the best rule (vertical axis) and the degree of correlation
Data-Mining Bias: The Fool’s Gold of Objective TA
301
--- page 300 ---

(horizontal axis) among the rules. Rule correlation was simulated as follows: An initial ATR performance history was generated. In the generation
of a second ATR history, a biased random device was consulted to determine the monthly returns of ATR history 2. The bias was set to the desired
level of correlation. For example, if a .7 correlation was desired, a coin ﬂip
was simulated with the probability of heads = 0.70. If the coin landed on
heads, then the monthly return for the second ATR would be the same as
the monthly return of the initial ATR. This was continued for subsequent
ATR histories.
Each ATR was simulated over a 100-month history. Three different
tests were run, each based on a different number of ATRs: 10, 100, 1,000.
In other words, one test measures the data-mining bias associated with
the best ATR rule out of 100. As in prior tests, all rules had expected returns equal to zero. The vertical axis of the plot represents the datamining bias. The factor being examined here, rule correlation, was varied
from 0 to 1.0. Note that the bias remains high until rule correlations approach a level of 1.0. Thus, rule correlation does not have a major impact
in reducing the data-mining bias until there is a high level of correlation in
their returns. Also note that the data-mining bias is higher for the best of
1,000 rules than it is for best of 10. This is simply a manifestation of factor
1, the greater the number of rules from which the best is selected, the
greater the data-mining bias.
Factor 4: Presence of Positive Outliers in Rule Returns.
A
sample of rule returns (daily, weekly, or monthly) that contains a few extremely large positive observations has the potential to create a large data
302 METHODOLOGICAL, PSYCHOLOGICAL, PHILOSOPHICAL, STATISTICAL FOUNDATIONS
0.2
0.4
0.6
0.8
1.0
0
24
18
12
6
Best of 1000 ATRs
Best of 100 ATRs
Best of 10 ATRs
Rule Correlation
Data
Mining
Bias
%
Yr.
FIGURE 6.36
Data-mining bias versus rule correlation (annualized percent return number of monthly observations = 100).
--- page 301 ---

mining bias. The size of the bias will depend on how extreme the values
are and the number of observations used to compute the mean. If a small
number of observations are used, one extremely positive value can boost
the sample mean dramatically. A large number of observations will lessen
the impact of an occasional extreme value.
Distributions that contain extreme values are said to have heavy tails.
The tails of a distribution are the outer right and left zones where the extreme but rare observations lie. Heavy-tailed distributions extend farther
away from the distribution’s center than light-tailed distributions. The normal distribution has light tails. Figure 6.37 illustrates this distinction. The
distribution in the upper portion of Figure 6.37 has the normal bell shape.
Note how quickly the tails disappear as one moves away from the distribution’s center. This tells us that extreme observations are rare to the point
of being virtually nonexistent. People’s heights are normally distributed. It
is rare to see someone over seven feet tall. No one has ever seen a person
over 10 feet. The distribution in the lower portion of the ﬁgure is heavy
tailed. Although extreme observations are also rare, they occur more frequently than in light-tailed distributions. Were people’s heights distributed
this way, you might meet someone 20 feet tall!
As mentioned earlier, when the distribution of daily (weekly, monthly)
returns contains extreme observations, a sample mean, computed from
these observations, can also take on an extreme value. This occurs when
one or more of the extreme values wind up in the sample and the sample
size is small. From this it follows that heavy tails in the return distribution
tend to cause tail heaviness of the sampling distribution of the mean.
Data-Mining Bias: The Fool’s Gold of Objective TA
303
Heavy Tails
Light Tails
0
0
Outliers:
Extreme Positive
Months, Days, Etc.
FIGURE 6.37
Lightversus heavy-tailed return distributions.
--- page 302 ---

Nevertheless, the value of a sample mean is never as extreme as the most
extreme value found in a sample. This is simply the effect of averaging.
Therefore, the sampling distribution of the mean return will always have
lighter tails than the distribution of interval returns. This is illustrated in
Figure 6.38. Two return distributions are depicted. On the left is a return
distribution with heavy tails. The sampling distribution of the mean based
on this distribution also has heavy tails, although they are lighter than the
return distribution itself. On the right is a thin-tailed return distribution. A
sampling distribution of the mean based on it necessarily has light tails.
Note that both of the sampling distributions in the Figure 6.38 are
based on the same sample size. Sample size is a separate factor inﬂuencing tail heaviness of the sampling distribution. I wanted to hold sample
size constant so as not to confuse the issue.
Now let’s consider the effect of sample size on the sampling distribution’s tail heaviness. When more observations are used to compute the
sample mean, the effect of tail heaviness in the return distribution is minimized. The greater the number of observations used to compute the sample mean, the lighter will be the tails of the sampling distribution. This is
illustrated in Figure 6.39. The return distribution clearly has heavy tails.
On the left is the sampling distribution of the mean based on a small sample size. Its tails, though not as heavy as the return distribution itself, are
still heavy. On the right is a sampling distribution of the mean derived
from the same return distribution, except that a larger sample size is used
304 METHODOLOGICAL, PSYCHOLOGICAL, PHILOSOPHICAL, STATISTICAL FOUNDATIONS
Return Distribution: Heavy Tails
Return Distribution: Light Tails
Resulting
Sampling Distribution of
the Mean
Resulting
Sampling Distribution of
 the Mean
0
                 0
0
0
FIGURE 6.38
Impact of extremes in return distribution on sampling distribution: equal sample size.
--- page 303 ---

to compute the sample mean. The tails of this sampling distribution are
lightened as a result.
What is the relevance of all this to the data-mining bias? A heavytailed sampling distribution is saying that randomness is playing a large
role in the mean return. Randomness is always bad news for the data
miner.31 Imagine two rules. Both have expected returns of zero. One has a
heavy-tailed sampling distribution. The other has a sampling distribution
with light tails. The heavy tails tell us that there is a greater probability
that the rule will produce a mean return, in a back test, that is much
higher than its expected return. If this rule is picked by the data miner, its
data-mining bias will be large and its out-of-sample performance is likely
to be disappointing. This is illustrated in Figure 6.40. The heavy-tailed
sampling distribution shows that it is within the realm of probability for
the rule to earn mean return of greater than 30 percent in a back test. In
the case of the sampling distribution with light tails, a return that high
would have a probability of almost zero.
It is widely recognized that the distribution of stock market returns
and the returns of other ﬁnancial asset have relatively heavy tails compared to a normal distribution.32 A rule that was short, by coincidence,
when the market crashed may win the data-mining-performance competition, but it will have won for the wrong reason.
The issue of tail heaviness and its resultant impact on the data-mining
Data-Mining Bias: The Fool’s Gold of Objective TA
305
Return Distribution: Heavy Tails
0
Sampling Distribution
 Small Sample Size
(Tails Still Heavy)
Sampling Distribution
 Large Sample Size
(Lighter Tails)
0
                     0
FIGURE 6.39
Impact of sample size on tail heaviness of the sampling
distribution.
--- page 304 ---

bias was examined experimentally. The data-mining bias was compared
for two sets of ATRs. One set used the S&P 500 monthly returns, a distribution with tails that are heavier than those of the normal distribution, to
generate performance histories. The other set of ATRs used a return distribution with intentionally light tails. As in the other experiments, the
ATR with the best-observed performance was selected and its data-mining
bias was measured. The results of these experiments were clear. The datamining bias was much less pronounced for the ATRs that were based on
the light-tailed return distribution. This ﬁnding is of practical value only
when data-mining rules exit at ﬁxed targets. This has the effect of eliminating extreme outcomes. This in turn has the effect of reducing tail heaviness in the sampling distribution of the performance statistic. In most
instances, however, rule researchers are stuck with the return distributions produced by ﬁnancial market behavior. Because markets are subject
to extreme events, mean rule returns will tend to be extreme as well.
Factor 5: Variation in Expected Returns among the ATRs.
This factor refers to the degree of variation in the expected returns among
the set of rules considered during data mining. The ATR experiments discussed thus far have considered ATRs with uniform predictive power. All
have had expected returns set at zero. When all rules are of equal merit,
be that merit none, low, or high, any differences in their observed performances are due entirely to luck. In such a case, the winner of the datamining performance competition will simply be the luckiest rule. Thus,
the difference between its observed mean return and its expected return
will be large. Therefore, when all rules possess equal expected returns,
the data-mining bias will be large.
306 METHODOLOGICAL, PSYCHOLOGICAL, PHILOSOPHICAL, STATISTICAL FOUNDATIONS
0
0
Extraordinarily
Lucky
Back-Tests
+10%
-10%
+10%
-10%
+30%
-30%
Expected Return
Expected Return
FIGURE 6.40
Lightversus heavy-tailed sampling distributions.
--- page 305 ---

However, if the universe of rules explored during data mining differs
with respect to their expected returns, the data-mining bias will tend to be
smaller. Under certain conditions, it will be very small. The following experiments investigate how variation in expected returns with the rule universe impacts the data-mining bias. This is accomplished by creating a
universe of ATRs that have differing levels of expected return. Recall, that
an ATR’s expected return is entirely determined by its designated probability of a proﬁtable month.
Let’s ﬁrst consider what the following experiments should show. Suppose a universe of ATRs contains one that is truly superior to all the others. It has an expected return of +20 percent, whereas the others all have
expected returns of zero. We would expect its true superiority to reveal itself by producing the highest-observed performance most of the time (on
any given test it is not guaranteed to do so). Consequently, most of the
time the superior ATR will get picked and the data-mining bias associated
with it will tend to be small. The bias will tend to be small because its observed performance was earned the old-fashioned way, by dint of predictive power rather than luck.
Experiment 2: Data Mining ATRs with Differing
Expected Returns
The following tests investigate the data-mining bias within a universe populated by ATRs whose expected returns differ. In these tests, the majority
of ATRs have expected returns equal to zero or close to zero. However, a
few ATRs with returns signiﬁcantly greater than zero are sprinkled in.
This is intended to replicate the world a rule data miner can reasonably
hope to encounter—there really is some TA gold in the mountains of data
although it is rare.
In addition to investigating the magnitude of the data-mining bias, this
set of tests also addresses another question: Does data mining rest on a
sound premise? That is, does picking the rule with the best-observed performance do a better job of identifying authentic predictive power than
randomly selecting a rule from the universe of rules. Data mining must, at
the very least, pass this minimal test of efﬁcacy to establish that it is a
reasonable research approach. Figure 6.41 shows the expected return for
an ATR given its speciﬁed probability of a proﬁtable month. Bear in mind
that this graph is speciﬁc to the monthly SP returns used in these simulation experiments.
Recall that an ATR’s expected return is determined entirely by its
probability-of-proﬁtable-month (PPM). The following tests assume that
rules with high expected returns are rare. To simulate this assumption, the
PPM assigned to each ATR was drawn at random from a distribution of
Data-Mining Bias: The Fool’s Gold of Objective TA
307
