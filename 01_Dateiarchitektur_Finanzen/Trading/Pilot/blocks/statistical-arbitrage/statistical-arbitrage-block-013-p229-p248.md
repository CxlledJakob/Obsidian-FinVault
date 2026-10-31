# Statistical Arbitrage_ Algorithmic Trading Insights and -- Karen M_ Sowers; Andrew Pole -- Wiley Finance, 1, 2007 -- Wiley & Sons, Incorporated, John -- isbn13 9780470138441 -- 6b0138550172e24db7f13c932e054fb9 -- An.pdf — pages 229–248

--- page 229 ---

202
STATISTICAL ARBITRAGE
(a)
5
10
15
20
5
10
15
20
25
20
15
10
5
0
30
(b)
0
50
100
150
200
FIGURE 11.7
Cuscore identiﬁcation of trend change for noisy data: (a) time series;
(b) Cuscore
The illustration in Figure 11.7 is more dramatic than that in the
previous ﬁgure over which we were so excited. Eyeball analysis is
of little use here, serving only to generate eyestrain. The Cuscore
statistic, by stark contrast, signals a high probability of a trend
increase by time 15 and practical certainty one or two periods later.
11.3.1
Using the Cuscore to Identify a Catastrophe
In the foregoing examples, the underlying trend was constant and the
coefﬁcient β in the Cuscore statistic was set to the known value of
1.0. Unfortunately, ﬁnancial series do not come to us packaged with
a convenient quantiﬁcation of underlying rate of change. We have to
work with the raw observations. Completing the task of identifying
a catastrophe move in a spread series requires the speciﬁcation of the
underlying trend prior to the potential catastrophe. At ﬁrst thought,
one might suggest using a local average computed using an EWMA as
recommended in Chapter 3. But a chicken and egg difﬁculty becomes
apparent almost as soon as the suggestion is made. The local average,
be it EWMA or some other formulation, will be contaminated as
--- page 230 ---

Statistical Arbitrage Rising
203
soon as the catastrophe move begins. The Cuscore will be in the
impossible position of detecting a change in slope using not the new
and old slope quantiﬁcation but the new quantiﬁcation and itself.
What is needed is an estimate of the trend if no change had occurred
allowing that a change may have occurred. Since the timing of a
potential change is unknown, what can one do?
Two simple strategies have some efﬁcacy. For underlying trend
estimation in the presence of potential catastrophes, one can use a
substantial period of time, such as several multiples of the catastrophe
duration, obtained from inspection of the empirical distribution of
catastrophe moves in tradeable spreads.2 A second scheme is to
employ an estimate of the slope coefﬁcient obtained from the EWMA
ordinarily found to be sensible for the series under study. The formula
for the modiﬁed Cuscore statistic becomes:
Q =

(yt −ˆβtt)t
where ˆβt is the estimated current slope coefﬁcient. Derivation of ˆβt is
given in Appendix 11.1 where the Cuscore statistic for trend change
detection in stock prices is examined in some detail.
Operationally, the statistic works well, but there may be superior
detection procedures for early catastrophe move identiﬁcation. One
possibility (explored in Appendix 11.1) is to employ a lagged local
trend estimate to avoid the chicken and egg problem. Since it is
‘‘known’’ that catastrophe moves are identiﬁed ﬁve time-steps after
onset, it is reasonable to estimate the underlying trend by excluding
at least the ﬁve most recent series observations.
Why not lag the EWMA by more than ﬁve observations, just to
be ‘‘safe’’? (Technically, increase the probability of detecting a catastrophe move in the presence of noise when the catastrophe build-up
is ‘‘gentle’’). That is a question of the modeler’s art as well as detector performance characteristics. Signiﬁcant relevant considerations
2Identifying catastrophe moves in past data is far simpler than doing so on line. Any
candidate move can be conﬁrmed by later data before it is assigned a classiﬁcation
and employed in study of identiﬁcation and characterization rules. On-line decisions
must be made, and trading decisions taken, before such conﬁrmation is possible. Of
course, conﬁrmation is eventually possible but that is after one has made a proﬁt or
incurred a loss.
--- page 231 ---

