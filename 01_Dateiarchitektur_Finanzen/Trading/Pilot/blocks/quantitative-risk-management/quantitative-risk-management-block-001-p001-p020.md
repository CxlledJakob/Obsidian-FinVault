# Quantitative Risk Management_ Concepts, Techniques, and -- Alexander J_ McNeil, Rüdiger Frey, Paul Embrechts -- Princeton series in finance, -- isbn13 9780691122557 -- 478a0059673fecd0c76229cd3d8884e7 -- Anna’s Arc.pdf — pages 1–20

--- page 1 ---

Quantitative Risk Management
--- page 2 ---

Quantitative Risk Management: Concepts, Techniques and Tools
is a part of the
Princeton Series in Finance
Series Editors
Darrell Dufﬁe
Stephen Schaefer
Stanford University
London Business School
Finance as a discipline has been growing rapidly. The numbers of researchers in
academy and industry, of students, of methods and models have all proliferated in
the past decade or so. This growth and diversity manifests itself in the emerging
cross-disciplinary as well as cross-national mix of scholarship now driving the ﬁeld
of ﬁnance forward. The intellectual roots of modern ﬁnance, as well as the branches,
will be represented in the Princeton Series in Finance.
Titles in this series will be scholarly and professional books, intended to be read
by a mixed audience of economists, mathematicians, operations research scientists, ﬁnancial engineers, and other investment professionals. The goal is to provide the ﬁnest cross-disciplinary work in all areas of ﬁnance by widely recognized
researchers in the prime of their creative careers.
Other Books in This Series
Financial Econometrics: Problems, Models, and Methods by Christian Gourieroux
and Joann Jasiak
Credit Risk: Pricing, Measurement, and Management by Darrell Dufﬁe and Kenneth
J. Singleton
Microfoundations of Financial Economics: An Introduction to General Equilibrium
Asset Pricing by Yvan Lengwiler
Credit Risk Modeling: Theory and Applications by David Lando
--- page 3 ---

Quantitative Risk Management
Concepts, Techniques and Tools
Alexander J. McNeil
R¨udiger Frey
Paul Embrechts
Princeton University Press
Princeton and Oxford
--- page 4 ---

Copyright c⃝2005 by Princeton University Press
Published by Princeton University Press,
41 William Street, Princeton, New Jersey 08540
In the United Kingdom: Princeton University Press,
3 Market Place, Woodstock, Oxfordshire OX20 1SY
All rights reserved
Library of Congress Cataloguing-in-Publication Data
McNeil, Alexander J., 1967–
Quantitative risk management : concepts, techniques, and tools /Alexander J.
McNeil, R¨udiger Frey, Paul Embrechts
p.cm.—(Princeton series in ﬁnance)
Includes bibliographical references and index.
ISBN 0-691-12255-5 (cloth : alk. paper)
1. Risk management—Mathematical models. 2. Finance—Mathematical
models. 3. Insurance—Mathematical models. 4. Mathematical statistics.
I. Frey, R¨udiger. II. Embrechts, Paul. III. Title. IV. Series.
HD61.M395 2005
658.15′5′0151—pcc22
2005049603
British Library Cataloguing-in-Publication Data
A catalogue record for this book is available from the British Library
This book has been composed in Times and typeset by T&T Productions Ltd, London
Printed on acid-free paper ⃝
∞
www.pup.princeton.edu
Printed in the United States of America
10 9 8 7 6 5 4 3 2 1
--- page 5 ---

To Janine, Alexander and Calliope
Alexander
F¨ur Catharina und Sebastian
R¨udiger
Voor Gerda, Rita en Guy
Paul
--- page 6 ---
--- page 7 ---

