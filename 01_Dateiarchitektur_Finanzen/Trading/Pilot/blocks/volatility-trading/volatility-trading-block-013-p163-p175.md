# Volatility Trading_ Sinclair_Volatility Trading -- Euan Sinclair(auth_) -- Wiley Trading, 1, 2013 -- John Wiley & Sons, Incorporated -- isbn13 9781118347133 -- 2634a86bfed8248fa7ba3fb72595bbbc -- Anna’s Archive.pdf — Chapter 8: Money Management (pages 163–175)

--- page 163 ---

MONEY MANAGEMENT
150
The situation for traders is different. Here we have a positive expectation.
But we would still like to perform a similar trick to Oscar and somewhat
smooth our stream of proﬁts. We would also like to reduce our dependency
on the long run. This was the problem addressed by Browne (1999, 2000).
Speciﬁcally he found the dynamic strategy that maximized the probability of
reaching a given wealth level in a speciﬁed time. He shows that the optimal
fraction to invest with T, time left to reach the Goal B when current wealth
is W, is given by
f ∗=
1
σ√T
B exp(−rT)
W
n

N−1
W exp (rT)
B

(8.33)
where
n(x) =
1
√2π
exp
−x2
2

(8.34a)
N(x) =
x

=∞
n(z)dz
(8.34b)
and r is the interest rate.
Browne shows that this sizing strategy is equivalent to the hedging
strategy of a binary call. This argument is insightful and should help option
traders get a feel for the behavior of the strategy. It may also help us think of
ideas for generalizing the argument to more realistic scenarios, for example,
where we have a stop placed on our bankroll as well as a target on the
upside.
If we have a stock that evolves according to our normal model of GBM,
the value of an option that pays B if we are above the strike, K, at time, T,
is given by
C = B exp(−r(T −t))N


ln
 S
K

+

r −1
2σ2

(T −t)
σ√T −t


(8.35)
(Haug 2007b).
The delta of this option is given by
∆= B exp(−r(T −t))n


ln
 S
K

+

r −1
2σ2

(T −t)
σ√T −t


1
Sσ√T −t
(8.36)
--- page 164 ---

MONEY MANAGEMENT
151
∆is the number of shares in the hedging portfolio, so at any time the
value of the hedge is given by ∆xS. If we were actually short the option,
our aim would be to hedge it so that we maximized the probability that
we could pay off the claim at expiry. Or, at any given time our ‘‘wealth’’
is given by the expression in Equation 8.35 and we need to maximize the
probability that our terminal wealth is given by B. The optimal policy in
such a case is given by Equation 8.33, here with wealth x = C(t,S). Making
this substitution we obtain
f ∗= ∆S
(8.37)
So this strategy is indeed equivalent to the hedging strategy of the digital
call where we consider the ‘‘stock price’’ to be our wealth, W. Figures 8.11
and 8.12 show the difference between this dynamic sizing strategy and the
constant Kelly strategy. This assumes that we are trading a stock with a
drift of 22 percent, an annualized volatility of 45 percent, and there is
also a risk-free rate of 8 percent. In this case the Kelly ratio is 0.6914.
Our goal is to make 50 percent in a session of 100 trading days (not
completely unreasonable but very optimistic given the drift and volatility
of the underlying). We can see that initially the Browne strategy is much
more aggressive. We know that our goal requires us to take signiﬁcant
risk. Initially we trade at a leverage of 1.8, three times the leverage of the
Kelly strategy. But as we get closer to our goal, we signiﬁcantly dial down
the risk. In practice, we would continually monitor our goals and make
adjustments (this process is discussed in Chapter 9).
60
80
100
120
140
160
180
1
7
13
19
25
31
37
43
49
55
61
67
73
79
85
91
97
Trading Days
Wealth
Kelly
Browne
FIGURE 8.11
The Wealth Accumulated When Following the Browne and Kelly
Strategies
--- page 165 ---

MONEY MANAGEMENT
152
0
0.2
0.4
0.6
0.8
1
1.2
1.4
1.6
1.8
2
1
6
11
16
21
31
36
41
46
51
56
61
66
71
76
81
86
91
96
Trading Days
Browne Ratio and Goal Likelihood
Browne ratio
Probability of Success
FIGURE 8.12
The Browne Ratio and the Probability of Reaching the Goal
TABLE 8.3
Time Needed for Browne’s Strategy to Beat Competing
Strategies by 10 Percent
Bankruptcy
Probability
Time to Beat Cash
by 10 Percent (years)
Time to Beat Stock
by 10 Percent (years)
0.05
1.3
85
0.01
14
900
0.001
43
2,780
0.0001
73
4,774
He also shows that the expected time for this strategy to beat any other
is given by
T =


