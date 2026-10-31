# Statistical Arbitrage_ Algorithmic Trading Insights and -- Karen M_ Sowers; Andrew Pole -- Wiley Finance, 1, 2007 -- Wiley & Sons, Incorporated, John -- isbn13 9780470138441 -- 6b0138550172e24db7f13c932e054fb9 -- An.pdf — pages 39–58

--- page 39 ---

12
STATISTICAL ARBITRAGE
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
20
25
30
35
40
45
50
55
$
CAL
AMR
2000
FIGURE 2.2
Daily closing prices, CAL and AMR (2000)
by 150 percent! (Proﬁt is increased by a smaller percentage in 2002
over that obtained with rule 2 because rule 2 gains from the reverse
bet which is unaltered in rule 3. There was no reverse bet in 2003,
the position being carried into 2004.)
This single illustration demonstrates in blinding clarity the massive opportunity that lay before Tartaglia’s group in 1985, an era
when spreads routinely varied over an even wider range than exhibited in the examples in this chapter.
2.2.3
Rule Calibration
Immediately when one extends the analysis beyond a single pair, or
examines a longer history of a single pair, the problem of calibration
is encountered. In Figure 2.2 another pair of price histories is shown,
--- page 40 ---

Statistical Arbitrage
13
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
2000
0
5
10
15
20
25
$
FIGURE 2.3
Daily closing spread, CAL–AMR
now for the single year 2000. Figure 2.3 shows the corresponding
spread.1
Wow! We should have shown that example earlier. The spread
varies over a $20 range, three times the opportunity of the CAL–AMR
1The price series for AMR is adjusted for the spinoff of Sabre, the company’s
reservations business, on March 16, 2000. Without proper adjustment, the close
price series would drop from $60 to $30 overnight—an unrealistically dramatic
spread change! We elected to adjust prices moving back in time, so that the
pre-spinoff prices are altered from the values that obtained in the market at the time,
preserving more recent prices. Trading AMR in January 2000, one would of course
have been working at the actual pre-spinoff level of circa $60. How one makes price
adjustments, forward or backward, is a matter of taste, though it must be done
consistently. Return series computed from adjusted price histories are unique and for
that and other reasons, most analysis is done in terms of returns rather than prices.
In this book, prices are used for demonstration because the elucidated points are
more graphically made therewith. Price adjustment for corporate events, including
dividends and splits, is critical to proper calculation of gains from trading.
--- page 41 ---

14
STATISTICAL ARBITRAGE
example examined in Figure 2.1. But right there in that rich opportunity lies the ﬁrst difﬁculty for Rules 1–3: The previously derived
calibration is useless here. Applying it would create two trades for
Rule 3, entering when the spread exceeded $4 and $6 in January.
Signiﬁcant stress would quickly ensue as the spread increased to over
$20 by July. Losses would still be on the books at the end of the
year. Clearly we will have to determine a different calibration for any
of Rules 1–3. Equally clearly, the basic form of the rules will work
just ﬁne.
Now consider the problem of calibration applied to hundreds or
thousands of potential spreads. Eyeballing graphs would require a lot
of eyeballs. A numerical procedure, an automatic way of calibrating
rules, is needed. Enter statistics. The trading rules were divined by
visually determining the range over which the spread varied. This
is trivially computed automatically: The maximum and minimum
spread in Figure 2.1 is −$2 and $7. Allowing a margin of, say, 20
percent, an automatic calibration would give entry and exit values
of $5 and $0 for rule 1. This is not exactly what we selected
by eye, but operationally it generates similar (though richer) trades.
Critically, the procedure is readily repeated on any number of spreads
by computer.
For the second example (Figure 2.2) the spread range is $3 to $22.
The 20 percent margin calibration gives trade entry and exit values
of $18 and $7 respectively. Applying Rule 1 with this automatic
calibration yields a proﬁtable trade in 2000. That desirable outcome
stands in stark contrast to the silly application of the example one
calibration (entry at $4 and $6 and unwind at $0 as eyeballed from
Figure 2.1) to the spread in Figure 2.2 which leads to nauseating
mark to market loss.
Calibration Epochs
In the foregoing discussion of eyeball calibration,
we did not make explicit the span of time being considered, which
is two years in the ﬁrst example, one in the second. Naturally,
both examples were selected to convey in stark terms the beautiful
simplicity and evident availability of the pair trading opportunity.
Nevertheless, the examples are not unrealistic. And so: How much
time is appropriate?
The stocks in Figures 2.1 and 2.2 are the same: CAL and AMR.
The question, ‘‘How much time is appropriate?’’, is now seen to be
--- page 42 ---

