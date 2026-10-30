# Evidence-based Technical Analysis_ Applying the Scientific Method and Statistical Inference to Trading Signals.pdf — pages 248–267

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
--- page 249 ---

method has nothing to do with estimating the value of a population parameter or testing a claim made about its value. As previously mentioned,
the Monte Carlo permutation method tests a claim about the information
content of the rule’s signals. Speciﬁcally, the H0 asserted under the Monte
Carlo permutation method is that the long and short positions dictated by
the rule are devoid of useful information about future market changes. Because there is no reference to a population parameter (e.g., mean rule return) there is nothing to create a conﬁdence interval for!
The bootstrap percentile procedure for constructing the conﬁdence
intervals works as follows: Suppose the rule’s returns have been resampled 5,000 times and a mean is computed for each resample. This would
result in 5,000 different values for the resampled mean return. We know
that because of sampling variability, these means will differ. Next suppose
that the set of 5,000 values is arranged in rank order from highest mean to
lowest. Then, depending on the conﬁdence interval desired, the highest x
percent and lowest >x percent of values are removed from the ordered
list, where
So if a 90 percent conﬁdence interval is desired, one would remove
the highest 5 percent and the lowest 5 percent of the values in the 5,000 resampled means. This would require removing the highest 250 and the 250
lowest values of the resampled mean. After these extreme values are removed, the highest remaining resampled mean would be the upper bound
of the 90 percent conﬁdence interval and the lowest remaining resampled
mean is the lower bound.The 99 percent conﬁdence interval would result
by removing only the highest 25 (top .5 percent) and the lowest 25 (bottom .5 percent) from the set of 5,000 resampled means comprising the
sampling distribution.
Hypothesis Tests versus Conﬁdence Intervals: Potential Con-
ﬂict.
Some astute readers may have envisioned a problem. It is possible
for a hypothesis test and a conﬁdence interval to lead to different conclusions about a rule’s expected return. This prospect stems from the fact
that a hypothesis test focuses on the right tail of the sampling distribution
whereas the conﬁdence interval focuses on the left tail of the sampling
distribution. This means it is possible for the lower bound of a 90 percent
conﬁdence interval to imply that there is a 5 percent probability that a
rule’s expected return is less than zero, while a hypothesis test conducted
at the .05 signiﬁcance level rejects H0. In other words, it is possible for the
X =
−
100
Confidence Interval Desired
2
250 METHODOLOGICAL, PSYCHOLOGICAL, PHILOSOPHICAL, STATISTICAL FOUNDATIONS
--- page 250 ---

conﬁdence interval to tell us that the rule does not have predictive power
while the hypothesis tells us that it does. In theory, the hypothesis test
and the conﬁdence interval should come to the same conclusion on this
issue. That is to say, if the lower bound of a 90 percent conﬁdence interval tells us that the rule’s expected return is less than 0 percent, then a
hypothesis test at the .05 signiﬁcance level would presumably not reject
the null hypothesis.
Conﬂicting conclusions can arise when the sampling distribution is
not symmetrical (i.e., is skewed to the right or left). This is illustrated in
Figure 5.22. The sampling distribution, which is clearly skewed to the left,
is shown in two positions. In the lower portion of Figure 5.22, the sampling distribution is positioned as it would be for conducting a test of H0.
Because less than 5 percent of the sampling distribution’s right tail lies
above the mean return of the back-tested rule, the test indicates the rule is
signiﬁcant at the .05 level. In other words, H0 can be rejected in favor of
the alternative hypothesis, HA, that claims the rule has an expected return
that is greater than zero.
The upper portion of Figure 5.22 shows the sampling distribution as
it would be positioned to construct a 90 percent conﬁdence interval using the bootstrap percentile method. Note that the lower bound of the
conﬁdence interval is below a zero rate of return. This tells us there is
greater than a .05 probability that the rule’s true rate of return is less
than zero. In other words, the 90 percent conﬁdence interval leads to a
conclusion that is opposite to the conclusion of the hypothesis test. The
Hypothesis Tests and Confidence Intervals
251
0
10
Sampling
Distribution
Positioned for
Test of
Null Hypothesis
Sampling Distribution
Positioned for
Confidence Interval
Mean Back-Test Return
Historical Sample
90% CI
Less than .05
of Sampling Distribution
Above Mean Return
Lower Bound
90% Confidence
Interval Below 0
0
Null
Hypothesis
FIGURE 5.22
Potentially conﬂicting conclusions: hypothesis test versus conﬁ-
dence interval.
--- page 251 ---