N−1 (1 −α) −N−1

1
1 −ε

σ(f −f ′)


2
(8.38)
So now we can compare this strategy to Kelly’s results given above.
These numbers are far better than for the Kelly strategy. Recall that for
Kelly to beat the stock by 10 percent (at the 95 percent conﬁdence level), it
would take 10,286 years. Granted, trading using the Kelly criterion would
leave us with no chance of bankruptcy but the signiﬁcant improvement in
the expected time to perform may well make this small risk worthwhile.
As we can see according to the criteria of expected time to dominate,
this method is far better than Kelly. It is also riskier. Speciﬁcally, we expect
--- page 166 ---

MONEY MANAGEMENT
153
to achieve our goal with probability V, and go bankrupt with probability
1 −V, where V is given by
V = N

N−1
W exp (rT)
B

+ µ −r
σ
√
T

(8.39)
and where
µZ is the expected drift of the asset.
V
is also shown above in Figure 8.12.
As we said earlier, when utility functions are involved we need to decide
what exactly we mean by successful.
The situations examined so far have been static. Either we have had an
opportunity to place a single trade/bet and see how it fares or we have
had the opportunity to invest in an asset with ﬁxed drift and volatility. A
more realistic situation is one where the parameters we are interested in are
changing. In particular we have seen in Chapter 5 that implied volatility is
a mean-reverting process. Considering these situations leads to a seemingly
paradoxical situation.
Proebsting’s paradox is the counterintuitive result that application of the
Kelly criterion can seemingly lead to bankruptcy. As with most ‘‘paradoxes’’
this one can be resolved, but looking at the argument and its resolution
is nevertheless worthwhile. The situation was ﬁrst pointed out by Todd
Proebsting in an e-mail to Edward Thorpe who wrote about it in Wilmott
Magazine (Thorpe 2008).
Imagine a situation where a gambler is offered a bet with a 50 percent
chance of winning. A win pays $2 and a loss loses $1. Equation 8.5 tells us
that the Kelly fraction is 0.25. Now, before the game is played, the bettor
is offered another bet on the same event. This one pays $5 if it wins and
still only can lose $1. We need to determine the fraction of bankroll, f, to
allocate to this new opportunity. After the bet is resolved the gambler’s
bankroll will either be 1.5 W0 + 5 f W0, if he wins, or 0.75 W0 −f W0 if he
loses. So we need to maximize
0.5 ln(1.5W0 + 5f W0) + 0.5 ln(0.75W0 + f W0)
(8.40)
This gives f = 0.225.
So the total fraction (the total bet on ﬁrst the 2/1 bet and then the 5/1
bet) is 0.425. The paradox is that if only the 5/1 bet was offered the Kelly
fraction would be 0.4. So application of the Kelly criterion leads us to be
more when some of the bet is at worse odds.
Even more alarmingly, if the gambler is offered better and better odds
he will eventually bet all of his money (in the limit). This gives him a
--- page 167 ---

