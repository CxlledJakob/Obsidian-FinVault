# Quantitative financial analytics_ the path to investment profits.pdf — pages 58–77

--- page 58 ---

The Challenge
35
1934 gave the Board of Governors of the Federal Reserve System the
power to set margin requirements for all stocks and bonds. Another
practice that caused problems prior to 1933 was the short sale.
This process is still permitted, although the SEC may make rules
governing its use.
In order to determine whether one has earned above (or below)
market returns, one must have a good measure of the average
performance of stocks in general. No perfect indicator exists. The
most widely used average is the DJIA. The DJIA is primarily a
blue-chip measure, although many investors use it for overall market
activity. S&P computes indices that have a larger base than the Dow
Averages. The S&P measures are also statistically superior to the
Dow calculation.
References
Adams, C. F. and Henry Adams, Chapters of Erie. Ithaca: Great Seal
Books, 1956.
Allen, F. L., Only Yesterday. New York: Harper & Row, 1964.
Cootner, P. H., ed., The Random Character of Stock Market Prices.
Cambridge: The M.l.T. Press, 1964.
DePamphilis, D. M., Mergers, Acquisitions, and Other Restructuring
Activities, 6th ed. New York: Academic Press, 2012.
Fama, E. F., “Random Walks in Stock Market Prices,” Financial Analysts
Journal, September–October 1965, pp. 55–59.
Fama, E. F., “Eﬃcient Capital Markets: A Review of Theory and Empirical
Work,” Journal of Finance, May 1970, pp. 383–423.
Galbraith, J. K., The Great Crash. Boston: Houghton-Miﬄin Co., 1954.
Graham, B. and D. Dodd, Security Analysis. New York: McGraw-Hill, 1934.
Graham, B., D. Dodd, and S. Cottle, Security Analysis, 6th ed. New York:
McGraw-Hill Book Company, 2009.
Keynes, J. M., A Tract on Monetary Reform. London: McMillan & Co.,
1923.
Keynes, J. M. The General Theory of Employment, Interest, and Money.
New York: Harcourt, Brace, and World, 1936.
Lee, Ruben, What is an Exchange? The Automation, Management, and
Regulation of Financial Markets. New York: Oxford University Press,
1998.
Mackay, C., Memoirs of Extraordinary Popular Delusions and the Madness
of Crowds. London: George Routledge and Sons, 1869.
--- page 59 ---

36
Quantitative Financial Analytics
Rubinstein M., A History of the Theory of Investments. New York: John
Wiley & Sons, 2006.
Taleb, N., The Black Swan. New York: Random House, 2007.
Thompson, J. R., E. E. Williams, and M. C. Findlay, Models for Investors
in Real World Markets. New York: John Wiley & Sons, 2003.
Williams, E. E. and H. A. Napier, Essentials of Entrepreneurship. Chicago:
T.&N.O. Book Co., 2013, pp. 257–268.
--- page 60 ---

Chapter 2
Financial Mathematics
Gentlemen, if the man who invented compound interest
had of secured a patent on his idea he would have had
without any doubt the greatest invention the world has
ever produced.
Security Investment Co., 1916
Introduction
The ﬁnancial economics texts typically begin with a discussion
of compound interest, yields, and returns. Others then turn to
probabilistic considerations such as stochastic ﬁnance. Here, we step
back a bit and consider the underpinnings of ﬁnancial mathematics
and some of its applications.
Although some of the techniques in this book require the
use of computers and programming languages, with Monte Carlo
resampling techniques, the bulk of ﬁnancial mathematics is still
performed in spreadsheets, or with high-powered hand calculators.
Indeed, soon these calculations will be carried out on the reader’s
handheld communication device. It is nonetheless humbling to note
that many multi-billion dollar deals are estimated, calculated, and
“what-if-ed” with the lowly HP-12C ﬁnancial calculator.
In essence, there is nothing out of the ordinary in ﬁnancial
mathematics not encountered in usual practice, except for the
following three additional axioms which are generally not stated: the
axioms of Value, Time, and of the Time Value of Money (TVOM).
Although the following concepts deliver the reader to a mineﬁeld of
philosophical considerations, we hope that he or she will absorb the
37
--- page 61 ---

