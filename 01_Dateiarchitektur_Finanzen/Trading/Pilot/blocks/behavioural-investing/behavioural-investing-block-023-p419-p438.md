# Behavioural Investing_ A Practitioners Guide to Applying -- James Montier -- Wiley finance series, Chichester, West Sussex, England, 2007 -- Wiley ; -- isbn13 9780470490297 -- 552a06a98fb1ad4320dc7c3128ea169b -- Ann.pdf — pages 419–438

--- page 419 ---

33
Sector-Relative Factors Work Best*
Written with Andrew Lapthorne
Value, size and momentum are well-documented providers of excess returns but
can lead to some uncomfortably large sector bets. Using industry-relative factors
reduces this problem, as well as getting around many problems associated with
accounting regimes and capital structures. Our back-testing suggests that value
and size work best on a sector-adjusted basis, while price momentum does not.
Ĺ Should we screen stocks on absolute levels of valuation, momentum and size or should
we look at everything relative to a set of sector peers? Despite most research teams being
organized along sector-lines, much quant work seems less enthusiastic about making stockto-peer comparisons, preferring to select stocks using absolute valuation and to adjust sector
bets afterwards, typically through some kind of optimization process.
Ĺ Perhaps the reason why sector-relative measures are not overly popular is that most backtests, looking back over the last 10 or so years, would highlight how absolute levels of
valuation (in particular), momentum and size would have worked better unadjusted to differing industry characteristics. We argue in this chapter that this period of factor performance,
typiﬁed by big swings in sector rotation (courtesy of the TMT bubble) is not particularly
representative and, as such, a sector-relative approach to factor selection is more appropriate
going forward.
Ĺ Certainly the fundamental arguments for a sector-relative approach are compelling. Industries have different capital requirements and accounting regimes and, as such, a low price to
book, for example, rather than representing a “value” opportunity, may simply be deﬁning
a type of business.
Ĺ Constructing portfolios based on absolute rather than sector-relative measures, reduces sector
diversiﬁcation (i.e. can result in some fairly large sector bets). While sector constraints can
be imposed later, this would have the effect of diminishing the exposure to any given factor
and possibly future returns. A sector-relative approach might allow for a more diversiﬁed
portfolio from the offset and without diminishing the exposure to any given factor.
Ĺ We have back-tested four valuation metrics (PE, PC, PB and DY), size and a common
(6-month) price momentum strategy. Our results conﬁrm our prior comment, that over the
last 10 years, a non-adjusted approach generally worked best, although not always.
Ĺ However, over a more extended 30-year period and in the 10 years prior to the bubble commencing, a sector-relative approach has generally outperformed a market-wide approach.
Absolute and risk-adjusted returns were found to be higher for most valuation metrics and
*This article appeared in Global Quantitative Strategy on 23 November 2006. The material discussed was accurate at the time
of publication.
--- page 420 ---

396
Behavioural Investing
in most regions with the exception of Japan (as ever!). Statistical signiﬁcance of these
returns also improved in most cases. Even small versus large size was found to have better
returns on a sector-adjusted basis. The results for price momentum was more mixed with the
industry-relative measure delivering results with greater statistical signiﬁcance, but lower
absolute returns. Given that price itself is not a function of industry make-up or accounting
regime, this result is probably not too surprising.
--- page 421 ---

Sector-Relative Factors Work Best
397
60
70
80
90
100
110
120
130
140
150
160
Jan-90
Jul-90
Jan-91
Jul-91
Jan-92
Jul-92
Jan-93
Jul-93
Jan-94
Jul-94
Jan-95
Jul-95
Jan-96
Jul-96
Jan-97
Jul-97
Jan-98
Jul-98
Jan-99
Jul-99
Jan-00
60
70
80
90
100
110
120
130
140
150
160
Sector relative
Market-wide
Figure 33.1
Sector-relative versus rather than absolute price to book strategies in the US during the
1990s (using long/short quintiles).
Source: DrKW Macro research.
There is a wide body of research recognizing that selecting stocks based on price momentum
and/or a low valuation has generated excess returns over the long term. Most of this research
concentrates on using absolute levels of such things as price to earnings, cashﬂow and so on.
This research note asks if there is any beneﬁt to looking at such measures on an industry-relative
rather than a market-wide basis.
For a start, constructing portfolios based on absolute levels of valuation is likely to lead to
large sectors bets, which, while perhaps proﬁtable in the long-term, can result in sustained
periods of underperformance. (Witness the suffering and asset losses incurred by value
managers during the TMT bubble.) Building a portfolio based on sector-relative rather than
market-wide measures should lead to a more diversiﬁed portfolio and, as such, perhaps offer
better risk-adjusted returns. Figure 33.1 shows that during the 1990s the style rotation was not
so much towards growth stocks but towards growth sectors.
In a research note published in June 1996,1 we highlighted how style-returns were not
simply a function of sector rotation. We found that the returns produced from constructing
factor portfolios within sectors were equivalent to, and highly correlated with, market-wide
factor portfolios. So we concluded that the excess returns from taking a value and/or momentum
approach were still available even when constraining sector exposure.
Unfortunately building individual portfolios within sectors was not optimal. Many sectors
did not have a sufﬁcient number of liquid stocks and we were forced to create long/short
baskets using tritiles rather than deciles or quintiles. As a consequence the resulting factor
spread between the long and short portfolios was reduced, and subsequently the alpha generated
was not as attractive as when executed market-wide.
Another way of minimizing sector risk is to use sector-adjusted factors rather than simply using market-wide variables. Research by Asness et al. (2000), for example, has highlighted how
1 See Global Quantitative Strategy, Intra-sector style returns – its more than sector rotation (5 June 2006).
--- page 422 ---