ﬁgure shows that the ambiguity is due to the asymmetrical shape of the
sampling distribution.
Fortunately this problem does not afﬂict the research conducted in
this book, which uses the sample mean as a performance statistic. The
all-important Central Limit Theorem assures us that the sampling distribution of the mean will not be seriously skewed (asymmetrical) as long
as the sample size is large. To recap, the Central Limit Theorem tells us
that, as sample size increases, the sampling distribution of the mean
tends toward a symmetrical bell shape. Other performance statistics
may not behave this way. In situations where the sampling distribution
is not symmetrical, there are bootstrap techniques, which involve pivoting the sampling distribution to alleviate this problem. Unfortunately,
these other methods can have problems of their own. In any case, this
all makes the mean return an attractive performance statistic to use in
rule testing.
Conﬁdence Intervals for the TT-4-91 Rule.
This section gives an
example of the conﬁdence interval for the rule TT-4-91. Figure 5.23 shows
the 80 percent conﬁdence interval superimposed on the bootstrapped
252 METHODOLOGICAL, PSYCHOLOGICAL, PHILOSOPHICAL, STATISTICAL FOUNDATIONS
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
80%
FIGURE 5.23
Sampling distribution and 80 percent conﬁdence interval for
rule TT-4-91.
--- page 252 ---

sampling distribution positioned at the rule’s observed back-tested return
of +4.84 percent. The lower bound of the 80 percent conﬁdence interval is
+0.62 percent. The upper bound is +9.06 percent. This tells us that if rule
TT-4-91 were to be back tested on 100 independent samples of data and an
80 percent conﬁdence interval were to be placed around the mean return
in each sample, in approximately 80 of the samples, the true expected return of the rule would be enclosed by the conﬁdence interval.
Hypothesis Tests and Confidence Intervals
253
--- page 253 ---

Data-Mining
Bias: The Fool’s
Gold of
Objective TA
I
n rule data mining, many rules are back tested and the rule with the best
observed performance is selected. That is to say, data mining involves a
performance competition that leads to a winning rule being picked. The
problem is that the winning rule’s observed performance that allowed it to
be picked over all other rules systematically overstates how well the rule is
likely to perform in the future. This systematic error is the data-mining bias.
Despite this problem, data mining is a useful research approach. It
can be proven mathematically that, out of all the rules tested, the rule
with the highest observed performance is the rule most likely to do the
best in the future, provided a sufﬁcient number of observations are used
to compute performance statistics.1 In other words, it pays to data mine
even though the best rule’s observed performance is positively biased.
This chapter explains why the bias occurs, why it must be taken into account when making inferences about the future performance of the best
rule, and how such inferences can be made.
I begin by introducing this somewhat abstract topic with several anecdotes, only one of which is related to rule data mining. They are appetizers
intended to make later material more digestible. Readers who want to start
on the main course immediately may choose to skip to the section titled
“Data Mining.”
The following deﬁnitions will be used throughout this chapter and are
placed here for the convenience of the reader.
• Expected performance: the expected return of a rule in the immediate practical future. This can also be called the true performance of
the rule, which is attributable to its legitimate predictive power.
--- page 254 ---

• Observed performance: the rate of return earned by a rule in a back
test.
• Data-mining bias: the expected difference between the observed
performance of the best rule and its expected performance. Expected
difference refers to a long-run average difference that would be obtained by numerous experiments that measure the difference between the observed return of the best rule and the expected return of
the best rule.
• Data mining: the process of looking for patterns, models, predictive
rules, and so forth in large statistical databases.
• Best rule: the rule with the best observed performance when many
rules are back tested and their performances are compared.
• In-sample data: the data used for data mining (i.e., rule back testing).
• Out-of-sample data: data not used in the data mining or back-testing
process.
• Rule universe: the full set of rules back tested in a data mining
venture.
• Universe size: the number of rules comprising the rule universe.
FALLING INTO THE PIT: TALES OF THE
DATA-MINING BIAS
This following account is apocryphal. Some years ago, before I took up
the study of statistics, I was approached by an impresario seeking backers
for a show business venture that he claimed would be enormously profitable. The show was to feature a monkey that could write Shakespearian
prose by dancing on the keyboard of a word processor.
At each show, the literate monkey, whom the promoter had named the
Bard, would be placed at a keyboard and a large screen would display to
an audience what the monkey wrote, as it was being written. Surely, people would rush to see the Bard, and my share of ticket sales would yield a
handsome return on the required investment of $50,000. At least, that was
the promoter’s claim. “It can’t miss!” was his refrain.
I was intrigued, but wanted some proof that the monkey could actually produce Shakespearian prose. Any investor would. I was given proof
. . . of a sort. It was what accountants call a cold-comfort letter. The letter
said, “We have examined the Bard’s previous works and he has in fact
written the words ‘To be or not to be, that is the question.’ We are, however, unfamiliar with the circumstances under which these words were
written.”
What I really wanted was a live demonstration. Regrettably, my
256 METHODOLOGICAL, PSYCHOLOGICAL, PHILOSOPHICAL, STATISTICAL FOUNDATIONS
--- page 255 ---

