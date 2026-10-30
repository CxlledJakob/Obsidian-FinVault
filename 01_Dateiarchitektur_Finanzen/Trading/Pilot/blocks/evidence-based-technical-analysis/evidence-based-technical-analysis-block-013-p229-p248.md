# Evidence-based Technical Analysis_ Applying the Scientific Method and Statistical Inference to Trading Signals.pdf — pages 229–248

--- page 229 ---

that could occur due to sampling variability. Note that the sampling distribution is positioned so that the most likely value of the return is zero. This
merely reﬂects the value of the population parameter asserted by H0. Also
note that the observed (back tested) value of the rule’s average return falls
well within the range of random variation allowed by the sampling distribution. This is an unsurprising result. In other words, the deviation between the observed value of the test statistic and the hypothesized
(predicted) value could easily be due to sampling error. Hence the evidence is not strong enough to warrant a rejection of H0.
Figure 5.7 makes it clear that the width of the sampling distribution is
critical in deciding if the deviation between the observed return and the
hypothesized return is large enough to warrant a rejection of H0. We saw
in Chapter 4 that the width of a statistic’s sampling distribution is determined by two factors: (1) the amount of variation within the parent population which gave rise to the sample, and (2) the number of observations
comprising the sample. With respect to the ﬁrst factor, the greater the
variability of the data comprising the population, in this case daily rule returns, the larger the width of the sampling distribution. With respect to the
second factor, the larger the number of observations comprising the sample, the smaller the width of the sampling distribution.
In Figure 5.8 the sampling distribution is relatively narrow. The observed value of the sample statistic lies in the outer right tail of the sampling distribution. This would be considered an improbable or surprising
observation and one that would be incompatible with the hypothesized
value. Such evidence would warrant a rejection of H0.
230 METHODOLOGICAL, PSYCHOLOGICAL, PHILOSOPHICAL, STATISTICAL FOUNDATIONS
0
Positive Returns
Deviation
Negative Returns
Value of the Population  Parameter
Asserted by H0
Sampling Distribution
for
Mean Return
Sample Statistic
FIGURE 5.7
Unsurprising evidence lies well within the range of sampling variation; H0 not rejected.
--- page 230 ---

These diagrams convey an intuitive sense of how the size of the deviation between an observed value and a hypothesized value (the value predicted by the hypothesis) is used to falsify a hypothesis. To be rigorous,
this intuition must be quantiﬁed. This is done by translating the observed
value’s deviation into a probability— speciﬁcally the probability of observing a deviation that large under the condition that the hypothesized value
is true. A probability that is contingent on the existence of a speciﬁed
condition, in this case that the hypothesized value is true, is called a conditional probability. Said differently, a conditional probability is a probability that is conditional upon some other fact being true.
In a hypothesis test, this conditional probability is given the special
name p-value. Speciﬁcally, it is the probability that the observed value of
the test statistic could have occurred conditioned upon (given that) the
hypothesis being tested (H0) is true. The smaller the p-value, the greater is
our justiﬁcation for calling into question the truth of H0. If the p-value is
less than a threshold, which must be deﬁned before the test is carried out,
H0 is rejected and HA accepted. The p-value can also be interpreted as the
probability H0 will be erroneously rejected when H0 is in fact true. P-value
also has a graphical interpretation. It is equal to the fraction of the sampling distribution’s total area that lies at values equal to and greater than
the observed value of the test statistic.
Let’s consider how all of this pertains to the test of a rule. For example, if a rule’s return in a back test was +3.5 percent, we mark the value
+3.5 percent on the horizontal axis upon which the sampling distribution
sits. We then determine the fraction of the sampling distribution’s area
Hypothesis Tests and Confidence Intervals
231
0
Positive Returns
Deviation
Negative Returns
Value of the Population  Parameter
Asserted by H0
Sampling Distribution
for
Mean Return
Sample Statistic
FIGURE 5.8
Surprising (improbable) evidence at the outer edge of the range of
sampling variation; H0 rejected.
--- page 231 ---

