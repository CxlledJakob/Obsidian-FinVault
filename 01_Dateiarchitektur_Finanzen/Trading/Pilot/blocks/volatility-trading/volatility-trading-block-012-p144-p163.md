# Volatility Trading_ Sinclair_Volatility Trading -- Euan Sinclair(auth_) -- Wiley Trading, 1, 2013 -- John Wiley & Sons, Incorporated -- isbn13 9781118347133 -- 2634a86bfed8248fa7ba3fb72595bbbc -- Anna’s Archive.pdf — Chapter 8: Money Management (pages 144–163)

--- page 144 ---

131
C H A P T E R 8
Money
Management
Everybody’s got a plan until they get hit.
—Mike Tyson
A
lthough it is not true that a good money management system can turn
any trading method into a proﬁtable one, it is certainly possible to ruin
even the best trades with poor money management. Edge estimation and
capture are difﬁcult and both involve subjective judgment. So it is probably
understandable that traders focus so heavily on these aspects of trading. But
money management and trade sizing is just as essential for success. In this
chapter we look at the various methods we can use to size trades and the
risk/reward characteristics that each choice implies.
■Ad Hoc Sizing Schemes
Consider the equity curves shown in Figures 8.1 and 8.2. It seems obvious
that the trader in the ﬁrst ﬁgure is in some sense better. He has made
much more money in the same period of time, albeit while displaying
more variance. Actually, in this instance, the trades that the traders made
were identical. All the difference in their equity curve was due to the
sizing strategy. Both traders were playing a game where they ﬂipped a coin
and received a dollar if they were correct and paid a dollar if they were
wrong. Each won 550 bets out of 1,000. But the ﬁrst trader ﬁnished with
$5,207 and the second only accumulated $620. Trade sizing is clearly an
important issue.
Volatility Trading,   Second Edition.    Euan Sinclair
© 2013 Euan Sinclair. Published 2013 by John Wiley & Sons, Inc.
--- page 145 ---

MONEY MANAGEMENT
132
0
1,000
2,000
3,000
4,000
5,000
6,000
7,000
8,000
1
101
201
301
401
501
601
701
801
901
1,001
Number of  Trades
Cumulative P/L
FIGURE 8.1
An Equity Curve for a Trader Betting 5 Percent of His Bankroll on
Each Trade
0
100
200
300
400
500
600
700
1,001
901
801
701
601
501
401
301
201
101
1
Number of Trades
Cumulative P/L
FIGURE 8.2
An Equity Curve for a Trader Betting $5 on Each Trade
The simplest method is to size according to ‘‘feel.’’ The trade size is
adjusted on an ad hoc basis depending on how good the trader thinks the
individual bet is. This is a terrible idea. This isn’t really so different to
picking trades based on feel and it is quite possible that the sizing decisions
can dominate the trade choices themselves. Our entire methodology is
based on the idea that we can systematically approach the trading process,
and to size our trades according to hunches goes completely against this. It
will let us fall victim to our moods and psychological biases: precisely what
we are trying to avoid.
The next step is to trade the same amount every time. For example, we
might choose to always trade 100 options or 1,000 vega. This is known
--- page 146 ---

