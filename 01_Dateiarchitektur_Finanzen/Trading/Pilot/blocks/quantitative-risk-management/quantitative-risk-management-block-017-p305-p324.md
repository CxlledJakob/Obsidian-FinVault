# Quantitative Risk Management_ Concepts, Techniques, and -- Alexander J_ McNeil, Rüdiger Frey, Paul Embrechts -- Princeton series in finance, -- isbn13 9780691122557 -- 478a0059673fecd0c76229cd3d8884e7 -- Anna’s Arc.pdf — pages 305–324

--- page 305 ---

7.2. Threshold Exceedances
289
Example 7.27 shows that the interpretation of Hill plots can be difﬁcult. In practice, various deviations from the ideal situation can occur. If the data do not come
from a distribution with a regularly varying tail, the Hill method is really not appropriate and Hill plots can be very misleading. Serial dependence in the data can
also spoil the performance of the estimator, although this is also true for the GPD
estimator. EKM contains a number of Hill “horror plots” based on simulated data
illustrating the issues that arise (see Notes and Comments).
Hill-based tail estimates.
For the risk-management applications of this book we
are less concerned with estimating the tail index of heavy-tailed data and more
concerned with tail and risk-measure estimates. We give a heuristic argument for a
standard tail estimator based on the Hill approach. We assume a tail model of the
form ¯F(x) = Cx−α, x ⩾u > 0, for some high threshold u; in other words, we
replace the slowly varying function by a constant for sufﬁciently large x. For an
appropriate value of k the tail index α is estimated by ˆα(H)
k,n and the threshold u is
replaced by Xk,n (or X(k+1),n in some versions); it remains to estimate C. Since
C can be written as C = uα ¯F(u), this is equivalent to estimating ¯F(u), and the
obvious empirical estimator is k/n (or (k −1)/n in some versions). Putting these
ideas together gives us the Hill tail estimator in its standard form:
ˆ¯F(x) = k
n
 x
Xk,n
−ˆα(H)
k,n
.
(7.24)
Writingtheestimatorinthiswayemphasizesthewayitistreatedmathematically.For
any pair k and n, both the Hill estimator and the associated tail estimator are treated
as functions of the k upper order statistics from the sample of size n. Obviously it is
possible to invert this estimator to get a quantile estimator and it is also possible to
devise an estimator of expected shortfall using arguments about regularly varying
tails.
The GPD-based tail estimator (7.21) is usually treated as a function of a random
number Nu of upper order statistics for a ﬁxed threshold u.The different presentation
of these estimators in the literature is a matter of convention and we can easily recast
both estimators in a similar form. Suppose we rewrite (7.24) in the notation of (7.21)
by substituting ˆξ(H), u and Nu for 1/ˆα(H)
k,n , Xk,n and k, respectively. We get
ˆ¯F(x) = Nu
n

1 + ˆξ(H) x −u
ˆξ(H)u
−1/ˆξ(H)
.
This estimator lacks the additional scaling parameter β in (7.21) and tends not to
perform as well, as is shown in simulated examples in the next section.
7.2.5
Simulation Study of EVT Quantile Estimators
First we consider estimation of ξ and then estimation of the high quantile VaRα. In
both cases estimators are compared using mean squared errors (MSEs); we recall
that the MSE of an estimator ˆθ of a parameter θ is given by MSE( ˆθ) = E( ˆθ −θ)2 =
(E( ˆθ −θ))2 + var( ˆθ), and thus has the well-known decomposition into squared
--- page 306 ---

290
7. Extreme Value Theory
Bias
k
Variance
0
0
100
200
300
400
0
0.02
0.04
−0.2
0.2
k
MSE
0
100
200
300
400
0.02
0.04
0.06
0.08
0.10
(a)
(b)
(c)
Figure 7.9.
Comparison of (a) estimated MSE, (b) bias and (c) variance for the Hill (dotted
line) and GPD (solid line) estimators of ξ, the reciprocal of the tail index, as a function of k
(or Nu), the number of upper order statistics from a sample of 1000 t-distributed data with
four degrees of freedom. See Example 7.28 for details.
bias plus variance. A good estimator should keep both the bias term E( ˆθ −θ) and
the variance term var( ˆθ) small.
Sinceanalyticalevaluationofbiasandvarianceisnotpossible,wecalculateMonte
Carlo estimates by simulating 1000 datasets in each experiment. The parameters of
the GPD are determined in all cases by ML; PWM, the main alternative, gives
slightly different results, but the conclusions are similar.
We calculate estimates using the Hill method and the GPD method based on different numbers of upper order statistics (or differing thresholds) and try to determine
the choice of k (or Nu) that is most appropriate for a sample of size n. In the case
of estimating VaR we also compare the EVT estimators with the simple empirical
quantile estimator.
Example 7.28 (Monte Carlo experiment). We assume that we have a sample of
1000 iid data from a t distribution with four degrees of freedom and want to estimate ξ, the reciprocal of the tail index, which in this case has the true value 0.25.
(This is demonstrated in Example 7.29 at the end of this chapter.) The Hill estimate is constructed for k values in the range {2, . . . , 200} and the GPD estimate is
constructed for k (or Nu) values in {30, 40, 50, . . . , 400}. The results are shown in
Figure 7.9.
The t distribution has a well-behaved regularly varying tail and the Hill estimator gives better estimates of ξ than the GPD method, with an optimal value of k
around 20–30. The variance plot shows where the Hill method gains over the GPD
method; the variance of the GPD-based estimator is much higher than that of the
Hill estimator for small numbers of order statistics. The magnitudes of the biases
are closer together, with the Hill method tending to overestimate ξ and the GPD
--- page 307 ---

