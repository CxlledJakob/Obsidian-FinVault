# Analysis of Financial Time Series, Third Edition (Wiley -- Ruey S_ Tsay -- Wiley series in probability and statistics, 3rd ed_, -- John Wiley & Sons, -- isbn13 9780470414354 -- 9f99b80c7b2dedd477f463dc5323f3b6 -- An.pdf — pages 210–229

--- page 210 ---

nonlinear models
183
Year
Log return
1970
1980
1990
2000
20
10
0
10
Figure 4.3
Time plot of daily log returns for IBM stock from July 3, 1962, to December 31, 2003.
are 0.015 and 0.010, and those of the volatility equation are 0.004, 0.003, and
0.003, respectively. All estimates are statistically signiﬁcant at the 5% level.
The Ljung–Box statistics of the standardized residuals give Q(10) = 5.19(0.82)
and Q(20) = 24.38(0.18), where the number in parentheses denotes the p value
obtained using χ2
m−1 distribution because of the estimated AR(2) coefﬁcient.
For the squared standardized residuals, we obtain Q(10) = 11.67(0.31) and
Q(20) = 18.25(0.57). The model is adequate in modeling the serial dependence
and conditional heteroscedasticity of the data. But the unconditional mean for
rt of model (4.12) is 0.060, which is substantially larger than the sample mean
0.039, indicating that the model might be misspeciﬁed.
Next, we employ the TGARCH model of Chapter 3 and obtain
rt = 0.014 −0.028rt−2 + at,
at = σtϵt,
σ 2
t = 0.075 + 0.081Pt−1a2
t−1 + 0.157Nt−1a2
t−1 + 0.863σ 2
t−1,
(4.13)
where Pt−1 = 1 −Nt−1, Nt−1 is the indicator for negative at−1 such that Nt−1 = 1
if at−1 < 0 and = 0 otherwise, the standard errors of the parameters in the mean
equation are 0.013 and 0.009, and those of the volatility equation are 0.007,
0.008, 0.010, and 0.010, respectively. All estimates except the constant term of
the mean equation are signiﬁcant. Let ˜at be the standardized residuals of model
(4.13). We have Q(10) = 2.47(0.98) and Q(20) = 25.90(0.13) for the {˜at} series
--- page 211 ---

184
nonlinear models and their applications
and Q(10) = 97.07(0.00) and Q(20) = 170.3(0.00) for {˜a2
t }. The model fails to
describe the conditional heteroscedasticity of the data.
The idea of TAR models can be used to reﬁne the prior TGARCH model by
allowing for increased ﬂexibility in modeling the asymmetric response in volatility.
More speciﬁcally, we consider an AR(2)−TAR−GARCH(1,1) model for the series
and obtain
rt = 0.033 −0.023rt−2 + at,
at = σtϵt,
σ 2
t = 0.075 + 0.041a2
t−1 + 0.903σ 2
t−1
+ (0.030a2
t−1 + 0.062σ 2
t−1)Nt−1,
(4.14)
where Nt−1 is deﬁned in Eq. (4.13). All estimates in model (4.14) are signiﬁcantly
different from zero at the usual 1% level. Let ˆat be the standardized residuals of
model (4.14). We obtain Q(10) = 6.09(0.73) and Q(20) = 25.29(0.15) for {ˆat}
and Q(10) = 13.54(0.20) and Q(20) = 19.56(0.49) for {ˆa2
t }. Thus, model (4.14)
is adequate in modeling the serial correlation and conditional heteroscedasticity
of the daily log returns of IBM stock considered. The unconditional mean return
of model (4.14) is 0.033, which is much closer to the sample mean 0.039 than
those implied by models (4.12) and (4.13). Comparing the two ﬁtted TGARCH
models, we see that the asymmetric behavior in daily IBM stock volatility is much
stronger than what is allowed in a GJR model. Speciﬁcally, the coefﬁcient of σ 2
t−1
also depends on the sign of at−1. Note that model (4.14) can be further reﬁned by
imposing the constraint that the sum of the coefﬁcients of a2
t−1 and σ 2
t−1 is one
when at−1 < 0.
Remark.
A RATS program to estimate the AR(2)−TAR−GARCH(1,1) model
used is given in Appendix A. The results might be slightly different from those of
SCA given in the text.
□
4.1.3
Smooth Transition AR (STAR) Model
A criticism of the SETAR model is that its conditional mean equation is not continuous. The thresholds {γj} are the discontinuity points of the conditional mean
function µt. In response to this criticism, smooth TAR models have been proposed;
see Chan and Tong (1986) and Ter¨asvirta (1994) and the references therein. A time
series xt follows a 2-regime STAR(p) model if it satisﬁes
xt = c0 +
p

i=1
φ0,ixt−i + F
xt−d −
s
	 
c1 +
p

i=1
φ1,ixt−i

+ at,
(4.15)
where d is the delay parameter,
 and s are parameters representing the location and
scale of model transition, and F(·) is a smooth transition function. In practice, F(·)
often assumes one of three forms—namely, logistic, exponential, or a cumulative
--- page 212 ---

nonlinear models
185
distribution function. From Eq. (4.15) and with 0 ≤F(·) ≤1, the conditional mean
of a STAR model is a weighted linear combination between the following two
equations:
µ1t = c0 +
p

i=1
φ0,ixt−i,
µ2t = (c0 + c1) +
p

i=1
(φ0,i + φ1,i)xt−i.
The weights are determined in a continuous manner by F[(xt−d −
)/s]. The
prior two equations also determine properties of a STAR model. For instance, a
prerequisite for the stationarity of a STAR model is that all zeros of both AR
polynomials are outside the unit circle. An advantage of the STAR model over
the TAR model is that the conditional mean function is differentiable. However,
experience shows that the transition parameters
 and s of a STAR model are hard
