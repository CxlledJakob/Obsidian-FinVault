# Volatility Trading_ Sinclair_Volatility Trading -- Euan Sinclair(auth_) -- Wiley Trading, 1, 2013 -- John Wiley & Sons, Incorporated -- isbn13 9781118347133 -- 2634a86bfed8248fa7ba3fb72595bbbc -- Anna’s Archive.pdf — Chapter 9: Trade Evaluation — C H A P T E R 1 2 (pages 235–242)

--- page 235 ---

223
C H A P T E R 1 2
The VIX
O
ur derivation of Black-Scholes-Merton (BSM) made certain assumptions about the behavior of the underlying. It is also possible, given
the options, to calculate a volatility that makes no such assumptions. This
is referred to as model-free implied volatility and forms the basis for the
pricing of variance swaps and the calculation of the VIX index.
Variance swaps were based on an idea by Carr and Madan (1998). They
used the entire cross-section of options, not just the at-the-money options,
of a given expiration to build a portfolio whose exposure to variance was
independent of the underlying price. The basic idea was further formalized
by Britten-Jones and Neuberger (2000) and extended by Jiang and Tian
(2005) to the case where the underlying paid dividends and the risk-free
rate is nonzero. They show that the asset return’s variance between two
times, T1 and T2 (in the risk-neutral world), is
E[VT1,T2] = 2
T
∞

0
C(T2, X exp(rT2)) −C(T1, X exp(rT1))
X2
dX
(12.1)
Or, if we consider the starting time to be the present, we can express
this in terms of the forward price, Ft, and only using out-of-the-money
options as
E[V01,T] = 2
T exp(rT)


F

0
P (T, X)
X2
dX +
∞

F
C(T, X)
X2
dX


(12.2)
Equations 12.1 and 12.2 actually give a model-free implied variance;
when we take the square root to get volatility we introduce an upward bias
by Jensen’s inequality.
Volatility Trading,   Second Edition.    Euan Sinclair
© 2013 Euan Sinclair. Published 2013 by John Wiley & Sons, Inc.
--- page 236 ---

THE VIX
224
■The VIX Index
The Volatility Index (VIX) was introduced by the Chicago Board Options
Exchange (CBOE) in 1993. It was designed to be a benchmark index for
equity market volatility. In 2003 the calculation methodology was changed
to give a model-independent forward-looking volatility index: the S&P 500
option market’s expected value of volatility over the next 30 days. It is a
discrete version of Equation 12.2 where the integral has been approximated
by a sum. As far as I know, the ﬁrst study of the discrete situation was by
Demeterﬁet al. (1999), who examined in some detail the effect of using a
ﬁnite number of strikes.
A comparison of the two methodologies for constructing the VIX is given
in Carr and Wu (2006). The derivation of the fair value for the VIX is
readily available (see, for example, www.cboe.com), and the index values
have been back-calculated to January 2, 1990.
The VIX is calculated from a weighted strip of options by the following
formulae:
σ2
VIX = 2
T
N

i=1
∆Xi
X2i
exp(rT)V(Xi) −1
T
 F
X0
−1
2
(12.3)
F = X0 + exp(rT)(C0 −P0)
(12.4)
∆Xi = Xi+1 + Xi−1
2
(12.5)
where
r is the risk free rate
T is the expiration time (which the CBOE calculates to the minute)
F is the forward price of the index
X0 is the strike price immediately below the forward price
Xi is the strike of the ith out-of-the-money option
V is the midprice of the corresponding option
Equations 12.3 to 12.5 are applied to the ﬁrst two option expirations, T1
and T2, and we then interpolate to ﬁnd a constant 30-day volatility:
VIX = 100

T1σ2
VIX1
NT2 −N30
NT2 −NT1

+ T2σ2
VIX2
N30 −NT1
NT2 −NT1
 N365
N30
(12.6)
where NT is the number of minutes remaining for the appropriate contract.
--- page 237 ---

