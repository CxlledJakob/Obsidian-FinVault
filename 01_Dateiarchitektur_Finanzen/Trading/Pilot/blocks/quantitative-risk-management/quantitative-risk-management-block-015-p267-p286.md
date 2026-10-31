# Quantitative Risk Management_ Concepts, Techniques, and -- Alexander J_ McNeil, Rüdiger Frey, Paul Embrechts -- Princeton series in finance, -- isbn13 9780691122557 -- 478a0059673fecd0c76229cd3d8884e7 -- Anna’s Arc.pdf — pages 267–286

--- page 267 ---

6.2. Bounds for Aggregate Risks
251
A third correlation fallacy.
Based on the above result we can highlight a third
important fallacy concerning correlation to add to the two in Section 5.2.1.
Fallacy 3. VaR for the sum of two risks is at its worst when these two risks have
maximal correlation, i.e. are comonotonic.
Any superadditive VaR example yields a correction to this statement; one such
case was shown in Example 6.7 and a further one is given below in Example 6.22. In
a superadditive VaR situation we have VaRα(L1 + L2) > VaRα(L1) + VaRα(L2)
for two risks L1 and L2 and some conﬁdence level α. By Proposition 6.15 and
Remark 6.16 the right-hand side VaRα(L1) + VaRα(L2) corresponds to the VaR of
L1 + L2 when L1 and L2 are comonotonic. Moreover, Theorem 5.25 and Example 6.14 imply that the correlation of L1 and L2 is maximal in the comonotonic case.
Hence the superadditive portfolio case must correspond to a smaller correlation. The
remainder of Section 6.2 is devoted to the issue of ﬁnding the worst case.
Remark 6.17. For expected shortfall the expression ϱ(L1 + L2) is maximized for
comonotonic losses. To see this, note that Proposition 6.15 together with (2.23)
imply that expected shortfall also has the comonotonic additivity property. Since
expected shortfall is coherent, we have ϱ(L1 + L2) ⩽ϱ(L1) + ϱ(L2), so that
comonotonicity is in fact the worst possible case. There exists a whole class of
coherent risk measures, known as spectral risk measures, which share this property
(see Notes and Comments). Note, also, that if we work with VaR but restrict our
attention to elliptical distributions for the vector L, then VaR is a coherent risk
measure (Theorem 6.8). Fallacy 3 is taken out of play and comonotonicity does
correspond to the worst case.
Restrictions on dependence using copulas.
Before discussing bounds on VaR we
need to formalize the restrictions we make on the dependence structure of the df
F of L. Recall that in the case of continuous marginal dfs Fi, there is a unique
copula C such that F = C(F1, . . . , Fd), and one possibility is to impose dependence
restrictions on L1, . . . , Ld through conditions on C. Recall from Theorem 5.7 that
W ⩽C ⩽M, where W and M denote the Fr´echet lower and upper bounds,
respectively.
We introduce dependence restrictions of the following type.
(A2) C ⩾C0 for a copula C0.
When d = 2 the case of unconstrained optimization can be treated as a special case of
restriction (A2) by setting C0 = W, since W is a proper copula in this case; however,
for d > 2 unconstrained optimization is not a special case of restriction (A2).
The case where C0 = Π, the independence copula in (5.6), corresponds to socalled positive lower orthant dependence (PLOD) (see M¨uller and Stoyan 2002,
Deﬁnition 3.10.1). In Theorem 3.10.4 of M¨uller and Stoyan (2002), it is shown that,
if cov(f (L), g(L)) ⩾0 for all increasing functions f, g : Rd →R, then L is
PLOD.
Note that the relation “⩾” in (A2) is not a complete ordering on the space of all
copulas, meaning that for any two copulas C1 and C2 it is not necessarily true that
--- page 268 ---

252
6. Aggregate Risk
either C1 ⩾C2 or C2 ⩾C1. As a consequence, a constraint of the type (A2) may
only give a restrictive view on dependence alternatives.
Notationfortheoptimizationproblem.
Inordertoformulatesomeofthekeyresults
for the optimization problem (6.11), we need some extra notation. Given a vector
x = (x1, . . . , xd)′ ∈Rd, we write x−i = (x1, . . . , xi−1, xi+1, . . . , xd)′. Also, for
x−d ∈Rd−1 ﬁxed, we deﬁne Ψ ∧
x−d(s) := sup{xd ∈R : Ψ (x−d, xd) < s} for s ∈R.
In our set-up, it is convenient to identify the df F of L given ﬁxed margins with the
copula C that combines the margins to give the df C(F1, . . . , Fd). Denote by µC
the corresponding probability measure on Rd and deﬁne, for s ∈R,
σC,Ψ (F1, . . . , Fd)(s) := µC(Ψ (L) < s),
τC,Ψ (F1, . . . , Fd)(s) :=
sup
x1,...,xd−1∈R
C(F1(x1), . . . , Fd−1(xd−1), F −
d (Ψ ∧
x−d(s))),
where F −
d (x) stands for the left limit of Fd in x. It follows that
mΨ (s) := inf{P(Ψ (L) < s) : Li ∼Fi, i = 1, . . . , d}
= inf{σC,Ψ (F1, . . . , Fd)(s) : C ∈Cd},
where Cd denotes the set of all d-dimensional copulas.
Remark 6.18. The strict inequality “<” in the deﬁnition of mΨ (s) is essential (see
Embrechts and Puccetti 2005, Remark 3.1(ii)).
Optimization subject to proper copula constraints.
It turns out that a proper lower
copula constraint as in (A2) allows for an easier analysis. Recall that the unconstrained case C ⩾W is a special case of (A2) only if d = 2.
Theorem 6.19 (lower bound with partial information). Let L be a random vector
in Rd (d ⩾2) having margins F1, . . . , Fd and copula C. Assume that there exists
a copula C0 such that C ⩾C0 (i.e. Assumption (A2) holds). If Ψ : Rd →R is
increasing, then, for s ∈R,
σC,Ψ (F1, . . . , Fd)(s) ⩾τC0,Ψ (F1, . . . , Fd)(s).
(6.13)
If, moreover, Ψ is right-continuous in its last argument, then the copula
Ct(u) :=

max(t, C0(u)),
u ∈[t, 1]d,
min{u1, . . . , ud},
otherwise,
where t = τC0,Ψ (F1, . . . , Fd)(s) attains the bound in (6.13).
Proof. See Theorems 3.1 and 3.2 in Embrechts and Puccetti (2005).
Translated into the language of VaR and using the notation VaRα,max
:=
τC0,Ψ (F1, . . . , Fd)←(α) for the inverse of the τ function in (6.13), Theorem 6.19
becomes
VaRα(Ψ (L)) ⩽VaRα,max,
(6.14)
--- page 269 ---