398
Behavioural Investing
industry-relative factors appear to offer better returns than using a simple market-wide variable. Beyond reducing sector-risk within a portfolio, there are several compelling arguments
for using industry-relative measures. Cohen and Polk (1998) argue along with Asness et al.
that valuation measures such as price to book are highly dependent on accounting standards,
and that capital requirements will vary greatly across industries. A low price to book, rather
than representing a “value” opportunity, may simply be deﬁning a type of business.
METHODOLOGY
Every month for each region we use a proprietary universe of stocks corrected (which includes
dead stocks) to create long/short quintile portfolios based on two sets of factors. The ﬁrst set
of factors we test are simply the straightforward unadjusted values. So, for example, in testing
P/E we simply rank the universe according to their P/E and go long the 20% of stocks with the
cheapest P/E and short the 20% of stocks with the highest P/E.2 The second set of variables
we measure are all relative to the median value of the sector in which the stock resides. If a
stock has a dividend yield of 4% and the median dividend yield of stocks in its sector is 3%,
then the value we test is 1%, i.e. 4% −3%. The valuation data is based on ‘as reported’ MSCI
data. For each set of factors, we measure the average unweighted performance of each of these
portfolios over the month, rebalancing every month for the last 30 years.
As ever, when performing sector work we encounter the problem that the GICS classiﬁ-
cation system we use did not exist for a considerable proportion of our back-testing period.
Nonetheless as most of the sectors seen today represent similar descriptions of what existed
previously, we are not overly concerned. Also we are reassured that our results are similar to
those seen in other research where an entirely different classiﬁcation system has been used.
Therefore, each month we have calculated the performance of long and short portfolios
based on both an absolute and a sector relative factor. However, because we are only selecting
stocks at the more extreme end of any given variable, if a sector’s factors are all tightly
clustered around a particular level, then the sector would probably see no representation in
either the long or the short portfolio. So, although the sector-relative measure reduces sector
skew, it does not fully diversify industry exposure. However, this method, compared to trying
to represent all sectors, does allow a wider factor exposure and therefore hopefully better
returns.
Figure 33.2 compares the difference in global sector weightings of the long and short price
to book portfolios put together, based on either an absolute or a sector-relative price to book
measure. For example, when building portfolios using an unadjusted price to book, there is
almost a 7% difference between the weighting of the material sector in the long portfolio and
the short portfolio (i.e. a 12% weighting in the long portfolio versus a 5% weighting in the
short). When using a sector-relative price to book measure this difference is reduced down to
almost nothing.
THE RESULTS
Despite the apparent attraction of such an intra-sector methodology and research suggesting
that it improves returns, many seem unconvinced by such an approach. Back-testing results
over the last 10 or so years suggest the reasons why. Just as being underweight the TMT sectors
2 In practice we use earnings yield so as to include stocks with negative proﬁts.
--- page 423 ---

