# INVESTMENT VALUATION TOOLS AND TECHNIQUES FOR DETERMINING -- Aswath Damodaran -- Wiley finance series, 3rd ed_, Hoboken, N_J, New Jersey, -- John -- isbn13 9781118011522 -- f84d1622bdc2de526da0dda803c52830 -- Anna’s.pdf — pages 115–134

--- page 115 ---

FIGURE 5.4
Cumulative Normal Distribution
A NOTE ON ESTIMATING THE INPUTS TO THE BLACK-SCHOLES MODEL
The Black-Scholes model requires inputs that are consistent on time measurement. There are two places where this affects estimates. The ﬁrst relates to the
fact that the model works in continuous time, rather than discrete time. That
is why we use the continuous time version of present value (exp–rt) rather than
the discrete version, (1 + r)–t. It also means that the inputs such as the riskless
rate have to be modiﬁed to make them continuous time inputs. For instance, if
the one-year Treasury bond rate is 6.2 percent, the risk-free rate that is used in
the Black-Scholes model should be:
Continuous riskless rate = ln(1 + Discrete riskless rate)
= ln(1.062) = .06015 or 6.015%
The second relates to the period over which the inputs are estimated. For
instance, the preceding rate is an annual rate. The variance that is entered
into the model also has to be an annualized variance. The variance, estimated
from ln(asset prices), can be annualized easily because variances are linear in
time if the serial correlation is zero. Thus, if monthly or weekly prices are
used to estimate variance, the variance is annualized by multiplying by 12 or
52, respectively.
96
OPTION PRICING THEORY AND MODELS
--- page 116 ---

ILLUSTRATION 5.2:
Valuing an Option Using the Black-Scholes Model
On March 6, 2001, Cisco Systems was trading at $13.62. We will attempt to value a July 2001 call option with a strike price of $15, trading on the CBOE on the same day for $2. The following are the
other parameters of the options:
■The annualized standard deviation in Cisco Systems stock price over the previous year was 81%.
This standard deviation is estimated using weekly stock prices over the year, and the resulting
number was annualized as follows:
Weekly standard deviation = 11.23%
■The option expiration date is Friday, July 20, 2001. There are 103 days to expiration, and the annualized Treasury bill rate corresponding to this option life is 4.63%.
The inputs for the Black-Scholes model are as follows:
Current stock price (S) = $13.62
Strike price on the option = $15
Option life = 103/365 = 0.2822
Standard deviation in ln(stock prices) = 81%
Riskless rate = 4.63%
Inputting these numbers into the model, we get:
Using the normal distribution, we can estimate the N(d1) and N(d2):
N(d1) = .5085
N(d2) = .3412
The value of the call can now be estimated:
Value of Cisco call = S N(d1) – K e–rt N(d2)
= 13.62(.5085) – 15 e–(.0463)(.2822)(.3412) = $1.87
Since the call is trading at $2, it is slightly overvalued, assuming that the estimate of standard
deviation used is correct.
d
ln
d
1
2
2
13 62
15 00
0463
81
2
2822
81
2822
0212
0212
81
2822
4091
=
⎛
⎝⎜
⎞
⎠⎟+
+
⎛
⎝⎜
⎞
⎠⎟
=
=
−
= −
.
.
.
.
.
.
.
.
.
.
.
.
Annualized standard deviation = 11.23% × 52 = 81%
Option Pricing Models
97
--- page 117 ---

Model Limitations and Fixes
The Black-Scholes model was designed to value
European options that can be exercised only at maturity and whose underlying assets do not pay dividends. In addition, options are valued based on the assumption
that option exercise does not affect the value of the underlying asset. In practice, assets do pay dividends, options sometimes get exercised early, and exercising an option can affect the value of the underlying asset. Adjustments exist that, while not
perfect, provide partial corrections to the Black-Scholes model.
Dividends
The payment of a dividend reduces the stock price; note that on the
ex-dividend day, the stock price generally declines. Consequently, call options
become less valuable and put options more valuable as expected dividend payments increase. There are two ways of dealing with dividends in the Black-
Scholes model:
1. Short-term options. One approach to dealing with dividends is to estimate the
present value of expected dividends that will be paid by the underlying asset
during the option life and subtract it from the current value of the asset to use
as S in the model.
Modiﬁed stock price = Current stock price
– Present value of expected dividends
during the life of the option
2. Long-term options. Since it becomes less practical to estimate the present
value of dividends the longer the option life, an alternate approach can be
used. If the dividend yield (y = Dividends/Current value of the asset) on the
underlying asset is expected to remain unchanged during the life of the option, the Black-Scholes model can be modiﬁed to take dividends into account.
IMPLIED VOLATILITY
The only input in the Black Scholes on which there can be signiﬁcant disagreement among investors is the variance. While the variance is often estimated by
looking at historical data, the values for options that emerge from using the
historical variance can be different from the market prices. For any option,
there is some variance at which the estimated value will be equal to the market price. This variance is called an implied variance.
Consider the Cisco option valued in Illustration 5.2. With a standard deviation of 81 percent, the value of the call option with a strike price of $15
was estimated to be $1.87. Since the market price is higher than the calculated
value, we tried higher standard deviations, and at a standard deviation 85.40
percent the value of the option is $2 (which is the market price). This is the
implied standard deviation or implied volatility.
98
OPTION PRICING THEORY AND MODELS
--- page 118 ---