6.2. Bounds for Aggregate Risks
253
for 0 < α < 1, which gives an upper bound of the kind in (6.10). If Ψ is given by
the sum operator, abbreviated to Ψ = +, this bound is
VaRα,max =
inf
u∈[0,1]d,C0(u)=α(F ←
1 (u1) + · · · + F ←
d (ud)).
(6.15)
The unconstrained case.
The unconstrained case for d > 2 is more difﬁcult. First
of all, the standard bound (6.13) evaluated at C0 = W still holds but may fail to
be sharp. For Ψ = + and F1 = · · · = Fd = F with F a continuous df on R+, it
reduces to
τW,+(F, . . . , F)(s) = (dF(s/d) −d + 1)+
(6.16)
for large enough s (see Embrechts and Puccetti (2005) for details). The next result
yields a better bound.
Theorem 6.20 (a better bound in the unconstrained case). Let F be a continuous
df on R+ and let F1 = · · · = Fd = F. Then, for all s ⩾0 and ¯F = 1 −F,
m+(s) ⩾1 −d
inf
r∈[0,s/d]
 s−(d−1)r
r
¯F(x) dx
s −dr
.
(6.17)
Proof. See Theorem 4.2 in Embrechts and Puccetti (2005).
Remark 6.21. The value of m+(s) can be closely approximated by solving two
linear programmes (see Embrechts and Puccetti 2005; Embrechts, H¨oing and Juri
2003).
Examples.
In a ﬁrst example we consider the special, though important, case when
F1 = F2 = Φ, the standard normal df. The second example considers higherdimensional portfolios with Pareto margins.
Example 6.22 (worst VaR for a portfolio with normal margins). For i = 1, 2
let Fi = Φ. In Figure 6.1 we have plotted the worst VaRα(L1 + L2) calculated using (6.16) as a function of α together with the curve corresponding to
the comonotonic case calculated using Proposition 6.15. The fact that the former lies above the latter implies the existence of portfolios with normal margins for which VaR is not subadditive. For example, for α = 0.95, the upper
bound is 3.92, whereas VaRα(Li) = 1.645, so, for the worst VaR portfolio,
VaR0.95(L1 + L2) = 3.92 > 3.29 = VaR0.95(L1) + VaR0.95(L2). The worstcase copula is shown in Figure 6.2 (see Embrechts, H¨oing and Puccetti (2005) for
further details).
As explained in Theorem 6.20, the case d ⩾3 is more subtle, as the standard
bound (6.15) fails to be sharp. The strictly lower bound (6.17) in the case of identical
distributions can be computed easily. In Section 10.1.4 we will show that operational
risk losses can be modelled reasonably well by heavy-tailed Pareto distributions with
inﬁnite variance. In the case of operational risk one faces the calculation of VaRs
at the 99% (or even higher) level across numerous (up to 56) classes of risk. The
dependence between the loss rvs for these classes is mostly unknown, so we face
the above unconstrained optimization problem for VaRα(L1 + · · · + Ld). The next
example contains some calculations for Pareto portfolios.
--- page 270 ---

254
6. Aggregate Risk
0
1
2
3
4
5
6
7
VaR   (L1 + L2)
α
0.5
0.6
0.7
0.8
0.9
1.0
α
Figure 6.1.
The worst-case VaRα (solid line) plotted against α for two standard normal
risks; the case of comonotonic risks (dotted line) is shown as a comparison.
20
40
60
80
100
120
0
−2
−2
−1
−3
2
1
2
3
0
0
Figure 6.2.
Contour and perspective plots of the density function of the distribution of
(L1, L2) leading to the worst-case VaR for L1 + L2 at the α = 0.95 level when the Li are
standard normal.
Example 6.23 (VaR bounds for Pareto portfolios). Suppose that Li ∼Pa(1.5, 1)
for i = 1, . . . , d so that E(Li) = 2 and VaR(Li) = ∞. In the unconstrained case,
Table 6.1 contains the bounds obtained from Theorem 6.20 (which, for reasons we
will not discuss, are known as dual bounds). The portfolio sizes 8 and 56 have been
chosen with the operational risk problem in mind, as explained above, whereas 100
--- page 271 ---

6.2. Bounds for Aggregate Risks
255
Table 6.1.
Bounds for VaRα(d
i=1 Li) for portfolios of Pa(1.5, 1)-distributed risks are
given in columns marked “dual”; columns marked “com” give values in the comonotonic
case. Numbers are expressed in thousands.
VaRα(8
i=1 Li)
VaRα(56
i=1 Li)
VaRα(100
i=1 Li)
VaRα(1000
i=1 Li)












α
com
dual
com
dual
com
dual
com
dual
0.90
0.03
0.08
0.20
0.67
0.36
1.23
3.64
12.73
0.95
0.05
0.14
0.36
1.10
0.64
2.00
6.37
20.77
0.99
0.16
0.41
1.15
3.32
2.05
6.05
20.54
62.66
0.999
0.79
1.93
5.54
15.63
9.90
28.43
99.00
294.47
and 1000 could represent the sizes of typical credit portfolios. The assumption of a
single common Pareto distribution for all individual losses is of course a simpliﬁ-
cation for computational purposes.
Notes and Comments
There is a large literature on Fr´echet problems. Our discussion is mainly based
on Embrechts, H¨oing and Juri (2003), Embrechts, H¨oing and Puccetti (2005)
and Embrechts and Puccetti (2005). These papers also contain the most important
references to the existing literature. Historically, the question of bounding the df of
a sum of rvs with given marginals goes back to Kolmogorov and was answered by
Makarov (1981) for d = 2. Frank, Nelsen and Schweizer (1987) restated Makarov’s
result using the notion of a copula. Independently, R¨uschendorf (1982) gave a very
elegant proof of the same result using duality. Williamson and Downs (1990) introduced the use of dependence information.
Fallacy 3 originally appeared in Embrechts, McNeil and Straumann (2002); it
ceases to be a fallacy if we replace VaR by expected shortfall or a spectral risk
measure. For spectral risk measures see Kusuoka (2001), Acerbi (2002) and Tasche
(2002).A closely related class of risk measures mainly used in insurance applications
is referred to as distortion or Wang measures (see Wang 1996). A nice discussion is
to be found in Denuit and Charpentier (2004).
Embrechts, H¨oing and Juri (2003) gave the most general theorem for general d
and Ψ ; their main result on the sharpness of the bounds for d ⩾3 and no constraints,
however, contains an error: this was corrected in Embrechts and Puccetti (2005). For
the construction of the copula(s) leading to the worst VaR, see Embrechts, H¨oing
and Puccetti (2005). Numerous other authors (especially in analysis and actuarial
mathematics) have contributed to this area and we refer to the above papers for
references. Besides the comprehensive book by M¨uller and Stoyan (2002), several
other texts in actuarial mathematics contain interesting contributions on dependence
modelling (see, for example, Chapter 10 in Kaas et al. (2001) for a start). A rich set
of optimization problems within an actuarial context are to be found in De Vylder
(1996): see especially “Part II: Optimization Theory”, where the author “shows how
to obtain best upper and lower bounds on functionals T (F) of the df F of a risk,
under moment or other integral constraints”. An excellent account is to be found
--- page 272 ---

