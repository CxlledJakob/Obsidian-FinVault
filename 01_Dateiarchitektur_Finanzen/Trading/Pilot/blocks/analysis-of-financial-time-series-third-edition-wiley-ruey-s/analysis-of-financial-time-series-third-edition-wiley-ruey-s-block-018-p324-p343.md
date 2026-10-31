# Analysis of Financial Time Series, Third Edition (Wiley -- Ruey S_ Tsay -- Wiley series in probability and statistics, 3rd ed_, -- John Wiley & Sons, -- isbn13 9780470414354 -- 9f99b80c7b2dedd477f463dc5323f3b6 -- An.pdf — pages 324–343

--- page 324 ---

distributions of stock prices and log returns
297
Consequently, the estimated expected log return for Cisco Systems’ stock was
−0.94% per annum, and the estimated standard deviation was 27.5% per annum
in 2007.
6.4
DISTRIBUTIONS OF STOCK PRICES AND LOG RETURNS
The result of the previous section shows that if one assumes that price of a stock
follows the geometric Brownian motion
dPt = µPt dt + σPt dwt,
then the logarithm of the price follows a generalized Wiener process
d ln(Pt) =

µ −σ 2
2

dt + σ dwt,
where Pt is the price of the stock at time t and wt is a Wiener process. Therefore,
the change in log price from time t to T is normally distributed as
ln(PT ) −ln(Pt) ∼N


µ −σ 2
2

(T −t), σ 2(T −t)

.
(6.9)
Consequently, conditional on the price Pt at time t, the log price at time T > t is
normally distributed as
ln(PT ) ∼N

ln(Pt) +

µ −σ 2
2

(T −t), σ 2(T −t)

.
(6.10)
Using the result of lognormal distribution discussed in Chapter 1, we obtain the
(conditional) mean and variance of PT as
E(PT ) = Pt exp[µ(T −t)],
Var(PT ) = P 2
t exp[2µ(T −t)]{exp[σ 2(T −t)] −1}.
Note that the expectation conﬁrms that µ is the expected rate of return of the stock.
The prior distribution of stock price can be used to make inferences. For
example, suppose that the current price of stock A is $50, the expected return of the
stock is 15% per annum, and the volatility is 40% per annum. Then the expected
price of stock A in 6 months (0.5 year) and the associated variance are given by
E(PT ) = 50 exp(0.15 × 0.5) = 53.89,
Var(PT ) = 2500 exp(0.3 × 0.5)[exp(0.16 × 0.5) −1] = 241.92.
The standard deviation of the price 6 months from now is
√
241.92 = 15.55.
--- page 325 ---

298
continuous-time models and their applications
Next, let r be the continuously compounded rate of return per annum from time
t to T . Then we have
PT = Pt exp[r(T −t)],
where T and t are measured in years. Therefore,
r =
1
T −t ln
PT
Pt

.
By Eq. (6.9), we have
ln
PT
Pt

∼N


µ −σ 2
2

(T −t), σ 2(T −t)

.
Consequently, the distribution of the continuously compounded rate of return per
annum is
r ∼N

µ −σ 2
2 ,
σ 2
T −t

.
The continuously compounded rate of return is, therefore, normally distributed with
mean µ −σ 2/2 and standard deviation σ/
√
T −t.
Consider a stock with an expected rate of return of 15% per annum and a
volatility of 10% per annum. The distribution of the continuously compounded
rate of return of the stock over 2 years is normal with mean 0.15 −0.01/2 = 0.145
or 14.5% per annum and standard deviation 0.1/
√
2 = 0.071 or 7.1% per annum.
These results allow us to construct conﬁdence intervals (CI) for r. For instance,
a 95% CI for r is 0.145±1.96 × 0.071 per annum (i.e., 0.6%, 28.4%).
6.5
DERIVATION OF BLACK–SCHOLES DIFFERENTIAL EQUATION
In this section, we use Ito’s lemma and assume no arbitrage to derive the
Black–Scholes differential equation for the price of a derivative contingent to
a stock valued at Pt. Assume that the price Pt follows the geometric Brownian
motion in Eq. (6.8) and Gt = G(Pt, t) is the price of a derivative (e.g., a call
option) contingent on Pt. By Ito’s lemma,
dGt =
∂Gt
∂Pt
µPt + ∂Gt
∂t
+ 1
2
∂2Gt
∂P 2
t
σ 2P 2
t

dt + ∂Gt
∂Pt
σPt dwt.
The discretized versions of the process and previous result are

Pt = µPt
t + σPt
wt,
(6.11)