MONEY MANAGEMENT
154
100 percent chance of going bankrupt and was precisely the situation that
the Kelly criterion was designed to avoid.
Proebsting’s paradox is important because this situation occurs all the
time in trading. Prices change continuously and our edge (odds) ﬂuctuates
accordingly. The most satisfactory resolution of the paradox was given by
Aaron Brown (also in an e-mail to Ed Thorpe). In a rare case of ﬁnance
theory illuminating a gambling issue rather than vice versa, Brown made
use of the idea of marking to market.
Speciﬁcally when the gambler is offered the 5/1 bet it means that on a
marked to market basis his 2/1 bet is a loser. That bet may not have settled
but it is still a loser as we can now get a better payoff for the same cost.
And, as any derivatives trader should know, it is the daily P/L that matters,
not what would happen if the trade was held until expiration. What is the
change in the gambler’s bankroll when the odds move from 2/1 to 5/1?
Alternatively, how much does he have to pay to get at the current market
price of 5/1, a bet that pays 2 for a win? This is the value of γ that satisﬁes
(2 −γ) = 5(1 + γ)
γ = −0.5
that is, entering a 2/1 bet for 0.25 of our bankroll and then having the odds
change to 5/1 is the same as not having bet, having the bankroll change by
−0.5 × 0.25W = −0.125W, and then betting at 5/1 odds.
Generally if we bet f X on a bet with a payout of X/1, then we get offered
Y/1 odds (where Y > B) the mark-to-market wealth (which we should use
to calculate the new betting fraction) is
W = 1 + x
1 + Y W0
(8.41)
where x is the weighted average of the odds
x = f xX + (1 −f x)Y
(8.42)
We will see that trading a mean-reverting process is similar. As the
deviations from fair value get larger we will do more of the trade. This leads
to the rule of thumb: When in trouble, double. But this is true only to a
point. In a continuous trading setting, as we get better and better prices we
will be losing money on the position we have already established. Eventually
these losses will have depleted our bankroll to the point where we actually
want to have a smaller position on. This is consistent with how market
makers are told to size their trades when they have things pushed against
them. The old rule would have a market maker sell 100 at his ﬁrst level,
--- page 168 ---

MONEY MANAGEMENT
155
then back up and sell 200 at the next level, back up again and sell 300 at
the next level. But if things get pushed further from ‘‘fair value’’ he would
start to buy the position back. This isn’t necessarily because his estimate of
what is fair might have changed (although by this point it probably will have
done) but because he has lost money and the short 600-lot position is too
large a function of his new account size.
We will set up a simple model that captures the basic features of what
we are trading, and try to generalize the Kelly argument. The simplest
mean-reverting model is the single parameter Ornstein-Uhlenbeck process,
governed completely by its speed of reversion, µ. Also let’s assume for
simplicity that we have normalized the underlying, S, so it has a mean of
zero and a standard deviation of one.
dS = −µSdt + √2µdZ
(8.43)
As with GBM these asset paths look very noisy and just looking at them
would be a very bad way to estimate the true reversion speed. Actually,
visual inspection wouldn’t even be enough to see that these were mean
reverting. For example, the three paths shown in Figure 8.13 all simulate
ﬁve years of daily prices with a reversion speed of 100 percent.
The optimal asset allocation for such a process has been studied
(Boguslavsky and Boguslavskaya 2004; Liu and Longstaff 2004). They
showed that if we try to generalize the Kelly approach and maximize the
expected value of the logarithm of wealth the solution is that we should
hold
−W × σ/2
(8.44)
in the asset.
So if we are risking $100 and the price of the asset is 1.8 standard
deviations from its mean (i.e., σ = 1.8) then we will have a short position
of 100 × 1.8/2 = 90. In practical terms this means we should have on a
position such that if the spread goes back to the mean we should make $90.
Figures 8.14 and 8.15 show the results of a ‘‘trading session’’ where we
size our trades according to this rule.
There are a number of important things to note about this deceptively
simple result.
■Wealth is equally important as the attractiveness of the trade (σ and W
are interchangeable in the result).
■The maximum position is at σ = 21/2. Beyond this the effect of losing
wealth dominates. The trades are now better but our bankroll is now also
smaller.
--- page 169 ---

MONEY MANAGEMENT
156
−1.5
−1
−0.5
0
0.5
1
1.5
2
2.5
3
(a)
−2
−1.5
−1
−0.5
0
0.5
1
1.5
(b)
−2
−1
−1.5
0.5
0
2
1.5
1
2.5
3
3.5
(c)
FIGURE 8.13
Three Different Instances of an Asset Path Generated by the Same
Mean-Reverting Process
■At deviations smaller than 21/2, we add to trades as they go against us.
Here the extra edge in the trade dominates the fact that we are losing
money on our position.
■This result is independent of the reversion speed. High reversion rates
are good, but only because we get to do more trades in the same period
of time.
--- page 170 ---

