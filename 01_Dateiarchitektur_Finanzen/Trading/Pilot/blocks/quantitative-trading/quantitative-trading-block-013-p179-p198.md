# Quantitative Trading_ How to Build Your Own Algorithmic -- Ernest P_ Chan -- Wiley Trading, 1, 2008 -- John Wiley & Sons, Ltd_ -- isbn13 9780470284889 -- e4d660df1c1a75e8676a28ff4f852fa7 -- Anna’s Archive.pdf — Chapter 8: Conclusion Can Independent Traders (pages 179–198)

--- page 179 ---

C H A P T E R 8
Conclusion
Can Independent Traders
Succeed?
Q
uantitative trading gained notoriety in the summer of 2007
when some enormous hedge funds run by some of the most
reputable money managers rung up losses measured in billions in just a few days (though some had recovered by the end of
the month). They brought back bad memories of other notorious
hedge fund debacles such as that of Long-Term Capital Management
and Amaranth Advisors (both referenced in Chapter 6), except that
this time it was not just one trader or one ﬁrm, but losses at multiple
funds over a short period of time.
And yet, ever since I began my career in the institutional quantitative trading business, I have spoken to many small, independent
traders, working in shabby ofﬁces or their spare bedrooms, who
gain small but steady and growing proﬁts year-in and year-out, quite
unlike the stereotypical reckless day traders of the popular imagination. In fact, many independent traders that I know of have not
only survived the periods when big funds lost billions, but actually
thrived in those times. This has been the central mystery of trading
to me for many years: how does an independent trader with insignificant equity and minimal infrastructure trade with high Sharpe ratio
while ﬁrms with all-star teams fail spectacularly?
157
--- page 180 ---

158
QUANTITATIVE TRADING
At the beginning of 2006, I left the institutional money management business and struck out on my own to experience this ﬁrsthand. I ﬁgured that if I could not trade proﬁtably when I was free of
all institutional constraints and politics, then either trading is a hoax
or I am just not cut out to be a trader. Either way, I promised myself
that in such an event I would quit trading forever. Fortunately, I survived. Along the way, I also found the key to that central mystery to
which I alluded earlier.
The key, it turns out, is capacity, a concept I introduced at the
end of Chapter 2. (To recap: Capacity is the amount of equity a strategy can generate good returns on.) It is far, far easier to generate
a high Sharpe ratio trading a $100,000 account than a $100 million
account. There are many simple and proﬁtable strategies that can
work at the low capacity end that would be totally unsuitable to
hedge funds. This is the niche for independent traders like us.
Let me elaborate on this capacity issue. Most proﬁtable strategies that have low capacities are acting as market makers: providing short-term liquidity when it is needed and taking quick proﬁts
when the liquidity need disappears. If, however, you have billions
of dollars to manage, you now become the party in need of liquidity, and you have to pay for it. To minimize the cost of this liquidity
demand, you necessarily have to hold your positions over long periods of time. When you hold for long periods, your portfolio will
be subject to macroeconomic changes (i.e., regime shifts) that can
cause great damage to your portfolio. Though you may still be profitable in the long run if your models are sound, you cannot avoid the
occasional sharp drawdowns that attract newspaper headlines.
Other disadvantages beset large-capacity strategies favored by
large institutions. The intense competition among hedge funds
means the strategies become less proﬁtable. The lowered returns
in turn pressure the fund manager to overleverage. To beat out the
competition, traders need to resort to more and more complicated
models, which in turn invite data-snooping bias. But despite the increasing complexity of the models, the fundamental market inefﬁ-
ciency that they are trying to exploit may remain the same, and thus
their portfolios may still end up holding very similar positions. We
discussed this phenomenon in Chapter 6. When market environment
--- page 181 ---

