# The Kelly capital growth investment criterion _ theory and -- Leonard C_ Maclean, Edward O_ Thorp, W_ T_ Ziemba, Leonard -- World Scientific Handbook -- isbn13 9781283148344 -- bec576e26410d0c695fd5b867d08ec4f -- An.pdf — pages 96–115

--- page 96 ---

Optimal Gambling Systems for Favorable Games
69
281
It is interesting to calculate E( G J ) by assuming that S J is log normally distributed.
Letting S J = S J I E, we thus assume that S J has the density function
f ( x) = (x cr .J2"it) -1 exp [ - (In x - Jl)2 I 2 cr2 ], where Jl and cr are parameters depending on the stock. We note E (s J) = exp (Jl + cr2 /2).
If t is the time in months remaining until expiration (which is when S J is realized),
then we assume (J. = log So + mt and 0"2 = a2t, where So = So E is the present stock
price and m and a are constants depending on the stock. Thus E(s J) = So exp
[em + a2/2)t]. A mean increase of 10% per year is approximated by setting 12(m +
a2/2) = .1. If we estimate a2 from past price changes we can solve for m.
Letting w, = WIlE, where W, is the final warrant price, a calculation yields
E( w,) = E(s,) N«(J./O" + 0") - N«(J./O"), where N is the normal distribution. (Compare
the equivalent expression from pp. 464-466 of [5].) Now suppose that So = .5, that a
has the realistic value of .Iso or .05, and that 12(m + a2/2) = .1, whence m =
.085/12. Then for t = 24 we have cr = ).06 = .245 and Jl = log .5 + .17 = -.523.
This yields E(w,) = .0015 and E(s,) = .61, whence E(G,) = .20 + .11 = .31. Thus
the profit, with 70% margin on both warrant and common, is .31/.49 or 63.3% and
the annual rate is 31.6 %. Note that the warrant is virtually worthless!
Instead of selling one warrant short and buying one share of common, we can sell
short w warrants and buy s shares of common. Neglecting commissions, which we do
throughout for simplicity, the gain G at any point (S, W) is s(S - So) -we W - Wo).
Thus the line G = 0, the zero profit line, is the line through (Wo, So) with positive
slope slw = 11m. We call m the mix. Points below the zero profit line represent gain
and points above it represent loss. If 1 < m < co, the zero profit line intersects the S
axis at So - m Wo and it intersects the line W = S - E at S = [me Wo + E) - So] /
(m - 1); W = (m Wo + E - So) I (m - 1).
When the warrant expires the hedge position will yield a profit if S, is between
the S values of the two intersections and it will yield a loss if S, is beyond the intersections. For instance, if So = .5E and Wo = .2E, the choice m = 2 insures a final
profit if .IE < s, < 1.9E. Such safety is characteristic of the warrant hedge.
The final gain G, is s(S,- So) + wWo if S, < E and it is sCSI - So) + w( Wo +
E - S,) if S, > E. Thus as a function of S, it is an inverted "V" with apex above
S, = E. With 100 % margin, the initial investment is s So + w Wo so the gain per
unit invested is g, = G ,/(s So + w Wo). With margin of ot on the common and f3 on
the warrants it is g, = G,/(ot s So + f3 w Wo).
We have assumed so far that a hedge position is held unchanged until expiration,
then closed out. This static or "desert island" strategy is not optimal. In practice
intermediate decisions in the spirit of dynamic programming lead to considerably
superior dynamic strategies. The methods, technical details, and probabilistic summary are more complex so we defer the details for possible subsequent publication.
Probabilistic summary
The warrant hedge may offer high expectation with low risk. The gain per unit
g,isg, = [(Sf + So) + m Wo] / (ot So + f3m Wo) when SJ < Eandg, = [(S,- So)
+ m( Wo + E - Sf)] / (ot So + f3m Wo) if SJ > E. The gain per unit depends only
on the random variable S ,. This has an unknown distribution but it can be estimated.
The other quantities are constants depending on circumstances.
--- page 97 ---

70
E. 0. Thorp
282
PART II. A MATHEMATICAL THEORY FOR COMMITTING
RESOURCES IN FAVORABLE GAMES
1. INTRODUCTION: COIN TOSSING
Suppose we are confronted with an infinitely rich adversary who will match all bets
we make on repeated independent trials of a biased coin (whose two outcomes are
"heads" and "tails".) Assume that we have finite capital Xo, that we bet Bi on the
outcome of the ith trial, where Xi is our capital after the ith trial, and that the probability of heads is p, where -1 < p < I. (This is approximately the situation in Nevada
blackjack, except that the game is played with a "mix" of biased coins.) Our problem
is to decide how much to bet at each trial. A classic criterion is to choose Bi so that
our expected gain E(Xi - Xi-I) is maximized at each trial, which is equivalent to
maximizing E(Xn) for all n.
Define Tj by Tj = I if the jth trial results in success and Tj = -1 if the jth trial
n
results in failure. Then X j = X j_1 + TjBj, j = 1,2, ... , and Xn = Xo + l: TjBj.
j=1
We assume that Tj , Xj' and Bj are all random variables on a suitable sample space Q.
If, for example, Bj is a function of Xo, XI' . . . , Xj _ 1 as it is in the common gambling
systems, e.g. Martingale, Labouchere, etc. (note that Bk = I Xk - Xk - 1 I so we need
not add the Bk , k = I, ... ,j - I), then we see by induction that Bj is a function of
Xo, T I , T2 , •• • Hence the underlying sample space can be taken to be the space of all
sequences of successes and failures, with the usual product measure.
Suppose, more generally, that the player determined Bj by examining Xo, ... ,
Xj _ I' and then "consulting" a chance device, e.g., a near-by roulette wheel. Then the
sample space consisting of an infinite product of spaces, each of them a joint outcome
of the roulette wheel and the latest trial, might be suitable. Such possibilities are included if we simply assume T j , Xj and Bj are all random variables on some suitable
sample space n.
When Bj > Xj-I' the player is betting more than he has. He is asking for credit.
This is common in gambling casinos, in the stock market (buying on margin), in real
estate (mortgages) and is not unrealistic.
When Bj < 0, the player is making a "negative" bet. To interpret this, we note
that in our sequence of Bernoulli trials, or coin toss between two players, that what
one wins, Xj - Xo, the other loses. To make a negative bet may be interpreted as
"backing" the other side of the game, to taking the role of the "other" player.
In particular, the payoff BjTj from trialj may be written as (-B) (-T). If Bj;£ 0,
then -Bj > °
and may be interpreted as a nonnegative bet by a player who succeeds
when -Tj = I, i.e., with probability q, and who fails with probability p. The -Tj are
independent so we have Bernoulli trials with success probabilities q, i.e., the other
side of the game.
For simplicity we shall assume in what follows that ° < Bj ::;; X j - 1, but we may
wish at a future time to remove one or both of these limitations.
We also assume that Bj is independent of Tj , i.e., the amount bet on the jth outcome is independent of that outcome.
Definition: A betting strategy is a family {B j } such that ° ::: B j ::;; Xj _ I ,j = I, 2, ...
Theorem I: The betting strategies Bj = Xj _ 1 when p > t; Bj = 0, p < t; Bj arbitrary when p = t; are precisely the ones which maximize E(X) for eachj.
n
n
Proof: Since Xn = Xo + l: BJj, E(Xn) = Xo + l: E(BjTj ) =
j=1
j=l
--- page 98 ---

Optimal Gambling Systems for Favorable Games
71
283
n
= Xo + r (p-q)E(Bj).Ifp-q = O, i.e.,p = t,thenE(Bj)doesnotaffectE(Xn ).
j=l
If p - q > 0, i.e. p > t, then E(Bj ) should be maximized, i.e., Bj = Xj' to maximize
E(Xn). Similarly, if p - q < 0, i.e., p < t, then E(Bj ) should be minimized to maximize the jth term, i.e., Bj = 0. Clearly, these maxima are not attained with other
choices for Bj • This establishes the theorem.
Remark. In the foregoing discussion, the Bernoulli trials and the Tj can be generalized, yielding a more general theorem. (The Tj become "payoff functions" that are
not necessarily identically distributed; roulette is the classic example.) The particular
case of blackjack is covered, for instance, by replacing p and q throughout by Pj
and qj for the respective probabilities that Tj = I or-l.
To maximize our expected gain we must bet our total resources at each trial. Thus
if we lose once we are ruined, and the probability of this is I - pn -+ I so maximizing
expected gain is undesirable.
2. MINIMIZING THE PROBABILITY OF RUIN
Suppose instead that we play to minimize the probability of eventual ruin, where
ruin occurs after the jth outcome if Xj = o. If we impose no further restriction on Bj ,
then many strategies minimize the probability of ruin. For example, it suffices to
choose Bj < X j _ d2. The discreteness of money makes it realisti·c to assume B j ;:::::
C > 0, where C is a non-zero constant. We further restrict ourselves to the subclass
of strategies where Bj equals C whenever ° < Xj - 1 < a, Bj = 0 if Xj - 1 < 0 or
Xj - 1 > a, and C divides both a - z and z, where we have set z = Xo. This lets us use
the gambler's ruin formulae ([8], page 3(4).
Consider the gambler's ruin situation: Xo = z, Bj = I if 0 < Xj _ 1 < a, Bj = 0
if X j - 1 = 0 or Xj - 1 = a, a and z are integers. Let r be a positive number (necessarily
rational) such that zr and ar are integers. Let R(r) be the ruin probability when z and a
are replaced by zr and ar, respectively. This is equivalent to betting r -1 units when
o < X j - 1 < a, in the original problem.
We have R(r) = (6or - 6U
) / (oar - I), where 0 < p =l= 1- and 6 = q/p.
Theorem 2: (a) If 1 > p > t, R(r) is a strictly decreasing function of r. (b) If
o < p < 1. R(r) is a strictly increasing function of r.
Proof: Follows from Lemma 3 below.
Part (a) of the Theorem says that in a favorable game, the chance of ruin is decreased
by decreasing stakes. Note that for p > t, i.e., e < 1, lim R (r) = 0, hence by
r-+",
making stakes sufficiently small, the chance of ruin can be made arbitrarily small.
Lemma 3. Let a> z > 0, x> O. IfO < 6 < 1, then I(x) = (6 ZX - 6ax ) / (1- 6°X )
is strictly decreasing as x increases, x > 0. If 6 > 1, I (x) is strictly increasing as x
increases, x > o.
Proof: Elementary calculations which we omit.
Theorem 2(a) shows that, at least in the limited subclass of strategies to which it
applies, we minimize ruin by making a minimum bet on each trial.
In fact, this holds for a broader class of strategies:
Theorem 3' : If 1 > p > t, the strategy Bj = I if 1 < z < a-I, Bj = ° otherwise
(timid play), uniquely minimizes the probability of ruin among the strategies where B j
is an integer satisfying 1 < Bj < min (z, a-z) if I < z < a-I, Bj = 0 otherwise.
Proof: We first show that if timid play is optimal, then it is uniquely so. Let qz be
the probability of ruin, starting from z, under timid play. To establish uniqueness it
suffices to show
--- page 99 ---

