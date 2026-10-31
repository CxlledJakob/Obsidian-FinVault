# Algorithmic Trading (Winning Strategies and Their Rationale) -- Chan, Ernest P_ -- 2013 may 22 -- John Wiley & Sons, Inc_ -- doi 10_1002_9781118676998 -- e374e4354dcd660c7bc666e0297a580b -- Anna’s Archive.pdf — Chapter 5: Chapter 5 (pages 138–143)

--- page 138 ---

126
ALGORITHMIC TRADING
Students of commodities markets know that seasonality is often a prominent feature. So you may fi nd that for a particular market, only calendar
spreads of certain months (and certain months apart) mean-revert. However, we won’t pursue these market-dependent details here.
We can try this same linear mean reversion strategy on the VX calendar
spreads. It turns out that Equation 5.7 works only for a future whose underlying is a traded asset, and VIX is not one. (If you scatter-plot the log VX
futures prices as a function of time-to-maturity as we did in Figure 5.4 for
CL, you will fi nd that they do not fall on a straight line.) Various researchers have suggested alternative formulae suitable for the VX future (see, for
example, Dupoyet, Daigler, and Chen, 2011), but I have found that none
can explain the mean-reverting property of VX calendar spreads in the face
Example 5.4 (Continued)
This results in an attractive unlevered APR of 8.3 percent and a
Sharpe ratio of 1.3 from January 2, 2008, to August 13, 2012. The
cumulative returns curve is shown in Figure 5.7.
FIGURE 5.7 Cumulative Returns of the Linear Mean Reversion Strategy
Applied on CL 12-Month Calendar Spread
--- page 139 ---

127
MEAN REVERSION OF CURRENCIES AND FUTURES
of the non-mean reversion of the VX future itself. So we can rely on only
our empirical observation that an ADF test on the ratio back/front of VX also
shows that it is stationary with a 99 percent probability. If we apply our usual
linear mean-reverting strategy using ratio as the signal (and with a 15-day
look-back for the moving average and standard deviations), VX yields an
APR of 17.7 percent and a Sharpe ratio of 1.5 from October 27, 2008, to
April 23, 2012 (see Figure 5.8 for a plot of its cumulative returns), though
it performed much more poorly prior to October 2008. In the next section,
I will present graphic evidence that there is a regime change in the behavior
of VIX and its futures around the time of the fi nancial crisis of 2008, so perhaps this abrupt change in the strategy performance is related to that as well.

■Futures Intermarket Spreads
As I stated in the introduction of this chapter, it is not easy to fi nd futures
intermarket spreads (i.e., pairs of futures from diff erent underlyings) that
are mean reverting. Nevertheless, let’s systematically round up some of the
usual suspects.
The most obvious candidate for pair trading futures is intermarket spreads
between markets that are closely related. For example, the energy complexes (WTI crude oil CL, Brent crude oil BZ, unleaded gasoline RB, and
heating oil HO, all traded on the New York Mercantile Exchange [NYMEX])
should off er rich potential opportunities.
FIGURE 5.8 Cumulative Returns of Linear Mean
Reversion Strategy on VX Calendar Spread
--- page 140 ---

128
ALGORITHMIC TRADING
Before we run a Johansen test on these four contracts, we can fi rst examine a well-known portfolio called the crack spread consisting of long three
contracts of CL, short two contracts of RB, and short one contract of HO.
This is called the crack spread because we can obtain gasoline and heating
oil by cracking the long hydrocarbon chains of crude oil molecules, and
the 3:2:1 hedge ratios come about because three barrels of CL produces
approximately two barrels of RB and one barrel of heating oil, though this
is not universally true for all refi ners. One advantage of trading the crack
spread is that NYMEX off ers a ready-made basket for it, with a much lower
margin requirement than if we trade them separately.
However, running an ADF test on the crack spread from May 20, 2002,
to May 4, 2012, shows that this spread is not mean reverting. The chart of
this spread (Figure 5.9) reveals a dramatic increase in value around March 9,
2007, to July 3, 2008, and then a sharp drop after that, and running the
linear mean reversion strategy on it shows negative returns for that period.
(Note that we must back-adjust the continuous contracts using prices rather
than returns in this test; otherwise, this price spread will show a discontinuous jump at rollovers, as explained in Chapter 1.)
Another spread that would seem to be a good candidate is CL and BZ in a
1:1 ratio. After all, their underlyings are both crude oils. But another quick
ADF test will show that it is far from stationary. BZ has relentlessly outperformed CL due to a variety of factors. The likely culprits include the increasing oil production in the United States (Friedman, 2012), the pipeline
bottleneck at Cushing, Oklahoma (Philips, 2012), and geopolitical concerns
FIGURE 5.9 The Crack Spread
--- page 141 ---

