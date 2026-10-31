# The Kelly capital growth investment criterion _ theory and -- Leonard C_ Maclean, Edward O_ Thorp, W_ T_ Ziemba, Leonard -- World Scientific Handbook -- isbn13 9781283148344 -- bec576e26410d0c695fd5b867d08ec4f -- An.pdf — pages 286–305

--- page 286 ---

259
QU(llItilatilie Fillance, Vol. 5, No. 4, August 2005, 343- 355
11 Routledge
~
TayIor& Fraoci' Groop
19
Time to wealth goals in capital accumulation
LEONARD c. MACLEAN*t , WILLIAM T. ZIEMBAt§ and YUMING LI ~
tSchool of Business Administration, Dalhousie University, Halifax, NS, Canada B3H IZ5
t Sauder School of Business, University of British Columbia, Vancouver, BC, Canada V6T IZ2
§Department of Finance, Sloan School of Management, 50 Memorial Drive E52-410,
Massachusetts Institute of Technology, Cambridge, MA 02142-1 347, USA
I. Introduction
-,rSchool of Business, California State University, Fullerton, CA 92834, USA
(Received 26 January 2004; infina/form /5 Apri/ 2005)
This paper considers the problem of investment of capital in risky assets in a dynamic capital
market in continuolls time. The model controls risk, and in particular the risk associated with
errors in the estimation of asset returns. The framework for investment risk is a geometric
Brownian motion model for asset prices. with random rates of return. The information
filtration process and the capital allocation decisions are considered separately. The fi ltration
is based on a Bayesian model for asset prices, and an (empirical) Bayes estimator for current
price dynamics is developed from the price history. Given the conditional price dynamics,
investors allocate wealth to achieve their fi nancial goals efficiently over time. The price updating and wealth reallocations occur when control limits on the wealth process are attained.
A Bayesian fractional Kelly strategy is optimal at each rebalancing, assuming that the risky
assets are jointly lognormal distributed. The strategy minimizes the expected time to the upper
wealth limit while maintaining a high probability of reaching that goal before falling to a
lower wealth limit. The fractional Kelly strategy is a blend of the log-optimal portfolio and
cash and is eq uivalently represented by a negative power utility function, under the multiva riate lognormal distribution assumption. By rebalancing when control limits are reached,
the wealth goals approach provides greater control over downside risk and upside growth. The
wealth goals approach with random rebalancing times is compared to the expected utility
approach with fixed rebalancing ti mes in an asset allocation problem involving stocks, bonds,
and cash.
Keywords: Capital accumulation; Wealth goals; Investment of capital
In capital accumulation under uncertainty, a decisionmaker must determine how much capital to invest in
riskless and risky investment opportunities at each point
in time. The investment strategy yields a stream of capital
over time, with investment decisions made so that
the distribution of wealth has desirable properties.
An investment strategy which has generated considerable
interest is the growth optimal or Kelly strategy, where the
expected logarithm of wealth is maximized (Kelly 1956).
The wealth distribution of this strategy has many attractive characteristics (see e.g. Hakansson 1970, 1971,
Markowitz 1976, Hakansson and Ziemba 1995). As
Breiman (1 960, 1961 ), and Algoet and Cover (1 988)
have shown, the Kelly strategy maximizes the long run
expected rate of growth of capital and minimizes the
expected time to reach a fixed level of wealth for sufficiently large goals under mild conditions. Researchers
such as Thorp (1975), Hausch et al. (1981), Grauer and
Hakansson (1986, 1987), and Mulvey and Vladimirow
(1992) have used the optimal growth strategy to compute
optimal portfolio weights in multi-asset and worldwide
asset allocation problems.
The literature considers the stream of capital foll owing
from an investment policy from either a wealth or a time
perspective. In most situations the expected utility of
accumulated capital at a fixed point in time is analysed.
There is particular interest in the logarithm of accumulated capital, and the corresponding rate of capital
growth. Alternatively, the growth rate can be viewed as
the time it takes for accumulated capital to reach wealth
milestones.
*Correspondi ng author. Email: Imac1ean@mgmt.dal.ca
The distribution of accumulated capital to a fixed
point in time and the distribution of the first passage
Qual/fi/afire Fillallce
ISSN 1469- 7688 print/ISSN 1469- 7696 online © 2005 Taylor & Francis
http://www.tandf.co.uk/journals
DO lo 10.1080/1 4697680500149552
--- page 287 ---

260
L. C. MacLean, W T. Ziemba and Y Li
344
L. C. MacLean et al.
time to a fixed level of accumulated capital are variables
controlled by the investment decisions. The Kelly strategy
maximizes the expected logarithm of accumulated capital
or the expected growth rate. However, the strategy is very
aggressive. As Hausch and Ziemba (1985) and Clark and
Ziemba (1 987) have demonstrated, the optimal portfolio
weights in the risky assets given by this strategy tend to be
so large for favourable investments that the chances of
losing a substantial portion of wealth are very high, particularly if the probability estimates are in error. In the
time domain, the chances are high that the first passage to
subsistence wealth occurs before achieving the established
wealth goals.
When the investor is more risk averse, then this can be
reflected in the utility function choice. If the utility
function has an Arrow-Pratt risk aversion parameter,
e.g. the constant relative risk aversion (CRRA) utility,
then the value of this parameter captures risk tolerance;
see Kallberg and Ziemba (1 983).
Another approach is to define a measure of risk which
depends on the investment decision. A standard measure
of risk is volatility as defined by the variance of wealth at
a point in time or the variance of the passage time to a
wealth target. Mean-variance analysis of wealth has been
widely used to determine investment strategies; see
Markowitz (1952, 1987). In the time domain the meanvariance approach yields different strategies. However,
the logarithm of wealth and the first passage time have
consistent mean-variance
properties;
see
Burkhardt
(1998).
An alternative to variance is to use a downside risk
measure (Breitmeyer et al. 1999). MacLean et al. (1992)
considered, as risk measures, quantiles for wealth, logwealth and first passage time in identifying investment
strategies which achieve capital growth with a required
level of security. Security is defined as controlling downside risk. Growth is traded for security with fractional
Kelly strategies. In discrete time models with general
return distributions this strategy is generally suboptimal,
but it has attractive wealth/time distribution properties.
See MacLean and Ziemba (1999) for extensions of this
research. The emphasis in that trade-off work is the properties of the wealth process for a given fraction. For
example, the probability of reaching upper wealth U
before lower wealth L is calculated for various strategies.
In this paper, the reverse problem of findin g a strategy
which achieves a specified probability (risk) is studied.
The most common downside risk measure is Value at
Risk (VaR) (Jorion 1997). Va R has been studied extensively (Artzner et al. 1999, Gaivoronski and Pflug 2005).
Basak and Shapiro (2001 ) consider VaR in a model with
C RRA utility. Although VaR is an industry standard it
has weaknesses in controlling risk. The most serious
shortcoming is the insensitivity to very large losses
which have small probabilitythe essence of risk.
Measures based on lower partial moments (incomplete
means) such as Cva R (Rockafeller and Uryasev 2000)
and convex risk measures based on target violations
(Carino and Ziemba 1998, Rockafeller and Ziemba
2000) attempt to deal with this problem.
Similar to mean-variance, a variety of mean-risk
problems have been studied. Bi-criteria problems such
as maximizing expected logarithm of wealth subject to a
VaR constraint are consistent with stochastic dominance,
the traditional concept for ordering wealth distributions.
(Ogryczak and Ruszczynski 2002).
There is, however, another issue complicating the
measurement of risk and return, which is the estimation
of parameters defining the returns distribution. The value
of the risk/return measures in practice are estimates of
the true values, and the error of the estimates of measures
is very sensitive to errors in the estimation of the returns
distribution. Furthermore, the sensitivity to estimation
errors of expected value measures (mean, CVaR) is
much greater than quantile measures (median, VaR).
In this paper parameter estimation and risk control
are considered in a model where the filtration and control
processes are separate. A dynamic stochastic model for
asset prices is presented in section 2. The model is a generalization to the multi-asset case of the random coefficients model of Browne and Whitt (1996). The inclusion
of many assets facilitates the estimation of model coefficients since the correlation between assets is related to the
intrinsic model structure. The existence of latent factors
generating price movements is implied by the equations
for price dynamics. Alternatively, price parameters could
be related to observable state variables, as is the case in
the model of Xia (200 I). (See also Brennan 1998)
Given the estimated price dynamics, an investment
decision is made to control the path of future wealth.
In section 3, an approach to control is developed based
upon wealth levels as stopping rules. In practice, an
investment portfolio cannot be continuously rebalanced
and a realistic approach is to reconsider the investment
decision at regular discrete time intervals (Rogers 2000).
At each rebalance time, with additional data and a change
in wealth, price parameters are re-estimated and a new
investment strategy
is developed. The process is
illustrated in figure I. The most significant aspect of the
rebalancing is the accuracy of the estimated returns
distribution. If forecasts are accurate, then wealth will
accumulate as expected. If prices are not as forecast
over the next hold interval then unacceptable wealth
levels may result. To protect against that outcome Ivea/th
limils can be placed on the wealth process. If the wealth
trajectory is within the limits, the wealth process is under
control. However, the asset pricing model and the investment decisions are reconsidered when a control limit is
reached. So rebalancing occurs at a random time rather
than at a given point in time. Intervention occurs when
the wealth trajectory is not proceeding as expected and it
can be concluded that the investment decision does not fit
the true securities price process.
Whether rebalancing occurs at fixed or random times,
at the rebalancing the investor:
1. generates new estimates for returns distributions;
2. establishes next lVea/lh limits for random time rebalancing, or the next hold time for the fi xed rebalance
interval;
--- page 288 ---

Time to Wealth Goals in Capital Accumulation
261
Time 10 Iveallh goals in capilal accumulation
345
Portfolio
Decision
Parameter
Estimates
D
Figure 1. Dynamic investment process.
3. determines a nell' investment slralegy based on the
updated returns estimates, and control limits or
hold time.
At a rebala nce point, the decision on investment
is based on accumulated wealth at a planning ho rizon.
A number of bi-criteria decision models have been mentioned, but the model considered is maximization of
expected utility at the horizon, with a negative power
utility. It is significant that there exist wealth goals and
an associated bi-criteria decision model which yields an
identical investment strategy. Although demonstrated
for the special case of negative power utility, this result
is general, so that wealth goals reflect a wide range of
preferences.
The wealth goals decision is put in the context of
capital growth with security. So a strategy is determined
which minimizes
the expected
time to
the upper
limit (grolVlh) while maintaining a high probability of
achieving the upper limit before falling to the lower
limit (security). The optimal strategy for the power utility
and growth-security models is shown to be fracl ional
Kelly-a blend of the risk free (cash) strategy and the
optimal growth strategy.
Although the negative power utility and wealth goals
models are linked by the strategy, the approaches to risk
are different. The expected utility model considers risk at
the ho rizon, whereas the wealth goals model considers
risk along the trajectory. In section 4, the wealth goals
and power utility approaches are compared for the fundamental problem of investing in stocks, bonds, and cash
over time. It is shown that there is an advantage from
wealth goals, since rebalancing occurs at times indicated
by the wealth trajecto ry, i.e. the wealth conditio n.
This result is comparable to the superiority of condition
based intervention in repairable systems (Aven a nd
Jensen 1999). Appendix A contains proofs for propositions in the text.
2. Dynamic estimation of asset price distributions
In the dynamic investment process shown in fi gure I,
the returns o n risky assets are re-estimated at the time
of rebalancing a portfolio. The updated returns distributions are inputs to the investment decision models. In this
section a linear pricing model is proposed where the estimation problem is separated from the control problem.
The model is Bayesian, so that the updating of parameter
estimates follows from Bayes theorem, and fits naturally
into the dynamic investment process.
2.1. Price model
Suppose there are 111 risky assets, with P'(I) equal to the
trading price of asset i at time I. i = I, . ,m, and a riskless asset with rate of return I' at time I. The risky asset
prices are assumed to have a joint log-normal distribution.
Letting
Y,(I) = CnP;(t),
i = 0, .. . ,111,
the price
dynamics are defined by the stochastic differential
equations
dYo(I)= rd t,
(I)
dY;(I) = "',(I)dl +8; dU;, i= I, ... ,m,
where d U;,
i = I, ... , 171, are
independent standard
Brownian motions. They represent the variation in price
specific to each security. The other component of price
variation is generated by the instantaneous mean rate of
return ",,{I), i = I, ... , m. Assume that ",;(1) is a random
variable with distribution defined by
",;(t) = /1.; + y;Z ,(I),
i = 1, ... ,171.
(2)
The Z;, i = I, . . . ,117, are correlated Ga ussian variables,
with Pu being the correlation between Z; and Z j- So the
rates of return are correlated, with the covariance between
",;(1) and "'J{I) given by Y;YjPij'
The price process defined by ( I) and (2) is a variation
on the Merton model (1992) with the conditio n that the
rates Clj, i = I , .
, 111, are stochastic and the volatilities OJ,
i = I, .
, 117, are not stochastic. The intention is to emphasize uncertainty in the mean since errors in estimating the
mean have by far the greatest impact on portfolio decisions (Chopra and Ziemba 1993). The asset prices in the
model are correlated, with the correlatio n generated by
the relationship between the random rates of return o n
assets. Presumably those rates of return are related
through some cOl11l11on factors. The factors may be lalem,
as is assumed in this paper, o r they may be observable
state variables as presented by Xia (2001), who considers
the single risky asset case.
If the model for prices is correct then the error in
forecasting prices arises from errors in parameter
estimates. Error from incorrect modeling may be confounded with estimation error, so attention to the correct
model in an applicatio n may be significant. There are
--- page 289 ---

262
L. C. MacLean, W T. Ziemba and Y Li
346
L. C. MacLean et al.
generalizations of (I) and (2) which can be incorporated
into the approach developed in this section. For example,
the rates of return could be defined by stochastic
differential equations: dai(l) = fLi d l + Yi dq" where dqi
are correlated Brownian motions, i = I, ... , m. Then
a,(l) = ai(O) + fLil + Yi0Z,(I), and the rates are dynamic.
The assumption in (2) simplifies the presentation, so that
formulation is followed, but reference to the dynamic
linear model will be made where appropriate. With regard
to the stationary process (2), Ihe model assumplion applies
lmlif Ihe nexl rebalance poinl. That is, the distribution for
the random rates is the same between rebalance points,
but the distribution at the next point may change. The
model in (2) can be considered as an approximation
between rebalance points. When used with control limits,
where rebalancing occurs when the actual prices depart
from model forecasts, this is a useful approach.
From (I) and (2) the relevant distributions for
asset prices follow. Let Y(l) = (YI (I), ... , Y",(l))' , fL =
(fLJ, .. , fL",)', a = (a l, ' . , a",)', 6. = diag(8;' .. , 8~, ) ,
and r = (Yij), where Yij = YiYA;
(Prior)
a ~ N(fL, r),
(3)
(Conditional)
(Y(1)la, 6.) ~ N(al, 16.),
(4)
(Marginal)
Y(I) ~ N(fL(I), E(I)),
(5)
where fL(l) = IfL and E(I) = 12r + 16. = ret) + 6.(1).
The Bayesian pricing model defined by (3}-(5) has an
alternative structural model representation. The prior
covariance has a decomposition r = AA', where A is an
m x I matrix with I=" m. Consider the independent lalel1l
jaclors F ' = (FI , . .. , FI) , F ' ~ N(O, I), and the errors
/ (1) = (£1 (I), ... , "",(1)), e'(I) ~ N (O, 6.(1)). Let A (I) = I A.
Then the log prices at time I are
Y(I) = fLU) + A(I)F + set).
(6)
From (6), Y(I) ~ N(fL(!), E(/)), where E(I) = A(1)A'(I)+
6.(1). The relationship between prices is driven by underlying common factors which are unobserved. This
manifests itself in rates of return, a = fL + AF, which
are random.
The factor model in (6) has been the subject of numerous asset pricing studies, with the factors representing
traded portfolio's in some cases (Campbell el al. 1997).
Here, the factor model is used to define estimates
for parameters in the inter-temporal pricing model of
(I) and (2).
2.2. Bayes estimation
At the time an investor is rebalancing a portfolio, information is available on past realized securities prices.
Consider the data availa ble at time I, (Y(I), °
=" s =" I},
and the corresponding filtrati on F,v = a( Y(I), °
=" s =" I),
the a -algebra generated by the process Y up to time I.
Conditioned on the data, the distribution for the rate of
return can be determined from Bayes theorem. That is,
a(l) = (a(I)IFt') ex N(&(I), ret)),
(7)
where &(1) = fL(l) + (I - 6.(I)E- I (1))(1'(1) - fL(I)), with
1'(1) = ~ Y(I),
I
and
-
I
I
r(1) = (2 (I - 6.(I)E- (1))6.(1).
The Bayes eSlimale for the rate of return a(l) is the
conditional expectation &(1) = Ea(I). This estimate is the
minimum mean squared error forecast for the rate given
the data. In the context of rebalancing, this is the
planning value for a until the next decision time 1+ f
(when the stopping boundaries are reached or the
fixed rebalance time occurs). Then, since no information
is
added
in
the
hold
interval,
E(a(I)!F,v) =
E(E(a(I)IF,~, )IF,v) , and the best estimate is &(1) throughout the interval.
The Bayes estimate a(l) has an appealing form. It is
inherently dynamic, so that estimates can be updated as
more information on prices is obtained. In particular,
at the next rebalance time 1+ f , the posterior &(1) becomes
the next prior and Bayes theorem is used to update with
the
new
information-Y(I + f).
This
approach
is
described in MacLean el al. (2004). There is another
approach which emphasizes the current dynamics. The
pricing model parameters (fL, r, 6.) are interpreted as
values for the most recent rebalance cycle, and only
data from that time interval is used in estimating the
parameters. With control limits, the recent data contains
information on a change in dynamics, and a change in
prior parameters. The technique for implying the values
for the prior parameters from data is empirical Bayes
estin1ation.
To develop the estimation consider a rebalance interval
(0, I) and prices at the discrele times kIln, k = 0, ... , n,
with corresponding log prices Y(k) := Y[(kl n)I]. The
change in log prices between times kil n and [(k + 1)l n]1
is e(k) = Y(k) -
Y(k -
I), k = I, ... , n. From the model
equations
e(k)=':'a +
fi6. I/2Z,
k=I , ... ,n,
(8)
n
'1-;;
where Z ~ N(O, I).
The increment vectors defined by (8) are independent
and Gaussian for each k . The covariance matrix for each
vector is
12
I
E,,(I) = ,. r + - 6. = r ,,(I) + 6.,,(1),
n-
11
and
I "
1'(1) = - L e(k)
n k= 1
Consider observed log prices on risky securities at the
discrete
time
points:
{Yik, i= 1, ... ,111, k=O, ... , n}.
With eik = Yik -
Yi k- J, the data on increments (firstorder differences
i~ log prices) are {eik> i = I, ... , m,
k = I, ... , n}. Let the covariance matrix for the observed
increments be Su" the estimate of E,,(I).
--- page 290 ---

Time to Wealth Goals in Capital Accumulation
263
Time to \Vealth goals in capital accumulation
347
From the random effects model (8) the theoretical
covariance is factored as l:,,(t) = r,,(t) + "',,(t). [f the
rank (r,,(t» = I < m, then the sample covariance matrix
can be factored to produce estimates of r,,(t) and "',,(t).
In terms of the structural model for prices in (6), the
assumption rank (r,,(t» = I < m is equivalent to the
assumption Ihe number of latent faclors I is strictly less
Ihan the number of risky assets m.
Assuming 1< m, a maximum likelihood factor analysis
of S'" with I factors will yield a loading matrix L", and a
specific error matrix D,,,, where D", is diagonal. Since the
number of factors is known, (L"" D",) is an efficient estimator of (A,,(t), "',,(I», with A,,(I) = (l/n)A (Lawley and
Maxwell 1971). Then G", = L", L;" is an efficient estimator
of r ,,(t).
The prior mean J.i for the rates of return on securities
in a rebalance interval needs to be estimated. If it is
assumed that the rates have a common prior ~l1eal1,
i.e. J.i; = J.i, i = I, ... , m, then the overall mean yet) =
(1 / 1) L:=I Y;(t) is an estimate of J.i, where Y;(t) =
(1 / t)Y;(t). The assumption of a common value is consistent with a long run rate of return on secu rities.
(Alternatively, securities in the same class could have
a common mean, with differences between classes of
securities.)
The discussion has identified estimates for all model
parameters within a rebalance interval. The conditional
distribution for securities prices can be estimated, and in
particular the conditional mean rate of return for the next
time interval can be forecast. Since the forecast is the
Bayes formula with the prior parameters estimated from
data it is an empirical Bayes estimate.
Proposition 1:
Let Yb k = 0, ... , n, be observations on
Ihe veclor of log prices of risky assels 01 regular inlervals
of widlil I/n, IVilh the Slalistics ~omputed from first-order
increments: S"" L"" D", and Y,. Theil
/:,. = (n/t )D,,,,
A = (n/I)L,,, are estimates of Ihe model parameters '"
and A, respeclively.
With
/:,.(1) = I/:", A(I) = tA
and
S; = A(t)A'(t) + /:,.(t), an eslimate for Ihe conditional
mean rate of return at time I is
&,,(1) = yet) + (I -
/:,.(t)S;)(Y(t) -
yet))
(9)
Furthermore, the limit as II --> 00 of &,,(1) is &(1).
The empirical Bayes estimate in (9) is a natural form ulation given the proposed pricing model. If the model is
correct then &,,(1) has smaller mean squared error than
well known estimates for the rate of return, such as the
maximum likelihood estimate and the James-Stein estimate. [f the model is correct but the number of latent
factors is unknown, then there is additional estimation
error from estimating that number. However, results
from similar models indicate such error is small; see
Macl ean and Weldon (1996). If a dynamic model for
rates, a;(1) = a;(O) + J.i;! + Y;0Z;(I), i = I, ... , ! , is the
correct formulation then the approach described above
can be modified to obtain empirical Bayes estimates for
parameters. The modification involves calculating secondorder differences to obtain a random effects model with iid
second-order increments.
With this estimation procedure, an essential component
of the dynamic investment process is in place. The next
component, the planning model, will have the forecasts
from the estimated model as inputs.
3. Portfolio planning models
Assuming that at a rebalance point the data has been
filtered to obtain estimates for the parameters, the
decision on how much capital to allocate to the various
assets is now considered. The objective is to control the
path of accumulated capital generated by the decision and
the unfolding asset prices. The decision will be developed
from (he estimated price parameters whereas capital will
accumulate from the (rue process. Of course, if the estimates used in computing a strategy are substantially in
error, then the trajectory of wealth will not proceed as
anticipated, but the trajectory may still be under control.
At the rebalancing time t, there are estimates for the
conditional rate of return art), and the volatility /:"(1),
based on the methods of section 2. The forecast dynamics
for the price process, conditional on the estimates for
parameters, are
d Y(I) = &(t)dt + /:,.1 /2(I)dZ,
(10)
where the innovations process dZ is standard Brownian
motion.
An investment strategy is a vector process
!(xo(t), X(t», t ~ 01 = ! Xo(I), (X I(t), ... , x",(I» , t ~ 01,
(II)
where L;~o x;(t) = I for any I , with xo(t) the investment
in the risk-free asset. The proportions of wealth invested
in the m risky assets are unconstrained since xo(t) can
always be chosen, with borrowing or lending, to satisfy
the budget constraint.
The forecast change in wealth from an investment decision X(t) is determined by the conditional price process
(10). Suppose the investor at time t has wealth W(I) and
let ¢;(t) = &;(t) + (1 / 2)81(1), i = I , ... ,m. Then the forecast for the instantaneous change in wealth is
d Wet) = [~ X;(t)(¢;(I) - r) + r] W(t)dl
+ Wet) t
x;(t)8;(t)dZ;,
([2)
i=l
where dZ; is standard Brownian motion.
There is a grolvth condilion which will be required of
any feasible investment strategy:
With a fixed mix strategy over the hold interval satisfying the growth condition, the forecast wealth process
W( r), r ~ I,
defin ed
by
(12)
follows
geometric
Brownian motion such that W(r) ~ O.
--- page 291 ---

264
L. C. MacLean, W T Ziemba and Y Li
348
L. C. MacLean et al.
To determine an investment decision which controls
wealth, two approaches are considered. First, a model
which considers preferences for wealth at the planning
horizon is defined. The standard approach is to maximize
expected utility at a planning horizon. Because of uncertainty in the parameters for the asset pricing model,
parameters are re-estimated and decisions revised at
regular intervals in time up to the horizon. In the second
approach, the preferences at the horizon are used to
develop wealth goals (limits). Then a wealth goals
model is defined, which has an equivalent investment
strategy. The contrast from the approaches comes from
rebalancing times. The wealth goals approach involves a
random hold interval, with stopping/rebalancing occurring when specified upper or lower wealth goals are
reached.
The matching of preferences in the two approaches
does not mean that the same fixed mix strategy is used
for both models. The rebalance times are different, and
therefore there are different parameter estimates used in
the strategy calculation.
The link between the planning models is stochastic
dominance. Wealth WI dominates wealth W 2 iff Eu(WI)
is greater than
or equal to
Eu( W 2),
with strict
inequality for at least one utility function u E V. Orders
of stochastic dominance are determined by classes of
utilities. If Vk = {ul( _l)i-IuU) 0:: O,} = I, ... , kl, so that
VI :::) V2 :::) ... , then VI is the class of monotone utilities,
V2 the class of concave monotone utilities, . . . , and
Voocontains the CRRA utilities. Since the CRRA utilities
are a limiting subset, they are a reasonable reference class.
There are alternative formulations of the various orders
of stochastic dominance. In particular, first order is
equivalent to dominance in the cumulative distribution
of wealth. The wealth goals model will be defined on
the distribution of wealth, and therefore is based on
first-order dominance principles. However, it is a relaxation of first-order dominance in that it focuses on parts of
the distribution in a bi-criteria problem.
3.1. Expected utility strategy with fixed rehalallce times
Consider an investor whose objective is to maximize the
expected utility of wealth at the end of a finite planning
horizon T. To obtain an explicit solution we assume a
constant relative risk aversion (CRRA) utility. The utility
of wealth w is
At the current decision time, the parameters in the pricing
model are estimated and an investment strategy is determined, conditional on those estimates. Consider the
conditional CRRA wealth problem.
Definition 1:
The conditional CRRA wealth problem at
rebalance time I, with current wealth w" horizon T and
estimated parameters &(1), 3.(1), is to find the strategy
X(I) E X, which maximizes
£[W~I)~l
where the forecast dynamics of wealth W(t) are given
by (12).
Proposition 2:
The oplimal slralegy lor Ihe condilional
CRRA weallh problem is
X*(I) = _ 1_3. - I (t)(¢(t) - re).
(13)
1-,8
As ,8 --+ 0 in definition I the utility is log and the efficient
strategy is the benchmark optimal growth solution:
X(t) = Do - I (¢(t) - re). The fractionI= 1/ (1 -,8) captures
the aversion to risk (Pratt 1964). When 0 < ,8 < 1, the
positive power utility case, the optimal portfolio invests
more than the benchmark, with the over-investment
financed
through
borrowing
(levered
strategies).
Although the strategy X~ (t) , 0 < ,8 < I, is optimal, it is
problematic from the perspective of the distribution of
terminal wealth W(I). Let Fp be the distribution function
for terminal wealth following strategy X#(I), with Fo the
terminal wealth distribution following the benchmark
strategy. Distributions can be compared with the firstorder stochastic dominance
relation:
Fp, dominates
Fp, iff F~ ,(IV)
::S Fp, (IV) for IV E R with strict inequality
for some IV.
Proposition 3:
The terminal weallh dislribution Folor Ihe
benchmark portfolio first -order stochaslically dominales
Ihe dislribulion Fplor 0 < ,8 < I.
This result provides a rationale for a restriction ,8 ::s 0
to the negative power and log utility functions, and the
resulting class of fractional Kelly strategies pX(t), where
p ::s I. First-order stochastic dominance is defined on the
class of all monotone utilities, of which the CRRA utility
is a small subset. Imposing the first-order dominance condition on the fraction from a CRRA utility model is a
restriction, but other work, where a risk constraint such
as VaR is included in the expected CRRA utility model,
has shown that levered strategies are excluded (Basak and
Shapiro 2001).
The solution in (13) is independent of current wealth IV,
and the planning horizon T.
The decision is sensitive to estimation and modeling error, and at regular intervals of width s model
parameters are re-estimated using the empirical Bayes
methodology.
The actual investment decision at times I, I + s, .
would change with the new estimates.
3.2. Wealth goals stl'ategy ami ralldom I'ehalallce times
The uncertainty in returns on investment, whether from
natural variability, variability in underlying factors, or
errors in estimation, is the motivation for strategies that
control risk. In the conditional CRRA utility problem the
risk associated with the forecast wealth at the horizon is
controlled with the risk aversion parameter ,8, with the
--- page 292 ---

Time to Wealth Goals in Capital Accumulation
265
Time 10 weallh goals in capilal accumulalion
349
estimation risk controlled by regularly updating estimates
for parameters. Updates are appropriate when there is
evidence that current estimates are substantially in
error. This concept of updating based on the gap between
expected and actual processes suggests another way to
control the wealth process. That is, to set control limits
(or wealth goals), as is the practice in process control.
The wealth goals are action levels so that the investment
portfolio is rebalanced if either of the goals is reached.
With wealth w, at time I, the lower and upper wealth goals
.!:!::( and WI are set, where !!:, < W t < \tit. If the investment
strategy X(/) is chosen, then the strategy is followed
until either ~, or IV, is reached. At that point the portfolio
is rebalanced. So new estimates are generated, new goals
are set and a new strategy is chosen. Between rebalancing
points a fixed mix strategy is followed. Information on
prices is obtained between rebalance points, but it is
only used when the accumulated information on actual
prices signals that the forecasts for price movements are
substantially in error, that is, when a control limit is
reached.
The choice of wealth goals is an important component
of the control process. Wealth goals can be an expression
of preferences as naturally as a utility function. Our
approach is to first consider the form of an investment
strategy for given weallh goals, assuming the wealth goals
are feasible, i.e. admit an investment strategy. Then a
methodology for specifying goals based on expected
utility is developed.
The risk and return characteristics of the wealth process have traditionally guided the choice of strategy X(/).
Within the wealth goals context, therefore:
(i) the chance of hitting the lower wealth goal should
be small. That is, the downside risk should be
controlled;
(ii) the upper wealth goal, the preferred target, should be
reached as quickly as possible. That is, the growlh
rale of capital should be maximized.
To formalize downside risk in the wealth goals
approach, consider
T,.,(X(I), w, 1&(1),3.(/» = firsl passage lime to weallh w
starting with lvealth w, at time I andfollolVing investment
slralegy X ( I) , condilioned on Ihe eSlimales[or paramelers
at time t.
Let the set of wealth goals be denoted by
B( = {btlb/ = U:!:p WI), 0 <'!:!::t < WI < WI }'
For b, E B" downside risk for a strategy X(/) E X, is
measured by
mh,(X(/»
= Pr[ T!!C/( X(I), IV,IO:(I), 3.(1») .:': T;;;, ( X(I), W, I&(I), 3.(/»)].
(14)
The risk is the probability the first passage time to ~, is
smaller than the first passage time to IV,.
Risk measures are associated with acceptance sets of
capital accumulation paths (Artzner el 01. 1999). Let
Q(X(I» be the set of all paths of WeT), T ::: I, and let
A(X(I» be the set of acceptable paths. If A' (X(I» is the
complement, then the downside risk for
X(I) is
9l(X(I» = a(A' (X(t)) . That is, the risk for a strategy is
the probability measure of the unacceptable set of paths.
Desirable properties of risk measures have been considered in the literature. The following basic axioms for
a dmvl1side risk measure are proposed in Breitmeyer el 01.
(1999).
A:
(non-negativity)
m(X(/» ::: o.
B:
(normalization)
If AC(X(I)) = <P, then ~l(X(/» = O .
C: (downside focus) If AC(X[ (I» = AC(X2(/» , then
D: (monotonicity)
m(x[ (I) = m(X2(/».
If A' (X[ (I» <; A' (X2(/» , then
Dl(X[(/».:': 9l(X2(t»
Consider the measure in (14). From the growth condition
defining feasible strategies, X(/) E X" any path eventually
reaches IV" and the acceplance sel for the measure is
defined as
Ab,(X(l)) = palhs of WeT), T ::: I,
which reach wt before ever dropping to .!:!::r
Using this definition of acceptance sets, the risk measure
defined in (14) satisfies axioms A- D.
With an appropriate risk measure defined in terms
of wealth goals, risk can be controlled with a constraint
on the measure. For control limits b, E B, and risk
level I - y, 0 .:': y.:': I, feasible strategies X(I) E X, are
required to satisfy mb (X(I» < I -
y .
The other characte;istic of t he wealth goals approach is
the anticipation that the upper limit is reached as quickly
as possible. With the expected time defined as
Gb,(X(I» = EI T;;;,(X(I), 11',1&(1), 3.(t)) \ ,
(15)
the objective is to minimize Gb (X(/». Speed in the time
domain is a growth measur~ . Suppose the random
time to a fixed wealth goal T;;; is mapped onto random
wealth at a fixed time T by W ; = IV, exp(T - T;;;). Then,
E{ln WT } = [In IV, + 7] - E{T;;; }. Minimizing the expected
time to the wealth goal IV, is a~alogous to maximizing the
expected log of wealth to the appropriate horizon T. The
log optimal strategy maximizes the rate of growth of
capital, so (15) is a capital growth criterion. With reference to first-order stochastic dominance, the expected log
of wealth is equivalent to the median wealth, since wealth
is lognormal.
With the risk-return characteristics specified by (14)
and (15), a Growth-Securily decision model can be
defined. Security is the complement of risk, that is,
Sb,CX(/)) = I -
D1b,CX(/» .
Definition 2:
For given control limits h, E B, and risk
level I - y,O .:': y .:': I, and estimates &(/), 3.(1), the conditional Growth- Security strategy X(t) is determined
from the problem
Minimize {Gb'cX(/»ISb,CX(t)) ::: y,X(I) E X, ).
(16)
--- page 293 ---

266
L. C. MacLean, W T. Ziemba and Y. Li
350
L. C. MacLean et al.
Explicit expressions for the optimal solution to (16) will
where
be developed for the geometric Brownian motion model.
Consider the wealth process W(r), r ::: I, with forecast
dynamics given by (12). Let
H ,(X(I)) = [1/I,(X(0) - r] ,
a7(X(t))
m
1/I,(X(l)) = L
X;(l)(¢,(I) - r) + r,
i= 1
m
ai(X(I)) = L
xi(l)81(l), 'P1(X(l)) = 21/1,(X(l)) -
a~(X(I)),
i= !
and
e(X(I)) = 'PI(X(I)) .
I
a?(X(I))
The measures Cb (X(I)) and Sb (X(t)) = I - mb (X(t)) for
geometric Brow~ ian motion ~ re given by Karlin and
Taylor (1981):
( ( )) _ 2In(wl /w,)
(17)
Ch, X; t -
'P,(X(t)) ,
These expressions define growth and security in terms
of the estimated parameters of the returns distribution
and the control limits. Therefore, the growthsecurity
strategy from (16) can be related to those inputs.
Proposition 4:
Suppose 01 rebalance time I, the investor
has wealth w,, parameter estimates aCt), t.(t), and the
return on the risk-free asset is r. If control limits (wealth
goals) are b, E B, and Ihe risk level is I - y, Ihen the condilional grOlvth-securily efficient stralegy at lime t is
X;, (t) = (Xib, (t), ... ,x~'b,(t))' wilh
where e is a vector of ones.
The expression in (19) reveals the approach to risk
control with wealth goals. The component X(t) =
t. - I (r)(¢(I) - re) is the optimal grolVth portfolio (Merton
1992), or the Kelly stralegy (Kelly 1956) or the benchmark
portfolio (Basak and Shapiro 200 I). The function
P,(W" b" y) defines a fraction invested in the risky assets
that depends on current wealth, wealth goals, and risk
level. Hence, the strategy which is growth-security efficient is fractional Kelly, as is the case for CRRA utility.
An expression for the investment fraction follows from
proposition 4.
Corollory 1:
For lVealth goals b, E B" the fraclion of
lVealth invesled in risky assets at the rebalancing lime I is
min{l ,p,J for
-
2
2rh,
[h, . H ,(X(t))] + -_- ,
a?(X(t))
(20)
[log 1V, -
log !.!:,]
h, =
,
[log 1V, -
log!.!:, - logy*]
and
y*
is
the
minimum
positive
root
of
yyl+ 1 - y+(ly) = 0 for
[log w, - log w,]
c, = [log 1V, -
log !.!:,]'
The solutions to the conditional CRRA problem and the
conditional G- S problem apply to one stage in the multistage investment process. Although the form of the solutions is fractional Kelly for both problems, there are
differences. The CR RA solution is independent of current
wealth and the planning horizon. The G-S solution
depends on the current wealth and the horizon through
the wealth goals. Both solutions depend on the estimates
for price parameters.
3.3. Wealth goals
The dynamic investment process of figure I is almost
complete. However, the specification of wealth goals in
the G-S approach has not been addressed. The purpose in
rebalancing is to develop a new investment policy when
the current policy is not working. The method for determining goals in this analysis is based on preferences for
wealth at the planning horizon as defined by the CRRA
utility. A technique of matched strategies, which replicates
the wealth preferences at the horizon, provides a fair
comparison of the accumulated wealth for the contrasting
models. That is, if expected utility is the standard, then
performance of the G- S problem relative to that standard
is studied. It is important to realize that the matching
technique can be implemented with other standard
problems. The wealth goals can be important milestones
without reference to other problems.
Consider choices for f3 and b, = C.i.!:" w,) which produce
the same strategy, that is P,(IV" b" y) = I/ (l - (3) . From
the definition of P,(W" b" y), there are potentially many
combinations of goals which are linked to the same f3.
Since the expected utility fraction invested in the benchmark portfolio is independent of current wealth, whereas
the process control fraction depends on the current wealth
w, and the probability y, the values IV, and y will be fixed,
and the f3 -> b, link explored. Consider, then, the conditional f3-class of goals, with W, = w~ , y = l
(21)
The set ~(f3) ,; B, defines wealth goals with the same
Arrow-Pratt relative risk aversion given the current
wealth I V~ and risk probability l. Proposition 5 establishes that such goals actually exist.
Proposition 5:
At
the
rebalance
time
t
consider
currel1l weallh IV~. risk probabililY yO and risk aversion
--- page 294 ---

Time to Wealth Goals in Capital Accumulation
267
Time 10 Ivealth goals in capital accumulation
351
parameter fJ. Assume that the benchmark portfolio sati4ies
the growlh conciilion, i.e.
o/,(X(t))
I
--- -
> - .
o}(X(t))
2
Then B?(fJ) is non-empty Jar fJ < O.
Consider the following matching heuristic for setting
wealth goals at any rebalancing time T:
I. TV; = E(WEU(r + s)) is the expected wealth at time
r+s with the CRRA strategy
I
-
X"(r) = (I _ fJ) X(r).
2. 1£; = max{l£,lb, E B~(fJ)}.
Setting goals at b; = (l!';, TV;) maintains the investment
fracti on at p, = 1/ (1 - fJ) for any rebalancing time T, and
links the goals to the holding time s.
4. Comparisons
The accumulated capital from the wealth goals with random rebalancing times, and expected utility with fixed
rebalancing times is now analysed for the fundamental
problem of allocating investment capital to stocks,
bonds and cash over time. The matching heuristic
approach is used to insure the problems are comparable,
with the main difference being rebalancing time.
Daily prices for stocks and bonds are simulated
using the dynamic pricing model, discretized to days.
If P;(l) is the price for asset i on day t, where i = 0
(cash), I (stock), and 2 (bonds), then consider the increments e;(l)= lnP;{I + 1) - lnP;(i), i= O, 1,2. From the
model, e;(t) = a; + 8;2;{t), where 2;(t) are independent
Gaussian variables. For cash returns, ao = In(1 + r). It
is assumed that (ai , a2) are Gaussian variables dependent
on a single latent state variable. So a ; = f.L + A;F, i = 1, 2,
with F standard Gaussian. There is a simple structure to
model parameters in this single factor case. If the covariance for risky asset log prices is ~ , The model implies
~ = /1/1' + t., where /I = (A j, A21' and t. = diag(81, 8~ ).
The factor solution is
/I = (..,rfJOI1 , ..,rfJ022)',
t. = diag«1 - Ipl)uij, (\ -
I pl)u~2) '
If the true covariance is known, then model parameters
are specified and daily prices can be simulated.
Conversely, if a sample covariance matrix is determined
from a sequence of prices then the parameter values can
be estimated using these equations. The estimates are
empirical Bayes, based on the methods in section 2.
For the simulation of asset prices, data on yearly asset
returns corresponding to the S&P500, Solomon Brothers
bond index, and U.S. T-bills for 1980- 1990 were used
to generate seed parameters. Statistics on the associated
Mean
Variance
Covariance
Table I. Daily rates of return.
Stocks
Bonds
0.00050
0.00031
0.00062
0.00035
0.00014
Cash
0.00019
o
07 O'----~50:---1~O.,.
0 ---,1"'5:-0 ---::2.;-00:-----=25::0,----:-:300
Figure 2. Daily prices for stocks and bonds.
daily returns are in table I. The corresponding statistics
for log-rates were used as seeds.
Daily prices were generated for one year (260 trading
days) and this was repeated 200 times. The one year
horizon is appropriate for the simulation since it provides
sufficient time for differentiation of capital accumulation from the PC and EU strategies. The contrasting
approaches to selecting an investment strategy were
applied to each trajectory of prices. Initial parameter estimates were taken from average daily returns for the prior
year, 1979. For expected utility, rebalancing (revising
estimates of price model parameters; calculating new
strategy) was done every 30 days. For process control,
rebalancing occurs when control limits are reached. The
estimation is based on the covariance matrix. To increase
stability the covariance analysed at the jth rebalancing
at time I is
As time increases the updating is weighted to the observed
covariance S. The procedure for setting limits (wealth
goals) is described in section 4, where the process control
fraction is maintained at p, = 1/ (\ - fJ).
The expected utility and wealth goals (process control)
methods are shown for the trajectory of prices in figure 2.
This trajectory has a volatile return on stock and is a
useful example.
The expected utility strategies and portfolio values for
the setting I - fJ = 1.1 are given in table 2. The rebalancing occurred at 30 day intervals. The strategy emphasizes
stocks and is quite stable. The return on the portfolio at
the end of the year was 24%.
--- page 295 ---

268
L. C. MacLean, W T. Ziemba and Y Li
352
L. C. M aeLean et al.
Time
I
31
61
91
121
151
181
211
241
Time
I
64
65
66
67
74
88
107
108
115
11 8
120
123
130
Table 2. Expected utility performance.
Stocks
0.4670
0.7439
0.8688
0.8963
0.9701
0.9432
0.9864
1.0125
0.9820
Strategy
Bonds
0. 1465
- 0.1 319
- 0.1 770
- 0.2292
- 04437
- 04726
- 04 900
- 04181
- 0.3989
Port value
I
0.8943
0.9930
1.1 287
1.4089
1.3114
1.2164
1.1 508
1.21 78
Table 3. Wealth goals performance.
Strategy
Wealth limits
Stocks
Bonds
Port value
Upper
Lower
04670
0.1465
I
1.0112
0.5765
0.5805
0.1140
1.0148
1.028 1
0.5309
0.6346
0.1010
1.0379
1.0526
0.52 12
0.6656
0.09 \0
1.0562
1.0717
0.5 196
0.6744
0.0864
1.0787
1.0946
0.530 1
0.6804
0.0898
1.1065
1.1229
0.5427
0.7106
0.067 1
1.1433
1.1 615
0.5385
0.7566
- 0.0011
1.1 644
1.1 844
0.523 1
0.7889
- 0.0509
1.1910
1.21 27
0.5 177
0.7995
- 0.0936
1.2375
1.2603
0.535 1
0.8060
- 0.1302
1.277 1
1.3006
0.55 14
0.8089
- 0.1 571
1.3387
1.3634
0.5779
0.8242
- 0.1957
1.3640
1.3898
0.5798
0.7864
- 0.2 152
1.4043
1.4290
0.6234
The process control methodology was run on the same
trajectory, with settings I - fJ = 1.1 , I - y = 0.03. Those
results are presented in table 3. There is initially more
frequent rebalancing with wealth goals, because of the
volatility. When prices settle down, the fi xed mix strategy
does not change. The return at the end of the year was
42%. It is noteworthy that the return was monotone and
the advantage of the PC strategy increases with time.
The comparison of the expected utility and process
control approaches is the expected wealth ratio at the
end of the year. The wealth ratio for each trajectory is
the accumulated wealth with the process control strategy
divided by the accumulated wealth with the expected
utility strategy.
Table 4 presents mean wealth ratios for values for the
C RRA utility parameter fJ, and the process control risk
probability 1- y. The levered strategies (O< fJ < I)
are included, although those strategies are not growthsecurity efficient.
The wealth goals (process control) approach has a substantial advantage over expected utility, demonstrating
the effect of accounting for current wealth (at the control
limit) in determining a strategy. Since the PC strategy is
determined (matched) from the EU strategy, the expected
wealth advantage of being less risk averse (decreasing
I - fJ) is embedded in the PC strategy, but the PC advantage over E U grows since the volatility is controlled by
Table 4. Expected wealth ratios.
I - y
I - /l
0.0 1
0.02
0.03
0.04
0.05
1.1 5
1.291
1.290
1.289
1.265
1.264
1.10
1.322
1.321
1.320
1.298
1.293
1.05
1.365
1.364
1.359
1.340
1.337
1.00
14 10
1408
1.403
1.384
1.38 1
0.95
1.460
1.459
1.457
1.443
1.433
0.90
1.523
1.522
1.520
1.507
1.491
0.85
1.608
1.608
1.607
1.602
1.584
the upper and lower limits. As the security requirement is
relaxed (y decreasing) the expected wealth advantage for
PC decreases. This results from the specific construction
of the strategy, where the lower control limit drops with
decreased y and given upper control limit.
The cases where (I - fJ) < I , the levered strategies, are
high risk and are stochastically dominated as established
in Proposition 4.
5. Conclusion
This paper considers the risk to accumulated capital in a
multi-asset investment problem where the distribution of
asset prices has random parameters. The basis for investment strategies is either process control, where wealth is
controlled by upper and lower goals, or expected utility of
terminal wealth at the horizon. In the process control
approach, the portfolio is re-balanced when either wealth
goal is reached.
At a re-balancing time the history of asset prices is used
to update the conditional price distribution. An empirical
Bayes estimator of distribution parameters is defined
based on the observed correlation structure of asset
prices. With the revised price distribution, new upper
and lower wealth goals or the next re-balance time are
selected and a new optimal strategy is derived. The process control strategy is growthsecuri ty efficient in the
sense that it has maximum growth among strategies
with a specified level of risk. Assuming a lognormal distribution for asset returns, the growth-security strategy is
a blend of the risk-free portfolio and the optimal growth
portfolio.
The wealth goals approach and the expected utility
approach with constant relative risk aversion are compared. An equivalence between the wealth goals and the
risk aversion parameter is developed. Although the alternative models have the same portfolio solution with the
appropriate choices of parameter values, the wealth goals
approach has the advantage of a direct control of downside risk and a re-balancing of the portfolio based on
significa nt change in the price process and change in
wealth. The benefit of intervening when the condition of
wealth deviates from expectations rather than at regular
intervals in time is clear. Re-balancing at specified
points in time when wealth is proceeding as expected is
analogous to tampering in process control, and typically
introduces extra risk.
--- page 296 ---

Time to Wealth Goals in Capital Accumulation
269
Time to weallh goals in capital accumulation
353
Acknowledgements
This work was presented at the Bachelier World Congress
2002, and seminars at The University of British Columbia
and Dalhousie University. The authors wish to thank
Yonggan Zhao for assistance with the computations.
This research was supported by grants from the Natural
Sciences and Engineering Research Council of Canada
and the National Center of Competence in Research
FlNRISK, Swiss National Foundation.
Then
The first-order conditions
_ d_ E ( W#(Tt)) _ 0
Appendix A
dX;(t)
f3
-
This appendix contains proofs for the propositions in the
reduce to
paper.
Proposition 2:
The optimal Slrategy for the CRRA
wealth problem is given by
X'(t) =_I _ t,- I(t)(¢(t) - re).
( 13)
1 -f3
Proof:
The analysis is similar to theorem 6.2 in Janecek
(1998). For investment
strategy
X(t)
the fo recast
dynamics of wealth are
[ '"
]
dW(I) = 8 x;(t)(¢;(t) - r) + r W(t)d t
'"
+ Wet) L
x;(t)8;(t)dZ ;.
i= ]
With X(r) = X(I) and ¢;(r) = ¢;(t), r :O: I, based on info rmation to time I, integration from t to T gives the forecast
wealth at the horizon
W(Tt)
{[ '"
I"'
]
= w, exp 8 x;(t)(¢;(I) - r) + r -"28 x1(t)iJ(t)
x (T - t) + (T -
1)1/2 ~X;(t)8;(I)Z; } ,
where Z; ~ N(O, I). The expected utility of wealth is
Consider the expression
(¢;(t) - r) - (I - f3)x7(t)8;(1) = 0,
i= I , ... ,1,
and X*(/) is as stated.
D
Proposition 3:
The lerminal weallh dislribution Fo for
Ihe
benchmark
portfolio
.firsl-order
stochastically
dominates the dislribution Fp for 0 < f3 < I.
Proof: Let 1/I(X) and O"(X) be the instantaneous mean
rate of return and standard deviation, respectively,
of the optimal growth (benchmark) portfolio. Let
f = 1/( 1 -
f3) and define
1/I(XP) = 1/I(f) =f(1/I(X) - r) + r),0"2(f) =/0"2(X)
and
Under the assumptions of the model, terminal wealth
W(I + T )
from
the
strategy xP is
log-nol"lnally
distributed with
F ( ) _ N[ln{(IV/IV,) - [<P(f)/211!l
# w -
O"(j)xiT-J'
where N is the G aussian cumulative distribution.
Since 0"2(f) is increasing in fa nd <P(J) is decreasing in f
fo r f > I (optimality of benchmark), the statement in the
proposition follows.
D
Proposition 4:
Suppose at rebalance time I, the investor
has weallh IV" fo recast dynamics of asset prices given the
history {Y" 0 S s s tl, and the return on Ihe risk-Fee assel
is r. If COl1lrol limits (weallh goals) are b, E B, and Ihe risk
level is I - y, Ihell Ihe growlhsecurity efficient strategy at
lime t is Xi,,(t) = (Xib,(/), ... , X;',b,(t))' wilh
Xi,,(t) = prClV" b" y)t, - I (t)(¢(t) - re),
( 19)
where e is a veclor of ones.
Proof:
Let!.!:, = IV,/k and w, = k"wi' where k > I and
c > O. For simplicity the time variable I is deleted. From
(16) and (1 7) the growthsecurity efficiency problem is
{
I
I -
k -O(X)
}
m~x .p(X) I _ I« I+I)8(,\") :0: y, X feasible .
--- page 297 ---

270
L. C. MacLean, W T. Ziemba and Y Li
354
L. C. MacLean et al.
Letting y = k - O(¥) , the constraint requires yy,+1 - y+
(I - y) :0:: O. Consider the minimum positive root y* of
the equation yy,+1 - y + (I - y) = 0, where y' ~ I since
y* = I is a root. Then yy,+1 - Y + (I - y) :0:: 0 for y ~ y'
and the constraint is satisfied if k - 9(¥) ~ y' or
II(X) :0:: -C~~~) = q* :0:: 0,
where q* depends upon ~" w"
and y. But 1I(X) :o:: q'
if 21/t(X) - ( I - q*)(J2(X) :0:: O.
Hence,
the
efficiency
problem is
m~xj21/t(x) - (J2(X)121/t(x)
-(I + q')(J2(X):o:: 0, X feasiblel.
If X* is a solution to this problem then it also solves, for
optimal multiplier A *, the Lagrangian problem
m~x L(X, 1.*),
where
The first-order conditions 'VxL(X*, A' ) = 0 imply that the
optimal X* satisfies the linear system
2(1 + A')(4)i - 1') - 2( 1 + 1.' (1 + q*))[xioT] = 0,
i= 1, ... ,1.
The solution to this system is X* = p,(IV" ~,, WI' y)x
t, - I (4)(t) - re) where
1 +1.'
p ,(IV"~,, WI' y) = I + 1.*(1 + q' )'
D
k -IJ(¥) = y'. Let i = t, - 1(4) - re) and X* = pi. Then the
equation becomes
[( I - IOgY' )(J2(X)]/ - 2[{L(X) - r]p - 21' = O.
logk
The statement in the corollary follows.
D
Proposition 5:
At the rebalance lime I consider curren I
weallh w?, risk probability l and risk aversion parameler fJ. Assume Ihal Ihe benchmark portfolio salisfies the
growlh condition, i.e.
1/t,(i(t))
I
----- >-.
(Jl(X(I))
2
It follOlvs thai lfi(fJ) is non-emply for fJ < 0
Proof:
From corollary l, p,(IV" b" y)= 1/(I-fJ) implies
I _
(J2(X)
" - 2r(l -
fJ)2 + 2H(X)(J2(X)(l - fJ)
K > O.
Since
hllV , WI) =
log IV, - log w,
,
-,
log IV, -
lo g~, - logy'
any (~" WI) E B?(fJ) must satisfy the equation h(~" WI) =
K.
From the assumption
fJ < O and 1/t/(J2> 1/2 it
follows that 0 < K < I. The solution y* of the equation
yyC+I _ y + (I - y) = 0 has the property y' t I as
wt t w( , for fixed ~~ < WI- SO there exists (~~, w7) such
that h(~~ , w;) > K. Also for fixed w;, h~ " 1i0) t 0 as
~l t w,. That is, there is a .!£: with h(]f:, w;) = K.
0
Corollory 1:
For IVealth goals b, E B"
the /raetion of References
Iveallh invesled in risky assets 01 Ihe rebalancing time t is
min{l , PI} for
p,(IV" hI' y) = h, . H,(i(/)) +
-
2
2rh,
[hI . H,(X(t))] + - 2- -
'
(J,(X(I))
where
H,(i(1)) = [1/ttCi(~) -
1'] ,
(Jl(X(t))
h, =
[log IV, -
log ~, ]
,
[log 11', -Iog~, -logy']
(20)
and y* is the minimum positive 1'001 of yy,+1 - y +
(I - y) = o for
Proof:
[Iogw, - log 11',]
c, = [log w, -
log~ ,l'
C l ea rly , p, ~ I, with
1 +1.'
p, = 1 +1.' (1 +q*)
if 1.* = 0, i.e. when the constraint is not binding. If the
security constraint is binding then X* is a solution to
Algoe!, P.H. and Cover, T.M., Asymptotic optimality
and asymptotic equipartiation properties of log-optimum
investment. Allnals of Probabilily, 1988, 16, 876-898.
Artzner, P., Delbaen, F., Eber, J. and Heath, D., Coherent
measures of risk. Mathematical F;nance, 1999,9, 203- 228.
Aven, T. and Jensen, U., Stochastic Models in Reliability, 1999
(Springer: New York).
Basak, S. and Shapiro, A., Value at Risk based risk
management: optimal policies and asset prices. Review oI
Financial SlUdies, 2001 , 14, 371-405.
Breiman, L., Investment policies for expanding business optimal
in a long-run sense. Naval Research Logistics Quarterly, 1960,
7, 647- 651.
Breiman, L., Optimal gambling systems for favorable games, in
Proceedings oI the 4th Berkeley Symposium on Mathematics,
Slalislics alld Probabilily, Vol. I, 1961, pp. 63- 68.
Breitmeyer, c., Hakenes, H., Pfingsten, A. and Rechtien, c.,
Learing from poverty measurement: an axiomatic approach
to measure downside risk. Working Paper, University of
Muenster, Germany, 1999.
Brennan, MJ., The role of learning in dynamic portfolio
decisions. European Finance Review, 1998, I, 295- 306.
Browne, S. and Whitt, W., Portfolio choice and the Bayesian
Kelly criterion. Advances in Applied Probability, 1996, 28,
1145- 1176.
Burkhardt, T., A mean-variance of first passage time approach
to portfolio selection in a lognormal world, in Ihe VIII
International
ConfereJ1ce
on
Stochastic
Programming.
Vancouver, August, 1998.
--- page 298 ---

Time to Wealth Goals in Capital Accumulation
271
Time 10 wealth goals ill capital accumulatioll
355
Campbell, J., La, A. and MacKinlay, C., The Econometrics
of Financial Markel.s,
1997 (Princeton University Press:
Princeton, NJ).
Carino, D.R. and Ziemba, W.T., Formulation of the Russell
Yasuda
Kasai
Financial
Planning
Model.
Operations
Research, 1998, 46, 450-462.
Chopra, V.K. and Ziemba, W.T., The effect of errors in means,
variances, and covariances on optimal portfolio choice.
Journal 0/ Port/olio Management, 1993, 19,6--11.
Clark, R. and Ziemba, W.T., Playing the turn-of-the-yea r effect
with index futures. Operations Research, 1987,35, 799- 8 13.
Gaivoronski, A. and Pflug. G., Value-at-risk in portfolio
optimization:
properties
and
computational
approach.
Journal oj Risk, 2005, 7(2), 1- 31.
Grauer, R.R. and Hakansson, N.H., A half century of returns
on levered and un levered portfolios of stocks, bonds and bills,
with and without small stocks. Journal of Business, 1986,59,
287-3 18.
Grauer, R.R. and Hakansson, N.H., Gains from international
diversification: 1968-85 returns on portfolios of stocks and
bonds . .Ioumal 0/ Finance, 1987, 42,72 1-739.
Hakansson,
N.H .,
Optimal investment and consumption
strategies under risk for a class of utility functions.
Econometrica, 1970, 38, 587- 607.
Hakansson, N.H., Capital growth and the mean-variance
approach to portfolio selection. Journal oj Financial and
Quantitative Analysis, 1971, 6, 517- 557.
Hakansson, N. H. and Ziemba, W.T., Capital growth theory.
In Finance, edited by R.A. Jarrow, V. Maksimovic and
W.T. Ziemba, pp. 65- 86, 1995 (North-Holland: Amsterdam).
Hausch, D.B. and Ziemba, W.T., Transactions costs, extent
of inefficiencies, entries and multiple wagers in a racetrack
betting model. Managemel1l Science, 1985, 31,38 1-392.
Hausch, D.B. Ziemba, W.T. and Rubinstein, M., Efficiency of
the market for racetrack betting. Management Science, 1981,
27, 1435- 1452.
Janecek, K., Maximum growth strategies in gambling and
investment. Unpublished MSc thesis, Charles University,
Prague, 1998.
JOl·ion, P., Vallle-at-Risk: The Benchmark for Controlling
Market Risk, 1997 (Irwin: Chicago).
Kallberg, J.G. and Ziemba, W.T., Comparison of alternative
utility
functions
in
portfolio
selection
problems.
Management Science, 1983,29, 1257-1276.
Karlin, S. and Taylor, H.M., A Second Course in Stochastic
Processes, 1981 (New York: Academic Press).
Kelly, J., A new interpretation of information rate. Bell System
Technology Journal, 1956,35, 917-926.
Lawley, D.N. and Maxwell, A.E., Factor Analysis as a
Statistical Method, 1971 (Butterworths: London).
MacLean, L.e., Sanegre, R., Zhao, Y. and Ziemba, W.T.,
Capital growth with security. Jounlal of Economic Dynamics
and Control, 2004, 28, 937- 954.
MacLean, L.e. and Weldon, K. L., Estimating multivariate
random effects without replication. COI11I11UIl. Statist. Theory
Meth., 1996,24, 1447-1469.
Maclean, L.C. and Ziemba, W.T., Growth versus security
tradeoffs
in
dynamic
investment
analysis.
Anllals oj
Operations Research, 1999, 85, 193- 225.
MacLean, L.e., Ziemba, W.T. and Blazenko, G., Growth
versus security in dynamic investment analysis. Management
Science, 1992, 38, 1562- 1585.
Markowitz, H.M., Portfolio Selection. Journal oj Finance, 1952,
7,77-9 1.
Markowitz, H.M., Investment for the long run: new evidence
for an old rule. Journal 0/ Finance, 1976, 31,1273-1286.
Markowitz, H.M., Meall-variance Analysis ill PorlJolio Choice
alld Capital Markets, 1987 (Basil Blackwell: New York).
Merton, R.C., COl1linuous Time Finance, 2nd ed., 1992
(Blackwell: Malden, MA).
Mulvey, J.M. and Vladimirou, H., Stochastic network programming for financial planning problems. Management Science,
1992, 38, 1642-1664.
Ogryczak, W. and Ruszczynski, A., Dual stochastic dominance
and related mean risk models. S IAM Journal on Optimization,
2002, 13, 60-78.
Pratt, J.W., Risk aversion in the small and in the large.
Econometrica, 1964, 32, 122- 136.
Rockafeller, R.T. and Uryasev, S., Optimization of conditional
val ue-at-risk. Journal of Risk, 2000, 2, 21-41.
Rockafeller, R.T. and Ziemba, W., Modified risk measures
and
acceptance
sets.
Mimeo.
University
of
British
Columbia, 2000.
Rogers,
L.C.G.,
The
relaxed
investor
and
parameter
uncertainty. Finance and Slochastics, 2000, 5, \31- 154.
Thorp,
E.O., Portfolio choice and the Kelly criterion.
In Stochastic Optimization Models in Finance, edited by
W.T.
Ziemba and
R.G.
Vickson, pp. 599- 619,
1975
(Academic Press: New York).
Xia, Y., l earning about predictability: the effects of parameter
uncertainty on dynamic asset allocation. JOllrnal oj Finance,
200 I, 56, 205- 246.
--- page 299 ---

This page is intentionally left blank
--- page 300 ---

20
Survival and Evolutionary Stability of the Kelly Rule*
Igor V. Evstigneev
Economics Department, School of Social Sciences,
University of Manchester, United Kingdom
igor. evstigneev@manchester.ac.uk
Thorsten Hens
Swiss Banking Institute, University of Zurich, Switzerland
thens@isb. uzh. ch
Klaus Reiner Schenk-Hoppe
Leeds University Business School and School of Mathematics,
University of Leeds, United Kingdom
K.R.Schenk-Hoppe@leeds.ac.uk
Abstract
This chapter gives an overview of current research in evolutionary finance. We
mainly focus on the survival and stability properties of investment strategies
associated with the Kelly rule. Our approach to the study of the wealth dynamics
of investment strategies is inspired by Darwinian ideas on selection and mutation.
The goal of this research is to develop an evolutionary framework for practical
investment advice.
1
Introduction
273
The principal objective of our evolutionary approach to the study of financial market
dynamics is the development and analysis of models that constitute a plausible
alternative to the conventional general equilibrium framework. Our aim is to provide
a framework that is suitable for delivering practical investment advice.
The equilibrium concept most commonly used in financial economics is due to
Radner (1972). This equilibrium notion involves the plans and price expectations
*Financial support by the Finance Market Fund, Norway (project Stability of Financial Markets:
An Evolutionary Approach) and the National Center of Competence in Research "Financial Valuation and Risk Management" , Switzerland (project Behavioural and Evolutionary Finance) is
gratefully acknowledged. This chapter was written during KRSH's visit to the Department of
Finance and Management Science at the Norwegian School of Economics and Business Administration in August 2009. We are grateful to Terje Lensberg, Edward O. Thorp and William
T. Ziemba for their helpful comments.
--- page 301 ---

274
I V. Evstigneev, T Hens and K. R. Schenk-Hoppe
of agents as well as market prices. A well-known drawback of that framework is
the necessity of agents to have perfect foresight (rational expectations) in order
to establish an equilibrium (see the discussion in Laffont (1989) and Dubey et al.
(1987)) market participants have to agree on the future prices for each of the possible
future realizations of the states of the world (without knowing which particular state
will be realized).
Our evolutionary model differs radically from that approach: only historical
observations and the current state of the world influence the agents' behavior; no
agreement about the future market structure is required and no coordinated actions
by the agents are assumed. From a practical finance perspective, the important distinction between our approach and the conventional general equilibrium paradigm
lies in the data required to formulate the model. The evolutionary model does
not use agents' characteristics that are unobservable (such as individual utilities
or subjective beliefs). We describe aims of investors in terms of properties (survival, evolutionary stability, etc.) holding almost surely, rather than in terms of
the maximization of expected utilities. We consider this robust modeling approach
as the basis for developing a new generation of dynamic equilibrium models that
could be used for practical quantitative recommendations applicable in the financial
industry.
The general approach underlying this direction of work is to apply evolutionary
dynamics -
mutation and selection -
to the analysis of the long-run performance of
investment strategies. A stock market is understood as a heterogeneous population
of frequently interacting portfolio rules in competition for market capital. The
ultimate goal is to build a Darwinian theory of portfolio selection. Evolutionary
ideas have a long history in the social sciences going back to Malthus, who played
an inspirational role for Darwin (for a review of the subject see, e.g., Hodgeson
(1993). A more recent stage of development of these ideas began in the 1950s with
the publications of Alchian (1950) and others. An important role in this line of
work has been played by the interdisciplinary research conducted in the 1980s and
1990s under the auspices of the Santa Fe Institute in New Mexico, USA -
see,
e.g., Arthur et al. (1997) , Farmer and Lo (1999) , LeBaron et al. (1999) , Blume and
Easley (1992) , and Blume and Durlauf (2005).
Our model also revives the literature on stochastic dynamic games going back
to Shapley (1953). The framework also shares some conceptual features with the
games of survival pioneered by Milnor and Shapley (1957) and the dynamic market
game in Shubik and Whitt (1973). The main difference is that we use the notion
of survival strategies rather than that of Nash equilibrium. In a finance context,
the focus on survival is an advantage (over those approaches invoking expectations)
because it is a property holding almost surely and not requiring discounted or
undiscounted utility.
This survey is based on the research carried out by Amir et al. (2005, 2008,
2009), Evstigneev et al. (2002, 2006, 2008) and Hens and Schenk-Hoppe (2005).
--- page 302 ---

Survival and Evolutionary Stability of the Kelly Rule
275
A general survey of evolutionary finance is provided by Evstigneev et al. (2009).
The issue of survival of traders in Radner's setting has been studied by Blume and
Easley (1992); see also the surveys Blume and Easley (2008, 2009).
Section 2 explains in details the model, Section 3 discusses its dynamics and
defines the concepts of survival and evolutionary stability, Section 4 surveys the
results obtained in the literature, and Section 5 concludes.
2
Model
Consider a market in which K ~ 2 assets are traded. Each asset k = 1, 2, ... , K pays
dividends at dates t = 1,2, .... The non-negative payoff Dt,k(st) ~ 0 depends on the
history st = (Sl' ... , St) of states of the world up to date t. The states are random
factors modeled in terms of an exogenous stochastic process Sl, S2, ... , where St is a
random element of a measurable space St. We assume functions to be measurable
throughout the following. At each date (and in each random situation), at least one
asset is assumed to pay a strictly positive dividend:
K L Dt,k(st) > 0 for all t, st.
(1)
k=l
The total net supply of asset k is equal to the random amount Vt,k(st) > 0
(a constant VO,k > 0 at the initial time t = 0). The vector of market prices
is Pt =
(Pt,l, ···,Pt,K) E RIf., where Pt,k is the price per unit.
We assume
vt,k(st)/vt_l ,k(st-l) ~ '"Y > 0 for t ~ 0 and all st. This condition is satisfied, e.g.,
if the asset supply is constant or increasing; the supply however cannot decrease at
an ever-increasing rate.
There are N ~ 2 investors, or traders, acting in the market. A portfolio of
investor i at date t = 0, 1, ... is specified by a vector e~ =
(e~ , l' ... , e~ , K) E RIf. where
e~ k is the number of units of asset k held in the portfolio. The value of investor
i'~ portfolio at date tis (Pt, e~) = 'Lf=l pt,keLk' The state of the market at each
date t is characterized by the set (Pt, et, ... , ef) consisting of the price vector and
all traders' portfolios.
Investors i = 1,2, ... , N enter the market at date t = 0 with endowments
wb > 0 that form their initial budgets. At date t ~ 1, investor i's budget is
(Dt(st) + Pt, eLl), where Dt(st) = (Dt,l(St), ... , Dt,K(St)). This budget consists of
two components linked to the portfolio eLl: the dividends (Dt(st), eLl) received
and the market value (Pt, eLl) expressed in terms of the current prices Pt.
A fraction ex of the budget is invested in assets. We will assume that the investment rate ex E (0,1) is a fixed number, the same for all the traders. The remaining
amount of wealth is withdrawn from the market through a tax rate 1 -
ex (or, if
you dislike taxes, through a consumption rate 1 - ex). The assumption of a common
1 -
ex for all the investors is quite natural when interpreted as a tax rate. As a
consumption rate it might seem a restrictive condition, however, it is indispensable
--- page 303 ---

276
1. V. Evstigneev, T Hens and K. R, Schenk-Hoppe
since we focus on the analysis of the comparative performance of trading strategies
in the long run, Without this assumption, an analysis of this kind does not make
sense: a seemingly worse long-run performance of an investment strategy might be
simply due to a higher consumption rate,
For each t ;::: 0, every trader i = 1,2, "" N selects a vector of portfolio weights
A~ = (A~ 1, "" A~ K) according to which he/she plans to distribute the available budget bet';een ass~ts, Vectors A~ belong to the unit simplex /j. K = {( aI, "" a K) ;::: 0 :
a1 + '" + aK = I}, In game-theoretic terms, the vectors A~ represent the investors'
actions, The portfolio weights at each date t ;::: 0 are selected by the N investors simultaneously and independentlythe investors participate in a simultaneous-move
N -person dynamic game,
The investors' actions can depend (for t ;::: 1) on the history st of the states of
the world and the history of the game (pt-1, ()t-1, At - l ), where pt-1 = (Po, ""pt-d
is the history of asset price vectors and
()t-1 = (()o, ()l, "" ()t-d, ()I = (()t, "" ()r)
At- 1 = (AO, AI, "" At-d, Al = (Ai, "" Ar)
are the sets of vectors describing the portfolios and the portfolio weights of all the
traders at all the dates up to t - 1.
The history of the game contains information about the market history -
the
sequence (Po, ()o), "" (Pt-l, ()t-d ofthe states ofthe market -
and about the actions
At of all the investors i = 1, "" N at all the dates l = 0, "" t - 1. A vector Ab E /j.K
and a sequence of measurable functions with values in /j. K
Ai( t
t-1 ()t-1 \i-1) t
1 2
t S,P
,
, /\
,
=
, ""
form an investment strategy Ai of trader i, specifying a portfolio rule according
to which trader i selects portfolio weights at each date t ;::: 0, This is a general
game-theoretic definition of a strategy, assuming full information about the history
of the game, including the players' previous actions, and the knowledge of all the
past and present states of the world, Among general investment strategies, we will
distinguish those for which A~ depends only on st and not on the market history,
We will call such strategies basic, Note that basic strategies are in general not
simple (constant),
To complete the description of the market, it remains to define a dynamic equilibrium for the assets, Suppose that at date 0, each investor i has selected some
portfolio weights Xo = (Ab l' "" Xo K) E /j. K, Then the amount invested in asset k
by trader i is exAb,k Wo and 'the tot~l amount invested in asset k is ex L~l Ab,k wo' It
is assumed that the market is always in equilibrium (asset supply is equal to asset
demand), which makes it possible to determine the equilibrium price PO,k of each
asset k from the equation
N
PO,k VO,k = ex L Xb,k wb
(2)
i=l
--- page 304 ---

Survival and Evolutionary Stability a/the Kelly Rule
277
The left-hand side is the total market value PO,k VO,k of the supply of asset k while the
right-hand side represents the total wealth invested in asset k by all the investors.
Equilibrium ensures that both sides are equal, i.e., (2) holds. The portfolio weights
>"0 chosen by the traders at date 0 determine their portfolios eo at date 0 by
.
o>"hkwO
eo k =
'
,
PO,k
(3)
i.e., the current market value PO,keO,k of the kth position of investor i's portfolio is
equal to the fraction >"O,k of the investor's investment budget owb.
Consider now the situation at any date t ~ 1. Suppose all investors have chosen
their portfolio weights >..~ = (>..~ I, ... , >..~ K)' Then the equilibrium of asset supply
,
,
and demand determines the market-clearing prices of assets k = 1, ... , K through
the relation
N
Pt,k vt,k = a L >"~ , k(Dt(st) + Pt , e~_ l )
i=l
(4)
The investment budgets o(Dt(st) + Pt, e~_ l ) of the traders i = 1,2, ... , N are distributed between assets in the proportions >..tk' so that the kth position of the
trader i's portfolio e~ is
(5)
The price vector Pt is determined implicitly as the solution to the system of
equations (4). The existence and uniqueness of a non-negative vector Pt solving (4)
(for any st and any feasible eL l and >"D is proved in Amir et al. (2009, Proposition
1).
For a given strategy profile (AI , ... , AN ) of investors and their endowments
W6, ... , wr/, a path of the market game is generated by setting
(6)
(7)
for all t = 1, 2, ... , and i = 1, ... , N; and by defining Pt and e~ recursively according
to equations (2)- (5). The random dynamical system (Arnold 1998) described above
defines step by step the vectors of portfolio weights >"~(st) , the equilibrium prices
Pt(st) and the investors' portfolios e ~ (s t ) as measurable vector functions of st for
each moment of time t ~ 0 (for t = 0 these vectors are constant). Thus, we obtain
a random path of the game
(Pt(st); ei(st) , ... , ef (st); >..i(st) , ... , >..t' (st))
(8)
as a vector stochastic process in Rf. x Rf. N X Rf. N .
The above description is correct only if the price of each asset is strictly positive.
Strategy profiles which guarantee this property at each period will be called admissible. Admissibility is satisfied, e.g., if the strategy profile contains an investor who
--- page 305 ---

278
1. V. Evstigneev, T Hens and K. R. Schenk-Hoppe
uses a strategy with strictly positive portfolio weights. We will deal only with such
strategy profiles from now on and, therefore, have well-definedness of the random
dynamical system. Then (using induction) the equilibrium path all the portfolios
e~ = (e~, l ' ... , e~,K) are non-zero and the wealth
(9)
is strictly positive.
Equation (5) implies L~l e~,k = vt,k, i.e., market clearing for every asset k and
each date t 2': 1 (analogously for t = 0). For every equilibrium state of the market
one therefore has that markets clear, Pt > 0 and e~ =I- 0 for all i.
The description of a financial market is game-theoretic: the market dynamics is
formulated as a simultaneous-move N -person dynamic game. Less general versions
of the model can be motivated by invoking Marshall's (1949) principle of temporary
equilibrium (Evstigneev et al., 2008) or evolutionary dynamics (Evstigneev et al.,
2006).
3
Dynamics and Stability
This section provides details on the dynamics of the model and defines notions of
survival and evolutionary stability. An explicit formulation of the dynamics for the
investors' wealth as well as their relative wealth is given.
3.1
Dynamics and the role of basic strategies
Let (AI , ... , AN) be an admissible strategy profile of the investors. Consider the
path (8) of the random dynamical system generated by this strategy profile and the
given initial budgets. Let w~ > 0 denote the investor i's wealth at date t 2': O. For
t 2': 1, w~ = wHst) is given by formula (9) while each investor i's endowment, wh,
is a constant.
When studying the dynamics of this wealth process for a fixed strategy profile, it
is sufficient to consider the class of basic strategies, i.e., those strategies for which A~
depends only on the history of states until time t, st, and not on the market history.
This assertion holds because any sequence of vectors Wt = (wi , ... , wf) of wealth
generated by some strategy profile (A!, ... , AN) can be generated by a strategy
profile (Ai (st), ... , Af (st)) consisting of basic portfolio rules. The corresponding
vector functions A~(st) can be defined recursively by (6) and (7), using (2)- (5).
This observation is very useful when studying the dynamic properties (such
as survival or evolutionary stability) for a basic strategy -
as we will do here.
However this 'reduction' of the model to basic strategies has its limitations when
dealing with the characteristics of a general (non-basic) strategy which competes in
markets with different opponents. Such a strategy will in general take on different
basic strategies, dependent on the pool of competitors -
it is therefore not basic.
