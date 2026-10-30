# Advances in Financial Machine Learning.pdf — pages 343–362

--- page 343 ---

316
MULTIPROCESSING AND VECTORIZATION
allows us to implement it in a seamless way. Function getPCs receives̃ W through
the argument eVec. The argument molecules contains a subset of the file names in
ﬁleNames, where each file represents Zb. The key concept to grasp is that we compute
the dot product of a Zb with the slice of the rows of̃ Wb defined by the columns in Zb,
and that molecular results are aggregated on the fly (redux= pd.DataFrame.add).
SNIPPET 20.14
PRINCIPAL COMPONENTS FOR A SUBSET OF THE
COLUMNS
pcs=mpJobList(getPCs,('molecules',ﬁleNames),numThreads=24,mpBatches=1,
path=path,eVec=eVec,redux=pd.DataFrame.add)
#——————————————————————————————————————
def getPCs(path,molecules,eVec):
# get principal components by loading one file at a time
pcs=None
for i in molecules:
df0=pd.read_csv(path+i,index_col=0,parse_dates=True)
if pcs is None:pcs=np.dot(df0.values,eVec.loc[df0.columns].values)
else:pcs+=np.dot(df0.values,eVec.loc[df0.columns].values)
pcs=pd.DataFrame(pcs,index=df0.index,columns=eVec.columns)
return pcs
This approach presents two advantages: First, because getPCs loads dataframes
Zb sequentially, for a sufficiently large B, the RAM is not exhausted. Second, mpJob-
List executes the molecules in parallel, hence speeding up the calculations.
In real life ML applications, we often encounter datasets where Z contains billions
of datapoints. As this example demonstrates, parallelization is not only beneficial in
terms of reducing run time. Many problems could not be solved without parallelization, as a matter of memory limitations, even if we were willing to wait longer.
EXERCISES
20.1 Run Snippets 20.1 and 20.2 with timeit. Repeat 10 batches of 100 executions.
What is the minimum elapsed time for each snippet?
20.2 The instructions in Snippet 20.2 are very useful for unit testing, brute force
searches, and scenario analysis. Can you remember where else in the book have
you seen them? Where else could they have been used?
20.3 Adjust Snippet 20.4 to form molecules using a two-nested loops scheme, rather
than a linear scheme.
20.4 Compare with timeit:
(a) Snippet 20.4, by repeating 10 batches of 100 executions. What is the minimum elapsed time for each snippet?
--- page 344 ---

BIBLIOGRAPHY
317
(b) Modify Snippet 20.4 (from exercise 3), by repeating 10 batches of 100 executions. What is the minimum elapsed time for each snippet?
20.5 Simplify Snippet 20.4 by using mpPandasObj.
20.6 Modify mpPandasObj to handle the possibility of forming molecules using a
two-nested loops scheme with an upper triangular structure.
REFERENCE
Ascher, D., A. Ravenscroft, and A. Martelli (2005): Python Cookbook, 2nd ed. O’Reilly Media.
BIBLIOGRAPHY
Gorelick, M. and I. Ozsvald (2008): High Performance Python, 1st ed. O’Reilly Media.
L´opez de Prado, M. (2017): “Supercomputing for finance: A gentle introduction.” Lecture materials,
Cornell University. Available at https://ssrn.com/abstract=2907803.
McKinney, W. (2012): Python for Data Analysis, 1st ed. O’Reilly Media.
Palach, J. (2008): Parallel Programming with Python, 1st ed. Packt Publishing.
Summerfield, M. (2013): Python in Practice: Create Better Programs Using Concurrency, Libraries,
and Patterns, 1st ed. Addison-Wesley.
Zaccone, G. (2015): Python Parallel Programming Cookbook, 1st ed. Packt Publishing.
--- page 345 ---
--- page 346 ---

CHAPTER 21
Brute Force and Quantum Computers
21.1
MOTIVATION
Discrete mathematics appears naturally in multiple ML problems, including hierarchical clustering, grid searches, decisions based on thresholds, and integer optimization. Sometimes, these problems do not have a known analytical (closed-form)
solution, or even a heuristic to approximate it, and our only hope is to search for it
through brute force. In this chapter, we will study how a financial problem, intractable
to modern supercomputers, can be reformulated as an integer optimization problem.
Such a representation makes it amenable to quantum computers. From this example
the reader can infer how to translate his particular financial ML intractable problem
into a quantum brute force search.
21.2
COMBINATORIAL OPTIMIZATION
Combinatorial optimization problems can be described as problems where there is a
finite number of feasible solutions, which result from combining the discrete values
of a finite number of variables. As the number of feasible combinations grows, an
exhaustive search becomes impractical. The traveling salesman problem is an example of a combinatorial optimization problem that is known to be NP hard (Woeginger
[2003]), that is, the category of problems that are at least as hard as the hardest problems solvable is nondeterministic polynomial time.
What makes an exhaustive search impractical is that standard computers evaluate
and store the feasible solutions sequentially. But what if we could evaluate and store
all feasible solutions at once? That is the goal of quantum computers. Whereas the
bits of a standard computer can only adopt one of two possible states ({0, 1}) at once,
quantum computers rely on qubits, which are memory elements that may hold a linear
superposition of both states. In theory, quantum computers can accomplish this thanks
319
--- page 347 ---

