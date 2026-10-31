# Quantitative Risk Management_ Concepts, Techniques, and -- Alexander J_ McNeil, Rüdiger Frey, Paul Embrechts -- Princeton series in finance, -- isbn13 9780691122557 -- 478a0059673fecd0c76229cd3d8884e7 -- Anna’s Arc.pdf — pages 495–514

--- page 495 ---

10.2. Elements of Insurance Analytics
479
...........................................................................................................................................................................................................
...
.
Sum of claims (log scale)
1 − F(x) (log scale)
600
700
800
900
1000
Normal approx.
Gamma approx
GPD fit (u = 650)
•
Simulated
735
10−1
10−2
10−3
10−4
10−5
Panjer recursion
Figure 10.5.
Simulated CPoi(100, LN(1, 1)) data (n = 100 000) with normal-, translated-gamma, GPD and Panjer recursion (see Example 10.17) approximations (on log–log
scale).
...................................................................................................................................................................................... .. .. ..... ..
. .
.
.
Sum of claims (log scale)
40
50
60
70
80
90
Normal approx.
Gamma approx.
GPD fit (u = 50)
•
Simulated
1 − F(x) (log scale)
10−1
10−2
10−3
10−4
10−5
Figure 10.6.
Simulated CPoi(100, Pa(4, 1)) data (n = 100 000) with normal-,
translated-gamma, and GPD approximations (on log–log scale).
identities:
s0 = P(SN = 0) = P(N = 0) = p0,
sn = P(SN = n) =
∞

k=1
pkg(k)
n ,
n ⩾1,
⎫
⎪⎪⎬
⎪⎪⎭
(10.16)
where the latter formula corresponds to Proposition 10.4 but now in the discrete
case. As in Proposition 10.4 we note that (10.16) is difﬁcult to calculate, mainly due
--- page 496 ---

480
10. Operational Risk and Insurance Analytics
to the convolutions g(k)
n . However, for an important class of counting variables N,
(10.16) can be reduced to a simple recursion. For this, we introduce the so-called
Panjer classes.
Deﬁnition 10.10 (Panjer class). The probability mass function (pk) of N belongs
to the Panjer(a, b) class for some a, b ∈R if the following relationship holds for
r ⩾1: pr = (a + (b/r))pr−1.
Example 10.11 (binomial). If N ∼B(n, p), then its probability mass function is
pr =
+n
r
,
pr(1 −p)n−r for 0 ⩽r ⩽n and it can be easily checked that
pr
pr−1
= −
p
1 −p + (n + 1)p
r(1 −p) ,
showing that N belongs to the Panjer(a, b) class with a = −p/(1 −p) and
b = (n + 1)p/(1 −p).
Example 10.12 (Poisson). If N ∼Poi(λ), then its probability mass function
pr = e−λλr/r! satisﬁes pr/pr−1 = λ/r, so N belongs to the Panjer(a, b) class
with a = 0 and b = λ.
Example 10.13 (negative binomial). If N has a negative binomial distribution,
denoted N ∼NB(α, p), then its probability mass function is
pr =
α + r −1
r

pα(1 −p)r,
r ⩾0, α > 0, 0 < p < 1
(see Section A.2.7 for further details). We can easily check that
pr
pr−1
= 1 −p + (α −1)(1 −p)
r
.
Hence N belongs to the Panjer(a, b) class with a = 1 −p and b = (α −1)(1 −p).
In Proposition 10.20 we will show that the negative binomial model follows very
naturally from the Poisson model when one randomizes the intensity parameter of
the latter using a gamma distribution.
Remark 10.14. Onecanshowthat,neglectingdegeneratemodelsfor(pk),theabove
three examples are the only counting distributions satisfying Deﬁnition 10.10. This
result goes back to Johnson and Kotz (1969) and was formulated explicitly in the
actuarial literature in Sundt and Jewell (1982).
Theorem 10.15 (Panjer recursion). Suppose that N satisﬁes the Panjer(a, b)
class condition and g0 = P(X1 = 0) = 0, then s0 = p0 and, for r ⩾1,
sr = r
i=1(a + (bi/r))gisr−i.
Proof. We already know that s0 = p0 from (10.16), so suppose that r ⩾1.
Noting that X1, . . . , Xn are iid, we require the following well-known identity for
--- page 497 ---

10.2. Elements of Insurance Analytics
481
exchangeable rvs:
E

X1

n

i=1
Xi = r

= 1
n
n

j=1
E

Xj

n

i=1
Xi = r

= 1
nE

n

j=1
Xj

n

i=1
Xi = r

= r
n.
(10.17)
Moreover, using the fact that g(n−1)
0
= 0 for n ⩾2, we make the preliminary calculation that
pn−1
r−1

i=1

a + bi
r

gig(n−1)
r−i
= pn−1
r

i=1

a + bi
r

gig(n−1)
r−i
= pn−1
r

i=1

a + bi
r

P

X1 = i,
n

j=2
Xj = r −i

= pn−1
r

i=1

a + bi
r

P

X1 = i,
n

j=1
Xj = r

= pn−1
r

i=1

a + bi
r

P

X1 = i

n

j=1
Xj = r

g(n)
r
= pn−1E

a + bX1
r

n

j=1
Xj = r

g(n)
r
= pn−1

a + b
n

g(n)
r
= png(n)
r ,
where (10.17) is used in the ﬁnal step. Therefore, the identity (10.16) yields
sr =
∞

n=1
png(n)
r
= p1gr +
∞

n=2
png(n)
r
= (a + b)p0gr +
∞

n=2
r−1

i=1

a + bi
r

gipn−1g(n−1)
r−i
= (a + b)s0gr +
r−1

i=1

a + bi
r

gi
∞

n=2
pn−1g(n−1)
r−i
= (a + b)grs0 +
r−1

i=1

a + bi
r

gisr−i
=
r

i=1

a + bi
r

gisr−i.
--- page 498 ---

