# Quantitative financial analytics_ the path to investment profits.pdf — pages 533–552

--- page 533 ---

510
Quantitative Financial Analytics
Taleb, N., The Black Swan. New York: Random House, 2007.
Thompson, J. R., E. E. Williams and M. C. Findlay, Models for Investors
in Real World Markets. New York: John Wiley & Sons, 2003.
Treynor, J. L. “How to Rate Management of Investment Funds.” Harvard
Business Review, January–February 1965, pp. 63–75.
Treynor, J. L. and K. K. Mazuy, “Can Mutual Funds Outguess the
Market?” Harvard Business Review, July–August 1966, pp. 131–136.
Treynor, J. L., “Toward a theory of market value of risky assets.”
Written in 1962 but published only recently in Asset Pricing and
Portfolio Performance, edited by Robert A. Korajczyk (London: Risk
Publications, 1999), pp. 15–22.
Whitmore, G. A., “Third-Degree Stochastic Dominance.” American Economic Review, June 1970, pp. 457–459.
--- page 534 ---

Appendix A
Time Value of Money
Numquam poneda est pluralitas sine necessitate.
William of Occam
Present and Future Value Factors
As we saw in Chapter 2, the time value of money (TVoM) axiom
requires some additional algebra in order to value a stream of
payments or dividends realized in future time periods. Table A1
provides some basic time value equivalence factors needed to evaluate
the economic value of these income/expense streams. Traditionally
this has been accomplished with the use of factor tables; this is
generally unnecessary given the ubiquitous computer power available
today. We provide a brief description, generating and summary
formulas, a cash-ﬂow diagram, and pseudo-code needed for the
analyst to calculate her own equivalency factors. Most of these
formulas are available in spreadsheet programs such as Microsoft
Excel as well.
There are also calculators for these factors which can be found
on the Internet; a small sample includes:
• www.ﬁnanceformulas.net
• www.calculator.net/ﬁnancial-calculator.html
• www.ultimatecalculators.com
• www.thecalculatorsite.com/ﬁnance/
511
--- page 535 ---

512
Quantitative Financial Analytics
Table A.1. Time Value Equivalency Factors
Generator or
Cash Flow
Factor Name
Formula
Pseudo-Code
Diagram
Future value
(compound
amount factor)
F = P × (1 + r)N
same
Present value
factor
P = F × (1 + r)−N
same
Capital recovery
factor
P =
N
X
t=1
A
(1 + i)t
A = P/
X
(1 + i)−t
= P
i(1 + i)N
(1 + i)N −1
Present value of an
annuity factor
P =
N
X
t=1
A
(1 + i)t
= A
X
(1 + i)−t
P = A(1 + i)N −1
i(1 + i)N
Uniform series
compound
amount factor
F = A
N
X
t=1
(1 + i)t−1
= A(1 + i)N −1
i
Sinking fund factor
A =
F
PN
t=1(1 + i)t−1
= F
i
(1 + i)N −1
--- page 536 ---

Appendix A: Time Value of Money
513
It is perhaps more reasonable to code one’s own formulas which
will free the analyst from having to have access to the internet in
order to accomplish her job.
In Table A.1, i is the annual interest rate (in percent), and n
and t are usually the time index, with N being the total number of
(equally spaced) periods. We usually assume payments are at the end
of the (annual) periods; periods with more granularity are treated
in Chapter 2. Factor tables normally present the required factors
corresponding to $1 in future or present values.
Microsoft Excel formulas can be speciﬁed from the intrinsic
or online help for the present value and payment functions, PV
and PMT.
Internal Rate of Return (IRR) Calculation
When the payment streams are not identical, we must use the more
general equation PV = n
t=1
Pt
(1+r)t , where r is the discount rate (or
the to-be-determined IRR) and Pt are the net cash ﬂows each period.
The net present value (NPV) takes into account the initial investment
and can be expressed as NPV = −P0+PV (Pt) = −P0+n
t=1
Pt
(1+r)t .
Chapter 5 discusses the forecasting skills needed to estimate future
cash ﬂows, but it is usually the case that we are trying to solve for
the target rate of return r. Unlike the constant payment formulas
in Table A.1, in the general case, there are no closed-form solutions,
and the IRR must be solved iteratively.
Solution of the IRR arises from ﬁnding the roots of the nth order
polynomial that the NPV formula generates. Consider the case where
the initial investment is $10,000 and there are 2 periods of cash ﬂow.
With PV = P0 we have
P1
(1+r) +
P2
(1+r)2 = P0, or P1(1 + r) + P2 =
P0(1+r)2. Continuing, this is (P1 +P2 −P0)+(P1 −2P0)r−P0r2 = 0
which deﬁnes a parabola and can be written as C+Br+Ar2 = 0. The
nature of the two roots depends on the discriminant value, B2−4AC.
Suppose the two cash ﬂows are $3,000 and $4,000, respectively.
Our quadratic may be written as 10r2 + 17r + 3, with resulting
discriminant B2 −4AC = 169 = 132 > 0, yielding the two real roots
identiﬁed on Figure A.1. Indeed, for n = 2 we have the quadratic
--- page 537 ---

