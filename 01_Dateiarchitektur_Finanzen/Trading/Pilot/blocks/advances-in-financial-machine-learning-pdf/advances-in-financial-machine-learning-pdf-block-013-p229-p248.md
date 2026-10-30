# Advances in Financial Machine Learning.pdf — pages 229–248

--- page 229 ---

202
BACKTEST STATISTICS
FIGURE 14.1
Examples of drawdown (DD) and time under water + (TuW)
r HHI index on negative returns: This is getHHI(ret[ret < 0]) in
Snippet 14.3.
r HHI index on time between
bets: This is
getHHI(ret.groupby
(pd.TimeGrouper (freq= 'M')).count()) in Snippet 14.3.
r 95-percentile DD: This is the 95th percentile of the DD series derived by
Snippet 14.4.
r 95-percentile TuW: This is the 95th percentile of the TuW series derived by
Snippet 14.4.
14.6
IMPLEMENTATION SHORTFALL
Investment strategies often fail due to wrong assumptions regarding execution costs.
Some important measurements of this include:
r Broker fees per turnover: These are the fees paid to the broker for turning the
portfolio over, including exchange fees.
r Average slippage per turnover: These are execution costs, excluding broker
fees, involved in one portfolio turnover. For example, it includes the loss caused
by buying a security at a fill-price higher than the mid-price at the moment the
order was sent to the execution broker.
r Dollar performance per turnover: This is the ratio between dollar performance (including brokerage fees and slippage costs) and total portfolio
turnovers. It signifies how much costlier the execution could become before
the strategy breaks even.
--- page 230 ---

EFFICIENCY
203
r Return on execution costs: This is the ratio between dollar performance
(including brokerage fees and slippage costs) and total execution costs. It should
be a large multiple, to ensure that the strategy will survive worse-than-expected
execution.
14.7
EFFICIENCY
Until now, all performance statistics considered profits, losses, and costs. In this section, we account for the risks involved in achieving those results.
14.7.1
The Sharpe Ratio
Suppose that a strategy’s excess returns (in excess of the risk-free rate), {rt}t=1,…,T,
are IID Gaussian with mean 𝜇and variance 𝜎2. The Sharpe ratio (SR) is defined as
SR = 𝜇
𝜎
The purpose of SR is to evaluate the skills of a particular strategy or investor.
Since 𝜇, 𝜎are usually unknown, the true SR value cannot be known for certain. The
inevitable consequence is that Sharpe ratio calculations may be the subject of substantial estimation errors.
14.7.2
The Probabilistic Sharpe Ratio
The probabilistic Sharpe ratio (PSR) provides an adjusted estimate of SR, by removing the inflationary effect caused by short series with skewed and/or fat-tailed returns.
Given a user-defined benchmark3 Sharpe ratio (SR∗) and an observed Sharpe ratiô SR,
PSR estimates the probability that̂ SR is greater than a hypothetical SR∗. Following
Bailey and L´opez de Prado [2012], PSR can be estimated aŝ
PSR [SR∗] = Z
⎡
⎢
⎢
⎢
⎢⎣
(̂
SR −SR∗) √
T −1
√
1 −̂ 𝛾3̂SR +̂ 𝛾4 −1
4̂
SR
2
⎤
⎥
⎥
⎥
⎥⎦
where Z [.] is the cumulative distribution function (CDF) of the standard Normal distribution, T is the number of observed returns,̂ 𝛾3 is the skewness of the returns, and̂
𝛾4 is the kurtosis of the returns (̂𝛾4 = 3 for Gaussian returns). For a given SR∗,̂ PSR
increases with greater̂ SR (in the original sampling frequency, i.e. non-annualized), or
longer track records (T), or positively skewed returns (̂𝛾3), but it decreases with fatter
3 This could be set to a default value of zero (i.e., comparing against no investment skill).
--- page 231 ---

204
BACKTEST STATISTICS
FIGURE 14.2
PSR as a function of skewness and sample length
tails (̂𝛾4). Figure 14.2 plotŝ PSR for̂ 𝛾4 = 3,̂ SR = 1.5 and SR∗= 1.0 as a function of̂
𝛾3 and T.
14.7.3
The Deflated Sharpe Ratio
The deflated Sharpe ratio (DSR) is a PSR where the rejection threshold is adjusted to
reflect the multiplicity of trials. Following Bailey and L´opez de Prado [2014], DSR
can be estimated aŝ PSR [SR∗], where the benchmark Sharpe ratio, SR∗, is no longer
user-defined. Instead, SR∗is estimated as
SR∗=
√
V
[{̂
SRn
}] (
(1 −𝛾) Z−1 [
1 −1
N
]
+ 𝛾Z−1 [
1 −1
N e−1])
where V[{̂SRn}] is the variance across the trials’ estimated SR, N is the number
of independent trials, Z [.] is the CDF of the standard Normal distribution, 𝛾is the
Euler-Mascheroni constant, and n = 1, … , N. Figure 14.3 plots SR∗as a function of
V[{̂SRn}] and N.
The rationale behind DSR is the following: Given a set of SR estimates, {̂SRn},
its expected maximum is greater than zero, even if the true SR is zero. Under the
null hypothesis that the actual Sharpe ratio is zero, H0 : SR = 0, we know that the
expected maximum̂ SR can be estimated as the SR∗. Indeed, SR∗increases quickly
as more independent trials are attempted (N), or the trials involve a greater variance
(V[{̂SRn}]). From this knowledge we derive the third law of backtesting.
--- page 232 ---