204
STATISTICAL ARBITRAGE
as you pursue this investigation are:
■What is the distribution of differences between underlying trend
and catastrophe precursor trend?
■What is the distribution of the magnitude of catastrophic reversions?
■What is the relationship of the magnitude of catastrophic reversions to the duration of the build-up and the magnitude of the
difference between underlying trend and catastrophe precursor
trend?
■What is the set of catastrophes that is economically desirable to
capture?
■What is the cost of a false identiﬁcation of a catastrophe?
Good hunting!
11.3.2
Is It Over?
A popcorn move ﬁnishes when the spread series returns to the
(local) mean, plus a bit beyond the mean contributed by stochastic
resonance. When is a catastrophe move complete? I have most
proﬁciently answered this to date through a ﬁxed duration following
detection of a spike in the opposite direction of the development of
the catastrophe. If the catastrophe developed as an increase over the
underlying trend, as in the previous examples, then the catastrophic
change ending the move would be a sudden decrease.
I have not answered the question with the success achieved in
other areas of statistical arbitrage modeling. Whether the catastrophic
move is a single large move or a trend over several periods, the onset is
revealed by Cuscore monitoring. A second modiﬁed Cuscore statistic
is employed, recognizing the nature of the move: The underlying
trend is now the build-up of the catastrophe itself so the appropriate
estimate is based on the interval starting at the estimated onset of
the catastrophe and ending one or two periods before the latest
observation. The Cuscore is speciﬁcally looking for a spike in the
opposite direction of the catastrophe build-up; here we allow a spike
to be over one or two periods, hence the need to exclude the latest
couple of observations from the trend estimate. Including them would
put the Cuscore in an impossible position similar to that described
earlier for the catastrophe onset detection.
--- page 232 ---

Statistical Arbitrage Rising
205
Best efforts to date in specifying a bet exit rule, catastrophe over,
is a combination of the duration and magnitude of the catastrophic
move. A signiﬁcant danger is waiting too long and getting caught in
a subsequent catastrophe which negates the gains of the ﬁrst. There
is plenty of room here for improvement in modeling and trade rule
prescription.
11.4
CATASTROPHE THEORETIC INTERPRETATION
Algorithms are formulaic and primitive; there is no comparison to
human consciousness. Most traders are inconsistent and unfaithful
to their model(s). Algorithms are dumbly consistent, unimaginative.
Still, with many algorithmic interactions taking place in the market
there may be emergent behaviors, unpredictable from pure analysis
of individual algorithm to algorithm interaction.
Examine the Catastrophe surface3 shown in Figure 11.8. The
catastrophe move, a slow build-up then a sudden drop, is created by
3I chose to call the new reversion pattern the catastrophe process, rather than popcorn
2 or some other label, because it is catchy and does capture the rather different
move dynamic than is both suggested by the name and exhibited by the popcorn
process. The development of an explanatory model of investor behavior, which
might represent why the new style moves occur, is separated from the description
and exploitation of those moves. The underlying elements of algorithm-to-algorithm
interaction and growing popularity and use of trading algorithms in place of direct
human action are undisputed. They are observed facts. Stock price histories are also
incontrovertible facts. The patterns I have discerned in those histories are debatable:
There is a lot of noise in any example I could show.
Trading models built to exploit the dynamics represented by the popcorn and
catastrophe processes have undeniable track records. That is existential proof of
model efﬁcacy and supports the validity of the pattern descriptions, but it does not
prove any theory of why the patterns are the way they are. The popcorn process
has been so long established and so widely exploited at multiple frequencies that
providing a rationale has not received much attention. The rise of a new pattern
with the background of failure (in terms of economic exploitation) of the old also
does not require a rationalization. If it persists and statistical arbitrageurs begin to
discover it and churn out decent returns, once again investors will experience their
own catastrophic shift from skepticism (fear of loss) to hope (greed).
While a rationalization is not necessary for the rise of the phenomenon of
reversion by catastrophe, an understanding of market forces driving new dynamics
and a cogent, plausible theory of how those forces interact and might produce
(Continued)
--- page 233 ---