38
Quantitative Financial Analytics
basic ideas and consult appropriate texts for the other nuances which
will arise.
Axiom of value
There exists an asset X, which can be exchanged for another asset
Y . We may possess 2X irrespective of the value of X expressed in
terms of the reference asset Y . Suppose X may be exchanged for 3Y .
We say the price of the asset in terms of Y is 3. Then the value of X
with respect to Y is 3Y , or VY (X)XY = 3. In this case, the holding
of 2X is worth 6Y .
The formal name for this framework is numeraire analysis, and
it is mostly outside the scope of this text. However, this and other
concepts are not unusually hard to grasp, so we will mention them
here. The fundamental point of numeraire analysis is that the asset
valuation for non-arbitrage assets can be made in terms of any
convenient reference asset. A non-arbitrage asset is any asset which
retains its fundamental existence irrespective of any reference asset
valuation, such as physical gold, or (non-dividend paying) shares in
a company, or a bond which pays a terminal value at time t = T. In
contrast, an outright holding of currency (for example dollars, $) is
considered an arbitrage asset since another buyer can buy back the
asset using funds upon which interest has been earned.
For our purposes, we are generally concerned with the reference
asset of currency, i.e., we exchange X for $/ /¥/£, etc., and we normally hold such assets over multiple periods of time. For convenience
and consistency with the majority of texts, therefore, we will usually
express assets X(t) valued in a home currency with customary
symbols, such as F (futures), S (stocks), C/P (calls and puts), V
(derivative contracts), B (bonds), or D (dividends of cash ﬂows).
Axiom of time
We treat time in a unidirectional sense, i.e., time moves “forward,” in
most systems it progresses “to the right.” Indeed, almost all physical
systems have in their implicit axioms the rule that future states are
not known, i.e., the system is causal. Thus, ∀s, t and t ≥s, we say
--- page 62 ---

Financial Mathematics
39
t is a later time than s; or, from an outside perspective, t is “in the
future with respect to s.”
As we discuss in Chapter 9, utility can be applied to time and
value. In this book, our concern is generally about making allocation
decisions at the present for cash ﬂow streams occurring in the
future, or vice versa. We do not generally spend too much time on
past allocations. These are considered in accounting terms as sunk
costs/opportunities. So, most cases in ﬁnance deal with present and
future values.
We are again ignoring the philosophical aspects of the existence,
deﬁnition, and progression of time. Occasionally, we might make a
distinction between spatial dimensions (the world we live in) and a
set of spatial dimensions onto which the time dimension is added.
(a) Beginning points: For making a reference to a beginning point
in time we say t = t0. For s, t ∈R, there are applications where
t = (s, t) ∈Rk, k > 1.
(b) “Ending” (Horizon) time: t = h or t = T. For any two points
in between, t ≥s, we can deﬁne ∆t = t −s ≥0, which
is often notated as τ = t −s ≥0, although we normally
reserve τ for continuous time, or time-to-horizon presentations.
In many applications, τ = h −t0, t0 = 0 and h ≡T such that
τ = (T −0) = T.
(c) Increments of time: In general, τ ∈T , is an index set, giving
∆τ = τn −τm. There are various ways to deal with increments
in this notation. The simplest way is to restrict ourselves to
“periods” of variable lengths of time, not necessarily equal, or
∆t = tk −tk−τ. Here, “τ” has developed a new use, as an
increment.
An even simpler way to express increments is to use countable
index sets T ≡T so that ∆t = tk −tk−l, where l is an integer.
This has the added beneﬁt of freeing up our symbol τ for more
widely used deﬁnitions (see below).
Yet another simpliﬁcation is to restrict attention to l = 1, or
∆t = tk −tk−1. This permits a simple, intuitive, and discrete
system.
--- page 63 ---

