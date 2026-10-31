# Quantitative financial analytics_ the path to investment profits.pdf — pages 552–571

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
--- page 553 ---

530
Quantitative Financial Analytics
variance must be determined (estimated) from the sample. Examples
of estimators would include the sample mean ¯X = 1
n
n
i=1 Xi and
sample standard deviation S =

1
n−1
n
i=1 (Xi −¯X)2; analogues for
the skewness and kurtosis are calculated similarly. These statistics
are easily calculated in software. Statistical inference on many
problems such as the population mean is facilitated using the
so-called t-distribution. Suppose we have normal data for X, and
we are interested in testing for or ﬁnding conﬁdence limits for the
true population mean E(X) = µ. It turns out that the sample mean
is unbiased, that is, E( ¯X) = µ also. Additionally, recall that the
standard deviation of the sample mean is σ/√n. If we standardize
the sample mean as Z =
¯
X−µ
σ/√n, we ﬁnd that Z is normally distributed
with mean zero and unity variance, so it is easy to evaluate statistical
statements about the sample mean by using the z-table in Table B.2.
Unfortunately, we do NOT KNOW σ! If we used the sample
standard deviation s, the resulting standardized distribution is NOT
normal. It is, however, easy to work with since we can use a t-table
to do the job. The t-distribution is very similar to the normal
distribution except that it has no parameters other than the degree of
freedom ν. In the case of ¯X, the ν = n −1. Algebraically, Z =
¯
X−µ
s/√n
is distributed tn−1. For very large sample sizes, the t-distribution
approaches the standard normal. For small sample sizes, it becomes
more platykurtic until at n = 1 it becomes what is known as the
Cauchy distribution, with no ﬁnite moments at all; see Figure B.4
for a graphical comparison.
Examples
1. Suppose that the mean interest rate value on the high-grade utility
bonds for the ﬁrst quarter of next year is expected to be 8 percent,
and that the sample standard deviation of s = 1 percent has been
obtained based on a sample of size 10. What is the probability
that the rate on these bonds will be no lower than 7 percent?
P(X > 0.07) = P
X −0.07
0.01
> 0.07 −0.08
0.01

= P(T > −1).
--- page 554 ---

Appendix B: Financial Statistics
531
Figure B.4. Normal and t-Distributions Compared
Note that the t-score is equal to the z-score in the previous
example, but since we have substituted s for σ in the standardization, the t-distribution is required. Since we did, we need the
probability that t10 ≤−1. In Table B.2, the closest probability
corresponding to 1.0 in the ν
= 10 row is 0.15, giving an
answer of 85 percent. A more exact value could be obtained from
interpolation in the table, or better, from using software to look
up the actual value of 0.1705, giving a ﬁnal result of 83 percent.
This is slightly lower than the 84 percent probability obtained in
the previous normal example, reﬂecting the greater variability of
the t statistic due to the introduction of another statistic, s, in
the denominator of the standardization.
Diﬀerences of many multi-millions of dollars can be based on
a single decimal place value, indicating that, as in this case, it
is vastly superior to use the t-distribution when the population
standard deviation is not known. Since software is ubiquitous and
required in most cases anyway, one should almost always use the
t-distribution in numerical work.
2. It is believed that daily percent stock market returns of CAT stock
are normally distributed. Suppose we have observed 20 days of
--- page 555 ---

532
Quantitative Financial Analytics
market activity (1 month), and have estimated the sample mean
(daily) return to be 0.0716 percent, or 7.16 basis points (bps), with
sample standard deviation of 2.212 percent. Obtain a 90 percent
conﬁdence interval for the unknown mean population return based
on the original data.
A common conﬁdence interval formula for t-distributed data
can be written as µ
∈
¯x ± (tn−1, α
2 )(s/√n). In this case,
¯x = 0.000716, s/√n = 0.02212/
√
20 = 0.00507, and the t19,.05
critical value is obtained from Table B.2 as 1.729, giving the
90 percent conﬁdence interval as µ ∈0.0716 ± 1.729(0.5074) =
(−0.81%, 0.95%). Since the conﬁdence interval spans zero, we
cannot be statistically certain that the true mean return itself
is diﬀerent than zero. A larger sample size would be required to
better answer the question. Using a year of trading data (ν = 251)
gives a standard error s/
√
251 = 0.0014 versus 5.07 bps, resulting
in a 90 percent conﬁdence interval for µ of 6.9–7.4 bps.
Covariance
The covariance of two random variables Y and X is deﬁned as:
Cov(X, Y ) = E[(X −µX)(Y −µY )].
(B.7)
Expanding, we ﬁnd:
Cov(Y, X) = E[(XY −Y µX −XµY + µXµY )]
= E(XY ) −µXµY −µXµY + µXµY
= E(XY ) −µXµY .
(B.8)
The covariance gives some indication of how two random variables
will vary together.
The correlation coeﬃcient and the covariance of two random
variables are related in the following way:
ρxy = Cov(X, Y )
σxσy
,
(B.9)
which may be rewritten as:
Cov(X, Y ) = ρxyσyσx.
(B.10)
--- page 556 ---