occupying values equal to or greater than +3.5 percent. Suppose that this
area equals 0.10 of the sampling distribution’s total area. The value 0.10 is
the sample statistic’s p-value. This fact is equivalent to saying that if the
rule’s true return were zero, there is a 0.10 probability that its return in a
back test would attain a value as high as +3.5 percent or higher due to
sampling variability (chance). This is illustrated in Figure 5.9.
p-value, Statistical Signiﬁcance, and
Rejecting the Null Hypothesis
A second name for the p-value of the test statistic is the statistical significance of the test. The smaller the p-value, the more statistically signiﬁ-
cant the test result. A statistically signiﬁcant result is one for which the
p-value is low enough to warrant a rejection of H0.
The smaller the p-value of a test statistic, the more conﬁdent we can
be that a rejection of the null hypothesis is a correct decision. The p-value
can be looked upon as the degree to which the observed value of the test
statistic conforms to the null hypothesis (H0). Larger p-values mean
greater conformity, and smaller values mean less conformity. This is simply another way of saying that the more surprising (improbable) an observation is in relation to a given view of the world (the hypothesis), the
more likely it is that world view is false.
How small does the p-value need to be to justify a rejection of the
H0? This is problem speciﬁc and relates to the cost that would be incurred by an erroneous rejection. We will deal with the matter of errors
and their costs in a moment. However, there are some standards that
232 METHODOLOGICAL, PSYCHOLOGICAL, PHILOSOPHICAL, STATISTICAL FOUNDATIONS
0
Null Hypothesis
&
Sampling Distribution
Mean Return
Area = 0.10 of total sampling distribution
Area = 0.10 of total sampling distribution
Test Statistic: +3.5%
p-value = 0.10
FIGURE 5.9
P-Value: fractional area of sampling distribution greater than +3.5%,
conditional probability of +3.5% or more given that H0 is true.
--- page 232 ---

are commonly used. A p-value of 0.10 is often called possibly signiﬁ-
cant. A p-value of 0.05 or less is typically termed statistically signiﬁcant
and is usually considered to be the largest p-value that would give a scientist license to reject H0. When the p-value is 0.01 or less it is called
called very signiﬁcant and values of 0.001 or less are termed highly
signiﬁcant.
Test Conclusions and Errors
A hypothesis test leads to one of two possible conclusions: (1) reject H0,
or (2) accept H0. What is actually true also has two possibilities: (1) H0 is
true, that is, the expected return of the rule is zero or less); or (2) H0 is in
fact false, that is, the rule’s expected return is greater than zero because it
possesses some degree of predictive power. Given that the test has two
possible conclusions, and the truth has two possible states, there are four
possible outcomes. They can be illustrated by a table with four cells
shown in Figure 5.10.
The hypothesis test can err in two ways. A type I error is said to occur when a low p-value leads us to reject H0, but in reality H0 is true. This
would be the case when a rule is truly devoid of predictive power, but by
luck it generates a sufﬁciently proﬁtable back test that its p-value is low
enough to justify rejecting H0. This is a case of the rule researcher being
fooled by randomness. The second type of error, called a type II error,
occurs when a high p-value leads us to retain H0, when it is in fact false.
In other words, the back test fooled us into concluding the rule has no
predictive power, but it actually does and its expected return is greater
than zero.
Hypothesis Tests and Confidence Intervals
233
Truth
(The Reality Only Known to God)
Test
Result
&
Conclusion
H0 True
Rule Return < = 0
H0 False
Rule Return > 0
High
P-value
H0
Not
Rejected
Low
P-value
H0
Rejected
Correct Decision
TA Rule Useless
We Discard It
Type I Error
TA Rule Useless
We Use it
Earn Zero Return
& Take Risk
Type II Error
TA Rule Good
We Don’t Use It
Opportunity Loss
Correct Decision
TA Rule Good
We Use Rule &
Make Profits
FIGURE 5.10
Possible outcomes of a hypothesis test.
--- page 233 ---

At the time the hypothesis test is conducted, only God knows for certain if an error has occurred and of which type. Mere mortals relying on
statistical inference must accept the reality that the test’s conclusion may
be in error.
From the standpoint of an objective technician, the two types of errors have different consequences. A type I error, where H0 is mistakenly
rejected, leads to the use of a worthless rule. This exposes trading capital
to risk without the prospect of compensation. A type II error causes a useful rule to be ignored, resulting in lost trading opportunities. Of the two
kinds of error, type I is more serious. Lost trading capital is worse than
lost opportunities. When capital is exhausted one is out of the game,
whereas there will always be other trading opportunities.
The hypothesis test can also be right in two ways: a correct rejection
of H0, when the rule does have merit, and a correct acceptance of the H0,
when the TA rule is useless.
COMPUTER-INTENSIVE METHODS FOR GENERATING
THE SAMPLING DISTRIBUTION
As previously mentioned, hypothesis testing requires a method for estimating the shape of the sampling distribution of the test statistic. There
are two ways to do this: the traditional approach of mathematical statistics, and the more recently developed computer-intensive randomization
methods. This section discusses two computer-based methods: bootstrapping and the Monte Carlo permutation.
Both the traditional and computer-intensive approaches solve the
problem of estimating the degree of random variation in a test statistic
when there is only a single sample of data and, therefore, only a single
value of the test statistic. As previously stated, a single value of a statistic
cannot convey a sense of its variability.
Computer-intensive methods estimate the sampling distribution’s
shape by randomly resampling (reusing) the original sample of observation so as to produce new computergenerated samples. A test statistic is
then computed for each resample. This procedure can be repeated as
many times as desired, perhaps thousands of times, thus producing a large
set of values for the sample statistic. The sampling distribution is developed from this large set of computer-generated values. It might seem
strange that reusing the original sample of observations over and over
again would allow one to approximate the variability of a sample statistic,
yet it does! Not only does this work quite well in practice, the approach is
grounded in sound mathematical theory.
234 METHODOLOGICAL, PSYCHOLOGICAL, PHILOSOPHICAL, STATISTICAL FOUNDATIONS
--- page 234 ---

