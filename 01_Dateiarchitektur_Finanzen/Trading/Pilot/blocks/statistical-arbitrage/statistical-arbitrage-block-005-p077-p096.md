# Statistical Arbitrage_ Algorithmic Trading Insights and -- Karen M_ Sowers; Andrew Pole -- Wiley Finance, 1, 2007 -- Wiley & Sons, Incorporated, John -- isbn13 9780470138441 -- 6b0138550172e24db7f13c932e054fb9 -- An.pdf — pages 77–96

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
--- page 78 ---

Structural Models
51
The notation, et ∼N(0, ht) means that the (error) term et is assumed
to be randomly distributed according to the normal distribution with
mean 0 and variance ht. (The ‘‘TGARCH’’ model uses a Student t
distribution in place of the normal for smoother response to ‘‘large’’
deviations.) In this model, the disparity between a forecast and
the corresponding outcome feeds directly into subsequent forecast
variance. A large forecast error ‘‘forces’’ the model to anticipate
forthcoming large volatility. That, in turn, means that less weight
will be accorded to the next observation in updating parameter
estimates. Therefore, when a model with GARCH error structure is
ﬁtted to data that exhibits volatility clusters (bursts of higher than
normal volatility) the weight given to the more variable observations
in estimating the structural part of the model is reduced relative to
the weight given to less variable observations.
In contrast to weighted estimation procedures, which assume a
known functional form of variance variability (such as the ‘‘level to
the power 1.5’’ which arises often in product sales data being the
result of a compound Poisson process), the GARCH model estimates
the changing pattern of variation along with the structural part of
the model. The pattern of variability is not speciﬁed ahead of time,
but a rule of recognition is: Large forecast–outcome discrepancies
signify large volatility.
Models may include greater lag structure—more ϵt−k terms much
like higher order autoregression models for mean structure. Interpretation of such models is difﬁcult and, unsurprisingly, successful
applications are largely restricted to low lag structures.
There is an enormous literature on GARCH models, beginning with Engle’s 1982 paper, with applications in macroeconomics
and ﬁnance.
3.4.4
Pattern Finding Techniques
Exploiting persistent patterns of stock price behavior has been
approached directly through pattern ﬁnding procedures including
neural networks and wavelets. Wavelet analysis, a sort of localized Fourier analysis, decomposes a time series into a collection of
locally orthogonal basis functions with weights appropriate to the
raw series in question. A neural network is a collection of weighted
transformation functions; there is no explicit temporal structure but
--- page 79 ---

52
STATISTICAL ARBITRAGE
such structure is implicit in the transformation of the inputs (past
observations of a series) to the output (forecasts).
Neural networks are excellent tools for ﬁnding patterns in data.
Where patterns recur, network forecasts can be extraordinarily good.
A major drawback though is the lack of interpretability. While it is
possible to disentangle the transformations in a small network (at
most a single hidden layer, only a handful of nodes per layer, well
behaved transfer functions) and thereby attach theoretical understanding, this is not the routine situation. And what of that? If a
neural network successfully identiﬁes predictive footprints in stock
price data, what does it matter if the intellectual grasp of the
input–output transformation is looser than a competitor’s model
built from autoregressions applied to (say) factor residuals (Section
3.6)? It may not matter at all and we leave the contentious matter to
your consideration.
A great advantage of neural networks is their ﬂexibility, which
is the reason they are such good pattern identiﬁers to begin with.
When structural change occurs, neural networks can be very quick
to identify that a change is underway and subsequently characterize
newly stable patterns. The attendant danger, always a partner of such
ﬂexibility, is that identiﬁed patterns may be ephemeral, their existence
ﬂeeting in terms of usable exploitation opportunities. Borrowing from
Orwell’s fancy: description yes, prediction no.
3.4.5
Fractal Analysis
We refer the interested reader to the inventor, Benoit B. Mandelbrot
2004, who tells it best.
3.5
WHICH RETURN?
Which return do you want to forecast? The answer may seem obvious
if you have a particular context in mind: Forecast return for today
and trade around that. In general the answer is not obvious outside
the context of theory, data analysis, and trading goals. Let’s assume
that the latter is simply to maximize strategy return (subject to some
risk controls that will be left unspeciﬁed here). Without theoretical
guidance, we might proceed simply to explore some traditional time
scales, investigating patterns of daily, weekly, or monthly return.
--- page 80 ---

