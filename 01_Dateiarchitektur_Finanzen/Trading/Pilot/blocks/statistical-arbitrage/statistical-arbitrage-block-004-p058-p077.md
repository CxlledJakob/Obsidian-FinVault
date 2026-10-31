# Statistical Arbitrage_ Algorithmic Trading Insights and -- Karen M_ Sowers; Andrew Pole -- Wiley Finance, 1, 2007 -- Wiley & Sons, Incorporated, John -- isbn13 9780470138441 -- 6b0138550172e24db7f13c932e054fb9 -- An.pdf — pages 58–77

--- page 58 ---

Statistical Arbitrage
31
Immediately, a question arises: Is market impact not subsumed in
the construction of the forecast function? Superﬁcially only. There is
an implicit assumption that the stocks can be traded instantaneously
at the current price. Okay, but why should the time delay to complete
a physical trade result in a cost? Should we not expect that some
prices will go with the desired trade and some against, with everything averaging out over numerous trades on many days? Again,
superﬁcially only. Our participation in the market is not accounted
for in the model building process. A buy order from us adds to
demand, dragging up price; the opposite for a sell order. Thus, our
own trading introduces a force against us in the market. So our
forecasts are really only valid providing we do not act on them and
participate in the market.
One might ask that, since the goal is to build a forecast model that
is exploitable, why not include the information that the forecasts will
be traded into the model building? The short—and probably also the
long—answer to that is that it is just too difﬁcult. (Equivalently, the
necessary data is unavailable; see Chapter 10 for what is possible,
even routine for a select few, at present.) The pragmatic expedient is
therefore to build a forecast that is expected to be valid if we remain
a passive observer, then make an adjustment for the effect our active
participation is likely to have.
Market impact is a function of what we decide to trade. Denoting the current portfolio by c, the objective function is extended
generically to:
p′f −market impact(p −c) −kp′p −λp′l −λ1p′l1 −· · · −λqp′lq
Determining the functional form of ‘‘market impact’’ is an unsolved
research problem for most participants because of inadequate data
(typically restricted to one’s own order and ﬁll records) and, in some
cases, lack of motivation. Again, see Chapter 10 for more recent
developments.
2.5.3
Risk Control Using Event Correlations
In the preceding section we explored the idea of event correlations
as a basis for identifying collections of stocks that existentially share
common risk factors: Stocks repeatedly exhibit directional price
--- page 59 ---

32
STATISTICAL ARBITRAGE
change at the same time, in the same orientation, and move by a
similar amount between such changes. Within a group, stocks have
similar elasticity to news or what one might call ‘‘event betas.’’
Building a portfolio that is matched dollar-for-dollar long and
short from dollar-matched portfolios built from groups of stocks
characterized by similar event betas automatically incorporates substantial risk control. Each group deﬁnes a collection of stocks that
have repeatedly exhibited essentially the same price reaction to economic developments meaningful for those stocks. The key feature
here is the repeated nature of the moves. To bowdlerize Ian Fleming,2
once is happenstance, twice is coincidence, the third time is common
risk exposure. A portfolio thus formed has a low probability of
experiencing large loss generating disparate moves of constituent
stocks in response to a market shock. After the terrorist attacks on
the United States in 2001, event beta–neutral portfolios of large
capitalization stocks exhibited only mundane volatility in valuation despite the dramatic market decline and spike in individual
stock volatility.
2.6
DYNAMICS AND CALIBRATION
The reversion exploitation model is applied to local data. For
example, estimated interstock volatilities are calculated using a
weighting scheme, discounting older data (see Chapter 3). In the
trade rules examined earlier in this chapter, we chose a 60-day
ﬁxed-length window and computed trade limits on spreads as a
function of the spread range (a) directly, and (b) using the empirical
standard deviation of the spread distribution. These daily updated
estimates adjust current trade entry and exit points. Similarly, daily
updated liquidity estimates modify trade deal size and portfolio concentration. Thus, even with an unchanged model there is continuous
adaptation to local market conditions.
Occasionally the model is recalibrated (or a manager ‘‘blows
up’’). Recall the CAL–AMR spread, which changed radically from
$20 in 2000 to $6 in 2002.
2Spoken by Auric Goldﬁnger to James Bond in Ian Fleming’s Goldﬁnger.
--- page 60 ---

