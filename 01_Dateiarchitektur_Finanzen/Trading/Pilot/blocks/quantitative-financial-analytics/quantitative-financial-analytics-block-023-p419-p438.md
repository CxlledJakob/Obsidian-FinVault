# Quantitative financial analytics_ the path to investment profits.pdf — pages 419–438

--- page 419 ---

This page intentionally left blank
This page intentionally left blank
This page intentionally left blank
This page intentionally left blank
--- page 420 ---

Chapter 9
Risk, Uncertainty, Utility
and Portfolio Theory
A man who seeks advice about his actions will not be
grateful for the suggestion that he maximize expected
utility.
A. D. Roy
Utility Theory
Before we can proceed with the analysis and selection of portfolios,
it is necessary to establish criteria of choice. In other words, what
attribute(s) of a particular security or portfolio of securities make(s)
it more desirable than another security or portfolio? The reader
might be tempted to suggest that return (or income or wealth —
three measures that tend to move in the same direction and are thus
used somewhat interchangeably in this discussion) is the appropriate
criterion. This statement appears to be unambiguously true in at
least two cases, which we shall now consider.
All the writers we can ﬁnd on the subject agree in one way or
another that more wealth is preferable to less, other things being
equal. Therefore, if security A promised a certain return of 20 percent, but security B promised a certain return of only 10 percent,
A would be unambiguously preferred to (in terminology used later
“is said to dominate”) B, and return would be a satisfactory criterion.
The crucial point to remember, however, is that we are discussing
certain increments to wealth.
If we now assume that the returns on the securities discussed
above are not certain but rather subject to probability distributions
397
--- page 421 ---

398
Quantitative Financial Analytics
with the mathematical expectations of 20 percent and 10 percent,
it is still possible to salvage the return criterion. To do so, we must
assume it possible to engage in an inﬁnite number of independent
trials of A and B, each trial involving an inﬁnitely small proportion
of our total wealth. The law of large numbers tells us that the
actual return will approach the expected return, A will be preferred
to B, and the expected return will be an appropriate ranking
criterion.
Unfortunately, we rarely encounter certainties or inﬁnitely divisible and replicable events in the real world. The diﬃculties involved in
the employment of the expected return criterion in other situations
are easy to illustrate. Suppose that one were oﬀered the following
options: (1) receive $1; (2) bet $100 against $102 on the ﬂip of a
fair coin; (3) bet $100,000 against $100,002 on the same ﬂip. The
expected return of each option is $1 and, by this criterion, one would
be indiﬀerent among them. Yet it seems unlikely that any real person
would be indiﬀerent as to which option was chosen. It would appear
that more reﬁned selection criteria are required.
Perhaps the most famous illustration of the limitations of the
expected return criterion is the Petersburg Paradox. The original
work on this subject was published almost three centuries ago (Daniel
Bernoulli, 1954) This article was a translation from Latin into English
by Louise Sommer. The original article appeared in the Papers of the
Imperial Academy of Sciences in Petersburg, 1738, pp. 175–192.) The
paradox can be stated as follows:
Peter tosses a coin and continues to do so until it should land
“heads” when it comes to the ground. He agrees to give Paul one
ducat if he gets “heads” on the very ﬁrst throw, two ducats if he
gets it on the second, four if on the third, eight if on the fourth,
and so on, so that with each additional throw the number of ducats
he must pay is doubled. Suppose we seek to determine the value of
Paul’s expectation (p. 31 of translation).
The expected return of this proposition is [(1/2) (1 ducat) + (1/4)
(2 ducats) + (1/8) (4 ducats) + . . . ] = (1/2 ducat + 1/2 ducat +
1/2 ducat + . . . ) = ∞
n=1
2n−1
2n
= ∞. Yet it was noted that no one
--- page 422 ---