514
Quantitative Financial Analytics
Figure A.1. Quadratic IRR
formula giving the solution r = (−0.20, −1.5). Note that the ﬁrst
solution, −20 percent IRR, represents a loss on investment. The
second solution is not feasible and hence is disregarded.
Now let us suppose we have a negative cash ﬂow of $4,000 in year
two; the new IRR equation becomes 10r2 + 17r + 11 with a negative
discriminant, which has the imaginary roots r = −0.85 ± 0.614i. As
can be seen from the ﬁgure, its graph does not cross zero, but merely
has an inﬂection and functional minimum at r = −0.85.
In almost all practical problems, the number of cash ﬂows is
non-trivial, and the IRR equation must be solved iteratively. Multiple
roots can be obtained. Consider a project with four cash ﬂows:
P1
(1 + r) +
P2
(1 + r)2 +
P3
(1 + r)3 +
P4
(1 + r)4 = P0
P1(1 + r)3 + P2(1 + r)2 + P3(1 + r) + P4 = P0(1 + r)4
--- page 538 ---

Appendix A: Time Value of Money
515
(P1 + P2 + P3 + P4 −P0) + (3P1 + 2P2 + P3 −4P0)r
+ (3P1 + P2 −6P0)r2 + (P1 −4P0)r3 −P0r4 = 0.
These can be expressed as f(r) = z1 + z2r + z3r2 + z4r3 + z5r4 = 0
and we wish to solve for the resulting IRR value(s).
Project NPV with Uneven Cash Flows
Discount rate = 18.50115 percent
Year
1
2
3
4
Net Cash Flow
3,000
4,000
6,000
2,000
Discount rate
0.185
0.185
0.185
0.185
x PV factor
0.8439
0.7121
0.6009
0.5071
Present Value Cash Flows
2,531.62 2,848.49 3,605.65 1,014.24
Total PV of Cash Flows
10,000.00
Less Initial Investment
−10,000.00
Net Present Value
0.00
Using this data, we obtain two real and two complex roots, i.e.,
r∗= (0.1850115, −1.258 ± 0.6258i, −1.36812). We use the realistic
value of 18.5 percent in the table since the others are not feasible
(Figure A.2).
The three indicated inﬂection points (one real and two complex)
are obtained by:
d
drf(r) = z2 + 2z3r + 3z4r2 + 4z5r3 = 0, giving
r∗
f′ = (−0.24595, −1.2645 ± 0.359i).
The quartic polynomial is the highest degree that can be solved
algebraically; indeed Ferrari’s 1540 solution for the four roots requires
an entire page to transcribe. The discriminant alone is quite complex
--- page 539 ---

516
Quantitative Financial Analytics
Figure A.2. Quartic IRR
and can be used to determine which of nine cases the roots will satisfy.
In this appendix, we use the R language polyroot function, which is
an instance of the Jenkins–Traub (1972) iterative algorithm. Other
software such as the HP-12C’s ﬁnancial functions, Excel’s Solver, and
various other programs and apps can also solve these higher order
problems.
Since many pro forma ﬁnancial statements typically forecast out
5 periods, let us see what sort of roots the quintic polynomials
possess. We look at two possible scenarios outlined below.
Project NPV with Uneven Cash Flows
Year
1
2
3
4
5
Scenario 1
3,000
4,000
6,000
2,000
5,000
Scenario 2
3,000
4,000
−2,000
2,000
−1,000
--- page 540 ---

