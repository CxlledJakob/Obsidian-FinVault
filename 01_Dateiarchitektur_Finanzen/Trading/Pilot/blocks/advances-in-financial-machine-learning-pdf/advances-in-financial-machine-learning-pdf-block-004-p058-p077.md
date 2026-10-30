# Advances in Financial Machine Learning.pdf — pages 58–77

--- page 58 ---

BARS
31
where the size of the expected imbalance is implied by |2v+ −E0[vt]|. When 𝜃T is
more imbalanced than expected, a low T will satisfy these conditions. This is the
information-based analogue of volume and dollar bars, and like its predecessors, it
addresses the same concerns regarding tick fragmentation and outliers. Furthermore,
it also addresses the issue of corporate actions, because the above procedure does
not rely on a constant bar size. Instead, the bar size is adjusted dynamically.
2.3.2.3
Tick Runs Bars
TIBs, VIBs, and DIBs monitor order flow imbalance, as measured in terms of ticks,
volumes, and dollar values exchanged. Large traders will sweep the order book, use
iceberg orders, or slice a parent order into multiple children, all of which leave a
trace of runs in the {bt}t=1,…,T sequence. For this reason, it can be useful to monitor
the sequence of buys in the overall volume, and take samples when that sequence
diverges from our expectations.
First, we define the length of the current run as
𝜃T = max
{
T
∑
t|bt=1
bt, −
T
∑
t|bt=−1
bt
}
Second, we compute the expected value of 𝜃T at the beginning of the bar
E0[𝜃T] = E0[T]max{P[bt = 1], 1 −P[bt = 1]}
In practice, we can estimate E0[T] as an exponentially weighted moving average of
T values from prior bars, and P[bt = 1] as an exponentially weighted moving average
of the proportion of buy ticks from prior bars.
Third, we define a tick runs bar (TRB) as a T∗-contiguous subset of ticks such that
the following condition is met:
T∗= arg min
T
{𝜃T ≥E0[T]max{P[bt = 1],1 −P[bt = 1]}}
where the expected count of ticks from runs is implied by max{P[bt = 1],
1 −P[bt = −1]}. When 𝜃T exhibits more runs than expected, a low T will satisfy
these conditions. Note that in this definition of runs we allow for sequence breaks.
That is, instead of measuring the length of the longest sequence, we count the number
of ticks of each side, without offsetting them (no imbalance). In the context of forming
bars, this turns out to be a more useful definition than measuring sequence lengths.
2.3.2.4
Volume/Dollar Runs Bars
Volume runs bars (VRBs) and dollar runs bars (DRBs) extend the above definition of
runs to volumes and dollars exchanged, respectively. The intuition is that we wish to
sample bars whenever the volumes or dollars traded by one side exceed our expectation for a bar. Following our customary nomenclature for the tick rule, we need to
determine the index T of the last observation in the bar.
--- page 59 ---

32
FINANCIAL DATA STRUCTURES
First, we define the volumes or dollars associated with a run as
𝜃T = max
⎧
⎪
⎨
⎪⎩
T
∑
t|bt=1
btvt, −
T
∑
t|bt=−1
btvt
⎫
⎪
⎬
⎪⎭
where vt may represent either number of securities traded (VRB) or dollar amount
exchanged (DRB). Your choice of vt is what determines whether you are sampling
according to the former or the latter.
Second, we compute the expected value of 𝜃T at the beginning of the bar,
E0[𝜃T] = E0[T]max{P[bt = 1]E0[vt|bt = 1], (1 −P[bt = 1])E0[vt|bt = −1]}
In practice, we can estimate E0[T] as an exponentially weighted moving average
of T values from prior bars, P[bt = 1] as an exponentially weighted moving average of the proportion of buy ticks from prior bars, E0[vt|bt = 1] as an exponentially
weighted moving average of the buy volumes from prior bars, and E0[vt|bt = −1] as
an exponentially weighted moving average of the sell volumes from prior bars.
Third, we define a volume runs bar (VRB) as a T∗-contiguous subset of ticks such
that the following condition is met:
T∗= arg min
T
{𝜃T ≥E0[T]max{P[bt = 1]E0[vt|bt = 1],
(1 −P[bt = 1])E0[vt|bt = −1]}}
where the expected volume from runs is implied by max{P[bt = 1]E0[vt|bt = 1],
(1 −P[bt = 1])E0[vt|bt = −1]}. When 𝜃T exhibits more runs than expected, or the
volume from runs is greater than expected, a low T will satisfy these conditions.
2.4
DEALING WITH MULTI-PRODUCT SERIES
Sometimes we are interested in modelling a time series of instruments, where the
weights need to be dynamically adjusted over time. Other times we must deal with
products that pay irregular coupons or dividends, or that are subject to corporate
actions. Events that alter the nature of the time series under study need to be treated
properly, or we will inadvertently introduce a structural break that will mislead our
research efforts (more on this in Chapter 17). This problem appears in many guises:
when we model spreads with changing weights, or baskets of securities where dividends/coupons must be reinvested, or baskets that must be rebalanced, or when an
index’s constituents are changed, or when we must replace an expired/matured contract/security with another, etc.
--- page 60 ---

