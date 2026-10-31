# Quantitative Risk Management_ Concepts, Techniques, and -- Alexander J_ McNeil, Rüdiger Frey, Paul Embrechts -- Princeton series in finance, -- isbn13 9780691122557 -- 478a0059673fecd0c76229cd3d8884e7 -- Anna’s Arc.pdf — pages 438–457

--- page 438 ---

422
9. Dynamic Credit Risk Models
9.5.1
Basic Results
The PDE characterization of f .
We assume that the state variable process (Ψt) is
the unique solution of the SDE
dΨt = µ(Ψt) dt + σ(Ψt) dWt,
Ψ0 = ψ ∈D,
(9.33)
with state space given by the domain D ⊆R. Here (Wt) is a standard, onedimensional Brownian motion on some ﬁltered probability space (Ω, F , P, (Ft)),
and µ and σ are continuous functions from D to R, respectively R+. Consider functions R, g : D →R+. Since (Ψt) is Markovian, given the present value Ψt, the
future evolution (Ψs)s⩾t of the state variable process is independent of Ft, and we
obtain
E

exp

−
 T
t
R(Ψs) ds

g(ΨT )
				 Ft

= f (t, Ψt)
(9.34)
for some function f : [0, T ]×D →R+. The next lemma gives the characterization
of f in terms of a parabolic PDE announced above.
Lemma 9.26 (Feynman–Kac). If f is once continuously differentiable in t and
twice continuously differentiable in ψ, it solves the terminal-value problem
ft + µ(ψ)fψ + 1
2σ 2(ψ)fψψ = R(ψ)f,
(t, ψ) ∈[0, T ) × D,
f (T, ψ) = g(ψ),
ψ ∈D,
'
(9.35)
where lower indices denote partial derivatives. Conversely, suppose that the function
g is bounded, that R(ψ) ⩾0 for all ψ ∈D, and that ˜f : [0, T ] × D →R+ is a
bounded solution of the terminal value problem (9.35). Let (Ψt) be a solution of the
SDE (9.33). Then E(exp(−
 T
t R(Ψs) ds)g(ΨT ) | Ft) = ˜f (t, Ψt).
The Feynman–Kac formula is a standard result of stochastic calculus and it is
discussed in many textbooks on stochastic processes and ﬁnancial mathematics, so
we omit the proof (references are given in Notes and Comments).
Afﬁne term structure.
The following assumption ensures that the solution of the
PDE (9.35), with terminal condition g(ψ) = exp(uψ), uψ ⩽0 for ψ ∈D, is of
the form (9.32), so that we have an afﬁne term structure. Note that g ≡1 for u = 0;
this is the appropriate terminal condition for pricing zero-coupon bonds.
Assumption 9.27. R, µ and σ 2 are afﬁne functions of ψ, i.e. there are constants
ρ0, ρ1, k0, k1, h0 and h1 such that R(ψ) = ρ0 + ρ1ψ, µ(ψ) = k0 + k1ψ and
σ 2(ψ) = h0 + h1ψ. Moreover, for all ψ ∈D we have h0 + h1ψ ⩾0 and
ρ0 + ρ1ψ ⩾0.
Fix some T > 0. We try to ﬁnd a solution of (9.35) of the form ˜f (t, ψ) =
exp(α(t, T ) + β(t, T )ψ) for continuously differentiable functions α(· , T ) and
β(· , T ). As ˜f (T, ψ) = exp(uψ), we immediately obtain the terminal condition
α(T, T ) = 0, β(T, T ) = u. Denote by α′(· , T ) and β′(· , T ) the derivative of α and
β with respect to t. Using the special form of ˜f we obtain that
˜ft = (α′ + β′ψ) ˜f ,
˜fψ = β ˜f
and
˜fψψ = β2 ˜f .
--- page 439 ---

9.5. Afﬁne Models
423
Hence, under Assumption 9.27 the PDE (9.35) takes the form
(α′ + β′ψ) ˜f + (k0 + k1ψ)β ˜f + 1
2(h0 + h1ψ)β2 ˜f = (ρ0 + ρ1ψ) ˜f .
Dividing by ˜f and rearranging we obtain
α′ + k0β + 1
2h0β2 −ρ0 + (β′ + k1β + 1
2h1β2 −ρ1)ψ = 0.
Since this equation must hold for all ψ ∈D, we obtain the following ODE system:
β′(t, T ) = ρ1 −k1β(t, T ) −1
2h1β2(t, T ),
β(T, T ) = u,
(9.36)
α′(t, T ) = ρ0 −k0β(t, T ) −1
2h0β2(t, T ),
α(T, T ) = 0.
(9.37)
The ODE (9.36) for β(· , T ) is a so-called Ricatti equation. While explicit solutions exist only in certain special cases, the ODE is easily solved numerically. The
ODE (9.37) for α(· , T ) can be solved by simple (numerical) integration once β has
been determined. Summing up, we have the following proposition.
Proposition 9.28. Suppose that Assumption 9.27 holds, that the ODE system
(9.36), (9.37) has a unique solution (α, β) on [0, T ] and that there is some C such
that β(t, T )ψ ⩽C for all t ∈[0, T ], ψ ∈D. Then
E

exp

−
 T
t
R(Ψs) ds

exp(uΨT )
				 Ft

= exp(α(t, T ) + β(t, T )Ψt).
Proof. The result follows immediately from Lemma 9.26, as our assumption on β
implies that ˜f (t, ψ) = exp(α(t, T ) + β(t, T )ψ) is bounded.
9.5.2
The CIR Square-Root Diffusion
A very popular afﬁne model is the square-root diffusion model proposed by Cox,
Ingersoll and Ross (1985) as a model for the short rate of interest. In this model (Ψt)
is given by the solution of the SDE
dΨt = κ( ¯θ −Ψt) dt + σ

Ψt dWt,
Ψ0 = ψ > 0,
(9.38)
for parameters κ, ¯θ, σ > 0 and state space D = [0, ∞). Clearly, (9.38) is an afﬁne
model in the sense of Assumption 9.27; the parameters are given by k0 = κ ¯θ,
k1 = −κ, h0 = 0 and h1 = σ 2.
It is well known that the SDE (9.38) admits a global solution (see Notes and
Comments for a reference). This issue is non-trivial since the square-root function
is not Lipschitz and since one has to ensure that the solution remains in D for all
t > 0. Note that (9.38) implies that (Ψt) is a mean reverting process: if Ψt deviates
from the mean-reversion level ¯θ, the process is pulled back towards ¯θ. Moreover, if
the mean reversion is sufﬁciently strong relative to the volatility, trajectories never
reach zero. More precisely, let τ0(Ψ ) := inf{t ⩾0 : Ψt = 0}. It is well known
that for κ ¯θ ⩾1
2σ 2 we have P(τ0(Ψ ) < ∞) = 0, whereas for κ ¯θ < 1
2σ 2 we have
P(τ0(Ψ ) < ∞) = 1.
--- page 440 ---

424
9. Dynamic Credit Risk Models
In the CIR square-root model the Ricatti equations (9.36) and (9.37) can be solved
explicitly. Using Proposition 9.28, one has
E

exp

−
 T
t
(ρ0 + ρ1Ψs) ds
 				 Ft

