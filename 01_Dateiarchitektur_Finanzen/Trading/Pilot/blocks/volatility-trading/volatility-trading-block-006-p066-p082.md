# Volatility Trading_ Sinclair_Volatility Trading -- Euan Sinclair(auth_) -- Wiley Trading, 1, 2013 -- John Wiley & Sons, Incorporated -- isbn13 9781118347133 -- 2634a86bfed8248fa7ba3fb72595bbbc -- Anna’s Archive.pdf — Chapter 4: Volatility Forecasting (pages 66–82)

--- page 66 ---

49
C H A P T E R 4
Volatility
Forecasting
I
n Chapter 2, we saw how to measure what volatility currently is. Next
we need to forecast what it will be over the lifetime of the option. This is
obviously more difﬁcult.
Successful trading demands successful forecasting. If traders cannot
forecast successfully, all of their other skills will be useless. However,
because markets are always changing, we will always be uncertain of our
true ability to do so. All we can ever really know is how we have performed
in the past.
But before we look at how to forecast volatility, we need to ask why
we think that it can be predicted. It is generally accepted (by academics at
least) that underlying returns are close to unpredictable. And the principal
reason for this is that if it were possible to forecast market direction, traders
would act on the predictions and push prices toward a level where no
more predictability existed. Why would this same argument not apply to
volatility? Even if traders are ﬁrmly of the opinion that markets are clearly
inefﬁcient they should pay attention to these arguments. Someone who
understands why and how markets can become efﬁcient will have better
insight into why and how they can become inefﬁcient.
In some of his early work on the Efﬁcient Market Hypothesis (EMH),
Fama (1970) gave three conditions that were sufﬁcient for efﬁciency. He
is careful to note that these may not be necessary conditions and that
something close to these conditions existing may be enough for efﬁciency,
but they are clearly a good place to start when thinking about why we hope
to make money from our predictions.
Volatility Trading,   Second Edition.    Euan Sinclair
© 2013 Euan Sinclair. Published 2013 by John Wiley & Sons, Inc.
--- page 67 ---

VOLATILITY FORECASTING
50
■Absence of Transaction Costs
Transaction costs involved in volatility trading take the form of brokerage,
bid/ask spreads, taxes, exchange fees, and clearing costs. Clearly, these are
not zero and are actually far larger than costs associated with trading stocks
or futures. In particular, to trade volatility through options a trader needs
to dynamically hedge. This is costly in terms of transaction costs and also
imposes considerable overhead cost associated with monitoring risk. The
existence of variance swaps may seem to be a counterpoint, but these only
trade bilaterally in the OTC market. These markets tend to be wider than
those listed on exchanges and traders are restricted to a limited number of
counterparties.
■Perfect Information Flow
News must ﬂow quickly and freely to all market participants. This is truer
now than it has been at any time in the past. But although there are
many good news services available at low cost, there is still a substantial
amount of option trading based on inside information (at least in equity
options) (Bradley, Cline, and Lian 2009; Arnold et al. 2000). This can be
very proﬁtable and there are strategies based on identifying such traders
and piggybacking their positions. Insider information is by deﬁnition not
available to everyone and is an example of imperfect information ﬂow.
■Agreement about the Price Implications
of Information
As we see in Chapter 5, option prices do not react instantaneously to public
news. In some cases it can take several weeks for prices to adjust. This
implies that there is some disagreement about the effect of the news.
So it seems like these conditions are not satisﬁed in the option markets.
As Fama stressed, this doesn’t mean that the markets are inefﬁcient, but
this, together with the anecdotal evidence of seeing consistently proﬁtable
option traders and trading companies, leads me to believe that volatility
markets are inefﬁcient enough to trade proﬁtably. Further, it seems likely
that they will remain so.
Wealsonoteherethatoptionshaveenoughwrinklesintheirspeciﬁcations
and behavior that it can be proﬁtable to trade them in ways in which they
--- page 68 ---

