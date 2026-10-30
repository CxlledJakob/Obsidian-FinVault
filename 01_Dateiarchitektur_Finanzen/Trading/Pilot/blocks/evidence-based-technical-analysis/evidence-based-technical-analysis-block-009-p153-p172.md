# Evidence-based Technical Analysis_ Applying the Scientific Method and Statistical Inference to Trading Signals.pdf — pages 153–172

--- page 153 ---

One challenge that faces the real-world chartist is the fact that actual
price oscillations do not trace out clearly identiﬁable peaks and troughs.
Rather, peaks and troughs occur at numerous oscillation scales from tiny
waves lasting minutes to very large ones lasting years or decades. This
property, called fractal scaling, imposes a burden on the subjective analyst trying to identify a head-and-shoulders pattern. The analyst must visually ﬁlter the price behavior to isolate peaks and troughs at one particular
scale of interest. This is relatively easy in retrospect, but it is quite difﬁcult
as the pattern is actually unfolding in real time.
C&O addressed this problem by using a percentage ﬁlter, also known
as an Alexander ﬁlter45 or a zigzag indicator, which is discussed by Merrill
The Scientific Method and Technical Analysis
153
Head & Shoulders
Double Bottom
Not H&S
Not H&S
Not
H&S
Not DB
Not DB
Not DB
FIGURE 3.7
Objective patterns—deﬁnitive exclusion rules.
Price
Time
Neck Line
A
E
B
D
C
Prior
Peak
Prior
Trough
Neck Line
Cross
Sell Signal
Left
Shoulder
Left
Trough
Right
Trough
Right
Shoulder
Head
FIGURE 3.8
Head and shoulders.
--- page 154 ---

in Filtered Waves.46 It is an objective method for identifying peaks and
troughs as prices evolve. Troughs are identiﬁed after prices have moved
up from a recent price low by an amount greater than a speciﬁed threshold percentage and peaks are identiﬁed after prices have moved down
from a recent price high by the threshold percentage. The problem is that
the identiﬁcation occurs with a time lag, the time it takes for prices to
move the threshold amount. For example, if the threshold is set at 5 percent, then a peak is not detected until prices have fallen at least 5 percent
from the most recent price maximum, and troughs are not detected until
prices have risen at least 5 percent from the recent price minimum. The
minimum required price movement causes a lag between the time the
peak or trough actually occurred and the time at which it is detected by
the zigzag ﬁlter.
Next, C&O addressed how to determine the correct threshold percentage to deﬁne the zigzag ﬁlter. Different ﬁlter thresholds would reveal
head-and-shoulders patterns of different size (scale). For example, a 3
percent ﬁlter might reveal a head-and-shoulders pattern that a 10 percent
ﬁlter would completely ignore. This makes it possible for multiple headand-shoulders patterns of differing scale to exist simultaneously. C&O addressed this problem by subjecting each ﬁnancial instrument (stock or
currency) to 10 different zigzag ﬁlters employing a range of threshold values. This allowed them to identify head-and-shoulders patterns on a variety of scales.
This raised yet another problem. What should the 10 ﬁlter thresholds
be? Clearly, a set of thresholds that would be good for one instrument
may not be good for another because they are characterized by different
levels of volatility. Realizing this, C&O take each instrument’s recent
volatility into account to arrive at the set of 10 ﬁlter thresholds used for
that instrument. This insight allowed their head-and-shoulders algorithm
to generalize across markets with different volatilities. C&O deﬁned a
market’s volatility, V, as the standard deviation of daily percentage price
changes over the most recent 100 trading days. The 10 thresholds were
arrived at by multiplying V by 10 different coefﬁcients; 1.5, 2.0, 2.5, 3.0,
3.5, 4.0, 4.5, 5.0, 5.5, 6.0. This resulted in 10 zigzag ﬁlters with varying sensitivity. The validity of the set of coefﬁcients chosen by C&O were con-
ﬁrmed by visual inspection of price charts by TA practitioners who
agreed that the 10 zigzag ﬁlters did a reasonable job of identifying headand-shoulders patterns.
Next C&O addressed the problem of deﬁning rules that qualify a candidate pattern as a valid head-and-shoulders. These rules were applied to
the instrument once its price had been zigzag ﬁltered and the peaks and
troughs at a given scale had been identiﬁed.
154 METHODOLOGICAL, PSYCHOLOGICAL, PHILOSOPHICAL, STATISTICAL FOUNDATIONS
--- page 155 ---

