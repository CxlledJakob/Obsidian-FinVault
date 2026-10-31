# The Kelly capital growth investment criterion _ theory and -- Leonard C_ Maclean, Edward O_ Thorp, W_ T_ Ziemba, Leonard -- World Scientific Handbook -- isbn13 9781283148344 -- bec576e26410d0c695fd5b867d08ec4f -- An.pdf — pages 685–704

--- page 685 ---

This page is intentionally left blank
--- page 686 ---

45
Introduction to the Evidence of the Use of Kelly Type
Strategies by the Great Investors and Others
657
We know that in the long run, full Kelly strategies dominate other strategies, but
they are very risky short term. Hence, practical applications to long sequences of
wagers are especially appropriate. Current hedge fund trading that enters and exits
in a few seconds is such an application. Thorp (1960) coined the term Fortunes's
Formula in his application of Kelly to the game of blackjack using his card counting
system. The count provides an estimate of the mean so that with more favorable
counts the player should wager more. Typically, blackjack players can play about
60+ hands per hour. So this application works well for full Kelly. But the risk
is high that even after a few hours, with say a 1% edge, a player may be behind.
Hence, blackjack teams typically use fractional Kelly strategies, with fractions of
0.2 to 0.8 being common. Gottlieb (1984, 1985) describes the early use of these
fractional Kelly strategies.
It is no coincidence that many of the greatest hedge fund and portfolio managers are former blackjack players. Billionaires like trend follower Harold McPike,
bond guru Bill Gross, options trader Blair Hull, and racetrack guru Bill Benter are
some examples. Other top investors like Renaissance Medallion hedge fund trader
Jim Simons and Warren Buffett, the legendary greatest investor in the world, use
strategies that employ Kelly-type ideas to attain long term wealth growth. So did
the great economist John Maynard Keynes in managing the King's College Cambridge endowment. As we have seen the size of Kelly wagers is largely dependent
upon the probability of losing and it is important not to overbet. Since, the effect
of errors in means are risk aversion dependent, these wagers for Kelly bettors are
very sensitive to good mean estimates. Otherwise, it is easy to overbet.
The book Fortune's Formula written by William Poundstone (2005) brought
the Kelly ideas to a wider audience. So now many investment newsletters such
as Morningstar and The Motley Fool suggest Kelly strategies (see Fuller (2006)
and Lee, 2006). Unfortunately, most of these sources do not fully understand the
computation of Kelly strategies in the multivariate case and when there are portfolio
management imperfections (such as slippage). As well, they often miss the subtleties
and danger of these Kelly applications. In this final part of the book, we present
applications of Kelly and fractional Kelly modeling.
Hausch, Ziemba, and Rubinstein (HRZ) (1981) present a weak market efficiency
anomaly in the horserace place and show markets and how it can be exploited and
wagered on using the Kelly criterion. The idea is to use probabilities derived in a
--- page 687 ---