MONEY MANAGEMENT
133
as a ﬁxed trade size system. Any system that can ﬁnd value will be proﬁtable
(over the long run) with such a sizing scheme. In back testing this is often
the sizing scheme used, as it most clearly shows the proﬁtability of the
underlying method.
Or we could choose to trade a constant percentage of our bankroll at
each opportunity. This is known as a ﬁxed fraction sizing system.
Our example earlier was for just one group of 1,000 bets. Figure 8.3
shows the results for another three trials. We can see two things. First,
even though in all cases we have the same mathematical edge (a 55 percent
chance of winning an even money bet) the results vary wildly. Second, the
choice of bet size makes a huge difference. Proportional betting sometimes
results in vastly greater ﬁnal wealth and our wealth can never go to zero
(at least in the idealized case we consider here where we have inﬁnitely
divisible currency units), but looks to be much more volatile in its results
than ﬁxed betting.
This numerical experiment has clearly shown that the choice of a staking
plan is important. And in addition to the two schemes mentioned earlier,
there are a number of others we could dream up. For example, we could
bet so that all successful bets would win the same amount, increase bets
(either by absolute size or relative size) after a win, or we could adopt
a similar strategy where we increase bet size after a loss. With all these
schemes there will be parameters we need to choose, for example, what
percentage of our bankroll to start betting with.
These methods are often used as the basis of betting systems. It is
quite easy to make them seem appealing to mathematically unsophisticated
gamblers. Let’s consider again our coin-tossing game where we win at a
rate of 55 percent. If we double our stake each time we lose a bet until we
eventually win, we end many betting runs with wins of a single unit but
eventually we lose our entire bankroll. We haven’t changed the expectation
of our distribution, but we have introduced a massive amount of skew,
trading frequency of win for size of loss.
How can we decide between all the alternatives? A possible solution to
this problem was found by John Kelly (1956).
■The Kelly Criterion
Consider a general situation such that when we win, we gain w percent and
when we lose, we lose l percent. Our bankroll is initially W0. Each bet is a
set fraction, f, of the bankroll.
--- page 147 ---

MONEY MANAGEMENT
134
0
1,000
2,000
3,000
4,000
5,000
6,000
7,000
8,000
1
101
201
301
401
501
601
701
801
901
1,001
Number of Trades
Cumulative P/L
% bets
$ bets
(a)
0
50
100
150
200
250
300
1
101
201
301
401
501
601
701
801
901
1001
Number of Trades
Cumulative P/L
% bets
$ bets
(b)
0
500
1,000
1,500
2,000
2,500
3,000
3,500
4,000
4,500
5,000
1
101
201
301
401
501
601
701
801
901
1,001
Number of Trades
Cumulative P/L
% bets
$ bets
(c)
FIGURE 8.3
Three More Comparative Equity Curves for the Same Process as in
Figure 8.1
--- page 148 ---

MONEY MANAGEMENT
135
So after a win our bankroll is
W0(1 + fw)
(8.1)
Or we can say that the gain factor is (1 + fw). Similarly, a loss would leave
us with
W0(1 −f l)
(8.2)
So the gain factor here is (1 −fl). More simply, each time we win we
multiply by (1 + fw) and when we lose we multiply by (1 −fl). So for n
wins and m losses the gain factor is
G( f ) = (1 + fw)n(1 −f l)m
(8.3)
Or per trade we get
G( f )
1
n+m ≡g( f ) = (1 + fw)p(1 −f l)q
(8.4)
where p = n/(n + m) is the probability of a win and q = m/(n + m) is the
probability of a loss.
It would be a mistake to choose f to maximize G. On any ﬁnite number
of bets, our expected return would be maximized by betting our entire
bankroll each time. Sadly, this also gives us a 100 percent chance of going
bankrupt, as eventually we are bound to lose. This strategy takes no account
of risk. We actually want to maximize our risk-adjusted return or utility.
This involves choosing a particular utility function again. Generally the log
utility function is chosen (we could choose any one of a number of utility
functions but the log function can be shown to do better in the long run
than any other). In this case we will not be maximizing expected wealth but
we will be maximizing typical wealth. This distinction is important. The
average value would be heavily distorted by the unlikely case where the
trader wins every trade. This won’t be of great consolation to the traders
who have gone bankrupt. By maximizing the logarithm of expected wealth
we eliminate the possibility of bankruptcy.
So we take the log of the gain function and ﬁnd the optimal f by
differentiating with respect to f then setting this equal to zero. This gives
f = (pw −ql)
wl
(8.5)
(So in our initial simple example the Kelly fraction would have been 0.1.)
Our expected bankroll after N bets would be given by
W = W0(1 + p ln(1 + fw) + q ln(1 −f l))N
(8.6)
Figure 8.4 shows the expected bankroll for 10 bets as a function of bet
size where wins pay twice as much as the losses and we win 45 percent of
--- page 149 ---

