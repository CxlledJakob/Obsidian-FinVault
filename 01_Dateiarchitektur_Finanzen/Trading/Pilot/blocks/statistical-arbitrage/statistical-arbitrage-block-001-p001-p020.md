# Statistical Arbitrage_ Algorithmic Trading Insights and -- Karen M_ Sowers; Andrew Pole -- Wiley Finance, 1, 2007 -- Wiley & Sons, Incorporated, John -- isbn13 9780470138441 -- 6b0138550172e24db7f13c932e054fb9 -- An.pdf — pages 1–20

--- page 1 ---
--- page 2 ---

Statistical
Arbitrage
Algorithmic Trading Insights
and Techniques
ANDREW POLE
John Wiley & Sons, Inc.
--- page 3 ---
--- page 4 ---

Statistical
Arbitrage
--- page 5 ---

Founded in 1807, John Wiley & Sons is the oldest independent
publishing company in the United States. With ofﬁces in North
America, Europe, Australia, and Asia. Wiley is globally committed
to developing and marketing print and electronic products and
services for our customers’ professional and personal knowledge and
understanding.
The Wiley Finance series contains books written speciﬁcally for
ﬁnance and investment professionals as well as sophisticated individual investors and their ﬁnancial advisors. Book topics range from
portfolio management to e-commerce, risk management, ﬁnancial
engineering, valuation, and ﬁnancial instrument analysis, as well as
much more.
For a list of available titles, visit our Web site at www.Wiley
Finance.com.
--- page 6 ---

Statistical
Arbitrage
Algorithmic Trading Insights
and Techniques
ANDREW POLE
John Wiley & Sons, Inc.
--- page 7 ---

Copyright c⃝2007 by Andrew Pole. All rights reserved.
Published by John Wiley & Sons, Inc., Hoboken, New Jersey.
Published simultaneously in Canada.
Wiley Bicentennial logo: Richard J. Paciﬁco.
No part of this publication may be reproduced, stored in a retrieval system, or transmitted in
any form or by any means, electronic, mechanical, photocopying, recording, scanning, or
otherwise, except as permitted under Section 107 or 108 of the 1976 United States Copyright
Act, without either the prior written permission of the Publisher, or authorization through
payment of the appropriate per-copy fee to the Copyright Clearance Center, Inc., 222
Rosewood Drive, Danvers, MA 01923, (978) 750-8400, fax (978) 750-4470, or on the Web
at www.copyright.com. Requests to the Publisher for permission should be addressed to the
Permissions Department, John Wiley & Sons, Inc., 111 River Street, Hoboken, NJ 07030,
(201) 748-6011, fax (201) 748-6008, or online at http://www.wiley.com/go/permission.
Limit of Liability/Disclaimer of Warranty: While the publisher and author have used their
best efforts in preparing this book, they make no representations or warranties with respect to
the accuracy or completeness of the contents of this book and speciﬁcally disclaim any implied
warranties of merchantability or ﬁtness for a particular purpose. No warranty may be created
or extended by sales representatives or written sales materials. The advice and strategies
contained herein may not be suitable for your situation. You should consult with a
professional where appropriate. Neither the publisher nor author shall be liable for any loss of
proﬁt or any other commercial damages, including but not limited to special, incidental,
consequential, or other damages.
For general information on our other products and services or for technical support, please
contact our Customer Care Department within the United States at (800) 762-2974, outside
the United States at (317) 572-3993 or fax (317) 572-4002.
Wiley also publishes its books in a variety of electronic formats. Some content that appears in
print may not be available in electronic books. For more information about Wiley products,
visit our Web site at www.wiley.com.
Library of Congress Cataloging-in-Publication Data:
Pole, Andrew, 1961–
Statistical arbitrage : algorithmic trading insights and techniques /
Andrew Pole.
p. cm. — (Wiley ﬁnance series)
Includes bibliographical references and index.
ISBN 978-0-470-13844-1 (cloth)
1. Pairs trading. 2. Arbitrage---Mathematical models. 3. Speculation-
-Mathematical models. I. Title.
HG4661.P65 2007
332.64’5 — dc22
2007026257
ISBN 978-0-470-13844-1
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
--- page 8 ---