Structural Models
53
A little more thought might suggest investigating how return evolves
with duration: Examining returns for 1, 2, 3, . . . ,k days might indicate
a natural time period for a particular type of series, whether it is
individual raw stock prices or functions thereof such as factors (see
Section 3.6); one might also want to examine the maximum return
over the next m days.
Pattern matching models, more elaborate and technically demanding than the models discussed in this book, lead one to consider more
general, multivariate functions of stock return series.
3.6
A FACTOR MODEL
The modeling discussion thus far has focused on spreads between
pairs of stocks, the domain where statistical arbitrage, as pairs
trading, had its genesis. Now we will discuss some modeling
ideas applied to individual stock price series analyzed as a
collection.
The notion of common risk factors, familiar from Barra-type
models, lies at the heart of so-called factor models for stock returns:
The basic idea is that returns on a stock can be decomposed into
a part that is determined by one or more underlying factors in the
market (and in common with other stocks) and a part that is speciﬁc
to the stock, so-called idiosyncratic return:
stock return = return to market factors + idiosyncratic return
Early models formed using this decomposition simply identiﬁed
market factors as industries (the S&P industry sectors) and a general
market factor. Some modelers used indexes as proxies for the factors,
building multiple regression models, autoregression models, or other
models for daily, weekly, or monthly returns; they also fashioned
forecasts from (a) forecast models for indexes (b) the constructed
regression (etc.) models, and built portfolios accordingly.
Later attempts used a more general model called a statistical
factor model. In a factor model, the factors are estimated from the
historical stock return data and a stock’s return may be dependent
on, or driven by, several of these factors.
--- page 81 ---

54
STATISTICAL ARBITRAGE
3.6.1
Factor Analysis
A factor analysis of a multivariate data set seeks to estimate a
statistical model in which the data are ‘‘explained’’ by regression
on a set of m factors, each factor being itself a linear combination
(weighted average) of the observables.
Factor analysis has much in common with principal component
analysis (PCA) which, since it is more familiar, is good for comparison. Factor analysis is a model based procedure whereas principal
component analysis is not. PCA looks at a set of data and ﬁnds those
directions in observation space in which the data exhibits greatest
variation. Factor analysis seeks to estimate weights for a set of linear
combinations of the observables—so-called factors—to minimize
discrepancy between observations and model ﬁtted values.
If the distinction between PCA and factor analysis seems hazy,
good. It is. And we will say no more about it.
Suppose the universe of stocks has p elements (stocks). We might
usefully entertain the component stocks of the S&P 500 index (as of
a ﬁxed date) as an orienting example. Pick a number of factors, m.
Given daily historical returns on the selected stock universe, a factor
analysis procedure will yield m factors deﬁned by their respective
factor loadings. These loadings are weights applied to each of the
stocks. Thus, factor 1 has loadings l1,1, . . . , l1,500. The other m −1
factors similarly have their own loadings.
Multiplying the loadings by the (unobserved) factors yields values
for the returns. Thus, given the loadings matrix L, the columns of
which are the loadings vectors just described, estimates of the factors,
or factor scores, can be calculated.
So, after a factor analysis one has, in addition to the original
p stock return time series, m time series of factor estimates. It may
help to think of the parallel with industry index construction; some
statistical factors may look like industry indexes, and may even be
thought of that way. But keep in mind the important structural
distinction that statistical factors are a function solely of stock price
history with no information on company fundamentals considered.
If one were to regress the stock returns on the factors one would
obtain a set of regression coefﬁcients. For each stock, there is one
coefﬁcient per factor. These coefﬁcients are the stock exposures to the
factors. By construction of the factors, there is no other set of m linear
combinations of the observables that can give a better regression for
--- page 82 ---

