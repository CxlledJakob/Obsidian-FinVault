# Analysis of Financial Time Series, Third Edition (Wiley -- Ruey S_ Tsay -- Wiley series in probability and statistics, 3rd ed_, -- John Wiley & Sons, -- isbn13 9780470414354 -- 9f99b80c7b2dedd477f463dc5323f3b6 -- An.pdf — pages 362–381

--- page 362 ---

econometric approach to var calculation
335
The 95% quantile is then
−0.00071 + 1.6449 ×
√
0.0003211 = 0.02877.
The
VaR
for
a
long
position
of
$10
million
with
probability
0.05
is
VaR = $10,000,000 × 0.02877 = $287,700. The result shows that, with probability 95%, the potential loss of holding that position next day is $287, 200 or
less assuming that the AR(2)–GARCH(1,1) model holds. If the tail probability is
0.01, then the 99% quantile is
−0.00071 + 2.3262 ×
√
0.0003211 = 0.0409738.
The VaR for the position becomes $409, 738.
CASE 2.
Assume that ϵt is a standardized Student-t distribution with 5 degrees
of freedom. The ﬁtted model is
rt = −0.0003 −0.0335rt−2 + at,
at = σtϵt,
σ 2
t = 0.000003 + 0.0559a2
t−1 + 0.9350σ 2
t−1.
From the data, we have r9189 = 0.00201, r9190 = 0.0128, and σ 2
9190 = 0.000349.
Consequently, the prior Student-t AR(2)–GARCH(1,1) model produces 1-stepahead forecasts
ˆr9190(1) = −0.000367
and
ˆσ 2
9190(1) = 0.0003386.
The 95% quantile of a Student-t distribution with 5 degrees of freedom is 2.015
and that of its standardized distribution is 2.015/√5/3 = 1.5608. Therefore, the
95% quantile of the conditional distribution of r9191 given F9190 is
−0.000367 + 1.5608
√
0.0003386 = 0.028354.
The VaR for a long position of $10 million is
VaR = $10,000,000 × 0.028352 = $283,520,
which is essentially the same as that obtained under the normality assumption. The
99% quantile of the conditional distribution is
−0.000367 + (3.3649/

5/3)
√
0.0003386 = 0.0475943.
The corresponding VaR is $475, 943. Comparing with that of Case 1, we see the
heavy-tail effect of using a Student-t distribution with 5 degrees of freedom; it
increases the VaR when the tail probability becomes smaller. In R and S-Plus, the
quantile of a Student-t distribution with m degrees of freedom can be obtained
by the command qt(p,m), for example, xp = qt(0.99,5.23) for the 99th percentile of a Student-t distribution with 5.23 degrees of freedom.
--- page 363 ---

336
extreme values, quantiles, and value at risk
7.3.1
Multiple Periods
Suppose that at time h we want to compute the k-horizon VaR of an asset whose
log return is rt. The variable of interest is the k-period log return at the forecast
origin h (i.e., rh[k] = rh+1 + · · · + rh+k). If the return rt follows the time series
model in Eqs. (7.5) and (7.6), then the conditional mean and variance of rh[k]
given the information set Fh can be obtained by the forecasting methods discussed
in Chapters 2 and 3.
Expected Return and Forecast Error
The conditional mean E(rh[k]|Fh) can be obtained by the forecasting method of
ARMA models in Chapter 2. Speciﬁcally, we have
ˆrh[k] = rh(1) + · · · + rh(k),
where rh(ℓ) is the ℓ-step-ahead forecast of the return at the forecast origin h. These
forecasts can be computed recursively as discussed in Section 2.6.4. Using the MA
representation
rt = µ + at + ψ1at−1 + ψ2at−2 + · · ·
of the ARMA model in Eq. (7.5), we can write the ℓ-step-ahead forecast error at
the forecast origin h as
eh(ℓ) = rh+ℓ−rh(ℓ) = ah+ℓ+ ψ1ah+ℓ−1 + · · · + ψℓ−1ah+1;
see Eq. (2.33) and the associated forecast error. The forecast error of the expected
k-period return ˆrh[k] is the sum of 1-step to k-step forecast errors of rt at the
forecast origin h and can be written as
eh[k] = eh(1) + eh(2) + · · · + eh(k)
= ah+1 + (ah+2 + ψ1ah+1) + · · · +
k−1

i=0
ψiah+k−i
= ah+k + (1 + ψ1)ah+k−1 + · · · +
k−1

i=0
ψi

ah+1,
(7.7)
where ψ0 = 1.
Expected Volatility
The volatility forecast of the k-period return at the forecast origin h is the conditional variance of eh[k] given Fh. Using the independent assumption of ϵt+i for
--- page 364 ---

econometric approach to var calculation
337
i = 1, . . . , k, where at+i = σt+iϵt+i, we have
Vh(eh[k]) = Vh(ah+k) + (1 + ψ1)2Vh(ah+k−1) + · · · +
k−1

i=0
ψi
2
Vh(ah+1)
= σ 2
h(k) + (1 + ψ1)2σ 2
h(k −1) + · · · +
k−1

