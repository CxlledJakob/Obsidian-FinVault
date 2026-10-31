# Volatility Trading_ Sinclair_Volatility Trading -- Euan Sinclair(auth_) -- Wiley Trading, 1, 2013 -- John Wiley & Sons, Incorporated -- isbn13 9781118347133 -- 2634a86bfed8248fa7ba3fb72595bbbc -- Anna’s Archive.pdf — Chapter 3: Stylized Facts about Returns and Volatility (pages 53–65)

--- page 53 ---

35
C H A P T E R 3
Stylized Facts
about Returns
and Volatility
I
n Chapter 1, we learned why we would want to measure and forecast
volatility and in Chapter 2, we learned how to do this. Now we need to
see how volatility actually behaves.
■Deﬁnition of a Stylized Fact
In the study of ﬁnancial data, a stylized fact is a feature that is consistent
enough to be generally accepted as truth. Many traders and most ﬁnancial
journalists have an event-based approach to understanding markets. Moves
are explained or rationalized by connecting them to a particular piece of
news. As different assets are affected by entirely different news items, in
this paradigm we would not necessarily expect to see any commonality in
their price series. For example, Apple (AAPL) and gold are very different
things. Why would their price series have any similarities at all?
However, econometric studies have shown remarkable amounts of
similarity in ﬁnancial time series. The variations of asset prices share a
number of nontrivial statistical properties. These have become known as
stylized facts. The qualiﬁer is important: These are generalities. Gaining
generality allows us to see broad similarities, but we also lose some ability
to make precise statements. In fact, many of the facts we look at will be
qualitative.
Volatility Trading,   Second Edition.    Euan Sinclair
© 2013 Euan Sinclair. Published 2013 by John Wiley & Sons, Inc.
--- page 54 ---

STYLIZED FACTS ABOUT RETURNS AND VOLATILITY
36
It is surprisingly difﬁcult to incorporate all these features into models
of the underlying, let alone option pricing models. Often our knowledge
isn’t even sufﬁcient to distinguish between competing explanations. But as
we have already said, we aren’t looking for a model that captures these
features. Instead we will use a number of tweaks and fudges to incorporate
the facts into our use of the Black-Scholes-Merton (BSM) formalism and the
volatility estimation problem. As traders of volatility, we naturally need to
know as much as possible about it.
There are a number of excellent reviews and surveys of stylized facts.
See, for example, Cont (2001).
List of Stylized Facts
■Volatility is not constant. It mean-reverts, clusters, and possesses long
memory.
■Large returns occur relatively frequently. These large moves have subsequent aftershocks.
■In most markets, volatility and returns have a negative correlation. This
effect is asymmetric: negative returns cause volatility to rise sharply while
positive returns lead to a smaller drop in volatility. This effect occurs
most prominently in equity markets.
■Volatility and volume have a strong positive relationship.
■The distribution of volatility is close to log-normal.
■Volatility Is Not Constant
This fact has been documented in a number of studies. See, for example,
Akgiray (1989) or Turner and Weigel (1992). The effect is robust to the
exact way volatility is estimated and is easy to visually conﬁrm. Figure 3.1
shows the 30-day close-to-close volatility of SPY from 2000 to 2011.
Not only does volatility change but, more interestingly, it changes in
speciﬁc ways. First, volatility clusters. This appears to have been ﬁrst noted
by Mandelbrot (1963) who said, ‘‘Large changes tend to be followed by
large changes . . . and small changes tend to be followed by small changes.’’
Speciﬁcally both squared returns and absolute returns (proxies for one-day
volatility) display signiﬁcant autocorrelation. Figures 3.2 and 3.3 show these
autocorrelations for the S&P 500 as a function of various lags.
The size and persistence of these autocorrelations is in contrast to the
lack of autocorrelation we see with returns. Figure 3.4 shows return
--- page 55 ---

