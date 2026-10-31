# Volatility Trading_ Sinclair_Volatility Trading -- Euan Sinclair(auth_) -- Wiley Trading, 1, 2013 -- John Wiley & Sons, Incorporated -- isbn13 9781118347133 -- 2634a86bfed8248fa7ba3fb72595bbbc -- Anna’s Archive.pdf — Chapter 5: Implied Volatility Dynamics (pages 83–102)

--- page 83 ---

67
C H A P T E R 5
Implied Volatility
Dynamics
I
n the previous chapters, we have looked at ways to measure and forecast
realized volatility. In a sports gambling context, this would be akin to
our forecasting which team would be most likely to win the game. In this
chapter, we look at the ways implied volatility can move. This would be
the equivalent of predicting how the bookmakers’ line might move before
the game. Remember that we are not trading either realized or implied
volatility directly. We are trading the spread between the two, so edge can
be found on both sides.
It is difﬁcult to talk about the characteristics of the implied volatility
because there are a number of implied volatilities; generally each distinct
put/call pair has its own volatility. This forms the well-known volatility
surface. Figure 5.1 shows a typical volatility surface for a set of index
options, the NASDAQ-100 Trust Series 1 exchange-traded fund (QQQQ).
It has signiﬁcant structure both across strikes and maturity. We separately
show the strike and term structure in Figures 5.2 and 5.3.
Before we analyze the shapes that the surface takes, let’s take a moment to
remember what is important to us as traders. When trading vanilla options
we are primarily interested in things that move. Shapes are less important
to us. Changes in shapes may be important. If we were trading structured
products this may well not be the case. Here the volatility smile would
be an input to another model, and taking the shape into account could be
necessary to avoid arbitrage. We look at such an example in Chapter 13
where we discuss options on leveraged exchange-traded funds (ETFs).
One way of determining the relative importance of different types of
movement is principal component analysis (PCA). This is a mathematical
Volatility Trading,   Second Edition.    Euan Sinclair
© 2013 Euan Sinclair. Published 2013 by John Wiley & Sons, Inc.
--- page 84 ---

IMPLIED VOLATILITY DYNAMICS
68
40 41 42 43 44 45 46 47 48 49 50 51 52 53 54 55
16
142
0
0.05
0.1
0.15
0.2
0.25
0.3
0.35
0.4
0.45
Implied Volatility
Strike
Time (Days)
FIGURE 5.1
The Implied Volatility Surface for QQQQ on August 1, 2007
0
0.05
0.1
0.15
0.2
0.25
0.3
0.35
0.4
0.45
0.5
40
41
42
43
44
45
46
47
48
49
50
51
52
53
54
55
Strike
Implied Volatility
FIGURE 5.2
The Implied Volatility of the August Options as a Function of Strike for
QQQQ on August 1, 2007
techniqueusedtoreducethedimensionalityofdatasets.Foranintroduction,
refer to Alexander (2001a). Derman and Kamal (1997) applied PCA to
S&P 500 and Nikkei options. They examined the daily change in the
volatility surface where it was parameterized by delta and time to maturity.
Skiadopoulos, Hodges, and Clelow (2000) applied PCA to changes of S&P
500 implied volatilities for given maturity buckets, using both strike and
moneyness metrics. Alexander (2001b) applied PCA to daily changes in the
deviations of strike volatilities from the at-the-money (ATM) volatilities.
Alexander’s work is most directly useful to us. She showed that a parallel
shift of the implied volatility smile accounted for between 65 and 80 percent
--- page 85 ---

IMPLIED VOLATILITY DYNAMICS
69
0.217
0.218
0.219
0.22
0.221
0.222
0.223
0.224
0.225
0.226
0.227
0.228
0
20
40
60
80
100
120
140
160
Time (Days)
ATM Implied Volatility
FIGURE 5.3
The Term Structure of Implied Volatility for the At-the-Money Options
for QQQQ on August 1, 2007
of the total variation of volatility. A tilting of the curve explained a further
5 to 15 percent of the variation, and the curvature component explained
about another 5 percent of the changes. So the most important thing to
understand is the dynamics of the overall level of volatility, followed by the
slope of the curve. Don’t ever forget this point. The dynamics of the smile
can be seductive, and many very smart people have spent a lot of time and
money examining its dynamics, but the level of volatility is many times more
changeable and hence more economically signiﬁcant.
The fact that the overall level of implied volatility is the dominant risk
factor also partially addresses the objection that the at-the-money implied
volatility is not the correct thing to compare to our realized volatility
forecast. Technically this is correct. We should compare our volatility
forecast to the implied volatility swap, a structure consisting of the weighted
average of a continuum of option prices. But in practice this isn’t really
a good way to go about trading the implied/realized spread, for several
reasons:
■The number of available strikes is usually very limited so the constructed
swap will not be particularly close to its ideal.
■The bid/ask spread in the options that needs to be crossed makes
construction of the swap very expensive.
■At-the-money volatility movement dominates the movement of the
implied volatility surface.
--- page 86 ---

