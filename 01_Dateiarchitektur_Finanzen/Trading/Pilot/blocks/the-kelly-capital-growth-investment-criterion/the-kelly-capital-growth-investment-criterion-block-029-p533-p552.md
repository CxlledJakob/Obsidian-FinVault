# The Kelly capital growth investment criterion _ theory and -- Leonard C_ Maclean, Edward O_ Thorp, W_ T_ Ziemba, Leonard -- World Scientific Handbook -- isbn13 9781283148344 -- bec576e26410d0c695fd5b867d08ec4f -- An.pdf — pages 533–552

--- page 533 ---

504
H M Markowitz
1282
The Journal of Finance
Equation (2) implies that we have W~ ~ W? if and only if
I
I
I
I
-
~ log(l +1) > - ~ log(l +r?).
1 i - I
1 i= I
(19)
Thus (18) will hold in any play of the game in which there exists a T such that
1
I
1
I
-
~ log(l +1) > -
~ log(l +r?)
Ii_I
I i _I
for all I> T.
(20)
Or, if we let
(21 )
(20) may be written as
for I> T.
(22)
Under the present simplified assumptions
(23)
by definition of MEL. But for random variables YI,h, ... with identical distributions and with (finite) expected value p., we have
1
I
lim -
~ (y;-p.)=O
1-+00 1 i-I
except for a set of probability measure zero. In other words
1
I
lim -
~ y;=p.
1 ..... 00 1 i-I
(24)
(25)
except for a set of sequences which have (in total) zero probability of occurrence
(c.f. the strong law of large numbers in [4] or [5]). But (23) and (25) imply (as a
simple corollary of the definition of the limit of sequence) that there exists T such
that
(26)
except on a set of probability zero; hence (17) holds except on a set of measure
zero. Since
(27)
is not affected by arbitrarily changing the value of U on a set of measure zero, we
--- page 534 ---