= exp(α(T −t) + β(T −t)Ψt),
with
β(τ) =
−2ρ1(eγ τ −1)
γ −κ + eγ τ(γ + κ),
(9.39)
α(τ) = −ρ0τ + 2κ ¯θ
σ 2 ln

2γ e1/2τ(γ + κ)
γ −κ + eγ τ(γ + κ)

,
(9.40)
and τ := T −t, γ :=

κ2 + 2σ 2ρ1. These formulas are the key to pricing bonds
in models where the risk-free short rate and default intensities are afﬁne functions
of independent square-root processes, as is shown in the next example.
Example 9.29 (a three-factor model). We now consider the pricing of zero-coupon
bonds in a three-factor model similar to models that are frequently used in the
literature. We assume that Ψt = (Ψt,1, Ψt,2, Ψt,3)′ is a vector of three independent
square-root diffusions with dynamics dΨt,i = κi( ¯θi −Ψt,i) dt + σi

Ψt,i dWt,i for
independentBrownianmotions(Wt,i), i = 1, 2, 3.Therisk-freeshortrateofinterest
is given by rt = r0 + Ψt,2 −Ψt,1 for a constant r0 ⩾0; the hazard rate of the
counterparty under consideration is given by γt = γ1Ψt,1 + Ψt,3 for some constant
γ1 > 0. This parametrization allows for negative instantaneous correlation between
(rt) and (γt), which is in line with empirical evidence. Note, however, that this
negative correlation comes at the expense of possibly negative riskless interest rates.
In this context the price of a default-free zero-coupon bond is given by
p0(t, T ) = E

exp

−
 T
t
rs ds
 				 Ft

= e−r0(T −t)E

exp

−
 T
t
Ψs,2 ds
 				 Ft

E

exp
  T
t
Ψs,1 ds
 				 Ft

,
(9.41)
where we have used the independence of (Ψt,1), (Ψt,2), (Ψt,3). Each of the terms
in (9.41) can be evaluated using the above formulas for α and β (equations (9.39)
and (9.40)).Assuming that we have recovery of treasury in default (see Section 9.4.1)
and a deterministic percentage loss given default δ, we obtain that the price of a
defaultable zero-coupon bond is given by
p1(t, T ) = (1 −δ)p0(t, T ) + δE

exp

−
 T
t
(rs + γs) ds
 				 Ft

.
By deﬁnition of rt and γt the last term on the right-hand side equals
δE

exp

−
 T
t
r0 + (γ1 −1)Ψs,1 + Ψs,2 + Ψs,3 ds
 				 Ft

,
which can be evaluated in a similar way to the evaluation of expression (9.41). In the
next section we will show how one deals with more complicated recovery models,
such as recovery of face value.
--- page 441 ---

9.5. Afﬁne Models
425
9.5.3
Extensions
A jump-diffusion model for (Ψt).
We brieﬂy discuss an extension of the basic
model(9.33),wheretheeconomicfactorprocess(Ψt)followsadiffusionwithjumps.
Adding jumps to the dynamics of (Ψt) provides more ﬂexibility for modelling default
correlations in models with conditionally independent defaults (see Section 9.6.3
below).
In this section we assume that (Ψt) is the unique solution of the SDE
dΨt = µ(Ψt) dt + σ(Ψt) dWt + dZt,
Ψ0 = ψ ∈D.
(9.42)
Here (Zt) is a pure jump process whose jump intensity at time t is equal to λZ(Ψt)
for some function λZ : D →R+ and whose jump-size distribution has df ν on R.
Intuitively this means that given the trajectory (Ψt(ω))t⩾0 of the factor process,
(Zt) jumps at the jump times of an inhomogeneous Poisson process (see Section 10.2.7) with time-varying intensity λZ(t, Ψt); the size of the jumps has df ν.
SupposenowthatAssumption9.27holds,andthatλZ(ψ) = l0+l1ψ forconstants
l0, l1 such that λZ(ψ) > 0 for all ψ ∈D. In that case we say that (Ψt) follows
an afﬁne jump diffusion. For x ∈R denote by ˆν(x) =

R e−xy dν(y) ∈(0, ∞]
the extended Laplace–Stieltjes transform of ν (with domain R instead of the usual
domain [0, ∞)). Consider the following extension of the ODE system (9.36), (9.37):
β′(t, T ) = ρ1 −k1β(t, T ) −1
2h1β2(t, T ) −l1(ˆν(−β(t, T )) −1),
(9.43)
α′(t, T ) = ρ0 −k0β(t, T ) −1
2h0β2(t, T ) −l0(ˆν(−β(t, T )) −1),
(9.44)
with terminal condition β(T, T ) = u for some u ⩽0 and α(T, T ) = 0. Suppose
that the system (9.44), (9.43) has a unique solution α, β and that β(t, T )ψ ⩽C
for all t
∈[0, T ], ψ
∈D (for l0 or l1̸
= 0 this implicitly implies that
ˆν(−β(t, T )) < ∞for all t). Deﬁne ˜f (t, ψ) = exp(α(t, T ) + β(t, T )ψ). Using
similar arguments to those above, it can then be shown that the conditional expectation E(exp(−
 T
t R(Ψs) ds) exp(uΨT ) | Ft) equals ˜f (t, Ψt).
Example 9.30 (the model of Dufﬁe and Gˆarleanu (2001)). The following jumpdiffusion model has been used in the literature on CDO pricing. The dynamics of
(Ψt) are given by
dΨt = κ( ¯θ −Ψt) dt + σ

Ψt dWt + dZt
(9.45)
for parameters κ, ¯θ, σ > 0 and a jump process (Zt) with constant jump intensity
l0 > 0 and exponentially distributed jump sizes with parameter 1/µ. Following
Dufﬁe and Gˆarleanu, we will sometimes call the model (9.45) a basic afﬁne jump
diffusion. Note that these assumptions imply that the mean of ν is equal to µ and that
ν has support [0, ∞), so that (Ψt) has only upward jumps. Hence the existence of a
solution to (9.45) follows from the existence of solutions in the pure diffusion case.
It is relatively easy to show that for t →∞we obtain E(Ψt) →¯θ + l0µ/κ. For
illustrative purposes we present the parameter values used in Dufﬁe and Gˆarleanu
--- page 442 ---

426
9. Dynamic Credit Risk Models
Table 9.1.
Parameters used in the model of Dufﬁe and Gˆarleanu (2001). Recall that l0 gives
theintensityofjumpinthefactorprocess,µgivestheaveragejumpsize.Withtheseparameters
the average waiting time for a jump in the systematic factor process is 1/l0 = 5 years.
κ
¯θ
σ
l0
µ
0.6
0.02
0.14
0.2
0.1
0
0.10
0.20
0.30
Time
0
0.10
0.20
0.30
10
2
4
6
8
0
(a)
(b)
Figure 9.8.
(a) A typical trajectory of the basic afﬁne jump diffusion model (9.45) and
(b) the corresponding jumps of (Zt). The parameter values used are given in Table 9.1; the
initial value Ψ0 is equal to the long-run mean ¯θ + (l0µ)/κ marked by the horizontal line.
(2001) in Table 9.1; a typical trajectory of (Ψt) is simulated in Figure 9.8. Next we
compute the Laplace–Stieltjes transform ˆν. We obtain for u > −1/µ that
ˆν(u) =
 ∞