Gt =
∂Gt
∂Pt
µPt + ∂Gt
∂t
+ 1
2
∂2Gt
∂P 2
t
σ 2P 2
t

t + ∂Gt
∂Pt
σPt
wt,
(6.12)
--- page 326 ---

derivation of black–scholes differential equation
299
where
Pt and
Gt are changes in Pt and Gt in a small time interval
t. Because

wt = ϵ
√

t for both Eqs. (6.11) and (6.12), one can construct a portfolio of the
stock and the derivative that does not involve the Wiener process. The appropriate
portfolio is short on derivative and long ∂Gt/∂Pt shares of the stock. Denote the
value of the portfolio by Vt. By construction,
Vt = −Gt + ∂Gt
∂Pt
Pt.
(6.13)
The change in Vt is then

Vt = −
Gt + ∂Gt
∂Pt

Pt.
(6.14)
Substituting Eqs. (6.11) and (6.12) into Eq. (6.14), we have

Vt =

−∂Gt
∂t
−1
2
∂2Gt
∂P 2
t
σ 2P 2
t

t.
(6.15)
This equation does not involve the stochastic component
wt. Therefore, under
the no arbitrage assumption, the portfolio Vt must be riskless during the small
time interval
t. In other words, the assumptions used imply that the portfolio
must instantaneously earn the same rate of return as other short-term, risk-free
securities. Otherwise there exists an arbitrage opportunity between the portfolio
and the short-term, risk-free securities. Consequently, we have

Vt = rVt
t = (r
t)Vt,
(6.16)
where r is the risk-free interest rate. By Eqs. (6.13)–(6.16), we have
∂Gt
∂t
+ 1
2
∂2Gt
∂P 2
t
σ 2P 2
t

t = r

Gt −∂Gt
∂Pt
Pt

t.
Therefore,
∂Gt
∂t
+ rPt
∂Gt
∂Pt
+ 1
2σ 2P 2
t
∂2Gt
∂P 2
t
= rGt.
(6.17)
This is the Black–Scholes differential equation for derivative pricing. It can be
solved to obtain the price of a derivative with Pt as the underlying variable. The
solution so obtained depends on the boundary conditions of the derivative. For a
European call option, the boundary condition is
GT = max(PT −K, 0),
--- page 327 ---

300
continuous-time models and their applications
where T is the expiration time and K is the strike price. For a European put option,
the boundary condition becomes
GT = max(K −PT , 0).
Example 6.4.
As a simple example, consider a forward contract on a stock
that pays no dividend. In this case, the value of the contract is given by
Gt = Pt −K exp[−r(T −t)],
where K is the delivery price, r is the risk-free interest rate, and T is the expiration
time. For such a function, we have
∂Gt
∂t
= −rK exp[−r(T −t)],
∂Gt
∂Pt
= 1,
∂2Gt
∂P 2
t
= 0.
Substituting these quantities into the left-hand side of Eq. (6.17) yields
−rK exp[−r(T −t)] + rPt = r{Pt −K exp[−r(T −t)]},
which equals the right-hand side of Eq. (6.17). Thus, the Black–Scholes differential
equation is indeed satisﬁed.
6.6
BLACK–SCHOLES PRICING FORMULAS
Black and Scholes (1973) successfully solved their differential equation in Eq.
(6.17) to obtain exact formulas for the price of European call-and-put options. In
what follows, we derive these formulas using what is called risk-neutral valuation
in ﬁnance.
6.6.1
Risk-Neutral World
The drift parameter µ drops out from the Black–Scholes differential equation. In
ﬁnance, this means the equation is independent of risk preferences. In other words,
risk preferences cannot affect the solution of the equation. A nice consequence of
this property is that one can assume that investors are risk neutral. In a risk-neutral
world, we have the following results:
• The expected return on all securities is the risk-free interest rate r.
• The present value of any cash ﬂow can be obtained by discounting its expected
value at the risk-free rate.
6.6.2
Formulas
The expected value of a European call option at maturity in a risk-neutral world is
E∗[max(PT −K, 0)],
--- page 328 ---

black–scholes pricing formulas
301
where E∗denotes expected value in a risk-neutral world. The price of the call
option at time t is
ct = exp[−r(T −t)]E∗[max(PT −K, 0)].
(6.18)
Yet in a risk-neutral world, we have µ = r, and by Eq. (6.10), ln(PT ) is normally
distributed as
ln(PT ) ∼N

ln(Pt) +

r −σ 2
2

(T −t), σ 2(T −t)