7.2. Threshold Exceedances
291
Bias
k
Var
50
100
150
200
250
300
k
MSE
50 100 150 200 250 300
0.10
0.12
0.14
0.16
(a)
(b)
(c)
0.09
0.11
0.12
−0.05
0.10
0.20
0
0.05
0.15
0.10
Figure 7.10.
Comparison of (a) estimated MSE, (b) bias and (c) variance for the Hill (dotted
line) and GPD (solid line) estimators of VaR0.99, as a function of k (or Nu), the number of
upper order statistics from a sample of 1000 t-distributed data with four degrees of freedom.
Dashed line also shows results for the (threshold-independent) empirical quantile estimator.
See Example 7.28 for details.
method tending to underestimate it. If we were to use the GPD method, the optimal
choice of threshold would be one giving 100–150 exceedances.
The conclusions change when we attempt to estimate the 99%VaR; the results are
shown in Figure 7.10. The Hill method has a negative bias for low values of k but a
rapidly growing positive bias for larger values of k; the GPD estimator has a positive
bias that grows much more slowly; the empirical method has a negative bias. The
GPD attains its lowest MSE value for a value of k around 100, but, more importantly,
the MSE is very robust to the choice of k because of the slow growth of the bias.
The Hill method performs well for 20 ⩽k ⩽75 (we only use k values that lead to a
quantile estimate beyond the effective threshold Xk,n) but then deteriorates rapidly.
Both EVT methods obviously outperform the empirical quantile estimator. Given
the relative robustness of the GPD-based tail estimator to changes in k, the issue of
threshold choice for this estimator seems less critical than for the Hill method.
7.2.6
Conditional EVT for Financial Time Series
The GPD method when applied to threshold exceedances in a ﬁnancial return series
(as in Examples 7.24 and 7.25) is essentially an unconditional method for estimating
the tail of the P&L distribution and associated risk measures. In Chapter 2 we argued
that a conditional risk-measurement approach may be more appropriate for short
time horizons, and in Section 2.3.6 we observed that this generally led to better
backtesting results. We now consider a simple adaptation of the GPD method to
obtain conditional risk-measure estimates in a time series context. This adaptation
uses the GARCH model and related ideas in Chapter 4.
We assume in particular that we are in the framework of Section 4.4.2 so that
Lt−n+1, . . . , Lt are negative log-returns generated by a strictly stationary time series
process (Lt). This process is assumed to be of the form Lt = µt + σtZt, where µt
--- page 308 ---

292
7. Extreme Value Theory
and σt are Ft−1-measurable and (Zt) are iid innovations with some unknown df G;
an example would be an ARMA model with GARCH errors. To obtain estimates of
the risk measures
VaRt
α = µt+1 + σt+1qα(Z),
ESt
α = µt+1 + σt+1 ESα(Z),
we ﬁrst ﬁt a GARCH model by the QML procedure of Section 4.3.4 (since we do not
assume a particular innovation distribution) and use this to estimate µt+1 and σt+1.
As an alternative we could use EWMA volatility forecasting instead. To estimate
qα(Z) and ESα(Z) we essentially apply the GPD tail estimation procedure to the
innovation distribution G. To get round the problem that we do not observe data
directly from the innovation distribution, we treat the residuals from the GARCH
analysis as our data and apply the GPD tail estimation method of Section 7.2.3 to the
residuals. In particular, we estimate qα(Z) and ESα(Z) using the VaR and expected
shortfall formulas in (7.18) and (7.19).
In Section 2.3.6 it was shown that this method gives good VaR estimates; in that
example the sample size was taken to be n = 1000 and the threshold was always
set so that there were 100 exceedances. In fact, the method also gives very good
conditional expected shortfall estimates, as is shown in the original paper of McNeil
and Frey (2000).
Notes and Comments
The ideas behind the importantTheorem 7.20, which underlies GPD modelling, may
be found in Pickands (1975) and Balkema and de Haan (1974). Important papers
developing the technique in the statistical literature are Davison (1984) and Davison
and Smith (1990). The estimation of the parameters of the GPD, both by ML and by
the method of probability-weighted moments, is discussed in Hosking and Wallis
(1987). The tail estimation formula (7.21) was suggested by Smith (1987) and the
theoretical properties of this estimator for iid data in the domain of attraction of an
extreme value distribution are extensively investigated in this paper. The Danish ﬁre
loss example is taken from McNeil (1997).
The Hill estimator goes back to Hill (1975) (see also Hall 1982). The theoretical
properties for dependent data, including linear processes with heavy-tailed innovations and ARCH and GARCH processes, were investigated by Resnick and St˘aric˘a
(1995,1996).TheideaofsmoothingtheestimatorisexaminedinResnickandSt˘aric˘a
(1997) and Resnick (1997). For Hill “horror plots”, showing situations when the Hill
estimator delivers particularly poor estimates of the tail index, see EKM, pp. 194,
270 and 343.
Alternative estimators based on order statistics include the estimator of Pickands
(1975), which is also discussed in Dekkers and de Haan (1989), and the DEdH
estimator of Dekkers, Einmahl and de Haan (1989). This latter estimator is used as
the basis of a quantile estimator in de Haan and Rootz´en (1993). Both the Pickands
and DEdH estimators are designed to estimate general ξ in the extreme value limit (in
contrast to the Hill estimator, which is designed for positive ξ); in empirical studies
the DEdH estimator seems to work better than the Pickands estimator. The issue of
--- page 309 ---

7.3. Tails of Speciﬁc Models
293
the optimal number of order statistics in such estimators is taken up in a series of
papers by Dekkers and de Haan (1993) and Dan´ıelsson et al. (2001). A method is
proposed which is essentially based on the bootstrap approach to estimating mean
squared error discussed in Hall (1990). A review paper relevant for applications to
insurance and ﬁnance is Matthys and Beirlant (2000).
Analyses of the tails of ﬁnancial data using methods based on the Hill estimator
can be found in Koedijk, Schafgans and de Vries (1990), Lux (1996) and various
papers by Dan´ıelsson and de Vries (1997a,b,c). The conditional EVT method was
developed in McNeil and Frey (2000); a Monte Carlo method using the GPD model
to estimate risk measures for the h-day loss distribution is also described. See also
Gen¸cay, Sel¸cuk and Ulug¨ulyaˇgci (2003) and Gen¸cay and Sel¸cuk (2004) for interesting applications of EVT methodology to VaR estimation.
7.3
Tails of Speciﬁc Models
In this short section we survey the tails of some of the more important distributions
and models that we have encountered in this book.
7.3.1
Domain of Attraction of Fr´echet Distribution
AsstatedinSection7.1.2,thedomainofattractionoftheFr´echetdistributionconsists
of distributions with regularly varying tails of the form ¯F(x) = x−αL(x) for α > 0,
where α is known as the tail index. These are heavy-tailed models where higherorder moments cease to exist. Normalized maxima of random samples from such
distributions converge to a Fr´echet distribution with shape parameter ξ = 1/α,
and excesses over sufﬁciently high thresholds converge to a generalized Pareto
distribution with shape parameter ξ = 1/α.
We now show that the Student t distribution and the inverse gamma distribution
are in this class; we analyse the former because of its general importance in ﬁnancial
modelling and the latter because it appears as the mixing distribution that yields the
Student t in the class of normal variance mixture models (see Example 3.7). In
Section 7.3.3 we will see that the mixing distribution in a normal variance mixture
model essentially determines the tail of that model.
Both the t and inverse gamma distributions are presented in terms of their density,
and the analysis of their tails proves to be a simple application of a useful result
known as Karamata’s Theorem, which is given in Section A.1.3.
Example 7.29 (Student t distribution). It is easily veriﬁed that the standard univariate t distribution with ν ⩾1 has a density of the form fν(x) = x−(ν+1)L(x).
Hence Karamata’s Theorem (see Theorem A.5) allows us to calculate the form of
the tail ¯Fν(x) =
 ∞
