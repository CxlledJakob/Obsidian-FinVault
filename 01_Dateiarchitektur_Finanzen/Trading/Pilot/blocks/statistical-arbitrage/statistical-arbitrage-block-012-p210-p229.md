# Statistical Arbitrage_ Algorithmic Trading Insights and -- Karen M_ Sowers; Andrew Pole -- Wiley Finance, 1, 2007 -- Wiley & Sons, Incorporated, John -- isbn13 9780470138441 -- 6b0138550172e24db7f13c932e054fb9 -- An.pdf — pages 210–229

--- page 210 ---

CHAPTER10
Arise Black Boxes
Felix qui potuit rerun cognoscere causas.
Happy is he who can know the cause of things.
—Virgil
10.1
INTRODUCTION
H
aving invented the pairs trading business two decades ago,
Morgan Stanley was at the forefront of the creation of a new
business in the early 2000s; a less risky, more sustainable business,
which, in a wonderful example of commercial parricide, has systematically destroyed opportunities for old-line pairs trading. Algorithmic
trading was born. Huge order ﬂow from institutions and hedge funds,
much of which is electronically matched in house, provided multiple
opportunities for bounty beyond the expected brokerage fees. Combining the insight and knowledge learned from proprietary trading
(beginning with the classic pairs trading business) with analysis of
a warehouse of order ﬂow data, Morgan Stanley and other brokers
built trading tools that incorporate models for forecasting market
impact as a function of order size and time of day, moderated by
speciﬁc daily trading volume stock by stock.
Recognizing that there was an enormously lucrative opportunity
hanging on simple to use, automatic trading technology that did not
systematically incur slippage, brokers elected to offer the tools to
clients. It was a masterfully timed decision. Coming as new statistical
arbitrageurs were appearing with abandon, vendors were able to
seduce those whom their tools would eventually help destroy, along
with existing clients thirsting for any new edge that had the promise
183
--- page 211 ---

184
STATISTICAL ARBITRAGE
of lower transaction costs or marginal improvements in execution
price. The genius of the business was compounded as the institutional
and statistical arbitrageurs’ order ﬂow provided an ongoing feast of
data for the data miners whose voracious appetite for such cannot
be sated.
Patterns of transaction volume by stock, by day of the week, by
time of day, and by current day’s trading volume were constructed
from the mined data. The mere ability to predict with measurable
efﬁcacy how much would be given up from current price to buy or
sell a speciﬁc number of shares in a ﬁxed period was a stunning
development to traders. Hedge funds had for years made their own
attempts; using their much less rich data than broker archives it is
unlikely their achievement matched the brokers’ success. Regardless,
an edge was eliminated.
Fitting logistic-type models to order ﬂow and ﬁll data quickly
produced the ﬁrst generation of models, allowing traders to obtain
quantitative answers to frequently faced, urgent questions:
■How much will I have to pay to buy x thousand shares of XYZ
in the next half hour?
■How much will I have to pay if I wait the remainder of the
trading day?
■How much can I sell of XYZ in one hour keeping the impact to
k cents?
An unadvertised beauty of these tools is the self-propagating
nature of the opportunity set. As traders switched to the technology,
a new set of order ﬂow information was presented to and collected
by vendors. Now it was possible to examine the trading of both the
impatient ‘‘pay up and get it done’’ and the relaxed ‘‘wait and see’’
players. Models of client proﬁles, built automatically from the client
order ﬂow, trading tool conﬁguration, and ﬁll/cancel–correct records
practically generate themselves. With the ability to gauge how much
a client would be willing to pay for a ﬁll, and estimates of how long
it would take to get the trade at much lower market impact, the
many possibilities fairly screamed themselves to researchers, echoing
and amplifying the old-line pairs trade screams heard by a previous
generation two decades earlier.
--- page 212 ---