i=0
ψi
2
σ 2
h(1),
(7.8)
where Vh(z) denotes the conditional variance of z given Fh and σ 2
h(ℓ) is the ℓ-
step-ahead volatility forecast at the forecast origin h. If the volatility model is
the GARCH model in Eq. (7.6), then these volatility forecasts can be obtained
recursively by the methods discussed in Chapter 3.
As an illustration, consider the special time series model
rt = µ + at,
at = σtϵt,
σ 2
t = α0 + α1a2
t−1 + β1σ 2
t−1.
Then we have ψi = 0 for all i > 0. The point forecast of the k-period return at the
forecast origin h is ˆrh[k] = kµ and the associated forecast error is
eh[k] = ah+k + ah+k−1 + · · · + ah+1.
Consequently, the volatility forecast for the k-period return at the forecast origin
h is
Var(eh[k]|Fh) =
k

ℓ=1
σ 2
h(ℓ).
Using the forecasting method of GARCH(1,1) models in Section 3.5, we have
σ 2
h(1) = α0 + α1a2
h + β1σ 2
h,
σ 2
h(ℓ) = α0 + (α1 + β1)σ 2
h(ℓ−1),
ℓ= 2, . . . , k.
(7.9)
Using Eq. (7.9), we obtain that for the case of ψi = 0 for i > 0,
Var(eh[k]|Fh) =
α0
1 −φ

k −1 −φk
1 −φ

+ 1 −φk
1 −φ σ 2
h(1),
(7.10)
where φ = α1 + β1 < 1. If ψi̸ = 0 for some i > 0, then one should use the general
formula of Var(eh[k]|Fh) in Eq. (7.8). If ϵt is Gaussian, then the conditional distribution of rh[k] given Fh is normal with mean kµ and variance Var(eh[k]|Fh). The
--- page 365 ---

338
extreme values, quantiles, and value at risk
quantiles needed in VaR calculations are readily available. If the conditional distribution of at is not Gaussian (e.g., a Student-t or generalized error distribution),
simulation can be used to obtain the multiperiod VaR.
Example 7.3 (Continued).
Consider the Gaussian AR(2)–GARCH(1,1)
model of Example 7.3 for the daily log returns of IBM stock. Suppose that we
are interested in the VaR of a 15-day horizon starting at the forecast origin 9190
(i.e., December 31, 1998). We can use the ﬁtted model to compute the conditional
mean and variance for the 15-day log return via r9190[15] = 15
i=1 r9190+i
given F9190. The conditional mean is −0.00998 and the conditional variance is
0.0047948, which is obtained by the recursion in Eq. (7.9). The 95% quantile of
the conditional distribution is then −0.00998 + 1.6449
√
0.0047948 = 0.1039191.
Consequently, the 5% 15-day horizon VaR for a long position of $10 million
is VaR = $10,000,000 × 0.1039191 = $1,039,191. This amount is smaller than
$287,700 ×
√
15 = $1,114,257. This example further demonstrates that the
square root of time rule used by RiskMetrics holds only for the special white
noise IGARCH(1,1) model used. When the conditional mean is not zero, proper
steps must be taken to compute the k-horizon VaR.
7.3.2
Expected Shortfall under Conditional Normality
We can use the result of Section 7.2.3 to calculate the ES when the conditional
distribution of the log return is N(µt, σ 2
t ). The result is
ESq = µt + f (xq)
p
σt,
where q = 1 −p and xq is the qth quantile of the standard normal distribution.
For instance, if p = 0.01, then ES0.99 = µt + 2.6652σt.
7.4
QUANTILE ESTIMATION
Quantile estimation provides a nonparametric approach to VaR calculation. It makes
no speciﬁc distributional assumption on the return of a portfolio except that the
distribution continues to hold within the prediction period. There are two types of
quantile methods. The ﬁrst method is to use empirical quantile directly, and the
second method uses quantile regression.
7.4.1
Quantile and Order Statistics
Assuming that the distribution of return in the prediction period is the same as that
in the sample period, one can use the empirical quantile of the return rt to calculate
VaR. Let r1, . . . , rn be the returns of a portfolio in the sample period. The order
--- page 366 ---

quantile estimation
339
statistics of the sample are these values arranged in increasing order. We use the
notation
r(1) ≤r(2) ≤· · · ≤r(n)
to denote the arrangement and refer to r(i) as the ith order statistic of the sample.
In particular, r(1) is the sample minimum and r(n) the sample maximum.
Assume that the returns are independent and identically distributed random variables that have a continuous distribution with probability density function (pdf)
f (x) and CDF F(x). Then we have the following asymptotic result from the statistical literature [e.g., Cox and Hinkley (1974), Appendix 2], for the order statistic
r(ℓ), where ℓ= np with 0 < p < 1.
Result. Let xp be the pth quantile of F(x), that is, xp = F −1(p). Assume that
the pdf f (x) is not zero at xp [i.e., f (xp)̸ = 0]. Then the order statistic r(ℓ) is
asymptotically normal with mean xp and variance p(1 −p)/[nf 2(xp)]. That is,
r(ℓ) ∼N

xp, p(1 −p)
n[f (xp)]2
"
,
ℓ= np.
(7.11)
Based on the prior result, one can use r(ℓ) to estimate the quantile xp, where
ℓ= np. In practice, the probability of interest p may not satisfy that np is a positive
integer. In this case, one can use simple interpolation to obtain quantile estimates.
More speciﬁcally, for noninteger np, let ℓ1 and ℓ2 be the two neighboring positive
integers such that ℓ1 < np < ℓ2. Deﬁne pi = ℓi/n. The previous result shows that
r(ℓi) is a consistent estimate of the quantile xpi. From the deﬁnition, p1 < p < p2.
Therefore, the quantile xp can be estimated by
ˆxp = p2 −p
p2 −p1
r(ℓ1) + p −p1
p2 −p1
r(ℓ2).
(7.12)
In practice, sample quantiles can easily be obtained from most statistical packages,
including R and S-Plus. A demonstration is given after the examples.
Example 7.4.
Consider the daily log returns of Intel stock from December 15,
1972, to December 31, 2008. There are 9096 observations. For a long position in the
Intel stock, we consider the negative log returns. Since 9096 × 0.95 = 8641.2, we
have ℓ1 = 8641, ℓ2 = 8642, p1 = 8641/9096, and p2 = 8642/9096. The empirical
95% quantile of the negative log returns can be obtained as
ˆx0.95 = 0.8r(8641) + 0.2r(8642) = 4.2952%,
r(i) is the ith order statistic of the negative log returns. In this particular instance,
r(8641) = 4.2951% and r(8642) = 4.2954%.
--- page 367 ---

