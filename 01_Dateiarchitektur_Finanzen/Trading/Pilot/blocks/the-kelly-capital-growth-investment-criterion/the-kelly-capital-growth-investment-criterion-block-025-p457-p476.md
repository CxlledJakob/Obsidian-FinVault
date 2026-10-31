# The Kelly capital growth investment criterion _ theory and -- Leonard C_ Maclean, Edward O_ Thorp, W_ T_ Ziemba, Leonard -- World Scientific Handbook -- isbn13 9781283148344 -- bec576e26410d0c695fd5b867d08ec4f -- An.pdf — pages 457–476

--- page 457 ---

428
M A. H. Dempster, 1. V. Evstigneev and K. R. Schenk-Hoppe
specific points in time. It is an active portfolio management that rebalances positions by selling assets, whose portfolio value exceed the given benchmark to finance
the purchase of those assets with a too low weight in the portfolio.
The significance of constant proportions strategies for investment science was
established in Kelly (1956)'s work on information theory and its application to
betting markets. A detailed account is provided in Part I of this volume. Kelly's
research was inspired by Claude Shannon's lectures on investment problems in which
the founder of the mathematical theory of information outlined his pioneering ideas
in the field of investment science (though he never published in it); see Cover (1998)
for the history of this approach.
The optimality property of the Kelly rule, which maximizes the growth rate of
capital in the case of independent and identically distributed returns on investment,
motivated the research on the log-optimum investment principle, Breiman (1961),
Algoet and Cover (1988), MacLean, Ziemba and Blazenko (1992), Hakansson and
Ziemba (1995), Browne and Whitt (1996), Cover (1991), Li (1998), and others. Constant proportions strategies have been studied in many different frameworks, e.g.,
Browne (1998), Luenberger (1998), Aurell et al. (2000) and Aurell and Muratore-
Ginanneschi (2000), Fernholz (2002), Fernholz and Karatzas (2005), Fernholz et al.
(2005), Evstigneev, Hens and Schenk-Hoppe (2009a, 2009b), Kuhn and Luenberger
(forthcoming). This approach has proved quite successful in practical finance as
witnessed by a considerable body of empirical literature, see Thorp (1971), Perold
and Sharpe (1988), Ziemba and Mulvey (1998), Mulvey (2001, 2009), Dries et al.
(2002), Dempster et al. (2003), Mulvey et al. (2007), and others as well as Part VI
in this volume.
In contrast to this literature on investment, we will ignore questions of optimality of trading strategies and will not make use of expected utility or related
concepts. Our goal is to analyze the performance of arbitrary fixed-mix (constant
proportions) strategies in markets with different characteristics. We are only interested in 'generic' properties of (not necessarily optimal) fixed-mix strategies and
their performance relative to buy-and-hold strategies. l
This survey is based on the authors' research, Evstigneev and Schenk-Hoppe
(2002) and Dempster, Evstigneev, and Schenk-Hoppe (2003, 2007, 2008) . In these
papers, we study the wealth dynamics of investors employing fixed-mix strategies.
Very general (and mostly counter-intuitive) results on fixed-mix strategies are obtained under the assumption that markets will exhibit some degree of stationarity
either of (relative) prices or returns. This assumption of stationarity of asset returns
is widely accepted in financial theory (and, thus, the basis for practical investment
advice) allowing, as it does, expected exponential price growth and mean reversion,
volatility clustering and very general intertemporal dependence, such as long memory effects, of returns. Stationarity of returns for instance is a salient feature of the
Cox-Ross-Rubinstein binomial asset pricing model.
lOf course it is well-known that optimally-chosen rebalancing strategies perform at least as well
as any buy-and-hold portfolio, see Part II in this volume.
--- page 458 ---

Growing Wealth with Fixed-Mix Strategies
429
The remainder of this chapter is organized as follows. Section 1.1 invites the
readers to test their intuition while Section 1.2 provides a very simple illustrative
example. The general theory of constant proportions strategies in stationary markets is covered in Section 2. A generalization to fixed-mix strategies as well as an
application to currency market models is given in Section 3. The most intriguing case of stock markets with stationary returns, covered in Section 4, delivers
counter-intuitive results that even experienced researchers find puzzling. Section 5
discusses several prominent explanations for volatility-induced growth and provides
an interpretation that agrees with our findings. Section 6 concludes.
1.1
A test of your intuition
There is barely any 'better' result than one that is (completely) counter-intuitive.
But before one is tempted to make such a claim on one's own findings, it seems
appropriate to test the audience's intuition. In the following, we ask a few questions
to which the reader has to promptly guess the answer. Many scientists have been
asked these questions casually in private, at seminars, and at conferences. The
following insights were first reported in Dempster, Evstigneev, and Schenk-Hoppe
(2007). Non-technically minded readers can skip to the next section which provides
the informal discussion of an intriguing example.
Stationary markets: puzzles and misconceptions. Consider a market with K assets whose price process Pt = (pi , ... ,pf) is ergodic and stationary. (It is assumed
that prices are log-integrable.) The assumption of stationarity of asset prices, perhaps after some detrending, seems plausible when modeling currency markets where
'prices' are determined by exchange rates of all the currencies with respect to some
selected reference currency.
Question 1. Suppose vectors of asset prices Pt = (pi,· .. ,pf) fluctuate randomly,
forming a stationary stochastic process (assume even that the vectors Pt are iid (independent identically distributed)). Consider a fixed-mix self-financing investment
strategy prescribing rebalancing one's portfolio at each of the dates t = 1,2, ... so
as to keep equal investment proportions of wealth in all the assets. What is the
tendency of the portfolio value in the long run, as t -> oo? Will the value: (a)
decrease; (b) increase; or (c) fluctuate randomly, converging (in some sense) to a
stationary process?
The audience of our respondents was quite broad and professional, but practically nobody succeeded in guessing the correct answer, which is (b). Among those
with a firm view, nearly all selected (c). There were also a couple of respondents
who decided to bet on (a). Common intuition suggests that if the market is stationary, then the portfolio value for a constant proportions strategy must converge
in one sense or another to a stationary process. The usual intuitive argument in
support of this conjecture appeals to the self-financing property. The self-financing
--- page 459 ---

