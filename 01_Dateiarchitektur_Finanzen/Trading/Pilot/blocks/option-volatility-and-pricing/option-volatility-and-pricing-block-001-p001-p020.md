# Option Volatility and Pricing_ Advanced Trading Strategies -- Sheldon Natenberg -- 2nd ed, 2014 -- McGraw Hill Professional -- isbn13 9780071818773 -- 6a48d008bd9beef283debf7bad0b2e4a -- Anna’s Archive.pdf — pages 1–20

--- page 1 ---
--- page 2 ---

Option
Volatility
and
Pricing
--- page 3 ---

This page intentionally left blank
--- page 4 ---

S E C O N D E D I T I O N
Option
Volatility
and
Pricing
Sheldon Natenberg
N E W YO R K   C H I C A G O   S A N F R A N C I S C O   L I S B O N   L O N D O N   M A D R I D
M E X I C O C I T Y   M I L A N   N E W D E L H I   S A N J UA N   S E O U L
S I N G A P O R E   S Y D N E Y   T O RO N T O
Advanced Trading
Strategies and Techniques
--- page 5 ---

Copyright © 2015 by Sheldon Natenberg. All rights reserved. Except as permitted under the United States Copyright
Act of 1976, no part of this publication may be reproduced or distributed in any form or by any means, or stored in a
database or retrieval system, without the prior written permission of the publisher, with the exception that the program
listings may be entered, stored, and executed in a computer system, but they may not be reproduced for publication.
ISBN: 978-0-07-181878-0
MHID: 0-07-181878-2
The material in this eBook also appears in the print version of this title: ISBN: 978-0-07-181877-3,
MHID: 0-07-181877-4.
eBook conversion by codeMantra
Version 1.0
All trademarks are trademarks of their respective owners. Rather than put a trademark symbol after every occurrence
of a trademarked name, we use names in an editorial fashion only, and to the benefit of the trademark owner, with
no intention of infringement of the trademark. Where such designations appear in this book, they have been printed
with initial caps.
McGraw-Hill Education eBooks are available at special quantity discounts to use as premiums and sales promotions
or for use in corporate training programs. To contact a representative, please visit the Contact Us page at www.
mhprofessional.com.
TERMS OF USE
This is a copyrighted work and McGraw-Hill Education and its licensors reserve all rights in and to the work. Use
of this work is subject to these terms. Except as permitted under the Copyright Act of 1976 and the right to store
and retrieve one copy of the work, you may not decompile, disassemble, reverse engineer, reproduce, modify, create
derivative works based upon, transmit, distribute, disseminate, sell, publish or sublicense the work or any part of it
without McGraw-Hill Education’s prior consent. You may use the work for your own noncommercial and personal
use; any other use of the work is strictly prohibited. Your right to use the work may be terminated if you fail to comply
with these terms.
THE WORK IS PROVIDED “AS IS.” McGRAW-HILL EDUCATION AND ITS LICENSORS MAKE NO
GUARANTEES OR WARRANTIES AS TO THE ACCURACY, ADEQUACY OR COMPLETENESS OF OR
RESULTS TO BE OBTAINED FROM USING THE WORK, INCLUDING ANY INFORMATION THAT CAN
BE ACCESSED THROUGH THE WORK VIA HYPERLINK OR OTHERWISE, AND  EXPRESSLY DISCLAIM
ANY WARRANTY, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO IMPLIED WARRANTIES
OF MERCHANTABILITY OR FITNESS FOR A PARTICULAR PURPOSE. McGraw-Hill Education and its
licensors do not warrant or guarantee that the functions contained in the work will meet your requirements or that its
operation will be uninterrupted or error free. Neither McGraw-Hill Education nor its licensors shall be liable to you
or anyone else for any inaccuracy, error or omission, regardless of cause, in the work or for any damages resulting
therefrom. McGraw-Hill Education has no responsibility for the content of any information accessed through the
work. Under no circumstances shall McGraw-Hill Education and/or its licensors be liable for any indirect, incidental,
special, punitive, consequential or similar damages that result from the use of or inability to use the work, even if any
of them has been advised of the possibility of such damages. This limitation of liability shall apply to any claim or
cause whatsoever whether such claim or cause arises in contract, tort or otherwise.
--- page 6 ---

To Leona, for her support and encouragement throughout my career.
To Eddie, who continually makes me proud to be a father.
--- page 7 ---