To Eliza and Marina
--- page 9 ---
--- page 10 ---

Contents
Preface
xiii
Foreword
xix
Acknowledgments
xxiii
CHAPTER 1
Monte Carlo or Bust
1
Beginning
1
Whither? And Allusions
4
CHAPTER 2
Statistical Arbitrage
9
Introduction
9
Noise Models
10
Reverse Bets
11
Multiple Bets
11
Rule Calibration
12
Spread Margins for Trade Rules
16
Popcorn Process
18
Identifying Pairs
20
Reﬁning Pair Selection
21
Event Analysis
22
Correlation Search in the Twenty-First Century
26
Portfolio Conﬁguration and Risk Control
26
Exposure to Market Factors
29
Market Impact
30
Risk Control Using Event Correlations
31
Dynamics and Calibration
32
Evolutionary Operation: Single Parameter Illustration
34
vii
--- page 11 ---

viii
CONTENTS
CHAPTER 3
Structural Models
37
Introduction
37
Formal Forecast Functions
39
Exponentially Weighted Moving Average
40
Classical Time Series Models
47
Autoregression and Cointegration
47
Dynamic Linear Model
49
Volatility Modeling
50
Pattern Finding Techniques
51
Fractal Analysis
52
Which Return?
52
A Factor Model
53
Factor Analysis
54
Defactored Returns
55
Prediction Model
57
Stochastic Resonance
58
Practical Matters
59
Doubling: A Deeper Perspective
61
Factor Analysis Primer
63
Prediction Model for Defactored Returns
65
CHAPTER 4
Law of Reversion
67
Introduction
67
Model and Result
68
The 75 percent Rule
68
Proof of the 75 percent Rule
69
Analytic Proof of the 75 percent Rule
71
Discrete Counter
73
Generalizations
73
Inhomogeneous Variances
74
Volatility Bursts
75
Numerical Illustration
76
First-Order Serial Correlation
77
Analytic Proof
79
Examples
82
Nonconstant Distributions
82
Applicability of the Result
84
Application to U.S. Bond Futures
85
--- page 12 ---

Contents
ix
Summary
87
Appendix 4.1: Looking Several Days Ahead
87
CHAPTER 5
Gauss Is Not the God of Reversion
91
Introduction
91
Camels and Dromedaries
92
Dry River Flow
95
Some Bells Clang
98
CHAPTER 6
Interstock Volatility
99
Introduction
99
Theoretical Explanation
103
Theory versus Practice
105
Finish the Theory
105
Finish the Examples
106
Primer on Measuring Spread Volatility
108
CHAPTER 7
Quantifying Reversion Opportunities
113
Introduction
113
Reversion in a Stationary Random Process
114
Frequency of Reversionary Moves
117
Amount of Reversion
118
Movements from Quantiles Other Than
the Median
135
Nonstationary Processes: Inhomogeneous Variance
136
Sequentially Structured Variances
136
Sequentially Unstructured Variances
137
Serial Correlation
138
Appendix 7.1: Details of the Lognormal Case in Example 6
139
CHAPTER 8
Nobel Difﬁculties
141
Introduction
141
Event Risk
142
Will Narrowing Spreads Guarantee Proﬁts?
144
Rise of a New Risk Factor
145
--- page 13 ---

