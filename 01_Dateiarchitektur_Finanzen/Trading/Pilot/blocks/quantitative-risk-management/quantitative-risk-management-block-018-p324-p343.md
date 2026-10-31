# Quantitative Risk Management_ Concepts, Techniques, and -- Alexander J_ McNeil, Rüdiger Frey, Paul Embrechts -- Princeton series in finance, -- isbn13 9780691122557 -- 478a0059673fecd0c76229cd3d8884e7 -- Anna’s Arc.pdf — pages 324–343

--- page 324 ---

308
7. Extreme Value Theory
where marks have a generalized Pareto distribution, but are unpredictable, meaning
that the excess losses are iid GPD. In the second model we consider the case of
predictable marks. In this model the excess losses are conditionally generalized
Pareto, given the exceedance history up to the time of the mark, with a scaling
parameter that depends on that history. In this way we get a model where, in a
period of excitement, both the temporal intensity of occurrence and the magnitude
of the exceedances increase.
In point process language our models are processes N(·) on a state space of the
form X = (0, n] × (u, ∞) such that N(A) = n
i=1 I{(i,Xi)∈A} for sets A ⊂X. To
build these models we start with the intensity of the reparametrized version of the
standard POT model given in (7.37). We recall that this model simply says that
exceedances of the threshold u occur as a homogeneous Poisson process with rate τ
and that excesses have a generalized Pareto distribution with df Gξ,β.
Model with unpredictable marks.
We ﬁrst introduce the notation v∗(t)
=

j:0<Tj <th(t −Tj, ˜Xj −u) for the self-excitement function, where the function h
is as in Section 7.4.3. We generalize (7.37) and consider a self-exciting model with
conditional intensity
λ∗(t, x) = τ + ψv∗(t)
β

1 + ξ x −u
β
−1/ξ−1
(7.39)
on a state space X = (0, n] × (u, ∞), where τ > 0 and ψ ⩾0. Effectively, we
have combined the one-dimensional intensity in (7.38) with a GPD density. When
ψ = 0 we have an ordinary POT model with no self-exciting structure.
It is easy to calculate that the conditional rate of crossing the threshold x ⩾u at
time t, given information up to that time, is
τ ∗(t, x) =
 ∞
x
λ∗(t, y) dy = (τ + ψv∗(t))

1 + ξ x −u
β
−1/ξ
,
(7.40)
which, for ﬁxed x, is simply a one-dimensional self-exciting process of the form
(7.38). The implied distribution of the excess losses when an exceedance takes place
is generalized Pareto, because
τ ∗(t, u + x)
τ ∗(t, u)
=

1 + ξx
β
−1/ξ
= ¯Gξ,β(x),
(7.41)
independently of t. Statistical ﬁtting of this model is performed by maximizing a
likelihood of the form
L(θ; data) = exp

−nτ −ψ
 n
0
v∗(s) ds
 Nu
!
j=1
λ∗(Tj, ˜Xj).
(7.42)
A model with predictable marks.
A model with predictable marks can be obtained
by generalizing (7.39) to get
λ∗(t, x) = τ + ψv∗(t)
β + αv∗(t)

1 + ξ
x −u
β + αv∗(t)
−1/ξ−1
,
(7.43)
--- page 325 ---

7.4. Point Process Models
309
where β > 0 and α ⩾0. For simplicity we have assumed that the GPD scaling is
also linear in the self-excitement function v∗(t). The properties of this model follow
immediately from the model with unpredictable marks. The conditional crossing
rate of the threshold x ⩾u at time t is as in (7.40) with the parameter β replaced by
the time-dependent self-exciting function β + αv∗(t). By repeating the calculation
in (7.41) we ﬁnd that the distribution of the excess loss over the threshold, given
that an exceedance takes place at time t and given the history of exceedances up
to time t, is generalized Pareto with df Gξ,β+αv∗(t). The likelihood for ﬁtting the
model is again (7.42), where the function λ∗(t, x) is now given by (7.43). Note that
by comparing a model with α = 0 and a model with α > 0 we can formally test the
hypothesis that the marks are unpredictable using a likelihood ratio test
Example 7.42 (self-exciting POT model for S&P daily loss data). We continue
the analysis of the data of Example 7.41 by ﬁtting self-exciting POT models with
both unpredictable and predictable marks to the 200 exceedances of the threshold
u = 1.5%. The former is equivalent to ﬁtting a self-exciting model to the exceedance
times as in Example 7.41 and then ﬁtting a GPD to the excess losses over the
threshold; thus the estimated intensity of crossing the threshold is identical to the
one shown in Figure 7.13. The log-likelihood for this model is −783.4, whereas a
model with predictable marks gives a value of −779.3 for one extra parameter α;
in a likelihood ratio test the p-value is 0.004, showing a signiﬁcant improvement.
In Figure 7.14 we show the exceedance data as well as the estimated intensity
τ ∗(t, u) of exceeding the threshold in the model with predictable marks. We also
show the estimated mean of the GPD for the conditional distribution of the excess
loss above the threshold, given that an exceedance takes place at time t. The GPD
mean (β + αv∗(t))/(1 −ξ) and the intensity τ ∗(t, u) are both afﬁne functions of
the self-excitement function v∗(t) and obviously follow its path.
Calculating conditional risk measures.
Finally, we note that self-exciting POT
models can be used to estimate a kind of analogue of a conditional VaR and also
a conditional expected shortfall. If we have analysed n daily data ending on day t
and want to calculate, say, a 99% VaR, then we treat the problem as a (conditional)
return-level problem; we look for the level at which the conditional exceedance
intensity at a time point just after t (denoted by t+) is 0.01. In general, to calculate
a conditional estimate of VaRt
α (for α sufﬁciently large) we would attempt to solve
the equation τ ∗(t+, x) = (1 −α) for some value of x satisfying x ⩾u. In the
model with predictable marks this is possible if τ + ψv∗(t+) > 1 −α and gives
the formula
VaRt
α = u + β + αv∗(t+)
ξ

1 −α
τ + ψv∗(t+)
−ξ
−1

.
The associated conditional expected shortfall could then be calculated by observing
that the conditional distribution of excess losses above VaRt
α given information up to
time t is GPD with shape parameter ξ and scaling parameter given by β+αv∗(t+)+
ξ(VaRt
α −u).
--- page 326 ---