Contents
Preface
xiii
1
Risk in Perspective
1
1.1
Risk
1
1.1.1
Risk and Randomness
1
1.1.2
Financial Risk
2
1.1.3
Measurement and Management
3
1.2
A Brief History of Risk Management
5
1.2.1
From Babylon to Wall Street
5
1.2.2
The Road to Regulation
8
1.3
The New Regulatory Framework
10
1.3.1
Basel II
10
1.3.2
Solvency 2
13
1.4
Why Manage Financial Risk?
15
1.4.1
A Societal View
15
1.4.2
The Shareholder’s View
16
1.4.3
Economic Capital
18
1.5
Quantitative Risk Management
19
1.5.1
The Nature of the Challenge
19
1.5.2
QRM for the Future
22
2
Basic Concepts in Risk Management
25
2.1
Risk Factors and Loss Distributions
25
2.1.1
General Deﬁnitions
25
2.1.2
Conditional and Unconditional Loss Distribution
28
2.1.3
Mapping of Risks: Some Examples
29
2.2
Risk Measurement
34
2.2.1
Approaches to Risk Measurement
34
2.2.2
Value-at-Risk
37
2.2.3
Further Comments on VaR
40
2.2.4
Other Risk Measures Based on Loss Distributions
43
2.3
Standard Methods for Market Risks
48
2.3.1
Variance–Covariance Method
48
2.3.2
Historical Simulation
50
2.3.3
Monte Carlo
52
2.3.4
Losses over Several Periods and Scaling
53
2.3.5
Backtesting
55
2.3.6
An Illustrative Example
55
--- page 8 ---

viii
Contents
3
Multivariate Models
61
3.1
Basics of Multivariate Modelling
61
3.1.1
Random Vectors and Their Distributions
62
3.1.2
Standard Estimators of Covariance and Correlation
64
3.1.3
The Multivariate Normal Distribution
66
3.1.4
Testing Normality and Multivariate Normality
68
3.2
Normal Mixture Distributions
73
3.2.1
Normal Variance Mixtures
73
3.2.2
Normal Mean-Variance Mixtures
77
3.2.3
Generalized Hyperbolic Distributions
78
3.2.4
Fitting Generalized Hyperbolic Distributions to Data
81
3.2.5
Empirical Examples
84
3.3
Spherical and Elliptical Distributions
89
3.3.1
Spherical Distributions
89
3.3.2
Elliptical Distributions
93
3.3.3
Properties of Elliptical Distributions
95
3.3.4
Estimating Dispersion and Correlation
96
3.3.5
Testing for Elliptical Symmetry
99
3.4
Dimension Reduction Techniques
103
3.4.1
Factor Models
103
3.4.2
Statistical Calibration Strategies
105
3.4.3
Regression Analysis of Factor Models
106
3.4.4
Principal Component Analysis
109
4
Financial Time Series
116
4.1
Empirical Analyses of Financial Time Series
117
4.1.1
Stylized Facts
117
4.1.2
Multivariate Stylized Facts
123
4.2
Fundamentals of Time Series Analysis
125
4.2.1
Basic Deﬁnitions
125
4.2.2
ARMA Processes
128
4.2.3
Analysis in the Time Domain
132
4.2.4
Statistical Analysis of Time Series
134
4.2.5
Prediction
136
4.3
GARCH Models for Changing Volatility
139
4.3.1
ARCH Processes
139
4.3.2
GARCH Processes
145
4.3.3
Simple Extensions of the GARCH Model
148
4.3.4
Fitting GARCH Models to Data
150
4.4
Volatility Models and Risk Estimation
158
4.4.1
Volatility Forecasting
158
4.4.2
Conditional Risk Measurement
160
4.4.3
Backtesting
162
4.5
Fundamentals of Multivariate Time Series
164
4.5.1
Basic Deﬁnitions
164
4.5.2
Analysis in the Time Domain
166
4.5.3
Multivariate ARMA Processes
168
4.6
Multivariate GARCH Processes
170
4.6.1
General Structure of Models
170
4.6.2
Models for Conditional Correlation
172
4.6.3
Models for Conditional Covariance
175
--- page 9 ---

