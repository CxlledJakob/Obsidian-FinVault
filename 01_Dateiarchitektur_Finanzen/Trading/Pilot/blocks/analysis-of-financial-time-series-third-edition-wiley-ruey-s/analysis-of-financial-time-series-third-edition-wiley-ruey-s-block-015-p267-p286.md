# Analysis of Financial Time Series, Third Edition (Wiley -- Ruey S_ Tsay -- Wiley series in probability and statistics, 3rd ed_, -- John Wiley & Sons, -- isbn13 9780470414354 -- 9f99b80c7b2dedd477f463dc5323f3b6 -- An.pdf — pages 267–286

--- page 267 ---

240
high-frequency data analysis and market microstructure
5-minute time intervals
Average
0
10
20
30
40
50
60
70
80
10
15
20
25
Figure 5.2
Time plot of average number of transactions in 5-minute time intervals. There are 78
observations, averaging over 63 trading days from 11/01/90 to 1/31/91 for IBM stock.
TABLE 5.2
Two-Way Classiﬁcation of Price Movements in Consecutive Intraday
Trades for IBM Stocka
ith Trade
(i −1)th trade
+
0
−
Margin
+
441
5498
3948
9887
0
4867
29779
5473
40119
−
4580
4841
410
9831
Margin
9888
40118
9831
59837
aThe price movements are classiﬁed into “up,” “unchanged,” and “down.” The data span is from
November 1, 1990, to January 31, 1991.
consecutive trades [i.e., from the (i −1)th to the ith transaction] in the sample.
From the table, trade-by-trade data show that:
1. Consecutive price increases or decreases are relatively rare, which are about
441/59837 = 0.74% and 410/59837 = 0.69%, respectively.
2. There is a slight edge to move from up to unchanged rather than to down;
see row 1 of the table.
3. There is a high tendency for the price to remain unchanged.
--- page 268 ---

empirical characteristics of transactions data
241
4. The probabilities of moving from down to up or unchanged are about the
same; see row 3.
The ﬁrst observation mentioned before is a clear demonstration of bid–ask
bounce, showing price reversals in intraday transactions data. To conﬁrm this phenomenon, we consider a directional series Di for price movements, where Di
assumes the value +1, 0, and −1 for up, unchanged, and down price movement,
respectively, for the ith transaction. The ACF of {Di} has a single spike at lag 1
with value −0.389, which is highly signiﬁcant for a sample size of 59,837 and
conﬁrms the price reversal in consecutive trades.
As a second illustration, we consider the transactions data of IBM stock in
December 1999 obtained from the TAQ database. The normal trading hours are
from 9:30 am to 4:00 pm Eastern time, except for December 31 when the market
closed at 1:00 pm. Comparing with the 1990–1991 data, two important changes
have occurred. First, the number of intraday tradings has increased sixfold. There
were 134,120 intraday tradings in December 1999 alone. The increased trading
intensity also increased the chance of multiple transactions within a second. The
percentage of trades with zero time duration doubled to 22.98%. At the extreme,
there were 42 transactions within a given second that happened twice on December
3, 1999. Second, the tick size of price movement was $ 1
16 = $0.0625 instead of
$ 1
8. The change in tick size should reduce the bid–ask spread. Figure 5.3 shows the
daily number of transactions in the new sample. Figure 5.4(a) shows the time plot
of time durations between trades, measured in seconds, and Figure 5.4(b) is the
After-hour
Regular
0
2000
4000
6000
8000
10000
Day
Number of trades
Figure 5.3
IBM transactions data for December 1999. Box plot shows the number of transactions in
each trading day with after-hours portion denoting number of trades with time stamp after 4:00 PM.
--- page 269 ---

242
high-frequency data analysis and market microstructure
Sequence
(a)
(b)
Duration
0
20000
40000
60000
80000
100000
120000
0 20 40 60 80
Sequence
Change
0
20000
40000
60000
80000
100000
120000
−60
−200 204060
Figure 5.4
IBM transactions data for December 1999. (a) Time plot of time durations between trades
and (b) time plot of price changes in consecutive trades measured in multiples of tick size of $1/16.
Only data during normal trading hours are included.
time plot of price changes in consecutive intraday trades, measured in multiples
of the tick size of $ 1
16. As expected, Figures 5.3 and 5.4(a) show clearly the
inverse relationship between the daily number of transactions and the time interval
between trades. Figure 5.4(b) shows two unusual price movements for IBM stock
on December 3, 1999. They were a drop of 63 ticks followed by an immediate
jump of 64 ticks and a drop of 68 ticks followed immediately by a jump of 68 ticks.
Unusual price movements like these occurred infrequently in intraday transactions.
Focusing on trades recorded within regular trading hours, we have 61,149 trades
out of 133,475 with no price change. This is about 45.8% and substantially lower
than that between November 1990 and January 1991. It seems that reducing the
tick size increased the chance of a price change. Table 5.3 gives the percentages of
trades associated with a price change. The price movements remain approximately
TABLE 5.3
Percentages of Intraday Transactions Associated with a Price Change
for IBM Stock Traded in December 1999a
Size
1
2
3
4
5
6
7
>7
Downward Movements
Percentage
18.03
5.80
1.79
0.66
0.25
0.15
0.09
0.32
Upward Movements
Percentage
18.24
5.57
1.79
0.71
0.24
0.17
0.10
0.31
aThe percentage of transactions without price change is 45.8% and the total number of transactions
recorded within regular trading hours is 133,475. The size is measured in multiples of tick size $ 1/16.
--- page 270 ---

