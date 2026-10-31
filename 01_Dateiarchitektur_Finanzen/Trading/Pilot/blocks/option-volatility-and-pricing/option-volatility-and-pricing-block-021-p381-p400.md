# Option Volatility and Pricing_ Advanced Trading Strategies -- Sheldon Natenberg -- 2nd ed, 2014 -- McGraw Hill Professional -- isbn13 9780071818773 -- 6a48d008bd9beef283debf7bad0b2e4a -- Anna’s Archive.pdf — pages 381–400

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
--- page 382 ---

B i n o m i a l O p t i o n P r i c i n g 	 365
Fgure 19-2  Binomial notation for a five-period binomial tree.
S0,0
S1,1
S1,0
S2,2
S2,1
S2,0
S3,3
S3,2
S3,1
S3,0
S4,4
S4,3
S4,2
S4,1
S4,0
S5,0
S5,1
S5,2
S5,3
S5,4
S5,5
Figure 19-3  A call value at any point along the binomial tree.
.41
.59
.41
.59
.41
.59
.41
.59
.41
.59
.41
.59
C1,1 = 7.75
C2,2 = 11.24
C3,3 = 15.76
C3,2 = 5.00
C3,1 = 0
C3,0 = 0
C2,1 = 2.92
C2,0 = 0
C1,0 = 1.71
C0,0 = 5.22
Ci,j = [ pCi+1,j+1 + (1 – p)Ci+1,j] / (1 + rt/n)
know that there is a 41 percent chance that the stock will move down in price,
in which case the option will be worth 5.00. The expected value of the option
at C2,2 is therefore
(0.59 × 15.76) + (0.41 × 5.00) = 11.35
--- page 383 ---

366
O P T I O N V O L AT I L I T Y A N D P R I C I N G
The theoretical value of the option at C2,2 is the present value of 11.35
11.35
1
0.03/3
11.35
1.01
11.24
+
=
=
Using the same reasoning, the theoretical value of the option at C2,1 is
(0.59
5.00)
(0.41
0)
1.01
2.92
×
+
×
=
The value of the option at C2,0 must be 0 because either an upward or downward move results in a value of 0. We can express the value of a call at any
point along the binomial tree as
C
pC
p C
r
t n
(1
)
1
/
i j
i
j
i
j
,
1,
1
1,
=
+
−
+ ×
+
+
+
Working backwards along the tree, we come finally to C0,0, the option’s initial theoretical value. Of course, we already know from our previous calculation that this value is 5.22, so why go through the process of calculating the call
value at every point along the binomial tree? The reason for calculating these
intermediate values is that they not only enable us to determine some of the
risk sensitivities associated with the option, but also, as we will see later, they enable us to calculate the value of an American option.
The Delta
We know the initial value of the 100 call, 5.22. But what is the option’s delta at
C0,0? The delta is the change in the option’s value with respect to movement in
the price of the underlying contract. We can express this as a fraction
Δ
C
C
S
S
u
d
n
d
∆=
−
−
As we move from C0,0 to either C1,1 or C1,0, the option will go up in value to 7.75
or down in value to 1.71. At the same time, the stock will move up in price to
105.00 or down in price to 95.24. The delta is therefore
7.75 1.71
105
95.24
6.04
9.76
0.62
−
−
=
=
Using the whole-number format, the initial delta of the 100 call is 62.
We can calculate the delta at every point along the binomial tree by dividing the change in the option’s value by the change in the underlying price
Δi,  j
C
C
S
S
i
j
i
j
i
j
i
j
1,
1
1,
1,
1
1,
=
−
−
+
+
+
+
+
+
Figure 19-4 shows the stock price, the value of the 100 call, and the delta of the
call at every node along the binomial tree.
In Chapter 8, we showed that the dynamic hedging process enables us
to capture the difference between an option’s value and its price. We can see
--- page 384 ---

