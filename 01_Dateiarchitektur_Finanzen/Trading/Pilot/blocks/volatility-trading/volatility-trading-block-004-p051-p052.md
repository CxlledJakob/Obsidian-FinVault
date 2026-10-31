# Volatility Trading_ Sinclair_Volatility Trading -- Euan Sinclair(auth_) -- Wiley Trading, 1, 2013 -- John Wiley & Sons, Incorporated -- isbn13 9781118347133 -- 2634a86bfed8248fa7ba3fb72595bbbc -- Anna’s Archive.pdf — Chapter 2: Volatility Measurement (pages 51–52)

--- page 51 ---

VOLATILITY MEASUREMENT
32
0
0.05
0.1
0.15
0.2
0.25
0.3
8
9
10
11
12
13
14
15
16
Central Standard Time
C Volatility
FIGURE 2.8
C Intraday Volatility
0
0.05
0.1
0.15
0.2
0.25
8
9
10
11
12
13
14
15
16
Central Standard Time
DNA Volatility
FIGURE 2.9
DNA Intraday Volatility
fast intraday seasonality will average out and for time periods shorter than
this, the effects of path dependency will massively overwhelm inaccuracies
in volatility prediction.
Using high-frequency data seems like an obvious thing to do. Using higher
frequency data allows us to use more data from a recent time period. This
should give convergence to the true, unobservable volatility while avoiding
the issue of using data from past periods that are now irrelevant. However,
there are some issues to consider.
First, traders who insist of sampling at very high frequencies will have
to deal seriously with the issues of microstructure. For example, bid/ask
bounce is an important feature that impacts prices but should not really be
--- page 52 ---

VOLATILITY MEASUREMENT
33
expected to contribute to long-term volatility. These microstructure effects
are well beyond the scope of this book. Those interested could start with
Gencay et al. (2001) or Lequex (1999).
Second, the frequency of sampling should depend on why volatility
is being estimated. For example, using high-frequency returns might be
sensible if we are trying to estimate market impact (see the model of
Gatheral in Chapter 6), but there is plenty of evidence (Corsi 2009; Lynch
and Zumbach 2003) to suggest that low-frequency volatility is a better
predictor of high-frequency volatility than vice versa. So as a long-term
forecasting tool, using high-frequency data is possibly the wrong approach.
■Summary
Unlike price, volatility cannot be instantaneously measured. It is an average
and needs to be estimated over time. In real markets, the deﬁnition of
volatility might not lead to the best way to actually estimate it. There
are many ways to measure volatility and even after making the choice of
statistical estimator weneed to choose further parameters. It is important
to know about these methods but in the end, volatility measurement is
something of an art.
■Estimate volatility using a variety of methods, keeping in mind the
strengths and weaknesses of each.
■Try to choose a sample length that achieves a balance between including
data from periods that is no longer relevant and using too little data so
that sampling error dominates.
