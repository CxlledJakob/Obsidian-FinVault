# Volatility Trading_ Sinclair_Volatility Trading -- Euan Sinclair(auth_) -- Wiley Trading, 1, 2013 -- John Wiley & Sons, Incorporated -- isbn13 9781118347133 -- 2634a86bfed8248fa7ba3fb72595bbbc -- Anna’s Archive.pdf — Chapter 6: Hedging (pages 108–127)

--- page 108 ---

93
C H A P T E R 6
Hedging
W
e saw in Chapter 1 that the idea of hedging is central to the Black-
Scholes-Merton (BSM) framework. The concept of hedging was
used in the derivation of the BSM equation and it is necessary to hedge to
remove exposure to the return of the underlying. To isolate our volatility
exposure we need to hedge. Professional option traders are well aware of
this. However, the actual process of hedging causes confusion and is subject
to several misconceptions.
There is an old saying that any option trade can be proﬁtable if only it
is hedged correctly. If hedging is thought of as part of the option trading
process, and not as a completely unrelated trading strategy, this is simply
untrue. Although it is possible that some traders have a special ability to
trade the underlying, this is not even the point of hedging. Hedging is about
mitigating risk so that we can proﬁt from our prediction of volatility. On
average, a trade will not make money unless we sell implied volatility higher
than realized volatility or we buy implied volatility lower than realized
volatility. Due to the dispersion of trade outcomes around this outcome,
enough trades that were based on an incorrect volatility prediction will
be winners to keep some traders convinced that this is not true. That is
okay. They are wrong—and in a zero sum game, having some participants
mistaken about a fundamental aspect of trading can only help the rest of us.
Even if traders can proﬁtably trade both volatility and the direction
of the underlying, they should not forget that these will now be two
separate strategies: Volatility trading is not dependent on the ability to trade
directionally. Further, even the best directional traders will not always have
a view on the underlying, while an option trader always needs a hedging
plan. In this chapter, we devise such a plan.
If we could trade the underlying in any size we wanted and without
incurring any costs, we should do so and continuously adjust our stock
Volatility Trading,   Second Edition.    Euan Sinclair
© 2013 Euan Sinclair. Published 2013 by John Wiley & Sons, Inc.
--- page 109 ---

HEDGING
94
position to remain delta-neutral. As we saw in Chapter 1, this would make
our proﬁt a function of the difference between the implied volatility and
the realized volatility. However, in the real world we can only trade in
discrete size, and each trade costs us money in commissions and bid/ask
spreads. This makes continuously adjusting delta impractical.
There are proofs that rely on mathematical properties of geometric
Brownian motion (GBM) to show that the continuous replication demanded
by the BSM model incurs inﬁnite transaction costs over any time period,
no matter how small. But there is a further problem: When the underlying
has a discrete bid/ask spread we can never actually have a ﬂat delta position
anyway. Our gamma will cause us to have different deltas when valued
against the bid or the offer. So in this case our delta will change even when
the underlying isn’t going anywhere. Hedging this bid/ask bounce would
incur costs while removing no risk.
It is hard to overstate the importance of hedging cheaply and efﬁciently.
Replication risks due to imperfect hedging can easily exceed the anticipated
proﬁts from the perceived implied volatility mispricing. Transaction costs
from hedging can be large. They are also easy to ignore, as they accumulate
progressively over the lifetime of the trade and are not easily perceived by
traders, who tend to become focused on short-term results.
To see the extent of the issue, consider the following example. We are
short 1,000 vega of at-the-money options on a stock initially priced at $100,
which have one year until expiry. Actual volatility is 40 percent and we
sold the position at an implied volatility of 50 percent. Before any costs,
we expect to make a proﬁt of $10,000 if we hold it until expiry. However,
the bid/ask spread in the underlying is $0.1. Table 6.1 shows the total
expected proﬁt for this position if we hedge to a delta-neutral position at
various frequencies. (These numbers were the results of a Monte Carlo
simulation of this situation, where we looked at the average result of 10,000
realizations of this situation.)
TABLE 6.1
The Average Proﬁt Realized When Rebalancing
Hedges at Different Intervals (in a perfect BSM
world, we would make $10,000)
Hedge Frequency
Average Realized
Proﬁt ($)
Weekly hedge
9,791
Daily hedge
9,220
Twice daily
8,830
Five times daily
7,952
--- page 110 ---