Conclusion
159
changes, a stampede out of similar losing positions can (and did)
cause a complete meltdown of the market.
Another reason that independent traders can often succeed
when large funds fail is the myriad constraints imposed by management in an institutional setting. For example, as a trader in a
quantitative fund, you may be prohibited from trading a long-only
strategy, but long-only strategies are often easier to ﬁnd, simpler,
more proﬁtable, and if traded in small sizes, no more risky than
market-neutral strategies. Or you may be prohibited from trading
futures. You may be required to be not only market neutral but
also sector neutral. You may be asked to ﬁnd a momentum strategy when you know that a mean-reverting strategy would work.
And on and on. Many of these constraints are imposed for risk
management reasons, but many others may be just whims, quirks,
and prejudices of the management. As every student of mathematical optimization knows, any constraint imposed on an optimization problem decreases the optimal objective value. Similarly,
every institutional constraint imposed on a trading strategy tends to
decrease its returns, if not its Sharpe ratio as well. Finally, some
senior managers who oversee frontline portfolio managers of quantitative funds are actually not well versed in quantitative techniques,
and they tend to make decisions based on anything but quantitative
theories.
When your strategy shows initial proﬁts, these managers may
impose enormous pressure for you to scale up quickly, and when
your strategy starts to lose, they may force you to liquidate the portfolios and abandon the strategy immediately. None of these interferences in the quantitative investment process is mathematically
optimal.
Besides, such managers often have a mercurial temper, which
seldom mixes well with quantitative investment management. When
loss of money occurs, rationality is often the ﬁrst victim.
As an independent trader, you are free from such constraints
and interferences, and as long as you are emotionally capable to
adhere to the discipline of quantitative trading, your trading environment may actually be closer to the optimal than that of a large
fund.
--- page 182 ---

160
QUANTITATIVE TRADING
Actually, there is one more reason why it is easier for hedge
funds to blow up than for individual traders trading their own accounts to do so. When one is trading other people’s money, one’s
upside is almost unlimited, while the downside is simply to get ﬁred.
Hence, despite the pro forma adherence to stringent institutional
risk management procedures and constraints, one is fundamentally
driven to trade strategies that are more risky in an institutional setting, as long as you can sneak past the risk manager. But Mr. J´erˆome
Kerviel at Soci´et´e G´en´erale has shown us that this is not at all
difﬁcult!
L’Affaire Soci´et´e G´en´erale cost the bank $7.1 billion and may
have indirectly led to an emergency Fed rate cut in the United States.
The bank’s internal controls failed to discover the rogue trades for
three years because Mr. Kerviel has worked in the back ofﬁce and
has gained great familiarity with ways to evade the control procedures (Clark, 2008).
In fact, Mr. Kerviel’s deceptive technique is by no means original.
When I was working at a large investment bank, there was a pair of
proprietary traders who traded quantitatively. They were enclosed
in a glass bubble at a corner of the vast trading ﬂoor, either because
they could not be bothered by the hustle and bustle of the nonquantitative traders, or they had to keep their trade secrets, well, secret.
As far as I could tell, neither of them ever talked to anyone. Nor, it
seemed, did they ever speak to each other.
One day, one of the traders disappeared, never to return. Shortly
thereafter, hordes of auditors were searching through his ﬁles and
computers. It turned out that, just like Mr. Kerviel, this trader had
worked in the information technology (IT) department and was
quite computer savvy. He managed to manufacture many millions
of false proﬁts without anyone’s questioning him until, one day, a
computer crash somehow stopped his rogue program in its track
and exposed his activities. Rumor had it that he disappeared to India and has been enjoying the high life ever since.
So there you have it. I hope I have made a convincing case that
independent traders can gain an edge over institutional traders, if
trading is conducted with discipline and care. Of course, the side
beneﬁts of being independent are numerous, and they begin with
--- page 183 ---

