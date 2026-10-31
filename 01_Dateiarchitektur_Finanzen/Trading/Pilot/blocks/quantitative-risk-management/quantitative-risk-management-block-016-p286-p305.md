# Quantitative Risk Management_ Concepts, Techniques, and -- Alexander J_ McNeil, Rüdiger Frey, Paul Embrechts -- Princeton series in finance, -- isbn13 9780691122557 -- 478a0059673fecd0c76229cd3d8884e7 -- Anna’s Arc.pdf — pages 286–305

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
--- page 287 ---

7.1. Maxima
271
Table 7.1.
Approximate values of the extremal index as a function of
the parameter α1 for the ARCH(1) process in (4.24).
α1
0.1
0.3
0.5
0.7
0.9
θ
0.999
0.939
0.835
0.721
0.612
• Strict white noise processes (iid rvs) have extremal index θ = 1.
• ARMA processes with Gaussian strict white noise innovations have θ = 1
(EKM, pp. 216–218). However, if the innovation distribution is in MDA(Hξ)
for ξ > 0, then θ < 1 (EKM, pp. 415, 416).
• ARCH and GARCH processes have θ < 1 (EKM, pp. 476–480).
The ﬁnal fact is particularly relevant to our ﬁnancial applications, since we saw
in Chapter 4 that ARCH and GARCH processes provide good models for many
ﬁnancial return series.
Example 7.11 (the extremal index of the ARCH(1) process). In Table 7.1 we
reproduce some results from de Haan et al. (1989), who calculate approximate
values for the extremal index of the ARCH(1) process (see Deﬁnition 4.16) using a
Monte Carlo simulation approach. Clearly, the stronger theARCH effect (that is, the
magnitude of the parameter α1), the greater the tendency of the process to cluster.
For a process with parameter 0.9 the extremal index value θ = 0.612 is interpreted
as suggesting that the average cluster size is 1/θ = 1.64.
7.1.4
The Block Maxima Method
Fitting the GEV distribution.
Suppose we have data from an unknown underlying
distribution F, which we suppose lies in the domain of attraction of an extreme value
distribution Hξ for some ξ. If the data are realizations of iid variables, or variables
from a process with an extremal index such as GARCH, the implication of the theory
is that the true distribution of the n-block maximum Mn can be approximated for
large enough n by a three-parameter GEV distribution Hξ,µ,σ.
We make use of this idea by ﬁtting the GEV distribution Hξ,µ,σ to data on the nblock maximum. Obviously we need repeated observations of an n-block maximum
and we assume that the data can be divided into m blocks of size n. This makes most
sense when there are natural ways of blocking the data. The method has its origins in
hydrology, where, for example, daily measurements of water levels might be divided
into yearly blocks and the yearly maxima collected. Analogously, we will consider
ﬁnancial applications where daily return data (recorded on trading days) are divided
into yearly (or semesterly or quarterly) blocks and the maximum daily falls within
these blocks are analysed.
We denote the block maximum of the jth block by Mnj, so our data are
Mn1, . . . , Mnm.The GEV distribution can be ﬁtted using various methods, including
maximum likelihood.An alternative is the method of probability-weighted moments
(see Notes and Comments). In implementing maximum likelihood it will be assumed
that the block size n is quite large so that, regardless of whether the underlying data
are dependent or not, the block maxima observations can be taken to be independent.
--- page 288 ---

272
7. Extreme Value Theory
In this case, writing hξ,µ,σ for the density of the GEV distribution, the log-likelihood
is easily calculated to be
l(ξ, µ, σ; Mn1, . . . , Mnm)
=
m

i=1
ln hξ,µ,σ(Mni)
= −m ln σ −

1 + 1
ξ
 m

i=1
ln

1 + ξ Mni −µ
σ

−
m

i=1

1 + ξ Mni −µ
σ
−1/ξ
,
which must be maximized subject to the parameter constraints that σ > 0 and
1 + ξ(Mni −µ)/σ > 0 for all i. While this represents an irregular likelihood
problem, due to the dependence of the parameter space on the values of the data,
the consistency and asymptotic efﬁciency of the resulting MLEs can be established
for the case when ξ > −1
2 using results in Smith (1985).
In determining the number and size of the blocks (m and n, respectively), a tradeoff necessarily takes place: roughly speaking, a large value of n leads to a more
accurate approximation of the block maxima distribution by a GEV distribution and
a low bias in the parameter estimates; a large value of m gives more block maxima
data for the ML estimation and leads to a low variance in the parameter estimates.
Note also that, in the case of dependent data, somewhat larger block sizes than
are used in the iid case may be advisable; dependence generally has the effect that
convergence to the GEV distribution is slower, since the effective sample size is nθ,
which is smaller than n.
Example 7.12 (block maxima analysis of S&P return data). Suppose we turn
the clock back and imagine it is the early evening of Friday 16 October 1987. An
unusually turbulent week in the equity markets has seen the S&P 500 index fall
by 9.21%. On that Friday alone the index is down 5.25% on the previous day, the
largest one-day fall since 1962.
We ﬁt the GEV distribution to annual maximum daily percentage falls in value
for the S&P index. Using data going back to 1960, shown in Figure 7.2, gives us
28 observations of the annual maximum fall (including the latest observation from
the incomplete year 1987). The estimated parameter values are ˆξ = 0.27, ˆµ = 2.04
and ˆσ = 0.72 with standard errors 0.21, 0.16 and 0.14, respectively. Thus the ﬁtted
distribution is a heavy-tailed Fr´echet distribution with an inﬁnite fourth moment,
suggesting that the underlying distribution is heavy-tailed. Note that the standard
errors imply considerable uncertainty in our analysis, as might be expected with only
28 observations of maxima. In fact, in a likelihood ratio test of the null hypothesis
that a Gumbel model ﬁts the data (H0 : ξ = 0), the null hypothesis cannot be
rejected.
To increase the number of blocks we also ﬁt a GEV model to 56 semesterly
maxima and obtain the parameter estimates ˆξ = 0.36, ˆµ = 1.65 and ˆσ = 0.54 with
standard errors 0.15, 0.09 and 0.08. This model has an even heavier tail, and the null
hypothesis that a Gumbel model is adequate is now rejected.
--- page 289 ---

