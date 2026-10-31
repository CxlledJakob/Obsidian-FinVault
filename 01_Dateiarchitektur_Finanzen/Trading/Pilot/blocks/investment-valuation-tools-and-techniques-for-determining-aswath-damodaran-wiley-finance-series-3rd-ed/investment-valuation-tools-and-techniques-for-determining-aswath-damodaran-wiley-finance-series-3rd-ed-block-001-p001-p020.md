# INVESTMENT VALUATION TOOLS AND TECHNIQUES FOR DETERMINING -- Aswath Damodaran -- Wiley finance series, 3rd ed_, Hoboken, N_J, New Jersey, -- John -- isbn13 9781118011522 -- f84d1622bdc2de526da0dda803c52830 -- Anna’s.pdf — pages 1–20

--- page 1 ---
--- page 2 ---

Investment
Valuation
--- page 3 ---

Founded in 1807, John Wiley & Sons is the oldest independent publishing company in the
United States. With ofﬁces in North America, Europe, Australia, and Asia, Wiley is globally committed to developing and marketing print and electronic products and services for
our customers’ professional and personal knowledge and understanding.
The Wiley Finance series contains books written speciﬁcally for ﬁnance and investment
professionals as well as sophisticated individual investors and their ﬁnancial advisors.
Book topics range from portfolio management to e-commerce, risk management, ﬁnancial
engineering, valuation, and ﬁnancial instrument analysis, as well as much more.
For a list of available titles, please visit our Web site at www.WileyFinance.com.
--- page 4 ---

Investment
Valuation
Tools and Techniques for
Determining the Value of Any Asset
Third Edition
ASWATH DAMODARAN
www.damodaran.com
WILEY
John Wiley & Sons, Inc.
--- page 5 ---

Copyright © 2012 by Aswath Damodaran. All rights reserved.
Published by John Wiley & Sons, Inc., Hoboken, New Jersey.
Published simultaneously in Canada.
No part of this publication may be reproduced, stored in a retrieval system, or transmitted in any form
or by any means, electronic, mechanical, photocopying, recording, scanning, or otherwise, except as
permitted under Section 107 or 108 of the 1976 United States Copyright Act, without either the prior
written permission of the Publisher, or authorization through payment of the appropriate per-copy fee
to the Copyright Clearance Center, Inc., 222 Rosewood Drive, Danvers, MA 01923, (978) 750-8400,
fax (978) 646-8600, or on the Web at www.copyright.com. Requests to the Publisher for permission
should be addressed to the Permissions Department, John Wiley & Sons, Inc., 111 River Street, Hoboken,
NJ 07030, (201) 748-6011, fax (201) 748-6008, or online at http://www.wiley.com/go/permissions.
Limit of Liability/Disclaimer of Warranty: While the publisher and author have used their best efforts
in preparing this book, they make no representations or warranties with respect to the accuracy or
completeness of the contents of this book and speciﬁcally disclaim any implied warranties of
merchantability or ﬁtness for a particular purpose. No warranty may be created or extended by sales
representatives or written sales materials. The advice and strategies contained herein may not be
suitable for your situation. You should consult with a professional where appropriate. Neither the
publisher nor author shall be liable for any loss of proﬁt or any other commercial damages, including
but not limited to special, incidental, consequential, or other damages.
For general information on our other products and services or for technical support, please contact our
Customer Care Department within the United States at (800) 762-2974, outside the United States at
(317) 572-3993 or fax (317) 572-4002.
Wiley also publishes its books in a variety of electronic formats. Some content that appears in print
may not be available in electronic books. For more information about Wiley products, visit our web
site at www.wiley.com.
Library of Congress Cataloging-in-Publication Data:
Damodaran, Aswath.
Investment valuation : tools and techniques for determining the value of any asset / Aswath
Damodaran.—3rd ed.
p. cm.—(Wiley ﬁnance series)
Includes bibliographical references and index.
ISBN 978-1-118-01152-2 (cloth); ISBN 978-1-118-20654-6 (ebk);
ISBN 978-1-118-20655-3 (ebk); ISBN 978-1-118-20656-0 (ebk)
ISBN 978-1-118-13073-5 (paper); ISBN 978-1-118-20657-7 (ebk);
ISBN 978-1-118-20658-4 (ebk); ISBN 978-1-118-20659-1 (ebk)
1. Corporations—Valuation—Mathematical models.
I. Title.
HG4028.V3 D353
2012
658.15—dc23
2011052858
10   9   8   7   6   5   4   3   2   1
--- page 6 ---

