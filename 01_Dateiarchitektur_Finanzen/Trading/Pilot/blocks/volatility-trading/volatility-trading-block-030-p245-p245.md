# Volatility Trading_ Sinclair_Volatility Trading -- Euan Sinclair(auth_) -- Wiley Trading, 1, 2013 -- John Wiley & Sons, Incorporated -- isbn13 9781118347133 -- 2634a86bfed8248fa7ba3fb72595bbbc -- Anna’s Archive.pdf — Chapter 9: Trade Evaluation — LEVERAGED ETFS (pages 245–245)

--- page 245 ---

LEVERAGED ETFS
233
That is,
dL = LλdSt
S
(13.1)
Strictly, this applies to a continuously rebalanced strategy but it is
a reasonable approximation to daily rebalancing. Now assume that the
reference ETF follows GBM so that
dS = µSdt + σSdz
(13.2)
where, as usual, µ is the drift term, σ is the volatility, and z is a Brownian
motion.
The crude idea behind the rebalancing strategy is to obtain a payoff of the
form
 S
S0
λ
(13.3)
We use this to guess the form of the evolution of the leveraged ETF
value,
L = L0
 S
S0
λ
(13.4)
Applying It¯o’s lemma to this ansatz gives us
dL = ∂L
∂t dt + ∂L
∂SdS + 1
2
∂2L
∂S2σ2S2dt
= L

λdS
S + 1
2λ (λ −1) σ2dt

(13.5)
which is clearly not the desired solution (Equation 13.3). Hence we need
to modify our guess by including a variance term.
L = L0
 S
S0
λ
exp

−1
2λ (λ −1) σ2t

(13.6)
Applying It¯o’s lemma directly shows that this fund evolution replicates
the trading strategy required by Equation 13.1. Note that this has two
distinct parts: the naive leveraged return and the drag due to realized
variance. This is why the myth is an oversimpliﬁcation. It is quite possible
for the ﬁrst term to dominate the second and cause the leveraged ETF to
have overperformance. Consider the case of TLT and UBT, ETFs designed
to give respectively the daily return and twice the daily return of the Barclays
Capital U.S. 20+ Year Treasury Index. Between June 1, 2011, and June
1, 2012, TLT gained 37.9 percent while UBT gained 82.1 percent, an
overperformance of 6.3 percent.
