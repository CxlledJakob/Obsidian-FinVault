# Quantitative Trading_ How to Build Your Own Algorithmic -- Ernest P_ Chan -- Wiley Trading, 1, 2008 -- John Wiley & Sons, Ltd_ -- isbn13 9780470284889 -- e4d660df1c1a75e8676a28ff4f852fa7 -- Anna’s Archive.pdf — Front matter (pages 1–20)

--- page 1 ---

Wiley Trading
E R N E ST P. C H A N
How to Build Your Own Algorithmic Trading Business
Quantitative
Trading
--- page 2 ---
--- page 3 ---

Quantitative
Trading
--- page 4 ---

Founded in 1807, John Wiley & Sons is the oldest independent publishing company in the United States. With ofﬁces in North America, Europe,
Australia, and Asia, Wiley is globally committed to developing and marketing print and electronic products and services for our customers’ professional and personal knowledge and understanding.
The Wiley Trading series features books by traders who have survived
the market’s ever changing temperament and have prospered—some by
reinventing systems, others by getting back to basics. Whether a novice
trader, professional, or somewhere in-between, these books will provide
the advice and strategies needed to prosper today and well into the future.
For a list of available titles, visit our Web site at www.WileyFinance.com.
--- page 5 ---

Quantitative
Trading
How to Build Your Own
Algorithmic Trading Business
ERNEST P. CHAN
John Wiley & Sons, Inc.
--- page 6 ---

Copyright C⃝2009 by Ernest P. Chan. All rights reserved.
Published by John Wiley & Sons, Inc., Hoboken, New Jersey.
Published simultaneously in Canada.
No part of this publication may be reproduced, stored in a retrieval system, or transmitted in
any form or by any means, electronic, mechanical, photocopying, recording, scanning, or otherwise, except as permitted under Section 107 or 108 of the 1976 United States Copyright Act,
without either the prior written permission of the Publisher, or authorization through payment
of the appropriate per-copy fee to the Copyright Clearance Center, Inc., 222 Rosewood Drive,
Danvers, MA 01923, (978) 750-8400, fax (978) 646-8600, or on the web at www.copyright.com.
Requests to the Publisher for permission should be addressed to the Permissions Department,
John Wiley & Sons, Inc., 111 River Street, Hoboken, NJ 07030, (201) 748-6011, fax (201) 748-
6008, or online at http://www.wiley.com/go/permissions.
Limit of Liability/Disclaimer of Warranty: While the publisher and author have used their best
efforts in preparing this book, they make no representations or warranties with respect to the
accuracy or completeness of the contents of this book and speciﬁcally disclaim any implied
warranties of merchantability or ﬁtness for a particular purpose. No warranty may be created
or extended by sales representatives or written sales materials. The advice and strategies contained herein may not be suitable for your situation. You should consult with a professional
where appropriate. Neither the publisher nor author shall be liable for any loss of proﬁt or any
other commercial damages, including but not limited to special, incidental, consequential, or
other damages.
For general information on our other products and services or for technical support, please
contact our Customer Care Department within the United States at (800) 762-2974, outside the
United States at (317) 572-3993 or fax (317) 572-4002.
Wiley also publishes its books in a variety of electronic formats. Some content that appears
in print may not be available in electronic books. For more information about Wiley products,
visit our web site at www.wiley.com.
Library of Congress Cataloging-in-Publication Data
Chan, Ernest P.
Quantitative trading: how to build your own algorithmic trading business / Ernest P. Chan.
p. cm.–(Wiley trading series)
Includes bibliographical references and index.
ISBN 978-0-470-28488-9 (cloth)
1. Investment analysis.
2. Stocks.
3. Stockbrokers.
I. Title.
HG4529.C445
2009
332.64–dc22
2008020125
Printed in the United States of America.
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
--- page 7 ---

To my parents Hung Yip and Ching, and to Ben.
--- page 8 ---
--- page 9 ---

Contents
Preface
xi
Acknowledgments
xvii
CHAPTER 1
The Whats, Whos, and Whys of Quantitative
Trading
1
Who Can Become a Quantitative Trader?
2
The Business Case for Quantitative Trading
4
Scalability
5
Demand on Time
5
The Nonnecessity of Marketing
7
The Way Forward
8
CHAPTER 2
Fishing for Ideas
9
How to Identify a Strategy That Suits You
12
Your Working Hours
12
Your Programming Skills
13
Your Trading Capital
13
Your Goal
16
A Taste for Plausible Strategies and Their Pitfalls
17
How Does It Compare with a Benchmark and How Consistent
Are Its Returns?
18
How Deep and Long Is the Drawdown?
21
How Will Transaction Costs Aﬀect the Strategy?
22
Does the Data Suﬀer from Survivorship Bias?
24
How Did the Performance of the Strategy Change over the Years?
24
vii
--- page 10 ---

