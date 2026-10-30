# Advances in Financial Machine Learning.pdf — pages 267–286

--- page 267 ---

240
MACHINE LEARNING ASSET ALLOCATION
with solution 𝜔=
V−1a
a′V−1a. For the characteristic vector a = 1N, the solution is the
minimum variance portfolio. If V is diagonal, 𝜔n =
V−1
n,n
∑N
i=1 V−1
i,i
. In the particular case of
N = 2, 𝜔1 =
1
V1,1
1
V1,1 +
1
V2,2
= 1 −
V1,1
V1,1+V2,2 , which is how stage 3 splits a weight between
two bisections of a subset.
16.A.3
REPRODUCING THE NUMERICAL EXAMPLE
Snippet 16.4 can be used to reproduce our results and simulate additional numerical
examples. Function generateData produces a matrix of time series where a number
size0 of vectors are uncorrelated, and a number size1 of vectors are correlated.
The reader can change the np.random.seed in generateData to run alternative
examples and gain an intuition of how HRP works. Scipy’s function linkage can be
used to perform stage 1 (Section 16.4.1), function getQuasiDiag performs stage 2
(Section 16.4.2), and function getRecBipart carries out stage 3 (Section 16.4.3).
SNIPPET 16.4
FULL IMPLEMENTATION OF THE HRP ALGORITHM
import matplotlib.pyplot as mpl
import scipy.cluster.hierarchy as sch,random,numpy as np,pandas as pd
#———————————————————————————————————————
def getIVP(cov,**kargs):
# Compute the inverse-variance portfolio
ivp=1./np.diag(cov)
ivp/=ivp.sum()
return ivp
#———————————————————————————————————————
def getClusterVar(cov,cItems):
# Compute variance per cluster
cov_=cov.loc[cItems,cItems] # matrix slice
w_=getIVP(cov_).reshape(-1,1)
cVar=np.dot(np.dot(w_.T,cov_),w_)[0,0]
return cVar
#———————————————————————————————————————
def getQuasiDiag(link):
# Sort clustered items by distance
link=link.astype(int)
sortIx=pd.Series([link[-1,0],link[-1,1]])
numItems=link[-1,3] # number of original items
while sortIx.max()>=numItems:
sortIx.index=range(0,sortIx.shape[0]*2,2) # make space
df0=sortIx[sortIx>=numItems] # find clusters
i=df0.index;j=df0.values-numItems
sortIx[i]=link[j,0] # item 1
--- page 268 ---

REPRODUCING THE NUMERICAL EXAMPLE
241
df0=pd.Series(link[j,1],index=i+1)
sortIx=sortIx.append(df0) # item 2
sortIx=sortIx.sort_index() # re-sort
sortIx.index=range(sortIx.shape[0]) # re-index
return sortIx.tolist()
#———————————————————————————————————————
def getRecBipart(cov,sortIx):
# Compute HRP alloc
w=pd.Series(1,index=sortIx)
cItems=[sortIx] # initialize all items in one cluster
while len(cItems)>0:
cItems=[i[j:k] for i in cItems for j,k in ((0,len(i)/2), \
(len(i)/2,len(i))) if len(i)>1] # bi-section
for i in xrange(0,len(cItems),2): # parse in pairs
cItems0=cItems[i] # cluster 1
cItems1=cItems[i+1] # cluster 2
cVar0=getClusterVar(cov,cItems0)
cVar1=getClusterVar(cov,cItems1)
alpha=1-cVar0/(cVar0+cVar1)
w[cItems0]*=alpha # weight 1
w[cItems1]*=1-alpha # weight 2
return w
#———————————————————————————————————————
def correlDist(corr):
# A distance matrix based on correlation, where 0<=d[i,j]<=1
# This is a proper distance metric
dist=((1-corr)/2.)**.5 # distance matrix
return dist
#———————————————————————————————————————
def plotCorrMatrix(path,corr,labels=None):
# Heatmap of the correlation matrix
if labels is None:labels=[]
mpl.pcolor(corr)
mpl.colorbar()
mpl.yticks(np.arange(.5,corr.shape[0]+.5),labels)
mpl.xticks(np.arange(.5,corr.shape[0]+.5),labels)
mpl.saveﬁg(path)
mpl.clf();mpl.close() # reset pylab
return
#———————————————————————————————————————
def generateData(nObs,size0,size1,sigma1):
# Time series of correlated variables
#1) generating some uncorrelated data
np.random.seed(seed=12345);random.seed(12345)
x=np.random.normal(0,1,size=(nObs,size0)) # each row is a variable
#2) creating correlation between the variables
cols=[random.randint(0,size0–1) for i in xrange(size1)]
y=x[:,cols]+np.random.normal(0,sigma1,size=(nObs,len(cols)))
x=np.append(x,y,axis=1)
--- page 269 ---