310
7. Extreme Value Theory
Intensity
0.10
0.20
0.30
Times
GPD mean
0
500
1000
1500
2000
0.6
0.8
1.0
1.2
1.4
2
4
6
(a)
(b)
(c)
Figure 7.14.
(a) Exceedance pattern for 200 largest daily losses in S&P data. (b) Estimated
intensity of exceeding the threshold in a self-exciting POT model with predictable marks.
(c) Mean of the conditional generalized Pareto distribution of the excess loss above the
threshold. See Example 7.42 for details.
Notes and Comments
For more information about point processes consult EKM, Cox and Isham (1980),
Kallenberg (1983) and Resnick (1987). The point process approach to extremes
dates back to Pickands (1971) and is also discussed in Leadbetter, Lindgren and
Rootz´en (1983), Leadbetter (1991) and Falk, H¨usler and Reiss (1994).
The two-dimensional Poisson point process model was ﬁrst used in practice by
Smith (1989) and may also be found in Smith and Shively (1995); both these papers
discuss the adaptation of the point process model to incorporate covariates or time
trends in the context of environmental data. An insurance application is treated
in Smith and Goodman (2000), which also treats the point process model from a
Bayesian perspective. An interesting application to wind storm losses is Rootz´en
and Tajvidi (1997).A further application of the bivariate point process framework to
model insurance loss data showing trends in both intensity and severity of occurrence
is found in McNeil and Saladin (2000). For further applications to insurance and
ﬁnance, see Chavez-Demoulin and Embrechts (2004). An excellent overview of
statistical approaches to the GPD and point process models is found in Coles (2001).
The derivation of likelihoods for point process is beyond the scope of this book
and we have simply recorded the likelihoods to be maximized without further justiﬁ-
cation. See Daley and Vere-Jones (2003, Chapter 7) for more details on this subject;
see also Coles (2001, p. 127) for a good intuitive account in the Poisson case.
The original reference to the Hawkes self-exciting process is Hawkes (1971).
There is a large literature on the application of such processes to earthquake modelling; a starter reference is Ogata (1988). The application to ﬁnancial data was
--- page 327 ---

7.5. Multivariate Maxima
311
suggested in Chavez-Demoulin, Davison and McNeil (2005). The idea of a POT
model with self-exciting structure explored in Section 7.4.4 is new.
7.5
Multivariate Maxima
In this section we give a brief overview of the theory of multivariate maxima, stating
the main results in terms of copulas.A class of copulas known as extreme value copulas emerges as the class of natural limiting dependence structures for multivariate
maxima. These provide useful dependence structures for modelling the joint tail
behaviour of risk factors that appear to show tail dependence. The main reference
is Galambos (1987), which is one of the few texts to treat the theory of multivariate
maxima as a copula theory (although Galambos does not use the word, referring to
copulas simply as dependence functions).
7.5.1
Multivariate Extreme Value Copulas
Let X1, . . . , Xn be iid random vectors in Rd with joint df F and marginal dfs
F1, . . . , Fd. We label the components of these vectors Xi = (Xi,1, . . . , Xi,d)′ and
interpret them as losses of d different types. We deﬁne the maximum of the jth
component to be Mn,j = max(X1,j, . . . , Xn,j), j = 1, . . . , d. In classical multivariate EVT the object of interest is the vector of componentwise block maxima:
Mn = (Mn,1, . . . , Mn,d)′. In particular, we are interested in the possible multivariate
limiting distributions for Mn under appropriate normalizations, much as in the univariate case. It should, however, be observed that the vector Mn will in general not
correspond to any of the vector observations Xi.
We seek limit laws for
Mn −dn
cn
=
Mn,1 −dn,1
cn,1
, . . . , Mn,d −dn,d
cn,d
′
,
as n →∞, where cn = (cn,1, . . . , cn,d)′ and dn = (dn,1, . . . , dn,d)′ are vectors of normalizing constants, the former satisfying cn > 0. Note that in this and
other statements in this section, arithmetic operations on vectors of equal length are
understood as componentwise operations. Supposing that (Mn −dn)/cn converges
in distribution to a random vector with joint df H, we have
lim
n→∞P
Mn −dn
cn
⩽x

= lim
n→∞F n(cnx + dn) = H(x).
(7.44)
Deﬁnition 7.43 (MEV distribution and domain of attraction). If (7.44) holds
for some F and some H, we say that F is in the maximum domain of attraction
of H, written F ∈MDA(H), and we refer to H as a multivariate extreme value
distribution (MEV distribution).
The convergence issue for multivariate maxima is already partly solved by the
univariate theory. If H has non-degenerate margins, then these must be univariate
extreme value distributions of Fr´echet, Gumbel or Weibull type. Since these are continuous, Sklar’s Theorem tells us that H must have a unique copula. The following
theorem asserts that this copula C must have a particular kind of scaling behaviour.
--- page 328 ---

312
7. Extreme Value Theory
Theorem 7.44 (EV copula). If (7.44) holds for some F and some H with GEV
margins, then the unique copula C of H satisﬁes
C(ut) = Ct(u),
∀t > 0.
(7.45)
Any copula with the property (7.45) is known as an extreme value copula (EV copula) and can be the copula of an MEV distribution. The independence and comonotonicity copulas are EV copulas and the Gumbel copula provides an example of a
parametric EV copula family. The bivariate version in (5.11) obviously has property (7.45), as does the exchangeable higher-dimensional Gumbel copula based
on (5.38) as well as the non-exchangeable versions based on (5.43)–(5.45).
There are a number of mathematical results characterizing MEV distributions and
EV copulas. One such result is the following.
Theorem 7.45 (Pickands representation). The copula C is an EV copula if and
only if it has the representation
C(u) = exp

B

ln u1
d
k=1 ln uk
, . . . ,
ln ud
d
k=1 ln uk

d

i=1
ln ui

,
(7.46)
where B(w) =

Sd max(x1w1, . . . , xdwd) dH(x) and H is a ﬁnite measure on the
d-dimensional simplex, i.e. the set Sd = {x : xi ⩾0, i = 1, . . . , d, d
i=1 xi = 1}.
The function B(w) is sometimes referred to as the dependence function of the EV
copula. In the general case, such functions are difﬁcult to visualize and work with,
but in the bivariate case they have a simple form which we discuss in more detail.
In the bivariate case we redeﬁne B(w) as a function of a scalar argument by
setting A(w) := B((w, 1−w)′) with w ∈[0, 1]. It follows from Theorem 7.45 that
a bivariate copula is an EV copula if and only if it takes the form
C(u1, u2) = exp

(ln u1 + ln u2)A

ln u1
ln u1 + ln u2

,
(7.47)
where A(w) =
 1
0 max((1 −x)w, x(1 −w)) dH(x) for a measure H on [0, 1]. It
can be inferred that such bivariate dependence functions must satisfy
max(w, 1 −w) ⩽A(w) ⩽1,
0 ⩽w ⩽1,
(7.48)
and must moreover be convex. Conversely, a differentiable, convex function A(w)
satisfying (7.48) can be used to construct an EV copula using (7.47).
The upper and lower bounds in (7.48) have intuitive interpretations. If A(w) = 1
for all w, then the copula (7.47) is clearly the independence copula, and if A(w) =
max(w, 1−w), then it is the comonotonicity copula. It is also useful to note, and easy
to show, that we can extract the dependence function from the EV copula in (7.47)
by setting
A(w) = −ln C(e−w, e−(1−w)),
w ∈[0, 1].
(7.49)
Example 7.46 (Gumbel copula). We consider the asymmetric version of the bivariate Gumbel copula deﬁned by (5.11) and construction (5.43), i.e. the copula
CGu
θ,α,β(u1, u2) = u1−α
1
u1−β
2
exp{−((−α ln u1)θ + (−β ln u2)θ)1/θ}.
--- page 329 ---