HEDGING
95
■Ad Hoc Hedging Methods
Traders use a number of different methods for deciding when to rebalance
their hedge. Long after option pricing was considered a science, hedging
was still thought of as an art and as a result early hedging theories were
somewhat ad hoc.
Hedging at Regular Intervals
One of the simplest hedging strategies is to hedge at ﬁxed time intervals.
At the end of each time period we execute an underlying trade that sets
our delta to zero (or as close to it as possible after allowing for discrete
trading units). This practice is sometimes employed by large facilitation
desks that may have option positions in several hundred underlyings. At the
end of each day the delta for each underlying is ﬂattened. This is simple to
understand and implement, but it is totally arbitrary in the choice of time
interval. Obviously, hedging more often decreases risk. Equally obviously,
hedging less often decreases costs. It should also be clear that a one-week
option should be hedged differently from a one-year option. A day in the
life of a one-week option is far more signiﬁcant than a day in the life of a
one-year option.
Hedging to a Delta Band
This is a strategy commonly used by market makers or traders who trade
only a few products. Here we choose a ﬁxed delta that we are able to
tolerate. When our delta exceeds this, we hedge.
We need to somehow choose the size of the band. Generally this is
done by considering the dollar risk we are exposed to by an unhedgeable
gap move in the underlying, such as an opening price jump. This could
also depend on the sign of the gamma in the portfolio. We may decide to
be looser in our hedging if we are long because an adverse move will be
partially insured by the gamma. Having to make this choice isn’t necessarily
a problem—we will see that such choices are inevitable. The problem is
that the choice should be dependent on the option position rather than
ﬁxed. This method relies on ad hoc adjustments to achieve this.
Hedging Based on Underlying Price Changes
When using this strategy the trader rebalances the delta after the underlying
has moved by a certain amount. This is based on the sensible idea that the risk
--- page 111 ---

HEDGING
96
in the portfolio is due to underlying moves, so these should form the basis
for rebalancing decisions. However, we are still left searching for a method
that tells us how to choose the appropriate price change. Traders also need
to decide whether to calibrate the method based on percentage changes,
dollar changes, technical levels of importance, or implied or historical
standard deviations.
■Utility-Based Methods
We know that hedging is a trade-off between reducing risk and incurring
costs. When economists deal with such compromises, they often turn to
the concept of utility. This gives us the necessary framework for deciding
between different alternatives.
Utility Theory
Imagine that you are given a choice between receiving a certain amount
of money or taking a bet that has a 50 percent chance of winning
$100 and a 50 percent chance of winning nothing. Clearly the bet
has an expected value of $50. If you would rather receive a certain
payoff of less than $50, you are risk-averse. If you would take $50
you are risk-neutral. If you would only accept more than $50, you are
risk-seeking.
The certain amount that you would settle for is the called the
certainty equivalent. If we plot a graph of certainty equivalent as a
function of the bet size we can visualize our utility function. For a
risk-averse trader, the utility curve will have downward curvature.
This means that the utility of a given amount of money is greater than
the amount of money itself. This can be seen in Figure 6.1. Conversely,
the utility function for a risk-seeking trader curves upward. The utility
of a given amount of money is less than the amount of money itself.
Such a utility curve is shown in Figure 6.2.
The two most important aspects of (sensible) utility functions for a
trader are that they slope up because we prefer more money to less,
and they curve downward because we become more risk-averse when
larger amounts are involved.
--- page 112 ---

HEDGING
97
Money
Utility
FIGURE 6.1
The Utility Function for a Risk-Averse Trader
Money
Utility
FIGURE 6.2
The Utility Function for a Risk-Seeking Trader
We can quantify our risk aversion by using the Arrow-Pratt absolute
risk aversion, which is deﬁned by
r = U′′(W)
U′(W)
(6.1)
A commonly used utility function is the exponential utility function.
It has the functional form
U(W) = −exp(−γW)
(6.2)
--- page 113 ---

HEDGING
98
It is unique in having constant absolute risk aversion as r = γ is
independent of the wealth, W.
Let’slookatanexampletoseehowwewouldﬁndourrisktolerance.
We do this by asking questions about the certainty equivalents of risky
outcomes that are normally distributed.
Suppose the distribution of future wealth has a mean µ and a
standard deviation σ. For example, µ = $10,000 and σ = $2,000.
So
E[U] = E[−exp(−γW)]
(6.3)
≈−exp

−γ

µ −1
2γσ2