empirical characteristics of transactions data
243
35000
40000
45000
50000
55000
40.0
41.0
42.0
Seconds
(a)
Price
0
10000
20000
30000
40000
−0.3
0.0
0.3
Index
(b)
Price change
Figure 5.5
Transactions data of Boeing stock on December 1, 2008. (a) Price series over calendar time
measured in seconds from midnight and (b) time plot of price changes in consecutive trades measured
in cents. Only data during normal trading hours are included.
symmetric with respect to zero. Large price movements in intraday tradings are
still relatively rare.
Finally, we consider the transactions data of Boeing stock on December 1,
2008. There are 43,894 transactions within the regular trading hours. Figure 5.5(a)
shows the transaction prices versus the calendar time measured in seconds from
the midnight, and Figure 5.5(b) shows the time plot of price changes. In this
particular instance, the price shows a downward trend within the day, but the
price changes continue to exhibit patterns similar to those before using the decimal
system. Figure 5.6 shows the histogram of the price changes for the Boeing stock.
The histogram shows some distinct characteristics. First, the price changes appear to
be symmetric with respective to zero. Second, the price changes indeed concentrate
on multiples of one cent. Out of the 43,894 transactions, 58.5% have no price
change; see the big spike of the histogram. Details of the summary of price changes
for the Boeing stock are given in Table 5.4. The remaining 4.59% of the price
changes not shown in Table 5.4 are not in multiples of one cent.
Remark.
The recordkeeping of high-frequency data is often not as good as
that of observations taken at lower frequencies. Data cleaning becomes a necessity
in high-frequency data analysis. For transactions data, missing observations may
happen in many ways, and the accuracy of the exact transaction time might be
questionable for some trades. For example, recorded trading times may be beyond
--- page 271 ---

244
high-frequency data analysis and market microstructure
Price change
Frequency
0.3
0.2
0.1
0.0
0.1
0.2
0.3
0.4
0
5000
10000
15000
20000
25000
Figure 5.6
Histogram of price changes for Boeing stock on December 1, 2008.
TABLE 5.4
Frequencies of Price Change for Boeing Stock on December 1, 2008
Cents
< −3
−3
−2
−1
0
1
2
3
>3
Percentage
1.63
1.05
3.51
12.6
58.5
12.2
3.45
0.94
1.53
4:00 pm Eastern time even before the opening of after-hours tradings. How to handle
these observations deserves a careful study. A proper method of data cleaning
requires a deep understanding of the way in which the market operates. As such,
it is important to specify clearly and precisely the methods used in data cleaning.
These methods must be taken into consideration in making inference.
□
Again, let ti be the calendar time, measured in seconds from midnight, when the
ith transaction took place. Let Pti be the transaction price. The price change from
the (i −1)th to the ith trade is yi ≡
Pti = Pti −Pti−1 and the time duration is

ti = ti −ti−1. Here it is understood that the subscript i in
ti and yi denotes the
time sequence of transactions, not the calendar time. In what follows, we consider
models for yi and
ti both individually and jointly.
5.4
MODELS FOR PRICE CHANGES
The discreteness and concentration on “no change” make it difﬁcult to model
the intraday price changes. Campbell et al. (1997) discuss several econometric
--- page 272 ---

