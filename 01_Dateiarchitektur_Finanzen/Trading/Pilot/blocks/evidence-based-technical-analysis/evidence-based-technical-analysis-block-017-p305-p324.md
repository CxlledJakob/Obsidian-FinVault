# Evidence-based Technical Analysis_ Applying the Scientific Method and Statistical Inference to Trading Signals.pdf — pages 305–324

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
--- page 306 ---

PPMs. The distribution used for this purpose has a shape similar to the
distribution of wealth in a society. It has a long tail out to the right, indicating that wealthy individuals, like Bill Gates, are extremely rate while a
great many are poor. The distribution of expected returns used for these
experiments was deﬁned such that an ATR with an expected return of 19
percent per year or greater had a frequency of occurrence of about 1 in
10,000. The expected return for the average ATR in the universe was +1.4
percent per year. The approximate shape of the distribution used is illustrated in Figure 6.42.
Although the speciﬁc assumptions underlying this distribution may
not be accurate, they are probably correct to within one order of magnitude. This is based on the performance of the best hedge funds using
308 METHODOLOGICAL, PSYCHOLOGICAL, PHILOSOPHICAL, STATISTICAL FOUNDATIONS
Probability of Profitable Month
0 %
10 %
20 %
30 %
40 %
50 %
60 %
1.0
0.90
0.80
0.70
0.60
0.50
FIGURE 6.41
Expected return (f) probability of proﬁtable month.
0
Frequency
Expected ATR Return
1.4%
19%
FIGURE 6.42
Distribution of ATR expected returns.
--- page 307 ---

technical analysis. However, for purposes of these experiments, the
speciﬁcs are not crucial. The real purpose here is to measure the datamining bias in a universe of rules whose expected returns differ and to investigate how the bias can thwart the objective of data mining, ﬁnding
merit in a universe where it is rare.
Is Data Mining Based on a Sound Premise?—
A Qualiﬁed Yes!
This section addresses the important fundamental question: Is data mining based on a sound premise? This is really two questions. First, is observed mean return a useful indicator of rule merit in the sense that the
rule with the highest observed mean return has a higher expected return
than a rule picked at random? If a randomly selected rule is as likely to
perform well in the future as a rule that performed well in a back test,
then data mining is a pointless activity. Second, is more data mining better? That is, does testing a larger number of rules lead to the discovery of
a rule with higher expected returns? If so, then back testing 250 rules
would be a better idea than back testing only ten.
Fortunately for the ﬁeld of data mining, the answer to both questions
is a qualiﬁed yes. The qualiﬁcation relates to the number of observations
that are used to compute the rule’s mean return or other performance statistics. If a sufﬁcient number of observations is used, then the answer to
both questions is yes. This is very good news for the data miner. However,
when the number of observations is small, data mining does not work.
One would do just as well picking a rule by guess, and data mining a larger
number of rules will not produce better rules.
Because the number of observations used is crucial, no doubt
the reader would like to know how many are sufﬁcient. Unfortunately,
there is no simple answer. The requisite number depends on the performance statistic and the nature of the raw data. The best I can do is to
provide representative charts that give a general sense of requisite sample sizes.
In prior plots, the vertical axis represented the data-mining bias in annualized percent return per year. Take note, however, that in Figure 6.43,
the vertical axis represents the true merit or expected return of the rule
with the highest-observed performance—the rule that would be selected
by the data miner. Clearly, such a plot could not be produced for actual TA
rules because their expected returns are never known. The horizontal
axis represents the number of ATRs tested to ﬁnd the one with the bestobserved performance. The set of numbers considered was: 1 (no data
mining), 2, 4, 8, 16, 32, 64, 128, and 256. There are three curves on the plot.
Each curve is based on a different number of monthly observations used
Data-Mining Bias: The Fool’s Gold of Objective TA
309
--- page 308 ---