VOLATILITY FORECASTING
51
weren’t really designed. Indeed, volatility trading itself is an example of
such a strategy. This situation is common in gambling. Blackjack can be
beaten, if you count cards. Roulette can be beaten, if you time the ball.
Scratch card lotteries can be beaten, if you understand the algorithm that
designs the cards. Similarly, for example, options can be traded together
with credit products to create capital structure arbitrages, or equity options
can be traded against index options to take a position in implied correlation.
Before we start applying any mathematics, let’s look again at some of
the characteristics of what we are trying to forecast. How does volatility
behave? As we saw in Chapter 3:
■Volatility has more large moves up than down.
■Volatility seems to be—locally, at least—mean-reverting; it is pulled
toward its long-term mean.
These general features need to be kept in mind as we try to make volatility
forecasts.
The simplest forecasting method is to just assume that the next N days
will be like the last N. So if we have measured the volatility (using whatever
estimator) over the past 30 days to be 20 percent, we will use this as our
forecast for the next 30. This is sometimes known as the moving window
method. The obvious problem with this forecast is that a big move in the
stock’s price, say a jump due to good earnings, will stay in the volatility
estimateforNdaysthendropoutabruptly.ThiseffectisshowninFigure4.1.
0
0.2
0.4
0.6
0.8
1
1.2
Date
30-Day Volatility
6/20/2006
7/4/2006
7/18/2006
8/15/2006
8/1/2006
8/29/2006
9/12/2006
9/26/2006
10/10/2006
10/24/2006
11/7/2006
11/21/2006
12/5/2006
12/19/2006
1/2/2007
1/16/2007
1/30/2007
2/13/2007
2/27/2007
3/13/2007
3/27/2007
4/10/2007
4/24/2007
FIGURE 4.1
The 30-Day Moving Window Close-to-Close Volatility for True Religion
Apparel Inc. (TRLG) between June 20, 2006,and May 7, 2007
--- page 69 ---

VOLATILITY FORECASTING
52
Clearly the volatility forecast after the jump should not be 100 percent.
Thejump,ahugeevent,hasalreadyhappenedandisveryatypical.Obviously
it is biasing the forecast (note that it is not biasing the estimate of current
volatility. Volatility over the previous 30 days was indeed 100 percent).
A standard way to address this is to use the exponentially weighted moving
average model (EWMA). This takes the form
σ2
t = λσ2
t−1 + (1 −λ)r2
(4.1)
where λ is a parameter between zero and one. This models the variance as a
weighted average between the most recent squared returns and the previous
variance. (We have used the variance form here because it is normally stated
in this way, as are the later time series models we review). A lower value
of λ means less emphasis is placed on the more distant past and more on
the most recent observation. Generally values of between 0.9 and 0.99
are used.
This method has the virtues of being simple to use and understood. It has
the drawback of being a stupid solution. If the event truly was an outlier we
would be better off excluding it from our data set when we forecast what
volatility will be in the future. An exponential weighting may smooth the
jumps in our volatility forecast but it does so purely to make things look
pretty: A better solution is for the trader to decide if the event really was
an outlier and if it were to then exclude it or to treat it as a somewhat
special case that could occur again and weight its contribution accordingly.
To postulate that its effect decays exponentially really just dodges the issue.
For example, a jump due to earnings is clearly an abnormal event. It
would be good trading practice to exclude this from future forecasts (unless
they include future earnings dates). Why would it make sense to use an
exponential decay? The earnings announcement was a single event. There
won’t be a lesser earnings announcement the next day as well, and an even
smaller one the day after that.
A further problem with this method is that it doesn’t take into account
the context of the most recent measurement. Both casual examination and
careful statistical analysis show that volatility is a mean-reverting process;
high volatility is likely to be followed by periods of lower volatility and vice
versa. The EWMA forecast ignores this. The forecast variance tomorrow is
the same as the forecast variance for the day after and for all days after that.
The famous GARCH (Generalized Auto-Regressive Conditional Heteroskedasticity) family of models addresses this by adding a long-term
average variance that we expect variance to revert to, so that if variance
is currently high we may expect it to stay high in the near term (as in
--- page 70 ---

VOLATILITY FORECASTING
53
the EWMA model) but that it will eventually revert to normality. The
GARCH(1,1) model is
σ2
t = γV + αr2
t−1 + βσ2
t−1
(4.2)
where V is the long-term variance. Clearly we must have
γ + α + β = 1
(4.3)
And when γ = 0, α = 1 −λ and β = λ, we recover the EWMA model
as a special case. Generally this model is written in the form
σ2
t = ω + αr2
t−1 + βσ2
t−1
(4.4)
This is a more convenient form to use when estimating the parameters
but is used at the expense of a nice interpretation for the meaning of the
ﬁrst term. Now the long-term variance is given by
V =
ω
1 −α −β
(4.5)
Insteadofhavingdependenceononlytheﬁrstlaggedreturnsandvariances
it is possible to further generalize the model to include the past p returns
and the past q variances. This results in the GARCH(p,q) model.
σ2
t = ω + α1r2
t−1 + . . . + αpr2
t−p + β1σ2
t−1 + . . . βqσ2
t−q
(4.6)
To use GARCH to forecast volatility we approach the subject iteratively.
Clearly for some time step in the future
σ2
t+τ = ω + αr2
t+τ−1 + βσ2
t+τ−1
(4.7)
Or
σ2
t+τ = (1 −α −β)V + αr2
t+τ−1 + βσ2
t+τ−1
So
σ2
t+τ −V = α(r2
t+τ−1 −V) + β(σ2
t+τ−1 −V)
(4.8)
And if we use the fact that
E[r2
t ] = σ2
t
We get
E[σ2
t+τ −V] = (α + β)E[σ2
t+τ−1 −V]
And iterating, we get
E[σ2
t+τ −V] = (α + β)τE[σ2
t −V]
E[σ2
t+τ] = V + (α + β)τ(σ2
t −V)
(4.9)
--- page 71 ---

