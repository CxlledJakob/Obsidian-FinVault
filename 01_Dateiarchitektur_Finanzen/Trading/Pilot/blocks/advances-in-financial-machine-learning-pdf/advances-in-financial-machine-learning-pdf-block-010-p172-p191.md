# Advances in Financial Machine Learning.pdf — pages 172–191

--- page 172 ---

DYNAMIC BET SIZES AND LIMIT PRICES
145
FIGURE 10.2
Discretization of the bet size, d = 0.2
overtrading, I suggest you discretize the bet size as m∗= round
[
m
d
]
d, where d ∈
(0, 1] determines the degree of discretization. Figure 10.2 illustrates the discretization of the bet size. Snippet 10.3 implements this notion.
SNIPPET 10.3
SIZE DISCRETIZATION TO PREVENT
OVERTRADING
def discreteSignal(signal0,stepSize):
# discretize signal
signal1=(signal0/stepSize).round()*stepSize # discretize
signal1[signal1>1]=1 # cap
signal1[signal1<-1]=-1 # floor
return signal1
10.6
DYNAMIC BET SIZES AND LIMIT PRICES
Recall the triple-barrier labeling method presented in Chapter 3. Bar i is formed
at time ti,0, at which point we forecast the first barrier that will be touched. That
prediction implies a forecasted price, Eti,0[pti,1], consistent with the barriers’ settings.
In the period elapsed until the outcome takes place, t ∈[ti,0, ti,1], the price pt fluctuates
and additional forecasts may be formed, Etj,0[pti,1], where j ∈[i + 1, I] and tj,0 ≤ti,1.
In Sections 10.4 and 10.5 we discussed methods for averaging the active bets and
--- page 173 ---

146
BET SIZING
discretizing the bet size as new forecasts are formed. In this section we will introduce
an approach to adjust bet sizes as market price pt and forecast price fi fluctuate. In the
process, we will derive the order’s limit price.
Let qt be the current position, Q the maximum absolute position size, and̂ qi,t the
target position size associated with forecast fi, such that̂
qi,t = int[m[𝜔, fi −pt]Q]
m [𝜔, x] =
x
√
𝜔+ x2
where m [𝜔, x] is the bet size, x = fi −pt is the divergence between the current market
price and the forecast, 𝜔is a coefficient that regulates the width of the sigmoid function, and Int [x] is the integer value of x. Note that for a real-valued price divergence
x, −1 < m [𝜔, x] < 1, the integer valuê qi,t is bounded −Q <̂ qi,t < Q.
The target position sizê qi,t can be dynamically adjusted as pt changes. In particular, as pt →fi we get̂ qi,t →0, because the algorithm wants to realize the gains. This
implies a breakeven limit pricē p for the order sizê qi,t −qt, to avoid realizing losses.
In particular,̄
p =
1
|̂qi,t −qt|
|̂qi,t|
∑
j=|qt+sgn[̂qi,t−qt]|
L
[
fi, 𝜔, j
Q
]
where L[fi, 𝜔, m] is the inverse function of m[𝜔, fi −pt] with respect to pt,
L[fi, 𝜔, m] = fi −m
√
𝜔
1 −m2
We do not need to worry about the case m2 = 1, because |̂qi,t| < 1. Since this
function is monotonic, the algorithm cannot realize losses as pt →fi.
Let us calibrate 𝜔. Given a user-defined pair (x, m∗), such that x = fi −pt and m∗=
m [𝜔, x], the inverse function of m [𝜔, x] with respect to 𝜔is
𝜔= x2(m∗−2 −1)
Snippet 10.4 implements the algorithm that computes the dynamic position size
and limit prices as a function of pt and fi. First, we calibrate the sigmoid function,
so that it returns a bet size of m∗= .95 for a price divergence of x = 10. Second,
we compute the target position̂ qi,t for a maximum position Q = 100, fi = 115 and
pt = 100. If you try fi = 110, you will get̂ qi,t = 95, consistent with the calibration
of 𝜔. Third, the limit price for this order of sizê qi,t −qt = 97 is pt < 112.3657 < fi,
which is between the current price and the forecasted price.
--- page 174 ---

DYNAMIC BET SIZES AND LIMIT PRICES
147
SNIPPET 10.4
DYNAMIC POSITION SIZE AND LIMIT PRICE
def betSize(w,x):
return x*(w+x**2)**-.5
#———————————————————————————————————————
def getTPos(w,f,mP,maxPos):
return int(betSize(w,f-mP)*maxPos)
#———————————————————————————————————————
def invPrice(f,w,m):
return f-m*(w/(1-m**2))**.5
#———————————————————————————————————————
def limitPrice(tPos,pos,f,w,maxPos):
sgn=(1 if tPos>=pos else -1)
lP=0
for j in xrange(abs(pos+sgn),abs(tPos+1)):
lP+=invPrice(f,w,j/ﬂoat(maxPos))
lP/=tPos-pos
return lP
#———————————————————————————————————————
def getW(x,m):
# 0<alpha<1
return x**2*(m**-2–1)
#———————————————————————————————————————
def main():
pos,maxPos,mP,f,wParams=0,100,100,115,{'divergence':10,'m':.95}
w=getW(wParams['divergence'],wParams['m']) # calibrate w
tPos=getTPos(w,f,mP,maxPos) # get tPos
lP=limitPrice(tPos,pos,f,w,maxPos) # limit price for order
return
#———————————————————————————————————————
if __name__=='__main__':main()
As an alternative to the sigmoid function, we could have used a power functioñ
m [𝜔, x] = sgn [x] |x|𝜔, where 𝜔≥0, x ∈[−1, 1], which results iñ m [𝜔, x] ∈[−1, 1].
This alternative presents the advantages that:
r̃ m [𝜔, −1] = −1,̃ m [𝜔, 1] = 1.
r Curvature can be directly manipulated through 𝜔.
r For 𝜔> 1, the function goes from concave to convex, rather than the other way
around, hence the function is almost flat around the inflexion point.
We leave the derivation of the equations for a power function as an exercise. Figure
10.3 plots the bet sizes (y-axis) as a function of price divergence f −pt (x-axis) for
both the sigmoid and power functions.
--- page 175 ---