B i n o m i a l O p t i o n P r i c i n g 	 367
this same principal at work in the binomial model. Returning to Figure 19-4,
suppose that we buy the 100 call at its theoretical value of 5.22 and create a
delta-neutral hedge (Δ = 62) by selling 62 percent of an underlying stock contract at a price of 100. What will be the result if we hold the position for one
time period?
If the stock price moves up to 105.00, the option will be worth 7.75, resulting in a profit on the option of 7.75 – 5.22 = 2.53. At the same time, we will
lose 0.62 × (100 – 105) = −3.10 on the stock position, giving us a loss on the
hedge of
+2.53 – 3.10 = –0.57
If the stock price moves down to 95.24, the option will be worth 1.71, resulting in a loss on the option of 1.71 – 5.22 = –3.51. At the same time, we will
make 0.62 × (100 – 95.24) = 2.95 on the stock position, giving us a loss on the
hedge of
–3.51 +2.95 = –0.56
It seems that we will lose money, either 0.56 or 0.57, regardless of whether the
stock moves up or down in price. In fact, both numbers are the same, the difference being due to a rounding error in our calculations (the true delta is 61.88).
But this still leaves us with a loss when option pricing theory says we ought to
break even.
Figure 19-4  Delta of an option using a binomial tree.
110.25
11.24
∆ = 100
.41
.59
.41
.59
.41
.59
.41
.59
.41
.59
.41
.59
100.00
5.22
∆ = 62
105.00
7.75
∆ = 81
95.24
1.71
∆ = 31
100.00
2.92
∆ = 51
90.70
0
∆ = 0
115.76
15.76
105.00
5.00
95.24
0
86.38
0
∆i,j = (Ci+1,j+1 – Ci+1,j)/( Si+1,j+1 – Si+1,j)
--- page 385 ---

368
O P T I O N V O L AT I L I T Y A N D P R I C I N G
Recall that when we bought the option and sold stock, the cash flow was a
credit to our account of
–5.22 + 0.62 × 100 = +56.78
At an interest rate over this time period of 1.00 percent, we are able to earn interest on this credit of
0.01 × 56.78 ≈ +0.57
Including this in our calculations, we do in fact just break even.
If we go through the delta-neutral rehedging process at every node in the
tree, taking into consideration the value of the hedge as well as any interest
considerations, regardless of the path the stock follows, at expiration, we will
break exactly even. It therefore follows that if we are able to buy an option at
a price less than theoretical value or sell an option at a price greater than theoretical value, we will show a profit at expiration equal to the difference between
the price at which we traded the option and its theoretical value. This is the
principle of dynamic hedging described in Chapter 8.
The Gamma
The gamma of an option is the change in the option’s delta with respect to
movement in the price of the underlying contract. As we did with the delta, we
can express the gamma as a fraction
S
S
∆
∆
u
d
u
d
Γ =
−
−
In Figure 19-4, we can see that as we move from C0,0 to either C1,1 or C1,0, the
option’s delta will either go up to 81 or down to 31. At the same time, the stock
will either move up to 105.00 or move down to 95.24. The gamma is therefore
81 31
105.00
95.24
50
9.76
5.1
−
−
=
=
The initial gamma of the 100 call is 5.1.
We can calculate the gamma at any point along the binomial tree by dividing the change in the option’s delta by the change in the underlying price
S
S
∆
∆
i j
i
j
i
j
i
j
i
j
,
1,
1
1,
1,
1
1,
Γ
=
−
−
+
+
+
+
+
+
The Theta
The theta is the change in an option’s value as time passes, assuming everything else, including the underlying price, remains unchanged. In a binomial
model, at each time period, the underlying price is assumed to move either up
--- page 386 ---

B i n o m i a l O p t i o n P r i c i n g 	 369
or down. The underlying price remains unchanged only after two time periods, when the underlying price either goes up and down or down and up. To
approximate the theta, we must therefore consider the change in the option’s
value over two time periods.
In Figure 19-4, we can see that as we move from C0,0 to C2,1, the value of
the 100 call drops from 5.22 to 2.92, for a loss in value of 2.30. If we want to
estimate the daily theta, we can divide by the number of days during this twoperiod time
0 0252
0.75
365
3
91.25
2.30
91.25
.
×
=
−
= −
We can approximate the daily theta at any point along the tree as
C
C
t
n
365/
i j
i
j
,
2,
1
−
×
+
+
Vega and Rho
It would be convenient if we could use the same simple arithmetic to calculate the vega and rho that we used to calculate the delta, gamma, and theta.
Unfortunately, there is no simple solution to the volatility and interest-rate
sensitivities. To determine the vega, we must change the volatility input—we
will see shortly how we determine this input—and then see how the option’s
value changes. To determine the rho, we must change the interest-rate input.
The Values of u and d
We have chosen the upward move u and downward move d so that they form a
recombining binomial tree. The terminal price for the security is independent of
the order in which the price moves occur. Whether the security moves up first
and then down or down first and then up, the result is the same
u × d = d × u
If the upward and downward moves were not recombining, the number of calculations would be greatly increased because each node on the binomial tree
would yield a completely new set of upward and downward values.
We have also chosen u and d so that they are the multiplicative inverse of
each other
u × d = d × u = 1.00
This ensures that if the security makes an upward move followed by a downward
move or a downward move followed by an upward move, the resulting underlying price will be same price at which it began. If u and d were not inverses, there
would be a drift in the underlying price. If, for example, u and d were chosen to be
1.25 and 0.75, then there would be a downward drift because
u × d = 1.25 × 0.75 = 0.9375
--- page 387 ---

