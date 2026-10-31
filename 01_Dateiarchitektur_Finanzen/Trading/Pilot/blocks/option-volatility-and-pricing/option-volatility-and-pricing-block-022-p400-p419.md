# Option Volatility and Pricing_ Advanced Trading Strategies -- Sheldon Natenberg -- 2nd ed, 2014 -- McGraw Hill Professional -- isbn13 9780071818773 -- 6a48d008bd9beef283debf7bad0b2e4a -- Anna’s Archive.pdf — pages 400–419

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
--- page 401 ---

384
O P T I O N V O L AT I L I T Y A N D P R I C I N G
When calculating historical volatility, traders typically exclude weekends
and holidays, resulting in a trading year of between 250 and 260 days. But one
might also calculate volatility using all 365 days, assigning a 0 price change to
nontrading days. This method might be appropriate when trying to compare
the volatilities of products traded on two different exchanges with different trading calendars. The two methods will obviously yield slightly different historical
volatilities. But, if historical volatility is used as a general guideline to future realized volatility, the differences are unlikely to be significant. This can be seen in
Figure 20-1, which shows the three-month volatility of the Standard and Poor’s
(S&P) 500 Index calculated using only trading days (approximately 252 days per
year) and using all 365 days.1 The graphs are almost indistinguishable.
Although daily price returns are most often used to calculate historical volatility, we might instead use weekly price returns. How will this affect the historical volatility calculation? Figure 20-2 shows the three-month volatility of gold
from 2001 through 2010 calculated using both daily and weekly price returns.
In general, the graphs show similar characteristics, although fluctuations seem to
be slightly greater using weekly returns. This is probably due to the smaller number of data points (13 weekly data points rather than 91 daily data points). The
greater number of data points will tend to have a smoothing effect. Because the
1 Because volatility is always quoted on an annualized basis, whether we calculate historical volatility using all
365 days or only trading days, the standard deviation of price changes must be multiplied by the square root
of the number of trading periods in a year. For a 365-day trading year, the standard deviation must be multiplied by 365
19.1
≈
.
Figure 20-1  S&P 500 Index three-month historical volatility: 2001–2010.
Annualized volatility
80%
Dec-00
Dec-01
Dec-02
Dec-03
Dec-04
Dec-05
Dec-06
Dec-07
Dec-08
Dec-09
Dec-10
70%
60%
50%
40%
30%
20%
10%
0%
Volatility calculated using only trading days
Volatility calculated using all 365 days
--- page 402 ---

V o l at i l i t y R e v i s i t e d 	 385
graphs show similar characteristics, we can conclude that if a contract is volatile
from day to day, it will be equally volatile from week to week or month to month.
Daily returns are used most often in order to increase the number of data points
in the volatility calculation and therefore yield a more accurate volatility.
Suppose that the price of a contract fluctuates wildly during a trading day,
making dramatic up and down moves, yet finishes the day unchanged. If this is
a common occurrence, then using only settlement prices to calculate the historical volatility may result in an incomplete picture of a contract’s true volatility.
To take into consideration intraday price movement, several alternative methods have been proposed to calculate historical volatility.
The extreme-value method, proposed by Michael Parkinson,2 uses the high and
low values during a 24-hour period. This method not only gives a more complete picture of volatility but may also be useful when no definitive settlement
prices are available. Using the extreme-value method, the annualized historical
volatility is given by
n
h
l
t
1
2
ln(2)
ln
i
i
i
n
2
1∑



=
2 Michael Parkinson, “The Extreme Value Method of Estimating the Variance of the Rate of Return,” Journal
of Business 53(1):61–64, 1980.
Figure 20-2  Gold three-month historical volatility: 2001–2010.
Annualized volatility
50%
Dec-00
Dec-01
Dec-02
Dec-03
Dec-04
Dec-05
Dec-06
Dec-07
Dec-08
Dec-09
Dec-10
40%
30%
20%
10%
0%
Volatility calculated from daily price changes
Volatility calculated from weekly price changes
--- page 403 ---

386
O P T I O N V O L AT I L I T Y A N D P R I C I N G
where n = number of price returns, hi = highest price during the chosen time
interval, li = lowest price during the chosen time interval, ln = natural logarithm, and t = the length of each time interval in years.
An alternative approach proposed by Mark Garman and Michael Klass3
expands the Parkinson method by also including the opening and closing prices
for an underlying contract. Using this method, the annualized historical volatility is given by
n
h
l
n
c
o
t
1
2
ln
1 2ln(2)
1
ln
i
i
i
i
i
n
i
n
2
2
1
1
∑
∑
[
]