148
BET SIZING
1.0
0.5
0.0
–0.5
–1.0
–1.0
–0.5
0.0
0.5
1.0
FIGURE 10.3
f [x] = sgn [x] |x|2 (concave to convex) and f [x] = x(.1 + x2)−.5 (convex to concave)
EXERCISES
10.1 Using the formulation in Section 10.3, plot the bet size (m) as a function of the
maximum predicted probability (̃p) when ‖X‖ = 2, 3, … , 10.
10.2 Draw 10,000 random numbers from a uniform distribution with bounds
U[.5, 1.].
(a) Compute the bet sizes m for ‖X‖ = 2.
(b) Assign 10,000 consecutive calendar days to the bet sizes.
(c) Draw 10,000 random numbers from a uniform distribution with bounds
U [1, 25].
(d) Form a pandas series indexed by the dates in 2.b, and with values equal
to the index shifted forward the number of days in 2.c. This is a t1 object
similar to the ones we used in Chapter 3.
(e) Compute the resulting average active bets, following Section 10.4.
10.3 Using the t1 object from exercise 2.d:
(a) Determine the maximum number of concurrent long bets,̄ cl.
(b) Determine the maximum number of concurrent short bets,̄ cs.
(c) Derive the bet size as mt = ct,l
1̄
cl −ct,s
1̄
cs , where ct,l is the number of concurrent long bets at time t, and ct,s is the number of concurrent short bets at
time t.
--- page 176 ---

BIBLIOGRAPHY
149
10.4 Using the t1 object from exercise 2.d:
(a) Compute the series ct = ct,l −ct,s, where ct,l is the number of concurrent
long bets at time t, and ct,s is the number of concurrent short bets at time t.
(b) Fit a mixture of two Gaussians on {ct}. You may want to use the method
described in L´opez de Prado and Foreman [2014].
(c) Derive the bet size as mt =
⎧
⎪
⎨
⎪⎩
F[ct]−F[0]
1−F[0]
if ct ≥0
F[ct]−F[0]
F[0]
if ct < 0
, where F [x] is the CDF
of the fitted mixture of two Gaussians for a value x.
(d) Explain how this series {mt} differ from the bet size series computed in
exercise 3.
10.5 Repeat exercise 1, where you discretize m with a
stepSize=.01,
stepSize=.05, and stepSize=.1.
10.6 Rewrite the equations in Section 10.6, so that the bet size is determined by a
power function rather than a sigmoid function.
10.7 Modify Snippet 10.4 so that it implements the equations you derived in exercise 6.
REFERENCES
L´opez de Prado, M. and M. Foreman (2014): “A mixture of Gaussians approach to mathematical
portfolio oversight: The EF3M algorithm.” Quantitative Finance, Vol. 14, No. 5, pp. 913–930.
Wu, T., C. Lin and R. Weng (2004): “Probability estimates for multi-class classification by pairwise
coupling.” Journal of Machine Learning Research, Vol. 5, pp. 975–1005.
BIBLIOGRAPHY
Allwein, E., R. Schapire, and Y. Singer (2001): “Reducing multiclass to binary: A unifying approach
for margin classifiers.” Journal of Machine Learning Research, Vol. 1, pp. 113–141.
Hastie, T. and R. Tibshirani (1998): “Classification by pairwise coupling.” The Annals of Statistics,
Vol. 26, No. 1, pp. 451–471.
Refregier, P. and F. Vallet (1991): “Probabilistic approach for multiclass classification with neural
networks.” Proceedings of International Conference on Artificial Networks, pp. 1003–1007.
--- page 177 ---
--- page 178 ---