x
fν(y) dy by essentially treating the slowly varying function as
a constant and taking it out of the integral. We get
¯Fν(x) =
 ∞
x
y−(ν+1)L(y) dy ∼ν−1x−νL(x),
x →∞,
from which we conclude that the df Fν of a t distribution has tail index ν and
Fν ∈MDA(H1/ν) by Theorem 7.8.
--- page 310 ---

294
7. Extreme Value Theory
Example 7.30 (inverse gamma distribution). The density of the inverse gamma
distribution is given in (A.11). It is of the form fα,β(x) = x−(α+1)L(x), since
exp(−β/x) →1 as x →∞. Using the same technique as in Example 7.29, we
deduce that this distribution has tail index α, so Fα,β ∈MDA(H1/α).
7.3.2
Domain of Attraction of Gumbel Distribution
A mathematical characterization of the Gumbel class is that it consists of the
so-called von Mises distribution functions and any other distributions which
are tail equivalent to von Mises distributions (see EKM, pp. 138–150). We
give the deﬁnitions of both of these concepts below. Note that distributions
in this class can have both inﬁnite and ﬁnite right endpoints; again we write
xF = sup{x ∈R : F(x) < 1} ⩽∞for the right endpoint of F.
Deﬁnition 7.31 (von Mises distribution function). Suppose there exists some
z < xF such that F has the representation
¯F(x) = c exp

−
 x
z
1
a(t) dt

,
z < x < xF ,
where c is some positive constant, a(t) is a positive and absolutely continuous
function with density a′, and limx→xF a′(x) = 0. Then F is called a von Mises
distribution function.
Deﬁnition 7.32 (tail equivalence). Two dfs F and G are called tail equivalent if
they have the same right endpoints (i.e. xF = xG) and limx→xF ¯F(x)/ ¯G(x) = c for
some constant 0 < c < ∞.
To decide whether a particular df F is a von Mises df, the following condition is
extremely useful. Assume there exists some z < xF such that F is twice differentiable on (z, xF ) with density f = F ′ and F ′′ < 0 in (z, xF ). Then F is a von Mises
df if and only if
lim
x→xF
¯F(x)F ′′(x)
f 2(x)
= −1.
(7.25)
We now use this condition to show that the gamma df is a von Mises df.
Example 7.33 (gamma distribution). The density f
= fα,β of the gamma
distribution is given in (A.7), and a straightforward calculation yields F ′′(x) =
f ′(x) = −f (x)(β + (1 −α)/x) < 0, provided x > max((α −1)/β, 0).
Clearly, limx→∞F ′′(x)/f (x) = −β. Moreover, using L’Hˆopital’s rule we get
limx→∞¯F(x)/f (x) = limx→∞−f (x)/f ′(x) = β−1. Combining these two limits
establishes (7.25).
Example 7.34 (GIG distribution). The density of an rv X ∼N−(λ, χ, ψ) with
the GIG distribution is given in (A.8). Let Fλ,χ,ψ(x) denote the df and consider the
case where ψ > 0. If ψ = 0, then the GIG is an inverse gamma distribution, which
was shown in Example 7.30 to be in the Fr´echet class. If ψ > 0, then λ ⩾0, and
a similar technique to Example 7.33 could be used to establish that the GIG is a
--- page 311 ---

7.3. Tails of Speciﬁc Models
295
von Mises df. In the case where λ > 0 it is easier to demonstrate tail equivalence
with a gamma distribution, which is the special case when χ = 0. We observe that
lim
x→∞
¯Fλ,χ,ψ(x)
¯Fλ,0,ψ(x) = lim
x→∞
fλ,χ,ψ(x)
fλ,0,ψ(x) = cλ,χ,ψ
for some constant cλ,χ,ψ. It follows that Fλ,χ,ψ ∈MDA(H0).
7.3.3
Mixture Models
In this book we have considered a number of models for ﬁnancial risk-factor changes
that arise as mixtures of rvs. In Chapter 3 we introduced multivariate normal variance
mixture models including the Student t, and (symmetric) generalized hyperbolic
distributions, which have the general structure given in (3.19). A one-dimensional
normal variance mixture (or the marginal distribution of a d-dimensional normal
variance mixture) is of the same type (see Section A.1.1) as an rv X satisfying
X d=
√
WZ,
(7.26)
where Z ∼N(0, 1) and W is an independent, positive-valued scalar rv. We would
like to know more about the tails of distributions satisfying (7.26).
More generally, to understand the tails of the marginal distributions of elliptical
distributions it sufﬁces to consider spherical distributions, which have the stochastic
representation
X d= RS
(7.27)
for a random vector S that is uniformly distributed on the unit sphere Sd−1 =
{s ∈Rd : s′s = 1}, and an independent radial variate R (see Section 3.3.1 and
Theorem 3.22 in particular). Again we would like to know more about the tails of
the marginal distributions of the vector X in (7.27).
In Section 4.3 of Chapter 4 we considered strictly stationary stochastic processes (Xt), such as GARCH processes satisfying equations of the form
Xt = σtZt,
(7.28)
where (Zt) are strict white noise innovations, typically with a Gaussian or (more
realistically) a scaled Student t distribution, and σt is a Ft−1-measurable rv representing volatility. These models can also be seen as mixture models and we would
like to know something about the tail of the stationary distribution of (Xt).
A useful result for analysing the tails of mixtures is the following theorem due to
Breiman (1965), which we immediately apply to spherical distributions.
Theorem 7.35 (tails of mixture distributions). Let X be given by X = YZ for
independent, non-negative rvs Y and Z such that
(1) Y has a regularly varying tail with tail index α;
(2) E(Zα+ε) < ∞for some ε > 0.
Then X has a regularly varying tail with tail index α and
P(X > x) ∼E(Zα)P(Y > x),
x →∞.
--- page 312 ---

