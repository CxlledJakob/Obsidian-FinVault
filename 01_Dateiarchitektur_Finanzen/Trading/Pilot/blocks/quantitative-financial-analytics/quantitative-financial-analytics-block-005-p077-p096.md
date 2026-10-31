# Quantitative financial analytics_ the path to investment profits.pdf — pages 77–96

--- page 77 ---

54
Quantitative Financial Analytics
SO
SO
RT= ST
SO
RT
ST
ST
ST
t=T
R
1
0
-1
0
0
r%
r
‘
θ1
θ2

 in (-90,90)
Figure 2.1. Geographical Relationship of Returns
SO=1
SO=1
1.3167
1
RT=πRi=
1.0712        1.0712        1.0712        1.0712
1.1
1.05
1.2
.95
1                   2                   3                    4
1                   2                   3                    4
1.3167
1.3167
R = 1.3167¼ = 1.071
R = 1.075 (7.5%)
1.0754=1.3354
Figure 2.2. Equivalent Terminal Values
This symmetry is easily explained as ln(1/R) = ln R−1 = −ln R.
Again considering t = T, and RT = ST /S0, the returns can be
diagrammed as shown in Figure 2.1 (assuming S0 = 1).
The resulting reconstitution of the terminal values is illustrated
in Figure 2.2.
Although log returns are mathematically useful and interesting,
their use is not as widespread in ﬁnance as are percent returns.
We argue that percent returns of 10,500 percent are cognitively
meaningless and that another approach should be used. Note from
Table 2.3 that for any given year, there are a large number of stocks
--- page 78 ---

Financial Mathematics
55
Table 2.3. 1-year Extreme Returnsa
Worse Returns
Better Returns
Date
Total
Returns
Num
Percent
Returns
Num
Percent
Jan-85
230
−50%
4
1.70
100%
10
4.30
−75
1
0.40
200
3
1.30
−90
1
0.40
300
1
0.40
−99
0
0
500
0
0
Jan-87
466
−50%
17
3.65
100%
8
1.72
−75
5
1.07
200
0
0
−90
1
0.21
300
0
0
−99
0
0
500
0
0
Jan-99
4,096
−50%
378
9.20
100%
518
12.60
−75
88
2.10
200
223
5.40
−90
26
0.60
300
121
3.00
−99
4
0.10
500
61
1.50
Jan-01
4,186
−50%
577
13.80
100%
224
5.40
−75
205
4.90
200
66
1.60
−90
73
1.70
300
23
0.50
−99
24
0.60
500
7
0.20
Jan-05
4,787
−50%
277
5.80
100%
178
3.70
−75
53
1.10
200
25
0.50
−90
19
0.40
300
6
0.10
−99
3
0.10
500
1
0
Jan-08
5,050
−50%
2,080
41.19
100%
15
0.30
−75
783
15.50
200
2
0.04
−90
223
4.42
300
1
0.02
−99
18
0.36
500
0
0
Jan-10
4,641
−50%
133
2.90
100%
239
5.10
−75
33
0.70
200
32
0.70
−90
11
0.20
300
9
0.20
−99
2
0
500
0
0
aExtreme returns formed from January holdings for all U.S./Canadian stocks
exceeding marketcap and liquidity constraints.
whose 1-year returns exceed either a 100 percent gain or a 50 percent
loss. Other scalings are possible which have more intuitive appeal
than extreme percent units.
One such scaling is the “decibel” scale, indicated in the third
column in Table 2.4. This has been shown to be a natural scaling
--- page 79 ---

56
Quantitative Financial Analytics
Table 2.4. Presentation of Extreme Returns.
R
r (%)
Ln R
10 Log10R
101
10000
2.004
20.04
21
2000
1.322
13.22
10
900
1.000
10.00
6
500
0.778
7.78
5
400
0.699
6.99
4
300
0.602
6.02
3
200
0.477
4.77
2
100
0.301
3.01
1
0
0.000
0.00
0.50
−50
−0.301
−3.01
0.33
−67
−0.477
−4.77
0.25
−75
−0.602
−6.02
0.10
−90
−1.000
−10.00
0.05
−95
−1.301
−13.01
0.01
−99
−2.000
−20.00
when perceived by the human mind, although there are still surprises
with that. More work needs to be done in this area; a better scaling
is required in order to handle changes in the negative area, as well
as from negative to positive values, or from very small to moderate
values, etc.
Summary
There is nothing out of the ordinary in ﬁnancial mathematics not
encountered in usual practice, except for the following three axioms
which are generally not stated: the axioms of Value, Time, and of
the TVOM. Although the following concepts deliver the reader to a
mineﬁeld of philosophical considerations, we hope that he or she will
absorb the basic ideas and consult appropriate texts for the other
nuances which will arise.
A good part of ﬁnancial analysis depends upon calculations of
compound interest. This is because the time horizon in ﬁnance is
usually long, and so some method must be obtained to compare
ﬁnancial ﬂows over time. Because of the TVOM axiom, and the fact
that ﬁnancial ﬂows may be “invested” at some positive rate of
--- page 80 ---

