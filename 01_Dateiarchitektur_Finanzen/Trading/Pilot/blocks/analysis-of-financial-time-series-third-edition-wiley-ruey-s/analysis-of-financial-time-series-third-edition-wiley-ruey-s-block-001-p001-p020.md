# Analysis of Financial Time Series, Third Edition (Wiley -- Ruey S_ Tsay -- Wiley series in probability and statistics, 3rd ed_, -- John Wiley & Sons, -- isbn13 9780470414354 -- 9f99b80c7b2dedd477f463dc5323f3b6 -- An.pdf — pages 1–20

--- page 1 ---
--- page 2 ---

Analysis of Financial Time Series
Third Edition
RUEY S. TSAY
The University of Chicago
Booth School of Business
Chicago, IL
A JOHN WILEY & SONS, INC., PUBLICATION
--- page 3 ---
--- page 4 ---

Analysis of Financial Time Series
--- page 5 ---

WILEY SERIES IN PROBABILITY AND STATISTICS
Established by WALTER A. SHEWHART and SAMUEL S. WILKS
Editors: David J. Balding, Noel A. C. Cressie, Garrett M. Fitzmaurice,
Iain M. Johnstone, Geert Molenberghs, David W. Scott, Adrian F. M. Smith,
Ruey S. Tsay, Sanford Weisberg
Editors Emeriti: Vic Barnett, J. Stuart Hunter, Jozef L. Teugels
A complete list of the titles in this series appears at the end of this volume.
--- page 6 ---

Analysis of Financial Time Series
Third Edition
RUEY S. TSAY
The University of Chicago
Booth School of Business
Chicago, IL
A JOHN WILEY & SONS, INC., PUBLICATION
--- page 7 ---

Copyright 2010 by John Wiley & Sons, Inc. All rights reserved.
Published by John Wiley & Sons, Inc., Hoboken, New Jersey.
Published simultaneously in Canada.
No part of this publication may be reproduced, stored in a retrieval system, or transmitted in any form
or by any means, electronic, mechanical, photocopying, recording, scanning, or otherwise, except as
permitted under Section 107 or 108 of the 1976 United States Copyright Act, without either the prior
written permission of the Publisher, or authorization through payment of the appropriate per-copy fee
to the Copyright Clearance Center, Inc., 222 Rosewood Drive, Danvers, MA 01923, (978) 750-8400,
fax (978) 750-4744. Requests to the Publisher for permission should be addressed to the Permissions
Department, John Wiley & Sons, Inc., 111 River Street, Hoboken, NJ 07030, (201) 748-6011, fax (201)
748-6008, or online at http://www.wiley.com/go/permission.
Limit of Liability/Disclaimer of Warranty: While the publisher and author have used their best efforts
in preparing this book, they make no representations or warranties with respect to the accuracy or completeness of the contents of this book and speciﬁcally disclaim any implied warranties of merchantability
or ﬁtness for a particular purpose. No warranty may be created or extended by sales representatives
or written sales materials. The advice and strategies contained herein may not be suitable for your
situation. You should consult with a professional where appropriate. Neither the publisher nor author
shall be liable for any loss of proﬁt or any other commercial damages, including but not limited to
special, incidental, consequential, or other damages.
For general information on our other products and services or for technical support, please contact our
Customer Care Department within the United States at (800) 762-2974, outside the United States at
(317) 572-3993 or fax (317) 572-4002.
Wiley also publishes its books in a variety of electronic formats. Some content that appears in print
may not be available in electronic formats. For more information about Wiley products, visit our web
site at www.wiley.com.
Library of Congress Cataloging-in-Publication Data:
Tsay, Ruey S., 1951–
Analysis of ﬁnancial time series / Ruey S. Tsay. – 3rd ed.
p. cm. – (Wiley series in probability and statistics)
Includes bibliographical references and index.
ISBN 978-0-470-41435-4 (cloth)
1.
Time-series analysis.
2.
Econometrics.
3.
Risk management.
I.
Title.
HA30.3T76 2010
332.01’51955–dc22
2010005151
Printed in the United States of America
10 9 8 7 6 5 4 3 2 1
--- page 8 ---

