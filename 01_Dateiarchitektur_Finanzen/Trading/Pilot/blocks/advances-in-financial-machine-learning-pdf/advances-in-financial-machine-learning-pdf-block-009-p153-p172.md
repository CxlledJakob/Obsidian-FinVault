# Advances in Financial Machine Learning.pdf — pages 153–172

--- page 153 ---

FIGURE 8.3
MDA feature importance computed on a synthetic dataset
FIGURE 8.4
SFI feature importance computed on a synthetic dataset
--- page 154 ---

REFERENCES
127
The labels are a function of a combination of features, and trying to forecast them
independently misses the joint effects. Still, SFI is useful as a complement to MDI
and MDA, precisely because both types of analyses are affected by different kinds of
problems.
EXERCISES
8.1 Using the code presented in Section 8.6:
(a) Generate a dataset (X, y).
(b) Apply a PCA transformation on X, which we denotė X.
(c) Compute MDI, MDA, and SFI feature importance on (̇X, y), where the base
estimator is RF.
(d) Do the three methods agree on what features are important? Why?
8.2 From exercise 1, generate a new dataset (̈X, y), wherë X is a feature union of X
anḋ X.
(a) Compute MDI, MDA, and SFI feature importance on (̈X, y), where the base
estimator is RF.
(b) Do the three methods agree on the important features? Why?
8.3 Take the results from exercise 2:
(a) Drop the most important features according to each method, resulting in a
features matrix⃛X.
(b) Compute MDI, MDA, and SFI feature importance on (⃛X, y), where the base
estimator is RF.
(c) Do you appreciate significant changes in the rankings of important features,
relative to the results from exercise 2?
8.4 Using the code presented in Section 8.6:
(a) Generate a dataset (X, y) of 1E6 observations, where 5 features are informative, 5 are redundant and 10 are noise.
(b) Split (X, y) into 10 datasets {(Xi, yi)}i=1,…,10, each of 1E5 observations.
(c) Compute the parallelized feature importance (Section 8.5), on each of the 10
datasets, {(Xi, yi)}i=1,…,10.
(d) Compute the stacked feature importance on the combined dataset (X, y).
(e) What causes the discrepancy between the two? Which one is more reliable?
8.5 Repeat all MDI calculations from exercises 1–4, but this time allow for masking
effects. That means, do not set max_features=int(1) in Snippet 8.2. How do
results differ as a consequence of this change? Why?
REFERENCES
American Statistical Association (2016): “Ethical guidelines for statistical practice.” Committee on Professional Ethics of the American Statistical Association (April). Available at
http://www.amstat.org/asa/files/pdfs/EthicalGuidelines.pdf.
--- page 155 ---

128
FEATURE IMPORTANCE
Belsley, D., E. Kuh, and R. Welsch (1980): Regression Diagnostics: Identifying Influential Data and
Sources of Collinearity, 1st ed. John Wiley & Sons.
Goldberger, A. (1991): A Course in Econometrics. Harvard University Press, 1st edition.
Hill, R. and L. Adkins (2001): “Collinearity.” In Baltagi, Badi H. A Companion to Theoretical Econometrics, 1st ed. Blackwell, pp. 256–278.
Louppe, G., L. Wehenkel, A. Sutera, and P. Geurts (2013): “Understanding variable importances
in forests of randomized trees.” Proceedings of the 26th International Conference on Neural
Information Processing Systems, pp. 431–439.
Strobl, C., A. Boulesteix, A. Zeileis, and T. Hothorn (2007): “Bias in random forest variable importance measures: Illustrations, sources and a solution.” BMC Bioinformatics, Vol. 8, No. 25,
pp. 1–11.
White, A. and W. Liu (1994): “Technical note: Bias in information-based measures in decision tree
induction.” Machine Learning, Vol. 15, No. 3, pp. 321–329.
--- page 156 ---