40
Quantitative Financial Analytics
Suppose we translate our time frame of reference to t0 = 0,
and consider n periods of equal length ∆t. Then our horizon
h = n∆t, which we can also write as t = tN. Using years, for
example.
Here, we have t0 = 0 years, ∆t = 1 year, and h = n∆t,
sometimes written with N being the maximum number of
periods. Note that with t0 = 0, T −t0 = n (or N).
(d) Arbitrary point with respect to T: For an arbitrary point t:
0
t0
t
T
We can deﬁne a “time remaining” in an analysis as τ = T −t.
For t = t0, τ = T −t0 is the “full” horizon time.
For example, suppose a time-dated instrument is scheduled to
expire 1 month from the day it comes into existence. Then at
the outset the time to expiration (TTE) is 1 month, or 100% of
its lifetime. Thus, t0 = 0, T = 1, so τ = T −t = 1(month). One
week later, t = 1
4 and τ = T −t = 3
4(month). Note that 1 second
before trading stops on this option, τ ≈0 (1 trade-second).
For another example, a time-dated instrument with 90-day
(3-month) maturity changes hand 1 month from issue. Thus,
τ = T −t = 3 −1 = 2 months = 60 days.
Axiom of time value of money (TVOM)
For a currency (for example, a dollar), $(t) > $(t+k), ∀k > 0. That is,
the value of a dollar today is more than the same dollar at some time
in the future, since in general it may have been invested in a money
market instrument earning a positive rate of interest. Time has a
price, denominated in percent of principal involved. This relation
--- page 64 ---

Financial Mathematics
41
has been in operation for millennia and has been mathematically
described at least since Fibonacci in 1202 AD. This is also true
in spite of the near zero-interest rate environment that prevailed
from 2009–2016. Even in a zero-rate regime, statistical considerations
require the TVOM axiom, since events which decrease the asset’s
reference value (price) can always occur in the time interval [t, t+∆t).
Future and Present Value
Simple and compound interest
A good part of ﬁnancial analysis depends upon calculations of
compound interest. This is because the time horizon in ﬁnance is
usually long, and so some method must be obtained to compare
ﬁnancial ﬂows over time. Because of the TVOM axiom, and the
fact that ﬁnancial ﬂows may be “invested” at some positive rate
of interest, a ﬂow received today is worth more than an equal ﬂow
received in the future. This idea may be expressed as a very simple
equation:
Dn = D0
n



(1 + i)(1 + i) · · · (1 + i),
(2.1)
Dn = D0(1 + i)n,
where D0 is a ﬁnancial ﬂow (number of dollars) invested today; Dn
is the value n periods from now of the invested ﬂow D0; and i is the
periodic rate of interest by which D0 will grow for n periods, held
constant in this equation.
Thus, if $1,000 is put into a savings account today and is left
there for one year at a rate of interest of 5 percent compounded and
paid annually, that sum will be worth $1,050 after one year. If the
$1,000 is left on deposit for two years, at the end of the second year
it would be worth:
Dn = $1,000(1.05)2 = $1,102.50.
The factor (1 + i)n may be obtained immediately using a calculator,
a spreadsheet, or the formulas in Appendix A. Thus, if $1,000 is left
--- page 65 ---

42
Quantitative Financial Analytics
on deposit for 20 years (assuming annual compounding), at the end
of that period it would be worth:
$1,000(2.653) = $2,653.00.
Continuous compounding
Interest may be compounded more often than once per year. When
interest is compounded several times during the year, we interpret
as follows:
Let:
t = number of years
T = horizon time (n · t)
r = annual interest rate (using 12% in the example)
D0 = $1,000 initial investment
m = Compounding frequency
Annual: m = 1
DT = 1,000(1 + r)1 = $1,120.
Semi-annual: m = 2
DT = D0

1 + r
m
mt
= D0

1 + r
2
2t
= $1,000 · (1.06)2 = $1,123.60.
Quarterly: m = 4
DT = D0

1 + r
4
4t
= $1,000 · (1.03)4 = $1,125.51.
Daily: m = 360.
There are various conventions for the number of days in the
year. For ﬁxed income investments, the most common numbers in
use are 360 and 365 (calendar days). Which one is intended will be
speciﬁed in context, or by industry standard. Business (trading) days
are about 252 per year. The actual number of days in a year, 365.25,
--- page 66 ---

Financial Mathematics
43
is almost never used
DT = $1,000 ·

1 +
r
360
360t
= $1,127.47.
Note that although the terminal value is going up with the compounding frequency, it appears to be approaching a limit, which it
is, and may be written as
lim
m→∞(1 + r/m)mt = lim
m→∞