0
e−ux(1/µ)e−x/µ dx =
1
1 + µu;
for u ⩽−1/µ we get ˆν(u) = ∞. We therefore have all the necessary ingredients
to set up the Ricatti equations (9.44) and (9.43). In the case of the model (9.45) it
is in fact possible to solve these equations explicitly (see, for example, Chapter 11
of Dufﬁe and Singleton (2003)). However, the explicit solution is given by a very
lengthy expression, so we omit the details.
Application to recovery payments.
According to Theorem 9.23, in a model with a
doubly stochastic default time τ with risk-neutral hazard rate γ (Ψt), the price in t
of a recovery payment of size (1 −δ) at the default time τ equals
(1 −δ)E
  T
t
γ (Ψs) exp

−
 s
t
R(Ψu) du

ds
				 Ft

,
(9.46)
where again R(ψ) = r(ψ) + γ (ψ). Using the Fubini Theorem this equals
(1 −δ)
 T
t
E

γ (Ψs) exp

−
 s
t
R(Ψu) du
 				 Ft

ds.
(9.47)
Suppose now that γ (ψ) = γ 0 + γ 1ψ, that R(ψ) = ρ0 + ρ1ψ and that (Ψt)
is given by an afﬁne jump diffusion as introduced above. In that case the inner
--- page 443 ---

9.5. Afﬁne Models
427
expectation in (9.47) is given by a function F(t, s, Ψt). This function can be computed using an extension of the basic afﬁne methodology, so that (9.47) can be
computed by one-dimensional numerical integration. Deﬁne for 0 ⩽t ⩽s the
function ˜f (t, s, ψ) = exp(α(t, s) + β(t, s)ψ), where α(· , s) and β(· , s) solve the
ODEs (9.44), (9.43) with terminal condition α(s, s) = β(s, s) = 0. Denote by ˆν′(x)
the derivative of the Laplace–Stieltjes transform of ν. Then it is a straightforward
application of standard calculus to show that, modulo some integrability conditions,
F(t, s, ψ) = ˜f (t, s, ψ)(A(t, s) + B(t, s)ψ), where A(· , s) and B(· , s) solve the
following ODE system:
B′(t, s) + k1B(t, s) + h1βB(t, s) −l1ˆν′(−β)B(t, s) = 0,
(9.48)
A′(t, s) + k0B(t, s) + h0βB(t, s) −l0 ˆν′(−β)B(t, s) = 0,
(9.49)
with terminal condition A(s, s) = γ0, B(s, s) = γ1. Again, (9.48) and (9.49) are
straightforward to evaluate numerically.
Example 9.31 (defaultable zero-coupon bonds and CDS). We now have all the
necessary ingredients to compute prices and credit spreads of defaultable zerocoupon bonds and CDS spreads in a model with a doubly stochastic default time
with hazard rate γt = Ψt for a one-dimensional afﬁne jump diffusion (Ψt). In Figure 9.9 we plot the credit spread for defaultable bonds for the recovery assumptions
discussed in Section 9.4.1. Note that, for T →t, i.e. for time to maturity close to
zero, the spread tends to c(t, t) = δΨt > 0, as claimed in Section 9.4.3; in particular,
the credit spread does not vanish as T →t. This is in stark contrast to ﬁrm-value
models, where typically c(t, t) = 0, as was shown in Section 8.2.1. Note further
that, for T −t large, under the RF assumption we obtain negative credit spreads,
which is clearly unrealistic. These negative credit spreads are caused by the fact that
under RF we obtain a payment of ﬁxed size 1 −δ immediately at default. If the
default-free interest rate r is relatively large, it may happen that
EQ

exp

−
 τ
0
rs ds

(1 −δ)I{τ⩽T }

< EQ

exp

−
 T
0
rs ds

I{τ⩽T }

,
even if δ > 0. This stems from the fact that on the right-hand side discounting is
done over the whole period [0, T ] (as opposed to [0, τ]), so that discounting has a
large impact on the value of the right-hand side, compensating the higher terminal
pay-off. In Figure 9.10 we have plotted the fair spreads for CDS with and without
accrued payments for varying maturities, assuming that the risk-neutral hazard rate
follows a basic afﬁne jump diffusion.
Notes and Comments
The Feynman–Kac formula is discussed, for example, in Section 4.5 of Bj¨ork (1998),
or, at a slightly more technical level, in Section 5.7 of Karatzas and Shreve (1988).
Important original papers on afﬁne models in term structure modelling are Dufﬁe
and Kan (1996) for diffusion models and Dufﬁe, Pan and Singleton (2000) for jump
diffusions. The latter paper also contains other applications of afﬁne models, such
--- page 444 ---

428
9. Dynamic Credit Risk Models
Time to maturity
Credit spread (%)
10
15
20
0
0
1
2
3
4
5
5
6
7
Zero recovery
RM
RF
RT
Figure 9.9.
Spreads of corporate zero-coupon bonds in the Dufﬁe–Gˆarleanu model (9.45)
for various recovery assumptions. The parameters of (Ψt) are given in Table 9.1; the initial
value is Ψ0 ≈0.0533. The risk-free interest rate and the loss given default are deterministic
and are given by r = 6% and δ = 0.5. Note that under the RT recovery model, the spread
becomes negative for large times to maturity.
Time to maturity
Fair spread (%)
10
15
20
2.4
2.5
2.6
2.7
2.8
No accrued payments
Accrued payments
0
5
Figure 9.10.
Fair CDS spreads in the Dufﬁe–Gˆarleanu model (9.45) for a CDS contract
with semiannual premium payments and varying time to maturity. The parameters of (Ψt)
are given in Table 9.1; the initial value is Ψ0 ≈0.0533. The risk-free interest rate and the loss
given default are deterministic and are given by r = 6% and δ = 0.5. Note that, for small
time to maturity, the fair swap spread is approximately equal to δΨ0 ≈2.7%.
as the pricing of equity options under stochastic volatility and econometric issues
related to afﬁne models. It should be mentioned that there is also a converse to
Proposition 9.28: if the conditional expectations E(exp(−
 T
t R(Ψs) ds)euΨT | Ft)
are all exponentially afﬁne functions of Ψt, the process (Ψt) is necessarily afﬁne
(see Dufﬁe and Kan (1996) and in particular Dufﬁe, Filipovic and Schachermayer
(2003) for details).
The mathematical properties of the CIR model are discussed in, for example,
Chapter 6.2 of Lamberton and Lapeyre (1996), where the explicit solution (9.39)
and (9.40) of the Ricatti equations in the CIR model is also derived. The model
studied in Example 9.29 is akin to models proposed by Dufﬁe and Singleton (1999a).
Problems related to the modelling of negative correlation between state variable
--- page 445 ---

