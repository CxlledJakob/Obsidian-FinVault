# Quantitative financial analytics_ the path to investment profits.pdf — pages 115–134

--- page 115 ---

92
Quantitative Financial Analytics
discussion, it should be obvious that money-market instruments
possess a fairly high level of substitutability for each other (on
both the supply and demand sides of the market), and thus any
change in treasury bill rates would be quickly reﬂected in the rates
of the other instruments. The basic topic of this book, however,
is long-term securities. Even here, as it was shown above, actions
of the government will aﬀect dividendand interest-paying ability.
A question arises, however, as to whether such policy actions have a
direct eﬀect upon long-term security prices, and the market rates of
return. To be speciﬁc, is there a mechanism through which changes
in short-term rates (or security prices) are also reﬂected in changed
long-term rates? This section is directed to that question.
The theory of the term structure of interest rates holds that
the observed market yield on otherwise identical securities may
be a function of the securities’ term to maturity. In other words,
market return may be dependent upon maturity as well as all the
other factors determining yield. Acceptance of this theory allows a
yield curve to be drawn as a valid functional relationship. Three
hypothetical yield curves are shown below. It is assumed that the
securities depicted on a given curve diﬀer only by maturity, not
by other risk factors (U.S. government bonds are often used in the
analysis for this reason). Curve A is called a ﬂat yield curve, curve B
is upward sloping, and curve C is downward sloping. The implications
of the slope of the curve and the exact relationship of maturity to
yield will depend upon which of the several term structure hypotheses
one is prepared to accept.
The pure expectations hypothesis of the term structure is the
simplest to understand. Let it be assumed that taxes and transaction
costs do not exist, all securities are riskless as to income (the coupon
will be paid), and all investors have identical expectations as to
future short-term interest rates (the model should also work if enough
investors at the margin share common expectations). It should then
follow that an individual wishing to invest in bonds for 10 years could
buy a series of 10 one-year issues, two ﬁve-year issues, a single 10-year
issue, or a 20-year issue to be sold at the end of 10 years. Assuming
the individual wishes to maximize proﬁts, such an investor would
--- page 116 ---

The Securities Markets and Macroeconomics
93
YIELD TO MATURITY
YEARS TO MATURITY
A
B
C
Figure 3.10. Three Hypothetical Yield Curves for Homogeneous Bonds which
Diﬀer Only by Maturity
presumably engage in that series of bond transactions promising the
greatest return.
Because everyone has been assumed to hold the same expectations, equilibrium would not be established until the returns on all
such courses of action were the same. At this point, one would earn
the same return for a 10-year investment in bonds whether he or
she bought a 10-year issue, a series of one-year issues, and so on.
As the expected short-term rates have been assumed to be agreed
upon, the pure expectations hypothesis essentially posits that longterm rates will adjust accordingly to maintain holding-period returns
constant.
Let:
Rn = average rate of return, compounded once per period, on a
bond maturing at the end of period n if purchased at the
beginning of period t;
rj = expectation in period t of the rate of interest on one-period
bonds purchased at the beginning of period j (note that if
t = j, the rate is known);
ρp,n = expectation in period t of the average rate of return, compounded once per period, on bonds bought at the beginning
of period p to mature at the end of period n.
--- page 117 ---

94
Quantitative Financial Analytics
Then, for an investment of n years to have a uniform expected
return regardless of maturity purchased:
(1 + Rn)n = (1 + rt)(1 + rt+1) · · · (1 + rn).
(3.16)
Equation (3.16) merely reaﬃrms that the value of the investment
after n years should be the same whether an n year bond or n oneyear bonds were bought; this equation is restated in more general
form as Equation (3.17). It illustrates that the average annual return
on the long-term bond is the geometric mean of the intervening
expected short-term rates:
Rn =


n

j=1
(1 + rj)


