# Advances in Financial Machine Learning.pdf — pages 20–39

--- page 20 ---

CONTENTS
xv
Exercises, 208
References, 209
Bibliography, 209
15
Understanding Strategy Risk
211
15.1
Motivation, 211
15.2
Symmetric Payouts, 211
15.3
Asymmetric Payouts, 213
15.4
The Probability of Strategy Failure, 216
15.4.1
Algorithm, 217
15.4.2
Implementation, 217
Exercises, 219
References, 220
16
Machine Learning Asset Allocation
221
16.1
Motivation, 221
16.2
The Problem with Convex Portfolio Optimization, 221
16.3
Markowitz’s Curse, 222
16.4
From Geometric to Hierarchical Relationships, 223
16.4.1
Tree Clustering, 224
16.4.2
Quasi-Diagonalization, 229
16.4.3
Recursive Bisection, 229
16.5
A Numerical Example, 231
16.6
Out-of-Sample Monte Carlo Simulations, 234
16.7
Further Research, 236
16.8
Conclusion, 238
Appendices, 239
16.A.1
Correlation-based Metric, 239
16.A.2
Inverse Variance Allocation, 239
16.A.3
Reproducing the Numerical Example, 240
16.A.4
Reproducing the Monte Carlo Experiment, 242
Exercises, 244
References, 245
PART 4
USEFUL FINANCIAL FEATURES
247
17
Structural Breaks
249
17.1
Motivation, 249
17.2
Types of Structural Break Tests, 249
--- page 21 ---

xvi
CONTENTS
17.3
CUSUM Tests, 250
17.3.1
Brown-Durbin-Evans CUSUM Test on Recursive
Residuals, 250
17.3.2
Chu-Stinchcombe-White CUSUM Test on Levels, 251
17.4
Explosiveness Tests, 251
17.4.1
Chow-Type Dickey-Fuller Test, 251
17.4.2
Supremum Augmented Dickey-Fuller, 252
17.4.3
Suband Super-Martingale Tests, 259
Exercises, 261
References, 261
18
Entropy Features
263
18.1
Motivation, 263
18.2
Shannon’s Entropy, 263
18.3
The Plug-in (or Maximum Likelihood) Estimator, 264
18.4
Lempel-Ziv Estimators, 265
18.5
Encoding Schemes, 269
18.5.1
Binary Encoding, 270
18.5.2
Quantile Encoding, 270
18.5.3
Sigma Encoding, 270
18.6
Entropy of a Gaussian Process, 271
18.7
Entropy and the Generalized Mean, 271
18.8
A Few Financial Applications of Entropy, 275
18.8.1
Market Efficiency, 275
18.8.2
Maximum Entropy Generation, 275
18.8.3
Portfolio Concentration, 275
18.8.4
Market Microstructure, 276
Exercises, 277
References, 278
Bibliography, 279
19
Microstructural Features
281
19.1
Motivation, 281
19.2
Review of the Literature, 281
19.3
First Generation: Price Sequences, 282
19.3.1
The Tick Rule, 282
19.3.2
The Roll Model, 282
--- page 22 ---

CONTENTS
xvii
19.3.3
High-Low Volatility Estimator, 283
19.3.4
Corwin and Schultz, 284
19.4
Second Generation: Strategic Trade Models, 286
19.4.1
Kyle’s Lambda, 286
19.4.2
Amihud’s Lambda, 288
19.4.3
Hasbrouck’s Lambda, 289
19.5
Third Generation: Sequential Trade Models, 290
19.5.1
Probability of Information-based Trading, 290
19.5.2
Volume-Synchronized Probability of Informed
Trading, 292
19.6
Additional Features from Microstructural Datasets, 293
19.6.1
Distibution of Order Sizes, 293
19.6.2
Cancellation Rates, Limit Orders, Market Orders, 293
19.6.3
Time-Weighted Average Price Execution Algorithms, 294
19.6.4
Options Markets, 295
19.6.5
Serial Correlation of Signed Order Flow, 295
19.7
What Is Microstructural Information?, 295
Exercises, 296
References, 298
PART 5
HIGH-PERFORMANCE COMPUTING RECIPES
301
20
Multiprocessing and Vectorization
303
20.1
Motivation, 303
20.2
Vectorization Example, 303
20.3
Single-Thread vs. Multithreading vs. Multiprocessing, 304
20.4
Atoms and Molecules, 306
20.4.1
Linear Partitions, 306
20.4.2
Two-Nested Loops Partitions, 307
20.5
Multiprocessing Engines, 309
20.5.1
Preparing the Jobs, 309
20.5.2
Asynchronous Calls, 311
20.5.3
Unwrapping the Callback, 312
20.5.4
Pickle/Unpickle Objects, 313
20.5.5
Output Reduction, 313
20.6
Multiprocessing Example, 315
Exercises, 316
--- page 23 ---

