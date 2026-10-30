# Advances in Financial Machine Learning.pdf — pages 115–134

--- page 115 ---

88
FRACTIONALLY DIFFERENTIATED FEATURES
5.7
CONCLUSION
To summarize, most econometric analyses follow one of two paradigms:
1. Box-Jenkins: Returns are stationary, however memory-less.
2. Engle-Granger: Log-prices have memory, however they are non-stationary.
Cointegration is the trick that makes regression work on non-stationary series,
so that memory is preserved. However the number of cointegrated variables is
limited, and the cointegrating vectors are notoriously unstable.
In contrast, the FFD approach introduced in this chapter shows that there is no
need to give up all of the memory in order to gain stationarity. And there is no need
for the cointegration trick as it relates to ML forecasting. Once you become familiar
with FFD, it will allow you to achieve stationarity without renouncing to memory (or
predictive power).
In practice, I suggest you experiment with the following transformation of your
features: First, compute a cumulative sum of the time series. This guarantees that
some order of differentiation is needed. Second, compute the FFD(d) series for various d ∈[0, 1]. Third, determine the minimum d such that the p-value of the ADF
statistic on FFD(d) falls below 5%. Fourth, use the FFD(d) series as your predictive
feature.
EXERCISES
5.1 Generate a time series from an IID Gaussian random process. This is a memoryless, stationary series:
(a) Compute the ADF statistic on this series. What is the p-value?
(b) Compute the cumulative sum of the observations. This is a non-stationary
series without memory.
(i) What is the order of integration of this cumulative series?
(ii) Compute the ADF statistic on this series. What is the p-value?
(c) Differentiate the series twice. What is the p-value of this over-differentiated
series?
5.2 Generate a time series that follows a sinusoidal function. This is a stationary
series with memory.
(a) Compute the ADF statistic on this series. What is the p-value?
(b) Shift every observation by the same positive value. Compute the cumulative
sum of the observations. This is a non-stationary series with memory.
(i) Compute the ADF statistic on this series. What is the p-value?
(ii) Apply an expanding window fracdiff, with 𝜏= 1E −2. For what minimum d value do you get a p-value below 5%?
(iii) Apply FFD, with 𝜏= 1E −5. For what minimum d value do you get a
p-value below 5%?
--- page 116 ---

BIBLIOGRAPHY
89
5.3 Take the series from exercise 2.b:
(a) Fit the series to a sine function. What is the R-squared?
(b) Apply FFD(d = 1). Fit the series to a sine function. What is the R-squared?
(c) What value of d maximizes the R-squared of a sinusoidal fit on FFD(d).
Why?
5.4 Take the dollar bar series on E-mini S&P 500 futures. Using the code
in Snippet 5.3, for some d ∈[0, 2], compute fracDiff_FFD(fracDiff
_FFD(series,d),-d). What do you get? Why?
5.5 Take the dollar bar series on E-mini S&P 500 futures.
(a) Form a new series as a cumulative sum of log-prices.
(b) Apply FFD, with 𝜏= 1E −5. Determine for what minimum d ∈[0, 2] the
new series is stationary.
(c) Compute the correlation of the fracdiff series to the original (untransformed)
series.
(d) Apply an Engel-Granger cointegration test on the original and fracdiff series.
Are they cointegrated? Why?
(e) Apply a Jarque-Bera normality test on the fracdiff series.
5.6 Take the fracdiff series from exercise 5.
(a) Apply a CUSUM filter (Chapter 2), where h is twice the standard deviation
of the series.
(b) Use the filtered timestamps to sample a features’ matrix. Use as one of the
features the fracdiff value.
(c) Form labels using the triple-barrier method, with symmetric horizontal barriers of twice the daily standard deviation, and a vertical barrier of 5 days.
(d) Fit a bagging classifier of decision trees where:
(i) The observed features are bootstrapped using the sequential method
from Chapter 4.
(ii) On each bootstrapped sample, sample weights are determined using the
techniques from Chapter 4.
REFERENCES
Alexander, C. (2001): Market Models, 1st edition. John Wiley & Sons.
Hamilton, J. (1994): Time Series Analysis, 1st ed. Princeton University Press.
Hosking, J. (1981): “Fractional differencing.” Biometrika, Vol. 68, No. 1, pp. 165–176.
Jensen, A. and M. Nielsen (2014): “A fast fractional difference algorithm.” Journal of Time Series
Analysis, Vol. 35, No. 5, pp. 428–436.
L´opez de Prado, M. (2015): “The Future of Empirical Finance.” Journal of Portfolio Management,
Vol. 41, No. 4, pp. 140–144. Available at https://ssrn.com/abstract=2609734.
BIBLIOGRAPHY
Cavaliere, G., M. Nielsen, and A. Taylor (2017): “Quasi-maximum likelihood estimation and bootstrap inference in fractional time series models with heteroskedasticity of unknown form.”
Journal of Econometrics, Vol. 198, No. 1, pp. 165–188.
--- page 117 ---