CHAPTER 9
Hyper-Parameter Tuning with
Cross-Validation
9.1
MOTIVATION
Hyper-parameter tuning is an essential step in fitting an ML algorithm. When this
is not done properly, the algorithm is likely to overfit, and live performance will
disappoint. The ML literature places special attention on cross-validating any tuned
hyper-parameter. As we have seen in Chapter 7, cross-validation (CV) in finance is
an especially difficult problem, where solutions from other fields are likely to fail. In
this chapter we will discuss how to tune hyper-parameters using the purged k-fold
CV method. The references section lists studies that propose alternative methods that
may be useful in specific problems.
9.2
GRID SEARCH CROSS-VALIDATION
Grid search cross-validation conducts an exhaustive search for the combination of
parameters that maximizes the CV performance, according to some user-defined
score function. When we do not know much about the underlying structure of the
data, this is a reasonable first approach. Scikit-learn has implemented this logic in
the function GridSearchCV, which accepts a CV generator as an argument. For
the reasons explained in Chapter 7, we need to pass our PurgedKFold class (Snippet 7.3) in order to prevent that GridSearchCV overfits the ML estimator to leaked
information.
129
--- page 157 ---

130
HYPER-PARAMETER TUNING WITH CROSS-VALIDATION
SNIPPET 9.1
GRID SEARCH WITH PURGED K-FOLD
CROSS-VALIDATION
def clfHyperFit(feat,lbl,t1,pipe_clf,param_grid,cv=3,bagging=[0,None,1.],
n_jobs=-1,pctEmbargo=0,**ﬁt_params):
if set(lbl.values)=={0,1}:scoring='f1' # f1 for meta-labeling
else:scoring='neg_log_loss' # symmetric towards all cases
#1) hyperparameter search, on train data
inner_cv=PurgedKFold(n_splits=cv,t1=t1,pctEmbargo=pctEmbargo) # purged
gs=GridSearchCV(estimator=pipe_clf,param_grid=param_grid,
scoring=scoring,cv=inner_cv,n_jobs=n_jobs,iid=False)
gs=gs.ﬁt(feat,lbl,**ﬁt_params).best_estimator_ # pipeline
#2) fit validated model on the entirety of the data
if bagging[1]>0:
gs=BaggingClassiﬁer(base_estimator=MyPipeline(gs.steps),
n_estimators=int(bagging[0]),max_samples=ﬂoat(bagging[1]),
max_features=ﬂoat(bagging[2]),n_jobs=n_jobs)
gs=gs.ﬁt(feat,lbl,sample_weight=ﬁt_params \
[gs.base_estimator.steps[-1][0]+'__sample_weight'])
gs=Pipeline([('bag',gs)])
return gs
Snippet
9.1
lists
function
clfHyperFit,
which
implements
a
purged
GridSearchCV. The argument ﬁt_params can be used to pass sample_weight,
and param_grid contains the values that will be combined into a grid. In addition,
this function allows for the bagging of the tuned estimator. Bagging an estimator is
generally a good idea for the reasons explained in Chapter 6, and the above function
incorporates logic to that purpose.
I advise you to use scoring='f1' in the context of meta-labeling applications,
for the following reason. Suppose a sample with a very large number of negative (i.e.,
label ‘0’) cases. A classifier that predicts all cases to be negative will achieve high
'accuracy' or 'neg_log_loss', even though it has not learned from the features
how to discriminate between cases. In fact, such a model achieves zero recall and
undefined precision (see Chapter 3, Section 3.7). The 'f1' score corrects for that
performance inflation by scoring the classifier in terms of precision and recall (see
Chapter 14, Section 14.8).
For other (non-meta-labeling) applications, it is fine to use 'accuracy' or
'neg_log_loss', because we are equally interested in predicting all cases. Note
that a relabeling of cases has no impact on 'accuracy' or 'neg_log_loss', however it will have an impact on 'f1'.
This example introduces nicely one limitation of sklearn’s Pipelines : Their
fit method does not expect a sample_weight argument. Instead, it expects a
ﬁt_params keyworded argument. That is a bug that has been reported in GitHub;
however, it may take some time to fix it, as it involves rewriting and testing much
functionality. Until then, feel free to use the workaround in Snippet 9.2. It creates a
--- page 158 ---

