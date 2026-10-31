# Zero to Hero in Cryptocurrency Trading.pdf — pages 1–20

--- page 1 ---
--- page 2 ---

Zero to Hero in Cryptocurrency Trading
Copyright © 2023 Packt Publishing
All rights reserved. No part of this book may be reproduced, stored in a retrieval system, or transmitted in any form
or by any means, without the prior written permission of the publisher, except in the case of brief quotations embedded
in critical articles or reviews.
Every effort has been made in the preparation of this book to ensure the accuracy of the information presented.
However, the information contained in this book is sold without warranty, either express or implied. Neither the author
nor Packt Publishing or its dealers and distributors will be held liable for any damages caused or alleged to have been
caused directly or indirectly by this book.
Packt Publishing has endeavored to provide trademark information about all of the companies and products mentioned
in this book by the appropriate use of capital. However, Packt Publishing cannot guarantee the accuracy of this
information.
Group Product Manager: Kaustubh Manglurkar
Publishing Product Manager: Apeksha Shetty
Senior Editor: Tazeen Shaikh
Technical Editor: Kavyashree K S
Copy Editor: Safis Editing
Project Coordinator: Farheen Fathima
Proofreader: Safis Editing
Indexer: Manju Arasan
Production Designer: Shankar Kalbhor
Marketing Coordinator: Nivedita Singh
First published: September 2023
Production reference: 1150923
Published by Packt Publishing Ltd.
Grosvenor House
11 St. Paul ’s Square
--- page 3 ---

Birmingham
B3 1RB, UK.
ISBN 978-1-83763-128-5
www.packtpub.com
Contributors
About the author
Bogdan Vaida is a seasoned private investor who has backed over 300 crypto start-ups. He is a founding member of
Iron Capital, a VC company incorporated in Dubai. Eight years ago, he founded his own company and has managed
teams at various stages of development. He is an advisor for several blockchain projects, including Gravvity,
Blockchain Valley Virtual, Gentlemen Capital, Bountie, MetaVill, and Umay. For fun and profit, he trades daily, having
his own trading course and programming his own trading indicators and strategies.
About the reviewer
Ratanlal Mahanta is currently working as a quant trader for a quant firm. He has several years of experience in the
modeling and simulation of quantitative trading. Ratanlal holds a master’s degree in science in computational finance,
and his research areas include quant trading, optimal execution, and high-frequency trading. He has over 10 years of
experience in the finance industry and is gifted at solving difficult problems that lie at the intersection of markets,
technology, research, and design.
--- page 4 ---

Table of Contents
Preface
1
Introduction to Cryptocurrency Trading
Disclaimer
My journey into trading
Overview of the book’s structure
Market myths
I will find a successful strategy on YouTube
I will make money paying for trading signals
I will run a successful trading bot
I will successfully invest in copy-trading platforms
And why do these strategies, signals, and bots fail?
Summary
Exercises
Answers to the exercises
2
Understanding the Basics
A trader ’s psychology
Risk assessment questionnaire
Cryptocurrencies as an asset class
A candlestick story
Timeframes
Market participants
Types of markets
Summary
Exercises
--- page 5 ---

3
Technical Analysis – Candles and Patterns
TradingView
Activities
Market patterns
I. The story of the pattern is more important than the pattern
II. The story changes as the pattern develops
III. Every pattern instance has a random outcome
IV. Seek confluence, not certainty
V. There’s always a pattern you haven’t noticed
Candlestick patterns
Hammer (bullish) versus Shooting Star (bearish)
Inverted Hammer (bullish) versus Hanging Man (bearish)
Doji (neutral)
Spinning Top (neutral)
Dragonfly Doji (bullish) versus Gravestone Doji (bearish)
Morning (Doji) Star (bullish) versus Evening (Doji) Star (bearish)
Bullish Engulfing versus Bearish Engulfing
Bullish Harami versus Bearish Harami
Three W hite Soldiers (bullish) versus Three Black Crows (bearish)
Marubozu (bullish or bearish)
Candlestick patterns questions
Activities
Chart patterns
Double Bottom (bullish) versus Double Top (bearish)
Inverse Head and Shoulders (bullish) versus Head and Shoulders (bearish)
Bull Flag (bullish) versus Bear Flag (bearish)
Cup and Handle (bullish) versus Inverted Cup and Handle (bearish)
Descending, ascending, symmetrical, and expanding triangles
Falling W edge (bullish) versus Rising W edge (bearish)
Ascending, Descending, and Horizontal (Parallel) Channels (or
Rectangles)
--- page 6 ---

