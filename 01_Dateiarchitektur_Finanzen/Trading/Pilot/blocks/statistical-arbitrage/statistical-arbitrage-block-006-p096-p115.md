# Statistical Arbitrage_ Algorithmic Trading Insights and -- Karen M_ Sowers; Andrew Pole -- Wiley Finance, 1, 2007 -- Wiley & Sons, Incorporated, John -- isbn13 9780470138441 -- 6b0138550172e24db7f13c932e054fb9 -- An.pdf — pages 96–115

--- page 96 ---

Law of Reversion
69
the previous day when at the same time the spread on that previous
day exceeds the median.
Those distinctions may seem arcane but proper understanding
is critical to the correct evaluation of expected result of a strategy.
Suppose that on eight days out of ten the spread is precisely equal
to the median. Then the scheme makes a prediction only for 20
percent of the time. That understanding ﬂows directly from the
conjunction/disjunction distinction. With the wrong understanding
a ﬁve-to-one ratio of expected return to actual return of a scheme
would ensue.
Operationally, one may bet on the outcome of the spread tomorrow once today’s spread is conﬁrmed (close of trading). On those
days for which the spread is observed to be greater than the median
spread, the bet for tomorrow is that the exhibited spread tomorrow
will be less than the spread seen today. The proportion of winning
bets in such a scheme is the conditional given that probability:
Pr[Pt+1 < Pt|Pt > m] = 3
4
Similarly, bets in the other direction will be winners three quarters
of the time. Does this mean that we win ‘‘1.5 of the time?’’ Now that
really would be a statistical arbitrage! The missing consideration is the
relative frequency with which the conditioning event occurs. Now,
Pt < m occurs half of the time by deﬁnition of the median. Therefore,
half of the time we will bet on the spread decreasing relative to today
and of those bets, three quarters will be winners. The other half of
the time we will bet on the spread increasing relative to today and
of those bets, three quarters will also be winners. Thus, over all
bets, three quarters will be winners. (In the previous illustration, the
conditioning events occur only 20 percent of the time and the result
would be 3
4 × 1
5 or just
3
20.)
Before proceeding to the proof of the result, note that the
assumption of continuity is crucial (hence the emphasis in the model
statement). It is trivial to show that the result is not true for discrete
variables (see the ﬁnal part of this section).
4.2.2
Proof of the 75 Percent Rule
The proof of the result uses a geometric argument to promote
visualization of the problem structure. An added bonus is that one
--- page 97 ---

70
STATISTICAL ARBITRAGE
Pt = Pt−1
Pt−1 > Pt
Pt−1 < Pt
1
2
(a)
(b)
Pt−1
Pt
median
median
FIGURE 4.1
Domain of joint distribution of Pt and Pt−1
can see that certain structural assumptions made in the theorem may
be relaxed. These relaxations are discussed following the proof of the
basic result.
Consider the joint distribution of two consecutive terms of the
sequence, Pt−1 and Pt. Assuming independence, the contours of this
joint distribution are symmetric (about the line Pt = Pt−1) regardless
of the precise form of the underlying distribution. In particular, it is
not necessary to assume that the distribution has a symmetric density
function.
Consider Figure 4.1. The domain of the joint distribution (the
positive quadrant of ℜ2 including the zero boundaries) is partitioned
in both dimensions at the median point. By the deﬁnition of the
median, the four quadrants so constructed each represent 25 percent
of the joint distribution.
The lower left and upper right quadrants are bisected radially
from the joint median by the axis of symmetry. Now, the symmetry of
the density contours—resulting from independent, identical marginal
distributions—means that both halves of each quadrant cover the
same total probability. Therefore, each half-quadrant accounts for
12.5 percent of the total joint probability.
The remainder of the proof consists of identifying on the ﬁgure
those regions corresponding to the union in the probability statement
made earlier. This is clearly and precisely the union of shaded regions
--- page 98 ---

