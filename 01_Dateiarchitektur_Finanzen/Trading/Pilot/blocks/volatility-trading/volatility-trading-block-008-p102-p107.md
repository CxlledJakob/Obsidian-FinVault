# Volatility Trading_ Sinclair_Volatility Trading -- Euan Sinclair(auth_) -- Wiley Trading, 1, 2013 -- John Wiley & Sons, Incorporated -- isbn13 9781118347133 -- 2634a86bfed8248fa7ba3fb72595bbbc -- Anna’s Archive.pdf — Chapter 5: Implied Volatility Dynamics (pages 102–107)

--- page 102 ---

IMPLIED VOLATILITY DYNAMICS
86
A better solution was proposed by Corrado and Su (1996). They
performed an expansion (technically a Gram-Charlier expansion) of the
return distribution. This means that the parameters are time invariant (unless
the distribution really did change shape). The European call price is given by
C = CBSM + µ3Q3 + (µ4 −3)Q4
(5.14)
where
µ3 is the skewness of the returns
µ4 is the kurtosis
CBSM is the normal BSM call value
Q 3 = 1
6Sσ
√
T((2σ
√
T −d1)n(d1) + σ2TN(d1))
(5.15)
Q 4 = 1
24Sσ
√
T((d2
1 −1 −3σ
√
Td2)n(d1) + σ3√
T3N(d1))
(5.16)
where, as usual,
d1 =
ln
 S
X

+

r + σ2
2

T
σ√T
(5.17)
d2 = d1 −σ
√
T
(5.18)
N(x) =
1
√2π
x

−∞
exp
−z2
2

dz
(5.19)
is the cumulative normal distribution function and
n(x) =
1
√2π
exp
−x2
2

(5.20)
The put/call parity relationship can be used to ﬁnd the value of the put by
P = C −S + X exp(−rT)
(5.21)
Initially, we consider these parameters to be purely implied—that is,
they are only meaningful in the context of the option market and have no
direct relationship to the underlying return distribution. We use the quoted
option prices to back out the option parameters, but now we will not get
an implied volatility for each strike. We will get, from all the options of
a given expiry, an implied volatility, skewness, and kurtosis, reducing our
parameters from one per strike to just three.
To ﬁnd the implied skewness and kurtosis, we work directly from
Equation 5.4, searching for the parameters that minimized the squared
--- page 103 ---

IMPLIED VOLATILITY DYNAMICS
87
0
0.1
0.2
0.3
0.4
0.5
0.6
0.7
30
35
40
45
50
55
60
65
70
Strike
Implied Volatility
FIGURE 5.13
The Mid-Market Implied Volatility of the October Options as a
Function of Strike for GME on September 5, 2007 (ATM Strike Is 49.67)
difference of the quoted market prices and those from the new formula.
Figure 5.13 shows the implied volatility curve for the October 2007 expiry
for GameStop Corp. (GME) on September 5, 2007.
When we minimized the sum of the squares of the differences between
the quoted prices and the Corrado-Su prices from Equation 5.14 by changing
the σ, µ3, and µ4, we obtained the following results: σ = 0.508, µ3 =
−0.701, and µ4 = 4.42.
Strengths
■We can now think of implied skewness and implied kurtosis in ways
analogous to implied volatility. So we can maintain records of their
normal ranges and values for the products we trade. We can construct
term structures of skewness and kurtosis.
■We can directly compare the results with measurements of the realized
moments (again just as we did for volatility). We can construct skew and
kurtosis cones.
Weaknesses
■The volatility in the Corrado-Su formula is not the at-the-money implied
volatility. This can initially be confusing.
■The other implied moments don’t really affect the implied smile in the
way we would intuitively want them to. For example, a trader likes to
think of skewness as the linear slope of the implied volatility curve. But
--- page 104 ---

IMPLIED VOLATILITY DYNAMICS
88
0
0.1
0.2
0.3
0.4
0.5
0.6
0.8
0.85
0.9
0.95
1
1.05
1.1
1.15
1.2
Strike (as percentage of ATM)
Implied Volatility
FIGURE 5.14
The Equivalent Implied Volatility as a Function of Moneyness When σ
= 0.50, µ3 = −0.70, and µ4 = 0
if we hold volatility constant, and set the kurtosis equal to zero, the
Corrado-Su model gives a curve of equivalent BSM implied volatilities as
a function of strike, as shown in Figure 5.14.
■Similarly traders think of kurtosis as causing the convexity of the implied
volatility curve. But if we hold volatility constant and set skewness equal
to zero, the Corrado-Su model gives the curve of equivalent BSM implied
volatilities as a function of strike (see Figure 5.15). Note that it is not
symmetric around the ATM volatility. And the minimum of the implied
volatility occurs below the at-the-money strike.
■Thus the higher moments are somewhat intertwined in their effects.
We cannot directly attribute a shift in the shape of the curve to either
skewness or kurtosis. See Figure 5.16.
It is possible to obtain negative option prices, and not just for implausible
situations. For example, if the underlying price is 50, there are 50 days
remaining until expiry, interest rates are 5 percent, volatility is 50 percent,
skewness is −0.7, and kurtosis is 0 we would obtain a price of −0.21 for
the 65 strike call. Rubinstein (1998) gives approximate skewness/kurtosis
values where this will not happen. Jondeau and Rockinger (1999, 2001)
use the methods of Barton and Dennis (1952) to derive the boundary in the
--- page 105 ---

