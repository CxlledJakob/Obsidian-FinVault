# Analysis of Financial Time Series, Third Edition (Wiley -- Ruey S_ Tsay -- Wiley series in probability and statistics, 3rd ed_, -- John Wiley & Sons, -- isbn13 9780470414354 -- 9f99b80c7b2dedd477f463dc5323f3b6 -- An.pdf — pages 343–362

--- page 343 ---

316
continuous-time models and their applications
x
Density
−0.10
−0.05
0.0
0.05
0.10
0
5 10 15 20 25 30
x
Density
−0.010 −0.005
0.0
0.005
0.010
22 24 26 28 30
x
Density
−0.10
−0.08
−0.06
−0.04
0
2
3
4
1
x
Density
0.04 0.05 0.06 0.07
(c)
(a)
(d)
(b)
0.08 0.09 0.10
0.0
0.2
0.4
Figure 6.9
Density comparisons between normal distribution and distribution of Eq. (6.31). Dotted
line denotes the normal distribution. Both distributions have mean zero and variance 2.0572×10−4.
(a) Overall comparison, (b) comparison of peaks, (c) left tails, and (d) right tails.
the risk premiums; see Kou (2002) for more details. The unique solution of the
prior equation is given by
Pt = P0 exp


r −σ 2
2 −λψ

t + σwt
 nt

i=1
Ji.
To price a European option in the jump diffusion model, it remains to compute the
expectation, under the measure P ∗, of the discounted ﬁnal payoff of the option. In
particular, the price of a European call option at time t is given by
ct = E∗[e−r(T −t)(PT −K)+]
= E∗

e−r(T −t)

Pt exp
r −σ 2
2
−λψ

(T −t)
+ σ
√
T −tϵ
! nT

i=1
Ji −K
+
+

,
(6.32)
where T is the expiration time, (T −t) is the time to expiration measured in
years, K is the strike price, (y)+ = max(0, y), and ϵ is a standard normal random
--- page 344 ---

jump diffusion models
317
variable. Kou (2002) shows that ct is analytically tractable as
ct =
∞

n=1
n

j=1
e−λ(T −t) λn(T −t)n
n!
2j
22n−1
 2n −j −1
n −1

(A1,n,j + A2,n,j + A3,n,j)
+ e−λ(T −t) 0
Pte−λψ(T −t)(h+) −Ke−r(T −t)(h−)
1
,
(6.33)
where (·) is the CDF of the standard normal random variable,
A1,n,j = Pte−λψ(T −t)+nκ 1
2

1
(1 −η)j +
1
(1 + η)j

(b+) −e−r(T −t)K(b−),
A2,n,j = 1
2e−r(T −t)−ω/η+σ 2(T −t)/(2η2)K
×
j−1

i=0

1
(1 −η)j−i −1
 
σ√T −t
η
i
1
√
2π
Hhi(c−),
A3,n,j = 1
2e−r(T −t)+ω/η+σ 2(T −t)/(2η2)K
×
j−1

i=0

1 −
1
(1 + η)j−i
 
σ
√
T −t
η
i
1
√
2π
Hhi(c+),
b± = ln(Pt/K) + (r ± σ 2/2 −λψ)(T −t) + nκ
σ
√
T −t
,
h± = ln(Pt/K) + (r ± σ 2/2 −λψ)(T −t)
σ
√
T −t
,
c± = σ√T −t
η
±
ω
σ√T −t
,
ω = ln
 K
Pt

+ λψ(T −t) −

r −σ 2
2

(T −t) −nκ,
ψ =
eκ
1 −η2 −1,
and the Hhi(·) functions are deﬁned as
Hhn(x) = 1
n!
 ∞
x
(s −x)ne−s2/2 ds,
n = 0, 1, . . . ,
(6.34)
and Hh−1(x) = exp(−x2/2), which is
√
2πf (x) with f (x) being the probability
density function of a standard normal random variable; see Abramowitz and Stegun
--- page 345 ---