The two computer-intensive methods, the bootstrap and Monte
Carlo permutation, are similar in that they both rely on randomization.
That is, they randomly resample the original sample. However, the two
methods are different in several important respects. First, they test
slightly different versions of H0. Although, in both, H0 asserts that the
rule being tested has no predictive power, they do so in slightly different ways. The H0 tested by the bootstrap asserts that the population distribution of rule returns has an expected value of zero or less. In
contrast, the H0 tested by the Monte Carlo permutation method asserts
that the rule’s output values (+1 and –1) are randomly paired9 with future market price changes. In other words, it asserts that the rule’s output is uninformative noise that could have just as easily been generated
by a roulette wheel.
Because the bootstrap and the Monte Carlo methods test somewhat
different versions of the null hypothesis, they require different data. The
bootstrap utilizes a daily history of rule returns. The Monte Carlo uses a
daily history of the rule’s output values (i.e., a sequence of +1 and –1’s)
and a daily history of price changes for the market being traded.
The two methods also use different random sampling methods. The
bootstrap uses a randomization method called resampling with replacement, whereas the Monte Carlo randomly pairs rule output values with
market returns without replacement. This distinction will be clariﬁed in
the description of each method’s algorithm.
Because of these differences, the methods generate somewhat different sampling distributions. Therefore, it is possible that the conclusion to
reject or not to reject H0 may not always be the same. However, extensive
simulations conducted by Dr. Timothy Masters, developer of the Monte
Carlo permutation method, show that both methods generally do agree
when they are applied to detrended market data. For this reason, the hypothesis tests conducted in this book use detrended market data for both
the bootstrap and Monte Carlo methods.
The ﬁnal distinction of the Monte Carlo permutation method is that it
is in the public domain, whereas the bootstrap method that is suitable for
rule testing is a patented product that is available only from its developer,
Quantmetrics.10
The Bootstrap
The bootstrap method was ﬁrst described by Efron11 in 1979 and then re-
ﬁned in several later publications cited in Eric Noreen’s Computer Intensive Methods for Testing Hypotheses.12 The bootstrap derives a sampling
distribution of the test statistic by resampling with replacement from an
original sample.
Hypothesis Tests and Confidence Intervals
235
--- page 235 ---

The bootstrap is based on a truly amazing mathematical fact, the
bootstrap theorem. A mathematical theorem deduces a previously unrecognized truth from the established theorems and foundational assumptions (axioms) of a mathematical system. Assuming that certain
reasonable conditions are satisﬁed, the bootstrap theorem assures us that
it will converge to a correct sampling distribution as the sample size goes
to inﬁnity. From a practical standpoint, this means that given a single sample of observations bootstrapping can produce the sampling distribution
needed to test the signiﬁcance of a TA rule.
In its basic form, the bootstrap is not suitable for evaluating the statistical signiﬁcance of rules discovered by data mining. However, a modiﬁcation invented and patented by Dr. Halbert White, professor of economics
at the University of California, San Diego, extended the application of the
bootstrap to rules discovered by data mining. This modiﬁcation to the
bootstrap, which is incorporated in software called “Forecaster’s Reality
Check,” is discussed in Chapter 6 and utilized in Chapter 9 to evaluate the
statistical signiﬁcance of over 6,000 rules for trading the S&P 500.
Bootstrap Procedure: White’s Reality Check.
The description
that follows pertains to the use of bootstrapping in the context of testing
the statistical signiﬁcance test of a single TA rule. Thus, the following description does not address the issue of data mining. Figure 5.11 illustrates
236 METHODOLOGICAL, PSYCHOLOGICAL, PHILOSOPHICAL, STATISTICAL FOUNDATIONS
1,231 Observations
Resample 1
BS Mean = 0.8
Resample 5,000
BS Mean = -2.6
1,231 Observations
1,231 Observations
Resample 2
BS Mean = -1.8
1,231 Observations
Resample 3
BS Mean = 1.9
1,231 Observations
0.8
-1.8
1.9
 -2.6
5000
 Resampled Means