7.5. Multivariate Maxima
313
0.2
0.4
0.6
0.6
0.5
0.7
0.8
0.9
1.0
0.6
0.5
0.7
0.8
0.9
1.0
0.8
1.0
0
0.2
0.4
0.6
0.8
1.0
0
w
w
A(w)
A(w)
(a)
(c)
(d)
(b)
Figure7.15.
Plotofdependencefunctionsfor(a)thesymmetricGumbel,(b)theasymmetric
Gumbel, (c) the symmetric Galambos and (d) the asymmetric Galambos copulas (asymmetric
cases have α = 0.9 and β = 0.8) as described in Examples 7.46 and 7.47. Dashed lines show
boundaries of the triangle in which the dependence function must reside; solid lines show
dependence functions for a range of parameter values.
As already remarked, this copula has the scaling property (7.45) and is an EV copula.
Using (7.49) we calculate that the dependence function is given by
A(w) = (1 −α)w + (1 −β)(1 −w) + ((αw)θ + (β(1 −w))θ)1/θ.
We have plotted this function in Figure 7.15 for a range of θ values running from 1.1
to 10 in steps of size 0.1. Part (a) shows the standard symmetric Gumbel copula with
α = β = 1; the dependence function essentially spans the whole range from independence, represented by the upper edge of the dashed triangle, to comonotonicity,
represented by the two lower edges of the dashed triangle which comprise the function A(w) = max(w, 1 −w). Part (b) shows an asymmetric example with α = 0.9
and β = 0.8; in this case we still have independence when θ = 1, but the limit as
θ →∞is no longer the comonotonicity model. The Gumbel copula model is also
sometimes known as the logistic model.
Example 7.47 (Galambos copula). This time we begin with the dependence function given by
A(w) = 1 −((αw)−θ + (β(1 −w))−θ)−1/θ,
(7.50)
where 0 ⩽α, β ⩽1 and 0 < θ < ∞. It can be veriﬁed that this is a convex function
satisfying max(w, 1 −w) ⩽A(w) ⩽1 for 0 ⩽w ⩽1, so it can be used to create
an EV copula in (7.47). We obtain the copula
CGal
θ,α,β(u1, u2) = u1u2 exp{((−α ln u1)−θ + (−β ln u2)−θ)−1/θ},
--- page 330 ---

314
7. Extreme Value Theory
which has also been called the negative logistic model. We have plotted this function
in Figure 7.15 for a range of θ values running from 0.2 to 5 in steps of size 0.1.
Part (c) shows the standard symmetric case with α = β = 1 spanning the whole
range from independence to comonotonicity. Part (d) shows an asymmetric example
with α = 0.9 and β = 0.8; in this case we still approach independence as θ →0,
but the limit as θ →∞is no longer the comonotonicity model.
A number of other bivariate EV copulas have been described in the literature (see
Notes and Comments).
7.5.2
Copulas for Multivariate Minima
The structure of limiting copulas for multivariate minima can be easily inferred from
the structure of limiting copulas for multivariate maxima; moving from maxima to
minima essentially involves the same considerations that we made at the end of
Section 7.1.1 and uses identity (7.2) in particular.
Normalized componentwise minima of iid random vectors X1, . . . , Xn with df
F will converge in distribution to a non-degenerate limit if the df ˜F of the random vectors −X1, . . . , −Xn is in the maximum domain of attraction of an MEV
distribution (see Deﬁnition 7.43), written ˜F ∈MDA(H). Of course, for a radially
symmetric distribution, ˜F coincides with F.
Let M∗
n be the vector of componentwise maxima of −X1, . . . , −Xn so that
M∗
n,j = max(−X1,j, . . . , −Xn,j). If ˜F ∈MDA(H) for some non-degenerate H,
we have
lim
n→∞P
M∗
n −dn
cn
⩽x

= lim
n→∞
˜F n(cnx + dn) = H(x)
(7.51)
for appropriate sequences of normalizing vectors cn and dn, and an MEV distribution H of the form H(x) = C(Hξ1(x1), . . . , Hξd(xd)), where Hξj denotes a GEV
distribution with shape parameter ξj and C is an EV copula satisfying (7.45).
Deﬁning the vector of componentwise minima by mn and using (7.2), it follows
from (7.51) that
lim
n→∞P
mn + dn
cn
⩾x

= H(−x),
so that normalized minima converge in distribution to a limit with survival function
H(−x) = C(Hξ1(−x1), . . . , Hξd(−xd)). It follows that the copula of the limiting
distributionoftheminimaisthesurvivalcopulaofC (seeSection5.1.5fordiscussion
of survival copulas). In general, the limiting copulas for minima are survival copulas
of EV copulas and concrete examples of such copulas are the Gumbel and Galambos
survival copulas.
In the special case of a radially symmetric underlying distribution, the limiting
copula of the minima is precisely the survival copula of the limiting EV copula of
the maxima.
7.5.3
Copula Domains of Attraction
As in the case of univariate maxima we would like to know which underlying
multivariate dfs F are attracted to which MEV distributions H. We now give a
--- page 331 ---

