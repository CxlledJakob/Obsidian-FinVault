# Cycle Analytics for Traders (Advanced Technical Trading -- Ehlers, John F_ -- 10_1002_9781118728611, 2013 nov 18 -- John Wiley & Sons, Inc_ -- doi 10_1002_9781118728611 -- 1af2315757f5680b2f83029a006fd7ab -- Anna’s .pdf — Front matter (pages 1–11)

--- page 1 ---

CYCLE ANALYTICS FOR
TR
T ADERS
--- page 2 ---

CYC
Y LE ANA
N LYTICS
FOR TR
T ADERS
Advanced Technical Trading
Concepts
John F. Ehlers
--- page 3 ---

Cover image: Chart © iStockphoto.com/Andrey Prokhorov
Cover design: Wiley
Copyright © 2013 by John F. Ehlers. All rights reserved.
Published by John Wiley & Sons, Inc., Hoboken, New Jersey.
Published simultaneously in Canada.
No part of this publication may be reproduced, stored in a retrieval system, or transmitted in any
form or by any means, electronic, mechanical, photocopying, recording, scanning, or otherwise,
except as permitted under Section 107 or 108 of the 1976 United States Copyright Act, without
either the prior written permission of the Publisher, or authorization through payment of the
appropriate per-copy fee to the Copyright Clearance Center, Inc., 222 Rosewood Drive, Danvers,
MA 01923, (978) 750-8400, fax (978) 646-8600, or on the Web at www.copyright.com. Requests
to the Publisher for permission should be addressed to the Permissions Department, John Wiley &
Sons, Inc., 111 River Street, Hoboken, NJ 07030, (201) 748-6011, fax (201) 748-6008, or online
at www.wiley.com/go/permissions.
Limit of Liability/Disclaimer of Warranty: While the publisher and author have used their best efforts
in preparing this book, they make no representations or warranties with respect to the accuracy
or completeness of the contents of this book and specifically disclaim any implied warranties of
merchantability or fitness for a particular purpose. No warranty may be created or extended by
sales representatives or written sales materials. The advice and strategies contained herein may not
be suitable for your situation. You should consult with a professional where appropriate. Neither the
publisher nor author shall be liable for any loss of profit or any other commercial damages, including
but not limited to special, incidental, consequential, or other damages.
For general information on our other products and services or for technical support, please contact
our Customer Care Department within the United States at (800) 762-2974, outside the United
States at (317) 572-3993 or fax (317) 572-4002.
Wiley publishes in a variety of print and electronic formats and by print-on-demand. Some material
included with standard print versions of this book may not be included in e-books or in printon-demand. If this book refers to media such as a CD or DVD that is not included in the version
you purchased, you may download this material at http://booksupport.wiley.com. For more
information about Wiley products, visit www.wiley.com.
Library of Congress Cataloging-in-Publication Data:
Ehlers, John F., 1933-
Cycle analytics for traders : advanced technical trading concepts / John F. Ehlers.
pages cm
ISBN 978-1-118-72851-2 (cloth) — ISBN 978-1-118-72841-3 (ebk) — ISBN 978-1-118-72860-4
(ebk)
1. Technical analysis (Investment analysis)
2. Investment analysis.
I. Title.
HG4529.E388 2014
332.63’2042 — dc23
2013034306
Printed in the United States of America
10   9   8   7   6   5   4   3   2   1
--- page 4 ---

v
C O N T E N T S
Preface
ix
About the Author
xiii
CHAPTER 1
Unified Filter Theory
1
Transfer Response
1
Nonrecursive Filters
3
Recursive Filters
8
Generalized Filters
10
Programming the Filters
11
Wave Amplitude, Power, and Decibels (dB)
13
Key Points to Remember
13
CHAPTER 2
SMAs, EMAs, or Other?
15
Simple Moving Averages (SMAs)
15
Exponential Moving Averages (EMAs)
18
Weighted Moving Averages (WMAs)
21
Median Filter
22
Key Points to Remember
23
CHAPTER 3
Smoothing Filters on Steroids
25
Nonrecursive Filters
25
Modified Simple Moving Averages
29
Modified Least-Squares Quadratics
30
SuperSmoother
31
--- page 5 ---