Risk, Uncertainty, Utility and Portfolio Theory
399
would ever pay a very large sum, much less an inﬁnite sum, to play
the game. Therein lay the paradox.
Because it was apparent in this example and numerous others
that individuals were not consistent maximizers of expected wealth,
an analytical problem arose. In order to make statements and
predictions about human behavior in economic decision-making, it is
necessary to assume some consistency in goal seeking. It is especially
desirable to assume that humans act in order to maximize happiness,
satisfaction, and so on. Expected wealth had served as a satisfactory
surrogate for these goals, but its limitations became too great (as in
the above case). Instead of seeking another measurable surrogate,
the writers of the period simply identiﬁed an abstract concept,
utility, as that which everyone sought to maximize. By deﬁnition,
therefore, everyone is a utility maximizer, because the only meaning
of utility is that bundle of happiness, satisfaction, and so on that one
directs all of one’s actions toward maximizing. It then follows that
whichever course of action provides the greatest utility is the one to
be undertaken.
Unfortunately, this analysis has solved no problems. In order
to determine which course of action provides the greatest utility,
it is necessary to measure the utility. This, in turn, requires
identifying those measurable variables of which utility is a function
and specifying the function. In view of the measurement problems, it
is not surprising that early writers chose to assume that utility was
simply a function of wealth (although not a linear function — which
would obviate the advantages of identifying utility as a separate
concept).
Daniel Bernoulli approached the problem by assuming that the
same proportional additions to the initial level of wealth should have
the same absolute utility. Thus, $100,000 would have the same utility
to a millionaire as $1 to the same person when he only possessed $10.
Operationally, this approach assumes that the utility of a money gain
is a log function of the size of the gain. In general, if initial wealth (α)
is set at the origin on a utility scale, then the utility of an increase in
wealth (Θ) can be shown as a constant times log α+Θ
α . Speciﬁcally,
Bernoulli demonstrated that the value of the Petersburg game, under
--- page 423 ---

400
Quantitative Financial Analytics
these assumptions, would be √α + 1 ×
4√α + 2 ×
8√α + 4 · · · −α.
If initial wealth of the player (α) were 0, this would reduce to
√
1×
4√
2×
8√
4 · · · = 2, implying that he would be indiﬀerent between
the right to play the game and a gift of two ducats. (Bernoulli,
op. cit., p. 32.) Other indiﬀerence points were 3 for α = 10, 4
for α = 100, and 6 for α = 1000.) Bernoulli posits the following
example:
Suppose Caius, a Petersburg merchant, has purchased commodities
in Amsterdam which he could sell for ten thousand rubles if he had
them in Petersburg. He therefore orders them to be shipped there
by sea, but is in doubt whether or not to insure them. He is well
aware of the fact that at this time of year, of one hundred ships
which sail from Amsterdam to Petersburg, ﬁve are usually lost.
However, there is no insurance available below the price of eight
hundred rubles a cargo, an amount which he considers outrageously
high. The question is, therefore, how much wealth must Caius
possess apart from the goods under consideration in order that
it be sensible for him to abstain from insuring them?
If X represents his fortune, then this together with the value of
the expectation of the safe arrival of his goods is given by
100
(X + 10,000)95X5 =
20
(X + 10,000)19X.
In case, he abstains. With insurance, he will have a certain
fortune of X + 9,200. Equating these two magnitudes we get:
(X + 10,000)19X = (X + 9200)20 or, approximately, X = 5,043.
If, therefore, Caius, apart from the expectation of receiving his
commodities, possesses an amount greater than 5043 rubles he will
be right in not buying insurance. If, on the contrary, his wealth is
less than this amount he should insure his cargo (Ibid., p. 29).
There have been many interesting extensions, reﬁnements, and
contradictions of the Bernoulli analysis. It has been shown, for example, that under certain circumstances, Bernoullian utility assumptions can be used to avoid utility analysis altogether. It will be
recalled that Bernoulli suggested that decisions be made on the
basis of the expected (arithmetic mean) utility, which was in turn
based on the logs of the returns. If we assume that long-run wealth
--- page 424 ---