296
7. Extreme Value Theory
Proposition 7.36 (tails of spherical distributions). Let X d= RS ∼Sd(ψ) have
a spherical distribution. If R has a regularly varying tail with tail index α, then so
does |Xi| for i = 1, . . . , d. If E(Rk) < ∞for all k > 0, then |Xi| does not have a
regularly varying tail.
Proof. Suppose that R has a regularly varying tail with tail index α and consider
RSi. Since |Si| is a non-negative rv with ﬁnite support [0, 1] and ﬁnite moments, it
follows from Theorem 7.35 that R|Si|, and hence |Xi|, are regularly varying with
tail index α. If E(Rk) < ∞for all k > 0, then E|Xi|k < ∞for all k > 0, so that
|Xi| cannot have a regularly varying tail.
Example 7.37 (tails of normal variance mixtures). Suppose that X d=
√
WZ with
Z ∼Nd(0, Id) and W an independent scalar rv, so that both Z and X have spherical
distributions and X has a normal variance mixture distribution. The vector Z has the
spherical representation Z d= ˜RS, where ˜R2 ∼χ2
d (see Example 3.24). The vector
X has the spherical representation X d= RS, where R d=
√
W ˜R.
Now, the chi-squared distribution (being a gamma distribution) is in the domain of
attraction of the Gumbel distribution, so E( ˜Rk) = E(( ˜R2)k/2) < ∞for all k > 0.
We ﬁrst consider the case when W has a regularly varying tail with tail index α so that
¯FW(w) = L(w)w−α. It follows that P(
√
W > x) = P(W > x2) = L2(x)x−2α,
where L2(x) := L(x2) is also slowly varying, so that
√
W has a regularly varying
tail with tail index 2α. By Theorem 7.35, R d=
√
W ˜R also has a regularly varying
tail with tail index 2α and, by Proposition 7.36, so do the components of |X|.
To consider a particular case, suppose that W ∼Ig( 1
2ν, 1
2ν), so that, by Example 7.30, W is regularly varying with tail index 1
2ν. Then
√
W has a regularly
varying tail with tail index ν and so does |Xi|; this is hardly surprising because
X ∼td(ν, 0, Id), implying that Xi has a univariate Student t distribution with ν
degrees of freedom, and we already know from Example 7.29 that this has tail
index ν.
On the other hand, if FW ∈MDA(H0), then E(Rk) < ∞for all k > 0 and |Xi|
cannot have a regularly varying tail by Proposition 7.36. This means, for example,
that univariate generalized hyperbolic distributions do not have power tails (except
for the special boundary case corresponding to Student t) because the GIG is in
the maximum domain of attraction of the Gumbel distribution, as was shown in
Example 7.34.
Analysis of the tails of the stationary distribution of GARCH-type models is more
challenging. In view of Theorem 7.35 and the foregoing examples, it is clear that
when the innovations (Zt) are Gaussian, then the law of the process (Xt) in (7.28)
will have a regularly varying tail if the volatility σt has a regularly varying tail.
Mikosch and St˘aric˘a (2000) analyse the GARCH(1, 1) model (see Deﬁnition 4.20),
where the squared volatility satisﬁes σ 2
t
= α0 + α1X2
t−1 + βσ 2
t−1. They show
that under relatively weak conditions on the innovation distribution of (Zt), the
volatility σt has a regularly varying tail with tail index κ given by the solution of
the equation
E((α1Z2
t + β)κ/2) = 1.
(7.29)
--- page 313 ---

7.3. Tails of Speciﬁc Models
297
Table 7.2.
Approximate theoretical values of the tail index κ solving (7.29) for various
GARCH(1, 1) processes with Gaussian and Student t innovation distributions.
t distribution



Parameters
Gauss
ν = 8
ν = 4
α1 = 0.2,
β = 0.75
4.4
3.5
2.7
α1 = 0.1,
β = 0.85
9.1
5.8
3.4
α1 = 0.05, β = 0.95
21.1
7.9
3.9
In Table 7.2 we have calculated approximate values of κ for various innovation distributions and parameter values using numerical integration and root-ﬁnding procedures. By Theorem 7.35 these are the values of the tail index for the stationary
distribution of the GARCH(1, 1) model itself.
Two main ﬁndings are obvious: for any ﬁxed set of parameter values, the tail
index gets smaller and the tail of the GARCH model gets heavier as we move to
heavier-tailed innovation distributions; for any ﬁxed innovation distribution, the tail
of the GARCH model gets lighter as we decrease theARCH effect (α1) and increase
the GARCH effect (β).
Tail dependence in elliptical distributions.
We close this section by giving a result
that reveals an interesting connection between tail dependence in elliptical distributions and regular variation of the radial rv R in the representation X d= µ + RAS
of an elliptically symmetric distribution given in Proposition 3.28.
Theorem 7.38. Let X d= µ + RAS ∼Ed(µ, Σ, ψ), where µ, R, A and S are as
in Proposition 3.28 and we assume that σii > 0 for all i = 1, . . . , d. If R has a
regularly varying tail with tail index α > 0, then the coefﬁcient of upper and lower
tail dependence between Xi and Xj is given by
λ(Xi, Xj) =
 π/2
(π/2−arcsin ρij ) cosα(t) dt
 π/2
0
cosα(t) dt
,
(7.30)
where ρij is the (i, j)th element of P = ℘(Σ) and ℘is the correlation operator
deﬁned in (3.5).
An example where R has a regularly varying tail occurs in the case of the multivariate t distribution X ∼td(ν, µ, Σ). It is obvious from the arguments used in
Example 7.37 that the tail of the df of R is regularly varying with tail index α = ν.
Thus (7.30) with α replaced by ν gives an alternative expression to (5.31) for calculating tail-dependence coefﬁcients for the t copula Ct
ν,P .
Arguably, the original expression (5.31) is easier to work with, since the df of
a univariate t distribution is available in statistical software packages. Moreover,
the equivalence of the two formulas allows us to conclude that we can use (5.31)
to evaluate tail-dependence coefﬁcients for any bivariate elliptical distribution with
correlation parameter ρ when the distribution of the radial rv R has a regularly
varying tail with tail index ν.
--- page 314 ---