To Teresa and my father, and in memory of my mother
--- page 9 ---
--- page 10 ---

Contents
Preface
xvii
Preface to the Second Edition
xix
Preface to the First Edition
xxi
1
Financial Time Series and Their Characteristics
1
1.1
Asset Returns, 2
1.2
Distributional Properties of Returns, 7
1.2.1
Review of Statistical Distributions and Their Moments, 7
1.2.2
Distributions of Returns, 14
1.2.3
Multivariate Returns, 18
1.2.4
Likelihood Function of Returns, 19
1.2.5
Empirical Properties of Returns, 19
1.3
Processes Considered, 22
Appendix: R Packages, 24
Exercises, 25
References, 27
2
Linear Time Series Analysis and Its Applications
29
2.1
Stationarity, 30
2.2
Correlation and Autocorrelation Function, 30
2.3
White Noise and Linear Time Series, 36
2.4
Simple AR Models, 37
2.4.1
Properties of AR Models, 38
2.4.2
Identifying AR Models in Practice, 46
2.4.3
Goodness of Fit, 53
2.4.4
Forecasting, 54
vii
--- page 11 ---

viii
contents
2.5
Simple MA Models, 57
2.5.1
Properties of MA Models, 59
2.5.2
Identifying MA Order, 60
2.5.3
Estimation, 61
2.5.4
Forecasting Using MA Models, 62
2.6
Simple ARMA Models, 64
2.6.1
Properties of ARMA(1,1) Models, 64
2.6.2
General ARMA Models, 66
2.6.3
Identifying ARMA Models, 66
2.6.4
Forecasting Using an ARMA Model, 68
2.6.5
Three Model Representations for an ARMA Model, 69
2.7
Unit-Root Nonstationarity, 71
2.7.1
Random Walk, 72
2.7.2
Random Walk with Drift, 73
2.7.3
Trend-Stationary Time Series, 75
2.7.4
General Unit-Root Nonstationary Models, 75
2.7.5
Unit-Root Test, 76
2.8
Seasonal Models, 81
2.8.1
Seasonal Differencing, 82
2.8.2
Multiplicative Seasonal Models, 84
2.9
Regression Models with Time Series Errors, 90
2.10
Consistent Covariance Matrix Estimation, 97
2.11
Long-Memory Models, 101
Appendix: Some SCA Commands, 103
Exercises, 104
References, 107
3
Conditional Heteroscedastic Models
109
3.1
Characteristics of Volatility, 110
3.2
Structure of a Model, 111
3.3
Model Building, 113
3.3.1
Testing for ARCH Effect, 114
3.4
The ARCH Model, 115
3.4.1
Properties of ARCH Models, 117
3.4.2
Weaknesses of ARCH Models, 119
3.4.3
Building an ARCH Model, 119
3.4.4
Some Examples, 123
3.5
The GARCH Model, 131
3.5.1
An Illustrative Example, 134
--- page 12 ---

contents
ix
3.5.2
Forecasting Evaluation, 139
3.5.3
A Two-Pass Estimation Method, 140
3.6
The Integrated GARCH Model, 140
3.7
The GARCH-M Model, 142
3.8
The Exponential GARCH Model, 143
3.8.1
Alternative Model Form, 144
3.8.2
Illustrative Example, 145
3.8.3
Second Example, 145
3.8.4
Forecasting Using an EGARCH Model, 147
3.9
The Threshold GARCH Model, 149
3.10
The CHARMA Model, 150
3.10.1
Effects of Explanatory Variables, 152
3.11
Random Coefﬁcient Autoregressive Models, 152
3.12
Stochastic Volatility Model, 153
3.13
Long-Memory Stochastic Volatility Model, 154
3.14
Application, 155
3.15
Alternative Approaches, 159
3.15.1
Use of High-Frequency Data, 159
3.15.2
Use of Daily Open, High, Low, and Close Prices, 162
3.16
Kurtosis of GARCH Models, 165
Appendix: Some RATS Programs for Estimating Volatility Models, 167
Exercises, 168
References, 171
4
Nonlinear Models and Their Applications
175
4.1
Nonlinear Models, 177
4.1.1
Bilinear Model, 177
4.1.2
Threshold Autoregressive (TAR) Model, 179
4.1.3
Smooth Transition AR (STAR) Model, 184
4.1.4
Markov Switching Model, 186
4.1.5
Nonparametric Methods, 189
4.1.6
Functional Coefﬁcient AR Model, 198
4.1.7
Nonlinear Additive AR Model, 198
4.1.8
Nonlinear State-Space Model, 199
4.1.9
Neural Networks, 199
4.2
Nonlinearity Tests, 205
4.2.1
Nonparametric Tests, 206
4.2.2
Parametric Tests, 209
4.2.3
Applications, 213
--- page 13 ---

