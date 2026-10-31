# Volatility Trading_ Sinclair_Volatility Trading -- Euan Sinclair(auth_) -- Wiley Trading, 1, 2013 -- John Wiley & Sons, Incorporated -- isbn13 9781118347133 -- 2634a86bfed8248fa7ba3fb72595bbbc -- Anna’s Archive.pdf — Chapter 9: Trade Evaluation (pages 195–198)

--- page 195 ---

TRADE EVALUATION
182
half indicates persistence. An exponent less than a half is indicative of
antipersistence or mean reversion. The Hurst exponent applies to data sets
that are statistically self-similar. This means that the statistical properties for
the data set are constant (this is an assumption that we make in most of these
analyses). The Hurst exponent is intimately related to the fractal dimension
of a data set and chaos theory. This is well beyond the scope of this book. The
interested reader should refer to Peters (1996) and the references therein.
First we need to understand rescaled range analysis (often called R/S
analysis). We know that when we ﬂip an unbiased coin, the expected
difference between the number of heads and tails in N attempts grows as
N1/2. This is a characteristic of Brownian motions. In general,
R ≈cNh
(9.9)
where R is the range, c is a constant, and h is the scaling exponent, h = 0.5
in the coin-tossing example. Hurst (1951) generalized this concept from the
special case where h = 0.5. We start with a time series, xt, and construct
the series of deviations
Dt,N =
t

k=1
(xk −MN)
(9.10)
where Dt,N is the cumulative deviation over N periods and MN is the average
of xt over N periods. The range is then deﬁned as the difference between
the maximum and minimum value calculated in Equation 9.10.
R = max(Dt,N) −min(Dt,N)
(9.11)
We now normalize the range by dividing by the standard deviation of the
original observations. This is the rescaled range, R/S. The Hurst exponent,
h, is deﬁned by
R/S = (aN)h
(9.12)
Taking logarithms gives us an equation that can easily be estimated by
linear regression.
ln(R/S) = h ln(N) + ln(a)
(9.13)
This requires a fairly large amount of data to estimate accurately. Hurst
also gave a simple approximation, which estimates h from a single value.
h = ln(R/S)
ln
N
2

(9.14)
This assumes that the constant a, in Equation 9.14 is equal to one-half.
This approximation tends to overstate h when it is over 0.7 and understate
--- page 196 ---

TRADE EVALUATION
183
h when it is under 0.4. However, for short data series where regression
results will be unreliable it gives a reasonable estimate.
When applying rescaled range analysis to trading results, the time series
under consideration should be the logarithmic return series.
Higher Level Evaluation
After you have been tracking your results for a while you will be in a
position to see what has been working and what hasn’t. The incorrect thing
to do is to work on the things that have been weak. Trading is not a sport.
For example, if you want to improve your golf it probably makes sense to
spend time practicing the weaker parts of your game. Improving these will
improve your game and it is also likely that there is more room for easier
improvement. However, in trading you don’t have to do all kinds of trades.
You are perfectly free to do only the types that work for you.
It seems that traders who are good at one or two types of trades become
scared that those things will stop working and decide they need to diversify.
Or possibly they are simply overconﬁdent and think if they can succeed at
one thing they can succeed at ﬁve.
It is always important to try new things, as the concern of a ﬁnite trade
lifetime is somewhat valid. But it is far more important to push the things
that are working. A major danger in trading is not taking the most money out
of a strategy when it is working. Ironically, the fear of a trade degenerating
is what leads to this.
Without doubt the toughest situation to evaluate and handle is where a
long-term winning trade starts to degrade in performance. Can we just put
this down to luck? That could be possible, but we need to be as careful
when separating randomness from signal here, just as we were when we
were evaluating successful trades. It is not just that trades change over
time. The act of trading will eventually cause the edge to dissipate. This
doesn’t only happen at the level of the individual trader. As trades are found
to be proﬁtable more traders will enter and proﬁts will decrease. All the
secrecy in the world will not stop this. Eventually we need to consider these
possibilities:
■The source of edge has disappeared. Sometimes this can be obvious, such
as when the tick size in QQQQ options was reduced from a nickel to a
penny. This was clearly an issue that market makers need to adapt to.
But sometimes the cause of the degradation is more subtle. The author is
good friends with a successful baseball gambler who in 2003, had a return
--- page 197 ---

TRADE EVALUATION
184
of more than 400 percent with a Sharpe ratio of 4. The bets were based
on extensive sabermetric analysis and computer simulations. By 2007 his
return had dwindled to nothing. He had learned more about baseball, but
the market had learned faster (he now trades equity options).
■The ability to execute the trade has declined. This could be due to
changing technology (which could probably go into the ﬁrst category if
technological execution was actually the original source of edge) or to
the effects of increasing age or lack of desire.
■The counterparties of their trades have changed. There is a big difference
to taking the other side of retail ﬂow and trading with other professionals.
Once you have identiﬁed a change in performance, you need to compare
your current methodology to your behavior when you were winning. What
has changed? Sometimes you will ﬁnd that you are now taking shortcuts
due to boredom or overfamiliarity. If you can’t ﬁnd any differences, get a
second opinion.
Changes in ourselves or the markets can occur so gradually that we
are unaware of them. Sometimes it pays to ask, ‘‘If I was starting today,
would I choose this product to trade? Why?’’ (Flexibility when it comes to
choosing products is a great advantage. This option is generally not available
to institutional traders but even if the question is hypothetical, it can be a
useful exercise to identify possible changes that need to be adapted to). A
good rule to remember is that it is making money that counts, not trading
the most complex or glamorous products. This isn’t like professional sports.
Hitting .400 in the minors isn’t the same as doing it in the major leagues,
but in trading, a million dollars is a million dollars. We are all professionals.
There are no minor leagues.
■Summary
The easiest way to improve is to keep detailed records and then review
them. Not only is this necessary to improve but merely doing it almost
guarantees improvement. It forces us to take ownership of our successes
and failures and helps us to see exactly what we can and cannot do. As the
football coach Bill Parcells said, ‘‘You are what your record says you are.’’
■Keep track of the daily results of all trades.
■All trades should have preestablished goals so that terms like success and
failure are deﬁned in advance.
--- page 198 ---

TRADE EVALUATION
185
■All instances where a trading signal is overridden, either by a trader or a
manager, should be noted so that we know how successful such calls are.
■All risk measures have weaknesses. Like our use of different volatility
estimators, learn to use a variety and become comfortable with the
different pictures they provide.
■Remain aware that even a good strategy can go through bad periods.
Don’t give up on the basis of a poor performance over a small sample size
unless something has deﬁnitely changed in the market.
■Consistency of performance is more important than the actual level of
performance.
■Focus on what works and stop doing what doesn’t.