318
continuous-time models and their applications
(1972). The Hhn(x) functions satisfy the recursion
nHhn(x) = Hhn−2(x) −xHhn−1(x),
n ≥1,
(6.35)
with starting values Hh−1(x) = e−x2/2 and Hh0(x) =
√
2π(−x).
The pricing formula involves an inﬁnite series, but its numerical value can be
approximated quickly and accurately through truncation (e.g., the ﬁrst 10 terms).
Also, if λ = 0 (i.e., there are no jumps), then it is easily seen that ct reduces to the
Black–Scholes formula for a call option discussed before.
Finally, the price of a European put option under the jump diffusion model
considered can be obtained by using the putf -call parity; that is,
pt = ct + Ke−r(T −t) −Pt.
Pricing formulas for other options under the jump diffusion model in Eq. (6.26)
can be found in Kou (2002).
Example 6.8.
Consider the stock of Example 6.6, which has a current price
of $80. As before, assume that the strike price of a European option is K = $81
and other parameters are r = 0.08 and T −t = 0.25. In addition, assume that the
price of the stock follows the jump diffusion model in Eq. (6.26) with parameters
λ = 10, κ = −0.02, and η = 0.02. In other words, there are about 10 jumps per
year with average jump size −2% and jump size standard error of 2%. Using the
formula in Eq. (6.33), we obtain ct = $3.92, which is higher than the $3.49 of
Example 6.6 when there are no jumps. The corresponding put option assumes the
value pt = $3.31, which is also higher than what we had before. As expected,
adding the jumps while keeping the other parameters ﬁxed increases the prices of
both European options. Keep in mind, however, that adding the jump process to
the stock price in a real application often leads to different estimates for the stock
volatility σ.
6.10
ESTIMATION OF CONTINUOUS-TIME MODELS
Next, we consider the problem of estimating directly the diffusion equation (i.e.,
Ito process) from discretely sampled data. Here the drift and volatility functions
µ(xt, t) and σ(xt, t) are time varying and may not follow a speciﬁc parametric form. This is a topic of considerable interest in recent years. Details of the
available methods are beyond the scope of this chapter. Hence, we only outline
the approaches proposed in the literature. Interested readers can consult the corresponding references and Lo (1988).
There are several approaches available for estimating a diffusion equation. The
ﬁrst approach is the quasi-maximum-likelihood approach, which makes use of the
fact that for a small time interval dwt is normally distributed; see Kessler (1997)
and the references therein. The second approach uses methods of moments; see
--- page 346 ---

appendix a: integration of black–scholes formula
319
Conley, Hansen, Luttmer, and Scheinkman (1997) and the references therein. The
third approach uses nonparametric methods; see Ait-Sahalia (1996, 2002). The
fourth approach uses semiparametric and reprojection methods; see Gallant and
Long (1997) and Gallant and Tauchen (1997). Recently, many researchers have
applied Markov chain Monte Carlo methods to estimate the diffusion equation; see
Eraker (2001) and Elerian, Chib, and Shephard (2001).
APPENDIX A: INTEGRATION OF BLACK–SCHOLES FORMULA
In this appendix, we derive the price of a European call option given in Eq. (6.19).
Let x = ln(PT ). By changing variable and using g(PT ) dPT = f (x) dx, where
f (x) is the probability density function of x, we have
ct = exp[−r(T −t)]
 ∞
K
(PT −K)g(PT ) dPt
= e−r(T −t)
 ∞
ln(K)
(ex −K)f (x) dx
= e−r(T −t)

 ∞
ln(K)
exf (x) dx −K
 ∞
ln(K)
f (x) dx

.
(6.36)
Because x = ln(PT ) ∼N[ln(Pt) + (r −σ 2/2)(T −t), σ 2(T −t)], the integration
of the second term of Eq. (6.36) reduces to
 ∞
ln(K)
f (x) dx = 1 −
 ln(K)
−∞
f (x) dx
= 1 −CDF[ln(K)]
= 1 −(−h−) = (h−),
where CDF[ln(K)] is the cumulative distribution function (CDF) of x = ln(PT )
evaluated at ln(K), (·) is the CDF of the standard normal random variable, and
−h−= ln(K) −ln(Pt) −(r −σ 2/2)(T −t)
σ
√
T −t
= −ln(Pt/K) −(r −σ 2/2)(T −t)
σ
√
T −t
.
The integration of the ﬁrst term of Eq. (6.36) can be written as
 ∞
ln(K)
1
√
2π

σ 2(T −t)
exp

x −[x −ln(Pt) −(r −σ 2/2)(T −t)]2
2σ 2(T −t)
"
dx,
--- page 347 ---

320
continuous-time models and their applications
where the exponent can be simpliﬁed to
x −{x −[ln(Pt) + (r −σ 2/2)(T −t)]}2
2σ 2(T −t)
= −{x −[ln(Pt) + (r + σ 2/2)(T −t)]}2
2σ 2(T −t)
+ ln(Pt) + r(T −t).
Consequently, the ﬁrst integration becomes
 ∞
ln(K)
exf (x) dx = Pter(T −t)
 ∞
ln(K)
1
√
2π

σ 2(T −t)
× exp

−{x −[ln(Pt) + (r + σ 2/2)(T −t)]}2
2σ 2(T −t)

dx,
which involves the CDF of a normal distribution with mean ln(Pt) + (r +
σ 2/2)(T −t) and variance σ 2(T −t). By using the same techniques as those of
the second integration shown before, we have
 ∞
ln(K)
exf (x) dx = Pter(T −t)(h+),
where h+ is given by
h+ = ln(Pt/K) + (r + σ 2/2)(T −t)
σ
√
T −t
.
Putting the two integration results together, we have
ct = e−r(T −t)[Pter(T −t)(h+) −K(h−)] = Pt(h+) −Ke−r(T −t)(h−).
APPENDIX B: APPROXIMATION TO STANDARD NORMAL
PROBABILITY
The CDF (x) of a standard normal random variable can be approximated by
(x) =

1 −f (x)[c1k + c2k2 + c3k3 + c4k4 + c5k5]
if x ≥0,
1 −(−x)
if x < 0,
where f (x) = exp(−x2/2)/
√
2π, k = 1/(1 + 0.2316419x), c1 = 0.319381530,
c2 = −0.356563782,
c3 = 1.781477937,
c4 = −1.821255978,
and
c5 =
1.330274429.
For illustration, using the earlier approximation, we obtain (1.96) = 0.975002,
(0.82) = 0.793892, and (−0.61) = 0.270931. These probabilities are very
close to that obtained from a typical normal probability table.
--- page 348 ---

