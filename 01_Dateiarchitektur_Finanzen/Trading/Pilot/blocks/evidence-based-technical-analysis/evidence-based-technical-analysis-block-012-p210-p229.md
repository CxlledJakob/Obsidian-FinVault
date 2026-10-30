# Evidence-based Technical Analysis_ Applying the Scientific Method and Statistical Inference to Trading Signals.pdf — pages 210–229

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
--- page 211 ---

There are a few points about the normal distribution that should be
understood:
• It is completely described by its mean and its standard deviation. If
these two facts are known, you know every thing that there is to know
about the distribution.
• About 68 percent of the observations lie within one standard deviation of the mean, and about 95 percent lie within two standard deviations of the mean.
• The tails of the distribution become quite thin beyond two standard
deviations. Thus values beyond three standard deviations are rare and
beyond four are extremely rare.
The normal distribution, which is illustrated in Figure 4.32, is so common that it has been called a fundamental feature of the natural world. Its
shape is caused by the additive effects of many independent factors acting
on the same situation. For example, systolic blood pressure is affected by
genetic factors, diet, weight, lifestyle, aerobic conditioning, and a multitude of other factors. When they interact, the probability distribution of
blood pressures in a large group of randomly selected people will have the
bell-shaped distribution.
Figure 4.3339 shows several very nonnormal population distributions
along with the shape of the sampling distribution of the mean. Note how
the sampling distribution converges to a normal shape as a sample size is
increased irrespective of the shape of the distribution of the data in the
212 METHODOLOGICAL, PSYCHOLOGICAL, PHILOSOPHICAL, STATISTICAL FOUNDATIONS
Mean
68% of the Area
95% of the Area
+1 σ
+2 σ
1 σ
2 σ
FIGURE 4.32
The normal distribution.
--- page 212 ---

parent population. There is nothing magical about the number 30. The rate
at which the sampling distribution converges to a normal shape as a function of sample size depends on the shape of the parent distribution. Note
that for three of the cases in the ﬁgure, a sample size of ﬁve produces a
nearly normally shaped sampling distribution of the mean. However, for
the bottom case in the ﬁgure, the sampling distribution of the mean does
not become normal-like until a sample size of 30.
The Standard Error of the Mean
We are now in a position to take the ﬁnal step toward deﬁning the sampling distribution of the mean as it is done in classical statistics. So far, it
has been established that:
1. The sampling distribution of the mean converges to the shape of a
normal distribution as the sample size is increased.
2. A normal distribution is fully described by its mean and its standard
deviation.
Statistical Analysis
213
Parent
Population
Sampling
Distribution: n=2
Sampling
Distribution: n=5
Sampling
Distribution: n=30
FIGURE 4.33
Given sufﬁcient sample size the sampling distribution of the
mean approaches normal shape irrespective of the variable’s distributional shape.
--- page 213 ---

3. The standard deviation of the sampling distribution of the mean, also
known as the standard error of the mean, is directly related to the
standard deviation of the population from which the samples were
taken.
4. The standard error of the mean is inversely related to the square root
of the sample size.
The standard error of the mean is equal to the standard deviation of
the population divided by the square root of the sample size. This is a true
statement but not of practical use because the standard deviation of the
population is not known. This is simply a consequence of the fact that the
full population is not observable. However, the standard deviation of the
population can be estimated from the sample. This estimate, which is designated by sigma-hat, is shown in equation in Figure 4.34. The little roof or
hat over the sigma is statistical symbolism for a quantity that has been estimated. You will note that the divisor within the radical sign is n – 1,
rather than n. This modiﬁcation compensates for the fact that the sample
standard deviation understates the standard deviation of the population.
This expression is used to estimate the standard deviation of the parent population, which is then used in the equation in Figure 4.35 to estimate the standard error of the mean.
With the standard error of the mean in hand, and the assumption that
the sampling distribution is normal, it is now possible to form a good esti-
214 METHODOLOGICAL, PSYCHOLOGICAL, PHILOSOPHICAL, STATISTICAL FOUNDATIONS
Σ
xi
(       ) 2