256
6. Aggregate Risk
in Denuit and Charpentier (2004). The deﬁnitive account from an actuarial point of
view is Denuit et al. (2005).
Rosenberg and Schuermann (2004) give some idea of the applicability of aggregation ideas used in this chapter. They construct the joint risk distribution for a typical,
large, internationally active bank using the method of copulas and aggregate risk
measures across the categories of market, credit and operational risk.
6.3
Capital Allocation
6.3.1
The Allocation Problem
Consider an investor who can invest in a ﬁxed set of d different investment possibilities with losses represented by the rvs L1, . . . , Ld. We have the following economic
interpretations depending on the area of application.
Performance measurement. Here the investor is a ﬁnancial institution and the Li
represent the (negative of the) P&L of d different lines of business.
Loan pricing. Here the investor is a loan book manager responsible for a portfolio
of d loans.
General investment. Here we consider either an individual or institutional investor
and the standard interpretation that the Li are (negative) P&Ls corresponding to
a set of investments in various assets.
The performance of the different business units or investments is usually measured using some sort of RORAC (return on risk-adjusted capital) approach, i.e. by
considering a ratio of the form
expected proﬁt/risk capital,
(6.18)
where we leave the precise deﬁnition of the terms vague. In many applications risk
capital might correspond to economic capital: the capital derived by considering the
ﬂuctuation of the loss around the expected loss (the unexpected loss), rather than
the absolute loss. Similarly, in a modern approach to loan pricing, the spread of a
loan contains a risk premium component, which is computed by applying a target
interest rate to the risk capital needed to sustain an individual loan (see Section 9.3.4
for details).
Obviously the general approach embodied in (6.18) raises the question of what the
appropriate risk capital for an individual investment opportunity might be. Thus the
question of performance of the investment is intimately connected with the subject
of risk measurement as addressed in Sections 2.2 and 6.1. A two-step procedure is
used in practice.
(1) Compute the overall risk capital ϱ(L), where L = d
i=1 Li and ϱ is a particular risk measure such as VaR or ES; note that at this stage we are not
stipulating that ϱ must be coherent.
--- page 273 ---

6.3. Capital Allocation
257
(2) Allocate the capital ϱ(L) to the individual investment possibilities according
to some mathematical capital allocation principle such that, if ACi denotes
the capital allocated to the investment with potential loss Li, the sum of the
allocated amounts corresponds to the overall risk capital ϱ(L).
In this section we are interested in step (2) of the procedure; loosely speaking we
require a mapping that takes as input the individual losses L1, . . . , Ld and the risk
measure ϱ and yields as output the vector (AC1, . . . , ACd) such that
ϱ(L) =
d

i=1
ACi,
(6.19)
and such a mapping will be called a capital allocation principle. The relation (6.19)
is sometimes called the full allocation property since all of the overall risk capital
ϱ(L) (not more, not less) is allocated to the investment possibilities; we consider this
property to be an integral part of the deﬁnition of an allocation principle. Of course,
there are other properties of a capital allocation principle that are desirable from an
economic viewpoint; we ﬁrst make some formal deﬁnitions and give examples of
allocation properties before discussing further properties.
The formal set-up.
Let L1, . . . , Ld be rvs on a common probability space
(Ω, F , P) representing losses (or proﬁts) for d investment possibilities. For our
discussion it will be useful to consider portfolios where the weights of the individual
investment opportunities are varied with respect to our basic portfolio (L1, . . . , Ld),
which is regarded as a ﬁxed random vector. That is, we consider an open set
Λ ⊂Rd \{0} of portfolio weights and deﬁne for λ ∈Λ the loss L(λ) = d
i=1 λiLi;
the loss of our actual portfolio is of course L(1). Let ϱ be some risk measure deﬁned
on a set M which contains the rvs {L(λ) : λ ∈Λ}. We then deﬁne the associated
risk-measure function rϱ : Λ →R by rϱ(λ) = ϱ(L(λ)). Thus rϱ(λ) is the required
risk capital for a position λ in the set of investment possibilities.
Deﬁnition 6.24. Let rϱ be a risk-measure function on some set Λ ⊂Rd \ {0}
such that 1 ∈Λ. A mapping πrϱ : Λ →Rd is called a per-unit capital allocation
principle associated with rϱ if, for all λ ∈Λ, we have
d

i=1
λiπ
rϱ
i (λ) = rϱ(λ).
(6.20)
The interpretation of this deﬁnition is that π
rϱ
i gives the amount of capital allocated
to one unit of Li, when the overall position has loss L(λ). The amount of capital
allocated to the position λiLi is thus λiπ
rϱ
i and the equality (6.20) simply means that
the overall risk capital rϱ(λ) is fully allocated to the individual portfolio positions.
6.3.2
The Euler Principle and Examples
From now on we restrict our attention to risk measures that are positive homogeneous
(satisfying Axiom 6.3 in Section 6.1.1), such as a coherent risk measure, but also
--- page 274 ---

258
6. Aggregate Risk
the standard deviation risk measure or VaR. Obviously the associated risk-measure
function must satisfy rϱ(tλ) = trϱ(λ) for all t > 0, λ ∈Λ, so rϱ : Λ →R is
a positive-homogeneous function of a vector argument. Recall Euler’s well-known
rule that states that if rϱ is positive homogeneous and differentiable at λ ∈Λ, we
have
rϱ(λ) =
d

