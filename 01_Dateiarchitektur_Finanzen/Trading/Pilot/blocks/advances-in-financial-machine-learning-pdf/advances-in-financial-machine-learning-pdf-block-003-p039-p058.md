# Advances in Financial Machine Learning.pdf — pages 39–58

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
--- page 40 ---

REQUISITES
13
TABLE 1.2
Common Pitfalls in Financial ML
#
Category
Pitfall
Solution
Chapter
1
Epistemological
The Sisyphus paradigm
The meta-strategy
paradigm
1
2
Epistemological
Research through
backtesting
Feature importance
analysis
8
3
Data processing
Chronological
sampling
The volume clock
2
4
Data processing
Integer differentiation
Fractional
differentiation
5
5
Classification
Fixed-time horizon
labeling
The triple-barrier
method
3
6
Classification
Learning side and size
simultaneously
Meta-labeling
3
7
Classification
Weighting of non-IID
samples
Uniqueness weighting;
sequential
bootstrapping
4
8
Evaluation
Cross-validation
leakage
Purging and
embargoing
7, 9
9
Evaluation
Walk-forward
(historical) backtesting
Combinatorial purged
cross-validation
11, 12
10
Evaluation
Backtest overfitting
Backtesting on
synthetic data; the
deflated Sharpe ratio
10–16
work so well when you run your algorithms on financial data, this book will help
you. Sometimes you may not understand the financial rationale behind some structures (e.g., meta-labeling, the triple-barrier method, fracdiff), but bear with me: Once
you have managed an investment portfolio long enough, the rules of the game will
become clearer to you, along with the meaning of these chapters.
1.5
REQUISITES
Investment management is one of the most multi-disciplinary areas of research, and
this book reflects that fact. Understanding the various sections requires a practical
knowledge of ML, market microstructure, portfolio management, mathematical
finance, statistics, econometrics, linear algebra, convex optimization, discrete
math, signal processing, information theory, object-oriented programming, parallel
processing, and supercomputing.
Python has become the de facto standard language for ML, and I have to assume
that you are an experienced developer. You must be familiar with scikit-learn
(sklearn), pandas, numpy, scipy, multiprocessing, matplotlib and a few other libraries.
--- page 41 ---

14
FINANCIAL MACHINE LEARNING AS A DISTINCT SUBJECT
Code snippets invoke functions from these libraries using their conventional prefix,
pd for pandas, np for numpy, mpl for matplotlib, etc. There are numerous books on
each of these libraries, and you cannot know enough about the specifics of each one.
Throughout the book we will discuss some issues with their implementation, including unresolved bugs to keep in mind.
1.6
FAQs
How can ML algorithms be useful in finance?
Many financial operations require making decisions based on pre-defined rules, like
option pricing, algorithmic execution, or risk monitoring. This is where the bulk of
automation has taken place so far, transforming the financial markets into ultra-fast,
hyper-connected networks for exchanging information. In performing these tasks,
machines were asked to follow the rules as fast as possible. High-frequency trading
is a prime example. See Easley, L´opez de Prado, and O’Hara [2013] for a detailed
treatment of the subject.
The algorithmization of finance is unstoppable. Between June 12, 1968, and
December 31, 1968, the NYSE was closed every Wednesday, so that back office could
catch up with paperwork. Can you imagine that? We live in a different world today,
and in 10 years things will be even better. Because the next wave of automation does
not involve following rules, but making judgment calls. As emotional beings, subject
to fears, hopes, and agendas, humans are not particularly good at making fact-based
decisions, particularly when those decisions involve conflicts of interest. In those situations, investors are better served when a machine makes the calls, based on facts
learned from hard data. This not only applies to investment strategy development, but
to virtually every area of financial advice: granting a loan, rating a bond, classifying
a company, recruiting talent, predicting earnings, forecasting inflation, etc. Furthermore, machines will comply with the law, always, when programmed to do so. If a
dubious decision is made, investors can go back to the logs and understand exactly
what happened. It is much easier to improve an algorithmic investment process than
one relying entirely on humans.
How can ML algorithms beat humans at investing?
Do you remember when people were certain that computers would never beat humans
at chess? Or Jeopardy!? Poker? Go? Millions of years of evolution (a genetic algorithm) have fine-tuned our ape brains to survive in a hostile 3-dimensional world
where the laws of nature are static. Now, when it comes to identifying subtle patterns
in a high-dimensional world, where the rules of the game change every day, all
that fine-tuning turns out to be detrimental. An ML algorithm can spot patterns in a
100-dimensional world as easily as in our familiar 3-dimensional one. And while we
all laugh when we see an algorithm make a silly mistake, keep in mind, algorithms
have been around only a fraction of our millions of years. Every day they get better
at this, we do not. Humans are slow learners, which puts us at a disadvantage in a
fast-changing world like finance.
--- page 42 ---