1 + rt
mt
mt
= ert.
(2.2)
Thus, DT = D0ert.
Continuous compounding is an unusual species. It even reportedly puzzled the great Einstein. In our example, DT = $1,000e0.12t =
$1,000e0.12 = $1,127.50. We ﬁrst note that the change from 360 to
continuous compounding did not make much diﬀerence. Although
some rules such as the rule-of-72 give rough ideas of the compounding relationship, they result in terminal values which invariably are
non-intuitive. (The rule-of-72 posits that dividing an interest rate
into 72 will result in the approximate number of years required for an
investment to double.) In our 1-year example, if we were to calculate
this amount over a 20-year period, the compound factor would be
e0.12·20 = 11.0231; yet, it takes 48 years at an interest rate of 5
percent to attain the same terminal value of 11.0231.
In most practical ﬁnance applications, semi-quarterly, quarterly,
or perhaps monthly compounding is typically suﬃcient, continuous
compounding is mostly used for approximating and for mathematical
and conceptual reasons. It is, however, widely used in ﬁnancial
engineering.
Annuity values
When funds are deposited periodically to an account, the terminal
or annuity value of the payments is given by a series of the following
type:
Vn = D0(1 + r)n + D1(1 + i)n−1 + · · · + Dn(1 + i)n−n,
Vn =
n

t=0
Dt(1 + i)n−t.
(2.3)
--- page 67 ---

44
Quantitative Financial Analytics
Each payment has its own terminal value of Dt(1 + i)n−t, until the
ﬁnal payment at Dnwhich earns no interest, and indeed would be
withdrawn as soon as it is deposited. An alternate annuity value is
made by excluding this ﬁnal payment, or
Vn =
n−1

t=0
Dt(1 + i)n−t.
(2.4)
If the deposits are equal over time, i.e., D0 = D1 = Dt = D, we have
Vn = D
n−1

t=0
(1 + i)n−t,
or
Vn
D =
n−1

t=0
(1 + i)n−t.
This latter term is the compound value of an annuity and can be
calculated with some small amount of additional work, or can be
calculated using Appendix A.
In the case of continuous compounding, Equation (2.3) becomes
Vn =

 n
0
D(t)

1 + i
m
m(n−t)
dt.
In the limit we ﬁnd
Vn =

 n
0
D(t)ei(n−t)dt.
Assuming i and D are constant we may integrate to obtain
Vn = D
i (ein −1).
(2.5)
Present value and discounting
A present value (PV) is the value today of funds received in the
future. It is, in eﬀect, the reverse operation of a compounded sum.
Thus, if we know Dn dollars will be received n periods from now,
and if we know the rate of interest, we can determine the PV, D0,
of that future sum. This process is described simply by rewriting
--- page 68 ---

Financial Mathematics
45
Equation (2.1) in the following form:
D0 =
Dn
(1 + i)n = Dn(1 + i)−n.
(2.6)
Again, the PV factors may be easily calculated, or the reader may
refer to an appropriate PV table. This interest rate i is often referred
to as a discount rate since it is the factor which deﬂates a future
value to the present, reﬂecting the fundamental axiom of TVOM.
Determination of the appropriate discount rate is a thorny issue.
Discounting can also be calculated based on a more frequent
discounting program, or even continuously, exactly as we did for
future value. For continuous discounting, we have
D0 = Dte−rt.
(2.7)
For annuities, the PV of future payments is
PV = V0 = D0(1 + r)−0 + D1(1 + i)−1 + · · · + Dn(1 + i)−n,
or
V0 =
n

t=0
Dt(1 + i)−t.
(2.8)
When the payments Dt vary from year to year, the PV must be
obtained after some computer programming, or by manually adding
each term using discount factors. Most ﬁnancial calculators and other
applications have built-in routines to accommodate the user input of
diﬀering incomes streams.
If the payments are constant over time, however, Equation (2.8)
may be simpliﬁed to
V0 = D
n

t=0
(1 + i)−t.
(2.9)
Similar to how we obtained (2.4), if we assume that the ﬁrst payment
is received 1 year from now, then the equation becomes
V0
D =
n

