# Advances in Financial Machine Learning.pdf — pages 1–20

--- page 1 ---
--- page 2 ---

Praise for Advances in Financial Machine Learning
In his new book Advances in Financial Machine Learning, noted financial scholar
Marcos L´opez de Prado strikes a well-aimed karate chop at the naive and often statistically overfit techniques that are so prevalent in the financial world today. He points
out that not only are business-as-usual approaches largely impotent in today’s hightech finance, but in many cases they are actually prone to lose money. But L´opez de
Prado does more than just expose the mathematical and statistical sins of the finance
world. Instead, he offers a technically sound roadmap for finance professionals to join
the wave of machine learning. What is particularly refreshing is the author’s empirical
approach—his focus is on real-world data analysis, not on purely theoretical methods that may look pretty on paper but which, in many cases, are largely ineffective in
practice. The book is geared to finance professionals who are already familiar with
statistical data analysis techniques, but it is well worth the effort for those who want
to do real state-of-the-art work in the field.”
Dr. David H. Bailey, former Complex Systems Lead,
Lawrence Berkeley National Laboratory. Co-discoverer of the
BBP spigot algorithm
“Finance has evolved from a compendium of heuristics based on historical financial
statements to a highly sophisticated scientific discipline relying on computer farms
to analyze massive data streams in real time. The recent highly impressive advances
in machine learning (ML) are fraught with both promise and peril when applied to
modern finance. While finance offers up the nonlinearities and large data sets upon
which ML thrives, it also offers up noisy data and the human element which presently
lie beyond the scope of standard ML techniques. To err is human, but if you really
want to f**k things up, use a computer. Against this background, Dr. L´opez de Prado
has written the first comprehensive book describing the application of modern ML
to financial modeling. The book blends the latest technological developments in ML
with critical life lessons learned from the author’s decades of financial experience in
leading academic and industrial institutions. I highly recommend this exciting book
to both prospective students of financial ML and the professors and supervisors who
teach and guide them.”
Prof. Peter Carr, Chair of the Finance and Risk Engineering
Department, NYU Tandon School of Engineering
“Marcos is a visionary who works tirelessly to advance the finance field. His writing is
comprehensive and masterfully connects the theory to the application. It is not often
you find a book that can cross that divide. This book is an essential read for both
practitioners and technologists working on solutions for the investment community.”
Landon Downs, President and Cofounder, 1QBit
“Academics who want to understand modern investment management need to read
this book. In it, Marcos L´opez de Prado explains how portfolio managers use machine
learning to derive, test, and employ trading strategies. He does this from a very
unusual combination of an academic perspective and extensive experience in industry, allowing him to both explain in detail what happens in industry and to explain
--- page 3 ---

how it works. I suspect that some readers will find parts of the book that they do not
understand or that they disagree with, but everyone interested in understanding the
application of machine learning to finance will benefit from reading this book.”
Prof. David Easley, Cornell University. Chair of the
NASDAQ-OMX Economic Advisory Board
“For many decades, finance has relied on overly simplistic statistical techniques
to identify patterns in data. Machine learning promises to change that by allowing
researchers to use modern nonlinear and highly dimensional techniques, similar to
those used in scientific fields like DNA analysis and astrophysics. At the same time,
applying those machine learning algorithms to model financial problems would be
dangerous. Financial problems require very distinct machine learning solutions.
Dr. L´opez de Prado’s book is the first one to characterize what makes standard
machine learning tools fail when applied to the field of finance, and the first one to
provide practical solutions to unique challenges faced by asset managers. Everyone
who wants to understand the future of finance should read this book.”
Prof. Frank Fabozzi, EDHEC Business School. Editor of
The Journal of Portfolio Management
“This is a welcome departure from the knowledge hoarding that plagues quantitative
finance. L´opez de Prado defines for all readers the next era of finance: industrial scale
scientific research powered by machines.”
John Fawcett, Founder and CEO, Quantopian
“Marcos has assembled in one place an invaluable set of lessons and techniques for
practitioners seeking to deploy machine learning techniques in finance. If machine
learning is a new and potentially powerful weapon in the arsenal of quantitative
finance, Marcos’s insightful book is laden with useful advice to help keep a curious practitioner from going down any number of blind alleys, or shooting oneself in
the foot.”
Ross Garon, Head of Cubist Systematic Strategies. Managing
Director, Point72 Asset Management
“The first wave of quantitative innovation in finance was led by Markowitz optimization. Machine Learning is the second wave, and it will touch every aspect of finance.
L´opez de Prado’s Advances in Financial Machine Learning is essential for readers
who want to be ahead of the technology rather than being replaced by it.”
Prof. Campbell Harvey, Duke University. Former President of
the American Finance Association
“How does one make sense of todays’ financial markets in which complex algorithms route orders, financial data is voluminous, and trading speeds are measured
in nanoseconds? In this important book, Marcos L´opez de Prado sets out a new
paradigm for investment management built on machine learning. Far from being a
“black box” technique, this book clearly explains the tools and process of financial
--- page 4 ---

