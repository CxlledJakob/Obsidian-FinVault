# The Kelly capital growth investment criterion _ theory and -- Leonard C_ Maclean, Edward O_ Thorp, W_ T_ Ziemba, Leonard -- World Scientific Handbook -- isbn13 9781283148344 -- bec576e26410d0c695fd5b867d08ec4f -- An.pdf — pages 1–20

--- page 1 ---

World Scientific Handbook in Financial Economic Series -
Vol. 3
THEORY and PRACTICE
-
THE __________
_
KELLY CAPITAL GROWTH
INVESTMENT CRITERION
I
,
I • I
~
~
1
I
I
leonard ( Maclean
Edward 0 Thorp
. .
.
Wilham T Ziemba
editors
,I» World Scientific
--- page 2 ---

THEORY and PRACTICE
_
THE ________
_
KELLY CAPITAL GROWTH
INVESTMENT CRITERION
--- page 3 ---

World Scientific Handbook in Financial Economic Series
(ISSN: 2010-1732)
Series Editor:
William T. Ziemba
Professor Emeritus, University of British Columbia, Canada
Visiting Professor, Oxford University and University of Reading, UK
Advisory Editors:
Kenneth J. Arrow
Stanford University, USA
George C. Constantinides
University of Chicago, USA
Espen Eckbo
Dartmouth College, USA
Harry M. Markowitz
University of California, USA
Robert C. Merton
Harvard University, USA
Stewart C. Myers
Massachusetts institute of Technology,
USA
Paul A. Samuelson
Massachusetts institute of Technology,
USA
William F. Sharpe
Stanford University, USA
The Handbooks in Financial Economics (HIFE) are intended to be a definitive source for
comprehensive and accessible information in the field of finance. Each individual volume
in the series presents an accurate self-contained survey ofa sub-field of finance, suitable
for use by finance, economics and financial engineering professors and lecturers,
professional researchers, investments, pension fund and insurance portfolio mangers, risk
managers, graduate students and as a teaching supplement.
The HIFE series will broadly cover various areas of finance in a multi-handbook series.
The HIFE series has its own web page that include detailed information such as the
introductory chapter to each volume, an abstract of each chapter and biographies of
editors. The series will be promoted by the publisher at major academic meetings and
through other sources. There will be links with research articles in major journals.
The goal is to have a broad group of outstanding volumes in various areas of financial
economics. The evidence is that acceptance of all the books is strengthened over time and
by the presence of other strong volumes. Sales, citations, royalties and recognition tend
to grow over time faster than the number of volumes published.
Published
Vol. 1
Stochastic Optimization Models in Finance (2006 Edition)
edited by William T Ziemba & Raymond G. Vickson
Vol. 2
Efficiency of Racetrack Betting Markets (2008 Edition)
edited by Donald B. Hausch, Victor S. Y. Lo & William T Ziemba
Vol. 3
The Kelly Capital Growth Investment Criterion: Theory and Practice
edited by Leonard C. MacLean, Edward 0. Thorp & William T Ziemba
--- page 4 ---

World Scientific Handbook in Financial Economic Series -
Vol. 3
THEORY and PRACTICE
___ THE ___________________ _
KELLY CAPITAL GROWTH
INVESTMENT CRITERION
Editors
leonard C Maclean
Dalhousie University, USA
Edward 0 Thorp
University of California, Irvine, USA
William T Ziemba
Mathematical Institute, Oxford University, UK and University of British Columbia, Canada
'~World Scientific
NEW JERSEY· LONDON· SINGAPORE· BEIJING· SHANGHAI · HONG KONG· TAIPEI· CHENNAI
--- page 5 ---

Published by
World Scientific PublisWng Co. Pte. Ltd.
5 Toh Tuck Link, Singapore 596224
USA offlce: 27 Warren Street, Suite 401-402, Hackensack, NJ 07601
UK offlce: 57 Shelton Street, Covent Garden, London WC2H 9HE
Library of Congress Cataloging-in-Publication Data
The Kelly capital growth investment criterion : theory and practice I edited by Leonard C. MacLean,
Edward O. Thorp, William T. Ziemba.
p. em. -- (World Scientific handbook in financial economic series, 2010-1732 ; 3)
Includes bibliograpWcal references.
ISBN-13: 978-9814293495
ISBN-lO : 9814293490
ISBN-13: 978-9814293501
ISBN-lO : 9814293504
1. Investments--Mathematical models. 2. Portfolio management--Mathematical models.
1. MacLean, L. C. (Leonard C.) II. Thorp, Edward O. III. Ziemba, W. T.
HG45 15.2.K45201O
332.63'2042--dc22
British Library Cataloguing-in-Publication Data
2010044902
A catalogue record for this book is available fro m the British Library.
Copyright © 2011 by World Scientific PublisWng Co. Pte. Ltd.
All rights reserved. This book, or parts thereof, may not be reproduced in any form or by any means, electronic or
mechanical, including photocopying, recording or any information storage and retrieval system now known or to
be invented, without written permission from the Publisher.
For photocopyi ng of material in tWs volume, please pay a copyi ng fee through the Copyright Clearance Center,
Inc., 222 Rosewood Drive, Danvers, MA 0 1923, USA. In this case permission to photocopy is not required from
the publisher.
Printed in Singapore.
--- page 6 ---

To my wife Gwenolyn, for her patience and encouragement, and Dalhousie
University for its constant support over many years
Leonard C. MacLean
To Vivian, with whom I've shared "the long run"
Edward O. Thorp
To Sandra for companionship, help, patience, and understanding over a long time
and to the memory of Kelly criterion pioneeers, John L. Kelly, Henry A. Latane,
Leo Breiman, and Kelly critic Paul A. Samuelson
William T. Ziemba
--- page 7 ---

This page is intentionally left blank
--- page 8 ---

Contents
Preface
List of Contributors
Acknow ledgments
Pictures
Part I: The Early Ideas and Contributions
1. Introduction to the Early Ideas and Contributions
2. Exposition of a New Theory on the Measurement of Risk
(translated by Louise Sommer)
D. Bernoulli
Econometrica, 22, 23-36 (1954)
3. A New Interpretation of Information Rate
J. R. Kelly, Jr.
Bell System Technical Journal, 35, 917- 926 (1956)
4. Criteria for Choice among Risky Ventures
H. A. Latane
Journal of Political Economy, 67, 144- 155 (1959)
5. Optimal Gambling Systems for Favorable Games
L. Breiman
Proceedings of the 4th Berkeley Symposium on
Mathematical Statistics and Probability, 1, 63- 68 (1961)
VII
xv
XVll
XXI
xxv
3
11
25
35
47
--- page 9 ---

viii
Contents
6. Optimal Gambling Systems for Favorable Games
61
E. O. Thorp
Review of the International Statistical Institute, 37(3) ,
273-293 (1969)
7. Portfolio Choice and the Kelly Criterion
81
E. O. Thorp
Proceedings of the Business and Economics Section of
the American Statistical Association, 215- 224 (1971)
8. Optimal Investment and Consumption Strategies under Risk
91
for a Class of Utility Functions
N. H. Hakansson
Econometrica, 38, 587- 607 (1970)
9. On Optimal Myopic Portfolio Policies, with and without
113
Serial Correlation of Yields
N. H. Hakansson
Journal of Business, 44, 324- 334 (1971)
10. Evidence on the "Growth-Optimum-Model"
125
R. Roll
The Journal of Finance, 28(3), 551- 566 (1973)
Part II: Classic Papers and Theories
11. Introduction to the Classic Papers and Theories
143
12. Competitive Optimality of Logarithmic Investment
147
R. M. Bell and T . M. Cover
Mathematics of Operations Research, 5(2) ,
161- 166 (1980)
13. A Bound on the Financial Value of Information
153
A. R. Barron and T. M. Cover
IEEE Transactions of Information Theory, 34(5) ,
1097- 1100 (1988)
--- page 10 ---

14.
15.
16.
17.
18.
19.
20.
Asymptotic Optimality and Asymptotic Equipartition
Properties of Log-Optimum Investment
P. H. Algoet and T. M. Cover
Annals of Probability, 16(2), 876- 898 (1988)
Universal Portfolios
T . M. Cover
Mathematical Finance, 1(1), 1- 29 (1991)
The Cost of Achieving the Best Portfolio in Hindsight
E. Ordentlich and T. M. Cover
Mathematics of Operations Research, 23(4),
960- 982 (1998)
Optimal Strategies for Repeated Games
M. Finkelstein and R. Whitley
Advanced Applied Probability, 13, 415- 428 (1981)
The Effect of Errors in Means, Variances and Co-Variances
on Optimal Portfolio Choice
V. K. Chopra and W. T. Ziemba
Journal of Portfolio Management, 19, 6- 11 (1993)
Time to Wealth Goals in Capital Accumulation
L. C. MacLean, W . T . Ziemba, and Y. Li
Quantitative Finance, 5(4), 343- 355 (2005)
Survival and evolutionary Stability of Rule the Kelly
1. V. Evstigneev, T. Hens, and K. R. Schenk-Hoppe
(2010)
Contents
IX
157
181
211
235
249
259
273
--- page 11 ---

x
Contents
21. Application of the Kelly Criterion to Ornstein-Uhlenbeck
Processes
Y. Lv and B. K. Meister
Lecture Notes of the Institute for Computer Sciences, 4,
1051- 1062 (2009)
Part III: The Relationship of Kelly Optimization to
Asset Allocation
22. Introduction to the Relationship of Kelly Optimization to
Asset Allocation
23. Survival and Growth with a Liability: Optimal Portfolio
Strategies in Continuous Time
24.
25.
26.
27.
28.
S. Browne
Mathematics of Operations Research, 22(2) , 468- 493
(1997)
Growth versus Security in Dynamic Investment Analysis
L. C. MacLean, W. T. Ziemba, and G. Blazenko
Management Science, 38(11), 1562-1585 (1992)
Capital Growth with Security
L. C. MacLean, R. Sanegre, Y. Zhao, and W. T . Ziemba
Journal of Economic Dynamics and Control, 28(4),
937-954 (2004)
Risk-Constrained Dynamic Active Portfolio Management
S. Browne
Management Science, 46(9), 1188-1199 (2000)
Fractional Kelly Strategies for Benchmark Asset Management
M. Davis and S. Lleo (2010)
A Benchmark Approach to Investing and Pricing
E. Platen (2010)
285
301
307
331
355
373
385
409
--- page 12 ---

Contents
Xl
29. Growing Wealth with Fixed-Mix Strategies
M. A. H. Dempster, 1. V. Evstigneev, and
K. R. Schenk-Hoppe (2010)
P art IV : Critics and Assessing the Good and Bad
P roperties of K elly
30. Introduction to the Good and Bad Properties of Kelly
31. Lifetime Portfolio Selection by Dynamic Stochastic
Programming
P. A. Samuelson
Review of Economics and Statistics, 51, 239- 246 (1969)
32. Models of Optimal Capital Accumulation and Portfolio
Selection and the Captial Growth Criterion
W . T. Ziemba and R. G. Vickson (2010)
33. The "Fallacy" of Maximizing the Geometric Mean in Long
Sequences of Investing or Gambling
P. A. Samuelson
Proceedings National Academy of Science, 68(10),
2493- 2496 (1971)
34. Why We Should Not Make Mean Log of Wealth Big Though
Years to Act Are Long
P. A. Samuelson
Journal of Banking and Finance, 3, 305- 307 (1979)
35. Investment for the Long Run: New Evidence for an Old Rule
H. M. Markowitz
Journal of Finance, 31(5), 1273- 1286 (1976)
36. Understanding the Kelly Criterion
E. O. Thorp
Wilmott, May and September (2008)
427
459
465
473
487
491
495
509
--- page 13 ---

Xli
Contents
37. Concave Utilities Are Distinguished by Their
525
Optimal Strategies
E. O. Thorp and R. Whitley
Colloquia Mathematica Societatis Janos Bolyai,
813-830 (1972)
38. Medium Term Simulations of the Full Kelly and
543
Fractional Kelly Strategies Investment
L. C. MacLean, E. O. Thorp, Y. Zhao, and
W. T. Ziemba (2010)
39. Good and Bad Kelly Properties of the Kelly Criterion
563
L. C. MacLean, E. O. Thorp, and W. T. Ziemba (2010)
Part V: Utility Foundations
40. Introduction to the Utility Foundations of Kelly
575
41. Capital Growth Theory
577
N. H. Hakansson and W. T. Ziemba
In R. A. J arrow , V. Maksimovic, and W. T. Ziemba
(Eds.) , Finance, Handbooks in OR fj MS, Volume 9,
65- 86. North Holland (1995)
42. A Preference Foundation for Log Mean-Variance Criteria in
599
Portfolio Choice Problems
D. G. Luenberger
Journal of Economic Dynamics and Control, 17,
88- 906 (1993)
43. Portfolio Choice with Endogenous Utility: A Large
619
Deviations Approach
M. Stutzer
Journal of Econometrics, 116, 365-386 (2003)
--- page 14 ---

44.
45.
46.
47.
48.
49.
50.
Contents
On Growth-Optimality vs. Security against Underperformance
M. Stutzer (2010)
Part VI: Evidence of the Use of Kelly Type Strategies by the
Great Investors and Others
Introduction to the Evidence of the Use of Kelly Type
Strategies by the Great Investors and Others
Efficiency of the Market for Racetrack Betting
D. B. Hausch, W. T. Ziemba, and M. E. Rubinstein
Management Science, 27, 1435- 1452 (1981)
Transactions Costs, Extent of Inefficiencies, Entries and
Multiple Wagers in a Racetrack Betting Model
D. B. Hausch and W. T. Ziemba
Management Science, 31, 381- 394 (1985)
The Dr. Z Betting System in England
W. T. Ziemba and D. B. Hausch
In D. B. Hausch, V. Lo, and W. T . Ziemba (Eds.),
Efficiency of Racetrack Betting Markets, 567- 574.
World Scientific (2008)
A Half Century of Returns on Levered and Unlevered Portfolios
of Stocks, Bonds and Bills, with and without Small Stocks
R. R. Grauer and N. H. Hakansson
Journal of Business, 592, 287- 318 (1986)
A Dynamic Portfolio of Investment Strategies: Applying
Capital Growth with Drawdown Penalties
J. M. Mulvey, M. Bilgili, and T. M. Vural (2010)
Xlll
641
657
663
681
695
703
735
--- page 15 ---

XIV
Contents
51. Intertemporal Surplus Management
M. Rudolf and W. T. Ziemba
Journal of Economic Dynamics and Control, 28,
975-990 (2004)
52. The Symmetric Downside-Risk Sharpe Ratio and the
Evaluation of Great Investors and Speculators
W. T. Ziemba
Journal of Portfolio Management, 32(1), 108- 122
(2005)
53. Postscript: The Renaissance Medallion Fund
R. E. S. Ziemba and W. T. Ziemba
In Scenarios for Risk Management and Global
Investment Strategies, 295- 298. Wiley (2007)
54. The Kelly Criterion in Blackjack Sports Betting and the
Stock Market
E. O. Thorp
In S. A. Zenios and W. T. Ziemba (Eds.),
Handbook of Asset and Liability Management,
Volume 1, 387- 428. Elsevier (2006)
Bibliography
Author Index
Subject Index
753
769
785
789
833
839
843
--- page 16 ---

xv
Preface
The modern development of the Kelly, or growth optimal, approach to allocating investments began with J .L. Kelly's seminal 1956 paper, over two hundred years after Daniel
Bernoulli's 1738 introduction to the notion of logarithmic utility. Kelly's paper was followed by Latane's (1959) intuitive economic analysis and theoretical advances by Breiman
(1960, 1961). Breiman showed that the Kelly maximization of expected utility with a logarithmic utility function also maximized the long run asymptotic growth of wealth while
minimizing the expected time to reach arbitrarily large goals. Thorp (1962, 1966, 1969,
1971) pioneered the application of the Kelly criterion to actual gambling and investment.
Ziemba and Vickson (1975) surveyed the literature presenting key papers, introductions
and problems up to that time; for an update, see Ziemba and Vickson (2006). Algoet
and Cover (1988) generalized the Breiman results to wider classes of assets and arbitrary
ergodic market processes. MacLean, Ziemba and Blazenko (1992) show applications to
a wide variety of sports and gambling events following Hausch, Ziemba and Rubinstein's
(1981) application to racetrack betting.
Thorp (1960) suggested the term Fort'une '8 Formula which later became the title of William
Poundstone's 2005 book. This was in an abstract for a talk Thorp gave to the American
Mathematical Society in January 1961, presenting his blackjack card counting discovery
and his use of the Kelly approach to size bets in favorable situations. The term Kelly
criterion appears to date from Thorp (1966) and is used in Thorp (1969)
Over the years both theory and practice have developed prolifically. The theory has been
extended to managing portfolios of investments, results have been obtained for a broad
range of distributional assumptions, the simultaneous management of assets and liabilities
has been elaborated upon, and the various properties, advantages and disadvantages have
been clarified.
We now have a fuller understanding of the tradeoff between risk and reward for fractional
Kelly versus full Kelly and for Kelly subject to minimizing the underperformance of a
benchmark or specified desired wealth path.
The theory has also benefitted from the practical experience of gamblers, traders, hedge
v
--- page 17 ---

XVI
Preface
fund managers and investors, especially from some of the greatest investors.
In this volume we present a selection of many of the most important papers from the now
vast and growing literature on the subject. While we could not publish all the important
papers, we feel that the main results appear here.
The volume is organized into six sections that cover the early ideas and contributions,
classic papers and theories, relations to asset allocation including optimization with withdrawals, fractional Kelly wagering and its relations to benchmarks, assessing the good and
bad properties of Kelly wagering, utility foundations and the use of Kelly type strategies
by various investors including the greatest investors.
We thank our authors for their contributions, those who helped us with the editing and
production especially Sandra Schwartz and our publisher, World Scientific, for their production and promotion of this volume. Special thanks go to Tom Cover for many helpful
comments on earlier versions of the introductions and to Bryan Fitzgerald for valuable
data.
Leonard C. MacLean
Edward O. Thorp
William T. Ziemba
March 2010
--- page 18 ---

List of Contributors
Contributors
Andrew R. Barron
Department of Statistics, Yale University,
Connecticut, USA
Bernhard K. Meister
Department of Physics,
Renmin University of China, China
Daniel Bernoulli
University of Basel, Switzerland
David G. Luenberger
Stanford University, Stanford, USA
Donald B. Hausch
School of Business, University of Wisconsin,
Wisconsin, USA
Eckhard Platen
School of Finance and Economics and
Department of Mathematical Sciences,
University of Technology, Sydney, Australia
Edward O. Thorp
Edward O. Thorp and Associates,
Newport Beach, CA, USA
Erik Ordentlich
Hewlett Packard Labs, Palo Alto, California, USA
George Blazenko
School of Business Administration,
Simon Fraser University, British Columbia, Canada
xvii
Chapters
13
21
2
42
46, 47, 48
28
6,7,36,37,38,39,
54
16
24
--- page 19 ---

XV111
List a/Contributors
Contributors
Harry M. Markowitz
IBM Thomas J. Watson Research Center,
Yorktown Heights, New York, USA
Henry A. Latane
Chapel Hill, University of North Carolina, USA
Igor V. Evstigneev
Economics Department, School of Social Sciences,
University of Manchester, UK
John L. Kelly Jr.
Bell Labs, New Jersey, USA
John M. Mulvey
Princeton University, New Jersey, USA
Klaus R. Schenk-Hoppe
Leeds University Business School and
School of Mathematics,
University of Leeds, UK
Leo Breiman
University of California, Los Angeles, USA
Leonard C. MacLean
School of Business Administration,
Dalhousie University, Halifax, Canada
Mark Davis
Department of Mathematics,
Imperial College London, London, UK
Mark Finkelstein
University of California, Irvine, USA
Markus Rudolf
WHU-Otto Beisheim Graduate School of Management,
Dresdner Bank Chair of Finance, Germany
Mehmet Bilgili
Alliance Bernstein, Equity Trading, New York, USA
Chapters
35
4
20,29
3
50
20,29
5
19, 24, 25, 38, 39
27
17
51
50
--- page 20 ---

Contributors
Michael Stutzer
Burridge Center for Securities Analysis and Valuation,
Leeds School of Business, University of Colorado,
Boulder, USA
Nils H. Hakansson
Walter A. Haas School of Business,
University of California, Berkeley, USA
Paul A. Samuelson
Department of Economics,
Massachusetts Institute of Technology, Cambridge, USA
Paul H. Algoet
Boston University, Massachusetts, USA
Rafael Sanegre
University of British Columbia, Canada
Rachel E. S. Ziemba
Roubini Global Economics, London, UK
Raymond G. Vickson
Professor Emeritus,
University of Waterloo, Canada
Robert M. Bell
Stanford University, Stanford, USA
Robert R. Grauer
Simon Fraser University, Canada
Robert Whitley
University of California, Irvine, USA
Richard Roll
Anderson School of Management,
UCLA, Los Angeles, USA
Sebastien Lleo
Department of Mathematics,
Imperial College London, London, UK
List of Contributors
xix
Chapters
43, 44
8,9,41,49
31, 33, 34
14
25
53
32
12
49
17,37
10
27