exercises
321
EXERCISES
6.1. Assume that the log price pt = ln(Pt) follows a stochastic differential
equation
dpt = γ dt + σ dwt,
where wt is a Wiener process. Derive the stochastic equation for the price Pt.
6.2. Considering the forward price F of a nondividend-paying stock, we have
Ft,T = Pter(T −t),
where r is the risk-free interest rate, which is constant, and Pt is the current stock price. Suppose Pt follows the geometric Brownian motion dPt =
µPt dt + σPt dwt. Derive a stochastic diffusion equation for Ft,T .
6.3. Assume that the price of IBM stock follows the Ito process
dPt = µPt dt + σPt dwt,
where µ and σ are constant and wt is a standard Brownian motion. Consider
the daily log returns of IBM stock in 1997. The average return and the sample
standard deviation are 0.00131 and 0.02215, respectively. Use the data to
estimate the parameters µ and σ assuming that there were 252 trading days
in 1997.
6.4. Suppose that the current price of a stock is $120 per share with volatility
σ = 50% per annum. Suppose further that the risk-free interest rate is 7% per
annum and the stock pays no dividend. (a) What is the price of a European
call option contingent on the stock with a strike price of $125 that will expire
in 3 months? (b) What is the price of a European put option on the same stock
with a strike price of $118 that will expire in 3 months? If the volatility σ
is increased to 80% per annum, then what are the prices of the two options?
6.5. Derive the limiting marginal effects of the ﬁve variables K, Pt, T −t, σ,
and r on a European put option contingent on a stock.
6.6. A stock price is currently $60 per share and follows the geometric Brownian
motion dPt = µPt dt + σPt dt. Assume that the expected return µ from the
stock is 20% per annum and its volatility is 40% per annum. What is the
probability distribution for the stock price in 2 years? Obtain the mean and
standard deviation of the distribution and construct a 95% conﬁdence interval
for the stock price.
6.7. A stock price is currently $60 per share and follows the geometric Brownian
motion dPt = µPt dt + σPt dt. Assume that the expected return µ from
the stock is 20% per annum and its volatility is 40% per annum. What is
the probability distribution for the continuously compounded rate of return
of the stock over 2 years? Obtain the mean and standard deviation of the
distribution.
--- page 349 ---

322
continuous-time models and their applications
6.8. Suppose that the current price of stock A is $70 per share and the price
follows the jump diffusion model in Eq. (6.26). Assume that the risk-free
interest rate is 8% per annum, the stock pays no dividend, and its volatility
(σ) is 30% per annum. In addition, the price on average has about 15 jumps
per year with average jump size −2% and jump standard error 3%. What is
the price of a European call option with strike price $75 that will expire in
3 months? What is the price of the corresponding European put option?
6.9. Consider the European call option of a nondividend-paying stock. Suppose
that Pt = $20, K = $18, r = 6% per annum, and T −t = 0.5 year. If the
price of a European call option of the stock is $2.10, what opportunities are
there for an arbitrageur?
6.10. Consider the put option of a nondividend-paying stock. Suppose that Pt =
$44, K = $47, r = 6% per annum, and T −t = 0.5 year. If the European
put option of the stock is selling at $1.00, what opportunities are there for
an arbitrageur?
REFERENCES
Abramowitz, M. and Stegun, I. A. (1972). Handbook of Mathematical Functions, 10th ed.
U.S. National Bureau of Standards, Washington, DC.
Ait-Sahalia, Y. (1996). Testing continuous-time models for the spot interest rate. Review of
Financial Studies 9: 385–426.
Ait-Sahalia, Y. (2002). Maximum likelihood estimation of discretely sampled diffusions: A
closed-form approach. Econometrica 70: 223–262.
Bakshi, G., Cao, C., and Chen, Z. (1997). Empirical performance of alternative option pricing
models. Journal of Finance 52: 2003–2049.
Billingsley, P. (1968). Convergence of Probability Measures. Wiley, New York.
Billingsley, P. (1986). Probability and Measure, 2nd ed. Wiley, New York.
Black, F. and Scholes, M. (1973). The pricing of options and corporate liabilities. Journal
of Political Economy 81: 637–654.
Conley, T. G., Hansen, L. P., Luttmer, E. G. J., and Scheinkman, J. A. (1997). Short-term
interest rates as subordinated diffusions. Review of Financial Studies 10: 525–577.
Cox, J. C. and Rubinstein, M. (1985). Options Markets. Prentice Hall, Englewood Cliffs,
NJ.
Donsker, M. (1951). An invariance principle for certain probability limit theorems. Memoirs
American Mathematical Society No. 6.
Dufﬁe, D. (1995). Dynamic Asset Pricing Theory, 2nd ed. Princeton University Press, Princeton, NJ.
Elerian, O., Chib, S., and Shephard, N. (2001). Likelihood inference for discretely observed
non-linear diffusions. Econometrica 69: 959–993.
Eraker, B. (2001). MCMC analysis of diffusion models with application to ﬁnance. Journal
of Business & Economic Statistics 19: 177–191.
Gallant, A. R. and Long, J. R. (1997). Estimating stochastic diffusion equations efﬁciently
by minimum chi-squared. Biometrika 84: 125–141.
--- page 350 ---