to estimate. In particular, most empirical studies show that standard errors of the
estimates of
 and s are often quite large, resulting in t ratios of about 1.0; see
Ter¨asvirta (1994). This uncertainty leads to various complications in interpreting
an estimated STAR model.
Example 4.4.
To illustrate the application of STAR models in ﬁnancial time
series analysis, we consider the monthly simple stock returns for Minnesota Mining
and Manufacturing (3M) Company from February 1946 to December 2008. If
ARCH models are entertained, we obtain the following ARCH(2) model:
Rt = 0.013 + at,
at = σtϵt,
σ 2
t = 0.003 + 0.088a2
t−1 + 0.109a2
t−2,
(4.16)
where standard errors of the estimates are 0.002, 0.0003, 0.047, and 0.050, respectively. As discussed before, such an ARCH model fails to show the asymmetric
responses of stock volatility to positive and negative prior shocks. The STAR model
provides a simple alternative that may overcome this difﬁculty. Applying STAR
models to the monthly returns of 3M stock, we obtain the model
Rt = 0.015 + at,
at = σtϵt,
σ 2
t = (0.003 + 0.205a2
t−1 + 0.092a2
t−2) +
0.001 −0.239a2
t−1
1 + exp(−1000at−1),
(4.17)
where the standard error of the constant term in the mean equation is 0.002 and the
standard errors of the estimates in the volatility equation are 0.0002, 0.074, 0.043,
0.0004, and 0.080, respectively. The scale parameter 1000 of the logistic transition
function is ﬁxed a priori to simplify the estimation. This STAR model provides
some support for asymmetric responses to positive and negative prior shocks. For
--- page 213 ---

186
nonlinear models and their applications
a large negative at−1, the volatility model approaches the ARCH(2) model
σ 2
t = 0.003 + 0.205a2
t−1 + 0.092a2
t−2.
Yet for a large positive at−1, the volatility process behaves like the ARCH(2) model
σ 2
t = 0.004 −0.034a2
t−1 + 0.092a2
t−2.
The negative coefﬁcient of a2
t−1 in the prior model is counterintuitive, but the
magnitude is small. As a matter of fact, for a large positive shock at−1, the ARCH
effects appear to be weak even though the parameter estimates remain statistically
signiﬁcant. The results shown are obtained using the command optim in R. A
RATS program for estimating the STAR model is given in Appendix A.
R Program for Estimating the STAR Model Used
> da=read.table("m-3m4608.txt",header=T)
> rtn=da[,2]
> source("star.R")
> par=c(.001,.002,.256,.141,.002,-.314)
> m2=optim(par,star,method=c("BFGS"),hessian=T)
# function to calculate the likelihood of a STAR model.
star <- function(par){
f = 0
T1=length(rtn)
h=c(1,1)
at=c(0,0)
for (t in 3:T1){
resi = rtn[t]-par[1]
at=c(at,resi)
sig=par[2]+par[3]*at[t-1]^2+par[4]*at[t-2]^2
sig1=par[5]+par[6]*at[t-1]^2
tt=sqrt(sig+sig1/(1+exp(-1000*at[t-1])))
h=c(h,tt)
x=resi/tt
f=f+log(tt)+0.5*x*x
}
f
}
4.1.4
Markov Switching Model
The idea of using probability switching in nonlinear time series analysis is discussed
in Tong (1983). Using a similar idea, but emphasizing aperiodic transition between
various states of an economy, Hamilton (1989) considers the Markov switching
--- page 214 ---

nonlinear models
187
autoregressive (MSA) model. Here the transition is driven by a hidden two-state
Markov chain. A time series xt follows an MSA model if it satisﬁes
xt =

c1 + p
i=1 φ1,ixt−i + a1t
if st = 1,
c2 + p
i=1 φ2,ixt−i + a2t
if st = 2,
(4.18)
where st assumes values in {1,2} and is a ﬁrst-order Markov chain with transition
probabilities
P (st = 2|st−1 = 1) = w1,
P (st = 1|st−1 = 2) = w2.
The innovational series {a1t} and {a2t} are sequences of iid random variables with
mean zero and ﬁnite variance and are independent of each other. A small wi
means that the model tends to stay longer in state i. In fact, 1/wi is the expected
duration of the process to stay in state i. From the deﬁnition, an MSA model uses a
hidden Markov chain to govern the transition from one conditional mean function
to another. This is different from that of a SETAR model for which the transition is
determined by a particular lagged variable. Consequently, a SETAR model uses a
deterministic scheme to govern the model transition, whereas an MSA model uses a
stochastic scheme. In practice, the stochastic nature of the states implies that one is
never certain about which state xt belongs to in an MSA model. When the sample
size is large, one can use some ﬁltering techniques to draw inference on the state of
xt. Yet as long as xt−d is observed, the regime of xt is known in a SETAR model.
This difference has important practical implications in forecasting. For instance,
forecasts of an MSA model are always a linear combination of forecasts produced
by submodels of individual states. But those of a SETAR model only come from
a single regime provided that xt−d is observed. Forecasts of a SETAR model also
become a linear combination of those produced by models of individual regimes
when the forecast horizon exceeds the delay d. It is much harder to estimate
an MSA model than other models because the states are not directly observable.
Hamilton (1990) uses the EM algorithm, which is a statistical method iterating
between taking expectation and maximization. McCulloch and Tsay (1994) consider
a Markov chain Monte Carlo (MCMC) method to estimate a general MSA model.
We discuss MCMC methods in Chapter 12.
McCulloch and Tsay (1993) generalize the MSA model in Eq. (4.18) by letting the transition probabilities w1 and w2 be logistic, or probit, functions of some
explanatory variables available at time t −1. Chen, McCulloch, and Tsay (1997)
use the idea of Markov switching as a tool to perform model comparison and selection between nonnested nonlinear time series models (e.g., comparing bilinear and
SETAR models). Each competing model is represented by a state. This approach
to select a model is a generalization of the odds ratio commonly used in Bayesian
analysis. Finally, the MSA model can easily be generalized to the case of more
than two states. The computational intensity involved increases rapidly, however.
For more discussions of Markov switching models in econometrics, see Hamilton
(1994, Chapter 22).
--- page 215 ---