Financial Mathematics
57
interest, a ﬂow received today is worth more than an equal ﬂow
received in the future. In most practical ﬁnance applications, semiquarterly, quarterly, or perhaps monthly compounding is typically
suﬃcient; continuous compounding is mostly used for approximating
and for mathematical and conceptual reasons. It is however widely
used in ﬁnancial engineering.
A PV is the value today of funds received in the future. It is, in
eﬀect, the reverse operation of a compounded sum. Thus, if we know
X dollars will be received n periods from now, and if we know the
rate of interest, we can determine the PV, Y , of that future sum.
Return on investment is one of the underpinnings of the investment paradigm. We have the expectation of a return in a reasonable
period of time, along with safety of that return, as well as safety of the
investment itself. Gross returns are also called total returns. Financial
returns can be considered a growth factor of an investment and are
quite similar to future value, depending on the compounding scheme.
While gross returns are quite useful, it is however completely natural
to want to have at our disposal measures of incremental return. We
examined the relative merits of 3 useful deﬁnitions of incremental
returns. Each one of them is applicable in individual periods, or
over an entire time horizon. These are absolute diﬀerences, relative
returns, and mathematical returns.
Problems
1. How much will $5,000 be worth in 10 years if the rate of
interest is 10 percent under conditions of annual compounding?
Quarterly compounding? Continuous compounding?
2. Let $250 be placed in a savings account that pays interest of 1
percent per quarter compounded quarterly. How much will it be
worth after 1 year (4 compounding periods)?
3. Plot the compound growth factor of $1 over 10-, 20-, and 50-year
periods for the interest rates r = (0.01, 0.02, 0.05, 10).
4. A savings account in Mexico pays interest of 12.5 percent
compounded annually. If $100,000 is put into this account today,
how much will be on deposit 20 years from now? (Solve through
--- page 81 ---

58
Quantitative Financial Analytics
interpolation and the use of common logarithms. Account for the
rather large diﬀerence in your results.)
5. Schmidt places $50 in the bank each quarter. His bank pays
interest quarterly at an annual rate of 4 percent. How much will
Schmidt have on deposit after three years?
6. Gormann puts $600 in a savings account each year. He is paid
interest of 6 percent per annum compounded annually. How much
will he have after 5 years?
7. A special depository account requires annual payments of $1,000.
After 8 years, the account matures and pays to the holder
$10,000. At what annual rate of interest do funds grow in this
account?
8. Determine the present value of $10,000 received in 20 years when
interest is compounded at 5 percent:
a. Annually
b. Continuously (Hint: 1/e ∼0.368)
9. Verify using an online data provider that the monthly and
daily returns for stock indexes such as the S&P 500, DJIA, or
NASDAQ provide the same 20-year CAGR.
10. Verify (prove) the rule-of-72: a rough translation of Pacioli’s
1494 summary goes something like, “In wanting to know of any
capital, at a given yearly percentage, in how many years it will
double adding the interest to the capital, keep as a rule [the
number] 72 in mind, which you will always divide by the interest,
and what results, in that many years it will be doubled.”
References
Rubinstein, M., A History of the Theory of Investments: My Annotated
Bibliography. Hoboken, NJ: John Wiley & Sons, 2006.
Ruppert, D., Statistics and Data Analysis for Financial Engineering.
New York, NY: Springer, 2011.
Vecer, J., Stochastic Finance: A Numeraire Approach. Boca Raton, FL:
Chapman and Hall/CRC, 2011.
--- page 82 ---

