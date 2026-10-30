# Evidence-based Technical Analysis_ Applying the Scientific Method and Statistical Inference to Trading Signals.pdf — pages 191–210

--- page 191 ---

Statistical Measures of Variability (Dispersion)
Measures of variability describe the degree to which the observations in a
sample are dispersed about their central tendency. In other words, measures of variability quantify the width of a frequency distribution.
Among the widely used measures of dispersion are the variance, the
mean absolute deviation, and the standard deviation. They are important
in the traditional approach to statistics (i.e., classical statistics). The standard deviation is the square root of the average squared deviation of each
observation from the mean of the data. The formula for the standard deviation of a sample is shown in Figure 4.15.
An intuitive notion of dispersion is best conveyed with pictures. Figure 4.16 shows a number of idealized frequency distributions with differing degrees of variation and different central tendencies. They are
idealized in the sense that the stair-step look that characterizes real frequency distributions has been smoothed away. The key point of Figure
4.16 is that central tendency and variation (dispersion) are independent
characteristics of a frequency distribution. In row 1 of Figure 4.16, the
four distributions have the same degree of variation but different central
values. In row 2 the distributions have the same central value but different
degrees of variation. In row 3 all distributions have different central values and different degrees of variation.
192 METHODOLOGICAL, PSYCHOLOGICAL, PHILOSOPHICAL, STATISTICAL FOUNDATIONS
Σ
Xi
(         ) 2
 –
Where:
X
n
n
i
X
Is an individual observation on variable X
Is the sample mean on variable X
Is number of observations in the sample
s  =
X
Standard Deviation of a Sample of Observations
FIGURE 4.15
Standard deviation of a sample of observations.
--- page 192 ---

PROBABILITY
The notion of probability is important in statistics because it is used to
quantify uncertainty. A conclusion reached via statistical inference is uncertain; that is, there is a chance of error. Thus, an inference about the
value of a population parameter has some chance of being wrong. This
chance is given in terms of a probability.
We routinely use informal notions of probability to form expectations
and make choices. Is the person I ﬁnd so wonderful now, likely to remain
so after marriage? What is the chance I will ﬁnd gold if I dig in a certain
spot? Is it probable I will feel fulﬁlled pursing a career in law? Should I
buy that stock, and if I do, how much proﬁt am I likely to make?
The informal usage of probability is connected to a cluster of interchangeable terms illustrated in Figure 4.17.
For our purposes, something more deﬁnitive is required. The deﬁnition of probability that makes the most sense for the work that lies ahead
is based on the notion of relative frequency. The relative frequency of an
event is the number of times the event actually occurred divided by the total number of opportunities on which the event could have occurred. Relative frequency is given as a fraction between 0 and 1. It could rain every
Statistical Analysis
193
1
2
3
Same Degree of Dispersion but Different Means
Equal Means but Different Degrees of Dispersion
Different Means and Different Degrees of Dispersion
0
5
10
15
FIGURE 4.16
Central tendency and dispersion are distinct attributes of
a distribution.
--- page 193 ---

day, but in the month of April the relative frequency of rain has actually
been 0.366 (11 out of 30 days). If rain never occurred, then its relative frequency would be 0. If rain occurred every day, its relative frequency is 1.0.
Thus, the relative frequency of an outcome is equal to:
In the box-of-beads experiment the value of f-g was measured 50
times. This was the maximum number of opportunities for any speciﬁc f-g
value to occur. In fact, the value f-g = 0.65 occurred on 5 out of 50. Therefore, it had a relative frequency of 5/50 or 0.10.
Probability is the relative frequency of an event over the long run—
the very long run. That is to say, the probability of an event is its relative
frequency of occurrence given an inﬁnite number of opportunities for its
occurrence. Probability is stated as a number that lies in the range of 0 to
1 inclusive. A probability value of 0 means the event never occurs,
whereas a value of 1.0 means it always occurs.
Probability is a theoretical notion because it is never possible to observe an inﬁnite number of anything. For practical purposes, however,
when the number of observations becomes very large, relative frequency
approaches theoretical probability.
The Law of Large Numbers
The tendency of relative frequencies to converge to theoretical probabilities, as the number of observations becomes large, is called the Law of
Large Numbers.20 The operation of the Law of Large Numbers can be illustrated with coin tossing. The possible outcomes (events) are heads or tails
and the probability of heads is known to be 0.50. The Law tells us that the
Number of occurrences of an event
Number of possible opportunities for the event to occur
194 METHODOLOGICAL, PSYCHOLOGICAL, PHILOSOPHICAL, STATISTICAL FOUNDATIONS
Probability
Random
Likelihood
Luck
Risk
Uncertainty
Chance
FIGURE 4.17
Common notions of probability.
--- page 194 ---