CHAPTER 11
The Dangers of Backtesting
11.1
MOTIVATION
Backtesting is one of the most essential, and yet least understood, techniques in the
quant arsenal. A common misunderstanding is to think of backtesting as a research
tool. Researching and backtesting is like drinking and driving. Do not research under
the influence of a backtest. Most backtests published in journals are flawed, as the
result of selection bias on multiple tests (Bailey, Borwein, L´opez de Prado, and Zhu
[2014]; Harvey et al. [2016]). A full book could be written listing all the different
errors people make while backtesting. I may be the academic author with the largest
number of journal articles on backtesting1 and investment performance metrics, and
still I do not feel I would have the stamina to compile all the different errors I have
seen over the past 20 years. This chapter is not a crash course on backtesting, but a
short list of some of the common errors that even seasoned professionals make.
11.2
MISSION IMPOSSIBLE: THE FLAWLESS BACKTEST
In its narrowest definition, a backtest is a historical simulation of how a strategy would
have performed should it have been run over a past period of time. As such, it is a
hypothetical, and by no means an experiment. At a physics laboratory, like Berkeley
Lab, we can repeat an experiment while controlling for environmental variables, in
order to deduce a precise cause-effect relationship. In contrast, a backtest is not an
experiment, and it does not prove anything. A backtest guarantees nothing, not even
achieving that Sharpe ratio if we could travel back in time in our retrofitted DeLorean
DMC-12 (Bailey and L´opez de Prado [2012]). Random draws would have been different. The past would not repeat itself.
1 http://papers.ssrn.com/sol3/cf_dev/AbsByAuth.cfm?per_id=434076; http://www.QuantResearch.org/.
151
--- page 179 ---

152
THE DANGERS OF BACKTESTING
What is the point of a backtest then? It is a sanity check on a number of variables,
including bet sizing, turnover, resilience to costs, and behavior under a given scenario.
A good backtest can be extremely helpful, but backtesting well is extremely hard. In
2014 a team of quants at Deutsche Bank, led by Yin Luo, published a study under the
title “Seven Sins of Quantitative Investing” (Luo et al. [2014]). It is a very graphic
and accessible piece that I would advise everyone in this business to read carefully.
In it, this team mentions the usual suspects:
1. Survivorship bias: Using as investment universe the current one, hence ignoring that some companies went bankrupt and securities were delisted along the
way.
2. Look-ahead bias: Using information that was not public at the moment the
simulated decision would have been made. Be certain about the timestamp for
each data point. Take into account release dates, distribution delays, and backfill
corrections.
3. Storytelling: Making up a story ex-post to justify some random pattern.
4. Data mining and data snooping: Training the model on the testing
set.
5. Transaction costs: Simulating transaction costs is hard because the only way
to be certain about that cost would have been to interact with the trading book
(i.e., to do the actual trade).
6. Outliers: Basing a strategy on a few extreme outcomes that may never happen
again as observed in the past.
7. Shorting: Taking a short position on cash products requires finding a lender.
The cost of lending and the amount available is generally unknown, and
depends on relations, inventory, relative demand, etc.
These are just a few basic errors that most papers published in journals make routinely. Other common errors include computing performance using a non-standard
method (Chapter 14); ignoring hidden risks; focusing only on returns while ignoring other metrics; confusing correlation with causation; selecting an unrepresentative
time period; failing to expect the unexpected; ignoring the existence of stop-out limits or margin calls; ignoring funding costs; and forgetting practical aspects (Sarfati
[2015]). There are many more, but really, there is no point in listing them, because of
the title of the next section.
11.3
EVEN IF YOUR BACKTEST IS FLAWLESS, IT IS
PROBABLY WRONG
Congratulations! Your backtest is flawless in the sense that everyone can reproduce
your results, and your assumptions are so conservative that not even your boss could
object to them. You have paid for every trade more than double what anyone could
possibly ask. You have executed hours after the information was known by half the
globe, at a ridiculously low volume participation rate. Despite all these egregious
--- page 180 ---

A FEW GENERAL RECOMMENDATIONS
153
costs, your backtest still makes a lot of money. Yet, this flawless backtest is probably
wrong. Why? Because only an expert can produce a flawless backtest. Becoming
an expert means that you have run tens of thousands of backtests over the years. In
conclusion, this is not the first backtest you produce, so we need to account for the
possibility that this is a false discovery, a statistical fluke that inevitably comes up
after you run multiple tests on the same dataset.
The maddening thing about backtesting is that, the better you become at it, the
more likely false discoveries will pop up. Beginners fall for the seven sins of Luo et al.
[2014] (there are more, but who’s counting?). Professionals may produce flawless
backtests, and will still fall for multiple testing, selection bias, or backtest overfitting
(Bailey and L´opez de Prado [2014b]).
11.4
BACKTESTING IS NOT A RESEARCH TOOL
Chapter 8 discussed substitution effects, joint effects, masking, MDI, MDA, SFI,
parallelized features, stacked features, etc. Even if some features are very important,
it does not mean that they can be monetized through an investment strategy. Conversely, there are plenty of strategies that will appear to be profitable even though they
are based on irrelevant features. Feature importance is a true research tool, because it
helps us understand the nature of the patterns uncovered by the ML algorithm, regardless of their monetization. Critically, feature importance is derived ex-ante, before the
historical performance is simulated.
In contrast, a backtest is not a research tool. It provides us with very little insight
into the reason why a particular strategy would have made money. Just as a lottery
winner may feel he has done something to deserve his luck, there is always some
ex-post story (Luo’s sin number three). Authors claim to have found hundreds of
“alphas” and “factors,” and there is always some convoluted explanation for them.
Instead, what they have found are the lottery tickets that won the last game. The
winner has cashed out, and those numbers are useless for the next round. If you would
not pay extra for those lottery tickets, why would you care about those hundreds of
alphas? Those authors never tell us about all the tickets that were sold, that is, the
millions of simulations it took to find these “lucky” alphas.
The purpose of a backtest is to discard bad models, not to improve them. Adjusting your model based on the backtest results is a waste of time . . . and it’s dangerous. Invest your time and effort in getting all the components right, as we’ve discussed elsewhere in the book: structured data, labeling, weighting, ensembles, crossvalidation, feature importance, bet sizing, etc. By the time you are backtesting, it
is too late. Never backtest until your model has been fully specified. If the backtest
fails, start all over. If you do that, the chances of finding a false discovery will drop
substantially, but still they will not be zero.
11.5
A FEW GENERAL RECOMMENDATIONS
Backtest overfitting can be defined as selection bias on multiple backtests. Backtest
overfitting takes place when a strategy is developed to perform well on a backtest, by
--- page 181 ---

