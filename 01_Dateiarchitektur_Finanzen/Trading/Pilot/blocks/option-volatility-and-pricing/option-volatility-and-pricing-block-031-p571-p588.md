# Option Volatility and Pricing_ Advanced Trading Strategies -- Sheldon Natenberg -- 2nd ed, 2014 -- McGraw Hill Professional -- isbn13 9780071818773 -- 6a48d008bd9beef283debf7bad0b2e4a -- Anna’s Archive.pdf — pages 571–588

--- page 571 ---

554
B
Some Useful Math
The mathematical functions and calculations referred to in this text are
included in almost all commonly used spreadsheets, and for most traders,
it is not necessary to know exactly how the calculations are made. Of far
greater importance is the ability to interpret the numbers that result from
the calculations.
For the reader who is interested, a detailed discussion of these mathematical concepts can be found in any good statistics or finance textbook. For convenience, we include an overview of these concepts and applications.
Rate-of-Return Calculations
An interest rate is the most common rate of return. The total interest can be
computed in three ways: simple, compound, and continuous. If

r = annual interest rate

t = time to maturity, in years

n = number of compounding periods per year

PV = present value of an investment

FV = future value of an investment

ln(x) = natural logarithm

ex = exp(x) = exponential function [(note that the natural
exponential function and natural logarithm are inverses,
that is, ln(ex) = eln(x) = x)]
then, for simple interest,

FV = PV × (1 + r × t)

PV = FV/(1 + r × t)

r = (FV/PV – 1)/t

t = (FV/PV – 1)/r
--- page 572 ---

S o m e U s e f u l M at h 	 555
for compound interest,

FV = PV × (1 + r × t)nt

PV = FV/(1 + r/n)nt = FV × (1 + r/n)–nt

r = [(FV/PV)1/nt – 1] × n

t = [ln(FV/PV)/ln(1 + r/n)]/n
and for continuous interest,

FV = PV × ert

PV = FV/ert = FV × e–rt

r = ln(FV/PV)/t

t = ln(FV/PV)/r
Because volatility is a continuously compounded rate of return, we can use
the exponential and logarithmic functions to do similar calculations for volatility. If

t = time to expiration, in years

F = a forward price after the period of time t

σ = annual volatility or standard deviation

X = an option’s exercise price
then a price range of n standard deviations is

F × e–nσ√t (down n standard deviations)

F × enσ√t (up n standard deviations)
The number of standard deviations required to reach an exercise price is
ln(X/F)/σ√t
Normal Distributions and Standard Deviation
If

xi = each data point

n = number of data points

σ = standard deviation or volatility

µ = average or mean
then the mean or average µ is
n
x
1
i
i
n
1∑
µ =
=
When calculating the standard deviation from the entire population, σ is
given by
n
x
1
(
)
i
i
n
2
1∑
σ
µ
=
−
=
--- page 573 ---

556
O P T I O N V O L AT I L I T Y A N D P R I C I N G
When estimating the standard deviation from a sample of the entire population, σ is given by1
n
x
1
1
(
)
i
i
n
2
1∑
σ
µ
=
−
−
=
The normal distribution curve n(x) is given by
n x
e
( )
1
2
x(
) /2
2
2
σ
π
=
µ
σ
−
−
In a standard normal distribution, µ = 0 and σ = 1.
Many of the measures associated with a distribution are derived from a
group of numbers called moments. In general, the jth moment mj about the mean
µ of a distribution is given by2
m
n
x
1
(
)
j
i
j
i
n
1∑
µ
=
−
=
From the second, third, and fourth moments, we can calculate the skewness and kurtosis of a distribution
m
m
m
m
m
Skewness
Kurtosis
3
2
2
4
2
2
=
=
A perfectly normal distribution has a skewness of 0 and a kurtosis of 3. To
normalize the kurtosis such that a normal distribution has a kurtosis of 0, it is
common to subtract 3
m
m
Kurtosis
3
4
2
2
=
−
Figure B-1 shows calculation of the mean and standard deviation for the
pinball distribution in Figure 6-2. The steps required to calculate the skewness and kurtosis would require an inordinate amount of space. However, the
relevant values, including the first three moments, are

m2 = 9.0291  m3 = 1.1095  m4 = 222.7640

Skewness = 1.1095/(9.0291 × √9.0291) = +0.0409
(The right tail of the distribution is very slightly longer than the left tail.)
Kurtosis = (222.7640/9.02912) – 3 = –0.2675
(The peak of the distribution is slightly lower and the tails slightly shorter than
a true normal distribution.)
1 The sample standard deviation is sometimes denoted with s (instead of σ).
2 In the same way we calculate a sample standard deviation by dividing by n – 1, we can also calculate sample
moments by dividing by n – 1 rather than dividing by n.
--- page 574 ---

S o m e U s e f u l M at h 	 557
Volatility
Volatility is usually calculated as a sample standard deviation. It is also common to assume a mean of 0. The estimated annualized volatility is then
given by
n
x
t
1
1
(
)
i
i
n
2
1∑
σ =
−
=
where xi = ln(pn/pn–1) = natural logarithm of the current price pn divided
by the previous price pn–1
 and t = the time interval, in years, between price