i=1
λi
∂rϱ
∂λi
(λ).
(6.21)
Comparison of (6.21) with (6.20) suggests the following deﬁnition.
Deﬁnition 6.25 (Euler capital allocation principle). If rϱ is a positive-homogeneous risk-measure function, which is differentiable on the set Λ, then the per-unit
Euler capital allocation principle associated with rϱ is the mapping
πrϱ : Λ →Rd,
π
rϱ
i (λ) = ∂rϱ
∂λi
(λ).
(6.22)
The Euler principle is sometimes called allocation by the gradient, since
πrϱ(λ) = ∇rϱ(λ). Obviously the Euler principle gives a full allocation of the risk
capital. We now look at a number of concrete examples of Euler allocations corresponding to different choices of risk measure ϱ.
Standard deviation and the covariance principle.
Consider the risk measure function rSD(λ) = √var(L(λ)) and write Σ for the covariance matrix of (L1, . . . , Ld).
Then we have rSD(λ) = (λ′Σλ)1/2, from which it follows that
πrSD
i
(λ) = ∂rSD
∂λi
(λ) = (Σλ)i
rSD(λ) =
d
j=1 cov(Li, Lj)λj
rSD(λ)
= cov(Li, L(λ))
√var(L(λ)) .
In particular, for the original portfolio of investment possibilities corresponding to
λ = 1, the capital allocated to the ith investment possibility is
ACi = πrSD
i
(1) = cov(Li, L)
√var(L) ,
L := L(1).
(6.23)
This formula is known as the covariance principle.
VaR and VaR contributions.
Suppose that rα
VaR(λ) = qα(L(λ)). In this case it can
be shown that, subject to technical conditions,
π
rα
VaR
i
(λ) = ∂rα
VaR
∂λi
(λ) = E(Li | L(λ) = qα(L(λ))),
1 ⩽i ⩽d.
(6.24)
The derivation of (6.24) is more involved than that of the covariance principle and
we give a justiﬁcation following Tasche (2000) under the simplifying assumption
that the loss distribution of (L1, . . . , Ld) has a joint density. In the following lemma
we denote by φ(u, l2, . . . , ld) = fL1|L2,...,Ld(u | l2, . . . , ld) the conditional density
of L1.
Lemma 6.26. Assume that d ⩾2 and that (L1, . . . , Ld) has a joint density. Then,
for any vector (λ1, . . . , λd) of portfolio weights such that λ1̸ = 0, we ﬁnd that
--- page 275 ---

6.3. Capital Allocation
259
(i) L(λ) has density
fL(λ)(t) = |λ1|−1E

φ

λ−1
1

t −
d

j=2
λjLj

, L2, . . . , Ld

;
and
(ii) for i = 2, . . . , d,
E(Li | L(λ) = t) =
E(Liφ(λ−1
1 (t −d
j=2 λjLj), L2, . . . , Ld))
E(φ(λ−1
1 (t −d
j=2 λjLj), L2, . . . , Ld))
,
a.s.
Proof. For (i) consider the case λ1 > 0 and observe that we can write
P(L(λ) ⩽t) = E(P(L(λ) ⩽t | L2, . . . , Ld))
= E

P

L1 ⩽λ−1
1

t −
d

j=2
λjLj
 				 L2, . . . , Ld

= E
  λ−1
1 (t−d
j=2 λj Lj )
−∞
φ(u, L2, . . . , Ld) du

.
The assertion follows on differentiating under the expectation.
For (ii) observe that we can write
E(Li | L(λ) = t) = lim
δ→0
δ−1E(LiI{t<L(λ)⩽t+δ})
δ−1P(t < L(λ) ⩽t + δ) = (∂/∂t)E(LiI{L(λ)⩽t})
fL(λ)(t)
,
provided fL(λ)(t)̸ = 0. The result follows on applying a similar conditioning technique to the ones used in the proof of (i) to the numerator.
We now explain why (6.24) follows from Lemma 6.26. Since the rv L(λ) has a
density, we have P(L(λ) ⩽qα(L(λ))) = α. Writing k(t) = λ−1
1 (t −d
j=2λjLj)
we have
α = P(L(λ) ⩽rα
VaR(λ)) = E
  k(rα
VaR(λ))
−∞
φ(u, L2, . . . , Ld) du

.
(6.25)
We take derivatives of (6.25) with respect to λi for i = 2, . . . , d to get
0 = λ−1
1 E
∂rα
VaR(λ)
∂λi
−Li

φ(k(rα
VaR(λ)), L2, . . . , Ld)

.
Solving this expression for ∂rα
VaR(λ)/∂λi and using part (ii) of Lemma 6.26
yields (6.24), as desired. Analogous calculations can be done for i = 1 and λ1 < 0.
Tasche (2000) makes the derivations mathematically rigorous by using the implicit
function theorem and giving all necessary conditions. In summary, the capital allocation takes the form ACi = E(Li | L = VaRα(L)), L := L(1).
--- page 276 ---

260
6. Aggregate Risk
Expected shortfall and shortfall contributions.
Now consider using the riskmeasure function rα
ES(λ) = E(L | L ⩾qα(L(λ))) corresponding to expected
shortfall. It follows from Deﬁnition 2.15 that we can write
rα
ES(λ) =
1
1 −α
 1
α
ru
VaR(λ) du,
where we make use of the notation rα
VaR(λ) = qα(L(λ)) as above. We apply the
Euler principle by again computing the derivative with respect to λi. Assuming the
differentiability of ru
VaR(λ), we have
∂rα
ES
∂λi
(λ) =
1
1 −α
 1
α
∂ru
VaR
∂λi
(λ) du =
1
1 −α
 1
α
E(Li | L(λ) = qu(L(λ))) du.
NowweassumethatfL(λ) isstrictlypositivesothatthedfofL(λ)hasadifferentiable
inverse and we can make the change of variables v = qu(L(λ)) = F ←
L(λ)(u). Since
dv/du = (fL(λ)(v))−1, we get
∂rα
ES
∂λi
(λ) =
1
1 −α
 ∞