relative frequency of heads will converge to its theoretical value, 0.5, as
the number of coin tosses becomes large. However, even for a large number of tosses, a departure from 0.50 can still occur, though the likely size
of the departures decreases as the number of tosses increases. For small
samples, however, The Law of Large Numbers warns us that the relative
frequency of heads can differ substantially from 0.50. When the number of
tosses is only three, a value of 1.0 can easily occur—three heads in three
tosses.
Figure 4.18 shows the fraction of heads in a coin-toss experiment as
the number of tosses grows from one to one thousand. When the number
of tosses (observations) is less than 10, the fraction of heads experienced
two large deviations from 0.50. At 3 tosses the fraction of heads reached
0.66 (2 out of 3). At 8, the fraction was 0.375 (3 out of 8). However, as the
number of tosses increased the random variable, fraction heads, experienced progressively smaller deviations from the expected value of 0.50.
This is exactly what the Law of Large Numbers predicts.
Now imagine a naive coin ﬂipper. Upon observing ﬁve heads in ﬁve
tosses, he loudly proclaims, “I’ve found the holy grail of coins. It always
comes up heads.” The Law of Large Numbers says that the poor fellow’s
optimism is unwarranted. This is also likely to be true for the TA researcher who ﬁnds a rule with ﬁve historical signals, all of which were
correct. Optimism is most likely unwarranted. Chapter 6 will show that if
this rule was selected because it was the best performing rule out of a
large universe of back-tested rules, that is to say, it was discovered by data
mining, there would be even less reason to be optimistic about its future
performance.
Statistical Analysis
195
Number of Coin Flips (log scale)
0
1
10
100
1,000
0.20
0.40
0.60
0.80
1.0
F
R
A
C
T
I
O
N
H
E
A
D
S
0.50
FIGURE 4.18
Law of Large Numbers.
--- page 195 ---

Theoretical versus Empirical Probability
There are two kinds of probabilities: theoretical and empirical. “Theoretical probabilities can be determined with a good degree of conﬁ-
dence purely on logical grounds. They are derived independent of prior
experience, most often based on arguments of symmetry.”21 In other
words, they can be deduced without any reference to the world of experience. The probability of a head in a coin toss is a theoretical probability. There is no need to toss it ten thousand times to predict that over
the long run the probability of heads is 0.50. Simply the fact that the
coin is fair, that it has two faces, and that it is unlikely to land on its
edge is sufﬁcient grounds for suspecting heads and tails are equally
likely. The probabilities for being dealt a royal ﬂush in poker, the occurrence of a six in a dice roll, and the chance of winning Lotto are also
theoretical because each can be determined by a logical analysis of the
situation.
Empirical probabilities are based on observed frequencies. Technical analysis is concerned with this type of probability. The chance of
new snowfall on Mount Hood during the month of July or the likelihood
of a rise in the stock market following a 2 percent drop in interest rates
are examples of empirical probabilities. They can only be determined
by observing numerous past instances of the speciﬁed conditions
(Mount Hood in July), and determining the relative frequency of the
event (new snow).
When determining empirical probabilities, it is vitally important
that each instance be characterized by the same set of conditions. In TA
this is a practical impossibility. Each past instance of a 2 percent drop
in interest rates is similar with respect to that speciﬁc condition, but
there are numerous other conditions that may not be the same. For example, the level of interest rates prior to the 2 percent drop may differ
from observation to observation. In one instance, interest rates were at
5 percent prior to the drop whereas in another they were 10 percent. Of
course, the level of interest rates could be added to the set of conditions that deﬁne each instance, but that has the downside of reducing
the number of comparable instances. Moreover, there will always be
other conditions that are not part of the speciﬁed condition set. The inability to control all potentially relevant variables is an unfortunate fact
of life in nonexperimental/observational sciences. In contrast, the experimental scientist enjoys the supreme advantage of being able to hold
constant all or nearly all relevant variables except the one being investigated. Imagine being able to do that in TA! I am told this is how it is in
the afterlife.
196 METHODOLOGICAL, PSYCHOLOGICAL, PHILOSOPHICAL, STATISTICAL FOUNDATIONS
--- page 196 ---