changes.
If the underlying contract is a stock, in theory, the price returns xi should
be adjusted to reflect the forward price of pn–1 over each time period. However, unless interest rates are very high or the stock will pay a dividend, using
the actual price rather than the forward price is unlikely to significantly alter
the results.
The volatility calculation for the stock option example in Figure 8-1 is
shown in Figure B-2. Because price changes were observed at seven-day intervals (t = 7/365), to annualize the volatility, it was necessary to divide by
√7/365. The calculation represents the population standard deviation (dividing by n rather than n – 1) and is based on the actual mean of the price changes.
Figure B-1  Calculation of the mean and standard deviation for the distribution in Figure 6-2.
Number of
occurrences
Trough
number
Total
value
0
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
11
12
13
14
15
0
2
2
4
5
6
9
10
11
9
7
5
3
2
1
1
77
0
2
4
12
20
30
54
70
88
81
70
55
36
26
14
15
577
Mean = 577/77 = 7.4935
Deviation
from the
mean
Deviation
squared
Deviation
squared
times
occurrences
–7.4935
–6.4935
–5.4935
–4.4935
–3.4935
–2.4935
–1.4935
–0.4935
+0.5065
+1.5065
+2.5065
+3.5065
+4.5065
+5.5065
+6.5065
+7.5065
56.1525
42.1655
30.1785
20.1915
12.2045
6.2175
2.2305
0.2435
0.2565
2.2695
6.2825
12.2955
20.3085
30.3215
42.3345
56.3475
0
84.3310
60.3570
80.7660
61.0225
37.3050
20.0745
2.4350
2.8215
20.4255
43.9775
61.4775
60.9255
60.6430
42.3345
56.3475
695.2440
--- page 575 ---

558
O P T I O N V O L AT I L I T Y A N D P R I C I N G
We might also calculate the volatility assuming a 0 mean or use an estimated
standard deviation. The various results are as follows:

Population standard deviation, actual mean:
37.62%

Population standard deviation, 0 mean:
37.88%

Estimated standard deviation, actual mean
39.65%

Estimated standard deviation, 0 mean:
39.93%
There is very little difference between the calculations made from the actual
mean and a 0 mean. The estimated standard deviation is always greater than
the population standard deviation.
Figure B-2  Volatility calculation for the stock option example in Figure 8-1.
Stock
price
Logarithmic
return
Deviation
from mean
Deviation
squared
97.70
99.50
+.018256
+.012152
.000148
92.75
−.070250
−.076355
.005830
95.85
+.032877
+.026773
.000717
96.20
+.003645
−.002460
.000006
102.45
+.062946
+.056842
.003231
93.30
−.093555
−.099660
.009932
91.15
−.023314
−.029419
.000865
95.20
+.043473
+.037369
.001396
102.80
+.076805
+.070701
.004999
103.85
+.010162
+.004058
.000016
Sum of
the returns
Sum of the squared
deviations
+.061045
.027140
mean return = .006105
Annualized
volatility
=
(.027140/10)/ 7/365
= .052096/.138485
= .3762 (37.62%)
--- page 576 ---

559
Index
Adjusted delta, 499
Adjustments
in Black-Scholes model, 348
dynamic hedging with, 121–122
to original hedge, 123
risks and neutral, 246
to spread, 246–248
trader choices for, 247–248
in volatility spreads, 206–208
All or none (AON), 539
American option, 32, 292, 539
arbitrage boundaries for, 293–295, 300
binomial tree and, 370–371
Black-Scholes model not for, 309, 377
delta values in, 313
dividend-paying stocks and, 373–376
European option compared to, 315–317
evaluating, 314
pricing of, 309–317
AON. See All or none
Approximations, ,
for put-call-parity, 271-273
for Black-Scholes value, 350-352
Arbitrage, 19–21, 265–266, 539
boundaries, 293–299, 300
free, 59, 60
index, 452–454, 545
relationships, 291
risk, 273–290
ARCH. See Autoregressive conditional
heteroskedasticity
Asian option. See Average price option
Ask price, 66
Assignment, 29–30, 539
At the forward, 60, 539
At the money, 33–35, 93
bull and bear strategies and, 222–226
delta, 136
gamma, 149–150
straddles, 477
theta, 141
vega, 145–146
Automatic exercise, 35–36, 539
Autoregressive conditional
heteroskedasticity (ARCH), 394
Average price option, 540
Bachelier, Louis, 61–62, 76
Backspread, 179, 540
Backward, 14, 524–526, 530, 540
Balanced skew, 487
Barone-Adesi, Giovanni, 309
Barone-Adesi-Whaley model, 309–310
Barrier option, 540
Bear spread, 222–226, 540
Bermuda option, 540
Bias, in futures market, 457–458
Bid price, 66
Bid-ask spread, 251–252, 427–428, 485
Binary option, 540
Binomial expansion, 361
Binomial model. See Cox-Ross-Rubinstein
model
Binomial notation, 363-365
Binomial option pricing, 358
Binomial tree, 359–360
American options and, 370–371
Black-Scholes model values in, 379
call value, 364
dividend-paying stock and, 374–375
with dividends, 372
notation for, 363–365
one-period, 360–361
periods used in, 378
recombining, 368
Black, Fischer, 57, 61, 62
Blackout period, 304
Black-Scholes model, 61–68, 120
approximations of, 350–352
binomial values in, 379
--- page 577 ---