370
O P T I O N V O L AT I L I T Y A N D P R I C I N G
In order to calculate the theta, as we did previously, we need to eliminate the
drift in the underlying price. This will be true if u and d are multiplicative
inverses.
Other than the restrictions that u and d are inverses and result in a driftless underlying price, we have not specified exactly what the values of u and d
should be. It will not come as a surprise that u and d must be derived from the
volatility input. If we want binomial values to approximate Black-Scholes values, u and d must be chosen in such a way that the terminal prices approximate
a lognormal distribution. We can achieve this by defining u and d as a one standard deviation price change over each time period in our binomial tree
u
e
d
e
and
t n
t n
/
/
=
=
σ
σ
−
In our three-period example, what volatility does u = 1.05 represent? To
determine this, we can work backwards to solve for the volatility σ
u
e
e
e
1.05
75/3
25
0.5
=
=
=
=
σ
σ
σ
Taking the natural logarithm of each side, we get
ln(1.05) = ln(e0.5σ) >> 0.0488 = 0.5σ >> σ =0.0976  (9.76%)
In our three-period example, we used a volatility of 9.76 percent.
Gamma Rent
In theory, every volatility position in the option market represents a tradeoff
between the cash flow created by the dynamic hedging process and the decay
in the option’s value as time passes. A positive gamma, negative theta position
will make money through dynamic hedging but lose money through time decay. A negative gamma, positive theta position will perform just the opposite,
losing money through dynamic hedging but making money through time decay. Traders sometimes refer to volatility trading as renting the gamma, with the
rental costs being equal to the theta.
Over a given time period, how much movement is required in the underlying contract to offset the effects of time decay? We can give an approximate
answer by going back to our binomial tree. We know that a delta-neutral position taken at theoretical value will just break even if the underlying contract
moves either up by u or down by d. The magnitudes of the u and d are equal to
u
e
d
e
and
t n
t n
/
/
=
=
σ
σ
−
But these values are equal to a one standard deviation price change over the
time interval t/n. Therefore, over any interval of time, the amount of price
movement needed in the underlying contract to just break even must be equal
to one standard deviation.
The reason that this is only an approximation is that while u and d remain constant, theta changes, sometime very rapidly, as time passes. For very
short time intervals or with a great deal of time remaining to expiration, this
--- page 388 ---

B i n o m i a l O p t i o n P r i c i n g 	 371
approximation will be reasonably accurate. However, over longer time intervals or with very little time remaining to expiration, the changes in the theta
will cause the approximation to be less accurate.
American Options
Let’s go back to our three-period binomial tree in Figure 19-1. But instead of
calculating the value of a 100 call,  as we did in Figure 19-4, let’s work backwards from the terminal prices to calculate the value of a 100 put. The underlying prices, theoretical values, and delta and gamma values for the 100 put are
all shown in Figure 19-5. The reader may wish to confirm that the call and put
values in Figures 19-4 and 19-5 are consistent with basic principles of option
pricing: at every node, put-call parity is maintained; the absolute values of call
and put deltas always add up to 100; and the call and put gammas are identical.
If we assume that the 100 put is European and cannot be exercised early,
the only reason to calculate the intermediate values is to determine the delta
and gamma. But suppose that the 100 put is American. Might there be any reason to exercise the option prior to expiration?
Look closely at the value of the 100 put at P2,0 in Figure 19-5. The theoretical value of the put is 8.31. But with an underlying price of 90.70  the put has
an intrinsic value of 9.30. If the put is American, anyone holding the put under
those conditions will choose to exercise it early. If we are using a binomial tree
to evaluate an American option, we might compare the value of the European
option with the intrinsic value at each node. If the intrinsic value is greater than
Figure 19-5  The value of a 100 put at any point along the binomial tree.
.41
.59
.41
.59
.41
.59
.41
.59
.41
.59
.41
.59
100.00
P0,0 = 2.28
∆ = –38
Г = 5.1
95.24
P1,0 = 4.50
∆ = –69
Г = 5.5
105.00
P1,1 = .78
∆ = –19
Г = 4.8
110.25
P2,2 = 0
∆ = 0
100.00
P2,1 = 1.93
∆ = –49
90.70
P2,0 = 8.31
∆ = –100
115.76
P3,3 = 0
105.00
P3,2 = 0
95.24
P3,1 = 4.76
86.38
P3,0 = 13.62
Pi,j = [pPi+1,j+1 + (1 – p)Pi+1,j]/(1+ rt/n)
--- page 389 ---