MONEY MANAGEMENT
157
−2.0000
−1.5000
−1.0000
−0.5000
0.0000
0.5000
1.0000
1.5000
937
859
781
703
625
547
469
391
313
235
157
79
1
Time (Days)
Price
1,015 1,093 1,171 1,249
FIGURE 8.14
The Mean Reverting Asset Price
0.00
100.00
200.00
300.00
400.00
500.00
600.00
700.00
925
848
771
694
617
540
463
386
309
232
155
78
1
Time (Days)
Wealth
1,002 1,079 1,156 1,233
FIGURE 8.15
The Wealth Generated by Trading According to Equation 8.44
As with all strategies that maximize the expectation of the logarithm of
wealth, this is an aggressive money management scheme. To some extent
this can be partially managed by careful choice of W0 (where we will apply
partial instead of full Kelly). But a further danger exists here. We have
assumed that the process is governed by an Ornstein-Uhlenbeck process
with normal innovations. The real processes we deal with in ﬁnance will
generally have fatter tails than implied by the normal distribution. Things
will not work so well in this case. Figures 8.16 and 8.17 show the results
of a trading session where the distribution is logistic rather than normal.
The important difference between this example and that of Figures 8.12
and 8.13 is that here we have an excess kurtosis of 9. The results are clearly
affected for the worse.
There doesn’t seem to be any published work on optimal positioning for
these types of processes, but some intuition can be gained by running some
simulations. Fat-tailed distributions also have thin middles. So in addition
to the larger proportion of large moves we can also expect more small
moves. This would seem to suggest that modifying the strategy by trading
more aggressively when entering looking for small moves then exiting
--- page 171 ---

MONEY MANAGEMENT
158
–4
–3
–2
–1
0
1
2
3
4
5
6
1
45
89
133
177
221
265
309
353
397
441
485
529
573
617
661
705
749
793
837
881
925
969
1,013
1,057
1,101
1,145
1,189
Time (Days)
Price
1,233
FIGURE 8.16
The Mean-Reverting Asset Price
0
2,000
4,000
6,000
8,000
10,000
12,000
14,000
16,000
1
47
93
139
185
231
277
323
369
415
461
507
553
599
645
691
737
783
829
875
921
967
1,013
1,059
1,105
1,151
1,197
1,243
Time (Days)
Wealth
FIGURE 8.17
The Wealth Generated by Trading According to Equation 8.44
more quickly when things move against us. Numerical experiments seem
to support this.
It is important to emphasize the dangerous game we are playing here.
This theory shows that when trading a mean-reverting process we should
(at ﬁrst) add to our position as it goes against us. This clearly can be
dangerous. The danger has nothing to do with such unsupported rules as
‘‘only losers add to losers.’’ In fact, the theory shows that the optimal trading
rule in this instance is to add to losers. Further, this rule can be enunciated,
tested, and modiﬁed in a way that vague general assertions cannot. The real
danger is that the system may fundamentally change so that the ‘‘mean’’ we
will eventually revert to is totally different to the one we started with. This
is why we need to fundamentally evaluate why the initial trade has gone
against us. Imagine we are short a stock at 20 percent volatility because
we think the fair value is 13 percent. If it gets choppy because a few large
orders enter the market on an otherwise slow day and implied volatility
rises to 22 percent, we are probably justiﬁed in selling more. However,
--- page 172 ---

MONEY MANAGEMENT
159
consider the example of InterOil Corporation (IOC). At 2 P.M. EST on June
26, 2007, huge sell orders hit the market and drove the stock price down
from $40.2 to $26.5. There was no news about the company on any of the
major news wires. July implied volatility jumped from about 94 percent
to 120 percent. In this case a fundamental revaluation of the company had
occurred. We have no news or analysis to consider and huge volume was
being transacted (6 million shares in an hour in a stock with an average daily
volume of 600,000). In this case to sell more volatility would be foolhardy
and irresponsible. So each case needs to be considered in context.
This is obviously an area where experience of a particular market can be
an asset. But there is a good way to use experience and a bad way. The
good way is to use your knowledge defensively. You should actively look
for things that are out of place with what you have seen in the past and then
be extra cautious. The bad way is to overﬁt to past data. If you have never
seen deviations as large before, that doesn’t necessarily mean that this is the
best trade you have ever done. This could well mean your past experience
is now irrelevant.
Selling a rising market and buying a falling market is the replication
strategy for a short option. In Chapter 4, we saw that forecast volatility
is generally below implied volatility. Part of the reason for this was that
in selling implied volatility we were selling insurance against events that
have never occurred before. That is also the case when scaling into any
mean-reverting asset. You have to be aware of this and be prepared to stop
scaling in, even when it can look better than it ever has before.
In practice, it will generally be difﬁcult, or even impossible, to maintain
the perfect level of positioning. Illiquidity, transaction costs, noncontinuous
trading, position limits, and order entry restrictions mean that at best we
will need to use Equation 8.44 as a guide. It might also be helpful to have a
discrete rule to guide us in putting on the ﬁrst portion of the position. Let’s
try a simple argument for maximizing our total proﬁt given, that we have to
choose one point for entering the trade. This and other rules for selecting
entry points in mean reverting processes were covered in Vidyamurthy
(2004).
In this toy model we assume that the deviations of the asset price from
its mean value are normally distributed and independent. So at any time
we just draw a number from a normal distribution to ﬁnd the deviation
and this is independent of the previous values. For a normally distributed
process, the probability at any time that we have deviated by more than S
from the mean is just the integral of the process. This is equal to 1 −N(S)
(where N [.] is the cumulative normal distribution function). So in, T, time
--- page 173 ---