Structural Models
55
the chosen estimation criterion (most often maximum likelihood).
There are inﬁnitely many equivalent sets, however. Strategies with
names such as varimax rotation and principal factors—related to
principal component analysis—are used to select a unique member
from this inﬁnite set.
Note that there is a duality between factor loadings and
stock exposures to factors. The duality, which is a consequence
of the factor deﬁnition and construction, is such that the rows of the
loadings matrix are the stock exposures to the factors. That is, in
the p × m loadings matrix L, the element li,j is both the loading of
the jth factor on the ith stock and the exposure of the ith stock to the
jth factor.
What is the interpretation of a factor model? It is this: The
universe of p stocks is supposed to be a heavily confused view of
a much smaller set of fundamental entities—factors. Crudely, one
might suppose that the stock universe is really driven by one factor
called ‘‘the market.’’ Less crudely one might suppose that, in addition
to the market, there are a dozen ‘‘industry’’ factors. The factor
analysis may then be viewed as a statistical procedure to disentangle
the structure—the factors—from the noisy image presented by the
full stock universe, and to show how the stock universe we observe
is constructed from the ‘‘real’’ factor structure.
3.6.2
Defactored Returns
Another successful model based on factor analysis reversed the usual
thinking: Take out the market and sector movements from stock
returns before building a forecast model. The rationale is this: To the
extent that market factors are unpredictable but sentiment about the
relative position of individual stocks is stable over several days, such
ﬁltered returns should exhibit more predictable structure. Let’s look
in a little more detail at this interesting idea.
Residuals from the ﬁtted regression model (stocks regressed on
estimated factors) will be referred to as defactored returns. It is
these defactored returns on which attention is focused. Why? The
notion is that return to a stock may be considered as being composed of return to a set of underlying factors (market, industry,
or whatever other interpretation might be entertained) plus some
individual stock-speciﬁc amount. For a stock i this may be expressed
--- page 83 ---

56
STATISTICAL ARBITRAGE
algebraically as:
ri = rf1, + · · · + rfm + rsi
For a market and industry neutral portfolio, it is the stock-speciﬁc
component which remains in the residual of the standard ﬁtted model.
Moreover, the stock-speciﬁc component may be more predictable
than the others in the short term and following this construction.
For example, regardless of today’s overall market sentiment, the
relative positions (value) of a set of related stocks are likely to be the
similar to what they were yesterday. In such situations, a portfolio
constructed from forecasts of ‘‘de-marketed’’ returns is still likely to
yield a positive result.
A simpliﬁed illustration may help to convey the essence of the
notion. Suppose a market comprises just two stocks in roughly equal
proportion (capitalization, value, price). On day t the return may
be denoted:
r1,t = mt + ηt,
r2,t = mt −ηt
In this case, the factor model will include just one component and
historical data analysis will reveal the market to be essentially the
average of the two constituent stocks. (More generally, different
stocks will have different exposures to a factor—mt would appear
weighted in the equations—but with weights intimately bound up
with the factor deﬁnition as already described.) In this case, the
stock-speciﬁc return will be of the same magnitude for each stock,
but signed differently. Now, if this quantity, ηt, can be predicted
better than by random guess, then regardless of the pattern of the
market return, a portfolio long stock 1 and short stock 2 (vice versa
when η is negative) will, on average, yield a positive return.
In a more realistic situation, as long as many bets are made
and there is some forecast power in the defactored return model
(which may be a EWMA, autoregression, etc.), the trading strategy
should win. Making bets dependent on the size of forecast returns
and optimizing selected portfolios for risk should improve return/risk
performance.
Brief details of the algebra of factor analysis and the construction
of the defactored returns model are given in Section 3.10.
--- page 84 ---

Structural Models
57
Operational Construction of Defactored Returns
Factor loadings/exposures must be updated periodically to maintain any reasonable
expectation of forecast (and hence trading) performance. Since the
statistical factors directly reﬂect (supposed) structure in the stock
price histories, it is not surprising to discover that the structure
is dynamic. Estimating factor relationships from stale data will
most likely produce results with unpromising forecast performance.
The selection of the frequency of factor updating is, like similar
dynamic model elements previously remarked on, a matter for the
investigator’s art. Quarterly or half yearly revision cycles are often
used.
Defactored returns must be calculated using the most recent
past set of loading estimates and not the contemporaneous set,
ensuring that the defactored return series are always defactored
out of sample. While this is deleterious for simulation results, it is
critical for strategy implementation. It is easy to pay lip service to
this commonly acknowledged matter but also easy in a complicated
model or estimation procedure to forget it.
A dynamic model, generalization of the DLM might be considered so that model parameters are revised each day according to a
structural equation, but the extra computational complexity was not
justiﬁed in the late 1980s. Today there is no such computational
concern and dynamic factor models have appeared in the statistical
literature with applications to stock price prediction. With these
complicated models it is incredibly easy, and tempting, to allow great
ﬂexibility, unwittingly taking a path to a model that does little more
than follow the data. More than one manager eventually fell victim
to the seduction, optimized to oblivion.
3.6.3
Prediction Model
After all the work necessary to build the time series of defactored
returns for each stock, the modeler is still faced with constructing a
forecast model for those returns. That does not imply a return to ﬁrst
base since that would mean that the rationale for the defactorization
was void. Nonetheless, one is, as stated, faced with a forecast
model building task. One might consider autoregressive models,
for example. Note that cointegration models should presumably be
of little value here because common factors are supposedly removed
in the defactorization procedure.
--- page 85 ---