.
Let g(PT ) be the probability density function of PT . Then the price of the call
option in Eq. (6.18) is
ct = exp[−r(T −t)]
 ∞
K
(PT −K)g(PT ) dPT .
By changing the variable in the integration and some algebraic calculations (details
are given in Appendix A), we have
ct = Pt(h+) −K exp[−r(T −t)](h−),
(6.19)
where (x) is the cumulative distribution function (CDF) of the standard normal
random variable evaluated at x,
h+ = ln(Pt/K) + (r + σ 2/2)(T −t)
σ√T −t
,
h−= ln(Pt/K) + (r −σ 2/2)(T −t)
σ
√
T −t
= h+ −σ
√
T −t.
In practice, (x) can easily be obtained from most statistical packages. Alternatively, one can use an approximation given in Appendix B.
The Black–Scholes call formula in Eq. (6.19) has some nice interpretations.
First, if we exercise the call option on the expiration date, we receive the stock,
but we have to pay the strike price. This exchange will take place only when the call
ﬁnishes in-the-money (i.e., PT > K). The ﬁrst term Pt(h+) is the present value
of receiving the stock if and only if PT > K and the second term −K exp[−r(T −
t)](h−) is the present value of paying the strike price if and only if PT > K.
A second interpretation is particularly useful. As shown in the derivation of the
Black–Scholes differential equation in Section 6.5, (h+) = ∂Gt/∂Pt is the number of shares in the portfolio that does not involve uncertainty, the Wiener process.
This quantity is known as the delta in hedging. We know that ct = Pt(h+) + Bt,
where Bt is the dollar amount invested in risk-free bonds in the portfolio (or
short on the derivative). We can then see that Bt = −K exp[−r(T −t)](h−)
--- page 329 ---

302
continuous-time models and their applications
directly from inspection of the Black–Scholes formula. The ﬁrst term of the formula, Pt(h+), is the amount invested in the stock, whereas the second term,
K exp[−r(T −t)](h−), is the amount borrowed.
Similarly, we can obtain the price of a European put option as
pt = K exp[−r(T −t)](−h−) −Pt(−h+).
(6.20)
Since the standard normal distribution is symmetric with respect to its mean 0.0,
we have (x) = 1 −(−x) for all x. Using this property, we have (−hi) =
1 −(hi). Thus, the information needed to compute the price of a put option is
the same as that of a call option. Alternatively, using the symmetry of normal
distribution, it is easy to verify that
pt −ct = K exp[−r(T −t)] −Pt,
which is referred to as the put–call parity and can be used to obtain pt from ct. The
put–call parity can also be obtained by considering the following two portfolios:
1. Portfolio A. One European call option plus an amount of cash equal to
K exp[−r(T −t)].
2. Portfolio B. One European put option plus one share of the underlying stock.
The payoff of these two portfolios is
max(PT , K)
at the expiration of the options. Since the options can only be exercised at the
expiration date, the portfolios must have identical value today. This means
ct + K exp[−r(T −t)] = pt + Pt,
which is the put–call parity given earlier.
Example 6.5.
Suppose that the current price of Intel stock is $80 per share
with volatility σ = 20% per annum. Suppose further that the risk-free interest rate
is 8% per annum. What is the price of a European call option on Intel with a strike
price of $90 that will expire in 3 months?
From the assumptions, we have Pt = 80, K = 90, T −t = 0.25, σ = 0.2, and
r = 0.08. Therefore,
h+ = ln(80/90) + (0.08 + 0.04/2) × 0.25
0.2
√
0.25
= −0.9278,
h−= h+ −0.2
√
0.25 = −1.0278.
--- page 330 ---

black–scholes pricing formulas
303
Using any statistical software (e.g., R or S-Plus) or the approximation in Appendix
B, we have
(−0.9278) = 0.1767,
(−1.0278) = 0.1520.
Consequently, the price of a European call option is
ct = $80(−0.9278) −$90(−1.0278) exp(−0.02) = $0.73.
The stock price has to rise by $10.73 for the purchaser of the call option to break
even.
Under the same assumptions, the price of a European put option is
pt = $90 exp(−0.08 × 0.25)(1.0278) −$80(0.9278) = $8.95.
Thus, the stock price can rise an additional $1.05 for the purchaser of the put option
to break even.
Example 6.6.
The strike price of the previous example is well beyond the
current stock price. A more realistic strike price is $81. Assume that the other
conditions of the previous example continue to hold. We now have Pt = 80, K =
81, r = 0.08, and T −t = 0.25, and the hi become
h+ = ln(80/81) + (0.08 + 0.04/2) × 0.25
0.2
√
0.25
= 0.125775,
h−= h+ −0.2
√
0.25 = 0.025775.
Using the approximation in Appendix B, we have (0.125775) = 0.5500 and
(0.025775) = 0.5103. The price of a European call option is then
ct = $80(0.125775) −$81 exp(−0.02)(0.025775) = $3.49.
The price of the stock has to rise by $4.49 for the purchaser of the call option to
break even. On the other hand, under the same assumptions, the price of a European
put option is
pt = $81 exp(−0.02)(−0.025775) −$80(−0.125775)
= $81 exp(−0.02) × 0.48972 −$80 × 0.44996 = $2.89.
The stock price must fall $1.89 for the purchaser of the put option to break
even.
--- page 331 ---

