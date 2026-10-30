# Evidence-based Technical Analysis_ Applying the Scientific Method and Statistical Inference to Trading Signals.pdf — pages 77–96

--- page 77 ---

or there is a motivation to ﬁnd one, the conﬁrmation bias, discussed previously, makes it likely that a correlative relationship will be detected even
if none exists. It is hard to imagine a TA analyst who is not impacted either
by prior belief, motivation, or both.
Even if there is no prior belief or no motivation to believe, people
still display a pronounced tendency to perceive illusory correlations.
Smedslund performed one of the earliest experiments showing this tendency.112 Nurses were shown 100 cards that were supposed to represent
actual patients. Each card indicated if the patient manifested a particular
symptom or not (the binary predictor) and whether that patient was ultimately diagnosed with a speciﬁc disease (the binary outcome). The
nurses’ task was to determine if the symptom was truly correlated with
the disease. The data shown to the nurses is summarized in the contingency table in Figure 2.16.
Over 85 percent of the nurses said the symptom was correlated with
the disease. They were persuaded by the 37 salient conﬁrmatory instances
falling in the upper left cell (symptom present and disease present). However, their conclusion was not supported by the data. A proper analysis of
this data, which takes all cell counts into consideration, indicates that the
symptom is not correlated with the disease.
76
METHODOLOGICAL, PSYCHOLOGICAL, PHILOSOPHICAL, STATISTICAL FOUNDATIONS
Cell A
37
Disease
Present
Symptom
Present
Symptom
NOT Present
Disease
NOT Present
True Diagnosis
instances
Cell B
17
instances
Cell C
33
instances
Cell D
13
instances
FIGURE 2.16
Data evaluated by nurses—Smedslund study (1963).
--- page 78 ---

Giving All Cells Their Due
A formal statistical test that considers all cell counts would be the rigorous way to determine if the nurses’ data was indicative of a valid correlation. However, one need not even resort to a formal test to see that there
is no correlation between the symptom and the disease. All cells can be
taken into consideration by computing some simple ratios of the cell
counts. For example, the proportion of patients that manifested the symptom and who ultimately proved to have the disease was approximately
0.69 (cell A divided by [cell A + cell B], 37/54 = 0.685). However, the proportion of patients that did not have the symptom that ultimately were diagnosed with the disease was almost the same or 0.72 (cell C divided by
[cell C + Cell D], 33/46 = 0.717). This quick-and-dirty calculation shows
that likelihood of having the disease was about the same (.69 and .72) regardless of whether the symptom was present. Had the symptom really
been correlated with the disease, the two proportions would have been
quite different, such as 0.90 of those with the symptom had the disease
whereas only 0.40 of those without the symptom had the disease. This
would not necessarily suggest that the symptom was a cause of the disease but only that it was a valid predictor of it.
In light of the fact that even simple ratios showed no correlation between symptom and disease, it is surprising that 85 percent of the nurses
concluded that the symptom was a reliable predictor of the disease. The
nurses were presented with other data sets as well. Overall, the factor that
best explained whether the nurses perceived a correlation was simply the
number of conﬁrmatory instances (cell A: symptom and disease both occur). Their judgments were unaffected by the relative proportions that
went into the calculation done earlier. In other words, the nurses did
not pay attention to the number of cases in the other three cells. As previously noted, many psychological studies have supported Smedslund’s
ﬁndings.113
The statistically correct way to detect a correlation between two binary variables is the Chi-square test.114 The test determines whether the
number of instances falling into each cell differs signiﬁcantly from the
number that would be expected in each cell if there were no correlation
between the variables. In other words, the test determines if cell counts
depart signiﬁcantly from a random sprinkling of the instances among the
four cells. When cell counts do depart signiﬁcantly115 from a random pattern, the Chi-square statistic takes on a large value. This is legitimate evidence of a correlation.
In Figure 2.17 the data from the nurses’ study have been altered to illustrate how cell counts might appear for a symptom that is correlated
with the disease. Each cell also contains the number of instances that
The Illusory Validity of Subjective Technical Analysis
77
--- page 79 ---