58
STATISTICAL ARBITRAGE
Many elaborations may be entertained. For instance, there may
be more stability in factor estimation on time scales with granularity
much longer than one day.
The natural alternative of building a forecast model for the factor
series and predicting those series may be entertained. However, this
would not replace the defactored return predictions: In the simple
example of the previous section, factor prediction is equivalent to
prediction of mt (or a cumulative version thereof). The defactored
component is still present.
An unanswered question that arises in this consideration of
return forecasting is: What is the relationship between k-day ahead
cumulative stock returns and k-day ahead factor estimates? From the
earlier discussion, another pertinent consideration is: If, as posited,
the market factors are more erratic than the defactored component,
then the forecasts will be less useful (in the sense that trading them
will yield more volatile results). These considerations indicate that
factor predictions are a secondary task for return exploitation (in
the context of a valid defactor model). However, factor prediction
models—defactor structured return model or not—are useful in
monitoring for market structural change and identifying the nature
and extent of such change.
3.7
STOCHASTIC RESONANCE
With a model-based understanding of spread or stock price temporal
dynamics, there is another crucial part of the process in which
analysis can demonstrate exploitation possibilities. Consider a spread
that may be characterized as a popcorn process: Occasionally the
spread departs from its (locally in time) ‘‘normal’’ value subsequently
to return to that norm over a reasonably well deﬁned trajectory. The
normal level is not constant. When not subject to some kind of motion
inducing force such as a block trade, spreads meander around a local
average value, sometimes greater and sometimes less. This motion is
largely random—it can, at least, be satisfactorily considered random
in the present context. Knowing that once a spread has ‘‘returned’’ to
its mean it will henceforth exhibit essentially random variation about
that mean suggests that the reversion exit rule can be modiﬁed from
the basic ‘‘exit when the forecast is zero’’ to ‘‘exit a little on the other
--- page 86 ---