PROBABILITY DISTRIBUTIONS OF RANDOM VARIABLES
A probability distribution shows how often we can expect the different
possible values of a random variable to occur (i.e., their relative frequencies). The probability distribution of a random variable is a relative frequency distribution built from an inﬁnite number of observations.
The concept of a probability distribution can be understood by
thinking of a sequence of relative frequency distributions, each built
from increasing numbers of observations and progressively narrower
bins or intervals. Gradually, the relative frequency distribution becomes
a probability distribution. With increasing numbers of observations,
more discrete intervals of decreasing width can be created.22 As the
number of observations approaches inﬁnity, the number of intervals
approaches inﬁnity and their widths shrink to zero. Thus, the relative frequency distribution morphs into what is called a probability
distribution, more technically referred to as a probability density
function.23
Figures 4.19 though 4.23 show how a relative frequency distribution
evolves into a probability density function as the number of intervals is
increased and their interval widths are decreased. The height of each
bar represents the relative frequency of events falling within the bar’s interval. The ﬁgures presume that the random variable is a measure of
price change.
This succession of diagrams shows that a probability density function
is, in effect, a relative frequency distribution composed of an inﬁnite number of observations whose intervals are inﬁnitely narrow. Here is where
things get a bit strange. If the intervals of a probability distribution have
Statistical Analysis
197
Relative
Frequency
Price Change Intervals
FIGURE 4.19
Relative frequency distribution based on ﬁve intervals.
--- page 197 ---

198 METHODOLOGICAL, PSYCHOLOGICAL, PHILOSOPHICAL, STATISTICAL FOUNDATIONS
Relative
Frequency
Price Change Intervals
FIGURE 4.20
Relative frequency distribution based on seven intervals.
Relative
Frequency
Price Change Intervals
FIGURE 4.21
Relative frequency distribution based on ﬁfteen intervals.
Relative
Frequency
Price Change Intervals
FIGURE 4.22
Relative frequency distribution based on twenty nine intervals.
--- page 198 ---

zero width, then there are zero observations per interval. This seems to
make no sense! However, it is quite common for mathematical concepts
to be at odds with common sense. In geometry, a point has location but
occupies no space (i.e., length, width, and breadth equal zero), a line has
length but zero width, and so forth.
The fact that an interval has zero observations has a strange implication—the probability that any single value of a continuous random variable will ever occur is equal to zero. For this reason, it only makes sense
to speak of the probability that a random variable will assume a value
within a speciﬁed range of values. In other words, it makes sense to speak
of the probability that a random variable will assume a value between
speciﬁed minimum and maximum values. It also makes sense to speak of
the probability that a random variable will assume a value that is equal to
or greater than some speciﬁed value or less than or equal to a speciﬁed
value. For example, we can speak of the probability that a value of 3.0 or
greater will occur. However, it would make no sense to speak of the probability of a value of exactly 3.0.24
This somewhat counterintuitive idea ﬁts nicely with rule testing.
When testing the statistical signiﬁcance of a rule’s past rate of return, we
will be concerned with the probability that a rate of return of +10 percent
or higher could have occurred by chance under the condition that the rule
has no predictive power. Probability density functions can provide such
information.
Statistical Analysis
199
Probability
Density
No Specific Intervals
FIGURE 4.23
Probability density function.
--- page 199 ---