MONEY MANAGEMENT
160
steps we can expect to have T (1 −N(S)) times, where the asset price has a
deviation greater than or equal to S. The normal distribution is symmetric
so we have an equal number of times where the spread is less than or equal
to −S. So in T time steps, we will have traded 2T (1 −N(S)) times. Each
of these gives a proﬁt of S. So the total proﬁt is given by
2T S(1 −N(S))
(8.45)
To ﬁnd the maximum of this function with respect to S, we differentiate
and set the result equal to zero. This gives the result
Smax = 0.75σ
(8.46)
Figure 8.18 shows the shape of the theoretical distribution of the P/L as
a function of the entry level.
How different will trading a real process be? A true ﬁnancial process will
differ from this ideal in three important ways.
1. The distribution will have fat tails.
2. There will be different behavior associated with declines and increases
(for example, the Volatility Index (VIX) is mean-reverting but is prone
to have larger moves up than down).
3. The standard deviation of the process will not be constant.
But rather than use a more complex model, we now look at trading a
mean-reverting product with various entry levels and see how the P/L varies
in practice. We simulate trading the VIX. We know this is a mean-reverting
process. Here we follow a simple Bollinger band rule. We buy or sell the
VIX after it has deviated by a certain amount from its moving average. As
can be seen, the deviation from the simple moving average is somewhat
3.5
3
2.5
2
1.5
1
0.5
0
P/L
SDs
60
80
100
120
0
20
40
FIGURE 8.18
The Shape of the P/L Distribution as a Function of Entry Level
--- page 174 ---

MONEY MANAGEMENT
161
0
20
40
60
80
100
120
140
3.5
3
2.5
2
1.5
1
0.5
0
SDs
P/L
FIGURE 8.19
The Shape of the P/L Distribution for the VIX Trade
normal looking but clearly is fat tailed and skewed. We could address the
skewness issue by having different bands for buying and selling but that is not
the point of this exercise. This is not meant to be a realistic trading idea. It is
just intended to show that Equation 8.46 has some applicability to a situation
that we know does not follow the necessary simplifying assumptions.
We can see in Figure 8.19 that the peak of the P/L function is close to
the theoretical point of 0.75 standard deviations. So aggressively scalping
can produce more proﬁts. But note that the left-hand end of the curve tails
off much faster so it is probably safer to err on the side of caution and trade
slightly less often than optimal.
■Summary
Although trade sizing can’t turn a losing trade into a winning one, our
choices still have a signiﬁcant impact on our proﬁtability, variance, and
drawdowns. It is important that our sizing scheme and parameters are
established before we start trading, and then only adjusted after very careful
consideration. It is easy to overreact to atypically good or bad runs of
results.
■Before you can choose a money management scheme you must be clear
what you are trying to accomplish. Your monetary goals, time constraints,
and maximum tolerable drawdowns need to be fully speciﬁed in advance.
■When there is more edge, trade bigger.
■When there is more variance or uncertainty, trade smaller.
--- page 175 ---

MONEY MANAGEMENT
162
■The Kelly scheme will eventually overwhelm all others.
■The Browne scheme is useful for hitting speciﬁc targets.
■When trading volatility we have to be prepared to do more as a trade
initially goes against us.
■Adding arbitrary price based stops to a trading system is a poor idea.
We should exit our trades when we are wrong. Having volatility move
against us may not indicate that we are wrong at all.
■A good rule of thumb is that a trade should be big enough that the proﬁts
mean something, but not so big that the losses are catastrophic. If this
optimum size can’t be found, the trade probably doesn’t have enough
edge to begin with.