to compute the ATR’s mean annual return. The number of monthly observations used for these three cases were: 2, 100, and 1,000.
The second question posed was the following: Does testing more
rules lead to the discovery of a rule with a higher expected return? If so,
the curve of expected return should rise as the number of ATRs examined to ﬁnd the best one goes up. In other words, the expected return of
the ATR with the best-observed performance should be positively correlated with the number tested to ﬁnd the best. On the other hand, if the
curve does not rise, it would be telling us that more searching does not
lead to rules of higher merit. This would mean that data mining is a
fruitless activity.
In Figure 6.43, two of the three curves rise—the one based on 100
monthly observations and the one based on 1,000. This tells us that back
testing more rules leads to the discovery of higher merit rules. The curve
based on 1,000 rises more steeply than the one based on 100. This is
telling us that when performance statistics are computed from a larger
number of observations, data mining more reliably leads to better rules.
This is good news for data miners who pay attention to the issue of sample size.
The curve in Figure 6.43 that does not rise also tells a story: When too
few observations are used to compute the performance statistic, data mining does not work. That is to say, testing more rules does not lead to the
discovery of better rules. The ﬂat curve shows that when only two months
were used to compute the mean return of each ATR, the expected return
of the best performing ATR out of 256 ATRs was no higher than the best
310 METHODOLOGICAL, PSYCHOLOGICAL, PHILOSOPHICAL, STATISTICAL FOUNDATIONS
Number of ATRs Tested To Find The Best
n =2
n =1000
n =100
2.4%
4.8%
7.2%
9.6%
64
128
256
1
Universe
Average
Expected
Return
1.4%/yr
Expected
Return
% / Yr.
32
FIGURE 6.43
Expected return of best performing ATR versus number of ATRs
back tested.
--- page 309 ---

performing ATR when only one was tested (i.e., no data mining). The importance of sample size cannot be over emphasized!
Now let’s go back and address the ﬁrst question: Does data mining select rules with higher expected returns than simply picking one at random
from the universe? Figure 6.43 speaks to this question as well. Note the
curve based on two observations remains stuck at +1.4 percent as the number of ATRs tested is increased. A return of +1.4 percent is the expected return of the average ATR in the ATR universe. In other words, if one were to
grab an ATR at random from the universe and note its expected return and
repeat this many times, on average the expected return of the randomly selected rule would be +1.4 percent. Figure 6.41 tells us that when only two
months of observations are used, picking the ATR with the best-observed
performance is no better than picking an ATR at random. The fact that the
curve is ﬂat says that it does not matter how many ATRs are tested. However, the curves based on 100 and 1,000 observations rise well above the
universe average. For example, when a best is picked from 256 ATRs using
1,000 months of history to compute the observed mean return, its expected
return is +10 percent a year, far above the universe average of +1.4 percent.
The bottom line: When there are a sufﬁcient number of observations a
rule’s observed rate of return is a useful, though positively biased, indicator of its expected rate of return. However, when there are too few observations, the observed rate of return is virtually useless.
Data-Mining Bias as a Function of Universe Size:
In a Universe of Variable Merit
The previous section established that the payoff from data mining increases as the number of rules tested is increased, given sufﬁcient sample
size. This shows that observed performance of the best rule is a useful,
though positively biased, gauge of its expected return. The question is:
How large is this bias associated with the best rule (highest observed return) when the universe is composed of rules that differ in terms of their
expected returns?
The ﬁgures that follow (Figures 6.44, 6.45, 6.46, 6.47) are plots of the
data-mining bias (vertical axis) versus the number of rules back tested in
a rule universe where merit is distributed according to the distribution
displayed in Figure 6.42. Each plot is based on a different number of
monthly observations for computing mean return: 2, 100, and 1,000
months, respectively. First, each curve is shown individually (Figures
6.44, 6.45, and 6.46). Figure 6.47 shows the three curves placed on top of
one another. It gives a sense of the relative magnitude of the data-mining
bias at different sample sizes.
Data-Mining Bias: The Fool’s Gold of Objective TA
311
--- page 310 ---

Figure 6.44 is based on using only two months of observations to compute each ATR’s observed return. The ﬁgure clearly shows the problem
created by using a small sample size. For example, the observed performance of the best performing ATR out of 256 ATRs overstates its expected
return by over 200 percent per year. For short performance histories, the
data-mining bias is extreme. However, for the 100-observation case,
shown in Figure 6.43, and for the 1,000 observation case shown in Figure
6.44, the bias is dramatically smaller. For example, the bias associated
with the best ATR of 256 is approximately 18 percent when 100 months
are used and less than 3 percent when 1,000 months are used.
312 METHODOLOGICAL, PSYCHOLOGICAL, PHILOSOPHICAL, STATISTICAL FOUNDATIONS
Length ATR Performance
History: 2 Months
Number of ATRs Tested To Find Best
Data
Mining
Bias
Of
Best
ATR
Annual
% Return
60
120
180
240
64
128
256
1
32
FIGURE 6.44
Data-mining bias versus number of ATRs tested in variable merit
rule universe using a two-month performance history.
Number of ATRs Tested To Find The Best
2.4
4.8
7.2
9.6
64
128
256
1
32
Data
Length ATR Performance
History: 100 Months
Mining
Bias
Of
Best
ATR
Annual
% Return
FIGURE 6.45
Data-mining bias versus number of ATRs tested in variable merit
rule universe using a 100 month performance history.
--- page 311 ---

