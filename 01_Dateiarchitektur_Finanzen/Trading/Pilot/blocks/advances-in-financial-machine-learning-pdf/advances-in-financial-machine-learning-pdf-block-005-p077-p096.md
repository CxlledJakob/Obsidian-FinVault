# Advances in Financial Machine Learning.pdf — pages 77–96

--- page 77 ---

50
LABELING
#2) create out object
out=pd.DataFrame(index=events_.index)
out['ret']=px.loc[events_['t1'].values].values/px.loc[events_.index]-1
out['bin']=np.sign(out['ret'])
return out
3.6
META-LABELING
Suppose that you have a model for setting the side of the bet (long or short). You just
need to learn the size of that bet, which includes the possibility of no bet at all (zero
size). This is a situation that practitioners face regularly. We often know whether we
want to buy or sell a product, and the only remaining question is how much money
we should risk in such a bet. We do not want the ML algorithm to learn the side, just
to tell us what is the appropriate size. At this point, it probably does not surprise you
to hear that no book or paper has so far discussed this common problem. Thankfully,
that misery ends here. I call this problem meta-labeling because we want to build a
secondary ML model that learns how to use a primary exogenous model.
Rather than writing an entirely new getEvents function, we will make some
adjustments to the previous code, in order to handle meta-labeling. First, we accept a
new side optional argument (with default None), which contains the side of our bets
as decided by the primary model. When side is not None, the function understands
that meta-labeling is in play. Second, because now we know the side, we can effectively discriminate between profit taking and stop loss. The horizontal barriers do not
need to be symmetric, as in Section 3.5. Argument ptSl is a list of two non-negative
float values, where ptSl[0] is the factor that multiplies trgt to set the width of
the upper barrier, and ptSl[1] is the factor that multiplies trgt to set the width
of the lower barrier. When either is 0, the respective barrier is disabled. Snippet 3.6
implements these enhancements.
SNIPPET 3.6
EXPANDING getEvents TO INCORPORATE
META-LABELING
def getEvents(close,tEvents,ptSl,trgt,minRet,numThreads,t1=False,side=None):
#1) get target
trgt=trgt.loc[tEvents]
trgt=trgt[trgt>minRet] # minRet
#2) get t1 (max holding period)
if t1 is False:t1=pd.Series(pd.NaT,index=tEvents)
#3) form events object, apply stop loss on t1
if side is None:side_,ptSl_=pd.Series(1.,index=trgt.index),[ptSl[0],ptSl[0]]
else:side_,ptSl_=side.loc[trgt.index],ptSl[:2]
events=pd.concat({'t1':t1,'trgt':trgt,'side':side_}, \
axis=1).dropna(subset=['trgt'])
df0=mpPandasObj(func=applyPtSlOnT1,pdObj=('molecule',events.index), \
numThreads=numThreads,close=inst['Close'],events=events,ptSl=ptSl_)
--- page 78 ---

HOW TO USE META-LABELING
51
events['t1']=df0.dropna(how='all').min(axis=1) # pd.min ignores nan
if side is None:events=events.drop('side',axis=1)
return events
Likewise, we need to expand the getBins function, so that it handles metalabeling. Snippet 3.7 implements the necessary changes.
SNIPPET 3.7
EXPANDING getBins TO INCORPORATE
META-LABELING
def getBins(events,close):
’’’
Compute event's outcome (including side information, if provided).
events is a DataFrame where:
—events.index is event's starttime
—events[’t1’] is event's endtime
—events[’trgt’] is event's target
—events[’side’] (optional) implies the algo's position side
Case 1: (’side’ not in events): bin in (-1,1) <—label by price action
Case 2: (’side’ in events): bin in (0,1) <—label by pnl (meta-labeling)
’’’
#1) prices aligned with events
events_=events.dropna(subset=['t1'])
px=events_.index.union(events_['t1'].values).drop_duplicates()
px=close.reindex(px,method='bﬁll')
#2) create out object
out=pd.DataFrame(index=events_.index)
out['ret']=px.loc[events_['t1'].values].values/px.loc[events_.index]-1
if 'side' in events_:out['ret']*=events_['side'] # meta-labeling
out['bin']=np.sign(out['ret'])
if 'side' in events_:out.loc[out['ret']<=0,'bin']=0 # meta-labeling
return out
Now the possible values for labels in out['bin'] are {0,1}, as opposed to
the previous feasible values {−1,0,1}. The ML algorithm will be trained to decide
whether to take the bet or pass, a purely binary prediction. When the predicted label
is 1, we can use the probability of this secondary prediction to derive the size of the
bet, where the side (sign) of the position has been set by the primary model.
3.7
HOW TO USE META-LABELING
Binary classification problems present a trade-off between type-I errors (false positives) and type-II errors (false negatives). In general, increasing the true positive rate
of a binary classifier will tend to increase its false positive rate. The receiver operating
--- page 79 ---