340
extreme values, quantiles, and value at risk
R Demonstration
> da=read.table("d-intc7208.txt",header=T)
> intc=log(da[,2]+1)
> nintc=-intc
> quantile(nintc,0.95)
95%
0.04295213
> quantile(rtn,.05) % An alternative
5%
-0.04295213
Example 7.5.
Consider again the daily log returns of IBM stock from July 3,
1962, to December 31, 1998. Using all 9190 observations, the empirical 95% quantile of the negative log returns can be obtained as (r(8730) + r(8731))/2 = 0.021603,
where r(i) is the ith order statistic and np = 9190 × 0.95 = 8730.5. The VaR of
a long position of $10 million is $216,030, which is much smaller than those
obtained by the econometric approach discussed before. Because the sample size is
9190, we have 9098 < 9190 × 0.99 < 9099. Let p1 = 9198/9190 = 0.98999 and
p2 = 9099/9190 = 0.9901. The empirical 99% quantile can be obtained as
ˆx0.99 = p2 −0.99
p2 −p1
r(9098) + 0.99 −p1
p2 −p1
r(9099)
= 0.0001
0.00011(3.627) + 0.00001
0.00011(3.657)
≈3.630.
The 1% 1-day horizon VaR of the long position is $363, 000. Again this amount
is lower than those obtained before by other methods.
Discussion.
Advantages of using the empirical quantile method to VaR calculation include (a) simplicity and (b) using no speciﬁc distributional assumption.
However, the approach has several drawbacks. First, it assumes that the distribution
of the return rt remains unchanged from the sample period to the prediction period.
Given that VaR is concerned mainly with tail probability, this assumption implies
that the predicted loss cannot be greater than that of the historical loss. It is deﬁ-
nitely not so in practice. Second, when the tail probability p is small, the empirical
quantile is not an efﬁcient estimate of the theoretical quantile. Third, the direct
quantile estimation fails to take into account the effect of explanatory variables
that are relevant to the portfolio under study. In real application, VaR obtained by
the empirical quantile can serve as a lower bound for the actual VaR.
□
The expected shortfall can also be estimated directly from the sample returns.
Let ˆxq be the empirical qth quantile, where q = 1 −p with p being the upper tail
--- page 368 ---

quantile estimation
341
probability. We have
ESq = 1
Nq
n

i=1
x(i)I[x(i) > ˆxq],
where I[·] = 1 if x(i) > ˆxq and = 0, otherwise, and Nq denotes the number of xi
greater than ˆxq. For illustration, consider the negative IBM daily log returns. If
p = 0.01, we have ˆx0.99 = 3.630. Therefore, ES0.99 = 5.097.
R Demonstration
> da=read.table("d-ibm6298.txt",header=T)
> ibm=log(da[,2]+1)*100
> nibm=-ibm
> q99=quantile(nibm,0.99)
> q99
99%
[1] 3.630295
> idx=c(1:length(nibm))[nibm>q99] % locate the exceedances
> es=mean(nibm[idx])
> es
[1] 5.097222
7.4.2
Quantile Regression
In real application, one often has explanatory variables available that are important
to the problem under study. For example, the action taken by Federal Reserve
Banks on interest rates could have important impacts on the returns of U.S.
stocks. It is then more appropriate to consider the distribution function rt+1|Ft,
where Ft includes the explanatory variables. In other words, we are interested
in the quantiles of the distribution function of rt+1 given Ft. Such a quantile
is referred to as a regression quantile in the literature; see Koenker and Bassett
(1978).
To understand regression quantile, it is helpful to cast the empirical quantile of
the previous subsection as an estimation problem. For a given probability p, the
pth quantile of {rt} is obtained by
ˆxp = argminβ
n

i=1
wp(ri −β),
where wp(z) is deﬁned by
wp(z) =
 pz
if z ≥0,
(p −1)z
if z < 0.
Regression quantile is a generalization of such an estimate.
--- page 369 ---

342
extreme values, quantiles, and value at risk
To see the generalization, suppose that we have the linear regression
rt = β′xt + at,
(7.13)
where β is a k-dimensional vector of parameters and xt is a vector of predictors that
are elements of Ft−1. The conditional distribution of rt given Ft−1 is a translation
of the distribution of at because β′xt is known. Viewing the problem this way,
Koenker and Bassett (1978) suggest estimating the conditional quantile xp|Ft−1 of
rt given Ft−1 as
ˆxp|Ft−1 ≡inf{β′
ox|Rp(βo) = min},
(7.14)
where “Rp(βo) = min” means that βo is obtained by
βo = argminβ
n

