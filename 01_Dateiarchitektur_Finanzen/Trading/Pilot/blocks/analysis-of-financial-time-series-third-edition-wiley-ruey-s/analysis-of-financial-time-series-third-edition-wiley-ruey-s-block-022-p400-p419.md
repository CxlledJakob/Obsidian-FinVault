# Analysis of Financial Time Series, Third Edition (Wiley -- Ruey S_ Tsay -- Wiley series in probability and statistics, 3rd ed_, -- John Wiley & Sons, -- isbn13 9780470414354 -- 9f99b80c7b2dedd477f463dc5323f3b6 -- An.pdf — pages 400–419

--- page 400 ---

new approach based on the extreme value theory
373
Distribution of Excesses
Under the two-dimensional Poisson process model considered, the conditional distribution of the excess xt = rt −η over the threshold η is a GPD with shape
parameter ξt and scale parameter ψt = αt + ξt(η −βt). Therefore, we can make
use of the relationship between a standard exponential distribution and GPD, and
deﬁne
wti =



1
ξti ln

1 + ξti
rti −η
ψti

+
if ξti̸ = 0,
rti −η
ψti
if ξti = 0.
(7.43)
If the model is adequate, {wti} are independent and exponentially distributed with
mean 1; see also Smith (1999). We can then apply the QQ plot to check the validity
of the GPD assumption for excesses.
Independence
A simple way to check the independence assumption, after adjusting for the effects
of explanatory variables, is to examine the sample autocorrelation functions of zti
and wti. Under the independence assumption, we expect that both zti and wti have
no serial correlations.
7.7.8
An Illustration
In this section, we apply a two-dimensional inhomogeneous Poisson process model
to the daily log returns, in percentages, of IBM stock from July 3, 1962, to
December 31, 1998. We focus on holding a long position of $10 million. The
analysis enables us to compare the results with those obtained before by using
other approaches to calculating VaR.
We begin by pointing out that the two-dimensional homogeneous model of
Example 7.7 needs further reﬁnements because the ﬁtted model fails to pass the
model checking statistics of the previous section. Figures 7.8(a) and 7.8(b) show
the autocorrelation functions of the statistics zti and wti, deﬁned in Eqs. (7.42) and
(7.43), of the homogeneous model when the threshold is η = 2.5%. The horizontal
lines in the plots denote asymptotic limits of two standard errors. It is seen that both
zti and wti series have some signiﬁcant serial correlations. Figures 7.9(a) and 7.9(b)
show the QQ plots of the zti and wti series. The straight line in each plot is the
theoretical line, which passes through the origin and has a unit slope under the
assumption of a standard exponential distribution. The QQ plot of zti shows some
discrepancy.
To reﬁne the model, we use the mean-corrected log return series
ro
t = rt −¯r,
¯r =
1
9190
9190

t=1
rt,
--- page 401 ---

374
extreme values, quantiles, and value at risk
Lag
(a)
ACF
1
2
3
4
5
6
7
8
9
10
−0.4
0.0 0.2 0.4
Lag
(c)
ACF
1
2
3
4
5
6
7
8
9
10
−0.4
0.0 0.2 0.4
Lag
(b)
ACF
1
2
3
4
5
6
7
8
9
10
−0.4
0.0 0.2 0.4
Lag
(d)
ACF
1
2
3
4
5
6
7
8
9
10
−0.4
0.0 0.2 0.4
Figure 7.8
Sample autocorrelation functions of the z and w measures for two-dimensional Poisson
models. Parts (a) and (b) are for homogeneous model and parts (c) and (d) are for inhomogeneous
model. Data are daily mean-corrected log returns, in percentages, of IBM stock from July 3, 1962, to
December 31, 1998, and the threshold is 2.5%. A long ﬁnancial position is used.
where rt is the daily log return in percentages, and employ the following explanatory variables:
1. x1t: an indicator variable for October, November, and December. That is,
x1t = 1 if t is in October, November, or December. This variable is chosen
to take care of the fourth-quarter effect (or year-end effect), if any, on the
daily IBM stock returns.
2. x2t: an indicator variable for the behavior of the previous trading day. Specifically, x2t = 1 if and only if the log return ro
t−1 ≤−2.5%. Since we focus on
holding a long position with threshold 2.5%, an exceedance occurs when the
daily price drops over 2.5%. Therefore, x2t is used to capture the possibility
of panic selling when the price of IBM stock dropped 2.5% or more on the
previous trading day.
3. x3t: a qualitative measurement of volatility, which is the number of days
between t −1 and t −5 (inclusive) that has a log return with magnitude
exceeding the threshold. In our case, x3t is the number of ro
t−i satisfying
|ro
t−i| ≥2.5% for i = 1, . . . , 5.
4. x4t: an annual trend deﬁned as x4t = (year of time t −1961)/38. This variable is used to detect any trend in the behavior of extreme returns of IBM
stock.
--- page 402 ---

new approach based on the extreme value theory
375
5. x5t: a volatility series based on a Gaussian GARCH(1,1) model for the
mean-corrected series ro
t . Speciﬁcally, x5t = σt, where σ 2
t is the conditional
variance of the GARCH(1,1) model
ro
t = at,
at = σtϵt,
ϵt ∼N(0, 1),
σ 2
t = 0.04565 + 0.0807a2
t−1 + 0.9031σ 2
t−1.
These ﬁve explanatory variables are all available at time t −1. We use two volatility measures (x3t and x5t) to study the effect of market volatility on VaR. As
shown in Example 7.3 by the ﬁtted AR(2)–GARCH(1,1) model, the serial correlations in rt are weak so that we do not entertain any ARMA model for the mean
equation.
Using the prior ﬁve explanatory variables and deleting insigniﬁcant parameters,
we obtain the estimation results shown in Table 7.4. Figures 7.8(c) and 7.8(d)
and Figures 7.9(c) and 7.9(d) show the model checking statistics for the ﬁtted
two-dimensional inhomogeneous Poisson process model when the threshold is
η = 2.5%. All autocorrelation functions of zti and wti are within the asymptotic
two standard error limits. The QQ plots also show marked improvements as they
•••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••• •
•
•
•
exp
(a)
hz
0
1
2
3
4
5
6
0
5
10
15
••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••• • • •
•
hw
•••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••• •
• •
•
ihz
0
2
4
6
••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••
• •
•
•
ihw
0
2
4
6
8
exp
(c)
0
1
2
3
4
5
6
exp
(d)
0
1
2
3
4
5
6
exp
(b)
0
1
2
3
4
5
6
0
2
4
6
8
Figure 7.9
Quantile-to-quantile plot of z and w measures for two-dimensional Poisson models. Parts
(a) and (b) are for homogeneous model and parts (c) and (d) are for inhomogeneous model. Data are
daily mean-corrected log returns, in percentages, of IBM stock from July 3, 1962, to December 31,
1998, and the threshold is 2.5%. A long ﬁnancial position is used.
--- page 403 ---