52
LABELING
FIGURE 3.2
A visualization of the “confusion matrix”
characteristic (ROC) curve of a binary classifier measures the cost of increasing the
true positive rate, in terms of accepting higher false positive rates.
Figure 3.2 illustrates the so-called “confusion matrix.” On a set of observations,
there are items that exhibit a condition (positives, left rectangle), and items that do not
exhibit a condition (negative, right rectangle). A binary classifier predicts that some
items exhibit the condition (ellipse), where the TP area contains the true positives
and the TN area contains the true negatives. This leads to two kinds of errors: false
positives (FP) and false negatives (FN). “Precision” is the ratio between the TP area
and the area in the ellipse. “Recall” is the ratio between the TP area and the area
in the left rectangle. This notion of recall (aka true positive rate) is in the context
of classification problems, the analogous to “power” in the context of hypothesis
testing. “Accuracy” is the sum of the TP and TN areas divided by the overall set of
items (square). In general, decreasing the FP area comes at a cost of increasing the
FN area, because higher precision typically means fewer calls, hence lower recall.
Still, there is some combination of precision and recall that maximizes the overall
efficiency of the classifier. The F1-score measures the efficiency of a classifier as the
harmonic average between precision and recall (more on this in Chapter 14).
Meta-labeling is particularly helpful when you want to achieve higher F1-scores.
First, we build a model that achieves high recall, even if the precision is not
particularly high. Second, we correct for the low precision by applying meta-labeling
to the positives predicted by the primary model.
--- page 80 ---

THE QUANTAMENTAL WAY
53
Meta-labeling will increase your F1-score by filtering out the false positives, where
the majority of positives have already been identified by the primary model. Stated
differently, the role of the secondary ML algorithm is to determine whether a positive
from the primary (exogenous) model is true or false. It is not its purpose to come up
with a betting opportunity. Its purpose is to determine whether we should act or pass
on the opportunity that has been presented.
Meta-labeling is a very powerful tool to have in your arsenal, for four additional
reasons. First, ML algorithms are often criticized as black boxes (see Chapter 1).
Meta-labeling allows you to build an ML system on top of a white box (like a fundamental model founded on economic theory). This ability to transform a fundamental
model into an ML model should make meta-labeling particularly useful to “quantamental” firms. Second, the effects of overfitting are limited when you apply metalabeling, because ML will not decide the side of your bet, only the size. Third, by
decoupling the side prediction from the size prediction, meta-labeling enables sophisticated strategy structures. For instance, consider that the features driving a rally may
differ from the features driving a sell-off. In that case, you may want to develop an
ML strategy exclusively for long positions, based on the buy recommendations of
a primary model, and an ML strategy exclusively for short positions, based on the
sell recommendations of an entirely different primary model. Fourth, achieving high
accuracy on small bets and low accuracy on large bets will ruin you. As important as
identifying good opportunities is to size them properly, so it makes sense to develop
an ML algorithm solely focused on getting that critical decision (sizing) right. We will
retake this fourth point in Chapter 10. In my experience, meta-labeling ML models
can deliver more robust and reliable outcomes than standard labeling models.
3.8
THE QUANTAMENTAL WAY
You may have read in the press that many hedge funds are embracing the quantamental approach. A simple Google search will show reports that many hedge funds,
including some of the most traditional ones, are investing tens of millions of dollars in
technologies designed to combine human expertise with quantitative methods. It turns
out, meta-labeling is exactly what these people have been waiting for. Let us see why.
Suppose that you have a series of features that you believe can forecast some
prices, you just do not know how. Since you do not have a model to determine the side
of each bet, you need to learn both side and size. You apply what you have learned in
Section 3.5, and produce some labels based on the triple-barrier method with symmetric horizontal barriers. Now you are ready to fit your algorithm on a training set,
and evaluate the accuracy of your forecasts on a testing set. Alternatively, you could
do the following:
1. Use your forecasts from the primary model, and generate meta-labels. Remember, horizontal barriers do not need to be symmetric in this case.
2. Fit your model again on the same training set, but this time using the metalabels you just generated.
3. Combine the “sides” from the first ML model with the “sizes” from the second
ML model.
--- page 81 ---

54
LABELING
You can always add a meta-labeling layer to any primary model, whether that is an
ML algorithm, an econometric equation, a technical trading rule, a fundamental analysis, etc. That includes forecasts generated by a human, solely based on his intuition.
In that case, meta-labeling will help us figure out when we should pursue or dismiss
a discretionary PM’s call. The features used by such meta-labeling ML algorithm
could range from market information to biometric statistics to psychological assessments. For example, the meta-labeling ML algorithm could find that discretionary
PMs tend to make particularly good calls when there is a structural break (Chapter
17), as they may be quicker to grasp a change in the market regime. Conversely, it
may find that PMs under stress, as evidenced by fewer hours of sleep, fatigue, change
in weight, etc. tend to make inaccurate predictions.1 Many professions require regular
psychological exams, and an ML meta-labeling algorithm may find that those scores
are also relevant to assess our current degree of confidence on a PM’s predictions.
Perhaps none of these factors affect discretionary PMs, and their brains operate independently from their emotional being, like cold calculating machines. My guess is
that this is not the case, and therefore meta-labeling should become an essential ML
technique for every discretionary hedge fund. In the near future, every discretionary
hedge fund will become a quantamental firm, and meta-labeling offers them a clear
path to make that transition.
3.9
DROPPING UNNECESSARY LABELS
Some ML classifiers do not perform well when classes are too imbalanced. In those
circumstances, it is preferable to drop extremely rare labels and focus on the more
common outcomes. Snippet 3.8 presents a procedure that recursively drops observations associated with extremely rare labels. Function dropLabels recursively
eliminates those observations associated with classes that appear less than a fraction
minPct of cases, unless there are only two classes left.
SNIPPET 3.8
DROPPING UNDER-POPULATED LABELS
def dropLabels(events,minPtc=.05):
# apply weights, drop labels with insufficient examples
while True:
df0=events['bin'].value_counts(normalize=True)
if df0.min()>minPct or df0.shape[0]<3:break
print 'dropped label',df0.argmin(),df0.min()
events=events[events['bin']!=df0.argmin()]
return events
1 You are probably aware of at least one large hedge fund that monitors the emotional state of their research
analysts on a daily basis.
--- page 82 ---