7.1. Maxima
273
1960
1965
1970
1975
1980
1985
••
•
•
•••••• •
••
••
••••
•••
•
••
•
••
10
15
20
25
••••
•
•
•
•
•••••••••••••
•••••••••
•••••••••
••••••
•
•
•
•
•••
•
•
•
•
(a)
−6
−4
−2
0
2
4
0
5
20
30
40
50
0
10
(b)
(c)
0
2
4
6
0
2
4
6
Maxima
Maxima
Figure 7.2.
(a) S&P percentage returns for the period 1960 to 16 October 1987. (b) Annual
maxima of daily falls in the index; superimposed is an estimate of the 10-year return level
with associated 95% conﬁdence interval (dotted lines). (c) Semesterly maxima of daily falls
in the index; superimposed is an estimate of the 20-semester return level with associated 95%
conﬁdence interval. See Examples 7.12 and 7.15 for full details.
Return levels and stress losses.
The ﬁtted GEV model can be used to analyse stress
losses and we focus here on two possibilities: in the ﬁrst approach we deﬁne the
frequency of occurrence of the stress event and estimate its magnitude, this being
known as the return-level estimation problem; in the second approach we deﬁne the
size of the stress event and estimate the frequency of its occurrence, this being the
return-period problem.
Deﬁnition 7.13 (return level). Let H denote the df of the true distribution of
the n-block maximum. The k n-block return level is rn,k = q1−1/k(H), i.e. the
(1 −1/k)-quantile of H.
The k n-block return level can be roughly interpreted as that level which is
exceeded in one out of every k n-blocks on average. For example, the 10-tradingyear return level r260,10 is that level which is exceeded in one out of every 10 years on
average. (In the notation we assume that every year has 260 trading days, although
this is only an average and there will be slight differences from year to year.) Using
our ﬁtted model we would estimate a return level by
ˆrn,k = H −1
ˆξ, ˆµ,ˆσ

1 −1
k

= ˆµ + ˆσ
ˆξ

−ln

1 −1
k
−ˆξ
−1

.
(7.7)
Deﬁnition 7.14 (return period). Let H denote the df of the true distribution of
the n-block maximum. The return period of the event {Mn > u} is given by
kn,u = 1/ ¯H(u).
Observe that the return period kn,u is deﬁned in such a way that the kn,u n-block
return level is u. In other words, in kn,u n-blocks we would expect to observe a
single block in which the level u was exceeded. If there was a strong tendency for
the extreme values to cluster, we might expect to see multiple exceedances of the
--- page 290 ---

274
7. Extreme Value Theory
level within that block. Assuming that H is the df of a GEV distribution and using
our ﬁtted model, we would estimate the return period by ˆkn,u = 1/ ¯Hˆξ, ˆµ,ˆσ(u).
Note that both ˆrn,k and ˆkn,u are simple functionals of the estimated parameters
of the GEV distribution. As well as calculating point estimates for these quantities
we should give conﬁdence intervals that reﬂect the error in the parameter estimates
of the GEV distribution. A good method is to base such conﬁdence intervals on the
likelihood ratio statistic, as described in Section A.3.5. To do this we reparametrize
the GEV distribution in terms of the quantity of interest. For example, in the case
of return level, let φ = H −1
ξ,µ,σ(1 −(1/k)) and parametrize the GEV distribution by
θ = (φ, ξ, σ)′ rather than θ = (ξ, µ, σ)′. The maximum likelihood estimate of φ
is the estimate (7.7) and a conﬁdence interval can be constructed according to the
method in Section A.3.5 (see (A.22) in particular).
Example 7.15 (stress losses for S&P return data). We continue Example 7.12 by
estimating the 10-year return level and the 20-semester return level based on data up
to 16 October 1987, using (7.7) for the point estimate and the likelihood ratio method
as described above to get conﬁdence intervals. The point estimator of the 10-year
return level is 4.3% with a 95% conﬁdence interval of (3.4, 7.1); the point estimator
of the 20-semester return level is 4.5% with a 95% conﬁdence interval of (3.5, 7.4).
Clearly, there is some uncertainty about the size of events of this frequency even
with 28 years or 56 semesters of data.
The day after the end of our dataset, 19 October 1987, was Black Monday. The
index fell by the unprecedented amount of 20.5% in one day. This event is well
outside our conﬁdence interval for a 10-year loss. If we were to estimate a 50-year
return level (an event beyond our experience if we have 28 years of data), then our
point estimate would be 7.0 with a conﬁdence interval of (4.7, 22.2), so the 1987
crash lies close to the upper boundary of our conﬁdence interval for a much rarer
event. But the 28 maxima are really too few to get a reliable estimate for an event
as rare as the 50-year event.
If we turn the problem around and attempt to estimate the return period of a
20.5% loss, the point estimate is 2100 years (i.e. a 2 millennium event) but the 95%
conﬁdence interval encompasses everything from 45 years to essentially never! The
analysis of semesterly maxima gives only moderately more informative results: the
point estimate is 1400 semesters; the conﬁdence interval runs from 100 semesters
to 1.6 × 106 semesters. In summary, on 16 October 1987 we simply did not have
the data to say anything meaningful about an event of this magnitude. This illustrates the inherent difﬁculties of attempting to quantify events beyond our empirical
experience.
Notes and Comments
The main source for this chapter is Embrechts, Kl¨uppelberg and Mikosch (1997)
(EKM). Further important texts on EVT include Gumbel (1958), Leadbetter, Lindgren and Rootz´en (1983), Galambos (1987), Resnick (1987), Falk, H¨usler and Reiss
(1994), Reiss and Thomas (1997), Coles (2001) and Beirlant et al. (2004).
--- page 291 ---