154
THE DANGERS OF BACKTESTING
monetizing random historical patterns. Because those random patterns are unlikely to
occur again in the future, the strategy so developed will fail. Every backtested strategy
is overfit to some extent as a result of “selection bias”: The only backtests that most
people share are those that portray supposedly winning investment strategies.
How to address backtest overfitting is arguably the most fundamental question
in quantitative finance. Why? Because if there was an easy answer to this question,
investment firms would achieve high performance with certainty, as they would invest
only in winning backtests. Journals would assess with confidence whether a strategy
may be a false positive. Finance could become a true science in the Popperian and
Lakatosian sense (L´opez de Prado [2017]). What makes backtest overfitting so hard to
assess is that the probability of false positives changes with every new test conducted
on the same dataset, and that information is either unknown by the researcher or not
shared with investors or referees. While there is no easy way to prevent overfitting, a
number of steps can help reduce its presence.
1. Develop models for entire asset classes or investment universes, rather than
for specific securities (Chapter 8). Investors diversify, hence they do not make
mistake X only on security Y. If you find mistake X only on security Y, no matter
how apparently profitable, it is likely a false discovery.
2. Apply bagging (Chapter 6) as a means to both prevent overfitting and reduce
the variance of the forecasting error. If bagging deteriorates the performance of
a strategy, it was likely overfit to a small number of observations or outliers.
3. Do not backtest until all your research is complete (Chapters 1–10).
4. Record every backtest conducted on a dataset so that the probability of backtest
overfitting may be estimated on the final selected result (see Bailey, Borwein,
L´opez de Prado, and Zhu [2017a] and Chapter 14), and the Sharpe ratio may
be properly deflated by the number of trials carried out (Bailey and L´opez de
Prado [2014b]).
5. Simulate scenarios rather than history (Chapter 12). A standard backtest is a
historical simulation, which can be easily overfit. History is just the random
path that was realized, and it could have been entirely different. Your strategy
should be profitable under a wide range of scenarios, not just the anecdotal
historical path. It is harder to overfit the outcome of thousands of “what if”
scenarios.
6. If the backtest fails to identify a profitable strategy, start from scratch. Resist
the temptation of reusing those results. Follow the Second Law of Backtesting.
SNIPPET 11.1
MARCOS’ SECOND LAW OF BACKTESTING
“Backtesting while researching is like drinking and driving.
Do not research under the influence of a backtest.”
—Marcos L´opez de Prado
Advances in Financial Machine Learning (2018)
--- page 182 ---

STRATEGY SELECTION
155
11.6
STRATEGY SELECTION
In Chapter 7 we discussed how the presence of serial conditionality in labels defeats
standard k-fold cross-validation, because the random sampling will spatter redundant
observations into both the training and testing sets. We must find a different (true
out-of-sample) validation procedure: a procedure that evaluates our model on the
observations least likely to be correlated/redundant to those used to train the model.
See Arlot and Celisse [2010] for a survey.
Scikit-learn has implemented a walk-forward timefolds method.2 Under this
approach, testing moves forward (in the time direction) with the goal of preventing
leakage. This is consistent with the way historical backtests (and trading) are done.
However, in the presence of long-range serial dependence, testing one observation
away from the end of the training set may not suffice to avoid informational leakage.
We will retake this point in Chapter 12, Section 12.2.
One disadvantage of the walk-forward method is that it can be easily overfit. The
reason is that without random sampling, there is a single path of testing that can
be repeated over and over until a false positive appears. Like in standard CV, some
randomization is needed to avoid this sort of performance targeting or backtest optimization, while avoiding the leakage of examples correlated to the training set into
the testing set. Next, we will introduce a CV method for strategy selection, based on
the estimation of the probability of backtest overfitting (PBO). We leave for Chapter
12 an explanation of CV methods for backtesting.
Bailey et al. [2017a] estimate the PBO through the combinatorially symmetric
cross-validation (CSCV) method. Schematically, this procedure works as follows.
First, we form a matrix M by collecting the performance series from the N trials.
In particular, each column n = 1, … , N represents a vector of PnL (mark-to-market
profits and losses) over t = 1, … , T observations associated with a particular model
configuration tried by the researcher. M is therefore a real-valued matrix of order
(TxN). The only conditions we impose are that (1) M is a true matrix, that is, with the
same number of rows for each column, where observations are synchronous for every
row across the N trials, and (2) the performance evaluation metric used to choose the
“optimal” strategy can be estimated on subsamples of each column. For example, if
that metric is the Sharpe ratio, we assume that the IID Normal distribution assumption
can be held on various slices of the reported performance. If different model configurations trade with different frequencies, observations are aggregated (downsampled)
to match a common index t = 1, … , T.
Second, we partition M across rows, into an even number S of disjoint submatrices
of equal dimensions. Each of these submatrices Ms, with s = 1, … , S, is of order
( T
S xN).
Third, we form all combinations CS of Ms, taken in groups of size S
2. This gives a
total number of combinations
( S
S∕2
)
=
( S −1
S∕2 −1
)
S
S∕2
= . . . =
S∕2−1
∏
i=0
S −i
S∕2 −i
--- page 183 ---