Contents
ix
4.6.4
Fitting Multivariate GARCH Models
178
4.6.5
Dimension Reduction in MGARCH
179
4.6.6
MGARCH and Conditional Risk Measurement
182
5
Copulas and Dependence
184
5.1
Copulas
184
5.1.1
Basic Properties
185
5.1.2
Examples of Copulas
189
5.1.3
Meta Distributions
192
5.1.4
Simulation of Copulas and Meta Distributions
193
5.1.5
Further Properties of Copulas
195
5.1.6
Perfect Dependence
199
5.2
Dependence Measures
201
5.2.1
Linear Correlation
201
5.2.2
Rank Correlation
206
5.2.3
Coefﬁcients of Tail Dependence
208
5.3
Normal Mixture Copulas
210
5.3.1
Tail Dependence
210
5.3.2
Rank Correlations
215
5.3.3
Skewed Normal Mixture Copulas
217
5.3.4
Grouped Normal Mixture Copulas
218
5.4
Archimedean Copulas
220
5.4.1
Bivariate Archimedean Copulas
220
5.4.2
Multivariate Archimedean Copulas
222
5.4.3
Non-exchangeable Archimedean Copulas
224
5.5
Fitting Copulas to Data
228
5.5.1
Method-of-Moments using Rank Correlation
229
5.5.2
Forming a Pseudo-Sample from the Copula
232
5.5.3
Maximum Likelihood Estimation
234
6
Aggregate Risk
238
6.1
Coherent Measures of Risk
238
6.1.1
The Axioms of Coherence
238
6.1.2
Value-at-Risk
241
6.1.3
Coherent Risk Measures Based on Loss Distributions
243
6.1.4
Coherent Risk Measures as Generalized Scenarios
244
6.1.5
Mean-VaR Portfolio Optimization
246
6.2
Bounds for Aggregate Risks
248
6.2.1
The General Fr´echet Problem
248
6.2.2
The Case of VaR
250
6.3
Capital Allocation
256
6.3.1
The Allocation Problem
256
6.3.2
The Euler Principle and Examples
257
6.3.3
Economic Justiﬁcation of the Euler Principle
261
7
Extreme Value Theory
264
7.1
Maxima
264
7.1.1
Generalized Extreme Value Distribution
265
7.1.2
Maximum Domains of Attraction
267
7.1.3
Maxima of Strictly Stationary Time Series
270
7.1.4
The Block Maxima Method
271
--- page 10 ---

x
Contents
7.2
Threshold Exceedances
275
7.2.1
Generalized Pareto Distribution
275
7.2.2
Modelling Excess Losses
278
7.2.3
Modelling Tails and Measures of Tail Risk
282
7.2.4
The Hill Method
286
7.2.5
Simulation Study of EVT Quantile Estimators
289
7.2.6
Conditional EVT for Financial Time Series
291
7.3
Tails of Speciﬁc Models
293
7.3.1
Domain of Attraction of Fr´echet Distribution
293
7.3.2
Domain of Attraction of Gumbel Distribution
294
7.3.3
Mixture Models
295
7.4
Point Process Models
298
7.4.1
Threshold Exceedances for Strict White Noise
299
7.4.2
The POT Model
301
7.4.3
Self-Exciting Processes
306
7.4.4
A Self-Exciting POT Model
307
7.5
Multivariate Maxima
311
7.5.1
Multivariate Extreme Value Copulas
311
7.5.2
Copulas for Multivariate Minima
314
7.5.3
Copula Domains of Attraction
314
7.5.4
Modelling Multivariate Block Maxima
317
7.6
Multivariate Threshold Exceedances
319
7.6.1
Threshold Models Using EV Copulas
319
7.6.2
Fitting a Multivariate Tail Model
320
7.6.3
Threshold Copulas and Their Limits
322
8
Credit Risk Management
327
8.1
Introduction to Credit Risk Modelling
327
8.1.1
Credit Risk Models
327
8.1.2
The Nature of the Challenge
329
8.2
Structural Models of Default
331
8.2.1
The Merton Model
331
8.2.2
Pricing in Merton’s Model
332
8.2.3
The KMV Model
336
8.2.4
Models Based on Credit Migration
338
8.2.5
Multivariate Firm-Value Models
342
8.3
Threshold Models
343
8.3.1
Notation for One-Period Portfolio Models
344
8.3.2
Threshold Models and Copulas
345
8.3.3
Industry Examples
347
8.3.4
Models Based on Alternative Copulas
348
8.3.5
Model Risk Issues
350
8.4
The Mixture Model Approach
352
8.4.1
One-Factor Bernoulli Mixture Models
353
8.4.2
CreditRisk+
356
8.4.3
Asymptotics for Large Portfolios
357
8.4.4
Threshold Models as Mixture Models
359
8.4.5
Model-Theoretic Aspects of Basel II
362
8.4.6
Model Risk Issues
364
8.5
Monte Carlo Methods
367
8.5.1
Basics of Importance Sampling
367
8.5.2
Application to Bernoulli-Mixture Models
370
--- page 11 ---