IMPLIED VOLATILITY DYNAMICS
70
Short Straddle
−2.5
−2
−1.5
−1
−0.5
0
0.5
1
1.5
2
2.5
80
85
90
95
100
105
110
115
120
Moneyness
Profit
FIGURE 5.4
The Payoff of a Short Straddle Position
Note: This is proﬁtable if the underlying doesn’t move too much or is not volatile. This is the option
traders’ working deﬁnition of volatility.
■Visual inspection of the payoff structure of a straddle position should
clearly show that this position is dependent on the absolute movement
of the underlying (see Figure 5.4). Remember that in Chapter 1 we
stated that we were only thinking of volatility as a crude proxy for
this movement. All ﬁnite samples have volatility. It is just a simple
measurement of an admittedly far more complex phenomenon.
■Volatility Level Dynamics
First we look at the dynamics of the overall level of implied volatility. We
could examine the actual volatility of the ATM options, but this is tricky.
First note that there generally is no actual at-the-money option. There
is a strike slightly below the actual ATM point and another above it. Each
strike has a put and a call. Finally, each option has a bid price and an offer
price. So to get the ATM volatility we need to construct an appropriately
weighted average of these eight implied volatilities. Next, we have to
average this number with that obtained from another maturity to get a
constant maturity implied volatility. The details and choices involved in
this process can signiﬁcantly alter the ﬁnal number.
Alternatively, we can use a model-free implied volatility such as the
Volatility Index (VIX) index published by the CBOE (this is based on
the S&P 500 index, but indexes based on similar methodologies are
available from commercial vendors such as ivolatility.com). This used to
--- page 87 ---

IMPLIED VOLATILITY DYNAMICS
71
0
5
10
15
20
25
30
35
40
45
50
1/2/1990
1/2/1991
1/2/1992
1/2/1993
1/2/1994
1/2/1995
1/2/1996
1/2/1997
1/2/1998
1/2/1999
1/2/2000
1/2/2001
1/2/2002
1/2/2003
1/2/2004
1/2/2005
1/2/2006
1/2/2007
VIX
FIGURE 5.5
The VIX Implied Volatility Index
be constructed from averaged option implied volatilities but is now based
on the concept of model-free volatility. Figure 5.5 shows the VIX from its
inception at the start of 1990 until the end of July 2007.
So we do the broad analysis of implied volatility by using volatility indices,
but we have to trade the level given by the at-the-money option. This is just
another example of the messiness inherent in trading.
Several crude features can be seen immediately:
■The level of the VIX has two regimes: a high and volatile regime where it
oscillates between 20 and 40, and a regime where it is quieter and stays
between 10 and 20.
■The volatility of the index is positively related to the level.
■There are more large moves up than down.
■It seems to be, locally at least, mean-reverting.
This last statement needs further elaboration, as it is something that is
often said but equally often left undeﬁned. (See accompanying box.)
Mean Reversion
Traders and analysts often say that volatility is a mean-reverting process
(this was a reason that we preferred the generalized auto regressive
conditional heteroskedasticity [GARCH] model to the exponentially
weighted moving average model [EWMA] for forecasting realized
--- page 88 ---

IMPLIED VOLATILITY DYNAMICS
72
volatility), but there is often a lack of precision in what they mean.
Here we look at several different deﬁnitions of mean reversion so we
can have some unambiguous things to look for when discussing the
dynamics of implied volatility. (Incidentally, the same ambiguity exists
when discussing trends in ﬁnancial markets. It often seems obvious
in retrospect that a trend has occurred but traders ﬁnd it difﬁcult to
deﬁne in advance exactly what one is).
Informal Deﬁnition
A time series is mean-reverting if it falls after reaching a maximum
and rises after reaching a minimum.
This deﬁnition is intuitively appealing. All that needs to be done
is to look at the series, ﬁnd the extreme values, and then see if the
series subsequently reversed from these. According to this thinking,
the equity market was clearly undervalued in the early 1980s and
drastically overvalued in the middle of 1987. Unfortunately, this
deﬁnition is also self-fulﬁlling. It is a truism to say that a series will
be lower after its maximum. This applies to any series at all. We will
need to come up with something more falsiﬁable.
More Formal Deﬁnition
A time series is mean-reverting if its returns have negative autocorrelation.
Under this deﬁnition, a below-average return in one period is
compensated for by a higher-than-average return in subsequent periods. The VIX is mean-reverting under this deﬁnition. It has a daily
autocorrelation of −0.04, weekly of −0.21, and monthly of −0.12.
This model can be simply expressed as
Rt = ρ(Rt−1 −µ) + µ + σZt
(5.1)
where
R is the returns at time t
ρ is the autocorrelation
µ is the mean return
σ is the volatility of the returns
Z is a draw from a standard normal distribution
A realization of this process is given in Figure 5.6.
--- page 89 ---