There are two messages expressed by Figures 6.44, 6.45, and 6.46.
First, the number of observations has a major impact on data-mining bias.
Second, when the number of observations used to compute rule performance is large, the bias levels out quickly. This is seen Figure 6.46 based
on 1,000-month performance histories. The data-mining bias of the best of
16 ATRs is not much worse than the best of 256. Figure 6.47 superimposes
the prior three ﬁgures. It shows that searching a larger number of ATRs to
ﬁnd a best (i.e., more data mining) does not increase the magnitude of the
bias once the number of ATRs tested exceeds a modest number. In other
words, the penalty for testing more rules does not increase, once a rather
Data-Mining Bias: The Fool’s Gold of Objective TA
313
Number of ATRs Tested To Find The Best
1.2
1.8
0.6
2.4
3.0
64
128
256
1
32
Data
Length ATR Performance
History: 1000 Months
Mining
Bias
Of
Best
ATR
Annual
% Return
FIGURE 6.46
Data-mining bias versus number of ATRs tested in variable merit
rule universe using a 1,000-month performance history.
Number of ATRs Tested To Find The Best
60
120
180
240
64
128
256
1
32
90
150
30
210
Data
Mining
months=100
months=1000
months=2
Bias
Of
Best
ATR
Annual
% Return
FIGURE 6.47
Data-mining bias versus number of ATRs tested in variable merit
rule universe.
--- page 312 ---

low threshold number of rules has been exceeded, provided, of course,
that a sufﬁcient number of observations has been used to compute the
performance statistic.
How quickly the data-mining bias stabilizes once this threshold is
passed can be seen more clearly in Figure 6.48, which is a portion of the
curve for the 100-month observation case magniﬁed. It shows the region
along the horizontal axis where the number of ATRs tested is between 1
and 40. After approximately 30 ATRs have been examined, increasing the
number tested has a minimal effect on the size of the data-mining bias.
This is good news for the data miner who utilizes an adequate number of
observations. The bottom line: testing a larger number of rules is a good
thing, and the penalty for doing so drops off quickly if a sufﬁcient number
of observations are used to compute the performance statistic that is used
for rule selection.
Data-Mining Bias as a Function of Number of
Observations: In a Universe of Variable Merit
This section presents a series of plots showing the relationship between
the magnitude of the data-mining bias (vertical axis) and the number of
monthly observations used to compute the observed performance statistic (horizontal axis). This effect was visible on prior plots by showing separate curves of the bias versus number of ATRs for distinct values of 2,
100, and 1,000 months. However, the plots presented in this section show
the relationship between the bias and number of observations along a
continuum of the number of months.
314 METHODOLOGICAL, PSYCHOLOGICAL, PHILOSOPHICAL, STATISTICAL FOUNDATIONS
Number of ATRs Tested To Find The Best
Length ATR Performance
History: 100 Months
4.8
9.6
14.4
1
10
20
30
40
7.2
12.0
2.4
16.8
Data
Mining
Bias
Of
Best
ATR
Annual
% Return
FIGURE 6.48
Data-mining bias stabilizes quickly when sample size is sufﬁcient.
--- page 313 ---

Each plot shows the data-mining bias as a function of number of observations, with that number ranging from 1 month to 1,024 months. What
we would expect to see, on the basis of previous ﬁndings, is for the bias to
be large when the number of observations is small. This is indeed what occurs. The message to the data miner is clear: Heed the Law of Large Numbers. Figures 6.49, 6.50, and 6.51 show the data-mining bias versus the
number of observations used to compute mean ATR return for three different cases: best ATR of 2, best of 10, and best of 100, respectively. Figure
6.52 shows the three curves superimposed.
Data-Mining Bias: The Fool’s Gold of Objective TA
315
Number of Observations to Compute Mean Return
6
12
18
1
200
400
600
800
1000
9
15
3
21
24
Data
Mining
Bias
Of
Best
ATR
Annual
% Return
FIGURE 6.49
Data-mining bias versus number of observations for best ATR of 2.
Number of Observations to Compute Mean Return
12
36
1
200
400
600
800
1000
24
48
60
Data
Mining
Bias
Of
Best
ATR
Annual
% Return
FIGURE 6.50
Data-mining bias versus number of observations for best ATR of 10.
--- page 314 ---