would be expected if there were no predictive relation between symptom
and disease (the random pattern). For example, in cell B, there were only
7 occurrences of disease with the symptom present (a false signal). If the
instances conformed to a random pattern, one would expect about 16
false signals. Thus, the relative proportion of disease, if symptom is present, is 0.87 versus 0.50 when the symptom is not present. The difference
in the proportions shows that the symptom is correlated with the disease.
The Role of Asymmetric Binary Variables
in Illusory Correlation
Illusory correlations are especially likely to emerge when the variables
involved are binary variables of a particular type—asymmetric binary
variables.116 Binary variables can be either symmetric or asymmetric. A
binary variable is said to be of the symmetric type if each of its possible
values is associated with the presence of an attribute (red/blue or Republican/Democrat) or the occurrence of an event (rain/snow or
78
METHODOLOGICAL, PSYCHOLOGICAL, PHILOSOPHICAL, STATISTICAL FOUNDATIONS
Cell A
47
Disease
Present
Symptom
Present
Symptom
NOT Present
Disease
NOT Present
Final Diagnosis
Expected = 37.8
Cell B
7
Expected = 16.2
Cell C
23
Expected = 32.2
Cell D
23
46
70
100
30
Expected = 13.8
54
FIGURE 2.17
Evidence of valid correlation.
--- page 80 ---

ﬂood/ﬁre). However, in the case of an asymmetric binary variable, one of
the variable’s two values depicts the absence of an attribute or the
nonoccurrence of an event. For example, (attribute present/attribute not
present) or (event occurred/event did not occur). In other words, one of
the variable’s states represents something not happening or a feature not
being present.
Research117 shows that when both the predictor and outcome variables are of the binary asymmetric type, the conﬁrmatory instances (pattern occurs and expected outcome occurs) are extraordinarily salient and
especially likely to consume the attention of the informal data analyst.
This attentional shift to the upper left cell strongly encourages the perception of illusory correlations. Recall that when the variables are asymmetric binaries, the other three cells of the contingency table contain
instances in which one or both of the variables are registering the absence
of the pattern, the nonoccurrence of the expected outcome or both pattern absence and outcome nonoccurrence.
The nonoccurrence of an event, or the absence of an attribute, is easily overlooked, because people have difﬁculty conceptualizing and evaluating this kind of evidence. The research just alluded to has shown it takes
more cognitive effort to evaluate instances where something does not occur than instances where something does. To illustrate the extra cognitive
effort required to process a statement involving the nonoccurrence of an
event or the absence of an attribute, consider the following two statements. Although they both convey the same information, the meaning of
the ﬁrst, which is given in an afﬁrmative form, is intuitively obvious. However, the meaning of the second, which is given in the negative form, requires some thought.
Statement 1: All humans are mortal.
Statement 2: All nonmortals are nonhumans.
Many of the propositions of subjective TA assert the existence of a
correlation between a pair of asymmetric binary variables: a signal/pattern that is either present on the chart or not and an outcome that the signal/pattern is supposed to predict, which either occurs or does not. Thus
the psychological research described earlier suggests that subjective TA
practitioners will be especially likely to fall prey to illusory correlations.
They will tend to be overly impressed with conﬁrmatory instances, in
which the pattern/signal did occur and the expected outcome also occurred, and give too little attention and weight to the three other types of
instances. Some examples of subjective patterns along with their expected outcomes are illustrated Table 2.1.
The Illusory Validity of Subjective Technical Analysis
79
--- page 81 ---

Hidden or Missing Data Compounds the Problem
of Illusory Correlations
The discussion so far shows how people come to believe in bogus correlations because of an insufﬁcient consideration of all relevant information
in a contingency table. However, the subjective technician’s plight does
not end here. Further compounding the propensity to detect illusory correlations is the problem of missing data. The cell counts needed to ﬁll in
the contingency table are not even readily available. The missing data
problem is yet another consequence of subjective analysis.
Without objectively deﬁned signals/patterns and without objectively
deﬁned standards for evaluating their outcomes, it is impossible obtain
the requisite counts that are needed to ﬁll the cells of the contingency
table. Without these counts, the true efﬁcacy of the signal/pattern cannot
be evaluated. This applies even to the conﬁrmatory instances found in the
upper left cell of the table, although subjective practitioners seem never
to run short of conﬁrmatory examples.118 Objective deﬁnitions are the
only solution to the missing data problem. Until TA adopts objectivity, it
will continue to operate on the basis of magical thinking and myth.
Once an illusory correlation is accepted as fact, two previously mentioned cognitive errors assure the misconception’s longevity. The mere belief in the specious relationship increases the likelihood that additional
supportive evidence will be noticed (conﬁrmation bias). Moreover, the alleged correlation is easily assimilated into one’s system of beliefs. As
Gilovich points out, once a phenomenon is suspected to exist, people are
easily able to come up with an explanation about why it exists and what it
means. In other words humans are very good at inventing stories after the
fact.119 Studies show that when people are falsely informed that they are
either above average or below average at some task, they can readily invent a reason that explains why.120 Part of the appeal of subjective TA is
the fascinating story offered about why it works. The story itself helps
sustain belief.
80
METHODOLOGICAL, PSYCHOLOGICAL, PHILOSOPHICAL, STATISTICAL FOUNDATIONS
TABLE 2.1
Subjective Patterns and Their Expected Outcomes
Pattern/Signal
Expected Outcome
Head-and-shoulders top
Downtrend
Completed 5th Elliott wave
Corrective wave
Strong uptrend, then ﬂag
Continuation of uptrend
Extremely bullish sentiment readings
Bear market
--- page 82 ---