EFFICIENCY
205
FIGURE 14.3
SR∗as a function of V[{̂SRn}] and N
SNIPPET 14.5
MARCOS’ THIRD LAW OF BACKTESTING. MOST
DISCOVERIES IN FINANCE ARE FALSE BECAUSE OF ITS
VIOLATION
“Every backtest result must be reported in conjunction with all the trials
involved in its production. Absent that information, it is impossible to assess
the backtest’s ‘false discovery’ probability.”
—Marcos L´opez de Prado
Advances in Financial Machine Learning (2018)
14.7.4
Efficiency Statistics
Useful efficiency statistics include:
r Annualized Sharpe ratio: This is the SR value, annualized by a factor
√
a,
where a is the average number of returns observed per year. This common annualization method relies on the assumption that returns are IID.
r Information ratio: This is the SR equivalent of a portfolio that measures its performance relative to a benchmark. It is the annualized ratio between the average
excess return and the tracking error. The excess return is measured as the portfolio’s return in excess of the benchmark’s return. The tracking error is estimated
as the standard deviation of the excess returns.
r Probabilistic Sharpe ratio: PSR corrects SR for inflationary effects caused
by non-Normal returns or track record length. It should exceed 0.95, for the
--- page 233 ---

206
BACKTEST STATISTICS
standard significance level of 5%. It can be computed on absolute or relative
returns.
r Deflated Sharpe ratio: DSR corrects SR for inflationary effects caused by
non-Normal returns, track record length, and multiple testing/selection bias.
It should exceed 0.95, for the standard significance level of 5%. It can be computed on absolute or relative returns.
14.8
CLASSIFICATION SCORES
In the context of meta-labeling strategies (Chapter 3, Section 3.6), it is useful to
understand the performance of the ML overlay algorithm in isolation. Remember that
the primary algorithm identifies opportunities, and the secondary (overlay) algorithm
decides whether to pursue them or pass. A few useful statistics include:
r Accuracy: Accuracy is the fraction of opportunities correctly labeled by the
overlay algorithm,
accuracy =
TP + TN
TP + TN + FP + FN
where TP is the number of true positives, TN is the number of true negatives,
FP is the number of false positives, and FN is the number of false negatives.
r Precision: Precision is the fraction of true positives among the predicted
positives,
precision =
TP
TP + FP
r Recall: Recall is the fraction of true positives among the positives,
recall =
TP
TP + FN
r F1: Accuracy may not be an adequate classification score for meta-labeling
applications. Suppose that, after you apply meta-labeling, there are many more
negative cases (label ‘0’) than positive cases (label ‘1’). Under that scenario, a
classifier that predicts every case to be negative will achieve high accuracy, even
though recall=0 and precision is undefined. The F1 score corrects for that flaw,
by assessing the classifier in terms of the (equally weighted) harmonic mean of
precision and recall,
F1 = 2 precision ⋅recall
precision + recall
As a side note, consider the unusual scenario where, after applying metalabeling, there are many more positive cases than negative cases. A classifier that predicts all cases to be positive will achieve TN=0 and FN=0, hence
accuracy=precision and recall=1. Accuracy will be high, and F1 will not be
smaller than accuracy, even though the classifier is not able to discriminate
between the observed samples. One solution would be to switch the definitions
--- page 234 ---

ATTRIBUTION
207
of positive and negative cases, so that negative cases are predominant, and then
score with F1.
r Negative log-loss: Negative log-loss was introduced in Chapter 9, Section 9.4,
in the context of hyper-parameter tuning. Please refer to that section for details.
The key conceptual difference between accuracy and negative log-loss is that
negative log-loss takes into account not only whether our predictions were correct or not, but the probability of those predictions as well.
See Chapter 3, Section 3.7 for a visual representation of precision, recall, and
accuracy. Table 14.1 characterizes the four degenerate cases of binary classification.
As you can see, the F1 score is not defined in two of those cases. For this reason,
when Scikit-learn is asked to compute F1 on a sample with no observed 1s or with
no predicted 1s, it will print a warning (UndeﬁnedMetricWarning), and set the F1
value to 0.
TABLE 14.1
The Four Degenerate Cases of Binary Classification
Condition
Collapse
Accuracy
Precision
Recall
F1
Observed all 1s
TN=FP=0
=recall
1
[0,1]
[0,1]
Observed all 0s
TP=FN=0
[0,1]
0
NaN
NaN
Predicted all 1s
TN=FN=0
=precision
[0,1]
1
[0,1]
Predicted all 0s
TP=FP=0
[0,1]
NaN
0
NaN
When all observed values are positive (label ‘1’), there are no true negatives or
false positives, thus precision is 1, recall is a positive real number between 0 and 1
(inclusive), and accuracy equals recall. Then, F1 = 2 recall
1+recall ≥recall.
When all predicted values are positive (label ‘1’), there are no true negatives or
false negatives, thus precision is a positive real number between 0 and 1 (inclusive),
recall is 1, and accuracy equals precision. Then, F1 = 2 precision
1+precision ≥precision.
14.9
ATTRIBUTION
The purpose of performance attribution is to decompose the PnL in terms of risk
classes. For example, a corporate bond portfolio manager typically wants to understand how much of its performance comes from his exposure to the following risks
classes: duration, credit, liquidity, economic sector, currency, sovereign, issuer, etc.
Did his duration bets pay off? What credit segments does he excel at? Or should he
focus on his issuer selection skills?
These risks are not orthogonal, so there is always an overlap between them. For
example, highly liquid bonds tend to have short durations and high credit rating, and
are normally issued by large entities with large amounts outstanding, in U.S. dollars.
As a result, the sum of the attributed PnLs will not match the total PnL, but at least we
will be able to compute the Sharpe ratio (or information ratio) per risk class. Perhaps
the most popular example of this approach is Barra’s multi-factor method. See Barra
[1998, 2013] and Zhang and Rachev [2004] for details.
--- page 235 ---