EXERCISES
55
Incidentally, another reason you may want to drop unnecessary labels is this known
sklearn bug: https://github.com/scikit-learn/scikit-learn/issues/8566. This sort of bug
is a consequence of very fundamental assumptions in sklearn implementation, and
resolving them is far from trivial. In this particular instance, the error stems from
sklearn’s decision to operate with standard numpy arrays rather than structured arrays
or pandas objects. It is unlikely that there will be a fix by the time you are reading
this chapter, or in the near future. In later chapters, we will study ways to circumvent
these sorts of implementation errors, by building your own classes and expanding
sklearn’s functionality.
EXERCISES
3.1 Form dollar bars for E-mini S&P 500 futures:
(a) Apply a symmetric CUSUM filter (Chapter 2, Section 2.5.2.1) where the
threshold is the standard deviation of daily returns (Snippet 3.1).
(b) Use Snippet 3.4 on a pandas series t1, where numDays= 1.
(c) On those sampled features, apply the triple-barrier method, where
ptSl = [1,1] and t1 is the series you created in point 1.b.
(d) Apply getBins to generate the labels.
3.2 From exercise 1, use Snippet 3.8 to drop rare labels.
3.3 Adjust the getBins function (Snippet 3.5) to return a 0 whenever the vertical
barrier is the one touched first.
3.4 Develop a trend-following strategy based on a popular technical analysis statistic
(e.g., crossing moving averages). For each observation, the model suggests a side,
but not a size of the bet.
(a) Derive meta-labels for ptSl= [1,2] and t1 where numDays= 1. Use as
trgt the daily standard deviation as computed by Snippet 3.1.
(b) Train a random forest to decide whether to trade or not. Note: The decision
is whether to trade or not, {0,1}, since the underlying model (the crossing
moving average) has decided the side, {−1,1}.
3.5 Develop a mean-reverting strategy based on Bollinger bands. For each observation, the model suggests a side, but not a size of the bet.
(a) Derive meta-labels for ptSl= [0,2] and t1 where numDays= 1. Use as
trgt the daily standard deviation as computed by Snippet 3.1.
(b) Train a random forest to decide whether to trade or not. Use as features: volatility, serial correlation, and the crossing moving averages from
exercise 2.
(c) What is the accuracy of predictions from the primary model (i.e., if the secondary model does not filter the bets)? What are the precision, recall, and
F1-scores?
(d) What is the accuracy of predictions from the secondary model? What are the
precision, recall, and F1-scores?
--- page 83 ---

56
LABELING
BIBLIOGRAPHY
Ahmed, N., A. Atiya, N. Gayar, and H. El-Shishiny (2010): “An empirical comparison of machine
learning models for time series forecasting.” Econometric Reviews, Vol. 29, No. 5–6, pp. 594–
621.
Ballings, M., D. van den Poel, N. Hespeels, and R. Gryp (2015): “Evaluating multiple classifiers for
stock price direction prediction.” Expert Systems with Applications, Vol. 42, No. 20, pp. 7046–
7056.
Bontempi, G., S. Taieb, and Y. Le Borgne (2012): “Machine learning strategies for time series forecasting.” Lecture Notes in Business Information Processing, Vol. 138, No. 1, pp. 62–77.
Booth, A., E. Gerding and F. McGroarty (2014): “Automated trading with performance weighted
random forests and seasonality.” Expert Systems with Applications, Vol. 41, No. 8, pp. 3651–
3661.
Cao, L. and F. Tay (2001): “Financial forecasting using support vector machines.” Neural Computing
& Applications, Vol. 10, No. 2, pp. 184–192.
Cao, L., F. Tay and F. Hock (2003): “Support vector machine with adaptive parameters in financial
time series forecasting.” IEEE Transactions on Neural Networks, Vol. 14, No. 6, pp. 1506–
1518.
Cervell´o-Royo, R., F. Guijarro, and K. Michniuk (2015): “Stock market trading rule based on pattern
recognition and technical analysis: Forecasting the DJIA index with intraday data.” Expert
Systems with Applications, Vol. 42, No. 14, pp. 5963–5975.
Chang, P., C. Fan and J. Lin (2011): “Trend discovery in financial time series data using a casebased fuzzy decision tree.” Expert Systems with Applications, Vol. 38, No. 5, pp. 6070–
6080.
Kuan, C. and L. Tung (1995): “Forecasting exchange rates using feedforward and recurrent neural
networks.” Journal of Applied Econometrics, Vol. 10, No. 4, pp. 347–364.
Creamer, G. and Y. Freund (2007): “A boosting approach for automated trading.” Journal of Trading,
Vol. 2, No. 3, pp. 84–96.
Creamer, G. and Y. Freund (2010): “Automated trading with boosting and expert weighting.” Quantitative Finance, Vol. 10, No. 4, pp. 401–420.
Creamer, G., Y. Ren, Y. Sakamoto, and J. Nickerson (2016): “A textual analysis algorithm for the
equity market: The European case.” Journal of Investing, Vol. 25, No. 3, pp. 105–116.
Dixon, M., D. Klabjan, and J. Bang (2016): “Classification-based financial markets prediction
using deep neural networks.” Algorithmic Finance, forthcoming (2017). Available at SSRN:
https://ssrn.com/abstract=2756331.
Dunis, C., and M. Williams (2002): “Modelling and trading the euro/US dollar exchange rate: Do
neural network models perform better?” Journal of Derivatives & Hedge Funds, Vol. 8, No. 3,
pp. 211–239.
Feuerriegel, S. and H. Prendinger (2016): “News-based trading strategies.” Decision Support Systems, Vol. 90, pp. 65–74.
Hsu, S., J. Hsieh, T. Chih, and K. Hsu (2009): “A two-stage architecture for stock price forecasting by integrating self-organizing map and support vector regression.” Expert Systems with
Applications, Vol. 36, No. 4, pp. 7947–7951.
Huang, W., Y. Nakamori, and S. Wang (2005): “Forecasting stock market movement direction
with support vector machine.” Computers & Operations Research, Vol. 32, No. 10, pp. 2513–
2522.
Kara, Y., M. Boyacioglu, and O. Baykan (2011): “Predicting direction of stock price index movement
using artificial neural networks and support vector machines: The sample of the Istanbul Stock
Exchange.” Expert Systems with Applications, Vol. 38, No. 5, pp. 5311–5319.
Kim, K. (2003): “Financial time series forecasting using support vector machines.” Neurocomputing,
Vol. 55, No. 1, pp. 307–319.
--- page 84 ---