STYLIZED FACTS ABOUT RETURNS AND VOLATILITY
37
0
0.05
0.1
0.15
0.2
0.25
0.3
2/15/2000
8/14/2000
2/12/2001
8/10/2001
2/14/2002
8/14/2002
2/12/2003
8/12/2003
2/10/2004
8/10/2004
2/7/2005
8/5/2005
2/3/2006
8/3/2006
2/2/2007
8/2/2007
1/31/2008
7/30/2008
1/28/2009
7/28/2009
1/26/2010
7/26/2010
1/21/2011
7/21/2011
Date
30-Day Volatility
FIGURE 3.1
The 30-Day Close-to-Close Volatility for SPY from January 2000 until
December 2011
0
0.05
0.1
0.15
0.2
0.25
1
3
5
7
9
11
13
15
17
19
21
23
25
27
29
Lag (days)
Autocorrelation of Squared Returns
FIGURE 3.2
Autocorrelations for the Squared Returns of the S&P 500 from 1950
to 2011
autocorrelation for the S&P 500 as a function of various lags over the same
period. They are practically indistinguishable from zero.
Volatility clustering does not depend on the underlying product. It has
been observed in indices, stocks, commodities, and currencies (Taylor
1986). It is also generally true that absolute returns are more highly
correlated than the squared returns. The slow decay of the autocorrelation
function is also referred to as ‘‘long memory.’’
Clustering means that a good estimate of future volatility is whatever
current volatility is. Option traders have internalized the rule of thumb that
--- page 56 ---

STYLIZED FACTS ABOUT RETURNS AND VOLATILITY
38
0
0.05
0.1
0.15
0.2
0.25
0.3
0.35
1
3
5
7
9
11
13
15
17
19
21
23
25
27
29
Lag (days)
Autocorrelation of Absolute Returns
FIGURE 3.3
Autocorrelations for the Absolute Returns of the S&P 500 from 1950
to 2011
–0.05
–0.04
–0.03
–0.02
–0.01
0
0.01
0.02
0.03
0.04
1
3
5
7
9
11
13
15
17
19
21
23
25
27
29
Lag (days)
Autocorrelation of Returns
FIGURE 3.4
Autocorrelations for the Absolute Returns of the S&P 500 from 1950
to 2011
says tomorrow’s volatility will be the same as today’s. They generally do
not even think how remarkable this is. The underlying price certainly does
not have this property, which is the ﬁrst reason that volatility is relatively
predictable.
There are a few other facts to note about volatility clustering:
■The clustering tends to be larger in developed markets than in emerging
markets.
--- page 57 ---

STYLIZED FACTS ABOUT RETURNS AND VOLATILITY
39
■The clustering is more pronounced during bear markets than during
rallies, but the decay of the autocorrelations is also faster in bear markets.
■During crashes or other huge panics, the autocorrelation decays fastest.
The other stylized fact that aids forecasting is that the volatility is meanreverting. As the positive autocorrelations eventually decay, short-term
volatility reverts to the long-term mean. A robust test for mean reversion is
the variance ratio test of Campbell, Lo, and MacKinlay (1997). When the
volatility measured from daily returns is greater than that which is measured
from longer returns, we have mean reversion. This is because the market is
ﬂuctuating but not going anywhere over the longer term. For example, the
Volatility Index (VIX) has an annualized daily volatility of 0.96 (from 1990
to 2011), an annualized weekly volatility of 0.84 and an annualized monthly
volatility of 0.59. Realized volatility is similar.
While volatility is mean-reverting, it is often not obvious what the
current value of the mean is. This is true of many things in life. Short-term
ﬂuctuations oscillate around a slowly changing mean value. Consider again
our lucky baseball hitter who gets ﬁve hits in ﬁve at bats. It is clear that
this isn’t a reasonable estimate of his true talent, and we expect some
reversion. But does he revert to the .277 average of the previous year
or the .300 average of his career? The changing mean value of volatility
can be signiﬁcant. Figures 3.5 and 3.6 show the VIX (the CBOE S&P 500
implied volatility index), and its mean, in two different time periods. Each
is mean-reverting, but to a very different mean.
0
5
10
15
20
25
30
35
40
45
50
1/3/2000
1/3/2001
1/3/2002
1/3/2003
Date
VIX
FIGURE 3.5
The VIX and Its Mean Value from 2000 to 2003
--- page 58 ---

