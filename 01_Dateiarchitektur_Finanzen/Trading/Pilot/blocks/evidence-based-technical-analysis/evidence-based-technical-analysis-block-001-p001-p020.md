# Evidence-based Technical Analysis_ Applying the Scientific Method and Statistical Inference to Trading Signals.pdf — pages 1–20

--- page 1 ---

Evidence-Based
Technical
Analysis
Applying the Scientiﬁc
Method and
Statistical Inference
to Trading Signals
DAVID R. ARONSON
John Wiley & Sons, Inc.
--- page 2 ---

Copyright © 2007 by David R. Aronson. All rights reserved.
Published by John Wiley & Sons, Inc., Hoboken, New Jersey.
Published simultaneously in Canada.
Library of Congress Cataloging-in-Publication Data:
Aronson, David R., 1945–
Evidence-based technical analysis : applying the scientiﬁc method and
statistical inference to trading signals / David R. Aronson.
p.
cm.—(Wiley trading series)
Includes bibliographical references and index.
ISBN-13: 978-0-470-00874-4 (cloth)
ISBN-10: 0-470-00874-1 (cloth)
1. Investment analysis.
I. Title.
II. Series.
HG4529.A77
2007
332.63'2042—dc22
2006014664
Printed in the United States of America
--- page 3 ---

Contents
Acknowledgments
ix
About the Author
xi
Introduction
1
PART I
Methodological, Psychological,
Philosophical, and Statistical
Foundations
CHAPTER 1
Objective Rules and Their Evaluation
15
CHAPTER 2
The Illusory Validity of Subjective
Technical Analysis
33
CHAPTER 3
The Scientiﬁc Method and Technical
Analysis
103
CHAPTER 4
Statistical Analysis
165
CHAPTER 5
Hypothesis Tests and Conﬁdence Intervals
217
CHAPTER 6
Data-Mining Bias: The Fool’s Gold
of Objective TA
255
CHAPTER 7
Theories of Nonrandom Price Motion
331
PART II
Case Study: Signal Rules
for the S&P 500 Index
CHAPTER 8
Case Study of Rule Data Mining
for the S&P 500
389
CHAPTER 9
Case Study Results and the Future of TA
441
--- page 4 ---

APPENDIX
Proof That Detrending Is Equivalent to
Benchmarking Based on Position Bias
475
Notes
477
Index
517
--- page 5 ---

Introduction
T
echnical analysis (TA) is the study of recurring patterns in ﬁnancial
market data with the intent of forecasting future price movements.1
It is comprised of numerous analysis methods, patterns, signals, indicators, and trading strategies, each with its own cheerleaders claiming
that their approach works.
Much of popular or traditional TA stands where medicine stood before
it evolved from a faith-based folk art into a practice based on science. Its
claims are supported by colorful narratives and carefully chosen (cherry
picked) anecdotes rather than objective statistical evidence.
This book’s central contention is that TA must evolve into a rigorous
observational science if it is to deliver on its claims and remain relevant.
The scientiﬁc method is the only rational way to extract useful knowledge
from market data and the only rational approach for determining which
TA methods have predictive power. I call this evidence-based technical
analysis (EBTA). Grounded in objective observation and statistical inference (i.e., the scientiﬁc method), EBTA charts a course between the magical thinking and gullibility of a true believer and the relentless doubt of a
random walker.
Approaching TA, or any discipline for that matter, in a scientiﬁc manner is not easy. Scientiﬁc conclusions frequently conﬂict with what seems
intuitively obvious. To early humans it seemed obvious that the sun circled the earth. It took science to demonstrate that this intuition was
wrong. An informal, intuitive approach to knowledge acquisition is especially likely to result in erroneous beliefs when phenomena are complex
or highly random, two prominent features of ﬁnancial market behavior.
Although the scientiﬁc method is not guaranteed to extract gold from the
mountains of market data, an unscientiﬁc approach is almost certain to
produce fool’s gold.
This book’s second contention is that much of the wisdom comprising
the popular version of TA does not qualify as legitimate knowledge.
--- page 6 ---

