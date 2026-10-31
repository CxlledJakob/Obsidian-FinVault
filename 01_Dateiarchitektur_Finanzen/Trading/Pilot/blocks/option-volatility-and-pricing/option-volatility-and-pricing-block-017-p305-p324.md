# Option Volatility and Pricing_ Advanced Trading Strategies -- Sheldon Natenberg -- 2nd ed, 2014 -- McGraw Hill Professional -- isbn13 9780071818773 -- 6a48d008bd9beef283debf7bad0b2e4a -- Anna’s Archive.pdf — pages 305–324

--- page 305 ---

288
O P T I O N V O L AT I L I T Y A N D P R I C I N G
In this case, the time box is a combination of buying the August 90/100 box
and selling the June/August 90 roll.
From the foregoing examples, we can see that if we buy a long-term box
and sell a lower-exercise-price roll or buy a short-term box and sell a higherexercise-price roll, both combinations result in the same time box. We can confirm this by calculating the value of the June and August 90/100 boxes as well
as the June/August 90 and 100 rolls
=
+
×
=
June 90/100 box
10
1
0.06
2/12
9.90
=
+
×
=
August 90/100 box
10
1
0.06
4/12
9.80
=
+
×
−+
×
−
=
June/August 90 roll
90
1
0.06
2/12
90
1
0.06
4/12
0.40
0.47
=
+
×
−+
×
−
=
June/August 100 roll
100
1
0.06
2/12
100
1
0.06
4/12
0.40
0.57
If we buy the June 90/100 box and sell the June/August 100 roll, the total
value is
–9.90 + .57 = –9.33
If we buy the August 90/100 box and sell the June/August 90 roll, the total
value is
–9.80 + .47 = –9.33
The total in both cases is equal to the value of the time box.
Using Synthetics in Volatility Spreads
Any mispriced arbitrage relationship will be quickly recognized by almost all
traders. Consequently, there are few opportunities to profit from a mispriced
conversion or reversal. When a mispricing does arise, it is likely to be small and
very short-lived. Only a professional trader, who has low transaction costs and
immediate access to markets, is likely to be able to profit from such a situation.
But even if a trader does not intend to execute an arbitrage,  he may be able to
use a knowledge of arbitrage pricing relationships to execute a strategy at more
favorable prices.
In Chapter 14, we noted that because there is a synthetic equivalent for
every contract, there are three ways to buy a straddle:
1.	 Buy a call, buy a put.
2.	 Buy a call, buy a put synthetically (buy two calls, sell an underlying
contract)
3.	 Buy a call synthetically, but a put (buy two puts, buy an underlying
contract)
--- page 306 ---

O p t i o n A r b i t r a g e 	 289
Suppose that we have the following prices for a call, a put, and an underlying stock:
Bid
Offer
Stock
51.45
51.50
50 call
4.10
4.20
50 put
2.35
2.40
If there are three months remaining to expiration, interest rates  are 4.00 percent, and we expect the stock to pay a dividend of .25 prior to expiration, what
is the best way to buy the 50 straddle?
Assuming that we must sell at the bid price and buy at the offer price, if we
buy the straddle outright, we will pay a total of 4.20 + 2.40 = 6.60. Suppose,
however, that we  buy the put synthetically (i.e., buy the call, sell the underlying). How much are we actually paying for the put?
Recall the approximation for put-call parity for stock options
Call price – put price = stock price – exercise price

+ interest on exercise price – expected dividends
If we buy the put synthetically, we will have to pay 4.20 for the call and sell the
stock at 51.45. Therefore,
4.20 – ?? = 51.45 – 50 + 50 × .04 × 3/12 – .25 = 1.70
The cost of buying the put synthetically must be 2.50. This is higher than the
actual price of 2.40, so this is a worse choice than buying the straddle outright.
What about buying the call synthetically (i.e., buy the put, buy the underlying)? We will pay 2.40 for the put and 51.50 for the stock. This gives us
?? – 2.40 = 51.50 – 50 + 50 × .04 × 3/12 – .25 = 1.75
The synthetic call price is 4.15. This is in fact better than the actual call price
of 4.20. If we buy the straddle synthetically, buying two calls and buying stock,
we are paying a total of 4.15 + 2.40 = 6.55, or .05 better than buying the straddle outright.
How important is a savings of .05? That probably depends on several
factors—the size in which the spread will be done, the liquidity of the market,
and execution costs and brokerage fees. A professional trader, who has very
low transaction costs and tends to trade in large volumes, ought to be very
happy to save .05. On the other hand, a retail customer may find that the outright straddle, because it involves only two contracts rather than three, entails
lower transaction costs and can be executed more easily in the marketplace.
It might be a better practical choice, even if it means giving up a potential
savings of .05.
It might seem that when we are able to trade a contract synthetically at a
better price than the actual price, there must an arbitrage opportunity available.
--- page 307 ---