n – 1
Where:
xi
n
Is an individual observation on variable x  in the population
Is the sample mean on variable x
Is number of observations in the sample
x
x
σ  =
Estimate of Population Standard Deviation
Based on a Sample of Observations
–
FIGURE 4.34
Estimate of population standard deviation based on a sample of
observations.
--- page 214 ---

mate of the sampling distribution of the mean. And recall all this was on
the basis of a single sample.
There is one problem with the traditional approach. It assumes that
the sampling distribution is normally shaped (bell curve). If this proves
not to be so, the conclusions reached will be inaccurate. For this reason, I
have chosen to use an alternative method for estimating the sampling distribution of the mean, based on computer simulation.
DERIVING THE SAMPLING DISTRIBUTION WITH
THE COMPUTER-INTENSIVE APPROACH
Until about 30 years ago there was no alternative to the classical approach
for deriving the sampling distribution from a single sample. Now there is—
the computer-intensive approach. By systematically resampling the single
available sample many times, it is possible to approximate the shape of the
sampling distribution. This procedure is described in this section.
The next chapter will present two computer-based methods: bootstrap resampling and Monte Carlo permutation. Although each method
has its limitations, as is true for any statistical method, they are useful alternatives to the classic approach.
The bootstrap is so named because it seemingly lifts itself up, as if by
its own bootstraps, to approximate the shape of the sampling distribution. In this book, it will be used to approximate the shape of the sampling distribution of the average return for rules that have no predictive
power. The Monte Carlo permutation method is named after the famed
European gambling casino because it uses the computer as if it were a
roulette wheel.
By whatever means it is generated, the sampling distribution serves
the same purpose. It tells us how much the back-tested return of a nonpredictive rule can vary above or below zero due to the random effects of
sampling. Thus, it serves as the benchmark for evaluating rule performance. If the rule’s mean return is too high to be due to sampling variability, the rule is judged to have predictive power.
Statistical Analysis
215
n
Standard
Error
of
the Mean
=
σ
FIGURE 4.35
The standard error of the mean.
--- page 215 ---

PREVIEW OF NEXT CHAPTER
We have already made a number of references to using statistical inference
to test claims. The ofﬁcial title for this activity is hypothesis testing. The
next chapter discusses the rationale and mechanics of hypothesis testing.
It will also consider another use of statistical inference, estimating
conﬁdence intervals. A conﬁdence interval is a range that contains the
true value of the population parameter with a speciﬁed level of conﬁ-
dence. For example, if the observed mean return of a rule is 15 percent
the 95 percent conﬁdence interval might indicate that the rule’s true return lies between 5 percent return and 25 percent return. The width of the
conﬁdence interval, in this case 20 percentage points, is derived from the
same sampling distribution that is used for hypothesis testing.
216 METHODOLOGICAL, PSYCHOLOGICAL, PHILOSOPHICAL, STATISTICAL FOUNDATIONS
--- page 216 ---

Hypothesis Tests
and Conﬁdence
Intervals
TWO TYPES OF STATISTICAL INFERENCE
Statistical inference encompasses two procedures: hypothesis testing and
parameter estimation. Both are concerned with the unknown value of a
population parameter. A hypothesis test determines if a sample of data is
consistent with or contradicts a hypothesis about the value of a population parameter, for example, the hypothesis that its value is less than or
equal to zero. The other inference procedure, parameter estimation, uses
the information in a sample to determine the approximate value of a population parameter.1 Thus, a hypothesis test tells us if an effect is present or
not, whereas an estimate tells us about the size of an effect.
In some ways both forms of inference are similar. Both attempt to
draw a conclusion about an entire population based only on what has
been observed in a sample drawn from the population. In going beyond
what is known, both hypothesis testing and parameter estimation take the
inductive leap from the certain value of a sample statistic to the uncertain
value of a population parameter. As such, both are subject to error.
However, important differences distinguish parameter estimation
from hypothesis testing. Their goals are different. The hypothesis test
evaluates the veracity of a conjecture about a population parameter
leading to an acceptance or rejection of that conjecture. In contrast, estimation is aimed at providing a plausible value or range of values for
the population parameter. In this sense, estimation is a bolder endeavor
and offers potentially more useful information. Rather than merely
telling us whether we should accept or reject a speciﬁc claim such as a
--- page 217 ---

