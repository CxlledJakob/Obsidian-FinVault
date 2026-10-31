# Statistical Arbitrage_ Algorithmic Trading Insights and -- Karen M_ Sowers; Andrew Pole -- Wiley Finance, 1, 2007 -- Wiley & Sons, Incorporated, John -- isbn13 9780470138441 -- 6b0138550172e24db7f13c932e054fb9 -- An.pdf — pages 172–191

--- page 172 ---

Nobel Difﬁculties
145
breaking down; if the breakdown applies to the underlying common
structure of the stock return series, then the stocks will cease to satisfy
pair selection criteria and trading will cease. If the common structure
remains, with spreads oscillating about a new level or returning to
the recent historical level, the stocks will continue to be selected and
will again be traded proﬁtably once the disturbance is over.
On Thursday August 20, 1998 the takeover of SAI by AIG was
announced. SAI closed on Wednesday at $64 3
8 the all stock deal
valued SAI at a 25 percent premium (before the market opening).
One might seriously wonder at the nature of the buying pressure
behind the run-up in price of SAI before the takeover.
8.3
RISE OF A NEW RISK FACTOR
The international credit crisis of the summer of 1998 was an interesting time for the practice of statistical arbitrage. Performance
problems began in June and, for many, accelerated through July and
August. During this time, it became starkly apparent for the ﬁrst time
that perceptions about the credit quality of a company had a direct
impact on investor conﬁdence in near-term company valuation. As
sentiment became negative and stocks were marked down across the
market, the magnitude of price decline was strongly related to the
credit rating of outstanding corporate debt. Companies with lower
rating had their stock price decimated by a factor of three to one
more than companies with a higher rating. Such dramatic discriminatory action had not previously been described; certainly there was
no prior episode in the history of statistical arbitrage.
There are many hypotheses, fewer now entertained than was the
case at the time, about the nature of the linkages between credit and
equity markets in 1998, and why the price movements were so dramatic. Without doubt, the compounding factor of the demise of the
hedge fund Long-Term Capital Management and the unprecedented
salvage operation forced by the Federal Reserve upon unenthusiastic
investment banks heightened prevalent fears of systemic failure of the
U.S. ﬁnancial system. At the naive end of the range of hypotheses is
the true, but not by itself sufﬁcient, notion that the Fed’s actions simply ampliﬁed normal panic reactions to a major economic failing. An
important factor was the speed with which information, speculation,
gossip, and twaddle was disseminated and the breadth of popular
--- page 173 ---

146
STATISTICAL ARBITRAGE
coverage from twenty-four hour ‘‘news’’ television channels to the
Internet. The large number of day traders and active individual participants drawn into the market during the 1990s by the attraction of
the bull run, and trading made easy by technological developments,
provided a receptive audience for the broadcast noise and a fertile
environment in which to germinate and breed fear and panic. There
was much poor decision making borne of instantaneous judgments,
couched as ‘‘analysis’’ though often little more than the rambling of
the moment to ﬁll immediate desire for sound bites, speedily implemented by the facilitating technology. Good for volatility and studies
of lemming-like behavior in cognitively higher order species, bad for
blood pressure and ulcers.
When the impact of the Russian default began to be experienced
on the U.S. stock markets, concern grew that companies would be
progressively squeezed in the market for credit and this concern
led to stock price markdowns. As the crisis continued and stock
prices declined, the prices of companies with lower credit rating
declined faster and cumulatively by more than prices of companies
with higher credit rating, existentially proving the prevalent fear,
rational or not, that tightening credit markets (the link from the
Russian default to this outcome internationally or speciﬁcally in the
United States not convincingly, coherently made) would make raising
ﬁnance more expensive. And what could be more logical than that
poorer rated companies would have to pay more? The apparent logic
for discriminatory stock price realignment looks unassailable on the
surface. Since that is as far as much ‘‘analysis’’ went (and goes) the
consequences were those of self fulﬁlling prophecy. Was there ever
a likelihood of U.S. interest rates being raised as a result of the
Russian default?
Corporate debt rating became a signiﬁcant discriminatory factor
in U.S. equities in the summer of 1998. Any portfolio constructed
absent attention to this factor was likely to be exposed to valuation
loss directly as the lower rated stocks’ prices declined more than
proportionately compared with higher rated stocks. Whether constructed as a collection of matched pairs from a vanilla pair trading
strategy or from a sophisticated factor-based return prediction model
makes no difference at the outset. Losses are inevitable.
As the discriminatory stock price patterns developed, discriminatory results distinguished types of statistical arbitrage strategy,
--- page 174 ---