290
O P T I O N V O L AT I L I T Y A N D P R I C I N G
But in our example no arbitrage opportunity exists. If we do a conversion (i.e.,
sell call, buy put, buy stock), the put-call parity calculation is

4.10 – 2.40 = 51.50 – 50 + 50 × .04 × 3/12 – .25

1.70 = 1.75
We will be selling stock, synthetically, at 1.70 and buying at 1.75.
If we instead do a reverse conversion (i.e., buy call, sell put, sell stock), the
calculation is

4.20 – 2.35 = 51.45 – 50 + 50 × .04 × 3/12 – .25

1.85 = 1.70
Now we are buying stock, synthetically, at 1.85 and selling at 1.70. Because we
must buy at the bid and sell at the offer, no arbitrage is available in either case.
Our goal, however, was a volatility spread, not an arbitrage. And the bid-ask
spreads were such that we were able to buy the straddle synthetically at a savings of .05.
Let’s expand the number of options and consider a different example:
Bid
Offer
45 call
7.40
7.55
45 put
0.70
 0.75
50 call
4.10
4.20
50 put
2.35
2.40
55 call
1.95
2.00
55 put
5.10
5.25
If, as before, there are three months remaining to expiration and interest rates
are 4 percent, what is the best way to buy the 45/50/55 butterfly?
We might begin by comparing the prices of the call and put butterflies. We
know that these are equivalent strategies and ought to have the same prices.

Call butterfly:

  Buy one 45 call
–7.55

  Sell two 50 calls
+8.20

  Buy one 55 call
–2.00

–1.35

Put butterfly:

  Buy one 45 put
–0.75

  Sell two 50 puts
+4.70

  Buy one 55 put
–5.25

–1.30
Buying the put butterfly is slightly better than buying the call butterfly.
--- page 308 ---

O p t i o n A r b i t r a g e 	 291
In addition to buying the call or put butterfly, we have a third choice—we
can sell an iron butterfly. In Chapter 14, we noted that selling an iron butterfly
(i.e., buy a strangle and sell a straddle) is equivalent to buying a butterfly. Moreover, the value of the iron butterfly and the value of an actual butterfly must
add up to the present value of the amount between exercise prices. In our example, the values must add up to
5.00/(1 + .04 × 3/12) = 4.95
Therefore, paying 1.30 for the put butterfly is the same as selling the iron butterfly for 4.95 – 1.30 = 3.65. At what price can we sell the iron butterfly?

Iron butterfly:

  Buy one 45 put
–0.75

  Buy one 55 call
–2.00

  Sell one 50 put
+2.35

  Sell one 50 call
+4.10

+3.70
If buying the put butterfly for 1.30 is equivalent to selling the iron butterfly for
3.65, then selling the iron butterfly at a price of 3.70 must be .05 better. This, in
theory, seems to be the best way to buy the 45/50/55 butterfly.
Even though selling the iron butterfly is best in theory, other factors, such
as ease of execution and transaction costs, may play a role. Everything else being equal, though, selling the iron butterfly for 3.70 is the best way to execute
our butterfly strategy.
The relationship between the prices of call butterflies, put butterflies, and
iron butterflies is based on synthetic relationships—the ability to express any
contract as a synthetic equivalent. The reader may wish to confirm that no arbitrage opportunities exist, either in the form of conversions, reverse conversions, or boxes. Our goal, however, was not to take advantage of an arbitrage
opportunity but rather to find the best price at which to buy a butterfly. Our
knowledge of synthetic pricing relationships enabled us to do this.
Figure 15-3 is a summary of basic arbitrage pricing relationships. Whenever a trader is considering a strategy, he ought to always ask whether he can do
better by executing some part of his strategy synthetically. Usually this will not
be possible because synthetic relationships tend to be very efficient. Occasionally, though, the trader will find that the synthetic position is slightly more favorable. And over a career of trading, even small savings can add up.
--- page 309 ---

292
O P T I O N V O L AT I L I T Y A N D P R I C I N G
Figure 15-3  Summary of arbitrage relationships for European options.
Note:  Calculations exclude interest on dividends.
C=call price    P=put price    F=underlying futures price    S=underlying stock price    X=exercise price
r=annual interest rate    t=time to expiration in years    D=expected dividends
simple interest
continuous interest
approximation
put-call parity:
C − P = (F−X)/(1+rt)
C − P = (F−X)e−rt
C − P = S − X/(1+rt) − D
C − P = S − Xe−rt − D
C − P ≈ S − X + Xrt − D
box value:
Xl = lower exercise price
Xh = higher exercise price
(Xh−Xl)/(1+rt)      (Xh−Xl)e−rt      (Xh−Xl) − (Xh−Xl)rt
long box = long (bull) call spread  +  long (bear) put spread
roll value for stock options:
tl = time to expiration
      for long-term option