KEY DEFINITIONS: PROPOSITIONS AND CLAIMS,
BELIEF AND KNOWLEDGE
I have already used the terms knowledge and belief but have not rigorously deﬁned them. These and several other key terms will be used repeatedly in this book, so some formal deﬁnitions are needed.
The fundamental building block of knowledge is a declarative statement, also known as a claim or a proposition. A declarative statement is
one of four types of utterances that also include exclamations, questions,
and commands. Declarative statements are distinguished from the others
in that they have truth value. That is to say, they can be characterized as
either true or false or probably true or probably false.
The statement “Oranges are on sale at the supermarket for ﬁve cents a
dozen” is declarative. It makes a claim about a state of affairs existing at
the local market. It may be true or false. In contrast, the exclamatory
statement “Holy cow, what a deal,” the command “Go buy me a dozen,” or
the question “What is an orange?” cannot be called true or false.
Our inquiry into TA will be concerned with declarative statements,
such as, “Rule X has predictive power.” Our goal is to determine which of
these declarative statements warrant our belief.
What does it mean to say, “I believe X.”? “With regard to states of affairs in general (i.e., ‘matters of fact’ or ‘what will happen’) believing X
amounts to expecting to experience X if and when we are in a position to
do so.”2 Therefore, if I believe the claim that oranges are on sale for ﬁve
cents a dozen, it means that I expect to be able to buy oranges for ﬁve
cents a dozen if I go to the store. However, the command to buy some oranges or the exclamation that I am happy about the opportunity, set up no
such expectation.
What does all this all means for us? For any statement to even be considered as a candidate for belief, it must “assert some state of affairs that
can be expected.3 Such statements are said to have cognitive content—
they convey something that can be known. “If the statement contains
nothing to know then there is nothing there to be believe.”4
Although all declarative statements presumably have cognitive content, not all actually do. This is not a problem if the lack of cognitive
content is obvious, for example, the declaration “The square root of
Tuesday is a prime number.”5 This utterance is, on its face, nonsense.
There are other declarative statements, however, whose lack of cognitive content is not so obvious. This can be a problem, because such
statements can fool us into thinking that a claim has been made that
sets up an expectation, when, in fact, no claim has really been put forward. These pseudo-declarative-statements are essentially meaningless
claims or empty propositions.
2
INTRODUCTION
--- page 7 ---

Although meaningless claims are not valid candidates for belief, this
does not stop many people from believing in them. The vague predictions
made in the daily astrology column or the nebulous promises made by
promoters of bogus health cures are examples of meaningless claims.
Those who believe these empty propositions simply do not realize that
what they have been told has no cognitive content.
A way to tell if a statement has cognitive content and is, thus, a valid
candidate for belief is the discernible-difference test6 described by Hall.
“Utterances with cognitive content make claims that are either true or
false; and whether they are true or false makes a difference that can be
discerned. That is why these utterances offer something to believe and
why there is no point in trying to believe an utterance that makes no such
offer”7 In other words, a proposition that passes the discernible-difference
test sets up an expectation such that the state of affairs, if the statement
were true, is recognizably different from the state of affairs, if the statement were false.
The discernible-difference criterion can be applied to statements purporting to be predictions. A prediction is a claim to know something about
the future. If a prediction has cognitive content, it will be clearly discernible in the outcome if the prediction was accurate or not. Many, if not
most, of the forecasts issued by practitioners of popular TA are devoid of
cognitive content on these grounds. In other words, the predictions are
typically too vague to ever determine if they were wrong.
The truth or falsity of the claim oranges are on sale for ﬁve cents a
dozen will make a discernible difference when I get to the market. It is
this discernible difference that allows the claim to be tested. As will be described in Chapter 3, testing a claim on the basis of a discernible difference is central to the scientiﬁc method.
Hall, in his book Practically Profound, explains why he ﬁnds
Freudian psychoanalysis to be meaningless when examined in light of the
discernible-difference test.
“Certain Freudian claims about human sexual development are compatible with all possible states of affairs. There is no way to conﬁrm or disconﬁrm either ‘penis envy’ or ‘castration complex’ because there is no
distinguishable difference between evidence afﬁrming and evidence denying these interpretations of behavior. Exactly opposite behaviors are
equally predictable, depending on whether the alleged psychosexual
stress is overt or repressed.” The requirement of “cognitive content rules
out all utterances that are so loose, poorly formed or obsessively held
(e.g., conspiracy theories) that there is no recognizable difference between what would be the case if they were so, and what would be the case
if they were not.”8 In a like vein, the Intelligent Design Theory carries no
cognitive freight in the sense that no matter what life form is observed it is
Introduction
3
--- page 8 ---

