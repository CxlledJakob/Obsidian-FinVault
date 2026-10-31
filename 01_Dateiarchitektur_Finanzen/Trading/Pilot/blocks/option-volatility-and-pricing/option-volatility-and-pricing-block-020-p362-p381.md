# Option Volatility and Pricing_ Advanced Trading Strategies -- Sheldon Natenberg -- 2nd ed, 2014 -- McGraw Hill Professional -- isbn13 9780071818773 -- 6a48d008bd9beef283debf7bad0b2e4a -- Anna’s Archive.pdf — pages 362–381

--- page 362 ---

T h e B l a c k - S c h o l e s M o d e l 	 345
n(x ) and N(x )
Before continuing, it will be useful to define two important probability functions—n(x) and N(x). In this chapter and in previous discussions of volatility, we
have often referred to the concept of a bell-shaped, or normal, distribution.
Depending on the mean and standard deviation, there can be many different
normal distributions, but n(x), the standard normal distribution, is perhaps the most
common. It has a mean of 0 and a standard deviation of 1. The standard normal distribution, shown in Figure 18-2, also has one very useful characteristic:
the total area under the curve adds up to exactly 1. That is, the curve represents
100 percent of all occurrences that form a true normal distribution.
Although the standard normal distribution takes in 100 percent of all occurrences, we may want to know what percent of the occurrences fall within a
specific portion of the standard normal distribution. This is given by N(x), the
standard cumulative normal distribution function. If x is some number of standard
deviations, N(x) returns the probability of getting an occurrence less than x by
calculating the area under the standard normal distribution curve between the
values of –∞ and x, as shown in Figure 18-3. That is, N(x) tells us what percentage of all possible occurrences fall between –∞ and x. Obviously, N(+∞) must
be 1.00 because 100 percent of all occurrences must fall between –∞ and +∞.
And N(–∞) must be 0 because there can be no occurrences to the left of –∞. Because the normal distribution curve is symmetrical, with 50 percent of the occurrences falling to the left of 0 and 50 percent falling to the right, N(0) must
equal 0.50. It also follows that the area under the curve between –∞ and x must
be equal to the area under the curve between –x and +∞, resulting in this useful relationship
N(x) = 1 – N(–x)
Figure 18-2  n(x )—the standard normal distribution curve with mean = 0 and standard
deviation = 1.
0
Standard deviations
–1
–2
–3
+3
+2
+1
0
.1
.2
.3
.4
--- page 363 ---

346
O P T I O N V O L AT I L I T Y A N D P R I C I N G
The Black-Scholes model makes all calculations using the probabilities associated with a normal distribution. This may seem inconsistent with our assumption that the prices of an underlying contract are lognormally distributed
because a normal distribution and a lognormal distribution are clearly not the
same. However, by making some adjustments to the value of x, we can use N(x)
to generate probabilities associated with a lognormal distribution.
It will also be useful to define three numbers used to describe many common distributions:
Mode.  The peak of the distribution. The point at which the greatest number
of occurrences take place.
Mean.  The balance point of the distribution. The point at which half the
value of the occurrences fall to the left and half to the right.
Median.  The point at which half the occurrences fall to the left and half to
the right.
In a perfect normal distribution, all these points fall in the same place, exactly
in the middle of the distribution. But consider the distribution in Figure 18-1.
The mode, mean, and median of this distribution all fall at different points, as
shown in figure Figure 18-4. The mode is approximately 9.3, the mean is approximately 12.7, and the median is approximately 10.5. To make the appropriate adjustments to a lognormal distribution so that we can use the probabilities
associated with a normal distribution, we must locate these numbers.
The Black-Scholes model begins by defining the relationship between the
exercise price and the underlying price. In a normal distribution, this is simply
S – X, but in a lognormal distribution, the relationship is
S
X
ln



Figure 18-3  N(x )—the area under the standard normal distribution curve between –∞ and x.
+∞
–∞
–x
x
N(–∞) = 0
N(+∞) = 1
N(0) = .5
N(–x) = 1 – N(x)
N(–x)
0
--- page 364 ---

T h e B l a c k - S c h o l e s M o d e l 	 347
If S > X, this value is positive, and the call is in the money; if S < X, the value is
negative, and the call is out of the money.
Next, because options are valued off the forward price and the forward
price is a function of interest rates, we must adjust this relationship by the interest component over the life of the option rt. This gives us2
S
X
rt
ln


+
The number of standard deviations associated with an occurrence depends
on how far the occurrence is from the mean of the distribution. In a normal distribution, the mean, like the mode, is located in the exact center of the distribution. But in Figure 18-4, which approximates a lognormal distribution, with its
elongated right tail, we can see that the mean must be somewhere to the right of
the mode. How far to the right? This depends on the standard deviation of the
lognormal distribution. The higher the standard deviation, the longer  the right
tail, and consequently, the further to the right we must shift the mean. Mathematically, the shift is equal to σ2t/2. Adding this adjustment gives us
S
X
rt
t
ln
2
2
σ