MONEY MANAGEMENT
136
–0.2
0
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
0.2
0.4
0.6
0.8
1
1.2
1.4
1.6
Bet Size
Bankroll
FIGURE 8.4
The Expected Bankroll for 10 Bets as a Function of Bet Size
bets. The Kelly ratio in this case is 0.175, which corresponds to the peak
of the curve. Betting more than twice Kelly turns the growth rate negative
and our bankroll becomes more depleted as we bet bigger.
Running some simple simulations should make several points abundantly
clear:
■The Kelly fraction generally ﬁnishes with more wealth than any other
chosen proportional scheme.
■The swings in our equity become uncomfortably large when betting the
Kelly fraction.
■Betting more than Kelly is worse than betting less.
This last point is worth emphasizing. Betting more than Kelly results in
higher volatility and lower returns. This can be seen in Figure 8.5 where
we show one realization of a proﬁt and loss (P/L) curve for the coin tossing
game when using half Kelly, full Kelly, and twice Kelly bet sizes.
At this point, let’s just assume that the Kelly strategy is sufﬁciently
intriguing to make it worthwhile considering a more realistic situation:
one that is closer to those we might encounter when trading ﬁnancial
instruments.
We need to generalize the situation to deal with a continuous outcome.
Imagine trading a situation where the outcome of a bet or trade is known
to have a certain distribution. This would be the typical situation facing a
trader: Either the distribution can be estimated from historical trade results
--- page 150 ---

MONEY MANAGEMENT
137
8,000
10,000
12,000
14,000
16,000
Kelly
half Kelly
0
2,000
4,000
6,000
901 1,001
801
701
601
501
401
301
201
101
1
Cumulative P/L
Number of Trades
twice Kelly
FIGURE 8.5
The Relative Volatility of a P/L Path Generated by Trading at Various
Multiples of the Kelly Ratio
or from more theoretical considerations. We do still insist at this point
that the trades be independent and identically distributed. Again we bet a
fraction, f, of our wealth at the start of each period so that
Wn = Wn−1 + f Wn−1g(Xn)
(8.7)
where Xn is the random variable giving the result of the nth trade and it has
the payoff g(Xn). After a sequence of n trades our bankroll will be
Wn = W0
n
i=1
(1 + fg(Xi))
(8.8)
Now we take logarithms as before:
ln(Wn) = W0
n

i=1
ln(1 + fg(Xi))
(8.9)
So
E[ln(Wn)] = nW0E[ln(1 + fg(Xn))]
(8.10)
= nW0

ln(1 + fg(x))(x)dx
(8.11)
where (x) is the distribution function that describes the results of the
trades. If we maximize over the bankroll fraction, f, we ﬁnd that the optimal
value is the one that satisﬁes
 g(x)(x)dx
1 + fg(x) = E

g (x)
1 + fg(x)

= 0
(8.12)
--- page 151 ---

MONEY MANAGEMENT
138
This equation is quite general. It applies to all distributions. It is sometimes
incorrectly stated that the Kelly criterion only applies to trades with binary
outcomes. This is untrue. However, in the case of binary events, certain
simpliﬁcations can be made. These approximations do indeed have limited
applicability. In general, Equation 8.12 is too unwieldy to use directly, but
if we consider the case where our edge per trade is small we can make
things simpler (and sadly this case usually is fairly representative of reality).
In this situation we know that f will be small and we can expand Equation
8.12 in a power series, and then truncate after leading order to get
0 ≈

g(x)(x)(1 −fg(x) + · · ·)dx
=

g(x)(x)dx −f

g2(x)(x)dx + · · ·
(8.13)
But the ﬁrst term is just the expected payoff for a unit bet and the second
term is the variance of the payoff, g(x). So in the limit of small edge we
obtain
f = r
σ2
(8.14)
This is certainly simple enough to use. To estimate our trading size we
need only the expected return of the trade and its variance, no matter how
complicated the actual trade is. Actually, the return here should generally
be interpreted as the return over the risk-free rate. Many derivations neglect
to mention this (those aimed at gamblers probably neglect it as it is difﬁcult
to earn interest while sitting at a blackjack table and bookmakers tend not
to pay interest, either).
The expected growth rate for someone trading at a fraction, f, of the Kelly
ratio is given by
GR =