Nobel Difﬁculties
147
though manager action in the face of persistent and cumulatively
large losses complicates assessment: the mix of model versus manager (to the extent that is meaningful) being impossible to identify.
Simulation studies devoid of manager contamination indicate that
factor models exhibited more resilience1 than pure spread-based
models, and quicker resumption of positive returns.
With recognition of a new risk factor, what should be done?
Factor models, when the factor decomposition is recomputed using
return history from the period affected, will naturally incorporate
‘‘debt rating,’’ so direct action is not necessary. Inaction does beg
a few questions though: What should be done during the evolving
episode once the factor has been identiﬁed (or posited at least)? Is the
best one can do simply to wait for a new window of data from which
to estimate stock exposures to the factor (and meanwhile take a
performance wallop to the chin)? Answer to the latter is obvious but,
beyond a simple ‘‘No,’’ sensible prescriptions are more demanding
to compose. General speciﬁcation of the foremost requirement is
direct: Eliminate exposure to the posited factor from the portfolio.
Precise action to accomplish that is a tad more difﬁcult—what are
the exposures? In the haste necessitated by the strong emotional push
and business need to staunch losses, luck played its role.
1From where does this greater resilience derive? A partial answer can be constructed
by contrasting a basic pair strategy with a basic factor model strategy (which models
are precisely the source of the simulation results on which the evidential commentary
is made). The pair portfolio consists of bets on pairs of stocks that are matched
on standard fundamental measures including industry classiﬁcation, capitalization,
and price–earnings ratio. A ﬁrst-order DLM forecast model is assumed for the
spread (using the log price ratio series), with an approximate GARCH-like variance
law. Bets are made when the spread deviates from its forecast by 15 percent or
more (annualized). All signaled bets are taken and held until the model generates
an exit signal; bets are not rebalanced; no stop loss rule is applied. The factor
model is constructed as described in Chapter 3, with the optimization targeting
annualized 15 percent for comparison with the pair model. Positions are rebalanced
daily according to forecasts and factor exposures.
There is some evidence that credit rating was correlated with a combination
of the structural factors estimated for the factor model. To the extent that is true,
robustness of model performance to the new risk factor is clearly imparted. The
raw stock universe to which the factor analysis is applied (the trade candidates)
has some impact on results, as it does for the pair strategy. Nonetheless, with the
matched stock universe, the factor model displayed desirable performance robustness
compared with the pair model.
--- page 175 ---

148
STATISTICAL ARBITRAGE
And what of nonfactor models? First, identify how factor risk
is managed in the strategy, then extend the approach to the debt
rating factor. For pair-based strategies, the obvious remedy is to
homogenize all admissible pair combinations with respect to debt
rating. That is, admit only those pair combinations of stocks in
which the two constituent stocks have sufﬁciently similar debt rating.
Then highly rated stocks will be paired with highly rated stocks,
low rated stocks with low rated stocks, thereby avoiding bets on
stocks that exhibited discordant price moves in response to concern
over the debt factor. Many other aspects of debt rating and related
issues would sensibly be investigated, too, including whether to
employ position weights decreasing with debt rating, restrict low
rated stocks to short positions, or an absolute veto on companies
with very poor debt ratings.
As the research is pursued, an important question to answer
is: What impact would have been seen on past performance of a
strategy from incorporation of new modeling restrictions? It is all
very well to congratulate oneself for ﬁnding the proximate cause
of performance problems, to determine and implement prophylactic
changes in one’s modeling, but one also needs to know what impact
on future performance (other than safeguarding when the factor is
active in a negative sense) is likely to ensue. More extensive discussion
of this subject in a broader context of performance disruption is
presented in Chapter 9.
8.4
REDEMPTION TENSION
The pattern of redemption of a broad-based, long-only fund is
perfectly ‘‘designed’’ to adversely impact a fast-turn, long–short
reversion play. Selling off a long-only fund generates asymmetric
pressure on stock prices—it is all one way, down. If the selling is
broad based, and to some extent persistent, then the impact on spread
positions can be only negative.
It is assumed that ‘‘broad based’’ means that a substantial portion
of the stocks traded in the reversion strategy is affected—assume half.
The long portfolio investment strategy, and hence current positions,
is assumed to be unrelated to the reversion strategy: Approximate
this by the assumption that the selling affects equally long and short
--- page 176 ---