rule’s average return is less than or equal to zero, estimation approximates the average return and provides a range of values within which
the rule’s true rate of return should lie at a speciﬁed level of probability.
For example, it may tell us that the rule’s estimated return is 10 percent
and there is a 95 percent probability that it falls within the range of 5
percent to 15 percent. This statement contains two kinds of estimates; a
point estimate, that the rule’s return is 10 percent, and an interval estimate, that the return lies in the range 5 percent to 15 percent. The rule
studies discussed in Part Two use estimation as an adjunct to the hypothesis tests.
HYPOTHESIS TESTS VERSUS INFORMAL INFERENCE
If a rule has been proﬁtable in a sample of historical data, this sample statistic is an indisputable fact. However, from this fact, what can be inferred
about the rule’s future performance? Is it likely to be proﬁtable because it
possesses genuine predictive power or are proﬁts unlikely because its
past proﬁts were due to chance? The hypothesis test is a formal and rigorous inference procedure for deciding which of these alternatives is more
likely to be correct, and so can help us decide if it would be rational to use
the rule for actual trading in the future.
Conﬁrmatory Evidence: It’s Nice, It’s Necessary,
but It Ain’t Sufﬁcient
Chapter 2 pointed out that informal inference is biased in favor of conﬁrmatory evidence. That is to say, when we use common sense to test the
validity of an idea, we tend to look for conﬁrmatory evidence—facts consistent with the idea’s truth. At the same time, we tend to ignore or give
too little weight to contradictory evidence. Common sense tells us, and
rightly so, that if the idea is true, instances where the idea worked (conﬁrmatory evidence) should exist. However, informal inference makes the
mistake of assuming that conﬁrmatory evidence is sufﬁcient to establish
its truth. This is a logical error. Conﬁrmatory evidence does not compel
the conclusion that the idea is true. Because it is consistent with the idea’s
truth, it merely allows for the possibility that the idea is true.
The crucial distinction between necessary evidence and sufﬁcient evidence was illustrated in Chapter 4 with in the following example. Suppose
we wish to test the truth of the assertion: The creature I observe is a dog. We
observe that the creature has four legs (the evidence). This evidence is consistent with (i.e., conﬁrmatory of) the creature being a dog. In other words, if
218 METHODOLOGICAL, PSYCHOLOGICAL, PHILOSOPHICAL, STATISTICAL FOUNDATIONS
--- page 218 ---

the creature is a dog, then it will necessarily have four legs. However, four
legs are not sufﬁcient evidence to establish that the creature is a dog. It may
very well be another four-legged creature (cat, rhino, and so forth).
Popular articles on TA will often try to argue that a pattern has predictive power by presenting instances where the pattern made successful
predictions. It is true that, if the pattern has predictive power, then there
will be historical cases where the pattern gave successful predictions.
However, such conﬁrmatory evidence, while necessary, is not sufﬁcient to
logically establish that the pattern has predictive power. It is no more able
to compel the conclusion that the pattern has predictive power than the
presence of four legs is able to compel the conclusion that the creature
is a dog.
To argue that conﬁrmatory instances are sufﬁcient commits the fallacy of afﬁrming the consequent.
If p is true, then q is true.
q is true.
Invalid Conclusion: Therefore, p is true.
If the pattern has predictive power, then past examples of success
should exist.
Past examples of success exist, and here they are.
Therefore, the pattern has predictive power.
Chapter 3 showed that although conﬁrmatory evidence is not sufﬁ-
cient to prove the truth of an assertion, contradictory evidence—evidence
that is incompatible with an assertion’s truth—is sufﬁcient to establish
that the assertion is false. The fact that a creature lacks four legs is sufﬁ-
cient to falsify the assertion that the creature is a dog. This is the valid
form of argument called denial of the consequent.
If p is true, then q is true.
q is not true.
Therefore, p is not true (i.e., p is false).
If the creature is a dog, then the creature has four legs.
Creature does not have for legs.
Therefore, creature is not a dog.
The logical basis of the hypothesis test is falsiﬁcation of the consequent. As such, it is a potent antidote to the conﬁrmation bias of informal
inference and an effective preventative of erroneous belief.
Hypothesis Tests and Confidence Intervals
219
--- page 219 ---