188
nonlinear models and their applications
Example 4.5.
Consider the growth rate, in percentages, of the U.S. quarterly
real gross national product (GNP) from the second quarter of 1947 to the ﬁrst
quarter of 1991. The data are seasonally adjusted and shown in Figure 4.4, where
a horizontal line of zero growth is also given. It is reassuring to see that a majority
of the growth rates are positive. This series has been widely used in nonlinear
analysis of economic time series. Tiao and Tsay (1994) and Potter (1995) use TAR
models, whereas Hamilton (1989) and McCulloch and Tsay (1994) employ Markov
switching models.
Employing the MSA model in Eq. (4.18) with p = 4 and using a Markov chain
Monte Carlo method, which is discussed in Chapter 12, McCulloch and Tsay (1994)
obtain the estimates shown in Table 4.1. The results have several interesting ﬁndings. First, the mean growth rate of the marginal model for state 1 is 0.909/(1 −
0.265 −0.029 + 0.126 + 0.11) = 0.965 and that of state 2 is −0.42/(1 −0.216 −
0.628 + 0.073 + 0.097) = −1.288. Thus, state 1 corresponds to quarters with positive growth, or expansion periods, whereas state 2 consists of quarters with negative
growth, or a contraction period. Second, the relatively large posterior standard deviations of the parameters in state 2 reﬂect that there are few observations in that state.
This is expected as Figure 4.4 shows few quarters with negative growth. Third,
the transition probabilities appear to be different for different states. The estimates
indicate that it is more likely for the U.S. GNP to get out of a contraction period
than to jump into one −0.286 versus 0.118. Fourth, treating 1/wi as the expected
duration for the process to stay in state i, we see that the expected durations for
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
•
•
•••
•
•
••
•
••
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
••
•
•
•
••
•
••
•
•
•
•
•
•
Year
Growth
1950
1960
1970
1980
1990
−2
−1
0
1
2
3
4
Figure 4.4
Time plot of growth rate of U.S. quarterly real GNP from 1947.II to 1991.I. Data are
seasonally adjusted and in percentages.
--- page 216 ---

nonlinear models
189
TABLE 4.1
Estimation Results of Markov Switching Model with p = 4 for Growth
Rate of U.S. Quarterly Real GNP, Seasonally Adjusteda
Parameter
ci
φ1
φ2
φ3
φ4
σi
wi
State 1
Estimate
0.909
0.265
0.029
−0.126
−0.110
0.816
0.118
Standard Error
0.202
0.113
0.126
0.103
0.109
0.125
0.053
State 2
Estimate
−0.420
0.216
0.628
−0.073
−0.097
1.017
0.286
Standard Error
0.324
0.347
0.377
0.364
0.404
0.293
0.064
aThe estimates and their standard errors are posterior means and standard errors of a Gibbs sampling
with 5000 iterations.
a contraction period and an expansion period are approximately 3.69 and 11.31
quarters. Thus, on average, a contraction in the U.S. economy lasts about a year,
whereas an expansion can last for 3 years. Finally, the estimated AR coefﬁcients
of xt−2 differ substantially between the two states, indicating that the dynamics of
the U.S. economy are different between expansion and contraction periods.
4.1.5
Nonparametric Methods
In some ﬁnancial applications, we may not have sufﬁcient knowledge to prespecify
the nonlinear structure between two variables Y and X. In other applications, we
may wish to take advantage of the advances in computing facilities and computational methods to explore the functional relationship between Y and X. These
considerations lead to the use of nonparametric methods and techniques. Nonparametric methods, however, are not without cost. They are highly data dependent
and can easily result in overﬁtting. Our goal here is to introduce some nonparametric methods for ﬁnancial applications and some nonlinear models that make use
of nonparametric methods and techniques. The nonparametric methods discussed
include kernel regression, local least-squares estimation, and neural network.
The essence of nonparametric methods is smoothing. Consider two ﬁnancial
variables Y and X, which are related by
Yt = m(Xt) + at,
(4.19)
where m(·) is an arbitrary, smooth, but unknown function and {at} is a white
noise sequence. We wish to estimate the nonlinear function m(·) from the data. For
simplicity, consider the problem of estimating m(·) at a particular date for which
X = x. That is, we are interested in estimating m(x). Suppose that at X = x we
have repeated independent observations y1, . . . , yT . Then the data become
yt = m(x) + at,
t = 1, . . . , T.
Taking the average of the data, we have
T
t=1 yt
T
= m(x) +
T
t=1 at
T
.
--- page 217 ---

190
nonlinear models and their applications
By the law of large numbers, the average of the shocks converges to zero as T
increases. Therefore, the average ¯y = (T
t=1 yt)/T is a consistent estimate of m(x).
That the average ¯y provides a consistent estimate of m(x) or, alternatively, that the
average of shocks converges to zero shows the power of smoothing.
In ﬁnancial time series, we do not have repeated observations available at X = x.
What we observed are {(yt, xt)} for t = 1, . . . , T . But if the function m(·) is
sufﬁciently smooth, then the value of Yt for which Xt ≈x continues to provide
accurate approximation of m(x). The value of Yt for which Xt is far away from
x provides less accurate approximation for m(x). As a compromise, one can use a
weighted average of yt instead of the simple average to estimate m(x). The weight
should be larger for those Yt with Xt close to x and smaller for those Yt with
Xt far away from x. Mathematically, the estimate of m(x) for a given x can be
written as
ˆm(x) = 1
T
T