THE VIX
225
The VIX index (also known as the cash VIX) is not a tradable asset. The
index can be instantaneously replicated but would need to be continuously
rebalanced both due to the need to stay at 30-day maturity and also because
of the concavity introduced by taking the square root. However, VIX futures
do trade and they offer a number of attractive ways to speculate on implied
volatility.
■VIX Futures
VIX futures were listed in March 2004 (followed by VIX options in 2006).
These settle to the cash value of the VIX. Because the VIX index cannot be
statically replicated the usual futures pricing relationship based on cash and
carry arbitrage does not hold. Instead, VIX futures need to be priced by
assuming a model for the future evolution of implied volatility. VIX futures
fair value calculations are model dependent.
Many such models have been proposed but there is no consensus
emerging. Further, even if we had a good model it might not be very useful
to most traders. The market prices of the futures don’t seem to oscillate
around the models’ predictions. We would ﬁnd ourselves putting on a trade
and waiting until expiration. Some hedge funds may operate like this, but
option-trading ﬁrms tend not to. Trading ﬁrms (and most option traders)
also tend to be suspicious of model-driven trades.
However, there are a number of trading opportunities that are not model
dependent. We look at some of these next.
VIX Basis as a Predictor of the Futures
Simon and Campasano (2012) present evidence that the futures can be
predicted by looking at the basis. That is, if the futures are trading over the
cash VIX the futures will tend to fall and if the futures are trading below the
cash VIX they will tend to rise. This is not what is predicted by the rational
expectations hypothesis. Rational expectations says that the futures prices
are unbiased predictors of the future value of the cash VIX. If this was true
the basis would have no predictive power.
The study looked at the VIX from 2006 until 2011. In this period, the
VIX averaged 23.7 and the front two futures averaged 23.8 and 24.4,
respectively. The high of the VIX was 81.1 and the low was 9.9. Because
volatility mean reverts the range, of the futures was smaller: The front
month had a range of 10.3 to 69.0. The front-month basis averaged 0.66
--- page 238 ---

THE VIX
226
(meaning the future price is higher than the cash by this amount), with a
low decile of −1.40 and a high decile of 2.01.
In general, when the VIX is high the futures curve will be downward
sloping and when the VIX is low the curve will slope upward. But this
phenomenon is far from universal. For example, when the VIX is below 20,
the futures curve was downward sloping 22 percent of the time and when
the VIX was between 40 and 50 the curve was upward sloping 46 percent
of the time. Such seemingly anomalous behavior can lead to some of the
best trading opportunities.
The basic basis trade is:
■If the front futures are above the cash and the expected daily convergence
is greater than 0.1 VIX points, we short a future.
■If the front futures are below the cash and the expected daily convergence
is greater than 0.1 VIX points, we buy a future.
■We hold the trade for ﬁve days.
The results are summarized in Table 12.1.
Most of the proﬁts come from realizing the expected roll. That is, the
futures coalesce to the cash index at the rate we expect.
As we discussed in Chapter 3, there is a strong negative correlation
between the changes in volatility and the returns of the S&P 500. So while
we are trying to collect the roll premium we will be exposed to some
substantial risk if the VIX moves, and the largest of these moves will be
driven by the movement in the stock index. Simon and Campasano (2012)
hedged this risk by buying S&P 500 futures if they were long VIX futures
and selling S&P 500 futures if they were short VIX futures. They estimated
the hedge ratio by regressing VIX returns on the index returns and the index
returns scaled by time until expiration. The results of the hedged trade are
shown in Table 12.2.
As we might expect, hedging slightly decreased the proﬁtability of
each trade but smoothed the results by increasing the winning percentage
(particularly for long trades).
TABLE 12.1
The Results of the VIX-Basis
Trade Strategy
Shorts
Longs
Mean PL
$656
$1,040
Winners/Losers
53/29
22/20
--- page 239 ---

THE VIX
227
TABLE 12.2
The Results of the Hedged
VIX-Basis Trade Strategy
Shorts
Longs
Mean PL
$539
$908
Winners/Losers
55/27
27/15
■Volatility ETNs
This term structure effect can also be traded through the volatility exchange
traded notes (ETNs), in particular the iPath shortand medium-term VIX
futures ETNs, VXX, and VXZ. As the VIX cannot be replicated, there are
no cash VIX ETNs. There are also no ETNs that directly track VIX futures,
as there is no feasible way for an ETN to mimic an expiring product.
The ﬁrst successful VIX-based ETN was the iPath VXX that was listed
in January 2009. The VXX replicates the short-term VIX futures index as
constructed by S&P 500. This consists of a rolling 30-day VIX future. Each
day we roll 1/30th of the front future and buy the next second future.
In February 2009 the VXZ was introduced. The VXZ is a similar product
based on the mid-term VIX futures (the fourth and seventh futures).
Each of these ETNs depends not only on the level of the VIX but also
the term structure of the futures. For example, if the second future is more
expensive than the ﬁrst then VXX loses to the rolling process. The VIX
futures term structure for June 1, 2011, is shown in Figure 12.1.
10
12
14
16
18
20
22
24
26
1
2
3
4
5
6
7
8
Months to Expiry
VIX Futures
FIGURE 12.1
The VIX Futures Term Structure for June 1, 2011
--- page 240 ---