BIBLIOGRAPHY
57
Krauss, C., X. Do, and N. Huck (2017): “Deep neural networks, gradient-boosted trees, random
forests: Statistical arbitrage on the S&P 500.” European Journal of Operational Research,
Vol. 259, No. 2, pp. 689–702.
Laborda, R. and J. Laborda (2017): “Can tree-structured classifiers add value to the investor?”
Finance Research Letters, Vol. 22 (August), pp. 211–226.
Nakamura, E. (2005): “Inflation forecasting using a neural network.” Economics Letters, Vol. 86,
No. 3, pp. 373–378.
Olson, D. and C. Mossman (2003): “Neural network forecasts of Canadian stock returns using
accounting ratios.” International Journal of Forecasting, Vol. 19, No. 3, pp. 453–465.
Patel, J., S. Sha, P. Thakkar, and K. Kotecha (2015): “Predicting stock and stock price index movement using trend deterministic data preparation and machine learning techniques.” Expert
Systems with Applications, Vol. 42, No. 1, pp. 259–268.
Patel, J., S. Sha, P. Thakkar, and K. Kotecha (2015): “Predicting stock market index using fusion
of machine learning techniques.” Expert Systems with Applications, Vol. 42, No. 4, pp. 2162–
2172.
Qin, Q., Q. Wang, J. Li, and S. Shuzhi (2013): “Linear and nonlinear trading models with gradient
boosted random forests and application to Singapore Stock Market.” Journal of Intelligent
Learning Systems and Applications, Vol. 5, No. 1, pp. 1–10.
Sorensen, E., K. Miller, and C. Ooi (2000): “The decision tree approach to stock selection.” Journal
of Portfolio Management, Vol. 27, No. 1, pp. 42–52.
Theofilatos, K., S. Likothanassis, and A. Karathanasopoulos (2012): “Modeling and trading the
EUR/USD exchange rate using machine learning techniques.” Engineering, Technology &
Applied Science Research, Vol. 2, No. 5, pp. 269–272.
Trafalis, T. and H. Ince (2000): “Support vector machine for regression and applications to financial
forecasting.” Neural Networks, Vol. 6, No. 1, pp. 348–353.
Trippi, R. and D. DeSieno (1992): “Trading equity index futures with a neural network.” Journal of
Portfolio Management, Vol. 19, No. 1, pp. 27–33.
Tsai, C. and S. Wang (2009): “Stock price forecasting by hybrid machine learning techniques.”
Proceedings of the International Multi-Conference of Engineers and Computer Scientists,
Vol. 1, No. 1, pp. 755–760.
Tsai, C., Y. Lin, D. Yen, and Y. Chen (2011): “Predicting stock returns by classifier ensembles.”
Applied Soft Computing, Vol. 11, No. 2, pp. 2452–2459.
Wang, J. and S. Chan (2006): “Stock market trading rule discovery using two-layer bias decision
tree.” Expert Systems with Applications, Vol. 30, No. 4, pp. 605–611.
Wang, Q., J. Li, Q. Qin, and S. Ge (2011): “Linear, adaptive and nonlinear trading models for
Singapore Stock Market with random forests.” Proceedings of the 9th IEEE International Conference on Control and Automation, pp. 726–731.
Wei, P. and N. Wang (2016): “Wikipedia and stock return: Wikipedia usage pattern helps to predict
the individual stock movement.” Proceedings of the 25th International Conference Companion
on World Wide Web, Vol. 1, pp. 591–594.̇
Zbikowski, K. (2015): “Using volume weighted support vector machines with walk forward testing
and feature selection for the purpose of creating stock trading strategy.” Expert Systems with
Applications, Vol. 42, No. 4, pp. 1797–1805.
Zhang, G., B. Patuwo, and M. Hu (1998): “Forecasting with artificial neural networks: The state of
the art.” International Journal of Forecasting, Vol. 14, No. 1, pp. 35–62.
Zhu, M., D. Philpotts and M. Stevenson (2012): “The benefits of tree-based models for stock selection.” Journal of Asset Management, Vol. 13, No. 6, pp. 437–448.
Zhu, M., D. Philpotts, R. Sparks, and J. Stevenson, Maxwell (2011): “A hybrid approach to combining CART and logistic regression for stock ranking.” Journal of Portfolio Management,
Vol. 38, No. 1, pp. 100–109.
--- page 85 ---
--- page 86 ---