viii
CONTENTS
Does the Strategy Suﬀer from Data-Snooping Bias?
25
Does the Strategy “Fly under the Radar" of Institutional
Money Managers?
27
Summary
28
CHAPTER 3
Backtesting
31
Common Backtesting Platforms
32
Excel
32
MATLAB
32
TradeStation
35
High-End Backtesting Platforms
35
Finding and Using Historical Databases
36
Are the Data Split and Dividend Adjusted?
36
Are the Data Survivorship Bias Free?
40
Does Your Strategy Use High and Low Data?
42
Performance Measurement
43
Common Backtesting Pitfalls to Avoid
50
Look-Ahead Bias
51
Data-Snooping Bias
52
Transaction Costs
60
Strategy Reﬁnement
65
Summary
66
CHAPTER 4
Setting Up Your Business
69
Business Structure: Retail or Proprietary?
69
Choosing a Brokerage or Proprietary Trading Firm
71
Physical Infrastructure
75
Summary
77
CHAPTER 5
Execution Systems
79
What an Automated Trading System Can Do for You
79
Building a Semiautomated Trading System
81
Building a Fully Automated Trading System
84
Minimizing Transaction Costs
87
--- page 11 ---

Contents
ix
Testing Your System by Paper Trading
89
Why Does Actual Performance Diverge from Expectations?
90
Summary
92
CHAPTER 6
Money and Risk Management
95
Optimal Capital Allocation and Leverage
95
Risk Management
103
Psychological Preparedness
108
Summary
111
Appendix: A Simple Derivation of the Kelly Formula when
Return Distribution Is Gaussian
112
CHAPTER 7
Special Topics in Quantitative Trading
115
Mean-Reverting versus Momentum Strategies
116
Regime Switching
119
Stationarity and Cointegration
126
Factor Models
133
What Is Your Exit Strategy?
140
Seasonal Trading Strategies
143
High-Frequency Trading Strategies
151
Is It Better to Have a High-Leverage versus
a High-Beta Portfolio?
153
Summary
154
CHAPTER 8
Conclusion: Can Independent Traders
Succeed?
157
Next Steps
161
Appendix
A Quick Survey of MATLAB
163
Bibliography
169
About the Author
173
Index
175
--- page 12 ---
--- page 13 ---

Preface
B
y some estimates, quantitative or algorithmic trading now accounts for over one-third of the trading volume in the United
States. There are, of course, innumerable books on the advanced mathematics and strategies utilized by institutional traders
in this arena. However, can an independent, retail trader beneﬁt
from these algorithms? Can an individual with limited resources and
computing power backtest and execute their strategies over thousands of stocks, and come to challenge the powerful industry participants in their own game?
I will show you how this can, in fact, be achieved.
WHO IS THIS BOOK FOR?
I wrote this book with two types of readers in mind:
1. Aspiring independent (“retail”) traders who are looking to start
a quantitative trading business.
2. Students of ﬁnance or other technical disciplines (at the undergraduate or MBA level) who aspire to become quantitative
traders and portfolio managers at major institutions.
Can these two very different groups of readers beneﬁt from the
same set of knowledge and skills? Is there anything common between managing a $100 million portfolio and managing a $100,000
portfolio? My contention is that it is much more logical and sensible for someone to become a proﬁtable $100,000 trader before
xi
--- page 14 ---

xii
PREFACE
becoming a proﬁtable $100 million trader. This can be shown to be
true on many fronts.
Many legendary quantitative hedge fund managers such as Dr.
Edward Thorp of the former Princeton-Newport Partners (Poundstone, 2005) and Dr. Jim Simons of Renaissance Technologies Corp.
(Lux, 2000) started their careers trading their own money. They did
not begin as portfolio managers for investment banks and hedge
funds before starting their own fund management business. Of
course, there are also plenty of counterexamples, but clearly this
is a possible route to riches as well as intellectual accomplishment,
and for someone with an entrepreneurial bent, a preferred route.
Even if your goal is to become an institutional trader, it is still
worthwhile to start your own trading business as a ﬁrst step. Physicists and mathematicians are now swarming Wall Street. Few people on the Street are impressed by a mere PhD from a prestigious
university anymore. What is the surest way to get through the door
of the top banks and funds? To show that you have a systematic
way to proﬁts—in other words, a track record. Quite apart from
serving as a stepping stone to a lucrative career in big institutions,
having a proﬁtable track record as an independent trader is an invaluable experience in itself. The experience forces you to focus on
simple but proﬁtable strategies, and not get sidetracked by overly
theoretical or sophisticated theories. It also forces you to focus
on the nitty-gritty of quantitative trading that you won’t learn from
most books: things such as how to build an order entry system that
doesn’t cost $10,000 of programming resource. Most importantly, it
forces you to focus on risk management—after all, your own personal bankruptcy is a possibility here. Finally, having been an institutional as well as a retail quantitative trader and strategist at different times, I only wish that I had read a similar book before I started
my career at a bank—I would have achieved proﬁtability many
years sooner.
Given these preambles, I won’t make any further apologies in
the rest of the book in focusing on the entrepreneurial, independent traders and how they can build a quantitative trading business
on their own, while hoping that many of the lessons would be useful
on their way to institutional money management as well.
--- page 15 ---