consistent with the notion that it manifests an underlying form speciﬁed
by some intelligent designer.9
What then is knowledge? Knowledge can be deﬁned as justiﬁed true
belief. Hence, in order for a declarative statement to qualify as knowledge, not only must it be a candidate for belief, because it has cognitive
content, but it must meet two other conditions as well. First, it must be
true (or probably true). Second, the statement must be believed with justiﬁcation. A belief is justiﬁed when it is based on sound inferences from
solid evidence.
Prehistoric humans held the false belief that the sun moved across
the sky because the sun orbited the earth. Clearly they were not in possession of knowledge, but suppose that there was a prehistoric person
who believed correctly that the sun moved across the sky because of
the earth’s rotation. Although this belief was true, this individual could
not be described as possessing knowledge. Even though they believed
what astronomers ultimately proved to be true, there was no evidence
yet to justify that belief. Without justiﬁcation, a true belief does
not attain the status of knowledge. These concepts are illustrated in
Figure I.1.
4
INTRODUCTION
Well Formed
Declarative Statements
(True or False)
True
Beliefs
Justified
by Evidence
& Inference
True
Statements
Candidates for Belief
Empty Claims
Questions
Commands

A
ll
 S
t
a
t
e
m
e
n
t
s
Knowledge
FIGURE I.1
Knowledge: justiﬁed true belief.
--- page 9 ---

From this it follows that erroneous beliefs or false knowledge fail to
meet one or more of the necessary conditions of knowledge. Thus, an erroneous belief can arise either because it concerns a meaningless claim or
because it concerns a claim that, though meaningful, is not justiﬁed by
valid inferences from solid evidence.
Still, even when we have done everything right, by drawing the best
possible inference from sound evidence, we can still wind up adopting
erroneous beliefs. In other words, we can be justiﬁed in believing a
falsehood, and honestly claim to know something, if it appears to be
true according to logically sound inferences from the preponderance of
available evidence. “We are entitled to say ‘I know’ when the target
of that claim is supported beyond reasonable doubt in the network
of well-tested evidence. But that is not enough to guarantee that we
do know.”10
Falsehoods are an unavoidable fact of life when we attempt to know
things about the world based on observed evidence. Thus, knowledge
based on the scientiﬁc method is inherently uncertain, and provisional,
though less uncertain than knowledge acquired by less formal methods.
However, over time, scientiﬁc knowledge improves, as it comes to describe reality in a progressively more accurate manner. It is a continual
work in progress. The goal of EBTA is a body of knowledge about market
behavior that is as good as can be had, given the limits of evidence gathering and the powers of inference.
ERRONEOUS TA KNOWLEDGE: THE COST
OF UNDISCIPLINED ANALYSIS
To understand why the knowledge produced by the popular version of TA
is untrustworthy, we must consider two distinct forms of TA: subjective
and objective. Both approaches can lead to erroneous beliefs, but they do
so in distinct ways.
Objective TA methods are well deﬁned repeatable procedures that issue unambiguous signals. This allows them to be implemented as computerized algorithms and back-tested on historical data. Results produced by
a back test can be evaluated in a rigorous quantitative manner.
Subjective TA methods are not well-deﬁned analysis procedures. Because of their vagueness, an analyst’s private interpretations are required.
This thwarts computerization, back testing, and objective performance
evaluation. In other words, it is impossible to either conﬁrm or deny a
subjective method’s efﬁcacy. For this reason they are insulated from evidentiary challenge.
Introduction
5
--- page 10 ---