t=1
wt(x)yt,
(4.20)
where the weights wt(x) are larger for those yt with xt close to x and smaller for
those yt with xt far away from x. In Eq. (4.20), we assume that the weights sum
to T . One can treat 1/T as part of the weights and make the weights sum to one.
From Eq. (4.20), the estimate ˆm(x) is simply a local weighted average with
weights determined by two factors. The ﬁrst factor is the distance measure (i.e.,
the distance between xt and x). The second factor is the assignment of weight for
a given distance. Different ways to determine the distance between xt and x and to
assign the weight using the distance give rise to different nonparametric methods.
In what follows, we discuss the commonly used kernel regression and local linear
regression methods.
Kernel Regression
Kernel regression is perhaps the most commonly used nonparametric method in
smoothing. The weights here are determined by a kernel, which is typically a
probability density function, is denoted by K(x), and satisﬁes
K(x) ≥0,

K(z) dz = 1.
However, to increase the ﬂexibility in distance measure, one often rescales the
kernel using a variable h > 0, which is referred to as the bandwidth. The rescaled
kernel becomes
Kh(x) = 1
hK(x/h),

Kh(z) dz = 1.
(4.21)
The weight function can now be deﬁned as
wt(x) =
Kh(x −xt)
T
t=1 Kh(x −xt)
,
(4.22)
--- page 218 ---

nonlinear models
191
X
Kernel
−3
−2
−1
0
1
2
3
0.0
0.2
0.4
0.6
0.8
Figure 4.5
Standard normal kernel (solid line) and Epanechnikov kernel (dashed line) with bandwidth
h = 1.
where the denominator is a normalization constant that makes the smoother adaptive to the local intensity of the X variable and ensures the weights sum to one.
Plugging Eq. (4.22) into the smoothing formula (4.20), we have the well-known
Nadaraya–Watson kernel estimator
ˆm(x) =
T

t=1
wt(x)yt =
T
t=1 Kh(x −xt)yt
T
t=1 Kh(x −xt)
;
(4.23)
see Nadaraya (1964) and Watson (1964). In practice, many choices are available
for the kernel K(x). However, theoretical and practical considerations lead to a
few choices, including the Gaussian kernel
Kh(x) =
1
h
√
2π
exp

−x2
2h2

and the Epanechnikov kernel (Epanechnikov, 1969)
Kh(x) = 0.75
h

1 −x2
h2

I
***x
h
*** ≤1

,
where I (A) is an indicator such that I (A) = 1 if A holds and I (A) = 0 otherwise.
Figure 4.5 shows the Gaussian and Epanechnikov kernels for h = 1.
--- page 219 ---

192
nonlinear models and their applications
To understand the role played by the bandwidth h, we evaluate the
Nadaraya–Watson estimator with the Epanechnikov kernel at the observed values
{xt} and consider two extremes. First, if h →0, then
ˆm(xt) →Kh(0)yt
Kh(0)
= yt,
indicating that small bandwidths reproduce the data. Second, if h →∞, then
ˆm(xt) →
T
t=1 Kh(0)yt
T
t=1 Kh(0)
= 1
T
T

t=1
yt = ¯y,
suggesting that large bandwidths lead to an oversmoothed curve—the sample mean.
In general, the bandwidth function h acts as follows. If h is very small, then the
weights focus on a few observations that are in the neighborhood around each xt.
If h is very large, then the weights will spread over a larger neighborhood of xt.
Consequently, the choice of h plays an important role in kernel regression. This is
the well-known problem of bandwidth selection in kernel regression.
Bandwidth Selection
There are several approaches for bandwidth selection; see H¨ardle (1990) and Fan
and Yao (2003). The ﬁrst approach is the plug-in method, which is based on
the asymptotic expansion of the mean integrated squared error (MISE) for kernel
smoothers
MISE = E
 ∞
−∞
[ ˆm(x) −m(x)]2 dx,
where m(·) is the true function. The quantity E[ ˆm(x) −m(x)]2 of the MISE is a
pointwise measure of the mean squared error (MSE) of ˆm(x) evaluated at x. Under
some regularity conditions, one can derive the optimal bandwidth that minimizes
the MISE. The optimal bandwidth typically depends on several unknown quantities
that must be estimated from the data with some preliminary smoothing. Several
iterations are often needed to obtain a reasonable estimate of the optimal bandwidth.
In practice, the choice of preliminary smoothing can become a problem. Fan and
Yao (2003) give a normal reference bandwidth selector as
ˆhopt =

1.06sT −1/5
for the Gaussian kernel,
2.34sT −1/5
for the Epanechnikov kernel,
where s is the sample standard error of the independent variable, which is assumed
to be stationary.
--- page 220 ---

nonlinear models
193
The second approach to bandwidth selection is the leave-one-out cross validation. First, one observation (xj, yj) is left out. The remaining T −1 data points
are used to obtain the following smoother at xj:
ˆmh,j(xj) =
1
T −1

t̸=j
wt(xj)yt,
which is an estimate of yj, where the weights wt(xj) sum to T −1. Second,
perform step 1 for j = 1, . . . , T and deﬁne the function
CV(h) = 1
T
T