This page intentionally left blank
--- page 8 ---

vii
Contents
Preface  xiii
1
Financial Contracts
1
Buying and Selling  5
Notional Value of a Forward Contract  6
Settlement Procedures  6
Market Integrity  10
2
Forward Pricing
12
Physical Commodities (Grains, Energy Products,
Precious Metals, etc.)  14
Stock  15
Bonds and Notes  17
Foreign Currencies  17
Stock and Futures Options  19
Arbitrage  19
Dividends  22
Short Sales  23
3
Contract Specifications and Option Terminology
26
Contract Specifications  26
Option Price Components  32
4
Expiration Profit and Loss
37
Parity Graphs  38
5
Theoretical Pricing Models
52
The Importance of Probability  53
A Simple Approach  57
The Black-Scholes Model  61
--- page 9 ---

viii
C O N T E N T S
6
Volatility
69
Random Walks and Normal Distributions  69
Mean and Standard Deviation  73
Forward Price as the Mean of a Distribution  76
Volatility as a Standard Deviation  77
Scaling Volatility for Time  78
Volatility and Observed Price Changes  80
A Note on Interest-Rate Products  81
Lognormal Distributions  82
Interpreting Volatility Data  85
7
Risk Measurement I
97
The Delta   100
The Gamma  105
The Theta  108
The Vega  110
The Rho  111
Interpreting the Risk Measures  112
8
Dynamic Hedging
119
Original Hedge  122
9
Risk Measurement II
135
Delta  135
Theta  141
Vega  145
Gamma  149
Lambda (Λ)  154
10	 Introduction to Spreading
158
What Is a Spread?  159
Option Spreads  165
11	 Volatility Spreads
169
Straddle  170
Strangle  171
Butterfly  173
Condor  176
Ratio Spread  179
Christmas Tree  182
Calendar Spread  182
Time Butterfly  191
Effect of Changing Interest Rates and Dividends  192
Diagonal Spreads  196
--- page 10 ---

C o n t e n t s
ix
Choosing an Appropriate Strategy  199
Adjustments  201
Submitting a Spread Order  203
12	 Bull and Bear Spreads
210
Naked Positions  210
Bull and Bear Ratio Spreads  211
Bull and Bear Butterflies and Calendar Spreads  212
Vertical Spreads  214
13	 Risk Considerations
228
Volatility Risk  229
Practical Considerations  235
How Much Margin for Error?  240
Dividends and Interest  240
What Is a Good Spread?  241
14	 Synthetics
254
Synthetic Underlying   254
Synthetic Options  256
Using Synthetics in a Spreading Strategy  260
Iron Butterflies and Iron Condors  261
15	 Option Arbitrage
265
Options on Futures  268
Locked Futures Markets  270
Options on Stock  271
Arbitrage Risk  274
16	 Early Exercise of American Options
293
Arbitrage Boundaries  294
Early Exercise of Call Options on Stock  300
Early Exercise of Put Options on Stock  303
Impact of Short Stock on Early Exercise  306
Early Exercise of Options on Futures  306
Protective Value and Early Exercise  309
Pricing of American Options  310
Early Exercise Strategies  318
Early Exercise Risk  320
17	 Hedging with Options
322
Protective Calls and Puts  323
Covered Writes  325
Collars  329
--- page 11 ---

x
C O N T E N T S
Complex Hedging Strategies  332
Hedging to Reduce Volatility  334
Portfolio Insurance  336
18	 The Black-Scholes Model
339
n(x ) and N(x )  345
A Useful Approximation  351
The Delta  353
The Theta  355
Maximum Gamma, Theta, and Vega  355
19	 Binomial Option Pricing
359
A Risk-Neutral World  359
Valuing an Option  361
The Delta  366
The Gamma  368
The Theta  368
Vega and Rho  369
The Values of u and d  369
Gamma Rent  370
American Options  371
Dividends  373
20	 Volatility Revisited
381
Historical Volatility  382
Volatility Forecasting  392
Implied Volatility as a Predictor of Future Volatility  395
Forward Volatility  405
21	 Position Analysis
411
Some Thoughts on Market Making  428
Stock Splits  439
22	 Stock Index Futures and Options
442
What Is an Index?  442
Stock Index Futures  451
Stock Index Options  459
23	 Models and the Real World
464
Markets Are Frictionless  465
Interest Rates Are Constant over the Life of an Option  467
Volatility Is Constant over the Life of the Option  469
Trading Is Continuous  472
--- page 12 ---

