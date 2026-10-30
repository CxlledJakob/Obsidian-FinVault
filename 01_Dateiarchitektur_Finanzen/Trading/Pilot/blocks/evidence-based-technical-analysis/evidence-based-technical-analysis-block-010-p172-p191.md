# Evidence-based Technical Analysis_ Applying the Scientific Method and Statistical Inference to Trading Signals.pdf — pages 172–191

--- page 172 ---

The central concept of statistical inference is extrapolating from samples. A sample of observations is studied, a pattern is discerned, and this
pattern is expected to hold for (extrapolated to) cases outside the observed sample. For example, a rule observed to be proﬁtable in a sample
of history is projected to be proﬁtable in the future.
Let’s begin to think about the concept in the context of a problem that
has nothing to do with technical analysis. It comes from an excellent
book: Statistics, A New Approach by Wallis and Roberts.9 The problem
concerns a box ﬁlled with a mixture of white and grey beads. The total
number of beads and the numbers of grey and white beads are unknown.
The task is to determine the fraction of beads that are grey in the entire
box. For purposes of brevity, this value will be designated as F-G (fraction-grey in box).
To make this situation similar to statistical problems faced in the real
world, there is a wrinkle. We are not allowed to view the entire contents
of the box at one time, thus preventing a direct observation of F-G. This
constraint makes the problem realistic because, in actual problems, observing all the items of interest, such as all beads in the box, is either impossible or impractical. In fact, it is this constraint that creates the need
for statistical inference.
Although we are not allowed to examine the box’s contents in its entirety, we are permitted to take samples of 20 beads at a time from the box
and observe them. So our strategy for acquiring knowledge about F-G will
be to observe the fraction of grey beads in a multitude of samples. In this
example 50 samples will be taken. The lowercase f-g stands for the fraction of grey beads in a sample.
A sample is obtained as follows: The bottom of the box contains a
sliding panel with 20 small depressions, sized so that a single bead is captured in each depression. The panel can be slid out of the box by pushing
it with a similar panel that takes its place. This keeps the remaining
beads from dropping out of the bottom. Consequently, each time the
panel is removed, we obtain a sample of 20 beads and have the opportunity to observe the fraction grey (f-g) in that sample. This is illustrated in
Figure 4.5.
After the fraction of grey beads (f-g) in a given sample has been determined, the sample beads are placed back into the box and it is given a
thorough shaking before taking another sample of 20. This gives each
bead an equal chance of winding up in the next sample of 20. In the parlance of statistics, we are making sure that each sample is random. The
entire process of taking a sample, noting the value f-g, putting the sample
back in the box, and shaking the box is repeated 50 times. At the end of
the whole procedure we end up with 50 different values for f-g, one value
for each sample examined.
Statistical Analysis
173
--- page 173 ---

By placing each sample back in the box before taking another sample, we are maintaining a stable concentration for the fraction of grey
beads in the box. That is to say, the value for F-G is kept constant over
the course of the 50 samplings. Problems in which the statistical characteristics remain stable over time are said to be stationary. If the beads
were not replaced after each sample the value F-G would change over the
course of the 50 samplings, as groups of beads were permanently removed from the box. A problem in which the statistical characteristics
change over time is said to be nonstationary. Financial markets may indeed be nonstationary, but for pedagogical purposes, the box-of-beads
problem is designed to be stationary.
It is important to keep in mind the distinction between F-G and f-g.
F-G refers to the fraction of grey beads in the entire box. In the language
of statistics, all the observations in which we are interested are called a
population. In this example, the term population refers to the color of all
the beads in the box. The term sample refers to a subset of the population. Thus, F-G refers to the population while f-g refers to the sample.
Our assigned task is to gain as much knowledge as possible about the
value of F-G by observing the value f-g over 50 separate samples.
It is also important to keep clear the distinction between two numbers: the number of observations comprising a sample—in this case 20
beads—and the number of samples taken—in this case 50.
PROBABILITY EXPERIMENTS AND RANDOM VARIABLES
Probability is the mathematics of chance.10 A probability experiment is
an observation on or a manipulation of our environment that has an uncertain outcome.11 This would include actions such as noting the pre-
174 METHODOLOGICAL, PSYCHOLOGICAL, PHILOSOPHICAL, STATISTICAL FOUNDATIONS
What Fraction
Are
Gray?
F–G
Sliding Panel
FIGURE 4.5
Determining f-g for each sample.
--- page 174 ---