request could not be accommodated. The impatient promoter explained
the monkey was temperamental and besides, there were many other
anxious investors clamoring to buy the limited number of shares being
offered. So I seized the opportunity and plunked down $50,000. I was
conﬁdent it was just a matter of time before the proﬁts would start
ﬂowing in.
The night of the ﬁrst show arrived. Carnegie Hall was packed to capacity with a crowd that anxiously awaited the ﬁrst words. With everyone’s eyes glued to the big screen, the Bard’s ﬁrst line of text appeared.
lkas1dlk5jf wo44iuldjs sk0ek 123pwkdzsdidip’adipjasdopiksd
Things went downhill quickly from there. The audience began
screaming for refunds, I threw up, and the Bard defecated on the keyboard before scampering off the stage. My investment went up in a cloud
of smoke.
What happened? Thinking it unimportant, the promoter failed to
disclose a key fact. The Bard had been chosen from 1,125,385 other
monkeys, all of whom had been given the opportunity to dance on a
keyboard every day for the past 11 years, 4 months, and 5 days. A computer monitored all their gibberish to ﬂag any sequence of letters that
matched anything ever written by Shakespeare. The Bard was the ﬁrst
monkey to ever do so.
Even in my state of statistical illiteracy, I doubt I would have invested
had I known this. Mere common sense would have told me that chance
alone favored the occurrence of some Shakespearian quote in such a
large mass of nonsense. The freedom to data mine the trillions of letters
generated by an army of monkeys raised the probability of a lucky sequence of letters to a virtual certainty. The Bard was not literate, he was
just lucky.
The fault, Dear Brutus, lay with the sincere but statistically naïve
promoter. He was deluded by the data-mining bias and attributed too
much signiﬁcance to a result obtained by data mining. Despite my loss,
I’ve tried not to judge the promoter too harshly. He sincerely believed
that he had found a truly remarkable monkey. He was simply misled by
intuition, a faculty inadequate for evaluating matters statistical and
probabilistic.
By the way, the promoter has kept the Bard as a pet and still allows
him to dance on that once-magical keyboard in hopes of new evidence of
literacy. In the meanwhile, to keep body and soul together, he is now selling technical trading systems developed along similar lines. He has a
throng of dancing monkeys developing rules, some of which seem to work
quite well, in the historical data.
Data-Mining Bias: The Fool’s Gold of Objective TA
257
--- page 256 ---

Proving the Existence of God with Baseball Stats
Collectors of sports statistics have also been seduced by the data-mining
bias. For example, there is Norman Bloom, who concluded that interesting and unusual patterns found in baseball statistics prove the existence
of God. After thousands of searches through his database, the dedicated
data miner found patterns he believed to be so amazing they could only be
explained by a universe made orderly by God.
One of Bloom’s patterns was as follows: George Brett, the third baseman for Kansas City, hit his third home run in the third game of the playoffs, to tie the score 3-3. Bloom reasoned that, for the number three to be
connected in so many ways, compelled the conclusion it was the handiwork of God. Another interesting pattern discovered by Bloom had to do
with the stock market: The Dow Jones Industrial Average crossed the
1,000 level 13 times in 1976, miraculously similar to the fact that there
were 13 original colonies that united in 1776 to form the United States.
As pointed out by Ronald Kahn,2 Bloom committed several errors on
the way to his unjustiﬁed conclusions. First, he did not understand the
role of randomness and that seemingly rare coincidences are in fact quite
probable if one searches enough. Bloom found his mystical patterns by
evaluating thousands of possible attribute combinations. Second, Bloom
did not specify what constituted an important pattern before he began his
searches. Instead, he took the liberty of using an arbitrary criterion of importance deﬁned after the fact. Whatever struck his fancy as interesting
and unusual was deemed to be important. Kahn points out that one is
guaranteed to discover “interesting” patterns when they are searched for
in such an undisciplined manner.
Discovering Hidden Predictions in
the Old Testament
Even Bible scholars have fallen into the data mining pit. In this instance,
the well intentioned but statistically unsophisticated researchers found
predictions of major world events encoded in the text of the Old Testament. Knowledge of the future would certainly imply that the words had
been inspired by an omniscient Creator. However, there was one small
problem with these predictions, known as Bible Codes. They were always
discovered after the predicted event had taken place. In other words, the
codes predict with 20/20 hindsight.3
The Bible Codes are clusters of words imbedded in the text that are
discovered by linking together letters separated by a speciﬁc number of
intervening spaces or other letters. These constructed words are referred
to as equal letter sequences or ELS. Code researchers grant themselves
258 METHODOLOGICAL, PSYCHOLOGICAL, PHILOSOPHICAL, STATISTICAL FOUNDATIONS
--- page 257 ---