f −f 2
2
 r2
σ2
(8.15)
which is maximized for f = 1: trading at the full Kelly ratio when the growth
rate is
GRmax = r2
2σ2
(8.16)
And we see that the growth rate is zero for f = 0, the case where we don’t
trade at all, and f = 2, when we drastically overbet. As the growth rate is
symmetric around f = 1, we can see it is better to bet more conservatively
and hence to underestimate our edge (or equivalently to overestimate our
variance) as we will obtain the same growth for f = 1 −x and f = 1 + x.
--- page 152 ---

MONEY MANAGEMENT
139
If we are trading according to the Kelly criterion the probability that we
reach a bankroll B × W > W0 before we dip to A × W < W0 is given by
P(A, B) =
1 −A1−2
f
B1−2
f −A1−2
f
(8.17)
It is interesting that the edge and variance of the trade don’t appear here.
Having a ‘‘better’’ trade just speeds up the process. If A = 0.5 and B = 2,
we get P(A,B) = 2/3. Conversely, this means that when betting at full Kelly
you have a one-third chance of having your bankroll halve before it doubles!
As we saw in our earlier simulations Kelly sizing is exceedingly volatile.
To deal with these extreme drawdowns it is reasonably common for Kelly
devotees to trade at a fraction of the Kelly ratio. Table 8.1 shows how the
probability of halving before doubling can be changed by using a fractional
Kelly ratio.
Reducing drawdowns by trading at a fraction of the Kelly ratio is not a
free lunch. By trading smaller we dramatically increase the time needed to
reach our upside goal. The expected exit time is given by
E[T] = 1
GR log
 BP(A,B)
AP(A,B)−1

(8.18)
This is the mean time before we reach our goal (B.W0), or are stopped
out (at A.W0).
There is no compelling theoretical reason for sizing trades according to the
fractional Kelly idea. Fractional Kelly doesn’t correspond to maximizing any
utility function. There are two practical reasons for using fractional Kelly.
1. It is a pragmatic attempt to ﬁnd a middle ground between realizing the
potential returns from trading at the full Kelly ratio and reducing the
resulting high volatility.
TABLE 8.1
Probability of Doubling before
Halving as a Function of
the Kelly Fraction That
We Are Trading
Fraction of Kelly
Prob (A,B)
1
0.667
0.8
0.739
0.6
0.834
0.4
0.941
0.2
0.998
--- page 153 ---

MONEY MANAGEMENT
140
2. It is a poor man’s Bayesian approach to acknowledging the general
difﬁculty of beating markets. For example, half-Kelly corresponds to
taking an average of our edge estimate and the zero-edge alternative that
the market is a perfect predictor of future value.
We now have some sort of intuition about our prospective proﬁt and
loss distribution when using Kelly. We have the expected growth rate, a
measure of dispersion (the drawdown probability) and the expected time to
reach our goals. But it is actually possible to calculate the entire probability
distribution of our future bankroll. A paper by Chapman (2007) shows
how the bankroll spreads through time. For convenience we take the initial
bankroll to be one. He shows the probability distribution evolves as
P(x, f , t) = exp

1 −1
f

t

1
√2πt
exp

−

log x +
3
2 −1
f

t
2
2t


(8.19)
Figure 8.6 is worth examining carefully. It shows the evolution through
time of the probability distribution function (PDF) of the bankroll when
trading at the Kelly fraction. We see that over time the bankroll relaxes
and diffuses away from its initial value. We can also see that when betting
at the full Kelly ratio, our distribution of outcomes is highly skewed (this
should have already been evident from the earlier discussions of drawdowns
but some more visual evidence can emphasize the point). The peak of the
probability distribution function is less than one. We know that in the long
run the Kelly strategy comprehensively dominates other strategies but we
also know the result of any one series of trades is volatile so may be poor in
the short run (before the growth rate has had a chance to overwhelm the
volatility) and the ‘‘long run’’ may take quite some time to arrive.
Figure 8.7 shows how trading at a reduced Kelly fraction (in this case
half-Kelly) substantially shifts the peak of the PDF to the right while still
maintaining the skewness, which makes large wins possible.
Conversely, Figure 8.8 shows that trading higher than Kelly (twice Kelly
in this instance) means that the PDF is pulled toward zero as time passes.
Sizing bets/trades according to the Kelly criterion is a controversial topic
(see Poundstone 2005 for a very readable account). Most of the discussion
centers around the idea that maximizing the logarithm of expected wealth
isn’t really what a sensible investor would want; that is, the utility function
is speciﬁed incorrectly. The anti-Kelly group includes Nobel Prize winners
--- page 154 ---