Risk, Uncertainty, Utility and Portfolio Theory
401
maximization is a desirable goal, then it can be shown that the
arithmetic mean of the logarithms (utilities) of returns is maximized
when the geometric mean of returns is maximized. Therefore, the
criteria of choice may in this case revert to maximization of return,
deﬁned as the geometric mean.
Bernoulli presented the case of a poor man who came into
possession of a lottery ticket promising a 50–50 chance of 20,000
ducats or nothing and asked if he would be considered unwise to sell
the ticket to a rich man for 9,000 ducats. Let us further assume that
the poor man has wealth of 1,000 ducats and the rich man 100,000
ducats. From these data, the following table may be constructed:
Future Occurences
Criterion
Ticket
Ticket
Arith.
Geo.
Strategy
Wins
Loses
Mean
Mean
Poor Man
(Hold)
2.1
0.1
1.1
0.46
(Sell)
1.0
1.0
1.0
1.0
Rich Man
(Buy)
1.11
0.91
1.01
1.005
(Don’t Buy)
1.00
1.00
1.00
1.00
Probabiltiy
0.5
0.5
The case of the rich man is fairly simple. If he wins, his return is
(100,000+20,000−9,000)/100,000 = 1.11; if he loses it is (100,000−
9000)/100,000 = 0.91. If the poor man sells the ticket, he has a
10,000 certainty; to hold the ticket then becomes a gamble which
pays a (10,000 −9,000 + 20,000)/10,000 = 2.1 return if he wins and
(10,000 −9,000)/10,000 = 0.1 if he loses. As shown in the table, the
rich man would want to buy and the poor man would want to hold the
ticket on the basis of the arithmetic mean, but the transaction would
be desirable for both on the basis of the geometric mean. Bernoulli
--- page 425 ---

402
Quantitative Financial Analytics
would claim the latter result valid from a utility standpoint and it
could also be argued the same from a long-run wealth maximization
standpoint.
A solution to the paradox was also oﬀered and published by
Bernoulli along with his own. In the solution, it was assumed that
the utility of wealth was equal to the square root of its quantity. As
such, the utility of the Petersburg game was:
1/2
√
1 + 1/4
√
2 + 1/8
√
4 + · · · =
1
2 −
√
2
,
and its value in certain money was [1/(2−
√
2)]2, or slightly less than
three ducats (Bernoulli, op. cit., pp. 32–34.).
A second solution was also suggested. In this case, it was assumed
that the utility of wealth remained constant beyond a certain point.
For argument, it was assumed that the utility of all sums greater
than 224 was the same as that of 224. The value of the Petersburg
game then became 1/2 + 1/2 + (24 times) + 1/2 + 1/4 + 1/8 + · · · =
12 + 1 = 13. The utility function implied by this solution is linear
to 224 and horizontal beyond; as such, it is bounded upward. This
is important because it can be shown that an unbounded function
(like Bernoulli’s log function) can still give an inﬁnite value. See Karl
Menger, quoted in Arrow (1971), p. 23.
On the other hand, a bounded function is probably unrealistic
and violates the assumption that more wealth is always preferred to
less. Menger’s contention has to do with the fact that the inclinations
of many people to disregard very small probabilities, very small
probability diﬀerences, and also very small amounts of money cannot
be ﬁtted into an orderly axiomatic system.
Finally, some authorities assume that the utility function is
quadratic, of the form Ux = a + bx −cx2 where a, b, and c are
constants and b and c are positive. A limitation of quadratic utility
functions is that they are not only bounded upward but, indeed, have
a maximum beyond which utility declines; it is generally assumed
that only the portion to the left of the maximum constitutes the
relevant range. A major advantage of quadratic utility functions is
--- page 426 ---

Risk, Uncertainty, Utility and Portfolio Theory
403
that they are completely consistent with the assumption that assets
are chosen on the basis of only the ﬁrst two moments about the mean
of the distribution of returns. We shall return to the signiﬁcance of
this attribute.
Von Neumann–Morgenstern Utility
Early writers on utility theory often claimed that it was possible
to measure utility on an absolute scale, whereby the joy or pain of
money gains and losses could be exactly computed and even compared among individuals. This group, identiﬁed as the neoclassical
cardinal utility theory school, was essentially discredited by the ordinal utility theory writers. The latter agreed that, through revealed
preference, it was possible to detect which goods or combinations
of goods were preferred (or were a matter of indiﬀerence) to other
goods or combinations by the individual under analysis. The point
of disagreement, however, was that the ordinalists contended that
it was impossible to say by how much one combination of goods
was preferred to another. They further insisted that interpersonal
comparisons of utility gains and losses could not be made, and that
all the writing about the absolute measurement of joy and pain (going
back to Bentham’s hedonist calculus, if not earlier) was, at best,
non-operational.
Modern cardinal utility theory dates from the work of von
Neumann and Morgenstern (John von Neumann and Oskar Morgenstern, 1944). They contend only that, given certain assumptions and
certain data about an individual’s preferences, it is possible to predict
his choices in certain risky situations. The method is called cardinal
only because it employs numbers in making these predictions; it
makes no pretense of absolute measures and has essentially nothing
in common with the earlier cardinal school.
In general, it is assumed that the individual is intelligent,
rational, and fully understands the implications of the alternatives
being presented to him. In addition, the following ﬁve axioms
must be assumed for von Neumann–Morgenstern utility calculations
--- page 427 ---