Statistical Arbitrage
15
dramatically important continually, not just as a once-only decision
for each candidate pair. Imagine the consequences of using the
calibration of the CAL–AMR spread from 2000 for trading in
2002–2003. In this case, the consequences look benign: no trades. But
that is a negative consequence because valuable trading opportunities
are missed. In other cases, horribly costly bets would be placed using
a rule calibrated on out-of-date price history.
This question of how much price history to use to calibrate a
trading rule is critical. In contrast to the analysis described thus far,
one shot, static analysis in which the rule is applied to the same
price history as that from which it was derived, practical trading is
always an application of the past to the unknown future. In Figure
2.4, the four-year spread (2000–2003) history for CAL–AMR is
shown together with upper and lower limits, maximum −20 percent
range and minimum +20 percent range, respectively, calculated with
a look back window of three months. While these limits are, at times,
not nearly as good as the eyeball limits previously examined, they do
Q1
Q2
Q3
Q4
Q1
Q2
Q3
Q4
Q1
Q2
Q3
Q4
Q1
Q2
Q3
Q4
2000
2001
2002
2003
-10
-5
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
FIGURE 2.4
Daily closing spread, CAL–AMR (with upper and lower trade rule
margins)
--- page 43 ---

16
STATISTICAL ARBITRAGE
retain good properties for trade identiﬁcation. Furthermore, unlike
the previous in sample calculations, the current estimates are out of
sample projections. On any day, the only price information used in
the calculation is publicly available history. The computed limits are,
therefore, practically actionable.
Applying Rule 2, there are 19 trades (ignoring the ﬁrst quarter of
2000 since the limits are computed on insufﬁcient data), comprising
4 losing trades and 15 winning trades. Both winning and losing
trades exhibit periods where substantial mark to market losses are
incurred before gains accrue toward the end of the trade. One last
observation: Notice how the volatility of the spread has substantially
declined from 2000–2003; much will be said about that development
in later chapters.
2.2.4
Spread Margins for Trade Rules
In response to the demonstrated problem of determining operational
limits on the spread range to guide trade decisions, we chose to use
margins of 20 percent. In the three-month window the upper boundary, ‘‘short the spread,’’ is max spread −20 percent range, the lower
boundary, ‘‘buy the spread,’’ is min spread +20 percent range. This
operational procedure has the great merit of ready interpretation. It is
unambiguously clear what the margins are: one ﬁfth of the calculated
range of the spread over the previous three months.
Less satisfactory is the use of the extreme values, max and min.
Extremes exhibit great variability. Projecting extremes is therefore
subject to great uncertainty: Think of outliers and all you have read
in statistics texts about careful analysis thereof. Modeling extremes is
a complicated and fascinating area of study with applications ranging
from peak river ﬂow for ﬂood prediction to electricity demand for
prediction of generation requirements and the likelihood of outages,
among many others.
From the extensive variability of extremes comes the need for a
substantial margin (20 percent) for practicable trade rules. Suppose
that just the largest 10 percent of spread displacements served to
generate sufﬁcient trading opportunities to sustain a business based
on historical analysis. It would be unwise to rely on that margin
for actual trading because of the inherent uncertainty in projecting
information into the future. Extremes in the future are certain to
--- page 44 ---