ts = time to expiration
      for short-term option
D = expected dividends
      between expirations
X/(1+rsts) − X/(1+rltl) − D      Xe−rsts − Xe−rltl − D      X(tl−ts)r − D
long roll = long call calendar spread  +  short put calendar spread
time box (diagonal roll)
               for stock options:
Xs/(1+rsts) − Xl/(1+rltl) − D
Xse−rsts − Xl
e−rltl − D
time box value  =  long-term box  −  lower exercise price roll
                                       =  short-term box  −  higher exercise price roll
--- page 310 ---

293
Early Exercise of
American Options
Thus far we have assumed that all option strategies involve holding a position
to expiration. Because many exchange-traded options are American, carrying
with them the right of early exercise, it will be worthwhile to consider some of
the characteristics of American options. Specifically, we will want to answer
three questions:
1.	 Under what circumstances might a trader consider exercising an
American option prior to expiration?
2.	 If early exercise is deemed desirable, is there an optimal time to do so?
3.	 How much more should a trader be willing to pay for an American
option over an equivalent European option?
In order for early exercise to be desirable, there must be some advantage
to holding a position in the underlying contract rather than a position in the
option contract. This advantage can come in the form of dividends that the
owner of stock will receive or in the form of a positive cash flow on which interest can be earned. If there are no dividend or interest considerations, there is
no value to early exercise. In that case,
value of an American option = value of a European option
This is generally true for options on futures traded on exchanges outside the
United States, where the options are subject to futures-type settlement. Futures contracts do not pay dividends, and no cash flow takes place when either
the underlying futures contract or options on that contract are traded. Even
though the options may be American, there is effectively no early exercise value
associated with such options.
16
--- page 311 ---

294
O P T I O N V O L AT I L I T Y A N D P R I C I N G
Arbitrage Boundaries
When evaluating a contract, a trader might try to determine an arbitrage boundary for that contract—the lowest price (the lower arbitrage boundary) or highest
price (the upper arbitrage boundary) at which the contract can trade without
there being some arbitrage opportunity. Identifying the arbitrage boundaries
for European and American options can help us  understand the early exercise
criteria for American options.
Consider these prices:
Contract
Price
June 90 call
9.90
Underlying contract
100.00
If the June 90 call is American, everyone will want to buy the call for 9.90, sell
the underlying contract for 100.00, and immediately exercise the option. The
resulting cash flow will be

Buy the June 90 call
    –9.90

Sell the underlying contract
+100.00

Exercise the call
   –90.00

Total profit and loss (P&L)
     +.10
There is an arbitrage profit of  0.10.
Now consider these prices:
Contract
Price
June 70 put
4.80
Underlying contract
65.00
If the June 70 put is American, everyone will want to buy the put for 4.80, buy
the underlying contract for 65.00, and immediately exercise the option. The
resulting cash flow will be

Buy the June 70 put
  –4.80

Buy the underlying contract
–65.00

Exercise the put
+70.00

Total P&L
  +0.20
There is an arbitrage profit of 0.20.
We can conclude from these examples that an American option should
never trade for less than intrinsic value. If it does, everyone will buy the option,
hedge the position with the underlying contract, and exercise the option, all of
which will result in an immediate arbitrage profit. We can express the lower arbitrage boundary for an American option as

For a call:
At least the maximum of [0, S – X ]

For a put:
At least the maximum of [0, X – S ]
where X is the exercise price, and S is the price of the underlying contract.
--- page 312 ---

E a r ly E x e r c i s e o f A m e r i c a n   O p t i o n s 	 295
We have included the qualifier at least for both calls and puts because, as we
will see, the lower arbitrage boundary for an American option may in fact be
greater than intrinsic value. For the present, we will simply say that it cannot be
less than intrinsic value.
To determine the lower arbitrage boundary for a European option, we can
use put-call parity
−
=
−
+ ×
C
P
F
X
r
t
1
The lowest possible price for a put is 0, so the lower arbitrage boundary for a
European call must be
C
F
X
r
t
1
≥
−
+ ×
where F is either the price of an underlying futures contract or the forward
price for an underlying stock.
For a futures option, the lower arbitrage boundary for a call is the present
value of the intrinsic value. This means that if European options on futures are
subject to stock-type settlement, the lower arbitrage boundary will always be
less than  intrinsic value because the present value must be less than  intrinsic
value.
For example,

Futures price = 1,167.00

Time to expiration = 6 months

