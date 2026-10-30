# Advances in Financial Machine Learning.pdf — pages 134–153

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
--- page 135 ---

108
CROSS-VALIDATION IN FINANCE
FIGURE 7.3
Embargo of post-test train observations
SNIPPET 7.2
EMBARGO ON TRAINING OBSERVATIONS
def getEmbargoTimes(times,pctEmbargo):
# Get embargo time for each bar
step=int(times.shape[0]*pctEmbargo)
if step==0:
mbrg=pd.Series(times,index=times)
else:
mbrg=pd.Series(times[step:],index=times[:-step])
mbrg=mbrg.append(pd.Series(times[-1],index=times[-step:]))
return mbrg
#———————————————————————————————————————
testTimes=pd.Series(mbrg[dt1],index=[dt0]) # include embargo before purge
trainTimes=getTrainTimes(t1,testTimes)
testTimes=t1.loc[dt0:dt1].index
7.4.3
The Purged K-Fold Class
In the previous sections we have discussed how to produce training/testing splits
when labels overlap. That introduced the notion of purging and embargoing, in the
--- page 136 ---

BUGS IN SKLEARN’S CROSS-VALIDATION
109
particular context of model development. In general, we need to purge and embargo
overlapping training observations whenever we produce a train/test split, whether
it is for hyper-parameter fitting, backtesting, or performance evaluation. Snippet 7.3
extends scikit-learn’s KFold class to account for the possibility of leakages of testing
information into the training set.
SNIPPET 7.3
CROSS-VALIDATION CLASS WHEN OBSERVATIONS
OVERLAP
class PurgedKFold(_BaseKFold):
’’’
Extend KFold class to work with labels that span intervals
The train is purged of observations overlapping test-label intervals
Test set is assumed contiguous (shuffle=False), w/o training samples in between
’’’
def __init__(self,n_splits=3,t1=None,pctEmbargo=0.):
if not isinstance(t1,pd.Series):
raise ValueError('Label Through Dates must be a pd.Series')
super(PurgedKFold,self).__init__(n_splits,shufﬂe=False,random_state=None)
self.t1=t1
self.pctEmbargo=pctEmbargo
def split(self,X,y=None,groups=None):
if (X.index==self.t1.index).sum()!=len(self.t1):
raise ValueError('X and ThruDateValues must have the same index')
indices=np.arange(X.shape[0])
mbrg=int(X.shape[0]*self.pctEmbargo)
test_starts=[(i[0],i[-1]+1) for i in \
np.array_split(np.arange(X.shape[0]),self.n_splits)]
for i,j in test_starts:
t0=self.t1.index[i] # start of test set
test_indices=indices[i:j]
maxT1Idx=self.t1.index.searchsorted(self.t1[test_indices].max())
train_indices=self.t1.index.searchsorted(self.t1[self.t1<=t0].index)
if maxT1Idx<X.shape[0]: # right train (with embargo)
train_indices=np.concatenate((train_indices,indices[maxT1Idx+mbrg:]))
yield train_indices,test_indices
7.5
BUGS IN SKLEARN’S CROSS-VALIDATION
You would think that something as critical as cross-validation would be perfectly
implemented in one of the most popular ML libraries. Unfortunately that is not the
case, and this is one of the reasons you must always read all the code you run, and a
strong point in favor of open source. One of the many upsides of open-source code is
--- page 137 ---

110
CROSS-VALIDATION IN FINANCE
that you can verify everything and adjust it to your needs. Snippet 7.4 addresses two
known sklearn bugs:
1. Scoring functions do not know classes_, as a consequence of sklearn’s
reliance on numpy arrays rather than pandas series: https://github.com/scikitlearn/scikit-learn/issues/6231
2. cross_val_score will give different results because it passes weights to
the fit method, but not to the log_loss method: https://github.com/scikitlearn/scikit-learn/issues/9144
SNIPPET 7.4
USING THE PurgedKFold CLASS
def cvScore(clf,X,y,sample_weight,scoring='neg_log_loss',t1=None,cv=None,cvGen=None,
pctEmbargo=None):
if scoring not in ['neg_log_loss','accuracy']:
raise Exception('wrong scoring method.')
from sklearn.metrics import log_loss,accuracy_score
from clfSequential import PurgedKFold
if cvGen is None:
cvGen=PurgedKFold(n_splits=cv,t1=t1,pctEmbargo=pctEmbargo) # purged
score=[]
for train,test in cvGen.split(X=X):
ﬁt=clf.ﬁt(X=X.iloc[train,:],y=y.iloc[train],
sample_weight=sample_weight.iloc[train].values)
if scoring=='neg_log_loss':
prob=ﬁt.predict_proba(X.iloc[test,:])
score_=-log_loss(y.iloc[test],prob,
sample_weight=sample_weight.iloc[test].values,labels=clf.classes_)
else:
pred=ﬁt.predict(X.iloc[test,:])
score_=accuracy_score(y.iloc[test],pred,sample_weight= \
sample_weight.iloc[test].values)
score.append(score_)
return np.array(score)
Please understand that it may take a long time until a fix for these bugs is agreed
upon, implemented, tested, and released. Until then, you should use cvScore in Snippet 7.4, and avoid running the function cross_val_score.
EXERCISES
7.1 Why is shuffling a dataset before conducting k-fold CV generally a bad idea in
finance? What is the purpose of shuffling? Why does shuffling defeat the purpose
of k-fold CV in financial datasets?
7.2 Take a pair of matrices (X, y), representing observed features and labels. These
could be one of the datasets derived from the exercises in Chapter 3.
--- page 138 ---

