# Volatility Trading_ Sinclair_Volatility Trading -- Euan Sinclair(auth_) -- Wiley Trading, 1, 2013 -- John Wiley & Sons, Incorporated -- isbn13 9781118347133 -- 2634a86bfed8248fa7ba3fb72595bbbc -- Anna’s Archive.pdf — Chapter 9: Trade Evaluation — LEVERAGED ETFS (pages 247–247)

--- page 247 ---

LEVERAGED ETFS
235
■Options on Leveraged ETFs
Because we have Equation 13.6 describing L as a function of S, we can price
options on L as a compound option on S. Carr and Madan (1998) showed
that any payoff function g(S) can be replicated as
g(S) = g(c) + g′(c)(S −c) +
c

−∞
g′′(X)(X −S)+dX
+
∞

c
g′′(X)(S −X)+dX
(13.11)
and the value of the option O(g) is given by
O(g) = g(c) + g′(c)(C −P) +
c

0
g′′(X)P(X)dX +
∞

c
g′′(X)C(X)dX
(13.12)
for any scalar, c. Now we consider the option on S to be L (i.e., g(S) = L)
and choose c = 0 to get
O(g) = 2L0
S0
exp(−σ2t)
∞

c
C(X)dX
(13.13)
So if we want to replicate L using options on S, we need to use a basket
of equally weighted calls. In other words, L is a power option on S with the
decay factor exp(−σ2t).
A similar approach can be used to price European options on L. First take
λ >0. If the strike (in terms of L) is k the payoff function is
g(S) =

L0
 S
S0
λ
exp
λ −λ2
2
σ2t

−k
+
(13.14)
Taking derivatives and substituting into Equation 13.11, we eventually
arrive at the value of a call on L, CL, in terms of calls on S, CS.
CL = L0
S0
λ exp
λ −λ2
2
σ2t



k∗
λ−1CS(S0k∗, t) + (λ −1)
∞

k∗
Xλ−2CS(S0X, t)dX


(13.15)