First, the head and shoulders identiﬁed by C&O’s algorithm had to satisfy the following basic rules:
1. The head of the pattern must be higher than both the left and right
shoulders.
2. The instrument must be in an uptrend prior to the formation of the
head-and-shoulders pattern. Thus, the pattern’s left shoulder has to be
above the prior peak (PP) and the pattern’s left trough has to be above
the prior trough (PT).
Next C&O grappled with more subtle and complex issues to qualify a
candidate pattern as a valid head-and-shoulders. They accomplished this
with a set of innovative measurements that qualiﬁed the pattern in terms
of its vertical and horizontal symmetry and the time it took for the pattern
to complete. These rules allowed them to deﬁnitively label a candidate
pattern as either head-and-shoulders or a non–head-and-shoulders.
Vertical Symmetry Rules
The vertical symmetry rules exclude patterns with necklines that are too
steeply sloped. The pattern in Figure 3.9 has acceptable vertical symmetry.
The rules compare the price levels of the right and left shoulders (A
and E) and the price levels of the right and left troughs (B and D) with a
price level deﬁned by the midpoint of segment AB, designated as point
X, and the midpoint of segment DE designated as point Y. To qualify as a
The Scientific Method and Technical Analysis
155
Price
Time
Neck Line
A
E
B
D
X
Y
C
PP
PT
Vertical
Symmetry
Rule
E > X & D < X
A > Y & B < Y
FIGURE 3.9
Good vertical symmetry.
--- page 156 ---

vertically symmetrical head-and-shoulders, the pattern must satisfy the
following rules.
1. The price level of the left shoulder peak, point A, must exceed the
price level of point Y.
2. The price level of the right shoulder peak, point E, must exceed the
price level of point X.
3. The price level of the left trough, point B, must be less than the price
level of point Y.
4. The price level of the right trough, point D, must be less than the price
level of point X.
Figures 3.10 and 3.11 show two head-and-shoulders patterns that
would be excluded because the vertical symmetry criteria have not been
satisﬁed.
Horizontal Symmetry Rule
Another feature used by C&O to distinguish head-and-shoulders patterns
from non-head-and-shoulders patterns was horizontal symmetry. A pattern with good horizontal symmetry is one for which the head, at point C,
is roughly equidistant from the peaks representing the pattern’s two shoulders (points A and E). C&O’s rule was that the distance from the head to
156 METHODOLOGICAL, PSYCHOLOGICAL, PHILOSOPHICAL, STATISTICAL FOUNDATIONS
Price
Time
D
B
A
X
C
Y
E
FIGURE 3.10
Poor vertical symmetry—neckline slope too steep.
--- page 157 ---

one shoulder should not be greater than 2.5 times the distance of the head
to the other shoulder. There is nothing magical about the value 2.5 other
than it seemed reasonable. See Figure 3.12.
Figure 3.13 is an example of a pattern that fails the test for horizontal
symmetry. Note the right shoulder is stretched too far to the right. A pattern with excessive leftward stretch would also be disqualiﬁed.
The Scientific Method and Technical Analysis
157
Price
Time
D
B
X
C
Y
E
A
FIGURE 3.11
Poor vertical symmetry—neckline slope too steep.
Price
Time
A
E
B
D
C
Horizontal
Symmetry
Rule
D1< 2.5  D2
D2< 2.5  D1
D1
D2
FIGURE 3.12
Good horizontal symmetry.
--- page 158 ---

