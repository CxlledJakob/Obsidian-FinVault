# Evidence-based Technical Analysis_ Applying the Scientific Method and Statistical Inference to Trading Signals.pdf — pages 267–286

--- page 267 ---

the ﬁrst rule tested does not stop the research. The rule is reﬁned or a new
rule is deﬁned, and it is tested and its performance is evaluated. The cycle
continues until a rule with good performance is produced. This process
may involve testing tens, hundreds, thousands, or even greater numbers
of rules.
Data-Mining Bias: The Fool’s Gold of Objective TA
269
Rule Idea
Program Rule
Back Test
Stop Research
Start Trading
Satisfactory ?
Observed Performance
YES
NO
Get
Job
Working
at
McDonalds
FIGURE 6.2
Single rule back testing.
Rule Idea
Program Rule
Back Test
Stop Research
Start Trading
Satisfactory ?
Observed Performance
YES
NO
Start
Data
Mining
Data Mining
Loop
FIGURE 6.3
Rule Data mining.
--- page 268 ---

Legitimate Uses of Observed Performance
For this discussion, the assumed performance statistic is the mean rate
of return over the back-test period. The observed performance statistic
can play a legitimate role both in single-rule back testing and in data
mining. However, the roles are different. In single-rule back testing, observed performance serves as an estimator of future performance. In
data mining, observed performance serves as a selection criterion. Problems arise for the data miner when observed performance is asked to
play both roles.
In single-rule back testing, the tested rule’s mean return can legitimately be used as an unbiased estimate of the rule’s expected return. In
other words, the tested rule’s most likely future return is its back tested
return. This is merely a restatement of a something covered in Chapter
4. There, we learned that a sample mean provides an unbiased estimate
of the mean of the parent population that gave birth to the sample. The
sample mean may err due to the random variation of sampling. It may
be greater than the population mean or less than it, but neither error is
more likely. This principle pertains to the case of a single-rule back test.
The rule’s mean return in a back test is an unbiased estimate of its expected return in the future. And although its historic mean return is indeed its most likely return in the future, its performance may prove to
be higher or lower, with neither being more likely. This is illustrated in
Figure 6.4.
In data mining, the back-test performance statistic plays a very different role than it does in single-rule back testing. In data mining, back-
270 METHODOLOGICAL, PSYCHOLOGICAL, PHILOSOPHICAL, STATISTICAL FOUNDATIONS
Time
$
Cumulative
Gains
 In-Sample
Future
Observed
Performance
Expected
Performance
+/-
Random Variation
Back-Test
FIGURE 6.4
Expected performance for single rule back test.
--- page 269 ---

tested performance serves as a selection criterion. That is to say, it is
used to identify the best rule. The mean returns of all back-tested rules
are compared and the one with the highest return is selected. This, too,
is a perfectly legitimate use of the back test (observed) performance
statistic.
It is legitimate in the sense that the rule with the highest back-tested
mean return is in fact the rule that is most likely to perform the best in the
future. This is certainly not guaranteed, but it is the most reasonable inference that can be made. A formal mathematical proof of this statement is
offered by White.25
The Data Miner’s Mistake: Misuse
of Observed Performance
Let’s recap two key points. In a single-rule back test, past performance
can be used as an unbiased estimate of future performance. In multiplerule back testing (i.e., data mining), past performance can be used as a selection criterion.
The data miner’s mistake is using the best rule’s back-tested performance to estimate its expected performance. This is not a legitimate use
of back-tested performance because the back-tested performance of the
best-performing rule is positively biased. That is, the level of performance
that allowed the rule to win the performance competition overstates its
true predictive power and its expected performance. This is the data-mining
bias. This concept is illustrated in Figure 6.5.
Data-Mining Bias: The Fool’s Gold of Objective TA
271
Time
$
Cumulative
Gains
 In-Sample
Future
Observed
False Expectation
Performance
Data
Mining
Bias
Best-Rule
Expected
Performance
of Best-Rule
FIGURE 6.5
Expected performance of best data-mined rule.
--- page 270 ---