7.5. Multivariate Maxima
315
useful result in terms of copulas which is essentially due to Galambos (see Notes
and Comments).
Theorem 7.48. Let F(x) = C(F1(x1), . . . , Fd(xd)) for continuous marginal dfs
F1, . . . , Fd and some copula C. Let H(x) = C0(H1(x1), . . . , Hd(xd)) be an MEV
distribution with EV copula C0. Then F ∈MDA(H) if and only if Fi ∈MDA(Hi)
for 1 ⩽i ⩽d and
lim
t→∞Ct(u1/t
1 , . . . , u1/t
d ) = C0(u1, . . . , ud),
u ∈[0, 1]d.
(7.52)
This result shows that the copula C0 of the limiting MEV distribution is determined solely by the copula C of the underlying distribution according to (7.52); the
marginal distributions of F determine the margins of the MEV limit but are irrelevant to the determination of its dependence structure. This motivates us to introduce
the concept of a copula domain of attraction.
Deﬁnition 7.49. If (7.52) holds for some C and some EV copula C0, we say that
C is in the copula domain of attraction of C0, written C ∈CDA(C0).
There are a number of equivalent ways of writing (7.52). First, by taking logarithms and using the asymptotic identity ln(x) ∼x −1 as x →1, we get, for
u ∈(0, 1]d,
lim
t→∞t(1 −C(u1/t
1 , . . . , u1/t
d )) = −ln C0(u1, . . . , ud),
lim
s→0+
1 −C(us
1, . . . , us
d)
s
= −ln C0(u1, . . . , ud).
⎫
⎪⎬
⎪⎭
(7.53)
By inserting ui = exp(−xi) in the latter identity and using exp(−sx) ∼1 −sx as
s →0, we get, for x ∈[0, ∞)d,
lim
s→0+
1 −C(1 −sx1, . . . , 1 −sxd)
s
= −ln C0(e−x1, . . . , e−xd).
(7.54)
Example 7.50 (limiting copula for bivariate Pareto distribution). In Example 5.12 we saw that the bivariate Pareto distribution has univariate Pareto margins
Fi(x) = 1 −(κi/(κi + x))α and Clayton survival copula. It follows from Example 7.6 that Fi ∈MDA(H1/α), i = 1, 2. Using (5.14) the Clayton survival copula is
calculated to be C(u1, u2) = u1 + u2 −1 + ((1 −u1)−1/α + (1 −u2)−1/α −1)−α.
Using (7.54) it is easily calculated that C0(u1, u2) = u1u2 exp(((−ln u1)−1/α +
(−ln u2)−1/α)−α), which is the standard exchangeable Galambos copula of Example 7.47. Thus the limiting distribution of maxima consists of two Fr´echet dfs connected by the Galambos copula.
The coefﬁcients of upper tail dependence play an interesting role in the copula
domain of attraction theory. In particular, they can help us to recognize copulas that
lie in the copula domain of attraction of the independence copula.
Proposition 7.51. LetC beabivariatecopulawithuppertail-dependencecoefﬁcient
λu and assume that C satisﬁes C ∈MDA(C0) for some EV copula C0. Then λu
is also the upper tail-dependence coefﬁcient of C0 and is related to its dependence
function by λu = 2(1 −A( 1
2)).
--- page 332 ---

316
7. Extreme Value Theory
Proof. We use (5.28) and (5.14) to see that
λu = lim
q→1−
ˆC(1 −q, 1 −q)
1 −q
= 2 −lim
q→1−
1 −C(q, q)
1 −q
.
Byusingtheasymptoticidentityln x ∼x−1asx →1andtheCDAcondition(7.53)
we can calculate
lim
q→1−
1 −C0(q, q)
1 −q
= lim
q→1−
ln C0(q, q)
ln q
= lim
q→1−lim
s→0+
1 −C(qs, qs)
−s ln q
= lim
q→1−lim
s→0+
1 −C(qs, qs)
−ln(qs)
= lim
v→1−
1 −C(v, v)
1 −v
,
which shows that C and C0 share the same coefﬁcient of upper tail dependence.
Using the formula λu = 2−limq→1−ln C0(q, q)/ ln q and the representation (7.47)
we easily obtain that λu = 2(1 −A( 1
2)).
In the case when λu = 0 we must have A( 1
2) = 1, and the convexity of dependence
functions dictates that A(w) is identically one, so C0 must be the independence
copula. In the higher-dimensional case this is also true: if C is a d-dimensional
copula with all upper tail-dependence coefﬁcients equal to zero, then the bivariate
margins of the limiting copula C0 must all be independence copulas, and, in fact,
it can be shown that C0 must therefore be the d-dimensional independence copula
(see Notes and Comments).
As an example consider the limiting distribution of multivariate maxima of Gaussian random vectors. Since the pairwise coefﬁcients of tail dependence of Gaussian
vectors are zero (see Example 5.32), the limiting distribution is a product of marginal
Gumbel distributions. The convergence is extremely slow, but ultimately normalized
componentwise maxima are independent in the limit.
Now consider the multivariate t distribution, which has been an important model
throughout this book. If X1, . . . , Xn are iid random vectors with a td(ν, µ, Σ)
distribution, we know from Example 7.29 that univariate maxima of the individual
components are attracted to univariate Fr´echet distributions with parameter 1/ν.
Moreover, we know from Example 5.33 that tail dependence coefﬁcients for the
t copula are strictly positive; the limiting EV copula cannot be the independence
copula.
In fact, the limiting EV copula for t-distributed random vectors can be calculated
using (7.54), although the calculations are tedious. In the bivariate case it is found
that the limiting copula, which we call the t-EV copula, has dependence function
A(w) = wtν+1
(w/(1 −w))1/ν −ρ

(1 −ρ2)/(ν + 1)

+ (1 −w)tν+1
((1 −w)/w)1/ν −ρ

(1 −ρ2)/(ν + 1)

,
(7.55)
where ρ is the off-diagonal component of P = ℘(Σ). This dependence function
is shown in Figure 7.16 for four different values of ν and ρ values ranging from
--- page 333 ---

7.5. Multivariate Maxima
317
0.2
0.4
0.6
0.6
0.5
0.7
0.8
0.9
1.0
0.6
0.5
0.7
0.8
0.9
1.0
0.8
1.0
0
0.2
0.4
0.6
0.8
1.0
0
w
w
A(w)
A(w)
(a)
(c)
(d)
(b)
Figure 7.16.
Plots of dependence function for the t-EV copula for (a) ν = 2,
(b) ν = 4, (c) ν = 10 and (d) ν = 20, and with various values of ρ.
−0.5 to 0.9 with increments of 0.1. As ρ →1 the t-EV copula converges to the
comonotonicity copula; as ρ →−1 or as ν →∞it converges to the independence
copula.
7.5.4
Modelling Multivariate Block Maxima
A multivariate block maxima method analogous to the univariate method of Section 7.1.4 could be developed, although similar criticisms apply, namely that the
block maxima method is not the most efﬁcient way of making use of extreme data.
Also, the kind of inference that this method allows may not be exactly what is desired
in the multivariate case, as will be seen.
Suppose we divide our underlying data into blocks as before and we denote
the realizations of the block maxima vectors by Mn,1, . . . , Mn,m, where m is the
total number of blocks. The distributional model suggested by the univariate and
multivariate maxima theory consists of GEV margins connected by an extreme value
copula.
In the multivariate theory there is, in a sense, a “correct” EV copula to use, which
is the copula C0 to which the copula C of the underlying distribution of the raw data
is attracted. However, the underlying copula C is unknown and so the approach is
generally to work with any tractable EV copula that appears appropriate for the task
in hand. In a bivariate application, if we restrict to exchangeable copulas, then we
have at our disposal the Gumbel, Galambos and t-EV copulas, and a number of other
possibilities for which references in Notes and Comments should be consulted. As
will be apparent from Figures 7.15 and 7.16, the essential functional form of all
these families is really very similar; it makes sense to work with either Gumbel
or Galambos as these have simple forms that permit a relatively easy calculation
--- page 334 ---