MONEY MANAGEMENT
141
0.4
0.5
0.6
t = 0.5
t = 1
0
0.1
0.2
0.3
6
5
4
3
2
1
0
Probability Distribution
Bankroll
t = 2
t = 3
FIGURE 8.6
The Evolution through Time of the PDF of the Bankroll When Trading at
the Kelly Fraction
0.25
0.3
0.35
0.4
t = 0.5
t = 1
0
0.05
0.1
0.15
0.2
6
5
4
3
2
1
0
Probability Distribution
Bankroll
t = 2
t = 3
FIGURE 8.7
The Evolution through Time of the PDF of the Bankroll When Trading at
the Half of the Kelly Fraction
(Samuelson 1979), ﬁnance professionals (Brown 2002), and sports gamblers
(Miller, www.professionalgambler.com). However, the other side of the
argument also boasts some impressive names, including Ed Thorpe (1984,
1997), Claude Shannon (inventor of information theory), David Shaw
(founder of D. E. Shaw), and William Miller (manager of the Legg Mason
Value Trust, the only SEC regulated mutual fund to outperform the S&P
500 for 10 consecutive years). As the method is dependent on a utility
--- page 155 ---

MONEY MANAGEMENT
142
0.6
0.7
0.8
0.9
1
t = 0.5
t = 1
0
0.1
0.2
0.3
0.4
0.5
6
5
4
3
2
1
0
Probability Distribution
Bankroll
t = 2
t = 3
FIGURE 8.8
The Evolution through Time of the PDF of the Bankroll When Trading at
Twice of the Kelly Fraction
function, it isn’t too surprising that people disagree. But instead of getting
into arguments over what other people’s risk preferences should be, let’s
simply look at the Kelly criterion’s good and bad points.
Good Points
■Maximizing the expected value of the logarithm of wealth asymptotically
maximizestherateofgrowth,sotheKellystrategyeventuallyoutperforms
all others.
■The Kelly strategy has zero risk of ruin.
■On average we will always be ahead of any other strategy.
■The strategy is myopic, in the sense that we only ever need to consider
our current opportunities and bankroll, not subsequent situations. This
is not the case for progression-type methodologies where current trade
sizes are a function of previous trade sizes. Myopia is useful when deciding
if a strategy is practically useable.
■Trading a fraction of the Kelly amount allows us to easily tune our desired
level of risk at the expense of lower expected returns.
Bad Points
■When betting a fraction of wealth, a loss followed by a win still leaves us
behind.
--- page 156 ---

MONEY MANAGEMENT
143
■The amount bet becomes extremely large in situations where we have a
large amount of edge, that is, when the probability of a win is high or the
risk is very low.
■Probability estimation becomes crucial. Overinvesting based on overestimation of success likelihood will lead to disaster.
■The total amount of money invested is far larger than the winnings.
■Due to the strategy’s volatile outcomes, it is possible to have sessions
with poor outcomes even though the long-term expectations are high.
■The time necessary for the long run to dominate can be very long indeed.
■Sometimes it isn’t obvious what ‘‘bankroll’’ is.
The good points have been studied and may well seem so good that any
bad points can be ignored. Isn’t the fact that sizing according to the Kelly
criterion eventually creates more wealth than any other strategy, enough
to override any concerns? Before we come to this conclusion, let’s take a
slightly closer look at the bad points we haven’t already noted.
■Time for Kelly to Dominate
We all know we need to be patient when trading. This is often axiomatically
stated as a virtue. We tend to say reﬂexively that we possess patience
because we are so acutely aware that it is necessary for a good trader, but
how patient do we need to be to reap the beneﬁts of the Kelly strategy?
An example from Browne (2000) shows that waiting for the long run
can be more tedious than we might reasonably expect. He considers an
investor who has a choice between a stock with an annual return of
15 percent and a volatility of 30 percent and an interest bearing account
that pays 7 percent. The Kelly criterion (Equation 8.14) has us invest
89 percent of our wealth (0.15 −0.07/(0.3)2) in the stock and put the
remainder in the bank. Before we have a 95 percent probability of beating
the all cash portfolio by 10 percent, we have to wait 157 years. Even
worse, to have a 95 percent probability of beating the all-stock portfolio
by 10 percent, we have to wait 10,286 years. Even the expected times
to outperform these benchmarks is 2.8 years and 184 years.1 Patience is
indeed necessary.
1The expected time for Kelly to outperform another strategy with a trading fraction f′, by
ε percent is given by
2
σ2(f −f ′)2 ln (1 + ε)
--- page 157 ---