Pattern Completion Rule: Maximum Time
to Neckline Penetration
C&O also speciﬁed a rule that excludes patterns that take too long to penetrate the neckline once the right shoulder, point E, has been formed. As
with other features, this criterion is deﬁned in terms of the pattern’s internal proportions rather than some ﬁxed number of time units. This allows
the rule to be applied to all patterns irrespective of their time frame or
scale.
The maximum time allowed for the movement from the right shoulder, point E, until the penetration of the neckline is the temporal distance
separating the two shoulders, points A and E. The pattern in Figure 3.14
meets the time to completion criterion because the temporal distance
from the right shoulder until neckline penetration (D4) is less than the
temporal separation of the shoulders (D3). The pattern in Figure 3.15 does
not qualify because D4 exceeds D3.
Future Information Leakage: Look-Ahead Bias
In their simulation of head-and-shoulders patterns, C&O took precautions
against the future information leakage or look-ahead bias problem. This
problem afﬂicts back tests that assume the possession of knowledge that
was not truly available when a trading decision was made. In the context
of back testing, this can make results appear more proﬁtable than would
be possible in actual trading. An extreme example would be assuming access to the Wall Street Journal the day before its publication.
158 METHODOLOGICAL, PSYCHOLOGICAL, PHILOSOPHICAL, STATISTICAL FOUNDATIONS
Price
Time
A
E
B
D
C
D2 > 2.5  D1
D1
D2
FIGURE 3.13
Poor horizontal symmetry.
--- page 159 ---

In the context of back testing the head-and-shoulders pattern, future
information leakage can occur if the zigzag threshold percentage is larger
than the percentage distance between the right shoulder peak and the
neckline. It would not be legitimate to assume a short-sale signal due to a
neckline penetration until the right shoulder (point E) has been detected.
However, it is possible for prices to cross the neckline before the right
shoulder is identiﬁed by the zigzag ﬁlter. To clarify, suppose the right
shoulder, point E, lies only 4 percent above the neckline, but the threshold
The Scientific Method and Technical Analysis
159
Price
Time
Completion
Rule
D4< D3
Neck Line
A
E
B
D
C
D3
D4
FIGURE 3.14
Pattern completion rule satisﬁed.
Price
Time
D4>D3
Neck Line
D3
D4
A
B
D
C
E
FIGURE 3.15
Pattern completion rule not satisﬁed.
--- page 160 ---

for the zigzag ﬁlter is 10 percent. It would not be legitimate to assume that
a trader knew about the neckline penetration because a 10 percent decline from the right shoulder would have been required to identify the
right shoulder of the head-and-shoulders pattern. In this example, assuming an entry price only 4 percent below the right shoulder would be more
favorable than waiting for a price 10 percent below the right shoulder, the
price movement required to have a fully formed head-and-shoulders pattern. To avoid this problem, C&O assumed an entry after the right shoulder had been objectively identiﬁed by the zigzag ﬁlter. Though this was a
less favorable entry price in some instances, the back test was unencumbered by look-ahead bias. I mention this because it shows C&O’s attention
to detail.
C&O’s pattern deﬁnition also deals with numerous other issues regarding entry and exit of positions, stop-loss levels, and so forth, but the
point has been made that it is possible to transform subjective chart patterns into objective testable patterns. Readers may take exception to arbitrary aspects of C&O’s pattern. All well and good if the reader has a better
objective deﬁnition to offer.
As a ﬁnal sanity check, C&O showed patterns that had been identiﬁed
by their automated head-and-shoulders algorithm to a number of
chartists. C&O claim that the chartists agreed that the patterns identiﬁed
by the objective head-and-shoulders algorithm did indeed conform to subjective head-and-shoulders criteria.
Head-and-Shoulders Back Test Results
Does the head-and-shoulders pattern carry predictive information with respect to stocks or currencies? In a word, the pattern hailed as a cornerstone of charting is a bust. Tests by C&O show that it is worthless on
stocks and only modestly proﬁtable on currencies. The pattern was profitable in two out of six currencies tested, but the relatively complicated
head-and-shoulders algorithm was far outperformed by a much simpler
objective signal based on zigzag ﬁlters. Moreover, when C&O tested the
occurrence of a head-and-shoulders in conjunction with the zigzag rule either as a conﬁrming or disconﬁrming signal, the head-and-shoulders pattern added no value. In other words, zigzag signals did no better when the
head-and-shoulders signal was in the same direction as the zigzag signal
and the zigzag did no worse when the head-and-shoulders signal was in
the opposite direction.The bottom line for currency traders: the value of
head-and-shoulders is doubtful.47
The head-and-shoulders performed worse on stocks. C&O evaluated
the head-and-shoulders on 100 randomly selected equities48 over the pe-
160 METHODOLOGICAL, PSYCHOLOGICAL, PHILOSOPHICAL, STATISTICAL FOUNDATIONS
--- page 161 ---