304
continuous-time models and their applications
6.6.3
Lower Bounds of European Options
Consider the call option of a nondividend-paying stock. It can be shown that the
price of a European call option satisﬁes
ct ≥Pt −K exp[−r(T −t)];
that is, the lower bound for a European call price is Pt −K exp[−r(T −t)]. This
result can be veriﬁed by considering two portfolios:
1. Portfolio A. One European call option plus an amount of cash equal to
K exp[−r(T −t)].
2. Portfolio B. One share of the stock.
For portfolio A, if the cash is invested at the risk-free interest rate, it will result in
K at time T . If PT > K, the call option is exercised at time T and the portfolio is
worth PT . If PT < K, the call option expires worthless and the portfolio is worth
K. Therefore, the value of portfolio is
max(PT , K).
The value of portfolio B is PT at time T . Hence, portfolio A is always worth more
than (or, at least, equal to) portfolio B. It follows that portfolio A must be worth
more than portfolio B today; that is,
ct + K exp[−r(T −t)] ≥Pt,
or
ct ≥Pt −K exp[−r(T −t)].
Furthermore, since ct ≥0, we have
ct ≥max(Pt −K exp[−r(T −t)], 0).
A similar approach can be used to show that the price of a corresponding
European put option satisﬁes
pt ≥max{K exp[−r(T −t)] −Pt, 0}.
Example 6.7.
Suppose that Pt = $30, K = $28, r = 6% per annum, and T −
t = 0.5. In this case,
Pt −K exp[−r(T −t)] = $[30 −28 exp(−0.06 × 0.5)] ≈$2.83.
Assume that the European call price of the stock is $2.50, which is less than the
theoretical minimum of $2.83. An arbitrageur can buy the call option and short the
stock. This provides a new cash ﬂow of $(30 −2.50) = $27.50. If invested for 6
months at the risk-free interest rate, the $27.50 grows to $27.50 exp(0.06 × 0.5) =
$28.34. At the expiration time, if PT > $28, the arbitrageur exercises the option,
--- page 332 ---

black–scholes pricing formulas
305
closes out the short position, and makes a proﬁt of $(28.34 −28) = $0.34. On
the other hand, if PT < $28, the stock is bought in the market to close the short
position. The arbitrageur then makes an even greater proﬁt. For illustration, suppose
that PT = $27.00, then the proﬁt is $(28.34 −27.00) = $1.34.
6.6.4
Discussion
From the formulas, the price of a call or put option depends on ﬁve
variables—namely, the current stock price Pt, the strike price K, the time to
expiration T −t measured in years, the volatility σ per annum, and the interest
rate r per annum. It pays to study the effects of these ﬁve variables on the price
of an option.
Marginal Effects
Consider ﬁrst the marginal effects of the ﬁve variables on the price of a call option
ct. By marginal effects we mean changing one variable while holding the others
ﬁxed. The effects on a call option can be summarized as follows:
1. Current Stock Price Pt. ct is positively related to ln(Pt). In particular, ct →0
as Pt →0 and ct →∞as Pt →∞. Figure 6.3(a) illustrates the effects with
K = 80, r = 6% per annum, T −t = 0.25 year, and σ = 30% per annum.
Current stock price
(a)
(b)
Value of a call
0
20
40
60
80
100 120
0
10
20
30
40
Value of a put
0
40
20
60
80
Current stock price
0
20
40
60
80
100 120
Figure 6.3
Marginal effects of current stock price on price of an option with K = 80, T −t = 0.25,
σ = 0.3, and r = 0.06: (a) call option and (b) put option.
--- page 333 ---