Law of Reversion
71
(a) and (b), which is the domain of the joint distribution excepting
unshaded regions (1) and (2). The latter regions each account for
12.5 percent of the total joint probability as shown in the previous
paragraph. Therefore, the union of regions (a) and (b) represents
exactly three quarters of the joint probability.
It is worth noting at this point that we did not decompose the
upper left or lower right quadrants. Fortunately, it is not necessary
to do so since there is no speciﬁc result for the general case.
4.2.3
Analytic Proof of the 75 Percent Rule
The purpose of giving a geometric argument is to facilitate understanding of generalizations of the result that will be presented in
the next section. Before proceeding thereto, we establish the result
analytically. Write X = Pt and Y = Pt−1 to simplify notation. The
two events:
{X < Y ∩Y > m}
and
{X > Y ∩Y < m}
are disjoint (easily seen from the fact that Y > m and Y < m cannot
occur simultaneously: On the graph, regions (a) and (b) do not
overlap), so the probability of the disjunction is simply the sum of
the individual probabilities. Consider the ﬁrst part of the disjunction:
Pr[X < Y ∩Y > m] =
 ∞
m
 y
−∞
fXY(x, y)dxdy
where fXY(x, y) denotes the joint density function of X and Y. By
the assumption of independence, the joint density is just the product
of the individual marginal densities, which in this case are identical
(also by assumption). Denoting the marginal density generically by
f(.) and its corresponding distribution by F(.), proceed as follows:
 ∞
m
 y
−∞
fXY(x, y)dxdy =
 ∞
m
 y
−∞
f(x)f(y)dxdy
=
 ∞
m
F(y)f(y)dy
=
 ∞
m
F(y)dF(y)
--- page 99 ---

72
STATISTICAL ARBITRAGE
The last step is simply recognition that the density function of
a random quantity is the analytic derivative of the corresponding
distribution function. The remaining steps are trivial:
 ∞
m
F(y)dF(y) = 1
2F(y)2

∞
m
= 1
2

lim
t→∞F(t)
2
−F(m)2

= 1
2

1 −
1
2
	2
= 3
8
For the second part of the disjunction, the result follows from a
similar argument after an initial algebraic simpliﬁcation. First, note
that the event Y < m may be expressed as the union of two disjoint
events:
Y < m ≡{(X > Y) ∩(Y < m)} ∪{(X < Y) ∩(Y < m)}
By deﬁnition (recall that m is the median of the distribution), the
probability of the event Y < m is one half. Therefore, using the fact
that probabilities for disjoint events are additive, we may write:
Pr[X > Y ∩Y < m] = 1
2 −Pr[X < Y ∩Y < m]
Now, proceeding much as for the ﬁrst part:
Pr[X > Y ∩Y < m] = 1
2 −
 m
−∞
 y
−∞
fXY(x, y)dxdy
= 1
2 −
 m
−∞
F(y)dF(y)
= 1
2 −1
2

F(m)2 −

lim
t→−∞F(t)
	2
--- page 100 ---

Law of Reversion
73
= 1
2 −1
2
1
2
	2
= 3
8
Adding the probabilities of the two parts yields the result.
4.2.4
Discrete Counter
Consider a random variable that takes on just two distinct values,
a and b, with probabilities p and 1 −p, respectively. Whenever
p̸ = 1
2, the probability of the random variable exceeding the median
is also not equal to one half! Notwithstanding that minor oddity,
examine the probabilities of the two events comprising the theorem
statement:
{X < Y ∩Y > m}
and
{X > Y ∩Y < m}
In this discrete example these events are speciﬁcally:
{X = a ∩Y = b}
and
{X = b ∩Y = a}
which each have probability p(1 −p), hence, the probability in
the theorem is 2p(1 −p). The maximum value this probability can
assume is 1
2 when p = 1
2 (differentiate, equate to zero, solve).
4.2.5
Generalizations
Financial time series are notorious for the tenacity with which they
refuse to reveal underlying mathematical structure (though Mandelbrot, 2004, may demur from that statement). Features of such data,
which often show up in statistical modeling, include: nonnormal
distributions (returns are frequently characterized by leptokurtosis);
nonconstant variance (market dynamics often produce bursts of high
and low volatility, and modelers have tried many approaches from
GARCH and its variants to Mandelbrot’s fractals, see Chapter 3);
and serial dependence. The conditions of the theorem can be relaxed
to accommodate all of these behaviors.
--- page 101 ---