Sector-Relative Factors Work Best
399
−7.0
−6.0
−5.0
−4.0
−3.0
−2.0
−1.0
0.0
1.0
2.0
3.0
4.0
5.0
6.0
7.0
Pharmaceuticals
Software
Health Care
Retailing
Energy
Consumer Services
Commercial Services
Media
Household Goods
Telecoms
Food Retail
Diversified Financials
Consumer Staples
Semiconductors
Utilities
Transportation
Durables & Apparel
Capital Goods
Insurance
Technology
Automobiles
Banks
Real Estate
Materials
Sector relative price to book
Absolute price to book
Overweight
Underweight
Figure 33.2
Relative sector weightings in an absolute and sector relative long/short price to book
strategy (global universe, % difference).
Source: DrKW Macro research.
hurt investors during the inﬂating of the equity bubble, did it help them after the subsequent
bust? Much of the value outperformance subsequent to the bust was down to being in cheap
(i.e. non-TMT) sectors.
However, in the periods prior to the bubble-bursting, sector-relative valuation delivered the
better returns. An exception to this was Japan where the non-adjusted valuation measures
worked best. Looking forward, our argument would be that, with little in the way, extreme
sector-valuations out there, i.e. cross-sectional sector valuation spreads, are very low rather
than very high as they were in the latter part of the 1990s. So, as such, sector-relative measures
may win out once again.
Figures 33.3–33.6 show the annual difference in returns between employing either sectorrelative or absolute value strategies in four regions. They highlight how, for a long period of
time prior to the bubble-bursting, making a sector adjustment improved returns to a long/short
value strategy.
We realize that Table 33.1 doesn’t look particularly friendly and needs some explanation.
The ﬁgures quoted outside the brackets are the annualized returns for a zero net investment
strategy based on our long/short baskets. The numbers inside the brackets are the t-stats, which
is simply a measure of statistical signiﬁcance. We are only really interested in those annualized
returns with t-stats above 2.0. For each period, we have highlighted the better return (with a
minimum t-stat of 2.0) in italic for each factor in each region.
On initial inspection, the results appear quite mixed. Most of the value strategies appear to
beneﬁt from a sector-relative approach, which makes sense given different accounting regimes,
capital structures, and so on. The results for dividend yield are a bit more mixed. This perhaps
highlights how the level of dividend yield is not so much a function of company’s industry
and more a decision by management on payout levels earnings to retain. It could also suggest
that dividend yield is more related to sector rotation than the other value strategies we’ve
looked at.
Perhaps somewhat surprisingly Smallcap versus Largecap also worked well on a sector
relative basis and even though this must be viewed within the context of a universe that most
--- page 424 ---

400
Behavioural Investing
−35
−30
−25
−20
−15
−10
−5
0
5
10
15
20
25
30
1977
1978
1979
1980
1981
1982
1983
1984
1985
1986
1987
1988
1989
1990
1991
1992
1993
1994
1995
1996
1997
1998
1999
2000
2001
2002
2003
2004
2005
2006
Price to cashflow
Price to earnings
Price to book
Figure 33.3
Europe ex-UK – sector-relative versus market-wide factor returns (annual returns, %
difference between both approaches).
Source: DrKW Macro research.
academics would consider to be Largecap, it does suggest that the size effect is not about
buying “small industries” but by buying smaller companies within Industries.
Price momentum, as we have noted in prior studies while still working on an industryrelative basis (the results were marginally more statistically signiﬁcant), is not as effective as
when employed on a market-wide basis.
−25
−20
−15
−10
−5
0
5
10
15
20
25
1977
1978
1979
1980
1981
1982
1983
1984
1985
1986
1987
1988
1989
1990
1991
1992
1993
1994
1995
1996
1997
1998
1999
2000
2001
2002
2003
2004
2005
2006
Price to cashflow
Price to earnings
Price to book
Figure 33.4
USA – sector-relative versus market-wide factor returns (annual returns, % difference
between both approaches).
Source: DrKW Macro research.
--- page 425 ---

Sector-Relative Factors Work Best
401
−60
−55
−50
−45
−40
−35
−30
−25
−20
−15
−10
−5
0
5
10
15
20
25
30
1977
1978
1979
1980
1981
1982
1983
1984
1985
1986
1987
1988
1989
1990
1991
1992
1993
1994
1995
1996
1997
1998
1999
2000
2001
2002
2003
2004
2005
2006
Price to cashflow
Price to earnings
Price to book
Figure 33.5
UK – sector-relative versus market-wide factor returns (annual returns, % difference
between both approaches).
Source: DrKW Macro research.
The t-statistics in Table 33.1, a measure of signiﬁcance, are generally higher for the sectorrelative approach. This would suggest, and conﬁrmed in Table 33.2, that risk-adjusted returns
should be better for the industry adjusted measures. We have highlighted in italic the better
measure of each factor for each region. We would point out that some risk-adjusted returns
are fairly meagre and should simply be ignored. Again for price to cashﬂow, price to earnings,
and price to book there have been clear beneﬁts to using the sector-relative measures over
−25
−20
−15
−10
−5
0
5
10
15
20
25
1977
1978
1979
1980
1981
1982
1983
1984
1985
1986
1987
1988
1989
1990
1991
1992
1993
1994
1995
1996
1997
1998
1999
2000
2001
2002
2003
2004
2005
2006
Price to cashflow
Price to earnings
Price to book
Figure 33.6
Japan – sector-relative versus market-wide factor returns (annual returns, % difference
between both approaches).
Source: DrKW Macro research.
--- page 426 ---