318
7. Extreme Value Theory
of the copula density (which is needed for likelihood inference). Even if the “true”
underlying copula were t, it would not really make sense to use the more complicated
t-EV copula, since the dependence function in (7.55) for any ν and ρ can be very
accurately approximated by the dependence function of a Gumbel copula.
TheGumbelcopulaalsoallowsustoexplorethepossibilityofasymmetrybyusing
the general non-exchangeable family described in Example 7.46. For applications in
dimensions higher than two, the higher-dimensional extensions of Gumbel discussed
in Sections 5.4.2 and 5.4.3 may be useful, although we should stress again that
multivariate extreme value models are best suited to low-dimensional applications.
Putting these considerations together, data on multivariate maxima could be modelled using the df Hξ,µ,σ,θ(x) = Cθ(Hξ1,µ1,σ1(x1), . . . , Hξd,µd,σd(xd)) for some
tractable parametric EV copula Cθ. The usual method involves maximum likelihood inference and the maximization can either be performed in one step for all
parameters of the margins and copula or broken into two steps, whereby marginal
models are estimated ﬁrst and then a parametric copula is ﬁtted using the ideas in
Sections 5.5.2 and 5.5.3. The following bivariate example gives an idea of the kind
of inference that can be made with such a model.
Example 7.52. Let M65,1 represent the quarterly maximum of daily percentage falls
of the US dollar against the euro and let M65,2 represent the quarterly maximum of
daily percentage falls of the US dollar against the yen. We deﬁne a stress event for
eachofthesedailyreturnseries:forthedollaragainsttheeurowemightbeconcerned
about a 4% fall in any one day; for the dollar against the yen we might be concerned
about a 5% fall in any one day. We want to estimate the unconditional probability
that one or both of these stress events occurs over any quarter. The probability p of
interest is given by p = 1 −P(M65,1 ⩽4%, M65,2 ⩽5%) and approximated by
1−Hξ,µ,σ,θ(0.04, 0.05), where the parameters are estimated from the block maxima
data. Of course, a more worrying scenario might be that both of these stress events
should occur on the same day. To calculate the probability of simultaneous extreme
events we require a different methodology, which is developed in Section 7.6.
Notes and Comments
Early works on distributions for bivariate extremes include Geffroy (1958),
Tiago de Oliveira (1958) and Sibuya (1960). A selection of further important papers
in the development of the subject include Galambos (1975), de Haan and Resnick
(1977), Balkema and Resnick (1977), Deheuvels (1980) and Pickands (1981). The
texts by Galambos (1987) and Resnick (1987) have both been inﬂuential; our presentation more closely resembles the former.
Theorem 7.44 is proved in Galambos (1987) (see Theorem 5.2.1 and Lemma 5.4.1
therein (see also Joe 1997, p. 173)). Theorem 7.45 is essentially a result of Pickands
(1981). A complete version of the proof is given in Theorem 5.4.5 of Galambos
(1987), although it is given in the form of a characterization of MEV distributions
with Gumbel margins. This is easily reformulated as a characterization of the EV
copulas. In the bivariate case necessary and sufﬁcient conditions for A(w) in (7.47)
to deﬁne a bivariate EV copula are given in Joe (1997, Theorem 6.4).
--- page 335 ---

7.6. Multivariate Threshold Exceedances
319
The copula of Example 7.47 appears in Galambos (1975). A good summary
of other bivariate and multivariate extreme value copulas is found in Kotz and
Nadarajah(2000);theyarepresentedasMEVdistributionswithunitFr´echetmargins
but the EV copulas are easily inferred from this presentation. See also Joe (1997,
Chapters 5 and 6), in which EV copulas and their higher-dimensional extensions
are discussed. Many parametric models for extremes have been suggested by Tawn
(1988, 1990).
Theorem 7.48 is found in Galambos (1987), where the necessary and sufﬁcient
copula convergence criterion is given as limn→∞Cn(u1/n) = C0(u) for positive
integers n; by noting that for any t > 0 we have the inequalities
C[t]+1(u1/[t]) ⩽Ct(u1/t) ⩽C[t](u1/([t]+1)),
it can be inferred that this is equivalent to limt→∞Ct(u1/t) = C0(u). Further
equivalent CDA conditions are found in Takahashi (1994). The idea of a domain of
attraction of an EV copula also appears in Abdous, Ghoudi and Khoudraji (1999).
Not every copula is in a copula domain of attraction; a counterexample may be
found in Schlather and Tawn (2002).
We have shown that pairwise asymptotic independence for the components of
random vectors implies pairwise independence of the corresponding components
in the limiting MEV distribution of the maxima. Pairwise independence for an
MEV distribution in fact implies mutual independence, as recognized and described
by a number of authors: see Galambos (1987, Corollary 5.3.1), Resnick (1987,
Theorem 5.27), and the earlier work of Geffroy (1958) and Sibuya (1960).
7.6
Multivariate Threshold Exceedances
In this section we describe practically useful models for multivariate extremes
(again in low-dimensional applications) that build on the basic idea of modelling
excesses over high thresholds with the generalized Pareto distribution (GPD) as
in Section 7.2. The idea is to use GPD-based tail models of the kind discussed in
Section 7.2.3 together with appropriate copulas to obtain models for multivariate
threshold exceedances.
7.6.1
Threshold Models Using EV Copulas
Assume that the vectors X1, . . . , Xn have unknown joint distribution F(x) =
C(F1(x1), . . . , Fd(xd)) for some unknown copula C and margins F1, . . . , Fd, and
that F is in the domain of attraction of an MEV distribution. Much as in the univariate case we would like to approximate the upper tail of F(x) above some vector of
high thresholds u = (u1, . . . , ud)′. The univariate theory of Sections 7.2.2 and 7.2.3
tells us that, for xj ⩾uj and uj high enough, the tail of the marginal distribution
Fj may be approximated by a GPD-based functional form
˜Fj(xj) = 1 −λj

1 + ξj
xj −uj
βj
−1/ξj
,
(7.56)
--- page 336 ---