−
−




=
=
where oi = opening price at the beginning of trading, and ci = closing price at
the end of trading.
As with the traditional close-to-close estimator, both the Parkinson and
Garman-Klass estimators are annualized by dividing by the square root of t,
the time between price intervals. (This is the same as multiplying by the square
root of the number of time intervals in a year.)
Figure 20-3 shows the three-month volatility of the EuroStoxx 50 Index,
a widely followed index of large European companies. The volatility has been
calculated using three methods: close-to-close, high-low (Parkinson), and openhigh, low-close (Garman-Klass). The last two methods seem to yield a consistently lower volatility than the first method. The explanation probably has to
do with the fact that Parkinson and Garman-Klass are used only when markets
are open and trading is continuous. But the EuroStoxx 50 Index is not calculated continuously. It is calculated during a period of just under 10 hours, from
approximately 9:00 a.m. to 6:50 p.m. European time. During the remaining
hours of the day, the volatility of the index is unobservable. Because of this,
for contracts that trade only during part of the day, Garman and Klass recommend giving some weight to the close-to-close estimate. One approach is to
give the observable volatility (either Parkinson or Garman-Klass) weight proportional to the fraction of the day during which the market is open and give
the remaining weight to the close-to-close volatility. This usually means giving
greater weight to the close-to-close volatility estimate because many markets
are closed more hours than they are open. But the Parkinson and Garman-
Klass methods are generally considered more accurate estimates, at least when
a market is trading continuously. Thus, it might make more sense to increase
the weightings for these estimates and reduce the weightings for the close-toclose estimate. Garman and Klass propose a precise formula for weighting
the estimates, but a practical solution might be to simply weight the estimates
equally.
Because we have gone into the calculation of historical volatility in some
detail, the reader may have been left with the impression that the method
3Mark B. Garman and Michael J. Klass, “On the Estimation of Security Price Volatilities from Historical
Data,” Journal of Business 53(1):67–78, 1980.
--- page 404 ---

V o l at i l i t y R e v i s i t e d 	 387
chosen will be an important determinant of whether an option strategy is successful or not. For most traders, though, historical volatility is simply a guideline
to what the trader is really interested in—the future realized volatility. Because
the results of each method are unlikely to differ significantly, in practice, it
probably does not make much difference which method is chosen. It is far more
important to be able to interpret historical volatility data rather than to worry
about the exact method used.
Some Volatility Characteristics
In Chapter 6, we used the analogy that the volatility in its different interpretations—historical, future, implied—is similar to the weather. The volatilityweather analogy can also help us identify some basic volatility characteristics.
Suppose that we are trying to estimate tomorrow’s high temperature,
and we have only one piece of information, today’s high temperature. What
is our best estimate? Because temperatures do not usually change dramatically from one day to the next, our best estimate of tomorrow’s high temperature is probably the same as today’s high temperature. Temperature
readings are said to be serial correlated. In the absence of other information,
the best guess about what will happen over the next time period is what happened over the last time period. Volatility seems to exhibit this serial correlation characteristic. What will happen in the future often depends on what
happened in the past.
Figure 20-3  EuroStoxx 50 Index three-month historical volatility: 2001–2010.
Annualized volatility
60%
Dec-00
Dec-01
Dec-02
Dec-03
Dec-04
Dec-05
Dec-06
Dec-07
Dec-08
Dec-09
Dec-10
50%
40%
30%
20%
10%
0%
Close-to-close
High-low (Parkinson)
Open-high, low-close (Garman-Klass)
--- page 405 ---

388
O P T I O N V O L AT I L I T Y A N D P R I C I N G
Now suppose that we know not only today’s high temperature but we also
know the average high temperature at this time of year. If today’s high temperature is higher than the average, an intelligent estimate for tomorrow’s high probably will be lower than today’s high. If today’s high temperature is lower than
the average, an intelligent estimate for tomorrow’s high will be higher than today’s high. We know that temperatures tend to be mean reverting. Volatility also
seems to exhibit this characteristic. There is a greater likelihood that volatility,
like temperature, will move toward the mean rather than away from it.
We can see the mean-reverting characteristic of volatility if we compare
Figure 20-2, the three-month volatility of gold, with Figure 20-4, the price of
gold over the same period.4 Both prices and volatility sometimes rise and sometimes fall. But unlike the price of an underlying contract, which can move in
one direction for long periods of time, there seems to be an equilibrium number to which volatility tends to return. Over the 10-year period in question,
the price of gold rose from under $300 per ounce to over $1,400 per ounce.
Although prices fluctuated, they never again reached the lows of 2001. On the
other hand, gold volatility, in spite of dramatic fluctuations between a low of
9 percent and a high of over 40 percent, always seemed to return eventually to
the 10 to 20 percent range.
We might conclude from Figure 20-2 that gold tends to exhibit a long-term
average or mean volatility. When volatility rises above the mean, one can be fairly
certain that it will eventually fall back to its mean. When volatility falls below
4 Historical gold volatility in Figure 20-2 and Bund volatility in Figure 20-5 were calculated from settlement
prices of the front-month futures contract.
Figure 20-4  Gold futures prices: 2001–2010.
Gold price, dollars per ounce
1,600
Dec-00
Dec-01
Dec-02
Dec-03
Dec-04
Dec-05
Dec-06
Dec-07
Dec-08
Dec-09 Dec-10
1,400
1,200
1,000
800
600
400
200
--- page 406 ---