372
O P T I O N V O L AT I L I T Y A N D P R I C I N G
the European value, we can replace the value at that node with the option’s intrinsic value and then continue to work backwards to determine the option’s
value at each preceding node. If we replace the value at P2,0 with 9.30, the put
value at P1,0 will be
(0.59
1.93)
(0.41
9.30)
1.01
4.90
×
+
×
=
We need to replace the European value of 4.50 at P1,0 with the American value
of 4.90.
Finally, the initial value, P0,0, is
(0.59
0.78)
(0.41
4.90)
1.01
2.44
×
+
×
=
Because the delta and gamma are calculated from option values at every node,
these new values will affect the calculation of the delta and gamma for an
American option. The initial delta of the 100 put if it is American is
0.78
4.90
105.00
95.24
0.42
−
−
=
The delta of the European 100 put was –38, but the delta of American 100
put is –42. The values for an American 100 put at every node are shown in
Figure 19-6. Because the delta is affected by the possibility of early exercise,
the gamma will also be affected. The gamma for the 100 put is now
19
79
105.00
95.24
6.1
−
−
−
=
rather than a gamma of 5.1 for the European option.
Figure 19-6  The value of an American 100 put.
105.00
.78
∆ = –19
Г = 4.8
100.00
2.44
∆ = –42
Г = 6.1
95.24
4.90
∆ = –79
Г = 5.5
90.70
9.30
∆ = –100
110.25
0
∆ = 0
.41
.59
.41
.59
.41
.59
.41
.59
.41
.59
.41
.59
100.00
1.93
∆ = –49
115.76
0
105.00
0
95.24
9.76
86.38
13.62
--- page 390 ---

B i n o m i a l O p t i o n P r i c i n g 	 373
Dividends
How does the possibility of early exercise affect the value of a call? If we look
at the call value at every node in Figure 19-4, we find that at no point is it less
than intrinsic value. This means that the European and American values must
be the same. And, indeed, we know from Chapter 16 that if a stock does not
pay a dividend over the life of the option, there is never any reason to exercise
an American stock option call early.
But what if the stock does pay a dividend? Suppose that the stock in
Figure 19-1 will pay a dividend of 2.00 at some point during the last time period. When a stock pays a dividend, its price typically drops by the amount of
the dividend. Consequently, each terminal price in our binomial tree will be reduced by the amount of the dividend,4 as shown in Figure 19-7. (The terminal
values if there is no dividend are shown in parentheses.) If we want to calculate
the value of the 100 call, we can use these new terminal prices. Then, as before,
we can use the probabilities p and 1 – p to calculate the theoretical value and
delta of the 100 call at each node of the binomial tree. These values are shown
in Figure 19-8.
The value for the 100 call in Figure 19-8 is a European value because we
never considered the possibility of early exercise. But look more closely at the
value of the call one time period prior to expiration with the stock price at
4 For simplicity, we ignore the interest that can be earned on the dividend payment. A more accurate binomial
tree should also include this amount.
Figure 19-7  A binomial tree with dividend payment
100.00
95.24
105.00
100.00
.41
.59
.41
.59
.41
.59
103.00
93.24
.59
.41
.59
.41
.59
.41
Dividend
payment
of 2.00
110.25
90.70
(115.76)
113.76
(105.00)
(95.24)
(86.38)
86.38
Terminal prices are reduced by the amount of the dividend.
--- page 391 ---