74
STATISTICAL ARBITRAGE
The result extends to arbitrary continuous random variables
directly: The constraint of support on the nonnegative real line is not
required. In the geometric argument, no explicit scaling is required
for the density axes (the zero origin is convenient for explication).
In the analytic argument, recall that we did not restrict the region of
support of the densities.
Note that if the underlying distribution has a symmetric density
function (implying either that the support is the whole real line
or a ﬁnite interval), then the pivotal point is the expected value
(mean) of the density if it exists. The Cauchy distribution, sometimes
appropriate for modeling daily price moves, does not have a deﬁned
expected value, but it does have a median and the stated result holds.
The 75 percent rule is extended for nonconstant variances in
Section 4.3.
The independence assumption is straightforwardly relaxed: From
the geometric argument, it is only necessary that the contours of
the joint distribution be symmetric. Therefore, the independence
condition in the theorem can be replaced by zero correlation. An
analytical treatment, with examples, is presented in Section 4.4.
Finally, generalizing the argument for the nonconstant variance
case extends the result so that the spread distribution may be different
every day, providing that certain frequency conditions are satisﬁed.
Details are given in Section 4.5.
4.3
INHOMOGENEOUS VARIANCES
Spreads are supposed to be generated independently each day from
a distribution in a given family of distributions. The family of
distributions is ﬁxed but the particular member from which price is
generated on a given day is uncertain. Members of the family are
distinguished only by the variance. Properties of the realized variance
sequence now determine what can be said about the price series.
What can be said if the variances, day to day, exhibit independent
‘‘random’’ values? Then spreads will look as if drawn from, not a
member of the original family, but from an average of all the members
of the family where the averaging is over the relative frequencies of
the possible variances. In other words, the spread on day t is no
longer generated from F for a given σ but from the integrated
--- page 102 ---

Law of Reversion
75
distribution:
FP(p) =

Fσ(p)dσ
For example, suppose that the family of variance conditional distributions is the normal family (with constant mean in this context)
and that the variances occur randomly as if generated from an
inverse gamma distribution; then spreads will look as if they were
generated by the Student t distribution. The key to the result
is the random element; it guarantees (probabilistically) that the
daily transitions look as if the underlying spread model is Student
t. (This point is expanded upon in Section 4.5 where a similar argument proves the result for arbitrarily different generating
distributions day-to-day. An extended discussion of the relationship of marginal distribution to a time series of values is given
in Chapter 5.)
We can therefore state that the 75 percent rule is true in the case
of inhomogeneous variance sequences.
Note that the distributions for spread (conditional on variance)
and for (unconditional) variance need not be of mathematically
convenient forms as used in the previous example. Any regular
(‘‘well behaved,’’ in terms of continuity) distributions will yield
the 75 percent result. There is no requirement for the density or
distribution function to be expressed in a closed form mathematical
expression.
4.3.1
Volatility Bursts
Autoregressive conditional heteroscedastic (ARCH) models (Engle,
1982) were introduced to capture the observed clustering of variances
in macro economic data. In the past few years ARCH and GARCH
models have been heavily used in the econometric and ﬁnance literature, the latter because of the oft remarked phenomenon of volatility
bursts. Most such bursts are of increased volatility from a regular
level, typically associated with bad news about a company. Historically, bursts of low volatility are less frequently experienced. Since
early 2003, however, volatility of stocks on the U.S. exchanges has
been declining. Spread volatility reached unprecedented lows in 2003
--- page 103 ---