Interest rate = 4.00 percent
If options are subject to stock-type settlement, the lower arbitrage boundary
for the 1,100 call is
−
+
×
=
1,167.00
1,100
1
0.04
6/12
65.69
Even though the intrinsic value is 67.00, the lower arbitrage boundary is 65.69.
For stock options, if we replace F with the forward price for the stock and
we ignore interest on dividends, the lower arbitrage boundary for a European
call is
C
S
X
r
t
D
(1
)
≥
−
+ ×
−
A stock option call cannot trade for less than the stock price minus the discounted value of the exercise price less dividends. This means that the lower
arbitrage boundary for an out-of-the-money stock option call can be greater
than 0. For example,

Stock price
=	49.50

Time to expiration	 =	6 months

Interest rate
=	4.00 percent

Dividend
=	0
A 50 call, even though it is out of the money, has a lower arbitrage boundary of
−
+
×
=
49.50
50
1
0.04
6/12
0.48
--- page 313 ---

296
O P T I O N V O L AT I L I T Y A N D P R I C I N G
If the call is trading for less than 0.48, say, 0.40, we can buy the call, sell the
stock, and exercise the call at expiration. The cash flows will be

Buy the 50 call
 –0.40

Pay interest on the call price (0.40 × 0.04 × 6/12)
  –0.01

Sell stock
+49.50

Collect interest on the stock price (49.50 × 0.04 × 6/12)	  +0.99

Exercise the call at expiration
–50.00

Total P&L
  +0.08
This is exactly the difference between the call price of 0.40 and the lower arbitrage boundary of 0.48.
In this example, we can be certain of an arbitrage profit of at least 0.08 because we know that we can close out the position at expiration by exercising the
call, thereby purchasing the stock back at a price no higher than 50. Suppose,
however, that the stock price at expiration is less than 50. Instead of exercising
the call, we can purchase the stock at its market price. This will result in an even
greater profit than 0.08. The lower arbitrage boundary tells us the price below
which there is an arbitrage opportunity and at the same time determines the
minimum amount that can be made. The maximum amount can be even greater
if at expiration the stock is trading at a price below the exercise price.
What is the lower arbitrage boundary for the 50 call if it is an American
option? We might assume that it must be 0 because the option is out of the
money, and no one would ever exercise an out-of-the-money option. But early
exercise is a right, not an obligation. We can convert an American option into
a European option simply by choosing not to exercise it early. The lower arbitrage boundary for an American option is therefore at least intrinsic value.
If the lower arbitrage boundary for an equivalent European option is greater
than intrinsic value, as it is in this example, then this number also serves as the
lower arbitrage boundary for the American option:
American call ≥ maximum [0, S – X, (F – X)/(1 + r × t)]
In this example, the lower arbitrage boundary for the 50 call is 0.48 regardless
of whether the option is European or American.
Let’s change our example slightly:

Stock price = 49.50

Time to expiration = 6 months

Interest rate = 4.00 percent

Dividend = 0.65 payable every three months (total dividend of 1.30)
What is the lower arbitrage boundary for a European 45 call?
−
+
×
−
=
49.50
45
1
0.04
6/12
1.30
4.08
If the call is American, its intrinsic value (49.50 – 45 = 4.50) is greater than the
European value of 4.08. Therefore, the lower arbitrage boundary for an American 45 call is 4.50.
--- page 314 ---

E a r ly E x e r c i s e o f A m e r i c a n   O p t i o n s 	 297
By reversing F and X, we can use put-call parity to determine the lower arbitrage boundary for a European put
≥
−
+ ×
P
X
F
r
t
1
As with a futures option call, the lower arbitrage boundary for a European put
is the present value of the intrinsic value.
For stock options, we can replace F with the stock forward price, giving us
the lower arbitrage boundary for a put
≥
+ × −
+
P
X
r
t
S
D
1
A stock option put cannot trade for less than the discounted value of the exercise price minus the stock price plus dividends.

Stock price = 49.50

Time to expiration = 6 months

Interest rate = 4.00 percent

Dividend = 0
The lower arbitrage boundary for a European 50 put must be 0 because
+
×
−
= −
50
1
0.04
6/12
49.50
.48
If, however, the option is American, the lower arbitrage boundary will be the
option’s intrinsic value of 0.50.
Because we can always turn an American put into a European put
simply by choosing not to exercise it, the lower arbitrage boundary for an
American put is
American put ≥ maximum [0, X – S, (X – F)/(1 + r × t)]
Because the lower arbitrage boundary for European options is a function
of time, interest rates, and, in the case of stock, dividends, as time passes, the
boundary is constantly changing. For futures options that are subject to stocktype settlement, the boundary is always rising because the present value is always rising toward intrinsic value. For stock options, however, the boundary
may rise or fall depending on whether the forward price is greater than or less
than the cash price. If the forward price is greater than the cash price (interest
is greater than dividends), the lower arbitrage boundary will rise for calls and
fall for puts. If the forward price is less than the cash price (interest is less than
dividends), the boundary will fall for calls and rise for puts. A graphic representation of these changes is shown in Figures 16-1 through 16-4.
If the lower arbitrage boundary for a European option is less than intrinsic
value, a European option can, in some cases, be worth less than intrinsic value.
When this occurs, as time passes, the value of the option will rise toward intrinsic value. As a consequence, the option will have a positive theta. This was discussed in Chapter 7 and shown graphically in Figure 7-9.
--- page 315 ---