Sample Mean after
Adjustment = 0%
Mean of 5,000 Means
Bootstrapped Sampling Distribution
Of The Mean
0%
Returns from Tested Rule
1------
2------
3------
5000---
FIGURE 5.11
How bootstrapping produces the sampling distribution for the
sample mean return.
--- page 236 ---

the bootstrap procedure. The double arrows between each resample and
the original sample indicate that the sampling is being done with replacement (explained below).
There are several things worthy of note in Figure 5.11. First, the original sample, represented by the large oval, is comprised of the daily returns
earned by the rule on detrended data. As discussed in Chapter 1, the detrended market data has an average daily change of zero.
Second, before the resampling operation begins, the daily returns of
the rule are adjusted by a procedure called zero-centering, not to be confused with the detrending. The zero-centering adjustment makes the mean
daily return of the rule equal to zero. In other words, if the rule was able to
earn a nonzero return on detrended data, its returns must be zero centered. This serves the purpose of bringing the daily returns into conformity with the H0, which asserts that their average value is equal to zero.
This step is accomplished by ﬁrst computing the mean daily return of the
rule and then subtracting that mean value from each daily rule return.
Once the rule’s daily returns have been zero centered in this fashion we
are in a position to generate a sampling distribution that conforms to H0’s
assumption.
Third, the number of daily observations comprising each resample
must be exactly equal to the number of observations in the original sample.
The bootstrap theorem only holds true if the number of observations in
each resample is equal to the number of observations in the original sample. In the ﬁgure, the original sample is composed of 1,231 observations.
Thus, each bootstrapped resample is also comprised of 1,231 observations.
Fourth, each resample is produced by sampling with replacement.
This means that after a daily rule return has been selected at random from
the original sample and its value has been noted, it is then replaced back
into the original sample before another daily return is selected at random.
This makes it possible for an individual daily return to be selected more
than once or for it never to be selected at all for a given resample. It is this
element of randomness that enables the bootstrap procedure to model the
variability in the sample statistic.
Fifth, the diagram shows 5,000 resamples being taken. A mean is computed for each resample. These 5,000 means are used to construct the
sampling distribution of the mean.
The sequence of steps involved in bootstrapping the sampling distribution of the mean is:
1. Calculate the mean daily return for the rule over the observations in
the original sample (1,231 in Figure 5.11).
2. Zero centering: Subtract the mean daily return from each day’s return in the original sample.
Hypothesis Tests and Confidence Intervals
237
--- page 237 ---

3. Place the zero-centered data in a bucket.
4. Select a daily return at random from the bucket and note its value.
5. Place that return back in the bucket, and then thoroughly stir the
bucket (some statisticians prefer their samples shaken rather than
stirred).
6. Perform steps 4 and 5 exactly N – 1 more times (e.g., 1,230) creating
a total of N (1,231) randomly selected observations. This completes
the ﬁrst bootstrapped sample.
7. Compute the mean return for the N (1,231) observations in the ﬁrst
resample. This is one value of the bootstrapped mean.
8. Perform steps 6 through 9 a large number of times (5,000) yielding a
large number of bootstrapped means.
9. Form the sampling distribution of the means.
10. Compare the observed mean return of the rule to the sampling distribution and determine the fraction of the 5,000 means comprising the
sampling distribution that exceed the observed mean return of the
rule to determine the p-value. See Figure 5.12.
Monte Carlo Permutation Method [MCP]
Monte Carlo simulation, invented by Stanislaw Ulam (1909–1984), is a
general method for solving mathematical problems by random sampling.
The Monte Carlo permutation method for rule testing was developed by
Dr. Timothy Masters. He is the ﬁrst to propose this approach as a way to
238 METHODOLOGICAL, PSYCHOLOGICAL, PHILOSOPHICAL, STATISTICAL FOUNDATIONS
Average
Return
of
Tested
Rule
Null Hypothesis
0%
p-value = 0.04
0
FIGURE 5.12
Comparing the rule’s mean return to the bootstrapped sampling
distribution of the mean.
--- page 238 ---

produce the sampling distribution to test the statistical signiﬁcance of a
rule’s back-tested performance. It is presented as an alternative to White’s
reality check.
Although the Monte Carlo method has been in existence for a long
time, it had not been previously applied to rule testing. This was made
possible by Dr. Masters’ insight that the Monte Carlo method could generate the sampling distribution of a rule with no predictive power. This is accomplished by randomly pairing or permuting the detrended daily returns
of the market (e.g., S&P 500) with the ordered13 times series representing
the sequence of daily rule output values. Recall that the H0 tested by the
Monte Carlo permutation method asserts that the returns of the rule being
evaluated are a sample from a population of returns that were generated
by a rule with no predictive power. The daily returns of such a rule can be
simulated by randomly pairing the rule’s output values (+1 and –1) with
the market’s price changes. The random pairing of the rule output values
with market changes destroys any predictive power that the rule may
have had. I refer to this random pairing as a noise rule.
The process of randomly pairing market-price changes with rule output values is illustrated in Figure 5.13. The daily time series of rule output
values are simply those that were produced by the rule that is being evaluated in their original order. After the sequence of output values has been
randomly paired with what is effectively a scrambled version of the market’s history, the mean daily return of the noise rule can be computed.
This value appears in the grey box at the end of each row. To produce the
sampling distribution we need many such values.
Hypothesis Tests and Confidence Intervals
239
Randomized SP500
 Return1
