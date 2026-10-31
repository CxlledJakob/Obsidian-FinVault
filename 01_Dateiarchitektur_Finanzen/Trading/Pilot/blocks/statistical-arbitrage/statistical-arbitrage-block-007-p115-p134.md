# Statistical Arbitrage_ Algorithmic Trading Insights and -- Karen M_ Sowers; Andrew Pole -- Wiley Finance, 1, 2007 -- Wiley & Sons, Incorporated, John -- isbn13 9780470138441 -- 6b0138550172e24db7f13c932e054fb9 -- An.pdf — pages 115–134

--- page 115 ---

88
STATISTICAL ARBITRAGE
n
p75
0
5
10
15
20
0.0
0.2
0.4
0.6
0.8
1.0
p = 0.75
p = 0.25
p = 0.35
p = 0.5
FIGURE 4.9
Probability of at least 1 ‘‘winning move’’ in next n days
location adjustment in the applications, there is obviously greater
opportunity for reversion if more than one day ahead may be
considered. Of course, it is crucial that each day in the k-day period
ahead can be looked at individually; if one may only look at k-day
movements, then the situation is essentially unchanged from the
one-day case. When each day may be considered, there are multiple
(independent) chances of a win (a reversion), so the probability of a
win increases.
Figure 4.9 shows the probability of a move from the current
position in the direction of the median occurring within the next k
days for k = 1, . . . , 20. The probability of such a move occurring in
one day is 0.75 from the theorem. The other probabilities are calculated from the binomial distribution as described next. The ﬁgure
also includes graphs assuming a winning probability of 0.25, 0.35,
and 0.5: In practice, a lower value than 0.75 will be observed under
the best circumstances because of theorem assumption violations.
By assumption, prices are independent each day. The theorem
states that the probability of a reversionary move from the current
position is 0.75 for any day. So, the probability of a reversionary
move from the price on day t is 0.75 for day t + 1, for day t + 2
--- page 116 ---

Law of Reversion
89
regardless of what happens on day t + 1 (this is the independence
assumption), and so on. Thus, the number of days in the next k
days that show reversion from today’s price is a binomial quantity
with parameters k (the number of trials) and 0.75 (the probability of
success on a given trial). The probability shown in the graph is then:
Pr[1 or more successes in k days] = 1 −Pr[0 successes in k days]
= 1 −
k
0

0.750(1 −0.75)k−0
= 1 −0.25k
When the independence constraint is relaxed, the binomial result is
not valid, deviation from it being a function of the temporal structure
of the series. Where that structure is simple trending, the longer ahead
one looks the less accurate the binomial probability is. Accuracy may
be restored by appropriate attention to the structural form of the
prediction function: adding an estimated trend component.
--- page 117 ---
--- page 118 ---

CHAPTER5
Gauss Is Not the God of Reversion
It is better to be roughly right than precisely wrong.
—J.M. Keynes
5.1
INTRODUCTION
W
e begin with two quotes:
The distribution of nominal interest rates indicates that there
is no mean reversion in interest rates and the structure does
not resemble a normal distribution.
In contrast, real interest rates appear to be normally
distributed. The distribution suggests interest rates have the
characteristic of mean reversion.
Both of these quotes, from research publications (several years
ago) of a large, successful Wall Street ﬁrm, contain fallacious logical
implications. There is no explicit deﬁnition of what is meant by
‘‘mean reversion’’ and one might, therefore, take the depictions
of reversion through marginal distributions of yields as deﬁning it
implicitly. But that would mean that the author is not talking about
mean reversion in the general sense in which it is widely interpreted.
The ﬁrst statement is wrong because time series that exhibit
marginal distributions of any shape whatsoever can be mean reverting. The 75 Percent Theorem in Chapter 4 proves that unambiguously. Note the caveat: can be. It is not sufﬁcient to look at the
marginal distribution of a time series in order to be able to correctly
make a pronouncement on whether that series exhibits the quality of
91
--- page 119 ---