machine learning. For academics and practitioners alike, this book fills an important
gap in our understanding of investment management in the machine age.”
Prof. Maureen O’Hara, Cornell University. Former President of
the American Finance Association
“Marcos L´opez de Prado has produced an extremely timely and important book on
machine learning. The author’s academic and professional first-rate credentials shine
through the pages of this book—indeed, I could think of few, if any, authors better
suited to explaining both the theoretical and the practical aspects of this new and
(for most) unfamiliar subject. Both novices and experienced professionals will find
insightful ideas, and will understand how the subject can be applied in novel and useful ways. The Python code will give the novice readers a running start and will allow
them to gain quickly a hands-on appreciation of the subject. Destined to become a
classic in this rapidly burgeoning field.”
Prof. Riccardo Rebonato, EDHEC Business School. Former
Global Head of Rates and FX Analytics at PIMCO
“A tour de force on practical aspects of machine learning in finance, brimming with
ideas on how to employ cutting-edge techniques, such as fractional differentiation
and quantum computers, to gain insight and competitive advantage. A useful volume
for finance and machine learning practitioners alike.”
Dr. Collin P. Williams, Head of Research, D-Wave Systems
--- page 5 ---
--- page 6 ---

Advances in Financial Machine Learning
--- page 7 ---
--- page 8 ---

Advances in Financial
Machine Learning
MARCOS L ´OPEZ DE PRADO
--- page 9 ---

Cover image: © Erikona/Getty Images
Cover design: Wiley
Copyright © 2018 by John Wiley & Sons, Inc. All rights reserved.
Published by John Wiley & Sons, Inc., Hoboken, New Jersey.
Published simultaneously in Canada.
The views expressed in this book are the author’s and do not necessarily reflect those of the organizations
he is affiliated with.
No part of this publication may be reproduced, stored in a retrieval system, or transmitted in any form or
by any means, electronic, mechanical, photocopying, recording, scanning, or otherwise, except as
permitted under Section 107 or 108 of the 1976 United States Copyright Act, without either the prior
written permission of the Publisher, or authorization through payment of the appropriate per-copy fee to
the Copyright Clearance Center, Inc., 222 Rosewood Drive, Danvers, MA 01923, (978) 750-8400, fax
(978) 646-8600, or on the Web at www.copyright.com. Requests to the Publisher for permission should
be addressed to the Permissions Department, John Wiley & Sons, Inc., 111 River Street, Hoboken, NJ
07030, (201) 748-6011, fax (201) 748-6008, or online at www.wiley.com/go/permissions.
Limit of Liability/Disclaimer of Warranty: While the publisher and author have used their best efforts in
preparing this book, they make no representations or warranties with respect to the accuracy or
completeness of the contents of this book and specifically disclaim any implied warranties of
merchantability or fitness for a particular purpose. No warranty may be created or extended by sales
representatives or written sales materials. The advice and strategies contained herein may not be suitable
for your situation. You should consult with a professional where appropriate. Neither the publisher nor
author shall be liable for any loss of profit or any other commercial damages, including but not limited to
special, incidental, consequential, or other damages. The views expressed in this book are the author’s
and do not necessarily reflect those of the organizations he is affiliated with.
For general information on our other products and services or for technical support, please contact our
Customer Care Department within the United States at (800) 762-2974, outside the United States at
(317) 572-3993, or fax (317) 572-4002.
Wiley publishes in a variety of print and electronic formats and by print-on-demand. Some material
included with standard print versions of this book may not be included in e-books or in print-on-demand.
If this book refers to media such as a CD or DVD that is not included in the version you purchased, you
may download this material at http://booksupport.wiley.com. For more information about Wiley
products, visit www.wiley.com.
ISBN 978-1-119-48208-6 (Hardcover)
ISBN 978-1-119-48211-6 (ePDF)
ISBN 978-1-119-48210-9 (ePub)
Printed in the United States of America
10
9
8
7
6
5
4
3
2
1
--- page 10 ---