What Is a Statistical Hypothesis?
A statistical hypothesis is a conjecture about the value of a population parameter. Often this is a numerical characteristic, such as the average return of a rule. The population parameter’s value is unknown because it is
unobservable. For reasons previously discussed, it is assumed to have
value equal to or less than zero.
What an observer does know is the value of a sample statistic for a
sample that has been drawn from the population. Thus, the observer is
faced with a question: Is the observed value of the sample statistic consistent with the hypothesized value of the population parameter? If the observed value is close to the hypothesized value, the reasonable inference
would be that the hypothesis is correct. If, on the other hand, the value of
the sample value is far away from the hypothesized value, the truth of the
hypothesis is called into question.
Close and far are ambiguous terms. The hypothesis test quantiﬁes
these terms making it possible to a draw a conclusion about the veracity
of the hypothesis. The test’s conclusion is typically given as a number between 0 and 1.0. This number indicates the probability that the observed
value of the sample statistic could have occurred by chance under the
condition that (given that or assuming that) the hypothesized value is
true. For example, suppose it is hypothesized that a rule’s expected return
is equal to zero, but the back test produced a return of +20 percent. The
conclusion of the hypothesis test may say something like the following: If
the rule’s expected rate of return were truly equal to zero, there is a 0.03
probability that the back-tested return could be equal to or greater than
+20 percent due to chance. Because there is only a 3 percent probability
that a 20 percent return could have occurred by chance if the rule were
truly devoid of predictive power, then we can be quite conﬁdent that the
rule was not simply lucky in the back test.
Falsifying a Hypothesis with Improbable Evidence
A hypothesis test begins by assuming that the hypothesis being tested is
true. Based on this assumption, predictions are deduced from the hypothesis about the likelihood of various new observations. In other words, if
the hypothesis is true, then certain outcomes would be probable to occur
whereas other outcomes would be improbable. Armed with this set of expectations an observer is in a position to compare the predictions with
subsequent observations. If predictions and observations agree, there is
no reason to question the hypothesis. However, if low probability outcomes are observed—outcomes that would be inconsistent with the truth
of the hypothesis—the hypothesis is deemed falsiﬁed. Thus, it is the oc-
220 METHODOLOGICAL, PSYCHOLOGICAL, PHILOSOPHICAL, STATISTICAL FOUNDATIONS
--- page 220 ---

currence of unexpected evidence that is the basis for refuting a hypothesis. Though this line of reasoning is counterintuitive, it is logically correct
(denial of the consequent) and extremely powerful. It is the logical basis
of scientiﬁc discovery.
To give a concrete example, suppose I view myself as an excellent social tennis player. My hypothesis is David Aronson is an excellent social
tennis player. I join a tennis club with members whose age and years of
play are similar to mine. On the basis of my hypothesis, I conﬁdently predict to other club members that I will win at least three-quarters of my
games (predicted win rate = 0.75). This prediction is merely a deductive
consequence of my hypothesis. I test the hypothesis by keeping track of
my ﬁrst 20 games. After 20 games I am shocked and disappointed. Not only
have I not scored a single victory (observed win rate = 0), but most losses
have been by wide margins. This outcome is clearly inconsistent with the
prediction deduced from my hypothesis. Said differently, my hypothesis
implied that this evidence had a very low probability of occurrence. Such
surprising evidence forcefully calls for a revision (falsiﬁcation) of my hypothesis. Unless I prefer feel-good delusions to observed evidence, it is
time to abandon my delusions of tennis grandeur.2
In the preceding situation, the evidence was overwhelmingly clear. I
lost every one of 20 games. However, what if the evidence had been ambiguous? Suppose I had won two-thirds of my games. An observed win
rate of 0.66 is below the predicted win rate of 0.75 but not dramatically so.
Was this merely a random negative deviation from the predicted win rate
or was the deviation of sufﬁcient magnitude to indicate the hypothesis
about my tennis ability was faulty? This is where statistical analysis becomes necessary. It attempts to answer the question: Was the difference
between the observed win rate (0.66) and the win rate predicted by my hypothesis (0.75) large enough to raise doubts about the veracity of the hypothesis? Or, alternatively: Was the difference between 0.66 and 0.75
merely random variation in that particular sample of tennis matches? The
hypothesis test attempts to distinguish prediction errors that are small
enough to be the result of random sampling from errors so large that they
indicate a faulty hypothesis.
Dueling Hypotheses: The Null Hypothesis versus
the Alternative Hypothesis
A hypothesis test relies on the method of indirect proof. That is, it establishes the truth of something by showing that something else is false. Therefore, to prove the hypothesis that we would like to demonstrate as correct,
we show that an opposing hypothesis is incorrect. To establish that hypothesis A is true, we show that the opposing hypothesis Not-A is false.
Hypothesis Tests and Confidence Intervals
221
--- page 221 ---