1/n
−1.
(3.17)
It should follow for any length of time n −k(k < n):
(1 + Rn−k)n−k = (1 + rt)(1 + rt+1) · · · (1 + rn−k).
(3.18)
Dividing Equation (3.16) by Equation (3.18) and rearranging terms,
we obtain:
(1 + rn−k+1)(1 + rn−k+2) · · · (1 + rn) =
(1 + Rn)n
(1 + Rn−k)n−k .
(3.19)
The information in Equation (3.19) tells us that, given the assumptions above, if we can observe the market rate on n-year (say, 10-year
bonds) and on n −k (say, seven-year bonds), then we have also
obtained information about the currently expected one-year yields for
the intervening period (years 8, 9, and 10). Furthermore, the pure
expectations hypothesis would imply that it is currently expected
that bonds with a maturity of k (three) years bought at the beginning
of year n −k + 1 (eight) would have an average yield equal to the
geometric mean of these expected one-year yields. Therefore:
(1 + ρn−k+1,n)k = (1 + rn−k+1)(1 + rn−k+2) · · · (1 + rn).
(3.20)
Substituting Equation (3.19) into Equation (3.20) we obtain:
(1 + ρn−k+1,n)k =
(1 + Rn)n
(1 + Rn−k)n−k ,
(3.21)
--- page 118 ---

The Securities Markets and Macroeconomics
95
or
ρn−k+1,n =
k

(1 + Rn)n
(1 + Rn−k)n−k −1.
(3.22)
Under the assumptions made, the investor could input the
current market rate on 10-year and seven-year bonds to the right
side of Equation (3.22) and obtain the market’s current expectation
of the rate on three-year bonds seven years from now. Before the
reader becomes unduly excited about the interest rate prediction
implications of Equation (3.22), a strong caveat is required. In the
ﬁrst place, it is necessary that the long-term rates be unbiased
estimators of expected intervening short-term rates (for example,
Equations (3.16)–(3.18) must hold); possible causes for this assumption to be unrealistic are considered below. Even if this condition
holds, however, Equation (3.22) solves only ρp,n (the rate currently
expected on bonds sold in p to mature in n), not Rp,n (the actual
rate in year p on bonds maturing in n). Thus, as a practical matter,
expectations may change over time or be wrong in the ﬁrst place
(possibilities assured away in formulating the model) such that
ρp,n̸ = Rp,n.
Example
Assume that riskless securities are available in ﬁve-year maturities to
yield 6 percent and three-year maturities to yield 5 percent. Under
all the assumptions of the pure expectations hypothesis, what is the
rate currently expected on two-year bonds three years hence?
n = 5; n −k = 3; k = 2; Rn = .06; Rn−k = .05
ρn−k+1,n =
k

(1 + Rn)n
(1 + Rn−k)n−k −1
ρ4,5 =
2

(1.06)5
(1.05)3 −1 =

1.338
1.158 −1 =
√
1.1554 −1 ≈7.5%.
Thus, it is currently expected that two-year bonds will sell at an
annual return of about 7.5 percent at the beginning of year four.
--- page 119 ---

96
Quantitative Financial Analytics
Term structure theory: Other hypotheses
and implications
In view of the discussion earlier in this chapter, the reader may be
wondering what impact inﬂation would have on the pure expectations
model. It should be borne in mind that the theory deals only with
nominal (market) rates of interest, not real rates. To the extent
that future inﬂation is anticipated, then, by the monetarist view the
expected one-year rates (rj) would be adjusted accordingly and, if
all the other assumptions held, the model would remain valid. The
problem arises, of course, if future inﬂation is incorrectly estimated.
In this case, unexpected inﬂation merely becomes another factor that
can cause expectations to change over time and cause the failure of
predictions made with Equation (3.22) to be fulﬁlled.
Another complication has been raised by a school of thought
associated with Sir John Hicks (1939). It can be shown that a
given change in the market rate of interest will have a greater
eﬀect upon the price of a bond the longer its term to maturity
(see the example below). Sir John and his followers argued that the
increased capital risk on long-term bonds makes lenders prefer shortterm issues and requires a liquidity premium in order to lend on a
long-term basis. Although short-term lending does reduce principal
risk, it increases income risk (the risk or what will be earned in
future periods) because the investor is then at the mercy of future
short-term rates. Hicks assumed the former is more compelling than
the latter. It is also maintained that borrowers prefer the security
of having money for long periods (thus not being forced into the
market at unseemly times) and are willing to pay this premium.
The result is the Hicksian liquidity preference version of the expectations hypothesis. This version contends that long-term rates reﬂect
expected future short-term rates plus a liquidity premium for lending
long and as such, are biased estimates upward of the expected future
short-term rate. Let:
Lj = liquidity premium required in period t to lend long term
rather than short term in period j.
--- page 120 ---

