# Quantitative financial analytics_ the path to investment profits.pdf — pages 381–400

--- page 381 ---

358
Quantitative Financial Analytics
Lakonishok, Josef, Andrei Shleifer, and Robert W. Vishny, “Contrarian
Investment, Extrapolation, and Risk,” Journal of Finance, December
1994, pp. 1541–1578.
Malkiel, B. G., A Random Walk Down Wall Street, 12th edn., New York,
NY: Norton, 2015.
Ross, Howard, The Elusive Art of Accounting. New York, NY: The Ronald
Press Company, 1966.
Rubinstein M., A History of the Theory of Investments. New York, NY:
John Wiley & Sons, 2006.
Sharpe, William F., Gordon J. Alexander, and Jeﬀery V. Bailey, Investments, 6th edn., Upper Saddle River, NJ: Prentice Hall, 1999.
Taleb, N., The Black Swan. New York: Random House, 2007.
Thompson, J. R., E. E. Williams, and M. C. Findlay, Models for Investors
in Real World Markets. New York, NY: John Wiley & Sons, 2003.
Williams, E. E. and M. C. Findlay, Investment Analysis. Englewood Cliﬀs,
NJ: Prentice Hall, Inc., 1974.
Williams, J. B., The Theory of Investment Value. Cambridge, MA: Harvard
University Press, 1938.
--- page 382 ---

Chapter 8
Futures and Options
We can easily represent things as we wish them to be.
Aesop
Introduction
This chapter is about futures, options and other derivatives, which
might be more aptly described as speculative securities. A futures
contract is a legally binding agreement to buy or sell a commodity or
ﬁnancial instrument at a later date. Futures contracts may be traded
on an organized exchange, or on the “over-the-counter (OTC)”
market. Exchange-traded contracts are standardized according to the
quality, quantity, and delivery time and location for each commodity.
The only variable is price. An option on a security gives the option
buyer the right — but not the obligation — to buy or sell a particular
asset at a stated price at any time prior to a speciﬁed date. There
are two fundamental types of options: calls and puts. A call option
conveys to the option buyer the right to purchase a particular security
at a stated price at any time during the life of the option. A put
option conveys to the option buyer the right to sell a particular asset
at a stated price at any time during the life of the option.
In general, a “derivative” security is simply a contract whose
value is determined by the performance of an underlying asset.
A philosophical example could be common stock, which is a security
laying claim to the earnings and net assets of a corporation.
Derivatives may be written or bought on other derivatives, such as
an option on a futures contract, or an option on an option.
359
--- page 383 ---

360
Quantitative Financial Analytics
Examples of speculative securities include:
• A credit default swap (CDS) is essentially an insurance product
which pays oﬀif a debt issuer defaults on its obligations. Buying
3-year credit default swaps on Greek sovereign debt back in 2007
would have cost about 15 bps annually, or about $150,000 per
annum for CDS on $100 million of Greek debt. At the height
of the Greek ﬁnancial crisis, these CDS were selling for around
5,000 bps (yielding in a 3,333 percent proﬁt). Note that the par
value (principal amount) of each bond is 10,000 bps. Thus, no CDS
would ever be valued more than that. It is interesting that, in the
Greek case cited, purchasers were willing to pay 1/3 of the par
value of the instrument simply for insurance.
• Buying puts on UAL and AA the week before the 9–11 attack
would have resulted in another tremendous proﬁt opportunity.
• One could have purchased deep out of the money calls (200 points)
on AAPL for $14.50 back in January 2012, and in September 2012,
they could have been sold for $100+, less the premium paid. Proﬁt
on a 10-call position: $85,500 on an investment of $14,500, or about
589 percent return. Proﬁt if buying an equivalent amount of stock
(36 shares): $25,375/$14,500 = 175 percent return.
• An option seller on expiration day in January 2013, sells 10 of
the February AAPL 450 puts for 70c, for income production.
These were 65 points out of the money, a safe bet for AAPL.
Four trading days later, these very puts had to be bought back at
$15.06, resulting in a loss of $14.36 per contract, a $14,360 loss on
potential gain of only $700, a 1,950 percent ﬂummoxing. Had the
trader been foolish enough to sell the February 500 puts at $8.00
each, she would have had to repurchase them at $53.50, for a loss
of $45,500.
• Buying 6-month puts on cotton in April 2012, ﬁve cents out of the
money, would have cost 1.64c per contract ($820); 5 months later
cotton had dropped 20c and each contract had increased in value
by $10,000, for a return of 1,219 percent.
• In 2005, when gold broke above $500/oz, the “smart money”
loaded up on gold futures and exchange-traded funds (ETF’s).
--- page 384 ---