RANDOMIZED SEARCH CROSS-VALIDATION
131
new class, called MyPipeline, which inherits all methods from sklearn’s Pipeline.
It overwrites the inherited ﬁt method with a new one that handles the argument
sample_weight, after which it redirects to the parent class.
SNIPPET 9.2
AN ENHANCED PIPELINE CLASS
class MyPipeline(Pipeline):
def ﬁt(self,X,y,sample_weight=None,**ﬁt_params):
if sample_weight is not None:
ﬁt_params[self.steps[-1][0]+'__sample_weight']=sample_weight
return super(MyPipeline,self).ﬁt(X,y,**ﬁt_params)
If you are not familiar with this technique for expanding classes, you may want
to read this introductory Stackoverflow post: http://stackoverflow.com/questions/
576169/understanding-python-super-with-init-methods.
9.3
RANDOMIZED SEARCH CROSS-VALIDATION
For ML algorithms with a large number of parameters, a grid search cross-validation
(CV) becomes computationally intractable. In this case, an alternative with good statistical properties is to sample each parameter from a distribution (Begstra et al. [2011,
2012]). This has two benefits: First, we can control for the number of combinations
we will search for, regardless of the dimensionality of the problem (the equivalent
to a computational budget). Second, having parameters that are relatively irrelevant
performance-wise will not substantially increase our search time, as would be the
case with grid search CV.
Rather than writing a new function to work with RandomizedSearchCV, let us
expand Snippet 9.1 to incorporate an option to this purpose. A possible implementation is Snippet 9.3.
SNIPPET 9.3
RANDOMIZED SEARCH WITH PURGED K-FOLD CV
def clfHyperFit(feat,lbl,t1,pipe_clf,param_grid,cv=3,bagging=[0,None,1.],
rndSearchIter=0,n_jobs=-1,pctEmbargo=0,**ﬁt_params):
if set(lbl.values)=={0,1}:scoring='f1' # f1 for meta-labeling
else:scoring='neg_log_loss' # symmetric towards all cases
#1) hyperparameter search, on train data
inner_cv=PurgedKFold(n_splits=cv,t1=t1,pctEmbargo=pctEmbargo) # purged
if rndSearchIter==0:
gs=GridSearchCV(estimator=pipe_clf,param_grid=param_grid,
scoring=scoring,cv=inner_cv,n_jobs=n_jobs,iid=False)
else:
--- page 159 ---