C = S e–yt N(d1) – K e–rt N(d2)
From an intuitive standpoint, the adjustments have two effects. First, the
value of the asset is discounted back to the present at the dividend yield to
take into account the expected drop in asset value resulting from dividend
payments. Second, the interest rate is offset by the dividend yield to reﬂect
the lower carrying cost from holding the asset (in the replicating portfolio).
The net effect will be a reduction in the value of calls estimated using this
model.
ILLUSTRATION 5.3:
Valuing a Short-Term Option with Dividend Adjustments—
The Black-Scholes Correction
Assume that it is March 6, 2001, and that AT&T is trading at $20.50 a share. Consider a call option on
the stock with a strike price of $20, expiring on July 20, 2001. Using past stock prices, the annualized
standard deviation in the log of stock prices for AT&T is estimated at 60%. There is one dividend,
amounting to $0.15, and it will be paid in 23 days. The riskless rate is 4.63%.
Present value of expected dividend = $0.15/1.046323/365 = $0.15
Dividend-adjusted stock price = $20.50 – $0.15 = $20.35
Time to expiration = 103/365 = 0.2822
Variance in ln(stock prices) = 0.62 = 0.36
Riskless rate = 4.63%
The value from the Black-Scholes model is:
d1 = 0.2551
N(d1) = 0.6007
d2 = –0.0636
N(d2) = 0.4745
Value of call = $20.35(0.6007) – $20 exp–(0.0463)(.2822)(0.4746) = $2.86
The call option was trading at $2.60 on that day.
where d
ln S
K
r
y
t
t
d
d
t
2
1
2
1
2
=
⎛
⎝⎜
⎞
⎠⎟+
−
+
⎛
⎝⎜
⎞
⎠⎟
=
−
σ
σ
σ
Option Pricing Models
99
--- page 119 ---

ILLUSTRATION 5.4:
Valuing a Long-Term Option with Dividend Adjustments—
Primes and Scores
The CBOE offers longer-term call and put options on some stocks. On March 6, 2001, for instance,
you could have purchased an AT&T call expiring on January 17, 2003. The stock price for AT&T is
$20.50 (as in the previous example). The following is the valuation of a call option with a strike price
of $20. Instead of estimating the present value of dividends over the next two years, assume that
AT&T’s dividend yield will remain 2.51% over this period and that the risk-free rate for a two-year
Treasury bond is 4.85%. The inputs to the Black-Scholes model are:
S = Current asset value = $20.50
K = Strike price = $20
Time to expiration = 1.8333 years
Standard deviation in ln(stock prices) = 60%
Riskless rate = 4.85%
Dividend yield = 2.51%
The value from the Black-Scholes model is:
The call was trading at $5.80 on March 8, 2001.
Early Exercise
The Black-Scholes model was designed to value European options
that can be exercised only at expiration. In contrast, most options that we encounter in practice are American options and can be exercised at any time until expiration. As mentioned earlier, the possibility of early exercise makes American
options more valuable than otherwise similar European options; it also makes
them more difﬁcult to value. In general, though, with traded options, it is almost
always better to sell the option to someone else rather than exercise early, since
options have a time premium (i.e., they sell for more than their exercise value).
There are two exceptions. One occurs when the underlying asset pays large dividends, thus reducing the expected value of the asset. In this case, call options
may be exercised just before an ex-dividend date, if the time premium on the
d =
ln
d2 = .4894 − .6
Value of call = $20.50 exp−(.0251)(1.8333) (0.6877) − $20 exp−(.0485)(1.8333)(0.3733) = $6.63
1
20.50
20.00
2 1.8333
1.8333
1.8333  = − .3230                                       N(d2) = 0.3733
⎛
⎝⎜
⎞
⎠⎟+⎛
⎝⎜
⎞
⎠⎟
= 0.4894    N(d1) = 0.6877
.0485 − .0251 + .62
.6
optst.xls: This spreadsheet allows you to estimate the value of a short-term option
when the expected dividends during the option life can be estimated.
optlt.xls: This spreadsheet allows you to estimate the value of an option when the
underlying asset has a constant dividend yield.
100
OPTION PRICING THEORY AND MODELS
--- page 120 ---

options is less than the expected decline in asset value as a consequence of the
dividend payment. The other exception arises when an investor holds both the
underlying asset and deep in-the-money puts (i.e., puts with strike prices well
above the current price of the underlying asset) on that asset at a time when interest rates are high. In this case, the time premium on the put may be less than
the potential gain from exercising the put early and earning interest on the exercise price.
There are two basic ways of dealing with the possibility of early exercise. One
is to continue to use the unadjusted Black-Scholes model and to regard the resulting value as a ﬂoor or conservative estimate of the true value. The other is to try to
adjust the value of the option for the possibility of early exercise. There are two
approaches for doing so. One uses the Black-Scholes model to value the option to
each potential exercise date. With options on stocks, this basically requires that
the investor values options to each ex-dividend day and chooses the maximum of
the estimated call values. The second approach is to use a modiﬁed version of the
binomial model to consider the possibility of early exercise. In this version, the up
and the down movements for asset prices in each period can be estimated from the
variance.2
Approach 1: Pseudo-American Valuation
Step 1: Deﬁne when dividends will be paid and how much the dividends will be.
Step 2: Value the call option to each ex-dividend date using the dividendadjusted approach described earlier, where the stock price is reduced by the
present value of expected dividends.
Step 3: Choose the maximum of the call values estimated for each ex-dividend
day.
ILLUSTRATION 5.5:
Using Pseudo-American Option Valuation to Adjust for Early Exercise
Consider an option with a strike price of $35 on a stock trading at $40. The variance in the ln(stock
prices) is 0.05, and the riskless rate is 4%. The option has a remaining life of eight months, and there
are three dividends expected during this period:
Expected Dividend
Ex-Dividend Day
$0.80
In 1 month
$0.80
In 4 months
$0.80
In 7 months
2To illustrate, if σ2 is the variance in ln(stock prices), the up and the down movements in the
binomial can be estimated as follows:
u = Exp [(r – σ2/2)(T/m) + √(σ2T/m)]
d = Exp [(r – σ2/2)(T/m) – √(σ2T/m)]
where u and d are the up and down movements per unit time for the binomial, T is the life of
the option, and m is the number of periods within that lifetime.
Option Pricing Models
101
--- page 121 ---