320
BRUTE FORCE AND QUANTUM COMPUTERS
to quantum mechanical phenomena. In some implementations, qubits can support
currents flowing in two directions at once, hence providing the desired superposition.
This linear superposition property is what makes quantum computers ideally suited
for solving NP-hard combinatorial optimization problems. See Williams [2010] for
a general treatise on the capabilities of quantum computers.
The best way to understand this approach is through a particular example. We
will now see how a dynamic portfolio optimization problem subject to generic transaction cost functions can be represented as a combinatorial optimization problem,
tractable to quantum computers. Unlike Garleanu and Pedersen [2012], we will not
assume that the returns are drawn from an IID Gaussian distribution. This problem
is particularly relevant to large asset managers, as the costs from excessive turnover
and implementation shortfall may critically erode the profitability of their investment
strategies.
21.3
THE OBJECTIVE FUNCTION
Consider a set on assets X = {xi}, i = 1, … , N, with returns following a multivariate Normal distribution at each time horizon h = 1, … , H, with varying mean and
variance. We will assume that the returns are multivariate Normal, time-independent,
however not identically distributed through time. We define a trading trajectory as
an NxH matrix 𝜔that determines the proportion of capital allocated to each of the N
assets over each of the H horizons. At a particular horizon h = 1, … , H, we have a
forecasted mean 𝜇h, a forecasted variance Vh and a forecasted transaction cost function 𝜏h [𝜔]. This means that, given a trading trajectory 𝜔, we can compute a vector of
expected investment returns r, as
r = diag[𝜇′𝜔] −𝜏[𝜔]
where 𝜏[𝜔] can adopt any functional form. Without loss of generality, consider the
following:
r 𝜏1 [𝜔] = ∑N
n=1 cn,1
√
||𝜔n,1 −𝜔∗
n||
r 𝜏h [𝜔] = ∑N
n=1 cn,h
√
||𝜔n,h −𝜔n,h−1||, for h = 2, … , H
r 𝜔∗
n is the initial allocation to instrument n, n = 1, … , N
𝜏[𝜔] is an Hx1 vector of transaction costs. In words, the transaction costs associated with each asset are the sum of the square roots of the changes in capital allocations, re-scaled by an asset-specific factor Ch = {cn,h}n=1,…,N that changes with
h. Thus, Ch is an Nx1 vector that determines the relative transaction cost across
assets.
--- page 348 ---

AN INTEGER OPTIMIZATION APPROACH
321
The Sharpe Ratio (Chapter 14) associated with r can be computed as (𝜇h being net
of the risk-free rate)
SR [r] =
∑H
h=1 𝜇
′
h𝜔h −𝜏h [𝜔]
√∑H
h=1 𝜔
′
hVh𝜔h
21.4
THE PROBLEM
We would like to compute the optimal trading trajectory that solves the problem
max
𝜔
SR [r]
s.t. :
N
∑
i=1
|𝜔i,h| = 1, ∀h = 1, … , H
This problem attempts to compute a global dynamic optimum, in contrast to the
static optimum derived by mean-variance optimizers (see Chapter 16). Note that noncontinuous transaction costs are embedded in r. Compared to standard portfolio optimization applications, this is not a convex (quadratic) programming problem for at
least three reasons: (1) Returns are not identically distributed, because 𝜇h and Vh
change with h. (2) Transaction costs 𝜏h [𝜔] are non-continuous and changing with h.
(3) The objective function SR [r] is not convex. Next, we will show how to calculate solutions without making use of any analytical property of the objective function
(hence the generalized nature of this approach).
21.5
AN INTEGER OPTIMIZATION APPROACH
The generality of this problem makes it intractable to standard convex optimization
techniques. Our solution strategy is to discretize it so that it becomes amenable to
integer optimization. This in turn allows us to use quantum computing technology to
find the optimal solution.
21.5.1
Pigeonhole Partitions
Suppose that we count the number of ways that K units of capital can be allocated
among N assets, where we assume K > N. This is equivalent to finding the number
of non-negative integer solutions to x1 + … + xN = K, which has the nice combinatorial solution
(
K + N −1
N −1
)
. This bears a similarity to the classic integer partitioning
problem in number theory for which Hardy and Ramanujan (and later, Rademacher)
proved an asymptotic expression (see Johansson [2012]). While order does not matter in the partition problem, order is very relevant to the problem we have at hand.
--- page 349 ---