Time Series of
Rule Output Values
Randomized Rule
Return1
-0.4
+1.2
-2.6
-0.8
+1.7
+3.1
Mean
Return2
-2.6
-0.9
+0.3
-0.8
+1
+1
+1
+1
-1
-1
-1
-1
-1
-1
+0.4
-1.2
+2.6
+0.8
-1.7
- 3.1
-2.6
-0.9
+0.3
-0.8
-0.34
-0.4 +1.2
-2.6
-0.8 +1.7 +3.1
-2.6
-0.9 +0.3
-0.8
-0.4 +1.2
-2.6
-0.8
-1.7
- 3.1 +2.6 +0.9 -0.3
+0.8
Randomized SP500
 Return2
Randomized Rule
Return2
Mean
Return1
-0.62
Randomized SP500
 Return3
Randomized Rule
Return3
-0.4
-2.6 +1.7
-0.9
+3.1
-0.8
-2.6
+0.3 +1.2
-0.8
-2.6 +1.7
-0.4
-0.9 +0.8 +0.8
-0.3
-1.2 +2.6
-3.1
Mean
Return3
-0.26
FIGURE 5.13
Monte Carlo permutation method.
--- page 239 ---

To produce additional values of noise rule mean returns, the same
time series of actual rule output values is paired with (permuted with) numerous scrambled (randomized) versions of market-price changes. The illustration shows only three Monte Carlo permutations but in practice it
would be done a large number of times, perhaps 5,000. The 5,000 values
for average return are then used to form the sampling distribution of the
mean return earned by a noise rule—a rule with no predictive power.
Procedure.
The sequence of steps to generate the sampling distribution by the Monte Carlo permutation method is as follows:
1. Obtain a sample of one-day market-price changes for the period of
time over which the TA rule was tested, detrended as described in
Chapter 1.
2. Obtain the time series of daily rule output values over the back-test
period. Assume for this illustration that there were 1,231 such values, one rule output value for each day on which the rule was tested.
3. Place the market’s detrended one-day-forward price changes on a
piece of paper. Place them in a bin and stir.
4. Randomly select a market-price change from the bin and pair it with
the ﬁrst (earliest) rule output value. Do not put the price change
back in the bin. In other words this sampling is being done without
replacement.
5. Repeat step 4 until all the returns in the bin have been paired with a
rule output value. In this example there will be a total of 1,231 such
pairings.
6. Compute the return for each of the 1,231 random pairings. This is
done by multiplying the rule’s output value (+1 for long, –1 for short)
by the market’s one-day-forward price change.
7. Compute the average return for the 1,231 returns obtained in step 6.
8. Repeat steps 4 through 7 a large number of times (e.g., 5,000).
9. Form the sampling distribution of the 5,000 values obtained in step 8.
10. Place the tested rule’s rate of return on the sampling distribution and
compute the p-value (the fraction of random rule returns equal to or
greater than the tested rule’s return).
Application of Computer Intensive Methods
to Back-Test of a Single Rule
This section demonstrates the application of the two computer-intensive
hypothesis testing methods to a single rule: 91 day channel breakout14 us-
240 METHODOLOGICAL, PSYCHOLOGICAL, PHILOSOPHICAL, STATISTICAL FOUNDATIONS
--- page 240 ---