A Behaviorist’s Explanation of Illusory
Correlations
Thus far, the discussion has explained the birth and longevity of erroneous beliefs in terms of cognitive psychology. A separate subdiscipline of
psychology, behaviorism, offers a somewhat different account of why
erroneous beliefs as to the efﬁcacy of subjective TA should be so durable.
Behavioral psychology is concerned with roles of reward (positive reinforcement) and punishment (negative reinforcement) in the learning of
habitual behaviors. If a pigeon is put in a cage and rewarded with a food
pellet each time it pecks at a button, it will eventually learn the habit of
pecking the button. Once this behavior has been acquired, the bird will
continue pecking the button so long as the food pellets keep coming.
However, if the reward is stopped, the bird eventually learns that the behavior no longer pays, and the learned behavior is extinguished.
One area of interest within behavioral psychology is the relationship
between the strength of a habit, indicated by the degree to which it resists extinction, and the speciﬁc type of reinforcement schedule that
originally led to the habit’s formation. The question is which type of reinforcement schedule produces the strongest habits. The simplest type of
reinforcement is rewarding every action—each peck earns a pellet. Another is partial reinforcement, in which rewards come only at ﬁxed time
intervals, such as every 60 seconds, or ﬁxed behavior intervals, such as
every tenth peck. It has been discovered that partial reinforcement
schedules produce slower learning (habit takes longer to form) but
stronger habits.
Most relevant to the domain of TA is the fact that of all the partial reinforcement schedules investigated, random reinforcement121 produces
habits that are most resistant to extinction. Under random reinforcement,
the organism’s behavior is not truly associated with the receipt of a reward. Behavior is rewarded by chance. In one experiment, a pigeon
pecked at a colored button and received random reinforcement for a mere
60 seconds. However, the pecking behavior continued for 3.5 hours after
the reward was stopped. In other words, the pathetic bird engaged in a
fruitless activity for a period that was 210 times longer than the random
reinforcement period that produced the habit.122
Random reinforcement is precisely the type of reward received by
someone who believes in an illusory TA correlation. Every so often, by
chance, the signal/pattern is followed by the expected outcome, thus reinforcing the belief. Behaviorist studies would predict that such a belief
would be extremely resistant to extinction. Superstitions and compulsive
gambling, two habits that rest on illusory correlations, are known to be
extremely difﬁcult to cure.123
The Illusory Validity of Subjective Technical Analysis
81
--- page 83 ---

When I worked on the ﬂoor of the American Stock Exchange, I met
several traders who displayed superstitious behavior. One fellow insisted
on wearing the same tie every day, which contained an accurate historical
record of his tastes in soup. Another was adamant about entering the trading ﬂoor through one particular door of the several available. Another refused to use a red pen. Each of these odd habits was probably initiated by
an accidental pairing of the behavior with a desired or undesirable outcome and then perpetuated by random reinforcement.
MISPLACED FAITH IN CHART ANALYSIS
Subjective technicians, irrespective of the speciﬁc method they practice,
believe in the efﬁcacy of visual chart analysis. Price charts are presumed
to be a valid method for detecting exploitable order in ﬁnancial market
data. The pioneers of TA used charts to discover the discipline’s foundational principles, and today they remain the primary analysis tool. This
section explains why conﬁdence in chart analysis is misplaced.
This is not to say that charts have no role in TA. They can serve as a
source of inspiration that leads to the formation of testable hypotheses
about market behavior. However, unless and until these conjectures are
vigorously and objectively tested, they remain mere suppositions rather
than trustworthy knowledge.
An Informal Search for Order Is Sure to Find It
Humans have both the need and the capacity to ﬁnd order and meaning in
their experience. “It may have been bred into us through evolution because of its general adaptiveness: We can capitalize on ordered phenomena in ways that we cannot on those that are random. The predisposition
to detect patterns and make connections is what leads to discovery and
advance. The problem is that the tendency is so strong and so automatic
that we sometimes detect coherence even when it does not exist.”124
A trait of intuitive, nonscientiﬁc thinking is the tendency to accept
without question surface impressions and obvious explanations. Unfortunately, what is obvious at ﬁrst blush is not necessarily valid. To the
ancients it seemed obvious the sun orbited the earth. To the pioneers of
TA it seemed obvious that ﬁnancial market prices formed patterns and
trends. Just as early observers of the heavens perceived mythical ﬁgures like Leo the Lion and Orion the Hunter in the random arrangements of stars, the ﬁrst technicians saw heads-and-shoulders, double
and triple tops, and other patterns in the meandering movements of
82
METHODOLOGICAL, PSYCHOLOGICAL, PHILOSOPHICAL, STATISTICAL FOUNDATIONS
--- page 84 ---