Statistical Arbitrage
17
be different from extremes in the past. If a spread experiences a
‘‘quiet period,’’ business will be poor because few opportunities
will be identiﬁed even though there may be plenty of proﬁtable
opportunities. Better to be conservative and use a larger margin. Of
course, a spread may exhibit a volatile period; the consequences there
are more volatility in mark to market revenue but not a reduction in
business or total proﬁt.
Greater stability is obtained between extremes. Projecting the
central location of the spread is done with considerably greater conﬁ-
dence than projecting the extremes. Therefore, most implementations
modify the ‘‘go short’’ and ‘‘go long’’ limits to be computed as offsets
from the center rather than offsets from the extremes. Bollinger bands,
mean plus or minus a standard deviation, are a classic example. In
spite of the rationale though, it is arguable how much stability is
improved by this switch of focus: The standard deviation is computed from all the data, extremes included, and since observations are
squared, the extreme values actually receive proportionally greater
weight! Robust procedures are sensibly employed, which amounts to
excluding (in more sophisticated applications, down-weighting) the
most extreme values in a sample before computing summary statistics
such as the mean and standard deviation.
Extrapolating percentage points of the spread distribution, say the
twentieth and eightieth percentile, is similarly robust but is seldom
seen. Operationally it is of no practical signiﬁcance in the simple
trading rules described here. Greater signiﬁcance is found where
models are more sophisticated and the asymmetry of distributions
has mercenary implications.
Greater (presumed) stability is achieved at the cost of some
interpretability. There is no unique relationship between the standard
deviation of a distribution and the range. When presented with
standard deviations, many assume or don’t realize they are assuming
an underlying normal distribution and equate mean plus and minus
one standard deviation as two-thirds probability and mean plus and
minus two standard deviations as 95 percent probability. Financial
data is typically nonnormal, exhibiting asymmetry and signiﬁcantly
more observations several standard deviations from the mean, the
so-called ‘‘heavy tails.’’ These tails are heavy only by comparison
to the normal distribution, not by what is typical in ﬁnance data.
The use of tail area probabilities from the normal distribution is
--- page 45 ---

18
STATISTICAL ARBITRAGE
therefore a frequent cause of miscalculation—and usually that means
underestimation—of risk. Most errors of this kind are trivially
avoided by using the empirical distribution—the data itself—rather
than assumed mathematical forms. Moreover, it is quite simple to
examine the ﬁt of a normal curve to a set of data and judge the
accuracy of probability calculations for intervals of interest, be they
in the tail or center of the distribution. Chapter 5 demonstrates these
points in a discussion of reversion in price series.
With so many potentially costly errors attached to the use of
sample moments (mean and standard deviation) why is the range
so readily abandoned? What has been gained by the sophistry? In
addition to the aforesaid (almost unconscious) action on the part of
many, there is the conscious action on the part of many others that is
driven by mathematical tractability of models. Extreme values (and
functions thereof) are difﬁcult to work with analytically, whereas
standard deviations are generally much easier. For the normal distribution typically assumed, the mean and standard deviation are
deﬁning characteristics and are therefore essential.
While the technicalities are important for understanding and
analysis, the practical value for application in the late 1980s and
early 1990s was minimal: Reversion was evident on such a large
scale and over such a wide range of stocks that it was impossible not
to make good returns except by deliberate bad practice! That rich
environment has not existed for several years. As volatility in some
industries declined—the utilities sector is a splendid example (Gatev,
et al.)—raw standard deviation rules were rendered inadequate as
the expected rate of return on a trade shrank below transaction
costs. Implementing a minimum rate of return lower bound on
trades solved that, and in later years provided a valuable risk management tool.
2.3
POPCORN PROCESS
The trading rules exhibited thus far make the strong statement that
a spread will systematically vary from substantially above the mean
to substantially below the mean and so forth. The archetype of this
pattern of temporal development is the sine wave. In the early years
of pairs trading, that archetype provided the theoretical model for
--- page 46 ---