qα(L(λ))
E(Li | L(λ) = v)fL(λ)(v) dv
=
1
1 −α E(Li; L(λ) ⩾qα(L(λ))).
This gives a capital allocation of the form
ACi = E(Li | L ⩾VaRα(L)),
L := L(1),
(6.26)
where ACi is known as the expected shortfall contribution of investment possibility
(or line of business) i. This is a popular allocation principle in practice, and is
generally considered to be preferable to the covariance principle and the principle
based on VaR contributions. See Notes and Comments for literature on its use in
practice in the context of credit portfolios.
Euler allocation for elliptical loss distributions.
In the following corollary to Theorem 6.8 we consider the special case of an elliptical loss distribution for the vector
of investment opportunities (L1, . . . , Ld). We consider this distribution to be centred at zero so that it really represents ﬂuctuations of the loss around the expected
loss. We ﬁnd that the relative amounts of capital allocated to each investment opportunity are always the same, regardless of whether we base an Euler allocation on the
standard deviation, VaR or expected shortfall risk measures, or indeed any positivehomogeneous risk measure. Thus allocation is very simple in this case: depending
on our choice of risk measure we calculate the total risk capital to be allocated and
then use a simple partitioning formula given in (6.27) below.
Corollary 6.27. Assume that rϱ : Λ →R is the risk-measure function of a positivehomogeneous risk measure ϱ depending only on the distribution of the loss. Let
L ∼Ed(0, Σ, ψ). Then, under an Euler allocation, the relative capital allocation is
given by
ACi
ACj
= π
rϱ
i (1)
π
rϱ
j (1)
=
d
k=1 Σik
d
k=1 Σjk
,
1 ⩽i, j ⩽d.
(6.27)
--- page 277 ---

6.3. Capital Allocation
261
Proof. From the proof of Theorem 6.8 we deduce that, by the positive homogeneity
of the risk measure, we have
rϱ(λ) = ϱ(L(λ)) = ϱ

d

i=1
λiLi

=
√
λ′Σλϱ(Y1),
where Y1 is the ﬁrst component of a spherical random vector with characteristic
generator ψ. For the allocation we get
πrϱ(λ) = ∇rϱ(λ) =
Σλ
√
λ′Σλ
ϱ(Y1),
from which the result follows.
6.3.3
Economic Justiﬁcation of the Euler Principle
Signals for performance measurement.
A ﬁrst economic justiﬁcation for capital
allocation based on the Euler principle was given by Tasche (1999), who addressed
the issue of whether it gave “the right signals for investment decisions”. He formalized the idea as follows.
Deﬁnition 6.28. Let rϱ be a risk-measure function which is differentiable on Λ
and πrϱ an associated per-unit capital allocation principle. Then πrϱ is suitable for
performance measurement if, for all λ ∈Λ, we have
∂
∂λi
−E(L(λ))
rϱ(λ)

⎧
⎪⎪⎪⎨
⎪⎪⎪⎩
> 0,
if −E(Li)
π
rϱ
i (λ)
> −E(L(λ))
rϱ(λ)
,
< 0,
if −E(Li)
π
rϱ
i (λ)
< −E(L(λ))
rϱ(λ)
.
In words, this says that if the performance of investment opportunity i as measured
by its per-unit return divided by per-unit risk capital π
rϱ
i
is better (respectively,
worse) than the performance of the overall portfolio, then increasing (respectively,
decreasing) the weight λi of that investment opportunity by a small amount improves
the overall performance of the portfolio. Tasche then proves the following result,
for the proof of which we refer to the original paper.
Proposition 6.29. Under the assumptions of Deﬁnition 6.28, the only per-unit capital allocation principle suitable for performance measurement is the Euler principle.
Fairness considerations.
Another justiﬁcation for the Euler principle was given
by Denault (2001). His approach uses cooperative game theory and is based on
the notion of “fairness”. Assume that the risk-measure function rϱ derives from a
coherent risk measure ϱ. In that case, since ϱ(L) ⩽d
i=1 ϱ(Li), the overall risk
capital required for the portfolio is smaller than the sum of the risk capital required
for the business units on a stand-alone basis. Fairness now means that each business
unit proﬁts from this diversiﬁcation beneﬁt, in the sense that ACi ⩽ϱ(Li). In the
next deﬁnition we slightly extend this intuitive notion of fairness.
--- page 278 ---

262
6. Aggregate Risk
Deﬁnition 6.30. Given a coherent risk measure ϱ with associated risk-measure
function rϱ, a per-unit capital allocation principle πrϱ is said to be fair if, for all
λ ∈Λ and all γ ∈[0, 1]d, the following inequality holds:
d

i=1
γiλiπ
rϱ
i (λ) ⩽rϱ(γ1λ1, . . . , γdλd).
(6.28)
Note that, by the deﬁnition of a per-unit capital allocation principle in (6.20), we
have equality in (6.28) if we take γ = 1. The economic interpretation of (6.28)
is straightforward for a vector γ ∈{0, 1}d satisfying γi = I{i∈N}, where N ⊂
{1, . . . , d} is a subset of the investment opportunities. In that case the left-hand side
of (6.28) gives the combined capital that is allocated to the investment opportunities
in the set N given that the overall portfolio is represented by the vector λ with
loss L(λ) = d
i=1 λiLi. The right-hand side is the combined capital allocated to
the opportunities in the set N on a stand-alone basis, i.e. in a portfolio with no
investments in the opportunities Nc := {1, . . . , d}\N and loss given by 
i∈N λiLi.
Since ϱ is coherent and, in particular, subadditive, we have
ϱ

d

i=1
λiLi

⩽ϱ
 
i∈N
λiLi

+ ϱ
 
i∈Nc
λiLi

,
which essentially says that the investments in N enjoy a diversiﬁcation beneﬁt by
being part of the overall portfolio represented by λ. Fairness suggests that they
should proﬁt from this beneﬁt by being allocated a smaller amount of capital than
they would have on a stand-alone basis; this is exactly the content of (6.28).
The interpretation of (6.28) for general γ ∈(0, 1]d is more involved, but perhaps easiest if we use the interpretation that the Li represent losses for different
lines of business. We introduce the portfolio ˜λ = (γ1λ1, . . . , γdλd)′ and note that
it represents a scaling back of activity across the ﬁrm with respect to the original
portfolio λ. We can rewrite (6.28) as
d

i=1
˜λiπ
rϱ
i (λ) ⩽
d

i=1
˜λiπ
rϱ
i (˜λ).
The left-hand side represents the overall capital allocated to the scaled-back portfolio
considered as part of the original portfolio. The right-hand side represents the overall
capital allocated to the scaled-back portfolio considered as a stand-alone entity. If
the inequality were the other way round, there would be a systematic incentive for
business units to scale back their activities.
Translating a game-theoretical result of Aubin (1979) into the context of capital
allocation with a coherent risk measure, Denault (2001) shows that for a differentiable risk-measure function rϱ that is derived from a coherent risk measure ϱ, the
only fair allocation principle is the Euler principle. Obviously, this gives additional
support for using the Euler principle if one works in the realm of coherent risk
measures.
--- page 279 ---

