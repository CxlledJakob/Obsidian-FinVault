# The Kelly capital growth investment criterion _ theory and -- Leonard C_ Maclean, Edward O_ Thorp, W_ T_ Ziemba, Leonard -- World Scientific Handbook -- isbn13 9781283148344 -- bec576e26410d0c695fd5b867d08ec4f -- An.pdf — pages 58–77

--- page 58 ---

A New Interpretation of Information Rate
A NEW INTERPRETATION OF INFORMATION RATE
(b) Since the minimum value of H(a) subject to
obtains when
L~=l
s as
1
as = pes)
and H(X) = H(a), any deviation from fair odds helps the gambler.
31
923
(c) Since the gambler's exponential gain would be H(a) - H(X) if he had
no inside information, we can interpret R = H(X) - H(X/Y) as the increase
of Gmax due to the communication channel. When there is no channel, i.e.,
H(X/Y) = H(X) , Gmax is minimized (at zero) by setting
1
as =-
Ps
This gives further meaning to the concept "fair odds."
WHEN THERE IS A "TRACK TAKE"
In the case there is a "track take" the situation is more complicated. It can
no longer be assumed that L:s a(s/r) = 1. The gambler cannot make canceling
bets since he loses a percentage to the track. Let br = 1 - L:s a(s/r), i.e., the
fraction not bet when the received symbol is the rth one. Then the quantity to
be maximized is
G = LP(s,r)log[br +asa(s/r)),
(2)
rs
subject to the constraints
br + L a(s/r) = 1.
8
In maximizing (2) it is sufficient to maximize the terms involving a particular
value of r and to do this separately for each value of r since both in (2) and in
the associated constraints, terms involving different r's are independent. That
is, we must maximize terms of the type
Gr = q(r) L q(s/r) log[br + asa(s/r)]
s
subject to the constraint
br + La(s/r) = 1
s
--- page 59 ---

32
J L. Kelly, Jr.
924
THE BELL SYSTEM TECHNICAL JOURNAL, JULY 1956
Actually, each of these terms is the same form as that of the gambler's
exponential gain where there is no channel
G = LP(S) log[b + Qsa(s)].
(3)
8
We will maximize (3) and interpret the results either as a typical term in the
general problem or as the total exponential gain in the case of no communication
channel. Let us designate by A the set of indices, s, for which a(s) > 0, and by
>.' the set for which a(s) = O. Now at the desired maximum
fJG
p(s)Qs
10 e = k
for S£A
=
fJa(s)
b + a{s)Qs
g
fJG
L
pes)
loge = k
=
fJb
b + a(s)Qs
s
fJG
p(s)Q s I
< k
for S£A'
= -boge =
fJa(s)
where k is a constant. The equations yield
k = loge,
b
a(s) = pes) - -
Q s
b = l=2.
1-0"
for S£A
where p = L),P(S), a = L),(I/Qs), and the inequalities yield
I-p
p(s)Qs ;£ b = 1 _ a
for S£A'
We will see that the conditions
0'<1
p(s)Qs > 1-p
for S£A
I-a
p{s)Qs
~ 1-p
for S£A'
1-0'
completely determine A.
If we permute indices so that
p(S)Qs ~ pes + 1)Qs+1
--- page 60 ---

A New Interpretation of Information Rate
33
A NEW INTERPRETATION OF INFORMATION RATE
925
then A must consist of all s ~ t where t is a positive integer or zero. Consider
how the fraction
varies with t, where t t l
Pt = I>(s),
<Tt = L-;
1 as
Fo = 1
Now if p(l)al < 1, Ft increases with t until <Tt ~ 1. In this case t = 0 satisfies
the desired conditions and A is empty. If p(l)al > 1 Ft decreases with t until
p(t + l)at+1 < Ft or <Tt ~ 1. If the former occurs, i.e., p(t + l)at+l < Ft , then
Ft+1 > Ft and the fraction increases until <Tt ~ 1. In any case the desired value
of t is the one which gives Ft its minimum positive value, or if there is more
than one such value of t, the smallest. The maximizing process may be summed
up as follows:
(a) Permute indices so that p(s)as ~ p(s + l)aS+1
(b) Set b equal to the minimum positive value of
t
t
I-pt
'"
",1
--
where Pt = ~p(s), <Tt = ~ -
1 - <Tt
1
1 as
(c) Set a(s) = p(s) - bias or zero, whichever is larger. (The a(s) will sum to
1- b.)
The desired maximum G will then be
~
I-Pt
Gma:c = ~p(s) logp(s)a s + (1 - Pt) log -1--
1
-
<Tt
where t is the smallest index which gives
1- Pt
1 - <Tt
its minimum positive value.
It should be noted that if p(s)as < 1 for all s no bets are placed, but if
the largest p(s)as > 1 some bets might be made for which p(s)as < 1, i.e., the
expected gain is negative. This violates the criterion of the classical gambler
who never bets on such an event.
CONCLUSION
The gambler introduced here follows an essentially different criterion from
the classical gambler. At every bet he maximizes the expected value of the
logarithm of his capital. The reason has nothing to do with
--- page 61 ---

34
J L. Kelly, Jr.
926
THE BELL SYSTEM TECHNICAL JOURNAL, JULY 1956
the value function which he attached to his money, but merely with the fact
that it is the logarithm which is additive in repeated bets and to which the
law of large numbers applies. Suppose the situation were different; for example,
suppose the gambler'S wife allowed him to bet one dollar each week but not to
reinvest his winnings. He should then maximize his expectation (expected value
of capital) on each bet. He would bet all his available capital (one dollar) on
the event yielding the highest expectation. With probability one he would get
ahead of anyone dividing his money differently.
It should be noted that we have only shown that our gambler's capital will
surpass, with probability one, that of any gambler apportioning his money differently from ours but still in a fixed way for each received symbol, independent
of time or past events. Theorems remain to be proved showing in what sense, if
any, our strategy is superior to others involving a(sJr) which are not constant.
Although the model adopted here is drawn from the real-life situation of
gambling it is possible that it could apply to certain other economic situations.
The essential requirements for the validity of the theory are the possibility of
reinvestment of profits and the ability to control or vary the amount of money
invested or bet in different categories. The "channel" of the theory might correspond to a real communication channel or simply to the totality of inside
information available to the investor.
Let us summarize briefly the results of this paper. If a gambler places bets on
the input symbol to a communication channel and bets his money in the same
proportion each time a particular symbol is received, his capital will grow (or
shrink) exponentially. If the odds are consistent with the probabilities of occurrence of the transmitted symbols (Le., equal to their reciprocals), the maximum
value of this exponential rate of growth will be equal to the rate of transmission
of information. If the odds are not fair, i.e., not consistent with the transmitted symbol probabilities but consistent with some other set of probabilities, the
maximum exponential rate of growth will be larger than it would have been
with no channel by an amount equal to the rate of transmission of information.
In case there is a "track take" similar results are obtained, but the formulae
involved are more complex and have less direct information theoretic interpretations.
ACKNOWLEDGMENTS
I am indebted to R. E. Graham and C. E. Shannon for their assistance in
the preparation of this paper.
--- page 62 ---