560
I N D E X
Black-Scholes model (continued )
continuous diffusion process assumed
in, 472
as continuous-time model, 84
delta in, 352–354
dividends in, 67–68
equation, 339–340
as European pricing model, 309, 377
formulae, 349–350
gamma and vega in, 354–357
implied volatility in, 130–131, 307
interest rates in, 66–67
jump-diffusion model variation of, 475
lognormal distribution assumptions in,
85, 341–344, 506
not for American options, 309, 377
out of the money options and, 470–471
as probabilistic model, 471
put-call parity in, 340–341
theoretical values calculated with, 63
theta of, 354
time to expiration in, 65–66
underlying price in, 66, 345–346
variations, 62
volatility in, 68, 339
Black-Scholes-Merton model, 338
BMX. See Chicago Board Options
Exchange BuyWrite Index
Body of butterfly, 192
Bonds and notes, 17
Borrowing costs rbc, 24
Box, 280–282, 540
Breakeven prices, 51
Breakeven volatility, 116–117, 130
Broad based stock indexes, 441–442
Bull and bear butterfly, 211–212
Bull and bear calendar spread, 212–214
Bull and bear ratio spread, 210–211, 213
Bull and bear vertical spread, 215–217
Bull spread, 222–226, 540
Bull straddle, 171
Bund futures, 388, 390
Butterfly, 289, 506–507, 540
bull and bear, 211–212
call or put, 290
iron, 260–262, 290, 545
and implied distributions, 508
long, 174–175, 201
short, 174–175, 201
time, 191–192
Buying, 284, 287
Buy/write, 326–327, 540
Cabinet bid, 420, 540
Calendar spread, 195, 237, 239–240, 540
bull and bear, 212–214
implied volatility and, 405–408
long and short, 189–190, 204, 214
rolls and, 284–286
Call
butterfly, 290
Christmas tree, 183, 203
covered, 486
delta, 137, 139
lambda and, 154–156
option, 3, 26, 299–302, 540–541
protective, 322–324
ratio spread, 179–181, 203
synthetics, 288, 551
theoretical value of, 101, 108–109, 111,
310–311
Cap, 322, 514, 540, 541
Capitalization, 443
Capitalization weighted index, 443, 454–456
Carry trade, 20
Cash, 1, 8, 31–32, 459–461, 461–462
Cash-and-carry arbitrage, 20
Cash-and-carry strategy, 159, 161
Cash-secured put, 327
Castelli, Charles, 61
CBOE. See Chicago Board Options
Exchange
CEV. See Constant elasticity of variance
model
Charm, 139–141, 541
Chicago Board Options Exchange
(CBOE), 62, 250, 309, 459, 515, 530
Chicago Board Options Exchange
BuyWrite Index (BXM), 327
Chicago Mercantile Exchange, 36, 67,
81, 452
Chooser option, 541
Christmas tree, 182–184, 203, 541
Circuit breakers, 464
Clearing firm, 11
Clearing member, 541
Clearinghouse, 10, 11, 541
Closing trade, 5
CME Clearing House, 10
Collar, 328–330, 541
Color, of option, 152–153, 541
Combination (Combo), 266, 541
Combo value, 266, 267
Commodity markets, 486
Companion option, 256, 259
--- page 578 ---

I n d e x 	 561
Complex positions, 45–46, 410–411,
420–423
Compound option, 541
Condor, 176–178, 541
Constant elasticity of variance (CEV)
model, 478
Contango, 14, 524–526, 530, 541
Contingency order, 208, 542
Continuous diffusion process, 471–472
Continuous-time model, 84
Contract specifications, 26–30
Convenience yield, 15
Conversion market, 267
Conversion, 265–266, 273, 275, 277–282,
289, 542
Counterparty, 10
Covered call, 486
Covered option, 329
Covered write, 61, 324–328, 542
Cox, John, 309, 358
Cox-Ross-Rubinstein model, 309–310
Crack spread, 163–164
Credit spread, 214
Curvature, 105–108
Cylinder. See Collars
DAX Index, 448
Debit spread, 214
Declared date, 22–23
Delta (∆), 64, 110, 492, 542
adjusted, 499
of American options, 313
in Black-Scholes model, 352–354
of bull spread, 218-219, 223
call, 137, 139
decay, 139
hedge ratio and, 102–103
implied, 136
at the money, 136
negative and positive, 416
position, 169
probability and, 104–106
put, 138
rate of change and, 100–102
theoretical underlying position and,
103–104
as volatility changes, 135–136
Delta (directional) risk, 227
Delta-neutral, 103, 121, 129–130, 133,
353–354, 421, 542
Derivative contracts, 4
Dermna, Emanuel, 57
Diagonal ratio spread, 236–237
Diagonal roll. See Time box
Diagonal spread, 196–200, 542
Diffusion process, 472–473
Digital option. See Binary option
Dividend play, 318
Dividend value, 300, 302
Dividend-paying stocks, 373–376
Dividends, 279, 373–379
binomial tree with, 372
in Black-Scholes model, 67–68
declared date of, 22–23
Dow Jones Industrial Average
paying, 452
ex-date of, 22–23, 68, 543
implied, 21, 273
payable date of, 23
record date of, 22
risk and, 239–240, 278–280
stock options influenced by, 100
calendar spreads and, 192–195
Divisor, 446–447
Dow Jones Industrial Average, 445, 452
Downside contract position, 418
Dragonfly, 504, 542
Driftless theta, 354
Dynamic hedging, 336, 474, 512, 542
with adjustments, 121–122
delta-neutral, 133
process of, 127–129
Early exercise, 292
of call option, 299–302
of future option, 305–307
protective value and, 308
of put option, 302–305
risk, 319–320
short stock impact on, 305
strategies, 317–319
Efficiency, 244–246, 542
Efficient-market hypothesis, 394
Elasticity, 154, 542. See also Lambda
Equal-weighted index, 444
Equilibrium price, 429
Equity portfolio, 457
Euro-bund options, 269
Eurocurrency, 81–82, 542
Eurocurrency rate, 543
European box, 314
European option, 32, 60, 62, 253, 292, 543
American option compared to, 315–317
arbitrage boundaries for, 293–299
--- page 579 ---