402
Behavioural Investing
Table 33.1
Regional market-wide versus sector relative factor returns (annualized returns with t-stat*
in brackets)
Last 30 years
Last 10 years
Prior 10 years
Sector-
Market-
Sector-
Market-
Sector-
Marketrelative
wide
relative
wide
relative
wide
Price to Cashﬂow
Europe ex-UK
6.3 (3.5)
5.6 (2.6)
8.6 (2.8)
10.6 (2.3)
6.4 (2.4)
5.7 (2.1)
US
7.9 (4.6)
6.8 (2.3)
10.2 (2.6)
8.7 (1.2)
1.8 (0.9)
0.5 (0.2)
UK
7.9 (4.1)
6.6 (2.4)
9.5 (2.4)
13.9 (2.0)
6.1 (2.1)
3.9 (1.2)
Japan
8.0 (4.8)
7.8 (3.6)
8.7 (3.4)
10.4 (2.8)
8.6 (3.1)
9.2 (2.6)
World
10.5 (5.9)
9.7 (4.7)
14.1 (5.5)
13.8 (3.3)
6.8 (1.9)
5.7 (1.5)
Price to Earnings
Europe ex-UK
9.0 (5.3)
7.5 (3.4)
6.6 (2.1)
9.5 (2.2)
9.9 (3.9)
8.1 (3.1)
US
6.4 (4.0)
5.5 (2.0)
5.3 (1.3)
6.0 (0.9)
0.9 (0.5)
−0.6 (−0.2)
UK
8.1 (4.5)
9.7 (3.6)
11.4 (3.0)
18.2 (2.7)
4.4 (1.6)
4.3 (1.3)
Japan
5.9 (3.8)
7.2 (3.6)
4.1 (1.2)
6.0 (1.5)
8.0 (3.3)
9.7 (2.9)
World
9.7 (4.3)
9.4 (3.9)
9.3 (2.9)
10.5 (2.6)
7.7 (1.6)
7.3 (1.5)
Price to Book
Europe ex-UK
6.5 (3.4)
5.7 (2.6)
7.0 (2.0)
11.4 (2.8)
7.0 (2.2)
4.1 (1.2)
US
5.0 (2.9)
5.9 (2.4)
4.6 (1.2)
7.2 (1.3)
2.9 (1.3)
2.1 (0.7)
UK
7.3 (3.8)
5.0 (2.0)
7.3 (2.2)
8.2 (1.6)
7.1 (2.4)
4.9 (1.4)
Japan
10.5 (5.2)
11.5 (4.0)
10.7 (2.2)
12.3 (1.9)
14.4 (6.4)
16.6 (4.0)
World
8.8 (4.1)
8.5 (3.7)
9.4 (2.2)
9.9 (2.0)
7.7 (2.1)
7.7 (2.1)
Dividend Yield
Europe ex-UK
5.0 (3.0)
2.5 (1.3)
7.8 (2.8)
10.7 (3.0)
4.3 (1.8)
2.1 (0.9)
US
1.9 (1.3)
−2.4 (−1.0)
−0.1 (−0.1)
−4.3 (−1.0)
−1.1 (−0.6)
−4.8 (−1.4)
UK
−0.3 (−0.1)
2.4 (0.9)
5.7 (1.6)
10.2 (1.8)
−3.9 (−1.2)
−2.4 (−0.6)
Japan
8.9 (3.9)
8.7 (2.8)
9.6 (1.9)
9.8 (1.4)
15.4 (6.2)
16.7 (5.1)
World
8.7 (4.0)
8.5 (3.5)
9.9 (3.0)
11.1 (2.8)
9.1 (1.9)
10.8 (2.1)
Small versus large
Europe ex-UK
7.2 (4.4)
5.2 (2.5)
5.2 (1.8)
0.2 (0.1)
6.5 (2.3)
7.4 (2.0)
US
3.9 (2.5)
7.4 (3.2)
2.8 (0.7)
8.3 (1.4)
1.9 (0.9)
2.6 (0.8)
UK
5.0 (2.9)
2.4 (0.9)
2.7 (0.8)
−2.9 (−0.5)
4.0 (1.4)
2.0 (0.4)
Japan
5.4 (2.4)
6.7 (2.1)
4.4 (0.9)
3.8 (0.6)
8.2 (2.3)
11.6 (2.2)
World
8.2 (5.3)
7.8 (3.9)
7.4 (2.7)
5.3 (1.3)
6.7 (2.4)
7.4 (2.3)
6-month price momentum (execution lagged by 1 month)
Europe ex-UK
10.7 (5.2)
12.0 (4.8)
10.9 (2.7)
12.0 (2.3)
7.0 (1.9)
8.3 (2.0)
US
4.1 (2.8)
5.7 (2.5)
7.4 (2.6)
11.1 (2.5)
0.7 (0.3)
−0.7 (−0.2)
UK
7.7 (3.8)
9.9 (3.6)
7.5 (1.7)
11.5 (1.7)
7.2 (2.1)
8.0 (2.0)
Japan
0.5 (0.2)
1.1 (0.4)
3.6 (0.8)
4.4 (0.8)
−3.7 (−1.1)
−7.1 (−1.6)
World
8.0 (4.3)
9.3 (4.5)
10.5 (2.7)
11.6 (2.5)
5.9 (1.8)
5.6 (1.7)
* We are interested in those returns with a t-stat at 2.0 or above, then we highlight either the sector relative or
market-wide factor with the best annualized returns.
Source: DrKW Macro research.
the market-wide number. For price momentum the results are marginally in favour of the
sector-relative measure but only just, and in most cases the absolute level of achieved returns
are the more interesting.
--- page 427 ---