374
O P T I O N V O L AT I L I T Y A N D P R I C I N G
110.25. The theoretical value of the 100 call is 9.26. But, with a stock price of
110.25, the call has an intrinsic value of 10.25. If the call is American, anyone
holding the call under these conditions will choose to exercise it early. As we
did with an American put, at each node, we can compare the European value
of the call with its intrinsic value. If the intrinsic value is greater than the European value, we can replace the value at that node with the option’s intrinsic
value and then continue to work backwards to determine the option’s value at
each preceding node. The initial value of the call, C0,0, will then be the value
of an American call. The complete binomial tree for the American 100 call is
shown in Figure 19-9.
If we want to construct a binomial tree for a dividend-paying stock, it
might seem that we can simply reduce all stock prices following the dividend
payment by the amount of the dividend. In Figure 19-7, where the dividend was paid over the last time period, this reduced the terminal prices by
2.00. But suppose that the dividend is paid during the next-to-last time period, as shown in Figure 19-10. The stock prices at the following nodes are
reduced by 2.00. But look at what happens when we continue to calculate
stock prices using u = 1.05 and d = 0.9524. The subsequent stock prices do
not recombine. Each node begins a new binomial tree. In our three-period
binomial tree, this may not seem like a significant problem. We can still calculate the value of an option using the terminal stock prices (now there are
Figure 19-8  The value of a European call on a dividend-paying stock.
100.00
3.99
∆ = 52
Г = 5.5
95.24
1.02
∆ = 19
105.00
6.12
∆ = 73
100.00
1.75
∆ = 31
.41
.59
.41
.59
.41
.59
113.76
13.76
103.00
3.00
93.24
0
84.38
0
.59
.41
.59
.41
.59
.41
Dividend
payment
of 2.00
110.25
9.26
∆ = 100
90.70
0
∆ = 0
--- page 392 ---

B i n o m i a l O p t i o n P r i c i n g 	 375
Figure 19-9  The value of an American call on a dividend-paying stock.
100.00
4.33
∆ = 58
Г = 6.6
95.24
1.02
∆ = 19
105.00
6.70
∆ = 83
100.00
1.75
∆ = 31
.41
.59
.41
.59
.41
.59
113.76
13.76
103.00
3.00
93.24
0
84.38
0
.59
.41
.59
.41
.59
.41
Dividend
payment
of 2.00
110.25
10.25
∆ = 100
90.70
0
∆ = 0
Figure 19-10  The value of an American call on a dividend-paying stock.
100.00
95.24
105.00
.41
.59
Dividend
payment
of 2.00
.59
.41
.59
.41
(110.25)
108.25
(100.00)
98.00
(90.70)
88.70
.41
.59
113.66
103.10
102.90
93.33
.41
.59
93.14
84.48
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
1.05 – .9524
1 – p = 1–.59 = .41
--- page 393 ---

376
O P T I O N V O L AT I L I T Y A N D P R I C I N G
six terminal prices instead of four) and then work backward to determine
the option’s theoretical value. The value for the 100 call using our new binomial tree is shown in Figure 19-11.
What if there are multiple dividend payments over the life of the option?
And what if our binomial tree consists of many time periods? Because each
dividend payment generates a new set of binomial prices, the number of calculations required to value an option will be greatly increased, perhaps to the
point of being unwieldy. This presents a problem to which there is no ideal
solution. Perhaps the simplest way to handle dividend payments is to create
a complete binomial tree without dividends and then reduce the stock price
at each node by the total amount of dividends. An example of this is shown
in Figure 19-12, which represents an approximation of the call option value
generated in Figure 19-11. Instead of generating new binomial prices after
the dividend payment, we have simply reduced all subsequent values by the
2.00 amount of the dividend. We can see that this is only an approximation.
The call values in Figure 19-12 tend to be slightly larger than the values in
Figure 19-11.
One final comment about the values for p and 1 – p. We typically expect a
probability to fall between 0 to 1.00, that is, somewhere between “no chance”
and “absolute certainty.” However, this is not necessarily true for p and 1 – p.
Consider the conditions in Figure 19-11:
Figure 19-11  A binomial tree with an early dividend payment.
100.00
3.95
∆ = 52
95.24
.99
∆ = 18
105.00
6.08
∆ = 74
.41
.59
108.25
9.24
∆ = 100
98.00
1.69
∆ = 30
88.70
0
∆ = 0
.59
.41
.59
.41
.41
.59
113.66
13.66
103.10
3.10
102.90
2.90
93.33
0
.41
.59
93.14
0
84.48
0
.41
.59
Dividend
payment
of 2.00
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
--- page 394 ---