Futures and Options
361
The steady rise of gold from $400 to almost $1,800/oz in 7 years
with its compound growth rate of 23.5 percent has been a major
success story of alternative investing.
From these examples, it can be seen that fabulous proﬁts (and
losses) have been obtained through speculating in common stock and
index options, futures and other derivatives. Although it is unlikely
that too many people actually bought or sold these instruments at
the times indicated in the above illustrations, it is nonetheless true
that price movements of large magnitudes have occurred for many
derivatives in the past, and the risk-seeking investor, albeit ruinaverse, should consider these instruments as a potentially attractive
speculative vehicle.
A famous example
When Ted Turner shocked the world on September 18, 1997 by
promising to give $1 billion of his wealth to the United Nations
programs over 10 years, he was not going to take any chances that
it could cost more than $1 billion. In fact, given his basis in the
stock, some could argue that it only cost him around $3 million;
indeed, others have mused that his after-tax position increased by
$100 million. Mr. Turner was quoted as saying “the donation will
be made in ten annual installments of $100 million in Time Warner
stock”. His August 1997 net worth was reportedly about $3.2 billion,
and TWX stock was trading at $51.50 per share, so he was ﬁguring
on selling around 20 million shares of the stock.
Sometime before the announcement, on May 12, 1997, Mr. Turner
had already established a collar on two million shares, when TWX
common was trading around $45; he bought 3-year put[s] with a
strike price of $39.63 and sold 3-year call[s] with a strike of $60.90.
This was presumably done on the over the counter market, as that is
the venue for deals such as these. This collar could have been a debit
position, i.e., it had a net positive cash ﬂow, but even if it didn’t,
the cost was not that much. Moreover, he could also borrow up to
90 percent of the put’s strike for additional liquidity if he needed to.
Given his likely negligible cost basis in Time Warner, Turner could
--- page 385 ---

362
Quantitative Financial Analytics
have simply sold covered calls on the position until he had to pay
a periodic payment; however, his cash ﬂow planning would beneﬁt
from a calculated downside of $39.63.
Eight months later in December 1997, when TWX was trading
around 62, on the way up to 100, it is likely that some or all of
his position would have been called, and he would have had to sell
at $60.90. Suppose the entire position was called. His proﬁt on the
upside was about (2,000,000)($15.90) = $31,800,000 (The $15.90
was the gain from $45 to $60.90). We don’t know his cost on the
puts, but assuming conservatively that it was a zero-cost collar, his
little proﬁt during this uptick was about $32 million. He could then
establish another collar further up the scale. By the time next year’s
installment was due, TWX had risen to 68 AFTER a stock split! This
pattern of higher and higher prices continued until about 2–3 months
prior to the AOL merger of January 11, 2001, after which the opposite
price performance was realized. The price languished around $15 to
$20 per share; during the good years Ted was making his payments
using only about one and a half to two million shares per year, but
from 2002 through 2006, his progress payments required some ﬁve
million shares apiece, for a total of up to 35 million shares.
Unfortunately, we have no way of knowing exactly how the
Turner deal played out, but the fact remains that he was able to lock
--- page 386 ---