models for price changes
245
models that have been proposed in the literature. Here we mention two models
that have the advantage of employing explanatory variables to study the intraday
price movements. The ﬁrst model is the ordered probit model used by Hauseman,
Lo, and MacKinlay (1992) to study the price movements in transactions data. The
second model has been considered recently by McCulloch and Tsay (2000) and is
a simpliﬁed version of the model proposed by Rydberg and Shephard (2003); see
also Ghysels (2000).
5.4.1
Ordered Probit Model
Let y∗
i be the unobservable price change of the asset under study (i.e., y∗
i = P ∗
ti −
P ∗
ti−1), where P ∗
t is the virtual price of the asset at time t. The ordered probit model
assumes that y∗
i is a continuous random variable and follows the model
y∗
i = xiβ + ϵi,
(5.15)
where xi is a p-dimensional row vector of explanatory variables available at
time ti−1, β is a p × 1 parameter vector, E(ϵi|xi) = 0, Var(ϵi|xi) = σ 2
i , and
Cov(ϵi, ϵj) = 0 for i̸ = j. The conditional variance σ 2
i is assumed to be a positive
function of the explanatory variable wi, that is,
σ 2
i = g(wi),
(5.16)
where g(·) is a positive function. For ﬁnancial transactions data, wi may contain
the time interval ti −ti−1 and some conditional heteroscedastic variables. Typically,
one also assumes that the conditional distribution of ϵi given xi and wi is Gaussian.
Suppose that the observed price change yi may assume k possible values. In
theory, k can be inﬁnity, but countable. In practice, k is ﬁnite and may involve
combining several categories into a single value. For example, we have k = 7 in
Table 5.1, where the ﬁrst value “−3 ticks” means that the price change is −3 ticks
or lower. We denote the k possible values as {s1, . . . , sk}. The ordered probit model
postulates the relationship between yi and y∗
i as
yi = sj
if
αj−1 < y∗
i ≤αj,
j = 1, . . . , k,
(5.17)
where αj are real numbers satisfying −∞= α0 < α1 < · · · < αk−1 < αk = ∞.
Under the assumption of conditional Gaussian distribution, we have
P (yi = sj|xi, wi) = P (αj−1 < xiβ + ϵi ≤αj|xi, wi)
=



P (xiβ + ϵi ≤α1|xi, wi)
if j = 1,
P (αj−1 < xiβ + ϵi ≤αj|xi, wi)
if j = 2, . . . , k −1,
P (αk−1 < xiβ + ϵi|xi, wi)
if j = k,
--- page 273 ---

246
high-frequency data analysis and market microstructure
=





α1 −xiβ
σi(wi)

if j = 1,


αj −xiβ
σi(wi)

−

αj−1 −xiβ
σi(wi)

if j = 2, . . . , k −1,
1 −

αk−1 −xiβ
σi(wi)

if j = k,
(5.18)
where (x) is the cumulative distribution function of the standard normal random
variable evaluated at x, and we write σi(wi) to denote that σ 2
i is a positive function
of wi. From the deﬁnition, an ordered probit model is driven by an unobservable
continuous random variable. The observed values, which have a natural ordering,
can be regarded as categories representing the underlying process.
The ordered probit model contains parameters β, αi (i = 1, . . . , k −1), and
those in the conditional variance function σi(wi) in Eq. (5.16). These parameters can be estimated by the maximum-likelihood or Markov chain Monte Carlo
methods.
Example 5.1.
Hauseman et al. (1992) apply the ordered probit model to
the 1988 transactions data of more than 100 stocks. Here we only report their
result for IBM. There are 206,794 trades. The sample mean (standard deviation)
of price change yi, time duration
ti, and bid–ask spread are −0.0010(0.753),
27.21(34.13), and 1.9470(1.4625), respectively. The bid–ask spread is measured
in ticks. The model used has nine categories for price movement, and the functional
speciﬁcations are
xiβ = β1
t∗
i +
3

v=1
βv+1yi−v +
3

v=1
βv+4SP5i−v +
3

v=1
βv+7IBSi−v
+
3

v=1
βv+10[Tλ(Vi−v) × IBSi−v],
(5.19)
σ 2
i (wi) = 1.0 + γ 2
1
t∗
i + γ 2
2 ABi−1,
(5.20)
where Tλ(V ) = (V λ −1)/λ is the Box–Cox (1964) transformation of V with λ ∈
[0, 1] and the explanatory variables are deﬁned by the following:
•
t∗
i = (ti −ti−1)/100 is a rescaled time duration between the (i −1)th and
ith trades with time measured in seconds.
• ABi−1 is the bid–ask spread prevailing at time ti−1 in ticks.
--- page 274 ---

models for price changes
247
• yi−v (v = 1, 2, 3) is the lagged value of price change at ti−v in ticks. With k
= 9, the possible values of price changes are {−4, −3, −2, −1, 0, 1, 2, 3, 4}
in ticks.
• Vi−v (v = 1, 2, 3) is the lagged value of dollar volume at the (i −v)th transaction, deﬁned as the price of the (i −v)th transaction in dollars times the
number of shares traded (denominated in hundreds of shares). That is, the
dollar volume is in hundreds of dollars.
• SP5i−v (v = 1, 2, 3) is the 5-minute continuously compounded returns of the
Standard and Poor’s 500 index futures price for the contract maturing in the
closest month beyond the month in which transaction (i −v) occurred, where
the return is computed with the futures price recorded 1 minute before the
nearest round minute prior to ti−v and the price recorded 5 minutes before this.
• IBSi−v (v = 1, 2, 3) is an indicator variable deﬁned by
IBSi−v =