V o l at i l i t y R e v i s i t e d 	 389
the mean, one can be fairly certain that it will eventually rise to its mean. There
is a constant gyration back and forth through this mean.
Mean reversion is a common volatility characteristic of almost all traded
underlying contracts. Figures 20-1 and 20-5 show the three-month historical volatility, using daily returns, for the S&P 500 Index and Bund futures
from 2001 to 2010. In spite of the dramatic fluctuations, both the S&P 500
Index and Bund futures tend to exhibit a mean volatility to which both contracts
tend to return. In the case of the S&P 500 Index, this seems to be somewhere
between 15 and 20 percent. In the case of the Bund, a much less volatile contract, the mean volatility seems to be around 5 percent.
In Figures 20-6 through 20-8, we can see more clearly the mean-reverting
characteristic of volatility. These graphs show the minimum, maximum, and average realized volatilities for the S&P 500 Index, gold futures, and Bund futures
from 2001 to 2010 over time periods ranging from 2 to 300 weeks. For example, in Figure 20-6, if we consider every possible two-week period from 2001 to
2010, we can see that the minimum two-week volatility for the S&P 500 Index
was approximately 5 percent, while the maximum two-week volatility was just
over 100 percent. The average two-week volatility was approximately 18 percent. For every possible 300-week period, the minimum volatility for the S&P
500 Index was approximately 14 percent, the maximum volatility was 24 percent, and the average volatility was approximately 19 percent. The graphs for
the gold futures (Figure 20-7) and for Bund futures (Figure 20-8) show the same
Figure 20-5  Bund futures three-month historical volatility: 2001–2010.
Annualized volatility
10%
Dec-00
Dec-01
Dec-02
Dec-03
Dec-04
Dec-05
Dec-06
Dec-07
Dec-08
Dec-09
Dec-10
8%
6%
4%
2%
0%
--- page 407 ---

390
O P T I O N V O L AT I L I T Y A N D P R I C I N G
Figure 20-6  S&P 500 Index historical realized volatility by time period: 2001–2010.
Annualized volatility
100%
0
50
100
150
200
250
Number of weeks in period
300
90%
80%
70%
60%
50%
40%
30%
20%
10%
0%
Maximum volatility
Minimum volatility
Average volatility
Figure 20-7  Gold futures historical realized volatility by time period: 2001–2010.
Annualized volatility
70%
0
50
100
150
200
250
Number of weeks in period
300
60%
50%
40%
30%
20%
10%
0%
Maximum volatility
Minimum volatility
Average volatility
--- page 408 ---

V o l at i l i t y R e v i s i t e d 	 391
general characteristics. As we increase the length of time over which the volatility is calculated, the results tend to converge to an average or mean volatility.
Graphs similar to those in Figures 20-6 through 20-8 are often used to
illustrate the term structure of volatility—the likelihood of volatility falling within a
given range over a specified period of time. The term-structure graph typically
has a conic shape, with greater variations over short periods of time and smaller
variations over long periods.5 Because of the term structure of volatility, it is
often easier to predict long-term volatility than short-term volatility. This may
seem counterintuitive because we tend to expect greater variability over long periods of time than over short periods. However, volatility can be thought of as an
average variability. Over long periods of time, the large and small price fluctuations tend to offset each other, resulting in more stable results.
Because long-term volatility tends to be more stable than short-term volatility, one might assume that it is easier to value long-term options than shortterm options. This would be true if all options were equally sensitive to changes
in volatility. But we know that long-term options have greater vega values than
short-term options—they are more sensitive to changes in volatility. This means
that any volatility error will be greatly magnified when evaluating a long-term
option. Depending on the time to expiration, the effect of a two or three percentage point volatility error on a long-term option may be greater than a five
or six percentage point error on a short-term option.
5 For additional discussion of volatility cones, see Galen Burghardt and Morton Lane, “How to Tell If Options
Are Cheap,” Journal of Portfolio Management, Winter:72–78, 1990.
Figure 20-8  Bund futures historical realized volatility by time period: 2001–2010.
Annualized volatility
14%
0
50
100
150
200
250
Number of weeks in period
300
12%
10%
8%
6%
4%
2%
0%
Maximum volatility
Minimum volatility
Average volatility
--- page 409 ---