FAQs
15
Does that mean that there is no space left for human investors?
Not at all. No human is better at chess than a computer. And no computer is better
at chess than a human supported by a computer. Discretionary PMs are at a disadvantage when betting against an ML algorithm, but it is possible that the best results
are achieved by combining discretionary PMs with ML algorithms. This is what has
come to be known as the “quantamental” way. Throughout the book you will find
techniques that can be used by quantamental teams, that is, methods that allow you
to combine human guesses (inspired by fundamental variables) with mathematical
forecasts. In particular, Chapter 3 introduces a new technique called meta-labeling,
which allows you to add an ML layer on top of a discretionary one.
How does financial ML differ from econometrics?
Econometrics is the application of classical statistical methods to economic and financial series. The essential tool of econometrics is multivariate linear regression, an
18th-century technology that was already mastered by Gauss before 1794 (Stigler
[1981]). Standard econometric models do not learn. It is hard to believe that something as complex as 21st-century finance could be grasped by something as simple
as inverting a covariance matrix.
Every empirical science must build theories based on observation. If the statistical
toolbox used to model these observations is linear regression, the researcher will fail
to recognize the complexity of the data, and the theories will be awfully simplistic,
useless. I have no doubt in my mind, econometrics is a primary reason economics
and finance have not experienced meaningful progress over the past 70 years (Calkin
and L´opez de Prado [2014a, 2014b]).
For centuries, medieval astronomers made observations and developed theories about celestial mechanics. These theories never considered non-circular orbits,
because they were deemed unholy and beneath God’s plan. The prediction errors were
so gross, that ever more complex theories had to be devised to account for them. It was
not until Kepler had the temerity to consider non-circular (elliptical) orbits that all of
the sudden a much simpler general model was able to predict the position of the planets with astonishing accuracy. What if astronomers had never considered non-circular
orbits? Well . . . what if economists finally started to consider non-linear functions?
Where is our Kepler? Finance does not have a Principia because no Kepler means no
Newton.
Financial ML methods do not replace theory. They guide it. An ML algorithm
learns patterns in a high-dimensional space without being specifically directed. Once
we understand what features are predictive of a phenomenon, we can build a theoretical explanation, which can be tested on an independent dataset. Students of economics and finance would do well enrolling in ML courses, rather than econometrics.
Econometrics may be good enough to succeed in financial academia (for now), but
succeeding in business requires ML.
What do you say to people who dismiss ML algorithms as black boxes?
If you are reading this book, chances are ML algorithms are white boxes to you.
They are transparent, well-defined, crystal-clear, pattern-recognition functions. Most
--- page 43 ---