IMPLIED VOLATILITY DYNAMICS
73
−10
−8
−6
−4
−2
0
1
3
5
7
9
11
13
15
17
19
21
23
25
27
29
31
33
35
37
39
41
43
45
47
49
51
2
Time
Rt
4
6
8
10
FIGURE 5.6
A Mean-Reverting Random Process as Described by Equation 5.1
(The parameters were µ = 0, ρ = −0.2, and σ = 2.8)
Now contrast this with Figure 5.7.
−8
−6
−4
−2
0
2
4
6
8
10
1 3 5 7 9 11 13 15 17 19 21 23 25 27 29 31 33 35 37 39 41 43 45 47 49 51
Time
Rt
FIGURE 5.7
Weekly Returns of the VIX in 1990
This is obviously not proof of anything, but it is certainly suggestive
that this form of mean reversion is applicable to the VIX, at least for
short periods.
A Trader’s Deﬁnition
A time series is mean-reverting if it can be proﬁtably traded by
methods that assume that moves tend to reverse instead of continue.
This deﬁnition allows for many different processes. It is far broader
than assuming negative autocorrelation. A number of the classical
--- page 90 ---

IMPLIED VOLATILITY DYNAMICS
74
technical indicators can form the basis for such a system. (Please note
that we are asserting nothing about the general efﬁcacy of technical
analysis; it is just being used as a test in this speciﬁc case.)
The VIX also passes this test. A simple Bollinger band strategy
where we sell two standard deviations above an EWMA or buy two
standard deviations below an EWMA and exit at the close of the next
day would have been a solid winner. It has produced 62.2 percent
winning trades with average winners being 1.05 points and average
losers being 0.93 points since January 1990. This could be made better
by tweaking the parameters, and by setting the buy level differently
to the sell level to take the asymmetry of movement into account,
but that isn’t the point here. We don’t aim to make a viable trading
system. We just claim that the VIX does what a trader expects a
mean-reverting time series to do. (This system is useless in practice,
as the spot VIX index doesn’t trade. Sadly, things that are easy to price
are usually hard to trade.)
However, the central idea behind this very simple system is
important. Large implied volatility moves will often reverse. This
should be kept in mind when we enter option positions.
More formal time series models give mixed results. Some researchers
have claimed success in their predictions of implied volatility (Ahoniemi
2006; Brooks and Oozeer 2002), but the models seem to be of limited
practical use as trading tools.
However, there are clear regularities in the evolution of at-the-money
implied volatilities that can form the basis of trades. An example is the
evolution of implied volatilities before a company’s earnings announcement.
The front-month volatility will almost always rise signiﬁcantly in the weeks
before the earnings release. An example is shown in Figure 5.8, where we
see the evolution of the front-month volatility for Apple (AAPL) for the
month before the second-quarter earnings announcement after the close
on April 25, 2007. This pattern of implied volatility rising before the
announcement, then dropping once the news is released, is ubiquitous.
It certainly appears that there is a trading opportunity here. Actually
there are two. The ﬁrst idea is to buy implied volatility a few weeks before
earnings in anticipation of implied volatility rising. This can sometimes
work. Remember, though, that while implied volatility will be rising, the
actual prices of the options will probably not be: You will need the vega
proﬁts and the proﬁts from scalping the long gamma to offset the decay of
the options due to the passing of time. This is certainly worth looking for,
--- page 91 ---