92
STATISTICAL ARBITRAGE
mean reversion. That is why the second statement is also wrong. It is
entirely possible for a time series to be as far from mean reverting as
imaginable (well, almost) while at the same time exhibiting a normal
marginal distribution, as is demonstrated in the ﬁnal section of this
chapter.
Mean reversion by deﬁnition involves temporal dynamics: The
sequence in which data, samples from the marginal distribution,
occur is the critical factor.
5.2
CAMELS AND DROMEDARIES
The report mentioned at the opening of this chapter shows a histogram of the ten-year bond yields since 1953, presented in a section
called, ‘‘A Double Humped Distribution.’’ The claim is that a time
series exhibiting such an obviously nonnormal marginal distribution
cannot be reversionary. Despite the imagery of the title, there are,
in fact, several modes in the histogram. However, it is sufﬁcient
to demonstrate a reversionary time series that has an extremely
pronounced bimodal distribution.
Figure 5.1 shows a combined random sample of 500 values from
the normal distribution with mean 4.5 and 500 values from the
normal distribution with mean 8.5 (and unit standard deviation for
both). These locations are motivated by the major modes of the bond
yield distribution; they are not critical to the demonstration.
Figure 5.2 shows one possible time series of these 1,000 points.
How much reversion is exhibited, from day 1, by this series? A lot.
Consider each segment separately. Take any point in either segment
far from the segment average (4.5 in the ﬁrst segment, 8.5 in the
second). How many points must be passed before the time series
exhibits a value closer to the segment average? Typically only one or
two. The series never departs from the segment mean never to return;
on the contrary, the series continually crosses the average—almost a
deﬁnition of reversion. A veritable excited popcorn process!
That leaves one to consider the implications of the single change
point: the move from the ﬁrst segment to the second in which the
segment mean increases. Does a single mean shift in a time series
destroy the property of mean reversion? Only if the process has to be
reverting to a global mean—that would be an unusually restrictive
interpretation of mean reversion; it would also be unhelpful and
--- page 120 ---

2
4
6
8
10
12
0
50
100
150
200
FIGURE 5.1
Marginal distribution: mixture distribution of half N[4.5,1] and half
N[8.5,1]
0
200
400
600
800
1,000
2
4
6
8
10
FIGURE 5.2
Time series realization of the sample depicted in Figure 5.1
93
--- page 121 ---

94
STATISTICAL ARBITRAGE
misleading in a time series context, and misleading, too, in assessing
trading opportunities that necessarily occur in a time series, sequential
manner. Suppose that the raw data are daily values. Then for two
years, the ﬁrst segment of the combined series, the data would
unarguably be described as mean reverting. Shortly after the mean
increase the same conclusion would be acknowledged, albeit the
mean to which the series reverts is increased. Two more years of
splendid reversion to the (new) mean then follow. How could anyone
then look at the marginal distribution of the daily data, having
traded wonderfully proﬁtably the most basic mean reverting strategy
describable, and announce that the series was not mean reverting?
A second distributional concern raised is that the bond data
distribution has a pronounced right-hand tail. This feature is actually
irrelevant insofar as the property of mean reversion is concerned.
Figure 5.3 shows a histogram of 1,200 points: the 1,000 from
the normal mixture of the previous example with 200 uniformly
randomly distributed over the interval [10,14]. Figure 5.4 shows one
possible time series of the 1,200 points: How much reversion is there
in this series? A lot, once again. The ﬁrst two segments are mean
reverting as demonstrated in the previous paragraphs. What about
the ﬁnal segment? The points are a random sample from a uniform
2
4
6
8
10
12
14
0
50
100
150
200
FIGURE 5.3
Marginal distribution with heavy right tail
--- page 122 ---

Gauss Is Not the God of Reversion
95
0
200
400
600
800
1,000
1,200
2
4
6
8
10
12
14
FIGURE 5.4
Time series realization of the sample depicted in Figure 5.3
ordered by underlying sampling distribution
distribution, not a normal distribution, and therefore according to
the report, the time series cannot be mean reverting. From the graph,
would you agree? If you do, I would like to entertain some gambles
with you!
One might reasonably charge that these examples are artiﬁcial.
Real time series don’t exhibit such convenient segmentation. This
is undeniable. But it is also not an issue. Figure 5.5 shows another
possible realization of the random sample in Figure 5.3. It was
obtained by randomly selecting, without replacement, the values in
the original sample of 1,200 and plotting in order of selection. How
much reversion is exhibited? Lots. Don’t you agree just from an
eyeball analysis?
Whether the marginal distribution of a time series is a dromedary
or a camel really doesn’t matter as far as mean reversion is concerned.
To repeat: Temporal structure is the critical feature.
5.2.1
Dry River Flow
Camels are distinguished largely by their remarkable adaptation to
life in arid regions, the twin key abilities bestowed by evolution
being the sponge-like capacity of the body to absorb water and the
--- page 123 ---