Structural Models
59
side of the zero forecast from which the trade was entered.’’ Here
the ‘‘little’’ is calibrated by analysis of the range of variability of the
spread in recent episodes of wandering about the mean before it took
off (up or down). Volatility forecasting models, GARCH, stochastic
volatility, or other models may be useful in this task.
The phenomenon of ‘‘noise at rest,’’ the random wandering
about the local mean just exempliﬁed, is known as stochastic
resonance.
As you read the foregoing description, you may feel a sense of
deja vu. The description of modeling the variation about the mean
during periods of zero forecast activity is quite the same as the general
description of the variation of the spread overall. Such self-similarity
occurs throughout nature according to Benoit Mandelbrot, who
invented a branch of mathematics called fractals for the study and
analysis of such patterns. Mandelbrot, 2004, has argued that fractal
analysis provides a better model for understanding the movements
of prices of ﬁnancial instruments than anything currently in the
mathematical ﬁnance literature. It is unknown whether any successful
trading strategies have been built using fractal analysis; Mandelbrot
himself does not believe his tools are yet sufﬁciently developed for
prediction of ﬁnancial series to be feasible.
3.8
PRACTICAL MATTERS
Forecasts of stock price movements are incredibly inaccurate. Take
this message to heart, especially if you have completed a standard
introductory course on statistical regression analysis. The traditional presentation proclaims that a regression model is not very
useful (some statisticians would say useless) if the R-square is less
than 70 percent. If you have not taken such a course and do not
know what an R-square is, no matter: Read on. The traditional
presentation is not wrong. It is just not appropriate to the situation we are concerned with here. Now, observing that your weekly
return regressions produced ﬁtted R-squares of 10 percent or less,
perk up!
The key to successfully exploiting predictions that are not very
accurate is that the direction is forecast correctly somewhat better
than 50 percent of the time (assuming that up and down forecasts
--- page 87 ---

60
STATISTICAL ARBITRAGE
are equally accurate).1 If a model makes correct directional forecasts
(50 + ϵ)% of the time, then the net gain is (50 + ϵ) −(50 −ϵ)% =
2ϵ% of the bets. This net gain can be realized if one can make a
sufﬁcient number of bets. The latter caveat is crucial because averages
are reliable indicators of performance only in the aggregate.
Guaranteeing that 2ϵ% of one’s bets is the net outcome of a
strategy is not sufﬁcient, by itself, to guarantee making a proﬁt:
Those bets must cover transaction costs. And remember, it is not the
1The situation is actually more complicated in a manner that is advantageous to
a fund manager. Symmetry on gains and losses makes for a simple presentation
of the point that a small bias can drive a successful strategy; one can readily live
with relative odds that would cause a physician nightmares. The practical outcome
of a collection of bets is determined by the sum of the gains minus the sum of
the losses. A big win pays for many small losses. The signiﬁcance of this fact is
in directing a manager to construct stop loss rules (early exit from a bet that is
not working according to forecast expectation) that curtail losses without limiting
gains. Where this is possible, a model with seemingly textbook sized relative odds in
favor of winning forecasts can be proﬁtably traded within prescribed risk tolerances.
Technically, such rules modify the utility function of a model by altering the
characteristics of the outcome set by employing a procedure in which the forecast
model is only one of several elements.
A warning: Beware of being fooled by purveyors of tales of randomness.
A strategy that offers bets that typically generate a small loss and occasionally a
whopping gain sounds alluring when proffered as relief after a cunningly woven
web of disaster shown to seemingly inevitably follow plays where the odds are
conventionally in favor of winning. After these examples of catastrophe are depicted,
solace is offered in the guise of an alternative characterized by low risk (small losses)
with large gain potential. A crafty invocation of the straw man technique of
persuasion. Or, statisticulation, as Huff would call it.
A ﬁne artisan of the word weaves an impressing story of unavoidable doom
employing unimpeachable calculus of probability. Then, Pow! Batman saves the
‘‘What can I do?’’ day with a tale of the occasional big win bought by easy-to-take
small losses. A complete reversal of pattern. That cannot—can it?—but dispel the
doom instantly. Opposite pattern must beget opposite emotion. Joy!
Now about those small losses. Lots of small losses. Total up those small losses
and discover the shamelessly omitted (oops, I mean inadvertently hidden in the
detail) large cumulative loss over an extended period before the Batman surprise.
So what have we truly gotten? A few periods of glee before inevitable catastrophe
supplanted with prolonged, ulcer inducing negativity, despondency, despair, and
(if you can stand the wait) possible vindication! It is still an uncertain game. Just
different rules.
There are many kinds of randomness.
--- page 88 ---

Structural Models
61
average transaction cost that must be covered by the net gain. It is the
much larger total cost of all bets divided by the small percentage of
net gain bets that must be covered. For example, if my model wins 51
percent of the time, then the net gain is 51 −49 = 2 percent of bets.
Thus, out of 100 bets (on average) 51 will be winners and 49 will be
losers. I make net 2 winning bets for each 100 placed. Statistically
guaranteed. My fee for playing, though, is the fee for making all 100
bets, not just the net 2. Thus, my 2 percent guaranteed net winners
must cover the costs for all 100 percent of the bets.
Statistical forecast models can do much more than simply predict
direction. They can predict magnitude also. Consider a ﬁrst-order
autoregressive model for weekly returns, for example: The size of the
return for next week is forecast explicitly (as a fraction of the return
for last week). If an estimated statistical model has any validity, then
those magnitudes can be used to improve trade selection: Forecasts
that are smaller than trade cost are ignored. No point in making bets
that have expected gain less than the cost of the game, is there?
Now, what about all that prediction inaccuracy we talked about?
If predictions are okay on average but lousy individually, how can we
rely on individual forecasts to weed out trades with expected return
lower than trade cost? Won’t we throw away trades that turn out to
be enormously proﬁtable? And take trades that return less than costs?
Indeed yes. Once again, it is the frequency argument that is
pertinent here. On average, the set of trades discarded as unproﬁtable
after costs has expected return lower than trade cost. Also, on
average, the set of retained trades has expected return greater than
trade cost. Thus, the statistically guaranteed net gain trades have
expected return greater than trade cost.2
3.9
DOUBLING: A DEEPER PERSPECTIVE
It is tempting after an extended discussion of technical models, even
at the limited descriptive level of this chapter, to be seduced into
2Recall footnote 1, on improving the outcome of a forecast model by imposing a
bet rationing (stop loss) rule. Such a procedure increases the average gain of bets
made according to the forecast model, so one might squeeze just a little more from
an opportunity set by realizing that return bias can convert some raw losing trades
(those with average gain less than transaction cost) into winning trades. Subtle. And
nice. See also the discussion of stochastic resonance in Section 3.7.
--- page 89 ---