VOLATILITY FORECASTING
54
0.1
0.11
0.12
0.13
0.14
0.15
0.16
0.17
0
20
40
60
80
100
120
Time (Days)
Volatility
FIGURE 4.2
The Term Structure of Volatility Predicted by a GARCH(1,1) Model for
MSFT on May 21, 2007
Equation 4.9 can be used to generate a term structure for the volatility
forecast. Figure 4.2 shows such a term structure for volatility after ﬁtting a
GARCH(1,1) model to the daily return series for Microsoft (MSFT) using
data from May 21, 2003, to May 21, 2007. The estimated parameters for
the process were ω = 0.00000505, α = 0.,053 and β = 0.884.
GARCHmodelscanonlyproducetermstructuresthatexponentiallytend
toward the long-term mean. They cannot account for the humped volatility
term structures that are often observed in the market, where, for example,
the two-month volatility is above both the one-month and three-month
levels. This indicates that the option market does not ‘‘believe’’ in GARCH.
■Maximum Likelihood Estimation
Generally when traders or risk managers use EWMA, they arbitrarily
choose the smoothing parameter, λ. We could also do this for GARCH and
arbitrarily set values for the parameters. However, those who believe the
variance process is described by a GARCH model generally do not do this,
relying instead on maximum likelihood estimation to ﬁnd the parameters
for each underlying. (This is one of the often-stated objections to GARCH:
that it is subject to retrospective curve ﬁtting of the parameters. More
correctly, this is a possible problem with the common implementation of
the model rather than with the model itself.)
Maximum likelihood estimation (MLE) is a method for estimating the
parameters of a probability distribution. Likelihood differs from probability.
--- page 72 ---