90
FRACTIONALLY DIFFERENTIATED FEATURES
Johansen, S. and M. Nielsen (2012): “A necessary moment condition for the fractional functional
central limit theorem.” Econometric Theory, Vol. 28, No. 3, pp. 671–679.
Johansen, S. and M. Nielsen (2012): “Likelihood inference for a fractionally cointegrated vector
autoregressive model.” Econometrica, Vol. 80, No. 6, pp. 2267–2732.
Johansen, S. and M. Nielsen (2016): “The role of initial values in conditional sum-of-squares estimation of nonstationary fractional time series models.” Econometric Theory, Vol. 32, No. 5,
pp. 1095–1139.
Jones, M., M. Nielsen and M. Popiel (2015): “A fractionally cointegrated VAR analysis of economic
voting and political support.” Canadian Journal of Economics, Vol. 47, No. 4, pp. 1078–1130.
Mackinnon, J. and M. Nielsen, M. (2014): “Numerical distribution functions of fractional unit root
and cointegration tests.” Journal of Applied Econometrics, Vol. 29, No. 1, pp. 161–171.
--- page 118 ---

P A R T 2
Modelling
Chapter 6: Ensemble Methods, 93
Chapter 7: Cross-Validation in Finance, 103
Chapter 8: Feature Importance, 113
Chapter 9: Hyper-Parameter Tuning with Cross-Validation, 129
91
--- page 119 ---
--- page 120 ---

CHAPTER 6
Ensemble Methods
6.1
MOTIVATION
In this chapter we will discuss two of the most popular ML ensemble methods.1 In the
references and footnotes you will find books and articles that introduce these techniques. As everywhere else in this book, the assumption is that you have already used
these approaches. The goal of this chapter is to explain what makes them effective,
and how to avoid common errors that lead to their misuse in finance.
6.2
THE THREE SOURCES OF ERRORS
ML models generally suffer from three errors:2
1. Bias: This error is caused by unrealistic assumptions. When bias is high, the
ML algorithm has failed to recognize important relations between features and
outcomes. In this situation, the algorithm is said to be “underfit.”
2. Variance: This error is caused by sensitivity to small changes in the training
set. When variance is high, the algorithm has overfit the training set, and that
is why even minimal changes in the training set can produce wildly different
predictions. Rather than modelling the general patterns in the training set, the
algorithm has mistaken noise with signal.
1 For
an
introduction
to
ensemble
methods,
please
visit:
http://scikit-learn.org/stable/modules/
ensemble.html.
2 I would not typically cite Wikipedia, however, on this subject the user may find some of the illustrations
in this article useful: https://en.wikipedia.org/wiki/Bias%E2%80%93variance_tradeoff.
93
--- page 121 ---