Appendix A: Time Value of Money
517
The roots for Scenario 1 (r∗
5) and Scenario 2 (r∗
5′) calculate to be:
r∗
5 = (+0.273, −0.835 ± 0.717i, −1.651 ± 0.549i)
r∗
5′ = (−1.87, −0.393 ± 0.66i, −1.018 ± 0.552i).
We note that for all positive cash ﬂows, there is a single positive
IRR value (27.3 percent), but for the case of 2 negative values,
there are no positive real roots. In another case (not shown), with
a single negative cash ﬂow, there were two negative roots. Thanks
to Descarte’s “Rule of Signs,” as can be seen from the polynomials
labeled on Figure A.3, the number of sign changes in Scenario 1 is
one, which means there is one positive real root (which there indeed
is); in the second scenario, there are no sign changes and hence we
see no positive real roots.
There is much current and historical interest in solving, ﬁnding
bounds for, or simply analyzing the roots of polynomials, and
Figure A.3. Quintic IRR
--- page 541 ---

518
Quantitative Financial Analytics
the interested reader is directed to any convenient encyclopedia of
mathematics for further knowledge.
Problems
1. The sum of $5,000 is placed in a savings account that pays
interest of 4 percent compounded annually. How much will be
in the account after 25 years?
2. What would your result be in the problem above if interest were
compounded quarterly (at the same 4 percent annual rate)?
3. Suppose this savings account paid interest of 4 percent (annually)
compounded daily. What would be the approximate amount in
the account after 25 years? What is the exact amount? What
is the exact amount net of annual income tax on earnings of
25 percent?
4. What is the annuity value of 25 payments of $100 at a rate of 10
percent per period?
5. What is the present value of $1,000 received 10 years from now
if interest is compounded annually at a rate of 6 percent?
6. What is the present value of $250 received in nine years if interest
is compounded annually at a rate of 8.5 percent?
7. The Atlantic Share Corp. has purchased stock in the Lambert
Co. It is expected that Lambert shares will be selling for about
$100 in 10 years and that Lambert will pay a dividend of about
two dollars per share over the next 10 years. If Atlantic wished
to earn 20 percent on its investment, how much should it have
paid for the Lambert shares?
8. The Ludmilla Corp. pays a dividend of one dollar per share and
expects to increase the dividend by ten cents per year for the next
ﬁve years. Ludmilla now sells for $20 per share. If an investor
wished to earn 10 percent on Ludmilla shares, at what price
would the stock have to sell in ﬁve years?
9. The Daland Shipping Corp. has paid a dividend of three dollars
per share to common stockholders for the past 20 years and
plans to continue doing so in the future. Prospects for growth in
the ﬁrm are negligible because the ﬁrm merely reinvests annual
--- page 542 ---

Appendix A: Time Value of Money
519
depreciation ﬂows and does not retain earnings or seek external
ﬁnancing. If investors believe Daland should yield 6 percent,
determine the market price of the shares.
10. A mortgage has a term of 25 years. The face value of the
mortgage is $30,000, and it has a yield to maturity of 4 percent. Assuming continuous compounding, what annual payment
should be made on the mortgage?
--- page 543 ---

This page intentionally left blank
This page intentionally left blank
This page intentionally left blank
This page intentionally left blank
--- page 544 ---