16
FINANCIAL MACHINE LEARNING AS A DISTINCT SUBJECT
people do not have your knowledge, and to them ML is like a magician’s box: “Where
did that rabbit come from? How are you tricking us, witch?” People mistrust what they
do not understand. Their prejudices are rooted in ignorance, for which the Socratic
remedy is simple: education. Besides, some of us enjoy using our brains, even though
neuroscientists still have not figured out exactly how they work (a black box in itself).
From time to time you will encounter Luddites, who are beyond redemption. Ned
Ludd was a weaver from Leicester, England, who in 1779 smashed two knitting
frames in an outrage. With the advent of the industrial revolution, mobs infuriated by
mechanization sabotaged and destroyed all machinery they could find. Textile workers ruined so much industrial equipment that Parliament had to pass laws making
“machine breaking” a capital crime. Between 1811 and 1816, large parts of England were in open rebellion, to the point that there were more British troops fighting
Luddites than there were fighting Napoleon on the Iberian Peninsula. The Luddite
rebellion ended with brutal suppression through military force. Let us hope that the
black box movement does not come to that.
Why don’t you discuss specific ML algorithms?
The book is agnostic with regards to the particular ML algorithm you choose.
Whether you use convolutional neural networks, AdaBoost, RFs, SVMs, and so on,
there are many shared generic problems you will face: data structuring, labeling, weighting, stationary transformations, cross-validation, feature selection, feature importance, overfitting, backtesting, etc. In the context of financial modeling,
answering these questions is non-trivial, and framework-specific approaches need to
be developed. That is the focus of this book.
What other books do you recommend on this subject?
To my knowledge, this is the first book to provide a complete and systematic treatment
of ML methods specific for finance: starting with a chapter dedicated to financial data
structures, another chapter for labeling of financial series, another for sample weighting, time series differentiation, . . . all the way to a full part devoted to the proper backtesting of investment strategies. To be sure, there are a handful of prior publications
(mostly journal articles) that have applied standard ML to financial series, but that
is not what this book offers. My goal has been to address the unique nuisances that
make financial ML modeling particularly challenging. Like any new subject, it is fast
evolving, and the book will be updated as major advances take place. Please contact
me at mldp@quantresearch.org if there is any particular topic you would like to see
treated in future editions. I will gladly add those chapters, while acknowledging the
names of those readers who suggested them.
I do not understand some of the sections and chapters. What should I do?
My advice is that you start by reading the references listed at the end of the chapter.
When I wrote the book, I had to assume the reader was familiar with the existing
literature, or this book would lose its focus. If after reading those references the sections still do not make sense, the likely reason is that they are related to a problem
well understood by investment professionals (even if there is no mention of it in the
--- page 44 ---

FAQs
17
literature). For example, Chapter 2 will discuss effective methods to adjust futures
prices for the roll, a problem known to most practitioners, even though it is rarely
addressed in textbooks. I would encourage you to attend one of my regular seminars,
and ask me your question at the end of my talk.
Why is the book so fixated on backtest overfitting?
There are two reasons. First, backtest overfitting is arguably the most important open
problem in all of mathematical finance. It is our equivalent to “P versus NP” in computer science. If there was a precise method to prevent backtest overfitting, we would
be able to take backtests to the bank. A backtest would be almost as good as cash,
rather than a sales pitch. Hedge funds would allocate funds to portfolio managers
with confidence. Investors would risk less, and would be willing to pay higher fees.
Regulators would grant licenses to hedge fund managers on the basis of reliable evidence of skill and knowledge, leaving no space for charlatans. In my opinion, an
investments book that does not address this issue is not worth your time. Why would
you read a book that deals with CAPM, APT, asset allocation techniques, risk management, etc. when the empirical results that support those arguments were selected
without determining their false discovery probabilities?
The second reason is that ML is a great weapon in your research arsenal, and a
dangerous one to be sure. If backtest overfitting is an issue in econometric analysis,
the flexibility of ML makes it a constant threat to your work. This is particularly the
case in finance, because our datasets are shorter, with lower signal-to-noise ratio, and
we do not have laboratories where we can conduct experiments while controlling
for all environmental variables (L´opez de Prado [2015]). An ML book that does not
tackle these concerns can be more detrimental than beneficial to your career.
What is the mathematical nomenclature of the book?
When I started to write this book, I thought about assigning one symbol to each mathematical variable or function through all the chapters. That would work well if this
book dealt with a single subject, like stochastic optimal control. However this book
deals with a wide range of mathematical subjects, each with its own conventions.
Readers would find it harder to consult references unless I also followed literature
standards, which means that sometimes we must re-use symbols. To prevent any
confusion, every chapter explains the nomenclature as it is being used. Most of the
math is accompanied by a code snippet, so in case of doubt, please always follow
the code.
Who wrote Chapter 22?
A popular perception is that ML is a new fascinating technology invented or perfected
at IBM, Google, Facebook, Amazon, Netflix, Tesla, etc. It is true that technology firms
have become heavy users of ML, especially in recent years. Those firms sponsored
some of the most publicized recent ML achievements (like Jeopardy! or Go), which
may have reinforced that perception.
However, the reader may be surprised to learn that, in fact, U.S. National Laboratories are among the research centers with the longest track record and experience
--- page 45 ---

18
FINANCIAL MACHINE LEARNING AS A DISTINCT SUBJECT
in using ML. These centers utilized ML before it was cool, and they applied it successfully for many decades to produce astounding scientific discoveries. If predicting
what movies Netflix should recommend you to watch next is a worthy endeavor, so it
is to understand the rate of expansion of the universe, or forecasting what coastlines
will be most impacted by global warming, or preventing a cataclysmic failure of our
national power grid. These are just some of the amazing questions that institutions
like Berkeley Lab work on every day, quietly but tirelessly, with the help of ML.
In Chapter 22, Drs. Horst Simon and Kesheng Wu offer the perspective of a deputy
director and a project leader at a major U.S. National Laboratory specializing in largescale scientific research involving big data, high-performance computing, and ML.
Unlike traditional university settings, National Laboratories achieve scientific breakthroughs by putting together interdisciplinary teams that follow well-devised procedures, with strong division of labor and responsibilities. That kind of research model
by production chain was born at Berkeley Lab almost 90 years ago and inspired the
meta-strategy paradigm explained in Sections 1.2.2 and 1.3.1.
1.7
ACKNOWLEDGMENTS
Dr. Horst Simon, who is the deputy director of Lawrence Berkeley National
Laboratory, accepted to co-author Chapter 22 with Dr. Kesheng Wu, who leads
several projects at Berkeley Lab and the National Energy Research Scientific
Computing Center (NERSC).3 ML requires extreme amounts of computing power,
and my research would not have been possible without their generous support and
guidance. In that chapter, Horst and Kesheng explain how Berkeley Lab satisfies the
supercomputing needs of researchers worldwide, and the instrumental role played
by ML and big data in today’s scientific breakthroughs.
Prof. Riccardo Rebonato was the first to read this manuscript and encouraged me
to publish it. My many conversations with Prof. Frank Fabozzi on these topics were
instrumental in shaping the book in its current form. Very few people in academia
have Frank’s and Riccardo’s industry experience, and very few people in the industry
have Riccardo’s and Frank’s academic pedigree.
Over the past two decades, I have published nearly a hundred works on this book’s
subject, including journal articles, books, chapters, lectures, source code, etc. In my
latest count, these works were co-authored with more than 30 leading experts in this
field, including Prof. David H. Bailey (15 articles), Prof. David Easley (8 articles),
Prof. Maureen O’Hara (8 articles), and Prof. Jonathan M. Borwein (6 articles). This
book is to a great extent also theirs, for it would not have been possible without their
support, insights, and continuous exchange of ideas over the years. It would take too
long to give them proper credit, so instead I have published the following link where
you can find our collective effort: http://www.quantresearch.org/Co-authors.htm.
Last but not least, I would like to thank some of my research team members for
proofreading the book and helping me produce some of the figures: Diego Aparicio,
3 http://www.nersc.gov/about.
--- page 46 ---