322
BRUTE FORCE AND QUANTUM COMPUTERS
Asset 1
Asset 2
Asset 3
Asset 1
Asset 2
Asset 3
Units of capital
Units of capital
FIGURE 21.1
Partitions (1, 2, 3) and (3, 2, 1) must be treated as different
For example, if K = 6 and N = 3, partitions (1, 2, 3) and (3, 2, 1) must be treated as
different (obviously (2, 2, 2) does not need to be permutated). Figure 21.1 illustrates
how order is important when allocating 6 units of capital to 3 different assets. This
means that we must consider all distinct permutations of each partition. Even though
there is a nice combinatorial solution to find the number of such allocations, it may
still be computationally intensive to find as K and N grow large. However, we can use
Stirling’s approximation to easily arrive at an estimate.
Snippet 21.1 provides an efficient algorithm to generate the set of all partitions, pK,N = {{pi}i=1,…,N|pi ∈𝕎, ∑N
i=1 pi = K}, where 𝕎are the natural numbers
including zero (whole numbers).
SNIPPET 21.1
PARTITIONS OF k OBJECTS INTO n SLOTS
from itertools import combinations_with_replacement
#———————————————————————————————————————
def pigeonHole(k,n):
# Pigeonhole problem (organize k objects in n slots)
for j in combinations_with_replacement(xrange(n),k):
r=[0]*n
for i in j:
r[i]+=1
yield r
--- page 350 ---

AN INTEGER OPTIMIZATION APPROACH
323
21.5.2
Feasible Static Solutions
We would like to compute the set of all feasible solutions at any given horizon h, which we denote Ω. Consider a partition set of K units into N assets,
pK,N. For each partition {pi}i=1,…,N ∈pK,N, we can define a vector of absolute weights such that |𝜔i| = 1
K pi, where ∑N
i=1 |𝜔i| = 1 (the full-investment constraint). This full-investment (without leverage) constraint implies that every weight
can be either positive or negative, so for every vector of absolute weights
{|𝜔i|}i=1,…,N we can generate 2N vectors of (signed) weights. This is accomplished by multiplying the items in {|𝜔i|}i=1,…,N with the items of the Cartesian product of {−1, 1} with N repetitions. Snippet 21.2 shows how to generate the set Ω of all vectors of weights associated with all partitions, Ω =
{{ sj
K pi
}|||{sj}j=1,…,N ∈{−1, 1}x … x{−1, 1}
⏟⏞⏞⏞⏞⏞⏞⏞⏞⏞⏞⏞⏞⏟⏞⏞⏞⏞⏞⏞⏞⏞⏞⏞⏞⏞⏟
N
,{pi}i=1,…,N ∈pK,N}
.
SNIPPET 21.2
SET 𝛀OF ALL VECTORS ASSOCIATED WITH
ALL PARTITIONS
import numpy as np
from itertools import product
#———————————————————————————————————————
def getAllWeights(k,n):
#1) Generate partitions
parts,w=pigeonHole(k,n),None
#2) Go through partitions
for part_ in parts:
w_=np.array(part_)/ﬂoat(k) # abs(weight) vector
for prod_ in product([-1,1],repeat=n): # add sign
w_signed_=(w_*prod_).reshape(-1,1)
if w is None:w=w_signed_.copy()
else:w=np.append(w,w_signed_,axis=1)
return w
21.5.3
Evaluating Trajectories
Given the set of all vectors Ω, we define the set of all possible trajectories Φ as the
Cartesian product of Ω with H repetitions. Then, for every trajectory we can evaluate its transaction costs and SR, and select the trajectory with optimal performance
across Φ. Snippet 21.3 implements this functionality. The object params is a list of
dictionaries that contain the values of C, 𝜇, V.
--- page 351 ---