BIBLIOGRAPHY
111
(a) Derive the performance from a 10-fold CV of an RF classifier on (X, y), without shuffling.
(b) Derive the performance from a 10-fold CV of an RF on (X, y), with shuffling.
(c) Why are both results so different?
(d) How does shuffling leak information?
7.3 Take the same pair of matrices (X, y) you used in exercise 2.
(a) Derive the performance from a 10-fold purged CV of an RF on (X, y), with
1% embargo.
(b) Why is the performance lower?
(c) Why is this result more realistic?
7.4 In this chapter we have focused on one reason why k-fold CV fails in financial
applications, namely the fact that some information from the testing set leaks into
the training set. Can you think of a second reason for CV’s failure?
7.5 Suppose you try one thousand configurations of the same investment strategy,
and perform a CV on each of them. Some results are guaranteed to look good,
just by sheer luck. If you only publish those positive results, and hide the rest,
your audience will not be able to deduce that these results are false positives, a
statistical fluke. This phenomenon is called “selection bias.”
(a) Can you imagine one procedure to prevent this?
(b) What if we split the dataset in three sets: training, validation, and testing?
The validation set is used to evaluate the trained parameters, and the testing
is run only on the one configuration chosen in the validation phase. In what
case does this procedure still fail?
(c) What is the key to avoiding selection bias?
BIBLIOGRAPHY
Bharat Rao, R., G. Fung, and R. Rosales (2008): “On the dangers of cross-validation: An experimental evaluation.” White paper, IKM CKS Siemens Medical Solutions USA. Available at
http://people.csail.mit.edu/romer/papers/CrossVal_SDM08.pdf.
Bishop, C. (1995): Neural Networks for Pattern Recognition, 1st ed. Oxford University Press.
Breiman, L. and P. Spector (1992): “Submodel selection and evaluation in regression: The X-random
case.” White paper, Department of Statistics, University of California, Berkeley. Available at
http://digitalassets.lib.berkeley.edu/sdtr/ucb/text/197.pdf.
Hastie, T., R. Tibshirani, and J. Friedman (2009): The Elements of Statistical Learning, 1st ed.
Springer.
James, G., D. Witten, T. Hastie and R. Tibshirani (2013): An Introduction to Statistical Learning,
1st ed. Springer.
Kohavi, R. (1995): “A study of cross-validation and bootstrap for accuracy estimation and
model selection.” International Joint Conference on Artificial Intelligence. Available at
http://web.cs.iastate.edu/~jtian/cs573/Papers/Kohavi-IJCAI-95.pdf.
Ripley, B. (1996): Pattern Recognition and Neural Networks, 1st ed. Cambridge University Press.
--- page 139 ---
--- page 140 ---