EXERCISES
19
Dr. Lee Cohn, Dr. Michael Lewis, Dr. Michael Lock, Dr. Yaxiong Zeng, and
Dr. Zhibai Zhang.
EXERCISES
1.1 Are you aware of firms that have attempted to transition from discretionary
investments to ML-led investments, or blending them into what they call “quantamental” funds?
(a) Have they succeeded?
(b) What are the cultural difficulties involved in this transition?
1.2 What is the most important open problem in mathematical finance? If this problem was resolved, how could:
(a) regulators use it to grant investment management licenses?
(b) investors use it to allocate funds?
(c) firms use it to reward researchers?
1.3 According to Institutional Investor, only 17% of hedge fund assets are managed
by quantitative firms. That is about $500 billion allocated in total across all
quantitative funds as of June 2017, compared to $386 billion a year earlier.
What do you think is driving this massive reallocation of assets?
1.4 According to Institutional Investor’s Rich List, how many quantitative investment firms are placed within the top 10 most profitable firms? How does that
compare to the proportion of assets managed by quantitative funds?
1.5 What is the key difference between econometric methods and ML? How would
economics and finance benefit from updating their statistical toolkit?
1.6 Science has a very minimal understanding of how the human brain (or any brain)
works. In this sense, the brain is an absolute black box. What do you think
causes critics of financial ML to disregard it as a black box, while embracing
discretionary investing?
1.7 You read a journal article that describes an investment strategy. In a backtest, it
achieves an annualized Sharpe ratio in excess of 2, with a confidence level of
95%. Using their dataset, you are able to reproduce their result in an independent
backtest. Why is this discovery likely to be false?
1.8 Investment advisors are plagued with conflicts of interest while making decisions on behalf of their investors.
(a) ML algorithms can manage investments without conflict of interests. Why?
(b) Suppose that an ML algorithm makes a decision that leads to a loss. The
algorithm did what it was programmed to do, and the investor agreed to the
terms of the program, as verified by forensic examination of the computer
logs. In what sense is this situation better for the investor, compared to a
loss caused by a discretionary PM’s poor judgment? What is the investor’s
recourse in each instance?
(c) Would it make sense for financial advisors to benchmark their decisions
against the decisions made by such neutral agents?
--- page 47 ---