t=1
wp(rt −β′xt),
where wp(·) is deﬁned as before. A computer program to obtain such an estimated
quantile can be found in Koenker and D’Orey (1987). The package quantreg of
R performs quantile regression analysis.
7.5
EXTREME VALUE THEORY
In this section, we review some extreme value theory in the statistical literature.
Denote the return of an asset, measured in a ﬁxed time interval such as daily,
by rt. Consider the collection of n returns, {r1, . . . , rn}. The minimum return of
the collection is r(1), that is, the smallest order statistic, whereas the maximum
return is r(n), the maximum order statistic. Speciﬁcally, r(1) = min1≤j≤n{rj} and
r(n) = max1≤j≤n{rj}. Following the literature and using the loss function in VaR
calculation, we focus on properties of the maximum return r(n). However, the theory
discussed also applies to the minimum return of an asset over a given time period
because properties of the minimum return can be obtained from those of the maximum by a simple sign change. Speciﬁcally, we have r(1) = −max1≤j≤n{−rj} =
−rc
(n), where rc
t = −rt with the superscript c denoting sign change. The minimum
return is relevant to holding a long ﬁnancial position. As before, we shall use negative log returns, instead of the log returns, to perform VaR calculation for a long
position.
7.5.1
Review of Extreme Value Theory
Assume that the returns rt are serially independent with a common cumulative
distribution function F(x) and that the range of the return rt is [l, u]. For log
--- page 370 ---

extreme value theory
343
returns, we have l = −∞and u = ∞. Then the CDF of r(n), denoted by Fn,n(x),
is given by
Fn,n(x) = Pr[r(n) ≤x]
= Pr(r1 ≤x, r2 ≤x, . . . , rn ≤x)
(by deﬁnition of maximum)
=
n

j=1
Pr(rj ≤x)
(by independence)
=
n

j=1
F(x) = [F(x)]n.
(7.15)
In practice, the CDF F(x) of rt is unknown and, hence, Fn,n(x) of r(n) is unknown.
However, as n increases to inﬁnity, Fn,n(x) becomes degenerated—namely,
Fn,n(x) →0 if x < u and Fn,n(x) →1 if x ≥u as n goes to inﬁnity. This
degenerated CDF has no practical value. Therefore, the extreme value theory is
concerned with ﬁnding two sequences {βn} and {αn}, where αn > 0, such that the
distribution of r(n∗) ≡(r(n) −βn)/αn converges to a nondegenerate distribution as
n goes to inﬁnity. The sequence {βn} is a location series and {αn} is a series of
scaling factors. Under the independent assumption, the limiting distribution of the
normalized minimum r(n∗) is given by
F∗(x) =

exp[−(1 + ξx)−1/ξ]
if ξ̸ = 0,
exp[−exp(−x)]
if ξ = 0,
(7.16)
for x < −1/ξ if ξ < 0 and for x > −1/ξ if ξ > 0, where the subscript ∗signiﬁes
the maximum. The case of ξ = 0 is taken as the limit when ξ →0. The parameter
ξ is referred to as the shape parameter that governs the tail behavior of the limiting
distribution. The parameter α = 1/ξ is called the tail index of the distribution.
The limiting distribution in Eq. (7.16) is the generalized extreme value (GEV)
distribution of Jenkinson (1955) for the maximum. It encompasses the three types
of limiting distribution of Gnedenko (1943):
• Type I: ξ = 0, the Gumbel family. The CDF is
F∗(x) = exp[−exp(−x)],
−∞< x < ∞.
(7.17)
• Type II: ξ > 0, the Fr´echet family. The CDF is
F∗(x) =

exp[−(1 + ξx)−1/ξ]
if x > −1/ξ,
0
otherwise.
(7.18)
• Type III: ξ < 0, the Weibull family. The CDF here is
F∗(x) =

exp[−(1 + ξx)−1/ξ]
if x < −1/ξ,
1
otherwise.
"
--- page 371 ---

344
extreme values, quantiles, and value at risk
x
Density
−10
−5
0
5
10
0.0
0.1
0.2
0.3
0.4
0.5
0.6
Weibull
Frechet
Gumbel
Figure 7.2
Probability density functions of extreme value distributions for maximum. Solid line is
for Gumbel distribution, dotted line is for Weibull distribution with ξ = −0.5, and dashed line is for
Fr´echet distribution with ξ = 0.9.
Gnedenko (1943) gave necessary and sufﬁcient conditions for the CDF F(x) of rt
to be associated with one of the three types of limiting distribution. Brieﬂy speaking, the tail behavior of F(x) determines the limiting distribution F∗(x) of the
maximum. The right tail of the distribution declines exponentially for the Gumbel
family, by a power function for the Fr´echet family, and is ﬁnite for the Weibull
family (Figure 7.2). Readers are referred to Embrechts, Kuppelberg, and Mikosch
(1997) for a comprehensive treatment of the extreme value theory. For risk management, we are mainly interested in the Fr´echet family, which includes stable
and Student-t distributions. The Gumbel family consists of thin-tailed distributions
such as normal and lognormal distributions. The probability density function (pdf)
of the generalized limiting distribution in Eq. (7.16) can be obtained easily by
differentiation:
f∗(x) =

(1 + ξx)−1/ξ−1 exp[−(1 + ξx)−1/ξ]
if ξ̸ = 0,
exp[−x −exp(−x)]
if ξ = 0,
(7.19)
where −∞< x < ∞for ξ = 0, and x < −1/ξ for ξ < 0, and x > −1/ξ for ξ > 0.
The aforementioned extreme value theory has two important implications. First,
the tail behavior of the CDF F(x) of rt, not the speciﬁc distribution, determines
the limiting distribution F∗(x) of the (normalized) maximum. Thus, the theory is
generally applicable to a wide range of distributions for the return rt. The sequences
--- page 372 ---