j=1
[yj −ˆmh,j(xj)]2W(xj),
where W(·) is a nonnegative weight function satisfying n
j=1 W(xj) = T , that
can be used to down-weight the boundary points if necessary. Decreasing the
weights assigned to data points close to the boundary is needed because those
points often have fewer neighboring observations. The function CV(h) is called
the cross-validation function because it validates the ability of the smoother to
predict {yt}T
t=1. One chooses the bandwidth h that minimizes the CV(·) function.
Local Linear Regression Method
Assume that the second derivative of m(·) in model (4.19) exists and is continuous
at x, where x is a given point in the support of m(·). Denote the data available by
{(yt, xt)}T
t=1. The local linear regression method to nonparametric regression is to
ﬁnd a and b that minimize
L(a, b) =
T

t=1
[yt −a −b(x −xt)]2Kh(x −xt),
(4.24)
where Kh(·) is a kernel function deﬁned in Eq. (4.21) and h is a bandwidth. Denote
the resulting value of a by ˆa. The estimate of m(x) is then deﬁned as ˆa. In practice,
x assumes an observed value of the independent variable. The estimate ˆb can be
used as an estimate of the ﬁrst derivative of m(·) evaluated at x.
Under the least-squares theory, Eq. (4.24) is a weighted least-squares problem
and one can derive a closed-form solution for a. Speciﬁcally, taking the partial
derivatives of L(a, b) with respect to both a and b and equating the derivatives to
zero, we have a system of two equations with two unknowns:
T

t=1
Kh(x −xt)yt = a
T

t=1
Kh(x −xt) + b
T

t=1
(x −xt)Kh(x −xt),
T

t=1
yt(x −xt)Kh(x −xt) = a
T

t=1
(x −xt)Kh(x −xt) + b
T

t=1
(x −xt)2Kh(x −xt).
--- page 221 ---

194
nonlinear models and their applications
Deﬁne
sT,ℓ=
T

t=1
Kh(x −xt)(x −xt)ℓ,
ℓ= 0, 1, 2.
The prior system of equations becomes

 sT,0
sT,1
sT,1
sT,2

 a
b

=

T
t=1 Kh(x −xt)yt
T
t=1(x −xt)Kh(x −xt)yt

.
Consequently, we have
ˆa = sT,2
T
t=1 Kh(x −xt)yt −sT,1
T
t=1(x −xt)Kh(x −xt)yt
sT,0sT,2 −s2
T,1
.
The numerator and denominator of the prior fraction can be further simpliﬁed as
sT,2
T

t=1
Kh(x −xt)yt −sT,1
T

t=1
(x −xt)Kh(x −xt)yt
=
T

t=1
{Kh(x −xt)[sT,2 −(x −xt)sT,1]}yt.
sT,0sT,2 −s2
T,1 =
T

t=1
Kh(x −xt)sT,2 −
T

t=1
(x −xt)Kh(x −xt)sT,1
=
T

t=1
Kh(x −xt)[sT,2 −(x −xt)sT,1].
In summary, we have
ˆa =
T
t=1 wtyt
T
t=1 wt
,
(4.25)
where wt is deﬁned as
wt = Kh(x −xt)[sT,2 −(x −xt)sT,1].
In practice, to avoid possible zero in the denominator, we use the following ˆm(x)
to estimate m(x):
ˆm(x) =
T
t=1 wtyt
T
t=1 wt + 1/T 2 .
(4.26)
--- page 222 ---

nonlinear models
195
Notice that a nice feature of Eq. (4.26) is that the weight wt satisﬁes
T

t=1
(x −xt)wt = 0.
Also, if one assumes that m(·) of Eq. (4.19) has the ﬁrst derivative and ﬁnds the
minimizer of
T

t=1
(yt −a)2Kh(x −xt),
then the resulting estimator is the Nadaraya–Watson estimator mentioned earlier.
In general, if one assumes that m(x) has a bounded kth derivative, then one can
replace the linear polynomial in Eq. (4.24) by a (k −1)-order polynomial. We refer
to the estimator in Eq. (4.26) as the local linear regression smoother. Fan (1993)
shows that, under some regularity conditions, the local linear regression estimator
has some important sampling properties. The selection of bandwidth can be carried
out via the same methods as before.
Time Series Application
In time series analysis, the explanatory variables are often the lagged values of
the series. Consider the simple case of a single explanatory variable. Here model
(4.19) becomes
xt = m(xt−1) + at,
and the kernel regression and local linear regression method discussed before are
directly applicable. When multiple explanatory variables exist, some modiﬁcations
are needed to implement the nonparametric methods. For the kernel regression, one
can use a multivariate kernel such as a multivariate normal density function with
a prespeciﬁed covariance matrix:
Kh(x) =
1
(h
√
2π)p||1/2 exp

−1
2h2 x′−1x

,
where p is the number of explanatory variables and  is a prespeciﬁed positivedeﬁnite matrix. Alternatively, one can use the product of univariate kernel functions
as a multivariate kernel—for example,
Kh(x) =
p

i=1
0.75
hi

1 −x2
i
h2
i

I
****
xi
hi
**** < 1

.
This latter approach is simple, but it overlooks the relationship between the explanatory variables.
--- page 223 ---