The Securities Markets and Macroeconomics
97
Then Equation (3.13) in liquidity preference form becomes:
(1 + Rn)n = (1 + rt + Lt)(1 + rt+1 + Lt+1) · · · (1 + rn + Ln).
(3.23)
The simplest comparison is with bonds maturing in year n −1:
(1 + Rn−1)n−1
= (1 + rt + Lt)(1 + rt+1 + Lt+1) · · · (1 + rn−1 + Ln−1).
(3.24)
Dividing Equation (3.13) by Equation (3.15) and simplifying, we
obtain:
rn = ρn,n =
(1 + Rn)n
(1 + Rn−1)n−1 −Ln −1.
(3.25)
It thus becomes obvious that we cannot even predict currently
expected rates much less actual future rates, without a complete
schedule of the liquidity premiums embodied in the long-term rates.
It can be shown from Equation (3.16) that, if future shortterm rates are expected to be constant (rt = rt+1 = · · · = rn),
then the long-term rate should be equal to the short-term rate
(Rn = rt = · · · = rn) for any term selected. This implies a ﬂat
yield curve for neutral expectations under the pure expectations
hypothesis. In like manner, if future short-term rates are expected to
rise from the current level (rt < rn), then the long-term rate, as the
geometric mean of the short-term rates, should be greater than the
current short-term rate (Rn). This implies an upward sloping yield
curve. The liquidity preference version implies an upward sloping
yield curve even under neutral expectations, however. Remember
that even if short-term rates are assumed constant in Equation (3.23)
the existence of the liquidity premiums (the L terms, assumed to be
positive increasing with n) assures that Rn will rise as n increases.
Thus, an upsloping yield curve does not mean that rates must rise in
the future or necessarily that people think they will; it may merely
represent neutral expectations and liquidity preference.
Note should be taken of the behavior of the yield curve over an
interest rate cycle. If there exists some concept of the “normal” level
of interest then it should follow that when rates are “low” relative
--- page 121 ---

98
Quantitative Financial Analytics
to the norm, the yield curve should be upward sloping. The mere
fact that future short-term rates are expected to be higher than
current rates would cause the long-term rate to exceed the shortterm rate by the analysis given above for the pure expectations case.
Under the Hicks’ version, the upslope should be greater than that for
liquidity preference under neutral expectations. Likewise, at “high”
interest rate levels, the curve would be downward sloping under the
pure expectations model and moderately upward sloping, ﬂat, or
downward sloping (depending upon how “high” the rates are) under
the liquidity preference version.
The null hypothesis with regard to term structure theory is the
market segmentation, or institutional pressure, theory. Advocates of
this theory contend the market at each maturity level (especially
long-term versus short-term) is populated by borrowers and lenders
who, because of the nature of their operations, legal restrictions, and
so on, ﬁnd it very diﬃcult to operate at any other maturity level.
As a result, it is contended, the markets at diﬀerent maturity levels
are segmented from each other. Long and short rates would thus be
determined by supply and demand conditions within their respective
markets and, at least within broad limits, would have no necessary
relationships to each other. A yield curve would represent a specious
functional relationship, and no information at all could be derived
from its slope.
Now that we have come full circle from establishing the concept
of term structure to discrediting it, perhaps it is time to reassess.
The yield curve in the U.S. has been fairly generally upward sloping
since the end of World War II. Rates have risen during this period,
but not by enough to justify the slope. During the late 1970s, the
hyperinﬂation induced by the ﬁscal and monetary policies of the
Carter administration produced an incredible yield curve inversion
with short rates being many basis points above long rates. With
this exception, however, the downslope when rates were at cyclical
peaks has not been nearly as steep as the upslope when rates were
“low.” This casual evidence, plus a good bit of empirical work, tends
to indicate that the liquidity preference version may be more useful
than the unmodiﬁed pure expectations hypothesis.
--- page 122 ---