9.6. Conditionally Independent Defaults
429
process in an afﬁne setting are discussed in Section 5.8 of Lando (2004). It is possible
to compute the conditional expectation (9.46) for the price of a recovery payment
as the solution of a parabolic PDE, which stems from the Feynman–Kac formula
(see, for example, Lando 1998 for details). Empirical work on afﬁne models for
defaultable bonds includes the publications of Duffee (1999) and Driessen (2005).
9.6
Conditionally Independent Defaults
We begin our analysis of reduced-form models for portfolio credit risk with a brief
overview of the existing model classes.
9.6.1
Reduced-Form Models for Portfolio Credit Risk
The simplest reduced-form models for portfolio credit risk are models with conditionally independent defaults. In this class default times are independent given the
realization of some observable economic background process; hence these models are an extension of the static Bernoulli mixture models of Section 8.4. More
sophisticated models for dependent defaults include copula models and models
with interacting intensities. Copula models have become popular in practice and we
give an in-depth discussion of this model class in Sections 9.7 and 9.8; models with
interacting intensities are discussed in Section 9.8.3.
The common feature of the latter two model classes, as opposed to models with
conditionally independent defaults, is the presence of default contagion and counterparty risk. Loosely speaking, this means that the conditional default probability of
a non-defaulted ﬁrm jumps (usually upwards) given the additional information that
some other ﬁrm has defaulted. As a consequence the credit spread of bonds issued
by a non-defaulted ﬁrm increases given the news that some other ﬁrm has defaulted.
Mathematically, default contagion is reﬂected in jumps in the martingale default
intensity of non-defaulted ﬁrms at the default times of other ﬁrms in the portfolio.
The impact of the default of some ﬁrm on the conditional default probability of other
ﬁrms can arise via different channels. On the one hand it might be due to direct
economic links between ﬁrms, such as a close business relationship or a strong
borrower–lender relationship. For instance, the default probability of a corporate
bank is likely to increase if one of its major borrowers defaults. This direct channel
of default interaction is termed counterparty risk. On the other hand, changes in the
conditional default probability of non-defaulted ﬁrms can be caused by information
effects: investors might revise their estimate of the ﬁnancial health of non-defaulted
ﬁrms in light of the news that a particular ﬁrm has defaulted. In that case one speaks
of information-based default contagion.
A lot of recent research deals with the modelling of counterparty risk and default
contagion for a number of reasons. First, there is substantial empirical evidence for
interaction between default events. A recent example is provided by the downfall
of the energy giant Enron in autumn 2001: the news that Enron had used illegal
accounting practices led to rising credit spreads for many other corporations as
bond investors lost conﬁdence in the accounting statements of these corporations—
a striking example of default contagion. Moreover, the stock price of major lenders
--- page 446 ---

430
9. Dynamic Credit Risk Models
to Enron fell in anticipation of large losses on these loans, reﬂecting counterparty
risk. Formal empirical evidence for interaction between default events is listed in
Notes and Comments. A second reason for modelling default contagion is that
this might help to explain the clustering of defaults around economic recessions
observed in real data. However, this is not to say that models with conditionally
independent defaults are of little interest. Yu (2005a) shows that the low default
correlations in models with conditionally independent defaults may be related more
closely to an unsatisfactory modelling of state variables than to a problem of the
approach per se. We will discuss this issue in more detail in Section 9.6.3 below.
On a related note, not every default of a major corporation leads to changes in the
credit spreads of the remaining ﬁrms, so conditional independence is often realistic.
Moreover, more sophisticated models of default dependence may be hard to calibrate
in practice, particularly for large portfolios. In any case, the discussion of models
with conditionally independent defaults will provide a methodological basis for
studying more complicated models.
Notation.
In keeping with Section 9.1, we use the following notation for our analysisofdynamicportfoliocreditriskmodels.Weconsideraportfolioofmobligorswith
default times τi and default indicator processes Yt,i = Yi(t) = I{τi⩽t}, 1 ⩽i ⩽m,
on some generic probability space (Ω, F , P), where the interpretation of P (physical measure or equivalent martingale measure) will depend on the context. (Note
that we switch freely between the notation Xt,i and the notation Xi(t) for generic
processes deﬁned at the level of individual obligors; generally we favour Xt,i for
stochastic processes and Xi(t) for deterministic ones, but we also depart from this
for reasons of notational elegance in individual formulas.)
In dynamic portfolio credit risk models it is convenient to consider survival
functions instead of distribution functions. As usual, ¯Fi(t) = P(τi > t) denotes
the tail or survival function of obligor i; the joint survival function is denoted
by ¯F(t1, . . . , tm) = P(τ1 > t1, . . . , τm > tm). Throughout our analysis we restrict
ourselves to models without simultaneous defaults. We may therefore denote the
ordered default times by T0 < T1 < · · · < Tm, where T0 = 0 and, for 1 ⩽n ⩽m,
Tn = min{τi : τi > Tn−1, 1 ⩽i ⩽m}. By ξn ∈{1, . . . , m} we denote the identity
of the ﬁrm defaulting at time Tn. Finally,
An = {1 ⩽i ⩽m : Yi(Tn) = 0} = {1, . . . , m} \ {ξ1, . . . , ξn}
is the set of non-defaulted ﬁrms immediately after time Tn.
As in the previous sections, (Ft) represents our background ﬁltration, typically
generated by some observable process (Ψt) representing economic factors. Moreover, we introduce the ﬁltrations {Hi
t }, 1 ⩽i ⩽m, (Ht) and (Gt) by
Hi
t = σ({Ys,i : s ⩽t}),
Ht = Hi
t ∨· · · ∨Hm
t
and
Gt = Ft ∨Ht. (9.50)
{Hi
t } is the ﬁltration generated by default observation for obligor i alone; (Ht) is
the ﬁltration generated by default observation for all obligors; (Gt) contains default
information for all obligors and observable background information and thus represents the information available to investors at time t. Often (Ht) is called the
internal ﬁltration generated by the default times τi, 1 ⩽i ⩽m.
--- page 447 ---

9.6. Conditionally Independent Defaults
431
9.6.2
Conditionally Independent Default Times
In this section we discuss general mathematical properties of models with conditionally independent defaults; speciﬁc examples from the literature are considered
in the next section. We start with a formal deﬁnition of conditionally independent
default times.
Deﬁnition 9.32. Given a probability space (Ω, F , P) with background ﬁltration
(Ft) and random times τ1, . . . , τm, the τi are conditionally independent doubly
stochastic random times if
(i) each of the τi is a doubly stochastic random time in the sense of Deﬁnition 9.11 with background ﬁltration (Ft) and (Ft)-conditional hazard-rate
process (γt,i); and
(ii) the rvs τ1, . . . , τm are conditionally independent given F∞, i.e. we have, for
all t1, . . . , tm > 0,
P(τ1 ⩽t1, . . . , τm ⩽tm | F∞) =
m
!
i=1
P(τi ⩽ti | F∞).
(9.51)
Construction and simulation via thresholds.
The lemma that follows extends
Lemma 9.12.
Lemma 9.33. Let (γt,1), . . . , (γt,m) be positive, (Ft)-adapted processes such
that Γt,i :=
 t
0 γs,i ds is strictly increasing and ﬁnite for any t > 0. Let E =
(E1, . . . , Em)′ be a vector of independent, standard exponentially distributed rvs
independent of F∞. Deﬁne τi by τi = Γ −1
i
(Ei). Then τ1, . . . , τm are conditionally
independent doubly stochastic random times.
Proof. According to Lemma 9.12, each of the τi is a doubly stochastic random time
with (Ft)-hazard-rate process (γt,i). It remains to verify the conditional independence. Using the fact that τi ⩽t ⇐⇒Ei ⩽Γt,i, we have
P(τ1 ⩽t1, . . . , τm ⩽tm | F∞) = P(E1 ⩽Γt1,1, . . . , Em ⩽Γtm,m | F∞)
=
m
!
i=1
P(Ei ⩽Γti,i | F∞)
=
m
!
i=1
P(τi ⩽ti | F∞).
(9.52)
Note that (9.52) holds since the rvs Γti,i are measurable with respect to F∞, whereas
the Ei are mutually independent and independent of F∞.
Lemma 9.33 is the basis for the following simulation algorithm.
--- page 448 ---