392
O P T I O N V O L AT I L I T Y A N D P R I C I N G
What else can we say about volatility? Looking again at Figure 20-2, we
might surmise that volatility has some trending characteristics. From early 2004
through the middle of 2005, there was a persistent downward trend in gold volatility. This was followed by a more dramatic upward trend from the middle of
2005 to the middle of 2006. And from early 2007 through most of 2008, there
seemed to be a stepping-stone increase in volatility to a high of over 40 percent.
Within these major trends, there were also minor trends as volatility rose and
fell for short periods of time. In this respect, volatility charts seem to display
some of the same characteristics as price charts, and it would not be unreasonable to apply some of the same principles used in technical analysis to volatility
analysis. It is important to remember, however, that although price changes and
volatility are related, they are not the same thing. If a trader tries to apply exactly the same rules of technical analysis to volatility analysis, he is likely to find
that in some cases the rules have no relevance and that in other cases the rules
must be modified to take into account the unique characteristics of volatility.
Volatility Forecasting
How can we use historical volatility data, together with the characteristics of
volatility, to predict future realized volatility? Suppose that we have the following historical volatility data for an underlying contract:

6-week historical volatility:
28 percent

12-week historical volatility:
22 percent

26-week historical volatility:
19 percent

52-week historical volatility:
18 percent
We might prefer to look at more volatility data, but if these are the only data
available, how should we go about making a volatility forecast?
One possible approach is to simply average all the available data:
(28% + 22% + 19% + 18%)/4 = 21.75%
Using this method, each piece of historical data is given equal weight. But is
this reasonable? Perhaps some data are more important than other data. A
trader might assume, for example, that the more current the data, the greater
their importance. Because the 28 percent volatility over the last six weeks is
more current than the other volatility data, perhaps 28 percent should play
a greater role in our volatility forecast. We might, for example, give twice the
weight, 40 percent, to the six-week volatility but only 20 percent weight to each
of the other time periods:
(40% × 28%) + (20% × 22%) + (20% × 19%) + (20% × 18%) = 23.0%
Our volatility forecast has increased slightly because of the additional weight
given to the six-week historical volatility.
Of course, if it is true that the more recent volatility over the last 6 weeks
is more important than the other data, it follows that the volatility over the
--- page 410 ---

V o l at i l i t y R e v i s i t e d 	 393
last 12 weeks ought to be more important than the volatility over the last 26
and 52 weeks. It also follows that the volatility over the last 26 weeks must be
more important that the volatility over the last 52 weeks. We can factor this
into our forecast by using a regressive weighting, giving more distant volatility
data progressively less weight in our forecast. For example, we might calculate
(40% × 28%) + (30% × 22%) + (20% × 19%) + (10% × 18%) = 23.4%
Here we have given the 6-week volatility 40 percent of the weight, the 12-week
volatility 30 percent of the weight, the 26-week volatility 20 percent of the
weight, and the 52-week volatility 10 percent of the weight.
We have made the assumption that the more recent the data, the greater
their importance. Is this always true? If we are interested in evaluating shortterm options, it may be true that data that cover short periods of time are the
most important. But suppose that we are interested in evaluating very long-term
options. Over long periods of time, the mean-reverting characteristic of volatility is likely to reduce the importance of any short-term fluctuations in volatility.
In fact, over very long periods of time, the most reasonable volatility forecast is
simply the long-term mean volatility of the instrument. Therefore, the relative
weight we give to the different volatility data will depend on the amount of time
remaining to expiration for the options in which we are interested.
In a sense, all the historical volatilities we have at our disposal are current;
they simply cover different periods of time. How do we know which data are the
most important? In addition to the mean-reverting characteristic, we know that
volatility also tends to be serial correlated. The volatility over any given period
is likely to depend on, or correlate with, the volatility over the previous period,
assuming that both periods cover the same amount of time. If the volatility of
a contract over the last four weeks was 15 percent, the volatility over the next
four weeks is more likely to be close to 15 percent than far away from 15 percent. Once we realize this, we might logically choose to give the greatest weight
to the volatility data covering a time period closest to the life of the options in
which we are interested. That is, if we are trading very long-term options, the
long-term data should be given the most weight. If we are trading very shortterm options, the short-term data should be given the most weight. And if we
are trading intermediate-term options, the intermediate-term data should be
given the most weight.
Given the serial correlation characteristic of volatility, what volatility
should we assign to options that expire in five months if we have only our
four historical volatilities: 6-week, 12-week, 26-week, and 52-week volatilities?
Because 5 months is closest to 26 weeks, we can give the 26-week volatility the
greatest weight and give other data correspondingly lesser weight
(15% × 28%) + (25% × 22%) + (35% × 19%) + (25% × 18%) = 20.85%
Alternatively, if we are interested in evaluating 3-month options, we can
give the greatest weight to the 12-week historical volatility
(25% × 28%) + (35% × 22%) + (25% × 19%) + (15% × 18%) = 22.15%
--- page 411 ---