376
extreme values, quantiles, and value at risk
TABLE 7.4
Estimation Results of Two-Dimensional Inhomogeneous Poisson Process
Model for Daily Log Returns, in Percentages, of IBM Stock from July 3, 1962 to
December 31, 1998a
Parameter
Constant
Coefﬁcient of x3t
Coefﬁcient of x4t
Coefﬁcient of x5t
Threshold 2.5% with 334 Exceedances
βt
0.3202
1.4772
2.1991
(Std.err)
(0.3387)
(0.3222)
(0.2450)
ln(αt)
−0.8119
0.3305
1.0324
(Std.err)
(0.1798)
(0.0826)
(0.2619)
ξt
0.1805
0.2118
0.3551
−0.2602
(Std.err)
(0.1290)
(0.0580)
(0.1503)
(0.0461)
Threshold 3.0% with 184 Exceedances
βt
1.1569
2.1918
(Std.err)
(0.4082)
(0.2909)
ln(αt)
−0.0316
0.3336
(Std.err)
(0.1201)
(0.0861)
ξt
0.6008
0.2480
−0.3175
(Std.err)
(0.1454)
(0.0731)
(0.0685)
aFour explanatory variables deﬁned in the text are used. The model is for holding a long position on
IBM stock. The sample mean of the log returns is removed from the data.
indicate no model inadequacy. Based on these checking results, the inhomogeneous
model seems adequate.
Consider the case of threshold 2.5%. The estimation results show the following:
1. All three parameters of the intensity function depend signiﬁcantly on the
annual time trend. In particular, the shape parameter has a negative annual
trend, indicating that the log returns of IBM stock are moving farther away
from normality as time passes. Both the location and scale parameters
increase over time.
2. Indicators for the fourth quarter, x1t, and for panic selling, x2t, are not signiﬁcant for all three parameters.
3. The location and shape parameters are positively affected by the volatility of
the GARCH(1,1) model; see the coefﬁcients of x5t. This is understandable
because the variability of log returns increases when the volatility is high.
Consequently, the dependence of log returns on the tail index is reduced.
4. The scale and shape parameters depend signiﬁcantly on the qualitative measure of volatility. Signs of the estimates are also plausible.
The explanatory variables for December 31, 1998, assumed the values x3,9190 =
0, x4,9190 = 0.9737, and x5,9190 = 1.9766. Using these values and the ﬁtted model
--- page 404 ---

the extremal index
377
in Table 7.4, we obtain
ξ9190 = 0.01195,
ln(α9190) = 0.19331,
β9190 = 6.105.
Assume that the tail probability is 0.05. The VaR quantile shown in Eq. (7.36) gives
VaR = 3.03756%. Consequently, for a long position of $10 million, we have
VaR = $10,000,000 × 0.0303756 = $303,756.
If the tail probability is 0.01, the VaR is $497, 425. The 5% VaR is slightly larger
than that of Example 7.3, which uses a Gaussian AR(2)–GARCH(1,1) model. The
1% VaR is larger than that of Case 1 of Example 7.3. Again, as expected, the
effect of extreme values (i.e., heavy tails) on VaR is more pronounced when the
tail probability used is small.
An advantage of using explanatory variables is that the parameters are adaptive
to the change in market conditions. For example, the explanatory variables for
December 30, 1998, assumed the values x3,9189 = 1, x4,9189 = 0.9737, and x5,9189 =
1.8757. In this case, we have
ξ9189 = 0.2500,
ln(α9189) = 0.52385,
β9189 = 5.8834.
The 95% quantile (i.e., the tail probability is 5%) then becomes 2.69139%. Consequently, the VaR is
VaR = $10,000,000 × 0.0269139 = $269,139.
If the tail probability is 0.01, then VaR becomes $448, 323. Based on this example,
the homogeneous Poisson model shown in Example 7.8 seems to underestimate
the VaR.
7.8
THE EXTREMAL INDEX
So far our discussions of extreme values are based on the assumption that the
data are iid random variables. However, in reality extremal events tend to occur in
clusters because of the serial dependence in the data. For instance, we often observe
large returns (both positive and negative) of an asset after some news event. In this
section we extend the theory and applications of extreme values to cases in which
the data form a strictly stationary time series. The basic concept of the extension
is extremal index, which allows one to characterize the relationship between the
dependence structure of the data and their extremal behavior. Our discussion will
be brief. Interested readers are referred to Beirlant et al. (2004, Chapter 10) and
Embrechts et al. (1997).
Let x1, x2, . . . be a strictly stationary sequence of random variables with marginal
distribution function F(x). Consider the case of n observations {xi|i = 1, . . . , n}.
--- page 405 ---