298
O P T I O N V O L AT I L I T Y A N D P R I C I N G
Figure 16-1  Lower arbitrage boundary for a European call on futures (stock-type
settlement).
As time passes, the boundary
rises toward intrinsic value.
Intrinsic value:
F – X
Lower arbitrage boundary:
(F – X) / (1 + r × t)
Higher futures prices
Lower futures prices
X
0
Figure 16-2  Lower arbitrage boundary for a European put on futures (stock-type
settlement).
Higher futures prices
Lower futures prices
As time passes, the boundary
rises toward intrinsic value.
Intrinsic value:
X – F
Lower arbitrage boundary:
(X – F) / (1 + r × t)
X
0
--- page 316 ---

E a r ly E x e r c i s e o f A m e r i c a n   O p t i o n s 	 299
Figure 16-3  Lower arbitrage boundary for a European call on stock.
Lower arbitrage boundary
if F < S
As time passes, the boundary
moves toward intrinsic value.
Lower arbitrage boundary
if F > S
X/(1 + r × t) + D
if F > S
X/(1 + r × t) + D
if F < S
Intrinsic value
S – X
Higher stock prices
Lower stock prices
X
0
Figure 16-4  Lower arbitrage boundary for a European put on stock.
As time passes, the boundary
moves toward intrinsic value.
Intrinsic value
X – S
Lower arbitrage
boundary if F > S
Lower arbitrage
boundary if F < S
X/(1 + r × t) + D
if F > S
X/(1 + r × t) + D
if F < S
Higher stock prices
Lower stock prices
X
0
--- page 317 ---

300
O P T I O N V O L AT I L I T Y A N D P R I C I N G
Although traders are primarily interested in the lower exercise boundary
for an option, for completeness, we might also want to determine the upper arbitrage boundary for an option. Because the underlying contract cannot fall
below 0, the upper arbitrage boundary for an American put, whether on futures or stock, must be the exercise price. For a European put, which is subject
to stock-type settlement, the upper boundary is the present value of the exercise price

American put ≤ X

European put ≤ X /(1 + r × t)
To determine the upper arbitrage boundary for a call, we can use put-call
parity
−
=
−
+ ×
C
P
F
X
r
t
1
We know that the maximum value for a European put is X/(1 + r × t). Therefore, the maximum value for a European call is
C
F
X
r
t
X
r
t
F
r
t
1
1
1
≤
−
+ × + + ×
=
+ ×
A European call on a futures contract has a maximum value equal to the futures price discounted by interest. If options are subject to futures-type settlement, the maximum value is simply the price of the underlying futures
contract.
For a European call on stock, we can replace F with the forward price for
stock S × (1 + r × t) – D
≤
×
+ ×
−
−
+ ×
+ + ×
C
S
r
t
D
X
r
t
X
r
t
(1
)
1
1
Ignoring interest on dividends gives us
≤
−
−
+ ×
+ + ×
=
−
C
S
D
X
r
t
X
r
t
S
D
1
1
A European call on stock has a maximum value equal to the stock price less
dividends. An American call has a maximum value equal to the stock price. A
summary of arbitrage boundaries is shown in Figure 16-5.
Early Exercise of Call Options on Stock
Under what conditions might we choose to exercise an American call option on
stock prior to expiration? To answer this question, let’s think about the components that make up the value of a call.
Clearly, if we are considering exercising an option, it must be in the money.
Therefore, one component must be intrinsic value. A call also offers some protective value over a stock position because the call’s loss is limited by the exercise
price. The likelihood that the stock will fall below the exercise price depends on
the volatility, so we might refer to this protective value as volatility value. As volatility rises, we are willing to pay more for the call. The call also includes some
--- page 318 ---