The Securities Markets and Macroeconomics
99
Predictions made on the basis of even the liquidity preference
version have turned out badly, however. The fact that the implied
rates diﬀer from the actual rate (ρp,n̸ = Rp,n) does not disprove the
theory, of course; people could simply be wrong in their expectations.
To assume that they are wrong consistently, however, is not very
appealing. Nor is it terribly inviting to join the market segmentationists; it is diﬃcult to accept that the most fungible of all commodities
could be traded in such imperfect markets. Other models have
assumed that people change their expectations of future rates on the
basis of errors they make in estimating past rates. This error-learning
model is fairly successful in explaining rate changes. Although these
models are based on the pure expectations hypothesis, they are
consistent with the liquidity preference version as well.
Examples
l. Assume that a 3 percent bond, paying interest semiannually, is
selling at par. If the rate of interest goes to 4 percent, what would
happen to price of the bond if its maturity were:
a. one year
b. 10 years
c. never (a perpetual bond)
Period
Payment
@2%/Period
P.V.
a.
1
$15
0.98
$14.70
2
1,015
0.961
975.42
990.12
b.
1–19
$15
15.678
$235.17
20
1,015
0.673
683.1
$918.27
c.
$15/.02 = $750
2. Assume that expected one-year rates are as follows: Year one,
4 percent; year two, 5 percent; and year three, 6 percent. Assume
--- page 123 ---

100
Quantitative Financial Analytics
further that a lender requires a liquidity premium of 0.2 percent
to lend two years instead one and that this premium grows at a
compounded rate of 6 percent as the term of the loan increases.
a. What are the market rates on twoand three-year bonds?
(1 + Rn)n = (1 + rt + Lt)(1 + rt+1 + Lt+1)
(1 + R2)2 = (1 + .04 + 0)(1 + .05 + .002)
R2 =
√
1.09408 −1 = 4.6%
(1 + R3)3 = (1 + .04 + 0)(1 + .05 + .002)(1 + .06 + .00212)
(1 + R3)3 = (1.04)(1.052)(1.06212) = 1.162044
R3 =
3√
1.162044 −1 = 5.1%.
b. If four-year bonds are yielding 6 percent, what is the implied
one-year rate for year four?
ρ4,4 = (1 + R4)4
(1 + R3)3 −L4 −1
ρ4,4 = (1.06)4
1.1620 −(.002)(1.06)2 −1
ρ4,4 = 1.262
1.162 −(.002)(1.124) −1
ρ4,4 = 1.086 −.002 −1 = 8.4%.
Summary
In this chapter, we have outlined the major characteristics of the
money and capital markets. We have also observed the conﬂicting
eﬀects of both monetary and ﬁscal policies upon the securities
markets. Increases in government spending (or business investment),
by increasing aggregate demand, tend to put upward pressure on
security prices; yet, the increased supply of securities issued to
ﬁnance such spending exerts downward pressure on prices. Likewise,
increases in the money supply, by making money more plentiful
in the portfolio relative to securities, tend to push security prices
--- page 124 ---

The Securities Markets and Macroeconomics
101
upward (rates downward); yet, constant infusions of money can fuel
inﬂationary expectations and drive rates up.
All the above contradictions indicate the diﬃculty of determining
the ﬁnal eﬀects of changes in macroeconomic variables. Nevertheless,
because these variables are essential determinants of the risk and
return patterns evidenced by individual securities, the analyst must
assess them as best he or she can. The issue of the term structure
of interest rates continues to be a debatable one with economic,
econometric, and statistical models all failing to really capture the
observed shapes and dynamics as the interest rate cycles unfold.
Problems
1. Find the price and yield on a treasury bill:
a. due in 30 days on a 4 percent basis.
b. due in 180 days on a 5 percent basis.
c. due in 150 days on a 6 percent basis.
2. Refer to 1, above:
a. Suppose you bought the bill in 1(b) and were selling it 30 days
later as per 1(c). What return did you earn?
b. Would you have been wiser to elect 1(a)?
c. Would your answer to 1(a) change depending upon whether
the bill were originally a 91- or 182-days bill? Why?
d. What return on a tax-exempt security would be equivalent to
1(a), (b), and (c) if the investor’s tax rate were 30 percent
and 60 percent?
3. In the example of the NKV Trust in the chapter, suppose it
decided not to cover the transaction and instead to sell the Dak
at the end of six months for whatever the going rate was at the
time. What would their return have been if the exchange rate at
the time were 30:1? 35:1? 50:1? Why is an uncovered transaction
inconsistent with the basic function of the money market?
4. Compute the annual return, on both a covered and uncovered
basis, of the purchase of $10M, 90-day U.K. Treasury bills at
--- page 125 ---