MONEY MANAGEMENT
144
■Effect of Parameter Mis-Estimation
In practical ﬁnancial applications we will never really know the distribution
of outcomes of the trades. Do our errors in estimating the distribution
actually matter? This was studied by Medo, Pis’mak, and Zhang (2008).
First we consider trades with a binary outcome. If we lose, we pay a
dollar and if we win, we gain a dollar. If the win probability is p > 0.5, we
have a favorable game and the Kelly ratio is
f = 2p −1
(8.20)
But what if we don’t know p? What if we have to estimate it from historical
data? Assume that we have N trials to do this estimation and in this period
we see w wins. Bayes’ theorem gives the distribution of the true probability
as
θ(p|w, N) =
π(p)P(w|p, N)
1

0
π(p)P(w|p, N)dp
(8.21)
where π(p) is the prior distribution of p, and P(w|p,N) is the probability
distribution of w, given N and p. P is a binomial distribution with mean pN.
P(w|p, N) =

N
w

pw(1 −p)N−w
(8.22)
As all of the information we have is contained in the observations, the
prior needs to reﬂect this maximum ignorance. So we need to use the
uniform distribution, π(p) = 1, over the range of p from zero to one (The
choice or prior can also be used to bias our estimate low, reﬂecting caution
in our ability. For example, we might choose to use a distribution deﬁned
over the range of zero to 0.75). Evaluating the integral in Equation 8.21
gives us
θ(p|w, N) =
(N + 1)!
w!(N −w)!pw(1 −p)N−w
(8.23)
This distribution has a mean
⟨p⟩= w + 1
N + 2
(8.24)
This is important. Our naive guess of win rate (6 wins out of 10 implying
a true rate of 0.6) will always overestimate. We need to incorporate the
effects of our prior ignorance. This lessens the weight we give to the
observations. The distribution is shown in Figure 8.9 for w = 6 and N = 10.
Note also that there is a signiﬁcant chance of the results of this trade
--- page 158 ---

MONEY MANAGEMENT
145
0
0.5
1
1.5
2
2.5
3
0
0.2
0.4
0.6
0.8
1
1.2
Unobservable True Probability
Density
FIGURE 8.9
The Posterior Distribution When Observing 6 Wins in 10 Plays
appearing to have a negative expectation. This can be found by looking at
how much of the cumulative Kelly distribution is below 0.5. In this case it
is around 27 percent.
Further, we can calculate the variance of the distribution.
Var(p) = (w + 1)(w + 2)
(N + 2)(N + 3) −(w + 1)2
(N + 2)2
(8.25)
In this example, we get a standard deviation of 0.137.
What is the Kelly ratio in these circumstances, where clearly we have the
extra ‘‘risk’’ of parameter uncertainty? There is a signiﬁcant chance that we
may even be playing in a losing game.
The Kelly ratio is the amount, f, that maximizes the logarithmic gain. We
also know, from the work of Chapman (among others), that this corresponds
to using the average of the win probability. But we can illustrate this with a
simple example.
Consider the simplest case. The winning probability can take one of two
values: p1 with probability F1 or p2 with probability F2. Now we can write
the growth rate as
G = (F1p1 + F2p2) ln(1 + f ) + (1 −F1p1 −F2p2) ln(1 −f )
(8.26)
Differentiating this with respect to f and setting equal to zero gives the
Kelly ratio as
f = 2(F1p1 + F2p2) −1
(8.27)
--- page 159 ---

