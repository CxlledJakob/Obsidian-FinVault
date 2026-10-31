# Volatility Trading_ Sinclair_Volatility Trading -- Euan Sinclair(auth_) -- Wiley Trading, 1, 2013 -- John Wiley & Sons, Incorporated -- isbn13 9781118347133 -- 2634a86bfed8248fa7ba3fb72595bbbc -- Anna’s Archive.pdf — Chapter 9: Trade Evaluation — LEVERAGED ETFS (pages 248–248)

--- page 248 ---

LEVERAGED ETFS
236
where
k∗=
 k
L0
exp
λ −λ2
2
σ2t
 1
λ
(13.16)
Similarly, for λ < 0
CL = L0
S0
|λ| exp
λ −λ2
2
σ2t



k∗
λ−1PS(S0k∗, t) + (1 −λ)
k∗

0
Xλ−2PS(S0X, t)dX


(13.17)
and the puts for λ > 0 are
PL = L0
S0
λ exp
λ −λ2
2
σ2t



k∗
λ−1PS(S0k∗, t) + (λ −1)
k∗

0
Xλ−2PS(S0X, t)dX


(13.18)
and for λ < 0
PL = L0
S0
|λ| exp
λ −λ2
2
σ2t



k∗
λ−1CS(S0k∗, t) + (1 −λ)
0

k∗
Xλ−2CS(S0X, t)dX


(13.19)
The most important quantity here is k*. S0k* is ‘‘the most likely strike’’:
According to equation Z, if L = L0 then
S = S0

exp
λ2 −λ
2
σ2t
 1
λ
(13.20)
is the most likely place for S to be. This gives us the recipe for comparing
volatilities on the leveraged ETF and the reference product. The leveraged
ETF, L, should have λ times the volatility of the option on the reference
product, S, with strike S0k*. The option markets are generally fairly close to
this value. Figure 13.1 shows the front-month implied volatilities for SSO
(from July 23, 2012) together with the theoretical value from this model.