VOLATILITY FORECASTING
55
Probabilityreferstothechancethatafutureeventoccurs,whereaslikelihood
refers to past events. In MLE the parameters are chosen to maximize the
probability of the ﬁnal observed outcome actually happening.
A commonly cited example is estimating the number of cabs in a city.
All we know is that all cabs are given a unique number and that numbers
are consecutively issued, with no numbers being skipped. If the ﬁrst cab
we see has number 2,028, what is our MLE estimate? Clearly there can
be no fewer than 2,028 cabs. Recall that MLE looks to ﬁnd the parameter
that makes the observation most likely. In this case if there were exactly
2,028 cabs in the city our chances of spotting that particular car would be
1/2028. If there were any more cars than this we would have had a smaller
chance of seeing exactly that one. So the MLE estimate is 2028. Note that
although this is our best estimate it could be a long way from the actual
number. There could well be 10,000 cabs. But MLE makes the best use of
the information available to us.
The next example is less trivial, although still somewhat contrived. Let’s
assume that we toss a coin 10 times. We don’t know if it is a fair coin or
not. In fact it could be one of three coins. One coin gives a head one-third
of the time, one gives a head one-half of the time and one gives a head
two-thirds of the time. If we get six heads in our experiment, what coin is
it most likely that we were using?
Let p be the (unknown) probability of throwing a head. So the probability
of getting a tail is 1 −p. The result of a coin toss is described by the binomial
distribution. The probability of getting h heads from N tosses is
Pr(h) =
n!
(n −h)!h!ph(1 −p)n−h
(4.10)
So
Pr(h = 6|p = 1/3) =
10!
(4)!5!
1
3
62
3
4
≈0.057
(4.11)
Pr(h = 6|p = 1/2) =
10!
(4)!5!
1
2
61
2
4
≈0.205
(4.12)
Pr(h = 6|p = 2/3) =
10!
(4)!5!
2
3
61
3
4
≈0.228
(4.13)
So in this case it is most likely that we have been tossing the coin that
comes up heads two-thirds of the time.
--- page 73 ---

VOLATILITY FORECASTING
56
This is an example of applying MLE to a discrete distribution. The case
of a continuous distribution involves similar reasoning.
The likelihood function for a GARCH (1,1) model is given by
t
i=1

1

2ψ2i
exp
−r2i
2σ2i

(4.14)
Although it is normal to use the equivalent log-likelihood version
t

i=1

−ln

σ2
i

−r2i
σ2i

(4.15)
After ﬁtting a GARCH(1,1) model to a few price series, the reader is
likely to discover a problem: the log-likelihood function is very ﬂat. We are
likely to have difﬁculties ﬁtting a model as there will be very small changes
in the likelihood for a wide range of parameters. This can be somewhat
addressed by using variance targeting, where the omega term is set equal to
the unconditional variance of the sample multiplied by 1 −α −β, and we
only vary the alpha and beta terms.
Still, it may be necessary to use more sophisticated numerical techniques
if we want to use GARCH models extensively. These could also provide
statistics giving the goodness of ﬁt of the model. There are a number of
reasons why the model may not ﬁt the data well. These include:
■Insufﬁcient data. Generally at least 1,000 data points are required. If
you have less data, you may just decide to choose parameters that ‘‘look
right.’’ This isn’t as terrible as it may ﬁrst appear. This is what we typically
do when using an EWMA, for example. It is also not so different to
arbitrarily choosing a window length to measure close to close volatility.
■Poor initial values for the parameters.
■Persistent seasonality contained in the data. This is a particular problem
with intraday data, which exhibit persistent seasonality in the volatility.
Daily data seems to be the natural timescale to use for GARCH modeling.
■The model is wrong: The data just aren’t consistent with the model
chosen! In particular, it might be that the fattails in the return distribution
are not due to GARCH effects, so that using a normal distribution in our
GARCH model doesn’t address the problem completely.
Econometricians have developed a large number of models to address
this last issue. Some of the more common models are listed below but this
is far from exhaustive. In fact, since the original work by Engle (1982), an
--- page 74 ---