Sector-Relative Factors Work Best
403
Table 33.2
Risk-adjusted returns by factor and by region
Last 30 years
Last 10 years
Prior 10 years
Region
Sector
Market
Sector
Market
Sector
Market
Price to Cashﬂow
Europe ex-UK
0.61
0.46
0.88
0.71
0.76
0.67
US
0.81
0.42
0.83
0.37
0.29
0.05
UK
0.72
0.42
0.76
0.65
0.66
0.38
Japan
0.84
0.64
1.07
0.88
0.98
0.82
World
1.05
0.83
1.73
1.05
0.59
0.48
Price to Earnings
Europe ex-UK
0.93
0.60
0.67
0.69
1.23
0.99
US
0.71
0.36
0.43
0.28
0.16
−0.06
UK
0.79
0.64
0.95
0.86
0.50
0.42
Japan
0.67
0.64
0.37
0.49
1.03
0.91
World
0.76
0.70
0.90
0.82
0.50
0.46
Price to Book
Europe ex-UK
0.61
0.47
0.64
0.88
0.68
0.37
US
0.51
0.43
0.38
0.42
0.42
0.21
UK
0.67
0.35
0.69
0.50
0.75
0.44
Japan
0.92
0.72
0.69
0.59
2.03
1.27
World
0.73
0.66
0.71
0.64
0.65
0.67
Dividend Yield
Europe ex-UK
0.53
0.22
0.89
0.95
0.57
0.30
US
0.23
−0.17
−0.02
−0.32
−0.19
−0.44
UK
−0.02
0.16
0.49
0.58
−0.38
−0.20
Japan
0.70
0.50
0.60
0.46
1.96
1.62
World
0.70
0.63
0.96
0.90
0.61
0.67
Small versus large cap
Europe ex-UK
0.79
0.44
0.57
0.02
0.73
0.64
US
0.44
0.56
0.24
0.46
0.27
0.25
UK
0.51
0.16
0.26
−0.16
0.44
0.14
Japan
0.42
0.38
0.29
0.18
0.72
0.69
World
0.94
0.70
0.86
0.42
0.76
0.72
6-month price momentum (lagged by 1 month)
Europe ex-UK
0.93
0.87
0.86
0.74
0.61
0.63
US
0.50
0.45
0.82
0.80
0.10
−0.06
UK
0.68
0.65
0.54
0.53
0.68
0.64
Japan
0.04
0.07
0.26
0.25
−0.36
−0.52
World
0.78
0.81
0.86
0.79
0.58
0.54
Source: DrKW Macro research.
CONCLUSION
So our back-tests seem to conclude that when building a stock screening or selection process,
most valuation criteria beneﬁt from being adjusted relative to their sector peers but price
momentum doesn’t. Size, while working sector-relative, presents a practical problem in that
given the lower returns from a stand-alone size strategy it would need to be timed, and from our
perspective small size tends to outperform from a low not high valuation base. As such size,
while undoubtedly an important factor, can be ignored in favour, of sector-relative valuation,
i.e. if Smallcaps were cheap the model should be highlighting them anyway.
--- page 428 ---
--- page 429 ---