references
323
Gallant, A. R. and Tauchen, G. (1997). The relative efﬁciency of method of moments
estimators. Working paper, Economics Department, University of North Carolina.
Hull, J. C. (2007). Options, Futures, and Other Derivatives with Derivagem CD, 7th ed.
Prentice Hall, Upper Saddle River, NJ.
Kessler, M. (1997). Estimation of an ergodic diffusion from discrete observations. Scandinavian Journal of Statistics 24: 1–19.
Kou, S. (2002). A jump diffusion model for option pricing. Management Science 48:
1086–1101.
Lo, A. W. (1988). Maximum likelihood estimation of generalized Ito’s processes with discretely sampled data. Econometric Theory 4: 231–247.
Merton, R. C. (1976). Option pricing when the underlying stock returns are discontinuous.
Journal of Financial Economics 5: 125–144.
--- page 351 ---
--- page 352 ---

C H A P T E R
7
Extreme Values, Quantiles,
and Value at Risk
Extreme price movements in the ﬁnancial markets are rare but important. The stock
market crash on Wall Street in October 1987 and other big ﬁnancial crises such as
the Long-Term Capital Management and the bankruptcy of Lehman Brothers have
attracted a great deal of attention among investors, practitioners, and researchers.
The recent worldwide ﬁnancial crisis characterized by the substantial increase in
market volatility, for example, the volatility index (VIX) of the Chicago Board
Options Exchange index, and the big drops in market indices has further generated discussions on market risk and margin setting for ﬁnancial institutions. As a
result, value at risk (VaR) has become the standard measure of market risk in risk
management. Its usefulness and weaknesses are widely discussed.
In this chapter, we discuss various methods for calculating VaR and the statistical
theories behind these methods. In particular, we consider the extreme value theory
developed in the statistical literature for studying rare (or extraordinary) events
and its application to VaR. Both unconditional and conditional concepts of extreme
values are discussed. The unconditional approach to VaR calculation for a ﬁnancial
position uses the historical returns of the instruments involved to compute VaR.
On the other hand, a conditional approach uses the historical data and explanatory
variables to calculate VaR. The explanatory variables may include macroeconomic
variables of an economy and accounting variables of companies involved.
Other approaches to VaR calculation discussed in the chapter are RiskMetrics,
econometric modeling using volatility models, and empirical quantile. We use daily
log returns of IBM stock to illustrate the actual calculation of all the methods
discussed. The results obtained can therefore be used to compare the performance
of different methods. Figure 7.1 shows the time plot of daily log returns of IBM
stock from July 3, 1962, to December 31, 1998, for 9190 observations.
VaR is a point estimate of potential ﬁnancial loss. It contains a certain degree
of uncertainty. It also has a tendency to underestimate the actual loss if an extreme
Analysis of Financial Time Series, Third Edition, By Ruey S. Tsay
Copyright 2010 John Wiley & Sons, Inc.
325
--- page 353 ---

326
extreme values, quantiles, and value at risk
Year
Log return
1970
1980
1990
2000
−0.2
−0.1
0.0
0.1
Figure 7.1
Time plot of daily log returns of IBM stock from July 3, 1962, to December 31, 1998.
event actually occurs. To overcome the weaknesses of VaR, we discuss other risk
measures such as expected shortfalls and the loss distribution of a ﬁnancial position
in the chapter.
7.1
VALUE AT RISK
There are several types of risk in ﬁnancial markets. Credit risk, operational risk,
and market risk are the three main categories of ﬁnancial risk. Value at risk (VaR)
is mainly concerned with market risk, but the concept is also applicable to other
types of risk. VaR is a single estimate of the amount by which an institution’s
position in a risk category could decline due to general market movements during
a given holding period; see Dufﬁe and Pan (1997) and Jorion (2006) for a general
exposition of VaR. The measure can be used by ﬁnancial institutions to assess
their risks or by a regulatory committee to set margin requirements. In either case,
VaR is used to ensure that the ﬁnancial institutions can still be in business after
a catastrophic event. From the viewpoint of a ﬁnancial institution, VaR can be
deﬁned as the maximal loss of a ﬁnancial position during a given time period for a
given probability. In this view, one treats VaR as a measure of loss associated with
a rare (or extraordinary) event under normal market conditions. Alternatively, from
the viewpoint of a regulatory committee, VaR can be deﬁned as the minimal loss
under extraordinary market circumstances. Both deﬁnitions will lead to the same
VaR measure, even though the concepts appear to be different.
--- page 354 ---