I would like to dedicate this book to Michele, whose patience
and support made it possible, and to my four children—
Ryan, Brendan, Kendra, and Kiran—who provided the inspiration.
--- page 7 ---
--- page 8 ---

Preface to the Third Edition
T
his is a book about valuation—the valuation of stocks, bonds, options, futures
and real assets. It is a fundamental precept of this book that any asset can be valued, albeit imprecisely in some cases. I have attempted to provide a sense of not
only the differences between the models used to value different types of assets, but
also the common elements in these models.
The past decade has been an eventful one for those interested in valuation for
several reasons. First, the growth of Asian and Latin American markets brought
emerging market companies into the forefront, and you will see the increased focus
on these companies in this edition. Second, we saw the havoc wreaked by macroeconomic factors on company valuations during the bank crisis of 2008, and a blurring of the lines between developed and emerging markets. The lessons I learned
about ﬁnancial fundamentals during the crisis about risk-free rates, risk premiums
and cash ﬂow estimation are incorporated into the text. Third, the past year has seen
the inﬂux of social media companies, with small revenues and outsized market capitalizations, in an eerie replay of the dot-com boom from the late 1990s. More than
ever, it made clear that the more things change, the more they stay the same. Finally,
the entry of new players into equity markets (hedge funds, private equity investors
and high-frequency traders) has changed markets and investing dramatically. With
each shift, the perennial question arises: “Is valuation still relevant in this market?”
and my answer remains unchanged, “Absolutely and more than ever.”
As technology increasingly makes the printed page an anachronism, I have tried
to adapt in many ways. First, this book will be available in e-book format, and
hopefully will be just as useful as the print edition (if not more so). Second, every
valuation in this book will be put on the web site that will accompany this book
(www.damodaran.com), as will a signiﬁcant number of datasets and spreadsheets.
In fact, the valuations in the book will be updated online, allowing the book to have
a much closer link to real-time valuations.
In the process of presenting and discussing the various aspects of valuation, I
have tried to adhere to four basic principles. First, I have attempted to be as comprehensive as possible in covering the range of valuation models that are available
to an analyst doing a valuation, while presenting the common elements in these
models and providing a framework that can be used to pick the right model for any
valuation scenario. Second, the models are presented with real-world examples,
warts and all, so as to capture some of the problems inherent in applying these
models. There is the obvious danger that some of these valuations will appear to be
hopelessly wrong in hindsight, but this cost is well worth the beneﬁts. Third, in
keeping with my belief that valuation models are universal and not market-speciﬁc,
illustrations from markets outside the United States are interspersed throughout the
book. Finally, I have tried to make the book as modular as possible, enabling a
reader to pick and choose sections of the book to read, without a signiﬁcant loss of
continuity.
vii
--- page 9 ---
--- page 10 ---

Contents
CHAPTER 1
Introduction to Valuation
1
A Philosophical Basis for Valuation
1
Generalities about Valuation
2
The Role of Valuation
6
Conclusion
9
Questions and Short Problems
9
CHAPTER 2
Approaches to Valuation
11
Discounted Cash Flow Valuation
11
Relative Valuation
19
Contingent Claim Valuation
23
Conclusion
25
Questions and Short Problems
25
CHAPTER 3
Understanding Financial Statements
27
The Basic Accounting Statements
27
Asset Measurement and Valuation
29
Measuring Financing Mix
36
Measuring Earnings and Proﬁtability
42
Measuring Risk
47
Other Issues in Analyzing Financial Statements
53
Conclusion
55
Questions and Short Problems
55
CHAPTER 4
The Basics of Risk
58
What is Risk?
58
Equity Risk and Expected Return
59
Alternative Models for Equity Risk
71
A Comparative Analysis of Equity Risk Models
76
Models of Default Risk
77
Conclusion
81
Questions and Short Problems
82
CHAPTER 5
Option Pricing Theory and Models
87
Basics of Option Pricing
87
Determinants of Option Value
89
ix
--- page 11 ---