the freedom to try any spacing interval they wish and allow the words
comprising the cluster to be arranged in virtually any conﬁguration so
long as the cluster occurs in what the researcher deems4 to be a compact
region of the original text. What constitutes a compact region and what
words constitute a prediction are always deﬁned after a code has been
discovered. Note the use of an evaluation criterion deﬁned after the fact.
This is not scientiﬁcally kosher.
The Bible Code scholars contend that the occurrence of a code is so
statistically unlikely that it can only be explained by its having been put
there by God. Their fundamental error—the error made by all naive data
miners—is the failure to understand that given enough searching (data
mining), the occurrence of such patterns is actually highly probable. Thus,
it is likely that researchers will ﬁnd codes that correspond to names,
places, and events of historical importance. For example, the word 1990
in the same region of text as Saddam Hussein and war are not rare
events requiring a metaphysical explanation. However, when found in
1992, after the ﬁrst Iraq war had taken place, the word pattern seemingly
predicted the 1990 Iraq war. Bear in mind that the words Bush, Iraq, invasion, and desert storm would serve just as nicely as a code that also appears to predict the 1990 Iraq war. Indeed, there are a huge number of
word combinations that would correspond to the 1990 war, after the particulars of that historical event are known.
In his 1997 book, The Bible Code, author Michael Drosnin, a journalist
with no formal training in statistics, describes the research of Dr. Eliyahu
Rips. Dr. Rips is an expert in the mathematics of group theory, a branch
of mathematics that is not particularly relevant to the problem of datamining bias. Though Drosnin claims that the Bible Codes have been endorsed by a roster of famous mathematicians, 45 statisticians who
reviewed Rips’s work found it to be totally unconvincing.5 Data-mining
bias is, at its heart, a problem of faulty statistical inference.
Statisticians take a dim view of the unconstrained searching practiced by Bible Code researchers. It commits a mathematical sin called the
excessive burning of degrees of freedom. To the statistical sophisticate,
the stench produced by this incineration is most foul. As pointed out by
Dr. Barry Simon, “A Skeptical Look at the Torah Codes,”6 in Chumash,
just one of the 14 books comprising the Torah, approximately 3 billion
possible words can be produced from the existing text when the ELS
spacing interval is allowed to vary from 1 to 5,000. Searching this set of
manufactured words for interesting conﬁgurations is no different than
searching through tons of gibberish written by an army of monkeys dancing on keyboards.
The foolishness of the Bible Code scholars’ search algorithms becomes apparent when they are applied to non-Biblical texts of similar
Data-Mining Bias: The Fool’s Gold of Objective TA
259
--- page 258 ---