IMPLIED VOLATILITY DYNAMICS
75
0.3
0.32
0.34
0.36
0.2
0.22
0.24
0.26
0.28
5/3/2007
4/28/2007
4/23/2007
4/18/2007
4/13/2007
4/8/2007
4/3/2007
3/29/2007
3/24/2007
3/19/2007
Implied Volatility
Date
FIGURE 5.8
The AAPL Front-Month Volatility around the Second Quarter 2007
Earnings Release
althoughtransactioncostslimittheapplicabilityoftheideatothemoreactive
stocks.
A direct test of this idea is simple if tedious. Before earnings, we buy the
straddle and hope that the increase in implied volatility and movement of
the underlying compensates us for the time decay in the position.
■Buyafront-monthstraddle10days(orascloseaspossible)beforeearnings
are announced and sell on the close of the day before the announcement.
■Normalize results by dividing by the price of the underlying (so the results
are independent of the stock price).
We tested this on a sample of 73 stocks (large capitalization stocks with
continuous prices and option data) from Q1 2005 until Q3 2010. Assuming
a bid/ask spread of two cents (this reﬂects costs now, not necessarily what
they were in the past, so these results are of what might be possible now
and going forward and don’t reﬂect what the strategy may have made in
real trading historically), the results are:
■Forty-three percent of trades were proﬁtable.
■Win size/loss size is 1.70.
■The results are skewed positively (skewness of 5.4) and fat-tailed (excess
kurtosis of 76.6).
We need to convert these results into trades. We put a $10,000 notional
size bet on each trade. So, for example, on a $100 stock we would buy one
straddle ($100 stock price times the 100 shares that each option is on). The
results of this are shown in Figure 5.9.
--- page 92 ---

IMPLIED VOLATILITY DYNAMICS
76
0
5,000
10,000
15,000
20,000
25,000
30,000
35,000
40,000
1
2
3
4
5
6
7
8
9 10 11 12 13 14 15 16 17 18 19 20 21 22 23
Time Period
PL ($)
FIGURE 5.9
Results of the Long Straddle Strategy
It is important to note that Figure 5.9 shows proﬁts on an earnings cycle
basis. The daily variation would be higher.
Although this trade is clearly proﬁtable, we can improve it by looking
at the types of stocks that do well. We noted in Chapter 4 that grouping
stocks by their fundamentals helped us forecast volatility. Are similar effects
in play here?
We analyzed the results as functions of price-to-earnings ratio (PE),
market cap, dividend yield, number of analysts covering the company, and
the dispersion of the analyst earnings estimates, which are deﬁned as (high
estimate-low estimate)/average estimate.
The ﬁrst thing to note is that any relationship is nonlinear and won’t be
captured by correlation. This can be seen in Figure 5.10, where we plot the
P/L as a function of analyst dispersion.
However, we can use a more robust method to look for relationships.
We divide the sample of companies into quartiles for each factor and look
at the average PL. This is shown in Table 5.1.
As we can see, there is no clear pattern when we sort the results by
quartiles for PE, capitalization, yield, or the number of analysts. However,
the relationship to dispersion is interesting. Stocks with high dispersion are
more proﬁtable. High dispersion literally means that the analysts disagree
about the unreleased earnings. This means we are in a situation of uncertainty. The implied volatility of the options increases because of this and
we make money being long volatility. This doesn’t happen instantaneously
because it takes time for the analysts to report their forecasts and the market
to realize that they don’t agree.
--- page 93 ---

IMPLIED VOLATILITY DYNAMICS
77
–2
–1
0
1
2
3
4
5
0
20
40
60
80
Dispersion
Average P/L (%)
FIGURE 5.10
Results of the Long Straddle Strategy as a Function of Analyst Forecast
Dispersion
TABLE 5.1
Proﬁtability ($) of the Long Straddle Strategy
as a Function of Fundamentals
Quartile PE Market Cap Dividend Yield Analysts Dispersion
Lowest
51
19
52
10
3
Second
5
17
−9
23
10
Third
21
41
10
22
14
Fourth
7
3
31
20
48
Next we test the proﬁtability of selling volatility over earnings. Before
earnings we will sell the straddle and hope that the collapse in implied
volatility compensates us for the movement of the underlying.
■Sell a front-month straddle the day (or as close as possible) before
earnings are announced and buy it back on the close of the day after the
announcement.
■Normalize results by dividing by the price of the underlying (so the results
are independent of the stock price).
We tested this on the same sample of 73 stocks from Q1 2005 until Q3
2010. The results are:
■Sixty-four percent of trades were proﬁtable.
■Win size/loss size is 0.69.
■The results are skewed negatively (skewness of negative 2.1) and fat-tailed
(excess kurtosis of 12.2).
--- page 94 ---