The best rule’s performance does not truly deteriorate out of sample.
It only appears that way as the out-of-sample performance assumes a
level that reﬂects the rule’s true predictive power without the good luck
that allowed it to beat the other rules. Its in-sample performance was a
combination of some level of predictive power, possibly zero, and a big
component of good luck. The good luck that shined on the rule during
the back test is now shining elsewhere. In a like manner, the monkey did
not suffer a loss of literary skill on the night of the big show. His performance merely reﬂected his true literary ability minus the good luck that
allowed him to produce letters that happened to match a segment of
Shakespearian prose.
DATA MINING AND STATISTICAL INFERENCE
This section discusses the connection between data-mining bias and statistical inference. This section will cover the following points: (1) the distinction between biased and unbiased estimators, (2) the distinction
between random error and systematic error (i.e., bias), (3) the fact that
unbiased estimators are afﬂicted with random error but biased estimators
are afﬂicted with both random error and systematic error, (4) statistical
statements hold true for a large number of observations, such as a large
number of estimates, and (5) the data-mining bias is an effect that shows
up generally over many instances of data mining; thus we cannot say that
any particular data-mined result is biased.
Unbiased Error and Systematic Error
All scientiﬁc observations are subject to error. Error is deﬁned as the difference between an observed value and the true value:
Error = observed – true
A positive error is said to occur when the observed value is greater
than true value. Negative error is the reverse. If a scale indicates a person
weighs 140 lbs but they actually weight 150, the error is negative 10 lbs.
There are two distinct types of error: unbiased and biased (systematic). All observations are infected with some degree of unbiased error.
No measuring instrument or technique is perfect. This type of error has an
expected value of zero. This means that if a large number of observations
are made on some phenomenon, such as the return of a rule, and those
observations are afﬂicted only with unbiased error, the observed values
272 METHODOLOGICAL, PSYCHOLOGICAL, PHILOSOPHICAL, STATISTICAL FOUNDATIONS
--- page 271 ---

will be haphazardly distributed about the true value. If an average were to
be computed for all these errors the average would be approximately
zero. See Figure 6.6.
In contrast, observations afﬂicted with systematic error tend to lie on
one side of the truth. Such observations are said to be biased. When the
errors of many biased observations are averaged, the average error will be
distinctly nonzero. See Figure 6.7. In the illustration the observations are
positively biased and their average error (observed – true) is positive.
Suppose a chemist observes the weight of a residue left by a chemical
reaction on one hundred separate instances. Unbiased error might be attributable to random variations in laboratory humidity over the course of the
one hundred weighings. The amount of moisture in the residue affects its
weight. Systematic error, if present, could be due to an imperfection in the
scale, always causing the observed weight to be lower than the true weight.
Unbiased and Biased Statistics
Interpreting a large sample of observations is difﬁcult. As was discussed
in Chapter 4, a sensible ﬁrst step is data reduction. This reduces the large
Data-Mining Bias: The Fool’s Gold of Objective TA
273
Probability
Distribution
Of
Observed
Values
True
&
Most Likely
Observed
Value
FIGURE 6.6
Unbiased observations.
Probability
Distribution
Of
Observed
Values
Most
Likely
Observed
Value
True
Value
FIGURE 6.7
Observations with systematic error.
--- page 272 ---