RELATIONSHIP BETWEEN PROBABILITY AND
FRACTIONAL AREA OF THE PROBABILITY DISTRIBUTION
Let’s recap what has been established up to this point:
1. The probability of an event is its relative frequency of occurrence
given an inﬁnite number of instances in which the event could have
occurred.
2. A probability density function is a relative frequency distribution built
from an inﬁnite number of observations and intervals of zero width.
3. The relative frequency of a random variable taking on a value within a
given interval is equal to the fractional area of the frequency distribution sitting on top of that interval. See Figure 4.24.
We are now ready to take the ﬁnal step in this sequence of thinking. It
is analogous to point 3 in the preceding list, except that the term relative
frequency distribution is replaced with probability density function. The
probability that a continuous random variable will assume a value within
a speciﬁed range is equal to the fraction of the probability density func-
200 METHODOLOGICAL, PSYCHOLOGICAL, PHILOSOPHICAL, STATISTICAL FOUNDATIONS
Relative
Frequency
0.019
0.019
0.091
0.234
0.091
0.234
0.312
Relative Frequency
of a Value in This Range = 0.344
Bars Represent 0.344 of
Distribution’s Total Area
Values of Random
Variable
FIGURE 4.24
The correspondence of relative frequency and fractional area of
a distribution.
--- page 200 ---

tion encompassed by (sitting above) that range. This concept is illustrated
in Figure 4.25. It shows the probability that X, a continuous random variable, will assume a value within the range A-B is equal to 0.70.
In many instances, the interval in question refers to the extreme or
tail of the distribution. For example, Figure 4.26 shows the probability
that random variable X will assume a value of B or greater. The probability is 0.15.
The probability distribution of a random variable is a very useful concept. Even though an individual future observation on random variable X
is not predictable, a large number of observations form a highly predictable pattern. This pattern is the random variable’s probability density
function.
Now, here is where these ideas start to come together for us. Chapter
5 will show that when a hypothesis is represented by the probability distribution of a random variable we will be able to use an observed value of
the random variable to test the veracity of the hypothesis. This will enable
us to conclude if a rule’s back-tested proﬁtability was due to luck or genuine predictive power.
The probability distribution used for this purpose is a speciﬁc type. It
is called a sampling distribution—perhaps the most important one in all of
statistics and certainly the most important for TA analysts.
Statistical Analysis
201
Range of Random Variable X
A
B
Area Above
Interval AB
Is
0.70 of
Distribution’s
Total Area
D
E
N
S
I
T
Y
P
R
O
B
A
B
I
L
I
T
Y
FIGURE 4.25
The probability random variable X will assume a value between A
and B equals the fraction of the distribution’s total area above the interval A,B.
--- page 201 ---

THE SAMPLING DISTRIBUTION: THE MOST IMPORTANT
CONCEPT IN STATISTICAL INFERENCE
To recap:
1. A random variable is the outcome of a probability experiment.
2. Taking a sample of a given number of observations from a population
and computing the value of a statistic such as the sample’s mean is a
probability experiment.25
3. A sample statistic26 is a random variable in the sense that it ﬂuctuates
unpredictably from one sample of observations to the next. The sample statistic ﬂuctuates randomly because chance determines which
speciﬁc observations wind up in a particular sample, and it is that particular set of observations that determines the value of the statistic for
that sample. In the box-of-beads experiment, the value f-g varied randomly from one 20-bead sample to the next because the particular set
of beads that wound up in a given sample was determined by chance.
4. A relative frequency distribution describes how often the possible
values of a random variable occur over a very large number of
observations.
We are now ready to meet the sampling distribution, the most important concept in statistical inference.
202 METHODOLOGICAL, PSYCHOLOGICAL, PHILOSOPHICAL, STATISTICAL FOUNDATIONS
Range of Random Variable X
B
D
E
N
S
I
T
Y
P
R
O
B
A
B
I
L
I
T
Y
Fraction of
Distribution
Beyond “B” = 0.15
of Area
0.15
FIGURE 4.26
The probability random  variable X will assume a value equal to or
greater than B equals the fraction of the distribution’s total area equal to or greater
than B.
--- page 202 ---