562
I N D E X
Forward conversion. See Conversion
Forward price, 2–3, 12–17, 76–77,
270–271, 543
Forward rate, 16, 408
Forward start option, 544
Forward volatility, 404–409
Forward-rate agreement (FRA), 16
Free float, 445
Frequency distribution, 480–481
Frictionless markets, 125–126, 463–466
Front spread, 182, 544
FTSE 100 index, 485
Fugit, 307, 544
Future volatility, 394–397
Futures contract, 2, 544
early exercise of, 305–307
locked markets, 269–270
notional value, 455
option’s difference with, 26–27
options on, 267–269
on stock index, 450–451
synthetics, 270, 277
Futures exchange, 2
Futures market, 457–458, 464
Futures option, 19, 30–31
Futures-type settlement, 7–9, 36, 112, 544
Gamma (Γ), 110, 113, 152, 544
in Black-Scholes model, 354–357
of bull spreads, 223
influence of expiration and volatility,
150–151
magnitude risk measured by, 115–116
at the money, 149–150
negative and positive, 106–107, 230,
414–418, 421
options, 154, 367
as option’s curvature, 105–108
rent, 369–370
spread, 165
theta tradeoff with, 237
underlying price changes and, 149–150
Gamma (curvature) risk, 227–228
Gamma spread, 165
Gaps, real world, 476
GARCH. See Generalized Autoregressive
conditional heteroskedasticity
Garman, Mark, 62, 385
Garman-Klass estimators, 385
Garman-Kohlhagen model, 62, 67
Generalized Autoregressive conditional
heteroskedasticity (GARCH), 394
European option (continued )
arbitrage relationships for, 291
Black-Scholes model pricing of, 309, 377
dividend-paying stocks and, 373
European pricing model, 309, 377
EuroStoxx 50 Index, 385–386, 402, 405, 407
EWMA. See Exponentially weighted
moving average
Exchange option, 543
Exchanges, 6–9, 449, 464
Exchange-traded contracts, 10, 160
Exchange-traded funds, 454
Exchange-traded options, 29
Ex-dividend date (Ex-date), 22–23, 68, 543
Execution risk, 273–274
Exercise, 29–30, 543
Exercise notice, 35
Exercise price, 4, 29, 65, 215, 543
Exotic option, 182, 543
Expected value, 53–54, 59–60
Expiration date, 2, 4, 28–29, 65–66, 73, 543
Expiration straddle, 476–477
Expiry. See Expiration date
Exponentially weighted moving average
(EWMA), 393–394
Extreme-value method, 384
Extrinsic value. See Time value
Fair value. See Theoretical value
Fear index, 523
Fence. See Collars
Figlewski, Stephen, 57
Fill or kill (FOK), 208, 543
Fixed-income markets, 161–162
Flat peak (platykurtic), 481
Flat skew, 487
Flex option, 27, 543
Floating skew, 489, 490
Floor, 322–323, 543
FOK. See Fill or kill
Forecasting, volatility, 391–394
Foreign currencies, 17–18
Foreign currency options, 99
Forward contract, 2, 543
basis, 13
fair price for, 12–14
for foreign currency, 17–18
interest rate risk, 21
long-term, 452
notional value, 6
stock index, 455
synthetics, 254
--- page 580 ---