242
MACHINE LEARNING ASSET ALLOCATION
x=pd.DataFrame(x,columns=range(1,x.shape[1]+1))
return x,cols
#———————————————————————————————————————
def main():
#1) Generate correlated data
nObs,size0,size1,sigma1=10000,5,5,.25
x,cols=generateData(nObs,size0,size1,sigma1)
print [(j+1,size0+i) for i,j in enumerate(cols,1)]
cov,corr=x.cov(),x.corr()
#2) compute and plot correl matrix
plotCorrMatrix('HRP3_corr0.png',corr,labels=corr.columns)
#3) cluster
dist=correlDist(corr)
link=sch.linkage(dist,'single')
sortIx=getQuasiDiag(link)
sortIx=corr.index[sortIx].tolist() # recover labels
df0=corr.loc[sortIx,sortIx] # reorder
plotCorrMatrix('HRP3_corr1.png',df0,labels=df0.columns)
#4) Capital allocation
hrp=getRecBipart(cov,sortIx)
print hrp
return
#———————————————————————————————————————
if __name__=='__main__':main()
16.A.4
REPRODUCING THE MONTE CARLO EXPERIMENT
Snippet 16.5 implements Monte Carlo experiments on three allocation methods:
HRP, CLA, and IVP. All libraries are standard except for HRP, which is provided
in Appendix 16.A.3, and CLA, which can be found in Bailey and L´opez de Prado
[2013]. The subroutine generateData simulates the correlated data, with two types
of random shocks: common to various investments and specific to a single investment.
There are two shocks of each type, one positive and one negative. The variables for
the experiments are set as arguments of hrpMC. They were chosen arbitrarily, and the
user can experiment with alternative combinations.
SNIPPET 16.5
MONTE CARLO EXPERIMENT ON HRP
OUT-OF-SAMPLE PERFORMANCE
import scipy.cluster.hierarchy as sch,random,numpy as np,pandas as pd,CLA
from HRP import correlDist,getIVP,getQuasiDiag,getRecBipart
#———————————————————————————————————————
def generateData(nObs,sLength,size0,size1,mu0,sigma0,sigma1F):
# Time series of correlated variables
#1) generate random uncorrelated data
--- page 270 ---

REPRODUCING THE MONTE CARLO EXPERIMENT
243
x=np.random.normal(mu0,sigma0,size=(nObs,size0))
#2) create correlation between the variables
cols=[random.randint(0,size0–1) for i in xrange(size1)]
y=x[:,cols]+np.random.normal(0,sigma0*sigma1F,size=(nObs,len(cols)))
x=np.append(x,y,axis=1)
#3) add common random shock
point=np.random.randint(sLength,nObs-1,size=2)
x[np.ix_(point,[cols[0],size0])]=np.array([[-.5,-.5],[2,2]])
#4) add specific random shock
point=np.random.randint(sLength,nObs-1,size=2)
x[point,cols[-1]]=np.array([-.5,2])
return x,cols
#———————————————————————————————————————
def getHRP(cov,corr):
# Construct a hierarchical portfolio
corr,cov=pd.DataFrame(corr),pd.DataFrame(cov)
dist=correlDist(corr)
link=sch.linkage(dist,'single')
sortIx=getQuasiDiag(link)
sortIx=corr.index[sortIx].tolist() # recover labels
hrp=getRecBipart(cov,sortIx)
return hrp.sort_index()
#———————————————————————————————————————
def getCLA(cov,**kargs):
# Compute CLA's minimum variance portfolio
mean=np.arange(cov.shape[0]).reshape(-1,1) # Not used by C portf
lB=np.zeros(mean.shape)
uB=np.ones(mean.shape)
cla=CLA.CLA(mean,cov,lB,uB)
cla.solve()
return cla.w[-1].ﬂatten()
#———————————————————————————————————————
def hrpMC(numIters=1e4,nObs=520,size0=5,size1=5,mu0=0,sigma0=1e-2, \
sigma1F=.25,sLength=260,rebal=22):
# Monte Carlo experiment on HRP
methods=[getIVP,getHRP,getCLA]
stats,numIter={i.__name__:pd.Series() for i in methods},0
pointers=range(sLength,nObs,rebal)
while numIter<numIters:
print numIter
#1) Prepare data for one experiment
x,cols=generateData(nObs,sLength,size0,size1,mu0,sigma0,sigma1F)
r={i.__name__:pd.Series() for i in methods}
#2) Compute portfolios in-sample
for pointer in pointers:
x_=x[pointer-sLength:pointer]
cov_,corr_=np.cov(x_,rowvar=0),np.corrcoef(x_,rowvar=0)
#3) Compute performance out-of-sample
x_=x[pointer:pointer+rebal]
--- page 271 ---