Appendix B
Financial Statistics
And Satan stood up against Israel, and provoked David to number
Israel. . . And David’s heart smote him after that he had numbered
the people. And David said unto Hashem, I have sinned greatly in
that I have done: and now, I beseech thee, O Hashem, take away
the iniquity of thy servant; for I have done very foolishly.
1 Chronicles 21:1, 2 Samuel 24:10
Probability, Random Variables, and Measures
of Location, Dispersion and Shape
A variable that eludes predictability but that has a speciﬁc range
or set of possible values and a deﬁnite probability associated with
each value is called a random variable. In ﬁnance, one makes
use of random variables frequently because many of the values
determined are based on future events. These are rarely known with
certainty, but with eﬀort, it may be possible to attach probabilities
to each possible outcome of a given future event. The assignment
of probabilities is generally a subjective matter, although the use
of statistical methods may reduce the uncertainty associated with
obtaining relative likelihoods.
An exhaustive set of probabilities attaching to all possible
outcomes of a given future event is called a probability distribution.
Suppose xi is the ith outcome of event X; then p(xi) is the probability
that X will take on the value p(xi). The probability distribution for
event X is given by p(x). For example, let event X be the price of a
stock in 10 years. If we can make educated guesses about the range
of prices at which the stock may sell and the relative likelihood for
521
--- page 545 ---

522
Quantitative Financial Analytics
each price, this range and the attaching probabilities constitute a
probability distribution.
One may generate several important measures from a probability
distribution. Perhaps the most important is the mean or expected
value, which is deﬁned as:
E(X) =

i
xip(Xi).
(B.1)
For an exhaustive distribution (where all possible values are speci-
ﬁed), 
i p(xi) = 1.
The expected value is a measure of central tendency and is
frequently the best value to assume for X for decision-making
purposes. There are other measures of central tendency, however,
that may be useful for speciﬁc types of decisions. The mode of a
distribution is that value of X with the largest p(xi). The median is
the value that is the midpoint in the distribution; that is, it is the
value that divides the distribution in half.
A second important characteristic that may be generated from a
probability distribution is the variance. The variance is deﬁned as:
V (X) = E(X −E(X))2 =

i
[xi −E(X)]2p(xi).
(B.2)
The variance is a least-squares measure of the degree of deviation
about the mean. Hence, it is often used as an indicator of the
“riskiness” of a distribution. The square root of the variance, the
standard deviation, is sometimes used in place of the variance as a
measure of deviation. (The symbols µ and σ are used to indicate
mean and standard deviation in many ﬁnance texts, although for
samples the symbols ¯x and s are more appropriate.) Note that the
units of the standard deviation are the same as for the data itself,
which is one reason it is so often used to describe spread of the values
of X.
Dispersion and risk are frequently used interchangeably in
ﬁnance. More concretely, however, three states of future events
should be delineated. In the ﬁrst state, that of certainty, we know
which value X will take. In this instance, [xi −E(X)] = 0, because
xi = E(X). When [xi −E(X)] = 0, V (X) also equals zero. This
--- page 546 ---

Appendix B: Financial Statistics
523
is the best of all possible worlds, but it rarely prevails in the real
world. The second state is that of uncertainty. This state exists
when  p(xi) < 1 or when probabilities cannot be assigned to given
values. When  p(xi) < 1, all possible outcomes are not known; the
distribution is not exhaustive; and V (X) is undeﬁned. This is an
intolerable state that must be altered if decisions are to be made.
The ﬁnal state, risk, obtains when p(xi)̸ = 1, but  p(xi) = 1. In
this case, we do not know which value X will take on, but we can
specify the probabilities that (X = xi), and all possible outcomes are
known (the distribution is exhaustive). Under conditions of risk, it
is clear that the greater V (X) becomes, the poorer estimate of the
ultimate outcome will be E(X), or any xi. Therefore, the greater the
dispersion of the distribution, the riskier the distribution becomes.
The variance and standard deviation are absolute measures of
dispersion. As such, they do not always provide a basis for good
comparisons. For example, suppose two stocks had expected prices
of $10 and $100, respectively, and standard deviations of $1 and
$5. If we examined only the standard deviation, the second stock
might appear riskier than the ﬁrst. On the other hand, the expected
value of the second is much greater than that of the ﬁrst. The
relative dispersion, hence, is actually larger for the ﬁrst stock. A good
measure of relative dispersion is the coeﬃcient of variation, which is
given by:
CV (X) =