Conclusion
161
freedom. Personally, I am much happier with my work now than I
have ever been in my career, despite the inevitable gut-wrenching
drawdowns from time to time.
NEXT STEPS
So let’s say you have found a few good, simple strategies and are
happily trading in your spare bedroom. Where do you go from here?
How do you grow?
Actually, I discussed growth in Chapter 6, but in a limited sense.
Using the Kelly formula, you can indeed achieve exponential growth
of your equity, but only up to the total capacity of your strategies. After that, the source of growth has to come from increasing the number of strategies. You can, for example, look for strategies that trade
at higher frequencies than the ones you currently have. To do that,
you have to invest and upgrade your technological infrastructure,
and purchase expensive high-frequency historical data. Or, conversely, you can look for strategies that hold longer periods. Despite
their typically lower Sharpe ratios, they do enormously improve
your capacity. For many of these strategies, you probably have to
invest in expensive historical fundamental data for your backtest.
If you are an equity trader, you can branch out into futures or
currencies, which typically have higher capacities than equity models. If you run out of ideas or lack expertise in a new market that you
want to enter, you can form collaborations with other like-minded
traders, or you can hire consultants to help with the research. If you
are running too many strategies to manage manually on your own,
you can push your automation further so that there is no need for
you to manually intervene in the daily trading unless exceptions or
problems occur. Of course, you can also hire a trader to monitor all
these strategies for you.
These investments in data, infrastructure, and personnel are all
part of reinvesting some of your earnings to further the growth of
your trading business, not unlike growing any other type of business. When you have reached a point where your capacity is higher
than what the Kelly formula suggests you can prudently utilize, it
--- page 184 ---

162
QUANTITATIVE TRADING
may be time for you to start taking on investors, who will at the very
least defray the costs of your infrastructure, if not provide an incentive fee. Alternatively, you might want to take your strategy (and,
more importantly, your track record) to one of the larger hedge
funds and ask for a proﬁt-sharing contract.
After the recent major losses at quantitative hedge funds, many
people have started to wonder if quantitative trading is viable in the
long term. Though the talk of the demise of quantitative strategies
appears to be premature at this point, it is still an important question from the perspective of an independent trader. Once you have
automated everything and your equity is growing exponentially, can
you just sit back, relax, and enjoy your wealth? Unfortunately, experience tells us that strategies do lose their potency over time as
more traders catch on to them. It takes ongoing research to supply
you with new strategies.
There are always upheavals and major regime changes that may
occur once every decade but will nevertheless cause sudden deaths
to certain strategies. As with any commercial endeavor, a period of
rapid growth will inevitably be followed by the steady if unspectacular returns of a mature business. As long as ﬁnancial markets demand instant liquidity, however, there will always be a proﬁtable
niche for quantitative trading.
--- page 185 ---

A P P E N D I X
A Quick Survey
of MATLAB
M
ATLAB is a general-purpose software package developed
by Mathworks, Inc., which is used by many institutional
quantitative researchers and traders as their platform for
backtesting, particularly those that work in statistical arbitrage. In
Chapter 3, I introduced this platform and compared its pros and
cons with some other alternatives. Most of the strategy examples
in this book are written in MATLAB. Many of those strategies are
portfolio-trading strategies involving hundreds of stocks that are
very difﬁcult to backtest in Excel. Here, I will provide a quick survey
of MATLAB for those traders who are unfamiliar with the language,
so they can see if it is worthwhile for them to invest in acquiring and
learning to use this platform for their own backtesting.
MATLAB is not only a programming language; it is also an integrated development platform that includes a very user-friendly program editor and debugger. It is an interpreted language, meaning
that similar to Visual Basic, but unlike a conventional programming
language like C, it does not need to be compiled before it can be
run. Yet it is much more ﬂexible and powerful for backtesting than
using Excel or Visual Basic because of the large number of builtin functions useful for mathematical computations, and because it
is an array-processing language that is specially designed to make
163
--- page 186 ---