1
if Pi−v >(P a
i−v + P b
i−v)/2,
0
if Pi−v = (P a
i−v + P b
i−v)/2,
−1
if Pi−v < (P a
i−v + P b
i−v)/2,
where P a
j and P b
j are the ask and bid price at time tj.
The parameter estimates and their t ratios are given in Table 5.5. All the t ratios
are large except one, indicating that the estimates are highly signiﬁcant. Such high
t ratios are not surprising as the sample size is large. For the heavily traded IBM
stock, the estimation results suggest the following conclusions:
1. The boundary partitions are not equally spaced but are almost symmetric
with respect to zero.
TABLE 5.5
Parameter Estimates of Ordered Probit Model in Eqs. (5.19) and (5.20)
for the 1988 Transaction Data of IBM, Where t Denotes the t Ratio
Boundary Partitions of the Probit Model
Parameter
α1
α2
α3
α4
α5
α6
α7
α8
Estimate
−4.67
−4.16
−3.11
−1.34
1.33
3.13
4.21
4.73
t
−145.7
−157.8
−171.6
−155.5
154.9
167.8
152.2
138.9
Equation Parameters of the Probit Model
Parameter
γ1
γ2
β1 :
t∗
i
β2 : y−1
β3
β4
β5
β6
Estimate
0.40
0.52
−0.12
−1.01
−0.53
−0.21
1.12
−0.26
t
15.6
71.1
−11.4
−135.6
−85.0
−47.2
54.2
−12.1
Parameter
β7
β8
β9:
β10
β11
β12
β13
Estimate
0.01
−1.14
−0.37
−0.17
0.12
0.05
0.02
t
0.26
−63.6
−21.6
−10.3
47.4
18.6
7.7
Source: Reprinted with permission of Elsevier from Journal of Financial Economics (1992, Vol. 31,
p. 345)
--- page 275 ---

248
high-frequency data analysis and market microstructure
2. The transaction duration
ti affects both the conditional mean and conditional variance of yi in Eqs. (5.19) and (5.20).
3. The coefﬁcients of lagged price changes are negative and highly signiﬁcant,
indicating price reversals.
4. As expected, the bid–ask spread at time ti−1 signiﬁcantly affects the conditional variance.
5.4.2
Decomposition Model
An alternative approach to modeling price change is to decompose it into three
components and use conditional speciﬁcations for the components; see Rydberg
and Shephard (2003). The three components are an indicator for price change, the
direction of price movement if there is a change, and the size of price change if a
change occurs. Speciﬁcally, the price change at the ith transaction can be written as
yi ≡Pti −Pti−1 = AiDiSi,
(5.21)
where Ai is a binary variable deﬁned as
Ai =

1
if there is a price change at the ith trade,
0
if price remains the same at the ith trade,
(5.22)
Di is also a discrete variable signifying the direction of the price change if a change
occurs, that is,
Di|(Ai = 1) =

1
if price increases at the ith trade,
−1
if price drops at the ith trade,
(5.23)
where Di|(Ai = 1) means that Di is deﬁned under the condition of Ai = 1, and Si is
the size of the price change in ticks if there is a change at the ith trade and Si = 0
if there is no price change at the ith trade. When there is a price change, Si is a
positive integer-valued random variable.
Note that Di is not needed when Ai = 0, and there is a natural ordering in the
decomposition. Di is well deﬁned only when Ai = 1 and Si is meaningful when
Ai = 1 and Di is given. Model speciﬁcation under the decomposition makes use
of the ordering.
Let Fi be the information set available at the ith transaction. Examples of
elements in Fi are
ti−j, Ai−j, Di−j, and Si−j for j ≥0. The evolution of price
change under model (5.21) can then be partitioned as
P (yi|Fi−1) = P (AiDiSi|Fi−1)
= P (Si|Di, Ai, Fi−1)P (Di|Ai, Fi−1)P (Ai|Fi−1).
(5.24)
--- page 276 ---

models for price changes
249
Since Ai is a binary variable, it sufﬁces to consider the evolution of the probability
pi = P (Ai = 1) over time. We assume that
ln

pi
1 −pi

= xiβ
or
pi =
exiβ
1 + exiβ ,
(5.25)
where xi is a ﬁnite-dimensional vector consisting of elements of Fi−1 and β is a
parameter vector. Conditioned on Ai = 1, Di is also a binary variable, and we use
the following model for δi = P (Di = 1|Ai = 1):
ln

δi
1 −δi

= ziγ
or
δi =
eziγ
1 + eziγ ,
(5.26)
where zi is a ﬁnite-dimensional vector consisting of elements of Fi−1 and γ is
a parameter vector. To allow for asymmetry between positive and negative price
changes, we assume that
Si|(Di, Ai = 1) ∼1 +

g(λu,i)
if Di = 1, Ai = 1,
g(λd,i)
if Di = −1, Ai = 1,
(5.27)
where g(λ) is a geometric distribution with parameter λ and the parameters λj,i
evolve over time as
ln