7.2. Threshold Exceedances
275
The forms of the limit law for maxima were ﬁrst studied by Fisher and Tippett
(1928). The subject was brought to full mathematical fruition in the fundamental
papers of Gnedenko (1941, 1943). The concept of the extremal index, which appears
in the theory of maxima of stationary series, has a long history. The ﬁrst mathematically precise deﬁnition seems to have been given by Leadbetter (1983). See also
Leadbetter, Lindgren and Rootz´en (1983) and Smith and Weissman (1994) for more
details. The theory required to calculate the extremal index of an ARCH(1) process
(as in Table 7.1) is found in de Haan et al. (1989) and also in EKM, pp. 473–480.
For the GARCH(1, 1) process consult Mikosch and St˘aric˘a (2000).
A further difﬁcult task is the statistical estimation of the extremal index from time
series data under the assumption that these data do indeed come from a process with
an extremal index. Two general methods known as the blocks and runs methods are
described in EKM, Section 8.1.3; these methods go back to work of Hsing (1991)
and Smith and Weissman (1994). Although the estimators have been used in realworld data analyses (see, for example, Davison and Smith 1990)), it remains true
that the extremal index is a very difﬁcult parameter to estimate accurately.
The maximum likelihood ﬁtting of the GEV distribution is described by Hosking
(1985) and Hosking, Wallis and Wood (1985). Consistency and asymptotic normality can be demonstrated for the case ξ > −0.5 using results in Smith (1985).
An alternative method known as probability-weighted moments (PWM) has been
proposed by Hosking, Wallis and Wood (1985) (see also EKM, pp. 321–323). The
analysis of block maxima in Examples 7.12 and 7.15 is based on McNeil (1998).
Analyses of ﬁnancial data using the block maxima method may also be found in
Longin (1996), one of the earliest papers to apply EVT methodology to ﬁnancial
data.
7.2
Threshold Exceedances
The block maxima method discussed in Section 7.1.4 has the major defect that it is
very wasteful of data; to perform our analyses we retain only the maximum losses in
large blocks. For this reason it has been largely superseded in practice by methods
based on threshold exceedances, where we use all data that are extreme in the sense
that they exceed a particular designated high level.
7.2.1
Generalized Pareto Distribution
The main distributional model for exceedances over thresholds is the generalized
Pareto distribution (GPD).
Deﬁnition 7.16 (GPD). The df of the GPD is given by
Gξ,β(x) =

1 −(1 + ξx/β)−1/ξ,
ξ̸ = 0,
1 −exp(−x/β),
ξ = 0,
(7.8)
where β > 0, and x ⩾0 when ξ ⩾0 and 0 ⩽x ⩽−β/ξ when ξ < 0. The
parameters ξ and β are referred to, respectively, as the shape and scale parameters.
--- page 292 ---

276
7. Extreme Value Theory
0
2
4
6
8
0
2
4
6
8
x
x
0.2
0.4
0.6
0.8
1.0
0
g(x)
0.2
0.4
0.6
0.8
1.0
0
G(x)
(a)
(b)
Figure 7.3.
(a) Distribution function of GPD in three cases: the solid line corresponds to
ξ = 0 (exponential); the dotted line to ξ = 0.5 (a Pareto distribution); and the dashed line to
ξ = −0.5 (Pareto type II). The scale parameter β is equal to 1 in all cases. (b) Corresponding
densities.
Like the GEV distribution in Deﬁnition 7.1, the GPD is generalized in the sense
that it contains a number of special cases: when ξ > 0 the df Gξ,β is that of an
ordinary Pareto distribution with α = 1/ξ and κ = β/ξ (see Section A.2.8); when
ξ = 0 we have an exponential distribution; when ξ < 0 we have a short-tailed,
Pareto type II distribution. Moreover, as in the case of the GEV distribution, for
ﬁxed x the parametric form is continuous in ξ, so limξ→0 Gξ,β(x) = G0,β(x). The
df and density of the GPD for various values of ξ and β = 1 are shown in Figure 7.3.
In terms of domains of attraction we have that Gξ,β ∈MDA(Hξ) for all ξ ∈R.
Note that, for ξ > 0 and ξ < 0, this assertion follows easily from the characterizations in Theorems 7.8 and 7.10. In the heavy-tailed case, ξ > 0, it may be easily
veriﬁed that E(Xk) = ∞for k ⩾1/ξ. The mean of the GPD is deﬁned provided
ξ < 1 and is
E(X) = β/(1 −ξ).
(7.9)
The role of the GPD in EVT is as a natural model for the excess distribution over
a high threshold. We deﬁne this concept along with the mean excess function, which
will also play an important role in the theory.
Deﬁnition 7.17 (excess distribution over threshold u). Let X be an rv with df F.
The excess distribution over the threshold u has df
Fu(x) = P(X −u ⩽x | X > u) = F(x + u) −F(u)
1 −F(u)
(7.10)
for 0 ⩽x < xF −u, where xF ⩽∞is the right endpoint of F.
Deﬁnition 7.18 (mean excess function). The mean excess function of an rv X with
ﬁnite mean is given by
e(u) = E(X −u | X > u).
(7.11)
--- page 293 ---