156
THE DANGERS OF BACKTESTING
For instance, if S = 16, we will form 12,780 combinations. Each combination c ∈CS
is composed of S∕2 submatrices Ms.
Fourth, for each combination c ∈CS, we:
1. Form the training set J, by joining the S∕2 submatrices Ms that constitute c. J is
a matrix of order ( T
S
S
2xN) = ( T
2 xN).
2. Form the testing set̄ J, as the complement of J in M. In other words,̄ J is the
( T
2 xN) matrix formed by all rows of M that are not part of J.
3. Form a vector R of performance statistics of order N, where the n-th item of R
reports the performance associated with the n-th column of J (the training set).
4. Determine the element n∗such that Rn ≤Rn∗, ∀n = 1, … , N. In other words,
n∗= arg maxn{Rn}.
5. Form a vector̄ R of performance statistics of order N, where the n-th item of̄
R reports the performance associated with the n-th column of̄ J (the testing
set).
6. Determine the relative rank of Rn∗within̄ R. We denote this relative rank as̄ 𝜔c,
wherē 𝜔c ∈(0, 1). This is the relative rank of the out-of-sample (OOS) performance associated with the trial chosen in-sample (IS). If the strategy optimization procedure does not overfit, we should observe that Rn∗systematically
outperforms̄ R (OOS), just as Rn∗outperformed R (IS).
7. Define the logit 𝜆c = log[̄ 𝜔c
1−̄𝜔c
]. This presents the property that 𝜆c = 0 when
Rn∗coincides with the median of̄ R. High logit values imply a consistency
between IS and OOS performance, which indicates a low level of backtest
overfitting.
Fifth, compute the distribution of ranks OOS by collecting all the 𝜆c, for c ∈CS.
The probability distribution function f(𝜆) is then estimated as the relative frequency
at which 𝜆occurred across all CS, with ∫∞
−∞f(𝜆)d𝜆= 1. Finally, the PBO is estimated
as PBO = ∫0
−∞f(𝜆)d𝜆, as that is the probability associated with IS optimal strategies
that underperform OOS.
The x-axis of Figure 11.1 shows the Sharpe ratio IS from the best strategy selected.
The y-axis shows the Sharpe ratio OOS for that same best strategy selected. As it can
be appreciated, there is a strong and persistent performance decay, caused by backtest
overfitting. Applying the above algorithm, we can derive the PBO associated with this
strategy selection process, as displayed in Figure 11.2.
The observations in each subset preserve the original time sequence. The random
sampling is done on the relatively uncorrelated subsets, rather than on the observations. See Bailey et al. [2017a] for an experimental analysis of the accuracy of this
methodology.
--- page 184 ---

STRATEGY SELECTION
157
1.0
0.5
0.0
–0.5
–1.0
–1.5
–2.0
–2.5
0.5
1.0
1.5
2.0
2.5
3.0
SR IS
Prob[SR OOS<0]=0.74
[SR OOS]=0.87+–0.75*[SR IS]+err | adjR2=0.17
1 | OOS Perf. Degradation
SR OOS
FIGURE 11.1
Best Sharpe ratio in-sample (SR IS) vs Sharpe ratio out-of-sample (SR OOS)
0.35
0.30
0.25
0.20
0.15
0.10
0.05
0.00
–8
–6
–4
–2
0
Logits
1 | Hist. of Rank Logits
Prob Overfit=0.74
Frequency
2
4
6
FIGURE 11.2
Probability of backtest overfitting derived from the distribution of logits
--- page 185 ---