Chapter 3
The Securities Markets and
Macroeconomics
This [ﬁnancial] crisis . . . has turned out to be much
broader than anything I could have imagined . . .
Alan Greenspan, October 23, 2008
The Securities Markets
Negotiable ﬁnancial assets are traded in the money and capital
markets. The distinction between the two is based upon the maturity
of the ﬁnancial asset under consideration. The money market is generally deﬁned as consisting of negotiable securities with a maturity of
one year or less; the capital market is composed of the longer-term
securities (including equities, which have a theoretically perpetual
life). The distinction, however, is generally more signiﬁcant than the
mere artiﬁcial division at the one-year maturity level.
The instruments of the money market, aside from being less than
a year in maturity, are also generally of high investment quality and
are purchased as a means of obtaining some return on temporarily
idle funds; in other words, the money market is a market in nearmoney instruments where safety of principal and liquidity are the
primary considerations.
The capital market, on the other hand, not only includes
securities of all degrees of risk but also tends to be utilized by
investors with funds to be committed for substantial periods. Finally,
long-term debt securities constitute a portion of the capital market
at the time of their issuance, but as they approach maturity they
59
--- page 83 ---

60
Quantitative Financial Analytics
become money-market instruments. We shall begin the discussion
with the more traditional money-market instruments, which, in the
context of this book, may be viewed as possible interest-earning cash
substitutes in the investment portfolio.
Securities of the U.S. government
The U.S. treasury bill is one of the most signiﬁcant money market
instruments. This short-term U.S. government obligation is oﬀered
in 28-, 91-, and 182-day maturities. Bills do not carry an interest
coupon but are sold at less than their face value. Because of the
large amount of bills outstanding, the narrow spreads between bid
and asked prices, and the lack of credit risk, treasury bills are
viewed as very desirable liquidity instruments. Bills of nineand
twelve-month maturity are also oﬀered. Some of the government
agencies discussed below issue short-term debt as well that would
qualify as money market instruments. Also, as mentioned before, the
longer-term government and agency securities become money-market
instruments when they approach maturity.
Suppose that an investor desired to ﬁnd the price and yield on
a treasury bill due in 300 days on a 3 percent basis. Since treasury
bills are quoted on a “discount” basis, the price would be:
3% × (300/360) = 2.5% “discount.”
Price = $975 per $1,000 face value of the bill, and the approximate
true rate would be:
(25/975) × (365/300) = 3.12%.
The latter is an approximation because it assumes annual compounding. The government has devised a more complicated computation for equivalent bond yield assuming semiannual compounding.
Bill rates are quoted every business day in the ﬁnancial press and
online so it is not even necessary to make speciﬁc calculations. Since
1926, the average 30-day bill has yielded about 3 percent. After the
2007 collapse, the Federal Reserve Board (see discussion below) has
maintained a policy of keeping rates at extremely low levels. Indeed,
--- page 84 ---

The Securities Markets and Macroeconomics
61
30-day bills have regularly yielded only a few basis points (a basis
point is 1/100 of 1 percent). In fact, yields actually went negative for
a few days, meaning that investors were willing to pay Uncle Sam
for the privilege of lending him money!
Because we shall continually refer to U.S. federal government
securities as devoid of credit (default) risk, we shall explain this point.
It does not mean that we feel an entity with almost $20 trillion in
debt (with additional unfunded liabilities such as Social Security and
Medicare) is a great credit risk by normal standards of evaluation.
What it does mean is that, because the government has the power
of money creation, it would undoubtedly create enough new money
to repay any bondholder who demanded redemption. Only events
like war, revolution, or, by some deﬁnitions, hyperinﬂation, could
prevent this and would cause all other dollar-denominated obligations
to become worthless anyway.
It is interesting to note that in 2012, one might obtain a yield
of only, say, 20 basis points on a treasury bill. This means that
a purchaser of $100,000 in bills would have earned just $200 over
the span of a year. If that investor paid federal income taxes of
36 percent, he or she would have a net after-tax return of only $128
(or 0.128 percent). The inﬂation rate has been above 2.50 percent
recently, meaning that an investor in treasury bills has actually lost
about 2.37 percent on an annualized basis. Why would intelligent
investors accept such miserable returns? Part of the answer to this
question will be revealed later in this chapter.
Municipal securities
Securities issued by states and their political subdivisions are
usually known by the broad term municipals or “Munis” and are
distinguished by the fact that their interest is, in most cases, exempt
from federal income taxes. Although municipals are generally long
term in maturity and are considered later in the chapter, certain
situations give rise to short-term obligations. A city or state may
borrow in anticipation of tax receipts or the proceeds of a bond issue.
A municipal bond issue itself may have a portion that matures within
a year and thus might qualify as a money-market instrument. The
--- page 85 ---

