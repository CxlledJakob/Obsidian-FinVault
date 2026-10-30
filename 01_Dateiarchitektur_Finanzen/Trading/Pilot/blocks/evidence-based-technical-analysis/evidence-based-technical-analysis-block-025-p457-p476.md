# Evidence-based Technical Analysis_ Applying the Scientific Method and Statistical Inference to Trading Signals.pdf — pages 457–476

--- page 457 ---

a long position would be taken. This more complex rule has four parameters that can be optimized: short moving-average span, long moving-average
span, rsi_max, and rsi_min. A large number of parameter combinations
are then run against the training data.
As expected, the increased complexity allows the four-parameter rule
to earn a higher return in the training data. Suppose it makes 50 percent in
the training data compared to 30 percent earned by its two-parameter predecessor. The increased performance in the training data was a predictable
consequence of the increased complexity (additional parameters). We are,
however, pleasantly surprised to learn that the four-parameter rule also
does better in the testing set, earning 20 percent versus the 15 percent
earned by the basic dual moving-average rule. When a more complex rule
performs better in the test set, it is reasonable to assume that the additional complexity successfully exploited additional systematic aspects of
market behavior.
Therefore, it’s back to the drawing board again with another attempt
to improve the rule performance with yet additional complexity. This involves new conditions with additional parameters. The new conditions
might be other ﬁlters, or they could be alternative entry signals. At each
increment in complexity, all the possible combinations of the parameter
values are evaluated on the training set and the best performing combination is then run against the test set. The process of adding complexity is
continued until performance in the test set begins to decline. This is the
signal that the boundary between underﬁtting and overﬁtting has been
crossed; the additional complexity has begun to ﬁt the noise in the training data. The optimal rule is the rule of highest complexity that did the
best performance in the test set.
What then is the purpose of the third data segment, the validation set?
Thus far, it has not been touched. The astute reader will have realized that
the performance attained by the optimal complexity rule in the test data
set is positively biased. The repeated visits to the test set to ﬁnd the rule of
optimal complexity induced a positive bias—the data-mining bias. Hence,
to obtain an unbiased estimate of the optimal complexity rule’s expected
performance in the future, we must go to the validation set. Because the
validation set was not utilized in the search for optimal parameter values
or optimal complexity, it remains untainted.
THE FUTURE OF TECHNICAL ANALYSIS
Technical analysis stands at a fork in the road. Its future depends on the
path practitioners take. The traditional path continues the nonscientiﬁc
subjectivist tradition of naive theories built on untestable propositions,
Case Study Results and the Future of TA
461
--- page 458 ---

anecdotal evidence, and intuitive analysis. The other path is the scientiﬁc
approach, which I refer to as evidence-based technical analysis (EBTA). It
is conﬁned to testable methods and objective evidence, rigorously and
skeptically examined with the appropriate tools of statistical inference.
Thus, EBTA charts a course between foolish gullibility and relentless
skepticism.
I now exercise literary license for literary effect and make the following unfalsiﬁable, forecast: Technical analysis will be marginalized to the
extent it does not modernize. There are ample precedents in the history
of science to substantiate this statement. Astrology, which gave birth to
the science of astronomy, now languishes on the periphery while its offspring thrives as the mainstream discipline.
Will TA remain on its traditional unscientiﬁc path, thus fating it to be
cast aside with other ancient practices, or will it adopt EBTA and remain
vital and relevant? The historical precedents are not favorable. The history of science suggests that few practitioners who are committed to a
given paradigm ever abandon it. This is consistent with evidence presented in Chapter 2, which established that beliefs are extremely resilient.
Studies have shown that a belief can survive a complete discrediting of
the evidence that originally gave rise to the belief. If TA were to remain on
its traditional path, it would indeed be unfortunate. I believe that this will
inevitably lead to TA relinquishing territory it originally staked to more
rigorous disciplines, such as empirical and behavioral ﬁnance.
This is not to suggest that traditional TA will lose all its fans. There
will always be consumers for the services of soothsayers and seers. Divining the future is, after all, the world’s second oldest profession.23 Some audience is assured because of a deep psychic need to reduce anxiety
provoked by the uncertainty of the future. According to Scott Armstrong,
an expert in forecasting theory, the brisk demand for the seers’ services is
most certainly not attributable to forecast accuracy. In his paper, “The
Seer-Sucker Theory: The Value of Experts in Forecasting,”24 Armstrong argues that people pay heavily for the experts’ views, despite their lack of
accuracy. What customers are really buying is an illusory reduction in uncertainty and an off-loading of responsibility onto the expert. Armstrong
refers to these consumers as suckers because of the barrage of studies
cited in his paper showing that experts’ forecasts are minimally better
than those of nonexperts. This lack of accuracy has been found to hold
true across a range of disciplines, including ﬁnancial predictions.
One seminal study cited by Armstrong is by Alfred Cowles,25 who
studied the track record of the market-guru of the early 1930s, Hamilton,
the editor of the Wall Street Journal. Despite Hamilton’s reputation
among his readers, Cowles’s study showed that, over the period 1902 to
1929, 50 percent of the guru’s forecasts of directional change were wrong.
462
CASE STUDY: SIGNAL RULES FOR THE S&P 500 INDEX
--- page 459 ---