length, such as the Sears catalogue, Moby Dick, Tolstoy’s War and Peace,
or the Chicago telephone directory. When these texts are searched, coded
after the fact predictions of historical events are also found. This suggests
the codes are a by-product of the search method and not of the text being
searched.
In a more recent book by Drosnin, The Bible Code II: The Countdown, he shows how the codes “predicted” the terrible events of 9/11/01.
Why, you ask, didn’t he warn us before the events happened? He did not
because he could not. He discovered the predictions after the tragedy occurred. Drosnin is another example of a well-intentioned but naïve researcher fooled by the data-mining bias.
Data-Mining Newspaper Reporters
Newspaper reporters have also been duped by the data-mining bias. In the
mid 1980s, they reported the story of Evelyn Adams, who had won the
New Jersey state lottery twice in four months.7 Newspaper accounts put
the probability of such an occurrence at 1 in 17 trillion. In fact, the probability of ﬁnding a double winner was far higher and the story far less
newsworthy than the reporters had thought.
The before-the-fact (a priori) probability that Ms. Adams or any other
individual will win the lottery winner twice is indeed 17 trillion to one.
However, the after-the-fact probability of ﬁnding someone who has already won twice by searching the entire universe of all lottery players is
far higher. Harvard statisticians Percy Diaconis and Frederick Mosteller
estimated the probability to be about 1 in 30.
The qualiﬁer after-the-fact is the key. It refers to a perusal of data after
outcomes are known. Just as the probability that any individual monkey
will in the future produce a Shakespearian quote is extremely small, the
probability that there exists some monkey, among millions of monkeys,
that has already produced some literate prose, is substantially higher.
Given enough opportunity, randomness produces some extraordinary outcomes. The seemingly rare is actually quite likely.
Mining the UN Database for Gold
and Finding Butter
David J. Leinweber, on the faculty of California Institute of Technology
and formerly a managing partner at First Quandrant, a quantitative pension management company, has warned ﬁnancial market researchers
about the data-mining bias. To illustrate the pitfalls of excessive searching, he tested several hundred economic time series in a UN database to
260 METHODOLOGICAL, PSYCHOLOGICAL, PHILOSOPHICAL, STATISTICAL FOUNDATIONS
--- page 259 ---

ﬁnd the one with the highest predictive correlation to the S&P 500. It
turned out to be the level of butter production in Bangladesh, with a correlation of about 0.70, an unusually high correlation in the domain of economic forecasting.
Intuition alone would tell us a high correlation between Bangladesh
butter and the S&P 500 is specious, but now imagine if the time series
with the highest correlation had a plausible connection to the S&P 500.
Intuition would not warn us. As Leinweber points out, when the total
number of time series examined is taken into account, the correlation
between Bangladesh butter and the S&P 500 Index is not statistically
signiﬁcant.
The bottom line: whether one searches sport statistics, the Bible, the
random writings of monkeys, the universe of lottery players, or ﬁnancial
market history, data mining can lead to false conclusions if the data mining bias is not taken into account.
THE PROBLEM OF ERRONEOUS KNOWLEDGE
IN OBJECTIVE TECHNICAL ANALYSIS
TA is comprised of two mutually exclusive domains—subjective and objective. To recap, objective TA is conﬁned to methods that are sufﬁciently
well deﬁned that they can be reduced to a computerized algorithm and
back tested. Everything else is, by default, subjective TA.
Both domains are contaminated with erroneous knowledge, but the
falsehoods are of very different types. The loosely deﬁned propositions
of subjective TA carry no cognitive freight, generate no testable predictions,8 and are, therefore, shielded from empirical challenge. Without
this crucial procedure for excising worthless ideas, falsehoods accumulate. As a result, subjective TA is not a legitimate body of knowledge but
a collection of folklore resting on a ﬂimsy foundation of anecdote and
intuition.
Objective TA methods have the potential to be valid knowledge but
only if back-test results are considered in light of randomness (sampling variability) and data-mining bias. Because many objective practitioners are unaware of these effects, falsehoods accumulate in this
domain as well.
Erroneous objective TA manifests as out-of-sample9 performance deterioration—a rule that performs well in the sample used for back testing
but then performs worse in out-of-sample data. This problem is illustrated
in Figure 6.1.
Data-Mining Bias: The Fool’s Gold of Objective TA
261
--- page 260 ---

Explanations for Out-of-Sample Deterioration:
Old and New
Out-of-sample performance deterioration is a well-known problem.10 Objective technicians have proposed a number of explanations. I propose a
relatively new one, based on data-mining bias.
The least plausible explanation attributes the problem to random variation. Although it is true that a rule’s performance will vary from one sample of history to another due to sampling variability, this explanation does
not even ﬁt the evidence. If random variation were responsible, then outof-sample performance would be higher than in-sample performance
about as frequently as it is lower. Anyone experienced with back testing
knows that out-of-sample performance is inferior far more often.
A second rationale is that the market’s dynamics changed when the
out-of-sample period began. It is reasonable to assume that ﬁnancial
markets are nonstationary systems.11 However, it is not reasonable to
assume that each time a rule fails out of sample it is because market dynamics have changed. It would be odd, almost ﬁendish, for the market
to always change its ways just when a rule moves from the technician’s
laboratory to the real world of trading. It is simply implausible to suggest that a market’s dynamics change as frequently as rules fail out of
sample.
An even more elaborate explanation, also based on changing market
dynamics, invokes the additional assumption that the change occurred because the rule has been adopted by too many traders. This story asserts
that the buying and selling of the traders using the rule has destroyed the
262 METHODOLOGICAL, PSYCHOLOGICAL, PHILOSOPHICAL, STATISTICAL FOUNDATIONS
Time
$
Cumulative
Gains
 In-Sample