298
7. Extreme Value Theory
Notes and Comments
Section 7.3 has been a highly selective account tailored to the study of a number
of very speciﬁc models, and all of the theoretical subjects touched upon—regular
variation, von Mises distributions, tails of products, tails of stochastic recurrence
equations—can be studied in much greater detail.
For more about regular variation, slow variation and Karamata’s Theorem see
Bingham, Goldie and Teugels (1987) and Seneta (1976). A summary of the more
important ideas with regard to the study of extremes is found in Resnick (1987).
Section 7.3.2, with the exception of the examples, is taken from EKM, and detailed
references to results on von Mises distributions and the maximum domain of attraction of the Gumbel distribution are found therein.
Theorem 7.35 follows from results of Breiman (1965). Related results on distributions of products are found in Embrechts and Goldie (1980). The discussion of
tails of GARCH models is based on Mikosch and St˘aric˘a (2000); the theory involves
the study of stochastic recurrence relations and is essentially due to Kesten (1973).
See also Mikosch (2003) for an excellent introduction to these ideas.
The formula for tail-dependence coefﬁcients in elliptical distributions when the
radial rv has a regularly varying tail is taken from Hult and Lindskog (2002). Similar
results were derived independently by Schmidt (2002); see also Frahm, Junker and
Szimayer (2003) for a discussion of the applicability of such results to ﬁnancial
returns.
7.4
Point Process Models
In our discussion of threshold models in Section 7.2 we considered only the magnitude of excess losses over high thresholds. In this section we consider exceedances
of thresholds as events in time and use a point process approach to model the occurrence of these events. We begin by looking at the case of regularly spaced iid data
and discuss the well-known peaks-over-threshold (POT) model for the occurrence
of extremes in such data; this model elegantly subsumes the models for maxima and
the GPD models for excess losses that we have so far described.
However, the assumptions of the standard POT model are typically violated
by ﬁnancial return series, because of the kind of serial dependence that volatility clustering generates in such data. Our ultimate aim is to ﬁnd more general
point process models to describe the occurrence of extreme values in ﬁnancial time
series, and we ﬁnd suitable candidates in the class of self-exciting point processes.
These models are of a dynamic nature and can be used to estimate conditional
VaRs; they offer an interesting alternative to the conditional EVT approach of Section 7.2.6 with the advantage that no prewhitening of data with GARCH processes
is required.
The following section gives an idea of the theory behind the POT model, but may
be skipped by readers who are content to go directly to a description of the standard
POT model in Section 7.4.2.
--- page 315 ---

7.4. Point Process Models
299
7.4.1
Threshold Exceedances for Strict White Noise
Consider a strict white noise process (Xi)i∈N representing ﬁnancial losses.While we
discuss the theory for iid variables for simplicity, the results we describe also hold for
dependent processes with extremal index θ = 1, i.e. processes where extreme values
show no tendency to cluster (see Section 7.1.3 for examples of such processes).
Throughout this section we assume that the common loss distribution is in the
maximum domain of attraction of an extreme value distribution (MDA(Hξ)) so
that (7.1) holds for the non-degenerate limiting distribution Hξ and normalizing sequences cn and dn. From (7.1) it follows, by taking logarithms and using
ln(1 −y) ∼−y as y →0, that for any ﬁxed x we have
lim
n→∞n ln(1 −¯F(cnx + dn)) = ln Hξ(x),
lim
n→∞n ¯F(cnx + dn) = −ln Hξ(x).
⎫
⎬
⎭
(7.31)
Throughout this section we also consider a sequence of thresholds (un(x)) deﬁned
by un(x) := cnx + dn for some ﬁxed value of x. Clearly, (7.31) implies that we
have n ¯F(un(x)) →−ln Hξ(x) as n →∞for this sequence of thresholds.
The number of losses in the sample X1, . . . , Xn exceeding the threshold un(x) is
a binomial rv, Nun(x) ∼B(n, ¯F(un(x))), with expectation n ¯F(un(x)). Since (7.31)
holds, the standard Poisson limit result implies that, as n →∞, the number
of exceedances Nun(x) converges to a Poisson rv with mean λ(x) = −ln Hξ(x),
depending on the particular x chosen.
The theory goes further. Not only is the number of exceedances asymptotically
Poisson, these exceedances occur according to a Poisson point process. To state the
result it is useful to give a brief summary of some ideas concerning point processes.
On point processes.
Suppose we have a sequence of rvs or vectors Y1, . . . , Yn
taking values in some state space X (for example, R or R2) and we deﬁne, for any
set A ⊂X, the rv
N(A) =
n

i=1
I{Yi∈A},
(7.32)
which counts the random number of Yi in the set A. Under some technical conditions
(see EKM, pp. 220–223), (7.32) is said to deﬁne a point process N(·). An example
of a point process is the Poisson point process.
Deﬁnition 7.39 (Poisson point process). The point process N(·) is called a Poisson
point process (or Poisson random measure) on X with intensity measure Λ if the
following two conditions are satisﬁed.
(a) For A ⊂X and k ⩾0,
P(N(A) = k) =
⎧
⎨
⎩
e−Λ(A) Λ(A)k
k!
,
Λ(A) < ∞,
0,
Λ(A) = ∞.
--- page 316 ---

300
7. Extreme Value Theory
(b) For any m ⩾1, if A1, . . . , Am are mutually disjoint subsets of X, then the
rvs N(A1), . . . , N(Am) are independent.
The intensity measure Λ(·) of N(·) is also known as the mean measure because
E(N(A)) = Λ(A). We also speak of the intensity function (or simply intensity) of the process, which is the derivative λ(x) of the measure satisfying
Λ(A) =

A λ(x) dx.
Asymptotic behaviour of the point process of exceedances.
Consider again the
strict white noise (Xi)i∈N and sequence of thresholds un(x) = cnx + dn for some
ﬁxed x. For n ∈N and 1 ⩽i ⩽n let Yi,n = (i/n)I{Xi>un(x)} and observe that Yi,n
can be thought of as returning either the normalized “time” i/n of an exceedance,
or zero. The point process of exceedances of the threshold un is the process Nn(·)
with state space X = (0, 1] given by
Nn(A) =
n