Buildup, Breakout, and Breakdown
The Retest and the Fakeout (trend confirmation)
Differences between candlestick patterns and chart patterns
Chart pattern questions
Activities
Supply and demand
The law of demand
The law of supply
The market-clearing price
Activities
Support and resistance
Let’s speak in pictures
A game of randomness
Summary
4
Technical Analysis – Technical Indicators
Technical indicator categories
Trend indicators - moving averages
Repainting
Fees
Activities
Momentum indicators - relative strength index
RSI formula
Activities
Volatility - average true range
ATR formula
Activities
Volume - market volume
Activities
Trend analysis - divergences
Activities
--- page 7 ---

Summary
5
The Centralized Exchange
W hat is the CEX?
Depositing money
Trading sections
Long versus short
Activities
Types of orders
Market orders
Limit orders
Stop limit orders
Stop market orders (only available in the futures markets)
OCO orders (spot and margin markets only)
Trailing stop orders
Other types of orders
Spot versus futures
Activities
Leverage and liquidation
Activities
The order book, market depth, commissions, spreads, and slippage
The market depth or depth of the market
Liquidity
The bid-ask spread
Slippage
Market makers
A metaphor for it all – 3Commas
Connecting to an exchange
SmartTrade
Paper trading/demo account
Your first (demo) trade
--- page 8 ---

Activities
Summary
6
Money Management
Limiting losses
Limiting losses strategically
Limiting losses in the trading account
Limiting losses in trading
Activities
Position sizing
Method 1 – percent of equity (variation)
Method 2 – fixed fractional position sizing (also known as fixed risk
position sizing)
Activities
Keeping a trading journal
Adjusting to the market
Handling emotions
Planning your trades
Your trading plan
Dollars or Bitcoin?
Summary
7
Finding Your Edge
Trading system essentials
Filters
The setup
The entry trigger
The stop loss
The take profit
--- page 9 ---

Optional
The review
Identifying a trading pattern
YouTube/Twitter/Telegram/Discord/TradingView and other social channels
TradingView’s indicators and strategies
Learning PineScript or Python and get hired as a coder
Developing your own
Defining entry and exit points
Entries
Exits
The SHIELD mentality
Backtesting
Activities
Forward testing
Paper trading (the dry-run)
Live action
Testing checklist
Summary
8
Automated Trading
Technical requirements
Coding trading strategies – from Pine Script to Python and beyond
Coding an indicator in TradingView
Editing existing indicators
Making your own indicator
Converting an indicator into a strategy
Caveats when coding Pine Script strategies
Linking the strategy to a 3Commas bot
Coding a strategy in Freqtrade
Freqtrade intro
Directions for installation and configuration
--- page 10 ---

Creating your own strategy
Trading ideas
Summary
Further reading
9
What’s Next?
10
BONUS – One Month of Trading
Preparing the tools
June 7, 2023
June 8, 2023
Trading
June 8 – BTC analysis
June, 10 – Trade 1 BTC/BUSD
Adding other coins to watch
June, 10 – Trade 2 ETH/BUSD
Using ATR bands
June, 10 – Trade 3 DATA/BUSD
June, 10 – Trade 4 GRT/BUSD
June, 12 – Trade 5 POLS/BUSD
June, 14 – Trade 6 XVS/BUSD
June, 14 – Trade 7 VIDT/BUSD
June, 14 and 16 – Trade 8 and 9 TOMO/BUSD
June, 16 – Trade 10 CELR/BUSD
June, 16 – Trade 11 ANT/BUSD
Using vFMSS
June, 16 – Trade 12 BAKE/BUSD (vFMSS)
June, 16 – Trade 13 VIDT/BUSD (vFMSS)
June, 17 – Trade 14 THETA/BUSD (vFMSS)
--- page 11 ---