430
M A. H. Dempster, 1. V. Evstigneev and K. R. Schenk-Hoppe
constraint seems to exclude possibilities of unbounded growth. This argument is
also substantiated by the fact that in the deterministic case both the prices and
the portfolio value are constant. This way of reasoning makes the answer (c) to the
above question more plausible a priori than the others.
It might seem surprising that the wrong guess (c) has been put forward even
by those who have known about examples of volatility pumping for a long time.
The reason for this might lie in the non-traditional character of the setting where
not only the asset returns but the prices themselves are stationary. Moreover,
the phenomenon of volatility-induced growth is more paradoxical in the case of
stationary prices, where growth emerges "from nothing". In the conventional setting
of stationary returns, volatility serves as the cause of an acceleration of growth,
rather than its emergence from prices with zero growth rates.
A potentially promising attempt to understand the correct answer to Question
1 might be to refer to the concept of arbitrage. Getting something from nothing
as a result of an arbitrage opportunity seems to be similar to the emergence of
growth in a stationary setting where there are no obvious sources for growth. As
long as we deal with an infinite time horizon, we would have to consider some kind
of asymptotic arbitrage. All known concepts of this kind2 however are much weaker
than what we would need in the present context. According to our results, growth
is exponentially fast, unbounded wealth is achieved with probability one, and the
effect of growth is demonstrated for specific (constant proportions) strategies. None
of these properties can be directly deduced from asymptotic arbitrage.
Thus, there are no convincing arguments showing that volatility-induced growth
in stationary markets can be derived from, or explained by, asymptotic arbitrage
over an infinite time horizon. But what can be said about relations between stationarity and arbitrage over finite time intervals? As is known, there are no arbitrage
opportunities (over a finite time horizon) if and only if there exists an equivalent
martingale measure. A stationary process can be viewed as an 'antipodal concept'
to the notion of a martingale. This might lead to the conjecture that in a stationary
market arbitrage is a typical situation. Is this true or not? Formally, the question
can be stated as follows.
Question 2. Suppose vectors of asset prices Pt = (pi , ... ,pf) form a stationary
stochastic process (assume even that the vectors Pt are iid) Furthermore, suppose
the first asset k = 1 is riskless with constant price pi = 1. The market is frictionless
and there are no portfolio constraints (in particular, short selling is allowed). Does
this market have arbitrage opportunities over a finite time horizon?
An arbitrage opportunity over a fixed time horizon is understood in the conventional sense: the existence of a trading strategy that does not require any investment
2E.g. Ross (1976) , Huberman (1982) , Kabanov and Kramkov (1994), and Klein and Schacher mayer
(1996).
--- page 460 ---

Growing Wealth with Fixed-Mix Strategies
431
Table 1 Net return of the two assets in t he market
Asset 1
Asset 2
Heads
+50%
-55%
Tails
- 40%
+ 100%
at the initial time, is self-financing, does not incur a loss at the terminal time, and
makes a gain with strictly positive probability. Again, the answer to this question
is practically never guessed immediately. The correct answer depends on whether
the distribution of the price vector of the risky assets is continuous or discrete.
For example, if (PT, ... ,pf) takes on a finite number of values, then an arbitrage
opportunity exists. But if its distribution is continuous, there are no arbitrage
opportunities. For details see Evstigneev and Kapoor (2006).
If your intuition led you astray, the remainder of this chapter will help to offer
insights into these counter-intuitive results. Even if your intuition led you to the
correct answers, you might be interested in the precise formulation of the results
and the ideas behind their proofs.
1.2
An illustrative example
The potential of constant proportions investment strategies for financial growth can
be demonstrated by means of the following example which seems simple enough to
be discussed at high-school level. A related example is presented in Dempster,
Evstigneev, and Schenk-Hoppe (2008) (see also Luenberger, 1998, Chapter 15). A
more demanding illustration, though with a sound empirical background, is given
in Ziemba (2008).
Two investment opportunities available at every point in time: 0, 1, 2 .... The
realized returns of the assets between two points in time are determined by flipping
a fair coin (only one!). Think of the outcome (heads/tails) as a economy-wide event
that effects the two investments in different ways. The net returns are defined in
Table l.
Investors who buy and hold the first asset will see their wealth decline (exponentially fast) over time. The grow rate is negative:
91 := 0.5 In(l.5) + 0.5 In(0.6) :::::0 - 0.05268 < 0
Investment in only the second asset does not yield any better performance because
the growth rate is negative as well and equal to 91:
92 := 0.5 In(0.45) + 0.5 In(2.0) = 91 < 0
Now consider an investor with a constant proportions strategy. Suppose the
investor divides his wealth 50 : 50 between the two assets. After each change in the
value of the two portfolio positions, the investor rebalances his portfolio by trading
assets to restore the 50: 50 split of wealth. The growth rate of his wealth is
0.5 In(0.5 . l.5 + 0.5· 0.45) + 0.5 In(0.5 . 0.6 + 0.5· 2.0) :::::0 +0.1185 > 0
--- page 461 ---

432
M A. H. Dempster, 1. V. Evstigneev and K. R. Schenk-Hoppe
60
50
40
30
20
10
-10
-20
-30
-40
0
250
500
750
1000
Figure 1 Wealth dynamics of the two passive investors (both decreasing) and the active investor
with 50: 50 constant proportions strategy (increasing). Initial wealth is 1.0. Logarithmic scale on
y-axis.
Both passive investors (holding only one asset) will see their wealth halve in less than
14 periods on average. In contrast, the investor following a constant proportions
strategies with proportions 50: 50 will, on average, double his wealth more often
than every 6th period. A typical realization of the wealth dynamics is depicted in
Figure 1.
The active investor's choice of the proportions is arbitrary. Indeed, qany constant proportions investment strategy holding both assets will generate growth in excess of either buy-and-hold strategy. The 50: 50 proportions create positive growth
while strategies with proportions close to 100: 0 (or 0 : 100) entail growth at negative
rate but one that is higher than gl = g2.
Examples, examples, examples. The above example is just one of many. Indeed
most descriptions (and analyses) of the phenomenon of generating financial growth
from volatility are restricted to examples involving specialized models. Since the
deduction of general principles from examples is an unreliable route if a thorough
mathematical analysis is feasible, it might come as no surprise that several terms
have been coined to describe this phenomenon and many different explanations
for its origins have been put forward. In the remainder of this chapter, we will
present mathematical results on the growth-volatility nexus in general (discretetime) models and attempt to de-mystify its origins and explanations.
1.3
Notation
All models discussed in this chapter share the basic setup. The definitions and
concepts are listed and discussed here. An investor observes prices and takes actions
--- page 462 ---