Arise Black Boxes
185
All of this opportunity offered itself for reaping without requirement of capital commitment. The risk of proprietary trading was
eliminated and the ‘‘new’’ business became inﬁnitely scalable.
Morgan Stanley has competitors, of course. Algorithmic trading
tools have been developed and marketed by Goldman Sachs, Credit
Suisse First Boston, Lehman Brothers, Bank of America, and others.
10.2
MODELING EXPECTED TRANSACTION VOLUME
AND MARKET IMPACT
The place to begin is the data mine. What data is available and
which of it is pertinent to answering the ‘‘How much. . . ?’’ questions.
Suppose that for stock XYZ there is a history of daily transaction
volume data by individual trade, for over ten years. That is 2,500
days of daily transaction material. The ﬁrst thing to do is examine
the cumulative trade volume by day: Every stock has a distinctive
character to its pattern of trading over the day, a footprint if you
like. Using a one-shoe-ﬁts-all approach, forecasting an elephant’s
footprint using a generic mammal footprint may work but will suffer
from needlessly large inaccuracies (noise or error variance). Worse
would be to use an asp’s footprint (try to describe it). You can see
the problem.
The problem is easily addressed by applying a modicum of speci-
ﬁcity in the data analysis and model building. Computers don’t care
how many model variants they process. You should care, however;
overspeciﬁcity where it is unnecessary also leads to over-large prediction variance because a ﬁnite data resource does not yield an inﬁnitely
divisible reservoir of information. The more the data is carved into
different animals, the less information there is on each. If two or more
animals are essentially identical (for the purpose under investigation)
the data is best pooled. Moreover, the more models one tests on data,
the greater the likelihood of ﬁnding a spuriously good ﬁt. These are
well known, though often ignored, details of good applied statistical
analysis.
Begin looking at the data with a view to identifying a trading
day pattern in transaction volume. How to characterize it? While
it is unlikely that the daily pattern ten years ago is close to the
daily pattern today, it would be inadvisable to assume so. Remember
--- page 213 ---

186
STATISTICAL ARBITRAGE
that reversion patterns exploited by the original pairs trade persisted
with economically exploitable frequency and magnitude for a decade
and a half before technological and market developments caused a
dramatic change. Examine some daily cumulative transaction volume
charts from ten years ago, some from ﬁve years ago some from this
year. You will notice a similar form to the graph (curve) but obvious
differences—faster cumulation early in the day and again late in the
day comparing recent patterns to earlier patterns. Better not simply
aggregate all the data and estimate an average curve then.
Look more closely at daily patterns for the last three months.
That is 60 charts. Examine a three-month set from ten years ago.
You notice quite a lot of overlap in the basic shapes. But look at the
scales: The stock trades at much higher volumes now than it did a
decade ago. Hmmm. Rescale the graphs to show cumulative percent
of daily total volume. Now all graphs are on the same 0–100 scale.
Aha! There is much less variability in the patterns of the last quarter.
So, whether a given day is relatively high or relatively low volume, a
similar pattern for the trading over the day is revealed.
How do we use this insight? One goal is to represent the curve (of
cumulative percentage trade volume in a day) in a way in which it will
readily yield the proportion of a day’s trade volume in the market at a
speciﬁc time. In other words, to provide a ready answer to questions
such as, How much of the volume is transacted by 2 p.m.? There are
many mathematical functions that have the generic S shape required:
Cumulative density functions of probability distributions provide a
natural set since distributions are precisely what are being examined
here. A convenient form for statistical model building (which we
have not yet considered) is the logistic function.
Pick a function. Fit it to the data. You can now readily make
sensibly quantiﬁed stock-speciﬁc responses to the question: How
much of the day’s volume is transacted by 2 p.m.? On average . . .
Now today happens to be a reasonably heavy trading day for the
stock, with 4 million shares traded by 11:30 a.m. How many shares
are expected to trade by 2 p.m.? From the estimated pattern, fully
30 percent of the day’s volume is typically transacted by 11:30 a.m.,
and 40 percent by 2 p.m. Easily you compute 1.3 million shares
are expected to trade over the next 90 minutes. You want to trade
100,000 shares. Should not have to pay much to achieve that. Right?
--- page 214 ---