208
BACKTEST STATISTICS
Of equal interest is to attribute PnL across categories within each class. For example, the duration class could be split between short duration (less than 5 years),
medium duration (between 5 and 10 years), and long duration (in excess of 10 years).
This PnL attribution can be accomplished as follows: First, to avoid the overlapping
problem we referred to earlier, we need to make sure that each member of the investment universe belongs to one and only one category of each risk class at any point in
time. In other words, for each risk class, we split the entire investment universe into
disjoint partitions. Second, for each risk class, we form one index per risk category.
For example, we will compute the performance of an index of short duration bonds,
another index of medium duration bonds, and another index of long duration bonds.
The weightings for each index are the re-scaled weights of our investment portfolio,
so that each index’s weightings add up to one. Third, we repeat the second step, but
this time we form those risk category indices using the weights from the investment
universe (e.g., Markit iBoxx Investment Grade), again re-scaled so that each index’s
weightings add up to one. Fourth, we compute the performance metrics we discussed
earlier in the chapter on each of these indices’ returns and excess returns. For the sake
of clarity, in this context the excess return of a short duration index is the return using
(re-scaled) portfolio weightings (step 2) minus the return using (re-scaled) universe
weightings (step 3).
EXERCISES
14.1 A strategy exhibits a high turnover, high leverage, and high number of bets, with
a short holding period, low return on execution costs, and a high Sharpe ratio.
Is it likely to have large capacity? What kind of strategy do you think it is?
14.2 On the dollar bars dataset for E-mini S&P 500 futures, compute
(a) HHI index on positive returns.
(b) HHI index on negative returns.
(c) HHI index on time between bars.
(d) The 95-percentile DD.
(e) The 95-percentile TuW.
(f) Annualized average return.
(g) Average returns from hits (positive returns).
(h) Average return from misses (negative returns).
(i) Annualized SR.
(j) Information ratio, where the benchmark is the risk-free rate.
(k) PSR.
(l) DSR, where we assume there were 100 trials, and the variance of the trials’
SR was 0.5.
14.3 Consider a strategy that is long one futures contract on even years, and is short
one futures contract on odd years.
(a) Repeat the calculations from exercise 2.
(b) What is the correlation to the underlying?
--- page 236 ---

BIBLIOGRAPHY
209
14.4 The results from a 2-year backtest are that monthly returns have a mean of 3.6%,
and a standard deviation of 0.079%.
(a) What is the SR?
(b) What is the annualized SR?
14.5 Following on exercise 1:
(a) The returns have a skewness of 0 and a kurtosis of 3. What is the PSR?
(b) The returns have a skewness of -2.448 and a kurtosis of 10.164. What is the
PSR?
14.6 What would be the PSR from 2.b, if the backtest had been for a length of 3 years?
14.7 A 5-year backtest has an annualized SR of 2.5, computed on daily returns. The
skewness is -3 and the kurtosis is 10.
(a) What is the PSR?
(b) In order to find that best result, 100 trials were conducted. The variance of
the Sharpe ratios on those trials is 0.5. What is the DSR?
REFERENCES
Bailey, D. and M. L´opez de Prado (2012): “The Sharpe ratio efficient frontier.” Journal of Risk,
Vol. 15, No. 2, pp. 3–44.
Bailey, D. and M. L´opez de Prado (2014): “The deflated Sharpe ratio: Correcting for selection
bias, backtest overfitting and non-normality.” Journal of Portfolio Management, Vol. 40, No. 5.
Available at https://ssrn.com/abstract=2460551.
Barra (1998): Risk Model Handbook: U.S. Equities, 1st ed. Barra. Available at http://www
.alacra.com/alacra/help/barra_handbook_US.pdf.
Barra (2013): MSCI BARRA Factor Indexes Methodology, 1st ed. MSCI Barra. Available at https://www.msci.com/eqb/methodology/meth_docs/MSCI_Barra_Factor%20Indices_
Methodology_Nov13.pdf.
CFA Institute (2010): “Global investment performance standards.” CFA Institute, Vol. 2010, No. 4,
February. Available at https://www.gipsstandards.org/.
Zhang, Y. and S. Rachev (2004): “Risk attribution and portfolio performance measurement—
An overview.” Working paper, University of California, Santa Barbara. Available at http://
citeseerx.ist.psu.edu/viewdoc/summary?doi=10.1.1.318.7169.
BIBLIOGRAPHY
American Statistical Society (1999): “Ethical guidelines for statistical practice.” Available at
http://www.amstat.org/committees/ethics/index.html.
Bailey, D., J. Borwein, M. L´opez de Prado, and J. Zhu (2014): “Pseudo-mathematics and financial charlatanism: The effects of backtest overfitting on out-of-sample performance.” Notices
of the American Mathematical Society, Vol. 61, No. 5. Available at http://ssrn.com/abstract=
2308659.
Bailey, D., J. Borwein, M. L´opez de Prado, and J. Zhu (2017): “The probability of backtest overfitting.” Journal of Computational Finance, Vol. 20, No. 4, pp. 39–70. Available at http://ssrn.
com/abstract=2326253.
Bailey, D. and M. L´opez de Prado (2012): “Balanced baskets: A new approach to trading and hedging
risks.” Journal of Investment Strategies (Risk Journals), Vol. 1, No. 4, pp. 21–62.
Beddall, M. and K. Land (2013): “The hypothetical performance of CTAs.” Working paper, Winton
Capital Management.
--- page 237 ---