Observed Performance and Expected Performance
versus Number of Observations in a Universe
of Variable Merit
Figures 6.53 and 6.54 display two curves. The upper curve is the observed
performance of the best-performing ATR amongst, say, 10 ATRs. The
lower curve shows the expected return for that best-performing ATR. The
vertical axis represents annualized return, both observed and expected.
The horizontal axis represents the number of monthly observations. So,
for example, in Figure 6.53, point A on the upper curve represents the observed performance of the best ATR out of 10 when 400 observations were
316 METHODOLOGICAL, PSYCHOLOGICAL, PHILOSOPHICAL, STATISTICAL FOUNDATIONS
Number of Observations to Compute Mean Return
24
48
72
1
200
400
600
800
1000
36
60
12
84
96
Data
Mining
Bias
Of
Best
ATR
Annual
% Return
FIGURE 6.51
Data-mining bias versus number of observations for best ATR
of 100.
Number of Observations to Compute Mean Return
Best of 100
24
48
72
1
200
400
600
800
1000
36
60
12
84
Best of 10
Best of 2
Data
Mining
Bias
Of
Best
ATR
Annual
% Return
FIGURE 6.52 Data-mining bias versus number of observations for best ATR of 2,
10, and 100.
--- page 315 ---

used to compute the ATR’s observed mean return. Point B represents that
ATR’s expected return. The vertical distance between them is the datamining bias, given these speciﬁc conditions: best of 10 ATRs and 400
monthly observations.
Here is what we should anticipate, given the results of prior experiments. When the number of observations is small, randomness will dominate merit, and observed performance will be much greater than expected
performance—a large data-mining bias. This will show up on the plot as
the two curves being far apart. The large vertical gap between the curves
occurs when the performance statistic is based on few observations because this permits one ATR to get very lucky. However, as more observa-
Data-Mining Bias: The Fool’s Gold of Objective TA
317
 6
12
18
24
30
36
Observed
Performance
Best ATR of 10
A
B
%
Return
Per
Year
Number of Observations to Compute Mean Return
Expected
Performance
Best ATR of 10
200
400
1
600
800
1000
FIGURE 6.53
Observed and expected performance best ATR versus number of
observations based on 10 ATRs.
12
24
36
48
60
Observed
Performance
Best ATR of 500
%
Return
Per
Year
Number of Observations to Compute Mean Return
Expected
Performance
Best ATR of 500
200
400
1
600
800
1000
FIGURE 6.54
Observed and expected performance best ATR versus number of
observations.
--- page 316 ---

tions are used to compute mean return, the curves should converge as observed performance more truly represents expected performance. However, the curve of observed performance will always lie above the curve of
expected performance because a best-of-selection criterion will always induce some positive bias when luck plays a role in observed performance.
These tests were run for two cases. Figure 6.53 shows the curves for
the best ATR of 10. Figure 6.54 shows them for the best ATR of 500. As expected, the bias shrinks as the number of observations is increased (the
curves converge). Also, as expected, the bias is greater for the 500 ATR
case than for the 10 ATR case due to the greater opportunity for luck
when more ATRs are examined to ﬁnd a best.
Data-Mining Bias as a Function of Rule
Correlation: In a Universe of Variable Merit Based
on 500 ATRs
We have previously seen that when the returns of the candidate rules are
correlated, it reduces the data-mining bias. Correlation shrinks the bias
because correlation reduces the effective number of rules being examined. In the extreme case, where all rules have perfectly correlated returns, there is really only one rule being tested. In this situation, no data
mining takes place, and so the data-mining bias shrivels to zero. These results were for a universe of rules of equal merit; all had expected returns
of zero. Now results for a variable-merit universe are presented.
Figure 6.55 plots the expected return (vertical axis) of the universe’s best-performing ATR as the number of ATRs examined (horizontal axis) is varied from 1 to 256. There are four curves, each
318 METHODOLOGICAL, PSYCHOLOGICAL, PHILOSOPHICAL, STATISTICAL FOUNDATIONS
1.2
2.4
3.6
4.8
Expected
Return
% / Year
Number of ATRs Tested To Find Best (log scale)
4
16
1
6
4
256
0.9
0
0.6
0.3
FIGURE 6.55
Expected return of best ATR versus number of ATRs. Tested at
four levels of correlation: 0, 0.3, 0.6, 0.9. Number of observations= 100.
--- page 317 ---