102
Quantitative Financial Analytics
9 percent if the spot pound is $2.40 = £1, and the 90-day forward
pound is $2.35, if the actual spot rate in 90 days is:
a. $2.40 = £1
b. $2.30 = £1
c. $2.50 = £1.
5. A bond has a coupon yield of 5 percent (that is, pays $50.00 per
year on a par of $1,000), matures in 20 years, and sells for 80.
Compute the yield to maturity of the bond using the discount
tables and the shortcut formula. Compare your results.
6. Mr. Elgar has bought stock in the Pomp and Circumstance Corp.
The ﬁrm pays a dividend $1.00 per share per year. Elgar feels
that this dividend will be maintained over the 10 years he plans
to hold the stock. If Elgar paid $25.00 per share and sold his
stock for $30.00 per share in 10 years what is his expected yield
from holding the stock?
7. Suppose Mr. Aged (see the example in the chapter) is expected
to live 10 years and 10-year securities yield 8 percent. Would this
change the solution?
8. Mr. Ronson (see example in the chapter) is also contemplating
the purchase of a 10-year security of the Ziﬀgovernment. The
Ziﬀtrade at 50 to the dollar and could trade at 40 to the dollar
at the end of 10 years with a probability of 0.2. Gross yield
is 12 percent, with 30 percent withholding treated as a credit
on U.S. taxes. The IET is 5 percent. Determine Mr. Ronson’s
expected return.
9. The Lafarge Corporation has a 40 percent tax rate and is contemplating the purchase of securities of the Camus Corporation.
Camus’s 20-year, 7 percent debentures are selling at 95, while
the preferred (6 percent) is selling at par. What is the return on
each security? Which should be purchased? Why? Would your
answer change if Lafarge were a tax-exempt institution?
10. Ignoring taxes and transfers, if b = 0.9 and ∆I = $5 billion, what
is ∆Y ?
11. If b = 0.7, Z = 0.1, and ∆G = $1 billion, what is ∆Y ?
12. If b = 0.7, t = 0.2, tr = 0, and ∆G = $5 billion, what is ∆Y ?
--- page 126 ---

The Securities Markets and Macroeconomics
103
13. Answer 12 assuming tr = 0.1.
14. If A = $100 billion, b = 0.8, t = 0.2, and tr = 0, plot the S + T
curve.
15. If ¯G = $50 billion, B = $40 billion, and g = $3 billion per
1 percent ∆i, graph the G + I curve.
16. Given the data in Problems 14 and 15, graph the IS curve.
17. What would happen to the IS curve derived in Problem 16 given
each of the following:
a. t becomes 0.25;
b. ¯G becomes $60 billion;
c. G becomes $4 billion per 1 percent ∆i;
d. b becomes 0.85?
18. In a loanable funds framework, determine the eﬀect of each of
the following changes upon the equilibrium rate of interest:
a. an increase in the federal government’s deﬁcit;
b. an increase in the marginal propensity to consume;
c. an increased aversion on the part of localities to go into debt
to pay for trains that “go to nowhere;”
d. a decrease in businessman’s expectations of future proﬁt to
be earned from investment projects;
e. a public lack of conﬁdence in the future manifesting itself in
the form of an increase asset demand for money;
f. a federal deﬁcit partially ﬁnanced by the sale of bonds to the
Federal Reserve, causing an equivalent increase in the money
supply.
19. Interpret the above events in a Keynesian framework, what
diﬀerences, if any, do you ﬁnd? Why?
20 If l = 0.2 and m = $10 billion per 1 percent ∆i, J = 170 billion,
and M = $200 billion, construct the LM curve.
21. Given the data in the Problems 16 and 20, determine the
equilibrium level of Y and i.
22. Assume the GDP = $800 billion, M = $200 billion, Vo is
constant, and the current level of output represents 95 percent of
full employment. Give a monetarist explanation of what would
happen if M were increased to $200 billion.
--- page 127 ---