Appendix B: Financial Statistics
533
Suppose the future performance of two stocks, X and Y , is being
considered. Stock X is believed to perform quite favorably under
bull market conditions, and an investment in it should produce a
handsome proﬁt. Under bear market conditions, however, this stock
should do very badly, and the investment would show a sizeable loss
in this case. Stock Y , on the other hand, will do moderately well in
a bull market, but will remain at current levels even if the market in
general does rather poorly. A return matrix under the two possible
market conditions is given below:
Market Condition
Probability
Proﬁt Stock X
Proﬁt Stock Y
Bull Market
.5
$4,000
$1,000
Bear Market
.5
−2,000
–0–
The independent expected value and variance for each stock
would be:
Stock X : (0.5)(4,000)
=
2,000
(0.5)(−2,000)
=
−1,000
E(X)
=
1,000
(4,000) −(1,000) = (3,000)2 →9,000,000(0.5) = 4,500,000
(−2,000) −(1,000) = (−3,000)2 →9,000,000(0.5) = 4,500,000
V (X) = 9,000,000
Stock Y : (0.5)(1,000)
=
500
(0.5)(0)
=
0
E(X)
=
500
(1, 000) −(500) = (500)2 →250, 000(0.5) = 125,000
(0) −(500) = (−500)2 →250, 000(0.5) = 125,000
V (X) = 250,000.
The covariance between the two investments would be:
Cov(X, Y ) = E(XY ) −µXµY
E(XY ) = (4,000)(1,000)(0.5) + (−2,000)(0)(0.5) = 2,000,000
--- page 557 ---

534
Quantitative Financial Analytics
µXµY = (1,000)(500) = 500,000
Cov(X, Y ) = 2,000,000 −500,000 = 1,500,000.
The correlation coeﬃcient between the investments is given by:
ρxy = Cov(X, Y )
σxσy
=
1,500,000
(3,000)(500) = 1,500,000
1,500,000 = 1.00.
Notice that when the two variables are correlated using only two
values for each variable, the loss of degrees of freedom forces a
correlation coeﬃcient of unity.
In the case of samples, we deﬁne the sample covariance as:
SXY =
1
n −1
n

i=1
(Xi −¯X)(Yi −¯Y ).
With simplifying formula:
(n −1)SXY =

XiYi −¯X

Yi −¯Y

Xi + n ¯X ¯Y
=

XiYi −n ¯X ¯Y .
. We can then deﬁne the sample correlation coeﬃcient as the ratio of
the sample covariance divided by the product of the sample standard
deviations; i.e., rxy =
Sxy
SxSy .
Regression and Correlation Analysis
The relationship between two or more random variables may be
described through the use of a technique called regression analysis.
When only two variables are involved, the analysis is referred to
as simple regression. When more than two variables are involved,
the term multiple regression is applied. In order to determine the
closeness of the relationship between variables, one variable must
be selected as the dependent variable. This choice is important and
will depend on the nature of the variables. The other variables are
said to be independent. With the establishment of the dependent and
independent variables, a least-squares trend line may be computed.
This line may take the form of a linear equation, if it is believed that
--- page 558 ---

Appendix B: Financial Statistics
535
the relationship between the variables is linear, or it may take the
form of a non-linear equation.
Suppose we wish to establish the relationship between two
variables, Y and X. Suppose further that we believe X to be the
independent variable and Y to be the dependent one. We may
establish a general equation of the form Y = f(X). Now, let us try
to decide what form the equation should take. One method of doing
this would be to prepare a simple scatter diagram plotting pairs of
points representing Y and X values (see Figure B.5). In the case of
our general equation above, we shall assume that the relationship
appears to be more or less linear. Thus, we shall be ﬁtting a linear
least-squares trend line when we regress Y against X.
The properties of the least-squares trend line may be described
by two equations:

(Y −ˆY ) = 0