306
continuous-time models and their applications
2. Strike Price K. ct is negatively related to ln(K). In particular, ct →Pt as
K →0 and ct →0 as K →∞.
3. Time to Expiration. ct is related to T −t in a complicated manner, but we
can obtain the limiting results by writing h+ and h−as
h+ = ln(Pt/K)
σ
√
T −t
+ (r + σ 2/2)
√
T −t
σ
,
h−= ln(Pt/K)
σ
√
T −t
+ (r −σ 2/2)√T −t
σ
.
If Pt < K, then ct →0 as (T −t) →0. If Pt > K, then ct →Pt −K as
(T −t) →0 and ct →Pt as (T −t) →∞. Figure 6.4(a) shows the marginal
effects of T −t on ct for three different current stock prices. The ﬁxed
variables are K = 80, r = 6%, and σ = 30%. The solid, dotted, and dashed
lines of the plot are for Pt = 70, 80, and 90, respectively.
4. Volatility σ. Rewriting h+ and h−as
h+ = ln(Pt/K) + r(T −t)
σ
√
T −t
+ σ
2
√
T −t,
Time to expiration
(a)
(b)
Value of a call
0.0
0.2
0.4
0.8
0.6
1.0
0
5
10
15
Value of a put
0
2
4
6
8
10
12
Time to expiration
0.0
0.2
0.4
0.8
0.6
1.0
Figure 6.4
Marginal effects of time to expiration on price of an option with K = 80, σ = 0.3, and
r = 0.06: (a) call option and (b) put option. Solid, dotted, and dashed lines are for current stock price
Pt = 70, 80, and 90, respectively.
--- page 334 ---

black–scholes pricing formulas
307
h−= ln(Pt/K) + r(T −t)
σ
√
T −t
−σ
2
√
T −t,
we obtain that (a) if ln(Pt/K) + r(T −t) < 0, then ct →0 as σ →0, and
(b) if ln(Pt/K) + r(T −t) ≥0, then ct →Pt −Ke−r(T −t) as σ →0 and
ct →Pt as σ →∞. Figure 6.5(a) shows the effects of σ on ct for K = 80,
T −t = 0.25, r = 0.06, and three different values of Pt. The solid, dotted,
and dashed lines are for Pt = 70, 80, and 90, respectively.
5. Interest Rate. ct is positively related to r such that ct →Pt as r →∞.
The marginal effects of the ﬁve variables on a put option can be obtained
similarly. Figures 6.3(b), 6.4(b), and 6.5(b) illustrates the effects for some selected
cases.
Some Joint Effects
Figure 6.6 shows the joint effects of volatility and strike price on a call option,
where the other variables are ﬁxed at Pt = 80, r = 0.06, and T −t = 0.25. As
expected, the price of a call option is higher when the volatility is high and the
strike price is well below the current stock price. Figure 6.7 shows the effects on
Volatility
Value of a call
0.0
0.2
0.4
0.6
0.8
1.0
1.2
0
5
10
15
20
25
Volatility
(b)
(a)
Value of a put
0.0
0.2
0.4
0.6
0.8
1.0
1.2
0
5
10
15
20
Figure 6.5
Marginal effects of stock volatility on price of an option with K = 80, T −t = 0.25, and
r = 0.06: (a) call option and (b) put option. Solid, dotted, and dashed lines are for current stock price
Pt = 70, 80, and 90, respectively.
--- page 335 ---

308
continuous-time models and their applications
0.2
0.4
0.6
0.8
1
1.2
Volatility
60
70
80
90
100
Striking price
 0
5 10 15 20 25 30 35
Value of a call
Figure 6.6
Joint effects of stock volatility and strike price on call option with Pt = 80, r = 0.06, and
T −t = 0.25.
0.2
0.4
0.6
0.8
1
1.2
Volatility
60
70
80
90
100
Striking price
 0
10
20
30
40
Value of a put
Figure 6.7
Joint effects of stock volatility and strike price on put option with K = 80, T −t = 0.25,
and r = 0.06.
--- page 336 ---