representing a different level of correlation in returns amongst the
ATRs from which the best is selected. The correlation levels are: 0.0,
0.3, 0.6, and 0.9. The number of monthly observations used to compute
ATR mean return is set at 100 months.
The ﬁrst thing to note about Figure 6.55 is that the higher the level of
correlation, the less the expected return of the best-performing one. This is
consistent with the previous ﬁnding that when fewer ATRs are back tested,
there is less opportunity to discover better ones (see Figure 6.43). Higher
correlation means we are effectively searching through a smaller universe
than the actual number of ATRs tested would suggest. As pointed out earlier,
in the extreme case in which correlation is 1.0, there is no data mining at all.
When the correlation among the ATR returns is nearly perfect, 0.9, the expected return of the best of 256 ATRs is only +1.4 percent. This is the same as
an ATR picked at random. In other words, at a correlation of 0.9 the effective
number of ATRs being tested is quite small (little data mining). Less data
mining means less opportunity to ﬁnd good rules. Conversely, when correlation among rule returns is zero, the effective size of the universe is maximized—we really are searching among 256 different ATRs. Consequently, the
expected return of the best ATR out of 256 is nearly 4 percent, considerably
above the universe average of +1.4 percent (data mining works!).
Summary of Findings Regarding the
Data-Mining Bias
This section has presented the results of numerous experiments. It is
worthwhile, at this point, to summarize our ﬁndings. They make clear the
nature of the problem that must be solved by the methods presented in
the next section.
1. The observed performance of a rule discovered by data mining—that
is, the best performer in a set of back-tested rules—is positively biased. Its expected future return is less than its observed historical
performance. Its likely performance in any sample of data from the future will be lower than the back-tested performance that allowed it to
win the performance competition.
2. The magnitude of the data-mining bias is profoundly affected by the
number of observations used to compute the performance statistic
used to select the best rule. The number of observations affects both
the width and tail thickness of the performance statistic’s sampling
distribution.
a. The larger the number of observations, the narrower the sampling
distribution and the smaller the data-mining bias.
Data-Mining Bias: The Fool’s Gold of Objective TA
319
--- page 318 ---

b. The larger the number of observations, the lighter the tails of the
sampling distribution and the smaller the data-mining bias.
3. The larger the number of rules searched, the larger the data-mining
bias.
4. The smaller the variability in true quality (expected return) among the
rules tested, the larger will be the data-mining bias. In other words,
the more equivalent the predictive power of the rules back tested, the
greater will be the bias. This point was not explored experimentally.
5. Data mining works when the sample size is large. The more rules
tested, the higher the expected performance of the rule ultimately selected. Data mining does not work when the sample size is too small.
SOLUTIONS: DEALING WITH THE DATA-MINING BIAS
Data mining works but its results are positively biased. Hence, if the set of
candidate rules examined by the data miner contains any rules with superior expected returns, data mining can be an effective way to ﬁnd them.
However, their future performance will, in all probability, be less than
their back-tested performance. This out-of-sample performance deterioration is simply a fact of life in the data-mining business.
A worse problem occurs when all candidate rules are worthless—all
have expected returns of zero or less. In this instance, the data miner runs
the risk of being fooled by the data-mining bias and choosing a rule whose
expected return is zero. This is the fool’s gold of the objective technician.
This section discusses some ways to reduce this risk.
Three approaches have been proposed: out-of-sample testing, a datamining correction factor proposed by Markowitz and Xu, and randomization methods. Out-of-sample testing involves excluding one or more
subsets of the historical data from the data mining (out-of-sample). This
data is then used to evaluate the best rule discovered in the mined data
(in-sample). The selected rule’s performance on the data that was insulated from mining operations provides an unbiased estimate of its expected return in future data. A number of schemes for partitioning the
historical data into in-sample and out-of-sample segments have been proposed. I summarize several of them later.
A second approach, one that has not been widely discussed outside
the academic literature, is based on randomization methods like bootstrapping and Monte Carlo. This approach offers a number of advantages.
First, it allows the data miner to test as many rules as desired. Testing a
greater number of rules increases the chance of ﬁnding superior rules.
320 METHODOLOGICAL, PSYCHOLOGICAL, PHILOSOPHICAL, STATISTICAL FOUNDATIONS
--- page 319 ---