324
BRUTE FORCE AND QUANTUM COMPUTERS
SNIPPET 21.3
EVALUATING ALL TRAJECTORIES
import numpy as np
from itertools import product
#———————————————————————————————————————
def evalTCosts(w,params):
# Compute t-costs of a particular trajectory
tcost=np.zeros(w.shape[1])
w_=np.zeros(shape=w.shape[0])
for i in range(tcost.shape[0]):
c_=params[i]['c']
tcost[i]=(c_*abs(w[:,i]-w_)**.5).sum()
w_=w[:,i].copy()
return tcost
#———————————————————————————————————————
def evalSR(params,w,tcost):
# Evaluate SR over multiple horizons
mean,cov=0,0
for h in range(w.shape[1]):
params_=params[h]
mean+=np.dot(w[:,h].T,params_['mean'])[0]-tcost[h]
cov+=np.dot(w[:,h].T,np.dot(params_['cov'],w[:,h]))
sr=mean/cov**.5
return sr
#———————————————————————————————————————
def dynOptPort(params,k=None):
# Dynamic optimal portfolio
#1) Generate partitions
if k is None:k=params[0]['mean'].shape[0]
n=params[0]['mean'].shape[0]
w_all,sr=getAllWeights(k,n),None
#2) Generate trajectories as cartesian products
for prod_ in product(w_all.T,repeat=len(params)):
w_=np.array(prod_).T # concatenate product into a trajectory
tcost_=evalTCosts(w_,params)
sr_=evalSR(params,w_,tcost_) # evaluate trajectory
if sr is None or sr<sr_: # store trajectory if better
sr,w=sr_,w_.copy()
return w
Note that this procedure selects an globally optimal trajectory without relying on
convex optimization. A solution will be found even if the covariance matrices are
ill-conditioned, transaction cost functions are non-continuous, etc. The price we pay
for this generality is that calculating the solution is extremely computationally intensive. Indeed, evaluating all trajectories is similar to the traveling-salesman problem.
--- page 352 ---

A NUMERICAL EXAMPLE
325
Digital computers are inadequate for this sort of NP-complete or NP-hard problems;
however, quantum computers have the advantage of evaluating multiple solutions at
once, thanks to the property of linear superposition.
The approach presented in this chapter set the foundation for Rosenberg et
al. [2016], which solved the optimal trading trajectory problem using a quantum
annealer. The same logic can be applied to a wide range on financial problems
involving path dependency, such as a trading trajectory. Intractable ML algorithm
can be discretized and translated into a brute force search, intended for a quantum
computer.
21.6
A NUMERICAL EXAMPLE
Below we illustrate how the global optimum can be found in practice, using a digital
computer. A quantum computer would evaluate all trajectories at once, whereas the
digital computer does this sequentially.
21.6.1
Random Matrices
Snippet 21.4 returns a random matrix of Gaussian values with known rank, which
is useful in many applications (see exercises). You may want to consider this code
the next time you want to execute multivariate Monte Carlo experiments, or scenario
analyses.
SNIPPET 21.4
PRODUCE A RANDOM MATRIX OF A GIVEN RANK
import numpy as np
#———————————————————————————————————————
def rndMatWithRank(nSamples,nCols,rank,sigma=0,homNoise=True):
# Produce random matrix X with given rank
rng=np.random.RandomState()
U,_,_=np.linalg.svd(rng.randn(nCols,nCols))
x=np.dot(rng.randn(nSamples,rank),U[:,:rank].T)
if homNoise:
x+=sigma*rng.randn(nSamples,nCols) # Adding homoscedastic noise
else:
sigmas=sigma*(rng.rand(nCols)+.5) # Adding heteroscedastic noise
x+=rng.randn(nSamples,nCols)*sigmas
return x
Snippet 21.5 generates H vectors of means, covariance matrices, and transaction
cost factors, C, 𝜇, V. These variables are stored in a params list.
--- page 353 ---

326
BRUTE FORCE AND QUANTUM COMPUTERS
SNIPPET 21.5
GENERATE THE PROBLEM’S PARAMETERS
import numpy as np
#———————————————————————————————————————
def genMean(size):
# Generate a random vector of means
rMean=np.random.normal(size=(size,1))
return rMean
#———————————————————————————————————————
#1) Parameters
size,horizon=3,2
params=[]
for h in range(horizon):
x=rndMatWithRank(1000,3,3,0.)
mean_,cov_=genMean(size),np.cov(x,rowvar=False)
c_=np.random.uniform(size=cov_.shape[0])*np.diag(cov_)**.5
params.append({'mean':mean_,'cov':cov_,'c':c_})
21.6.2
Static Solution
Snippet 21.6 computes the performance of the trajectory that results from local (static)
optima.
SNIPPET 21.6
COMPUTE AND EVALUATE THE STATIC SOLUTION
import numpy as np
#———————————————————————————————————————
def statOptPortf(cov,a):
# Static optimal porftolio
# Solution to the "unconstrained" portfolio optimization problem
cov_inv=np.linalg.inv(cov)
w=np.dot(cov_inv,a)
w/=np.dot(np.dot(a.T,cov_inv),a) # np.dot(w.T,a)==1
w/=abs(w).sum() # re-scale for full investment
return w
#———————————————————————————————————————
#2) Static optimal portfolios
w_stat=None
for params_ in params:
w_=statOptPortf(cov=params_['cov'],a=params_['mean'])
if w_stat is None:w_stat=w_.copy()
else:w_stat=np.append(w_stat,w_,axis=1)
tcost_stat=evalTCosts(w_stat,params)
sr_stat=evalSR(params,w_stat,tcost_stat)
print 'static SR:',sr_stat
--- page 354 ---