62
Quantitative Financial Analytics
quality of these issues can vary widely, and the ratings (see discussion
below) on the bonds of the issuing entity will give some indication
of credit-worthiness. Only the issues of bodies having one of the
top two or three bond ratings would be of suﬃciently high quality
to be considered a true money-market instrument. The short-term
municipal market is also fed by the interim ﬁnancing needs of various
housing and renewal authorities. The notes of state and local housing
authorities are generally treated as obligations of the appropriate
government body, and their quality is judged accordingly.
An additional advantage of municipals is that they are also
usually exempt from state taxes in the state of issuance. A disadvantage is that the issues may be small, thus the secondary
markets are often rather illiquid. To illustrate the tax eﬀect of
municipals, consider the Treasury bill analyzed above. Its yield was
only 0.20 percent, or 0.128 percent after-tax. Thus, if an otherwise
similar municipal security oﬀered a return in excess of 0.128 percent,
the after-tax return to the holder would be more attractive. Since
many munis are below the credit-worthiness of the U.S. government
(California cannot print money but Uncle Sam can), these instruments often have to yield more, say somewhere between 0.128 and
0.20 percent.
Bankers’ acceptances
A bankers’ acceptance arises from a commercial transaction, often
involving international trade. An American importer may send a
letter of credit with an order for goods to a foreign exporter. The
exporter may then draw a time draft (an order to pay in the future)
against the importer and sell it to his local bank at a discount in order
to receive immediate payment. The foreign bank will then send the
draft and title to the goods to the importer’s bank. The importer’s
bank accepts the draft by indicating that it will guarantee payment.
The time draft is now a bankers’ acceptance that is sold in the money
market to pay the foreign bank. Because the bank is obligated on
the instrument, acceptances tend to trade on the basis of the bank’s
credit rather than that of the company primarily obligated. In a very
crude sense, an acceptance may be viewed as a postdated certiﬁed
--- page 86 ---

The Securities Markets and Macroeconomics
63
check sold at a discount. Most large banks and bond dealers carry a
wide range of sizes and maturities in acceptances, although it may
not be possible to match desires exactly.
Negotiable certiﬁcates of deposit and commercial paper
Negotiable Certiﬁcates of Deposit (CDs) are claims upon time
deposits at banks that may be sold prior to the maturity of the
deposit. The deposit itself is made for a speciﬁed period (at a rate
tied to the maturity) and may not be withdrawn early. The ability to
negotiate the ownership of the deposit, however, provides essentially
the same liquidity beneﬁts as withdrawal to the owner and allows the
higher rates associated with longer-term deposits to be earned. These
deposits are backed by the Federal Deposit Insurance Corporation
(FDIC) to $250,000; but because negotiable CDs are rarely smaller
than multiples of $1 million, this is little comfort. Beyond FDIC
insurance, the only security is the size and quality of the issuing
bank. As a result, only the CDs of the larger money-market banks
really qualify as money-market instruments.
The commercial paper market consists of the short-term, unsecured promissory notes of industrial and ﬁnancial companies.
Directly placed paper is that sold directly by the borrower to the
lender. Sales ﬁnance and consumer ﬁnance companies are the major
sellers of directly placed paper, using the proceeds to carry the
inventory of dealer and consumer loans they hold. Directly placed
paper is generally sold to mature on any day desired by the lender
from 3 to 270 days hence (an obvious advantage if the lenders
know exactly when they want their money back). A disadvantage of
directly placed paper is that there is no secondary market, although
in cases of hardship the issuer may buy it back early.
Dealer-placed commercial paper is sold in the form of a onetime issue through a bond dealer. Finance companies also use this
approach, and industrial companies employ it for seasonal working
capital needs or as an alternative to bank borrowing. In all cases,
and especially with dealer-placed paper, the issuer will be required
to keep open bank lines of credit to secure the retirement of the issue.
--- page 87 ---