482
10. Operational Risk and Insurance Analytics
Remark 10.16. In the case of both the FFT method and the Panjer recursion,
an initial discretization of the loss df G generally has to be made, which introduces an approximation error.An in-depth discussion of discretization errors for the
computation of compound distributions is to be found in Gr¨ubel and Hermesmeier
(1999, 2000) (see also references therein for a comparison of these approaches). A
slight correction to Theorem 10.15 has to be made if g0 = P(X1 = 0) > 0. One
obtains s0 = ∞
k=0 pkgk
0 and, for r ⩾1, sr = (1 −ag0)−1 r
i=1(a + bi/r)gisr−i
(see Mikosch 2004, Theorem 3.3.10). In Notes and Comments we give further references.
Example 10.17 (Panjer recursion for the CPoi(100, LN(1, 1)) case). In Figure 10.5 we have included the Panjer approximation for the CPoi(100, LN(1, 1))
case. In order to apply Theorem 10.15, we ﬁrst have to discretize the lognormal df.
An equispaced discretization of about 0.5 yields the Panjer approximation in Figure 10.5, which is excellent for quantile values around 0.999, relevant for applications. The 99.9% quantile estimate based on the Panjer recursion is 735, a value very
close to the GPD estimate. Far out in the tail, beyond 0.999, say, rounding errors
become important (the tail drifts off) and one has to be more careful; in Notes and
Comments we give some references on how to improve recursive methods far out
in the tail.
10.2.4
Poisson Mixtures
Poissonmixturemodelshavebeenusedinbothcreditandoperationalriskmodelling;
for an example in the latter case see Cruz (2002, Section 5.2.2) as well as the book
jacket, which features a negative binomial distribution (a particular Poisson mixture
model). Poisson mixtures have been used by actuaries for a long time; the negative
binomial made its ﬁrst appearance in the actuarial literature as the distribution of
the number of repeated accidents suffered by an individual in a given time span (see
Seal 1969).
In Example 10.5 we introduced the compound Poisson model CPoi(λ, G), where
N ∼Poi(λ) counts the number of losses and G is the loss severity df. One disadvantage of the Poisson frequency distribution is that var(N) = λ = E(N), whereas
count data often exhibit so-called over-dispersion, meaning that they indicate a
model where var(N) > E(N). A standard way to achieve this is by mixing the
intensity λ over some df FΛ(λ), i.e. assume that λ > 0 is a realization of a positive
rv Λ with this df so that, by deﬁnition,
pN(k) = P(N = k) =
 ∞
0
P(N = k | Λ = λ) dFΛ(λ)
=
 ∞
0
e−λ λk
k! dFΛ(λ).
(10.18)
Deﬁnition 10.18 (the mixed Poisson distribution). The rv N with df (10.18) is
called a mixed Poisson rv with structure (or mixing) distribution FΛ.
A consequence of the next result is that mixing leads to over-dispersion.
--- page 499 ---

10.2. Elements of Insurance Analytics
483
Proposition 10.19. Suppose that N is mixed Poisson with structure df FΛ. Then
E(N) = E(Λ) and var(N) = E(Λ) + var(Λ), i.e. for Λ non-degenerate, N is
over-dispersed.
Proof. One immediately obtains
E(N) =
∞

k=0
kpN(k) =
 ∞
0
∞

k=0
ke−λ λk
k! dFΛ(λ) =
 ∞
0
λ dFΛ(λ) = E(Λ).
And, similarly,
E(N2) =
∞

k=0
k2pN(k) = E(Λ) + E(Λ2),
so the result follows.
We now give a concrete example of a mixed Poisson distribution, which is particularly important in both operational risk and credit risk modelling. Indeed we have
already used the following result when describing the industry credit risk model
CreditRisk+ in Section 8.4.2.
Proposition 10.20 (negative binomial as Poisson mixture). Suppose that the rv
N has a mixed Poisson distribution with a gamma-distributed mixing variable Λ ∼
Ga(α, β). Then N has a negative binomial distribution N ∼NB(α, β/(β + 1)).
Proof. Using the deﬁnition of a gamma distribution in Section A.2.4 we have
P(N = k) =
 ∞
0
βα
Γ (α)
λk
k! e−λλα−1e−βλ dλ =
βα
k!Γ (α)
 ∞
0
λα+k−1e−(β+1)λ dλ.
Substituting u = (β + 1)λ, the integral can be evaluated to be
 ∞
0
(β + 1)−(α+k)uα+k−1e−u du = Γ (α + k)
(β + 1)α+k .
This yields
P(N = k) =

β
β + 1
α
1
β + 1
k Γ (α + k)
k!Γ (α) .
Using the relation Γ (α + k) = (α + k −1) · · · αΓ (α), we see that this is equal to
the probability mass function of a negative binomial rv with p := β/(β + 1) (see
Section A.2.7).
Recall the deﬁnition of compound sums from Section 10.2.2 (Assumption 10.3
and Proposition 10.4). In the special case of mixed Poisson rvs, compounding leads
to so-called compound mixed Poisson distributions. There is much literature on dfs
of this type (see Notes and Comments).
--- page 500 ---

