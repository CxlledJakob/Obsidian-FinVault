# The Kelly capital growth investment criterion _ theory and -- Leonard C_ Maclean, Edward O_ Thorp, W_ T_ Ziemba, Leonard -- World Scientific Handbook -- isbn13 9781283148344 -- bec576e26410d0c695fd5b867d08ec4f -- An.pdf — pages 438–457

--- page 438 ---

28
A Benchmark Approach to Investing and Pricing
Eckhard Platen
University of Technology Sydney,
School of Finance €3 Economics and Department of Mathematical Sciences,
PO Box 123, Broadway, NSW, 2007, Australia
Abstract
This paper introduces a general market modeling framework, the benchmark
approach, which assumes the existence of the numeraire portfolio. This is the
strictly positive portfolio that when used as benchmark makes all benchmarked
non-negative portfolios supermartingales, that is intuitively speaking downward
trending or trendless. It can be shown to equal the Kelly portfolio, which maximizes expected logarithmic utility. In several ways, the Kelly or numernire portfolio is the "best" performing portfolio and cannot be outperformed systematically
by any other non-negative portfolio. Its use in pricing as numeraire leads directly to the real world pricing formula, which employs the real world probability
when calculating conditional expectations. In a large regular financial market ,
the Kelly portfolio is shown to be approximated by well-diversified portfolios.
JEL Classification: G 10, G 13
1991 Mathematics Subject Classification: primary 90A12; secondary 60G30,
62P20.
Keywords and phrases: Kelly portfolio, real world pricing, numeraire portfolio,
strong arbitrage, diversification.
1
Introduction
409
The classical asset pricing theories, as developed in Debreu (1959), Sharpe (1964),
Lintner (1965), Merton (1973a,b), Ross (1976), Harrison and Kreps (1979), Constantinides (1992), and Cochrane (2001) represent forms of relative pricing, since
the existence of an equivalent risk neutral probability measure is typically requested.
However, relative pricing ignores in the long run the presence of the equity premium.
This paper presents an extension of classical risk neutral pricing in a general modeling framework, the benchmark approach, where a form of absolute pricing naturally
emerges, see Platen (2002) Platen (2002, 2006) and Platen and Heath (2006). The
benchmark represents here the "best" performing, strictly positive, tradable portfolio, which turns out to be the K elly portfolio, see Kelly (1956). Most results we
--- page 439 ---

410
E. Platen
present can be stated in a model independent manner. The benchmark approach
only requires the existence of the benchmark, playing the role of the numeraire
portfolio, originally discovered in Long (1990). The benchmark approach with the
Kelly portfolio as benchmark is directly applicable in portfolio optimization and
covers a wider modeling world than classical theories allow.
We will see that non-negative portfolios, when denominated in units of the
benchmark are supermartingales. This supermartingale property has been already
observed for particular settings, for instance, in Long (1990) , Bajeux-Besnainou
and Portait (1997), Becherer (2001) , Platen (2002), Biihlmann and Platen (2003),
Platen and Heath (2006), Karatzas and Kardaras (2007), and Kardaras and Platen
(2008b). For the purpose of pricing, the inverse of the benchmark plays the role
of the stochastic discount factor in the language of Cochrane (2001). Within this
paper, there will be no major additional assumption made beyond the request on the
existence of a numeraire portfolio. A series of fundamental results follows from this
assumption by a few basic arguments. Some of these describe "best" performance
properties of the Kelly portfolio which underline its fundamental importance in
investing.
In Platen and Heath (2006), the benchmark approach has been described for
jump-diffusion markets. Probably the most striking feature of the rich benchmark
framework is the possible co-existence of several self-financing portfolios that may
perfectly replicate one and the same payoff. The presence of different replicating
portfolios is not consistent with the classical Law of One Price. The proposed
Law of the Minimal Price identifies for a given contingent claim the corresponding
minimal replicating portfolio process, which characterizes also in an incomplete
market the economically correct price process. The Law of the Minimal Price
yields directly the real world pricing formula, where the expectation is taken with
respect to the real world probability measure and the Kelly portfolio appears as the
numeraire. No change of probability measure is performed under real world pricing,
which extends the classical risk neutral approach. Consequently, the request on the
existence of an equivalent risk neutral probability measure is here avoided and a
much wider modeling world is available. The real world pricing formula generalizes
the risk neutral pricing formula as well as the actuarial pricing formula. These
formulae represent the central pricing rules in their respective streams of literature
and nothing else is here requested than the existence of the Kelly portfolio. The
fact that the Law of One Price does not hold does not create strong arbitrage
opportunities in the sense of this paper. We will see that there is no economic
reason to exclude any weaker form of arbitrage as under the classical no-arbitrage
approach.
A Diversification Theorem will be derived along the lines of Platen (2005). It
states that any diversified portfolio in a regular financial market approximates the
Kelly portfolio. This makes the benchmark approach rather practical and allows
one to interpret a well-diversified portfolio as proxy for the Kelly portfolio. For
--- page 440 ---