value at risk
327
In what follows, we deﬁne VaR under a probabilistic framework. Suppose that
at the time index t we are interested in the risk of a ﬁnancial position for the
next ℓperiods. Let
V (ℓ) be the change in value of the underlying assets of the
ﬁnancial position from time t to t + ℓand L(ℓ) be the associated loss function.
These two quantities are measured in dollars and are random variables at the time
index t. L(ℓ) is a positive or negative function of
V (ℓ) depending on the position
being short or long. Denote the cumulative distribution function (CDF) of L(ℓ) by
Fℓ(x). We deﬁne the VaR of a ﬁnancial position over the time horizon ℓwith tail
probability p as
p = Pr[L(ℓ) ≥VaR] = 1 −Pr[L(ℓ) < VaR].
(7.1)
From the deﬁnition, the probability that the position holder would encounter a loss
greater than or equal to VaR over the time horizon ℓis p. Alternatively, VaR
can be interpreted as follows. With probability (1 −p), the potential loss encountered by the holder of the ﬁnancial position over the time horizon ℓis less than
VaR.
The previous deﬁnition shows that VaR is concerned with the upper tail behavior
of the loss CDF Fℓ(x). For any univariate CDF Fℓ(x) and probability q, such that
0 < q < 1, the quantity
xq = inf{x|Fℓ(x) ≥q}
is called the qth quantile of Fℓ(x), where inf denotes the smallest real number
x satisfying Fℓ(x) ≥q. If the random variable L(ℓ) of Fℓ(x) is continuous, then
q = Pr[L(ℓ) ≤xq].
If the CDF Fℓ(x) of Eq. (7.1) is known, then 1 −p = Pr[L(ℓ) < VaR] so that
VaR is simply the (1 −p)th quantile of the CDF of the loss function L(ℓ) (i.e.,
VaR = x1−p). Sometimes, VaR is referred to as the upper pth quantile because
p is the upper tail probability of the loss distribution. The CDF is unknown in
practice, however. Studies of VaR are essentially concerned with estimation of the
CDF and/or its quantile, especially the upper tail behavior of the loss CDF.
In real applications, calculation of VaR involves several factors:
1. The probability of interest p, such as p = 0.01 for risk management and
p = 0.001 in stress testing.
2. The time horizon ℓ. It might be set by a regulatory committee, such as 1 day
or 10 days for market risk and 1 year or 5 years for credit risk.
3. The frequency of the data, which might not be the same as the time horizon
ℓ. Daily observations are often used in market risk analysis.
4. The CDF Fℓ(x) or its quantiles.
5. The amount of the ﬁnancial position or the mark-to-market value of the
portfolio.
--- page 355 ---

328
extreme values, quantiles, and value at risk
Among these factors, the CDF Fℓ(x) is the focus of econometric modeling.
Different methods for estimating the CDF give rise to different approaches to VaR
calculation.
Remark.
The deﬁnition of VaR in Eq. (7.1) is based on the upper tail of
a loss function. For a long ﬁnancial position, loss occurs when the returns are
negative. Therefore, we shall use negative returns in data analysis for a long
ﬁnancial position. Furthermore, the VaR deﬁned in Eq. (7.1) is in dollar amount.
Since log returns correspond approximately to percentage changes in value of
a ﬁnancial asset, we use log returns rt in data analysis. The VaR calculated
from the upper quantile of the distribution of rt+1 given information available
at time t is therefore in percentage. The dollar amount of VaR is then the cash
value of the ﬁnancial position times the VaR of the log return series. That is,
VaR = Value × VaR(of log returns). If necessary, one can also use the approximation VaR = Value × [exp(VaR of log returns) −1].
□
Remark.
VaR is a prediction concerning possible loss of a portfolio in a
given time horizon. It should be computed using the predictive distribution of
future returns of the ﬁnancial position. For example, the VaR for a 1-day horizon of a portfolio using daily returns rt should be calculated using the predictive
distribution of rt+1 given information available at time t. From a statistical viewpoint, predictive distribution takes into account the parameter uncertainty in a
properly speciﬁed model. However, predictive distribution is hard to obtain, and
most of the available methods for VaR calculation ignore the effects of parameter
uncertainty.
□
Remark.
From the prior discussion, VaR is just a quantile of the loss function.
It does not fully describe the upper tail behavior of the loss function. In practice,
two assets may have the same VaR yet encounter different losses when the VaR is
exceeded. Furthermore, the VaR does not satisfy the sub-additivity property, which
states that a risk measure for two portfolios after they have been merged should be
no greater than the sum of their risk measures before they were merged. Therefore,
care must be exercised in using VaR to measure risk. We discuss the concept of
expected shortfall later as an alternative to measuring risk. The expected shortfall
is also known as the conditional value at risk (CVaR).
□
7.2
RISKMETRICS
J. P. Morgan developed the RiskMetrics methodology to VaR calculation; see
Longerstaey and More (1995). In its simple form, RiskMetrics assumes that the
continuously compounded daily return of a portfolio follows a conditional normal
distribution. Denote the daily log return by rt and the information set available at
time t −1 by Ft−1. RiskMetrics assumes that rt|Ft−1 ∼N(µt, σ 2
t ), where µt is the
conditional mean and σ 2
t is the conditional variance of rt. In addition, the method
--- page 356 ---