104
Quantitative Financial Analytics
23. Assuming the facts in Problem 22:
a. If the long-run real rate of interest is 3 percent and the former
pure rate of interest was 5 percent, what should happen as a
result of the increase in M?
b. What should happen if a 10 percent increase in M were
expected to become an annual event, while the increase in real
output at full employment (caused by improved technology
and population growth) were estimated at 4 percent?
24. A former U.S. Secretary of the Treasury analyzed a stock market
collapse this way: “The stock market decline reﬂects the smart
people being convinced they don’t need common stocks as a
hedge against inﬂation. Our economic policies have broken the
back of the rampant price increases of recent years.” Discuss the
merits of the secretary’s argument.
25. Assume that the following one-year interest rates are anticipated:
Year
Rate
1
5%
2
10%
3
5%
4
20%
a. If $100 were invested in one-year bonds at the beginning of
year one, to what amount will it grow by the end of year four?
b. What annual rate of interest would a four-year bonds need to
oﬀer to be competitive?
c. Answer b for a three-year bond sold at the beginning of
year two.
d. Answer b for a two-year bond sold at the beginning of year
three.
e. Answer b for a three-year bond sold at the beginning of
year one.
f. At what price would bond in b sell at the end of year two?
Year three?
--- page 128 ---

The Securities Markets and Macroeconomics
105
g. How would your answer to f change if, during year two, the
expected rate in year four declined to 15 percent?
26. Riskless bonds are currently selling as follow:
Yield
Maturity
6%
5 years
7%
6 years
8%
7 years
Employing the pure expectations hypothesis:
a. What is the expected one-year rate ﬁve years from now?
b. What is the expected two-year rate ﬁve years from now?
c. What is the expected one-year rate six years from now?
27. If 25-year riskless bonds yield 4 percent, and 10-year bonds yield
6 percent, what is the expected 15-year rate 10 years hence under
the pure expectations hypothesis?
28. Suppose the long-run real rate of interest is expected to be
3 percent. In addition, there is expected to be inﬂation of
3 percent in year one, 2 percent in year two, 1 percent in year
three, and none thereafter. In a monetarist pure expectations
framework, what rate of interest would be currently observable in
the market on (a) one-year bonds; (b) three-year bonds; (c) 10-
year bonds? If, in the next instant, the market also began to
expect 2 percent inﬂation in year four, what would happen to
the price of the three bonds?
29. Suppose that a 6 percent riskless security is currently selling at
par and pays interest semiannually. If the interest rate were to
drop to 4 percent, what would be the eﬀect upon the price of the
bond if its maturity were (a) six months; (b) one year; (c) ﬁve
years; (d) 10 years; (e) 15 years; (f) perpetual?
30. a. Rework Problem 29 under the assumption that the interest
rate went from 6 to 8 percent.
b. Graph both sets of prices obtained against maturity.
--- page 129 ---

106
Quantitative Financial Analytics
c. Suppose that in the next instant there is a 0.5 probability that
the rate will stay at 6 percent, a 0.25 probability that it will go
to 8 percent, and 0.25 probability that it will go to 4 percent.
(1) What is the expected value of the interest rate level and
the price of the 6 percent bond that corresponds to it?
(2) What is the expected value of the price of the 6 percent
bond at each maturity level?
(3) Which maturity would you prefer to hold in this case?
d. Can you now explain what ﬁnancial economists mean when
they discuss how asymmetrical distribution of expected
interest rates will result in an asymmetrical distribution of
expected bond prices?
e. What slope of the yield curve has been assumed in this
problem? Are the assumptions concerning interest rate expectations consistent with this slope? Does it seem likely that this
slope could be maintained? Why?
f. May changes in interest rates and inverse changes in bond
prices be used interchangeably in capital market analysis as
though they were equivalent?
31. Under the liquidity preference version, assume that lenders
require a premium of 0.1 percent to lend for two years instead
of one (L2 = 0.1 percent) and that this premium grows at
a compound rate of 10 percent per year for each additional
year they must lend long (that is, L3 = (0.1 percent)(1.10) =
0.11 percent). Under this assumption, rework Problem 26.
32. In a pure expectations framework, assume that currently
expected one-year rates are:
Year
Rate
1
3%
2
4%
3
5%
4
6%
5
7%
--- page 130 ---