extension of ito’s lemma
309
a put option under the same conditions. The price of a put option is higher when
the volatility is high and the strike price is well above the current stock price.
Furthermore, the plot also shows that the effects of a strike price on the price of a
put option becomes more linear as the volatility increases.
6.7
EXTENSION OF ITO’S LEMMA
In derivative pricing, a derivative may be contingent on multiple securities. When
the prices of these securities are driven by multiple factors, the price of the derivative is a function of several stochastic processes. The two-factor model for the term
structure of interest rate is an example of two stochastic processes. In this section,
we brieﬂy discuss the extension of Ito’s lemma to the case of several stochastic
processes.
Consider a k-dimensional continuous-time process xt = (x1t, . . . , xkt)′, where k
is a positive integer and xit is a continuous-time stochastic process satisfying
dxit = µi(xt) dt + σi(xt) dwit,
i = 1, . . . , k,
(6.21)
where wit is a Wiener process. It is understood that the drift and volatility functions
µi(xit) and σi(xit) are functions of time index t as well. We omit t from their
arguments to simplify the notation. For i̸ = j, the Wiener processes wit and wjt
are different. We assume that the correlation between dwit and dwjt is ρij. This
means that ρij is the correlation between the two standard normal random variables
ϵi and ϵj deﬁned by
wit = ϵi
t and
wjt = ϵj
t. Assume that Gt = G(xt, t)
is a function of the stochastic processes xit and time t. The Taylor expansion gives

Gt =
k

i=1
∂Gt
∂xit

xit + ∂Gt
∂t
t + 1
2
k

i=1
k

j=1
∂2Gt
∂xit∂xjt

xit
xjt
+ 1
2
k

i=1
∂2Gt
∂xit∂t
xit
t + · · · .
The discretized version of Eq. (6.21) is

wit = µi(xt)
t + σi(xt)
wit,
i = 1, . . . , k.
Using a similar argument as that of Eq. (6.5) in Section 6.3, we can obtain that
lim

t→0(
xit)2 →σ 2
i (xt) dt,
(6.22)
lim

t→0(
xit
xjt) →σi(xt)σj(xt)ρij dt.
(6.23)
--- page 337 ---

310
continuous-time models and their applications
Using Eqs. (6.21)–(6.23), taking the limit as
t →0, and ignoring higher order
terms of
t, we have
dGt =


k

i=1
∂Gt
∂xit
µi(xt) + ∂Gt
∂t
+ 1
2
k

i=1
k

j=1
∂2Gt
∂xit∂xjt
σi(xt)σj(xt)ρij

dt
+
k

i=1
∂Gt
∂xit
σi(xt) dwit.
(6.24)
This is a generalization of Ito’s lemma to the case of multiple stochastic processes.
6.8
STOCHASTIC INTEGRAL
We brieﬂy discuss stochastic integration so that the price of an asset can be obtained
under the assumption that it follows an Ito process. We deduce the integration result
using Ito’s formula. For a rigorous treatment on the topic, readers may consult
textbooks on stochastic calculus. First, like the usual integration of a deterministic
function, integration is the opposite of differentiation so that
 t
0
dxs = xt −x0
continues to hold for a stochastic process xt. In particular, for the Wiener process wt, we have
 t
0 dws = wt because w0 = 0. Next, consider the integration
 t
0 ws dws. Using the prior result and taking integration of Eq. (6.7), we have
w2
t = t + 2
 t
0
ws dws.
Therefore,
 t
0
ws dws = 1
2(w2
t −t).
This is different from the usual deterministic integration for which
 t
0 y dy = (y2
t −
y2
0)/2.
Turn to the case that xt is a geometric Brownian motion—that is, xt satisﬁes
dxt = µxt dt + σxt dwt,
where µ and σ are constant with σ > 0; see Eq. (6.8). Applying Ito’s lemma to
G(xt, t) = ln(xt), we obtain
d ln(xt) =

µ −σ 2
2

dt + σ dwt.
--- page 338 ---

jump diffusion models
311
Performing the integration and using the results obtained before, we have
 t
0
d ln(xs) =

µ −σ 2
2
	  t
0
ds + σ
 t
0
dws.
Consequently,
ln(xt) = ln(x0) + (µ −σ 2/2)t + σwt
and
xt = x0 exp[(µ −σ 2/2)t + σwt].
Changing the notation xt to Pt for the price of an asset, we have a solution for the
price under the assumption that it is a geometric Brownian motion. The price is
Pt = P0 exp[(µ −σ 2/2)t + σwt].
(6.25)
6.9
JUMP DIFFUSION MODELS
Empirical studies have found that the stochastic diffusion model based on Brownian
motion fails to explain some characteristics of asset returns and the prices of their
derivatives [e.g., the “volatility smile” of implied volatilities; see Bakshi, Cao, and
Chen (1997) and the references therein]. Volatility smile is referred to as the convex
function between the implied volatility and strike price of an option. Both out-ofthe-money and in-the-money options tend to have higher implied volatilities than
at-the-money options especially in the foreign exchange markets. Volatility smile
is less pronounced for equity options. The inadequacy of the standard stochastic
diffusion model has led to the developments of alternative continuous-time models.
For example, jump diffusion and stochastic volatility models have been proposed
in the literature to overcome the inadequacy; see Merton (1976) and Dufﬁe (1995).
Jumps in stock prices are often assumed to follow a probability law. For example,
the jumps may follow a Poisson process, which is a continuous-time discrete process. For a given time t, let Xt be the number of times a special event occurs
during the time period [0, t]. Then Xt is a Poisson process if
Pr(Xt = m) = λmtm
m! exp(−λt),
λ > 0.
That is, Xt follows a Poisson distribution with parameter λt. The parameter λ
governs the occurrence of the special event and is referred to as the rate or intensity
of the process. A formal deﬁnition also requires that Xt be a right-continuous
homogeneous Markov process with left-hand limit.
In this section, we discuss a simple jump diffusion model proposed by Kou
(2002). This simple model enjoys several nice properties. The returns implied
--- page 339 ---