320
7. Extreme Value Theory
where λj = ¯Fj(uj). This suggests that for x ⩾u we use the approximation
F(x) ≈C( ˜F1(x1), . . . , ˜Fd(xd)). But C is also unknown and must itself be approximated in the tail. The following heuristic argument suggests that we should be able
to replace C by its limiting copula C0.
The CDA condition (7.52) suggests that for any value v ∈(0, 1)d and t sufﬁciently
large we may make the approximation C(v1/t) ≈C1/t
0 (v). If we now write w =
v1/t, we have
C(w) ≈C1/t
0 (wt) = C0(w),
(7.57)
by the scaling property of EV copulas. The approximation (7.57) will be best for
large values of w, since v1/t →1 as t →∞.
We assume then that we can substitute the copula C with its EV limit C0 in the
tail, and this gives us the overall model
˜F(x) = C0( ˜F1(x1), . . . , ˜Fd(xd)),
x ⩾u.
(7.58)
We complete the model speciﬁcation by choosing a ﬂexible and tractable parametric
EV copula for C0. As before, the Gumbel copula family is particularly convenient.
7.6.2
Fitting a Multivariate Tail Model
Assume we have observations X1, . . . , Xn from a df F with a tail that permits the
approximation (7.58). Of these observations, only a minority are likely to be in the
joint tail (x ⩾u); other observations may exceed some of the individual thresholds
but lie below others. The usual way of making inferences about all the parameters of
such a model (the marginal parameters ξj, βj, λj, for j = 1, . . . , d, and the copula
parameter (or parameter vector) θ) is to maximize a likelihood for censored data.
Let us suppose that mi components of the data vector Xi exceed their respective
thresholds in the vector u. The only relevant information that the remaining components convey is that they lie below their thresholds; such a component Xi,j is said
to be censored at the value uj. The contribution to the likelihood of Xi is given by
Li = Li(ξ, β, λ, θ; Xi) = ∂mi ˜F(x1, . . . , xd)
∂xj1 · · · ∂xjmi

max(Xi,u)
,
where the indices j1, . . . , jmi are those of the components of Xi exceeding their
thresholds.
For example, in a bivariate model with Gumbel copula (5.11) the likelihood
contribution would be
Li =
⎧
⎪⎪⎪⎪⎨
⎪⎪⎪⎪⎩
CGu
θ (1 −λ1, 1 −λ2),
Xi,1 ⩽u1, Xi,2 ⩽u2,
CGu
θ,1( ˜F1(Xi,1), 1 −λ2) ˜f1(Xi,1),
Xi,1 > u1, Xi,2 ⩽u2,
CGu
θ,2(1 −λ1, ˜F2(Xi,2)) ˜f2(Xi,2),
Xi,1 ⩽u1, Xi,2 > u2,
cGu
θ ( ˜F1(Xi,1), ˜F2(Xi,2)) ˜f1(Xi,1) ˜f2(Xi,2),
Xi,1 > u1, Xi,2 > u2,
(7.59)
where ˜fj denotes the density of the univariate tail model ˜Fj in (7.56), cGu
θ (u1, u2)
denotes the Gumbel copula density and CGu
θ,j(u1, u2) := (∂/∂uj)CGu
θ (u1, u2)
--- page 337 ---

7.6. Multivariate Threshold Exceedances
321
Table 7.3.
Parameter estimates and standard errors (in brackets) for a bivariate
tail model ﬁtted to exchange-rate return data; see Example 7.53 for details.
$/€
$/¥
u
0.75
1.00
Nu
189
126
λ
0.094 (0.0065)
0.063 (0.0054)
ξ
−0.049 (0.066)
0.095 (0.11)
β
0.33 (0.032)
0.38 (0.053)
θ
1.10 (0.030)
denotes a conditional distribution of the copula, as in (5.15). The overall likelihood
is a product of such contributions and is maximized with respect to all parameters
of the marginal models and copula.
In a simpler approach, parameters of the marginal GPD models could be estimated
as in Section 7.2.3 and only the parameters of the copula obtained from the above
likelihood. In fact this is also a sensible way of getting starting values before going
on to the global maximization over all parameters.
The model described by the likelihood (7.59) has been studied in some detail
by Ledford and Tawn (1996) and a number of related models have been studied in
the statistical literature on multivariate EVT (see Notes and Comments for more
details).
Example 7.53 (bivariate tail model for exchange-rate return data). We analyse
daily percentage falls in the value of the US dollar against the euro and the Japanese
yen, taking data for the eight-year period 1996–2003. We have 2008 daily returns
and choose to set thresholds at 0.75% and 1.00%, giving 189 and 126 exceedances,
respectively.Inafullmaximizationofthelikelihoodoverallparameters,weobtained
the estimates and standard errors shown in Table 7.3. The value of the maximized
log-likelihood is −1064.7, compared with −1076.4 in a model where independence
in the tail is assumed (i.e. a Gumbel copula with θ = 1), showing strong evidence
against an independence assumption.
We can now use the ﬁtted model (7.58) to make various calculations about stress
events. For example, an estimate of the probability that on any given day the dollar
falls by more than 2% against both currencies is given by
p12 := 1 −˜F1(2.00) −˜F2(2.00) + CGu
θ ( ˜F1(2.00), ˜F2(2.00)) = 0.000 315,
with ˜Fj as in (7.56), making this approximately a 13-year event (assuming 250 trading days per year). The marginal probabilities of falls in value of this magnitude are
p1 := 1 −˜F1(2.00) = 0.0014 and p2 := 1 −˜F2(2.00) = 0.0061. We can use this
information to calculate so-called spillover probabilities for the conditional occurrence of stress events; for example, the probability that the dollar falls 2% against
the yen given that it falls 2% against the euro is estimated to be p12/p1 = 0.23.
--- page 338 ---

322
7. Extreme Value Theory
7.6.3
Threshold Copulas and Their Limits
Another, more recent, approach to multivariate extremes looks explicitly at the kind
of copulas we get when we condition observations to lie above or below extreme
thresholds. Just as the GPD is a natural limiting model for univariate threshold
exceedances, so we can ﬁnd classes of copula that are natural limiting models for
the dependence structure of multivariate exceedances.
The theory has been studied in most detail in the case of exchangeable bivariate
copulas, and we concentrate on this case. Moreover, it proves slightly easier to
switch our focus at this stage and ﬁrst consider the lower-left tail of a probability
distribution, before showing how the theory is adapted to the upper-right tail.
Lower threshold copulas and their limits.
Consider a random vector (X1, X2)
with continuous margins F1 and F2 and an exchangeable copula C. We consider
the distribution of (X1, X2) conditional on both being below their v-quantiles, an
event we denote by Av = {X1 ⩽F ←
1 (v), X2 ⩽F ←
2 (v)}, 0 < v ⩽1. Assuming
C(v, v)̸ = 0, the probability that X1 lies below its x1-quantile and X2 lies below its
x2-quantile conditional on this event is
P(X1 ⩽F ←
1 (x1), X2 ⩽F ←
2 (x2) | Av) = C(x1, x2)
C(v, v) ,
x1, x2 ∈[0, v].
Considered as a function of x1 and x2 this deﬁnes a bivariate df on [0, v]2, and by
Sklar’s Theorem we can write
C(x1, x2)
C(v, v)
= C0
v(F(v)(x1), F(v)(x2)),
x1, x2 ∈[0, v],
(7.60)
for a unique copula C0
v and continuous marginal distribution functions
F(v)(x) = P(X1 ⩽F ←
1 (x) | Av) = C(x, v)
C(v, v),
0 ⩽x ⩽v.
(7.61)
This unique copula may be written as
C0
v(u1, u2) =
C(F ←
(v)(u1), F ←
(v)(u2))
C(v, v)
,
(7.62)
and will be referred to as the lower threshold copula of C at level v. Juri andW¨uthrich
(2002), who developed the approach we describe in this section, refer to it as a lower
tail dependence copula (LTDC). It is of interest to attempt to evaluate limits for this
copula as v →0; such a limit will be known as a limiting lower threshold copula.
Much like the GPD in Example 7.19, limiting lower threshold copulas must possess a stability property under the operation of calculating lower threshold copulas
in (7.62). A copula C is a limiting lower threshold copula if, for any threshold
0 < v ⩽1, it satisﬁes
C0
v(u1, u2) = C(u1, u2).
(7.63)
Example 7.54 (Clayton copula as limiting lower threshold copula). For the
standard bivariate Clayton copula in (5.12) we can easily calculate that F(v) in (7.61)
is
F(v)(x) = (x−θ + v−θ −1)−1/θ
(2v−θ −1)−1/θ
,
0 ⩽x ⩽v,
--- page 339 ---