210
BACKTEST STATISTICS
Benjamini, Y. and Y. Hochberg (1995): “Controlling the false discovery rate: A practical and powerful approach to multiple testing.” Journal of the Royal Statistical Society, Series B (Methodological), Vol. 57, No. 1, pp. 289–300.
Bennet, C., A. Baird, M. Miller, and G. Wolford (2010): “Neural correlates of interspecies perspective taking in the post-mortem Atlantic salmon: An argument for proper multiple comparisons
correction.” Journal of Serendipitous and Unexpected Results, Vol. 1, No. 1, pp. 1–5.
Bruss, F. (1984): “A unified approach to a class of best choice problems with an unknown number
of options.” Annals of Probability, Vol. 12, No. 3, pp. 882–891.
Dmitrienko, A., A.C. Tamhane, and F. Bretz (2010): Multiple Testing Problems in Pharmaceutical
Statistics, 1st ed. CRC Press.
Dudoit, S. and M.J. van der Laan (2008): Multiple Testing Procedures with Applications to
Genomics, 1st ed. Springer.
Fisher, R.A. (1915): “Frequency distribution of the values of the correlation coefficient in samples of
an indefinitely large population.” Biometrika (Biometrika Trust), Vol. 10, No. 4, pp. 507–521.
Hand, D. J. (2014): The Improbability Principle, 1st ed. Scientific American/Farrar, Straus and
Giroux.
Harvey, C., Y. Liu, and H. Zhu (2013): “. . . And the cross-section of expected returns.” Working
paper, Duke University. Available at http://ssrn.com/abstract=2249314.
Harvey, C. and Y. Liu (2014): “Backtesting.” Working paper, Duke University. Available at
http://ssrn.com/abstract=2345489.
Hochberg Y. and A. Tamhane (1987): Multiple Comparison Procedures, 1st ed. John Wiley and
Sons.
Holm, S. (1979): “A simple sequentially rejective multiple test procedure.” Scandinavian Journal
of Statistics, Vol. 6, pp. 65–70.
Ioannidis, J.P.A. (2005): “Why most published research findings are false.” PloS Medicine, Vol. 2,
No. 8, pp. 696–701.
Ingersoll, J., M. Spiegel, W. Goetzmann, and I. Welch (2007): “Portfolio performance manipulation
and manipulation-proof performance measures.” Review of Financial Studies, Vol. 20, No. 5,
pp. 1504–1546.
Lo, A. (2002): “The statistics of Sharpe ratios.” Financial Analysts Journal, Vol. 58, No. 4
(July/August), pp. 36–52.
L´opez de Prado M., and A. Peijan (2004): “Measuring loss potential of hedge fund strategies.”
Journal of Alternative Investments, Vol. 7, No. 1 (Summer), pp. 7–31. Available at http://ssrn
.com/abstract=641702.
Mertens, E. (2002): “Variance of the IID estimator in Lo (2002).” Working paper, University of
Basel.
Roulston, M. and D. Hand (2013): “Blinded by optimism.” Working paper, Winton Capital Management.
Schorfheide, F. and K. Wolpin (2012): “On the use of holdout samples for model selection.” American Economic Review, Vol. 102, No. 3, pp. 477–481.
Sharpe, W. (1966): “Mutual fund performance.” Journal of Business, Vol. 39, No. 1, pp. 119–138.
Sharpe, W. (1975): “Adjusting for risk in portfolio performance measurement.” Journal of Portfolio
Management, Vol. 1, No. 2 (Winter), pp. 29–34.
Sharpe, W. (1994): “The Sharpe ratio.” Journal of Portfolio Management, Vol. 21, No. 1 (Fall), pp.
49–58.
Studen´y M. and Vejnarov´a J. (1999): “The multiinformation function as a tool for measuring stochastic dependence,” in M. I. Jordan, ed., Learning in Graphical Models. MIT Press, pp. 261–296.
Wasserstein R., and Lazar N. (2016) “The ASA’s statement on p-values: Context, process, and
purpose.” American Statistician, Vol. 70, No. 2, pp. 129–133. DOI: 10.1080/00031305.2016.
1154108.
Watanabe S. (1960): “Information theoretical analysis of multivariate correlation.” IBM Journal of
Research and Development, Vol. 4, pp. 66–82.
--- page 238 ---