ing the Dow Jones Transportation Index (input series 4) as the rule’s input
series. This rule, which is designated as TT-4-91, and all others tested in
Part Two of this book are described in detail in Chapter 8. The main point
for current purposes is to demonstrate the hypothesis test. The rule was
used to generate long and short signals on the S&P 500 index from November 1980 through June 2005. Over this period of time, the rule earned
an annualized return of 4.84 percent using detrended S&P 500 data to
compute the rule’s daily returns. The expected annual return of a rule with
no predictive power is zero on detrended data.
Both the bootstrap and the Monte Carlo permutation methods were
used to test the null hypothesis that the rule has no predictive power. The
question is this: Is TT-4-91’s +4.84 percent return sufﬁcient to reject the
null hypothesis?
Testing Rule Performance Using Bootstrap: White’s Reality
Check.
To generate the sampling distribution of the average return, the
speciﬁc steps taken starting with the detrended S&P 500 data are:
1. Zero Centering the Daily Rule Returns: Because the rule generates a
positive return (+4.84 percent) on the detrended market data, the average daily return of the rule (approximately 0.0192 percent per day)
is subtracted from the return earned by the rule each day. This transformation creates a set of daily returns whose average value is zero,
thereby making the data conform to H0. Note—this is not to be confused with the detrending of the S&P 500 data.
2. Resampling the Daily Returns: The zero-centered daily returns as
computed in the preceding step are sampled with replacement. This
must be done exactly 6,800 times (the number of observations in the
original sample) for the Bootstrap Theorem to hold true.
3. Compute the Mean Return: The mean daily return is computed for the
6,800 resampled returns. This is the ﬁrst bootstrapped mean.
4. Repeat steps 2 and 3 5,000 times. This obtains 5,000 values for the resampled mean.
5. Create the bootstrapped distribution of resampled means.
6. Compare rule’s +4.84 percent return to the sampling distribution to
determine the fraction of the sampling distribution’s area that lies at
values equal to or greater than +4.84 percent per annum. This is done
by counting the fraction of the 5,000 bootstrapped means that have
values equal to or greater than this return.
Results: H0 Rejected—Rule Possibly Has Predictive Power.
Figure 5.14 shows the bootstrapped sampling distribution with the actual
Hypothesis Tests and Confidence Intervals
241
--- page 241 ---

performance of rule TT-4-91 superimposed. The p-value of 0.0692 indicates that .069 of the 5,000 bootstrapped means were equal to or greater
than +4.84 percent. This means that if the rule’s expected return were
truly equal to zero, about 7 times out of 100, the rule would earn a return
of +4.84 percent or greater simply due to chance (sampling variability).
Statisticians would regard such a result as possibly signiﬁcant. As will be
seen in Chapter 6, the amount of searching that led to the discovery of the
rule, speciﬁcally whether the rule was found amongst a large group of
back-tested rules, can impact the p-value and the rule’s signiﬁcance. Consequently, the results quoted here assume that this was the only rule proposed for back testing.
Testing Rule Performance with Monte Carlo Permutation
Method.
The following steps describe the process of applying the
Monte Carlo Permutation Method to a rule’s back-tested performance:
1. The time series of daily rule output values is laid out in its proper sequence over the time period of the rule back test. As stated earlier
there will be 6,800 of these daily +1 and –1 values.
2. Each of the 6,800 detrended one day forward price changes is inscribed on a ball. These 6,800 balls are placed in a bin.
242 METHODOLOGICAL, PSYCHOLOGICAL, PHILOSOPHICAL, STATISTICAL FOUNDATIONS
0.02
0.04
0.06
0.08
0.10
0.12
-0.15
-0.10
-0.05
0
0.05
0.10
0.15
TT- 4-91
+4.84%
p-value
0.069
FIGURE 5.14
Bootstrapped sampling  distribution for rule TT-4-91 and its p-value.
--- page 242 ---

3. The bin is shaken, and then, one at a time, the balls are drawn at random and paired with an individual rule output value. Thus, each of the
rule’s daily output values is matched with a single one day forward
S&P 500 return. This is done without replacement until all balls have
been paired with a rule output value. Because there are exactly 6,800
daily market returns and 6,800 rule output values, the bin will be
empty when this step is complete.
4. Multiply each rule value (+1 or –1) by the associated S&P 500 return.
This gives the return that would be earned by the noise rule over the
next day. This step will produce 6,800 daily rule returns.
5. Average the 6,800 values obtained in step 4. This is the ﬁrst Monte
Carlo permuted mean return for a noise rule.
6. Steps 3 through 5 must be repeated 5,000 times.
7. Produce the sampling distribution from the 5,000 Monte Carlo means.
8. Compare the return of the TT-4-91 rule with the sampling distribution
and determine the fraction of Monte Carlo means that equal or exceed
the return earned by the rule. This is the p-value.
Monte Carlo Results: Rule Possibly Has Predictive Power.
Conﬁrming the bootstrapped result, the Monte Carlo method gives a p-value
that is almost identical.
ESTIMATION
Estimation is the other form of statistical inference. In contrast to hypothesis testing, which is oriented to the acceptance or rejection of a claim
made about the value of a population parameter, estimation’s purpose is
to approximate the value of the population parameter. In our case, it will
be used to estimate the expected return of a rule.
Point Estimates
There are two kinds of estimates: point and interval. A point estimate is a
single value that approximates the population parameter, for example the
rule has an expected return of 10 percent. An interval estimate is a range
of values within which the population parameter lies with a given level of
probability. The following statement would exemplify this: The rule’s expected return lies within the range 5 percent to 15 percent with a probability of 0.95.
Actually, we already have been making point estimates, but they have
Hypothesis Tests and Confidence Intervals
243
--- page 243 ---