VOLATILITY FORECASTING
57
enormous number of versions have been developed.1 One paper documents
a comparative test of 330 models (Hansen and Lunde 2005).
■EGARCH: Exponential GARCH. This models the log of the variance.
This means it can incorporate asymmetry, as negative shocks can have a
different effect to positive shocks (Nelson 1991).
■GJR-GARCH: This is another asymmetric model where an extra term
is present in the case of downward shocks (Glosten, Jagannathan, and
Runkle 1993).
■IGARCH: Integrated GARCH. This further constrains the parameters so
that alpha and beta sum to one.
■TGARCH: Threshold GARCH. This has an extra term that applies when
shocks are negative, again allowing asymmetry.
■AGARCH: Absolute Value GARCH. This directly models volatility
instead of variance (Taylor 1986; Schwert 1989).
■CGARCH: Component GARCH. This models the variance as the sum
of several processes or components. One could be used to capture the
short-term response to shock and another to capture the long-term
response. This allows the model to capture long memory effects (Engle
and Lee 1999; Ding and Granger 1996).
It certainly seems that GARCH does capture some elements of the
time evolution of variance. Further, it can be motivated by a fairly simple
microstructure based argument (Sato and Takayasu 2002). However, the
fact that so many models exist in the family, with no one being deﬁnitively
superior, can certainly be seen as a negative. Also, if we estimate the
parameters of the model using MLE, then reestimate the model at a later
date we ﬁnd little persistence in the values of the parameters. This would
also seem to indicate that the model was not a particularly good description
of reality. And note that this model is meant to be predictive not just
descriptive. Unlike BSM, which is just a conceptual framework, a volatility
forecast really does need to have good correspondence with the future.
In addition to the GARCH family, there are many other methods for
predicting time series. These include neural networks, genetic algorithms
and classical econometric methods such as the ARMA family of models. We
1Engle actually developed ARCH. The GARCH model was ﬁrst proposed by Bollerslev
(1986). ARCH is GARCH(0,1).
--- page 75 ---

VOLATILITY FORECASTING
58
don’t touch on these here for several reasons: I have seen no conclusive
evidence that they are any good at predicting; genetic algorithms and neural
nets are very specialized methods that are easy to misuse, and while time
series analysis is probably a good thing to know (refer to Taylor 1986), it is
doubtful that spending a great deal of time trying to reﬁne a point forecast
is worth it.
Even if we agree with the Nobel Prize committee that the GARCH
‘‘frame-work is an indispensable tool for risk assessment in the ﬁnancial
sector,’’2 it isn’t actually the breakthrough that an option trader needs.
A point forecast of volatility just isn’t all that useful. We need a forecast of
the volatility distribution. Selling one-month implied volatility at 15 percent
might seem like a good idea if we have a forecast of 12 percent. It will seem
like less of a good idea if we know that one-month realized volatility has had
a range of 11 to 35 percent. It isn’t just the forecast that is necessary. It is
putting the forecast into the context of a volatility range. A simple way to
do this is through the use of volatility cones.
As stated in the seminal paper on the subject (Burghart and Lane 1990),
‘‘The purpose of a volatility cone is to illustrate the ranges of volatility
experience for different trading horizons.’’ Let’s look at the example of
MSFT volatility for the four years ending April 30, 2007. We calculate
volatility (here we use the close-to-close estimator but there is no reason
that another estimator could not be used) over (nonoverlapping) periods
of 20 trading days, 40 trading days, 60 trading days, 120 trading days, and
240 trading days. These correspond closely to one calendar month, two
months, three months, six months, and one year. The results are displayed
in Figure 4.3.
When displayed graphically, we can see why this method was called a
volatility cone. The cone shows the tendency for short-term volatilities to
ﬂuctuate more widely than longer dated volatilities. One the one hand,
this is obvious: as big moves will be averaged away in the longer term.
On the other hand, we also know that volatility measurements are prone
to sampling error and this more dramatically affects shorter measurement
periods (refer back to Table 2.3, where we saw how sampling error is
dependent on sample size). Further, to gain the most information from a
given price series it would generally be necessary to use overlapping data.
This clearly will induce an artiﬁcial degree of correlation in the estimates
of volatility and will bias our results somewhat. We need to take all of this
2From the press release accompanying the announcement of the 2003 prize for economics.
--- page 76 ---