(6.4)
So the certainty equivalent, W0, is given by
W0 = µ −1
2γσ2
(6.5)
This can be inverted to give an expression for the risk aversion, λ.
γ = 2(µ −W0)
σ2
(6.6)
Now suppose that the trader is indifferent between this distribution
of wealth and a certain outcome of $8,000; that is, W0 = $8,000.
Here
γ = 2(10,000 −8,000)
2,000 · 2,000
= 0.001
We can go through this process for various wealth levels and various
distributions. Quite a large amount of variability tends to be found.
Real traders tend to exhibit little consistency in their risk appetites,
either through time or as a function of the amount of the money
at stake. Many behavioral ﬁnance studies directly address this point
(Kahneman and Tversky 1979; Barberis, Huang, and Santos 2001).
For this and other reasons, the use of utility functions in economics
has been subject to criticism (Mirowski 1989; McCauley 2004). This
needn’t overly concern us. As with our use of the BSM model, utility
is just a framework for us to think within. Although traders may never
speciﬁcally know their utility function and although their risk aversion
may change, it isn’t unreasonable to state that they prefer more to less
and are risk-averse. This is all we really need.
--- page 114 ---

HEDGING
99
Hodges and Neuberger (1989) recognized that as BSM really prices the
replication strategy rather than the option directly, they could do the same
thing but also incorporate transaction costs. Actually, including transaction
costs was ﬁrst done by Leland (1985) but, while his results led to pricing the
option with a modiﬁed volatility to allow for the costs of hedging, we still
need to continuously adjust the hedge. So this doesn’t address the practical
problem of when best to hedge.
The most important idea in Hodges and Neuberger’s paper is that there
comes a point where the option trader is indifferent (in the utility sense)
to holding the risk associated with the mis-hedged option and the cost
associated with hedging it. If we can specify our level of risk aversion, this
strategy is optimal. They formulated the problem in terms of maximizing
the exponential utility function, but it was subsequently proved (Davis,
Panas, and Zariphopoulou 1993; Andersen and Damgaard 1999) that the
results are basically independent of the precise form of the utility function.
As mentioned in the accompanying box on utility, we would be justiﬁed in
being suspicious of any result that didn’t have this property.
The mathematics required to formulate the problem are beyond the scope
of this book. Sadly, the resulting valuation equation has no analytic solution
and needs to be solved numerically. Even this is not easy. The required
computations are prohibitively time consuming. There is no practical way
to use the Hodges-Neuberger (HN) methodology as a real-time hedging
guide.
But because it is the optimal solution, its properties are important to
understand. Figures 6.3 and 6.4 show the hedging bandwidth for a long-call
position and a short-call position. When our position’s delta moves outside
0
0.1
0.2
0.3
0.4
0.5
0.6
0.7
0.8
0.9
1
0
0.2
0.1
0.3
0.5
0.7
0.9
0.4
0.6
0.8
1
Call Delta
Bands
FIGURE 6.3
Optimal Hedging Bands for the Long-Call Option as Functions of the
BSM Delta (Dashed Line)
--- page 115 ---

HEDGING
100
0
0.1
0.2
0.3
0.4
0.5
0.6
0.7
0.8
0.9
1
0
0.2
0.1
0.3
0.5
0.7
0.9
0.4
0.6
0.8
1
Call Delta
Bands
FIGURE 6.4
Optimal Hedging Bands for the Short-Call Option as Functions of the
BSM Delta (Dashed Line)
the band, we hedge to bring our delta back to the edge of the band. (This is
only true if we assume that the counterparty in an option trade has no ability
to predict the direction of the underlying. There is some evidence that
option customers are partially informed. In this case we should immediately
hedge the delta of any new option trade to the BSM delta. However,
subsequent delta rehedging would follow the HN scheme and we would
only hedge if we moved outside the bands. It probably wouldn’t be wise
to overhedge the original trade to achieve the same directional risk as the
counterparty, unless you had a clear idea of the magnitude and duration
of the customer’s directional trading ability. This would require extensive
analysis.) The parameters chosen are not particularly realistic but have been
chosen to exaggerate the properties of the solution. We chose the case of a
one-year option with volatility of 0.3, transaction costs of 2 percent, zero
interest and carry rates, and a risk aversion of one.
Several points are immediately obvious. First of all, the short and long
positions need to be hedged differently. The band for the short position is
narrower. So we hedge our short positions more defensively. We have time
decay on our side so we take less chance with delta, whereas when we are
hedging long positions we need to let our deltas run. Interestingly, this is in
accordance with trader folklore.
Another way to see why this should be is to note that the hedger of a long
position sees a different level of volatility than that seen by the hedger of a
short position. As the underlying reaches a new high, short gamma hedgers
will be inclined to buy. In doing so, they will make the high even higher by
paying the offer. In contrast, a seller sells at the bid, slightly lower than the
--- page 116 ---