From the standpoint of EBTA, subjective methods are the most problematic. They are essentially meaningless claims that give the illusion of
conveying cognitive content. Because the methods do not specify how
they are to be applied, different analysts applying it to the same set of
market data can reach different conclusions. This makes it impossible to
determine if the method provides useful predictions. Classical chart pattern analysis,11 hand-drawn trend lines, Elliott Wave Principle,12 Gann patterns, Magic T’s and numerous other subjective methods fall into this
category.13 Subjective TA is religion—it is based on faith. No amount of
cherry-picked examples showing where the method succeeded can cure
this deﬁciency.
Despite their lack of cognitive content and the impossibility of ever
being supported by sound evidence, there is no shortage of fervent believers in various subjective methods. Chapter 2 explains how ﬂaws in human
thinking can produce strong beliefs in the absence of evidence or even in
the face of contradictory evidence.
Objective TA can also spawn erroneous beliefs but they come about
differently. They are traceable to faulty inferences from objective evidence. The mere fact that an objective method has been proﬁtable in a
back test is not sufﬁcient grounds for concluding that it has merit. Past
performance can fool us. Historical success is a necessary but not a sufﬁ-
cient condition for concluding that a method has predictive power and,
therefore, is likely to be proﬁtable in the future. Favorable past performance can occur by luck or because of an upward bias produced by one
form of back testing called data mining. Determining when back-test
proﬁts are attributable to a good method rather than good luck is a question that can only be answered by rigorous statistical inference. This is
discussed in Chapters 4 and 5. Chapter 6 considers the problem of datamining bias. Although I will assert that data mining, when done correctly,
is the modern technician’s best method for knowledge discovery, specialized statistical tests must be applied to the results obtained with data
mining.
HOW EBTA IS DIFFERENT
What sets EBTA apart from the popular form of TA? First, it is restricted
to meaningful claims—objective methods that can be tested on historical
data. Second, it utilizes advanced forms of statistical inference to determine if a proﬁtable back test is indicative of an effective method. Thus,
6
INTRODUCTION
--- page 11 ---

the prime focus of EBTA is determining which objective methods are worthy of actual use.
EBTA rejects all forms of subjective TA. Subjective TA is not even
wrong. It is worse than wrong. Statements that can be qualiﬁed as wrong
(untrue) at least convey cognitive content that can be tested. The propositions of subjective TA offer no such thing. Though, at ﬁrst blush, they
seem to convey knowledge, when they are examined critically, it becomes
clear they are empty claims.
Promoters of New Age health cures excel at empty claims. They tell
you that wearing their magic copper bracelet will make you will feel better and put more bounce in your step. They suggest your golf game will
improve and maybe even your love life. However, the claim’s lack of speci-
ﬁcity makes it impossible to nail down exactly what is being promised or
how it can be tested. Such claims can never be conﬁrmed or contradicted
with objective evidence. On these same grounds, it can be said that the
propositions of subjective TA are empty and thus insulated from empirical
challenge. They must be taken on faith.
In contrast, a meaningful claim is testable because it makes measurable promises. It states speciﬁcally how much your golf game will improve or how bouncy your steps will be. This speciﬁcity opens the claim
to being contradicted with empirical evidence.
From the perspective of EBTA, proponents of subjective methods are
faced with a choice: They can reformulate the method to be objective, as
one practitioner of the Elliott Wave Principle has done,14 thus exposing it
to empirical refutation, or they must admit the method must be accepted
on faith. Perhaps Gann lines actually provide useful information. In their
present form, we are denied this knowledge.
With respect to objective TA, EBTA does not take proﬁtable back
tests at face value. Instead, they are subjected to rigorous statistical
evaluation to determine if proﬁts were due to luck or biased research.
As will be pointed out in Chapter 6, in many instances, proﬁtable back
tests may be a data miner fool’s gold. This may explain why many objective TA methods that perform well in a back testing perform worse when
applied to new data. Evidence-based technical analysis uses computerintensive statistical methods that minimize problems stemming from the
data-mining bias.
The evolution of TA to EBTA also has ethical implications. It is the
ethical and legal responsibility of all analysts, whatever form of analysis
they practice, to make recommendations that have a reasonable basis
and not to make unwarranted claims.15 The only reasonable basis for asserting an analysis method has value is objective evidence. Subjective
Introduction
7
--- page 12 ---