VOLATILITY FORECASTING
59
0
0.05
0.1
0.15
0.2
0.25
0.3
0.35
0.4
0.45
0.5
20
40
60
120
240
Time (Days)
Volatility
FIGURE 4.3
The Volatility Cone for MSFT, Generated from the Four Years of
Closing Prices Ending on April 30, 2007
into account. Speciﬁcally, we need to know how much bias is introduced
into our volatility estimates by using overlapping data. This problem was
studied extensively by Hodges and Tompkins (2002). They found that
variance measured from overlapping return series need to be multiplied by
the adjustment factor,
m =
1
1 −h
n + h2 −1
3n2
(4.16)
where h is the length of each subseries (for example, 20 days) and n = T
−h + 1 is the number of distinct subseries available for a total number of
observations, T. So for the example given above in Table 4.1, we would
have the case where we need to adjust the variance measured over 60-day
subperiods from 1,006 data points the adjustment factor would be 1.06, or
approximately 1.03 when applied to the volatility. Using this adjustment
factor means that we can use rolling windows for estimating volatility.
which makes volatility cones a useful trading tool.
TABLE 4.1
The Volatility Cone Numbers for MSFT, Generated from the Four
Years of Prices up to April 30, 2007
20-Day Volatility
40-Day Volatility
60-Day Volatility
120-Day Volatility
Maximum
0.465
0.352
0.287
0.258
75%
0.213
0.213
0.225
0.200
Median
0.159
0.172
0.169
0.181
25%
0.123
0.149
0.147
0.161
Minimum
0.062
0.096
0.091
0.136
--- page 77 ---

VOLATILITY FORECASTING
60
Given that for stocks, and many futures, the impact of news is far
more important than any other factor in projecting and forecasting realized
volatility, we may generally be best served by comparing implied volatility
to the historical volatility distribution given by the volatility cone. Selling
one-month implied volatility at 35 percent because this is in the 90th
percentile for one-month volatility over the past two years can form the
basis of a sensible trading plan. Selling 35 percent because GARCH is
forecasting the realized volatility to be 20 percent is less sensible. The point
forecast isn’t as important as the possible distribution of results.
Obviously, it is also possible to construct volatility cones from the other
volatility estimators.
The volatility cone is useful for placing current market information
(realized volatility, implied volatility, and the spread between them) into
historical context. But it doesn’t place it in the context of the current overall
market. This is also something to monitor. If we had a choice of selling
Citigroup’s implied volatility at 39 percent when its realized is 26 percent
or selling the S&P 500 implied volatility at 24 percent when its realized
was 18 percent, we should think carefully. We are not getting much more
edge as a percentage for selling the single stock than we are for the index.
Consider using the implied/realized spread of the index as a benchmark for
the amount of edge you look for in all of your trades. Things change and
this context is always very important.
Volatility cones are often not helpful to marketmakers or other very
active traders. In fact, they can be very irritating. This is because whenever
the volatility cone tells you that implied volatility is historically high, you
will already be short it. Generally you will have been selling it all the way
up, and will now be sitting on a losing position. But at least you will now
know that implied volatility is at an all-time high, and now might not be
the best time to cover. And marketmakers will lose money in these types of
situations anyway. Ignorance can’t help.
■Volatility Forecasting Using Fundamental
Information
We have seen that volatility has a number of regularities that make it
amenable to forecasting with time series methods. But we shouldn’t forget
that we generally know more about the underlying than just the returns. For
example, a stock is literally a share of a business. This business has earnings,
--- page 78 ---

VOLATILITY FORECASTING
61
book value, debt, sales, revenue, and many other pieces of fundamental
information associated with it. These can also be used to help forecast
volatility. In isolation, these forecasts are not necessarily better than those
based on time series, but they do use different information than that typically
looked at by the market (and remember that even the more sophisticated
time series models are highly correlated with the simple close-to-close
model).
Here we look at the method applied to equity volatility forecasting, but
a similar analysis could be applied to commodities (which are probably the
asset class most driven by fundamentals) after choosing an appropriate set
of independent variables.
As fundamental information arrives far less frequently than price, this
method is better suited to longer dated forecasts. It also seems likely that,
similar to the way value investors in stocks often have to wait a long time
to realize their edge, that this method could suffer through long periods
of poor performance. The method is also better suited to forecasting the
relative volatility of stocks rather than arriving at an absolute forecast.
Sridharan (2012) shows that the market underestimates volatility for
ﬁrms with:
■High research and development costs.
■High cash ﬂow volatility.
■Earnings management.
The market overestimates volatility for ﬁrms with:
■Large size.
■High return on assets.
■High leverage.
This list shouldn’t be totally surprising. As some accounting variables are
associated with risk because they are indicative of greater future uncertainty,
they should also be useful in the prediction of future realized volatility. The
one result that might be a little surprising is that high leverage leads to the
market overestimating future volatilities. Given that there is a relationship
between leverage and default, it seems that naively, we would want to be
long volatility on highly levered ﬁrms. In fact though, for a ﬁrm to become
highly leveraged it needs good access to the debt markets, and the bond
market has a better understanding of this risk than the volatility market does.
--- page 79 ---