+
+
2. We could in fact drop rt and at the same time replace S with its forward price Sert. The values are the same:
ln(S/X ) + rt = ln(Sert/X ).
Figure 18-4
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
10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27
Mean
(12.7)
Mode
(9.3)
Median
(10.5)
Mode:
The peak of the distribution
Mean:
The point where half the value (occurrences per trough multiplied by trough number) lies to

the left and half to the right
Median:
The point where half of all occurrences lies to the left and half to the right
--- page 365 ---

348
O P T I O N V O L AT I L I T Y A N D P R I C I N G
Combining the interest-rate and volatility components gives us the numerator
for d1
S
X
r
t
ln
2
2
σ



+
+




Finally, we must convert this value to some number of standard deviations.
If we know the value of one standard deviation, we can divide by this value to
determine the total number of standard deviations. In fact, we know that over
any time period t, one standard deviation is equal to
t
σ
. If we divide by this
value, the result, d1, tells us, in standard deviations, how far the exercise price is
from the mean when adjusted for a lognormal distribution
In the equation shown in Figure 18-5, the calculation of d1 may seem
somewhat complicated, but it is really just a collection of adjustments to the
exercise price and underlying price that enable us to use a cumulative normal
distribution function to calculate probabilities.
Once we have determined the value of d1, multiplying the forward price of the
stock by N(d1) gives us the average value of all stock above the exercise price at
expiration.
Figure 18-5
the relationship between
the underlying price and
the exercise price (how
much the option is inor out-of-the-money)
spot price to forward
price adjustment
(carry on the underlying)
adjustment for the mean
of a lognormal distribution
normalization factor (one standard
deviation) to determine the total
number of standard deviations
}
}
}
}
ln
r
t
+
+
)
(
d1 =
S
X
)
(
2
--- page 366 ---

T h e B l a c k - S c h o l e s M o d e l 	 349
Having calculated the average value of all stock above the exercise price,
we still need to determine the likelihood that the option will be exercised. To do
this, we need the median of the distribution, the point that exactly bisects the
total number of occurrences. In Figure 18-4, we can see that the median in a
lognormal distribution falls somewhere to the left of the mean. How far to the
left? In fact, the median falls to the left by
t
σ
d
d
t
2
1
σ
=
−
The value N(d2) uses the median to calculate the probability of the option
being in the money at expiration and therefore being exercised. Multiplying
this probability by the exercise price gives us the average amount we will pay at
expiration if we own the option
XN(d2)
Taking the average value of the stock we will receive at expiration and
subtracting the average amount we will pay at expiration gives us the expected
value for the call
SertN(d1) – XN(d2)
There is still one final step in calculating the theoretical value of a call option, and this step explains how the terms S–rtN(d1) and XN(d2) become SN(d1)
and Xe–rtN(d2), which is the way they appear in the Black-Scholes model. The
expression SertN(d1) – XN(d2) represents the expected value of the option at expiration. If we must pay for the option today, the theoretical value is the present value of the expected value. Multiplying the expected value by e–rt yields
the familiar form of the Black-Scholes model
C = [SertN(d1) – XN(d2)]e–rt = SN(d1) – Xe–rtN(d2)
In the original Black-Scholes model, the underlying contract was assumed
to be a non-dividend-paying stock. However, since its introduction, the model
has been extended to evaluate options on other types of underlying instruments. This is most commonly done by including an adjustment factor b that
varies depending on the type of underlying instrument and the settlement
procedure for the options. If r is the domestic interest rate and rf is the foreign
interest rate, then

b = r
The original Black-Scholes model for options on a nondividend-paying stock

b = 0
The Black model for options on futures

b = r – rf	 The Garman-Kohlhagen model for options on foreign
currencies
The complete Black-Scholes model, with variations and sensitivities, is given
in Figure 18-6.
--- page 367 ---

350
O P T I O N V O L AT I L I T Y A N D P R I C I N G
If
S  =  the spot price or underlying price

X  =  the exercise price

t   =  the time to expiration, in years

r   =  the domestic interest rate

σ  =  the annualized volatility or standard deviation, in percent
then the value of a European call, C, and the value of a European put, P, are given by

C  =  S e(b−r)t N(d1) − X e−rt N(d2)
P  =  X e−rt N(−d2) − S e(b−r)t N(−d1)
where
d
ln S
X
b
2
t
t
1
2
=



+
+ σ




σ
d
ln S
X
b
2
t
t
d
t
2
2
1
=



+
−σ




σ
=
−σ
The common variations on the original Black-Scholes model are determined by the value
of b.
If
b  =  r :
The Black-Scholes model for options on stock

b  =  r  =  0 :	The Black-Scholes model for options on futures where the options are
subject to futures-type settlement

b  =  0 :
The Black model for options on futures where the options are subject to
stock-type settlement

b  =  r − rf :	 The Garman-Kohlhagen model for options on foreign currencies, where rf
is the foreign interest rate
For options on a dividend paying stock the spot price, S, must be discounted by the value
of the expected dividend payments.  This can be approximated by setting b = r − q, where
q is the annual dividend yield in percent.  For a more exact calculation we can deduct from
S the value of each dividend payment, D, together with the interest which can be earned
on that dividend payment to expiration.  S is then replaced by S − ΣDier td, where td is the
time remaining from each dividend payment to expiration of the option.
Figure 18-6  The Black-Scholes model.
Call
Put
Delta (Δ)
e(b−r)t N(d1)
e(b−r)t [N(d1)−1]
Gamma (Γ)
e
n(d )
S
t
(b r)t
1
σ
−
same for calls and puts
e
n(d )
S
t
(b r)t
1
σ
−
Theta (Θ)*
Se
n(d )
2 t
(b
r)Se
N(d )-rXe
N(d )
(b r)t
1
(b r)t
1
rt
2
−
σ +
−
−
−
−
Se
n(d )
2 t
(b
r)Se
N(d )+ rXe
N( d )
(b r)t
1
(b r)t
1
rt
2
−
σ +
−
−
−
−
−
Vega**
Se(b−r)t n(d1)√t
same for calls and puts
Se(b−r)t n(d1)√t
Rho (Ρ)**
tXe−rt N(d2) if b ≠ 0
−tC if b = 0
−tXe−rt N(−d2) if b ≠ 0
−tP if b = 0
Rhof or Phi (Φ)
−tSe(b−r)t N(d1)
tSe(b−r)t N(−d1)
Elasticity (Λ)
ΔC (S/C)
ΔP (S/P)
*The theta formula gives the sensitivity of the option to the passage of one year.  To express
theta values in the more common form of daily decay the theta must be divided by 365.
**The vega and rho formulas give the sensitivity of the option to a one full point (100%)
change in volatility (the vega) or interest rates (rho).  To express vega and rho values in the
more common form of a one percentage point change in volatility or interest rates the
vega and rho must be divided by 100.
(continued)
--- page 368 ---

T h e B l a c k - S c h o l e s M o d e l 	 351
A Useful Approximation
A trader might wonder whether it is possible to calculate a Black-Scholes value
without using a computer. In general, the answer is no; the computations are
just too complex. However, there is one type of approximation that many traders are able to make without too much difficulty.
Suppose that an option is exactly at the money (X = S) and that there is
one year to expiration (t = 1). Suppose also that the interest rate is 0 (r = 0) and
that volatility is 1 percent (σ = 0.01). This means that ln(S/X) = 0 and that
t
σ

= 0.01. Calculating d1 and d2, we get
d
d
0.01 /2
0.01
0.005 and
0.01 /2
0.01
0.005
1
2
2
2
=
=
= −
=
If we calculate N(d1) and N(d2), we find that
N(d1) = 0.501995  and  N(d2) = 0.498005
Because the interest rate is 0, the value of the call option must be
(S × 0.501995) – (X × 0.498005)
Call
Put
Vanna
e
n(d ) d
(b r)t
1
2
−
σ
−
same for calls and puts
e
n(d ) d
(b r)t
1
2
−
σ
−
Charm
e
n(d )
b
t
d
2t
(b r)N(d )
(b r)t
1
2
1
−
σ
−



+
−








−
e
n(d )
b
t
d
2t
(b r)N(d )
(b r)t
1
2
1
−
σ
−



−
−








−
Speed
S 1
d
t
1
−Γ
+
σ




same for calls and puts
S 1
d
t
1
−Γ
+
σ




Color
r
b
bd
t
1 d d
2t
1
1
2
Γ
−
+
σ
+ −




same for calls and puts
r
b
bd
t
1 d d
2t
1
1
2
Γ
−
+
σ
+ −




Volga (Vomma)
vega
d d
1
2
σ




same for calls and puts
vega
d d
1
2
σ




Vega Decay
vega r
b
bd
t
1 d d
2t
1
1
2
−
+
σ
−−




same for calls and puts vega r
b
bd
t
1 d d
2t
1
1
2
−
+
σ
−−




Zomma
d d
1
1
2
Γ
−
σ




same for calls and puts
d d
1
1
2
Γ
−
σ




A complete listing of all sensitivities and their formulas can be found in The Complete Guide
to Option Pricing Formula by Espen Gaarder Haug, 2nd Edition, 2007, McGraw-Hill.
Figure 18-6  (continued )
--- page 369 ---

352
O P T I O N V O L AT I L I T Y A N D P R I C I N G
If X = S, the value of the call is
X × (0.501995 – 0.498005) = X × 0.003990
What does this number tell us? For a one-year European option that is exactly at the forward (i.e., the forward price is equal to the exercise price), for
each percentage point of volatility, the expected value for the option is equal
to the exercise price multiplied by 0.00399. If the exercise price is 100, the expected value is 0.00399 × 100 = 0.399 for each percentage point in volatility.
Why doesn’t this value change as we increase volatility? Although the
first percentage point of volatility may be worth 0.00399, perhaps the second
percentage point is worth either more or less than 0.00399. But recall from
Chapter 9 that the vega of an at-the-money option is relatively constant with
respect to changes in volatility. Therefore, at a volatility of 20 percent, the value
of a 100 call should be
20 × 100 × 0.00399 = 7.98
At a volatility of 35 percent, the value should be
35 × 100 × 0.00399 = 13.965
We also know that the theoretical value of an at-the-forward option is proportional to its exercise price. If the value of a one-year 100 call at a volatility
of 20 percent is 7.98, under the same conditions, the value of an at-the-forward
50 call should be
20 × 50 × 0.00399 = 3.99
and the value of a 125 call should be
20 × 125 × 0.00399 = 9.975
We can further refine our approximation if we note that an at-the-money
option is made up entirely of time value and that the time value of an option is
proportional to the square root of time. If a one-year 100 call is worth 7.98 at
a volatility of 20 percent, the same call with six months to expiration (t = 0.5)
must be worth
7.98
0.5
7.98
0.707
5.64
×
=
×
=
Lastly, this is an approximation for the expected value. To determine the
theoretical value, we must discount by interest to get the present value. Putting
everything together, for an exactly at-the-forward European option, the expected value at expiration is approximately3
X
t
(
100)
0.00399
σ
×
×
×
×
3 To further simplify this approximation, many traders round .00399 to .004.  This leads to what is sometimes
referred to as the 40% rule:  the expected value of an at-the-forward option is equal to approximately 40% of
one standard deviation, where one standard deviation is equal to F × σ√t.
--- page 370 ---

T h e B l a c k - S c h o l e s M o d e l 	 353
and the theoretical value is4
X
t
r
t
(
100)
0.00399
1
σ
×
×
×
×
+ ×
This approximation applies to both calls and puts because under put-call parity, an exactly at-the-forward European call and put must have the same value.
For example, if volatility is 18 percent, what is the expected value of a
three-month (t = ¼) at-the-forward option with an exercise price of 65?
65
0.18
100
0.00399
65 18
0.00399
2.33
14
12
×
×
×
×
=
×
×
×
≈
If interest rates are 4 percent, the option’s theoretical value is approximately
2.33
1
0.04/4
2.33
1.01
2.31
+
=
≈
Although this is a commonly used approximation, it is only an approximation. As we increase time and volatility, the approximation will actually be
slightly greater than the true Black-Scholes value. This is because the vega of an
at-the-money option declines slightly as we increase volatility, and this decline
is magnified with greater time to expiration. This can be seen in Figure 9-14:
the vega of an at-the-money option, although relatively constant with respect to
changes in volatility, does in fact decline slightly with increasing volatility. If, in
our example, we raise the volatility to 40 percent and increase the time to expiration to two years, the approximation for the expected value is
65
40
2
0.00399
65
40
1.414
0.00399
14.67
×
×
×
=
×
×
×
≈
while the actual Black-Scholes expected value is 14.48.
The reader who is familiar with the characteristics of a standard normal distribution may already have recognized the significance of the value
0.00399. Referring to Figure 18-2, for a standard normal distribution with
a mean of 0 and standard deviation of 1, the peak of the distribution has a
value of approximately 0.399 (more exactly, 0.398942). Because a volatility of
1 percent represents 1/100 of a standard deviation, the value from the model
is 0.399/100 = 0.00399.
The Delta
In the Black-Scholes model, the delta of an option is equal to N(d1). When we
defined the delta in Chapter 7, we suggested that the delta is approximately
the probability that an option will finish in the money. But we now know that
the true probability that an option will finish in the money is equal to N(d2).
Although N(d1) and N(d2) are often very close in value, especially for shortterm options, N(d1) (the delta) is always larger than N(d2).
4 For a more exact calculation, 1 + r × t can be replaced by e rt.
--- page 371 ---

354
O P T I O N V O L AT I L I T Y A N D P R I C I N G
For a call option that is at the forward, the delta will be greater than 50,
even if only slightly. Because we know that
Put delta = call delta – 100
the delta of a put will be less than –50 in absolute value. This means that an atthe-forward straddle will have a positive delta. If a call and put have the same
exercise price, at what forward price will the delta of the call and put be identical? This will occur when d1 is exactly 0. A straddle will therefore be exactly
delta neutral when
S
X
r
t
ln
/2
0
2
σ(
)



+
+

=
Solving, for S, we get
S
Xe
r
t
/2
2
=
σ(
)
−
+


For a straddle to be exactly delta neutral, the forward price will be less than the
exercise price by a factor of
e
r
t
/2
2
σ(
)
−
+


As time or volatility increases, the forward price at which the straddle is delta
neutral drops further and further below the exercise price—the call goes further out of the money, and the put goes further into the money. With a 0 interest rate, the underlying price at which a 100 straddle will be exactly delta
neutral is shown in Figure 18-7. At very low volatilities, the delta-neutral price
Figure 18-7  The underlying price at which a straddle is exactly delta-neutral.
Volatility
Underlying price
100
99
98
97
96
95
94
93
92
91
90
89
88
50%
45%
40%
35%
30%
25%
20%
15%
Interest rate = 0
Exercise price = 100
The underlying price at which a
straddle is exactly delta-neutral.
As volatility and time increase, the
delta-neutral underlying price
declines: the put is more deeply
in-the-money; the call is further
out-of-the-money
12 months to
expiration
6 months to
expiration
3 months to
expiration
10%
5%
0%
--- page 372 ---

T h e B l a c k - S c h o l e s M o d e l 	 355
is close to 100. But, at very high volatilities and with increasing time to expiration, the delta-neutral price is well below 100.
The Theta
Of all the sensitivities derived from the Black-Scholes model, the formula for
theta is probably the most complex. Depending on the underlying instrument
and the option settlement procedure, the passage of time affects option values
in three different ways. First, there is a decay in the option’s volatility value—
as time passes, the distribution of possible prices at expiration becomes more
restricted. This is represented by the first term in the theta formula
Se
n d
t
(
)
2
b r t
(
)
1 σ
−
−
Second, for an underlying contract such as stock, the spot price is assumed to
move toward the forward price as time passes. This is represented by the second term in the theta formula
b
r Se
N d
(
)
(
)
b r t
(
)
1
−
−
Finally, the present value of the option’s expected value at expiration is changing as time passes. This appears in the formula as
rXe
N d(
)
rt
2
−
We know from put-call parity that the volatility value for a call and put
with identical contract specifications must be the same. The sign of the first
component, the decay in volatility value, must therefore be the same for calls
and puts. The other two theta components depend on the effects of interest
rates and may be either positive or negative depending on the settlement procedure and whether the option is a call or a put.
The decay in volatility value is almost always more important than interest considerations and will tend to dominate the theta calculation. If interest rates are 0 or if options on futures are subject to futures-type settlement,
the second and third components in the theta formula will be 0, leaving only
the volatility decay component. In this case, the volatility decay component,
sometimes referred to as the driftless theta, will be the sole factor that determines
how an option’s theoretical value changes as time passes.
Maximum Gamma, Theta, and Vega
In Chapter 7, we suggested that an option has its maximum gamma, theta, and
vega when it is exactly at the money. But, just as we tend to assign a delta of 50
to an at-the-money option, this is only an approximation. Where does the maximum gamma, theta, and vega really occur?
--- page 373 ---

356
O P T I O N V O L AT I L I T Y A N D P R I C I N G
Without going into the mathematical derivation, we can summarize the
critical underlying prices S as follows:

Delta of 50:

S
Xe
b
t
(
/2)
2
=
σ
−−

Maximum gamma5:

S
Xe
b
t
(
3
/2)
2
=
σ
−−

Maximum theta5:

S
Xe b
t
(
/2)
2
=
σ
+

Maximum vega5:

S
Xe
b
t
(
/2)
2
=
σ
−+
If b = 0, the maximum gamma and theta will occur at an underlying price that
is higher than the exercise price, and the maximum vega will occur at an underlying price that is lower than the exercise price. Moreover, the maximum
gamma and theta will occur at the same underlying price. This is shown in
Figure 18-8 for a one-year option with an exercise price of 100. If we raise interest rates (b > 0), the underlying price at which the maximum gamma and
vega occur will fall, and the underlying price where the maximum theta occurs
will rise. This is shown in Figure 18-9.
We might also consider what will happen to the vega of an option as we
change time. The answer may seem obvious because we previously made the
assumption that the vega always increases with time—long-term options are
Figure 18-8  At an interest rate of zero, the underlying price at which the maximum
gamma, theta, and vega occur.*
Volatility
Underlying price
120
115
110
105
100
95
90
85
80
75
70
65
50%
45%
40%
35%
30%
25%
20%
15%
Interest rate = 0
Exercise price = 100
The underlying price at which
the maximum gamma, theta,
and vega occur.
Maximum
gamma
Maximum
theta and vega
10%
5%
0%
*We can also relate the critical underlying prices to the higher-order risk measures. If we ignore the extremes,
where the option is either very deeply in the money or very far out of the money, the maximum gamma will occur
when the option’s speed is 0. The maximum theta will occur when the option’s charm is 0. The maximum vega will
occur when the option’s vanna is 0.
--- page 374 ---

T h e B l a c k - S c h o l e s M o d e l 	 357
more sensitive to a change in volatility than short-term options. But this is true
only if the underlying price is equal to the forward price, as it is assumed to be
when evaluating options on futures. If we evaluate a stock option, the forward
price for stock is a function of both time and interest rates. If interest rates are
greater than 0, and assuming no dividends, as we increase time, the forward
price will increase, causing the option to become either more or less at the forward. Because an at-the-forward option tends to have the highest vega, changing time can cause the vega of an option to either rise or fall. This means that
under some conditions, it is possible for the vega of a stock option to decline if
we increase to expiration. We can see this effect in Figure 18-10.
With an underlying stock price of 100, a volatility of 20 percent, and interest rate of 0, the vega of a 100 call always increases as we increase time to
expiration. But as we raise interest rates, there is some point in time at which
the opposite occurs—the option’s vega begins to decline as we increase time to
expiration. At an interest rate of 10 percent, this occurs if there are more than
33 months remaining to expiration. At an interest rate of 20 percent, the critical time is 10 months remaining to expiration.
We can also see where these critical points are by looking at a graph of the
vega decay, as shown in Figure 18-11. At an interest rate of 0, the vega decay is
always positive. At an interest rate of 10 percent, the vega decay is positive with
less than 33 months to expiration but negative with more than 33 months. And at
an interest rate of 20 percent, the vega decay is positive with less than 10 months
to expiration and negative with more than 10 months.
Figure 18-9  At an interest rate of 4 percent, the underlying price at which the maximum
gamma, theta, and vega will occur.
Volatility
Underlying price
120
115
110
105
100
95
90
85
80
75
70
65
50%
45%
40%
35%
30%
25%
20%
15%
Maximum
theta
Maximum
vega
Maximum
gamma
10%
5%
0%
Interest rate = 4%
Exercise price = 100
The underlying price at which
the maximum gamma, theta,
and vega occur.
--- page 375 ---

358
O P T I O N V O L AT I L I T Y A N D P R I C I N G
Figure 18-10  Vega as time and interest change.
Time to expiration (months)
Vega
0
.10
.20
.30
.40
.50
.60
.70
.80
48
46
42
39
36
33
30
27
24
21
18
15
12
9
6
3
0
Interest rate = 20%
Interest rate = 10%
Interest rate = 0%
Stock price = 100
Exercise price = 100
Volatility = 20%
Increasing the interest rate
can cause the vega of a
stock option to decline
as time increases.
Figure 18-11  Vega decay as time and interest change.
Time to expiration (months)
Vega decay (the change in vega as time passes)
–.0002
0
.0002
.0004
.0006
.0008
.0010
48
46
42
39
36
33
30
27
24
21
18
15
12
9
6
3
0
Stock price = 100
Exercise price = 100
Volatility = 20%
Interest rate = 10%
Interest rate = 0%
Interest rate = 20%
--- page 376 ---

359
Binomial Option Pricing
The Black-Scholes model is the most widely used of all theoretical option pricing models. Unfortunately, a full understanding of the model requires some familiarity with advanced mathematics. In the late 1970s, three professors, John
Cox of the Massachusetts Institute of Technology, Stephen Ross of Yale University, and Mark Rubinstein of the University of California at Berkeley, were
trying to develop a method of explaining basic option pricing theory to their
students without using advanced mathematics. The method they proposed, binomial option pricing,1 is not only relatively easy to understand, but the binomial
model (also known as the Cox-Ross-Rubinstein model) that resulted from this approach can be used to price some options (primarily American options) that
cannot be priced using the Black-Scholes model.
A Risk-Neutral World
Consider a security that is currently trading at 100 and that,
on some day in the future, can
take on one of two prices, 120
and 90. Assuming that there are
no interest or dividend considerations, would you rather buy
or sell this security at today’s
price of 100?
Instinctively, it seems that
one would rather be long this
security at a price of 100 than
short the security at the same
price. After all, the security can
go up 20 but down only 10.
1 John C. Cox, Stephen A. Ross, and Mark Rubinstein, “Option Pricing: A Simplified Approach,” Journal of
Financial Economics 7(3):229–263, 1979.
19
120
90
100
--- page 377 ---

360
O P T I O N V O L AT I L I T Y A N D P R I C I N G
The decision to go long is probably based on the assumption that the likelihood of the price rising and falling is the same, 50 percent. But why should the
probabilities be the same? Perhaps the probability of movement in one direction is greater than the probability of movement in the other direction. Indeed,
there should be some probability of upward movement p and downward movement 1 – p such that an investor will be indifferent as to whether he buys or sells
the security. For an investor to be indifferent, the total expected value must be
equal to the current price of 100
p × 120 + (1 – p) × 90 = 100
Solving for p, we get
120p + 90 – 90p = 100 >> 30p = 10 >> p = ⅓
We can confirm that this is correct by doing the arithmetic
⅓ × 120 + ⅔ × 90 = 40 + 60 = 100
If S is the current security price, we can generalize this approach by defining u and d as multipliers that represent the magnitudes of the upward and
downward moves. This results in a one-period binomial tree:
Su
p
1–p
Sd
S
In a risk-neutral world,
pSu + (1 – p)Sd = S
Solving for p,
p(Su) + (1 – p)Sd = S >> pu + d – pd = 1 >> p = (1 – d)/(u – d)
In our original example, u and d were 1.20 and 0.90, respectively, with p
equal to
1
0.90
1.20
0.90
0.10
0.30
1
3
−
−
=
=
What should p and 1 – p be for a non-dividend-paying stock? For an investor to be indifferent to buying or selling, the risk neutral probabilities
--- page 378 ---

B i n o m i a l O p t i o n P r i c i n g 	 361
must yield a value that is equal to the forward price for the stock S(1 + r × t).
Therefore,
p(Su) + (1 – p)Sd = S(1 + r × t) >> pu + d – pd = 1 + r × t >> p =
r
t
d
u
d
(1
)
+ ×
−
−
Valuing an Option
Suppose that we want to value an option using a one-period binomial tree. We
know at expiration that an option is worth exactly its intrinsic value, the maximum of [S – X, 0] for a call and the maximum of [X – S, 0] for a put. In a oneperiod binomial tree, the expected value of a call is
p × max[Su – X, 0] + (1 – p) × max[Sd – X, 0]
The theoretical value of the call is the present value of the expected value
p
Su
X
p
Sd
X
r
t
max[
,0]
(1
)
max[
,0]
1
×
−
+
−
×
−
+ ×
Using the same reasoning, the theoretical value of the put is
p
X
Su
p
X
Sd
r
t
max[
,0]
(1
)
max[
,0]
1
×
−
+
−
×
−
+ ×
Suppose that we expand our binomial tree to two periods each of length
t/2 and also make the assumption that u and d are multiplicative inverses. Then
d = 1/u >> u = 1/d >> ud = du = 1
This means that an up move followed by a down move or a down move
followed by an up move results in the same price. If the magnitudes of the up
and down moves u and d are the same at every branch in our tree, then in a riskneutral world, the probability of an upward move will always be
p
r
t n
d
u
d
[1
(
/ )]
=
+
×
−
−
and the probability of a down move will always be 1 – p.
Su
Sd
S
1–p
p
Sdd
Suu
Sud
p
Sdu
p
1–p
1–p
--- page 379 ---

362
O P T I O N V O L AT I L I T Y A N D P R I C I N G
There are now three possible prices for the underlying at expiration—Suu, Sud,
and Sdd. There is only one path that will lead to either Suu or Sdd. But there are
two possible paths to the middle price Sud. The underlying can go up and then
down or down and then up. The theoretical value of a call in the two-period
example is
p
Suu
X
p
p
Sud
X
p
Sdd
X
r
t
max[
,0]
2
(1
)
max[
,0]
(1
)
max[
,0]
(1
/2)2
×
−
+
×
×
−
×
−
+
−
×
−
+ ×
The value of a put is
p
X
Suu
p
p
X
Sud
p
X
Sdd
r
t
max[
,0]
2
(1
)
max[
,0]
(1
)
max[
,0]
(1
/2)2
×
−
+
×
×
−
×
−
+
−
×
−
+ ×
Using this approach, we can expand our binomial tree to any number of
periods.
If

n = number of periods in the binomial tree

t = time to expiration in years

r = annual interest rate
the possible terminal underlying prices are
Sujd(n-j)    for j = 0, 1, 2, …, n
The number of paths that will lead to each terminal price is given by the binomial expansion2
n
j n
j
!
!(
)!
−
The values of a European call and put are
r
t n
n
j n
j
p
p
Su d
X
Call
1
(1
/ )
!
!(
)!
(1
)
max[
,0]
n
j
n
j
j
n
j
j
n
0∑
=
+ ×
−
×
−
×
−
−
−
=
r
t n
n
j n
j
p
p
X
Su d
Put
1
(1
/ )
!
!(
)!
(1
)
max[
,0]
n
j
n
j
j
n
j
j
n
0∑
=
+ ×
−
×
−
×
−
−
−
=
A Three-Period Example
Suppose that

n = 3

S = 100

t = 9 months (0.75 year)

r = 4 percent (0.04)

u = 1.05

d = 1/u ≈ 0.9524
2 The binomial expansion is sometimes written as
n
j



.
--- page 380 ---

B i n o m i a l O p t i o n P r i c i n g 	 363
Then the values of p and 1 – p are

=
+ ×
−
−
=
+
−
−
=
p
r
t n
d
u
d
(1
/ )
(1
0.03/3)
0.9524
1.05
0.9524
0.59

1 – p = 1 – 0.59 = 0.41
The complete three-period binomial tree is shown in Figure 19-1.3
Using the three-period binomial tree, what should be the value of a 100
call and a 100 put?
Terminal
Price
100 Call
Value
100 Put
Value
Probability
Number of
Paths
Total
Probability
115.76
15.76
0
0.59 × 0.59 × 0.59 = 0.2054
1
0.2054
105.00
5.00
0
0.59 × 0.59 × 0.41 = 0.1427
3
0.4281
95.24
0
4.76
0.59 × 0.41 × 0.41 = 0.0992
3
0.2976
86.38
0
13.62
0.41 × 0.41 × 0.41 = 0.0689
1
0.0689
3 For simplicity, binomial trees are often drawn symmetrically from top to bottom. However, this can be somewhat misleading. If drawn to scale, the branches typically become narrower as we move from top to bottom. We can see this in Figure 19-1: 115.76 – 105.00 = 10.76 (the top two branches); 105.00 – 95.24 = 9.76
(the middle two branches); 95.24 – 86.38 = 8.86 (the bottom two branches). Because 10.76 > 9.76 > 8.86, the
branches must be getting narrower.
Figure 19-1  A three-period binomial tree.
100.00
.41
.59
Stock price (S) = 100.00
Number of periods (n) = 3
Time to expiration (t) = 9 months = .75
Annual interest rate (r) = 4.00%
u = 1.05
d = 1/1.05 ≈ .9524
p =
=
≈ .59
.0576
.0976
1 + (.04 × .75/3) – .9524
1.05 –.9524
1 – p = 1 – .59 = .41
105.00
95.24
110.25
100.00
90.70
.41
.59
.41
.59
115.76
105.00
95.24
.41
.59
.41
.59
.41
.59
86.38
--- page 381 ---

364
O P T I O N V O L AT I L I T Y A N D P R I C I N G
The value of the 100 call is
0.2054
(115.76
100)
0.4281
(105.00
100)
(1
0.03/3)
0.2054
15.76
0.4281
5.00
(1.0927/3)
3
3
5.22
×
−
+
×
−
+
=
×
+
×
=
The value of the 100 put is
0.2976
(100
95.24)
0.0689
(100
86.38)
(1
0.03/3)
0.2976
4.76
0.0689
13.62
1.0927
3
2.28
×
−
+
×
−
+
=
×
+
×
=
If the values for the 100 call and put are correct, they should be consistent
with put-call parity
C
P
F
X
r
t
1
−
=
−
+ ×
We can check this by first calculating the forward price for the stock. Because
we are compounding interest over three time periods, the forward price is
F = 100 × (1 + 0.75 × 0.04/3)3 = 100 × 1.0303 = 103.03
Then
F
X
r
t n
(1
/ )
103.03 100
1.0303
2.94
n
−
+ ×
=
−
=
which is indeed equal to C – P
5.22 – 2.28 = 2.94
Binomial Notation
When constructing a binomial tree, it is customary to denote each price in
the tree as Si,j, where i, j = 0, 1, 2, . . . , n. The value of i locates S along the tree
moving from left to right. The value of j locates S moving from bottom to top.
A five-period binomial tree using this notation is shown in Figure 19-2.
Instead of filling in a binomial tree with the underlying prices Si,j at each
node, we can instead fill in the tree with option values, either Ci,j for calls or
Pi,j for puts. Figure 19-3 shows the value of a 100 call at each node along the
binomial tree in Figure 19-1. The terminal values C3,j are simply the maximum of either S3j – 100 or 0. For S3,3 = 115.76, the value of the call C3,3 is
equal to 115.76 – 100 = 15.76; for S3,2 = 105.00, the value of the call C3,2 is
equal to 105.00 – 100 = 5.00. For S3,1 = 95.24 and S3,0 = 86.38, the 100 call
is out of the money, so both C3,1 and C3,0 are 0.
It’s obvious what the value of the 100 call is at expiration, either  intrinsic value or 0. But what should be the value of the call at other nodes along
the tree? To determine these values, we can work backwards from the terminal values using the probabilities of upward and downward moves and discounting by interest to determine the present value. For example, what is the
value of C2,2? We know that there is a 59 percent chance that at S2,2 the stock
will move up in price, in which case the option will be worth 15.76. We also