TA methods cannot meet this standard. Objective TA, conducted in accordance with the standards of EBTA can.
EBTA RESULTS FROM ACADEMIA
Evidence-based technical analysis is not a new idea. Over the past two
decades, numerous articles in respected academic journals16 have approached TA in the rigorous manner advocated by this book.17 The evidence is not uniform. Some studies show TA does not work, but some
show that it does. Because each study is conﬁned to a particular aspect of
TA and a speciﬁc body of data, it is possible for studies to reach different
conclusions. This is often the case in science.
The following are a few of the ﬁndings from academic TA. It shows
that, when approached in a rigorous and intellectually honest manner, TA
is a worthwhile area of study.
• Expert chartists are unable to distinguish actual price charts of stocks
from charts produced by a random process.18
• There is empirical evidence of trends in commodities19 and foreign exchange markets that can be exploited with the simple objective trend
indicators. In addition, the proﬁts earned by trend-following speculators may be justiﬁed by economic theory20 because their activities
provide commercial hedgers with a valuable economic service, the
transference of price risk from hedger to speculator.
• Simple technical rules used individually and in combinations can
yield statistically and economically signiﬁcant proﬁts when applied to
stock market averages composed of relatively young companies (Russell 2000 and NASDAQ Composite).21
• Neural networks have been able to combine buy/sell signals of simple
moving-average rules into nonlinear models that displayed good predictive performance on the Dow Jones Average over the period 1897
to 1988.22
• Trends in industry groups and sectors persist long enough after detection by simple momentum indicators to earn excess returns.23
• Stocks that have displayed prior relative strength and relative weakness continue to display above-average and below-average performance over horizons of 3 to 12 months.24
• United States stocks, selling near their 52-week highs, outperform
other stocks. An indicator deﬁned as the differential between a
stock’s current price and its 52-week high is a useful predictor of fu-
8
INTRODUCTION
--- page 13 ---

ture relative performance.25 The indicator is an even more potent predictor for Australian stocks.26
• The head-and-shoulders chart pattern has limited forecasting power
when tested in an objective fashion in currencies. Better results can
be had with simple ﬁlter rules. The head-and-shoulders pattern, when
tested objectively on stocks, does not provide useful information.27
Traders who act on such signals would be equally served by following
a random signal.
• Trading volume statistics for stocks contain useful predictive information28 and improve the proﬁtability of signals based on large price
changes following a public announcement.29
• Computer-intensive data-modeling neural networks, genetic algorithms, and other statistical learning and artiﬁcial-intelligence methods have found proﬁtable patterns in technical indicators.30
WHO AM I TO CRITICIZE TA?
My interest in TA began in 1960 at the age of 15. During my high-school
and college years I followed a large stable of stocks using the Chartcraft
point and ﬁgure method. I have used TA professionally since 1973, ﬁrst
as a stock broker, then as managing partner of a small software company, Raden Research Group Inc.—an early adopter of machine learning
and data mining in ﬁnancial market applications—and ﬁnally as a proprietary equities trader for Spear, Leeds & Kellogg.31 In 1988, I earned the
Chartered Market Technician designation from the Market Technicians
Association. My personal TA library has over 300 books. I have published approximately a dozen articles and have spoken numerous times
on the subject. Currently I teach a graduate-level course in TA at the
Zicklin School of Business, Baruch College, City University of New York.
I freely admit my previous writings and research do not meet EBTA standards, in particular with regard to statistical signiﬁcance and the datamining bias.
My long-standing faith in TA began to erode in response to a very
mediocre performance over a ﬁve-year period trading capital for Spear,
Leeds and Kellogg. How could what I believed in so fervently not work?
Was it me or something to do with TA in general? My academic training in
philosophy provided fertile grounds for my growing doubts. My concerns
crystallized into full ﬂedged skepticism as a result of reading two books:
How We Know What Isn’t So by Thomas Gilovich and Why People Believe
Weird Things, by Michael Shermer. My conclusion: Technical analysts,
Introduction
9
--- page 14 ---