CHAPTER 8
Feature Importance
8.1
MOTIVATION
One of the most pervasive mistakes in financial research is to take some data, run
it through an ML algorithm, backtest the predictions, and repeat the sequence until
a nice-looking backtest shows up. Academic journals are filled with such pseudodiscoveries, and even large hedge funds constantly fall into this trap. It does not matter
if the backtest is a walk-forward out-of-sample. The fact that we are repeating a test
over and over on the same data will likely lead to a false discovery. This methodological error is so notorious among statisticians that they consider it scientific fraud, and
the American Statistical Association warns against it in its ethical guidelines (American Statistical Association [2016], Discussion #4). It typically takes about 20 such
iterations to discover a (false) investment strategy subject to the standard significance
level (false positive rate) of 5%. In this chapter we will explore why such an approach
is a waste of time and money, and how feature importance offers an alternative.
8.2
THE IMPORTANCE OF FEATURE IMPORTANCE
A striking facet of the financial industry is that so many very seasoned portfolio
managers (including many with a quantitative background) do not realize how easy
it is to overfit a backtest. How to backtest properly is not the subject of this chapter;
we will address that extremely important topic in Chapters 11–15. The goal of this
chapter is to explain one of the analyses that must be performed before any backtest
is carried out.
Suppose that you are given a pair of matrices (X, y), that respectively contain
features and labels for a particular financial instrument. We can fit a classifier on
(X, y) and evaluate the generalization error through a purged k-fold cross-validation
(CV), as we saw in Chapter 7. Suppose that we achieve good performance. The next
113
--- page 141 ---

114
FEATURE IMPORTANCE
natural question is to try to understand what features contributed to that performance.
Maybe we could add some features that strengthen the signal responsible for the classifier’s predictive power. Maybe we could eliminate some of the features that are only
adding noise to the system. Notably, understanding feature importance opens up the
proverbial black box. We can gain insight into the patterns identified by the classifier
if we understand what source of information is indispensable to it. This is one of the
reasons why the black box mantra is somewhat overplayed by the ML skeptics. Yes,
the algorithm has learned without us directing the process (that is the whole point
of ML!) in a black box, but that does not mean that we cannot (or should not) take
a look at what the algorithm has found. Hunters do not blindly eat everything their
smart dogs retrieve for them, do they?
Once we have found what features are important, we can learn more by conducting
a number of experiments. Are these features important all the time, or only in some
specific environments? What triggers a change in importance over time? Can those
regime switches be predicted? Are those important features also relevant to other
related financial instruments? Are they relevant to other asset classes? What are the
most relevant features across all financial instruments? What is the subset of features
with the highest rank correlation across the entire investment universe? This is a much
better way of researching strategies than the foolish backtest cycle. Let me state this
maxim as one of the most critical lessons I hope you learn from this book:
SNIPPET 8.1
MARCOS’ FIRST LAW OF
BACKTESTING—IGNORE AT YOUR OWN PERIL
“Backtesting is not a research tool. Feature importance is.”
—Marcos L´opez de Prado
Advances in Financial Machine Learning (2018)
8.3
FEATURE IMPORTANCE WITH SUBSTITUTION EFFECTS
I find it useful to distinguish between feature importance methods based on whether
they are impacted by substitution effects. In this context, a substitution effect takes
place when the estimated importance of one feature is reduced by the presence of
other related features. Substitution effects are the ML analogue of what the statistics
and econometrics literature calls “multi-collinearity.” One way to address linear substitution effects is to apply PCA on the raw features, and then perform the feature
importance analysis on the orthogonal features. See Belsley et al. [1980], Goldberger
[1991, pp. 245–253], and Hill et al. [2001] for further details.
8.3.1
Mean Decrease Impurity
Mean decrease impurity (MDI) is a fast, explanatory-importance (in-sample, IS)
method specific to tree-based classifiers, like RF. At each node of each decision
tree, the selected feature splits the subset it received in such a way that impurity is
--- page 142 ---

FEATURE IMPORTANCE WITH SUBSTITUTION EFFECTS
115
decreased. Therefore, we can derive for each decision tree how much of the overall
impurity decrease can be assigned to each feature. And given that we have a forest of
trees, we can average those values across all estimators and rank the features accordingly. See Louppe et al. [2013] for a detailed description. There are some important
considerations you must keep in mind when working with MDI:
1. Masking effects take place when some features are systematically ignored
by tree-based classifiers in favor of others. In order to avoid them, set
max_features=int(1)when using sklearn’s RF class. In this way, only one
random feature is considered per level.
(a) Every feature is given a chance (at some random levels of some random
trees) to reduce impurity.
(b) Make sure that features with zero importance are not averaged, since the
only reason for a 0 is that the feature was not randomly chosen. Replace
those values with np.nan.
2. The procedure is obviously IS. Every feature will have some importance, even
if they have no predictive power whatsoever.
3. MDI cannot be generalized to other non-tree based classifiers.
4. By construction, MDI has the nice property that feature importances add up to
1, and every feature importance is bounded between 0 and 1.
5. The method does not address substitution effects in the presence of correlated
features. MDI dilutes the importance of substitute features, because of their
interchangeability: The importance of two identical features will be halved, as
they are randomly chosen with equal probability.
6. Strobl et al. [2007] show experimentally that MDI is biased towards some predictor variables. White and Liu [1994] argue that, in case of single decision
trees, this bias is due to an unfair advantage given by popular impurity functions toward predictors with a large number of categories.
Sklearn’s RandomForest class implements MDI as the default feature importance score. This choice is likely motivated by the ability to compute MDI on the
fly, with minimum computational cost.1 Snippet 8.2 illustrates an implementation of
MDI, incorporating the considerations listed earlier.
SNIPPET 8.2
MDI FEATURE IMPORTANCE
def featImpMDI(ﬁt,featNames):
# feat importance based on IS mean impurity reduction
df0={i:tree.feature_importances_ for i,tree in enumerate(ﬁt.estimators_)}
df0=pd.DataFrame.from_dict(df0,orient='index')
df0.columns=featNames
df0=df0.replace(0,np.nan) # because max_features=1
1 http://blog.datadive.net/selecting-good-features-part-iii-random-forests/.
--- page 143 ---

116
FEATURE IMPORTANCE
imp=pd.concat({'mean':df0.mean(),'std':df0.std()*df0.shape[0]**-.5},axis=1)
imp/=imp['mean'].sum()
return imp
8.3.2
Mean Decrease Accuracy
Mean decrease accuracy (MDA) is a slow, predictive-importance (out-of-sample,
OOS) method. First, it fits a classifier; second, it derives its performance OOS according to some performance score (accuracy, negative log-loss, etc.); third, it permutates
each column of the features matrix (X), one column at a time, deriving the performance OOS after each column’s permutation. The importance of a feature is a function of the loss in performance caused by its column’s permutation. Some relevant
considerations include:
1. This method can be applied to any classifier, not only tree-based classifiers.
2. MDA is not limited to accuracy as the sole performance score. For example,
in the context of meta-labeling applications, we may prefer to score a classifier
with F1 rather than accuracy (see Chapter 14, Section 14.8 for an explanation).
That is one reason a better descriptive name would have been “permutation
importance.” When the scoring function does not correspond to a metric space,
MDA results should be used as a ranking.
3. Like MDI, the procedure is also susceptible to substitution effects in the presence of correlated features. Given two identical features, MDA always considers one to be redundant to the other. Unfortunately, MDA will make both
features appear to be outright irrelevant, even if they are critical.
4. Unlike MDI, it is possible that MDA concludes that all features are unimportant. That is because MDA is based on OOS performance.
5. The CV must be purged and embargoed, for the reasons explained in Chapter 7.
Snippet 8.3 implements MDA feature importance with sample weights, with
purged k-fold CV, and with scoring by negative log-loss or accuracy. It measures
MDA importance as a function of the improvement (from permutating to not permutating the feature), relative to the maximum possible score (negative log-loss of 0, or
accuracy of 1). Note that, in some cases, the improvement may be negative, meaning
that the feature is actually detrimental to the forecasting power of the ML algorithm.
SNIPPET 8.3
MDA FEATURE IMPORTANCE
def featImpMDA(clf,X,y,cv,sample_weight,t1,pctEmbargo,scoring='neg_log_loss'):
# feat importance based on OOS score reduction
if scoring not in ['neg_log_loss','accuracy']:
raise Exception('wrong scoring method.')
from sklearn.metrics import log_loss,accuracy_score
cvGen=PurgedKFold(n_splits=cv,t1=t1,pctEmbargo=pctEmbargo) # purged cv
scr0,scr1=pd.Series(),pd.DataFrame(columns=X.columns)
--- page 144 ---

FEATURE IMPORTANCE WITHOUT SUBSTITUTION EFFECTS
117
for i,(train,test) in enumerate(cvGen.split(X=X)):
X0,y0,w0=X.iloc[train,:],y.iloc[train],sample_weight.iloc[train]
X1,y1,w1=X.iloc[test,:],y.iloc[test],sample_weight.iloc[test]
ﬁt=clf.ﬁt(X=X0,y=y0,sample_weight=w0.values)
if scoring=='neg_log_loss':
prob=ﬁt.predict_proba(X1)
scr0.loc[i]=-log_loss(y1,prob,sample_weight=w1.values,
labels=clf.classes_)
else:
pred=ﬁt.predict(X1)
scr0.loc[i]=accuracy_score(y1,pred,sample_weight=w1.values)
for j in X.columns:
X1_=X1.copy(deep=True)
np.random.shufﬂe(X1_[j].values) # permutation of a single column
if scoring=='neg_log_loss':
prob=ﬁt.predict_proba(X1_)
scr1.loc[i,j]=-log_loss(y1,prob,sample_weight=w1.values,
labels=clf.classes_)
else:
pred=ﬁt.predict(X1_)
scr1.loc[i,j]=accuracy_score(y1,pred,sample_weight=w1.values)
imp=(-scr1).add(scr0,axis=0)
if scoring=='neg_log_loss':imp=imp/-scr1
else:imp=imp/(1.-scr1)
imp=pd.concat({'mean':imp.mean(),'std':imp.std()*imp.shape[0]**-.5},axis=1)
return imp,scr0.mean()
8.4
FEATURE IMPORTANCE WITHOUT SUBSTITUTION EFFECTS
Substitution effects can lead us to discard important features that happen to be redundant. This is not generally a problem in the context of prediction, but it could lead
us to wrong conclusions when we are trying to understand, improve, or simplify a
model. For this reason, the following single feature importance method can be a good
complement to MDI and MDA.
8.4.1
Single Feature Importance
Single feature importance (SFI) is a cross-section predictive-importance (out-ofsample) method. It computes the OOS performance score of each feature in isolation.
A few considerations:
1. This method can be applied to any classifier, not only tree-based classifiers.
2. SFI is not limited to accuracy as the sole performance score.
3. Unlike MDI and MDA, no substitution effects take place, since only one feature
is taken into consideration at a time.
4. Like MDA, it can conclude that all features are unimportant, because performance is evaluated via OOS CV.
--- page 145 ---

118
FEATURE IMPORTANCE
The main limitation of SFI is that a classifier with two features can perform better
than the bagging of two single-feature classifiers. For example, (1) feature B may be
useful only in combination with feature A; or (2) feature B may be useful in explaining the splits from feature A, even if feature B alone is inaccurate. In other words,
joint effects and hierarchical importance are lost in SFI. One alternative would be
to compute the OOS performance score from subsets of features, but that calculation will become intractable as more features are considered. Snippet 8.4 demonstrates one possible implementation of the SFI method. A discussion of the function
cvScore can be found in Chapter 7.
SNIPPET 8.4
IMPLEMENTATION OF SFI
def auxFeatImpSFI(featNames,clf,trnsX,cont,scoring,cvGen):
imp=pd.DataFrame(columns=['mean','std'])
for featName in featNames:
df0=cvScore(clf,X=trnsX[[featName]],y=cont['bin'],sample_weight=cont['w'],
scoring=scoring,cvGen=cvGen)
imp.loc[featName,'mean']=df0.mean()
imp.loc[featName,'std']=df0.std()*df0.shape[0]**-.5
return imp
8.4.2
Orthogonal Features
As argued in Section 8.3, substitution effects dilute the importance of features measured by MDI, and significantly underestimate the importance of features measured
by MDA. A partial solution is to orthogonalize the features before applying MDI and
MDA. An orthogonalization procedure such as principal components analysis (PCA)
does not prevent all substitution effects, but at least it should alleviate the impact of
linear substitution effects.
Consider a matrix {Xt,n} of stationary features, with observations t = 1, … , T and
variables n = 1, … , N. First, we compute the standardized features matrix Z, such
that Zt,n = 𝜎−1
n (Xt,n −𝜇n), where 𝜇n is the mean of {Xt,n}t=1,…,T and 𝜎n is the standard
deviation of {Xt,n}t=1,…,T. Second, we compute the eigenvalues Λ and eigenvectors
W such that Z′ZW = WΛ, where Λ is an NxN diagonal matrix with main entries
sorted in descending order, and W is an NxN orthonormal matrix. Third, we derive
the orthogonal features as P = ZW. We can verify the orthogonality of the features
by noting that P′P = W′Z′ZW = W′WΛW′W = Λ.
The diagonalization is done on Z rather than X, for two reasons: (1) centering the
data ensures that the first principal component is correctly oriented in the main direction of the observations. It is equivalent to adding an intercept in a linear regression;
(2) re-scaling the data makes PCA focus on explaining correlations rather than variances. Without re-scaling, the first principal components would be dominated by the
--- page 146 ---

FEATURE IMPORTANCE WITHOUT SUBSTITUTION EFFECTS
119
columns of X with highest variance, and we would not learn much about the structure
or relationship between the variables.
Snippet 8.5 computes the smallest number of orthogonal features that explain at
least 95% of the variance of Z.
SNIPPET 8.5
COMPUTATION OF ORTHOGONAL FEATURES
def get_eVec(dot,varThres):
# compute eVec from dot prod matrix, reduce dimension
eVal,eVec=np.linalg.eigh(dot)
idx=eVal.argsort()[::-1] # arguments for sorting eVal desc
eVal,eVec=eVal[idx],eVec[:,idx]
#2) only positive eVals
eVal=pd.Series(eVal,index=['PC_'+str(i+1) for i in range(eVal.shape[0])])
eVec=pd.DataFrame(eVec,index=dot.index,columns=eVal.index)
eVec=eVec.loc[:,eVal.index]
#3) reduce dimension, form PCs
cumVar=eVal.cumsum()/eVal.sum()
dim=cumVar.values.searchsorted(varThres)
eVal,eVec=eVal.iloc[:dim+1],eVec.iloc[:,:dim+1]
return eVal,eVec
#-----------------------------------------------------------------
def orthoFeats(dfX,varThres=.95):
# Given a dataframe dfX of features, compute orthofeatures dfP
dfZ=dfX.sub(dfX.mean(),axis=1).div(dfX.std(),axis=1) # standardize
dot=pd.DataFrame(np.dot(dfZ.T,dfZ),index=dfX.columns,columns=dfX.columns)
eVal,eVec=get_eVec(dot,varThres)
dfP=np.dot(dfZ,eVec)
return dfP
Besides addressing substitution effects, working with orthogonal features provides
two additional benefits: (1) orthogonalization can also be used to reduce the dimensionality of the features matrix X, by dropping features associated with small eigenvalues. This usually speeds up the convergence of ML algorithms; (2) the analysis is
conducted on features designed to explain the structure of the data.
Let me stress this latter point. An ubiquitous concern throughout the book is the
risk of overfitting. ML algorithms will always find a pattern, even if that pattern is
a statistical fluke. You should always be skeptical about the purportedly important
features identified by any method, including MDI, MDA, and SFI. Now, suppose
that you derive orthogonal features using PCA. Your PCA analysis has determined
that some features are more “principal” than others, without any knowledge of the
labels (unsupervised learning). That is, PCA has ranked features without any possible
overfitting in a classification sense. When your MDI, MDA, or SFI analysis selects
as most important (using label information) the same features that PCA chose as
--- page 147 ---

120
FEATURE IMPORTANCE
FIGURE 8.1
Scatter plot of eigenvalues (x-axis) and MDI levels (y-axis) in log-log scale
principal (ignoring label information), this constitutes confirmatory evidence that the
pattern identified by the ML algorithm is not entirely overfit. If the features were
entirely random, the PCA ranking would have no correspondance with the feature
importance ranking. Figure 8.1 displays the scatter plot of eigenvalues associated with
an eigenvector (x-axis) paired with MDI of the feature associated with an engenvector
(y-axis). The Pearson correlation is 0.8491 (p-value below 1E-150), evidencing that
PCA identified informative features and ranked them correctly without overfitting.
I find it useful to compute the weighted Kendall’s tau between the feature importances and their associated eigenvalues (or equivalently, their inverse PCA rank). The
closer this value is to 1, the stronger is the consistency between PCA ranking and feature importance ranking. One argument for preferring a weighted Kendall’s tau over
the standard Kendall is that we want to prioritize rank concordance among the most
importance features. We do not care so much about rank concordance among irrelevant (likely noisy) features. The hyperbolic-weighted Kendall’s tau for the sample in
Figure 8.1 is 0.8206.
Snippet 8.6 shows how to compute this correlation using Scipy. In this example, sorting the features in descending importance gives us a PCA rank sequence
very close to an ascending list. Because the weightedtau function gives higher
weight to higher values, we compute the correlation on the inverse PCA ranking,
pcRank**-1. The resulting weighted Kendall’s tau is relatively high, at 0.8133.
--- page 148 ---

PARALLELIZED VS. STACKED FEATURE IMPORTANCE
121
SNIPPET 8.6
COMPUTATION OF WEIGHTED KENDALL’S TAU
BETWEEN FEATURE IMPORTANCE AND INVERSE PCA RANKING
>>> import numpy as np
>>> from scipy.stats import weightedtau
>>> featImp=np.array([.55,.33,.07,.05]) # feature importance
>>> pcRank=np.array([1,2,4,3]) # PCA rank
>>> weightedtau(featImp,pcRank**-1.)[0]
8.5
PARALLELIZED VS. STACKED FEATURE IMPORTANCE
There are at least two research approaches to feature importance. First, for each security i in an investment universe i = 1, … , I, we form a dataset (Xi, yi), and derive the
feature importance in parallel. For example, let us denote 𝜆i,j,k the importance of
feature j on instrument i according to criterion k. Then we can aggregate all results
across the entire universe to derive a combined Λj,k importance of feature j according to criterion k. Features that are important across a wide variety of instruments are
more likely to be associated with an underlying phenomenon, particularly when these
feature importances exhibit high rank correlation across the criteria. It may be worth
studying in-depth the theoretical mechanism that makes these features predictive. The
main advantage of this approach is that it is computationally fast, as it can be parallelized. A disadvantage is that, due to substitution effects, important features may
swap their ranks across instruments, increasing the variance of the estimated 𝜆i,j,k.
This disadvantage becomes relatively minor if we average 𝜆i,j,k across instruments
for a sufficiently large investment universe.
A second alternative is what I call “features stacking.” It consists in stacking all
datasets {(̃Xi, yi)}i=1,…,I into a single combined dataset (X, y), wherẽ Xi is a transformed instance of Xi (e.g., standardized on a rolling trailing window). The purpose
of this transformation is to ensure some distributional homogeneity,̃ Xi ∼X. Under
this approach, the classifier must learn what features are more important across all
instruments simultaneously, as if the entire investment universe were in fact a single
instrument. Features stacking presents some advantages: (1) The classifier will be fit
on a much larger dataset than the one used with the parallelized (first) approach; (2)
the importance is derived directly, and no weighting scheme is required for combining
the results; (3) conclusions are more general and less biased by outliers or overfitting;
and (4) because importance scores are not averaged across instruments, substitution
effects do not cause the dampening of those scores.
I usually prefer features stacking, not only for features importance but whenever a
classifier can be fit on a set of instruments, including for the purpose of model prediction. That reduces the likelihood of overfitting an estimator to a particular instrument
or small dataset. The main disadvantage of stacking is that it may consume a lot of
--- page 149 ---

122
FEATURE IMPORTANCE
memory and resources, however that is where a sound knowledge of HPC techniques
will come in handy (Chapters 20–22).
8.6
EXPERIMENTS WITH SYNTHETIC DATA
In this section, we are going to test how these feature importance methods respond
to synthetic data. We are going to generate a dataset (X, y) composed on three kinds
of features:
1. Informative: These are features that are used to determine the label.
2. Redundant: These are random linear combinations of the informative features.
They will cause substitution effects.
3. Noise: These are features that have no bearing on determining the observation’s
label.
Snippet 8.7 shows how we can generate a synthetic dataset of 40 features
where 10 are informative, 10 are redundant, and 20 are noise, on 10,000 observations. For details on how sklearn generates synthetic datasets, visit: http://scikitlearn.org/stable/modules/generated/sklearn.datasets.make_classification.html.
SNIPPET 8.7
CREATING A SYNTHETIC DATASET
def getTestData(n_features=40,n_informative=10,n_redundant=10,n_samples=10000):
# generate a random dataset for a classification problem
from sklearn.datasets import make_classiﬁcation
trnsX,cont=make_classiﬁcation(n_samples=n_samples,n_features=n_features,
n_informative=n_informative,n_redundant=n_redundant,random_state=0,
shufﬂe=False)
df0=pd.DatetimeIndex(periods=n_samples,freq=pd.tseries.offsets.BDay(),
end=pd.datetime.today())
trnsX,cont=pd.DataFrame(trnsX,index=df0),
pd.Series(cont,index=df0).to_frame('bin')
df0=['I_'+str(i) for i in xrange(n_informative)]+
['R_'+str(i) for i in xrange(n_redundant)]
df0+=['N_'+str(i) for i in xrange(n_features-len(df0))]
trnsX.columns=df0
cont['w']=1./cont.shape[0]
cont['t1']=pd.Series(cont.index,index=cont.index)
return trnsX,cont
Given that we know for certain what feature belongs to each class, we can evaluate
whether these three feature importance methods perform as designed. Now we need
--- page 150 ---

EXPERIMENTS WITH SYNTHETIC DATA
123
a function that can carry out each analysis on the same dataset. Snippet 8.8 accomplishes that, using bagged decision trees as default classifier (Chapter 6).
SNIPPET 8.8
CALLING FEATURE IMPORTANCE FOR
ANY METHOD
def featImportance(trnsX,cont,n_estimators=1000,cv=10,max_samples=1.,numThreads=24,
pctEmbargo=0,scoring='accuracy',method='SFI',minWLeaf=0.,**kargs):
# feature importance from a random forest
from sklearn.tree import DecisionTreeClassiﬁer
from sklearn.ensemble import BaggingClassiﬁer
from mpEngine import mpPandasObj
n_jobs=(-1 if numThreads>1 else 1) # run 1 thread with ht_helper in dirac1
#1) prepare classifier,cv. max_features=1, to prevent masking
clf=DecisionTreeClassiﬁer(criterion='entropy',max_features=1,
class_weight='balanced',min_weight_fraction_leaf=minWLeaf)
clf=BaggingClassiﬁer(base_estimator=clf,n_estimators=n_estimators,
max_features=1.,max_samples=max_samples,oob_score=True,n_jobs=n_jobs)
ﬁt=clf.ﬁt(X=trnsX,y=cont['bin'],sample_weight=cont['w'].values)
oob=ﬁt.oob_score_
if method=='MDI':
imp=featImpMDI(ﬁt,featNames=trnsX.columns)
oos=cvScore(clf,X=trnsX,y=cont['bin'],cv=cv,sample_weight=cont['w'],
t1=cont['t1'],pctEmbargo=pctEmbargo,scoring=scoring).mean()
elif method=='MDA':
imp,oos=featImpMDA(clf,X=trnsX,y=cont['bin'],cv=cv,sample_weight=cont['w'],
t1=cont['t1'],pctEmbargo=pctEmbargo,scoring=scoring)
elif method=='SFI':
cvGen=PurgedKFold(n_splits=cv,t1=cont['t1'],pctEmbargo=pctEmbargo)
oos=cvScore(clf,X=trnsX,y=cont['bin'],sample_weight=cont['w'],scoring=scoring,
cvGen=cvGen).mean()
clf.n_jobs=1 # paralellize auxFeatImpSFI rather than clf
imp=mpPandasObj(auxFeatImpSFI,('featNames',trnsX.columns),numThreads,
clf=clf,trnsX=trnsX,cont=cont,scoring=scoring,cvGen=cvGen)
return imp,oob,oos
Finally, we need a main function to call all components, from data generation to
feature importance analysis to collection and processing of output. These tasks are
performed by Snippet 8.9.
SNIPPET 8.9
CALLING ALL COMPONENTS
def testFunc(n_features=40,n_informative=10,n_redundant=10,n_estimators=1000,
n_samples=10000,cv=10):
# test the performance of the feat importance functions on artificial data
# Nr noise features = n_features—n_informative—n_redundant
trnsX,cont=getTestData(n_features,n_informative,n_redundant,n_samples)
--- page 151 ---

124
FEATURE IMPORTANCE
dict0={'minWLeaf':[0.],'scoring':['accuracy'],'method':['MDI','MDA','SFI'],
'max_samples':[1.]}
jobs,out=(dict(izip(dict0,i)) for i in product(*dict0.values())),[]
kargs={'pathOut':'./testFunc/','n_estimators':n_estimators,
'tag':'testFunc','cv':cv}
for job in jobs:
job['simNum']=job['method']+'_'+job['scoring']+'_'+'%.2f'%job['minWLeaf']+ \
'_'+str(job['max_samples'])
print job['simNum']
kargs.update(job)
imp,oob,oos=featImportance(trnsX=trnsX,cont=cont,**kargs)
plotFeatImportance(imp=imp,oob=oob,oos=oos,**kargs)
df0=imp[['mean']]/imp['mean'].abs().sum()
df0['type']=[i[0] for i in df0.index]
df0=df0.groupby('type')['mean'].sum().to_dict()
df0.update({'oob':oob,'oos':oos});df0.update(job)
out.append(df0)
out=pd.DataFrame(out).sort_values(['method','scoring','minWLeaf','max_samples'])
out=out['method','scoring','minWLeaf','max_samples','I','R','N','oob','oos']
out.to_csv(kargs['pathOut']+'stats.csv')
return
For the aesthetically inclined, Snippet 8.10 provides a nice layout for plotting feature importances.
SNIPPET 8.10
FEATURE IMPORTANCE PLOTTING FUNCTION
def plotFeatImportance(pathOut,imp,oob,oos,method,tag=0,simNum=0,**kargs):
# plot mean imp bars with std
mpl.ﬁgure(ﬁgsize=(10,imp.shape[0]/5.))
imp=imp.sort_values('mean',ascending=True)
ax=imp['mean'].plot(kind='barh',color='b',alpha=.25,xerr=imp['std'],
error_kw={'ecolor':'r'})
if method=='MDI':
mpl.xlim([0,imp.sum(axis=1).max()])
mpl.axvline(1./imp.shape[0],linewidth=1,color='r',linestyle='dotted')
ax.get_yaxis().set_visible(False)
for i,j in zip(ax.patches,imp.index):ax.text(i.get_width()/2,
i.get_y()+i.get_height()/2,j,ha='center',va='center',
color='black')
mpl.title('tag='+tag+' | simNum='+str(simNum)+' | oob='+str(round(oob,4))+
' | oos='+str(round(oos,4)))
mpl.saveﬁg(pathOut+'featImportance_'+str(simNum)+'.png',dpi=100)
mpl.clf();mpl.close()
return
--- page 152 ---

EXPERIMENTS WITH SYNTHETIC DATA
125
FIGURE 8.2
MDI feature importance computed on a synthetic dataset
Figure 8.2 shows results for MDI. For each feature, the horizontal bar indicates
the mean MDI value across all the decision trees, and the horizontal line is the standard deviation of that mean. Since MDI importances add up to 1, if all features were
equally important, each importance would have a value of 1/40. The vertical dotted
line marks that 1/40 threshold, separating features whose importance exceeds what
would be expected from undistinguishable features. As you can see, MDI does a very
good job in terms of placing all informative and redundant features above the red dotted line, with the exception of R_5, which did not make the cut by a small margin.
Substitution effects cause some informative or redundant features to rank better than
others, which was expected.
Figure 8.3 shows that MDA also did a good job. Results are consistent with those
from MDI’s in the sense that all the informed and redundant features rank better than
the noise feature, with the exception of R_6, likely due to a substitution effect. One not
so positive aspect of MDA is that the standard deviation of the means are somewhat
higher, although that could be addressed by increasing the number of partitions in
the purged k-fold CV, from, say, 10 to 100 (at the cost of 10 × the computation time
without parallelization).
Figure 8.4 shows that SFI also does a decent job; however, a few important features rank worse than noise (I_6, I_2, I_9, I_1, I_3, R_5), likely due to joint effects.
--- page 153 ---

FIGURE 8.3
MDA feature importance computed on a synthetic dataset
FIGURE 8.4
SFI feature importance computed on a synthetic dataset