IMPLIED VOLATILITY DYNAMICS
89
0
0.1
0.2
0.3
0.4
0.5
0.6
0.8
0.85
0.9
0.95
1
1.05
1.1
1.15
1.2
Strike (as percentage of ATM)
Implied Volatility
FIGURE 5.15
The Equivalent Implied Volatility as a Function of Moneyness When σ
= 0.50, µ3 = 0, and µ4 = 10
−1.5
−1
−0.5
0
0.5
1
1.5
0.5
0
1.5
1
2.5
2
3.5
3
4.5
4
Excess Kurtosis
Skewness
FIGURE 5.16
The Skewness/Kurtosis Region, Inside Which the Gram-Charlier
Expansion Is a Probability Density
skewness/kurtosis space where the Gram-Charlier expansion is positive.
This is shown in Figure 5.16. We see that only relatively mild deviations
from normality are allowable.
The model of Corrado and Su is only directly applicable to European
options, but it is fairly straightforward to implement the idea in a tree
setting where we could apply U.S. (or more general) boundary conditions.
This idea was ﬁrst proposed by Rubinstein (1998), who worked with the
Edgeworth expansion. Haug (2007b) provides code for both Edgeworth
and Gram-Charlier trees.
--- page 106 ---

IMPLIED VOLATILITY DYNAMICS
90
■Term Structure Dynamics
Market makers are typically most focused on order ﬂow and risks in the
shorter maturity options. This is a sensible use of their resources. These
options are both where most volume is and also where trades can change
the overall risk proﬁle most quickly. However, it seems that this attention
on the front months (among other things, obviously) leads to a good trading
opportunity for others.
Because volatility is mean-reverting we would expect one volatility point
change in the front-month options’ implied volatility to be accompanied
by a somewhat smaller one in the back months. However, in practice the
back-month’s implied volatilities tend to move much more than would be
predicted by a rational expectations model: they overreact.
This effect was ﬁrst documented by Stein (1989), but it still exists more
than 20 years later. This suggests to me that there is some psychological
component to the market-makers behavior as the actual methods for trade
execution; volatility surface adjustment and risk management have changed
dramatically over that period.
He hypothesizes that the long-term implied volatility is the average of
the short-term implied volatility and the expected value of the short-term
implied volatility in the future. Speciﬁcally
σl −⟨σ⟩= 1
2(σs −⟨σ⟩+ E(σt+∆t
s −⟨σ⟩))
(5.22)
where σl is the long-term implied volatility, σs is the short-term implied
volatility, σt+∆ts is the short-term implied volatility at the future time
t+∆t and <σ> is the long-term average implied volatility. After taking
expectations and rearranging, we get
(σt+∆t
s −σs) −2(σl −σs) = 0
(5.23)
Thus, we can test for misreaction in the implied volatility term structure
by regressing the prediction error (the ﬁrst term of Equation 5.23) onto
the slope of the term structure. According to rational expectations, the
prediction error should be merely noise. Stein showed that this was untrue.
After establishing that the prediction error was systematically biased
he assumed that the instantaneous volatility followed an AR(1) process.
Then he could show that the constant of proportionality relating the levels
of frontand back-month volatilities was too high. The theoretical value
was around 0.85, while in reality it was around 0.95. So the back-month
volatilities substantially overreacted to movement in the shorter duration
options.
--- page 107 ---

IMPLIED VOLATILITY DYNAMICS
91
Stein actually downplayed the practical implications of the result. He
gave an example where long-term average volatility was 0.15 and the
front-month implied volatility was 0.25. With a proportionality constant of
0.85, the longer dated option should have an implied volatility of 0.15 +
0.85 (0.25 −0.15) = 0.235. But if the option market was using a constant
of 0.95, the long-dated option’s implied volatility would be 0.245. In 1989,
such a difference was not economically signiﬁcant. In 2012, it certainly is.
■Summary
Option trading requires knowledge of two types of volatility: realized
volatility, which is a measure of the underlying’s variability; and implied
volatility, which gives the market price of the options. We are interested
in the spread between these two volatilities. Implied volatility dynamics are
also tricky to quantify and forecast. Implied volatilities move more slowly
than realized volatilities, but implied volatilities have a term and strike
structure that also needs to be accounted for. Nonetheless, we can state
some general principles of which the trader should stay cognizant:
■The most important implied volatility for a trader is the at-the-money
level. Most of the implied volatility movement is a shift in the level of
volatility. The slope and curvature of the implied curve are of diminishing
variability (and hence importance).
■Implied volatility is mean-reverting.
■The shape of the implied volatility curve tends to be relatively stable
in a given product, although the actual reason for the smile can vary
dramatically between products.
■The Corrado-Su model allows us to put implied skewness and implied
kurtosis on the same footing as implied volatility.