A hypothesis test, therefore, involves two hypotheses. One is called
the null hypothesis and the other the alternative hypothesis. The names
are strange, but they are so well entrenched that they will be used here.
The alternative hypothesis, the one the scientist would like to prove, asserts the discovery of important new knowledge. The opposing or null hypothesis simply asserts that nothing new has been discovered. For
example, Jonas Salk, inventor of the polio vaccine, put forward the alternative hypothesis that his new vaccine would prevent polio more effectively than a placebo. The null hypothesis asserted that the Salk vaccine
would not prevent polio more effectively than a placebo. For the TA rules
tested in this book, the alternative hypothesis asserts the rule has an expected return greater than zero. The null hypothesis asserts that the rule
does not have an expected return greater than zero.
For purposes of brevity, I will adopt the conventional notation: HA for
the alternative hypothesis, and H0 for the null hypothesis. A way to remember this is the null hypothesis asserts that zero new knowledge has
been discovered, thus the symbol H0.
It is crucial to the logic of a hypothesis test that HA and H0 be deﬁned
as mutually exclusive and exhaustive propositions. What does this mean?
Two propositions are said to be exhaustive if, when taken together, they
cover all possibilities. HA and H0 cover all possibilities. Either the polio
vaccine has a preventive effect or it does not. There is no other possibility.
Either a TA rule generates returns greater than zero or it does not.
The two hypotheses must also be deﬁned as mutually exclusive. Mutually exclusive propositions cannot both be true at the same time, so if H0
is shown to be false, then HA must be true and vice versa. By deﬁning the
hypotheses as exhaustive and mutually exclusive statements, if it can be
shown that one hypothesis is false, then we are left with the inescapable
222 METHODOLOGICAL, PSYCHOLOGICAL, PHILOSOPHICAL, STATISTICAL FOUNDATIONS
Alternative
Hypothesis
Rule Return
Greater Than
Zero
Null
Hypothesis
Rule Return
Less Than
Or Equal to
Zero
FIGURE 5.1
Mutually exclusive and exhaustive hypotheses.
--- page 222 ---