Statistical Arbitrage
33
The techniques of evolutionary operation (EVOP) can be
employed to help uncover persistent changes in the nature of the
reversion phenomenon exploited by a model. Reversion is exhibited
by stock price spreads on many frequencies (Mandelbrot, fractal
analysis), one of which is targeted by a modeler’s chosen calibration, that choice being dictated by factors including robustness of
the response to small changes in parameter values, modeler’s preference, research results, and luck. Applying EVOP, several other
frequencies (model calibrations) are monitored in tandem with the
traded model to provide information on changes in the nature of the
response across frequencies. There is always noise—one frequency
never dominates nearby frequencies in terms of actual and simulated
trading performance month after month. It is crucial to understand
the normal extent of this noise so that apparent (recent) underperformance by the traded model vis-`a-vis a nearby (in model space)
competitor model is not misinterpreted as a need for a model change.
There is also evolution. Over several years, trends in the reversion
response as revealed through comparative model performance stand
out from the local variation (noise). When identiﬁed, such a trend
should be adapted to—the traded model calibration revised.
Analysis of a classic pair-trading strategy employing a ﬁrst-order,
dynamic linear model (see Chapter 3) and exhibiting a holding
period of about two weeks applied to large capital equities shows a
fascinating and revealing development. In March 2000 a trend to a
lower frequency that began in 1996 was discovered. First hinted at in
1996, the scale of the change was within experienced local variation
bounds, so the hint was only identiﬁable later. Movement in 1997 was
marginal. In 1998, the problems with international credit defaults
and the Long Term Capital Management debacle totally disrupted
all patterns of performance making inference difﬁcult and hazardous.
Although the hint was detectable, the observation was considered
unreliable. By early 2000, the hint, there for the fourth consecutive
year and now cumulatively strong enough to outweigh expected
noise variation, was considered a signal. Structural parameters of
the ‘‘traded’’ model were recalibrated for the ﬁrst time in ﬁve years,
a move expected to improve return for the next few years by two
or three points over what it would otherwise have been. Simulation
for 2000–2002 signiﬁcantly exceeded that expectation as market
developments caused a decline in performance of higher frequency
--- page 61 ---

34
STATISTICAL ARBITRAGE
compared with lower frequency strategies. See Chapter 9 for a
detailed discussion of the issues involved.
2.6.1
Evolutionary Operation: Single
Parameter Illustration
Evolutionary operation for a single parameter is illustrated in the four
panels of Figure 2.9. Panel (a) shows an archetypal response curve:
For a range of possible values for a model coefﬁcient, the (simulated)
return from operating the strategy shows a steady increase tailing off
into a plateau then quickly falling off a cliff. One would like to identify
the value of the parameter for which return is maximized—and that is
simple when analyzing past data and when the response relationship
is invariant.
Panel (b) illustrates what one observes in practice. Every year
the response is different. Similar—that is why strategies work more
often than not—but different. When selecting a parameter value at
which to operate a strategy, it is critical to understand both the form
of the response curve and the natural amount of variation and relate
these to understanding of the phenomenon under study—reversion
in this case—when it is available. Picking the return-maximizing
value of the parameter from panel (a) is risky because in some years
the response curve shifts sufﬁciently that model performance falls off
the cliff. Risk management operates at the model calibration stage,
too: Back away from the cliff and settle for generally good years and
low risk of a catastrophe rather than occasional outstanding years
and occasional disasters. One should expect that disasters will occur
from uncontrollable factors: Admitting large probabilities of disaster
from ‘‘controllable’’ factors is not a sound risk management policy.
Panel (c) shows an archetypal evolution in response: The general
form moves smoothly through space over time (and the form may
itself smoothly change over time). In practice such evolution, when
it occurs, occurs in conjunction with normal system variation as
just seen in panel (b). Experience is thus like a combination of the
movements in panels (b) and (c), illustrated in panel (d).
As the response curve changes over time, a range of the parameter
space consistently yields good strategy performance. Every year is
different and over time the parameter range to aim for gradually
moves. The original range continues to deliver reasonable performance, but becomes less attractive over several years. Evolutionary
--- page 62 ---

Statistical Arbitrage
35
(a)
(b)
(c)
(d)
1
2
3
4
FIGURE 2.9
Evolutionary operation: detecting sustained system response change
operation, the continual monitoring of system performance away
from the currently believed best calibration, enables one to identify
transient and persistent system response changes. Transient changes
provide information to update the view of normal system response
--- page 63 ---

36
STATISTICAL ARBITRAGE
variation; enduring system response changes can be adapted to,
improving long-term system performance.
As just exempliﬁed, evolutionary operation monitoring looks
beguilingly simple—and, indeed, the concepts and rote application
are straightforward. Unsurprisingly, reality is more complex. The
time scale and timing of change may differ from the annual focus
explicitly used here. And, of course, models are typically deﬁned by
a collection of parameters, not just one.
Years are somewhat artiﬁcial and arbitrary time periods in this
monitoring context. Change can occur abruptly within a calendar
year (September 11, 2001) or slowly over one or more years. Monitoring aspects of a strategy that reveal diagnostic information at
different frequencies is another critical task.
Statistical arbitrage models have several critical deﬁning parameters. The monitoring scheme is complicated because there are
interaction effects: The impact of a change in one parameter depends
upon the settings of other parameters. The scheme of continual assessment of the performance of alternative model calibrations must be
designed to reveal changes in those interactions as well as changes in
the direct response of strategy performance to individual parameters.
More complicated models that involve several steps of analysis formally may include hundreds or even thousands of estimated
parameters. Conceptually, the monitoring problem is ostensibly the
same: One is looking for evidence of change other than transient
noise over time. The practice is yet more complicated than for models with handfuls of parameters because these high-parameter-count
models often lack manageable interpretability of individual parameters. Answering the question, ‘‘What does change X in parameter
θ signify?’’, is impossible. Indeed, with such models even positing
the question is difﬁcult. Groups of parameters may have a collective
interpretability in which case understanding can be built component
by component, sometimes with a hierarchical structure.
To close this section, it is worth reiterating an important point:
Underpinning monitoring activity, from mechanics to interpretation
to action, is understanding of the phenomenon being exploited—why
it exists, what drives the opportunities, and how exploitation works
in the context of the model.
--- page 64 ---

CHAPTER3
Structural Models
Private information is practically the source of every large
modern fortune.
—An Ideal Husband, Oscar Wilde
3.1
INTRODUCTION
T
he discussion in Chapter 2 is couched largely in terms of trading
rules based on estimates of spread ranges calculated on moving
windows of data history. Figure 3.1 shows the bands calculated as
mean plus or minus one standard deviation using a window of 60
days for the CAL–AMR spread. (Compare this with Figure 2.4,
wherein the limits are calculated using the maximum −20 percent
range and minimum +20 percent range over a 60-day window, and
review the discussion in Section 2.2.) Implicit in these trading rules
is a forecast that the spread will in the near future return to the local
mean. Figure 3.2 shows the CAL–AMR spread again, this time with
the implied forecast function.
In formal terms the point forecast, or expected value, for every
future time period is the currently estimated mean value. Now it is
not really believed that the spread will actually equal the mean each
time period, or even one time period in the near future. (Obviously
the trading rules anticipate systematic variation above and below the
mean.) It is simply that the best guess based on using the moving
average model is that in the near future, the spread will likely exhibit
values centered on the mean. How near is ‘‘near’’ remains, like so
much else, unspeciﬁed.
37
--- page 65 ---

38
STATISTICAL ARBITRAGE
2000
2001
2002
2003
2004
−10
−5
0
5
10
15
20
25
$
Spread
Upper Trade Boundary
Lower Trade Boundary
FIGURE 3.1
Daily closing spread, CAL–AMR, with standard deviation trade
boundaries
The mean plus or minus standard deviation trading rules were
not compiled by formal statistical model building. Rather, simple
eyeballing and a little thinking lead to the hypotheses, expressed as
trade rules, which turned out to work satisfactorily. Nonetheless,
the rules constitute a model with the forecast function interpretation
just cited.
The CSFB tool, mentioned in Chapter 2, goes a little further than
our eyeballing and systematically searches through many alternative model speciﬁcations—window length and number of standard
deviations for trade entry boundaries. This model ﬁtting or selection
procedure implicitly uses a utility maximization criterion, maximize
simulated trading proﬁt, instead of a statistical estimation procedure
such as maximum likelihood or least squares. That is a sophisticated
approach, unfortunately undermined by the sole focus on in-sample
calculations. Effectively, the utility function is misstated for the purpose of identifying models that might be expected to do somewhat
reasonably in practice. What is really of interest is maximizing proﬁt
out of sample with some regard to draw-down limits, mimicking
--- page 66 ---

Structural Models
39
2000
2001
2002
2003
2004
−10
−5
0
5
10
15
20
25
$
Spread
Moving Average
FIGURE 3.2
Daily closing spread, CAL–AMR, with moving average forecast
function
actual use of divined trading rules, but those considerations begin to
take the tool in the direction of a strategy simulator, which is not
likely to be offered free of charge.
3.2
FORMAL FORECAST FUNCTIONS
The value of thinking about a formal forecast function is that it
gives a speciﬁc set of values to compare to realizations and thereby
to judge the efﬁcacy of model projections. Mark to market losses
on a trade will indicate the presence of a potential problem; the
pattern of forecast–outcome discrepancies provides information on
the possible nature of the problem. Such information admits a richer
set of responses to loss situations than a blunt stop loss rule such as
a simple percentage loss.
In this chapter, we will consider a few of the structurally simplest
classical models for time series data. One or two non–time-seriesmodel architectures will also be described illustrating somewhat more
involved modeling of stock price data.
--- page 67 ---

40
STATISTICAL ARBITRAGE
3.3
EXPONENTIALLY WEIGHTED MOVING AVERAGE
Moving average, or MA, models are familiar from Chapter 2. A
more ﬂexible scheme for local smoothing of series is the exponentially
weighted moving average, or EWMA. In contrast to the ﬁxed window
of data with equal weights of the MA, the EWMA scheme applies
exponentially declining weights to the entire data history. Recent
data thereby have the most inﬂuence on the current estimate and
forecasts, while large events in the remote past retain inﬂuence. The
form of the projected forecast function (for k = 1, 2, 3, . . . , n steps
ahead) is, like that of the MA, a straight line. The value is different,
however. An EWMA is computed recursively as:
xt = λxt−1 + (1 −λ)yt−1
where yt is the observation at time t, xt is the EWMA estimate, and
λ is the discount factor. The size of the discount factor 0 ≤λ ≤1
dictates how fast older observations become irrelevant to the current
estimate (equivalently, how much data history contributes to the
current estimate).
The recursive form of the EWMA forecast calculation immediately reveals a simpliﬁcation over MA schemes. Only the current
forecast xt needs to be retained to combine with the next observation for updating the forecast. While computers don’t care whether
one or twenty or ﬁfty pieces of information have to be retained in
memory, people do. In fact, the moving average can be expressed
in a recursive fashion that requires only two pieces of information
to be carried so the efﬁcient memory support is unfairly hijacked
by EWMA. Much more compelling are the advantages demonstrated
below; once familiar with exponential smoothing for forecasting, you
will want to consign your moving average routines to the ‘‘obsolete’’
folder.
Figure 3.3 shows the CAL–AMR spread with EWMA(0.04) and
MA(60) forecast functions. The EWMA discount factor, 0.04, was
selected speciﬁcally (by eye—a formal closeness criterion such as
minimum mean square could have been employed but this context
simply doesn’t require that degree of formalism) to give a close match
to the 60-day moving average. Only when the raw series (the spread),
changes dramatically, do the two forecast functions differ by an
--- page 68 ---

Structural Models
41
2000
2001
2002
2003
2004
−10
−5
0
5
10
15
20
25
$
EWMA(0.04)
MA(60)
FIGURE 3.3
CAL–AMR spread with EWMA and MA forecast functions
appreciable amount. Table 3.1 gives EWMA discount factors that
produce similar local mean estimates to a range of moving averages
(for ‘‘well behaved’’ data series).
The utility of the EWMA’s ﬂexibility is starkly apparent in two
situations where reversion plays fail: step changes and trends in
spreads. Figure 3.4 illustrates the situation where a spread suddenly
narrows and subsequently varies around the new, lower mean value.
The mean and standard deviation bands (using a 20-day window)
indicate that the long bet entered on September 7 incurred a large
TABLE 3.1
EWMA–MA
equivalences
MA(k)
EWMA(λ)
10
0.20
30
0.09
60
0.04
--- page 69 ---

42
STATISTICAL ARBITRAGE
6
13
20
27
3
10
17
24
31
7
14
21
28
5
12
Jul
Aug
Sep
2001
−10
−5
0
5
10
15
20
$
EWMA
MA
Spread
Upper Trade Boundary
Lower Trade Boundary
FIGURE 3.4
Level change in spread and MA-EWMA forecast functions
mark to market loss, $11, at the time of the spread decrease and
eventually the bet closed at a loss of that magnitude on October 11
(assuming a popcorn process model). Using the EWMA instead of
the MA is of negligible difference. The ﬂexibility advantage shows
up as soon as we introduce forecast monitoring and intervention.
When the large forecast error occurs (the day of the unusual
spread decrease) the monitoring system is triggered, alerting the
modeler to a potential violation of model assumptions, and hence,
invalidating the forecasts. Upon further investigation, the modeler
might discover a fundamental reason for the spread behavior, which
might lead to a decision to terminate the trade. (No search was
necessary on September 17, 2001 but decisions on whether to hold or
exit bets were critical to manager performance.) Figure 3.5 illustrates
a forecast function in which the historical development of the spread
is discarded in favor of a single new observation. Forecast uncertainty
would typically be large, illustrated by the wide limits.
If no information is discovered, a reasonable action is to watch
closely how the spread develops over the next few days (still looking
--- page 70 ---

Structural Models
43
−10
−5
0
5
10
15
1
29
1
33
1
37
1
41
1
45
1
49
1
53
1
57
1
61
Observation
Forecast
Forecast Uncertainty
FIGURE 3.5
Intervention forecast function
for fundamental news, of course). If the spread begins migrating
back to the pre-shift range, then no action is necessary. If the spread
continues to move around the newly established level, then the
model forecasts can be improved by introducing that knowledge
to the model. With the EWMA it is straightforward to make the
adjustment. By increasing the discount factor for just one period,
giving more weight to recent spread values, the forecasts quickly
become centered around the newly established level, as shown in
Figure 3.6. Judgments of the value of the open bet, and of new bets,
are improved much sooner than otherwise. The open bet is exited
sooner, on September 21, still at a loss but the capital is freed up and
the position risk eliminated. Proﬁtable new bets are quickly identiﬁed
which, without the adjustment, would have been missed while the
routine model played catch up: September 27 through October 2 and
October 8 through October 10 for a combined gain of $3.64.
Forecast monitoring and model adjustment are also feasible
with the MA model but the practicalities of the adjustment are
considerably more awkward than the one-time use of an intervention
discount factor in the EWMA. Try it and see!
--- page 71 ---

44
STATISTICAL ARBITRAGE
−10
−5
0
5
10
15
1
29
1
33
1
37
1
41
1
45
1
49
1
53
1
57
1
61
1
65
1
69
FIGURE 3.6
Post-intervention forecasts
From where did the value of the intervention discount come?
Many sophisticated and fascinating control schemes exist in the
engineering literature, but for our purposes a simple calibration
procedure can be used. From a collection of spread histories, isolate
the points at which step changes in the spread occurred. Experiment
with a range of intervention discount factors until the pattern of
forecasts across all the cases is adequate. (Once more, subjective
terms such as ‘‘adequate’’ are left to your interpretation.)
How large a spread is indicative of possible level shift? Look
again at your data: Three standard deviations from the mean occurs
how often? How many false monitor alarms would ensue with that
calibration? What about four standard deviations? How many level
shifts are missed? With what consequences for spread bets? It is
not useful to rely on probabilities of standard deviation moves for a
normal distribution—3 standard deviations from the mean occurring
0.2 percent of the time—because spreads are typically not normally
distributed. To see this, form the daily spread data from your favorite
pair into a histogram, overlay the best ﬁtting normal density curve
(match the sample mean and variance). Examine the quality of the ﬁt
in the tails and in the center of the density.
--- page 72 ---

Structural Models
45
−1.5
−1.0
−0.5
0.0
0.5
1.0
1.5
0.0
0.5
1.0
1.5
FIGURE 3.7
CAL–AMR spread returns, December 2001 to May 2002, with
normal density
Figure 3.7 illustrates a common situation. Daily returns from a
sample of six months of the CAL–AMR spread (December 2001
through May 2002) are displayed in a histogram; a normal density curve is ﬁtted to the sample mean and standard deviation is
superimposed. I leave the commentary to you.
Empirical experimentation is a sounder approach to developing
understanding than blind assumption of normality, and a good place
from which to build a representative formal model if that is your goal.
Chapter 5 debunks some common misconceptions about underlying
distributions and reversion in time series data.
A more detailed discussion of forecast monitoring; intervention
and automatic adaptation schemes, including likelihood based tests
instead of the rudimentary standard deviation rules suggested here;
and evidence accumulation strategies is given in Pole et al., 1994. That
volume details the class of models known as dynamic linear models
(DLM) which contain as special cases MA and EWMA models,
and also autoregressive models that feature prominently in some
statistical arbitrageurs’ offerings. The structure of the DLM provides
for a rather richer analysis than anything discussed in this volume.
--- page 73 ---

46
STATISTICAL ARBITRAGE
In Chapter 9, Section 2, a situation that practically screamed
for intervention is related: the forced liquidation of $4.4 billion in
October 2003 because of massive redemptions in response to the
New York attorney general’s investigation of Janus for mutual fund
market timing activities. Expected market reaction to the terrorist
attacks on the United States in September 2001 is a ﬁne example of
the need for careful review and the value of well designed, selective
intervention.
Not all changes of level are as dramatic as in the preceding
example. Often a new level is reached after a migration over several
days rather than in a single, outsize leap. The British Petroleum
(BP)–Royal Dutch Shell (RD) spread shown in Figure 3.8 exhibits
several such migrations. Two EWMA forecast functions are illustrated. The ﬁrst is a standard EWMA with discount factor 0.09
(which is similar to a moving average on 25 days except at times of
signiﬁcant change where the MA lags the EWMA’s adjustment to
the data, as previously remarked), which adapts rather slowly to the
Jan
Feb
Mar
Apr
May
Jun
Jul
Aug
Sep
Oct
Nov
Dec
2003
2
3
4
5
6
7
8
$
EWMA with automatic trend adjustment
EWMA
FIGURE 3.8
Trend detection and level adjustment
--- page 74 ---

Structural Models
47
$4 change in spread level in the ﬁrst quarter of 2003. The second
is an EWMA that switches to a high discount factor when a level
shift is detected to be underway. The increased pace of adaptation
is evident in the downward shift of the spread in February 2003,
the two subsequent shifts upward in April and June, and another
downward shift in late July.
For this demonstration, the switching rule is quite crude: When
the spread exceeds a one standard deviation margin from the basic
EWMA for several days in succession, use the high discount factor for
faster adjustment. (The local standard deviation is computed using
EWMA smoothing.)
Before leaving the BP–RD spread, take another look. Over the
whole year, the spread exhibits a nicely controlled sinusoidal-like
variation about a mean of $5. What do you make of that?
3.4
CLASSICAL TIME SERIES MODELS
There are many books on the market that describe models for
characterizing time series and making forecasts. A few are listed in
the bibliography and those are your ﬁrst stopping point for a detailed
understanding of model forms, statistical estimation and forecasting
procedures, and practical guidance on data analysis and model
building. In this section we give heuristic descriptions of several
model types that have been successfully employed by statistical
arbitrageurs. The discussion will be grounded in the context of
the spread and reversion descriptions and archetypal underlying
processes (sinusoidal and popcorn).
3.4.1
Autoregression and Cointegration
Probably the most commonly applied time series model structure in
any ﬁeld is the autoregressive model. Future values of a series are
projected as weighted averages of recently exhibited values in that
series. Examples already seen include the moving average and the
exponentially weighted moving average.
The autoregressive model of order p relates the series outcome
at time t to a linear combination of the p immediately preceding
outcomes:
yt = β1yt−1 + · · · + βt −pyt −p + ϵt
--- page 75 ---

48
STATISTICAL ARBITRAGE
The coefﬁcients, βi, or model parameters, are determined by estimation from a set of observations of the series. The ﬁnal term, ϵt is the
so-called ‘‘error term’’ in which is conveniently gathered all the variability that cannot readily be subsumed in the structural part of the
model. This is the term typically assumed to be normally distributed
when standard estimation methods are applied and properties of
parameter estimates or forecasts are discussed.
Autoregressive models often appear as ARIMA models, which
stands for autoregressive integrated moving average. The classic, and
unsurpassed, reference is Box and Jenkins (1976). A moving average
model in this context is, confusingly, somewhat different from the
moving average previously encountered. Here it is really a shorthand
way of writing a very long moving average of a series past values
using a mathematical equivalence to an average of a few imaginary
terms. That is quite a mouthful as well as brain fag so we will not
pursue it here.
And what of the ‘‘integrated’’ part? That is simply a differencing
operation applied to a series before investigating autoregression
structure. For example, daily differences in prices, zt = pt −pt−1 in an
obvious notation, might exhibit autoregression structure. The model
for the raw price series is then called an integrated autoregression.
The EWMA forecast function, while originally developed in the
logical, data analytic way for smoothing variable observations as we
introduced it earlier, is actually derivable as the optimal forecast for
an integrated model.
This leads nicely to cointegration. Often several series are observed
to move together in ways suggestive of a relationship; common situations include (a) one series driving another, and (b) several series driven
by
common
underlying
processes.
Multivariate
forms
of
ARIMA models can represent very complicated structures of this sort
including contemporaneous and lagged feedback relationships.
A structure familiar to spread modelers (but perhaps not known
by its technical name) is cointegration. Where two (or more) series
are nonstationary individually but their difference (the spread, in our
context) is stationary (think of that as meaning ‘‘approximated in
good measure by an autoregression’’), the series are called cointegrated. The difference (and it may be a difference other than the
ﬁrst though we will not pursue that here) is well modeled by an
autoregression.
--- page 76 ---

Structural Models
49
A related class of autoregression models provides parsimonious
structural forms for series with long-term serial correlation dependencies. Long-term correlation can be directly captured by a very
high order autoregression, but estimation problems ensue because
of the high parameter count. Autoregressive fractionally integrated
moving average (ARFIMA) models overcome the parameter count
problem, essentially ﬁtting ARMA models to series after fractionally
differencing.
3.4.2
Dynamic Linear Model
All of the models discussed in the preceding section rely on a
considerable degree of stationarity in data series for their efﬁcacy.
Model parameters are estimated over a long history of data and are
supposed to be unchanging. In ﬁnancial practice, it is seldom that
relationships in data are even approximately unchanging for any
length of time. Parameter updating procedures are universal, reﬁtting
models to moving windows of data, a commonly used (and useful)
device. The local mean and volatility calculations used in Chapter 2
exemplify the procedure.
A ﬂexible model structure that directly embodies temporal movement in data deﬁning qualities, local mean for example, is the dynamic
linear model. In the DLM, temporal change in model parameters is
explicitly included through the speciﬁcation of an evolution equation.
Consider a ﬁrst order autoregression:
yt = βyt−1 + ϵt
in which the realizations of a series are composed of two parts:
a systematic propagation of a ﬁxed portion of the immediate past
deﬁned by the parameter β, and a random addition ϵt. Now consider a
ﬂexible generalization of that model in which the systematic element
propagated sequentially may vary in magnitude period by period.
The parameter β is now time indexed and its variation is strictly
formalized so that evolution is permitted but revolution is not.
The dynamic model is speciﬁed by two equations, one deﬁning the
observation sequence and one deﬁning the systematic evolution:
yt = βtyt−1 + ϵt
observation equation
βt = βt−1 + ωt
system equation
--- page 77 ---

50
STATISTICAL ARBITRAGE
In the system equation, the term ωt is a random term that controls,
by the magnitude of its variance, how fast the regression coefﬁcient
βt can change. With ωt identically zero, the dynamic model reduces
to the familiar static model. With a ‘‘large’’ variance for ωt, the
data series history is immediately discounted so that βt = yt/yt−1.
You may begin to see how intervention in the dynamic linear model,
exempliﬁed for the EWMA model in Section 3.3, is implemented.
The DLM includes ARIMA, EWMA, and regression models as
special cases, making it a rich, ﬂexible class with which to work.
Monitoring and intervention strategies are readily deﬁned for each
model component separately and in combination. See, Pole, et al.
for examples.
3.4.3
Volatility Modeling
Volatility modeling has an extensive pedigree in quantitative ﬁnance.
Use in statistical arbitrage is less direct than in derivative valuation
where most theoretical development and published applications are
seen, but it is nonetheless helpful. Consider just the simple spread
modeling that provides much of the background of the discussion in
this book: The variance of the return stream determines the richness
of potential bets (the basic viability of candidate raw material for a
strategy), variability of mark to market gains and losses while a bet
is extant (the risk proﬁle of a strategy, stop loss rules), and return
stretching by stochastic resonance (see Section 3.7).
Generalized autoregressive conditional heteroscedastic (GARCH)
and stochastic volatility models loom large in the modeling of volatilities. The derivatives literature is replete with variants of the basic
GARCH model with acronyms ranging from AGARCH through
EGARCH to GJR GARCH, IGARCH, SGARCH and TGARCH.
GARCH models are linear regression models with a nonlinear structural speciﬁcation for the error variance. The error variance, in other
models assumed to be a constant or a known function of some aspect
of the model or time (see the discussion of variance laws in Pole,
et al.), is speciﬁed to be a linear function of the error term in the basic
regression function. Consider, again, the ﬁrst-order autoregression
and now add a ﬁrst-order GARCH component:
yt = βyt−1 + ϵt,
et ∼N(0, ht),
ht = α0 + α1ϵ2
t−1