cise time of arrival after a long trip, observing the number of inches of
snow that falls in a storm or the face of a coin that appears after the
tossing of a coin.
The quantity or quality observed in a probability experiment is called
a random variable such as the face of a coin after a ﬂip, the number of
inches of snow that fell, or a value that summarizes a sample of observations (e.g., a sample average). This quantity or quality is said to be random
because it is affected by chance. Whereas, an individual observation of a
random variable is unpredictable, by deﬁnition, a large number of observations made on a random variable may have highly predictable features.
For example, on a given coin toss, it is impossible to predict head or tails.
However, given one thousand tosses, that the number of heads will lie
within a speciﬁed range of 500 is highly predictable.
Depending on how it is deﬁned, a random variable assumes at least
two different values, though it can assume more—perhaps even an inﬁnite
number. The random variable in a coin toss, the face visible after the toss,
can assume two possible values (heads or tails). The random variable, de-
ﬁned as the temperature at noon taken at the base of the Statue of Liberty,
can assume a very large number of values, with the number limited only
by the precision of the thermometer.
Sampling: The Most Important
Probability Experiment
The most important probability experiment in statistical analysis is sampling. It involves the extraction of a subset of observations from a population. Here the random variable at issue is called a sample statistic. It is any
computable characteristic of the sample. The value f-g is an example of a
sample statistic.
Sampling can be done in a number of different ways, but it is crucial
that the observations that are selected for the sample be chosen in a random manner and that they be selected independently of each other. This
means that all observations that could possibly end up in the sample have
an equal chance of doing so. Because no particular observation has a better chance of appearing in the sample than any other, the observations
that wind up in the sample do so by chance. Samples must be constructed
in this manner because the principles of probability, upon which statistical reasoning rests, assume that the observations that wind up in the sample got there randomly.
Consider the test of a new medicine on a sample of volunteers. The
sample must be constructed so that anyone who might eventually take the
medicine has an equal chance of being selected for the test group. If the
subjects in the experiment are not selected this way, the results of the test
Statistical Analysis
175
--- page 175 ---

will not lead to a sound conclusion. A medical experiment that selects test
subjects who are expected to respond favorably to the medication will
produce a biased conclusions. In other words, the estimates of the medication’s efﬁcacy in the general population will be too optimistic.
Imagine taking a single bead at random from the box with your eyes
closed and then observing its color. This is a sampling experiment with a
sample size of one. The bead’s color, grey or white, is the random variable.
Now imagine randomly selecting 20 beads from the box. Here the sample
size is 20 and the fraction grey in that sample (f-g) is a sample statistic that
is also a random variable.
As discussed earlier, we will call this random variable f-g. It is a random variable because its value is affected by chance. It can assume 21 different values {0, 0.05, 0.10, 0.15, . . . , 1.0}. Now let’s get back to the goal:
increasing our knowledge about the value of F-G.
The Knowledge Gleaned from One Sample
Suppose the ﬁrst sample contains 13 grey beads out of 20. The value of the
sample statistic f-g is 0.65 (13/20). What does this tell us about F-G? With
only this information, some might be tempted to conclude that we have
solved the problem, and that 0.65 is the fraction grey for the entire box
(i.e., F-G = 0.65). This view tacitly and naively assumes that a single sample can provide perfect knowledge. At the opposite extreme are those
who just as wrongly conclude that the sample is too small to supply any
information.
Both conclusions are wrong. First, there is no basis for thinking that
we could acquire perfect knowledge from one sample. Though it is possible that a single sample of 20 beads might be a perfect replica of the
entire contents of the box, it is not likely. For example, if the true value
of F-G were 0.568, a 20-bead sample could never produce such a value.
An f-g value of 0.55 (11 grey of 20) is as close as one could get. Ten grey
beads in the sample would give an f-g of 0.50, 11 would give 0.55, and 12
would give 0.60.
Those who assert that nothing has been learned are also mistaken.
On the basis of this sample alone, two possibilities can be eliminated.
We can reject with absolute certainty that F-G = 1.0 (i.e., all beads grey)
because there were 7 white beads in the sample. With equal certainty,
we can reject the proposition that F-G is 0, because there were 13 grey
beads in the sample.
However, more precise estimates of F-G on the basis of the single observed value of f-g are subject to uncertainty. Even if we were to take numerous samples and have numerous values of f-g, the value of F-G would
remain uncertain. This is because a sample is, by deﬁnition, a partial rep-
176 METHODOLOGICAL, PSYCHOLOGICAL, PHILOSOPHICAL, STATISTICAL FOUNDATIONS
--- page 176 ---