set of measurements to a smaller set of summary statistics: sample mean,
sample variance, and other computed measures that describe the entire
set of observations.
Chapter 4 also pointed out that a sample statistic, such as the mean, is
subject to a particular type of random error called sampling error. This error is unbiased. Here, the term error refers to the deviation between a
sample mean and the mean of population from which the sample was
taken. Because the sample does not represent the population perfectly,
the mean of the sample will deviate to some degree from the mean of the
population.
Relating this back to objective TA, a rule back test produces a large
sample of observations—the rule’s daily, weekly, or monthly returns.
This sample is made more intelligible by reducing it to a performance
statistic (e.g., annualized average return, Sharpe ratio, and such). As is
true of any sample statistic, the performance statistic is subject to random error. However, the statistic may also be subject to systematic error or bias.
To state the obvious, a historical performance statistic cannot be put
in the bank or be used to buy a Ferrari. Its sole economic utility is the inference it allows us to make about future performance of the rule that
produced it. Objective technicians use back-tested performance to make
an inference about a rule’s expected performance in the form of a conﬁ-
dence interval or a hypothesis test. In either case, the accuracy of the inference will depend on the type of error: unbiased or systematic, and its
magnitude.
Biased statistics are afﬂicted with systematic error. As stated previously in a single-rule back test, the mean return is an unbiased statistic.
Therefore, inferences about the rule’s expected return based on back-test
performance will be subject only to a form of unbiased error called sampling variability.
This, however, is not the case for the best rule found via data mining.
The observed average return of the best-performing rule is a positively
biased statistic. As a result, inferences based on it will be systematically
in error. This means that when conducting a hypothesis test, one would
be prone to reject the null hypothesis more frequently than the signiﬁ-
cance level would suggest. For example, at a signiﬁcance level of 0.05
one expects to reject the null hypothesis in error only 5 times in 100.
However, if the observed performance is positively biased, then H0 will
be rejected more frequently than it should, perhaps far more frequently.
This will result in trading using rules that appear to have predictive
power but in fact do not. The question is: What causes the back-tested
return of the best rule, the rule picked by the data miner, to overstate its
true predictive power?
274 METHODOLOGICAL, PSYCHOLOGICAL, PHILOSOPHICAL, STATISTICAL FOUNDATIONS
--- page 273 ---

The Mean versus the Maximum
Single-rule back testers and data miners are looking at two entirely different statistics. The single-rule back tester is observing the mean of a single
sample. The data miner is observing the maximum mean among a multitude of sample means. It is easy to overlook the fact that these are two entirely different statistics.
To be clear, in the case of a single-rule back test there is one set of results—the rule’s daily returns generated over the back-test period. They
are summarized by a performance statistic (e.g., mean daily return). In
data mining, many rules are back tested, and so there are many sets of results and many performance statistics. If 50 rules have been back tested
the data miner has the opportunity to observe 50 mean returns prior to selecting the rule that produced the maximum mean return.
The set of 50 means returns can be considered as a set of observations, which, in turn, could be summarized with a statistic. For example
one could compute the mean of the means. That is the mean return of all
50 rules. Another statistic that could be computed for this set of observations would be the minimum mean—the mean return of the rule that did
the worst. Yet another statistic would be the maximum mean—the mean
return of the rule that did the best.
The statistic observed by the data miner is the maximum mean from
among the 50 rules. This is illustrated in Figure 6.8, where all rules are assumed to be useless and have an expected return equal to zero. Each dot
represents the observed mean return of a different rule. Note that the
mean return of the rule that had the maximum return (37 percent) is not
at all representative of that rule’s expected return (0 percent). It simply
got lucky in the back test. When many rules are back tested, the one with
Data-Mining Bias: The Fool’s Gold of Objective TA
275
0
Observed Rate of Return
+30%
-30%
Mean
Of
Fifty Means
Maximum Mean
Among
Fifty Means
+37%
FIGURE 6.8
Observed performance of 50 rule back tests.
--- page 274 ---