394
O P T I O N V O L AT I L I T Y A N D P R I C I N G
In the foregoing examples, we used only four historical volatilities. But the
more volatility data that are available, the more accurate any volatility forecast
is likely to be. Not only will more data, covering different periods of time, give
a better overview of the volatility characteristics of an underlying instrument,
they will also enable a trader to more closely match historical volatilities to options with different periods of time to expiration. In our examples, we used historical volatilities over the last 12 and 26 weeks as approximations to forecast
volatilities over the next six and three months. Ideally, we would like historical
data covering exactly sixand three-month periods.
This approach to forecasting volatility is one that many traders use intuitively. It depends on identifying the typical characteristics of volatility and then
projecting a volatility over some future period.
The analysis of a data series in order to predict future values falls into an
area of study usually referred to as time-series analysis. We might wish to apply
time-series models to volatility forecasting, but to do so, we need a series of data
points where each point is independent of every other point. In our examples,
the volatilities we used to make our prediction do not form a true time series because the volatilities overlap and, as such, are not really independent of each
other. The 52-week volatility overlaps the 26-, 12-, and 6-week volatilities. The
26-week volatility overlaps the 12- and 6-week volatilities. And the 12-week volatility overlaps the 6-week volatility. But suppose that instead of using as our data
points, the historical volatilities, we use the underlying returns. These returns
create a true time series to which we might be able to apply a time-series model.
One time-series model often used to estimate future volatility is the exponentially weighted moving average (EWMA) model. In this model, greater weight
is always given to more recent returns, with older returns given progressively
smaller weightings. If α is the weighting assigned to each return r, then the estimated variance (the square of the standard deviation) σ2 over the next period
of time is given by
r
r
r
n
n
nr
2
1 1
2
2 2
2
1
1
2
n
2

σ = α
+ α
+
+ α
+ α
−
−
where rn is the most recent return. The constraints are that all the weightings
must add up to 1.00
1.00
i
i
n
1∑α =
=
and that the more recent the return, the greater is the weighting
n
n 1
α > α −
By choosing a variable λ between 0 and 1.00, the constraints will be met if
(1
)
1
i
i
n
1
α = λ
−λ
−λ
−
--- page 412 ---

V o l at i l i t y R e v i s i t e d 	 395
As we reduce the value of λ, more recent returns are assigned progressively
greater weight—the variance estimate tends to discount the effect of older
returns. As we increase the value of λ, the estimate makes less and less distinction between returns—older returns become just as important as newer
returns. As λ approaches 1.00 (it can never be exactly 1.00), the weight for all
returns converges to a single value, 1.00/n. A common choice for λ in many
risk-management programs is something close to 0.94.
The EWMA model is relatively simple method for predicting volatility.
Two factors that it ignores are the likely correlation between successive returns
and the mean-reversion characteristic of volatility. The time-series models
most often used to forecast volatility were an outgrowth of the autoregressive conditional heteroskedasticity (ARCH) model first proposed by Robert Engle in 1982.6
The techniques used in ARCH models have subsequently been refined and
extended into what is now commonly referred to as the generalized autoregressive conditional heteroskedasticity (GARCH) family of volatility forecasting models. GARCH models consist of three components: a volatility estimate, such
as EWMA; a correlation component reflecting the fact that the magnitude of
successive returns tends to be correlated (i.e., large returns tend to be followed
by large returns, and small returns tend to be followed by small returns); and a
mean-reversion component specifying how fast volatility tends to revert to its
mean. An in-depth discussion of GARCH models is beyond the scope of this
text, but further information on these models is available in most advanced
texts on time-series analysis.
Implied Volatility as a Predictor of Future Volatility
If, as many traders believe, prices in the marketplace reflect all available information affecting the value of a contract,7 the best predictor of the future realized volatility ought to be the implied volatility. Just how good a predictor of
future volatility is implied volatility? Although it may be impossible to answer
this question definitively, because that would require a detailed study of many
markets over long periods of time, we still might gain some insight by looking
at sample data.
Figure 20-9 shows the three-month realized volatility (approximately 63
trading days) for the S&P 500 Index and a rolling implied volatility for threemonth at-the-money options8 on the index from 2002 through 2010. However,
the values for the three-month realized volatility have been shifted forward
so that each data point represents the future realized volatility of the index
over the next three months. If implied volatility is a perfect predictor of future
volatility, both graphs would be identical, but obviously, this is not the case.
6 Robert F. Engle, “Autoregressive Conditional Heteroskedsticity with Estimates of the Variance of United
Kingdom Inflation,” Econometrica 50(4):987–1000, 1982. Engle was awarded the 2003 Nobel Prize in
Economics.
7 This is known in finance as the efficient-market hypothesis.
8 The three-month implied volatility was calculated by interpolating between the implied volatility of options
bracketing three months.
--- page 413 ---