64
Quantitative Financial Analytics
Eurodollars and non-U.S. money-market instruments
From the lender’s point of view, the Eurodollar market merely
presents the opportunity to buy negotiable CDs, expressed in dollars,
from non-U.S. banks (either foreign banks or foreign branches of U.S.
banks). A major disadvantage of this form of short-term investment is
that the regulation, disclosure, and deposit insurance in this market
leave much to be desired, so the possibility of a panic or default
cannot be ignored. This possibility is enhanced by the fact that the
bank of deposit is creating a liability in a currency (the dollar) that its
own government is under no obligation to provide in times of crisis.
In theory, there is no reason why an American investor should not
consider the liquidity instruments of any major foreign country if the
credit standing is adequate. To minimize the risk of the transaction,
however, it is necessary to “cover” it in the forward exchange market
(which merely involves reaching an agreement in the present as to
the price at which one will buy or sell an amount of foreign money
at some point in the future).
To illustrate covered arbitrage, suppose that the NKV Trust
wished to buy $1 million of 10 percent, 180-day securities of the
Dak government. The Dak currency is currently exchanging at 30 to
the dollar. The 180-day forward Dak is quoted at 31 to the dollar (the
rate at which it would be possible to contract now for delivery in six
months). The return to be earned by NKV on a covered transaction
would be given as follows:
Now:
(a) Sell $1M to obtain Dak (@30:1) = 30M Dak
(b) Buy 30M Dak securities (will earn interest of
1.5M Dak)
(c) Sell 31.5M Dak for delivery in 180 days against
the dollar (@31:1)
In 6 months:
(a) Redeem bonds = 31.5M Dak
(b) Deliver on forward contract
(31.5M/31) = $1,016,130
Return =
$16,130
$1,000,000 × 360
180 ≈3.2%.
--- page 88 ---

The Securities Markets and Macroeconomics
65
The Capital Market
The capital market may be distinguished from the money market
in several ways. The securities involved are far more numerous and
varied. The markets themselves generally lack the breadth and depth
of the money market in the technical sense that the spread between
bid and asked prices is greater and the change in price on consecutive
transactions is also generally greater. Finally, the capital market is
regulated by the government (primarily through the Securities and
Exchange Commission and its various self-regulatory arms) in many
more speciﬁc ways than the money market.
The major distinction between the money and capital markets is
the maturity of the instruments. Because capital market instruments
have maturities beyond one year, the measurement of yield on these
securities depends upon time value of money calculations. From
Chapter 2, we know that the basic equation for the yield on any
asset is:
P0 =
A1
(1 + i)1 +
A2
(1 + i)2 + · · · +
An
(1 + i)n ,
(3.1)
where P0 is the current price of the asset; A1 is the dollar return
from the asset one period (year) from now; A2 is the dollar return
two periods from now, and so on; n is the number of periods the
asset will generate payments; and i is the yield on the asset.
This equation may be rewritten as:
P0 =
n

t=1
At
(1 + i)t .
(3.2)
The computation of a rate of return is easy if the dollar payments
in the future are constant. All one need to do is divide the dollar
payments into its current value. Either present value factor tables
or direct calculator (computer) computations demonstrate this. For
example, if a mortgage obligates the borrower to pay a sum of $1,000
per year for 18 years, and the face value of the mortgage is $10,000,
the factor is:
$10,000/$1,000 = 10.
--- page 89 ---

66
Quantitative Financial Analytics
Using the factor calculations in Appendix A, we ﬁnd that a factor
10.059 exists for an 18-year present value if the rate of return is
7 percent. Thus, the mortgage has a yield of about 7 percent. In
many cases, the solution for a rate of return will not be found directly
from the tables but will require interpolation. Using a calculator or
computer provides more accurate results and is much easier.
When the future payment stream is not constant but diﬀers from
year to year, the solution is more tedious and requires a trial and error
approach. Bonds pay an annual (or more frequently, semiannual)
coupon. At the date of maturity of the bond, the principal sum (par
value) of the bond is repaid to the holder. Thus, Equation (3.1) could
be rewritten in this case as:
P0 =
n

t=1
Ct
(1 + i)t +
Pn
(1 + i)n ,
(3.3)
where P0 is the current market price of the bond; Ct is the annual
dollar coupon payment on the bond; Pn is the par value of the bond;
n is the number of years until the bond matures; i is the yield to
maturity on the bond.
Suppose a bond will mature in ﬁve years. The bond will pay
$1,000 upon maturity and pays $70.00 per year each year for the ﬁveyear period. What is its yield to maturity? To ﬁnd the answer, we
must know the current price of the bond, which we shall assume is 95.
Since bond prices are quoted in percentages of par, this means that
for a $1,000 par bond one pays $950.00 for a stream of payments of
$70.00 for ﬁve years plus $1,000 at the end of the ﬁfth year. Because
the bond is selling at a discount, we know that its yield must be
greater than its coupon yield of 7 percent (that is, $70.00 on a par
of $1,000). From factor calculations, we ﬁnd that at 8 percent, the
present value of this stream is:
3.993 × $70.00 = $279.51
0.681 × $1000.00 = 681.00
$960.51.
--- page 90 ---