June, 17 – Trade 15 STG/BUSD (vFMSS)
June, 18 – Trade 16 GLMR/BUSD (the Crypto Pairs Screener)
Using SLs
June, 18 – Trade 17 ACH/BUSD (vFMSS)
June, 18 – Trade 18 KAVA/BUSD (vFMSS)
June, 18 – Trade 19 HOOK/BUSD (vFMSS)
June, 18 – Trade 20 GFT/BUSD (vFMSS)
June, 22 – Trade 21 KEY/BUSD (the Crypto Pairs Screener)
June, 23 – Trade 22 AGLD/BUSD
June, 22 – Trade 23 GLM/BUSD
June, 24 – Trade 24 OMG/BUSD (the Crypto Pairs Screener)
June, 25 – Taking a break
June, 26 – BTC analysis
June, 28 – PUNDIX/BUSD (a new trick for you)
June, 28 – XLM/BUSD
Final results
Index
Other Books You May Enjoy
--- page 12 ---

Preface
Trading is like being a seasoned captain navigating the unpredictable sea of the market. You have your vessel, the
trading strategy, built with your knowledge and experiences. The instruments at your disposal, the indicators and
charts, act as your compass and map. The high and low tides of the sea mirror the volatile market prices.
Weather patterns come and go – storms of market uncertainty, peaceful periods of stable prices, the unpredictable
gusts of news events stirring the market – yet, the seasoned captain remains steady, adjusting the sails accordingly.
The goal is not to conquer the sea but to ride its waves, to understand its patterns, to respect its power, and to make it
an ally. Success is a journey rather than a destination, and each day brings a new sunrise, a new trading opportunity.
Just as the captain learns the sea’s moods over time, so does the trader grow in understanding the market’s rhythms.
Welcome to a journey through the intricate labyrinth of cryptocurrency trading. This book is your seasoned guide,
ready to lead you through the twists and turns and equip you with the knowledge to navigate the market’s volatile seas.
From debunking market myths to building a unique trading strategy, you’ll get the foundations you need to weather
even the most formidable market storms. It’s not just about theory; it’s also about practical, hands-on learning. We
explore the understanding of market participants, technical analysis, trading psychology, and money management
techniques. This journey is about understanding the ebbs and flows of the market, creating and refining your trading
system, and learning to ride the market waves, ever prepared for the next trading opportunity.
--- page 13 ---

Who this book is for
This comprehensive guide is designed to cater to the following audience:
Trading novices eager to learn the ropes and start their journey into cryptocurrency trading
Crypto market enthusiasts who want to actively participate in trading rather than just holding
Traders whose initial attempts haven’t been successful and want a structured path to improve their results
Learners who are interested in trading psychology and money management techniques
Anyone who wants to develop and automate their own successful trading strategies
Readers looking for hands-on examples, real-time scenarios, and a wealth of interactive resources to help them navigate the dynamic world of
cryptocurrency markets
Dive into structured lessons, learn about trading psychology and money management techniques, and develop and
automate your own successful trading strategies. With hands-on examples, real-time scenarios, and a wealth of
interactive resources, you’ll be well-equipped to navigate the dynamic world of cryptocurrency markets and unleash
your potential as a cryptocurrency trader.
--- page 14 ---