658
L. C. MacLean, E. 0. Thorp and W T. Ziemba
simple market (the win pool involving n horses) in a market that is more complex
-
the place pool involving n( n - 1) combinations and/or the show pool involving
n(n - 1)(n - 2) combinations, Previous studies (see Hausch and Ziemba, 2008,
for an up to date survey of results), indicate that the win market at racetracks is
efficient except for a favorite-Iongshot bias, Favorites are underbet and longshots
are overbet, This bias has been apparent for well over 50 years, although recent
changes in the betting to allow rebates for large bettors and head to head wagering
on a betting exchange have changed this shape to some extent; see graphs in Hausch
and Ziemba (2008). This biases for win is in the opposite direction of the bias for
place and show where favorites are overbet and longshots underbet so in the HZR
analysis that was the probability of finishing one-two for place or one-two-three for
show, the biases tend to cancel. So HZR assume that the probability that horse i
wins is simply its betting fraction Wi/W, and the probability that i is first and j is
second is the chance that i wins and j wins a race that does not contain i, namely
(WdW ) {
W j / W
}
1-Wd W
where Wi are the wagers to win on horse i and W = 2:: Wi. While its known that
these Harville formulas are biased, the bias cancels in the HZR application, again
see Hausch and Ziemba (2008) for current research on this bias. HZR compute the
expected value of place and show bets and note that there frequently are favorable
bets with expected values well above l.0 per dollar bet. Applying the Kelly criterion
leads to a complex non-concave non-linear programming model to compute optimal
wagers that include the transactions costs or slippage that comes from the effect of
our investor's bets on the odds. They show that the system yields positive profits
at several racetracks. To make the system operational, they solved thousands of
Kelly models and regressed the optimal bets and expected values on the ratio of
the place and show pool bet on horse i. Then at the track, one only needs to look
at Wi and W and Pi and P or Si and S, where Pi are the wagers to place on horse
i and Si are the wagers to show on horse i. A quick scan can indicate whether a
bet is good or not.
Hausch and Ziemba (1985) added further refinements to the basic system. These
included equations for the optimal place and show bets for varying initial wealth and
place or show betting pool size. These were subsequently used in a calculator that
allows players to punch in the four parameters from above and compute quickly
the expected value and Kelly bet. This includes the track take adjustment, and
coupled entry adjustments if needed that Hausch and Ziemba worked out. They
also looked into the effects of the track take and breakage (the rounding to 2.20 or
2.10 for example from 2.25 and 2.18 payoffs to the nearest dime per $2 or $1 bet ,
respectively. Finally, they computed how many players can be using the system at
the same time before the market will become efficient. Ziemba and Hausch (1984,
1986, 1987) wrote two books that made the system popular and famous. Now
twenty-five years late, the system is still in use although the conditions are rougher
--- page 688 ---

Introduction to the Evidence of the Use of Kelly Type Strategies
659
in 2010 than in the 1980s because of the two factors mentioned above (rebates and
betting exchanges) and the fact that there is so much cross track betting these days
that about half the betting pool has not arrived when the horses begin running.
But the clever punter can estimate this odds movement that occurs after the bets
have to be made.
Ziemba and Hausch (1994, 2008) show how to modify the place and show system
developed in the HZR and HZ papers to a different betting system that is used
in some other countries such as England. In the UK, there is no show betting,
only place, but the number of horses that place is not necessarily two as in North
America. Rather, it depends on the number of horses running in the race. There
can be one, two, three or four horses that place when the number of horses running
is at most four, 5- 7, 8- 15 or 16+, respectively. In the UK there are bookies offering
fixed odds and the parimutuel tote as discussed here. In North America place
and show bets pay back the stakes of the horses that place or show and then the
net profit is divided equally among these two or three qualifiers. The the payoffs
depend on the number of winning tickets on each qualifier. But in the UK, the
entire pool, after the take, is divided into 1, 2, 3 or 4 equal portions which is then
split into the individual payoffs. So you can see that with a large amount bet on
one horse, the payoffs for a £1 bet can be as low as £1. With this minimum payoff
there are arbitrages possible, see Hausch and Ziemba (1990) for the US and Jackson
and Waldron (2003) for the UK and other locales. Ziemba and Hausch develop the
expected value equation and Kelly criterion bet sizing. These equations yield simple
graphs to apply the system in the UK.
In all of these applications, the theory indictes that the calculations should be
based, as Thorp has argued, on total liquid wealth not just the track wealth. Wilcox
(2003ab, 2005) has argued for a related theory where decisions are made on excess
wealth after liabilities are deducted. This is a fractional Kelly strategy.
Grauer and Hakansson (1986) and in a number of other papers apply the Kelly
modeling approach to asset-allocation problems. They use a simple asset return
distribution procedure: it is assumed that the past will repeat itself. At the beginning of each period t, the investor chooses a portfolio on the basis of a utility
function for gross returns, R, given by
~ { R r, for
"y::;; 1.
"y
The data used are the total monthly and yearly returns including interest and
dividends on stocks, long-term government bonds, long-term corporate bonds and
small capitalized stocks for 1926- 1983 in the Ibbotson and Sinquefield CRSP file.
They compute results for the no-leverage and leveraged cases with and without small
capitalized stocks for "y = 1 (positive power), 3/4, 1/2, 1/4 and 0 (full Kelly) and
negative powers - 1, -2, ... , -75. They did quarterly and yearly revisions. The
simple historical probability approach gives good results. Small stocks generally
add value.
--- page 689 ---

660
L. C. MacLean, E. 0. Thorp and W T. Ziemba
Mulvey, Bilgili and Vural (2010) apply Kelly type models to deal with various practical issues involving imperfections such as transaction costs, operational
constraints and path dependencies, etc for use by investors such as defined benefit pension plans, Their model is modified to also provide downside protection
in turbulent markets, They apply the theory to recent US stock market behavior
including the 2008 crash period, They show how large endowments can modify
their typical three step process: select benchmarks, revise portfolio allocation targets and select active managers to deal with these issues. Fixed mix portfolio
rates along with exchange traded ETFs provide volatility induced wealth growth.
They show that gains are larger in upswings and losses lower in crash periods
than the underlying indices. The increasing correlation of equity assets during
crash periods is dealt with by developing a portfolio of low correlation investment
strategies.
Rudolf and Ziemba (2004) present a continuous time model for pension or insurance company surplus management over time. Such lifetime intertemporal portfolio
investment models date to Ramsey (1928), Phelps (1962) and Samuelson (1969) in
discrete time and Merton (1969) in continuous time. Rudolf and Ziemba use an
extension of the Merton (1973, 1990) model that maximizes the intertemporal expected utility of the surplus of assets net of liabilities using liabilities as a new variable. They assume that both the asset and the liability return follow Ito processes
as functions of a risky state variable. The optimum occurs for investors holding four
funds: the market portfolio, the hedge portfolio for the state variable, the hedge
portfolio for the liabilities, and the riskless asset. This is a four fund CAPM, while
Merton has a three fund CAPM, and the ordinary Sharpe-Lintner-Mossin CAPM
has two funds. The hedge portfolio provides maximum correlation to the state variable, that is, it provides the best possible hedge against the variance of the state
variable. In contrast to Merton's result in the assets only case, the liability hedge
is independent of preferences and depends only on the funding ratio. With hyperbolic risk aversion utility, which includes negative exponential, power and log, the
investments in the state variable hedge portfolio are also preference independent,
and with Kelly type log utility, the market portfolio investment depends only on
the current funding ratio.
Having surplus over time is what life and other insurance companies, pension
funds and other organizations try to achieve. With both life insurance companies
and pension funds, parts of the surplus are distributed to the clients usually once
every year. Hence, optimizing their investment strategy is well represented by
maximizing the expected lifetime utility of the surplus.
A case study involves a US based investor investing in the stock and bond
markets of the US, UK, Japan, the EMU, Canada and Switzerland. The investor
faces an exposure to five foreign currencies euro, British pound, Japanese yen,
Canadian dollar and Swiss franc, and can invest in eight funds. Five of them are
hedge portfolios for the state variables, which are assumed to be currency returns
--- page 690 ---

Introduction to the Evidence of the Use of Kelly Type Strategies
661
and the others by portfolio separation are the market portfolios, the riskless asset
and the liability hedge portfolio.
The holdings of the various funds depend only on the funding ratio and on
the currency betas of the distinct markets. For a funding ratio of one, there is no
investment in the market portfolio and only diminishing investments in the currency
hedge portfolios. The portfolio betas against the five currencies are close to zero for
all funding ratios. The higher the funding ratio is, the higher is the investment in the
market portfolio, the lower are the investments in the liability and the state variable
hedge portfolios, and the lower is the investment in the riskless fund. Negative
currency hedge portfolios imply an increase of the currency exposure instead of a
hedge against it. The increase of the market portfolio holdings and the reduction
of the hedge portfolio holdings and the riskless fund for increasing funding ratios
shows that the funding ratio is directly related to the ability to bear risk. Rather
than risk aversion coefficients, the funding ratio provides an objective measure to
quantify attitudes towards risk.
Ziemba (2005) investigates the records of great investors and proposes a simple
modification of the ordinary Sharpe ratio to evaluate them more fairly. In most
cases these investors have mostly monthly or quarterly gains with few losses so the
ordinary Sharpe ratio penalizes them for gains by increasing the portfolio standard
deviation. The funds discussed are Windsor of George Neff, the Ford Foundation,
the Harvard Endowment, Tiger of Julian Robertson, Quantum of George Soros
and Berkshire Hathaway of Warren Buffett. The modified Sharpe ratio simply
replaces the gains by the mirror image of the losses. So gains are not penalized but
only losses.
With the ordinary Sharpe ratio the Ford Foundation beats Berkshire Hathaway
even though the geometric mean return is much less. So the question is does Berkshire dominate with the modified DSSR downside symmetric Sharpe ratio. Only
Berkshire improves with the DSSR but the Ford Foundation and the Harvard endowment are still slightly better. This is because Berkshire has the most large
gains of all the funds studied but also has a lot of large losses on a monthly or quarterly basis and more than the other funds. So Berkshire is oriented towards a full
Kelly long term valuation where intermediate monthly, quarterly and even yearly
returns are not the goal, rather long terms growth is the goal. So we believe Buffett
acts like a full Kelly bettor in his investment strategies. These funds have DSSRs
about 1.0.
Princeton-Newport, run by Edward O. Thorp, a co-editor of this book, had
a DSSR of 13.8 with a very smooth wealth path with only three monthly losses,
and no quarterly or yearly losses, over the twenty year period 1969-1988. Thorp
had similar good results in other funds run later. Renaissance Medallion, run by
James Simon, arguably the current top hedge fund in the world, had, as reported
by Ziemba and Ziemba (2007), an even higher 26.4 DSSR with very few monthly
or quarterly losses. no yearly losses, and very high mean returns during the period
January 1993 to April 2005.
--- page 691 ---

662
L. C. MacLean, E. 0. Thorp and W T. Ziemba
Thorp (2006) presents a comprehensive survey of his considerable use over almost
fifty years of Kelly strategies in blackjack, sports betting and the stock market
along with theoretical results he has found useful in practice. He traces the early
first serious application of Kelly methods to blackjack bet sizing, to various sports
betting applications and his great success as a hedge fund trader with the Princeton-
Newport and later hedge funds.
--- page 692 ---

Management Science, 27, 1435- 1452 (1985)
46
EFFICIENCY OF THE MARKET FOR RACETRACK
BETTING*
DONALD B. HAUSCH, t WILLIAM T. ZIEMBAt AND MARK RUBINSTEIN§
Many racetrack bettors have systems. Since the track is a market similar in many ways to
the stock market one would expect that the basic strategies would be either fundamental or
technical in nature. Fundamental strategies utilize past data available from radng forms,
spedal sources, etc. to "handicap" races. The investor then wagers on one or more horses
whose probability of winning exceeds that determined by the odds by an amount sufficient to
overcome the track take. Technical systems require less information and only utilize current
betting data. They attempt to find inefficiencies in the "market" and bet on such "overlays"
when they have positive expected value. Previous studies and our data confirm that for win
bets these inefficiencies, which exist for underbet favorites and overbet longshots, are not
sufficiently great to result in positive profits. This paper describes a technical system for place
and show betting for which it appears to be possible to make substantial positive profits and
thus to demonstrate market inefficiency in a weak form sense. Estimated theoretical probabilities of all possible finishes are compared with the actual amounts bet to determine profitable
betting situations. Since the amount bet influences the odds and theory suggests that to
maximize long run growth a logarithmic utility function is appropriate the resulting model is a
nonlinear program. Side calculations generally reduce the number of possible bets in anyone
race to three or less hence the actual optimization is quite simple. The system was tested on
data from Santa Anita and E)(hibition Park using ellact and approximate solutions (that make
the system operational at tl:e track given the limited time available for placing bets) and found
to produce substantial positive profits. A model is developed to demonstrate that the profits
are not due to chance but rather to proper identification of market inefficiencies.
(FINANCE-PORTFOLIO; GAMES- GAMBLING)
1. The Racetrack Market
663
For the most part,l academic research on security markets has bypassed an
interesting and accessible market-the racetrack for thoroughbred horses-with its
highly standardized form of security-the tote ticket. The racetrack shares many of the
characteristics of the arch typical securities market in listed common stocks. Moreover
the racetrack gains further interest from its significant differences, and more importantly, because it is inherently a more elementary market context, lacking many of the
dynamic features which complicate analysis of the stock market.
The "market" at the track in North America convenes for about 20 minutes, during
which participants place bets on any number of the six to twelve horses in the
following race. In a typical race, participants can bet on each horse, either to win,
place or show.2 The horses that finish the race first, second or third are said to finish
• Accepted by Vijay S. Bawa, former Departmental Editor; received April 3, 1980. This paper has been
with the authors 2 months for I revision.
tNorthwestern University.
tUniversity of British Columbia.
I University of California, Berkeley.
I For surveys, see Copeland and Weston [6], Fama [9J, [10] and Rubinstein [22J.
20ther bets such as the daily double (pick the winners in the first and second race), the quinella (pick the
first two finishers regardless of order in a given race) and the e)(acta (pick the first two finishers in e)(act
order in a given race) as well as various combinations are possible as well. Such bets are utilized by the
public to construct low probability high payoff bets. For discussion of some of the implications of such bets
see Rosett (21].
Efficiency of Racelrack Belting MarkelS
373
--- page 693 ---

664
D. B. Hausch, W T Ziemba and M Rubinstein
374
D. B. HAUSCH, W. T. ZIEMBA AND M. R. RUBINSTEIN
"in-the-money." All participants who have bet a horse to win, realize a positive return
on that bet only if the horse is first, while a place bet realizes a positive return if the
horse is first or second, and a show bet realizes a positive return if the horse is first,
second OT third. Regardless of the outcome, all bets have limited liability. Unlike most
casino games such as roulette, but like the stock market, security prices (i.e. the
"odds") are jointly determined by all the participants and a rule governing transaction
costs (i.e. the track "take"). To take the simplest case, for win, all bets across all horses
to win are aggregated to form the win pool. If Wi represents the total amount bet by all
participants on horse i to win, then W = L:i W; is the win pool and WQ/ W; is the
payoff per dollar bet on horse I to win if and only if horse i wins, where 1 - Q is the
percentage transaction costs.3 If horse i does not win, the payoff per dollar bet is zero.
The track is "competitive" in the sense that every dollar bet on horse i to win,
regardless of the identification of the bettor, has the same payoff. The "state contingent" price of a dollar received if and only if horse i wins is Pi = (W;/ WQ) and the
one plus riskless return is 1/L:iPi = Q, a number less than one. The interest rate at the
track is thus negative and solely determined by the level of transactions costs. Thus,
apart from an exogeneously set riskless rate, the participants at the track jointly
determine the security prices. For example, by betting more on one horse than
another, the state-contingent price of the first horse increases relative to the second, or
alternatively the payoff per dollar bet decreases on the first relative to the second.
The rules for division of the place and show pools are slightly more complex than
the win pool. Let Pj be the amount bet on horse j to place and P == L:jPj be the place
pool. Similarly Sk is the amount bet on horse k to show and the show pool is
S == L:kSk' The payoff per dollar bet on horse j to place is
I +[PQ- Pi -
Pj ]!(2Pj ) if
o
{ i is first and j is second or
j is first and i is second
otherwise.
Thus if horses i and j are first and second each bettor on j (and also i) to place first
receives the amount of his bet back. The remaining amount in the place pool, after the
track take, is then split evenly between the place bettors on i and j. The payoff to horse
j to place is independent of whether j finishes first or second, but it is dependent on
which horse finishes with it. A bettor on horse j to place hopes that a longshot, not a
favorite, will finish with it.
The payoff per dollar bet on show is analogous
I + [SQ - Si -
~ - Sk]!(3Sk ) if
o
{ k is fi.Ts.t, seco~d or thir~
and fInIshes WIth i and)
otherwise.
In many ways the racetrack is like the stock market. A technical strategy based on
discrepancies between the amounts bet on the same horses to win, place and show, is
examined in this paper. Since a short position has a perfectly negative correlated
outcome to the result of normal bet a given horse can be "shorted" by buying tickets
on all the other horses in a race.
The racetrack also differs from the stock market in important ways. In the stock
market, an investor's profit depends not only on the initial price he pays for a security,
lThe actual transactions cost is more complicated aoo is described below.
--- page 694 ---

Efficiency of the Market for Racetrack Betting
665
EFFICIENCY OF TIlE MARKET FOR RACETRACK BETIING
375
but also on what some other investor is willing to pay him for it when he decides to
sell. Thus his profit depends not only on how well the underlying firm does in terms of
earnings over the time he holds its stock (i.e. supply uncertainty), but also on how
other investors value that stock in the future (i.e. demand uncertainty). Given the
initial price, both the nature and behavior of other market participants determine his
profit. Thus current stock prices might depend not only on "fundamental" factor~ but
also on market "psychology"-the tastes, beliefs, and endowments of other investors,
etc. In contrast once all bets are placed at the track prior to a given race (i.e. initial
security prices are given), the result of the race and the corresponding payoffs depend
only on nature. There is no demand uncertainty at the track.
2.
Previous Work on Racetrack Efficiency
A market is efficient if current security prices fully reflect all available relevant
information. If this is the case, experts should not be able to achieve higher than
average returns with regularity. A number of investigators have demonstrated that the
New York Stock Exchange and other major security markets are efficient and
so-called experts in fact achieve returns when adjusted for risk that are no higher than
those that would be received from random investments (see Copeland and Weston [6],
Fama [9], [10] and Rubinstein [22] for discussion, terminology, and relevant references). For an exception see Downes and Dyckman [7].
Snyder [24] provided an investigation of the efficiency of the market for racetrack
bets to win. The question Snyder poses is whether or not bets at different odds levels
yield the same average return. The rate of return for odds group i is
N~(O. + I) - N
R. =
I
I
I
I
Nj
where Nj and Nj* are the number of horses, and the number who won, respectively, at
odds OJ = ( WQ / Wi - I). A weakly-efficient market in Snyder's sense would set
Ri = Q for all i, where I - Q is the percentage track take. His results as well as those
of Fabricant [8], Griffith [12], [13], McClothlin [18], Seligman [23] and Weitzman [27]
suggest that there are "strong and stable biases but these are not large enough to make
it possible to earn a positive profit" [24; 1110]. In particular, extreme favorites tend to
be under bet and longshots overbet. The combined results of several studies comparing
over 30,000 races are summarized in Table 1.
TABLE I (Snyder [24])
Rates of Return on Bets to Win by Grouped Odds, Take Added Back
Midpoint of grouped odds
Study
0.75
1.25
2.5
5.0
7.5
10.0
15.0
33.0
Fabricant
11.1'
9.0'
4.6'
-1.4
- 3.3
- 3.7
- 8.1
- 39.5'
Griffith
8.0
4.9
3.1
- 3.1
- 34.6'
- 34.1'
- 10.5
- 65.5'
McGlothlin
8.0b
8.0'
8.0'
- 0.8
- 4.6
_7.0b
- 9.7
- 11.0
Seligman
14.0
4.0
- 1.0
1.0
- 2.0
-4.0
-7.8
- 24.2
Snyder
5.5
5.5
4.0
-1.2
3.4
2.9
2.4
-
15.8
Wei~man
9.0'
3.2
6.8"
- 1.3
- 4.2
- 5.1
- 8.2b
-
18.0'
Combined
9.1'
6.4'
6.1'
- 1.2
- 5.2"
- 5.2'
- 10.2'
- 23.7"
'Significantly different from zero at 1% level or better.
b Significantly different from zero at 5% level or better.
--- page 695 ---

666
D. B. Hausch, W. T. Ziemba and M Rubinstein
376
D. B. HAUSCH. W. T. ZIEMBA AND M. R. RUBINSTEIN
Since the track take averages abou t 18%. the net rate of return for any strategy
which consistently bets within a single odds category is - 9% or less. For horses with
odds averaging 33 the net rate of return is about - 42%.
Conventional financial theory does not explain these biases because it is usual to
assume that as nondiversifiable risk (e.g. variance) rises expected return rises as well.
In the win pool expected return declines as risk increases. An explanation consistent
with the expected utility hypothesis is that investors (as a composite) are risk lovers
and behave as if the betting opportunities are limited to a single race. Weitzman [27]
and Ali [I] have estimated such utility functions. Ali's estimated utility function over
wealth w is the convex function
u( x) = 1.91 W 1.1784
( R 2 = .9981 ).
which has increasing absolute risk aversion. Thus by the Arrow-Pratt (3], [19] theory
investors will take more risk as their wealth declines. This explains the common
phenomenon that bettors, when losing, tend to bet more and more on longer odds
horses in a desperate attempt to recoup earlier losses. Moreover, since u is nearly linear
for large w investors are nearly risk neutral at such wealth levels.
A second explanation is that gamblers simply prefer low probability high prize
combinations (i.e. longshots) to high probability low prize combinations. Besides the
possible gains involved, gamblers have egos associated with analyzing racing forms
and pitting one's predictions against others. Luck and entertainment as well are largely
absent in betting favorites. The thrill is to successfully detect a moderate or long odds
winner and thus confirm one's ability to outperform the other bettors. Such a scenario
is consistent with the data and leads to the biases. Rosett [21] provides an analysis of
ways to construct low probability high prize bets through parlays and other combinations that can be used to avoid the longshot tail bias problem and to take advantage of
the favorite bias. In an effort to capitalize on this market many tracks feature such bets
in the form of the daily double, the exacta and the quinella. However, none of these
schemes appear to yield bets with positive net returns.4
Other studies of racetrack efficiency have been conducted by Ali [2], Figlewski [II]
and Snyder [24]. Ali shows that the win market is efficient in the sense that independently derived bets with identical probabilities of winning do in fact have the same
odds in a statistical sense. His analysis utilizes daily double bets and the corresponding
parlays, i.e. bet the proceeds if the chosen horse wins the first race on the chosen horse
in the second race, for 1089 races. Figlewski, using a multinomial logit probability
model to measure the information content of the forecasts of professional handicappers and data from 189 races at Belmont in 1977, found that these forecasts do contain
considerable information but the track odds generated by bettors discount almost all
of it. Snyder provided strong form efficiency tests of the form : are there persons with
special information that would allow them to outperform the general public? He found
using data on 846 races at Arlington Park in Chicago that forecasts from three leading
newspapers. the daily racing form and the official track handicapper did not lead to
bets that outperformed the general public.
4 For an entertaining account of an " expert" who was able to achieve positive net returns over a full racing
season. see Beyer (51. See also Vergin [261.
--- page 696 ---

Efficiency of the Market for Racetrack Betting
667
EFFICIENCY OF THE MARKET FOR RACETRACK BETTING
377
3.
Proposed Test
The studies described in §2 examine racetrack efficiency with respect to the win pool
only. In this paper our concern is with the efficiency of the place and show pools
relative to the win pool and with the development of procedures to best capitalize on
potential inefficiencies between these three "markets." We utilize the following definition of weak-form efficiency: the market is weakly-dficient if no individual can earn
positive profits using trading rules based on historical price information. In Baumol's
[4; 46) words .. . "all opportunities for profit by systematic betting are eliminated".
Our analysis utilizes the following two data sets: I) Data Set I: all dollar bets to win,
place and show for the 627 races over 75 days involving 5895 horses running in the
1973/74 winter season at Santa Anita Racetrack in Arcadia, California, collected by
Mark Rubinstein; and 2) Data Set 2: all dollar bets to win, place and show for the
1065 races over 110 days involving 9037 horses running in the 1978 summer season at
Exhibition Park, Vancouver, British Columbia, collected by Donald B. Hausch and
William T. Ziemba.
In the analysis of the efficiency of the win pool one may compare the actual
frequency of winning with the theoretical probability of winning as reflected through
the odds. Similar analyses are possible for the place and show pools once an estimate
of the theoretical probabilities of placing and showing for all horses is available. There
is no unique way to obtain these estimates. However, very reasonable estimates obtain
from the natural generalization of the following simple procedure. Suppose three
horses have probabilities to win of 0.5, 0.3, and 0.2, respectively. Now if horse 2 wins, a
Bayesian would naturally expect that the probabilities that horses 1 and 3 place (i.e.
win second place) are 0.510.7 and 0.2/0.7, respectively. In general if q; (i = I, ... , n)
is the probability horse i wins, then the probability that i is first and j is second is
and the probability that i is first, j is second and k is third is
q;qjqk/(1 - q;)(1 - q; - qj).
(I)
(2)
Harville [14) gives an analysis of these formulas. Despite their apparent reasonableness
they suffer from at least two flaws:
I) no account is made of the possibility of the "Silky Sullivan" problem; that is,
some horses generally either win or finish out-of-the-money-for example, see footnote
5 in (15); for these horses the formulas greatly over-estimate the true probability of
finishing second or third; and
2) the formulas are not derivable from first principles involving individual horses
running times; even independence of these random variables T 1, •• • , Tn is neither
necessary nor sufficient to imply the formulas.
In addition to assuming (I) and (2) we assume that
n
q; = W;/ 2: W;.
i-I
(3)
That is, the win pool is efficient. The discussion above, of course, indicates that this
assumption is suspect in the tails and this is discussed below. Table 2a-c compares the
actual versus theoretical probability of winning, placing and showing for data set 2.
--- page 697 ---

668
D. B. Hausch, W. T. Ziemba and M Rubinstein
378
D. B. HAUSCH, W. T. ZIEMBA AND M. R. RUBINSTEIN
Similar tables for data set 1 appear in King [17]; see also Harville (14). The usual tail
biases appear in Table 2a (although they are not significant at the 5% confidence
level). One has reverse tail biases in the finishing second and third probabilities, see
Tables 2b, c in [15]. This occurs because if the probability to win is overestimated
(underestimated) and probabilities sum to one it is likely that the probabilities of
finishing second and third would be underestimated (overestimated). Tables 2b, c,
indicate how these biases tend to cancel when they are aggregated to form the
theoretical probabilities and frequencies of placing and showing.s
TABLE 2
Actual vs. Theoretical Probability of Winning. Placing and Showing: Exhibition Park 1978
(a)
Theoretical
Number
Average
Actual
Estimated
Probability
of
Theoretical
Frequency
Standard
of Winning
Horses
Probability
of Winning
Error
0.000 -0.025
540
0.019
0.016
0.005
0.026
-0.050
1498
0.037
0.036
0.005
0.051
-0.100
2658
0.073
0.079
0.005
0.\01
-0.150
1772
0.123
0.126
0.008
0.151
-0.200
1199
0.172
0.156
0.010
0.201
-0.250
646
0.223
0.227
0.016
0.251
-0.300
341
0.272
0.263
0.024
0.301
-0.350
199
0.323
0.306
0.033
0.351
-0.400
101
0.373
0.415'
0.049
0.401+
~
0.450
".469
0.055
9037
(b)
Theoretical
Number
Average
Actual
Estimated
Probability
of
Theoretical
Frequency
Standard
of Placing
Horses
Probability
of Placing
Error
0.000 -0.025
21
0.022
0.000·
0.000
0.026
- 0.050
391
0.040
0.030
0.009
0.051
-0.100
1394
0.075
0.080
0.007
0.101
-0.150
1335
0.124
0.1 52"
0.010
0.151
-0.200
1295
0.174
0.174
0.011
0.201
-0.250
1057
0.223
0.243
0.013
0.251
- 0.300
871
0.274
0.304
0.016
0.301
-0.350
772
0.323
0.314
0.017
0.351
-0.400
580
0.373
0.3\3"
0.019
0.401
-0.450
420
0.424
0.395
0.024
0.451
-0.500
321
0.472
0.457
0.028
0.501
-0.550
202
0.523
0.415·
0.035
0.551
-0.600
149
0.573
0.483"
0.041
0.601
-0.650
114
0.623
0.570
0.046
0.651
-0.700
51
0.672
0.627
0.068
0.701
- 0.750
41
0.721
0.731
0.069
0.751 +
23
0.792
0.782
0.086
9037
S Since it is the accuracy of these probabilities rather than the q/s that is of crucial importance in the
calculations and model below this canceling provides some justification for omitting the tail biases in (3). In
practice. bets are only made on horses with expected returns considerably above I. e.g .• \.16 at Santa Anita.
Modification of the qj to include these biases might change the 1.16 to 1.14. for example. See also the
discussion below and in §§4 and 5.
--- page 698 ---

Efficiency of the Market for Racetrack Betting
669
EFFICIENCY OF THE MARKET FOR RACETRACK BETTING
379
TABLE 2 (continued)
Actual vs. Theoretical Probability of Winning. Placing and Showing: Exhibition Park 1978
(c)
Theoretical
Number
Average
Actual
Estimated
Probability
of
Theoretical
Frequency
Standard
of Showing
Horses
Probability
of Showing
Error
0.000 -0.025
0
0.026 -0.050
55
0.043
0.036
0.025
0.051
-0.100
592
0.078
0.081
0.011
0.101
-0.150
895
0.125
0.165'
0.012
0.151
-0.200
909
0.175
0.195
0.013
0.201
-0.250
799
0.224
0.292'
0.016
0.251
-0.300
885
0.275
0.289
0.015
0.301
-0.350
794
0.324
0.346
0.017
0.351
-0.400
703
0.374
0.398
0.018
0.401
-0.450
655
0.425
0.433
0.019
0.451
-0.500
617
0.475
0.452
0.020
0.501
-0.550
542
0.524
0.477'
0.021
0.551
-0.600
396
0.573
0.477'
0.025
0.601
-0.650
375
0.624
0.599
0.025
0.651
-0.700
264
0.672
0.609'
0.030
0.701
-0.750
206
0.722
0.582'
0.034
0.751
-0.800
154
0.773
0.655'
0.038
0.801
-0.850
113
0.821
0.752
0.041
0.851
-0.900
53
0.873
0.830
0.052
0.901 +
-1Q.
0.925
0.833
0.068
9037
• Categories when the theoretical probability and the actual frequency are different at the 5%
significance level are denoted by ··s. The estimated standard error is (S2/ N)t where the actual
frequency sample variance S2 = N(E(X 2) - (EX)2)/(N - I). Since the X; are either 0 or I. E(X2)
-
EX and s2 - N(EX - (EX)2)/(N - I).
Formulas (1)-(3) can be used to develop procedures that yield net rates of return for
place and show betting that are higher than expected (i.e.-18%) and indeed make
positive profits. As a first step towards development of a "system" we present the
results on the two data sets of $1 bets when the theoretical expected return is a for
varying a. The expected return from a $1 bet to place on horse I iS6.7
EX r == ± ( q/qj ) [1 + .l INT {( Q (P + 1) - (1 + PI + Pj ) ) ( _1_) x 20} ]
i-I I - ql
20
2
I + PI
i*'
.s ( ~
) [
...L
{( Q( P + I) - (I + Pi + Pd ) ( _I)
} ]
+.~ I _
.
I + 20 INT
2
I + P
x 20
,
,-I
~
I
i*'
(4)
6The expressions (4) and (5) give the marginal expected return for an additional $1 bet to place or show
on horse I. To obtain the average expected rates of return one simply replaces (I + PI) and (I + Sf) in these
expressions by PI and St. respectively. From a practical point of view with usual track data these quantities
are virtually identical.
7 A further complication, not reflected in (4) and (5) jJelow, is that a $2 winning bet must return at least
$2.10. Hence in these "minus pools" involving an extreme favorite the track's take is less than 1 - Q.
--- page 699 ---

670
D. B. Hausch, W T Ziemba and M Rubinstein
380
D. B. HAUSCH, W. T. ZIEMBA AND M. R. RUBINSTEIN
where Q is I minus the track take, P == 2:.P; is the place pool, P; is bet on horse i to
place and INT( Y) means the largest integer not exceeding Y. In (4) the quantities P
and P; are the amounts bet before an additional $1 is bet; similarly with Sand S; in
(5), below. The expressions involving INT take into account the fact that $2 bets
return payoffs rounded down to the nearest $0.10. The two expressions represent the
expected payoffs if I is first or second, respectively. Similarly the expected payoff from
a $1 bet to show on horse I is
[
I
'{( Q(S+l)-(l+S,+Sj+Sk»)( I)
}]
X I + 20 INl
3
I + S,
X 20
[ I
{( Q(S+I)-(I+S;+S'+Sk»)( I) }]
X I + 20 INT
3
. I + S,
X 20
[
I
{( Q ( S + I) - (I + S; + Sj + S, ) ) ( I)
} ]
X I + 20 INT
3
I + S,
X 20
,
(5)
where S == LS; is the show pool, S; is bet on horse i to show and the three expressions
represent the expected payoffs if I is first, second and third, respectively.
Naturally one would expect that positive profits would not be obtained, given the
inherent inaccuracies in assumptions (1)-(3), unless the theoretical expected return ex
was significantly greater than I. However we might hope that the actual rate of return
would at least increase with ex and be somewhat near ex. Table 3 indicates this is true
for both data sets. The perverse behavior for high ex in the place pool is presumably a
small sample phenomenon. Additional calculations along these lines appear in Harville
[14].
4.
A Betting Model
The results in Table 3 give a strong indication that there are significant inefficienCies
in the place and show pools and that it is possible not only to achieve above average
returns but to make substantial profits. In this section we develop a model indicating
not only which horses should be bet but how much should be bet taking into account
investor preferences and wealth levels and the effect of bet size on the odds.
We consider an investor having initial wealth Wo contemplating a series of bets. It is
--- page 700 ---

Efficiency of the Market for Racetrack Betting
671
EFFICIENCY OF THE MARKET FOR RACETRACK BETIING
381
TABLE 3
Results of Belling $1 to Place or Show on Horses with a Theoretical Expected Return of at Least a
Exhibition Park
Place
Show
Number of
Total Net
Net Rate
Number of
Total Net
Net Rate
a
Bets
Profit ($)
of Return (%)
Bets
Profit ($)
of Return (%)
1.04
225
5.10
2.3
612
33.20
5.4
1.08
126
- 10.10
-8.0
386
53.50
13.9
1.12
69
11. JO
16.1
223
40.80
18.3
1.16
40
5.10
12.8
143
26.30
18.4
1.20
18
5.30
29.4
95
21.70
22.8
1.25
II
-2.70
-24.5
44
11.20
25.5
1.30
3
-3
- 100.0
27
10.80
.40.0
1.50
0
0
3
6
200.0
Santa Anita
Place
Show
Number of
Total Net
Net Rate
Number of
Total Net
Net Rate
a
Bets
Profit ($)
of Return (%)
Bets
Profit ($)
of Return (%)
1.04
103
12.30
11.9
307
-
18.00
- 5.9
1.08
52
12.80
24.6
162
6.90
4.3
1.12
22
9.:W
41.8
89
3.00
3.4
1.16
7
2.30
32.9
46
12.40
27.0
1.20
3
-1.30
-43.3
27
6.20
23.0
1.25
0
0
9
6.00
66.7
1.30
0
0
5
5.10
102.0
1.50
0
0
0
0
natural to suppose that the investor would wish to maximize the long run rate of asset
growth and thus employ the so-called Bernoulli capital growth model; see Ziemba and
Vickson (28) for references and discussion of various assumptions and results. We use
the following result: if in each time period t = 1,2, . .. there are J investment
opportunities with returns per unit invested denoted by the random variables
X/I' ... ,xrI ' where the X/j have finitely many distinct values and for distinct t the
families are independent, then maximizing E log2:A,;x/j• s.t. 2:A,j < WI' A/; ;;. 0 maximizes the asymptotic rate of asset growth. The assumptions are quite reasonable in a
horseracing context because there are a finite number of return possibilities and the
race by race returns ar~ likely to be nearly independent since different horses will be
running (although the jockeys and trainers may not be).
The second key feature of the model is that it considers an investor's ability to
influence the odds by the size of his bets.8 This yields the following model to calculate
SThe first model to include this feature seems to be Isaacs [16J. Only win bets are considered with linear
utility, and he is able to determine the. el(act solution in closed form. His model may be useful in situations
where the perfect market assumption (3) is violated or where special expertise leads one to believe their
estimates of the q; are better than those of the other bettors.
--- page 701 ---

672
D. B. Hausch, W T Ziemba and M Rubinstein
382
D. B. HAUSCH, W. T. ZIEMBA AND M. R. RUBINSTEIN
the optimal amounts to bet for place and show.
n
Q( P + 2:1-1 PI) - (Pi + Pj + Pi + Pj )
2
n
+ Wo -
2:
51-
1- 1
I".i.j.k
s.t. 2: (p, + s,) <: wo,
p, > O,S, > 0,/ = I, .. . , n,
'-I
(6)
where Q = 1 - the track take, W;, lJ and Sk are the total dollar amounts bet to win,
place and show on the indicated horses by the crowd, respectively, W == ~ Wi'
P =="LlJ and S == "LSk are the win, place and show pools, respectively, qi == Wi / W is
the theoretical probability that horse i wins, Wo is initial wealth and p, and s, are the
investor's bets to place and show on horse I, respectively.
The formulation (6) maximizes the expected logarithm of final wealth considering
the probabilities and payoffs from all possible horserace finishes. It is exact except for
the minor adjustment made that the rounding down to the nearest $0.10 for a two
dollar bet, see (4) and (5), is omitted.9 For the values of a ~ 1.16 it was observed that
in a given race at most three p, and three s, were nonzero. When (6) is then simplified it
can be solved in less than I second of CPU time.1O A discussion of the generalized
concavity properties of (6) will appear in a forthcoming paper by Kallberg and
Ziemba.
The results are illustrated by function 1 in Figures 1 and 2 for the two data sets
using an initial wealth of $10,000. In both cases the bets produced from (6) lead to well
above average returns and to positive profits. J J These results may be contrasted with
random betting; function 2 in Figures 1 and 2. Intuition suggests that Santa Anita with
its larger betting pools would have more accurate estimates of the qi than would be
obtained at Exhibition Park. Hence positive profits would result from lower values of
a. The results bear this out and only horses with a ~ 1.20 for Exhibition Park were
considered for possible bets. Generally speaking the bets are usually favorites and
almost always on those horses with maximum (Wj W)/(Pj P) and (Wi/ W)/(Sj S)
91t is possible to include this feature in (6) but it greatly complicates the solution procedure (e.g.
differentiability is lost) with lillie added gain in accuracy.
10 All calculations were made on UBC's AMDAHL 470V6 Model II computer using a code for the
generalized reduced gradient algorithm.
11 The procedure was to calculate the optimal bets to place and show in each race using (6) with the
present wealth level. The results of the race and the actual payoffs that reflect the track's take and breakage
are known. The payoff for our investor's bets were calculated using all the bets of the crowd plus the bets of
our investor taking into account the track's take and breakage. i.e. the payoffs are thus those that would
have occurred had our investor actually made his bets. The wealth level was then lIdjusted to reflect the
race's gain or loss and the procedure continued for all races.
--- page 702 ---

Efficiency of the Market for Racetrack Betting
673
EFFICIENCY OF THE MARKET FOR RACETRACK BETTING
383
18000
17263
17242
:I:
f-
...J «
w
~
Wo
3
6000
4000
2000 2500
"'- '. 2
00
10
20
30
40
SO
60
70
80
DAYS
I Results from eKpected log betting to place and show when expected returns are 1.16 or better with initial
wealth SIO,OOO.
2 Approximate wealth level history for random horse betting. Total dollars bet is as in system I (S 116,074).
Track payback is 82.5%, therefore final wealth level is SI0,000-0.175(SI16.074)- -SIO,313 (Note:
breakage is not taken into consideration)
] Results from using the Exhibition Park approximate regression scheme (with initial wealth S2,500) at
Santa Anita.
FIGURE 1.
Wealth Level Histories for Alternative Betting Schemes; Santa Anita: 1973/74 Season.
ratios. These ratios of the theoretical probability of winning to the track take unadjusted odds to place or show form a type of cost-benefit ratio that provides a first
approximation to a. This is discussed further in §5, below. Most of the bets are to show
and one tends to bet only about once per day. The numbers of bets and their size
distribution are presented in Table 4. As expected, the influence on the odds made by
our investor's bets is much greater at Exhibition Park hence the bets there tend to be
much smaller than at Santa Anita. However, even there about 10% of the bets exceed
$1000.
The log formulation has absolute risk aversion 1/ w, which for wealth around
$10,000 is virtually zero. Zero absolute risk aversion is, of course, achieved by linear
utility. One then will bet on the horse (or horses) with the highest a until the influence
on the odds drops this horse (or horses) below another horse's a, etc., continuing until
there are no favorable bets fr the betting wealth has been fully utilized. The results of
such linear utility betting With Wo = $10,000 are: at Exhibition Park with a ;;. 1.20 final
wealth is $14,818; at Santa Anita with a;;' 1.16 final wealth is $10,910. Such a strategy
is a very risky one and leads to some very large bets. The log function has the distinct
advantage that it implies negative infinite utility at zero wealth hence bets having any
significant probability of yielding final wealth near zero are avoided.
--- page 703 ---

674
D. B. Hausch, W. T. Ziemba and M Rubinstein
384
D. B. HAUSCH, W. T. ZIEMBA AND M. R. RUBINSTEIN
18000
::t:
1.6220
f- 16000
....J
<t:
\.lJ 14000
~
12000
Wo = 10000 '------
8000
--'- --"""'--.0--
6000
-- '- --.
4000
-"", , --,""'--. -. - -2
2000
0
0
10
20
30
40
50
60
70
80
90
100
110
DAY
I Results from expected log betting to place and show when expected returns are 1.20 or better with initial
wealth S 10,000.
2 Approximate wealth level history for random horse betting. Total dollars bet is as in system 2 (S8461).
Track payback is 81.9% therefore final wealth level is SIO,OOO - 0.181($38461) = $3,035. (Note: Breakage is
not taken into consideration.)
FIGURE 2.
Wealth Level Histories for Alternative Betting Schemes; Exhibition Park: 1978 Season.
TABLE 4
Size Distribution of Bets, Wo = $10,000, Log Utility
Santa Anita
Exhibition Park
Place
Show
Place
Show
%of
%of
%of
%of
%of
%of
%of
%of
Size
Bets
$Bet
Bets
SBet
Bets
SBeL
Bets
SBet
0-50
7.1
0.3
2.6
0.1
29.4
3.6
17.0
1.0
51-100
0
0
1.3
0.1
23.5
6.7
13.8
2.8
101-200
0
0
3.9
0.4
5.9
2.9
22.3
9.3
201-300
21.4
6.1
5.2
1.0
5.9
4.4
14.9
10.3
301-500
7.1
3.2
9.1
2.6
23.5
30.6
8.5
9.1
501-700
14.3
10.3
13.0
5.7
0
0
6.4
10.5
701-1000
14.3
14.4
7.8
4.8
0
0
7.4
17.5
> 1001
35.8
65.7
57.1
85.3
11.8
51.8
9.7
39.5
n -
14 SII,932 n -77 $104, 142
n -
17
$4,954 n - 94"
$33,507
ToO' pi \0' L. r
Bets
Bets
~"' PI"/ ~'" Show
Bets
Bets
Total Sa~ta = $116 074
Anita Bettmgs
'
'Two of these bets had EX: ;. 1.20 and st = O.
Total Exhibition = $38 461
Park Belling
,
--- page 704 ---

Efficiency of the Market for Racetrack Betting
675
EFFICIENCY OF THE MARKET FOR RACETRACK BETTING
385
S.
Making the System Operational
The calculations reported in Figures I and 2 were made under the assumption that
the investor is free to bet once al1 other bettors have placed their bets. In practice one
can only attempt to be one of the last bettors. 12 There is a natural tradeoff between
placing a bet too early and increasing the inaccuracies and running the possibility of
arriving too late at the betting window to place a bet. 13 The time just prior to the
beginning of a race is crucial since many bets are typically made then including the so
called "smart money" bets made very close to the beginning of the race so their impact
on other bettors is minimized. It is thus extremely important that the investor be able
to perform all calculations necessary to place the bet(s) very quickly. Typically, since
tracks have neither public phones nor electricity, calculations can at most utilize
battery operated calculators or possibly a battery operated special purpose computer.
Even if computing times were negligible the very act of punching in the data needed
for an exact calculation is too time-consUJping since it takes more than one minute.
Therefore, in practice, approximations that utilize a limited number of input data
elements are required. Several types of approximations are possible such as the tabular
rules of thumb developed by King [17] or the regression procedures suggested here.
Our procedure indicates whether or not a bet to place or show is warranted and at
what level using the following eight data inputs: wo, Wi*' Pi*, ~*' 8;., W, P and S,
where i* is an i for which (WJ W)/(PJ P) is maximized and}* IS a) for which
(Uj/W)/(S/S) is maximized. It is easy to determine i· and}*, particularly since i*
often equals)*, by inspection of the tote board. The approximation supposes that the
only possible bets are i* to place and)· to show. The regressions, as given below, must
be calibrated to a given track and initial wealth level. As a prelude to actual betting
the 'regressions were calibrated at Exhibition Park for Wo = $2500. For calculated i* the
expected return on a $1 bet to place is approximated by
_
Wi./W
EXt. = 0.39445 + 0.51338 Pi./ P ,
R2 = 0.776.
(7)
If EXt.;.. 1.20 then the optimal bet to place is approximated by
Pi. = -459.32 + 1715.6qi.-0.042518qi.P -7440.1qt.
+ 1379Iq? +0.J0247Pi.+49.572lnwo,R2 = 0.954.
(8)
Similarly for}* the expected return on a $1 bet to show is approximated by
_
~*/W
EX/. = 0.64514 + 0.32806 Sj./ S '
R2 = 0.650.
(9)
12The model as developed in this paper utilizes an inefficiency in the place and show pools to yield
positive profits. A:1 investor's bets are determined by his wealth level as well as the profitability of one or
more such bets. There mayor may not exist "enough" inefficiency to provide positive profits for additional
investors using a system of this nature. In "the context of the Isaac's model, for win bets with linear utility,
Thrall (25) showed that if there were positive profits to be made and each new investor was aware of all
previous investor's bets then the profits for these various bettors are shared and in the limit become zero. It
is likely that a similar result obtains for the model discussed here.
I) At some tracks, such as Santa Anita, betting ends precisely at post time when the electric totalizator
machines are shut off. At other tracks including Exhibition Park. betting ends when the horses enter the
starting gate which may be 2 or even 3 minutes past the post time.