206
STATISTICAL ARBITRAGE
continuous moves through a two-dimensional space. The dimensions
correspond to a ‘‘normal’’ factor and a ‘‘splitting’’ factor in catastrophe theory parlance. At low levels of the splitting factor, variation
in the normal factor causes smooth variation in the outcome surface. At high levels of the splitting factor, movement in the normal
factor generates outcomes in two distinct regions, separated by a
discontinuity—the catastrophic jump. The discontinuity is asymmetric: Jumps ‘‘up’’ and jumps ‘‘down’’ occur at different levels of the
normal factor for a constant level of splitting factor; this is known
as hysteresis, commonly interpreted as inertia or resistance. (Figure
11.9 shows a cross-section of the catastrophe surface, parallel to
the normal axis, at a high level of splitting factor, illustrating the
asymmetric jump process.)
This is the classical description of the two-dimensional cusp catastrophe. Application to stock price development identiﬁes ‘‘avarice’’
with the normal factor and ‘‘fear’’ with the splitting factor. Consider
a movement over the surface beginning at A, with a low level of fear.
emergent patterns is necessary to promote unbiased critical attention in the formative
period. The simple catastrophe theory model presented in the text is offered as one
possible way in which identiﬁed market forces recently introduced and growing in
inﬂuence as old behaviors and interactions are supplanted might be understood. The
catastrophe model is a plausible representation of what is currently known, but it is
not a formal model from which predictions can be made. V. I. Arnold in Catastrophe
Theory acidly remarks that ‘‘articles on catastrophe theory are distinguished by a
sharp and catastrophic lowering of the level of demands of rigor and also of novelty
of published results.’’ You have been cautioned.
Arnold further remarks, ‘‘In the majority of serious applications. . . the result
was known before the advent of catastrophe theory.’’ The strong implication in
our context, despite the lapse of 20 years since Arnold wrote, is that even if the
representation and interpretation of the model presented is valid, it is probably better
(more rigorously, more convincingly) constructed using tools other than catastrophe
theory. I am, in fact, engaged in research using game theoretic tools to model
trading algorithm interactions. This work is at too early a stage of development to
report here. Finally, to quote Arnold again, ‘‘In applications to the theory of the
behavior of stock market players, like the original premises, so the conclusions are
more of heuristic signiﬁcance only.’’ My premises are rather more than heuristic,
algorithm-to-algorithm interaction and increasing dominance of algorithms and
removal of direct human interaction, and patterns discerned from stock price data
history being there for anyone to inquire of. Nonetheless, it is quite right to regard the
catastrophe model of market agent behavior as heuristic. In keeping with Arnold’s
tone, I propose to describe the model as the Tadpole theorem with the explicit
intention that it is just a little bit of Pole!
--- page 234 ---

•
A
B
C
D
normal factor (avarice)
splitting factor (fear)
FIGURE 11.8
Catastrophe surface
FIGURE 11.9
Cross-section of catastrophe surface at high level of splitting factor
207
--- page 235 ---