x
contents
4.3
Modeling, 214
4.4
Forecasting, 215
4.4.1
Parametric Bootstrap, 215
4.4.2
Forecasting Evaluation, 215
4.5
Application, 218
Appendix A: Some RATS Programs for Nonlinear Volatility Models, 222
Appendix B: R and S-Plus Commands for Neural Network, 223
Exercises, 224
References, 226
5
High-Frequency Data Analysis and Market Microstructure
231
5.1
Nonsynchronous Trading, 232
5.2
Bid–Ask Spread, 235
5.3
Empirical Characteristics of Transactions Data, 237
5.4
Models for Price Changes, 244
5.4.1
Ordered Probit Model, 245
5.4.2
Decomposition Model, 248
5.5
Duration Models, 253
5.5.1
The ACD Model, 255
5.5.2
Simulation, 257
5.5.3
Estimation, 260
5.6
Nonlinear Duration Models, 264
5.7
Bivariate Models for Price Change and Duration, 265
5.8
Application, 270
Appendix A: Review of Some Probability Distributions, 276
Appendix B: Hazard Function, 279
Appendix C: Some RATS Programs for Duration Models, 280
Exercises, 282
References, 284
6
Continuous-Time Models and Their Applications
287
6.1
Options, 288
6.2
Some Continuous-Time Stochastic Processes, 288
6.2.1
Wiener Process, 289
6.2.2
Generalized Wiener Process, 291
6.2.3
Ito Process, 292
6.3
Ito’s Lemma, 292
6.3.1
Review of Differentiation, 292
--- page 14 ---

contents
xi
6.3.2
Stochastic Differentiation, 293
6.3.3
An Application, 294
6.3.4
Estimation of µ and σ, 295
6.4
Distributions of Stock Prices and Log Returns, 297
6.5
Derivation of Black–Scholes Differential Equation, 298
6.6
Black–Scholes Pricing Formulas, 300
6.6.1
Risk-Neutral World, 300
6.6.2
Formulas, 300
6.6.3
Lower Bounds of European Options, 304
6.6.4
Discussion, 305
6.7
Extension of Ito’s Lemma, 309
6.8
Stochastic Integral, 310
6.9
Jump Diffusion Models, 311
6.9.1
Option Pricing under Jump Diffusion, 315
6.10
Estimation of Continuous-Time Models, 318
Appendix A: Integration of Black–Scholes Formula, 319
Appendix B: Approximation to Standard Normal Probability, 320
Exercises, 321
References, 322
7
Extreme Values, Quantiles, and Value at Risk
325
7.1
Value at Risk, 326
7.2
RiskMetrics, 328
7.2.1
Discussion, 331
7.2.2
Multiple Positions, 332
7.2.3
Expected Shortfall, 332
7.3
Econometric Approach to VaR Calculation, 333
7.3.1
Multiple Periods, 336
7.3.2
Expected Shortfall under Conditional Normality, 338
7.4
Quantile Estimation, 338
7.4.1
Quantile and Order Statistics, 338
7.4.2
Quantile Regression, 341
7.5
Extreme Value Theory, 342
7.5.1
Review of Extreme Value Theory, 342
7.5.2
Empirical Estimation, 345
7.5.3
Application to Stock Returns, 348
7.6
Extreme Value Approach to VaR, 353
7.6.1
Discussion, 356
--- page 15 ---