96
STATISTICAL ARBITRAGE
0
200
400
600
800
1,000
1,200
2
4
6
8
10
12
14
FIGURE 5.5
Time series realization of the sample depicted in Figure 5.3
randomly reordered
drip-feed use thereof. Dry rivers, those with notable periods of no
stream ﬂow, are common in arid landscapes (and often the source of
replenishment for camels). Looking at a time series of stream ﬂow
for a dry river, one would ﬁnd it difﬁcult to deny the claim that such
a series is reversionary. The series always returns to zero no matter
how far it departs therefrom in the rainy season.
What is the typical marginal distribution of dry river ﬂow?
Obviously it is very asymmetric. So, entirely without recourse to
mathematical formalism or rigor, we have a proof that a reversionary time series need not be characterized by a symmetric marginal
distribution such as the normal.
The Bell Still Tolls
Often a so-called Gamma distribution is a good
approximation (allowing for reasonable fudge for the zeroes) to dry
river ﬂow. Now, a squared Gaussian variable is distributed as a
Chi-squared variable, which is also a Gamma variable. More than
curious coincidence?
But Not for Reversion
The dry river ﬂow example is just one particular
case of self-evident reversion. To repeat: any marginal distribution
can be exhibited by a reversionary time series.
--- page 124 ---

−5
0
5
10
0
50
100
150
200
250
300
FIGURE 5.6
Random sample of 1,000 points from N[2.65, 2.442]
0
200
400
600
800
1,000
−5
0
5
10
FIGURE 5.7
Time series realization of the sample depicted in Figure 5.6
97
--- page 125 ---

98
STATISTICAL ARBITRAGE
5.3
SOME BELLS CLANG
A time series exhibiting a normal marginal distribution is not predisposed to exhibit mean reversion. Extraordinary diversion is equally
possible. Figure 5.6 shows a random sample from the normal distribution with mean 2.65 and standard deviation 2.44—the sample
values of the real yield data in the cited analysis. Figure 5.7 shows
one possible realization of this sample as a time series in which the
sample points are taken in order of magnitude. How much reversion
is exhibited, from day 1, by this series? Not one bit. As with my
earlier example, the charge of ‘‘unrealistic’’ or ‘‘points don’t occur
in [size] order’’ can be readily made. But such charges are irrelevant:
The point demonstrated, no matter how stylized the illustration, is
that a normal marginal distribution for a sample from a time series
reveals nothing about the temporal properties of that series, reversion
or any other.
The paper from which the quotes at the beginning of this chapter
are taken, and the content of which is critically examined here, is not
included in the references list.
--- page 126 ---

CHAPTER6
Interstock Volatility
. . .the investor does (or should) consider expected return a
desirable thing and variance of return an undesirable thing.
—Harry Markowitz, Journal of Finance,
Vol. 7, No. 1, 1952
6.1
INTRODUCTION
T
he reversion exploited in pairs trading is the reversion of stock
prices to each other following a movement apart, or a movement
apart following an unusual narrowing—the popcorn process of
Chapter 2. The amount of movement in stock prices is measured
by and expressed as stock volatility, which is the standard deviation
of price changes (returns). The volatility that is relevant to the
spread reversion scheme is the volatility of relative price movements
between stocks, hence interstock volatility. Figure 6.1(a) shows the
daily closing price (adjusted for splits and dividends) of two related
stocks, ENL and RUK, for the ﬁrst six months of 1999. The price
series track each other very closely, further demonstrated by the price
difference (spread) series shown in Figure 6.1(b). Ignoring the scales,
the spread series looks like any stock price series, and it will not be
surprising to discover that the volatility of the spread is similar in
character to stock price volatility.
Stock price volatility is the standard deviation of returns. But
what is the relevant measure of spread volatility? In Chapter 2 we
calibrated trade rules by directly computing the standard deviation
of the spread itself. Here we are interested in the technical deﬁnition
99
--- page 127 ---

Jan
Feb
Mar
Apr
May
Jun
Jul
1999
Jan
Feb
Mar
Apr
May
Jun
Jul
1999
Jan
Feb
Mar
Apr
May
Jun
Jul
1999
(a) Adjusted close price
(b) Adjusted close price difference
(c) Annualized volatility
20
25
30
35
40
45
$
ELN
RUK
−15
−10
−5
0
5
10
$
ELN – RUK
0
50
100
%
ELN
RUK
spread
FIGURE 6.1
(a) Daily adjusted close prices of ENL and RUK; (b) spread;
(c) volatilities
100
--- page 128 ---