The Sampling Distribution Deﬁned
The sampling distribution is the probability distribution of a random variable, and that random variable happens to be a sample statistic. In other
words, the sampling distribution shows the various possible values the
sample statistic can assume, and their associated probabilities.27 For example, “the sampling distribution of the sample mean refers to the probability
distribution of all possible means for all possible random samples of a
given size from some population.”28 Here, the sample statistic is the mean.
The sample statistic in the box-of-beads experiments was f-g. Its random variation across 50 samples, each comprised of 20 beads, was shown
by the relative frequency distribution in Figure 4.8. If, instead of 50 values
we were to take all possible 20-bead samples—a very large number—this
theoretical distribution would be f-g’s sampling distribution.
In rule back testing, the sample statistic is a measure of performance
observed in a back test. In this book that sample statistic will be the rule’s
average rate of return. A back test typically produces a single observed
value for the performance statistic because we have a single sample of
market history. Now imagine what it would be like if we were able to test
a rule in an inﬁnite number of independent samples of market history.
This would provide an inﬁnite number of values for the performance statistic. If this set of data were then converted into a relative frequency distribution, it would be the statistic’s exact sampling distribution. This is
obviously not possible because we do not have an inﬁnite number of independent samples of historical data. However, statisticians have developed
several methods to get something that approximates the exact sampling
distribution closely enough to be useful, despite the fact that we have only
one sample of historical data and one value of the sample statistic. Two of
these methods will be discussed later in this chapter.
The Sampling Distribution Quantiﬁes Uncertainty
The sampling distribution of a statistic is the foundation of statistical inference because it quantiﬁes the uncertainty caused by the randomness of
sampling (sampling variability).
As stated above, the sampling distribution displays the relative frequencies of a statistic if it were to be measured in an inﬁnite number of
random samples of the same size, drawn from the same parent population. The box-of-beads experiments showed that the value of a statistic, f-g
ﬂuctuated randomly from sample to sample. Figure 4.8 showed that these
values tend to fall into a well-behaved pattern, not a random chaotic mess.
The fact that the pattern of random variation is well behaved is what
makes statistical inference possible.
Statistical Analysis
203
--- page 203 ---

It may seem ironic that a sample statistic would show such a regular pattern given that it is, in fact, a random variable. Thankfully for statisticians, it does. Figure 4.8 revealed a central value (i.e., the mean of
the sampling distribution) of approximately 0.55. It also showed a welldeﬁned pattern of dispersion about this central value. This pattern allowed us to conclude, with a fair degree of assurance, that the value of the
population parameter F-G was contained within the range 0.40 to 0.65. It
also allowed us to conclude, although with somewhat diminished conﬁ-
dence, that F-G was more accurately pinned in the range between 0.50
and 0.60. It was the degree of dispersion in f-g’s sampling distribution that
permitted these statements to be made about the value of the population
parameter F-G.
The dispersion of the sampling distribution quantiﬁes the uncertainty
of our knowledge about the population parameter F-G. The distribution’s
central tendency conveys information about the most likely value of F-G,
approximately 0.55. Knowing this is nice, but it is not enough. It is also important to know about the reliability of the value 0.55. In other words,
how accurately does the sampling distribution’s central tendency of 0.55
portray the true value of F-G?
The reliability (degree of certainty) is conveyed by the dispersion of
the sampling distribution. The greater the distribution’s dispersion around
its central value, 0.55, the less certain we can be that 0.55 accurately informs us about the true value F-G, the proportion of grey beads in the entire box.
To illustrate this point consider the two following sampling distributions. Both have central values of 0.55 but their dispersions are quite different. The ﬁrst shown in Figure 4.27 is a narrow dispersion thereby
delivering a strong impression that F-G is in the vicinity of 0.55. The distribution in Figure 4.28 is wider thus conveying a less certain message about
F-G value. It is saying that the true value F-G may be considerably different from the central value of the sampling distribution.
In summary, certainty is directly related to the dispersion of the sampling distribution. And the certainty of a conclusion about a population
parameter depends upon the width of the statistic’s sampling distribution—greater width means greater uncertainty.
Suppose it is hypothesized that a rule’s expected return is equal to
zero. Also suppose the rule’s back-tested return turns out to be greater
than zero. Is the positive return sufﬁcient evidence to conclude that the
hypothesized value of zero is false? The answer will depend on how far
above zero the back-tested return is relative to the width of the sampling distribution. If the relative deviation is large the hypothesis can be
rejected. Quantifying the relative deviation and the reasoning behind a
204 METHODOLOGICAL, PSYCHOLOGICAL, PHILOSOPHICAL, STATISTICAL FOUNDATIONS
--- page 204 ---