EXERCISES
327
21.6.3
Dynamic Solution
Snippet 21.7 computes the performance associated with the globally dynamic optimal
trajectory, applying the functions explained throughout the chapter.
SNIPPET 21.7
COMPUTE AND EVALUATE THE
DYNAMIC SOLUTION
import numpy as np
#———————————————————————————————————————
#3) Dynamic optimal portfolios
w_dyn=dynOptPort(params)
tcost_dyn=evalTCosts(w_dyn,params)
sr_dyn=evalSR(params,w_dyn,tcost_dyn)
print 'dynamic SR:',sr_dyn
EXERCISES
21.1 Using the pigeonhole argument, prove that ∑N
n=1
(
N
n
)
= 2N −1.
21.2 Use Snippet 21.4 to produce random matrices of size (1000, 10), sigma= 1 and
(a) rank= 1. Plot the eigenvalues of the covariance matrix.
(b) rank= 5. Plot the eigenvalues of the covariance matrix.
(c) rank= 10. Plot the eigenvalues of the covariance matrix.
(d) What pattern do you observe? How would you connect it to Markowitz’s
curse (Chapter 16)?
21.3 Run the numerical example in Section 21.6:
(a) Use size= 3, and compute the running time with timeit. Repeat 10
batches of 100 executions. How long did it take?
(b) Use size= 4, and timeit. Repeat 10 batches of 100 executions. How long
did it take?
21.4 Review all snippets in this chapter.
(a) How many could be vectorized?
(b) How many could be parallelized, using the techniques from Chapter 20?
(c) If you optimize the code, by how much do you think you could speed it up?
(d) Using the optimized code, what is the problem dimensionality that could
be solved within a year?
21.5 Under what circumstances would the globally dynamic optimal trajectory match
the sequence of local optima?
(a) Is that a realistic set of assumptions?
(b) If not,
--- page 355 ---

328
BRUTE FORCE AND QUANTUM COMPUTERS
(i) could that explain why na¨ıve solutions beat Markowitz’s (Chapter 16)?
(ii) why do you think so many firms spend so much effort in computing
sequences of local optima?
REFERENCES
Garleanu, N. and L. Pedersen (2012): “Dynamic trading with predictable returns and transaction
costs.” Journal of Finance, Vol. 68, No. 6, pp. 2309–2340.
Johansson, F. (2012): “Efficient implementation of the Hardy-Ramanujan-Rademacher formula,”
LMS Journal of Computation and Mathematics, Vol. 15, pp. 341–359.
Rosenberg, G., P. Haghnegahdar, P. Goddard, P. Carr, K. Wu, and M. L´opez de Prado (2016): “Solving the optimal trading trajectory problem using a quantum annealer.” IEEE Journal of Selected
Topics in Signal Processing, Vol. 10, No. 6 (September), pp. 1053–1060.
Williams, C. (2010): Explorations in Quantum Computing, 2nd ed. Springer.
Woeginger, G. (2003): “Exact algorithms for NP-hard problems: A survey.” In Junger, M., G.
Reinelt, and G. Rinaldi: Combinatorial Optimization—Eureka, You Shrink! Lecture notes in
computer science, Vol. 2570, Springer, pp. 185–207.
--- page 356 ---

CHAPTER 22
High-Performance Computational
Intelligence and Forecasting
Technologies
Kesheng Wu and Horst D. Simon
22.1
MOTIVATION
This chapter provides an introduction to the Computational Intelligence and Forecasting Technologies (CIFT) project at Lawrence Berkeley National Laboratory (LBNL).
The main objective of CIFT is to promote the use of high-performance computing
(HPC) tools and techniques for analysis of streaming data. After noticing the data
volume being given as the explanation for the five-month delay for SEC and CFTC
to issue their report on the 2010 Flash Crash, LBNL started the CIFT project to apply
HPC technologies to manage and analyze financial data. Making timely decisions
with streaming data is a requirement for many business applications, such as avoiding impending failure in the electric power grid or a liquidity crisis in financial markets. In all these cases, the HPC tools are well suited in handling the complex data
dependencies and providing a timely solution. Over the years, CIFT has worked on
a number of different forms of streaming data, including those from vehicle traffic,
electric power grid, electricity usage, and so on. The following sections explain the
key features of HPC systems, introduce a few special tools used on these systems,
and provide examples of streaming data analyses using these HPC tools.
22.2
REGULATORY RESPONSE TO THE FLASH CRASH OF 2010
On May 6, 2010, at about 2:45 p.m. (U.S. Eastern Daylight Time), the U.S. stock
market experienced a nearly 10% drop in the Dow Jones Industrial Average, only to
recover most of the loss a few minutes later. It took about five months for regulatory
329
--- page 357 ---