7.2. Threshold Exceedances
277
The excess df Fu describes the distribution of the excess loss over the threshold
u, given that u is exceeded. The mean excess function e(u) expresses the mean of
Fu as a function of u. In survival analysis the excess df is more commonly known as
the residual life df—it expresses the probability that, say, an electrical component
which has functioned for u units of time fails in the time period (u, u + x]. The
mean excess function is known as the mean residual life function and gives the
expected residual lifetime for components with different ages. For the special case
of the GPD, the excess df and mean excess function are easily calculated.
Example 7.19 (excess distribution of exponential and GPD). If F is the df of
an exponential rv, then it is easily veriﬁed that Fu(x) = F(x) for all x, which is
the famous lack-of-memory property of the exponential distribution—the residual
lifetime of the aforementioned electrical component would be independent of the
amount of time that component has already survived. More generally, if X has df
F = Gξ,β, then, using (7.10), the excess df is easily calculated to be
Fu(x) = Gξ,β(u)(x),
β(u) = β + ξu,
(7.12)
where 0 ⩽x < ∞if ξ ⩾0 and 0 ⩽x ⩽−(β/ξ) −u if ξ < 0. The excess
distribution remains a GPD with the same shape parameter ξ but with a scaling that
grows linearly with the threshold u. The mean excess function of the GPD is easily
calculated from (7.12) and (7.9) to be
e(u) = β(u)
1 −ξ = β + ξu
1 −ξ ,
(7.13)
where 0 ⩽u < ∞if 0 ⩽ξ < 1 and 0 ⩽u ⩽−β/ξ if ξ < 0. It may be observed
that the mean excess function is linear in the threshold u, which is a characterizing
property of the GPD.
Example 7.19 shows that the GPD has a kind of stability property under the
operation of calculating excess distributions. We now give a mathematical result
that shows that the GPD is, in fact, a natural limiting excess distribution for many
underlying loss distributions. The result can also be viewed as a characterization
theorem for the domain of attraction of the GEV distribution. In Section 7.1.2 we
looked separately at characterizations for each of the three cases ξ > 0, ξ = 0 and
ξ < 0; the following result offers a global characterization of MDA(Hξ) for all ξ
in terms of the limiting behaviour of excess distributions over thresholds.
Theorem 7.20(Pickands–Balkema–deHaan). Wecanﬁnda(positive-measurable
function) β(u) such that
lim
u→xF
sup
0⩽x<xF −u
|Fu(x) −Gξ,β(u)(x)| = 0,
if and only if F ∈MDA(Hξ), ξ ∈R.
Thus the distributions for which normalized maxima converge to a GEV distribution constitute a set of distributions for which the excess distribution converges
to the GPD as the threshold is raised; moreover, the shape parameter of the limiting
--- page 294 ---

278
7. Extreme Value Theory
GPD for the excesses is the same as the shape parameter of the limiting GEV distribution for the maxima. We have already stated in Section 7.1.2 that essentially all
the commonly used continuous distributions of statistics are in MDA(Hξ) for some
ξ, so Theorem 7.20 proves to be a very widely applicable result that essentially says
that the GPD is the canonical distribution for modelling excess losses over high
thresholds.
7.2.2
Modelling Excess Losses
We exploit Theorem 7.20 by assuming that we are dealing with a loss distribution F ∈MDA(Hξ) so that, for some suitably chosen high threshold u, we can
model Fu by a generalized Pareto distribution. We formalize this with the following
assumption.
Assumption 7.21. Let F be a loss distribution with right endpoint xF and assume
that for some high threshold u we have Fu(x) = Gξ,β(x) for 0 ⩽x < xF −u and
some ξ ∈R and β > 0.
This is clearly an idealization, since in practice the excess distribution will generally not be exactly GPD, but we use Assumption 7.21 to make a number of calculations in the following sections.
The method.
Given loss data X1, . . . , Xn from F, a random number Nu will exceed
our threshold u; it will be convenient to relabel these data ˜X1, . . . , ˜XNu. For each
of these exceedances we calculate the amount Yj = ˜Xj −u of the excess loss. We
wish to estimate the parameters of a GPD model by ﬁtting this distribution to the
Nu excess losses. There are various ways of ﬁtting the GPD including maximum
likelihood (ML) and probability-weighted moments (PWM). The former method is
more commonly used and is easy to implement if the excess data can be assumed
to be realizations of independent rvs, since the joint density will then be a product
of marginal GPD densities.
Writing gξ,β for the density of the GPD, the log-likelihood may be easily calculated to be
ln L(ξ, β; Y1, . . . , YNu) =
Nu

j=1
ln gξ,β(Yj)
= −Nu ln β −

1 + 1
ξ
 Nu

j=1
ln

1 + ξ Yj
β

,
(7.14)
which must be maximized subject to the parameter constraints that β > 0 and
1 + ξYj/β > 0 for all j. Solving the maximization problem yields a GPD model
Gˆξ, ˆβ for the excess distribution Fu.
Non-iid data.
For insurance or operational risk data the iid assumption is often
unproblematic, but this is clearly not true for time series of ﬁnancial returns. If the
data are serially dependent but show no tendency to give clusters of extreme values,
then this might suggest that the underlying process has extremal index θ = 1. In this
--- page 295 ---