Statistical Analysis
205
0
0.02
0.04
0.06
0.08
0.1
0.12
0.14
0.16
0.18
0.2
0
0.1
0.2
0.3
0.4
0.5
0.6
0.7
0.8
0.9
1
f–g
F
R
E
L
A
T
I
V
E
R
E
Q
U
E
N
C
Y
FIGURE 4.27
Relative frequency distribution: f-g. (sample size = 20, number of
samples=50).
0
0.02
0.04
0.06
0.08
0.1
0.12
0.14
0.16
0.18
0.2
0
0.1
0.2
0.3
0.4
0.5
0.6
0.7
0.8
0.9
1
f–g
F
R
E
L
A
T
I
V
E
R
E
Q
U
E
N
C
Y
FIGURE 4.28
Relative frequency distribution: f-g. (sample size = 20, number of
samples=50).
--- page 205 ---

decision to reject or not to reject the hypothesis will be treated in Chapter 5. The important point for now is that the width of the sampling distribution is critically important in answering this question.
Sampling Distribution of Trading Performance
A sampling distribution can be formed for any statistic: the average
(mean), the median, the standard deviation, and many other statistics
used in statistical inference.29 Each has its own sampling distribution.
This discussion here is conﬁned to the sampling distribution of the
mean because the performance statistic used to evaluate TA rules in this
book is a rule’s mean rate of return. However, there are many other performance measures that might be used: the Sharpe ratio,30 the proﬁt factor,31
the mean return divided by the Ulcer Index,32 and so forth. It should be
pointed out that the sampling distributions of these alternative performance
statistics would be different from the sampling distribution of the mean.
It should also be pointed out that the methods used in this book to
generate the sampling distribution of the mean may be of limited value in
generating sampling distributions for performance statistics with elongated right tails. This can occur with performance statistics that involve
ratios such as the Sharpe ratio, the mean-return-to-Ulcer-Index ratio, and
the proﬁt factor. However, this problem can be mitigated by taking the log
of the ratio to shorten the right tail.
The Three Distributions of Statistical Inference
Statistical inference actually involves three different distributions, one of
which is the sampling distribution. They are easy to confuse. This section
is intended to clarify their differences. In the context of rule testing the
three distributions are:
1. Data distribution of the population: an inﬁnite sized distribution
comprised of all possible daily rule returns, which we assume extends
into the immediate practical future.
2. Data distribution of the sample: a distribution comprised of a ﬁnite
number (N) of daily rule returns from the past.
3. Sampling distribution: an inﬁnite-sized distribution of the sample
statistic—in this case it is the rule’s mean return. It represents the
mean returns of the rule, if it were to be tested in an inﬁnite number
of random samples of size N extracted from the population.
There are two points to emphasize. First, the observations comprising
the data distribution of the population and the data distribution of the
206 METHODOLOGICAL, PSYCHOLOGICAL, PHILOSOPHICAL, STATISTICAL FOUNDATIONS
--- page 206 ---