404
Quantitative Financial Analytics
to hold:
1. Transitivity. If the subject is indiﬀerent between outcomes A and
B and also between B and C, he must be indiﬀerent between A
and C.
2. Continuity of preferences. If A is preferred to B and B is preferred
to no change, there must be a probability α(0 < α < 1), such that
the individual is indiﬀerent between αA and B.
3. Independence. If A is preferred to B, then for any probability
α(0 < α < 1), αA + (1 −α)B is preferred to B. Or, viewed
another way, if one is indiﬀerent between A and B, then one is
also indiﬀerent between αA and αB.
4. Desire for high probability of success. If A is preferred to no change
and if α1 > α2, then α1A is preferred to α2A.
5. Compound probabilities. If one is indiﬀerent between αA and B,
and ifα = α1 × α2, then one is indiﬀerent between α1α2A and B.
In sum, if the outcomes of one risky event are other risky events,
the subject should act on the basis of ﬁnal outcomes and their
associated probabilities alone.
If these assumptions can be made, the analyst may then begin
to chart the utility of wealth function of his subject. The ﬁrst step
is to deﬁne arbitrarily in terms of utils (the cardinal utility unit of
measurement) two end points of the range of wealth to be tested;
it is important to use end points because the methodology is one of
interpolation but it may not be used for extrapolation. Suppose, for
example, we deﬁned $0 as 0 utils and $1 million as 1000 utils and
the following conversation ensued:
Q. How much would you be willing to pay for a lottery ticket oﬀering
a 50–50 chance of $1 ¯M or $0?
A. $250,000 [0.5 (0 utils) + 0.5 (1000 utils) = 500 U].
Q. How much would you pay for a 50–50 chance of $250,000 or
nothing?
A. $62,500 [0.5 (0 U) + 0.5 (500 U) = 250 U].
--- page 428 ---

Risk, Uncertainty, Utility and Portfolio Theory
405
U
0
W
.25m
.50m
.75m
1.0m
1000
750
500
250
Figure 9.1. Utility as a Function of Wealth (U =
√
W )
We have thus assumed two points on the utility versus wealth
graph (see Figure 9.1) and have been able to compute two more. In
so doing, and in various applications we will make of this analysis,
we have employed the expected utility maxim of von Neumann–
Morgenstern analysis:
The utility of the game (risky event) is not the utility of the
expected value of the game but rather the expected value of the utilities
associated with the outcomes of the game.
To be speciﬁc, in our ﬁrst question above, the utility of the lottery
ticket was not the utility of its expected value ($500,000) but rather
the expected value of the utilities of the two outcomes ($0 and
$1 ¯M). If the utility of the game were the utility of its expected
value, then the individual would be indiﬀerent between the lottery
and a gift of $500,000, and we would be back in the Petersburg
Paradox.
It will be noted that in the numerical example, the utility of
wealth is a square root function. In practice, of course, it is not likely
to be so well behaved. But, by asking enough lottery-type questions,
it should be possible to plot a curve and from the curve to determine
the utility associated with every wealth outcome within the relevant
range of a risky situation.
Suppose that our subject in the above example (for whom
U =
√
W) is faced with a risky situation with the possible outcomes
--- page 429 ---

406
Quantitative Financial Analytics
enumerated below:
Outcome
Probability
EV
+10,000
.3
3,000
+90,000
.5
45,000
+490,000
.2
98,000
µ = 146,000
The certain sum for which he would be willing to sell his interest
is given by:
W
U =
√
W
Probability
EU
+10,000
100 U
.3
30
+90,000
300 U
.5
150
+490,000
700 U
.2
140
320 U
W = U2 = (320)2 = $102,400.
This game possesses the same utility to the subject as a certain
$102,400.
Indiﬀerence Curves
Let us return to our subject in the last section for whom the utility
of wealth was equal to the square root of his wealth position. Again
deﬁning $0 as 0 utils and $1 ¯M as 1000 utils, we may conclude that
having $250,000 possesses (√250,000) = 500 utils for the subject,
as shown by point A on Figure 9.2. A 50–50 chance, represented
by point D, of having $90,000(√90,000 = 300 U), point B, or
$490,000(√490,000 = 700 U), point C, also provides [(0.5)(200 U) +
(0.5)(700 U)] = 500 utils for the subject. Furthermore, a 50–50
chance, represented by point G of having $10,000(√10,000 = 100 U),
--- page 430 ---