resentation of the full contents of the box. Only by observing every bead
in the population could all uncertainty about F-G be eliminated. And this
is prohibited.
However, with what has been learned from the single sample, some
intelligent guesses can be made that go beyond the certain knowledge that
F-G is neither 0 nor 1.0. For example, although a claim that F-G is as low
as 0.10 cannot be conclusively ruled out; no one would take it seriously.
The observed f-g value of 0.65 obtained from the ﬁrst sample is too far
above 0.10 for it to be a credible estimate of F-G. If F-G really were as low
0.10, the probability of getting a sample with an f-g of 0.65 would seem unlikely just based on common sense. We could apply the same kind of logic
to dispense with a claim that F-G = 0.95. An f-g reading of 0.65 would seem
too low if the entire box were composed of 95 percent grey beads. The
bottom line: It is fair to say that a single sample does provide some knowledge about F-G.
What Can Be Learned from 50 Samples?
Greater knowledge about F-G can be obtained by analyzing more samples.
Assume another 49 samples are taken and the value f-g for each sample is
measured. The ﬁrst thing we would notice is that f-g varies in an unpredictable fashion from sample to sample. This particular form of random
behavior is one of the most important phenomena in all of statistics. It is
called sampling variability or sampling variation.
Sampling variation is important because it is responsible for the uncertainty in statistical conclusions. Greater sampling variability translates
to greater uncertainty. The greater the ﬂuctuations in f-g from one sample
to the next , the greater will be the uncertainty about the value of F-G.
Regrettably, this important phenomenon, sampling variability, is unfamiliar to many people who analyze data. This is understandable because
real world problems do not offer the luxury of looking at more than one
independent sample. The box-of-beads provides this opportunity.
As will be seen, by conducting 50 sampling experiments, the random
variation in f-g becomes obvious. This is quite different from the situation
faced by rule researchers. They typically have a single historical sample of
the market, and if all that data is used to test a rule, only one observed
value of the performance statistic is obtained. This provides no opportunity to see how the rule’s performance would vary if it were tested in numerous independent samples. The bottom line is this: Sampling variation
is an important fact that may not be obvious to data analysts unfamiliar
with statistical analysis. This is a huge blind spot!
Sampling variation can be seen in a table of the 50 f-g values. See
Table 4.1.
Statistical Analysis
177
--- page 177 ---

Not surprisingly, the value of f-g, a random variable, ﬂuctuates from
sample to sample. This is an example of chance in operation. However,
f-g’s value is not entirely determined by chance. Its value is also
strongly inﬂuenced by the value of F-G, the proportion of grey beads in
the entire box.
Thus, it can be said that each observed value of f-g is the result of two
inﬂuences; the underlying phenomenon, F-G, and randomness caused by
sampling. F-G acts like a center of gravity, always keeping f-g within a certain range. In some samples, randomness nudged the value f-g above F-G.
In other samples, randomness nudged f-g below F-G. From sample to sample the value of f-g oscillates randomly around this center of gravity. This
is sampling variability.
Another important aspect of this situation is that the number of observations impacts our level of uncertainty about the value of F-G. The
greater the number of observations comprising the sample, the more precisely the value f-g will reﬂect the value F-G. Suppose that, instead of taking a 20-bead sample, we took a 200-bead sample. The random variation in
f-g around F-G would be smaller. In fact, it would be about one third of
what it is for a 20-bead sample. This is a very important point: the larger
the sample size, the smaller the impact of randomness. Two hundred
beads dampen the ability of any single bead to push f-g away from F-G. In
178 METHODOLOGICAL, PSYCHOLOGICAL, PHILOSOPHICAL, STATISTICAL FOUNDATIONS
TABLE 4.1
Fraction of Grey Beads in 50 Different Samples
Sample
Sample
Sample
Number
f-g
Number
f-g
Number
f-g
1
0.65
18
0.60
35
0.60
2
0.60
19
0.40
36
0.55
3
0.45
20
0.60
37
0.50
4
0.60
21
0.45
38
0.50
5
0.45
22
0.55
39
0.45
6
0.45
23
0.45
40
0.50
7
0.55
24
0.50
41
0.55
8
0.40
25
0.70
42
0.45
9
0.55
26
0.55
43
0.55
10
0.40
27
0.60
44
0.60
11
0.55
28
0.70
45
0.60
12
0.50
29
0.50
46
0.60
13
0.35
30
0.70
47
0.65
14
0.40
31
0.50
48
0.50
15
0.65
32
0.90
49
0.50
16
0.65
33
0.40
50
0.65
17
0.60
34
0.75
--- page 178 ---