λj,i
1 −λj,i

= wiθj
or
λj,i =
ewiθj
1 + ewiθj ,
j = u, d,
(5.28)
where wi is again a ﬁnite-dimensional explanatory variable in Fi−1 and θj is a
parameter vector.
In Eq. (5.27), the probability mass function of a random variable x, which
follows the geometric distribution g(λ), is
p(x = m) = λ(1 −λ)m,
m = 0, 1, 2, . . . .
We added 1 to the geometric distribution so that the price change, if it occurs,
is at least 1 tick. In Eq. (5.28), we take the logistic transformation to ensure that
λj,i ∈[0, 1].
The previous speciﬁcation classiﬁes the ith trade, or transaction, into one of
three categories:
1. No price change: Ai = 0 and the associated probability is (1 −pi).
2. A price increase: Ai = 1, Di = 1, and the associated probability is piδi. The
size of the price increase is governed by 1 + g(λu,i).
3. A price drop: Ai = 1, Di = −1, and the associated probability is pi(1 −δi).
The size of the price drop is governed by 1 + g(λd,i).
--- page 277 ---

250
high-frequency data analysis and market microstructure
Let Ii(j) for j = 1, 2, 3 be the indicator variables of the prior three categories.
That is, Ii(j) = 1 if the jth category occurs and Ii(j) = 0 otherwise. The loglikelihood function of Eq. (5.24) becomes
ln[P (yi|Fi−1)] = Ii(1) ln[(1 −pi)] + Ii(2)[ln(pi) + ln(δi)
+ ln(λu,i) + (Si −1) ln(1 −λu,i)]
+ Ii(3)[ln(pi) + ln(1 −δi) + ln(λd,i) + (Si −1) ln(1 −λd,i)],
and the overall log-likelihood function is
ln[P (y1, . . . , yn|F0)] =
n

i=1
ln[P (yi|Fi−1)],
(5.29)
which is a function of parameters β, γ , θu, and θd.
Example 5.2.
We illustrate the decomposition model by analyzing the intraday
transactions of IBM stock from November 1, 1990, to January 31, 1991. There were
63 trading days and 59,838 intraday transactions in the normal trading hours. The
explanatory variables used are:
1. Ai−1: the action indicator of the previous trade [i.e., the (i −1)th trade within
a trading day]
2. Di−1: the direction indicator of the previous trade
3. Si−1: the size of the previous trade
4. Vi−1: the volume of the previous trade, divided by 1000
5.
ti−1: time duration from the (i −2)th to (i −1)th trade
6. BAi: the bid–ask spread prevailing at the time of transaction
Because we use lag-1 explanatory variables, the actual sample size is 59,775. It
turns out that Vi−1,
ti−1, and BAi are not statistically signiﬁcant for the model
entertained. Thus, only the ﬁrst three explanatory variables are used. The model
employed is
ln

pi
1 −pi

= β0 + β1Ai−1,
ln

δi
1 −δi

= γ0 + γ1Di−1,
(5.30)
ln

λu,i
1 −λu,i

= θu,0 + θu,1Si−1,
ln

λd,i
1 −λd,i

= θd,0 + θd,1Si−1.
--- page 278 ---

models for price changes
251
TABLE 5.6
Parameter Estimates of ADS Model in Eq. (5.30) for IBM Intraday
Transactions from December 1, 1990, to January 31, 1991
Parameter
β0
β1
γ0
γ1
Estimate
−1.057
0.962
−0.067
−2.307
Standard Error
0.104
0.044
0.023
0.056
Parameter
θu,0
θu,1
θd,0
θd,1
Estimate
2.235
−0.670
2.085
−0.509
Standard Error
0.029
0.050
0.187
0.139
The parameter estimates, using the log-likelihood function in Eq. (5.29), are given
in Table 5.6. The estimated simple model shows some dynamic dependence in the
price change. In particular, the trade-by-trade price changes of IBM stock exhibit
some appealing features:
1. The probability of a price change depends on the previous price change.
Speciﬁcally, we have
P (Ai = 1|Ai−1 = 0) = 0.258,
P (Ai = 1|Ai−1 = 1) = 0.476.
The result indicates that a price change may occur in clusters and, as expected,
most transactions are without price change. When no price change occurred
at the (i −1)th trade, then only about one out of four trades in the subsequent
transaction has a price change. When there is a price change at the (i −1)th
transaction, the probability of a price change in the ith trade increases to
about 0.5.
2. The direction of price change is governed by
P (Di = 1|Fi−1, Ai) =