Nobel Difﬁculties
149
positions of the reversion strategy. So, ‘‘all’’ affected longs reduce in
value under the selling pressure of the redemption activity, and ‘‘all’’
affected shorts reduce in liability. On average there should be no net
impact on the reversion strategy.
True . . . to begin with. But what has happened to the universe
of spreads in the reversion strategy? Those spreads in which both
the long and the short are affected by the downward price pressure
are essentially unchanged: Assume roughly proportional reductions
in price. (In practice, stocks that have been relatively strong will
be the initial focus of selling as the ﬁre sale lieutenant seeks to
maximize revenue—a one-sided, negative impact on a spread bet.
The resulting price change will be larger for weak stocks when they
are sold off, making the net result for a reversion-based book negative
rather than nil. For this discussion, we continue with the optimistic
assumption of zero net impact.) But for those spreads in which only
the long or the short is in a stock facing redemption selling, the
spread will change. Some will narrow, making money; some will
widen, losing money. Still net nothing. But those narrowing spreads
lead to bet exits—proﬁt taking. The widening spreads continue
to widen and lose more. Furthermore, continuing price reductions
cause the spread model to take on new positions, which then proceed
to lose money as the spreads continue to widen under continued
selling. If the selling continues long enough—and for a large holding
this is almost guaranteed—the natural trade cycle of the spread
strategy will complete itself and those new trades will exit, locking
in losses.
The picture can get even worse. When the selling is over, some
stocks recover with a similar trend—as if there is persistent buying
pressure. Who knows why that should be—reversion of relative
value! For those stocks, new spread positions are entered: Remember,
some previously entered positions ﬁnished on their natural dynamic
and so the model is sitting and waiting for new entry conditions.
Bingo, furnished as the stock price begins to reclaim lost ground. And
the losing spread bet (now in the opposite direction) is made again.
High-frequency reversion strategies make lots of bets on small
relative movements. Long-only fund redemptions cause price movements of a cumulatively much larger magnitude; the mechanics
described in this section create the conditions for a blood bath for
statistical arbitrage.
--- page 177 ---

150
STATISTICAL ARBITRAGE
8.4.1
Supercharged Destruction
A large equity statistical arbitrage portfolio is perfectly designed
to create, on liquidation, guaranteed losing conditions for other
statistical arbitrage portfolios. Size matters because the sell-off of
longs and the buy-in of shorts has to persist over the natural cycle of
other players. If it does not, then initial losses will be reversed before
existing trades are unwound; damage is limited largely to (possibly
stomach churning) P&L volatility. Destruction, when it occurs, is
supercharged because both sides of spread bets are simultaneously
adversely affected.
In November 1994 Kidder Peabody, on being acquired, reportedly eliminated a pair trading portfolio of over $1 billion. Long
Term Capital Management (LTCM), in addition to its advertized,
highly leveraged, interest instrument bets, reportedly had a large pair
trading portfolio that was liquidated (August 1998) as massive losses
elsewhere threatened (and eventually undermined) solvency.
8.5
THE STORY OF REGULATION FAIR
DISCLOSURE (FD)
Regulation ‘‘Fair Disclosure’’ was proposed by the SEC on December
20, 1999 and had almost immediate practical impact. That immediacy, ten months before the rule was ofﬁcially adopted, is stark
testament to some of the egregious behavior of Wall Street analysts
now infamous for such practices as promoting a stock to clients
while privately disparaging it, or changing a negative opinion to a
positive opinion to win underwriting business and then restoring the
negative opinion!
Activities eventually outlawed by Regulation FD had dramatic
negative impact on statistical arbitrage portfolios in 1999. Most
readily identiﬁable was the selective disclosure of earnings in the days
before ofﬁcial announcements. Typically, favored analysts would
receive a tip from a CEO or CFO. Analysts and favored clients
could then act on information before it became public. If the news
was good, a stock’s price would rise under buying pressure from
the in-crowd, statistical models would signal the relative strength
against matched stocks, and the stock would be shorted. Days later
when the news was made public, general enthusiasm would bid up
--- page 178 ---