extreme value theory
345
{βn} and {αn}, however, may depend on the CDF F(x). Second, Feller (1971,
p. 279) shows that the tail index ξ does not depend on the time interval of rt.
That is, the tail index (or equivalently the shape parameter) is invariant under time
aggregation. This second feature of the limiting distribution becomes handy in the
VaR calculation.
The extreme value theory has been extended to serially dependent observations {rt}n
t=1 provided that the dependence is weak. Berman (1964) shows that the
same form of the limiting extreme value distribution holds for stationary normal
sequences provided that the autocorrelation function of rt is squared summable
(i.e., ∞
i=1 ρ2
i < ∞), where ρi is the lag-i autocorrelation function of rt. For further results concerning the effect of serial dependence on the extreme value theory,
readers are referred to Leadbetter, Lindgren, and Rootz´en (1983, Chapter 3). We
shall discuss extremal index for a strictly stationary time series later in Section 7.8.
7.5.2
Empirical Estimation
The extreme value distribution contains three parameters—ξ, βn, and αn. These
parameters are referred to as the shape, location, and scale parameters, respectively. They can be estimated by using either parametric or nonparametric methods.
We review some of the estimation methods.
For a given sample, there is only a single minimum or maximum, and we cannot
estimate the three parameters with only an extreme observation. Alternative ideas
must be used. One of the ideas used in the literature is to divide the sample into
subsamples and apply the extreme value theory to the subsamples. Assume that
there are T returns {rj}T
j=1 available. We divide the sample into g nonoverlapping
subsamples each with n observations, assuming for simplicity that T = ng. In other
words, we divide the data as
{r1, . . . , rn|rn+1, . . . , r2n|r2n+1, . . . , r3n| · · · |r(g−1)n+1, . . . , rng}
and write the observed returns as rin+j, where 1 ≤j ≤n and i = 0, . . . , g −1.
Note that each subsample corresponds to a subperiod of the data span. When n is
sufﬁciently large, we hope that the extreme value theory applies to each subsample.
In application, the choice of n can be guided by practical considerations. For
example, for daily returns, n = 21 corresponds approximately to the number of
trading days in a month and n = 63 denotes the number of trading days in a
quarter.
Let rn,i be the maximum of the ith subsample (i.e., rn,i is the largest return of the
ith subsample), where the subscript n is used to denote the size of the subsample.
When n is sufﬁciently large, xn,i = (rn,i −βn)/αn should follow an extreme value
distribution, and the collection of subsample maxima {rn,i|i = 1, . . . , g} can then
be regarded as a sample of g observations from that extreme value distribution.
Speciﬁcally, we deﬁne
rn,i = max
1≤j≤n{r(i−1)n+j},
i = 1, . . . , g.
(7.20)
--- page 373 ---

346
extreme values, quantiles, and value at risk
The collection of subsample maxima {rn,i} is the data we use to estimate the
unknown parameters of the extreme value distribution. Clearly, the estimates
obtained may depend on the choice of subperiod length n.
Remark.
When T is not a multiple of the subsample size n, several methods
have been used to deal with this issue. First, one can allow the last subsample to
have a smaller size. Second, one can ignore the ﬁrst few observations so that each
subsample has size n.
□
The Parametric Approach
Two parametric approaches are available. They are the maximum-likelihood and
regression methods.
Maximum-Likelihood Method
Assuming that the subperiod maxima {rn,i} follow a generalized extreme value
distribution such that the pdf of xi = (rn,i −βn)/αn is given in Eq. (7.19), we can
obtain the pdf of rn,i by a simple transformation as
f (rn,i)=



1
αn

1 + ξn(rn,i−βn)
αn
!−(1+ξn)/ξn exp

−

1 + ξn(rn,i−βn)
αn
−1/ξn
if ξn̸ = 0,
1
αn exp

−rn,i−βn
αn
−exp

−rn,i−βn
αn
!
if ξn = 0,
where it is understood that 1 + ξn(rn,i −βn)/αn > 0 if ξn̸ = 0. The subscript n is
added to the shape parameter ξ to signify that its estimate depends on the choice
of n. Under the independence assumption, the likelihood function of the subperiod
maxima is
ℓ(rn,1, . . . , rn,g|ξn, αn, βn) =
g

i=1
f (rn,i).
Nonlinear estimation procedures can then be used to obtain maximum-likelihood
estimates of ξn, βn, and αn. These estimates are unbiased, asymptotically normal,
and of minimum variance under proper assumptions. See Embrechts et al. (1997)
and Coles (2001) for details. We apply this approach to some stock return series
later.
Regression Method
This method assumes that {rn,i}g
i=1 is a random sample from the generalized extreme
value distribution in Eq. (7.16) and makes use of properties of order statistics; see
Gumbel (1958). Denote the order statistics of the subperiod maxima {rn,i}g
i=1 as
rn(1) ≤rn(2) ≤· · · ≤rn(g).
--- page 374 ---

extreme value theory
347
Using properties of order statistics (e.g., Cox and Hinkley, 1974, p. 467),
we have
E{F∗[rn(i)]} =
i
g + 1,
i = 1, . . . , g.
(7.21)
For simplicity, we separate the discussion into two cases depending on the value
of ξ. First, consider the case of ξ̸ = 0. From Eq. (7.16), we have
F∗[rn(i)] = exp