C o n t e n t s
xi
Expiration Straddles  477
Volatility Is Independent of the Price of the Underlying Contract  479
Underlying Prices at Expiration Are Lognormally Distributed  479
Skewness  and Kurtosis  482
24	 Volatility Skews
485
Modeling the Skew  490
Skewness and Kurtosis  496
Skewed Risk Measures  499
Shifting the Volatility  501
Skewness and Kurtosis Strategies  502
Implied Distributions  507
25	 Volatility Contracts
512
Realized Volatility Contracts  513
Implied Volatility Contracts  515
Trading the VIX  524
Replicating a Volatility Contract  535
Volatility Contract Applications  537

Afterword: A Final Thought
539
 A
Glossary of Option Terminology
540
 B
Some Useful Math
554
Rate-of-Return Calculations  554
Normal Distributions and Standard Deviation  555
Volatility  557
Index  559
--- page 13 ---

This page intentionally left blank
--- page 14 ---

P r e fa c e
xiii
Preface
It probably seems strange for an author to wait 20 years to revise a professional
publication, especially one that has been continuously in print over the entire
period. To those of you who were hoping for at least one revision in the intervening years, I can only offer my apology and the excuse that other obligations
prevented me from undertaking such a revision.
Much has changed in option markets over the last 20 years. Most markets are now fully electronic, and the days of floor trading are clearly numbered. Only in the United States do option-trading floors still exist, and even
those are inevitably giving way to electronic trading. Twenty years ago, organized option markets existed only in the major industrialized nations. But as
the importance of derivatives as both an investment vehicle and a risk-management tool has become widely recognized, new option markets have opened
in countries around the world. Options are now traded not only on traditional
products—stocks, interest rates, commodities, and foreign currencies—but also
on a bewildering array of new products—real estate, pollution, weather, inflation, and insurance. Many exchanges have also added variations on traditional
products—short-term and midcurve options, flex options, options on spreads,
and implied and realized volatility contracts.
Not only has there been a dramatic increase in the number of option markets, but the traders in those markets have become increasingly sophisticated.
When this text was first published, knowledgeable traders could only be found
at firms that traded derivatives professionally—market-making firms, hedge
funds, investment banks, and other proprietary trading firms. Now, many retail
customers have a level of knowledge equal to that of a professional trader.
At the same time, universities are adding or expanding programs in financial
engineering. In many cases, those who choose a career in derivatives trading
have already had in-depth exposure to the mathematics of option pricing.
While much has changed in the last 20 years, much has also remained
the same. There is still a core body of material that a serious option trader
needs to master, and this core material is much the same as it has always been.
The previous edition of this text was an attempt to present this material in a
manner that was easily accessible and that did not require a familiarity with
advanced mathematics. This edition retains that approach. Although some
presentations may have been changed in the interest of improving an explanation or clarifying a concept, all the major topics from the previous edition
have been retained.
--- page 15 ---

So what’s new in this edition? As in the first edition, an attempt has been
made to explain important concepts in the simplest possible manner using an
intuitive rather than mathematical approach. However, it is also true that a full
understanding of many option concepts requires a familiarity with more advanced mathematics. Consequently, some explanations have been expanded
to include a discussion of the relevant mathematics. But even these discussions
tend to avoid mathematical concepts with which many readers are unlikely to
be familiar. Many chapters have also been expanded to include a more detailed
discussion of the relevant topics. In addition, there are several completely new
chapters covering forward pricing, risk dynamics, the Black-Scholes model,
binomial option pricing, and volatility contracts.
As with any living language, market terminology, and more specifically, option terminology, has changed over time. Some terms that were common when
the first edition appeared have gone out of favor or disappeared completely.
Other terms that did not previously exist have gained wide acceptance. This is
reflected in small changes to the vocabulary used in this text.
It is almost impossible to keep up with the amount of information that is
available on options. Not only do new books appear with greater frequency, but
the Internet has enabled traders to find relevant source material almost instantaneously. For this reason, the Bibliography has been eliminated. This should
not be construed as an attempt to discourage readers from consulting other
sources. This book represents only one approach to options—that of a professional trader. Many excellent option books are available, and any aspiring
option trader will want to consult a broad range of texts in order to understand
the many different ways one can approach option markets. For those who are
interested in the mathematics of option pricing, this text is in no way meant to
take the place of a good university textbook on financial engineering.
Nothing in this text is really new, and all the concepts will be familiar, in
one form or another, to most experienced option traders. The presentation
represents my best attempt, as an option educator, to present these concepts in
a clear and easily accessible manner. The material is based not only on what
I have personally learned throughout my career but also on the knowledge and
experiences of many others with whom I have been privileged to work. In particular, my colleagues Tim Weithers and Samuel Kadziela offered many helpful comments and insights and in some cases rescued me from embarrassing
errors. Any remaining errors, of which there are almost certainly a few, are
strictly my own.
I make no claim to having found a magic secret to successful option trading. Anyone seeking such a formula will have to look elsewhere. The secret, if
there is one, is in learning as much as possible, applying in the real world what
has been learned, and analyzing both one’s successes and one’s failures.
Sheldon Natenberg
	 xiv