I n d e x 	 563
option pricing compared with, 90–91
reevaluation of, 131
relative changes in, 400
sensitivity to changes in, 425–426
term structure of, 397–404, 430–432
time decay and, 380–381
In price, 544
In the money, 33–35, 92, 545
Index
arbitrage, 452–454, 545
broad based stock, 441–442
calculation, 443–445
capitalization-weighted, 443, 454–456
divisor, 446–447
equal-weighted, 444
fear, 523
geometric-weighted, 445
impact of individual stock price changes,
448–450
narrow based stock, 441–442
price-weighted, 443–445, 449, 454–455
rebalancing, 445
replicating, 454–456
total-return, 447–448
volume-weighted average price, 450
In-option, 544
In-price, 544
Insurance policies, 4, 321
Interest, 5, 123–124, 239–240, 278–280,
303, 318–319
Interest rates, 228
in Black-Scholes model, 66–67
foreign currency options and, 99
forward contract and risks of, 21
implied, 21, 273
negative, 83
option values influenced by, 97–100,
466-467
products volatility of, 81–82
stock options importance of, 305–306,
466–467
in theoretical pricing models, 126
theoretical value and, 467
volatility spreads with dividends and,
192–195
Interest-rate value, 300
Intermarket spreads, 161–162, 545
Intrinsic value, 32–34, 38–40, 299–300, 545
Investment skew, 486–487
IOC. See Immediate or cancel
Iron butterfly, 260–262, 290, 545
Iron condor, 262–263, 545
Geometric-weighted index, 445
Go long or short, 5
Gold, 93–96, 384, 387, 389
Good ‘til canceled (GTC), 544
Greeks, 99
GTC. See Good ‘til canceled
Guts, 172, 544
Haircut, 8, 544
Half-steps, 378
Hedge ratio. See Delta (∆)
Hedgers, 321, 544
Hedging
collars used in, 328–330
complex strategies in, 331–333
covered-writes used in, 324–328
high and low implied volatility in, 331
natural long or short in, 321
protective calls and puts in, 322–324
stock index futures and, 457
strategy summary of, 330
using vertical spreads, 332–333
using volatility spreads, 332
volatility contracts used for, 536
volatility reduced by, 333–334
Higher-order risk measures, 355
Historical volatility, 381–386, 392
of Bund futures, 388, 390
of EuroStoxx 50, 386, 402
of gold, 93–96, 384, 389
of S&P 500 Index, 87, 383, 389
Hockey-stick diagrams, 40
Horizontal spread. See Calendar spread
Illiquid market, 66
Immediate or cancel (IOC), 544
Implied delta, 136
Implied distribution, 506–510
Implied dividend, 21, 273
Implied interest rates, 21, 273
Implied spot price, 21
Implied volatility, 88–89, 92–95, 116, 199, 544
assessing risk of, 401
in Black-Scholes model, 130–131, 307
calendar spread and, 405–408
contracts, 512, 514–523
defining, 514
EuroStoxx 50 and, 407
floating skews as, 490
future volatility predicted by, 394–397
hedging with high and low, 331
influence of, 188–189
--- page 581 ---

564
I N D E X
strangle, 172–173, 201, 262
synthetic, 253, 260–261
time butterfly, 193
Long-term Equity Anticipation Security
(LEAP), 545
Long-term options, 27–28
Lookback option, 546
Magnitude risk, 115–116
Margin and variation settlement, 7
Margin deposit, 7
Margin of error, 239, 240–244
Margins, 8, 546
Market conditions
market making and, 429–430
option traders and changes in, 139–140
option values influenced by, 97–98
positions influenced by, 435–436
risk analysis and changes in, 434–435, 437
risk and, 413, 415–416
stock splits and, 438–440
theoretical edge and, 231
Market integrity, 10–11
Market liquidity, 235
Market maker, 427–430, 432–433, 546
Market order, 208, 546
Market-if-touched (MIT), 546
Market-on-close (MOC), 453, 546
Markets, 126, 165–166
commodity, 486
declining, 426–427
fixed-income, 161–162
frictionless, 463–466
futures contracts and locked, 23,
269–270, 546
option position in, 64
option traders and speed of, 53
volatility measuring speed of, 69
Mark-to-market, 546
Married put, 547
Maturity date. See expiration date
Mean, 73–77, 345
Mean reverting, 387–388, 398
Median, 345
Merton, Robert, 62, 338
Mid-Atlantic option. See Bermuda option
Midcurve options, 28, 547
MIT. See Market-if-touched
MOC. See Market-on-close
Models. See specific model
Modes, 84, 345
Moneyness, 491
Jelly roll. See Roll
Jump process, 472, 473
Jump-diffusion model, 475, 478
Jump-diffusion process, 472, 473
Kansas City Board of Trade, 452
Kappa (Κ), 110, 545
Klass, Michael, 385
Knock-in option. See In-option
Knock-out option. See Out-option
Kohlhagen, Steven, 62
Kurtosis, 481–483, 495–498, 501–506, 555
Ladder, 545. See also Christmas tree
Lambda (Λ), 154–156. See also Elasticity
Last trading day, 28
LEAP. See Long-term Equity Anticipation
Security
Leg, 163–164, 545
Leverage value. See Elasticity
LIBOR. See London Interbank
Offered Rate
Limit, 546
Limit order, 208, 546
Liquid market, 66
Liquidity, 249–250, 427
Local, 546
Locked limit, 23
Locked markets, 23, 546
Lognormal distributions, 82–83
Black-Scholes model and assumptions of,
85, 341–344, 506
butterflies with, 508
price changes in, 84
standard deviations and, 346–348
of underlying price, 478–481
London Interbank Offered Rate (LIBOR),
67, 81
Long, 54, 321, 477
butterfly, 174–175, 201
calendar spread, 189–190, 204, 214
call, 38, 42–43
call Christmas tree, 183, 204
condor, 177–178, 202
natural, 321
position, 5, 98, 328, 546
premium, 197, 546
put, 39, 42–43
put Christmas tree, 184, 203
rate rl, 24
ratio spread, 546
straddle, 170–171, 205
--- page 582 ---