including myself, know a lot of stuff that isn’t so, and believe a lot of
weird things.
TECHNICAL ANALYSIS: ART, SCIENCE,
OR SUPERSTITION?
There is a debate in the TA community: Is it an art or a science? The question has been framed incorrectly. It is more properly stated as: Should TA be
based on superstition or science? Framed this way the debate evaporates.
Some will say TA involves too much nuance and interpretation to render its knowledge in the form of scientiﬁcally testable claims. To this I retort: TA that is not testable may sound like knowledge, but it is not. It is
superstition that belongs in the realm of astrology, numerology, and other
nonscientiﬁc practices.
Creativity and inspiration play a crucial role in science. They will be
important in EBTA as well. All scientiﬁc inquiries start with a hypothesis,
a new idea or a new insight inspired by a mysterious mixture of prior
knowledge, experience and a leap of intuition. Yet, good science balances
creativity with analytical rigor. The freedom to propose new ideas must
be married to an unyielding discipline that eliminates ideas that prove
worthless in the crucible of objective testing. Without this anchor to reality, people fall in love with their ideas, and magical thinking replaces critical thought.
It is unlikely that TA will ever discover rules that predict with the precision of the laws of physics. The inherent complexity and randomness of
financial markets and the impossibility of controlled experimentation
preclude such ﬁndings. However, predictive accuracy is not the deﬁning
requirement of science. Rather, it is deﬁned by an uncompromising openness to recognizing and eliminating wrong ideas.
I have four hopes for this book: First, that it will stimulate a dialogue
amongst technical analysts that will ultimately put our ﬁeld on a ﬁrmer intellectual foundation; second, that it will encourage further research along
the lines advocated herein; third, that it will encourage consumers of TA
to demand more “beef” from those who sell products and services based
upon TA; and fourth, that it will encourage TA practitioners, professional
and otherwise, to understand their crucial role in a human-machine partnership that has the potential to accelerate the growth of legitimate TA
knowledge.
No doubt some fellow practitioners of TA will be irritated by these
ideas. This can be a good thing. An oyster irritated by a grain of sand
sometimes yields a pearl. I invite my colleagues to expend their
10
INTRODUCTION
--- page 15 ---

energies adding to legitimate knowledge rather than defending the
indefensible.
This book is organized in two sections. Part One establishes the
methodological, philosophical, psychological, and statistical foundations
of EBTA. Part Two demonstrates one approach to EBTA: testing of 6,402
binary buy/sell rules on the S&P 500 on 25 years of historical data. The
rules are evaluated for statistical signiﬁcance using tests designed to cope
with the problem of data-mining bias.
Introduction
11
--- page 16 ---

Methodological,
Psychological,
Philosophical,
and Statistical
Foundations
--- page 17 ---

Objective Rules
and Their
Evaluation
T
his chapter introduces the notion of objective binary signaling rules
and a methodology for their rigorous evaluation. It deﬁnes an evaluation benchmark based on the proﬁtability of a noninformative signal.
It also establishes the need to detrend market data so that the performances of rules with different long/short position biases can be compared.
THE GREAT DIVIDE: OBJECTIVE VERSUS SUBJECTIVE
TECHNICAL ANALYSIS
Technical analysis (TA) divides into two broad categories: objective and
subjective. Subjective TA is comprised of analysis methods and patterns
that are not precisely deﬁned. As a consequence, a conclusion derived
from a subjective method reﬂects the private interpretations of the analyst
applying the method. This creates the possibility that two analysts applying the same method to the same set of market data may arrive at entirely
different conclusions. Therefore, subjective methods are untestable, and
claims that they are effective are exempt from empirical challenge. This is
fertile ground for myths to ﬂourish.
In contrast, objective methods are clearly deﬁned. When an objective
analysis method is applied to market data, its signals or predictions are
unambiguous. This makes it possible to simulate the method on historical
data and determine its precise level of performance. This is called back
testing. The back testing of an objective method is, therefore, a repeatable
--- page 18 ---