a one-bead sample, the single selected bead will produce an f-g of either 0
or 1.0. In a two-bead sample, f-g can be 0, 0.50 or 1.0. In a three-bead sample, f-g can be 0, 0.33, 0.66, or 1.0. Thus, the larger the sample size, the
smaller will be the magnitude of random variation in f-g. Large samples
give F-G, the truth that we wish to know, the ability to reveal itself. This is
an effect of the Law of Large Numbers: Large samples reduce the role of
chance. In other words, it can be stated that the larger the size of a sample, the more tightly the values of f-g will cluster about the value F-G. This
is one of the most important principles in statistics.
We have learned an important concept of statistics that can be
stated as follows: even though the value of F-G does not change over
the course of the 50 sampling experiments, the value f-g can vary considerably from sample to sample. The phenomenon is called sampling
variability. It is present whenever a random sample of observations is
used to form a conclusion about a larger universe (i.e., population).
Sampling variability is the source of the uncertainty that is addressed
by statistical inference.12
Frequency Distribution of the Sample Statistic f-g
In the box-of-beads experiment, the random variable f-g can assume
21 possible values ranging from zero, when there are no grey beads in
a sample, to 1.0, when the sample is composed entirely of grey beads.
The 50 observed values of f-g are shown in Table 4.1. A casual examination shows that some values of f-g occurred with greater frequency than
others. Values in the range of 0.40 to 0.65 occurred quite often, whereas
values less than 0.40 and greater than 0.65 almost never occurred. In
the 50 samples taken, f-g assumed the value 0.50 nine times, 0.55 eight
times, and 0.60 ten times. Note that the value 0.65, which characterized
the ﬁrst sample, appeared only ﬁve times. Therefore, that value was
not among the most common values, but it was not particularly unusual
either.
A plot called a frequency distribution or frequency histogram communicates this information more forcefully than words or a table. It displays
how frequently each of f-g’s possible values occurred over the 50 sampling
experiments. The term distribution is apt, because it depicts how a set of
observations on a random variable are distributed or sprinkled across the
variable’s range of possible values.
Arrayed along the horizontal axis of the frequency distribution is a sequence of intervals, or bins, one for each possible value of f-g. The height
of the vertical bar over each interval represents the number of times that a
speciﬁc value of f-g occurred. Figure 4.6 shows the frequency distribution
of the 50 f-g values.
Statistical Analysis
179
--- page 179 ---

The Equivalence of Frequency and Area
Frequency distributions depict an important relationship between the
frequency of a particular value or set of values and the area covered by
the bars representing that value or set of values. This concept can be
understood if we ﬁrst consider the entire distribution. In Figure 4.6, all
the grey bars comprising the frequency distribution represent all 50
of the observed values of f-g. Thus, the area covered by all the vertical bars corresponds to 50 observations. You can verify this by summing the counts associated with all of the vertical bars. They will add
up to 50.
The same principle applies to any fraction of the distribution’s area. If
you were to determine the fraction of the frequency distribution’s total
area covered by the area of a single bar, you would ﬁnd that the bar’s fractional area is equal to the fraction of the total observations represented by
that bar. For example, the vertical bar associated with the f-g value 0.60
shows a count (frequency) of 10. Thus, the bar represents 20 percent
(10/50) of the observed values. If you were to then measure the area covered by this vertical bar, you would ﬁnd that its area represents 0.20 of
the total area covered by the entire distribution. This idea is illustrated in
Figure 4.7.
180 METHODOLOGICAL, PSYCHOLOGICAL, PHILOSOPHICAL, STATISTICAL FOUNDATIONS
0
1
2
3
4
5
6
7
8
9
10
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
Sample Size = 20       Number of Samples = 50
f–g
F
R
E
Q
U
E
N
C
Y
FIGURE 4.6
Frequency Distribution: (f-g).
--- page 180 ---