The Securities Markets and Macroeconomics
67
This present value is too high. Hence, the yield must be greater than
8 percent. Let us try 9 percent:
3.890 × $70.00 = $272.30
0.650 × $1000 = 650.00
$922.30.
The value of $950.00 is between $960.51 and $922.30. Thus, by
interpolation we may ﬁnd the yield to maturity:
8.0 percent = $960.51
9.0 percent = $922.30
8.3 percent = $950.00.
For a bond, there is a shortcut formula that will give the yield to
maturity rather closely if the bond is selling reasonably near par and
if there are only a few years before it matures. This equation is:
i = C + (Pn −P0)/n
(Pn + P0)/2
.
(3.4)
We may use Equation (3.4) to solve for the yield in the previous
example:
i = 70 + (1000 −950)/5
(1000 + 950)/2
= 80
975 = 8.2%.
Thus, the shortcut formula comes close to the actual yield to
maturity of 8.3 percent. This computation is again most easily made
on a calculator or computer.
Long-term debt instruments
The long-term marketable debt of the federal government consists of
treasury notes and treasury bonds, both of which usually pay interest
semiannually. The notes are issued with an original maturity of one
to ten years and are generally sold quarterly. Although the bonds
have no maturity restrictions, they are presently sold in 20 and 30
year maturities.
--- page 91 ---

68
Quantitative Financial Analytics
Government agencies and sponsored corporations also issue
shortand long-term debt in their own names. This group includes
the Federal National Mortgage Association (“Fanny Mae”), the
Government National Mortgage Association (“Ginny Mae”), the
Student Loan Marketing Association (“Sallie Mae”), the Tennessee
Valley Authority (TVA), the Federal Home Loan Mortgage Corporation (“Freddie Mac”), the Federal Land Banks, the Farmers’ Home
Administration, and the Export–Import Bank and other agencies
that seem to be created regularly by the federal government. None of
the debts of these agencies is a direct obligation of the government,
although it has been assumed by the investment community that
none of them would be allowed to default. As a result, agency issues
command a rate only slightly higher than treasury securities. The
securities are generally issued originally following an announcement
by the ﬁscal agent and trade in a reasonably active secondary
market.
One aid in market eﬃciency is size of issue. Even with the best
of intentions, it is very diﬃcult to maintain an active secondary
market in a security of which there is little outstanding. This is
one reason that treasury bills are such good liquidity instruments;
every weekly oﬀering is for several billion dollars, and therefore a
transaction involving several million dollars worth of bills should
not upset the market greatly. The longer-term issues, however, are
smaller, raising the possibility of a large transaction inﬂuencing the
price. For example, if an investor wished to acquire in the market
$10 million of a $200 million corporate bond issue, he or she might
need to bid the price up signiﬁcantly to ﬁll the order. Fortunately,
ratings come to the rescue. Instead of seeking a particular issue,
the investor might simply specify that he or she wished to buy
$10 million of Aa-rated industrials maturing in the next 10–15 years.
His or her broker could then obtain whichever bonds of this type were
oﬀered, and the investor would receive several diﬀerent bonds at a
far more reasonable price. Thus, ratings help make “thin” markets
more eﬃcient (See Chapter Six for more details.).
Finally, bonds are also oﬀered by international institutions
of which the U.S. is a member. Included in this group are the
--- page 92 ---