DEALING WITH MULTI-PRODUCT SERIES
33
Futures are a case in point. In my experience, people struggle unnecessarily when
manipulating futures, mainly because they do not know how to handle the roll well.
The same can be said of strategies based on spreads of futures, or baskets of stocks or
bonds. In the next section, I’ll show you one way to model a basket of securities as if
it was a single cash product. I call it the “ETF trick” because the goal is to transform
any complex multi-product dataset into a single dataset that resembles a total-return
ETF. Why is this useful? Because your code can always assume that you only trade
cashlike products (non-expiring cash instruments), regardless of the complexity and
composition of the underlying series.
2.4.1
The ETF Trick
Suppose we wish to develop a strategy that trades a spread of futures. A few nuisances
arise from dealing with a spread rather than an outright instrument. First, the spread
is characterized by a vector of weights that changes over time. As a result, the spread
itself may converge even if prices do not change. When that happens, a model trading
that series will be misled to believe that PnL (the net mark-to-market value of profits
and losses) has resulted from that weight-induced convergence. Second, spreads can
acquire negative values, because they do not represent a price. This can often be
problematic, as most models assume positive prices. Third, trading times will not
align exactly for all constituents, so the spread is not always tradeable at the last
levels published, or with zero latency risk. Also, execution costs must be considered,
like crossing the bid-ask spread.
One way to avoid these issues is to produce a time series that reflects the value of $1
invested in a spread. Changes in the series will reflect changes in PnL, the series will
be strictly positive (at worst, infinitesimal), and the implementation shortfall will be
taken into account. This will be the series used to model, generate signals, and trade,
as if it were an ETF.
Suppose that we are given a history of bars, as derived from any of the methods
explained in Section 2.3. These bars contain the following columns:
r oi,t is the raw open price of instrument i = 1, … , I at bar t = 1, … , T.
r pi,t is the raw close price of instrument i = 1, … , I at bar t = 1, … , T.
r 𝜑i,t is the USD value of one point of instrument i = 1, … , I at bar t = 1, … , T.
This includes foreign exchange rate.
r vi,t is the volume of instrument i = 1, … , I at bar t = 1, … , T.
r di,t is the carry, dividend, or coupon paid by instrument i at bar t. This variable
can also be used to charge margin costs, or costs of funding.
where all instruments i = 1, … , I were tradeable at bar t = 1, … , T. In other words,
even if some instruments were not tradeable over the entirety of the time interval
[t −1, t], at least they were tradeable at times t −1 and t (markets were open and
able to execute orders at those instants). For a basket of futures characterized by an
--- page 61 ---