Risk, Uncertainty, Utility and Portfolio Theory
407
U
0
W
.25m
.50m
.75m
A
B
C
D
E
F
G
490,000
810,000
10,000
90,000
µA=250,000
µD=290,000
µG=410,000
1000
750
500
250
Figure 9.2. Utility as a Function of Wealth (U =
√
W), Speciﬁc Values
point E, or $810,000(√810,000 = 900 U), point F, also provides
[(0.5) (100 U) + (0.5) (900 U)] 500 utils.
Therefore, because the opportunities represented by points A,
D, and G provide the same utility, the subject should be indiﬀerent
among them. Note, however, the following diﬀerences in the expected
value and standard deviation of opportunities A, D, and G.
(1) µA = $250,000(1.0) = $250,000
σA =

(250,000 −250,000)2(1.0) = 0.
(2) µD = ($90,000)(0.5) + (490,000)(0.5) = $290,000
σD =

($90,000 −290,000)2(0.5) + (490,000 −290,000)2(0.5)
= $200,000.
(3) µG = ($10,000)(0.5) + ($810,000)(0.5) = $410,000
σG =

($10,000 −410,000)2(0.5) + (810,000 −410,000)2(0.5)
= $400,000.
--- page 431 ---

408
Quantitative Financial Analytics
600,000
400,000
200,000
0
µ
A
D
U1
U2
U3
G
250,000
290,000
410,000
Figure 9.3. Risk Averse Indiﬀerence Curves
Because we have decided that each of these three opportunities
provides equal utility let us graph them in (µ, σ) space, as shown in
Figure 9.3 as curve U2.
What we have generated, of course, is an indiﬀerence curve,
the locus of all points on the graph providing the same utility as
a $250,000 certainty. (It is possible also to derive indiﬀerence curves
from utility functions mathematically by the expansion of a Taylor
series.) Because we are depicting a three-dimensional graph (µ, σ, U)
in two-dimensional (µ, σ) space, there are an inﬁnite number of
indiﬀerence curves that could be drawn, one corresponding to each
certain sum (U1 and U3 are representative examples on Figure 9.3).
In dealing with indiﬀerence curves, it is important to remember
that: (1) each point on a given indiﬀerence curve provides the same
utility as all other points on the same curve, and (2) each point on
a second given indiﬀerence curve (for the same person at the same
time) provides a constant amount of greater (or less) utility than
each point on the ﬁrst curve.
Now observe that the indiﬀerence curves are concave and positively sloped in (µ, σ) space since dU/dW > 0 and d2U/dW2 < 0,
then dσ/dµ > 0. This implies that our subject requires a greater
expected return (µ) in order to tolerate a greater dispersion of
possible outcomes (σ) and be equally satisﬁed. Because dispersion
of possible outcomes about the mean has been deﬁned as a measure
of risk, we may say, in the popular parlance, that our subject is a
risk averter.
--- page 432 ---

Risk, Uncertainty, Utility and Portfolio Theory
409
400,000
200,000
0
µ
A
D
U1
U
W
U2
U2=500
µA,µD,µG
U3
G
E
B
A,D,G
C
E
Figure 9.4. Risk Neutral Indiﬀerence Curves
Suppose, instead of the above situation, that our subject had a
linear total utility of wealth function; this is the same thing as assuming a constant marginal utility of wealth function or that $200,000 is
exactly twice as desirable as $100,000. The resulting utility-of-wealth
function and indiﬀerence curves are given in Figure 9.4. Because the
expected utility of the outcomes equals the utility of the expected
value, all opportunities having the same expected value will have the
same utility, regardless of risk. The indiﬀerence curves are therefore
vertical, since dU/dW > 0 and d2U/dW2 = 0, then dσ/dµ = ∞.
A person possessing such a function is called risk neutral.
Finally, suppose our subject had an increasing marginal utility of
wealth function, such that $200,000 was more than twice as desirable
as $100,000. We observe, in Figure 9.5 that risky combinations
D and G provide the same utility as certainty A, but with a
lower expected value. The corresponding indiﬀerence curves for the
--- page 433 ---