330
HIGH-PERFORMANCE COMPUTATIONAL INTELLIGENCE
agencies to come up with an investigation report. In front of a congressional panel
investigating the crash, the data volume (~20 terabytes) was given as the primary reason for the long delay. Since HPC systems, such as those at National Energy Research
Scientific Computing (NERSC) center,1 routinely work with hundreds of terabytes
in minutes, we should have no problem processing the data from financial markets.
This led to the establishment of the CIFT project with the mission to apply the HPC
techniques and tools for financial data analysis.
A key aspect of financial big data is that it consists of mostly time series. Over the
years, the CIFT team, along with numerous collaborators, has developed techniques
to analyze many different forms of data streams and time series. This chapter provides
a brief introduction to the HPC system including both hardware (Section 22.4) and
software (Section 22.5), and recounts a few successful use cases (Section 22.6). We
conclude with a summary of our vision and work so far and also provide contact
information for interested readers.
22.3
BACKGROUND
Advances in computing technology have made it considerably easier to look for complex patterns. This pattern-finding capability is behind a number of recent scientific
breakthroughs, such as the discovery of the Higgs particle (Aad et al. [2016]) and
gravitational waves (Abbot et al. [2016]). This same capability is also at the core
of many internet companies, for example, to match users with advertisers (Zeff and
Aronson [1999], Yen et al. [2009]). However, the hardware and software used in science and in commerce are quite different. The HPC tools have some critical advantages that should be useful in a variety of business applications.
Tools for scientists are typically built around high-performance computing (HPC)
platforms, while the tools for commercial applications are built around cloud computing platforms. For the purpose of sifting through large volumes of data to find useful
patterns, the two approaches have been shown to work well. However, the marquee
application for HPC systems is large-scale simulation, such as weather models used
for forecasting regional storms in the next few days (Asanovic et al. [2006]). In contrast, the commercial cloud was initially motivated by the need to process a large
number of independent data objects concurrently (data parallel tasks).
For our work, we are primarily interested in analyses of streaming data. In particular, high-speed complex data streams, such as those from sensor networks monitoring
our nation’s electric power grid and highway systems. This streaming workload is not
ideal for either HPC systems or cloud systems as we discuss below, but we believe
that the HPC ecosystem has more to offer to address the streaming data analysis than
the cloud ecosystem does.
Cloud systems were originally designed for parallel data tasks, where a large number of independent data objects can be processed concurrently. The system is thus
1 NERSC is a National User Facility funded by U.S. Department of Energy, located at LBNL. More information about NERSC can be found at http://nersc.gov/.
--- page 358 ---

HPC HARDWARE
331
designed for high throughput, not for producing real-time responses. However, many
business applications require real-time or near-real-time responses. For example, an
instability event in an electric power grid could develop and grow into a disaster in
minutes; finding the tell-tale signature quickly enough would avert the disaster. Similarly, signs of emerging illiquidity events have been identified in the financial research
literature; quickly finding these signs during the active market trading hours could
offer options to prevent shocks to the market and avoid flash crashes. The ability to
prioritize quick turnaround time is essential in these cases.
A data stream is by definition available progressively; therefore, there may not be a
large number of data objects to be processed in parallel. Typically, only a fixed amount
of the most recent data records are available for analysis. In this case, an effective way
to harness the computing power of many central processing units (CPUs) cores is to
divide the analytical work on a single data object (or a single time-step) to many CPU
cores. The HPC ecosystem has more advanced tools for this kind of work than the
cloud ecosystem does.
These are the main points that motivated our work. For a more thorough comparison of HPC systems and cloud systems, we refer interested readers to Asanovic
et al. [2006]. In particular, Fox et al. [2015] have created an extensive taxonomy for
describing the similarities and differences for any application scenario.
In short, we believe the HPC community has a lot to offer to advance the state-ofthe-art for streaming analytics. The CIFT project was established with a mission to
transfer LBNL’s HPC expertise to streaming business applications. We are pursuing
this mission via collaboration, demonstration, and tool development.
To evaluate the potential uses of HPC technology, we have spent time working
with various applications. This process not only exposes our HPC experts to a variety
of fields, but also makes it possible for us to gather financial support to establish a
demonstration facility.
With the generous gifts from a number of early supporters of this effort, we established a substantial computing cluster dedicated to this work. This dedicated computer (named dirac1) allows users to utilize an HPC system and evaluate their applications for themselves.
We are also engaged in a tool development effort to make HPC systems more
usable for streaming data analysis. In the following sections, we will describe the
hardware and software of the dedicated CIFT machine, as well as some of the demonstration and tool development efforts. Highlights include improving the data handling
speed by 21-fold, and increasing the speed of computing an early warning indicator
by 720-fold.
22.4
HPC HARDWARE
Legend has it that the first generation of big data systems was built with the spare
computer components gleaned from a university campus. This is likely an urban
legend, but it underscores an important point about the difference between HPC
systems and cloud systems. Theoretically, a HPC system is built with custom
--- page 359 ---