IMPLIED VOLATILITY DYNAMICS
78
–5,000
0
5,000
10,000
15,000
20,000
25,000
30,000
1
2
3
4
5
6
7
8
9 10 11 12 13 14 15 16 17 18 19 20 21 22 23
Time Period
PL ($)
FIGURE 5.11
Results of the Short Straddle Strategy
Sizing in the same way as before, we arrive at the results shown in
Figure 5.11.
As before, we look at the dependence of the results on the fundamental
factors. The results are shown in Table 5.2.
In this case it seems that there is a slight tendency for this strategy to fare
poorly with high PE stocks. Studies have shown that such growth stocks do
react to earnings differently to value stocks and this effect might be related
(He, Lee, and Wei 2010). In any event, the effect observed is weak if it is
even real.
But again we see a link with analyst dispersion: High dispersion leads to
higher proﬁts. There are likely two reasons for this. Remember that we are
trading the implied volatility of the options against the realized volatility of
the stock as it moves in reaction to the news release. As we stated earlier,
high analyst dispersion leads to high implied volatility so we will be selling
the straddle at a good price. But we also beneﬁt from the dispersion with
regard to the actual move of the stock price. Stocks move when news
comes out. News is, by deﬁnition, something that isn’t priced into the stock
TABLE 5.2
Proﬁtability ($) of the Short Straddle Strategy
as a Function of Fundamentals
Quartile
PE
Market Cap Dividend Yield Analysts Dispersion
Lowest
29
6
16
23
11
Second
24
30
1
6
14
Third
23
9
29
20
24
Fourth
−2
29
30
24
25
--- page 95 ---

IMPLIED VOLATILITY DYNAMICS
79
already, that is, something contrary to expectations. Wide dispersion is a
reﬂection of the fact that analysts, and hence the market, have no coherent
expectation. There can be no ‘‘surprise’’ if no one agrees on what to expect.
The idea of trading implied volatility’s reaction to impending news
is also applicable to other products. For example, interest rate products
display a similar pattern before large economic releases, and commodity
implied volatilities generally rise before inventory or crop reports. Indeed,
a study by Carr Futures (Panos 1997) showed that from January 1994 until
December 1996, buying delta-neutral straddles at the close on the Monday
of the week of an unemployment report (released on Friday before the
market opens) and selling at the close on Thursday would have realized a
proﬁt of about nine option ticks (a 6.53 percent return).
When we sell options over such an event, it can be helpful to calculate
the jump in the underlying price that is being implied by the option prices.
To ﬁnd the implied jump, we compare the ATM implied volatilities of the
front-month and second-month options. The assumption is that just before
the event, most of the difference will due to the uncertainty because of the
announcement. There may also be other reasons for the difference, but we
hope the event is the dominant one.
First note that if the front-month implied volatility is lower than that of
the second month, the event is not being projected to cause any movement.
If the front month is higher than the second month, we need to ﬁrst
calculate the forward volatility, σ12, the volatility being implied from the
ﬁrst expiration at T1 until the second expiration at T2. This is
σ12 =

σ2
2T2 −σ2
1T1
T2 −T1
(5.2)
where
σ1 is the implied volatility of the front month
σ2 is the implied volatility of the second month
The volatility attributed to the event, σE, is the difference of the
front-month volatility and the forward volatility.
σE =

T1(σ2
1 −σ2
12) =

(σ2
1 −σ2
2) T1T2
T2 −T1
(5.3)
Now, using Equation 2.12 we ﬁnd that the expected absolute return (the
jump) is
E(|R|) =

2
π σE
(5.4)
--- page 96 ---