i=1
I{Yi,n∈A}
(7.33)
for A ⊂X. As the notation indicates, we consider this process to be an element
in a sequence of point processes indexed by n. The point process (7.33) counts
the exceedances with time of occurrence in the set A and we are interested in the
behaviour of this process as n →∞.
It may be shown (see Theorem 5.3.2 in EKM) that Nn(·) converges in distribution
on X to a Poisson process N(·) with intensity measure Λ(·) satisfying Λ(A) =
(t2−t1)λ(x)forA = (t1, t2) ⊂X,whereλ(x) = −ln Hξ(x)asbefore.Thisimplies,
in particular, that E(Nn(A)) →E(N(A)) = Λ(A) = (t2 −t1)λ(x). Clearly, the
intensity does not depend on time and takes the constant value λ := λ(x); we refer
to the limiting process as a homogeneous Poisson process with intensity or rate λ.
Application of the result in practice.
We give a heuristic argument explaining how
this limiting result is used in practice. We consider a ﬁxed large sample size n and a
ﬁxed high threshold u, which we assume satisﬁes u = cny + dn for some value y.
We expect that the number of threshold exceedances can be approximated by a
Poisson rv and that the point process of exceedances of u can be approximated by a
homogeneous Poisson process with rate λ = −ln Hξ(y) = −ln Hξ((u−dn)/cn). If
we replace the normalizing constants cn and dn by σ > 0 and µ, we have a Poisson
process with rate −ln Hξ,µ,σ(u). Clearly, we could repeat the same argument with
any high threshold so that, for example, we would expect it to be approximately true
that exceedances of the level x ⩾u occur according to a Poisson process with rate
−ln Hξ,µ,σ(x).
We thus have an intimate relationship between the GEV model for block maxima
and a Poisson model for the occurrence in time of exceedances of a high threshold.
The arguments of this section thus provide theoretical support for the observation in
Figure 4.3: that exceedances for simulated iid t data are separated by waiting times
that behave like iid exponential observations.
--- page 317 ---

7.4. Point Process Models
301
7.4.2
The POT Model
The theory of the previous section combined with the theory of Section 7.2 suggests
an asymptotic model for threshold exceedances in regularly spaced iid data (or data
from a process with extremal index θ = 1). The so-called POT model makes the
following assumptions.
• Exceedances occur according to a homogeneous Poisson process in time.
• Excess amounts above the threshold are iid and independent of exceedance
times.
• The distribution of excess amounts is generalized Pareto.
There are various alternative ways of describing this model. It might also be called a
marked Poisson point process, where the exceedance times constitute the points
and the GPD-distributed excesses are the marks. It can also be described as a
(non-homogeneous) two-dimensional Poisson point process, where points (t, x)
in two-dimensional space record times and magnitudes of exceedances. The latter
representation is particularly powerful, as we now discuss.
Two-dimensional Poisson formulation of POT model.
Assume that we have regularly spaced random losses X1, . . . , Xn and that we set a high threshold u. We
assume that, on the state space X = (0, 1] × (u, ∞), the point process deﬁned by
N(A) = n
i=1 I{(i/n,Xi)∈A} is a Poisson process with intensity at a point (t, x) given
by
λ(t, x) = 1
σ

1 + ξ x −µ
σ
−1/ξ−1
,
(7.34)
provided (1+ξ(x−µ)/σ) > 0, and by λ(t, x) = 0 otherwise. Note that this intensity
does not depend on t but does depend on x, and hence the two-dimensional Poisson
process is non-homogeneous; we simplify the notation to λ(x) := λ(t, x). For a set
of the form A = (t1, t2) × (x, ∞) ⊂X, the intensity measure is
Λ(A) =
 t2
t1
 ∞
x
λ(y) dy dt = −(t2 −t1) ln Hξ,µ,σ(x).
(7.35)
It follows from (7.35) that for any x ⩾u the implied one-dimensional process of
exceedances of the level x is a homogeneous Poisson process with rate τ(x) :=
−ln Hξ,µ,σ(x). Now consider the excess amounts over the threshold u. The tail of
the excess df over the threshold u, denoted ¯Fu(x) before, can be calculated as the
ratio of the rates of exceeding the levels u + x and u. We obtain
¯Fu(x) = τ(u + x)
τ(u)
=

1 +
ξx
σ + ξ(u −µ)
−1/ξ
= ¯Gξ,β(x)
for a positive scaling parameter β = σ + ξ(u −µ). This is precisely the tail of
the GPD model for excesses over the threshold u used in Section 7.2.2. Thus this
seemingly complicated model is indeed the POT model described informally at the
beginning of this section.
--- page 318 ---

302
7. Extreme Value Theory
Note also that the model implies the GEV distributional model for maxima. To
see this, consider the event that {Mn ⩽x} for some value x ⩾u. This may be
expressed in point process language as the event that there are no points in the set
A = (0, 1]×(x, ∞). The probability of this event is calculated to be P(Mn ⩽x) =
P(N(A) = 0) = exp(−Λ(A)) = Hξ,µ,σ(x), x ⩾u, which is precisely the GEV
model for maxima of n-blocks used in Section 7.1.4.
Statistical estimation of the POT model.
The most elegant way of ﬁtting the POT
model to data is to ﬁt the point process with intensity (7.34) to the exceedance data
in one step. Given the exceedance data { ˜Xj : j = 1, . . . , Nu}, the likelihood can be
written as
L(ξ, σ, µ; ˜X1, . . . , ˜XNu) = exp(−τ(u))
Nu
!
j=1
λ( ˜Xj).
(7.36)
Parameter estimates of ξ, σ and µ are obtained by maximizing this expression,
which is easily accomplished by numerical means. For literature on the derivation
of this likelihood, see Notes and Comments.
There are, however, simpler ways of getting the same parameter estimates. Suppose we reparametrize the POT model in terms of τ := τ(u) = −ln Hξ,µ,σ(u), the
rate of the one-dimensional Poisson process of exceedances of the level u, and
β = σ + ξ(u −µ), the scaling parameter of the implied GPD for the excess losses
over u. Then the intensity in (7.34) can be rewritten as
λ(x) = λ(t, x) = τ
β