CHAPTER 4
Sample Weights
4.1
MOTIVATION
Chapter 3 presented several new methods for labeling financial observations. We
introduced two novel concepts, the triple-barrier method and meta-labeling, and
explained how they are useful in financial applications, including quantamental
investment strategies. In this chapter you will learn how to use sample weights to
address another problem ubiquitous in financial applications, namely that observations are not generated by independent and identically distributed (IID) processes.
Most of the ML literature is based on the IID assumption, and one reason many ML
applications fail in finance is because those assumptions are unrealistic in the case of
financial time series.
4.2
OVERLAPPING OUTCOMES
In Chapter 3 we assigned a label yi to an observed feature Xi, where yi was a function
of price bars that occurred over an interval [ti,0, ti,1
]. When ti,1 > tj,0 and i < j, then yi
and yj will both depend on a common return rtj,0,min{ti,1,tj,1
}, that is, the return over the
interval [tj,0, min {ti,1, tj,1
}]. The implication is that the series of labels, {yi
}
i=1,…,I,
are not IID whenever there is an overlap between any two consecutive outcomes,
∃i ||ti,1 > ti+1,0 .
Suppose that we circumvent this problem by restricting the bet horizon to ti,1 ≤
ti+1,0. In this case there is no overlap, because every feature outcome is determined
before or at the onset of the next observed feature. That would lead to coarse models where the features’ sampling frequency would be limited by the horizon used to
determine the outcome. On one hand, if we wished to investigate outcomes that lasted
a month, features would have to be sampled with a frequency up to monthly. On the
other hand, if we increased the sampling frequency to let’s say daily, we would be
59
--- page 87 ---

60
SAMPLE WEIGHTS
forced to reduce the outcome’s horizon to one day. Furthermore, if we wished to
apply a path-dependent labeling technique, like the triple-barrier method, the sampling frequency would be subordinated to the first barrier’s touch. No matter what
you do, restricting the outcome’s horizon to eliminate overlaps is a terrible solution.
We must allow ti,1 > ti+1,0, which brings us back to the problem of overlapping outcomes described earlier.
This situation is characteristic of financial applications. Most non-financial ML
researchers can assume that observations are drawn from IID processes. For example, you can obtain blood samples from a large number of patients, and measure their
cholesterol. Of course, various underlying common factors will shift the mean and
standard deviation of the cholesterol distribution, but the samples are still independent: There is one observation per subject. Suppose you take those blood samples,
and someone in your laboratory spills blood from each tube into the following nine
tubes to their right. That is, tube 10 contains blood for patient 10, but also blood from
patients 1 through 9. Tube 11 contains blood from patient 11, but also blood from
patients 2 through 10, and so on. Now you need to determine the features predictive
of high cholesterol (diet, exercise, age, etc.), without knowing for sure the cholesterol level of each patient. That is the equivalent challenge that we face in financial
ML, with the additional handicap that the spillage pattern is non-deterministic and
unknown. Finance is not a plug-and-play subject as it relates to ML applications.
Anyone who tells you otherwise will waste your time and money.
There are several ways to attack the problem of non-IID labels, and in this chapter
we will address it by designing sampling and weighting schemes that correct for the
undue influence of overlapping outcomes.
4.3
NUMBER OF CONCURRENT LABELS
Two labels yi and yj are concurrent at t when both are a function of at least one common return, rt−1,t =
pt
pt−1 −1. The overlap does not need to be perfect, in the sense of
both labels spanning the same time interval. In this section we are going to compute
the number of labels that are a function of a given return, rt−1,t. First, for each time
point t = 1, … , T, we form a binary array, {1t,i
}
i=1,…,I, where 1t,i ∈{0, 1}. Variable
1t,i = 1 if and only if [ti,0, ti,1
] overlaps with [t −1, t] and 1t,i = 0 otherwise. Recall
that the labels’ spans {[ti,0, ti,1
]}
i=1,…,I are defined by the t1 object introduced in
Chapter 3. Second, we compute the number of labels concurrent at t, ct = ∑I
i=1 1t,i.
Snippet 4.1 illustrates an implementation of this logic.
SNIPPET 4.1
ESTIMATING THE UNIQUENESS OF A LABEL
def mpNumCoEvents(closeIdx,t1,molecule):
’ ’ ’
Compute the number of concurrent events per bar.
+molecule[0] is the date of the first event on which the weight will be computed
+molecule[-1] is the date of the last event on which the weight will be computed
--- page 88 ---

AVERAGE UNIQUENESS OF A LABEL
61
Any event that starts before t1[molecule].max() impacts the count.
’ ’ ’
#1) find events that span the period [molecule[0],molecule[-1]]
t1=t1.ﬁllna(closeIdx[-1]) # unclosed events still must impact other weights
t1=t1[t1>=molecule[0]] # events that end at or after molecule[0]
t1=t1.loc[:t1[molecule].max()] # events that start at or before t1[molecule].max()
#2) count events spanning a bar
iloc=closeIdx.searchsorted(np.array([t1.index[0],t1.max()]))
count=pd.Series(0,index=closeIdx[iloc[0]:iloc[1]+1])
for tIn,tOut in t1.iteritems():count.loc[tIn:tOut]+=1.
return count.loc[molecule[0]:t1[molecule].max()]
4.4
AVERAGE UNIQUENESS OF A LABEL
In this section we are going to estimate a label’s uniqueness (non-overlap) as its
average uniqueness over its lifespan. First, the uniqueness of a label i at time t is
ut,i = 1t,ic−1
t . Second, the average uniqueness of label i is the average ut,i over the
label’s lifespan,̄ ui =
(∑T
t=1 ut,i
) (∑T
t=1 1t,i
)−1
. This average uniqueness can also
be interpreted as the reciprocal of the harmonic average of ct over the event’s lifespan. Figure 4.1 plots the histogram of uniqueness values derived from an object t1.
Snippet 4.2 implements this calculation.
FIGURE 4.1
Histogram of uniqueness values
--- page 89 ---