378
extreme values, quantiles, and value at risk
As before, let x(n) be the maximum of the data, that is, x(n) = max{xi}. We seek
the limiting distribution of (x(n) −βn)/αn for some suitably chosen normalizing
constants αn > 0 and βn. If {xi} were iid, Section 7.5 shows that the only possible nondegenerate limits are the extreme value distributions. What is the limiting
distribution when {xi} are serially dependent?
To answer this question, we start with a heuristic argument. Suppose that the
serial dependence of the stationary series xi decays quickly so that xi and xi+ℓare
essentially independent when ℓis sufﬁciently large. In other words, assume that the
long-range dependence of xi vanishes quickly. Now divide the data into disjoint
blocks of size k. Speciﬁcally, let g = [n/k] be the largest integer less than or equal
to n/k. The ith block of the data is then {xj|j = (i −1) ∗k + 1, . . . , i ∗k}, where
it is understood that the (g + 1)th block may contain less than k observations.
Let xk,i be the maximum of the ith block, that is, xk,i = max{xj|j = (i −1) ∗k +
1, . . . , i ∗k}. The collection of block maxima is {xk,i|i = 1, . . . , g + 1}. From the
deﬁnitions, it is easy to see that
x(n) =
max
i=1,...,g+1 xk,i.
(7.44)
That is, the sample maximum is also the maximum of the block maxima. If the
block size k is sufﬁciently large and the block maximum xk,i does not occur near
the end of the ith block, then xk,i and xk,i+1 are sufﬁciently far apart and essentially independent under the assumption of weak long-range dependence in {xi}.
Consequently, {xk,i|i = 1, . . . , g + 1} can be regarded as a sample of iid random
variables, and the limiting distribution of its maximum, which is x(n), should be
the extreme value distribution. The prior discussion shows that, under some proper
condition, the limiting distribution of the maximum of a strictly stationary time
series is also the extreme value distribution.
The proper condition needed for the maximum x(n) of a strictly stationary time
series to have the extreme value limiting distribution is obtained by Leadbetter
(1974) and known as the D(un) condition. Details are given in the next section.
The prior heuristic argument also suggests that, even though the limiting distribution of x(n) is also the extreme value distribution, the parameters associated with
the limiting distribution, however, will not be the same as those when {xi} are iid
random samples because the limiting distribution depends on the marginal distribution of the underlying sequences. For the iid sequences, the marginal distribution
is F(x), but for a stationary series the underlying sequences are the block maxima xk,i whose marginal distribution is not F(x). The marginal distribution of xk,i
depends on k and the strength of serial dependence in {xi}.
7.8.1
The D(un) Condition
Consider the sample x1, x2, . . . , xn. To place limits on the long-range dependence
of {xi}, let un be a sequence of thresholds increasing at a rate for which the expected
number of exceedances of xi over un remains bounded. Mathematically, this says
that lim sup n[1 −F(un)] < ∞, where F(·) is the marginal cumulative distribution
--- page 406 ---

the extremal index
379
function of xi. For any positive integers p and q, suppose that iv (v = 1, . . . , p)
and jt (t = 1, . . . , q) are arbitrary integers satisfying
1 ≤i1 < i2 < · · · < ip < j1 < · · · < jq ≤n,
where j1 −ip ≥ℓn, where ℓn is a function of the sample size n such that ℓn/n →0
as n →∞. Let A1 = {i1, i2, . . . , ip} and A2 = {j1, j2, . . . , jq} be two sets of time
indices. From the prior condition, elements in A1 and A2 are separated by at least
ℓn time periods. The condition D(un) is satisﬁed if
|P ( max
i∈A1∪A2
xi ≤un) −P (max
i∈A1
xi ≤un)P (max
i∈A2
xi ≤un)| ≤δn,ℓn,
(7.45)
where δn,ℓn →0 as n →∞. This condition says that any two events of the form
{maxi∈A1 xi ≤un} and {maxi∈A2 xi ≤un} can become asymptotically independent
as the sample size n increases when the index subsets A1 and A2 of {1, 2, . . . , n}
are separated by a distance ℓn which satisﬁes ℓn/n →0 as n →∞. The D(un)
condition looks complicated, but it is relatively weak. For instance, consider Gaussian sequences with autocorrelation ρn for lag n. The D(un) condition is satisﬁed
if ρn ln(n) →0 as n →∞; see Berman (1964).
Leadbetter’s Theorem 1.
Suppose that {xi|i = 1, . . . , n} is a strictly stationary time series for which there exist sequences of constants αn > 0 and βn and a
nondegenerate distribution function F∗(·) such that
P

x(n) −βn
αn
≤x

→d F∗(x),
n →∞,
where →d denotes convergence in distribution. If D(un) holds with un = αnx + βn
for each x such that F∗(x) > 0, then F∗(x) is an extreme value distribution function.
The prior theorem shows that the possible limiting distributions for the maxima
of strictly stationary time series satisfying the D(un) condition are also the extreme
value distributions. As noted before, the dependence can affect the limiting distribution, however. The effect of the dependence appears in the marginal distribution
of the block maxima xk,i. To state the effect more precisely, let {˜x1, ˜x2, . . . , ˜xn}
be a sequence of iid random variables such that the marginal distribution of ˜xi is
the same as that of the stationary time series xi. Let ˜x(n) be the maximum of {˜xi}.
Leadbetter (1983) establishes the following result.
Leadbetter’s Theorem 2.
If there exist sequences of constants αn > 0 and βn
and a nondegenerate distribution function ˜F∗(x) such that
P

 ˜x(n) −βn
αn
≤x

→d ˜F∗(x),
n →∞,
--- page 407 ---

380
extreme values, quantiles, and value at risk
if the condition D(un) holds with un = αnx + βn for each x such that ˜F∗(x) > 0,
and if P [(x(n) −βn)/αn ≤x] converges for some x, then
P

x(n) −βn
αn
≤x

→d F∗(x) = ˜F θ
∗(x),
n →∞,
for some constant θ ∈(0, 1].
The constant θ is called the extremal index. It plays an important role in determining the limiting distribution F∗(x) for the maximum of a strictly stationary time
series. To see this, we provide some simple derivations for the case of ξ̸ = 0. From
the result of Eq. (7.16), ˜F∗(x) is the generalized extreme value distribution and
assumes the form
˜F∗(x) = exp

−

1 + ξ x −β
α
	−1/ξ
,
where ξ̸ = 0 and 1 + ξ(x −β)/α > 0. In other words, we assume that for the iid
sequence {˜xi}, the limiting extreme distribution of ˜x(n) has parameters ξ, β and α.
Based on Theorem 2 of Leadbetter (1983), we have
F∗(x) = ˜F θ
∗(x) = exp