riod from July 1962 until December 1993. On average, each stock gave one
head-and-shoulders signal per year, counting both long and short signals,
giving a sample of over 3,100 signals. To test the pattern’s proﬁtability on
actual stock prices, C&O established a benchmark based on the pattern’s
performance on pseudo-price histories. These simulated price histories
were generated from actual historical price changes strung together in a
random fashion. By using actual price changes, the pseudo-price histories
had the same statistical characteristics as real stocks, but any predictability due to authentic temporal structure—the structure TA patterns are intended to exploit—was eliminated Despite the fact that the pseudo-price
histories were randomly generated, head-and-shoulders patterns that ﬁt
C&O’s deﬁnition still emerged. This conﬁrms the results of Harry Roberts
referred to earlier.
If the head-and-shoulders patterns appearing in real stock data are
useful, they should generate proﬁts superior to those achieved by trading
the patterns appearing in the fake stock price histories. C&O found that
head-and-shoulders patterns in actual stock prices lost slightly more
money than the signals on pseudo-price histories. According to the study
“the results uniformly suggest that head-and-shoulders trading are not
proﬁtable.” The signals lose on average about 0.25 percent over a 10-day
holding period. This compares with an average loss of 0.03 percent for
head-and-shoulders patterns in the pseudo-stock data. C&O referred to
traders using the pattern as “noise traders,” speculators who mistake a
random signal for an informative one.
Conﬁrming C&O’s ﬁndings is the work of Lo et al.49 Lo used an alternative method of objectifying the H&S pattern based on kernel regression,
a sophisticated local50 smoothing technique. Their study was unable to unseat the null hypothesis that the head-and-shoulders pattern is useless.51
Bulkowski52 found the head-and-shoulders was proﬁtable, but his research falls short. He does not provide an objective pattern deﬁnition that
back-testable pattern or entry and exit rules. In other words, his study is
subjective TA. In addition, his results fail to adjust for the trend of the general stock market over the time period in which he tested the patterns.
SUBSETS OF TA
Given the preceding discussion, TA can be seen as comprised of four subsets: (1) subjective TA, (2) objective TA with unknown statistical signiﬁ-
cance, (3) objective TA that is not statistically signiﬁcant, and (4)
objective TA that is statistically signiﬁcant.
The Scientific Method and Technical Analysis
161
--- page 162 ---