HEDGING
101
high. The cumulative effect of crossing bid/ask like this means that the long
and short positions have different volatility levels to contend with.
This was also the central result of Leland’s. He showed that the adjusted
volatility for a long option position was
σ = σ

1 −λ
σ

8
π∆t
(6.7)
where λ is the proportional transaction cost
∆t is the time between rebalancing
For a short option position, the adjusted volatility is
σ = σ

1 + λ
σ

8
π∆t
(6.8)
Although we do not explicitly use Leland’s results to determine our
hedging strategy, these are important results. Before doing any option
trade, we need to be aware approximately how much edge will be eroded
by cumulative delta hedging. This effect can be considerable, particularly
for low-volatility, illiquid stocks. For example, if fair volatility is 10 percent
and the bid/ask spread is 1 percent, an option that is rehedged daily would
need to be sold at an implied volatility of more than 15.9 percent to account
for this.
Additionally, the optimal delta band does not span the BSM delta. A
perfectly hedged portfolio in the BSM world may need to be adjusted
when transaction costs are present. This is also consistent with Leland’s
observation because if an out-of-the-money call sees a higher volatility, due
to the dependency of the option’s delta on volatility, it acts like it has a
higher delta. Similarly, an in-the-money option acts like it has a lower delta.
This causes the hedging band to be centered around an S-shape modiﬁed
delta, rather than the BSM delta.
The preceding analysis was done for European options, but the general
idea can be extended to cover U.S. options. This is similar to the BSM
model, where the partial differential equation is general but the methods
used to solve it are dependent on the exact boundary conditions. This caveat
also applies to the other models we look at. We can normally expect the
results for U.S. options to be similar to those obtained for European options
(in most cases U.S. options can be thought of as European).
Not evident from Figures 6.3 and 6.4, but the essential feature of
the model, is that the width of the hedging band is dependent on the
risk aversion. A large risk-aversion parameter means that traders want to
--- page 117 ---

HEDGING
102
accept little risk. So theywant tight hedging bands and will hedge often.
Conversely, a trader with a small risk-aversion parameter will be prepared
to hedge less frequently, accepting risk to reduce hedging costs. Neither of
these choices is more correct than the other. As with all hedging methods,
we need to decide how risk-averse we are. But given this choice, the HN
formalism gives us the optimal balance between risk and reward.
The Asymptotic Solution of Whalley
and Wilmott
If we assume that the transaction costs are small (relative to the value of
the option in the BSM world), it is possible to derive some approximate
solutions to the full problem. This was ﬁrst done by Whalley and Wilmott
(1993, 1994). They show that the boundaries of the no-transaction regions
are given by
∆= ∂V
∂S ±
3
2
exp (−r (T −t)) λS2
γ
 1
3
(6.9)
where λ is the proportional transaction cost—that is, transaction costs are
of the form
tc = λ|N|S
(6.10)
where N is the total number of shares traded.
Although the authors considered the case of hedging a short position in a
European call option, the method is far more general: It can be applied to
the hedging of general portfolios. The solution has a number of pleasingly
sensible aspects. An example of the resulting hedging bands is shown in
Figure 6.5. This was for the case of a one-year option with volatility of
0.3, transaction costs of 2 percent, zero interest and carry rates, and a risk
aversion of one.
■As transaction costs decrease, the hedging bandwidth decreases. Indeed,
as costs go to zero, the BSM delta is recovered.
■As risk aversion increases, the hedging bandwidth decreases, as in the full
HN theory.
■The strategy can be reduced to an analytical formula, which makes
implementing it in Excel feasible.
■The method can also deal with transaction costs with different structures.
In particular it can handle transaction costs proportional to the number
--- page 118 ---