132
HYPER-PARAMETER TUNING WITH CROSS-VALIDATION
gs=RandomizedSearchCV(estimator=pipe_clf,param_distributions= \
param_grid,scoring=scoring,cv=inner_cv,n_jobs=n_jobs,
iid=False,n_iter=rndSearchIter)
gs=gs.ﬁt(feat,lbl,**ﬁt_params).best_estimator_ # pipeline
#2) fit validated model on the entirety of the data
if bagging[1]>0:
gs=BaggingClassiﬁer(base_estimator=MyPipeline(gs.steps),
n_estimators=int(bagging[0]),max_samples=ﬂoat(bagging[1]),
max_features=ﬂoat(bagging[2]),n_jobs=n_jobs)
gs=gs.ﬁt(feat,lbl,sample_weight=ﬁt_params \
[gs.base_estimator.steps[-1][0]+'__sample_weight'])
gs=Pipeline([('bag',gs)])
return gs
9.3.1
Log-Uniform Distribution
It is common for some ML algorithms to accept non-negative hyper-parameters only.
That is the case of some very popular parameters, such as C in the SVC classifier
and gamma in the RBF kernel.1 We could draw random numbers from a uniform
distribution bounded between 0 and some large value, say 100. That would mean that
99% of the values would be expected to be greater than 1. That is not necessarily the
most effective way of exploring the feasibility region of parameters whose functions
do not respond linearly. For example, an SVC can be as responsive to an increase in C
from 0.01 to 1 as to an increase in C from 1 to 100.2 So sampling C from a U [0, 100]
(uniform) distribution will be inefficient. In those instances, it seems more effective to
draw values from a distribution where the logarithm of those draws will be distributed
uniformly. I call that a “log-uniform distribution,” and since I could not find it in the
literature, I must define it properly.
A random variable x follows a log-uniform distribution between a > 0 and b > a
if and only if log [x] ∼U [log [a] , log [b]
]. This distribution has a CDF:
F [x] =
⎧
⎪
⎨
⎪⎩
log [x] −log [a]
log [b] −log [a]
for a ≤x ≤b
0
for x < a
1
for x > b
From this, we derive a PDF:
f [x] =
⎧
⎪
⎨
⎪⎩
1
x log [b∕a]
for a ≤x ≤b
0
for x < a
0
for x > b
Note that the CDF is invariant to the base of the logarithm, since
log
[ x
a
]
log
[ b
a
] =
logc
[ x
a
]
logc
[ b
a
]
for any base c, thus the random variable is not a function of c. Snippet 9.4 implements
1 http://scikit-learn.org/stable/modules/metrics.html.
2 http://scikit-learn.org/stable/auto_examples/svm/plot_rbf_parameters.html.
--- page 160 ---

RANDOMIZED SEARCH CROSS-VALIDATION
133
1000
800
600
400
200
0
–5
0
0
0
1000
2000
3000
4000
5000
6000
7000
8000
250
500
750
1000
5
FIGURE 9.1
Result from testing the logUniform_gen class
(and tests) in scipy.stats a random variable where [a, b] = [1E −3, 1E3], hence
log [x] ∼U [log [1E −3] , log [1E3]
]. Figure 9.1 illustrates the uniformity of the samples in log-scale.
SNIPPET 9.4
THE logUniform_gen CLASS
import numpy as np,pandas as pd,matplotlib.pyplot as mpl
from scipy.stats import rv_continuous,kstest
#———————————————————————————————————————
class logUniform_gen(rv_continuous):
# random numbers log-uniformly distributed between 1 and e
def _cdf(self,x):
return np.log(x/self.a)/np.log(self.b/self.a)
def logUniform(a=1,b=np.exp(1)):return logUniform_gen(a=a,b=b,name='logUniform')
#———————————————————————————————————————
a,b,size=1E-3,1E3,10000
vals=logUniform(a=a,b=b).rvs(size=size)
print kstest(rvs=np.log(vals),cdf='uniform',args=(np.log(a),np.log(b/a)),N=size)
print pd.Series(vals).describe()
mpl.subplot(121)
pd.Series(np.log(vals)).hist()
mpl.subplot(122)
pd.Series(vals).hist()
mpl.show()
--- page 161 ---