P R E FA C E
--- page 16 ---

Option
Volatility
and
Pricing
--- page 17 ---

This page intentionally left blank
--- page 18 ---

1
Financial Contracts
My friend Jerry lives in a small town, the same town in which he was born and
raised. Because Jerry’s parents are no longer alive and many of his friends have
left, he is seriously thinking of packing up and moving to a larger city. However,
Jerry recently heard that there is a plan to build a major highway that will pass
very close to his hometown. Because the highway is likely to bring new life to
the town, Jerry is reconsidering his decision to move away. It has also occurred
to Jerry that the highway may bring new business opportunities.
For many years, Jerry’s family was in the restaurant business, and Jerry
is thinking of building a restaurant at the main intersection leading from the
highway into town. If Jerry does decide to build the restaurant, he will need to
acquire land along the highway. Fortunately, Jerry has located a plot of land,
currently owned by Farmer Smith, that is ideally suited for the restaurant. Because
the land does not seem to be in use, Jerry is hoping that Farmer Smith might
be willing to sell it.
If Farmer Smith is indeed willing to sell, how can Jerry acquire the land
on which to build his restaurant? First, Jerry must find out how much Farmer
Smith wants for the land. Let’s say $100,000. If Jerry thinks that the price is
reasonable, he can agree to pay this amount and, in return, take ownership of
the land. In this case, Jerry and Farmer Smith will have entered into a spot or
cash transaction.
In a cash transaction, both parties agree on terms, followed immediately
by an exchange of money for goods. The trading of stock on an exchange is
usually considered to be a cash transaction: the buyer and seller agree on the
price, the buyer pays the seller, and the seller delivers the stock. The actions
essentially take place simultaneously. (Admittedly, on most stock exchanges,
there is a settlement period between the time the price is agreed on and the
time the stock is actually delivered and payment is made. However, the settlement period is relatively short, so for practical purposes most traders consider
this a cash transaction.)
However, it has also occurred to Jerry that it will probably take several
years to build the highway. Because Jerry wants the opening of his restaurant
1
--- page 19 ---

2
O P T I O N V O L AT I L I T Y A N D P R I C I N G
to coincide with the opening of the highway, he doesn’t need to begin construction on the restaurant for at least another year. There is no point in taking possession of the land right now—it will just sit unused for a year. Given
his construction schedule, Jerry has decided to approach Farmer Smith with
a slightly different proposition. Jerry will agree to Farmer Smith’s price of
$100,000, but he will propose to Farmer Smith that they complete the transaction in one year, at which time Farmer Smith will receive payment, and Jerry
will take possession of the land. If both parties agree to this, Jerry and Farmer
Smith will have entered into a forward contract. In a forward contract, the parties
agree on the terms now, but the actual exchange of money for goods does not
take place until some later date, the maturity or expiration date.
If Jerry and Farmer Smith enter into a forward contract, it’s unlikely that
the price Farmer Smith will want for his land in one year will be the same price
that he is asking today. Because both the payment and the transfer of goods are
deferred, there may be advantages or disadvantages to one party or the other.
Farmer Smith may point out that if he receives full payment of $100,000 right
now, he can deposit the money in his bank and begin to earn interest. In a forward contract, however,  he will have to forego any interest earnings. As a result,
Farmer Smith may insist that he and Jerry negotiate a one-year forward price that
takes into consideration this loss of interest.
Forward contracts are common when a potential buyer requires goods in
the future or when a potential seller knows that a supply of goods will be ready
for sale in the future. A bakery may need a periodic supply of grain to support
operations. Some grain may be required now, but the bakery also knows that
additional grain will be required at regular intervals in the future. In order to
eliminate the risk of rising grain prices, the bakery can buy grain in the forward
market—agreeing on a price now but not taking delivery or making payment
until some later date. In the same way, a farmer who knows that he will have
grain ready for harvest at a later date can sell his crop in the forward market to
insure against falling prices.
When a forward contract is traded on an organized exchange, it is usually
referred to as a futures contract. On a futures exchange, the contract specifications
for a forward contract are standardized to more easily facilitate trading. The
exchange specifies the quantity and quality of goods to be delivered, the date
and place of delivery, and the method of payment. Additionally, the exchange
guarantees the integrity of the contract. Should either the buyer or the seller
default, the exchange assumes the responsibility of fulfilling the terms of the
forward contract.
The earliest futures exchanges enabled producers and users of physical
commodities—grains, precious metals, and energy products—to protect themselves against price fluctuations. More recently, many exchanges have introduced futures contracts on financial instruments—stocks and stock indexes,
interest-rate contracts, and foreign currencies. Although there is still significant
trading in physical commodities, the total value of exchange-traded financial
instruments now greatly exceeds the value of physical commodities.
Returning to Jerry, he finds that he has a new problem. The government
has indicated its desire to build the highway, but the necessary funds have not
--- page 20 ---