94
ENSEMBLE METHODS
3. Noise: This error is caused by the variance of the observed values, like unpredictable changes or measurement errors. This is the irreducible error, which
cannot be explained by any model.
Consider a training set of observations {xi}i=1,…,n and real-valued outcomes
{yi}i=1,…,n. Suppose a function f[x] exists, such that y = f[x] + 𝜀, where 𝜀is white
noise with E[𝜀i] = 0 and E[𝜀2
i ] = 𝜎2
𝜀. We would like to estimate the function̂ f[x]
that best fits f[x], in the sense of making the variance of the estimation error
E[(yi −̂ f[xi])
2] minimal (the mean squared error cannot be zero, because of the noise
represented by 𝜎2
𝜀). This mean-squared error can be decomposed as
E
[
(yi −̂ f[xi])
2]
=
⎛
⎜
⎜
⎜⎝
E[̂f[xi] −f[xi]]
⏟⏞⏞⏞⏞⏞⏞⏟⏞⏞⏞⏞⏞⏞⏟
bias
⎞
⎟
⎟
⎟⎠
2
+ V[̂f[xi]]
⏟⏟⏟
variance
+
𝜎2
𝜀
⏟⏟⏟
noise
An ensemble method is a method that combines a set of weak learners, all based
on the same learning algorithm, in order to create a (stronger) learner that performs
better than any of the individual ones. Ensemble methods help reduce bias and/or
variance.
6.3
BOOTSTRAP AGGREGATION
Bootstrap aggregation (bagging) is an effective way of reducing the variance in forecasts. It works as follows: First, generate N training datasets by random sampling with
replacement. Second, fit N estimators, one on each training set. These estimators are
fit independently from each other, hence the models can be fit in parallel. Third, the
ensemble forecast is the simple average of the individual forecasts from the N models.
In the case of categorical variables, the probability that an observation belongs to a
class is given by the proportion of estimators that classify that observation as a member of that class (majority voting). When the base estimator can make forecasts with
a prediction probability, the bagging classifier may derive a mean of the probabilities.
If you use sklearn’s BaggingClassiﬁer class to compute the out-of-bag
accuracy, you should be aware of this bug: https://github.com/scikit-learn/scikitlearn/issues/8933. One workaround is to rename the labels in integer sequential
order.
6.3.1
Variance Reduction
Bagging’s main advantage is that it reduces forecasts’ variance, hence helping address
overfitting. The variance of the bagged prediction (𝜑i[c]) is a function of the number
of bagged estimators (N), the average variance of a single estimator’s prediction (̄𝜎),
--- page 122 ---

BOOTSTRAP AGGREGATION
95
and the average correlation among their forecasts (̄𝜌):
V
[
1
N
N
∑
i=1
𝜑i[c]
]
= 1
N2
N
∑
i=1
( N
∑
j=1
𝜎i,j
)
= 1
N2
N
∑
i=1
(
𝜎2
i +
N
∑
j≠i
𝜎i𝜎j𝜌i,j
)
= 1
N2
N
∑
i=1
⎛
⎜
⎜
⎜
⎜
⎜
⎜
⎜
⎜⎝̄
𝜎2 +
N
∑
j≠ī
𝜎2̄𝜌
⏟⏟⏟
= (N −1)̄𝜎2̄𝜌
for a fixed i
⎞
⎟
⎟
⎟
⎟
⎟
⎟
⎟
⎟⎠
=̄ 𝜎2 + (N −1)̄𝜎2̄𝜌
N
=̄ 𝜎2
(̄
𝜌+ 1 −̄ 𝜌
N
)
where
𝜎i,j
is
the
covariance
of
predictions
by
estimators
i,j;
∑N
i=1̄ 𝜎2 =
∑N
i=1 𝜎2
i ⇔̄ 𝜎2 = N−1 ∑N
i=1 𝜎2
i ; and ∑N
j≠ī 𝜎2̄𝜌= ∑N
j≠i 𝜎i𝜎j𝜌i,j ⇔̄ 𝜌= (̄𝜎2N(N −1))−1
∑N
j≠i 𝜎i𝜎j𝜌i,j.
The equation above shows that bagging is only effective to the extent that̄ 𝜌<
1; as̄ 𝜌→1 ⇒V[ 1
N
∑N
i=1 𝜑i[c]] →̄ 𝜎2. One of the goals of sequential bootstrapping
(Chapter 4) is to produce samples as independent as possible, thereby reducinḡ 𝜌,
which should lower the variance of bagging classifiers. Figure 6.1 plots the standard
deviation of the bagged prediction as a function of N ∈[5, 30],̄ 𝜌∈[0, 1] and̄ 𝜎= 1.
FIGURE 6.1
Standard deviation of the bagged prediction
--- page 123 ---