E a r ly E x e r c i s e o f A m e r i c a n   O p t i o n s 	 301
interest-rate value. As interest rates rise, the call becomes a more desirable substitute for holding a stock position. Finally, there is dividend value. But unlike volatility value and interest value, both of which increase the value of the call, the
dividend reduces the value of the call. Therefore,
Call value =  intrinsic value + volatility value + interest value – dividend value
Suppose that we are able determine the value of each of these components
and find that the dividend value is greater than the combined volatility value
and interest value
Dividend value > volatility value + interest value
In this case, the value of the call will be less than intrinsic value. And, indeed,
European options can, in some cases, trade for less than intrinsic value. But,
if the call is American, it becomes an early exercise candidate because we can
collect the intrinsic value now by simultaneously exercising the call and selling
the stock.
How can we estimate the value of the volatility, interest-rate, and dividend
components? The dividend component is simply the total dividend the stock is
expected to pay over the life of the option. The interest value must be the interest that we would have to pay if we were to sell the call and buy the stock and
carry this position to expiration. If the call is deeply in the money, its value will
be very close to intrinsic value, and the total cash flow will be approximately
equal to the exercise price
Intrinsic value = stock price – exercise price
We might reach the same conclusion by observing that if we exercise the call,
we will have to pay the exercise price. The interest value must be the approximate cost of carrying the exercise price to expiration.
The volatility component is somewhat more difficult to determine. But
we know that the volatility value depends on the likelihood of the stock price
Lower Arbitrage Boundary
American
European
Options on futures
(stock-type settlement)
Call
Put
max[0, F − X]
max[0, X − F]
max[0, (F − X)/(1 + r × t)]
max[0, (X − F)/(1 + r × t)]
Options on stock
Call
Put
max[0, S − X, S − X/(1 + r × t) − D]
max[0, X − S, X/(1 + r × t) − S + D]
max[0, S − X/(1 + r × t) − D]
max[0, X/(1 + r × t) − S + D]
Upper Arbitrage Boundary
American
European
Options on futures
(stock-type settlement)
Call
Put
F
X
F/(1 + r × t)
X/(1 + r × t)
Options on stock
Call
Put
S
X
S − D
X/(1 + r × t)
Figure 16-5  Summary of arbitrage boundaries.
--- page 319 ---

302
O P T I O N V O L AT I L I T Y A N D P R I C I N G
falling below the exercise price. The value of the companion put (the put
with the same exercise price and expiration date as the call) must be a good
estimate of this value. We know from put-call parity that the vegas of calls
and puts with the same exercise price and expiration date are the same—they
have the same sensitivity to changes in volatility. Therefore, their volatility
values ought to be the same.1
For example, consider the following:

Stock price = 100

Time to expiration = 1 month

Interest rate = 6.00 percent

Dividend = 0.75, payable in 15 days
Is the 90 call an early exercise candidate if the price of the 90 put is 0.20?
We know the dividend value (0.75) and the volatility value (0.20), so the
only component we need to calculate is the cost of carrying the exercise price
to expiration
90 × .06 × 1/12 = .45
The early exercise criteria are satisfied because
Dividend value > volatility value + interest value
0.75 > 0.20 + 0.45 = 0.65
In Figure 16-6 we can see why the 90 call has become an early exercise
candidate—its European value has fallen below intrinsic value.2 If given the
choice between exercising now or carrying the option position to expiration,
we will come out ahead by 0.10 if we exercise now.
But are those our only two choices—exercise now or not at all? An American option can be exercised at any time prior to expiration. Instead of exercising today, what about exercising the option tomorrow? Or the day after that?
Suppose that we exercise today instead of exercising tomorrow. What
will we gain, and what will we lose? We will lose one day’s worth of volatility
value. We will also lose one day’s worth of interest on the exercise price. In
return, we get . . . nothing. We are exercising to get the dividend. But the dividend will not be paid for 15 days. Because we always give up some volatility
value and some interest value when we exercise an American call option on
stock prior to expiration, the only time we will consider exercising the option
early is the day before the stock pays the dividend. On no other day will early
exercise be optimal.
1 Although the companion put also has some interest and dividend value, these components will tend to be small.
Changing interest rates or dividends will cause the forward price to change, which is similar to changing the underlying price. But the put, with its small delta, will be relatively insensitive to these changes. Consequently, the out-ofthe-money put has only a small interest-rate and dividend value. There is no sensitivity measure for dividends, but
we can confirm that the put is relatively insensitive to changes in interest rates by noting that an out-of-the-money
option has a small rho value compared with an in-the-money option.
2 Figure 16-6 is clearly not drawn to scale. The point at which the European lower arbitrage boundary graph bends
appears to be halfway between 90 and 100. The actual point is X/(1 + r × t) + D = 90/(1 + 0.06/12) + 0.75 =
90.30.
--- page 320 ---