CHAPTER 15
Understanding Strategy Risk
15.1
MOTIVATION
As we saw in Chapters 3 and 13, investment strategies are often implemented in terms
of positions held until one of two conditions are met: (1) a condition to exit the position with profits (profit-taking), or (2) a condition to exit the position with losses (stoploss). Even when a strategy does not explicitly declare a stop-loss, there is always
an implicit stop-loss limit, at which the investor can no longer finance her position
(margin call) or bear the pain caused by an increasing unrealized loss. Because most
strategies have (implicitly or explicitly) these two exit conditions, it makes sense to
model the distribution of outcomes through a binomial process. This in turn will help
us understand what combinations of betting frequency, odds, and payouts are uneconomic. The goal of this chapter is to help you evaluate when a strategy is vulnerable
to small changes in any of these variables.
15.2
SYMMETRIC PAYOUTS
Consider a strategy that produces n IID bets per year, where the outcome Xi of a
bet i ∈[1, n] is a profit 𝜋> 0 with probability P[Xi = 𝜋] = p, and a loss −𝜋with
probability P[Xi = −𝜋] = 1 −p. You can think of p as the precision of a binary
classifier where a positive means betting on an opportunity, and a negative means
passing on an opportunity: True positives are rewarded, false positives are punished, and negatives (whether true or false) have no payout. Since the betting outcomes {Xi}i=1,…,n are independent, we will compute the expected moments per
bet. The expected profit from one bet is E[Xi] = 𝜋p + (−𝜋)(1 −p) = 𝜋(2p −1). The
variance is V[Xi] = E[X2
i ] −E[Xi]2, where E[X2
i ] = 𝜋2p + (−𝜋)2(1 −p) = 𝜋2, thus
211
--- page 239 ---

212
UNDERSTANDING STRATEGY RISK
V[Xi] = 𝜋2 −𝜋2(2p −1)2 = 𝜋2[1 −(2p −1)2] = 4𝜋2p(1 −p). For n IID bets per
year, the annualized Sharpe ratio (𝜃) is
𝜃[p, n] =
nE[Xi]
√
nV[Xi]
=
2p −1
2
√
p(1 −p)
⏟⏞⏞⏞⏞⏟⏞⏞⏞⏞⏟
t−value of p
under H0 : p = 1
2
√
n
Note how 𝜋cancels out of the above equation, because the payouts are symmetric. Just as in the Gaussian case, 𝜃[p, n] can be understood as a re-scaled t-value.
This illustrates the point that, even for a small p > 1
2, the Sharpe ratio can be made
high for a sufficiently large n. This is the economic basis for high-frequency trading,
where p can be barely above .5, and the key to a successful business is to increase
n. The Sharpe ratio is a function of precision rather than accuracy, because passing
on an opportunity (a negative) is not rewarded or punished directly (although too
many negatives may lead to a small n, which will depress the Sharpe ratio toward
zero).
For example, for p = .55,
2p−1
2
√
p(1−p) = 0.1005, and achieving an annualized Sharpe
ratio of 2 requires 396 bets per year. Snippet 15.1 verifies this result experimentally. Figure 15.1 plots the Sharpe ratio as a function of precision, for various betting
frequencies.
2.0
n=0
n=25
n=50
n=75
n=100
1.5
1.0
0.5
0.0
–0.5
–1.0
–1.5
–2.0
0.400
0.425
0.450
0.475
0.500
0.525
0.550
0.575
0.600
FIGURE 15.1
The relation between precision (x-axis) and sharpe ratio (y-axis) for various bet frequencies (n)
--- page 240 ---

ASYMMETRIC PAYOUTS
213
SNIPPET 15.1
TARGETING A SHARPE RATIO AS A FUNCTION OF
THE NUMBER OF BETS
out,p=[],.55
for i in xrange(1000000):
rnd=np.random.binomial(n=1,p=p)
x=(1 if rnd==1 else -1)
out.append(x)
print np.mean(out),np.std(out),np.mean(out)/np.std(out)
Solving for 0 ≤p ≤1, we obtain −4p2 + 4p −
n
𝜃2+n = 0, with solution
p = 1
2
(
1 +
√
1 −
n
𝜃2 + n
)
This equation makes explicit the trade-off between precision (p) and frequency
(n) for a given Sharpe ratio (𝜃). For example, a strategy that only produces weekly
bets (n = 52) will need a fairly high precision of p = 0.6336 to deliver an annualized
Sharpe of 2.
15.3
ASYMMETRIC PAYOUTS
Consider a strategy that produces n IID bets per year, where the outcome Xi
of a bet i ∈[1, n] is 𝜋+ with probability P[Xi = 𝜋+] = p, and an outcome 𝜋−,
𝜋−< 𝜋+ occurs with probability P[Xi = 𝜋−] = 1 −p. The expected profit from
one bet is E[Xi] = p𝜋+ + (1 −p)𝜋−= (𝜋+ −𝜋−)p + 𝜋−. The variance is V[Xi] =
E[X2
i ] −E[Xi]2, where E[X2
i ] = p𝜋2
+ + (1 −p)𝜋2
−= (𝜋2
+ −𝜋2
−)p + 𝜋2
−, thus V[Xi] =
(𝜋+ −𝜋−)2p(1 −p). For n IID bets per year, the annualized Sharpe ratio (𝜃) is
𝜃[p, n, 𝜋−, 𝜋+] =
nE[Xi]
√
nV[Xi]
=
(𝜋+ −𝜋−)p + 𝜋−
(𝜋+ −𝜋−)
√
p(1 −p)
√
n
And for 𝜋−= −𝜋+ we can see that this equation reduces to the symmetric
case: 𝜃[p, n, −𝜋+, 𝜋+] =
2𝜋+p+𝜋+
2𝜋+
√
p(1−p)
√
n =
2p−1
2
√
p(1−p)
√
n = 𝜃[p, n]. For example, for
n = 260, 𝜋−= −.01, 𝜋+ = .005, p = .7, we get 𝜃= 1.173.
Finally, we can solve the previous equation for 0 ≤p ≤1, to obtain
p = −b +
√
b2 −4ac
2a
--- page 241 ---