62
STATISTICAL ARBITRAGE
forgetting that models are wrong. Some are useful and that is the
context in which we use them. When applying a model, an activity
of signal urgency and import is error analysis. Where and how a
model fails informs on weaknesses that could be ameliorated and
improvements that might be discovered.
In Chapter 2 we introduced ‘‘Rule 3,’’ a bet doubling scheme
in which a spread bet was doubled if the spread became sufﬁ-
ciently large. The idea was motivated by observing spread patterns
in the context of an already formulated model, Rule 1 or 2—this
is error analysis notwithstanding the quasi informality of rule positing based on eyeballing data rather than formal statistical model
building.
With more complicated models, eyeball analysis is infeasible.
Then one must explicitly focus upon the results of trading a model,
either in practice (with dollars at risk) or synthetically, (using simulations). Beyond the standard fare of comparing forecast return with
outcome one can examine the trajectory of bet outcome from the
point of placement to the point of unwinding. In the example of
the spread doubling the typical trajectory of cumulative return on
the original bet is a J curve: Losses at ﬁrst are subsequently recovered then (the doubling phase) proﬁts accrue. Trade analysis from
any model, regardless of complexity, can reveal such evolutionary
patterns and, hence, provide raw material for strategy enhancements
such as doubling.
Notice how the dynamic of the trade, not the identiﬁcation
of placement and unwind conditions, reveals the opportunities in
this analysis. Dynamics, trade and other, are a recurring theme in
this text. While the end result is what makes it to the bank and
investor reports, dynamics of how the result is made are critical
for identifying problems and opportunities. They are also important
to understand from the perspective of explaining monthly return
variability to investors when trades extend over calendar month-end
boundaries.
Figure 3.9 shows the archetypal trio of trade cumulative return
trajectories: (a) gain from trade inception to unwinding; (b) loss from
inception to trade cancellation; (c) the J-curve of initial loss followed
by recovery and gain. Analysis of collections of trades in each category
can reveal possibilities for strategy improvement. Imagine what you
would do with the discovery of a distinct characterization of price
--- page 90 ---

Structural Models
63
(a)
(b)
time from trade inception
return
(c)
FIGURE 3.9
Archetypal trade cumulative return trajectories
and volume history immediately preceding trade signals that divided
prospective trades into the three categories.3 Imagine.
3.10
FACTOR ANALYSIS PRIMER
The following material is based on the description of factor analysis
in The Advanced Theory of Statistics, Volume 3, Chapter 43, by Sir
Maurice Kendall, Alan Stuart, and Keith Ord (now called Kendall’s
Advanced Theory of Statistics [KS]). The notation is modiﬁed from
KS so that matrices are represented by capital letters. Thus, γ in KS
is  here. This makes usage consistent throughout.
Suppose there are p stocks, returns for which are determined
linearly from values of m < p unobservable factors:
rj =
m

k=1
ljkfk + µj + ϵj,
j = 1, . . . , p
3This type of research has received considerable attention in seismology where
predicting earthquakes remains a research priority for several countries, recently
highlighted by the tsunami death toll of over 200,000 from the December 2004
event in the Indian Ocean.
--- page 91 ---