HEDGING
103
0
0.1
0.2
0.3
0.4
0.5
0.6
0.7
0.8
0.9
1
0
0.2
0.1
0.3
0.5
0.7
0.9
0.4
0.6
0.8
1
Call Delta
Bands
FIGURE 6.5
The Approximate Hedging Bands from the Whalley and Wilmott
Asymptotic Method as Functions of the BSM Delta
of shares, as opposed to being proportional to the value of the shares
as in Equation 6.10. Ticket charges and brokerage are examples of such
costs. And it is a matter of some debate whether the bid/ask spread (the
dominant cost) should be modeled this way. We address this later in
this chapter. The model can also accommodate the generally unrealistic
situation where the costs are a single ﬁxed charge. This might be the case
if there is a high trade cost that is set irrespective of the size of the trade.
This would possibly impact a retail customer but will not be relevant to
even a semiprofessional.
The Whalley and Wilmott (WW) method also has some unfortunate
aspects:
■The asymmetry of longand short-gamma positions that came out of the
full HN solution is lost. Only the magnitude of gamma is relevant to the
asymptotic solution.
■The hedging band is now centered on the BSM delta, losing another
feature of the full HN solution.
A problem can arise in practice. If traders see an underlying get choppy
or start whipping around, it isn’t always obvious whether they should adjust
the bid/ask spread or increase the volatility. To the trader these have the
same primary impact: They both make hedging more difﬁcult. However, the
effect in these models (HN and WW) is very different. For an at-the-money
option, increasing the volatility will lower the gamma, which leads to a
tighter hedging band. But increasing the bid/ask spread (the proportional
--- page 119 ---

HEDGING
104
transaction cost) leads to a wider hedging band. How do we deal with this
important practical issue? The discrepancy is caused by the fact that these
models explicitly incorporate risk aversion. Volatility is a traded quantity.
It contains both risk and reward. When volatility is high these models tell us
to fear the worst and hedge often. But the bid/ask spread is purely a cost.
It has no rewarding aspects. If the bid/ask spread is wide, the models tell
us to hold off hedging to avoid multiple whipsaw losses.1 The trader needs
to consider this and think carefully about what aspect of the market is really
changing. Volatility isn’t the same as transaction costs at all (even a perfect,
frictionless market has volatility), but they can look the same at ﬁrst glance.
Although it is not really feasible in many market situations, it is possible
to separately and statistically estimate transaction costs and volatility.
Transaction costs can be estimated by keeping track of the difference
between our execution price and the previous trade. It is completely
a microstructure issue (although what constitutes microstructure can vary
between traders; Fidelity will have a very different view of transaction costs
than a market maker standing in the crude oil pit at the NYMEX). Volatility
can be estimated by using a time period that includes a large number of
trades of a size relevant to the particular trader.
Just as with the BSM model, these hedging schemes should not be
thought of as true models of reality. They just give a consistent and
systematic framework for dealing with the world. This particular issue
emphasizes this fact.
The Double Asymptotic Method
of Zakamouline
The two relatively simple transaction cost models are those of Leland and
Whalley and Wilmott. They can both be viewed as special cases of the
Hodges and Neuberger model: Leland describes how to replicate an option
in the presence of transaction costs when we are risk-neutral; Whalley and
Wilmott incorporate risk aversion but insist on the costs being small.
Although these models are simple to apply and use, and will almost
certainly be an improvement over more ad hoc methods, they lose some of
theappealingaspectsofthefullHNmodel.Morecrucially,carefulnumerical
simulations show that the approximations can signiﬁcantly underperform
the full strategy—in other words, for a given level of transaction costs, a
1This helpful explanation is from Johnny at www.nuclearphynance.com.
--- page 120 ---

HEDGING
105
portfolio hedged with the WW model will experience more variance than
one hedged according to the HN model. (This isn’t really a criticism. It
should be obvious that an approximation won’t perform as well as the full
model.)
Zakamouline (2006a, 2006b, and 2006c) examined the stylized facts of
the nature of the utility-based hedging strategies (essentially the bullet points
in the preceding section) and proposed a functional form for a hedging
strategy that preserved the most important features; this was also proposed
independently by Risher (2004). The hedging bands take the form
∆= ∂V(σm)
∂S
± (H1 + H0)
(6.11)
Immediately we can see that instead of being centered on the BSM delta,
it is based on the BSM delta evaluated at the modiﬁed volatility, σm.
σ2
m = σ2(1 −K)
(6.12)
H1 will be a gamma-dependent term, similar in effect to that in the WW
model. The exact numerical solution of the HN model shows that even
for very far out-of-the-money options (with practically no gamma), the
width of the hedging band does not go to zero. This feature is not captured
by the WW model. This means that we need to introduce the H0 term.
Zakamouline postulated the functional form of the solution and then used
numerical analysis to ﬁt the parameters. The results were
H0 =
λ
γSσ2T
(6.13)
H1 = 1.12λ0.31T0.05
exp (−rT)
σ
0.25||
γ
0.5
(6.14)
K = −4.76λ0.78
T0.02
exp (−rT)
σ
0.25
(γS2||)0.15
(6.15)
An example of the resulting hedging bands is shown in Figures 6.6 and
6.7. These were for the case of a one-year option with volatility of 0.3,
transaction costs of 2 percent, zero interest and carry rates, and a risk
aversion of one.
As can be seen from Figures 6.6 and 6.7, Zakamouline’s method gives
results that look much closer to the HN result than those of WW. In
particular the middle of the no-transaction region does not coincide with
the BSM delta. This comes about from using a modiﬁed hedging volatility.
Before we can compare the various strategies, we need some sort of
common benchmark. The strategies don’t all do the same thing. Some
--- page 121 ---