34
Cheap Countries Outperform*
Cheap countries outperform their expensive counterparts by around 7% p.a. Instead of worrying too much about correlations, those with a global equity mandate
should concentrate their portfolios in the cheapest markets. We also ﬁnd a strong
momentum effect within relative equity market selection.
Ĺ In this chapter we update and extend work originally done by Asness et al. (1997). They
found strong parallels between the cross-sectional performance of stocks and countries;
that is to say, cheap countries outperformed expensive countries (just as cheap stocks tend
to outperform expensive stocks). And those countries that have done best over the last
12 months tend to continue to do well (just as happens with stocks).
Ĺ Our empirical ﬁndings show that cheap countries outperform expensive countries by around
7% p.a. The worst performing “value” strategy was simple PE which still showed a 5.5%
outperformance by cheap countries! Dividend yield and price to book both showed higher
“value” outperformance. The value effects we ﬁnd are not just compensation for greater
risk.
Ĺ Momentum effects are even stronger than value effects. The highest momentum countries
outperform the lowest momentum countries by nearly 16% p.a.!
Ĺ We explore both long-only and long/short versions of these value and momentum-based
strategies, and present various diagnostics on these baskets. In general, both value and
momentum strategies add value to country selection.
*This article appeared in Global Equity Strategy on 30 April 2003. The material discussed was accurate at the time of publication.
--- page 430 ---
--- page 431 ---

Cheap Countries Outperform
407
75
77
79
81
83
85
87
89
91
93
95
97
99
01
03
−0.60
−0.40
−0.20
0
0.20
0.40
0.60
0.80
1.00
−0.60
−0.40
−0.20
0
0.20
0.40
0.60
0.80
1.00
Figure 34.1
Problem or distraction? 36 month rolling correlation US and UK equity returns.
Source: DrKW Macro research.
Several client meetings have uncovered much sympathy for our view on the UK market.
However, one question keeps coming up time and time again: What about the correlation
with the US market? The trouble with correlations is that they alter over time – for instance,
according to Goetzmann et al. (00), the UK/US correlation has ranged from 0.08 to 0.51 at
various times since the 1870s (see Global Equity Strategy, 22 July 2002, for more details).
One client even suggested that my much beloved valuation framework might be as good as
useless! I would refute this on the grounds that, in the long run, as we have shown many
times before, valuations determine returns. However, this leads to the obvious question of the
necessary time horizon in order to exploit such opportunities (Figure 34.1).
Now I have to make a confession. I am, at heart, a value investor, and as such I have
pretty much taken on faith the idea that cheapness tends to outperform. However, upon further
reﬂection it struck me that most of the studies I had read, or the empirical work I had done,
was actually based on stock data – that is to say, within each country, value strategies tended
to outperform over the long run. But I had seen very little work on whether this was true at the
country level.
As I have noted in other contexts, Sherlock Holmes was fond of opining “It is a capital
mistake to theorize before you have all the evidence. It biases the judgement.” Could I have
fallen foul of this advice?
Somewhere in the dim and distant past, I was sure I had seen someone writing on whether
value strategies worked at the country level. A quick search of my study at home revealed that
the article I had been thinking of was ‘Parallels between the cross-sectional predictability of
stock and country returns’ by Asness et al. (1997). This insightful paper showed that value
effects (as deﬁned by high book to price outperforming low book to price), and momentum
effects were both seen at the country level as well as the stock level.
I decided to update and extend their study, and with the invaluable aid of Rui Antunes
from our Global Quantitative Strategy team, we embarked on doing so. The ﬁrst runs weren’t
promising; we couldn’t ﬁnd the effects we had hoped. So I contacted Cliff Asness who kindly
pointed out that there was an error in our data-downloading process which altered the lining
--- page 432 ---