The ﬁrst subset, subjective TA, has already been deﬁned as methods
that cannot be reduced to a back-testable algorithm. Subsets two, three,
and four refer to objective methods.
The second subset is comprised of objective methods of unknown
value. Though these methods are objective and may have been back
tested, their results have not been evaluated for statistical signiﬁcance.
Here, it is simply a matter of applying the methods discussed in Chapters
4, 5, and 6. This is not meant to suggest that applying statistical methods
to back test results is simple, but rather that the decision to do so is.
The third subset, which I refer to as useless TA, consists of objective
TA rules for which results have been comprehensively back tested and
evaluated with statistical methods, but have been reveled to add no value
either on a stand-alone basis or when used in combination with other
methods. In all likelihood, the majority of objective TA methods will fall
into this subset. This is to be expected because ﬁnancial markets are extremely difﬁcult to predict due to their inherent complexity and randomness. In fact, in all ﬁelds of science, most proposed ideas do not work.
Important discoveries are rare. This is not obvious because the numerous
failures are typically not reported in the lay press or even in scientiﬁc
journals. What is most important is having a procedure in place for getting
rid of methods that do not work.
The fourth subset, useful TA, consists of objective methods that produce statistically signiﬁcant or, better yet, economically signiﬁcant results. Though some rules will be useful on a stand-alone basis, the
complexity and randomness of ﬁnancial markets make it likely that most
162 METHODOLOGICAL, PSYCHOLOGICAL, PHILOSOPHICAL, STATISTICAL FOUNDATIONS
NO
Subjective
YES
RIGOROUS
EVALUATION
NO
Objective
Value
Unknown
YES
SIGNIFICANT
NO
Objective
No Value
YES
Objective
Valuable
TESTABLE
EBTA
EBTA
FIGURE 3.16
Subsets of Technical Analysis.
--- page 163 ---

rules will add value when used in combination with other rules to form
complex rules.
Evidence-based technical analysis (EBTA) refers to subsets (3) and
(4)—objective TA that has been back tested and subjected to statistical
analysis. Given the preceding discussion, the categorization of TA is illustrated in Figure 3.16.
The next three chapters discuss the application of statistical analysis
to back-test results.
The Scientific Method and Technical Analysis
163
--- page 164 ---

Statistical
Analysis
S
tatistics is the science of data.1 In the late nineteenth century,
renowned British scientist and author H.G. Wells (1866–1946) said
that an intelligent citizen in a twentieth-century free society would
need to understand statistical methods. It can be said that an intelligent
twenty-ﬁrst-century practitioner or consumer of TA has the same need.
This chapter and the next two address aspects of statistics that are particularly relevant to TA.
Statistical methods are not needed when a body of data conveys a
message loudly and clearly. If all people drinking from a certain well die
of cholera but all those drinking from a different well remain healthy,
there is no uncertainty about which well is infected and no need for statistical analysis. However, when the implications of data are uncertain,
statistical analysis is the best, perhaps the only, way to draw reasonable
conclusions.
Identifying which TA methods have genuine predictive power is
highly uncertain. Even the most potent rules display highly variable performance from one data set to the next. Therefore, statistical analysis is
the only practical way to distinguish methods that are useful from those
that are not.
Whether or not its practitioners acknowledge it, the essence of TA is
statistical inference. It attempts to discover generalizations from historical data in the form of patterns, rules, and so forth and then extrapolate
them to the future. Extrapolation is inherently uncertain. Uncertainty is
uncomfortable.
The discomfort can be dealt with in two ways. One way is to pretend
--- page 165 ---