Journal o/Political Economy, 67, 144-155 (1959)
35
4
CRITERIA FOR CHOICE AMONG RISKY VENTURES
HENRY ALLEN LATANE
Chapel Hill, North Carolina
THE SUB GOAL
T
HIS paper is concerned with the
problem of how to make rational
choices among strategies in situations involving uncertainty. Such choices
can be expressed through payout matrices
stated in terms of some measure of value
to be maximized. These matrices show
the probabilities of all relevant future occurrences and the payouts resulting from
the combined effects of each possible
strategy, on the one hand, and each
relevant future occurrence, on the other.l
All this information is needed to choose
the proper strategy rationally. It would
1 Payout matrices are shown in Tables 1, 2, and
3. The payouts represent the possible final outcomes
of choices among strategies. The matrices have
single-valued payouts and probabilities. Many, if
not all, decision problems can be reduced to such
form. Consider first the probabilities. A subjective
probability distribution of an imperfectly known
underlying probability can be reduced to a subjective probability of the event itself. For example, suppose a gambler believes that there is a 0.5 probability that a coin is biased so that it always comes up
tails and a 0.5 probability that it is unbiased. He
has a subjective probability of 0.25 for heads and
0.75 for tails, and these probabilities would be used
in his payout matrix as long as his probability beliefs remain unchanged. Consider next the payouts.
In much discussion of decision theory the payouts
are taken as given, with only the probabilities subject to uncertainty. However, in real life the sizes
of the payouts often are as subject to uncertainty as
are the probabilities. But, even when the payouts
are uncertain a matrix filled in with single values
can be constructed. If we have probability distributions of payouts for all specified occurrences (such as
heads and tail. in the toss of a coin), a payout matrix
can be constructed listing each possible payout and
the subjective probability of its occurrence. These
large matrices often can be reduced to simple twovalued distributions of payouts without much loss of
information.
be impossible for a decision-maker to
choose rationally among strategies if he
disregarded either the probability of the
relevant future occurrences or any of the
possible payouts.
The problem of rational decisionmaking can be broken down into three
steps: (1) deciding upon an objective and
criteria for choosing among strategies;
(2) filling out a payout matrix; and (3)
choosing among available strategies on
the basis of this matrix and the criteria.
In real life the second step-deciding
upon the size of the payout matrix, measured by the number of columns represen ting relevant future occurrences and rows
representing available strategies, and
filling in the matrix with reasonable estimates of payouts and probabilitiesis
by far the most difficult part of the
decision-maker's job. This paper has
little to say about these problems. It
deals largely with the first step: the problem of setting up cri teria for choosing
among strategies on the basis of a filledin payout matrix.
A hierarchy of goals and guides for
reaching these goals is involved in rational choices among strategies. This
hierarchy consists of (1) a goal; (2) a
subgoal; and (3) a criterion for choosing
among strategies to reach the subgoal,
that is, a measure that must be maximized to attain the subgoal. The goal in
rational decision-making is the maximization of some measure of value. Each
decision is made for the sake of the
difference it will make in terms of this
144
--- page 63 ---

36
H A. Lalane
CRITERIA FOR CHOICE AMONG RISKY VENTURES
145
objective. The decision-maker is confronted with a payout matrix expressed
in terms of either a subjective utility
measure such as utiles or an objective
measure such as money or bushels of
wheat. He wishes to choose the strategy
that will give him the maximum payout.
This is his goal. When some one strategy
gives a higher payout than any other
strategy in all relevant future occurrences, the goal itself enables the decision-maker to choose among strategies.
He merely chooses the dominant strategy.
When there is no strategy superior to
all the rest in all possible future occurrences, the decision-maker needs some
other guide for making decisions, since
the goal itself does not enable him to
make his choice. This guide is here called
the "subgoal." The need for a subgoal
exists because the outcome of specific
strategies is subject to probabilistic uncertainty. In utility theory the payout
matrix is expressed in terms of some
measure of subjective utility, say, utiles.
Choice of the strategy that will give the
maximum payout in utiles is the goal,
and choice of the strategy with the maximum expected utility2 is taken as the
subgoal. Given a completely filled-in
matrix, this subgoal can surely be
reached. Whether or not the goal is
reached depends on future occurrences,
but, in any event, the subgoal of maximization of the expected value of the payouts expressed in utiles is logically related to the goal of maximization of the
forthcoming payout also expressed in
utiles.
In this paper a second subgoal is proposed for use when the choice is repetitious and has cumulative effects and
2 The expected utility of a strategy is computed
by mUltiplying all possible payouts expressed in
u tiles by their respective probabilities and then
slimming the products.
when the goal is maximization of wealth
at the end of a large number of choices.
Under these conditions the choice of the
strategy that has a greater probability
(PI) of leading to as much or more
wealth than any other significantly different strategy at the end of a large
number of choices also is a logical subgoal. The P' subgoal is not as general as
the maximum expected utility subgoal.
For example, it would not apply to
unique choices. When a man is faced with
a once-in-a-lifetime choice of risking his
whole fortune and his life on a venture
that will produce great rewards if successful, it does not help him to know that
he is almost certain to be ruined if he
takes such a risk often enough. The P'
subgoal is not logically related to the
goal in this case. 3 Such a man, however,
could set up a payout matrix expressed
in utiles and decide which course of
action maximized his expected utility.
Here the maximum expected utility subgoal is logically related to the goal even
though the P' subgoal is not. The P' subgoal is less general bu t would seem to be
more operational than the expected utility subgoal because of the difficulty of
constructing a payout matrix expressed
in terms of utiles, especially if the decision involves a firm or group of people.
The P' subgoal would seem to be particularly applicable to many business
3 For certain utility functions and for certain repeated gambles, no amount of repetition justifies the
rule that the gamble which is almost sure to bring
the greatest wealth is the preferable one. For example, the pI subgoal is not appropriate for a
decision-maker for whom the possibility of great
gain, however small and diminishing, is more important than maximization of the probability of as
much or more wealth than can be obtained by any
other strategy in the long run. Such a decision·
maker may adopt a course of action that is almost
certain to result in less wealth in the long run.
Whether or not his utility function is compatihle
with the specified goal of maximum long-run wealth
is not at issue here.
--- page 64 ---