Second, it does not require holding data aside, as is done in out-of-sample
testing, thereby allowing all available historical data to be used for data
mining. Third, it permits signiﬁcance testing, and, sometimes, approximate conﬁdence intervals can be produced.
A third approach, the data-mining correction factor developed by
Markowitz and Xu, deﬂates the observed performance of the rule that did
the best. The reader is directed to source material for this approach. As a
point of interest, limited experiments conducted with this method suggest
it can work surprisingly well, but it can also fail miserably, depending on
the conditions.
Out-of-Sample Testing
Out-of-sample testing is based on the valid notion that the performance of
a data-mined rule,33 in out-of-sample data, provides an unbiased estimate
of the rule’s future performance. Of course, due to sampling variation, the
rule may perform differently in the future than it does in its out-of-sample
test, but there is no reason to presume it will do worse. Because out-ofsample performance is unbiased, it makes sense to reserve data for out-ofsample testing.
This raises the issue of how to best segment the historical data into insample and out-of-sample subsets. Various schemes have been proposed.
The simplest is to create two subsets; the early portion of the historical
data is used for data mining while the later portion is reserved for out-ofsample testing. See diagram A in Figure 6.56.34 A more sophisticated segmentation scheme breaks the historical data up in a checkerboard pattern
such that both in-sample and out-of-sample data come from all parts of
the history. See diagrams B and C in Figure 6.56.
Data-Mining Bias: The Fool’s Gold of Objective TA
321
Time
In-Sample
Out-of-Sample
In-Sample
Out-of-Sample
In-Sample
I-S
I-S
I-S
I-S
I-S
O-S
O-S
O-S
O-S
A.
B.
C.
FIGURE 6.56
In-sample and out-of-sample segmentation of historical data.
--- page 320 ---

Walk-Forward Testing.
Another data segmentation approach speciﬁc to ﬁnancial market trading applications is walk-forward testing. It is
described in Pardo,35 De La Maza,36 Katz and McCormick,37 and Kaufman.38
It employs a moving data window, which itself is divided into an in-sample
and out-of-sample segment. The terminology used for the in-sample and
out-of-sample segments is somewhat different, however. Because walkforward testing has a dynamic aspect, in which the rule is being modiﬁed
over time as the market evolves, the terminology alludes to a rule that is
learning from its experience. Thus the in-sample segment is referred to as
the training data set because the best parameter values for the rule are
learned in this portion of the data. The out-of-sample segment is referred
to as the testing data set, because the parameter values that were learned
in the training test are tested for performance in this data segment.
The notion of a moving data window is well known in time series
analysis and technical analysis. Moving averages, moving max-min price
channels, and rate-of-change indicators, to name a few, employ a data
window that slides along the time axis. Mathematical operations, such as
determining the maximum value or the average value, are conﬁned to the
data in the window.
In the context of rule testing, the data window (training set + testing
set) that is walked forward is sometimes referred to as a fold (see Figure
6.57). An out-of-sample performance estimate is computed for each fold.
Because there are typically numerous folds and hence numerous out-ofsample estimates, it becomes possible to determine the variance of the
performance statistic. This allows a conﬁdence interval to be computed.
Moreover, the moving data window adds a dynamic adaptive aspect to
rule testing. A new rule can be formulated in each new realization of the
data window. This makes walk-forward testing especially attractive for
nonstationary phenomena such as ﬁnancial markets. Hsu and Kuan found
adaptive trading rules (they referred to them as learning strategies) effective in their test of over 36,000 objective rules.39
In a walk-forward scheme, the training segment is used for data mining, and then the best rule found there is tested on the testing segment.
This yields an unbiased estimate of its out-of-sample performance. Then,
the entire window is moved forward and the process is repeated.
The walk-forward process is illustrated in Figure 6.57. Note, the window is moved forward by a sufﬁcient amount so that testing data segments in separate folds do not to overlap. In this way, the of out-of-sample
performance estimates are independent of each other.
Limitations of Data Out-of-Sample Testing Methods.
As an antidote to the data-mining bias, out-of-sample testing suffers from several
deﬁciencies. First and foremost, the virginal status of the data reserved
322 METHODOLOGICAL, PSYCHOLOGICAL, PHILOSOPHICAL, STATISTICAL FOUNDATIONS
--- page 321 ---