164
APPENDIX
computations on arrays (i.e., vectors or matrices) simply and
quickly. In particular, many loops that are necessary in C or Visual
Basic can be replaced by just one line of code in MATLAB. It also
includes extensive text processing facilities such that it is useful as
a powerful tool for parsing and analyzing texts (such as web pages).
Furthermore, it has a comprehensive graphics library that enables
easy plotting of many types of graphs, even animations. (Many of
the ﬁgures and charts in this book are created using MATLAB.) Finally, MATLAB codes can be compiled into C or C++ executables
that can run on computers without the MATLAB platform installed.
In fact, there is third-party software that can convert MATLAB code
into C source codes, too.
The basic syntax of MATLAB is very similar to Visual Basic or C.
For example, we can initialize the elements of an array x like this:
x(1)=0.1;
x(2)=0.3;
% 3 elements of an array initialized.
% This is by default a row-vector
x(3)=0.2;
Note that we don’t need to ﬁrst “declare” this array, nor do we
need to tell MATLAB its expected size beforehand. If you leave out
the “;” sign, MATLAB will print out the result of the content of the
variable being assigned a value. Any comments can be written after
the “%” sign. If you wish, you can initialize a large number of elements en masse to a common value:
% assigning the value 0.8 to all elements of a 3-vector y.
This is a row-vector.y=0.8*ones(1, 3)
Now if you want to do a vector addition of the two vectors, you
can do it the old-fashioned way (just as you would in C), that is,
using a loop:
for i=1:3
z(i)=x(i)+y(i) % z is [0.9 1.1 1]
end
But the power of MATLAB is that it can handle many array operations in parallel very succinctly, without using loops. (That’s why it
--- page 187 ---

A Quick Survey of MATLAB
165
is called a vector-processing language.) So instead of the loop above,
you can just write
z=x+y % z is the same [0.9 1.1 1]
Even more powerful, you can easily select part of the different
arrays and operate on them. What do you think would be the results
of the following?
w=x([1 3])+z([2 1])
x([1 3]) selected the ﬁrst and third elements of x, so x([1 3]) is
just [0.1 0.2]. z([2 1]) selected the second and ﬁrst elements of y, in
that order, so z([2 1]) is [1.1 0.9]. So w is [1.2 1.1].
You can delete parts of an array just as easily:
x([1 3])=[] % this leaves x as [0.3]
To concatenate two arrays is also trivial. To concatenate by
rows, use the “;” to separate the arrays:
u=[z([1 1]); w]
% u is now
% [0.9000
0.9000;
% 1.2000
1.1000]
To concatenate by columns, omit the “;”:
v=[z([1 1]) w]
% v is now
% [0.9000
0.9000
1.2000
1.1000]
Selection of a subarray can be done not only with arrays containing indices; it can be done with arrays containing logical values
as well. For example, here is a logical array:
vlogical=v<1.1
% vlogical is [1 1 0 0], where the 0s and 1’s
% indicate whether that element is less than 1.1 or
% not.
vlt=v(vlogical) % vlt is [0.9 0.9]
--- page 188 ---

166
APPENDIX
In fact, we can select the same subarray with the oft-used shorthand
vlt=v(v<1.1) % vlt is the same [0.9 0.9]
If, for some reasons, you are interested in the actual indices of
the elements of v that have value less than 1.1, you can use the “ﬁnd”
function:
idx=find(v<1.1); % idx is [1 2]
Naturally, you can use this index array to select the same subarray as before:
vlt=v(idx); % vlt is the again same [0.9 0.9]
So far, the array examples are all one-dimensional. But of
course, MATLAB can deal with multidimensional arrays as well.
Here is a two-dimensional example:
x=[1 2 3; 4 5 6; 7 8 9];
% x is
%
1
2
3
%
4
5
6
%
7
8
9
You can select the entire row or column of multi-dimensional
array by using the “:” symbol. For example,
xr1=x(1,:) % xr1 is the first row of x, i.e. xr1 is [1 2 3]
xc2=x(:, 2)% xc2 is the second column of x, i.e. xc2 is
% 2
% 5
% 8
Naturally, you can delete an entire row from an array using the
same method.
x(1,:) =[] % x is now just [4 5 6; 7 8 9]
--- page 189 ---

A Quick Survey of MATLAB
167
The transpose of a matrix is indicated by a simple ‘′’. So the
transpose of x is just x′, which is
4
7
5
8
6
9
Elements of arrays do not have to be numbers. They can be
strings, or even arrays themselves. This kind of arrays is called cell
array in MATLAB. In the following example, C is just such a cell
array:
C={[1 2 3]; [‘a’ ‘b’ ‘c’ ‘d’]}
% C is
% [1 2 3]
% ‘abcd’
One of the beauties of MATLAB is that practically all built-in
functions can work on all elements of arrays concurrently. For example,
log(x) % this gives
% 1.3863
1.6094
1.7918
% 1.9459
2.0794
2.1972
There are a large number of such built-in functions. Some of the
ones I have used are:
sum, cumsum, diag, max, min, mean, std, corrcoef,
repmat, reshape, squeeze, sort, sortrow, rand, size,
length, eigs,
fix, round, floor, ceil, mod,
factorial, setdiff, union, intersect, ismember,
unique, any, all, eval, eye, ones, strmatch, regexp,
regexprep, plot, hist, bar, scatter, try, catch,
circshift, datestr, datenum,
isempty, isfinite,
isnan, islogical, randperm
If the built-in functions of the basic MATLAB platform do not
meet all your needs, you can always purchase additional toolboxes from MATLAB. Some of the toolboxes useful to quantitative traders are the optimization, partial differential equations
--- page 190 ---