Criteria/or Choice among Risky Ventures
37
146
HENRY ALLEN LATANE
decisions such as those involved in portfolio management. Wealth-holders have
the option of holding their wealth in
many different combinations of stocks,
bonds, and cash. The allocation of
wealth among these types of assets involves a series of choices extending over
time. The fact that these choices are
repetitive in nature with cumulative effects may be used as the key factor in
defining a goal, a subgoal, and a criterion for choosing among portfolios.
The problem of choice among portfolios may be stated in terms of the payout matrix in Table 1. In this table Pi
TABLE 1
PAYOUT MATRIX FOR VARYING PORTFOLIOS
PORTFOLIO
RELEVANT FUTURE O CCURRENCES
1, . .. ,j, .. . , k
1. . . . . . . . . . . . . . . .
a iI, . .. , au, ... , al ~:
'to . • . • • • • . • • . • • • • . • .
ail, ... , Qij, .• . , ai/~
t.
Probability of occurrence . . .. . .. . . .
PI, ... , Pi> . .. , PI,
represents the probability of the jth occurrence, with 'J;Pi = 1, and a ii represents the return from the ith portfolio
with i = 1, .. . , t, if the jth occurrence
takes place, withj = 1, ... , k. A return
is the payout, including return of principal, per dollar of portfolio value per inves tmen t period (here called "year").
Returns cannot be negative, so that
ai ~ O. The portfolio manager is faced
with such a payout matrix for n years
and wants to choose in a rational manner
one portfolio from all available portfolios in each of the n years. 4
The goal of portfolio management is
taken to be to select a portfolio so as to
maximize wealth at the end of a period
of years, assuming reinvestment of all returns.5 Let Wi be the final value of $1.00
placed in portfolio i if returns are reinvested n times. Then the goal of portfolio management is taken to be to
select the optimum portfolio so that
W:P1 ~ Wi, with i = 1, ... ,t. This
goal cannot be used as a basis for choice
among portfolios, since which portfolio
will have the maximum Wn depends on
future occurrences.
The sub goal proposed here is the
choice of the portfolio that has a greater
probability (PI) of being as valuable or
more valuable than any other significantly different portfolio at the end of n
years, n being large. It is shown below
4 The idea of maximizing wealth at the end of a
large number of separate decisions based on the same
payout matriK may appear unrealistic, but portfolio
managers are continually being faced with choices
having cumulative effects and involving approximately the same payouts and probabilities time after
time. For example, year after year a portfolio manager may have probability beliefs such as; "I look
for conditions in the next ten years to be very similar
to those prevailing in 1926 through 1935. Bonds will
yield about 4 per cent per annum during the whole
period. Some day we are going to have a boom and
a bust in the stock market, but I do not know which
is going to come first." Choosing one portfolio to
hold in each of the n years is not the same as choosing one portfolio at the beginning of the period to
hold throughout the n years. For example, if the
probability beliefs at the beginning of one year are
such that the maximum pi allocation of the portfolio is 40 per cent in bonds and 60 per cent in stock
and if these beliefs remain the same at the beginning
of the next year, then the maximum pi allocation
again will be 40 per cent in bonds and 60 per cent in
stock at the beginning of the second year. If the relative prices of stocks and bonds have changed between the two dates, it will be necessary for the
portfolio manager to make some sales and purchases
in his portfolio to bring it into line with the desired
proportions even if these proportions themselves
have not changed.
• Few wealth-holders reinvest all returns, so the
problem of maximizing wealth assuming no withdrawals is somethat unrealistic. However, this restriction can be modified. If withdrawals per unit of
time are a fixed proportion of wealth (considered as
interest, for example), they will not affect proper
maximizing action. \Vhatever would maKimize
wealth, assuming no withdrawals, 1I'0uld maximize
wealth, assuming proportionate withdrawals.
--- page 65 ---

38
H A. Lalane
CRITERIA FOR CHOICE AMONG RISKY VENTURES
147
that the portfolio having a probability
distribution of returns with the highest
geometric mean, G, also has the greatest
P'.
The central fact of this paper is a
simple one: If the value of an asset, say,
portfolio i, priced initially at $1.00 is believed to change after a year to, alternatively, ail or ai2, ... ,or aik, with respective probabilities PI, pz, . .. , Pk,
and if the proceeds are reinvested n
times, then the final value of the investment, Wi, "converges in probability" to
Gi = aft • aft' • • • afk".
The
probability that the absolute difference between W7 and G7 is smaller than any
preassigned positive number will approach 1 as n increases indefini tely. In
other words, the final return from $1 .00
invested in portfolio i, assuming reinvestment of all annual returns for n years
will converge in probability on Gi, the
nth power of the geometric mean of the
probability distribution of annual returns from that portfolio. This relationship is intuitively obvious, since the ail
return will "tend" to occur npl times, the
aii return will tend to occur npi times,
and so forth, if n is large. It can be
proved rigorously by use of the law of
large numbers applied to the logarithms
of the annual returns.
Let nj be the number of occurrences of
the jth relevant future occurrence, with
27.nj = n, with j = 1, ... ,k, then nj
n i: pj and njn log aij i: Pi log aij as
n ~ aJ. But log Wi = 27.njn log aij,
with j = 1, ... , k and log Gi = 27.pj log
aij, so log Wi i~ log Gi and Wi I~ Gi as
n ~ aJ.6 It follows from this that, if
Gi > Gj , then the probability, pi, that
Wi > WJ at the end of n years approaches 1 as n increases indefinitely.
The portfolio with the highest G is almost certain to be more valuable than
any other significantly different portfolio in the long run. For this reason G is
accepted here as a rational criterion for
choice among portfolios.
SUB GOALS AND SUBJECTIVE UTIJ.ITY
Rational choice among strategies is
the ancient problem of the gambler who
has the option to choose among bets.
Classical writers on probability theory
recommended that problems of this kind
be solved by first computing the expected winnings (possibly negative) for
each available bet and then choosing the
bet with the highest mathematical expectation of winning. Since there was no
reason to assume that, of two persons
encountering
identical risks,
either
should expect to have his desires more
closely fulfilled, the classical writers
thought that no characteristic of the
risk-takers themselves ought to be taken
into consideration; only those matters'
should be weighed carefully that pertain
to the terms of the risk. 7 In 1738 Daniel
Bernoulli in four short paragraphs demonstrated that the use of the mathematical expectation of winnings did not
always apply and proposed instead that
gamblers should evaluate bets on the
basis of the mathematical expectation of
the utilities of winnings. ~
In terms of subgoals as defined in this
study, Bernoulli showed that use of the
6 The asymptotic quality of G is used in information theory as developed by Dr. Claude Shannon
and was applied to a gambling situation by John
Kelly in "A New Interpretation of Information
Rate," Bell System Technical Journal, August, 1956,
pp. 917-26. See also R. Bellman and R. Kalaba,
"Dynamic Programming and Statistical Communication Theory," Proceedings of the NlLtional Academy
of Science, XLIII (1957), 749-51. I had no knowledge of this work when I first proposed the pi subgoal at a Cowles Foundation Seminar in February,
1956.
7 See Daniel Bernoulli, "Exposition of a New
Theory on the Measurement of Risk," trans. Louise
Sommer, Econometrica, XXII (January, 1954) , 23.
"[bid., p. 24.
--- page 66 ---