HEDGING
106
−0.2
0
0.2
0.4
0.6
0.8
1
1.2
0
0.2
0.4
0.6
0.8
1
1.2
Call Delta
Bands
FIGURE 6.6
Approximate Long-Call Hedging Bands from the Zakamouline
Asymptotic Method as Functions of the BSM Delta
0
0.1
0.2
0.3
0.4
0.5
0.6
0.7
0.8
0.9
1
0
0.2
0.1
0.3
0.5
0.7
0.9
0.4
0.6
0.8
1
Call Delta
Bands
FIGURE 6.7
Approximate Short-Call Hedging Bands from the Zakamouline
Asymptotic Method as Functions of the BSM Delta
are based on time increments and some are based on price moves. For
example, consider the regular time interval rebalancing method. First we
choose a time period; then we perform a simulation and compute the risk
and return of the strategy. Then we vary the time interval and repeat the
process. Eventually we will obtain an efﬁcient frontier for the strategy. We
do this for each strategy and compare the frontiers. This lets us ﬁnd the best
strategy (in return terms) for a given level of risk. For return we choose the
replication error: the total effect of all of the transaction costs. For risk we
choose the variance of the replication error. This means we evaluate risk in
the familiar mean-variance framework, but other risk measures are certainly
valid (refer to Chapter 9 for a discussion of the strengths and drawbacks of
some of these measures).
--- page 122 ---

HEDGING
107
Simulations of this type were carried out by Zakamouline (2005, 2006b)
and Martellini and Priaulet (2002). Zakamouline simulated the hedging
of a short position in a one-year call option. The time hedging intervals
varied from 1.25 (trading) days to 50 days. The parameters of the other
models were chosen so that the ﬁnal results were all in a similar part of
the mean-variance surface. (This is similar to how a trader would use the
models. He would calibrate a new hedging model by saying, ‘‘Currently my
hedging strategy leaves me with X amount of risk. If I have the new model
leave me with the same amount of risk, how much money do I save?’’)
Numerical simulations show that Zakamouline’s approximation clearly
dominates the others. By this we mean that for a given level of risk, the
strategy costs the least to implement. Ideally, we would like one strategy to
dominate for all levels of risk. This doesn’t completely happen. The relative
quality of the different strategies is dependent on the level of risk aversion
and the level of transaction costs.
A further consideration when choosing a hedging strategy is that not
all are equally easy to implement. The Hodges-Neuberger scheme is at
one extreme in that it is the optimal solution but practically impossible
to use. The Zakamouline scheme is a better approximation to this ideal
than is the Whalley-Wilmott method, but it is also more difﬁcult to use in
practice as some trading software doesn’t easily facilitate its implementation
(in particular, the change in delta with respect to volatility is not calculated
by all systems).
Another complication is that an option position will often have a gamma
proﬁle that changes sign as a function of the underlying. For example,
consider the long butterﬂy position consisting of long a 90 percent call,
short two 100-percent calls, and long one 110-percent call. This has the
payoff shown in Figure 6.8.
Imagine that we managed to somehow enter this position for zero cost.
We are now in the fantastic situation of having a position that can only make
money—but only if we do not continuously hedge it! If the underlying
ﬂuctuates between the 90 percent and 110 percent strikes, we will always
be short gamma, and if we hedge the deltas that we accumulate, buying
high and selling low, we can easily lose money. This example should tell us
two important things. First, the dynamic hedging strategy needs to take the
global gamma proﬁle into account. Second, if we can cheaply work into a
static hedge with other options, this is vastly preferable to dynamic hedging
with the underlying.
There is a more important point that needs to be made here. As we
emphasize throughout this book, it is vital to ﬁgure out exactly what one
--- page 123 ---