214
UNDERSTANDING STRATEGY RISK
where:
r a = (n + 𝜃2)(𝜋+ −𝜋−)2
r b = [2n𝜋−−𝜃2(𝜋+ −𝜋−)] (𝜋+ −𝜋−
)
r c = n𝜋2
−
As a side note, Snippet 15.2 verifies these symbolic operations using SymPy Live:
http://live.sympy.org/.
SNIPPET 15.2
USING THE SymPy LIBRARY FOR SYMBOLIC
OPERATIONS
>>> from sympy import *
>>> init_printing(use_unicode=False,wrap_line=False,no_global=True)
>>> p,u,d=symbols('p u d')
>>> m2=p*u**2+(1-p)*d**2
>>> m1=p*u+(1-p)*d
>>> v=m2-m1**2
>>> factor(v)
The above equation answers the following question: Given a trading rule characterized by parameters {𝜋−, 𝜋+, n}, what is the precision rate p required to achieve a
Sharpe ratio of 𝜃∗? For example, for n = 260, 𝜋−= −.01, 𝜋+ = .005, in order to get
𝜃= 2 we require a p = .72. Thanks to the large number of bets, a very small change
in p (from p = .7 to p = .72) has propelled the Sharpe ratio from 𝜃= 1.173 to 𝜃= 2.
On the other hand, this also tells us that the strategy is vulnerable to small changes in
p. Snippet 15.3 implements the derivation of the implied precision. Figure 15.2 displays the implied precision as a function of n and 𝜋−, where 𝜋+ = 0.1 and 𝜃∗= 1.5.
As 𝜋−becomes more negative for a given n, a higher p is required to achieve 𝜃∗for
a given 𝜋+. As n becomes smaller for a given 𝜋−, a higher p is required to achieve 𝜃∗
for a given 𝜋+.
SNIPPET 15.3
COMPUTING THE IMPLIED PRECISION
def binHR(sl,pt,freq,tSR):
’ ’ ’
Given a trading rule characterized by the parameters {sl,pt,freq},
what's the min precision p required to achieve a Sharpe ratio tSR?
1) Inputs
sl: stop loss threshold
pt: profit taking threshold
freq: number of bets per year
--- page 242 ---

ASYMMETRIC PAYOUTS
215
FIGURE 15.2
Heat-map of the implied precision as a function of n and 𝜋−, with 𝜋+ = 0.1 and 𝜃∗= 1.5
tSR: target annual Sharpe ratio
2) Output
p: the min precision rate p required to achieve tSR
’ ’ ’
a=(freq+tSR**2)*(pt-sl)**2
b=(2*freq*sl-tSR**2*(pt-sl))*(pt-sl)
c=freq*sl**2
p=(-b+(b**2–4*a*c)**.5)/(2.*a)
return p
Snippet 15.4 solves 𝜃[p, n, 𝜋−, 𝜋+] for the implied betting frequency, n. Figure 15.3
plots the implied frequency as a function of p and 𝜋−, where 𝜋+ = 0.1 and 𝜃∗= 1.5.
As 𝜋−becomes more negative for a given p, a higher n is required to achieve 𝜃∗for
a given 𝜋+. As p becomes smaller for a given 𝜋−, a higher n is required to achieve 𝜃∗
for a given 𝜋+.
SNIPPET 15.4
COMPUTING THE IMPLIED BETTING FREQUENCY
def binFreq(sl,pt,p,tSR):
’ ’ ’
Given a trading rule characterized by the parameters {sl,pt,freq},
what's the number of bets/year needed to achieve a Sharpe ratio
tSR with precision rate p?
Note: Equation with radicals, check for extraneous solution.
--- page 243 ---

216
UNDERSTANDING STRATEGY RISK
FIGURE 15.3
Implied frequency as a function of p and, with = 0.1 and = 1.5
1) Inputs
sl: stop loss threshold
pt: profit taking threshold
p: precision rate p
tSR: target annual Sharpe ratio
2) Output
freq: number of bets per year needed
’ ’ ’
freq=(tSR*(pt-sl))**2*p*(1-p)/((pt-sl)*p+sl)**2 # possible extraneous
if not np.isclose(binSR(sl,pt,freq,p),tSR):return
return freq
15.4
THE PROBABILITY OF STRATEGY FAILURE
In the example above, parameters 𝜋−= −.01, 𝜋+ = .005 are set by the portfolio manager, and passed to the traders with the execution orders. Parameter n = 260 is also set
by the portfolio manager, as she decides what constitutes an opportunity worth betting on. The two parameters that are not under the control of the portfolio manager
are p (determined by the market) and 𝜃∗(the objective set by the investor). Because
p is unknown, we can model it as a random variable, with expected value E [p]. Let
us define p𝜃∗as the value of p below which the strategy will underperform a target
Sharpe ratio 𝜃∗, that is, p𝜃∗= max{p|𝜃≤𝜃∗}. We can use the equations above (or the
binHR function) to conclude that for p𝜃∗=0 = 2
3, p < p𝜃∗=0 ⇒𝜃≤0. This highlights
--- page 244 ---