0.483
if Di−1 = 0 (i.e., Ai−1 = 0),
0.085
if Di−1 = 1, Ai = 1,
0.904
if Di−1 = −1, Ai = 1.
This result says that (a) if no price change occurred at the (i −1)th trade,
then the chances for a price increase or decrease at the ith trade are about
even; and (b) the probabilities of consecutive price increases or decreases are
very low. The probability of a price increase at the ith trade given that a price
change occurs at the ith trade and there was a price increase at the (i −1)th
trade is only 8.6%. However, the probability of a price increase is about
90% given that a price change occurs at the ith trade and there was a price
decrease at the (i −1)th trade. Consequently, this result shows the effect of
bid–ask bounce and supports price reversals in high-frequency trading.
3. There is weak evidence suggesting that big price changes have a higher
probability to be followed by another big price change. Consider the size of
--- page 279 ---

252
high-frequency data analysis and market microstructure
a price increase. We have
Si|(Di = 1) ∼1 + g(λu,i),
λu,i = 2.235 −0.670Si−1.
Using the probability mass function of a geometric distribution, we obtain
that the probability of a price increase by one tick is 0.827 at the ith trade
if the transaction results in a price increase and Si−1 = 1. The probability
reduces to 0.709 if Si−1 = 2 and to 0.556 if Si−1 = 3. Consequently, the
probability of a large Si is proportional to Si−1 given that there is a price
increase at the ith trade.
A difference between the ADS of Eq. (5.21) and ordered probit models is that
the former does not require any truncation or grouping in the size of a price change.
R Demonstration for Logistic Linear Regression
The following output has been edited:
> da=read.table("ibm91-ads.txt",header=T)
> da1=read.table("ibm91-adsx.txt",header=T)
> Ai=da[,1]
% Select the variables
> Di=da[,2]
> Aim1=da1[,4]
> Dim1=da1[,5]
>
> m1=glm(Ai∼Aim1,family=binomial) %Fit a linear
logistic model
> summary(m1)
Call:
glm(formula = Ai ∼Aim1, family = binomial)
Deviance Residuals:
Min
1Q
Median
3Q
Max
-1.1373
-0.7724
-0.7724
1.2180
1.6462
Coefficients:
Estimate Std. Error z value Pr(>|z|)
(Intercept) -1.05667
0.01142
-92.55
<2e-16 ***
Aim1
0.96164
0.01827
52.62
<2e-16 ***
---
>
> di=Di[Ai==1]
% Select the cases in which Ai = 1.
> dim1=Dim1[Ai==1]
> di=(di+abs(di))/2
% Logistic regression works for 1 or 0,
% but di is coded 1 or -1 so that change is needed.
> m2=glm(di∼dim1,family=binomial)
> summary(m2)
Call:
glm(formula = di ∼dim1, family = binomial)
--- page 280 ---

duration models
253
Deviance Residuals:
Min
1Q
Median
3Q
Max
-2.1640
-1.1493
0.4497
1.2058
2.2193
Coefficients:
Estimate Std. Error z value Pr(>|z|)
(Intercept) -0.06663
0.01728
-3.855 0.000116 ***
dim1
-2.30693
0.03595 -64.171 <
2e-16 ***
5.5
DURATION MODELS
Duration models are concerned with time intervals between trades. Longer durations indicate lack of trading activities, which in turn signify a period of no new
information. The dynamic behavior of durations thus contains useful information
about intraday market activities. Using concepts similar to the ARCH models for
volatility, Engle and Russell (1998) propose an autoregressive conditional duration (ACD) model to describe the evolution of time durations for (heavily traded)
stocks. Zhang et al. (2001) extend the ACD model to account for nonlinearity and
structural breaks in the data. In this section, we introduce some simple duration
models. As mentioned before, intraday transactions exhibit some diurnal pattern.
Therefore, we focus on the adjusted time duration

t∗
i =
ti/f (ti),
(5.31)
where f (ti) is a deterministic function consisting of the cyclical component of

ti. Obviously, f (ti) depends on the underlying asset and the systematic behavior
of the market. In practice, there are many ways to estimate f (ti), but no single
method dominates the others in terms of statistical properties. A common approach
is to use smoothing spline. Here we use simple quadratic functions and indicator
variables to take care of the deterministic component of daily trading activities.
For the IBM data employed in the illustration of ADS models, we assume
f (ti) = exp[d(ti)],
d(ti) = β0 +
7

j=1
βjfj(ti),
(5.32)
where
f1(ti) = −
ti −43200
14400
	2
,
f3(ti) =



−
ti −38700
7500
	2
if ti < 43200,
0
otherwise,
f2(ti) = −
ti −48300
9300
	2
,
f4(ti) =



−
ti −48600
9000
	2
if ti ≥43200,
0
otherwise,
--- page 281 ---