IMPLIED VOLATILITY DYNAMICS
80
Using Equation 5.4, we can ﬁnd the expected jump from the front two
implied volatilities and compare this to our estimate of the actual move in
the underlying.
■The Smile and the Underlying
There are two widely used heuristics that attempt to describe the movement
of the implied volatility smile as a function of the underlying’s moves: the
sticky strike rule and the sticky delta rule. Sticky strike says that the volatility
of a given strike is unchanged as the underlying moves. Sticky delta says that
the smile moves with the underlying so that options with a given delta keep
the same volatility. So, for example, the strike of a 10-delta call will change
but the volatility of the 10-delta call will remain constant. These rules are
also known as ﬁxed skew and ﬂoating or swimming skew respectively.
Neither rule describes real market dynamics particularly well. Derman
(1999) tested the rules by examining S&P 500 options. He found that the
sticky strike rule was used by the market when the underlying was range
bound and the sticky delta rule was used when the market was trending.
In other words, each heuristic works sometimes. This makes sense, as
these rules are really just an encapsulation of the option market’s opinion
at a given time. Traders should be comfortable with both situations and
understand the implications of their choice.
Sticky Strike
Mathematically, this rule says that implied volatility is independent of the
underlying.
∂σ(X)
∂S
= 0
(5.5)
Recall that the instantaneous P/L for a hedged long option position is
1
2S2(σ2
realized −σ2
implied)
(Equation 1.7)
Under sticky strike conditions this results makes it possible to set up
portfolios that are arbitrages.
Consider a delta-neutral call spread with the short leg weighted by the
ratio of the individual option gammas.
C1(X1) −1
2
C2 (X2)
(5.6)
--- page 97 ---

IMPLIED VOLATILITY DYNAMICS
81
With X1 > X2 and σ(X1) < σ(X2) (i.e., a downward sloping implied
volatility curve). Now if we calculate the PL for this spread, the realized
variance terms cancel and we get
1
2S21(σ2
2 −σ2
1)
(5.7)
This is always positive (we have set up a positive gamma position that
also collects theta).
Sticky Delta
This implied volatility rule also admits arbitrages. Consider a dynamically
hedged, delta-neutral risk-reversal where we are short an out-of-the-money
put and long an out-of-the-money call. Under the assumption of sticky
delta, if the underlying increases, both options’ implied volatilities will
increase. However, the call will now be closer to the at-the-money point
and hence now have more vega than the put. So the call’s value will rise
more than the put’s will fall. The portfolio will make money. Similarly, if
the underlying drops, both options will decrease in value but this time the
short put will fall more and again the portfolio will be proﬁtable.
Another way of seeing that sticky delta can be correct in only a limited
sense is what we have seen in Chapter 3: that realized volatility typically rises
when the underlying falls and that this will lead to a corresponding rise in
the at-the-money implied volatility. Sticky delta doesn’t have this effect: It
keeps the implied volatility of the (changing) at-the-money strike constant.
An attempt to address this is to ﬂoat the volatility curve on a ‘‘backbone’’
or ‘‘path,’’ which is a decreasing function of strike. This is illustrated in
Figure 5.12. The slope of this path can be estimated by regressing historical
implied volatility changes on historical underlying returns, but this is likely
to be fairly inconclusive. In practice the trader normally chooses the gradient
to match current market behavior.
No matter how we have decided to move implied volatility as a function
of the underlying, we should incorporate the volatility change into our
delta. Although formally delta is deﬁned as the partial derivative of the option
price with respect to the underlying, traders typically like it to describe
their total directional exposure, that is, the total derivative.
dC
dS = δC
δS + δC
δσ
δσ
δS
= ∆BSM + vegaδσ
δS
(5.8)
--- page 98 ---

