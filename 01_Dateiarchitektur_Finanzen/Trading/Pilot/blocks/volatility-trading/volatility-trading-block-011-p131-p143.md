# Volatility Trading_ Sinclair_Volatility Trading -- Euan Sinclair(auth_) -- Wiley Trading, 1, 2013 -- John Wiley & Sons, Incorporated -- isbn13 9781118347133 -- 2634a86bfed8248fa7ba3fb72595bbbc -- Anna’s Archive.pdf — Chapter 7: Distribution of Hedged Option Positions (pages 131–143)

--- page 131 ---

117
C H A P T E R 7
Distribution
of Hedged
Option Positions
I
n Chapter 1, we stated the central result that
P/L = Vega (σimplied −σrealized)
(7.1)
Actually, this is only true on average. There are wide ﬂuctuations around
this amount. In this chapter we look at the causes and magnitude of these so
we know exactly what we can expect as the results of our trades.
■Discrete Hedging and Path Dependency
As an example, imagine we buy one-year call options with a total vega of
$1,000, at an implied volatility of 30 percent and realized volatility over
their lifetime is in fact 30 percent. We hedge delta each day on the close. The
proﬁt and losses (P/Ls) for 10 realizations of this process are shown here:
–$516
$154
–$108
–$537
$331
Volatility Trading,   Second Edition.    Euan Sinclair
© 2013 Euan Sinclair. Published 2013 by John Wiley & Sons, Inc.
--- page 132 ---

DISTRIBUTION OF HEDGED OPTION POSITIONS
118
–$1,741
–$230
$138
$423
$1,984
The average P/L is a loss of $10.2. This is reasonably close to the
expected value of zero, but there is a wide dispersion of values. No doubt in
one universe there are traders who are justifying their loss of $1,741 to their
manager and others who are concocting a story about how their trading
prowess made $1,984. What is really going on here? What will the actual
distribution of results look like? The central insight in the Black-Scholes-
Merton (BSM) argument is that an option can be replicated by trading the
underlying. Figure 7.1 shows the results of 100 simulations, where we
actually try to replicate this option. As we are long a call the replicating
portfolio should look like a short-call position.
So things are approximately what we expect. This indeed looks like
the payoff from a short-call position struck at 100, with the initial value
corresponding to a vega of $1,000. But the replication isn’t perfect. There
is signiﬁcant dispersion around the true value. The dispersion is dependent
on the ﬁnal underlying price with the most variability occurring when we
expire near the strike.
The ﬁrst thing to note is that we are not hedging continuously. Discrete
hedging makes our nondirectional strategy very path-dependent (this has
nothing to do with the weak path dependence of U.S. options as opposed
–200,000
–150,000
–100,000
–50,000
0
50,000
0
50
100
150
200
Terminal Stock Price
Hedging Portfolio Value
FIGURE 7.1
One Hundred Realizations of the Hedging Strategy for the
One-Year Option
--- page 133 ---

DISTRIBUTION OF HEDGED OPTION POSITIONS
119
to European options). Two sample paths with exactly the same realized
volatility can lead to different P/Ls. Consider an extreme example where
all the movement of the underlying is due to one jump. In the ﬁrst path, the
jump happens on the ﬁrst day, as shown in Figure 7.2. In the second path,
the jump happens right before expiration (Figure 7.3).
In each case, the position P/L is the change in the call price minus the
change in the value of the hedge position.
P/L = C(T) −C(0) −

∆(t) × (S(t) −S(t −1))
(7.2)
But in this special case, we only need to evaluate the delta immediately
before the jump. For the case of an at-the-money (ATM) call,
Case One: ∆>0.5
Case Two: ∆=0.5
So the difference in P/L in these two instances is
∆(P/L) = (∆1 −∆2) × (S(T) −S(0))
(7.3)
Time
Price
FIGURE 7.2
Path One: The Jump on the First Day
Time
Price
FIGURE 7.3
Path Two: The Jump Right before Expiration
--- page 134 ---