−

1 + ξn
rn(i) −βn
αn
	−1/ξn
.
(7.22)
Consequently, using Eqs. (7.21) and (7.22) and approximating expectation by an
observed value, we have
i
g + 1 = exp

−

1 + ξn
rn(i) −βn
αn
	−1/ξn
,
i = 1, . . . , g.
Taking natural logarithm twice, the prior equation gives
ln

−ln

i
g + 1
	
= −1
ξn
ln

1 + ξn
rn(i) −βn
αn

,
i = 1, . . . , g.
In practice, letting ei be the deviation between the previous two quantities and
assuming that the series {et} is not serially correlated, we have a regression setup
ln

−ln

i
g + 1
	
= −1
ξn
ln

1 + ξn
rn(i) −βn
αn

+ ei,
i = 1, . . . , g. (7.23)
The least-squares estimates of ξn, βn, and αn can be obtained by minimizing the
sum of squares of ei.
When ξn = 0, the regression setup reduces to
ln

−ln

i
g + 1
	
= −1
αn
rn(i) + βn
αn
+ ei,
i = 1, . . . , g.
The least-squares estimates are consistent but less efﬁcient than the likelihood
estimates. We use the likelihood estimates in this chapter.
--- page 375 ---

348
extreme values, quantiles, and value at risk
The Nonparametric Approach
The shape parameter ξ can be estimated using some nonparametric methods. We
mention two such methods here. These two methods are proposed by Hill (1975)
and Pickands (1975) and are referred to as the Hill estimator and Pickands estimator,
respectively. Both estimators apply directly to the returns {rt}T
t=1. Thus, there is no
need to consider subsamples. Denote the order statistics of the sample as
r(1) ≤r(2) ≤· · · ≤r(T ).
Let q be a positive integer. The two estimators of ξ are deﬁned as
ξp(q) =
1
ln(2) ln
 r(T −q+1) −r(T −2q+1)
r(T −2q+1) −r(T −4q+1)

,
q ≤T /4,
(7.24)
ξh(q) = 1
q
q

i=1
0
ln(r(T −i+1)) −ln(r(T −q))
1
,
(7.25)
where the argument (q) is used to emphasize that the estimators depend on q and the
subscripts p and h denote Pickands and Hill estimators, respectively. The choice of
q differs between Hill and Pickands estimators. It has been investigated by several
researchers, but there is no general consensus on the best choice available. Dekkers
and De Haan (1989) show that ξp(q) is consistent if q increases at a properly chosen
pace with the sample size T . In addition, √q[ξp(q) −ξ] is asymptotically normal
with mean zero and variance ξ 2(22ξ+1 + 1)/[2(2ξ −1) ln(2)]2. The Hill estimator is
applicable to the Fr´echet distribution only, but it is more efﬁcient than the Pickands
estimator when applicable. Goldie and Smith (1987) show that √q[ξh(q) −ξ] is
asymptotically normal with mean zero and variance ξ 2. In practice, one may plot the
Hill estimator ξh(q) against q and ﬁnd a proper q such that the estimate appears to
be stable. The estimated tail index α = 1/ξh(q) can then be used to obtain extreme
quantiles of the return series; see Zivot and Wang (2003).
7.5.3
Application to Stock Returns
We apply the extreme value theory to the daily log returns of IBM stock from July
3, 1962, to December 31, 1998. The returns are measured in percentages, and the
sample size is 9190 (i.e., T = 9190). Figure 7.3 shows the time plots of extreme
daily log returns when the length of the subperiod is 21 days, which corresponds
approximately to a month. The October 1987 crash is clearly seen from the plot.
Excluding the 1987 crash, the range of extreme daily log returns is between 0.5
and 13%.
Table 7.1 summarizes some estimation results of the shape parameter ξ via
the Hill estimator. Three choices of q are reported in the table, and the results
are stable. To provide an overall picture of the performance of the Hill estimator,
Figure 7.4 shows the scatterplots of the Hill estimator ξh(q) and its pointwise 95%
conﬁdence interval against q. For both positive and negative extreme daily log
--- page 376 ---

extreme value theory
349
Year
(a)
max
1970
1980
1990
2000
2
4
6
8 10 12
min
−25−20−15−10 −5
0
Year
(b)
1970
1980
1990
2000
Figure 7.3
Maximum and minimum daily log returns of IBM stock when subperiod is 21 trading days.
Data span is from July 3, 1962, to December 31, 1998: (a) positive returns and (b) negative returns.
TABLE 7.1
Results of Hill Estimator for Daily Log Returns of IBM Stock from July
3, 1962, to December 31, 1998a
q
190
200
210
rt
0.300(0.022)
0.299(0.021)
0.305(0.021)
−rt
0.290(0.021)
0.292(0.021)
0.289(0.020)
aStandard errors are in parentheses.
returns, the estimator is stable except for cases when q is small. The estimated
shape parameters are about 0.30 and are signiﬁcantly different from zero at the
asymptotic 5% level. The plots also indicate that the shape parameter ξ appears to
be larger for the negative extremes, indicating that the daily log return may have a
heavier left tail. Overall, the result indicates that the distribution of daily log returns
of IBM stock belongs to the Fr´echet family. The analysis thus rejects the normality
assumption commonly used in practice. Such a conclusion is in agreement with
that of Longin (1996), who used a U.S. stock market index series. R and S-Plus
commands used to perform the analysis are given in the demonstration below.
Next, we apply the maximum-likelihood method to estimate parameters of the
generalized extreme value distribution for IBM daily log returns. Table 7.2 summarizes the estimation results for different choices of the length of subperiods ranging
--- page 377 ---