196
nonlinear models and their applications
Example 4.6.
To illustrate the application of nonparametric methods in ﬁnance,
consider the weekly 3-month Treasury bill secondary market rate from 1970 to 1997
for 1461 observations. The data are obtained from the Federal Reserve Bank of St.
Louis and are shown in Figure 4.6. This series has been used in the literature as
an example of estimating stochastic diffusion equations using discretely observed
data. See references in Chapter 6. Here we consider a simple model
yt = µ(xt−1) dt + σ(xt−1) dwt,
where xt is the 3-month Treasury bill rate, yt = xt −xt−1, wt is a standard Brownian motion, and µ(·) and σ(·) are smooth functions of xt−1, and apply the local
smoothing function lowess of R or S-Plus to obtain nonparametric estimates of
µ(·) and σ(·); see Cleveland (1979). For simplicity, we use |yt| as a proxy of the
volatility of xt.
For the simple model considered, µ(xt−1) is the conditional mean of yt given
xt−1, that is, µ(xt−1) = E(yt|xt−1). Figure 4.7(a) shows the scatterplot of y(t)
versus xt−1. The plot also contains the local smooth estimate of µ(xt−1) obtained
by lowess of R or S-Plus. The estimate is essentially zero. However, to better
understand the estimate, Figure 4.7(b) shows the estimate ˆµ(xt−1) on a ﬁner scale.
It is interesting to see that ˆµ(xt−1) is positive when xt−1 is small but becomes
negative when xt−1 is large. This is in agreement with the common sense that
Year
Rate
1970
1975
1980
1985
1990
1995
4
6
8
10
12
14
16
Figure 4.6
Time plot of U.S. weekly 3-month Treasury bill rate in secondary market from 1970 to
1997.
--- page 224 ---

nonlinear models
197
x(t−1)
y(t)
0.04 0.06 0.08 0.10 0.12 0.14 0.16
−0.01 0.0 0.01 0.02
(a)
x(t−1)
m
0.04 0.06 0.08 0.10 0.12 0.14 0.16
−0.002
0.0 0.001
(b)
x(t−1)
abs(y)
0.04 0.06 0.08 0.10 0.12 0.14 0.16
0.0 0.005
0.015
(c)
x(t−1)
s
0.04 0.06 0.08 0.10 0.12 0.14 0.16
0.0
0.004
0.008
(d)
••••
•••
••••
•
•••••••
••••••••••••••••
•••••••••••••••••••••••••••••••
••
••
•
•••••••
•
•••••••••••••••••••••
•••••••••
••••••••••••••••••••••••••••••••••••••••••••
•••••••••••
•
•
•••••
••••
•
•
•
•••
•
•
•
••••••••••
•
•
••••••••
•
•
•
•
•
••••
••
••
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
• •
•
•
••
••••
••••
•
•••
•
•••••••
•
•
•••
••••
••
•••••••••••••••••••••••••••••
••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••
••••••••••
•
•••••••••••••••••••••••
•••••••••••
•
•
•
• •
••
•
•••••••••••••
••
•••••••
••
••••••••••
••
•
•
•
•
•
•
••
•
• •
•••
•
••••
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
• •
•••
•
••
• •
•
•••
•
••
• • •
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
•
•
••
•
•
•
•
•
•
••••
•
••
•
•
••
•
•
•
•••
••••••
•
•
•
•
•
•••
•
•
•••
••••
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
•
••
•
••
•
•
••••••
•••••••••••••••••••••
••••••••••••••
•
••••••••••••••••••••
••••••••••••••••••••••••••••••
••
••••••
•••••
••••••
••••••••••••••
•••••••••••
••••••••••••••••••••••••
•••••••••••••••••••••••••••••••••••••••••••••••
•
••••••••••••
•••••••••••
•
•
•••••
•
••••••••••••••••
•••••••••••••••••••••••••••••••••••••••••••••••••••••••
••••••••
••••
••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••
••••
•••
••••
•
•••
••
••
••••••••••••••••
•
••••
•••
•••••
••
••
•
•••••
•••••••
•
••
••
•
••
•••••
•
•••••••••••
•••••••
••
•
••••
••••
•
•••••••••••••••••
•••
••••••••••••
••
•••••
•••
•••
•••••
••
••••
•
••••
•
•••••
•
•
••
••
•
•
•
•••••
•••
•
•
•
••
•••••
•
•
•
•
•
••••••
•
•••
•
•
•
••
•
•
•
•
• •
•
•••
•
•
••
••
•
•
•
•
••
•
•••••••
•••
•
•••
••
•
••••••••••••••••••••••••••••
••••••••••••••••••••••••••••••••••••••••••••••
•••••••••••••
•••
••••••••••••
•
••••••••••••••••••••••••
•
•
•••••
•••••
•
•
•
• •
••
•
••••••••••••••••
••••
•
•••••••••
•
••••
•
•
• •
••
•
•
• •
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
•
• •
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
• •
•••
•
••
•
•
••••
•
••
•
• •
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
••
•
••
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
•
••
•
•
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
•••
•
•••
••
•
•
•
•
•
•••
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
••••••••••••
•
••
•
•
•
•
••••
•••••
•
•••
•
•••••
•••••••••••••••••••••••••••••••••
•
•••••••••••••••••••••••
•••••
•
•
•
•••••
•
•••••
••
••••••
•••••••••
•••••••••••••••••••••••••••••
••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••
•••••••••
•
•
•
•
•••
••
•••••••••••••••
••••••••••••••••
•••••••••••••••
••••••••••••••••
•
•••••••••
•
••••
••
•
••
••••••••••••••••••••••••••••••••••••••••••••••••••••••••••
•
••••
•
••••••••••••••••••••••••••••••••••••••
••••••••••••
•••••••
•••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••
•
••••••
••••••••••••••••••••••••••••••••••••
••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••
Figure 4.7
Estimation of conditional mean and volatility of weekly 3-month Treasury bill rate via a
local smoothing method: (a) yt vs. xt−1, where yt = xt −xt−1 and xt is interest rate; (b) estimate of
µ(xt−1); (c) |yt| vs. xt−1; and (d) estimate of σ(xt−1).
when the interest rate is high, it is expected to come down, and when the rate is
low, it is expected to increase. Figure 4.7(c) shows the scatterplot of |y(t)| versus
xt−1 and the estimate of ˆσ(xt−1) via lowess. The plot conﬁrms that the higher the
interest rate, the larger the volatility. Figure 4.7(d) shows the estimate ˆσ(xt−1) on
a ﬁner scale. Clearly, the volatility is an increasing function of xt−1 and the slope
seems to accelerate when xt−1 is approaching 10%. This example demonstrates
that simple nonparametric methods can be helpful in understanding the dynamic
structure of a ﬁnancial time series.
R and S-Plus Commands Used in Example 4.6
> z1=read.table(’w-3mtbs7097.txt’,header=T)
> x=z1[4,1:1460]/100
> y=(z1[4,2:1461]-z1[4,1:1460])/100
> par(mfcol=c(2,2))
> plot(x,y,pch=’*’,xlab=’x(t-1)’,ylab=’y(t)’)
> lines(lowess(x,y))
> title(main=’(a) y(t) vs x(t-1)’)
> fit=lowess(x,y)
--- page 225 ---