76
STATISTICAL ARBITRAGE
and 2004; implications of that development for statistical arbitrage
are examined in Chapter 9.
When volatility exhibits bursts, variances are not generated independently each day but exhibit serial correlation. The 75 percent rule
still holds by this argument: Within a burst, the theorem applies as if
the situation were (approximately) constant variance. Therefore, only
the transition days could alter the result. There are comparatively
few such days, so the result will stand to a very close approximation.
In fact, the result can be shown to hold exactly: The transitions
are irrelevant—see the argument in Section 4.5 for the general
nonconstant variance case. Chapter 5 presents analysis of related
patterns.
4.3.2
Numerical Illustration
Figure 4.2(a) shows the histogram of a sample of 1,000 values
generated from the normal–inverse Gamma scheme:
σ 2
t ∼IG[a, b],
Pt ∼N[0, σ 2
t ]
First, generate an independent drawing of σ 2
t from the inverse Gamma
distribution (with parameters a and b—the actual speciﬁcation of a
(a)
−3
−2
−1
0
1
0.0
0.5
1.0
1.5
Prices from normal-inverse gamma model; T_5 superimposed
(b)
0
200
400
600
800
1000
−3
−2
−1
0
1
FIGURE 4.2
Random sample from normal–inverse Gamma model
--- page 104 ---

Law of Reversion
77
and b does not matter: Any nonnegative values will do). Then, using
this value of σ 2
t , generate a value for Pt from the normal distribution
with mean 0 and variance σ 2
t . Superimposed on the histogram is the
density function of the Student t distribution, which is the theoretical
marginal distribution of spreads here. Figure 4.2(b) shows the sample
as a time series.
The proportion of one-day moves in the direction of the median
is 75.37 percent, satisfyingly in accord with the rule.
4.4
FIRST-ORDER SERIAL CORRELATION
The result can be extended to the case of correlated variables. The
simplest case to consider is that of distributions with symmetric density functions, since then the contours are circles (uncorrelated) or
ellipses (correlated). In the latter case, one can see that by dividing
up ℜ2 into quadrants along the major and minor axes of the contours, then bisecting those quadrants radially from the joint median
point as previously, one is left with equiprobable regions once again.
(Recall that, with symmetric densities, all quadrants are probablistically bisected this way, not just those corresponding to the lower left
and upper right in the rotated coordinates.) The remaining task is
to identify the half quadrants with a correct statement (like the one
with which the original result was stated) in terms of the random
quantities. The result is easily seen by example. Suppose that Pt and
Pt−1 have covariance c. Deﬁne a new variable as a linear combination of the correlated variables, Zt = a(Pt −rPt−1). The coefﬁcient r
is set to:
r = cov[Pt, Pt−1]
var[Pt−1]
(which is just the correlation between Pt and Pt−1) in order to make
Pt−1 and Zt uncorrelated; the scale factor a is chosen to make the
variance of Zt equal to the variance of Pt:
a = (1 −r2)−1
2
Now the theorem applies to Pt−1 and Zt providing that Zt has the
same distribution as Pt−1, so that we have:
Pr[(Zt < Pt−1 ∩Pt−1 > m) ∪(Zt > Pt−1 ∩Pt−1 < m)] = 0.75
--- page 105 ---

78
STATISTICAL ARBITRAGE
Substituting for Zt converts the expression into a form involving the
original variables:
Pr[(aPt −arPt−1 > Pt−1 ∩Pt−1 > m)
∪(aPt −arPt−1 > Pt−1 ∩Pt−1 < m)] = 0.75
Rearrangement of terms gives the required expression:
Pr[(Pt < (a−1 + r)Pt−1 ∩Pt−1 > m)
∪(Pt > (a−1 + r)Pt−1 ∩Pt−1 < m)] = 0.75
Clearly, the case of zero correlation, equivalently r = 0 and a = 1,
with which we began is a special case of this more general result.
The boundary, Pt = (a−1 + r)Pt−1, partitions the quadrants of
ℜ2 in proportions determined by the size of the correlation. In the
uncorrelated case, the quadrants are bisected as we saw earlier.
Figure 4.3 shows the relationship of a−1 + r =
√
1 −r2 + r with r.
The maximum,
√
2, occurs at r =

1
2 (easily shown analytically by
the usual procedure of differentiating, equating to zero, and solving).
r
−1.0
−0.5
0.0
0.5
1.0
−1.0
−0.5
0.0
0.5
1.0
1.5
(1 − r2) + r
FIGURE 4.3
r versus

(1 −r2) + r
--- page 106 ---

Law of Reversion
79
It is important not to lose sight of the additional constraint
introduced in the argument here. The theorem applies to correlated
variables providing that a linear combination of variables with the
stated marginal distribution retains that distributional form. This is
true of normal variables, bivariate Student t variables, and lots of
others. But it is not true in general.
At the limit when Pt and Pt−1 are perfectly correlated (r →1, a →
∞) the result breaks down. Failure is caused by the singularity as the
original two degrees of freedom (two distinct days or observations)
collapse into a single degree of freedom (two days constrained to
have the same price so the reversion statement of the theorem is
impossible).
4.4.1
Analytic Proof
The frequency of one-day moves in the direction of the median is
given by the probability:
Pr[(Pt < Pt−1 ∩Pt−1 > m) ∪(Pt > Pt−1 ∩Pt−1 < m)]
Consider the ﬁrst part of the disjunction:
Pr[Pt <Pt−1 ∩Pt−1>m] =
 ∞
m
Pr[Pt < Pt−1 ∩Pt−1 = p]dp
=
 ∞
m
Pr[Pt<Pt−1|Pt−1 = p]Pr[Pt−1 = p]dp
=
 ∞