the highest average return will almost always have been the beneﬁciary of
good luck. This is why its back-tested performance is likely to overestimate its expected performance. In a different sample, with less luck, the
rule is likely to do worse.
This is the key lesson to take away from this: The observed performance of the best-performing rule, amongst a large set of rules, is a positively biased estimate of that best rule’s expected performance because it
incorporates a substantial degree of good luck. Data miners who don’t understand this are likely to be disappointed with this rule’s out-of-sample
performance.
Sound Inference Requires the Correct
Sampling Distribution
Sound statistical inference depends on using the correct sampling distribution. Each test statistic has a sampling distribution that is appropriate
for testing its statistical signiﬁcance. The sampling distribution that
would be correct for testing the signiﬁcance of a single sample mean or
constructing its conﬁdence interval would not be correct if the test statistic being observed were, in fact, a maximum mean among a multitude of
sample means.
Therefore, to make sound inferences, the data miner requires the
sampling distribution of the maximum mean among a multitude of means
because that is the statistic being considered when evaluating the best
rule found by data mining. The central tendency of the sampling distribution of the maximum mean reﬂects the role that good luck can play in data
mining. The central tendency of a sampling distribution of a single sample
mean does not.
Now let’s consider how all this impacts a test of signiﬁcance. As discussed in Chapter 5, in a traditional test of signiﬁcance, the null hypothesis asserts that the trading rule has an expected return equal to zero or
less. The test statistic is the rule’s observed mean return. In this case let’s
assume the return was +10 percent annualized. The sampling distribution
of the test statistic is centered at the hypothesized value of zero. The pvalue is the area of the sampling distribution that is equal to or greater
than a 10 percent return. This area represents the probability that, if the
rule’s expected return were truly equal to zero, the rule could have produced a return of +10 percent or higher by chance. If the p-value is smaller
than a preset value, such as 0.05, the null hypothesis would be rejected
and the alternative hypothesis, that the rule’s expected return is greater
than zero, would be accepted. So long as the performance of only one rule
was being evaluated this is all well and good.
Now consider signiﬁcance testing in the data mining case. Continuing
276 METHODOLOGICAL, PSYCHOLOGICAL, PHILOSOPHICAL, STATISTICAL FOUNDATIONS
--- page 275 ---

with the data mining example from the prior section, assume that 50
rules have been back tested. The rule with best performance earned annualized return of +37 percent. A traditional test of signiﬁcance, with a
signiﬁcance level of 0.05, would look like the one in Figure 6.9. The sampling distribution shown is centered at zero, reﬂecting the null’s assumption that the expected return of a rule with no predictive power would
generate a return of zero. This sampling distribution does not account for
the data-mining bias. Experimental results presented later in this chapter
will show that this assumption is wrong. They will demonstrate that even
when all rules tested during data mining have expected returns equal to
zero, the best performing rule is likely to display a much higher performance than zero.
Note in Figure 6.9 that the observed performance of +37 percent
falls far out in the right tail of the sampling distribution giving a p-value
of less than 0.05. On the basis of this evidence, the null hypothesis
would be rejected and the inference would be that the rule has an expected return greater than zero (i.e., has predictive power). This conclusion is wrong!
If, however, the observed performance of this best rule of 50 were
to be subjected to a more advanced test of statistical signiﬁcance that
does take into account the data-mining bias, the picture would look
considerably different. This is shown Figure 6.10, where the observed
mean return for best-rule-of-50 is compared to the correct sampling distribution. This is the sampling distribution of the statistic maximummean among 50 means. This sampling distribution properly reﬂects
the biasing effects of data mining. Note that the sampling distribution is
no longer centered at zero. Rather, it is centered at +33 percent. Against
Data-Mining Bias: The Fool’s Gold of Objective TA
277
70
60
50
40
30
20
10
Observed
 Performance
 Best Rule of
50
37%
-70 -60 -50 -40 -30 -20 -10 0
Relative
Freq.
f
Null
Hypothesis
Expected = 0%
p-value < 0.05
Sampling Distribution
Of A Single Sample
Mean
FIGURE 6.9
Traditional sampling distribution (does not account for data-mining
bias).
--- page 276 ---