20
FINANCIAL MACHINE LEARNING AS A DISTINCT SUBJECT
REFERENCES
Bailey, D., P. Borwein, and S. Plouffe (1997): “On the rapid computation of various polylogarithmic
constants.” Mathematics of Computation, Vol. 66, No. 218, pp. 903–913.
Calkin, N. and M. L´opez de Prado (2014a): “Stochastic flow diagrams.” Algorithmic Finance, Vol.
3, No. 1, pp. 21–42.
Calkin, N. and M. L´opez de Prado (2014b): “The topology of macro financial flows: An application
of stochastic flow diagrams.” Algorithmic Finance, Vol. 3, No. 1, pp. 43–85.
Easley, D., M. L´opez de Prado, and M. O’Hara (2013): High-Frequency Trading, 1st ed. Risk Books.
L´opez de Prado, M. (2014): “Quantitative meta-strategies.” Practical Applications, Institutional
Investor Journals, Vol. 2, No. 3, pp. 1–3.
L´opez de Prado, M. (2015): “The Future of Empirical Finance.” Journal of Portfolio Management,
Vol. 41, No. 4, pp. 140–144.
Stigler, Stephen M. (1981): “Gauss and the invention of least squares.” Annals of Statistics, Vol. 9,
No. 3, pp. 465–474.
BIBLIOGRAPHY
Abu-Mostafa, Y., M. Magdon-Ismail, and H. Lin (2012): Learning from Data, 1st ed. AMLBook.
Akansu, A., S. Kulkarni, and D. Malioutov (2016): Financial Signal Processing and Machine Learning, 1st ed. John Wiley & Sons-IEEE Press.
Aronson, D. and T. Masters (2013): Statistically Sound Machine Learning for Algorithmic Trading
of Financial Instruments: Developing Predictive-Model-Based Trading Systems Using TSSB,
1st ed. CreateSpace Independent Publishing Platform.
Boyarshinov, V. (2012): Machine Learning in Computational Finance: Practical Algorithms for
Building Artificial Intelligence Applications, 1st ed. LAP LAMBERT Academic Publishing.
Cerniglia, J., F. Fabozzi, and P. Kolm (2016): “Best practices in research for quantitative equity
strategies.” Journal of Portfolio Management, Vol. 42, No. 5, pp. 135–143.
Chan, E. (2017): Machine Trading: Deploying Computer Algorithms to Conquer the Markets, 1st
ed. John Wiley & Sons.
Gareth, J., D. Witten, T. Hastie, and R. Tibshirani (2013): An Introduction to Statistical Learning:
with Applications in R, 1st ed. Springer.
Geron, A. (2017): Hands-On Machine Learning with Scikit-Learn and TensorFlow: Concepts, Tools,
and Techniques to Build Intelligent Systems, 1st ed. O’Reilly Media.
Gyorfi, L., G. Ottucsak, and H. Walk (2012): Machine Learning for Financial Engineering, 1st ed.
Imperial College Press.
Hackeling, G. (2014): Mastering Machine Learning with Scikit-Learn, 1st ed. Packt Publishing.
Hastie, T., R. Tibshirani, and J. Friedman (2016): The Elements of Statistical Learning, 2nd ed.
Springer-Verlag.
Hauck, T. (2014): Scikit-Learn Cookbook, 1st ed. Packt Publishing.
McNelis, P. (2005): Neural Networks in Finance, 1st ed. Academic Press.
Raschka, S. (2015): Python Machine Learning, 1st ed. Packt Publishing.
--- page 48 ---

P A R T 1
Data Analysis
Chapter 2: Financial Data Structures, 23
Chapter 3: Labeling, 43
Chapter 4: Sample Weights, 59
Chapter 5: Fractionally Differentiated Features, 75
21
--- page 49 ---
--- page 50 ---

CHAPTER 2
Financial Data Structures
2.1
MOTIVATION
In this chapter we will learn how to work with unstructured financial data, and from
that to derive a structured dataset amenable to ML algorithms. In general, you do not
want to consume someone else’s processed dataset, as the likely outcome will be that
you discover what someone else already knows or will figure out soon. Ideally your
starting point is a collection of unstructured, raw data that you are going to process
in a way that will lead to informative features.
2.2
ESSENTIAL TYPES OF FINANCIAL DATA
Financial data comes in many shapes and forms. Table 2.1 shows the four essential
types of financial data, ordered from left to right in terms of increasing diversity. Next,
we will discuss their different natures and applications.
2.2.1
Fundamental Data
Fundamental data encompasses information that can be found in regulatory filings
and business analytics. It is mostly accounting data, reported quarterly. A particular
aspect of this data is that it is reported with a lapse. You must confirm exactly when
each data point was released, so that your analysis uses that information only after
it was publicly available. A common beginner’s error is to assume that this data was
published at the end of the reporting period. That is never the case.
For example, fundamental data published by Bloomberg is indexed by the last date
included in the report, which precedes the date of the release (often by 1.5 months). In
other words, Bloomberg is assigning those values to a date when they were not known.
You could not believe how many papers are published every year using misaligned
23
--- page 51 ---

24
FINANCIAL DATA STRUCTURES
TABLE 2.1
The Four Essential Types of Financial Data
Fundamental Data
Market Data
Analytics
Alternative Data
r Assets
r Liabilities
r Sales
r Costs/earnings
r Macro variables
r . . .
r Price/yield/implied
volatility
r Volume
r Dividend/coupons
r Open interest
r Quotes/cancellations
r Aggressor side
r . . .
r Analyst
recommendations
r Credit ratings
r Earnings
expectations
r News sentiment
r . . .
r Satellite/CCTV
images
r Google searches
r Twitter/chats
r Metadata
r . . .
fundamental data, especially in the factor-investing literature. Once you align the data
correctly, a substantial number of findings in those papers cannot be reproduced.
A second aspect of fundamental data is that it is often backfilled or reinstated.
“Backfilling” means that missing data is assigned a value, even if those values were
unknown at that time. A “reinstated value” is a corrected value that amends an incorrect initial release. A company may issue multiple corrections for a past quarter’s
results long after the first publication, and data vendors may overwrite the initial values with their corrections. The problem is, the corrected values were not known on
that first release date. Some data vendors circumvent this problem by storing multiple
release dates and values for each variable. For example, we typically have three values for a single quarterly GDP release: the original released value and two monthly
revisions. Still, it is very common to find studies that use the final released value and
assign it to the time of the first release, or even to the last day in the reporting period.
We will revisit this mistake, and its implications, when we discuss backtesting errors
in Chapter 11.
Fundamental data is extremely regularized and low frequency. Being so accessible
to the marketplace, it is rather unlikely that there is much value left to be exploited.
Still, it may be useful in combination with other data types.
2.2.2
Market Data
Market data includes all trading activity that takes place in an exchange (like CME)
or trading venue (like MarketAxess). Ideally, your data provider has given you a raw
feed, with all sorts of unstructured information, like FIX messages that allow you
to fully reconstruct the trading book, or the full collection of BWIC (bids wanted
in competition) responses. Every market participant leaves a characteristic footprint
in the trading records, and with enough patience, you will find a way to anticipate
a competitor’s next move. For example, TWAP algorithms leave a very particular
footprint that is used by predatory algorithms to front-run their end-of-day trading
(usually hedging) activity (Easley, L´opez de Prado, and O’Hara [2011]). Human
GUI traders often trade in round lots, and you can use this fact to estimate what
percentage of the volume is coming from them at a given point in time, then associate
it with a particular market behavior.
--- page 52 ---