62
SAMPLE WEIGHTS
SNIPPET 4.2
ESTIMATING THE AVERAGE UNIQUENESS OF A
LABEL
def mpSampleTW(t1,numCoEvents,molecule):
# Derive average uniqueness over the event's lifespan
wght=pd.Series(index=molecule)
for tIn,tOut in t1.loc[wght.index].iteritems():
wght.loc[tIn]=(1./numCoEvents.loc[tIn:tOut]).mean()
return wght
#———————————————————————————————————————
numCoEvents=mpPandasObj(mpNumCoEvents,('molecule',events.index),numThreads, \
closeIdx=close.index,t1=events['t1'])
numCoEvents=numCoEvents.loc[~numCoEvents.index.duplicated(keep='last')]
numCoEvents=numCoEvents.reindex(close.index).ﬁllna(0)
out['tW']=mpPandasObj(mpSampleTW,('molecule',events.index),numThreads, \
t1=events['t1'],numCoEvents=numCoEvents)
Note that we are making use again of the function mpPandasObj, which speeds up
calculations via multiprocessing (see Chapter 20). Computing the average uniqueness
associated with label i,̄ ui, requires information that is not available until a future time,
events['t1']. This is not a problem, because {̄ui
}
i=1,…,I are used on the training
set in combination with label information, and not on the testing set. These {̄ui
}
i=1,…,I
are not used for forecasting the label, hence there is no information leakage. This
procedure allows us to assign a uniqueness score between 0 and 1 for each observed
feature, in terms of non-overlapping outcomes.
4.5
BAGGING CLASSIFIERS AND UNIQUENESS
The probability of not selecting a particular item i after I draws with replacement on
a set of I items is (1 −I−1)I. As the sample size grows, that probability converges to
the asymptotic value limI→∞(1 −I−1)I = e−1. That means that the number of unique
observations drawn is expected to be (1 −e−1) ≈2
3.
Suppose that the maximum number of non-overlapping outcomes is K ≤I. Following the same argument, the probability of not selecting a particular item i after I
draws with replacement on a set of I items is (1 −K−1)I. As the sample size grows,
that probability can be approximated as (1 −I−1)I K
I ≈e−K
I . That means that the number of unique observations drawn is expected to be 1 −e−K
I ≤1 −e−1. The implication is that incorrectly assuming IID draws leads to oversampling.
When
sampling
with
replacement
(bootstrap)
on
observations
with
I−1 ∑I
i=1̄ ui ≪1, it becomes increasingly likely that in-bag observations will
be (1) redundant to each other, and (2) very similar to out-of-bag observations.
--- page 90 ---

BAGGING CLASSIFIERS AND UNIQUENESS
63
Redundancy of draws makes the bootstrap inefficient (see Chapter 6). For example, in the case of a random forest, all trees in the forest will essentially be
very similar copies of a single overfit decision tree. And because the random
sampling makes out-of-bag examples very similar to the in-bag ones, out-of-bag
accuracy will be grossly inflated. We will address this second issue in Chapter
7, when we study cross-validation under non-IID observations. For the moment,
let us concentrate on the first issue, namely bagging under observations where
I−1 ∑I
i=1̄ ui ≪1.
A first solution is to drop overlapping outcomes before performing the bootstrap.
Because overlaps are not perfect, dropping an observation just because there is a
partial overlap will result in an extreme loss of information. I do not advise you to
follow this solution.
A second and better solution is to utilize the average uniqueness, I−1 ∑I
i=1̄ ui, to
reduce the undue influence of outcomes that contain redundant information. Accordingly, we could sample only a fraction out['tW'].mean() of the observations, or
a small multiple of that. In sklearn, the sklearn.ensemble.BaggingClassiﬁer
class
accepts
an
argument
max_samples,
which
can
be
set
to
max_samples=out['tW'].mean(). In this way, we enforce that the in-bag
observations are not sampled at a frequency much higher than their uniqueness.
Random forests do not offer that max_samples functionality, however, a solution
is to bag a large number of decision trees. We will discuss this solution further in
Chapter 6.
4.5.1
Sequential Bootstrap
A third and better solution is to perform a sequential bootstrap, where draws are made
according to a changing probability that controls for redundancy. Rao et al. [1997]
propose sequential resampling with replacement until K distinct original observations appear. Although interesting, their scheme does not fully apply to our financial
problem. In the following sections we introduce an alternative method that addresses
directly the problem of overlapping outcomes.
First, an observation Xi is drawn from a uniform distribution, i ∼U [1, I], that
is, the probability of drawing any particular value i is originally 𝛿(1)
i
= I−1. For the
second draw, we wish to reduce the probability of drawing an observation Xj with
a highly overlapping outcome. Remember, a bootstrap allows sampling with repetition, so it is still possible to draw Xi again, but we wish to reduce its likelihood, since
there is an overlap (in fact, a perfect overlap) between Xi and itself. Let us denote as
𝜑the sequence of draws so far, which may include repetitions. Until now, we know
that 𝜑(1) = {i}. The uniqueness of j at time t is u(2)
t,j = 1t,j
(
1 + ∑
k∈𝜑(1) 1t,k
)−1
, as
that is the uniqueness that results from adding alternative j’s to the existing sequence
of draws 𝜑(1). The average uniqueness of j is the average u(2)
t,j over j’s lifespan,
--- page 91 ---