for out-of-sample testing has a short life span. It is lost as soon as it is used
one time. From that point forward, it is no longer able to provide unbiased
estimates of rule performance.
A second deﬁciency is that it eliminates certain portions of the data
from mining operations. Thus it reduces the amount of data available to
ﬁnd patterns. When noise is high and information is low, more observations are extremely valuable.
Third, the decision about how to apportion the data between the insample and out-of-sample subsets is arbitrary. There is no theory that
suggests what fraction of the data should be assigned to training and
testing. Results can be very sensitive to these choices. Often it’s a seatof-the-pants call.
Markowitz/Xu Data Mining Correction Factor
A formula for estimating the data-mining bias has been proposed by
Markowitz and Xu40 (MX) and described for practical implementation in
an Excel spreadsheet by De La Maza.41 Markowitz is well known for his pioneering work in modern portfolio theory, for which he shared the 1990
Nobel prize in economics.
The MX method does not require data segmentation. What is required, though, is the complete set of interval returns (e.g., daily, weekly,
monthly, and such) for all rules examined by the data miner en route to
selecting a best-performing rule. The method corrects for the data-mining
bias by shrinking the observed performance of the best rule back toward
the average performance of all rules tested. The degree of shrinkage is
determined by several factors including: (1) the degree of variation in
each rule’s daily returns around the grand mean daily return for all rules
Data-Mining Bias: The Fool’s Gold of Objective TA
323
Time
Time
Time
Time
Train
Test
Fold1
Fold2
Fold3
Fold4
Train
Train
Train
Test
Test
Test
FIGURE 6.57
Walk-forward data testing two data segments.
--- page 322 ---

tested, (2) the degree of variation in each rule’s mean return around the
mean return for all rules tested, (3) the number of rules examined, and
(4) the number of time intervals (e.g., days) of returns.
The article by De La Maza, which was referred to earlier, lays out the
details for constructing a spreadsheet that computes the value of a shrinkage factor, B, which is a number between zero and one. This value is then
plugged into the formula
H′ = R+ B(H – R)
Where
H′ is the expected return for the best-performing rule after adjustment for the data-mining bias.
R is the average return of all the tested rules.
H is the observed performance of the best rule.
B is the shrinkage factor.
The corrected or shrunken performance estimate for the best rule, H’,
will lie somewhere between its observed performance and the average for
all rules tested. When B equals zero, then the expected return for the best
rule is simply equal to the average return of all rules (R). As B approaches
a value of 1, the expected return of the best rule approaches its backtested return. This occurs in a case where no data-mining bias was detected and thus no need to shrink the observed return of the best rule.
The result given by MX is very approximate. Under some conditions,
the shrunken performance estimate can be quite good. However, under
other conditions easily encountered in practice, its results can be seriously in error. MX is best used as a rough guideline.
Randomization Methods
Chapter 5 introduced two randomization methods that can be used to test
the statistical signiﬁcance of a rule’s observed performance in a back test.
They were bootstrapping and Monte Carlo permutation. As pointed out in
Chapter 5, these signiﬁcance tests were only valid for a single rule back test,
that is, where there was no data mining used to discover the rule. However,
with modiﬁcations described in this section, these procedures can also be
used to test the statistical signiﬁcance of a rule discovered with data mining.
Both randomization methods allow the data miner to use all historical
data for rule discovery. This circumvents the arbitrary decisions required
with out-of-sample testing: how to partition the data into in-sample and
324 METHODOLOGICAL, PSYCHOLOGICAL, PHILOSOPHICAL, STATISTICAL FOUNDATIONS
--- page 323 ---