Interstock Volatility
101
of volatility, not simply a scale factor, and this requires focusing
on an appropriate return series. Considering the price difference in
Figure 6.1(b), with the trace variously above and below zero, it
is obvious that one should not treat the spread as a price—inﬁnite
‘‘returns’’ are readily exhibited by such a series! The relevant measure
is apparent from consideration of how a basic reversion strategy
exploits spreads: When the spread widens or narrows beyond some
threshold whereupon reversion is subsequently expected, make two
bets, one on each stock, one a buy and the other a sell. Thus, the
spread bet return is the sum of the return on the stock bought and
the negative return on the stock sold:
spread return = return on buy −return on sell
(assuming equal dollar bets and measuring return to the long only).
Therefore, the value of interest, a measure of the range of variation
in the value of a spread bet or spread volatility, is directly computed
from the spread return series, itself the numeric difference of the buy
and sell return. (At this point of detail, one can begin to see how
the considerations generalize beyond the pair setting to more general
statistical arbitrages.)
Figure 6.1(c) shows the volatility traces, using a trailing 20-day
window, of the two stocks ENL and RUK and of the spread
ENL–RUK. (In all of the examples in this chapter, volatilities are
computed under the conventional assumption of locally zero-mean
return.) The spread volatility is, as foreshadowed, visually similar to
the stock volatilities. Curiously, it is consistently greater than both
the individual stock volatilities—more about that later.
Another example is shown in Figure 6.2, this time for the pair
General Motors (GM) and Ford (F). Notice that the volatility of the
spread is sometimes greater and sometimes less than the volatility of
both stocks, and sometimes greater than one but less than the other.
These two examples expose many of the features of spread
volatility that are important in understanding and exploiting spread
relationships both for the simplest pairs, as illustrated, and more
general cases including baskets of stocks. Figure 6.3 shows another
example, this time of two unrelated stocks, Microsoft (MSFT) and
EXXON (XON).
--- page 129 ---

Jan
Feb
Mar
Apr
May
Jun
Jul
1999
Jan
Feb
Mar
Apr
May
Jun
Jul
1999
50
55
60
65
70
75
80
$
GM
F
0
5
10
15
20
$
GM – F
0
20
40
60
80
%
GM
F
spread
(a) Adjusted close price
(b) Adjusted close price difference
(c) Annualized volatility
Jan
Feb
Mar
Apr
May
Jun
Jul
1999
FIGURE 6.2
(a) Daily adjusted close prices of GM and F; (b) spread;
(c) volatilities
102
--- page 130 ---

Interstock Volatility
103
6.2
THEORETICAL EXPLANATION
Relative price movement is functionally dependent on the price
movements of individual stocks: What could be simpler than price of
A −price of B? When looking at the variability of relative prices, the
relationship is more complicated. The key relationship is that for the
spread return already given:
spread return = return on buy −return on sell
Writing A for the return on buy, B for the return on sell, and S for
the spread return, the spread volatility is expressed as:

V[S] =

V[A −B]
=

V[A] + V[B] −2V[A, B]
where V[·] denotes (statistical or probabilistic) variance, and V[·, ·]
similarly denotes covariance. This expression immediately reveals
how and why the spread volatility can be less than, greater than, or
equal to the volatility of either constituent stock. The pertinent factor
is the covariance of (the returns of) those two stocks, V[A, B].
If the two stocks A and B (abusing notation quite deliberately)
are in fact the same stock, then the variances (the square of the
volatility) are the same and, crucially, the covariance is also equal
to the variance. Hence the volatility of the spread is zero: What else
could it be since the spread itself is identically zero?
Now, what if the two stocks are unrelated? Statistically, this is
equivalent to saying that the covariance is zero. Then the spread
volatility reduces to:

V[S] =

V[A] + V[B]
That is, spread volatility is larger than both of the individual stock
volatilities. If the individual stocks have similar volatility, V[A] ≈
V[B], then the inﬂation factor is about 40 percent:

V[S] =

V[A] + V[B]
≈

2V[A]
= 1.414

V[A]
--- page 131 ---

Jan
Feb
Mar
Apr
May
Jun
Jul
1999
Jan
Feb
Mar
Apr
May
Jun
Jul
1999
Jan
Feb
Mar
Apr
May
Jun
Jul
1999
60
70
80
90
100
110
$
MSFT
XON
−10
0
10
20
30
$
MSFT – XON
0
20
40
60
80
%
MSFT
XON
spread
(a) Adjusted close price
(b) Adjusted close price difference
(c) Annualized volatility
FIGURE 6.3
(a) Daily adjusted close prices of MSFT and XON; (b) spread;
(c) volatilities
104
--- page 132 ---