158
THE DANGERS OF BACKTESTING
EXERCISES
11.1 An analyst fits an RF classifier where some of the features include seasonally
adjusted employment data. He aligns with January data the seasonally adjusted
value of January, etc. What “sin” has he committed?
11.2 An analyst develops an ML algorithm where he generates a signal using closing
prices, and executed at close. What’s the sin?
11.3 There is a 98.51% correlation between total revenue generated by arcades and
computer science doctorates awarded in the United States. As the number of
doctorates is expected to grow, should we invest in arcades companies? If not,
what’s the sin?
11.4 The Wall Street Journal has reported that September is the only month of the
year that has negative average stock returns, looking back 20, 50, and 100 years.
Should we sell stocks at the end of August? If not, what’s the sin?
11.5 We download P/E ratios from Bloomberg, rank stocks every month, sell the top
quartile, and buy the long quartile. Performance is amazing. What’s the sin?
REFERENCES
Arlot, S. and A. Celisse (2010): “A survey of cross-validation procedures for model selection.”
Statistics Surveys, Vol. 4, pp. 40–79.
Bailey, D., J. Borwein, M. L´opez de Prado, and J. Zhu (2014): “Pseudo-mathematics and financial
charlatanism: The effects of backtest overfitting on out-of-sample performance.” Notices of the
American Mathematical Society, Vol. 61, No. 5 (May), pp. 458–471. Available at https://ssrn
.com/abstract=2308659.
Bailey, D., J. Borwein, M. L´opez de Prado, and J. Zhu (2017a): “The probability of backtest overfitting.” Journal of Computational Finance, Vol. 20, No. 4, pp. 39–70. Available at http://ssrn
.com/abstract=2326253.
Bailey, D. and M. L´opez de Prado (2012): “The Sharpe ratio efficient frontier.” Journal of Risk,
Vol. 15, No. 2 (Winter). Available at https://ssrn.com/abstract=1821643.
Bailey, D. and M. L´opez de Prado (2014b): “The deflated Sharpe ratio: Correcting for selection
bias, backtest overfitting and non-normality.” Journal of Portfolio Management, Vol. 40, No. 5,
pp. 94–107. Available at https://ssrn.com/abstract=2460551.
Harvey, C., Y. Liu, and H. Zhu (2016): “. . . and the cross-section of expected returns.” Review of
Financial Studies, Vol. 29, No. 1, pp. 5–68.
L´opez de Prado, M. (2017): “Finance as an industrial science.” Journal of Portfolio Management, Vol. 43, No. 4, pp. 5–9. Available at http://www.iijournals.com/doi/pdfplus/10.3905/jpm
.2017.43.4.005.
Luo, Y., M. Alvarez, S. Wang, J. Jussa, A. Wang, and G. Rohal (2014): “Seven sins of quantitative
investing.” White paper, Deutsche Bank Markets Research, September 8.
Sarfati, O. (2015): “Backtesting: A practitioner’s guide to assessing strategies and avoiding pitfalls.” Citi Equity Derivatives. CBOE 2015 Risk Management Conference. Available at
https://www.cboe.com/rmc/2015/olivier-pdf-Backtesting-Full.pdf.
--- page 186 ---

BIBLIOGRAPHY
159
BIBLIOGRAPHY
Bailey, D., J. Borwein, and M. L´opez de Prado (2016): “Stock portfolio design and backtest
overfitting.” Journal of Investment Management, Vol. 15, No. 1, pp. 1–13. Available at
https://ssrn.com/abstract=2739335.
Bailey, D., J. Borwein, M. L´opez de Prado, A. Salehipour, and J. Zhu (2016): “Backtest overfitting in
financial markets.” Automated Trader, Vol. 39. Available at https://ssrn.com/abstract=2731886.
Bailey, D., J. Borwein, M. L´opez de Prado, and J. Zhu (2017b): “Mathematical appendices to: ‘The
probability of backtest overfitting.’” Journal of Computational Finance (Risk Journals), Vol.
20, No. 4. Available at https://ssrn.com/abstract=2568435.
Bailey, D., J. Borwein, A. Salehipour, and M. L´opez de Prado (2017): “Evaluation and ranking of market forecasters.” Journal of Investment Management, forthcoming. Available at
https://ssrn.com/abstract=2944853.
Bailey, D., J. Borwein, A. Salehipour, M. L´opez de Prado, and J. Zhu (2015): “Online
tools for demonstration of backtest overfitting.” Working paper. Available at https://ssrn
.com/abstract=2597421.
Bailey, D., S. Ger, M. L´opez de Prado, A. Sim and, K. Wu (2016): “Statistical overfitting and backtest
performance.” In Risk-Based and Factor Investing, Quantitative Finance Elsevier. Available at
ttps://ssrn.com/abstract=2507040.
Bailey, D. and M. L´opez de Prado (2014a): “Stop-outs under serial correlation and ‘the triple
penance rule.’” Journal of Risk, Vol. 18, No. 2, pp. 61–93. Available at https://ssrn.com/
abstract=2201302.
Bailey, D. and M. L´opez de Prado (2015): “Mathematical appendices to: ‘Stop-outs under serial
correlation.’” Journal of Risk, Vol. 18, No. 2. Available at https://ssrn.com/abstract=2511599.
Bailey, D., M. L´opez de Prado, and E. del Pozo (2013): “The strategy approval decision: A Sharpe
ratio indifference curve approach.” Algorithmic Finance, Vol. 2, No. 1, pp. 99–109. Available
at https://ssrn.com/abstract=2003638.
Carr, P. and M. L´opez de Prado (2014): “Determining optimal trading rules without backtesting.”
Working paper. Available at https://ssrn.com/abstract=2658641.
L´opez de Prado, M. (2012a): “Portfolio oversight: An evolutionary approach.” Lecture at Cornell
University. Available at https://ssrn.com/abstract=2172468.
L´opez de Prado, M. (2012b): “The sharp razor: Performance evaluation with non-normal returns.”
Lecture at Cornell University. Available at https://ssrn.com/abstract=2150879.
L´opez de Prado, M. (2013): “What to look for in a backtest.” Lecture at Cornell University. Available
at https://ssrn.com/abstract=2308682.
L´opez de Prado, M. (2014a): “Optimal trading rules without backtesting.” Lecture at Cornell University. Available at https://ssrn.com/abstract=2502613.
L´opez de Prado, M. (2014b): “Deflating the Sharpe ratio.” Lecture at Cornell University. Available
at https://ssrn.com/abstract=2465675.
L´opez de Prado, M. (2015a): “Quantitative meta-strategies.” Practical Applications, Institutional
Investor Journals, Vol. 2, No. 3, pp. 1–3. Available at https://ssrn.com/abstract=2547325.
L´opez de Prado, M. (2015b): “The Future of empirical finance.” Journal of Portfolio Management,
Vol. 41, No. 4, pp. 140–144. Available at https://ssrn.com/abstract=2609734.
L´opez de Prado, M. (2015c): “Backtesting.” Lecture at Cornell University. Available at https://ssrn.
com/abstract=2606462.
L´opez de Prado, M. (2015d): “Recent trends in empirical finance.” Journal of Portfolio Management,
Vol. 41, No. 4, pp. 29–33. Available at https://ssrn.com/abstract=2638760.
--- page 187 ---