Criteria/or Choice among Risky Ventures
39
148
HENRY ALLEN LATANl!:
expected-value subgoal did not always
lead to choices that seemed rational to
him and proposed instead the use of the
expected-utility subgoal. He used the following example:
Somehow a very poor fellow obtains a lottery
ticket that will yield with equal probability
either nothing or twenty thousand ducats. Will
this man evaluate his chances of winning at ten
thousand ducats? Would he not be ill-advised to
sell this lottery ticket for nine thousand
ducats? To me it seems that the answer is in the
negative. On the other hand I am inclined to
believe that a rich man would be ill-advised to
refuse to buy the lottery ticket for nine thousand ducats. If I am not wrong then it seems
clear that all men cannot use the same rule to
evaluate the gamble. 9
Bernoulli's example is somewhat aside
from the daily business of living, but,
when stripped of its gambling wrappings
and expressed in terms of payouts and
returns, it is seen to represent a major
segment of economic decision-making.
The hypothetical market price of the
ticket, which has an equal probability of
paying 20,000 ducats or nothing, is 9,000
ducats. Both the poor man and the rich
man have the option either to hold the
lottery ticket or to hold 9,000 ducats.
Possible payouts range from 2.22 per
ducat risked to 0. Payouts with ranges
such as this-indeed, much greater
rangesare ordinary economic occurrences. The magnitude of the choice
faced by the rich man is well within the
range of ordinary business decisions, and
the "poor man" today is continually
faced with implicit or explicit decisions as
serious as that faced by Bernoulli's
lottery-ticket owner. He must decide
whether to move to a new job, buy a new
home, sign a second mortgage. He is continually offered the opportunity to undertake such risky ventures as purchasing his own truck, opening a restaurant,
9 Ibid.
buying some uranium stock, some oil
stock, or some investment shares. Some
of these options may be highly advantageous, and he must choose some
one course of action in each case. The effects of these choices are cumulative;
that is, the decision-maker never comes
back to exactly the same position he
occupied before making his choice. The
major difference between Bernoulli's
problem and other choices among courses
of action is that the ticket-holder's
choice is dearly defined, while the other
opportunities are usually ignored, or the
choices are muddled.
TABLE 2
PAYOUT MATRIX OF GAINS AND LOSSES
FUTURE O CCUR.RENCE
Ticket
Ticket
CRI'
STRA.TEGY
Wins
Loses
TElUON A
a) Poor man:
Hold ticket . . .
20
0
10
Sell ticket ... .
9
9
9
b) Rich man:
Buy ticket. ..
11
-
9
1
Not buy ticket
0
0
0
Probability of occurrence .. .. .. . .
0.5
0.5
Thus Bernoulli's example is representative of a wide class of choices. The
decision-maker is being faced continually
with such choices, and the outcome of
each decision affects his entire future. In
the following discussion this example is
stated in payout matrices constructed to
illustrate choices based on <.a) classical
mathematical expectation (the expected
value subgoal) ; (b) Bernoulli's subjective
utility (the expected-utility subgoal);
and \c) the maximum chance (Pi) subgoal.
Table 2 shows the classical approach
to choosing among risky ventures. The
payout matrix, expressed in terms of
thousands of ducats, shows the probability of the lottery ticket paying off or not
and the net payout to the poor man and
to the rich man for each of two courses of
--- page 67 ---

40
H A. Lalane
CRITERIA FOR CHOICE AMONG RISKY VENTURES
149
action. The classical writers would calculate the mathematical expectation, A, of
the net payouts and choose that strategy
which maximizes A. In this case they
would recommend that the rich man buy
the ticket for 9,000 ducats and that the
poor man refuse to sell it at this price.
The mathematical expectation (that
is, the arithmetic mean) of the probability distribution of payouts is, indeed, a
good criterion when there are large
numbers of independent trials. Even
decision-makers who make repeated
choices with cumulative effects (for example, the operators of roulette wheels
and insurance companies) are rightly
interested in this average when each risk
is small in relation to total wealth. There
is little or no conflict under these conditions between the use of the arithmetic
mean as a criterion and the use of the
geometric mean of the probability distribution of payouts per dollar of wealth
as a criterion./O When a decision-maker
can surely bet the same small amount on
a large number of independent trials, he
can maximize the expected value of his
gain, and also the likelihood of having
more gain than can be obtained by any
other plan, by choosing that set of bets
which gives him the greatest mathematically expected payout. For example,
if Bernoulli's poor man had found 10,000
tickets involving 10,000 independent
drawings, each with a payout equally
likely to be 2 ducats or nothing, he clearly would be unwise to sell his block of
tickets for 9,000 ducats. His winnings on
10,000 different trials would be almost
10 When a gambler who has the choice of betting
or not betting bets all his wealth on the toss of a
fair coin with a payout of $3.00 per $1.00 bet if
heads occur and nothing per $1.00 bet if tails occur,
he is maximizing the expected value of the payout
but not G. When he can bet only 1 per cent of his
wealth, however, he will maximize both A and G by
betting.
certainly very close to 10,000 ducats, the
mathematical expectation of the value of
the set of tickets, and the advice of the
classical writers would be sound.
Bernoulli used the lottery-ticket example to show that the expected values of
the payouts are not good guides in making choices involving large risks. He proposed instead that the expected value of
the utilities of the payouts be used as a
criterion. He would fill in the payout
matrix in Table 2 not with the money
value of the gains and losses but with
their utilities and then would use the
mathematical expectation of these utilities as his criterion.
Whether or not particular payout
matrices expressed in terms of subjective
utility are realistic is not a problem here.
But Bernoulli's procedure is very much
at issue. He defines the "mean utility"
of a course of action as the mathematical
expectation of the probability distribution of the possible utilities from that
course of action. He then states, with no
discussion, that this mean utility can be
used as a basis for valuing risks, that is,
as a basis for choosing among courses of
action. In other words, he explains why
he expresses his profits (or losses) in
terms of subjective utility, but he does
not give any justification for maximizing
the mathematical expectation of these
utilities. Bernoulli's use of subjective
utility has had wide recognition, and his
use of mathematical expectation also has
been widely adopted with little or no
discussion.ll
11 Mathematical expectation now is used as a
basis for defining utility. The present emphasis on
the axiomatic approach to utility is largely derived
from John von Neumann and Oskar Morgenstern,
Theory of Games and Economic Behavior (rev. cd.;
Princeton, N.J. : Princeton University Press, 1935).
They say : "We have practically defined numerical
utility as being that thing for which the calculus of
mathematical expectations is legitimate" (p. 28).
--- page 68 ---