not been described as such. Every time we compute a sample mean and
use it to approximate the population mean, we are making a point estimate. This fact is easily overlooked. Some commonly used point estimators are: the mean, median, standard deviation, and the variance. The
estimate is computed from a sample of observations taken from the population. In other words, a point estimate is a sample statistic. The formula
to compute a sample mean is shown in Figure 5.15.
The use of means (averages) is so ubiquitous in TA that it is taken for
granted, yet the sample mean turns out to be an elegant and powerful estimator. It provides a single value that is, in an important sense, the best
(most informative) estimate of the population’s mean. This is an important fact.
Just how informative the sample mean is becomes clear when we
consider the criteria used to judge the quality of an estimator. Good estimators should be: unbiased, consistent, efﬁcient, and sufﬁcient. In terms
of these four criteria, it can be shown that the sample mean is the best estimator of the population mean.15
An estimator is unbiased if its expected value is equal to the population value. Said differently, if an estimator is unbiased its deviations from
the true population value have an average value of zero. The sample
mean’s deviations from the population mean are unbiased. This allows us
to say that a rule’s mean return in a historical sample is an unbiased estimate of its mean return in the immediate practical future.
Another criterion of a point estimator’s goodness is its consistency.
An estimator is said to be consistent if its value converges to the value of
244 METHODOLOGICAL, PSYCHOLOGICAL, PHILOSOPHICAL, STATISTICAL FOUNDATIONS
x1
x2
x3
x =
+
+
+ .  .  .xn
x = Σ
i = 1
 xi
n
n
 Where Xi is an individual observation on variable X
n
Sample Mean of Variable X
FIGURE 5.15
Sample mean of variable X.
--- page 244 ---

the population parameter as sample size is increased. The Law of Large
Numbers tells us that this is so for the sample mean.
Estimators should also be efﬁcient. This criterion relates to the width
of its sampling distribution. As mentioned earlier, an estimator is a sample
statistic, and thus has a sampling distribution. The most efﬁcient estimator is the one that produces the narrowest sampling distribution. In other
words, the most efﬁcient estimator has the smallest standard error.16 Both
the sample mean and the sample median are unbiased and consistent estimators of the population mean for populations that are distributed symmetrically. However, the sample mean is more efﬁcient than the sample
median. For large samples, the standard error of the mean is about 80 percent smaller than the sample median’s standard error.17
The ﬁnal trait of a good point estimator is called its sufﬁciency. “An
estimator is sufﬁcient if it makes such use of all the available sample data
that no other estimator would add any information about the parameter
being estimated.”18 The sample mean is sufﬁcient in this sense.
Interval Estimates—The Conﬁdence Interval
More informative than the point estimate is the interval estimate, also
known as a conﬁdence interval. It is described in this section.
What Do Conﬁdence Intervals Tell Us?
A point estimate has limited value because it conveys no sense of the uncertainty in the estimate
due to sampling error. The conﬁdence interval solves this problem by
combining the information of the point estimate with the information
about the estimator’s sampling distribution.
A conﬁdence interval is a range of values that surround the point estimate. The interval is deﬁned by upper and lower values called bounds. In
addition, the interval is accompanied by a probability number that tells us
how likely it is that the true value of the population parameter falls within
the bounds of the conﬁdence interval. By convention the probability is
stated as a percentage rather than a fraction. Thus, a 90 percent conﬁ-
dence interval for the mean has a 0.90 probability of enclosing within its
bounds the population’s true mean value.
When thinking about what a conﬁdence interval tells us, it is best to
think of what would happen if one were to construct a large number of 90
percent conﬁdence intervals, each based on an independent sample of
data taken from the population. If this were to be done, about 90 percent
of the intervals would actually encompass the value of the population’s
parameter. By extension, about 10 percent of the conﬁdence intervals
would fail to include the population parameter. This is illustrated in Figure 5.16 for 10 conﬁdence intervals. Ten is a small number, which I used to
Hypothesis Tests and Confidence Intervals
245
--- page 245 ---

keep the ﬁgure simple. The true, but unknown, population mean is indicated by the Greek letter μ (mu). The sample mean is identiﬁed by the dot
within each conﬁdence interval. Note that one of the conﬁdence intervals
fails to enclose the population mean.
The researcher can choose whatever conﬁdence level is desired. For
example a 99 percent conﬁdence level contains the true population mean
with a probability of 0.99. Of course, there is a price to be paid for the
higher level of conﬁdence—the interval is wider. In other words, the price
for higher conﬁdence is reduced precision. Note in Figure 5.17, by increasing the conﬁdence level to 99 percent, the error made by the 90 percent
246 METHODOLOGICAL, PSYCHOLOGICAL, PHILOSOPHICAL, STATISTICAL FOUNDATIONS
Means
&
90% Confidence
 Intervals