Cowles also reviewed the predictive performance of 20 insurance companies, 16 ﬁnancial services, and 24 ﬁnancial publications, all of which produced unimpressive records. The same conclusion can be found in the
statistics provided by Hulbert’s ﬁnancial digest, which currently follows
the performance of over 500 investment portfolios recommended by
newsletters. In one Hulbert study, 57 newsletters were tracked for the 10-
year period from August 1987 through August 1998. During that time, less
than 10 percent of the newsletters beat the Wilshire 5000 Index’s compound rate of return.
Armstrong also contends that expertise, beyond a minimal level, adds
little in the way of predictive accuracy. Thus, consumers would be better off
buying the least expensive predictions, which are likely to be as accurate as
the most expensive, or investing the modest effort required to achieve a level
of accuracy that would be comparable to the most expensive experts.
Recently, there have been signs that sophisticated consumers of Wall
Street advice are unwilling to pay for traditional TA. During 2005, two of
Wall Street’s largest brokerage ﬁrms shut down traditional TA research departments.26 Whether this is a random blip or the start of a trend remains
to be seen.
Evidence-Based Technical Analysis:
The Scientiﬁc Path
Adopting a scientiﬁc approach will have immediate beneﬁts for technical
analysis. The elimination of subjective TA, either by its being reformulated
into objective testable methods or by jettisoning it altogether, would
transform TA into a legitimate scientiﬁc activity. Only ideas that are
testable would be entertained, and only those that prove themselves with
objective evidence would be admitted to its body of knowledge.
This is not to suggest that, if EBTA were to be adopted, all answers
will be clear-cut and all debate will end—far from it. Debate is part and
parcel of the scientiﬁc process. Even in the hard sciences, important questions seek resolution, but the questions are about meaningful hypotheses
that spin off testable consequences.
EBTA has limits. The major one is the inability to conduct controlled
experiments, the gold standard of scientiﬁc investigation. In a controlled
experiment, the effect of one variable can be isolated and studied by holding all other variables constant. TA is inevitably an observational science
that must look to history for new knowledge.
Technical analysis is not alone in this regard. Archeology, paleontology, and geology also rely on historical data. Nevertheless, they are scientiﬁc disciplines because they deal in testable questions and look to
objective evidence to separate useful from useless ideas.
Case Study Results and the Future of TA
463
--- page 460 ---

There are statistical procedures that can partly ameliorate the lack
of experimental controls. For example, when Fosback27 quantiﬁed the
optimism/pessimism of mutual-fund managers, he removed the confounding effect of short-term interest rates on cash reserves with regression analysis. By nullifying the powerful inﬂuence of short-term interest
rates on mutual fund cash reserves, he was able to derive an uncontaminated measure of fund manager psychology called the Fosback Index. In
a like manner, Jacobs and Levy28 used multiple regression analysis to
minimize the confounding effects of multiple variables. This allowed
them to derive puriﬁed indicators for the prediction of relative stock
performance. For example, they were able to measure the pure returnreversal29 effect, thus revealing it to be one of the most powerful and
consistent predictors of relative stock performance. In other words,
they found a TA effect that works, namely, stocks that have been weak
over the past month tend to have positive relative performance over the
following month.
Another disadvantage of not being able to conduct controlled experiments is the inability to produce new samples of data. Technical analysis researchers have one body of market history that gets used over and
over again. This contributes to the data-mining-bias problem. The more
rules one tests in a given body of data, the more likely a rule will ﬁt the
data by accident. The inability to produce new sets of observations,
which can be done in the experimental sciences, underscores the importance of using statistical inference methods that take the data-mining
bias into account.
The Expert’s Role in a
Human-Computer Partnership
I assert that the future of TA would be best served by a partnership between TA experts and computers. This is not a new prescription. I was
ﬁrst exposed to it in the writings of Felsen30 over 30 years ago, and leading
edge TA practitioners have been taking advantage of advanced data modeling and machine learning for almost as long.31 Within the past decade,
numerous articles in peer-reviewed journals have shown the value of applying advanced data-mining methods to technical and fundamental indicators. Valid objective patterns have been found.32
This partnership exploits a synergy between human experts and computers. The synergy exists because the information processing abilities of
these two entities are complimentary—computers are strong where humans are weak and visa versa. I am referring speciﬁcally to computers
armed with data mining software and humans possessing expertise in a
particular domain: TA, cytology, oil ﬁeld geology, etc.
464
CASE STUDY: SIGNAL RULES FOR THE S&P 500 INDEX
--- page 461 ---

Though it is an oversimpliﬁcation, people are inventive but computers are not. People can pose questions and hypothesize explanations that
organize disparate facts into a pattern. However, this uniquely human
ability has a dark side; it makes us gullible. Our gullibility is a consequence of a mind that evolved to be more prone to a state of belief than
an attitude of skepticism. Therefore, although we are good at proposing
ideas, like new indicators or new rules to test, we are ineffectual at the
equally important task of disposing of poor ideas. Moreover, our intellect
never evolved to interpret highly complex or random phenomena. This
shows up in our limited abilities to engage in conﬁgural thinking, the intellectual task required when combining a multitude of variables into a
prediction or judgment.
Though computers cannot invent, data-mining software allows them
to dispose of irrelevant indicators and to synthesize complex models that
can combine numerous variables into predictions. In other words, computers can engage in conﬁgural analysis. A computer’s ability to synthesize complex high-dimensional models is only limited by the amount of
data available. This constraint on predictive modeling, known as the curse
of dimensionality, was named by mathematician Richard Bellman. In
essence it says that as the number of indicators comprising a multidimensional space is increased, where each indicator is represented by a dimension, the observations populating the space become less dense at an
exponential rate. A certain level of data density is required to allow datamining software to distinguish valid patterns from background randomness. Maintaining a given level of data density as dimensions are increased
thus requires an exponentially increasing number of observations. If 100
observations meet data density requirements at the two-dimensional level,
1,000 would be required at three dimensions and 10,000 at four dimensions.
Despite this very real limitation on data mining, modern data-mining software is inﬁnitely better at conﬁgural reasoning and complex pattern detection than the smartest humans.
The bottom line is this: Computers can do what people can’t and people can do what computers can’t. It is the perfect marriage.
The Futility of the Subjective Forecaster
Despite the potential of a human-computer synergy many traditional practitioners insist on using subjective methods to derive a forecast or signal
from a multitude of indicators. They do so in the face of an overwhelming
body of evidence, that has been accumulating over the last 50 years that
demonstrates the futility of such an approach. These studies show that, for
recurrent prediction problems, across a variety of ﬁelds, subjective predictions are rarely superior to predictions based on even simple statistical
Case Study Results and the Future of TA
465
--- page 462 ---