Arise Black Boxes
187
The foregoing analysis considered only transaction volume; price
information in the record has not yet been examined. Let’s redress
that directly. In the set of 60 days of trading data for XYZ, there
are many individual buy and sell transactions for order sizes as small
as 100 shares to as large as 100,000 shares. The ﬁll information for
all orders is also recorded. Plotting order size against the change in
price from the order price (or market price at time of order) and the
average ﬁll price shows a deﬁnite relationship (and a lot of variation).
Once again, some of the variation magically disappears when each
day is scaled according to that day’s overall volume in the stock.
Orders, up to a threshold labeled ‘‘visibility threshold,’’ have less
impact on large-volume days.
Fitting a mathematical curve or statistical model to the order
size–market impact data yields a tool for answering the question:
How much will I have to pay to buy 10,000 shares of XYZ? Note
that buy and sell responses may be different and may be dependent
on whether the stock is moving up or down that day. Breaking down
the raw (60-day) data set and analyzing up days and down days
separately will illuminate that issue. More formally, one could deﬁne
an encompassing statistical model including an indicator variable for
up or down day and test the signiﬁcance of the estimated coefﬁcient.
Given the dubious degree to which one could reasonably determine
independence and other conditions necessary for the validity of such
statistical tests (without a considerable amount of work) one will
be better off building prediction models for the combined data and
for the up/down days separately and comparing predictions. Are
the prediction differences of practical signiﬁcance? What are the
differences?
One drawback of ﬁtting separate models to the distinct data
categories is that interaction effects (between volume, up/down day,
buy/sell, etc.) cannot be estimated. If one is looking for understanding, this is a serious omission as interactions reveal subtleties of
relationships often not even dimly suggested by one-factor-at-a-time
analysis. If one is looking for a decent prediction, the omission is intellectually serious (if there are interactions) but practically (depending
on the nature of the interactions) of less import.
Time of day is also signiﬁcant in market impact estimation—recall
the analysis of the cumulative trading volume pattern over the day.
Filling an order during the ‘‘slow’’ or more thinly traded part of the
--- page 215 ---

188
STATISTICAL ARBITRAGE
day requires either more patience for a given slippage limit or a willingness to increase that limit. Time of day was not addressed in the
order size–market impact analysis outlined previously. Obviously it
can be, and the obvious approach is to slice the data into buckets
for the slow and not slow parts of the day (or simply do it by, say,
half-hour segments) and estimate individual models for each. While
the statistical modeling and analysis can be made more sophisticated, the simple bucketing procedure posited here serves to exemplify
the opportunity and the approach. (Examples of fruitful sophistication include formally modeling parameters across time slices with
a smooth function, and employing classiﬁcation procedures such as
regression trees to identify natural groupings.)
10.3
DYNAMIC UPDATING
Examining the basic patterns of daily trading volume from ten years
ago and more recently has prompted the realization that patterns
have changed. Immediately one is confronted by the problem of
how to manage the change in predictive models estimated from
the data. The ﬁrst action was to use only recent data to build the
model to use now. We’ll assume recent time at 60 days. Now one
is confronted by the question, When should the models be revised?
We are once again faced with the questions about types of change,
rates of evolution, and methods of dynamic updating that were
discussed with respect to the reversion models in Chapter 2. The
basic issues here are no different. One might reasonably elect to use
a rolling 60-day window, reestimating modeled relationships each
day. One might also routinely compare the latest daily pattern with
the distribution of patterns seen (a) recently or (b) further distant
in time to make a judgment about whether today is unusual. If
it is, perhaps it would be wise to apply a ‘‘conservatism ﬁlter’’ to
the forecasts? A measure of the rate of change could be devised
(there are standard ways of comparing probability distributions,
from summary statistics, including moments, to integrated measures
of information), and employed to build a general dynamic updating
scheme that is more ﬂexible than the simple 60-day moving history
window.
--- page 216 ---