(Y −ˆY )2 = minimum,
where Y are original observations, and ˆY are trend-line computed
values.
The ﬁrst equation assures that the positive and negative deviations of observed values Y from trend values ˆY exactly balance out.
The second equation guarantees a “best ﬁt” in that the sum of the
squares of the deviations about this line is smaller than for any other
line. It should be noted that the properties of the least-squares trend
line are the same as those of the arithmetic average (mean) for a
probability distribution.
The equation for a straight line (linear relationship) is of the form
Y = a+bX. Hence, we need to ﬁnd values for a and b that will satisfy
the properties detailed in Equations (B.7) and (B.8). This may be
done by solving two additional equations called normal equations.
The ﬁrst normal equation is obtained by multiplying the general
equation through by the coeﬃcient of the ﬁrst constant and summing
(note that the coeﬃcient of a is one):
Y = a + bX

Y =

a +

bX.
--- page 559 ---

536
Quantitative Financial Analytics
Figure B.5. Scatterplot of Cyclically Adjusted P/E Ratio vs. Dividend Yield1
1Fun with CAPE (Don’t cry for me Argentina), http://www.dollarwiseﬂ.com/tag/greece, accessed 2/23/15
--- page 560 ---

Appendix B: Financial Statistics
537
Because a is a constant,  a = na. Also, because b is a constant,
 bX = b  X. Thus,

Y = na + b

X.
The second normal equation may be found by multiplying the
general equation through by the coeﬃcient of the second constant
and summing:
Y = a + bX
XY = aX + bX2
ΣXY = ΣaX + ΣbX2
ΣXY = aΣX + bΣX2.
Year
Sales (million)
Net Income (millions)
2009
10
0
2010
12
1
2011
13
2
2012
11
3
2013
14
4
Suppose the Alberich Mining Corp. wished to regress its sales
activity and the net income it earns. Data for the past ﬁve years are
given below:
A least-square regression equation for Alberich could be determined by using the normal equations:
Y = f(X), where Y is net income and X is sales.
ΣY = 10
ΣX = 60
ΣXY = 127
ΣX2 = 730
ΣY = na + bΣX
--- page 561 ---

538
Quantitative Financial Analytics
10 = 5a + 60b
ΣXY = aΣX + bΣX2
127 = 60a + 730b.
Solving simultaneously, we ﬁnd:
127
=
60a + 730b
120
=
60a + 720b
7
=
10b
b = 0.7
10
=
5a + 60(0.7)
a = −6.4.
Thus, the least-squares regression equation is:
Yc = −6.4 + 0.7X.
The computation of least-squares trend lines may be done more
eﬃciently than through the use of Equations (B.9) and (B.10). The
intercept a may be computed by:
a = ΣY −bΣX
n
= ¯Y −b ¯X.
and the slope b by:
b = (ΣXY ) −(ΣXΣY )/n
ΣX2 −(ΣX)2/n
= rxy
sy
sx

.
The solution to the problem posed above would be (solving for b ﬁrst
because it is required to compute a):
b = [127] −[(60)(10)]/5
(730) −(60)2/5
= 0.7
a = 10 −(0.7)(60)
5
= −6.4.
The simplest method of computing least-squares equations is by
use of the computer. Programs exist that can handle large amounts
of correlated data. Computations involving more than 20 or so
inputs become onerous when calculations are made manually, and
few analysts rely on calculators any longer to ﬁt least-squares trend
--- page 562 ---

Appendix B: Financial Statistics
539
lines. Computers can also perform the more complicated computations associated with multiple regression analysis and non-linear
least-squares equations. Because few analysts use hand methods
anymore, the calculations presented above should serve as an
explication of the mathematical process underlying regression and
correlation analysis rather than as a tool to provide solutions.
Once the least-squares trend line is established, the analyst
may wish to know just how good the ﬁt is between the variables.
Thus, a measure of the closeness of the relationship between the
variables must be sought. The ﬁrst step in this process requires
the determination of the standard error of the estimate, which is a
measure of the deviation of actual values around the estimated trend
line. The standard error of the estimate is given by the following
equation:
sy·x =

Σ(Y −ˆY )2
n −1
.
If sy·x = 0, we know that all actual values lie on the trend line, and
there is a clear linear relationship between Y and X. On the other
hand, if there were no linear relationship between the variables, the
standard error of the estimate would equal the standard deviation of
the dependent variable sy·x = sy.
Determination of the standard error of the estimate allows us
to compute an index of the closeness of the relationship between
the variables. This index, called the coeﬃcient of correlation, is
given by:
ry·x =