xviii
CONTENTS
Reference, 317
Bibliography, 317
21
Brute Force and Quantum Computers
319
21.1
Motivation, 319
21.2
Combinatorial Optimization, 319
21.3
The Objective Function, 320
21.4
The Problem, 321
21.5
An Integer Optimization Approach, 321
21.5.1
Pigeonhole Partitions, 321
21.5.2
Feasible Static Solutions, 323
21.5.3
Evaluating Trajectories, 323
21.6
A Numerical Example, 325
21.6.1
Random Matrices, 325
21.6.2
Static Solution, 326
21.6.3
Dynamic Solution, 327
Exercises, 327
References, 328
22
High-Performance Computational Intelligence and Forecasting
Technologies
329
Kesheng Wu and Horst D. Simon
22.1
Motivation, 329
22.2
Regulatory Response to the Flash Crash of 2010, 329
22.3
Background, 330
22.4
HPC Hardware, 331
22.5
HPC Software, 335
22.5.1
Message Passing Interface, 335
22.5.2
Hierarchical Data Format 5, 336
22.5.3
In Situ Processing, 336
22.5.4
Convergence, 337
22.6
Use Cases, 337
22.6.1
Supernova Hunting, 337
22.6.2
Blobs in Fusion Plasma, 338
22.6.3
Intraday Peak Electricity Usage, 340
22.6.4
The Flash Crash of 2010, 341
22.6.5
Volume-synchronized Probability of Informed Trading
Calibration, 346
--- page 24 ---

CONTENTS
xix
22.6.6
Revealing High Frequency Events with Non-uniform
Fast Fourier Transform, 347
22.7
Summary and Call for Participation, 349
22.8
Acknowledgments, 350
References, 350
Index
353
--- page 25 ---
--- page 26 ---

About the Author
Marcos L´opez de Prado manages several multibillion-dollar funds for institutional
investors using machine learning algorithms. Over the past 20 years, his work has
combined advanced mathematics with supercomputing technologies to deliver billions of dollars in net profits for investors and firms. A proponent of research by
collaboration, Marcos has published with more than 30 leading academics, resulting
in some of the most-read papers in finance.
Since 2010, Marcos has also been a Research Fellow at Lawrence Berkeley
National Laboratory (U.S. Department of Energy’s Office of Science), where he
conducts research focused on the mathematics of large-scale financial problems and
high-performance computing at the Computational Research department. For the past
seven years he has lectured at Cornell University, where he currently teaches a graduate course in financial big data and machine learning in the Operations Research
department.
Marcos is the recipient of the 1999 National Award for Academic Excellence,
which the government of Spain bestows upon the best graduate student nationally.
He earned a PhD in financial economics (2003) and a second PhD in mathematical
finance (2011) from Universidad Complutense de Madrid. Between his two doctorates, Marcos was a postdoctoral research fellow of RCC at Harvard University for
three years, during which he published more than a dozen articles in JCR-indexed
scientific journals. Marcos has an Erd´´os #2 and an Einstein #4, according to the American Mathematical Society.
xxi
--- page 27 ---
--- page 28 ---

Preamble
Chapter 1: Financial Machine Learning as a Distinct Subject, 3
1
--- page 29 ---
--- page 30 ---