xii
contents
7.6.2
Multiperiod VaR, 357
7.6.3
Return Level, 358
7.7
New Approach Based on the Extreme Value Theory, 359
7.7.1
Statistical Theory, 360
7.7.2
Mean Excess Function, 361
7.7.3
New Approach to Modeling Extreme Values, 363
7.7.4
VaR Calculation Based on the New Approach, 365
7.7.5
Alternative Parameterization, 367
7.7.6
Use of Explanatory Variables, 371
7.7.7
Model Checking, 372
7.7.8
An Illustration, 373
7.8
The Extremal Index, 377
7.8.1
The D(un) Condition, 378
7.8.2
Estimation of the Extremal Index, 381
7.8.3
Value at Risk for a Stationary Time Series, 384
Exercises, 384
References, 387
8
Multivariate Time Series Analysis and Its Applications
389
8.1
Weak Stationarity and Cross-Correlation Matrices, 390
8.1.1
Cross-Correlation Matrices, 390
8.1.2
Linear Dependence, 392
8.1.3
Sample Cross-Correlation Matrices, 392
8.1.4
Multivariate Portmanteau Tests, 397
8.2
Vector Autoregressive Models, 399
8.2.1
Reduced and Structural Forms, 399
8.2.2
Stationarity Condition and Moments of a VAR(1)
Model, 401
8.2.3
Vector AR(p) Models, 403
8.2.4
Building a VAR(p) Model, 405
8.2.5
Impulse Response Function, 413
8.3
Vector Moving-Average Models, 417
8.4
Vector ARMA Models, 422
8.4.1
Marginal Models of Components, 427
8.5
Unit-Root Nonstationarity and Cointegration, 428
8.5.1
An Error Correction Form, 431
8.6
Cointegrated VAR Models, 432
8.6.1
Speciﬁcation of the Deterministic Function, 434
--- page 16 ---

contents
xiii
8.6.2
Maximum-Likelihood Estimation, 435
8.6.3
Cointegration Test, 436
8.6.4
Forecasting of Cointegrated VAR Models, 437
8.6.5
An Example, 438
8.7
Threshold Cointegration and Arbitrage, 442
8.7.1
Multivariate Threshold Model, 444
8.7.2
The Data, 445
8.7.3
Estimation, 445
8.8
Pairs Trading, 446
8.8.1
Theoretical Framework, 446
8.8.2
Trading Strategy, 448
8.8.3
Simple Illustration, 449
Appendix A: Review of Vectors and Matrices, 456
Appendix B: Multivariate Normal Distributions, 460
Appendix C: Some SCA Commands, 461
Exercises, 462
References, 464
9
Principal Component Analysis and Factor Models
467
9.1
A Factor Model, 468
9.2
Macroeconometric Factor Models, 470
9.2.1
Single-Factor Model, 470
9.2.2
Multifactor Models, 474
9.3
Fundamental Factor Models, 476
9.3.1
BARRA Factor Model, 477
9.3.2
Fama–French Approach, 482
9.4
Principal Component Analysis, 483
9.4.1
Theory of PCA, 483
9.4.2
Empirical PCA, 485
9.5
Statistical Factor Analysis, 489
9.5.1
Estimation, 490
9.5.2
Factor Rotation, 492
9.5.3
Applications, 492
9.6
Asymptotic Principal Component Analysis, 498
9.6.1
Selecting the Number of Factors, 499
9.6.2
An Example, 500
Exercises, 501
References, 503
--- page 17 ---