rules (models). A recurrent prediction problem is one in which the same
type of prediction must be made repeatedly on the basis of a similar set of
information. Examples of recurring prediction problems include technical
analysis, predicting violence of prisoners being released, predicting if a
borrower is likely to default on a loan, and so on. The information set that
is available to the decision maker is a set of readings on a multitude of
variables. In TA, this would be a set of technical indicator readings. In
credit evaluation, it would be a set of ﬁnancial ratios. The task is to determine if there exists a stable functional relationship between the indicators
and the outcome that is to be predicted, to ascertain what the nature of
that relationship is, and then to combine the variables according to that
functional relationship. When the relationship is complex and involves
more than just a few factors, the decision maker is faced with a conﬁgural
thinking problem that exceeds human intellectual limits. The only choice
for the subjective expert is to fall back on intuition.
The seminal study comparing the accuracy of subjective predictions
(expert intuition) to predictions based on statistical rules (models) was
done by Paul Meehl33 in 1954. It was a review of prior studies, known as a
meta-analysis, which examined 20 studies that had compared the subjective diagnoses of psychologists and psychiatrists with those produced by
linear statistical models. The studies covered the prediction of academic
success, the likelihood of criminal recidivism, and predicting the outcomes of electrical shock therapy. In each case, the experts rendered a
judgment by evaluating a multitude of variables in a subjective manner.
“In all studies, the statistical model provided more accurate predictions or
the two methods tied.”34 A subsequent study by Sawyer35 was a meta
analysis of 45 studies. “Again, there was not a single study in which clinical global judgment was superior to the statistical prediction (termed ‘mechanical combination’ by Sawyer).”36 Sawyer’s investigation is noteworthy
because he considered studies in which the human expert was allowed access to information that was not considered by the statistical model, and
yet the model was still superior. For example, the academic performance
of 37,500 sailors in naval training school was more accurately predicted
by a model based on test scores than by judges who had access to test
scores and who had conducted personal interviews. The judges apparently gave too much weight to the nuanced information they thought they
had obtained in the personal interviews and gave too little to objective
measurable facts.
An article by Camerer37 compared the accuracy of experts’ subjective
predictions with two objective methods: the predictions of multivariate
linear models derived with regression analysis and a second method
based on a mathematical model of how the experts rendered their judgments. The least accurate predictions were the subjective judgments
466
CASE STUDY: SIGNAL RULES FOR THE S&P 500 INDEX
--- page 463 ---

made by experts. The most accurate predictions were made by the linear
regression model. Figure 9.9 was prepared from data presented by Russo
and Schoemaker38 summarizing Camerer’s results. The ﬁgure of merit
used to compare the forecasting methods was the correlation coefﬁcient
between predicted outcome and actual outcome. The correlation coefﬁ-
cient can range from 0, signifying the predictions were worthless, to 1.0
signifying perfect predictive accuracy. The prediction problems spanned
nine different ﬁelds: (1) academic performance of graduate students, (2)
life-expectancy of cancer patients, (3) changes in stock prices, (4) mental
illness using personality tests, (5) grades and attitudes in a psychology
course, (6) business failures using ﬁnancial ratios, (7) students’ ratings of
teaching effectiveness, (8) performance of life insurance sales personnel,
and (9) IQ scores using Rorschach Tests. Note that the average correlation of the statistical model was 0.64 versus the expert average of 0.33. In
terms of information content, which is measured by the correlation coefﬁ-
cient squared or r-squared, the model’s predictions were on average 3.76
times as informative as the experts’.
Numerous additional studies comparing expert judgment to statistical
models (rules) have conﬁrmed these ﬁndings, forcing the conclusion that
people do poorly when attempting to combine a multitude of variables to
make predictions or judgments. In 1968, Goldberg39 showed that a linear
prediction model utilizing personality test scores as inputs could discriminate neurotic from psychotic patients better than experienced clinical diagnosticians. The model was 70 percent accurate compared with expert
accuracy that ranged from 52 percent to 67 percent. A 1983 study showed
Case Study Results and the Future of TA
467
Correlation
Predicted
versus
Actual
1
0.9
0.8
0.7
0.6
0.5
0.4
0.3
0.2
0.1
0
–0.1
Expert
Model
1
2
3
4
5
6
7
8
9
Model
Mean
0.64
Expert
Mean
0.33
FIGURE 9.9
Predictive performance of subjective expert versus objective linear
model in nine ﬁelds.
--- page 464 ---