E a r ly E x e r c i s e o f A m e r i c a n   O p t i o n s 	 303
For an American call option on stock to be an early exercise candidate, the
early exercise criteria must hold true over the entire life of the option
Dividend value > volatility value + interest value
But, for an option to be an immediate early exercise candidate, this condition
must also hold true over the next day. For a call option on stock, the only day
on which a trader need consider early exercise is the day before the stock pays
a dividend. Indeed, if a stock pays no dividend over the life of the option, there
is never any reason to exercise the call prior to expiration.
Early Exercise of Put Options on Stock
Under what conditions might we choose to exercise an American put option on
stock prior to expiration? Just as we separated the value of a stock option call
into its components, we can do the same with a stock option put. Again, we begin with the intrinsic value. To this, we can add the volatility value—the protective value afforded by the put in the event that the stock price rises above the
exercise price. There will also be interest value—if we exercise the put, we will
collect interest on the exercise price. Finally, there will be some dividend value.
Put value = intrinsic value + volatility value – interest value + dividend value
Note that volatility value and dividend value increase the value of the
put, while the interest value reduces the put’s value. Suppose that we are able
Figure 16-6
S
(100.00)
European lower
arbitrage boundary
American lower
arbitrage boundary
(intrinsic value)
At a stock price of 100.00, the
European value of the 90 call
is less than the intrinsic value.
European
theoretical value
X
(90) X/(1 + r × t) + D
Higher stock prices
Lower stock prices
0
--- page 321 ---

304
O P T I O N V O L AT I L I T Y A N D P R I C I N G
to determine the value of each of these components and find that the interest
value is greater than the combined volatility value and dividend value
Interest value > volatility value + dividend value
If this is true, the value of the option will be less than intrinsic value. But, if the
option is American, it becomes an early exercise candidate because we can collect the intrinsic value right now by exercising the put.
We can estimate the value of these components in the same way we estimated them for a call. The interest value is the amount of interest we will earn on
the exercise price to expiration if we exercise the put. The dividend value is the
total dividend the stock is expected to pay over the life of the option. The volatility value is approximately the price of the companion out-of-the-money call.
Consider this situation:

Stock price = 100

Time to expiration = 2 months

Interest rate = 6.00 percent

Dividend = 0.40
Is the 120 put an early exercise candidate if the price of the 120 call is 0.55?
We know the volatility value (0.55) and dividend value (0.40). The interest
on the exercise price to expiration is
120 × .06 × 1/6 = 1.20
The early exercise criteria are satisfied because

Interest value > volatility value + dividend value

1.20 > .55 + .40 = .95
We can see in Figure 16-7 that at a stock price of 100, the value of the
European 120 put falls below intrinsic value, making the put an early exercise
candidate. If given the choice between exercising now or carrying the option
position to expiration, we will come out ahead by 0.25 if we exercise now.3
As with a call, for a put to be an immediate early exercise candidate, the
early exercise criteria must hold true not only over the entire life of the option but also over the next day. We will exercise today only if we expect to gain
more over the next day through early exercise than we lose. Will this be true
for our 120 put?
Suppose that the dividend of 0.40 will be paid tomorrow. If we exercise today instead of tomorrow, we will gain one day’s worth of interest
120 ×0.06/365 = 0.02
In return, we are giving up one day’s worth of volatility value as well as the
value of the dividend. Even if we assume that the volatility value is negligible,
3 Figure 16-7, like Figure 16-6, is not drawn to scale. The point at which the European lower arbitrage boundary
graph bends is X/(1 + r × t) + D = 120/(1 + 0.06/6) + 0.40 = 119.21.
--- page 322 ---

E a r ly E x e r c i s e o f A m e r i c a n   O p t i o n s 	 305
the dividend of 0.40 that we will lose is far greater than the interest of 0.02
that we will earn. Clearly, we should wait one day before exercising the option,
foregoing one day’s worth of interest but retaining the value of the dividend.
Suppose that the dividend will be paid two days from now. If we exercise
today instead of waiting until the dividend is paid, we will earn two days’ worth
of interest, 0.04, but we will still lose the dividend of 0.40. Waiting two days to
exercise is still a better strategy.
When should we exercise a put early? Because a trader will not want to
give up the value of the dividend, the most common day on which to exercise a
stock option put early is the day on which the stock pays the dividend. But unlike stock option calls, where the only day on which the option ought to be exercised early is the day before the stock pays the dividend, a stock option put
might be exercised any time prior to expiration. Early exercise will be optimal
if the interest that can be earned is greater than the combined volatility and
dividend value.
Ignoring the volatility value, we can see that no trader will exercise a put
early if the total interest that can be earned is less than the dividend. In our
example, where we expect to earn 0.02 in interest per day, early exercise can
never be optimal if the dividend will be paid within the next 20 days because
0.40/.02 = 20
With fewer than 20 days to the dividend payment, we can never earn enough
interest to offset the loss of the dividend. For put options, this blackout period can
be easily calculated by dividing the dividend by the daily interest that can be
earned on the exercise price. During this period, no knowledgeable trader will
Figure 16-7
At a stock price of 100.00, the
European value of the 120 put
is less than the intrinsic value.
European
theoretical value
American lower
arbitrage boundary
(intrinsic value)
European
lower
arbitrage
boundary
S
(100.00)
X
(120)
X/(1 + r × t) + D
Higher stock prices
Lower stock prices
0
--- page 323 ---