m
Pr[Pt < p|Pt−1 = p] Pr[Pt−1 = p]dp
Notation is abused here to emphasize the logic. For continuous
quantities, it is not correct to write Pr[Pt−1 = p] since the probability
of the quantity taking on any speciﬁc value is zero. The correct
expression is the density function evaluated at p:
Pr[Pt < Pt−1 ∩Pt−1 > m] =
 ∞
m
Pr[Pt < p|Pt−1 = p]f(p)dp
Note that the conditional cumulative probability (ﬁrst term) reduces
to the unconditional value Pr[Pt < p] when Pt and Pt−1 are independent, the case considered in Section 4.2.
--- page 107 ---

80
STATISTICAL ARBITRAGE
In order to simplify notation in the remaining derivation of the
result, let X denote Pt and Y denote Pt−1. Then the probability of
interest is:
Pr[X < Y ∩Y > m] =
 ∞
m
Pr[X < p|Y = p]f(p)dp
Expand the conditional cumulative probability Pr[X < p|Y = p] into
the integral of the conditional density to obtain fX|Y(p) = Pr[X = x
|Y = p]:
Pr[X < Y ∩Y > m] =
 ∞
m
 p
−∞
fX|Y(x)dxf(p)dp
=
 ∞
m
 p
−∞
fX|Y(x)f(p)dxdp
=
 ∞
m
 p
−∞
fXY(x, p)dxdp
where f XY(. . .) denotes the joint density function of X and Y.
Now, using:
 ∞
m
 ∞
−∞
fXY(x,p)dxdp = 1
2
(since the inner integral reduces to the marginal density of X and, by
deﬁnition of the median, the outer integral is then precisely one half),
and noting that:
 ∞
m
 ∞
−∞
fXY(x, p)dxdp =
 ∞
m
 p
−∞
fXY(x, p)dxdp
+
 ∞
m
 ∞
p
fXY(x, p)dxdp
it follows immediately that:
 ∞
m
 p
−∞
fXY(x, p)dxdp = 1
2 −
 ∞
m
 ∞
p
fXY(x, p)dxdp
--- page 108 ---

Law of Reversion
81
This may seem like an irrelevant diversion but, in fact, it takes the
proof to within two steps of completion. At this point, we invoke the
symmetry of the joint density (which follows from the assumption of
identical marginal distributions). Formally, an expression of symmetry is:
 ∞
m
 p
m
fXY(x, p)dxdp =
 ∞
m
 x
m
fXY(x, p)dpdx
Now, reversing the order of integration (be careful to watch the
integral limits) yields the algebraic equivalence:
 ∞
m
 x
m
fXY(x, p)dpdx =
 ∞
m
 ∞
p
fXY(x, p)dxdp
Therefore:
 ∞
m
 p
m
fXY(x, p)dxdp =
 ∞
m
 ∞
p
fXY(x, p)dxdp
Penultimately, note that the sum of the latter two integrals is one
quarter (again, by deﬁnition of the median):
 ∞
m
 p
m
fXY(x, p)dxdp +
 ∞
m
 ∞
p
fXY(x, p)dxdp
=
 ∞
m
 ∞
m
fXY(x, p)dxdp = 1
4
And so:
 ∞
m
 p
−∞
fXY(x, p)dxdp = 1
2 −
 ∞
m
 ∞
p
fXY(x, p)dxdp
= 1
2 −1
2
1
4

= 3
8
The argument is similar for the second part of the disjunction.
--- page 109 ---

82
STATISTICAL ARBITRAGE
(a)
−4
−2
0
2
4
0
100
200
(b)
0
200
400
600
800
1,000
−4
0
2
4
FIGURE 4.4
Random sample from autocorrelated model
4.4.2
Examples
Example 1
One thousand terms were generated from a ﬁrst-order
autoregressive model with serial correlation parameter r = 0.71 (see
Figure 4.3 and the ﬁnal remarks in Section 4.4 regarding this choice)
and normally distributed random terms. Figure 4.4(b) shows the time
plot; Figure 4.4(a) shows the sample marginal distribution.
The proportion of reversionary moves exhibited by the series is
62 percent.
Adding a little more realism, we compute an estimate of the
median treating the series as if it were observed day by day. Analysis
of the local median adjusted series (using window length of 10) is
illustrated in Figure 4.5. A slightly greater proportion of reversionary
moves is exhibited by the adjusted series, 65 percent.
4.5
NONCONSTANT DISTRIBUTIONS
Suppose that spreads are generated from a normal distribution for
100 days, followed by a uniform distribution for 50 days. Within
each period the basic theorem is applicable; therefore, with one
exception in 150 days the 75 percent rule is true. Suppose that on the
one hundred ﬁfty-ﬁrst day, price range is generated from the normal
distribution once again. What can we say?
--- page 110 ---