Contents
xi
8.6
Statistical Inference for Mixture Models
374
8.6.1
Motivation
374
8.6.2
Exchangeable Bernoulli-Mixture Models
375
8.6.3
Mixture Models as GLMMs
377
8.6.4
One-Factor Model with Rating Effect
381
9
Dynamic Credit Risk Models
385
9.1
Credit Derivatives
386
9.1.1
Overview
386
9.1.2
Single-Name Credit Derivatives
387
9.1.3
Portfolio Credit Derivatives
389
9.2
Mathematical Tools
392
9.2.1
Random Times and Hazard Rates
393
9.2.2
Modelling Additional Information
395
9.2.3
Doubly Stochastic Random Times
397
9.3
Financial and Actuarial Pricing of Credit Risk
400
9.3.1
Physical and Risk-Neutral Probability Measure
401
9.3.2
Risk-Neutral Pricing and Market Completeness
405
9.3.3
Martingale Modelling
408
9.3.4
The Actuarial Approach to Credit Risk Pricing
411
9.4
Pricing with Doubly Stochastic Default Times
414
9.4.1
Recovery Payments of Corporate Bonds
414
9.4.2
The Model
415
9.4.3
Pricing Formulas
416
9.4.4
Applications
418
9.5
Afﬁne Models
421
9.5.1
Basic Results
422
9.5.2
The CIR Square-Root Diffusion
423
9.5.3
Extensions
425
9.6
Conditionally Independent Defaults
429
9.6.1
Reduced-Form Models for Portfolio Credit Risk
429
9.6.2
Conditionally Independent Default Times
431
9.6.3
Examples and Applications
435
9.7
Copula Models
440
9.7.1
Deﬁnition and General Properties
440
9.7.2
Factor Copula Models
444
9.8
Default Contagion in Reduced-Form Models
448
9.8.1
Default Contagion and Default Dependence
448
9.8.2
Information-Based Default Contagion
453
9.8.3
Interacting Intensities
456
10 Operational Risk and Insurance Analytics
463
10.1
Operational Risk in Perspective
463
10.1.1 A New Risk Class
463
10.1.2 The Elementary Approaches
465
10.1.3 Advanced Measurement Approaches
466
10.1.4 Operational Loss Data
468
10.2
Elements of Insurance Analytics
471
10.2.1 The Case for Actuarial Methodology
471
10.2.2 The Total Loss Amount
472
10.2.3 Approximations and Panjer Recursion
476
10.2.4 Poisson Mixtures
482
--- page 12 ---

xii
Contents
10.2.5 Tails of Aggregate Loss Distributions
484
10.2.6 The Homogeneous Poisson Process
484
10.2.7 Processes Related to the Poisson Process
487
Appendix
494
A.1
Miscellaneous Deﬁnitions and Results
494
A.1.1
Type of Distribution
494
A.1.2
Generalized Inverses and Quantiles
494
A.1.3
Karamata’s Theorem
495
A.2
Probability Distributions
496
A.2.1
Beta
496
A.2.2
Exponential
496
A.2.3
F
496
A.2.4
Gamma
496
A.2.5
Generalized Inverse Gaussian
497
A.2.6
Inverse Gamma
497
A.2.7
Negative Binomial
498
A.2.8
Pareto
498
A.2.9
Stable
498
A.3
Likelihood Inference
499
A.3.1
Maximum Likelihood Estimators
499
A.3.2
Asymptotic Results: Scalar Parameter
499
A.3.3
Asymptotic Results: Vector of Parameters
500
A.3.4
Wald Test and Conﬁdence Intervals
501
A.3.5
Likelihood Ratio Test and Conﬁdence Intervals
501
A.3.6
Akaike Information Criterion
502
References
503
Index
529
--- page 13 ---