Futures and Options
363
in his commitment at presumably no real transaction cost, especially
given his likely extremely low cost basis in the stock.
Futures
It is logical to begin our discussion with futures since the commodities
of life were the ﬁrst traded goods. Beer production was sold forward
as far back as in the time of Uruk III, Sumer, 31st century B.C.
Indeed, our record of this contract is a pictographic script tablet
which has all the elements of a futures contract. Beer production is
still being sold forward today, and other commodities surround our
daily experience. Consider the humble cup of coﬀee; to produce it
requires ﬁve futures contracts: coﬀee, sugar, lumber (for the stirring
stick), crude oil (for the Styrofoam cup or plastic stirring stick), and
milk. If one uses powdered creamer, one also needs various other
chemicals and industrial products, which trade futures but in the
OTC markets.
Organized futures exchanges were observed in history beginning
in 1570. This is when forward contracts began trading on London’s
Royal Exchange. Stock options were traded on London joint stock
companies and government gilts (“stocks”) as early as 1690. Most
of the U.S. commodity exchanges were established in the mid-19th
century, with new ones emerging and mergers/consolidations occurring ever since. The economic raison d’ˆetre for futures contracts is to
oﬀset commodity price risk from commercial operators to speculators
who are willing and able to assume the market price risk. Organized
exchanges permitted the standardization of forward contracts which
allowed producers, users, and speculators much improved access to
markets and pricing transparency to the underlying values.
Futures contract speciﬁcations include the contract size, product
description, pricing unit, tick size (minimum ﬂuctuation), daily price
limits, trading hours, contract months (e.g., Mar, Jun, Sep, Dec),
settlement procedure (cash or physical delivery), position limits and
ticker symbols. For example, one can trade rainfall index futures
and options on the Chicago Mercantile Exchange (CME), which are
contracts on inches of rainfall for 10 U.S. cities. The contract size
is $500 times the respective CME rainfall index; the pricing unit is
--- page 387 ---

364
Quantitative Financial Analytics
$1 per index point (1 point = 1 inch of rainfall); there are no price
limits; settlement procedure is by cash (we do not have to deliver
rainfall); contract months are Mar, Apr, May, Jun, Jul, Aug, Sep,
Oct. Trading is done by the automated trading system GLOBEX,
with a daily rest period of 3:15–5:00 p.m. Options on the rainfall
contract are traded by open outcry in the pits, Monday through
Friday, 8:30 a.m.–3:15 p.m.
Although traditionally the exchanges were established to facilitate trade in the agricultural commodities, today there is much wider
variety of tradable products. A sample of these futures products
include interest rates, equities, commodities, foreign exchange rates,
weather products, real estate products (S&P/Case-Shiller Home
Price Index), and alternative investments, along with associated
options. Trading in futures can be a highly sophisticated venture,
especially if one wishes to become a clearing member or engage in a
seat on one of the exchanges. Clearly, commercial users would like to
lock in supply or a future sales price for their commodities. But it is
the allure to the speculator which keeps the market ineﬃciency holes
ﬁlled in. One could open a miniscule account at a futures brokerage
(say $5,000) and begin trading crude oil, for example.
The exchanges also establish margin requirements to trade the
products, and the brokers have their margin requirements as well.
Futures margins are not like stock margin accounts, which are
really loans of cash to the account holder by the brokerage (called
“call money” in the past); futures margins are actually performance
bonds deposited by the trader, and proﬁts and losses are markedto-market (MTM) each day with a corresponding debit or credit
of cash to the account. For example, the Crude Oil West Texas
Intermediate contract trades for all months on CME/New York
Mercantile Exchange (NYMEX), with a trading unit of 1,000 bbl
(42,000 gallons), and physical delivery. The settlement type is important, many ﬁnancial products are cash-settled, but many commodity
contracts are still settled physically, in this case, one would need to
provide 42,000 gallons of crude oil to the designated delivery point.
Price adjustments can be made for other types of oil besides WTI. At
a time when the price of crude oil is $100, a typical trading margin
--- page 388 ---

Futures and Options
365
is $3,400. So if we are long one contract and the price of oil goes
up by $1/bbl, we have made $1,000, a 20 percent return on our
“investment” (margin). This is tempting to the speculator. Note that
this $3,400 performance bond is 3.4 percent of the 1,000 bbl contract,
indicating a leverage of over 9:1 on the asset.
After the initial margin has been deposited with the broker, a
“maintenance” level must be maintained before additional margin is
required. For example, the initial/maintenance margin for gold might
be $4,400/$4,000. Hence, a long gold contract can sustain a $4 drop
in the price of gold before additional margin must be provided.
Some authors quote an inﬁnite return in this case since “futures
do not involve an exchange of funds” at inception. Although this is
true, there is a deﬁnite opportunity cost of having one’s funds tied
up in margin in order to trade futures. For example, to trade a single
S&P 500 index futures contract requires a margin in 2014 of $24,000.
With a point size of $250 per S&P 500 index point, this represents
only a 1.04 percent return; however, 10 points returns $2,500, or
10.4 percent. We prefer to and will henceforth use the real-world
calculations. On the other hand, if oil drops $5/bbl in a day, then
the trader will receive a margin call to deposit more money into the
account. Brokers do not think lightly about margin calls, they will
close the account’s positions, at a loss sometimes, and they can still
demand more money. If there are several positions in the account,
proﬁtable ones will be closed out ﬁrst as well as the losing ones;
the trader sometimes has no control. Caveat emptor! The salient
elements of futures contracts are the contract symbol, the trading
(expiration) month, and the contract volume and open interest (see
Figure 8.1).
The contract months are designated using the symbols:
F
G
H
J
K
M
N
Q
U
V
X
Z
Ja
Fb
Mr
Ap
Ma
Je
Jl
Ag
Se
Oc
Nv
Dc
Futures volume is quoted with the previous day’s volume and
open interest unless a real-time screen is available. It is evident that
trading volume drops oﬀfor the further out months; the highest
volume is for the “spot” month, in this case the February contract
--- page 389 ---