Interstock Volatility
105
6.2.1
Theory versus Practice
The illustration in Figure 6.1 shows the spread volatility for two
related stocks to be larger than both the individual stock volatilities.
The theory advanced in the previous section says (1) spread volatility
is zero for identical stocks, and (2) spread volatility is larger than
both individual stocks for unrelated stocks. Ugh? Surely ‘‘related
stocks’’ (such as ENL and RUK) are more like ‘‘identical stocks’’
than ‘‘unrelated stocks.’’ So according to the theory, shouldn’t the
volatility of the ENL–RUK spread be small?
Now we must distinguish between statistical deﬁnitions of terms
and English interpretations of the same terms. The two Elsevier
stocks, ENL and RUK, are indeed related—essentially they are
the same company. The historical traces of the price series show
extraordinarily similar behavior as beﬁts that. Over the long term,
one is justiﬁed in stating that the prices are the same. However,
the price traces on the daily time scale seldom move precisely in
parallel; therefore the spread between the two does vary—seen in
Figure 6.1(b)—and spread volatility is not zero. In fact, over the
short term, the two price series show a negative relationship: In
Figure 6.1(a) the two price traces proceed sinuously like two snakes
entwined in a cartoon embrace, the one moving up when the other
moves down and vice versa. Statistically, this means that the two
series are negatively correlated, particularly on the short-term return
scale which is pertinent to local volatility calculations.
Aha! Negative correlation (hence, negative covariance). Put that
in the formula for spread volatility and immediately it is clear why the
Elsevier stocks’ spread volatility is greater than both the individual
stock volatilities. Proﬁt in the bank for pairs trading!
6.2.2
Finish the Theory
Return to the expression for spread volatility:

V[S] =

V[A] + V[B] −2V[A,B]
Write σ 2 = min(V[A], V[B]) and σ 2 = max(V[A], V[B]), then it is
trivial to sandwich the spread volatility between multiples of the
individual stock volatilities for uncorrelated stocks (V[A, B] = 0):
√
2σ ≤

V[S] ≤
√
2σ
--- page 133 ---

106
STATISTICAL ARBITRAGE
Two immediate observations have already been noted: For two
similarly volatile stocks, the spread will exhibit 40 percent more
volatility than the individual stocks; for two perfectly positively
correlated stocks, the spread will exhibit no volatility because it is
constant. That leaves one extreme case of relatedness: where A and B
are perfectly negatively correlated, A = −B. Here the spread volatility
is double the individual stock volatility:
V[S] = V[A] + V[B] −2V[A, B]
= V[A] + V[−A] −2V[A, −A]
= V[A] + V[A] + 2V[A, A]
= 4V[A]
Hence,

V[S] = 2

V[A]. For statistical arbitrage this is (almost) the
grail of spread relationships.
6.2.3
Finish the Examples
What can be inferred about the GM–F and MSFT–XON examples
with the beneﬁt of the theory for the volatility of spreads? Given a
description of the stock and spread volatility traces, one can point
to periods of changing local correlation, positive to negative. Of
course, one can observe correlation by direct calculation: See Figure
6.4. Average correlation in this ﬁrst six months of 1999 is 0.58;
maximum 20-day correlation is 0.86; minimum 20-day correlation
is −0.15. Important to note here, for spread exploitation, are the
dynamic changes in correlations and, hence, spread volatility and the
range of variation.
From late April the GM–F spread volatility was less than both
individual stock volatilities, as it was for most of March. In fact, from
the spread trace in Figure 6.2(b) it is clear that for most of April and
May, and again in June, the spread was practically constant in comparison to its value outside those periods. The spread volatility trace
in Figure 6.2(c) shows a 50 percent hike in April and a similar drop
in May. Clearly these are artifacts of the unusually large (negative)
single day spread return on April 7 (see Figure 6.5) and the 20-day
window used to compute an estimate of volatility—review the local
correlation in Figure 6.4. Outlier down-weighting and smoothing are
--- page 134 ---

0.2
0.4
0.6
0.8
19990104 19990129 19990226 19990331 19990430 19990528 19990630
FIGURE 6.4
GM–F rolling 20-day correlation
−0.05
0.0
0.05
percent
19990104
19990129
19990226
19990331
19990430
19990528
19990630
FIGURE 6.5
GM–F spread daily return
107