BARS
25
One appealing aspect of FIX data is that it is not trivial to process, unlike fundamental data. It is also very abundant, with over 10 TB being generated on a daily
basis. That makes it a more interesting dataset for strategy research.
2.2.3
Analytics
You could think of analytics as derivative data, based on an original source, which
could be fundamental, market, alternative, or even a collection of other analytics.
What characterizes analytics is not the content of the information, but that it is not
readily available from an original source, and that it has been processed for you in
a particular way. Investment banks and research firms sell valuable information that
results from in-depth analyses of companies’ business models, activities, competition,
outlook, etc. Some specialized firms sell statistics derived from alternative data, for
example, the sentiment extracted from news reports and social media.
A positive aspect of analytics is that the signal has been extracted for you from a
raw source. The negative aspects are that analytics may be costly, the methodology
used in their production may be biased or opaque, and you will not be the sole
consumer.
2.2.4
Alternative Data
Kolanovic and Krishnamachari [2017] differentiate among alternative data produced
by individuals (social media, news, web searches, etc.), business processes (transactions, corporate data, government agencies, etc.), and sensors (satellites, geolocation,
weather, CCTV, etc.). Some popular satellite image or video feeds include monitoring
of tankers, tunnel traffic activity, or parking lot occupancies.
What truly characterizes alternative data is that it is primary information, that is,
information that has not made it to the other sources. Before Exxon Mobile reported
increased earnings, before its market price shot up, before analysts wrote their commentary of their latest filings, before all of that, there were movements of tankers
and drillers and pipeline traffic. They happened months before those activities were
reflected in the other data types. Two problematic aspects of alternative data are their
cost and privacy concerns. All that spy craft is expensive, and the surveilled company
may object, not to mention bystanders.
Alternative data offers the opportunity to work with truly unique, hard-to-process
datasets. Remember, data that is hard to store, manipulate, and operate is always the
most promising. You will recognize that a dataset may be useful if it annoys your data
infrastructure team. Perhaps your competitors did not try to use it for logistic reasons,
gave up midway, or processed it incorrectly.
2.3
BARS
In order to apply ML algorithms on your unstructured data, we need to parse it,
extract valuable information from it, and store those extractions in a regularized
format. Most ML algorithms assume a table representation of the extracted data.
--- page 53 ---

26
FINANCIAL DATA STRUCTURES
Finance practitioners often refer to those tables’ rows as “bars.” We can distinguish
between two categories of bar methods: (1) standard bar methods, which are
common in the literature, and (2) more advanced, information-driven methods,
which sophisticated practitioners use although they cannot be found (yet) in journal
articles. In this section, we will discuss how to form those bars.
2.3.1
Standard Bars
Some bar construction methods are very popular in the financial industry, to the point
that most data vendors’ APIs offer several of them. The purpose of these methods is
to transform a series of observations that arrive at irregular frequency (often referred
to as “inhomogeneous series”) into a homogeneous series derived from regular
sampling.
2.3.1.1
Time Bars
Time bars are obtained by sampling information at fixed time intervals, e.g., once
every minute. The information collected usually includes:
r Timestamp
r Volume-weighted average price (VWAP)
r Open (i.e., first) price
r Close (i.e., last) price
r High price
r Low price
r Volume traded, etc.
Although time bars are perhaps the most popular among practitioners and academics, they should be avoided for two reasons. First, markets do not process information at a constant time interval. The hour following the open is much more active
than the hour around noon (or the hour around midnight in the case of futures). As
biological beings, it makes sense for humans to organize their day according to the
sunlight cycle. But today’s markets are operated by algorithms that trade with loose
human supervision, for which CPU processing cycles are much more relevant than
chronological intervals (Easley, L´opez de Prado, and O’Hara [2011]). This means that
time bars oversample information during low-activity periods and undersample information during high-activity periods. Second, time-sampled series often exhibit poor
statistical properties, like serial correlation, heteroscedasticity, and non-normality of
returns (Easley, L´opez de Prado, and O’Hara [2012]). GARCH models were developed, in part, to deal with the heteroscedasticity associated with incorrect sampling.
As we will see next, forming bars as a subordinated process of trading activity avoids
this problem in the first place.
2.3.1.2
Tick Bars
The idea behind tick bars is straightforward: The sample variables listed earlier
(timestamp, VWAP, open price, etc.) will be extracted each time a pre-defined number
--- page 54 ---