B i n o m i a l O p t i o n P r i c i n g 	 377

Stock price S = 100

Time to expiration t = 9 months

Number of periods n = 3

Interest rate r = 4 percent

u = 1.05

d = 1/u = 0.9524
The values for p and 1 – p resulting from these values are 0.59 and 0.41, respectively. But suppose that we are in a high inflationary climate and that instead
of setting r equal to 4 percent, we set r equal to 40 percent. The new values of
p and 1 – p will be
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
0.1)
0.9524
1.05
0.9524
1.51
1 – p = 1 – 1.51 = –0.51
Thus p and 1 – p no longer look like traditional probabilities: p exceeds 1.00,
and 1 – p is negative. In fact, p and 1 – p can fall outside the range for a typical
probability. For this reason, they are sometimes referred to as pseudoprobabilities.
What is the implication of p being greater than 1.00 and 1 – p being less
than 0? This means that the potential for movement in the underlying stock is
not sufficiently large to offset the interest loss should we buy the stock. In our
example with u = 1.05, if the stock price always rises over each time period,
we will show a profit of 5 percent. But with an interest rate of 30 percent, we
Figure 19-12  The value of an American call on a dividend-paying stock.
100.00
4.02
∆ = 53
95.24
1.02
∆ = 19
105.00
6.18
∆ = 73
98.00
1.75
∆ = 31
.41
.59
.41
.59
.41
.59
113.76
13.76
103.00
3.00
93.24
0
84.38
0
108.25
9.26
∆ = 100
88.70
0
∆ = 0
Dividend
payment
of 2.00
.41
.59
.41
.59
.41
.59
All stock prices following the dividend payment
are reduced by the amount of the dividend (2.00)
--- page 395 ---

378
O P T I O N V O L AT I L I T Y A N D P R I C I N G
would always be better off leaving our money in the bank and earning interest
over each three-month time period of
0.30/4 = 7.5%
Of course, if we increase the stock volatility by increasing the value of u, then
the potential profit from investing in the stock will go up. If we choose a large
enough value for u, the values for p and 1 – p will indeed fall between 0 and
1.00. Because the value for u must be greater than 1 + r × t/n, with an interest
rate of 30 percent, u must be greater than
1 + 0.3 × 0.75/3 = 1.075
As we did with the Black-Scholes model, we can use the binomial model to
evaluate options on different underlying instruments. The binomial model and
its variations are shown in Figure 19-13.
How close are option values generated by a binomial model to those generated by the Black-Scholes model? This question only makes sense for European options because the Black-Scholes model cannot be used to evaluate
American options. In our three-period binomial tree, the value of a European
100 call is 5.22, and the value of a 100 put is 2.28. Using the Black-Scholes
If
S  =  the spot price or underlying price

X  =  the exercise price

t   =  the time to expiration, in years

r   =  the domestic interest rate

σ  =  the annualized volatility or standard deviation, in percent

n  =  the number of periods in the binomial tree

u  =  eσ√t/n

d  =  1/u  =  e−σ√t/n

p  =  [ (1 + bt/n) − d ] / [u − d]
Call
1
(1 rt/n)
n!
j!(n
j)! x p (1 p)
x max[Su d
X, 0]
n
j
n j
j
n j
j 0
n
∑
=
+
−
−
−
−
−
=
Put
1
(1 rt/n)
n!
j!(n
j)! x p (1 p)
x max[X
Su d
, 0]
n
j
n j
j
n j
j 0
n
∑
=
+
−
−
−
−
−
=
The variations on the binomial model are determined by the values of r and b.
If
b = r  > 0:
The binomial model for options on stock

b  =  r  =  0 :
The binomial model for options on futures where the options are
subject to futures-type settlement

b = 0 and r  > 0:	 The binomial model for options on futures where the options are
subject to stock-type settlement

b  =  r − rf :
The binomial model for options on foreign currencies, where rf  is the
foreign interest rate
Figure 19-13
(continued)
--- page 396 ---