The Securities Markets and Macroeconomics
69
International Bank for Reconstruction and Development ((IBRD)
or simply, World Bank) and the Inter-American Development Bank.
These issues are secured by the assets of the banks and, beyond
that, by the right of the banks to call upon their members for
additional contributions to meet debt requirements. The investment
community has viewed this “back door” guarantee as only slightly
weaker than the implicit guarantee of the agency issues and has
priced the securities accordingly.
Municipals were introduced earlier in this chapter, and the point
was made that they are currently generally exempt from federal
income taxes. These bonds are often in serial form, meaning that
a speciﬁed portion of an issue matures each year. They may also
be identiﬁed as either general obligations or revenue bonds. General
obligation bonds (GOs) pledge the “full faith and credit” of the
government entity to the payment of the bonds. In analyzing such
bonds (discussed in detail in Chapter 6), aside from the ratings given
by the bond agencies and the default record of the community, one
often looks at the value of property, the tax rate, debt per capita,
debt service as a proportion of the operating budget, and various
demographic factors. Is the community growing? Or is it dependent
upon one industry, so on?
Revenue bonds, on the other hand, do not pledge the credit of the
community but only the proceeds from the project being ﬁnanced by
the bonds (everything from toll roads to college dormitories). In this
case, therefore, the investor looks at the need for the project, the
adequacy of the expected usage and charges, and so on. Confusion
can arise because there have been cases of quite credit-worthy
communities defaulting upon revenue bonds when proceeds were
inadequate because they were not obligated to pay the bonds; the
Calumet Skyway bonds issued by Chicago several decades ago is
a case in point, and this example also illustrates some additional
protection oﬀered by the bond market. It is almost an unwritten rule
that an issuer who has defaulted will ﬁnd it virtually impossible to
raise new funds until settlement is made with the old holders. Even
though Chicago was not legally obligated on the Calumet bonds, it
found the reception for its other bonds after the default suﬃciently
--- page 93 ---