366
Quantitative Financial Analytics
Low
Prev.
Settle
5375
CASH
-3
5375
5375
5378
0
0
5372
Prev.
Prev.
Volume Open Int.
-5
5387
CLG17
5409
5341
5377
360194
457983
5466
5481
-6
CLH17
5502
5437
5472
Crude Oil WTI
Daily Prices As of :- Monday, 2 January, 2017
Symbol:CL
Contract Close
Change Open
High
128316
327402
5543
-6
5553
CLJ17
5578
5517
5549
59365
150761
5605
-6
5633
CLK17
5638
5581
5611
32881
113161
5649
-6
5668
CLM17
5684
5624
5655
41040
227315
5676
-6
5702
CLN17
5704
5656
5682
17697
51573
5690
-6
5695
CLQ17
5719
5669
5696
9163
49607
5699
-5
5720
CLU17
5728
5680
5704
11939
73010
5703
-5
5722
CLV17
5728
5681
5708
5212
40632
5705
-5
5716
CLX17
5730
5692
5710
4372
37511
5706
-5
5709
CLZ17
5736
5679
5711
23949
207020
5699
-4
5718
CLF18
5718
5690
5703
1832
36928
5691
-4
CLG18
5691
5691
5695
448
14962
5682
-4
CLH18
5682
5682
5686
1035
23529
5673
-3
CLJ18
5673
5673
5676
286
7153
5664
-3
CLK18
5664
5664
5667
191
5415
5659
-2
5669
CLM18
5679
5631
5661
4072
57326
5650
-2
CLN18
5650
5650
5652
467
4878
Figure 8.1. Crude Oil Futures Quotes, January 2, 2017 (Source: Barchart.com,
Chicago, IL)
(CLG17). For a less-actively traded product, this front-month volume
drop-oﬀis very clearly seen.
Investing in futures and options is an oxymoron since all
derivatives contracts have varying active months and ﬁxed expiration
dates; most “investing” is therefore in fact trading. Professional
futures traders use a combination of fundamental and technical
analysis techniques. Fundamental analysis includes research into
the factors aﬀecting (worldwide) supply and demand, since indeed,
price is supposed to be at the intersection of supply and demand.
Typical factors in an agricultural commodity trader’s analysis include
--- page 390 ---

Futures and Options
367
expected harvest, yield per acre, the status of stored supply, weather,
global climate change, and even includes the political sphere (e.g.,
corn and fuels). Econometric models of commodity prices are quite
complex, all of these factors and more go into cattle prices, for
example, as well as do current (worldwide) trends in dining.
Other fundamental techniques include seasonality studies, such
as those for July lean hogs, the prices tend to be a minimum in
August and steadily climb to a peak in the following month of
May. Actual trading results over 15 years for a strategy such as
“Buying August lean hogs on Feb 12 and sell May 1 results in proﬁts
over 80 percent of the time.” There are many seasonal strategies
which have seen 100 percent proﬁtable results.
Another fundamental technique is to trade spreads. These positions are the result of buying one contract and selling another related
future. It is believed that although prices may not be predictable,
the spread between either calendar contracts or related commodity
contracts is more predictable. Much research has borne this out.
A typical example might be buy Jul lean hogs and sell Jun lean
hogs on March 9 and hold until May 8; this strategy has been
successful in 100 percent of the cases from 1993 to 2008. (See CME
Group Commodity Products. 2008 Moore Research Report, Pork.
Chicago, IL).
Rober Robens (see Williams and Noseworthy, 1987) summarizes
these concepts as follows:
“Seasonal price movements are a function of ‘normal’ market
conditions and relationships that economists and analysts often
rely upon for recommendations and projections. For seasonals to
be reliable it is important to identify the signiﬁcant variables that
are the primary motivating forces for change. In commodities,
these variables often center around crop production and harvest
considerations, free stocks and inventories, domestic consumption
and export demand.
“Spreads are simply price relationships which exist in change
between commodities futures contract months of between diﬀerent
commodities. These price relationships often have characteristic
behavioral patterns resulting from certain repeated fundamental
considerations.”
--- page 391 ---