−θ

1 + ξ x −β
α
	−1/ξ
= exp

−
 1
θξ + ξ x −β
αθξ
	−1/ξ
= exp

−

ξ α/ξ + x −β
αθξ
	−1/ξ
= exp

−

1 + ξ x −β + α/ξ −αθξ/ξ
αθξ
	−1/ξ
= exp

−

1 + ξ
x −[β −α
ξ (1 −θξ)]
αθξ
−1/ξ

= exp

−

1 + ξ∗
x −β∗
α∗
	−1/ξ∗
,
(7.46)
where ξ∗= ξ, α∗= αθξ, and β∗= β −α(1 −θξ)/ξ. Therefore, for a stationary
time series {xi} satisfying the D(un) condition, the limiting distribution of the
sample maximum is the generalized extreme value distribution with the shape
parameter ξ, which is the same as that of the iid sequences. On the other hand, the
location and scale parameters are affected by the extremal index θ. Speciﬁcally,
α∗= αθξ and β∗= β −α(1 −θξ)/ξ. Results for the case of ξ = 0 can be derived
via the same approach and we have α∗= α and β∗= β + α ln(θ).
--- page 408 ---

the extremal index
381
A formal deﬁnition of the extremal index is as follows: Let {xi} be a strictly
stationary time series with marginal cumulative distribution function F(x) and θ
a nonnegative number. Assume that for every τ > 0 there exists a sequence of
thresholds un such that
lim
n→∞n[1 −F(un)] = τ,
(7.47)
lim
n→∞P (x(n) ≤un) = exp(−θτ).
(7.48)
Then θ is called the extremal index of the time series {xi}. See Embrechts et al.
(1997). Note that, for the corresponding iid sequence {˜xi}, under the assumption
that Eq. (7.47) holds, we have
lim
n→∞P (˜x(n) ≤un) = lim
n→∞[F(un)]n = lim
n→∞

1 −1
nn[1 −F(un)]
"n
→exp(−τ),
where we have used the property limn→∞(1 −y/n)n = exp(−y). Thus, the deﬁ-
nition also highlights the role played by the extremal index θ.
7.8.2
Estimation of the Extremal Index
There are several ways to estimate the extremal index θ of a strictly stationary
time series {xi}. Each estimation method is associated with an interpretation of the
extremal index. In what follows, we discuss some of the estimation methods.
The Blocks Method
From the deﬁnition of the extremal index θ, we have, for a large n, that
P (x(n) ≤un) ≈P θ(˜x(n) ≤un) = [F(un)]nθ,
provided that n[1 −F(un)] →τ > 0. Hence
lim
n→∞
ln P (x(n) ≤un)
n ln F(un)
= θ.
(7.49)
This limiting relationship suggests a method to estimate θ. The denominator can
be estimated by the sample quantile, namely
ˆF(un) = 1
n
n

i=1
I (xi ≤un) = 1 −1
n
n

i=1
I (xi > un) = 1 −N(un)
n
,
where I (C) = 1 if the augment C holds and = 0 otherwise, that is, I (C) is the indicator variable for the statement C, and N(un) denotes the number of exceedances
of the sample over the threshold un. The numerator P (x(n) ≤un) is harder to estimate. One possibility is to use the block maxima. Speciﬁcally, let k = k(n) be a
--- page 409 ---

382
extreme values, quantiles, and value at risk
properly chosen block size that depends on the sample size n and, as before, let
g = [n/k] be the integer part of n/k. For simplicity, assume that n = gk. The ith
block consists of {xj|j = (i −1) ∗k + 1, . . . , i ∗k} and let xk,i be the maximum
of the ith block. Using Eq. (7.44) and the approximate independence of block
maxima, we have
P (x(n) ≤un) = P ( max
1≤i≤g xk,i ≤un) ≈[P (xk,i ≤un)]g.
The probability P (xk,i ≤un) can be estimated from the block maxima, that is,
ˆP (xk,i ≤un) = 1
g
g

i=1
I (xk,i ≤un) = 1 −1
g
g

i=1
I (xk,i > un) = 1 −G(un)
g
,
where G(un) is the number of blocks such that the block maximum exceeds the
threshold un. Combining the estimators for numerator and denominator, we obtain
ˆθ(1)
b
= g
n
ln[1 −G(un)/g]
ln[1 −N(un)/n] = 1
k
ln[1 −G(un)/g]
ln[1 −N(un)/n],
(7.50)
where the subscript b signiﬁes the blocks method. Note that N(un) is the number
of exceedances of the sample {xi} over the threshold un and G(un) is the number
of blocks with one or more exceedances. Using approximation based on Taylor
expansion of ln(1 −x), we obtain a second estimator:
ˆθ(2)
b
= 1
k
G(un)/g
N(un)/n = G(un)
N(un).
Based on the results of Hsing et al. (1988), this estimator can also be interpreted as
the reciprocal of the mean cluster size of the limiting compound Poisson process
N(un).
The Runs Method
O’Brien (1987) proved, under certain weak mixing condition, that
lim
n→∞P (x∗
(n) ≤un|x1 > un) = θ,
where x∗
(n) = max2≤i≤s xi, where s is a function of the sample size n satisfying
some growth conditions, including s →∞and s/n →0 as n →∞. See Beirlant
et al. (2004) and Embrechts et al. (1997) for details. This result has been used to
construct an estimator of θ based on runs:
ˆθ(3)
r
=
n−k
i=1 I (Ai,n)
n
i=1 I (xi > un) =
n−k
i=1 I (Ai,n)
N(un)
,
--- page 410 ---