how poorly human experts do when the number of variables is increased.
The task was to predict the propensity for violence among newly admitted
male psychiatric patients based on 19 inputs. The average accuracy of the
experts, as measured by the correlation coefﬁcient between their prediction of violence and the actual manifestation of violence, was a poor 0.12.
The single best expert had a score of 0.36. The predictions of a linear statistical model, using the same set of 19 inputs, achieved a correlation of
0.82. In this instance the model’s predictions were nearly 50 times more informative than the experts’.
Meehl continued to expand his research of comparing experts and
statistical models and in 1986 concluded that “There is no controversy in
social science which shows such a large body of qualitatively diverse studies coming out so uniformly in the same direction as this one. When you
are pushing 90 investigations [currently greater than 15040] predicting
everything from the outcomes of football games to the diagnosis of liver
disease and when you can hardly come up with a half dozen studies showing even a weak tendency in favor of the clinician, it is time to draw a
practical conclusion.”41
The evidence continues to accumulate, yet few experts pay heed. The
most comprehensive study comparing the accuracy of experts’ predictions with those produced by linear statistical prediction models was
done by Grove and Meehl in 1996,42 which covers 136 studies. In 96 percent of these studies, the rules either outperformed or equaled the experts. In a similar study in 2000, Swets, Monahan, and Dawes compared
three methods of prediction in medicine and psychology: (1) expert subjective judgment, (2) statistical rules (models), and (3) a combination of
the ﬁrst two where the output of the statistical rule was modiﬁed by the
expert’s judgment. Their ﬁnding was consistent with prior studies, leading
to the conclusion that experts who continue to operate on the basis of
subjective judgment, are not only in error in a predictive sense but perhaps in an ethical one as well.43
From the foregoing, Hastie and Dawes44 draw the following conclusions.
1. Experts and novices make subjective judgments by relying on a relatively small number of inputs (3 to 5). Assessments of livestock
and weather forecasting are exceptions in that a larger number of
inputs is typically used. The ability to use a larger set of information can be explained by the fact that immediate and precise feedback is available, which enables the experts in these two domains
to learn. In other areas, like medical diagnosis, school admissions,
and ﬁnancial forecasting, feedback is often delayed or never available. Hastie and Dawes’s conclusion suggests why subjective technicians do not learn from their mistakes—precise feedback is not
468
CASE STUDY: SIGNAL RULES FOR THE S&P 500 INDEX
--- page 465 ---

available because of the lack of objective pattern deﬁnitions and
evaluation criteria.
2. For a wide range of judgment tasks, experts’ judgments can be explained by an additive (linear) model of the inputs.
3. Few judges use nonlinear/conﬁgural thinking to combine inputs even
though they are under the impression that they are doing so. However, when they do use conﬁgural reasoning, they tend to do it
poorly.45
4. Experts do not understand how they arrive at their own judgments.
This problem is most pronounced among highly experienced experts.
As a result, their judgments are inconsistent when given the same set
of inputs on different occasions.
5. In many domains, judges do not agree with each other when given the
same set of information. The low level of interjudge agreement says
that someone is wrong.
6. When irrelevant information is added to the set of inputs, judges become more conﬁdent although accuracy does not improve. Clearly,
they are unable to distinguish relevant from irrelevant variables.
7. There are very few judges who are demonstrably superior.
Hastie and Dawes’s conclusions have received additional support
from Tetlock,46 who evaluated predictions from experts in different ﬁelds
and compares them to relatively simple statistical models that extrapolate recent trends. Tetlock’s work, which appears to be the most rigorous
long-term study ever conducted of expert judgment in the political and
economic domains, does suggest that certain subjective cognitive styles
of decision making are superior. He calls this style the fox. However, he
shows that all human-based predictions, whatever their style, pale in
comparison to formal model-based predictions. Using a two-dimensional
framework for evaluating forecast accuracy, discrimination, and calibration, the accuracy of formal models, based on a method called generalized autoregressive distributed lags, far exceeds the performance of
human experts.47
Why Are Experts’ Subjective Predictions So Poor?
Although there is general agreement among those who study expert judgment, that it is rarely superior to objective forecasts, there is less agreement about why. A number of explanations have been proposed: the
intrusion of emotional factors, the lack of consistency in how factors are
weighted, excessive weight given to vivid concrete features that have little
Case Study Results and the Future of TA
469
--- page 466 ---

predictive power, inadequate weight given to abstract statistics that possess predictive power, the failure to use conﬁgural rules properly, falling
prey to illusory correlations, failing to notice valid correlations, and being affected by the actions and statements of others. Many of these were
covered in Chapter 2, with respect to the birth and maintenance of erroneous beliefs, and in Chapter 7, with respect to information cascades
and herd behavior, and I will not repeat them here. Here, I will consider
the intrusion of emotional factors on the subjective forecaster, which
has not been discussed in prior chapters.
A number of investigators have considered the effect of emotions on
subjective judgments made under conditions of uncertainty. One model,
proposed by Loewenstein et al.,48 suggests that a subjective forecast is
impacted by the decision maker’s anticipated emotional reaction to the
prediction’s outcome. Even though the expert’s anxieties about the
chance of being wrong have no valid role in a forecast, they appear to
play a role. Nofsinger49 presents Lowenstein’s model in a diagram that I
have reproduced in Figure 9.10. Note that when a person is making a
prediction they are impacted by anticipating their emotions in response
to the possible outcomes. This affects both the cognitive evaluation of
information and the current emotional state of the decision maker.50
Slovic, Finucane, Peters, and MacGregor51 explain the intrusion of
emotions on the subjective decision maker in terms of affect. Affect refers
to the good or bad feelings associated with a stimulus. These feelings often operate unconsciously and produce rapid reﬂex-like behaviors that
470
CASE STUDY: SIGNAL RULES FOR THE S&P 500 INDEX
Anticipated
Outcomes
Including
Anticipated
Emotions
Subjective
Probability
Assessments
Other Factors;
Vividness
Immediacy
Background
Mood
Cognition
Evaluation
Feelings
Behavior
Outcomes
(Including
Emotions)
FIGURE 9.10
Lowenstein’s model of judgment impacted by affect.
--- page 467 ---