Arise Black Boxes
189
10.4
MORE BLACK BOXES
We have deliberately singled out Morgan Stanley at the beginning of
the chapter because of the link to the genesis of our major theme:
statistical arbitrage. But Morgan Stanley is not the only ﬁrm to
have analyzed transaction data and offered tools to the marketplace
encapsulating trading intelligence discovered therefrom. Goldman
Sachs’ operations on the ﬂoor of the NYSE—the Spear, Leeds &
Kellog specialists bought in 2000—represent a gold mine potentially
even more valuable than Morgan Stanley’s database. Bank of America
bought the technology of hedge fund Vector in 2002: ‘‘. . . computer
algorithms will factor in a particular stock’s trading characteristics
and BofA’s own position in it then generate buy and sell quotes’’
(Institutional Investor, June 2004; italics added for emphasis). Credit
Suisse First Boston (CSFB) hired a former employee of the renowned
and technologically advanced hedge fund D.E. Shaw, and built a tool
that ‘‘processes fully 40% of its [CSFB’s] order ﬂow’’ (Institutional
Investor, June 2004); Lehman Brothers and more than a dozen others
are also in the business.
In addition to the developments just listed, at least one new
brokerage, Miletus, has been spun out of a billion dollar hedge
fund to monetize the value in the trading algorithms developed for
the hedge fund’s own trading. In another technology driven development, beginning with Goldman Sachs in late 2006, at least two
offerings of general hedge fund replication by algorithmic means have
been brought to market. As these instruments gain popularity there
are likely to be new systematic pattern generating forces added to
the market.
10.5
MARKET DEFLATION
Figure 10.1 depicts the market for buying and selling stocks, a generic
market where buyers and sellers come together to agree on a price
for mutually acceptable exchange of ownership. There are many
buyers and many sellers. Lots of individual excitors. Many points of
agreement. Substantial volatility.
Figure 10.2 depicts the arriving market for buying and selling
stocks. The many individual buyers and sellers come together by
--- page 217 ---

190
STATISTICAL ARBITRAGE
Buyers
Sellers
MARKET
high volatility
FIGURE 10.1
The way the market was
MARKET — low volatility
r   e   s   i   d   u   a   l
algorithm 4
buyers
sellers
sellers
buyers
sellers
buyers
algorithm 17
algorithm 24
FIGURE 10.2
A deﬂated market model
the intermediating management of a handful of computer algorithms
which internally cross a substantial portion of orders and satisfy
the residual by restrained, unexcitable exchange in the central
market. There are many buyers and sellers. Many points of agreement. But less unmitigated agitation than the traditional bazaar.
Constrained volatility.
--- page 218 ---

CHAPTER11
Statistical Arbitrage Rising
. . .to worry about everything is unnerving. It is also
counterproductive, for it can result in continual tinkering
with a correctly operating system in response to imagined
phantoms in the data.
—Statistical Control by Monitoring and Feedback
Adjustment, Box and Luceno
B
y the end of 2004, statistical arbitrage practitioners had been
beleaguered for a year. Investors and commentators cite performance volatility but no return set against market advance (in 2003);
adduce accusative assertions of irreversible decline from visible market changes; and largely turn deaf ears to the necessary complexity
of the reality (see Chapters 9 and 10 for a full exegesis).
Set against that siege is the present discourse and a return of
performance since 2006. Chapters 2 to 8 set out the nature and
extent of traditional statistical arbitrage opportunities, approaches to
formal modeling and systematic exploitation of those opportunities,
the nature of market dynamics that wreaks havoc on portfolios
built and managed according to statistical arbitrage models. Chapter
9 examines one-liner condemnations of the discipline, the logic of
which is: This change eliminates a part of statistical arbitrage return;
the change is permanent; your opportunity set is therefore gone. The
claims are found pertinent but inadequate to explain the record. The
far more complex reality is no less devastating but, upon deeper
reﬂection, cannot support condemnation. In their complexity, the
enduring elements are not wholly destructive of statistical arbitrage.
To the contrary, some of the more far-reaching market structural
191
--- page 219 ---