432
9. Dynamic Credit Risk Models
Algorithm 9.34 (multivariate threshold simulation).
(1) Generateatrajectoryofthehazard-rateprocesses(γt,i)fori = 1, . . . , m.Here
the same techniques as in the univariate case can be used; note, however,
that for a high-dimensional factor vector this step can become quite timeconsuming.
(2) Generate a vector E of independent standard exponentially distributed rvs
(the threshold vector) and set τi = Γ −1
i
(Ei), 1 ⩽i ⩽m.
As in the univariate case, Lemma 9.33 has a converse, which we state without the
simple proof.
Lemma 9.35. Let τ1, . . . , τm be conditionally independent doubly stochastic random times with (Ft)-hazard-rate processes (γt,i). Deﬁne a random vector E by
Ei = Γi(τi), 1 ⩽i ⩽m. Then E is a vector of independent, standard exponentially
distributed rvs that is independent of F∞, and τi = Γ −1
i
(Ei) almost surely.
Recursive default time simulation.
We now describe a second recursive algorithm
for simulating conditionally independent default times, which is sometimes more
efﬁcient than multivariate threshold simulation. Moreover, the algorithm generalizes
naturally to reduced-form models with interacting intensities (see Section 9.8.3).We
need the following lemma, which gives properties of the ﬁrst default time T1.
Lemma 9.36. Let τ1, . . . , τm be conditionally independent doubly stochastic randomtimeswithhazard-rateprocesses(γt,1), . . . , (γt,m).ThenT1 isadoublystochastic random time with (Ft)-conditional hazard-rate process ¯γt := m
i=1 γt,i, t ⩾0.
Proof. Using the conditional independence of the τi we get
P(T1 > t | F∞) = P(τ1 > t, . . . , τm > t | F∞) =
m
!
i=1
exp

−
 t
0
γs,i ds

,
which is obviously equal to exp(−
 t
0 ¯γs ds). As this expression is Ft-measurable,
the result follows.
Next we compute the conditional probability of the event {ξ1 = i} given the ﬁrst
default time T1 and full information about the background ﬁltration.
Proposition 9.37. Under the assumptions of Lemma 9.36 we have
P(ξ1 = i | F∞∨σ(T1)) = γi(T1)/ ¯γ (T1),
i ∈{1, . . . , m}.
Proof. Conditional on F∞the τi are independent with deterministic hazard rate
γi(t), so it is enough to prove the proposition for independent random times with
deterministic hazard rate. Fix some t > 0 and note that the probability of having
more than one default in the interval (t −h, t] is of order o(h), as the random vector
(τ1, . . . , τm) has a joint density. Hence
P({ξ1 = i} ∩{T1 ∈(t −h, t]}) = P({τi ∈(t −h, t]} ∩{τj > t, j̸ = i}) + o(h)
= P(τi ∈(t −h, t])
!
j̸=i
P(τj > t)
--- page 449 ---

9.6. Conditionally Independent Defaults
433
by the independence of the τi. Since P(τi > t) = exp(−
 t
0 γi(s) ds), 1 ⩽i ⩽m,
this equals
exp

−
 t−h
0
γi(s) ds

1 −exp

−
 t
t−h
γi(s) ds

×
!
j̸=i
exp

−
 t
0
γj(s) ds

+ o(h).
Hence we get
lim
h→0+ h−1P({ξ1 = i} ∩{T1 ∈(t −h, t]}) = γi(t) exp

−
 t
0
¯γ (s) ds

.
Moreover, by Lemma 9.36,
lim
h→0+ h−1P(T1 ∈(t −h, t]) =
¯
γ (t) exp

−
 t
0
¯γ (s) ds

,
so the claim follows from the deﬁnition of elementary conditional expectation and
L’Hˆopital’s rule.
Algorithm 9.38 (recursive default time simulation). This algorithm simulates a
realization of the sequence (Tn, ξn) up to some maturity date T . Recall that for
n ⩾1 the set of non-defaulted ﬁrms immediately after Tn is denoted by An and
set A0 := {1, . . . , m}. Deﬁne ¯γ n
t := 
i∈An γt,i, 0 ⩽n ⩽m. Then the algorithm
proceeds in the following steps.
(1) Generate a trajectory of the hazard-rate processes (γt,i).
(2) Generate T1 by standard univariate threshold simulation, using the fact that
T1 has hazard rate ( ¯γ 0
t ) by Lemma 9.36.
(3) Determineξ1 asarealizationofanrvξ withP(ξ = i) = γi(T1)/ ¯γ 0(T1)(using
Proposition 9.37).
(4) If T1 ⩾T stop. Otherwise note that, for conditionally independent defaults,
P(T2 −T1 > t | T1, ξ1, F∞) = P(τj > T1 + t, j ∈A1, | T1, ξ1, F∞)
P(τj > T1, j ∈A1, | T1, ξ1, F∞)
= exp

−
 T1+t
T1
¯γ 1
s ds

.
(9.53)
Generate the waiting time T2 −T1 via univariate threshold simulation using
(9.53); determine ξ2 as before, using the fact that, for i ∈A1,
P(ξ2 = i | T1, T2, ξ1, F∞) = γi(T2)/ ¯γ 1(T2).
(5) Proceed in this way until Tn ⩾T for some n ⩽m or until all ﬁrms have
defaulted.
--- page 450 ---

434
9. Dynamic Credit Risk Models
Recursive default time simulation is particularly efﬁcient if we want to simulate
only defaults occurring before some maturity date T and if defaults are rare. In that
case, typically Tn > T already for n relatively small, so only a few ordered default
times need to be simulated. With multivariate threshold simulation, on the other
hand, we need to simulate the default times of all obligors in the portfolio.
Martingale intensities.
The following proposition shows that, for conditionally
independent defaults, martingale intensities and hazard rates coincide.
Proposition 9.39. Let τ1, . . . , τm be conditionally independent doubly stochastic random times with hazard-rate processes (γt,1), . . . , (γt,m). Then the process
Mt,i := Yt,i −
 t∧τi