Growing Wealth with Fixed-Mix Strategies
433
only at particular points in time. These time periods are denoted t = 0, 1, 2, ....
The price dynamics are driven by random factors. These factors are described
by a stochastic process St with t = 0, ±1, ±2, .... The process takes values in a
measurable space S. The realization of the random parameter St corresponds to
the state of the world at time t. Denote by P the probability measure induced by
the stochastic process St, t = 0, ±1, ±2, . .. , on the space of its paths. There are
K :;:. 2 assets traded in the market. Asset prices Pt = (pi, .. . ,pf ) > 0, at the time
periods t = 0, 1, 2, ... are described as a sequence of strictly positive random vectors
with values in the K -dimensional linear space RK. We will assume that the price
vector Pt depends on the history of the process St up to time t:
It is supposed, without further mentioning, that all functions of st will be
measurable.
A market is called stationary if the process St is stationary and the price vectors
Pt do not explicitly depend on t, i.e., Pt = p(st ). We will further assume that the
process St is ergodic and that E llnpk(st)1 < 00 for all k = 1, ... , K.
A stochastic process 6 , 6, . .. is stationary if, for any m = 0, 1, 2, . .. and
any measurable function ¢(Xo, Xl , . .. , xm ) , the distribution of the random variable ¢t :=
¢ (~t, ~t+ l , ... '~t+m ) (t = 0, 1, ... ) does not depend on t. According to this definition, all probabilistic characteristics of the process ~t are timeinvariant.
If ~t is stationary, then for any measurable function ¢ for which
E I¢ (~t , ~t+l' ... '~t+m)
1 < 00 , the averages
¢ l + ... + ¢t
t
(1)
converge almost surely (a.s.) as t --+ 00 by Birkhofi"'s ergodic theorem -
see, e.g. ,
Billingsley (1965). If the limit of all averages of the form (1) is non-random (equal
to a constant a.s.) , then the process ~t is called ergodic. In this case, the above
limit is equal a.s. to the expectation E ¢t, which does not depend on t by virtue of
stationarity of ~t.
The exponential growth rate of a stochastic process 6 ,6 , ... with ~t > ° is
defined by
1
lim - ln~t
t ....,oo t
(2)
provided the limit exists. Suppose the process ~ is stationary and ergodic with
E In ~m < 00, then its growth rate zero because r lln ~t --+ ° a.s. by Proposition
4.1.3 in Arnold (1998). One also has
1
In 6 + ... + In ~t
tln(6 · ... ·~t) =
t
--+ Eln~m=const.(a. s .)
(3)
This property is frequently used below.
--- page 463 ---

434
M A. H. Dempster, 1. V. Evstigneev and K. R. Schenk-Hoppe
At each time period t, the investor chooses a portfolio ht (st) = (hi( st), ... ,
hr (st)) with a non-negative number of units of asset k, h~(st) 2: O. Short selling of
assets is ruled out in our model by this assumption of non-negativity. A sequence
ht(st) , t = 0,1,2, ... , of portfolios is called a trading strategy. The value of a
portfolio ht at time t is Ptht = LkP~h~.
A trading strategy H = (ho , h1 , ... ) with initial wealth wo > 0 is self-financing
if Po ho = Wo and
(4)
The inequalities in (4) are supposed to hold almost surely with respect to the
probability measure P. The market value of the portfolio after trade does not
exceed the vale of the yesterday's portfolio at current prices. This budget constraint
restricts the investor's choice.
A balanced trading strategy H is of the form
(5)
with a scalar-valued function 'YO > 0 and a vector function h(.) 2: O. If t = 0, we
assume that ho(sO) = h(sO). It is assumed that In 'Y(st) and In Ih(st) 1 are integrable
with respect to the measure P , i.e., El ln 'Y(st)1 and El lnlh(st)11 are finite. Define
Ih l = Lk Ihkl for a vector h = (hk).
These strategies are called balanced because they are of balanced growth: (5)
implies that all proportions between the amounts of different assets in the portfolio
h~ (st)
h~ (st)
hj (st)
hk(st) ,
j-=!=k
(6)
form stationary stochastic processes. The random growth rate of the amount of
each asset k = 1, . . . , K , in the portfolio
hk(st)
hk(st)
h~_: (st-l) = 'Y(st) hk(st-l)
is a stationary process. A balanced strategy is self-financing (4) if and only if
(7)
Stationarity implies that if (7) holds for some t, it holds for all t.
Suppose the vector of asset prices is stationary. Then every non-negative vector
function h(st) with Elln Ih(st) 11 < 00 defines a self-financing balanced strategy (5)
by
p(st) h(st-l)
'Y( st):= p( st) h( st)
since Ellnpk(st)1 < 00, and relations (4) and (7) hold as equalities.
(8)
--- page 464 ---

Growing Wealth with Fixed-Mix Strategies
435
Balanced trading strategies have the property that the growth rate of wealth
of any investor employing it is completely determined by the expected value of "(.
Proposition 1 in Evstigneev and Schenk-Hoppe (2002) states that for any balanced
trading strategy (5)
lim ~ In(p( st) ht( st)) = lim ~ In I ht (st) I = E In "(( so)
(a.s.)
(9)
t->oo t
t->oo t
This result shows strict positivity of E In "(( sO) == E In "(( st) implies exponential
growth of wealth, i.e., p(st) ht(st) ---> 00 a.s. exponentially fast.
2
Asset Markets with Stationary Prices
We first discuss the simplest model in which one can analyze generic properties of
fixed-mix strategies: a market in which prices are stationary processes. It turns out
that any constant proportions strategy produces growth, though in this stationary
market the growth rate of each asset price is zero and, therefore, buy-and-hold
strategies do not yield positive growth. This results might seem, at the first glance,
counter-intuitive. This section is based on Evstigneev and Schenk-Hoppe (2002).
All notations are introduced in Section 1.3.
2.1
The model
A constant proportions strategy in a market with K assets is characterized by a
vector A = (Al' ... , AK) in the set
~ = {(Al"'" AK) E RK : Ak > 0, t Ak = I}
k=l
(10)
To avoid pathological cases, we assume strict positivity of all components. Proportional investment rules of this kind are sometimes termed completely mixed.
The trading strategy ht is a constant proportions strategy if
(11)
for all t = 1, 2, ... and k = 1, ... ,K. The investor rebalances the portfolio in every
period in time by investing the constant share Ak of the wealth Pt ht- 1 into the kth
asset. The investor's wealth at the beginning of period t is determined by evaluating
the portfolio ht - 1 (bought in the previous period) at the current price system p~.
We assume that all the coordinates of ht are non-negative: short sales are ruled
out.
Constant proportions strategies are self-financing because (11) implies
Pt ht = Pt ht- 1
Given a vector A, the strategy is uniquely defined by its initial portfolio ho (sO).
Recursive application of (11) determines ht(st) for every t = 1, 2, ....
--- page 465 ---

436
M A. H. Dempster, 1. V. Evstigneev and K. R. Schenk-Hoppe
In the study of the growth rate of wealth, the initial portfolio does not matter,
see Evstigneev and Schenk-Hoppe (2002, pp. 568). Indeed if there are two constant
proportions strategies ht and ht both generated by the same A E ~ but with different
(non-zero) initial portfolios, then there exist~ , C > 0 such that ~h~ ::::; h~ ::::; ch~ for
all k and all t ~ 1. Obviously, lim C 1 ln Ihtl > 0 a.s. if and only if lim C 1 ln Ihtl > 0
a.s. (and exponential growth is at the same speed).
2.2
The growth rate
Constant proportions strategies generate balanced portfolios. From the representation (5), the growth rate of the investors wealth is obtained as the expected value
E In 1'( sO). The notion of balanced portfolios goes back, though in a somewhat different form, to Radner (1971)'s study of stochastic generalizations of the von Neumann economic growth model. Arnold, Evstigneev, and Gundlach (1999) study
this concept of balanced paths in a general setting. The application to financial
problems is recent.
The central result on the growth rate of constant proportions strategies in markets with stationary asset prices is obtained by showing that they can be written
as balanced strategies and that E In 1'( sO) ~ O. To have a strictly positive growth
rate, the price process p( st) must be non-degenerate.
We impose the following assumption:
(A) With strictly positive probability, the random variable
pk(st)jpk(st-l )
is not constant with respect to k = 1,2, . . . ,K , i.e., there exist m and n (that might
depend on st) for which
(12)
All results in this Handbook section will be proved under this assumption, though
it will be convenient to repeat this condition in different disguiseseach best suited
for the particular application.
Under assumption (A), one has the following result, see Evstigneev and Schenk-
Hoppe (2002, Theorem 1).
Theorem 1. Fix any A = (AI"'" AK) E ~ , and let Wo be a strictly positive
number.
Then there exists a vector function ho(sO) ~ 0 such that the constant
proportions strategy ht generated by A and ho is a balanced strategy with initial
wealth wo, and we have
.
1
.
1
hm -lnptht = hm -In Ihtl > 0
(a.s.)
t->oo t
t->oo t
(13)
The construction of the vector function ho(sO) ~ 0 is as follows. Suppose the
proportions A E ~ and initial wealth Wo > 0 are given. To show that ht is a balanced
--- page 466 ---

Growing Wealth with Fixed-Mix Strategies
437
trading strategy one needs to define a vector function he) :::: 0 and a scalar-valued
function /,(.) > 0 such that ht coincides with the strategy defined in (5) (and that
ht(sO ) = h(sO)) . Define
-
t
( Al Wo
AK Wo )
h(s ) =
pl(st) " ' " pK (st)
(14)
and
t
_ p(st) h(st-l ) [_ K
pk(st) 1
/,(s)-
- LAk k( t-l)
Wo
k= l
P s
(15)
This is a balanced trading strategy which coincides with ht recursively defined by
(11).
Strictly positive growth (E In /,( st) > 0) holds because Jensen's inequality (applied to the probability measure Ak on the set {I, ... , K} ) implies that
K
pk(st )
K
pk(st)
In L Ak pk (st-l ) :::: L Ak In pk(stl)
k=l
k=l
(16)
with strict inequality on a set of positive probability by assumption (12), which
ensures
t
K
pk(st) _
E ln /,(s) > LAkE ln k(st-l) - 0
k=l
P
Strict positivity of E In /,( st) means that wealth tends to infinity at an exponential rate. If the non-degeneracy condition (A) is not satisfied, the market is
essentially deterministic and all prices are constant. In this case, all strategies give
zero growth. Indeed, (12) is a very weak requirement that is satisfied in virtually
every market.
The result presented in Theorem 1 holds under (sufficiently) small proportional
transaction costs, see Evstigneev and Schenk-Hoppe (2002, Theorem 2).
2.3
Interpretation
Our analysis shows that constant proportions strategies provide growth in a market
in which buy-and-hold strategies do not deliver any. The intuition behind this result
is that constant proportions strategies 'exploit ' the persistent fluctuation of prices.
When keeping a fixed fraction of wealth invested in each asset , a change in prices
leads the investor to sell those assets that are expensive relative to the other assets
and to purchase relatively cheap assets. The stationarity of prices implies that this
portfolio rule yields a strictly positive expected rate of growth, despite the fact that
each asset price has growth rate zero. The notion of an asset being 'cheap' resp.
'expensive' makes sense when prices are stationary. If the current price is below
the expected value, then the tomorrow's price has a higher-than-average chance
of being larger than today's price. This asset is cheap today. In other words, if
--- page 467 ---

438
M A. H. Dempster, 1. V. Evstigneev and K. R. Schenk-Hoppe
prices are stationary, there is reversion to the median (which is also true for price
ratios). Rebalancing strategies, on average, buy low and sell high. In the model
with stationary returns (rather than prices), accepting this interpretation would be
falling victim to the gambler's fallacy, see Section 4.
The result highlights the benefit of financial engineering. The implementation
of a constant proportions strategy requires to invest actively in the available assets
by rebalancing at discrete time periods -
the growth is financially engineered by
making use of Jensen's inequality.
3
Fixed-Mix Strategies in Stationary Markets
The model with constant proportions strategies can be generalized to accommodate
the transfer of fractions between different portfolio positions. An application to
currency markets is provided. In this model, the exchange rates fluctuate randomly
in time as stationary stochastic processes. This aspect of our analysis is inspired,
in particular, by recent work of Kabanov (1999) and Kabanov and Stricker (2001).
This section follows Dempster, Evstigneev, and Schenk-Hoppe (2003). Again, the
main result holds under small proportional transaction costs.
3.1
The model
A fixed-mix strategy is determined by a (non-random) matrix Akj, k, j = 1, . . . ,K,
such that
K
Akj > 0 , L Akj = 1
(17)
k=l
In each time period, this strategy prescribes the transfer of a fixed share Akj > 0
of the jth position of the portfolio to the kth position (k, j E {I, ... , K}). The
dynamics of the wealth invested in the portfolio positions are given by
K
kk_ ,\",
jj
Pt ht - ~
AkjPt ht-1
(18)
j=l
For any matrix Akj satisfying (17)), a strategy H is called a fixed-mix strategy
associated with the matrix A = (Akj), if (18) holds for all k, t and st.
Any fixed-mix strategy is self-financing: Ptht = Ptht-1. As in the previous
section, we are interested in the asymptotic behavior of the portfolio ht (and its
market value) of a trader employing a fixed-mix investment rule.
In the deterministic case, the analysis of the long-term dynamics is simple.
The price Pt = P = (pI, ... ,pk) > 0 is a constant vector. The corresponding
process ht defined by (18) is deterministic and will always converge to a steady
state. This claim follows from results on positive matrices, Kemeny and Snell (1960).
This result, combined with the assumption of stationarity, might seem to rule out
--- page 468 ---

Growing Wealth with Fixed-Mix Strategies
439
unbounded growth and could lead to the (wrong) conjecture of the convergence of
ht to a stationary distribution in the stochastic case.
The case studied in Section 2 corresponds to the situation in which Akj does not
depend on j:
Akj = Ak with Ak > 0 ,
and
Al + ... + AK = 1
because (18) reduces to (11).
3.2
Currency markets
(19)
The foreign exchange market is arguably the real-world example closest to a market
in which prices are stationary. We show to formulate the wealth dynamics of a
currency trader with a fixed-mix strategy in the above model.
Currencies k = 1,2, ... , K are traded in a frictionless market. The exchange
k"
"
k"
rates 7r/ = 7rkl(st) > 0 fluctuate randomly in time. The real number 7r/ denotes
the amount of currency k which can be purchased by selling one unit of currency j
at time t. We assume absence of arbitrage at each point in time t, i.e.z the exchange
rates must satisfy
~kj _
~km ~mj
Ht
-
Ht
Ht
(20)
for all k, m and j.
Assume the trader follows any fixed-mix strategy (17) by dividing the holdings
hLl 2:: 0 of currency j purchased at time t-l according to the proportions Akj > 0,
k = 1, ... , K at time t. The amount AkjhLl is exchanged into currency k. After
execution of all these transactions, the amount of currency k obtained at time t is
equal to
(21)
The dynamics (21) can be written in the form (18). Take currency 1 as a numeraire
and define
Pk _
~lk
t -
Ht
k"k
""
k""
The relation (20) implies 7r/ = l/7ri
and 7ril = 1. Therefore, 7r/ = pUp~.
Multiplying (21) by 7rik and using these relations, yields the formulation (18) of the
wealth dynamics.
3.3
The growth rate
The analysis of the long-term growth of an investor following a fixed-mix strategy is
conceptually identical to that of constant proportions strategies. First, one shows
that there is an initial portfolio such that the fixed-mix strategy leads to a balanced portfolio. Then, one proves that the growth rate is independent of the initial
--- page 469 ---

440
M A. H. Dempster, I. V Evstigneev and K. R. Schenk-Hoppe
portfolio. Finally, one shows that this growth rate is strictly positive under a nondegeneracy condition. The mathematical tools required in the proof however are
very different. The case of fixed-mix strategies requires considerably more advanced
methods.
As in Section 2 we assume that the market is stationary and the state of the
world St is ergodic. The price process Pt = p(st) satisfies Ellnpk(st)l < 00 for all
k = 1, ... ,K. The growth rate of each asset price is zero because C 1 lnpt --+ 0 a.s.
and, therefore, buy-and-hold strategies do not yield positive growth.
We assume non-degeneracy of the price process p(st):
(B) The vector 15(st) = (151 (st), ... ,15K (st)) of normalized prices
_
t
pj(st)
jY(s):= Lmpm(st)
j E {l,,,.,K}
is not constant a.s. with respect to st.
This assumption says that there is no constant vector c for which 15(st) = c
almost surely. By virtue of stationarity of (St), condition (B) holds for all t if
is satisfied for some t. If St is ergodic, the condition (B) is equivalent to the
following requirement (Dempster, Evstigneev, and Schenk-Hoppe, 2003, pp. 271):
With positive probability, the ratios pk(st)jpk(st-1) are not constant with respect
to k. This is condition (A).
The main result on the performance of an investor employing any fixed-mix
strategy is as follows, Dempster, Evstigneev, and Schenk-Hoppe (2003, Theorem 1).
Theorem 2. Let ht(st), t ;:::: 0, be a fixed-mix strategy associated with the matrix
A = (Akj) satisfying (17) . For each k E {1,2 , . . . ,K}, the limit
1
lim -lnh~
t ..... oo t
(22)
exists and is strictly positive almost surely. Furthermore, this limit does not depend
on k, and
.
1
k
.
1
hm -In ht = hm -lnptht > 0 (a.s.)
t ..... oo t
t ..... oo t
(23)
The result ensures that the wealth of a fixed-mix investor tends to infinity at
an exponential rate. All portfolio positions and the investor's wealth grow at the
same positive exponential rate. This finding generalizes the results in Section 2 to
the general case of fixed-mix investment strategies.
The proof of Theorem 2 rests on the observation that one can define a balanced
fixed-mix strategy for any given matrix A satisfying (17). Recall that a trading
strategy H is balanced if ht(st) = " (Sl) . . . ,,(st) h(st) (a.s.) for t ;:::: l. For t = 0,
we assume ho(sO) = h(sO). The function ,,(.) > 0 is scalar-valued and h(·) > 0 is a
vector function such that Elln ,,(st) I < 00 and Ih(st) I = l. The norm Ihl of a vector
h = (hk) is defined as Lk lhkl. The assumption lh(st) l = 1, which was not imposed
in (5), will be satisfied automatically in the present case.
--- page 470 ---

Growing Wealth with Fixed-Mix Strategies
441
For balanced strategies, all the proportions between the amounts of different
assets in the portfolio and the random growth rate of the amount of each asset in
the portfolio are stationary stochastic processes. To show existence of a balanced
fixed-mix strategy associated with the matrix A = (Akj), one needs to show there are
appropriate functions /'(.) and hC). Indeed, Theorem 2 in Dempster, Evstigneev,
and Schenk-Hoppe (2003) ensures that for each matrix A satisfying (17), there is a
unique balanced fixed-mix strategy with I h( st) I = l.
The construction can be sketched as follows. Denote by At = A(st) = (Akj(st))
the positive random K x K matrix defined by
t
pj(st)
Akj(S ) = Akj pk(st)
(24)
We have Elln Akj (st) I < 00. With this definition, the fixed-mix strategy H can be
represented as
(25)
Stationarity of (St) implies that functions /'(.) and xC) (satisfying Elln/,(st)1 < 00
and Ix( st) I = 1) generate a balanced A-strategy if and only if
/,(st)x(st) = A(st)X(st-1) (a.s.)
(26)
The existence of a solution to this equation follows from a stochastic version of the
Perron- Frobenius theorem, Theorem A.l in Dempster, Evstigneev, and Schenk-
Hoppe (2003). The problem (26) cannot be solved by applying the conventional
Perron- Frobenius theorem because the vector x(st) on the left-hand side does not
coincide with the vector X(st-1) on the right-hand side as the function x(st) is
obtained by 'time-shifting' x( st-1) .
The independence of the growth rate from the initial portfolio is proved by
couching the one-step forward portfolio between multiples of the portfolio X(Sl),
analogous to the outline in Section 2. All have the same growth rate.
Finally, the strict positivity of the fixed-mix strategies' growth rate is asserted
by proving that Eln /,(st) > O. This can be seen as follows. Denote by h(·),x(·))
the balanced strategy corresponding to the fixed mix strategy A. The relation (26)
implies
K
pj (st)
.
'V(st)xk (st) = ~
Ak· --Xl (st-1)
k E {I
K}
I
~ lpk(st)
, ... ,
1=1
(27)
The Perron- Frobenius theorem yields existence of a vector r = (r1, . . . ,rK) > 0
with
K
rk = LAkjrj k E {I, . . . ,K}
j=l
Put f3kj = r;;lAkjrj. One finds that
t
K
pJ(st) pJ(st-1)xj(st-1)rk
/,(s ) = L
f3kj pj(st-1)
pk(st)xk(st)r
k E {I, ... , K}
(28)
1=1
1
--- page 471 ---