208
STATISTICAL ARBITRAGE
The price develops smoothly in the direction of B with increasing
avarice. As the price increases further to C (the surface is tilted
upward along the splitting factor axis) fear begins to infect participants. Eventually, fear surpasses avarice as the dominant concern
and there is a quick price pullback. What is the nature of the fear?
Simply that the divergence in price from recent local trend is not
fundamentally justiﬁed but is promoted by (algorithms’) attempts
to over-exploit buyers. (Algorithms don’t actually experience fear,
or have any experience at all, nor do they act from or demonstrate
emotion. Bear with the sloppy, informal use of descriptive language:
This is a work in progress. I have not by any means established
‘‘the’’ theory. Indeed, as you can see, I am still working on proper
explication of what I have hypothesized about the process underlying
observed price dynamics.) To repeat, algorithms have no conscious
experience. However, algorithms do encapsulate learning about price
movement dynamics (see Chapter 10), knowledge of how much is to
be given up or gained through backing away from the market, and
waiting. All this as well as information on current market moves feeds
into a calculated reaction that has the appearance of fear—pullback.
The depiction of fear and avarice factors represents the combination of participants—buyers, sellers, specialists—as represented
through their algorithms. The avarice axis measures the maximum
state of avarice affecting traders and specialists: Whoever has the
greediest sentiment of the moment dominates interactions and price
movements. In like manner, the fear axis measures the maximum
state of fear infecting participants.
As buy pressure is seen by the specialist, pennying begins. Trading
algorithms, typically with some pricing room permitted in order to
complete trades, follow the specialist up. Responding, the specialist’s
avarice increases and pennying continues (possibly picking up pace,
though the description here does not require that level of speciﬁcity).
As these interactions continue, price is moved higher until trading
algorithms determine that it is time to suspend buying: Calibrated
on much previous data to ‘‘expect’’ how much will be necessary
to complete trades, unemotional algorithms display saintly patience.
Buy pressure eases. Immediately the specialists’ avarice turns to fear.
Keeping price high will generate no proﬁt if buyers stay mute and
there is no business. Sellers share the fear. Price drops precipitously
(in comparison with the rise) to rekindle buyer interest.
--- page 236 ---

Statistical Arbitrage Rising
209
One might ask, Why not smooth decline? Because reaction
to fear is different from satisfying avarice (whether it is fear of
selling too cheaply or buying too expensively), notwithstanding algorithms. Remember that algorithms are designed and coded by people.
Patience. Wait for a signiﬁcant decline. Therefore, without intermediate activity, downward pennying accelerates and, in many cases, is
observed as a multipenny catastrophic drop.
Satisﬁed that patience has paid off, the cycle begins over again,
very likely from a starting price higher than the starting price of the
original move, as these short-term catastrophic retrenchments are
usually partial. Enthusiasm, avarice, builds again quickly and price
races ahead of the sustainable growth path. Realization sets in, fear,
and equilibrium is quickly, if temporarily, restored.
How does this description of algorithmic interaction and the
resulting behavior of stock prices relate to spreads? Directly. Stock
prices move at differential rates as they always have. The catastrophe
moves of individual stocks naturally combine to generate catastrophe moves in spreads. Dynamics are different; scaling is different.
But the basic description is identical.
11.5
IMPLICATIONS FOR RISK MANAGEMENT
A valuable risk management tool in the successful management of
many statistical arbitrage models is the so-called hurdle rate of
return. A model’s forecast function provides an explicit expected
rate of return for any contemplated bet. Managers typically specify
a minimum rate of return, the hurdle, which must be satisﬁed before
a bet is made to avoid collections of bets that are, in the aggregate,
probabilistically sure losers. In times of perceived heightened general
risk, typically exempliﬁed by increased volatility, actual or expected,
a standard practice is to raise the hurdle. This prophylactic action is
designed to avoid entering reversion bets early, while divergence is still
a strong force, thereby avoiding initial losses and, hence, increasing
return. The tactic is a broad sweep action that is appropriate when
concern is of a general increase in variation not focused on speciﬁc
market sectors or stocks. (The tactic can, of course, be directed
toward speciﬁc market sectors or other collections of stocks if there
is reason to be so concerned.)
For the popcorn process, the basic forecast function is a constant,
the value at any time being reasonably computed as an EWMA (with
--- page 237 ---

210
STATISTICAL ARBITRAGE
more sophisticated modelers employing local trend components, too,
depending on the time scale over which the move is exploited).
When the spread pops, the expected return is calculated as a fraction
of the deviation between the spread and the forecast value. When
volatility is expected to increase, the pops will be expected to increase
in magnitude; waiting for larger pops is obviously sensible. (Slow,
rather than sudden, increases in volatility are automatically managed,
feeding into dynamic recalibration of models. The scenario we are
concerned with here is an increase of sufﬁcient magnitude in a short
interval that is outside the capacity of automatic model adjustment.
That is a risk scenario rather than ordinary evolution dynamics.) The
point is that the expectation-based information is not accessible to
the model from data analysis, but it can be communicated by the
modeler.
Are the considerations of risk, sudden nonspeciﬁc increases in
volatility, any different from those just articulated when considering
catastrophe moves? At ﬁrst blush it does not appear so. Catastrophe
moves are a convergence following a divergence, so rescaling for a
spike in volatility is just as relevant as it is for popcorn (or other
reversion) models. That ﬁrst blush might be of embarrassment upon
further reﬂection. Since early 2004 when the catastrophe process
emerged as the better descriptor of local price and spread motions,
the general level of market (and spread) volatility has been historically
low (see Chapter 9). We do not have any empirical guidance on what
will happen when volatility spikes. Rescaling of local catastrophe
moves may be the result. But it could easily be something different.
A good argument can be made that increased volatility will swamp
the catastrophes, certainly sinking the ability to identify and exploit
them on line, leading to the return of the popcorn process. Is such a
development more than theoretically conceivable if the hypothesis of
algorithmic interaction driving price dynamics is and remains true?
What would cause volatility to spike? People, of course. Algorithms
are tools. Ultimately, people drive the process. We are largely in the
realm of speculation at this point. Here are a couple of further points
to guide your thinking:
■Waiting longer in a local trend: a duration criterion rather than
expected rate of return criterion. (Is there a return forecast that
can be combined?)
--- page 238 ---