DISTRIBUTION OF HEDGED OPTION POSITIONS
120
So if we are short this call we do better in the ﬁrst instance because we
are long more stock as a hedge. This is admittedly an extreme example
but the general principle holds. The timing of a move is important to the
proﬁtability of an option.
Let’s now look in more detail at the size and nature of this effect when
we have more realistic sample paths. Take a stock initially trading at $100.
Assume rates, dividends, and the drift are zero. Again we buy one-year call
options with a total vega of $1,000, at an implied volatility of 30 percent
and simulate 100 paths where the realized volatility over their lifetime is in
fact 30 percent. Speciﬁcally we use GBM, so the stock path is given by
S(t + ∆t) = S(t) exp

−σ2
2 ∆t + σ
√
∆tε

(7.4)
where ε is drawn from a standard normal distribution with mean of zero
and standard deviation of one. In Figure 7.4, we hedge weekly. The results
are summarized in Table 7.1.
Frequency
0
2
4
6
8
10
12
14
16
18
–18,000
–16,000
–14,000
–12,000
–10,000
–8,000
–6,000
–4,000
–2,000
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
More
P/L
Percentage of Observations
FIGURE 7.4
The P/L Distribution for $1,000 Vega of Initially ATM Options When
Hedged Once a Week
TABLE 7.1
Summary Statistics for the Hedging Frequency
Experiment
Hedge Frequency
P/L
σP/L
Kurtosis
Skew
Daily
−107.19
2,615.2
4.05
0.25
Weekly
−140.36
5,714.6
3.66
0.16
--- page 135 ---

DISTRIBUTION OF HEDGED OPTION POSITIONS
121
Frequency
0
5
10
15
20
25
30
35
Percentage of Observations
–18,000
–16,000
–14,000
–12,000
–10,000
–8,000
–6,000
–4,000
–2,000
2,000
0
4,000
6,000
8,000
10,000
12,000
14,000
16,000
18,000
More
P/L
FIGURE 7.5
The P/L Distribution for $1,000 Vega of Initially ATM Options When
Hedged Once a Day
In Figure 7.5, we hedge daily.
From this crude experiment, we can draw some tentative conclusions:
■The average P/L is roughly zero.
■The distribution is roughly normal looking.
■The dispersion is inversely proportional to the hedging frequency, more
speciﬁcally it is closely approximated by N–1/2 when N is the number of
hedges (see Figure 7.6).
We said earlier that ‘‘realized volatility over their lifetime is in fact
30 percent.’’ This wasn’t exactly true. The process that generated the
underlying price did have a volatility of 30 percent. But we were only
observing the process at discrete intervals. This introduces sampling error.
From Chapter 2, Equation 2.10, we know that the sampling error is given by
σmeasured ≈σ ±
σ
√
2N
(7.5)
So the volatility of the P/L as a function of the initial option value will be
approximated by
σP/L ≈Vega
σ
√
2N
(7.6)
--- page 136 ---

DISTRIBUTION OF HEDGED OPTION POSITIONS
122
0
2,000
4,000
6,000
8,000
10,000
12,000
0
50
100
150
200
250
300
Number of Hedges
Standard Deviation of P/L
FIGURE 7.6
The Distribution of the Hedging Error as a Function of the Number
of Rebalances
This argument isn’t rigorous and isn’t actually correct, either. The actual
relationship is given by
σP/L ≈
π
4 Vega σ
√N
(7.7)
(Kamal and Derman 1999).
This result can be used to derive a useful rule of thumb for the standard
deviation of a straddle position. An approximation for the value of an
at-the-money option (put or call) is given by
C ≈
1
√2π
Sσ
√
T
(7.8)
(Brenner and Subrahmanyam 1994). So the vega of a straddle (a put and a
call) is approximately
Vega ≈
2
√2π
S
√
T
(7.9)
If we think of the straddle as a single volatility bet and hedge only once,
Equation 7.7 gives us
σP/L ≈
1
√
2
S
√
Tσ
(7.10)
Also note that in this case only the actual realized volatility is relevant. It
only matters where we are at expiry, not on what the option market is
implying after we have done our trade.
The important point is that traders can be correct about their assessment
of realized volatility and still not make money. This is just the risk we take
--- page 137 ---