160
THE DANGERS OF BACKTESTING
L´opez de Prado, M. (2015e): “Why most empirical discoveries in finance are likely wrong, and what
can be done about it.” Lecture at University of Pennsylvania. Available at https://ssrn.com/
abstract=2599105.
L´opez de Prado, M. (2015f): “Advances in quantitative meta-strategies.” Lecture at Cornell University. Available at https://ssrn.com/abstract=2604812.
L´opez de Prado, M. (2016): “Building diversified portfolios that outperform out-of-sample.” Journal of Portfolio Management, Vol. 42, No. 4, pp. 59–69. Available at https://ssrn.com/
abstract=2708678.
L´opez de Prado, M. and M. Foreman (2014): “A mixture of Gaussians approach to mathematical
portfolio oversight: The EF3M algorithm.” Quantitative Finance, Vol. 14, No. 5, pp. 913–930.
Available at https://ssrn.com/abstract=1931734.
L´opez de Prado, M. and A. Peijan (2004): “Measuring loss potential of hedge fund strategies.”
Journal of Alternative Investments, Vol. 7, No. 1, pp. 7–31, Summer 2004. Available at
https://ssrn.com/abstract=641702.
L´opez de Prado, M., R. Vince, and J. Zhu (2015): “Risk adjusted growth portfolio in a finite investment horizon.” Lecture at Cornell University. Available at https://ssrn.com/abstract=2624329.
--- page 188 ---

CHAPTER 12
Backtesting through Cross-Validation
12.1
MOTIVATION
A backtest evaluates out-of-sample the performance of an investment strategy using
past observations. These past observations can be used in two ways: (1) in a narrow
sense, to simulate the historical performance of an investment strategy, as if it had
been run in the past; and (2) in a broader sense, to simulate scenarios that did not
happen in the past. The first (narrow) approach, also known as walk-forward, is so
prevalent that, in fact, the term “backtest” has become a de facto synonym for “historical simulation.” The second (broader) approach is far less known, and in this chapter
we will introduce some novel ways to carry it out. Each approach has its pros and
cons, and each should be given careful consideration.
12.2
THE WALK-FORWARD METHOD
The most common backtest method in the literature is the walk-forward (WF)
approach. WF is a historical simulation of how the strategy would have performed in
past. Each strategy decision is based on observations that predate that decision. As
we saw in Chapter 11, carrying out a flawless WF simulation is a daunting task that
requires extreme knowledge of the data sources, market microstructure, risk management, performance measurement standards (e.g., GIPS), multiple testing methods,
experimental mathematics, etc. Unfortunately, there is no generic recipe to conduct
a backtest. To be accurate and representative, each backtest must be customized to
evaluate the assumptions of a particular strategy.
WF enjoys two key advantages: (1) WF has a clear historical interpretation. Its
performance can be reconciled with paper trading. (2) History is a filtration; hence,
using trailing data guarantees that the testing set is out-of-sample (no leakage), as
long as purging has been properly implemented (see Chapter 7, Section 7.4.1). It is a
161
--- page 189 ---

162
BACKTESTING THROUGH CROSS-VALIDATION
common mistake to find leakage in WF backtests, where t1.index falls within the
training set, but t1.values fall within the testing set (see Chapter 3). Embargoing is
not needed in WF backtests, because the training set always predates the testing set.
12.2.1
Pitfalls of the Walk-Forward Method
WF suffers from three major disadvantages: First, a single scenario is tested (the historical path), which can be easily overfit (Bailey et al. [2014]). Second, WF is not
necessarily representative of future performance, as results can be biased by the particular sequence of datapoints. Proponents of the WF method typically argue that
predicting the past would lead to overly optimistic performance estimates. And yet,
very often fitting an outperforming model on the reversed sequence of observations
will lead to an underperforming WF backtest. The truth is, it is as easy to overfit a
walk-forward backtest as to overfit a walk-backward backtest, and the fact that changing the sequence of observations yields inconsistent outcomes is evidence of that
overfitting. If proponents of WF were right, we should observe that walk-backwards
backtests systematically outperform their walk-forward counterparts. That is not the
case, hence the main argument in favor of WF is rather weak.
To make this second disadvantage clearer, suppose an equity strategy that is backtested with a WF on S&P 500 data, starting January 1, 2007. Until March 15, 2009,
the mix of rallies and sell-offs will train the strategy to be market neutral, with low
confidence on every position. After that, the long rally will dominate the dataset, and
by January 1, 2017, buy forecasts will prevail over sell forecasts. The performance
would be very different had we played the information backwards, from January 1,
2017 to January 1, 2007 (a long rally followed by a sharp sell-off). By exploiting a
particular sequence, a strategy selected by WF may set us up for a debacle.
The third disadvantage of WF is that the initial decisions are made on a smaller
portion of the total sample. Even if a warm-up period is set, most of the information
is used by only a small portion of the decisions. Consider a strategy with a warm-up
period that uses t0 observations out of T. This strategy makes half of its decisions
( T−t0
2
)
on an average number of datapoints,
(T −t0
2
)−1 (
t0 + T + t0
2
) T −t0
4
= 1
4T + 3
4t0
which is only a 3
4
t0
T + 1
4 fraction of the observations. Although this problem is attenuated by increasing the warm-up period, doing so also reduces the length of the
backtest.
12.3
THE CROSS-VALIDATION METHOD
Investors often ask how a strategy would perform if subjected to a stress scenario
as unforeseeable as the 2008 crisis, or the dot-com bubble, or the taper tantrum, or
--- page 190 ---