A Benchmark Approach to Investing and Pricing
411
further results on the benchmark approach the reader is referred to Platen and
Heath (2006).
The remainder of the paper is organized as follows: It introduces the numeraire
portfolio in Section 2. Section 3 derives various manifestations of "best" performance for the Kelly portfolio. The Law of the Minimal Price is proposed in Section 4. In Section 5 we discuss the concept of real world pricing. Section 6 introduces
a strong form of arbitrage. Finally, Section 7 provides a version of the Diversification
Theorem.
2
Benchmark Approach
Along the lines of Platen (2002) (Platen, 2002, 2006) and Platen and Heath (2006),
we consider a general financial market in continuous time with d risky, non-negative,
primary securities, d E {I, 2, . . . }. These securities could be, for instance, shares,
currencies or other traded securities. Denote by st the value of the corresponding
/h primary security account, j E {O, 1, ... , d}, at time t ~ O. This non-negative
account holds units of the jth primary security together with all dividends or interest
payments reinvested. The Oth primary security account S~ denotes the value of the
locally riskless savings account at time t ~ o. The dynamics of the primary security
accounts need not be specified when formulating the main statements.
The market participants can form self-financing portfolios with primary security
accounts as constituents. A portfolio value sf at time t is described by the number
of of units held in the jth primary security account Sf for all j E {O, 1, ... , d} ,
t ~ o. For simplicity, assume that the units of the primary security accounts are
perfectly divisible, and that for all t E [0,(0) the values o~, of, ... , Of, for any given
strategy 0= {Ot = (o~,of, ... ,of)T, t ~ O}, depend only on information available
at time t. The portfolio value at this time is given by the sum
d
sf = Lot st
j=O
We consider only self-financing portfolios where changes in their value are only due
to changes in the values of the primary security accounts. We neglect any market
frictions or liquidity effects.
By V: denote the set of all strictly positive, finite, self-financing portfolios with
initial capital x > O. The benchmark approach employs a very special strictly
positive portfolio as benchmark, which we denote by S 8* E V:. Later it will
become apparent that it is the Kelly portfolio, see Kelly (1956), which is in several
ways the "best" performing strictly positive tradable portfolio. On the other hand,
it will turn out that it is also the natural numeraire , see Long (1990), for pricing
any type of claim when employing the real world probability for calculating the
respective conditional expectation in the resulting pricing formula.
--- page 441 ---

412
E. Platen
Let Et(X) denote the conditional expectation under the real world probability
measure P given the information available at time t ;:::: O.
Definition 2.1.
For given x> 0, a strictly positive, finite, self-financing portfolio
SfH E V: is called a numemire portfolio if all non-negative portfolios S6, when
denominated in units of S6*, are supermartingales.
The notion of a numemire portfolio was originally introduced by Long (1990) in
a rather special setting. Later it was generalized in Bajeux-Besnainou and Portait
(1997) and Becherer (2001). These authors worked under classical no-arbitrage
assumptions that are consistent with the existence of an equivalent risk neutral
probability measure, see Delbaen and Schachermayer (199S). More recently, Platen
(2002), Biihlmann and Platen (2003), Platen and Heath (2006), and Platen (2006)
emphasized that in a more general setting one still obtains a viable financial market
model, as long as a numemire portfolio exists. Also Fernholz and Karatzas (2005),
Karatzas and Kardaras (2007) , and Kardaras and Platen (200Sb) consider financial
market models beyond the classical no-arbitrage framework.
To provide a basis, let us formulate the only major assumption of the paper:
Assumption 2.2.
For given x > 0, there exists a numemire portfolio S6* E V:.
This assumption is satisfied for a wide range of financial market models used in
practice. For instance, in Platen and Heath (2006) it has been verified for jumpdiffusion markets. Karatzas and Kardaras (2007) and Kardaras and Platen (200Sb)
confirm the validity of Assumption 2.2 for a wide range of semi-martingale markets.
Now, under the benchmark approach we choose the numemire portfolio as
benchmark. The benchmarked value Sf of a portfolio S6 is given by the ratio
' 6
Sf
S - -
t -
S6*
t
for all t;:::: O.
Definition 2.1 leads by Assumption 2.2 directly to the following
conclusion:
Corollary 2.3.
The benchmarked value Sf of any non-negative portfolio S6 satisfies the supermartingale property
S6 > E (S6)
t -
t
s
(2.1)
for all 0 ::; t ::; s < 00 .
Consequently, the currently observed benchmarked value of a non-negative portfolio is always greater than or equal to its expected future benchmarked value. This
means intuitively, if there were any trend in a benchmarked non-negative portfolio,
then this trend could only point downward.
The supermartingale property (2.1) is the fundamental property of a financial
market. For instance, it yields easily the uniqueness of the benchmark by the
--- page 442 ---

A Benchmark Approach to Investing and Pricing
413
following argument: Consider two strictly positive portfolios that are supposed
to be numeraire portfolios. According to Corollary 2.3, the first portfolio, when
expressed in units of the second one, must satisfy the supermartingale property
(2.1). By the same argument, the second portfolio, when expressed in units of the
first one, must also satisfy the supermartingale property. Consequently, by Jensen's
inequality the portfolios have to be identical, and the value process S5* E Vi of a
numeraire portfolio is unique. Note that the stated uniqueness does not imply that
the number of units invested has to be unique, which is due to potential redundancies
in primary security accounts.
3
Best Performance of the Benchmark
In this section we list several manifestations of the fact that our benchmark S5*
is the "best" performing, strictly positive, tradable portfolio and equals the Kelly
portfolio:
3.1
Numeraire portfolio
First, the definition of the numeraire portfolio S5* itself, given by Definition 2.1,
expresses the fact that this portfolio performs "best" in the sense that the expected
returns of benchmarked non-negative portfolios never become strictly positive.
3.2
Kelly portfolio
As a second manifestation of "best" performance, we derive the growth optimality
of the benchmark, which identifies it very generally as the Kelly portfolio, a fact
that has been documented for special models in the literature, for instance, in Long
(1990). The expected growth gf,h of a strictly positive portfolio S5 over the time
period (t, t + h] for t, h > °
is given by the conditional expectation
gf,h = E t (In (A~, h))
of the logarithm of the portfolio ratio
A5
_ Sf+h
t,h -
S5
t
To identify the strictly positive portfolio that maximizes the expected growth, let us
perturb at time t :;:. 0, the investment in a given strictly positive portfolio S~ E Vi,
x > 0, by some small fraction E E (o,~) of some non-negative portfolio S5. For
analyzing the changes in the expected growth of the perturbed portfolio S5 g define
the derivative of expected growth in the direction of S5 as the right hand limit
8g~,\ I
1·
1 ( 5g
~)
--
-
lm-
9
-g
8E
0'=0 -
0'-->0 E
t,h
t ,h
(3.1)
--- page 443 ---

414
E. Platen
for t, h ~ O. Obviously, if the portfolio that maximizes expected growth coincides
in (3.1) with the portfolio SQ., then the resulting derivative of expected growth will
never be greater than zero for all non-negative portfolios Sli. This leads to the
following definition of growth optimality:
Definition 3.1.
A strictly positive portfolio S Q. is called growth optimal if the
corresponding derivative of expected growth is less than or equal to zero for all
non-negative portfolios SIi , that is,
gt ,h
< 0
o lie I
oc
E=O -
for all t, h ~ O.
Note that this definition is different to the classical characterization of the Kelly
portfolio or growth optimal portfolio. In the literature, it is typically based on the
maximization of expected logarithmic utility from terminal wealth, as used in Kelly
(1956) and later also employed in a stream of literature, including Latane (1959) ,
Breiman (1960) , Hakansson (1971) , Merton (1973a), Roll (1973) and Markowitz
(1976), among many others. It is clear from Definition 3.1 and the standard logutility definition of the Kelly portfolio, see for instance Kelly (1956) and Thorp
(1972), that the above growth optimal portfolio equals the Kelly portfolio. The
following result provides a convenient method for the identification of the benchmark
or numeraire portfolio in a given investment universe by searching for its Kelly
portfolio.
Theorem 3.2.
The numeraire portfolio is growth optimal.
Proof: For c E (0, ~) , two consecutive times t and t + h with h > 0, and a nonnegative portfolio SIi , with Sf > 0, consider the perturbed portfolio Slie under the
choice sf = Sr in (3.1), yielding a portfolio ratio A~~h = c A~, h - (1 - c) A~,h >
O. One then obtains by the well-known inequality In(x)
<:::; x -I for x ~ 0,
the relations
and
Ali
AIi*
t ,h -
t ,h
Alie
t ,h
Since A~eh > 0 one obtains from (3.3) for A~ h -
A~*h ~ 0 the inequality
,
,
,
clie > 0
t ,h -
(3.2)
(3.3)
(3.4)
--- page 444 ---

A Benchmark Approach to Investing and Pricing
and for Ai,h - Ath < 0, because of c E (0, ~) and Ai,h ::::: 0, the relation
A,h
1
1
COg > - ~
= -
> - -- > -2
t h -
AO
A O
-
1
-
,
t gh
1 - c + c ~
- c
,
A1,*h
Summarizing (3.2)- (3.5) yields the upper and lower bounds
AO
-2 < COg < ~-1
-
t ,h -
AO*
t,h
where by Definition 2.1 one has
415
(3.5)
(3.6)
(3.7)
By using (3.6) and (3.7) it follows by the Dominated Convergence Theorem, see
Shiryaev (1984), that
This proves by Definitions 2.1 and 3.1 that the numeraire portfolio SO* is growth
optimal.
D
3.3
Long term growth
To formulate a third manifestation of "best" performance for the benchmark, define
the long term growth rate gO of a strictly positive portfolio So E Vi as the upper
limit
l = lim sup ~ In (S~)
t--->oo
t
So
(3.8)
The long term growth rate (3.8) is defined pathwise almost surely and does not
involve any expectation. By exploiting the supermartingale property (2.1), the
following fascinating property of the Kelly portfolio will be shown very generally
below.
Theorem 3.3.
The numeraire portfolio SO* E Vi achieves the maximum long
term growth rate. This means, when compared with any other strictly positive portfolio SO E Vi, one has
(3.9)
--- page 445 ---

416
E. Platen
Proof: Similar as in Karatzas and Shreve (1998) consider a strictly positive portfolio S6 E Vi, x > 0, with the same initial capital as the numeraire portfolio,
that is, S8 = S8* = x > 0. By Corollary 2.3, we can use the following maximal
inequality, derived in Doob (1953) , where for any k E {I, 2, ... } and E E (0, 1) one
has
exp{Ek}P ( sup sf> eXP{Ek}) S; Eo (SZ) S; sg = 1
k$t<oo
One finds for fixed E E (0,1) that
~
P C~~Joo In (Sf) > E k) S; ~
exp{ -E k} < 00
By the Borel-Cantelli lemma, see Shiryaev (1984), there exists a random variable
kc such that for all k 2> kc and t 2> k it holds that
In (Sf) S; E k S; E t
Therefore, it follows for all k > kc the estimate
sup ~ In (Sf) S; E
t?k t
which implies that
1
(S6)
1
(S6*)
lim sup - In -%
S; lim sup - In -i; + E
t--->oo
t
So
t--->oo
t
So
(3.10)
Since the inequality (3.10) holds for all E E (0, 1) one obtains with (3.8) the relation
(3.9).
0
According to Theorem 3.3, the trajectory of the Kelly portfolio outperforms in
the long run those of all other strictly positive portfolios that start with the same
initial capital. This property is independent of any model choice and, therefore,
very robust. An investor, who is aiming in the long run for the highest possible
wealth, has to invest her or his total tradable wealth into the Kelly portfolio.
3.4
Systematic outperformance
Over short and medium time horizons, almost any strictly positive portfolio can generate larger returns than those exhibited by the Kelly portfolio. However, the fourth
manifestation of "best" performance will show that such short term out performance
cannot be achieved systematically. To formulate a corresponding statement properly, we will employ the following definition:
Definition 3.4.
A non-negative portfolio S6 systematically outperforms a strictly
positive portfolio S8 if
(i) both portfolios start with the same initial capital Sfa = sfa;
--- page 446 ---