396
O P T I O N V O L AT I L I T Y A N D P R I C I N G
In general, the volatility of the S&P 500 Index tends to lead the implied volatility. If the index becomes more volatile, implied volatility rises; if the index
becomes less volatile, implied volatility falls. The marketplace seems to react
to the volatility of the index. This was particularly evident during 2008, when
implied volatility rose following the dramatic increase in volatility of the index,
and in 2009, when implied volatility fell as the index itself became less volatile.
We can do the same comparison using a 12-month period. Figure 20-10
shows the 12-month future realized volatility of the S&P 500 Index (approximately 252 trading days) versus a rolling 12-month at-the-money implied volatility over the same time period. Here the lag is even more evident due to the
longer time frame.
Clearly, the implied volatility in our examples did not accurately predict
future volatility. But, even if the implied volatility was not a totally accurate
predictor, perhaps we can draw some conclusions by looking at the difference
between the implied volatility and the future realized volatility. This is shown in
Figure 20-11 for both 3- and 12-month options. A positive value indicates an
implied volatility that was too low (the future realized volatility turned out to be
higher), while a negative value indicates an implied volatility that was too high
(the future realized volatility turned out to be lower).
We can see in Figure 20-11 that for much of the period in question,
implied volatility seemed to predict a future volatility that was too high by up
to 10 percentage points. But there are some dramatic exceptions. During 2008,
Figure 20-9  S&P 500 Index three-month future volatility versus the three-month implied
volatility.
Annualized volatility
80%
Dec-01
Dec-02
Dec-03
Dec-04
Dec-05
Dec-06
Dec-07
Dec-08
Dec-09
Dec-10
70%
60%
50%
40%
30%
20%
10%
0%
3-month future realized volatility
3-month implied volatility
--- page 414 ---

V o l at i l i t y R e v i s i t e d 	 397
Figure 20-10  S&P 500 Index 12-month future volatility versus the 12-month implied volatility.
Annualized volatility
80%
Dec-01
Dec-02
Dec-03
Dec-04
Dec-05
Dec-06
Dec-07
Dec-08
Dec-09
Dec-10
70%
60%
50%
40%
30%
20%
10%
0%
12-month future realized volatility
12-month implied volatility
Figure 20-11  Difference between future volatility and implied volatility for the S&P 500 Index.
Future realized volatility minus implied volatility
+50%
Dec-01
Dec-02
Dec-03
Dec-04
Dec-05
Dec-06
Dec-07
Dec-08
Dec-09
Dec-10
+40%
+30%
+20%
+10%
0%
–10%
–20%
–30%
September 8, 2008: 3-month future volatility = 72%

Implied volatility = 22%
3-month future volatility less 3-month implied volatility
12-month future volatility less 12-month implied volatility
November 20, 2008: 3-month future volatility = 45%

Implied volatility = 65%
the three-month implied volatility at one point predicted a future volatility that
was too low by almost 50 percentage points and at another point predicted a
volatility that was too high by 20 percentage points. Admittedly, 2008 was a year
--- page 415 ---