410
Quantitative Financial Analytics
0
µ
A
D
D
U1
U
W
U2
U2=500
µA
µD
µG
U3
G
E
B
G
A
F
400,000
200,000
Figure 9.5. Risk-Seeking Indiﬀerence Curves
subject are concave but negatively sloped. Since dU/dW > 0 and
d2U/dW2 > 0, then dσ/dµ < 0. Such a person is called a risk
seeker.
Now that the indiﬀerence curves have been geometrically derived
from their respective utility-of-wealth functions, it becomes convenient to switch the axes in their graphs for subsequent discussion.
It will be observed that this task is accomplished in Figure 9.6,
and we shall henceforth deal with the indiﬀerence curves in (σ, µ)
space. Furthermore, we shall concentrate our attention upon the risk
averter. It has been demonstrated that the risk averter’s indiﬀerence
curves in (σ, µ) space will be positively sloped and concave from
above. The actual shape of the curves, of course, depends upon the
corresponding utility-of-wealth function.
--- page 434 ---

Risk, Uncertainty, Utility and Portfolio Theory
411
µ
µ
µ
U1
U2
U3
U1
U2
U3
U1
U2
U3
Risk Averter
Risk Neutral
Risk Seeker
Figure 9.6. Indiﬀerence Curves in (σ, µ) Space
If the utility function happens to be quadratic (U = a+bx−cx2),
it has also been shown that the indiﬀerence curves will be concentric
circles with the center at σ = 0 and µ = the value of X which
maximizes the utility function (−b/2c). The indiﬀerence curves
corresponding to other types of utility functions are not nearly so
simple to specify.
In a famous article (Milton Friedman and Leonard J. Savage,
1948.), the authors set about to rationalize the following observable
phenomena:
1. People buy ﬁre insurance, thus preferring a certain small loss
to the small probability of a large loss coupled with the large
probability of no loss. This game is undertaken at unfair odds
(the premium pays for costs and proﬁts of the insurance company
as well as loss coverage) indicating that the individual will pay a
premium to avoid risk in this range of his wealth function and is
thus risk averse.
2. The same people also buy lottery tickets or engage in other forms
of gambling, thus preferring a large probability of a small loss
--- page 435 ---

412
Quantitative Financial Analytics
0
TOTAL WEALTH
UTILITY
Figure 9.7. Friedman-Savage Utility Function
combined with the small probability of a large gain to no change in
their wealth. Because such gambles are also undertaken at unfair
odds (the house proﬁt), the behavior implied is risk seeking over
this range of the wealth function.
3. Finally, the lotteries considered in 2 are observed to have more
than one prize, implying that people would prefer a greater
probability of winning a smaller prize and thus are risk averse
at wealth levels beyond some point.
The utility function implied by such behavior is shown in
Figure 9.7.
The Friedman–Savage conclusions help to explain the tendency
of people to risk “excess” funds at unfair odds in the hope of making
a “killing.” Unfortunately, however, the risk-seeking range will diﬀer
for diﬀerent individuals and over time. As such, predictions about
behavior are almost impossible to make under this system and few
practical application have been devised.
In another famous article, some similar questions were considered
(Harry Markowitz, 1952b). The utility function he derived is shown
in Figure 9.8. Present or accustomed wealth is placed at the origin.
Small increases in wealth are shown to give increasing satisfaction
(implying risk-seeking behavior), although diminishing marginal
utility does eventually occur. In like manner, small losses are not
too bothersome.
Large losses do create large disutilities, but these tend toward a
limit below some level of loss. One possible cause of the latter is that
--- page 436 ---

Risk, Uncertainty, Utility and Portfolio Theory
413
TOTAL WEALTH
UTILITY
Present or accustomed
wealth
1
3
2
4
Figure 9.8. Markowitz Utility Function
the probability of catastrophic loss is generally so low and the cost of
insurance relatively so high that most people ignore the possibility
(for example, the likelihood of being killed in an auto accident on a
single trip to the grocery store).
As a generalization, it may be said that an individual will ignore
outcomes falling to the left of inﬂection point 1 in Figure 9.8 and
insure against those falling between points 1 and 2. Between points 2
and 3, the individual may gamble (or speculate at unfavorable odds);
if, however, he wins or loses enough to fall outside this range, he
will quit. Between points 3 and 4 (often viewed as the investment
range), the individual will show increasingly risk-averse behavior.
Beyond point 4, the risk aversion becomes rather severe, as there is
little increase in utility associated with any gain in wealth (perhaps
implying a well-diversiﬁed portfolio of treasury bills). Obviously, the
Markowitz analysis is even more diﬃcult to apply operationally than
the Friedman–Savage, even though it may be more descriptive of real
behavior than the simple models presented above.
Several diﬃculties with utility analysis remain. Utility functions
that are bounded upward (implying a zero marginal utility of wealth),
as in the alternative solution to the Petersburg Paradox, not only
violate the basic notion that more wealth is preferable to less, but
also cause risky situations to be indeterminate. As long as all the
possible outcomes of a risky event lie on the horizontal portion of
the utility function, not only is the risky event as desirable as a
--- page 437 ---