The Securities Markets and Macroeconomics
107
Graph the yield curve (up to ﬁve-year bonds) implied by the
data. Rework assuming the order of the rates is reversed.
Assuming that expectation are fulﬁlled, what will the ﬁrst four
years of the yield curves drawn in a and b look like next year?
33. Rework Problem 32 employing the liquidity preference assumptions of Problem 31. Compare your results by placing the
corresponding curves on the same graph. What is the eﬀect of
the presence of liquidity preference?
References
Barro, R. J., Modern Business Cycle Theory. Cambridge, MA: Harvard
University Press, 1989.
Coyle, D., GDP: A Brief but Aﬀectionate History. Princeton: University
Press, 2014.
Davidson, P., Post Keynesian Macroeconomic Theory: A Foundation for
Successful Economic Policies for the Twenty-First Century, 2nd edn.
London: Edgar Elgar, 2011.
Friedman, M., The Supply of Money and Changes in Prices and Output,
Testimony of Congress, 1958.
Friedman, M., A Program for Monetary Stability. New York: Fordham
University, 1960.
Friedman, M. and Anna Schwartz, A Monetary History of the United States,
1867–1960. Princeton, NJ: Princeton University Press, 1963.
Fisher, I., The Purchasing Power of Money. New York: Macmillan, 1922.
Gilman, M., Robert E. Lucas, Jr.’s Collected Papers on Monetary Theory.
Cambridge: Howard University Press, 2013.
Hicks, J., Value and Capital, 2nd edn. London: Oxford University Press,
2001 (ﬁrst published 1939).
Keynes, J. M., The General Theory of Employment, Interest and Money.
New York: Harcourt, Brace and World, 1936.
Marshall, A., Money, Credit and Commerce. London: Macmillan, 1922.
Sargent, T. J., “Robert E. Lucas, Jr.’s Collected Works on Monetary
Theory,” Review Article, Journal of Economic Literature, March 2015,
pp. 43–64.
Taylor, J. B. and M. Woodford, eds. Handbook of Macroeconomics.
Amsterdam: North Holland, 1999.
--- page 131 ---

This page intentionally left blank
This page intentionally left blank
This page intentionally left blank
This page intentionally left blank
--- page 132 ---

Chapter 4
Financial Statement Analysis
Now what I want is, Facts. Teach these boys and girls
nothing but Facts. Facts alone are wanted in life. Plant
nothing else, and root out everything else. You can only
form the minds of reasoning animals upon Facts; nothing
else will ever be of any service to them . . . Stick to the
Facts, sir!
Charles Dickens, Hard Times (1854)
Ratio Analysis
In this chapter, we begin the process of analyzing individual securities. The culmination of our eﬀorts will be the estimation of the
variables needed to build an optimal portfolio: expected returns,
variances, and covariances. In Chapter 5, some useful techniques for
obtaining measures of these variables will be discussed. Additional
procedures will be developed in later chapters.
The art of ﬁnancial analysis has depended for years on the
computation of ratios of data from the published ﬁnancial statements
of corporations (for example, balance sheets, income statements, cash
ﬂow statements, and so on). The earliest attempts at evaluating
a ﬁrm and its securities were mainly qualitative assessments and
shrewd guesses. These early attempts were succeeded by the computation of a growing battery of comparative ﬁnancial statistics.
These comparisons were of two kinds: comparisons over time and
comparisons among diﬀerent variables at the same time. The ﬁrst
form yielded simple but important information. As an example,
suppose ABC Corp. earned $125,000 last year and $150,000 this
109
--- page 133 ---