the extremal index
383
where N(un) is the number of exceedances of the sample {xi} over the threshold
un, k is a function of n, and Ai,n = {xi > un, xi+1 ≤un, . . . , xi+k ≤un}. Note that
Ai,n denotes the event that an exceedance is followed by a run of k observations
below the threshold. Since k/n →0 as n →∞, we can write the runs estimator as
ˆθ(3)
r
≈(n −k)−1 n−k
i=1 I (Ai,n)
n−1N(un)
.
Finally, other estimators of θ are available in the literature. See, for instance, the
methods discussed in Beirlant et al. (2004). For demonstration, we consider, again,
the negative daily log returns of IBM stock from July 3, 1962, to December 31,
1998. Figure 7.10 shows the estimates of the extremal index for various thresholds
when the block size k = 10. We chose k = 10 because the daily log returns have
weak serial dependence. The estimates are based on the blocks method, that is,
ˆθ(1)
b . From the plot, we see that ˆθ(1)
b
≈0.82 for threshold 0.025. Indeed, a simple
direct calculation using k = 10 and threshold 0.025 gives ˆθ(1)
b
= 0.823. The plot
also shows that the estimate ˆθ(1)
b
of the extremal index might be sensitive to the
choices of threshold and block size k.
5
58
129 209 289 369 449 529 609 689 769 850
0.8
0.9
1.0
1.1
0.08520
0.02960
0.02280
0.01840
0.01460
0.01200
0.00716
K
theta (919 blocks of size 10)
Threshold
Figure 7.10
Estimates of extremal index for negative daily log returns of IBM stock from July 3,
1962, to December 31, 1998. Block size is k = 10 and lower horizontal axis of plot K denotes number
of blocks whose maximum exceeds threshold.
--- page 411 ---

384
extreme values, quantiles, and value at risk
7.8.3
Value at Risk for a Stationary Time Series
The relationship between F∗(x) of the maximum of a stationary time series and
˜F∗(x) of its iid counterpart established in Theorem 2 of Leadbetter (1983) can be
used to calculate the VaR of a ﬁnancial position when the associated log returns
form a stationary time series. Speciﬁcally, from P (x(n) ≤un) ≈[F(x)]nθ, the (1 −
p)th quantile of F(x) is the (1 −p)nθth quantile of the limiting extreme value
distribution of x(n). Consequently, the VaR of Eq. (7.28) based on the extreme
value theory becomes
VaR =

βn −αn
ξn
2
1 −
0
−nθ ln(1 −p)
1−ξn3
if ξn̸ = 0
βn −αn ln[−nθ ln(1 −p)]
if ξn = 0,
(7.51)
where n is the length of the subperiod. From the formula, we risk underestimating
the VaR if the extremal index is overlooked.
As an illustration, again consider the negative daily log returns of IBM stock
from July 3, 1962, to December 31, 1998. Using ˆθ(1)
b
= 0.823, the 1% VaR for the
long position of $10 millions on the stock for the next trading day becomes 3.2714
for the case of choosing n = 63 days in parameter estimation. As expected, this is
higher than the 3.0497 of Example 7.6 when the extremal index is neglected.
R Demonstration
> library(evir)
> help(exindex)
> m1=exindex(nibm,10) %Estimate the extremal index
of Figure 7.10.
>
% VaR calculation.
> 2.583-(.945/.335)*(1-(-63*.823*log(.99))^-.335)
[1] 3.271388
EXERCISES
7.1. Consider the daily returns of GE stock from January 2, 1998, to December 31,
2008. The data can be obtained from CRSP or the ﬁle d-ge9808.txt. Convert
the simple returns into log returns. Suppose that you hold a long position on
the stock valued at $1 million. Use the tail probability 0.01. Compute the
value at risk of your position for 1-day horizon and 15-day horizon using the
following methods:
(a) The RiskMetrics method.
(b) A Gaussian ARMA–GARCH model.
(c) An ARMA–GARCH model with a Student-t distribution. You should also
estimate the degrees of freedom.
(d) The traditional extreme value theory with subperiod length n = 21.
--- page 412 ---

exercises
385
7.2. The ﬁle d-csco9808.txt contains the daily simple returns of Cisco Systems
stock from 1998 to 2008 with 2767 observations. Transform the simple returns
to log returns. Suppose that you hold a long position of Cisco stock valued
at $1 million. Compute the value at risk of your position for the next trading
day using probability p = 0.01.
(a) Use the RiskMetrics method.
(b) Use a GARCH model with a conditional Gaussian distribution.
(c) Use a GARCH model with a Student-t distribution. You may also estimate
the degrees of freedom.
(d) Use the unconditional sample quantile.
(e) Use a two-dimensional homogeneous Poisson process with threshold 2%,
that is, focusing on the exceeding times and exceedances that the daily
stock price drops 2% or more. Check the ﬁtted model.
(f) Use a two-dimensional nonhomogeneous Poisson process with threshold
2%. The explanatory variables are (1) an annual time trend, (2) a dummy
variable for October, November, and December, and (3) a ﬁtted volatility
based on a Gaussian GARCH(1,1) model. Perform a diagnostic check on
the ﬁtted model.
(g) Repeat the prior two-dimensional nonhomogeneous Poisson process with
threshold 2.5 or 3%. Comment on the selection of threshold.
7.3. Use Hill’s estimator and the data d-csco9808.txt to estimate the tail index
for daily log returns of Cisco stock.
7.4. The ﬁle d-hpq3dx9808.txt contains dates and the daily simple returns of
Hewlett-Packard, the CRSP value-weighted index, equal-weighted index, and
the S&P 500 index from 1998 to 2008. The returns include dividend distributions. Transform the simple returns to log returns. Assume that the tail
probability of interest is 0.01. Calculate value at risk for the following ﬁnancial
positions for the ﬁrst trading day of year 2009.
(a) Long on Hewlett-Packard stock of $1 million and S&P 500 index of $1
million using RiskMetrics. The α coefﬁcient of the IGARCH(1,1) model
for each series should be estimated.
(b) The same position as part (a) but using a univariate ARMA–GARCH
model for each return series.
(c) A long position on Hewlett-Packard stock of $1 million using a twodimensional nonhomogeneous Poisson model with the following explanatory variables: (1) an annual time trend, (2) a ﬁtted volatility based on a
Gaussian GARCH model for Hewlett-Packard stock, (3) a ﬁtted volatility
based on a Gaussian GARCH model for the S&P 500 index returns, and
(4) a ﬁtted volatility based on a Gaussian GARCH model for the valueweighted index return. Perform a diagnostic check for the ﬁtted models.
Are the market volatility as measured by the S&P 500 index and valueweighted index returns helpful in determining the tail behavior of stock
returns of Hewlett-Packard? You may choose several thresholds.
--- page 413 ---