stock and commodity prices. These patterns form the lexicon of subjective chart analysis.
Our nervous system seems to be wired to see shapes regardless of
whether they are real. Dr. John Elder,125 a noted authority on predictive
modeling and data mining, calls this the “bunnies in the clouds” effect.
There is, however, good reason to question the validity of chart analysis,
and by extension, to question the validity of knowledge based on it. I contend that trends and patterns on charts that appear real to the eye may often be illusions born of the mind’s voracious, though indiscriminate,
appetite to perceive order.
This is not meant to imply that ﬁnancial markets are devoid of authentic trends and patterns. In fact, there is sound empirical evidence that patterns exist which have predictive power.126 It does mean, however, that
visual inspection of charts is an inadequate means for discovering or verifying the authenticity of patterns. Studies127 have shown that even expert
chartists cannot reliably distinguish between authentic stock charts and
simulated charts produced by a random process. A method of analysis
that cannot discriminate real charts from fakes cannot provide reliable
analysis of the real. A jeweler who can’t tell the difference between authentic diamonds and dime-store costume jewelry is in no position to appraise a diamond necklace.
Illusory Trends and Patterns in Financial Data
Statistician Harry Roberts said that technical analysts fall victim to the illusion of patterns and trends for two possible reasons. First, “the usual
method of graphing stock prices gives a picture of successive (price) levels rather than of price changes and levels can give an artiﬁcial appearance of pattern or trend. Second, chance behavior itself produces
patterns that invite spurious interpretations.”128
Roberts showed that the same chart patterns to which TA attaches
importance129 appear with great regularity in random walks. A random
walk is, by deﬁnition, devoid of authentic trends, patterns, or exploitable
order of any kind. However, Roberts’ random-walk charts displayed headand-shoulder tops and bottoms, triangle tops and bottoms, triple tops and
bottoms, trend channels, and so forth.
You can create a random-walk chart from a sequence of coin ﬂips by
starting with an arbitrary price, say $100, and adding one dollar for each
head and subtracting one dollar for each tail. In other words, the face of
the coin represents a price change and the chart shows a sequence of simulated price levels. Each simulated price in the sequence is equal to the
cumulative algebraic sum of all prior random changes added to the starting value. If you carry out this process for three hundred or so ﬂips, you
The Illusory Validity of Subjective Technical Analysis
83
--- page 85 ---

may be amazed at the patterns that appear. Many will be similar to the patterns found on actual charts of ﬁnancial assets. Clearly the patterns or
trends that appear on a coin-ﬂip chart cannot predict its future evolution.
This raises an important question: if chartist-like patterns can appear
with such regularity in random walks, and it is known that these patterns
cannot be predictive, how can the same patterns be considered predictive
simply because they happen to appear on a real chart?
Perhaps we should not trust the eye of Roberts. He was a statistician,
not an expert in TA. If an expert chartist were able to spot the patterns
occurring in random-walk charts as fakes the way a competent jeweler
can spot a counterfeit diamond, then Roberts’s random-walk experiment
would not prove anything other than his lack of chart expertise. Certainly, expert chartists should claim that they can tell the difference between patterns occurring in random walks and those occurring on real
charts. After all, if the patterns on actual markets charts form as a result
of changes in supply and demand and/or oscillations in market mood, as
TA claims, they should look different from the accidental meanderings on
a random-walk chart!130
Unfortunately expert chartists have been unable to tell the difference
between real and fake charts. Arditti131 put them to the test. When presented with an assortment of real charts mixed with random-walk charts,
the chartists examined by Arditti were no more accurate at telling the real
from the fake than a guess. This result was subsequently conﬁrmed in an
informal study132 by Professor Jeremy Siegel of the Wharton Business
School.133 Siegel presented the graphs shown in Figure 2.18 (four real and
four random) to a group of top Wall Street stockbrokers who considered
themselves competent chart readers. Again, the experts were unable to reliably distinguish the real from the random. I conducted a similar experiment using graduate business students who had just completed a course
in technical analysis. Their accuracy was consistent with guessing. The
real charts are indicated by the X.
What can we conclude from these results? First, they do not imply
that ﬁnancial markets are random, and hence devoid of valid trends and
patterns. But they do call into question the efﬁcacy of subjective/visual
chart analysis as a means of knowledge acquisition and forecasting. If
chart reading were a valid skill, it should at least be possible to distinguish
an actual chart from a random fake.
Evidence of Illusory Trends in Sports
Financial markets are not the only arena in which observers are plagued
by the illusion of order. Many sports fans and athletes believe in performance trends, periods of hot and cold performance. What baseball fan or
84
METHODOLOGICAL, PSYCHOLOGICAL, PHILOSOPHICAL, STATISTICAL FOUNDATIONS
--- page 86 ---

player does not think batting slumps or hitting streaks are real? Basketball
fans, players, coaches, and sports commentators speak of the so-called
hot hand, a trend of above-average shooting accuracy.
These beliefs are widely held because trends in athletic performance
seem so obvious. However, rigorous statistical analysis of player performance134 indicates that the hot hand phenomenon is an illusion. The fans
have been duped by their intuition. This erroneous belief stems from a
faulty notion about how random phenomena ought to behave.135 Common
sense would have us believe that streaks (a sequence of strike-outs, or a
sequence of successful shots, and so forth) should not occur in a random
process. Rather, intuition incorrectly tells us that random processes
should display something resembling an alternating pattern of positive
and negative outcomes.
The truth is that sports trends are, by and large a cognitive illusion.
What appears to be a batting slump or a hitting streak is often nothing
more than a run of similar outcomes, a phenomenon that is quite common
in random processes. A valid trend is a streak of longer duration than
those that are ordinary in random data. That is to say, a real trend is a
streak of sufﬁcient length that it would be rare in a random process.
Gilovich points out that “although a player’s performance does not
display longer streaks than those allowed by chance, it does not mean that
the player’s performance is chance determined. It is not. Whether a given
The Illusory Validity of Subjective Technical Analysis
85
X
X
X
X
FIGURE 2.18
Real and randomly generated stock charts.
Siegel, Jeremy J., Stocks for the Long Run, 3rd Edition, Copyright 2002, 1998,
1994, McGraw-Hill; the material is reproduced with the permission of The McGraw-
Hill Companies.
--- page 87 ---