1 + ξ x −u
β
−1/ξ−1
,
(7.37)
where ξ ∈R and τ, β > 0. Using this parametrization it is easily veriﬁed that the
log of the likelihood in (7.36) becomes
ln L(ξ, σ, µ; ˜X1, . . . , ˜XNu) = ln L1(ξ, β; ˜X1 −u, . . . , ˜XNu −u) + ln L2(τ; Nu),
where L1 is precisely the likelihood for ﬁtting a GPD to excess losses given in (7.14)
and ln L2(τ; Nu) = −τ +Nu ln τ, which is the log-likelihood for a one-dimensional
homogeneous Poisson process with rate τ. Such a partition of a log-likelihood into a
sum of two terms involving two different sets of parameters means that we can make
separate inferences about the two sets of parameters; we can estimate ξ and β in a
GPD analysis and then estimate τ by its MLE Nu and use these to infer estimates
of µ and σ.
Advantages of the POT model formulation.
One might ask what the advantages of
approaching the modelling of extremes through the two-dimensional Poisson point
process model described by the intensity (7.34) could be? One advantage is the fact
that the parameters ξ, µ and σ in the Poisson point process model do not have any
theoretical dependence on the threshold chosen, unlike the parameter β in the GPD
model, which appears in the theory as a function of the threshold u. In practice, we
would expect the estimated parameters of the Poisson model to be roughly stable
over a range of high thresholds, whereas the estimated β parameter varies with
threshold choice.
--- page 319 ---

7.4. Point Process Models
303
For this reason the intensity (7.34) is a framework that is often used to introduce
covariate effects into extreme value modelling. One method of doing this is to replace
the parameters µ and σ in (7.34) by parameters that vary over time as a function
of deterministic covariates. For example, we might have µ(t) = α + γ ′y(t), where
y(t) represents a vector of covariate values at time t. This would give us Poisson
processes that are also non-homogeneous in time.
Applicability of the POT model to return series data.
We now turn to the use of
the POT model with ﬁnancial return data. An initial comment is that returns do
not really form genuine point events in time, in contrast to recorded water levels
or wind speeds, for example. Returns are discrete-time measurements that describe
changes in value taking place over the course of, say, a day or a week. Nonetheless,
we assume that if we take a longer-term perspective, such data can be approximated
by point events in time.
In Section 4.1.1 and in Figure 4.3 in particular, we saw evidence that, in contrast
to iid data, exceedances of a high threshold for daily ﬁnancial return series do not
necessarily occur according to a homogeneous Poisson process. They tend instead
to form clusters corresponding to episodes of high volatility. Thus the standard POT
model is not directly applicable to ﬁnancial return data.
Theory suggests that for stochastic processes with extremal index θ < 1, such
as GARCH processes, the extremal clusters themselves should occur according to
a homogeneous Poisson process in time, so that the individual exceedances occur
according to a Poisson cluster process (see, for example, Leadbetter 1991). Thus
a suitable model for the occurrence and magnitude of exceedances in a ﬁnancial
return series might be some form of marked Poisson cluster process.
Rather than attempting to specify the mechanics of cluster formation, it is quite
common to try to circumvent the problem by declustering ﬁnancial return data: we
attempt to formally identify clusters of exceedances and then we apply the POT
model to cluster maxima only. This method is obviously somewhat ad hoc, as there
is usually no clear way of deciding where one cluster ends and another begins. A
possible declustering algorithm is given by the runs method. In this method a run
size r is ﬁxed and two successive exceedances are said to belong to two different
clusters if they are separated by a run of at least r values below the threshold (see
EKM, pp. 422–424). In Figure 7.11 the DAX daily negative returns of Figure 4.3
have been declustered with a run length of 10 trading days; this reduces the 100
exceedances to 42 cluster maxima.
However, it is not clear that applying the POT model to declustered data gives us
a particularly useful model. We can estimate the rate of occurrence of clusters of
extremes and say something about average cluster size; we can also derive a GPD
model for excess losses over thresholds for cluster maxima (where standard errors
for parameters may be more realistic than if we ﬁtted the GPD to the dependent
sample of all threshold exceedances). However, by neglecting the modelling of
cluster formation, we cannot make more dynamic statements about the intensity of
occurrence of threshold exceedances at any point in time. In the next section we will
describe point process models that attempt to do just that.
--- page 320 ---

304
7. Extreme Value Theory
0.04
0.06
0.08
0.10
0.12
0.04
0.06
0.08
0.10
0.12
•••••••••••••••••••••••••••••••••••••••••••••••• ••••••
••
•
•
•
•
Exponential quantiles
•••••••••••••••••••••••••••••••••
• •
•
•
•
•
0.02
0.04
0.06
0.08
0.2
0.4
0.6
0.8
1.0
0.02
0.04
0.06
0.08
0
Time
0.2
0.4
0.6
0.8
1.0
Time
Ordered data
Ordered data
Negative return
Negative return
5
4
3
2
1
0
Exponential quantiles
4
3
2
1
0
(a)
(b)
Figure 7.11.
(a) DAX daily negative returns and a QQplot of their spacings as in Figure 4.3.
(b) Data have been declustered with the runs method using a run length of 10 trading days.
The spacings of the 42 cluster maxima are more consistent with a Poisson model.
Example 7.40 (POT analysis of AT&T weekly losses). We close this section with
an example of a standard POT model applied to extremes in ﬁnancial return data. To
mitigate the clustering phenomenon discussed above we use weekly return data, as
previously analysed in Examples 7.24 and 7.25. Recall that these yield 102 weekly
percentage losses for the AT&T stock price exceeding a threshold of 2.75%. The
data are shown in Figure 7.12, where we observe that the inter-exceedance times
seem to have a roughly exponential distribution, although the discrete nature of the
times and the relatively low value of n means that there are some tied values for the
spacings, which makes the plot look a little granular. Another noticeable feature is
that the exceedances of the threshold appear to become more frequent over time,
which might be taken as evidence against the homogeneous Poisson assumption for
threshold exceedances and against the implicit assumption that the underlying data
form a realization from a stationary time series. It would be possible to consider a
--- page 321 ---