350
extreme values, quantiles, and value at risk
15
48
81 119
162
205
248
291
334
377
420
463
0.15
0.30
0.0636
0.0428
0.0341
0.0306
0.0286
0.0265
0.0249
0.0234
Order statistics
xi (CI, p = 0.95)
Threshold
15
48
81 119
162
205
248
291
334
377
420
463
0.2
0.4
0.6
0.0552
0.0377
0.0315
0.0283
0.0258
0.0243
0.0228
0.0213
Order statistics
xi (CI, p = 0.95)
Threshold
Figure 7.4
Scatterplots of Hill estimator for daily log returns of IBM stock. Sample period is from
July 3, 1962, to December 31, 1998: upper plot is for positive returns and lower one for negative
returns.
TABLE 7.2
Maximum-Likelihood Estimates of Extreme Value Distribution for Daily
Log Returns of IBM Stock from July 3, 1962 to December 31, 1998a
Length of Subperiod
Scale αn
Location βn
Shape Par. ξn
Minimal Returns
1 mon. (n = 21, g = 437)
0.823(0.035)
1.902(0.044)
0.197(0.036)
1 qur (n = 63, g = 145)
0.945(0.077)
2.583(0.090)
0.335(0.076)
6 mon. (n = 126, g = 72)
1.147(0.131)
3.141(0.153)
0.330(0.101)
1 year (n = 252, g = 36)
1.542(0.242)
3.761(0.285)
0.322(0.127)
Maximal Returns
1 mon. (n = 21, g = 437)
0.931(0.039)
2.184(0.050)
0.168(0.036)
1 qur (n = 63, g = 145)
1.157(0.087)
3.012(0.108)
0.217(0.066)
6 mon. (n = 126, g = 72)
1.292(0.158)
3.471(0.181)
0.349(0.130)
1 year (n = 252, g = 36)
1.624(0.271)
4.475(0.325)
0.264(0.186)
aStandard errors are in parentheses.
--- page 378 ---

extreme value theory
351
from 1 month (n = 21) to 1 year (n = 252). From the table, we make the following
observations:
• Estimates of the location and scale parameters βn and αn increase in modulus
as n increases. This is expected as magnitudes of the subperiod minimum and
maximum are nondecreasing functions of n.
• Estimates of the shape parameter (or equivalently the tail index) are stable for
the negative extremes when n ≥63 and are approximately 0.33.
• Estimates of the shape parameter are less stable for the positive extremes. The
estimates are smaller in magnitude but remain signiﬁcantly different from zero.
• The results for n = 252 have higher variabilities as the number of subperiods
g is relatively small.
Again the conclusion obtained is similar to that of Longin (1996), who provided a
good illustration of applying the extreme value theory to stock market returns.
The results of Table 7.2 were obtained using a Fortran program developed by
Richard Smith and modiﬁed by the author. The package evir of R performs similar
estimation. S-Plus is also based on the evir package. I demonstrate below the
commands used. Note that the package uses subgroup maxima in the estimation so
that negative log returns are used for holding long ﬁnancial positions. Furthermore,
xi, sigma, mu in the package corresponds to (ξn, αn, βn) of the table. The estimates
obtained by R and S-Plus are close to those in Table 7.2. A source of minor
difference is that in Table 7.2 I dropped some data points at the beginning when
the sample size T is not a multiple of the subgroup size n. Consequently, results
of the R package have one more subgroup than that of Table 7.2.
R Demonstration for Extreme Value Analysis
The series is daily IBM log returns from 1962 to 1998. The following output was
edited:
> library(evir)
> help(hill)
> da=read.table("d-ibm6298.txt",header=T)
> ibm=log(da[,2]+1)*100
> nibm=-ibm
> par(mfcol=c(2,1))
<== Obtain plots
> hill(ibm,option=c("xi"),end=500)
> hill(nibm,option=c("xi"),end=500)
# A simple R program to compute Hill estimate
> source("Hill.R")
> Hill
function(x,q){
# Compute the Hill estimate of the shape parameter.
# x: data and q: the number of order statistics used.
sx=sort(x)
T=length(x)
--- page 379 ---

352
extreme values, quantiles, and value at risk
ist=T-q
y=log(sx[ist:T])
hill=sum(y[2:length(y)])/q
hill=hill-y[1]
sd=sqrt(hill^2/q)
cat("Hill estimate & std-err:",c(hill,sd),"\n")
}
> m1=Hill(ibm,190)
Hill estimate & std-err: 0.3000144 0.02176533
> m1=Hill(nibm,190)
Hill estimate & std-err: 0.2903796 0.02106635
> m1=gev(nibm,block=21)
> m1
$n.all
[1] 9190
$n
[1] 438
$data
[1] 3.2884827 3.6186920 3.9936970 ...
$block
[1] 21
$par.ests
xi
sigma
mu
0.1954537 0.8240286 1.9033817
$par.ses
xi
sigma
mu
0.03553259
0.03477151
0.04413856
$varcov
[,1]
[,2]
[,3]
[1,]
1.262565e-03
-2.831235e-05 -0.0004336771
[2,] -2.831235e-05
1.209058e-03
0.0008477562
[3,] -4.336771e-04
8.477562e-04
0.0019482125
> names(m1)
[1] "n.all" "n" "data" "block" "par.ests"
[6] "par.ses" "varcov" "converged" "nllh.final"
> plot(m1)
Make a plot selection (or 0 to exit):
1: plot: Scatterplot of Residuals
2: plot: QQplot of Residuals
Selection: 1
Deﬁne the residuals of a GEV distribution ﬁt as
wi =