Statistical Arbitrage Rising
211
■Waiting longer for a bigger build-up means fewer opportunities
and the catastrophic response is unchanged because in the catastrophe move, the reaction is not to the mean but toward an old,
not really relevant, benchmark level.
11.6
SIGN OFF
The new paradigm is as yet in an inchoate state. It is actually
two paradigms, a mix of a continued variant of the old reversion
paradigm as interstock volatility increases, and the new trend and
reversal paradigm just outlined.
Traditional interstock volatility driven reversion plays may stage
a resurgence in appeal as a source of systematic return. Rising interest rates, increasing entrepreneurial risk-taking activity, or possibly
a sudden recession-induced market scramble, are the drivers of this
potential. The potential is there but the extent of the opportunity will
be limited, returns constrained by the structural impact of decimalization, patient institutional trading (VWAP and other algorithms),
and simple competition (Chapter 9).
The promise of the new paradigm is certain. However, it is not
yet screaming—perhaps this kind of scream will only be heard, like
Santa’s sleigh bells, by believers?
APPENDIX 11.1: UNDERSTANDING
THE CUSCORE
The Cuscore statistic for detecting a change in trend was developed
by statisticians working in industrial process control where the goal is
to be alerted as soon as possible when a process requires adjustment.
An example is production of ball bearings of a speciﬁed diameter.
The target mean (diameter) is known. Samples of ball bearings are
taken sequentially and measured, the average diameter calculated and
plotted on a chart. Deviations from the target mean occur over time
as the production machine is subject to wear. Ball bearing diameters
begin to increase. A plot of the Cuscore statistic reveals the onset of
wear very quickly. (In practice, the range of diameters in the samples
would also be monitored; different kinds of machine wear create
different kinds of output variation.)
--- page 239 ---