sample (1 and 2 in the preceding list) are comprised of single-day rule returns. In contrast, the observations comprising the sampling distribution
are sample statistics in which each observation represents the mean return of the rule computed over a sample of days. Second, both the population distribution and the sampling distribution are theoretical in the sense
that they refer to an inﬁnite number of possible observations. In contrast,
the data distribution of the sample is composed of a ﬁnite number of observations from a historical back test.
The relationship between these three distributions can be visualized
by imagining an experiment similar to the box-of-beads experiment. In
this case, however, you are to imagine a population distribution of daily
rule returns that is inﬁnite in size. Imagine taking 50 independent samples
from the population, where each sample is comprised of a substantial
number of daily rule returns. Next, determine the mean return for each
sample and then plot the sampling distribution of the 50 means. This is illustrated in Figure 4.29.33
The Real World: The Problem of One Sample
The preceding discussion was theoretical in the sense that we imagined
what it would be like if we could observe 50 independent samples from a
Statistical Analysis
207
Sample #2 of n
Daily returns
Sample #1 of n
Daily returns
Sample # 50 of n
Daily Returns
Mean Sample #1
Mean Sample #2
Mean Sample #50
Data
Distribution
in the
Sample
of Size n
(daily returns)
Parent
Population Mean
Sampling
Distribution
50
Sample Means
Data
Distribution
in the
Population
(daily returns)
Distribution of the Means
of Sample Size n
FIGURE 4.29
The three distributions of statistical inference.
--- page 207 ---

parent population. In most real-world statistical problems, there is only
one sample of observations and thus one value for the sample mean. The
problem is that with only one sample mean available we have no notion of
the sample statistic’s variability. The problem of one sample and one mean
is illustrated in Figure 4.30.
Fortunately, we can learn a lot about a sample statistic’s variability
and its sampling distribution by looking at the single available sample.
The discovery of how to do this, early in the twentieth century, is what
made the ﬁeld of statistical inference possible. In fact, statisticians have
developed two distinct approaches for estimating the sampling distribution of a statistic from a single sample of observations: classical and computer intensive. Although both will be discussed, the computer-intensive
approach will be used for the rule tests performed in Part Two.
DERIVING THE SAMPLING DISTRIBUTION:
THE CLASSICAL APPROACH
This classical approach is the one most often taught in basic statistics
courses. It is attributed to the two fathers of mathematical statistics, Sir
Ronald Fisher (1890–1962) and Jerzy Neyman (1894–1981). It utilizes
probability theory and integral calculus to derive the sampling distribution on the basis of a single observed sample. It provides estimates of the
sampling distribution’s dispersion, its mean, and its basic shape (normal).
208 METHODOLOGICAL, PSYCHOLOGICAL, PHILOSOPHICAL, STATISTICAL FOUNDATIONS
Daily Returns
Distribution of  Daily Returns
Comprising the Population
Daily Returns
Distribution of Daily Returns
Comprising the Sample
One Value for Sample
Mean
(known)
Population
Mean
 (not known)
FIGURE 4.30
The real world: one sample and one value of the test statistic.
--- page 208 ---

In other words, it provides everything needed to quantify the reliability of
an inference based on a single sample of observations.
The Sampling Distribution of the Sample Mean
Every statistic has its own sampling distribution. This discussion will focus on the sampling distribution of the mean (average), because it is the
statistic used in Part Two to evaluate TA rules.
Classical statistical theory tells us several things about the sampling
distribution of the mean.
1. The mean of a large sample is a good estimate of the mean of the population distribution from which the sample was obtained. The larger
the sample, the more closely the sample mean conforms to the population mean.
2. The dispersion of the sampling distribution depends on the size of the
sample. For a given population, the larger the sample, the narrower
the sampling distribution.
3. The dispersion of the sampling distribution also depends on the
amount of variation within the parent population data. The bigger the
variation in the parent population, the wider the sampling distribution.
4. Under the conditions that apply to the evaluation of TA rules, the
shape of the sampling distribution of the mean will tend towards the
so-called normal or bell shape, with the conformity to the normal
shape increasing as the sample size increases. Other sample statistics,
such as ratios, can be profoundly nonnormal.
Each of these concepts is now explained.
The Mean of a Large Sample Is a Good Estimate of the Population Mean.
This is a manifestation of The Law of Large Numbers,
which we met previously in the context of a coin-ﬂipping experiment. To
recap, The Law of Large Numbers tells us that the larger the number of
observations comprising the sample, the more closely the sample mean
will approximate the population mean. There are some qualifying conditions34 attached to this promise, but they need not concern us here.
The graph of the coin-ﬂipping experiment illustrated the action of the
Law of Large Numbers (Figure 4.18). As the number of coin tosses increased, the proportion of heads gradually converged to its theoretically
correct value of 0.50. In the early stages of the experiment, when the sample size was small, there were large departures from 0.50. These departures illustrate the large role that chance plays in small samples. In four
Statistical Analysis
209
--- page 209 ---