Preface
Why have we written this book?
In recent decades the ﬁeld of ﬁnancial risk management has undergone explosive development. This book is devoted speciﬁcally to
quantitative modelling issues arising in this ﬁeld. As a result of our own discussions
and joint projects with industry professionals and regulators over a number of years,
we felt there was a need for a textbook treatment of quantitative risk management
(QRM) at a technical yet accessible level, aimed at both industry participants and
students seeking an entrance to the area.
We have tried to bring together a body of methodology that we consider to be core
material for any course on the subject. This material and its mode of presentation
represent the blending of our own views, which come from the perspectives of
ﬁnancial mathematics, insurance mathematics and statistics. We feel that a book
combining these viewpoints ﬁlls a gap in the existing literature and partly anticipates
the future need for quantitative risk managers in banks, insurance companies and
beyond with broad, interdisciplinary skills.
Who was this book written for?
This book is primarily a textbook for courses
on QRM aimed at advanced undergraduate or graduate students and professionals
from the ﬁnancial industry. A knowledge of probability and statistics at least at the
level of a ﬁrst university course in a quantitative discipline and familiarity with
undergraduate calculus and linear algebra are fundamental prerequisites. Though
not absolutely necessary, some prior exposure to ﬁnance, economics or insurance
will be beneﬁcial for a better understanding of some sections.
The book has a secondary function as a reference text for risk professionals interested in a clear and concise treatment of concepts and techniques used in practice.
As such, we hope it will facilitate communication between regulators, end-users and
academics.
A third audience for the book is the growing community of researchers working in
the area. Most chapters take the reader to the frontier of current, practically relevant
research and contain extensive, annotated references that guide the reader through
the burgeoning literature.
Ways to use this book.
Based on our experience of teaching university courses
on QRM at ETH Zurich, the Universities of Zurich and Leipzig and the London
School of Economics, a two-semester course of 3–4 hours a week can be based on
material in Chapters 2–8 and parts of Chapter 10; Chapter 1 is typically given as
background reading material. Chapter 9 is a more technically demanding chapter
that has been included because of the current interest in quantitative methods for
pricing and hedging credit derivatives; it is primarily intended for more advanced,
specialized courses on credit risk (see below).
--- page 14 ---

xiv
Preface
A course on market risk can be based on a fairly complete treatment of
Chapters 2–4, with excursions into material in Chapters 5, 6 and 7 (normal mixture
copulas, coherent risk measures, extreme value methods for threshold exceedances)
as time permits.
A course on credit risk can be based on Chapters 8 and 9 but requires a preliminary
treatment of some topics in earlier chapters. Sections 2.1 and 2.2 give the necessary
grounding in basic concepts; Sections 3.1, 3.2, 3.4, 5.1 and 5.4 are necessary for
an understanding of multivariate models of portfolio credit risk; and Sections 6.1
and 6.3 are required to understand how capital is allocated to credit risks.
A short course or seminar on operational risk could be based on Chapter 10,
but would also beneﬁt from some supplementary material from other chapters;
Sections 2.1 and 2.2 and Chapters 6 and 7 are particularly relevant.
It is also possible to devise more specialized courses, such as a course on riskmeasurement and aggregation concepts based on Chapters 2, 5 and 6, or a course on
risk-management techniques for ﬁnancial econometricians based on Chapters 2–4
and 7. Material from various chapters could be used as interesting examples to
enliven statistics courses on subjects like multivariate analysis, time series analysis
and generalized linear modelling.
What we have not covered.
We have not been able to address all topics that a reader
might expect to ﬁnd under the heading of QRM. Perhaps the most obvious omission
is the lack of a section on the risk management of derivatives by hedging.We felt here
that the relevant techniques, and the ﬁnancial mathematics required to understand
them, are already well covered in a number of excellent textbooks. Other omissions
include RAROC (risk-adjusted return on capital) and performance-measurement
issues. Besides these larger areas, many smaller issues have been neglected for
reasons of space, but are mentioned with suggestions for further reading in the
“Notes and Comments” sections, which should be considered as integral parts of
the text.
Acknowledgements.
The origins of this book date back to 1996, when A.M. and
R.F. began postdoctoral studies in the group of P.E. at the Federal Institute of Technology (ETH) in Zurich. All three authors are grateful to ETH for providing the
environment in which the project ﬂourished. A.M. and R.F. thank Swiss Re and
UBS, respectively, for providing the ﬁnancial support for their postdoctoral positions. R.F. has subsequently held positions at the Swiss Banking Institute of the
University of Zurich and at the University of Leipzig and is grateful to both institutions for their support.
The Forschungsinstitut f¨ur Mathematik (FIM) of the ETH Zurich provided ﬁnancial support at various stages of the project. At a crucial juncture in early 2004
the Mathematisches Foschungsinstitut Oberwolfach was the venue for a memorable
week of progress. P.E. recalls fondly his time as Centennial Professor of Finance at
the London School of Economics; numerous discussions with colleagues from the
Department ofAccounting and Finance helped in shaping his view of the importance
of QRM. We also acknowledge the invaluable contribution of RiskLab Zurich to the
--- page 15 ---