Law of Reversion
83
−4
−2
0
2
4
−4
−2
0
2
4
(a)
0
100
200
300
(b)
0
200
400
600
800
1,000
FIGURE 4.5
Random sample from autocorrelated model, locally median adjusted:
(a) histogram (b) time series
Unequivocally we can say that the 75 percent rule is true on
average throughout the series. The crux of the proof is the two
transition days: (1) from normal to uniform, and (2) from uniform
to normal. Recall Figure 4.2. Region 1 is probabilistically bounded
by 0 < Pr[(1)] < 1
4 for random quantities from any two continuous,
independent distributions (by which it is meant that the probability
Pr[(1)] = Pr[(Pt, Pt−1) ∈(1)]). This follows from the deﬁnition of the
median as stated in Section 4.2. Denote this probability by p. Now,
the complement of region 1 in the quadrant therefore has probability
1
4 −p (with the same kind of meaning attached to ‘‘probability of a
region’’ as previously). The transitions are the key because only when
the distribution changes is the basic result in question. Indeed, it is
not hard to show that the result does not hold. For each transition
where p > 1
8 (normal to uniform is a case in point) the theorem result
is not 75 percent but 100(1 −2p)% < 75%. However, for each
such transition, the reverse transition exhibits the complementary
probability 1
4 −p for region 1.
Similar analysis applies to region 2. And this is true irrespective
of whether the probability of region 2 is the same as the probability
of region 1—which it is not if one or the other of the distributions is
asymmetric.
Thus, if transitions occur in pairs, the exhibited probability is the
average and, hence, the 75 percent result resurfaces. (If both densities
--- page 111 ---

84
STATISTICAL ARBITRAGE
0
50
100
150
200
250
300
−5
0
5
10
FIGURE 4.6
Random sample from mixed normal, lognormal, and Student t
distributions
are symmetric, then the ‘‘pairs’’ condition is sufﬁcient. However, if
at least one density is asymmetric, so that Pr[(1)]̸ = Pr[(2)], then the
pairs must occur often enough to statistically guarantee that there
are few pairs in region 1–2 compared to 1–1 or 2–2.)
One can push the argument further to prove the case for three
alternative distributions, the key caveat being that each of the three
distinct pairwise transitions occur equally often in both directions.
An appeal to mathematical induction then completes the proof for
an arbitrary number of alternative distributions.
4.6
APPLICABILITY OF THE RESULT
After several pages of theoretical development, it is a good idea to
pause and ask, ‘‘What is the relevance to model-based stock trading?’’ A major starting assumption is stationarity—a conveniently
unaddressed, unmentioned in fact, thus far. We required spreads to
be ‘‘independent, identically distributed’’ (later relaxing the conditions to allow for serial correlation); implicit therein in a time series
context is stationarity.
--- page 112 ---

Law of Reversion
85
Now stock price series are not stationary. What about spreads?
They are typically not stationary either. However, dynamically
adjusted for local estimates of location and variance, a reasonable
approximation to stationarity can be made. There is a link here to the
idea of cointegration (see Chapter 3). It may be difﬁcult to uncover
structure in individual price series but the difference between series
(spreads) more readily yields predictable relationships. Extending the
basic notion of cointegration to locally deﬁned series (we might use
the nomenclature ‘‘locally cointegrated’’) identiﬁes the link.
It is in this spirit of informed, dynamic approximation that the
theoretical result has guiding validity.
4.7
APPLICATION TO U.S. BOND FUTURES
The theorem presented in this chapter, while motivated by the discussion of spreads between stock prices of similar companies (the
classic pair of a pairs trade), is applicable with much greater generality. As long as the conditions on the ‘‘price’’ series are reasonably
met, the theorem applies to any ﬁnancial instrument. Of course, the
rub is in the meeting of the conditions—many series do not (without more attention to the structural development over time—trend
developments for example). Bond prices do show a good ﬁt to the
theorem.
U.S. 30-year Treasury bond futures were studied with the simple forecasting model for changes in daily high–low price range.
The front future contract, being the most liquid, was examined.
(Because of concern about possible distortions arising from contract
expirations, the study was repeated with contract rollover at 15
business days prior to expiration of the front future. No distortions
were observed in the analysis, hence the results of the vanilla series
are reported.) Figure 4.7 shows the sample distribution of the data
for 1990–1994 used in the study—a strong skew is evident in the
distribution. A time plot of the series is given in Figure 4.8.
In the prediction model, the median value was estimated each
day using data for the preceding 20 business days. Operationally,
this local median calculation is desirable to minimize the effects of
evolutionary change. One of the beneﬁts is a reduction in serial
correlation: The raw series (equivalent to using a constant median)
--- page 113 ---