254
high-frequency data analysis and market microstructure
Minutes
0
100
200
300
400
−1.0
−0.6
−0.2
(a)
Minutes
0
100
200
300
400
−1.0
−0.6
−0.2
(c)
Minutes
0
100
200
300
400
−1.0
−0.6
−0.2
(d)
Minutes
0
100
200
300
400
−2.0
−1.0
0.0
(b)
Figure 5.7
Quadratic functions used to remove deterministic component of IBM intraday trading
durations: (a)–(d) are functions f1(·) to f4(·) of Eq. (5.32), respectively.
and f5(ti) and f6(ti) are indicator variables for the ﬁrst and second 5 minutes of
market opening [i.e., f5(·) = 1 if and only if ti is between 9:30 am and 9:35 am
Eastern time], and f7(ti) is the indicator for the last 30 minutes of daily trading
[i.e., f7(ti) = 1 if and only if the trade occurred between 3:30 pm and 4:00 pm
Eastern time]. Figure 5.7 shows the plot of fi(·) for i = 1, . . . , 4, where the time
scale on the x axis is in minutes. Note that f3(43200) = f4(43200), where 43,200
corresponds to 12:00 noon.
The coefﬁcients βj of Eq. (5.32) are obtained by the least-squares method of
the linear regression
ln(
ti) = β0 +
7

j=1
βjfj(ti) + ϵi.
The ﬁtted model is
ln( ,

ti) = 2.555 + 0.159f1(ti) + 0.270f2(ti) + 0.384f3(ti)
+ 0.061f4(ti) −0.611f5(ti) −0.157f6(ti) + 0.073f7(ti).
Figure 5.8 shows the time plot of average durations in 5-minute time intervals over
the 63 trading days before and after adjusting for the deterministic component.
Figure 5.8(a) shows the average durations of
ti and, as expected, exhibits a
--- page 282 ---

duration models
255
10
20
30
40
5-minute intervals
Average duration
Average duration
0
10
20
30
40
50
60
70
80
2.0
2.2
2.4
2.6
2.8
3.0
3.2
(b)
5-minute intervals
0
10
20
30
40
50
60
70
80
(a)
Figure 5.8
IBM transactions data from 11/01/90 to 1/31/91: (a) average durations in 5-minute time
intervals and (b) average durations in 5-minute time intervals after adjusting for deterministic component.
diurnal pattern. Figure 5.8(b) shows the average durations of
t∗
i (i.e., after the
adjustment), and the diurnal pattern is largely removed.
5.5.1
The ACD Model
The autoregressive conditional duration (ACD) model uses the idea of GARCH
models to study the dynamic structure of the adjusted duration
t∗
i of Eq. (5.31).
For ease in notation, we deﬁne xi =
t∗
i .
Let ψi = E(xi|Fi−1) be the conditional expectation of the adjusted duration
between the (i −1)th and ith trades, where Fi−1 is the information set available
at the (i −1)th trade. In other words, ψi is the expected adjusted duration given
Fi−1. The basic ACD model is deﬁned as
xi = ψiϵi,
(5.33)
where {ϵi} is a sequence of independent and identically distributed nonnegative
random variables such that E(ϵi) = 1. In Engle and Russell (1998), ϵi follows a
standard exponential or a standardized Weibull distribution, and ψi assumes the
form
ψi = ω +
r

j=1
γjxi−j +
s

j=1
ωjψi−j.
(5.34)
--- page 283 ---

256
high-frequency data analysis and market microstructure
Such a model is referred to as an ACD(r, s) model. When the distribution of ϵi
is exponential, the resulting model is called an EACD(r, s) model. Similarly, if
ϵi follows a Weibull distribution, the model is a WACD(r, s) model. If necessary,
readers are referred to Appendix A for a quick review of exponential and Weibull
distributions.
Similar to GARCH models, the process ηi = xi −ψi is a martingale difference
sequence [i.e., E(ηi|Fi−1) = 0], and the ACD(r, s) model can be written as
xi = ω +
max(r,s)

j=1
(γj + ωj)xi−j −
s

j=1
ωjηi−j + ηj,
(5.35)
which is in the form of an ARMA process with non-Gaussian innovations. It is
understood here that γj = 0 for j > r and ωj = 0 for j > s. Such a representation
can be used to obtain the basic conditions for weak stationarity of the ACD model.
For instance, taking expectation on both sides of Eq. (5.35) and assuming weak
stationarity, we have
E(xi) =
ω
1 −max(r,s)
j=1
(γj + ωj)
.
Therefore, we assume ω > 0 and 1 > 
j(γj + ωj) because the expected duration is
positive. As another application of Eq. (5.35), we study properties of the EACD(1,1)
model.
EACD(1,1) Model
An EACD(1,1) model can be written as
xi = ψiϵi,
ψi = ω + γ1xi−1 + ω1ψi−1,
(5.36)
where ϵi follows the standard exponential distribution. Using the moments of a
standard exponential distribution in Appendix A, we have E(ϵi) = 1, Var(ϵi) = 1,
and E(ϵ2
i ) = Var(xi) + [E(xi)]2 = 2. Assuming that xi is weakly stationary (i.e.,
the ﬁrst two moments of xi are time invariant), we derive the variance of xi. First,
taking the expectation of Eq. (5.36), we have
E(xi) = E[E(ψiϵi|Fi−1)] = E(ψi),
E(ψi) = ω + γ1E(xi−1) + ω1E(ψi−1).
(5.37)
Under weak stationarity, E(ψi) = E(ψi−1) so that Eq. (5.37) gives
µx ≡E(xi) = E(ψi) =
ω
1 −γ1 −ω1
.
(5.38)
Next, because E(ϵ2
i ) = 2, we have E(x2
i ) = E[E(ψ2
i ϵ2
i |Fi−1)] = 2E(ψ2
i ).
--- page 284 ---