134
HYPER-PARAMETER TUNING WITH CROSS-VALIDATION
9.4
SCORING AND HYPER-PARAMETER TUNING
Snippets 9.1 and 9.3 set scoring='f1' for meta-labeling applications. For
other applications, they set scoring='neg_log_loss' rather than the standard
scoring='accuracy'. Although accuracy has a more intuitive interpretation, I
suggest that you use neg_log_loss when you are tuning hyper-parameters for an
investment strategy. Let me explain my reasoning.
Suppose that your ML investment strategy predicts that you should buy a security, with high probability. You will enter a large long position, as a function of the
strategy’s confidence. If the prediction was erroneous, and the market sells off instead,
you will lose a lot of money. And yet, accuracy accounts equally for an erroneous buy
prediction with high probability and for an erroneous buy prediction with low probability. Moreover, accuracy can offset a miss with high probability with a hit with low
probability.
Investment strategies profit from predicting the right label with high confidence.
Gains from good predictions with low confidence will not suffice to offset the losses
from bad predictions with high confidence. For this reason, accuracy does not provide
a realistic scoring of the classifier’s performance. Conversely, log loss3 (aka crossentropy loss) computes the log-likelihood of the classifier given the true label, which
takes predictions’ probabilities into account. Log loss can be estimated as follows:
L [Y, P] = −log [Prob [Y |P]] = −N−1
N−1
∑
n=0
K−1
∑
k=0
yn,klog [pn,k
]
where
r pn,k is the probability associated with prediction n of label k.
r Y is a 1-of-K binary indicator matrix, such that yn,k = 1 when observation n was
assigned label k out of K possible labels, and 0 otherwise.
Suppose that a classifier predicts two 1s, where the true labels are 1 and 0. The first
prediction is a hit and the second prediction is a miss, thus accuracy is 50%. Figure 9.2
plots the cross-entropy loss when these predictions come from probabilities ranging
[0.5, 0.9]. One can observe that on the right side of the figure, log loss is large due to
misses with high probability, even though the accuracy is 50% in all cases.
There is a second reason to prefer cross-entropy loss over accuracy. CV scores a
classifier by applying sample weights (see Chapter 7, Section 7.5). As you may recall
from Chapter 4, observation weights were determined as a function of the observation’s absolute return. The implication is that sample weighted cross-entropy loss
estimates the classifier’s performance in terms of variables involved in a PnL (markto-market profit and losses) calculation: It uses the correct label for the side, probability for the position size, and sample weight for the observation’s return/outcome. That
3 http://scikit-learn.org/stable/modules/model_evaluation.html#log-loss.
--- page 162 ---

EXERCISES
135
FIGURE 9.2
Log loss as a function of predicted probabilities of hit and miss
is the right ML performance metric for hyper-parameter tuning of financial applications, not accuracy.
When we use log loss as a scoring statistic, we often prefer to change its sign,
hence referring to “neg log loss.” The reason for this change is cosmetic, driven by
intuition: A high neg log loss value is preferred to a low neg log loss value, just
as with accuracy. Keep in mind this sklearn bug when you use neg_log_loss:
https://github.com/scikit-learn/scikit-learn/issues/9144. To circumvent this bug, you
should use the cvScore function presented in Chapter 7.
EXERCISES
9.1 Using the function getTestData from Chapter 8, form a synthetic dataset of
10,000 observations with 10 features, where 5 are informative and 5 are noise.
(a) Use GridSearchCV on 10-fold CV to find the C, gamma optimal hyperparameters on a SVC with RBF kernel, where param_grid= {'C':[1E-
2,1E-1,1,10,100],'gamma':[1E-2,1E-1,1,10,100]} and the scoring function is neg_log_loss.
(b) How many nodes are there in the grid?
(c) How many fits did it take to find the optimal solution?
(d) How long did it take to find this solution?
--- page 163 ---