Preface
xv
enterprise: the agenda for the book was strongly inﬂuenced by joint projects and
discussions with the RiskLab sponsors UBS, Credit Suisse and Swiss Re. We have
also beneﬁted greatly from the NCCR FINRISK research program in Switzerland,
which funded doctoral and postdoctoral research on topics in the book.
We are indebted to numerous proof-readers who have commented on various
parts of the manuscript, and to colleagues in Zurich, Leipzig and beyond who
have helped us in our understanding of QRM and the mathematics underlying it.
These include StefanAltner, PhilippeArtzner, Jochen Backhaus, Guus Balkema, Uta
Beckmann, Reto Baumgartner,Wolfgang Breymann, Reto Bucher, Hans B¨uhlmann,
Peter B¨uhlmann, Val´erie Chavez-Demoulin, Dominik Colangelo, Freddy Delbaen,
Rosario Dell’Aquila, Stefan Denzler, Alexandra Dias, Stefano Demarta, Damir
Filipovic, Gabriel Frahm, Hansj¨org Furrer, Rajna Gibson, Kay Giesecke, Enrico
De Giorgi, Bernhard Hodler, Andrea H¨oing, Christoph Hummel, Alessandro Juri,
Roger Kaufmann, Philipp Keller, Hans Rudolf K¨unsch, Filip Lindskog, Hans-Jakob
L¨uthi, Natalia Markovich, Benoˆıt Metayer, Johanna Neˇslehov´a, Monika Popp,
Giovanni Puccetti, Hanspeter Schmidli, Sylvia Schmidt, Thorsten Schmidt, Uwe
Schmock, Philipp Sch¨onbucher, Martin Schweizer, Torsten Steiger, Daniel Straumann, Dirk Tasche, Eduardo Vilela, Marcel Visser and Jonathan Wendin. For her
help in preparing the manuscript we thank Gabriele Baltes.
We thank Richard Baggaley and the team at Princeton University Press for all
their help in the production of this book. We are also grateful to our anonymous
referees who provided us with exemplary feedback, which has shaped this book for
the better. Special thanks go to Sam Clark at T&T Productions Ltd, who took our
uneven LATEX code and turned it into a more polished book with remarkable speed
and efﬁciency.
To our wives, Janine, Catharina and Gerda, and our families our sincerest debt of
gratitude is due. Though driven to distraction no doubt by our long contemplation
of risk, without obvious reward, their support was constant.
Further resources.
Readers are encouraged to visit the book’s homepage at
www.pupress.princeton.edu/titles/8056.html
to ﬁnd supplementary resources for this book. Our intention is to make available the
computer code (mostly S-PLUS) used to generate the examples in this book, and to
list errata.
Special abbreviations.
A number of abbreviations for common terms in probability
are used throughout the book; these include “rv” for random variable, “df” for
distribution function, “iid” for independent and identically distributed and “se” for
standard error.
--- page 16 ---
--- page 17 ---

1
Risk in Perspective
In this chapter we provide a non-mathematical discussion of various issues that form
the background to the rest of the book. In Section 1.1 we begin with the nature of risk
itself and how risk relates to randomness; in the ﬁnancial context (which includes
insurance) we summarize the main kinds of risks encountered and explain what it
means to measure and manage such risks.
A brief history of ﬁnancial risk management, or at least some of the main ideas
that are used in modern practice, is given in Section 1.2, including a summary of the
process leading to the BaselAccords. Section 1.3 gives an idea of the new regulatory
framework that is emerging in the ﬁnancial and insurance industries.
In Section 1.4 we take a step back and attempt to address the fundamental question
of why we might want to measure and manage risk at all. Finally, in Section 1.5, we
turn explicitly to quantitative risk management (QRM) and set out our own views
concerning the nature of this discipline and the challenge it poses. This section in
particular should give more insight into why we have chosen to address the particular
methodological topics in this book.
1.1
Risk
The Concise Oxford English Dictionary deﬁnes risk as “hazard, a chance of bad
consequences, loss or exposure to mischance”. In a discussion with students taking a course on ﬁnancial risk management, ingredients which typically enter are
events, decisions, consequences and uncertainty. Mostly only the downside of risk
is mentioned, rarely a possible upside, i.e. the potential for a gain. For ﬁnancial
risks, the subject of this book, we might arrive at a deﬁnition such as “any event or
action that may adversely affect an organization’s ability to achieve its objectives
and execute its strategies” or, alternatively, “the quantiﬁable likelihood of loss or
less-than-expected returns”. But while these capture some of the elements of risk,
no single one-sentence deﬁnition is entirely satisfactory in all contexts.
1.1.1
Risk and Randomness
Independently of any context, risk relates strongly to uncertainty, and hence to the
notion of randomness. Randomness has eluded a clear, workable deﬁnition for many
centuries; it was not until 1933 that the Russian mathematician A. N. Kolmogorov
gave an axiomatic deﬁnition of randomness and probability (see Kolmogorov 1933).
This deﬁnition and its accompanying theory, though not without their controversial
--- page 18 ---