168
APPENDIX
(for derivative traders), genetic algorithms, statistics, neural networks, signal processing, wavelet, ﬁnancial, ﬁnancial derivatives,
GARCH, ﬁnancial times series, datafeed, and ﬁxed-income toolboxes. If these toolboxes are too costly, or if they still do not meet
all your needs, there are also a number of free user-contributed toolboxes available for download from the Internet. I have introduced
one of them in this book: the Econometrics toolbox developed by
James LeSage (www.spatial-econometrics.com). There are a number of others that I have used before: the Bayes Net toolbox from
Kevin Murphy (www.cs.ubc.ca/∼murphyk/Software/BNT/bnt.html),
or the GARCH toolbox from Kevin Sheppard (www.kevinsheppard.
org/research/ucsd garch/ucsd garch.aspx). The easy availability of
these user-contributed toolboxes and the large community of MAT-
LAB users from whom you can ask for help greatly enhance the usefulness of MATLAB as a computational platform.
You can, of course, write your own functions in MATLAB, too. I
have given a number of example functions in this book, all of which
can be downloaded from my web site, www.epchan.com/book. In
fact, it is very helpful for you to develop your own library of utilities
functions that you often use for constructing trading strategies. As
this homegrown library grows, your productivity in developing new
strategies will increase as well.
--- page 191 ---

Bibliography
Alexander, Carol. 2001. Market Models: A Guide to Financial Data Analysis. West Sussex: John Wiley & Sons Ltd.
Chai, Soo, and Joon Lim. 2007. “Economic Turning Point Forecasting Using Neural Network with Weighted Fuzzy Membership Functions.” Lecture
Notes in Computer Science, Springer.
Clark, Nicola. 2008. “French Bank Says Its Controls Failed for 2 Years.”
New York Times, Febrary 21. Available at: http://www.nytimes.com/2008/
02/21/business/worldbusiness/21bank.html?ex=1361336400&en=cf84f377
6a877eac&ei=5124&partner=permalink&exprod=permalink.
Cover, Thomas. 1991. “Universal Portfolios.” Mathematical Finance 1(1):
1–29.
Duhigg, Charles. 2006. “Street Scene; A Smarter Computer to Pick Stock.”
New York Times, November 24.
Economist. 2007a. “Too Much Information.” July 12. Available at: www
.economist.com/ﬁnance/displaystory.cfm?story id=9482952.
Economist. 2007b. “This Year’s Model.” December 13. Available at: www
.economist.com/ﬁnance/displaystory.cfm?story id=10286619.
Fama, Eugene, and Kenneth French. 1992. “The Cross-Section of Expected
Stock Returns.” Journal of Finance XLVII(2): 427–465.
Fielden, Sandy. 2006. “Seasonal Surprises.” Energy Risk, September. Available at: www.lim.com/pdfdocs/marketing/marketfocus sept05.pdf.
Grinold, Richard, and Ronald Kahn. 1999. Active Portfolio Management.
New York: McGraw-Hill.
Kaufmann, Sylvia, and Martin Scheicher. 1996. “Markov-Regime Switching
in Economic Variables: Part I. Modelling, Estimating and Testing. Part II.
A Selective Survey.” Institute for Advanced Studies Economics Series
no. 38.
169
--- page 192 ---