What this book covers
Chapter 1, Introduction to Cryptocurrency Trading, sets the stage for the structured learning experience that this
book aims to provide. The chapter will share the author’s story and process and then debunk market myths and explain
why many traders lose money. It will help you understand the pitfalls of information circulating among the trading
community and equip you with the practical knowledge needed for your trading journey.
Chapter 2, Understanding the Basics, is designed to help you navigate your emotional responses when trading
through a risk assessment questionnaire. You will also take your first steps in studying a chart on various timeframes
through a unique candlelight story. The chapter will delve into the trading behaviors of different market participants,
helping you comprehend why sudden buy or sell actions occur in the market, even if indicators suggest otherwise.
Finally, you’ll learn about the three different types of markets.
Chapter 3, Technical Analysis – Candles and Patterns, lays the foundation for your trading career by introducing
one of the most powerful charting tools: TradingView. This chapter will guide you to see the “story of the price” on
your screen and comprehend the emotions driving small price movements through candlestick patterns. You will
explore chart patterns for stronger and long-lasting movements, delve into support and resistance areas, and
understand the laws that govern them.
Chapter 4, Technical Analysis – Technical Indicators, introduces the most commonly used indicators in trading,
making sure you understand how each works and in which situations you should use them.
Chapter 5, The Centralized Exchange, demystifies the operations of centralized exchanges and trading procedures
on these platforms. The chapter also discusses an advanced tool that links to centralized exchanges, making the trading
process user-friendly.
Chapter 6, Money Management, dives into crucial aspects of trading strategy management, including loss limitation,
position sizing, the advantages of maintaining a trading journal, the essentiality of a precise trading plan, and the choice
between trading in stablecoin versus Bitcoin.
Chapter 7, Finding Your Edge, guides you through the extensive process of developing and implementing a
successful trading strategy, starting with the basics of a trading system, identifying potential trading patterns, and
culminating in defining entry and exit points – crucial elements for risk mitigation and profit securing.
Chapter 8, Automated Trading, focuses on the technical aspects of trading strategies, starting with creating a custom
indicator in TradingView using Pine Script. It then transitions to coding strategies using an open source bot for
cryptocurrency trading. This allows for 24/7 trade execution with accuracy and speed, effectively marrying your
trading ideas with technical execution for powerful, automated systems. Why not trade while you sleep?
Chapter 9, What’s Next?, is a road map for your journey after the book. Having learned sufficient theory and practice
and developed a strategy that can be traded manually or automatically, this chapter suggests a recommended path
forward.
Bonus Chapter, contains trades I took during one month of trading. Here, you can see me in action: see how I analyze
Bitcoin, how I think when entering the trades, and even what I feel regarding consecutive wins and losses (yes, I have
those too!).
--- page 15 ---

To get the most out of this book
This book builds your trading knowledge from the ground up. If you are interested in automated trading (found in
Chapter 8), you will need basic programming knowledge in order to learn the Pine Script language, and basic Python
knowledge if you want to use Freqtrade to automate your strategy.
Software/hardware covered in the book
Operating system requirements
Python 3.10 or above
Windows, macOS, or Linux
Pine Script V5
If you are using the digital version of this book, we advise you to type the code yourself or access the code
from the book’s GitHub repository (a link is available in the next section). Doing so will help you avoid any
potential errors related to the copying and pasting of code. The GitHub repository also includes folders
with high-quality images for you to follow, along with templates for indicators, strategies, and a backtesting
methodology.
In the event any links in the book expire, kindly drop us an email at errataall@packt.com
Download the example code files
You can download the templates mentioned in this book from GitHub at https://github.com/PacktPublishing/Zero-to-
Hero-in-Cryptocurrency-Trading. If there’s an update to the code, it will be updated in the GitHub repository. You can
also find the color images there, in case you want to zoom in on the data presented.
We also have other code bundles from our rich catalog of books and videos available at
https://github.com/PacktPublishing/. Check them out!
Download the color images
We also provide a PDF file that has color images of the screenshots and diagrams used in this book. You can
download it here: https://packt.link/pXrot.
Conventions used
There are a number of text conventions used throughout this book.
Code in text: Indicates code words in text, database table names, folder names, filenames, file extensions,
pathnames, dummy URLs, user input, and Twitter handles. Here is an example: “We’re using the latest version of the
Freqtrade interface, v3. We will use the class name PrivateMACross to call the strategy from the command line.”
A block of code is set as follows:

class PrivateMACross(IStrategy):
    INTERFACE_VERSION = 3
--- page 16 ---

Any command-line input or output is written as follows:

docker-compose run --rm freqtrade backtesting --config user_data/config/config-backtestingbook.json --strategy PrivateMACross --timerange 20210811-20220812 --timeframe 1d -p BTC/BUSD
Bold: Indicates a new term, an important word, or words that you see onscreen. For instance, words in menus or
dialog boxes appear in bold. Here is an example: “If we run this strategy on BTCBUSD 4H and go to the Strategy
Tester tab, we’d get a -1% net profit.”
TIPS OR IMPORTANT NOTES
Appear like this.
Get in touch
Feedback from our readers is always welcome.
General feedback: If you have questions about any aspect of this book, email us at customercare@packtpub.com
and mention the book title in the subject of your message.
Contact the author: If you are interested in contacting the author, feel free to email him at
contact@vaidabogdan.com. Make sure to mention the title of the book in the subject of your email.
Errata: Although we have taken every care to ensure the accuracy of our content, mistakes do happen. If you have
found a mistake in this book, we would be grateful if you would report this to us. Please visit
www.packtpub.com/support/errata and fill in the form.
Piracy: If you come across any illegal copies of our works in any form on the internet, we would be grateful if you
would provide us with the location address or website name. Please contact us at copyright@packt.com with a link to
the material.
If you are interested in becoming an author: If there is a topic that you have expertise in and you are interested in
either writing or contributing to a book, please visit authors.packtpub.com.
Share Your Thoughts
Once you’ve read Zero to Hero in Cryptocurrency Trading, we’d love to hear your thoughts! Please click here to go
straight to the Amazon review page for this book and share your feedback.
Your review is important to us and the tech community and will help us make sure we’re delivering excellent quality
content.
Download a free PDF copy of this book
Thanks for purchasing this book!
Do you like to read on the go but are unable to carry your print books everywhere?
Is your eBook purchase not compatible with the device of your choice?
Don’t worry, now with every Packt book you get a DRM-free PDF version of that book at no cost.
--- page 17 ---