6.3. Capital Allocation
263
From a practical point of view, the use of expected shortfall and expected shortfall
contributions might be a reasonable choice in many application areas, particularly
for credit risk management and loan pricing (see Notes and Comments, where this
issue is discussed further).
Notes and Comments
A broad, non-technical discussion of capital allocation and performance measurement is to be found in Matten (2000). The term “Euler principle” seems to have
been ﬁrst used in Patrik, Bernegger and R¨uegg (1999). The result (6.24) is found in
Gourieroux and Scaillet (2000) andTasche (2000); the former paper assumes that the
losses have a joint density and the latter gives a slightly more general result as well
as technical details concerning the differentiability of the VaR and ES risk measures
with respect to the portfolio composition. Differentiability of the coherent premium
principle of Section 6.1.3 is discussed in Fischer (2003). The derivation of allocation
principles from properties of risk measures is also to be found in Goovaerts, Dhaene
and Kaas (2003) and Goovaerts, van den Boor and Laeven (2005).
For the arguments concerning suitability of risk measures for performance measurement, see Tasche (1999). The game-theoretic approach to allocation is found
in Denault (2001); see also Kalkbrener (2005) for similar arguments. For an early
contribution on game theory applied to cost allocation in an insurance context, see
Lemaire (1984).
Applications to credit risk are found in Kalkbrener, Lotter and Overbeck (2004)
and Merino and Nyfeler (2003); these make strong arguments in favour of the use of
expected shortfall contributions. However, Pfeifer (2004) contains some compelling
examples to show that expected shortfall as a risk measure and expected shortfall
contributions as an allocation method may have some serious deﬁciencies when
used in non-life insurance. The existence of rare, extreme events may lead to absurd
capital allocations when based on expected shortfall. The reader is therefore urged
to reﬂect carefully before settling on a speciﬁc risk measure and allocation principle.
It may also be questionable to base a “coherent” risk-sensitive capital allocation on
formal criteria only; for further details on this see Koryciorz (2004).
--- page 280 ---

7
Extreme Value Theory
Much of this chapter is based on the presentation of extreme value theory (EVT)
in Embrechts, Kl¨uppelberg and Mikosch (1997) (henceforth EKM) and whenever
theoretical detail is missing the reader should consult that text. Our intention here
is to provide more information about the statistical methods of EVT than is given
in EKM, while brieﬂy summarizing the theoretical ideas on which the statistical
methods are based.
Broadly speaking, there are two main kinds of model for extreme values. The
most traditional models are the block maxima models described in Section 7.1: these
are models for the largest observations collected from large samples of identically
distributed observations.
A more modern and powerful group of models are those for threshold exceedances, described in Section 7.2. These are models for all large observations that
exceed some high level, and are generally considered to be the most useful for
practical applications, due to their more efﬁcient use of the (often limited) data on
extreme outcomes.
Section 7.3 is a shorter, theoretical section providing more information about
the tails of some of the distributions and models that are prominent in this book,
includingthetailsofnormalvariancemixturemodelsandstrictlystationaryGARCH
models.
Sections 7.5 and 7.6 provide a concise summary of the more important ideas in
multivariate extreme value theory; they deal, respectively, with multivariate maxima
and multivariate threshold exceedances. The novelty of these sections is that the
ideas are presented as far as possible using the copula methodology of Chapter 5.
The style is similar to Sections 7.1 and 7.2, with the main results being mostly stated
without proof and an emphasis being given to examples relevant for applications.
7.1
Maxima
To begin with we consider a sequence of iid rvs (Xi)i∈N representing ﬁnancial losses.
These may have a variety of interpretations, such as operational losses, insurance
losses and losses on a credit portfolio over ﬁxed time intervals. Later we relax the
assumption of independence and consider that the rvs form a strictly stationary time
series of dependent losses; they might be (negative) returns on an investment in a
single stock, an index, or a portfolio of investments.
--- page 281 ---

7.1. Maxima
265
7.1.1
Generalized Extreme Value Distribution
Convergence of sums.
The role of the generalized extreme value (GEV) distribution in the theory of extremes is analogous to that of the normal distribution
(and more generally the stable laws) in the central limit theory for sums of rvs.
Assuming that the underlying rvs X1, X2, . . . are iid with a ﬁnite variance and writing Sn = X1 + · · · + Xn for the sum of the ﬁrst n rvs, the standard version of the
central limit theorem (CLT) says that appropriately normalized sums (Sn −an)/bn
converge in distribution to the standard normal distribution as n goes to inﬁnity. The
appropriate normalization uses sequences of normalizing constants (an) and (bn)
deﬁned by an = nE(X1) and bn = √var(X1). In mathematical notation we have
lim
n→∞P
Sn −an
bn
⩽x

= Φ(x),
x ∈R.
Convergence of maxima.
Classical EVT is concerned with limiting distributions
for normalized maxima Mn = max(X1, . . . , Xn) of iid rvs; we refer to these as block
maxima. The only possible non-degenerate limiting distributions for normalized
block maxima are in the GEV family.
Deﬁnition 7.1 (the generalized extreme value (GEV) distribution). The df of the
(standard) GEV distribution is given by
Hξ(x) =

exp(−(1 + ξx)−1/ξ),
ξ̸ = 0,
exp(−e−x),
ξ = 0,
where 1 + ξx > 0. A three-parameter family is obtained by deﬁning Hξ,µ,σ(x) :=
Hξ((x −µ)/σ) for a location parameter µ ∈R and a scale parameter σ > 0.
The parameter ξ is known as the shape parameter of the GEV distribution and
Hξ deﬁnes a type of distribution, meaning a family of distributions speciﬁed up to
location and scaling (see Section A.1.1 for a formal deﬁnition). The extreme value
distribution in Deﬁnition 7.1 is generalized in the sense that the parametric form
subsumes three types of distribution which are known by other names according to
the value of ξ: when ξ > 0 the distribution is a Fr´echet distribution; when ξ = 0
it is a Gumbel distribution; when ξ < 0 it is a Weibull distribution. We also note
that for ﬁxed x we have limξ→0 Hξ(x) = H0(x) (from either side) so that the
parametrization in Deﬁnition 7.1 is continuous in ξ, which facilitates the use of this
distribution in statistical modelling.
The df and density of the GEV distribution are shown in Figure 7.1 for the three
cases ξ = 0.5, ξ = 0 and ξ = −0.5, corresponding to Fr´echet, Gumbel and Weibull
types, respectively. Observe that theWeibull distribution is a short-tailed distribution
with a so-called ﬁnite right endpoint. The right endpoint of a distribution will be
denoted by xF = sup{x ∈R : F(x) < 1}. The Gumbel and Fr´echet distributions
have inﬁnite right endpoints, but the decay of the tail of the Fr´echet distribution is
much slower than that of the Gumbel distribution.
Suppose that block maxima Mn of iid rvs converge in distribution under an appropriate normalization. Recalling that P(Mn ⩽x) = F n(x), we observe that this
--- page 282 ---