7.2. Threshold Exceedances
279
case, asymptotic theory that we summarize in Section 7.4 suggests a limiting model
for high-level threshold exceedances, in which exceedances occur according to a
Poisson process and the excess loss amounts are iid generalized Pareto distributed.
If extremal clustering is present, suggesting an extremal index θ < 1 (as would
be consistent with an underlying GARCH process), the assumption of independent
excess losses is less satisfactory. The easiest approach is to neglect this problem
and to consider the ML method to be a quasi-maximum likelihood (QML) method,
where the likelihood is misspeciﬁed with respect to the serial dependence structure
of the data; we follow this course in this section. The point estimates should still be
reasonable, although standard errors may be too small. In Section 7.4 we discuss
threshold exceedances in non-iid data in more detail.
Excesses over higher thresholds.
From the model we have ﬁtted to the excess
distribution over u we can easily infer a model for the excess distribution over any
higher threshold. We have the following lemma.
Lemma 7.22. Under Assumption 7.21 it follows that Fv(x) = Gξ,β+ξ(v−u)(x) for
any higher threshold v ⩾u.
Proof. We use (7.10) and the df of the GPD in (7.8) to infer that
¯Fv(x) =
¯F(v + x)
¯F(v)
=
¯F(u + (x + v −u))
¯F(u)
¯F(u)
¯F(u + (v −u))
=
¯Fu(x + v −u)
¯Fu(v −u)
=
¯Gξ,β(x + v −u)
¯Gξ,β(v −u)
= ¯Gξ,β+ξ(v−u)(x).
Thus the excess distribution over higher thresholds remains a GPD with the same
ξ parameter but a scaling that grows linearly with the threshold v. Provided that
ξ < 1, the mean excess function is given by
e(v) = β + ξ(v −u)
1 −ξ
=
ξv
1 −ξ + β −ξu
1 −ξ ,
(7.15)
where u ⩽v < ∞if 0 ⩽ξ < 1 and u ⩽v ⩽u −β/ξ if ξ < 0.
The linearity of the mean excess function (7.15) in v is commonly used as a
diagnostic for data admitting a GPD model for the excess distribution. It forms
the basis for the following simple graphical method for choosing an appropriate
threshold.
Sample mean excess plot.
For positive-valued loss data X1, . . . , Xn we deﬁne
the sample mean excess function to be an empirical estimator of the mean excess
function in Deﬁnition 7.18. The estimator is given by
en(v) =
n
i=1(Xi −v)I{Xi>v}
n
i=1 I{Xi>v}
.
(7.16)
--- page 296 ---

280
7. Extreme Value Theory
To study this function we generally construct the mean excess plot {(Xi,n, en(Xi,n)) :
2 ⩽i ⩽n}, where Xi,n denotes the ith order statistic. If the data support a GPD
model over a high threshold, then (7.15) suggests that this plot should become
increasingly “linear” for higher values of v. A linear upward trend indicates a GPD
model with positive shape parameter ξ; a plot tending towards the horizontal indicates a GPD with approximately zero shape parameter, or, in other words, an exponential excess distribution; a linear downward trend indicates a GPD with negative
shape parameter.
These are the ideal situations but in practice some experience is required to read
mean excess plots. Even for data that are genuinely generalized Pareto distributed,
the sample mean excess plot is seldom perfectly linear, particularly towards the
right-hand end, where we are averaging a small number of large excesses. In fact
we often omit the ﬁnal few points from consideration, as they can severely distort
the picture. If we do see visual evidence that the mean excess plot becomes linear,
then we might select as our threshold u a value towards the beginning of the linear
section of the plot (see, in particular, Example 7.24).
Example 7.23 (Danish ﬁre loss data). The Danish ﬁre insurance data are a wellstudied set of ﬁnancial losses that neatly illustrate the basic ideas behind modelling
observations that seem consistent with an iid model. The dataset consists of 2156
ﬁre insurance losses over 1 000 000 Danish kroner from 1980 to 1990 inclusive. The
loss ﬁgure represents a combined loss for a building and its contents, as well as in
some cases a loss of business earnings; the losses are inﬂation adjusted to reﬂect
1985 values and are shown in Figure 7.4(a).
The mean excess plot in Figure 7.4(b) is in fact fairly “linear” over the entire range
of the losses and its upward slope leads us to expect that a GPD with positive shape
parameter ξ could be ﬁtted to the entire dataset. However, there is some evidence
of a “kink” in the plot below the value 10 and a “straightening out” of the plot
above this value, so we have chosen to set our threshold at u = 10 and ﬁt a GPD
to excess losses above this threshold, in the hope of obtaining a model that is a
good ﬁt to the largest of the losses. The ML parameter estimates are ˆξ = 0.50 and
ˆβ = 7.0 with standard errors 0.14 and 1.1, respectively. Thus the model we have
ﬁtted is essentially a very heavy-tailed, inﬁnite-variance model. A picture of the
ﬁtted GPD model for the excess distribution ˆFu(x −u) is also given in Figure 7.4(c),
superimposed on points plotted at empirical estimates of the excess probabilities for
each loss; note the good correspondence between the empirical estimates and the
GPD curve.
In insurance we might use the model to estimate the expected size of the insurance loss, given that it enters a given insurance layer. Thus we can estimate
the expected loss size given exceedance of the threshold of 10 000 000 kroner
or of any other higher threshold by using (7.15) with the appropriate parameter
estimates.
Example 7.24 (AT&T weekly loss data). Suppose we have an investment inAT&T
stock and want to model weekly losses in value using an unconditional approach. If
--- page 297 ---