136
HYPER-PARAMETER TUNING WITH CROSS-VALIDATION
(e) How can you access the optimal result?
(f) What is the CV score of the optimal parameter combination?
(g) How can you pass sample weights to the SVC?
9.2 Using the same dataset from exercise 1,
(a) Use
RandomizedSearchCV
on
10-fold
CV
to
find
the
C,
gamma
optimal
hyper-parameters
on
an
SVC
with
RBF
kernel,
where
param_distributions= {'C':logUniform(a= 1E-2,b=
1E2),'gamma':logUniform(a= 1E-2,b= 1E2)},n_iter= 25
and
neg_log_loss is the scoring function.
(b) How long did it take to find this solution?
(c) Is the optimal parameter combination similar to the one found in exercise 1?
(d) What is the CV score of the optimal parameter combination? How does it
compare to the CV score from exercise 1?
9.3 From exercise 1,
(a) Compute the Sharpe ratio of the resulting in-sample forecasts, from point 1.a
(see Chapter 14 for a definition of Sharpe ratio).
(b) Repeat point 1.a, this time with accuracy as the scoring function. Compute
the in-sample forecasts derived from the hyper-tuned parameters.
(c) What scoring method leads to higher (in-sample) Sharpe ratio?
9.4 From exercise 2,
(a) Compute the Sharpe ratio of the resulting in-sample forecasts, from point
2.a.
(b) Repeat point 2.a, this time with accuracy as the scoring function. Compute
the in-sample forecasts derived from the hyper-tuned parameters.
(c) What scoring method leads to higher (in-sample) Sharpe ratio?
9.5 Read the definition of log loss, L [Y, P].
(a) Why is the scoring function neg_log_loss defined as the negative log loss,
−L [Y, P]?
(b) What would be the outcome of maximizing the log loss, rather than the negative log loss?
9.6 Consider an investment strategy that sizes its bets equally, regardless of the forecast’s confidence. In this case, what is a more appropriate scoring function for
hyper-parameter tuning, accuracy or cross-entropy loss?
REFERENCES
Bergstra, J., R. Bardenet, Y. Bengio, and B. Kegl (2011): “Algorithms for hyper-parameter optimization.” Advances in Neural Information Processing Systems, pp. 2546–2554.
Bergstra, J. and Y. Bengio (2012): “Random search for hyper-parameter optimization.” Journal of
Machine Learning Research, Vol. 13, pp. 281–305.
--- page 164 ---

BIBLIOGRAPHY
137
BIBLIOGRAPHY
Chapelle, O., V. Vapnik, O. Bousquet, and S. Mukherjee (2002): “Choosing multiple parameters for
support vector machines.” Machine Learning, Vol. 46, pp. 131–159.
Chuong, B., C. Foo, and A. Ng (2008): “Efficient multiple hyperparameter learning for loglinear models.” Advances in Neural Information Processing Systems, Vol. 20. Available at
http://ai.stanford.edu/~chuongdo/papers/learn_reg.pdf.
Gorissen, D., K. Crombecq, I. Couckuyt, P. Demeester, and T. Dhaene (2010): “A surrogate modeling and adaptive sampling toolbox for computer based design.” Journal of Machine Learning
Research, Vol. 11, pp. 2051–2055.
Hsu, C., C. Chang, and C. Lin (2010): “A practical guide to support vector classification.” Technical
report, National Taiwan University.
Hutter, F., H. Hoos, and K. Leyton-Brown (2011): “Sequential model-based optimization for general algorithm configuration.” Proceedings of the 5th international conference on Learning and
Intelligent Optimization, pp. 507–523.
Larsen, J., L. Hansen, C. Svarer, and M. Ohlsson (1996): “Design and regularization of neural networks: The optimal use of a validation set.” Proceedings of the 1996 IEEE Signal Processing
Society Workshop.
Maclaurin, D., D. Duvenaud, and R. Adams (2015): “Gradient-based hyperparameter optimization
through reversible learning.” Working paper. Available at https://arxiv.org/abs/1502.03492.
Martinez-Cantin, R. (2014): “BayesOpt: A Bayesian optimization library for nonlinear optimization,
experimental design and bandits.” Journal of Machine Learning Research, Vol. 15, pp. 3915–
3919.
--- page 165 ---
--- page 166 ---

P A R T 3
Backtesting
Chapter 10: Bet Sizing, 141
Chapter 11: The Dangers of Backtesting, 151
Chapter 12: Backtesting through Cross-Validation, 161
Chapter 13: Backtesting on Synthetic Data, 169
Chapter 14: Backtest Statistics, 195
Chapter 15: Understanding Strategy Risk, 211
Chapter 16: Machine Learning Asset Allocation, 221
139
--- page 167 ---
--- page 168 ---