72
E. 0. Thorp
284
qn < pqz+k + q qz-k' 2 < k < a-2, z-k > 0, z + k < a.
(1)
Using qz = (6°_6Z ) I (6°-1) and simplifying (1), we find that it is equivalent to show
I(p) =p2k-l + q2k-l_ pk-l qk-t > 0, 1/2 <p < 1.
(2)
This follows at once from the observations 10·) = 0, I ( I) = I, and f' (p) > 0,
t<p<l.
To show that timid play is optimal, let Q(z) = l-qz, and adopt the terminology
of [6]. Then Q(z) is the probability of success, both for z in our original game, and
for zln in a normalized game where the possible fortunes are F = {O, I/a, 21a, ... ,
zla, ... , 1 = a/a }, and the betting units and limits are l/a as large as before.
The establishment of (1) shows Q(z) is excessive. But obviously u(z) ~ Q(z)
< U(z) so by [6, Theorem 2.12.3], Q(z) = U (z).
Thus timid play is the one and only strategy in our class of strategies which minimizes the probability of ruin.
Remark: In [6] it is shown that bold play is optimal but not necessarily unique
when p < t (pages 2, 87ff, 101ft"). If there is also a legal upper limit to bets, there may
be more than one optimal strategy; whether bold play is one of them seems to be
unknown (page 4). Betting systems which minimize the probability of ruin in certain
favorable games are also discussed in [10].
The strategy which minimizes ruin has the unsatisfactory consequence that it also
minimizes our expected gain. Some strategy is called for which is intermediate between minimizing ruin (and expectation) and maximizing expectation (assuring ruin).
A remarkable solution, in a certain sense very close to best possible, was proposed
in [13].
3. THE KELLY CRITERION
Consider Bernoulli trials with I > p > t and Bj = I Xj-t, where ° < 1< I is a
constant. (This is sometimes called "fixed fraction" or "proportional" betting.) Let
Sn and Fn be the number of successes and failures, respectively, in n trials. Then
Observe that I = ° andl = 1 are uninteresting; we assume ° < I < 1. Note too
that if 1< 1. there is no chance that Xn = 0, ever. Hence ruin, in the sense of the
gambler's ruin problem, cannot occur. We reinterpret "ruin" to mean that for each
s > 0, lim P [Xn > s] = 0, and we shall see that this can occur. Note too that we
n
are now assuming that capital is infinitely divisible. However, this assumption is not
a serious problem in practical applications of the theory.
Remark: The min-max criterion of game theory is an inappropriate criterion in
Bernoulli trials. If Bj is a positive integer for all}, the maximum loss, i.e. ruin, is always
possible and all strategies have the same maximum possible loss, hence all are equivalent. If capital is infinitely divisible, ruin is as we redefined it, and we restrict ourselves
to fixed fractions, then for an infinite series of trials the min-max criterion (suitably
probabilitistically modified) considers all I with 1 > I > Ie equivalent and all I with
° < 1< Ic equivalent. It chooses the latter class. For a fixed number n of trials,
smaller I are preferred over larger f The criteria of minimizing ruin or of maximizing
expectation likewise fail to make desirable distinctions between the fixed fraction
strategies.
--- page 100 ---