Criteria/or Choice among Risky Ventures
41
150
HENRY ALLEN LATANf:
Bernoulli's problem can also be solved
by the use of the maximum-chance (P')
subgoal. Table 3 shows the payout
matrix of returns (that is, payouts, including return of principal, per dollar of
wealth) for the poor man, who is assumed to have a wealth of 1,000 ducats
aside from his lottery ticket, and for the
rich man, who is assumed to have a
wealth of 100,000 ducats. The arithmetic
mean, A, of the probability distribution
of returns is higher for the poor man
when he holds the ticket and for the rich
man when he buys the ticket. The geo-
TABLE 3
PAYOUT MATRIX OF RETURNS
FUTURE OCCURRENCE
Ticket
Ticket
CRITERWN
S TRATEGY
Wins
Loses
A
G
a) Poor man:
Hold ticket.
2. 1
0 . 1
1.1
0.46
Sell ticket ..
1.0
1.0
1.0
1.0
b) Rich man:
Buy ticket.
1.11
0.91
1.01
1.005
Not buy
ticket ..
1.00
1.00
1.00
1.00
Probability of occurrence .. .. . . 0 .5
0 .5
metric mean, G, of returns for the poor
man is higher when the ticket is sold,
however, and G for the rich man is higher
when he buys the ticket.
Over a long enough period of time
many economic choices involving returns
of the same order of magnitude repeat
themselves. Bernoulli's poor man may
never find another lottery ticket, but he
probably will have many options among
courses of action with as wide, or wider,
a range of returns. It is assumed here
that both the rich man and the poor man
will have many opportunities to risk the
same proportions of their respective
fortunes on approximately the same
terms and that both men prefer more
wealth to less wealth, everything else
being equal. If these assumptions are
valid, the maximization of P', the probability of having more wealth at the end
of a long series of such choices than can
be obtained by any other specified
course of action, is a rational subgoal,
and G is a rational criterion. The use of
the maximum-chance subgoal results in
courses of action for both the rich man
and the poor man which seemed rational
to Bernoulli.
The decision-maker who is interested
in maximizing his wealth at the end of a
long series of choices should ask himself
how he would come out in the long run if
he made the same choice on the same
terms over and over again. It is not
necessary for him to ask himself what his
individual subjective utility of winning
is. This is not to say that other goals,
rather than the goal of maximum wealth
at the end of a long series of choices, are
irrational. Indeed, the use of subgoals
based on the goal of maximum wealth
often may be irrational. For example, the
man who desperately needs $10.00 to
escape a jail sentence and who has only
$1.00 may well be justified in taking a
gamble to get his money, even though
this gamble would not stand the maximum-chance subgoal test. Even under
these conditions, however, it would be
useful for the man to know that he
should not often act in such a manner, if
he wants to build up his fortune so as to
avoid similar predicaments in the future.
In his paper Bernoulli uses the expected utilities of the payouts as his
criterion. He then reaches the conclusion
that the utility resulting from any small
increase in wealth usually is inversely
proportional to the quantity of goods
previously possessed.12 Under these conditions the utilities of the returns vary as
their logarithms, and the geometric
mean, G, of the probability distributions
12 This is generally crediten with being the first
use of a utili ty function.
--- page 69 ---

42
H A. Lalane
CRITERIA FOR CHOICE AMONG RISKY VENTURES
151
of returns can be used as a criterion instead of expected utility. The arithmetic
mean of the logarithms (utilities) of returns is maximized when G is maximized. 13
Bernoulli gives a number of applications of his formula to gambling and to
insurance. In each instance he is able to
give a specific answer. He says that
everyone who bets any part of his fortune
on a mathematically fair game of chance
is acting irrationally, and he then determines what odds a gambler with a
specified fortune must obtain to break
even in the long run. Most of his problems still are interesting in their own
right, and many have a bearing on proper
portfolio management. For instance, he
demonstrates with numerical examples
the advantages of diversification among
equally risky ventures and between
risky and safe assets.
Bernoulli's approach to the valuation
of risky ventures is not contradictory to
the maximum-chance (P') approach.
Not only do the two approaches lead to
the same conclusion when they both can
be applied but they tend to support each
other. Wealth-holders may be divided
into two groups. The first group contains
those to whom each risk is a unique event
either because they do not expect it to
recur or because they keep its effects entirely separate from the results of other
risks. For example, the man who each
year sets aside a small sum to bet on the
races during his vacation, with the intention of "living it up" if he wins and
writing it off to experience if he loses,
presumably is not actuated by long-run
profit-maximizing motives. The effects of
,3 As pointed out to me by Professor L. J. Savage
(in correspondence), not only is the maximization of
G the rule for maximum expected utility in connection with Bernoulli's function but (insofar as cerlain
approximations are permissible) this same rule is approximately valid for all utility functions.
each risk are kept separate. AnaJysis
based on maximum chance has nothing
to offer this first class of wealth-holders.
The choice between profit and safety or
expected return and variance is a matter
of subjective utility. Bernoulli's assumption that the satisfaction derived from a
small gain tends to vary in inverse proportion to the initial wealth mayor may
not be a shrewd guess.
The second class of wealth-holders includes those who expect to be faced repeatedly with risks of the same general
type and magnitude. This group includes those making most business and
portfolio decisions and hence is of great
importance. It includes, specifically, all
those who want to maximize the value of
their portfolio at the end of n years,
assuming reinvestment of all returns.
Here there is a definite rule for choosing
between risk and return, the P' subgoal,
based on maximum-chance principles.
This class may be subdivided further
into (a) those who undertake only one
risky venture at a time and (b) those who
are able to diversify their risky ventures.
Because so many economic phenomena,
including yields on stocks, tend to fluctuate together over time, diversification
among risky ventures cannot go as far
toward eliminating risk as otherwise
would be the case. Final choice among
efficient portfolios for both groups, (a)
and (b), is based on maximization of G,
not because this maximizes subjective
utility, but because it maximizes P'.
Bernoulli states that the wealthholder should ask himself whether the
added satisfaction associated with the
expected gain justifies undertaking the
risky venture. He bases an exact rule of
behavior on his assumption as to how the
added satisfaction varies with the size of
the potential gain or loss in relation to
the size of the portfolio. The rule mayor
--- page 70 ---