368
Quantitative Financial Analytics
Because of the temporal nature of the futures asset, and the time
it takes for market fundamentals to change (hopefully in the direction
of the analyst’s belief), futures and options are most often traded
using technical analysis, which we discuss in more detail later in this
book. Technical analysis comprises a vast toolkit of market price and
volume indicators in order to give position entry and exit guidance.
These tools range from simple moving averages, to visual behavioral
patterns, to sophisticated statistical calculations. Academic research
holds that all such techniques have no value; operationally, even
the purely fundamental futures traders use a collection of technical
indicators to inform their positions.
The most successful class of futures operator is the commercial
class. They are the ones who have a need for 112,000 pounds of (nondomestic) sugar at 13c per pound. The second most successful class
of futures trader is the broker and managed funds class. Another
successful group is the authors who make their income from selling
books, newsletters, and seminars on trading. It is considered unusual
for an individual small commodity speculator to survive more than
ﬁve years in the markets.
Warrants
A common stock warrant is simply a legal instrument issued by
a corporation that grants the holder the right to purchase the
common stock of the corporation at a stated price within a stated
period of time. Thus, there are three basic elements to the common
stock warrant. The ﬁrst of these, the privilege of exchange, is the
most essential element. This privilege usually entitles the holder
to exchange the warrant for common stock, on the basis of one
warrant for one share of stock, although multiple or fractional shares
are sometimes speciﬁed. The second, the stated price of exchange
or option price, is the price for common above which the warrant
becomes mathematically valuable. This option price may be ﬁxed
over the life of the warrant or may change, usually rising as the age
of the warrant increases. The ﬁnal element, the stated period of time,
is the duration of the life of the warrant. This period may vary from
a few days to perpetuity.
--- page 392 ---

Futures and Options
369
Prior to the introduction of exchange-traded stock options in
1973, a healthy market in warrant trading was oﬀered by the
major stock exchanges (NYSE, AMEX, NASDAQ, TSX), covering
companies such as AT&T, Ford Motor Company, AIG, General
Motors, etc. Warrants were a major source of speculative leverage.
Since then, the market has thinned considerably, with warrants
trading mostly on smaller issues. According to the advisory service
http://commonstockwarrants.com, as of January 2017, there were
183 publicly traded warrants on 164 U.S. and Canadian companies;
this compares to approximately 12,000 options traded on 3,817 US
companies. Due to the thin nature of the warrants markets, there are
usually large spreads between the bid and ask prices. Listed stock
options on the other hand trade on the organized options exchanges,
such as the Chicago Board Options Exchange (CBOE) and several
others. This is one diﬀerence between warrants and exchange-traded
options. The other main distinction is the availability of longer
expiration horizons, as opposed to a maximum of 3 years with options
on a smaller sampling of stocks. Yet another diﬀerence is that the
number of outstanding warrants is limited by their oﬀering and
cannot be increased; but, option open interest can be increased any
time two parties wish to create another contract.
An example will illustrate these three elements. Suppose ABC
Co. has an issue of 33/4 perpetuals that have been outstanding for
quite some time. Each warrant of this issue is exchangeable for one
share of common stock at $3.75 for the remainder of the life of the
company. Thus, when the price of ABC common advances beyond
33/4, the warrant assumes a mathematical value. This mathematical
value is precisely the diﬀerence between the price of the stock
and $3.75.
In 1942, the common stock warrants of RKO were selling for
$0.0625 each. Four years later, they were selling for $13, representing
a 208-fold increase. In 1948, Hoﬀman Radio warrants were priced
at a nickel apiece. Two years later, they sold as high as $25 each —
a 500-fold increase. Universal Picture warrants sold at $39 in 1945,
but by 1947, they had fallen to $1.50. Between August 1956 and
December 1959, General Tire common advanced from $50 to $280
--- page 393 ---