170
BIBLIOGRAPHY
Klaassen, Franc. 2002. “Improving GARCH Volatility Forecasts with
Regime-Switching GARCH.” Empirical Economics 27(2): 363–394.
Khandani, Amir, and Lo, Andrew. 2007. “What Happened to the Quants
in August 2007?” Preprint. Available at: web.mit.edu/alo/www/Papers/
august07.pdf.
Lux, Hal. 2000. “The Secret World of Jim Simons.” Institutional Investor
Magazine, November 1.
Markoff, John. 2007. “Faster Chips Are Leaving Programmers in Their
Dust.” New York Times, December 17. Available at: www.nytimes.com/
2007/12/17/technology/17chip.html?ex=1355634000&en=a81769355deb79
53&ei=5124&partner=permalink&exprod=permalink.
Nielsen, Steen, and Jan Overgaard Olesen. 2000. “Regime-Switching Stock
Returns and Mean Reversion.” Working Paper 11–2000. Department of Economics, Copenhagen Business School.
Oldﬁeld, Richard. 2007. Simple but Not Easy. Doddington Publishing.
Poundstone, William. 2005. Fortune’s Formula. New York: Hill and
Wang.
Heston, Steven, and Ronnie Sadka. 2007. “Seasonality in the Cross-Section
of Expected Stock Returns.” AFA 2006 Boston Meetings Paper, July. Available at: lcb1.uoregon.edu/rcg/seminars/seasonal072604.pdf.
Ritter, Jay. 2003. “Behavioral Finance.” Paciﬁc-Basin Finance Journal
11(4), September: 429–437.
Sharpe, William. 1994. “The Sharpe Ratio.” Journal of Portfolio Management, Fall. Available at: www.stanford.edu/∼wfsharpe/art/sr/sr.htm.
Singal, Vijay. 2006. Beyond the Random Walk. Oxford University Press,
USA.
Schiller, Robert. 2007. “Historic Turning Points in Real Estate.” Cowles
Foundation Discussion Paper No. 1610. Available at: cowles.econ.yale.edu.
Schiller, Robert. 2008. “Economic View; How a Bubble Stayed under the
Radar.” New York Times, March 2. Available at www.nytimes.com/2008/
03/02/business/02view.html?ex=1362286800&en=da9e48989b6f937a&ei=
5124&partner=permalink&exprod=permalink.
Taleb, Nassim. 2007. The Black Swan: The Impact of the Highly Improbable. Random House.
Thaler, Richard. 1994. The Winner’s Curse. Princeton, NJ: Princeton University Press.
--- page 193 ---

Bibliography
171
Thorp, Edward. 1997. “The Kelly Criterion in Blackjack, Sports Betting, and the Stock Market.” Handbook of Asset and Liability Management, Volume I, Zenios and Ziemba (eds.). Elsevier 2006. Available at:
www.EdwardOThorp.com.
Toepke, Jerry. 2004. “Fill ‘Er Up! Beneﬁt from Seasonal Price Patterns
in Energy Futures.” Stocks, Futures and Options Magazine. March 3(3).
Available at: www.sfomag.com/issuedetail.asp?MonthNameID=March&
yearID=2004.
Uhlenbeck, George, and Leonard Ornstein. 1930. “On the Theory of Brownian Motion.” Physical Review 36: 823–841.
Van Norden, Simon, and Huntley Schaller. 1997. “Regime Switching in
Stock Market Returns.” Applied Financial Economics 7: 177–191.
--- page 194 ---
--- page 195 ---

About the Author
E
rnest P. Chan is the founder of E. P. Chan & Associates
(www.epchan.com), a consulting ﬁrm focusing on trading strategy and software development for money managers. He also co-manages EXP Quantitative Investments, LLC and
publishes the Quantitative Trading blog (epchan.blogspot.com),
which is syndicated to multiple ﬁnancial news services including
www.tradingmarkets.com and Yahoo! Finance. He has been quoted
by the New York Times and CIO magazine on quantitative hedge
funds, and has appeared on CNBC’s Closing Bell.
Ernie is an expert in developing statistical models and advanced
computer algorithms to discover patterns and trends from large
quantities of data. He was a researcher in computer science at IBM’s
T. J. Watson Research Center, in data mining at Morgan Stanley, and
in statistical arbitrage trading at Credit Suisse. He has also been a senior quantitative strategist and trader at various hedge funds, with
sizes ranging from millions to billions of dollars.
Ernie received his undergraduate degree from the University of
Toronto, and master of science and doctor of philosophy degrees
in theoretical physics from Cornell University. In recognition of his
expertise in statistical data mining, he was invited to serve on the
Program Committees of the International Conference of Knowledge
Discovery and Data Mining in 1998 and also of the SPIE Conference
on Data Mining and Knowledge Discovery in 1999. He was also invited to speak at the panel on Effective Arbitrage Strategies at the
ETF Evolution conference in New York in 2007.
173
--- page 196 ---
--- page 197 ---