The call option is ﬁrst valued to just before the ﬁrst ex-dividend date:
S = $40
K = $35
t = 1/12
σ2 = 0.05
r = 0.04
The value from the Black-Scholes model is:
Value of call = $5.131
The call option is then valued to before the second ex-dividend date:
Adjusted stock price = $40 – $0.80/1.041/12 = $39.20
K = $35
t = 4/12
σ2 = 0.05
r = 0.04
The value of the call based on these parameters is:
Value of call = $5.073
The call option is then valued to before the third ex-dividend date:
Adjusted stock price = $40 – $0.80/1.041/12 – $0.80/1.044/12 = $38.41
K = $35
t = 7/12
σ2 = 0.05
r = 0.04
The value of the call based on these parameters is:
Value of call = $5.128
The call option is then valued to expiration:
Adjusted stock price = $40 – $0.80/1.041/12 – $0.80/1.044/12 – $0.80/1.047/12 = $37.63
K = $35
t = 8/12
σ2 = 0.05
r = 0.04
The value of the call based on these parameters is:
Value of call = $4.757
Pseudo-American value of call = Maximum ($5.131, $5.073, $5.128, $4.757) = $5.131
Approach 2: Using the Binomial Model
The binomial model is much more capable of handling early exercise because it considers the cash ﬂows at each time period, rather than just at expiration. The biggest limitation of the binomial model is
determining what stock prices will be at the end of each period, but this can be
overcome by using a variant that allows us to estimate the up and the down movements in stock prices from the estimated variance. There are four steps involved:
Step 1: If the variance in ln(stock prices) has been estimated for the Black-
Scholes valuation, convert these into inputs for the binomial model:
u = e
d = e
dt
dt

r
dt
dt

r
−
+
⎛
⎝⎜
⎞
⎠⎟
−σ
−
+
⎛
⎝⎜
⎞
⎠⎟
σ
σ
σ
2
2
2
2
102
OPTION PRICING THEORY AND MODELS
--- page 122 ---

where u and d are the up and the down movements per unit time for the binomial,
and dt is the number of periods within each year (or unit time).
Step 2: Specify the period in which the dividends will be paid and make the assumption that the price will drop by the amount of the dividend in that period.
Step 3: Value the call at each node of the tree, allowing for the possibility of
early exercise just before ex-dividend dates. There will be early exercise if the remaining time premium on the option is less than the expected drop in option value
as a consequence of the dividend payment.
Step 4: Value the call at time 0, using the standard binomial approach.
Impact of Exercise on Underlying Asset Value
The Black-Scholes model is based
on the assumption that exercising an option does not affect the value of the underlying asset. This may be true for listed options on stocks, but it is not true for some
types of options. For instance, the exercise of warrants increases the number of
shares outstanding and brings fresh cash into the ﬁrm, both of which will affect the
stock price.3 The expected negative impact (dilution) of exercise will decrease the
value of warrants, compared to otherwise similar call options. The adjustment for
dilution to the stock price is fairly simple in the Black-Scholes valuation. The stock
price is adjusted for the expected dilution from the exercise of the options. In the
case of warrants, for instance:
Dilution-adjusted S = (S ns + W nw)/(ns + nw)
where
S = Current value of the stock
nw = Number of warrants outstanding
W = Value of warrants outstanding
ns = Number of shares outstanding
When the warrants are exercised, the number of shares outstanding will increase,
reducing the stock price. The numerator reﬂects the market value of equity, including both stocks and warrants outstanding. The reduction in S will reduce the value
of the call option.
There is an element of circularity in this analysis, since the value of the warrant
is needed to estimate the dilution-adjusted S and the dilution-adjusted S is needed
to estimate the value of the warrant. This problem can be resolved by starting the
process off with an assumed value for the warrant (e.g., the exercise value or the
current market price of the warrant). This will yield a value for the warrant, and
this estimated value can then be used as an input to reestimate the warrant’s value
until there is convergence.
3Warrants are call options issued by ﬁrms, either as part of management compensation contracts or to raise equity.
bstobin.xls: This spreadsheet allows you to estimate the parameters for a binomial
model from the inputs to a Black-Scholes model.
Option Pricing Models
103
--- page 123 ---