312
continuous-time models and their applications
by the model are leptokurtic and asymmetric with respect to zero. In addition,
the model can reproduce volatility smile and provide analytical formulas for the
prices of many options. The model consists of two parts, with the ﬁrst part being
continuous and following a geometric Brownian motion and the second part being
a jump process. The occurrences of jump are governed by a Poisson process, and
the jump size follows a double exponential distribution. Let Pt be the price of an
asset at time t. The simple jump diffusion model postulates that the price follows
the stochastic differential equation
dPt
Pt
= µ dt + σ dwt + d
 nt

i=1
(Ji −1)

,
(6.26)
where wt is a Wiener process, nt is a Poisson process with rate λ, and {Ji} is a
sequence of independent and identically distributed nonnegative random variables
such that X = ln(J) has a double exponential distribution with probability density
function
fX(x) = 1
2ηe−|x−κ|/η,
0 < η < 1.
(6.27)
The double exponential distribution is also referred to as the Laplacian distribution.
In model (6.26), nt, wt, and Ji are independent so that there is no relation between
the randomness of the model. Notice that nt is the number of jumps in the time
interval [0, t] and follows a Poisson distribution with parameter λt, where λ is a
constant. At the ith jump, the proportion of price jump is Ji −1.
The double exponential distribution can be written as
X −κ =

ξ
with probability 0.5,
−ξ
with probability 0.5,
(6.28)
where ξ is an exponential random variable with mean η and variance η2. The
probability density function of ξ is
f (x) = 1
ηe−x/η,
0 < x < ∞.
Some useful properties of the double exponential distribution are
E(X) = κ,
Var(X) = 2η2,
E(eX) =
eκ
1 −η2 .
For ﬁnite samples, it is hard to distinguish a double exponential distribution from a
Student-t distribution. However, a double exponential distribution is more tractable
analytically and can generate a higher probability concentration (e.g., higher peak)
around its mean value. As stated in Chapter 1, histograms of observed asset returns
tend to have a higher peak than the normal density. Figure 6.8 shows the probability
--- page 340 ---

jump diffusion models
313
x
Density
−0.2
−0.1
0.0
0.1
0.2
0
5
10
15
20
25
Figure 6.8
Probability density functions of double exponential and normal random variable with
mean zero and variance 0.0008. Solid line denotes the double exponential distribution. Dotted line is
the normal distribution.
density function of a double exponential random variable in the solid line and that
of a normal random variable in the dotted line. Both variables have mean zero and
variance 0.0008. The high peak of the double exponential density is clearly seen.
Solving the stochastic differential equation in Eq. (6.26), we obtain the dynamics
of the asset price as
Pt = P0 exp

µ −σ 2
2

t + σwt
 nt

i=1
Ji,
(6.29)
where it is understood that 0
i=1 = 1. This result is a generalization of Eq. (6.25)
by including the stochastic jumps. It can be obtained as follows. Let ti be the time
of the ith jump. For t ∈[0, t1), there is no jump and the price is given in Eq. (6.25).
Consequently, the left-hand price limit at time t1 is
Pt−
1 = P0 exp[(µ −σ 2/2)t1 + σwt1].
At time t1, the proportion of price jump is J1 −1 so that the price becomes
Pt1 = (1 + J1 −1)Pt−
1 = J1Pt−
1 = P0 exp[(µ −σ 2/2)t1 + σwt1]J1.
For t ∈(t1, t2), there is no jump in the interval (t1, t] so that
Pt = Pt1 exp[(µ −σ 2/2)(t −t1) + σ(wt −wt1)].
--- page 341 ---