I n d e x 	 565
Paralysis through analysis, 118
Parity. See Intrinsic value
Parity graphs, 38–51
Parkinson, Michael, 384
Partial derivatives, 100
Path dependent, 471
Phi (Φ), 112
Physical commodities, 2, 14–15
Physical settlement, 7–8
Physical underlying, 30–31
Pin risk, 274–275
P&L. See Profit and loss
Plain-vanilla-interest-rate swap, 5
Population standard deviation, 382
Portfolio insurance, 335–337
Portfolio manager, 333–334, 336, 537
Positive dividend risk, 279
Positive gamma position, 106–107, 415
Premium, 4
Price changes, 479
individual stock, 448–450
in lognormal distributions, 84
underlying, 141–142, 145–146,
149–150
volatility and observed, 80–81
Price distribution, 73
Price movement, 65, 72–75
Price volatility, 82
Price weighted index, 443–445, 449,
454–455
Pricing, of American options,
309–317
Pricing models, 62, 338–339
American, 309
entering skew into, 489–494
European, 309, 377
volatility skew in, 499
weaknesses, 484–485
Probabilistic model, 471
Probabilities, 4, 376, 483
delta and, 104–106
expected value, 53–54, 59–60
models and, 56–57
symmetrical distribution of, 60
theoretical values in, 54–56
Probability functions, 344
Profit and loss (P&L), 46–51, 124, 125, 133
Program trading, 453
Protective options, 323–324, 327, 329
Protective put, 486
Protective value, 308
Pseudoprobabilities, 376
Naked position, 164, 209, 547
Narrow based stock index, 441–442
Natural gas futures, 403–404
Natural longs and shorts, 321
Negative dividend risk, 279
Negative gamma position, 106–107, 230,
414–418, 421
Negative interest rates, 83
Negative theoretical edge, 118
Negative time value, 109–110
Negative vega, 230, 236
Negative volga, 236
Net contract position, 417
Neutral hedge. See Riskless hedge
Neutral spread, 210, 547
New York Mercantile Exchange, 29
Nominal value. See notional value
Nonsymmetrical strategies, 185
Normal distribution, 69–73, 75–77,
480–481, 554–556
Not held, 209, 547
Notional value, 6, 455
Notional vega, 513
OBO. See Order book official
OCO. See One-cancels-the-other
OEX. See Options Exchange Index
Omega (Ω), 154, 547
One-cancels-the-other (OCO),
209, 547
Open interest, 5
Open position, 5
Opening trade, 5
Option pricing, 32–36, 62, 90–91,
338–339, 358
Option replication. See Portfolio insurance
Option risk analysis, 116
Option-pricing theory, 119
Options Clearing Corporation, 10, 36
Options Exchange Index (OEX),
459, 515
Order book official (OBO), 547
Orders, submitting spread, 208–209
OTC. See Over-the-counter market
Out of the money, 33–35, 93, 135–136,
419–420, 423, 470–471, 547
Outliers, 481
Out-option, 547
Out-price, 547
Out-trade, 547
Over-the-counter (OTC) market, 19
Overwrite, 324, 547
--- page 583 ---

566
I N D E X
magnitude, 115–116
management, 97–100, 135
margin for error in, 239
negative and positive dividend, 279
neutral adjustments, 246
pin, 274–275
rho (interest-rate), 228
rolls and, 282–285
settlement, 276–278
spreading strategies and, 161, 166–168
in stock options, 240
strategies and considerations of, 234, 238
theoretical pricing models and types
of, 463
theta (time decay), 228
time boxes and, 285–287
vega (volatility), 228
volatility, 228–234
Risk measures, 99
higher-order, 355
interpreting, 112–118
skewed, 498–499
stock splits and, 439–440
traditional and nontraditional,
156–157
Risk reversal, 502, 549
Risk-analysis process, 432
Risk-free rate, 67
Riskless hedge, 63–64, 102
Risk-neutral world, 358–360
Risk-reward tradeoff, 40, 97, 176, 244
Roll, 282–286, 549
Ross, Stephen, 358
Rubinstein, Mark, 358
Sample standard deviation, 382
Scalper, 158, 549
Scholes, Myron, 61,62,338
Second-generation option. See Exotic option
Sell stock short, 23
Serial correlated, 386
Serial options, 27, 549
Settlement
in to cash, 31–32
dates, 22
in to a futures position, 30–31
futures-type, 7–9, 36, 112, 544
margin and variation, 7
options and types of, 36
physical, 7–8
in to the physical underlying, 30–31
procedures, 6–9
Put
butterfly, 290
cash-secured, 327
Christmas tree, 184, 203
delta, 138
lambda and, 154–156
long, 39, 42–43
married, 547
option, 4, 26, 302–305
protective, 322–324, 486
ratio spread, 179–181, 204
short, 40
short Christmas tree, 184
synthetics, 261–262, 551
theoretical value of, 101–102, 108–109,
111, 312
Put-call parity, 267–268, 462
in Black-Scholes model, 340–341
for stock options, 270–273, 288
synthetic futures contract and, 270
Quadratic model. See Barone-Adesi-
Whaley model
Random walk, 69–73, 471
Rate of return, 82, 553–554
Ratio spread, 179–182, 202, 210–211, 213,
236–237, 546, 549
Ratio straddle, 171
Ratio strategy, 162
Ratio write, 332
Realized profit, 7
Realized volatility, 86–87, 116, 512–514
Rebalancing process, 537
Recombining binomial tree, 368
Record date, 22
Rehedging, 129, 367
Reversal, 273, 275, 277–282, 502, 549
Reverse conversion, 265, 268, 278–279, 289
Rho (Ρ), 111–112, 113, 467, 549
Rho (interest-rate) risk, 228
Risk, 21, 273–274
analysis, 434–435, 437
arbitrage, 273–290
boxes, 280–282
complex positions, 422–423
delta (directional), 227
dividends and interest, 239–240, 278–280
early exercise, 319–320
gamma (curvature), 227–228
gamma spreads and, 236–237
interest and, 239–240, 278–280
--- page 584 ---