CHAPTER 1
Financial Machine Learning as a
Distinct Subject
1.1
MOTIVATION
Machine learning (ML) is changing virtually every aspect of our lives. Today ML
algorithms accomplish tasks that until recently only expert humans could perform.
As it relates to finance, this is the most exciting time to adopt a disruptive technology
that will transform how everyone invests for generations. This book explains scientifically sound ML tools that have worked for me over the course of two decades,
and have helped me to manage large pools of funds for some of the most demanding
institutional investors.
Books about investments largely fall in one of two categories. On one hand we
find books written by authors who have not practiced what they teach. They contain
extremely elegant mathematics that describes a world that does not exist. Just because
a theorem is true in a logical sense does not mean it is true in a physical sense. On the
other hand we find books written by authors who offer explanations absent of any
rigorous academic theory. They misuse mathematical tools to describe actual observations. Their models are overfit and fail when implemented. Academic investigation
and publication are divorced from practical application to financial markets, and
many applications in the trading/investment world are not grounded in proper science.
A first motivation for writing this book is to cross the proverbial divide that separates academia and the industry. I have been on both sides of the rift, and I understand
how difficult it is to cross it and how easy it is to get entrenched on one side. Virtue is
in the balance. This book will not advocate a theory merely because of its mathematical beauty, and will not propose a solution just because it appears to work. My goal
is to transmit the kind of knowledge that only comes from experience, formalized in
a rigorous manner.
3
--- page 31 ---

4
FINANCIAL MACHINE LEARNING AS A DISTINCT SUBJECT
A second motivation is inspired by the desire that finance serves a purpose. Over
the years some of my articles, published in academic journals and newspapers, have
expressed my displeasure with the current role that finance plays in our society.
Investors are lured to gamble their wealth on wild hunches originated by charlatans
and encouraged by mass media. One day in the near future, ML will dominate finance,
science will curtail guessing, and investing will not mean gambling. I would like the
reader to play a part in that revolution.
A third motivation is that many investors fail to grasp the complexity of ML applications to investments. This seems to be particularly true for discretionary firms moving into the “quantamental” space. I am afraid their high expectations will not be
met, not because ML failed, but because they used ML incorrectly. Over the coming years, many firms will invest with off-the-shelf ML algorithms, directly imported
from academia or Silicon Valley, and my forecast is that they will lose money (to
better ML solutions). Beating the wisdom of the crowds is harder than recognizing
faces or driving cars. With this book my hope is that you will learn how to solve some
of the challenges that make finance a particularly difficult playground for ML, like
backtest overfitting. Financial ML is a subject in its own right, related to but separate
from standard ML, and this book unravels it for you.
1.2
THE MAIN REASON FINANCIAL MACHINE LEARNING
PROJECTS USUALLY FAIL
The rate of failure in quantitative finance is high, particularly so in financial ML. The
few who succeed amass a large amount of assets and deliver consistently exceptional
performance to their investors. However, that is a rare outcome, for reasons explained
in this book. Over the past two decades, I have seen many faces come and go, firms
started and shut down. In my experience, there is one critical mistake that underlies
all those failures.
1.2.1
The Sisyphus Paradigm
Discretionary portfolio managers (PMs) make investment decisions that do not follow a particular theory or rationale (if there were one, they would be systematic PMs).
They consume raw news and analyses, but mostly rely on their judgment or intuition. They may rationalize those decisions based on some story, but there is always
a story for every decision. Because nobody fully understands the logic behind their
bets, investment firms ask them to work independently from one another, in silos, to
ensure diversification. If you have ever attended a meeting of discretionary PMs, you
probably noticed how long and aimless they can be. Each attendee seems obsessed
about one particular piece of anecdotal information, and giant argumentative leaps
are made without fact-based, empirical evidence. This does not mean that discretionary PMs cannot be successful. On the contrary, a few of them are. The point is,
they cannot naturally work as a team. Bring 50 discretionary PMs together, and they
--- page 32 ---