314
continuous-time models and their applications
Plugging in Pt1, we have
Pt = P0 exp[(µ −σ 2/2)t + σwt]J1.
Repeating the scheme, we obtain Eq. (6.29).
From Eq. (6.29), the simple return of the underlying asset in a small time
increment
t becomes
Pt+
t −Pt
Pt
= exp



µ −1
2σ 2

t + σ(wt+
t −wt) +
nt+
t

i=nt+1
Xi

−1,
where it is understood that a summation over an empty set is zero and Xi = ln(Ji).
For a small
t, we may use the approximation ex ≈1 + x + x2/2 and the result
(
wt)2 ≈
t discussed in Section 6.3 to obtain
Pt+
t −Pt
Pt
≈

µ −1
2σ 2

t + σ
wt +
nt+
t

i=nt+1
Xi + 1
2σ 2(
wt)2
≈µ
t + σϵ
√

t +
nt+
t

i=nt+1
Xi,
where
wt = wt+
t −wt and ϵ is a standard normal random variable.
Under the assumption of a Poisson process, the probability of having one jump
in the time interval (t, t +
t] is λ
t and that of having more than one jump is
o(
t), where the symbol o(
t) means that if we divide this term by
t then its
value tends to zero as
t tends to zero. Therefore, for a small
t, by ignoring
multiple jumps, we have
nt+
t

i=nt+1
Xi ≈
 Xnt+1
with probability λ
t,
0
with probability 1 −λ
t.
Combining the prior results, we see that the simple return of the underlying asset
is approximately distributed as
Pt+
t −Pt
Pt
≈µ
t + σϵ
√

t + I × X,
(6.30)
where I is a Bernoulli random variable with Pr(I = 1) = λ
t and Pr(I = 0) =
1 −λ
t, and X is a double exponential random variable deﬁned in Eq. (6.28).
Equation (6.30) reduces to that of a geometric Brownian motion without jumps.
Let G = µ
t + σϵ
√

t + I × X be the random variable on the right-hand
side of Eq. (6.30). Using the independence between the exponential and normal
--- page 342 ---

jump diffusion models
315
distributions used in the model, Kou (2002) obtains the probability density function
of G as
g(x) = λ
t
2η eσ 2
t/(2η2)

e−ω/η
ωη −σ 2
t
ση
√

t

+ eω/η
ωη + σ 2
t
ση
√

t
	
+ (1 −λ
t)
1
σ
√

t
f
x −µ
t
σ
√

t

,
(6.31)
where ω = x −µ
t −κ, and f (·) and (·) are, respectively, the probability density and cumulative distribution functions of the standard normal random variable.
Furthermore,
E(G) = µ
t + κλ
t,
Var(G) = σ 2
t + λ
t[2η2 + κ2(1 −λ
t)].
Figure 6.9 shows some comparisons between probability density functions of a
normal distribution and the distribution of Eq. (6.31). Both distributions have mean
zero and variance 2.0572 × 10−4. The mean and variance are obtained by assuming
that the return of the underlying asset satisﬁes µ = 20% per annum, σ = 20% per
annum,
t = 1 day = 1/252 year, λ = 10, κ = −0.02, and η = 0.02. In other
words, we assume that there are about 10 daily jumps per year with average jump
size −2%, and the jump size standard error is 2%. These values are reasonable
for a U.S. stock. From the plots, the leptokurtic feature of the distribution derived
from the jump diffusion process in Eq. (6.26) is clearly shown. The distribution
has a higher peak and fatter tails than the corresponding normal distribution.
6.9.1
Option Pricing under Jump Diffusion
In the presence of random jumps, the market becomes incomplete. In this case, the
standard hedging arguments are not applicable to price an option. But we can still
derive an option pricing formula that does not depend on attitudes toward risk by
assuming that the number of securities available is very large so that the risk of the
sudden jumps is diversiﬁable and the market will therefore pay no risk premium
over the risk-free rate for bearing this risk. Alternatively, for a given set of risk
premiums, one can consider a risk-neutral measure P ∗such that
dPt
Pt
= [r −λE(J −1)] dt + σ dwt + d
 nt

i=1
(Ji −1)

= (r −λψ) dt + σ dwt + d
 nt

i=1
(Ji −1)

,
where r is the risk-free interest rate, J = exp(X) such that X follows the double
exponential distribution of Eq. (6.27), ψ = eκ/(1 −η2) −1, 0 < η < 1, and the
parameters κ, η, ψ, and σ become risk-neutral parameters taking consideration of
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