332
HIGH-PERFORMANCE COMPUTATIONAL INTELLIGENCE
QDR Infiniband
+ 100 Gbps to ANI
File Servers (8) (/home) 160TB
Gateway Nodes (16)
ESNet
10Gb/s
QDR InfiniBand
Aggregation Switch
Router
ANI
100 Gb/s
Mgt Nodes (12)
Compute Servers
504 Nodes at ANL
720 Nodes at NErsc
   Intel Nehalem
   8 cores/node
Active Storage
Servers
FLASH/SSD Storage
Big Memory
Servers
1 TD of Memory per node
15 at ANL / 2 at NERSC
GPU Servers
266 Nvidia cards at ANL
FIGURE 22.1
Schematic of the Magellan cluster (circa 2010), an example of HPC computer cluster
high-cost components, while cloud systems are built with standard low-cost commodity components. In practice, since the worldwide investment in HPC systems
is much smaller than that of personal computers, there is no way for manufacturers
to produce custom components just for the HPC market. The truth is that HPC
systems are largely assembled from commodity components just like cloud systems.
However, due to their different target applications, there are some differences in
their choices of the components.
Let us describe the computing elements, storage system, and networking system in
turn. Figure 22.1 is a high-level schematic diagram representing the key components
of the Magellan cluster around year 2010 (Jackson et al. [2010]; Yelick et al. [2011]).
The computer elements include both CPUs and graphics processing units (GPUs).
These CPUs and GPUs are commercial products in almost all the cases. For example,
the nodes on dirac1 use a 24-core 2.2Ghz Intel processor, which is common to cloud
computing systems. Currently, dirac1 does not contain GPUs.
The networking system consists of two parts: the InfiniBand network connecting
the components within the cluster, and the switched network connection to the outside world. In this particular example, the outside connections are labeled “ESNet”
and “ANI.” The InfiniBand network switches are also common in cloud computing
systems.
The storage system in Figure 1 includes both rotating disks and flash storage.
This combination is also common. What is different is that a HPC system typically
has its storage system concentrated outside of the computer nodes, while a typical
cloud computing system has its storage system distributed among the compute
nodes. These two approaches have their own advantages and disadvantages. For
example, the concentrated storage is typically exported as a global file system to all
computer nodes, which makes it easier to deal with data stored in files. However, this
requires a highly capable network connecting the CPUs and the disks. In contrast,
--- page 360 ---

HPC HARDWARE
333
the distributed approach could use lower-capacity network because there is some
storage that is close to each CPU. Typically, a distributed file system, such as the
Google file system (Ghemawat, Gobioff, and Leung [2003]), is layered on top of a
cloud computing system to make the storage accessible to all CPUs.
In short, the current generation of HPC systems and cloud systems use pretty much
the same commercial hardware components. Their differences are primarily in the
arrangement of the storage systems and networking systems. Clearly, the difference
in the storage system designs could affect the application performance. However,
the virtualization layer of the cloud systems is likely the bigger cause of application
performance difference. In the next section, we will discuss another factor that could
have an even larger impact, namely software tools and libraries.
Virtualization is generally used in the cloud computing environment to make the
same hardware available to multiple users and to insulate one software environment
from another. This is one of the more prominent features distinguishing the cloud
computing environment from the HPC environment. In most cases, all three basic
components of a computer system—CPU, storage, and networking—are all virtualized. This virtualization has many benefits. For example, an existing application can
run on a CPU chip without recompiling; many users can share the same hardware;
hardware faults could be corrected through the virtualization software; and applications on a failed compute node could be more easily migrated to another node.
However, this virtualization layer also imposes some runtime overhead and could
reduce application performance. For time-sensitive applications, this reduction in performance could become a critical issue.
Tests show that the performance differences could be quite large. Next, we briefly
describe a performance study reported by Jackson et al [2010]. Figure 22.2 shows the
performance slowdown using different computer systems. The names below the horizontal axis are different software packages commonly used at NERSC. The left bar
corresponds to the Commercial Cloud, the middle bar to Magellan, and the (sometimes missing) right bar to the EC2-Beta-Opt system. The non-optimized commercial
FIGURE 22.2
The cloud ran scientific applications considerably slower than on HPC systems (circa
2010)
--- page 361 ---