out-of-sample, how much to use for training versus testing, and so on.
However, the randomization methods require that certain information
about each rule tested during data mining be retained. Because the speciﬁc information that must be retained depends on whether Monte Carlo
or bootstrapping is used, the information requirements of each method
will be discussed separately.
A brief review is in order to explain how randomization methods can
be used for signiﬁcance testing. The sampling distribution of a test-statistic
is the foundation of statistical inference. It describes the degree of random variation in a statistic. This distribution is vital in judging the statistical signiﬁcance of a rule’s observed performance. Chapter 5 pointed out
that the sampling distribution can be derived by bootstrapping or the
Monte Carlo permutation.
Bootstrapping the Sampling Distribution: White’s Reality
Check.
White’s Reality Check (WRC) was invented and patented by
economist Halbert White, a professor at the University of California at San
Diego. It uses the bootstrap42 method to derive a sampling distribution
that is appropriate to test the statistical signiﬁcance of the best rule found
by data mining. The software can be acquired from Quantmetrics,43 a ﬁrm
owned by Dr. White.
Prior to WRC, bootstrapping could be used to generate the sampling
distribution to test the signiﬁcance of a single rule. White’s innovation, for
which he was granted a patent, allows the bootstrap to be applied to the
best rule found by data mining. Speciﬁcally, WRC permits the data miner
to develop the sampling distribution for the best of N-rules, where N is the
number of rules tested, under the assumption that all of the rules have expected returns of zero. In other words, WRC generates the sampling distribution to test the null hypothesis that all the rules examined during data
mining have expected returns of zero.
Let’s take a highly simpliﬁed example to explain the procedure WRC
uses. Suppose the data miner has back tested only two rules (N = 2) over
10 days. I will refer to the rules as R1 and R2. Over the 10-day period R1
earned a mean daily return of 1 percent, whereas R2 earned a mean daily
return of 2 percent. The data miner picks rule 2 as the best performer, but
then wonders, as one should, if the 2 percent was the result of data-mining
bias and if its true expected return is actually zero. To generate the sampling distribution that would be appropriate for this data-mining venture,
the following steps are taken:
1. The rules are tested over 10 trading days. Thus 10 slips of paper are
used to represent each date of trading. They are numbered from 1
through 10 and placed in a bucket for sampling.
Data-Mining Bias: The Fool’s Gold of Objective TA
325
--- page 324 ---

2. The slips of paper are then sampled with replacement 10 times. Each
time a date is withdrawn from the bucket, the date number is noted.
The number of samplings is 10 because that was the length of each
rule’s performance history. This is a requirement of the Bootstrap
Theorem. Suppose the following dates were selected: 5, 3, 5, 5, 7, 2,
5, 8, 1, 2.
3. Using the dates obtained in step 2, a pseudo-track record based on
the actual daily returns associated with these dates is created for R1.
This procedure is also carried out for R2. We now have a randomly
generated performance history of length 10 for each rule.
4. Recall that our goal is to generate the sampling distribution for the
best-performing rule in a universe of rules which have expected returns equal to zero. Because it is possible, in fact it is our hope, that
at least one of the rules tested has an expected return greater than
zero, the raw historical returns of R1 and R2 must be adjusted to have
mean returns of zero. To accomplish this, WRC determines the mean
daily return for each rule tested and subtracts this amount from each
individual daily return.44 In this example, R1’s mean daily return is 1
percent and R2’s is 2 percent. Thus 1 percent is deducted from each
of R1’s daily returns whereas 2 percent is deducted from each of R2’s
daily returns. This has the effect of shifting the distribution of daily
returns for each rule so that it is centered over zero. These adjusted
daily returns are now used.
5. The adjusted returns of R1 for days 5, 3, 5, 5, 7, 2, 5, 8, 1, 2 are averaged. The adjusted returns for R2 are also averaged.
6. The larger of these two mean values is held aside as the ﬁrst value
used to form the sampling distribution of the maximum mean return
of N rules. In this case N = 2.
7. Steps 2 through 6 are repeated many times (e.g., 500 or more times).
8. The sampling distribution of the statistic, maximum mean return
in a universe of N (2) rules whose expected returns are zero is
formed from these 500 values.
9. With the sampling distribution now in hand, the p-value can be
computed.
10. The p-value would simply be the fraction of the 500 values obtained
at step 7 that exceed the average return of the tested rule. (See Chapter 5 for the procedure.)
The example described above was intentionally highly simpliﬁed. In a
more realistic case the data miner would examine a much larger number
of rules over a much longer time period. But the procedure for generating
326 METHODOLOGICAL, PSYCHOLOGICAL, PHILOSOPHICAL, STATISTICAL FOUNDATIONS