BARS
27
of transactions takes place, e.g., 1,000 ticks. This allows us to synchronize sampling
with a proxy of information arrival (the speed at which ticks are originated).
Mandelbrot and Taylor [1967] were among the first to realize that sampling as a
function of the number of transactions exhibited desirable statistical properties: “Price
changes over a fixed number of transactions may have a Gaussian distribution. Price
changes over a fixed time period may follow a stable Paretian distribution, whose
variance is infinite. Since the number of transactions in any time period is random,
the above statements are not necessarily in disagreement.”
Ever since Mandelbrot and Taylor’s paper, multiple studies have confirmed that
sampling as a function of trading activity allows us to achieve returns closer to IID
Normal (see An´e and Geman [2000]). This is important, because many statistical
methods rely on the assumption that observations are drawn from an IID Gaussian
process. Intuitively, we can only draw inference from a random variable that is invariant, and tick bars allow for better inference than time bars.
When constructing tick bars, you need to be aware of outliers. Many exchanges
carry out an auction at the open and an auction at the close. This means that for a
period of time, the order book accumulates bids and offers without matching them.
When the auction concludes, a large trade is published at the clearing price, for an
outsized amount. This auction trade could be the equivalent of thousands of ticks,
even though it is reported as one tick.
2.3.1.3
Volume Bars
One problem with tick bars is that order fragmentation introduces some arbitrariness
in the number of ticks. For example, suppose that there is one order sitting on the
offer, for a size of 10. If we buy 10 lots, our one order will be recorded as one tick.
If instead on the offer there are 10 orders of size 1, our one buy will be recorded as
10 separate transactions. In addition, matching engine protocols can further split one
fill into multiple artificial partial fills, as a matter of operational convenience.
Volume bars circumvent that problem by sampling every time a pre-defined
amount of the security’s units (shares, futures contracts, etc.) have been exchanged.
For example, we could sample prices every time a futures contract exchanges 1,000
units, regardless of the number of ticks involved.
It is hard to imagine these days, but back in the 1960s vendors rarely published
volume data, as customers were mostly concerned with tick prices. After volume
started to be reported as well, Clark [1973] realized that sampling returns by volume
achieved even better statistical properties (i.e., closer to an IID Gaussian distribution)
than sampling by tick bars. Another reason to prefer volume bars over time bars or
tick bars is that several market microstructure theories study the interaction between
prices and volume. Sampling as a function of one of these variables is a convenient
artifact for these analyses, as we will find out in Chapter 19.
2.3.1.4
Dollar Bars
Dollar bars are formed by sampling an observation every time a pre-defined market value is exchanged. Of course, the reference to dollars is meant to apply to the
--- page 55 ---

28
FINANCIAL DATA STRUCTURES
currency in which the security is denominated, but nobody refers to euro bars, pound
bars, or yen bars (although gold bars would make for a fun pun).
Let me illustrate the rationale behind dollar bars with a couple of examples. First,
suppose that we wish to analyze a stock that has exhibited an appreciation of 100%
over a certain period of time. Selling $1,000 worth of that stock at the end of the
period requires trading half the number of shares it took to buy $1,000 worth of that
stock at the beginning. In other words, the number of shares traded is a function
of the actual value exchanged. Therefore, it makes sense sampling bars in terms of
dollar value exchanged, rather than ticks or volume, particularly when the analysis
involves significant price fluctuations. This point can be verified empirically. If you
compute tick bars and volume bars on E-mini S&P 500 futures for a given bar size,
the number of bars per day will vary wildly over the years. That range and speed
of variation will be reduced once you compute the number of dollar bars per day
over the years, for a constant bar size. Figure 2.1 plots the exponentially weighted
average number of bars per day when we apply a fixed bar size on tick, volume,
and dollar sampling methods.
A second argument that makes dollar bars more interesting than time, tick, or
volume bars is that the number of outstanding shares often changes multiple times
over the course of a security’s life, as a result of corporate actions. Even after adjusting
for splits and reverse splits, there are other actions that will impact the amount of ticks
and volumes, like issuing new shares or buying back existing shares (a very common
practice since the Great Recession of 2008). Dollar bars tend to be robust in the face
of those actions. Still, you may want to sample dollar bars where the size of the bar is
not kept constant over time. Instead, the bar size could be adjusted dynamically as a
function of the free-floating market capitalization of a company (in the case of stocks),
or the outstanding amount of issued debt (in the case of fixed-income securities).
FIGURE 2.1
Average daily frequency of tick, volume, and dollar bars
--- page 56 ---