FROM BLACK-SCHOLES TO BINOMIAL
The process of converting the continuous variance in a Black-Scholes model
to a binomial tree is a fairly simple one. Assume, for instance, that you have
an asset that is trading at $30 currently and that you estimate the annualized
standard deviation in the asset value to be 40 percent; the annualized riskless
rate is 5 percent. For simplicity, let us assume that the option that you are
valuing has a four-year life and that each period is a year. To estimate the
prices at the end of each of the four years, we begin by ﬁrst estimating the up
and down movements in the binomial:
Based on these estimates, we can obtain the prices at the end of the ﬁrst node
of the tree (the end of the ﬁrst year):
Up price = $30(1.4477) = $43.43
Down price = $40(0.6505) = $19.52
Progressing through the rest of the tree, we obtain the following numbers:
u
exp
d
exp
=
=
=
=
+
−
⎛
⎝⎜
⎞
⎠⎟
−
+
−
⎛
⎝⎜
⎞
⎠⎟
.
.
.
.
.
.
.
.
4 1
05
4
2 1
4 1
05
40
2
1
2
2
1 4477
0 6505
30
43.43
19.52
62.88
28.25
12.69
8.26
18.38
40.90
91.03
104
OPTION PRICING THEORY AND MODELS
--- page 124 ---

ILLUSTRATION 5.6:
Valuing a Warrant on Avatek Corporation
Avatek Corporation is a real estate ﬁrm with 19.637 million shares outstanding, trading at $0.38 a
share. In March 2001 the company had 1.8 million options outstanding, with four years to expiration
and with an exercise price of $2.25. The stock paid no dividends, and the standard deviation in
ln(stock prices) was 93%. The four-year Treasury bond rate was 4.9%. (The options were trading at
$0.12 apiece at the time of this analysis.)
The inputs to the warrant valuation model are as follows:
S = (0.38 × 19.637 + 0.12 × 1.8 )/(19.637 + 1.8) = 0.3544
K = Exercise price on warrant = 2.25
t = Time to expiration on warrant = 4 years
r = Riskless rate corresponding to life of option = 4.9%
σ2 = Variance in value of stock = 0.932
y = Dividend yield on stock = 0.0%
The results of the Black-Scholes valuation of this option are:
d1 = 0.0418
N(d1) = 0.5167
d2 = –1.8182
N(d2) = 0.0345
Value of option = 0.3544(0.5167) – 2.25 exp–(0.049)(4)(0.0345) = $0.12
The options were trading at $0.12 in March 2001. Since the value was equal to the price, there was no
need for further iterations. If there had been a difference, we would have reestimated the adjusted
stock price and option value. If the options had been non-traded (as is the case with management
options), this calculation would have required an iterative process, where the option value is used to
get the adjusted value per share and the value per share to get the option value.
The Black-Scholes Model for Valuing Puts
The value of a put can be derived from
the value of a call with the same strike price and the same expiration date:
C – P = S – K e–rt
where C is the value of the call and P is the value of the put. This relationship between the call and put values is called put-call parity, and any deviations from
parity can be used by investors to make riskless proﬁts. To see why put-call parity
holds, consider selling a call and buying a put with exercise price K and expiration date t, and simultaneously buying the underlying asset at the current price S.
The payoff from this position is riskless and always yields K at expiration (t). To
see this, assume that the stock price at expiration is S∗. The payoff on each of the
positions in the portfolio can be written as follows:
warrant.xls: This spreadsheet allows you to estimate the value of an option when
there is a potential dilution from exercise.
Option Pricing Models
105
--- page 125 ---

Position
Payoffs at t if S∗ > K
Payoffs at t if S∗ < K
Sell call
–(S∗– K)
0
Buy put
0
K – S∗
Buy stock
S∗
S∗
Total
K
K
Since this position yields K with certainty, the cost of creating this position must be
equal to the present value of K at the riskless rate (K e–rt).
S + P – C = K e–rt
C – P = S – K e–rt
Substituting the Black-Scholes equation for the value of an equivalent call into this
equation, we get:
Value of put = K e–rt [1 – N(d2)] – S e–yt [1 – N(d1)]
Thus, the replicating portfolio for a put is created by selling short [1 – N(d1)] shares
of stock and investing K e–rt[1 – N(d2)] in the riskless asset.
ILLUSTRATION 5.7:
Valuing a Put Using Put-Call Parity: Cisco Systems and AT&T
Consider the call on Cisco Systems that we valued in Illustration 5.2. The call had a strike price of $15
on the stock, had 103 days left to expiration, and was valued at $1.87. The stock was trading at
$13.62, and the riskless rate was 4.63%. The put can be valued as follows:
Put value = C – S + K e–rt = $1.87 – $13.62 + $15 e–(.0463)(.2822) = $3.06
The put was trading at $3.38.
Also, a long-term call on AT&T was valued in Illustration 5.4. The call had a strike price of $20,
1.8333 years left to expiration, and a value of $6.63. The stock was trading at $20.50 and was expected to maintain a dividend yield of 2.51% over the period. The riskless rate was 4.85%. The put
value can be estimated as follows:
Put value = C – S e–yt + K e–rt = $6.63 – $20.5 e–(.0251)(1.8333) + $20 e–(.0485)(1.8333) = $5.35
The put was trading at $3.80. Both the call and the put were trading at different prices from our estimates, which may indicate that we have not correctly estimated the stock’s volatility.
where  d
ln S
K
r
y
t
t
d
d
t
1
2
2
1
2
=
⎛
⎝⎜
⎞
⎠⎟+
−
+
⎛
⎝⎜
⎞
⎠⎟
=
−
σ
σ
σ
106
OPTION PRICING THEORY AND MODELS
--- page 126 ---