Nobel Difﬁculties
151
the stock price further, generating losses on those short positions.
Long positions, signaled when the news was disappointing, suffered
similarly as prices declined, a lose–lose situation for short-term
statistical strategies.
This pattern of behavior became so rife that many market participants yelled vituperation; the SEC heard and acted. Notable effects
of the practice disappeared almost overnight.
Privileged information passed to analysts was not a new phenomenon in 1999. Widespread abuse of the privilege was new, or so it
seems from the events just outlined. If abuse existed previously, it was
not noticed. An interesting sidenote to the story is the effectiveness of
analysts. Many analysts with star reputations for making timely and
accurate forecasts of company performance became run-of-the-mill
forecasters after Regulation FD was announced.
8.6
CORRELATION DURING LOSS EPISODES
An investor lament heard when enduring portfolio losses:
‘‘Your results are [highly] correlated with those of other managers. . .’’ The implication here is that similar bets are being made,
contradicting claims of differentiation through different methods of
stock universe selection, trade identiﬁcation (forecast model), and
resulting trade characteristics such as holding period. Are the claims
of differentiation false? Is the performance correlation coincidental?
Two distinct, broadly based portfolios of stocks traded with a
reversion model are very likely to exhibit high coincidence of losing
periods. When normal market behavior (patterns of price movement
resulting from investor activities in normal times) is disrupted by an
event, international credit crisis and war are two recent examples,
there is a notable aggregate effect on stock prices: Recent trends of
relative strength and weakness are promoted. During event occasions
(and it is a near universal rule that ‘‘event’’ is synonymous with
‘‘bad’’ news), sell-off activity is always the result. Stocks perceived
as weak are sold off ﬁrst and to a greater extent than stocks that
are perceived as strong (or, at least, not weak). This is the reverse
of what is expected from a fund satisfying redemption notices—see
Section 8.4. The implication for spread trades is blindingly obvious:
losses. Regardless of the precise deﬁnition of a manager’s strategy,
--- page 179 ---

152
STATISTICAL ARBITRAGE
tradable universe, or speciﬁc collection of active bets at the time,
the common characteristic of all spread reversion bets, at a point in
time, is that stocks judged (relatively) weak are held long and stocks
judged (relatively) strong are held short. Mark to market losses
are inevitable.
The magnitude of losses, duration of losing streak, and time to
recovery will vary among managers, being strongly inﬂuenced by
individual reversion models and manager risk decisions.
Any economic, political, or other happening that causes investors
to become generally fearful instills a sell mentality. This has an
unambiguous effect on all broad-based portfolios of spread positions
on which mean reversion is being practiced. Unequivocally, performance turns negative; directional correlation of managers is high.
Interestingly, numerical correlation may not be high. The magnitude
of returns in negative performance periods can be quite different for
distinct portfolios. There is nothing in the rationale of fear-based
selling to suggest it should be ordered, evenly distributed across
market sectors or company capitalizations, or in any other way tidy.
Typically, a lot of untidiness should be expected. Hence, while managers should be expected to experience common periods of unusual
losses, the correlation of actual returns in losing periods examined
collectively and separately from returns in winning periods may be
positive, negative, or zero.
Losing periods are always followed by winning periods, by deﬁ-
nition. Extended intervals of market disruption punctuated by relief
must, on the arguments given, create similar patterns of losing and
winning intervals for spread reversion strategies.
And what can one say about relative performance of strategies
during generally positive periods for spread trading? Less correspondence of returns for distinct strategies is to be expected. Returns
are dependent on the precise dynamic moves exploited by individual
models. There is no unifying force creating short-, medium-, and
long-term dispersion followed by reversion that parallels the negative inﬂuence of fear. Exuberance is, perhaps, the closest to such
a force, creating reversionary opportunities randomly and at large.
But exuberance is less tangible than fear. It is less likely to induce
common decisions or actions. Investment results for collections of
managers will exhibit looser correspondence, greater heterogeneity
than in periods unfavorable to reversion.
--- page 180 ---

Nobel Difﬁculties
153
Fund A Return %
Fund B Return %
−1
0
1
2
−2
−1
0
1
2
FIGURE 8.3
Monthly returns for fund A and fund B, illustrating the fallacy of
correlation
Figure 8.3 illustrates the typical situation. Overall, fund A and
fund B show positively correlated returns, with a modest correlation
of 0.4. This correlation result is driven by the two quadrants where
both funds are winners or both are losers (positive–positive and
negative–negative) in which most trading outcomes lie. Within those
two quadrants, the good and the bad strategy periods, correlation
is negative: −0.19 in the bad times and −0.22 in the good times.
This seeming contradiction, positive overall correlation but negative
correlation in all dominant subperiods, is an example of the fallacy
of correlation. Notice that the strength of the relationship between
returns in the negative quadrant is actually lower, at 0.19, than
in the positive quadrant (0.22), which is contrary to the general
expectation described earlier. This example serves to illustrate a
common theme described several times in the text, that while we
can identify and characterize patterns—general or average—there is
always variability to appreciate and contend with. Notice, too, that
there are only ten data points in the negative quadrant, barely one
--- page 181 ---