conclusion that the other hypothesis must be true. Proving truth in this
fashion is called the method of indirect proof. These concepts are illustrated in the Figure 5.1.
RATIONALE OF THE HYPOTHESIS TEST
Two aspects of the hypothesis test warrant explanation. First, why the
test is focused on the null hypothesis. Second, why the null hypothesis is
assumed to be true rather than the alternative hypothesis. This section explains the reasoning behind both aspects.
Why Is the Null Hypothesis the Target
of the Test?
As discussed in Chapter 3, evidence can be used to logically deduce that
a hypothesis is false, but it cannot be used to deduce that it is true.3
Therefore, hypothesis testing must be about trying to falsify something.
The question is: Which of the hypotheses, H0 or HA, should be the target
of this effort?
Of the two competing claims, H0 presents a better target for falsiﬁcation because it can be reduced to a single claim about the value of the parameter. This means that only one test must be performed. If that single
value can be successfully challenged with evidence, H0 will have been falsiﬁed. In contrast, the alternative hypothesis represents an inﬁnite number of claims about the parameter’s value. With no unique value to shoot
at, an inﬁnite number of tests would have to be performed to falsify the alternative hypothesis.
In fact, both H0 and HA represent an inﬁnite number of claims about
the rule’s expected return, but H0 can be reduced to a single claim. First,
let’s consider why HA represents an inﬁnite number of claims. In asserting that the rule’s return is greater than zero, HA effectively says that the
rule’s expected return, over the immediate practical future, might be any
one of an inﬁnite set of values greater than zero: + 0.1 percent, or +2 percent or +6 percent or any other positive value. This is illustrated in Figure
5.2. Given that HA makes an inﬁnite number of claims, an inﬁnite number
of tests would have to be conducted to conclusively refute it. Clearly this
is impractical.
H0 also makes an inﬁnite number of claims about the value of
the population parameter. It asserts that the rule’s average return is
equal to zero or some value less than zero. However, only one of these
claims really matters—that the rule’s average return is equal to zero.
Hypothesis Tests and Confidence Intervals
223
--- page 223 ---

The attempt to falsify a single claim is a practical goal. If the most positive of these claims (return = 0) can be called into question by the rule’s
back-test proﬁtability, then all lesser claims (e.g., the rule’s return = –1.3
percent) are contradicted but to an even greater degree. This is how H0
reduces to the single claim that the rule’s return is zero. This is illustrated in Figure 5.3.
224 METHODOLOGICAL, PSYCHOLOGICAL, PHILOSOPHICAL, STATISTICAL FOUNDATIONS
0
Positive Returns
Negative Returns
+.01% +2 +4 +6 +8 +10
+12%
H1 Asserts:
Rule’s Expected Return > 0%.
Etc.
FIGURE 5.2
The alternative hypothesis makes an inﬁnite number of claims
about the rule’s expected rate of return.
0
Positive Returns
Negative Returns
0%
-2
-4
-6
-8
-10
-12%
H0 Asserts:
Rule’s Return < or = 0%.
Etc.
FIGURE 5.3
The null hypothesis makes an inﬁnite number of claims about the
population mean, but only one matters.
--- page 224 ---

Why Is the Null Hypothesis Assumed to Be True?
The hypothesis test assumes H0 is true on two grounds: scientiﬁc skepticism and the principle of simplicity (parsimony).
Skepticism.
The assumption that H0 is true is consistent with science’s
skeptical attitude toward all new claims of knowledge. As explained in
Chapter 3, this conservative stance is justiﬁed because making claims is
easy but making genuine discoveries is hard. The burden of proof should
be on the claimant.
Science has a legitimate concern with protecting the storehouse of
knowledge from contamination with falsehoods and weird beliefs. A useful analogy can be made to the criminal justice system. Free societies
have a legitimate concern with protecting the lone citizen from the vast
prosecutorial power of the state. For this reason the defendant in a criminal prosecution starts off with a presumption of innocence. This places
the burden of proving guilt—falsifying the assumption of innocence—on
the state, and it is indeed a substantial burden. To gain a conviction, the
state must provide evidence of guilt beyond a reasonable doubt, a very
high threshold. The initial assumption of innocence and the high threshold of proof can be seen as the legal system’s way of preventing the jails
and gallows from being contaminated with innocent citizens.
Following the scientiﬁc tradition, the hypothesis test places the burden of proof on those asserting new knowledge. In fact, whenever the
back-tested performance of a rule is greater than zero, the sample evidence actually favors HA—that the rule’s expected return is greater than
zero. However, the hypothesis test demands more than merely reasonable
evidence. It demands compelling evidence before abandoning the assumed truth of H0. Those asserting that a TA rule has predictive power
(HA) must meet a large burden of proof before they can reasonably expect
their claim to be accepted by scientiﬁc practitioners of TA.
Simplicity.
An additional reason to grant priority to H0 is the principle
of simplicity. This fundamental precept of science says that simpler theories are more likely to capture the true patterns of nature than more elaborate ones. This principle, known as Occam’s Razor, says that if a
phenomenon can be explained by more than one hypothesis, then the simplest hypothesis is more likely to be correct. H0, which explains a rule’s
past success as luck, is simpler than HA, which asserts that proﬁts stem
from a recurring market pattern with predictive power.
Simpler explanations (theories, rules, hypotheses, models, and so
forth) are more likely to be correct because they are less likely to ﬁt data
by chance. The more complex an explanation—that is, the more numerous
Hypothesis Tests and Confidence Intervals
225
--- page 225 ---