CHAPTER 10
Bet Sizing
10.1
MOTIVATION
There are fascinating parallels between strategy games and investing. Some of the
best portfolio managers I have worked with are excellent poker players, perhaps more
so than chess players. One reason is bet sizing, for which Texas Hold’em provides a
great analogue and training ground. Your ML algorithm can achieve high accuracy,
but if you do not size your bets properly, your investment strategy will inevitably
lose money. In this chapter we will review a few approaches to size bets from ML
predictions.
10.2
STRATEGY-INDEPENDENT BET SIZING APPROACHES
Consider two strategies on the same instrument. Let mi,t ∈[−1, 1] be the bet size of
strategy i at time t, where mi,t = −1 indicates a full short position and mi,t = 1 indicates a full long position. Suppose that one strategy produced a sequence of bet sizes
[m1,1, m1,2, m1,3] = [.5, 1, 0], as the market price followed a sequence [p1, p2, p3] =
[1, .5, 1.25], where pt is the price at time t. The other strategy produced a sequence
[m2,1, m2,2, m2,3] = [1, .5, 0], as it was forced to reduce its bet size once the market
moved against the initial full position. Both strategies produced forecasts that turned
out to be correct (the price increased by 25% between p1 and p3), however the first
strategy made money (0.5) while the second strategy lost money (−.125).
We would prefer to size positions in such way that we reserve some cash for the
possibility that the trading signal strengthens before it weakens. One option is to
compute the series ct = ct,l −ct,s, where ct,l is the number of concurrent long bets at
time t, and ct,s is the number of concurrent short bets at time t. This bet concurrency is
derived, for each side, similarly to how we computed label concurrency in Chapter 4
(recall the t1 object, with overlapping time spans). We fit a mixture of two Gaussians
141
--- page 169 ---

142
BET SIZING
on {ct}, applying a method like the one described in L´opez de Prado and Foreman
[2014]. Then, the bet size is derived as
mt =
⎧
⎪
⎨
⎪⎩
F[ct] −F[0]
1 −F[0]
if ct ≥0
F[ct] −F[0]
F[0]
if ct < 0
where F[x] is the CDF of the fitted mixture of two Gaussians for a value x. For example, we could size the bet as 0.9 when the probability of observing a signal of greater
value is only 0.1. The stronger the signal, the smaller the probability that the signal
becomes even stronger, hence the greater the bet size.
A second solution is to follow a budgeting approach. We compute the maximum
number (or some other quantile) of concurrent long bets, maxi{ci,l}, and the maximum number of concurrent short bets, maxi{ci,s}. Then we derive the bet size as
mt = ct,l
1
maxi{ci,l} −ct,s
1
maxi{ci,s}, where ct,l is the number of concurrent long bets at
time t, and ct,s is the number of concurrent short bets at time t. The goal is that the
maximum position is not reached before the last concurrent signal is triggered.
A third approach is to apply meta-labeling, as we explained in Chapter 3. We fit a
classifier, such as an SVC or RF, to determine the probability of misclassification, and
use that probability to derive the bet size. 1 This approach has a couple of advantages:
First, the ML algorithm that decides the bet sizes is independent of the primary model,
allowing for the incorporation of features predictive of false positives (see Chapter 3). Second, the predicted probability can be directly translated into bet size. Let us
see how.
10.3
BET SIZING FROM PREDICTED PROBABILITIES
Let us denote p [x] the probability that label x takes place. For two possible outcomes,
x ∈{−1, 1}, we would like to test the null hypothesis H0 : p [x = 1] = 1
2. We compute
the test statistic z =
p[x=1]−1
2
√
p[x=1](1−p[x=1]) =
2p[x=1]−1
2
√
p[x=1](1−p[x=1]) ∼Z, with z ∈(−∞, +∞)
and where Z represents the standard Normal distribution. We derive the bet size as
m = 2Z [z] −1, where m ∈[−1, 1] and Z [.] is the CDF of Z.
For more than two possible outcomes, we follow a one-versus-rest method. Let
X = {−1, … , 0, … , 1} be various labels associated with bet sizes, and x ∈X the predicted label. In other words, the label is identified by the bet size associated with it. For
each label i = 1, … , ‖X‖, we estimate a probability pi, with ∑‖X‖
i=1 pi = 1. We define
1 The references section lists a number of articles that explain how these probabilities are derived. Usually these probabilities incorporate information about the goodness of the fit, or confidence in the
prediction. See Wu et al. [2004], and visit http://scikit-learn.org/stable/modules/svm.html#scores-andprobabilities.
--- page 170 ---