7.6. Multivariate Threshold Exceedances
323
and its inverse is
F ←
(v)(u) = u(2v−θ −1 + uθ(1 −v−θ))−1/θ,
0 ⩽u ⩽1.
Thus the lower threshold copula for the Clayton copula can be calculated from (7.62)
anditmaybeveriﬁedthatthisisagaintheClaytoncopula.Inotherwords,theClayton
copula is a limiting lower threshold copula because (7.63) holds.
Upper threshold copulas.
To deﬁne upper threshold copulas we consider again a
random vector (X1, X2) with copula C and margins F1 and F2.We now condition on
the event ¯Av = {X1 > F ←
1 (v), X2 > F ←
2 (v)} for 0 ⩽v < 1. We have the identity
P(X1 > F ←
1 (x1), X2 > F ←
2 (x2) | ¯Av) =
¯C(x1, x2)
¯C(v, v) ,
x1, x2 ∈[v, 1].
Since ¯C(x1, x2)/ ¯C(v, v) deﬁnes a bivariate survival function on [v, 1]2, by (5.13)
we can write
¯C(x1, x2)
¯C(v, v)
= ˆC1
v( ¯G(v)(x1), ¯G(v)(x2)),
x1, x2 ∈[v, 1],
(7.64)
for some survival copula ˆC1
v of a copula C1
v and marginal survival functions
¯G(v)(x) = P(X1 > F ←
1 (x) | ¯Av) =
¯C(x, v)
¯C(v, v),
v ⩽x ⩽1.
(7.65)
The copula C1
v is known as the upper threshold copula at level v and it is now
of interest to ﬁnd limits as v →1, which are known as limiting upper threshold
copulas. In fact, as the following lemma shows, it sufﬁces to study either lower or
upper threshold copulas because results for one follow easily from results for the
other.
Lemma 7.55. The survival copula of the upper threshold copula of C at level v is
the lower threshold copula of ˆC at level 1 −v.
Proof. We use the identity ¯C(u1, u2) = ˆC(1 −u1, 1 −u2) and (7.65) to rewrite
(7.64) as
ˆC(1 −x1, 1 −x2)
ˆC(1 −v, 1 −v)
= ˆC1
v
 ˆC(1 −x1, 1 −v)
ˆC(1 −v, 1 −v)
,
ˆC(1 −v, 1 −x2)
ˆC(1 −v, 1 −v)

.
Writing y1 = 1 −x1, y2 = 1 −x2 and w = 1 −v we have
ˆC(y1, y2)
ˆC(w, w)
= ˆC1
1−w
 ˆC(y1, w)
ˆC(w, w)
,
ˆC(w, y2)
ˆC(w, w)

,
y1, y2 ∈[0, w],
and comparison with (7.60) and (7.61) shows that ˆC1
1−w must be the lower threshold
copula of ˆC at the level w = 1 −v.
It follows that the survival copulas of limiting lower threshold copulas are limiting
upper threshold copulas. The Clayton survival copula is a limiting upper threshold
copula.
--- page 340 ---

324
7. Extreme Value Theory
Relationship between limiting threshold copulas and EV copulas.
We give one
result which shows how limiting upper threshold copulas may be calculated for
underlyingexchangeablecopulasC thatareinthedomainofattractionofEVcopulas
with tail dependence, thus linking the study of threshold copulas to the theory of
Section 7.5.3.
Theorem 7.56. If C is an exchangeable copula with upper tail-dependence coefﬁ-
cient λu > 0 satisfying C ∈CDA(C0), then C has a limiting upper threshold copula
which is the survival copula of the df
G(x1, x2) = (x1 + x2)(1 −A(x1/(x1 + x2)))
λu
,
(7.66)
where A is the dependence function of C0. Also, ˆC has a limiting lower threshold
copula which is the copula of G.
Example 7.57 (upper threshold copula of Galambos copula). We use this result
to calculate the limiting upper threshold copula for the Galambos copula. We recall
that this is an EV copula with dependence function given in (7.50) and consider the
standard exchangeable case with α = β = 1. Using the methods of Section 5.2.3 it
may easily be calculated that the coefﬁcient of upper tail dependence of this copula
is λu = 2−1/θ. Thus the bivariate distribution G(x1, x2) in (7.66) is
G(x1, x2) = ( 1
2(x−θ
1
+ x−θ
2 ))−1/θ,
(x1, x2) ∈(0, 1]2,
the copula of which is the Clayton copula. Thus the limiting upper threshold copula
in this case is the Clayton survival copula. Moreover, the limiting lower threshold
copula of the Galambos survival copula is the Clayton copula.
The Clayton copula turns out to be an important attractor for a large class of
underlying exchangeable copulas. Juri and W¨uthrich (2003) have shown that all
Archimedean copulas whose generators are regularly varying at 0 with negative
parameter (meaning that φ(t) satisﬁes limt→0 φ(xt)/φ(t) = x−α for all x and some
α > 0) share the Clayton copula CCl
α as their limiting lower threshold copula.
It is of interest to calculate limiting lower and upper threshold copulas for the
t copula, and this can be done using Theorem 7.56 and the expression for the
dependence function in (7.55). However, the resulting limit is not convenient for
practical purposes because of the complexity of this dependence function. We have
already remarked in Section 7.5.4 that the dependence function of the t-EV copula is
indistinguishable for all practical purposes from the dependence functions of other
exchangeable EV copulas, such as Gumbel and Galambos. Thus Theorem 7.56
suggests that instead of working with the true limiting upper threshold copula of the
t copula we could instead work with the limiting upper threshold copula of, say, the
Galambos copula, i.e. the Clayton survival copula. Similarly, we could work with
the Clayton copula as an approximation for the true limiting lower threshold copula
of the t copula.
--- page 341 ---