7.2. Threshold Exceedances
281
1980
1982
1984
1986
1988
1990
50
100
150
200
250
•••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••• • • •
•
•
•
•
•
100
120
Threshold
Mean excess
••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••
••
•
10
50
100
0
0.2
0.4
0.6
0.8
1.0
x (log scale)
0
80
60
60
40
40
50
30
20
20
10
0
0
(a)
(b)
(c)
Fu(x − u)
Figure 7.4.
(a) Time series plot of the Danish data. (b) Sample mean excess plot.
(c) Empirical distribution of excesses and ﬁtted GPD. See Example 7.23 for full details.
Xt denotes the weekly log-return, then the percentage loss in value of our position
over a week is given by Lt = 100(1 −exp(Xt)) and data on this loss for the 521
complete weeks in the period 1991–2000 are shown in Figure 7.5(a).
A sample mean excess plot of the positive loss values is shown in Figure 7.5(b)
and this suggests that a threshold can be found above which a GPD approximation to
the excess distribution should be possible. We have chosen to position the threshold
at a loss value of 2.75%, which is marked by a vertical line on the plot and gives
102 exceedances.
We observed in Section 4.1 that monthlyAT&T return data over the period 1993–
2000 do not appear consistent with a strict white noise hypothesis, so the issue of
whether excess losses can be modelled as independent is relevant. This issue is taken
--- page 298 ---

282
7. Extreme Value Theory
1992
1994
1996
1998
2000
−20
−15
−10
−5
10
15
20
••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••
••
••
•
•
•
•
•
•
• •
•
0
10
15
Threshold
••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••• •
•• • •
10
20
30
0
0.2
0.4
0.6
0.8
1.0
x (log scale)
0
5
3
4
5
6
5
(b)
(c)
Mean excess
Fu(x − u)
(a)
Figure 7.5.
(a) Time series plot of AT&T weekly percentage loss data. (b) Sample mean
excess plot. (c) Empirical distribution of excesses and ﬁtted GPD. See Example 7.24 for full
details.
up in Section 7.4 but for the time being we ignore it and implement a standard ML
approach to estimating the parameters of a GPD model for the excess distribution;
we obtain the estimates ˆξ = 0.22 and ˆβ = 2.1 with standard errors 0.13 and 0.34,
respectively. Thus the model we have ﬁtted is a model that is close to having an
inﬁnite fourth moment.A picture of the ﬁtted GPD model for the excess distribution
ˆFu(x −u) is also given in Figure 7.5(c), superimposed on points plotted at empirical
estimates of the excess probabilities for each loss.
7.2.3
Modelling Tails and Measures of Tail Risk
In this section we describe how the GPD model for the excess losses is used to
estimate the tail of the underlying loss distribution F and associated risk measures.
To make the necessary theoretical calculations we again make Assumption 7.21.
--- page 299 ---

7.2. Threshold Exceedances
283
Tailprobabilitiesandriskmeasures.
WeobserveﬁrstlythatunderAssumption7.21
we have, for x ⩾u,
¯F(x) = P(X > u)P(X > x | X > u)
= ¯F(u)P(X −u > x −u | X > u)
= ¯F(u) ¯Fu(x −u)
= ¯F(u)

1 + ξ x −u
β
−1/ξ
,
(7.17)
which, if we know F(u), gives us a formula for tail probabilities. This formula
may be inverted to obtain a high quantile of the underlying distribution, which we
interpret as a VaR. For α ⩾F(u) we have that VaR is equal to
VaRα = qα(F) = u + β
ξ
1 −α
¯F(u)
−ξ
−1

.
(7.18)
Assuming that ξ < 1 the associated expected shortfall can be calculated easily
from (2.23) and (7.18). We obtain
ESα =
1
1 −α
 1
α
qx(F) dx = VaRα
1 −ξ + β −ξu
1 −ξ .
(7.19)
Note that Assumption 7.21 and Lemma 7.22 imply that excess losses above VaRα
have a GPD distribution satisfying FVaRα = Gξ,β+ξ(VaRα −u). The expected shortfall
estimator in (7.19) can also be obtained by adding the mean of this distribution to
VaRα,i.e.ESα = VaRα +e(VaRα),wheree(VaRα)isgivenin(7.15).Itisinteresting
to look at how the ratio of the two risk measures behaves for large values of the
quantile probability α. It is easily calculated from (7.18) and (7.19) that
lim
α→1
ESα
VaRα
=

(1 −ξ)−1,
ξ ⩾0,
1,
ξ < 0,
(7.20)
so the shape parameter ξ of the GPD effectively determines the ratio when we go
far enough out into the tail.
Estimation in practice.
We note that, under Assumption 7.21, tail probabilities,
VaRs and expected shortfalls are all given by formulas of the form g(ξ, β, ¯F(u)).
Assuming that we have ﬁtted a GPD to excess losses over a threshold u, as described
in Section 7.2.2, we estimate these quantities by ﬁrst replacing ξ and β in formulas (7.17)–(7.19) by their estimates. Of course, we also require an estimate of ¯F(u)
andherewetakethesimpleempiricalestimatorNu/n.Indoingthis,weareimplicitly
assuming that there is a sufﬁcient proportion of sample values above the threshold
u to estimate ¯F(u) reliably. However, we hope to gain over the empirical method by
using a kind of extrapolation based on the GPD for more extreme tail probabilities
and risk measures. For tail probabilities we obtain an estimator, ﬁrst proposed by
Smith (1987), of the form
ˆ¯F(x) = Nu
n