THE MAIN REASON FINANCIAL MACHINE LEARNING PROJECTS USUALLY FAIL
5
will influence one another until eventually you are paying 50 salaries for the work of
one. Thus it makes sense for them to work in silos so they interact as little as possible.
Wherever I have seen that formula applied to quantitative or ML projects, it has
led to disaster. The boardroom’s mentality is, let us do with quants what has worked
with discretionary PMs. Let us hire 50 PhDs and demand that each of them produce an
investment strategy within six months. This approach always backfires, because each
PhD will frantically search for investment opportunities and eventually settle for (1)
a false positive that looks great in an overfit backtest or (2) standard factor investing,
which is an overcrowded strategy with a low Sharpe ratio, but at least has academic
support. Both outcomes will disappoint the investment board, and the project will
be cancelled. Even if 5 of those PhDs identified a true discovery, the profits would
not suffice to cover for the expenses of 50, so those 5 will relocate somewhere else,
searching for a proper reward.
1.2.2
The Meta-Strategy Paradigm
If you have been asked to develop ML strategies on your own, the odds are stacked
against you. It takes almost as much effort to produce one true investment strategy
as to produce a hundred, and the complexities are overwhelming: data curation and
processing, HPC infrastructure, software development, feature analysis, execution
simulators, backtesting, etc. Even if the firm provides you with shared services in
those areas, you are like a worker at a BMW factory who has been asked to build an
entire car by using all the workshops around you. One week you need to be a master
welder, another week an electrician, another week a mechanical engineer, another
week a painter . . . You will try, fail, and circle back to welding. How does that
make sense?
Every successful quantitative firm I am aware of applies the meta-strategy
paradigm (L´opez de Prado [2014]). Accordingly, this book was written as a research
manual for teams, not for individuals. Through its chapters you will learn how to set
up a research factory, as well as the various stations of the assembly line. The role of
each quant is to specialize in a particular task, to become the best there is at it, while
having a holistic view of the entire process. This book outlines the factory plan,
where teamwork yields discoveries at a predictable rate, with no reliance on lucky
strikes. This is how Berkeley Lab and other U.S. National Laboratories routinely
make scientific discoveries, such as adding 16 elements to the periodic table, or
laying out the groundwork for MRIs and PET scans.1 No particular individual is
responsible for these discoveries, as they are the outcome of team efforts where
everyone contributes. Of course, setting up these financial laboratories takes time,
and requires people who know what they are doing and have done it before. But
what do you think has a higher chance of success, this proven paradigm of organized
collaboration or the Sisyphean alternative of having every single quant rolling their
immense boulder up the mountain?
1 Berkeley Lab, http://www.lbl.gov/about.
--- page 33 ---

6
FINANCIAL MACHINE LEARNING AS A DISTINCT SUBJECT
1.3
BOOK STRUCTURE
This book disentangles a web of interconnected topics and presents them in an
ordered fashion. Each chapter assumes that you have read the previous ones. Part
1 will help you structure your financial data in a way that is amenable to ML algorithms. Part 2 discusses how to do research with ML algorithms on that data. Here
the emphasis is on doing research and making an actual discovery through a scientific process, as opposed to searching aimlessly until some serendipitous (likely false)
result pops up. Part 3 explains how to backtest your discovery and evaluate the probability that it is false.
These three parts give an overview of the entire process, from data analysis to
model research to discovery evaluation. With that knowledge, Part 4 goes back to the
data and explains innovative ways to extract informative features. Finally, much of
this work requires a lot of computational power, so Part 5 wraps up the book with
some useful HPC recipes.
1.3.1
Structure by Production Chain
Mining gold or silver was a relatively straightforward endeavor during the 16th and
17th centuries. In less than a hundred years, the Spanish treasure fleet quadrupled
the amount of precious metals in circulation throughout Europe. Those times are
long gone, and today prospectors must deploy complex industrial methods to extract
microscopic bullion particles out of tons of earth. That does not mean that gold
production is at historical lows. On the contrary, nowadays miners extract 2,500
metric tons of microscopic gold every year, compared to the average annual 1.54
metric tons taken by the Spanish conquistadors throughout the entire 16th century!2
Visible gold is an infinitesimal portion of the overall amount of gold on Earth. El
Dorado was always there . . . if only Pizarro could have exchanged the sword for a
microscope.
The discovery of investment strategies has undergone a similar evolution. If a
decade ago it was relatively common for an individual to discover macroscopic alpha
(i.e., using simple mathematical tools like econometrics), currently the chances of that
happening are quickly converging to zero. Individuals searching nowadays for macroscopic alpha, regardless of their experience or knowledge, are fighting overwhelming
odds. The only true alpha left is microscopic, and finding it requires capital-intensive
industrial methods. Just like with gold, microscopic alpha does not mean smaller
overall profits. Microscopic alpha today is much more abundant than macroscopic
alpha has ever been in history. There is a lot of money to be made, but you will need
to use heavy ML tools.
Let us review some of the stations involved in the chain of production within a
modern asset manager.
2 http://www.numbersleuth.org/worlds-gold/.
--- page 34 ---