VOLATILITY FORECASTING
62
■The Variance Premium
When making forecasts, we generally ﬁnd that the implied volatility is equal
to or signiﬁcantly above our forecast volatility. The BSM implied volatility
is in general an upwardly biased estimate. For example, it is not uncommon
for our forecasts to be 30 percent below current implied volatilities, but we
practically never see the converse. There are a number of obvious reasons
for this.
■By selling implied volatility, we are selling insurance. Thus, there is a risk
premium associated with this.
■Perfectly reasonable things could happen that have never happened. These
are not taken into account if we only base our forecast on past data.
■Market microstructure encourages implied volatility to be biased high.
Market makers make the bulk of their money by collecting the bid ask
spread in the options. They will willingly bias their quotes a little too high
to protect their business. In essence, they are buying insurance (slight
long volatility exposure particularly on the downside), as any prudent
business owner will do.
Bakshi and Madan (2006) developed a model that helps us predict when
the spread would be particularly high or low. In their theory, the difference
between risk-neutral and physical volatility is connected to the higher-order
return moments. They predict positive volatility spreads when traders are
risk averse, and when the physical distribution is negatively skewed and
fat-tailed.
In this case, the authors assume a power utility of form
U(W) ∝exp(−γW)
(4.17)
Thisleadstothefollowingapproximaterelationshipbetweenthevolatility
spread(actuallydeﬁnedintermsofvariance)andthemomentsofthephysical
distribution.
σ2rn −σ2
σ2
≈−γσ × skew + γ2
2 σ2 × (kurtosis −3)
(4.18)
Using this, a trader can, for a given level of risk aversion, decide which
particular spreads are more overor underpriced on a relative basis.
Let’s look at an example. On August 3, 2012, I estimated the physical
moments of SPY and EEM. These are shown in Table 4.2.
On that day, the September at-the-money (ATM) implied volatility was
0.156 for the SPY and 0.225 for EEM. According to Equation 4.18, the
--- page 80 ---

VOLATILITY FORECASTING
63
TABLE 4.2
Estimates of Return Moments of
SPY and EEM on August 3, 2012
Moment
SPY
EEM
Volatility
0.136
0.186
Skewness
−0.1
−0.05
Kurtosis
3.6
3.5
volatility spread for SPY implies a risk aversion of about 6.4. If we accept
this as the market’s estimate of risk aversion and assume it is constant for
all indices, the implied volatility of EEM should be 0.221. So in this case, it
looks like the relative degree of mispricing is very similar.
WeseeinChapter5thatestimatesofskewnessandkurtosisarereasonably
noisy. Our estimates are probably not good enough to really make subtle
distinctions such as using this model to decide which index volatility is
richer. However, we can use the theory to get an idea of what the option
market is implying about future large moves that are not present in the
historical return series.
It seems sensible that spreads will be larger in situations where option
sellers are more risk averse: They will demand more of a premium to
compensate for their fear. It also seems sensible that spreads will widen
with the higher moments: All options are exposed to all moments of the
physical distribution.
However, the model doesn’t seem to ﬁt with the fact that, at least for
the S&P 500, spreads (in percentage terms) actually narrow as the Volatility
Index (VIX) increases. Table 4.3 shows the percentage volatility spreads for
various VIX levels from January 1990 to May 2012.
High VIX levels intuitively seem to be a measure of risk aversion, but
apparently not the particular one that this model considers. Obviously, real
markets are complicated and at any time there will be many effects in play
and they may be working against each other. In this case it may be that at
high levels of volatility, traders expect mean reversion to be a dominant
effect and this drives spreads lower. This effect is not included in Bakshi and
Madan’s model (2006).
TABLE 4.3
The Volatility Premium as a Function of the VIX Level
VIX < 20
20 < VIX < 30
30 < VIX < 40
40 < VIX < 50
50 < VIX
Days
3,102
1,925
407
111
56
Average spread
27.75%
19.78%
13.73%
9.26%
−11.52%
--- page 81 ---