DISTRIBUTION OF HEDGED OPTION POSITIONS
123
for not hedging inﬁnitely often and running up an inﬁnite amount of trading
cost. This variability is unfortunate but we can always reduce it by hedging
more frequently. Note that this is when the underlying follows a diffusive
process. If there are jumps we can’t alleviate the issue by hedging more
often. In the real world there are simply some risks we can’t hedge away.
Equity traders are trading drift but they are also exposed to volatility risk
and path dependency. Being long a stock that moves smoothly from 100
to 110 in one dollar increments is very different to being long a stock that
moves from 100 to 110 but dropped to 50 before shooting up. In each
case the ﬁnal price does not tell the full story of the risks involved in the
trade. We seek to trade volatility but we also have volatility sampling risk
(intimately related to the volatility of volatility) and path dependency.
■Volatility Dependency
This analysis has assumed that we were hedging our options at the true
volatility. In practice this is unknown and we need to choose a hedging
volatility. There are two obvious candidates, σforecast and σimplied. Which is
better and what consequences are attached to choosing a volatility that will
almost certainly not be the same as the realized volatility?
A simple set of examples shows that the results of this choice are
again very path-dependent. Consider the two underlying price paths
shown in Figure 7.7. These have exactly the same annualized volatility
(23.44 percent), but in one case the price drifts higher and in the other
case it does not.
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
1
2
3
4
5
6
7
8
9
10 11 12 13 14 15 16 17 18 19 20 21
Time
Price
FIGURE 7.7
Two Price Paths with Identical Volatility
--- page 138 ---

DISTRIBUTION OF HEDGED OPTION POSITIONS
124
TABLE 7.2
Results for Hedging the Same Option Portfolio
under Different Volatilities and Different Paths
Path
Hedge at Implied
Hedge at Realized
Drifting
$9,821
$10,516
Nondrifting
$6,765
$3,078
Assume we buy $1,000 vega of the one-month calls with a strike price of
100, at an implied volatility of 18.44 percent, and hedge at the end of each
day. Also assume that we are able to perfectly forecast the realized volatility.
(Note that here there will be no sampling induced errors in the P/L because
the price path has been exactly constructed rather than generated by a
speciﬁed random process.) Table 7.2 shows the P/L possibilities when we
hedge along each path with either the implied volatility or the forecast
volatility.
So obviously the choice matters a great deal, and equally obviously the
situation is very path-dependent. When the underlying is drifting and we
are long gamma, our hedges are going to be losers. We will be selling into a
rising market. So we want to hedge less often. If we use a higher volatility,
we see a lower gamma so we hedge less. Conversely in a choppy, trendless
market our hedges will tend to be winners. So we want to hedge more
often. So if we use a lower volatility we can ‘‘gain’’ more gamma. The
situation is obviously opposite if we are short options. Traders refer to this
hedging trick as letting their deltas run if they are long in a trending market,
or hedging defensively if they are short gamma in a trending market. This is
summarized in the mnemonic table (Table 7.3).
Next we more generally examine the problem of choosing a hedging
volatility. We assume we sell an option at an implied volatility, σi, and
we then hedge at the realized volatility, σr. Let’s examine how the P/L
of this position evolves through time as we hedge it. This is really just the
same argument we used in Chapter 1, but now we need to be very careful
TABLE 7.3
The Direction One Should Bias Volatility
for Different Option Positions as a Function
of Market Direction
Position
Market
Hedging Volatility Bias
Short Gamma
Trending
Low
Short Gamma
Range Bound
High
Long Gamma
Trending
High
Long Gamma
Range Bound
Low
--- page 139 ---