2
1. Risk in Perspective
aspects, now provide the lingua franca for discourses on risk and uncertainty, such
as this book.
In Kolmogorov’s language a probabilistic model is described by a triplet
(Ω, F , P). An element ω of Ωrepresents a realization of an experiment, in economics often referred to as a state of nature. The statement “the probability that
an event A occurs” is denoted (and in Kolmogorov’s axiomatic system deﬁned)
as P(A), where A is an element of F , the set of all events. P denotes the probability measure. For the less mathematically trained reader it sufﬁces to accept
that Kolmogorov’s system translates our intuition about randomness into a concise,
axiomatic language and clear rules.
Consider the following examples: an investor who holds stock in a particular
company; an insurance company that has sold an insurance policy; an individual
who decides to convert a ﬁxed-rate mortgage into a variable one. All of these situations have something important in common: the investor holds today an asset
with an uncertain future value. This is very clear in the case of the stock. For the
insurance company, the policy sold may or may not be triggered by the underlying event covered. In the case of a mortgage, our decision today to enter into this
reﬁnancing agreement will change (for better or for worse) the future repayments.
So randomness plays a crucial role in the valuation of current products held by the
investor, the insurance company or the home owner.
To model these situations a mathematician would now deﬁne a one-period risky
position (or simply risk) X to be a function on the probability space (Ω, F , P);
this function is called a random variable. We leave for the moment the range of X
(i.e. its possible values) unspeciﬁed. Most of the modelling of a risky position X
concerns its distribution function FX(x) = P(X ⩽x), the probability that by the
end of the period under consideration, the value of the risk X is less than or equal
to a given number x. Several risky positions would then be denoted by a random
vector (X1, . . . , Xd), also written in bold face as X; time can be introduced, leading
to the notion of random (or so-called stochastic) processes, usually written (Xt).
Throughout this book we will encounter many such processes, which serve as essential building blocks in the mathematical description of risk.
We therefore expect the reader to be at ease with basic notation, terminology and
results from elementary probability and statistics, the branch of mathematics dealing
with stochastic models and their application to the real world. The word “stochastic”
is derived from the Greek “Stochazesthai”, the art of guessing, or “Stochastikos”,
meaning skilled at aiming, “stochos” being a target. In discussing stochastic methods
forriskmanagementwehopetoemphasizetheskillaspectratherthantheguesswork.
1.1.2
Financial Risk
In this book we discuss risk in the context of ﬁnance and insurance (although many
of the tools introduced are applicable well beyond this context). We start by giving
a brief overview of the main risk types encountered in the ﬁnancial industry.
In banking, the best known type of risk is probably market risk, the risk of a change
in the value of a ﬁnancial position due to changes in the value of the underlying
--- page 19 ---