THE PROBABILITY OF STRATEGY FAILURE
217
the risks involved in this strategy, because a relatively small drop in p (from p = .7
to p = .67) will wipe out all the profits. The strategy is intrinsically risky, even if the
holdings are not. That is the critical difference we wish to establish with this chapter:
Strategy risk should not be confused with portfolio risk.
Most firms and investors compute, monitor, and report portfolio risk without realizing that this tells us nothing about the risk of the strategy itself. Strategy risk is not
the risk of the underlying portfolio, as computed by the chief risk officer. Strategy risk
is the risk that the investment strategy will fail to succeed over time, a question of far
greater relevance to the chief investment officer. The answer to the question “What
is the probability that this strategy will fail?” is equivalent to computing P[p < p𝜃∗].
The following algorithm will help us compute the strategy risk.
15.4.1
Algorithm
In this section we will describe a procedure to compute P[p < p𝜃∗]. Given a time
series of bet outcomes {𝜋t}t=1,…,T, first we estimate 𝜋−= E[{𝜋t|𝜋t ≤0}t=1,…,T], and
𝜋+ = E[{𝜋t|𝜋t > 0}t=1,…,T]. Alternatively, {𝜋−, 𝜋+} could be derived from fitting a
mixture of two Gaussians, using the EF3M algorithm (L´opez de Prado and Foreman
[2014]). Second, the annual frequency n is given by n = T
y , where y is the number of
years elapsed between t = 1 and t = T. Third, we bootstrap the distribution of p as
follows:
1. For iterations i = 1, … , I:
(a) Draw ⌊nk⌋samples from {𝜋t}t=1,…,T with replacement, where k is the number of years used by investors to assess a strategy (e.g., 2 years). We denote
the set of these drawn samples as {𝜋(i)
j }j=1,…,⌊nk⌋.
(b) Derive
the
observed
precision
from
iteration
i
as
pi =
1
⌊nk⌋‖{𝜋(i)
j |𝜋(i)
j
> 0}j=1,…,⌊nk⌋‖.
2. Fit the PDF of p, denoted f[p], by applying a Kernel Density Estimator (KDE)
on {pi}i=1,…,I.
For a sufficiently large k, we can approximate this third step as f[p] ∼
N[̄p,̄ p(1 −̄ p)], wherē p = E[p] = 1
T ‖{𝜋(i)
t |𝜋(i)
t
> 0}t=1,…,T‖. Fourth, given a threshold 𝜃∗(the Sharpe ratio that separates failure from success), derive p𝜃∗(see Section 15.4). Fifth, the strategy risk is computed as P[p < p𝜃∗] = ∫p𝜃∗
−∞f[p]dp.
15.4.2
Implementation
Snippet 15.5 lists one possible implementation of this algorithm. Typically we would
disregard strategies where P[p < p𝜃∗] > .05 as too risky, even if they invest in low
volatility instruments. The reason is that even if they do not lose much money, the
probability that they will fail to achieve their target is too high. In order to be deployed,
the strategy developer must find a way to reduce p𝜃∗.
--- page 245 ---

218
UNDERSTANDING STRATEGY RISK
SNIPPET 15.5
CALCULATING THE STRATEGY RISK IN PRACTICE
import numpy as np,scipy.stats as ss
#———————————————————————————————————————
def mixGaussians(mu1,mu2,sigma1,sigma2,prob1,nObs):
# Random draws from a mixture of gaussians
ret1=np.random.normal(mu1,sigma1,size=int(nObs*prob1))
ret2=np.random.normal(mu2,sigma2,size=int(nObs)-ret1.shape[0])
ret=np.append(ret1,ret2,axis=0)
np.random.shufﬂe(ret)
return ret
#———————————————————————————————————————
def probFailure(ret,freq,tSR):
# Derive probability that strategy may fail
rPos,rNeg=ret[ret>0].mean(),ret[ret<=0].mean()
p=ret[ret>0].shape[0]/ﬂoat(ret.shape[0])
thresP=binHR(rNeg,rPos,freq,tSR)
risk=ss.norm.cdf(thresP,p,p*(1-p)) # approximation to bootstrap
return risk
#———————————————————————————————————————
def main():
#1) Parameters
mu1,mu2,sigma1,sigma2,prob1,nObs=.05,-.1,.05,.1,.75,2600
tSR,freq=2.,260
#2) Generate sample from mixture
ret=mixGaussians(mu1,mu2,sigma1,sigma2,prob1,nObs)
#3) Compute prob failure
probF=probFailure(ret,freq,tSR)
print 'Prob strategy will fail',probF
return
#———————————————————————————————————————
if __name__=='__main__':main()
This approach shares some similarities with PSR (see Chapter 14, and Bailey and
L´opez de Prado [2012, 2014]). PSR derives the probability that the true Sharpe ratio
exceeds a given threshold under non-Gaussian returns. Similarly, the method introduced in this chapter derives the strategy’s probability of failure based on asymmetric
binary outcomes. The key difference is that, while PSR does not distinguish between
parameters under or outside the portfolio manager’s control, the method discussed
here allows the portfolio manager to study the viability of the strategy subject to the
parameters under her control: {𝜋−, 𝜋+, n}. This is useful when designing or assessing
the viability of a trading strategy.
--- page 246 ---