DISTRIBUTION OF HEDGED OPTION POSITIONS
125
whether we are evaluating quantities at the implied or realized volatilities.
Again our derivation will be informal. Readers interested in mathematical
details should consult Carr (1999), Henrard (2003), or Ahmad and
Wilmott (2005).
Expression 1.2 gives the value of the hedged portfolio after the ﬁrst
time step. Note that we need to evaluate the option at σi because we are
interested in the portfolio value as it is marked to market, but ∆needs to
be evaluated at the realized volatility because that is how we have chosen to
hedge. This is the P/L that hits our accounts at the end of each day.
C(St+1, σi) −C(St, σi) −∆(σr)(St+1 −St) + r(C(σi) −∆(σr)St) (7.11)
However, we also know that we can evaluate the portfolio at the realized
volatility,σr,andheretheoptionwillbevaluedcorrectly(bydeﬁnition)sothat
C(St+1, σr) −C(St, σr) −∆(σr)(St+1 −St) + r(C(σr) −∆(σr)St) = 0
(7.12)
So over one time step our marked to market proﬁt is
dC(σi) −dC(σr) + r(C(σr) −∆(σr)S)dt −r(C(σi) −∆(σr)S)dt
(7.13)
Now using the BSM expression (Expression 1.5) we could also write this
one step proﬁt as
1
2(σ2
i −σ2
r )S2(σi)dt + (∆(σi) −∆(σr))((µ −r)Sdt + σSdX)
(7.14)
■Expression 7.13 tells us that we will make money if σI > σr (leaving
aside the issues associated with discrete rebalancing).
■Equation 7.14 tells us that this proﬁt does not arrive smoothly. Equation
7.14 contains a random variable.
■The way the proﬁt is realized depends on the drift term, µ.
Figure 7.8 shows ﬁve possible paths for the P/L evolution as a function
of time for an option hedged at realized volatility. This was for the case of
a short position consisting of 1,000 vega of one year, at the money calls,
sold at a volatility of 40 percent and hedged at the realized volatility of
30 percent until expiry. Drift, rates, and dividend yields were zero.
Traders should be familiar with this situation. These P/L swings essentially are due to other people (the market) marking options against our
position. This isn’t meant to be taken as a conspiracy theory. We traded the
options because they were mispriced. They still are. We end up carrying
the wrong amount of stock against our position. We are hedged in our mind
--- page 140 ---

DISTRIBUTION OF HEDGED OPTION POSITIONS
126
–2,000
0
2,000
4,000
6,000
8,000
10,000
12,000
0
50
100
150
200
250
300
Time (Days)
P/L
FIGURE 7.8
Proﬁt as a Function of Time for a Short Position, Hedged at the Realized
Volatility
but not according to the market. Anyone who has ever tried to explain this
situation to their managers will know that it can be a difﬁcult conversation.
Next we look at what happens when we hedge at the implied volatility.
We go through the same analysis as above, but now all the relevant variables
are evaluated at the implied volatility. The one time step mark to market
proﬁt is given by
dC(σi) −∆(σi)dS −r(C(σi) −∆(σi)S)dt = 1
2(σ2
i −σ2
r )S2(σi)dt
(7.15)
■Equation 7.15 contains no stochastic terms. The proﬁt arrives deterministically.
■There are no issues with the options being ‘‘marked against us.’’ Whatever
they are marked at, we hedge accordingly.
■This is a viable hedging method even if we don’t know how to forecast
volatility very well! If we sell options because our only opinion is that
implied volatility is too high, we can still make money.
If we take the present value of the one-step proﬁt then sum over all time
steps, we arrive at the total P/L for the position.
1
2(σ2
i −σ2
r )

exp(−rt)S2(σi)dt
(7.16)
We can now see the path-dependence effect that we observed in the
earlier example. Even if our option is initially struck at the money, the drift
in the underlying will take it away from there until the option’s gamma is
--- page 141 ---