BET SIZING FROM PREDICTED PROBABILITIES
143
FIGURE 10.1
Bet size from predicted probabilities̃
p = maxi{pi} as the probability of x, and we would like to test for H0 :̃ p =
1
‖X‖.2 We
compute the test statistic z =̃
p−1
‖X‖
√̃
p(1−̃p) ∼Z, with z ∈[0 , +∞). We derive the bet size
as m = x (2Z [z] −1)
⏟⏞⏞⏞⏟⏞⏞⏞⏟
∈[0,1]
, where m ∈[−1, 1] and Z [z] regulates the size for a prediction
x (where the side is implied by x).
Figure 10.1 plots the bet size as a function of test statistic. Snippet 10.1 implements
the translation from probabilities to bet size. It handles the possibility that the prediction comes from a meta-labeling estimator, as well from a standard labeling estimator.
In step #2, it also averages active bets, and discretizes the final value, which we will
explain in the following sections.
SNIPPET 10.1
FROM PROBABILITIES TO BET SIZE
def getSignal(events,stepSize,prob,pred,numClasses,numThreads,**kargs):
# get signals from predictions
if prob.shape[0]==0:return pd.Series()
#1) generate signals from multinomial classification (one-vs-rest, OvR)
signal0=(prob-1./numClasses)/(prob*(1.-prob))**.5 # t-value of OvR
signal0=pred*(2*norm.cdf(signal0)-1) # signal=side*size
2 Uncertainty is absolute when all outcomes are equally likely.
--- page 171 ---

144
BET SIZING
if 'side' in events:signal0*=events.loc[signal0.index,'side'] # meta-labeling
#2) compute average signal among those concurrently open
df0=signal0.to_frame('signal').join(events[['t1']],how='left')
df0=avgActiveSignals(df0,numThreads)
signal1=discreteSignal(signal0=df0,stepSize=stepSize)
return signal1
10.4
AVERAGING ACTIVE BETS
Every bet is associated with a holding period, spanning from the time it originated to
the time the first barrier is touched, t1 (see Chapter 3). One possible approach is to
override an old bet as a new bet arrives; however, that is likely to lead to excessive
turnover. A more sensible approach is to average all sizes across all bets still active at a
given point in time. Snippet 10.2 illustrates one possible implementation of this idea.
SNIPPET 10.2
BETS ARE AVERAGED AS LONG AS THEY ARE
STILL ACTIVE
def avgActiveSignals(signals,numThreads):
# compute the average signal among those active
#1) time points where signals change (either one starts or one ends)
tPnts=set(signals['t1'].dropna().values)
tPnts=tPnts.union(signals.index.values)
tPnts=list(tPnts);tPnts.sort()
out=mpPandasObj(mpAvgActiveSignals,('molecule',tPnts),numThreads,signals=signals)
return out
#———————————————————————————————————————
def mpAvgActiveSignals(signals,molecule):
’ ’ ’
At time loc, average signal among those still active.
Signal is active if:
a) issued before or at loc AND
b) loc before signal's endtime, or endtime is still unknown (NaT).
’ ’ ’
out=pd.Series()
for loc in molecule:
df0=(signals.index.values<=loc)&((loc<signals['t1'])|pd.isnull(signals['t1']))
act=signals[df0].index
if len(act)>0:out[loc]=signals.loc[act,'signal'].mean()
else:out[loc]=0 # no signals active at this time
return out
10.5
SIZE DISCRETIZATION
Averaging reduces some of the excess turnover, but still it is likely that small trades
will be triggered with every prediction. As this jitter would cause unnecessary
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