442
M A. H. Dempster, 1. V. Evstigneev and K. R. Schenk-Hoppe
From this representation of l'(st) one can conclude (using Jensen's inequality and
several other arguments, see Dempster, Evstigneev and Schenk-Hoppe, 2003, Section 3) that Elnl'(st) > 0 under assumption (B).
3.4
Price processes with trend
The concept of a stationary market, where asset prices Pt fluctuate as stationary
stochastic processes, is an idealization. The assumption that only the relative proportions pi / p~ are stationary seems more realistic. Following Dempster, Evstigneev,
and Schenk-Hoppe (2003), let us assume that the prices are of the form
Pt = ~tfh
where Pt = p(st) is a process satisfying the assumptions we previously imposed on
Pt , and ~t = ~t(st) > 0 is any sequence of strictly positive random variables. The
factors ~t represent the dynamics of a price index. The normalized prices Pt are free
of this trend.
The above analysis can directly be applied to this more general price process.
The portfolio value Ptht satisfies
111
-lnptht = -ln~t + -lnptht
t
t
t
The growth rate of Ptht is determined by that of ~t and Ptht.
Under assumption (B), the process Ptht grows exponentially fast almost surely.
Consequently, if the price index ~t grows at an exogenous exponential rate r,
then the investor's wealth Ptht will grow almost surely at a rate r' strictly greater
than r.
4
Stock Markets with Stationary Returns
The observation that rebalancing a portfolio by following any constant proportions
or, more generally, any fixed-mix strategy leads to a strictly higher growth rate
of wealth than any buy-and-hold portfolio has been confirmed in markets with
stationary prices. After seeing the results and following the intuition that a reversion
to the mean is a powerful source of capital growth, one might wonder about the
case in which returns (rather than prices) are stationary processes. Indeed, as
explained in Section 1.1, there is no general agreement that the previous results
hold for stationary returns. This is quite sensible because the any notion of cheap
(or expensive) assets based on the argument that reversion to the long run trend
renders an asset cheap after a series of low returns would mean to fall victim to
the gambler's fallacy. This lack of a simple intuition for the wealth dynamics of
constant proportions strategies in markets where returns (not prices) are stationary
demands a thorough analysis of this case. How can one rest without having gained
an understanding of this problem? The presentation follows Dempster, Evstigneev,
--- page 472 ---