64
STATISTICAL ARBITRAGE
where the ϵs are error terms (observation error, model residual
structure). The coefﬁcients l are called factor loadings. The variable
means µj are usually subtracted before analysis. In our case, we
assume that returns have mean zero so that µj = 0. In matrix form:
r
(p × 1) =
L
(p × m)
f
(m × 1) +
µ
(p × 1) +
ϵ
(p × 1)
where L is the p × m matrix of coefﬁcients {lij}. (Note that this
expression is for one set of observations; that is, the set of returns on
p stocks for a single day.) Now assume:
1. That the f’s are independent normal variables with zero mean
and unit variance
2. That each ϵj is independent of all other ϵs and of all the fs and
has variance (or speciﬁcity) σ 2
j
It follows that:
cov(rj, rk) =
m

t=1
ljtlkt,
j̸ = k,
var(rj) =
m

t=1
l2
jt + σ 2
j
These relationships may be expressed succinctly in vector/matrix
form as:
 = LL′ +
where
 is the p × p matrix diag(σ 2
1 , . . . ,σ 2
p ).
From the data, we observe empirical values of . The objectives
are to determine the number of factors, m, and to estimate the
constants in L and
. Determination of m is highly subjective; it
is like choosing the number of components in principal component
analysis. Indeed, PCA is often used to get an initial estimate of m,
which may be reﬁned by likelihood ratio testing and residual analysis
of the m-factor model. In what follows, assume that m is ﬁxed.
--- page 92 ---

Structural Models
65
In some cases, interest is on the implied factor scores for particular
days in a sample. That is, given returns r,t = (r1,t, . . . , rp,t)′ on day
t, what are the implied values f,t = (f1,t, . . . , fm,t)′ for the m factors?
If L and
 are known, generalized least squares estimation of f ,t is
obtained by minimizing:
(r,t −µ −Lf,t)
′
−1(r,t −µ −Lf,t)
Note that the mean stock return vector, µ, is assumed to be zero.
(Recall that µj is the mean return of stock j; µ is not the mean stock
return on day t.) The solution of the minimization is:
ˆf,t = J−1L′
−1r,t
where J = L′
−1L. In practice, L and
 are unknown; the MLEs are
substituted.
An alternative estimator for the factor scores is given in S.J.
Press, Applied Multivariate Analysis, Section 10.3. (Our notation is
used for consistency herein.) Essentially, he assumes away the error
covariances when the model is restated as:
f,t = Ar,t + u,t,
t = 1, . . . , n
where the factor scores at time t are linear combinations of the
stock returns at that time. A subsequent appeal to a large sample
approximation results in the estimator:
ˆf,t = ˆL′(nRR′)−1r,t
3.10.1
Prediction Model for Defactored Returns
In the model described in Section 3.6, interest is in the defactored
returns. For day t, the set of defactored stock returns is deﬁned as
the difference between the observed set of returns and the weighted
factor scores (where the weights are, of course, the factor loadings):
dfr,t = r,t −ˆL′ˆf,t
This vector of defactored returns, computed for each day in the
sample, provides the raw time series from which the prediction
--- page 93 ---

66
STATISTICAL ARBITRAGE
model is constructed. In an autoregressive model, for example, the
entry in the regression for day t for stock j is:
k

a=1
dfrj,t−a = β1dfrj,t−k + · · · + βqdfrj,t−k−q+1 + ϵj,t
This equation states that the k-day cumulative defactored return to
day t is regressed on the q daily defactored returns immediately preceding the cumulation period. Notice that the regression coefﬁcients
are common across stocks.
The forecast of the k-day ahead cumulative defactored return at
the end of day t is constructed as:
k

a=1
dfrj,t+a = ˆβ1dfrj,t + · · · + ˆβqdfrj,t−q+1
Other forecast models may be employed: ‘‘You pay your money
and take your chances.’’
--- page 94 ---

CHAPTER4
Law of Reversion
Now here, you see it takes all the running you can do, to
keep in the same place.
—Through the Looking Glass, Lewis Carroll
4.1
INTRODUCTION
I
n this chapter, we begin a series of four excursions into the theoretical underpinnings of price movements exploited in statistical
arbitrage. The ﬁrst result, presented in this chapter, is a simple probability theorem that evinces a basic law guaranteeing the presence of
reversion in prices in an efﬁcient market. In Chapter 5 a common
confusion is cleared up regarding the potential for reversion where
price distributions are heavy tailed. In summary, reversion is possible
with any source distribution. Following that clariﬁcation, we discuss
in Chapter 6 deﬁnition and measurement of interstock volatility, the
variation which is the main course of reversion plays. Finally in this
theoretical series, we present in Chapter 7 a theoretical derivation of
how much reversion can be expected from trading a pair.
Together these four chapters demonstrate and quantify the
opportunity for statistical arbitrage in ideal (not idealized) market conditions. The material is not necessary for understanding the
remainder of the book, but knowledge of it will amplify appreciation
of the impact of market developments that have led to the practical elimination of the discipline of statistical arbitrage in the public
domain.
67
--- page 95 ---