BOOK STRUCTURE
7
1.3.1.1
Data Curators
This is the station responsible for collecting, cleaning, indexing, storing, adjusting,
and delivering all data to the production chain. The values could be tabulated or
hierarchical, aligned or misaligned, historical or real-time feeds, etc. Team members are experts in market microstructure and data protocols such as FIX. They must
develop the data handlers needed to understand the context in which that data arises.
For example, was a quote cancelled and replaced at a different level, or cancelled
without replacement? Each asset class has its own nuances. For instance, bonds are
routinely exchanged or recalled; stocks are subjected to splits, reverse-splits, voting
rights, etc.; futures and options must be rolled; currencies are not traded in a centralized order book. The degree of specialization involved in this station is beyond the
scope of this book, and Chapter 1 will discuss only a few aspects of data curation.
1.3.1.2
Feature Analysts
This is the station responsible for transforming raw data into informative signals.
These informative signals have some predictive power over financial variables. Team
members are experts in information theory, signal extraction and processing, visualization, labeling, weighting, classifiers, and feature importance techniques. For example, feature analysts may discover that the probability of a sell-off is particularly high
when: (1) quoted offers are cancelled-replaced with market sell orders, and (2) quoted
buy orders are cancelled-replaced with limit buy orders deeper in the book. Such a
finding is not an investment strategy on its own, and can be used in alternative ways:
execution, monitoring of liquidity risk, market making, position taking, etc. A common error is to believe that feature analysts develop strategies. Instead, feature analysts collect and catalogue libraries of findings that can be useful to a multiplicity of
stations. Chapters 2–9 and 17–19 are dedicated to this all-important station.
1.3.1.3
Strategists
In this station, informative features are transformed into actual investment algorithms.
A strategist will parse through the libraries of features looking for ideas to develop
an investment strategy. These features were discovered by different analysts studying
a wide range of instruments and asset classes. The goal of the strategist is to make
sense of all these observations and to formulate a general theory that explains them.
Therefore, the strategy is merely the experiment designed to test the validity of this
theory. Team members are data scientists with a deep knowledge of financial markets and the economy. Remember, the theory needs to explain a large collection of
important features. In particular, a theory must identify the economic mechanism that
causes an agent to lose money to us. Is it a behavioral bias? Asymmetric information?
Regulatory constraints? Features may be discovered by a black box, but the strategy
is developed in a white box. Gluing together a number of catalogued features does not
constitute a theory. Once a strategy is finalized, the strategists will prepare code that
utilizes the full algorithm and submit that prototype to the backtesting team described
below. Chapters 10 and 16 are dedicated to this station, with the understanding that
it would be unreasonable for a book to reveal specific investment strategies.
--- page 35 ---

8
FINANCIAL MACHINE LEARNING AS A DISTINCT SUBJECT
1.3.1.4
Backtesters
This station assesses the profitability of an investment strategy under various scenarios. One of the scenarios of interest is how the strategy would perform if history
repeated itself. However, the historical path is merely one of the possible outcomes of
a stochastic process, and not necessarily the most likely going forward. Alternative
scenarios must be evaluated, consistent with the knowledge of the weaknesses and
strengths of a proposed strategy. Team members are data scientists with a deep understanding of empirical and experimental techniques. A good backtester incorporates
in his analysis meta-information regarding how the strategy came about. In particular, his analysis must evaluate the probability of backtest overfitting by taking into
account the number of trials it took to distill the strategy. The results of this evaluation
will not be reused by other stations, for reasons that will become apparent in Chapter
11. Instead, backtest results are communicated to management and not shared with
anyone else. Chapters 11–16 discuss the analyses carried out by this station.
1.3.1.5
Deployment Team
The deployment team is tasked with integrating the strategy code into the production
line. Some components may be reused by multiple strategies, especially when they
share common features. Team members are algorithm specialists and hardcore
mathematical programmers. Part of their job is to ensure that the deployed solution
is logically identical to the prototype they received. It is also the deployment team’s
responsibility to optimize the implementation sufficiently, such that production
latency is minimized. As production calculations often are time sensitive, this team
will rely heavily on process schedulers, automation servers (Jenkins), vectorization, multithreading, multiprocessing, graphics processing unit (GPU-NVIDIA),
distributed computing (Hadoop), high-performance computing (Slurm), and parallel computing techniques in general. Chapters 20–22 touch on various aspects
interesting to this station, as they relate to financial ML.
1.3.1.6
Portfolio Oversight
Once a strategy is deployed, it follows a cursus honorum, which entails the following
stages or lifecycle:
1. Embargo: Initially, the strategy is run on data observed after the end date of the
backtest. Such a period may have been reserved by the backtesters, or it may
be the result of implementation delays. If embargoed performance is consistent
with backtest results, the strategy is promoted to the next stage.
2. Paper trading: At this point, the strategy is run on a live, real-time feed. In this
way, performance will account for data parsing latencies, calculation latencies,
execution delays, and other time lapses between observation and positioning.
Paper trading will take place for as long as it is needed to gather enough evidence that the strategy performs as expected.
3. Graduation: At this stage, the strategy manages a real position, whether in isolation or as part of an ensemble. Performance is evaluated precisely, including
attributed risk, returns, and costs.
--- page 36 ---

