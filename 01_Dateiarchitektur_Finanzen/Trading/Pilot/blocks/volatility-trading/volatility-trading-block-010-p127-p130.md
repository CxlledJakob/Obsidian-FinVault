# Volatility Trading_ Sinclair_Volatility Trading -- Euan Sinclair(auth_) -- Wiley Trading, 1, 2013 -- John Wiley & Sons, Incorporated -- isbn13 9781118347133 -- 2634a86bfed8248fa7ba3fb72595bbbc -- Anna’s Archive.pdf — Chapter 6: Hedging (pages 127–130)

--- page 127 ---

HEDGING
112
Substituting this into Equation 6.18 we obtain
Var[∆ln S] = α2λ∆tE[ni] = α2 µ∆t
(6.20)
where µ is deﬁned as the number of shares traded per unit of trading time.
The time change to trading time was designed to make this quantity
constant. So this equation also says that the variance of returns per unit of
trading time is also constant. Now we imagine that we undo our original
time shift. This means that both the volatility (σt) and µt, the number of
shares traded per unit of actual time, will be random variables. Eliminating
the common factor of ∆t (refer to Equation 4.18) we obtain
σ2
t = α2 µt
(6.21)
This gives a straightforward relationship between volume and volatility.
This has been conﬁrmed in numerous studies (Clark 1973; Tauchen and
Pitts 1983; Karpoff 1987), and few traders will dispute the relationship
(although they will argue over whether volume causes volatility or vice
versa). This model also leaves unsettled the dispute over whether trading
time is measured in number of trades or in volume of shares. Here, the
choices are equivalent.
Equation 6.22 gives us a simple way to estimate the market impact.
α =
σt
√µt
(6.22)
We know how to estimate the volatility. All we need to measure now is
the volume of stock traded per unit of time.
Strengths
■The model is very simple to understand and estimate.
■The model ﬁts our basic intuition: The more activity there is in a stock,
the less our market impact will be.
■We don’t need to deal with data at the level of individual transactions.
■This model can be used as a framework in the same way that we use
BSM and the hedging models in Chapter 1. We can tune it to each
individual market by multiplying by a prefactor. For example, we might
ﬁnd that DAX stocks are more slippery than FTSE stocks. (Merrill Lynch
calculated a list of these prefactors. I don’t include these here because
they are probably obsolete and they were estimated by asking Merrill
Lynch traders. I think, but cannot prove, that they reﬂect the attitudes
of individual traders as much as any fundamental aspect of each market.
--- page 128 ---

HEDGING
113
This is probably a place where the skill of a good, attentive trader can
make a signiﬁcant difference to overall performance.)
Weaknesses
■The model does not allow for sales to produce a different market impact
to buys.
■The model doesn’t take account of the market maker’s inventory, which
in practice has a large effect on the market impact of any particular order.
■Aggregation of Options on
Different Underlyings
As we saw at the start of this chapter, the best way to reduce our hedging
cost is to hedge less often. If we are trading options on a number of different
underlyings, there is a chance that many of our delta risks will offset. If
we are prepared to accept correlation risk instead, we can use this to avoid
hedging by aggregating our deltas and hedging market and possibly sector
risks in index products. Generally there is a trade-off here. An index position
is not going to be as good a hedge against our single stock option positions
as the stocks themselves would be, but we will save on transaction costs
because we will only need to hedge residual risk, not every individual risk.
The process of aggregation is simple enough in principle. Consider the
example where we have a Stock A with price SA = 100, and an Index I with
price SI = 1,000. Also assume that the index has an exchange-traded fund
(ETF) associated with it, so all of the trading units are comparable. Stock A
has a beta relative to the index, β = 1.5. This means that if the index moves
up 1 percent, A moves by 1.5 percent. If we are long 1,000 deltas of A
(whether shares or through option deltas) and the index moves 1 percent,
our proﬁt/loss ratio (P/L) is given by
P/L = $0.01 × β × SA × 1,000 = $15 × SA = $1,500
And for each unit of the index ETF we hold short, our loss will be
P/L = −$0.01 × 1,000 = $10
So to be hedged we need to hold a short position of 150 ETFs. Equivalently,
our delta in terms of the ETF is given by
∆I = βSA
SI
∆A
(6.23)
--- page 129 ---

HEDGING
114
To normalize gamma into ETF terms, write down the change in the
option value as a Taylor expansion:
dCA = ∆AdSA + A
2 dS2
A + · · ·
(6.24)
But
dSA = βSA
SI
dSI
so
dCA = ∆AβSA
SI
dSI + A
2 β2
SA
SI
2
dS2
I + · · ·
(6.25)
So the gamma term has to be
I =

β2S2
A
S2
I

A
(6.26)
Vega can be normalized in the same way as delta, but to do this we
need to know the volatility beta. This could be determined empirically by
regressing changes in the stock’s implied volatility on changes in index
volatility, but this is likely to give a very noisy and probably nonsensical
result. An alternative would be to assume that changes in implied volatility
and realized volatility are correlated perfectly (not a great assumption but
not the worst one to start with, either) and then use the result that the
volatility beta is the same as beta. To see this, start from the deﬁnition of
variance given by Equation 2.1b.
σ2
A = 1
N

ln
 SA (t)
SA(t −1)
2
≈1
N

dS2
A
= 1
N

(β2dS2
I )
≈β2σ2
I
(6.27)
(If we deﬁned β to be the slope of the regression of logarithmic returns
of the stock to logarithmic returns of the index, this relationship would be
exactly true instead of just a very good approximation.)
This tells how we could normalize our option positions. It is more of
a judgment call whether we should normalize them. It really comes down
to weighing the beneﬁts from reduced hedging costs against the errors
introduced by mis-estimation and the generally unstable nature of the beta
factors. Generally, estimating and forecasting beta is even more difﬁcult
than forecasting volatility (as we have to effectively estimate two volatilities
--- page 130 ---

HEDGING
115
and a correlation). When trading options speculatively, we think that we
have an edge in volatility prediction over the market. It probably isn’t wise
to conﬂate this bet with a more difﬁcult one when trying to save hedging
costs, but this trade-off is highly dependent on the particular situation. It is
probably unwise not to aggregate the Greeks from bills, notes, and bonds,
but whether to aggregate the risks from Microsoft (MSFT) and Google
(GOOG) into a Nasdaq book is more of a questionable call. Traders who
are serious about going down this path may want to consider using one
of the commercially developed factor models such as BARRA or APT to
quantify their risks.
The more conservative method would be to come up with hedging bands
for each underlying, and then also to keep track of the entire position’s risk
in terms of an index or possibly several indexes. This can help protect us
against the situation where the whole market moves against us but none of
our individual positions has reached a point where it should be hedged.
■Summary
To trade volatility, we need to continuously monitor, and periodically
adjust, our underlying position. Exactly how we choose to do this will have
a huge effect on our overall proﬁtability. Most of the trading that an option
trader does is actually hedging, so it is important to understand the process.
■Remember that hedging is designed to remove risk. If you are trying to
trade the underlying directionally, you are not hedging.
■Successful hedging removes the most risk for the least cost.
■The Hodges-Neuberger formalism solves this problem in theory but is
too cumbersome to use in practice.
■The approximation of Zakamouline is a good working solution that retains
most of the desirable features of the HN method.
■The Whalley-Wilmott approximation is a good rough approximation that
can be implemented within many commercially available pricing software
solutions.
■Further cost reduction can be achieved by aggregating option positions
across many different underlyings and managing the residual risk.
■Dynamic hedging cannot be relied on. It must be combined with static
hedging using other options. Only this can offset the risks associated with
jumps.