Statistical Arbitrage
19
(a)
0
20
40
60
80
100
5.5
5.0
4.5
4.0
6.0
(b)
0
20
40
60
80
100
6.0
5.5
5.0
4.5
4.0
FIGURE 2.5
Process archetypes: (a) sinusoidal, (b) popcorn
spread analysis, but many trade opportunities were observed to be
missed. An alternative archetype, which we shall call the ‘‘popcorn
process,’’ shown in Figure 2.5, provided new insight. Reversion to
the mean following a disturbance from that mean was more closely
focused upon. In this model, the constraint on spread motion of
undulation (even if more irregularly than the mathematical archetype)
is removed. An upward motion (move to a ‘‘distant’’ peak) may be
followed, after return to the local mean, by another excursion to a
distant peak. Similarly a decline to a distant trough may follow a
previous excursion to a distant trough without an intervening move
to a distant peak. The qualiﬁer ‘‘distant’’ is used here to distinguish
substantive moves from the mean from minor variation about the
mean. Two troughs are by deﬁnition separated by a peak but a peak
is of trading interest only if it is sufﬁciently removed from the mean
such that movement back to the mean is economically beneﬁcial.
The important point here is that a peak separating troughs can be
near the mean and is not forced or assumed to be substantially above
the mean.
--- page 47 ---

20
STATISTICAL ARBITRAGE
Expressing the popcorn process mathematically is more complicated than writing a sine function, but not much so. If the sine
function is written:
yt = sin(t)
then the popcorn function may be similarly written:
yt = It sin(t)
where It is an indicator function taking values 1 or −1 signaling
a peak or a trough move. The math is not important here; the
insight from the description and graphical depiction of the process is:
Exploiting the popcorn process is not efﬁciently accomplished using
the turtle trade. In Figure 2.5, panel (b), the turtle trade rule identiﬁes
a single trade with proﬁt $2. The popcorn process suggests a rule that
signals to exit a trade when the spread returns to the mean, rather
than assuming it will continue beyond the mean to an extreme on
the opposite side from which the trade was entered. This new rule
identiﬁes four trades with total proﬁt $4. Another novel feature of
the rule is that it contains periods where no capital is committed.
All the necessary calculations for the new rule have already been
described: local mean and range of the spread. The change is to the
trade rule.
Rule 4: When the spread increases (decreases) sufﬁciently far
from the mean (say, k standard deviations) sell (buy) the spread;
unwind the positions when the spread returns to the mean.
Many of the more elaborate models built by statistical arbitrageurs, whether for pairwise spreads or more complicated functions
of stock price histories, are based on the understanding of the popcorn
process, or reversion to the mean, rather than the sinusoidal or turtle
trade process. Chapter 3 describes some of the models and modeling
considerations. The interesting phenomenon of stochastic resonance
(also described in Chapter 3) admits a valuable modiﬁcation of the
exit condition in Rule 4.
2.4
IDENTIFYING PAIRS
The opportunity is huge. We have a set of operational trading rules and
automatic calibration procedures. Now, which pairs can we trade?
--- page 48 ---