IMPLIED VOLATILITY DYNAMICS
82
0
0.1
0.2
0.3
0.4
0.5
0.6
0.7
0.8
80
82
84
86
88
90
92
94
96
98
100
102
104
106
108
110
112
114
116
118
120
Strike
Implied Volatility
FIGURE 5.12
The Implied Volatility and Its Backbone as Functions of Strike
So, for example, if we are using the sticky delta paradigm we would
need to modify the Black-Scholes-Merton (BSM) delta in order to stay
directionally neutral.
■Smile Dynamics
Next we can examine the nature of the smile. We said earlier that the
smile isn’t as signiﬁcant as the level of volatility. This is true, but it isn’t
totally insigniﬁcant. There are several academic studies that show that smile
effects are proﬁtably tradable if transaction costs are sufﬁciently small (e.g.,
Goncalves and Guidolin 2005; Jha and Kalimipalli 2006). Also, all traders
need to be able to monitor and understand the smile in order to ﬁnd the
best strikes to trade. This becomes most relevant for products with many
strikes, so trades that isolate skewness (ratio spreads and risk reversals)
and kurtosis (butterﬂies and condors) are able to be constructed. It is also
of most relevance to market makers who can enter multilegged positions
without crossing the entire bid/ask spread in the option market.
Smiles exist for a number of reasons (this list is not exhaustive):
■In many products the typical end user is long and will naturally buy
downside protection.
■In equity products, longs may also have a propensity to sell calls against
their long stock positions.
■Upside strikes often trade at a premium to the at-the-money strike in
equities, due to the implied chance of a takeover. (Obviously this will
--- page 99 ---

IMPLIED VOLATILITY DYNAMICS
83
create a different curve than the previous effect, and which effect is
stronger will be highly productand period-speciﬁc.)
■If customers are long puts and short calls, then the market makers will
be short puts and long calls. Typically the customers don’t hedge (the
options are their hedge) and the market makers do. At least some of
this hedging is dynamic, and if the market drops toward their shorts,
the market impact of their hedging will increase volatility. The opposite
occurs if the market rallies toward their longs. In this sense the smile is a
self-fulﬁlling prophecy of the dependency of volatility on the level of the
underlying.
■In equity indexes the skew will be more pronounced than in the individual
stocks that make up the index. The volatility of an index, σ, is related to
the volatility of the components, σi, by
σ2 =
N

i=1
w2
i σ2
i + 2
N−1

i=1

j>1
wiwjρijσiσj
(5.9)
where
wi are the component weights
ρij are the correlations between the components
So we can see that there are two ways the index volatility can increase:
Either the component volatilities can increase or the correlations can
increase. Equation 5.9 is equally applicable to realized volatility and
correlation and to implied volatility and correlation. So the implied
volatility of an index also contains an implied correlation effect. Even
if all the components have ﬂat-implied volatility surface, the index can
exhibit a smile if correlation is expected to increase as the underlying
moves. And it is a generally held belief that correlation between stocks
increases in crashes or sharp downward moves.
■The actual underlying returns are not normally distributed; they exhibit
both skewness and kurtosis.
All but the last of these reasons are related to the buying (or selling)
pressure in the implied volatility market. This is difﬁcult to predict, but the
net effect tends to reach equilibrium in most markets. That is, the implied
volatility curve will take on a certain shape in a given product and then
basically keep that shape (Hafner and Wallmeier 2000; Cont and da Fonseca
2002).
--- page 100 ---

IMPLIED VOLATILITY DYNAMICS
84
We need a way to quantify the shape of the smile so that we can monitor
it for deviations from this equilibrium. At this point, we are not saying what
the skew should be. We are only saying what it typically is.
Before we get a little more technical, I would like to mention a simple
way to parameterize volatility smiles. This lets us compare smiles and is
useful as a quick way to do this across different expiries. It could also be
used to compare products of the same class, such as equity indexes or
government bonds. We parameterize the smile by the delta of the option,
and then divide all of the volatilities in a given month by the at-the-money
volatility of that month. This gives a curve that is remarkably constant
through time. I am not aware of any reason why this should be so—it could
well just be an artifact of how market makers have always propagated their
volatility smiles through time.
Table 5.3 shows the surprising effectiveness of this method using the
example of the QQQQ options. In fact, given the amount of interpolation
needed and the width of the bid/ask spread in volatility terms, one could
make the argument that in these terms all of the months had the same smile.
Not a bad start. However, this gives us no way to compare the implied
volatilities to any properties of the realized distribution.
We set up this problem in a way that is similar to our initial approach to
option pricing. We originally thought that options were only dependent on
the square of moves in the underlying, which leads us to price them based
on volatility. We did not think in terms of absolute moves in the stock price.
We used volatility because it would allow us to compare two underlyings
with very different prices. Now we know that volatility isn’t enough; our
process was misspeciﬁed. We need to extend the BSM methodology to
incorporate skewness and kurtosis.
TABLE 5.3
The Raw and Scaled Implied Volatilities of the QQQQ Options as a
Function of the Out-of-the-Money Delta from the Morning of
September 13, 2007
Delta
Oct. Raw
Vol.
Nov. Raw
Vol.
Dec. Raw
Vol.
Mar. Raw
Vol.
Oct. Scale
Vol.
Nov. Scale
Vol.
Dec. Scale
Vol.
Mar. Scale
Vol.
10
35.8
35.5
33.0
32.0
1.47
1.47
1.46
1.44
20
31.2
30.4
29.2
28.0
1.28
1.26
1.29
1.26
30
28.8
27.8
26.5
25.7
1.18
1.15
1.17
1.16
40
26.3
26.0
24.0
23.5
1.08
1.07
1.06
1.06
50
24.4
24.2
22.6
22.2
1.00
1.00
1.00
1.00
40
23.5
23.4
22.2
21.8
0.96
0.97
0.98
0.98
30
22.0
21.8
20.7
20.3
0.90
0.90
0.92
0.91
20
20.8
20.2
19.2
18.9
0.85
0.83
0.85
0.85
10
18.7
18.6
17.8
17.6
0.77
0.77
0.79
0.79
--- page 101 ---