shot is hit or missed is determined by a host of non-chance factors, foremost among them being the skill of the offensive and defensive players involved. However, one factor that does not inﬂuence or predict the
outcome is the player’s recent hit rate.”136
To understand why sports fans, athletes, and chart analysts fall prey
to the illusion of trends and patterns in data that may in fact be random
we must delve a bit deeper into the nature of intuitive judgment.
THE INTUITIVE JUDGMENT AND THE ROLE
OF HEURISTICS
“To simplify, there are basically two types of thought processes: automatic
and controlled.”137 “Intuition is automatic. It is our capacity for direct
knowledge, for immediate insight without observation or reason.”138 It is
perception-like, rapid, and effortless, notes Princeton University psychologist Daniel Kahneman. In contrast, “deliberate or controlled thinking
is reasoning-like, critical, and analytic.”139 The prototype of controlled
thought is scientiﬁc reasoning. The prototype of intuition is the brilliant
medical diagnostician who always seems to sniff the underlying disease.
Subjective technicians rely primarily on intuition, and they do so to their
detriment.
Human intelligence has limits. We can only pay attention to an
extremely small fraction of the information that comes to us through
our sensory organs. Moreover, the mind is not well suited to complex
tasks such as estimating probabilities and making decisions in a logically and probabilistically correct manner in situations characterized
by uncertainty.
To cope, we must simplify. We reduce the complexities of estimating
and decision making by resorting to a variety of quick and dirty rules of
reasoning known as judgment heuristics. They focus our attention on a
limited portion of the total information picture and utilize relatively simple forms of information processing and reasoning to arrive at conclusions quickly. All of this is done without awareness or exertion. We make
intuitive judgments as automatically and effortlessly as we recognize
someone’s face, a task for which the mind is very well suited.
We acquire judgment heuristics from life experience. The term
heuristic refers to the notion of discovery by trial and error, and this is
how these rules of thought are acquired. Moreover, they slip into usage so
subtly that we are unaware of how or when we learned them. And we
adopt them because, in general, they work. However, they work imperfectly and when they fail our judgment suffers.
86
METHODOLOGICAL, PSYCHOLOGICAL, PHILOSOPHICAL, STATISTICAL FOUNDATIONS
--- page 88 ---

The good news is that heuristic judgment tends to err in a consistent
manner. In other words, the judgments are biased—they tend to be wrong
in the same way over and over again.140 This consistency makes it possible
to predict the conditions under which heuristic judgments will fail and
how they will fail—whether the deviation from true value will be a positive or a negative one.
In general, heuristic judgments tend to err in situations characterized
by uncertainty.141 Financial markets are highly uncertain, so intuitive judgments in this arena are likely to be biased. The speciﬁc bias that afﬂicts
subjective technicians is the propensity to see trends and patterns in data
where such structures are not truly present. In other words, there is a systematic tendency to perceive order where only random behavior exists.
This may explain why chartists are unable to distinguish real charts from
pseudocharts produced from random data.
In the words of Professor Burton Malkiel, “Randomness is a difﬁcult
notion for people to accept. When events come in clusters and streaks,
people look for explanations and patterns. They refuse to believe that
such patterns—which frequently occur in random data—could equally be
derived from tossing a coin. So it is in the stock market as well.”142 Malkeil
takes the extreme position that the market is random. I do not share this
conviction but agree that people misperceive order in data that is random.
For this reason visual inspection of price charts cannot be trusted.
The illusion of trends and patterns in data that is truly random may be
attributable to the failure of a speciﬁc judgment heuristic called reasoning by representativeness. That is to say, a faulty application of the generally useful representativeness rule biases us toward the perception of
order where it does not exist.
Heuristic Bias and the Availability Heuristic
To recap, heuristics help us make complex decisions rapidly in spite of
the limitations of human intelligence, but they can cause those decisions
to be biased. The notion of heuristic bias is easily explained by considering the availability heuristic.
We rely on the availability heuristic to estimate the likelihood of future events. It is based on the reasonable notion that the more easily we
can bring to mind a particular class of events, the more likely it is that
such events will occur in the future. Events that are easily brought to
mind are said to be cognitively available. For example, plane crashes are
a class of events with high cognitive availability.
The availability heuristic makes a certain amount of sense. The ability
to recall a class of events is indeed related to how frequently they have occurred in the past, and it is also true that events that have happened fre-
The Illusory Validity of Subjective Technical Analysis
87
--- page 89 ---