408
Behavioural Investing
Table 34.1
Summary of performance
Strategy
Average
Long/Short Return
% p.a
Average
Excess Return
% p.a.
Dividend yield
6.8
6.0
Price to book
7.3
6.1
Price to earnings
5.5
4.6
Momentum
15.8
9.0
Source: DrKW Macro research.
up of the dates.1 Once we had put this right, the splendid truth was revealed. Cheap countries
outperformed expensive countries in the cross-section. My faith in value investing was restored.
In order to test the hypothesis we followed the methodology set out by Asness et al. The
universe of countries is the MSCI World in local currency (excluding Finland, Ireland, New
Zealand and Malaysia2). Each month we sorted the universe into tritiles on whichever criteria
we were examining. We then formed equally weighted portfolios at the month end, and tracked
total returns over the next month. We repeated this process monthly. The sample we used was
01/1975–03/2003.
Table 34.1 provides a summary of our ﬁndings. The ﬁrst column shows the average annual
return to a portfolio that goes long the top tritile (in terms of dividends and momentum) or
long the bottom tritile (in terms of price to book and price to earnings) against a short position
in the bottom tritile (in terms of dividends and momentum) or the top tritile (in terms of price
to book and price to earnings). Regardless of how we choose to deﬁne ‘value’ the strategies
show that an equal long short portfolio in favour of cheapness produces good returns. For
instance, a strategy that is long the highest dividend yielding tritile of the MSCI World, and
short the lowest yielding tritile, generates an average annual return of 6.8%.
As per Asness et al., we also check to see if countries exhibit a momentum effect. In our sort,
momentum is deﬁned as the price change over the prior 12 months. A very strong momentum
effect is uncovered. Countries that have risen the most over the last 12 months continue to
do so in the following month; conversely, those that have seen the weakest momentum in the
previous 12 months continue to be weak in the next month.
The second column shows the equivalent return for a long only fund manager, assuming
a benchmark of the MSCI World. Thus the returns are expressed as the excess of the tritile
relative to the benchmark. Once again we ﬁnd a signiﬁcant performance enhancement from
concentrating on value and momentum. For instance, the highest dividend yielding tritile
of the MSCI World outperforms the index by 6% p.a. The top tritile, in terms of the prior
12 months’ price performance, outperforms the MSCI World by 9% p.a.
This value and momentum outperformance is not simply a function of taking on extra risk.
The tables and ﬁgures on the following pages lay out the detailed information on each strategy.
However, a summary is provided in Table 34.2. It shows the return per unit of risk differential
between the high and low tritiles, and the high tritile against the market. In all cases, the
1 Thanks to Cliff for sparing the time and effort to correct our oversight.
2 The removal of these countries is not designed to ﬁx our results. It is just that they enter the universe later than 1975. We tested
to see if their exclusion signiﬁcantly altered the results, and found it didn’t.
--- page 433 ---

Cheap Countries Outperform
409
Table 34.2
Return risk differentials across strategies
Long/Short Return/Risk
Differential
Long Only
Return/Risk
Differential
DY
0.13
0.10
PB
0.14
0.09
PE
0.12
0.07
MOM
0.26
0.12
Source: DrKW Macro research.
Table 34.3
Current basket contents
DY
PB
PE
MOM
Long
Long
Long
Long
Belgium
Germany
Japan
Austria
Netherlands
Hong Kong
Belgium
Canada
Italy
Norway
Hong Kong
Australia
Norway
Japan
UK
Hong Kong
France
Singapore
Netherlands
USA
Hong Kong
Belgium
Spain
Japan
Short
Short
Short
Short
Denmark
Canada
USA
Norway
Austria
Spain
Switzerland
France
Canada
Australia
Italy
Belgium
USA
Netherlands
Germany
Sweden
Switzerland
Switzerland
France
Netherlands
Japan
USA
Sweden
Germany
Source: DrKW Macro research.
strategies show a positive differential, suggesting that their value added is not simply a result
of higher risk.
You may be wondering which countries are being suggested by this approach at the moment.
Table 34.3 lists out the long and short basket contents for April 2003. Sadly from my point of
view the UK only appears in the PE based selection!
STRATEGY BY STRATEGY INFORMATION
For each of the strategies we present a summary table and ﬁve graphs. The tables, like
Table 34.4, show a variety of information, most of which is hopefully self-explanatory.
However, some elements might beneﬁt from a little expansion.
We present two t-tests. The ﬁrst (labelled as T-test for difference in means) checks to see
if the average value obtained from the high and low portfolios are statistically different – an
absolute value greater than 1.6 is sufﬁcient to say we are 95% sure that the means are different.
Each of the strategies passes this test.
The second t-test we perform is to assess whether the average return from a long/short
portfolio is statistically different from zero. Again a ﬁgure of greater than absolute 1.6 is
--- page 434 ---