370
Quantitative Financial Analytics
(adjusted) — a 460 percent increase. The General Tire $60 warrants
went from $7.25 to $215, however, in the same span — a 2,865 percent
increase. More spectacularly, the $70 warrants went from $4.50 to
$205, for a 4,455 percent increase. The most dramatic performance
in the history of common stock warrants was the 123,077 percent
increase in the price of Tri-Continental warrants witnessed from 1942
to 1962. Although most of the trading activity today is in options on
common stocks and futures, the analysis is similar.
Common stock warrants may come into being in various ways.
The most typical of these include the following:
1. Through the sale of common stock and the warrants together as
a unit.
2. Through exchange as a result of a reorganization.
3. Through sale to underwriters at a nominal price — part of their
actual compensation.
4. Through separate public sale (rare).
5. Through attachment as a bonus to senior securities or preferred
stock.
The way a warrant comes into being may give some indication
as to the future performance of the common stock of the company
in question and, consequently, to the future value of the warrant.
Warrants that result from bankruptcy reorganizations, where stockholders and other junior-security holders are given warrants in the
reorganized company for their old securities, may be suspect. The
fact that the company had to be reorganized might give some
indication as to the future uncertainty for the common and hence
the warrant. Although amazing comebacks in such cases have been
witnessed (for example, the St. Louis Southwestern R.R. many years
ago), during the period after reorganization warrants tend to be
depressed.
When warrants are used as a partial compensation for investment
bankers or as a “sweetener” for other issues, no indication is given
about the future performance of the warrant. Many well-established
ﬁrms employ the second of these practices, and on occasion, both
are employed by established ﬁrms. The use of the warrant as a
--- page 394 ---

Futures and Options
371
sweetener for the sale of another issue, particularly debentures or
other forms of bond issue, is an alternative to issuing a convertible
security. Several advantages exist for the purchaser of the senior
security with warrants attached over the senior issue convertible into
common stock. First, the holder has the option of selling the warrant
and retaining the original issue. The convertible holder obviously
cannot do this. Second, the life of the warrant cannot be reduced or
terminated at the option of the company, whereas many convertible
issues are callable after a period of time. Finally, because of the
speculative attractiveness attaching to warrants alone they usually
command a greater premium in the market over their realizable value
than would a comparable convertible issue.
Determining the worth of a warrant would be a simple matter
if warrants sold at their mathematical value. Because there is value
associated with the option element of a warrant, however, warrants
generally sell above their mathematical worth. There is a tendency for
the actual price of a warrant to approach its mathematical value as
the price of the common stock rises signiﬁcantly beyond the exercise
price, however. The determinants of the price of a warrant are:
Pw = f(Po, Tn, Pc, Di, Fc),
(8.1)
where:
Pw = market price of the warrant
Po = option or exercise price of the common
Tn = duration of the issue, that is, time remaining before
expiration
Pc = current price of the common
Di = potential dilution, that is, ratio of the number of warrants
outstanding to the number of common shares outstanding
Fc = the future common stock price
From the discussion above, we may observe that Po and Pc have
a deﬁnite quantiﬁable relationship to the value of the warrant. These
two variables determine the mathematical value of the warrant, which
may be expressed as follows:
V = (Pc −Po)N,
(8.2)
--- page 395 ---

372
Quantitative Financial Analytics
where:
V is the mathematical value of the warrant
N is the number of shares that may be purchased with one warrant
Pc and Po are as in Equation (8.1)
To consider a simple example, if the stock of the XYZ Co.
were currently selling in the market place at $25 per share, and
each warrant allowed the purchase of one share of common stock
at $15 per share, the mathematical value of the XYZ Co. warrants
would be $10 per warrant.
The variables Tn, Di, and Fc determine the premium that one
would be willing to pay above the pure mathematical value of the
warrant. Tn suggests something quite important regarding the nature
of a stock warrant: a warrant is really nothing more than a longterm option enabling its owner to obtain the common stock at a
ﬁxed price in the future. Obviously, this option has a value that
exists even when the common stock is selling substantially below the
option price. This is true because the stock might rise above the
option price at some point during the life of the warrant. The value
related to the variable Tn might appear to be intuitively obvious:
the longer the time remaining in the life of the warrant, the more
valuable the option privilege becomes. Unfortunately, the empirical
relationship is not so easily discerned. Attempts to quantify the
eﬀects of longevity on the value of the warrant have produced some
evidence to suggest that this variable becomes important only as
the warrant approaches expiration. It has also been observed that
maturity diﬀerences are not important beyond a speciﬁc number of
years. It may be argued, however, that although isolated empirical
investigations have found a truncation eﬀect, there are no theoretical
grounds for such a phenomenon. This view is adopted by many
ﬁnancial economists, who maintain that warrants often expire with
the price of the common below the option price, although given
more time the common could rise to produce a mathematical value
for the warrant. Given two price relatives, common price to option
price and warrant price to option price, empirical data are ﬁtted
to functions of the form Y = aXb, and a graphical representation
--- page 396 ---