Although this idea may seem obvious, even trivial, it is an essential
aspect of statistical reasoning. Ultimately, we will use the fractional area
of a distribution to measure the probability that the back-test proﬁts of a
rule could have occurred by chance under the assumption that the rule
has no predictive power. When that probability is small, we are led to the
conclusion that the rule does have predictive power.
Relative Frequency Distribution of f-g
The relative frequency distribution is similar to the ordinary frequency
distribution discussed earlier. The height of a bar in an ordinary frequency
distribution represents an absolute number or count of the number of
times a particular value of a random variable was observed to occur. In
the relative frequency distribution, the height of a bar represents the number of observed occurrences relative to (divided by) the total number of
observations comprising the distribution. For example, f-g assumed the
value 0.60 on 10 out of 50 observations. Thus the value 0.60 had a relative
frequency of 10/50 or 0.20. The distribution’s bar for the value 0.60 would
be drawn to a height of 0.20 along the vertical scale. This is illustrated in
Figure 4.8.
Statistical Analysis
181
0
1
2
3
4
5
6
7
8
9
10
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
Q
U
E
N
C
Y
This Bar Has 0.20
of Distribution’s
Total Observations
This Bar Has 0.20
of Distribution’s
Total Area
FIGURE 4.7
Proportion of observations equals proportion of distribution’s total area.
--- page 181 ---

The equivalence between frequency and area that applies to ordinary
frequency distributions also applies to relative frequency distributions.
The relative frequency of all bars is equal (adds up) to 1.0. This simply
says that a random variable always (1.0 of the time) assumes a value
somewhere in the range encompassed by all bars. If you were to add up
the relative frequencies associated with all of the individual bars comprising the distribution, they would sum to 1.0 (100 percent of the observations). This has to be so because each bar represents the fraction of
observations falling into that interval, and, by deﬁnition, all the bars together represent all (1.0) the observations.
The relative frequency of any single bar or group of contiguous bars is
equal to their proportion of the distribution’s total area. Thus the relative
frequency of an f-g value of 0.65 and larger is equal to 0.10 + 0.06 + 0.02 +
0.02 = 0.20. This is equivalent to saying that the combined area of the contiguous bars associated with f-g values of 0.65 and larger is 20 percent of
the distribution’s total area. We will be making statements similar to this
when testing claims about TA rules. Based on this, it can be said that the
relative frequency of f-g values equal to or greater than 0.65 is 0.20. This is
illustrated in Figure 4.9.
182 METHODOLOGICAL, PSYCHOLOGICAL, PHILOSOPHICAL, STATISTICAL FOUNDATIONS
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
Sample Size = 20       Number of Samples = 50
FIGURE 4.8
Relative frequency distribution: (f-g).
--- page 182 ---

What Knowledge Has Been Gained about F-G
from Sampling?
So far, sampling has increased our level of knowledge about F-G. In the
ﬁrst 20-bead sample, f-g had a value of 0.65. Based on this observation,
two possibilities were conclusively ruled out: that F-G is equal to 0, and
that F-G is equal to 1.0.
Not being content with these meager morsels of wisdom, another 49
samples were taken, and the value f-g was observed in each. These 50 values showed that f-g varies randomly from sample to sample. However, despite the unpredictability of any single f-g value, an organized pattern
emerged from the randomness that was informative. The f-g values coalesced about a central value forming a well-organized hump. We suspect
that this central tendency is related to the value F-G, yet F-G’s precise
value remains uncertain because of the random variation in f-g. However,
in light of the hump’s relatively narrow width, it seems reasonable to conjecture that F-G lies somewhere in the range 0.40 to 0.65.
Given that we started with no knowledge of F-G and given that we
were precluded from examining the contents of the box in its entirety, a
lot was learned from these 50 samples.
Statistical Analysis
183
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
Sample Size = 20       Number of Samples = 50
Relative
Frequency
f–g = or > 0.65
Is 0.20
FIGURE 4.9
Relative frequency distribution: (f-g).
--- page 183 ---