MONEY MANAGEMENT
146
This is clearly just
f = 2⟨p⟩−1
(8.28)
This doesn’t seem particularly interesting, but when we combine this
with Equation 8.24 we see that
f = 2w −N
N + 2
(8.29)
If we compare this with the naive value where we estimate p to be w/N
we see that
f
fnaive
= 2w −N
N + 2
2 w
N −1
= 2w −N
N + 2 ×
N
2w −N =
N
N + 2
(8.30)
which implies that the naive estimate will always bias our bets too high.
This effect isn’t particularly large and in the limit of large N it disappears
completely. In fact after 100 trials we will be off by only 2 percent. Of
more importance is the variance of f. How many trials do we need to be
reasonably sure that our measured value is close to being correct?
The delta method tells us that the variance of f is given by
var( f ) =
∂f
∂p
2
var(p)
(8.31)
Using Equations 8.25 and 8.31 we get
var( f ) = 4
(w + 1) (w + 2)
(N + 2)(N + 3) −(w + 1)2
(N + 2)2

(8.32)
So looking back at the case in the ﬁgure where w = 6, N = 10: We
would estimate that the standard deviation of f would be approximately
0.274. This again diminishes as N increases. If we had observed 60 wins in
100 trials our standard deviation would be only 0.097.
The actual dependence of the standard deviation of the Kelly ratio with
sample size conforms to our expectations. More data implies less deviation.
For a theoretical win probability of 0.6, the deviation as a function of sample
size is shown in Figure 8.10.
■What Is Bankroll?
Bankroll certainly isn’t haircut. The haircut is the amount we need to post
at our clearing ﬁrm, but it certainly is not the amount you are able to
lose. Generally it is better to think of bankroll as the amount you can lose
before the strategy is abandoned. But sometimes this isn’t clear either. This
--- page 160 ---

MONEY MANAGEMENT
147
0
0.05
0.1
0.15
0.2
0.25
0.3
0.35
0.4
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
55
60
65
70
75
80
85
90
95
100
N
Standard Deviation of f
FIGURE 8.10
The Dependence of the Standard Deviation of f as a Function
of Sample Size
was studied by Leib (1995). He pointed out that amateur blackjack players
should bet much more aggressively than professionals as the amateurs could
replenish their bankrolls from their other income. This concept also applies
to traders who can switch jobs.
There are two ways that the Kelly criterion can be interpreted:
1. It is the strategy that maximizes the expect growth of the bankroll.
2. It is the strategy that maximizes the logarithmic utility function.
Neither interpretation is really consistent with a situation where we can
replenish our bankroll.
Within the ﬁrst framework, the goal is to become as rich as possible as
quickly as possible. Going bankrupt is bad because it makes further growth
impossible. Having any money at all left is inﬁnitely better than having
none. However, if there is another source of capital available (from another
job or backer, for example), then further growth is still possible.
Under the utility growth interpretation capital growth is just a consequence. Utility growth is an end in itself. Here, going broke is inﬁnitely bad
purely because utility becomes unboundedly bad.
Under either interpretation, losing all of your bankroll is inﬁnitely bad.
It is important to emphasize the word inﬁnitely. This means that there is
never any way to come back. And this is seldom the case in real life. We are
really talking about cases where the gambler has risked life itself.
We can align ourselves more closely with the Kelly approach if we consider our total wealth and then adjust the fractional adjustment accordingly.
--- page 161 ---