Futures and Options
373
similar to Figure 8.1 is depicted. In this diagram, the warrant price
relative (Pw/Po) is the dependent (Y ) variable, and the commonstock price relative (Pc/Po) is the independent (X) variable. The
maximum relative is given where (Pw/Po) = (Pc/Po). Values where
(Pw/Po) > (Pc/Po) are not possible, because this would imply
Pw > P (that is, the warrant price exceeded the common stock price).
The minimum relative is given where [(Pc/Po) −1] = [(Pw/Po)].
Values where [(Pc/Po) −1] > [(Pw/Po)] imply (Pc −Po) > Pw.
This condition is not possible because if the mathematical value of
the warrant exceeded its market price, arbitragers would buy the
warrant, exercise it, and sell the common until (Pc −Po) = Pw.
Possible relatives are given by functions A, B, and C. These
functions represent warrants of speciﬁc maturity categories with
increasing slopes corresponding to longer maturities. Thus, if function A were the ﬁt of warrants with maturities of one year or less
and B were the ﬁt of warrants with maturities of one to two years,
the latter group would command a larger premium than the former.
A
B
PW /PO
Maximum
Value
Minimum
Value
1.3
1.0
0.9
0.8
0.7
0.6
0.5
0.4
0.3
0.2
0
0.1
C
0.1
0.2
0.3
0.4 0.5
0.6
0.7 0.8
0.9
1.0 1.1
1.2
PC /PO
Figure 8.2. Warrant Longevity Value Model
--- page 397 ---

374
Quantitative Financial Analytics
Symbolically,
Pw(B)/Po(B)
Pc(B)/Po(B)
> Pw(A)/Po(A)
Pc(A)/Po(A)
,
thus:
Pw(B)/Pc(B) > Pw(A)/Pc(A).
This sort of relationship has been observed empirically where
the functional relationship ranged from Y
= 0.2753(X)1.8545 for
warrants of six-month to one-year maturities to Y = 0.5509(X)1.2155
for perpetual warrants. The R2 exceeds 0.94 for four of six functions,
indicating an excellent empirical ﬁt.
The second of the key variables in the determination of the value
of the premium applied to a given warrant issue is Di, the potential
dilution of earnings and dividends resulting from the exercise of
warrants after the option price is reached. Because common stock
warrants do not receive dividends, holders of warrants may elect
to exercise their option to buy common stock in order to enjoy
the income from dividends that the common pays. This, of course,
assumes that the common stock is paid a dividend, and many of the
companies that issue common-stock warrants do not pay dividends.
It also assumes that the premium has become insigniﬁcant relative
to the dividends that are paid. Thus, if XYZ common is selling at
$25 per share, its outstanding warrants are selling at $10.25, and the
exercise price is $15, some holders would exercise the purchase option
if the dividend were large enough. The fact that additional shares are
issued at less than the market price per share may produce a longrun dilution in earnings per share. This would occur if the present
value of earnings generated from plant and equipment purchased
with the funds obtained from the sale of new shares to warrant
holders were less than the price paid by warrant holders for their
shares. A dilution in long-run earnings would aﬀect the market price
of the common stock and hence the value of the warrant. In this
instance, the presence of a substantial volume of warrants might
serve to depress the market price per warrant.
--- page 398 ---