HEDGING
108
Long Butterfly
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
FIGURE 6.8
The Payoff of a Butterﬂy Spread as a Function of Moneyness
is trying to achieve at any point in the trading process. Speciﬁcally, what is
the point of hedging? Superﬁcially it is to remove exposure to the direction
of the underlying market. More generally it is to remove exposure to risks
we do not wish to accept while keeping exposure to those we do. If we
are market-making options, our edge comes from collecting the bid/ask
spread. To keep as much of this as possible, we should hedge as much of
our volatility exposure as we can by trading other options (preferably by
collecting the spread on these as well). This is covered as a practical problem
in Baird (1992) and Taleb (1997) and in a more formal setting by Carr, Ellis,
and Gupta (1998) and Hua and Wilmott (1999). However, if we explicitly
set out to take a position on the spread between realized and implied
volatilities, then this will generally not be possible. Dynamic hedging can
still leave many risks, but sometimes we actually want to take that risk on.
This is not a problem to approach in too dogmatic a manner. It needs to
be understood and mitigated to some degree and accepted to some degree.
The basic ways to deal with the problem can be summarized as follows:
■Inoculate your volatility bet from the effect of jumps by buying options in
the wings if you are short at-the-money options. (If you are long options,
you want exposure to jumps.)
■Try to diversify jump risk across products.
■Size each position to limit total losses.
■Don’t base your evaluation of the worst thing that could happen on the
worst thing that has happened in the past. If you are selling volatility,
--- page 124 ---

HEDGING
109
part of your premium exists because you are selling insurance premium
for events that have never happened before.
■Estimation of Transaction Costs
The ﬁxed components of trading costs for any underlying trade are trivial to
ﬁgure out. They consist of any brokerage, exchange, and clearing fees. More
difﬁcult are the proportional transaction costs, which are heavily dominated
by the bid/ask spread. If we are trading small enough, this will be equal to
half the quoted bid/ask spread. This is likely to be the case for individual
traders trading interest rate products or indexes. However, we will always
reach a size where the market impact of the trade will signiﬁcantly alter the
price we receive from the one that we saw quoted when we ﬁrst started
to hedge.
Generally, market depth looks something like that shown in Table 6.2
and Figure 6.9, where there is something like a V-shape distribution for
the cumulative size of bids and offers as a function of distance from the
current price.
But what we actually see at any time in the order book is unlikely to be
the actual total share quantity that we could trade. For example, we see
that if we went to the market to buy 1,000 Merrill Lynch shares we would
be ﬁlled at an average of 75.475 (200 at 75.44, 500 at 75.45, and 300 at
75.54) but in reality we would often be ﬁlled better, for two reasons. First,
we are only seeing resting limit orders in the book. If we were to split our
order into smaller blocks and execute these separately, our buying would
be likely to induce new selling orders to enter the market (in theory, that is
what a specialist is supposed to do). But of increasing relevance is the issue
TABLE 6.2
Market Depth for Merrill Lynch (MER) at 9:13 CST
on August 24, 2007
Bid Size
Bid Price
Offer Price
Offer Size
200
75.42
75.44
200
3,000
75.40
75.45
500
200
75.38
75.54
500
900
75.31
75.81
10,000
100
75.27
75.82
900
500
75.12
75.99
1,300
100
75.00
76.10
1,000
1,100
74.50
76.42
900
100
73.66
77.47
100
--- page 125 ---