96
ENSEMBLE METHODS
6.3.2
Improved Accuracy
Consider a bagging classifier that makes a prediction on k classes by majority voting
among N independent classifiers. We can label the predictions as {0,1}, where 1
means a correct prediction. The accuracy of a classifier is the probability p of labeling
a prediction as 1. On average we will get Np predictions labeled as 1, with variance
Np(1 −p). Majority voting makes the correct prediction when the most forecasted
class is observed. For example, for N = 10 and k = 3, the bagging classifier made
a correct prediction when class A was observed and the cast votes were [A, B, C] =
[4,3,3]. However, the bagging classifier made an incorrect prediction when class
A was observed and the cast votes were [A, B, C] = [4,1,5]. A sufficient condition
is that the sum of these labels is X > N
2 . A necessary (non-sufficient) condition is
that X > N
k , which occurs with probability
P
[
X > N
k
]
= 1 −P
[
X ≤N
k
]
= 1 −
⌊N∕k
⌋
∑
i=0
(
N
i
)
pi(1 −p)N−i
The implication is that for a sufficiently large N, say N > p(p −1∕k)−2, then
p > 1
k ⇒P[X > N
k ] > p, hence the bagging classifier’s accuracy exceeds the average
accuracy of the individual classifiers. Snippet 6.1 implements this calculation.
SNIPPET 6.1
ACCURACY OF THE BAGGING CLASSIFIER
from scipy.misc import comb
N,p,k=100,1./3,3.
p_=0
for i in xrange(0,int(N/k)+1):
p_+=comb(N,i)*p**i*(1-p)**(N-i)
print p,1-p_
This is a strong argument in favor of bagging any classifier in general, when
computational requirements permit it. However, unlike boosting, bagging cannot
improve the accuracy of poor classifiers: If the individual learners are poor classifiers
(p ≪1
k), majority voting will still perform poorly (although with lower variance).
Figure 6.2 illustrates these facts. Because it is easier to achievē 𝜌≪1 than p > 1
k,
bagging is more likely to be successful in reducing variance than in reducing bias.
For further analysis on this topic, the reader is directed to Condorcet’s Jury Theorem. Although the theorem is derived for the purposes of majority voting in political
--- page 124 ---

BOOTSTRAP AGGREGATION
97
FIGURE 6.2
Accuracy of a bagging classifier as a function of the individual estimator’s accuracy (P),
the number of estimators (N), and k = 2
science, the problem addressed by this theorem shares similarities with the above
discussion.
6.3.3
Observation Redundancy
In Chapter 4 we studied one reason why financial observations cannot be assumed to
be IID. Redundant observations have two detrimental effects on bagging. First, the
samples drawn with replacement are more likely to be virtually identical, even if they
do not share the same observations. This makes̄ 𝜌≈1, and bagging will not reduce
variance, regardless of N. For example, if each observation at t is labeled according
to the return between t and t + 100, we should sample 1% of the observations per
bagged estimator, but not more. Chapter 4, Section 4.5 recommended three alternative
solutions, one of which consisted of setting max_samples=out['tW'].mean() in
sklearn’s implementation of the bagging classifier class. Another (better) solution
was to apply the sequential bootstrap method.
The second detrimental effect from observation redundancy is that out-of-bag
accuracy will be inflated. This happens because random sampling with replacement
places in the training set samples that are very similar to those out-of-bag. In
such a case, a proper stratified k-fold cross-validation without shuffling before
partitioning will show a much lower testing-set accuracy than the one estimated
out-of-bag. For this reason, it is advisable to set StratiﬁedKFold(n_splits=k,
shufﬂe=False) when using that sklearn class, cross-validate the bagging classifier,
and ignore the out-of-bag accuracy results. A low number k is preferred to a high
--- page 125 ---

98
ENSEMBLE METHODS
one, as excessive partitioning would again place in the testing set samples too similar
to those used in the training set.
6.4
RANDOM FOREST
Decision trees are known to be prone to overfitting, which increases the variance of
the forecasts.3 In order to address this concern, the random forest (RF) method was
designed to produce ensemble forecasts with lower variance.
RF shares some similarities with bagging, in the sense of training independently
individual estimators over bootstrapped subsets of the data. The key difference with
bagging is that random forests incorporate a second level of randomness: When
optimizing each node split, only a random subsample (without replacement) of the
attributes will be evaluated, with the purpose of further decorrelating the estimators.
Like bagging, RF reduces forecasts’ variance without overfitting (remember, as
long as̄ 𝜌< 1). A second advantage is that RF evaluates feature importance, which
we will discuss in depth in Chapter 8. A third advantage is that RF provides out-of-bag
accuracy estimates, however in financial applications they are likely to be inflated (as
discussed in Section 6.3.3). But like bagging, RF will not necessarily exhibit lower
bias than individual decision trees.
If a large number of samples are redundant (non-IID), overfitting will still take
place: Sampling randomly with replacement will build a large number of essentially identical trees (̄𝜌≈1), where each decision tree is overfit (a flaw for which
decision trees are notorious). Unlike bagging, RF always fixes the size of the bootstrapped samples to match the size of the training dataset. Let us review ways
we can address this RF overfitting problem in sklearn. For illustration purposes,
I will refer to sklearn’s classes; however, these solutions can be applied to any
implementation:
1. Set a parameter max_features to a lower value, as a way of forcing discrepancy between trees.
2. Early stopping: Set the regularization parameter min_weight_fraction_
leaf to a sufficiently large value (e.g., 5%) such that out-of-bag accuracy converges to out-of-sample (k-fold) accuracy.
3. Use
BaggingClassiﬁer
on
DecisionTreeClassiﬁer
where
max_
samples is set to the average uniqueness (avgU) between samples.
(a) clf=DecisionTreeClassiﬁer(criterion='entropy',max_
features='auto',class_weight='balanced')
(b) bc=BaggingClassiﬁer(base_estimator=clf,n_estimators=
1000,max_samples=avgU,max_features=1.)
4. Use
BaggingClassiﬁer
on
RandomForestClassiﬁer
where
max_
samples is set to the average uniqueness (avgU) between samples.
3 For an intuitive explanation of Random Forest, visit the following link: https://quantdare.com/random
-forest-many-is-better-than-one/.
--- page 126 ---