0
γs,i ds is a (Gt)-martingale with (Gt) as in (9.50).
Proof. We know from Proposition 9.15 that (Mt,i) is a martingale with respect to
the ﬁltration {Gi
t} with Gi
t = Ft ∨Hi
t , i.e. that E(Ms,i | Gi
t) = Mt,i, s > t.
However, this does not automatically imply that (Mt,i) is also a (Gt)-martingale, as
Gi
t ⊂Gt, and so we could have E(Ms,i | Gt)̸ = E(Ms,i | Gi
t). In fact, this typically
happens in copula models (see Section 9.8.1 below). In the present situation the
conditionalindependenceoftheτi permitsustoovercomethisdifﬁculty.Thisisquite
intuitive: since the τi are conditionally independent, default information for obligor
j̸ = i is of no use in predicting the default of obligor i. A formal argument is as
follows. Using Lemma 9.35, we may assume that there is a vector E of independent,
standard exponential rvs, independent of F∞, such that for all 1 ⩽j ⩽m we have
τj = Γ −1
j
(Ej). Obviously, τi is independent of Ej for j̸ = i, so
E(Ms,i | Gi
t ∨σ({Ej : j̸ = i})) = E(Ms,i | Gi
t) = Mt,i.
(9.54)
On the other hand, if we know Ej and the trajectory (γu,j)0⩽u⩽t, we can determine
Yu,j for 0 ⩽u ⩽t. Hence Gt = Ft ∨H1
t ∨· · · ∨Hm
t is a subset of Gi
t ∨σ({Ej :
j̸ = i}), so (9.54) implies that E(Ms,i | Gt) = Mt,i, as required.
Remark 9.40 (pricing of single-name credit products). Suppose that τ1, . . . , τm
are conditionally independent doubly stochastic random times. Consider a singlename credit product with maturity T whose pay-off H depends only on the default
history of ﬁrm i and on the evolution of default-free security prices and is thus Gi
T -
measurable. A typical example is a vulnerable claim of the form H = I{τi>T }X for
an FT -measurable rv X. A similar argument to that in the proof of Proposition 9.39
shows that
EQ

exp

−
 T
t
rs ds

H
				 Gi
t

= EQ

exp

−
 T
t
rs ds

H
				 Gt

,
t ⩽T,
where (rt) is the Ft-adapted default-free short rate. Now, the left-hand side of the
above equation gives the price of the claim H in a single-ﬁrm model where the
information available to investors at time t is given by Gi
t, whereas the right-hand
side gives the price of H in the portfolio model where at time t investors have
access to the larger information set Gt containing default information on all ﬁrms
in the portfolio. Hence pricing formulas for single-name credit products obtained
--- page 451 ---

9.6. Conditionally Independent Defaults
435
in a single-ﬁrm model with a doubly stochastic default time, such as the pricing
formulas from Theorem 9.23, remain valid in a portfolio model with conditionally
independent default times. If we go beyond conditional independence this is no
longer true, as will be discussed in Section 9.8.1.
9.6.3
Examples and Applications
In most models with conditionally independent defaults, hazard rates are modelled
as linear combinations of independent afﬁne diffusions, possibly with jumps. A
typical model is as follows:
γt,i = γi0 +
p

j=1
γijΨ syst
t,j + Ψ id
t,i,
1 ⩽i ⩽m.
(9.55)
Here (Ψ syst
t,j ), 1 ⩽j ⩽p, and (Ψ id
t,i), 1 ⩽i ⩽m, are independent CIR square-root
diffusions or, slightly more generally, basic afﬁne jump diffusions as in (9.45); the
factor weights γij, 0 ⩽j ⩽p, are non-negative constants. Obviously, (Ψ syst
t
) represents the common or systematic factors, whereas (Ψ id
t,i) is an idiosyncratic factor
process affecting only the hazard rate of obligor i. Note that the weight of the
idiosyncratic factor can be incorporated into the parameters of the dynamics of
(Ψ id
t ), so we do not need an extra factor weight. Throughout this section we assume
that the background ﬁltration is generated by (Ψ syst
t
) and (Ψ id
t,i), 1 ⩽i ⩽m. In
practical applications of the model, the current value of these processes is derived
from observed prices of defaultable bonds.
We now present a few examples proposed in the literature. Duffee (1999) has estimated a model of the form (9.55) with p = 2; in his model all factor processes are
assumed to follow CIR square-root diffusions, so that their dynamics are characterized by the parameter triplet (κ, ¯θ, σ). In Duffee’s model, (Ψ syst
t
) represents factors
driving the default-free short rate; the parameters of these processes are estimated
from treasury data. The factor weights γij and the parameters of (Ψ id
t ), on the other
hand, are estimated from corporate bond-price data.
In their inﬂuential case study on CDO pricing, Dufﬁe and Gˆarleanu (2001) use
basic afﬁne jump diffusion processes of the form (9.45) to model the factors driving
the hazard rates. Jumps in (γt) represent shocks which increase the default probability of a ﬁrm. They consider a homogeneous model with one systematic factor,
i.e. γt,i = Ψ syst
t
+ Ψ id
t,i, 1 ⩽i ⩽m, and assume that the speed of mean-reversion κ,
the volatility σ and the mean jump size µ are identical for (Ψ syst
t
) and (Ψ id
t,i). It is
straightforward to show that this implies that the sum γt,i = Ψ syst
t
+ Ψ id
t,i follows a
basic afﬁne jump diffusion with parameters κ, ¯θsyst + ¯θid, σ, (l0)syst + (l0)id and µ;
the parameters of (γt,i) used in Dufﬁe and Gˆarleanu (2001) can be found in the row
labelled “base case” in Table 9.2.
Pricing single-name credit products.
As discussed in Remark 9.40, with conditionally independent defaults, pricing formulas obtained in a single-ﬁrm model remain
valid in the portfolio context. Moreover, with hazard rates as in (9.55) most actual
computations can be reduced to a one-dimensional problem involving afﬁne processes, to which the results of Section 9.5 apply. As a simple speciﬁc example we
--- page 452 ---

436
9. Dynamic Credit Risk Models
Table 9.2.
Parameter sets of the Dufﬁe–Gˆarleanu model used in Figure 9.11.
Parameter set
κ
¯θ
σ
l0
µ
Pure diffusion
0.6
0.0505
0.141
0
0
Base case
0.6
0.02
0.141
0.2
0.1
High jump intensity
0.6
0.0018
0.141
0.32
0.1
consider the computation of the conditional survival probability of obligor i. We
obtain from Remark 9.40 and Theorem 9.23 that
P(τi > T | Gt) = P(τi > T | Gi
t) = I{τi>t}E

exp

−
 T
t
γs,i ds
 				 Ft

.
For hazard-rate processes of the form (9.55) this equals
I{τi>t}e−γi0(T −t)E

exp

−
 T
t
Ψ id
s,i ds
 				 Ft

×
p
!
j=1
E

exp

−
 T
t
Ψ syst
s,j ds
 				 Ft

.
(9.56)
Each of the conditional expectations in (9.56) can now be computed using the results
on one-dimensional afﬁne models from Section 9.5. More general models, where
hazard rates are given by a general multivariate afﬁne process (and not simply by a
linear combination of independent one-dimensional afﬁne processes) can be dealt
with using the general afﬁne-model technology from Dufﬁe, Pan and Singleton
(2000).
Static version of the model.
It is interesting to look at the implications of conditional independence and the factor structure (9.55) of the hazard rates for the distribution of the default indicators at a given point in time T , as this links our analysis
to the static models of Chapter 8. For simplicity we suppose that the idiosyncratic
factor (Ψ id
t,i) vanishes for all ﬁrms. Fix some T > 0 and consider the random vector
YT = (YT,1, . . . , YT,m)′. We get, for y ∈{0, 1}m,
P(YT = y) = E(P(YT = y | F∞))
= E
 !
j:yj =1
P(τj ⩽T | F∞)
!
j:yj =0
P(τj > T | F∞)

.
Now we obviously have, using (9.55),
P(τi ⩽T | F∞) = 1 −exp

−γi0T −
p