this backdrop, the best rule’s performance no longer appears signiﬁ-
cant. The fraction of the sampling distribution that is equal to or greater
than the observed return of 37 percent is nearly half (0.45) of the distribution total area. In other words, if the expected return of each of the
50 rules were zero, then there is a 0.45 probability that the mean return
of the best rule would be greater than or equal to 37 percent due to
luck. From this, it is clear that 37 percent is not a statistically signiﬁcant
result. The particular sample of data in which the rule excelled just happened to favor the rule.
Figure 6.10 shows that randomness (good luck) can inﬂate the performance of a rule with no predictive power. It turns out that randomness is only one of two factors that jointly cause the data-mining bias.
The other cause is the selection principle that underlies all multiple
comparison procedures: picking the candidate with the best-observed
performance.
DATA-MINING BIAS: AN EFFECT WITH TWO CAUSES
The data-mining bias is the result of a conjoint effect: (1) randomness
and (2) the selection imperative of data mining or any multiple comparison procedure—picking the candidate with the best-observed performance. This section will examine how these two factors combine to
cause the observed performance of the best rule to overstate its expected
performance.
278 METHODOLOGICAL, PSYCHOLOGICAL, PHILOSOPHICAL, STATISTICAL FOUNDATIONS
70
60
50
40
30
20
10
Observed
 Performance
37%
-70 -60 -50 -40 -30 -20 -10 0
Relative
Freq.
f
Null
Hypothesis
Expected = 33%
p-value > 0.45
Sampling Distribution
Of Multi-Mean
Maximum
FIGURE 6.10
Correct sampling distribution (accounts for data-mining bias).
--- page 277 ---

Two Components of Observed Performance
The observed performance of a rule can be factored into two components.
One component of observed performance is attributable to the rule’s true
predictive power, if it has any. This is the component of performance due
to a recurring feature of market behavior that is exploited by the rule and
that should continue to manifest in the immediate practical future. This is
the rule’s expected performance.
The second component of observed performance is attributable to
randomness. Randomness can manifest as either good luck or bad luck.
Good luck boosts observed performance above expected performance
whereas bad luck pushes observed performance below expected. The
component of observed performance attributable to randomness cannot
be expected to repeat in the immediate practical future.
This discussion is summed up by the equation in Figure 6.11.
The Spectrum of Randomness
It is useful to think of a spectrum of randomness. This concept is depicted
in Figure 6.12.26 At one end of the spectrum, observed performance is
Data-Mining Bias: The Fool’s Gold of Objective TA
279
Observed
Performance =
Expected
Performance +/- Randomness
FIGURE 6.11
The two components of observed performance.
Mathematical
Proofs
Monkeys
as
Authors
Bible
Codes
TA  Rules
Lottery
Players
Physics Laws
Concert Level
Merit
Dominates
Luck
Dominates
Musician
FIGURE 6.12
Spectrum of randomness—relative contributions of merit versus
luck in observed outcomes.
--- page 278 ---

dominated by randomness. At this extreme, all performances are purely a
matter of luck. Here we ﬁnd literary works of monkeys dancing on word
processors and outcomes of lottery players. At the other end of the spectrum, observed performance is dominated by merit or systematic behavior. At this extreme, it is only merit that matters. Producing a valid proof
of a mathematical theorem resides here. Very nearby are the observed
performances of concert-level musicians. Also, in this neighborhood we
ﬁnd the the laws of physics whose highly accurate predictions are made
possible by the orderly behavior of certain aspects of nature.
Toward the middle of the randomness spectrum lie the most interesting data mining problems. The farther to the random end of the spectrum
one goes, the greater the risk of data-mining bias. Toward the right end of
the continuum, we ﬁnd a region that contains the TA rules. The complexity and randomness of ﬁnancial markets assure us that even the most potent rules will be weakly predictive. In this zone, the magnitude of the
data-mining bias will be large.
Now we come to an important principle. The larger the contribution
of randomness (luck) relative to merit in observed performance, the
larger will be the magnitude of the data-mining bias. The reason is this:
The greater the role of luck relative to merit, the greater the chance that
one of the many candidate rules will experience an extraordinarily lucky
performance. This is the candidate that will be selected by the data miner.
However, in situations where observed performance is strictly or primarily due to a candidate’s true merit, the data-mining bias will be nonexistent
or very small. In these cases, a candidate’s past performance will be a reliable predictor of future performance and the data miner will rarely ﬁll the
hopper with fool’s gold.
Because ﬁnancial markets are extremely difﬁcult to predict, most of a
rule’s observed performance will be due to randomness rather than its
predictive power. Thus the equation previously given in Figure 6.11 might
be better illustrated as it is in Figure 6.13. The large role of randomness
relative to merit (i.e., predictive power) makes it likely that TA rule data
mining will be infected with a large bias.
The range of problems to which multiple comparison procedures
might be applied can be visualized as lying along the spectrum of randomness. Toward the random end of the spectrum is a range associated with
280 METHODOLOGICAL, PSYCHOLOGICAL, PHILOSOPHICAL, STATISTICAL FOUNDATIONS
Observed
Performance
=
Predictive
Power
+/–
Randomness
FIGURE 6.13
Relative contributions of randomness and predictive power in observed performance.
--- page 279 ---