Out-of-sample
Observed
Performance
50%. ROI
FIGURE 6.1
Out-of-sample performance deterioration.
--- page 261 ---

market pattern that accounted for the rule’s back-test proﬁtability. This rationale also lacks plausibility. Given that there are an almost inﬁnite number of rules that could be formulated, it would be unlikely that a large
enough number of participants would adopt any particular rule. Even
when numerous traders adopt similar rules, as is the case with futures
trading funds that employ objective trend-following methods, reduced
rule performance seems to be due to changes in market volatility that are
not related to the usage of technical systems.12
A more plausible explanation13 of out-of-sample performance breakdown is based on randomness. It asserts that market dynamics are a combination of systematic or patterned behavior and randomness or noise.
Valid rules exploit the market’s systematic features. Because the systematic component should continue to manifest in out-of-sample data, it is a
dependable source of rule proﬁts. In contrast, the random component is a
nonrecurring phenomenon that will manifest differently in each sample of
data. It is reasoned that a portion of a rule’s in-sample performance was
luck—a coincidental correspondence between the rule’s signals and the
market’s nonrecurring noise. These lucky proﬁts will not manifest out of
sample, and so future performance will fall below past performance. This
explanation is closer to the mark, but it is incomplete. Randomness is only
one villain.
A more complete account of out-of-sample performance deterioration
is based on the data-mining bias. It names two villains: (1) randomness,
which is a relatively large component of observed performance and (2)
the logic of data mining, in which a best-performing rule is selected after
the back-tested performances of all tested rules are available for the data
miner’s examination. When these two effects combine, they cause the observed performance of the best rule to overstate its future (expected) performance. Thus, it is likely that the best rule’s future performance will be
worse than the level of performance that caused it to be selected from the
universe of rules tested.
The data-mining bias explanation for out-of-sample performance
deterioration is superior to the one based on changed market dynamics.
Both explanations ﬁt the data in the sense that they are both consistent
with the fact that out-of-sample performance tends to be worse. However, the latter explanation invokes the assumption that market dynamics have changed. The data-mining bias explanation does not. It simply
says that the process of data mining favors the selection of rules that
beneﬁted from good luck during the back test. When choosing among a
set of explanations that are equally adept at accounting for a phenomenon, it is wisest to choose the one making the fewest assumptions. This
is the principle of simplicity known as Occam’s Razor, which was discussed in Chapter 3.
Data-Mining Bias: The Fool’s Gold of Objective TA
263
--- page 262 ---

As will be shown, the observed performance of a rule can be decomposed into two independent components: randomness and the rule’s inherent predictive power. Of these two, randomness is by far the more
dominant component. Thus, the rule with the best-observed performance
was most likely the beneﬁciary of good luck. That is to say, randomness
boosted the rule’s performance above the level attributable to its true predictive power, if it possessed any. The opposite is the case for the rule
with the worst observed performance. It was most likely negatively impacted by luck. By selecting the rule with the highest observed performance, the data miner winds up picking a rule that experienced a large
component of good luck. Because luck cannot be counted on to repeat,
this rule’s out-of-sample performance is likely to settle back toward a level
that is representative of its inherent predictive power. This makes it probable that out-of-sample performance will be lower than the level of performance that allowed the rule to win the performance competition. The
bottom line: out-of-sample performance deterioration of the best rule is
most probably a fall from an unrealistically high expectation rather than
an actual decline in the rule’s predictive power.
DATA MINING
Data mining is the extraction of knowledge, in the form of patterns,
rules, models, functions, and such, from large databases. The limitations and biases of human intelligence make this task nearly impossible
for the unaided mind when the knowledge involves multiple variables,
nonlinear relationships, or high levels of noise. Thus, data mining relies
on computerized algorithms for knowledge extraction. An excellent discussion of the principal methods used in data mining can be found in
Elements of Statistical Learning,14 Predictive Data Mining: A Practical Guide,15 and Data Mining: Practical Machine Learning Tools and
Techniques.16
Data Mining as a Multiple Comparison Procedure
Data mining is based on a problem solving approach called a multiple
comparison procedure17 (MCP). The basic idea behind an MCP is to test
many different solutions to the problem and pick the one that performs
the best according to some criterion. Three elements are required to apply
an MCP: (1) a well-deﬁned problem, (2) a set of candidate solutions, and
(3) a ﬁgure of merit or scoring function that quantiﬁes the goodness of
each candidate’s performance. After all scores are in, they are compared
264 METHODOLOGICAL, PSYCHOLOGICAL, PHILOSOPHICAL, STATISTICAL FOUNDATIONS
--- page 263 ---