BOOK STRUCTURE
9
4. Re-allocation: Based on the production performance, the allocation to graduated strategies is re-assessed frequently and automatically in the context of a
diversified portfolio. In general, a strategy’s allocation follows a concave function. The initial allocation (at graduation) is small. As time passes, and the strategy performs as expected, the allocation is increased. Over time, performance
decays, and allocations become gradually smaller.
5. Decommission: Eventually, all strategies are discontinued. This happens when
they perform below expectations for a sufficiently extended period of time to
conclude that the supporting theory is no longer backed by empirical evidence.
In general, it is preferable to release new variations of a strategy and run them in
parallel with old versions. Each version will go through the above lifecycle, and old
strategies will receive smaller allocations as a matter of diversification, while taking
into account the degree of confidence derived from their longer track record.
1.3.2
Structure by Strategy Component
Many investment managers believe that the secret to riches is to implement an
extremely complex ML algorithm. They are setting themselves up for a disappointment. If it was as easy as coding a state-of-the art classifier, most people in Silicon
Valley would be billionaires. A successful investment strategy is the result of multiple factors. Table 1.1 summarizes what chapters will help you address each of the
challenges involved in developing a successful investment strategy.
Throughout the book, you will find many references to journal articles I have
published over the years. Rather than repeating myself, I will often refer you to
one of them, where you will find a detailed analysis of the subject at hand. All of
my cited papers can be downloaded for free, in pre-print format, from my website:
www.QuantResearch.org.
1.3.2.1
Data
r Problem: Garbage in, garbage out.
r Solution: Work with unique, hard-to-manipulate data. If you are the only user
of this data, whatever its value, it is all for you.
r How:
◦Chapter 2: Structure your data correctly.
◦Chapter 3: Produce informative labels.
◦Chapters 4 and 5: Model non-IID series properly.
◦Chapters 17–19: Find predictive features.
1.3.2.2
Software
r Problem: A specialized task requires customized tools.
r Solution: Develop your own classes. Using popular libraries means more competitors tapping the same well.
--- page 37 ---

10
FINANCIAL MACHINE LEARNING AS A DISTINCT SUBJECT
TABLE 1.1
Overview of the Challenges Addressed by Every Chapter
Part
Chapter
Fin. data
Software
Hardware
Math
Meta-Strat
Overfitting
1
2
X
X
1
3
X
X
1
4
X
X
1
5
X
X
X
2
6
X
2
7
X
X
X
2
8
X
X
2
9
X
X
3
10
X
X
3
11
X
X
X
3
12
X
X
X
3
13
X
X
X
3
14
X
X
X
3
15
X
X
X
3
16
X
X
X
X
4
17
X
X
X
4
18
X
X
X
4
19
X
X
5
20
X
X
X
5
21
X
X
X
5
22
X
X
X
r How:
◦Chapters 2–22: Throughout the book, for each chapter, we develop our own
functions. For your particular problems, you will have to do the same, following the examples in the book.
1.3.2.3
Hardware
r Problem: ML involves some of the most computationally intensive tasks in all
of mathematics.
r Solution: Become an HPC expert. If possible, partner with a National Laboratory to build a supercomputer.
r How:
◦Chapters 20 and 22: Learn how to think in terms of multiprocessing architectures. Whenever you code a library, structure it in such a way that functions
can be called in parallel. You will find plenty of examples in the book.
◦Chapter 21: Develop algorithms for quantum computers.
1.3.2.4
Math
r Problem: Mathematical proofs can take years, decades, and centuries. No
investor will wait that long.
--- page 38 ---