xiv
contents
10
Multivariate Volatility Models and Their Applications
505
10.1
Exponentially Weighted Estimate, 506
10.2
Some Multivariate GARCH Models, 510
10.2.1
Diagonal Vectorization (VEC) Model, 510
10.2.2
BEKK Model, 513
10.3
Reparameterization, 516
10.3.1
Use of Correlations, 516
10.3.2
Cholesky Decomposition, 517
10.4
GARCH Models for Bivariate Returns, 521
10.4.1
Constant-Correlation Models, 521
10.4.2
Time-Varying Correlation Models, 525
10.4.3
Dynamic Correlation Models, 531
10.5
Higher Dimensional Volatility Models, 537
10.6
Factor–Volatility Models, 543
10.7
Application, 546
10.8
Multivariate t Distribution, 548
Appendix: Some Remarks on Estimation, 549
Exercises, 554
References, 555
11
State-Space Models and Kalman Filter
557
11.1
Local Trend Model, 558
11.1.1
Statistical Inference, 561
11.1.2
Kalman Filter, 562
11.1.3
Properties of Forecast Error, 564
11.1.4
State Smoothing, 566
11.1.5
Missing Values, 570
11.1.6
Effect of Initialization, 571
11.1.7
Estimation, 572
11.1.8
S-Plus Commands Used, 572
11.2
Linear State-Space Models, 576
11.3
Model Transformation, 577
11.3.1
CAPM with Time-Varying Coefﬁcients, 577
11.3.2
ARMA Models, 580
11.3.3
Linear Regression Model, 586
11.3.4
Linear Regression Models with ARMA Errors, 588
11.3.5
Scalar Unobserved Component Model, 590
--- page 18 ---

contents
xv
11.4
Kalman Filter and Smoothing, 591
11.4.1
Kalman Filter, 591
11.4.2
State Estimation Error and Forecast Error, 594
11.4.3
State Smoothing, 595
11.4.4
Disturbance Smoothing, 597
11.5
Missing Values, 600
11.6
Forecasting, 601
11.7
Application, 602
Exercises, 609
References, 611
12
Markov Chain Monte Carlo Methods with Applications
613
12.1
Markov Chain Simulation, 614
12.2
Gibbs Sampling, 615
12.3
Bayesian Inference, 617
12.3.1
Posterior Distributions, 617
12.3.2
Conjugate Prior Distributions, 618
12.4
Alternative Algorithms, 622
12.4.1
Metropolis Algorithm, 622
12.4.2
Metropolis–Hasting Algorithm, 623
12.4.3
Griddy Gibbs, 623
12.5
Linear Regression with Time Series Errors, 624
12.6
Missing Values and Outliers, 628
12.6.1
Missing Values, 629
12.6.2
Outlier Detection, 632
12.7
Stochastic Volatility Models, 636
12.7.1
Estimation of Univariate Models, 637
12.7.2
Multivariate Stochastic Volatility Models, 643
12.8
New Approach to SV Estimation, 649
12.9
Markov Switching Models, 660
12.10
Forecasting, 666
12.11
Other Applications, 669
Exercises, 670
References, 671
Index
673
--- page 19 ---
--- page 20 ---

Preface
As many countries struggle to recover from the recent global ﬁnancial crisis, one
thing clear is that we do not want to suffer another crisis like this in the future.
We must study the past in order to prevent future ﬁnancial crisis. Financial data
of the past few years thus become important in empirical study. The primary
objective of the revision is to update the data used and to reanalyze the examples
so that one can better understand the properties of asset returns. At the same time,
we also witness many new developments in ﬁnancial econometrics and ﬁnancial
software packages. In particular, the Rmetrics now has many packages for analyzing
ﬁnancial time series. The second goal of the revision is to include R commands and
demonstrations, making it possible and easier for readers to reproduce the results
shown in the book.
Collapses of big ﬁnancial institutions during the crisis show that extreme events
occur in clusters; they are not independent. To deal with dependence in extremes,
I include the extremal index in Chapter 7 and discuss its impact on value at risk.
I also rewrite Chapter 7 to make it easier to understand and more complete. It
now contains the expected shortfall, or conditional value at risk, for measuring
ﬁnanical risk.
Substantial efforts are made to draw a balance between the length and coverage of the book. I do not include credit risk or operational risk in this revision
for three reasons. First, effective methods for assessing credit risk require further
study. Second, the data are not widely available. Third, the length of the book is
approaching my limit.
A brief summary of the added material in the third edition is:
1. To update the data used throughout the book.
2. To provide R commands and demonstrations. In some cases, R programs are
given.
3. To reanalyze many examples with updated observations.
4. To introduce skew distributions for volatility modeling in Chapter 3.
5. To investigate properties of recent high-frequency trading data and to add
applications of nonlinear duration models in Chapter 5.
xvii