68
STATISTICAL ARBITRAGE
4.2
MODEL AND RESULT
We present a model for forecasting prices of ﬁnancial instruments
that guarantees 75 percent forecasting accuracy. The chosen setting is
prediction about the daily spread range of a pair but a little reﬂection
will reveal a much wider applicability. Speciﬁcally, we focus on
predicting whether the spread tomorrow will be greater or smaller
than the spread today.
The model is quite simple. If the spread today is greater than the
expected average spread, then predict that the spread tomorrow will
be smaller than the spread today. On the other hand, if the spread
today was less than the expected average spread, then predict that
the spread tomorrow will be greater than the spread today.
4.2.1
The 75 Percent Rule
The model just described is formalized as a probability model as
follows. Deﬁne a sequence of identically distributed, independent
continuous random variables {Pt, t = 1, 2, . . .} with support on the
nonnegative real line and median m. Then:
Pr[(Pt > Pt−1 ∩Pt−1 < m) ∪(Pt < Pt−1 ∩Pt−1 > m)] = 0.75
In the language of the motivating spread problem, the random
quantity Pt is the spread on day t (a nonnegative value), and days are
considered to be independent. The two compound events comprising
the probability statement are straightforwardly identiﬁed with the
actions speciﬁed in the informal prediction model above. But a word
is in order regarding the details of each event. It is crucial to note that
each event is a conjunction, and, and not a conditional, given that,
as might initially be considered appropriate to represent the if –then
nature of the informal model. The informal model is a prescription
of the action that will be taken; the probability in which we are
interested is the probability of how often those actions (predictions)
will be correct. Thus, looking to expected performance, we want to
know how often the spread on a given day will exceed the spread on
the previous day when at the same time the spread on that previous
day does not exceed the median value. Similarly, we want to know
how often the spread on a given day will not exceed the spread on
--- page 96 ---

Law of Reversion
69
the previous day when at the same time the spread on that previous
day exceeds the median.
Those distinctions may seem arcane but proper understanding
is critical to the correct evaluation of expected result of a strategy.
Suppose that on eight days out of ten the spread is precisely equal
to the median. Then the scheme makes a prediction only for 20
percent of the time. That understanding ﬂows directly from the
conjunction/disjunction distinction. With the wrong understanding
a ﬁve-to-one ratio of expected return to actual return of a scheme
would ensue.
Operationally, one may bet on the outcome of the spread tomorrow once today’s spread is conﬁrmed (close of trading). On those
days for which the spread is observed to be greater than the median
spread, the bet for tomorrow is that the exhibited spread tomorrow
will be less than the spread seen today. The proportion of winning
bets in such a scheme is the conditional given that probability:
Pr[Pt+1 < Pt|Pt > m] = 3
4
Similarly, bets in the other direction will be winners three quarters
of the time. Does this mean that we win ‘‘1.5 of the time?’’ Now that
really would be a statistical arbitrage! The missing consideration is the
relative frequency with which the conditioning event occurs. Now,
Pt < m occurs half of the time by deﬁnition of the median. Therefore,
half of the time we will bet on the spread decreasing relative to today
and of those bets, three quarters will be winners. The other half of
the time we will bet on the spread increasing relative to today and
of those bets, three quarters will also be winners. Thus, over all
bets, three quarters will be winners. (In the previous illustration, the
conditioning events occur only 20 percent of the time and the result
would be 3
4 × 1
5 or just
3
20.)
Before proceeding to the proof of the result, note that the
assumption of continuity is crucial (hence the emphasis in the model
statement). It is trivial to show that the result is not true for discrete
variables (see the ﬁnal part of this section).
4.2.2
Proof of the 75 Percent Rule
The proof of the result uses a geometric argument to promote
visualization of the problem structure. An added bonus is that one