Growing Wealth with Fixed-Mix Strategies
443
and Schenk-Hoppe (2007), which also contains a proof of the main result under
small (proportional) transaction costs.
4.1
The model
Denote the (gross) return on asset k between time t - 1 and t by
k
Rk.- ~ k
2
K
t·-
k
= 1, , . . . , ,t2:1
Pt-l
(29)
Let Rt := (R}, ... ,Rn. We impose the assumption:
(R) The vector stochastic process Rt , t = 1, 2, . . . , is stationary and ergodic.
The expected values El ln R~ I, k = 1, 2, . . . , K , are finite.
The typical example of a stationary ergodic process is a sequence of iid (independent identically distributed) random variables. To avoid misunderstandings, we
emphasize that Brownian motion and a random walk are not stationary.
The asset price at time t and the initial price are related as P~ = p~Rt .... .
R~, where the random sequence R~ is stationary by (R ). This assumption on the
structure of the price process is a fundamental hypothesis in finance. Moreover, it is
quite often assumed that the random variables R~, t = 1, 2, ... are independent, i.e.,
the price process p~ forms a geometric random walk. This postulate, which is much
stronger than the hypothesis of stationarity of R~ , lies at the heart of the classical
theory of asset pricing (Black, Scholes, Merton), see e.g. Luenberger (1998).
Birkhoff's ergodic theorem implies
lIt
lim -lnp~= lim - "'lnR~ = ElnR~ (a.s.)
t-->oo t
t-->oo t ~
n=l
(30)
for each k = 1, 2, . . . , K. This means that the price of each asset k has almost
surely a well-defined and finite (asymptotic, exponential) growth rate, which turns
out to be equal a.s. to the expectation Pk := E In R~, the drift of this asset's price.
The drift can be positive, zero or negative. It does not depend on t in view of the
stationarity of Rt .
Consider an investor following a constant proportions strategy with proportions
(10). Fix any vector ,\ E ~. Given an initial portfolio ho > 0, the (self-financing)
trading strategy H is defined recursively by
h~ = '\kPt ht-dp~ k = 1, 2, ... , K , t 2: 1
(31)
This definition is equivalent to (11). Our aim is to study the asymptotic behavior
of the portfolio value Vi = Ptht as t --> 00, i.e. the limit limt-->oo rlln(Vi) describing
the (exponential) growth rate of the strategy.
--- page 473 ---