484
10. Operational Risk and Insurance Analytics
10.2.5
Tails of Aggregate Loss Distributions
In Section 7.1.2 we deﬁned the class of rvs with regularly varying or power tails. If
the (claim size) df G is regularly varying with index α > 0, then there exists a slowly
varying function L (Deﬁnition 7.7) such that ¯G(x) = 1 −G(x) = x−αL(x). The
next result shows that, for a wide class of counting dfs (pN(k)), the df of the
compound sum SN, FSN , inherits the power-like behaviour of G.
Theorem 10.21 (power-like behaviour of compound-sum distribution). Suppose that SN is a compound sum and that there exists an ε > 0 such that
∞
k=0(1 + ε)kpN(k) < ∞. If ¯G(x) = x−αL(x) with α ⩾0 and L slowly varying, then
lim
x→∞
¯FSN (x)
¯G(x)
= λ,
so ¯FSN inherits the power-like behaviour of ¯G.
Proof. This result holds more generally for subexponential dfs; a proof together with
further discussions can be found in Embrechts, Kl¨uppelberg and Mikosch (1997,
Section 1.3.3).
Example 10.22 (negative binomial). It is not difﬁcult to show that the negative
binomial case satisﬁes the condition on N in Theorem 10.21. The kind of argument
required is to be found in Embrechts, Kl¨uppelberg and Mikosch (1997, Example 1.3.11). Hence, if ¯G(x) = x−αL(x), the tail of the compound-sum df behaves
like the tail of G, i.e.
¯FSN (x) ∼α
β
¯G(x),
as x →∞.
(For details, see Embrechts, Kl¨uppelberg and Mikosch (1997, Section 1.3.3).)
Under the conditions of Theorem 10.21 the asymptotic behaviour of ¯FSN (x) in
the case of a Pareto loss df is again Pareto with the same index. This is clearly seen
in Figure 10.6 in the linear behaviour of the simulated losses as well as the ﬁtted
GPD. In the case of Figure 10.5, one can show that ¯FSN (x) decays like a lognormal
tail; see the reference given in the proof of Theorem 10.21 for details. Note that the
GPD is able to pick up the features of the tail in both cases.
10.2.6
The Homogeneous Poisson Process
In the previous sections we looked at counting rvs N over a ﬁxed time interval [0, 1],
say. Without any additional difﬁculty, we could have looked at N(t) counting the
number of events in [0, t] for t ⩾0. In the Poisson case this would correspond to
N(t) ∼Poi(λt); hence, for ﬁxed t and on replacing λ by λt, all of the previous
results concerning Poi(λ) rvs can be suitably adapted.
In this section we want to integrate the rvs N(t), t ⩾0, into a stochastic process
framework. The less mathematically trained reader should realize that there is a big
difference between a family of rvs indexed by time for which we only specify the
one-dimensional dfs (which is what we have done so far) and a stochastic process
--- page 501 ---

10.2. Elements of Insurance Analytics
485
˚
. . .
.. .. . . . ..... .
.
.. ..... . ....... ....... . ......... ....... ... .. .. ...... .... ................ ... ... . . . .. .
•
•
•
••
•• • • •
••• •• •
•
•• •• ••• •
• • ••• •• •••• •• • • ••••••••• ••••• •• • ••
•• •• • ••••• •••• •••• •• •••• ••••••
••• •••
• • • • •
•
˚ ˚ ˚
˚˚ ˚˚ ˚ ˚ ˚ ˚˚˚˚˚ ˚
˚
˚˚ ˚˚˚˚ ˚ ˚˚˚˚˚˚
˚ ˚˚˚˚˚˚˚ ˚ ˚˚˚˚˚˚˚˚˚ ˚˚˚˚˚˚˚ ˚˚˚ ˚˚ ˚˚ ˚˚˚˚˚˚ ˚˚˚˚ ˚
˚˚
˚ ˚˚˚˚˚˚˚
˚˚
˚˚˚
˚˚˚ ˚˚˚ ˚ ˚ ˚ ˚˚ ˚
•
•
•
•
•
•
•
•
•
•
˚˚
˚˚
˚ ˚˚˚
˚
t
0
0.2
0.4
0.6
0.8
1.0
0
20
40
60
80
100
N(t)
Figure 10.7.
Sample path of a counting process.
with a speciﬁc structure in which these rvs are embedded. This difference is akin to
the difference between marginal and joint distributions, a topic we have highlighted
as very important in Chapter 5 through the notion of copulas; of course, in the
stochastic process case, there also has to be some probabilistic consistency across
time. In a certain sense, the ﬁnite-dimensional problem of Chapter 5 becomes an
inﬁnite-dimensional problem.
After these words of warning on the difference between rvs and stochastic processes, we now take some methodological shortcuts to arrive at our goal. The interested reader wanting to learn more will have to delve deeper into the mathematical
background of stochastic processes in general and counting processes in particular.
The Notes and Comments contain some references.
Deﬁnition 10.23 (counting processes). A stochastic process N = (N(t))t⩾0 is
a counting process if its sample paths are right continuous with left limits existing,
and there exists a sequence of rvs T0 = 0, T1, T2, . . . tending almost surely to ∞
such that N(t) = ∞
k=1 I{Tk⩽t}.
A typical realization of such a process is given in Figure 10.7. We now deﬁne the
homogeneous Poisson process as a special counting process.
Deﬁnition 10.24 (homogeneous Poisson process). A stochastic process N =
(N(t))t⩾0 is a homogeneous Poisson process with intensity (rate) λ > 0 if the
following properties hold:
(i) N is a counting process;
(ii) N(0) = 0, almost surely;
(iii) N has stationary and independent increments; and
(iv) for each t > 0, N(t) ∼Poi(λt).
--- page 502 ---

486
10. Operational Risk and Insurance Analytics
t
0
0.2
0.4
0.6
0.8
1.0
0
20
40
60
80
100
N(t)
Figure 10.8.
Ten realizations of a homogeneous Poisson process with λ = 100.
Remark 10.25. Note that conditions (iii) and (iv) imply that, for 0 < u < v < t,
the rvs N(v) −N(u) and N(t) −N(v) are independent and that, for k ⩾0,
P(N(v) −N(u) = k) = P(N(v −u) = k)
= e−λ(v−u) (λ(v −u))k
k!
.
The rv N(v) −N(u) counts the number of events (claims, losses) in the interval
(u, v]; by stationarity, it has the same df as N(v −u). In Figure 10.8 we have
generated 10 realizations of a homogeneous Poisson process on [0, 1] with λ = 100.
Note the rather narrow band within which the various sample paths fall.
For practical purposes, the following result contains the main properties of the
homogeneous Poisson process.
Theorem 10.26 (characterizations of the homogeneous Poisson process). Suppose that N is a counting process. Then the following statements are equivalent:
(1) N is a homogeneous Poisson process with rate λ > 0;
(2) N has stationary and independent increments and
P(N(t) = 1) = λt + o(t),
as t ↓0,
P(N(t) ⩾2) = o(t),
as t ↓0;
(3) the inter-event times (k = Tk −Tk−1)k⩾1 are iid with df Exp(λ); and
(4) for all t > 0, N(t) ∼Poi(λt) and, given that (N(t) = k), the occurrence times
T1, T2, . . . , Tk have the same distribution as the ordered sample from k independent rvs, uniformly distributed on [0, t]; as a consequence, we can write
the conditional joint density as
fT1,...,Tk|N(t)=k(t1, . . . , tk) = k!
tk I{0<t1<···<tk<t}.
Proof. Many standard textbooks on stochastic processes contain proofs of this
important theorem (see, for example, Mikosch 2004; Resnick 1992).
--- page 503 ---