Option Pricing Models
90
Extensions of Option Pricing
107
Conclusion
109
Questions and Short Problems
109
CHAPTER 6
Market Efﬁciency—Deﬁnition, Tests, and Evidence
111
Market Efﬁciency and Investment Valuation
111
What Is an Efﬁcient Market?
112
Implications of Market Efﬁciency
112
Necessary Conditions for Market Efﬁciency
114
Propositions about Market Efﬁciency
114
Testing Market Efﬁciency
116
Cardinal Sins in Testing Market Efﬁciency
120
Some Lesser Sins That Can Be a Problem
121
Evidence on Market Efﬁciency
122
Time Series Properties of Price Changes
122
Market Reaction to Information Events
130
Market Anomalies
134
Evidence on Insiders and Investment Professionals
142
Conclusion
149
Questions and Short Problems
150
CHAPTER 7
Riskless Rates and Risk Premiums
154
The Risk-Free Rate
154
Equity Risk Premium
159
Default Spreads on Bonds
177
Conclusion
180
Questions and Short Problems
180
CHAPTER 8
Estimating Risk Parameters and Costs of Financing
182
The Cost of Equity and Capital
182
Cost of Equity
183
From Cost of Equity to Cost of Capital
210
Best Practices at Firms
221
Conclusion
222
Questions and Short Problems
223
CHAPTER 9
Measuring Earnings
229
Accounting versus Financial Balance Sheets
229
Adjusting Earnings
230
Conclusion
247
Questions and Short Problems
249
x
CONTENTS
--- page 12 ---

CHAPTER 10
From Earnings to Cash Flows
250
The Tax Effect
250
Reinvestment Needs
258
Conclusion
268
Questions and Short Problems
269
CHAPTER 11
Estimating Growth
271
The Importance of Growth
272
Historical Growth
272
Analyst Estimates of Growth
282
Fundamental Determinants of Growth
285
Qualitative Aspects of Growth
301
Conclusion
302
Questions and Short Problems
302
CHAPTER 12
Closure in Valuation: Estimating Terminal Value
304
Closure in Valuation
304
The Survival Issue
318
Closing Thoughts on Terminal Value
320
Conclusion
321
Questions and Short Problems
321
CHAPTER 13
Dividend Discount Models
323
The General Model
323
Versions of the Model
324
Issues in Using the Dividend Discount Model
344
Tests of the Dividend Discount Model
345
Conclusion
348
Questions and Short Problems
349
CHAPTER 14
Free Cash Flow to Equity Discount Models
351
Measuring What Firms Can Return to Their Stockholders
351
FCFE Valuation Models
357
FCFE Valuation versus Dividend Discount Model Valuation
372
Conclusion
376
Questions and Short Problems
376
CHAPTER 15
Firm Valuation: Cost of Capital and Adjusted Present Value Approaches
380
Free Cash ﬂow to the Firm
380
Firm Valuation: The Cost of Capital Approach
383
Contents
xi
--- page 13 ---