I n d e x 	 567
Spread, 158, 550
adjustments to, 246–248
bear, 222–226, 540
bid-ask, 251–252
bull, 222–226, 540
common features of, 169
credit and debit, 214
diagonal, 196–200, 542
diagonal ratio, 236–237
dynamic hedging and, 165
efficiency of, 244–246
front, 182, 544
for futures contracts, 160–161
gamma, 165
gamma risk of, 236–237
intermarket and intramarket, 161–162
liquidity in, 249–250
with negative vega, 230
static, 165
submitting order for, 208–209
theoretical value and deltas in, 218–219
trader buying, 164
trading style and, 248–249
volatility characteristics and, 233–234
Spreading strategies
defining, 159–164
futures contracts using, 160–161
in options markets, 165–166
risk controlled by, 166–168
risks reduced through, 161
synthetics used in, 259–260
Standard cumulative normal distribution
function, 344
Standard deviation
Black-Scholes model, 344–346
calculating, 382
lognormal distributions and, 346–348
mean and, 73–76
normal distribution and, 554–556
price movement and, 74–75
sample and population, 382
volatility as, 77–78
weekly, 79
Standard Portfolio Analysis of Risk
(SPAN), 36
Static hedge, 121
Static spread, 165
Sticky-delta skew, 492
Sticky-strike skew, 489
Stock index
broad and narrow based, 441–442
forward contract, 455
risk, 276–278
stock-type, 7–9, 36, 268, 316,
318–319, 550
Sharpe, William, 334
Sharpe ratio, 334
Short, 5
butterfly, 174–175, 201
calendar spread, 189–190, 204, 214
call, 39
call Christmas tree, 183, 203
collars, 330
condor, 177–178, 202
natural long or, 321
position, 5, 98, 328, 549
premium, 197, 549
put, 40
put Christmas tree, 184, 203
sales, 23–25
sell stock, 23
squeeze, 23, 195, 549
stock, 98, 305
straddle, 170–171, 201
strangle, 172–173, 201, 262
Short rate rs, 24
Short ratio spread, 549
Short-stock rebate, 24
Short-stock squeeze, 23, 195, 549
Short-term options, 27–28
Sigma (σ), 77, 549
Skew
balanced, 487
flat, 487
floating, 489, 490
investment, 486–487
model input of, 498
modeling , 489–494
risk measures and, 498–499
sticky-delta, 492
sticky-strike, 489
volatility, 485–486, 532, 552
Skewness, 481–482, 495–498, 501–506, 555
Slope, in parity graphs, 40–46
S&P 500 Index, 250, 327, 448, 478–479,
482, 515
historical volatility, 87, 383, 389
SPAN. See Standard Portfolio Analysis of Risk
Special opening rotation, 520
Specialist, 549–550
Speculator, 53, 131, 321, 410, 428, 550
Speed, 150–151, 550
Split-strike conversion, 328, 550. See also
Risk reversal
--- page 585 ---

568
I N D E X
contract types, 258
forward contract, 254
futures contract, 270, 277
long straddles, 260–261
long underlying, 253
options, 255–260
put, 261–262, 551
relationships, 267
short position, 264–265
spreading strategies using, 259–260
underlying, 253–255, 551
volatility spread using, 287–290
Tailing, 277
Tall peak (leptokurtic ), 481
Tau (τ), 551
Taxes, 127, 465
Term structure, 390, 397–405, 430–432,
551
Theoretical edge, 118, 227
margin of error and, 240–244
market conditions and, 231
market liquidity and, 235
Theoretical pricing models
basic inputs in, 335
diffusion process assumed in, 472–473
interest rates in, 126
performance of, 119–121
problems with, 56–57
risk types in, 463
underlying price in, 66
understanding and having faith in, 538
volatility in, 80, 89–90, 204, 206, 380
weaknesses in, 511–512
Theoretical value, 142–143, 551
Black-Scholes model calculating, 63
of call, 101, 108–109, 111, 310–311
in dynamic hedging, 133–134
of futures contract, 316
interest rates and, 467
of options, 55, 58
and probability, 54–56
of put, 101–102, 108–109, 111, 312
of underlying contract, 115
volatility changes and, 146–147
“The Theory of Options in Stocks and
Shares,” 61
The Theory of Speculation (Bachelier), 61–62
Theta (Θ), 113, 142–143, 551
of Black-Scholes model, 354
of bull spreads, 224–225
driftless, 354
Stock index (continued )
futures, 458–459
futures contract on, 450–451
hedging and futures in, 457
implied distribution of, 509
options, 458–462
Stock options, 19
dividends influencing, 100
interest rates important in, 305–306,
466–467
long and short positions , 98
physical underlying and, 30–31
put-call parity for, 270–273, 288
Stock splits, 438–440
Stocks
dividend-paying, 373–376
forward price for, 15–17
Index impacted by price changes in,
448–450
Stock-type settlement, 7–9, 36, 268, 316,
318–319, 550
Stop (loss) order, 209, 550
Stop-limit order, 209, 550
Straddles, 61, 170–171, 205, 238, 474, 550
buying, 287
delta neutral and, 353–354
expiration, 476–477
at the money, 477
synthetics and, 260–261
Strangles, 171–173, 238, 261, 550
Strap, 550
Strategies
bull and bear, 222–226
buy/write, 326–327, 540
cash-and-carry, 159, 161
choosing appropriate, 199–206
complex hedging, 331–333
early exercise, 317–319
efficiency of, 244–246
hedging summary of, 330
nonsymmetrical, 185
ratio, 162
risk considerations in, 234, 238
skewness and kurtosis, 501–506
symmetrical, 178
Strike price. See Exercise price
Strip, 519, 534–536, 550
Swap, 5, 550
Swaption, 550
Symmetrical strategies, 178
Synthetics, 287–290, 550
call, 288, 551
--- page 586 ---