198
nonlinear models and their applications
> plot(fit$x,fit$y,xlab=’x(t-1)’,ylab=’mu’,type=’l’,
+ ylim=c(-.002,.002))
> title(main=’(b) Estimate of mu(.)’)
> plot(x,abs(y),pch=’*’,xlab=’x(t-1)’,ylab=’abs(y)’)
> lines(lowess(x,abs(y)))
> title(main=’(c) abs(y) vs x(t-1)’)
> fit2=lowess(x,abs(y))
> plot(fit2$x,fit2$y,type=’l’,xlab=’x(t-1)’,ylab=’sigma’,
+ ylim=c(0,.01))
> title(main=’(d) Estimate of sigma(.)’)
The following nonlinear models are derived with the help of nonparametric
methods.
4.1.6
Functional Coefﬁcient AR Model
Recent advances in nonparametric techniques enable researchers to relax parametric
constraints in proposing nonlinear models. In some cases, nonparametric methods
are used in a preliminary study to help select a parametric nonlinear model. This is
the approach taken by Chen and Tsay (1993a) in proposing the functional coefﬁcient
autoregressive (FAR) model that can be written as
xt = f1(Xt−1)xt−1 + · · · + fp(Xt−1)xt−p + at,
(4.27)
where Xt−1 = (xt−1, . . . , xt−k)′ is a vector of lagged values of xt. If necessary,
Xt−1 may also include other explanatory variables available at time t −1. The
functions fi(·) of Eq. (4.27) are assumed to be continuous, even twice differentiable, almost surely with respect to their arguments. Most of the nonlinear models
discussed before are special cases of the FAR model. In application, one can use
nonparametric methods such as kernel regression or local linear regression to estimate the functional coefﬁcients fi(·), especially when the dimension of Xt−1 is low
(e.g., Xt−1 is a scalar). Recently, Cai, Fan, and Yao (2000) applied the local linear
regression method to estimate fi(·) and showed that substantial improvements in
1-step-ahead forecasts can be achieved by using FAR models.
4.1.7
Nonlinear Additive AR Model
A major difﬁculty in applying nonparametric methods to nonlinear time series analysis is the “curse of dimensionality.” Consider a general nonlinear AR(p) process
xt = f (xt−1, . . . , xt−p) + at. A direct application of nonparametric methods to estimate f (·) would require p-dimensional smoothing, which is hard to do when p is
large, especially if the number of data points is not large. A simple, yet effective
way to overcome this difﬁculty is to entertain an additive model that only requires
lower dimensional smoothing. A time series xt follows a nonlinear additive AR
--- page 226 ---

nonlinear models
199
(NAAR) model if
xt = f0(t) +
p

i=1
fi(xt−i) + at,
(4.28)
where the fi(·) are continuous functions almost surely. Because each function fi(·)
has a single argument, it can be estimated nonparametrically using one-dimensional
smoothing techniques and hence avoids the curse of dimensionality. In application,
an iterative estimation method that estimates fi(·) nonparametrically conditioned
on estimates of fj(·) for all j̸ = i is used to estimate a NAAR model; see Chen
and Tsay (1993b) for further details and examples of NAAR models.
The additivity assumption is rather restrictive and needs to be examined carefully
in application. Chen, Liu, and Tsay (1995) consider test statistics for checking the
additivity assumption.
4.1.8
Nonlinear State-Space Model
Making using of recent advances in MCMC methods (Gelfand and Smith, 1990),
Carlin, Polson, and Stoffer (1992) propose a Monte Carlo approach for nonlinear
state-space modeling. The model considered is
St = ft(St−1) + ut,
xt = gt(St) + vt,
(4.29)
where St is the state vector, ft(·) and gt(·) are known functions depending on some
unknown parameters, {ut} is a sequence of iid multivariate random vectors with
zero mean and nonnegative deﬁnite covariance matrix u, {vt} is a sequence of
iid random variables with mean zero and variance σ 2
v , and {ut} is independent of
{vt}. Monte Carlo techniques are employed to handle the nonlinear evolution of the
state transition equation because the whole conditional distribution function of St
given St−1 is needed for a nonlinear system. Other numerical smoothing methods
for nonlinear time series analysis have been considered by Kitagawa (1998) and the
references therein. MCMC methods (or computing-intensive numerical methods)
are powerful tools for nonlinear time series analysis. Their potential has not been
fully explored. However, the assumption of knowing ft(·) and gt(·) in model (4.29)
may hinder practical use of the proposed method. A possible solution to overcome
this limitation is to use nonparametric methods such as the analyses considered in
FAR and NAAR models to specify ft(·) and gt(·) before using nonlinear state-space
models.
4.1.9
Neural Networks
A popular topic in modern data analysis is neural networks, which can be classiﬁed
as a semiparametric method. The literature on neural networks is enormous, and
its application spreads over many scientiﬁc areas with varying degrees of success;
--- page 227 ---