Firm Valuation: The Adjusted Present Value Approach
398
Effect of Leverage on Firm Value
402
Adjusted Present Value and Financial Leverage
415
Conclusion
419
Questions and Short Problems
419
CHAPTER 16
Estimating Equity Value per Share
423
Value of Nonoperating Assets
423
Firm Value and Equity Value
440
Management and Employee Options
442
Value per Share When Voting Rights Vary
448
Conclusion
450
Questions and Short Problems
451
CHAPTER 17
Fundamental Principles of Relative Valuation
453
Use of Relative Valuation
453
Standardized Values and Multiples
454
Four Basic Steps to Using Multiples
456
Reconciling Relative and Discounted Cash Flow Valuations
466
Conclusion
467
Questions and Short Problems
467
CHAPTER 18
Earnings Multiples
468
Price-Earnings Ratio
468
The PEG Ratio
487
Other Variants on the PE Ratio
497
Enterprise Value to EBITDA Multiple
500
Conclusion
508
Questions and Short Problems
508
CHAPTER 19
Book Value Multiples
511
Price-to-Book Equity
511
Applications of Price–Book Value Ratios
521
Use in Investment Strategies
530
Value-to-Book Ratios
532
Tobin’s Q: Market Value/Replacement Cost
537
Conclusion
539
Questions and Short Problems
539
CHAPTER 20
Revenue Multiples and Sector-Speciﬁc Multiples
542
Revenue Multiples
542
Sector-Speciﬁc Multiples
571
xii
CONTENTS
--- page 14 ---

Conclusion
577
Questions and Short Problems
577
CHAPTER 21
Valuing Financial Service Firms
581
Categories of Financial Service Firms
581
What is Unique about Financial Service Firms?
582
General Framework for Valuation
583
Discounted Cash Flow Valuation
584
Asset-Based Valuation
599
Relative Valuation
599
Issues in Valuing Financial Service Firms
605
Conclusion
607
Questions and Short Problems
608
CHAPTER 22
Valuing Firms with Negative or Abnormal Earnings
611
Negative Earnings: Consequences and Causes
611
Valuing Negative Earnings Firms
615
Conclusion
639
Questions and Short Problems
639
CHAPTER 23
Valuing Young or Start-Up Firms
643
Information Constraints
643
New Paradigms or Old Principles:
A Life Cycle Perspective
644
Venture Capital Valuation
646
General Framework for Analysis
648
Value Drivers
659
Estimation Noise
661
Implications for Investors
662
Implications for Managers
663
The Expectations Game
663
Conclusion
665
Questions and Short Problems
666
CHAPTER 24
Valuing Private Firms
667
What Makes Private Firms Different?
667
Estimating Valuation Inputs at Private Firms
668
Valuation Motives and Value Estimates
688
Valuing Venture Capital and Private Equity Stakes
693
Relative Valuation of Private Businesses
695
Conclusion
699
Questions and Short Problems
699
Contents
xiii
--- page 15 ---

CHAPTER 25
Aquisitions and Takeovers
702
Background on Acquisitions
702
Empirical Evidence on the Value Effects of Takeovers
705
Steps in an Acquisition
705
Takeover Valuation: Biases and Common Errors
724
Structuring the Acquisition
725
Analyzing Management and Leveraged Buyouts
730
Conclusion
734
Questions and Short Problems
735
CHAPTER 26
Valuing Real Estate
739
Real versus Financial Assets
739
Discounted Cash Flow Valuation
740
Comparable/Relative Valuation
759
Valuing Real Estate Businesses
761
Conclusion
763
Questions and Short Problems
763
CHAPTER 27
Valuing Other Assets
766
Cash-Flow-Producing Assets
766
Non-Cash-Flow-Producing Assets
775
Assets with Option Characteristics
777
Conclusion
778
Questions and Short Problems
779
CHAPTER 28
The Option to Delay and Valuation Implications
781
The Option to Delay a Project
781
Valuing a Patent
789
Natural Resource Options
796
Other Applications
802
Conclusion
802
Questions and Short Problems
803
CHAPTER 29
The Options to Expand and to Abandon: Valuation Implications
805
The Option to Expand
805
When Are Expansion Options Valuable?
812
Valuing a Firm with the Option to Expand
815
Value of Financial Flexibility
817
The Option to Abandon
820
Reconciling Net Present Value and Real Option Valuations
823
Conclusion
823
Questions and Short Problems
824
xiv
CONTENTS
--- page 16 ---