Optimal Gambling Systems for Favorable Games
73
285
The quantity log [Xn / XO]l/n = (Sn / n) log (1 + f) + (Fn / n) log (1 - f) measures the rate of increase per trial. Since time is important it is plausible to in some
sense maximize this. Kelly's choice [13] was to maximize E log [ Xn / Xo ]l/n = p log
(1 + f) + q log (1 - f) == G (I), which we call the exponential rate of growth. The
following theorems show the advantages of maximizing G (I).
Theorem 4. If 1 > p > t, G (I) has a unique maximum at/* = p - q, ° <1* < 1,
where G (1*) = p log p + q log q + log 2 > 0. There is a unique fraction fc > °
such that G (/c) = 0, and Ie satisfies f* < fc < 1. Further, we have G (I) > 0,
° < I < Ie; G (I) < 0, I> /C, with G (I) strictly increasing, from ° to G (1*), on
[0,/*], and G (I) strictly decreasing, from G (1*) to - 00 on [/*, 1].
Theorem 5(a). If G (f) > 0, then lim Xn = 00 a.s., i.e., for each M, P.[ lim
n
n
Xn> MJ = 1.
(b) If G (f) < 0, then lim Xn = 0 a.s., i.e., for each c: > 0, P [lim Xn < c:] = 1.
n
n
(c) If G (f) = 0, then lim Xn =
OCJ a.s. and lim Xn = 0 a.s.
n
-n-
Thus for ° < I < fc, the player's fortune will eventually permanently exceed any
fixed bounds with probability one. For I = Ie it will almost surely oscillate wildly
between 0 and + 00. If I> fe, ruin is almost sure.
l/n
Proof: (a) By the Borel strong law ([17], page 19),limlog[Xn/Xo]
= G(f) > °
n
with probability 1. Hence, a.s., for w € n, where n is the space of all sequences of
Bernoulli trials, there exists N (w) such that for n > N (w),
log [Xn/ Xop/n> G(I)/2> O.
But then Xn > Xo en GU)j2 for n > N(w) so XnJ' 00.
(b) The proof is similar to part (a).
(c) We use the fact that, given any M, lim Sn > np + M + 1 and
n
.
.
/
~+M
lIm Sn < np - M -1. Then If Sn > np + M, log [Xn / XO]l n >
n
n
n-(np+M)
M
1+/ M
1+/
log (1 + f) +
log (l - f) = G (f) + -
log -1
/ = -log -1 -I'
n
n
-
n
-
whence Xn > Xo (~ = j) M. Since Sn > np + M infinitely often, a.s., then
li~ Xn > Xo (~ ~ j) M a.s. Since the right side may be chosen arbitrarily large,
lim Xn = 00 a.s.
n
The proof that lim Xn = 0 a.s. is similar.
n
Theorem 6: IfG(fd > G(f2), then lim X n(f1)/Xn(f2) = 00 a.s.
n
Proof: log [Xn (ld / Xo]l/n -log [Xn (12) / XO)l/n
= log [Xn (f1) / Xn (f2)]1/n = ~ log G :j:) + :n log G=j:). Therefore, by the
Borel strong law of large numbers, lim log [X n (f1) / X n (f2 )] -+ G (fd - G (f2) > 0
n
with probability 1. Now proceed as in the proof of Theorem 5(a).
In particular, we see that if one player uses/* and another, betting on the same favor-
--- page 101 ---

74
E. 0. Thorp
286
able situation, uses any other fixed fraction strategy I, then lim Xn(f*) / Xn (f) = co
n
with probability I. This is one of the important justifications of the criterion "bet to
maximize E log X n."
Bellman and Kalaba ([2], pages 200-201) show thatf* not only maximizes E log Xn
within the class of all fixed fraction betting strategies but in the class of "all" betting
strategies.
This also is a consequence of the following theorem, part of which was suggested
by a conversation with J. Holladay. Consider a series of independent trials in which
the return on one unit bet on the ith outcome is the random variable Qi. Then
n
n
Xn = n (Xi/Xi_dandElogXn = L Elog(Xi/Xi_ I ). We have Xi = Xi-I +
i= 1
i= 1
BiQi and Xi / Xi-I = 1 + (Bi / Xi-I) Qi. Thus each term is of the form E log (1 +
FiQ;) where the random variable Fi depends only on the first i-I trials, Qi depends
only on the ith trial, and hence Fi and Qi are independent. We are free to choose the
Fi to maximize E log (1 + FiQ;), subject to the constraint 0 ~ Fi ~ 1.
Theorem 7: If for each i there is anfi' 0 < fi < I, such that E log (1 + fiQi)
is defined and positive, then for each i there is a number Ii* such that E log ( 1 + FiQi)
attains its unique maximum for Fi = Ir a.s. To avoid trivialities we assume Qi * 0
a.s., each i.
Proof: It follows that the domain of definition of E log (I + fiQi) is an interval
[0, a;) or [0, ad, where ai = min (1, b;) and bi = sup U; :fiQi > ° a.s. } > O. Since
the second derivative with respect to h of E log ( 1 + hQi) is - E ( Q? i (1 + j;Qi)2) ,
which is defined and negative, any maximum of E log (I + /;Q i) is unique. The function is continuous on its domain so if it is defined at ai' there is a maximum. If it is
not defined at ai' then lim E log (1 + IiQ;) = -
oc> so again there is a maximum.
I I to,
By the independence of Fi and Qi' we can consider Fi(sl) and Qi(S2) as functions
on a product measure space SI x S2. Then
Elog(l+FiQi) = S S log(1+Fi(sl)Qi(s2» = EElog(l+Fi(sl)Qi)
S, S2
< E log (1 + !;* Qi) with equality if and only if E log (1 + Fi (s I) Qi) =
E log (1 + !;* Q;) a.s., which is equivalent to Ii * Qi = Fi (Sl) Qi a.s., and by the independence this means either It = Fi a.s. or Qi = ° a.s. hence It = Fi a.s., and the
theorem is established.
We see in particular from the preceding theorem that for Bernoulli trials with success probability Pi on the ith trial and 1 > Pi > t, E log Xn is maximized by simply
choosing on each trial the fraction Ii * = Pi - q i which maximizes E log ( 1 + h Qi ).
4. THE ADVANTAGES OF MAXIMIZING E LOG Xn
The desirability of maximizing E log Xn was established in a fairly general setting
by Breiman [3]. Consider repeated independent trials with finitely many outcomes
I = {I, ... , S } for each trial. Let P(i) = Pi' i = 1, .. . , s, and suppose that
{ AI' .. . , A, } is a collection of (betting) subsets of I, that each i is in some Ak , and
that payoff odds Ok correspond to the Ak • We bet amounts B I, . . . , B, on the respective
Ak and if outcome i occurs, we receive L Bjo j where the sum is over {j : i e: A j }.
We make the convention that A I = I and ° I = 1, which allows us to hold part of our
fortune in reserve by simply betting it on AI. We have, in effect, a generalized roulette
game.
--- page 102 ---

Optimal Gambling Systems for Favorable Games
75
287
Roulette and the wheel of fortune, as described in Part I, are covered directly by
Breiman's theory.
The theory easily extends to independent trials with finitely many outcomes which
are not identically distributed but which are a mix of finitely many distinct distributions, each occurring on a given trial with specified probabilities. The theory so extended applies to Blackjack and Nevada Baccarat, as described in Part 1.
Breiman calls a game (i.e., a series of such trials) favorable if there is a gambling
strategy such that Xn ~ 00 a.s. Thus the infinite divisibility of capital is tacitly assumed.
However, this is not a serious limitation of the theory. If the probability is "negligible"
that the player's capital will at some time be "small," then the theory based on the
assumption that capital is infinitely divisible applies to good approximation when the
player's capital is discrete. This problem is considered for Nevada Baccarat in [24],
pages 319 and 321.
Breiman establishes the following about strategies which maximize E log X n•
1. Allowing arbitrary strategies, there is a fixed fraction strategy B i = Ui, ... ,f,.)
which maximizes E log X n•
2. If two players bet on the same game, one using a strategy A * which maximizes
E log X n and the other using an "essentially different" strategy A, then lim
n
Xn (A*) / Xn (A) ~ 00 a.s.
3. The expected time to reach a fixed preassigned goal x is, asymptotically as x increases, least with a strategy which maximizes E log X n •
Thus strategies which maximize E log Xn are (asymptotically) best by two reasonable criteria.
5. A STOCK MARKET EXAMPLE
Though in practice there are only finitely many outcomes of a bet in the stock
market, it is technically convenient to approximate the finite distributions by discrete
countably infinite distributions or by continuous distributions. In fact it is generally
difficult not to do this. The additional hypotheses and difficulties which occur are,
from the practical point of view, artificial consequences of the technique. Hence the
new theory must preserve the conclusions of the finite theory so again we apportion
our resources to maximize E log X n•
As a first example, consider the following stock market investment. It was the first
to catch our interest, and was based on a tip from a company insider.
Suppose a certain stock now sells at 20 and that the anticipated price of the stock
in one year is uniformly distributed on the interval [15, 35]. We first computeJ* and
G (J*), assuming the stock is purchased and fully paid for now, and sold in one year.
The purchase and selling fees have been included in the price. Thus, the outcome of
this gamble, per unit bet, is described by dF (s) = C (_ t. t) ( s) ds, where F is the associated probability distribution and Cis) is I for s in A and 0 for s not in A.
The mean m of F is t > O. Also
t
.
~-
S log2 e
G(f)= S log2(1+fs)ds,G'(j) = S -1
f,ds,and lim G'(f) =-00.
-t
-t + S
It 4
Therefore Theorem 8 below applies and there is a uniqueJ* such that 0 <J* < 4 and
G' (/*) = O. To obtain f*, it suffices to solve
t fs ds
t
t
ds
h (f) = 0 where h (f) = fG' (f) / log2 e = S -1
f = S ds - S 1 + f
-t + s
-t
--.\-
S
.
It.
1 + if
= 1 - ( 1 / f) loge ( 1 + fs)
whIch reduces to 1 - (Iff) loge 1 _ 1.f = h (f).
-t
4
--- page 103 ---

76
E. 0. Thorp
288
Now h(f) has the same sign and root as G'(f) on (0,4). Since h(3) = I -110g.
13 > 0, G' (f) > 0 for 0 <1< 3. Therefore 3 < 1* < 4; calculation yields 1* =
3.60-.
Thus if the maximum fraction of current capital which can be bet is 1, we should
bet all our capital. However, if margin buying is allowed, we should (consistent with
our ability to cover later) be willing to bet as much as possible, up to a fraction 1*
which is 3.6 times our current capital.
The mathematical expectation for buying outright is 0.25 Vo if buying on margin
is excluded and 0.90 Vo if unlimited buying on margin is permitted, and additional
coverings can be made later as required, and we betf* = 3.60 of our current capital.
Integration yields
G(f) = [(log2 e) If] { (1 + 3114)[ In (1 + 3114) - 1 ] - (1-114)[ In (1 - fl 4) - 1 J}
from which we find G (1) = 0.28 and G (3.60) = .59.
Next, we compute 1* and G (/*), assuming that calls are purchased for 2 points
per share. Thus the outcome of this gamble per unit bet is described by the probability
distribution F with mass 5/20 at -1, and dF(s) = 2/20 if -1 < s < 6.5.
6.5
The mean m = 1.8125> O. Also G(I) = (5/20) log2 (1-1) + (2/20) J log2
-1
(1 + fs) ds and G'(I) = -(5/20»)Og2 e + (2/20) 6/ S110g2fe ds, from which it is
1-
-1
+ s
clear that lim G' (I) = - 00 . Therefore, again by Theorem 8 below, there is a unique
fil
f* such that G' (1*) = 0 and 0 < J* < 1.
It suffices to solve h (f) = 0 where h (f) = 20G' (I) I log2 e
= ;~f+ y{ 7.5-].IOg.(17 ~'j)}. We findJ* = 0.57. The mathematical expectation of the call purchase process is 1.8125 f* Vo or about 1.03 Yo.
Integration yields
G (f) = 0- ) log2 (1 -1)+ (Jn2 e 1101)( 1 + 6.51) [In ( 1 + 6.51) - 1 ] - ( 1 - f)
[ In ( 1 -I) - 1 ]. We find G ( 0.57 ) = 0.55.
Thus we have the interesting result that the expectation from buying calls is higher
than from buying on unlimited margin but that the growth coefficient is higher from
buying on unlimited margin. Our criterion selects the latter investment.
For buying on margin G ( 3 -) = .55 so our criterion selects buying on margin if
the margin requirement is less than t - and buying calls, if possible, if the margin
requirement exceeds t -.
.
In the preceding example we needed the following theorem to establish the uniqueness of/*. We define a = sup {t : F(- 00, t) = 0 } and note that if 1 + fa > 0 and
<:tJ
00 1
the integral G (I) = J log2 (1 + fs) dF (s) is defined, then G' (I) = J sl Ogj:2 e dF (s).
a
u
+ s
(See, e.g. [17], page 126).
<:tJ
1
Theorem 8: The function G' (I) = J s og2 e dF (s) is monotone strictly dea 1 + fs
<:tJ
creasing on [0, - 1/ a). If the mean m = J s dF (s) > 0, then the equation G' (I) =
a
j S log2 e dF (S) = 0 has exactly one solution f* in the interval (0, - 1/ a) iff lim
a 1 + fs
J7" ,.- I /a
G' (f) < O. In this event, G (I) is monotonely strictly increasing for fin [f*, - 1/ a).
Proof: If 0 <fl <f2 < -1/a, -1
Sf
> l~f (0 f= s> a)soG'(ll) > G'(l2)'
+ IS
+ 2 S
--- page 104 ---

Optimal Gambling Systems f or Favorable Games
77
289
From this and the right-hand continuity of G' (f) at 0, G' is monotone strictly decreasing on [0, -1 / a). By hypothesis G' ( ° )
= m log2 e > 0. Therefore, from the
continuity of G' (f) on [0, -1 / a ), G' (f) attains all values t on the interval
lim
G' (f) < t < G' (0) exactly once. Thus there is exactly one solution f* in
f 7"-1/0
(O,-l/a)iff
lim G'(f) < 0.
f7"-I /o
The description of G (f) is now evident.
6. WARRANT HEDGING
We next apply the criterion of maximizing E log Xn to the warrant hedge described
in Part 1. With the notation of Part I, and an assumed mix of 1, the gain X from a one
unit bet is
X = (sf - So + Wo ) / ( (X So + ~ Wo ), Sf < 1 , and
X = (Wo + 1 - So ) / ( (X So + ~ Wo ), Sf> I .
We wish to maximize the exponential rate of growth G (f), given by G (f) =
E log ( 1 + f X).
It can be shown that the situation is essentially the same as in Theorem 8 and that
this depends on the a.s. boundedness of X; we have in fact a.s. sup X = ( Wo + 1 - so) /
«x So + ~ wo) and a.s. inf X = - (so - wo) / «x So + ~ wo). Thus f* can be computed when the mix is 1, though the details are tedious.
When the mix is greater than 1, more serious difficulties appear. The payoff function
X has a.s. inf X = - co and a.s. sup X < co. This means that, no matter what fraction
f > 0 of our unit capital is bet, there is positive probability of losing at least the entire
unit. Thus any bet is rejected! Yet this is unrealistic. We now find out what is wrong.
First, the assumption that arbitrarily large losses have positive probability of occurrence is not realistic. (a) The broker will automatically act to liquidate the position
before the equity is lost. (b) The strategies for investing in hedges automatically lead
to liquidating the position after the common is substantially above exercise price.
There is, then, a maximum imposed on X by practice but it is not easy in practice
to specify this maximum. Further, this maximum will, in general, be a random
variable (a.s. bounded, however) which is a function of the individual's investment
strategy. It is not easy to determine the consequent probability distribution of sf' yet
this is required to calculate E log ( 1 + f X).
More generally, we might consider an individual's lifetime sequence of bets of
various kinds. It is plausible to assume that Xn = °
only upon the death of the individual, for although the individual may have no cash equity at a given instant, he does
have a cash "worth", based on his future income, serendipity, etc., and this should be
included in X n• This is true even of a (Billie Sol Estes) bettor who loses more than he
owns. The subtlety here, then, is that the accountant's figure for net assets (plus or
minus) is not an accurate figure for Xn as Xn decreases below small positive amounts.
One can also object to Xn at death being assigned the value 0, by arguing that the
chance of death in a time interval always has a small positive probability, thus making
E log Xn = - co always. Also, individuals when choosing between two alternatives
each involving a low probability of death generally do not meticulously select the
safer alternative (e.g., air travel versus train travel). Thus death should really be
treated as an event with a large but finite negative value.
Another common objection to E log Xn as a measure of "utility" is that, like all
such measures which are not a.s. bounded, it allows the St. Petersburg paradox.
--- page 105 ---

78
E. 0. Thorp
290
The foregoing objections to E log Xn only arise when we leave the case of finitely
many outcomes. We say that these are artificial technical difficulties which can all be
removed in the cases of practical importance. This may be tedious, as it is for the
warrant hedge, so we defer such matters for a subsequent paper.
7. PORTFOLIO SELECTION USING E LOG X
The Breiman results were obtained for repeated independent trials with finitely
many outcomes and finitely many ways to apportion our capital (amongst finitely
many betting sets). The results extend, as we have remarked, to independent trials
which are a mix of finitely many differently distributed trials (i.e., finitely many out-
(:omes and betting sets) provided that as n tends to infinity, the number of trials with
each distribution also tends to infinity.
There are significant real world situations, such as the selection and continuous
revision of a portfolio of securities, to which this extended theory does not generally
.apply. A difficulty which we have already discussed is that it may be technically convenient to introduce continuously distributed and possibly unbounded payoffs, but
now generalized to the apportionment of capital among a finite number of alternatives, rather than just betting a fraction on one alternative. Another problem is that
the sequence of betting situations may change so that no two are ever the same.
Further difficulties arise when we consider the possible dependence of trials. Still
other problems appear when we consider that in the real world the spectrum of situations is changing continuously and that a potentially continuous portfolio revision is
part of an optimal approach. (Actually, because of the transactions costs which occur
in practice, portfolio revision is likely to occur in discrete steps.)
The extent to which Breiman's conclusions for the finite case can be generalized in
these directions will be considered subsequently. For now we simply remark that the
possible generalizations promise to be adequate for the real world problems of portfolio selection.
Assuming this to be the case, we shall see in the next section that economists and
others now have for the first time an accurate guide for portfolio selection and revision.
8. THE KELLY CRITERION AND DEFICIENCIES IN
THE MARKOWITZ THEORY OF PORTFOLIO SELECTION
How to apportion funds among investments has endlessly puzzled economists and
decision-makers. The literature was noted for its lack of instruction in such matters.
When Markowitz' work on portfolio selection appeared, first in articles and later in
the monograph [I8], it became the standard reference.
Markowitz considers situations in which there are r alternative and, in general
correlated, investments, with the gain per unit invested of XI ' .. . , X" respectively.
(It is so much more dignified to call bets investments; we shall try to remember to do
this in this section.) One of the investments is, of course, cash. The gain is given by
X k = 0 a.s.
To select a portfolio is to apportion our resources so that fj is placed in the ith
investment. Markowitz' basic idea is that a portfolio is better if it has higher expectation and at least as small a variance or if it has at least as great an expectation and has
a lower variance. If two portfolios have the same expectation and variance, neither is
preferable. As the h range over all possible admissible values, the set of portfolios is
generated. Typically the assumptions on theh are 'i.fi = I, andfi ~ 0 for i = I, . .. , r .
--- page 106 ---

Optimal Gambling Systems for Favorable Games
79
291
If a portfolio has the property that no other portfolio in the set is preferable, then
it is called efficient. Markowitz says that the investor should always choose an efficient
portfolio. Which efficient portfolio to choose depends on factors outside the theory.
such as the investor's "needs".
The Markowitz theory has the obvious deficiency that if Ei and cr;, i = 1, 2, are
the expectation and variance of portfolios 1 and 2, then if E 1 < E2 and cri < cr~, the
theory cannot choose between the portfolios. Yet there are obvious instances where
"everyone" will choose the second portfolio over the first, such as when Fl ( x ) <
F2 ( X ) for all x. Specifically, let Xl be distributed uniformly on [1, 3], let X2 be uniformly distributed on [10, 100] and let X3 = 0 a.s. represent the possibility of holding
some of our resources in cash. Suppose Xl' X2 , and X3 are independent. Then
E 'E}; Xi = 2fl + 55f2 and cr2 'Efi Xi = 'Efi2cr/ = f~/3 + 675f~. All cash, or f3 = 1,
is an efficient portfolio since this is the unique portfolio with zero expectation. The
portfolio j~ = 1 also is efficient since this is the unique portfolio with greatest expectation. There are, in fact, infinitely many efficient portfolios. (They lie on a curve in the
11'/2 plane connecting (0, 0) and (0, I).) The theory doesn't tell us which is best,
yet 12 = I is clearly preferable to any alternative.
In the case where there are the two alternatives Xl = 0 a.s. (cash) and X2 with
E2 > 0 and (1'2 > 0, all portfolios are efficient and Markowitz' theory gives no information on which to choose. The Kelly criterion tells us to choose 12 to maximize
E log ( 1 + 12X2) and we know further from the theory of the Kelly criterion why
this choice is good. As we have seen, repeated trials of such an investment with 12
greater than the fraction Ie will lead to ruin a.s.
Remark: This incompleteness of Markowitz' theory is understandable since he only
uses probability information about first and second moments. We note though that
the examples he gives, and the real world applications, generally assume that more
detailed structure is known. Hence, it is reasonable that the criterion E log Xn , which
does use higher moment information, can provide a sharper theory.
Next consider those two-point probability distributions with masses m i located
at x j, i = I, 2, and with mean and variance 1. These are indistinguishable by Markowitz' criterion. A calculation shows, however, that for Xl defined by Xl = -J, X2 =
3/2, ml = 1/5, m2 = 4/5, the optimalfractionfi is 1 and G(ji) is -(1/5) log 3 + (4/5)
log 2. For X 2 defined by Xl = -2, X2 = 4/3, m 1 = 1/10, m2 = 9/10, we havef: = i
and Gun = -(1/10) log 4 + (9/10) log (3/2), which is smaller than Gun·
Hence if X:.
1 is the fortune after n repeated independent trials of an investor who
invests fi in X 1 at each trial and X n. 2 is the fortune after n trials of an investor who
invests in any manner whatsoever in X 2 at each trial, we have lim X:. 1/ X n• 2 = 00 a.s.
As a final example, suppose we are to apportion our resources between the foregoing Xl and X2 , which we now suppose to be independent, and cash, represented
by X3 . We impose the constraints Ii > 0, i = 1, 2, 3; II + 12 + 13 = 1, and II +
2/2 < 1. The latter constraint prevents investments where our losses exceed our total
resources. (The analysis and conclusion are essentially the same without this constraint.) The admissible portfolios are represented by the closed triangular region of
the positive quadrant bounded by the axes and the line II + 212 = 1.
We have E'L/iXi = II + Ii and, because of the independence of Xl and X2 ,
(J2'EJ;Xi =!f + !~. The efficient portfolios are the points ofthe!1.J2 plane 011 the
two closed line segments joining ( t, t) to (0, 0) and to (1, 0).
The function E log( 1+ 11 Xl +.f2X2) == G(flJ2) is given by 50 G(flJ2) =
--- page 107 ---

80
E. 0. Thorp
292
36 log (1 + 311/2 + 412/3) + 4 log ( 1 + 311/2 - 212) + 9 log ( 1 -11 +
+ 412 / 3) + log ( 1 - j~ - 212)' This function is undefined on the line joining
(0,1/3) and (1, 0). It is defined and continuous elsewhere on the triangle of portfolios
and as (/1'/2) tends to the segment from this triangle, G (/1'/2) --+ -
00. It follows
(by the continuity) that G (11,j~) attains an absolute maximum in the region of the
triangle where it is defined. We also know that any such maximum is positive. It
follows that, if an efficient portfolio maximizes G (/1'/2), then it must be a portfolio
from the interior of the segment joining (0, 0) and (1/3, 1/3). Hence the coordinates
must simultaneously satisfy the equations 0 G (/1'/2) / 011 = 0 and 0 G (/1 '/2) /
012 = O. (We note that in repeated independent trials where the investor selects an
efficient portfolio from the segment joining (1/3, 1/3) to (1,0), he will be ruined with
probability one.)
Setting 11 = 12 = t in the equations a G / 011 = 0 and a G / 012 = 0 and attempting to solve simultaneously yields, upon elimination between the two equations of the
last of the four fractions, the necessary condition -2796 + 3761 + Illt2 = O. Since
this is negative at t = 0 and t = 1, there are no roots in the interval 0 < t < 1/3.
Hence no efficient portfolio maximizes G (11'/2)'
We conclude that if X:. 1 is the fortune after n trials of a player who bets to maximize G (fl'/2) on each trial, and X n, 2 is the fortune of a player who chooses any
efficient portfolio on each trial, then lim X:, 1/ X n, 2 = 00 a.s. Furthermore, the
Kelly investor will reach a fixed goal x in less time, asymptotically as x --+ 00, than a
Markowitz investor.
The Kelly criterion should replace the Markowitz criterion as the guide to portfolio selection.
REFERENCES
[1] Baldwin, Cantey, Maisel, and McDermott (1956). The optimum strategy in blackjack, J. Amer.
Statist. Assoc., 51, 429-439.
(2] Bellman, R., Kalaba, R. (Sept. 1957). On the role of dynamic programming in statistical communication theory. IRE Trans. of the professional group on information theory, IT-3 no. 3, 197 -203.
(3) Breiman, L. (1961). Optimal gambling systems for favorable games. Fourth Berkeley Symposium
on probability and statistics, J, 65-7B.
[4] Coddington, E. A., Levinson, N. (1955). Theory of Ordinary Differential Equations. New York,
McGraw-Hill.
[5) Cootner, P. H., editor (1964). The Random Character of Stock Market Prices. The M.LT. press.
[6) Dubins, L., Savage, L. (1965). How to Gamble if You Must. New York, McGraw-HilI.
(7) Dunnington, G. Waldo (1955). Carl Friedrich Gauss, Titan of Science. New York, Hafner.
[B) Feller, W. (1957). An Introduction to Probability Theory and Its Applications, Vol. I, Revised.
New York, Wiley.
[9] Feller, W. (1966). An Introduction to Probability Theory and Its Applications, Vol. 11. New York,
Wiley.
(lO) Ferguson, T. S. (1965). Betting systems which minimize the probability of ruin. J. Soc. Indust.
Appl. Math., 13, no. 3.
[11] Foster, F. G. (1964). A computer technique for game-theoretic problems. 1. Chemin-de-fer
analyzed. Comput. J., 1, 124--130.
[12] Kassouf. Sheen T. (1965). A Theory and an Econometric Model for Common Stock Purchase
Warrants. Ph. D. Thesis, Columbia University, New York.
[13] Kelly, J. L. (1956). A new interpretation of information rate. Bell System Technical Journal, 35,
917--926.
(14) Kemeny, J. G., Snell, J. L. (1957). Game theoretic solution of baccarat, Amer. Math. Monthly,
114, no. 7, 465-9.
[15] Kendall, M. G., Murchland, J. D. Statistical aspects of the legality of gambling, J. Roy. Statist.
Soc. Ser. A. To be published.
--- page 108 ---

Procs. o/the Business and Economics Sect. o/the Amer. Stat. Assoc., 215- 224 (1971)
81
7
PORTFOLIO CHOICE AND THE KELLY CRITERION
Edward O. Thorp, University of California at Irvine:O::
I.
Introduction.
The Kelly (or capital growt!.»
criterion is to maximize the expected value
E log X of the logarithm of tr.e wealth random
variable X.
Logaritlunic utility has been widely
dis c ussed since Daniel Bernoulli introduced it
about 1730 in connection with the Petersburg
galne [3, 28].
However, it was not until certain
mathclnatical results were proven in a limited
setting by Kelly in 1956 and then in much more
general setting by Breiman in 1960 and 1961
thai logarithmic utility was clearly distinguished
~. its properties from other utilities as a guide
to portfolio selection.
(Sec also [2, 4, 15], and
the very significant paper of Hakansson [II). )
Suppose for each timp. period (n ;:.1, 2, ... )
there are k investment opportunities with results per unit invested denoted by the family of
random variables Xn,l'Xn,2"" ,Xn,k' Suppose
also that these random variables have only finitely many distinct values, that for distinct n
the farrdlies are independent of each other, and
that the joint probability distributions of distinct
farnilies (as subscripted) are identical. Then
Breiman's results imply that portfolio strategies
1\ which Inaximize E log Xn , where Xn is the
wealth at the end of the n-th time period, have
the fol1owing properties:
Property 1.
(Maximizing E log Xn asymptotic:c.:tlly maxiInizcs the rate of asset growth. ) If,
for each tim~ p~riod, two portfolio managers
have the same falnily of investmt'nt opportunities
or investn1.ent universes, and one uses a strategy
1\':: maximiz.ing Elog Xn whereas the other uses
an 'lessentially different l1 (1. e., ElogXn(II.*)-
E log Xn(/\)"~) strategy 1\, then lim XJI\*)/Xn(I\)" =
almost surely (a. s.).
Property 2.
The expected time to reach a
fixed preassigned goal x is, asymptotically as
x increases I least with a strategy maxhni zing
ElogX;,.
The qualification '1essentially different" conceals subtleties which are not generally appreciat~d. For instance [11], which is close in method
to this article, and whose conclusions we heartily
endorse, contains nUITlCroUS rnathematically
incorrect statemp.nts and several incorrect conclusions, mostly from overlooking the requiremp.nt 11essentially different. 11
We intend to
present a detailed analysis elsewhere and only
indie.,te the problem here: If Xj = Xj!Xj-l' then
even though E log Xj>O for all j it need not be the
ca.'>c that P(lim Xn =00) = 1. "In fact, we can have
215
(just .as in the case of Bernoulli trials and
E log Xj = 0; sec (26)) P(lim sup Xn = m) = I and
P(lim inf Xn = 0) = I (contrary to [11, p. 522, eq.
(18)) and following assertions) . Similarly, when
Elogxj<O for all j we can have these alternatives instead of P(lim Xn = 0) = 1 (contrary to [11,
p. 522, eg. (17)] and the following statemo.,tts;
footnote 1 is' also incorrect. )
Note (6) that with the preceding assumptions,
there is a fixed fraction strategy /\ which 111:lximizes E log Xn .
A fixed fraction strategy is one
in which the fraction of wealth f
. allocated to
n,)
investmp.nt Xn,j is ~ndependent of n.
We emphasize that Breiman's results can be
extended to cover many if not nlost of the more
cornplicated situations which arise in real world
portfolios. Specifically, the number and distributiqn of inve stmnnts can vary with the tinlt~
period, the randon1. variables need not be finit.e
or even discrete. and a certain amount of dependence can be introduced between the investm(~:1t
universes for different time periods.
\Ve have
used such extensions in certain applications (e.g.,
[25; 26, p. 287]).
We consider almost surely having more
wealth than if an l1essentially diffcrent l1 strategy
were followed, as the desirable objective for
most institutional portfolio managers.
(It also
see:ms appropriate ·for w.aalthy families who
wish mainly to accumulate and whose consUlnption expenses are only a sInall fraction of their
total wealth.) Property 1 says that maximizing
E log Xn is a recipe for approaching this goal
asymptotically as n increases. This is Gar
principal justification for selecting E log X as
the guide to portfolio selection.
In any real application n is finite, the limit
is not reached, and we have P(Xn(R')/Xn(A»I+ M)
=l .. qn,II.,M) where & ...... 0 as 0 ...... (1). M>O is
given, N'Iis the strategy which maximizes
ElogXn · and A is an "essentially different" strategy.
Thus in any application it is important to
have an idea of how rapidly· e -to O.
Work needs to
be done on this in order to reduce E log X to a
guide that is useful (not merely valuable) for
portfolio manage.rs. Some illustrative examples
for n=6 appear in[ll].
Property 2 shows us that nUl.xiITIizing E log X
also is appropriate [or individua~s who have a set
goal (c. g., to becorn0. a millionaire).
Appreciation of the compelling properties of
the Kelly criterion may have been impeded by
Reprinted from the 1971 Business and Economics Statistics Section Proceedings
of the American Statistical Association
--- page 109 ---

82
certain l1.1.iSlll'ldcrstandings about it that persist.
in the literature of mathematical economics.
The first misunderstanding involve~ failure
to distinguish among kinds of utility theories .
\Ve COlnpare and contrast three types of utility
theories: (1) descriptive, where data on observed
behavior is fitted mathem.atically.
Many different utility functions might be needed', corresponding to widely varying circumstances,
cultures, or behavior typesl ; (2) predictive,
which "explains" observed data: fits for obsCl"vf'd data arc deduced from hypotheses, with
the hope future data will also be found to fit.
Many different utility functions may be needed.
corresponding to the many sets of hypotheses
that lllay be put forward; (3) prescriptive (also
called normativeL which is a guide to behavior,
i. e., a recipe f;r optimally achieving a stated
goal.
It is not necessarily either descriptive or
predictive nor is it intended to be so,
\Ve use logaritrunic utility in this last way,
and nHlch of the n1isunderstanding of it comes
frol11. those who think it is being proposed as a
descriptive or a predictive theory.
The E log X
theory is a prescription for allocating resourCl~5
so as to (asymptotically) maximize the rate of
growth of as scts.
Another .iobjcetion" voiced by SOrnf! ecollOn1:'sts to E log X and, in fact to all unbounded
utility functions, is that it doesn't resolve the
(g(.'ncralized\ P(~ter5burg paradox.
The rebuttal
is blunt and pragmatic: The generalized Petersburg paradox dues not arise'in the rea.l world
btcause anyone real world random variable is
bourdcd (as is any finite collection). Thus in a.ny
real application the paradox does not arise ..
To insist that a utility function resolve the
paradox is an artificial requirement, certainly
pern1is sible, but obstructive and tangential to
the goal of building a theory which is also a
practical guide.
2. Samllelson's objections to logarithmic utility.
Samllelson [21, pp. 245-6; 22, pp. 4-5] says that
repeatedly authorities [S, 6,14, IS, 30] ..... have
proposed a drastic simplification of the decision
problen1 whenever T [the number of investmcnt
periodsj2 is large.
Rule: Act in each. period to maximize the
geol11etric Jl1l.'an or the expected value of log xt '
The plausibility of such a procedure Cornp.s
fr0111 the recognition of the following valid asyn1ptoLic result.
Theorem: Acting to ma.ximize the geometric
lnl~il.n at ~very step will if the period is "suffici(!mly long, II "aln"lOst certainly"3 result in
hj gilt' r tern"linal wealth and terminal utility than
(rOlli <Lny other decision rule, ": ..
IIFrol11. thi s indisputable fact. it is apparently
tl"ll~pljng to believe in the truth. of the following
f"d~>\· corollary~
False corollary: If maximiz~ng -the geo-
216
E. 0. Thorp
metric mean alnlost certainly leads to a bl."ttl "
outcomc, then the expc.cted value utility of it::;
outcomes exceeds that of any other rule, pro·
vided T is sufficiently large. It
Samuelson then gives count.cr(~xafnple5 t ( )
the corollary,
Wt.~ heartily ag~'ec that the COl"l.!-
lary is false.
In fact we had already sho'wn tin ··
for one of the utilities Salnllelson uses, for \Vl'
not.ed [26] that in the case o( Bernoulli u·i"l.
with probability 1/2<p< I of success, one;- shOUI'i
commi.t a fraction w == 1 of his capitn.l at. each
trial to maximize expected final gain E Xn (page
283; the utility is U(x) ::::x) whereas to InaxiInizl!
E log Xn he should commit w = Zp - I of his capital at each trial (page 285, Theorem -I).
The statC111ents v.·hieh we have seen in print
supporting this "false corollary" are by Latan~
[IS, p. lSI, fn. 13j as discussed in [ZI, p. 2-15,
fn. Ill. and Markowitz [16, pp. ix-x].
Latanc
may not have fully supported this coroJlary (or
he. adds the qualifier " . .. (in so far as certain
approximations are permissible) ... fl.
That thcrt.' were or are adherents of the
"false corollary" seenlS p\lzzling in viev.' of tIl<:
following forrrlll.lation.
Consider a T stage ~r..
vcstn1.cnt process. At ~ach stage we allocate our
resources among the available invcsln1.('nts. For
each sequence A of all,?cations which Wi! choos,- _
there is a corresponding terminal probability
distribution F* of assets at the con1pletion of
stage T. For each utility function U(·} J
~on·
sider those allocations A:;:(U) which maxinlize
the expected value of terminal utility
J U(x) dF:(X).
Assum~ sufficient hypotheses 010
U and the set of F: so that the integral is de -
fined and that furthermore the maximizing al1ocation A';:(U) exists.
Then Samnelson says that
A"'(log) is not in general A"(U) for other U.
This seems intuitively evident.
Even more seems strongly plausible: that if
Ui ' and Uz are inequivalent utilities then
J UI(x) d F~(X) and J U2 (x) dF:(X) will in general
be m~ximized for different F:. (Two utilities
UI ai,d .U? are equivalent if and only if there are
constants a and b such that UZ(x) = aUI(x) + b,
a> 0; otherwise VI and Uz are inequivalent.) In
this connection we have proved:
Theorem: Let U and V be utilities defined
and differentiable on (0, m), with U'(x) and V'(.'I
positive and. strictly decreasing as x increa.!W5,
Then if U and V are inequivalent, there is a
one period lnv·estment setting such that U and V
have distinct optimal strategies. 4
All this is in the nature of an aside for
Samuelson's correct criticism of the "false
--- page 110 ---

Portfolio Choice and the Kelly Criterion
corollaryH docs not apply to our use of logarithmic utility. Our point of view is: if your goal i"s
property 1 or property 2 , then a recipe for
achieving either goal is to n"laximize E log X .
These properties distinguish log from the prolixity of utility functions in the literature .
Furthermore, we consider these goals appropriate for n1.any (but not all) investors . Investors
with other uti1it.ie~ ;;-with goals incompatible
with logarithn1ic utility, will of course, find it
inappropriate .
Property I implies that if It' maximizes
E log Xn{/\) and A' is "essentially different, "
then Xn(Ir"') tends almost certainly to be better
than Xn(A') as n""'. Samuelson [21. p. 246).
apparently referring to this, says a!t~r refuting
the !lIaIse corollary": "Moreover, as 1 sho'wed
elsewhere [20. p. 4). the ordering principle of
selecting between two actions in terms of which
has the greater probability of producing a higher
result does not even possess the property of being transitive . . . . we could have wt,:*t; better than
\Y)~;:', and
Wi,l~:t better than w*, and also have. w::t
better than wi,'*:';. II
For SOlne entertaining e xamples, ·see the
discussion of no.n-transit1.vc dice in [91 . (Consider
the dice with equiprobable faces numbered as
follows: X ~ -(3.3.3.3,3.3); y ~ (4.4,4.4.1.1); Z ~
(5.5.2,2.2..2) . Then P(Z>Y) ~ 5/9. P(y>X) ~ 2/3,
P(X>Z) ~ 2/3.) What Samuelson does. not tell us is
that the property of producing a high;;-result
ahnost certainly, as in property 1, is transitive.
If 'wc have w ;;n:,::= >w~q almost certainly, and
w~;t~' >w::': alnlost ccrtainly, then we must have
w*~"'.: >w);t almost certainly.
One might· object [20. p . 6J that in a real investrnent sequence the limit as n -+(0 is not
reached . Instead the process stops at some finite
N. Thus we do not have XJI(o') > Xn(A') almost
certainly. Instead we have P(Xn(N'»Xn(A')) ~ 1- £N
where ~"'O as N-t co , and "transitivity can be
shown to fail.
This is correct. But an approximate form of
transitivity does hold: Let X, Y.Z be random variables with P(X>Y)~I-€I
' P(Y>Z)=l-'2. Then
P(X>Z);, 1- (£1 + '"2'. To prove this, let A be the
event X>Y, B be the event Y>Z. and· C be the
event X>Z. Then P(A)+P(B) ~ P(AUB)+p(AnB)
~ l+p(AnB) . But AnBCC so PIC) ;o;p(AnB)
;0; P(A)+P(B) - I. i. e .• P(X>Z);o; I - ('I + '2.).
Thus our approach is not aHectcd by the vartous Samuelson objections to the uses of logarithn1ic utility.
Mark~witz [16. pp. ix-x] says .... : inI955-56.
I concluded ... that the investor' who is currently
r e invC'sting everything for lithe long run" .should
maxilnize the expected yalue of the logarithm of
217
83
wealth. 11 (This assertion s e ems to be regal"Clle s s
of the investor's utility and so indicates b<:li e f in
the Bfalse coronary ." ") Mossin [181 and Sannlclson
[20] "II ... have each shown that this concluf>ion i::;
not true for a wide range of [utility] functions ...
The fascinating ~1ossin-Samuelson result, CO!Y\-
bined with the straightforward arguments supporting the earlie r conclusions, sE'.emcd pat'aduxical at first. 1 have since returned to the view of-
Chapter 6 (concluding that: for large T. the
Mossin-Samuelson Inan acts absurdly ... . I '
Markowitz says here, in effect, ,that alternate
utility functions (to log) are absurd , This position
is unsubstantiated and unreasonable.
He continues " ... like a player who would pay
an unlimited amount for the St. Petersburg
game ... ... If you agre~ with us that the St. Petersburg galYle is not realizable and may be ignored
when fashioning utility theories for the real 'world,
then his continuation I I •• , the tern1inal utility'function must be bounded to avoid this absurdity; .. , ! '
does not follow .
Finally, .J\1arkowitz says " .. . and the argl.: ~
ment in Chapter 6 applies when utility of tern1inal wealth is bounded." If he means by this that
the "false corollaryll holds if we restrict ourselves to bounded utility functions, then he is
mistaken. Mossin [18] already showed that the
optimal strategies for logx and xY/y, yt 0, are
fixed fraction fo r these and only these utilitie s.
Thus any bounde d utility besides x'l/v. 1'<0. \'."ill
have optimal strategies which are not fixed frac.-
tion. hence not optimal for logx .. ""Sa";nuelson[22]
gives counterexan1ples which include·. the bounded
utilities xY/y. Y < O. Since Mossin assumes U"
exists and our theorem only aSSUlnes that U'
exists, it provides additional counterexao1ples.
3. An outline of the theory of logarithmic _utility
as applied to portfolio selection. 'The sim?lest
case is Bernoulli trials with probability p of
success, O<p<l. The unique strategy which n)aximizes E log Xn i s to bet at trial n the fixed fraction f" ~ P - q of total current wealth Xn;1
if
p>l!2 and to bet nothing otherwise.
To o1aximize E log Xn is equivalent to nlaximizing Elog[X IX ]Im ".G(f). which we call the
n
0
(exponential) rate of growth (pel" time period). It
turns out that for p >-li2. G(f) has a unique positive maxinlun1 at P:< and that there is a critical
fraction fc ' O<f':'<fc<l. such that G(fc)oO .
G (f»0 if 0 < f < fc' G (f)<0 if fc < f ~ I (we a s sumo
IIno margin"; the case with l'nargin is sirr\ilar). If
f<fc ' Xn -tee a .s.; if f= fe' lim sup ~ = +(0 a.s .•
and liminfX ~ 0 a .s . ; if f>f • limX ~ 0 a.s .
11 .
c
n·
(llruinl!~.
Bernoulli trials exhibit many of the features
--- page 111 ---

84
of the following more general case. Suppose we·
have at each trial n = 1, 2, ... the k investlnent
opportunities Xn,l,Xn,2' ... ,Xn,k and that the conditions of property 1, section 1 are satisfied.
This means that the joint distributions of
{X . ,X ., ... ,X . j"l are the same for all n J for
\. n.l1 n,lZ
n,lj
each subset of indices l;;il<i2<· ··<i/k. FUrthermore f?cm.I' .. . • Xm •k } and {Xn • l •...• Xn •k} are
independent when m * n, and all random variables
X .. have only a finite number of distinct values.
1,)
Thus we have in successive time periods repeated independent trials of lithe sanle" investment
universe.
Since Breiman has shown that there is for
this case an optim.al fixed fraction strategy
It' = (li.*' .... ~). we will have an optimal strategy
if we find a strategy which maximizes ElogXn in
the cIa S 5 of fixed fraction strategie s.
Let "= (fl ... · .~) be any fixed fraction strategy. We assume that 1+· .. +~~1 so there is no
borrowing, or margin. The margin case is similar (the approach resembles [23]). Using the
concavity of the logarithm, it is easy to show
(see below) that the exponential rate of growth
E log [Xn(A)1X0 ]1In = GUi • .. ·.V is a concave function of (fl ... · .~). just as in the Bernoulli trials
case. The domain of G(f) in the Bernoulli trials
case was the interval [0.1) with G(f) 1-'" as f"l.
The domain in the present instance is analogous.
First, it is a subset of the k dimensional simplex
1.0 = {(fl·· .. ·F ~+ ... +pl; 1 ;;o ..... ~ ;;o} .
To establish the analogy further. let R
.
J
= Xn,j -1 , j = 1, ... ,k, be the return per unit on the
i-th investment opportunity at an arbitrary time
period n. Let the range of R be fro I; ... ; r .. }
J
1: J.
J.1j
and let the probability of the outcome ['\ =rl 'ml
and R =r
and " , and R = r
I be
2 2.m2
-k k.mkJ
p
. Then ElogX IX I =G(fi' ···.V
m l .m2 ..... "\
n n-
= l: ~
log (l+f r
+ ... + f r
\
mi' .... "\
I 1."1
K k.,,\ /
I;;ml ;;\; ... ;I;;,,\;!;\}, from which the concavity
of G(fl . .. .. ~' ) can be shown. Note that G(fl ••• · .~)
is defined if and only if 1+ fl 'I. "1 + ... +~rk.,,\ >0
for each set of indices ml ... ·.Il).. Thus the domain of G(f1 ... · .~) is the intersection of all
these open half-spaces with the k-dimensional
216
E. 0. Thorp
simplex ~. Note that the dOlnain is convex and
includes ~ll of 1.0 in some neighborhood of the
origin. Note too that the domain of G is all of ~
if (and only if) R/ -I for all j. i.e . • if there is
no probability of total loss on any investment.
The domain of G includes the interior of \
if
R;; -I. Both domains are particularly simple
J
.
and most cases of interest are included.
If fl' .... ~ arc chosen so that
I+fr
+ .. ·+fr
;;0 for some in ... ·.m.
I l.ml
K k.,,\
I
k
then P(fIXn •1 + ... + ~Xn.k;; 0) = € > 0 for all nand
ruin occurs with probability I . .
Computational procedures for finding an optimal fixed · fraction strategy (generally unicjue in
our present setting) are based on the theory of
concave (dually. convex) functions [29J and will
be presented elsewhere . (As Hakansson [11, p .
552] has noted. " ... the computational aspects of
the capital growth model arc [presently) much
less advanced" than for the Markowitz model. J
The theory lnay be extended to n10re general
randoITl variables and to dependence between different time periods . Most important, we may
include the case where tht! investment universe
changes with the time period, provided only that
there be some mild regularity conditions on the
X ..• such as that they be uniformly a . s. bounded
1,)
and that they do not tend to 0 uniforml y as i" ~ .
(See [IS). and the generalization of the Bernoulli
trials case as applied to blackjack in [26).) The
techniques rely heavily on those used to generalize the law of large numbers.
Transactions costs, the use of margin, and
the effect of tax'es can be incorporated into the
theory. Bellman's dynamic programming method
is used here.
The general procedure for developing the
theory into a practical tool imitates Markowitz
[16]. Markowitz requires as inputs estimates of
the expectations, standard deviations, and covariances of the Xi,j' We require joint probability distributions. This would seem to be a
much more severe requirement, but in practice
does not seem to be so [16. pp. 193-4. 198-201).
Among the actual i;"puts which Markowitz
chose were (I) past history [16. ex .• 8-20). (2)
probability beliefs of analysts (pp. 26-33). and
(3) models, most"notably regression models, to
predict future performance from past data (p. 33 •
. pp. 99-100). In each instance one can get enough
additional information to estimate E log (XnlXn _1).
There are, however, two great difficulties
which all theories of portfolio selection have, including ours and that of Markowitz. First, there
seems to be no established method for generally
--- page 112 ---

Portfolio Choice and the Kelly Criterion
predicting sC"curity prices which gives an edge of
even a few pc 1" cent. The random walk is the best
model for security prices today. (See [7, 10j.)
The second difficulty is that for portfolios
v ... ith 11lany securities the volume of inputs called
for is prohibitive: for 100 securities, Markowitz
requires 100 expectations and 4950 cQvar.iances;.
and our theory requires somewhat more information . Although considerable attention has been
given to finding condensed inputs that can be used
instead, this aspect of portfolio theory still
seems unsatisfactory.
In the fifth section we will show how both
the se difficulties were overcome in practice by
an institutional investor. That investor, guided
by the Kelly criterion, then outperformed for
the year 1970 everyone of the approximately400
Mutual Funds listed by the S & P stock guide!
But fir.t we relate our theory to that of
Markowitz.
4. Relation to the Markowitz theory; solution to
problems therein. The most widely used guide
to portfolio selection today is probably the Markowitz theory . The basic idea is that a portfolio
PI is supedor to a portfolio Pz If the expectation ("gain'l) is at least as great, i.e., E(P1)
1;E(PZ) and the standard deviation ("risk") is no
greater, i.e., a{PI)~a(pZ)' with at least one inequality. This partially orders the set (} of portfolios. A portfolio such that no portfolio is
superior (i.e., a maximal portfolio in the partial
ordering) is called efficient. The goal of the
portfolio manager is to determine the sct of efficient portfolios, from which he then makes a
choice ba sed on his needs.
This is intuitively very appealing: It is based
on standard quantities for the securities in the
portfolio, namely expectation .. standard deviation,
and covariance (needed to compute the variance
of the portfolio from that of the component securities). It also gives the portfolio manager ''choice.1I
As Markowitz [16, Chapter 6) has pointed out,
the optimal Kelly portfolio is approximately one
of the Markowitz efficient portfolios under cer -
tain circmTIstances. If E= E{P) and R= P-I is
the return per unit of the portfolio P, let log P
= log (ltR) = log ( (ltE)+ (R - E)). Expanding in
Taylor's series about ItE gives log P= 10g(I+E)
+ (R-E)/{l +E) - (R_E)Z /2{l +E)Z +higher order terms.
Taking expectations and neglecting higher order
terms gives ElogP= 10g{l+E)- J(P)/2{l+E)Z.
This leads to a simple pictorial relationship
with the Markowitz theory. Consider the E-a
plane, and plot (E(P), a(P)) for the efficient
portfolios. The locus of efficient portfolios is a
convex non-decreasing curve which includes its
endpoints (Figure I).
Then constant values of the growth. rate
219
85
FIGURE 1.
GROWTH RATE G (RETURN
RATE' R) IN THE E-a PLANE ASSUMING
THE VALIDITY OF THE POWER SERIES
APPROXIMATION.
1.00
.90
and A.eli-I
.80
.7
.60
.W
AO
.50
.60
.70 '
R<49%
R'6~%
G=ElogP approximately satisfy G=log{l+E)
_ aZ(p)/2{l+El. This family of curves is illustrated in Figure I and the {efficientj portfolio
which maximizes logarithmic utility is (approximately) the one which lies on the greatest G
curve. Because of the convexity of the curve of
efficient portfolios and the concavity of the G
curves, the (E, a) value where this occurs is
unique .
The · approximation to G breaks down badly
in some significant practical settings, including
that of the next section. But for portfolios with
large numbers of "typical" securities, the a"pprax ...
imation for G will generally -provide an efficient
pot.'tiolio which approximately maxilnizes asset
growth. This solves the portfolio manager's
problem of which efficient portfolio to choose.
Also, if he repeatedly chooses his portfolio in
successive time periods by this criterion he wi ll
tend to nlaximize the rate of growth of his as:i (' l s,
i.c.,. nlaximize "performance. II We see also that
in this instance the problem is reduced to that. of
finding the efficient portfolios plus the easy step
--- page 113 ---

86
of using Figure 1. Thus if the Markowitz theory
can be applied in practice in this setting, so can
our theory.
We have already remarked on the ambiguity
of the set of efficient portfolios. and how our
theory resolves them .. To illustrate further that
such ambiguity repre.sent~ a defect in the Markowitz theory, let X1 be uniformly distributed over
[1.3]. let Xz be uniformly distributed over [10.
100], let cor(~.Xz)= 1. and suppose these are
the only securities. Then ~ and Xz are both
efficient with 01 < 0z and El < ~ so Markowitz'
theory does not choose between them. Yet
"everyone ll would choose Xz over ~ because the
worst outcome with Xz is far better than the best
outcome from ~. (We presented this example in
[Z6). Hakansson [11] presents further examples
and an extended analysis. He formalizes the idea
by introducing the notion of stochastic dominance:
X stochastically dominates Y if P(X~Y) = 1 and
P(X>Y) > O. It is easy to prove the Lemma: An
E log X optimal portfolio is never stochastically
dominated. Thus our portfolio theory does not
have this defect. )
There are investment universes ()\" .. JXn~
such that a unique portfolio P maximizes ElogP
yet P is not efficient in the sense of Markowitz .
Hence choosing P in repeated independent trials
will outperform any strategy limited to choosing
efficient portfolios. In addition. the optimal
Kelly strategy gives positive growth rate, yet
sOlne of the Markowitzefficient strategies ·give
negative growth rate and ruin after repeated
trials. We gave such an example in [Z6] and
another appears in [ll]. See also [ll. pp. 553-4]
for further discussion of defects in the Marko ..
witz model.
5.
The theory in action: re suIts for a real institutional portfolio. The elements of a practical
profitable theory of convertible hedging were published in [Z7]. Thorp and I<assouI indicated an
annualized return on investments of the order of
Z5% per year . Since then the theory has been
greatly extended and refined with most of these
new results thus far unpublished.
The historical data which has been used to
develop the theory includes well over 100.000
observations of convertibles.
A convertible hedge transaction generally
involves two securities, one of which is conver -
tible into the other. Mathematical price relationships exist between pairs of such securities.
When one of the pair is comparatively underpriced.,
a profitable convertible hedge may be set \Ip by
buying the relatively underpriced security and
selling short an appropriate amount of the relatively overpriced security.
220
E. 0. Thorp
The purpose of selling short the oVf:rpricl::d
security is to reduce the risk in the pOSItion.
Typically, one sells short in a single hedge fr{)m
50% to 125% as much stock (in "share equivalents") as is held long. The exact proportions
depend on the analysis of the specific situation;
the quantity of stock sold short is se lected to
minimize risk. The risk (i.e., change in asset
value with fluctuations in market prices) in a
suitable convertible hedge should .be much less
than in the usual stock markjat long positions.
The securities involved in conve rtible hedges
include comlnon stock, convertible bonds, convertible. preferreds, and common stock purchase
warrants. Options such as puts, calls, and
straqdles may replace the convertible security.
For this purpose. the options may be either
written or purchased .
The theory of the convertible hedge is highly
enough developed so that the probability characte ristic s of a. single hedge can be worked out
based on.an assumption for the underlying distr·ibution of the comlnon . (Sometimes even this
can almost be dispensed with! See [27. App. CJ . )
A popular and plausible assumption is that the
future price of the common is log nor mally distributed about itst current price, with a trend and
a variance proportional to the tin1e . Plausible
estimates of these paran1eters are readily obtained. Furthermore . it turns out that the return
from the hedge is comparatively insensitive to
changes in the estimates for these parameters.
Thus with convertible hedging we fulfill two
important. conditions for the practical application
of our. (or any other) theory of portfolio choice:
(1) We have identified investment opportunities
which arc markedly superior to the usual ones .
Compare the return rate of Z0'70-25% per year
with the long term rate of 8'70 or so for listed
common stocks. Further I it can be shown that
the risks tend to be much less. (2) The probability inputs are available for computing
O(fl • ...• ~).
On November 3, 1969, a private institutional
investor decided to commit all its resources to
convertible hedging and ·to use the Kelly criterion
to allocate its assets. The performance record
appears in the Table.
The market period covered included one of
the sharp~st falling markets as well as one ofthe
sharpest rising markets (up 50% in 11 months)
since Wor.ld War II. The gain was +16.3% for the
year 1970. which outperformed all of the approximately 400 Mutual Funds Listed in the S 8< P
stock guide. Unaudited figures show that gains
were achieved during every single month.
The unusually low risk in the hedged posi -
tions is also indicated by the results for the ZOO
completed hedges . There were 190 winners . 6
breakevens, and 4- losses. The losses as a per
~ent of the long side of the specific investment
--- page 114 ---

Portfolio Choice and the Kelly Criterion
87
TABLE - PERFORMANCE RECORD
Change
Elapsed
·Growth Rate
To Date
Time
Date
('/0)
(months)
11-
3-69
0.0
0
12-31-69
+ 4.0
2
9-
1-70
+ 14.0
10
12-31-70
+21.0
14
6-30- 71"
+ 39.9
20
Assets on 7- 1-71 were 5.2 million.
* Preliminary-unaudited .
+ DJIA = Dow Jones Industrial Average.
++Compound growth rate, annualized.
ranged from I '70 to 15%.
To Date
('70)++
+26.8
+ 17.0
+ 17.7
+22.3
A characteristic of the Kelly criterion is
that as risk decreases and expectation rises,
the optimal (raction of assets to be invested in
a single situation may become "large." On several occasions', the institution, discussed abotJ'e'
invested up to 30% of its assets in single hedge".
Once it invested 150% of its assets in a single
arbitrage. This characteristic of Kelly portfolio strategy is not part of the behavior of most
portfolio Inanagers.
To indicate the techniques and probhnns, we
consider a sitnple portfolio with just one convertible hedge. We take as our example Kaufman
and Broad common stock and warrants. A price
history is indicated in Figure 2.
Price data shows that W= .455S is a reasonable fit for S;§38 and that \V = S _ 21.67 is a
reasonable fit for S ~ 44. Between S = 38 and
S=44 we have the line W=.84S-15.5. For simplicity of calculation we replace this in our illustrative analysis by W= .5S if S;:;44 and W=S- 22
if S ~44. The lines are also indicated in Figure 2.
Past history at the time the hedge was instituted in late 1970 supported the fit for S;:; 38.
The conversion feature of the warrant ensured
W~S- 21.67 until the warrant expires . Thus
W= S- 21.67 for S~44 underestimates the price
of the warrant in this region. Extensive historical studies of warrants [12 , 13, 24, 27] show that
the past history fit would probably be maintained
until about two years befoloe expiration, i.e., until about March, 1972. Thus it is plausible to
assun1e that for the next 1.3 years S may be
roughly approximated by W = .5S for S;:; 44 and
W = S - 22 for S 1; 44 .
Next we aSSUJne that St' the stock price at
time t >0 years after .the hedge was initiated, is
lognor mally distributed with density
221
DJIA
Starting
Gain Over
Closing
Chg.
Even With
DJIA
DJIA+
('/0)++
DJIA+
(%)
855
0. 0
855
0.0
800
- 6.3
889
+ 10.3
758
-11.3
974
+ 25.3
839
1.8
1034
+ 22.8
891
+ 4 .2
1196
+ 35.7
r::-: -1
[
2
2]
t (x)= (xo,,2n)
exp -(Iogx-IJ) 120 ,hence
t
2
mean E(St) = 1xp(lJ+0 /2) and standard deviation
O(St) = E(St) (eO -I J12. The functions 1.1 "U(t) and
0" oCt) depend on the stock and on the time t. If
t is the tin"le in years until St is realized, it is
plausible to assume U(t) = log S +mt and O(tr = a2t,
o
where So is the present stock price and n1. and a
are constants depending on the stock. For a detailed discussion, see [I, 19].
Then E(S)=S exp[(m+a2/l)t] and a mean int
0
crease o'f 10%/yea~ is approximated by setting
m+}/l = .1 . If we estimate} from past price
changes we can solve for m . In the case of
Kaufman and Broad it is plausible to take 0;'.45
whence }= ,}o, .20. This yields m,. O. We then
find O(St) = .5250 •
It is by no means established that the lognorm~l model is the app·ropriate one for stock
price series [7, 10]. However, once we clarify
certain. general principles by working through
our example on the basis of the lognormal model,
it can be shown that the results are substantially
unchanged by choosing instead any distribution
that roughly fit. observation!
For a time of one year, a computation shows
the return R(S) on the stocl< to be +10.5%, the r("!-
turn R(W) on the warrant to be +34.8%, O(S) = .52.
cr(W) = . 92 I and the correlation coefficient
cor(S, W) = .99. The difference" in R(S) and R(W)
shows that the·warrant is a nnlch. better buy than
the comnlono Thus a hedge long warrants and
short common has.a substantial positive expectation. The value cor(S, W)= .99 shows that a
--- page 115 ---

88
E. 0. Thorp
FIGURE l. PRICE HISTORY OF KAUFMAN AND BROAD COMMON, S, VERSUS THE WARI{ANTS, W.
The points moved up and to the right until they
reached the neighborhood of (38, 17). At this
point a 3:2 hedge (15,000 warrants long,
11,200 common short) was instituted.
As the points continued to move up
and to the right during the next
few n'lonths , the position was
closed out in stages with the
final liquidation at about
(58, 36).
2
w
25
hedge corresponding to the best linear fit of W
to S has a standard deviation of approximately
(1- . 99)1/2= . 1 which suggests that o(P) for the
optimal hedged portfolio is probably going to be
close to .1. The high return and low risk (or
the bedge will remain, it can be shown, under
wide variations in the choice of m and a.
To calculate the optimal mix of warrants
long to common short we Inaximize G(fl'~)
= E log (I +)S+~ W) . The detailed computational
procedures are too lengthy and involved to be
presented here . We plan to present them
elsewhere.
Our instit\ltional investor considered positions already held, some of which might have to
be closed out to release a s sets, and also other
current candidates for inve stment. The decision
was made to short COnllTIon and buy warrants ill
the ratio of three shares to four. The initial
Jnarket value of the long side was about 14% of
assets and for the short side about 20% of assets
The net profit, in te rms of the initial nl~rket
value of the long side, was about 20 ~o in six
months . This resulted fron1 a 'move in the
222
35
w·s
40
.
E{Sll,; <8.63
WIS, ) i. 29.66
Tc)'111S of warrant : 1 \va r r anl
+ $21 . 67 .... I sha r e com nion
stock un til 3-1-74 . Full p r 0 -
tcc tion again s t diluti on .
The
con'rany has thf! right tl) r t"!ou ce
the e xerc i se pl'ice fOl" lC'nl por a ry periods ; 750,OOO ... n i !Tt.ulb ;
and 5, 940,000 conunon out.
standing . COlllmon dividends
Q .05 ex 10-26-70 .
comlnon frail,} about 40 to a l nlost 60,
6. Cdntluding rema r ks , As remarked a bo .... e . we
do not propose logarithnlic utility a s dc ::-. ~~ riptiv e
oC actual invcstJne nt be havior, nor do we be li e ve
,anyone utility fun c tion could suffi ce . It wou ld be,
o! interest, howe ve r, to have eln pirkc:d c-..tide nc:e
showing areas of b e havio r which are cha.rac terized adequately b y logarithm ic utility, Neitl: c rdo
we intend Ibgarithmic utility to be prcdictivl!;
again, it would be of inter e st to know what it
does predict.
We only propose the theory t.o be nonn ative
or prescript'ivc, and only for those in. stitu tion s,
groups, or individuals who s e ove rriding curren t
obje ctive is n1aximization of the rate of as se t
growth. Those with a diffe rcnt "prin1c eli r c ctive"
may find that another \ltility function i$ a he tt e l'
gUide.
We have found ElogX to be ':alu"bl ~ a ' a
qualitative guide and su ggest that thi s could. be
its 'most inlportant \1 se , Once fa ni ilia rity Y\ l~ ' h
its properties is gained, Inany invc~tI1"H~, n t. fl ,)"
cisions can 'be guided by it without c Olnple x
supporting ca lc:ulation s,
What sort of econom,ic. b ehavi or can be E:.x ~