64
SAMPLE WEIGHTS̄
u(2)
j
=
(∑T
t=1 ut,j
) (∑T
t=1 1t,j
)−1
. We can now make a second draw based on the
updated probabilities
{
𝛿(2)
j
}
j=1,…,I,
𝛿(2)
j
=̄ u(2)
j
( I∑
k=1̄
u(2)
k
)−1
where
{
𝛿(2)
j
}
j=1,..,I are scaled to add up to 1, ∑I
j=1 𝛿(2)
j
= 1. We can now do a second
draw, update 𝜑(2) and re-evaluate
{
𝛿(3)
j
}
j=1,…,I. The process is repeated until I draws
have taken place. This sequential bootstrap scheme has the advantage that overlaps
(even repetitions) are still possible, but decreasingly likely. The sequential bootstrap
sample will be much closer to IID than samples drawn from the standard bootstrap
method. This can be verified by measuring an increase in I−1 ∑I
i=1̄ ui, relative to the
standard bootstrap method.
4.5.2
Implementation of Sequential Bootstrap
Snippet 4.3 derives an indicator matrix from two arguments: the index of bars
(barIx), and the pandas Series t1, which we used multiple times in Chapter 3. As
a reminder, t1 is defined by an index containing the time at which the features are
observed, and a values array containing the time at which the label is determined. The
output of this function is a binary matrix indicating what (price) bars influence the
label for each observation.
SNIPPET 4.3
BUILD AN INDICATOR MATRIX
import pandas as pd,numpy as np
#———————————————————————————————————————
def getIndMatrix(barIx,t1):
# Get indicator matrix
indM=pd.DataFrame(0,index=barIx,columns=range(t1.shape[0]))
for i,(t0,t1) in enumerate(t1.iteritems()):indM.loc[t0:t1,i]=1.
return indM
Snippet 4.4 returns the average uniqueness of each observed feature. The input is
the indicator matrix built by getIndMatrix.
--- page 92 ---

BAGGING CLASSIFIERS AND UNIQUENESS
65
SNIPPET 4.4
COMPUTE AVERAGE UNIQUENESS
def getAvgUniqueness(indM):
# Average uniqueness from indicator matrix
c=indM.sum(axis=1) # concurrency
u=indM.div(c,axis=0) # uniqueness
avgU=u[u>0].mean() # average uniqueness
return avgU
Snippet 4.5 gives us the index of the features sampled by sequential bootstrap. The
inputs are the indicator matrix (indM) and an optional sample length (sLength), with
a default value of as many draws as rows in indM.
SNIPPET 4.5
RETURN SAMPLE FROM SEQUENTIAL BOOTSTRAP
def seqBootstrap(indM,sLength=None):
# Generate a sample via sequential bootstrap
if sLength is None:sLength=indM.shape[1]
phi=[]
while len(phi)<sLength:
avgU=pd.Series()
for i in indM:
indM_=indM[phi+[i]] # reduce indM
avgU.loc[i]=getAvgUniqueness(indM_).iloc[-1]
prob=avgU/avgU.sum() # draw prob
phi+=[np.random.choice(indM.columns,p=prob)]
return phi
4.5.3
A Numerical Example
Consider a set of labels {yi
}
i=1,2,3, where label y1 is a function of return r0,3, label
y2 is a function of return r2,4 and label y3 is a function of return r4,6. The outcomes’
overlaps are characterized by this indicator matrix {1t,i
},
{1t,i
} =
⎡
⎢
⎢
⎢
⎢
⎢
⎢⎣
1
0
0
1
0
0
1
1
0
0
1
0
0
0
1
0
0
1
⎤
⎥
⎥
⎥
⎥
⎥
⎥⎦
--- page 93 ---

66
SAMPLE WEIGHTS
The procedure starts with 𝜑(0) = ∅, and a uniform distribution of probability,
𝛿i = 1
3, ∀i = 1, 2, 3. Suppose that we randomly draw a number from {1, 2, 3}, and
2 is selected. Before we make a second draw on {1, 2, 3} (remember, a bootstrap
samples with repetition), we need to adjust the probabilities. The set of observations drawn so far is 𝜑(1) = {2}. The average uniqueness for the first feature is̄ u(2)
1
=
(
1 + 1 + 1
2
)
1
3 = 5
6 < 1, and for the second feature is̄ u(2)
2
=
(
1
2 + 1
2
)
1
2 = 1
2 < 1. The
probabilities for the second draw are 𝛿(2) =
{
5
14, 3
14, 6
14
}
. Two points are worth mentioning: (1) The lowest probability goes to the feature that was picked in the first draw,
as that would exhibit the highest overlap; and (2) among the two possible draws outside 𝜑(1), the greater probability goes to 𝛿(2)
3 , as that is the label with no overlap to
𝜑(1). Suppose that the second draw selects number 3. We leave as an exercise the
update of the probabilities 𝛿(3) for the third and final draw. Snippet 4.6 runs a sequential bootstrap on the {1t,i
} indicator matrix in this example.
SNIPPET 4.6
EXAMPLE OF SEQUENTIAL BOOTSTRAP
def main():
t1=pd.Series([2,3,5],index=[0,2,4]) # t0,t1 for each feature obs
barIx=range(t1.max()+1) # index of bars
indM=getIndMatrix(barIx,t1)
phi=np.random.choice(indM.columns,size=indM.shape[1])
print phi
print 'Standard uniqueness:',getAvgUniqueness(indM[phi]).mean()
phi=seqBootstrap(indM)
print phi
print 'Sequential uniqueness:',getAvgUniqueness(indM[phi]).mean()
return
4.5.4
Monte Carlo Experiments
We can evaluate the efficiency of the sequential bootstrap algorithm through experimental methods. Snippet 4.7 lists the function that generates a random t1 series for a
number of observations numObs (I). Each observation is made at a random number,
drawn from a uniform distribution, with boundaries 0 and numBars, where numBars
is the number of bars (T). The number of bars spanned by the observation is determined by drawing a random number from a uniform distribution with boundaries 0
and maxH.
SNIPPET 4.7
GENERATING A RANDOM T1 SERIES
def getRndT1(numObs,numBars,maxH):
# random t1 Series
t1=pd.Series()
--- page 94 ---