DISTRIBUTION OF HEDGED OPTION POSITIONS
127
small and hence the potential proﬁt (Equation 7.16) is small. This makes
sense. We are putting on a volatility bet. We only get paid if we assume
some volatility risk and if an option is sufﬁciently far from the at-the-money
point we have no volatility exposure left. This is why traders want to end up
near the strike at expiration. The gamma is largest at that point in time and
space. If you are correct in your volatility assessment you make the most
money there. This is also an argument for trading strangles or strips instead
of straddles. We want to have a volatility position over a wide enough range
of the underlying.
This path dependency is also a reason why different strikes should indeed
trade at different implied volatilities. The path the underlying takes has
different effects on options of different strikes because their gamma proﬁle
will be very different. Equation 7.14 tells us that the fair implied volatility
(the volatility that makes the P/L zero) is gamma-dependent. This concept
is explored by Dupire (2006) in his work on ‘‘break-even volatility skews.’’
Note that this applies to both longand short-gamma positions. This may
come as a surprise. Most traders know that it is good for a short position
to gently settle near a strike at expiry. However, it is also good for a long
position to ﬁnish at the strike. The difference is that practically hedging the
long position becomes next to impossible at very short timescales and the
only time we can hedge easily is when realized volatility is low (i.e., we
gently settle near our long strike), which means our volatility forecast is
incorrect. We need to also note that expiring at a strike greatly increases
the feedback effects of the dynamic hedging of the market makers. If they
are long gamma, they will all be buying the underlying below the strike and
selling it above the strike thus compressing the realized volatility. This will
be bad for the option holders, but it is the low volatility that is bad, not being
near the strike. Being near the strike can be the cause of the low volatility.
Figure 7.9 shows ﬁve possible paths for the P/L evolution as a function
of time for an option hedged at implied volatility. This was for the case of a
short position consisting of 1,000 vega of one year, at the money calls, sold
at a volatility of 40 percent and hedged at the implied volatility until expiry.
Drift, rates, and dividend yields were zero.
Figure 7.9 shows that hedging at the implied volatility gives a smoother
P/L, but the end result is far more variable than when we hedge at realized
volatility. Most traders ﬁnd this a far easier situation to deal with.
Ahmad and Wilmott (2005) found expressions for the expected proﬁt
(as an integral) and the standard deviation (as a double integral) of an
option hedged at the implied volatility. The interested reader can refer to
these, but it is probably more useful to gain a feel for this situation by
--- page 142 ---

DISTRIBUTION OF HEDGED OPTION POSITIONS
128
–5,000
0
5,000
10,000
15,000
20,000
25,000
0
50
100
150
200
250
300
Time (Days)
P/L
FIGURE 7.9
Proﬁt as a Function of Time for a Short Position Hedged at
Implied Volatility
running simulations (these can also be extended to cover different stochastic
processes, an implied volatility smile and a position consisting of more than
one option type). Figures 7.10 and 7.11 shows the results of several such
simulations. We can clearly see some features.
■Out-of-the-money option positions have far more variance than at the
money options.
■We have less variance if we err on the high side when choosing a hedging
volatility.
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
0
0.1
0.2
0.3
0.4
0.5
0.6
0.7
0.8
Hedging Volatility
Standard Deviation
FIGURE 7.10
Standard Deviation for a Short At-the-Money Position Hedged
at Various Volatilities
--- page 143 ---

DISTRIBUTION OF HEDGED OPTION POSITIONS
129
0
10,000
20,000
30,000
40,000
50,000
60,000
70,000
0
0.1
0.2
0.3
0.4
0.5
0.6
0.7
0.8
Hedging Volatility
Standard Deviation
FIGURE 7.11
Standard Deviation for a Short 20 Delta Call Position Hedged
at Various Volatilities
We can hedge at any volatility we like. We are not restricted to implied
volatility or the forecast volatility. The general case was examined by Carr
and Henrotte but again, running simulations is probably the easiest way to
get a good picture of the situation.
■Summary
The BSM equation shows that option values are independent of the underlying return. However, in real markets volatility positions are dependent
on the underlying’s path and our choice of hedging volatility.
■Hedged option positions are very path-dependent.
■Correctly predicting realized volatility is no guarantee of being proﬁtable.
■Some variance in P/L can be eliminated by hedging more frequently.
■Hedging at realized volatility makes our ﬁnal P/L more certain but very
noisy.
■Hedging at implied volatility smooths the P/L but makes the ﬁnal amount
more uncertain.
