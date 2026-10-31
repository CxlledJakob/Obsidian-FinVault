# Analysis of Financial Time Series, Third Edition (Wiley -- Ruey S_ Tsay -- Wiley series in probability and statistics, 3rd ed_, -- John Wiley & Sons, -- isbn13 9780470414354 -- 9f99b80c7b2dedd477f463dc5323f3b6 -- An.pdf — pages 381–400

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
--- page 382 ---

extreme value approach to var
355
maximum is chosen based on Eq. (7.27), where P (rt ≤r∗
n) = 1 −p. Consequently,
for a given small upper tail probability p, the VaR of a ﬁnancial position with log
return rt is
VaR =

βn −αn
ξn
2
1 −
0
−n ln(1 −p)
1−ξn3
if ξn̸ = 0
βn −αn ln[−n ln(1 −p)]
if ξn = 0,
+
(7.28)
where n is the length of the subperiod.
Summary
We summarize the approach of applying the traditional extreme value theory to
VaR calculation as follows:
1. Select the length of the subperiod n and obtain subperiod maxima {rn,i},
i = 1, . . . , g, where g = [T /n].
2. Obtain the maximum-likelihood estimates of βn, αn, and ξn.
3. Check the adequacy of the ﬁtted extreme value model; see the next section
for some methods of model checking.
4. If the extreme value model is adequate, apply Eq. (7.28) to calculate VaR.
Remark.
Since we focus on loss function so that maxima of log returns are
used in the derivation. Keep in mind that for a long ﬁnancial position, the return
series used in loss function is the negative log returns, not the traditional log
returns.
□
Example 7.6.
Consider the daily log return, in percentage, of IBM stock from
July 3, 1962, to December 31, 1998. From Table 7.2, we have ˆαn = 0.945, ˆβn =
2.583, and ˆξn = 0.335 for n = 63. Therefore, for the left-tail probability p = 0.01,
the corresponding VaR is
VaR = 2.583 −0.945
0.335
'
1 −[−63 ln(1 −0.01)]−0.335(
= 3.04969.
Thus, for daily negative log returns of the stock, the upper 1% quantile is 3.04969.
If one holds a long position on the stock worth $10 million, then the estimated VaR
with probability 1% is $10,000,000 × 0.0304969 = $304, 969. If the probability is
0.05, then the corresponding VaR is $166, 641.
If we chose n = 21 (i.e., approximately 1 month), then ˆαn = 0.823, ˆβn = 1.902,
and ˆξn = 0.197. The upper 1% quantile of the negative log returns based on the
extreme value distribution is
VaR = 1.902 −0.823
0.197{1 −[−21 ln(1 −0.01)]−0.197} = 3.40013.
--- page 383 ---

356
extreme values, quantiles, and value at risk
Therefore, for a long position of $10,000,000, the corresponding 1-day horizon VaR
is $340, 013 at the 1% risk level. If the probability is 0.05, then the corresponding
VaR is $184, 127. In this particular case, the choice of n = 21 gives higher VaR
values.
It is somewhat surprising to see that the VaR values obtained in Example 7.6
using the extreme value theory are smaller than those of Example 7.3 that uses a
GARCH(1,1) model. In fact, the VaR values of Example 7.6 are even smaller than
those based on the empirical quantile in Example 7.5. This is due in part to the
choice of probability 0.05. If one chooses probability 0.001 = 0.1% and considers the same ﬁnancial position, then we have VaR = $546,641 for the Gaussian
AR(2)–GARCH(1,1) model and VaR = $666,590 for the extreme value theory
with n = 21. Furthermore, the VaR obtained here via the traditional extreme value
theory may not be adequate because the independent assumption of daily log
returns is often rejected by statistical testings. Finally, the use of subperiod maxima overlooks the fact of volatility clustering in the daily log returns. The new
approach of extreme value theory discussed in the next section overcomes these
weaknesses.
Remark.
As shown by the results of Example 7.6, the VaR calculation based
on the traditional extreme value theory depends on the choice of n, which is the
length of subperiods. For the limiting extreme value distribution to hold, one would
prefer a large n. But a larger n means a smaller g when the sample size T is ﬁxed,
where g is the effective sample size used in estimating the three parameters αn, βn,
and ξn. Therefore, some compromise between the choices of n and g is needed. A
proper choice may depend on the returns of the asset under study. We recommend
that one should check the stability of the resulting VaR in applying the traditional
extreme value theory.
□
7.6.1
Discussion
We have applied various methods of VaR calculation to the daily log returns of
IBM stock for a long position of $10 million. Consider the VaR of the position for
the next trading day. If the probability is 5%, which means that with probability
0.95 the loss will be less than or equal to the VaR for the next trading day, then
the results obtained are
1. $302, 500 for the RiskMetrics
2. $287, 200 for a Gaussian AR(2)–GARCH(1,1) model
3. $283, 520 for an AR(2)–GARCH(1,1) model with a standardized Student-t
distribution with 5 degrees of freedom
4. $216, 030 for using the empirical quantile
5. $184, 127 for applying the traditional extreme value theory using monthly
minima (i.e., subperiod length n = 21) of the log returns (or maxima of the
negative log returns)
--- page 384 ---

extreme value approach to var
357
If the probability is 1%, then the VaR is
1. $426, 500 for the RiskMetrics
2. $409, 738 for a Gaussian AR(2)–GARCH(1,1) model
3. $475, 943 for an AR(2)–GARCH(1,1) model with a standardized Student-t
distribution with 5 degrees of freedom
4. $365, 709 for using the empirical quantile
5. $340, 013 for applying the traditional extreme value theory using monthly
minima (i.e., subperiod length n = 21)
If the probability is 0.1%, then the VaR becomes
1. $566, 443 for the RiskMetrics
2. $546, 641 for a Gaussian AR(2)–GARCH(1,1) model
3. $836, 341 for an AR(2)–GARCH(1,1) model with a standardized Student-t
distribution with 5 degrees of freedom
4. $780, 712 for using the empirical quantile
5. $666, 590 for applying the traditional extreme value theory using monthly
minima (i.e., subperiod length n = 21)
There are substantial differences among different approaches. This is not surprising because there exists substantial uncertainty in estimating tail behavior of a
statistical distribution. Since there is no true VaR available to compare the accuracy
of different approaches, we recommend that one applies several methods to gain
insight into the range of VaR.
The choice of tail probability also plays an important role in VaR calculation. For
the daily IBM stock returns, the sample size is 9190 so that the empirical quantiles
of 5 and 1% are decent estimates of the quantiles of the return distribution. In
this case, we can treat the results based on empirical quantiles as conservative
estimates of the true VaR (i.e., lower bounds). In this view, the approach based
on the traditional extreme value theory seems to underestimate the VaR for the
daily log returns of IBM stock. The conditional approach of extreme value theory
discussed in the next section overcomes this weakness.
When the tail probability is small (e.g., 0.1%), the empirical quantile is a less
reliable estimate of the true quantile. The VaR based on empirical quantiles can
no longer serve as a lower bound of the true VaR. Finally, the earlier results show
clearly the effects of using a heavy-tail distribution in VaR calculation when the
tail probability is small. The VaR based on either a Student-t distribution with 5
degrees of freedom or the extreme value distribution is greater than that based on
the normal assumption when the probability is 0.1%.
7.6.2
Multiperiod VaR
The square root of time rule of the RiskMetrics methodology becomes a special
case under the extreme value theory. The proper relationship between ℓ-day and
--- page 385 ---

358
extreme values, quantiles, and value at risk
1-day horizons is
VaR(ℓ) = ℓ1/αVaR = ℓξVaR,
where α is the tail index and ξ is the shape parameter of the extreme value distribution; see Danielsson and de Vries (1997a). This relationship is referred to as the
α root of time rule. Here α = 1/ξ, not the scale parameter αn.
For illustration, consider the daily log returns of IBM stock in Example 7.6. If
we use p = 0.01 and the results of n = 63, then for a 30-day horizon we have
VaR(30) = (30)0.335VaR = 3.125 × $304,969 = $952,997.
Because ℓ0.335 < ℓ0.5, the α root of time rule produces lower ℓ-day horizon VaR
than the square root of time rule does.
7.6.3
Return Level
Another risk measure based on the extreme values of subperiods is the return level.
The g n-subperiod return level, Ln,g, is deﬁned as the level that is exceeded in one
out of every g subperiods of length n. That is,
P (rn,i > Ln,g) = 1
g ,
where rn,i denotes subperiod maximum. The subperiod in which the return level
is exceeded is called a stress period. If the subperiod length n is sufﬁciently large
so that normalized rn,i follows the GEV distribution, then the return level is
Ln,g = βn −αn
ξn

1 −

−ln

1 −1
g
	−ξn+
,
provided that ξn̸ = 0. Note that this is precisely the quantile of extreme value
distribution given in Eq. (7.26) with tail probability p∗= 1/g, even though we
write it in a slightly different way. Thus, return level applies to the subperiod
maximum, not to the underlying returns. This marks the difference between VaR
and return level.
For the daily negative IBM log returns with subperiod length of 21 days, we can
use the ﬁtted model to obtain the return level for 12 such subperiods (i.e., g = 12).
The return level is 4.4835%.
R and S-Plus Commands for Obtaining Return Level
> m1=gev(nibm,block=21)
# S-Plus output
> rl.21.12=rlevel.gev(m1, k.blocks=12, type=’profile’)
> class(rl.21.12)
[1] "list"
--- page 386 ---

new approach based on the extreme value theory
359
> names(rl.21.12)
[1] "Range" "rlevel"
> rl.21.12$rlevel
[1] 4.483506
# R output
> rl.21.12=rlevel.gev(m1,k.blocks=12)
> rl.21.12
[1] 4.177923 4.481976 4.858102
In the prior demonstration, the number of subperiods is denoted by k.blocks
and the subcommand, type = ‘profile’, produces a plot of the proﬁle loglikelihood conﬁdence interval for the return level. The plot is not shown here.
7.7
NEW APPROACH BASED ON THE EXTREME VALUE THEORY
The aforementioned approach to VaR calculation using the extreme value theory
encounters some difﬁculties. First, the choice of subperiod length n is not clearly
deﬁned. Second, the approach is unconditional and, hence, does not take into consideration effects of other explanatory variables. To overcome these difﬁculties, a
modern approach to extreme value theory has been proposed in the statistical literature; see Davison and Smith (1990) and Smith (1989). Instead of focusing on the
extremes (maximum or minimum), the new approach focuses on exceedances of
the measurement over some high threshold and the times at which the exceedances
occur. Thus, this new approach is also referred to as peaks over thresholds (POT).
For illustration, consider the daily returns of IBM stock used in this chapter and
a long position on the stock. Denote the negative daily log return by rt. Let η
be a prespeciﬁed high threshold. We may choose η = 2.5%. Suppose that the ith
exceedance occurs at day ti (i.e., rti ≤η). Then the new approach focuses on the
data (ti, rti −η). Here rti −η is the exceedance over the threshold η and ti is the
time at which the ith exceedance occurs. Similarly, for a short position, we may
choose η = 2% and focus on the data (ti, rti −η) for which rti ≥η.
In practice, the occurrence times {ti} provide useful information about the intensity of the occurrence of important “rare events” (e.g., less than the threshold η for
a long position). A cluster of ti indicates a period of large market declines. The
exceeding amount (or exceedance) rti −η is also of importance as it provides the
actual quantity of interest.
Based on the prior introduction, the new approach does not require the choice
of a subperiod length n, but it requires the speciﬁcation of threshold η. Different
choices of the threshold η lead to different estimates of the shape parameter k
(and hence the tail index 1/ξ). In the literature, some researchers believe that
the choice of η is a statistical problem as well as a ﬁnancial one, and it cannot
be determined based purely on statistical theory. For example, different ﬁnancial
institutions (or investors) have different risk tolerances. As such, they may select
different thresholds even for an identical ﬁnancial position. For the daily log returns
--- page 387 ---

360
extreme values, quantiles, and value at risk
of IBM stock considered in this chapter, the calculated VaR is not sensitive to the
choice of η.
The choice of threshold η also depends on the observed log returns. For a
stable return series, η = 2.5% may fare well for a long position. For a volatile
return series (e.g., daily returns of a dot-com stock), η may be as high as 10%.
Limited experience shows that η can be chosen so that the number of exceedances
is sufﬁciently large (e.g., about 5% of the sample). For a more formal study on the
choice of η, see Danielsson and de Vries (1997b).
7.7.1
Statistical Theory
Again consider the log return rt of an asset. Suppose that the ith exceedance
occurs at ti. Focusing on the exceedance rt −η and exceeding time ti results in a
fundamental change in statistical thinking. Instead of using the marginal distribution
(e.g., the limiting distribution of the minimum or maximum), the new approach
employs a conditional distribution to handle the magnitude of exceedance given
that the measurement exceeds a threshold. The chance of exceeding the threshold
is governed by a probability law. In other words, the new approach considers the
conditional distribution of x = rt −η given rt ≤η for a long position. Occurrence
of the event {rt ≤η} follows a point process (e.g., a Poisson process). See Section
6.9 for the deﬁnition of a Poisson process. In particular, if the intensity parameter
λ of the process is time invariant, then the Poisson process is homogeneous. If λ is
time variant, then the process is nonhomogeneous. The concept of Poisson process
can be generalized to the multivariate case.
The basic theory of the new approach is to consider the conditional distribution
of r = x + η given r > η for the limiting distribution of the maximum given in
Eq. (7.16). Since there is no need to choose the subperiod length n, we do not use
it as a subscript of the parameters. Then the conditional distribution of r ≤x + η
given r > η is
Pr(r ≤x + η|r > η) = Pr(η ≤r ≤x + η)
Pr(r > η)
= Pr(r ≤x + η) −Pr(r ≤η)
1 −Pr(r ≤η)
. (7.29)
Using the CDF F∗(·) of Eq. (7.16) and the approximation e−y ≈1 −y and after
some algebra, we obtain that
Pr(r ≤x + η|r > η) = F∗(x + η) −F∗(η)
1 −F∗(η)
=
exp

−

1 + ξ(x+η−β)
α
!−1/ξ"
−exp

−

1 + ξ(η−β)
α
!−1/ξ"
1 −exp

−

1 + ξ(η−β)
α
!−1/ξ"
≈1 −

1 +
ξx
α + ξ(η −β)
−1/ξ
,
(7.30)
--- page 388 ---

new approach based on the extreme value theory
361
where x > 0 and 1 + ξ(η −β)/α > 0. As is seen later, this approximation makes
explicit the connection of the new approach to the traditional extreme value theory.
The case of ξ = 0 is taken as the limit of ξ →0 so that
Pr(r ≤x + η|r > η) ≈1 −exp(−x/α).
The distribution with cumulative distribution function
Gξ,ψ(η)(x) =



1 −

1 +
ξx
ψ(η)
!−1/ξ
for ξ̸ = 0,
1 −exp[−x/ψ(η)]
for ξ = 0,
(7.31)
where ψ(η) > 0, x ≥0 when ξ ≥0, and 0 ≤x ≤−ψ(η)/ξ when ξ < 0, is called
the generalized Pareto distribution (GPD). Thus, the result of Eq. (7.30) shows that
the conditional distribution of r given r > η is well approximated by a GPD with
parameters ξ and ψ(η) = α + ξ(η −β). See Embrechts et al. (1997) for further
information. An important property of the GPD is as follows. Suppose that the
excess distribution of r given a threshold ηo is a GPD with shape parameter ξ
and scale parameter ψ(ηo). Then, for an arbitrary threshold η > ηo, the excess
distribution over the threshold η is also a GPD with shape parameter ξ and scale
parameter ψ(η) = ψ(ηo) + ξ(η −ηo).
When ξ = 0, the GPD in Eq. (7.31) reduces to an exponential distribution. This
result motivates the use of a QQ plot of excess returns over a threshold against
exponential distribution to infer the tail behavior of the returns. If ξ = 0, then the
QQ plot should be linear. Figure 7.6(a) shows the QQ plot of daily negative IBM
log returns used in this chapter with threshold 0.025. The nonlinear feature of the
plot clearly shows that the left tail of the daily IBM log returns is heavier than that
of a normal distribution, that is, ξ̸ = 0.
R and S-Plus Commands Used to Produce Figure 7.6
> par(mfcol=c(2,1))
> qplot(-ibm,threshold=0.025,main=’Negative daily IBM
log returns’)
> meplot(-ibm)
> title(main=’Mean excess plot’)
7.7.2
Mean Excess Function
Given a high threshold ηo, suppose that the excess r −ηo follows a GPD with
parameter ξ and ψ(ηo), where 0 < ξ < 1. Then the mean excess over the threshold
ηo is
E(r −ηo|r > ηo) = ψ(ηo)
1 −ξ .
--- page 389 ---

362
extreme values, quantiles, and value at risk
•••••••••••••••••••••••••••••••••••••••••••••••• ••••• • •• •• ••
•
•
•
0.05
0.10
0.15
0.20
0.25
0
1
2
3
4
5
6
Ordered data
(a)
Exponential quantiles
•
••
•• •
•••• •••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••• •• •• • • •• •• •
•
−0.10
−0.05
0.0
0.05
0.10
0.02
0.06
0.10
Threshold
(b)
Mean excess
Figure 7.6
Plots for daily negative IBM log returns from July 3, 1962, to December 31, 1998. (a)
QQ plot of excess returns over threshold 2.5% and (b) mean excess plot.
For any η > ηo, deﬁne the mean excess function e(η) as
e(η) = E(r −η|r > η) = ψ(ηo) + ξ(η −ηo)
1 −ξ
.
In other words, for any y > 0,
e(ηo + y) = E[r −(ηo + y)|r > ηo + y] = ψ(ηo) + ξy
1 −ξ
.
Thus, for a ﬁxed ξ, the mean excess function is a linear function of y = η −ηo.
This result leads to a simple graphical method to infer the appropriate threshold
value ηo for the GPD. Deﬁne the empirical mean excess function as
eT (η) = 1
Nη
Nη

i=1
(rti −η),
(7.32)
where Nη is the number of returns that exceed η and rti are the values of the
corresponding returns. See the next subsection for more information on the notation.
The scatterplot of eT (η) against η is called the mean excess plot, which should be
linear in η for η > ηo under the GPD. The plot is also called mean residual life plot.
--- page 390 ---

new approach based on the extreme value theory
363
Figure 7.6(b) shows the mean excess plot of the daily negative IBM log returns. It
shows that, among others, a threshold of about 3% is reasonable for the negative
return series. In the evir package of R and S-Plus, the command for mean excess
plot is meplot.
7.7.3
New Approach to Modeling Extreme Values
Using the statistical result in Eq. (7.30) and considering jointly the exceedances
and exceeding times, Smith (1989) proposes a two-dimensional Poisson process
to model (ti, rti). This approach was used by Tsay (1999) to study VaR in risk
management. We follow the same approach.
Assume that the baseline time interval is D, which is typically a year. In the
United States, D = 252 is used as there are typically 252 trading days in a year.
Let t be the time interval of the data points (e.g., daily) and denote the data span by
t = 1, 2, . . . , T , where T is the total number of data points. For a given threshold
η, the exceeding times over the threshold are denoted by {ti, i = 1, . . . , Nη} and
the observed log return at ti is rti. Consequently, we focus on modeling {(ti, rti)}
for i = 1, . . . , Nη, where Nη depends on the threshold η.
The new approach to applying the extreme value theory is to postulate that
the exceeding times and the associated returns [i.e., (ti, rti)] jointly form a twodimensional Poisson process with intensity measure given by
[(D2, D1) × (r, ∞)] = D2 −D1
D
S(r; ξ, α, β),
(7.33)
where
S(r; ξ, α, β) =

1 + ξ(r −β)
α
−1/ξ
+
,
0 ≤D1 ≤D2 ≤T , r > η, α > 0, β, and ξ are parameters, and the notation [x]+
is deﬁned as [x]+ = max(x, 0). This intensity measure says that the occurrence of
exceeding the threshold is proportional to the length of the time interval [D1, D2]
and the probability is governed by a survival function similar to the exponent of
the CDF F∗(r) in Eq. (7.16). A survival function of a random variable X is deﬁned
as S(x) = Pr(X > x) = 1 −Pr(X ≤x) = 1 −CDF(x). When ξ = 0, the intensity
measure is taken as the limit of ξ →0; that is,
[(D2, D1) × (r, ∞)] = D2 −D1
D
exp

−(r −β)
α

.
In Eq. (7.33), the length of time interval is measured with respect to the baseline
interval D.
--- page 391 ---

364
extreme values, quantiles, and value at risk
The idea of using the intensity measure in Eq. (7.33) becomes clear when one
considers its implied conditional probability of r = x + η given r > η over the time
interval [0, D], where x > 0,
[(0, D) × (x + η, ∞)]
[(0, D) × (η, ∞)]
=

1 + ξ(x + η −β)/α
1 + ξ(η −β)/α
−1/ξ
=

1 +
ξx
α + ξ(η −β)
−1/ξ
,
which is precisely the survival function of the conditional distribution given in
Eq. (7.30). This survival function is obtained from the extreme limiting distribution
for maximum in Eq. (7.16). We use survival function here because it denotes the
probability of exceedance.
The relationship between the limiting extreme value distribution in Eq. (7.16)
and the intensity measure in Eq. (7.33) directly connects the new approach of
extreme value theory to the traditional one.
Mathematically, the intensity measure in Eq. (7.33) can be written as an integral
of an intensity function:
[(D2, D1) × (r, ∞)] =
 D2
D1
 ∞
r
λ(t, z; ξ, α, β) dz dt,
where the intensity function λ(t, z; ξ, α, β) is deﬁned as
λ(t, z; ξ, α, β) = 1
D g(z; ξ, α, β),
(7.34)
where
g(z; ξ, α, β) =



1
α

1 + ξ(z−β)
α
!−(1+ξ)/ξ
if ξ̸ = 0,
1
α exp

−(z−β)
α
!
if ξ = 0.
Using the results of a Poisson process, we can write down the likelihood function
for the observed exceeding times and their corresponding returns {(ti, rti)} over the
two-dimensional space [0, T ] × (η, ∞) as
L(ξ, α, β) =


Nη

i=1
1
D g(rti; ξ, α, β)

exp

−T
D S(η; ξ, α, β)

.
(7.35)
The parameters ξ, α, and β can then be estimated by maximizing the logarithm of
this likelihood function. Since the scale parameter α is nonnegative, we use ln(α)
in the estimation.
Example 7.7.
Consider again the daily log returns of IBM stock from July 3,
1962, to December 31, 1998. There are 9190 daily returns. Table 7.3 gives some
--- page 392 ---

new approach based on the extreme value theory
365
TABLE 7.3
Estimation Results of a Two-Dimensional Homogeneous Poisson Model
for Daily Negative Log Returns of IBM Stock from July 3, 1962 to December 31,
1998a
Thr.
Exc.
Shape Parameter ξ
Log(Scale) ln(α)
Location β
Original Log Returns
3.0%
175
0.30697(0.09015)
0.30699(0.12380)
4.69204(0.19058)
2.5%
310
0.26418(0.06501)
0.31529(0.11277)
4.74062(0.18041)
2.0%
554
0.18751(0.04394)
0.27655(0.09867)
4.81003(0.17209)
Removing the Sample Mean
3.0%
184
0.30516(0.08824)
0.30807(0.12395)
4.73804(0.19151)
2.5%
334
0.28179(0.06737)
0.31968(0.12065)
4.76808(0.18533)
2.0%
590
0.19260(0.04357)
0.27917(0.09913)
4.84859(0.17255)
aThe baseline time interval is 252 (i.e., 1 year). The numbers in parentheses are standard errors, where
Thr. and Exc. stand for threshold and the number of exceedings.
estimation results of the parameters ξ, α, and β for three choices of the threshold
when the negative series {−rt} is used. As mentioned before, we use the negative
series {−rt}, instead of {rt} because we focus on holding a long ﬁnancial position.
The table also shows the number of exceeding times for a given threshold. It is seen
that the chance of dropping 2.5% or more in a day for IBM stock occurred with
probability 310/9190 ≈3.4%. Because the sample mean of IBM stock returns
is not zero, we also consider the case when the sample mean is removed from
the original daily log returns. From the table, removing the sample mean has
little impact on the parameter estimates. These parameter estimates are used next
to calculate VaR, keeping in mind that in a real application one needs to check
carefully the adequacy of a ﬁtted Poisson model. We discuss methods of model
checking in the next section.
7.7.4
VaR Calculation Based on the New Approach
As shown in Eq. (7.30), the two-dimensional Poisson process model used, which
employs the intensity measure in Eq. (7.33), has the same parameters as those
of the extreme value distribution in Eq. (7.16). Therefore, one can use the same
formula as that of Eq. (7.28) to calculate VaR of the new approach. More speciﬁ-
cally, for a given upper tail probability p, the (1 −p)th quantile of the log return
rt is
VaR =

β −α
ξ
2
1 −
0
−D ln(1 −p)
1−ξ3
if ξ̸ = 0,
β −α ln[−D ln(1 −p)]
if ξ = 0,
(7.36)
where D is the baseline time interval used in estimation. In the United States, one
typically uses D = 252, which is approximately the number of trading days in a
year.
--- page 393 ---

366
extreme values, quantiles, and value at risk
Example 7.8.
Consider again the case of holding a long position of IBM stock
valued at $10 million. We use the estimation results of Table 7.3 to calculate 1-day
horizon VaR for the tail probabilities of 0.05 and 0.01.
• Case I: Use the original daily log returns. The three choices of threshold η
result in the following VaR values:
1. η = 3.0%: VaR(5%) = $228,239, VaR(1%) = $359.303.
2. η = 2.5%: VaR(5%) = $219,106, VaR(1%) = $361,119.
3. η = 2.0%: VaR(5%) = $212,981, VaR(1%) = $368.552.
• Case II: The sample mean of the daily log returns is removed. The three
choices of threshold η result in the following VaR values:
1. η = 3.0%: VaR(5%) = $232,094, VaR(1%) = $363,697.
2. η = 2.5%: VaR(5%) = $225,782, VaR(1%) = $364,254.
3. η = 2.0%: VaR(5%) = $217,740, VaR(1%) = $372,372.
As expected, removing the sample mean, which is positive, slightly increases the
VaR. However, the VaR is rather stable among the three threshold values used. In
practice, we recommend that one removes the sample mean ﬁrst before applying
this new approach to VaR calculation.
Discussion.
Compared with the VaR of Example 7.6 that uses the traditional
extreme value theory, the new approach provides a more stable VaR calculation. The traditional approach is rather sensitive to the choice of the subperiod
length n.
□
The command pot of the R package evir can be used to perform the estimation
of the POT model. We demonstrate it below using the negative log returns of IBM
stock. As expected, the results are very close to those obtained before.
R Demonstration Using POT Command
> library(evir)
> m3=pot(nibm,0.025)
> m3
$n
[1] 9190
$period
[1]
1 9190
$data
[1] 0.03288483 0.02648772 0.02817316 .....
$span
[1] 9189
$threshold
--- page 394 ---

new approach based on the extreme value theory
367
[1] 0.025
$p.less.thresh
[1] 0.9662677
$n.exceed
[1] 310
$par.ests
xi
sigma
mu
beta
0.264078835 0.003182365 0.007557534 0.007788551
$par.ses
xi
sigma
mu
0.0229175739 0.0001808472 0.0007675515
$varcov
[,1]
[,2]
[,3]
[1,]
5.252152e-04 -2.873160e-06 -6.970497e-07
[2,] -2.873160e-06
3.270571e-08 -7.907532e-08
[3,] -6.970497e-07 -7.907532e-08
5.891353e-07
$intensity
%intensity function of exceeding the threshold
[1] 0.03373599
> plot(m3)
% model checking
Make a plot selection (or 0 to exit):
1: plot: Point Process of Exceedances
2: plot: Scatterplot of Gaps
3: plot: Qplot of Gaps
4: plot: ACF of Gaps
5: plot: Scatterplot of Residuals
6: plot: Qplot of Residuals
7: plot: ACF of Residuals
8: plot: Go to GPD Plots
Selection:
> riskmeasures(m3,c(0.95,0.99,0.999))
p
quantile
sfall
[1,] 0.950 0.02208860 0.03162728
[2,] 0.990 0.03616686 0.05075740
[3,] 0.999 0.07019419 0.09699513
7.7.5
Alternative Parameterization
As mentioned before, for a given threshold η, the GPD can also be parameterized
by the shape parameter ξ and the scale parameter ψ(η) = α + ξ(η −β). This
is the parameterization used in the evir package of R and S-Plus. Speciﬁcally,
(xi,beta) of R and S-Plus corresponds to [ξ, ψ(η)] of this chapter. The command
for estimating a GPD model in R and S-Plus is gpd. The output format for S-Plus
is slightly different from that of R. For illustration, consider the daily negative IBM
log return series from 1962 to 1998. The results of R are given below.
--- page 395 ---

368
extreme values, quantiles, and value at risk
R Demonstration
Data are negative IBM log returns. The following output was edited:
> library(evir)
> mgpd=gpd(nibm,threshold=0.025)
> names(mgpd)
[1] "n"
"data"
"threshold"
"p.less.thresh"
[5] "n.exceed"
"method"
"par.ests"
"par.ses"
[9] "varcov"
"information" "converged" "nllh.final"
> mgpd
$n
[1] 9190
$data
[1] 0.03288483 0.02648772 0.02817316 0.03618692 ....
$threshold
[1] 0.025
$p.less.thresh
%Percentage of data below the threshold.
[1] 0.9662677
$n.exceed
% Number of exceedances
[1] 310
$method
[1] "ml"
$par.ests
xi
beta
0.264184649 0.007786063
$par.ses
xi
beta
0.0662137508 0.0006427826
$varcov
[,1]
[,2]
[1,]
4.384261e-03 -2.461142e-05
[2,] -2.461142e-05
4.131694e-07
> par(mfcol=c(2,2)) %Plots for residual analysis
> plot(mgpd)
Make a plot selection (or 0 to exit):
1: plot: Excess Distribution
2: plot: Tail of Underlying Distribution
3: plot: Scatterplot of Residuals
4: plot: QQplot of Residuals
Selection:
Note that the results are very close to those in Table 7.3, where percentage log
returns are used. The estimates of ξ and ψ(η) are 0.26418 and α + ξ(η −β) =
exp(0.31529) + (0.26418)(2.5 −4.7406) = 0.77873, respectively, in Table 7.3. In
terms of log returns, the estimate of ψ(η) is 0.007787, which is the same as the R
and S-Plus estimate.
--- page 396 ---

new approach based on the extreme value theory
369
••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••• ••
•
0.1
0.2 0.3
0.0 0.2 0.4 0.6 0.8 1.0
x (on log scale)
Fu(x−u)
•••••••••••••••••••••••••••••••••••••••••••••••••••••• ••
•
0.1
0.2 0.3
0.00001 0.00100
x (on log scale)
1−F(x) (on log scale)
•••
•••
•
••••••
•
•••••••••
••••••••
•
••
•
•
•
•
••
•
••
••
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
••
•••••
•
••
••
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
••••••••••••
•
•••••
•
•
•
•••••
•••
••••
•••••••
••
••••••
••
•
••
••
•••
•••
•••
••••••
•
••
•
•
••
•••
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
••
•
•••
••
•
•
•••
•
••••
•
•
•
•
•
•
••
•
•••••
•
•
••
•
•
•••
•
••
•••••
•
••••
•
•
••
•
••
•
•
•
•
•••
•
••
•
••
•
•
•
•
•••••••
•••
•
•
•
•
•••
•
••
•
••
••
•
•
•
•••
Ordering
Residuals
0
50
100 150 200 250 300
0
2
4
6
8
••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••• • •
•
0
2
4
6
8
0
1
2
3
4
5
6
Ordered data
Exponential Quantiles
Figure 7.7
Diagnostic plots for GPD ﬁt to daily negative log returns of IBM stock from July 3, 1962,
to December 31, 1998.
Figure 7.7 shows the diagnostic plots for the GPD ﬁt to the daily negative log
returns of IBM stock. The QQ plot (lower right panel) and the tail probability
estimate (in log scale and in the lower left panel) show some minor deviation from
a straight line, indicating further improvement is possible.
From the conditional distributions in Eqs. (7.29) and (7.30) and the GPD in Eq.
(7.31), we have
F(y) −F(η)
1 −F(η)
≈Gη,ψ(η)(x),
where y = x + η with x > 0. If we estimate the CDF F(η) of the returns by the
empirical CDF, then
ˆF(η) = T −Nη
T
,
where Nη is the number of exceedances of the threshold η and T is the sample
size. Consequently, by Eq. (7.31),
F(y) = F(η) + G(x)[1 −F(η)]
≈1 −Nη
T

1 + ξ(y −η)
ψ(η)
−1/ξ
.
--- page 397 ---

370
extreme values, quantiles, and value at risk
This leads to an alternative estimate of the quantile of F(y) for use in VaR calculation. Speciﬁcally, for a small upper tail probability p, let q = 1 −p. Then, by
solving for y, we can estimate the qth quantile of F(y), denoted by VaRq, by
VaRq = η −ψ(η)
ξ

1 −

 T
Nη
(1 −q)
−ξ+
,
(7.37)
where, as before, η is the threshold, T is the sample size, Nη is the number of
exceedances, and ψ(η) and ξ are the scale and shape parameters of the GPD
distribution. This method to VaR calculation is used in R and S-Plus.
As mentioned before in Section 7.2.3, expected shortfall (ES) associated with a
given VaR is a useful risk measure. It is deﬁned as the expected loss given that the
VaR is exceeded. For generalized Pareto distribution, ES assumes a simple form.
Speciﬁcally, for a given tail probability p, let q = 1 −p and denote the value at
risk by VaRq. Then, the expected shortfall is deﬁned by
ESq = E(r|r > VaRq) = VaRq + E(r −VaRq|r > VaRq).
(7.38)
Using properties of the GPD, it can be shown that
E(r −VaRq|r > VaRq) = ψ(η) + ξ(VaRq −η)
1 −ξ
,
provided that 0 < ξ < 1. Consequently, we have
ESq = VaRq
1 −ξ + ψ(η) −ξη
1 −ξ
.
To illustrate the new method to VaR and ES calculations, we again use the daily
negative log returns of IBM stock with threshold 2.5%. In the evir package of
R and S-Plus, the command to compute VaR and ES via the peak over threshold
method is riskmeasures:
> riskmeasures(mgpd,c(0.95,0.99,0.999))
p
quantile
sfall
[1,] 0.950 0.02208959 0.03162619
[2,] 0.990 0.03616405 0.05075390
[3,] 0.999 0.07018944 0.09699565
From the output, the VaR values for the ﬁnancial position of $10 million are
$220, 889 and $361, 661, respectively, for tail probability of 0.05 and 0.01. These
two values are rather close to those given in Example 7.8 that are based on the
method of the previous section. The expected shortfalls for the ﬁnancial position
are $316, 272 and $507, 576, respectively, for tail probability of 0.05 and 0.01.
--- page 398 ---

new approach based on the extreme value theory
371
7.7.6
Use of Explanatory Variables
The two-dimensional Poisson process model discussed earlier is homogeneous
because the three parameters ξ, α, and β are constant over time. In practice, such
a model may not be adequate. Furthermore, some explanatory variables are often
available that may inﬂuence the behavior of the log returns rt. A nice feature of
the new extreme value theory approach to VaR calculation is that it can easily
take explanatory variables into consideration. We discuss such a framework in this
section. In addition, we also discuss methods that can be used to check the adequacy
of a ﬁtted two-dimensional Poisson process model.
Suppose that xt = (x1t, . . . , xvt)′ is a vector of v explanatory variables that are
available prior to time t. For asset returns, the volatility σ 2
t of rt discussed in
Chapter 3 is an example of explanatory variables. Another example of explanatory
variables in the U.S. equity markets is an indicator variable denoting the meetings
of the Federal Open Market Committee. A simple way to make use of explanatory
variables is to postulate that the three parameters ξ, α, and β are time varying and
are linear functions of the explanatory variables. Speciﬁcally, when explanatory
variables xt are available, we assume that
ξt = γ0 + γ1x1t + · · · + γvxvt ≡γ0 + γ ′xt,
ln(αt) = δ0 + δ1x1t + · · · + δvxvt ≡δ0 + δ′xt,
(7.39)
βt = θ0 + θ1x1t + · · · + θvxvt ≡θ0 + θ′xt.
If γ = 0, then the shape parameter ξt = γ0, which is time invariant. Thus, testing the
signiﬁcance of γ can provide information about the contribution of the explanatory
variables to the shape parameter. Similar methods apply to the scale and location
parameters. In Eq. (7.39), we use the same explanatory variables for all three
parameters ξt, ln(αt), and βt. In an application, different explanatory variables may
be used for different parameters.
When the three parameters of the extreme value distribution are time varying,
we have an inhomogeneous Poisson process. The intensity measure becomes
[(D1, D2) × (r, ∞)] = D2 −D1
D

1 + ξt(r −βt)
αt
−1/ξt
+
,
r > η.
(7.40)
The likelihood function of the exceeding times and returns {(ti, rti)} becomes
L =


Nη

i=1
1
D g(rti; ξti, αti, βti)

exp

−1
D
 T
0
S(η; ξt, αt, βt)dt

,
which reduces to
L =


Nη

i=1
1
D g(rti; ξti, αti, βti)

exp

−1
D
T

t=1
S(η; ξt, αt, βt)

(7.41)
--- page 399 ---

372
extreme values, quantiles, and value at risk
if one assumes that the parameters ξt, αt, and βt are constant within each trading
day, where g(z; ξt, αt, βt) and S(η; ξt, αt, βt) are given in Eqs. (7.34) and (7.33),
respectively. For given observations {rt, xt|t = 1, . . . , T }, the baseline time interval
D, and the threshold η, the parameters in Eq. (7.39) can be estimated by maximizing
the logarithm of the likelihood function in Eq. (7.41). Again we use ln(αt) to satisfy
the positive constraint of αt.
Remark.
The parameterization in Eq. (7.39) is similar to that of the volatility
models of Chapter 3 in the sense that the three parameters are exact functions of the
available information at time t. Other functions can be used if necessary.
□
7.7.7
Model Checking
Checking an entertained two-dimensional Poisson process model for exceedance
times and excesses involves examining three key features of the model. The
ﬁrst feature is to verify the adequacy of the exceedance rate, the second
feature is to examine the distribution of exceedances, and the ﬁnal feature is
to check the independence assumption of the model. We discuss brieﬂy some
statistics that are useful for checking these three features. These statistics are
based on some basic statistical theory concerning distributions and stochastic
processes.
Exceedance Rate
A fundamental property of univariate Poisson processes is that the time durations
between two consecutive events are independent and exponentially distributed. To
exploit a similar property for checking a two-dimensional process model, Smith
and Shively (1995) propose examining the time durations between consecutive
exceedances. If the two-dimensional Poisson process model is appropriate for
the exceedance times and excesses, the time duration between the ith and (i −1)th
exceedances should follow an exponential distribution. More speciﬁcally, letting
t0 = 0, we expect that
zti =
 ti
ti−1
1
D g(η; ξs, αs, βs) ds,
i = 1, 2, . . .
are iid as a standard exponential distribution. Because daily returns are discrete-time
observations, we employ the time durations
zti = 1
D
ti

t=ti−1+1
S(η; ξt, αt, βt)
(7.42)
and use the QQ plot to check the validity of the iid standard exponential distribution.
If the model is adequate, the QQ plot should show a straight line through the origin
with unit slope.
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