it does not exist. The other is the way of statistics, which meets uncertainty head on by acknowledging it, quantifying it, and then making the
best decision possible in the face of it. Bertrand Russell, the renowned
British mathematician and philosopher said, “Uncertainty, in the presence
of vivid hopes and fears, is painful, but must be endured if we wish to live
without the support of comforting fairy tales.”2
Many people are distrustful or disdainful of statistical analysis and
statisticians are often portrayed as nerdy number-crunching geeks divorced from reality. This shows up in jokes. We deride what we do not understand. There is the story about the six-foot-tall man who drowns in a
pond with an average depth of only two feet. There’s the tale about three
statisticians who go duck hunting. They spot a bird ﬂying overhead. The
ﬁrst shoots a foot too far to the left. The second shoots a foot too far to
the right. The third jumps up and exclaims, “We got it!!” Even though the
average error was zero, there was no duck for dinner.
Powerful tools can be put to bad purpose. Critics often charge that
statistics are used to distort and deceive. Of course, similar ends can be
achieved with words, although language is not held liable. A more rational
stance is needed. Rather than viewing all claims based on statistics with
suspicion or taking them all at face value, “a more mature response would
be to learn enough about statistics to distinguish honest, useful conclusions from skullduggery or foolishness.”3 “He who accepts statistics indiscriminately will often be duped unnecessarily. But, he who distrusts
statistics indiscriminately will often be ignorant unnecessarily. The middle
ground we seek between blind distrust and blind gullibility is an openminded skepticism. That takes an ability to interpret data skillfully.”4
A PREVIEW OF STATISTICAL REASONING
Statistical reasoning is new terrain for many practitioners and consumers
of TA. Trips to strange places are easier when you know what to expect.
The following is a preview of the next three chapters
For reasons discussed in Chapter 3, it is wise to start with the assumption that all TA rules are without predictive power and that a profitable back test was due to luck. This assumption is called the null
hypothesis. Luck, in this case, means a favorable but accidental correspondence between the rule’s signals and subsequent market trends in the
historical data sample in which the rule was tested. Although this hypothesis is a reasonable starting point, it is open to refutation with empirical
evidence. In other words, if observations contradict predictions made by
the null hypothesis, it is abandoned and the alternative hypothesis, that
166 METHODOLOGICAL, PSYCHOLOGICAL, PHILOSOPHICAL, STATISTICAL FOUNDATIONS
--- page 166 ---

the rule has predictive power, would be adopted. In the context of rule
testing, evidence that would refute the null hypothesis is a back-tested
rate of return that is too high to be reasonably attributed to mere luck.
If a TA rule has no predictive power, its expected rate of return will be
zero on detrended5 data. However, over any small sample of data, the profitability of a rule with no predictive power can deviate considerably from
zero. These deviations are manifestations of chance—good or bad luck.
This phenomenon can be seen in a coin-toss experiment. Over a small
number of tosses, the proportion of heads can deviate considerably from
0.50, which is the expected proportion of heads in a very large number of
tosses.
Generally, the chance deviations of a useless rule from a zero return
are small. Sometimes, however, a useless rule will generate signiﬁcant
proﬁts by sheer luck. These rare instances can fool us into believing a useless rule has predictive power.
The best protection against being fooled is to understand the degree
to which proﬁts can result from luck. This is best accomplished with a
mathematical function that speciﬁes the deviations from zero proﬁts that
can occur by chance. That is what statistics can do for us.
This function, called a probability density function, gives the probability of every possible positive or negative deviation from zero. In other
words, it shows the degree to which chance can cause a useless rule to
generate proﬁts. Figure 4.1 shows a probability density function.6 The fact
that the density curve is centered at a value of zero reﬂects the null hypothesis assertion that the rule has an expected return of zero.
Statistical Analysis
167
0
Back-Tested Rate of Return
Negative Returns
Probability
Density
Positive Returns
FIGURE 4.1
Probability density of chance performance—range of possible performance for a useless TA rule.
--- page 167 ---

In Figure 4.2, the arrow indicates the positive rate of return earned by
a rule when it was back tested. This raises the question: Is the observed
rate of return sufﬁciently positive to warrant a rejection of the null hypothesis that the rule’s true rate of return is zero? If the observed performance
falls well within the range of the deviations that are probably attributable
to chance, the evidence is considered to be insufﬁcient to reject the null
hypothesis. In such a case, the null hypothesis has withstood the empirical
challenge of the back-test evidence, and a conservative interpretation of
the evidence would suggest that the rule has no predictive power.
The strength of the back-test evidence is quantiﬁed by the fractional
area7 of the probability density function that lies at values equal to or
greater than the rule’s observed performance. This portion of the density
function is depicted by the darkened area to the right of the vertical arrow
in Figure 4.2. The size of this area can be interpreted as the probability
that a rate of return this high or higher could have occurred by chance under the condition that the rule has no predictive power (expected return =
0, or the null hypothesis is true). When this area occupies a relatively large
fraction of the density curve, it means that there is an equivalently large
probability that the positive performance was due to chance. When this is
the case, there is no justiﬁcation for concluding that the null hypothesis is
false. In other words, there is no justiﬁcation for concluding that the rule
does have predictive power.
However, if the observed performance is far above zero, the portion
of the probability density function lying at even more extreme values is
168 METHODOLOGICAL, PSYCHOLOGICAL, PHILOSOPHICAL, STATISTICAL FOUNDATIONS
0
Back-Tested Rate of Return
Negative Returns
Probability
Density
Positive Returns
Rate of return
this low falls well
within the range of
chance performance
FIGURE 4.2
Probability of chance performance for a useless rule.
--- page 168 ---

