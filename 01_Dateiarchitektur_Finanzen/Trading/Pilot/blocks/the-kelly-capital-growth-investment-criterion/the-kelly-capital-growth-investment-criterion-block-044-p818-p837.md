# The Kelly capital growth investment criterion _ theory and -- Leonard C_ Maclean, Edward O_ Thorp, W_ T_ Ziemba, Leonard -- World Scientific Handbook -- isbn13 9781283148344 -- bec576e26410d0c695fd5b867d08ec4f -- An.pdf — pages 818–837

--- page 818 ---

Chapter 9
54
THE KELLY CRITERION IN BLACKJACK SPORTS BETTING,
AND THE STOCK MARKET*
EDWARD O. THORP
Edward O. Thorp and Associates, Newport Beach, CA 92660, USA
Contents
Abstract
Keywords
1. Introduction
2. Coin tossing
3. Optimal growth: Kelly criterion formulas for practitioners
3.1. The probability ofreaching a fixed goal on or before 11 trials
3.2. The probability of ever being reduced to a fraction x of this initial bankroll
3.3. The probability of being at or above a specified value at the end of a specified number of
789
386
386
387
388
392
392
394
trials
395
3.4. Continuous approximation of expected time to reach a goal
396
3.5. Comparing fixed fraction strategies: the probability that one strategy leads another after 11
trials
396
4. The long run: when will the Kelly strategy "dominate"?
398
5. Blackjack
399
6. Sports betting
401
7. Wall street: the biggest game
405
7.1. Continuous approximation
406
7.2. The (almost) real world
409
7.3. The case for "fracti onal Kelly"
411
7.4. A remarkable formula
414
8. A case study
415
8.1. The constraints
416
8.2. The analysis and results
416
8.3. The recommendation and the result
417
8.4. The theory for a portfolio of securities
418
Paper presented at: The I Oth International Conference on Gambling and Risk Taking. Montreal, June 1997.
published in: Finding the Edge: Mathematical Analysis of Casino Games. edited by O. Vancura. 1.A. Cornelius, w.R. Eadington. 2000. Corrections added April 20, 2005.
Handbook of Asset and Liability Management, Volume I
Edited by S.A. Zenios and W. T. Ziemha
© 2006 Published by Elsevier B. V.
DOl: JO.JOJ6/SJ872-0978(06)OJ009-X
--- page 819 ---

790
386
9. My experience with the Kelly approach
10. Conclusion
Acknow ledgements
Appendix A. Integrals for deriving moments of E 00
Appendix B. Derivation of formula (3.1)
Appendix C. Expected time to reach goal
References
Abstract
E. 0. Thorp
£.0. Thorp
419
420
420
420
421
423
428
The central problem for gamblers is to find positive expectation bets. But the gambler also needs to know how to manage his money, i.e., how much to bet. In the stock
market (more inclusively, the securities markets) the problem is similar but more complex. The gambler, who is now an "investor", looks for "excess risk adjusted return".
In both these settings, we explore the use of the Kelly criterion, which is to maximize
the expected value of the logarithm of wealth ("maximize expected logarithmic utility"). The criterion is known to economists and financial theorists by names such as
the "geometric mean maximizing portfolio strategy", maximizing logarithmic utility,
the growth-optimal strategy, the capital growth criterion, etc. The author initiated the
practical application of the Kelly criterion by using it for card counting in blackjack.
We will present some useful formulas and methods to answer various natural questions
about it that arise in blackjack and other gambling games. Then we illustrate its recent
use in a successful casino sports betting system. Finally, we discuss its application to
the securities markets where it has helped the author to make a thirty year total of 80
billion dollars worth of "bets".
Keywords
Kelly criterion, betting, long run investing, portfolio allocation, logarithmic utility,
capital growth
JEL classification: C61, D81, G 1
--- page 820 ---