its assumptions, its conditions, and constraints—the more likely it is to ﬁt
a set of observations by chance. This is illustrated when ﬁtting a mathematical function to a set of data. A function can be thought of as a mathematical hypothesis that explains a given set of observations. In Figure 5.4,
two mathematical functions have been ﬁtted to the same set of data. One
function is linear. It is relatively simple in that it is deﬁned by only two coefﬁcients or degrees of freedom: its slope and where it cuts the vertical
axis (Y-intercept). In other words, the line’s ﬁt to the data can be improved by manipulating only these two factors.
The other function is a complex polynomial with 10 coefﬁcients.
Each coefﬁcient allows the curve to make an additional bend. With this
degree of ﬂexibility, the curve can weave and bend so that it touches
every data point. In fact, when a function is ﬁt to data using a method
called least-squares regression, a perfect ﬁt is guaranteed if the function
is allowed to contain as many degrees of freedom (coefﬁcients) as there
are data points. Although the linear function does not manage to touch
every observed point, it does describe the general tendency of the data;
increasing values of X are associated with increasing values of Y. In other
words, the simple function captures the essential feature of the data,
making it more likely that it represents the real relationship between X
and Y. In contrast, the complex function is most likely a detailed description of the data’s random ﬂuctuations in addition to the positive correlation between X and Y.
226 METHODOLOGICAL, PSYCHOLOGICAL, PHILOSOPHICAL, STATISTICAL FOUNDATIONS
X
Y
FIGURE 5.4
The superiority of simplicity—all else being equal.
--- page 226 ---

This is not to suggest that complex curves are never justiﬁed. If there
is enough data and it was generated by a complex process, an elaborate
model may very well be justiﬁed. However, all else being equal, the simpler explanation is more likely to be correct.
Strong and Weak Decisions
A hypothesis test leads to one of two decisions; reject H0 or retain H0. The
decisions are qualitatively different: the ﬁrst is a strong decision while the
second is a weak one.4 Rejection is a strong decision because it is compelled by improbable, informative evidence that forcefully contradicts H0.
In contrast, the decision to retain H0 is a relatively weaker choice because
the evidence is nothing more than consistent with what we had already
expected and assumed to be so, that H0 is true. In others words, the observed value of the test statistic is unsurprising and hence uninformative.
Had tests of Salk’s polio vaccine shown that recipients of the real vaccine had the same risk of getting the disease as recipients of the placebo,
H0 would be left intact, and no one would have been surprised by the vaccine’s failure. Nothing had worked up to that point, so it would have been
just another frustrating day at the lab. Of course this is not what actually
happened, and the course of medical history was changed. Salk’s decision
to reject H0 was compelled by a rate of infection in the treated group that
was surprisingly less than the placebo group.
It is in this way that a decision to reject H0 is fundamentally a stronger
decision than one to retain H0. It is a decision forced by evidence that is
strong enough to rebut an initial and entirely reasonable doubt that new
knowledge has been discovered. In contrast, the decision to retain H0 is
due to an absence of compelling evidence. The absence of compelling evidence does not mean the null is necessarily true or even probably true.5 It
simply means that it could be true. Because science takes a conservative
stance toward new knowledge, in the absence of compelling evidence, the
more reasonable conclusion is that nothing new has been discovered.
HYPOTHESIS TESTING: THE MECHANICS
“Three ingredients are usually necessary for a hypothesis test: (1) a hypothesis, (2) a test statistic, and (3) some means of generating the probability distribution (sampling distribution) of the test statistic under the
assumption that the hypothesis is true.”6 The term test statistic refers to
the sample statistic that is being used to test a hypothesis. Thus, the terms
are interchangeable.
Hypothesis Tests and Confidence Intervals
227
--- page 227 ---