and the candidate with the highest score (best-observed performance) is
selected as the best solution for the problem.
Consider how this problem-solving paradigm applies in the context of
rule data mining:
1. The problem: timing long and short positions in a ﬁnancial market to
generate proﬁts.
2. A set of candidate solutions (solution universe or solution space):
a set of rules proposed by the objective technician.
3. Figure of merit: a measure of ﬁnancial performance such as the average rate of return over a historical test period, Sharpe ratio, return
to Ulcer Index.18
The performances of all rules are determined by back testing, and the
rule achieving the highest performance is selected.
Rule Data Mining as a Speciﬁcation Search
Data mining can be understood as a speciﬁcation search. That is to say, it
is a hunt for the speciﬁcations of the rule that produces the highest performance. The speciﬁcations are a set of mathematical and/or logical operations applied to one or more market data series thus transforming them
into a time series of market positions dictated by the rule.
Suppose the rule deﬁned below turned out to be the best performing rule:
Hold a long position in the S&P 500 if the ratio of Dow Jones Transportation Average close divided by the S&P 500 close is greater than
its 50-day moving average, else hold a short position.
The rule is speciﬁed by two mathematical operators: ratio and moving average; two logical operators: the inequality operator greater-than,
the conditional if, then, else; a single numerical constant: 50; and two data
series: Dow Jones Transports and S&P 500. Data mining discovered that
this set of speciﬁcations produced better performance than any alternative set of speciﬁcations that was tested.
Types of Searches
Data mining searches range from the simple to the sophisticated. One of
the ways in which they differ is how broadly the search universe is de-
ﬁned. This section considers three deﬁnitions of the search universe,
Data-Mining Bias: The Fool’s Gold of Objective TA
265
--- page 264 ---

starting with the narrowest search and progressing to the broadest. All approaches to data mining, whether they search simply and narrowly or
broadly using the most advanced methods are subject to data-mining bias.
Parameter Optimization.
The narrowest form of data mining is parameter optimization. Here, the search universe is conﬁned to rules with
the same form differing only in terms of their parameter values. Thus,
the search is restricted to ﬁnding the parameter value(s) of the highestperforming rule of a particular form.
An example of a rule form would be the dual-moving-average crossover
rule. It is speciﬁed by two parameters; look-back periods for the short-term
and long-term moving average. Signals are given when the short-term moving average crosses above (buy) and below (sell) a longer-term moving average. Parameter optimization searches for the pair of parameter values
that yields the highest performance.
The maximum number of dual-moving-average crossover rules that
can be searched is equal to the product of the number of values tested for
the short-term parameter and number of values tested for the long-term
parameter. A search that considers all these combinations is referred to as
an exhaustive or brute-force search.
There are more intelligent search methods that restrict the search to
combinations that are more likely to yield good results. This is accomplished by using the performances of parameter combinations tested early
in the search to guide the combinations that will be tested at later stages.
One such intelligent search method is the genetic algorithm, a technique
based loosely on the principles of biological evolution. Its demonstrated
ability to ﬁnd parameter combinations that are close to optimal relatively
quickly makes it especially useful when the number of possible parameter
combinations is high. Genetic algorithms have also proven to be effective
when performance is impacted strongly by randomness, which renders
more conventional guided search methods based on calculus impractical.
Excellent discussions of optimization methods can be found in Pardo,19
and a review of various advanced methods can be found in Katz and Mc-
Cormick20 and Kaufman.21
Rule Searching.
A broader version of data mining is rule searching.
Here, the universe of rules differ in their conceptual form as well as their
parameter values. The dual-moving-average crossover rule is one formalism for trend-following. Thus, it is simply one form in the broader category of trend-following rules that also include channel breakouts,
moving-average bands, and so forth. The general category of trendfollowing rules is merely one technical analysis category among others
that include counter-trend (mean-reversion) rules,22 extreme value rules,
266 METHODOLOGICAL, PSYCHOLOGICAL, PHILOSOPHICAL, STATISTICAL FOUNDATIONS
--- page 265 ---