quently in the past are generally more likely to occur in the future. This is
in keeping with one theory of probability that asserts that the future likelihood of an event is related to its historical frequency.143 Taken as a class,
thunderstorms have been more frequent in the past than asteroid impacts,
and they do indeed have a higher future likelihood.
The problem with the availability heuristic is that there are factors
that can enhance an event’s cognitive availability that have nothing to do
with its historical frequency and are, therefore, irrelevant to estimating
its future likelihood. Consequently, our judgments of likelihood are
sometimes falsely inﬂated by the intrusion of these irrelevant factors.
Two factors that have no relevance to an event’s likelihood but that do increase its cognitive availability are recency and vividness. That is to say,
how recently144 an event of the type in question took place and how vivid
the event was both impact how easily we can bring such events to mind.
Consider plane crashes as a class of events. A plane crash that just occurred is both vivid and recent. As a result, in the period right after a
well-publicized plane crash many people tend to overestimate the likelihood of future plane crashes and are inordinately fearful of ﬂying. Note
the bias in the judgment is one of overestimating a probability. The availability heuristic never causes us to underestimate an event’s likelihood.
The error is always one of overestimating the probability.
The Representativeness Heuristic:
Reasoning by Similarity
The representativeness heuristic, which was ﬁrst identiﬁed by Tversky
and Kahneman145 is of particular relevance to subjective TA. We use this
rule to make intuitive classiﬁcation judgments. In other words, it is used
to estimate the probability that a particular object, for example the dog
before me, belongs to a particular class of objects, for example the class
of poodles. The underlying premise of the representativeness heuristic is
that each member of a class should display the key common attributes
that deﬁne the class. It is quite reasonable to expect that objects from the
same class should possess a similar set of characteristics. In arriving at a
judgment by representativeness about whether a given object belongs to a
particular class, we unconsciously consider the degree of similarity or
match between the attributes of the object and the set of attributes presumed to be representative of that class. This is why this heuristic is referred as a reasoning by representativeness.
In this section and the next, I will argue that visual chart analysis is inherently ﬂawed because of a bias toward the perception of order and pattern even in data that is truly random. I will contend that this bias is due to
a misapplication of the representativeness heuristic. In other words, a
88
METHODOLOGICAL, PSYCHOLOGICAL, PHILOSOPHICAL, STATISTICAL FOUNDATIONS
--- page 90 ---

bias stemming from a faulty application of the representativeness heuristic can explain why subjective technicians fall prey to an illusion of order
in charts that were, in fact, produced by a random process.
To explain how chartists make this mistake, which is rather subtle, we
will take a brief detour by considering a more easily understood case of
heuristic bias caused by representativeness reasoning.
As mentioned earlier, reasoning by representativeness is premised on
the notion that a class of objects or events can be represented by a class
stereotype—a typical example that possesses the class’s key distinguishing characteristics. Often this line of reasoning works well. However, it
fails when an object’s most noticeable features are not reliable indicators
of the object’s class. In other words, when the characteristics that most
draw our attention are not relevant in judging the object’s class146 reasoning by representativeness tends to fail. Unfortunately, intuitive judgment
tends to be based on the most obvious features of an object or event regardless of whether these features are truly useful indicators of its class.
Reasoning by representativeness estimates the probability than an
object belongs to a given class by considering the degree of match between the object’s most salient attributes and the most salient attributes
of the class stereotype. The greater the number of matching attributes,
the higher the adjudged probability that the object is indeed a member of
the class in question. “Modern psychologists hypothesize that our concepts of categories (classes) like bank tellers, feminists, microcomputers, skunks, and all kinds of things are represented cognitively as lists of
attributes that we believe are deﬁning characteristics of those entities.”147
This is illustrated in Figure 2.19. In many instances this fast and frugal
classiﬁcation rule gives accurate results. People would not use such a
rule it if it did not.
Let’s consider an example where the application of the representativeness rule leads to an erroneous judgment about an object’s class.
Imagine that you have just taken your seat on a commercial airline ﬂight
and you become concerned that a person (the object) seated next to you
may be a terrorist (the class). Your apprehension is aroused because the
person has the following obvious characteristics: man of apparently Middle Eastern origin, mustache, 25–30 years of age, wearing a turban, reading the Koran, and appearing nervous. Your conclusion that the man may
very well belong to the class of terrorists occurred quite spontaneously
because his obvious characteristics are similar to a set of characteristics
that was also possessed by (i.e., is representative of) the terrorists who
conducted the attacks of September 11, 2001. Your inference was based
on the representativeness heuristic. Now consider how you would have
reacted if the passenger were a young Middle Eastern man but was wearing blue jeans and a tee-shirt with an obscene logo, had on a New York
The Illusory Validity of Subjective Technical Analysis
89
--- page 91 ---