414
Quantitative Financial Analytics
certainty equal to the expected value of the risky event (which is
true for all linear utility functions) but it is also as desirable as a
certainty equal to its worst (or best!) possible outcome.
Furthermore, if the slope of the utility function becomes negative
at some point (implying a negative marginal utility of wealth), as in
the case of the quadratic, utility can be increased by throwing money
away; such pathological implications for behavior do not articulate
well with the basic rationality assumptions.
The assumptions of extreme risk aversion (corresponding to very
low or even negative marginal utilities of wealth) at high levels of
wealth do not appear to correspond terribly well to observed individual behavior. Many very rich individuals continue working well
beyond the point when one might expect that extra contributions
to wealth would produce almost no extra utility. Consider Warren
Buﬀett as an example. The entire idea that “money is merely the way
you keep score” argues against the notion of zero marginal utility.
In another vein, the history of families such as the Kennedys and
Rockefellers may indicate that the utility derived from the power
of wealth may supplant consumption requirements at high levels of
wealth. The theoretical basis of these assumptions is obscure, and
empirical justiﬁcation of them is virtually non-existent. One defense
often raised is that wealth exhibits diminishing marginal utility in the
way any consumer good does. The point ignored, of course, is that
wealth represents command over all goods and, although enough ice
cream cones may satisfy one’s craving and even cause illness beyond
a point, the application of the same logic to imply total satiation of
wants of all goods and services is not necessarily justiﬁed.
Indeed, one of the longest standing assumptions of risk aversion
seems to be in the ﬁeld of public ﬁnance, where the underlying notion
of a diminishing marginal utility of wealth is a necessary condition
to develop a normative case for progressive income taxation. Given
then that the notion of risk aversion existing at all levels of
wealth is open to some question, the idea of its increasing with
wealth (as implied by most of the standard functions introduced
in the chapter) is even more suspect. The idea of utility reaching
a maximum and thereafter declining (or even remaining constant)
--- page 438 ---

Risk, Uncertainty, Utility and Portfolio Theory
415
appears even more divorced from reality. Additional measures seem
required.
The implications of risk aversion varying over wealth levels and
especially, diminishing as wealth increases have been investigated.
A measure of local risk aversion (for small changes in wealth) r(W),
equal to the following:
r(W) = −U′′(W)
U′(W) .
The argument continues on to demonstrate that local risk aversion
is a decreasing function of wealth if and only if the premium
required to undertake any given risk declines as assets rise. It further
demonstrates that this requirement, r′(W) ≤0, is equivalent to the
condition U′′(W)U′(W) ≥[U∗(W)]2. A measure of proportional risk
aversion, r∗(W) = W × r(W) may also be introduced along with an
analysis and clariﬁcation of various functions in terms of constant,
increasing, or decreasing proportional and absolute risk aversion. One
example of constant risk aversion (the special case of no aversion) is
U(W) = f(W); an example of constant proportional risk aversion is
U(W) = f(log W).
Portfolio Theory
For the last 70–80 years, a very clear division has existed between the
work of the security analyst and that of the portfolio manager. The
analyst attempts to divide the universe of securities into three parts:
(1) underpriced (recommended purchase); (2) fully priced (recommended long-run hold); and (3) overpriced (no longer recommended).
The portfolio manager then constructs groups of securities into
recommended holdings based on risk/return characteristics. The ﬁrst
decision to be made usually involves the breakdown between stocks
and bonds; a general heuristic is to place enough of the portfolio in
bonds so that the interest payments, plus a token dividend from the
remainder in stocks, would meet the minimum income requirement
of the portfolio in all but the very worst of years. Beyond this
consideration, the ratio of bonds to stocks might also be varied