192
STATISTICAL ARBITRAGE
changes, set out in Chapter 10, necessarily create conditions for
a new statistical arbitrage paradigm. That emerging paradigm, its
driving forces and consequent statistically describable and therefore
exploitable stock price patterns, is set out in this chapter. It both
concludes the present volume and sets the scene for a subsequent
history to be written some years hence.
A few statistical arbitrage practitioners with long and outstanding performance pedigrees continued to deliver reasonable to good
returns while most have failed as described in earlier chapters.
This evidence supports the claims of (a) incomplete destruction of
traditional statistical arbitrage opportunities and (b) genesis and
development of new opportunities, though only proprietary information could reveal to what extent the evidence supports each claim
individually. Evidence in the analysis of the public record of stock
price history strongly suggests that the opportunity for extracting
outsize returns from high-frequency trading—intraday—is huge.
From the discussion throughout this book, it is clear that exploiting
that opportunity requires different models than the traditional mean
reversion type. Some such models are described later in this chapter.
Patterns of stock price movements within the trading day show
not reversion but momentum. There are also patterns of reversion
within the day but these patterns seem to be difﬁcult to predict
(though there are claims for success here); they occur spasmodically for broad portfolios, with precursor signals that are not easily
identiﬁed. Indeed it may be inappropriate to label the movement
as reversion; reversal may be more indicative of the dynamic. The
distinction is crucial. A reverting process assumes an underlying equilibrium to which price (or relative prices) tends to return following a
disturbance away from it (the popcorn process). Equilibrating forces
can be identiﬁed. The trends and reversals process makes no such
underlying assumption of equilibrium; rather, the process is one that
moves for more or less extended periods in one direction and then
in the other without a strong link from the one move to the next
(a memoryless switching process). Critical to the description and
assessment are the duration and magnitude of the directional moves:
They endure sufﬁciently long (think of sufﬁciently many time steps
where each step is visible to a person) and the move is large enough
to be exploited systematically, given necessary lags for turning point
identiﬁcation.
--- page 220 ---

Statistical Arbitrage Rising
193
Crucial to successful modeling is an understanding of the forces
in the market driving the trend creation. Penny moves are one
important factor, having already removed price friction eliminating
historically innate initial resistance to repeated (and therefore cumulatively large) moves. Compounding this is the increasing removal of
human specialists from the price setting process as more trades are
crossed automatically on electronic exchanges and by the brokerage
houses’ trading programs described in Chapter 10. Most signiﬁcant
are those ‘‘intelligent’’ trading engines and the signiﬁcant proportion
of transactions preempted as VWAP or TWAP. Old-line technical
analysis may, curiously, retain some efﬁcacy in exploiting the new
intraday trend patterns; but greatest success will inhere to those
whose modeling incorporates knowledge of the underlying motive
forces and algorithmic trading tactics.
Far removed from underlying equilibrating forces, driven by people making judgments of fair valuation of company prospects both
shortand long-term, the new paradigm is one of unemotional—
uninterested—rule-based systems continually probing other similar
entities. The process is mechanistic as in a geological process, water
ﬁnding the lowest level. Here, however, the rules are deﬁned by
human modelers and not the laws of the physical universe, and they
are changeable. Noise is omnipresent as human traders still directly
preempt a sizable chunk of market activity and originate all transactions. Notwithstanding the noise, the new forces for equilibrium are
searching not for fair relative prices but fair (mutually accepted by
participating entities) market clearing. This new paradigm may be
a reversion (!!!) to an age-old paradigm of economics: perfect competition. Now, on that train of thought one might conjure ideas of
dynamic cobweb algorithms, game theoretic strategies, and perhaps
a necessary repositioning of research into behavioral ﬁnance.
Volatility will remain consumed by the algorithms. Instead of
human-to-human interaction either face-to-face on the ﬂoor of the
NYSE or face-to-screen-to-face in electronic marts, there will be
algorithm-to-algorithm exchange. A large and growing part of the
emotion surrounding trading is removed, and with that removal
goes volatility. Yet in this focus on algorithms, we must not forget
that people still drive the system. With trades managed by algorithms implemented on incredibly fast processing computers, what
might be done by algorithms designed to go beyond passive market
--- page 221 ---