212
STATISTICAL ARBITRAGE
In engineering applications, like the ball bearing example, the
underlying level is a known target value. Thus, in the Cuscore for
detecting a change in trend, (yt −βt)t, the slope coefﬁcient, β, is
given. As we noted in section 11.3.1, the situation with stock price
data is different. There is no target price at which one can direct
a causal mechanism (notwithstanding hopeful prognostications of
analysts). Therefore, to detect a change in price trends, an estimate of
what the trend is changing from is required. Calculating an up-to-date
estimate of what the trend is believed to be, a local trend estimate, is
the way forward. Monitoring a time sequence of local trend estimates
itself provides direct evidence about change therein.
In this appendix we examine the detail of the Cuscore for trend
change detection. The study reveals how the Cuscore works and the
problems inherent in the use of locally estimated trends. This latter is
crucial. Insight about how estimated trends affect the Cuscore is critical to successful implementation of the detector and, hence, to online
exploitation of catastrophe moves. Without timely identiﬁcation,
there is no economically desirable real opportunity.
In Figure 11.10, the line ABC is an archetype of a change of trend,
the ﬁrst segment, AB, having slope 0.5 and the second segment, BC,
having slope 1.5. The dashed line BD is the continuation of line AB.
The dashed line AE is parallel to segment BC, having slope 1.5. We
will use these straight line segments—suppose them to be noise-free
price traces to ﬁx ideas, if that helps—to demonstrate the effects on
the Cuscore statistic from different assumptions about an underlying
trend when looking for a change in that trend. Knowledge of results
in the noise-free, theoretical model will guide our expectations when
we investigate noisy price series.
The Cuscore, (yt −βt)t, is the cumulative sum of deviations
of the observation series, yt, and the expected value assuming the
slope β. In Figure 11.10, that translates into the vertical separation
of y from the line segment AD. The ﬁrst observation is that all points
on AD will generate a zero contribution to Q. If there is no slope
change, Q is identically zero.
When the slope changes, observations depart from the expected
value under the base model (of no change). Values of y along the line
segment BC exceed the expected values on line segment BD by an
increasing amount with time. Cumulating these deviations in Q we
obtain the trace labeled 1 in Figure 11.11.
--- page 240 ---

Statistical Arbitrage Rising
213
0
10
20
30
40
0
10
20
30
40
50
60
A
B
C
D
E
FIGURE 11.10
Trend change archetype and Cuscore contribution detail
Now suppose that we do not know in advance the slope of
line segments AB and BC or that there is a change in slope at B.
Suppose instead, that beginning at A, our best understanding is that
the process should exhibit a slope of 1.0 as shown by line segment
AC (not drawn to reduce clutter). The Cuscore is shown as the
trace labeled 2 in Figure 11.11. Once again, the visual appearance
of the Cuscore is startling. Deviations of a series from an assumed
base model—a difference in the slope of a trend—are made starkly
evident. This second example reveals both the occurrence of a change
(the inﬂection point in the Cuscore trace) and the information that
the series begins with a smaller slope than hypothesized and switches
to a slope larger than hypothesized.
At this point, you probably have an inkling (or more) about the
next few steps.
Review Figure 11.2. The ﬁrst three catastrophe moves compound
a strong positive trend; the subsequent moves compound a variably
declining trend. How can we operationally, in real time, provide
the Cuscore with a reasonable chance of detecting the superimposed catastrophes from the underlying, longer-term trend changes?
--- page 241 ---

214
STATISTICAL ARBITRAGE
0
10
20
30
40
−4,000
−2,000
0
2,000
4,000
6,000
1
2
FIGURE 11.11
Cuscore with β = 0 and β = 1
An answer offered in the main text is to use a local trend estimate.
Let’s examine how the Cuscore behaves when a known, constant
trend is replaced with a local estimate.
In Figure 11.12, the EWMA consistently underestimates the real
series; that is a well known feature of moving averages, weighted or
otherwise, which are not designed to project a persistent trend. The
Cuscore reﬂects the ‘‘always trying to catch up’’ condition showing
an increasing value from the beginning of the series. The slope change
is captured, the rate of increase in the Cuscore is picking up, but
the strength of inference is slow to build compared with the Cuscore
using a known constant trend. The slowness problem comes directly
from the use of the EWMA after the slope change. In Figure 11.12,
the Cuscore contributions are the differences between the new slope
and the projected old slope (vertical differences BC–BD) exempliﬁed
by p −q. With an estimated level, the projection of the initial trend
AB to BD generating p −q is replaced with the EWMA generating
the much smaller deviance p −r. This is the chicken and egg problem.
We need to project the early trend beyond the change point, which is
unknown, to quickly detect that change point!
--- page 242 ---