HEDGING
110
0
2,000
4,000
6,000
8,000
10,000
12,000
14,000
16,000
18,000
73
73.5
74
74.5
75
75.5
76
76.5
77
77.5
78
Cumulative Volume
Price
FIGURE 6.9
The Cumulative Number of Shares Available as a Function of Price
of dark liquidity.2 There are a number of algorithms, formerly the preserve
of fairly sophisticated algorithmic trading hedge funds but now available to
most institutional traders, that won’t show the entire trade to the market
at once. A simple example is the iceberg order. Say we want to buy 1,000
Merrill Lynch. An iceberg might buy the 700 offered up to 75.44 and then
bid 75.44 on 100. If we are ﬁlled on this bid, the system automatically bids
75.44 for another 100 until our total order is ﬁlled. This type of order is
named iceberg because at any point we only see the tip of the order, most of
it remaining hidden.
So we need to estimate market impact transaction costs as a function of
order size. Just looking at the current market is not enough. Similar to the
Heisenberg Uncertainty Principle in quantum physics, our interaction with
the market changes the market. We need a fairly robust way of measuring
the effect of this interaction. This problem is one that is still an active area
of research in market microstructure, but we will present a simple yet
powerful model that captures many aspects of the situation, is easy to use,
and is a good starting point for any further research. This form of market
impact analysis was ﬁrst proposed at Merrill Lynch (Gatheral 2001).
As is fairly obvious to anyone with any experience at all in markets, trades
do not occur at constant intervals. To simplify the mathematics, let’s assume
we can make a change of timescale so that they do occur at equal intervals
(this transformation will never be knowable in reality, but conceptually we
can make a change to this new time—trading time). Now the number of
2This originally referred to the internal crossing of trades by large ﬁnancial institutions,
but has since had its meaning extended to cover any trading that can’t be directly seen.
--- page 126 ---

HEDGING
111
0
0.02
0.04
0.06
0.08
0.1
0.12
0.14
0.16
0.18
0.2
0
5
10
15
20
25
k
Probability Mass
λ = 5
λ = 10
FIGURE 6.10
Two Examples of the Poisson Distribution
trades in any interval, N∆t, is Poisson distributed with a constant parameter
λ. So in this timescale the expected number of trades, λ, per trading time
is constant. If the stock is busy, trading time ﬂows quickly. If the stock is
quiet then trading time is slow. (The Poisson distribution is illustrated in
Figure 6.10. Note that the distribution is only deﬁned for integer values of
k and the connective lines were only added to help visualize the shape.)
The market impact, F(n), is deﬁned as the amount the log midprice of
the underlying changes due to a trade of n shares. Or
∆ln S =
N∆t

i=1
sign(ni)F(|ni|)
(6.16)
For a Poisson distribution with parameter λ, we have
E[N∆t] = Var[N∆t] = λ∆t
(6.17)
so
Var[∆ln S] = E[N∆t]Var[F(ni)] + Var [N∆t]E[F(ni)]2
= λ∆tE[F(n)t]2
(6.18)
A number of researchers have concluded that market impact scales as the
square root of the trade size (Hasbrouck 1991; Madhavan and Smidt 1991;
BARRA 1997).
F(n) = α√n
(6.19)
where α is some constant, the market impact parameter.
--- page 127 ---

HEDGING
112
Substituting this into Equation 6.18 we obtain
Var[∆ln S] = α2λ∆tE[ni] = α2 µ∆t
(6.20)
where µ is deﬁned as the number of shares traded per unit of trading time.
The time change to trading time was designed to make this quantity
constant. So this equation also says that the variance of returns per unit of
trading time is also constant. Now we imagine that we undo our original
time shift. This means that both the volatility (σt) and µt, the number of
shares traded per unit of actual time, will be random variables. Eliminating
the common factor of ∆t (refer to Equation 4.18) we obtain
σ2
t = α2 µt
(6.21)
This gives a straightforward relationship between volume and volatility.
This has been conﬁrmed in numerous studies (Clark 1973; Tauchen and
Pitts 1983; Karpoff 1987), and few traders will dispute the relationship
(although they will argue over whether volume causes volatility or vice
versa). This model also leaves unsettled the dispute over whether trading
time is measured in number of trades or in volume of shares. Here, the
choices are equivalent.
Equation 6.22 gives us a simple way to estimate the market impact.
α =
σt
√µt
(6.22)
We know how to estimate the volatility. All we need to measure now is
the volume of stock traded per unit of time.
Strengths
■The model is very simple to understand and estimate.
■The model ﬁts our basic intuition: The more activity there is in a stock,
the less our market impact will be.
■We don’t need to deal with data at the level of individual transactions.
■This model can be used as a framework in the same way that we use
BSM and the hedging models in Chapter 1. We can tune it to each
individual market by multiplying by a prefactor. For example, we might
ﬁnd that DAX stocks are more slippery than FTSE stocks. (Merrill Lynch
calculated a list of these prefactors. I don’t include these here because
they are probably obsolete and they were estimated by asking Merrill
Lynch traders. I think, but cannot prove, that they reﬂect the attitudes
of individual traders as much as any fundamental aspect of each market.