194
STATISTICAL ARBITRAGE
participation to active market determination? Possibly probing other
algorithms for weakness, for opportunities to subvert naivete, or to
mislead into false judgment. Warfare by another name. The attraction for certain managers and the challenge for certain programmers
is irresistible.
Speculation of course, I think.
11.1
CATASTROPHE PROCESS
Since early 2004, spread motions have been observed to exhibit an
asymmetric process where divergence is slow and continuous but
convergence—the ‘‘reversion to the mean’’ of old—is fast(er), even
sudden by comparison. Convergence is not necessarily ‘‘to the mean’’
though it is in the direction of a suitably local view of the mean.
The ﬁrst two characteristics contrast with those of the popcorn
process, which exhibits a faster-paced departure from the norm and
slower return. The third characteristic, the degree of reversion to an
underlying mean, also distinguishes the two processes: In the newly
emerging process, the extent of the retrenchment move is far more
variable than was the case for the popcorn process.
Now we enter a deﬁnitional quagmire, so careful examination
and explication at length is desirable.
Contrast the classical popcorn process with the new process
using Figure 11.1. The notable features of the new process are:
a slow, smooth divergence from local equilibrium; fast reversion
toward that former equilibrium; partial reversion only (in most
cases); repeated moves in quick succession delineating a substantive
local trend away from the underlying equilibrium. (The latter is, as in
all archetypal illustrations, depicted as a constant level. In practice,
it is superimposed, on long-term trend movements—for a positive
trend, turn the page counterclockwise by several degrees to view the
archetype.)
The critical departure in this new ‘‘catastrophe’’ model is the
appearance of local trends within the period classically depicted as
sufﬁciently local to be constant. The local trend (within a trend) must
now be depicted and formally incorporated in the analysis because
it is part of the opportunity driver and is crucial to the successful
exploitation of the new reversionary moves. It cannot be ignored as
noise on an underlying (popcorn) process.
--- page 222 ---

Statistical Arbitrage Rising
195
(a)
0
20
40
60
80
100
4.0
4.5
5.0
5.5
6.0
(b)
0
20
40
60
80
100
4
6
8
10
12
A
B
C
FIGURE 11.1
(a) Archetype of the popcorn process showing reversion to a mean
(b) New archetype: catastrophe process
The combination of variable amounts of ‘‘reversion’’ and multiple moves in the same direction before a larger directional shift (singly
or, again, multiple small events) is driven by the interaction of algorithmic trades. (There may be other drivers, but they remain elusive
at this time.) Patient algorithms ease up when prices move repeatedly, penny by penny by penny—moves that specialists are keen on
following the change to decimalization and which are undoubtedly
programmed into some algorithms. What used to be a certain inertia
to moves when tick size was substantive, an eighth, is now eagerness
to repeatedly penny. Pennying was ridiculously lucrative at ﬁrst when
human traders still dominated order ﬂow. The patience and discipline
of algorithms having replaced direct trader involvement have altered
the dynamics of the interaction. The results, which seem now to be
clear, are the catastrophe moves we have described.
Notice the implications for the popcorn process model applied to
the catastrophe process relative price evolution: zero return.
A natural question to ask is, What happens over a longer timescale
than that encompassed in A–C in Figure 11.1? The description just
--- page 223 ---