divergence rules,23 diffusion rules, and so forth. Each category can be realized with numerous speciﬁc rule forms.
Part Two of this book presents a data-mining case study that is based
on rule searching. The study will focus on three rule categories or themes:
trends, extreme-values and transitions, and divergence. Each theme is realized with a speciﬁc rule form, which is deﬁned in Chapter 8.
Though rule searching considers a multitude of rule forms, each rule’s
complexity remains ﬁxed throughout the course of the search. Complexity refers to the number of parameters required to specify the rule. In
other words rule searching, as deﬁned herein, does not involve combining
simple rules to produce more complex rules
Rule Induction with Variable Complexity.
The broadest and
most ambitious form of data mining is rule induction. Here the search
considers rules of undeﬁned complexity. As the search proceeds, rules
of ever-greater complexity are considered. A complex rule might be
thought of as a composition of a simpler rule conjoined by logical operators or combined with a mathematical function as in a multivariate
model. Thus rule-induction data mining is concerned with ﬁnding the
rule of optimal complexity.
In contrast to less ambitious forms of data mining in which a rule’s
complexity is deﬁned at the outset of the search, rule induction uses machine learning (autonomous induction) to ﬁnd the degree of complexity
that produces the best performance. One scheme for rule induction
starts by testing individual rules. Next, pairs of rules are considered to
see if their performance is better than the best individual rule. Gradually, progressively more complex rules are tested and evaluated. In effect, rule-induction methods learn how to combine rules to optimize
performance.
Genetic algorithms, neural networks, recursive partitioning, kernel regression, support-vector machines, and boosted trees are some of the
methods used for these most ambitious of data-mining ventures. An excellent discussion of various methods and supporting statistical theory can
be found in The Elements of Statistical Learning by Hastie, Tibshirani,
and Friedman.24
OBJECTIVE TA RESEARCH
The goal of the objective technician is the discovery of a rule(s) that will
be proﬁtable in the future. The research method is back testing, which
produces an observable measure of performance. On the basis of this
Data-Mining Bias: The Fool’s Gold of Objective TA
267
--- page 266 ---

statistic, an inference is made about a population parameter, the rule’s
future or expected performance. It can be said, therefore, that the
essence of objective TA is statistical inference.
Why Objective Technicians Must Data Mine
The problem of out-of-sample performance failure has encouraged some
practitioners of objective TA to reject data mining. This is neither a wise
nor viable position. Today, an objective technician who refuses to data
mine is like the taxi driver who refuses to abandon the horse-drawn carriage—a charming relic but no longer suitable for getting to one’s destination efﬁciently.
Several factors compel the adoption of data mining as the preferred
method of knowledge acquisition. First, it works. Experiments presented
later in this chapter will show that under fairly general conditions, the
greater the number of rules back tested the greater the likelihood of ﬁnding a good rule.
Second, technological trends favor data mining. The cost effectiveness of personal computers, the availability of powerful back-testing and
data-mining software, and the availability of historical databases now
make data mining practical for individuals. As recently as a decade ago,
the costs limited data mining to institutional investors.
Third, at its current stage of evolution, TA lacks the theoretical
foundation that would permit a more traditional scientiﬁc approach to
knowledge acquisition. In developed sciences, such as physics, a single
hypothesis can be deduced from established theory and its predictions
can be tested against new observations. In the absence of theory, a
data-mining approach is called for, in which a multitude of hypotheses
(rules) are proposed and tested. The risk of this shotgun approach is
fool’s gold—rules that ﬁt the data by accident. Steps that can minimize
this risk are discussed later in this chapter.
Single-Rule Back-Testing versus Data Mining
Not all back testing is data mining. When just a single rule is proposed
and back tested, there is no data mining. This mode of research is illustrated in Figure 6.2. If the rule’s back test proves to be unsatisfactory, the
research stops and other more practical means of earning a living are
considered.
Data mining involves the back testing of many rules and picking one
based on its superior performance. This process is illustrated in Figure
6.3. Note that as depicted here an initial unsatisfactory performance by
268 METHODOLOGICAL, PSYCHOLOGICAL, PHILOSOPHICAL, STATISTICAL FOUNDATIONS
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