200
nonlinear models and their applications
I
N
P
U
T
O
U
T
P
U
T
HiddenLayer
Figure 4.8
Feed-forward neural network with one hidden layer for univariate time series analysis.
see Section 2 of Ripley (1993) for a list of applications and Section 10 for remarks
concerning its application in ﬁnance. Cheng and Titterington (1994) provide information on neural networks from a statistical viewpoint. In this subsection, we focus
solely on the feed-forward neural networks in which inputs are connected to one
or more neurons, or nodes,
in the input layer, and these nodes are connected
forward to further layers until they reach the output layer. Figure 4.8 shows an
example of a simple feed-forward network for univariate time series analysis with
one hidden layer. The input layer has two nodes, and the hidden layer has three.
The input nodes are connected forward to each and every node in the hidden layer,
and these hidden nodes are connected to the single node in the output layer. We call
the network a 2–3–1 feed-forward network. More complicated neural networks,
including those with feedback connections, have been proposed in the literature,
but the feed-forward networks are most relevant to our study.
Feed-Forward Neural Networks
A neural network processes information from one layer to the next by an “activation
function.” Consider a feed-forward network with one hidden layer. The jth node
in the hidden layer is deﬁned as
hj = fj

α0j +

i→j
wijxi

,
(4.30)
where xi is the value of the ith input node, fj(·) is an activation function typically
taken to be the logistic function
fj(z) =
exp(z)
1 + exp(z),
α0j is called the bias, the summation i →j means summing over all input nodes
feeding to j, and wij are the weights. For illustration, the jth node of the hidden
layer of the 2–3–1 feed-forward network in Figure 4.8 is
hj =
exp(α0j + w1jx1 + w2jx2)
1 + exp(α0j + w1jx1 + w2jx2),
j = 1, 2, 3.
(4.31)
--- page 228 ---

nonlinear models
201
For the output layer, the node is deﬁned as
o = fo

α0o +

j→o
wjohj

,
(4.32)
where the activation function fo(·) is either linear or a Heaviside function. If fo(·)
is linear, then
o = α0o +
k

j=1
wjohj,
where k is the number of nodes in the hidden layer. By a Heaviside function,
we mean fo(z) = 1 if z > 0 and fo(z) = 0 otherwise. A neuron with a Heaviside
function is called a threshold neuron, with 1 denoting that the neuron ﬁres its
message. For example, the output of the 2–3–1 network in Figure 4.8 is
o = α0o + w1oh1 + w2oh2 + w3oh3,
if the activation function is linear; it is
o =

1
if α0o + w1oh1 + w2oh2 + w3oh3 > 0,
0
if α0o + w1oh1 + w2oh2 + w3oh3 ≤0,
if fo(·) is a Heaviside function.
Combining the layers, the output of a feed-forward neural network can be written as
o = fo

α0o +

j→o
wjofj

α0j +

i→j
wijxi



.
(4.33)
If one also allows for direct connections from the input layer to the output layer,
then the network becomes
o = fo

α0o +

i→o
αioxi +

j→o
wjofj

α0j +

i→j
wijxi



,
(4.34)
where the ﬁrst summation is summing over the input nodes. When the activation
function of the output layer is linear, the direct connections from the input nodes
to the output node represent a linear function between the inputs and output. Consequently, in this particular case model (4.34) is a generalization of linear models.
--- page 229 ---

202
nonlinear models and their applications
For the 2–3–1 network in Figure 4.8, if the output activation function is linear,
then Eq. (4.33) becomes
o = α0o +
3

j=1
wjohj,
where hj is given in Eq. (4.31). The network thus has 13 parameters. If Eq. (4.34)
is used, then the network becomes
o = α0o +
2

i=1
αioxi +
3

j=1
wjohj,
where again hj is given in Eq. (4.31). The number of parameters of the network
increases to 15.
We refer to the function in Eq. (4.33) or (4.34) as a semiparametric function
because its functional form is known, but the number of nodes and their biases and
weights are unknown. The direct connections from the input layer to the output
layer in Eq. (4.34) mean that the network can skip the hidden layer. We refer to
such a network as a skip-layer feed-forward network.
Feed-forward networks are known as multilayer percetrons in the neural network
literature. They can approximate any continuous function uniformly on compact sets
by increasing the number of nodes in the hidden layer; see Hornik, Stinchcombe,
and White (1989), Hornik (1993), and Chen and Chen (1995). This property of neural networks is the universal approximation property of the multilayer percetrons.
In short, feed-forward neural networks with a hidden layer can be seen as a way
to parameterize a general continuous nonlinear function.
Training and Forecasting
Application of neural networks involves two steps. The ﬁrst step is to train the
network (i.e., to build a network, including determining the number of nodes and
estimating their biases and weights). The second step is inference, especially forecasting. The data are often divided into two nonoverlapping subsamples in the
training stage. The ﬁrst subsample is used to estimate the parameters of a given
feed-forward neural network. The network so built is then used in the second subsample to perform forecasting and compute its forecasting accuracy. By comparing
the forecasting performance, one selects the network that outperforms the others
as the “best” network for making inference. This is the idea of cross validation
widely used in statistical model selection. Other model selection methods are also
available.
In a time series application, let {(rt, xt)|t = 1, . . . , T } be the available data for
network training, where xt denotes the vector of inputs and rt is the series of
interest (e.g., log returns of an asset). For a given network, let ot be the output of