THE VIX
228
Here, the front future is trading 17.9 and the second future is trading
19.5. So each day we lose (1/30) × 19.5 −17.9 = 0.05. Thus, contango
(an upward sloping term structure) leads to decay of VXX.
Very loosely speaking, VXX is a slightly damped, decaying VIX series:
The correlation to the VIX is generally greater than 90 percent but the
volatility of the VIX is generally 1.5 to 2 times larger than VXX. VXZ is
a more heavily damped series with the volatility of the VIX three to four
times greater.
The CBOE also lists a three-month implied volatility index, VXV. Apart
from the maturity of the options involved this is calculated in the same
way as the VIX. These two indices allow us to deﬁne a model free implied
volatility term structure (IVTS) as
IVTS = VIX
VXV
(12.7)
An IVTS of greater than one would indicate that the term structure was
downward sloping (and the futures would be in backwardation). According
to the results in Section 12.2, this would lead us to believe that the futures
would rally. Donninger (2011) used the calendar effect to construct a
proﬁtable dynamic strategy from VXX and VXZ.
The strategy consists of a portfolio of VXX and VXZ with weights
determined by the level of IVTS. These weights are shown in Table 12.3.
The weights for VXX are always negative. But this does not mean that
we are always bearish. Although the beta for VXZ as a function of VXX
returns is around 0.45 (the ratio of VXX to VXZ in the ‘‘neutral outlook’’
where IVTS is between 0.91 and 0.97) it also depends on the overall VIX
level. In the lowest two groups (where IVTS > 0.97) we actually expect
VIX to rise. This is reﬂected in our VXZ position and the short VXX is just
a hedge against a sharp decline.
Adjusting our portfolio on the close each day produced the equity curve
shown in Figure 12.2. We assume we start with $100 and continue to
reinvest all the money at our disposal. Total annualized return was 99
percent with a maximum drawdown of 12 percent. The Sharpe ratio was
TABLE 12.3
The Weights for the ETN Strategy
IVTS Level
VXX Weight
VXZ Weight
IVTS ≤0.91
−0.60
0.40
0.91 < IVTS ≤0.97
−0.32
0.68
0.97 < IVTS ≤1.05
−0.25
0.75
IVTS > 1.05
−0.10
0.90
--- page 241 ---

THE VIX
229
0
50
100
150
200
250
300
350
Portfolio Value
8/13/2010
9/15/2010
10/15/2010
11/16/2010
12/17/2010
1/20/2011
2/22/2011
3/24/2011
4/26/2011
5/26/2011
6/28/2011
7/29/2011
8/30/2011
9/30/2011
11/1/2011
12/2/2011
1/5/2012
2/7/2012
3/9/2012
4/11/2012
5/11/2012
6/13/2012
7/16/2012
8/15/2012
FIGURE 12.2
The Performance of the Dynamic VXX/VXZ Strategy from
Mid-August 2010 to Mid-August 2012
2.62. This portfolio outperformed the simple benchmark of shorting VXX.
This would have worked as VXX declined (after accounting for splits) from
95.12 to 11.51, but the Sharpe ratio was 1.5 and we suffered through a
bad drawdown when VXX rallied from 20.11 on July 7, 2011, to 56.84 on
October 3, 2011.
■Other VIX Trades
Another way to monetize the VIX term structure is to trade calendar put
spreads. When the futures are in contango, we buy the front-month ATM
VIX put and sell an equal dollar amount of the second-month put with the
same strike. As the futures fall toward the cash value our long put will
increase in value more than our short loses due to its higher gamma. In the
event of a spike in the VIX, both puts will expire worthless. From 2009
to the end of 2011, this strategy had an average annualized return of 15.2
percent with a Sharpe ratio of 1.2. The largest drawdown was 18 percent.
A separate source of edge is the VIX variance premium. Implied volatility
for the VIX is consistently above the subsequent realized volatility. Barnea
and Hogan (2012) used synthetically constructed variance swaps to show
that this premium averaged 3.26 percent during the period from October
2006 to November 2010. We could use this fact directly and short VIX
straddles or strangles. This gives a similar risk/return proﬁle to shorting
equity index variance that we discussed in Chapter 11. Alternatively, we
--- page 242 ---

THE VIX
230
could combine this fact with the basis effect and implement a short futures
position through a short vega option position. An example would be to buy
one by two put spreads. This will get us short variance and short directionally
unless there is a downward spike in the VIX level, which is unlikely at all
times and particularly so when the futures are low and in contango.
■Summary
The VIX is a model-free implied volatility index. It cannot be traded directly
but there are a number of traded instruments based on the index. These can
often be used to trade the features of implied volatility we have explored in
earlier chapters.
■The VIX basis has the ability to predict future’s movement.
■This effect can also be traded through ETNs or options.
■VIX options’ implied volatilities tends to be higher than the subsequent
realized volatility.