306
O P T I O N V O L AT I L I T Y A N D P R I C I N G
exercise a put because the loss of the dividend will be greater than the total interest earned.
Blackout Period – the period prior to the ex-dividend date during which it is impossible
to earn enough interest through early exercise of a put to offset the loss of the dividend.
ex-dividend
date
blackout period
?
number of days in the blackout period =
dividend/(exercise price × interest rate/365)
time
This does not mean that a put should never be exercised prior to the dividend payment. In our example, if the dividend will be paid in 30 days and we exercise now, we will earn 30 days’ worth of interest, that is, 30 × 0.02 = 0.60. This
is greater than the 0.40 value of the dividend. As long as the volatility value over
the next 30 days is less than 0.20, immediate early exercise is a sensible choice.
Impact of Short Stock on Early Exercise
Interest rates are an important factor in deciding whether to exercise a stock
option early. If we reduce interest rates, calls are more likely to be exercised
early (early exercise results in a smaller interest loss), and puts are less likely to
be exercised early (early exercise results in smaller interest earnings). Because a
short stock position entails a lower interest rate (the rate is reduced by the borrowing costs), a trader who has a short stock position is more likely to exercise a
call option early. At the same time, a trader who does not already own stock will
be less likely to exercise a put option early. This is consistent with the general
rule that we proposed in Chapter 7:
Whenever possible, a trader should avoid a short stock position.
If a trader is carrying a short stock position, exercise of a call will reduce or
eliminate this position. If a trader is carrying no stock position, exercise of a
put will result in a short stock position. In the former case, a call is more likely
to be exercised early;  in the latter case, a put is less likely to be exercised early.
Early Exercise of Options on Futures
What happens when we exercise a futures option? Exercise of a call option enables us to buy the underlying futures contract at the exercise price. Exercise
of a put option enables us to sell the underlying futures contract at the exercise
price. Because the futures contract is subject to futures-type settlement, there
will be a variation credit equal to the option’s intrinsic value, the difference between the exercise price and the price of the futures contract. If the option is
subject to futures-type settlement, exercise will cause the option to disappear,
and we will be debited by an amount equal to the option’s value. Assuming that
--- page 324 ---

E a r ly E x e r c i s e o f A m e r i c a n   O p t i o n s 	 307
the price of the option is equal to its intrinsic value, the credit and debit will
cancel out, resulting in no cash flow. Because there is no cash flow, there can be
no advantage to early exercise. If, however, the option is subject to stock-type
settlement, as is the practice on futures exchanges in the United States, there
is no cash flow when the option position disappears. The only cash flow is the
variation credit on the futures position, a credit on which we can earn interest.
For a futures option to be an early exercise candidate, the option must be
subject to stock-type settlement, and the interest that can be earned on the intrinsic value must be greater than the volatility value that we are giving up
Interest value > volatility value
The interest on the option’s intrinsic value is either
(F – X) × r × t
for calls or
(X – F) × r × t
for puts.
As with stock options, we can estimate the volatility value of an option by
looking at the price of the companion out-of-the-money option. Suppose that
we have the following:

Futures price = 100

Time to expiration = 3 months

Interest rate = 8.00 percent
Is the 80 call an early exercise candidate if the price of the 80 put is 0.15?
The interest we can earn through early exercise is
(100 – 80) × 0.08 × 3/12 = 0.40
Because this is greater than the volatility value of .15, the option is an early exercise candidate. If given the choice between exercising now and holding the
position to expiration, we will come out ahead by 0.25 if we exercise now. For
the option to be an immediate early exercise candidate, it must also meet the
early exercise criteria over the next day. One day’s worth of interest must be
greater than one day’s worth of volatility value.
We can easily calculate one day’s worth of interest
(100 – 80) × .08/365 = 0.0044
How can we calculate one day’s worth of volatility value? We know that the
price of the companion option, in this case, the 80 put, is almost all volatility
value. As each day passes, the value of the option will fall by one day’s worth
of volatility value. This daily loss in value is simply the option’s theta. By determining the theta of the companion out-of-the-money option, we can estimate
one day’s worth of volatility value. Unlike the other calculations, this will require the use of a theoretical pricing model.