vi
CONTENTS
SuperSmoother Filter Applications
34
Key Points to Remember
36
CHAPTER 4
Decyclers
39
Decycler Construction
39
Decycler Application
41
Decycler Oscillator
43
Key Points to Remember
45
CHAPTER 5
Band-Pass Filters
47
Band-Pass Filter
47
Band-Pass Filter Q
51
Automatic Gain Control (AGC)
54
Spectral Dilation Removal
56
Band-Pass Filter
56
Measuring the Cycle Period
58
Key Points to Remember
61
CHAPTER 6
Market Structure and the Hurst Coefficient
63
Fractal Dimension
65
Computing the Hurst Coefficient
67
The Hurst Coefficient in Action
68
Drunkard’s Walk Hypothesis for Market Structure
70
Key Points to Remember
74
CHAPTER 7
Spectral Dilation
77
Frequency Content of Indicator Outputs
77
Roofing Filter as an Indicator
80
Impact of Spectral Dilation on
Conventional Indicators
83
Key Points to Remember
88
CHAPTER 8
Autocorrelation
91
Background
91
Autocorrelation
93
Autocorrelation Periodogram
102
Autocorrelation Reversals
110
Key Points to Remember
113
--- page 6 ---

vii
 CONTENTS
CHAPTER 9 FourierTransforms
T
115
Spectral Dilation
116
Discrete Fourier Transform (DFT)
117
Key Points to Remember
124
CHAPTER 10 Comb Filter Spectral Estimates
125
Spectral Dilation
125
Computing a Comb Filter Spectral Estimate
126
Key Points to Remember
133
CHAPTER 11 Adaptive Filters
135
Adaptive Relative Strength Index (RSI)
135
Adaptive Stochastic Indicator
142
Adaptive CCI (Commodity Channel Index)
147
Adaptive Band-Pass Filter
152
Adaptive Indicator Comparison
157
Key Points to Remember
158
CHAPTER 12 The Even Better Sinewave Indicator
159
Even Better Sinewave Approach
160
Even Better Sinewave Description
160
Using the Even Better Sinewave Indicator
162
Key Points to Remember
164
CHAPTER 13 Convolution
165
Theoretical Foundation
165
Heat Map Display
168
Computing Convolution
169
Key Points to Remember
174
CHAPTER 14 The HilbertTransformer
T
175
Analytic Signals
176
Hilbert Transformer Mathematics
177
Computing the Hilbert Transformer
181
The Hilbert Transformer Indicator
183
Using the Hilbert Transformer to
Compute the Dominant Cycle
186
--- page 7 ---

viii
CONTENTS
Dual Differentiator
187
Phase Accumulation
189
Homodyne
192
Key Points to Remember
194
CHAPTER 15 IndicatorTransforms
T
195
Fisher Transform
195
Inverse Fisher Transform
198
Cube Transform
200
Key Points to Remember
202
CHAPTER 16 SwamiCharts
203
SwamiCharts Overview
204
SwamiCharts RSI
205
SwamiCharts Stochastic
210
Roll Your Own SwamiCharts
216
Key Points to Remember
216
CHAPTER 17 Swing-Trading
T
Strategies
217
Conventional Wisdom
219
Anticipating the Turning Point
220
Sine Wave Uniqueness
221
Safety Valve
224
Exiting a Trade
225
Stop Loss
225
Evaluating a Trading Strategy
226
Monte Carlo Evaluation
227
Stockspotter.com
228
Key Points to Remember
229
About the Website
231
Index
233
--- page 8 ---

ix
P R E FA C E
I
t has been over 10 years since Rocket Science for Traders was published. In
those days, technical analysis was primarily the province of futures traders,
while portfolio theory and fundamental analysis comprised the conventional
wisdom for equity traders. However, there have been profound changes in
the marketplace since that time. Futures trading has lost popularity because
of scandals involving segregated customer accounts, the stock market’s relentless trend upward has been broken with the result that buy-and-hold
is no longer a valid investment strategy, and new trading vehicles such as
exchange-traded funds (ETFs) have evolved. In addition, commission rates
have decreased, and the Internet has made electronic trading available to
everyone. All this has caused investors to be more involved in the trading
process and interested in self-directed trading. Major brokerage houses have
responded by including technical analysis tools in their trading platforms.
This is a technical resource book written for self-directed traders who
want to understand the scientific underpinnings of the filters and indicators
they use in their trading decisions rather than to use the trading tools on
blind faith. There is plenty of theory and years of research behind the unique
solutions provided in this book, but the emphasis is on simplicity rather than
mathematical purity. In particular, the solutions use a pragmatic approach
to attain effective trading results. The concepts are presented so they can be
understood with only a background in algebra. The writing style in the book
is intentionally terse so the reader doesn’t need to wade through a mountain of words to find the ideas being presented. EasyLanguage computer
code is used to calculate and display the indicators. From my viewpoint,
--- page 9 ---