Dedicated to the memory of my coauthor and friend,
Professor Jonathan M. Borwein, FRSC, FAAAS,
FBAS, FAustMS, FAA, FAMS, FRSNSW
(1951–2016)
--- page 11 ---
--- page 12 ---

There are very few things which we know, which are not capable of
being reduced to a mathematical reasoning. And when they cannot,
it’s a sign our knowledge of them is very small and confused. Where a
mathematical reasoning can be had, it’s as great a folly to make use of
any other, as to grope for a thing in the dark, when you have a candle
standing by you.
—Of the Laws of Chance, Preface (1692)
John Arbuthnot (1667–1735)
--- page 13 ---
--- page 14 ---

Contents
About the Author
xxi
PREAMBLE
1
1
Financial Machine Learning as a Distinct Subject
3
1.1
Motivation, 3
1.2
The Main Reason Financial Machine Learning Projects Usually Fail, 4
1.2.1
The Sisyphus Paradigm, 4
1.2.2
The Meta-Strategy Paradigm, 5
1.3
Book Structure, 6
1.3.1
Structure by Production Chain, 6
1.3.2
Structure by Strategy Component, 9
1.3.3
Structure by Common Pitfall, 12
1.4
Target Audience, 12
1.5
Requisites, 13
1.6
FAQs, 14
1.7
Acknowledgments, 18
Exercises, 19
References, 20
Bibliography, 20
PART 1
DATA ANALYSIS
21
2
Financial Data Structures
23
2.1
Motivation, 23
ix
--- page 15 ---

x
CONTENTS
2.2
Essential Types of Financial Data, 23
2.2.1
Fundamental Data, 23
2.2.2
Market Data, 24
2.2.3
Analytics, 25
2.2.4
Alternative Data, 25
2.3
Bars, 25
2.3.1
Standard Bars, 26
2.3.2
Information-Driven Bars, 29
2.4
Dealing with Multi-Product Series, 32
2.4.1
The ETF Trick, 33
2.4.2
PCA Weights, 35
2.4.3
Single Future Roll, 36
2.5
Sampling Features, 38
2.5.1
Sampling for Reduction, 38
2.5.2
Event-Based Sampling, 38
Exercises, 40
References, 41
3
Labeling
43
3.1
Motivation, 43
3.2
The Fixed-Time Horizon Method, 43
3.3
Computing Dynamic Thresholds, 44
3.4
The Triple-Barrier Method, 45
3.5
Learning Side and Size, 48
3.6
Meta-Labeling, 50
3.7
How to Use Meta-Labeling, 51
3.8
The Quantamental Way, 53
3.9
Dropping Unnecessary Labels, 54
Exercises, 55
Bibliography, 56
4
Sample Weights
59
4.1
Motivation, 59
4.2
Overlapping Outcomes, 59
4.3
Number of Concurrent Labels, 60
4.4
Average Uniqueness of a Label, 61
4.5
Bagging Classifiers and Uniqueness, 62
4.5.1
Sequential Bootstrap, 63
4.5.2
Implementation of Sequential Bootstrap, 64
--- page 16 ---

CONTENTS
xi
4.5.3
A Numerical Example, 65
4.5.4
Monte Carlo Experiments, 66
4.6
Return Attribution, 68
4.7
Time Decay, 70
4.8
Class Weights, 71
Exercises, 72
References, 73
Bibliography, 73
5
Fractionally Differentiated Features
75
5.1
Motivation, 75
5.2
The Stationarity vs. Memory Dilemma, 75
5.3
Literature Review, 76
5.4
The Method, 77
5.4.1
Long Memory, 77
5.4.2
Iterative Estimation, 78
5.4.3
Convergence, 80
5.5
Implementation, 80
5.5.1
Expanding Window, 80
5.5.2
Fixed-Width Window Fracdiff, 82
5.6
Stationarity with Maximum Memory Preservation, 84
5.7
Conclusion, 88
Exercises, 88
References, 89
Bibliography, 89
PART 2
MODELLING
91
6
Ensemble Methods
93
6.1
Motivation, 93
6.2
The Three Sources of Errors, 93
6.3
Bootstrap Aggregation, 94
6.3.1
Variance Reduction, 94
6.3.2
Improved Accuracy, 96
6.3.3
Observation Redundancy, 97
6.4
Random Forest, 98
6.5
Boosting, 99
--- page 17 ---