Criteria/or Choice among Risky Ventures
43
152
HENRY ALLEN LATANE
may not be empirically useful, but it is
grounded on rather shaky evidence about
the exact shape of the utility function.
According to maximum-chance analysis,
the wealth-holder or portfolio manager
should ask himself how he can maximize
his chances of getting as good or better
return than can be obtained with any
other specified plan, assuming that he
risks the same proportion of his portfolio
on the same terms over and over again. It
turns out that the formula which enables
the portfolio manager to answer the
maximum-chance question is the same as
that developed by Bernoulli on grounds
of subjective utility.
In conclusion Bernoulli says:
Though a person who is fairly judicious by
natural instinct might have realized and spontaneously applied much of what I have here
explained, hardly anyone believed it possible to
define these problems with the precision we
have employed in our examples. Since all of our
propositions harmonize perfectly with experience it would be wrong to neglect them as
abstractions
resting
upon
precarious
hypotheses.14
Professor Stigler, in a review article,15
gives considerable space to Bernoulli's
hypothesis about the slope of the wealthholder's utility function, even though the
major emphasis of the article is on utility
not affected by probability. He mentions
that Laplace and Marshall, among
others, have accepted the law as a
realistic guide. He also points out the
similarity of Bernoulli's law to the
Weber-Fechner psychological hypothesis
that the just noticeable increment to any
stimulus is proportional to the stimulus.
Stigler says: "Bernoulli was right in
seeking the explanationl6 in utility and
u Op. cit., p. 31.
i6 George J. Stigler, "The Development of Utility Theory ," Journal of Political &onomy, L VIn
(1950), 373- 77.
he was wrong only in making a special
assumption with respect to the slope of
the utility curve for which there was no
evidence and which he submitted to no
tests. "17
More recently Savage in a section on
"Historical and Critical Comments on
Utility" had this to say:
Bernoulli went further than the law of
diminishing marginal utility and suggested that
the slope of utility as a function of wealth
might, at least as a rule of thumb, be supposed,
not only to decrease with, but to be inversely
proportional to, the cash value of wealth. To
this day, no other function has been suggested
as a better prototype for Everyman's utility
function .... Though it might be a reasonable
approximation to a person's utility in a moderate range of wealth, it cannot be taken seriously
over extreme ranges.18
INDIVIDUAL RISK PREFERENCE
As indicated in the previous section,
Bernoulli took the following steps to develop his utility function and to justify
diversification among risky ventures and
between risk assets and safe assets. (1)
He showed-subject to the implicit assumption about subgoals previously discussed~that the value of a risky venture
to the individual wealth-holder is not the
arithmetic mean of the probability distribution of returns (the mathematical
expectation of returns) but may be taken
to be the arithmetic mean of the probability distribution of the utilities of the
returns. (2) He stated that, in the absence of the unusual, the gain in utility
,. Bernoulli is explaining the reason for the
limited value of the game involved in the St. Petersburg paradox. This game is a type of risky venture
with an infinitely large mathematically expected
value but with an extremely small probability of
winning.
11 Stigler, op. cit., p. 375.
13 Leonard J. Savage, The Foundations of Statistics (New York: John Wiley & Sons, 1954), p. 94.
--- page 71 ---

44
H A. Lalane
CRITERIA FOR CHOICE AMONG RISKY VENTURES
153
resulting from any small increase in
wealth may be assumed to be inversely
proportional to the quantity of goods
previously possessed. (3) He developed a
formula for calculating the utility of a
risk asset to the individual wealth-holder
using as a criterion the utility function
developed in step 2. According to Bernoulli, the subjective utility of the
wealth-holder's assets, including the
risky venture, is measured by the geometric mean, G, of the probability distribution of payouts from such assets. (4)
Using this formula, he was able to calculate exactly the utility of the wealthholder's assets, including the risky venture, and to show that diversification
among risky ventures increases the
utility.19
Bernoulli's step 2 may be a reasonable
assumption about utility,2° but it is subject to so many qualifications and exceptions (it does not explain gambling, for
example) that it has not been accepted
as a suitable basis for erecting the superstructure of steps 3 and 4. The valuation
of risky ventures has been left to individual risk preference without any criterion for deciding what this preference
is likely to be. For example, Makower
and Marschak present a hypothetical
table in which an asset's marginal contribution is determined by adding together its contribution to "lucrativity"
and safety measured in "lucrativity
19 Bernoulli, op. cit., pp. 24, 25, 28, 30.
20 Cf. Alfred Marshall, Principles of Economics
(8th ed.; New York: Macmillan Co., 1950), p. 135.
Marshall says: "In accordance with a suggestion
made by Daniel Bernoulli, we may regard the satisfaction which a person derives from his income as
commencing when he has enough to support life,
and afterwards as increasing by equal amounts with
every equal successive percentage that is added to
his income; and vice versa for loss of income."
See also Savage's comment quoted previously.
units" determined by the safety preference rate for a single individual.~l These
individual safety preference rates, in
turn, are a matter of taste and must be
accepted as given. Friedman and Savage
build on Bernoulli's step 1 but modify
step 2 by developing a doubly inflected
curve comparing utility with income.22
Markowitz begins his analysis of portfolio selection by pointing out that "the
portfolio with the maximum expected return is not necessarily the one with the
minimum variance. There is a rate at
which the investor can gain expected return by taking on variance, or reduce
variance by giving up expected return.'m
He assumes that the investor considers,
or should consider, expected return a desirable thing and variance of return an
undesirable thing, and he defines an efficient portfolio as a portfolio with
minimum variance for a given expected
return or more and a maximum expected
return for a given variance or less. He
develops a method for selecting efficient
portfolios from the set of all possible
portfolios but does not give any basis for
choice among the efficient portfolios except the individual's safety preference
rate.
THE NEED FOR AN OBJECTIVE
CRITERION
The difficulty of evaluating subjective
risk preference and the need of an objective criterion are well indicated in the
21 Helen Makower and Jacob Marschak, "Assets,
Prices and Marketing Theory," Economica, V
(1938), 261-88. Reprinted in American Economic
Association, Readings in Price Theory (Chicago:
Richard D. Irwin, Inc., 1952), pp. 301-2.
22 Milton Friedman and L. J. Savage, "The Utility Analysis of Choices Involving Risk," Journal of
Political Economy, LVI (1948), 279-304.
2> Harry Markowitz, "Portfolio Selection," Journal of Finance, VII (March, 1952), 79.
--- page 72 ---