196
STATISTICAL ARBITRAGE
5.0
5.2
5.4
5.6
5.8
6.0
6.2
5
10
15
FIGURE 11.2
Extended popcorn move with catastrophe moves in detail
given, serial moves in one direction punctuated by partial retrenchment, then essentially the same in the opposite direction, as shown
in Figure 11.2, and variant in Figure 11.3, sounds like little more
than a sharper focus on the popcorn process, as if one simply turned
up the magniﬁcation to see more of the uninteresting, picture clouding, uneconomic detail. The proper interpretation is to extend the
time-scale so that the micro moves on the popcorn process become
as time signiﬁcant as the original popcorn move itself. Thus, the popcorn move may require as many as six (or even more) catastrophe
moves to complete—a long time in a dynamic market. Popcorn’s
return even under these ideal conditions is reduced many fold. But
the true picture, returning to Figure 11.1, is seriously worse. Over
the long time period just suggested, the local mean shifts more than
can be assumed away, invalidating the basic popcorn process. At
best, the outcomes become distributed across a range in which the
uninteresting values detract greatly from the interesting, as shown
in Figure 11.4, converting an exploitable structure to a textbook
or journal curiosity. Over the extended duration, the bet becomes
a fundamentally dominated play; for the statistical popcorn process
--- page 224 ---

5
10
15
5.0
5.2
5.4
5.6
5.8
6.0
6.2
FIGURE 11.3
Variant on extended popcorn move
5
10
15
20
25
distribution of outcomes very
variable because of extended
elapsed time
5.2
5.4
5.6
5.8
6.0
FIGURE 11.4
Extended popcorn move has variable result
197
--- page 225 ---

198
STATISTICAL ARBITRAGE
not predicated on fundamental analysis, forecast power evaporates
and the return along with it.
11.2
CATASTROPHIC FORECASTS
The magnitude of a catastrophe reversion is not accurately forecast
in comparison to forecasts of the popcorn process. But the great
variation in results from both systems, popcorn applied to popcorn
data, catastrophe to catastrophe data—and where is the cutoff?
Say pre-2002 for popcorn, post–mid-2004 for catastrophe, with
the intermediate 18 months dominated by disruptive inﬂuences of
change—means that for a large collection of bets, the statistical
measure R2 is similar. The signiﬁcance of that observation for trading
is an overall expectation of similar rates of return if the number of
bets in a reasonable period is similar and the overall variation in
the two sets of bets is also similar. Reality, of course, is not so
obligingly straightforward. As the catastrophe process has come
to characterize spread motions more accurately than the popcorn
process, general levels of spread volatility have been decreasing (see
Chapter 9). Before 2003, when the popcorn process provided a valid
representation of spread motions, volatility was nearly double that
prevailing in late 2004, when the catastrophe process provided a
more accurate model. These outcomes are not coincidental. Both are
driven by the increasing market penetration of trading algorithms (as
described in Chapter 10).
A reduction in overall variance of which a similar fraction is
captured by model forecasts—on the face of it, that is a recipe for a
reduction in return commensurate with the variance shrinkage. But
the face, too, is altered, in the shape of shorter duration moves and a
greater frequency of moves. The resulting increase in the number of
bets counters the lower revenue from individual bets. It is a partial
counter only and is itself countered in turn by transaction costs of
the increased bet count. Continued downward pressure on brokerage
and trading technology fees has been and will continue to be an
inevitable result.
At this point the critical question to answer is, How can systematic exploitation, trading the catastrophe signals, yield desirable
economic results?
--- page 226 ---

Statistical Arbitrage Rising
199
Ideally, one would like to identify the beginning of a catastrophe
jump just before it occurs, allowing sufﬁcient time to make a bet
without market impact, and identify the end of the move soon after
it is over to allow maximal capture of the catastrophe. Neither
identiﬁcation task has proven easy thus far, but approximations
based on duration measures have been established.
Return to the growth and drop (or decline and jump, if you prefer
the antithetical reversion) archetype catastrophe shown in Figure
11.5. Focusing on the build-up to the catastrophic move, one can
identify a duration rule that signals a bet entry k periods following the
start of the trend development. That trend onset becomes known only
several periods into the move. Statistical analysis reveals a distribution
of trend durations preceding a catastrophic retrenchment, and bet
entry is signaled at a ﬁxed point of that distribution. The eightieth
percentile is a good operating rule.
Timely identiﬁcation of the discontinuity, the change from divergence to reversion, is critical to successful exploitation of catastrophe
moves. There is much less statistical forgiveness in the timing of a
bet entry than was the case for popcorn moves. The relative speed of
0
10
20
30
40
50
0
20
40
60
80
100
A
B
C
D
FIGURE 11.5
Catastrophe move archetype
--- page 227 ---