410
Behavioural Investing
Table 34.4
Summary data on dividend yield baskets (1975–2003)
DY
Average Monthly
Return
Average Monthly Risk
Return/risk
High
1.5
4.5
0.33
Medium
1.0
4.6
0.23
Low
0.9
4.4
0.20
Market
1.0
4.0
0.24
T-test for difference
1.83
long-only α 1.38 (5.6)
long-only β 0.11 (1.9)
in means
T-test for long/short
3.69
long/short α 0.69 (4.0)
long/short β −0.1 (−1.7)
portfolio
% of correct calls
0.59
IC
0.17
IR
0.60
Source: DrKW Macro research.
enough for us to be sure that we can be 95% conﬁdent that such a portfolio doesn’t have a
zero average return. Once again all the portfolios pass this test.
The other pieces of information within Table 34.4 are the information coefﬁcient (IC) and
the information ratio (IR). The IC measures the correlation between the forecasts of the model
and the outcomes. It can be deﬁned as 2 × (f −0.5), where f is the percentage of calls the
model predicted accurately.
0
2000
4000
6000
8000
10000
12000
14000
Jan-75
Jan-78
Jan-81
Jan-84
Jan-87
Jan-90
Jan-93
Jan-96
Jan-99
Jan-02
High
Low
Figure 34.2
Portfolio performance 01/75=100.
Source: DrKW Macro research.
--- page 435 ---

Cheap Countries Outperform
411
−0.2
0
0.2
0.4
0.6
0.8
1
1.2
1.4
1.6
Jan-75
Jan-77
Jan-79
Jan-81
Jan-83
Jan-85
Jan-87
Jan-89
Jan-91
Jan-93
Jan-95
Jan-97
Jan-99
Jan-01
Jan-03
Figure 34.3
Cumulative returns on long/short portfolio.
Source: DrKW Macro research.
0
1
2
3
4
5
6
7
Jan-76
Jan-78
Jan-80
Jan-82
Jan-84
Jan-86
Jan-88
Jan-90
Jan-92
Jan-94
Jan-96
Jan-98
Jan-00
Jan-02
Figure 34.4
Standard deviation of long/short returns.
Source: DrKW Macro research.
--- page 436 ---

412
Behavioural Investing
−0.4
−0.2
0
0.2
0.4
0.6
0.8
1
1.2
1.4
1.6
Feb-75
Feb-77
Feb-79
Feb-81
Feb-83
Feb-85
Feb-87
Feb-89
Feb-91
Feb-93
Feb-95
Feb-97
Feb-99
Feb-01
Feb-03
Figure 34.5
Cumulative excess returns – long-only portfolio.
Source: DrKW Macro research.
−3
−2
−1
0
1
2
3
4
Feb-76
Feb-78
Feb-80
Feb-82
Feb-84
Feb-86
Feb-88
Feb-90
Feb-92
Feb-94
Feb-96
Feb-98
Feb-00
Feb-02
Figure 34.6
Standard deviation of long-only excess returns.
Source: DrKW Macro research.
Table 34.5
Summary data on price to book baskets (1975–2003)
PB
Average Monthly
Return
Average Monthly Risk
Return/Risk
High
0.9
4.7
0.19
Medium
1.1
4.4
0.24
Low
1.5
4.4
0.33
Market
1.0
4.0
0.24
T-test for difference
−1.59
long only α 1.35 (5.5)
long only β 0.10 (1.7)
in means
T-test for long/short
−3.06
long/short α 0.64 (3.4)
long/short β −0.1 (−1.9)
portfolio
% of correct calls
0.56
IC
0.13
IR
0.44
Source: DrKW Macro research.
--- page 437 ---

Cheap Countries Outperform
413
0
2000
4000
6000
8000
10000
12000
Jan-75
Jan-78
Jan-81
Jan-84
Jan-87
Jan-90
Jan-93
Jan-96
Jan-99
Jan-02
High
Low
Figure 34.7
Portfolio performance 01/75 = 100.
Source: DrKW Macro research.
−0.5
0
0.5
1
1.5
2
2.5
Jan-75
Jan-77
Jan-79
Jan-81
Jan-83
Jan-85
Jan-87
Jan-89
Jan-91
Jan-93
Jan-95
Jan-97
Jan-99
Jan-01
Jan-03
Figure 34.8
Cumulative returns on long/short portfolio.
Source: DrKW Macro research.
--- page 438 ---

414
Behavioural Investing
0
1
2
3
4
5
6
Jan-76
Jan-78
Jan-80
Jan-82
Jan-84
Jan-86
Jan-88
Jan-90
Jan-92
Jan-94
Jan-96
Jan-98
Jan-00
Jan-02
Figure 34.9
Standard deviation of long/short returns.
Source: DrKW Macro research.
−0.4
−0.2
0
0.2
0.4
0.6
0.8
1
1.2
1.4
1.6
Feb-75
Feb-77
Feb-79
Feb-81
Feb-83
Feb-85
Feb-87
Feb-89
Feb-91
Feb-93
Feb-95
Feb-97
Feb-99
Feb-01
Feb-03
Figure 34.10
Cumulative excess returns – long-only portfolio.
Source: DrKW Macro research.