70
Quantitative Financial Analytics
cold that oﬃcials for some years seriously considered paying them oﬀ
and ultimately did so.
Several factors frustrate the eﬀorts of American investors to
purchase foreign stocks and bonds. First, of course, is the currency
risk — the possibility that the currency in which the foreign security
is denominated will change its parity vis-`a-vis the dollar. In the shortterm area, it is suggested that a covering transaction in the forward
exchange market could eliminate this risk. Unfortunately, however,
the forward market in most currencies becomes quite thin beyond
six months, and even in the most active currencies it is diﬃcult to
obtain a commitment beyond a few years.
Taxes in foreign countries also present an additional burden. Most
long-term foreign securities are subject to withholding tax on interest
and dividends paid (most of the short-term foreign instruments are
exempted). Depending upon the tax treaty between the U.S. and the
foreign country involved, taxes withheld abroad may serve as either
a credit or deduction on American tax returns. If only a deduction
is allowed, a greater total tax is paid. Even if a full tax credit is
allowed, a loss may occur if the foreign withholding rate is greater
than the American rate paid (often the case for ﬁnancial institutions
and obviously so for tax-exempt organizations).
Corporate debt may take the form of either a publicly oﬀered
bond issue or a privately placed note. The private placement is
generally made with one or a few large institutional investors and
is, as a rule, held until maturity by the original purchasers. In return
for this lack of marketability, the lenders generally receive a slightly
higher coupon and are able to obtain a larger portion of the issue
(an advantage to institutions such as insurance companies that have
small staﬀs and much money to invest).
Bonds are sold to the public through an underwriting, by which
an investment banker buys the bonds from the issuer, marks them
up, and attempts to sell them to the general public. The bonds
can be bought from the issuer by the investment banker either at
a price negotiated by the parties involved, or by competitive bid.
Most companies regulated by agencies of the government (power
companies, railroads, and so on) are required to sell their securities
--- page 94 ---

The Securities Markets and Macroeconomics
71
by competitive bid; most others negotiate. The bonds are issues
and sold under an indenture, which is a statement of rights and
obligations negotiated between the issuing company and the trustee
(often the trust department of a bank) as representative of the
lenders. The importance of the indenture, and its salient features
printed in the prospectus, cannot be overstated; it is the ﬁnal arbiter
of the rights and duties of borrowers and the lender, as many bond
buyers have subsequently discovered to their sorrow.
Among the facts to be found in an indenture are the provisions
for retirement and refunding of the issue. For example, a portion
of the bond issue may be retired each year prior to maturity. This
may be done by having the company pay the trustee, who, in turn,
determines by lot which bonds will be called for redemption or by
merely having the company enter the market to buy the required
number of bonds. These two methods may usually be employed at
the company’s option, which is a disadvantage to the bondholder.
If rates rise and the bonds go to a discount, the company can
buy them in the market; if rates fall, the company can have the
trustee call the bonds at or above par. In like manner, the refunding
(or call) provisions also work to a disadvantage to the lender. In a
reasonably eﬃcient market, of course, the bondholder would receive
a higher return in compensation for these disadvantages. If interest
rates decline, the issuer invariably has the right to call the bond issue
and refund it at the lower rate. The only protection to the bondholder
is that such a call must generally be made at a slight premium over
par and that there may be an interval of 5 or 10 years after the bonds
are issued (the no-call period) during which a call is not allowed.
Finally, the company may be allowed to call the issue at a very
small premium if the funds do not come from a cheaper bond issue
(for example, if the company sells assets). The issuer can generally
be expected to undertake its most advantageous option, which is also
generally the least advantageous to the holder.
The indenture will also indicate the security of the issue.
Mortgage bonds are secured by a lien on all or part of the property of
the issuer. In bankruptcy, the mortgage bondholders have ﬁrst claim
upon the proceeds of the property against which they hold a lien;
--- page 95 ---

72
Quantitative Financial Analytics
to the extent that these proceeds are inadequate, the bondholders
become general creditors for the rest. It is also possible to issue
second (and even lower priority) mortgage bonds; these holders have
a claim on any proceeds from the mortgaged property after the prior
mortgage holders are satisﬁed (and become general creditors for any
of the remainder).
A very strong mortgage bond would include an after-acquired
clause, indicating that not only is all current property of the company
subject to the mortgage but all new property acquired later is also
encumbered; this provision is so strong that it would require the
company to make any new debt second mortgage or lower in priority.
The open-end indenture is less rigid in that the company is allowed
to issue additional debt on the same mortgage; to protect the old
holders; however, the new debt is generally limited to some fraction
(often 50–66 percent) of the net increase in property subject to the
mortgage.
Two other types of secured bonds are the collateral trust bond
and the equipment trust certiﬁcate. For the ﬁrst type, the borrower
places the securities of other companies into a trust and then issues
securities against the trust. For the second type, used extensively by
railroads and airlines, title to the equipment is held by a trustee for
the beneﬁt of the lenders until the company has redeemed the debt;
thus, the lenders can obtain immediate possession of the equipment
and resell it if the borrower goes into bankruptcy.
Debentures are not secured by any particular piece of property
and are only covered by the general credit of the borrowing corporation. In bankruptcy, the debenture holder ranks as a general
creditor of the corporation. Subordinated debentures are of even lower
priority, in that the proceeds that the holders would receive as general
creditors in bankruptcy must go to satisfy the claims of the issues to
which they are subordinated. Even junior subordinated debentures
have been issued.
Income bonds obligate the issuer to pay interest only if the ﬁrm’s
earnings are suﬃcient to make payment. The income bond has been
used historically by trustees in many railroad reorganizations. As
a result, these bonds have achieved a relatively poor reputation. It
--- page 96 ---

The Securities Markets and Macroeconomics
73
might also be noted that, in the purchase of most bonds, the investor
pays the price quoted plus accrued interest on the bond; in the case
of income bonds and bonds in default, no accrued interest is included
(the bonds are said to trade “ﬂat”). Finally, convertible bonds, which
grant the holder the option to exchange the bond for stock at a
speciﬁed ratio, are also issued in debenture form. These subjects are
discussed in greater detail in Chapter 7. In conclusion, it must be
stressed that only an examination of the indenture will reveal the
attributes of any given issue.
Equity securities
Equity instruments are also a part of the capital market. Preferred
stock represents a curious combination of various features of debt
and common stock. It is like common stock in that the instrument
is called stock and is included in the equity section of the balance
sheet of a corporation. Payments are called dividends and are not
deductible for tax purposes by the corporation; the payment of
dividends is not legally required, and the issue typically has no
given maturity. Preferred stock is like debt in that the dividends
have a ﬁxed maximum rate. Preferred holders generally have no vote
on corporate matters unless a speciﬁed number (often four to six
quarterly) of dividends are passed, in which case they may typically
elect a minority of the board of directors. Preferred stockholders are
entitled to no more than the amount paid in to the ﬁrm in case of
liquidation, and preferred stock may contain the same call, sinking
fund, or conversion features as any debenture. A rare type, called
participating preferred, provides that after preferred dividends have
been paid and common shareholders have received a like return, both
classes may participate by some formula in any additional dividends
to be paid.
Cumulative preferred requires that all past, unpaid dividends
be paid (although not with interest) before any common dividend
may be paid; noncumulative preferred only requires that the current
year’s dividend be paid before a common dividend is paid. Companies
with either large arrearages on their preferred stock or high-dividend
non-callable preferred are often forced to make an exchange oﬀer