To recap these items as they pertain to rule testing: (1) the hypothesis
H0 is that the rule has an expected return of zero or less, (2) the test statistic is the rule’s mean return obtained by back testing it in a historical sample of data, and (3) the sampling distribution represents the random
variation in the rule’s mean return if it were to be tested in many independent samples. The sampling distribution is centered at a mean return of
zero, reﬂecting the assumption asserted by H0.
As discussed in Chapter 4, the sampling distribution can be derived in
two ways: the analytical approach of classical statistics and via computer
simulation. There are two computer-based approaches: Monte-Carlo permutation and the bootstrap. Both will be used in the case study presented
in Part Two.
The Question: Is the Test Statistic Improbable?
The basic idea of a hypothesis test is simple: an outcome (observation)
that would rarely happen under the condition that the hypothesis were
true is good evidence that the hypothesis is not true.”7 If my hypothesis
that I am a good tennis player were true, then it would be rare (improbable) for me to lose 20 games in a row. To my surprise and embarrassment I
did lose 20 games in a row. That evidence implies my hypothesis is false.
Suppose a TA rule called MA50 is back tested. The MA50 rule is de-
ﬁned as follows: If S&P 500 close is greater than a 50-day moving average,
hold a long position in the S&P 500, otherwise hold a short position. The
alternative hypothesis (HA) asserts that the rule has predictive power and
is, therefore, expected to earn a rate of return greater than zero on detrended data.8 Zero is the rate of return expected for a rule with no predictive power. The null hypothesis (H0) asserts that the MA50’s expected
return is equal to zero or less. H0’s assertion is depicted in Figure 5.5.
228 METHODOLOGICAL, PSYCHOLOGICAL, PHILOSOPHICAL, STATISTICAL FOUNDATIONS
0
Positive Returns
Negative Returns
Value of the Population Parameter
Asserted by H0
FIGURE 5.5
Value of population parameter asserted by H0.
--- page 228 ---

The horizontal axis represents expected return over the immediate practical future.
MA50’s mean return is obtained by back testing the rule in a sample of
historical data. When this value is plotted on the same axis as the hypothesized value for population parameter, we get Figure 5.6.
Note that in Figure 5.6 there is a positive deviation between the value
predicted by H0 and the performance of the rule obtained in the back test.
This raises the question: Is the positive deviation so surprising that H0
should be rejected as an implausible hypothesis?
There are two possible explanations for the positive deviation. It
could simply be due to sampling error—the rule got lucky in the particular
sample of data used for back-testing—or, it could be because the hypothesized value of zero is wrong—the rule does have predictive power and its
expected return is indeed greater than zero. The objective of the hypothesis test is to determine if the evidence, speciﬁcally the size of positive deviation, is sufﬁciently rare, surprising, or improbable that it would warrant
a rejection of H0.
To assess the improbability of the evidence, the observed average
return, in particular its deviation from the hypothesized value, is evaluated in light of the sampling distribution. Recall, the sampling gives the
probability for various sized deviations between the observed value of
the sample statistic and its expected value due to sampling error. If the
observed value’s deviation is greater than what could reasonably be attributed to sampling error, then H0 is rejected and the alternative hypothesis, HA, is adopted. In other words, we conclude that the rule has
predictive power.
Figure 5.7 gives us an intuitive sense of the values of the sample statistic
Hypothesis Tests and Confidence Intervals
229
0
Positive Returns
Deviation
Negative Returns
Value of the Population  Parameter
Asserted by H0
Sample Statistic
Back-Tested
Performance
of the rule
FIGURE 5.6
Hypothesized value of population parameter compared to backtested performance.
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