j=1
γij
 T
0
Ψ syst
s,j ds

.
(9.57)
This shows that YT follows a Bernoulli mixture model with p-factor structure as in
Deﬁnition 8.10 with factor vector given by
Ψ :=
  T
0
Ψ syst
s,1 ds, . . . ,
 T
0
Ψ syst
s,p ds
′
and conditional default probabilities pi(Ψ ) as in (9.57).
--- page 453 ---

9.6. Conditionally Independent Defaults
437
Default correlation.
As we have seen in Chapter 8, default correlations (deﬁned
as correlation ρ(YT,i, YT,j), i̸ = j, of the default indicators) are crucial for the
tail of the credit loss distribution. In computing default correlations in models
with conditionally independent defaults it is more convenient to work with the
survival indicator 1 −YT,i. By the deﬁnition of standard linear correlation we
have
ρ(YT,i, YT,j) = ρ(1 −YT,i, 1 −YT,j)
=
P(τi > T, τj > T ) −¯Fi(T ) ¯Fj(T )
( ¯Fi(T )(1 −¯Fi(T )))1/2( ¯Fj(T )(1 −¯Fj(T )))1/2 .
(9.58)
For models with hazard rates as in (9.55), the computation of the survival probabilities ¯Fi(T ) using afﬁne-model technology has been discussed above. For the joint
survival probability we obtain, using conditional independence,
P(τi > T, τj > T ) = E(P(τi > T, τj > T | F∞))
= E(P(τi > T | F∞)P(τj > T | F∞))
= E

exp

−
 T
0
(γs,i + γs,j) ds

.
(9.59)
For hazard rates of the form (9.55), expression (9.59) can be decomposed in a similar
way to the decomposition in (9.56) and can thus be evaluated using our results on
one-dimensional afﬁne models.
It is often claimed that the default correlation values that can be attained in models
with conditionally independent defaults are too low compared with empirical default
correlations (see, for example, Hull and White 2001; Sch¨onbucher and Schubert
2001). Since default correlations do have a signiﬁcant impact on the loss distribution
generated by a model, we discuss this issue further. As a concrete example we use
the Dufﬁe–Gˆarleanu model and assume that (Ψ id
t ) vanishes. As discussed above, in
that case the default indicator vector YT follows an exchangeable Bernoulli mixture
model with mixing variable ˜Q given by 1 −exp(−
 T
0 Ψ syst
s
ds).
We have seen in Section 8.4.1 that in exchangeable Bernoulli mixture models
every default correlation ρ ∈(0, 1) can be obtained by choosing the variance
of the mixing variable sufﬁciently high. It follows that in the Dufﬁe–Gˆarleanu
model high levels of default correlation can be obtained if the variance of the rv
ΓT :=
 T
0 Ψ syst
s
ds is sufﬁciently high. A high variance of ΓT can be obtained by
choosing a high value for the volatility σ of the diffusion part of (Ψ syst
t
) or by
choosing a high value for the mean of the jump-size distribution µ or for the jump
intensity l0. A high value for σ translates into very volatile day-to-day ﬂuctuations
of credit spreads, which might contradict the behaviour of real bond-price data. This
shows that it might be difﬁcult to generate very high levels of default correlation
in models where hazard rates follow pure diffusion processes (see, however, Yu
(2005a) for an alternative view).
In the Dufﬁe–Gˆarleanu model we may alternatively raise the frequency or size
of the jumps in the hazard rate by increasing l0 or µ. This is a very effective
--- page 454 ---

438
9. Dynamic Credit Risk Models
Correlation (%)
10
15
20
Pure diffusion
Base case
High intensity
Time to maturity
0.4
0.6
0.8
1.0
0
10
0
2
4
6
8
Probability
5
(a)
(b)
Figure 9.11.
(a) Default correlations for varying time to maturity and three different parameter sets in the Dufﬁe–Gˆarleanu model for (Ψ id
t ) ≡0 and different parameter sets for (Ψ syst
t
).
The parameters of (Ψ syst
t
) are given in Table 9.2. We see that by increasing the intensity of
jumps in (Zt) the default correlation is increased substantially. (b) The survival probabilities
for the three parameter sets are essentially equal, so that the differences in default correlations
are solely due to the impact of the dynamics of (Ψ syst
t
) on the dependence structure of the
default times.
mechanism for generating default correlation, as is shown in Figure 9.11. In fact,
this additional ﬂexibility in modelling default correlations is an important motivation for considering afﬁne jump diffusions instead of the simpler CIR diffusion
models.
These qualitative ﬁndings obviously carry over to other models with conditionally
independent defaults. Summing up, we conclude that it is certainly possible to
generate high levels of default correlation in models with conditionally independent
defaults; however, the required models for the hazard-rate processes may become
relatively complex.
First-to-default swaps.
As a ﬁnal application we study the pricing of ﬁrst-todefault swaps in models with conditionally independent defaults. We consider a
portfolio of m ﬁrms. Premium payments on the swap are due at N points in time
0 < t1 < · · · < tN =: T . Provided that T1 > tn, the premium at time tn is of the
form x(tn −tn−1); at T1 premium payments stop. For simplicity we neglect accrued
premium payments. The default payment occurs at time T1 provided T1 < T . We
assume that the payment depends on the identity ξ1 of the ﬁrst defaulting ﬁrm (perhaps because of differing exposure sizes) but is otherwise deterministic, i.e. there
are constants l1, . . . , lm such that the default payment is equal to li if T1 < T
and ξ1 = i. As usual, the fair spread x∗of the swap is the value of x such
that at t = 0 the default payment leg and premium payment leg have the same
value.
Since, in practice, ﬁrst-to-default swaps are always priced relative to traded singlename CDSs, it is natural to adopt the martingale-modelling approach. We assume
that under the equivalent martingale measure Q the default times τi are conditionally
independent doubly stochastic random times with hazard rates of the form (9.55);
moreover, the risk-free short rate (rt) is assumed to be of the form (9.55). In this
--- page 455 ---

9.6. Conditionally Independent Defaults
439
set-up, for generic swap spread x the value of the premium payment equals
V prem =
N

n=1
EQ

exp

−
 tn
0
rs ds

I{T1>tn}

x(tn −tn−1).
(9.60)
Using Theorem 9.23 and Lemma 9.36 we get
EQ

exp

−
 tn
0
rs ds

I{T1>tn}

= EQ

exp

−
 tn
0
(rs +
m

i=1
γs,i) ds

.
For hazard rates and a risk-free short rate of the form (9.55) this can be expressed
as a product of expectations of the form EQ(exp(−C
 tn
0 Ψs ds)) for a constant C
and a one-dimensional afﬁne jump diffusion (Ψt), so the premium payments can be
computed using the methods developed in Section 9.5. Next we turn to the default
payments. We have
V def =
m

i=1
liEQ

exp

−
 T1
0
rs ds

I{T1⩽T }I{ξ1=i}

.
We begin by computing
EQ

exp

−
 T1
0
rs ds

I{T1⩽T }I{ξ1=i}
				 F∞

.
Conditioning on T1 we obtain that this equals
 T
0
exp

−
 t
0
r(s) ds

Q(ξ1 = i | T1 = t, F∞)f Q
T1|F∞(t) dt,
(9.61)
where f Q
T1|F∞(t) is the Q-density of T1 given F∞. By Lemma 9.36,
f Q
T1|F∞(t) = ¯γ (t) exp