experiment which allows claims of proﬁtability to be tested and possibly
refuted with statistical evidence. This makes it possible to ﬁnd out which
objective methods are effective and which are not.
The acid test for distinguishing an objective from a subjective method
is the programmability criterion: A method is objective if and only if it
can be implemented as a computer program that produces unambiguous market positions (long,1 short,2 or neutral3). All methods that cannot
be reduced to such a program are, by default, subjective.
TA RULES
Objective TA methods are also referred to as mechanical trading rules or
trading systems. In this book, all objective TA methods are referred to
simply as rules.
A rule is a function that transforms one or more items of information,
referred to as the rule’s input, into the rule’s output, which is a recommended market position (e.g., long, short, neutral). Input(s) consists of
one or more ﬁnancial market time series. The rule is deﬁned by one or
more mathematical and logical operators that convert the input time series into a new time series that consists of the sequence of recommended
market position (long, short, out-of-the-market). The output is typically
represented by a signed number (e.g., +1 or –1). This book adopts the convention of assigning positive values to indicate long positions and negative values to indicate shorts position. The process by which a rule
transforms one or more input series into an output series is illustrated in
Figure 1.1.
A rule is said to generate a signal when the value of the output series
changes. A signal calls for a change in a previously recommended market
position. For example a change in output from +1 to –1 would call for
closing a previously held long position and the initiation of a new short
position. Output values need not be conﬁned to {+1, –1}. A complex rule,
whose output spans the range {+10, –10}, is able to recommend positions
that vary in size. For example, an output of +10 might indicate that 10 long
positions are warranted, such as long 10 contracts of copper. A change in
the output from +10 to +5 would call for a reduction in the long position
from 10 contracts to 5 (i.e., sell 5).
Binary Rules and Thresholds
The simplest rule is one that has a binary output. In other words, its output can assume only two values, for example +1 and –1. A binary rule
16 METHODOLOGICAL, PSYCHOLOGICAL, PHILOSOPHICAL, STATISTICAL FOUNDATIONS
--- page 19 ---

could also be designed to recommend long/neutral positions or short/neutral positions. All the rules considered in this book are binary long/short
{+1, –1}.
An investment strategy based on a binary long/short rule is always in
either a long or short position in the market being traded. Rules of this
type are referred to as reversal rules because signals call for a reversal
from long to short or short to long. Over time a reversal rule produces a
time series of +1’s and –1’s that represent an alternating sequence of long
and short positions.
The speciﬁc mathematical and logical operators that are used to de-
ﬁne rules can vary considerably. However, there are some common
themes. One theme is the notion of a threshold, a critical level that distinguishes the informative changes in the input time series from its irrelevant
ﬂuctuations. The premise is that the input time series is a mixture of information and noise. Thus the threshold acts as a ﬁlter.
Rules that employ thresholds generate signals when the time series
crosses the threshold, either by the rising above it or falling beneath it.
These critical events can be detected with logical operators called inequalities such as greater-than (>) and less-than (<). For example, if the
Objective Rules and Their Evaluation
17
Time
Time
Etc.
Market
Time
Series
INPUT
Time Series
of
Market Position
OUTPUT
Mathematical
&
Logical
Operators
Rule
Long
Short
Time
FIGURE 1.1
TA rule transforms input time series into a time series of market position.
--- page 20 ---

time series is greater than the threshold, then rule output = +1, otherwise
rule output = –1.
A threshold may be set at a ﬁxed value or its value may vary over time
as a result of changes in the time series that is being analyzed. Variable
thresholds are appropriate for time series that display trends, which are
large long-lasting changes in the level of the series. Trends, which make
ﬁxed threshold rules impractical, are commonly seen in asset prices (e.g.,
S&P 500 Index) and asset yields (AAA bond yield). The moving average
and the Alexander reversal ﬁlter, also known as the zigzag ﬁlter, are examples of time series operators that are commonly used to deﬁne variable
thresholds. The operators used in the rules discussed in this book are detailed in Chapter 8.
The moving-average-cross rule is an example of how a variable
threshold is used to generate signals on a time series that displays trends.
This type of rule produces a signal when the time series crosses from one
side of its moving average to the other. For example;
If the time series is above its moving average, then the rule output
value = +1, otherwise the rule output value = –1.
This is illustrated in Figure 1.2.
Because it employs a single threshold, the signals generated by the
moving-average-cross rule are, by deﬁnition, mutually exclusive. Given a
single threshold, there are only two possible conditions—the times series
is either above or below4 the threshold. The conditions are also exhaustive (no other possibilities).5 Thus, it is impossible for the rule’s signals to
be in conﬂict.
18 METHODOLOGICAL, PSYCHOLOGICAL, PHILOSOPHICAL, STATISTICAL FOUNDATIONS
Price
Level
Moving
Average
Rule
Output
+1
-1
Time
Time Series
FIGURE 1.2
Moving-average-cross rule.