riskmetrics
329
assumes that the two quantities evolve over time according to the simple model:
µt = 0,
σ 2
t = ασ 2
t−1 + (1 −α)r2
t−1,
1 > α > 0.
(7.2)
Therefore, the method assumes that the logarithm of the daily price, pt = ln(Pt),
of the portfolio satisﬁes the difference equation pt −pt−1 = at, where at = σtϵt
is an IGARCH(1,1) process without drift. The value of α is often in the interval
(0.9, 1) with a typical value of 0.94.
A nice property of such a special random-walk IGARCH model is that the
conditional distribution of a multiperiod return is easily available. Speciﬁcally, for
a k-period horizon, the log return from time t + 1 to time t + k (inclusive) is
rt[k] = rt+1 + · · · + rt+k−1 + rt+k. We use the square bracket [k] to denote a khorizon return. Under the special IGARCH(1,1) model in Eq. (7.2), the conditional
distribution rt[k]|Ft is normal with mean zero and variance σ 2
t [k], where σ 2
t [k]
can be computed using the forecasting method discussed in Chapter 3. Using the
independence assumption of ϵt and model (7.2), we have
σ 2
t [k] = Var(rt[k]|Ft) =
k

i=1
Var(at+i|Ft),
where Var(at+i|Ft) = E(σ 2
t+i|Ft) can be obtained recursively. Using rt−1 = at−1 =
σt−1ϵt−1, we can rewrite the volatility equation of the IGARCH(1,1) model in Eq.
(7.2) as
σ 2
t = σ 2
t−1 + (1 −α)σ 2
t−1(ϵ2
t−1 −1)
for all t.
In particular, we have
σ 2
t+i = σ 2
t+i−1 + (1 −α)σ 2
t+i−1(ϵ2
t+i−1 −1)
for
i = 2, . . . , k.
Since E(ϵ2
t+i−1 −1|Ft) = 0 for i ≥2, the prior equation shows that
E(σ 2
t+i|Ft) = E(σ 2
t+i−1|Ft)
for
i = 2, . . . , k.
(7.3)
For the 1-step-ahead volatility forecast, Eq. (7.2) shows that σ 2
t+1 = ασ 2
t + (1 −
α)r2
t . Therefore, Eq. (7.3) shows that Var(rt+i|Ft) = σ 2
t+1 for i ≥1 and, hence,
σ 2
t [k] = kσ 2
t+1. The results show that rt[k]|Ft ∼N(0, kσ 2
t+1). Consequently, under
the special IGARCH(1,1) model in Eq. (7.2) the conditional variance of rt[k] is
proportional to the time horizon k. The conditional standard deviation of a k-period
horizon log return is then
√
kσt+1, which is
√
k times σt+1.
Given a tail probability, RiskMetrics uses the result rt[k]|Ft ∼N(0, kσ 2
t+1)
to calculate VaR for the log return. If the tail probability is set to 5%, then
VaR = 1.65σt+1 for the next trading day. This is the upper 5% quantile (or the
95th percentile) of a normal distribution with mean zero and standard deviation σt+1. For the next k trading days, VaR[k] = 1.65
√
kσt+1, which is the 95th
--- page 357 ---

330
extreme values, quantiles, and value at risk
percentile of N(0, kσ 2
t+1). Similarly, if the tail probability is 1%, then VaR =
2.326σt+1 for the next trading day and VaR[k] = 2.326
√
kσt+1 for the next k
trading days.
Consider the case of 1% tail probability. The VaR for the portfolio under Risk-
Metrics is then
VaR = Amount of position × 2.326σt+1,
for the next trading day and that of a k-day horizon is
VaR(k) = Amount of position × 2.326
√
kσt+1,
where the argument (k) of VaR is used to denote the time horizon and the portfolio
value is measured in dollars. Consequently, under RiskMetrics, we have
VaR(k) =
√
k × VaR.
This is referred to as the square root of time rule in VaR calculation under Risk-
Metrics.
If the log returns are in percentages, then the 1% VaR for the next trading day
is VaR = Amount of position × 2.326σt+1/100, where σt+1 is the volatility of the
percentage log returns.
Note that because RiskMetrics assumes log returns are normally distributed with
mean zero, the loss function is symmetric and VaR are the same for long and short
ﬁnancial positions.
Example 7.1.
The sample standard deviation of the continuously compounded
daily return of the German mark/U.S. dollar exchange rate was about 0.53%
in June 1997. Suppose that an investor was long in $10 million worth of
mark/dollar exchange rate contract. Then the 5% VaR for a 1-day horizon of the
investor is
$10,000,000 × (1.65 × 0.0053) = $87,450.
The corresponding VaR for 10-day horizon is
$10,000,000 × (
√
10 × 1.65 × 0.0053) ≈$276,541.
Example 7.2.
Consider the daily IBM log returns of Figure 7.1. As mentioned
in Chapter 1, the sample mean of the returns is signiﬁcantly different from zero.
However, for demonstration of VaR calculation using RiskMetrics, we assume in
this example that the conditional mean is zero and the volatility of the returns
follows an IGARCH(1,1) model without drift. The ﬁtted model is
rt = at,
at = σtϵt,
σ 2
t = 0.9396σ 2
t−1 + (1 −0.9396)a2
t−1,
(7.4)
--- page 358 ---