Jump Process Option Pricing Models
If price changes remain larger as the time periods in the binomial model are shortened,
it can no longer be assumed that prices change continuously. When price changes remain large, a price process that allows for price jumps is much more realistic. Cox and
Ross (1976) valued options when prices follow a pure jump process, where the jumps
can only be positive. Thus, in the next interval, the stock price will either have a large
positive jump with a speciﬁed probability or drift downward at a given rate.
Merton (1976) considered a distribution where there are price jumps superimposed on a continuous price process. He speciﬁed the rate at which jumps occur (λ)
and the average jump size (k), measured as a percentage of the stock price. The
model derived to value options with this process is called a jump diffusion model.
In this model, the value of an option is determined by the ﬁve variables speciﬁed in
the Black-Scholes model, and the parameters of the jump process (λ, k). Unfortunately, the estimates of the jump process parameters are so difﬁcult to make for
most ﬁrms that they overwhelm any advantages that accrue from using a more realistic model. These models, therefore, have seen limited use in practice.
EXTENSIONS OF OPTION PRICING
All the option pricing models described so far—the binomial, the Black-Scholes,
and the jump process models—are designed to value options with clearly deﬁned
exercise prices and maturities on underlying assets that are traded. However, the
options we encounter in investment analysis or valuation are often on real assets
rather than ﬁnancial assets. Categorized as real options, they can take much more
complicated forms. This section considers some of these variations.
Capped and Barrier Options
With a simple call option, there is no speciﬁed upper limit on the proﬁts that can be
made by the buyer of the call. Asset prices, at least in theory, can keep going up,
and the payoffs increase proportionately. In some call options, though, the buyer is
entitled to proﬁts up to a speciﬁed price but not above it. For instance, consider a
call option with a strike price of K1 on an asset. In an unrestricted call option, the
payoff on this option will increase as the underlying asset’s price increases above
K1. Assume, however, that if the price reaches K2, the payoff is capped at (K2 – K1).
The payoff diagram on this option is shown in Figure 5.5.
This option is called a capped call. Notice, also, that once the price reaches K2,
there is no longer any time premium associated with the option, and the option will
therefore be exercised. Capped calls are part of a family of options called barrier
options, where the payoff on and the life of the option are functions of whether the
underlying asset price reaches a certain level during a speciﬁed period.
The value of a capped call is always lower than the value of the same call without the payoff limit. A simple approximation of this value can be obtained by valuing the call twice, once with the given exercise price and once with the cap, and
taking the difference in the two values. In the preceding example, then, the value of
the call with an exercise price of K1 and a cap at K2 can be written as:
Value of capped call = Value of call (K = K1) – Value of call (K = K2)
Extensions of Option Pricing
107
--- page 127 ---

Barrier options can take many forms. In a knockout option, an option ceases to
exist if the underlying asset reaches a certain price. In the case of a call option, this
knockout price is usually set below the strike price, and this option is called a
down-and-out option. In the case of a put option, the knockout price will be set
above the exercise price, and this option is called an up-and-out option. Like the
capped call, these options are worth less than their unrestricted counterparts. Many
real options have limits on potential upside, or knockout provisions, and ignoring
these limits can result in the overstatement of the value of these options.
Compound Options
Some options derive their value not from an underlying asset, but from other options. These options are called compound options. Compound options can take
any of four forms—a call on a call, a put on a put, a call on a put, or a put on a
call. Geske (1979) developed the analytical formulation for valuing compound options by replacing the standard normal distribution used in a simple option model
with a bivariate normal distribution in the calculation.
Consider, for instance, the option to expand a project that is discussed in Chapter 30. While we will value this option using a simple option pricing model, in reality there could be multiple stages in expansion, with each stage representing an
option for the following stage. In this case, we will undervalue the option by considering it as a simple rather than a compound option.
Notwithstanding this discussion, the valuation of compound options becomes
progressively more difﬁcult as more options are added to the chain. In this case,
rather than wreck the valuation on the shoals of estimation error, it may be better
to accept the conservative estimate that is provided with a simple valuation model
as a ﬂoor on the value.
Rainbow Options
In a simple option, the uncertainty is about the price of the underlying asset. Some
options are exposed to two or more sources of uncertainty, and these options are
rainbow options. Using the simple option pricing model to value such options can
lead to biased estimates of value. As an example, consider an undeveloped oil reserve as an option, where the ﬁrm that owns the reserve has the right to develop the
reserve. Here there are two sources of uncertainty. The ﬁrst is obviously the price of
108
OPTION PRICING THEORY AND MODELS
FIGURE 5.5
Payoff on Capped Call
--- page 128 ---