154
STATISTICAL ARBITRAGE
quarter of that number in the positive quadrant. Thus, the correlation
is less well estimated (there are fewer degrees of freedom, or pieces
of information, in statistical parlance). And ten is a small number for
estimating a variable relationship—isn’t it?
It is not surprising that losing periods are experienced in common
by different spread reversion strategies. The visibility of such correlation following two extraordinary years of market disruption is
understandable. Understanding why the result is obtained is important: Attention is more likely to be rewarded if focus is shifted from
contemplating the unexceptional coincidence of negative returns to
examining where losses have best been contained. Attention should
also be focused on the prospects for a resurgence of the drivers of
spread reversion—on when and whether those drivers will reemerge
strongly enough to create systematically proﬁtable opportunities
for managers (see Chapter 11). Here, there is real possibility of
distinguishing future likely winners and losers.
--- page 182 ---

CHAPTER9
Trinity Troubles
Extinction occurs because selection promotes what is
immediately useful even if the change may be fatal in the
long run.
—T. Dobzhansky. 1958. ‘‘Evolution at Work.’’
Science 1,091–1,098
9.1
INTRODUCTION
B
eginning in early 2000, after nearly two decades of outstanding
proﬁtability, the returns of many statistical arbitrage managers
collapsed to zero or worse. Some managers continued to generate
excellent returns for two more years but they, too, ceased to perform starting in early 2002. The split into failures and successes
in 2000 is an interesting historical point in the story of statistical
arbitrage, demarcating a state change in high frequency reversion
dynamics. Of greater signiﬁcance because of its universal effect, the
performance watershed in 2002 was considered by many to mark
the death of statistical arbitrage as an absolute return generator,
though there remained a few observers who discerned temporary
structural problems and posited conditions under which statistical
arbitrage would rise again. Coherent analysis was not abundant,
investor patience was rarer even than that, and the latter became the
real death knell as it led to investment withdrawal, leaving managers
unable to meet payroll.
At the end of 2005 that was the dire state of statistical arbitrage;
as an investment discipline it had become an unsaleable product.
The year 2006 saw a resurgence in performance, vindicating those
who had maintained that the performance collapse was explained
155
--- page 183 ---

156
STATISTICAL ARBITRAGE
by a multiplicity of factors, many of which were transitory. With
the passing of those temporary disruptions to market coherence and
consistently predictable security price dynamics, the likely possibility
of a new productive period for statistical arbitrage was anticipated.
We are now nearly two years into just that renewal.
In this chapter, we begin by examining several one-liners loudly
touted as the cause of statistical arbitrage return decline. While each
may have had some negative impact, it is unlikely that the combined
effect has been more than 30 percent of historical return. A signiﬁcant
reduction, but not a cofﬁn maker for the strategy. Next we expand
the perspective to consider major developments in the U.S. economy
and ﬁnancial markets, describing the degree to which the impact on
statistical arbitrage is transient. One perspective on 2003 is offered
to set the context of the discussion.
Chapter 10 continues the theme of searching for reasons for
performance decline and sources of a revival. The focus is on technical developments by large brokerage houses. Long-term impact on
statistical arbitrage is certain, negative for many extant strategies but
creating new opportunities with increasing use of the tools by large
market participants (Chapter 11).
9.2
DECIMALIZATION
‘‘The bid–ask spread reduced from a quarter to two cents has
eliminated the statistical arbitrage edge.’’
Strategies may go by the same generic name, statistical arbitrage,
but there are important distinctions that are critical to understanding performance disparities over the last few years as well
as prospects for future performance. Starting in mid-2000, practitioners of high-frequency statistical arbitrage generally achieved
a poor return, in many cases actually negative for much of 2000
and 2001. The declining bid–ask spread, from prices quoted in
eighths to sixteenths to pennies, had an enormous negative impact
on those returns. Furthermore, consolidation of ﬂoor specialists into
the now ﬁve majors plus two small independents resulted in much
of the intraday and day-to-day price reversion being internalized by
those specialists. With research budgets, computers, and manpower
resources exceeding most statistical arbitrage fund managers, and the
--- page 184 ---

