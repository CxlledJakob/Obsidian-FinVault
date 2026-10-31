# The Kelly capital growth investment criterion _ theory and -- Leonard C_ Maclean, Edward O_ Thorp, W_ T_ Ziemba, Leonard -- World Scientific Handbook -- isbn13 9781283148344 -- bec576e26410d0c695fd5b867d08ec4f -- An.pdf — pages 609–628

--- page 609 ---

580
N. H. Hakansson and W T. Ziemba
68
N.H. Hakansson, w.T. Ziemba
The amount invested at time t - 1 is
Mt
LZit = Wt-l
i=l
and the value of the investment at time t, broken down between its risky and
riskfree components, is
Mt
Mt
Wt = L(1 + rit)Zit + (1 + rlt)( 1 - L
Zit),
i=2
i=2
which together yield the basic difference equation
where
Mt
Wt = L(rit -rlt)Zit+ Wt-l(1+rlt),
i=2
M t
Rt(Xt) == L(rit - rlt)xit + 1 + rlt ·
i=2
t = 1,2, . . .
(6)
t = 1,2, .. .
(7)
Let us now turn to the basic reinvestment problem which (ignores capital
infusions and distributions and) simply revises the portfolio at discrete points in
time. In view of (5), (6) may be written
t
Wt = Wo exp { LIn Rn(Xn)},
n=l
Defining
(8) becomes
Wt = wo[exp{Gt«(Xt)}]t
= wo(1 + gt)t,
t = 1,2, ....
(8)
(9)
(10)
where gt = exp G t «(Xt) - 1 is the compound growth rate of capital over the first t
periods.
By the law of large numbers,
under mild conditions, Thus, it is evident that for large T,
Wt -+ 0 if E[Gd s 8 < 0,
t 2: T,
(11)
--- page 610 ---

Capital Growth Theory
Ch. 3. Capital Growth Theory
WI -+ 00 if E[GtJ :::: 8 > 0,
t:::: T
gl -+ exp E[GtJ- 1.
Under stationary returns and policies (XI ), (11) and (12) simplify to
WI -+ 0 if E[ln Rn(xn)] < 0
WI -+ 00 if E[ln Rn (xn)] > 0
any n.
581
69
(12)
(13)
There is nothing intuitive that would suggest that the sign of E[ln Rn (xn)] is the
determinant of whether our capital will decline or grow in the (stationary) simple
reinvestment problem. What is evident is that the expected return on capital,
E[Rn] - 1, is not what matters. As (6) reminds us, capital growth (positive or
negative) is a multiplicative, not an additive process.
To illustrate the point, consider the case of only two assets, one riskfree yielding
5% per period, and the other returning either -60% or + 100% with equal probabilities in each period. Always putting all of our capital in the riskfree asset clearly
gives a 5% growth rate of capital. The expected return on the risky asset is 20%
per period. Yet placing all of our funds in the risky asset at the beginning of each
period results in a capital growth rate that converges to -1O.55%! It is easy to see
this. We will double our money to 200% roughly half of the time. But we will also
lose 60% (bringing the 200% to 80%) of our beginning-of-period capital about half
the time, for a 'two-period return' of -20% on average, or -10.55% per period.
Expected capital E[ WI]' on the other hand, has a growth rate of 20% per period.
What this simple example demonstrates is that there are many investment
strategies for which, as t -+ 00,
E[wtJ-+ 00
Median [wtJ -+ 0
Mode [WI] -+ 0
Pr{wl < $1} -+ 1.
The coexistence of the above four measures results when E[GtJ S 8 < 0 for t :::: T
and a long (but thin) upper tail is generated as WI moves forward in time.
In view of (7), (9) and (10), we observe that to 'maximize' the long-run growth
rate g(' it is necessary and sufficient to maximize E[ GI «XI))], or
Max {E[ln Rl (Xl)] + E[ln R2(X2)] + ... }
(14)
Whenever returns are independent from period to period or the economy obeys a
Markov process 1, it is necessary and sufficient to accomplish (14) to
Max E[ln RI(xl)] sequentially at each t - 1.
(15)
XI
I Algoet & Cover [1988] show formally that the growth-optimal strategy maintains its basic
properties under arbitrary returns .processes.
--- page 611 ---

582
N H. Hakansson and W T. Ziemba
70
NH. Hakansson, w.T. Ziemba
Since the geometric mean of Rt (Xt) = exp{E[ln Rt (Xt)]), we observe that (15) is
also equivalent to maximizing the geometric mean of principal plus return at each
point in time.
3.1. Properties of the growth-optimal investment strategy
Since the solution (xn to (15), in view of (10) and (13), almost surely leads
to more capital in the long run than any other investment policy which does
not converge to it, (xn is referred to as the growth-optimal investment strategy.
Existence is assured by the no-easy-money condition (4), the bounds on expected
returns (1)-(3), and the solvency constraint (5). The strict concavity of the
objective function in (15) implies that the optimal payoff distribution Rt (x7) is
unique; the optimal policy x7 itself will be unique only if, for any security i, there
is no portfolio of the other assets which can replicate the return pattern rit.
It is probably not surprising that the growth-optimal strategy never risks ruin, i.e.
Pr {Rt (x7) = O} = 0
-
because to grow you have to survive. But this need not mean that the solvency
constraint is not binding: E[ln Rt(xt)] may exist even when Rt touches 0 as long
as the lower tail is very thin. The conditions (1)-(3) imply that positive growth is
feasible. Another dimension of the consistency between short-term and long-term
performance was observed by Bell & Cover [1988].
As shown by Breiman [1961], the growth-optimal strategy also has the property
that it asymptotically minimizes the expected time to reach a given level of capital.
This is not surprising in view of the characteristics noted in the previous two
paragraphs.
It is also evident from (15) that the growth-optimal strategy is myopic even
when returns obey a Markov process (Hakansson 1971c). This property is clearly
of great practical significance since it means that the investor only needs to
estimate the coming period's (joint) return structure in order to behave optimally
in a long-run sense; future periods' return structures have no influence on the
current period's optimal decision. No other dynamic investment model has this
property in a Markov economy; only a small set of other families have it when
returns are independent from period to period (see Section 5).
The growth-optimal strategy implies, and is implied by, logarithmic utility of
wealth at the end of each period. This is because at each t - 1
Max E[ln Rt(xt)]
x,
~ Max {E[ln Rt(xt) + In wt-d}
x,
= Max E[ln(wt-1Rt(Xt))] = Max E[ln Wt(Zt)].
~
~
Since every utility function is unique (up to a positive linear transformation),
it also follows that the growth-optimal strategy is not consistent with any other
end-of-period utility function (more on this in the next subsection).
--- page 612 ---

Capital Growth Theory
Ch. 3. Capital Growth Theory
The relative risk aversion function
wu"(w)
q(w) == ----'---
u'(w)
583
71
equals 1 when u(w) = In(w) (it is 0 for a risk-neutral investor). Thus, we observe
that to do 'the best' in the long run in terms of capital growth, it is not only
necessary to be risk averse in each period. We must also display the 'right' amount
of risk aversion. The long-run growth rate of capital will be lower either if one
invests in a way which is more risk averse than the logarithmic function or relies
on an objective function which is less risk averse.
The growth-optimal investment strategy is not only linear in beginning-of-period
wealth but proportional as well since definitionally
Both of these properties are shared by only a small family of investment models.
Since the growth-optimal strategy is consistent with a logarithmic end-of-period
utility function only, it is clearly not consistent with the mean-variance approach
to portfolio choice -
which in turn is consistent with quadratic utility for
arbitrary security return structures, and, for normally distributed returns, with
those utility functions whose expected utilities exist when integrated with the
normal distribution, plus a few other cases, as shown by Ziemba & Vickson [1975]
and Chamberlain [1983]. This incompatibility is easy to understand; in solving for
the growth-optimal strategy, all of the moments of the return distributions matter,
with positive skewness being particularly favored. When the returns on the risky
assets are normally distributed, no matter how favorable the means and variances
are, the growth-optimal strategy cooly places 100% of the investable funds in the
riskfree asset.
The preceding does not imply that the growth-optimal portfolio necessarily is
far from the mean-variance efficient frontier (although this may be the case [see
e.g. Hakansson, 1971a]). It will generally be close to the MV-efficient frontier,
especially when returns are fairly symmetric. And as shown in Section 8, the
mean-variance model can in some cases be used to (sequentially) generate a close
approximation to the growth-optimal portfolios.
Other properties of the Kelly criterion can be found in MacLean, Ziemba &
Blazenko [1992, table 1].
3.2. Capital growth vs. expected utility
Based on (10), the uniqueness properties implied by (15), and the law of large
numbers, it is undisputable, as noted in the previous subsection, that the growthoptimal strategy almost surely generates more capital (under basic reinvestment)
in the long run than any other strategy which does not converge to it. At the
same time, however, we observed that the growth-optimal strategy is consistent
with logarithmic end-of-period utility of wealth only. This clearly implies that
there must be 'reasonable' utility functions which value almost surely less capital
--- page 613 ---

584
N. H. Hakansson and W. T. Ziemba
72
N.H. Hakansson, w.T. Ziemba
in the long run more than they value the distribution generated by the Kelly
criterion.
Consider the family
1
u(w) = -w Y ,
Y
Y < 1,
(16)
to which u(w) = In(w) belongs via Y = 0, and let (Xt(Y)) be the optimal portfolio
sequence generated by solving
Max E [~wr] at each t - 1.
x,
Y
For simplicity, consider the case of stationary returns. Since Xt (y) i= Xt (0) = x:'
it is evident that
(17)
even though there exist numbers a > 1 and T(E) such that
(18)
for every (1 »
E > O.
Many a student of investment has stubbed his toe by interpreting (18) to mean
that (xn generates higher expected utility than, say, (Xt(Y)) . (17) and (18) may
seem like a paradox but clearly implies that the geometric mean criterion does not
give rise to a 'universally best' investment strategy.
The intuition behind this truth is as follows. For Y < 0 in (16), (17) and
(18) occur because, despite the fact that the wealth distribution for (Xt(Y)) lies
almost entirely to the left of the wealth distribution for (xn , the lower tail of the
distribution for (Xt(Y)) is shorter and (imperceptibly) thinner than the (bounded)
left tail of the growth-optimal distribution. Thus, for negative powers, very small
adverse changes in the lower tail overpower the value of almost surely ending up
with a higher compound return. Conversely, for Y > 0, it is the longer (though
admittedly very thin) upper tail that gives rise to (17) in the presence of (18) even
though, again, the wealth distribution for (Xt(Y)) lies almost entirely to the left of
the wealth distribution for (xn.
4. Conditions for capital growth
As already noted, the determinants of whether capital will grow or decline
(almost surely) in the long run are given by (12) and (11). Conditions (1)-
(2) insure that (12) is feasible; in the absence of (1)-(2), positive growth may
be infeasible. If a positive long-run growth rate (bounded away from zero) is
achievable, then the growth-optimal strategy will find it. Thus we can state:
--- page 614 ---

Capital Growth Theory
585
Ch. 3. Capital Growth Theory
73
Theorem. In the absence of (1) and (2), a necessary and sufficient condition for
long-run capital growth to be feasible is that the growth-optimal strategy achieves a
positive growth rate, i. e. that for some E > 0 and large T
(19)
For y < 0, the objective functions in (16) attain long-run growth rates of capital
between those of the risk-free asset and of the growth-optimal strategy. But for
y > 0, the long run growth-rate may be negative. Consider for a moment the utility function u (w) = W 1/2, one of the most frequently cited examples of 'substantial'
risk aversion since Bernoulli's time. Even this venerable function may, however,
lead to (almost sure) ruin in the long-run: suppose, for example, that the riskfree
asset yields 2% per period and that there is only one risky asset, which gives either
a loss of 8.2% with probability 0.9, or a gain of 206% with probability 0.1. The optimal policy then calls for investing the fraction 1.5792 in the risky asset (by borrowing the fraction 0.5792 of current wealth to complete the financing) in each period.
But the average compound growth rate gt in (10) will now tend to -0.00756, or
-3/4%. Thus, expected utility 'grows' as capital itself almost surely vanishes.
What this example illustrates is that risk aversion plus a favorable return
structure [see (1)-(3)] are not sufficient to insure capital growth in the basic
reinvestment case.
5. Relationship to other long-run investment models
As shown in Section 3, the growth-optimal investment strategy has its traditional
origin in arguments concerning capital growth and the law of large numbers. But
it can also be derived strictly from an expected utility perspective -
but only as a
member of a small family.
Let n be the number of periods left to a terminal horizon point at time O.
Assume that wealth at that point, Wo, has utility Uo(wo), where U~ > 0 everywhere
and U~ < 0 for large WOo Then, with one period to go, we have the single-period
portfolio problem
Ul(Wl) == Max E[Uo(wo(zl))]
zllwl
where U I (WI) is the induced, or derived, utility of wealth WI at time 1 and the
difference equation (6) has been trivially modified to
Mn
Wn-I = L(1 + rin)Zin + wn(1 + rln),
n = 1,2, ....
i=2
Thus, with n periods to go, we obtain
Un(Wn) == Max E[Un-l(Wn-l(Zn))],
n = 1,2, ...
Znlwn
where (21) is a standard recursive equation.
(20)
(21)
--- page 615 ---

586
N H. Hakansson and W. T. Ziemba
74
N.H. Hakansson, WT. Ziemba
The induced utility of current wealth, Un(wn), of course, generally depends on
all the inputs to the problem, that is the utility of terminal wealth Uo, the joint
distribution functions of future returns Fn , ... , Fl, and the future interest rates
rln, ... , rll. But there are two rather interesting special cases. The first is the case
in which the induced utility functions Un(wn) depend only on the terminal utility
function Uo. This occurs when the returns are independent from period to period
and Uo( wo) is isoelastic, i.e.
1 Y
Uo(wo) = -wo , some y < l.
y
As first shown by Mossin [1968], (21) now gives
Un(Wn) = anUo(wn) + bn
'"" Uo(wn)
(where '"" means equivalent to) since an and bn are constraints with an positive.
The optimal investment policy is both myopic and proportional, i.e.
z7n(wn) = Xin(Y)Wn, all i
where the Xin (y) are constants.
The second special case obtains when returns are independent from period to
period, interest rates are deterministic, and the terminal utility function reflects
hyperbolic absolute risk aversion, that is (Hakansson 1971c)
1
-(wo + I/>)Y,
Y < 1,
Y
or
Uo(wo) =
(I/> - wo)Y,
Y > 1, I/> large;
(22)
or
- exp{ -I/>wo}
I/> > O.
In the first sub case
1 (
I/»Y
Un(wn) = -
Wn + --------
Y
(1 + rd ... (1 + rln)
(23)
where (23) holds globally for I/> ~ 0 and locally for I/> > 0, i.e. for Wn ::: Ln > O.
The optimal investment policy is
z7n(wn) = Xi/l(Y) ( Wn + (1 + rll) .~. (1 + rln») ,
i::: 2.
In the other two subcases, a closed form solution holds only locally.
But the most interesting result associated with (21) is surprisingly general.
Under mild conditions on Uo(wo), and independent (but nonstationary) returns
from period to period, we obtain [Hakansson, 1974; see also Leland, 1972; Ross,
--- page 616 ---

Capital Growth Theory
Ch. 3. Capital Growth Theory
1974; Huberman and Ross 1983]:
1
Y
un(wn) -+ -wn
y
and, if returns are stationary,
Thus, the class of utility functions
1
u(w) = -wY ,
y < 1,
Y
587
75
(24)
(25)
(16)
the only family with constant relative risk aversion (ranging from 0 to infinity)
and exhibiting myopic and proportional investment policies, is evidently applicable
to a large class of long-run investors. The optimal policies aoove are not meanvariance efficient, but for reasonably symmetric return distributions, they come
close to MV efficiency.
Since y = 0 in (24) corresponds to logarithmic utility of wealth, the growthoptimal strategy is clearly a member of this elite family of long-run oriented
investors. In other words, the geometric mean investment strategy has a solid
foundation in utility theory as well.
6. Relationship to intertemporal consumption-investment models
Up to this point, we have examined the basic dynamic investment problem,
i.e. without reference to cash inflows or outflows. Under some conditions, the
inclusion of these factors is straightforward and does not materially affect the
optimal investment policy. But a realistic model incorporating noncapital inand
outflows typically complicates the model substantially.
The basic dynamic consumption-investment model incorporates consumption
and a labor income into the dynamic reinvestment model. Following Fisher [1936],
wealth is viewed as a means to an end, namely consumption.
The basic difference equation (6) now becomes
M,
Wt = L(ri/ - rlt)Zi/ + (1 + rlt)(Wt-l - Ct) + Yt,
t = 1, ... , T,
(26)
i=2
where Ct is the amount consumed in period t (set aside at the beginning of the
period) and Yt is the labor income received at the end of period t.
Consistent with the foregoing, the individual's objective becomes
Max E[U(Cl, ... , CT)]
subject to
Ct :::: 0, all t
--- page 617 ---

588
N. H. Hakansson and W T. Ziemba
76
NH. Hakansson, w.T. Ziemba
where U is assumed to be monotone, strictly concave, and to reflect impatience,
i.e. considering the two consumption streams
(a, b, C3, ... , CT)
(b, a, C3, .. . , CT),
a > b
the first is preferred to the second.
In order to attain tractability, several strong assumptions are usually imposed:
1) the individual's lifetime (horizon) is known,
2) interest rates are viewed as deterministic,
3) the labor income Yt is deterministic; its present value is thus
Yt
YT
Yt-l == - + ... +
,
rlt
(l+rlt)···(l+rIT)
4) the utility function is assumed to be additive, i.e.
U (CI, ... , CT) = UI (cl) + alu2(c2) + ... + al .. . aT-Iur(cT),
(27)
where u; > 0, u;' < 0, and typically at < 1, for all t, which implies that preferences
are independent of past consumption.
Let
ft-I(Wt-l) = maximum expected utility at t -1 given Wt-I·
This gives
fr-l(Wt-l) = Max {Ut(Ct) + at E[ft(Wt)]),
t = 1, . .. , T,
(28)
C"Z,
where h(WT) == ° or bT(WT)
subject to
Ct ~ °
Pr{Wt ~ -Yrl = 1
Zit ~ 0,
i 1- St
(29)
(30)
(31)
for each t, where br( WT) represents a possible bequest motive. It is apparent
that ft-I (Wt-l) represents the utility of wealth and that it is induced or derived; it
clearly depends on everything in the model. Solving (28) recursively, it is evident
that, under our assumptions concerning labor income and interest rates, Yt can be
exchanged for cash in the solution.
Suppose that in (27)
1 y
Ut(Ct) = -ct ,
Y < 1, t = 1, ... , T.
Y
Then [Hakansson, 1970]
ft-I(Wt-l) = At-I(Wt-l + Yt-l)Y + Bt-l,
c;(Wt-d = Ct(Wt-1 + Yt- I),
(32)
--- page 618 ---

Capital Growth Theory
589
Ch. 3. Capital Growth Theory
77
and
M,
Z;t(Wt-d = Wt-l - c7 - LZ7t(Wt-l),
i=2
where the Ar, Br, and Ct are constants. Thus, the optimal consumption and
investment policies are again proportional, not to Wt-l but to Wt-l + Yt-l. The
latter quantity is sometimes referred to as permanent income.
Note that when y = 0 in (32), the consumer-investor does indeed employ the
growth-optimal strategy to invested funds.
Finally, the model (28)-(31) has been extended in a number of directions,
to incorporate a random lifetime, life insurance, a subsistence level constraint
on consumption, a Markov process for the economy, and an uncertain income
stream from labor -
with limited success [see Hakansson 1969, 1971b, 1972;
Miller, 1974]. In general, closed-form solutions do not exist when income streams,
payment obligations, and interest rates are stochastic. In such cases, multi-stage
stochastic programming models are helpful [see e.g. Mulvey & Ziemba, 1995].
7. Growth vs. security
Empirical evidence suggests that the average investor is more risk averse than
the growth-optimal investor, with a risk-tolerance corresponding to y ~ -3 in
(16) [see e.g. Blume & Friend, 1975]. While real-world investors exhibit a wide
range of attitudes towards risk, this means that the majority of investors are in
effect willing to sacrifice a certain amount of growth in favor of less variability, or
greater 'security'.
7.1 The discrete-time case
In view of the convergence results (24) and (25), it is evident that repeated
employment of (16) for any y < 0 attains an efficient tradeoff between growth and
security, as defined above, for the long-run investor. The concept of 'efficiency' is
thus employed in a sense analogous to that used in mean-variance analysis.
A number of more direct measures of the sacrifice of growth for security have
also been examined. In particular, MacLean, Ziemba & Blazenko [1992] analyzed
the tradeoffs based on three growth and three security measures. The three growth
measures are:
1. E (Wt «Xt)], the expected wealth level after t periods;
2. E[gtJ, the mean compound growth rate over the first t periods;
3. E[t : Wt«Xt)
~ y], the mean first passage time to reach wealth level y;
while the three security measures are:
4. Pr{ Wt «Xt» ~ y}, the probability that wealth level y will be reached in t
periods;
--- page 619 ---

590
N. H. Hakansson and W. T. Ziemba
78
N.H. Hakansson, w.T. Ziemba
5. Pr{wl«xl)) :::: hI, t = 1,2, ... }, the probability that the investor's wealth is
on or above a specified path;
6. Pr{ WI «XI)) :::: y before WI «(XI)) s h, where h < Wo < y}, which includes the
probability of doubling before halving.
Tradeoffs were generated via fractional Kelly strategies, i.e. strategies involving
(stationary) mixtures of cash and the growth-optimal investment portfolio. Applied
to a stationary environment, these strategies were shown to produce effective
tradeoffs in that as growth declines, security increases. However, these tradeoffs,
while easily computable, are generally not efficient, i.e. do not maximize security
for a given (minimum) level of growth. Other comparisons involving the growthoptimal strategy and half Kelly or other strategies may be found in Ziemba &
Hausch [1986], Rubinstein [1991], and Aucamp [1993].
7.2. The continuous-time case
Since transaction costs are zero under the perfect market assumption, it is natural to consider shorter and shorter periods between reinvestment decisions. In the
limit, reinvestment takes place continuously. Assuming that the returns on risky
assets can be described by diffusion processes, we obtain that optimal portfolios
are mean-variance efficient in that the instantaneous variance is minimized for
a given instantaneous expected return. The intuitive reason for this is that as
the trading interval is shortened, the first two moments of the security's return
become more and more dominant [see Samuelson, 1970]. The optimal portfolios
also exhibit the separation property -
as if returns over very short periods were
normally distributed. Over any fixed interval, however, payoff distributions are,
due to the compounding effect, usually lognormal. In other words, all investors
with the same probability assessments, but regardless of risk attitude, invest in
only two mutual funds, one of which is riskfree [Merton, 1971]. See also Karatzas,
Lehoczky, Sethi and Shreve [1986] and Sethi and Taksar [1988].
In view of the above, it is evident that the tradeoff between growth and security
generated by the fractional Kelly strategies in the continuous-time model when
the wealth process is lognormal is efficient in a mean-variance sense. Li [1993]
has addressed the growth vs. security question for the two asset case while Li &
Ziemba [1992] and Dohi, Tanaka, Kaio & Osaki [1994] have done so when there
are n risky assets that are jointly lognormally distributed.
8. Applications
8.1. Asset allocation
In view of the myopic property of the optimal investment policy in the dynamic
reinvestment problem [see (24) and (25)], it is natural to apply (15) for different
values of y to the problem of choosing investment portfolios over time. In
particular, the choice of broad asset categories, also known as the asset allocation
--- page 620 ---

Capital Growth Theory
591
Ch. 3. Capital Growth Theory
79
problem, lends itself especially well to such treatment. Thus, to implement the
growth-optimal strategy, for example, we merely solve (15) subject to relevant
constraints (on borrowing when available and on short positions) at the beginning
of each period.
To implement the model, it is necessary to estimate the joint distribution
function for next period's returns. Since all moments and comoments matter,
one way to do this is to employ the joint empirical distribution for the previous
n periods. This approach provides a simple and realistic means of generating
nonstationary scenarios of the possible outcomes over time. The raw distribution
may of course may be modified in any number of ways, for example via Stein
estimators [Jorion, 1985, 1986, 1991; Grauer & Hakansson, 1995], an inflation
adapter [Hakansson, 1989], or some other method.
Grauer and Hakansson applied the dynamic reinvestment model in a number
of settings with up to 16 different risk attitudes y under both quarterly and annual
portfolio revision. In the domestic setting [Grauer & Hakansson, 1982, 1985,
1986], the model was employed to construct and rebalance portfolios composed of
U.S. stocks, corporate bonds, government bonds, and a riskfree asset. Borrowing
was ruled out in the first article while margin purchases were permitted in the
other two. The third article also included small stocks as a separate investment'
vehicle. On the whole, the growth-optimal strategy lived up to its reputation. On
the basis of the empirical probability assessment approach, quarterly rebalancing,
and a 32-quarter estimating period applied to 1934-1992, the growth-optimal
strategy outperformed all the others -
with borrowing permitted, it earned an
average annual compound return of nearly 15%.
In Grauer & Hakansson [1987], the model was applied to a global environment
by including in the universe the four principal U.S. asset categories and up to fourteen non-U.S. equity and bond categories. The results showed that the gains from
including non-U.S. asset classes in the universe were remarkably large (in some
cases statistically significant), especially for the highly risk-averse strategies. With
leverage permitted and quarterly rebalancing, the geometric mean strategy again
came out on top, generating an annual compound return of 27% over the 1970-
1986 period. A different study examined the impact from adding three separate
real estate investment categories to the universe of available categories [Grauer &
Hakansson, 1994b]. Finally, Grauer, Hakansson & Shen [1990] examined the asset
allocation problem when the universe of risky assets was composed of twelve equaland value-weighted industry components of the U.S. stock market.
Mulvey [1993] developed a multi-period model of asset allocation which incorporates transaction costs, including price impact. The objective function is a
general concave utility function. A computational version developed by Mulvey
& Vladimirou [1992] focused on the isoelastic class of functions in which the
objective was to maximize the expected utility of wealth at the end of the planning
horizon. This model, like those based on the empirical distribution approach, can
handle assets possessing skewed returns, such as options and other derivatives,
and can be extended to include liabilities [see Mulvey & Ziemba, 1995]. Based on
historical data over the period 1979 to 1988, this research, based On multi-stage
--- page 621 ---

592
N. H. Hakansson and W T. Ziemba
80
NH. Hakansson, w.T. Ziemba
stochastic programming, showed that efficiencies could be gained vis-a-vis myopic
models in the presence of transaction costs by taking advantage of the network or
linear structure of the problem.
Mean-variance approximations. A number of authors have argued that, in the
single period case, power function policies can be well approximated by MV
policies, e.g. Levy & Markowitz [1979], Pulley [1981, 1983], Kallberg & Ziemba
[1979, 1983], and Kroll, Levy & Markowitz [1984]. However, there is an opposing
intuition which suggests that the power functions' strong aversion to low returns
and bankruptcy will lead them to select portfolios that are not MV-efficient, e.g.
Hakansson [1971a] and Grauer [1981, 1986]. It is therefore of interest to know
whether the power policies differ from the corresponding MV and quadratic
policies when returns are compounded over many periods.
Let fLit be the expected rate of return on security i at time t and O"ijt be the
covariance between the returns on securities i and j at time t. Then the MV
investment problem is
Max {T(1 + fLt} -10"/L
XI
subject to the usual constraints. The MV approximation to the power functions in
(16) are obtained [Ohlson, 1975; Pulley, 1981] when
1
T=--.
l-y
Under certain conditions this result holds exactly in continuous time [see Merton,
1973, 1980].
With quarterly revision, the MV model was found to approximate the exact
power function model very well [Grauer & Hakansson, 1993]. But with annual
revision, the portfolio compositions and returns earned by the more risk averse
power function strategies bore little resemblance to those of the corresponding
MV approximations. Quadratic approximations proved even less satisfactory in
this case. These results contrast somewhat with those of Kallberg & Ziemba [1983],
who in the quadratic case with smaller variances obtained good approximations for
horizons up to a whole year [see also MacLean, Ziemba & Blazenko, 1992].
8.2. Growth-security tradeoffs
The growth vs. security model has been applied to four well-known gamblinginvestment problems: blackjack, horse race wagering, lotto games, and commodity
trading with stock index futures. In at least the first three cases, the basic investment situation is unfavorable for the average player. However, systems have been
developed that yield a positive expected return. The various applications use a
variety of growth and security measures that appear to model each situation well.
The size of the optimal investment gamble also varies greatly, from over half to
less than one millionth of one's fortune.
--- page 622 ---

Capital Growth Theory
593
Ch. 3. Capital Growth Theory
81
Blackjack. By wagering more in favorable situations and less or nothing when the
deck is unfavorable, an average weighted edge is about 2%. An approximation to
provide insight into the long-run behavior of a player's fortune is to assume that
the game is a Bernoulli trial with a probability of success equal to 0.51. With a
2% edge, the optimal wager is also 2% of one's fortune. Professional blackjack
teams often use a fractional Kelly wagering strategy with the fraction drawn from
the interval 0.2 to 0.8. For further discussion, see Gottlieb [1985] and Maclean,
Ziemba & Blazenko [1992].
Horseracing. There is considerable evidence supporting the proposition that it is
possible to identify races where there is a substantial edge in the bettor's favor
(see the survey by Hausch & Ziemba [1995] in this volume). At thoroughbred
racetracks, one can find about 2-4 profitable wagers with an edge of 10% or more
on an average day. These opportunities arise because (1) the public has a distaste
for the high probability-low payoff wagers, and (2) the public is unable to properly
evaluate the worth of multiple horse place and show and exotic wagers because
of their complexity; for example, in a ten-horse race there are 120 possible show
finishes, each with a different payoff and chance of occurrence. In this situation,
interesting tradeoffs between growth and security arise as well.
The Kentucky Derby represents an interesting special case because of the
long distance (1 1/4 miles), the fact that the horses have not previously run this
distance, and the fame of the race. Hausch, Bain & Ziemba [1995] tabulated the
results from Kelly and half Kelly wagers using the system in Ziemba & Hausch
[1987] over the 61-year period 1934-1994. They also report the results from using
a filter rule based on the horse's breeding.
Lotto games. Lotteries tend to have very low expected payoffs, typically on the
order of 40 to 50%. One way to 'beat' parimutuel games is to wager on unpopular
numbers -
see Hausch & Ziemba [1995] for a survey. But even when the odds
are 'turned' favorable, the optimal Kelly wagers are extremely small and it may
take a very long time to reach substantial profits with high probability. Often an
initial wealth level in the seven figures is required to justify the purchase of even
a single $1 ticket. Comparisons between fractional and full Keily strategies can be
found in MacLean, Ziemba & Blazenko [1992].
Commodity trading. Repeated investments in commodity trades can be modeled
as a capital growth problem via suitable modifications for margin requirements,
daily mark-to-the-market procedures, and other practical details. An interesting
example is the turn-of-the-year effect exhibited by U.S. small stocks in January . .
One way to benefit from this anomaly is to take long positions in a small stock
index and short positions in large stock indices, because the transaction costs
(commissions plus market impact) are less than a tenth of what they would be
by transacting in the corresponding basket of securities. Using data from 1976
through January 1987, Clark & Ziemba [1987] calculated that the growth-optimal
--- page 623 ---

594
N. H. Hakansson and W T. Ziemba
82
N.H. Hakansson, w.T. Ziemba
strategy would invest 74% of one's capital in this opportunity. Hence fractional
Kelly strategies are suggested. See also Ziemba [1994].
9. Summary
Capital growth theory is useful in the analysis of many dynamic investment
situations, with many attractive properties. In the basic reinvestment case, the
growth-optimal investment strategy, also known as the Kelly criterion, almost
surely leads to more capital in the long run than any other investment policy which
does not converge to it. It never risks ruin, and also has the appealing property
that it asymptotically minimizes the expected time to reach a given level of capital.
The Kelly criterion implies, and is implied by, logarithmic utility of wealth (only)
at the end of each period; thus, its relative risk aversion equals 1, which makes it
more risk-tolerant than the average investor. As a result, tradeoffs between growth
and security have found application in a rich set of circumstances.
The fact that the growth-optimal investment strategy is proportional to beginning-of-period wealth is of great practical value. But perhaps the most significant
property of the Kelly criterion is that it is myopic not only when returns are
non stationary and independent but also when they obey a Markov process. In the
dynamic investment model with a given terminal objective function, the growthoptimal strategy is a member of the set to which the optimal policy converges as
the horizon becomes more distant. Finally, the Kelly criterion is optimal in many
environments in which consumption, noncapital income, and payment obligations
are present.
References
Algoet, P.H., and T.M. Cover (1988). Asymptotic optimality and asymtotic equipartition properties
at log-optimum investment. Ann. Prob., 16, 876-898.
Aucamp, D. (1993). On the extensive number of plays to achieve superior performance with the
geometric mean strategy. Manage. Sci. 39, 1163-1172.
Bell, R.M., and T.M. Cover (1980). Competitive optimality of logarithmic investment. Math. Oper.
Res. 5, 161-166.
Bell, R., and T.M. Cover (1988). Game-theoretic optimal portfolios. Manage. Sci. 34,724-733.
Bernoulli, D. (1738/1954). Exposition of a new theory on the measurement of risk (translation
Louise Summer). Econometrica, 22, 23-36.
Blume, M.E., and I. Friend (1975). The asset structure of individual portfolios and some implications for utility functions. 1. Finance 30, 585-603.
Breiman, L. (1960). Investment policies for expanding business optimal in a long-run sense. Nav.
Res. Logist. Q. 7, 647-651.
Breiman, L. (1961). Optimal gambling system for favorable games, in: Proc. 4th Berkeley Symp. on
Mathematics, Statistics and Probability 1, 63-68.
Chamberlain, G. (1983). A characterization of the distributions that imply mean-variance utility
functions. 1. Econ. Theory 29, 185-201.
.
Chernoff, H. (1980/1981). An analysis of the Massachusetts Numbers Game, Tech. Rep. No. 23,
MIT Department of Mathematics, Massachusetts Institute of Technology, Cambridge, MA.,
--- page 624 ---

Capital Growth Theory
595
Ch. 3. Capital Growth Theory
83
1980; shortened version published in Math. Intell. 3, 166-172.
Clark, R, and W:r. Ziemba (1987). Playing the turn of the year with index futures. Oper. Res. 35,
799-813.
Dohi, T., H. Tanaka, N. Kaio and S. Osaki (1994). Alternative Growth Versus Security in Continuous
Dynamic Trading. Eur. 1. Oper. Res., in press.
Efron, B., and e. Morris (1973). Stein's estimation rule and its competitors -
An empirical Bayes
approach. 1. Am. Stat. Assoc. 68, 117-130.
Efron, B., and e. Morris (1975). Data analysis using Stein's estimator and its generalizations. 1.
Am. Stat. Assoc. 70, 311-319.
Efron, 8., and e. Morris (1977). Stein's paradox in statistics. Sci. Am. 236, 119-127.
Epstein, RA. (1977). The Theory of Gambling and Statistical Logic, 2nd edition, Academic Press,
New York, NY.
Ethier, S.N. (1987). The Proportional Bettor's Fortune, in: Proe. 7th Int. Con! on Gambling and
Risk Taking, Department of Economics, University of Nevada, Reno, NY.
Ethier, S.N., and S. Tavare (1983). The proportional bettor's return on investment. I. Appl. Probab.
20, 563-573.
Feller, W. (1962). An Introduction to Probability Theory and Its Applications, 1, 2nd edition, John
Wiley & Sons, New York, NY.
Ferguson, T.S. (1965). Betting systems which minimize the probability of ruin. 1. Soc. Appl. Math.
13, 795-818.
Finkelstein, M., and R. Whitley (1981). Optimal strategies for repeated games. Adv. Appl. Prob. 13,
415-428.
Fisher, !. (1930). The Theory of Interest, New York, MacMillan, reprinted Augustus Kelley, 1965.
Friedman, J. (1982). Using the Kelly criterion to select optimal blackjack bets, Mimeo, Stanford
University.
Goldman, 8. (1974). A negative report on the 'near optimality' of the max-expected log policy as
applied to bounded utilities for long-lived programs. 1. Finane. Econ. 1,97-103.
Gottlieb, G. (1984). An optimal betting strategy for repeated games, Mimeo, New York University.
Gottlieb, G. (1985). An analystic derivation of blackjack win rates. Oper. Res. 33, 971-988.
Grauer, R.R. (1981). A comparison of growth optimal and mean variance investment policies. 1.
Finane. Quant. Anal. 16, 1-21.
Grauer, R.R. (1986). Normality, Solvency and Portfolio Choice, I. Finane. Quant. Anal. 21, 265-
278.
Grauer, R.R., and N.H. Hakansson (1982). Higher return, lower risk: Historical retuflU; on longrun, actively managed portfolios of stocks, bonds and bills, 1936-1978. Finane. Anal. 1. 38,
39-53.
Grauer, RR, and N.H. Hakansson (1985). Returns on levered, actively managed long-run portfolios of stocks, bonds and bills, 1934-1984. Finane. Anal. 1. 41,24-43.
Grauer, RR, and N.H. Hakansson (1986). A half-century of returns on levered and unlevered
portfolios of stocks, bonds, and bills, with and without small stocks. 1. Bus. 59, 287-318.
Grauer, RR., and N.H. Hakansson (1987). Gains from international diversification: 1968-85
returns on portfolios of stocks and bonds. 1. Finance 42, 721-739.
Grauer, R.R, and N.H. Hakansson (1993). On the use of mean-variance and quadratic approximations in implementing dynamic investment strategies: A comparison of returns and investment
policies. Manage. Sci. 39, 856-871.
Grauer, R.R., and N.H. Hakansson (1994a). On timing the market: The empirical probability
approach with an inflation adapter, Manuscript.
Grauer, RR., and N.H. Hakansson (1994b). Gains from diversifying' into real estate: Three decades
of portfolio returns based on the dynamic investment model, Real Estate Economics 23, 119-159.
Grauer, RR., and .N.H. Hakansson (1995). Stein and CAPM estimators of the means in asset
allocation, Working Paper (forthcoming)
Grauer, RR, N.H. Hakansson and Ee. Shen (1990). Industry rotation in the U.S. stock market:
1934-1986 returns on passive, semi-passive, and active strategies. 1. Banking Finance 14, 513-535.
--- page 625 ---

596
N. H. Hakansson and W T. Ziemba
84
NH. Hakansson, WT. Ziemba
Griffin, P. (1985). Different measures of win rate for optimal proportional betting. Manage. Sci. 30,
1540-1547.
Hakansson, N. (1969). Optimal investment and consumption strategies under risk, an uncertain
lifetime, and insurance. Int. Econ. Rev. 10, 443-466.
Hakansson, N. (1970). Optimal investment and consumption strategies under risk for a class of
utility functions. Econometrica 38, 587-607.
Hakansson, N. (1971a). Capital growth and the mean-variance approach to portfolio selection. 1.
Financ. Quant. Anal. 6, 517-557.
Hakansson, N. (1971b). Optimal entrepreneurial decisions in a completely stochastic environment.
Manage. Sci., Theory 17, 427-449.
Hakansson, N. (1971c). On optimal myopic portfolio policies, with and without serial correlation
of yields. 1. Bus. 44, 324-234.
Hakansson, N. (1972). Sequential investment-consumption strategies for individuals and endowment funds with lexicographic preferences, in: J. Bicksler (ed.), Methodology in Finance -
Investments, D.C. Heath & Company, Lexington, MA, pp. 175-203.
Hakansson, N. (1974). Convergence to isoelastic utility and policy in multiperiod portfolio choice.
1. Financ. Econ. 1, 201-224.
Hakansson, N. (1979). A characterization of optimal multiperiod portfolio policies, in: E. Elton
and M. Gruber (eds.), Ponfolio Theory, 25 Years Later, Amsterdam, North Holland, pp. 169-177.
Hakansson, N. (1989). On the value of adapting to inflation in sequential portfolio decisions, in:
B. Fridman and L. Ostman (eds.), Accounting Development -
Some Perspectives, The Economic
Research Institute, Stockholm School of Economics, pp. 151-185.
Hakansson, N., and B. Miller (1975). Compound-return mean-variance efficient portfolios never
risk ruin. Manage. Sci. 22, 391-400.
Hausch, D., and WT Ziemba (1985). Transactions costs, extent of inefficiencies, entries and
multiple wagers in a racetrack betting model. Manage. Sci. 31, 381-392.
Hausch, D., and W.T Ziemba (1990). Arbitrage strategies for cross-track betting on major horse
races. 1. Bus. 63, 61-78.
Hausch, D., and WT Ziemba (1995). Efficiency of sports and lottery betting markets, in: R.
Jarrow, V. Maksimovic and WT Ziemba (eds.), Finance, Handbooks in Operations Research
and Management Science, Vol 9, Elsevier, Amsterdam, pp. 545-580 (this volume).
Hausch, D., WT Ziemba and M. Rubinstein (1981). Efficiency of the market for racetrack betting.
Manage. Sci. 27, 1435-1452.
Hausch, D., R. Bain and WT Ziemba (1995). Wagering on the Kentucky Derby, 1934-1994,
Mimeo, University of British Columbia.
Huberman, G., and S. Ross (1983). Portfolio turnpike theorems, risk aversion and regularly varying
utility functions. Econometrica 51, 1345-136l.
Ibbotson Associates, Inc. (1986). Stocks, Bonds, Bills and Inflation: Market Results for 1926-1985,
Ibbotson Associates, Inc., Chicago.
Ibbotson Associates, Inc. (1988). Stocks, Bonds, Bills and Inflation: 1987 Yearbook, Ibbotson
Associates, Inc., Chicago.
James, W, and C. Stein (1961). Estimation with quadratic loss, in: Proc. 4th Berkeley Symp. on
Probability and Statistics I, Berkeley, University of California Press, pp. 361-379.
Jobson, J.D., and B. Korkie (1981).. Putting Markowitz theory to work. 1. Ponfolio Manag. 7,70-74.
Jobson, J.D., B. Korkie and V. Ratti (1979). Improved estimation for Markowitz portfolios using
James-Stein type estimators. in: Proc. American Statistical Association, Business and Economics
Statistics Section 41, 279-284.
Jorion, P. (1985). International portfolio diversification with estimation risk. 1. Bus. 58, 259-278.
Jorion, P. (1986). Bayes-Stein estimation for portfolio analysis. 1. Financ. Quant. Anal. 21,279-292.
Jorion, P (1991). Bayesian and CAPM estimators of the means: Implications for portfolio selection.
1. Banking Finance 15, 717-727.
Kalymon, B. (1971). Estimation risk in the portfolio selection model. 1. Financ. Quant. Anal. 6,
559-582.
--- page 626 ---

Capital Growth Theory
597
Ch. 3. Capital Growth Theory
85
Kallberg, 1.G., and w.T. Ziemba (1979). On the robustness of the Arrow-Pratt risk aversion
measure. Econ. Lett. 2, 21-26.
Kallberg, 1.G., and w.T. Ziemba (1983). Comparison of alternative utility functions in portfolio
selection problems. Manage. Sci. 9, 1257-1276.
Karatzas, I., 1. Lehoczky, S.P. Sethi and S.F. Shreve (1986). Explicit Solution of a General
Consumption/Investment Problem. Math. Oper. Res. 11, 261-294.
Kelly, 1.L., lr. (1956). A new interpretation of information rate. Bell Syst. Tech. 1. 35 917-926.
Kroll, Y., H. Levy and H. Markowitz (1984). Mean-variance versus direct utility maximization. I.
Finance 39, 47-75.
Latane, H. (1959). Criteria for choice among risky ventures. 1. Polito Econ. 67, 144-145.
Leland, H. (1972). On turnpike portfolios, in: K. Shell and G.P. Szego (eds.), Mathematical Methods
in Investment and Finance, Amsterdam, North-Holland.
Levy, H., and H. Markowitz (1979). Approximating expected utility by a function of mean and
variance. Am. Econ. Rev. 69,308-317.
Li, Y. (1993). Growth-security investment strategy for long and short runs. Manage. Sci. 39, 915-
934.
Li, Y., and w.T. Ziemba (1992). Security aspects of optimal growth models with minimum expected
time criteria, Mimeo, University of British Columbia, Canada.
Loistl, O. (1976). The erroneous approximation of expected utility by means of a Taylor's series
expansion: Analytic and computational results. Am. Econ. Rev. 66, 904-910.
MacLean, L.C, and w.T. Ziemba (1986). Growth versus security in a risky investment model, in:
F. Archetti, G. DiPillo and M. Lucertini (eds.), Stochastic Programming, Springer Verlag, pp.
78-87.
MacLean, L.C, and w.T. Ziemba (1990). Growth-security profiles in capital accumulation under
risk. Ann. Oper. Res. 31, 501-509.
MacLean, L.C, and w.T. Ziemba (1994). Capital growth and proportional investment strategies,
Mimeo, Dalhousie University.
MacLean, L.C, w.T. Ziemba and G. Blazenko (1992). Growth versus security in dynamic investment
analysis. Manage. Sci. 38, 1562-1585.
Markowitz, H.M. (1959). Portfolio Selection: Efficient Diversification of Investments. 10hn Wiley &
Sons, Inc., New York, NY.
Markowitz, H. (1976). Investment for the long run: New evidence for an old rule. I. Finance 31,
1273-1286.
Merton, R.C (1971). Optimal consumption and portfolio rules in a continuous-time model. I .
Econ. Theory 3, 373-413.
Merton, R.C. (1973). An intertemporal capital asset pricing model. Econometrica 41, 867-887.
Merton, R.C. (1980). On estimating the expected return on the market: An exploratory investigation. 1. Financ. Econ. 8, 323-361.
Miller, B.L. (1974). Optimal consumption with a stochastic income stream. Econometrica 42, 253-
266.
Mossin, J. (1968). Optimal multiperiod portfolio policies. 1. Bus. 41, 215-229.
Mulvey, 1.M. (1993). Incorporating transaction costs in models for asset allocation, in: Financial
Optimization, S. Zenios (ed.) Cambridge University Press.
Mulvey, 1.M., and H. Vladimirou (1992). Stochastic network programming for financial planning
problems. Manage. Sci. 38, 1642-1664.
Mulvey, 1.M., and w.T. Ziemba (1995). Asset and liability allocation in a global environment. in:
R. larrow, V. Maksimovic and w.T. Ziemba (eds.), Finance, Handbooks in Operations Research
and Management Science, Vol 9, Elsevier, Amsterdam, pp. 435-464 (this volume).
Ohlson, 1.A. (1975). The asymptotic validity of quadratic utility as the trading interval approaches
zero, in: w.T. Ziemba and R.G. Vickson (eds.), Stochastic Optimization Models in Finance,
Academic Press, New York, NY.
Pulley, L.B. (1981). A general mean-variance 'approximation to expected utility for short holding
periods. I. Financ. Quant. Anal. 16, 361-373.
--- page 627 ---

598
N. H. Hakansson and W. T. Ziemba
86
N.H. Hakansson, WT. Ziemba
Pulley, L.B. (1983). Mean-variance approximation to expected logarithmic utility. Oper. Res. 31,
685-696.
Ritter, J.R. (1988). The buying and selling behavior of individual investors at the turn of the year:
Evidence of price pressure effects. 1. Finance 43, 701-719.
Roll, R. (1983). Was ist das? The turn of the year effect and the return premia of small firms. 1.
Portfolio Manag. 10, 18-28.
Ross, S. (1974). Portfolio turnpike theorems for constant policies. 1. Financ. Econ. 1, 171-198.
Rotando, L.M., and E.O. Thorp (1992). The Kelly criterion and the stock market. Am. Math. Mon.
December, 922-931.
Rubinstein, M. (1977). The strong case for log as the premier model for financial modeling, in: H.
Levy and M. Sarnat (eds.), Financial Decisions Under Uncertainty, Academic Press, New York,
NY.
Rubinstein, M. (1991). Continuously rebalanced investment strategies. 1. Portfolio Manage. 17,
78-81.
Samuelson, P.A. (1970). The fundamental approximation theorem of portfolio analysis in terms of
means, variances, and higher moments. Rev. Econ. Studies 36, 537-542.
Samuelson, P.A. (1971). The 'fallacy' of maximizing the geometric mean in long sequences of
investing or gambling. Proc. Nat. Acad. Sci. 68, 2493-2496.
Samuelson, PA. (1977). St. Petersburg paradoxes: Defanged, dissected, and historically described.
1. Econ. Lit. XV, 24-55.
Sethi, S.P and M.1. Taksar (1988). A Note on Merton's Optimum Consumption and Portfolio Rules
in a Continuous-Time Model. 1. Econ. Theory 46, 395-401.
Stein, C. (1955). Inadmissibility of the usual estimator for the mean of a multivariate normal
distribution, in: Proc. 3rd Berkeley Symp. on Probability and Statistics I, University of California
Press, Berkeley, CA, pp. 197-206.
Thorp, E.O. (1966). Beat the Dealer, 2nd edition, Random House, New York, NY.
Thorp, E.O. (1975). Portfolio choice and the Kelly criterion, in: WT. Ziemba and R.G. Vickson
(eds.), Stochastic Optimization Models in Finance, Academic Press, New York, NY.
Williams, J. (1936). Speculation and carryover. Q. 1. Econ. L, 436-455.
Wu, M.G.H., and WT. Ziemba (1990). Growth versus security tradeoffs in dynamic investment
analysis, Mimeo, University of British Columbia, B.C.
Ziemba, WT. (1994). Investing in the turn of the year effect in the U.S. futures markets. Interfaces
24, 46-61.
Ziemba, WT., and D.B. Hausch (1986). Betting at the Racetrack, Dr. Z Investments, Inc., Los
Angeles and Vancouver.
Ziemba, WT., and D.B. Hausch (1987). Dr. Z's Beat the Racetrack, William Morrow, New York
(revised and expanded second edition of Ziemba-Hausch, Beat the Racetrack, Harcourt, Brace
and Jovanovich, 1984).
Ziemba, WT., C. Park an and R. Brooks-Hill (1974). Calculation of investment portfolios with
risk-free borrowing and lending. Manage. Sci. 21, 209-222.
Ziemba, WT., S.L. Brumelle, A. Gautier and S.L. Schwartz (1986). Dr. Z's 6/49 Lotto Guidebook,
Dr. Z Investments, Inc., Los Angeles and Vancouver.
Ziemba, WT. and R.G. Vickson (eds.) (1975). Stochastic Optimization Models in Finance, Academic Press, New York, N.Y.
--- page 628 ---

Journal of Economic Dynamics and Control 11 (1993) 881-906. North-Holland
42
A preference foundation for log
mean-variance criteria in
portfolio choice problems
David G. Luenberger
Stanford University. Stanford. CA 94305. USA
Received October 1991, final version received June 1992
599
The appropriate criterion for evaluating, and hence also for properly constructing, investment
portfolios whose performance is governed by an infinite sequence of stochastic returns has long been
a subject of controversy and fascination. A criterion based on the expected logarithm of one-period
return is known to lead to exponential growth with the greatest exponent, almost surely; and hence
this criterion is frequently proposed. A refinement has been to include the variance of the logarithm
of return as well, but this has had no substantial theoretical justification.
This paper shows that log mean-variance criteria follow naturally from elementary assumptions
on an individual's preference relation for deterministic wealth sequences. As a first and fundamental
step, it is shown that if a preference relation involves only the tail of a sequence, then that relation
can be extended to stochastic wealth sequences by almost sure equality. It is not necessary to
introduce a von Neumann-Morgenstern utility function or the associated axioms.
It is then shown that if tail preferences can be described by a 'simple' utility function, one that is of
the form lim._~p( W., II) where W. is wealth at period II, this utility must under suitable conditions
be a function of the expected logarithm of return, independent of the functional form of p. Finally,
'compound' utility functions are introduced; and they are shown under suitable conditions to be
functions of the expected value and variance of the logarithm of one-period return, again independently of the specific form ofthe underlying function. The infinite repetitions of the dynamic process
essentially 'hammer' all utility functions into a log mean-variance form.
I_ Introduction
Consider an investment situation wherein a fund is initially endowed with
capital and, through returns from investment, grows (or decreases) with time.
After the initial endowment, no additions or withdrawals are made. The initial
endowment is simply transformed by repeated chance operations of investment
as controlled by the portfolio structure. The management objective in this
Co"espolldellce to: David G. Luenberger, Department of Engineering-Economic Systems, Stanford
University, Stanford, CA 94305-4025. USA.
·The author wishes to thank David R. Carino for many helpful suggestions on this paper.
0165-1889/93/$06.00 © 1993-Elsevier Science Publishers B.V. All rights reserved