STYLIZED FACTS ABOUT RETURNS AND VOLATILITY
40
0
5
10
15
20
25
30
1/2/2004
1/2/2005
1/2/2006
Date
VIX
FIGURE 3.6
The VIX and Its Mean Value from 2004 to 2006
The interplay between clustering (positive autocorrelation) and mean
reversion dominates the dynamics of volatility.
■Characteristics of the Return Distribution
The returns of ﬁnancial instruments are not normally distributed. In
particular, they are skewed (usually negatively) and have fat tails (excess
kurtosis). The presence of fat tails mean that large moves occur far more
frequently than we would expect if the returns were normally distributed.
The existence of fat tails is far from a recent observation being noted at least
as early as 1927 by Mills (1927).
Between 1950 and 2011, the daily logarithmic returns of the S&P 500
have had an excess kurtosis of 21.3. There have been 24 days with returns
less than negative 5 percent and 17 days with returns greater than 5 percent.
The worst day (October 19, 1987) had a return of −20.47 percent. If
the returns were normally distributed with a volatility of 20 percent, the
probability of such a decline is about 10−88.
Figure 3.7 shows the realized daily returns as well as those from the
normal distribution.
The relative preponderance of large moves is a general feature of markets
and during all periods. Table 3.1 gives the excess kurtosis for a number of
underlyings.
--- page 59 ---

STYLIZED FACTS ABOUT RETURNS AND VOLATILITY
41
0
0.05
0.1
0.15
0.2
0.25
0.3
–0.1
–0.05
0
0.05
0.1
% Returns
Proportion of Returns
FIGURE 3.7
The S&P 500 Daily Percentage Returns (Solid Line) and Those
from a Normal Distribution (Dashed Line)
TABLE 3.1
Excess Kurtosis for a Number of Markets
Market
Period
Excess
Kurtosis
Gold
2005–2011
5.1
WTI Oil
2006–2011
2.1
Nasdaq
1971–2011
9.9
DAX 30
2000–2011
4.5
FTSE 100
1984–2011
7.9
Silver
2006–2011
5.1
Hang Seng
1986–2011
32.7
IBM
1962–2011
9.9
MSFT
1994–2011
6.4
GOOG
2005–2011
8.8
Another thing to note is that most of the kurtosis in stocks comes in the
overnight returns. This is shown in Table 3.2 for the Dow Jones Industrial
Index and its component stocks (the starting date of January 2002 was
chosen so that the stocks were traded in penny increments for the entire
period).
This effect is because many of the events that most affect stock prices are
released when the market is closed. The most obvious examples are earnings
--- page 60 ---

STYLIZED FACTS ABOUT RETURNS AND VOLATILITY
42
TABLE 3.2
Close-to-Open and Open-to-Close Kurtosis
for the Component Stocks of the Dow Jones
Industrial Average from 2002 to 2011
Underlying
Overnight
Excess
Kurtosis
Intraday
Excess
Kurtosis
Dow Jones 30
17.3
9.9
Alcoa
16.3
5.6
American Express
13.0
7.4
Boeing
13.6
2.4
Bank of America
34.7
16.4
Caterpillar
15.6
2.9
Cisco
27.1
3.3
Chevron
9.5
12.7
Du Pont
7.0
5.1
Disney
27.0
4.7
General Electric
24.5
9.4
Home Depot
13.7
5.4
Hewlett-Packard
31.4
3.4
IBM
25.7
3.5
Intel
29.8
2.9
Johnson & Johnson
119.4
7.1
JPMorgan Chase
16.4
12.6
Kraft Foods
49.0
4.1
Coca-Cola
13.5
7.5
McDonald’s
13.7
4.7
3M
15.2
4.4
Merck
132.0
6.8
Microsoft
26.0
5.2
Pﬁzer
48.6
3.0
Procter & Gamble
13.6
6.2
AT&T
10.5
6.0
Travelers
609.0
10.8
United Technologies
9.1
5.3
Verizon
9.6
6.1
Wal-Mart
12.4
4.9
Exxon Mobil
11.1
10.2
announcements that occur either after the close or before the open. Other
times, trading in a stock will be halted pending the release of news. Often
these stocks do not reopen until the next day. Interestingly, the two stocks
least affected are Exxon Mobil and Chevron. These are both oil companies
and often move when oil inventory ﬁgures are released. This takes place
during trading hours.
Another persistent effect is that volatility tends to increase when the
underlying price declines. This is also known as the leverage effect. This name
--- page 61 ---