BAGGING CLASSIFIERS AND UNIQUENESS
67
for i in xrange(numObs):
ix=np.random.randint(0,numBars)
val=ix+np.random.randint(1,maxH)
t1.loc[ix]=val
return t1.sort_index()
Snippet 4.8 takes that random t1 series, and derives the implied indicator matrix,
indM. This matrix is then subjected to two procedures. In the first one, we derive the
average uniqueness from a standard bootstrap (random sampling with replacement).
In the second one, we derive the average uniqueness by applying our sequential bootstrap algorithm. Results are reported as a dictionary.
SNIPPET 4.8
UNIQUENESS FROM STANDARD AND SEQUENTIAL
BOOTSTRAPS
def auxMC(numObs,numBars,maxH):
# Parallelized auxiliary function
t1=getRndT1(numObs,numBars,maxH)
barIx=range(t1.max()+1)
indM=getIndMatrix(barIx,t1)
phi=np.random.choice(indM.columns,size=indM.shape[1])
stdU=getAvgUniqueness(indM[phi]).mean()
phi=seqBootstrap(indM)
seqU=getAvgUniqueness(indM[phi]).mean()
return {'stdU':stdU,'seqU':seqU}
These operations have to be repeated over a large number of iterations. Snippet 4.9
implements this Monte Carlo using the multiprocessing techniques discussed in
Chapter 20. For example, it will take about 6 hours for a 24-cores server to carry out
a Monte Carlo of 1E6 iterations, where numObs=10, numBars=100, and maxH=5.
Without parallelization, a similar Monte Carlo experiment would have taken about
6 days.
SNIPPET 4.9
MULTI-THREADED MONTE CARLO
import pandas as pd,numpy as np
from mpEngine import processJobs,processJobs_
#———————————————————————————————————————
def mainMC(numObs=10,numBars=100,maxH=5,numIters=1E6,numThreads=24):
# Monte Carlo experiments
jobs=[]
for i in xrange(int(numIters)):
job={'func':auxMC,'numObs':numObs,'numBars':numBars,'maxH':maxH}
jobs.append(job)
--- page 95 ---

68
SAMPLE WEIGHTS
FIGURE 4.2
Monte Carlo experiment of standard vs. sequential bootstraps
if numThreads==1:out=processJobs_(jobs)
else:out=processJobs(jobs,numThreads=numThreads)
print pd.DataFrame(out).describe()
return
Figure 4.2 plots the histogram of the uniqueness from standard bootstrapped samples (left) and the sequentially bootstrapped samples (right). The median of the
average uniqueness for the standard method is 0.6, and the median of the average
uniqueness for the sequential method is 0.7. An ANOVA test on the difference of
means returns a vanishingly small probability. Statistically speaking, samples from
the sequential bootstrap method have an expected uniqueness that exceeds that of the
standard bootstrap method, at any reasonable confidence level.
4.6
RETURN ATTRIBUTION
In the previous section we learned a method to bootstrap samples closer to IID. In
this section we will introduce a method to weight those samples for the purpose of
training an ML algorithm. Highly overlapping outcomes would have disproportionate
weights if considered equal to non-overlapping outcomes. At the same time, labels
associated with large absolute returns should be given more importance than labels
--- page 96 ---

RETURN ATTRIBUTION
69
with negligible absolute returns. In short, we need to weight observations by some
function of both uniqueness and absolute return.
When labels are a function of the return sign ({−1, 1} for standard labeling or
{0, 1} for meta-labeling), the sample weights can be defined in terms of the sum of
the attributed returns over the event’s lifespan, [ti,0, ti,1
],̃
wi =
||||||
ti,1
∑
t=ti,0
rt−1,t
ct
||||||
wi =̃ wiI
( I∑
j=1̃
wj
)−1
hence ∑I
i=1 wi = I. We have scaled these weights to add up to I, since libraries
(including sklearn) usually define algorithmic parameters assuming a default weight
of 1.
The rationale for this method is that we wish to weight an observation as a function
of the absolute log returns that can be attributed uniquely to it. However, this method
will not work if there is a “neutral” (return below threshold) case. For that case, lower
returns should be assigned higher weights, not the reciprocal. The “neutral” case is
unnecessary, as it can be implied by a “−1” or “1” prediction with low confidence.
This is one of several reasons I would generally advise you to drop “neutral” cases.
Snippet 4.10 implements this method.
SNIPPET 4.10
DETERMINATION OF SAMPLE WEIGHT BY
ABSOLUTE RETURN ATTRIBUTION
def mpSampleW(t1,numCoEvents,close,molecule):
# Derive sample weight by return attribution
ret=np.log(close).diff() # log-returns, so that they are additive
wght=pd.Series(index=molecule)
for tIn,tOut in t1.loc[wght.index].iteritems():
wght.loc[tIn]=(ret.loc[tIn:tOut]/numCoEvents.loc[tIn:tOut]).sum()
return wght.abs()
#———————————————————————————————————————
out['w']=mpPandasObj(mpSampleW,('molecule',events.index),numThreads, \
t1=events['t1'],numCoEvents=numCoEvents,close=close)
out['w']*=out.shape[0]/out['w'].sum()