Trinity Troubles
157
unfair advantage of order ﬂow visibility, it should not be a surprise
that this has happened (see Chapter 10).
The statistical arbitrage edge was not eliminated. But the highfrequency opportunity was speedily removed from the public domain
and monopolized by a favored few. Strategies with a holding period
extending over weeks or months rather than days were largely unaffected by the change to decimalization. This dynamic characteristic
of models was signiﬁcant in explaining the performance split over
2000–2002 described in the opening section of the chapter. To
those exploiting a reversion process fundamentally different from the
high-frequency strategies, the contribution to proﬁt of longer term
bets from bid–ask spreads was fractional. There may have been some
performance deterioration from poorer execution, but not outright
elimination. To see this, let’s take a look at some examples.
Consider an average stock priced at $40 per share. Suppose that
the goal of a strategy is to earn 12 percent per annum, or 1 percent a
month on average. With a holding period of two months, a reversion
bet is expected, on average, to yield 2 percent, or 80 cents. The loss
of the long-time standard bid–ask spread of a quarter, now reduced
to a couple of cents following decimalization, can at most have
eliminated one-third of the expected gain on a bet. Annual return is,
therefore, reduced from 12 percent to 8 percent. This is a worst-case
analysis that ignores the ameliorating possibilities available from
trade timing tactics when trades can be made over several days—an
option not available to higher frequency strategies. The actual impact
of decimalization on the longer term strategy is more marginal.
The story doesn’t end with decimalization, of course, as subsequent sections of this chapter show. Surviving the switch to
decimalization, showing longer term statistical arbitrage strategies
to splendid advantage in 2000 and 2001, did not help counter other
structural changes that cumulated over 2002 and 2003.
9.2.1
European Experience
The European markets have been decimalized for decades yet
high-frequency statistical arbitrage has developed successfully over
the same time. The conclusion must be that decimalization itself
is not a barrier to proﬁt opportunity for the strategy; performance
problems are created by changes in market structure which causes
--- page 185 ---

158
STATISTICAL ARBITRAGE
changes in temporal dynamics, disrupting the patterns that statistical
arbitrageurs’ models are built to predict. European markets are fully
electronic, closer to the NASDAQ than the NYSE in that respect.
Yet statistical arbitrage in all those markets failed to generate a
return in 2003–2004. While it is possible that different causal factors
explain the lack of performance in each of the ‘‘three markets,’’ it
is more likely that a common factor was active. What candidates
might be implicated? The early part of 2003 was dominated by the
Iraq war. But what of the ﬁnal six months? And 2004? Economic
news gradually shifted from the uniformly gloomy and pessimistic
to generally optimistic, though the negative baggage of U.S. budget
and trade deﬁcits caused much consternation (on the part of commentators and professional economists). It is this change, and the
commensurate changes in investor behavior, that caused the nonperformance of statistical arbitrage across markets and managers. In
each of the markets, other market speciﬁc factors undoubtedly were
also present.
9.2.2
Advocating the Devil
Having just argued that decimalization was not a signiﬁcant factor
in the reduction of return in statistical arbitrage, except for some
high-frequency strategies, let’s consider how the change could have
been detrimental.
There is a lot of anecdotal evidence that liquidity within the day
has changed directly as a result of decimalization: How do these
changes relate to the day-to-day price behavior and trading volume
for statistical arbitrage? Prima facie evidence, the decline of strategy
return, is that market price patterns changed. How? In what ways?
Can a logical connection be made between the observed changes,
decimalization, and statistical arbitrage performance? Without considering the purported changed mechanics of intraday pricing, let us
suppose the claim of change to be correct. What are the implications
for daily price behavior?
Can a process be elucidated under which continuous trading
from 9:30 a.m. through 4 p.m. will, ceteris paribus, generate daily
price patterns structurally, notably, describably different depending
on the size of the individual market price increment? If not, then
systematic trading models evaluated on daily closing prices will also
--- page 186 ---

Trinity Troubles
159
not exhibit distinguishable outcomes except to the extent that the
bid–ask spread (at the close) is somehow captured by a strategy.
In fact, simulations of many such models exhibited poor returns
over 2003–2004. Either the observable, acknowledged, structural
changes to price moves within the day resulting from the change to
decimal quotes and penny increments led to change in the structure
of end-of-day prices across time, or some factor or factors other than
the change to decimalization explain the simulation outcome.
If a contrary observation had been made, then a plausible argument from decimalization to systematic trading strategy return could
be constructed: If day-to-day trading shows positive return but intraday trading shows no return then price moves in reaction to trades
eliminate the opportunity. The evidence to date neither supports
nor contradicts such a hypothesis. It is much more likely than not
that decimalization was a bit player in the explanation of statistical
arbitrage performance decline.
Suppose that statistical arbitrage’s historical performance was
derived solely from systematic obtaining of the consumer surplus
when spreads jump over a trade threshold and ﬁlls are obtained at
or better than even that ‘‘excess.’’ If decimalization reduces, almost
to nil, the jump and, we might reasonably suppose (supported by
experience), price improvement, too, then the expected return of bets
similarly reduces to almost nil. This scenario is seductive until one
realizes that it is little more than an elaboration of the bid–ask spread
argument. The consumer surplus of the jump plus price improvement
is quite simply the bid–ask spread (jump) plus price improvement.
Unless price improvement was a major component of strategy return,
this argument is reduced to dust.
9.3
STAT. ARB. ARBED AWAY
‘‘Stat. arb. has not generated a return in two years. It’s edge has been
‘arbed’ away.’’
This was heard with growing clamor as 2004 rolled on. But what
kind of evidence is there for the dismissal? With nothing further than
the observation of recent history offered to support the claim, we
must suppose that the performance evidence was deemed sufﬁcient
proof. As such, the argument is refuted simply by looking a little
--- page 187 ---