TA rule data mining. I used a range to represent rule data mining rather
than a single location to indicate that the level of randomness will vary
from one mining venture to the next. As will be demonstrated later in this
chapter, the level of randomness in any given data mining venture is determined by ﬁve independent factors.27 When these factors are taken into
consideration, it becomes possible to develop statistical signiﬁcance procedures that are better able to deal with the data-mining bias. In other
words, it becomes possible to compute the statistical signiﬁcance of or
conﬁdence interval for a rule that was discovered by data mining. These
procedures alleviate the key problem facing objective TA practitioners using data mining for knowledge discovery.
The Effectiveness of Multiple Comparison
Procedures under Differing Conditions
of Randomness
Multiple comparison procedures are applied to problems where a best solution is sought. A universe of candidate solutions is proposed. A ﬁgure of
merit quantiﬁes the observed performance of each candidate and the one
with the best-observed performance is selected.
Many people presume that MCP delivers on two promises: (1) The
candidate with the highest observed performance is most likely to perform the best in the future, and (2) the observed performance of the bestperforming candidate is a reliable estimate of its future performance. It
does deliver on the ﬁrst promise. However, in the domain of TA rule back
testing, it does not deliver on the second.
With regard to the ﬁrst promise, that the candidate with the highest
observed performance is also the one most likely to do best in the future,
this was proved to be true by White28 as the number of observations approaches inﬁnity. White showed that, as the sample size approaches inﬁnity, the probability that the candidate rule with the highest expected
return (i.e., the truly best rule) will make itself known by having the best
observed performance approaches 1.0. This tells us that the basic logic of
data mining is sound! The rule with the highest observed performance is
the rule that should be selected. The validity of this assumption will also
be demonstrated by mathematical experiments presented later in this
chapter: Experimental Investigation of the Data-Mining Bias. These results show that when a sufﬁcient number of observations are used to compute a rule’s performance statistic (e.g., its mean return), the rule with the
highest observed performance does have a higher expected return than a
rule picked at random from the universe of rules tested. Data mining
must, at the very least, pass this minimal test of efﬁcacy for it to be considered a worthwhile research method, and it does!
Data-Mining Bias: The Fool’s Gold of Objective TA
281
--- page 280 ---