386
extreme values, quantiles, and value at risk
7.5. Consider the daily returns of Alcoa (AA) stock and the S&P 500 composite
index (SPX) from 1998 to 2008. The simple returns and dates are in the ﬁle
d-aaspx9808.txt. Transform the simple returns to log returns and focus on
the daily negative log returns of AA stock.
(a) Fit the generalized extreme value distribution to the negative AA log
returns, in percentages, with subperiods of 21 trading days. Write down
the parameter estimates and their standard errors. Obtain a scatterplot and
a QQ plot of the residuals.
(b) What is the return level of the prior ﬁtted model when 24 subperiods of
21 days are used?
(c) Obtain a QQ plot (against exponential distribution) of the negative log
returns with threshold 2.5% and a mean excess plot of the returns.
(d) Fit a generalize Pareto distribution to the negative log returns with threshold 3.5%. Write down the parameter estimates and their standard errors.
(e) Obtain (i) a plot of excess distribution, (ii) a plot of the tail of the underlying distribution, (iii) a scatterplot of residuals, and (iv) a QQ plot of the
residuals for the ﬁtted GPD.
(f) Based on the ﬁtted GPD model, compute the VaR and expected shortfall
for probabilities q = 0.99 and 0.999.
7.6. Consider, again, the daily log returns of Alcoa (AA) stock in Exercise 7.5.
Focus now on the daily positive log returns. Answer the same questions as in
Exercise 7.5. However, use threshold 3% in ﬁtting the GPD model.
7.7. Consider the daily returns of SPX in d-aaspx9808.txt. Transform the
returns into log returns and focus on the daily negative log returns.
(a) Fit the generalized extreme value distribution to the negative SPX log
returns, in percentage, with subperiods of 21 trading days. Write down the
parameter estimates and their standard errors. Obtain a scatterplot and a
QQ plot of the residuals.
(b) What is the return level of the prior ﬁtted model when 24 subperiods of
21 days are used?
(c) Obtain a QQ plot (against exponential distribution) of the negative log
returns with threshold 2.5% and a mean excess plot of the returns.
(d) Fit a generalize Pareto distribution to the negative log returns with threshold 2.5%. Write down the parameter estimates and their standard errors.
(e) Obtain (i) a plot of excess distribution, (ii) a plot of the tail of the underlying distribution, (iii) a scatterplot of residuals, and (iv) a QQ plot of the
residuals for the ﬁtted GPD.
(f) Based on the ﬁtted GPD model, compute the VaR and expected shortfall
for probabilities q = 0.99 and 0.999.
7.8. Consider the daily log returns of the GE stock of Exercise 7.1. Obtain estimates ˆθ(1)
b
and ˆθ(3)
r
of the extremal index of (a) the positive return series
and (b) the negative return series, using block sizes k = 5 and 10 and
threshold 2.5%.
--- page 414 ---

references
387
REFERENCES
Beirlant, J., Goegebeur, Y., Segers, J., and Teugels, J. (2004). Statistics of Extremes: Theory
and Applications. Wiley, Hoboken, NJ.
Berman, S. M. (1964). Limiting theorems for the maximum term in stationary sequences.
Annals of Mathematical Statistics 35: 502–516.
Coles, S. (2001). An Introduction to Statistical Modeling of Extreme Values. Springer, New
York.
Cox, D. R. and Hinkley, D. V. (1974). Theoretical Statistics. Chapman and Hall, London.
Danielsson, J. and De Vries, C. G. (1997a). Value at risk and extreme returns. Working
paper, London School of Economics, London, UK.
Danielsson, J. and De Vries, C. G. (1997b). Tail index and quantile estimation with very
high frequency data. Journal of Empirical Finance 4: 241–257.
Davison, A. C. and Smith, R. L. (1990). Models for exceedances over high thresholds (with
discussion). Journal of the Royal Statistical Society Series B 52: 393–442.
Dekkers, A. L. M. and De Haan, L. (1989). On the estimation of extreme value index and
large quantile estimation. Annals of Statistics 17: 1795–1832.
Dufﬁe, D. and Pan, J. (1997). An overview of value at risk. Journal of Derivatives Spring:
7–48.
Embrechts, P., Kuppelberg, C., and Mikosch, T. (1997). Modelling Extremal Events.
Springer, Berlin.
Feller, W. (1971). An Introduction to Probability Theory and Its Applications, Vol. 2. Wiley,
New York.
Goldie, C. M. and Smith, R. L. (1987). Slow variation with remainder: Theory and applications. Quarterly Journal of Mathematics 38: 45–71.
Gnedenko, B. V. (1943). Sur la distribution limite du terme maximum of d’une s´erie
Al´eatorie. Annals of Mathematics 44: 423–453.
Gumbel, E. J. (1958). Statistics of Extremes. Columbia University Press, New York.
Hill, B. M. (1975). A simple general approach to inference about the tail of a distribution.
Annals of Statistics 3: 1163–1173.
Hsing, T., H¨usler, J. and Leadbetter, M. R. (1988). On the exceedance point process for a
stationary sequence. Probability Theory and Related Fields 78: 97–112.
Jenkinson, A. F. (1955). The frequency distribution of the annual maximum (or minimum)
of meteorological elements. Quarterly Journal of the Royal Meteorological Society 81:
158–171.
Jorion, P. (2006). Value at Risk: The New Benchmark for Managing Financial Risk, 3rd ed.
McGraw-Hill, Chicago.
Koenker, R. W. and Bassett, G. W. (1978). Regression quantiles. Econometrica 46: 33–50.
Koenker, R. W. and D’Orey, V. (1987). Computing regression quantiles. Applied Statistics
36: 383–393.
Leadbetter, M. R. (1974). On extreme values in stationary sequences. Zeitschrift f¨ur
Wahrscheinlichkeitsthorie und Verwandte Gebiete 28: 289–303.
Leadbetter, M. R. (1983). Extremes and local dependence in stationary sequences. Zeitschrift
f¨ur Wahrscheinlichkeitsthorie und Verwandte Gebiete 65: 291–306.
--- page 415 ---

