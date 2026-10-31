# The Kelly capital growth investment criterion _ theory and -- Leonard C_ Maclean, Edward O_ Thorp, W_ T_ Ziemba, Leonard -- World Scientific Handbook -- isbn13 9781283148344 -- bec576e26410d0c695fd5b867d08ec4f -- An.pdf — pages 628–647

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
--- page 629 ---

600
D. G. Luenberger
888
D.G. Luenberger, Log meanvariance criteria in investment problems
situation, roughly, is to cause the investment value to increase as rapidly as
possible, subject perhaps to considerations of security. Beyond this general
statement it is, at least initially, difficult to define a concrete investment criterion,
Yet this situation, even though highly idealized, closely approximates many real
money management situations, such as those involving university endowment
funds, mutual funds, gambling, expansion of a business enterprise, and personal
wealth-building. It is a situation that has received a great deal of attention in the
literature.
To make the situation tractable, it is usually assumed that the investment
environment is stationary in the sense that there is a fixed set of investment
opportunities each of which are available in every period and that the returns of
these investments are independent and identically distributed between periods
(although there is dependency among the different investments), With this
framework, the academic literature has traditionally taken three main approaches to this idealized management situation, One approach is to argue, on
the basis of very strong limit properties, that the best policy is the one that
maximizes Elog W", where W" denotes the wealth in the fund at some terminal
period nand E denotes the expectation operator [Kelly (1956), Brieman (1961),
Latane (1959)]. Because of the stationarity assumption, this policy reduces to
that of successively repeating the single-period policy of maximizing E log WI'
The second approach is based on adherence to the expected utility framework of
von Neumann and Morgenstern and suggests that one should maximize
EU( Wn ) for some utility function U, This includes U( w,,) = log W", but there
is no particular rationale for selecting that over any other utility function [see
Samuelson (1971)]. A third approach, also based on the expected utility framework, suggests that one maximize E [7= I (P)iU(Cj), where Cj is (a monetary
equivalent of) consumption drawn out .of the wealth at period i, and P,
o < fJ < 1, is a discount factor [Samuelson (1969)]. This last approach has good
economic justification within the von Neumann-Morgenstern framework, although the special form of additive discounted utility is quite specialized and
does not really capture the spirit of the original (vague) objective of managing
money which is not to be drawn down until the (distant) future, Our objective is
not to argue that one approach is superior to another, but simply to provide
a new preference foundation for the E log WI approach (or a generalization of it),
so that it can be addressed by economic principles,
There has been considerable interest in considering the limiting behavior of
the EU( WII) criterion as n -+ 00, to obtain approximate and simple results. It
has been hoped that this might provide some economic justification for the
expected log approach, The principal technique in such investigations has been
to impose restrictions on the utility function (usually through boundedness
assumptions) in order to deduce that the investment policy derived from the
Elog W" criterion also maximizes EU(W,,) as n -+ 00 [cf. Markowitz (1959),
Leland (1972)]. Such attempts have been of limited success, as elucidated in
--- page 630 ---

A Preference Foundation f or Log Mean-Variance Criteria in Portfolio Choice Problems
601
D.G. Luenberger. Log meanvariance criteria in investment problems
889
Samuelson (1971) and Goldman (1974). No convincing argument has yet been
made that reduces the general utility function approach (for a wide class of
useful utility functions) to the Elog Wn (or equivalently Elog W.) approach.
The E log Wn approach has been brought closer to standard economic theory
by generalizing it to a criterion based on a trade-off between E log Wn and
var(log w,,) [Williams (1936)]. Specifically, one defines an efficient frontier for
fixed n, where var(log Wn) is minimized subject to E log Wn ~ m, for various
values of m. An efficient policy corresponds to a point on this frontier. This
procedure parallels the familiar mean-variance approach to single-period investment [Markowitz (1952), Sharpe (1970), Tobin (1965), Lintner (1965)] and
has the appeal of simplicity of that familiar procedure. Of course, this itself may
not eliminate the conceptual gap between the asymptotic approach and classical
utility theory, since even single-period meanvariance theory is not consistent
with expected utility maximization except in special circumstances [Borch
(1963)]. However, it has been shown that the log mean~variance approach I
serves as an approximation to. the terminal utility approach when uncertainty is
'small' [Samuelson (1970)].
Because of its intuitive appeal and simplicity, it is natural to look for stronger
justification for log mean-variance criteria, and the central limit theorem might
seem to provide the basis for such a justification. The distribution of the
sum of the logarithms of n independent and identically distributed returns,
when its mean is subtracted and the result is normalized by dividing by n 112,
converges to a normal distribution. Ignoring the required normalization, one
might argue that the distribution of the sum itself is close to a normal distribution for large n. Then since this normal distribution is completely characterized
by its mean and variance, it is plausible to use these two parameters as
determinants for an investment criterion. This idea has been explored in
Hakansson (1971 a, b), and it was found that the corresponding efficient frontier
degenerates to a single point as n .... 00, since the ratio of standard deviation to
mean goes to zero.
If the normalization is accounted for, the situation is far more complex, since
there seems to be no valid limit argument. This was forcefully pointed out
in Merton and Samuelson (1974) and observation of this limit fallacy led
them once again to dismiss log mean-variance criteria as too simplistic. (Additionally, the very idea of using utility at a terminal time and taking the limit
also implicitly involves a fallacy since limn_co E{ U(Wn )} is not an expected
utility.)
So where does all of this leave us? The log mean criterion, or more generally,
the log mean-variance approach is intuitively appealing, but apparently not
consistent with standard expected utility theory.
I The phrase 'log mean-variance criteria' is used throughout as shorthand for 'criteria involving
only the mean and variance of the logarithm of the return'.
--- page 631 ---