t=1
(1 + i)−t.
(2.10)
The factor on the right-hand side of (2.10) may be computed.
--- page 69 ---

46
Quantitative Financial Analytics
Capitalization of an income stream
Under continuous compounding assumptions, the basic PV Equation (2.6) becomes
V0 =

 n
0
D(t)e−itdt.
(2.11)
If D(t) and i are constant, Equation (2.11) can be integrated to
give
V0 = D
i (1 −e−in).
(2.12)
Note that if the constant income stream continues indeﬁnitely,
as n →∞the equation reduces to
PV = V0 = D
i .
(2.13)
This last equation is a very important one, and the process
underlying the equation is frequently referred to as capitalization. A
number of ﬁnancial instruments have very long (or inﬁnite) lives. A
perpetual bond, for example, promises to pay a coupon of a constant
amount forever. Such an instrument may be evaluated very quickly
with Equation (2.13). In forecasting cash ﬂows of a company, for
example, detailed predictions may be made for a near-term horizon,
with the out-years being modeled by (2.13), using an economic
growth rate for perpetuity. Common stocks may also be valued with
this equation, but one must be careful about growth assumptions in
this case. For a ﬁrm that pays a reasonably constant dividend, the
equation is adequate. For a growth stock where D is increased over
time, the assumption of a constant D(t) is violated, and the equation
is inappropriate.
Financial Returns
Jokes about return “of” capital aside, return on investment is one
of the underpinnings of the investment paradigm. As we stated in
Chapter 1, we have the expectation of a return in a reasonable period
--- page 70 ---

Financial Mathematics
47
of time, along with safety of that return, as well as safety of the
investment itself.
Gross returns
These are also called total returns. Financial returns can be considered a growth factor of an investment S, and are quite similar
to future value, depending on the compounding scheme. To make a
working deﬁnition, for time t, we deﬁne a 1-period return as
Rt =
St
St−1
.
(2.14)
Clearly, S1 = S0R1. Here, the “return” R1 represents the growth
of the investment. Although it is not necessary to do so, one can
decompose this gross return into a return of principal plus a simple
growth rate (which could be an interest rate) r in 1 period, we have
that S1 = S0(1 + r)1. However, that is an example of a deﬁnition
of a marginal return; we will see that gross returns provide a much
simpler analysis framework.
Suppose we have a dollar-denominated asset S(t) ≡St which
exhibits the following growth factors over 4 periods:
R1 = 1.10
R2 = 1.05
R3 = 0.95
R4 = 1.20.
Assuming observable market prices, these growth factors are
easily obtained using (2.14). Since Rt = St/St−1 and St = St−1Rt,
and beginning with S0 = 100, we have
S1 = S0R1 = 100(1.10) = 110,
S2 = S1R2 = S0R1R2 = 110(1.05) = 115.5,
S3 = S2R3 = S0R1R2R3 = 115.5(.95) = 109.725,
S4 = S3R4 = S0R1R2R3R4 = 109.725(1.20) = 131.67.
(2.15)
The terminal value is quite easy to determine given the gross
returns. We state our terminal asset value as ST , and note from
--- page 71 ---

48
Quantitative Financial Analytics
the above that ST = S0
T
t=1 Rt = S0RT , where the terminal gross
return is RT . Again,
RT = (S1/S0)(S2/S1) · · · (S4/S3)
= S4/S0 = ST/S0 = ΠRt.
(2.16)
In our example, we have RT = 1.3167. It is rather pleasant that
the terminal gross return is independent of the time granularity of
the price series; neither is it sensitive to unequal increments. Using,
for example, the commodity cotton, from 9/8/11 to 9/6/12, there
were 252 trading days which saw the price descend from 105.02
to 75.59 (c/lb), giving a terminal return of 0.736. This will be the
same regardless of whether the prices are monthly, yearly, daily, or
sporadic, so long as the beginning and ending dates have data and
are properly recorded.
Since the gross returns are always greater than or equal to 0,
discounting and compounding is somewhat more straightforward
with returns as opposed to the general PV or future value of varying
income streams. The fundamental value of study is the terminal value
of an investment, which is easily observable for historical data, and its
analysis follows below. Determining a future terminal value, however,
is the essence of the problem of investments analysis.
As an aside, however, it should be noted that the return calculation can be diﬃcult if the payment streams change sign over the
time period in question. This rarely happens for ﬁnancial instruments
like bonds and stocks where investors pay for an income stream
and the only sign change takes place from the time of investment
(t = 0) with a negative sign and the payments received (all future t’s)
with positive signs. However, this same procedure can apply to the
purchase of any asset (say a machine or plant and equipment) which
may require infusions of cash in future periods that might result in
a negative net payment (additional investment). Each time there is
a sign change there may be another return solution. In essence, we
have a polynomial with n roots, and a solution for each root. If there
is only one sign change, there will only be one solution (positive or
negative). With many sign changes, there may be many solutions,
--- page 72 ---