266
7. Extreme Value Theory
−2
0
2
4
6
8
−2
0
2
4
6
8
x
x
0.1
0.2
0.4
0.6
0.8
1.0
0.2
0.3
0.4
0
0
h(x)
H(x)
(a)
(b)
Figure 7.1.
(a) The df of a standard GEV distribution in three cases: the solid line corresponds to ξ = 0 (Gumbel); the dotted line is ξ = 0.5 (Fr´echet); and the dashed line is
ξ = −0.5 (Weibull). (b) Corresponding densities. In all cases µ = 0 and σ = 1.
convergence means that there exist sequences of real constants (dn) and (cn), where
cn > 0 for all n, such that
lim
n→∞P((Mn −dn)/cn ⩽x) = lim
n→∞F n(cnx + dn) = H(x)
(7.1)
for some non-degenerate df H(x). The role of the GEV distribution in the study of
maxima is formalized by the following deﬁnition and theorem.
Deﬁnition 7.2 (maximum domain of attraction). If (7.1) holds for some nondegenerate df H, then F is said to be in the maximum domain of attraction of H,
written F ∈MDA(H).
Theorem 7.3 (Fisher–Tippett, Gnedenko). If F ∈MDA(H) for some nondegenerate df H then H must be a distribution of type Hξ, i.e. a GEV distribution.
Remarks 7.4.
(1) If convergence of normalized maxima takes place, the type of the limiting distribution (as speciﬁed by ξ) is uniquely determined, although the location and
scaling of the limit law (µ and σ) depend on the exact normalizing sequences
chosen; this is guaranteed by the so-called “convergence to types theorem”
(EKM, p. 554). It is always possible to choose these sequences such that the
limit appears in the standard form Hξ.
(2) By non-degenerate df we mean a limiting distribution which is not concentrated on a single point.
Examples.
We calculate two examples to show how the GEV limit emerges for
two well-known underlying distributions and appropriately chosen normalizing
sequences. To discover how normalizing sequences may be constructed in general
we refer to Section 3.3 of EKM.
--- page 283 ---

7.1. Maxima
267
Example 7.5 (exponential distribution). If the underlying distribution is an exponential distribution with df F(x) = 1 −exp(−βx) for β > 0 and x ⩾0, then
by choosing normalizing sequences cn = 1/β and dn = ln n/β we can directly
calculate the limiting distribution of maxima using (7.1). We get
F n(cnx + dn) =

1 −1
n exp(−x)
n
,
x ⩾−ln n,
lim
n→∞F n(cnx + dn) = exp(−e−x),
x ∈R,
from which we conclude that F ∈MDA(H0).
Example 7.6 (Pareto distribution). If the underlying distribution is a Pareto distribution (Pa(α, κ)) with df F(x) = 1 −(κ/(κ + x))α for α > 0, κ > 0 and x ⩾0,
we can take normalizing sequences cn = κn1/α/α and dn = κn1/α −κ. Using (7.1)
we get
F n(cnx + dn) =

1 −1
n

1 + x
α
−αn
,
1 + x
α ⩾n−1/α,
lim
n→∞F n(cnx + dn) = exp

−

1 + x
α
−α
,
1 + x
α > 0,
from which we conclude that F ∈MDA(H1/α).
Convergence of minima.
The limiting theory for convergence of maxima encompasses the limiting behaviour of minima using the identity
min(X1, . . . , Xn) = −max(−X1, . . . , −Xn).
(7.2)
It is not difﬁcult to see that normalized minima of iid samples with df F will convergence in distribution if the df ˜F(x) = 1 −F(−x), which is the df of the rvs
−X1, . . . , −Xn, is in the maximum domain of attraction of an extreme value distribution. Writing M∗
n = max(−X1, . . . , −Xn) and assuming that ˜F ∈MDA(Hξ)
we have
lim
n→∞P
M∗
n −dn
cn
⩽x

= Hξ(x),
from which it follows easily, using (7.2), that
lim
n→∞P
min(X1, . . . , Xn) + dn
cn
⩽x

= 1 −Hξ(−x).
Thus appropriate limits for minima are distributions of type 1 −Hξ(−x). For a
symmetric distribution F we have ˜F(x) = F(x), so that if Hξ is the limiting type of
distribution for maxima for a particular value of ξ, then 1 −Hξ(−x) is the limiting
type of distribution for minima.
7.1.2
Maximum Domains of Attraction
For most applications it is sufﬁcient to note that essentially all the common continuous distributions of statistics or actuarial science are in MDA(Hξ) for some value
--- page 284 ---

268
7. Extreme Value Theory
of ξ. In this section we consider the issue of which underlying distributions lead to
which limits for maxima.
The Fr´echet case.
The distributions that lead to the Fr´echet limit Hξ(x) for ξ > 0
have a particularly elegant characterization involving slowly varying or regularly
varying functions.
Deﬁnition 7.7 (slowly varying and regularly varying functions).
(i) A positive, Lebesgue-measurable function L on (0, ∞) is slowly varying at ∞
if
lim
x→∞
L(tx)
L(x) = 1,
t > 0.
(ii) A positive, Lebesgue-measurable function h on (0, ∞) is regularly varying
at ∞with index ρ ∈R if
lim
x→∞
h(tx)
h(x) = tρ,
t > 0.
Slowly varying functions are functions which, in comparison with power functions,
change relatively slowly for large x, an example being the logarithm L(x) = ln(x).
Regularly varying functions are functions which can be represented by power functions multiplied by slowly varying functions, i.e. h(x) = xρL(x).
Theorem 7.8 (Fr´echet MDA, Gnedenko). For ξ > 0,
F ∈MDA(Hξ) ⇐⇒
¯F(x) = x−1/ξL(x)
(7.3)
for some function L slowly varying at ∞.
This means that distributions giving rise to the Fr´echet case are distributions with
tails that are regularly varying functions with a negative index of variation. Their
tails decay essentially like a power function and the rate of decay α = 1/ξ is often
referred to as the tail index of the distribution.
These distributions are the most studied distributions in EVT and they are of particular interest in ﬁnancial applications because they are heavy-tailed distributions
with inﬁnite higher moments. If X is a non-negative rv whose df F is an element
of MDA(Hξ) for ξ > 0, then it may be shown that E(Xk) = ∞for k > 1/ξ
(EKM, p. 568). If, for some small ε > 0, the distribution is in MDA(H(1/2)+ε), it is
an inﬁnite-variance distribution, and if the distribution is in MDA(H(1/4)+ε), it is a
distribution with inﬁnite fourth moment.
Example 7.9 (Pareto distribution). In Example 7.6 we veriﬁed by direct calculation that normalized maxima of iid Pareto variates converge to a Fr´echet distribution.
Observe that the tail of the Pareto df in (A.13) may be written ¯F(x) = x−αL(x),
where it may be easily checked that L(x) = (κ−1 + x−1)−α is a slowly varying
function; indeed, as x →∞, L(x) converges to the constant κα. Thus we verify
that the Pareto df has the form (7.3).
--- page 285 ---