x
CONTENTS
Redemption Tension
148
Supercharged Destruction
150
The Story of Regulation Fair Disclosure (FD)
150
Correlation During Loss Episodes
151
CHAPTER 9
Trinity Troubles
155
Introduction
155
Decimalization
156
European Experience
157
Advocating the Devil
158
Stat. Arb. Arbed Away
159
Competition
160
Institutional Investors
163
Volatility Is the Key
163
Interest Rates and Volatility
165
Temporal Considerations
166
Truth in Fiction
174
A Litany of Bad Behavior
174
A Perspective on 2003
178
Realities of Structural Change
179
Recap
180
CHAPTER 10
Arise Black Boxes
183
Introduction
183
Modeling Expected Transaction Volume and Market Impact
185
Dynamic Updating
188
More Black Boxes
189
Market Deﬂation
189
CHAPTER 11
Statistical Arbitrage Rising
191
Catastrophe Process
194
Catastrophic Forecasts
198
Trend Change Identiﬁcation
200
Using the Cuscore to Identify a Catastrophe
202
Is It Over?
204
Catastrophe Theoretic Interpretation
205
Implications for Risk Management
209
--- page 14 ---

Contents
xi
Sign Off
211
Appendix 11.1: Understanding the Cuscore
211
Bibliography
223
Index
225
--- page 15 ---
--- page 16 ---

Preface
T
hese pages tell the story of statistical arbitrage. It is both a history,
describing the ﬁrst days of the strategy’s genesis at Morgan Stanley
in the 1980s through the performance challenging years of the early
twenty-ﬁrst century, and an exegesis of how and why it works. The
presentation is from ﬁrst principles and largely remains at the level
of a basic analytical framework. Nearly all temptation to compose
a technical treatise has been resisted with the goal of contributing a
work that will be readily accessible to the larger portion of interested
readership. I say ‘‘nearly all’’: Chapter 7 and the appendix to Chapter
11 probably belong to the category of ‘‘temptation not resisted.’’
Much of what is done by more sophisticated practitioners is discussed
in conceptual terms, with demonstrations restricted to models that
will be familiar to most readers. The notion of a pair trade—the
progenitor of statistical arbitrage—is employed to this didactic end
rather more broadly than actual trading utility admits. In adopting
this approach, one runs the risk of the work being dismissed as
a pairs trading manual; one’s experience, intent, and aspirations
for the text are more extensive, but the inevitability of the former
is anticipated. In practical trading terms, the simple, unelaborated
pair scheme is no longer very proﬁtable, nonetheless it remains a
valuable tool for explication, retaining the capacity to demonstrate
insight, modeling, and analysis while not clouding matters through
complexity. After a quarter century in the marketplace, for proﬁtable
schemes beyond paper understanding and illustration, one needs to
add some structural complexity and analytical subtlety.
One elaboration alluded to in the text is the assembling of a set
of similar pairs (without getting into much detail on what metrics
are used to gauge the degree of similarity), often designated as a
group. Modeling such groups can be done in several ways, with some
practitioners preferring to anchor a group on a notional archetype,
structuring forecasts in terms of deviation of tradable pairs from the
archetype; others create a formal implementation of the cohort as
xiii
--- page 17 ---