With regard to the second promise, that the observed performance of
the selected candidate is a reliable estimate of its future performance, the
news is not good. Jensen and Cohen29 point out that, when MCP is applied
in situations where randomness plays a signiﬁcant role in observed performance, the observed performance of the best-performing candidate
overestimates its expected (future) performance. In other words, when
observed performance is signiﬁcantly determined by luck, it is gives a positively biased estimate. This is the case in TA rule data mining.
Observed performance is a reliable estimate of the best candidate’s
future performance in situations where randomness is nonexistent or so
low that it can never inﬂuence the choice of the wining candidate. Such is
the case in a music competition or a competition at doing mathematical
proofs, where it is merit, not luck, that carries the day.
The bottom line: the MCP selected candidate is the candidate most
likely to do best in the future so long as a large number of observations
are used to compute the performance statistic. Nevertheless, in problems
where randomness has a signiﬁcant impact, observed performance is
positively biased, and the selected candidate’s future performance will, in
all probability, be worse than the performance that allowed it to win the
competition.
MCP Efﬁcacy in Low Randomness Situations
First, consider the application of MCP to problems with low randomness.
At this end of the spectrum, a candidate’s observed performance is dominated by merit, and MCP is effective in identifying superior merit.
This problem is exempliﬁed by the task of hiring a new ﬁrst violinist
for a symphony orchestra.30 The universe of candidates consists of the set
of musicians applying for the job. Each is asked to perform a challenging
composition, without prior rehearsal, for a panel of judges. The judges’
evaluation is the ﬁgure of merit. This acid test of instrumental competence, known as sightreading, is effective because great performances do
not occur by luck. If luck is a factor, it is a minor one. For example, a great
musician may have an off day because of a marital spat or a ﬂat tire on the
way to the audition, but even these random inﬂuences will have only a
small effect on a truly meritorious musician.
In this situation, observed performance is an accurate indicator of
true merit and an excellent predictor of future performance. This is
depicted in Figure 6.14. Each candidate’s merit, which is equivalent to
his expected performance, is indicated by the arrow. Both musicians
are excellent, although one is slightly better. The distribution of possible performance surrounding each candidate’s merit is narrow, indicating the minor impact of randomness on observed performance. Note
282 METHODOLOGICAL, PSYCHOLOGICAL, PHILOSOPHICAL, STATISTICAL FOUNDATIONS
--- page 281 ---

that there is no overlap in the distributions so that even if the better
candidate has an unlucky performance (i.e., at the extreme low end of
the distribution) and the lesser candidate has an extremely lucky one,
the better candidate will still be selected. This is another way of saying
that randomness is unlikely to inﬂate the inferior competitor’s performance sufﬁciently such that it would be selected over the higher merit
candidate.
MCP Efﬁcacy in High Randomness
Now consider a situation at the opposite end of the randomness spectrum, TA rule data mining. Here, randomness has a major impact on observed performance, for even the most potent TA rules or models possess
relatively little predictive power. This is a consequence of the complex
and highly random nature of ﬁnancial markets. The probability distribution of observed performance of a rule with an expected return of zero is
illustrated in Figure 6.15. Although zero is the most likely return, far
higher or lower returns are possible due to good or bad luck. If the rule is
unlucky in the back test, observed performance will be negative. Even
more problematic for the objective technician is when good luck shines
on the worthless rule and it earns a positive rate of return. This may fool
the objective technician into believing that TA gold has been found. In
fact, the rule’s signals coincided favorably with the market’s ﬂuctuations
purely by accident.
Although an extremely positive or negative average return is unlikely
for an individual rule, it becomes increasingly likely as more rules are
back tested. Just as the greater the number of people playing the lottery
Data-Mining Bias: The Fool’s Gold of Objective TA
283
Performance
Poor
Excellent
Expected
Performance
Higher Merit
Candidate
Probability
Expected
Performance
Lesser
Candidate
FIGURE 6.14
Low randomness—small merit differential. True merit shines
through thin fog of randomness.
--- page 282 ---

increases the chance that there will be someone lucky enough to win
twice, the greater the number of rules back tested increases the chance
that a rule will have an extraordinarily lucky observed performance. This
is the rule that would be picked by the data miner. The bottom line: when
observed performance is primarily due to randomness, it is likely that the
best observed performance, among a large set of observed performances,
will be largely an effect of randomness.
To see how luck might impact a data miner, imagine that you are observing a data miner at work. Furthermore, imagine that you are in the
fortunate position of knowing what no data miner ever knows, the true
expected return of each rule that is back tested. Suppose the data miner
back tests twelve different rules, and you know that each of the rules has
an expected return of 0 percent. All the data miner knows are the observed returns produced by each rule’s back test. In Figure 6.16, each
rule’s observed performance is depicted by an arrow on the probability
distribution. Each distribution is centered at zero, reﬂecting the fact that
each rule has an expected rate of return of zero. Notice that one rule got
lucky, producing an observed return of +60 percent. This is the rule that
would be selected by the data miner. In this case, the data-mining bias was
a positive 60 percent.
If the data miner were to test an even greater number of rules, the
chance of an even more positive observed performance would be increased. As will be discussed, the number of rules tested during data mining is one of ﬁve factors that impact the size of the data-mining bias. In
Figure 6.17, 30 rules are tested, and one managed to produce an observed
performance of 100 percent. This is the rule that would be selected by the
data miner. You know it is highly probable that its future performance will
be disappointing.
284 METHODOLOGICAL, PSYCHOLOGICAL, PHILOSOPHICAL, STATISTICAL FOUNDATIONS
Annualized Return
Negative Returns
Positive Returns
0
Expected
Return = 0%
Good Luck
Bad Luck
Probability
Possible
But
Rare
Possible
But
Rare
FIGURE 6.15
Probability distribution of observed performance.
--- page 283 ---