Yankee baseball cap instead of a turban, was reading a copy of Playboy
instead of the Koran, and was listening to rock music on an iPod while
blowing chewing-gum bubbles. You would not have been worried. Intuitive judgments of class rest on the assumption that the most obvious
characteristics of an individual are reliable indicators of that individual’s class.
Judgments based on representativeness can err because they fail to
take into account statistical and/or logical elements of a situation that are
truly relevant to an accurate judgment about its class. The probabilistically correct way of estimating the class of an event or object is called
Bayes’ theorem,148 which is derived from the axioms of probability theory.
If it were applied to the airline passenger suspected of being a terrorist, it
would take into account such things as the proportion of terrorists in the
world (i.e., the base rate of the class of terrorists), the proportion of people in the world that possess the set of observed characteristics (i.e., the
base rate of the pattern), and the proportion of terrorists that have this
pattern of characteristics (i.e., the conditional probability that these characteristics are present given that the individual is in fact a terrorist). When
these values are plugged into the equation that expresses Bayes’ theorem
we obtain the conditional probability that the person is a terrorist, given
that they possess the pattern of characteristics.
90
METHODOLOGICAL, PSYCHOLOGICAL, PHILOSOPHICAL, STATISTICAL FOUNDATIONS
C
K
Q
Stereotypical Class Member
Object
of
Uncertain
Class
Class
C
G M Q
FIGURE 2.19
Classiﬁcation by number of matching attributes.
--- page 92 ---

Because intuition operates on the basis of representativeness, rather
than Bayes’ law, we tend to commit an error called the base rate fallacy.
This is the failure to consider the base rate statistics characterizing a situation. Terrorists, fortunately, are very rare (i.e., have a very low base rate).
Thus, among the entire set of people who possess the same salient characteristics as the terrorists of 9/11/01, the fraction that are actually terrorists
is extremely small. Perhaps only one person in a million with these traits
is actually a terrorist. This fact is highly relevant to judging the likelihood
that the person seated next to us is dangerous. However, we tend to neglect base-rate statistics because intuitive judgment is focused on the attention-grabbing features of a situation or object rather than relevant facts
such as a base-rate.
An example of fallacious reasoning by representativeness was displayed by market analysts who predicted that a deﬂationary depression
would follow the stock market crash of October 1987. They were captivated by the very noticeable similarity between the behavior of the stock
market in 1929, which did lead to a deﬂationary depression, and its behavior in 1987. Both witnessed market crashes. This glaring similarity took
analysts’ attention away from signiﬁcant dissimilarities between 1987 and
1929. In other words, 1987 and 1929 were different with respect to factors
that do have some predictive information with respect to deﬂationary collapses. An examination of market crashes over the last 100 years shows
that a price crash is not a reliable predictor of a deﬂationary depression.
Another error associated with representative reasoning is called the
conjunction fallacy, a failure to take into account a basic law of logic
telling us that a proper subset must contain a smaller number of objects
than the larger set to which it belongs. The set horses is a proper subset of
the larger set, animals. It follows that horses must be fewer in number
than animals in general, which includes horses, bluebirds, aardvarks, and
so forth. However, when people rely on the representativeness rule, they
seem to ignore this law of logic and commit the conjunction149 fallacy. In
one experiment conducted by Tversky and Kahneman,150 subjects were
presented with the following description:
Linda is 31 years old, single, outspoken, and very bright. She majored in philosophy. As a student, she was deeply concerned with issues of discrimination and social justice, and also participated in
antinuclear demonstrations. Which possibility is most likely? (1)
Linda is a bank teller, or (2) Linda is a bank teller AND is active in
the feminist movement.
Astoundingly, 85 percent of the subjects responded that it was more
likely that Linda was a bank teller AND active in the feminist movement
The Illusory Validity of Subjective Technical Analysis
91
--- page 93 ---

than that Linda was simply a bank teller. This conclusion ignores the logical relationship between a set and a proper subset. Subjects became so
ﬁxated on the fact that Linda possessed a set of salient characteristics that
matched an intuitive stereotype of a feminist, that they committed the
conjunction fallacy. Clearly, the set of women who are both bank tellers
and active in the feminist movement is a subset of a larger category which
contains all female bank tellers including those who are feminists and
those who are not. Other studies conﬁrmed these ﬁndings and led Tversky
and Kahneman to conclude that people’s probability judgments are biased
by the addition of salient detail. Even though each additional detail describing an object reduces the probability that such an object exists,151
when people reason by representativeness, additional detail increases the
number of characteristics that match a class stereotype, thus increasing
an intuitive estimate of probability. The conjunction fallacy is illustrated
in Figure 2.20.
The conjunction fallacy can have disastrous consequences when it
seeps into jury verdicts. For example, consider which of two possibilities
would seem more likely152:
1. The defendant left the scene of the crime.
2. The defendant left the scene of the crime for fear of being accused of
murder.
92
METHODOLOGICAL, PSYCHOLOGICAL, PHILOSOPHICAL, STATISTICAL FOUNDATIONS
B
a
n
k

T
e
l
l
e
r
s
Bank Tellers
Who Are
Feminists
FIGURE 2.20
The conjunction fallacy.
--- page 94 ---