1 −s2y·x
s2y
.
The square of the coeﬃcient of correlation, r2, is called the coef-
ﬁcient of determination. Its value is the percentage of the variation
explained by the liner regression model. Values for r2 may be between
0 and 1. If two random variables are perfectly correlated, sy·x = 0.
Hence, r2 = 1−0
s2y = 1. If two variables are completely uncorrelated,
--- page 563 ---

540
Quantitative Financial Analytics
s2
y·x = s2
y. In this case, r2 = 1−
s2
y·x
s2y = 0. Thus, when two variables are
highly correlated, r2 will be a large decimal. When they are poorly
correlated, r2 will be a small decimal.
The equation for multiple regression is one of the form:
Y = a ± bX1 ± cX2 ± dX3.
In this instance, several independent variables are correlated with
the dependent variable, and a general measure of the closeness
of the relationship between the dependent variable and the joint
simultaneous conﬁguration of the independent variables is required.
This measure, designated the coeﬃcient of multiple determination,
or R2, is complicated to compute by hand. Although a number of
basic statistics books present short-cut equations for the calculation,
the statistic is always provided by computer programs that compute multiple-regression equations. Because the analyst will rarely
perform these calculations, we shall omit a detailed listing of the
equations required to determine R2.
Coeﬃcients of partial determination measure the relationship
between the dependent variable and any one of the independent
variables, while the other independent variables are held constant.
These coeﬃcients are distinct from the separate coeﬃcients of
determination of each independent variable with the dependent
variable. An interpretation of a coeﬃcient of partial determination may be made by considering an example multiple-regression
equation with partial coeﬃcients given under the independent
variables:
Y = a + bX1 + cX2 + dX3
(0.82) (0.91) (0.41)
R2 = 0.86.
In this example, 82 percent of the variation in Y that is not associated
with X2 or X3 is incrementally associated with X1.
There are several problems that develop in interpreting regression
results. High R2 values may occur when n is very small simply
because too few inputs are included to demonstrate variability. Also,
--- page 564 ---

Appendix B: Financial Statistics
541
it should be remembered that R2 measures covariation, not causality.
If green lights are highly associated with moving automobiles, this
does not mean that green lights cause automobiles to move. There
are further problems of inference from sample data to populations.
It may be necessary to test the hypothesis that the R2 determined is
signiﬁcantly diﬀerent from zero. The F test may be used for this
purpose, and its application is discussed in most statistics texts.
Other problems develop when serial correlation is suspected among
the disturbance terms. This phenomenon is particularly associated
with the use of time-series data, and the analyst should be aware of
the fact that the presence of serial correlation reduces the eﬃciency
of his estimators. Tests such as that developed by Durbin–Watson
may be used to discern serial correlation, although the problem is
beyond the scope of this book.
Conditional Probability Distributions
Two random variables are said to be independent if and only if:
P(X, Y ) = P(X) × P(Y ).
In this case, the probability of X assuming any value is not aﬀected
by any value Y might take on, and vice versa.
Statistical independence may be illustrated with a set of
conditional probabilities. Consider the following joint probability
distribution:
Possible Outcomes for Y
Y1 = $10
Y2 = $500
Possible Outcomes
Total
for X
Probability
X1 = $100
.30
.10
.40
X2 = $200
.20
.40
.60
Total Probability
.50
.50
1.00
There are two possible outcomes for X (that is, X1 and X2) and
two for Y (Y1 and Y2). Variable X may take on either of its values
--- page 565 ---

542
Quantitative Financial Analytics
without being inﬂuenced by or inﬂuencing Y . Thus, given the fact
that X = X1, we may observe that P(Y = Y1) = 0.30/40 = 0.75.
Given the fact that X = X1, it is also clear the P(Y = Y2) =
0.10/0.40 = 0.25. Because Y can only be Y1 or Y2, the sum of the
probabilities (0.75 + 0.25) must equal 1.00. Similarly, given the fact
that X = X2, P(Y = Y1) = 0.20/0.60 and P(Y = Y2) = 0.40/0.60,
and 1/3+2/3 = 1.00. The mathematical relationship of the variables
is described by:
P(Y |X) = P(Y, X)
P(X) ,
where
P(Y |X) is the conditional probability of event Y , given that the
event X has occurred.
P(X) is the probability of event X occurring.
P(Y ,X) is the joint probability of Y and X both occurring.
In Table B.1, the probability that X will take on value X1 [that
is, P(X = X1)] is simply 0.4. The probability that X = X1, given
that Y = Y2, however, is:
P(X1|Y2) = 0.10/0.50 = 0.20.
The probability that X = X1 and Y = Y1 would be:
P(X1, Y1) = P(Y1) × P(X1|Y1)
= (0.50)(0.30/0.50)
= 0.30.
If we assume that X will occur before Y (that is, X is assumed
to be given before Y takes on values), a tree diagram may be drawn
to indicate all possible outcomes (Figure B.6):
Note if we are concerned with the probability of Y1 occurring in
any event, the tree diagram clearly shows that P(Y1) = P(Y1, X1) +
P(Y1, X2) = 0.3 + 0.2 = 0.5.
--- page 566 ---