oil, and the second is the quantity of oil that is in the reserve. To value this undeveloped reserve, we can make the simplifying assumption that we know the quantity of
oil in the reserve with certainty. In reality, however, uncertainty about the quantity
will affect the value of this option and make the decision to exercise more difﬁcult.4
CONCLUSION
An option is an asset with payoffs that are contingent on the value of an underlying
asset. A call option provides its holder with the right to buy the underlying asset at
a ﬁxed price, whereas a put option provides its holder with the right to sell at a
ﬁxed price, at any time before the expiration of the option. The value of an option
is determined by six variables—the current value of the underlying asset, the variance in this value, the expected dividends on the asset, the strike price and life of
the option, and the riskless interest rate. This is illustrated in both the binomial and
the Black-Scholes models, which value options by creating replicating portfolios
composed of the underlying asset and riskless lending or borrowing. These models
can be used to value assets that have option like characteristics.
QUESTIONS AND SHORT PROBLEMS
In the problems following, use an equity risk premium of 5.5 percent if none is
speciﬁed.
1. The following are prices of options traded on Microsoft Corporation, which
pays no dividends.
Call
Put
K = 85
K = 90
K = 85
K = 90
One-month
$2.75
$1.00
$4.50
$ 7.50
Three-month
$4.00
$2.75
$5.75
$ 9.00
Six-month
$7.75
$6.00
$8.00
$12.00
The stock is trading at $83, and the annualized riskless rate is 3.8%. The standard deviation in ln(stock prices) (based on historical data) is 30%.
a. Estimate the value of a three-month call with a strike price of $85.
b. Using the inputs from the Black-Scholes model, specify how you would replicate this call.
c. What is the implied standard deviation in this call?
d. Assume now that you buy a call with a strike price of $85 and sell a call with
a strike price of $90. Draw the payoff diagram on this position.
e. Using put-call parity, estimate the value of a three-month put with a strike
price of $85.
2. You are trying to value three-month call and put options on Merck with a strike
price of $30. The stock is trading at $28.75, and the company expects to pay a
Questions and Short Problems
109
4The analogy to a listed option on a stock is the case where you do not know with certainty
what the stock price is when you exercise the option. The more uncertain you are about the
stock price, the more margin for error you have to give yourself when you exercise the option, to ensure that you are in fact earning a proﬁt.
--- page 129 ---

quarterly dividend per share of $0.28 in two months. The annualized riskless interest rate is 3.6%, and the standard deviation in log stock prices is 20%.
a. Estimate the value of the call and put options, using the Black-Scholes model.
b. What effect does the expected dividend payment have on call values? On put
values? Why?
3. There is the possibility that the options on Merck described in the preceding
problem could be exercised early.
a. Use the pseudo-American call option technique to determine whether this
will affect the value of the call.
b. Why does the possibility of early exercise exist? What types of options are
most likely to be exercised early?
4. You have been provided the following information on a three-month call:
S = 95
K = 90
t = 0.25
r = 0.04
N(d1) = 0.5750
N(d2) = 0.4500
a. If you wanted to replicate buying this call, how much money would you need
to borrow?
b. If you wanted to replicate buying this call, how many shares of stock would
you need to buy?
5. Go Video, a manufacturer of video recorders, was trading at $4 per share in
May 1994. There were 11 million shares outstanding. At the same time, it had
550,000 one-year warrants outstanding, with a strike price of $4.25. The stock
has had a standard deviation of 60%. The stock does not pay a dividend. The
riskless rate is 5%.
a. Estimate the value of the warrants, ignoring dilution.
b. Estimate the value of the warrants, allowing for dilution.
c. Why does dilution reduce the value of the warrants?
6. You are trying to value a long-term call option on the NYSE Composite index,
expiring in ﬁve years, with a strike price of 275. The index is currently at 250,
and the annualized standard deviation in stock prices is 15%. The average dividend yield on the index is 3% and is expected to remain unchanged over the
next ﬁve years. The ﬁve-year Treasury bond rate is 5%.
a. Estimate the value of the long-term call option.
b. Estimate the value of a put option with the same parameters.
c. What are the implicit assumptions you are making when you use the Black-
Scholes model to value this option? Which of these assumptions are likely to
be violated? What are the consequences for your valuation?
7. A new security on AT&T will entitle the investor to all dividends on AT&T over
the next three years, limiting upside potential to 20% but also providing downside protection below 10%. AT&T stock is trading at $50, and three-year call
and put options are traded on the exchange at the following prices:
Call Options
Put Options
K
1-Year
3-Year
1-Year
3-Year
45
$8.69
$13.34
$1.99
$ 3.55
50
$5.86
$10.89
$3.92
$ 5.40
55
$3.78
$  8.82
$6.59
$ 7.63
60
$2.35
$  7.11
$9.92
$10.23
How much would you be willing to pay for this security?
110
OPTION PRICING THEORY AND MODELS
--- page 130 ---

CHAPTER 6
Market Efﬁciency—
Deﬁnition, Tests, and Evidence
W
hat is an efﬁcient market? What does it imply for investment and valuation models? Clearly, market efﬁciency is a concept that is controversial and attracts strong
views, pro and con, partly because of differences between individuals about what it really means, and partly because whether markets are efﬁcient or not  is a core belief
that in large part determines how an investor approaches investing. This chapter provides a deﬁnition of market efﬁciency, considers the implications of an efﬁcient market
for investors, and summarizes some of the basic approaches that are used to test investment schemes, thereby proving or disproving market efﬁciency. It also provides a
summary of the voluminous research on whether markets are efﬁcient.
MARKET EFFICIENCY AND INVESTMENT VALUATION
The question of whether markets are efﬁcient, and, if not, where the inefﬁciencies lie,
is central to investment valuation. If markets are in fact efﬁcient, the market price
provides the best estimate of value, and the process of valuation becomes one of justifying the market price. If markets are not efﬁcient, the market price may deviate from
the true value, and the process of valuation is directed toward obtaining a reasonable
estimate of this value. Those who do valuation well, then, will be able to make higher
returns than other investors because of their capacity to spot underand overvalued
ﬁrms. To make these higher returns, though, markets have to correct their mistakes
(i.e., become efﬁcient) over time. Whether these corrections occur over six months or
over ﬁve years can have a profound impact on which valuation approach an investor
chooses to use and the time horizon that is needed for it to succeed.
There is also much that can be learned from studies of market efﬁciency, which
highlight segments where the market seems to be inefﬁcient. These inefﬁciencies can
provide the basis for screening all stocks to come up with a subsample that is more
likely to contain undervalued stocks. Given the size of the universe of stocks, this
not only saves time for the analyst, but it increases the odds signiﬁcantly of ﬁnding
underand overvalued stocks. For instance, some efﬁciency studies suggest that
stocks that are neglected by institutional investors are more likely to be undervalued and earn excess returns. A strategy that screens ﬁrms for low institutional investment (as a percentage of the outstanding stock) may yield a subsample of
neglected ﬁrms, which can then be valued to arrive at a portfolio of undervalued
ﬁrms. If the research is correct, the odds of ﬁnding undervalued ﬁrms should increase in this subsample.
111
--- page 131 ---