xiv
PREFACE
a gestalt or a synthetic instrument. Both of those approaches, and
others, can be formally analyzed as a hierarchical model, greatly
in vogue (and greatly productive of insight and application) in
mainstream statistical thinking for two decades; add to the standard
static structure the dynamic element in a time series setting and one is
very quickly building an analytical structure of greater sophistication
than routinely used as the didactic tool in this book. Nonetheless,
all such modeling developments rely on the insight and techniques
detailed herein.
Those readers with deeper knowledge of mathematical and statistical science will, hopefully, quickly see where the presentation can
be taken.
Maintaining focus on the structurally simple pair scheme invites
readers to treat this book as an explicit ‘‘how to’’ manual. From
this perspective, one may learn a reasonable history of the what
and the how and a decent knowledge of why it is possible. Contemporary successful execution will require from the reader some
additional thought and directed exploration as foregoing remarks
have indicated. For that task, the book serves as a map showing
major features and indicating where the reader must get out a compass and notebook. The old cartographers’ device ‘‘Here be dragons’’
might be usefully remembered when you venture thus.
The text has, unashamedly, a statistician’s viewpoint: Models can
be useful. Maintaining a model’s utility is one theme of the book.
The statistician’s preoccupation with understanding variation—the
appreciation of the knowledge that one’s models are wrong, though
useful, and that the nature of the wrongness is illuminated by the
structure of ‘‘errors’’ (discrepancies between observations and what
a model predicts) is another theme of the book. Or, rather, not a
distinct theme, but an overriding, guiding context for the material.
The notion of a pair trade is introduced in Chapter 1 and
elaborated upon in Chapter 2. Following explication and exempliﬁ-
cation, two simple theoretical models for the underlying phenomenon
exploited by pairs, reversion, are proposed. These models are used
throughout the text to study what is possible, illuminate how the possibilities might be exploited, consider what kinds of change would
have negative impact on exploitation, and characterize the nature
of the impact. Approaches for selecting a universe of instruments
for modeling and trading are described. Consideration of change is
--- page 18 ---

Preface
xv
introduced from this ﬁrst toe dipping into analysis, because temporal
dynamics underpin the entirety of the project. Without the dynamic
there is no arbitrage.
In Chapter 3 we increase the depth and breadth of the analysis,
expanding the modeling scope from simple observational rules1 for
pairs to formal statistical models for more general portfolios. Several
popular models for time series are described but detailed focus is on
weighted moving averages at one extreme of complexity and factor
analysis at another, these extremes serving to carry the message as
clearly as we can make it. Pair spreads are referred to throughout
the text serving, as already noted, as the simplest practical illustrator
of the notions discussed. Where necessary to make our urgencies
sensible, direct mention is made of other aspects of the arbitrageur’s
concern, including portfolio optimization and factor exposures. For
the most part though, incursions into multivariate territory are
avoided. Volatility modeling (and the fascinating idea of stochastic
resonance) are treated separately here and in Chapter 6; elsewhere
discussion is subsumed in that of the mean forecast process.
Chapter 4 presents a probability theorem that illuminates the
prevalence of price moves amenable to exploitation by the simple
rules ﬁrst applied in the late 1980s. The insight of this result guides
evaluation of exploitation strategies. Are results borne of brilliance
on the part of a modeler or would a high school graduate perform
similarly because the result is driven by structural dynamics, long
in the public domain, revealed by careful observation alone? Many
a claim of a ‘‘high’’ proportion of winning bets by a statistical
arbitrageur has more to do with the latter than any sophistication
of basic spread modeling or (importantly) risk management. When
markets are disrupted and the conditions underlying the theoretical
result are grossly violated, comparative practitioner performance
reveals much about basic understanding of the nature of the process
1There is no pejorative intent in the use of the term: The rules were effective. Statistical
content was limited to measurement of range of variation; no distributional study,
model formulation, estimation, error analysis, or forecasting was undertaken prior
to milking the observational insight. Those activities came soon enough—after the
proﬁts were piling up. With the expanded statistical study, adding trading experience
to historical data, came insight into subtleties of the stock price motions exploited
and the market forces driving repetitious occurrence of opportunities.
--- page 19 ---