small. Performance this positive would be inconsistent with the assertion
that the rule has no predictive power. In other words, the evidence would
be sufﬁcient to refute the null hypothesis. Another way to think of this is
as follows: If the null hypothesis were true, a level of performance this
positive would have a low probability of occurrence. This probability is
quantiﬁed by the proportion of the density function that lies at values
equal to or greater than the observed performance. This is illustrated in
Figure 4.3. Note that the observed performance lies in the extreme right
tail of the density curve that would pertain if the rule were devoid of predictive power.
It is important to understand what this evidence does not tell us. It
tells us nothing about the probability that either the null hypothesis or the
alternative hypothesis is true. It only speaks to the probability that the evidence could have occurred under the assumption that the null hypothesis
is, in fact, true. Thus, the probability speaks to the likelihood of the evidence, not the likelihood of the truth of the hypothesis. Observed evidence that would be highly improbable, under the condition that the null
hypothesis is true, permits an inference that the null hypothesis is false.
Recall that, in Chapter 3, it was shown that evidence that a creature
has four legs cannot conclusively establish the truth of the hypothesis:
The creature is a dog. Although evidence of four legs would be consistent
with the hypothesis that the creature is a dog, it is not sufﬁcient to prove,
deductively, that the creature is a dog. Similarly, while the observation of
positive performance would be consistent with the hypothesis that a rule
has predictive power, it is not sufﬁcient to prove that it does. An argument
that attempts to prove the truth of a hypothesis with observed evidence
Statistical Analysis
169
0
Back-Tested Rate of Return
Negative Returns
Probability
Density
Positive Returns
Rate of return
this high
unlikely to
be due to chance
FIGURE 4.3
Probability of chance performance for a good rule.
--- page 169 ---

that is consistent with the hypothesis commits the logical fallacy of afﬁrming the consequent.
If the creature is a dog, then it has four legs.
The creature has four legs.
Invalid Conclusion: Therefore, the creature is a dog.
If a rule has predictive power, then it will have a proﬁtable back test.
Back test was proﬁtable.
Invalid Conclusion: Therefore, rule has predictive power.
However, the absence of four legs is sufﬁcient to prove that the hypothesis, the creature is a dog, is false.8 In other words, observed evidence
can be used to conclusively prove that a hypothesis is false. Such an argument uses the valid deductive form, denial of the consequent. The general
form of an argument, in which the consequent is denied, is as shown:
If P is true, then Q is true.
Q is not true.
Valid Conclusion: Therefore, P is not true (i.e., P is false).
If the creature is a dog, then it has four legs.
Creature does not have four legs.
Valid Conclusion: Therefore, it is false that the creature is a dog.
The argument just given uses the evidence, the absence of four legs,
to conclusively falsify the notion that the creature is a dog. However, this
level of certitude is not possible in matters of science and statistics. One
can never conclusively falsify a hypothesis. Nevertheless, a similar logic
can be used to show that certain evidence is highly unlikely if the hypothesis were true. In other words, the evidence gives us grounds to challenge
the hypothesis. Thus, a highly proﬁtable back test can be used to challenge the hypothesis that the rule has no predictive power (i.e., that it has
an expected return of zero).
If a rule’s expected return is equal to zero or less, then a back test
should generate proﬁts that are reasonably close to zero.
The back-tested performance was not reasonably close to zero; in
fact, it was signiﬁcantly above zero.
Valid Conclusion: Therefore, the contention that the rule’s expected
return is equal to zero or less is likely to be false.
170 METHODOLOGICAL, PSYCHOLOGICAL, PHILOSOPHICAL, STATISTICAL FOUNDATIONS
--- page 170 ---