Statistical Arbitrage
21
Early on, stocks were grouped by broad industry classiﬁcation
and every pair within those groups was a candidate. Risk management
was rudimentary with Barra models applied to constructed portfolios
and identiﬁed factor exposures offset by trades away from the pair
portfolio (using stocks or Standard and Poor’s (S&P) futures to
neutralize β exposure, for example).
Elaborations were introduced as greater control over return variability became desirable and as experience showed where structural
weaknesses lay. Individual manager preference became inﬂuential
when hedge funds began marketing pairs trading and statistical
arbitrage strategies.
Maximizing correlations was an early ﬁlter applied to pair selection: Compute the correlation of each candidate pair (using, for
example, two years of daily data) and retain only those pairs having correlations greater than some minimum. On the assumption
that past correlation is predictive of future correlation, this ﬁltering
eliminates pairs of stocks that exhibit little or no relationship. The
rationale holds that uncorrelated stocks are behaviorally unrelated
and, hence, unpredictable as a pair.
2.4.1
Reﬁning Pair Selection
Reversion betting on pair spreads works best when the two constituent stock prices continually move apart and together again.
That pattern of behavior, stock A increasing when stock B decreases
and vice versa, generates very low (even negative) correlation. So
from a proﬁt or return perspective, were the early correlation ﬁlters
(searching for a high degree of correlation) quite wrong? No: In
the short term, proﬁts may be forgone by excluding low correlation
pairs but the long-run risk situation is greatly improved. Stocks that
typically exhibit contrary or unrelated price movements are more
likely to respond disparately to fundamental market developments
than stocks that tend to move together. At some point, unrelated
stocks are very likely to create a costly pair trade.
That insight motivates a subtly different approach to the correlation ﬁlter. Deﬁning risk moments (or events) as times when a stock
price trace changes direction such that a peak or trough is formed, it
is desirable for risk minimization purposes to select pairs that show
similar event histories—peaks and troughs close in time with similar
--- page 49 ---

22
STATISTICAL ARBITRAGE
sized moves for the two stocks between these events. Such pairs
are less likely to react divergently (except, perhaps, in the immediate aftermath) following a disturbance to the market (political,
industrial development, etc.). For proﬁt maximization, it is desirable
that between events the two stocks develop along different price
trajectories, exhibiting as much negative correlation—moving apart,
then together—as possible. See Chapter 5 for a formal treatment of
desirable and undesirable pair correlations.
2.4.2
Event Analysis
The turning point algorithm works as follows:
1. A local maximum in the price series is a turning point if subsequently the price series declines by an amount giving a negative
return greater in absolute value than a speciﬁed fraction of the
local, annualized return volatility.
2. Similarly, a local price minimum is a turning point if subsequently
the price rises by an amount giving a return greater than the
speciﬁed fraction of local, annualized return volatility.
3. Look at the price trace in Figure 2.6 (General Motors, daily
adjusted prices). Given a turning point identiﬁed at a, where
is the next turning point? Point a is clearly a local minimum;
therefore, the next turning point must be a local price maximum.
Move forward in time looking at the price series from a to t.
Identify the local maximum price in the interval [a, t]; call it p.
Is the decline from the price at p to the price at t greater than
k percent of the local volatility at t (looking back)?
4. When p = m and t = t1, the answer is no. Not until b is identiﬁed
as the local maximum (t > t2) and then not until t = t3, is the
answer yes.
5. For this example, speciﬁcation is for a window of 20 days to deﬁne
local volatility, an annualization factor of 16, and a turning point
qualifying fraction of 30 percent.
Figure 2.7 shows the General Motors price series again, this
time with turning points identiﬁed with a less demanding criterion:
A decline in price from a peak by 25 percent of the local volatility
qualiﬁes the peak as a turning point. Four additional local extrema are
--- page 50 ---

Statistical Arbitrage
23
80
70
60
50
40
19970102
19970524
19971016
19980312
a
m
b
c
t1
t2
t3
•
•
•
•
•
•
•
•
•
•
•
$
FIGURE 2.6
Adjusted close price trace (General Motors) with 30 percent turning
points identiﬁed
identiﬁed (ignoring the series end point) compared with the default
30 percent criterion. Still, two local peaks and troughs in mid-1997
are not identiﬁed by the algorithm. They provide returns of about
−4 percent in a few days—a fabulous annualized rate of return.
Figure 2.8 shows the General Motors price series once more, with
an even less stringent turning point criterion: A decline in price from
a peak by 20 percent of the local volatility qualiﬁes the peak as a
turning point. Eight additional local extrema are identiﬁed (ignoring
the series end point) compared with the default 30 percent criterion,
the same additional four identiﬁed by the 25 percent criterion plus
another four.
In other examples, changing the window length, the strict capture
by a less stringent criterion of the complete set of turning points identiﬁed by a more stringent criterion is not observed. These examples
and observations serve as reminders that the analysis here is strictly
statistical. The events reﬂect market sentiment but that may be driven
by news unrelated to the stock or by no identiﬁable cause. Finding
such reasons is an analyst’s job.
--- page 51 ---