388
extreme values, quantiles, and value at risk
Leadbetter, M. R., Lindgren, G., and Rootz´en, H. (1983). Extremes and Related Properties
of Random Sequences and Processes. Springer, New York.
Longerstaey, J. and More, L. (1995). Introduction to RiskMetricsTM, 4th ed. Morgan Guaranty Trust Company, New York.
Longin, F. M. (1996). The asymptotic distribution of extreme stock market returns. Journal
of Business 69: 383–408.
Longin, F. M. (1999a). Optimal margin level in futures markets: Extreme price movements.
Journal of Futures Markets 19: 127–152.
Longin, F. M. (1999b). From value at risk to stress testing: The extreme value approach.
Working paper, Centre for Economic Policy Research, London.
O’Brien, G. L. (1987). Extreme values for stationary and Markov sequences. Annals of
Probability 15: 281–291.
Pickands, J. (1975). Statistical inference using extreme order statistics. Annals of Statistics
3: 119–131.
Smith, R. L. (1989). Extreme value analysis of environmental time series: An application to
trend detection in ground-level ozone (with discussion). Statistical Science 4: 367–393.
Smith, R. L. (1999). Measuring risk with extreme value theory. Working paper, Department
of Statistics, University of North Carolina at Chapel Hill.
Smith, R. L. and Shively, T. S. (1995). A point process approach to modeling trends in
troposheric ozone. Atmospheric Environment 29: 3489–3499.
Tsay, R. S. (1999). Extreme value analysis of ﬁnancial data. Working paper, Graduate School
of Business, University of Chicago.
Zivot, E. and Wang, J. (2003). Modeling Financial Time Series with S-Plus. Springer, New
York.
--- page 416 ---

C H A P T E R
8
Multivariate Time Series Analysis
and Its Applications
Economic globalization and Internet communication have accelerated the integration of world ﬁnancial markets in recent years. Price movements in one market can
spread easily and instantly to another market. For this reason, ﬁnancial markets
are more dependent on each other than ever before, and one must consider them
jointly to better understand the dynamic structure of the global ﬁnance. One market
may lead the other market under some circumstances, yet the relationship may be
reversed under other circumstances. Consequently, knowing how the markets are
interrelated is of great importance in ﬁnance. Similarly, for an investor or a ﬁnancial institution holding multiple assets, the dynamic relationships between returns
of the assets play an important role in decision making. In this and the next two
chapters, we introduce econometric models and methods useful for studying jointly
multiple return series. In the statistical literature, these models and methods belong
to vector or multivariate time series analysis.
A multivariate time series consists of multiple single series referred to as components. As such, concepts of vector and matrix are useful in understanding
multivariate time series analysis. We use boldface notation to indicate vectors
and matrices. If necessary, readers may consult Appendix A of this chapter for
some basic operations and properties of vectors and matrices. Appendix B provides some results of multivariate normal distribution, which is widely used in
multivariate statistical analysis (e.g., Johnson and Wichern, 1998).
Let rt = (r1t, r2t, . . . , rkt)′ be the log returns of k assets at time t, where a′
denotes the transpose of a. For example, an investor holding stocks of IBM,
Microsoft, Exxon Mobil, General Motors, and Wal-Mart may consider the ﬁvedimensional daily log returns of these companies. Here r1t denotes the daily log
return of IBM stock, r2t is that of Microsoft, and so on. As a second example,
an investor who is interested in global investment may consider the return series
of the S&P 500 index of the United States, the FTSE 100 index of the United
Analysis of Financial Time Series, Third Edition, By Ruey S. Tsay
Copyright 2010 John Wiley & Sons, Inc.
389
--- page 417 ---

390
multivariate time series analysis and its applications
Kingdom, and the Nikkei 225 index of Japan. Here the series is three-dimensional,
with r1t denoting the return of the S&P 500 index, r2t the return of the Financial
Times Stock Exchange (FTSE) 100 index, and r3t the return of the Nikkei 225.
The goals of this chapter are (a) to explore the basic properties of rt and (b) to
study econometric models for analyzing the multivariate data {rt|t = 1, . . . , T }.
Many of the models and methods discussed in previous chapters can be generalized directly to the multivariate case. But there are situations in which the
generalization requires some attention. In some situations, one needs new models
and methods to handle the complicated relationships between multiple series. In
this chapter, we discuss these issues with emphasis on intuition and applications.
For statistical theory of multivariate time series analysis, readers are referred to
L¨utkepohl (2005) and Reinsel (1993).
8.1
WEAK STATIONARITY AND CROSS-CORRELATION MATRICES
Consider a k-dimensional time series rt = (r1t, . . . , rkt)′. The series rt is weakly
stationary if its ﬁrst and second moments are time invariant. In particular, the
mean vector and covariance matrix of a weakly stationary series are constant over
time. Unless stated explicitly to the contrary, we assume that the return series of
ﬁnancial assets are weakly stationary.
For a weakly stationary time series rt, we deﬁne its mean vector and covariance
matrix as
µ = E(rt),

0 = E[(rt −µ)(rt −µ)′],
(8.1)
where the expectation is taken element by element over the joint distribution of rt.
The mean µ is a k-dimensional vector consisting of the unconditional expectations
of the components of rt. The covariance matrix
0 is a k × k matrix. The ith
diagonal element of
0 is the variance of rit, whereas the (i, j)th element of
0 is
the covariance between rit and rjt. We write µ = (µ1, . . . , µk)′ and
0 = [ij(0)]
when the elements are needed.
8.1.1
Cross-Correlation Matrices
Let D be a k × k diagonal matrix consisting of the standard deviations of rit for
i = 1, . . . , k. In other words, D = diag{√11(0), . . . , √kk(0)}. The concurrent,
or lag-zero, cross-correlation matrix of rt is deﬁned as
ρ0 ≡[ρij(0)] = D−1
0D−1.
More speciﬁcally, the (i, j)th element of ρ0 is
ρij(0) =
ij(0)