7.1. Maxima
269
Further examples of distributions giving rise to the Fr´echet limit for maxima
include the Fr´echet distribution itself, inverse gamma, Student t, loggamma, F
and Burr distributions. We will provide further demonstrations for some of these
distributions in Section 7.3.1.
The Gumbel case.
The characterization of distributions in this class is more complicated than in the Fr´echet class. We have seen in Example 7.5 that the exponential
distribution is in the Gumbel class and, more generally, it could be said that the
distributions in this class have tails that have an essentially exponential decay. A
positive-valued rv with a df in MDA(H0) has ﬁnite moments of any positive order,
i.e. E(Xk) < ∞for every k > 0 (EKM, p. 148).
However, there is a great deal of variety in the tails of distributions in this class, so,
for example, both the normal and the lognormal distributions belong to the Gumbel
class (EKM, pp. 145–147). The normal distribution, as discussed in Section 3.1.4, is
thin tailed, but the lognormal distribution has much heavier tails and we would need
to collect a lot of data from the lognormal distribution before we could distinguish
its tail behaviour from that of a distribution in the Fr´echet class.
In ﬁnancial modelling it is often erroneously assumed that the only interesting
models for ﬁnancial returns are the power-tailed distributions of the Fr´echet class.
The Gumbel class is also interesting because it contains many distributions with
much heavier tails than the normal, even if these are not regularly varying power
tails. Examples are hyperbolic and generalized hyperbolic distributions (with the
exception of the special boundary case that is Student t).
Other distributions in MDA(H0) include the gamma, chi-squared, standard
Weibull (to be distinguished from the Weibull special case of the GEV distribution) and Benktander type I and II distributions (which are popular actuarial loss
distributions) and the Gumbel itself. We provide demonstrations for some of these
examples in Section 7.3.2.
The Weibull case.
This is perhaps the least important case for ﬁnancial modelling,
at least in the area of market risk, since the distributions in this class all have ﬁnite
right endpoints.Although all potential ﬁnancial and insurance losses are, in practice,
bounded, we will still tend to favour models that have inﬁnite support for loss
modelling. An exception may be in the area of credit risk modelling, where we will
see in Chapter 8 that probability distributions on the unit interval [0, 1] are very
useful. A characterization of the Weibull class is as follows.
Theorem 7.10 (Weibull MDA, Gnedenko). For ξ < 0,
F ∈MDA(H1/ξ) ⇐⇒xF < ∞and ¯F(xF −x−1) = x1/ξL(x)
for some function L slowly varying at ∞.
It can be shown (EKM, p. 137) that a beta distribution with density fα,β as given
in (A.4) is in MDA(H−1/β).This includes the special case of the uniform distribution
for β = α = 1.
--- page 286 ---

270
7. Extreme Value Theory
7.1.3
Maxima of Strictly Stationary Time Series
The standard theory of the previous sections concerns maxima of iid sequences.
With ﬁnancial time series in mind, we now look brieﬂy at the theory for maxima
of strictly stationary time series and ﬁnd that the same types of limiting distribution
apply.
In this section let (Xi)i∈Z denote a strictly stationary time series with stationary distribution F and let ( ˜Xi)i∈N denote the associated iid process, i.e. a
strict white noise process with the same df F. Let Mn = max(X1, . . . , Xn) and
˜Mn = max( ˜X1, . . . , ˜Xn) denote block maxima of the original series and the iid
series, respectively.
For many processes (Xi)i∈N, it may be shown that there exists a real number θ
in (0, 1] such that
lim
n→∞P{( ˜Mn −dn)/cn ⩽x} = H(x)
(7.4)
for a non-degenerate limit H(x) if and only if
lim
n→∞P{(Mn −dn)/cn ⩽x} = H θ(x).
(7.5)
Forsuchprocessesthisvalueθ isknownastheextremalindex oftheprocess(nottobe
confused with the tail index of distributions in the Fr´echet class).A formal deﬁnition
ismoretechnical(seeNotesandComments)butthebasicideasbehind(7.4)and(7.5)
are easily explained.
For processes with an extremal index, normalized block maxima converge in
distribution provided that maxima of the associated iid process converge in distribution: that is, provided the underlying distribution F is in MDA(Hξ) for some ξ.
Moreover, since H θ
ξ (x) can be easily veriﬁed to be a distribution of the same type as
Hξ(x), the limiting distribution of the normalized block maxima of the dependent
series is a GEV distribution with exactly the same ξ parameter as the limit for the
associated iid data; only the location and scaling of the distribution may change.
Writing u = cnx + dn we observe that, for large enough n, (7.4) and (7.5) imply
that
P(Mn ⩽u) ≈P θ( ˜Mn ⩽u) = F nθ(u),
(7.6)
so that for u large the probability distribution of the maximum of n observations
from the time series with extremal index θ can be approximated by the distribution
of the maximum of nθ < n observations from the associated iid series. In a sense,
nθ can be thought of as counting the number of roughly independent clusters of
observations in n observations, and θ is often interpreted as the reciprocal of the
mean cluster size.
Not every strictly stationary process has an extremal index (see EKM, p. 418,
for a counterexample) but, for the kinds of time series processes that interest us in
ﬁnancial modelling, an extremal index generally exists. Essentially, we only have
to distinguish between the cases when θ = 1 and the cases when θ < 1: for the
former there is no tendency to cluster at high levels and large sample maxima from
the time series behave exactly like maxima from similarly sized iid samples; for the
latter we must be aware of a tendency for extreme values to cluster.