A Benchmark Approach to Investing and Pricing
417
(ii) at a later time t the portfolio value sg is at least equal to sf, that is P(sg 2::
Sf) = 1, and
(iii) the probability for sg being strictly greater than sf is strictly positive so that
p (sg > Sf) > O.
Systematic outperformance of one portfolio by another one is possible under the
benchmark approach, see Platen and Heath (2006). The above notion of systematic
out performance was introduced in Platen (2004) and was motivated by the supermartingale property (2.1). It relates in some sense to the notion ofrelative arbitrage,
later studied in Fernholz and Karatzas (2005), and also to the notion of a maximal element earlier employed in Delbaen and Schachermayer (1998). The following
result presents a fourth manifestation of "best" performance of the benchmark:
Theorem 3.5.
The numemire portfolio cannot be systematically outperformed
by any non-negative portfolio.
Proof:
Consider a non-negative portfolio So with benchmarked value sg = 1 at a
given time t 2:: 0, where s~ 2:: 1 almost surely at some later time s E [t, (0). Then
it follows by the supermartingale property given in Corollary 2.3 that
Since one has s~ 2:: 1 almost surely and Et(S~) :s; 1, it can only follow that S~ = l.
This means that one has at time s the equality S~ = S~* almost surely. Therefore,
according to Definition 3.4 the portfolio So does not systematically outperform the
numemire portfolio.
D
As a consequence of Theorem 3.5, one can conclude that in the given very
general modeling setting, no active fund manager can systematically outperform
the benchmark. On the other hand, if the market portfolio is not the numemire
portfolio, which is most likely the case, and a fund approximates well the Kelly
portfolio, then this fund will not be outperformed systematically by the market
portfolio or any other significantly different portfolio. In the long run its path will
by property (3.8) beat the path of the market portfolio almost surely.
There are further manifestations of "best" performance of the Kelly portfolio.
For instance, in Kardaras and Platen (2008a), it is shown that the Kelly portfolio
minimizes some expected market time to reach a given wealth level. Results in this
direction can be found, for instance, in Browne (1998).
4
The Law of the Minimal Price
The fundamental supermartingale property (2.1) ensures that the maximum expected return of a benchmarked non-negative portfolio can at most equal zero. In
--- page 447 ---

418
E. Platen
the case when it equals zero for a given benchmarked price process for all time instances, then the current benchmarked value of the price is always the best forecast
of its future benchmarked values. In this case, one has equality in relation (2.1)
and we call such a price process fair. A benchmarked fair price process forms a
martingale. In general, not all primary security accounts and portfolios need to be
fair under the benchmark approach. This is the key property that differentiates this
approach from the classical approaches. For instance, there may exist benchmarked
portfolios that form local martingales but are not true martingales, as is extensively discussed in Platen and Heath (2006). Furthermore, note that non-negative
fair price processes are somehow minimal, as we shall see below.
It may be puzzling to some readers that discounting with another discount factor than the savings account ought to lead to "fair" prices or could be particularly
meaningful. Below we will give a valid reason why the Kelly portfolio is the "universal currency" that should be used for discounting when pricing under the real
world probability. It stems from the fact that the Kelly portfolio represents the
best performing portfolio and, thus, the natural numeraire for valuation when the
real world probability measure for calculating expectations.
The following Law of the Minimal Price substitutes the widely postulated classical Law of One Price, which no longer holds in our general setting:
Theorem 4.1.
Law of the Minimal Price.
If a fair portfolio process replicates
a given non-negative payoff at a given maturity date, then this portfolio represents
the minimal replicating portfolio among all non-negative portfolios that replicate this
payoff·
Proof:
A stochastic process [:;8, which satisfies relation (2.1) is a supermartingale,
see Shiryaev (1984). When equality holds in (2.1) then the process is fair and its
benchmarked value process is a martingale. Within a family of non-negative supermartingales with the same value at a given future payoff date, it is the martingale
among these supermartingales which attains almost surely the minimal possible
value at all times before the maturity date. This fundamental fact about the optimality of martingales in a family of supermartingales proves directly Theorem 4.l.
D
The existence of unfair price processes under the benchmark approach creates
new realistic effects that can be modeled and are not captured by any classical
no-arbitrage framework. For a given replicable payoff, it follows by Theorem 4.1
that the corresponding fair replicating portfolio describes the least expensive hedge
portfolio. This is also the economically correct price process in a competitive market. We emphasize that the Law of the Minimal Price generates a unique price
system for contracts and derivatives under the benchmark approach which only relies on the existence of a numeraire portfolio. As shown in Platen (2009), pricing
purely based on hedging or classical no-arbitrage arguments, as employed under the
--- page 448 ---

A Benchmark Approach to investing and Pricing
419
classical Arbitrage Pricing Theory, see Ross (1976), can lead in our general setting
to significantly more expensive prices than provided by fair price processes.
5
Real World Pricing
Define a contingent claim HT as a non-negative payoff delivered at maturity
T E (0,00), which is expressed in units of the domestic currency and has finite
expectation
Eo (:;) < 00.
(5.1)
By the Law of the Minimal Price one can identify the corresponding fair price
process via the following real world pricing formula:
Corollary 5.1.
If for a contingent claim HT, T E (0,00), there exists a fair
portfolio S8}; that replicates this claim at maturity T such that HT = Sg.II , then
its minimal replicating price at time t E [0, T] is given by the real world pricing
formula
S8 H = S8* E (HT)
t
t
t
S8*
T
(5.2)
Relation (5.2) is called the real world pricing formula because it involves the
conditional expectation E t with respect to the real world probability measure. This
formula can be interpreted in the sense of Cochrane (2001) as a pricing formula
that uses the stochastic discount factor (S[*)-1. Also the closely related use of the
corresponding state price density, pricing kernel and deflator are consistent with
the real world pricing formula (5.2) under appropriate assumptions. However, all
the classical pricing approaches exclude classical arbitrage, which is equivalent to
the existence of an equivalent risk neutral probability measure, see Delbaen and
Schachermayer (1998). In this manner, they postulate the Law of One Price, see
for instance Ingersoll (1987), Long (1990), Constantinides (1992), Duffie (2001), and
Cochrane (2001) for classical no-arbitrage settings. The benchmark approach with
its real world pricing concept does not require a risk neutral probability measure
to exist or equivalent classical no-arbitrage constraints and goes beyond the Law
of One Price. The real world pricing formula (5.2) only requires the existence of
the numemire portfolio and the finiteness of the expectation in (5.1). No measure
transformation needs to be applied.
An important special case of the real world pricing formula (5.2) arises when
HT is independent of S~*. In this case one obtains the actuarial pricing formula
(5.3)
with the fair zero coupon bond price
(5.4)
--- page 449 ---

420
E. Platen
that pays one monetary unit at maturity T. The fair zero coupon bond price
P(t, T) provides the discount factor in (5.3) in a way as it has been used intuitively
by actuaries for obtaining the, so called, net present value of HT. The real world
pricing formula provides a rigorous and general derivation of the actuarial pricing
formula that has been in use for centuries.
Let us now derive risk neutral pricing as a special case of real world pricing. For
this purpose we rewrite for t = 0 the real world pricing formula (5.2) in the form
sgll = Eo (AT ~~ HT)
(5.5)
" 0
while employing the benchmarked normalized savings account AT = ~~"
By the
o
supermartingale property (2.1) ofthe normalized benchmarked savings account process A = {At = fa, t 2:> O} we have 1 = Ao 2:> Eo(AT), Together with equation (5.5)
o
this yields the inequality
Eo (AT ¥ HT)
SIiH <
T
o -
Eo(AT)
(5.6)
If the benchmarked savings account is not a martingale, then equality does not
hold in relation (5.6). To ensure equality in (5.6), one needs to impose the strong
assumption that the savings account is fair, that is, intuitively its benchmarked
value has no trend and is a martingale. In this particular case, the expression on
the right hand side of (5.6) can be interpreted by Bayes' formula as the conditional
expectation of the discounted contingent claim under the, in this case existing,
equivalent risk neutral probability measure Q with Radon-Nikodym derivative AT =
~~. Only in this case when A is a martingale the relation (5.6) yields, in general,
for a contingent claim HT the classical risk neutral pricing formula
Sli II -
EO (S8 H )
0
-
0
SO
T
T
see, for instance, Harrison and Kreps (1979) or Karatzas and Shreve (1998). Here
E~ denotes the conditional expectation at time t = 0 under the equivalent risk
neutral probability measure Q. By inequality (5.6) it follows that the fair derivative
price is never more expensive than the price obtained under some formal application
of the standard risk neutral pricing rule.
Finally, it shall be noted for not perfectly hedgable contingent claims that utility
indifference pricing, in the sense of Davis (1997), leads in the case of incomplete
jump-diffusion markets again to the real world pricing formula (5.2), see Platen and
Heath (2006). Under real world pricing, the hedgable part of the claim is replicated
via the minimal possible hedge portfolio and the benchmarked unhedgable part
remains untouched. In some sense, the real world pricing formula provides the least
squares projection of a given unhedgable benchmarked contingent claim into the set
of current benchmarked prices, The benchmarked hedge error has zero mean and
--- page 450 ---

A Benchmark Approach to Investing and Pricing
421
its variance is minimized. This generalizes also the notion of local-risk minimization
for pricing in incomplete markets, as advocated in Follmer and Schweizer (1991),
Hofmann et al. (1992), and Schweizer (1995). In practice, when benchmarked hedge
errors can be diversified in the large book of a well diversified bank or insurance
company, then the total benchmarked hedge error vanishes by the Law of Large
Numbers asymptotically from the bank's trading book and the market becomes
asymptotically complete from this perspective. This shows that in practice real
world pricing makes perfect sense. Any systematically more expensive pricing would
make an institution less competitive. On the other hand, any lower prices would
make it unsustainable.
6
Strong Arbitrage
Since the benchmark approach goes significantly beyond the classical no-arbitrage
world, it is of importance to clarify the potential existence of arbitrage opportunities. In the literature, there exist many different mathematical definitions of
arbitrage, and one has to ensure that the given modeling framework is economically viable. Obviously, arbitrage opportunities can only be exploited by market
participants. These have to use their portfolios of total tradable wealth when trying
to exploit potential arbitrage opportunities. Due to the established legal concept
of limited liability, only non-negative total tradable wealth processes have to be
considered when studying the exploitation of potential arbitrage. Therefore, any
realistic arbitrage concept has to focus on non-negative, self-financing portfolios.
An obvious, strong form of arbitrage arises when a market participant can generate strictly positive wealth from zero initial capital. This leads to the following
definition of strong arbitrage, which was introduced in Platen (2002) motivated by
the supermartingale property (2.1):
Definition 6.1.
A non-negative portfolio S6 is a strong arbitrage if it starts with
zero initial capital, that is S8 = 0, and generates strictly positive wealth with strictly
positive probability at a later time t E (0,00), that is, P(st > 0) > O.
The exclusion of the above form of arbitrage has been independently argued
for on purely economic grounds by Loewenstein and Willard (2000). Important is
that if only strong arbitrage is excluded, then weaker forms of arbitrage may still
exist. However, this does not harm the economic viability of the market model.
For instance, there may exist, so-called, free snacks and cheap thrills, in the sense
of Loewenstein and Willard (2000), which usually represent situations of systematic outperformance in the sense of Definition 3.4. Also free lunches with vanishing
risk, as excluded in Delbaen and Schachermayer (1998), can exist without creating
complications from an economic point of view. Furthermore, by looking at any of
the weaker forms of arbitrage one realizes that these cannot be exploited in prac-
--- page 451 ---

422
E. Platen
tice without providing adequate collateral, see Platen and Heath (2006) . This request, however, makes the corresponding theoretical notions of weaker forms of arbitrage questionable from their practical relevance. By exploiting the supermartingale
property (2.1) , the following result can be established:
Theorem 6.2.
arbitrage.
There does not exist any non-negative portfolio that is a strong
Proof:
For a non-negative portfolio S6, which starts with zero initial capital, it
follows by the supermartingale property given in Corollary 2.3 that
6
'6
('6)
'6
° = So = x So ::::: x Eo St = x E(St) ::::: °
for t ::::: 0, where E(·) denotes expectation under the real world probability. By the
nonnegativity of sf and the strict positivity of si*, the event sf > ° can only have
zero probability, that is
P (Sf> 0) = °
This leads to the conclusion that sf equals zero for all t ::::: 0, which proves by
Definition 6.1 the Theorem 6.2.
D
Theorem 6.2 states that strong arbitrage is automatically excluded in the given
general benchmark framework. Therefore, different to the classical no-arbitrage approaches, pricing by excluding strong arbitrage does not make any sense. Instead,
one should use real world pricing which is economically and also theoretically meaningful, as we have seen.
7
Diversification
To conclude the paper, we consider the practical problem of identifying or approximating the Kelly portfolio of a given market. We will indicate how to construct
proxies for the Kelly portfolio that can be used for portfolio optimization and valuation under the benchmark approach. For simplicity, let us consider a continuous
financial market with its benchmarked lh primary security account value Sf at
time t satisfying the driftless stochastic differential equation (SDE)
j
dSj -
sj '" (yj ,k dW k
t
-
t~t
t
(7.1)
k=l
for t E [0,00), with sg > 0, see Platen and Heath (2006). The more general setting of
jump diffusion markets has been considered in Platen (2005) and forthcoming work
will generalize the results presented below, avoiding any particular assumptions. In
(7.1) Wk = {Wtk, t E [O,oo)} denotes an independent standard Wiener process,
k E {I, 2, . . . }. A benchmarked portfolio S6d with fractions 7rLt invested at time
--- page 452 ---

A Benchmark Approach to Investing and Pricing
423
t in the jth primary security account, where j E {I, 2, . .. , d} with d E {I, 2, ... },
satisfies the SDE
(7.2)
for t E [0,00), with Sgd > O.
It is clear that the benchmarked Kelly portfolio 5; equals the constant one and
its diffusion coefficients vanish. This leads us to define a sequence (SOd )dE {1 ,2, ... } of
benchmarked approximate K elly portfolios as a sequence of strictly positive portfolios
such that for all c > 0 we have
(7.3)
for t E [0,00).
Furthermore, a sequence (SOd)dE{1 ,2, ... } of benchmarked portfolios is called a
sequence of benchmar ked diversified portfolios if some constants K 1 , K 2 E (0, 00 )
and K 3 E {I, 2, ... } exist independently of d, such that for d E {K3, K 3 + I , ... }
each fraction 7rL,t is bounded in the form
(7.4)
almost surely for all j E {I , 2, ... , d} and t E [0,00).
If most benchmarked primary security accounts would have the same driving
Wiener process, then it may become difficult to form a benchmarked portfolio with
vanishing volatility. To avoid such a situation we assume that the given continuous
financial market is regular, which means that for all t E [0,00) and k E {I , 2, ... }
there exists a finite adapted stochastic process C = {Ct , t E [O,oo)} such that
(~Hk l) ,
<0 C,
(7.5)
almost surely.
This allows us to prove, similar as in Platen (2005), and Platen and Heath
(2006), the following Diversification Theorem:
Theorem 7.1.
In a regular continuous financial market each sequence of diversified portfolios is a sequence of approximate K elly portfolios.
Proof: For a sequence of diversified portfolios it follows from (7.4) and (7.5) that
--- page 453 ---

424
E. Platen
for each d E {l, 2, . . . } one has
~ (t, nj" ai k )' <; t, (~H"I Hkl) ,
(~H 'k l) ,
< (K2)2 Ct
-
d2K1
.
Consequently, we have for all c > 0 that
}~~ P (t (t 7rL,t CTi,k) 2 ;:::: c) = 0,
k=l
J=l
which proves (7.3).
D
8
Conclusion
A general financial modeling and pricing framework, the benchmark approach, has
been presented, which only assumes the existence of the numeraire portfolio. It
turns out that this portfolio coincides with the Kelly portfolio, which is in several
ways the "best" performing strictly positive portfolio. It can be used as benchmark
in the traditional sense of portfolio optimization but also as numeraire in derivative pricing. Under the benchmark approach, the classical Law of One Price does
generally not hold. It has been replaced by the Law of the Minimal Price, according to which the minimal replicating price process for a given contingent claim is
trendless when expressed in units of the Kelly portfolio. By exploiting this fact, the
real world pricing concept emerges with the Kelly portfolio as numeraire and the
real world probability measure as pricing measure. Real world pricing turns out to
be the natural pricing concept for nonhedgable contingent claims in an incomplete
market. Certain weak forms of arbitrage may exist under the benchmark approach
that are excluded under the classical no-arbitrage approach. However, this does
not harm the economic viability of the resulting general modeling framework. It
has been shown that diversified portfolios approximate asymptotically in a regular
market the Kelly portfolio, as the number of constituents increases.
References
Bajeux-Besnainou, I. and R. Portait (1997). T he numeraire portfolio: A new perspective
on financial theory. The European Journal of Finance, 3, 291- 309.
--- page 454 ---

A Benchmark Approach to Investing and Pricing
425
Becherer, D. (2001). The numeraire portfolio for unbounded semimartingales. Finance and
Stochastics, 5, 327- 34l.
Breiman, L. (1960) . Investment policies for expanding business optimal in a long run sense.
Naval Research Logistics Quarterly, 7 (4), 647 - 65l.
Browne, S. (1998). The return on investment from proportional portfolio strategies. Advances in Applied Probability, 30(1), 216- 238.
Biihlmann, H. and E. Platen (2003). A discrete time benchmark approach for insurance
and finance. ASTIN Bulletin, 33(2), 153- 172.
Cochrane, J. H. (2001). Asset Pricing. US: Princeton University Press.
Constantinides, G. M. (1992) . A theory of the nominal structure of interest rates. Review
Financial Studies, 5, 531- 552.
Davis, M. H. A. (1997). Option pricing in incomplete markets. In M. A. H. Dempster
and S. R. Pliska (Eds.), Mathematics of Derivative Securities, pp. 227- 254. UK:
Cambridge University Press.
Debreu, G. (1959) . Theory of Value. New York: John Wiley.
Delbaen, F. and W. Schachermayer (1998). The fundamental theorem of asset pricing for
unbounded stochastic processes. Mathematische Annalen, 312, 215- 250.
Doob, J. L. (1953). Stochastic Processes. New York: John Wiley.
Duffie, D. (2001) . Dynamic Asset Pricing Theory (3rd ed.). US: Princeton University
Press.
Fernholz, E. R. and 1. Karatzas (2005) . Relative arbitrage in volatility-stabilized markets.
Annals of Finance, 1(2) , 149- 177.
Follmer, H. and M. Schweizer (1991). Hedging of contingent claims under incomplete
information. In M. H. A. Davis and R. J . Elliott (Eds.), Applied Stochastic Analysis,
Vol. 5 of Stochastics Monograph, pp. 389-414. New York: Gordon and Breach.
Hakansson, N. H. (1971). Capital growth and the mean-variance approach to portfolio
selection. Journal of Financial and Quantitative Analysis, 6(1) , 517- 557.
Harrison, J. M. and D. M. Kreps (1979) . Martingale and arbitrage in multi period securities
markets. Journal of Economic Theory, 20, 381- 408.
Hofmann, N., E . Platen, and M. Schweizer (1992) . Option pricing under incompleteness
and stochastic volatility. Mathematical Finance, 2(3) , 153-187.
Ingersoll, J . E. (1987). Theory of Financial Decision Making. Studies in Financial Economics. Rowman and Littlefield.
Karatzas, 1. and C. Kardaras (2007). The numeraire portfolio in semi martingale financial
models. Finance Stochastics, 11(4), 447- 493.
Karatzas, 1. and S. E. Shreve (1998) . Methods of Mathematical Finance, Volume 39 of
Appl. Math. Springer.
Kardaras, C. and E. Platen (2008a). Minimizing the expected market time to reach a
certain wealth level. Technical report, University of Technology, Sydney. QFRC Research Paper 230, to appear in SIAM J. Financial Mathematics.
Kardaras, C. and E. Platen (2008b) . On financial markets where only buy-and-hold trading
is possible. Technical report, University of Technology, Sydney. QFRC Research
Paper 213.
Kelly, J. R. (1956) . A new interpretation of information rate. Bell Syst. Techn. J., 35,
917- 926.
Latane, H. (1959). Criteria for choice among risky ventures. J. Political Economy, 38,
145- 155.
Lintner, J . (1965). The valuation of risk assets and the selection of risky investments in
stock portfolios and capital budgets. Rev. Econom. Statist. , 47, 13- 37.
--- page 455 ---

426
E. Platen
Loewenstein, M. and G. A. Willard (2000). Local martingales, arbitrage, and viability:
Free snacks and cheap thrills. Econometric Theory, 16(1), 135- 161.
Long, J. B. (1990) . The numeraire portfolio. J. Financial Economics, 26, 29-69.
Markowitz, H. (1976) . Investment for the long run: New evidence for an old rule. J.
Finance, 31(5), 1273- 1286.
Merton, R. C. (1973a) . An intertemporal capital asset pricing model. Econometrica, 41,
867-888.
Merton, R. C. (1973b) . Theory of rational option pricing. Bell J. Econ. Management Sci.,
4, 141-183.
Platen, E . (2002) . Arbitrage in continuous complete markets. Adv. in Appl. Probab., 34(3) ,
540- 558.
Platen, E. (2004) . A benchmark framework for risk management. In Stochastic Processes
and Applications to Mathematical Finance, pp. 305- 335. Proceedings of the Ritsumeikan Intern. Symposium: World Scientific.
Platen, E. (2005) . Diversified portfolios with jumps in a benchmark framework. Asia-
Pacific Financial Markets, 11(1), 1-22.
Platen, E. (2006) . A benchmark approach to finance. Math. Finance, 16(1) , 131- 151.
Platen, E. (2009). Real world pricing of long term contracts. Technical report, University
of Technology, Sydney. QFRC Research Paper.
Platen, E. and D. Heath (2006). A Benchmark Approach to Quantitative Finance. New
York: Springer.
Roll, R. (1973). Evidence on the "Growth-Optimum" model. J. Finance, 28(3) , 551- 566.
Ross, S. A. (1976). The arbitrage theory of capital asset pricing. J. Economic Theory, 13,
341- 360.
Schweizer, M. (1995). On the minimal martingale measure and the Follmer-Schweizer
decomposition. Stochastic Anal. Appl. , 13, 573- 599.
Sharpe, W. F. (1964). Capital asset prices: A theory of market equilibrium under conditions of risk. J. Finance, 19, 425- 442.
Shiryaev, A. N. (1984). Probability. New York: Springer.
Thorp, E. O. (1972). Portfolio choice and the Kelly criterion. In Proceedings of the 1971
Business and Economics Section of the American Statistical Association, Volume 21,
pp.5- 224.
--- page 456 ---

29
Growing Wealth with Fixed-Mix Strategies*
Michael A. H. Dempster
Centre for Financial Research, University of Cambridge, United Kingdom
mahd2@cam.ac. uk
Igor V. Evstigneev
Economics Department, School of Social Sciences,
University of Manchester, United Kingdom
igor. evstigneev@manchester.ac.uk
Klaus Reiner Schenk-Hoppe
Leeds University Business School and School of Mathematics,
University of Leeds, United Kingdom
K.R.Schenk-Hoppe@leeds.ac.uk
Abstract
This chapter surveys theoretical research on the long-term performance of fixedmix investment strategies. These self-financing strategies rebalance the portfolio
over time so as to keep constant the proportions of wealth invested in various
assets. The main result is that wealth can be grown from volatility. Our findings
demonstrate the benefits of active portfolio management and the potential of
financial engineering.
1
Introduction
427
Investment advice is usually based on some optimality principle such as the maximization of expected utility or the growth rate. The present chapter takes a broader
view by studying generic features of an investment style based on constant proportions, or fixed-mix, strategies. These self-financing strategies aim to maintain fixed
proportions between the value of portfolio positions by trading in the market at
'Financial support by the Finance Market Fund, Norway (Stability of Financial Markets: An
Evolutionary Approach) and the National Center of Competence in Research Financial Valuation and Risk Management, Switzerland (Behavioural and Evolutionary Finance) is gratefully
acknowledged. This chapter was written during KRSH's visit to the Department of Finance and
Management Science at the Norwegian School of Economics and Business Administration in June
2009. We are grateful to editors Edward O. Thorp and William T. Ziemba for their many helpful
comments.
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