244
MACHINE LEARNING ASSET ALLOCATION
for func in methods:
w_=func(cov=cov_,corr=corr_) # callback
r_=pd.Series(np.dot(x_,w_))
r[func.__name__]=r[func.__name__].append(r_)
#4) Evaluate and store results
for func in methods:
r_=r[func.__name__].reset_index(drop=True)
p_=(1+r_).cumprod()
stats[func.__name__].loc[numIter]=p_.iloc[-1]-1
numIter+=1
#5) Report results
stats=pd.DataFrame.from_dict(stats,orient='columns')
stats.to_csv('stats.csv')
df0,df1=stats.std(),stats.var()
print pd.concat([df0,df1,df1/df1['getHRP']-1],axis=1)
return
#———————————————————————————————————————
if __name__=='__main__':hrpMC()
EXERCISES
16.1 Given the PnL series on N investment strategies:
(a) Align them to the average frequency of their bets (e.g., weekly observations
for strategies that trade on a weekly basis). Hint: This kind of data alignment
is sometimes called “downsampling.”
(b) Compute the covariance of their returns, V.
(c) Identify the hierarchical clusters among the N strategies.
(d) Plot the clustered correlation matrix of the N strategies.
16.2 Using the clustered covariance matrix V from exercise 1:
(a) Compute the HRP allocations.
(b) Compute the CLA allocations.
(c) Compute the IVP allocations.
16.3 Using the covariance matrix V from exercise 1:
(a) Perform a spectral decomposition: VW = WΛ.
(b) Form an array 𝜀by drawing N random numbers from a U[0, 1] distribution.
(c) Form an NxN matrix̃ Λ, wherẽ Λn,n = N𝜀nΛn,n(∑N
n=1 𝜀n)−1, n = 1, … , N.
(d) Computẽ V = W̃ΛW−1.
(e) Repeat exercise 2, this time using̃ V as covariance matrix. What allocation
method has been most impacted by the re-scaling of spectral variances?
16.4 How would you modify the HRP algorithm to produce allocations that add up
to 0, where |wn| ≤1, ∀n = 1, … , N?
16.5 Can you think of an easy way to incorporate expected returns in the HRP
allocations?
--- page 272 ---

REFERENCES
245
REFERENCES
Bailey, D. and M. L´opez de Prado (2012): “Balanced baskets: A new approach to trading and
hedging risks.” Journal of Investment Strategies, Vol. 1, No. 4, pp. 21–62. Available at
http://ssrn.com/abstract=2066170.
Bailey, D. and M. L´opez de Prado (2013): “An open-source implementation of the critical-line
algorithm for portfolio optimization.” Algorithms, Vol. 6, No. 1, pp. 169–196. Available at
http://ssrn.com/abstract=2197616.
Bailey, D., J. Borwein, M. L´opez de Prado, and J. Zhu (2014) “Pseudo-mathematics and
financial charlatanism: The effects of backtest overfitting on out-of-sample performance.”
Notices of the American Mathematical Society, Vol. 61, No. 5, pp. 458–471. Available at
http://ssrn.com/abstract=2308659.
Bailey, D. and M. L´opez de Prado (2014): “The deflated Sharpe ratio: Correcting for selection
bias, backtest overfitting and non-normality.” Journal of Portfolio Management, Vol. 40, No. 5,
pp. 94–107.
Black, F. and R. Litterman (1992): “Global portfolio optimization.” Financial Analysts Journal,
Vol. 48, pp. 28–43.
Brualdi, R. (2010): “The mutually beneficial relationship of graphs and matrices.” Conference Board
of the Mathematical Sciences, Regional Conference Series in Mathematics, Nr. 115.
Calkin, N. and M. L´opez de Prado (2014): “Stochastic flow diagrams.” Algorithmic Finance, Vol. 3,
No. 1, pp. 21–42. Availble at http://ssrn.com/abstract=2379314.
Calkin, N. and M. L´opez de Prado (2014): “The topology of macro financial flows: An application of stochastic flow diagrams.” Algorithmic Finance, Vol. 3, No. 1, pp. 43–85. Available at
http://ssrn.com/abstract=2379319.
Clarke, R., H. De Silva, and S. Thorley (2002): “Portfolio constraints and the fundamental law of
active management.” Financial Analysts Journal, Vol. 58, pp. 48–66.
De Miguel, V., L. Garlappi, and R. Uppal (2009): “Optimal versus naive diversification: How inefficient is the 1/N portfolio strategy?” Review of Financial Studies, Vol. 22, pp. 1915–1953.
Jurczenko, E. (2015): Risk-Based and Factor Investing, 1st ed. Elsevier Science.
Kolanovic, M., A. Lau, T. Lee, and R. Krishnamachari (2017): “Cross asset portfolios of tradable risk
premia indices. Hierarchical risk parity: Enhancing returns at target volatility.” White paper,
Global Quantitative & Derivatives Strategy. J.P. Morgan, April 26.
Kolm, P., R. Tutuncu and F. Fabozzi (2014): “60 years of portfolio optimization.” European Journal
of Operational Research, Vol. 234, No. 2, pp. 356–371.
Kuhn, H. W. and A. W. Tucker (1951): “Nonlinear programming.” Proceedings of 2nd Berkeley
Symposium. Berkeley, University of California Press, pp. 481–492.
Markowitz, H. (1952): “Portfolio selection.” Journal of Finance, Vol. 7, pp. 77–91.
Merton, R. (1976): “Option pricing when underlying stock returns are discontinuous.” Journal of
Financial Economics, Vol. 3, pp. 125–144.
Michaud, R. (1998): Efficient Asset Allocation: A Practical Guide to Stock Portfolio Optimization
and Asset Allocation, 1st ed. Harvard Business School Press.
Ledoit, O. and M. Wolf (2003): “Improved estimation of the covariance matrix of stock returns
with an application to portfolio selection.” Journal of Empirical Finance, Vol. 10, No. 5,
pp. 603–621.
Raffinot, T. (2017): “Hierarchical clustering based asset allocation.” Journal of Portfolio Management, forthcoming.
Rokach, L. and O. Maimon (2005): “Clustering methods,” in Rokach, L. and O. Maimon, eds., Data
Mining and Knowledge Discovery Handbook. Springer, pp. 321–352.
--- page 273 ---
--- page 274 ---