THE COMBINATORIAL PURGED CROSS-VALIDATION METHOD
163
the China scare of 2015–2016, etc. One way to answer is to split the observations
into two sets, one with the period we wish to test (testing set), and one with the
rest (training set). For example, a classifier would be trained on the period January
1, 2009–January 1, 2017, then tested on the period January 1, 2008–December 31,
2008. The performance we will obtain for 2008 is not historically accurate, since
the classifier was trained on data that was only available after 2008. But historical
accuracy was not the goal of the test. The objective of the test was to subject a strategy
ignorant of 2008 to a stress scenario such as 2008.
The goal of backtesting through cross-validation (CV) is not to derive historically accurate performance, but to infer future performance from a number of outof-sample scenarios. For each period of the backtest, we simulate the performance of
a classifier that knew everything except for that period.
Advantages
1. The test is not the result of a particular (historical) scenario. In fact, CV
tests k alternative scenarios, of which only one corresponds with the historical sequence.
2. Every decision is made on sets of equal size. This makes outcomes comparable across periods, in terms of the amount of information used to make those
decisions.
3. Every observation is part of one and only one testing set. There is no warm-up
subset, thereby achieving the longest possible out-of-sample simulation.
Disadvantages
1. Like WF, a single backtest path is simulated (although not the historical one).
There is one and only one forecast generated per observation.
2. CV has no clear historical interpretation. The output does not simulate how the
strategy would have performed in the past, but how it may perform in the future
under various stress scenarios (a useful result in its own right).
3. Because the training set does not trail the testing set, leakage is possible.
Extreme care must be taken to avoid leaking testing information into the training set. See Chapter 7 for a discussion on how purging and embargoing can
help prevent informational leakage in the context of CV.
12.4
THE COMBINATORIAL PURGED CROSS-VALIDATION METHOD
In this section I will present a new method, which addresses the main drawback of the
WF and CV methods, namely that those schemes test a single path. I call it the “combinatorial purged cross-validation” (CPCV) method. Given a number 𝜑of backtest
paths targeted by the researcher, CPCV generates the precise number of combinations of training/testing sets needed to generate those paths, while purging training
observations that contain leaked information.
--- page 191 ---

164
BACKTESTING THROUGH CROSS-VALIDATION
Paths
S15
S14
S13
S12
S11
S10
S9
S8
S7
S6
S5
S4
S3
S2
S1
G1
5
x
x
x
x
x
G2
5
x
x
x
x
x
G3
5
x
x
x
x
x
G4
5
x
x
x
x
x
G5
5
x
x
x
x
x
G6
5
x
x
x
x
x
FIGURE 12.1
Paths generated for 𝝋[6, 2] = 5
12.4.1
Combinatorial Splits
Consider T observations partitioned into N groups without shuffling, where groups
n = 1, … , N −1 are of size ⌊T∕N⌋, the Nth group is of size T −⌊T∕N⌋(N −1), and
⌊.⌋is the floor or integer function. For a testing set of size k groups, the number of
possible training/testing splits is
(
N
N −k
)
=
∏k−1
i=0 (N −i)
k!
Since each combination involves k tested groups, the total number of tested groups
is k( N
N−k
). And since we have computed all possible combinations, these tested
groups are uniformly distributed across all N (each group belongs to the same number of training and testing sets). The implication is that from k-sized testing sets on
N groups we can backtest a total number of paths 𝜑[N, k],
𝜑[N, k] = k
N
(
N
N −k
)
=
∏k−1
i=1 (N −i)
(k −1)!
Figure 12.1 illustrates the composition of train/test splits for N = 6 and k = 2.
There are ( 6
4
) = 15 splits, indexed as S1,… ,S15. For each split, the figure marks with
a cross (x) the groups included in the testing set, and leaves unmarked the groups that
form the training set. Each group forms part of 𝜑[6, 2] = 5 testing sets, therefore this
train/test split scheme allows us to compute 5 backtest paths.
Figure 12.2 shows the assignment of each tested group to one backtest path. For
example, path 1 is the result of combining the forecasts from (G1, S1), (G2, S1),
Paths
S15
S14
S13
S12
S11
S10
S9
S8
S7
S6
S5
S4
S3
S2
S1
G1
5
5
4
3
2
1
G2
5
5
4
3
2
1
G3
5
5
4
3
2
1
G4
5
5
4
3
2
1
G5
5
5
4
3
2
1
G6
5
5
4
3
2
1
FIGURE 12.2
Assignment of testing groups to each of the 5 paths