EXERCISES
219
EXERCISES
15.1 A portfolio manager intends to launch a strategy that targets an annualized SR of
2. Bets have a precision rate of 60%, with weekly frequency. The exit conditions
are 2% for profit-taking, and –2% for stop-loss.
(a) Is this strategy viable?
(b) Ceteris paribus, what is the required precision rate that would make the
strategy profitable?
(c) For what betting frequency is the target achievable?
(d) For what profit-taking threshold is the target achievable?
(e) What would be an alternative stop-loss?
15.2 Following up on the strategy from exercise 1.
(a) What is the sensitivity of SR to a 1% change in each parameter?
(b) Given these sensitivities, and assuming that all parameters are equally hard
to improve, which one offers the lowest hanging fruit?
(c) Does changing any of the parameters in exercise 1 impact the others? For
example, does changing the betting frequency modify the precision rate,
etc.?
15.3 Suppose a strategy that generates monthly bets over two years, with returns
following a mixture of two Gaussian distributions. The first distribution has
a mean of –0.1 and a standard deviation of 0.12. The second distribution has
a mean of 0.06 and a standard deviation of 0.03. The probability that a draw
comes from the first distribution is 0.15.
(a) Following L´opez de Prado and Peijan [2004] and L´opez de Prado and Foreman [2014], derive the first four moments for the mixture’s returns.
(b) What is the annualized SR?
(c) Using those moments, compute PSR[1] (see Chapter 14). At a 95% confidence level, would you discard this strategy?
15.4 Using Snippet 15.5, compute P[p < p𝜃∗=1] for the strategy described in exercise
3. At a significance level of 0.05, would you discard this strategy? Is this result
consistent with PSR[𝜃∗]?
15.5 In general, what result do you expect to be more accurate, PSR[𝜃∗] or
P[p < p𝜃∗=1]? How are these two methods complementary?
15.6 Re-examine the results from Chapter 13, in light of what you have learned in
this chapter.
(a) Does the asymmetry between profit taking and stop-loss thresholds in OTRs
make sense?
(b) What is the range of p implied by Figure 13.1, for a daily betting frequency?
(c) What is the range of p implied by Figure 13.5, for a weekly betting frequency?
--- page 247 ---

220
UNDERSTANDING STRATEGY RISK
REFERENCES
Bailey, D. and M. L´opez de Prado (2014): “The deflated Sharpe ratio: Correcting for selection
bias, backtest overfitting and non-normality.” Journal of Portfolio Management, Vol. 40, No.
5. Available at https://ssrn.com/abstract=2460551.
Bailey, D. and M. L´opez de Prado (2012): “The Sharpe ratio efficient frontier.” Journal of Risk, Vol.
15, No. 2, pp. 3–44. Available at https://ssrn.com/abstract=1821643.
L´opez de Prado, M. and M. Foreman (2014): “A mixture of Gaussians approach to mathematical
portfolio oversight: The EF3M algorithm.” Quantitative Finance, Vol. 14, No. 5, pp. 913–930.
Available at https://ssrn.com/abstract=1931734.
L´opez de Prado, M. and A. Peijan (2004): “Measuring loss potential of hedge fund strategies.” Journal of Alternative Investments, Vol. 7, No. 1 (Summer), pp. 7–31. Available at
http://ssrn.com/abstract=641702.
--- page 248 ---

CHAPTER 16
Machine Learning Asset Allocation
16.1
MOTIVATION
This chapter introduces the Hierarchical Risk Parity (HRP) approach.1 HRP portfolios address three major concerns of quadratic optimizers in general and Markowitz’s
Critical Line Algorithm (CLA) in particular: instability, concentration, and underperformance. HRP applies modern mathematics (graph theory and machine learning
techniques) to build a diversified portfolio based on the information contained in the
covariance matrix. However, unlike quadratic optimizers, HRP does not require the
invertibility of the covariance matrix. In fact, HRP can compute a portfolio on an
ill-degenerated or even a singular covariance matrix, an impossible feat for quadratic
optimizers. Monte Carlo experiments show that HRP delivers lower out-of-sample
variance than CLA, even though minimum-variance is CLA’s optimization objective. HRP produces less risky portfolios out-of-sample compared to traditional risk
parity methods. Historical analyses have also shown that HRP would have performed
better than standard approaches (Kolanovic et al. [2017], Raffinot [2017]). A practical application of HRP is to determine allocations across multiple machine learning
(ML) strategies.
16.2
THE PROBLEM WITH CONVEX PORTFOLIO OPTIMIZATION
Portfolio construction is perhaps the most recurrent financial problem. On a daily
basis, investment managers must build portfolios that incorporate their views and
forecasts on risks and returns. This is the primordial question that 24-year-old Harry
Markowitz attempted to answer more than six decades ago. His monumental insight
1 A short version of this chapter appeared in the Journal of Portfolio Management, Vo1. 42, No. 4,
pp. 59–69, Summer of 2016.
221