1 + ξn
rn,i −βn
αn
	−1/ξn
.
--- page 380 ---

extreme value approach to var
353
••••
•
••
•
•
•
•
••
•
•
••
•
•
•••••
•
•
•
•
•
••
•
•••
•
•••
•••
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
•••
••
•
••
••••
•
•
•
•
••
•
•
••
•
•
•
••
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
••
•
•
•••
•
•
•
•
•
•
•
••
•
•
•
•
•
••
•
•
•
••
•
•
•
•
•
••••••
•
•
•••
•
•
•
•
•
••
•
•
•••
•••
•
•
•
•
••
•
•
•
•
•
•
•
•••
•
•
•
•
•
•
•
•••
•
••••
•
••••
•••
•
•
•
••
••
•
•
••
••
•
•
•
•
••••
•
•
•••
••
•
••
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
•
•••
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
••
•
•
••
•
•
•
•••••••
•••••••
•
••••
•••••
•
•
•••
•
•
•
•
•
•
•
••
•
•
••
•
•••
••
•
•
••
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
••
•
•
•
•
•
•
••
•
•
•
•
••
•
•
•••••
•
•
•
•
•
•••
•
•
•
•
•••
•
••
••
•
•
•
••
•
•
••
••
•
•
•
••
•
•
•
••
••
••
•••••
•
•
•
•
•
•
•
•
•••
Ordering
Residuals
0
100
200
300
400
0
2
4
6
••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••• ••••
•
•
•
•
0
2
4
6
0
4
6
Ordered data
Exponential quantiles
2
Figure 7.5
Residual plots from ﬁtting GEV distribution to daily negative IBM log returns, in percentage, for data from July 3, 1962, to December 31, 1998, with subperiod length of 21 days.
Using the pdf of the GEV distribution and transformation of variables, one can
easily show that {wi} should form an iid random sample of exponentially distributed
random variables if the ﬁtted model is correctly speciﬁed. Figure 7.5 shows the
residual plots of the GEV distribution ﬁt to the daily negative IBM log returns
with subperiod length of 21 days. The left panel gives the residuals and the right
panel shows a quantile-to-quantile (QQ) plot against an exponential distribution.
The plots indicate that the ﬁt is reasonable.
Remark.
Besides evir, several other packages are also available in R to perform extreme value analysis. They are evd, POT, and extRemes.
□
7.6
EXTREME VALUE APPROACH TO VAR
In this section, we discuss an approach to VaR calculation using the extreme
value theory. The approach is similar to that of Longin (1999a,b), who proposed an eight-step procedure for the same purpose. We divide the discussion
into two parts. The ﬁrst part is concerned with parameter estimation using the
method discussed in the previous subsections. The second part focuses on VaR
calculation by relating the probabilities of interest associated with different time
intervals.
--- page 381 ---

354
extreme values, quantiles, and value at risk
Part I
Assume that there are T observations of an asset return available in the sample
period. We partition the sample period into g nonoverlapping subperiods of length
n such that T = ng. If T = ng + m with 1 ≤m < n, then we delete the ﬁrst m
observations from the sample. The extreme value theory discussed in the previous
section enables us to obtain estimates of the location, scale, and shape parameters
βn, αn, and ξn for the subperiod maxima {rn,i}. Plugging the maximum-likelihood
estimates into the CDF in Eq. (7.16) with x = (r −βn)/αn, we can obtain the
quantile of a given probability of the generalized extreme value distribution. Let
p∗be a small upper tail probability that indicates the potential loss and r∗
n be
the (1 −p∗)th quantile of the subperiod maxima under the limiting generalized
extreme value distribution. Then we have
1 −p∗=



exp

−

1 + ξn(r∗n−βn)
αn
!−1/ξn"
if ξn̸ = 0,
exp

−exp

−r∗n−βn
αn
!
if ξn = 0,
where it is understood that 1 + ξn(r∗
n −βn)/αn > 0 for ξn̸ = 0. Rewriting this
equation as
ln(1 −p∗) =



−

1 + ξn(r∗n−βn)
αn
!−1/ξn
if ξn̸ = 0,
−exp

−r∗n−βn
αn

if ξn = 0,
we obtain the quantile as
r∗
n =

βn −αn
ξn
2
1 −
0
−ln(1 −p∗)
1−ξn3
if ξn̸ = 0,
βn −αn ln[−ln(1 −p∗)]
if ξn = 0.
+
(7.26)
In ﬁnancial applications, the case of ξn̸ = 0 is of major interest.
Part II
For a given upper tail probability p∗, the quantile r∗
n of Eq. (7.26) is the VaR
based on the extreme value theory for the subperiod maximum. The next step is to
make explicit the relationship between subperiod maxima and the observed return
rt series.
Because most asset returns are either serially uncorrelated or have weak serial
correlations, we may use the relationship in Eq. (7.15) and obtain
1 −p∗= P (rn,i ≤r∗
n) = [P (rt ≤r∗
n)]n.
(7.27)
This relationship between probabilities allows us to obtain VaR for the original
asset return series rt. More precisely, for a speciﬁed small upper probability p,
the (1 −p)th quantile of rt is r∗
n if the upper tail probability p∗of the subperiod