7.6. Multivariate Threshold Exceedances
325
Limiting threshold copulas in practice
Limiting threshold copulas in dimensions
higher than two have not yet been extensively studied, nor have limits for nonexchangeable bivariate copulas or limits when we deﬁne two thresholds v1 and v2
and let these tend to zero (or one) at different rates. Thus the practical use of these
ideas is largely in bivariate applications when thresholds are set at approximately
similar quantiles and a symmetric dependence structure is assumed.
Let us consider a situation where we have a bivariate distribution that appears to
exhibit tail dependence in both the upper-right and lower-left corners. While true
lower and upper limiting threshold copulas may exist for this unknown distribution,
we could in practice simply adopt a tractable and ﬂexible parametric limiting threshold copula family. It is particularly easy to use the Clayton copula and its survival
copula as lower and upper limits, respectively.
Suppose,forexample,thatwesethighthresholdsatu = (u1, u2)′,sothatP(X1 >
u1) ≈P(X2 > u2) and both probabilities are small. For the conditional distribution
of (X1, X2) over the threshold u we could assume a model of the form
P(X ⩽x | X > u) ≈ˆCCl
θ (Gξ1,β1(x1 −u1), Gξ2,β2(x2 −u2)),
x > u,
where ˆCCl
θ
is the Clayton survival copula and Gξj ,βj denotes a GPD, as deﬁned
in 7.16. Inference about the model parameters (θ, ξ1, β1, ξ2, β2) would be based on
the exceedance data above the thresholds and would use the methods discussed in
Section 5.5.
Similarly, for a vector of low thresholds u satisfying P(X1 ⩽u1) ≈P(X2 ⩽u2)
with both these probabilities small, we could approximate the conditional distribution of (X1, X2) below the threshold u by a model of the form
P(X ⩽x | X < u) ≈CCl
θ ( ¯Gξ1,β1(u1 −x1), ¯Gξ2,β2(u2 −x2)),
x < u,
where CCl
θ is the Clayton copula and ¯Gξj ,βj denotes a GPD survival function. Inference about the model parameters would be based on the data below the thresholds
and would use the methods of Section 5.5.
Note and Comments
The GPD-based tail model (7.58) and inference for censored data using a likelihood of the form (7.59) have been studied by Ledford and Tawn (1996), although
the derivation of the model uses somewhat different asymptotic reasoning based on
a characterization of multivariate domains of attraction of MEV distributions with
unit Fr´echet margins found in Resnick (1987). The authors concentrate on the model
with Gumbel (logistic) dependence structure and discuss, in particular, testing for
asymptotic independence of extremes. Likelihood inference is non-problematic (the
problem being essentially regular) when θ > 0 and ξj > −1
2, but testing for independence of extremes θ = 1 is not quite so straightforward since this is a boundary
point of the parameter space. This case is possibly more interesting in environmental
applications than in ﬁnancial ones, where we tend to expect dependence of extreme
values.
--- page 342 ---

326
7. Extreme Value Theory
A related bivariate GPD model is presented in Smith, Tawn and Coles (1997). In
our notation they essentially consider a model of the form
¯F(x1, . . . , xd) = 1 + ln C0(exp( ˜F(x1) −1), . . . , exp( ˜F(xd) −1)),
x ⩾k,
where C0 is an extreme value copula. This model is also discussed in Smith (1994)
and Ledford and Tawn (1996); it is pointed out that ¯F does not reduce to a product
of marginal distributions in the case when C0 is the independence copula, unlike the
model in (7.58).
Another style of statistical model for multivariate extremes is based on the point
process theory of multivariate extremes developed in de Haan (1985), de Haan and
Resnick (1977) and Resnick (1987). Statistical models using this theory are found
in Coles and Tawn (1991) and Joe, Smith and Weissman (1992); see also the texts of
Joe (1997) and Coles (2001). New approaches to modelling multivariate extremes
can be found in Heffernan and Tawn (2004) and Balkema and Embrechts (2004);
the latter paper considers applications to stress testing high-dimensional portfolios
in ﬁnance.
Limiting threshold copulas are studied in Juri and W¨uthrich (2002, 2003). In
the latter paper it is demonstrated that the Clayton copula is an attractor for the
threshold copulas of a wide class of Archimedean copulas; moreover a version
of our Theorem 7.57 is proved. Limiting threshold copulas for the t copula are
investigated in Demarta and McNeil (2005). The usefulness of Clayton’s copula and
survival copula for describing the dependence in the tails of bivariate ﬁnancial return
data was conﬁrmed in a large-scale empirical study of high-frequency exchange-rate
returns by Breymann, Dias and Embrechts (2003).
--- page 343 ---

8
Credit Risk Management
Credit risk is the risk that the value of a portfolio changes due to unexpected changes
in the credit quality of issuers or trading partners. This subsumes both losses due to
defaults and losses caused by changes in credit quality, such as the downgrading of
a counterparty in an internal or external rating system. Credit risk is omnipresent
in the portfolio of a typical ﬁnancial institution. To begin with, the lending and corporate bond portfolios are obviously affected by credit risk. Perhaps less obviously,
credit risk accompanies any OTC (over-the-counter, i.e. non-exchange-guaranteed)
derivative transaction such as a swap, because the default of one of the parties
involved may substantially affect the actual pay-off of the transaction. Moreover,
in recent years a specialized market for credit derivatives has emerged in which
ﬁnancial institutions are active players (see Section 9.1 for details).
This brief list should convince the reader that credit risk is a highly relevant risk
category indeed, as it relates to the core activities of most banks. Credit risk is also
at the heart of many recent developments on the regulatory side, such as the new
Basel II Capital Accord discussed in Chapter 1. We devote two chapters to this
important risk category. In the present chapter we focus on static models and credit
risk management; dynamic models and credit derivatives are discussed in Chapter 9.
8.1
Introduction to Credit Risk Modelling
In this section we provide a brief overview of the various model types that are used
in credit risk before discussing some of the main challenges that are encountered in
credit risk management.
8.1.1
Credit Risk Models
The development of the market for credit derivatives and the Basel II process has
generated a lot of interest in quantitative credit risk models in industry, academia and
among regulators, so that credit risk modelling is at present a very active subﬁeld of
quantitative ﬁnance and risk management. In this context it is interesting that parts
of the new minimum capital requirements for credit risk are closely linked to the
structure of existing credit portfolio models, as will be explained in more detail in
Section 8.4.5.
There are two main areas of application for quantitative credit risk models: credit
risk management and the analysis of credit-risky securities. Credit risk management
models are used to determine the loss distribution of a loan or bond portfolio over