10.2. Elements of Insurance Analytics
487
Discussion.
Statement (2) in Theorem 10.26 implies that λ can indeed be interpreted as a rate or intensity: λ = limt↓0(1/t)P(N(t) = 1). Moreover, the same
statement implies that a homogeneous Poisson process does not allow for clustering
of events: limt↓0 P(N(t) ⩾2) = 0. Statement (3) gives an event-time deﬁnition of
a homogeneous Poisson process. It follows immediately that the ﬁrst event-time
has an Exp(λ) df: P(T1 > t) = P(N(t) = 0) = e−λt, t ⩾0. Statement (3), however, goes well beyond this by stating that the inter-event times k are iid with
k ∼Exp(λ). This leads to a straightforward way to simulate a stream of loss
events from a homogeneous Poisson process with rate λ. Moreover, this equivalent
deﬁnition immediately yields a generalization by assuming that the k are still iid
but that k ∼F, a general df. The resulting process is a so-called renewal process
(note that the only Markovian renewal process is the homogeneous Poisson process).
Finally, statement (4) yields an easy algorithm to generate the occurrences of
homogeneous Poisson times over the interval [0, t] given that we have in total
k events till t—we simply generate k uniform rvs on [0, t] and order them.
Multivariate Poisson processes.
In many applications we want to model the frequencies of different loss types with a number of Poisson processes while considering possible dependence between loss frequencies for different loss types. More
generally, we might want to construct a number of compound Poisson processes
where loss severities for the different business lines were also dependent. A natural
approach to modelling this dependence is to assume that all losses can be related
to a series of underlying and independent Poisson shock processes. In insurance
these shocks might be natural catastrophes; in credit risk modelling they might be
a variety of economic events, such as local or global recessions; in operational risk
modelling they might be the failure of various IT systems. When a shock occurs this
may cause losses of several different types; the common shock causes the numbers
of losses of each type to be dependent. See Lindskog and McNeil (2003), Pfeifer
and Neˇslehov´a (2004) and Chavez-Demoulin, Embrechts and Neˇslehov´a (2005) for
models of this kind.
10.2.7
Processes Related to the Poisson Process
Using the fundamental building block of the homogeneous Poisson process, one can
construct more general counting processes that are useful for loss-event modelling
in ﬁnance and insurance. Such generalizations include the following.
Renewal processes (mentioned above). The exponential waiting time distribution
is replaced by a general df F.
Inhomogeneous Poisson processes. Theconstantintensityλisreplacedbyadeterministic function λ(·).
Mixed Poisson processes. The deterministic constant intensity λ is replaced by an
rv Λ.
Doubly stochastic or Cox processes. λ is replaced by a stochastic process {λt :
t ⩾0} in accordance with notation used in Chapter 9 (see, for example, Deﬁnition 9.16).
--- page 504 ---

488
10. Operational Risk and Insurance Analytics
Self-exciting or Hawkes processes. λ is replaced by a stochastic process depending only on previous event times. See Section 7.4.3 for a concrete example.
Below, we highlight some features of some of these processes.
Inhomogeneous Poisson process.
Deﬁnition 10.27 (inhomogeneous Poisson). A counting process N is an inhomogeneous Poisson process if, for some deterministic function λ(s) ⩾0, the following
conditions hold:
(i) N(0) = 0, almost surely;
(ii) N has independent increments; and
(iii) for all t ⩾0,
P(N(t + h) −N(t) = 1) = λ(t)h + o(h),
h ↓0,
P(N(t + h) −N(t) ⩾2) = o(h),
h ↓0.
The function λ(·) is referred to as the intensity or rate function. The integral
Λ(t) =
 t
0 λ(s) ds is referred to as the intensity measure (or cumulative intensity
function).
Remark 10.28. A characterization theorem, similar to Theorem 10.26, can be
derived. In particular, we ﬁnd that, for 0 < s < t, N(t)−N(s) ∼Poi(Λ(t)−Λ(s)).
The inhomogeneous Poisson process is a useful tool in loss modelling whenever a
deterministic trend or seasonality component is to be modelled in the loss frequency.
The next example also shows that this process naturally emerges as a counting
process for record losses.
Example 10.29 (records). The world of ﬁnance and insurance abounds with statements on record events: the largest single day drop in the dollar/yen, the most
expensive hurricane, the three best fund managers during the last year, the second
largest loss due to internal fraud, the biggest one-day change in the credit spread of
a particular company, etc. Likewise, the world of records is intimately related to the
(general) theory of Poisson processes. In Notes and Comments we shall give several
references for this. Below we indicate how an easy example related to a question on
records leads to an inhomogeneous Poisson process as a model.
Suppose that the loss rvs Xi ⩾0 are iid with density function f (x) > 0, x ⩾0.
Deﬁne the counting process N:
N(t) =
∞

i=1
I{Xi⩽t and Xi>Xi−j , j=1,...,i−1}.
--- page 505 ---

10.2. Elements of Insurance Analytics
489
N(t) counts the number of records in the sequence (Xi)i⩾1 of size less than t
and (N(t)) is referred to as the record process. It follows that, for h, t > 0,
P(N(t + h) −N(t) ⩾1) =
∞

i=1
P(Xi ∈(t, t + h] and Xi−1 ⩽t, . . . , X1 ⩽t)
=
∞

i=1
(F(t + h) −F(t))(F(t))i−1
= F(t + h) −F(t)
1 −F(t)
=
f (t)
1 −F(t)h + o(h),
as h ↓0.
Moreover, for h, t > 0:
P(N(t + h) −N(t) ⩾2)
⩽