The second hypothesis involves a conjunction of “left the scene” and
“fear of accusation.” Because the second alternative is a subset of the ﬁrst,
it is by deﬁnition less probable. Clearly, there are reasons for someone’s
leaving a crime scene other than fear of being accused, like going to pick
up the dry cleaning. However, the additional detail of the second hypothesis lends a ring of plausibility because it increases a sense of match to actions that would be representative of a guilty party.
THE REPRESENTATIVENESS HEURISTIC AND THE
ILLUSION TRENDS AND PATTERNS IN CHARTS:
REAL AND FAKE
So far the representativeness heuristic has been discussed with respect to
its use in classifying objects. In fact, the heuristic is also involved in a
more abstract type of classiﬁcation judgment that is central to the practice of subjective TA: judging that a sample of data evidences trends and
patterns and is, therefore, worthy of further analysis or alternatively that
the data is a random hodge-podge not worthy of further analysis.
Bear in mind the judgment about whether a data set appears random
or nonrandom is not made with conscious awareness or intention. It occurs as automatically and unconsciously as the judgment involved in recognizing the face of a friend. All heuristic judgments, including reasoning
by representativeness, occur automatically and without conscious awareness. As a result, when a chartist concludes that a sample of price history
contains authentic patterns and trends (i.e., that the data is nonrandom)
and is, therefore, worthy of analysis, it is not a matter of controlled thinking. That is to say, the chartist does not consciously pose the question:
“Does this data appear as if it contains exploitable order and structure.”
Although heuristic judgments slip into our thinking unnoticed, they
can have a profound inﬂuence on our beliefs. The problem is that heuristic thinking fails to take into account important features of the data that
are relevant to determining if it does contain authentic patterns and
trends that might be exploited with further analysis.
In a previous section, I asked you to create an artiﬁcial price history
(random-walk chart) by ﬂipping a coin 300 times. If you did not do so
then, I urge you to do so now. Not only will it make this section more
meaningful, it may permanently change the way you look at charts. To
quote Martha Stewart, “that’s a good thing.”
If this was your ﬁrst exposure to data generated by a random process,
you may be surprised by how nonrandom it looks. You may not have expected to see formations that look like chart patterns (head-and-shoulders,
The Illusory Validity of Subjective Technical Analysis
93
--- page 95 ---

double top, etc.). The question we must consider is this: Why does this sequence, which we know to be random in origin, give the appearance of
having authentic patterns and trends. Or, said differently, why does data
generated by a purely random process appear as if it were generated by
a process governed by rules, which, if discovered, would make prediction possible?
Your chart may have looked something like Figure 2.21.
The bottom line is this: That which appears to be nonrandom is not
necessarily nonrandom. My contention is that the perception of trends
and patterns in randomly generated data occurs because of a faulty application of the representativeness heuristic. Speciﬁcally, the heuristic creates a faulty intuitive notion of how random data is supposed to look. That
is to say, it produces a false stereotype of randomness. Thus, when we
view data that does not appear to match this false stereotype, we automatically and erroneously conclude that the data is nonrandom. From this
ﬂawed conclusion, it is a short leap to the equally false perception of patterns and the equally false notion that the patterns contain predictive
information.
One consequence of representativeness-based reasoning is the expectation that an effect should resemble its cause. This is often reasonable. The Earth (big cause) is responsible for gravity (big effect), while a
mere pebble in our shoe causes only a minor annoyance. However, the
rule that an effect should resemble its cause does not always hold. The
1918 ﬂu pandemic, a big effect, was caused by a creature of submicroscopic proportions.
How does this relate to charts of asset prices? A set of data on a chart
can be seen as an effect of a process, the activity of a ﬁnancial market.
The process is the cause whereas the data is the effect. A chart of our
94
METHODOLOGICAL, PSYCHOLOGICAL, PHILOSOPHICAL, STATISTICAL FOUNDATIONS
Time
Price
FIGURE 2.21
Data from a random process that appears ordered.
--- page 96 ---

body’s hourly temperature over a 24-hour period is an effect caused by a
process that happens to be our body’s metabolism.
Because representativeness-based thinking operates involuntarily beneath conscious awareness, when we view the chart of an asset’s price
history, we tend to draw an automatic conclusion about the nature of the
process that generated the chart. Perhaps, if stock charts looked something like the trace in Figure 2.22, the pioneers of TA would have been less
likely to see exploitable structure, and the practice of TA would never
have been born. This data is supposed to approximate an intuitive stereotype of randomness: haphazard, disorderly, and without any hint of trend.
On the basis of the representativeness heuristic, we presume that if a
process (the cause) is random, its effect (the data) should also appear random. As a consequence of this assumption, any sample of data that deviates from the presumed stereotype of randomness, because it manifests
some sense of pattern or trend, is concluded to be the product of a nonrandom process. Stock charts give the appearance of having been generated by a nonrandom process. In other words they match an intuitive
notion of order and predictability. Bear in mind that ﬁnancial markets may
indeed be nonrandom to some degree and hence be amenable to prediction. However, that is not the issue here. Rather the issue is can nonrandom structure that is amenable to prediction be detected by visual
inspection and intuitive appraisal?
As mentioned previously, the deﬁciencies of reasoning by representativeness are due to an excessive focus on obvious appearances and the simultaneous disregard of important statistical and logical features. As will
be explained in Chapter 4, one of the most important features of a sample
of data, from the standpoint of data analysis, is the number of observations
comprising the sample. Valid conclusions about a sample of data must
take the number of observations into account. Moreover, the statistical
The Illusory Validity of Subjective Technical Analysis
95
Time
Price
FIGURE 2.22
Intuitive stereotype of random data: haphazard, disordered,
nontrending.