24
STATISTICAL ARBITRAGE
19970102
80
70
60
50
40
19970524
19971016
19980312
$
FIGURE 2.7
Adjusted close price trace (General Motors) with 25-percent turning
points identiﬁed
Table 2.1 gives a summary comparison of the alternative event
series for the pair Chrysler (before its acquisition by Daimler) and
General Motors. The increase in return correlation for interevent
returns is striking, as are the insigniﬁcant differences across alternative event series. The latter is a useful property—interevent
correlations are robust (not sensitive) to the precise calibration of
the event identiﬁcation algorithm. Therefore, it is not necessary to be
overly concerned about which set of events to use in the correlation
analysis as a screen for good risk-controlled candidate pairs.
Events in trading volume series provide information sometimes
not identiﬁed (by turning point analysis) in price series. Volume
patterns do not directly affect price spreads but volume spurts are a
useful warning that a stock may be subject to unusual trading activity
and that price development may therefore not be as characterized
in statistical models that have been estimated on average recent
historical price series. In historical analysis, ﬂags of unusual activity
are extremely important in the evaluation of, for example, simulation
--- page 52 ---

Statistical Arbitrage
25
19970102
70
80
60
50
40
19970524
19971016
19980312
$
FIGURE 2.8
Adjusted close price trace (General Motors) with 20 percent turning
points identiﬁed
TABLE 2.1
Event return summary for Chrysler–GM
Criterion
# Events
Return Correlation
daily
332
0.53
30% move
22
0.75
25% move
26
0.73
20% move
33
0.77
results. Identifying volume peaks in historical data is scarcely different
from the demonstration of peak identiﬁcation in price histories
documented previously. In live trading, however, forward-looking
monitoring for patterns of increased trading volume, an important
risk management tool, is subtly different. One needs to ﬂag volume
increase during the build-up before a peak is identiﬁable because
identiﬁcation after the fact is usually too late for ameliorating impact
on a portfolio.
--- page 53 ---

26
STATISTICAL ARBITRAGE
2.4.3
Correlation Search in the Twenty-First Century
Several vendors now offer software tools for managing aspects of
pairs trading, from identifying tradable pair candidates to execution
channels and portfolio management. Correlation searches of the type
described here were manually programmed and carried out in the
1980s. No longer is this necessary. Credit Suisse First Boston, for one,
offers a tool that allows a user to optimally ﬁt a Bollinger band–type
pair trading model to any speciﬁed pair of stocks. The program
searches over a range of ﬁxed-width windows simulating trading of
a mean plus or minus standard deviation model; simulation ‘‘proﬁt’’
is the metric used to compare models (data window length, Bollinger
bandwidth) and the maximum proﬁt generating model is identiﬁed.
One can very quickly ﬁt models to many pairs using such tools.
The dangers of relying solely on such shallow data analysis should
be immediately evident. Tools with similar capabilities are offered
by Goldman Sachs, Reynders Gray, and Lehman Brothers, among
others.
At this time, no commercial tools are known to exist that facilitate
identiﬁcation of event or turning points and compute interevent
correlations.
2.5
PORTFOLIO CONFIGURATION AND RISK CONTROL
As models were developed, increasing attention was directed to
portfolio risk control. Mean–variance approaches were favored for
a long time as proﬁts rolled in and risk was deemed ‘‘under control.’’
The folly of that thinking was rudely demonstrated in the summer of
1998, but that is getting ahead of the story (see Chapter 8).
Some modelers incorporated risk exposure calculations along
with return forecasts into the portfolio construction process directly
(see section 2.4, and the description of the defactor model in Chapter
3); others (particularly those whose model comprised a set of rules
with no explicit forecast function) ﬁrst constructed a portfolio, then
calculated the exposure of that portfolio to certain deﬁned market
factors, and controlled risk by hedging those exposures separately
from the bets constituting the portfolio.
The objective is to select a portfolio of stocks that maximizes
return to employed capital. Given perfect foresight, the optimal
--- page 54 ---