1.1. Risk
3
components on which that position depends, such as stock and bond prices, exchange
rates, commodity prices, etc. The next important category is credit risk, the risk of
not receiving promised repayments on outstanding investments such as loans and
bonds, because of the “default” of the borrower. A further risk category that has
received a lot of recent attention is operational risk, the risk of losses resulting from
inadequate or failed internal processes, people and systems, or from external events.
The boundaries of these three risk categories are not always clearly deﬁned, nor
do they form an exhaustive list of the full range of possible risks affecting a ﬁnancial institution. There are notions of risk which surface in nearly all categories
such as liquidity and model risk. The latter is the risk associated with using a misspeciﬁed (inappropriate) model for measuring risk. Think, for instance, of using the
Black–Scholes model for pricing an exotic option in circumstances where the basic
Black–Scholes model assumptions on the underlying securities (such as the assumption of normally distributed returns) are violated. It may be argued that model risk
is always present to some degree. Liquidity risk could be roughly deﬁned as the risk
stemming from the lack of marketability of an investment that cannot be bought or
sold quickly enough to prevent or minimize a loss. Liquidity can be thought of as
“oxygen for a healthy market”; we need it to survive but most of the time we are
not aware of its presence. Its absence, however, is mostly recognized immediately,
with often disastrous consequences.
The concepts, techniques and tools we will introduce in the following chapters
mainly apply to the three basic categories of market, credit and operational risk. We
should stress that the only viable way forward for a successful handling of ﬁnancial
risk consists of a holistic approach, i.e. an integrated approach taking all types of
risk and their interactions into account. Whereas this is a clear goal, current models
do not yet allow for a fully satisfactory platform.
As well as banks, the insurance industry has a long-standing relationship with
risk. It is no coincidence that the Institute of Actuaries and the Faculty of Actuaries
use the following deﬁnition of the actuarial profession.
Actuaries are respected professionals whose innovative approach to
making business successful is matched by a responsibility to the public
interest. Actuaries identify solutions to ﬁnancial problems. They manage assets and liabilities by analysing past events, assessing the present
risk involved and modelling what could happen in the future.
An additional risk category entering through insurance is underwriting risk, the
risk inherent in insurance policies sold. Examples of risk factors that play a role
here are changing patterns of natural catastrophes, changes in demographic tables
underlying (long-dated) life products, or changing customer behaviour (such as
prepayment patterns).
1.1.3
Measurement and Management
Much of this book is concerned with techniques for the measurement of risk, an
activity which is part of the process of managing risk, as we attempt to clarify in
this section.
--- page 20 ---

4
1. Risk in Perspective
Risk measurement.
Suppose we hold a portfolio consisting of d underlying investments with respective weights w1, . . . , wd so that the change in value of the portfolio
over a given holding period (the so-called P&L, or proﬁt and loss) can be written as
X = d
i=1 wiXi, where Xi denotes the change in value of the ith investment. Measuring the risk of this portfolio essentially consists of determining its distribution
function FX(x) = P(X ⩽x), or functionals describing this distribution function
such as its mean, variance or 99th percentile.
In order to achieve this, we need a properly calibrated joint model for the underlying random vector of investments (X1, . . . , Xd). We will consider this problem in
more detail in Chapter 2.At this point it sufﬁces to understand that risk measurement
is essentially a statistical issue; based on historical observations and given a speciﬁc
model, a statistical estimate of the distribution of the change in value of a position,
or one of its functionals, is calculated.As we shall see later, and this is indeed a main
theme throughout the book, this is by no means an easy task with a unique solution.
It should be clear from the outset that good risk measurement is a must. Increasingly, banking clients demand objective and detailed information on products bought
and banks can face legal action when this information is found wanting. For any
product sold, a proper quantiﬁcation of the underlying risks needs to be explicitly
made, allowing the client to decide whether or not the product on offer corresponds
to his or her risk appetite.
Risk management.
In a very general answer to the question of what risk management is about, Kloman (1990) writes that:
To many analysts, politicians, and academics it is the management of
environmental and nuclear risks, those technology-generated macrorisks that appear to threaten our existence. To bankers and ﬁnancial
ofﬁcersitisthesophisticateduseofsuchtechniquesascurrencyhedging
and interest-rate swaps. To insurance buyers or sellers it is coordination
of insurable risks and the reduction of insurance costs. To hospital
administrators it may mean “quality assurance”. To safety professionals
it is reducing accidents and injuries. In summary, risk management is
a discipline for living with the possibility that future events may cause
adverse effects.
The last phrase in particular (the italics are ours) captures the general essence of
risk management, although for a ﬁnancial institution one can perhaps go further. A
bank’s attitude to risk is not passive and defensive; a bank actively and willingly
takes on risk, because it seeks a return and this does not come without risk. Indeed
risk management can be seen as the core competence of an insurance company
or a bank. By using its expertise, market position and capital structure, a ﬁnancial
institution can manage risks by repackaging them and transferring them to markets
in customized ways.
Managing the risk is thus related to preserving the ﬂow of proﬁt and to techniques
like asset liability management (ALM), which might be deﬁned as managing a ﬁnancial institution so as to earn an adequate return on funds invested, and to maintain