200
STATISTICAL ARBITRAGE
the catastrophe reversion makes the opportunity loss from late identiﬁcation of a catastrophe much greater than for late identiﬁcation
of a popcorn move. Failure to enter before the cliff edge, point C
in Figure 11.5, essentially means missing the full opportunity. The
popcorn move seen in Figure 11.3 is quite different. Late entry will
lower return on a bet, but only marginally. Modeling and trading
catastrophe moves must embody a higher state of alertness.
11.3
TREND CHANGE IDENTIFICATION
There is a rich statistical literature on change point identiﬁcation
with many interesting models and approaches providing plenty of
fascination. Our purpose here is mundane by comparison, though
challenging nonetheless. (If any kind of pattern recognition in ﬁnancial data were not so challenging, we would hardly be writing and
reading about it.) An extremely useful approach from statistical
process control relies on Cuscore statistics (Box and Luceno 1987).
Consider ﬁrst a catastrophe superimposed on an underlying rising
series. Figure 11.6 shows a base trend with slope coefﬁcient 1.0 with
a catastrophe move having slope coefﬁcient 1.3 beginning at time
10. Let’s see how a Cuscore statistic for trend change works in this
readily understood illustration. The Cuscore statistic for detecting a
change in trend is:
Q =

(yt −βt)t
where yt is the series of observations, β is the regular slope coefﬁcient
(the rate of change in the observation series per unit time1) and t is a
time index. The Cuscore is shown in the lower panel of Figure 11.6.
Despite having seen many such graphs for many kinds of time series,
1Models for parametric change have much wider applicability than just time indexed
series, which is our focus here. Spatial models, where observation series are indexed
by geographic location rather than sequentially in time, are employed in many
sciences from geology to seismology (which often has both time and space indexing)
to biology (EEG readings form speciﬁc patterns across the head as well as particular
temporal development at each site). In stock price analysis, indexing by trade
volume is employed in trading algorithms (see Chapter 10) and by some statistical
arbitrageurs.
--- page 228 ---

Statistical Arbitrage Rising
201
(a)
5
10
15
20
5
10
15
20
0
0
50
100
150
200
10
5
15
20
25
30
(b)
FIGURE 11.6
Identiﬁcation of trend change: (a) gradient 1.0 shifts to 1.3 at time
11; (b) Cuscore
I never cease to be amazed at the seemingly magical way in which the
detection statistic uncovers and displays the incontrovertible evidence
of change. The slope increase of 30 percent from initial value 1.0
to subsequent value 1.3 looks, as just written, substantial. Thirty
percent is nearly one-third and that surely is substantive and ought
to make us take notice. But the graph generates a very different
perception. Were it not for the dashed continuation line, we would
be hard-pressed to notice the kink in the line at time 10. The visual
discordance is too small. Pictures may paint many words but here is
a case in which the words are more dramatic.
The dramatic shift from constant to exponential increase in the
Cuscore statistic recovers the situation efﬁciently and effectively.
Now, how does the Cuscore perform when observed values do
not fall neatly on prescribed mathematical lines? Figure 11.7 adds
random noise (Student t distribution on ﬁve degrees of freedom, a
heavier tailed distribution than the normal) to the series depicted
in Figure 11.6. If the slope increase was visually difﬁcult to discern
previously, it is practically impossible now. How does the Cuscore
statistic fare?
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