398
O P T I O N V O L AT I L I T Y A N D P R I C I N G
of extremes, but even during other years, a difference of 10 percentage points
between implied volatility and future volatility was not uncommon.
Implied volatility is at best an imperfect predictor of future volatility.
What else might we conclude from these graphs? Under normal conditions,
implied volatility seems to be too high—options tend to be overpriced. Buyers of
options may be willing to pay this extra premium in return for the few occasions when implied volatility is dramatically too low and there is a subsequent
volatility explosion. This is analogous to insurance. A rational buyer of insurance is aware that the price of an insurance contract is almost certainly higher
than its value. Otherwise, the insurance company would have no profit expectation. But buyers of insurance are willing to pay this extra premium for those
rare occasions when an unforeseen event occurs and the insurance becomes
absolutely necessary.
There are, of course, other reasons why options tend to be overpriced. For
the seller of an option, such as a market maker, there may be a cost to replicating the option through the dynamic hedging process, a cost that the market
maker is likely to pass on to the customer. Moreover, there may be weaknesses in the theoretical pricing model from which implied volatility is derived.
Taken together, these factors may in fact justify the seemingly inflated prices of
options in the marketplace.
The Term Structure of Implied Volatility
If held to expiration, the sole determinant of an option position’s value is, in
theory, the realized volatility of the underlying contract. However, a trader
may decide for a variety of reasons that a position should be closed prior to expiration. The position may have achieved its expected profit potential prior to
expiration. Or the position, even if it hasn’t achieved its expected profit, may
have become too risky. Or holding the position may require a large amount
of capital, capital that could be put to better use. Regardless of why a trader
decides to close out a position prior to expiration, there is usually one primary
cause: changes in implied volatility. Although we have emphasized the importance of realized volatility, in the real world of option trading, changes in implied volatility can often make or break a strategy. For this reason, a sensible
trader will give some thought to how changes in implied volatility will affect a
position.
It may seem that determining the sensitivity of a position to changes in
implied volatility is relatively simple. We need only determine the total position vega, which we can do by adding up all the individual vega values. Unfortunately, determining the true implied volatility risk can be significantly more
complex. We know that vega values change with changing market conditions,
so today’s vega may not be tomorrow’s vega. Moreover, the vega values across
different exercise prices and expiration months may not be a true reflection of
implied-volatility risk.
Consider a market where there are three expiration months, all in the same
calendar year—March, June, and September. Let’s assume that the mean volatility in this market is 25 percent, and although this almost never happens,
--- page 416 ---

V o l at i l i t y R e v i s i t e d 	 399
let’s also assume that the current implied volatility for every month is the same,
25 percent.
March
June
September
Implied volatility
25%
25%
25%
Suppose that the volatility of the underlying contract begins to rise. What
will happen to implied volatility? Implied volatility will almost certainly rise,
but will it rise at the same rate for each month? If the implied volatility for
March rises to 30 percent, will the implied volatility of June and September
also rise to 30 percent? Traders know that volatility is mean reverting, and there
is a greater likelihood that volatility will revert to its mean over long periods of
time than over short periods. Therefore, as we move to more distant expirations, implied volatility is likely to remain closer to its mean, in this case, 25 percent. The new implied volatilities might be
March
June
September
Implied volatility
30%
28%
26%
Mean reversion will also affect falling implied volatility. If the underlying
market becomes less volatile and implied volatility in March falls to 20 percent,
the new implied volatilities might be
March
June
September
Implied volatility
20%
22%
24%
Even if there is a large change in the implied volatility of short-term
options, the implied volatility of long-term options will tend to change less
because of the mean-reversion characteristics of volatility. Figure 20-12 shows
the typical term structure of implied volatility.
The fact that implied volatilities across different expiration months change
at different rates can have important implications for risk analysis. Consider an
option position consisting of four different expiration months with the following vega values for each month:
April
June
August
October
Time to expiration
2 months
4 months
6 months
8 months
Total vega
+15.00
–36.00
–21.00
+42.00
What is the implied-volatility risk of the position? We might begin by adding
up all the vegas
+15.00 – 36.00 – 21.00 + 42.00 = 0
With a total vega of 0, it might appear that there is no implied-volatility risk.
This, however, assumes that implied volatility will change at the same rate
across all months. But we know that this is unlikely. The implied volatility of
--- page 417 ---

