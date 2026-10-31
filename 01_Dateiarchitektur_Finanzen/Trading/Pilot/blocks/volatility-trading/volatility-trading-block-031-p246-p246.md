# Volatility Trading_ Sinclair_Volatility Trading -- Euan Sinclair(auth_) -- Wiley Trading, 1, 2013 -- John Wiley & Sons, Incorporated -- isbn13 9781118347133 -- 2634a86bfed8248fa7ba3fb72595bbbc -- Anna’s Archive.pdf — Chapter 9: Trade Evaluation — LEVERAGED ETFS (pages 246–246)

--- page 246 ---

LEVERAGED ETFS
234
■Leveraged ETFs as a Trade-Sizing Problem
A complimentary way of thinking about leveraged ETFs is in terms of trade
sizing. The fund issuers are making a leveraged bet on the underlying. As
we have seen in Chapter 8, these bets can be too big: leveraged to the
point where growth becomes negative. During the period of 2008 that
we presented in Table 13.1, FXI had a return of 9 percent and a realized
annualized volatility of 146 percent. Assuming an interest rate of 0 percent,
Equation 8.14 gives the critical amount of leverage (according to the Kelly
criterion) as 0.04. So clearly a leverage of 2 was going to be a problem.
■A Long-Short Trading Strategy
If leveraged ETFs were merely another example of inappropriate leverage
choice they might not be very interesting. However, because they exist as
distinct products, we can combine them with a position in the reference fund
to create a perpetual position that is only dependent on realized volatility.
Let’s buy one dollar of L and sell short λ dollars of S (if λ <0 this would
mean that we would be buying L). At any given time our account equity is
E = L
L0
−λ S
S0
−(1 −λ)
(13.7)
(where the last term is the cash credit or debit for initiating the position).
Equation 13.6 then implies
E =
 S
S0
λ
exp

−1
2λ (λ −1) σ2t

−λ S
S0
−(1 −λ)
(13.8)
For concreteness and simplicity we now choose λ to be 2. In this case
E =
 S
S0
2
exp(−σ2t) −2 S
S0
+ 1
(13.9)
This is a parabolic function of the scaled reference fund value.
This portfolio behaves like a long straddle: Large moves make money but
we also incur time decay. But we are also short realized variance. To make
money we need steady, persistent moves. The breakeven levels are given
by
S
S0
= exp(σ2t)(1 ±

1 −exp(−σ2t))
(13.10)