Investment f or the Long Run: New Evidence f or an Old Rule
505
Investment for the Long Run: New Evidence for an Old Rule
1283
have
EU( WO' wf, Wt,·.·);;;. EU( Wo, W~, W~, .. . ).
(28)
Thus, given our simplifying assumption of an unchanging probability distribution of returns for a given strategy, the superiority of MEL follows quite generally.
The case in which opportunities change from period to period and, whether or
not opportunities change, strategies may select different distributions at different
times, is treated in the appendix. It is shown there that if a certain continuity
condition holds, then MEL is optimal quite generally. If this continuity condition
does not hold, however, then there can exist games for which MEL is not optimal.
In this respect the results for the unending game are similar to those for the
sequence of games with constant V(g). In the latter case we found that MEL was
asymptotically optimal for the sequence of games if V( g) was continuous, but
could fail to be so if V(g) was discontinuous. In the case of the unending game, the
theorem is not concerned with asymptotic optimality in a sequence of games, but
optimality for a single game. Given a particular continuity condition, MEL is the
optimum strategy.
V.
CONCLUSIONS
The analysis of investment for the long run in terms of the weak law of large
numbers, Breiman's strong law analysis, and the utility analysis of unending games
presented here each imply the superiority of MEL under broad assumptions for the
hypothetical investor of [I], [2], [7], [8], [9], [10]. The acceptance or rejection of a
similar conclusion for the sequence-of-games formalization depends on the definition of asymptotic optimality. For example, if constant V(g) rather than constant
U( W T) is assumed, as this writer believed plausible on a priori grounds, then the
conclusion of the asymptotic analysis is approximately the same (even in terms of
where MEL fails) as those of the unending game.
I conclude, therefore, that a portfolio analyst should not be faulted for warning
an investor against choosing E, V efficient portfolios with higher E and V but
smaller Elog(l + R), perhaps not even presenting that part of the E, V curve which
lies above the point with approximate maximum Elog(l + R), on the grounds that
such higher E, V combinations have greater variability in the short run and less
"return in the long run".
ApPENDIX
Using the notation of footnote 7, we will show that if U1ow(a) = Uhi(a) for all a
then MEL is an optimum strategy quite generally; whereas, if Uhi(a»
U10w(a) for
some ao' then a game can be constructed in which MEL is not optimum.
U1ow(a) = Uhi(a) for all a is the "continuity condition" referred to in the text.
For v= L or 0, indicating the MEL strategy or some other strategy, respectively,
we define
(29)
--- page 535 ---

506
H M Markowitz
1284
The Journal of Finance
where
(30)
is the expected value of Y~ given the events prior to time t. From this follows
E {u~1 Lj', ... , u~: d =0.
(31 )
The u~ (for a given v) are thus what Doob [4] refers to as "orthogonal" random
variables, and Feller [5] calls "completely fair" random variables. Therefore,
writing var for variance,
00
var(u~)
~
2;:::00
n-I
n
(32)
implies
converges to 0 almost always.
(33)
(In particular, (32) holds if the var(u~) are bounded.) In addition to now assuming
condition (32) we will also assume that the game is such that
lim.!. ± L/
n-+oo n i - I
exists almost always.
(34)
This is the case, for example, when the same distributions are available each time,
whether or not "the other" strategy uses a constant distribution. Since L/ ~ L?
always, we have
1 n
1 n
1 n
lim -
~ L/ = lim sup -
~ L/;;' lim sup -
~ L?
n n i- I
n
n i-Inn
i - I
always.
Thus when (32) holds we have
1 n
1 n
lim- ~ yf'>limsup- ~ Y~
almost always.
n i - I
n i - I
In general,
a = limsup.!. ~ YY
n
implies
(since there al)"ays exists another series yr ,Yi, ... such that
1 n
a=lim- ~ Yi
n i - I
and
. for all n;
(35)
(36)
(37)
--- page 536 ---

Investment/or the Long Run: New Evidence/or an Old Rule
507
Investment for the Long Run: New Evidence for an Old Rule
1285
hence
If we now add to the assumptions expressed in equations (32) and (34), the
assumption that Uhi( a) = Ulow( a) for all a, we get directly from (36) and (37) that
EUL;;'EUo.
Conversely, the following is an example in which Uhi(ao) > Ulow(aJ and which
MEL is not optimum: let Wo= 1 and suppose that for some fixed positive a we
have U(1, 0.5, 0.5(1 + a), 0.5(1 + a)2, ... ) equals
Up , (1 + a), (1 +a)2, (1 + a)3, . .. ) < U( 1,1.5,1.5(1 + a), 1.5(1 + a)2, .. . ).
With such a U-function it would be better to take a 50-50 chance of WI = 0.5 or 1.5
followed by W t =(1+a)Wt _ p t>2, rather than have W t =(1+a).Wt _ 1 with
certainty for t> 1, ....
While the above shows that MEL can fail to be optimal when Uhi(a) > Ulow(a)
for some a, recall that we can have Uhi(a) > Ulow(a) for at most a countable
number of values of a. Thus MEL is optimal in a game in which
1 n
a= lim -
~ LL
n n ~ I
i-I
has a continuous distribution, or in which a has a discrete or mixed distribution
but in which none of the points of discontinuity of the cumulative probability
distribution of a have Uhi(a) > Ulow(a).
REFERENCES
1.
Leo Breiman. "Investment Policies for Expanding Businesses Optimal in a Long Run Sense,"
Naval Research Logistics Quarterly, 7:4, 1960, pp. 647~51.
2. --. "Optimal Gambling Systems for Favorable Games," Fourth Berkeley Symposium on
Probability anfi Statistics, I, 1961, pp. 65-78.
3. Daniel Bernoulli. "Exposition of a New Theory on the Measurement of Risk," Econometrica,
XXII, January 1954, pp. 23~3 . Translated by Louise Sommer-original 1738.
4. J. L. Doob. Stochastic Processes, John Wiley and Sons, New York, 1953.
5. William Feller. An Introduction to Probabality Theory and Its Applications, Volume II, John Wiley
and Sons, New York, 1966.
6. M. B. Goldman. "A Negative Report on the 'Near Optimality' of the Max-Expected-Log Policy As
Applied to Bounded Utilities for Long Lived Programs." Journal of Financial Economics, Vol. I,
No.1, May 1974.
7. J. L. Kelly, Jr. "A New Interpretation of Information Rate," Bell System Technical Journal, pp.
917-926, 1956.
8.
H. A. Latane. "Rational Decision Making in Portfolio Management," Ph.D. dissertation, University of North Carolina, 1957.
9. --. "Criteria for Choice Among Risky Ventures," Journal of Political Economy, April 1959.
10. H. M. Markowitz. Portfolio Selection: EffiCient Diversification of Investments, John Wiley and Sons,
New York, 1959; Yale University Press, 1972.
11. --. "Investment for the Long Run," Rodney L. White Center for Financial Research Working
Paper no. 20-72 (University of Pennsylvania) 1972.
--- page 537 ---

508
H M Markowitz
1286
The Journal of Finance
12. R. C. Merton and P. A. Samuelson. "Fallacy of the Log-Normal Approximation to Optimal
Portfolio Decision-Making Over Many Periods," Journal of Financial Economics, Volume I No.
I, May 1974.
13.
Karl Menger. "Das Unsicherheitsmoment in der Wertlehre. Betrachtungen im Anschluss an das
sogenannte Petersburger Spiel," Zeitschrift fur Nationalokonomie, Vol. 5, 1934. Translated in
Essays in Mathematical Economics in Honor of Oskar Morgenstern, M. Shubik ed., Princeton
University Press, 1967.
14.
P. A. Samuelson. "Risk and Uncertainty: A Fallacy of Large Numbers," Scientia, 6th Series, 57th
year, April-May 1963.
IS. ---. "Lifetime Portfolio Selection by Dynamic Stochastic Programming," Review of Economics
and Statistics, August 1969.
16. W. E. Yong and R. M. Trent. "Geometric Mean Approximation of Individual Security and
Portfolio Performance," Journal of Financial and Quantitative AnalySiS, June 1969.
17.
John von Neuman and Oskar Morgenstern. Theory of Games and Economic Behavior, Princeton
University Press, 1944. John Wiley and Sons, 1967.
--- page 538 ---

509
36
Understanding the Kelly Criterion*
Edward O. Thorp
In January 1961, I spoke at the annual meeting of the American Mathematical Society on "Fortune's Formula: The Game of Blackjack". This announced the
discovery of favorable card counting systems for blackjack. My 1962 book Beat
the Dealer explained the detailed theory and practice. The 'optimal' way to bet in
favorable situations was an important feature. In Beat the Dealer, I called this, naturallyenough, "The Kelly gambling system", since I learned about it from the 1956
paper by John L. Kelly (Claude Shannon, who refereed the Kelly paper, brought
it to my attention in November of 1960). I have continued to use it successfully
in gambling and in investing. Since 1966, I've called it "the Kelly Criterion". The
rising tide of theory about and practical use of the Kelly Criterion by several leading money managers received further impetus from William Poundstone's readable
book about the Kelly Criterion, Fortune's Formula. (As this title came from that
of my 1961 talk, I was asked to approve the use of the title) . At a value investor's
conference held in Los Angeles in May, 2007, my son reported that 'everyone' said
they were using the Kelly Criterion.
The Kelly Criterion is simple: bet or invest so as to maximize (after each bet)
the expected growth rate of capital, which is equivalent to maximizing the expected
value of the logarithm of wealth; but the details can be mathematically subtle.
Since they're not covered in Poundstone (2005), you may wish to refer to my article, Thorp (2006), and other papers in this volume. Also some services such as
Morningstar and Motley Fool have recommended it. These sources use the rule:
"optimal Kelly bet equals edge/odds" that applies only to the very special case of a
two-valued payoff.
Hedge fund manager, Mohnish Pabrai (2007), gives examples of the use of the
Kelly Criterion for investment situations (Pabrai won the bidding for the 2008 lunch
with Warren Buffett, paying over $600,000). Consider his investment in Stewart
Enterprises (Pabrai, 2007: 108-115), his analysis gave what he believed to be a list
of worst case scenarios and payoffs over the next 24 months which I summarize
in Table 1.
The expected growth rate of capital g(f) if we bet a fraction f of our net
*Reprinted revised from two columns from the series A Mathematician on Wall Street in Wilmott
Magazine, May and September 2008. Edited by Bill Ziemba.
--- page 539 ---

510
worth is
Table 1
Stewart enterprises,
payoff within 24 months.
P robability
PI = 8.80
P2 = 0.19
P3 = 0.01
Sum = 1.00.
3
Return
RI > 100%
R2 > 0%
R 3 = - 100%
g(1) = LPi In(l + Rd)
i= l
E. O. Thorp
(1)
where In means the logarithm to the base e. When we use Table 1 to insert the Pi
values, replacing the Ri by their lower bounds gives the conservative estimate
g(1) = O.SO In(l + i) + 0.011n(1 - 1) .
(2)
Setting g'(1) = 0 and solving gives the optimal Kelly fraction 1* = 0.975 noted by
Pabrai. Not having heard of the Kelly Criterion in 2000, Pabrai only bet 10% of
his fund on Stewart. Would he have bet more, or less, if he had then known about
Kelly's Criterion? Would I have? Not necessarily. Here are some of the many
reasons why:
(1) Opportunity costs. A simplistic example illustrates the idea. Suppose
Pabrai's portfolio already had one investment which was statistically independent
of Stewart and with the same payoff probabilities. Then, by symmetry, an optimal
strategy is to invest in both equally. Call the optimal Kelly fraction for each 1*,
then 21* < 1 since 21* = 1 has a positive probability of total loss, which Kelly
always avoids, so 1* < 0.50. The same reasoning for n such investments gives
1* < l / n . Hence, we need to know the other investments currently in the portfolio,
any candidates for new investments, and their (joint) properties, in order to find
the Kelly optimal fraction for each new investment, along with possible revisions
for existing investments. Formally, we solve the nonlinear programming problem:
maximize the expected logarithm of final wealth subject to the various constraints
on the asset weights (see the papers in Section 6 of this volume for examples).
Pabrai's discussion (e.g. pp. 7S- S1) of Buffett's concentrated bets gives considerable evidence that Buffet thinks like a Kelly investor, citing Buffett bets of 25%
to 40% of his net worth on single situations. Since 1* < 1 is necessary to avoid
total loss, Buffett must be betting more than 0.25 to 0.40 of i 8 in these cases. The
opportunity cost principle suggests it must be higher, perhaps much higher. Here's
what Buffett himself says, as reported in http://undergroundvalue.blogspot.com/
200S/ 02/ notes-from-buffett-meeting-215200S..23.html, notes from a Q & A session
with business students:
--- page 540 ---

Understanding the Kelly Criterion
Emory:
With the popularity of "Fortune's Formula" and the Kelly Criterion, there seems to be a lot of debate in the value community
regarding diversification vs. concentration. I know where you side
in that discussion, but was curious if you could tell us more about
your process for position sizing or averaging down.
Buffett:
I have 2 views on diversification. If you are a professional and
have confidence, then I would advocate lots of concentration. For everyone else, if it's not your game, participate in total
diversification. So this means that professionals use Kelly and amateurs better off with index funds following the capital asset pricing
model.
If it's your game, diversification doesn't make sense. It 's crazy
to put money in your 20th choice rather than your 1st choice. If
you have LeBron James on your team, don't take him out of the
game just to make room for some else.
Charlie and I operated mostly with 5 positions. If I were
running 50, 100, 200 million, I would have 80% in 5 positions, with
25% for the largest. In 1964, I found a position I was willing to
go heavier into, up to 40%. I told investors they could pull their
money out. None did. The position was American Express after
the Salad Oil Scandal. In 1951 I put the bulk of my net worth into
GEICO. With the spread between the on-the-run versus off-the-run
30 year Treasury bonds, I would have been willing to put 75% of
my portfolio into it. There were various times I would have gone
up to 75%, even in the past few years. If it 's your game and you
really know your business, you can load up.
511
This supports the assertion in Rachel and Bill Ziemba's 2007 book, that Buffett
thinks like a Kelly investor when choosing the size of an investment. They discuss
Kelly and investment scenarios at length.
Computing 1* without considering the available alternative investments is one
of the most common oversights I've seen in the use of the Kelly Criterion. It is a
dangerous error because it generally overestimates f*.
(2) Risk tolerance. As discussed at length in Thorp (2006) , "full Kelly" is too
risky for the tastes of many, perhaps most, investors and using instead an f = c1*,
with fraction c where 0 < c < 1 or "fractional Kelly" is much more to their liking.
Full Kelly is characterized by drawdowns which are too large for the comfort of
many investors. l
ISeveral papers in Section 3 in this volume, as do the following two papers in this section, discuss
fractional Kelly strategies.
--- page 541 ---

512
E. O. Thorp
(3) The "true" scenario is worse than the supposedly conservative lower
bound estimate. Then we are inadvertently betting more than 1* and, as discussed in Thorp (2006), we get more risk and less return, a strongly suboptimal
result. Betting i = cd*, 0 < c < 1 gives some protection against this (see the
graphs in Section 3, (MacLean, Ziemba and Blazenko (1992)).
(4) Black swans. As fellow Wilmott columnist Nassim Nicholas (Taleb 2007)
has pointed out so eloquently in his bestseller The Black Swan, humans tend not to
appreciate the effect of relatively infrequent unexpected high impact events. Failing
to allow for these "black swans", scenarios often don't adequately consider the
probabilities of large losses. These large loss probabilities may substantially reduce
1* . One approach to successfully model such black swans is to use a scenario
optimization stochastic programming model. 2 For Kelly bets that simply means
that you include such extreme scenarios and their consequences in the nonlinear
programming optimization to compute the optimal asset weights. The 1* will be
reduced by these negative events.
(5) The "long run". The Kelly Criterion's superior properties are asymptotic,
appearing with increasing probability as time increases. For instance:
As time t tends to infinity the Kelly bettor's fortune will, with probability tending to 1, permanently surpass that of any bettor following an "essentially different"
strategy.
The notion of "essentially different" has confounded some well known quants so
I'll take time here to explore some of its subtleties. Consider for simplicity repeated
tosses of a favorable coin, the outcome of the nth trial is Xn where P(Xn = 1) =
p> 1/2 and P(Xn = - 1) is 1 - P = q > O. The {Xn} are independent identically
distributed random variables. The Kelly fraction is 1* = p - q = E(Xn) > O. The
Kelly strategy is to bet a fraction in = 1* at each trial n = 1,2, .... Now consider
a strategy which bets 9n, n = 1,2, ... at each trial with 9n i= 1* for some n ::; N
and 9n = 1* thereafter. The {9n} strategy differs from Kelly on at least one of the
first N trials but copies it thereafter, but it does not differ infinitely often. There
is a positive probability that {9n} is ahead of Kelly at time N, hence ahead for
all n 2: N. For example consider the sequence of the first N outcomes such that
Xn = 1 if 9n > 1* and Xn = - 1 if 9n ::; 1*. Then for this specific sequence, which
has probability 2: qN, {9n} gains more than Kelly for each n ::; N where 9n i= 1*,
hence exceeds Kelly for all n 2: N.
What if instead in this coin tossing example we require that 9n i= 1* for infinitely
many n? This question arose indirectly about 15 years ago in the newsletter Blackjack Forum when a well known anti Kellyite, John Leib, challenged a well known
blackjack expert with (approximately) this proposition bet: Leib would produce
a strategy which differed from Kelly at every trial but would (with probability as
2There you assume the possibility of an event, specifying its consequences but not what it is. See
Geyer and Ziemba (2008) for the application to the Siemens Austria Pension Fund. Correlations
change as the scenario sets move from normal conditions to volatile to crash which include the
black swans. See also Ziemba (2003) for addit ional applications of this approach.
--- page 542 ---

Understanding the Kelly Criterion
513
close to 1 as you wish), after a finite number of trials, get ahead of Kelly and stay
ahead forever. When I read the challenge I immediately saw how Leib could win
the bet.
Leib's Paradox: Assuming capital is infinitely divisible,footnoteThe infinite divisibility of capital is a minor assumption and can be dealt with as needed in
examples where there is a minimum monetary unit by choosing a sufficiently large
starting capital. then given E > 0 there is an N > 0 and a sequence {In} with
In i: f* for all n, such that P(V; < Vn for all n 2' N) > 1 - varepsilon where
Vn = I1~=1 (1 + IiXi) and V; = I1~=1 (1 + f* Xi) . Furthermore, there is a b > 1 such
that P(Vn/V; 2' b,n 2' N) > I-varepsilon and P(Vn-V; ---+ (0) > I-varepsilon.
That is, for some N there is a non Kelly sequence that beats Kelly "infinitely badly"
with probability 1 -
E for all n 2' N.
Proof.
The proof has two parts. First we want to establish the assertion for
n = N. Second we show that once we have an {In, n <:::: N} that is ahead of Kelly
at n = N, we can construct {f n i: f*, n > N} to stay ahead.
To see the second part, suppose VM > VN. Then VN 2' a + bVN for some
a > 0, b > 1. For instance, VN >'N2' C > 0 since there are only a finite number
of sequences of outcomes in the first N trials, hence, only a finite number with
VN > VN. So:
VN 2' c + VN 2' c/2 + [(c/2) + VNl = c/2 + [dMax VN + VNl 2' c/2 + (d + I)VN
where d Max VN = c/2 defines d > 0 and Max VN is over all sequences of the first
N trials such that VN > VN. Setting c/2 = a > 0 and d + 1 = b > 1 suffices. Once
we have VN 2' a + bVN we can, for bookkeeping purposes, partition our capital into
two parts: a and bVN. For n > N we bet In = f* from bVN and an additional
amount a/2n from the a part, for a total which is generally unequal to f* of our
capital. If by chance for some n the total equals f* of our total capital we simply
revise a/2n to a/3n for that n. The portion bVN will become bVN for n > Nand
the portion a will never be exhausted so we have Vn > bV; for all n > N. Hence,
since P(VN ---+ (0) = 1, we have P(Vn/VN 2' b) = 1 from which it follows that
P(Vn - VN ---+ (0) = 1.
To prove the first part, we show how to get ahead of Kelly with probability 1- E
within a finite number of trials. The idea is to begin by betting less than Kelly
by a very small amount. If the first outcome is a loss, then we have more than
Kelly and use the strategy from the proof of the second part to stay ahead. If the
first outcome is a win, we're behind Kelly and now underbet on the second trial by
enough so that a loss on the second trial will put us ahead of Kelly. We continue
this strategy until either there is a loss and we are ahead of Kelly or until even
betting 0 is not enough to surpass Kelly after a loss. Given any N, if our initial
under bet is small enough, we can continue this strategy for up to N trials. The
probability of the strategy failing is pN, 1/2 < p < 1 Hence, given E > 0, we can
--- page 543 ---

514
E. O. Thorp
choose N such that pN < E and the strategy therefore succeeds on or before trial
N with probability 1 - pN > 1 -
E.
More precisely: suppose the first n trials are wins and we have bet a fraction
1* - ai with ai > 0, i = 1, ... ,n, on the ith trial. Then:
Vn
(1 + 1* - ad' .. (1 + 1* - an)
VN
(1 + f*) " . (1 + f*)
(1 - 1 ~1f* ) ". (1 - 1 ~nf* ) > (1 - ad'" (1- an) > 1 - (a1 +". + an)
where the last inequality is proven easily by induction. Letting al + ... + an = a,
so Vn/V; > 1 - a, what betting fraction 1* - b will put us ahead of Kelly if the
next trial is a loss? A sufficient condition is
b>_a_
-l -a
provided b <::: 1* and 0 < a < 1. If a <::: 1/2 then b = 2a suffices. Proceeding
recursively, we have these conditions on the ai: choose al > O. Then an+! =
2(al +-. ·+an), n = 1, 2, ... provided all the an <::: 1/2. Letting f(x) = alx+a2x2+ ..
we get the equation
f(x) - alX = 2xf(x)(1 + x + x2 + ".)
= 2xf(x)/(1- x)
whose solution is f(x) = al {x + 2 L~=2 3n- 2xn} from which an = 2a13n-2 if
n :::;, 2. Then given E > 0 and an N such that pN < E it suffices to choose al so that
aN = 2a13N-2 <::: min(f*, 1/2).
0
Although Leib did not have the mathematical background to give such a proof
he understood the idea and indicated this sort of procedure.
So far we've seen that all sequences which differ from Kelly for only a finite
number of trials, and some sequences which differ infinitely often (even always), are
not essentially different. How can we tell, then, if a betting sequence is essentially
different than Kelly? Going to a more general setting than coin tossing, assume now
for simplicity that the payoff random variables Xi are independent and bounded
below but not necessarily identically distributed.
At this point we come to an important distinction. In financial applications, one
commonly assumes that the fi are constants that are dependent only on the current
period payoff random variable (or variables). Such "myopic strategies" might arise
for instance, by selecting a utility function and maximizing expected utility to
determine the amount to bet. However, for gambling systems, the amount depend
on previous outcomes, i.e., fn = fn(Xl ,X2, ... ,Xn-d, just as it does in the Leib
--- page 544 ---

Understanding the Kelly Criterion
515
example. As Professor Stewart Ethier pointed out, our discussion of "essentially
different" is for the constant fi case. For a more general case, including the Leib
example and many of the classical gambling systems, I recommend Ethier's 2010
book on the mathematics of gambling.
We assume R(Xi) > 0 for all Xi from which it follows that ft > 0 for all i.
As before, Vn = Il ~=1 (1 + fiXi) and V; = Il ~=1 (1 + It Xi) from which In Vn =
L: ~=1 In(1 + fiXi) and In V; = L: ~=1 In(1 + ft Xi). Note from the definition f* that
E In(l + ft Xi) 2> E In(l + fiXi) , where E denotes the expected value, with equality
if and only if ft = fi. Hence:
n
n
i=1
i=1
where ai 2> 0 and ai = 0 if and only if It = J;. This series of non-negative
terms either increases to infinity or to a positive limit M. We say {fi} is essentially
different from Ut} if and only if L:~=1 ai tends to infinity as n increases. Otherwise,
{fi} is not essentially different from {ft}. The basic idea here can be applied to
more general settings.
(6) Given a large fixed goal, e.g., to multiply your capital by 100, or 1000,
the expected time for the Kelly investor to get there tends to be least.
Is a wealth multiple of 100 or 1000 realistic? Indeed. In the 511/2 years from
1956 to mid 2007, Warren Buffett has increased his wealth to about $5 x 1010. If
he had $2.5 x 104 in 1956, that's a multiple of 2 x 106 . We know he had about
$2.5 x 107 in 1969 so his multiple over these 38 years is about 2 x 103 . Even my
own efforts, as a late starter on a much smaller scale, have multiplied capital by
more than 2 x 104 over the 41 years from 1967 to early 2007. I know many investors
and hedge fund managers who have achieved such multiples. One of the best is Jim
Simons, who recently retired from running the Renaissance Medallion Fund. His
record to 2005 is analyzed in Section 6 of this book.
The caveat here is that an investor or bettor many not choose to make, or be
able to make, enough Kelly bets for the probability to be "high enough" for these
asymptotic properties to prevail, i.e., he doesn't have enough opportunities to make
it into this "long run". Below I explore investors for which Kelly or fractional Kelly
may be a more or less appropriate approach. An important consideration will be
the investor's expected future wealth multiple.
Using Kelly Optimization at PIMCO
During a recent interview in the Wall Street Journal (March 22- 23,2008), Bill Gross
and I discussed turbulence in the markets, hedge funds, and risk management. Bill
considered the question of risk management after he read Beat the Dealer in 1966.
That summer he was off to Las Vegas to beat blackjack. Just as I did some years
earlier, he sized his bets in proportion to his advantage, following the Kelly Criterion
--- page 545 ---

516
E. O. Thorp
as described in Beat the Dealer, and ran his $200 bankroll up to $10,000 over the
summer. Bill has gone from managing risk for his tiny bankroll to managing risk for
Pacific Investment Management Company's (PIMCO) investment pool of almost $1
trillion. 3 He still applies lessons he learned from the Kelly Criterion. As Bill said:
"Here at PIMCO it doesn't matter how much you have, whether it's $200 or $1
trillion. . .. Professional blackjack is being played in this trading room from the
standpoint of risk management and that's a big part of our success" .
The Kelly Criterion applies to multi period investing and we can get some insights by comparing it with Markowitzs standard portfolio theory for single period
investing.
Compound Growth and Mean-Variance Optimality
Nobel Prize winner Harry Markowitz introduced the idea of mean-variance optimal
portfolios. This class is defined by the property that, among the set of admissible
portfolios, no other portfolio has both higher mean return and lower variance. The
set of such portfolios as you vary return or variance is known as the efficient frontier.
The concept is a cornerstone of modern portfolio theory, and the mean and variance
refer to one period arithmetic returns. 4 In contrast, the Kelly Criterion is used to
maximize the long term compound rate of growth, a multiperiod problem. It seems
natural, then to ask the question: is there an analog to the Markowitz efficient
frontier for multiperiod growth rates, i.e., are there portfolios such that no other
portfolio has both a higher expected growth rate and a lower variance in the growth
rate? We'll call the set of such portfolios the compound growth mean-variance
efficient frontier.
Let's explore this in the simple setting of repeated independent identically distributed returns per unit invested, where the payoff random variables are {Xi: i =
1, ... ,n} with E(Xi ) > 0 so the "game" is favorable, and where the non-negative
fractions bet at each trial, specified in advance, are {fi : i = 1, ... , n}. To keep the
math simpler, we also assume that the Xi have a finite number of distinct values. After n trials the compound, growth rate per period is G( {fi}) = ~ 2::~ 110g(1 + fiXi)
and the expected growth rate g( {gd) = E[G( {fd)] = ~ 2:: ~=1 E 10g(1 + fiXi) =
~ 2:: ~= 1 Elog(l+ fiX) :s; Elog(l+ IX). The last step follows from the (strict) concavity of the log function, where as X has the common distribution of the Xi, we
define I = ~ 2::[:1 fi and we have equality if and only if fi = I for all i. Therefore,
if some fi differ from I, we have g( {fi}) < g( {f}). This tells us that betting the
same fixed fraction always produces a higher expected growth rate than betting a
varying fraction with the same average value. Note that whatever I turns out to
be, it can always be written as I = cf*, a fraction c of the Kelly fraction.
3PIMCO is widely regarded as the top bond trading operation in the world.
4 A comprehensive survey of mean-variance theory is in Markowitz and Van Dijk (2006).
--- page 546 ---

Understanding the Kelly Criterion
Now consider the variance of G( {fd). If is a random variable with:
P(X =a)=p,
P(x=- I) =q and a>O
then Var[ln(1 + fX)] = pq [In Cl~ aj) r
(Compare Thorp, 2006, Section 3.1).
517
Note: the change of variable f = bh, b > 0, shows the results apply to any two
valued random variable. We chose b = 1 for convenience.)
A calculation shows that the second derivative with respect to f is strictly
positive for 0 < f < 1 so Var[ln(1 + fX)] is strictly convex in f. It follows that:
1
n
1
n
Var[G( {fi})] = - L Var[log(l+ fiXi)] = - L Var[log(l+ fiX)] ~ Var[log(l+ jX)]
n
n
i=l
i=l
with equality if and only if fi = j for all i. Since every admissible strategy is therefore "dominated" by a fractional Kelly strategy, it follows that the mean-variance
efficient frontier for compound growth is a subset of the fractional Kelly strategies.
If we now examine the set of fractional Kelly strategies {J} = {cf*}, we see that
for 0 ::; c ::; 1, both the mean and the variance increase as c increases but for c ~ 1,
the mean decreases and the variance increases as c increases. Consequently {f*}
dominates the strategies for which c > 1 and they are not part of the efficient frontier. No fractional Kelly strategy is dominated for 0 ::; c ::; 1. We have established
in this limited setting:
Theorem. For repeated independent trials of a two valued random variable, the
mean-variance efficient frontier for compound growth over a finite number of trials
consists precisely of the fractional Kelly strategies {cf* : 0 ::; c ::; I}.
So, given any admissible strategy, there is a fractional Kelly strategy with 0 ::;
c ::; 1, which has a growth rate that is no lower and a variance of the growth rate
that is no higher. The fractional Kelly strategies in this instance are preferable in
this sense to all the other admissible strategies, regardless of any utility function
upon which they may be based. This deals with yet another objection to the
fractional Kelly strategies, namely that there is a wide spread in the distribution of
wealth levels as the number of periods increases. In fact, this eventually enormous
dispersion is simply the magnifying effect of compound growth on small differences
in growth rate and we have shown in the theorem that in the two outcome setting
this dispersion is minimized by the fractional Kelly strategies. Note that in this
simple setting, a one-period utility function will choose a constant h = cf which
will either be a fractional Kelly with c ::; 1 in the efficient frontier or will be too
risky, with c> 1, and not be in the efficient frontier.
As a second example, suppose we have a lognormal diffusion process with instantaneous drift rate m and variance s2 where as before the admissible strategies are
--- page 547 ---

518
E. O. Thorp
to specify a set of fixed fractions {Id for each of n unit time periods, i = 1, . . . , n.
Then, for a given I and unit time period Var G(f) = s2I2 as noted in (Thorp, 2006,
eq. (7.3)). Over n periods Var G( {Ii}) = S2 2::~=1 Ii2 ;:::: S2 2::~=1 P with equality if
and only if Ii = J for all i. This follows from the strict convexity of the function
h(x) = x2 . So the theorem also is true in this setting. I don't currently know how
generally the convexity of Var[ln(l + I X)] is true but whenever it is, and we also
have Var[ln(l + IX)] increasing in I , then the compound growth mean variance
efficient frontier is once again the set of fractional Kelly strategies with 0 ~ c ~ 1.
In email correspondence, Stewart Ethier subsequently showed that Var[ln(l + I X)]
need not be convex. Example (Ethier):
Let X assume values -1, 0 and 100 with probabilities 0.5, 0.49
and 0.01, respectively. Then, on approximately the interval [0.019,
0.180] the second derivative of the variance is negative, hence the
variance is strictly concave on that interval. The first derivative of
Var[ln(l+ IX)] equals 2 Cov(ln(l+ IX), X/(l+ IX)), which is always nonnegative because the two functions of X in the covariance
are increasing in X. Thus Var[ln(l + I X)] is always increasing in I.
The second derivative of Var[ln(l + I X)] equals 2 Var(X/(l + I X))-
2 Cov(ln(l+ I X)-l, X 2 /(1+ I X)2). However, the covariance term
sometimes exceeds the variance term.
Samuelson's Criticisms
The best known "opponent" ofthe Kelly Criterion is Nobel Prize winning economist,
Paul Samuelson, who has written numerous polemics, both published and private,
over the last 40 years. William Poundstone's book Fortune's Formula gives an
extensive account with references. The gist of it seems to be:
(1) Some authors once made the error of claiming, or seeming to claim, that
acting to maximize the expected growth rate (i.e., logarithmic utility) would approximately maximize the expected value of any other continuous concave utility
(the "false corollary").
Response: Samuelson's point was correct but, to others as well as me, obvious
the first time I saw the false claim. However, the fact that some writers made
mistakes has no bearing on an objective evaluation of the merits of the criterion.
So this is of no further relevance.
(2) In private correspondence to numerous people Samuelson has offered examples and calculations in which he demonstrates, with a two valued X ("stock") and
three utilities, H(W) = - l /W, K(W) = log W, and T(W) = W 1/ 2 , that if any
one who values his wealth with one of these utilities uses one of the other utilities
to choose how much to invest then he will suffer a loss as measured with his own
utility in each period and the sum of these losses will tend to infinity as the number
of periods increases.
--- page 548 ---

Understanding the Kelly Criterion
519
Response: Samuelson's computations are simply instances of the following general fact proven 30 years earlier by Thorp and Whitley (1972, 1974).5
Theorem 1. Let U and V be utilities defined and differentiable on (0,00) with
U'(x) and V'(x) positive and strictly decreasing as x increases. Then if U and
V are inequivalent, there is a one period investment setting such that U and V
have distinct sets of optimal strategies. Furthermore, the investment setting may be
chosen to consist only of cash and a two-valued random investment, in which case
the optimal strategies are unique.
Corollary 2. If the utilities U and V have the same (sets of) optimal strategies
fo r each finite sequence of investment settings, then U and V are equivalent.
Two utilities U1 and U2 are equivalent if and only if there are constants a and
b such that U2 (x) = aU1(x) + b(a > 0), otherwise U - 1 and U2 are inequivalent.
Thus, no utility in the class described in the theorem either dominates or is
dominated by any other member of the class.
Samuelson offers us utilities without any indication as to how we ought to choose
among them, except perhaps for this hint. He says that he and an apparent majority
of the investment community believe that maximizing U (x) = - 1/ x explains the
data better than maximizing U(x) = logx. How is it related to fractional Kelly?
Does this matter? Here are two examples showing that this utility can choose cf*
for any 0 < c < 1, c i=- 1/2, depending on the setting:
For a favorable coin toss and U(x) = - 1/x, we have f* = p,/(yIP + ,fij)2 which
increases from p,/2 or half Kelly to p, or full Kelly as p increases from 1/2 to 1,
giving us the set 1/2 < c1. On the other hand, if P (X = A) = P (X = - 1) = 1/2
describe the returns and A> 1 so P, > 0, p, = (A-l)/2 and the Kelly f* = p,/A. For
U(x) = - 1/x we find U maximized for f = {-2A± (4A2+A(Al )2)1/2}/A(Al ),
which is asymptotic to A -1/2 as A increases, compared to the Kelly f*, which is
asymptotic to 1/2 as A increases, giving us the set 0 < c < 1/2.
In the continuous case, the relation between c, g(f) and a(G(f)) is simple and
the tradeoff between growth and spread in growth rate as we adjust between 0
and 1 is easy to compute and it's easy to visualize the correspondence between
fractional Kelly and the compound growth mean-variance efficient frontier. This
is not the case for these two examples so the fact that U (x) = -1/ x can choose
any c, 0 < c < 1, c i=- 1/2 doesn't necessarily make it undesirable. 6 I suggest that
5The first Thorp and Whitley paper is reprinted in this book in Section 4 where three of Samuelson's papers are reprinted and discussed in the introduction to that part of this book.
6 MacLean, Ziemba and Li (2005) reprinted in Section 4 of this book, show that for lognormally
distributed assets, a fractional Kelly strategy is uniquely related to the coefficient a < 0 in t he
negative power utility function oow" via the formula c = 1/(1 - a) so 1/2 Kelly is -l/w. However,
when assets are lognormal this is only an approximation and, as shown here, it can be a poor
approximation.
--- page 549 ---

520
E. 0. Thorp
a useful way to look at the problem for any specific example involving n period
compound growth is to map the admissible portfolios into the (O"(G{fi}), g({fd))
plane, analogous to the Markowitz one period mapping into the (standard deviation,
return) plane. Then examine the efficient frontier and decide what tradeoff of growth
versus variability of growth you like. Professor Tom Cover points out that there
is no need to invoke utilities. Adopting this point of view, we're simply interested
in portfolios on the compound growth efficient frontier whether or not any of them
happen to be generated by utilities. The Samuelson's preoccupation with utilities
becomes irrelevant. The Kelly or maximum growth portfolio, which as it happens
can be computed using the utility U (x) = log x, has the distinction of being at the
extreme high end of the efficient frontier.
For another perspective on Samuelson's objections, consider the three concepts:
normative, descriptive and prescriptive. A normative utility or other recipe tells
us what portfolio we "ought" to choose, such as "bet according to log utility to
maximize your own good". Samuelson has indicated that he wants to stop people
from being deceived by such a pitch. I completely agree with him on this point.
My view is instead prescriptive: how to achieve an objective. If you know future
payoff for certain and want to maximize your long term growth rate then Kelly does
it. If, as is usually the case, you only have estimates of future payoffs and want to
come close to maximizing your long term growth rate, then to avoid damage from
inadvertently betting more than Kelly you need to back off from your estimate of
full Kelly and consider a fractional Kelly strategy. In any case, you may not like the
large drawdowns that occur with Kelly fractions over 1/2 and may be well advised
to choose lower values. The long term growth investor can construct the compound
growth efficient frontier and choose his most desirable geometric growth Markowitz
type combinations.
Samuelson also says that U (x) = - 1/ x seems roughly consistent with the data.
That is descriptive, i.e., an assertion about what people actually do. We don't argue
with that claim -
it's something to be determined by experimental economists and
its correctness or lack thereof has no bearing on the prescriptive recipe for growth
maximizing.
I met the economist Oscar Morgenstern (1902- 1977), coauthor with John von
Neumann of the great book, The Theory of Games and Economic Behavior, at his
company, Mathematica; in Princeton, New Jersey, in November of 1967 and, when
I outlined these views on normative, prescriptive and descriptive, he liked them
so much that he asked if he could incorporate them into an article he was writing
at the time. He also gave me an autographed copy of his book, On the Accuracy
of Economic Observations, which has an honored place in my library today and
which remains timely. (For instance, think about how the government has made
successive revisions in the method of calculating inflation so as to produce lower
numbers, thereby gaining political and budgetary benefits).
--- page 550 ---

Understanding the Kelly Criterion
521
Proebsting's Paradox
Next, we look at a curious paradox. Recall that one property of the Kelly Criterion is that if capital is infinitely divisible, arbitrarily small bets are allowed,
and the bettor can choose to bet only on favorable situations, then the Kelly bettor can never be ruined absolutely (capital equals zero) or asymptotically (capital
tends to zero with positive probability). Here's an example that seems to flatly
contradict this property. The Kelly bettor can make a series of favorable bets yet
be (asymptotically) ruined! Here's the email discussion through which I learned
of this.
From: Todd Proebsting
Subject: FW: incremental Kelly Criterion
Dear Dr. Thorp,
I have tried to digest much of your writings on applying the Kelly Criterion to gambling but I have found a simple question that is unaddressed.
I hope you find it interesting:
Suppose that you believe an event will occur with 50% probability and
somebody offers you 2:1 odds. Kelly would tell you to bet 25% of your
capital. Similarly, if you were offered 5:1 odds, Kelly would tell you to
bet 40%. Now, suppose that these events occur in sequence. You are
offered 2:1 odds, and you place a 25% bet. Then another party offers
you 5:1 odds. I assume you should place an additional bet, but for what
amount?
If you have any guidance or references on this question, I would appreciate it.
Thank you.
From: Ed Thorp
To: Todd Proebsting
Subject: Fw: incremental Kelly Criterion Interesting.
After the first bet the situation is:
A win gives a wealth relative of 1 + 0.25 * 2
A loss gives a wealth relative of 1 - 0.25
Now bet an additional fraction 1 at 5:1 odds and we have:
A win gives a wealth relative of 1 + 0.25 * 2 + 51
A loss gives a wealth relative of 1 - 0.25 - 1
The exponential rate of growth g(f) = 0.5*ln(1.5+5f) +0.5*ln(0.75- f)
Solving g'(f) = 0 yields 1 = 0.225 which was a bit of a surprise until I
thought about it for a while and looked at other related situations.
From: Todd Proebsting
To: Ed T horp
Subject: RE: incremental Kelly Criterion
Thank you very much for the reply.
--- page 551 ---

522
I, too, came to this result, but I thought it must be wrong since this
tells me to bet a total of 0.475 (0.25 + 0.225) at odds that are on average
worse than 5:1, and yet at 5:1, Kelly would say to bet only 0.400.
Do you have an intuitive explanation for this paradox?
From: Ed Thorp
To: Todd Proebsting
Subject: Re: incremental Kelly Criterion
I don't know if this helps, but consider the example:
A fair coin will be tossed (Pr Heads = Pr Tails = 0.5). You place a bet
which gives a wealth relative of 1 + u if you win and 1 - d if you lose (u
and d are both nonnegative). (No assumption about whether you should
have made the bet.) Then you are offered odds of 5:1 on any additional
bet you care to make. Now the wealth relatives are, each with Pr 0.5,
1 + u + 5f and 1 - d - f. The Kelly fraction is f = (4 - u - 5d)/10.
It seems strange that increasing either u or d reduces f. To see why it
happens, look at the In(l + x) function. This odd behavior follows from
its concave shape.
From: Todd Proebsting
To: Ed Thorp
Subject: RE: incremental Kelly Criterion
Yes, this helps. Thank you.
It is interesting to note that Kelly is often thought to avoid ruin. For
instance, no matter how high the offered odds, Kelly would never have
you bet more than 0.5 of bankroll on a fair coin with one single bet.
Things change, however, when given these string bets. If I keep offering
you better and better odds and you keep applying Kelly, then I can get
you to bet an amount arbitrarily close to your bankroll.
Thus, string bets can seduce people to risking ruin using Kelly. (Granted
at the risk of potentially giant losses by the seductress.)
From: Ed Thorp
To: Todd Proebsting
Subject: Re: incremental Kelly Criterion
Thanks. I hadn't noticed this feature of Kelly (not having looked at
string bets). To check your point with an example I chose consecutive
odds to one of An : 1 where An = 2n, n = 1,2, ... and showed by
induction that the amount bet at each n was fn = 3(n-l) /4n (where /\
is exponentiation and is done before division or multiplication) and that
sum{fn : n = 1, 2, ... } = 1.
A feature (virtue?) of fractional Kelly strategies, with the multiplier less
than 1, e.g. f = c* f(kelly) , 0 < c < 1, is that it (presumably) avoids
this.
E. O. Thorp
--- page 552 ---

Understanding the Kelly Criterion
523
In contrast to Proebsting's example, the property that betting Kelly or any fixed
fraction thereof less than one leads to exponential growth is typically derived by
assuming a series of independent bets or, more generally, with limitations on the degree of dependence between successive bets. For example, in blackjack there is weak
dependence between the outcomes of successive deals from the same unreshuffied
pack of cards but zero dependence between different packs of cards, or equivalently
between different shuffiings of the same pack. Thus the paradox is a surprise but
doesn't contradict the Kelly optimal growth property.
R eferences
Ethier, S. (2010) . The Doctrine of Chances. Berlin: Springer-Verlag.
Geyer, A. and W. T . Ziemba (2008) . The innovest Austrian pension fund financial planning
model InnoALM. Operations Research, 56(4), 797- 810.
MacLean, L. C., W . T. Ziemba and G. Blazenko (1992). Growth versus security in dynamic
investment analysis. Management Science, 38, 1562- 1585.
Markowitz, H. M. and E. van Dijk (2006). Risk return analysis, in S. A. Zenios and
W. T. Ziemba (eds.) , Handbook of Asset and Liability Management, Vol. I: Theory
and Methodology. Amsterdam: North Holland, 139- 197.
Pabrai, M. (2007). The Dhandho Investor. New York: Wiley.
Poundstone, W. (2005). Fortune 's Formula. US: Hill and Wang.
Taleb, N. N. (2007). The Black Swan: The Impact of the Highly Improbable. US: Barnes
and Noble.
Thorp, E. O. (2006). The Kelly Criterion in blackjack, sports betting and the stock market,
in S. A. Zenios and W. T. Ziemba (eds.) , Handbook of Asset and Liability Management, Vol. I: Theory and Methodology. Amsterdam: North Holland, 385- 428.
Thorp, E . O. and R. Whitley (1972). Concave utilities are distinguished by their optimal
strategies. Colloquia Mathematica Societatis Janos Bolyai, 9.
Thorp, E. O. and R. Whitley (1974). Progress in statistics, in Proceedings of the European
Meeting of Statisticians, Budapest. North Holland, pp. 813- 830.
Ziemba, R. E. S. and W. T. Ziemba (2007). Scenarios for Risk Management and Global
Investment Strategies. New York: Wiley.
Ziemba, W. T. (2003). The Stochastic Programming Approach to Asset Liability Management. AIMR.
Ziemba, W . T . and R. G. Vickson, eds. (2006) . Stochastic Optimization Models in Finance,
2nd Edition. Singapore: World Scientific.