MONEY MANAGEMENT
148
For example, if we have a trading account of $1 million and a total net worth
of $5 million we could choose a bankroll of $5 million and a Kelly fractional
multiplier of 0.1 instead of a bankroll of $1 million and a multiplier of 0.5.
For bets with small edge the differences will be minimal but when the edge
becomes large the difference will be apparent.
■Alternatives to Kelly
So is what Kelly does really what a trader wants? As always, the answer
is, ‘‘it depends.’’ What externally imposed constraints does he face? In a
personal account where no one else can stop him out due to a drawdown, a
trader may be happy to use Kelly and tune the volatility by trading a fraction
of the full Kelly ratio. Similarly, when we are making an enormous number
of trades in a short period we may accept a Kelly-based sizing method,
as we can be more conﬁdent that the long run will arrive soon enough to
overwhelm any variance effects. But when trading in an institutional setting
or when being backed by someone else, the Kelly criterion is probably
not really aligned with the interest of the trader. Here traders aren’t as
interested in optimal long-term growth as they are in a better chance of
making a proﬁt. They will trade maximal long-term potential for more
certain short-term proﬁts. We said earlier that Kelly was expected to
outperform other strategies, so what can traders do that are better? They
can gain a more certain short-term proﬁt by giving up the impossibility
of ever going broke. (When trading according to Kelly or any fractional
money management scheme we can never go broke. However, this is really
a theoretical point because most traders will get ﬁred as quickly for turning
in a 90 percent drawdown as a 100 percent drawdown.) To see the general
principle behind this trade-off we now look at Oscar’s system, a progressive
betting system ﬁrst devised by a craps player in the 1950s (Wilson 1965).
A progressive betting system can never turn a negative edge into a positive
edge. There is no magic. But the sizing algorithm can change certain aspects
of the payout schedule. We have already seen this. We earlier mentioned
the skewness generated by doubling bets after losses. Also, the fractional
Kelly system traded lower returns for smaller drawdowns. Oscar wanted
something entirely different. He just wanted every weekend he spent in
Las Vegas to end with a small win. So he devised a progression that works
exceedingly well in the short run.
There are two general types of betting progressions: positive progressions
and negative progressions. With a positive progression, the general theory
is that you raise your bets after wins, which means that your bigger bets
--- page 162 ---

MONEY MANAGEMENT
149
are primarily funded by prior proﬁts. The Kelly scheme is an example of a
positive progression.
With a negative progression, you raise your bets after losses. This attempt
to get back even more quickly is more dangerous, since a bad run of losses
can wipe you out quickly. However, these schemes are seductive in that
they allow you to win after a session in which you’ve lost more bets than
you’ve won. Since your bets after losses are bigger bets, you don’t have to
win so many of them to come back. Or you lose so many consecutive bets
that you go broke.
Many attempts have been made to combine the best features of these
systems. Oscar’s system was one. Oscar wanted to win just one unit. Each
session started with a one-unit bet. If it won, he stopped. If he lost, the next
bet was the same size. (So we take more risk than Kelly because our bets
as a percentage of our bankroll grow as we lose.) After a win, the next bet
would be one-unit higher than the last. No bet would ever be so large that
it would take us over the target.
This system has been analyzed in detail, ﬁrst by Wilson and then
more extensively by Ethier (1996). The probability of success is shown in
Table 8.2.
The problem is that in the rare instances that things go badly, they go
horrendously badly. According to Wilson, in the 1960s Julian Braun ran
a computer simulation of Oscar’s system. He assumed the house had a
betting limit of 500 units and that the probability of success for each bet was
244/495 (consistent with craps). In 280,000 trials there were 66 disasters
where the gambler bumped up against the house limit. These situations lost
an average of 13,000 units. So the laws of mathematics can’t be cheated, but
we can choose to push the disasters into the future rather than experience
them continuously. To a certain degree, you can choose when to take your
(inevitable) losses.
TABLE 8.2
The Probability of Reaching a Proﬁt Target of one unit before
having to quit when using Oscar’s system, as a function of the
win probability for a single trial, p, and the house limit M
M
p = 9/19
p = 244/495
p = 1/2
50
0.99078112
0.99620367
0.99734697
100
0.99464246
0.99841219
0.99904342
150
0.99587158
0.99902785
0.99947577
200
0.99646866
0.99930553
0.99965833
250
0.99681764
0.99946077
0.99975501
300
0.99704404
0.99955895
0.99981337
350
0.99720107
0.99962624
0.99985174
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