Financial Mathematics
49
including positive and negative real numbers, irrational numbers,
or imaginary numbers. For additional discussion and examples, see
Appendix A.
Incremental returns
While gross returns are quite useful, it is however completely natural
to want to have at our disposal measures of incremental return. We
examine the relative merits of 3 useful deﬁnitions of incremental
returns. Each one of them is applicable in individual periods, or over
an entire time horizon.
(a) Absolute diﬀerences: We could deﬁne an incremental return as
∆St = St −St−1. This would give us a series of the absolute
changes in the asset price, from which we could reconstruct the
terminal value. However, apples/oranges problems arise if you
try and compare say changes in cotton prices with those of other
assets. In the case of cotton in the previous example, ∆S is
−29.43, but for median home sale prices in a neighborhood, or
for yacht prices, the diﬀerence could easily be $50,000.
(b) Relative returns: The most widely used method of relative
comparison is to scale the change by the initial asset value, i.e.,
∆S/S. This is
St−St−1
St−1
= Rt −1 = r%, or what we call the
percent change in the asset price (percent return), and is highly
engrained in the most quantitatively literate people’s psyche. If
you start with an asset at $50, and sell at $55, you have made
a 10% “return.” Colloquially we use r, or rpct, instead of r%. In
fact, you have made a 10 “percent return.” Unfortunately, neither
the sum nor the average of percent returns applied to the original
asset price will recover the terminal value, which feature we need
for subsequent, consistent analysis.
(c) Mathematical returns: We deﬁne a mathematical return
r = ln(R) = ln(St/St−1) = ln St −ln St−1 = ∆ln S.
This return r, sometimes written as r, is close to but not exactly
the same as r% and is vastly diﬀerent for large diﬀerences. That
they are close is seen by the mathematical approximation for
--- page 73 ---

50
Quantitative Financial Analytics
the log function, as r = ln(R) ≈ln(1 + r%) = r% −
r2
%
2 +
r3
%
3 −· · · ≈r%. Using the second-order term makes for quite a
nice approximation, and also shows that r < r%. Note that this
approximation is only good in the range |r%| < 1; however, since
in many years there are hundreds of stocks which lose 50 percent
or more of their value, and there may be many dozens which
experience more than 100 percent positive returns, a symmetric
relative return is compelling. The log function transforms the
gross return into symmetric excursions as we will later show.
(d) Useful identities: Given r% and r, some identities are as follows:
R = 1 + r% = er,
(2.17)
R =
St
St−1
= 1 + r% = 1 +
 St
St−1
−1

= eln(St/St−1) = er.
(2.18)
(e) Rates of return: The arithmetic rate of return µ over an interval
[t, t + ∆t) is deﬁned as
r%
∆t = St+∆t −St
∆t · St
.
The instantaneous rate of return is obtained as ∆t →0, where
we have
dSt
dt · 1
St
= µ,
or
dSt
dt = µSt.
Similarly, the log rate of return is deﬁned as
ln R
∆t = ln(St+∆t/St)
∆t
= µ,
with ∆t →0 giving the instantaneous log rate of return
lim
∆t→0
ln St+∆t −ln St
∆t
= d ln S
dt
= dSt
dt · 1
St
= µ,
--- page 74 ---