xii
CONTENTS
6.6
Bagging vs. Boosting in Finance, 100
6.7
Bagging for Scalability, 101
Exercises, 101
References, 102
Bibliography, 102
7
Cross-Validation in Finance
103
7.1
Motivation, 103
7.2
The Goal of Cross-Validation, 103
7.3
Why K-Fold CV Fails in Finance, 104
7.4
A Solution: Purged K-Fold CV, 105
7.4.1
Purging the Training Set, 105
7.4.2
Embargo, 107
7.4.3
The Purged K-Fold Class, 108
7.5
Bugs in Sklearn’s Cross-Validation, 109
Exercises, 110
Bibliography, 111
8
Feature Importance
113
8.1
Motivation, 113
8.2
The Importance of Feature Importance, 113
8.3
Feature Importance with Substitution Effects, 114
8.3.1
Mean Decrease Impurity, 114
8.3.2
Mean Decrease Accuracy, 116
8.4
Feature Importance without Substitution Effects, 117
8.4.1
Single Feature Importance, 117
8.4.2
Orthogonal Features, 118
8.5
Parallelized vs. Stacked Feature Importance, 121
8.6
Experiments with Synthetic Data, 122
Exercises, 127
References, 127
9
Hyper-Parameter Tuning with Cross-Validation
129
9.1
Motivation, 129
9.2
Grid Search Cross-Validation, 129
9.3
Randomized Search Cross-Validation, 131
9.3.1
Log-Uniform Distribution, 132
9.4
Scoring and Hyper-parameter Tuning, 134
--- page 18 ---

CONTENTS
xiii
Exercises, 135
References, 136
Bibliography, 137
PART 3
BACKTESTING
139
10
Bet Sizing
141
10.1
Motivation, 141
10.2
Strategy-Independent Bet Sizing Approaches, 141
10.3
Bet Sizing from Predicted Probabilities, 142
10.4
Averaging Active Bets, 144
10.5
Size Discretization, 144
10.6
Dynamic Bet Sizes and Limit Prices, 145
Exercises, 148
References, 149
Bibliography, 149
11
The Dangers of Backtesting
151
11.1
Motivation, 151
11.2
Mission Impossible: The Flawless Backtest, 151
11.3
Even If Your Backtest Is Flawless, It Is Probably Wrong, 152
11.4
Backtesting Is Not a Research Tool, 153
11.5
A Few General Recommendations, 153
11.6
Strategy Selection, 155
Exercises, 158
References, 158
Bibliography, 159
12
Backtesting through Cross-Validation
161
12.1
Motivation, 161
12.2
The Walk-Forward Method, 161
12.2.1
Pitfalls of the Walk-Forward Method, 162
12.3
The Cross-Validation Method, 162
12.4
The Combinatorial Purged Cross-Validation Method, 163
12.4.1
Combinatorial Splits, 164
12.4.2
The Combinatorial Purged Cross-Validation
Backtesting Algorithm, 165
12.4.3
A Few Examples, 165
--- page 19 ---

xiv
CONTENTS
12.5
How Combinatorial Purged Cross-Validation Addresses
Backtest Overfitting, 166
Exercises, 167
References, 168
13
Backtesting on Synthetic Data
169
13.1
Motivation, 169
13.2
Trading Rules, 169
13.3
The Problem, 170
13.4
Our Framework, 172
13.5
Numerical Determination of Optimal Trading Rules, 173
13.5.1
The Algorithm, 173
13.5.2
Implementation, 174
13.6
Experimental Results, 176
13.6.1
Cases with Zero Long-Run Equilibrium, 177
13.6.2
Cases with Positive Long-Run Equilibrium, 180
13.6.3
Cases with Negative Long-Run Equilibrium, 182
13.7
Conclusion, 192
Exercises, 192
References, 193
14
Backtest Statistics
195
14.1
Motivation, 195
14.2
Types of Backtest Statistics, 195
14.3
General Characteristics, 196
14.4
Performance, 198
14.4.1
Time-Weighted Rate of Return, 198
14.5
Runs, 199
14.5.1
Returns Concentration, 199
14.5.2
Drawdown and Time under Water, 201
14.5.3
Runs Statistics for Performance Evaluation, 201
14.6
Implementation Shortfall, 202
14.7
Efficiency, 203
14.7.1
The Sharpe Ratio, 203
14.7.2
The Probabilistic Sharpe Ratio, 203
14.7.3
The Deflated Sharpe Ratio, 204
14.7.4
Efficiency Statistics, 205
14.8
Classification Scores, 206
14.9
Attribution, 207
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