BARS
29
2.3.2
Information-Driven Bars
The purpose of information-driven bars is to sample more frequently when new information arrives to the market. In this context, the word “information” is used in a market microstructural sense. As we will see in Chapter 19, market microstructure theories confer special importance to the persistence of imbalanced signed volumes, as
that phenomenon is associated with the presence of informed traders. By synchronizing sampling with the arrival of informed traders, we may be able to make decisions
before prices reach a new equilibrium level. In this section we will explore how to
use various indices of information arrival to sample bars.
2.3.2.1
Tick Imbalance Bars
Consider a sequence of ticks {(pt, vt)}t=1,…,T, where pt is the price associated with
tick t and vt is the volume associated with tick t. The so-called tick rule defines a
sequence {bt}t=1,…,T where
bt =
⎧
⎪
⎨
⎪⎩
bt−1
if Δpt = 0
||Δpt||
Δpt
if Δpt ≠0
with bt ∈{−1, 1}, and the boundary condition b0 is set to match the terminal value bT
from the immediately preceding bar. The idea behind tick imbalance bars (TIBs) is to
sample bars whenever tick imbalances exceed our expectations. We wish to determine
the tick index, T, such that the accumulation of signed ticks (signed according to the
tick rule) exceeds a given threshold. Next, let us discuss the procedure to determine T.
First, we define the tick imbalance at time T as
𝜃T =
T
∑
t=1
bt
Second, we compute the expected value of 𝜃T at the beginning of the bar, E0[𝜃T] =
E0[T](P[bt = 1] −P[bt = −1]), where E0[T] is the expected size of the tick bar,
P[bt = 1] is the unconditional probability that a tick is classified as a buy, and
P[bt = −1] is the unconditional probability that a tick is classified as a sell. Since
P[bt = 1] + P[bt = −1] = 1, then E0[𝜃T] = E0[T](2P[bt = 1] −1). In practice, we
can estimate E0[T] as an exponentially weighted moving average of T values from
prior bars, and (2P[bt = 1] −1) as an exponentially weighted moving average of bt
values from prior bars.
Third, we define a tick imbalance bar (TIB) as a T∗-contiguous subset of ticks
such that the following condition is met:
T∗= arg min
T
{
||𝜃T|| ≥E0 [T] |||2P [bt = 1] −1|||
}
--- page 57 ---

30
FINANCIAL DATA STRUCTURES
where the size of the expected imbalance is implied by |2P[bt = 1] −1|. When 𝜃T
is more imbalanced than expected, a low T will satisfy these conditions. Accordingly, TIBs are produced more frequently under the presence of informed trading
(asymmetric information that triggers one-side trading). In fact, we can understand
TIBs as buckets of trades containing equal amounts of information (regardless of the
volumes, prices, or ticks traded).
2.3.2.2
Volume/Dollar Imbalance Bars
The idea behind volume imbalance bars (VIBs) and dollar imbalance bars (DIBs) is
to extend the concept of tick imbalance bars (TIBs). We would like to sample bars
when volume or dollar imbalances diverge from our expectations. Based on the same
notions of tick rule and boundary condition b0 as we discussed for TIBs, we will
define a procedure to determine the index of the next sample, T.
First, we define the imbalance at time T as
𝜃T =
T
∑
t=1
btvt
where vt may represent either the number of securities traded (VIB) or the dollar
amount exchanged (DIB). Your choice of vt is what determines whether you are sampling according to the former or the latter.
Second, we compute the expected value of 𝜃T at the beginning of the bar
E0[𝜃T] = E0
[
T∑
t|bt=1
vt
]
−E0
[
T∑
t|bt=−1
vt
]
= E0[T](P[bt = 1]E0[vt|bt = 1]
−P[bt = −1]E0[vt|bt = −1])
Let us denote v+ = P[bt = 1]E0[vt|bt = 1], v−= P[bt = −1]E0[vt|bt = −1], so
that E0[T]−1E0[∑
t vt] = E0[vt] = v+ + v−. You can think of v+ and v−as decomposing the initial expectation of vt into the component contributed by buys and the
component contributed by sells. Then
E0[𝜃T] = E0[T](v+ −v−) = E0[T](2v+ −E0[vt])
In practice, we can estimate E0[T] as an exponentially weighted moving average
of T values from prior bars, and (2v+ −E0[vt]) as an exponentially weighted moving
average of btvt values from prior bars.
Third, we define VIB or DIB as a T∗-contiguous subset of ticks such that the
following condition is met:
T∗= arg min
T
{|𝜃T| ≥E0[T]|2v+ −E0[vt]|}
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