1 + ˆξ x −u
ˆβ
−1/ˆξ
,
(7.21)
--- page 300 ---

284
7. Extreme Value Theory
which we stress is only valid for x ⩾u. For α ⩾1 −Nu/n we obtain analogous
point estimators of VaRα and ESα from (7.18) and (7.19).
Of course we would also like to obtain conﬁdence intervals. If we have taken the
likelihood approach to estimating ξ and β, then it is quite easy to give conﬁdence
intervals for g(ˆξ, ˆβ, Nu/n) that take into account the uncertainty in ˆξ and ˆβ, but
neglect the uncertainty in Nu/n as an estimator of ¯F(u). We use the approach
described at the end of Section 7.1.4 for return levels, whereby the GPD model is
reparametrized in terms of φ = g(ξ, β, Nu/n) and a conﬁdence interval for ˆφ is
constructed based on the likelihood ratio test as in Section A.3.5.
Example 7.25 (risk measures forAT&T loss data). Suppose we have ﬁtted a GPD
model to excess weekly losses above the threshold u = 2.75% as in Example 7.24.
We use this model to obtain estimates of the 99% VaR and expected shortfall of the
underlying weekly loss distribution. The essence of the method is displayed in Figure 7.6; this is a plot of estimated tail probabilities on logarithmic axes, with various
dotted lines superimposed to indicate the estimation of risk measures and associated
conﬁdence intervals. The points on the graph are the 102 threshold exceedances and
are plotted at y-values corresponding to the tail of the empirical distribution function;
the smooth curve running through the points is the tail estimator (7.21).
Estimation of the 99% quantile amounts to determining the point of intersection of
the tail estimation curve and the horizontal line ¯F(x) = 0.01 (not marked on graph);
the ﬁrst vertical dotted line shows the quantile estimate. The horizontal dotted line
aids in the visualization of a 95% conﬁdence interval for the VaR estimate; the
degree of conﬁdence is shown on the alternative y-axis to the right of the plot.
The boundaries of a 95% conﬁdence interval are obtained by determining the two
points of intersection of this horizontal line with the dotted curve, which is a proﬁle
likelihood curve for the VaR as a parameter of the GPD model and is constructed
using likelihood ratio test arguments as in Section A.3.5. Dropping the horizontal
line to the 99% mark would correspond to constructing a 99% conﬁdence interval
for the estimate of the 99% VaR. The point estimate and 95% conﬁdence interval
for the 99% quantile are estimated to be 11.7% and (9.6, 16.1).
The second vertical line on the plot shows the point estimate of the 99% expected
shortfall. A 95% conﬁdence interval is determined from the dotted horizontal line
and its points of intersection with the second dotted curve. The point estimate and
95% conﬁdence interval are 17.0% and (12.7, 33.6). Note that if we divide the point
estimates of the shortfall and the VaR we get 17/11.7 ≈1.45, which is larger than
the asymptotic ratio (1 −ˆξ)−1 = 1.29 suggested by (7.20); this is generally the case
at ﬁnite levels and is explained by the second term in (7.19) being a non-negligible
positive quantity.
Before leaving the topic of GPD tail modelling it is clearly important to see how
sensitive our risk-measure estimates are to the choice of the threshold. Hitherto we
have considered single choices of threshold u and looked at a series of incremental
calculations that always build on the same GPD model for excesses over that threshold. We would hope that there is some robustness to our inference for different
choices of threshold.
--- page 301 ---

7.2. Threshold Exceedances
285
••••••••••••••••••••••••••••••••••••••••••••••••••••••••• ••••••••• •
•
•
•
•
10
20
30
40
x (log scale)
1 − F(x) (log scale)
99
95
5 × 10−2
5 × 10−3
5 × 10−4
Figure 7.6.
The smooth curve through the points shows the estimated tail of the AT&T
weekly percentage loss data using the estimator (7.21). Points are plotted at empirical tail
probabilities calculated from empirical df. The vertical dotted lines show estimates of 99%
VaR and expected shortfall. The other curves are used in the construction of conﬁdence
intervals. See Example 7.25 for full details.
Example 7.26 (varying the threshold). In the case of the AT&T weekly loss data
the inﬂuence of different thresholds is investigated in Figure 7.7. Given the importance of the ξ parameter in determining the weight of the tail and the relationship
between quantiles and expected shortfalls, we ﬁrst show how estimates of ξ vary
as we consider a series of thresholds that give us between 20 and 150 exceedances.
In fact, the estimates remain fairly constant around a value of approximately 0.2; a
symmetric 95% conﬁdence interval constructed from the standard error estimate is
also shown, and indicates how the uncertainty about the parameter value decreases
as the threshold is lowered or the number of threshold exceedances is increased.
Point estimates of the 99% VaR and expected shortfall estimates are also shown.
The former remain remarkably constant around 12%, while the latter show modest
variability that essentially tracks the variability of the ξ estimate. These pictures
provide some reassurance that different thresholds do not lead to drastically different
conclusions. We return to the issue of threshold choice again in Section 7.2.5.
--- page 302 ---