B i n o m i a l O p t i o n P r i c i n g 	 379
model, the values are 5.01 and 2.05. Both binomial values are greater than
the true Black-Scholes values. We can increase the accuracy of the binomial
model by increasing the number of time periods. In a four-period binomial
tree, the values are 4.79 and 1.84. Figure 19-14 shows the difference between
the Black-Scholes and binomial values for the 100 call as we increase the number of time periods from 1 to 10. We can see that the error oscillates between
positive and negative, with the absolute value of the error becoming smaller
and smaller. Indeed, if we build a tree with an infinite number of time periods, the error will converge to 0. The binomial and Black-Scholes values will
be identical.
How many periods should we use in a binomial model? As we divide the
time to expiration into smaller and smaller increments, we increase the accuracy. But a greater number of periods also increases the number of calculations, and this number increases exponentially. Given the tradeoff between
accuracy and speed, a common choice is often somewhere between 50 and
100 periods.
The accuracy of a binomial calculation can be further increased by taking
the average value generated by two periods, sometimes referred to as half-steps.
For example, the 9-period tree overvalues the 100 call by about 0.07 (Black-
Scholes value – binomial value = –0.07), whereas the 10-period tree undervalues the call by about 0.09. If we take the average of the 9- and 10-period values
(a 9½-period value), the option is undervalued by only 0.01. The results of this
averaging procedure can be seen in Figure 19-14.
The value of an option at any node along the binomial tree is

Ci,j = [ pCi+1,j+1 + (1−p)Ci+1,j ] / (1+rt/n)

Pi,j = [ pPi+1,j+1 + (1−p)Pi+1,j ] / (1+rt/n)
The delta of a call (ΔC) or put (ΔP) at any node along the binomial tree is

ΔCi,j = ( Ci+1,j+1 − Ci+1,j ) / ( Si+1,j+1 − Si+1,j )

ΔPi,j = ( Pi+1,j+1 − Pi+1,j ) / ( Si+1,j+1 − Si+1,j )
The gamma of a call (ΓC) or put (ΓP) at any node along the binomial tree is

ΓCi,j = ( ΔCi+1,j+1 − ΔCi+1,j ) / ( Si+1,j+1 − Si+1,j )

ΓPi,j = (ΔPi+1,j+1 − ΔPi+1,j ) / ( Si+1,j+1 − Si+1,j )
The annual theta of a call (θC) or put (θ P) at any node along the binomial tree is

θCi,j = ( C+i+1,i+2 − Ci,j ) / t

θPi,j = ( P+i+1,i+2 − Pi,j ) / t
Figure 19-13  (continued )
--- page 397 ---

380
O P T I O N V O L AT I L I T Y A N D P R I C I N G
Figure 19-14  As we increase the number of periods, the binomial value converges to the
Black-Scholes value.
0
Black-Scholes value minus binomial value
1
2
3
7
Number of periods in the binomial tree
0
+.04
+.06
+.08
+.02
4
5
6
–.06
–.04
–.02
–.08
10
8
9
Difference between the Black-Scholes call value and binomial call value
Difference between the Black-Scholes call value and average binomial call value
Exercise price = 100
Stock price = 100
Time to expiration = 3 months
Volatility = 9.76%
Interest rate = 4%
--- page 398 ---

381
Volatility Revisited
When a trader enters a volatility into a theoretical pricing model, what exactly
is he feeding into the model? We know the mathematical definition of volatility—
one standard deviation, in percent terms, over a one-year period. Beyond this,
we still have the question of interpretation. Does the number represent a realized volatility or an implied volatility? Are we talking about historical volatility
or future volatility? Long term or short term? The volatility a trader chooses
may vary depending on the answers to these questions.
Consider this situation:

Underlying price = 100.00

Time to expiration = 8 weeks

Interest rate = 0

Implied volatility = 20 percent
Suppose that we buy the 100 straddle at a price equal to its implied volatility of
20 percent, in this case 6.25. The position should be approximately delta neutral because both the 100 call and the 100 put are at the money. After we buy
the straddle, implied volatility rises to 22 percent. How are we doing?
We might instinctively assume that the position will show a profit because the
increase in implied volatility should be a reflection of rising option prices. Indeed, if
there is an immediate increase in implied volatility and all other conditions remain
unchanged, the price of the 100 straddle will rise to 6.87, resulting in a profit of
6.87 – 6.25 = +0.62
But suppose that implied volatility slowly rises to 22 percent over a period of
three weeks. Even though the increase in implied volatility will work in our favor,
the passage of time will cause the options to decay. In fact, with the underlying
contract still at 100.00, the straddle will be worth only 5.43, resulting in a loss of
5.43 – 6.25 = –0.82
The benefits of rising implied volatility were overwhelmed by the costs of
time decay.
20
--- page 399 ---