Criteria/or Choice among Risky Ventures
45
154
HENRY ALLEN LATANE
following quotation from a recent journal
article dealing with selection of an optimum combination of crops for a farmer:
The introduction of risk into an economic
model of a firm and consequently into a linear
programming model of a firm has been accomplished by describing risky outcomes as probability distributions and choosing from among
alternate possible distributions by the expected
utility hypothesis.
Two basic weaknesses have appeared in
applying this method of incorporating risk. One
difficulty arises in choosing a value for the
constant a, which in this case is some sort of
risk aversion indicator, and is, to some degree,
governed by the personal characteristics of the
entrepreneur. A large value for a indicates that
the entrepreneur places a great weight on the
variance as a deciding factor and is consequently highly averse to risk, and vice versa. The
estimation of such a constant to be used in a
model is thus quite important; the wrong
choice will invalidate any results obtained. The
derivation of this constant is a delicate task
beyond the scope of this paper.24
A major advantage of the criterion for
choice among risky ventures developed
in this paper is that it avoids the
necessity for direct subjective determination of such factors as Marschak's
"lucrativity units" or Freund's "risk
aversion indicator." As Roy remarks, "A
man who seeks advice about his actions
will not be grateful for the suggestion
that he maximize expected utility."26
The criteria for choice between risk
and safety in portfolio management can
be illustrated by assuming that a gambler has the choice of holding his money
in cash or of betting on a gambling device which, with equal probability, will
return R-s on loss occasions and R+s
on gain occasions with an expected re-
.. Rudolph J. Freund, "The Introduction of Risk
into a Programming Model," Econometrica, XXIV
(July, 1956),253-63.
2. A. D. Roy, "Safety First and the Holding of
Assets," Econometrica XX (1952),433.
turn of R per dollar played. The gambler's portfolio at any time consists of
the proportion of his wealth held in cash
plus the proportion bet on the gambling
device. When the gambler bets none of
his wealth, the expected return from his
portfolio is 1, and the standard deviation
of returns is O. As the proportion bet increases, both the expected portfolio return and the standard deviation of returns increase. When he bets all his
wealth, the expected portfolio return is
R, and the expected standard deviation
of returns is s. As long as R is greater
than 1, and R - s is less than 1, all possible combinations of the two assets in
this range are efficient portfolios in that
anyone of the' combinations gives the
maximum possible expected return for
some standard deviation or variance and
the minimum standard deviation or variance for some expected return. Neither
Marschak nor Friedman and Savage nor
Markowitz would be able to help the
gambler in choosing among these efficient
portfolios beyond telling him that he
should gamble heavily if he has a high
preference for risk and should be very
conservati ve in his betting if he has a
high risk-aversion factor. In this paper
an attempt is made to give the gambler
(and wealth-holders, in general) an objective criterion for making this choice.
The wealth-holder who adopts the
maximum-chance (PI) subgoal can reach
this subgoal by using the geometric
mean, G, of the probability distribution of
returns as his criterion and choose the
strategy that has the probability distribution of returns with the highest G .
Bernoulli also has shown that choice of
that risky venture with the highest G is a
rational choice (1) if maximization of the
mathematical expectation of the utilities
--- page 73 ---

46
H A. Lalane
CRITERIA FOR CHOICE AMONG RISKY VENTURES
155
of the payouts is a rational subgoal and
(2) if the utility of a small gain or loss
varies inversely with the amount of
wealth already possessed.
Most economists recognize that the
mathematical expectation and the variance of the probability distribution of
returns and the chance of ruin are important to the wealth-holder-but they
leave it to individual risk preference to
balance one factor against the others.
Since G depends on both the mathematical expectation and the variance of
the probability distribution of returns,
when G is maximized, there is no chance
of ruin if the wealth-holder's probability
beliefs are correct. Consequently, maximization of G falls within the generally
accepted range of rational behavior. This
is not to say that G is the only rational
criterion for choice among strategies; it
is to say, however, that it is a useful
criterion in dealing with a broad range of
problems.
--- page 74 ---

Proc. a/the 4th Berkeley Symp. on Math. Statistics and Probability, 1, 63--68 (1961)
5
OPTIMAL GAMBLING SYSTEMS FOR
FAVORABLE GAMES
L. BREIMAN
UNIVERSITY OF CALIFORNIA, LOS ANGELES
1. Introduction
47
Assume that we are hardened and unscrupulous types with an infinitely
wealthy friend. We induce him to match any bet we wish to make on the event
that a coin biased in our favor will turn up heads. That is, at every toss we have
probability p > 1/2 of doubling the amount of our bet. If we are clever, as well
as unscrupulous, we soon begin to worry about how much of our available fortune to bet at every toSS. Betting everything we have on heads on every to~s
williead to almost certain bankruptcy. On the other hand, if we bet a small,
but fixed, fraction (we assume throughout that money is infinitely divisible) of
our available fortune at every toss, then the law of large numbers informs us
that our fortune converges almost surely to plus infinity. What to do?
More generally, let X be a random variable taking values in the set
I = {I, ... , s} such that P{X = i} = p; and let there be a class e of subsets
Ai of I, where e = {AI, ... , A r}, with Ui Ai = I, together with positive
numbers (01, •.• , Or). We play this game by betting amounts f31, •.. , f3r on the
events {X E Aj} and if the event {X = i} is realized, we receive back the
amount L;EA; f310j where the sum is over allJ' such that i E A j • We may assume
that our entire fortune is distributed at every play over the betting sets e,
because the possibility of holding part of our fortune in reserve is realized by
taking AI, say, such that Al = I, and 01 = 1. Let 8" be the fortune after n plays;
we say that the game is favorable if there is a gambling strategy such that almost
surely 8 ft -+ 00. We give in the next section a simple necessary and sufficient
condition for a game to be favorable.
How much to bet on the various alternatives in a sequence of independent
repetitions of a favorable game depends, of course, on what our goal utility is.
There are two criterions, among the many possibilities, that seem pre-eminently
reasonable. One is the minimal time requirement, that is, we fix an amount x
we wish to win and inquire after that gambling strategy which will minimize the
expected number of trials needed to win or exceed x. The other is a magnitude
condition; we fix at n the number of trials we are going to play and examine the
size of our fortune after the n plays.
This research was supported in part by the Office of Naval Research under Contract
Nonr-222(53).
65
--- page 75 ---