286
7. Extreme Value Theory
20
40
60
80
100
120
140
−0.4
0
0.4
6.74
4.80
3.74
3.16
2.62
2.23
1.80
Exceedances
Shape (   ) (CI, p = 0.95)
Threshold
20
40
60
80
100
120
140
12
14
16
18
6.74
4.80
3.74
3.16
2.62
2.23
1.80
Exceedances
Percentage loss
Threshold
ξ
(a)
(b)
Figure 7.7.
(a) Estimate of ξ for different thresholds u and numbers of exceedances Nu,
together with a 95% conﬁdence interval based on the standard error. (b) Associated point
estimates of the 99% VaR (solid line) and expected shortfall (dotted line). See Example 7.26
for commentary.
7.2.4
The Hill Method
The GPD method is not the only way to estimate the tail of a distribution and, as an
alternative, we describe in this section the well-known Hill approach to modelling
the tails of heavy-tailed distributions.
Estimating the tail index.
For this method we assume that the underlying loss
distribution is in the maximum domain of attraction of the Fr´echet distribution so
that, by Theorem 7.8, it has a tail of the form
¯F(x) = L(x)x−α,
(7.22)
for a slowly varying function L (see Deﬁnition 7.7) and a positive parameter α.
Traditionally, in the Hill approach, interest centres on the tail index α, rather than
its reciprocal ξ, which appears in (7.3). The goal is to ﬁnd an estimator of α based
on identically distributed data X1, . . . , Xn.
--- page 303 ---

7.2. Threshold Exceedances
287
The Hill estimator can be derived in various ways (see EKM, pp. 330–336).
Perhaps the most elegant is to consider the mean excess function of the generic
logarithmic loss ln X, where X is an rv with df (7.22). Writing e∗for the mean
excess function of ln X and using integration by parts we ﬁnd that
e∗(ln u) = E(ln X −ln u | ln X > ln u)
=
1
¯F(u)
 ∞
u
(ln x −ln u) dF(x)
=
1
¯F(u)
 ∞
u
¯F(x)
x
dx
=
1
¯F(u)
 ∞
u
L(x)x−(α+1) dx.
For u sufﬁciently large, the slowly varying function L(x) for x ⩾u can essentially be
treated as a constant and taken outside the integral. More formally, using Karamata’s
Theorem (see Section A.1.3), we get, for u →∞,
e∗(ln u) ∼L(u)u−αα−1
¯F(u)
= α−1,
so limu→∞αe∗(ln u) = 1. We expect to see similar tail behaviour in the sample
mean excess function e∗
n (see (7.16)) constructed from the log observations. That
is, we expect that e∗
n(ln Xk,n) ≈α−1 for n large and k sufﬁciently small, where
Xn,n ⩽· · · ⩽X1,n are the order statistics as usual. Evaluating e∗
n(ln Xk,n) gives us
the estimator ˆα−1 = ((k −1)−1 k−1
j=1 ln Xj,n −ln Xk,n). The standard form of the
Hill estimator is obtained by a minor modiﬁcation:
ˆα(H)
k,n =
1
k
k

j=1
ln Xj,n −ln Xk,n
−1
,
2 ⩽k ⩽n.
(7.23)
The Hill estimator is one of the best-studied estimators in the EVT literature. The
asymptotic properties (consistency, asymptotic normality) of this estimator (as sample size n →∞, number of extremes k →∞and the so-called tail-fraction
k/n →0) have been extensively investigated under various assumed models for the
data, including ARCH and GARCH (see Notes and Comments). We concentrate on
the use of the estimator in practice and, in particular, on its performance relative to
the GPD estimation approach.
When the data are from a distribution with a tail that is close to a perfect power
function, the Hill estimator is often a good estimator of α, or its reciprocal ξ. In
practice, the general strategy is to plot Hill estimates for various values of k. This
gives the Hill plot {(k, ˆα(H)
k,n ) : k = 2, . . . , n}. We hope to ﬁnd a stable region in the
Hill plot where estimates constructed from different numbers of order statistics are
quite similar.
Example 7.27 (Hill plots). We construct Hill plots for the Danish ﬁre data of Example 7.23 and the weekly percentage loss data (positive values only) of Example 7.24
(shown in Figure 7.8).
--- page 304 ---

288
7. Extreme Value Theory
100
150
200
250
10
20
30
40
50
60
0
500
1000
1500
2000
10
20
30
40
50
60
50
0
10.60
2.99
1.32
0
10.60 7.75
5.39
4.23
5.62 3.98
1.77 1.46 1.20 1.00
56.2 29.0 25.0 20.8
16.9
0
2
4
6
8
10
12
0
2
4
6
8
10
12
0.5
1.5
2.5
0
1.0
2.0
3.0
0.5
1.5
2.5
0
1.0
2.0
3.0
(a)
(b)
(c)
(d)
Figure 7.8.
Hill plots showing estimates of the tail index α = 1/ξ for (a), (b) the AT&T
weekly percentages losses and (c), (d) the Danish ﬁre loss data. Parts (b) and (d) are expanded
versions of sections of (a) and (c) showing Hill estimates based on up to 60 order statistics.
It is very easy to construct the Hill plot for all possible values of k, but it can be
misleading to do so; practical experience (see Example 7.28) suggests that the best
choices of k are relatively small—say 10–50 order statistics in a sample of size 1000.
For this reason we have enlarged sections of the Hill plots showing the estimates
obtained for values of k less than 60.
For the Danish data the estimates of α obtained are between 1.5 and 2, suggesting ξ
estimates between 0.5 and 0.67, all of which correspond to inﬁnite-variance models
for these data. Recall that the estimate derived from our GPD model in Example 7.23
was ˆξ = 0.50. For the AT&T data there is no particularly stable region in the plot.
The α estimates based on k = 2, . . . , 60 order statistics mostly range from 2 to 4,
suggesting a ξ value in the range 0.25–0.5, which is larger than the values estimated
in Example 7.26 with a GPD model.
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