Read anywhere, any place, on any device. Search, copy, and paste code from your favorite technical books directly
into your application.
The perks don’t stop there, you can get exclusive access to discounts, newsletters, and great free content in your inbox
daily
Follow these simple steps to get the benefits:
1. Scan the QR code or visit the link below
https://packt.link/free-ebook/978-1-83763-128-5
2. Submit your proof of purchase
3. That’s it! We’ll send your free PDF and other benefits to your email directly
--- page 18 ---

1
Introduction to Cryptocurrency Trading
The main purpose of the book you’re holding right now is to provide you with a structured way to learn trading in a
way that isn’t so theoretical, as it dives right into developing and testing a working strategy that you can ultimately
automate and get tangible (and financial) benefits from.
In this first chapter, after I share my story and my process, I’ll delve right into market myths and why people lose
money in trading. As a heads up, most of the information that you hear from other traders (be it on YouTube or other
media) will actually sabotage you unless you are familiar with how the market works. My goal for this chapter is for
you to understand the myths that losing traders believe in so that you can circumvent them and get to the practical
information that will actually help you in your trading career.
In this chapter, we’re going to cover the following main topics:
Disclaimer
My journey into trading
Overview of the book’s structure
Market myths
Disclaimer
If you’re reading this book in order to become a super-trader and turn all your hard-earned income into billions, heed
my warning: this is not how the world works.
There is always an element of chance, and even by correctly applying a trading technique that statistically provides a
profit of 20% a month, you may lose money (and one of the reasons is statistics, which we’ll talk about later in the
book).
That being said, I truly believe that any reader who puts in the work will achieve a measurable degree of success, but I
cannot and will not promise any profits realized due to the methods presented here. I think that what any trader needs
(and what the world needs, for that matter) is clarity in the decisions they are going to make and the actions they’re
going to take.
What I can promise is that I will do everything in my power to help you understand how the market works, how you
can identify a way to beat it, and how you can test and automate a system that does that day and night. But the rest is
up to you.
You are still going to do all the hard work, from crunching the numbers to learning and applying what you’ve learned
numerous times until you develop a successful method. Such a feat is possible and probable, but only with a lot of
work.
Still, once that work is done, success is on the horizon, and once you get a taste of that, you are going to find this work
enjoyable and fruitful.
--- page 19 ---