WHAT IS AN EFFICIENT MARKET?
An efﬁcient market is one where the market price is an unbiased estimate of the
true value of the investment. Implicit in this derivation are several key concepts:
■Contrary to popular view, market efﬁciency does not require that the market
price be equal to true value at every point in time. All it requires is that errors
in the market price be unbiased; prices can be greater than or less than true
value, as long as these deviations are random.
■The fact that the deviations from true value are random implies, in a rough
sense, that there is an equal chance that any stock is underor overvalued at
any point in time, and that these deviations are uncorrelated with any observable variable. For instance, in an efﬁcient market, stocks with lower PE ratios
should be no more or no less likely to be undervalued than stocks with high PE
ratios.
■If the deviations of market price from true value are random, it follows that no
group of investors should be able to consistently ﬁnd underor overvalued
stocks using any investment strategy.
Deﬁnitions of market efﬁciency have to be speciﬁc not only about the market
that is being considered but also the investor group that is covered. It is extremely
unlikely that all markets are efﬁcient to all investors at all times, but it is entirely
possible that a particular market (for instance, the New York Stock Exchange) is ef-
ﬁcient with respect to the average investor. It is also possible that some markets are
efﬁcient while others are not, and that a market is efﬁcient with respect to some investors and not to others. This is a direct consequence of differential tax rates and
transaction costs, which confer advantages on some investors relative to others.
Deﬁnitions of market efﬁciency are also linked up with assumptions about
what information is available to investors and reﬂected in the price. For instance, a
strict deﬁnition of market efﬁciency that assumes that all information, public as
well as private, is reﬂected in market prices would imply that even investors with
precise inside information will be unable to beat the market. One of the earliest
classiﬁcations of levels of market efﬁciency was provided by Fama (1971), who argued that markets could be efﬁcient at three levels, based on what information was
reﬂected in prices. Under weak form efﬁciency, the current price reﬂects the information contained in all past prices, suggesting that charts and technical analyses
that use past prices alone would not be useful in ﬁnding undervalued stocks. Under
semi-strong form efﬁciency, the current price reﬂects the information contained not
only in past prices but all public information (including ﬁnancial statements and
news reports) and no approach that is predicated on using and massaging this information would be useful in ﬁnding undervalued stocks. Under strong form efﬁ-
ciency, the current price reﬂects all information, public as well as private, and no
investors will be able to ﬁnd undervalued stocks consistently.
IMPLICATIONS OF MARKET EFFICIENCY
An immediate and direct implication of an efﬁcient market is that no group of investors should be able to beat the market consistently using a common investment
112
MARKET EFFICIENCY—DEFINITION, TESTS, AND EVIDENCE
--- page 132 ---

strategy. An efﬁcient market would also carry negative implications for many investment strategies:
■In an efﬁcient market, equity research and valuation would be a costly task that
would provide no beneﬁts. The odds of ﬁnding an undervalued stock would
always be 50–50, reﬂecting the randomness of pricing errors. At best, the bene-
ﬁts from information collection and equity research would cover the costs of
doing the research.
■In an efﬁcient market, a strategy of randomly diversifying across stocks or indexing to the market, carrying little or no information cost and minimal execution costs, would be superior to any other strategy that created larger
information and execution costs. There would be no value added by active
portfolio managers and investment strategists.
■In an efﬁcient market, a strategy of minimizing trading (i.e., creating a portfolio and not trading unless cash was needed) would be superior to a strategy
that required frequent trading.
It is therefore no wonder that the concept of market efﬁciency evokes such strong
reactions on the part of portfolio managers and analysts, who view it, quite rightly,
as a challenge to their existence.
It is also important that there be clarity about what market efﬁciency does not
imply. An efﬁcient market does not imply that:
■Stock prices cannot deviate from true value; in fact, there can be large deviations from true value. The only requirement is that the deviations be random.
■No investor will beat the market in any time period. To the contrary, approximately half of all investors, prior to transaction costs, should beat the market
in any period.1
■No group of investors will beat the market in the long term. Given the number
of investors in ﬁnancial markets, the laws of probability would suggest that a
fairly large number are going to beat the market consistently over long periods,
not because of their investment strategies but because they are lucky. It would
not, however, be consistent if a disproportionately large number2 of these investors used the same investment strategy.
In an efﬁcient market, the expected returns from any investment will be consistent with the risk of that investment over the long term, though there may be deviations from these expected returns in the short term.
Implications of Market Efﬁciency
113
1Since returns are positively skewed—that is, large positive returns are more likely than large
negative returns (you cannot lose more than 100% on a stock)—less than half of all
investors will probably beat the market.
2One of the enduring pieces of evidence against market efﬁciency lies in the performance
records posted by many of the investors who learned their lessons from Benjamin Graham in
the 1950s. No probability statistics could ever explain the consistency and superiority of
their records.
--- page 133 ---