−
 t
0
¯γ (s) ds

.
Moreover, by Proposition 9.37,
Q(ξ1 = i | T1 = t, F∞) = γi(t)/ ¯γ (t).
Hence (9.61) equals
 T
0 γi(t) exp(−
 t
0(r(s) + ¯γ (s)) ds) dt. To compute the value
of V def we thus have to compute EQ(
 T
0 γt,i exp(−
 t
0 rs + ¯γs ds) dt). For hazard
rates of the form (9.55) this can be evaluated using the extended transform discussed
in Section 9.5.3; we omit the details. If the default payments li are all identical, the
ﬁrst-to-default swap can be priced like a single-name CDS, with the hazard rate of
the default time given by ( ¯γt); this follows immediately from Lemma 9.36.
In certain special cases higher-order default swaps can be evaluated analytically.
However, in most cases that are practically relevant, one has to use Monte Carlo
simulation, and the recursive default time simulation algorithm from the previous
section comes in handy.
--- page 456 ---

440
9. Dynamic Credit Risk Models
Notes and Comments
The empirical literature on default contagion and counterparty risk has two different
strands. On the one hand, there are papers such as Collin-Dufresne, Goldstein and
Helwege (2003) or Lang and Stulz (1992) which focus on the impact of defaults or
credit-spread widenings of a given ﬁrm on the credit spreads or stock returns of other
ﬁrms and hence on default contagion under a risk-neutral measure. For instance,
Collin-Dufresne, Goldstein and Helwege (2003) found that, even after controlling
for other macroeconomic variables inﬂuencing bond returns, the return of large
corporate bond indices in months where one or several large ﬁrms experienced a
signiﬁcant (above 200 basis points) widening in credit spreads is signiﬁcantly lower
than the return of these indices in other months; this is clear evidence supporting
contagion. Das, Dufﬁe and Kapadia (2005) and Jarrow and Yu (2001), on the other
hand, look at default contagion under the physical measure. Jarrow and Yu provide
a lot of anecdotal evidence for counterparty risk in small portfolios. Das, Dufﬁe
and Kapadia formally test whether models with conditionally independent defaults
driven by observable macroeconomic factors are sufﬁcient to explain the degree of
clustering one ﬁnds in actual default data for large portfolios (their default database
contains approximately 2000 ﬁrms). In their words, they “do not ﬁnd substantial
evidence of default clustering beyond that predicted by the doubly stochastic model
in their data”. These ﬁndings are only preliminary, but indicate nonetheless that
default contagion is relevant for the pricing and the hedging of portfolio-related
credit derivatives; for credit risk management issues, on the other hand, a model
with conditionally independent defaults and appropriately speciﬁed factors might
be sufﬁcient.
TheresultsofSection9.6.2arewellknown;foranalternativetreatmentattextbook
level, see, for example, Chapter 9 of Bielecki and Rutkowski (2002). The simulation
of conditionally independent default times is discussed in Dufﬁe and Singleton
(1999b) (see also Dufﬁe and Singleton 2003). Further empirical work on afﬁne
models for credit portfolios includes that of Duffee (1999) and Driessen (2005).
Default correlations in models with conditionally independent defaults are discussed
in Yu (2005a).
9.7
Copula Models
Copula models are widely used in practice for the pricing of basket credit derivatives
andCDOstructures.Theyareeasytocalibratetoagiventermstructureofdefaultable
bonds or CDS spreads; moreover, they can be used to model default contagion.
In this section we introduce theses models; particular attention will be given to
models where the copula has a factor structure, since these models have a convenient
representation as mixture models. Dynamic properties of copula models and default
contagion are studied in Section 9.8 below.
9.7.1
Deﬁnition and General Properties
To motivate our deﬁnition of copula models we return brieﬂy to models with
conditionally independent defaults. According to Lemma 9.35, if τ1, . . . , τm are
--- page 457 ---

9.7. Copula Models
441
conditionally independent doubly stochastic random times with (Ft)-adapted
hazard-rate processes (γt,1), . . . , (γt,m), we can ﬁnd a random vector E with independent, unit exponentially distributed components, independent of F∞, such that
τi = inf{t ⩾0 : Γt,i ⩾Ei}. We may rewrite this as
τi = inf{t ⩾0 : 1 −exp(−Γt,i) ⩾˜Ui := 1 −exp(−Ei)}.
(9.62)
Note that ˜U = ( ˜U1, . . . , ˜Um)′ is a vector of m independent rvs with uniform margins,
so that its joint df is the m-dimensional independence copula (see Section 5.1.2).
In the copula models we generalize this construction and replace the independence
copula with some other copula; obviously, this allows for a richer dependence structure of the τi than in the case of conditionally independent default times. Deﬁning
Ui := 1 −˜Ui we may rewrite (9.62) as τi = inf{t ⩾0 : exp(−Γt,i) ⩽Ui}. To be
in line with the literature we work with this description of the τi and deﬁne copula
models in terms of the copula C of U (or equivalently the survival copula ˆC of ˜U
introduced in Section 5.1.5). We call C the conditional survival copula of the ﬁrms;
this terminology will be justiﬁed below.
Deﬁnition 9.41 (copula model for default times). Let (γt,i), . . . , (γt,m) be nonnegative, (Ft)-adapted processes such that Γt,i < ∞for all t > 0, and let C be an
m-dimensional copula. Then the random times τ1, . . . , τm follow a copula model
with marginal hazard-rate processes (γt,i), i = 1, . . . , m, and conditional survival
copula C, if there is an m-dimensional random vector U ∼C, independent of F∞,
such that
τi = inf{t ⩾0 : exp(−Γt,i) ⩽Ui},
1 ⩽i ⩽m.
(9.63)
Note that Deﬁnition 9.41 provides an obvious way to simulate a copula model of
default, provided we know how to simulate the copula C. To simulate a realization of
τ1, . . . , τm we generate a realization of the hazard-rate processes (γt,1), . . . , (γt,m)
and, independently, a realization of the random vector U; the τi are then constructed
according to (9.63).
The crucial part in setting up a copula model is the choice of the threshold copula C. Useful copulas and the resulting copula models will be discussed in the next
subsection; for the moment we merely recall that we obtain conditionally independent default times if and only if we take C to be the independence copula.
We now collect some elementary consequences of Deﬁnition 9.41. Since Ei :=
−ln(1 −Ui) ∼Exp(1), Lemma 9.12, together with (9.63), immediately yields that
each of the τi is a doubly stochastic random time with (Ft)-conditional hazard-rate
process (γt,i). Hence Mt,i := Yt,i −Γi(t ∧τi) is a martingale with respect to the
ﬁltration {Gi
t} := (Ft) ∨{Hi
t }. Unless C is the independence copula, it is, however,
not true that Mt,i is also a martingale with respect to the ﬁltration (Gt), i.e. given
default information for other obligors as well (see Section 9.8.1 for details).
At time t = 0 the marginal distribution of the τi can be computed as in the
single-ﬁrm case. We have, using iterated conditional expectations,
P(τi ⩽T ) = E(P(τi ⩽T | F∞)) = 1 −E

exp

−
 T
0
γs,i ds

.
(9.64)