Financial Mathematics
51
again with dSt/dt = µSt. When µ is a constant, the solution for
St is obtained by an elementary guess and is St = Soeµt, the
formula for compound interest. Note that both instantaneous
arithmetic and log rates of return give the same progression
formula for St.
Summary measures
Since we normally deal with large data sets, or at least reasonably
lengthy series of data, a way of summarizing the period returns is
necessary for gauging how well one investment performs relative to
another. What we need is a summary growth rate for comparative
purposes. Consider the example returns in Table 2.1.
There is no doubt that the terminal return is 1.3167, obtained as

i Ri, but how might we summarize the period incremental returns?
We will examine the expected, average, and compound average
growth rates.
(a) Expected (mean) growth rate: A logical statistical solution to
the summary growth issue is to use expected return, E(R).
Unfortunately, in this conﬁguration, R is a random variable with
an unknown probability distribution. If we knew the distribution
we might be able to estimate its parameters, but great minds
have been trying to determine this distribution of R for over
60 years, without success, and not without great eﬀort. So we
will agree to defer developing some new theory of market return
distributions for another time.
Table 2.1. Comparison of Returns
R
r%
r
1.1
0.1
0.095
1.05
0.05
0.049
0.95
−0.05
−0.051
1.20
0.2
0.182
RT 1.3167
?
?
--- page 75 ---

52
Quantitative Financial Analytics
(b) Average (sample mean): This is quite a logical choice we have,
using percent returns, here denoted as r,
¯R = 1
n
n

i=1
Ri = 1
n(1 + r1 + · · · + 1 + rn)
= 1
n

n +

ri

= 1 + ¯r.
(2.19)
Using our data in Table 2.1, ¯R = 1.075. This measure is useful
in some applications but has the disadvantage that it will not
recover RT . That is, RT̸ = Π ¯R = ¯RN. Using ¯R, we obtain for
the terminal value R′
T = 1.3355. It is always the case that:
RT ≤¯RN,
(2.20)
which can be veriﬁed mathematically.
(c) Compound annual growth rate: Consider the geometric mean
⌢
R = (ΠRi)1/N of the gross returns:
⌢R = (ΠRi)1/N = (RT )1/N =
N√
RT .
(2.21)
⌢R has the deﬁnitional property that
⌢R
N
= RT , and that the
compound average growth rate (CAGR), r′ =
⌢R−1, is such that
the terminal value is always recovered as RT . This r′ is sometimes called the internal rate of return (IRR) of an investment,
but the IRR is not perfectly suited to this simple analysis, so we
prefer the standard term CAGR.
Using the deﬁnitions, we have the following tautology:
RT = ST
S0
= (1 + r′)(1 + r′) · · · (1 + r′) = (1 + r′)N,
=
⌢
R
N
= (ΠRi)
1
N N = ΠRi = RT .
(2.22)
We also have the following constraint:
⌢R ≤¯R ⇒r′ ≤¯r.
(2.23)
So in summary, our CAGR is calculated as
r′ =
N√
RT −1.
(2.24)
--- page 76 ---

Financial Mathematics
53
And using our Table 2.1 data, we calculate
⌢R = 1.07123, giving
r′ = 0.07123 < ¯r = 0.075. Of course, (1 + r′)4 = 1.071234 =
1.3167 = RT .
(d) Other considerations: Using the notation that ln Rt = rt, we have
ln
⌢
R = 1
N ln(ΠR)i = 1
N

ln Ri = lnR,
or the average log return ¯r. Thus,
⌢
R = e¯r, and
RT =
⌢R
N
= en¯r = e
P r = er1er2 · · · erN = R1R2 · · · RN.
(2.25)
The symmetry of log returns is very compelling. Consider the
table of realistic returns found in Table 2.2. The shaded section of
the table clearly shows the symmetry; the non-shaded areas depict
the percent returns which have no symmetry.
Table 2.2. Symmetry of Log Returns.
R
r (%)
r
100
9,900
4.605
10
900
2.303
5
400
1.609
2
100
0.693
1.333
33.333
0.288
1.25
25
0.223
1.10
10
0.095
1.05
5
0.049
1.01
1
0.01
1
0
0
0.99
−1
−0.01
0.95
−5
−0.051
0.90
−10
−0.105
0.85
−15
−0.163
0.667
−33.333
−0.405
0.5
−50
−0.693
0.2
−80
−1.609
0.1
−90
−2.303
0.01
−99
−4.605
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