602
D. G. Luenberger
890
D.C. Luenberger. Log meanl'ariance criteria in investment problems
In section 3 we set the stage for a new preference-based approach to the
problem. We begin by establishing preferences on infinite sequences of wealth
rather than wealth at a fixed (but later taken to the limit) terminal time. This
approach circumvents the limit problems encountered by the earlier approaches, and in fact provides a path whereby powerful limit theorems of
probability theory can be applied. The preference relations on infinite deterministic sequences are extended to stochastic sequences, not by imposition of a von
Neumann-Morgenstern expected value criterion, but instead quite naturally by
an 'almost sure' criterion, which is applicable when the original preference
relation depends entirely on asymptotic properties, as is appropriate for this
problem. It is then shown that a wide spectrum of these asymptotic preferences
reduce to log meanvariance criteria. Thus, under quite broad conditions the log
mean-variance approach is identical with an asymptotic preference approach.
The justification for the variance comes about, by the way, not from the central
limit theorem, but from its stronger cousin, the law of the iterated logarithm.
2. The investment environment
We begin by more explicitly defining the investment environment. There is an
underlying vector random process Z = {Zk} defined on a probability space
(D, §', Pl. Each Zk = (Z lk' Z2k> ... ,ZSk) is a vector of S random variables. An
investment policy (ill' ilz, ... ) is a sequence of mappings ilk: R' -+ R. This policy
defines a new process X = {Xd of random variables by X k = ilk(Zk)' The
X process is the single-period return process. The X process in turn generates
a wealth process W according to
where Wo is the (fixed) initial wealth. The investment problem, in this general
setting, is that of selecting the policy a within a class of feasible policies that leads
to the most desirable W process.
It should be noted that systematic withdrawals from the accumulated wealth
can be accommodated in this framework by incorporating them into the
definition of (Xk' For instance, a withdrawal of a fraction 13k of the wealth at
period k using investment policy
ilk is treated by setting X k = cxk(Zd
= (I - 13da/l(Zk)'
A concrete example of the general framework is where there are S securities,
each of which may be purchased in any amount at the beginning of each period.
If one unit of wealth (one dollar, say) is invested in security j, j = 1,2, ... ,S,
during period k, its value at the end of the period is Zjb where Zjk is a nonnegative random variable. The random vector Zk = (Zlk, 2 2k , ... ,2Sk ) thus
describes the single-period returns for period k. At the beginning of any period k, .
--- page 632 ---

A Preference Foundation for Log Mean- Variance Criteria in Portfolio Choice Problems
603
D.G. Luenberger, Log meanvariance criteria in inveslment problems
891
the investment manager apportions the current wealth Wk _ 1 among the S securities by choosing a weighting vector !Xk = «("ta, <X2b ••• , ("tnlc) such that
L~ = 1 ("ti/C = I, and, accordingly, invests U-j. - 1 C(jk in security i. The composite
single-period return is
Wealth at the end of the period is then
A choice of a sequence of vectors <Xl' C(2, ••. is an investment policy.2
The analysis in this paper is based on the following:
(A. I) Basic assumptions
(a) The Zk are independent, identically distributed, and nonnegative on
(Q,~, P).
(b) The ZIc are bounded above.
(c) Policies (C(l, C(2, •• • ) must be constant (that is, C(k = C( for all k = 1,2, ... ),
and C(: R~ ~ R + (no short sales).
(d) Each ("t is measurable and bounded. In particular,3 there is a C > 0 such that
C(Z/c) ~ C for all ("t and k.
Primarily we shall be concerned with the processes X and W derived from
Z and a policy <x. For this purpose we only require the following assumptions
(the first two of which follow directly from above):
(A.2) Properties of X and W
(a) The X k are independent, identically distributed. and nonnegative random
variables on the probability space {Q,~, P}.
For all k:
(b) X k ~ C.
(c) log X k has finite first and second moments.
(d) W/c = Wk-IXk, with Wo = 1.4
2In this example ilk is linear. Nonlinear mappings can accommodate options or other nonlinear
functions of a security's return without introducing additional securities.
3This uniform upper bound requirement is for convenience. It can be relaxed.
4 Wo = J is a normalization that is used for convenience only.
--- page 633 ---

604
D. G. Luenberger
892
D.G. Luenberger. Log mean-variance criteria in investment problems
The max E log policy
The wealth Wn can be written
Taking the logarithm of this equation we obtain
log Wn = log X I + log X 2 + . .. + log X n ,
or equivalently.
(1)
Under our assumptions, as n approaches infinity the right-hand side of (I)
approaches (almost surely) ElogXl (or ElogXk for any k = 1,2, . . . since all
are equal). Hence for large n
10g[Wn]l/n:::: ElogXI'
and, in a formal manner, we write
Wn :::: expn(E log X d·
(2)
Roughly speaking (2) says that wealth grows approximately exponentially
with a coefficient in the exponent equal to E log X l' This is an indication that
maximization of E log X I might be desirable. This reasoning can in fact be made
rigorous. [See Breiman (1961), Algoet and Cover (1985). and Bell and Cover
(1980).] However, this argument is not based on a definitive concept of optimality. Nevertheless, as shown in section 4 of this paper. the optimal log mean
policy does in fact correspond to optimization of any 'simple' asymptotic utility
function.
3. Preferences on sequences
Our approach is based on recognizing from the outset that one is selecting
from a set of competing infinite sequences of random variables. Hence the
preference relation should be constructed on these sequences directly.
Consider first deterministic sequences. Let r be the set of all such sequences
WI, W2, . . . having the following properties:
for all k.
(ii)
Wk ~ Ck
for all k,
where C is the bound in assumptions (A. I-d) and (A.2-b).
--- page 634 ---

A Preference Foundation for Log Mean- Variance Criteria in Portfolio Choice Problems
605
D.G. Luenberger, Log meanvariance criteria in investment problems
893
Assume that on r x r there is a preference relation ;2:. That is, ;2: defines
a preference relation on a pair of sequences. (If w, ve rand w'=v, we say w is
preferred to v.) Such a preference relation satisfies the following properties:
(P.1) Completeness: For every pair v, wer, either w;2:v or v;2:w.
(P.2) Reflexivity: For every wer, w;2:w.
(P.3) Transitivity: For every u, v, wer, if u;2:v and v,=w, then u;2:w.
Examples of preference relations can be easily constructed by restricting
attention to a finite set of indices k = 1,2, ... ,n and using any standard
finite-dimensional preference relation. In particular, one might define the relation in terms of wealth at a fixed (surrogate terminal) time n; i.e., w~v ifw" ~ v".
More interesting examples defining w~v includes
-1
-1
lim -log w" ~ lim -log Vn ,
n-ct.> n
n-co n
(3)
-
1 "
1 "
lim '2 L logwk ~ lim '2 L logvk'
"~<Xl n k=l
n~oo n k=1
(4)
<Xl
WOOD
"
">"
n
,,7:1 (2c)n - ,,7:1 (2C)n'
(5)
-1
-1
lim -log WI! W,,+ 1 ~ lim -log VnV" + 1 •
(6)
n-+C,() n
n-co n
We assume an additional property that is really the heart of our analysis.
(P.4) Tail Property: The preference relation depends only on the tail of the
sequences in r. That is if w, De rand w'=v, then w;2:v for any W, veT that differ
from wand v in at most a finite number of elements.
The examples (3), (4), and (6) are tail preferences.
The motivation for this assumption stems from the original proposed setting
of the investment problem. The investor is assumed to care only about the
long-term behavior of the investment; no finite portion is of concern. From
a technical perspective the introduction of tail preferences is precisely the
concept required to introduce the limit idea early, so that it need not be
5The notation lim indicates lim sup (that is, limit superior).
--- page 635 ---

606
D. G. Luenberger
894
D.G. Luenberger. Log meanvariance criteria in investment problems
introduced at a later stage of the logical development and then interchanged
with some other operation.
Preferences on stochastic processes
Now let "II' be the family of stochastic wealth processes derived from the
investment procedure of section 2. We wish to establish a preference relation on
"II' x "11'. That is, we wish to be able to compare two different stochastic
processes. This new preference relation should be an extension of the preference
relation on deterministic sequences defined above. r x r is a subset of R cx:. x R cD
and we let L!I be the corresponding subset of the Borel field on R en x R OO. This
leads to an additional technical requirement on the preference relation.
(P.5) Measurability: The subset {(w, v): w;:::v} of r x r is in 31.
We now extend the preference relation to a preference relation ;:::s on
stochastic wealth processes. The extension is by almost sure association.
Axiom.
Let W = (WI' W2 , . . • ), V = ( VI, V2 , .. • ) he stochastic processes in
"11'. Then W;:::s V if W:2: Va.s. That is
W;:::s V if P{ W:2: V] = 1 .
(7)
In other words, if for almost every realization of the processes the sequence
generated by W is deterministically preferred to the sequence generated by V,
then the stochastic process W is preferred to the stochastic process V.
This is a very natural (and very weak) axiom. Notice that the usual axioms
required to define preferences over stochastic events (through an expected utility
criterion) are not imposed. Our stochastic preference criterion is not an 'expected' criterion; it is an 'almost sure' criterion. Stoc~astic preference is induced
by almost sure deterministic preference. In a very real sense then this preference
structure is substantially weaker than that employed in traditional preference
approaches to this problem. (To be sure, it is in another sense stronger because
of the tail assumption.)
.
A potential difficulty with this axiom is that it may not make sense. It might
be that P{ W:2: V} = t in which case neither W;:::s V nor V:2:s W would hold.
A zero-one law insures that this is never a problem.
Theorem 1. !f (P.1)-(P.5) hold, the relation ;:::s is complete, reflexive, and
transitive.
Proof
Given Wand V in "/t', the sequence of pairs {( Jti, II;)} is a process on
(Q, §, Pl. Let X = (X I, X 2, ... ) and Y = (Y I , Y2 , .. • ) be the corresponding
--- page 636 ---

A Preference Foundation for Log Mean- Variance Criteria in Portfolio Choice Problems
607
D.C. Luenberger. Log meanvariance criteria in investment problems
895
single-period return processes. Under our assumptions (A.l) and (A.2) the pairs
(X .... Y,,) and (X" Y1) are independent for k # t. Because Xi and Yi are uniformly
bounded, all realizations of Wand V are in r. The event {W~ V} c Q is
measurable by (P.5) and is a tail event on the process of pairs {( Wi, Vi)}.
However, any tail event in this process is a symmetric event [see Beeiman (1968)
or Shiryayev (1984)] for the process {(Xi, Yi)} since such an event is not
influenced by a permutation of any finite number of elements of the processes.
This latter process is independent, and hence by the Hewitt-Savage Zero-One
Law [see Breiman (1968)], the probability of the event {W~ V} is either zero or
one.
If P{ W~ V} = 1, then W~s V. Suppose, however, that P{ W~ V } = O. We
have
1 = P {{ W ~ V} u { V ~ W} } ~ P { W ~ V} + P { V ~ W} ,
where the first equality follows from the completeness of the order ~. Hence, in
this case P{ V~ W} = 1, and V~s W. Therefore in any case either W~s V, or
V~sw.
Reflexivity follows immediately from the reflexivity of ~. Transitivity is fairly
immediate also: Let U ~s V, V ~s W. Then U ~ V and V~ Wexcept on subsets
M 1 and M 2, respectively, of Q, each of measure zero. Thus by transitivity of ~,
U ~ W except on M 1 U M 2' I
The key ingredient of this result is that measurable tail events on wealth
processes have probability of either zero or one. It is for that reason we can
define preference for stochastic wealth processes by almost sure association - the
relation is always almost sure one way or the other. We exploit this property
throughout the remainder of the paper.
4. Simple utility functions
A particularly useful way to describe a large class of preferences is through
a utility function. Again, a utility function first can be introduced on deterministic sequences, that is, on r. Then this utility, ifit defines a tail preference relation,
can be extended by almost sure association to a utility function on the set "Ir of
stochastic processes.
A utility function on r is a measurable real-valued function U: r -+ R. It
defines a preference relation through the definition w~v if U(w) ~ U(v). We say
that a utility function is a tail utility function if U(w) depends only on the tail of
w = (wt> W2 • ••• ) [that is, U(w) = U(w) if wand w differ in at most a finite
number of elements].
--- page 637 ---

608
D. G. Luenberger
896
D.G. Luenberger. Log meanvariance criteria in investment problems
We extend a tail utility function U from r to 1fr by use of the fact that, by the
zero-one law, if WE if/, then if U (W) is finite-valued, it is a degenerate random
variable; that is, it is a constant almost surely. The value of this constant is taken
to be the value of U ( W).
Although there is an infinite variety of possible tail utility functions, we focus
first on what we call simple utility functions. These are defined in terms of
limiting operations on functions of wealth at individual periods, with no interaction between periods. Specifically, simple utility functions have the form
U(w) = lim p(wn , n).
or
U(w) = lim p(wn, n),
" ..... ex:·
or algebraic combinations of these forms. In these expressions, P is a continuous
and increasing function of Wn for each n. This appears to be a very general class
of tail utility functions; and if we accept the idea of basing preferences on tail
events, this form of utility is very natural. We shall show, however, that this form
(with some minor restrictions) leads inevitably to the expected log return
criterion.
We
note
first
that
without
loss
of generality
we
may
write
p( w, n) = p(log w, n) by applying the one-to-one transformation log w, which
maps between (0, 00) and ( -
00, 00). The resulting p( ., n) is con'tinuous and
increasing since Pc. n) is. Finally, by adding a constant to U, if necessary, we
may assume p(l, n) = 0 or equivalently p(O, n) = O. Thus we define a simple
utility function as having the form
U(w) = lim p(log W n , n).
(8)
nrJ:..-
or
U(w) = lim p(log W n , n) ,
(9)
or combinations of the forms (8) and (9), where p has the properties stated above.
We extend these to the stochastic wealth process W by use of the fact, from the
proof of Theorem I, that tail events on W have probability of either zero or one.
This means, in particular, that if f: r -+ R is measurable and f(w) depends only
on the tail of the sequence w, then the random variable f( W) is constant almost
surely. Using this fact we define
U( W) = lim p(Jog Wn• n),
(lO)
n ........ -x;
--- page 638 ---

A Preference Foundation for Log Mean- Variance Criteria in Portfolio Choice Problems
609
D.G. Luenberger. Log meanvariance criteria in investment problems
897
or
U( W) = lim p(log Wit, n).
(11 )
n-c.c'!
The random variables U ( W) defined above are measurable as extended random
variables - see Shiryayev (1984, pp. 171, 358). If U ( W) is finite it is constant a.s.,
and the utility is taken to be this constant.
Not all functions p(.,.) will lead to meaningful utility functions. For example,
if p(z, n) = z, the process Wit = c" with c > 1 will lead to U( W) = 00. In general,
in order to obtain finite utility for feasible wealth processes, it is necessary that
p(z, n) satisfy appropriate growth-rate conditions with respect to n. In particular, p must decrease with n to counterbalance possible increases in z. The
following theorem gives suitable conditions.
Theorem 2.
For each n, let p(z, n) be continuous and increasing in z with
p(O, n) = O. Let X and W be processes satisfying (A.2). Assume E log Xl = m, and
define U by (/0).
(a) Iflimn~'" p(nz, n) = sgn(z) ' 00, then
U( W) = { + 00, m > 0,
-00, m<O.
(b) If limlt~oo p(nz, n) = g(z) where g(.) is continuous, then U( W) = g(m).
Proof.
We have O/n)log Wit -+ m a.s. Let z. = (ljn)log Wit, n = 1,2, ...• correspond to a particular realization of the process where convergence of z. -+ m
holds. Given € > 0, there is an N such that I Zit - ml < € for all n> N. By
monotonicity of p it follows that
p(n(m -
€), n) ~ p(nz", n) ~ p(n(m + €), n),
for all n > N. Hence
lim p(n(m - €), n) ~ lim p(nzlt • n) ~ lim p(n(m + €), n).
"~oo
If m > O. then for sufficiently small € > 0 both m - e > 0 and m + e > O. Therefore, if the hypothesis (a) holds. it follows that limlt_ oop(nz,,; n) = 00. A similar
argument shows that for m < 0 there holds limn_oop(nzn, n) = -
00. If the
hypothesis in (b) holds, then
lim p(nz", n) = g(m) .
--- page 639 ---

610
D. G. Luenberger
898
D.G. Luenberger. Log meanvariance criteria in investment problems
Finally, the conclusion follows since
I
I "
- log Wn = - L log X k --. m a.s.
n
n k= 1
by the strong law of large numbers, and hence the above values hold for
-
-
(
I
)
!~_ p(log Wn, n) = !~. p n ~Iog Wm n
almost surely. I
The parallel of Theorem 2 holds for the form (10), with limn_ xreplaced
everywhere by limn_ cx:, . It is clear that in either case g(m) is an increasing
function of m.
Theorem 2, and the above remarks, say roughly that, to within a monotone
transformation, the only real-valued tail simple utility function is m = E log X l '
We remark again, however, that although this 'appears' to be an expecteQ value
criterion, it is actually an 'almost sure' criterion. The expected value arises from
the strong law of large numbers, rather than from an assumption of expected
value utility.
It is perhaps useful to relate the theorem more directly to our earlier
discussion of other utility functions. For example, consideration of the
popular utility function defined as w~ on terminal wealth leads one to set
p(log W n , n) = exp( y log wn ) in (8). However, clearly p(nz, n) -+ sgn(z)' 00,
leading to the infinite result of part (a) of Theorem 2. The idea can be
salvaged by introduction of a I /n in the power, i.e., w~ /n or p(z, n) = e)·tln.
This leads to U ( W) = e ym• which again gives the expected logarithm
criterion.
5. Compound utility functions
It is apparent that there is a slight gap in Theorem 2. Part (a) covers the
cases m > 0 and m < 0 but not m = O. This is no real detraction from the
theorem, for part (a) says that under its conditions the corresponding utility
function is degenerate unless it is applied to a process with m = O. However,
this gap motivates the introduction of compound utility functions; since
by subtracting out the mean m from the process, there is room for other
possible forms.
Another motivation for compound utility functions is purely structural. We
let a compound utility function have a simple utility function as an argument.
--- page 640 ---

A Preference Foundation for Log Mean- Variance Criteria in Portfolio Choice Problems
611
D.G. Luenberger. Log meanvariance criteria in investment problems
899
However, by Theorem 2, we can take this simple utility function to be
U s( W) = m. This motivates the specific compound forms
U( W) = lim ",(log Wn -
nm, m, n) a.s.,
(12)
U( W) = lim ",(log w" - nm, m, n) a.s.,
( 13)
where", is continuous and increasing in its first two arguments. As before, the
equalities in (12) and (13) are to be interpreted in the almost sure sense. Such
a utility, depending on m, is clearly still a tail function.
Once we recognize the role of the mean log return m in compound utility
functions, it is not necessary to carry it along in our analysis. Instead, we
consider
U ( W) = lim 4>(log w", n) a.s.,
(14)
U(W) = lim 4>(1og Wit, n) a.s.,
(15)
where 4>(z, n) is increasing in z, for the special case where m = E log XI = o.
Then, later, we can simply put m back into the utility as an additional variable,
as in (12) or (13). This restriction to the study of utility functions (14) and (15)
amounts, really, to a further examination of simple utility functions when it is
known that m = O.
A special situation is the degenerate one where Wn = 1 for all n. We wish this
to have finite utility, and hence without loss of generality we may take
4>(0, n) = 0 for all n.
As before the behavior of 4> as a function of n is critical. To characterize the
appropriate behavior of 4> it turns out that the asymptotic behavior of 4> (Jnz, n)
is critical.
The following proposition and its corollary rule out a large class of
functions.
Lemma 1.
Suppose 4>(z, n) is increasing in z for each n with 4>(0, n) = ° and
Let X and W be processes satisfying (A.2) and assume E log XI = 0,
var(log X d = (12 > O. Then,for U defined by (14), U( W) ~ A.
--- page 641 ---

612
D, G, Luenberger
900
D,G, Lumberger. Log meanvariance criteria in investment problems
Proof Since 4>(0, n) = 0, it follows that A ~ O. In order to treat the case
A = oc as well as A < oc, we prove that if
lim lim 4>(\/~z, n) ~ A',
=-
~_ n- 'y.,
with A' ~ 00, then V( W) ~ A'. The lemma follows from this.
Let p(z) = lim n_", 4>(Jnz, n). Select f: > O. Then there is a z such that
p(z) > A' -
f:. Then, by the definition of p, there is N such that for all n > N,
4>(Jnz, n) > A' - 2e. By the monotonicity of 4>(' , n) we have
4>(Jnz, n, ~ 4>(Jnz, 11) > A' - 2f:,
for all z ~ i and all n > N.
Thus,6
where the last equality follows from the law of the iterated logarithm,
I,
log Wn
1
1m
=
a.s.,
noo (2a2nloglogn)1 /2
which shows that limn _ ", (Iog Wn)/Jn = oc, a.s. Therefore V( W) > A' - 2e,
Since this is true for all c > 0, it follows that V (W) ~ A '. I
Corollary.
If for all z > 0,
lim 4>(Jnz, n) = ox,
n- ~'
then,for V defined by (14). V( W) = oc.
Proof
We have A = 00 in the above lemma. I
Let us consider some examples. The function 4>(z, 11) = zln corresponds,
according to Theorem 2 of the previous section, to the simple utility function
with value V( W) = m; and hence in this context, with m = 0, V( W) = O. A = 0
for this function, so Lemma 1 gives V( W) ~ 0, The reverse inequality can be
established by a symmetric argument (see Lemma 3), and together these agree
with ,what is known from Theorem 2.
6 i.o, denotes 'infinitely often',
--- page 642 ---

A Preference Foundationfor Log Mean-Variance Criteria in Portfolio Choice Problems
613
D.G. Luenberger. Log meanvariance criteria in investment problems
901
n==l
z
Fig. I. An unusual function that is decreasing in n above A.
In general, if 4>(z, n) = z/q(n), then clearly q(n) must go to infinity faster than
In in order that A be finite and hence for the corresponding compound utility
function to be real-valued. For example, the function 4>(z, n) = z/Jn has
A = co .
Definition. Let A be a constant. The function of two variables 4>(Jnz, n) is
said to be decreaSing with respect to n above A if 4>(Jnz, n) > A implies
4>(j;+1z, n + 1) ~ 4>(Jnz, n).
The monotonicity property with respect to n is quite reasonable even if A > O.
An example is shown in fig. 1.
Corresponding to a function 4>(z, n) that is continuous and strictly increasing
in z for each n, let f(', n): D" -+ R [where D" is the range of 4>(' , n)] be the
inverse function of 4>( . , n); that is,
f(4)(z, n), n) = z,
for every z. This inverse exists and is also strictly increasing. We need the
following result which shows that if qJ ( Vnz, n) is decreasing with respect to n,
then f / Vn is increasing with respect to n.
Lemma 2. Suppose 4>(j;+1 z, n + 1) ~ 4>(Jnz, n) = r. Then,
f(r, n)/Jn ~f(r, n + l)/j;+1 .
--- page 643 ---

614
D. G. Luenberger
902
D.G. Luenberger. Log meanvariance criteria in investment problems
Proof
We have
(p(Jnz, n) = r,
cP(Jn+jz, n + I) = s,
with s ~ r. By applying f to these we have
z =f(r, n)/Jn,
z =f(s, n + l)/Jn+j ~f(r, n + l)/Jn+j,
where the inequality follows from the monotonicity of f(· , n + 1). Therefore
f(r, n)/Jn ~f(r, n + l)/Jn+j. I
We are now prepared to state the basic result of this section. We show,
essentially, that any compound utility function of wealth (14), derived from
a process with zero mean (of the logarithm), is a function only of
a 2 = var(Jog X d (or, equivalently, of a).
Proposition 1. Let U be defined by (14) and assume that cP(z, n) is continuous and
strictly increasing with respect to z for each n, and that cP(O, n) = 0. Suppose
further that cP(j-;,z, n) is decreasing with respect to n above A as defined in Lemma
1. Then there is afunction h on R + possibly taking values -
00 or + 00 such that
(i) h( a) is nondecreasing with respect to a;
(ii) for any process X and
W satisfying (A.2) with m = E(Iog Xl) = 0,
var(log Xl) = 0'2 > 0, there holds
U( W) = h(O') .
Proof
Defining A as in Lemma 1, we know that U( W) ~ A. For any r > A, we
have U ( W) > r if and only if
P{cP(log Wn , n) > r
i.o.} = I.
This is equivalent to
p{IOg ~n >f(r,;.) i.O.} = 1.
O'v'n
O'v'n
--- page 644 ---

A Preference Foundationfor Log Mean-Variance Criteria in Portfolio Choice Problems
615
D.G. Luenberger. Log meanvariance criteria in investment problems
903
According to the assumptions on 4> and the above lemma, Yn = f(r, n)/(11 In) is
increasing for r> A. Furthermore, f(r, n) > 0 for r> A ~ O. Therefore the
extended law of the iterated logarithm [Feller (1943), Breiman (1968, p. 297)]
states that the probability above is either zero or one, depending on whether the
sum
~ Yn
-y2 /2
L- -e "
n = 1 n
converges or diverges, respectively. If the sum converges for a given sequence
{Yn}, then it will converge also for {Y~} with Y~ > Yn' This is because (d/dx)
x [xe- X2/2] = [1 - x3Je-x2/2 < 0 for x > 1. Thus, for sufficiently large n, each
term in the sum for {Y~} is smaller than the corresponding term in the sum for
{Yn} . Therefore, if the sum converges for a given value of r, it also converges for
r' > r. It follows that
In a similar way, if the series converges for a given 11, it wiJ] also converge for
11' < 11. Hence U( W) = h(l1) where h(') is nondecreasing. I
A useful 4> for consideration is
z
4>(z, n) = (2 I
I
)1 /2 .
n og ogn
In this case the standard law of the iterated logarithm states that
.
10gWn
U ( W) = hm (2 1 I
) 1/2 = 11
a.s. ,
noo
n og ogn
and hence this 4> gives h(l1) = 11.
Proposition I shows that an investor with a utility function of the general
form (14), with the lim operation, prefers increased variance. Increased variance
increases the extent of upward variations, and presumably the investor values
these peaks.
The comparison to PrOposition 1 treats utilities of form (15), with the lim
operation. In this case the iiWestor wants to increase the lowest deviations, and
hence such an investor values low variances more than high variances.
Specifically, we have the following results.
--- page 645 ---

616
D. G. Luenberger
904
D.G. Luenberger. Log meanvariance criteria ill int'eSlmenl problems
Lemma 3.
Suppose 4J(z, n) is increasing in z for each n with 4J(0, n) = 0 and
lim lim 4J(y'7zz, n) = B.
z- -
''X:' n-::(.
Let X
and
W be processes satis/:ving (2) and assume E log X I = 0,
var(log X I) = a 2 > O. Then, for U defined hy (J 5). U (W) s B.
Proposition 2.
Let U be defined by (I5) alld assume that 4J( z, n) is continuous and
strictly increasing with respect (0 ;:: for each n, and that ¢(O, n) = O. Suppose
further that 4J('\/~z, n) is increasing with respect to n helow B as defined in Lemma
3. Then there is afunction 9 on R + possibly taking values -
oc: or + 00 such that
(i) g(a) is nonincreasing with respect to a;
(ii) for any processes X and W satisfving (A.2) with m = E(log X I) = 0,
var(log X t) = a 2 > 0, there holds
U( W) = g(a).
Finally, we may combine Propositions I and 2 and insert the explicit dependence of a general compound utility function on the mean m. We let I/I(z, m, n) be
continuous and strictly increasing with respect to z and increasing with respect
to m.
Theorem 3.
Let U be defined by either
(a) U( W) = limn~ cx: I/I(log Wn - nm, m, n) a.s., or
(b) U( W) = lim n _
lO 1/1 (log Wn - nm, m, n) a.s.
Correspondingly, assume thaljor each m, 4Jm(z, 11) = I/I(z, m, n) satisfies the conditions of Propositions I or 2. Then there is a function f on R x R + possibly taking
values -
iX or + ,x; such that
(i) f(m, a) is increasing with respect to m and either increasing or decreasing with
respect to a corresponding to (a) or (b);
(ii) for any processes
X
and
W
satisfying (A.2)
with
In = E log Xl,
var(log Xl) = a 2 > 0, there holds U (W) = .f(m, (J).
For a given process Z and a given family of feasible investment policies, one
can define the set S of attainable (m, a) pairs (achieved as the policy ranges over
all possibilities). If the set S is compact, the right frontier of the set S is the
right-most boundary of this set; that is, the points (m, a) having the largest a for
--- page 646 ---

A Preference Foundation for Log Mean-Variance Criteria in Portfolio Choice Problems
617
D.G. Luenberger, Log meanvariance criteria in investment problems
905
a given m. Then, according to the above theorem, an investor with a utility
function of the form (a) will select a policy corresponding to a point on this
frontier. Similarly, an investor with a utility function of the form (b) will select
a policy corresponding to a point on the left frontier.
6. Conclusion
We have approached infinite-horizon investment situations by considering preference orders on infinite sequences of wealth, and we suggested that
tail preferences are appropriate if the goal of investment is long-term 'wealth
building'. We showed that if the tail preference takes the form of a simple
utility function, then utility must be equivalent to the expected logarithm
of return. If preferences are represented by a compound utility function, that
function will be equivalent to a function of the expected logarithm and
variance of the logarithm.
Although our results require that certain technical assumptions be satisfied,
they are robust enough to support, at least roughly, the statement that: a tail
utility function involving the limits of total return must be equivalent to a
log meanvariance criterion. We do not anticipate, however, that the controversy over the use of such a criterion will subside. Indeed it should not.
Our result is based on the tail preference concept, which is an idealization
of what is generally a complex economic problem. However, since the log
mean-variance approach is so intuitively appealing, it is nice to have a
framework in which it is validated.
References
Algoet, P.H. and T.M. Cover, 1985. Asymptotic optimality and asymptotic equipartition properties
of log-optimum investment. Technical report 57 (Department of Statistics, Stanford University,
Stanford, CAl.
Bell, R. and T.M. Cover. 1980, Competitive optimality of logarithm investment, Mathematics of
Operations Research 5. 161-166.
Borch, K., 1963. A note on utility and attitudes to risk, Management Science 9. 697-701.
Breiman, L., 1961, Optimal gambling systems for favourable games, Proceedings of the Fourth
Berkeley Symposium 1,65-78.
Breiman, L., 1968, Probability (Addison-Wesley, Reading, MA).
Feller, W., 1943, The general form of the so-called law of the iterated logarithm, American
Mathematical Society Transactions 54, 373-402.
Goldman, M.B., 1974, A negative report on the 'near optimality' of the max-expected-Iog policy as
applied to bounded utilities for long-lived programs, 10urnal of Financial Economics 1,97- 103.
Hakansson, N.H., 197130 Capital growth and the mean-variance approach to portfolio selection,
10urnal of Financial and Quantitative Analysis 6, 517-557.
Hakansson, N.H .• 1971 b, Multi-period mean-variance analysis: Toward a general theory of portfolio choice, Journal of Finance 26. 857-884.
Kelley, J.L., Jr .. 1956. A new interpretation of information rate, Bell System Technical Journal 35,
917-926.
--- page 647 ---

618
D. G. Luenberger
906
D.G. Luenberger. Log meanvariance criteria in investment problems
Latani:, H., 1959, Criteria for choice among risky ventures, Journal of Political Economy 67,
144-155.
Leland, H., 1972, On turnpike portfolios, in: G. Szego and K. Shell, eds., Mathematical methods in
investment and finance (North-Holland, Amsterdam).
Lintner, J., 1965, The valuation of risk assets and the selection of risky investments in stock
portfolios and capital budgets, Review of Economics and Statistics 48, 13- 37.
Markowitz, H., 1952, Portfolio selection, Journal of Finance 12, 77-9\.
Markowitz, H., 1959, Portfolio selection: Efficient diversification of investment (Wiley, New York,
NY).
Merton, R.C. and P.A. Samuelson, 1974, Fallacy of the log-normal approximation to optimal
portfolio decision-making over many periods, Journal of Financial Economics I, 67-94.
Samuelson, P.A., 1969, Lifetime portfolio selection by dynamic stochastic programming, Review of
Economics and Statistics 51,239-246.
Samuelson, P.A., 1970, The fundamental approximation theorem of portfolio analysis in terms of
means, variances, and higher moments, Review of Economic Studies 37, 537-542.
Samuelson, P.A., 1971, The 'fallacy' of maximizing the geometric mean in long sequences of investing
or gambling, Proceedings of the National Academy of Sciences 68, 2493-2496.
Sharpe, W., 1970, Portfolio theory and capital markets (McGraw-Hill, New York, NY).
Shiryayev, A.N., 1984, Probability (Springer-Verlag, New York, NY).
Tobin, J., 1965, The theory of portfolio selection. in: I.H. Hahn and F.P.R. Brechling, eds., The
theory of interest rates (Macmillan, New York. NY).
Williams. J.B., 1936, Speculation and the carryover, Quarterly Journal of Economics 50, 436.