are not under the decision maker’s conscious control. Slovic points out
that feelings and images can weigh heavily in judgments that would be
better handled by a purely analytical and rational consideration of evidence. For example, a market analyst who has negative feelings associated with a declining market is likely to remain more bullish than the
evidence would warrant. However, not all judgments based on affect are
bad. Some situations are accurately represented by the feelings they provoke and do demand the fast reﬂex-like decisions produced by this mode
of thinking. Affective decision making was probably the dominant mode
of judgment during the evolution of the human species. In other words,
the speed of affective decision making had survival value. Fear of heights
or of large predators demanded faster choices than those that a conscious
weighing of pros and cons would have been able to produce. “However,
like other heuristics that provide generally adaptive responses but occasionally lead us astray, reliance on affect can also deceive us.”52 This occurs when the relevant features of a situation are not well represented by
the feelings they stimulate. Financial market prediction is such a situation, yet the subjective forecaster remains vulnerable to the automatic
and subconscious judgments of a heuristic based on affect.
The model offered by Joseph Forgas further illuminates the futility of
subjective forecasting.53 It explains that “the greater the complexity and
uncertainty in a situation, the more emotions will inﬂuence a decision.”54
This characterizes the task faced by the subjective TA analyst who operates against insurmountable obstacles when trying to evaluate a multitude
of indicators in a rational manner. I contend that subjective forecasting is
no longer the analyst’s proper role.
The Expert’s Proper and Crucial Role
in Human-Machine Partnership
The proper role of the TA practitioner in the envisioned human-computer
partnership is twofold: (1) proposing an information-rich set of candidate inputs suitable for presentation to the data-mining software, (2)
specifying the problem to be solved by data-mining software (i.e., the
target variable. In other words, the TA expert’s proper role is to supply
what the computer lacks, namely, expertise in the domain of TA and inventive talent.
It is somewhat ironic that in this high-tech era, the analyst’s role has
now taken center stage. This is a result of the changed economics of data
mining. Within the last decade, the price of computing power and powerful data-mining software has declined sharply. Whereas these resources
had been the exclusive domain of well-ﬁnanced research organizations as
recently as a decade or two ago, today they are commodities accessible to
Case Study Results and the Future of TA
471
--- page 468 ---

almost all market participants. These trends have democratized data mining. Most investors now have access to the same tools that once gave a
huge competitive advantage to the largest institutional investors. That advantaged has been greatly diminished. Consequently, the competitive advantage—the source of added value—has now shifted back to the human
analyst. The competitive advantage now lies with those TA experts possessing the best insights with regard to proposing indicators and specifying target variables. The TA practitioner who embraces the EBTA
philosophy is well positioned to play this role.
Indicator design and target speciﬁcation is a huge topic suitable for
entire books. There are many books that cover indicators that are speciﬁc
to TA.55 There is no need to duplicate that here. There are other books that
treat the more general problem of designing inputs (predictive variables)
that are suitable for speciﬁc types of data-mining algorithms.56 Different
algorithms have different requirements. For example, although it is crucial that inputs to a neural net be properly scaled, inputs to decision-tree
algorithms need not be. Masters,57 Pyle,58 and Weiss and Indurkhya59 cover
these issues nicely.
Indicator design refers to the speciﬁcation of transformations applied
to raw market data before it is presented to the data-mining tool. Data
miners often refer to this as preprocessing. The task of proposing a list of
information-rich and properly designed candidate indicators for a datamining problem requires the domain expertise and inventive talents of the
human analyst.
Anyone who has gotten their hands dirty in the data-mining trenches
knows the following truth: a necessary condition for success in data mining is a good set of candidate indicators. Good does not mean that all inputs have to be informative. However, some of the proposed variables
must contain useful information about the target variable. According to
Dorian Pyle, a noted authority on data mining, “after ﬁnding the right
problem to solve, data preparation is often the key to solving the problem.
It can easily be the difference between success and failure, between useable insights and incomprehensible murk, between worthwhile predictions and useless guesses.”60 Dr. Timothy Masters, another data-mining
authority, says, “Preprocessing is the is the key to success . . . even a primitive prediction model can perform well if the variables have been preprocessed in such as way as to clearly reveal the important information.”61
The message is ampliﬁed by Weiss and Indurkhya, in their book Predictive Data Mining. “The greatest gains in performance are often made by
describing more predictive features (indicators). It is the human who
speciﬁes the set of features . . . and who investigates how to transform the
original features into better features.” “The computer is smart about deleting weak features, but relatively dumb in the more demanding task of
472
CASE STUDY: SIGNAL RULES FOR THE S&P 500 INDEX
--- page 469 ---

composing new features or transforming raw data into more predictive
forms . . . the composition of features is a greater determining factor in
the quality of results than the speciﬁc prediction methods used to produce
those results. In most instances, feature composition is dependent on
knowledge of the application.”62
The TA practitioner who understands data-mining methods and the
important issues in indicator design will be well positioned to play this
crucial role in the human-machine partnership of twenty-ﬁrst-century
technical analysis. With the computer as an intelligence ampliﬁer and a
scientiﬁc orientation as the mindset, the EBTA practitioner is uniquely
well positioned to push the frontiers of market knowledge forward at an
accelerated pace. Given that human intelligence is essentially unchanging,
but computer intelligence is increasing at an exponential rate,63 no other
approach to TA makes sense.
Case Study Results and the Future of TA
473
--- page 470 ---

475
APPENDIX
Proof That
Detrending Is
Equivalent to
Benchmarking Based
on Position Bias
I
n order to compensate for market bias interacting with long-short bias,
one should compute the expected return of a random system with the
same long-short bias, and subtract this bias-related return from the return of the candidate system.
The expected value of a single raw return drawn from the population
of historical raw returns is, by deﬁnition, the mean of these returns.
(A.1)
Let Pi signify the position of a trading system at opportunity i. This
will be long, short, or neutral. The expected return of a trading system in
which positions are random is:
(A.2)
The total return of the candidate system is the sum of the raw returns
at those times when the candidate system is long, minus the sum of the
raw returns when the system is short:
(A.3)
Total
R
R
i
P
Long
i
P
Short
i
i
=
−
=
=
∑
∑
E
E
E
Random
Raw
P
Long
Raw
P
Short
i
i
=
−
=
=
∑
∑
E
n
R
Raw
i
i
n
=
=∑
1
1`
Evidence-Based Technical Analysis: Applying the Scientific
Method and Statistical Inference to Trading Signals
by David R. Aronson
Copyright © 2007 David R. Aronson
--- page 471 ---

The total return of the candidate system (Equation (A.3)) is corrected
for long/short prejudice by subtracting the expectation of a similarly prejudiced random system (Equation (A.2)). Subtraction distributes over the
summation, giving:
(A.4)
Notice that the corrected return of Equation (A.4) is identical to the
uncorrected return of Equation (A.3) except that the mean of the raw returns is subtracted from each individual raw return. In other words, to remove the effect of long/short imbalance in a biased market, all you need
to do is center the raw returns.
Corrected
R
E
R
E
i
Raw
P
Long
i
Raw
P
Short
i
i
=
−
−
−
=
=
∑
∑
(
)
(
)
476
DETRENDING IS EQUIVALENT TO BENCHMARKING BASED ON POSITION BIAS
--- page 472 ---

Notes
INTRODUCTION
1. Data typically considered by TA includes prices of ﬁnancial instruments;
trading volume; open interest, in the case of options and futures; as well as
other measures that reﬂect the attitudes and behavior of market participants.
2. J. Hall, Practically Profound: Putting Philosophy to Work in Everyday Life
(Lanham, MD: Rowman & Littleﬁeld Publishers, 2005).
3. Ibid., 4.
4. Ibid., 4.
5. Ibid., 5.
6. Ibid., 5.
7. Ibid., 5.
8. Ibid., 6.
9. Ibid., 5.
10. Ibid., 81.
11. R.D. Edwards and J. Magee, Technical Analysis of Stock Trends, 4th ed.
(Springﬁeld, MA: John Magee, 1958).
12. For a complete description of Elliott wave theory see R.R. Prechter and A.J.
Frost, Elliott Wave Principle (New York: New Classics Library, 1998).
13. Any version of these methods that has been made objective to the point
where it is back testable would negate this criticism.
14. The professional association of technical analysts, the Market Technicians
Association (MTA), requires compliance with the National Association of
Securities Dealers and the New York Stock Exchange. These self-regulating
bodies require “that research reports have a reasonable basis and no unwarranted claims.” Going even further, the MTA requires of its members
that they “shall not publish or make statements concerning the technical
position of a security, a market or any of its components or aspects unless such statements are reasonable and consistent in light of the available evidence and the accumulated knowledge in the ﬁeld of technical
analysis.”
15. Some peer-reviewed academic journals include Journal of Finance,
Financial Management Journal, Journal of Financial Economics, Journal of Financial and Quantitative Analysis, and Review of Financial
Studies.
--- page 473 ---

16. Outside of academia, there has been a move to greater emphasis on objective methods of TA, but often the results are not evaluated in a statistically
rigorous manner.
17. F.D. Arditti, “Can Analysts Distinguish Between Real and Randomly Generated Stock Prices?,” Financial Analysts Journal 34, no. 6 (November/
December 1978), 70.
18. J.J. Siegel, Stocks for the Long Run, 2nd ed. (New York: McGraw-Hill, 1998),
243.
19. G.R. Jensen, R.R. Johnson, and J.M. Mercer, “Tactical Asset Allocation and
Commodity Futures: Ways to Improve Performance,” Journal of Portfolio
Management 28, no. 4 (Summer 2002).
20. C.R. Lightner, “A Rationale for Managed Futures,” Technical Analysis of Stocks
& Commodities (2003). Note that this publication is not a peer-reviewed journal but the article appeared to be well supported and its ﬁndings were consistent with the peer-reviewed article cited in the prior note.
21. P.-H. Hsu and C.-M. Kuan, “Reexamining the Proﬁtability of Technical Analysis with Data Snooping Checks,” Journal of Financial Economics 3, no. 4
(2005), 606–628.
22. R. Gency, “The Predictability of Security Returns with Simple Technical
Trading Rules,” Journal of Empirical Finance 5 (1998), 347–349.
23. N. Jegadeesh, “Evidence of Predictable Behavior of Security Returns,” Journal of Finance 45 (1990), 881–898.
24. N. Jegadeesh and S. Titman, “Returns to Buying Winners and Selling Losers:
Implications for Stock Market Efﬁciency,” Journal of Finance 48 (1993),
65–91.
25. T.J. George and C.-Y. Hwang, “The 52-Week High and Momentum Investing,”
Journal of Finance 59, no. 5 (October 2004), 2145–2184.
26. B.R. Marshall and R. Hodges, “Is the 52-Week High Momentum Strategy
Proﬁtable Outside the U.S.?” awaiting publication in Applied Financial
Economics.
27. C.L. Osler, “Identifying Noise Traders: The Head and Shoulders Pattern in
U.S. Equities,” Staff Reports, Federal Reserve Bank of New York 42 (July
1998), 39 pages.
28. L. Blume and D. Easley, “Market Statistics and Technical Analysis: The Role
of Volume,” Journal of Finance 49, no. 1 (March 1994), 153–182.
29. V. Singal, Beyond the Random Walk: A Guide of Stock Market Anomalies
and Low-Risk Investing (New York: Oxford University Press, 2004). These
results are discussed in Chapter 4, “Short Term Price Drift.” The chapter also
contains an excellent list of references of other research relating to this
topic.
30. A.M. Safer, “A Comparison of Two Data Mining Techniques to Predict Abnormal Stock Market Returns,” Intelligent Data Analysis 7, no. 1 (2003), 3–14;
G. Armano, A. Murru, and F. Roli, “Stock Market Prediction by a Mixture of
Genetic-Neural Experts,” International Journal of Pattern Recognition &
Artiﬁcial Intelligence 16, no. 5 (August 2002), 501–528; G. Armano, M.
Marchesi, and A. Murru, “A Hybrid Genetic-Neural Architecture for Stock In-
478
NOTES
--- page 474 ---

dexes Forecasting,” Information Sciences 170, no. 1 (February 2005), 3–33;
T. Chenoweth, Z.O. Sauchi, and S. Lee, “Embedding Technical Analysis into
Neural Network Based Trading Systems,” Applied Artiﬁcial Intelligence 10,
no. 6 (December 1996), 523–542; S. Thawornwong, D. Enke, and C. Dagli,
“Neural Networks as a Decision Maker for Stock Trading: A Technical Analysis Approach,” International Journal of Smart Engineering System Design
5, no. 4 (October/December 2003), 313–325; A.M. Safer, “The Application of
Neural-Networks to Predict Abnormal Stock Returns Using Insider Trading
Data,” Applied Stochastic Models in Business & Industry 18, no. 4 (October
2002), 380–390; J. Yao, C.L. Tan, and H.-L. Pho, “Neural Networks for Technical Analysis: A Study on KLCI,” International Journal of Theoretical & Applied Finance 2, no. 2 (April 1999), 221–242; J. Korczak and P. Rogers, “Stock
Timing Using Genetic Algorithms,” Applied Stochastic Models in Business
& Industry 18, no. 2 (April 2002), 121–135; Z. Xu-Shen and M. Dong, “Can
Fuzzy Logic Make Technical Analysis 20/20?,” Financial Analysts Journal
60, no. 4 (July/August 2004), 54–75; J.M. Gorriz, C.G. Puntonet, M. Salmeron,
and J.J. De la Rosa, “A New Model for Time-Series Forecasting Using Radial
Basis Functions and Exogenous Data,” Neural Computing & Applications
13, no. 2 (2004), 100–111.
31. This ﬁrm was acquired by Goldman Sachs in September 2000.
CHAPTER 1
Objective Rules and
Their Evaluation
1. A long position in a security means the investor owns the security and hopes
to beneﬁt by selling it in the future at a higher price.
2. A short position in a security means the investor has sold the security without owning it but is obligated to buy it back at a later point in time. The
holder of a short position therefore beneﬁts from a subsequent price decline,
thereby permitting the repurchase at a lower level than the selling price,
earning a proﬁt.
3. Neutral refers to the case where the investor holds no position in the market.
4. It is assumed that all market information required by the method is known
and publicly available at the time the method produces the recommendation.
5. The possibility of the time series being equal to the moving average is eliminated by computing the value of the moving average to a greater degree of
precision than the price level.
6. J. Bollinger, Bollinger on Bollinger Bands (New York: McGraw-Hill, 2002).
7. T. Hayes, The Research Driven Investor: How to Use Information, Data and
Analysis for Investment Success (New York: McGraw-Hill, 2001), 63.
8. A diffusion indicator is based on an analysis of numerous market time series
within a deﬁned universe (e.g., all NYSE stocks). The same rule, such as a
moving average cross, is applied to all the series comprising the universe.
Each series is rated as in an uptrend or downtrend, depending on its position
Notes
479
--- page 475 ---

relative to its moving average. The value of the diffusion indicator is the percentage of time series that are in an upward trend. The indicator is conﬁned
to the range 0 to 100.
9. This analysis does not make clear how many rule variations were explored
to attain this level of discrimination. As will be pointed out in Chapter 6, it is
impossible to evaluate the signiﬁcance of these ﬁndings without information
on the amount of searching that led to the discovery of a rule.
10. Many of the rules tested in this book use data series other than the S&P 500
to generate signals on the S&P 500.
11. This law of statistics is discussed in detail in Chapter 4.
12. (0.9)  0.035% – (0.1)  0.035% = 0.028% per day or 7.31% annualized.
13. (0.60)  0.035% – (0.40)  0.035% = 0.007% per day or 1.78% annualized.
14. The look-ahead bias is discussed by Robert A. Haugen, The Inefﬁcient Stock
Market: What Pays Off and Why (Upper Saddle River, NJ: Prentice-Hall,
1999), 66.
15. The percentage of fund portfolios invested in interest-bearing cash instruments such as T-bills, commercial paper, and so forth.
CHAPTER 2
The Illusory Validity of Subjective
Technical Analysis
1. J. Baron, Thinking and Deciding, 3rd ed., (Cambridge, UK: Cambridge University Press, 2000), 12.
2. This ﬁgure, redrawn by the author, is similar to and inspired by one found in
G. Gigerenzer, Calculated Risks: How to Know When Numbers Deceive You
(New York: Simon & Schuster, 2002). That book cites as the original source
of the illustration R.N. Shepard, Mind Sights: Original Visual Illusions
(New York: W.H. Freeman & Company, 1990).
3. T. Gilovich, How We Know What Isn’t So: The Fallibility of Human Reason
in Everyday Life (New York: Free Press, 1991).
4. See “Defying Psychiatric Wisdom, These Skeptics Say Prove It,” New York
Times (March 9, 2004), F1–F3.
5. Alpha refers to the capital asset pricing model term, which represents the
Y-intercept obtained by regressing the returns of an investment strategy
on the returns of a market index. It represents the portion of return that is
not attributable to the volatility of the strategy (its beta). Meritorious investment strategies have alphas that are positive to a statistically signiﬁ-
cant degree.
6. J. Murphy, Technical Analysis of the Financial Markets: A Comprehensive
Guide to Trading Methods and Applications (New York: New York Institute
of Finance, 1999), 20, where market trends are said to be clearly visible.
7. H.V. Roberts, “Stock Market ‘Patterns’ and Financial Analysis: Methodological Suggestions,” Journal of Finance 14, no. 1 (March 1959), 1–10.
8. F.D. Arditti, “Can Analysts Distinguish Between Real and Randomly Generated Stock Prices?,” Financial Analysts Journal 34, no. 6 (November/
December 1978), 70. An informal test of the same nature is discussed by
480
NOTES
--- page 476 ---

J.J. Siegel, Stocks for the Long Run, 3rd ed. (New York: McGraw-Hill,
2002), 286.
9. Gilovich, How We Know.
10. Shermer, M., Why People Believe Weird Things: Pseudoscience, Superstition, and Other Confusions of Our Time (New York: W.H. Freeman, 1997).
11. Gilovich, How We Know.
12. Ibid., 10.
13. H.A. Simon, “Invariants of Human Behavior,” Annual Review of Psychology
41 (January 1990), 1–20.
14. Shermer, Why People Believe, 26.
15. Ibid., 26.
16. C. Sagan, The Demon-Haunted World: Science as a Candle in the Dark
(New York: Random House, 1995), 6.
17. C. Sagan.
18. U. Neisser, Cognitive Psychology (Englewood Cliffs, NJ: Prentice-Hall, 1967).
19. D. Kahneman, P. Slovic, and A. Tversky, Judgment under Uncertainty:
Heuristics and Biases (Cambridge, UK: Cambridge University Press, 1982).
20. H.A. Simon, Models of Man: Social and Rational (New York: John Wiley &
Sons, 1957).
21. G.A. Miller, “The Magical Number Seven, Plus or Minus Two: Some Limits on
Our Capacity for Processing Information,” Psychological Review 63 (1956),
81–97.
22. J.R. Hayes, Human Data Processing Limits in Decision Making, Report No.
ESD-TDR-62-48, Massachusetts: Air Force System Command, Electronics
System Division, 1962.
23. The term algebraic in this context refers to the fact that numbers with both
positive and negative values are being combined.
24. This is a simple linear combination. There are more sophisticated methods
of linear combining where the variables are assigned weights (weighted algebraic sum).
25. R. Hastie and R.M. Sawes, Rational Choice in an Uncertain World: The Psychology of Judgment and Decision Making (Thousand Oaks, CA: Sage Publications, 2001), 52.
26. J.E. Russo and P.J.H. Schoemaker, Decision Traps: The Ten Barriers to Brilliant Decision-Making and How to Overcome Them (New York: Doubleday,
1989), 137. The authors cite 10 studies comparing the accuracy of intuitive
expert prediction with predictions produced by objective linear models. The
studies include prediction of academic performance, life-expectancy of cancer patients, changes in stock prices, psychological diagnosis, bankruptcy,
student ratings of teacher effectiveness, sales performance, and IQ based on
Rorschach test. The average correlation between prediction and outcome for
expert judgment was 0.33 on a scale of 0 to 1.0. The average correlation for
the objective model was 0.64. In a meta-analysis of over 100 peer-reviewed
studies comparing expert judgment with statistical rules, statistical rules
were more accurate in 96 percent of the cases. See J.A. Swets, R.M. Dawes,
and J. Monahan, “Psychological Science Can Improve Diagnostic Decisions,”
Psychological Science in the Public Interest 1 (2000).
Notes
481