VOLATILITY FORECASTING
64
It could also be that volatility level is correlated with the higher order
moments of the distribution and that this overwhelms the risk aversion
issue. I think that the model is interesting but probably incomplete, while
the historical data (Table 4.3) are incontrovertible.
The incorrect conclusion to draw from the existence of the volatility
premium is that we can always proﬁt by selling implied volatility. We return
to this idea in Chapter 11 when we look at some cases where it is proﬁtable
to sell implied volatility.
Remember that insurance companies proﬁt largely from the proﬁts made
by reinvesting the insurance premium. This opportunity isn’t available to
option traders using borrowed funds. The option insurance premium alone
isn’t a good enough reason to sell options. But we need to acknowledge
its existence and de-bias our forecasts accordingly so that we can tell if an
option really is too expensive. So we adjust each forecast by subtracting
the ‘‘usual’’ implied/forecast spread. For example, the realized/implied
spread for the S&P 500 can be loosely proxied by the spread between the
rolling 30-day close-to-close volatility and the VIX index. This is shown in
Figure 4.4. The VIX is almost always above the 30-day rolling volatility.
You need to know the average amount of this premium. Remember that you
should be looking for things that are out of the ordinary. The actual spread is
shown in Figure 4.5. Here the average value is 3.09. This is the crucial value
to remember. (Note also that the period in April 2007 where the spread
went negative corresponds to a spike in the 30-day close-to-close volatility.
This was largely caused by the problem with historical volatilities being
backward looking, which we discussed earlier and showed in Figure 4.1.)
0
5
10
15
20
25
30
35
2/15/2006
3/27/2006
5/4/2006
6/13/2006
7/21/2006
8/29/2006
10/6/2006
11/14/2006
12/22/2006
2/5/2007
3/15/2007
4/24/2007
6/1/2007
7/11/2007
8/17/2007
9/26/2007
11/2/2007
12/12/2007
Volatility
Date
volatility
VIX
FIGURE 4.4
The VIX and the S&P 500 30-Day Volatility. (Note that the VIX is almost
always over the 30-Day Volatility)
--- page 82 ---

VOLATILITY FORECASTING
65
–6
–4
–2
0
2
4
6
8
10
12
3/24/2006
10/10/2006
4/28/2007
11/14/2007
Date
Implied Premium
FIGURE 4.5
The Implied Volatility Premium for the S&P 500
For a position trader, context-adjusted volatility cones can be useful
as they get to monitor volatility without having to continuously make
markets. They can wait to establish a position as it reaches the highs (and
the marketmakers will generally be eager to lighten up their positions at
this point). Position traders have to take advantage of the fact that they can
be selective. Trading may look like a competitive activity but it shouldn’t
be about posturing. There is no need to always have a position. Lions are
smart and powerful hunters, but they don’t waste energy ﬁghting rhinos.
They wait until the wounded antelope gets separated from the herd.
■Summary
Trading is hard. Many people are looking to hear that this isn’t the case.
Something that is sometimes said in encouragement is, ‘‘You don’t need
to predict.’’ This is completely wrong. All trading involves prediction.
Sometimes this is implicit. For example, when we buy something we are
implicitly prediction that its price will increase.
Given that we will be making predictions and given that volatility is far
more predictable than price, why not explicitly forecast volatility? Then we
will have an idea of our edge and our conﬁdence in the amount of edge.
■Place forecasts in context by using a volatility cone.
■Further consider the state of the entire market to determine if the
particular implied volatility under examination is at an extreme level
or whether this is just an appropriate level given the state of the broad
market.
■Be selective. Wait for an edge that is clear, measurable, and
understandable.