382
O P T I O N V O L AT I L I T Y A N D P R I C I N G
Now suppose that instead of rising, implied volatility falls to 18 percent.
How will this affect our position? If there is an immediate decline with no
changes in any other market conditions, the price of the 100 straddle will fall to
5.62, leaving us with a loss of
5.62 – 6.25 = –0.63
But suppose that as implied volatility falls to 18 percent, the underlying
price is also changing. We are now benefiting from a positive gamma. If the
underlying price rises immediately to 105.00, the 100 straddle will be worth
7.09, resulting in a profit of
7.09 – 6.25 = +0.84
If the underlying price moves in the other direction and falls immediately to
95.00, the straddle will be worth 6.87, now resulting in a profit of
6.87 – 6.25 = +0.62
The disadvantages of falling implied volatility were more than offset by the
benefits of movement in the underlying stock price.
This example illustrate an important principle of option trading:
The longer an option position is held, the more important is the realized volatility of
the underlying contract and the less important is the implied volatility. If a position
is held to expiration, realized volatility is the only consideration.
We saw this principle at work in Chapter 8 on dynamic hedging. The deltaneutral adjustment process eventually determined whether a position would
show a profit or loss, irrespective of any changes in implied volatility. This is
not to say that implied volatility is unimportant; prices are always important
because they will often determine interim cash flows and capital requirements.
But, in order to make sensible trading decisions, we need to know value as well
as price. In the final analysis, the value of an option position will be determined
by the volatility of the underlying contract.
Determining the right volatility input can be a difficult and frustrating exercise, even for an experienced option trader. The forecasting of directional price
movements, either through fundamental or technical analysis, is a commonly
studied area in trading, and there are many sources to which a trader can turn for
information on these subjects. Unfortunately, volatility is a much newer concept,
and there is less to guide a trader. In spite of this difficulty, an option trader must
make some effort to come up with a reasonable volatility input if he intends to
use a theoretical pricing model to make trading decisions and manage risk.
Historical Volatility
Because the realized volatility over the life of an option will eventually dominate any changes in implied volatility, we will certainly want to give some
thought to how we might predict future realized volatility. Such a prediction
--- page 400 ---

V o l at i l i t y R e v i s i t e d 	 383
will often begin by looking at historical volatility data. How should we calculate
historical volatility?
We know that volatility represents a standard deviation. Two methods are
commonly used to calculate a standard deviation, either
x
n
x
n
(
)
or
(
)
1
i
i
n
i
i
n
2
1
2
1
∑
∑
µ
−µ
−
−
=
=
In each case, xi are the data points, μ is the mean of all data points, and n is the
total number of data points. The only difference between the two methods is
the denominator, either n or n – 1.
If we want to know the standard deviation of an entire population of data
points, we can use the first method, dividing by n. This is known as the population standard deviation. Suppose, however, that we have a sample set of data
points from a larger population, and we want to use this sample to estimate
the standard deviation of the entire population. Because our sample is limited, we are likely to miss some of the more extreme data points in the larger
population. For this reason, our estimate of the standard deviation for the entire population is likely to be too low. To improve our estimate, we ought to increase the standard deviation calculation. This is commonly done by reducing
the size of the denominator from n to n – 1, resulting in a sample standard deviation of the larger population. Because historical volatility is most often used to
estimate a future volatility, historical volatility calculations are most often
made using the sample standard deviation, that is, dividing by n – 1.
The data points xi in a volatility calculation are the price returns, either the
percent change in the underlying price from one time period to the next
p
p
p
n
n
n
1
−
−
or, more commonly, the logarithmic change
p
p
ln
n
n 1
−
Time periods may be any length, but for exchange-traded contracts, returns
are usually based on the price change from one day’s settlement to the next.
In the standard deviation calculation, μ (the Greek letter mu) is the average of all price returns. Because the volatility is the deviation from average,
if a contract goes up 1 percent each day for 10 consecutive days, its volatility over the 10-day period is 0; the price change never deviated from its average. To most traders, this feels wrong. The upward moves of 1 percent ought
to represent some volatility other than 0. In fact, most historical volatility calculations use a zero-mean assumption: μ is always assumed to be 0 regardless of
the actual mean.