(a)
0
10
20
30
40
0
10
20
30
40
0
10
20
30
40
50
60
A
B
C
D
p
q
s
r
EWMA
lagged EWMA
(b)
0
500
1,000
1,500
FIGURE 11.12
(a) Cuscore contributions using local mean and (b) Cuscore using
local mean
215
--- page 243 ---

216
STATISTICAL ARBITRAGE
Updating the local mean estimate after the slope change reduces
the sensitivity of the Cuscore to detect that change. This suggests that
sensitivity might be recovered by delaying the local mean update.
What happens if a lagged local mean estimate is used in the Cuscore?
Returning to Figure 11.12, the Cuscore contribution postchange
increases from p −r to p −s, much nearer to the desirable p −q.
Unfortunately, this move does not eliminate the chicken and egg
problem; it simply relocates the henhouse! While the postchange
contributions to the Cuscore are indeed larger, so are the prechange
contributions. Thus, accurately distinguishing a change in the Cuscore trace is not more easily accomplished: Premature signaling
may be the frequent result. Reducing the lag—we used ﬁve periods
because analysis of a catalog of identiﬁed catastrophe moves in price
histories strongly suggested that most such moves with subsequent
economically exploitable catastrophe retrenchments are identiﬁable
ﬁve periods into the move—might help, but as soon as we move
from noiseless archetypes to noisy real data, the situation returns to
nearly hopeless.
What we are searching for is something in the data that quickly
and consistently registers a substantive change following the trend
change. In Figure 11.12 the EWMA trace responds quickly to the
trend change. Perhaps an estimate of local trend from the EWMA
might be a sensitive diagnostic? Figure 11.13 shows the estimated
slope coefﬁcient computed as the average change in the EWMA over
the most recent four periods:
ˆβt = 0.25(EWMAt −EWMAt−4)
This estimate shows none of the tardiness of the EWMA-based
Cuscore. Unfortunately, as soon as even modest noise is added to the
original series, the slope coefﬁcient estimate deteriorates considerably
as a sensitive diagnostic, though the sensitivity is greater for a longer
window when the underlying trend is constant other than at the point
of focus here, as shown in Figure 11.14.
At this point we have two candidates for trend change detection,
the Cuscore using a local mean estimate (EWMA) and local slope
coefﬁcient estimates based on the EWMA, each of which looks
somewhat promising. The Cuscore signals the change but is tardy,
the slope signals the change but is also tardy when noisy data is
--- page 244 ---

Statistical Arbitrage Rising
217
0
10
20
30
40
0.0
0.5
1.0
1.5
FIGURE 11.13
Estimated slope coefﬁcient, ˆβt = 0.25(EWMAt −EWMAt−4)
examined. Perhaps combining the two might amplify the result?
What do two ‘‘tardies’’ make? Before we reveal that, let’s review
the collection of Cuscore statistics examined so far. Figure 11.15
demonstrates the collection of Cuscore statics introduced in this
appendix applied to the noiseless trend change series. Qtheo is the
original Cuscore in which the initial trend is known. Qmm is the
Cuscore using a local mean estimate (EWMA), Qmmlag is the Cuscore
using a lagged local mean estimate, Qb1 is the Cuscore using a locally
estimated slope, Qb1lag is the Cuscore using a locally estimated slope
from the lagged local mean, and Qbtrue is the Cuscore using the actual
before and after change slope coefﬁcients. That’s a lot of Cuscores!
Qtheo and Qbtrue are theoretical benchmarks we would like an
operational Cuscore to approach as closely as possible. Qbtrue is
singularly interesting. Return for a moment to Figure 11.10. Qbtrue
cumulates deviations from the known line segment AB, so the value
is identically zero for t = 1 through t = 20. At t = 21 we switch from
the old slope coefﬁcient β = 0.5 to the new slope coefﬁcient β = 1.5
and thence begin cumulating deviations between observations on line
--- page 245 ---