How unlikely or rare must the positive performance be to reject the
notion that the rule is devoid of predictive power? There is no hard and
fast rule. By convention most scientists would not be willing to reject a
hypothesis so unless the observed performance has a 0.05 probability or
less of occurrence under the assumption the null is true. This value is
called the statistical signiﬁcance of the observation.
The discussion so far pertains to the case where only one rule is back
tested. In practice, however, TA rule research is typically not restricted to
testing a single rule. Economical computing power, versatile back-testing
software, and plentiful historical data make it easy, almost inviting, to test
many rules with the aim if selecting the one with the best performance.
This practice is known as data mining.
Although data mining is an effective research method, testing many
rules increases the chance of a lucky performance. Therefore, the threshold of performance needed to reject the null hypothesis must be set
higher, perhaps much higher. This higher threshold compensates for the
greater likelihood of stumbling upon a useless rule that got lucky in a
back test. This topic, the data mining bias, is discussed in Chapter 6.
Figure 4.4 compares two probability density functions. The top one
would be appropriate for evaluating the signiﬁcance for a single rule back
test. The lower density curve would be appropriate for evaluating the sig-
Statistical Analysis
171
0
Probability
Density
Appropriate Distribution
for Single-Rule Test
Back-Tested Rate of Return
Observed Performance
Observed Performance
Looks Significant
0
Probability
Density
Appropriate Distribution for Best of 1000 Rules
Does Not Look
Significant
FIGURE 4.4
Great performance in a single rule back test is only mediocre when
1,000 rules are tested.
--- page 171 ---

niﬁcance of the best-performing rule out of 1,000 back-tested rules. This
density curve takes into account the increased likelihood of luck that results from data mining. Notice that if this best rule’s observed performance were to be evaluated with the density curve appropriate for a
single rule, it would appear signiﬁcant because the performance is far out
in the right tail of the distribution. However, when the best rule’s performance is evaluated with the appropriate probability density function it
does not appear statistically signiﬁcant. That is to say, the rule’s rather
high performance would not warrant the conclusion that it has predictive
power or an expected return that is greater than zero.
THE NEED FOR RIGOROUS STATISTICAL ANALYSIS
The tools and methods of a discipline limit what it can discover. Improvements in them pave the way to greater knowledge. Astronomy took a great
leap forward with the invention of the telescope. Though crude by today’s
standards, the earliest instruments had 10 times the resolving power of the
unaided eye. Technical analysis has a similar opportunity, but it must replace informal data analysis with rigorous statistical methods.
Informal data analysis is simply not up to the task of extracting valid
knowledge from ﬁnancial markets. The data blossoms with illusory patterns whereas valid patterns are veiled by noise and complexity. Rigorous
statistical analysis is far better suited to this difﬁcult task.
Statistical analysis is a set of well-deﬁned procedures for the collection, analysis, and interpretation of data. This chapter and the next two
will introduce the way statistical tools and reasoning can be used to identify TA rules that work. This overview is necessarily condensed, and in
many instances I have sacriﬁced mathematical rigor for the sake of clarity.
However, these departures do not dilute the essential message: If TA is to
deliver on its claims, it must be grounded in a scientiﬁc approach that
uses formal statistical analysis.
AN EXAMPLE OF SAMPLING AND
STATISTICAL INFERENCE
Statistical reasoning is abstract and often runs against the grain of common sense. This is good and bad. Logic that runs counter to informal inference is good because it can help us where ordinary thinking lets us
down. However, this is exactly what makes it difﬁcult to understand. So
we should start with a concrete example.
172 METHODOLOGICAL, PSYCHOLOGICAL, PHILOSOPHICAL, STATISTICAL FOUNDATIONS
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