A Second Box of Beads
Now we will use sampling to learn the color proportions of a second box
of beads. It too is a mixture of grey and white. The objective is the same—
to learn the relative proportion of grey beads to the total number of beads
in a second box. We call this quantity F-G 2.
As before, we are not allowed to examine the full contents of box 2,
but we are permitted to take 50 samples, each composed of 20 beads. The
value f-g 2, which refers to the proportion of grey beads in a sample from
box 2, is measured in each sample. Again, note the distinction between
the terms F-G 2 and f-g 2. F-G 2 refers to the proportion of grey beads in
the entire box 2 whereas f-g 2 refers to the proportion of grey beads in an
individual sample. F-G 2 is not observable while f-g 2 is.
Figure 4.10 is the relative frequency distribution for 50 values of f-g 2.
There are several things to notice:
1. The general shape of the distribution for box 2 is similar to that of box
1, a hump clustering about a central value.
2. The central value of the distribution for box 2 is different than that of
box 1. The distribution for box 1 was centered near a value of 0.55.
The central value for box 2’s distribution is near 0.15. This is clearly
184 METHODOLOGICAL, PSYCHOLOGICAL, PHILOSOPHICAL, STATISTICAL FOUNDATIONS
0
0.3
0.25
0.2
0.15
0.1
0.05
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
f-g
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
Sample Size = 20       Number of Samples = 50
FIGURE 4.10
Relative frequency distribution box 2: (f-g).
--- page 184 ---

seen in Figure 4.11, which shows both distributions on the same horizontal scale. An arrow has been placed above each distribution at
their approximate central values. Thus the arrows represent average
values for f-g and f-g 2. From this we can conclude that box 1 has a
higher concentration of grey beads than box 2.
3. Even though the samples from box 1 and box 2 were both affected by
random variation, the degree of random variation differs. Box 2’s results are less variable than those of box 1. This is evidenced by box 2’s
narrower clustering about its central value. Given the lower degree of
sampling variation in box 2, it would be fair to say that we know the
value of F-G 2 with greater certainty than we know F-G.
What the Box Experiments Taught Us
about Statistics
Yogi Berra, former manager of the New York Yankees, said you can observe a lot just by looking. If he were a statistician, he might have said that
you can learn a lot just by sampling. Even though a sample is only a portion of a larger universe (population), it can teach us a lot about that pop-
Statistical Analysis
185
0
0.3
0.25
0.2
0.15
0.1
0.05
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
Box 2
Box 1
R
E
Q
U
E
N
C
Y
FIGURE 4.11
Relative frequency distributions compared.
--- page 185 ---

ulation. However, there are limits to what a sample can tell us, limits imposed by randomness.
A fundamental task of statistics is to quantify the uncertainty due to
sampling variability. This makes it possible to quantify the reliability of
statements of knowledge based on samples. Without such quantiﬁcation,
such statements are of limited value. Statistics cannot eliminate uncertainty, but it can inform us about it, and in so doing, it tempers assessments
of how much we know or how accurately we know it. Thus, statistical
analysis is a powerful antidote to the tendency to be overconﬁdent.
STATISTICAL THEORY
The box-of-beads experiments touched on many of the key ideas of statistical inference. We will now mix in some theory to extend those ideas to
the evaluation of TA rules.
The Six Elements of a Statistical
Inference Problem
Evaluating a claim that a TA rule has predictive power, that a new vaccine
can prevent illness, or any other claim of knowledge are examples of a
statistical inference problem. Generally, such problems can be reduced to
six key elements: (1) a population, (2) a sample consisting of a set of observations randomly selected from the population, (3) a population parameter, (4) a sample statistic, (5) an inference, and (6) a statement about
the reliability of the inference. Each of these elements will be discussed as
they relate to the box-of-beads experiments and then to the evaluation of
TA rules.
The Population.
A population consists of all possible observations of
a random variable. It is a large—perhaps inﬁnitely large—but a well-deﬁned
universe of observations. In the typical statistical inference problem, we
want to learn some fact about the population, but it is either impractical
or impossible to observe the population in its entirety. In the box-of-beads
experiments, the population consisted of the set of beads ﬁlling a box.
The color was the random variable. With respect to testing a TA rule, the
population consists of all conceivable daily returns13 that would be earned
by the rule’s signal over the immediate practical future.
To what does the term immediate practical future refer? It would be
unreasonable to assume that the dynamics of ﬁnancial markets are stationary, and so it would be unreasonable to expect that the proﬁtability of
186 METHODOLOGICAL, PSYCHOLOGICAL, PHILOSOPHICAL, STATISTICAL FOUNDATIONS
--- page 186 ---