tosses, though values of 0.75 or 0.25 are not the most probable, they are
quite common. However, when the number of coin tosses reaches 60, the
probability of 0.75 or 0.25 is less than 1 in 1,000. The important lesson: Increased sample size diminishes the role of chance.
The Dispersion of the Sampling Distribution Depends on the
Size of the Sample: the Larger the Sample the Less the Dispersion.
Imagine a very large population of observations on some variable whose standard deviation is 100. Usually, we do not know the
population standard deviation, but in this case we will assume that we do.
In Figure 4.31, I show the parent population distribution at the bottom. Above it are two sampling distributions for the variable’s mean for
sample sizes of 10 and 100. Notice that the width of the sampling distribution is cut by approximately one-third each time the sample size is increased by a factor of 10. One of the lessons from classical statistics is
that the standard deviation of the sampling distribution of the mean is inversely proportional to the square root of the sample size.35 Thus, if the
sample size is increased by a factor of 10, the width of the sampling distribution is reduced a factor of 3.16, the square root of 10. The parent distrib-
210 METHODOLOGICAL, PSYCHOLOGICAL, PHILOSOPHICAL, STATISTICAL FOUNDATIONS
Distribution of Data
in the Population
St. Deviation =100
Sampling Distribution
of The Mean
Sample Size = 10
St. Error = 31.62
Sampling Distribution
of the Mean
Sample Size = 100
Standard Error = 10
100
31.62
10
FIGURE 4.31
The narrowing of the sampling distribution with increased sample size.
--- page 210 ---

ution can be thought of as a sampling distribution with a sample size of
one (one mean—the population mean). The sampling distribution for a
sample size of 100 is one-tenth the width of the parent population. The essential message is the larger the sample size, the less the uncertainty
about the value of a sample statistic. Incidentally, the standard deviation
of the sampling distribution of the mean is given a special name in statistics, the standard error of the mean (see later explanation).
With some qualiﬁcations,36 the Law of Large Numbers tells us that the
larger the sample size, the more accurate our knowledge of the population’s average. With some caveats,37 therefore, we would like to work with
samples that are as large as possible so as to minimize the width of the
sampling distribution as much as possible.
The Dispersion of the Sampling Distribution of the Mean Also
Depends On the Amount of Variation within the Data Comprising the Parent Population.
There is another factor that impacts the
width of the sampling distribution—the amount of variation within the
parent population from which the sample was taken. The greater the variation within the population data, the greater will be the variation (dispersion) of the sampling distribution.
You can visualize this by thinking about a population that has no variation at all. For example, if all people in the population weighed 150 lbs,
every sample is going to have an average weight of 150 lbs. Therefore,
zero variation among the members of the population would lead to zero
variation in the sample average, and consequently a sampling distribution
that has no dispersion whatsoever. Conversely, if there is great variation
among the individuals comprising the population, there is going to be
greater variation in the sample averages, which translates to a fat sampling distribution.
Shape of the Sampling Distribution Tends Toward Normal.
The Central Limit Theorem, a foundational principle of classical statistics,
states that as the size of a sample gets larger, the sampling distribution of
the mean, with some qualiﬁcations,38 converges toward a speciﬁc shape irrespective of the shape of the population distribution. In other words, no
matter how weirdly shaped the distribution of the data in the parent population, the shape of the sampling distribution approaches a speciﬁc shape
that statisticians refer to as the normal distribution, also known as the
Gaussian distribution.
The normal distribution is the shape of the most common probability distribution. Often referred to as the bell curve because it has the silhouette of the Liberty Bell, the normal distribution characterizes
continuous variables that describe many real-world phenomena.
Statistical Analysis
211