Appendix B: Financial Statistics
543
Y 1
P (X 1, Y 1) = .30
X 1
P (Y 1|X1) = .75
   P (X 1) = .4
Y 2
P (X 1, Y 2) = .10
P (Y 2|X1) = .25
Y 1
P (X 2, Y 1) = .20
X 2
P (Y 1|X2) = .33
P (X 2) = .6
Y 2
P (X 2, Y 2) = .40
P (Y 2|X2) = .67
Figure B.6. Tree Diagram
Expected Values and Variances of Two or More
Random Variables
The expected value of two (or more) random variables is simply the
sum of the respective expected values, or:
E(Y + X) = E(Y ) + E(X).
The variance of two or more random variables is given by:
V =
N

i=1
N

j=1
ρijσiσj.
For two random variables, we ﬁnd:
V = ρyyσyσy + ρyxσyσx + ρxyσxσy + ρxxσxσx.
Now, we know ρyy = 1 and ρxx = 1. We also know that ρxy = ρyx.
Hence, we may calculate the variance as:
V = σ2
y + σ2
x + 2σyσxρxy.
In covariance form, we have:
V = V (Y ) + V (X) + 2Cov(X, Y ).
When random variables are percentages (such as in the case of
rates of return), the expected value of two or more random variables
--- page 567 ---

544
Quantitative Financial Analytics
is the weighted average of the respective expected returns:
E =
N

i=y
αiEi,
where αi is the proportion of the total placed in the ith investment.
In this case, the variance becomes:
V =
N

i=1
N

j=1
αiαjρijσiσj.
For two random variables,
V = α2
yσ2
y + α2
xσ2
x + 2αyαxρxyσyσx,
which, in covariance form, is:
V = α2
yV (Y ) + α2
xV (X) + 2αyαxCov(Y, X).
Reconsider the two stocks X and Y that were examined in the
section on Covariance. There, we found Stock X had an expected
proﬁt of $1,000 and a variance of $9 million. Stock Y had an expected
proﬁt of $500 and a variance of $250,000. The covariance between the
two investments was $1,500,000. Suppose an investor purchased both
stocks. His expected return from the portfolio would be:
E(X + Y ) = 1,000 + 500 = 1,500.
The variance of the total portfolio would be:
V (X + Y ) = 9,000,000 + 250,000 + 2(1,500,000)
= 12,250,000.
In the above case, we may assume that an equal investment of $10,000
had been made in each stock (total investment of $20,000). If all the
dollars had been put into Stock X, the expected return and variance
--- page 568 ---

Appendix B: Financial Statistics
545
would be:
E(X) = (2)(1,000) = 2,000
V (X) = 8,000 −2,000 = (6,000)2 →36,000,000(0.5) = 18,000,000
−4,000 −2,000 = (−6,000)2 →36,000,000(0.5) = 18,000,000
V (X) = 36,000,000.
A comparison of the return-variance pattern from each portfolio
would show:
E(X + Y ) = 1,500
E(X) = 2,000
V (X + Y ) = 20,000
V (X) = 36,000,000.
Thus, the diversiﬁed portfolio would provide a lower expected
return and a lower risk.
Problems
1. An analyst is attempting to predict the price of a bond next
year. The bond currently sells at 90, has six years to maturity,
and has a 6 percent coupon. The analyst has obtained predictions
from the economics department of his ﬁrm about the prime rate
of interest for next year. They feel the chances are about 0.5
that the prime rate will be 6 percent, about 0.3 that it will be
5 percent, and about 0.2 that it will be 4 percent. The analyst
believes that the bond he is analyzing should yield about 200
basis points (a basis point equals 0.01 percent) more than the
prime rate.
a. Formulate a probability distribution for the price of the bond
next year. (Use the short-cut yield formula given in Chapter 3
and compute the price to the nearest dollar.)
b. Determine the expected value of the price.
c. Compute the mode and median prices.
d. What is the standard deviation of the distribution? The
coeﬃcient of variation?
--- page 569 ---