a rule will endure in perpetuity. For this reason, the population with respect to TA rules cannot refer to returns occurring over an inﬁnite future.
A more reasonable notion is what I refer to as the immediate practical future. The immediate practical future refers to a ﬁnite future time period, over which it would be reasonable to expect a useful rule’s
proﬁtability to persist, even though markets are nonstationary. Any endeavor to ﬁnd predictive patterns must make some assumption about the
continuity of predictive power. In other words, unless one is willing to assume some persistence in predictive power, all forms of TA are pointless.
The assumption being made here is that a rule will continue to work long
enough to compensate the researcher for the effort of discovering it. This
is consistent with the position taken by Grossman and Stiglitz in “On the
impossibility of informationally efﬁcient markets.”14 It is also consistent
with the idea that proﬁtable rules signal opportunities to earn a risk premium,15 a topic discussed in Chapter 7.
Therefore, the immediate practical future refers to all possible random realizations of market behavior over a ﬁnite future. It is as if there
were an inﬁnite number of parallel universes, where all universes are an
exact duplicate except for the random component of the market’s behavior. In each realization, or universe, the pattern that accounts for the rule’s
proﬁtability is the same, but the random component of the market is different. This idea is illustrated in Figure 4.12.
Statistical Analysis
187
Immediate
Practical Future
Now
Historical
Sample
for Back-Testing
Infinite Number
of
Parallel Universes
$
Time
Sell
Buy
Random Realization 1
Random Realization 2
Random Realization 3
Random Realization 4
Random Realization 5
Random Realization 6
li
i
5
m
m
n
ization 3
d
n
a
R
m
n
o
a
a
FIGURE 4.12
Different realizations of randomness in an inﬁnitude of parallel
universes.
--- page 187 ---

The Sample.
The sample is a subset of the population that is available
for observation. In the box-of-beads case, we were able to observe 50 independent samples. In the case of a TA rule, we typically observe a single
sample of the rule’s performance by back testing it over a segment of market history. This sample is composed of a sequence of daily returns generated by the rule’s signals. The sequence of returns is reduced to a single
number, a sample performance statistic.
The Population Parameter.
The population parameter is a fact or
characteristic about the population that we would like to know. It is typically numerical, but it need not be.
Unfortunately, the population parameter is unknown because the entire population cannot be observed. The essence of statistical inference is
the attempt to increase our knowledge about a population parameter, despite the impossibility of observing the population in its entirety. In the
box-of-beads case, the population parameter of interest was the fraction
of grey beads in the box (i.e., F-G, and F-G 2). In the case of a TA rule, the
population parameter is the rule’s expected performance over the immediate practical future. Performance can be deﬁned in many ways. Some
common measures include average rate of return, Sharpe ratio, proﬁt factor, and so forth. In this book, our measure of performance is the annualized average daily return on detrended market (zero-centered) data.
In many statistical problems, it is safe to assume the population parameter never changes (i.e., it is a constant). In the box-of-beads experiment, the proportion of grey beads remained constant. Statistical
problems in which the population parameter remains ﬁxed are said to be
stationary.16 Now imagine a wrinkle on that situation. Suppose, unbeknownst to the experimenter, an invisible demon secretly removes or
adds grey beads between samplings. Now the population parameter, F-G,
is unstable, or nonstationary.”17
Earlier in this chapter, I said that it is best to start with an assumption
that any rule we test has no predictive power. That is, we assume that it
has an expected return equal to zero. Or, to put it in statistical terms, the
population parameter is assumed equal to be zero.
The Sample Statistic.
A sample statistic is a measurable attribute of
a sample.18 Its value is known because it has been observed. In this book,
the term sample statistic is restricted to numerical facts, for example a
proportion, a percentage, a standard deviation, an average rate of return, a
trimmed average,19 a Sharpe ratio, and so forth. In a statistical inference
problem, the sample statistic typically refers to the same measurable attribute as the population parameter. In the case of the box-of-beads, the
sample statistic, f-g, referred to the fraction of grey beads in an individual
188 METHODOLOGICAL, PSYCHOLOGICAL, PHILOSOPHICAL, STATISTICAL FOUNDATIONS
--- page 188 ---