P A R T 4
Useful Financial Features
Chapter 17: Structural Breaks, 249
Chapter 18: Entropy Features, 263
Chapter 19: Microstructural Features, 281
247
--- page 275 ---
--- page 276 ---

CHAPTER 17
Structural Breaks
17.1
MOTIVATION
In developing an ML-based investment strategy, we typically wish to bet when there
is a confluence of factors whose predicted outcome offers a favorable risk-adjusted
return. Structural breaks, like the transition from one market regime to another, is
one example of such a confluence that is of particular interest. For instance, a meanreverting pattern may give way to a momentum pattern. As this transition takes place,
most market participants are caught off guard, and they will make costly mistakes.
This sort of errors is the basis for many profitable strategies, because the actors on
the losing side will typically become aware of their mistake once it is too late. Before
they accept their losses, they will act irrationally, try to hold the position, and hope
for a comeback. Sometimes they will even increase a losing position, in desperation.
Eventually they will be forced to stop loss or stop out. Structural breaks offer some of
the best risk/rewards. In this chapter, we will review some methods that measure the
likelihood of structural breaks, so that informative features can be built upon them.
17.2
TYPES OF STRUCTURAL BREAK TESTS
We can classify structural break tests in two general categories:
r CUSUM tests: These test whether the cumulative forecasting errors significantly deviate from white noise.
r Explosiveness tests: Beyond deviation from white noise, these test whether the
process exhibits exponential growth or collapse, as this is inconsistent with a
random walk or stationary process, and it is unsustainable in the long run.
249
--- page 277 ---

250
STRUCTURAL BREAKS
◦Right-tail unit-root tests: These tests evaluate the presence of exponential
growth or collapse, while assuming an autoregressive specification.
◦Sub/super-martingale tests: These tests evaluate the presence of exponential growth or collapse under a variety of functional forms.
17.3
CUSUM TESTS
In Chapter 2 we introduced the CUSUM filter, which we applied in the context of
event-based sampling of bars. The idea was to sample a bar whenever some variable,
like cumulative prediction errors, exceeded a predefined threshold. This concept can
be further extended to test for structural breaks.
17.3.1
Brown-Durbin-Evans CUSUM Test on Recursive Residuals
This test was proposed by Brown, Durbin and Evans [1975]. Let us assume that at
every observation t = 1, … , T, we count with an array of features xt predictive of a
value yt. Matrix Xt is composed of the time series of features t ≤T, {xi}i=1,…,t. These
authors propose that we compute recursive least squares (RLS) estimates of 𝛽, based
on the specification
yt = 𝛽
′
t xt + 𝜀t
which is fit on subsamples ([1, k + 1], [1, k + 2], … , [1, T]), giving T −k least squares
estimates (̂𝛽k+1, … ,̂ 𝛽T). We can compute the standardized 1-step ahead recursive
residuals aŝ
𝜔t =
yt −̂ 𝛽
′
t−1xt
√
ft
ft =̂ 𝜎2
𝜀
[
1 + x
′
t
(X
′
tXt
)−1xt
]
The CUSUM statistic is defined as
St =
t∑
j=k+1̂
𝜔ĵ
𝜎𝜔̂
𝜎2
𝜔=
1
T −k
T
∑
t=k
(̂𝜔t −E[̂𝜔t])2
Under the null hypothesis that 𝛽is some constant value, H0 : 𝛽t = 𝛽, then St ∼
N[0, t −k −1]. One caveat of this procedure is that the starting point is chosen arbitrarily, and results may be inconsistent due to that.
--- page 278 ---