i<j
P(X1 ⩽t, . . . , Xi−1 ⩽t, Xi ∈(t, t + h],
Xi+1 ⩽t + h, . . . , Xj−1 ⩽t + h, Xj ∈(t, t + h])
=
  t+h
t
f (s) ds
2 
i<j
(F(t))i−1(F(t))j−i−1
= o(h2),
as h ↓0.
From these calculations one deduces that the record process N is inhomogeneous
Poisson with rate function λ(t) = f (t)/(1 −F(t)), the so-called hazard rate of F,
a notion that we encountered in Section 9.2.1.
Suppose now that, as in most practical cases, Λ(t) is strictly increasing, so
Λ(Λ−1(t)) = Λ−1(Λ(t)) = t. We can then always transform an inhomogeneous
Poisson process N with integrated intensity Λ into a homogeneous Poisson process
with intensity 1 by a change of time.
Proposition 10.30 (time change, operational time). Suppose that N is an inhomogeneous Poisson process with Λ strictly increasing and deﬁne, for t ⩾0,
˜N(t) = N(Λ−1(t)), then ˜N is homogeneous Poisson with intensity 1.
Proof. For t > 0 ﬁxed and k ⩾0,
P( ˜N(t) = k) = P(N(Λ−1(t)) = k) = e−Λ(Λ−1(t)) (Λ(Λ−1(t)))k
k!
= e−t tk
k!,
so ˜N(t) ∼Poi(t). By deﬁnition, the increments of ˜N are independent; moreover,
for 0 < u < v we have that
P( ˜N(v) −˜N(u) = k) = P(N(Λ−1(v)) −N(Λ−1(u)) = k)
= e−(Λ(Λ−1(v))−Λ(Λ−1(u))) (Λ(Λ−1(v)) −Λ(Λ−1(u)))k
k!
= e−(v−u) (v −u)k
k!
,
from which stationarity follows.
--- page 506 ---

490
10. Operational Risk and Insurance Analytics
This is one of the many examples in insurance and ﬁnance where a more complicated process (N) can be reduced to a standard (easier) model ( ˜N) through
the careful choice of a new time clock (a so-called time change construction)
(see also Section 9.2.3 on credit risk). Proposition 10.30 can be formulated more
generally for Λ not strictly increasing and the converse also holds. Proposition 10.30 justiﬁes the common simplifying assumption that a loss frequency
model is homogeneous (unit rate) Poisson, albeit in many cases only in operational time. The original time-scale of N is slowed down or speeded up in such a
way that, on average, ˜N has one claim per time unit, whereas N has, on average,
Λ(1) claims.
Remark 10.31. A standard way in which an inhomogeneous Poisson process
can be obtained from a homogeneous Poisson process is by random sampling.
Suppose an intensity function λ satisﬁes λ(s) ⩽c < ∞for s ⩾0. Start from
a homogeneous Poisson process with rate c > 0 and denote its arrival times
by T0 = 0, T1, T2, . . . . Construct a new process ˜N from (Ti)i⩾0 through deletion of each Ti independently of the other Tj with probability 1 −(λ(Ti)/c).
The so-called thinned counting process ˜N consists of the remaining (undeleted)
points. It can be shown that this process is inhomogeneous Poisson with intensity
function λ(·).
Mixed Poisson process.
The mixed Poisson rvs of Section 10.2.4 can be embedded
into a so-called mixed Poisson process. A single realization of such a process cannot be distinguished through statistical means from a realization of a homogeneous
Poisson process; indeed, to simulate a sample path, one ﬁrst draws a realization
of the random intensity λ = Λ(ω) and then draws the sample path of the homogeneous Poisson process with rate λ. (Here Λ denotes an rv and not the intensity
measure in the inhomogeneous Poisson case above.) Only by repeating this simulation more frequently does one see the different probabilistic nature of the mixed
Poisson process: compare Figure 10.9 with Figure 10.8. In the former we have
simulated 10 sample paths from a mixed Poisson process with mixing variable
Λ ∼Ga(100, 1) so that E(Λ) = 100. Note the much greater variability in the
paths.
Example 10.32. Whencountingprocessesareusedincreditriskmodellingthetimes
Tk typically correspond to credit events, for instance default or downgradings. More
precisely, a credit event can be constructed as the ﬁrst jump of a counting process N.
The df of the time to the credit event can be easily derived by observing that P(T1 >
t) = P(N(t) = 0). This probability can be calculated in a straightforward way for
a homogeneous Poisson process with intensity λ; we obtain P(N(t) = 0) = e−λt.
When N is a mixed Poisson process with mixing df FΛ we obtain
P(T1 > t) = P(N(t) = 0) =
 ∞
0
e−tλ dFΛ(λ) = ˆFΛ(t),
--- page 507 ---

10.2. Elements of Insurance Analytics
491
t
0
0.2
0.4
0.6
0.8
1.0
0
20
40
60
80
100
N(t)
Figure 10.9.
Ten realizations of a mixed Poisson process with Λ ∼Ga(100, 1).
the Laplace–Stieltjes transform of FΛ in t. In the special case when Λ ∼Ga(α, β),
the negative binomial case treated in Proposition 10.20, one ﬁnds that
P(T1 > t) =
 ∞
0
e−tλ βα
Γ (α)λα−1e−βλ dλ
=
βα
Γ (α)(t + β)−α
 ∞