I n d e x 	 569
of bull spreads, 224
decay, 147, 149, 356–357, 552
at the money, 145–146
negative, 230, 236
neutral, 399
notional, 513
as time passes, 147–148
underlying price changes and, 145–146
volatility changes influencing, 146–147
Vega (volatility) risk, 228
Vertical spread, 213–226, 329, 332–333, 552
VIX. See Volatility index
Volatility, 552
in Black-Scholes model, 68, 339
breakeven, 116–117, 130
calculating, 556–557
delta and changes in, 135–136
forecast, 87
forecasting, 391–394
forward, 404–409
future, 394–397
gamma and changes in, 150–151
hedging to reduce, 333–334
implied, 88–95, 512
interpreting data on, 85–95
in-the-money options and, 92
mean reverting, 387–388
observed price changes and, 80–81
realized, 86–87, 116, 512
rising and falling, 468–469
risk, 228–234
scaled for time, 78–79
shifting, 500–501
smirk, 485
as speed of market, 69
as standard deviation, 77–78
surface, 499
term structure of, 390
in theoretical pricing models, 80, 89–90,
204, 206, 380
theoretical value and changes in, 146–147
theta and changes in, 144–145
underlying contract price and, 478
value, 299, 304
vega and changes in, 146–147
Volatility contracts, 512–514
applications, 536–537
replicating, 534–536
used for hedging, 536
Volatility index (VIX), 515–519
characteristics of, 520–523
futures, 524–529
gamma tradeoff with, 237
at the money, 141
negative time value and, 109–110
of options, 367–368
positive, 417
as time decay, 108–109
underlying price changes and, 141–142
volatility changes and, 144–145
Theta (time decay) risk, 228
Three-way, 280, 551
Ticker symbols, 460
Time, volatility scaled for, 78–79
Time box, 285–287, 551
Time butterfly, 191–192
Time decay, 108–109, 380–381
Time premium, 33, 551
Time spreads. See Calendar spread
Time value, 32, 33–34, 543, 551
Time-series analysis, 393
Total-return index, 447–448
Trading, exchanges halting, 449, 464
Transaction costs, 126–127, 129
Type, 6, 551
Underlying, 4, 27-28,551
Underlying contract, 439
synthetic options and, 255–260
synthetic short position and, 264–265
theoretical value of, 115
volatility independent of price of, 478
Underlying position, 41–43, 103–104
Underlying price
in Black-Scholes model, 66, 345–346
cash index option and, 461–462
exercise price and, 49–51
gamma and changes in, 149–150
lognormal distribution of, 478–481
option value and, 37–38
in theoretical pricing models, 66
theta and changes in, 141–142
vega and changes in, 145–146
Unrealized profits, 7
Upside contract position, 419,
Value Line  Index, 452
Vanilla option, 551
Vanna, 139, 140, 146, 551
Variance contract, 513
Variance swap, 513
Variation, 8, 551
Vega, 110, 113, 116, 552
in Black-Scholes model, 354–357
--- page 587 ---

570
I N D E X
synthetics used in, 287–290
time butterfly, 191–192
Volga, 147–148, 552
Volume-weighted average price
(VWAP), 450
Vomma. See Volga
VWAP. See Volume-weighted average price
Warrant, 552
Wilmot, Paul, 57
Wings of butterfly, 192
Write, 325, 552
Yield volatility, 82
Zero-cost collar, 330, 552
Zero-mean assumptions, 382
Zomma, 152–154, 552
Volatility index (VIX) (continued )
options, 530–533
trading, 523–524
Volatility skew, 485–486, 532, 552
Volatility smile. See Volatility skew
Volatility spread, 169
adjustments, 206–208
butterfly, 173–176
calendar spread, 182–191
Christmas tree, 182
condor, 176–178
diagonal spread, 196–199
hedgers using, 332
interest rates and dividends in, 192–195
ratio spread, 179–182
straddles, 170–171
strangle, 171–173
submitting an order, 208–209
--- page 588 ---

About the Author
Sheldon Natenberg began his trading career in 1982 as an independent
market maker in equity options at the Chicago Board Options Exchange.
From 1985 to 2000, he traded commodity options, also as an independent floor
trader, at the Chicago Board of Trade.
While continuing to trade, Mr. Natenberg has also become active as an educator. In this capacity, he has conducted seminars for option traders at major
exchanges and professional trading firms in the United States, Europe, and the
Far East. In 2000, Mr. Natenberg joined the education team at Chicago Trading Company, a proprietary derivatives trading firm.