Statistical Arbitrage
27
portfolio consists of maximum possible investments in the stocks
with the greatest return until available capital is exhausted. Of
course, we do not have perfect foresight. In its stead, we make do
with the best forecast we have. The goal is still to maximize actual
return but, in the forecasting guess world, we have to focus attention
on expected return.
Forecasts, unlike foresight, do not come with a guarantee of the
outcome. There is risk in acting on forecasts. A single pair spread
expected to ‘‘revert to its local mean’’ may continue to increase
beyond the point at which stop loss limits force exit from the
position. This new element, risk, complicates the goal, which now
becomes twofold: Maximize expected return and maintain the risk
of achieving that return below a certain tolerance.
So far so good. Going from foresight to forecast we exchange
certainty for uncertainty; we move from guaranteed optimization
to constrained optimization of a best guess. However, in practice
matters are not quite as straightforward as that sentence seems to
imply. The ﬁrst obstacle is precisely specifying the notion of risk—or,
at least, its practical implementation. Risk arises because there is no
guarantee that a particular forecast will be borne out in reality.
Indeed, the truth is that it would be an extraordinary event if a
forecast turned out to be 100 percent accurate. Only one outcome
yields complete forecast accuracy. But there is an inﬁnity of possible
outcomes that translate to odds of inﬁnity to one against the forecast
being correct. Hence, the remarkable fact that a forecast is almost
certainly going to be wrong.
‘‘Go for the best’’ becomes ‘‘Go for the best guess—but bear in
mind what disasters might occur and do your best to protect against
those undesirable outcomes.’’
Just as we have to guess at the best (forecast) we have to guess
at the disasters. Typically, we do this a little differently from the
way we look for the best guess: Rather than looking for particular
disaster scenarios we look at the range of disasters—from small to
large—that may befall us. This view is encapsulated in the forecast
variance. (Scenario analysis is often used to be aware of ‘‘unlikely’’
extreme situations notwithstanding routine, daily, ‘‘risk controlled’’
portfolio construction. The distinction of extreme and routine risk is
deliberately vague.)
--- page 55 ---

28
STATISTICAL ARBITRAGE
The goal has, therefore, become: Maximize expected return subject to a limit on believed variation about that expected return. The
variance constraint reduces the admissible set of portfolios from the
set of all portfolios to the set of portfolios for which the expected
variation of the expected return is below some threshold.
It is crucial not to lose sight of the fact that all these quantities—
forecast returns and variances thereof—are uncertain. The forecast
variance guides us as to how much the outcome may reasonably be
expected to deviate from the best guess. But that forecast variance
is itself a guess. It is not a known quantity. And remember what
was stated only two paragraphs ago: Forecast variance characterizes
average behavior; anything is possible on any given instance.
With all those cautionary remarks having been said, it is true
that we are using a forecast constructed in the belief that it has
some predictive utility. That, on average—but not in any particular
case or set of cases—the forecasts will be better guesses of future
events than random guesses. And that the range of variation of
outcomes about the forecasts is reasonably quantiﬁed by the forecast
variances—again, on average.
Finally we are in a position to make operational the notion
and quantiﬁcation of risk. We deﬁned the risk of a portfolio as the
expected variance of that portfolio. Our aversion to risk is then taken
to be a constant multiple of that variance. Thus, the goal becomes:
Maximize expected return subject to a limit on expected variance
of return.
Let us express these results in mathematical form. First, deﬁnition
of terms:
n
Number of stocks in investment universe
f i
Expected forecast return for stock i; f = (f1, . . . , fn)′