BOOK STRUCTURE
11
r Solution: Use experimental math. Solve hard, intractable problems, not by proof
but by experiment. For example, Bailey, Borwein, and Plouffe [1997] found a
spigot algorithm for 𝜋(pi) without proof, against the prior perception that such
mathematical finding would not be possible.
r How:
◦Chapter 5: Familiarize yourself with memory-preserving data transformations.
◦Chapters 11–15: There are experimental methods to assess the value of your
strategy, with greater reliability than a historical simulation.
◦Chapter 16: An algorithm that is optimal in-sample can perform poorly outof-sample. There is no mathematical proof for investment success. Rely on
experimental methods to lead your research.
◦Chapters 17 and 18: Apply methods to detect structural breaks, and quantify
the amount of information carried by financial series.
◦Chapter 20: Learn queuing methods for distributed computing so that you
can break apart complex tasks and speed up calculations.
◦Chapter 21: Become familiar with discrete methods, used among others by
quantum computers, to solve intractable problems.
1.3.2.5
Meta-Strategies
r Problem: Amateurs develop individual strategies, believing that there is such a
thing as a magical formula for riches. In contrast, professionals develop methods to mass-produce strategies. The money is not in making a car, it is in making
a car factory.
r Solution: Think like a business. Your goal is to run a research lab like a factory,
where true discoveries are not born out of inspiration, but out of methodic hard
work. That was the philosophy of physicist Ernest Lawrence, the founder of the
first U.S. National Laboratory.
r How:
◦Chapters 7–9: Build a research process that identifies features relevant
across asset classes, while dealing with multi-collinearity of financial
features.
◦Chapter 10: Combine multiple predictions into a single bet.
◦Chapter 16: Allocate funds to strategies using a robust method that performs
well out-of-sample.
1.3.2.6
Overfitting
r Problem: Standard cross-validation methods fail in finance. Most discoveries in
finance are false, due to multiple testing and selection bias.
r Solution:
◦Whatever you do, always ask yourself in what way you may be overfitting. Be
skeptical about your own work, and constantly challenge yourself to prove
that you are adding value.
--- page 39 ---

12
FINANCIAL MACHINE LEARNING AS A DISTINCT SUBJECT
◦Overfitting is unethical. It leads to promising outcomes that cannot be delivered. When done knowingly, overfitting is outright scientific fraud. The fact
that many academics do it does not make it right: They are not risking anyone’s wealth, not even theirs.
◦It is also a waste of your time, resources, and opportunities. Besides, the
industry only pays for out-of-sample returns. You will only succeed after
you have created substantial wealth for your investors.
r How:
◦Chapters 11–15: There are three backtesting paradigms, of which historical
simulation is only one. Each backtest is always overfit to some extent, and it
is critical to learn to quantify by how much.
◦Chapter 16: Learn robust techniques for asset allocation that do not overfit
in-sample signals at the expense of out-of-sample performance.
1.3.3
Structure by Common Pitfall
Despite its many advantages, ML is no panacea. The flexibility and power of ML
techniques have a dark side. When misused, ML algorithms will confuse statistical flukes with patterns. This fact, combined with the low signal-to-noise ratio that
characterizes finance, all but ensures that careless users will produce false discoveries at an ever-greater speed. This book exposes some of the most pervasive errors
made by ML experts when they apply their techniques on financial datasets. Some of
these pitfalls are listed in Table 1.2, with solutions that are explained in the indicated
chapters.
1.4
TARGET AUDIENCE
This book presents advanced ML methods specifically designed to address the challenges posed by financial datasets. By “advanced” I do not mean extremely difficult to
grasp, or explaining the latest reincarnation of deep, recurrent, or convolutional neural networks. Instead, the book answers questions that senior researchers, who have
experience applying ML algorithms to financial problems, will recognize as critical.
If you are new to ML, and you do not have experience working with complex algorithms, this book may not be for you (yet). Unless you have confronted in practice the
problems discussed in these chapters, you may have difficulty understanding the utility of solving them. Before reading this book, you may want to study several excellent
introductory ML books published in recent years. I have listed a few of them in the
references section.
The core audience of this book is investment professionals with a strong ML background. My goals are that you monetize what you learn in this book, help us modernize finance, and deliver actual value for investors.
This book also targets data scientists who have successfully implemented ML
algorithms in a variety of fields outside finance. If you have worked at Google and
have applied deep neural networks to face recognition, but things do not seem to
