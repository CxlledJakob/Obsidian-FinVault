# Volatility Trading_ Sinclair_Volatility Trading -- Euan Sinclair(auth_) -- Wiley Trading, 1, 2013 -- John Wiley & Sons, Incorporated -- isbn13 9781118347133 -- 2634a86bfed8248fa7ba3fb72595bbbc -- Anna’s Archive.pdf — Chapter 9: Trade Evaluation — GENERATING RETURNS THROUGH VOLATILITY (pages 229–229)

--- page 229 ---

GENERATING RETURNS THROUGH VOLATILITY
217
0
100,000
200,000
300,000
400,000
500,000
600,000
Date
PL
1/5/2000
6/21/2000
12/6/2000
5/23/2001
11/7/2001
4/24/2002
10/9/2002
3/26/2003
9/10/2003
2/25/2004
8/11/2004
1/26/2005
7/13/2005
12/28/2005
6/14/2006
11/29/2006
5/16/2007
10/31/2007
4/16/2008
10/1/2008
3/18/2009
9/2/2009
2/17/2010
FIGURE 11.6
The Proﬁts from Selling the 20 Delta Strangle in the Second Expiration
QQQ Options When VIX Is Below 35
Average weekly return (annualized): 17.8 percent
Total return (annualized): 41.7 percent
Sharpe ratio: 1.30
Largest percentage drawdown: 31.4 percent
However, simple modiﬁcations allow us to capture a decent return while
reducing volatility.
For example, we can somewhat smooth the results by taking advantage
of the fact (mentioned in Chapter 4) that the volatility premium is
proportionally greater when the implied volatility is low. Figure 11.6 shows
the results of selling the 20-delta strangle only when the VIX is below 35.
Again the result is fairly robust with respect to the actual VIX level chosen
and indeed to which instrument is used as the measure of implied volatility.
The raw statistics don’t look to be greatly improved, but the proﬁt-loss
(PL) stream is far smoother and we avoid the terrible volatility of 2008.
Another enhancement is to take advantage of the fact that selling
options will do better in stable or declining VIX environments. If we
only sell options when the VIX is below its moving average (here we use
exponentially weighted moving average model [EWMA] with a decay factor
of 0.95) we do much better. The results are shown in Figure 11.7.
Although this graph looks appealing, we have to remember that this is
now a considerably less robust result than simply using the level of the VIX
as a ﬁlter. Although it is comparatively simple to avoid the turmoil of 2008
with almost any choice of moving average, dealing with periods when the
VIX oscillates in a range (such as from 2000 to 2003) is not straightforward.
The potential for curve ﬁtting is signiﬁcant. It is interesting to note that the
moving average (MA) ﬁlter outperforms the level ﬁlter mainly due to the
results pre-2004. After this, both strategies see their equity levels double.