160
STATISTICAL ARBITRAGE
further back. Over the 18 months from mid-1998 through the end
of 1999, the strategy yielded almost nil return (factor-based models
fared better than others), yet the subsequent two years yielded record
rates of return.
An extended period of ﬂat performance does not prove that
patterns of stock price behavior, the source of return from systematic
exploitation, have ceased to exist. Equally, there is no reason to
suppose, solely by examining the numbers, that unusually large
returns, or any particular pattern of returns, will be obtained as soon
as a dry spell ends or, indeed, that there will be an end thereto. To
understand what is possible, one needs to understand the nature of
the stock price movements, the inefﬁciency that is exploited by the
strategy, and how exploitation is achieved. To go further and posit
what is likely requires one to make statements about various states
of the world and to make forecasts (Chapter 11). Now, of course,
the claim can also be refuted by looking forward from when it was
made to today. Literally, there have been many happy statistical
arbitrage returns.
9.4
COMPETITION
‘‘Competition has eliminated the stat. arb. game.’’
It is tempting to dismiss this claim in an equally disdainful manner as in which it is presented. Leaving aside the implicit belittling
of statistical arbitrage as a ‘‘game,’’ those who practice it as such
are playing roulette. Winning streaks are possible but when things
go wrong the gamesters have no substance to fall back on. Rash
action, desperation, and inglorious exit from the industry follow.
For those who understand the drivers of their strategy and the subtleties of its implementation, shocks are survived through discipline
and control.
Did competition eliminate risk arbitrage as an investment strategy? Quite! The dearth of opportunity during 2002–2005 was not
because of a greater number of practitioners or increasing assets
managed in the strategy, both of which preceded the return decline,
but because of the structural change in the economy. As 2005 drew
to a close, anticipation was already building that merger activity
would increase, resuscitating the merger arbitrage business, with
just a few months of consistently positive economic news. Increased
--- page 188 ---

Trinity Troubles
161
participation in the business will have an impact on return as activity
increases. The gains will be smaller on average; better, more experienced managers will do well if they discover and exploit the new
patterns described in Chapter 11; neophytes, relying on traditional
ideas, will have a more difﬁcult time. Luck will play no small role.
What is the difference between merger and statistical arbitrage such that massive structural change in the economy—caused
by reactions to terrorist attacks, wars, and a series of corporate
misdeeds—was accepted as temporarily interrupting the business of
one but terminating it (a judgment now known to be wrong) for the
other? Immensely important is an understanding of the source of the
return generated by the business and the conditions under which that
source pertains. The magic words ‘‘deal ﬂow’’ echo in investor heads
the moment merger arbitrage is mentioned. A visceral understanding provides a comfortable intellectual hook: When the economy
improves (undeﬁned—another internalized ‘‘understanding’’) there
will be a resurgence in management interest in risk taking. Mergers
and acquisitions will happen. The game will resume after an interlude. There is no convenient label for the driver of opportunities in
statistical arbitrage (although some grasp at ‘‘volatility’’ in the hope
of an easy anchor—and partially it may be). There is no visceral
understanding of or belief in how statistical arbitrage works; nothing to relate to observable macroeconomic developments; no simple
indicator to watch. Beyond the visceral one has to think deeply. That
is difﬁcult and, hence, there is much uncertainty, confusion, and
an unavoidable scramble to the conservative ‘‘Statistical arbitrage is
dead.’’ How is the Resurrection viewed, I wonder?
The competition argument deserves serious attention. Though
there are no publicly available ﬁgures recording the amount of capital
devoted by hedge funds and proprietary trading desks of investment
banks to systematic equity trading strategies, it can be deduced
from the remarks of clearing brokers; investors; listings in Barron’s,
Altvest, and so forth that both the number of funds and the amount
of money devoted to the discipline increased greatly before 2000.
An immediate counter to this observation as evidence supporting
the competition hypothesis is that the increase in assets and number
of managers has been taking place for two decades yet only with
performance drought is a link to asset-class performance being made.
Statistical arbitrage performance did not decline in tandem with a
--- page 189 ---