BOOSTING
99
(a) clf=RandomForestClassiﬁer(n_estimators=1,criterion=
'entropy',bootstrap=False,class_weight='balanced_
subsample')
(b) bc=BaggingClassiﬁer(base_estimator=clf,n_estimators=
1000,max_samples=avgU,max_features=1.)
5. Modify the RF class to replace standard bootstrapping with sequential bootstrapping.
In summary, Snippet 6.2 demonstrates three alternative ways of setting up an RF,
using different classes.
SNIPPET 6.2
THREE WAYS OF SETTING UP AN RF
clf0=RandomForestClassiﬁer(n_estimators=1000,class_weight='balanced_subsample',
criterion='entropy')
clf1=DecisionTreeClassiﬁer(criterion='entropy',max_features='auto',
class_weight='balanced')
clf1=BaggingClassiﬁer(base_estimator=clf1,n_estimators=1000,max_samples=avgU)
clf2=RandomForestClassiﬁer(n_estimators=1,criterion='entropy',bootstrap=False,
class_weight='balanced_subsample')
clf2=BaggingClassiﬁer(base_estimator=clf2,n_estimators=1000,max_samples=avgU,
max_features=1.)
When fitting decision trees, a rotation of the features space in a direction that
aligns with the axes typically reduces the number of levels needed by the tree. For this
reason, I suggest you fit RF on a PCA of the features, as that may speed up calculations
and reduce some overfitting (more on this in Chapter 8). Also, as discussed in Chapter
4, Section 4.8, class_weight='balanced_subsample' will help you prevent the
trees from misclassifying minority classes.
6.5
BOOSTING
Kearns and Valiant [1989] were among the first to ask whether one could combine
weak estimators in order to achieve one with high accuracy. Shortly after, Schapire
[1990] demonstrated that the answer to that question was affirmative, using the procedure we today call boosting. In general terms, it works as follows: First, generate
one training set by random sampling with replacement, according to some sample
weights (initialized with uniform weights). Second, fit one estimator using that training set. Third, if the single estimator achieves an accuracy greater than the acceptance
threshold (e.g., 50% in a binary classifier, so that it performs better than chance), the
estimator is kept, otherwise it is discarded. Fourth, give more weight to misclassified
observations, and less weight to correctly classified observations. Fifth, repeat the
previous steps until N estimators are produced. Sixth, the ensemble forecast is the
weighted average of the individual forecasts from the N models, where the weights
--- page 127 ---

100
ENSEMBLE METHODS
FIGURE 6.3
AdaBoost decision flow
are determined by the accuracy of the individual estimators. There are many boosting
algorithms, of which AdaBoost is one of the most popular (Geron [2017]). Figure 6.3
summarizes the decision flow of a standard AdaBoost implementation.
6.6
BAGGING VS. BOOSTING IN FINANCE
From the above description, a few aspects make boosting quite different from
bagging:4
r Individual classifiers are fit sequentially.
r Poor-performing classifiers are dismissed.
4 For a visual explanation of the difference between bagging and boosting, visit: https://quantdare.com/
what-is-the-difference-between-bagging-and-boosting/.
--- page 128 ---

EXERCISES
101
r Observations are weighted differently in each iteration.
r The ensemble forecast is a weighted average of the individual learners.
Boosting’s main advantage is that it reduces both variance and bias in forecasts.
However, correcting bias comes at the cost of greater risk of overfitting. It could
be argued that in financial applications bagging is generally preferable to boosting. Bagging addresses overfitting, while boosting addresses underfitting. Overfitting is often a greater concern than underfitting, as it is not difficult to overfit an
ML algorithm to financial data, because of the low signal-to-noise ratio. Furthermore, bagging can be parallelized, while generally boosting requires sequential
running.
6.7
BAGGING FOR SCALABILITY
As you know, several popular ML algorithms do not scale well with the sample size.
Support vector machines (SVMs) are a prime example. If you attempt to fit an SVM
on a million observations, it may take a while until the algorithm converges. And even
once it has converged, there is no guarantee that the solution is a global optimum, or
that it is not overfit.
One practical approach is to build a bagging algorithm, where the base estimator belongs to a class that does not scale well with the sample size, like SVM.
When defining that base estimator, we will impose a tight early stopping condition.
For example, in sklearn’s SVM implementation, you could set a low value for the
max_iter parameter, say 1E5 iterations. The default value is max_iter=-1, which
tells the estimator to continue performing iterations until errors fall below a tolerance level. Alternatively, you could raise the tolerance level through the parameter tol, which has a default value tol=1E-3. Either of these two parameters will
force an early stop. You can stop other algorithms early with equivalent parameters,
like the number of levels in an RF (max_depth), or the minimum weighted fraction
of the sum total of weights (of all the input samples) required to be at a leaf node
(min_weight_fraction_leaf).
Given that bagging algorithms can be parallelized, we are transforming a large
sequential task into many smaller ones that are run simultaneously. Of course, the
early stopping will increase the variance of the outputs from the individual base estimators; however, that increase can be more than offset by the variance reduction associated with the bagging algorithm. You can control that reduction by adding more
independent base estimators. Used in this way, bagging will allow you to achieve fast
and robust estimates on extremely large datasets.
EXERCISES
6.1 Why is bagging based on random sampling with replacement? Would bagging
still reduce a forecast’s variance if sampling were without replacement?
--- page 129 ---

102
ENSEMBLE METHODS
6.2 Suppose that your training set is based on highly overlap labels (i.e., with low
uniqueness, as defined in Chapter 4).
(a) Does this make bagging prone to overfitting, or just ineffective? Why?
(b) Is out-of-bag accuracy generally reliable in financial applications? Why?
6.3 Build an ensemble of estimators, where the base estimator is a decision tree.
(a) How is this ensemble different from an RF?
(b) Using sklearn, produce a bagging classifier that behaves like an RF. What
parameters did you have to set up, and how?
6.4 Consider the relation between an RF, the number of trees it is composed of, and
the number of features utilized:
(a) Could you envision a relation between the minimum number of trees needed
in an RF and the number of features utilized?
(b) Could the number of trees be too small for the number of features used?
(c) Could the number of trees be too high for the number of observations available?
6.5 How is out-of-bag accuracy different from stratified k-fold (with shuffling) crossvalidation accuracy?
REFERENCES
Geron, A. (2017): Hands-on Machine Learning with Scikit-Learn and TensorFlow: Concepts, Tools,
and Techniques to Build Intelligent Systems, 1st edition. O’Reilly Media.
Kearns, M. and L. Valiant (1989): “Cryptographic limitations on learning Boolean formulae and
finite automata.” In Proceedings of the 21st Annual ACM Symposium on Theory of Computing,
pp. 433–444, New York. Association for Computing Machinery.
Schapire, R. (1990): “The strength of weak learnability.” Machine Learning. Kluwer Academic
Publishers. Vol. 5 No. 2, pp. 197–227.
BIBLIOGRAPHY
Gareth, J., D. Witten, T. Hastie, and R. Tibshirani (2013): An Introduction to Statistical Learning:
With Applications in R, 1st ed. Springer-Verlag.
Hackeling, G. (2014): Mastering Machine Learning with Scikit-Learn, 1st ed. Packt Publishing.
Hastie, T., R. Tibshirani and J. Friedman (2016): The Elements of Statistical Learning, 2nd ed.
Springer-Verlag.
Hauck, T. (2014): Scikit-Learn Cookbook, 1st ed. Packt Publishing.
Raschka, S. (2015): Python Machine Learning, 1st ed. Packt Publishing.
--- page 130 ---

CHAPTER 7
Cross-Validation in Finance
7.1
MOTIVATION
The purpose of cross-validation (CV) is to determine the generalization error of an
ML algorithm, so as to prevent overfitting. CV is yet another instance where standard ML techniques fail when applied to financial problems. Overfitting will take
place, and CV will not be able to detect it. In fact, CV will contribute to overfitting
through hyper-parameter tuning. In this chapter we will learn why standard CV fails
in finance, and what can be done about it.
7.2
THE GOAL OF CROSS-VALIDATION
One of the purposes of ML is to learn the general structure of the data, so that we
can produce predictions on future, unseen features. When we test an ML algorithm
on the same dataset as was used for training, not surprisingly, we achieve spectacular
results. When ML algorithms are misused that way, they are no different from file
lossy-compression algorithms: They can summarize the data with extreme fidelity,
yet with zero forecasting power.
CV splits observations drawn from an IID process into two sets: the training set
and the testing set. Each observation in the complete dataset belongs to one, and only
one, set. This is done as to prevent leakage from one set into the other, since that
would defeat the purpose of testing on unseen data. Further details can be found in
the books and articles listed in the references section.
There are many alternative CV schemes, of which one of the most popular is kfold CV. Figure 7.1 illustrates the k train/test splits carried out by a k-fold CV, where
k = 5. In this scheme:
1. The dataset is partitioned into k subsets.
2. For i = 1,…,k
103
--- page 131 ---

104
CROSS-VALIDATION IN FINANCE
FIGURE 7.1
Train/test splits in a 5-fold CV scheme
(a) The ML algorithm is trained on all subsets excluding i.
(b) The fitted ML algorithm is tested on i.
The outcome from k-fold CV is a kx1 array of cross-validated performance metrics. For example, in a binary classifier, the model is deemed to have learned something if the cross-validated accuracy is over 1/2, since that is the accuracy we would
achieve by tossing a fair coin.
In finance, CV is typically used in two settings: model development (like hyperparameter tuning) and backtesting. Backtesting is a complex subject that we will discuss thoroughly in Chapters 10–16. In this chapter, we will focus on CV for model
development.
7.3
WHY K-FOLD CV FAILS IN FINANCE
By now you may have read quite a few papers in finance that present k-fold CV
evidence that an ML algorithm performs well. Unfortunately, it is almost certain that
those results are wrong. One reason k-fold CV fails in finance is because observations
cannot be assumed to be drawn from an IID process. A second reason for CV’s failure
is that the testing set is used multiple times in the process of developing a model,
leading to multiple testing and selection bias. We will revisit this second cause of
failure in Chapters 11–13. For the time being, let us concern ourselves exclusively
with the first cause of failure.
Leakage takes place when the training set contains information that also appears
in the testing set. Consider a serially correlated feature X that is associated with labels
Y that are formed on overlapping data:
--- page 132 ---

A SOLUTION: PURGED K-FOLD CV
105
r Because of the serial correlation, Xt ≈Xt+1.
r Because labels are derived from overlapping datapoints, Yt ≈Yt+1.
By placing t and t + 1 in different sets, information is leaked. When a classifier
is first trained on (Xt, Yt), and then it is asked to predict E[Yt+1|Xt+1] based on an
observed Xt+1, this classifier is more likely to achieve Yt+1 = E[Yt+1|Xt+1] even if X
is an irrelevant feature.
If X is a predictive feature, leakage will enhance the performance of an already
valuable strategy. The problem is leakage in the presence of irrelevant features, as
this leads to false discoveries. There are at least two ways to reduce the likelihood of
leakage:
1. Drop from the training set any observation i where Yi is a function of information used to determine Yj, and j belongs to the testing set.
(a) For example, Yi and Yj should not span overlapping periods (see Chapter 4
for a discussion of sample uniqueness).
2. Avoid overfitting the classifier. In this way, even if some leakage occurs, the
classifier will not be able to profit from it. Use:
(a) Early stopping of the base estimators (see Chapter 6).
(b) Bagging of classifiers, while controlling for oversampling on redundant
examples, so that the individual classifiers are as diverse as possible.
i. Set max_samples to the average uniqueness.
ii. Apply sequential bootstrap (Chapter 4).
Consider the case where Xi and Xj are formed on overlapping information, where
i belongs to the training set and j belongs to the testing set. Is this a case of informational leakage? Not necessarily, as long as Yi and Yj are independent. For leakage to
take place, it must occur that (Xi, Yi) ≈(Xj, Yj), and it does not suffice that Xi ≈Xj or
even Yi ≈Yj.
7.4
A SOLUTION: PURGED K-FOLD CV
One way to reduce leakage is to purge from the training set all observations whose
labels overlapped in time with those labels included in the testing set. I call this
process “purging.” In addition, since financial features often incorporate series that
exhibit serial correlation (like ARMA processes), we should eliminate from the training set observations that immediately follow an observation in the testing set. I call
this process “embargo.”
7.4.1
Purging the Training Set
Suppose a testing observation whose label Yj is decided based on the information set
Φj. In order to prevent the type of leakage described in the previous section, we would
--- page 133 ---

106
CROSS-VALIDATION IN FINANCE
like to purge from the training set any observation whose label Yi is decided based on
the information set Φi, such that Φi ∩Φj = ∅.
In particular, we will determine that there is informational overlap between two
observations i and j whenever Yi and Yj are concurrent (see Chapter 4, Section 4.3),
in the sense that both labels are contingent on at least one common random draw. For
example, consider a label Yj that is a function of observations in the closed range t ∈
[tj,0, tj,1], Yj = f[[tj,0, tj,1]] (with some abuse of notation). For example, in the context
of the triple-barrier labeling method (Chapter 3), it means that the label is the sign of
the return spanning between price bars with indices tj,0 and tj,1, that is sgn[rtj,0,tj,1]. A
label Yi = f[[ti,0, ti,1]] overlaps with Yj if any of the three sufficient conditions is met:
1. tj,0 ≤ti,0 ≤tj,1
2. tj,0 ≤ti,1 ≤tj,1
3. ti,0 ≤tj,0 ≤tj,1 ≤ti,1
Snippet 7.1 implements this purging of observations from the training set. If the
testing set is contiguous, in the sense that no training observations occur between
the first and last testing observation, then purging can be accelerated: The object
testTimes can be a pandas series with a single item, spanning the entire testing
set.
SNIPPET 7.1
PURGING OBSERVATION IN THE TRAINING SET
def getTrainTimes(t1,testTimes):
’’’
Given testTimes, find the times of the training observations.
—t1.index: Time when the observation started.
—t1.value: Time when the observation ended.
—testTimes: Times of testing observations.
’’’
trn=t1.copy(deep=True)
for i,j in testTimes.iteritems():
df0=trn[(i<=trn.index)&(trn.index<=j)].index # train starts within test
df1=trn[(i<=trn)&(trn<=j)].index # train ends within test
df2=trn[(trn.index<=i)&(j<=trn)].index # train envelops test
trn=trn.drop(df0.union(df1).union(df2))
return trn
When leakage takes place, performance improves merely by increasing k →T,
where T is the number of bars. The reason is that the larger the number of testing
splits, the greater the number of overlapping observations in the training set. In many
cases, purging suffices to prevent leakage: Performance will improve as we increase
k, because we allow the model to recalibrate more often. But beyond a certain value
--- page 134 ---

A SOLUTION: PURGED K-FOLD CV
107
FIGURE 7.2
Purging overlap in the training set
k∗, performance will not improve, indicating that the backtest is not profiting from
leaks. Figure 7.2 plots one partition of the k-fold CV. The test set is surrounded by
two train sets, generating two overlaps that must be purged to prevent leakage.
7.4.2
Embargo
For those cases where purging is not able to prevent all leakage, we can impose
an embargo on training observations after every test set. The embargo does not
need to affect training observations prior to a test set, because training labels Yi =
f[[ti,0, ti,1]], where ti,1 < tj,0 (training ends before testing begins), contain information that was available at the testing time tj,0. In other words, we are only concerned with training labels Yi = f[[ti,0, ti,1]] that take place immediately after the
test, tj,1 ≤ti,0 ≤tj,1 + h. We can implement this embargo period h by setting Yj =
f[[tj,0, tj,1 + h]] before purging. A small value h ≈.01T often suffices to prevent
all leakage, as can be confirmed by testing that performance does not improve
indefinitely by increasing k →T. Figure 7.3 illustrates the embargoing of train
observations immediately after the testing set. Snippet 7.2 implements the embargo
logic.