riskmetrics
331
where {ϵt} is a standard Gaussian white noise series. As expected, this model is
rejected by the Q statistics. For instance, we have a highly signiﬁcant statistic
Q(10) = 56.19 for the squared standardized residuals.
From the data and the ﬁtted model, we have r9190 = −0.0128 and ˆσ 2
9190 =
0.0003472. Therefore, the 1-step-ahead volatility forecast is ˆσ 2
9190(1) = 0.000336.
The 95% quantile of the conditional distribution r9191|F9190 is 1.65 ×
√
0.000336 =
0.03025. Consequently, the 1-day horizon 5% VaR of a long position of $10 millions is
VaR = $10,000,000 × 0.03025 = $302,500.
The 99% quantile is 2.326 ×
√
0.000336 = 0.04265, and the corresponding 1%
VaR for the same long position is $426,500.
Remark.
To implement RiskMetrics in S-Plus, one can use ewma1 (exponentially weighted moving average of order 1) under the mgarch (multivariate
GARCH) command to obtain the estimate of 1 −α. Then, use the command predict to obtain volatility forecasts. For the IBM data used, the estimate of α is
1 −0.036 = 0.964 and the 1-step-ahead volatility forecast is ˆσ9190(1) = 0.01888.
Please see the demonstration below. This leads to VaR = $10,000,000 × (1.65 ×
0.01888) = $311,520 and VaR = $439,187 for p = 0.05 and 0.01, respectively.
These two values are slightly higher than those of Example 7.2, which are based
on estimates of the RATS package.
□
S-Plus Demonstration
The following output has been simpliﬁed:
> ibm.risk=mgarch(ibm~-1,
~ewma1)
> ibm.risk
ALPHA 0.036
> predict(ibm.risk,2)
$sigma.pred 0.01888
7.2.1
Discussion
An advantage of RiskMetrics is simplicity. It is easy to understand and apply.
Another advantage is that it makes risk more transparent in the ﬁnancial markets.
However, as security returns tend to have heavy tails (or fat tails), the normality
assumption used often results in underestimation of VaR. Other approaches to VaR
calculation avoid making such an assumption.
The square root of time rule is a consequence of the special model used by
RiskMetrics. If either the zero mean assumption or the special IGARCH(1,1)
model assumption of the log returns fails, then the rule is invalid. Consider the
simple model
rt = µ + at,
at = σtϵt,
µ̸ = 0,
σ 2
t = ασ 2
t−1 + (1 −α)a2
t−1,
--- page 359 ---

332
extreme values, quantiles, and value at risk
where {ϵt} is a standard Gaussian white noise series. The assumption that µ̸ = 0
holds for returns of many heavily traded stocks on the NYSE; see Chapter 1. For
this simple model, the distribution of rt+1 given Ft is N(µ, σ 2
t+1). The 95% quantile
used to calculate the 1-period horizon VaR becomes µ + 1.65σt+1. For a k-period
horizon, the distribution of rt[k] given Ft is N(kµ, kσ 2
t+1), where as before rt[k] =
rt+1 + · · · + rt+k. The 95% quantile used in the k-period horizon VaR calculation
is kµ + 1.65
√
kσt+1 =
√
k(
√
kµ + 1.65σt+1). Consequently, VaR(k)̸ =
√
k × VaR
when the mean return is not zero. It is also easy to show that the rule fails when
the volatility model of the return is not an IGARCH(1,1) model without drift.
7.2.2
Multiple Positions
In some applications, an investor may hold multiple positions and needs to compute the overall VaR of the positions. RiskMetrics adopts a simple approach for
doing such a calculation under the assumption that daily log returns of each
position follow a random-walk IGARCH(1,1) model. The additional quantities
needed are the cross-correlation coefﬁcients between the returns. Consider the
case of two positions. Let VaR1 and VaR2 be the VaR for the two positions
and ρ12 be the cross-correlation coefﬁcient between the two returns—that is,
ρ12 = Cov(r1t, r2t)/[Var(r1t)Var(r2t)]0.5. Then the overall VaR of the investor is
VaR =

VaR2
1 + VaR2
2 + 2ρ12VaR1VaR2.
The generalization of VaR to a position consisting of m instruments is straightforward as
VaR =
-
.
.
/
m

i=1
VaR2
i + 2
m

i<j
ρijVaRiVaRj,
where ρij is the cross-correlation coefﬁcient between returns of the ith and jth
instruments and VaRi is the VaR of the ith instrument.
The prior formula is obtained using the assumption that the joint distribution
of the log returns of assets involved in the portfolio is multivariate normal with
mean zero and covariance matrix t+1. Under such an assumption, the log return
of the portfolio is normal with mean zero and ﬁnite variance; see Appendix B of
Chapter 8 for properties of multivariate normal variables.
7.2.3
Expected Shortfall
Given a tail probability p, VaR is simply the (1 −p)th quantile of the loss function. In practice, the actual loss, if it occurs, can be greater than VaR. In this
sense, VaR may underestimate the actual loss. To have a better assessment of the
potential loss, one can consider the expected value of the loss function if the VaR
is exceeded. This consideration leads to the concept of expected shortfall (ES).
--- page 360 ---