duration models
257
Taking the square of ψi in Eq. (5.36) and the expectation and using weak
stationarity of ψi and xi, we have, after some algebra, that
E(ψ2
i ) = µ2
x ×
1 −(γ1 + ω1)2
1 −2γ 2
1 −ω2
1 −2γ1ω1
.
(5.39)
Finally, using Var(xi) = E(x2
i ) −[E(xi)]2 and E(x2
i ) = 2E(ψ2
i ), we have
Var(xi) = 2E(ψ2
i ) −µ2
x = µ2
x ×
1 −ω2
1 −2γ1ω1
1 −ω2
1 −2γ1ω1 −2γ 2
1
,
where µx is deﬁned in Eq. (5.38). This result shows that, to have time-invariant
unconditional variance, the EACD(1,1) model in Eq. (5.36) must satisfy 1 > 2γ 2
1 +
ω2
1 + 2γ1ω1. The variance of a WACD(1,1) model can be obtained by using the
same techniques and the ﬁrst two moments of a standardized Weibull distribution.
ACD Models with a Generalized Gamma Distribution
In the statistical literature, intensity function is often expressed in terms of hazard
function. As shown in Appendix B, the hazard function of an EACD model is
constant over time and that of a WACD model is a monotonous function. These
hazard functions are rather restrictive in application as the intensity function of
stock transactions might not be constant or monotone over time. To increase the
ﬂexibility of the associated hazard function, Zhang et al. (2001) employ a (standardized) generalized gamma distribution for ϵi. See Appendix A for some basic
properties of a generalized gamma distribution. The resulting hazard function may
assume various patterns, including U shape or inverted U shape. We refer to an
ACD model with innovations that follow a generalized gamma distribution as a
GACD(r, s) model.
5.5.2
Simulation
To illustrate ACD processes, we generated 500 observations from the ACD(1,1)
model:
xi = ψiϵi,
ψi = 0.3 + 0.2xi−1 + 0.7ψi−1
(5.40)
using two different innovational distributions for ϵi. In case 1, ϵi is assumed to
follow a standardized Weibull distribution with parameter α = 1.5. In case 2, ϵi
follows a (standardized) generalized gamma distribution with parameters κ = 1.5
and α = 0.5.
Figure 5.9(a) shows the time plot of the WACD(1,1) series, whereas
Figure 5.10(a) is the GACD(1,1) series. Figure 5.11 plots the histograms of both
simulated series. The difference between the two models is evident. Finally,
the sample ACFs of the two simulated series are shown in Figures 5.12(a) and
5.13(b), respectively. The serial dependence of the data is clearly seen.
--- page 285 ---

258
high-frequency data analysis and market microstructure
Time index
(a)
Duration
0
100
200
300
400
500
10
2
0
4
6
8
Standard duration
3
2
1
0
Time index
(b)
0
100
200
300
400
500
Figure 5.9
Simulated WACD(1,1) series in Eq. (5.40): (a) original series and (b) standardized series
after estimation. There are 500 observations.
Time index
(a)
Duration
0
100
200
300
400
500
0
20
40
80
60
Standard duration
0
5 10 15 20 25
Time index
(b)
0
100
200
300
400
500
Figure 5.10
Simulated GACD(1,1) series in Eq. (5.40): (a) original series and (b) standardized series
after estimation. There are 500 observations.
--- page 286 ---

duration models
259
0
2
4
6
8
10
0
20
40
60
80
100
120
Z
(a)
(b)
0
20
40
60
80
0
100
200
300
X
Figure 5.11
Histograms of simulated duration processes with 500 observations: (a) WACD(1,1) model
and (b) GACD(1,1) model.
Lag
(a)
ACF
0
5
10
15
20
25
30
−0.2
0.0
0.2
0.4
Lag
(b)
ACF
0
5
10
15
20
25
30
−0.2
0.0
0.2
0.4
Figure 5.12
Sample autocorrelation function of simulated WACD(1,1) series with 500 observations:
(a) original series and (b) standardized residual series.