444
M A. H. Dempster, 1. V. Evstigneev and K. R. Schenk-Hoppe
4.2
The growth rate
We impose the following non-degeneracy condition:
(C) With strictly positive probability,
pk(st)
pk (st-l)
pf(st) ip~~ (st-l) for some 1 :s; k, m :s; K and t ~ 1
This condition is a very mild assumption on the existence of volatility of the
price process. Condition (C) does not hold if and only if the relative prices of the
assets are constant in time (a.s.), i.e. , if with probability one, the ratio p~ /pr;:' of
the prices of any two assets k and m does not depend on t. This condition is also
equivalent to (B), see Dempster, Evstigneev, and Schenk-Hoppe (2003, pp. 271).
The condition (C) on asset prices has an equivalent formulation for asset returns:
(D) For some t ~ 1 (and hence, by virtue of stationarity, for each t ~ 1), the
probability
P{R~ i- Rr;:' for some 1 :S; k,m:S; K}
is strictly positive.
Equivalence can bee seen as follows. Note that p~ /pr;:' iptl/Pr'-l if and only
if p~ /ptl ipr;:' /Pr'-l' i.e. R~ i- Rr;:'. Denote by 6t the random variable that is
equal to 1 if the event {R~ i- Rr;:' for some 1 :s; k, m :s; K} occurs and 0 otherwise.
Condition (C) means that P{maXt;:'l 6t = I} > 0, while (D) states that, for some
t (and hence for each t), P{ 6t = I} > O. The latter property is equivalent to the
former because {maXt;:'l 6t = I} = U~l {6t = I}.
We can now state the main result on the growth of wealth of investors following
constant proportions strategies.
Theorem 3. Fix any A E 6..
(i) The growth rate of the constant proportions strategy is almost surely equal to
a constant which is strictly greater than Lk AkPk, where Pk is the drift of the price
of asset k.
(ii) Suppose all the assets have the same drift (therefore, almost surely the same
asymptotic growth rate), i.e., ElnR~ = P fo r each k = 1, ... ,K with some real
number p. Then the growth rate of the constant proportions strategy is almost surely
strictly greater than the growth rate of each individual asset.
In Theorem 3, assertion (ii) immediately follows from (i). The result (ii) shows
that any completely mixed constant proportions strategy grows at a rate strictly
greater than p, the growth rate of each particular asset. The growth of the investor's
wealth is only driven by the volatility of the price process. This result seems to
contradict conventional finance theory which usually regards the volatility of asset
prices as an impediment to financial growth. In the present context, volatility serves
as an endogenous source of its acceleration. Theorem 3 (ii) asserts the validity of
--- page 474 ---

Growing Wealth with Fixed-Mix Strategies
445
the conclusion drawn in the illustrative example discussed in Section 1.2. Indeed,
the constant proportions strategy (.5, .5) (as well as any other completely mixed
constant proportions strategy) yields a higher growth rate than the price of each
asset.
The first part of Theorem 3 places a floor under the constant proportions strategy's growth rate. When asset prices grow at different rates, there is no general
result that constant proportions strategy grow faster than any (completely diversified) buy-and-hold strategy. The latter grows at rate maxk Pk which is not strictly
dominated by L k AkPk · The growth-optimal constant proportions strategy however
will always grow at least as fast as any buy-and-hold in the model.
The proof of the above result is surprisingly simple and can be presented with
success to an audience with knowledge of only elementary probability and calculus:
Fix any vector A E .6... The random wealth dynamics of the corresponding constant
proportions strategy (31) are given by
KKk
K
k
Vi = Ptht = LP~htl = L
~t pt1ht l = L
~t AkPt-lht-l
k=l
k=l Pt-l
k=l Ptl
= [t,R~AklVil = (Rt A)Vi-l
(32)
for each t ::::: 1. This implies
(33)
for all t ::::: 1. The ergodic theorem ensures
l I
t
lim -In Vi = lim - '" In(Rn A) = E In(Rt A) (a.s.)
t-->oo t
t--> oo t ~
n=l
(34)
It remains to show that E ln(Rt A) > Lf:=l AkPk under the condition (D). Indeed, Jensen's inequality and (D ) ensure the relation
K
K
InLR~ A k > LA k(lnR~)
k=l
k=l
with strictly positive probability, while the non-strict inequality holds always.
Consequently,
K
K
E In(Rt A) > L AkE(ln R~) = L AkPk
(35)
k=l
k=l
This proves Theorem 3.
--- page 475 ---

446
M A. H. Dempster, 1. V. Evstigneev and K. R. Schenk-Hoppe
4.3
Interpretation
The rigorous proof of the presence of volatility-induced growth in markets where
asset returns are stationary leaves open the question on the intuition behind this
result.
It seems any explanation one can give is nothing but a repetition of the mathematical reasoning behind this result: If Ri, ... ,Rf are the random returns of the
K assets, then the asymptotic growth rates of these assets are E In R~, while the
asymptotic growth rate of a constant proportions strategy is Eln(Lk AkR~), which
is strictly greater than Lk AkEln(R~) by Jensen's inequality because the logarithmic function is strictly concave. The proof in Section 2 confirms that Jensen's
inequality is the central tool used in the proof. Any explanation not based on this
fact would be flawed.
It is well-known that a linear combination of assets can produce non-linearity
in a portfolio's characteristics. Indeed, this feature drives mean-variance portfolio
choice, cf. Luenberger (1998). In the present model, the rebalancing of the portfolio
so as to maintain constant proportions causes a non-linear effect in the portfolio's
growth rate with the feature that Eln(Lk AkR~) - Lk AkEln(R~) > 0 for any
A = (AI, ... , AK) E ~ provided assumption (C) holds.
Other attempts to appeal to intuition are discusses (and rejected) in the next
section.
An interesting problem is the question under which (general) assumptions
Eln(Lk AkR~) > 0 even if maxk Pk :::; 0 (or, less restrictive, mink Pk :::; 0). The
example in Section 1.2 possesses this property. In that example, PI = P2 < 0, but
E In(AIRi + A2R;) > 0 for the constant proportions strategy A = (.5, .5). But if A is
close to (1,0) or (0,1) the growth rate of wealth becomes negative as well. A partial
answer to this 'black swan' question is provided in Section 5. We discuss a case in
which the addition of a slower growing asset always enhances the growth of a constant proportions strategy and raises the growth rate over that of any buy-and-hold
strategy.
5
Myths and Misconceptions
The phenomenon of volatility-induced growth is simply counter-intuitive as confirmed by our test in Section 1.1. Providing a common-sense explanation for the
mathematical results can therefore not be a simple task. In this section, we discuss
some of the more prominent suggestions for intuition put forward in the literature.
5.1
Volatility pumping
The term 'volatility pumping' appears to have been first used by Luenberger (1998).
His suggestion is that constant proportions strategies force the investor to 'buy low
--- page 476 ---

Growing Wealth with Fixed-Mix Strategies
447
and sell high'-the common sense dictum of stock market trading. Those assets
whose prices have risen from the last rebalance date will be overweighted in the
portfolio, and their holdings must be reduced to meet the required proportions and
to be replaced in part by assets whose prices have fallen and whose holdings must
therefore be increased. This behavior leads to growth if asset returns exhibit some
stationarity properties.
In Section 2.3, we argued that this explanation is correct for stationary prices.
In the present case, accepting this explanation would mean to fall victim to the
gambler's fallacy. This explanation is not valid because when the price follows a
geometric random walk, the set of its values is generally unbounded and for every
value there is a smaller as well as a larger value. Suppose returns are iid, then 'high'
and 'low' do not have any meaning. Reversion to the long run trend (as postulated
by the ergodic theorem) is not an explanation either: arguing that the longer the
run of black numbers, the higher the odds of red numbers at the next spin of the
roulette wheel is the gambler's fallacy. When returns are determined by the flip of
a coin, an asset's upside and downside potential does not change over time. Such
an asset is not cheap or expensive at any point in time.
5.2
The importance of constancy
A more substantial lacuna in the above reasoning is that it does not reflect the
assumption of constancy of investment proportions. This leads to the question:
what will happen if the portfolio is rebalanced so as to sell all those assets that gain
value and buy only those ones which lose it? (This should lead to an even higher
growth rate -
provided volatility could be 'pumped'.)
Assume, for example, that there are two assets, the price PE of the first (riskless)
is always 1, and the price P; of the second (risky) follows a geometric random walk,
so that the gross return on it can be either 2 or 1/ 2 with equal probabilities. Suppose
the investor sells the second asset and invests all wealth in the first if the price PZ
goes up and performs the converse operation, betting all wealth on the risky asset,
if P; goes down. Then the sequence At = (Al,t, A2,t) of the vectors of investment
proportions will be iid with values (0, 1) and (1 ,0) taken on with equal probabilities.
Furthermore, Atl will be independent of Rt . By virtue of (34), the growth rate
of the portfolio value for this strategy is equal to Eln(RtAt-d = [In(O· 1 + 1 . 2)+
In(O· 1 + 1 . ~) + In(l . 1 + O· 2)+ In(l . 1 + O· ~)l/ 4 = 0, which is the same as the
growth rate of each of the two assets k = 1, 2. But this growth rate is strictly lower
than that of any completely mixed constant proportions strategy.
5.3
Energy-interpretation of volatility
Our results highlight the importance of volatility because fixed-mix strategies do
not produce growth beyond buy-and-hold portfolios in any of the above models
when prices or returns are constant. It is tempting to see volatility as a source of
energy that can be tapped to generate growth.