110
Quantitative Financial Analytics
year. The computation of a simple ratio [(This Year Sales −Last Year
Sales)/(Last Year Sales)] would show that sales were up by 20 percent
[($150,000−125,000)/($125,000)]. Although such a comparison is
extremely crude in that it gives no clue as to why sales increased
or whether such an increase will be sustained in the future, it is
nonetheless a very signiﬁcant ﬁrst step in analyzing the ﬁnancial
position of the company. The second form of comparison is one among
variables. Suppose ABC had sales this year of $150,000 and net
income of $15,000. A comparison of these data would show that net
income was 10 percent of sales. This information by itself may not be
terribly useful, although if it were observed that such a relationship
had held fairly steadily over time, perhaps a meaningful conclusion
could be drawn.
Ratio comparisons have been made and can be made whenever
it makes sense to examine the relationship between two or more
ﬁnancial numbers. There is nothing sacrosanct about any given
set of ratios, and diﬀerent comparisons may be necessary when
conditions diﬀer. Nevertheless, there is some advantage in attempting
to standardize the computation of ratios whenever possible. Hence,
ﬁnancial analysts have developed a core of ratios that may be used
in determining such things as the current ﬁnancial condition of the
ﬁrm, the trend in the ﬁrm’s ﬁnancial condition, and the ﬁnancial
condition of the ﬁrm in relationship to the position of other ﬁrms.
The information content of ratios and their use in determining
the risk position of the ﬁrm and the expected rates of return on
the ﬁrm’s securities will be the focal point of this chapter. In the
paragraphs that follow we present most of the basic ratios that the
ﬁnancial analyst may require. Additional ratios for unique industries
are also given.
A number of interest groups, including internal management,
may ﬁnd ratios a useful guide for policy making. We shall focus
here, however, on the use made of them by investors. Hence, we shall
examine each category of ratios as they may apply to the evaluation
of the securities of the ﬁrm. We name the ratio and provide a brief
description of what its purpose is.
It should be observed that there was a time when searching
for data and calculating ratios occupied most of an analyst’s time.
--- page 134 ---

Financial Statement Analysis
111
Today, however, the ubiquity of cheap computing power has made
the collection, dissemination, recapture, and possibly subsequential
analysis much, much easier. Computers record vast quantities of
company information and relay these data to the analyst upon
command. Data providers such as Standard & Poor’s Corporation,
Compustat, Capital IQ, Factset, and many others can provide
data such as 25 years of all balance sheet, income statement and
statements of cash ﬂow data at the press of a button. It is now
possible to compute all 45 ratios (and more) given below, along with
hundreds of other data elements, in seconds. Hence, the unpleasant
eﬀort of collection can be done painlessly in virtually no time. The
analyst, must therefore spend more time analyzing and thinking how
applicable the data in hand really is.
Financial Statements
Before we can delve into even the most common ratios, it is necessary
to understand the basics of ﬁnancial statements. These documents
show the ﬂow of revenues and proﬁts for a company over a period of
time, say a year, and the ﬁnancial position of the company at a given
date in time. The ﬁrst of these is called an income statement and the
second is called a balance sheet. The best way to become familiar with
both statements is by examining a set. On the two pages to follow are
income statements and balance sheets for American Funeral Supplies
(AFS), Inc. This ﬁctional company was founded in 1984 to supply
various ﬂuids, clothing, caskets, burial markers, and monuments to
independent funeral directors. AFS went public in 2010, and has
reported four complete years of statements ﬁled with the SEC.
The company is headquartered in New Orleans and has sales
of just under $7 billion. From its founding over 30 years ago,
revenues (sales) have grown from less than $10 million to the present
levels, or a compounded rate (taken from an HP-12C calculator) of
24.4 percent. Much of this growth has come from acquiring smaller
companies in the same line(s) of business. The remaining sales growth
has been generated by internal revenue development eﬀorts and
extensive marketing. Local funeral directors are called on regularly by
American salesmen. Extensive entertainment is also done to cement
personal relationships which are vital in this business.