F i n a n c i a l C o n t r a c t s
3
yet been authorized. With many other public works projects competing for a
limited amount of money, it’s possible that the entire highway project could be
canceled. If this happens, Jerry intends to return to his original plan and move
away. In order to make an informed decision, Jerry needs time to see what the
government will do. If the highway is actually built, Jerry wants to purchase
Farmer Smith’s land. If the highway isn’t built, Jerry wants to be able to walk
away without any obligation.
Jerry believes that he will know for certain within a year whether the highway project will be approved. As a result, Jerry approaches Farmer Smith with
a new proposition. Jerry and Farmer Smith will negotiate a one-year forward
price for the land, but Jerry will have one year to decide whether to go ahead
with the purchase. One year from now, Jerry can either buy the land at the
agreed-on forward price, or he can walk away with no obligation or penalty.
There is much that can happen over one year, and without some inducement Farmer Smith is unlikely to agree to this proposal. Someone may make
a better offer for the land, but Farmer Smith will be unable to accept the offer
because he must hold the land in the event that Jerry decides to buy. For the
next year, Farmer Smith will be a hostage to Jerry’s final decision.
Jerry understands Farmer Smith’s dilemma, so he offers to negotiate a
separate payment to compensate Farmer Smith for this uncertainty. In effect,
Jerry is offering to buy the right to decide at a later date whether to purchase
the land. Regardless of Jerry’s final decision, Farmer Smith will get to keep
this separate payment. If Jerry and Farmer Smith can agree on this separate
payment, as well as the forward price, they will enter into an option contract. An
option contract gives one party the right to make a decision at a later date. In
this example, Jerry is the buyer of a call option, giving him the right to decide
at a later date whether to buy. Farmer Smith is the seller of the call option.
Deciding whether to buy the land for his restaurant is not Jerry’s only problem. He owns a house that he inherited from his parents and that he was planning to sell prior to moving away. Before hearing about the highway project,
Jerry had put up a “For Sale” sign in front of the house, and a young couple,
seeing the sign, showed enough interest in the house to make an offer. Jerry was
seriously considering accepting the offer, but then the highway project came
up. Now Jerry doesn’t know what to do. If the government goes ahead with the
highway and Jerry goes ahead with his restaurant, he wants to keep his house.
If not, he wants to sell the house. Given the situation, Jerry might make a proposal to the couple similar to that which he made to Farmer Smith. Jerry and
the couple will agree on a price for the house, but Jerry will have one year in
which to decide whether to actually sell the house.
Like Farmer Smith, the couple’s initial reaction is likely to be negative.
If they agree to Jerry’s proposal, they will have to make temporary housing
arrangements for the next year. If they find another house they like better, they
won’t be able to buy it because they might eventually be required to purchase
Jerry’s house. They will spend the next year in housing limbo, a hostage to Jerry’s
final decision.
As with Farmer Smith, Jerry understands the couple’s dilemma and offers
to compensate them for their inconvenience by paying an agreed-on amount.