xvi
PREFACE
being exploited. Knowledge of the theoretical results often reveals
itself more when assumptions are violated than when things are hunky
dory and managers with solid understanding and those operating
intellectually blind generate positive returns in equal measure. (Tony
O’Hagan suggested that the basic probability result is long known,
but I have been unable to trace it. Perhaps the result is too trivial
to be a named result and exists as a simple consequence, a textbook
exercise, of basic distribution theory. No matter, the implication
remains profoundly signiﬁcant to the statistical arbitrage story.)
Chapter 5 critiques a published article (whose authors remain
anonymous here to protect their embarrassment) to clarify the broad
conditions under which the phenomenon of reversion occurs. A central role for the normal distribution is dismissed. The twin erroneous
claims that (a) a price series must exhibit a normal marginal distribution for reversion to occur, and (b) a series exhibiting a normal
marginal distribution necessarily exhibits reversion are unceremoniously dispelled. There is reversion anywhere and everywhere, as
Chapter 4 demonstrates.
Chapter 6 answers the question, important for quantifying the
magnitude of exploitable opportunities in reversion gambits, ‘‘How
much volatility is there in a spread?’’
Chapter 7 is for the enthusiast not easily dissuaded by the presence
of the many hieroglyphs of the probability calculus. Anyone with
a good ﬁrst course in probability theory can follow the arguments,
and most can manage the detailed derivations, too. The mechanics
are not enormously complicated. Some of the conceptual distinctions
may be challenging at ﬁrst—read it twice! The effort will be repaid
as there is signiﬁcant practical insight in the examples considered
at length. Knowledge of how close theoretical abstractions come
to reﬂecting measurable features of actual price series is invaluable
in assessing modeling possibilities and simulation or trading results.
Notwithstanding that remark, it is true that the remainder of the book
does not rely on familiarity with the material in Chapter 7. While
you may miss some of the subtlety in the subsequent discussions, you
will not lack understanding for omitting attention to this chapter.
Chapters 8 through 10 might have been labeled ‘‘The Fall,’’ as
they characterize the problems that beset statistical arbitrage beginning in 2000 and directly caused the catastrophic drop in return
during 2002–2004. An important lesson from this history is that
there was not a single condition or set of conditions that abruptly
--- page 20 ---

Preface
xvii
changed in 2000 and thereby eliminated forecast performance of
statistical arbitrage models. What a story that would be! Far more
dramatic than the prosaic reality, which is a complex mix of multiple
causes and timings. All the familiar one liners, including decimalization, competition, and low volatility, had (and have) their moment,
but none individually, nor the combination, can have delivered a blow
to ﬁnancial markets. Fundamentally altering the price dynamics of
markets in ways that drastically diminish the economic potential in
reversion schemes, mining value across the spectrum from the very
high frequency hare of intra-day to the venerable tortoise of a month
or more, requires a more profound explanation.
Change upon change upon change cataloged in Chapter 9 is at
the root of the dearth of return to statistical arbitrage in 2002–2004.
(Performance deterioration in 2000–2002 was evident but limited
to a subset of practitioners.) This unusual episode in recent U.S.
macroeconomic history is over, but the effects linger in the ﬁnancial
markets reﬂecting emergent properties of the collective behavior of
millions of investors; and surely those investors continue to embody,
no matter how lingering, those changes and the causes thereof.
The shift of trading from the ﬂoor of the New York Stock
Exchange to internal exchanges, in the guise of computer algorithms designed by large brokerage houses and investment banks, has
cumulatively become a change with glacier-like implacability. Slow.
Massive. Irresistible. Crushing. Reforming.2 A frequently remarked
facet of the evolving dynamics is the decline of market volatility.
Where has market volatility gone? In large part the algorithms have
eaten it. Reduce the voice of a single participant yelling in a crowd and
the babel is unaffected. Quite a signiﬁcant proportion of participants
and the reduced babel is oddly deafening. Now that computer programs (Chapter 10) ‘‘manage’’ over 60 percent of U.S. equity trades
among ‘‘themselves’’ the extraodinary result is akin to administering
a dose of ritalin to the hyperactive market child. In the commentary
on low volatility two themes stand out: one is a lament over the lack
2One major structural consequence, fed also by technical advance in the credit markets and the development of Exchange Traded Funds, is literally the forming anew
of patterns of price behavior detemined by the interaction of computer algorithms
as agents for share dealings. In addition to this re-forming, reform is simultaneously
underway with changes to Securities Exchange Commission regulations and NYSE
rules.