The Kelly Criterion in Blackjack Sports Betting, and the Stock Market
791
Ch. 9:
The Kelly Criterion in Blackjack Sports Betting, and the Stock Market
387
1. Introduction
The fundamental problem in gambling is to find posItIve expectation betting opportunities. The analogous problem in investing is to find investments with excess
risk-adjusted expected rates of return. Once these favorable opportunities have been
identified, the gambler or investor must decide how much of his capital to bet. This
is the problem which we consider here. It has been of interest at least since the
eighteenth century discussion of the St. Petersburg Paradox (Feller, 1966) by Daniel
Bernoulli.
One approach is to choose a goal, such as to minimize the probability of total loss
within a specified number of trials, N. Another example would be to maximize the
probability of reaching a fixed goal on or before N trials (Browne, 1996).
A different approach, much studied by economists and others, is to value money
using a utility function. These are typically defined for all non-negative real numbers,
have extended real number values, and are non-decreasing (more money is at least as
good as less money). Some examples are U (x) = x{/ , 0 :::;; a < 00, and U (x) = log x,
where log means loge' and log 0 = -00. Once a utility function is specified, the object
is to maximize the expected value of the utility of wealth.
Daniel Bernoulli used the utility function logx to "solve" the St. Petersburg Paradox. (But his solution does not eliminate the paradox because every utility function
which is unbounded above, including log, has a modified version of the St. Petersburg
Paradox.) The utility function log x was revisited by Kelly (1956) where he showed
that it had some remarkable properties. These were elaborated and generalized in an
important paper by Breiman (1961). Markowitz (1959) illustrates the application to securities. For a discussion of the Kelly criterion (the "geometric mean criterion") from
a finance point of view, see McEnally (1986). He also includes additional history and
references.
I was introduced to the Kelly paper by Claude Shannon at M.l.T. in 1960, shortly
after I had created the mathematical theory of card counting at casino blackjack. Kelly's
criterion was a bet on each trial so as to maximize E log X , the expected value of
the logarithm of the (random variable) capital X. I used it in actual play and introduced it to the gambling community in the first edition of Beat the Dealer (Thorp,
1962). If all blackjack bets paid even money, had positive expectation and were independent, the resulting Kelly betting recipe when playing one hand at a time would
be extremely simple: bet a fraction of your current capital equal to your expectation.
This is modified somewhat in practice (generally down) to allow for having to make
some negative expectation "waiting bets", for the higher variance due to the occurrence of payoffs greater than one to one, and when more than one hand is played at a
time.
Here are the properties that made the Kelly criterion so appealing. For ease of understanding, we illustrate using the simplest case, coin tossing, but the concepts and
conclusions generalize greatly.
--- page 821 ---

792
E. 0. Thorp
388
E.O. Thorp
2. Coin tossing
Imagine that we are faced with an infinitely wealthy opponent who will wager even
money bets made on repeated independent trials of a biased coin. Further, suppose that
on each trial our win probability is p > 1/ 2 and the probability oflosing is q = 1 - p.
Our initial capital is Xo. Suppose we choose the goal of maximizing the expected value
E (X,,) after n tria~s. How much should we bet, Bk, on the kth trial? Letting Tk = 1 if the
kth trial is a win and Tk = -I ifit is a loss, then Xk = Xk- I +TkBk for k = 1, 2, 3, ... ,
and X" = Xo + :L%=I TkBk. Then
"
"
Since the game has a positive expectation, i.e., p - q > 0 in this even payoff situation,
then in order to maximize E(X,,) we would want to maximize E(Bd at each trial.
Thus, to maximize expected gain we should bet all of our resources at each trial. Thus
BI = Xo and if we win the first bet, B2 = 2X 0, etc. However, the probability of ruin is
given by 1 - p" and with p < I, lim,,--+oo[ I - p"] = I so ruin is almost sure. Thus the
"bold" criterion of betting to maximize expected gain is usually undesirable.
Likewise, if we play to minimize the probability of eventual ruin (i.e., "ruin" occurs
if Xk = 0 on the kth outcome) the well-known gambler's ruin formula in Feller (\966)
shows that we minimize ruin by making a minimum bet on each trial, but this unfortunately also minimizes the expected gain. Thus "timid" betting is also unattractive.
This suggests ·an intermediate strategy which is somewhere between maximizing
E(X,,) (and assuring ruin) and minimizing the probability of ruin (and minimizing
E (X,,». An asymptotically optimal strategy was first proposed by Kelly (\956).
In the coin-tossing game just described, since the probabilities and payoffs for each
bet are the same, it seems plausible that an "optimal" strategy will involve always wagering the same fraction f of your bankroll. To make this possible we shall assume
from here on that capital is infinitely divisible. This assumption usually does not matter
much in the interesting practical applications.
If we bet according to Bi = f Xi - I, where 0 ~ f ~ I, this is sometimes called "fixed
fraction" betting. Where Sand F are the number of successes and failures, respectively,
in n trials, then our capital after n trials is X" = Xo(l + nS
(1- nF, where S + F = n.
With f in the interval 0 < f < I, Pr(X" = 0) = O. Thus "ruin" in the technical sense
of the gambler's ruin problem cannot occur. "Ruin" shall henceforth be reinterpreted to
mean that for arbitrarily small positive E, lim"--+oo[Pr(X,, ~ E)] = I. Even in this sense,
as we shall see, ruin can occur under certain circumstances.
We note that since
[ X ] 1/"
e"log
X~
--- page 822 ---

The Kelly Criterion in Blackjack Sports Betting, and the Stock Market
793
Ch. 9:
The Kelly Criterion .in) Blackjack Sporls Betting, and the Stock Market
389
the quantity
[ X"]! /,,
S
F
G,,(f) = log -
= -log(1 + j) + -Iog(l - j)
Xo
n
n
measures the exponential rate of increase per trial. Kelly chose to maximize the expected
value of the growth rate coefficient, g(f), where
g(f) = E{ 10g[~~r /"}. = E{ ~ 10g(1 + j) + =
l~g(1 - j)}
= P 10g(1 + j) + q 10g(1 - j).
Note that g(f) = (1 /n)E(logX,,) - (l/n)logXo so for n fixed, maximizing g(f) is
the same as maximizing E log X". We usually will talk about maximizing g(f) in the
discussion below. Note that
,
p
q
p-q-f
g (f) = 1 + f -
1 - f = (1 + j) (1 _ j) = 0
when f = f* = p - q.
Now
g"(j) = -p/(1 + j)2 - q/(1 - j)2 < 0
so that g' (f) is monotone strictly decreasing on [0, 1). Also g' (0) = p - q > 0 and
lim/---> !- g' (f) = -00. Therefore by the continuity of g' (j), g(f) has a unique maxie
mum at f = f*, where g(f*) = p log p + q log q + log 2 > O. Moreover, g(O) = 0 and
limj--->qg(f) = -00 so there is a unique number f,. > 0, where 0 < f* < fe < 1,
such that g(fc) = O. The nature of the function g(f) is now apparent and a graph of
g(f) versus f appears as shown in Figure I.
The following theorem recounts the important advantages of maximizing g(f). The
details are omitted here but proofs of (i)-(iii), and (vi) for the simple binomial case
can be found in Thorp (1969); more general proofs of these and of (iv) and (v) are in
Breiman (1961).
Theorem 1. (i) If g(f) > 0, then limn->oo X" = 00 almost surely, i.e., for each M,
Pr[liminfn->oo XII > M] = 1;
(ii) If g(j) < 0, then limll->oo X" = 0 almost surely; i.e., for each 8
>
0,
Pr[limsuPn->oo X" < 8] = 1;
(iii) If g(f) = 0, then lim sUPn-> 00 Xn = 00 a.s. and lim inf,,-> 00 Xn = 0 a.s.
(iv) Given a strategy cJ>* which maximizes E log X" and any other "essentially
different" strategy cJ> (not necessarily a fixed fractional betting strategy), then
lim'l->oo Xn(cJ>*)/ X,,(cJ» = 00 a.s.
(v) The expected time for the current capital X" to reach any fixed preassigned goal
C is, asymptotically, least with a strategy which maximizes E log X".
(vi) Suppose the return on one unit bet on the ith trial is the binomial random variable Ui; further, suppose that the probability of success is Pi, where 1/2 < Pi < l.
--- page 823 ---

794
E. 0. Thorp
390
E.O. Thorp
G(f)
o
f
Fig. I.
Then E log XII is maximized by choosing on each trial the fraction 1;* = Pi - qi which
maximizes E log(1 + if Vi).
Part (i) shows that, except for a finite number of terms, the player's fortune XII will
exceed any fixed bound M when f is chosen in the interval (0, fe) . But, if f > f e,
part (ii) shows that ruin is almost sure. Part (iii) demonstrates that if f = fe, X I1 will
(almost surely) oscillate randomly between °
and +00. Thus, one author's statement
that XI1 -+ Xo as n -+ 00, when f = f e, is clearly contradicted. Parts (iv) and (v)
show that the Kelly strategy of maximizing E log XII is asymptotically optimal by two
important criteria. An "essentially different" strategy is one such that the difference
E In X,: - E In XI1 between the Kelly strategy and the other strategy grows faster than
the standard deviation of In X~ - In XII' ensuring P (In X~ - In XII > 0) -+ 1. Part (vi)
establishes the validity of utilizing the Kelly method of choosing 1;* on each trial (even
if the probabilities change from one trial to the next) in order to maximize E log X n .
Example 2.1. Player A plays against an infinitely wealthy adversary. Player A wins
even money on successive independent flips of a biased coin with a win probability of
p = .53 (no ties). Player A has an initial capital of Xo and capital is infinitely divisible.
--- page 824 ---

The Kelly Criterion in Blackjack Sports Betting, and the Stock Market
795
Ch. 9:
The Kelly Criterion in Blackjack Sports Betting, and the Stock Market
391
Applying Theorem I(vi), f* = p -
q = .53 - .47 = .06. Thus 6% of current capital
should be wagered on each play in order to cause XII to grow at the fastest rate possible
consistent with zero probability of ever going broke. If Player A continually bets a
fraction smaller than 6%, XII will also grow to infinity but the rate will be slower.
If Player A repeatedly bets a fraction larger than 6%, up to the value f e, the same
thing applies. Solving the equation g(f) = .5310g(l + f) + .4710g(1 -
f) = 0
numerically on a computer yields fe = .11973-. So, if the fraction wagered is more
than about 12%, then even though Player A may temporarily experience the pleasure of
a faster win rate, eventual downward fluctuations will inexorably drive the values of XII
toward zero. Calculation yields a growth coefficient of g(f*) = f(.06) = .001801 so
that after n successive bets the log of Player A's average bankroll will tend to .001801n
times as much money as he started with. Setting .00180 I n = log 2 gives an expected
time of about n = 385 to double the bankroll.
The Kelly criterion can easily be extended to uneven payoff games. Suppose Player A
wins b units for every unit wager. Further, suppose that on each trial the win probability
is p > 0 and pb - q > 0 so the game is advantageous to Player A. Methods similar to
those already described can be used to maximize
g(f) = E 10g(XIII Xo) = P log(l + bf) + q log(l - f).
Arguments using calculus yield f* = (bp - q) I b, the optimal fraction of current capital
which should be wagered on each play in order to maximize the growth coefficient g(f).
This formula for f* appeared in Thorp (1984) and was the subject of an April 1997
discussion on the Internet at Stanford Wong's website, http://bj2I.com (miscellaneous
free pages section). One claim was that one'can only lose the amount bet so there was
no reason to consider the (simple) generalization of this formula to the situation where
a unit wager wins b with probability p > 0 and loses a with probability q . Then if
the expectation m == bp - aq > 0, f* > 0 and f* = mlab. The generalization
does stand up to the objection. One can buy on credit in the financial markets and lose
much more than the amount bet. Consider buying commodity futures or selling short a
security (where the loss is potentially unlimited). See, e.g., Thorp and Kassouf (1967)
for an account of the E.L. Bruce short squeeze.
For purists who insist that these payoffs are not binary, consider selling short a binary
digital option. These options are described in Browne (1996).
A criticism sometimes applied to the Kelly strategy is that capital is not, in fact,
infinitely divisible. In the real world, bets are multiples of a minimum unit, such as
$1 or $.0 I (penny "slots"). In the securities markets, with computerized records, the
minimum unit can be as small as desired. With a minimum allowed bet, "ruin" in the
standard sense is always possible. It is not difficult to show, however (see Thorp and
Walden, 1966) that if the minimum bet allowed is small relative to the gambler's initial
capital, then the probability of ruin in the standard sense is "negligible" and also that
the theory herein described is a useful approximation. This section follows Rotando and
Thorp (1992).
--- page 825 ---

796
E. O. Thorp
392
£.0. Thorp
3. Optimal growth: Kelly criterion formulas for practitioners
Since the Kelly criterion asymptotically maximizes the expected growth rate of wealth,
it is often called the optimal growth strategy. It is interesting to compare it with the other
fixed fraction strategies. I will present some results that I have found useful in practice.
My object is to do so in a way that is simple and easily understood. These results have
come mostly from sitting and thinking about "interesting questions". I have not made
a thorough literature search but I know that some of these results have been previously
published and in greater mathematical generality. See, e.g., Browne (1996, 1997) and
the references therein.
3. J. The probability of reaching a fixed goal on or before n trials
We first assume coin tossing. We begin by noting a related result for standard Brownian
motion. Howard Tucker showed me this in 1974 and it is probably the most useful single
fact I know for dealing with diverse problems in gambling and in the theory of financial
derivatives.
For standard Brownian motion X (t), we have
p(sup[X(t) - (at +b)] ~ 0, 0 (
t ( T)
= N(-a - (3) + e- 2{/b N(a - (3)
(3.1)
where a = ag and f3 = b / g. See Figure 2. See Appendix B for Tucker's derivation
of (3.1).
In our application a < O,b > o so we expect limT ...... oo P(X(t) ~ at+b, 0 ( t (
T)
=1.
Let f be the fraction bet. Assume independent identically distributed (i.d.d.) trials Yi ,
i = I, ... ,n, with P(Yi = I) = p > 1/2, P(Yi = -I) = q < 1/2; also assume p < 1
to avoid the trivial case p = I.
X(!)
/'
(0, b)
slope a< °
/
at+ b
/'
/'
(0,0)
T
!
b
(IOT ,O)
Fig. 2.
--- page 826 ---

The Kelly Criterion in Blackjack Sports Betting, and the Stock Market
797
Ch. 9:
The Kelly Criterion in Blackjack Sports Belling, and the Stock Market
393
Bet a fixed fraction f, 0 < f < 1, at each trial. Let Vk be the value of the gambler
or investor's bankroll after k trials, with initial value Vo . Choose initial stake Vo = 1
(without loss of generality); number of trials n; goal C > I.
What is the probability that Vk ?': C for some k, 1 :s; k :s; n? This is the same as the
probability that log Vk ?': log C for some k, I :s; k :s; n. Letting In = loge we have:
k
Vk = n(l + Yd)
and
i - I
k
In Vk = Lln(l + Yif) ,
i=1
k
ElnVk = LEln(l +Yif),
i=l
k
Var(ln Vk) = L Var(ln(l + Yi f)),
i=1
E In(l + Yi f) = p In(l + f) + q In(l - f) == m == g(f),
Var[ln(1 + Yif)] = p[ln(1 + f)]2 + q[ln(1 - f)]2 - m2
= (p _ p2)[ln(1 + f)]2 + (q _ q2)[ln(l _ f)]2
- 2pq In(l + f) In(l - f)
= pq ([In ( 1 + f)]2 - 21n( 1 + f) In(l - f) + [InC 1 - f)]2}
= pq{ln[(1 + f)/(I - f)]}2 == s2.
Drift in n trials: mn .
Variance in n trials: s2n.
In Vk ?': InC, 1 :s; k:S; n,
iff
k L In(l + Yi f) ?': In C, I :s; k :s; n,
iff
i=1
k
Sk == L[ln(l + fif) - m] ?': InC - mk,
I :S; k :s; n,
i=l
We want Prob(Sk ?': In C - mk, I :s; k :s; n).
Now we use our Brownian motion formula to approximate SII by Prob(X (t) ?': In Cmt/s2, 1 :s; t :s; s2n) where each term of SII is approximated by an XU), drift 0 and
--- page 827 ---

798
E. 0. Thorp
394
E.O. Thorp
variance s2 (0 :::::; t :::::; s2, s2 :::::; t :::::; 2s2 , .. . , (n -
l)s2 :::::; t :::::; ns2). Note: the
approximation is only "good" for "large" n.
Then in the original formula (3.1):
T = s2n ,
b = InC,
a = -m/s2,
(X = afl = -m..jii/s,
f3 = b/fl = InC/s..jii.
Example 3.1.
C =2,
n = 104 ,
p = .51,
q = .49,
f = .0117,
m = .000165561,
052 = .000136848.
Then
PO = .9142.
Example 3.2. Repeat with
f = .02,
then
m = .000200013,
052 = .000399947
and
PO = .9214.
3.2. The probability of ever being reduced to a fraction x of this initial bankroll
This is a question that is of great concern to gamblers and investors. It is readily answered, approximately, by our previous methods.
Using the notation of the previous section, we want P(Vk :::::; x for some k, 1 :::::; k :::::;
00). Similar methods yield the (much simpler) continuous approximation formula:
Prob(·) = e2"h
where a = -m/s2 and b = -Inx
which can be rewritten as
Probe-) = x ;\(2m/o5 2 )
where /\ means exponentiation.
(3.2)
--- page 828 ---

The Kelly Criterion in Blackjack Sports Betting, and the Stock Market
Ch. 9:
The Kelly Criterion in Blackjack Sports Betting. and the Stock Market
Example 3.3.
p = .51,
f = 1* = .02,
2m/s = 1.0002,
Probe-) ":,, x.
799
395
We will see in Section 7 that for the limiting continuous approximation and the Kelly
optimal fraction 1*, P (VI; (f*) ~ x for some k ) 1) = x.
My experience has been that most cautious gamblers or investors who use Kelly
find the frequency of substantial bankroll reduction to be uncomfortably large. We can
see why now. To reduce this, they tend to prefer somewhat less than the full betting
fraction f*. This also offers a margin of safety in case the betting situations are less
favorable than believed. The penalty in reduced growth rate is not severe for moderate
underbetting. We discuss this further in Section 7.
3.3. The probability of being at or above a specified value at the end of a specified
number of trials
Hecht (1995) suggested setting this probability as the goal and used a computerized
search method to determine optimal (by this criterion) fixed fractions for p - q = .02
and various c, n and specified success probabilities.
This is a much easier problem than the similar sounding in Section 3.1. We have for
the probability that X (T) at the end exceeds the goal:
1 1
00
P(X(T» ) aT+b)= ~
exp/-x2/2T}dx
v2rrT
(/1'+1>
= --
exp/-u2 / 2} du
1 1
00
.J2rrT
(/1'1 /2+1>1'- 1/2
where u= x/~ so x = aT +b gives u~ = aT +b and U = aTI /2 +bT- I/2. The
integral equals
1 - N(aTI /2 + bT- I/2) = N( _(aTI /2 + bT- 1/ 2))
= 1- N(a + f3) = N(-a -
f3).
(3.3)
For example (3.1) f = .01l7 and P = .7947. For example (3.2) P = .7433. Example
(3.1) is for the Hecht optimal fraction and example (3.2) is for the Kelly optimal fraction .
Note the difference in P values.
Our numerical results are consistent with Hecht's simulations in the instances we
have checked.
Browne (1996) has given an elegant continuous approximation solution to the problem: What is the strategy which maximizes the probability of reaching a fixed goal C on
or before a specified time n and what is the corresponding probability of success? Note
--- page 829 ---

800
E. O. Thorp
396
£.0. Thorp
that the optimal strategy will in general involve betting varying fractions, depending on
the time remaining and the distance to the goal.
As an extreme example, just to make the point, suppose n = I and C = 2. If Xo < 1
then no strategy works and the probability of success is O. But if I ~ Xo < 2 one should
bet at least 2 -
Xo, thus any fraction f ? (2 - Xo) / Xo, for a success probability of p.
Another extreme example: n = 10, C = 2 10 = 1024, Xo = 1. Then the only strategy
which can succeed is to bet f = 1 on every trial. The probability of success is pI 0 for
this strategy and 0 for all others (if p < 1), including Kelly.
3.4. Continuous approximation of expected time to reach a goal
According to Theorem I(v), the optimal growth strategy asymptotically minimizes the
expected time to reach a goal. Here is what this means. Suppose for goal C that m(C)
is the greatest lower bound over all strategies for the expected time to reach C. Suppose
t*(C) is the expected time using the Kelly strategy. Then limc --,> 00 (t* (c) / m(c» = 1.
The continuous approximation to the expected number of trials to reach the goal
C > Xo = I is
n(C, f) = (lnC)/ g(f)
where f is any fixed fraction strategy. Appendix C has the derivation. Now g(f) has a
unique maximum at g(f*) so n(C, f) has a unique minimum at f = f *. Moreover,
we can see how much longer it takes, on average, to reach C if one deviates from f*·
3.5. Comparing fixed fraction strategies: the probability that one strategy leads
another after n trials
Theorem I (iv) says that wealth using the Kelly strategy will tend, in the long run, to
an infinitely large multiple of wealth using any "essentially different" strategy. It can
be shown that any fixed f -If * is an "essentially different" strategy. This leads to the
question of how fast the Kelly strategy gets ahead of another fixed fraction strategy, and
more generally, how fast one fixed fraction strategy gets ahead of (or behind) another.
If WI/ is the number of wins in n trials and n -
WI/ is the number of losses,
G(f) = (WI//n) In(l + f) + (1 - WI//n) In(l - f)
is the actual (random variable) growth coefficient.
As we saw, its expectation is
g(f) = E(G(f)) = p log(l + f) + q log(l - f)
and the variance of G(f) is
VarG(f) = (pq) / n)lln((l + f) / (lf))}2
(3.4)
(3.5)
and it follows that G(f), which has the form G(f) = a(L Tk) / n +b, is approximately
normally distributed with mean g(f) and variance VarG(f). This enables us to give
--- page 830 ---

The Kelly Criterion in Blackjack Sports Betting, and the Stock Market
801
Ch. 9:
The Kelly Criterion in Blackjack Sports Betting, and the Stock Market
397
the distribution of XI1 and once again answer the question of Section 3.3. We illustrate
this with an example.
Example 3.4.
p = .51,
q = .49,
1* = .02,
N = 10,000 and
s = standard deviation of G(f)
gls
1.5
1.0
.5
1
.01
.02
.03
g
.000150004
.000200013
.000149977
s
.0001
.0002
.0003
Pr(G(f) ( 0)
.067
.159
.309
Continuing, we find the distribution of G(h) - GUt). We consider two cases.
Case 1. The same game
Here we assume both players are betting on the same trials, e.g., betting on the same
coin tosses, or on the same series of hands at blackjack, or on the same games with the
same odds at the same sports book. In the stock market, both players could invest in the
same "security" at the same time, e.g., a no-load S&P 500 index mutual fund.
We find
E(G(h) - G(It») = plog((1 + 12)/(1 + It») + q 10g((1- 12)/(1 - 1\»)
and
Var( G (h) - G (ft)) = (pq In) { log [ C ~ ~~) C ~ ~: ) J r
where G(h) - G(ft> is approximately normally distributed with this mean and variance.
Case 2. Identically distributed independent games
This corresponds to betting on two different series of tosses with the same coin.
E(G(h) -
G(fl» is as before. But now Var(G(h) - G(fj)
= Var(G(h» +
Var(G(fd) because G(h) and G(fj) are now independent. Thus
Let
Var( G(h) - G(It») = (pq In) {[IOgC ~ ~~) r
+ [IOgC ~ ~: rJ}·
a = log ( 1 + 1\ ) ,
1 - It
b = log (1 + h).
1- 12
Then in Case 1, VI = (pq In)(a - b)2 and in Case 2, V2 = (pq In)(a2 + b2) and since
a, b > 0, VI . < V2 as expected. We can now compare the Kelly strategy with other
--- page 831 ---

802
E. O. Thorp
398
E.O. Thorp
fixed fractions to determine the probability that Kelly leads after n trials. Note that this
probability is always greater than 1/2 (within the accuracy limits of the continuous
approximation, which is the approximation of the binomial distribution by the normal,
with its well known and thoroughly studied properties) because g(f*) - g(f) > 0
where 1* = p - q and I -=1= 1* is some alternative. This can fail to be true for small n,
where the approximation is poor. As an extreme example to make the point, if n = 1,
any I > f* beats Kelly with probability p > 1/ 2. If instead n = 2, I > f* wins
with probability p2 and p2 > 1/ 2 if p > 1/.J2 ~ .707l. Also, I < f* wins with
probability I - p2 and 1 -
p2 > 1/ 2 if p2 < 1/ 2, i.e., p < 1/.J2 = .7071. So when
n = 2, Kelly always loses more than half the time to some other I unless p = 1/.J2.
We now have the formulas we need to explore many practical applications of the
Kelly criterion.
4. The long run: when will the Kelly strategy "dominate"?
The late John Leib wrote several articles for Blackjack Forum which were critical of the
Kelly criterion. He was much bemused by "the long run". What is it and when, if ever,
does it happen?
We begin with an example.
Example 4.1.
p = .51 ,
n = 10,000,
Vi and Si, i = 1, 2, are the variance and standard deviation, respectively, for Section 3.5
Cases I and 2, and R = V2/V[ = (a 2 + b2)/(a - b)2 so S2 = s[-/k Table I summarizes some results. We can also approximate v'"R with a power series estimate using
only the first term of a and of b: a ~ 2ft, b ~ 212 so v'"R == J I? + 122/111 - 121·
The approximate results, which agree extremely well, are 2.236, 3.606 and 1.581, respectively.
The first two rows show how nearly symmetric the behavior is on each side of the
optimal f* = .02. The column (g2 - gl) / s[ shows us that f* = .02 only has a .5
standard deviation advantage over its neighbors I = .0 I and I = .03 after n = 10,000
Table I
Comparing strategies
II
.Ii
g 2 -
g l
.1'1
C~2 - g l ) j.~ 1
~
.01
.02
.00005001
.00010000
.50
2.236
.03
.02
.00005004
.00010004
.50
3.604
.03
.01
.00000003
.00020005
.00013346
1.581
--- page 832 ---

The Kelly Criterion in Blackjack Sports Betting, and the Stock Market
803
Ch. 9:
The Kelly Criterion in Blackjack Sports Betting, and the Stock Market
399
Table 2
The long run: Cli2 - g I) /s after 11 trials
II
h
11 = 104
11=4 x 104
11=16 x 104
11 = 106
.01
.02
.5
1.0
2.0
5.0
.03
.02
.5
1.0
2.0
5.0
.03
.01
.000133
.000267
.000534
.001335
trials. Since this advantage is proportional to vIn, the column (g2 - gl)ISj from Table 1
gives the results of Table 2.
The factor JR in Table 1 shows how much more slowly h dominates fl in Case 2
versus Case 1. The ratio (g2 -
g I) 1 S2 is JR times as large so the same level of dominance takes R times as long. When the real world comparisons of strategies for practical
reasons often use Case 2 comparisons rather than the more appropriate Case I comparisons, the dominance of f* is further obscured. An example is players with different
betting fractions at blackjack. Case 1 corresponds to both betting on the same sequence
of hands. Case 2 corresponds to them playing at different tables (not the same table,
because Case 2 assumes independence). (Because of the positive correlation between
payoffs on hands played at the same table, this is intermediate between Cases 1 and 2.)
It is important to understand that "the long run", i.e., the time it takes for f* to
dominate a specified neighbor by a specified probability, can vary without limit. Each
application requires a separate analysis. In cases such as Example 4.1, where dominance
is "slow", one might argue that using f * is not important. As an argument against this,
consider two coin-tossing games. In game 1 your edge is 1.0%. In game 2 your edge
is 1.1 %. With one unit bets, after n trials the difference in expected gain is E2 - E I =
.00In with standard deviation s of about..JIn hence (E2 - EI )Is ~ .001 vlnl v'2 which
is 1 when n = 2 x 106 . So it takes two million trials to have an 84% chance of the
game 2 results being better than the game 1 results. Does that mean it's unimportant to
select the higher expectation game?
S. Blackjack
For a general discussion of blackjack, see Thorp (1962, 1966), Wong (1994) and Griffin
(1979). The Kelly criterion was introduced for blackjack by Thorp (1962). The analysis
is more complicated than that of coin tossing because the payoffs are not simply one
to one. In particular the variance is generally more than I and the Kelly fraction tends
to be less than for coin tossing with-the same expectation. Moreover, the distribution
of various payoffs depends on the player advantage. For instance the frequency of pair
splitting, doubling down, and blackjacks all vary as the advantage changes. By binning
the probability of payoff types according to ex ante expectation, and solving the Kelly
equations on a computer, a strategy can be found which is as close to optimal as desired.
--- page 833 ---

804
E. 0. Thorp
400
E.O. Thorp
There are some conceptual subtleties which are noteworthy. To illustrate them we'll
simplify to the coin toss model.
At each trial, we have with probability .5 a "favorable situation" with gain or loss X
per unit bet such that P(X = I) = .51 , P(X = -I) =.49 and with probability.5 an
unfavorable situation with gain or loss Y per unit bet such that P(Y = I) = .49 and
P(Y = -1) = .51. We know before we bet whether X or Y applies.
Suppose the player must make small "waiting" bets on the unfavorable situations in
order to be able to exploit the favorable situations. On these he will place "large" bets.
We consider two cases.
Case 1. Bet fa on unfavorable situations and find the optimal f* for favorable situations. We have
g(f) = .5(.5110g(l + f) + .4910g(1 - f))
+ .5(.4910g(l + fa) + .51 log (I -
fa»).
(5.1)
Since the second expression in (5.1) is constant, f maximizes g(f) if it maximizes the
first expression, so f* = P - q = .02, as usual. It is easy to verify that when there is
a spectrum of favorable situations the same recipe, f/ = Pi - qi for the ith situation,
holds. Again, in actual blackjack f * would be adjusted down somewhat for the greater
variance. With an additional constraint such as fi ( kfo, where k is typically some
integral multiple of fo, representing the betting spread adopted by a prudent player,
then the solution is just fi ( min(f/, kfo) .
Curiously, a seemingly similar formulation of the betting problem leads to rather
different results.
Case 2. Bet f in favorable situations and af in unfavorable situations, 0 ( a ( I.
Now the bet sizes in the two situations are linked and both the analysis and results
are more complex. We have a Kelly growth rate of
g(f) = .5(.5110g(1 + f) + .4910g(1 - f))
+ .5(.4910g(1 + af) + .5110g(l - af)) .
(5.2)
If we choose a = 0 (no bet in unfavorable situations) then the maximum value for g(f)
is at f* = .02, the usual Kelly fraction.
If we make "waiting bets", corresponding to some value of a > 0, this will shift the
value of f* down, perhaps even to O. The expected gain divided by the expected bet is
.02(1 - a)/ (l + a) , a ~ O. If a = 0 we get .02, as expected. If a = 1, we get 0, as
expected: this is a fair game and the Kelly fraction is f* = O. As a increases from 0
to 1 the (optimal) Kelly fraction f* decreases from .02 to O. Thus the Kelly fraction for
favorable situations is less in this case when bets on unfavorable situations reduce the
overall advantage of the game.
Arnold Snyder called to my attention the fact that Winston Yamashita had (also) made
this point (March 18, 1997) on the "free" pages, miscellaneous section, of Stanford
Wong's web site.
--- page 834 ---

The Kelly Criterion in Blackjack Sports Betting, and the Stock Market
Ch. 9:
The Kelly Criterion in Blackjack Sports Betting, and the Stock Market
a
1'*
a
0
.0200
1/3
.1
.0178
.4
.2
.0154
.5
.3
.0128
.6
Table 3
f* versus a
1'*
.0120
.0103
.0080
.0059
a
.7
.8
.9
1.0
805
401
1'*
.0040
.0024
.0011
.0000
For this example, we find the new f* for a given value of a, 0 < a < 1, by solving
g' (f) = O. A value of a = 1/3, for instance, corresponds to a bet of 1/3 unit on Y and
I unit on X, a betting range of 3 to 1. The overall expectation is .0 I. Calculation shows
/* = .01200l. Table 3 shows how /* varies with a.
To understand why Cases I and 2 have different /*, look first at Equation (5.1).
The part of g(f) corresponding to the unfavorable situations is fixed when fo is fixed.
Only the part of g(f) corresponding to the favorable situations is affected by varying f.
Thus we maximize g(f) by maximizing it over just the favorable situations. Whatever
the result, it is then reduced by a fixed quantity, the part of g containing fo. On the
other hand, in Equation (5.2) both parts of g(f) are affected when f varies, because
the fraction af used for unfavorable situations bears the constant ratio a to the fraction
f used in favorable situations. Now the first term, for the favorable situations, has a
maximum at f = .02, and is approximately "flat" nearby. But the second term, for
the unfavorable situations, is negative and decreasing moderately rapidly at f = .02.
Therefore, it we reduce f somewhat, this term increases somewhat, while the first term
decreases only very slightly. There is a net gain so we find f* < .02. The greater a
is, the more important is the effect of this term so the more we have to reduce f to
get f*, as Table 3 clearly shows. When there is a spectrum of favorable situations the
solution is more complex and can be found through standard multivariable optimization
techniques.
The more complex Case 2 corresponds to what the serious blackjack player is likely
to need to do in practice. He will have to limit his current maximum bet to some multiple
of his current minimum bet. As his bankroll increases or decreases, the corresponding
bet sizes will increase or decrease proportionately.
6. Sports betting
In 1993 an outstanding young computer science Ph.D. told me about a successful sports
betting system that he had developed. Upon review I was convinced. I made suggestions
for minor simplifications and improvements. Then we agreed on a field test. We found
a person who was extremely likely to always be regarded by the other sports bettors as
a novice. I put up a test bankroll of $50,000 and we used the Kelly.system to estimate
our bet size.
--- page 835 ---

806
E. O. Thorp
402
£.0. Thorp
+80,000.00
+70,000.00 1- Total Profit
I
--------- Expected Profit I
+60.000.00
+50,000.00
+40,000.00
+30.000.00
+20,000.00
---t.
II ~
.
+10,000.00
+0.00
1
3
5
7
9
11
13
15
17
19
21
23
25
27
29
31
33
35
37
39
41
43
- 10,000.00
Fig. 3. Betting log Type 2 sports.
+70.000.00
+60,000.00 H -
Total Profit
I
------ Expected Profit I
~
....
1---
/
....
+50.000.00
+40.000.00
+30,000.00
+20,000.00
. -~- - -.-.--.------ --- .- -
--.-.----
.-.- -
--
I
+10,000.00
+0.00
_I, ~
1
5
9
13
17 21 25 29 33 37 41
45 49 53 57 61
65 69 73 77 8 1 85 89 93 97 101
-1 0.000.00
Fig. 4. Betting log Type I sports.
We bet on 101 days in the first four and a half months of 1994. The system works for
various sports. The results appear in Figures 3 and 4. After 101 days of bets, our $50,000
bankroll had a profit of $123,00Q, about $68,000 from Type I sports and about $55,000
from Type 2 sports. The expected returns are shown as about $62,000 for Type 1 and
about $27,000 for Type 2. One might assign the additional $34,000 actually won to luck.
But this is likely to be at most partly true because our expectation estimates from the
model were deliberately chosen to be conservative. The reason is that using too large
an f* and overbetting is much more severely penalized than using too small an f * and
underbetting.
.
--- page 836 ---

The Kelly Criterion in Blackjack Sports Betting, and the Stock Market
807
efl. 9:
The Kelly Criterion in Blackjack Sports Betting, and the Stock Market
403
Though $123,000 is a modest sum for some, and insignificant by Wall Street standards, the system performed as predicted and passed its test. We were never more than
a few thousand behind. The farthest we had to invade our bankroll to place bets was
about $10,000.
Our typical expectation was about 6% so our total bets ("action") were about
$2,000,000 or about $20,000 per day. We typically placed from five to fifteen bets a
day and bets ranged from a few hundred dollars to several thousand each, increasing as
our bankroll grew.
Though we had a net win, the net results by casino varied by chance from a substantial
loss to a large win. Particularly hard hit was the "sawdust joint" Little Caesar's. It "died"
towards the end of our test and I suspect that sports book losses to us may have expedited
its departure.
One feature of sports betting which is of interest to Kelly users is the prospect of
betting on several games at once. This also arises in blackjack when (a) a player bets
on multiple hands or (b) two or more players share a common bankroll. The standard
techniques readily solve such problems. We illustrate with:
Example 6.1. Suppose we bet simultaneously on two independent favorable coins with
betting fractions It and 12 and with success probabilities PI and P2, respectively. Then
the expected growth rate is given by
gUI, h) = PIP2 In(1 + II + h) + Plq2 ln(1 + It - h)
+ QlP2 ln(l - It + h) + QlQ2 ln(l - II - h)·
To find the optimal it and H we solve the simultaneous equations ag/alt = 0 and
ilg/a12 = O. The result is
I + f -
PI P2 -
q I q2 -
I
2 -
= c,
PIP2 + qlq2
It - 12 = PI q2 - ql P2 == d,
Plq2 + qlP2
it = (c + d)/2,
H = (c - d)/2.
(6.1)
These equations pass the symmetry check: interchanging 1 and 2 throughout maps
the equation set into itself.
An alternate form is instructive. Let mi = Pi - qi, i = 1, 2 so Pi = (1 + mj) /2 and
qi = (1 - mj)/2. Substituting in (6.1) and simplifying leads to:
ml +m2
c=----
l+mlm2 '
*
ml(l-m~)
II = I
2
2 '
-m l m2
(6.2)
which shows clearly the factors by which the It are each reduced from m7- Since the
mj are typically a few percent, the reduction factors are typically very close to 1.
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