CHAPTER 30
Valuing Equity in Distressed Firms
826
Equity in Highly Levered Distressed Firms
826
Implications of Viewing Equity as an Option
828
Estimating the Value of Equity as an Option
831
Consequences for Decision Making
836
Conclusion
839
Questions and Short Problems
839
CHAPTER 31
Value Enhancement: A Discounted Cash Flow Valuation Framework
841
Value-Creating and Value-Neutral Actions
841
Ways of Increasing Value
842
Value Enhancement Chain
859
Closing Thoughts on Value Enhancement
864
Conclusion
865
Questions and Short Problems
865
CHAPTER 32
Value Enhancement: Economic Value Added, Cash Flow Return on Investment,
and Other Tools
869
Economic Value Added
870
Cash Flow Return on Investment
884
A Postscript on Value Enhancement
890
Conclusion
891
Questions and Short Problems
891
CHAPTER 33
Probabilistic Approaches in Valuation: Scenario Analysis, Decision Trees,
and Simulations
894
Scenario Analysis
894
Decision Trees
899
Simulations
908
An Overall Assessment of Probabilistic Risk-Assessment Approaches
919
Conclusion
921
Questions and Short Problems
921
CHAPTER 34
Overview and Conclusion
925
Choices in Valuation Models
925
Which Approach Should You Use?
926
Choosing the Right Discounted Cash Flow Model
929
Choosing the Right Relative Valuation Model
933
When Should You Use the Option Pricing Models?
937
Conclusion
938
References
939
Index
954
Contents
xv
--- page 17 ---
--- page 18 ---

Investment
Valuation
--- page 19 ---
--- page 20 ---

CHAPTER 1
Introduction to Valuation
E
very asset, ﬁnancial as well as real, has a value. The key to successfully investing
in and managing these assets lies in understanding not only what the value is, but
the sources of the value. Every asset can be valued, but some assets are easier to
value than others, and the details of valuation will vary from case to case. Thus,
valuing of a real estate property will require different information and follow a different format than valuing a publicly traded stock. What is surprising, however, is
not the differences in techniques across assets, but the degree of similarity in the
basic principles of valuation. There is uncertainty associated with valuation. Often
that uncertainty comes from the asset being valued, though the valuation model
may add to that uncertainty.
This chapter lays out a philosophical basis for valuation, together with a discussion of how valuation is or can be used in a variety of frameworks, from portfolio
management to corporate ﬁnance.
A PHILOSOPHICAL BASIS FOR VALUATION
It was Oscar Wilde who described a cynic as one who “knows the price of everything, but the value of nothing.” He could very well have been describing some analysts and many investors, a surprising number of whom subscribe to the “bigger
fool” theory of investing, which argues that the value of an asset is irrelevant as long
as there is a “bigger fool” around willing to buy the asset from them. While this may
provide a basis for some proﬁts, it is a dangerous game to play, since there is no guarantee that such an investor will still be around when the time to sell comes.
A postulate of sound investing is that an investor does not pay more for an asset
than it’s worth. This statement may seem logical and obvious, but it is forgotten and
rediscovered at some time in every generation and in every market. There are those
who are disingenuous enough to argue that value is in the eye of the beholder, and
that any price can be justiﬁed if there are other investors willing to pay that price.
That is patently absurd. Perceptions may be all that matter when the asset is a
painting or a sculpture, but investors do not (and should not) buy most assets for
aesthetic or emotional reasons; ﬁnancial assets are acquired for the cash ﬂows expected on them. Consequently, perceptions of value have to be backed up by reality,
which implies that the price that is paid for any asset should reﬂect the cash ﬂows it
is expected to generate. The models of valuation described in this book attempt to
relate value to the level and expected growth of these cash ﬂows.
There are many areas in valuation where there is room for disagreement, including
how to estimate true value and how long it will take for prices to adjust to true value.
1