Data-Mining Bias: The Fool’s Gold of Objective TA
285
0
0
0
0
0
0
0
0
0
0
0
0
60%
FIGURE 6.16
Twelve different rules (each has an expected return of 0 percent).
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
100%
FIGURE 6.17
Data mining more rules increases probability of more extreme luck.
--- page 284 ---

The Risk of Picking an Inferior Rule
The prior examples assumed that all rules were of equal merit (all had expected returns equal to zero). Naturally, the data miner hopes that there is
at least one superior rule amongst all those tested, and that the superior
rule’s observed performance will identify it as such. Unfortunately, this is
not always the case.
This is another negative consequence of high randomness. The superior
rule, the one with highest expected return, may not get picked, because an
inferior rule’s lucky performance wins the data mining competition. An intuitive sense of the likelihood of this unfortunate result is portrayed in Figure
6.18. It shows the distribution of observed performance for two rules with
nearly identical expected performances, but one is indeed superior. However, the considerable overlap of the distributions gives a sense there is a
substantial chance the rule of lesser merit will produce the highest observed performance, causing it to get picked.
However, when the difference in expected returns (merit) between
the truly best rule and the next best rule is large enough, the data miner
can be more conﬁdent that best-observed performance will reliably
point to the superior rule. This is illustrated in the Figure 6.19. In other
words, when the difference in merit between the best rule and its nearest competitor is large, merit will be more likely to shine through the
fog of randomness. This is the illumination that guides the data miner to
the gold.
Practically speaking, the data miner is never aware of the risk of picking an inferior rule. That would require knowledge of true merit (expected
return), which is a population parameter and hence never known. The
286 METHODOLOGICAL, PSYCHOLOGICAL, PHILOSOPHICAL, STATISTICAL FOUNDATIONS
Performance
Low
High
0
Probability
Expected Return
Higher Merit Candidate
Expected Return
Lesser Merit Candidate
FIGURE 6.18
High randomness and small merit difference.
--- page 285 ---

data miner never gets to see the full consequences of the data-mining bias
until, as the song says, the future is past.
Five Factors Determine the Magnitude
of the Data-Mining Bias
Let us recap brieﬂy what has been established thus far:
• The data-mining bias is deﬁned as the expected difference between
the observed performance of a rule that wins the data mining competition and its true expected performance.
• Observed performance refers to the level of performance achieved by
a rule in back testing. Expected performance refers to the rule’s theoretical performance in the future.
• The observed performance of the highest-performing rule found by
data mining is positively biased. Therefore, its expected performance
out of sample will be less than the in-sample observed performance
that allowed it to beat other rules tested.
• Observed performance is a combination of randomness and predictive power. The greater the relative contribution of randomness, the
larger will be the magnitude the data-mining bias.
The relationship between the data-mining bias and the relative contribution of randomness is illustrated in Figure 6.20. As explained in the next
section, the degree of randomness encountered in a given data mining
venture depends on ﬁve factors that characterize the venture.
Data-Mining Bias: The Fool’s Gold of Objective TA
287
Performance
+20%
Low
High
0
Probability
Expected
Return
Superior Rule
Bad
Luck
Great
Luck
Expected
Return
Inferior Rule
FIGURE 6.19
High randomness and large merit difference (superiority overcomes randomness).
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