V (X)
E(X) .
(B.3)
or σ/µ in terms of other frequently employed symbols. When we
compute the coeﬃcient of variation, we ﬁnd that for the ﬁrst stock,
σ/µ = 1/10; whereas for the second, σ/µ = 5/100. Using this relative
measure of dispersion, the ﬁrst stock is clearly the riskier.
Another type of relative measure of dispersion is the semivariance. This statistic indicates only the variability in the negative direction and places the following constraint on the variance
equation:
[xi −E(X)] < 0.
(B.4)
--- page 547 ---

524
Quantitative Financial Analytics
As a measure of risk, the semi-variance has the advantage of not
penalizing values that are better than expected.
The variance is known technically as the second moment about
the mean. There are higher-degree moments that may also be
signiﬁcant in ﬁnancial analysis. Associated with the third moment
is the notion of skewness. Skewness is a measure of the symmetry of
a distribution about its mean. A distribution that is not skewed is
said to be symmetrical. A distribution with a long left tail is said
to be negatively skewed. One with a long right tail is said to be
positively skewed (see Figure B.1). A measure of skewness is provided
by computing the third moment about the mean and dividing it by
the cube of the standard deviation:
SK = E
X −µ
σ
3
=

i[Xi −E(X)]3p(xi)
(

V (X))
3
.
(B.5)
In general, positive values for SK are preferred to negative ones. One
practical application is that positive skewness has been shown to be a
necessary but not suﬃcient condition for preference, ceteris paribus,
for all families of utility functions that meet the requirements for
third-degree stochastic dominance (deﬁned in Chapter 10).
Figure B.1. Examples of Skewness
--- page 548 ---

Appendix B: Financial Statistics
525
Figure B.2. Comparisons of Heterokurtotic Distributions
A ﬁnal measure that may be important is associated with the
fourth moment about the mean. Kurtosis measures the peakedness
of a distribution and the tail behavior.
A normal, bell-shaped distribution is said to be mesokurtic. One
that is ﬂatter than the bell-shaped curve is said to be platykurtic,
and one that is steeper is said to be leptokurtic (see Figure B.2).
A common measure of kurtosis is computed by dividing the fourth
power of the standard deviation (square of the variance) into the
fourth moment about the mean:
KU = E
X −µ
σ
4
=

i[xi −E(X)]4p(xi)
[V (X)]2
.
(B.6)
Larger values for KU indicate a more peaked distribution. KU for a
mesokurtic distribution is +3. Lower values indicate a platykurtic
distribution, and higher ones suggest a leptokurtic distribution.
There seems to be no general agreement on the relative desirability
of the degree of kurtosis, except that highly platykurtic distributions
may have inﬁnite moments which makes ﬁnancial analysis diﬃcult
to perform.
Examples
An analyst is attempting to forecast the earnings per share of
Dynamo Quebec Power Ltd. for next year. He believes that four
--- page 549 ---

526
Quantitative Financial Analytics
values are possible and that the relative likelihood of each is described
as follows:
x1 = $2.50;
p(x) = 0.3
x2 = $2.00;
p(x) = 0.4
x3 = $1.70;
p(x) = 0.2
x4 = $1.10;
p(x) = 0.1.
1. What is the expected value of earnings for next year?
($2.50) × (0.3) = $0.75
($2.00) × (0.4) = $0.80
($1.70) × (0.2) = $0.34
($1.10) × (0.1) = $0.11
E(X) = $2.00.
2. What are the mode and median values of the distribution? The
mode is the most likely value. At xi = $2.00, p(xi) is greatest. The
median divides the distribution in half. This occurs at xi = $2.00.
3. What is the standard deviation of the distribution?
2.50 −2.00 = 0.50; (0.50)2 →(0.250) × (0.3) = 0.075
2.00 −2.00 = 0.00; (0.00)2 →(0.000) × (0.4) = 0.000
1.70 −2.00 = −0.30; (−0.30)2 →(0.090) × (0.2) = 0.018
1.10 −2.00 = −0.90; (−0.90)2 →(0.810) × (0.1) = 0.081
V (X) = 0.174
σ =
√
0.174 = $0.42.
4. What is the coeﬃcient of variation of Dynamo Quebec earnings?
CV (X) = $0.42
$2.00 = 0.21.
5. What is the semi-variance of earnings?
xi −E(X) < 0
$0.018 + $0.081 = $0.099.
--- page 550 ---