Index
A
Abnormal Returns, 10
Aegis System (Barra), 35
Alea Blog, 10
Algorithmic trading. See
Quantitative trading
Alphacet, 35, 36, 55, 85, 122–126
Alpha Testing (FactSet), 35
Amaranth Advisors, 110, 150, 157
Application programming
interface (API), 73, 84
Arbitrage pricing theory (APT).
See Factor models
Artiﬁcial intelligence, 116
and stock picking, 26–27
B
Backtesting, 20, 22, 24, 31–67,
144–148
common pitfalls to avoid,
50–60
data-snooping bias, 52–60
look-ahead bias, 51–52
common platforms, 32–36
Excel, 32
high-end, 35–36
MATLAB R⃝, 32–34
TradeStation, 35
historical databases, ﬁnding and
using, 36–43
high and low data, use of,
42–43
split and dividend-adjusted
data, 36–40
survivorship bias, 40–42
January effect, 144–146
performance measurement,
43–50
strategy reﬁnement, 65–66
transaction costs, 61–65
year-on-year seasonal trending
strategy, 146–148
Bank of Montreal, 150
Bayes Net toolbox, 168
Behavioral bias, 108–109
Behavioral ﬁnance, 108–111
Beta, 14
Black Monday, 106
“Black swan” events, 105
Bloomberg, 14, 36, 75
Bollinger bands, 23
Brett Steenbarger Trading
Psychology, 10
Bright Trading, 70
Business, setting up a, 69–78
choosing a brokerage or
proprietary trading ﬁrm,
71–75
physical infrastructure, 75–77
structure, 69–71
175
--- page 198 ---

176
INDEX
C
C#, 80, 85, 164
C++, 80, 85, 164
Calendar effect. See Seasonal
trading strategies
Capacity, 27, 158
Capital availability, effect on
choices, 15
Capital allocation, optimal, 95–103
Capital IQ, 136
Chicago Mercantile Exchange
(CME), 16
Clariﬁ, 35
CNBC Plus, 76
Cointegrating augmented
Dickey-Fuller test, 128
Cointegration, 126–133
forming a good cointegrating
pair of stocks, 128–130
Compustat, 136
Contagion, ﬁnancial, 104–105
Correlation, 131
Covariance matrix, 97
CSIdata.com, 37
CRSP.com, 37
D
Dark-pool liquidity, 71, 73, 88
Data mining, 121
Databases, historical, 37
Data-snooping bias, 25–27, 52–60,
91
out-of-sample testing, 53–55
sample size, 53
sensitivity analysis, 60
and underperformance of live
trading, 91
Decimalization of stock prices, 91,
120
Deleveraging, 152
Despair, 110
Disasters, physical or natural, 108
Discovery (Alphacet), 35, 36, 55,
85, 122–126
charting application, 125
Dollar-neutral portfolio, 43–44
Dow Jones, 36, 75
Drawdown, 20, 21–22, 43, 95
maximum, 21
calculating, 48–50
maximum duration, 21
calculating, 48–50
DTN.com, 37
Dynamic data exchange (DDE)
link, 80, 81–82, 83, 84, 85
E
ECHOtrade, 70
Econometrics toolbox, 168
The Economist, 10
Elite Trader, 10, 74
Elliott wave theory, 116
E-mini S&P 500 future, 16
Endowment effect, 108–109
Equity curve, 20
Excel, 3, 21, 32, 51, 163
dynamic data exchange (DDE)
link to, 80, 81–82, 83, 84, 85
using in automated trading
systems, 80, 81, 83, 84, 85
using to avoid look-ahead bias,
51
using to calculate maximum
drawdown and maximum
drawdown duration, 48
using to calculate Sharpe ratio
for long-only strategies,
45–46, 47