ii(0)jj(0)
=
Cov(rit, rjt)
std(rit)std(rjt),
--- page 418 ---

weak stationarity and cross-correlation matrices
391
which is the correlation coefﬁcient between rit and rjt. In time series analysis,
such a correlation coefﬁcient is referred to as a concurrent, or contemporaneous,
correlation coefﬁcient because it is the correlation of the two series at time t. It is
easy to see that ρij(0) = ρji(0), −1 ≤ρij(0) ≤1, and ρii(0) = 1 for 1 ≤i, j ≤k.
Thus, ρ(0) is a symmetric matrix with unit diagonal elements.
An important topic in multivariate time series analysis is the lead–lag relationships between component series. To this end, the cross-correlation matrices are
used to measure the strength of linear dependence between time series. The lag-ℓ
cross-covariance matrix of rt is deﬁned as

ℓ≡[ij(ℓ)] = E[(rt −µ)(rt−ℓ−µ)′],
(8.2)
where µ is the mean vector of rt. Therefore, the (i, j)th element of
ℓis the covariance between rit and rj,t−ℓ. For a weakly stationary series, the cross-covariance
matrix
ℓis a function of ℓ, not the time index t.
The lag-ℓcross-correlation matrix (CCM) of rt is deﬁned as
ρℓ≡[ρij(ℓ)] = D−1
ℓD−1,
(8.3)
where, as before, D is the diagonal matrix of standard deviations of the individual
series rit. From the deﬁnition,
ρij(ℓ) =
ij(ℓ)

ii(0)jj(0)
= Cov(rit, rj,t−ℓ)
std(rit)std(rjt) ,
(8.4)
which is the correlation coefﬁcient between rit and rj,t−ℓ. When ℓ> 0, this correlation coefﬁcient measures the linear dependence of rit on rj,t−ℓ, which occurred
prior to time t. Consequently, if ρij(ℓ)̸ = 0 and ℓ> 0, we say that the series rjt
leads the series rit at lag ℓ. Similarly, ρji(ℓ) measures the linear dependence of rjt
and ri,t−ℓ, and we say that the series rit leads the series rjt at lag ℓif ρji(ℓ)̸ = 0
and ℓ> 0. Equation (8.4) also shows that the diagonal element ρii(ℓ) is simply the
lag-ℓautocorrelation coefﬁcient of rit.
Based on this discussion, we obtain some important properties of the cross
correlations when ℓ> 0. First, in general, ρij(ℓ)̸ = ρji(ℓ) for i̸ = j because the
two correlation coefﬁcients measure different linear relationships between {rit} and
{rjt}. Therefore,
ℓand ρℓare in general not symmetric. Second, using Cov(x, y)
= Cov(y, x) and the weak stationarity assumption, we have
Cov(rit, rj,t−ℓ) = Cov(rj,t−ℓ, rit) = Cov(rjt, ri,t+ℓ) = Cov(rjt, ri,t−(−ℓ)),
so that ij(ℓ) = ji(−ℓ). Because ji(−ℓ) is the (j, i)th element of the matrix
−ℓ
and the equality holds for 1 ≤i, j ≤k, we have
ℓ=
′
−ℓand ρℓ= ρ′
−ℓ. Consequently, unlike the univariate case, ρℓ̸ = ρ−ℓfor a general vector time series when
ℓ> 0. Because ρℓ= ρ′
−ℓ, it sufﬁces in practice to consider the cross-correlation
matrices ρℓfor ℓ≥0.
--- page 419 ---

392
multivariate time series analysis and its applications
8.1.2
Linear Dependence
Considered jointly, the cross-correlation matrices {ρℓ|ℓ= 0, 1, . . .} of a weakly
stationary vector time series contain the following information:
1. The diagonal elements {ρii(ℓ)|ℓ= 0, 1, . . .} are the autocorrelation function
of rit.
2. The off-diagonal element ρij(0) measures the concurrent linear relationship
between rit and rjt.
3. For ℓ> 0, the off-diagonal element ρij(ℓ) measures the linear dependence of
rit on the past value rj,t−ℓ.
Therefore, if ρij(ℓ) = 0 for all ℓ> 0, then rit does not depend linearly on any
past value rj,t−ℓof the rjt series.
In general, the linear relationship between two time series {rit} and {rjt} can be
summarized as follows:
1. rit and rjt have no linear relationship if ρij(ℓ) = ρji(ℓ) = 0 for all ℓ≥0.
2. rit and rjt are concurrently correlated if ρij(0)̸ = 0.
3. rit and rjt have no lead–lag relationship if ρij(ℓ) = 0 and ρji(ℓ) = 0 for all
ℓ> 0. In this case, we say the two series are uncoupled.
4. There is a unidirectional relationship from rit to rjt if ρij(ℓ) = 0 for all
ℓ> 0, but ρji(v)̸ = 0 for some v > 0. In this case, rit does not depend on
any past value of rjt, but rjt depends on some past values of rit.
5. There is a feedback relationship between rit and rjt if ρij(ℓ)̸ = 0 for some
ℓ> 0 and ρji(v)̸ = 0 for some v > 0.
The conditions stated earlier are sufﬁcient conditions. A more informative approach
to study the relationship between time series is to build a multivariate model for
the series because a properly speciﬁed model considers simultaneously the serial
and cross correlations among the series.
8.1.3
Sample Cross-Correlation Matrices
Given the data {rt|t = 1, . . . , T }, the cross-covariance matrix
ℓcan be estimated by

ℓ= 1
T
T

t=ℓ+1
(rt −¯r)(rt−ℓ−¯r)′,
ℓ≥0,
(8.5)
where ¯r = (T
t=1 rt)/T is the vector of sample means. The cross-correlation matrix
ρℓis estimated by
ρℓ= 
D
−1
ℓ
D
−1,
ℓ≥0,
(8.6)