Appendix B: Financial Statistics
527
6. Determine the symmetry of the distribution.
(0.50)3 →(0.125) × (0.3) =
0.0375
(0)3 →(0) × (0.4) =
0
(−0.30)3 →(−0.027) × (0.2) = −0.0054
(−0.90)3 →(−0.729) × (0.1) = −0.0729
−0.0408
SK = −0.0404
0.0730 = −0.56.
The distribution is negatively skewed.
7. Compute the kurtosis of the distribution.
(0.50)4 →(0.0625) × (0.3) = 0.01875
(0)4 →(0) × (0.4) =
0
(−0.30)4 →(0.0081) × (0.2) = 0.00162
(−0.90)4 →(0.6561) × (0.1) = 0.06561
0.08598
KU = 0.08598
0.03066 = 2.80.
The distribution is slightly platykurtic.
The Normal Distribution
A very important distribution for decision-making purposes is the
normal distribution. This distribution describes continuous value
data, and has the characteristics of being perfectly symmetrical and
mesokurtic. The mean, median, and mode for this distribution are
identical, because it is not skewed. Probability calculations involving
the normal distribution are easily made with tables such as the one
provided in Table B.2.
One convenient feature of the normal distribution is that about
2/3 of the distribution lies within one standard deviation of the
mean. Within two standard deviations is about 95 percent of the
distribution, and all but a fraction of 1 percent of the distribution
lies within three standard deviations of the mean (see Figure B.3).
--- page 551 ---

528
Quantitative Financial Analytics
Figure B.3. The Standard Normal Distribution
Another important data transformation usually associated with
the normal distribution is that of standardization. For a random
variable X, we subtract its mean E(X) and divide by its standard
deviation to obtain a new random variable Z whose mean is zero and
variance unity. That is, Z = X−µ
σ
= X−E(X)
√
V (X) . In the case of normal
data, the standardized data is also normal, with commensurate
(µ, σ) = (0, 1). Standardized data values are sometimes referred to
as z-scores. Care should be taken with non-normal data, however, in
that while it can be standardized with mean zero and unity variance,
its distribution will often be unknown.
A rather underappreciated property of the normal distribution is
the very low probabilities it assigns to rare events. For example:
z
P(Z ≤z)
z
P(Z ≤z)
−6
9.8659E-10
3
0.998650102
−5
2.8665E-07
4
0.999968329
−4
3.1671E-05
5
0.999999713
−3
1.3499E-03
6
0.999999999
--- page 552 ---

Appendix B: Financial Statistics
529
Examples
1. The short-run price (over the next month) of a stock is assumed
to be normally distributed with a mean of $20 and a standard
deviation of $3. The current price of the stock is $15. What is the
probability that the purchase of the stock will result in a loss by
next month?
This example shows the usefulness of standardization. We need
P(xi < 15). By standardizing the normal data we have
P(X < 15) = P
X −µ
σ
< 15 −20
3

= P(Z < −1.67),
which is easily obtained from Table B.2 as 0.0475. $15 is 1.67σ
below the mean, giving a z-score of −1.67. Values below $15 will
occur with a probability of about 5 percent.
2. It is believed that interest rates on high-grade utility bonds are
normally distributed. It is felt that the mean value for the ﬁrst
quarter of next year will be 8 percent with a standard deviation
of 1 percent. What is the probability that the rate on these bonds
will be no lower than 7 percent?
P(X ≥0.07) = 0.84.
This may be taken directly from Table B.1. The value 7 percent is
exactly one standard deviation from the mean. Hence, values less
than 7 percent will occur with a probability of about 0.16, and
values 7 percent or greater will occur with a probability of 1.00 −
0.16 = 0.84.
Notice that since the distribution is continuous, there is
no probability associated with a single point value, so that
P(X ≤x) = P(X < x), or P(X > x) = 1 −P(X ≤x).
Sampling and the t-Distribution
Except when dealing with elicited probabilities, it is almost always
the case that the analyst is using samples from a probability
distribution, whose parameters are in reality unknown. Therefore,
in most practical work, calculated parameters such as the mean and