0
e−ssα−1 ds
= βα(t + β)−α,
t ⩾0,
so that T1 has a Pareto distribution T1 ∼Pa(α, β) (see Section A.2.8).
Processes with stochastic intensity.
A further important class of models is obtained
when λ in the homogeneous Poisson case is replaced by a general stochastic process (λt), yielding a two-tier stochastic model or so-called doubly stochastic process.
For example, one could take λt to be a diffusion or, alternatively, a ﬁnite-state
Markov chain. The latter case gives rise to a regime-switching model: in each state of
the Markov chain the intensity has a different constant level and the process remains
in that state for an exponential length of time, before jumping to another state. In
Figure 10.10 we have simulated the sample path of such a process randomly switching between λ = 10 and λ = 100. In Section 9.2.3 we looked at doubly stochastic
random times, which correspond to the ﬁrst jump of a doubly stochastic Poisson
process.
Notes and Comments
The story behind the name insurance analytics is told in Embrechts (2002). A good
place to start a search for actuarial literature is the website of the InternationalActuarial Association: www.actuaries.org. Several interesting books can be found on the
website of the Society of Actuaries, www.soa.org (whose postal address is, coincidentally, 475 North Martingale Rd #600, Schaumburg, Illinois). A standard Society
of Actuaries textbook on actuarial mathematics is Bowers et al. (1986); ﬁnancial
economics for actuaries is to be found in Panjer et al. (1998). For our purposes excellent texts are Mikosch (2004) and Partrat and Besson (2004). Rolski et al. (1999)
--- page 508 ---

492
10. Operational Risk and Insurance Analytics
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
•
•
•
•
•
•
•
•
•
•
•
•
•
•
•
•
•
•
•
•
•
˚
˚
˚
˚
˚
˚
˚
˚
˚
˚
˚
˚
˚
˚
˚
˚
˚
˚
˚
˚
˚
t
0
0.2
0.4
0.6
0.8
1.0
0
5
10
15
20
= 10
= 100
= 10
N(t)
λ
λ
λ
Figure 10.10.
Realization of a counting process with
a regime switch from λ = 10 to λ = 100.
gives a broad, more technical overview of the relevant stochastic process models. In
Chapter 6 we have given several references to actuarial tools relevant for the study
of risk measures; key words there were premium principles (Section 6.1), comonotonicity (Sections 5.1.6 and 6.2.2) and Fr´echet bounds (Sections 5.1.6 and 6.2).
Finally, an overview of the state of the art of actuarial modelling is to be found in
Teugels and Sundt (2004).
Actuarial textbooks dealing in particular with the modelling of loss distributions in
insurance are Hogg and Klugman (1984) and Klugman, Panjer and Willmot (1998).
Besides the general references above, an early textbook discussion of the use of
numerical methods for the calculation of the df of total loss amount rvs is Feilmeier
and Bertram (1987); B¨uhlmann (1984) contains a ﬁrst comparison between the FFT
method and Panjer recursion. More extensive comparisons, taking rounding and discretization errors into account, are found in Gr¨ubel and Hermesmeier (1999, 2000).
A discussion of the use of the FFT in insurance is given in Embrechts, Gr¨ubel and
Pitts (1993).Algorithms for the FFT are freely available on the Web, as a search will
quickly reveal. The original paper by Panjer (1981) also contains a density version of
Theorem 10.15. For an application of Panjer recursion to credit risk measurement
within the CreditRisk+ framework, see Credit Suisse Financial Products (1997).
Based on Giese (2003), Haaf, Reiss and Schoenmakers (2004) propose an alternative recursive method. For more recent work on Panjer recursion, especially in the
multivariate case, see, for example, Hesselager (1996) and Sundt (1999, 2000).
Asymptotic approximation methods going beyond the normal approximation
(10.13) are known in statistics under the names Berry–Ess´een, Edgeworth and
saddle-point.The former two are discussed, for example, in Embrechts, Kl¨uppelberg
and Mikosch (1997) and are of more theoretical importance. The saddle-point technique is very useful: see Jensen (1995) for an excellent summary, and Embrechts
et al. (1985) for an application to compound distributions. Gordy (2002) discusses
the importance of saddle-point methods for credit risk modelling, again within the
--- page 509 ---

10.2. Elements of Insurance Analytics
493
context of CreditRisk+. Wider applications within risk management can be found
in Studer (2001) and Glasserman (2003a,b)
Poisson mixture models with insurance applications in mind are summarized in
Grandell (1997) (see also Bening and Korolev 2002). In order to enter more deeply
into the world of counting processes, one has to study the theory of point processes.
Very comprehensive and readable accounts are Daley and Vere-Jones (2003) and
Karr (1991).A study of this theory is both mathematically demanding and practically
rewarding. Such models are being used increasingly in credit risk. The notion of
time change is fundamental to many applications in insurance and ﬁnance; for an
example of how it can be used to model operational risk, see Embrechts, Kaufmann
and Samorodnitsky (2004). For its introduction into ﬁnance, see An´e and Geman
(2000) and Dacorogna et al. (2001). An excellent survey is to be found in Peeters
(2004).
What have we not included in our brief account of the elements of insurance
analytics? We have not treated ruin theory and the general stochastic process theory
of insurance risk, credibility theory, dynamic ﬁnancial analysis, also referred to as
dynamic solvency testing, and reinsurance, to name but a few omissions.
The stochastic process theory of insurance risk has a long tradition. The ﬁrst
fundamental summary came through the pioneering work of Cram´er (1994a,b).
B¨uhlmann (1970) made the ﬁeld popular to several generations of actuaries. This
early work has now been generalized in every way possible. A standard textbook on
ruin theory isAsmussen (2000). The modelling of large claims and its consequences
for ruin estimates can be found in Embrechts, Kl¨uppelberg and Mikosch (1997).
Credibility theory concerns premium calculation for non-homogeneous portfolios
and has a very rich history rooted in non-life insurance mathematics. Its basic concepts were ﬁrst developed by American actuaries in the 1920s; pioneering papers
in this early period were Mowbray (1914) and Whitney (1918). Further important
work is found in the papers of Bailey (1945), Robbins (1955, 1964) and B¨uhlmann
(1967, 1968, 1971). An excellent review article tracing the historical development
of the basic ideas is Norberg (1979); see also Jewell (1990) for a more recent review.
Various textbook versions exist: B¨uhlmann and Gisler (2005) give an authoritative
account of its actuarial usage and hint at applications to ﬁnancial risk management.
Dynamic ﬁnancial analysis (DFA), also referred to as dynamic solvency testing
(DST), is a systematic approach, based on large-scale computer simulations, for
the integrated ﬁnancial modelling of non-life insurance and reinsurance companies
aimed at assessing the risks and beneﬁts associated with strategic decisions (see
Blum 2005; Blum and Dacorogna 2004). An easy introduction can be found in
Kaufmann, Gadmer and Klett (2001). The interested reader can consult the website
of the Casualty Actuarial Society (www.casact.org/research/drm).
--- page 510 ---

Appendix
A.1
Miscellaneous Deﬁnitions and Results
A.1.1
Type of Distribution
Deﬁnition A.1 (equality in type). Two rvs V and W (or their distributions) are
said to be of the same type if there exist constants a > 0 and b ∈R such that
V
d= aW + b.
In other words, distributions of the same type are obtained from one another by
location and scale transformations.
A.1.2
Generalized Inverses and Quantiles
Let T be an increasing function, i.e. a function satisfying y > x =⇒T (y) ⩾T (x),
with strict inequality on the right-hand side for some pair y > x. Thus an increasing
function may have ﬂat sections; if we want to rule this out, we stipulate that T is
strictly increasing, so y > x ⇐⇒T (y) > T (x). We ﬁrst note some useful facts
concerning what happens when increasing transformations are applied to rvs.
Lemma A.2.
(i) If X is an rv and T is increasing, then {X ⩽x} ⊂{T (X) ⩽T (x)} and
P(T (X) ⩽T (x)) = P(X ⩽x) + P(T (X) = T (x), X > x).
(A.1)
(ii) If F is the df of the rv X, then P(F(X) ⩽F(x)) = P(X ⩽x).
The second statement follows from (A.1) by noting that, for any x, the event given
by {F(X) = F(x), X > x} corresponds to a ﬂat piece of the df F and thus has zero
probability mass.
The generalized inverse of an increasing function T is deﬁned to be T ←(y) =
inf{x : T (x) ⩾y}, where we use the convention inf ∅= ∞. Strictly speaking,
this generalized inverse is known as the left-continuous generalized inverse. The
following basic properties may be veriﬁed quite easily.
Proposition A.3 (properties of the generalized inverse). For T increasing, the
following hold.
(i) T ←is an increasing, left-continuous function.
(ii) T is continuous ⇐⇒T ←is strictly increasing.
(iii) T is strictly increasing ⇐⇒T ←is continuous.
For the remaining properties assume additionally that T ←(y) < ∞.
--- page 511 ---

A.1. Miscellaneous Deﬁnitions and Results
495
F(x)
0
α
1
q  (F)
α
q  (F)
α
x
x
(a)
(b)
Figure A.1.
Calculation of quantiles in tricky cases. The ﬁrst case (a) is a continuous df,
but the ﬂat piece corresponds to an interval with zero probability mass. In the second case (b)
there is an atom of probability mass such that, for X with df F, we have P(X = qα(F)) > 0.
(iv) If T is right-continuous, T (x) ⩾y ⇐⇒T ←(y) ⩽x.
(v) T ←◦T (x) ⩽x.
(vi) T ◦T ←(y) ⩾y.
(vii) T is strictly increasing =⇒T ←◦T (x) = x.
(viii) T is continuous =⇒T ◦T ←(y) = y.
We apply the idea of generalized inverses to distribution functions. If F is a df,
then the generalized inverse F ←is known as the quantile function of F. In this
case, for α ∈(0, 1), we also use the alternative notation qα(F) = F ←(α) for the
α-quantile of F. Figure A.1 illustrates the calculation of quantiles in two tricky
cases.
In general, since a df need not be strictly increasing (part (a) of the ﬁgure), we have
F ←◦F(x) ⩽x, by Proposition A.3(v). But the values x, where F ←◦F(x)̸ = x,
correspond to ﬂat pieces and have zero probability mass. That is, we have the following useful fact.
Proposition A.4. If X is an rv with df F, then P(F ←◦F(X) = X) = 1.
A.1.3
Karamata’s Theorem
The following result for regularly varying functions is used in Chapter 7. For more
details see Bingham, Goldie and Teugels (1987). Essentially, the result says that the
slowly varying function can be taken outside the integral as if it were a constant. Note
that the symbol “∼” indicates asymptotic equality here, i.e. if we write a(x) ∼b(x)
as x →x0, we mean limx→x0 a(x)/b(x) = 1.
Theorem A.5 (Karamata’s Theorem). Let L be a slowly varying function which
is locally bounded in [x0, ∞) for some x0 ⩾0. Then,
(a) for κ > −1,
 x
x0
tκL(t) dt ∼
1
κ + 1xκ+1L(x), x →∞,
(b) for κ < −1,
 ∞
x
tκL(t) dt ∼−
1
κ + 1xκ+1L(x), x →∞.
--- page 512 ---

496
Appendix
A.2
Probability Distributions
The gamma and beta functions appear in the deﬁnitions of a number of these distributions. The gamma function is
Γ (α) =
 ∞
0
xα−1e−x dx,
α > 0,
(A.2)
and satisﬁes the useful recursive relationship Γ (α + 1) = αΓ (α). The β function
is
β(a, b) =
 1
0
xa−1(1 −x)b−1 dx,
a, b > 0.
(A.3)
It is related to the gamma function by β(a, b) = Γ (a)Γ (b)/Γ (a + b).
A.2.1
Beta
The rv X has a beta distribution, written X ∼Beta(a, b), if its density is
f (x) =
1
β(a, b)xa−1(1 −x)b−1,
0 < x < 1, a, b > 0,
(A.4)
where β(a, b) is the beta function in (A.3). The uniform distribution X ∼U(0, 1) is
obtained as a special case when a = b = 1.The mean and variance of the distribution
are, respectively, E(X) = α/(α + β) and var(X) = (αβ)/((α + β + 1)(α + β)2).
A.2.2
Exponential
The rv X has an exponential distribution, written X ∼Exp(λ), if its density is
f (x) = λ exp(−λx),
x > 0, λ > 0.
(A.5)
The mean of this distribution is E(X) = λ−1 and the variance is var(X) = λ−2.
A.2.3
F
The rv X has an F distribution, written X ∼F(ν1, ν2), if its density is
f (x) =
1
β( 1
2ν1, 1
2ν2)
ν1
ν2
ν1/2
x(ν1−2)/2
(1 + ν1x/ν2)(ν1+ν2)/2 ,
x > 0, ν1, ν2 > 0.
(A.6)
The mean of this distribution is E(X) = ν2/(ν2 −2) provided that ν2 > 2. Provided
that ν2 > 4, the variance is
var(X) = 2

ν2
ν2 −2
2 ν1 + ν2 −2
ν1(ν1 −4) .
A.2.4
Gamma
The rv X has a gamma distribution, written X ∼Ga(α, β), if its density is
f (x) =
βα
Γ (α)xα−1 exp(−βx),
x > 0, α > 0, β > 0,
(A.7)
where Γ (α) denotes the gamma function in (A.2). Using the recursive property of
the gamma function, the mean and variance of the gamma distribution are easily
--- page 513 ---

A.2. Probability Distributions
497
calculated to be E(X) = α/β and var(X) = α/β2. For ﬁtting a multivariate t distribution using the EM approach of Section 3.2.4 it is also useful to know that
E(ln X) = ψ(α) −ln(β), where ψ(k) = d ln(Γ (k))/dk is the digamma or psi
function.
An exponential distribution is obtained in the special case when α = 1. If X ∼
Ga(α, β) and k > 0, then kX ∼Ga(α, β/k). For two independent gamma variates
X1 ∼Ga(α1, β) and X2 ∼Ga(α2, β) we have that X1+X2 ∼Ga(α1+α2, β). Note
also that, if X ∼Ga( 1
2ν, 1
2), then X has a chi-squared distribution with ν degrees
of freedom, also written X ∼χ2
ν .
A.2.5
Generalized Inverse Gaussian
The rv X has a generalized inverse Gaussian (GIG) distribution, written X ∼
N−(λ, χ, ψ), if its density is
f (x) = χ−λ(√χψ)λ
2Kλ(√χψ) xλ−1 exp(−1
2(χx−1 + ψx)),
x > 0,
(A.8)
where Kλ denotes a modiﬁed Bessel function of the third kind with index λ and the
parameters satisfy χ > 0, ψ ⩾0 if λ < 0; χ > 0, ψ > 0 if λ = 0; and χ ⩾0,
ψ > 0 if λ > 0. For more on this Bessel function see Abramowitz and Stegun
(1965).
The GIG density actually contains the gamma and inverse gamma densities as special limiting cases, corresponding to χ = 0 and ψ = 0, respectively. In these cases
(A.8)mustbeinterpretedasalimit,whichcanbeevaluatedusingtheasymptoticrelations Kλ(x) ∼Γ (λ)2λ−1x−λ as x →0+ for λ > 0 and Kλ(x) ∼Γ (−λ)2−λ−1xλ
as x →0+ for λ < 0.The fact that Kλ(x) = K−λ(x) is also useful. In this way it can
be veriﬁed that, for λ > 0 and χ = 0, X ∼Ga(λ, 1
2ψ). If λ < 0 and ψ = 0, we have
X ∼Ig(−λ, 1
2χ). The case λ = −1
2 is known as the inverse Gaussian distribution.
Note that, in general, if Y ∼N−(λ, χ, ψ), then 1/Y ∼N−(−λ, ψ, χ).
For the non-limiting case when χ > 0 and ψ > 0 it may be calculated that
E(Xα) =
 χ
ψ
α/2 Kλ+α(√χψ)
Kλ(√χψ) ,
α ∈R,
(A.9)
E(ln X) = dE(Xα)
dα

α=0
.
(A.10)
A.2.6
Inverse Gamma
The rv X has an inverse gamma distribution, written X ∼Ig(α, β), if its density is
f (x) =
βα
Γ (α)x−(α+1) exp(−β/x),
x > 0, α > 0, β > 0.
(A.11)
Note that if Y ∼Ga(α, β), then 1/Y ∼Ig(α, β). Provided that α > 1, the
mean is E(X) = β/(α −1), and provided that α > 2 the variance is var(X) =
β2/((α −1)2(α −2)). Moreover, E(ln X) = ln(β) −ψ(α).
--- page 514 ---

498
Appendix
A.2.7
Negative Binomial
The rv N has a negative binomial distribution with parameters α > 0 and 0 < p < 1,
written X ∼NB(α, p), if its probability mass function is
P(N = k) =
α + k −1
k

pα(1 −p)k,
k = 0, 1, 2, . . . ,
(A.12)
where
+x
k
,
for x ∈R and k ∈N0 denotes an extended binomial coefﬁcient deﬁned
by
+x
0
,
= 1 and
x
k

= x(x −1) · · · (x −k + 1)
k!
,
k > 0.
The moments of this distribution are
E(N) = α(1 −p)/p
and
var(N) = α(1 −p)/p2.
For α = r ∈N the rv N + r represents the waiting time until the rth success
in independent Bernoulli trials with success probability p, i.e. the total number of
trials that are required until we have r successes. For α = 1 the rv N + 1 is said to
have a geometric distribution.
A.2.8
Pareto
The rv X has a Pareto distribution, written X ∼Pa(α, κ), if its df is
F(x) = 1 −

κ
κ + x
α
,
α, κ > 0, x ⩾0.
(A.13)
Provided that α > n, the moments of this distribution are given by
E(Xn) =
κnn!
n
i=1(α −i).
A.2.9
Stable
The rv X has an α-stable distribution, written X ∼St(α, β, γ, δ), if its characteristic
function is
φ(t) = E exp(itX) =

exp(−γ α|t|α(1 −iβ sign(t) tan(π/2)α) + iδt),
α̸ = 1,
exp(−γ |t|(1 + iβ sign(t)(2/π) ln |t|) + iδt),
α = 1,
(A.14)
where α ∈(0, 2], β ∈[−1, 1], γ > 0 and δ ∈R. Note that there are various
alternative parametrizations of the stable distributions and we use a parametrization
of Nolan (2005, Deﬁnition 1.8). The case X ∼St(α, 1, γ, 0) for α < 1 gives a distribution on the positive half-axis, which we refer to as a positive stable distribution.
A simulation algorithm for a standardized variate Z ∼St(α, β, 1, 0) is given
in Nolan (2005, Theorem 1.19). In the case where α̸ = 1, X = δ + γ Z has a
St(α, β, γ, δ) distribution; the case α = 1 is more complicated.