34
FINANCIAL DATA STRUCTURES
allocations vector 𝜔t rebalanced (or rolled) on bars B ⊆{1, … , T}, the $1 investment
value {Kt} is derived as
hi,t =
⎧
⎪
⎨
⎪⎩
𝜔i,tKt
oi,t+1𝜑i,t
∑I
i=1 ||𝜔i,t||
if t ∈B
hi,t−1
otherwise
𝛿i,t =
{
pi,t −oi,t
if (t −1) ∈B
Δpi,t
otherwise
Kt = Kt−1 +
I∑
i=1
hi,t−1𝜑i,t
(𝛿i,t + di,t
)
and K0 = 1 in the initial AUM. Variable hi,t represents the holdings (number of
securities or contracts) of instrument i at time t. Variable 𝛿i,t is the change of market value between t −1 and t for instrument i. Note that profits or losses are being
reinvested whenever t ∈B, hence preventing the negative prices. Dividends di,t are
already embedded in Kt, so there is no need for the strategy to know about them.
The purpose of 𝜔i,t
(∑I
i=1 |𝜔i,t|
)−1
in hi,t is to de-lever the allocations. For series of
futures, we may not know pi,t of the new contract at a roll time t, so we use oi,t+1 as
the closest in time.
Let 𝜏i be the transaction cost associated with trading $1 of instrument i, e.g., 𝜏i =
1E −4 (one basis point). There are three additional variables that the strategy needs
to know for every observed bar t:
1. Rebalance costs: The variable cost {ct} associated with the allocation rebalance is ct = ∑I
i=1(|hi,t−1|pi,t + |hi,t|oi,t+1)𝜑i,t𝜏i, ∀t ∈B. We do not embed ct in
Kt, or shorting the spread will generate fictitious profits when the allocation is
rebalanced. In your code, you can treat {ct} as a (negative) dividend.
2. Bid-ask spread: The cost {̃ct} of buying or selling one unit of this virtual ETF
is̃ ct = ∑I
i=1 |hi,t−1|pi,t𝜑i,t𝜏i. When a unit is bought or sold, the strategy must
charge this cost̃ ct, which is the equivalent to crossing the bid-ask spread of this
virtual ETF.
3. Volume: The volume traded {vt} is determined by the least active member in
the basket. Let vi,t be the volume traded by instrument i over bar t. The number
of tradeable basket units is vt = min
i
{
vi,t
|hi,t−1|
}
.
Transaction costs functions are not necessarily linear, and those non-linear costs
can be simulated by the strategy based on the above information. Thanks to the ETF
trick, we can model a basket of futures (or a single futures) as if it was a single nonexpiring cash product.
--- page 62 ---

DEALING WITH MULTI-PRODUCT SERIES
35
2.4.2
PCA Weights
The interested reader will find many practical ways of computing hedging weights
in L´opez de Prado and Leinweber [2012] and Bailey and L´opez de Prado [2012].
For the sake of completeness, let us review one way to derive the vector {𝜔t} used
in the previous section. Consider an IID multivariate Gaussian process characterized
by a vector of means 𝜇, of size Nx1, and a covariance matrix V, of size NxN. This
stochastic process describes an invariant random variable, like the returns of stocks,
the changes in yield of bonds, or changes in options’ volatilities, for a portfolio of N
instruments. We would like to compute the vector of allocations 𝜔that conforms to
a particular distribution of risks across V’s principal components.
First, we perform a spectral decomposition, VW = WΛ, where the columns in W
are reordered so that the elements of Λ’s diagonal are sorted in descending order.
Second, given a vector of allocations 𝜔, we can compute the portfolio’s risk as 𝜎2 =
𝜔′V𝜔= 𝜔′WΛW′𝜔= 𝛽′Λ𝛽= (Λ
1∕2𝛽)′(Λ
1∕2𝛽), where 𝛽represents the projection of
𝜔on the orthogonal basis. Third, Λ is a diagonal matrix, thus 𝜎2 = ∑N
n=1 𝛽2
nΛn,n,
and the risk attributed to the nth component is Rn = 𝛽2
nΛn,n𝜎−2 = [W′𝜔]2
nΛn,n𝜎−2,
with R′1N = 1, and 1N is a vector of N ones. You can interpret {Rn}n=1,…,N as the
distribution of risks across the orthogonal components.
Fourth, we would like to compute the vector 𝜔that delivers a user-defined risk distribution R. From earlier steps, 𝛽=
{
𝜎
√
Rn
Λn,n
}
n=1,…,N
, which represents the allocation in the new (orthogonal) basis. Fifth, the allocation in the old basis is given by
𝜔= W𝛽. Re-scaling 𝜔merely re-scales 𝜎, hence keeping the risk distribution constant. Figure 2.2 illustrates the contribution to risk per principal component for an
FIGURE 2.2
Contribution to risk per principal component
--- page 63 ---

36
FINANCIAL DATA STRUCTURES
inverse variance allocation. Almost all principal components contribute risk, including those with highest variance (components 1 and 2). In contrast, for the PCA portfolio, only the component with lowest variance contributes risk.
Snippet 2.1 implements this method, where the user-defined risk distribution
R is passed through argument riskDist (optional None). If riskDist is None,
the code will assume all risk must be allocated to the principal component with
smallest eigenvalue, and the weights will be the last eigenvector re-scaled to match
𝜎(riskTarget).
SNIPPET 2.1
PCA WEIGHTS FROM A RISK DISTRIBUTION R
def pcaWeights(cov,riskDist=None,riskTarget=1.):
# Following the riskAlloc distribution, match riskTarget
eVal,eVec=np.linalg.eigh(cov) # must be Hermitian
indices=eVal.argsort()[::-1] # arguments for sorting eVal desc
eVal,eVec=eVal[indices],eVec[:,indices]
if riskDist is None:
riskDist=np.zeros(cov.shape[0])
riskDist[-1]=1.
loads=riskTarget*(riskDist/eVal)**.5
wghts=np.dot(eVec,np.reshape(loads,(-1,1)))
#ctr=(loads/riskTarget)**2*eVal # verify riskDist
return wghts
2.4.3
Single Future Roll
The ETF trick can handle the rolls of a single futures contract, as a particular case of a
1-legged spread. However, when dealing with a single futures contract, an equivalent
and more direct approach is to form a time series of cumulative roll gaps, and detract
that gaps series from the price series. Snippet 2.2 shows a possible implementation
of this logic, using a series of tick bars downloaded from Bloomberg and stored in a
HDF5 table. The meaning of the Bloomberg fields is as follows:
r FUT_CUR_GEN_TICKER: It identifies the contract associated with that price. Its
value changes with every roll.
r PX_OPEN: The open price associated with that bar.
r PX_LAST: The close price associated with the bar.
r VWAP: The volume-weighted average price associated with that bar.
The argument matchEnd in function rollGaps determines whether the
futures series should be rolled forward (matchEnd=False) or backward
(matchEnd=True). In a forward roll, the price at the start of the rolled series
--- page 64 ---

DEALING WITH MULTI-PRODUCT SERIES
37
matches the price at the start of the raw series. In a backward roll, the price at the
end of the rolled series matches the price at the end of the raw series.
SNIPPET 2.2
FORM A GAPS SERIES, DETRACT IT FROM PRICES
def getRolledSeries(pathIn,key):
series=pd.read_hdf(pathIn,key='bars/ES_10k')
series['Time']=pd.to_datetime(series['Time'],format='%Y%m%d%H%M%S%f')
series=series.set_index('Time')
gaps=rollGaps(series)
for ﬂd in ['Close','VWAP']:series[ﬂd]-=gaps
return series
#———————————————————————————————————————————
def rollGaps(series,dictio={'Instrument':'FUT_CUR_GEN_TICKER','Open':'PX_OPEN', \
'Close':'PX_LAST'},matchEnd=True):
# Compute gaps at each roll, between previous close and next open
rollDates=series[dictio['Instrument']].drop_duplicates(keep='ﬁrst').index
gaps=series[dictio['Close']]*0
iloc=list(series.index)
iloc=[iloc.index(i)-1 for i in rollDates] # index of days prior to roll
gaps.loc[rollDates[1:]]=series[dictio['Open']].loc[rollDates[1:]]- \
series[dictio['Close']].iloc[iloc[1:]].values
gaps=gaps.cumsum()
if matchEnd:gaps-=gaps.iloc[-1] # roll backward
return gaps
Rolled prices are used for simulating PnL and portfolio mark-to-market values.
However, raw prices should still be used to size positions and determine capital consumption. Keep in mind, rolled prices can indeed become negative, particularly in
futures contracts that sold off while in contango. To see this, run Snippet 2.2 on a
series of Cotton #2 futures or Natural Gas futures.
In general, we wish to work with non-negative rolled series, in which case we
can derive the price series of a $1 investment as follows: (1) Compute a time series
of rolled futures prices, (2) compute the return (r) as rolled price change divided
by the previous raw price, and (3) form a price series using those returns (i.e.,
(1+r).cumprod()). Snippet 2.3 illustrates this logic.
SNIPPET 2.3
NON-NEGATIVE ROLLED PRICE SERIES
raw=pd.read_csv(ﬁlePath,index_col=0,parse_dates=True)
gaps=rollGaps(raw,dictio={'Instrument':'Symbol','Open':'Open','Close':'Close'})
rolled=raw.copy(deep=True)
for ﬂd in ['Open','Close']:rolled[ﬂd]-=gaps
rolled['Returns']=rolled['Close'].diff()/raw['Close'].shift(1)
rolled['rPrices']=(1+rolled['Returns']).cumprod()
--- page 65 ---

38
FINANCIAL DATA STRUCTURES
2.5
SAMPLING FEATURES
So far we have learned how to produce a continuous, homogeneous, and structured
dataset from a collection of unstructured financial data. Although you could attempt to
apply an ML algorithm on such a dataset, in general that would not be a good idea, for
a couple of reasons. First, several ML algorithms do not scale well with sample size
(e.g., SVMs). Second, ML algorithms achieve highest accuracy when they attempt to
learn from relevant examples. Suppose that you wish to predict whether the next 5%
absolute return will be positive (a 5% rally) or negative (a 5% sell-off). At any random
time, the accuracy of such a prediction will be low. However, if we ask a classifier to
predict the sign of the next 5% absolute return after certain catalytic conditions, we
are more likely to find informative features that will help us achieve a more accurate
prediction. In this section we discuss ways of sampling bars to produce a features
matrix with relevant training examples.
2.5.1
Sampling for Reduction
As we have mentioned earlier, one reason for sampling features from a structured
dataset is to reduce the amount of data used to fit the ML algorithm. This operation
is also referred to as downsampling. This is often done by either sequential sampling
at a constant step size (linspace sampling), or by sampling randomly using a uniform
distribution (uniform sampling).
The main advantage of linspace sampling is its simplicity. The disadvantages are
that the step size is arbitrary, and that outcomes may vary depending on the seed bar.
Uniform sampling addresses these concerns by drawing samples uniformly across the
entire set of bars. Still, both methods suffer the criticism that the sample does not necessarily contain the subset of most relevant observations in terms of their predictive
power or informational content.
2.5.2
Event-Based Sampling
Portfolio managers typically place a bet after some event takes place, such as a structural break (Chapter 17), an extracted signal (Chapter 18), or microstructural phenomena (Chapter 19). These events could be associated with the release of some macroeconomic statistics, a spike in volatility, a significant departure in a spread away from
its equilibrium level, etc. We can characterize an event as significant, and let the ML
algorithm learn whether there is an accurate prediction function under those circumstances. Perhaps the answer is no, in which case we would redefine what constitutes
an event, or try again with alternative features. For illustration purposes, let us discuss
one useful event-based sampling method.
2.5.2.1
The CUSUM Filter
The CUSUM filter is a quality-control method, designed to detect a shift in
the mean value of a measured quantity away from a target value. Consider IID
--- page 66 ---

SAMPLING FEATURES
39
observations {yt}t=1,…,T arising from a locally stationary process. We define the
cumulative sums
St = max {0, St−1 + yt −Et−1
[yt
]}
with boundary condition S0 = 0. This procedure would recommend an action at the
first t satisfying St ≥h, for some threshold h (the filter size). Note that St = 0 whenever yt ≤Et−1[yt] −St−1. This zero floor means that we will skip some downward
deviations that otherwise would make St negative. The reason is, the filter is set up to
identify a sequence of upside divergences from any reset level zero. In particular, the
threshold is activated when
St ≥h ⇔∃𝜏∈[1, t]
||||||
t∑
i=𝜏
(yi −Ei−1
[yt
]) ≥h
This concept of run-ups can be extended to include run-downs, giving us a symmetric CUSUM filter:
S+
t = max {0, S+
t−1 + yt −Et−1
[yt
]} , S+
0 = 0
S−
t = min {0, S−
t−1 + yt −Et−1
[yt
]} , S−
0 = 0
St = max {S+
t , −S−
t
}
Lam and Yam [1997] propose an investment strategy whereby alternating buy-sell
signals are generated when an absolute return h is observed relative to a prior high
or low. Those authors demonstrate that such strategy is equivalent to the so-called
“filter trading strategy” studied by Fama and Blume [1966]. Our use of the CUSUM
filter is different: We will sample a bar t if and only if St ≥h, at which point St is
reset. Snippet 2.4 shows an implementation of the symmetric CUSUM filter, where
Et−1[yt] = yt−1.
SNIPPET 2.4
THE SYMMETRIC CUSUM FILTER
def getTEvents(gRaw,h):
tEvents,sPos,sNeg=[],0,0
diff=gRaw.diff()
for i in diff.index[1:]:
sPos,sNeg=max(0,sPos+diff.loc[i]),min(0,sNeg+diff.loc[i])
if sNeg<-h:
sNeg=0;tEvents.append(i)
elif sPos>h:
sPos=0;tEvents.append(i)
return pd.DatetimeIndex(tEvents)
--- page 67 ---

40
FINANCIAL DATA STRUCTURES
FIGURE 2.3
CUSUM sampling of a price series
The function getTEvents receives two arguments: the raw time series we wish
to filter (gRaw) and the threshold, h. One practical aspect that makes CUSUM filters
appealing is that multiple events are not triggered by gRaw hovering around a threshold level, which is a flaw suffered by popular market signals such as Bollinger bands.
It will require a full run of length h for gRaw to trigger an event. Figure 2.3 illustrates
the samples taken by a CUSUM filter on a price series.
Variable St could be based on any of the features we will discuss in Chapters 17–
19, like structural break statistics, entropy, or market microstructure measurements.
For example, we could declare an event whenever SADF departs sufficiently from a
previous reset level (to be defined in Chapter 17). Once we have obtained this subset
of event-driven bars, we will let the ML algorithm determine whether the occurrence
of such events constitutes actionable intelligence.
EXERCISES
2.1 On a series of E-mini S&P 500 futures tick data:
(a) Form tick, volume, and dollar bars. Use the ETF trick to deal with the roll.
(b) Count the number of bars produced by tick, volume, and dollar bars on a
weekly basis. Plot a time series of that bar count. What bar type produces
the most stable weekly count? Why?
(c) Compute the serial correlation of returns for the three bar types. What bar
method has the lowest serial correlation?
--- page 68 ---

REFERENCES
41
(d) Partition the bar series into monthly subsets. Compute the variance of returns
for every subset of every bar type. Compute the variance of those variances.
What method exhibits the smallest variance of variances?
(e) Apply the Jarque-Bera normality test on returns from the three bar types.
What method achieves the lowest test statistic?
2.2 On a series of E-mini S&P 500 futures tick data, compute dollar bars
and dollar imbalance bars. What bar type exhibits greater serial correlation?
Why?
2.3 On dollar bar series of E-mini S&P 500 futures and Eurostoxx 50 futures:
(a) Apply Section 2.4.2 to compute the {̂𝜔t} vector used by the ETF trick. (Hint:
You will need FX values for EUR/USD at the roll dates.)
(b) Derive the time series of the S&P 500/Eurostoxx 50 spread.
(c) Confirm that the series is stationary, with an ADF test.
2.4 Form E-mini S&P 500 futures dollar bars:
(a) Compute Bollinger bands of width 5% around a rolling moving average.
Count how many times prices cross the bands out (from within the bands
to outside the bands).
(b) Now sample those bars using a CUSUM filter, where {yt} are returns and
h = 0.05. How many samples do you get?
(c) Compute the rolling standard deviation of the two-sampled series. Which
one is least heteroscedastic? What is the reason for these results?
2.5 Using the bars from exercise 4:
(a) Sample bars using the CUSUM filter, where {yt} are absolute returns and
h = 0.05.
(b) Compute the rolling standard deviation of the sampled bars.
(c) Compare this result with the results from exercise 4. What procedure delivered the least heteroscedastic sample? Why?
REFERENCES
An´e, T. and H. Geman (2000): “Order flow, transaction clock and normality of asset returns.” Journal
of Finance, Vol. 55, pp. 2259–2284.
Bailey, David H., and M. L´opez de Prado (2012): “Balanced baskets: A new approach to trading
and hedging risks.” Journal of Investment Strategies (Risk Journals), Vol. 1, No. 4 (Fall), pp.
21–62.
Clark, P. K. (1973): “A subordinated stochastic process model with finite variance for speculative
prices.” Econometrica, Vol. 41, pp. 135–155.
Easley, D., M. L´opez de Prado, and M. O’Hara (2011): “The volume clock: Insights into the high
frequency paradigm.” Journal of Portfolio Management, Vol. 37, No. 2, pp. 118–128.
Easley, D., M. L´opez de Prado, and M. O’Hara (2012): “Flow toxicity and liquidity in a high frequency world.” Review of Financial Studies, Vol. 25, No. 5, pp. 1457–1493.
Fama, E. and M. Blume (1966): “Filter rules and stock market trading.” Journal of Business, Vol.
40, pp. 226–241.
--- page 69 ---

42
FINANCIAL DATA STRUCTURES
Kolanovic, M. and R. Krishnamachari (2017): “Big data and AI strategies: Machine learning and
alternative data approach to investing.” White paper, JP Morgan, Quantitative and Derivatives
Strategy. May 18.
Lam, K. and H. Yam (1997): “CUSUM techniques for technical trading in financial markets.” Financial Engineering and the Japanese Markets, Vol. 4, pp. 257–274.
L´opez de Prado, M. and D. Leinweber (2012): “Advances in cointegration and subset correlation
hedging methods.” Journal of Investment Strategies (Risk Journals), Vol. 1, No. 2 (Spring), pp.
67–115.
Mandelbrot, B. and M. Taylor (1967): “On the distribution of stock price differences.” Operations
Research, Vol. 15, No. 5, pp. 1057–1062.
--- page 70 ---

CHAPTER 3
Labeling
3.1
MOTIVATION
In Chapter 2 we discussed how to produce a matrix X of financial features out of an
unstructured dataset. Unsupervised learning algorithms can learn the patterns from
that matrix X, for example whether it contains hierarchical clusters. On the other hand,
supervised learning algorithms require that the rows in X are associated with an array
of labels or values y, so that those labels or values can be predicted on unseen features
samples. In this chapter we will discuss ways to label financial data.
3.2
THE FIXED-TIME HORIZON METHOD
As it relates to finance, virtually all ML papers label observations using the fixed-time
horizon method. This method can be described as follows. Consider a features matrix
X with I rows, {Xi}i=1,…,I, drawn from some bars with index t = 1, …, T, where I ≤T.
Chapter 2, Section 2.5 discussed sampling methods that produce the set of features
{Xi}i=1,…,I. An observation Xi is assigned a label yi ∈{−1, 0, 1},
yi =
⎧
⎪
⎨
⎪⎩
−1
if rti,0,ti,0+h < −𝜏
0
if |rti,0,ti,0+h| ≤𝜏
1
if rti,0,ti,0+h > 𝜏
where 𝜏is a pre-defined constant threshold, ti,0 is the index of the bar immediately
after Xi takes place, ti,0 + h is the index of the h-th bar after ti,0, and rti,0,ti,0+h is the
price return over a bar horizon h,
rti,0,ti,0+h =
pti,0+h
pti,0
−1
43
--- page 71 ---

44
LABELING
Because the literature almost always works with time bars, h implies a fixed-time
horizon. The bibliography section lists multiple ML studies, of which Dixon et al.
[2016] is a recent example of this labeling method. Despite its popularity, there are
several reasons to avoid this approach in most cases. First, as we saw in Chapter
2, time bars do not exhibit good statistical properties. Second, the same threshold
𝜏is applied regardless of the observed volatility. Suppose that 𝜏= 1E −2, where
sometimes we label an observation as yi = 1 subject to a realized bar volatility of
𝜎ti,0 = 1E −4 (e.g., during the night session), and sometimes 𝜎ti,0 = 1E −2 (e.g.,
around the open). The large majority of labels will be 0, even if return rti,0,ti,0+h was
predictable and statistically significant.
In other words, it is a very common error to label observations according to a
fixed threshold on time bars. Here are a couple of better alternatives. First, label per
a varying threshold 𝜎ti,0, estimated using a rolling exponentially weighted standard
deviation of returns. Second, use volume or dollar bars, as their volatilities are much
closer to constant (homoscedasticity). But even these two improvements miss a key
flaw of the fixed-time horizon method: the path followed by prices. Every investment
strategy has stop-loss limits, whether they are self-imposed by the portfolio manager,
enforced by the risk department, or triggered by a margin call. It is simply unrealistic
to build a strategy that profits from positions that would have been stopped-out by the
exchange. That virtually no publication accounts for that when labeling observations
tells you something about the current state of the investment literature.
3.3
COMPUTING DYNAMIC THRESHOLDS
As argued in the previous section, in practice we want to set profit taking and stoploss limits that are a function of the risks involved in a bet. Otherwise, sometimes we
will be aiming too high (𝜏≫𝜎ti,0), and sometimes too low (𝜏≪𝜎ti,0), considering
the prevailing volatility.
Snippet 3.1 computes the daily volatility at intraday estimation points, applying a
span of span0 days to an exponentially weighted moving standard deviation. See the
pandas documentation for details on the pandas.Series.ewm function.
SNIPPET 3.1
DAILY VOLATILITY ESTIMATES
def getDailyVol(close,span0=100):
# daily vol, reindexed to close
df0=close.index.searchsorted(close.index-pd.Timedelta(days=1))
df0=df0[df0>0]
df0=pd.Series(close.index[df0–1], index=close.index[close.shape[0]-df0.shape[0]:])
df0=close.loc[df0.index]/close.loc[df0.values].values-1 # daily returns
df0=df0.ewm(span=span0).std()
return df0
We can use the output of this function to set default profit taking and stop-loss
limits throughout the rest of this chapter.
--- page 72 ---

THE TRIPLE-BARRIER METHOD
45
3.4
THE TRIPLE-BARRIER METHOD
Here I will introduce an alternative labeling method that I have not found in the literature. If you are an investment professional, I think you will agree that it makes more
sense. I call it the triple-barrier method because it labels an observation according to
the first barrier touched out of three barriers. First, we set two horizontal barriers and
one vertical barrier. The two horizontal barriers are defined by profit-taking and stoploss limits, which are a dynamic function of estimated volatility (whether realized
or implied). The third barrier is defined in terms of number of bars elapsed since the
position was taken (an expiration limit). If the upper barrier is touched first, we label
the observation as a 1. If the lower barrier is touched first, we label the observation
as a −1. If the vertical barrier is touched first, we have two choices: the sign of the
return, or a 0. I personally prefer the former as a matter of realizing a profit or loss
within limits, but you should explore whether a 0 works better in your particular
problems.
You may have noticed that the triple-barrier method is path-dependent. In order to
label an observation, we must take into account the entire path spanning [ti,0, ti,0 + h],
where h defines the vertical barrier (the expiration limit). We will denote ti,1 the time
of the first barrier touch, and the return associated with the observed feature is rti,0,ti,1.
For the sake of clarity, ti,1 ≤ti,0 + h and the horizontal barriers are not necessarily
symmetric.
Snippet 3.2 implements the triple-barrier method. The function receives four
arguments:
r close: A pandas series of prices.
r events: A pandas dataframe, with columns,
◦t1: The timestamp of vertical barrier. When the value is np.nan, there will
not be a vertical barrier.
◦trgt: The unit width of the horizontal barriers.
r ptSl: A list of two non-negative float values:
◦ptSl[0]: The factor that multiplies trgt to set the width of the upper barrier.
If 0, there will not be an upper barrier.
◦ptSl[1]: The factor that multiplies trgt to set the width of the lower barrier.
If 0, there will not be a lower barrier.
r molecule: A list with the subset of event indices that will be processed by a
single thread. Its use will become clear later on in the chapter.
SNIPPET 3.2
TRIPLE-BARRIER LABELING METHOD
def applyPtSlOnT1(close,events,ptSl,molecule):
# apply stop loss/profit taking, if it takes place before t1 (end of event)
events_=events.loc[molecule]
out=events_[['t1']].copy(deep=True)
--- page 73 ---

46
LABELING
if ptSl[0]>0:pt=ptSl[0]*events_['trgt']
else:pt=pd.Series(index=events.index) # NaNs
if ptSl[1]>0:sl=-ptSl[1]*events_['trgt']
else:sl=pd.Series(index=events.index) # NaNs
for loc,t1 in events_['t1'].ﬁllna(close.index[-1]).iteritems():
df0=close[loc:t1] # path prices
df0=(df0/close[loc]-1)*events_.at[loc,'side'] # path returns
out.loc[loc,'sl']=df0[df0<sl[loc]].index.min() # earliest stop loss.
out.loc[loc,'pt']=df0[df0>pt[loc]].index.min() # earliest profit taking.
return out
The output from this function is a pandas dataframe containing the timestamps (if
any) at which each barrier was touched. As you can see from the previous description,
the method considers the possibility that each of the three barriers may be disabled.
Let us denote a barrier configuration by the triplet [pt,sl,t1], where a 0 means
that the barrier is inactive and a 1 means that the barrier is active. The possible eight
configurations are:
r Three useful configurations:
◦[1,1,1]: This is the standard setup, where we define three barrier exit conditions. We would like to realize a profit, but we have a maximum tolerance for
losses and a holding period.
◦[0,1,1]: In this setup, we would like to exit after a number of bars, unless we
are stopped-out.
◦[1,1,0]: Here we would like to take a profit as long as we are not stopped-out.
This is somewhat unrealistic in that we are willing to hold the position for as
long as it takes.
r Three less realistic configurations:
◦[0,0,1]: This is equivalent to the fixed-time horizon method. It may still be
useful when applied to volume-, dollar-, or information-driven bars, and multiple forecasts are updated within the horizon.
◦[1,0,1]: A position is held until a profit is made or the maximum holding
period is exceeded, without regard for the intermediate unrealized losses.
◦[1,0,0]: A position is held until a profit is made. It could mean being locked
on a losing position for years.
r Two illogical configurations:
◦[0,1,0]: This is an aimless configuration, where we hold a position until we
are stopped-out.
◦[0,0,0]: There are no barriers. The position is locked forever, and no label is
generated.
Figure 3.1 shows two alternative configurations of the triple-barrier method. On
the left, the configuration is [1,1,0], where the first barrier touched is the lower
horizontal one. On the right, the configuration is [1,1,1], where the first barrier
touched is the vertical one.
--- page 74 ---

THE TRIPLE-BARRIER METHOD
47
(a)
(b)
FIGURE 3.1
Two alternative configurations of the triple-barrier method
--- page 75 ---

48
LABELING
3.5
LEARNING SIDE AND SIZE
In this section we will discuss how to label examples so that an ML algorithm can
learn both the side and the size of a bet. We are interested in learning the side of a
bet when we do not have an underlying model to set the sign of our position (long
or short). Under such circumstance, we cannot differentiate between a profit-taking
barrier and a stop-loss barrier, since that requires knowledge of the side. Learning the
side implies that either there are no horizontal barriers or that the horizontal barriers
must be symmetric.
Snippet 3.3 implements the function getEvents, which finds the time of the first
barrier touch. The function receives the following arguments:
r close: A pandas series of prices.
r tEvents: The pandas timeindex containing the timestamps that will seed every
triple barrier. These are the timestamps selected by the sampling procedures
discussed in Chapter 2, Section 2.5.
r ptSl: A non-negative float that sets the width of the two barriers. A 0 value
means that the respective horizontal barrier (profit taking and/or stop loss) will
be disabled.
r t1: A pandas series with the timestamps of the vertical barriers. We pass a
False when we want to disable vertical barriers.
r trgt: A pandas series of targets, expressed in terms of absolute returns.
r minRet: The minimum target return required for running a triple barrier search.
r numThreads: The number of threads concurrently used by the function.
SNIPPET 3.3
GETTING THE TIME OF FIRST TOUCH
def getEvents(close,tEvents,ptSl,trgt,minRet,numThreads,t1=False):
#1) get target
trgt=trgt.loc[tEvents]
trgt=trgt[trgt>minRet] # minRet
#2) get t1 (max holding period)
if t1 is False:t1=pd.Series(pd.NaT,index=tEvents)
#3) form events object, apply stop loss on t1
side_=pd.Series(1.,index=trgt.index)
events=pd.concat({'t1':t1,'trgt':trgt,'side':side_}, \
axis=1).dropna(subset=['trgt'])
df0=mpPandasObj(func=applyPtSlOnT1,pdObj=('molecule',events.index), \
numThreads=numThreads,close=close,events=events,ptSl=[ptSl,ptSl])
events['t1']=df0.dropna(how='all').min(axis=1) # pd.min ignores nan
events=events.drop('side',axis=1)
return events
Suppose that I = 1E6 and h = 1E3, then the number of conditions to evaluate
is up to one billion on a single instrument. Many ML tasks are computationally
--- page 76 ---

LEARNING SIDE AND SIZE
49
expensive unless you are familiar with multi-threading, and this is one of them. Here
is where parallel computing comes into play. Chapter 20 discusses a few multiprocessing functions that we will use throughout the book.
Function mpPandasObj calls a multiprocessing engine, which is explained in
depth in Chapter 20. For the moment, you simply need to know that this function will
execute applyPtSlOnT1 in parallel. Function applyPtSlOnT1 returns the timestamps at which each barrier is touched (if any). Then, the time of the first touch is
the earliest time among the three returned by applyPtSlOnT1. Because we must
learn the side of the bet, we have passed ptSl= [ptSl,ptSl] as argument, and we
arbitrarily set the side to be always long (the horizontal barriers are symmetric, so
the side is irrelevant to determining the time of the first touch). The output from this
function is a pandas dataframe with columns:
r t1: The timestamp at which the first barrier is touched.
r trgt: The target that was used to generate the horizontal barriers.
Snippet 3.4 shows one way to define a vertical barrier. For each index in tEvents,
it finds the timestamp of the next price bar at or immediately after a number
of days numDays. This vertical barrier can be passed as optional argument t1
in getEvents.
SNIPPET 3.4
ADDING A VERTICAL BARRIER
t1=close.index.searchsorted(tEvents+pd.Timedelta(days=numDays))
t1=t1[t1<close.shape[0]]
t1=pd.Series(close.index[t1],index=tEvents[:t1.shape[0]]) # NaNs at end
Finally, we can label the observations using the getBins function defined in Snippet 3.5. The arguments are the events dataframe we just discussed, and the close
pandas series of prices. The output is a dataframe with columns:
r ret: The return realized at the time of the first touched barrier.
r bin: The label, {−1, 0, 1}, as a function of the sign of the outcome. The function
can be easily adjusted to label as 0 those events when the vertical barrier was
touched first, which we leave as an exercise.
SNIPPET 3.5
LABELING FOR SIDE AND SIZE
def getBins(events,close):
#1) prices aligned with events
events_=events.dropna(subset=['t1'])
px=events_.index.union(events_['t1'].values).drop_duplicates()
px=close.reindex(px,method='bﬁll')
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