x
PREFACE
EasyLanguage is just a dialect of Pascal with key words for trading. Therefore, the code should be nearly as readable as English.
Cycles are unique because they are one of the few characteristics of market data that can be scientifically measured. However, cycle measurement is
extremely complex. In the most general sense, there is a triple infinity of
parameters–period, phase, and amplitude–that must be identified simultaneously to completely describe the cycles. Additionally, market cycles are
ephemeral and are often buried in pure noise. So the compromises begin.
One of the first realizations that a trader must make is that cycles cannot be
the basis of trades all the time. Sometimes the cycle swings are swamped by
trends, and it is folly to try to fight the trend. However, the cyclic swings can
be helpful to know when to buy on a dip in the direction of the trend. Traditional indicators such as Stochastics, relative strength index (RSI), moving
average convergence/divergence (MACD), and commodity channel index
(CCI) are subject to the same constraints, and therefore this book will lead
to a greater understanding of all technical indicators.
Most important, Cycle Analytics for Traders will allow traders to think of
their indicators and trading strategies in the frequency domain as well as
their motions in the time domain. This new viewpoint will enable them to
select the most efficient filter lengths for the job at hand. The descriptions
are written for understanding at several different levels. Traders with little
mathematical background will be able to assess general market conditions
to their advantage. More technically advanced traders will be able to create
indicators and strategies that automatically adapt to measured market conditions by using combinations of computer code that are described.
So what should a trader take away from this book? These are a few of the
new concepts that I have ranked in priority:

■An awareness of Spectral Dilation, and how to eliminate it or to use it to
your advantage.

■How to use automatic gain control (AGC) to normalize indicator amplitude swings.

■Thinking of prices in the frequency domain as well as in the time domain.

■An awareness that all indicators are statistical rather than absolute, as
implied by their single-line displays.

■Several advanced cookbook filters. These include the SuperSmoother, roof-f
ing filter, even better sinewave, decycler, and Hilbert Transform Indicator.
--- page 10 ---

xi
 PREFACE

■Several different methods of estimating market spectra and sifting out
the dominant cycle, with the autocorrelation periodogram being the preferred method.

■How to use transforms to improve the display and interpretation of indicators.
The concepts I have developed and derived from scientific principles are
new and useful aids to short-term trading. Ultimately, trading comes down
to buying and selling decisions. These decisions are never easy, and in the
final chapter I unite the concepts with a few tips and tricks that I have acquired in my years of trading. Above all, trading should be approached as a
statistical process. Even with a good performance of 60 percent winning
trades, 60 percent is a lot closer to 50–50 than it is to 100 percent regarding
a single event. Therefore, the performance judged by a few trades is invalid,
and I would encourage readers to stick with a trading strategy they have
developed with a profitable history, albeit hypothetical, and let the statistics
be the light to success in the long run.
As evidence of my warped sense of humor, each chapter starts with a
“Tom Swifty” pun that encapsulates the entire content of the chapter and
I hope serves as an anchor for the reader’s memory. I think the computer
code is often the most succinct and efficient method of describing a concept. Accordingly, my style is to be brief, with plenty of poetic license with
mathematical notation in an effort to convey the concepts to most traders.
Each chapter concludes with the significant points to remember from that
chapter.
I wish you all good trading.
John F. Ehlers
August 2013
--- page 11 ---

A B O U T T H E A U T H O R
xiii
J
ohn Ehlers is an electrical engineer, receiving his BSEE and MSEE
from the University of Missouri. He did his doctoral work at The
George Washington University, specializing in Fields & Waves and Information Theory. He has retired as a senior engineering fellow from Raytheon.
He has been a private trader since 1976.
John is a pioneer in introducing the MESA cycles-measuring algorithm
and the use of digital signal processing in technical analysis. He developed
maximum entropy spectrum analysis (MESA) over three decades ago. The
program has evolved with the increased capacity of modern computers.
John has written extensively about quantitative algorithmic trading
using advanced DSP (digital signal processing) and has spoken internationally on the subject. His books include MESA and Trading Market Cycles, Rocket
Science for Traders, and Cybernetic Analysis for Stocks and Futures. His approach
is unique. Any technique must first work on theoretical waveforms before
testing against real-world data is attempted.
John is a cofounder of StockSpotter.com.