For
10 Independent
Samples
Error
 90% CI
Fails To
Enclose
Population
Mean
True Population Mean
μ
FIGURE 5.16
90 percent conﬁdence intervals (.90 probability correct).
Means
&
99%
 Confidence
 Intervals
For 10
Independent
Samples
99% CI
Correct
Where
90% CI
Was
Wrong
True Population Mean
μ
FIGURE 5.17
99 percent conﬁdence intervals (.99 probability correct).
--- page 246 ---

conﬁdence interval in Figure 5.16 has been eliminated. The reduced error
rate was accomplished by using a wider (less precise) conﬁdence interval.
If a rule were to be back tested on one hundred independent samples
of data and a 90 percent conﬁdence interval were constructed about the
mean return observed in each sample, approximately 90 percent of these
conﬁdence intervals would contain the rule’s true or expected return in
the population. Figure 5.18 shows a 90 percent conﬁdence interval for a
rule that earned a 7 percent return in a back test. We can be certain, with a
probability of 0.90, that the rule has an expected return between 2 percent
and 12 percent.
The Conﬁdence Interval and Its Connection to the Sampling
Distribution.
Conﬁdence intervals are derived from the same sampling distribution that is used to compute the p-values for a hypothesis
test. Given what we have already learned about sampling error (sampling
variability), it can be said that the value of a sample mean is equal to the
unknown value of the population mean, plus or minus its sampling error.
This relationship is shown by the upper formula in Figure 5.19. By rearranging the terms of this formula we get the lower formula in Figure 5.19.
It says that the value of the population mean is equal to the known value
of the sample mean plus or minus sampling error.
The bottom formula tells us that, although we do not know the precise value of the population mean, we can take the value of the sample
mean, which we do know, and the sampling distribution of the mean,
which we also know, and obtain a range of values that contains the population mean with a speciﬁed level of probability. In operational terms,
this tells us that if we were to repeat the following procedure 1,000
times—compute a sample mean and a 90 percent conﬁdence interval—
Hypothesis Tests and Confidence Intervals
247
7%
Rule Return
Was 7% In
Historical Sample
2%
12%
Rate of Return
90%
Confidence
 Interval
FIGURE 5.18
90 percent conﬁdence interval for rule back test.
--- page 247 ---

the population mean would lie within approximately 900 of the 1,000 con-
ﬁdence intervals. This concept is illustrated when the procedure is repeated only 10 times in Figure 5.20. Note that one of the 10 conﬁdence
intervals fails to include the population mean. The point of this section is
that the conﬁdence interval’s width is derived from the width of the sampling distribution.
As was said earlier, the conﬁdence interval is based on the same sampling distribution that is used in the hypothesis test. However, in the case
of the conﬁdence interval, the sampling distribution is simply shifted from
the position it occupies in a hypothesis test. In the hypothesis test, the
sampling distribution is centered at the hypothesized value of the population mean, for example, zero. In the case of a conﬁdence interval, the sampling distribution is centered over the sample mean, for example, 7
percent. This concept is illustrated in Figure 5.21.
Generating Conﬁdence Intervals with the Bootstrap.
Bootstrapping can be used to derive conﬁdence intervals. The procedure is almost identical to the one used to generate the sampling distribution for a
hypothesis test.
There are numerous methods for computing bootstrap conﬁdence intervals. The one presented here, the bootstrap percentile method, is popular, easy to use, and generally gives good results. More sophisticated
methods are beyond the scope of this text.
It should be pointed out that the Monte Carlo permutation method
cannot be used to generate conﬁdence intervals. This is because the
248 METHODOLOGICAL, PSYCHOLOGICAL, PHILOSOPHICAL, STATISTICAL FOUNDATIONS
x
+/-
Sampling Error
The known sample mean is
the unknown population mean with error
The unknown population mean is
the known sample mean with error
+/-
Sampling Error
x = μ
μ =
FIGURE 5.19
The known sample mean is the unknown population mean with
error.
--- page 248 ---

Hypothesis Tests and Confidence Intervals
249
Means
&
90% Confidence
 Intervals
for
10 Independent
Samples
Sampling
Distribution
of the Mean
Confidence Intervals
Derived from
Sampling Distribution
μ
u
90%
Area
FIGURE 5.20
The connection between the conﬁdence interval and the sampling
distribution.
Sampling Distribution
Positioned for
Confidence Interval
Sampling Distribution
Positioned for
Hypothesis Test
Mean Return
in
Historical Sample
Hypothesized
Value
Population
Parameter
7%
0%
FIGURE 5.21
The sampling distribution positioned for a hypothesis test and
positioned for a conﬁdence interval.