334
HIGH-PERFORMANCE COMPUTATIONAL INTELLIGENCE
IB
14
12
10
8
6
4
2
0
32
64
128
256
Performance
512
1024
Commercial Cloud
10G - TCPoEth
10G - TCPoEth Vm
FIGURE 22.3
As the number of cores increases (horizontal axis), the virtualization overhead becomes
much more significant (circa 2010)
cloud instances run these software packages 2 to 10 times slower than on a NERSC
supercomputer. Even on the more expensive high-performance instances, there are
noticeable slowdowns.
Figure 22.3 shows a study of the main factor causing the slowdown with the software package PARATEC. In Figure 2, we see that PARATEC took 53 times longer
to complete on the commercial cloud than on an HPC system. We observe from Figure 3 that, as the number of cores (horizontal axis) increases, the differences among
the measured performances (measured in TFLOP/s) become larger. In particular, the
line labeled “10G- TCPoEth Vm” barely increases as the number of cores grows. This
is the case where the network instance is using virtualized networking (TCP over Ethernet). It clearly shows that the networking virtualization overhead is significant, to
the point of rendering the cloud useless.
The issue of virtualization overhead is widely recognized (Chen et al. [2015]).
There has been considerable research aimed at addressing both the I/O virtualization
overhead (Gordon et al. [2012]) as well as the networking virtualization overhead
(Dong et al. [2012]). As these state-of-the-art techniques are gradually being moved
into commercial products, we anticipate the overhead will decrease in the future, but
some overhead will inevitably remain.
To wrap up this section, we briefly touch on the economics of HPC versus cloud.
Typically, HPC systems are run by nonprofit research organizations and universities, while cloud systems are provided by commercial companies. Profit, customer
retention, and many other factors affect the cost of a cloud system (Armburst et al.
[2010]). In 2011, the Magellan project report stated that “Cost analysis shows that
DOE centers are cost competitive, typically 3–7 × less expensive, when compared to
commercial cloud providers” (Yelick et al. [2010]).
A group of high-energy physicists thought their use case was well-suited for
cloud computing and conducted a detailed study of a comparison study (Holzman
et al. [2017]). Their cost comparisons still show the commercial cloud offerings as
--- page 362 ---

HPC SOFTWARE
335
approximately 50% more expensive than dedicated HPC systems for comparable
computing tasks; however, the authors worked with severe limitations on data
ingress and egress to avoid potentially hefty charges on data movement. For complex
workloads, such as the streaming data analyses discussed in this book, we anticipate
that this HPC cost advantage will remain in the future. A 2016 National Academy of
Sciences study came to the same conclusion that even a long-term lease from Amazon is likely 2 to 3 times more expensive than HPC systems to handle the expected
science workload from NSF (Box 6.2 from National Academies of Sciences, [2016]).
22.5
HPC SOFTWARE
Ironically, the real power of a supercomputer is in its specialized software. There are a
wide variety of software packages available for both HPC systems and cloud systems.
In most cases, the same software package is available on both platforms. Therefore,
we chose to focus on software packages that are unique to HPC systems and have the
potential to improve computational intelligence and forecasting technologies.
One noticeable feature of the HPC software ecosystem is that much of the application software performs its own interprocessor communication through Message
Passing Interface (MPI). In fact, the cornerstone of most scientific computing books
is MPI (Kumar et al. [1994], Gropp, Lusk, and Skjellum [1999]). Accordingly, our
discussion of HPC software tools will start with MPI. As this book relies on data processing algorithms, we will concentrate on data management tools (Shoshami and
Rotem [2010]).
22.5.1
Message Passing Interface
Message Passing Interface is a communication protocol for parallel computing
(Gropp, Lusk, and Skjellum [1999], Snir et al. [1988]). It defines a number of pointto-point data exchange operations as well as some collective communication operations. The MPI standard was established based on several early attempts to build
portable communication libraries. The early implementation from Argonne National
Lab, named MPICH, was high performance, scalable, and portable. This helped MPI
to gain wide acceptance among scientific users.
The success of MPI is partly due to its separation of Language Independent Specifications (LIS) from its language bindings. This allows the same core function to
be provided to many different programming languages, which also contributes to
its acceptance. The first MPI standard specified ANSI C and Fortran-77 bindings
together with the LIS. The draft specification was presented to the user community
at the 1994 Supercomputing Conference.
Another key factor contributing to MPI’s success is the open-source license used
by MPICH. This license allows the vendors to take the source code to produce their
own custom versions, which allows the HPC system vendors to quickly produce their
own MPI libraries. To this day, all HPC systems support the familiar MPI on their
computers. This wide adoption also ensures that MPI will continue to be the favorite
communication protocol among the users of HPC systems.