7.4. Point Process Models
305
•••• •••
••
•••
••
•
•
••
••
•
•
•
••
••
•
•
•
•
13.01.92
24.02.92
24.02.94
24.02.96
24.02.98
24.02.00
13.01.94
13.01.96
13.01.98
13.01.00
Time
Time
50
100
150
Ordered data
−20
20
20
0
10
2
4
0
Exponential
quantiles
(a)
(b)
(c)
Figure 7.12.
(a) Time series ofAT&T weekly percentage losses from 1991 to 2000. (b) Corresponding realization of the marked point process of exceedances of the threshold 2.75%.
(c) QQplot of inter-exceedance times against an exponential reference distribution. See Example 7.40 for details.
POT model incorporating a trend of increasingly frequent exceedances, but we will
not go this far.
We ﬁt the standard two-dimensional Poisson model to the 102 exceedances of
the threshold 2.75% using the likelihood in (7.36) and obtain parameter estimates
ˆξ = 0.22, ˆµ = 19.9 and ˆσ = 5.95. The implied GPD shape parameter for the distribution of excess losses over the threshold u is ˆβ = ˆσ + ˆξ(u −ˆµ) = 2.1, so we
have exactly the same estimates of ξ and β as in Example 7.24.
The estimated exceedance rate for the threshold u = 2.75 is given by ˆτ(u) =
−ln Hˆξ, ˆµ,ˆσ(u) = 102, which is precisely the number of exceedances of that threshold, as theory suggests. It is of more interest to look at estimated exceedance rates
for higher thresholds. For example, we get ˆτ(15) = 2.50, which implies that losses
exceeding 15% occur as a Poisson process with rate 2.5 losses per 10-year period,
so that such a loss is, roughly speaking, a four-year event. Thus the Poisson model
gives us an alternative method of deﬁning the return period of a stress event and
a more powerful way of calculating such a risk measure. Similarly we can invert
the problem to estimate return levels: suppose we deﬁne the 10-year return level as
that level which is exceeded according to a Poisson process with rate one loss per
10 years, then we can easily estimate the level in our model by calculating
H −1
ˆξ, ˆµ,ˆσ(exp(−1)) = 19.9,
so the 10-year event is a weekly loss of roughly 20%. Using the proﬁle likelihood
method in Section A.3.5 we could also give conﬁdence intervals for such estimates.
--- page 322 ---

306
7. Extreme Value Theory
7.4.3
Self-Exciting Processes
In this section we move away from homogeneous Poisson models for the occurrence
times of exceedance of high thresholds and consider self-exciting point processes, or
so-calledHawkesprocesses.Inthesemodelsaseriesofrecentthresholdexceedances
causes the instantaneous risk of a threshold exceedance at the present point in time
to be higher. The main area of application of these models has traditionally been
in the modelling of earthquakes and their aftershocks; however, their structure also
seems appropriate for modelling market shocks and the tremors that follow these.
Given data X1, . . . , Xn and a threshold u, we will assume as usual that there are
Nu exceedances, comprising the data {(i, Xi) : 1 ⩽i ⩽n, Xi > u}. Note that
from now on we will express the time of an exceedance on the natural timescale
of the time series, so if, for example, the data are daily observations, then our
times are expressed in days. It will also be useful to have the alternative notation
{(Tj, ˜Xj) : j = 1, . . . , Nu}, which enumerates exceedances consecutively.
We ﬁrst consider a model for exceedance times only. In point process notation we
let Yi = iI{Xi>u}, so Yi returns an exceedance time, in the event that one takes place
at time i, and returns zero otherwise. The point process of exceedances is the process
N(·) with state space X = (0, n] given by N(A) = n
i=1 I{Yi∈A} for A ⊂X.
We assume that the point process N(·) is a self-exciting process with conditional
intensity
λ∗(t) = τ + ψ

j:0<Tj <t
h(t −Tj, ˜Xj −u),
(7.38)
where τ > 0, ψ ⩾0 and h is some positive-valued function. Each previous
exceedance (Tj, ˜Xj) contributes to the conditional intensity and the amount that it
contributes can depend on both the elapsed time (t −Tj) since that exceedance and
the amount of the excess loss ( ˜Xj −u) over the threshold. Informally, we understand
the conditional intensity as expressing the instantaneous chance of a new exceedance
of the threshold at time t, like the rate or intensity of an ordinary Poisson process.
However, in the self-exciting model, the conditional intensity is itself a stochastic
process which depends on ω, the state of nature, through the history of threshold
exceedances up to (but not including) time t.
Possible parametric speciﬁcations of the h function are
• h(s, x) = exp(δx −γ s), where δ, γ > 0; or
• h(s, x) = exp(δx)(s + γ )−(ρ+1), where δ, γ, ρ > 0.
Collecting all parameters in θ, the likelihood takes the form
L(θ; data) = exp

−
 n
0
λ∗(s) ds
 Nu
!
i=1
λ∗(Ti),
and may be maximized numerically to obtain parameter estimates.
Example 7.41 (S&P daily percentage losses 1996–2003). We apply the selfexciting process methodology to all daily percentage losses incurred by the Standard
--- page 323 ---

7.4. Point Process Models
307
Time
03.01.96
03.01.99
03.01.02
Time
10.01.96
10.01.99
10.01.02
•••••••••••••••••••••••••••••••••••••••••••••••••••••• ••• •
•
•
0
100
150
Time
0
500
1000
1500
2000
2
3
4
5
6
7
−6
−4
−2
0
2
4
6
0
2
4
6
0.05
0.15
0.25
50
Ordered data
Exponential quantiles
Intensity
(a)
(b)
(c)
(d)
Figure 7.13.
(a) S&P daily percentage loss data. (b) Two hundred largest losses. (c) A
QQplot of inter-exceedance times against an exponential reference distribution. (d) The estimated intensity of exceeding the threshold in a self-exciting model. See Example 7.41 for
details.
& Poor’s index in the eight-year period 1996–2003 (2078 values). In Figure 7.13 the
loss data are shown as well as the point process of the 200 largest daily losses exceeding a threshold of 1.50%. Clearly, there is clustering in the pattern of exceedance
data and the QQplot shows that the inter-exceedance times are not exponential.
We ﬁt the simpler self-exciting model with h(s, x) = exp(δx −γ s). The parameter estimates (and standard errors) are ˆτ = 0.032(0.011), ˆψ = 0.016(0.0069),
ˆγ = 0.026(0.011), ˆδ = 0.13(0.27), suggesting that all parameters except δ are
signiﬁcant. The log-likelihood for the ﬁtted model is −648.2, whereas the loglikelihood for a homogeneous Poisson model is −668.2; thus the Poisson special
case can clearly be rejected. The ﬁnal picture shows the estimated intensity λ∗(t)
of crossing the threshold throughout the data observation period, which seems to
reﬂect the pattern of exceedances observed.
Note that a simple reﬁnement of this model (and those of the following section)
would be to consider a self-exciting structure where both extreme negative and
extreme positive returns contributed to the conditional intensity; this would involve
setting upper and lower thresholds and considering exceedances of both.
7.4.4
A Self-Exciting POT Model
We now consider how the POT model of Section 7.4.2 might be generalized to
incorporateaself-excitingcomponent.Weﬁrstdevelopamarkedself-excitingmodel
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