Futures and Options
375
It can be argued in this case that exercise would not take place
because the rational holder of the warrants would simply sell at the
market price of $10.25 and buy the common at $25, for a cost of
$14.75 per share, a price lower than the $15 option price. This would
indeed be true if it were not for the “turn of the market” (brokerage
commissions, taxes, and so on). In this example, if the “turn” were
larger than the $0.25 diﬀerential, the option to purchase at $15 would
be exercised. Thus, if the diﬀerential, which is actually the premium,
is less than the turn, exercise may occur. If it is larger than the turn,
exercise will not occur.
All this assumes, of course, that the extra dividends received from
holding common are more valuable to the holder than the prospective
return from holding the warrant. In the above case, if the common
rose in price by 20 percent (from 25 to 30), the warrant would have
to rise to at least 15 (the mathematical value of the warrant), which
is almost a 50 percent increase. Thus, the speculator who expected
higher prices for XYZ common would probably prefer to hold the
warrant regardless of the XYZ dividend. This illustrates the major
attraction of warrants to the risk-seeking investor. Price movements
for warrants are generally magniﬁed in percentage terms from a given
change in the price of common. The phenomenon operates both
positively and negatively. If XYZ fell by 20 percent, from 25 to 20, the
warrant could fall by as much as 50 percent because the mathematical
value of the warrant would now be only 5. Even if a larger premium
developed at the lower warrant price, which frequently happens, the
percentage decline in the price of the warrant would be magniﬁed.
There is empirical evidence to demonstrate that ﬁrms with
the high dividend payouts tend to have slower rates of earnings
growth. This retardation of earnings growth may tend to reduce
the attractiveness of warrants that may be exercised for high-yield
common stocks. The negative impact of high cash payouts on warrant
values has been recognized in studies that have found dividend yields
to have a negative regression coeﬃcient, with higher yields indicating
lower warrant values.
The ﬁnal key variable in the determination of the value of the
premium to be applied to a given issue of common-stock warrants is
--- page 399 ---

376
Quantitative Financial Analytics
Fc, the future price of the common stock. In many ways, this variable
is the most important one for the determination of the value of the
warrant, and undoubtedly it is the most diﬃcult to handle. The ideal
way of approaching this variable is to follow the procedures indicated
previously for analyzing a common share. The important factors
here are the expected future earnings of the company, the expected
future dividends, and the expected future multiplier to apply to the
earnings of the company per common share when the stock is to
be sold. The analysis proceeds in the manner described earlier in
this book.
Suppose an analyst has forecasted the following earnings-pershare pattern for the Keystone Corp. for the next ﬁve years:
2014
$1.00
2015
$1.20
2016
$1.50
2017
$2.00
2018
$2.50
The analyst expects an earnings multiple of 20 to hold in 2018,
and he believes the ﬁrm will maintain a dividend payout of about
50 percent over the period. Keystone common sells at 261/4. If a
purchase were made at the beginning of 2014 for holding until 2018,
the following return would be expected:
2014
2015
2016
2017
2018
Dividends per
share (DPS)
$0.50
$0.60
$0.75
$1.00
$1.25
Market price at
terminal date
20 × 2.50 = 50.00
Dollar returns
$0.50
$0.60
$0.75
$1.00
$51.25
@ 16 percent
0.826
0.743
0.641
0.552
0.476
Annual present
value
$0.41
$0.45
$0.48
$0.55
$24.40
Total present value = $26.29.
--- page 400 ---

Futures and Options
377
Thus, if the stock were purchased at $26.25, a return of about
16 percent could be earned.
Keystone Corp. also has a set of warrants expiring in 2020. The
warrants give the holder the right to buy one share of common for
each warrant held at a price of $30 per share. The mathematical
value of the warrant currently is:
V = (Pc −Po)N
= ($26.25 −$30.00)(1)
= −$3.75.
although the warrant sells in the market for $5. Thus, investors
are paying a premium of $8.75 over the mathematical value of
the warrant. Investors evidently feel that the future prospects for
Keystone are suﬃciently bright to produce a stock price substantially
above the exercise price during the life of the warrant. Is this
optimism justiﬁable?
To answer this, we may determine the price of Keystone warrants
in 2018, given the above assumptions. If there were no premium
existing then, the warrant price would be:
Pw −V = 0
Pw = V = (Pc −Po)N
Pw = (50 −30)1 = $20.
and it could be higher if a premium continued. An investor who
bought the warrant would have an expected return of at least:
(X)($20) = $5
X = 0.25.
At 32 percent, a dollar received ﬁve years hence is worth $0.25 today.
Thus, the expected return would be about 32 percent. This compares
with an expected return of only 16 percent for the common.