86
STATISTICAL ARBITRAGE
0
1
2
3
0
100
200
300
FIGURE 4.7
Marginal distribution of high–low range of front U.S. 30-year bond
future
TABLE 4.1
Empirical study of U.S. 30-year bonds
Proportion
Proportion
Proportion
Year
Pt > Pt−1 | Pt−1 < m
Pt < Pt−1 | Pt−1 > m
Overall
1990
70%
75%
73%
1991
77%
72%
74%
1992
78%
76%
77%
1993
78%
76%
77%
1994
78%
76%
77%
All
77%
75%
76%
Note: 250 trading days per year
exhibits autocorrelations in the range [0.15, 0.2] for many lags; the
local median adjusted series exhibits no signiﬁcant autocorrelations.
Results of the forecasting exercise are presented in Table 4.1:
They are quite consistent with the theorem.
The result conﬁrmed by bond future prices is economically
exploitable. Some sophistication is required in the nature of the
implementation of the trading rule, particularly with respect to
managing trading costs, but there are many possibilities.
--- page 114 ---

Law of Reversion
87
0.5
1.0
1.5
2.0
2.5
3.0
3.5
900102
910102
920102
930104
940103
941220
$
FIGURE 4.8
Daily high–low range of front U.S. 30-year bond future
4.8
SUMMARY
The implication of the theorem statement is a little provocative: The
75 percent forecast accuracy is guaranteed only if the conditions of
the theorem are met. In practice, the evidence is that many stock prices
and spreads do meet the conditions approximately over short periods.
Moreover, the rate of change, when change occurs, is often sufﬁciently
slow that a properly calibrated, dynamic model (local characterization of the mean in the examples examined in this chapter) exhibits
reversion results similar to the theoretical prediction.
Empirical evidence for U.S. 30-year Treasury bonds suggests that
this market, also, comes close to meeting the conditions. Certainly
the accuracy of the empirical model is not demonstrably different
from 75 percent for the ﬁve years 1990–1994. With a little ingenuity,
many situations seemingly violating the conditions of the theorem
can be made to approximate them quite closely.
Appendix 4.1:
LOOKING SEVERAL DAYS AHEAD
Assuming no persistent directional movement (trending), as we have
been doing in the theoretical development and proxying by local
--- page 115 ---

88
STATISTICAL ARBITRAGE
n
p75
0
5
10
15
20
0.0
0.2
0.4
0.6
0.8
1.0
p = 0.75
p = 0.25
p = 0.35
p = 0.5
FIGURE 4.9
Probability of at least 1 ‘‘winning move’’ in next n days
location adjustment in the applications, there is obviously greater
opportunity for reversion if more than one day ahead may be
considered. Of course, it is crucial that each day in the k-day period
ahead can be looked at individually; if one may only look at k-day
movements, then the situation is essentially unchanged from the
one-day case. When each day may be considered, there are multiple
(independent) chances of a win (a reversion), so the probability of a
win increases.
Figure 4.9 shows the probability of a move from the current
position in the direction of the median occurring within the next k
days for k = 1, . . . , 20. The probability of such a move occurring in
one day is 0.75 from the theorem. The other probabilities are calculated from the binomial distribution as described next. The ﬁgure
also includes graphs assuming a winning probability of 0.25, 0.35,
and 0.5: In practice, a lower value than 0.75 will be observed under
the best circumstances because of theorem assumption violations.
By assumption, prices are independent each day. The theorem
states that the probability of a reversionary move from the current
position is 0.75 for any day. So, the probability of a reversionary
move from the price on day t is 0.75 for day t + 1, for day t + 2