STYLIZED FACTS ABOUT RETURNS AND VOLATILITY
43
came about as an explanation for the effect in equities. Assuming no debt is
issued, a fall in the stock price causes the company’s ﬁnancial leverage to
increase, which increases its risk. This leads to higher volatility. This sounds
plausible but doesn’t seem to explain the effect in practice (Figlewski and
Wang 2000).
This is not a new observation. It was mentioned in Black (1976) and
Christie (1982). Numerous studies have been published since. See, for
example, Edderington and Guan (2010) and Abura and Wagner (2010).
This effect is particularly prevalent for stock indices but is also true for
single stocks, bonds, and many commodities. It seems to be a feature of any
asset, which people invest in and hence has a positive expected return. For
example, it does not apply in general to currencies.
The asymmetry is also robust with respect to exactly how it is measured.
Most studies have looked at the correlations between returns and variances
(or volatilities) but other methods show the same broad effect. For example,
in a method similar in spirit to the ﬁrst exit time volatility discussed in
Chapter 2, Jensen, Johansen, and Simonsen (2003) analyze the ﬁrst exit
times for an asset to breach a corridor on the upside and the downside.
They show that the ﬁrst exit time is smaller for down moves than it is for
up moves.
Another simple way of noting the asymmetry is to calculate the average
size of positive returns and negative returns. Between 2000 and 2011, the
average positive daily return for SPY was 0.008891and the average negative
return was 0.01007. That is the average negative returns were just over
13 percent larger. The same was true for QQQ, with positive returns
averaging 0.013418 and negative returns averaging 0.01504 (a difference
of over 12 percent). Of the 24 years in this sample, the pattern held in all
but three (SPY in 2000, QQQ in 2003 and 2004).
Both fat tails and asymmetry are reﬂected in the structure of the implied
volatility surface. This is studied in Chapter 5.
■Volume and Volatility
Trading volume is heavily correlated with all measures of volatility. It is
difﬁcult to establish the causality in this relationship. Good arguments can be
made for trading volume moving the underlying price and causing volatility,
but also for volatility inducing investors to trade thus increasing volume.
However, the relationship itself is solid and holds over all timescales (when
overall market volume growth is controlled for). See, for example, Tauchen
and Pitts (1983) and Lee and Rui (2002).
--- page 62 ---

STYLIZED FACTS ABOUT RETURNS AND VOLATILITY
44
In Figures 3.8 and 3.9, we show the relationship by plotting daily volume
against daily absolute returns and the daily range for SPY during 2011.
It seems that the volatility-volume linkage is also related to the leverage
effect. Gallant, Rossi, and Tauchen (1993) ﬁnd that including lagged volume
signiﬁcantly diminishes the asymmetric response of volatility to return sign.
Andersen (1996) has proposed jointly estimating the dynamics of returns
and volume, but this line of research has not been widely developed. In
0
0.01
0.02
0.03
0.04
0.05
0.06
0.07
0.08
0
200,000,000
400,000,000
600,000,000
800,000,000
Daily Volume
Relative Daily Range
FIGURE 3.8
The SPY Daily Range Against the Daily Volume for 2011;
The Correlation Is 0.85
0
0.01
0.02
0.03
0.04
0.05
0.06
0.07
0
200,000,000
400,000,000
600,000,000
800,000,000
Daily Volume
Absolute Daily Return
FIGURE 3.9
The SPY Daily Absolute Return Against the Daily Volume for 2011;
The Correlation Is 0.68
--- page 63 ---