48
L. Breiman
66
FOURTH BERKELEY SYMPOSIUM: BREIMAN
In this work, we are especially interested in the asymptotic point of view.
We show that in the long run, from either of the two above criterions, there is
one strategy A * which is optimal. This strategy is found as that system of betting
(essentially unique) which maximizes E(log Sn). The reason for this result is
heuristically clear. Under reasonable betting systems Sn increases exponentially
and maximizing E(log Sn) maximizes the rate of growth.
In the second section we investigate the nature of A *. It is a conservative
policy which consists in betting fixed fractions of the available fortune on the
various A j • For example, in the coin-tossing game A * is: bet a fraction p -
q of
our fortune on heads at every game. It is also, in general, a policy of diversification involving the placing of bets on many of the Aj rather than the single one
with the largest expected return.
The minimal expected time property is covered in the tlt,ird section. We show}
.~
by an examination of the excess in Wald's formula, that"the desired fortune X i
becomes infinite, that the expected time under A * to amass x becomes less than ·
that under any other strategy.
Section four is involved with the magnitude problem. The content here is that
A * magnitudewise, does as well as any other strategy, and that if one picks a
policy which in the long run does not become close to A *, then we are asymptotically infinitely worse off.
Finally, in section five, we discuss the finite (nonasymptotic) case for the
coin-tossing game. We have been unsuccessful in our efforts to find a strategy
which minimizes the expected time for x fixed, but we state a conjecture which
expresses a moderate faith in the simplicity of things. It is not difficult, however,
to find a strategy which maximizes P{Sn ~ x} for fixed n, x and we state the
results with only a scant indication of proof, and then launch into a comparison
with the strategy A * for large n.
The conclusion of these investigations is that the strategy A * seems by all
reasonable standards to be asymptotically best, and that, in the finite case, it is
suboptimal in the sense of providing a uniformly good approximation to the
optimal results.
Since completing this work we have been allowed to examine the most significant manuscript of L. Dubins and L. J. Savage [1], which will soon be published. Although gambling has been associated with probability since its birth,
only quite recently has the question of gambling systems optimal with respect
to some goal utility been investigated carefully. To the beautiful and deep results
of Dubins and Savage, upon which work was commenced in 1956, must be given
priority as the first to formulate systematically and solve the problems of optimal
gambling strategies. We strongly recommend their work to every student of
probability theory.
Although our original impetus came from a different source, and although
their manuscript is almost wholly concerned with unfavorable and fair games,
there are a few small areas of overlap which I should like to point out and
acknowledge priority. Dubins and Savage did, of course, formulate the concept
--- page 76 ---

Optimal Gambling Systems for Favorable Games
49
OPTIMAL GAMBLING SYSTEMS
67
of a favorable game. For these games they considered the class of "fractionalizing
strategies," which consist in betting a fixed fraction of one's fortune at every
play, and noticed the interesting phenomenon that there was a critical fraction
such that if one bets a fixed fraction less than this critical value, then S" ~
00 a.s.
and if one bets a fixed fraction greater than this critical value, then Sn ~ 0 a.s.
In addition, our proposition 3 is an almost exact duplication of one of their
theorems. In their work, also, will be found the solution to maximizing P {Sn ~ x}
for an unfavorable game, and it is interesting to observe here the abrupt discontinuity in strategies as the game changes from unfavorable to favorable.
My original curiosity concerning favorable games dates from a paper of
J. L. Kelly, Jr. [2J in which there is an intriguing interpretation of information
theory from a gambling point of view. Finally, some of the last section, in problem and solution, is closely related to the theory of dynamic programming as
originated by R. Bellman [3].
2. The nature of A *
We introduce some notation. Let the outcome of the kth game be X k and
Rn = (Xn, ... , Xl)' Take the initial fortune So to be unity, and Sn the fortune
after n games. To specify a strategy A we specify for every n, the fractions
[Xin+l), ... ,x~n+I)J = Xn+l,bf our available fortune after the nth game, Sn, that
we will bet on alternative AI, ... , Ar in the (n + l)st game. Hence
(2.1)
Note that X
may depend on R". Denote A = (Xl, X2, ••• ). Define the random
'>1-1-1
variables V n by
(2.2)
V n = :E xJn) OJ,
Xn = i,
i1' ;EAj\
so that Sn+l = V n+ISn' Let W n = log V n, so we have
(2.3)
To define A *, consider the set of vectors};. = (AI, . .. , AI') with r nonnegative
components such that Al + ... + Xr = 1 and define a function W(X) on this
space 5 by
(2.4)
W(X) = :E pdog ( :E A;o;).
i
iEAj
The function W(};.) achieves its maximum on 5 and we denote W = maX~E(f W(};.).
PROPOSITION 1.
Let };.(1), };.(2) be in 5 such that W = W(};.(L»
= W(};.(2» , then
for all i, we have LtEAjAJI) OJ = LtEAj xj2) OJ.
-· PRC)OF.
Let a, {3 be positive numbers SliC~ that a + (3 = 1.
Then if
X = a};.(l) + (3};.(2), we have W(X) ;;;; W. But by tKe;J~ncavity of log
(2.5)
W(};.) ~ aW(};.(l) + (3W(};.(2»)
with equality if and only if the conclusion of the proposition holds.
--- page 77 ---

50
L. Breiman
68
FOURTH BERKELEY SYMPOSIUM: BREIMAN
Now let >:* be such that W = W(>:*) and define A * as (>:*, >:*, ... ). Although
>:* may not be unique, the random variables Wi, W~, . .. arising from ~ are by
proposition 1 uniquely defined, and form a sequence of indepelldent,--identically
distributed random variables.
Questions of uniqueness and description of >:* are complicated in the general
case. But some insight into the type of strategy we get using A * is afforded by
PROPOSITION 2.
Let the sets AI, • • . , Ar be disjoint, then no matter what the
odds OJ are, >:* is given by Xj = P{X E A j }.
The proof is a simple computation and is omitted.
From now on we restrict attention to favorable games and give the following
criterion.
PROPOSITION 3.
A game is favorable if and only if W > O.
PROOF.
We have
n
(2.6)
log S~ = l: Wt
I
If W = EW: is positive, then the strong law of large numbers yields S~ -? 00 a.s.
(Conversely, if there is a strategy A such that Sn -? 00 a.s. we use the result of
i
section 4, which says that for any strategy A, limn SnIS~ exists a.s. finite. Hence
S~ -? 00 a.s. and therefore W ~ O. Suppose W = 0, then the law of the iterated
logarithm comes to our rescue and provides a contradiction to S~ -? 00 •
3. The asymptotic time minimization problem
For any strategy A and any number x > I, define the random variable T(x) by
(3.1)
T(x) = {smallest n such that Sn ~ x},
and T*(x) the corresponding random variable using the strategy A*. That is,
T(x) is the number of plays needed under A to amass or exceed the fortune x.
This section is concerned with the proof of the following theorem.
THEOREM 1. If the random variables Wi, W;, ... are nonlattice,t then for any
strategy
(3.2)
1 .,
lim [ET(x) -
ET*(x)] = W l: (W -
EWn )
x~~
1
and there is a constant a, indepMdent of A and x such that
(3.3)
ET*(x) -
ET(x) ~ a.
Notice that the right side of (3.2) is always nonnegative and is zero only if A
is equivalent to A * in the sense that for every n, we have W n = W~. The reason
for the restriction that W: be nonlattice is f~_ .~pI>~.re.~t. But as this restriction
is on log V: rather than on V~ itself, the common games with rational values of
the odds OJ and probabilities Pi usually will be nonlattice. For instance, a little
number-theoretic juggling proves that in the coin-tossing case the countable set
of values of P for which W~ is lattice consists only of irrationals.'"