400
O P T I O N V O L AT I L I T Y A N D P R I C I N G
short-term options will tend to change more quickly than the implied volatility of long-term options. Given this, how should we determine our total
implied-volatility risk?
Suppose that the mean volatility in this market is 25 percent and that we
believe that the term structure of implied volatility is similar to that shown
in Figure 20-13. If April implied volatility rises to 28 percent, what will be
the profit or loss to the position? If there are two months remaining to April
expiration and implied volatility in April rises to 28 percent, we expect June
implied volatility to rise to only 27 percent, August implied volatility to only
26.5 percent, and October to only 26.1 percent. Adjusting for the different
rates of change, the result is a loss because
(3 × 15.00) – (2 × 36.00) – (1.5 × 21.00) + (1.1 × 42.00) = –12.30
And if April implied volatility falls to 22 percent, the result will be reversed;
we will show a profit of 12.30. Clearly, the position is not vega neutral. We would
much prefer implied volatility to fall than rise.
In order to form a more accurate picture of the implied-volatility risk, we
must adjust the vega values for each month. We know that for each percentage
point change in April implied volatility, June implied volatility will change by
2/3 = 0.67
Figure 20-12  The term structure of implied volatility.
Implied volatility
Mean volatility
Short-term options
Long-term options
Time to expiration
--- page 418 ---

V o l at i l i t y R e v i s i t e d 	 401
For each percentage point change in April implied volatility, August implied
volatility will change by
1.5/3 = 0.50
And for each percentage point change in April implied volatility, October
implied volatility will change by
1.1/3 = 0.37
If we want to know our total implied-volatility risk in terms of changes in April
implied volatility, we can adjust our vega values accordingly
June vega = –36.00 × 0.67 = –24.12
August vega = –21.00 × 0.5 = –10.50
October vega = +42.00 × 0.37 = +15.54
Adding everything up, we can see that we do indeed have a short vega position.
For each percentage point change in April implied volatility, the value of the
total position will change by
+15.00 – 24.12 – 10.50 +15.54 = –4.08
Figure 20-13  Relative changes in implied volatility for April, June, August, and October options.
Implied volatility
30%
0
2
4
8
6
(April)
(June)
(August)
Months to expiration
(October)
10
12
29%
28%
27%
26%
25%
24%
23%
22%
21%
20%
3.0
2.0
1.5
1.1
3.0
2.0
1.5
1.1
--- page 419 ---

402
O P T I O N V O L AT I L I T Y A N D P R I C I N G
In order to accurately assess implied-volatility risk, a trader will need some
method of determining how implied volatilities are likely to change across multiple expirations. This usually takes the form of an implied-volatility termstructure model. There is no single model that all traders use. Models are often
“home grown,” with a trader trying to develop a model that is consistent with his
mathematical sophistication, as well as his experience in the marketplace. Whatever the model, it will usually require at least three inputs: a primary month against
which all other months will be compared, a mean volatility to which implied
volatility tends to revert, and a “whippiness” factor that specifies how implied
volatility changes across other expirations with respect to changes in the primary
month. The primary month will often be the front month, where trading activity tends to be concentrated. But this is not always the case. In agricultural markets, trading activity is often concentrated in expiration months that fall close to
either the planting or harvesting calendar. If this is the case, one of these months
may be a better choice as the primary month. Additionally, implied volatility in
the front month can be unstable, especially as expiration approaches. It often
changes in ways that are inconsistent with the term structure of other expiration
months. As a result, many traders evaluate their position in front-month contracts separately from their positions in other months, with the volatility termstructure model applying to all months except the front month. The primary
month chosen in this approach will be something other than the front month.
Figure 20-14 shows how the term structure of implied volatility can evolve
over time. The values represent the implied volatilities during 2010 of atthe-money options on the EuroStoxx 50 Index for expirations extending out
24 months. Values were calculated at two-month intervals, on the first Friday
of February, April, June, August, October, and December. The reader may
find it useful to compare the changes in the term-structure graphs with the
30-day historical volatility of the EuroStoxx 50 Index during this period,
shown in Figure 20-15. In early February, the term-structure graph was downward sloping: long-term options were trading at lower implied volatilities than
short-term options. By April, as a result of declining index volatility, not only
had implied volatility declined, but the term-structure graph had inverted and
was upward sloping: long-term options were trading at higher implied volatilities than short-term options. After a dramatic increase in index volatility, the
June term-structure graph again became downward sloping. Finally, after declining index volatility in the last half of 2010, implied volatilities seemed to
settle into a middle area, with a relatively flat term structure.
Note one other important point: the disconnect between the front-month
implied volatility and the remainder of the term-structure graph in December.
The graph is generally upward sloping, but the front-month implied volatility
is still much higher than all other months. This is a common characteristic in
many option markets. The front-month implied volatility can often trade in a
way that is inconsistent with the term structure of other months.
The term structure in Figure 20-12 is typical of markets where the only
factors that tend to affect implied volatility are the recent volatility of the underlying contract and the mean volatility. However, in some markets, there may
also be a seasonal volatility factor.