EXPLOSIVENESS TESTS
251
17.3.2
Chu-Stinchcombe-White CUSUM Test on Levels
This test follows Homm and Breitung [2012]. It simplifies the previous method by
dropping {xt}t=1,…,T, and assuming that H0 : 𝛽t = 0, that is, we forecast no change
(Et−1[Δyt] = 0). This will allow us to work directly with yt levels, hence reducing the
computational burden. We compute the standardized departure of log-price yt relative
to the log-price at yn, t > n, as
Sn,t = (yt −yn)(̂𝜎t
√
t −n)−1̂
𝜎2
t = (t −1)−1
t∑
i=2
(Δyi)2
Under the null hypothesis H0 : 𝛽t = 0, then Sn,t ∼N[0, 1]. The time-dependent
critical value for the one-sided test is
c𝛼[n, t] =
√
b𝛼+ log[t −n]
These authors derived via Monte Carlo that b0.05 = 4.6. One disadvantage of this
method is that the reference level yn is set somewhat arbitrarily. To overcome this
pitfall, we could estimate Sn,t on a series of backward-shifting windows n ∈[1, t],
and pick St = sup
n∈[1,t]
{Sn,t}.
17.4
EXPLOSIVENESS TESTS
Explosiveness tests can be generally divided between those that test for one bubble
and those that test for multiple bubbles. In this context, bubbles are not limited to price
rallies, but they also include sell-offs. Tests that allow for multiple bubbles are more
robust in the sense that a cycle of bubble-burst-bubble will make the series appear to
be stationary to single-bubble tests. Maddala and Kim [1998], and Breitung [2014]
offer good overviews of the literature.
17.4.1
Chow-Type Dickey-Fuller Test
A family of explosiveness tests was inspired by the work of Gregory Chow, starting
with Chow [1960]. Consider the first order autoregressive process
yt = 𝜌yt−1 + 𝜀t
where 𝜀t is white noise. The null hypothesis is that yt follows a random walk, H0:
𝜌= 1, and the alternative hypothesis is that yt starts as a random walk but changes at
time 𝜏∗T, where 𝜏∗∈(0, 1), into an explosive process:
H1 : yt =
{ yt−1 + 𝜀t for t = 1, … , 𝜏∗T
𝜌yt−1 + 𝜀t for t = 𝜏∗T + 1, … , T, with 𝜌> 1
--- page 279 ---

252
STRUCTURAL BREAKS
At time T we can test for a switch (from random walk to explosive process) having taken place at time 𝜏∗T (break date). In order to test this hypothesis, we fit the
following specification,
Δyt = 𝛿yt−1Dt[𝜏∗] + 𝜀t
where Dt[𝜏∗] is a dummy variable that takes zero value if t < 𝜏∗T, and takes the value
one if t ≥𝜏∗T. Then, the null hypothesis H0 : 𝛿= 0 is tested against the (one-sided)
alternative H1 : 𝛿> 1:
DFC𝜏∗=̂ 𝛿̂
𝜎𝛿
The main drawback of this method is that 𝜏∗is unknown. To address this issue,
Andrews [1993] proposed a new test where all possible 𝜏∗are tried, within some
interval 𝜏∗∈[𝜏0, 1 −𝜏0]. As Breitung [2014] explains, we should leave out some of
the possible 𝜏∗at the beginning and end of the sample, to ensure that either regime
is fitted with enough observations (there must be enough zeros and enough ones in
Dt[𝜏∗]). The test statistic for an unknown 𝜏∗is the maximum of all T(1 −2𝜏0) values
of DFC𝜏∗.
SDFC =
sup
𝜏∗∈[𝜏0,1−𝜏0]
{DFC𝜏∗}
Another drawback of Chow’s approach is that it assumes that there is only one
break date 𝜏∗T, and that the bubble runs up to the end of the sample (there is no
switch back to a random walk). For situations where three or more regimes (random
walk →bubble →random walk …) exist, we need to discuss the Supremum Augmented Dickey-Fuler (SADF) test.
17.4.2
Supremum Augmented Dickey-Fuller
In the words of Phillips, Wu and Yu [2011], “standard unit root and cointegration tests
are inappropriate tools for detecting bubble behavior because they cannot effectively
distinguish between a stationary process and a periodically collapsing bubble model.
Patterns of periodically collapsing bubbles in the data look more like data generated
from a unit root or stationary autoregression than a potentially explosive process.” To
address this flaw, these authors propose fitting the regression specification
Δyt = 𝛼+ 𝛽yt−1 +
L
∑
l=1
𝛾lΔyt−l + 𝜀t
where we test for H0 : 𝛽≤0, H1 : 𝛽> 0. Inspired by Andrews [1993], Phillips and
Yu [2011] and Phillips, Wu and Yu [2011] proposed the Supremum Augmented
--- page 280 ---

EXPLOSIVENESS TESTS
253
–2
2018
2016
2014
2012
2010
2008
2006
2004
0.75
1.00
1.25
1.50
1.75
Close price (after ETF trick)
SADF
2.00
2.25
2.50
0
2
4
6
FIGURE 17.1
Prices (left y-axis) and SADF (right y-axis) over time
Dickey-Fuller test (SADF). SADF fits the above regression at each end point t with
backwards expanding start points, then computes
SADFt =
sup
t0∈[1,t−𝜏]
{ADFt0,t} =
sup
t0∈[1,t−𝜏]
{̂ 𝛽t0,t̂
𝜎𝛽t0,t
}
wherê 𝛽t0,t is estimated on a sample that starts at t0 and ends at t, 𝜏is the minimum
sample length used in the analysis, t0 is the left bound of the backwards expanding
window, and t = 𝜏, … , T. For the estimation of SADFt, the right side of the window
is fixed at t. The standard ADF test is a special case of SADFt, where 𝜏= t −1.
There are two critical differences between SADFt and SDFC: First, SADFt is computed at each t ∈[𝜏, T], whereas SDFC is computed only at T. Second, instead of
introducing a dummy variable, SADF recursively expands the beginning of the sample (t0 ∈[1, t −𝜏]). By trying all combinations of a nested double loop on (t0, t),
SADF does not assume a known number of regime switches or break dates. Figure
17.1 displays the series of E-mini S&P 500 futures prices after applying the ETF trick
(Chapter 2, Section 2.4.1), as well as the SADF derived from that price series. The
SADF line spikes when prices exhibit a bubble-like behavior, and returns to low levels
when the bubble bursts. In the following sections, we will discuss some enhancements
to Phillips’ original SADF method.
17.4.2.1
Raw vs. Log Prices
It is common to find in the literature studies that carry out structural break tests on raw
prices. In this section we will explore why log prices should be preferred, particularly
when working with long time series involving bubbles and bursts.
--- page 281 ---

254
STRUCTURAL BREAKS
For raw prices {yt}, if ADF’s null hypotesis is rejected, it means that prices are
stationary, with finite variance. The implication is that returns
yt
yt−1 −1 are not time
invariant, for returns’ volatility must decrease as prices rise and increase as prices
fall in order to keep the price variance constant. When we run ADF on raw prices,
we assume that returns’ variance is not invariant to price levels. If returns variance
happens to be invariant to price levels, the model will be structurally heteroscedastic.
In contrast, if we work with log prices, the ADF specification will state that
Δlog[yt] ∝log[yt−1]
Let us make a change of variable, xt = kyt. Now, log[xt] = log[k] + log[yt], and
the ADF specification will state that
Δlog[xt] ∝log[xt−1] ∝log[yt−1]
Under this alternative specification based on log prices, price levels condition
returns’ mean, not returns’ volatility. The difference may not matter in practice for
small samples, where k ≈1, but SADF runs regressions across decades and bubbles
produce levels that are significantly different between regimes (k ≠1).
17.4.2.2
Computational Complexity
The algorithm runs in (n2), as the number of ADF tests that SADF requires for a
total sample length T is
T
∑
t=𝜏
t −𝜏+ 1 = 1
2(T −𝜏+ 2)(T −𝜏+ 1) =
(T −𝜏+ 2
2
)
Consider a matrix representation of the ADF specification, where X ∈ℝTxN and
y ∈ℝTx1. Solving a single ADF regression involves the floating point operations
(FLOPs) listed in Table 17.1.
This gives a total of f(N, T) = N3 + N2(2T + 3) + N(4T −1) + 2T + 2 FLOPs
per ADF estimate. A single SADF update requires g(N, T, 𝜏) = ∑T
t=𝜏f(N, t) + T −𝜏
FLOPs (T −𝜏operations to find the maximum ADF stat), and the estimation of a full
SADF series requires ∑T
t=𝜏g(N, T, 𝜏).
Consider a dollar bar series on E-mini S&P 500 futures. For (T, N) = (356631,3),
an ADF estimate requires 11,412,245 FLOPs, and a SADF update requires
2,034,979,648,799 operations (roughly 2.035 TFLOPs). A full SADF time series
requires 241,910,974,617,448,672 operations (roughly 242 PFLOPs). This number
will increase quickly, as the T continues to grow. And this estimate excludes notoriously expensive operations like alignment, pre-processing of data, I/O jobs, etc.
Needless to say, this algorithm’s double loop requires a large number of operations.
An HPC cluster running an efficiently parallelized implementation of the algorithm
may be needed to estimate the SADF series within a reasonable amount of time.
Chapter 20 will present some parallelization strategies useful in these situations.
--- page 282 ---

EXPLOSIVENESS TESTS
255
TABLE 17.1
FLOPs per ADF Estimate
Matrix Operation
FLOPs
o1 = X′y
(2T −1)N
o2 = X′X
(2T −1)N2
o3 = o−1
2
N3 + N2 + N
o4 = o3o1
2N2 −N
o5 = y −Xo4
T + (2N −1)T
o6 = o
′
5o5
2T −1
o7 = o3o6
1
T −N
2 + N2
o8 =
o4[0, 0]
√
o7[0, 0]
1
17.4.2.3
Conditions for Exponential Behavior
Consider the zero-lag specification on log prices, Δlog[yt] = 𝛼+ 𝛽log[yt−1] + 𝜀t.
This can be rewritten as log[̃yt] = (1 + 𝛽)log[̃yt−1] + 𝜀t, where log[̃yt] = log[yt] + 𝛼
𝛽.
Rolling back t discrete steps, we obtain E[log[̃yt]] = (1 + 𝛽)tlog[̃y0], or E[log[yt]] =
−𝛼
𝛽+ (1 + 𝛽)t(log[y0] + 𝛼
𝛽). The index t can be reset at a given time, to project the
future trajectory of y0 →yt after the next t steps. This reveals the conditions that
characterize the three states for this dynamic system:
r Steady: 𝛽< 0 ⇒limt→∞E[log[yt]] = −𝛼
𝛽.
◦The disequilibrium is log[yt] −(−𝛼
𝛽) = log[̃yt].
◦Then E[log[̃yt]]
log[̃y0]
= (1 + 𝛽)t = 1
2 at t = −log[2]
log[1+𝛽] (half-life).
r Unit-root: 𝛽= 0, where the system is non-stationary, and behaves as a martingale.
r Explosive: 𝛽> 0, where limt→∞E[log[yt]] =
{
−∞, if log [y0] < 𝛼
𝛽
+∞, if log [y0] > 𝛼
𝛽
.
17.4.2.4
Quantile ADF
SADF takes the supremum of a series on t-values, SADFt = supt0∈[1,t−𝜏]{ADFt0,t}.
Selecting the extreme value introduces some robustness problems, where SADF estimates could vary significantly depending on the sampling frequency and the specific
timestamps of the samples. A more robust estimator of ADF extrema would be the
following: First, let st = {ADFt0,t}t0∈[0,t1−𝜏]. Second, we define Qt,q = Q[st, q] the q
quantile of st, as a measure of centrality of high ADF values, where q ∈[0, 1]. Third,
we definė Qt,q,v = Qt,q+v −Qt,q−v, with 0 < v ≤min{q, 1 −q}, as a measure of dispersion of high ADF values. For example, we could set q = 0.95 and v = 0.025. Note
--- page 283 ---

256
STRUCTURAL BREAKS
that SADF is merely a particular case of QADF, where SADFt = Qt,1 anḋ Qt,q,v is not
defined because q = 1.
17.4.2.5
Conditional ADF
Alternatively, we can address concerns on SADF robustness by computing
conditional moments. Let f[x] be the probability distribution function of st =
{ADFt0,t}t0∈[1,t1−𝜏], with x ∈st. Then, we define Ct,q = K−1 ∫∞
Qt,q xf[x]dx as a measure of centrality of high ADF values, anḋ Ct,q =
√
K−1 ∫∞
Qt,q (x −Ct,q)2f[x]dx as
a measure of dispersion of high ADF values, with regularization constant K =
∫∞
Qt,q f[x]dx. For example, we could use q = 0.95.
By construction, Ct,q ≤SADFt. A scatter plot of SADFt against Ct,q shows that
lower boundary, as an ascending line with approximately unit gradient (see Figure
17.2). When SADF grows beyond −1.5, we can appreciate some horizontal trajectories, consistent with a sudden widening of the right fat tail in st. In other words,
(SADFt −Ct,q)∕̇Ct,q can reach significantly large values even if Ct,q is relatively
small, because SADFt is sensitive to outliers.
Figure 17.3(a) plots (SADFt −Ct,q)∕̇Ct,q for the E-mini S&P 500 futures prices
over time. Figure 17.3(b) is the scatter-plot of (SADFt −Ct,q)∕̇Ct,q against SADFt,
computed on the E-mini S&P 500 futures prices. It shows evidence that outliers in st
bias SADFt upwards.
–2
–2
–1
0
1
2
3
4
0
2
4
6
FIGURE 17.2
SADF (x-axis) vs CADF (y-axis)
--- page 284 ---

EXPLOSIVENESS TESTS
257
2
4
6
8
10
12
14
2001
2003
2005
2007
2009
2011
2013
2015
2017
Time
(a)
2
(b)
4
6
0
–2
2
4
6
8
10
12
14
FIGURE 17.3
(a) (SADFt −Ct,q)∕̇Ct,q over time (b) (SADFt −Ct,q)∕̇Ct,q (y-axis) as a function of
SADFt (x-axis)
--- page 285 ---

258
STRUCTURAL BREAKS
17.4.2.6
Implementation of SADF
This section presents an implementation of the SADF algorithm. The purpose of this
code is not to estimate SADF quickly, but to clarify the steps involved in its estimation. Snippet 17.1 lists SADF’s inner loop. That is the part that estimates SADFt =
sup
t0∈[1,t−𝜏]
{̂
𝛽t0,t̂
𝜎𝛽t0,t
}, which is the backshifting component of the algorithm. The outer
loop (not shown here) repeats this calculation for an advancing t, {SADFt}t=1,…,T.
The arguments are:
r logP: a pandas series containing log-prices
r minSL: the minimum sample length (𝜏), used by the final regression
r constant: the regression’s time trend component
◦'nc': no time trend, only a constant
◦'ct': a constant plus a linear time trend
◦'ctt': a constant plus a second-degree polynomial time trend
r lags: the number of lags used in the ADF specification
SNIPPET 17.1
SADF’S INNER LOOP
def get_bsadf(logP,minSL,constant,lags):
y,x=getYX(logP,constant=constant,lags=lags)
startPoints,bsadf,allADF=range(0,y.shape[0]+lags-minSL+1),None,[]
for start in startPoints:
y_,x_=y[start:],x[start:]
bMean_,bStd_=getBetas(y_,x_)
bMean_,bStd_=bMean_[0,0],bStd_[0,0]**.5
allADF.append(bMean_/bStd_)
if allADF[-1]>bsadf:bsadf=allADF[-1]
out={'Time':logP.index[-1],'gsadf':bsadf}
return out
Snippet 17.2 lists function getXY, which prepares the numpy objects needed to
conduct the recursive tests.
SNIPPET 17.2
PREPARING THE DATASETS
def getYX(series,constant,lags):
series_=series.diff().dropna()
x=lagDF(series_,lags).dropna()
x.iloc[:,0]=series.values[-x.shape[0]-1:-1,0] # lagged level
y=series_.iloc[-x.shape[0]:].values
--- page 286 ---

EXPLOSIVENESS TESTS
259
if constant!='nc':
x=np.append(x,np.ones((x.shape[0],1)),axis=1)
if constant[:2]=='ct':
trend=np.arange(x.shape[0]).reshape(-1,1)
x=np.append(x,trend,axis=1)
if constant=='ctt':
x=np.append(x,trend**2,axis=1)
return y,x
Snippet 17.3 lists function lagDF, which applies to a dataframe the lags specified
in its argument lags.
SNIPPET 17.3
APPLY LAGS TO DATAFRAME
def lagDF(df0,lags):
df1=pd.DataFrame()
if isinstance(lags,int):lags=range(lags+1)
else:lags=[int(lag) for lag in lags]
for lag in lags:
df_=df0.shift(lag).copy(deep=True)
df_.columns=[str(i)+'_'+str(lag) for i in df_.columns]
df1=df1.join(df_,how='outer')
return df1
Finally, Snippet 17.4 lists function getBetas, which carries out the actual
regressions.
SNIPPET 17.4
FITTING THE ADF SPECIFICATION
def getBetas(y,x):
xy=np.dot(x.T,y)
xx=np.dot(x.T,x)
xxinv=np.linalg.inv(xx)
bMean=np.dot(xxinv,xy)
err=y-np.dot(x,bMean)
bVar=np.dot(err.T,err)/(x.shape[0]-x.shape[1])*xxinv
return bMean,bVar
17.4.3
Suband Super-Martingale Tests
In this section we will introduce explosiveness tests that do not rely on the standard
ADF specification. Consider a process that is either a subor super-martingale. Given