546
Quantitative Financial Analytics
e. Determine the semi-variance of the distribution. Comment
on the eﬃcacy of this statistic as a measure of risk in this
instance.
f. Describe the symmetry and kurtosis of the distribution.
2. The dividend payment for next year of the Elsa Company is
expected to be one dollar per share with a standard deviation
of ten cents. What is the probability that the dividend will be
greater than one dollar? What is the probability that no dividend
will be paid? What is the minimum dividend that one might
reasonably expect? Assume that dividend payments by Elsa are
normally distributed.
3. Jones bought a call on 100 shares of Ionocon Corp. this week.
His call entitles him to buy the shares at a price of $10 per
share for the next six months. The shares are now $10.50 per
share, and Jones’ call cost him a total of $150. He believes the
price of Ionocon shares for the near future is normally distributed
with a mean of $15 and a standard deviation of $5. What is the
probability that Jones will lose money?
4. Glamour Glow, Ltd. is a growth stock. The price of its shares
moves with the market. When stock prices are up, Glamour
Glow generally outperforms the averages. Alchemy Mining is a
contracyclical stock. When the market is up, Alchemy does not
do very well because investment dollars are chasing up stocks
like Glamour Glow. When the market is down, particularly if the
negative movement is the result of an international money panic,
Alchemy does extremely well. A return matrix for investment in
Glamour Glow and Alchemy under three market conditions is
given below:
Market Condition Probability Proﬁt-Glamour Proﬁt-Alchemy
Prosperity
.6
$3,000
−$1,000
Recession
.3
−1,000
0
Money panic
.1
−2,000
5,000
--- page 570 ---

Appendix B: Financial Statistics
547
a. Calculate the independent expected value and variance for
each stock.
b. What is the covariance between the two? The correlation
coeﬃcient?
5. Compute the standard error of the estimate, the coeﬃcient of
correlation, and the coeﬃcient of determination for the Alberich
Mining Corp. (See discussion earlier in chapter.) Interpret your
results.
6. The Rheingold Jewelry Co. is attempting to correlate its sales
(Y ) with several independent variables. It is felt that such
variables as national income (X1), the retail price level (X2),
and the level of interest rates (X3) might inﬂuence sales. After
gathering data for 20 years, the ﬁrm has determined the following
equation:
Y = 186 + 0.038(X1) −0.124(X2) −1.81(X3)
(0.84)
(0.22)
(0.45)
R2 = 0.64.
a. If sales are in thousands, what are the likely units for national
income, the retail price level, and the level of interest rates?
b. Let
X1 = 1,000
X2 = 126
X3 = 7.
Determine the trend value of sales.
c. Interpret the R2 value and the coeﬃcients of partial determination.
d. Suppose data had been gathered for only ﬁve years. What
would you expect to happen to R2? Why?
7. Using the joint probability table below, assume that Y will occur
before X. Draw a tree diagram indicating all possible outcomes.
--- page 571 ---

548
Quantitative Financial Analytics
Possible Outcomes for Y
Possible Outcomes
Total
for X
Y1 = $10
Y2 = $500
Probability
X1 = $100
.30
.10
.40
X2 = $200
.20
.40
.60
Total Probability
.50
.50
1.00
8. Let the outcomes in the above table take on the numerical values
given (that is, X1 = $100, and so on). Calculate the following:
a. The independent expected value and variance for X and Y .
b. The covariance between them.
c. The correlation coeﬃcient between them.
d. The expected return and variance of the combination.
9. Two investments have the following characteristics:
µX = $30,000
σX = $10,000
µY = $20,000
σY = 0.
What are the covariance and correlation coeﬃcient between the
investments?
10. Reconsider the prospective prices of Glamour Glow, Ltd., and
Alchemy Mining.
a. Determine the expected return and variance if both stocks are
bought.
b. Given the miserable expected performance of Alchemy, is
there any argument for including it in the portfolio?
11. A portfolio contains two stocks, A and B. The expected yield
from A is 10 percent, with a variance of 25 percent. The expected
yield from B is 8 percent, with a variance of 9 percent. The
correlation between returns from A and B is zero. If 1/5 of the
portfolio is in A and 4/5 in B, what is the expected return and
variance from the portfolio?