129
MEAN REVERSION OF CURRENCIES AND FUTURES
such as the embargo against Iranian oil in 2012, which aff ected Europe and
therefore BZ more than the United States.
If you want to backtest intermarket spreads yourself, don’t forget to
make sure that their prices are synchronous, as I cautioned in Chapter 1. In
particular, before BZ started trading at the NYMEX on September 5, 2001,
it was traded at the Intercontinental Petroleum Exchange in London, which
obviously has a diff erent closing time than NYMEX on which CL has always
been traded. So backtesting the BZ-CL spread before September 5, 2001,
using closing prices would be wrong. Also, we often need to multiply the
futures prices by a factor to convert points into USD.
Our search for mean-reverting intermarket futures spreads has not been
fruitful so far. But I will now discuss one unusual spread that will change that.
Volatility Futures versus Equity Index Futures
Many traders have observed that volatility is anti-correlated with the stock
equity market index: When the market goes down, volatility shoots up, and
to a lesser extent, vice versa. One way to visualize this inverse relationship is
to plot ES, the E-mini S&P 500 futures front-month prices, against VX, the
VIX futures front-month prices. This can be accomplished by the “scatter”
function in MATLAB, and the result is displayed in Figure 5.10.
The fi rst obvious feature of this plot is that, indeed, the stock index has an
inverse relationship with volatility. But, more interestingly, there appeared to
be two main regimes, 2004 to May 2008 and August 2008 to 2012. The second regime has a notably lower volatility for a given stock index level. In plain
FIGURE 5.10 A Study of Volatility Regimes: ES versus VX
--- page 142 ---

130
ALGORITHMIC TRADING
English, the market is less volatile nowadays. However, the range of volatilities is greater now, meaning that we have days with more extreme volatilities
than before. (There are other, shorter periods that may represent transitional
states, but we will ignore them in our analysis.) It would be a mistake to run
a linear regression or apply the Johansen test to a mixture of both regimes, so
we focus on the second one, which extends to the time of this writing.
We choose to compute the regression coeffi  cients only for the fi rst 500
days of the post–August 2008 data as the training set because later we would
like to use the various statistics from this regression to build our trading
model. Before we actually run the prices through the linear regression program, we have to remember that the futures prices of VX and ES are in different units: one point move in VX is $1,000, while one point move in ES is
$50. So we need to multiply the prices of VX by 1,000 and the prices of ES
by 50 in order for the hedge ratio to properly refl ect the ratio in the number
of contracts.
The linear relationship is shown in Equation 5.11.

ES × 50 = −0.3906 × VX × 1,000 + $77,150
(5.11)
where ES and VX are their re spective futures (settlement) prices. The standard deviation of the residues is $2,047. This means that a portfolio that is
long 0.3906 contracts of VX and long one contract of ES should be stationary,
as a plot (Figure 5.11) of this portfolio’s market value would convince us.
We can construct a Bollinger band–like mean-reverting strategy by shorting this portfolio whenever its value deviates from one standard deviation
FIGURE 5.11 Stationary Portfolio of ES and VX
--- page 143 ---

131
MEAN REVERSION OF CURRENCIES AND FUTURES
of the residuals determined in the training set. The APR on the test set July
29, 2010, to May 8, 2012, is 12.3 percent, with a Sharpe ratio of 1.4. It was
particularly profi table starting around the time of the Standard and Poor’s
downgrade of the U.S. credit rating. The cumulative returns curve is shown
in Figure 5.12.
There is a diff erent VX versus ES strategy that we can employ, which does
not rely on the mean-reverting properties of the spread VX-ES. Because that
is a momentum strategy, I will discuss it in the next chapter.
FIGURE 5.12 Cumulative Returns of VX-ES Mean
Reversion Strategy
• “Commodity” currencies as a group offer many opportunities for
cointegration.
• In computing the returns of a portfolio with two currency cross-rates, did
you pay attention to whether they have the same quote currency, the same
base currency, or neither? The formulae for computing returns are not the
same for all cases.
• Futures returns consist of two components: spot returns and roll returns.
• Backwardation means roll returns are positive, and far contracts are
cheaper than near contracts. Contango means roll returns are negative, and
far contracts are more expensive than near contracts.
• Because of roll returns, mean reversion of the spot price may not induce
mean reversion of the futures price.
• Mean reversion of futures calendar spreads of traded assets depends on
mean reversion of roll returns.
KEY POINTS