162
STATISTICAL ARBITRAGE
view of how assets/managers increased. The hypothesis was offered
only to explain the cessation of performance for two years; an abrupt
halt to a preceding excellent history. The hypothesis requires, to
overcome the ‘‘convenient but not adequately matched to evidence’’
tag, an explanation of why the competition effect only recently, and
dramatically, became apparent.
With the market in steep decline from 2000–2002, investors previously shy of hedge funds, including statistical arbitrage, increased
allocations to alternative investment disciplines. Therefore, it may
be argued that there was a step change (increase) in investment in
statistical arbitrage in 2002.
But . . . it did not all happen at the beginning of 2002, did it?
What other evidence, besides assets invested in and number
of practicing managers, can be sought to support or discredit the
competition hypothesis? The superﬁcial argument considered thus
far, increased attention correlated with poor performance, is barely
an argument at all; it is really only a coincidence of observations
with correlation taken for causality and no explanation of how a
causal mechanism might be expected to work. The simplest scenario
is ‘‘many managers were competing to trade the same stocks at the
same prices.’’ Even an approximation to this would be revealed to
participants through liquidity problems—unﬁlled trades, increased
slippage on ﬁlled trades, for example. Evidence to support such an
explanation has not been widely claimed.
If competition during trading eliminates the ‘‘consumer surplus’’ and price improvement (historically part of statistical arbitrage
return) then once again the effect should be visible in end-of-day
closing prices. The fact that many bets continue to be identiﬁed with
a substantial consumer surplus component belies the argument. The
reduction in number of opportunities is directly related to volatility,
which may very well be reduced in some part by greater competition
among a larger number of statistical arbitrage managers. That still
leaves the important question: Why is the sum total of return on the
identiﬁed opportunities reduced to zero?
Let us accept that competition in systematic trading of equities
has increased. There is no evidence, notwithstanding performance
problems, to support concomitant increase of market impact, and
consequently no evidence that greater competition is the major cause
of the decline of statistical arbitrage performance.
--- page 190 ---

Trinity Troubles
163
9.5
INSTITUTIONAL INVESTORS
‘‘Pension funds and mutual funds have become more efﬁcient in their
trading.’’
Three years of market decline pushed many institutional investors
to enormous effort to reduce costs and, hence, losses as return generation eluded most; transaction costs were prime targets. The argument
is that reversion opportunities historically set up by the large block
trades disappeared as traders of those blocks became smarter with
their trading.
‘‘Fidelity has been a ‘VWAP∗shop’ for several years’’
is frequently heard as shorthand for the argument. Once again, we
must note that these changes did not happen overnight. To the
extent that such changes have been a factor in statistical arbitrage
performance decline, it is confounded with other changes. Assessing the impact appears to be an insurmountable practical problem.
Certainly, institutional investors are major users of the trading tools
described in Chapter 10 and a substantial impact—negative for
statistical arbitrage—is undoubted.
9.6
VOLATILITY IS THE KEY
‘‘Market volatility ticked up—isn’t that supposed to be good for stat.
arb.?’’
From the beginning of 2002, people began searching for explanations for the lack of return from statistical arbitrage strategies. Many
managers had experienced a meager year in 2001 though many others had a good year. But shortly into 2002 managers everywhere
(almost) were experiencing poor performance. The decline in market
volatility was dragooned into service as ‘‘the’’ explanation for the
lack of statistical arbitrage performance. Impressively quickly the
volatility explanation became Antilochus’ hedgehog, a single ‘‘big’’
idea. Combined with investor pleading for silver bullet solutions to
the performance drought, observers might be forgiven for wondering
if they had entered a ﬁlm set! This chapter and the sequel stand as
explanation in the mode of Antilochus’ fox: many ‘‘small’’ ideas.
∗Volume Weighted Average Price.
--- page 191 ---

164
STATISTICAL ARBITRAGE
199503
0.05
0.10
0.15
199703
199903
200103
200303
FIGURE 9.1
S&P 500 within industry average local pairwise volatility
Spread bets exploit relative price movement between stocks. It is
interstock volatility that is critical for performance; and interstock
volatility, while constrained by market volatility, is not a simple
function of it (see Chapter 6). Often interstock volatility moves in
the contrary direction to market volatility. In the third quarter of
2003, interstock volatility declined to a record low, even as market
volatility increased. The decline continued through 2004.
Just as interstock volatility is not simply related to market volatility, so the level of interstock volatility is also not simply related to
strategy proﬁtability. Only a small proportion of the total volatility
is systematically exploited by spread models; large changes in the
level of interstock volatility are observed to have only a small impact
on the magnitude of strategy return (except when volatility decreases
to extremely low levels as seen in 2004 and except for more sophisticated models which capture more of the raw volatility) a larger
impact is observed on the variability of the return. Both relationships are well demonstrated by the contrasting market conditions
and strategy performance in the ﬁrst and third quarters of 2003. The