Remember that once you have walked a path, even a hard path, walking it again is easier. You will know the road, the
signs, the milestones, and the expected outcome, and in time, your trading techniques and developed strategies will
become more efficient at beating the market.
My journey into trading
When I was little, I loved Indiana Jones movies. I wanted to travel to unfamiliar places, to have adventures, and to
experience unique things.
While growing up, I became that explorer. But more than an explorer of places, I became an explorer of learning. I
started coding in the 8th grade, and later, I got a well-paid job at a tech company. Then, I found myself needing to learn
to socialize better, so I joined Toastmasters and learned the art of public speaking, which got me second place at
Toastmasters’ national public speaking contest. Next, I started doing trainings and helping others learn and learn how
to learn. I broke down difficult theoretical concepts and taught them in an experiential, gamified way. I covered a wide
range of topics from time management to online course creation, leadership, and personality typologies, and trained
people from varied backgrounds such as business, education, and management. This training extended from my home
country to countries such as Iceland, Armenia, and China.
After that, I founded my company in sales trainings together with two co-founders, and during the pandemic, we
developed a new direction: we provided live webinars to teachers and helped them teach online. Then, we added three
other verticals: a national certified trainer-training program, B2B training, and a non-profit featuring a community of
40,000 teachers, helping them develop their teaching skills and grow as educators.
I started trading in 2004 (right before going to college) and increased my account, the equivalent of today’s $500, by
10% in only a trimester. I did it by learning and applying technical and fundamental analysis. During that first year, the
account grew even more. However, local politics heavily influenced the local stock market, and trading using insider
information (insider trading) was common at that time. I was frustrated at being unable to find the reasons behind price
movements long after they had occurred, and after a while, I closed my account to dedicate myself to college.
With crypto, I started with the hype of 2017 just before the market crash (the moment when a lot of people withdrew
money from crypto, leaving enthusiasts with cryptocurrencies worth less than what they bought them for). I think most
people in crypto start before a crash. I bought some Bitcoin (BTC) and some Ethereum (ETH), but suddenly, their
values dropped significantly. Still, the technology was unique, and I wanted to play in that market, so I started trading it
(and learning everything I could about it).
By learning, I mean delving into everything. When I become fascinated by a project, you can find me devoting 12
hours a day to that project. At that time, my company was successful and running on autopilot, so dedicating 4 months
to trading was not out of the question. You will see later in the book how I love creating automated systems of profit.
I was pretty successful at trading; during the bull market, I was outperforming Bitcoin’s growth by 15% a month
(trading all day), and I was looking into how I could automate my trading to better leverage my time. This is how I
started learning Pine Script, TradingView’s scripting language. Pine Script was used to display indicators on charts
on TradingView’s platform, and learning it helped me develop better strategies and code alerts that would make my
phone ring when a trading opportunity was near.
--- page 20 ---

During that time, I was following an influencer’s account (@EmperorBTC) and he posted a trading technique that I
found interesting. I coded his strategy in Pine Script so that I could check its historical success and get alerts as to
when I should enter and exit trades, and I shared the code with him. Next, I found myself added to a private group
with other successful traders who were trading at another level. Together with these traders and with EmperorBTC’s
guidance, we were learning at an accelerated pace and developing great strategies that were beating the market.
I was linking those strategies to bots and automating them, dreaming about owning a Tesla and yachting when the 2021
crash happened.
Suddenly, my money-making strategies were unprofitable. Everything that worked during the bull market was still
beating Bitcoin, but Bitcoin was also beating itself.
So, I left my dreams for another day and went back to the drawing board. My learning switched from Exocharts and
volume profile techniques to developing strategies that could work for both markets. I learned about algorithmic
trading, the pandas framework, statistics, and how to better evaluate trading strategies considering drawdowns,
market crashes, and other (not-so-rare) events.
Since then, I have immersed myself in the world of statistics and developed smaller timescale strategies that run on 5-
minute candles (a term I will explain in Chapter 2) and provide a smaller but consistent profit through a higher number
of trades. That is the place where I found I can best use my analytical mind to identify opportunities to beat the
market.
And here I am now, giving you a shorter path to arrive at this place of evidence-based trading—a place from which
you can identify, test, and automate profitable strategies.
Overview of the book’s structure
I am an avid reader. My Goodreads account features over 100 books read per year. That is one every three days,
including audiobooks. I mostly read fiction now, but I have read my fair share of personal development books and a
whole bunch of trading books. What I found out during my page-turning adventures is that most trading books fail in
two respects:
They aren’t clear enough. Basically, they jump from concept to concept, making it hard for you to follow, or they immerse you in stories and
don’t provide enough useful content.
They don’t provide a step-by-step guide to arrive, together with the author, at the finish line. What they do instead is superficially present
concepts, tease you, and promote other programs at the end of the book.
Regarding the second point, I actually know a trading book that is delivered for free (minus a shipping and handling fee
that actually includes the book’s price) and teases the reader with methods of success that they can access by paying
for a high-ticket program.
However, throughout this book, I aim to provide you with content that is easy to follow and helps you increase your
knowledge in cryptocurrency trading (or fill in the gaps if you’ve traded before) and, step by step, chapter by chapter,
get you to a point where you can develop a successful strategy and automate it.
I’ve organized the chapters sequentially, but feel free to skim anything that you already know. Note that I recommend
skimming, not skipping. Make sure that you fully understand the sections that you’re skimming so that you don’t miss