Expected variance of returns, V[f]
ip
Value to be invested in stock i; p = (p1, . . . , pn)′
k
Risk tolerance factor
Now the goal is expressed as:
maximize p′f −kp′p
--- page 56 ---

Statistical Arbitrage
29
2.5.1
Exposure to Market Factors
Statistical arbitrage fund managers typically do not want a portfolio
that takes long positions only: Such a portfolio is exposed to the
market. (A pairs trading scheme, by deﬁnition, will not be biased but
statistical arbitrage models more generally readily generate forecasts
that, unless constrained, would lead to a portfolio with long or
short bias.) If the market crashes, the value of the portfolio crashes
with it. This much we can say regardless of the precise composition
of the portfolio. Given a desire for a market neutral strategy, the
goal is to pick off moves in stock prices after allowing for overall
market movement. That begs the question of how one deﬁnes ‘‘the
market.’’ Conventionally, the S&P 500 index is taken as (a proxy to)
the market. Each stock in the portfolio is statistically examined to
quantify the stock’s exposure to the S&P index. These quantiﬁcations
are then used to determine a portfolio’s exposure to the market.
Market neutrality is achieved by altering the proportions of stocks in
the portfolio.
Make the deﬁnition:
li Exposure of stock i to the market; l = (l1, . . . , ln)′
Then the market exposure of the portfolio p is:
market exposure = p′l
With the desire for market neutrality, the objective function is modi-
ﬁed to:
p′f −kp′p −λp′l
where λ is a Lagrange multiplier (relevant only to the optimization).
The neutrality desire is extended from the market as a whole to
include market sectors. We want to avoid overall exposure to, for
example, the oil industry. This is accomplished in the same way as is
market neutrality: Deﬁne exposures of stocks to ‘‘the oil industry.’’
Notice that this is a more general notion than simply deﬁning an
index for the oil industry and exposures of oil industry stocks to that
index. Potentially every stock, oil industry or not, has an exposure
--- page 57 ---

30
STATISTICAL ARBITRAGE
to the oil industry market factor. Given this set of exposures, the
objective function extends in a similar way as for the market factor.
Make the deﬁnition:
l1,i Exposure of stock i to the oil industry; l1 = (l1,1, . . . , l1,n)′
The objective function is extended to:
p′f −kp′p −λp′l −λ1p′l1
where λ1 is another Lagrange multiplier.
Obviously, other market factors may be included in the objective
function to ensure zero portfolio exposure thereto. For q market
factors, the objective function is:
p′f −kp′p −λp′l −λ1p′l1 −· · · −λqp′lq
Determining the portfolio that maximizes the objective function is a
straightforward application of the Lagrange multiplier method.
2.5.2
Market Impact
We forecast IBM stock to yield annualized return of 10 percent over
the next week. The forecast is more certain than any forecast we have
ever made. We want to buy $10 million worth of stock. Ordinarily,
a demand of that size will not be ﬁlled at the current offer price; most
likely the offer price will rise as the demand is ﬁlled. This is market
impact. Market impact is incurred with most trades, regardless of
size, since the market is not static between the time a forecast is
made (using the latest available price) and the time the desired trade
is placed and subsequently ﬁlled. Without actual trading history, it
is impossible to gauge market impact. Even with trading history,
it is possible only to make a guess: Once again we are forecasting
an uncertain event. (See Chapter 10 for recent developments with
critical implications for statistical arbitrage.)
The importance of market impact is great. A good estimate of
the likely realizable ﬁll price for desired trades enables the trading
system to ﬁlter potentially unproﬁtable trades from the portfolio
optimization.
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