NECESSARY CONDITIONS FOR MARKET EFFICIENCY
Markets do not become efﬁcient automatically. It is the actions of investors, sensing
bargains and putting into effect schemes to beat the market, that make markets ef-
ﬁcient. The necessary conditions for a market inefﬁciency to be eliminated are:
■The market inefﬁciency should provide the basis for a scheme to beat the market and earn excess returns. For this to hold true:
■The asset or assets that are the source of the inefﬁciency have to be traded.
■The transaction costs of executing the scheme have to be smaller than the
expected proﬁts from the scheme.
■There should be proﬁt-maximizing investors who:
■Recognize the potential for excess return.
■Can replicate the beat-the-market scheme that earns the excess return.
■Have the resources to trade on the stock(s) until the inefﬁciency disappears.
The internal contradiction of claiming that there is no possibility of beating the
market in an efﬁcient market and requiring proﬁt-maximizing investors to constantly seek out ways of beating the market and thus making it efﬁcient has been
explored by many. If markets were in fact efﬁcient, investors would stop looking
for inefﬁciencies, which would lead to markets becoming inefﬁcient again. It makes
sense to think about an efﬁcient market as a self-correcting mechanism, where inef-
ﬁciencies appear at regular intervals but disappear almost instantaneously as investors ﬁnd them and trade on them.
PROPOSITIONS ABOUT MARKET EFFICIENCY
A reading of the conditions under which markets become efﬁcient leads to general
propositions about where investors are most likely to ﬁnd inefﬁciencies in ﬁnancial
markets.
Proposition 1: The probability of ﬁnding inefﬁciencies in an asset market decreases as the ease of trading on the asset increases. To the extent that investors
have difﬁculty trading on an asset, either because open markets do not exist or because there are signiﬁcant barriers to trading, inefﬁciencies in pricing can continue
for long periods.
This proposition can be used to shed light on the differences between different
asset markets. For instance, it is far easier to trade on stocks than it is on real estate,
since markets are much more open, prices are in smaller units (reducing the barriers
to entry for new traders), and the asset itself does not vary from transaction to
transaction (one share of IBM is identical to another share, whereas one piece of
real estate can be very different from another piece that is a stone’s throw away).
Based on these differences, there should be a greater likelihood of ﬁnding inefﬁciencies (both underand overvaluation) in the real estate market.
Proposition 2: The probability of ﬁnding an inefﬁciency in an asset market increases as the transactions and information cost of exploiting the inefﬁciency increases. The cost of collecting information and trading varies widely across markets
and even across investments in the same markets. As these costs increase, it pays
less and less to try to exploit these inefﬁciencies.
114
MARKET EFFICIENCY—DEFINITION, TESTS, AND EVIDENCE
--- page 134 ---

Consider, for instance, the perceived wisdom that investing in “loser” stocks
(i.e., stocks that have done very badly in some prior time period) should yield excess returns. This may be true in terms of raw returns, but transaction costs are
likely to be much higher for these stocks since:
■They tend to be low-priced stocks, leading to higher brokerage commissions
and expenses.
■The bid-ask spread, a transaction cost paid at the time of purchase, becomes a
much higher fraction of the total price paid.
■Trading is often thin on these stocks, and small trades can cause prices to
change, resulting in a higher buy price or a lower sell price.
Corollary 1: Investors who can establish a cost advantage (either in information collection or in transaction costs) will be more able to exploit small inefﬁciencies than other investors who do not possess this advantage.
There are a number of studies that look at the effect of block trades on prices
and conclude that while block trades do affect prices, investors will not exploit
these inefﬁciencies because of the number of times they will have to trade and their
associated transaction costs. These concerns are unlikely to hold for a specialist on
the ﬂoor of the exchange, who can trade quickly, often and at no or very low costs.
It should be pointed out, however, that if the market for specialists is efﬁcient, the
value of a seat on the exchange should reﬂect the present value of potential beneﬁts
from being a specialist.
This corollary also suggests that investors who work at establishing a cost advantage, especially in relation to information, may be able to generate excess returns on the basis of these advantages. Thus John Templeton, who started investing
in Japanese and other Asian markets well before other portfolio managers, might
have been able to exploit the informational advantages he had over his peers to
make excess returns on his portfolios, at least for a few years.
Proposition 3: The speed with which an inefﬁciency is resolved will be directly related to how easily the scheme to exploit the inefﬁciency can be replicated by other investors. The ease with which a scheme can be replicated is
related to the time, resources, and information needed to execute it. Since very
few investors single-handedly possess the resources to eliminate an inefﬁciency
through trading, it is much more likely that an inefﬁciency will disappear
quickly if the scheme used to exploit the inefﬁciency is transparent and can be
copied by other investors.
To illustrate this point, assume that stocks are consistently found to earn excess
returns in the month following a stock split. Since ﬁrms announce stock splits publicly and any investor can buy stocks right after these splits, it would be surprising
if this inefﬁciency persisted over time. This can be contrasted with the excess returns made by some arbitrage funds in index arbitrage, where index futures are
bought (or sold), and stocks in the index are sold short or (bought). This strategy
requires that investors be able to obtain information on the index and spot prices
instantaneously, have the capacity (in terms of margin requirements and resources)
to trade index futures and to sell short on stocks, and to have the resources to take
and hold very large positions until the arbitrage unwinds. Consequently, inefﬁciencies in index futures pricing are likely to persist at least for the most efﬁcient arbitrageurs, with the lowest execution costs and the speediest execution times.
Propositions about Market Efﬁciency
115
