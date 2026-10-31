# The Kelly capital growth investment criterion _ theory and -- Leonard C_ Maclean, Edward O_ Thorp, W_ T_ Ziemba, Leonard -- World Scientific Handbook -- isbn13 9781283148344 -- bec576e26410d0c695fd5b867d08ec4f -- An.pdf — pages 837–856

--- page 837 ---

808
E. O. Thorp
404
E.O. Thorp
In the special case PI = P2 = p, d = 0 and 1* = it = f; = e/2 = (p - q)/
(2(p2 + q2». Letting m = p - q this may be written 1* = m/(l + m2) as the optimal
fraction to bet on each coin simultaneously, compared to f* = m to bet on each coin
sequentially.
Our simultaneous sports bets were generally on different games and typically not
numerous so they were approximately independent and the appropriate fractions were
only moderately less than the corresponding single bet fractions. Question: Is this always true for independent simultaneous bets? Simultaneous bets on blackjack hands at
different tables are independent but at the same table they have a pairwise correlation
that has been estimated at .5 (Griffin, 1979, p. 142). This should substantially reduce
the Kelly fraction per hand. The blackjack literature discusses approximations to these
problems. On the other hand, correlations between the returns on securities can range
from nearly -1 to nearly 1. An extreme correlation often can be exploited to great
advantage through the techniques of "hedging". The risk averse investor may be able
to acquire combinations of securities where the expectations add and the risks tend to
cancel. The optimal betting fraction may be very large.
The next example is a simple illustration of the important effect of covariance on the
optimal betting fraction.
Example 6.2. We have two' favorable coins as in the previous example but now their
outcomes need not be independent. For simplicity assume the special case where the
two bets have the same payoff distributions, but with ajoint distribution as in Table 4.
Now c+m +b = (l +m)/2 so b = (l-m)/2 -c and therefore 0 ::;; e ::;; (l-m)/2.
Calculation shows Var(Xi) = 1 -
m 2, Cor(XI, X2) = 4c -
(1 -
m)2 and
Cor(XI, X2) = [4c -
(1 - m)2]/(l - m2). The symmetry of the distribution shows
that g(fl, h) will have its maximum at fl :;= h = f so we simply need to maximize
g(f) = (c + m) In(1 + 2f) + e In(l - 2f). The result is 1* = m/(2(2c + m». We
see that for m fixed, as c decreases from (l - m)/2 and cor(X I , X2) = 1, to 0 and
cor(X I, X2) = -(1 - m)/(1 + m), 1* for each bet increases from m/2 to 1/2, as in
Table 5.
Table 4
Joint distribution of two "identical" favorable coins with correlated outcomes
XI:
X2: I
-I
C+1I1
h
-I
b
c
Table 5
I* increases as Cor( X I . X 2) decreases
Cor(XI. X2)
C
I*
(I - m) / 2
111/ 2
0
(I -
/112)/ 4
111 / (1 +111 2 )
-(I -
111) / (1 + 111)
0
1/2
--- page 838 ---

The Kelly Criterion in Blackjack Sports Betting, and the Stock Market
809
('II. 9:
The Kelly Criterion in Blackjack Sports Betting, and the Stock Market
405
It is important to note that for an exact solution or an arbitrarily accurate numerical
approximation to the simultaneous bet problem, covariance or correlation information
is not enough. We need to use the entire joint distribution to construct the g function.
We stopped sports betting after our successful test for reasons including:
(I) It required a person on site in Nevada.
(2) Large amounts of cash and winning tickets had to be transported between casinos.
We believed this was very risky. To the sorrow of others, subsequent events confirmed this.
(3) It was not economically competitive with our other operations.
If it becomes possible to place bets telephonically from out of state and to transfer
the corresponding funds electronically, we may be back.
7. Wall street: the biggest game
To illustrate both the Kelly criterion and the size of the securities markets, we return to
the study of the effects of correlation as in Example 6.2. Consider the more symmetric
and esthetically pleasing pair of bets VI and V2 , with joint distribution given in Table 6.
Clearly 0 :::;; a :::;; 1/ 2 and Cor( VI , V2) = Cor( V I, Vz:) = 4a -
I increases from
-1 to 1 as a increases from 0 to 1/ 2. Finding a general solution for (ft, 1;) appears
algebraically complicated (but specific solutions are easy to find numerically), which
is why we chose Example 6.2 instead. Even with reduction to the special case m 1 =
m2 = m and the use of symmetry to reduce the problem to finding f* = ft = f;,
a general solution is still much less simple. But consider the instance when a = 0 so
Cor(VI , V2) = -\. Then g(f) = In(l + 2m!) which increases without limit as f
increases. This pair of bets is a "sure thing" and one should bet as much as possible.
This is a simplified version of the classic arbitrage of securities markets: find a pair
of securities which are identical or "equivalent" and trade at disparate prices. Buy the
relatively underpric~d security and sell short the relatively overpriced security, achieving a correlation of -I and "locking in" a riskless profit. An example occurred in 1983.
My investment partnership bought $ 330 million worth of "old" AT&T and sold short
$332.5 million worth of when-issued "new" AT&T plus the new "seven sisters" regional
telephone companies. Much of this was done in a single trade as part of what was then
the largest dollar value block trade ever done on the New York Stock Exchange (December 1, 1983).
In applying the Kelly criterion to the securities markets, we meet new analytic problems. A bet on a security typically has many outcomes rather than just a few, as in
11/1 +
1
11/1 -I
Table 6
Joint distribution of VI and V2
(/
1/ 2 -
({
11/ 2 -
1
1/ 2 -
({
({
--- page 839 ---

810
E. O. Thorp
406
E.O. Thorp
most gambling situations. This leads to the use of continuous instead of discrete probability distributions. We are led to find f to maximize g(f) = E In(l + f X) =
f In(l + fx) dP(x) where P(x) is a probability measure describing the outcomes. Frequently the problem is to find an optimum portfolio from among n securities, where
n may be a "large" number. In this case x and fare n-dimension vectors and f x is
their scalar product. We also have constraints. We always need I + fx > 0 so In( . ) is
defined, and L fi = I (or some c > 0) to normalize to a unit (or to a c > 0) investment. The maximization problem is generally solvable because g(f) is concave. There
may be other constraints as well for some or all i such as fi ~ 0 (no short selling), or
fi ~ Mi or fi ~ mi (limits amount invested in ith security), or L Ifi! ~ M (limits
total leverage to meet margin regulations or capital requirements). Note that in some
instances there is not enough of a good bet or investment to allow betting the full f* , so
one is forced to underbet, reducing somewhat both the overall growth rate and the risk.
This is more a problem in the gaming world than in the much larger securities markets.
More on these problems and techniques may be found in the literature.
7.1. Continuous approximation
There is one technique which leads rapidly to interesting results. Let X be a random
variable with P(X = m + s) = P(X = m -
5) = .5. Then E(X) = m, Var(X) = 52.
With initial capital Vo, betting fraction f, and return per unit of X, the result is
V(f) = Vo(1 + (I - f)r + f X) = Vo(1 + r + f(X - r»),
where r is the rate of return on the remaining capital, invested in, e.g., Treasury bills.
Then
g(f) = E(G(f») = E(ln(V(f)1 Vo)) = E In(1 + r + f(X - r»)
= .5In(1 + r + f(m - r + s») + .5In(1 + r + f(m - r - s»).
Now subdivide the time interval into n equal independent steps, keeping the same drift
and the same total variance. Thus m, 52 and r are replaced by min, 52 I nand r I n,
respectively. We have n independent Xi, i = I , .. . , n, with
P(Xi =mln + sn- I / 2) = P(Xi = min - sn- I / 2) = .5.
Then
II
V,,(f)IVo = n(1 + (I - f)r + fXi).
i=1
Taking E(log(·» of both sides gives g(f). Expanding the result in a power series leads
to
(7.1 )
where 0(n - I / 2) has the property n 1/20(n - I/ 2) is bounded as n ~ 00. Letting n ~ 00
in (7.1) we have
goo(f) == r + f(m - r) -
s2 f2 /2 .
(7.2)
--- page 840 ---

The Kelly Criterion in Blackjack Sports Betting, and the Stock Market
811
('iI. 9:
The Kelly Criterion in Blackjack Sports Betting, and the Stock Market
407
The limit V == V 00 (f) of Vii (f) as n ---+ 00 corresponds to a log normal diffusion
process, which is a well-known model for securities prices. The "security" here has
instantaneous drift rate m, variance rate s2, and the riskless investment of "cash" earns
at an instantaneous rate r. Then goo (f) in (7.2) is the (instantaneous) growth rate of
capital with investment or betting fraction f. There is nothing special about our choice
of the random variable X. Any bounded random variable with mean E(X) = m and
variance Var(X) = s2 will lead to the same result. Note that f no longer needs to
he less than or equal to 1. The usual problems, with log(·) being undefined for negative
arguments, have disappeared. Also, f < 0 causes no problems. This simply corresponds
to selling the security short. If m < r this could be advantageous. Note further that the
investor who follows the policy f must now adjust his investment "instantaneously".
In practice this means adjusting in tiny increments whenever there is a small change
in V. This idealization appears in option theory. It is well known and does not prevent
the practical application of the theory (Black and Scholes, 1973). Our previous growth
functions for finite sized betting steps were approximately parabolic in a neighborhood
of f* and often in a range up to 0 ~ f
~ 2f*, where also often 2f* == t. Now with
the limiting case (7.2), goo (f) is exactly parabolic and very easy to study.
Lognormality of V (f) / Vo means 10g(V (n / Vo) is N (M, 52) distributed, with mean
M = goo(nt and variance 52 = Var(Goo(f)t for any time t. From this we can determine, for instance, the expected capital growth and the time tk required for V (f)
to be at least k standard deviations above Vo. First, we can show by our previous
methods that Var(Goo(f» = s2 f2, hence Sdev(Goo(f» = sf. Solving tkgoo =
kt} /2 Sdev(Goo(f» gives tkg~ hence the expected capital growth tkgoo, from which
we find tk. The results are summarized in Equations (7.3).
f* = (m - r)/s2,
goo(f) = r + f(m - r) - s2 f2 /2,
goo(f*) = (m - r)2/2s2 + r,
Var(Goo(f») = s2 f2,
Sdev(Goo(f») = sf,
tkgoo(f) = k2s2 f2 / goo,
tk = k2s2 12 / g~.
(7.3)
Examination of the expressions for tk goo (f) and tk show that each one increases as f
increases, for 0 ~ 1 < 1+ where f + is the positive root of s2 f2 /2 - (m - r) 1 - r = 0
and 1+ > 2f*.
Comment: The capital asset pricing model (CAPM) says that the market portfolio
lies on the Markowitz efficient frontier E in the (s, m) plane at a (generally) unique
point P = (so, mo) such that the line determined by P and (s = 0, m = r) is tangent
to E (at P). The slope of this line is the Sharpe ratio 5 = (mo -
ro)/so and from (7.3)
Koo(f*) = 52/2 + r so the maximum growth rate goo(f*) depends, for fixed r, only
on the Sharpe ratio. (See Quaife (1995).) Again from (7.3), f* = 1 when m = r + s2
in which case the Kelly investor will select the market portfolio without borrowing or
lending. If m > r + s2 the Kelly investor will use leverage and if m < r + s2 he will
--- page 841 ---

812
E. 0. Thorp
408
E.O. Tho!])
invest partly in T-bills and partly in the market portfolio. Thus the Kelly investor will
dynamically reallocate as f* changes over time because of fluctuations in the forecast
m, rand s2, as well as in the prices of the portfolio securities.
From (7.3), goo(1) = m -
s2/2 so the portfolios in the (s, m) plane satisfying
m - s2/2 = C, where C is a constant, all have the same growth rate. In the continuous approximation, the Kelly investor appears to have the utility function U (s, m) =
m - s2/2. Thus, for any (closed, bounded) set of portfolios, the best portfolios are exactly those in the subset that maximizes the one parameter family m - s2/2 = C. See
Kritzman (1998), for an elementary introduction to related ideas.
Example 7.1. The long run revisited. For this example let r = O. Then the basic equations (7.3) simplify to
r = 0: 1* = m/s2 ,
goo(f) = mf - s2 f2/2,
goo(f*) = m 2/2s2,
Var(G oo(f») = s2 f2,
Sdev(Goo(f») = sf.
(7.4)
How long will it take for V (f*) ~ Vo with a specified probability? How about
V (f* /2)? To find the time t needed for V (f) ~ Vo at the k standard deviations level of
significance (k = I, P = 84%; k = 2, P = 98%, etc.) we solve for t == tk:
(7.5)
We get more insight by normalizing all f with f* · Setting f = c f* throughout, we
find when r = 0
r = 0:
f* == m/s2 ,
f = em/s2 ,
goo(c1*) = m 2(c - c2/2)/s 2 ,
Sdev(Goo(c1*») = cm/s,
tgoo (c1*) = k 2e/(1 - e/2),
t(k,ef*) =k2s2/{m 2(1_e/2)2).
(7.6)
Equations (7.6) contain a remarkable result: V (f) ~ Vo at the k standard deviation
level of significance occurs when expected capital growth tgoo = k 2e/(1 -
e/2) and
this result is independent of m and s. For f = f* (e = 1 in (7.6», this happens for
k = I at tgoo = 2 corresponding to V = Voe2 and at k = 2 for tgoo = 8 corresponding
to V = Voe8. Now e8 === 2981 and at a 10% annual (instantaneous) growth rate, it takes
80 years to have a probability of 98% for V ~ Yo. At a 20% annual instantaneous rate it
takes 40 years. However, for f = f* /2, the number for k = I and 2 are tgoo = 2/3 and
8/3, respectively, just 1/3 as large. So the waiting times for Prob(V ~ Yo) to exceed
84% and 98% become 6.7 years and 26.7 years, respectively, and the expected growth
rate is reduced to 3/4 of that for f*.
--- page 842 ---

The Kelly Criterion in Blackjack Sports Betting, and the Stock Market
813
('iI. 9:
The Kelly Criterion in Blackjack Sports Betting, and the Stock Marker
409
Comment: Fractional Kelly versus Kelly when r = 0
From Equations (7,6) we see that goo(cf*)/goo(f*) = c(2 -
c), 0 ~ c < 00,
showing how the growth rate relative to the maximum varies with c, The relative risk
Sdev(Goo(cf*»/Sdev(Goo(f*» = c and the relative time to achieve the same expected total growth is 1/c(2 - c), 0 < c < 2, Thus the relative "spread" for the same
expected total growth is 1/(2 - c), 0 < c < 2. Thus, even by choosing c very small, the
spread around a given expected growth cannot be reduced by 1/2, The cOlTesponding
results are not quite as simple when r > O.
7.2. The (almost) real world
Assume that prices change "continuously" (no "jumps"), that portfolios may be revised
"continuously", and that there are no transactions costs (market impact, commissions,
"overhead"), or taxes (Federal, State, city, exchange, etc.). Then our previous model
applies.
Example 7.2. The S&P 500 Index. Using historical data we make the rough estimates
111 = .11, s = .15, r = .06. The equations we need for r =1= 0 are the generalizations
of (7.6) to r =1= 0 and f = cf*, which follow from (7.3):
cf* = c(m - r)/s2,
goo(cf*) = (m - r)2(c - c2/2))/s2 + r,
Sdev(Goo(cf*») = c(m - r)/s,
tgoo(cf*) = k2c2/(c - c2/2 + rs2/(m - r)2) ,
t(k, cf*) = k2c2( (m - r)2 /s2) / (({m - r)2/s2)(c - c2/2) + r (
(7.7)
If we define iii = m - r, Goo = Goo - r, goo = goo -
r, then substitution into
Equations (7.7) give Equations (7.6), showing the relation between the two sets. It also
shows that examples and conclusions about P (Vn > Vo) in the r = 0 case are equivalent
to those about P(ln(V(t)/Vo) > rt) in the r =1= 0 case. Thus we can compare various
strategies versus an investment compounding at a constant riskless rate r such as zero
coupon U.S. Treasury bonds.
'
From Equations (7.7) and c = 1, we find
f* = 2.22,
goo(f*) = .115,
Sdev( Goo(f*») = .33,
t = 8.32k2 years.
Thus, with f* = 2.22, after 8.32 years the probability is 84% that VII > Vo and
the expected value of loge VII / Vo) = .96 so the median value of VII / Vo will be about
£, . ,96 = 2.61.
With the usual unlevered f = 1, and c = .45, we find using (7.3)
goo(1) = m - s2/2 = .09875,
Sdev( Goo(l») = .15,
t(k, .45f*) = 2.31k2 years.
--- page 843 ---

814
E. 0. Thorp
410
E.O. Thorp
Writing tgoo = h(c) in (7.7) as
we see that the measure of riskiness, h(c), increases as c increases, at least up to the
point c = 2, corresponding to 2f* (and actually beyond, up to 1 + 1 + (1/:~~. )1 ).
Writing t(k, c1*) = t(c) as
t(c) = k2«m - r)2/s2)/(m - r)2/s2)(l - c/2) + r/c2
shows that t(c) also increases as c increases, at least up to the point c = 2. Thus for
smaller (more conservative) f
= cf*, c ( 2, specified levels of P(VI/ > Vo) are
reached earlier. For c < 1, this comes with a reduction in growth rate, which reduction
is relatively small for f near 1*.
Note: During the period 1975-1997 the short term T-bill total return for the year,
a proxy for r if the investor lends (i.e., f < 1), varied from a low of 2.90% (1993)
to a high of 14.71 % (1981). For details, see Ibbotson Associates, 1998 (or any later)
Yearbook.
A large well connected investor might be able to borrow at broker's call plus about
1 %, which might be approximated by T-bills plus I %. This might be a reasonable estimate for the investor who borrows (f > 1). For others the rates are likely to be higher.
For instance the prime rate from 1975-1997 varied from a low of 6% (1993) to a high
of 19% (1981), according to Associates First Capital Corporation (1998).
As r fluqtuates, we expect m to tend to fluctuate inversely (high interest rates tend
to depress stock prices for well known reasons). Accordingly, f* and goo will also
fluctuate so the 'long term S&P index fund investor needs a procedure for periodically
re-estimating and revising f* and his desired level of leverage or cash.
To illustrate the impact of r" > r, where r" is the investor's borrowing rate, suppose
r" in example (7.2) is r + 2% or .08, a choice based on the above cited historical values
for r, which is intermediate between "good" rt, ~ r + I %, and "poor" r" ~ the pri~e
rate ~ r + 3%. We replace r by rt, in Equations (7.7) and, if f* > I, f* = 1.33,
goo(f*) = .100, Sdev(Goo(f*» = .20, tgoo(f*) = .4k2, t = 4k2 years. Note how
greatly f* is reduced.
Comment: Taxes
Suppose for simplicity that aU gains are subject to a constant continuous tax rate T
and that all losses are subject to a constant continuous tax refund at the same rate T.
Think of the taxing entities, collectively, as a partner that shares a fraction T of all gains
and losses. Then Equations (7.7) become:
c1* = c(m - r) /s20 - T),
goo(c.t*) = (m - r)2(c - c2/2))/s2 + r( I - T),
Sdev(Goo(c.t*») = c(m - r)/s,
--- page 844 ---

The Kelly Criterion in Blackjack Sports Betting, and the Stock Market
815
( 'II. <J:
The Kelly Criterion in Blackjack Sports Betting, and the Stock Market
411
tgoo(cf*) = k2c2/ {c - c2/ 2 + r(1 - T)s2 / (m - r2)) ,
t(k, cf*) = k2c2((m - r)2/ s2)j{((m - r)2 / s2)(c - c2/2) +r(1- T)f
(7.7T)
It is interesting to see that cf* increases by the factor I/O - T) . For a high income
California resident, the combined state and federal marginal tax rate is 45% so this
ractor is 1/.55 = 1.82. The amplification of cf* leads to the same growth rate as before
exeept for a reduction by rT . The Sdev is unchanged and t (k, cf*) is increased slightly.
However, as a practical matter, the much higher leverage needed with a high tax rate
is typically not allowed under the margin regulation or is not advisable because the
inability to continuously adjust in the real world creates dangers that increase rapidly
with the degree of leverage.
7.3. The case for "fractional Kelly "
Figure 5 shows three g curves for the true m : mr = .5me, LOme and 1.5me, where
III,. is the estimated value of m. The vertical lines and the slanting arrows illustrate the
n:duction in g for the three choices of: f = .5 f e*' f e* and 1.5 f e* ' For example with
f = .5fe* or "half Kelly", we have no loss and achieve the maximum g = .25, in
case mr = .5me. But if mr = me then g = .75, a loss of .25 and if mr = 1.5me then
g = 1.25, a loss of 1.0, where all g are in units of m;/2s2. This is indicated both by
I.aSSl and LOSS2 on the vertical line above f / j~* = .5, and by the two corresponding
arrows which lead upward, and in this case to the right, from this line. A disaster occurs
when mr = .5me but we choose f = l.5 f e*' This combines overbetting f "* by 50%
with the overestimate of me = 2mr. Then g = -.75 and we will be ruined. It is still
had to choose f = f e* when mr = .5me for then g = 0 and we suffer increasingly wild
oscillations, both up and down, around our initial capitf\l. During a large downward
oscillation experience shows that bettors will generally either quit or be eliminated by a
minimum bet size requirement.
Some lessons here are:
( I) To the extent me is an uncertain estimate of mr, it is wise to assume m{ < me and
to choose f < f e* by enough to prevent g ~ O.
Estimates of me in the stock market have many uncertainties and, in cases of
forecast excess return, are more likely to be too high than too low. The tendency
is to regress towards the mean. Securities prices follow a "non-stationary process"
where m and s vary somewhat unpredictably over time. The economic situation can
change for companies, industries, or the economy as a whole. Systems that worked
may be partly or entirely based on data mining so m { may be substantially less
than me. Changes in the "rules" such as commissions, tax laws, margin regulations,
insider trading laws, etc., can also affect mr . Systems that do work attract capital,
which tends to push exceptional mt down towards average values. The drift down
means me > mr is likely.
--- page 845 ---

816
E. 0. Thorp
412
£.0. Thorp
g(f) unit ~ m'/2s'
PENALTY FOR EACH m, IFYOU CHOOSE THIS r
o Sf:
f:
1 Sf:
-- - r - -
T ---- r-
2.0
1.5
1.0
0.5
0.0 -+----+------'-:--__\! !}--'-----Ht-----..---+- If:
2:0
LOSS,
-0.5
- 1.0
- -- ----- --- -. - -- --
----.-.------ - --- --.- --- --.--
Fig_ 5_ Penalties for choosing f = j;, i- I* = ji.
Sports betting has much the same caveats as the securities markets, with its own
differences in detail. Rules changes, for instance, might include: adding expansion
teams; the three point rule in basketball; playing overtime sessions to break a tie;
changing types of bats, balls, gloves, racquets or surfaces.
Blackjack differs from the securities and sports betting markets in that the probabilities of outcomes can in principle generally be either calculated or simulated to
any desired degree of accuracy. But even here ml is likely to be at least somewhat
less than me. Consider player fatigue and errors, calculational errors and mistakes
in applying either blackjack theory or Kelly theory (e.g., calculating f* correctly,
for which some of the issues have been discussed above), effects of a fixed shuffle
point, non-random shuffling, preferential shuffling, cheating, etc.
(2) Subject to (I), choosing f in the range .5.ft; ~ f < f{; offers protection against
g ~ 0 with a reduction of g that is likely to be no more'than 25%.
--- page 846 ---

The Kelly Criterion in Blackjack Sports Betting, and the Stock Market
817
( '/1, <J:
The Kelly Criterion in Blackjack Sports Betting, and the Stock Market
4t3
Example 7.3. The great compounder, In 1964 a young hedge fund manager acquired a
\uhstantial interest in a small New England textile company called Berkshire Hathaway.
The stock traded then at 20. In 1998 it traded at 70,000, a multiple of 3500, and an annualized compound growth rate of about 27%, or an instantaneous rate of 24%. The once
young hedge fund manager Warren Buffett is now acknowledged as the greatest investor
or our time, and the world's second richest man. You may read about Buffett in Buffett
and Clark (1997), Hagstrom (1994, 2004), Kilpatrick (1994) and Lowenstein (1995). If,
as 1 was, you were fortunate enough to meet Buffett and identify the Berkshire opportunilY, what strategy does our method suggest? Assume (the somewhat smaller drift rate)
III = .20, s = .15, r = .06. Note: Plausible arguments for a smaller future drift rate
include regression towards the mean, the increasing size of Berkshire, and risk from the
aging of management. A counter-argument is that Berkshire's compounding rate has
heen as high in its later years as in its earlier years. However, the S&P 500 Index has
performed much better in recent years so the spread between the growth rates of the Index and of Berkshire has been somewhat less. So, if we expect the Index growth rate to
revert towards the historical mean, then we expect Berkshire to do so even more. From
Equations (7.3) or (7.7),
f* = 6.22,
goo(f*) = .495,
Sdev(Goo(f*») = .93,
t = 3.54k2 years.
Compare this to the unlevered portfolio, where f = 1 and c = 1/6.22 === .1607. We
lind:
f = 1,
goo(f) = .189,
Sdev( Goo (f) ) = .15,
tk = .63k2 years.
Leverage to the level 6.22 would be inadvisable here in the real world because securities prices may change suddenly and discontinuously. In the crash of October, 1987,
the S&P 500 index dropped 23% in a single day. If this happened at leverage of 2.0,
the new leverage would suddenly be 77 /27 = 2.85 before readjustment by selling part
of the portfolio. In the case of Berkshire, which is a large well-diversified portfolio,
suppose we chose the conservative f = 2.0. Note that this is the maximum initial leverage allowed "customers" under current regulations. Then goo(2) = .295. The values
in 30 years for median VXl/ Vo are approximately: f = I, Voo/ Vo = 288; f = 2,
V 00/ Vo = 6, 974; f = 6.22, V 00/ Vo = 2.86 X 106 . So the differences in results of
leveraging are enormous in a generation. (Note: Art Quaife reports s = .24 for 1980-
1997. The reader is invited to explore the example with this change.)
The results of Section 3 apply directly to this continuous approximation model of
a (possibly) leveraged securities portfolio. The reason is that both involve the same
"dynamics", namely log Gil (f) is approximated as (scaled) Brownian motion with drift.
So we can answer the same questions here for our portfolio that were answered in
Section 3 for casino betting. For instance (3.2) becomes
Prob(V (t)/ Vo ~ x for some t) = x'" (2goo/ Var(G oo»)
(7.8)
--- page 847 ---

818
E. O. Thorp
414
E.O. Thorp
where 1\ means exponentiation and 0 < x < 1. Using 0.4), for r = 0 and f = f* ,
2goo/Var(Goo ) = 1 so this simplifies to
ProbO = x.
0 ·9)
Compare with Example 3.3 For 0 < r < m and f = f* the exponent of x in (7.9)
becomes I + 2rs2/ (m - r)2 and has a positive first derivative so, as r increases, PO
decreases since 0 < x < 1, tending to 0 as r tends to m, which is what we expect.
7.4. A remarkable formula
In earlier versions of this chapter the exponent in Equations (3.2), 0 .8) and (7.9)
were off by a factor of 2, which I had inadvertently dropped during my derivation.
Subsequently Don Schlesinger posted (without details) two more general continuous
approximation formulas for the r = 0 case on the Internet at www.bjmath.com dated
June 19, 1997.
If Vo is the initial investment and y > I > x > 0 then for /* the probability that
V (t) reaches y Vo before x Vo is
Prob(V (t, f*) reaches y Vo before x Vo) = (I - x)/ (I - (x / y»)
(7.10)
and more generally, for f = cf*, 0 < c < 2,
Prob(V(t, cf*) reaches y VO before xVo)
= [I - / \(2 / c ~ 1)]/[1 - (x/y('(2/c - I)]
(7.11 )
where 1\ means exponentiation.
Clearly (7.10) follows from 0 .11) by choosing c = I. The r = 0 case of our
Equation (7.8) follows from 0 .11) and the r = 0 case of our Equation (7.9) follows
from (7.10). We can derive a generalization of (7.1 I) by using the classical gambler's
ruin formula (Cox and Miller, 1965, p. 31, Equation (2.0» and passing to the limit
as step size tends to zero (Cox and Miller, 1965, pp. 205-206), where we think of
10g(V(t, f)/ Vo) as following a diffusion process with mean goo and variance v(Goo),
initial value 0, and absorbing barriers at log y and log x . The result is
Prob(V(t, cf*) reaches yVO before xVo) = [I - x Aa]/[1 - (x/y) Aa]
(7.12)
where a = 2goo/ V (G (0) = 2M / V where M and V are the drift and variance, respectively, of the diffusion process per unit time. Alternatively, (7.12) is a simple restatement
of the known solution for the Wiener process with two absorbing barriers (Cox and
Miller, 1965, Example 5.5).
As Schlesinger notes, choosing x = 1/2 and y = 2 in (7.10) gives probe V (t , /*)
doubles before halving) = 2/3. Now consider a gambler or investor who focuses only
on values VII = 211 Vo. n = o. ± I. ±2, . . . , multiples of his initial capital. In log space,
loge VII / Vo) = n log 2 so we have a random walk on the integer multiples of log 2, where
--- page 848 ---

The Kelly Criterion in Blackjack Sports Betting, and the Stock Market
819
( "II ():
The Kelly Criterion in Blackjack Sports Betting, and the Stock Market
415
tlie probability of an increase is p = 2/3 and of a decrease, q = 1/3. This gives us a
l( lItvcnient compact visualization of the Kelly strategy's level of risk.
I f instead we choose c = 1/2 ("half Kelly"), Equation (7.11) gives probe V (t, !* /2)
douhles before halving) = 8/9 yet the growth rate goo(f* /2) = .75goo(f*) so "half
Kelly" has 3/4 the growth rate but much less chance of a big loss.
A second useful visualization of comparative risk comes from Equation (7.8) which
Prob(V(t,c!*)/Vo ::;;x forsomet) = xl\(2/c -l).
(7.13)
I'or c = 1 we had Prob(·) = x and for c = 1/2 we get Prob(·) = x 3. Thus "half
Kelly" has a much lessened likelihood of severe capital loss. The chance of ever losing
lialf the starting capital is 1/2 for f = !* but only 1/8 for f = !* /2. My gambling
alld investment experience, as well as reports from numerous blackjack players and
Il'ams, suggests that most people strongly prefer the increased safety and psychological
l'Olllfort of "half Kelly" (or some nearby value), in exchange for giving up 1/4 of their
gn lwth rate.
X. A case study
III the summer of 1997 the XYZ Corporation (pseudonym) received a substantial
alllount of cash. This prompted a review of its portfolio, which is shown in Table 7
i II the column 8/17/97. The portfolio was 54% in Biotime, ticker BTIM, a NASDAQ
hiotechnology company. This was due to existing and historical relationships between
people in XYZ Corp. and in BTIM. XYZ's officers and directors were very knowledge-
Monthly
Allllual
Monthly
Monthly
Table 7
Statistics for logs of monthly wealth relatives, 3/31/92 through 6/30/97
Berkshire
Mean
.0264
Standard deviation
.0582
Mean
.3167
Standard deviation
.2016
Covariance
.0034
Correlation
1.0000
BioTime
.0186
.2237
.2227
.7748
-.0021
.0500
- .1581
1.0000
SP500
.0146
.0268
.l753
.0929
.0005
-.0001
.0007
.2954
-.0237
1.0000
T-bills
.0035
.0008
.0426
.0028
1.2E-06
3.2E-05
5.7E- 06
6.7E-07
.0257
.1773
.2610
1.0000
--- page 849 ---

820
E. O. Thorp
416
E.O. Thorp
able about BTIM and felt they were especially qualified to evaluate it as an investment.
They wished to retain a substantial position in BTIM.
The portfolio held Berkshire Hathaway, ticker BRK, having first purchased it in 1991.
8.1. The constraints
Dr. Quaife determined the Kelly optimal portfolio for XYZ Corp. subject to certain constraints. The list of allowable securities was limited to BTIM, BRK, the Vanguard 500
(S&P 500) Index Fund, and T-bills. Being short T-bills was used as a proxy for margin debt. The XYZ broker actually charges about 2% more, which has been ignored in
this analysis. The simple CAPM (capital asset pricing model) suggests that the investor
only need consider the market portfolio (for which the S&P 500 is being substituted
here, with well known caveats) and borrowing or lending. Both Quaife and the author
were convinced that BRK was and is a superior alternative and their knowledge about
and long experience with BRK supported this.
XYZ Corp. was subject to margin requirements of 50% initially and 30% maintenance, meaning for a portfolio of securities purchased that initial margin debt (money
lent by the broker) was limited to 50% of the value of the securities, and that whenever
the value of the account net of margin debt was less than 30% of the value of the securities owned, then securities would have to be sold until the 30% figure was restored.
In addition XYZ Corp. wished to continue with a "significant" part of its portfolio in
BTIM.
8.2. The analysis and results
Using monthly data from 3/31/92 through 6/30/97, a total of 63 months, Quaife finds
the means, covariances, etc. given in Table 7.
Note from Table 7 that BRK has a higher mean and a lower standard deviation than
BTIM, hence we expect it to be favored by the analysis. But note also the negative
correlation with BTIM, which suggests that adding some BTIM to BRK may prove
advantageous.
Using the statistics from Table 7, Quaife finds the following optimal portfolios, under
various assumptions about borrowing.
As expected, BRK is important and favored over BTIM but some BTIM added to the
BRK is better than none.
If unrestricted borrowing were allowed it would be foolish to choose the corresponding portfolio in Table 8. The various underlying assumptions are only approximations
with varying degrees of validity: Stock prices do not change continuously; portfolios can't be adjusted continuously; transactions are not costless; the borrowing rate
is greater than the T-bill rate; the after tax return, if different, needs to be used; the
process which generates securities returns is not stationary and our point estimates of
the statistics in Table 7 are uncertain. We have also noted earlier that because "over-
--- page 850 ---

The Kelly Criterion in Blackjack Sports Betting, and the Stock Market
( h <J:
The Kelly Criterion in Blackjack Sports Betting. and the Stock Market
Table 8
Optimal portfolio allocations with various assumptions about borrowing
Security fraction
Security
Berkshire
BioTime
S&P 500
T-bills
Portfolio growth rate
Mean
Standard deviation
No borrowing
.63
.37
.00
.00
.36
.29
50% margin
1.50
.50
.00
-1.00
.62
.45
Unrestricted borrowing
6.26
1.18
12.61
-19.04
2.10
2.03
821
417
helling" is much more harmful than underbetting, "fractional Kelly" is prudent to the
extent the results of the Kelly calculations reflect uncertainties.
In fact, the data used comes from part of the period 1982-1997, the greatest bull
market in history. We would expect returns in the future to regress towards the mean so
Ihe means in Table 7 are likely to be overestimates of the near future. The data set is
necessarily short, which introduces more uncertainty, because it is limited by the amount
of BTIM data. As a sensitivity test, Quaife used conservative (mean, std. dev.) values for
Ihe price relatives (not their logs) for BRK of (1.15, .20), BTIM of (1.15, 1.0) and the
S&P 500 from 1926-1995 from Ibbotson (1998) of (1.125, .204) and the correlations
from Table 7. The result was fractions of 1.65, .17, .18 and -1 .00 respectively for BRK,
BTIM, S&P 500 and T-bills. The mean growth rate was . 19 and its standard deviation
was .30.
8.3. The recommendation and the result
The 50% margin portfolio reallocations of Table 8 were recommended to XYZ Corp.'s
hoard on 8117/97 and could have been implemented at once. The board-elected to do
nothing. On 10/9/97 (in hindsight, a good sale at a good price) it sold some BTIM
and left the proceeds in cash (not good). Finally on 2/9/98 after a discussion with
hoth Quaife and the author, it purchased 10 BRK (thereby gaining almost $140,000
hy 3/31/98, as it happened). The actual policy, led to an increase of 73.5%. What would
have happened with the recommended policy with no rebalance and with one rebalance on 1O/6/97? The gains would have been 117.6% and 199.4%, respectively. The
gains over the suboptimal board policy were an additional $475,935 and $1,359,826,
respectively.
The optimal policy displays three important features in this example: the use of leverage, the initial allocation of the portfolio, and possible rebalancing (reallocation) of the
portfolio over time. Each of these was potentially important in ,determining the final
--- page 851 ---

822
E. 0. Thorp
418
E.O. T//(J/jJ
result. The potential impact of continuously rebalancing to maintain maximum margin
is illustrated in Thorp and Kassouf (1967), Appendix A, The Avalanche Effort.
The large loss from the suboptimal policy was much more than what would have
been expected because BRK and BTIM appreciated remarkably. In .62 years, BRK was
up 60.4% and BTIM was up 62.9%. This tells us that-atypically-in the absence of
rebalancing, the relative initial proportions of BRK and BTIM did not matter much
over the actual time period. However, rebalancing to adjust the relative proportions of
BRK and BTIM was important, as the actual policy's sale of some BTIM on 10/9/97
illustrated. Also, rebalancing was important for adjusting the margin level as prices, in
this instance, rose rapidly.
Table S illustrates what we might have normally expected to gain by using 50% margin, rather than no margin. We expect the difference in the medians of the portfolio
distributions to be $1,OSO,736[exp(.62 x .62) - exp(.36 x .62)] = $236,316 or 21.9%
which is still large.
8.4. The theory for a portfolio of securities
Consider first the unconstrained case with a riskless security (T-bills) with portfolio
fraction fil and n securities with portfolio fractions fl , .. . , f". Suppose the rate of
return on the riskless security is r and, to simplify the discussion, that this is also the
rate for borrowing, lending, and the rate paid on short sale proceeds. Let C = (sii) be
the matrix such that sij, i, j = I, ... , n, is the covariance of the i th and jth securities
and M = (m I , /112, ... , 111/1)7 be the row vector such that 111; , i = I, ... , n, is the drift
rate of the ith security. Then the portfolio satisfies
fil + ... + f/l = I,
111 = f()r + fll11l + ... + f"I11/l = r + fdl11l - r) + ... + f;,(I11/l - r)
=r+FT(M-R),
.1'2 = FTCF
(S.I)
where FT = (II , ... , f;,) and T means "transpose", and R is the column vector
.,
(r, r, ... , r) oflength n.
Then our previous formulas and results for one security plus a riskless security apply
to goo UI , ... , f;,) = m -
.1'2/2. This is a standard quadratic maximization problem.
Using (S.I) and solving the simultaneous equations (Jgoo/(Jfj = 0, i = 1, ... , n, we get
F* = C - I[M -
R],
goout , ... , f;;) = r + (F*)TCF* /2
(S.2)
where for a unique solution we require C- I to exist, i.e., det C #- O. When all the
securities are uncorrelated, C is diagonal and we have I;* = (111; -
r)/s;; or ft =
(m; - r) /s;, which agrees with Equation (7.3) when II =, 1.
--- page 852 ---

The Kelly Criterion in Blackjack Sports Betting, and the Stock Market
823
Ch. 9:
The Kelly Criterion in Blackjack Sports Betting, and the Stock Market
419
Note: BRK issued a new class of common, ticker symbol BRKB, with the old common changing its symbol to BRKA. One share of BRKA can be converted to 30 shares
of BRKB at any time, but not the reverse. BRKB has lesser voting rights and no right
to assign a portion of the annual quota of charitable contributions. Both we and the market consider these differences insignificant and the A has consistently traded at about
30 times the price of the B.
If the price ratio were always exactly 30 to 1 and both these securities were included
in an analysis, they would each have the same covariances with other securities, so
det C = °
and Ci does not exist.
If there is an initial margin constraint of q , 0 ~ q ~ 1, then we have the additional
restriction
i!Ii + ... + ifni ~ l/q.
(8.3)
The n-dimensional subset in (8.3) is closed and bounded.
If the rate for borrowing to finance the portfolio is rb = r + eb, e" :) 0, and the rate
paid on the short sale proceeds is r ,,' = r -
e,', e" :) 0, then the m in Equation (8.1) is
altered. Let x+ = max(x , 0) and x- = max(O, -x) so x = x + - x - for all x. Define
f+ = ft + ... + t,;, the fraction of the portfolio held long. Let f- = f)- + .. . + t,-;,
the fraction of the portfolio held short.
Case 1. f+ ~ I
m = r + !I(m) -r) + ... + fll(m ll - r) -es/- .
(8.4.1 )
Case 2. f+ > 1
m = r + !I(m) - r) + . .. + fll(m ll - r) - e,,(j+ - 1) - es/-.
(8.4.2)
9. My experience with the Kelly approach
How does the Kelly-optimal approach do in practice in the securities markets? In a
little-known paper (Thorp, 1971) I discussed the use of the Kelly criterion for portfolio
management. Page 220 mentions that "On November 3, 1969, a private institutional
investor decided to ... use the Kelly criterion to allocate its assets". This was actually
a private limited partnership, specializing in convertible hedging, which I managed.
A notable competitor at the time (see Institutional Investor (1998» was future Nobel
prize winner Harry Markowitz. After 20 months, our record as cited was a gain of 39.9%
versus a gain for the Dow Jones Industrial Average of +4.2%. Markowitz dropped out
after a couple of years, but we liked our results and persisted. What would the future
bring?
Up to May 1998, twenty eight and a half years since the investment program began.
The partnership and its continuations have compounded at approximately 20% annually with a standard deviation of about 6% and approximately zero correlation with the
market ("market neutral"). Ten thousand dollars would, tax exempt, now be worth 18
--- page 853 ---

824
E. O. Thorp
420
£.0. Thorp
million dollars. To help persuade you that this may not be luck, 1 estimate that during this period I have made about $80 billion worth of purchases and sales ("action",
in casino language) for my investors. This breaks down into something like one and a
quarter million individual "bets" averaging about $65,000 each, with on average hundreds of "positions" in place at anyone time. Over all, it would seem to be a moderately
"long run" with a high probability that the excess performance is more than chance.
10. Conclusion
Those individuals or institutions who are long term compounders should consider the
possibility of using the Kelly criterion to asymptotically maximize the expected compound growth rate of their wealth. Investors with less tolerance for intermediate term
risk may prefer to use a lesser function. Long term compounders ought to avoid using
a greater fraction ("overbetting"). Therefore, to the extent that future probabilities are
uncertain, long term compounders should further limit their investment fraction enough
to prevent a significant risk of overbetting.
Acknowledgements
T thank Dr. Jerry Baese\, Professor Sid Browne, Professor Peter Griffin, Dr. Art Quaife,
and Don Schlesinger for comments and corrections and to Richard Reid for posting this
chapter on his website. I am also indebted to Dr. Art Quaife for allowing me to use his
analysis in the case study.
This chapter has been revised and expanded since its presentation at the 10th International Conference on Gambling and Risk Taking.
Appendix A. Integrals for deriving moments of E 00
10(a2, /)2) = ( DO exp[- (a2x 2+b2jx2)]dx,
Jo
III(a2, b2) = ( DO xllexp[- (a2x2+b2 jx2)]dx .
Jo
Given 10 find 12
lo(a2, b2) = roo exp[- (a2x2 +I}jx2)]dX
Jo
= - f~ exp[ _(a 2 ju2 + h2u2)]( -du jll?)
--- page 854 ---

The Kelly Criterion in Blackjack Sports Betting, and the Stock Market
I 'Ii, <J:
The Kelly Criterion in Blackjack Sports Belling, and the Stock Market
"here x = l/u and dx = -du/u2 so
hCllce
L (a 2 b2) = I (b2 a2) = y'li e-2labl
2,
0,
2 I b I
'
10 = 1
00 exp[ _(a 2x 2 + b2 /x2)] dx = U . VI~ - 1
00 V dU
where U = exp[·]' dV = dx, dU = (exp[· ])(-2a2x + 2b2x - 3 ) and V = x so
10 = exp[ _(a2x 2 + b2/x2)] . xl~
Hence:
-1
00 (-2a 2x 2 + 2b2/x2) exp[ _(a2x 2 + b2/x2)] dx
= 2a2h(a2, b2) - 2b2L2(a2 , b2).
10(a2, b2) = 2a2 h(a2, b2) - 2b2 L2(a2, b2)
and L2 (a 2, b2) = 10(b2, a2) so substituting and solving for h gives
Comments.
( I) We can solve for all even n by using 10, 1-2 and h and integration by parts.
825
421
(A. I)
(2) We can use the indefinite integral 10 corresponding to 10, and the previous methods,
to solve for 1-2, h, and then for all even n. Since
then
Appendix B. Derivation of formula (3.1)
This is based on a note from Howard Tucker. Any errors are mine,.
--- page 855 ---

826
E. O. Thorp
422
£.0. Thorp
From the paper by Paranjape and Park, if x(t) is standard Brownian motion, if a =I- 0,
b > 0,
p(X(t) ~ at + b, 0 ~ t ~ T I X(T) = s)
= 101 - exp{ - ~ (aT + B - S)}
if s ~ aT + b,
if s > aT + B.
Write this as:
p(X(t) ~ at +b, 0 ~ t ~ T I X(T))
~. 1 - exp{ -2b(aT + b - X(T))~} if X(T) ~ aT + b.
Taking expectations of both sides of the above, we get
p(X(t) ~ at + b, 0 ~ t ~ T)
=
(1 - e - 2iJ(aT+b-s)I / 1') __
e - s2/2T ds
/
aT+I>
1
- 00
J2nT
= __
e-·I /21 ds _ __
e- (.1 - 2b) /21 ds.
1
/aT + I>
.2"
e - 2ab /"1' + 1>
.
2"
J2n T
-00
J2n T
-00
Hence
P(X going above line at + b during [0, T)) = 1 - previous probability
= __
e- I /21 ds + e - 2ab . __
e - u /21 du,
I
JOO
.2 "
I
/aT - I>
2,
J2nT
a1'+iJ
J2nT
- 00
where u = s - 2b.
(B.l)
Now, when a = 0, b > 0,
[
] (21°O
2
'
P
sup X(t) ~ b = V -;;;re- V /21 dv,
O~ / ~ T
nT
I>
which agrees with a known formula (see, e.g., p. 261 of Tucker (1967)). In the case a >
0, when T -+ 00, since fliT -+ 0 and fl = s.d. of X(T) , the first integral -+ 0,
the second integral -+ 1, and P(X ever rises above line at + b) = e- 2"I>. Similarly, in
the case a < 0, peever rises above line at + b) = 1.
The theorem it comes from is due to Sten Malmquist, On certain confidence contours
for distribution functions, Ann. Math. Stat. 25 (1954), pp. 523-533. This theorem is
stated in S.R. Paranjape and C. Park, Distribution of the supremum of the two-parameter
Yeh-Wiener process on the boundary, J. App!. Prob. 10 (1973).
Letting ex = a fl, f3 = b I fl, formula (B. 1) becomes
PO = N( -ex - f3) + e- 2afi N(ex -
f3) where ex, f3 > 0
or
--- page 856 ---

The Kelly Criterion in Blackjack Sports Betting, and the Stock Market
827
Ch. 9:
The Kelly Criterion in Blackjack Sports Betting, and the Stock Market
423
p(x(t) :( at + b, 0 :( t :( T) = 1 -
PC) = N(a + fJ) - e- 2afJ N(a -
fJ)
for the probability the line is never surpassed. This follows from:
_1_1 00 e-·\·2j2T ds = _1_1 00
e-x2j2 dx = N( -a -
fJ )
.J2rrT aT+b
~
a./f+bj./f
--
eu-j2T du = N(a -
fJ)
1
j aT-b
?
.J2rrT
- 00
where s = aT + b, x = s / .JT = a.JT + b/ .JT, a = a.JT and fJ = b/ .JT.
The formula becomes:
p(sup[X(t) - (at + b)] ~ 0: 0 :( t :( T)
= N(-a -
fJ) + e- 2a/J N(a -
fJ)
= N(-a -
fJ) + e- 2afJ N(a -
fJ),
a , fJ > O.
Observe that
PC) < N(-a - m + N(a -
fJ) = {I - N(a +fJ)} + N(a -
fJ)
= jafJ a(x) dx + 1
00 a(x) dx < I
-00
a+fJ
as it should be.
Appendix C. Expected time to reach goal
and
Reference: Handbook of Mathematical Functions, Abramowitz and Stegun, Editors,
N.B.S. Applied Math. Series 55, June 1964.
P. 304, 7.4.33 gives with erf z == Jrr f~ er2 dt the integral:
f exp{ _(a 2 x2 + b2 /x2) } dx
= :- [e2a!Jerf(ax + b/x) + e- 211 !J erf(ax - b/x)] + C,
a i- O.
(C.l)
Now the left side is > 0 so for real a, we require a > 0 otherwise the right side is < 0,
a contradiction.
We also note that p. 302, 7.4.3. gives
roo exp{ -(at2 + b/ t 2)} dt = ~ ~e-2~
10
2V~
(C.2)
with ma > 0, mb > O.