(a)
0
10
20
30
40
0
10
20
30
40
0
10
20
30
40
50
60
observation series
EWMA
(b)
0.0
0.5
1.0
1.5
FIGURE 11.14
(a) Trend change with noise; (b) estimated slope coefﬁcient,
ˆβt = 0.25(EWMAt −EWMAt−4)
218
--- page 246 ---

Statistical Arbitrage Rising
219
0
10
20
30
40
Qmmlag
Qtheo
Qmm
Qb1lag
Qb1
Qbtrue
−1,500
−1,000
−500
500
1,000
1,500
0
FIGURE 11.15
Cuscores for several models
segment BC and the line AE, which is the new base model, assuming
gradient β = 1.5 from inception.
AE is parallel to BC (both have gradient β = 1.5) so the growth
of Q is linear as the deviations are constant. This contrasts with
the standard Cuscore in which the individual deviations increase
sequentially (excluding noise) and, hence, the cumulative sum grows
faster than linearly (Qtheo). Qbtrue has the initial advantage over Qtheo
because the deviations begin large, hence, the speed of detection of
change is faster. The advantage is a function of the relative size
of the two gradients and the time origin of the cumulation—the
duration of segment AB. In our task of identifying catastrophes, the
larger the prechange duration, the greater the discrepancies (AE–BC)
feeding the Cuscore, the greater the initial advantage over the standard Cuscore and, therefore, the sooner the likely identiﬁcation of a
trend change. Which of the noisy sample versions of the theoretical
benchmarks, Qb1 or Qmm, dominates in practical catastrophe identiﬁcation depends on the dynamics of the catastrophes and precursor
periods.
Earlier we remarked that Qtheo and Qbtrue are theoretical benchmarks that we would like an operational Cuscore to approach as
--- page 247 ---

220
STATISTICAL ARBITRAGE
0
10
20
30
40
−10,000
−8,000
−6,000
−4,000
−2,000
0
Qb
Qbtrue
^
FIGURE 11.16
Cuscores for noisy data
closely as possible. Remarkably Qˆb, our ‘‘product of two tardies’’
Cuscore, achieves an impressive standard of closeness with noiseless data. How is this possible? It is because larger discrepancies
between the observation and the estimated local mean (because of
the laggardly performance of the EWMA in the presence of sustained
trending) are multiplied by a larger estimated slope following the
change. The efﬁcacy of the Cuscore is not so much the result of two
tardies but of two enhanced discrepancies focused on a speciﬁc type
of change. Does the scheme really work with price data? Look at
Figure 11.16 and decide. And then think about how one might detect
decreases in trend.
The presentation in this appendix is rather informal. For a rigorous treatment of dynamic modeling and identiﬁcation of change,
see Pole et al, 1994. In that reference, the linear growth model provides explicit parameterization of a local mean and trend (growth),
dynamic updating of parameter estimates and forecasts, and formal
statistical diagnostics for parametric (slope, in our case) change.
The standard distributional assumptions of the DLM are strictly not
appropriate for stock price data, largely because of notable nonnormality of (normalized) price and return distributions. Nonetheless,
the models are useful if one takes a robust view of the formalities,
--- page 248 ---

Statistical Arbitrage Rising
221
concentrating on mean estimates, using standard deviations as a
guide to uncertainty, and not counting on normality at all (so-called
Linear Bayes methods).
Happy catastrophe hunting!
M01
Digitally signed by M01
DN: cn=M01, c=US
Date: 2008.06.14
23:39:33 -04'00'