sample. The population parameter, F-G, referred to the fraction of grey
beads in the whole box.
The bottom line is this: A sample statistic is important because it
sheds light on the population parameter. Beyond this, it is a fact of no particular importance. Some market historians seem to be unmindful of this
essential truth.
If a back test should result in a positive rate of return, it raises the following question: Is the positive performance a random deviation above
zero due to sampling variability or is it attributable to the rule’s predictive
power (i.e., the rule has an expected return greater than zero)? Answering
this question requires the tools of statistical inference. This is illustrated
in Figure 4.13.
An Inference.
Statistical inference is the inductive leap from the observed value of a sample statistic, which is known with certainty but
which is true only for a speciﬁc sample of data, to the value of a population parameter, which is uncertain but which is deemed to hold true for a
wide, perhaps inﬁnite, number of unobserved cases.
When a rule’s positive past performance can reasonably be attributed
to sampling variability, the reasonable inference is that its expected return
over the immediate practical future is zero or less. However, if the positive
performance is too high to be reasonably attributed to sampling variability
(luck), the reasonable inference would be that the rule possesses genuine
predictive power and has a positive expected return over the immediate
practical future.
Statistical Analysis
189
Date of
Earliest
Data
Date of
Most Recent
 Data
Sample Statistic
Average Return  = +10%
Expected
Return
????
Observable Past
Immediate
 Practical Future
Time
FIGURE 4.13
Is the parameter’s value greater than zero?
--- page 189 ---

A Statement about the Reliability of the Inference.
Because a
sample can not represent the population perfectly, inferences based on a
sample statistic are subject to uncertainty. In other words, it is possible
that the inference is wrong. We have already seen how sample statistics
vary randomly around the true value of the population parameter value.
The science of statistics goes beyond simply admitting that its inferences
are uncertain. It quantiﬁes their reliability. This makes statistical conclusions considerably more useful than those reached by informal methods
that do not provide such information.
The inference can be wrong in two ways. One error is concluding the
rule has predictive power when it does not. This is a case of good luck
shining on a worthless rule. This type of mistake translates into taking
market risks that will not be compensated. The other error is concluding
the rule has no predictive ability when it really does. This mistake results
in missed trading opportunities.
DESCRIPTIVE STATISTICS
The ﬁeld of statistics subdivides into two main areas: descriptive and inferential. The most important for TA is statistical inference, which was
discussed in the preceding sections. However, before making an inference, we must describe the sample data in a succinct and informative way.
The tools of descriptive statistics serve this purpose.
The goal of descriptive statistics is data reduction, that is, reducing a
large set of observed values to a smaller, more intelligible set of numbers
and plots. Descriptive statistics tell the story of the forest rather than the
individual trees. Three descriptive tools will be important for the work
that lies ahead: (1) frequency distributions, (2) measures of central tendency, and (3) measures of variation.
Frequency Distributions
Frequency distributions have already been discussed in connection with
the box-of-beads experiments. They were used to reduce a set of 50 observations on random variable f-g into an informative plot.
With only 50 observations, one might be able to form an overall impression of the data simply by looking at a table of numbers. Then again, if
the number of observations were 500 or 5,000, a table would not be as informative as a frequency distribution.
Plotting a frequency distribution is usually the ﬁrst step in analyzing a
190 METHODOLOGICAL, PSYCHOLOGICAL, PHILOSOPHICAL, STATISTICAL FOUNDATIONS
--- page 190 ---

set of data. It provides a quick visual impression of two key features of a
sample of observations: the central tendency (e.g., average value) and the
degree of dispersion or variation about the central value. For example,
Figure 4.11 showed that the two boxes of beads had different central values and different degrees of dispersion.
A visual impression of a sample is useful, but quantiﬁcation improves
matters. For our purposes, we will need to quantify two features of the
frequency distribution: its central tendency and its variability or dispersion about its central tendency.
Statistics That Measure Central Tendency
There are many measures of central tendency. Three of the most common
are the average, the median, and the mode. The average, also known as
the arithmetic mean, is used in many TA applications and is the summary
statistic used in this book. It is the sum of the observed values divided by
the number of observations.
It is important to distinguish the population mean from the sample
mean. The sample mean is a statistic, a known quantity that is computed from observed values and varies randomly from one sample to
the next. The population mean, in contrast, is unknown and does not
vary in stationary problems. The formula for the mean of a sample is
given in Figure 4.14 in two forms.
Statistical Analysis
191
x1
x2
x3
x =
+
+
+ .  .  .xn
x = Σ
i = 1x i
n
n
 Where xi is an individual observation on variable X
n
Sample Mean for Variable X
FIGURE 4.14
Sample mean for variable X.
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