STYLIZED FACTS ABOUT RETURNS AND VOLATILITY
45
any case, it seems sensible that traders should take account of volume when
projecting volatility, even just as a ﬁnal ﬁlter to avoid taking false signals.
■Distribution of Volatility
A number of studies have suggested that the distribution of volatility is
log-normal (Andersen, Bollerslev, Diebold, and Ebbens 2001;Cizeau et al.
1997), but at least one (Liu et al. 1999) has indicated that the tail of
the distribution would be better described as a power law. The particular
distribution is probably unimportant. The important thing is that the
distribution is heavily skewed to the right with many more periods of high
volatility that we would expect if the distribution was normal. This is shown
in Figure 3.10, where we show the distribution of 30-day volatility for the
S&P 500 from 1990 to 2011.
An equivalent way of stating this is that volatility spends much more time
in low states than in high states.
As we might expect, the volatility distribution is signiﬁcantly different
in bull and bear markets. From 1990 to 2011, if the S&P 500 was below
its 200-day moving average, the median 30-day volatility was 21.6 percent.
If the S&P 500 was above the 200-day moving average, the median 30-day
volatility was 12.1 percent. The distributions of volatility in bull and bear
markets are shown in Figures 3.11 and 3.12. This observation is robust
0
0.02
0.04
0.06
0.08
0.1
0.12
0.14
0.16
0
0.04
0.08
0.12
0.16
0.2
0.24
0.28
0.32
0.36
0.4
0.44
0.48
0.52
0.56
0.6
0.64
0.68
0.72
0.76
0.8
0.84
Volatility
Proportion
FIGURE 3.10
The Distribution of the 30-Day Volatility of the S&P 500 from 1990
to 2011
--- page 64 ---

STYLIZED FACTS ABOUT RETURNS AND VOLATILITY
46
0
0.02
0.04
0.06
0.08
0.1
0.12
0.14
0
0.04
0.08
0.12
0.16
0.2
0.24
0.28
0.32
0.36
0.4
0.44
0.48
0.52
0.56
0.6
0.64
0.68
0.72
0.76
0.8
0.84
Volatility
Proportion
FIGURE 3.11
The Distribution of the 30-Day Volatility of the S&P 500 from 1990
to 2011 during Bear Markets (Underlying below Its 200-Day Moving Average)
0
0.02
0.04
0.06
0.08
0.1
0.12
0.14
0.16
0.18
0.2
0
0.04
0.08
0.12
0.16
0.2
0.24
0.28
0.32
0.36
0.4
0.44
0.48
0.52
0.56
0.6
0.64
0.68
0.72
0.76
0.8
0.84
Volatility
Proportion
FIGURE 3.12
The Distribution of the 30-Day Volatility of the S&P 500 from 1990
to 2011 during Bear Markets (Underlying below Its 200-Day Moving Average)
with respect to how we measure volatility, and the length of the moving
average we use to deﬁne whether the underlying market is in a bull or
bear phase.
■Summary
It is obvious that as volatility traders, we need to understand volatility. This
is true no matter what level of quantitative analysis we intend to use. Each
--- page 65 ---

STYLIZED FACTS ABOUT RETURNS AND VOLATILITY
47
individual product will have certain quirks and nuances, but all volatilities
have a number of common features.
■Volatility clusters.
■Volatility mean reverts.
■Stock returns are not normally distributed. In particular, the return
distribution has fat tails.
■Volatility tends to increase as the underlying price declines.
■Volatility and volume are highly correlated.
■Volatility is approximately log-normally distributed.