Preface
xiii
WHAT KIND OF BACKGROUND DO YOU NEED?
Despite the scary-sounding title, you don’t need to be a math or
computer whiz in order to use this book as a guide to start trading
quantitatively. Yes, you do need to possess some basic knowledge
of statistics, such as how to calculate averages, standard deviations,
or how to ﬁt a straight line through a set of data points. Yes, you
also need to have some basic familiarity with Excel. But what you
don’t need is any advanced knowledge of stochastic calculus, neural
networks, or other impressive-sounding techniques.
Though it is true that you can make millions with nothing more
than Excel, it is also true that there is another tool that, if you are
proﬁcient at it, will enable you to backtest trading strategies much
more efﬁciently, and may also allow you to retrieve and process
data much more easily than you otherwise can. This tool is called
MATLAB®, and it is a mathematical platform that many institutional
quantitative strategists and portfolio managers use. Therefore, I will
demonstrate how to backtest the majority of strategies using MAT-
LAB. In fact, I have included a brief tutorial in the appendix on how
to do some basic programming in MATLAB. For many retail traders,
MATLAB is too expensive to purchase, but there are cheaper alternatives, which I will mention in Chapter 3 on backtesting. Furthermore, many university students can either purchase a cheaper student MATLAB license or they already have free access to it through
their schools.
WHAT WILL YOU FIND IN THIS BOOK?
This book is deﬁnitely not designed as an encyclopedia of quantitative trading techniques or terminologies. It will not even be about
speciﬁc proﬁtable strategies (although you can reﬁne the few example strategies embedded here to make them quite proﬁtable.) Instead, this is a book that teaches you how to ﬁnd a proﬁtable strategy
yourself. It teaches you the characteristics of a good strategy, how
to reﬁne and backtest a strategy to ensure that it has good historical
performance, and, more importantly, to ensure that it will remain
--- page 16 ---

xiv
PREFACE
proﬁtable in the future. It teaches you a systematic way to scale up
or wind down your strategies depending on their real-life proﬁtability. It teaches you some of the nuts and bolts of implementing an automated execution system in your own home. Finally, it teaches you
some basics of risk management, which is critical if you want to survive over the long term, and also some psychological pitfalls to avoid
if you want an enjoyable (and not just proﬁtable) life as a trader.
Even though the basic techniques for ﬁnding a good strategy
should work for any tradable securities, I have focused my examples on an area of trading I personally know best: statistical
arbitrage trading in stocks. While I discuss sources of historical
data on stocks, futures, and foreign currencies in the chapter on
backtesting, I did not include options because those are not in my
area of expertise.
The book is organized roughly in the order of the steps that
traders need to undertake to set up their quantitative trading business. These steps begin at ﬁnding a viable trading strategy (Chapter 2), then backtesting the strategy to ensure that it at least has
good historical performance (Chapter 3), setting up the business
and technological infrastructure (Chapter 4), building an automated
trading system to execute your strategy (Chapter 5), and managing
the money and risks involved in holding positions generated by this
strategy (Chapter 6). I will then describe in Chapter 7 a number of
important advanced concepts with which most professional quantitative traders are familiar, and ﬁnally conclude in Chapter 8 with
reﬂections on how independent traders can ﬁnd their niche and how
they can grow their business. I have also included an appendix that
contains a tutorial on using MATLAB.
You’ll see two different types of boxed material in this book:
r Sidebars containing an elaboration or illustration of a concept, and
r Examples, accompanied by MATLAB or Excel code.
--- page 17 ---

Preface
xv
For readers who want to learn more and keep up to date with
the latest news, ideas, and trends in quantitative trading, they are
welcome to visit my blog epchan.blogspot.com, where I will do my
best to answer their questions, as well as my premium content web
site epchan.com/subscriptions. My premium content web site contains articles of a more advanced nature, as well as backtest results
of several proﬁtable strategies. Readers of this book will have free
access to the premium content and will ﬁnd the password in a later
chapter to enter that web site.
—ERNEST P. CHAN
Toronto, Ontario
August 2008
--- page 18 ---
--- page 19 ---

Acknowledgments
M
uch of my knowledge and experiences in quantitative trading come from my colleagues and mentors at the various investment banks (Morgan Stanley, Credit Suisse,
Maple Securities) and hedge funds (Mapleridge Capital, Millennium Partners, MANE Fund Management), and I am very grateful for their advice, guidance, and help over the years. Since I
became an independent trader and consultant, I have beneﬁted
enormously from discussions with my clients, readers of my blog,
fellow bloggers, and various trader-collaborators. In particular, I
would like to offer thanks to Steve Halpern and Ramon Cummins for reading parts of the manuscript and correcting some
of the errors; to John Rigg for suggesting some of the topics
for my blog, many of which found their way into this book; to
Ashton Dorkins, editor-in-chief of tradingmarkets.com, who helped
syndicate my blog; and to Yaser Anwar for publicizing it to readers of his own very popular investment blog. I am also indebted to
editor Bill Falloon at John Wiley & Sons for suggesting this book,
and to my development editor, Emilie Herman, and production editor Christina Verigan for seeing this book through to fruition. Last
but not least, I thank Ben Xie for insisting that simplicity is the best
policy.
E.P.C.
xvii
--- page 20 ---