econometric approach to var calculation
333
Under RiskMetrics, the loss function is normally distributed so that the conditional
distribution of the loss function given that a VaR is exceeded is a truncated (from
below) normal distribution. Properties such as mean and variance of a truncated
normal distribution have been well-studied in the statistical literature. We can use
the mean of the distribution to calculate expected shortfall. Speciﬁcally, consider
the standard normal distribution X ∼N(0, 1). For a given upper tail probability p,
let q = 1 −p and VaRq be the associated VaR, that is, VaRq is the qth quantile of
X. Then the expectation of X given X > VaRq is E(X|X > VaRq) = f (VaRq)/p,
where f (x) = (1/
√
2π) exp(−x2/2) is the pdf of X. The expected shortfall for a
log return rt with conditional distribution N(0, σ 2
t ) is then
ESq = f (VaRq)
p
σt
or
ES1−p = f (VaR1−p)
p
σt.
For example, if p = 0.05, then VaR0.95 ≈1.645 and f (VaRq)/p = f (1.645)/0.05
= 2.0627 so that the expected shortfall under RiskMetrics is ES0.95 = 2.0627σt. If
p = 0.01, then ES0.99 = 2.6652σt.
7.3
ECONOMETRIC APPROACH TO VAR CALCULATION
A general approach to VaR calculation is to use the time series econometric models
of Chapters 2–4. For a log return series, the time series models of Chapter 2 can
be used to model the mean equation, and the conditional heteroscedastic models
of Chapter 3 or 4 are used to handle the volatility. For simplicity, we use GARCH
models in our discussion and refer to the approach as an econometric approach to
VaR calculation. Other volatility models, including the nonlinear ones in Chapter 4,
can also be used.
Consider the log return rt of an asset. A general time series model for rt can be
written as
rt = φ0 +
p

i=1
φirt−i + at −
q

j=1
θjat−j,
(7.5)
at = σtϵt,
σ 2
t = α0 +
u

i=1
αia2
t−i +
v

j=1
βjσ 2
t−j.
(7.6)
Equations (7.5) and (7.6) are the mean and volatility equations for rt. These two
equations can be used to obtain 1-step-ahead forecasts of the conditional mean and
conditional variance of rt assuming that the parameters are known. Speciﬁcally,
we have
ˆrt(1) = φ0 +
p

i=1
φirt+1−i −
q

j=1
θjat+1−j,
ˆσ 2
t (1) = α0 +
u

i=1
αia2
t+1−i +
v

j=1
βjσ 2
t+1−j.
--- page 361 ---

334
extreme values, quantiles, and value at risk
If one further assumes that ϵt is Gaussian, then the conditional distribution of
rt+1 given the information available at time t is N[ˆrt(1), ˆσ 2
t (1)]. Quantiles of this
conditional distribution can easily be obtained for VaR calculation. For example, the
95% quantile is ˆrt(1) + 1.65ˆσt(1). If one assumes that ϵt is a standardized Student-t
distribution with v degrees of freedom, then the quantile is ˆrt(1) + t∗
v (1 −p)ˆσt(1),
where t∗
v (1 −p) is the (1 −p)th quantile of a standardized Student-t distribution
with v degrees of freedom.
The relationship between quantiles of a Student-t distribution with v degrees
of freedom, denoted by tv, and those of its standardized distribution, denoted by
t∗
v , is
p = Pr(tv ≤q) = Pr

tv
√v/(v −2) ≤
q
√v/(v −2)

= Pr

t∗
v ≤
q
√v/(v −2)

,
where v > 2. That is, if q is the pth quantile of a Student-t distribution with
v degrees of freedom, then q/√v/(v −2) is the pth quantile of a standardized
Student-t distribution with v degrees of freedom. Therefore, if ϵt of the GARCH
model in Eq. (7.6) is a standardized Student-t distribution with v degrees of freedom
and the upper tail probability is p, then the (1 −p)th quantile used to calculate
the 1-period horizon VaR at time index t is
ˆrt(1) + tv(1 −p)ˆσt(1)
√v/(v −2) ,
where tv(1 −p) is the (1 −p)th quantile of a Student-t distribution with v degrees
of freedom.
Example 7.3.
Consider again the daily IBM log returns of Example 7.2. We
use two volatility models to calculate VaR of 1-day horizon at t = 9190 for a long
position of $10 million. These econometric models are reasonable based on the
modeling techniques of Chapters 2 and 3.
Because the position is long, we use rt = −rc
t , where rc
t is the usual log return
of IBM stock shown in Figure 7.1.
CASE 1.
Assume that ϵt is standard normal. The ﬁtted model is
rt = −0.00066 −0.0247rt−2 + at,
at = σtϵt,
σ 2
t = 0.00000389 + 0.0799a2
t−1 + 0.9073σ 2
t−1.
From the data, we have r9189 = 0.00201, r9190 = 0.0128, and σ 2
9190 = 0.00033455.
Consequently, the prior AR(2)–GARCH(1,1) model produces 1-step-ahead forecasts as
ˆr9190(1) = −0.00071
and
ˆσ 2
9190(1) = 0.0003211.
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