IMPLIED VOLATILITY DYNAMICS
85
Skewness is deﬁned by the third moment about the mean, normalized by
the standard deviation.
µ3 =
1
N
N

i=1
(xi −x)3
σ3
(5.10)
This equation is similar in form to Equation 2.1a. If the distribution is
symmetric the skewness will be zero (so, in particular, a normal distribution
will have zero skewness). If the left tail of the distribution is more
pronounced than the right tail, the distribution has negative skewness. If
the opposite is true it has positive skewness. The variance of the skewness
measured from a sample with size N is given by
Var(µ3) ≈6
N
(5.11)
Kurtosis is deﬁned by the normalized fourth moment about the mean:
µ4 =
1
N
N

i=1
(xi −x)4
σ4
(5.12)
It is a measure of the degree of fat-tailedness of the distribution. The normal
distribution has a kurtosis of 3. Distributions with a kurtosis greater than 3
are called leptokurtic. This includes practically all distributions we encounter
in ﬁnance. Distributions with a kurtosis smaller than 3 are called platykurtic.
Because under this deﬁnition the normal distribution is 3, we sometimes
refer to excess kurtosis: kurtosis minus 3. Confusingly, some authors use this
as a deﬁnition of kurtosis. The Microsoft Excel function KURT actually
calculates excess kurtosis.
The variance of the kurtosis measured from a sample with size N is
given by
Var(µ4) ≈24
N
(5.13)
The ﬁrst attempt to include these moments in option pricing was by
Jarrow and Rudd (1982), who worked with the price distribution. They
perturb the lognormal price distribution and express the new price distribution as an expansion, using lognormal distributions as basis functions. This
will work, but unfortunately the higher moments of the price distribution
are not constant at different maturities, so we would have time-varying
parameters to keep track of. This is a mathematical artifact and would occur
even if the true distribution didn’t change at all.
--- page 102 ---

IMPLIED VOLATILITY DYNAMICS
86
A better solution was proposed by Corrado and Su (1996). They
performed an expansion (technically a Gram-Charlier expansion) of the
return distribution. This means that the parameters are time invariant (unless
the distribution really did change shape). The European call price is given by
C = CBSM + µ3Q3 + (µ4 −3)Q4
(5.14)
where
µ3 is the skewness of the returns
µ4 is the kurtosis
CBSM is the normal BSM call value
Q 3 = 1
6Sσ
√
T((2σ
√
T −d1)n(d1) + σ2TN(d1))
(5.15)
Q 4 = 1
24Sσ
√
T((d2
1 −1 −3σ
√
Td2)n(d1) + σ3√
T3N(d1))
(5.16)
where, as usual,
d1 =
ln
 S
X

+

r + σ2
2

T
σ√T
(5.17)
d2 = d1 −σ
√
T
(5.18)
N(x) =
1
√2π
x

−∞
exp
−z2
2

dz
(5.19)
is the cumulative normal distribution function and
n(x) =
1
√2π
exp
−x2
2

(5.20)
The put/call parity relationship can be used to ﬁnd the value of the put by
P = C −S + X exp(−rT)
(5.21)
Initially, we consider these parameters to be purely implied—that is,
they are only meaningful in the context of the option market and have no
direct relationship to the underlying return distribution. We use the quoted
option prices to back out the option parameters, but now we will not get
an implied volatility for each strike. We will get, from all the options of
a given expiry, an implied volatility, skewness, and kurtosis, reducing our
parameters from one per strike to just three.
To ﬁnd the implied skewness and kurtosis, we work directly from
Equation 5.4, searching for the parameters that minimized the squared
