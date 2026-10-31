# Quantitative Trading_ How to Build Your Own Algorithmic -- Ernest P_ Chan -- Wiley Trading, 1, 2008 -- John Wiley & Sons, Ltd_ -- isbn13 9780470284889 -- e4d660df1c1a75e8676a28ff4f852fa7 -- Anna’s Archive.pdf — Chapter 1: Chapter 1 (pages 23–30)

--- page 23 ---

C H A P T E R 1
The Whats,
Whos, and Whys
of Quantitative
Trading
I
f you are curious enough to pick up this book, you probably have
already heard of quantitative trading. But even for readers who
learned about this kind of trading from the mainstream media
before, it is worth clearing up some common misconceptions.
Quantitative trading, also known as algorithmic trading, is the
trading of securities based strictly on the buy/sell decisions of computer algorithms. The computer algorithms are designed and perhaps programmed by the traders themselves, based on the historical performance of the encoded strategy tested against historical
ﬁnancial data.
Is quantitative trading just a fancy name for technical analysis,
then? Granted, a strategy based on technical analysis can be part of
a quantitative trading system if it can be fully encoded as computer
programs. However, not all technical analysis can be regarded as
quantitative trading. For example, certain chartist techniques such
as “look for the formation of a head and shoulders pattern” might
not be included in a quantitative trader’s arsenal because they are
quite subjective and may not be quantiﬁable.
Yet quantitative trading includes more than just technical analysis. Many quantitative trading systems incorporate fundamental
data in their inputs: numbers such as revenue, cash ﬂow, debt-toequity ratio, and others. After all, fundamental data are nothing but
1
--- page 24 ---

2
QUANTITATIVE TRADING
numbers, and computers can certainly crunch any numbers that are
fed into them! When it comes to judging the current ﬁnancial performance of a company compared to its peers or compared to its
historical performance, the computer is often just as good as human ﬁnancial analysts—and the computer can watch thousands of
such companies all at once. Some advanced quantitative systems
can even incorporate news events as inputs: Nowadays, it is possible to use a computer to parse and understand the news report.
(After all, I used to be a researcher in this very ﬁeld at IBM, working on computer systems that can understand approximately what a
document is about.)
So you get the picture: As long as you can convert information
into bits and bytes that the computer can understand, it can be regarded as part of quantitative trading.
WHO CAN BECOME A
QUANTITATIVE TRADER?
It is true that most institutional quantitative traders received their
advanced degrees as physicists, mathematicians, engineers, or computer scientists. This kind of training in the hard sciences is often
necessary when you want to analyze or trade complex derivative
instruments. But those instruments are not the focus in this book.
There is no law stating that one can become wealthy only by working with complicated ﬁnancial instruments. (In fact, one can become
quite poor trading complex mortgage-backed securities, as the ﬁnancial crisis of 2007–08 and the demise of Bear Stearns have shown.)
The kind of quantitative trading I focus on is called statistical arbitrage trading. Statistical arbitrage deals with the simplest ﬁnancial instruments: stocks, futures, and sometimes currencies. One
does not need an advanced degree to become a statistical arbitrage
trader. If you have taken a few high school–level courses in math,
statistics, computer programming, or economics, you are probably
as qualiﬁed as anyone to tackle some of the basic statistical arbitrage strategies.
--- page 25 ---

The Whats, Whos, and Whys of Quantitative Trading
3
Okay, you say, you don’t need an advanced degree, but surely
it gives you an edge in statistical arbitrage trading? Not necessarily.
I received a PhD from one of the top physics departments of the
world (Cornell’s). I worked as a successful researcher in one of the
top computer science research groups in the world (at that temple of
high-techdom: IBM’s T. J. Watson Research Center). Then I worked
in a string of top investment banks and hedge funds as a researcher
and ﬁnally trader, including Morgan Stanley, Credit Suisse, and so
on. As a researcher and trader in these august institutions, I had always strived to use some of the advanced mathematical techniques
and training that I possessed and applied them to statistical arbitrage trading. Hundreds of millions of dollars of trades later, what
was the result? Losses, more losses, and losses as far as the eye can
see, for my employers and their investors. Finally, I quit the ﬁnancial industry in frustration, set up a spare bedroom in my home as
my trading ofﬁce, and started to trade the simplest but still quantitative strategies I know. These are strategies that any smart high
school student can easily research and execute. For the ﬁrst time
in my life, my trading strategies became proﬁtable (one of which is
described in Example 3.6), and has been the case ever since. The
lesson I learned? As Einstein said: “Make everything as simple as
possible.” But not simpler.
(Stay tuned: I will detail more reasons why independent traders
can beat institutional money managers at their own game in
Chapter 8.)
Though I became a quantitative trader through a fairly traditional path, many others didn’t. Who are the typical independent
quantitative traders? Among people I know, they include a former
trader at a hedge fund that has gone out of business, a computer programmer who used to work for a brokerage, a former trader at one
of the exchanges, a former investment banker, a former biochemist,
and an architect. Some of them have received advanced technical
training, but others have only basic familiarity of high school–level
statistics. Most of them backtest their strategies using basic tools
like Excel, though others may hire programming contractors to help.
Most of them have at some point in their career been professionally
involved with the ﬁnancial world but have now decided that being
--- page 26 ---

4
QUANTITATIVE TRADING
independent suits their needs better. As far as I know, most of them
are doing quite well on their own, while enjoying the enormous freedom that independence brings.
Besides having gained some knowledge of ﬁnance through their
former jobs, the fact that these traders have saved up a nest egg
for their independent venture is obviously important too. When one
plunges into independent trading, fear of losses and of being isolated from the rest of the world is natural, and so it helps to have
both a prior appreciation of risks and some savings to lean on. It is
important not to have a need for immediate proﬁts to sustain your
daily living, as strategies have intrinsic rates of returns that cannot
be hurried (see Chapter 6).
Instead of fear, some of you are planning to trade because of
the love of thrill and danger, or an incredible self-conﬁdence that
instant wealth is imminent. This is also a dangerous emotion to bring
to independent quantitative trading. As I hope to persuade you in
this chapter and in the rest of the book, instant wealth is not the
objective of quantitative trading.
The ideal independent quantitative trader is therefore someone
who has some prior experience with ﬁnance or computer programming, who has enough savings to withstand the inevitable losses and
periods without income, and whose emotion has found the right balance between fear and greed.
THE BUSINESS CASE FOR
QUANTITATIVE TRADING
A lot of us are in the business of quantitative trading because it is
exciting, intellectually stimulating, ﬁnancially rewarding, or perhaps
it is the only thing we are good at doing. But for others who may have
alternative skills and opportunities, it is worth pondering whether
quantitative trading is the best business for you.
Despite all the talk about untold hedge fund riches and dollars
that are measured in units of billions, in many ways starting a
quantitative trading business is very similar to starting any small
business. We need to start small, with limited investment (perhaps
--- page 27 ---

The Whats, Whos, and Whys of Quantitative Trading
5
only a $50,000 initial investment), and gradually scale up the
business as we gain know-how and become proﬁtable.
In other ways, however, a quantitative trading business is very
different from other small businesses. Here are some of the most
important.
Scalability
Compared to most small businesses (other than certain dot-coms),
quantitative trading is very scalable (up to a point). It is easy to ﬁnd
yourselves trading millions of dollars in the comfort of your own
home, as long as your strategy is consistently proﬁtable. This is because scaling up often just means changing a number in your program. This number is called leverage. You do not need to negotiate
with a banker or a venture capitalist to borrow more capital for your
business. The brokerages stand ready and willing to do that. If you
are a member of a proprietary trading ﬁrm (more on this later in
Chapter 4 on setting up a business), you may even be able to obtain
a leverage far exceeding that allowed by Securities and Exchange
Commission (SEC) Regulation T. It is not unheard of for a proprietary trading ﬁrm to let you trade a portfolio worth $2 million intraday even if you have only $50,000 equity in your account (a ×40
leverage). At the same time, quantitative trading is deﬁnitely not a
get-rich-quick scheme. You should hope to have steadily increasing
proﬁts, but most likely it won’t be 200 percent a year, unlike starting
a dot-com or a software ﬁrm. In fact, as I will explain in Chapter 6
on money and risk management, it is dangerous to overleverage in
pursuit of overnight riches.
Demand on Time
Running most small businesses takes a lot of your time, at least
initially. Quantitative trading takes relatively little of your time. By
its very nature, quantitative trading is a highly automated business.
Sometimes, the more you manually interfere with the system and
override its decision, the worse it will perform. (Again, more on this
in Chapter 6.)
--- page 28 ---

6
QUANTITATIVE TRADING
How much time you need to spend on day-to-day quantitative
trading depends very much on the degree of automation you have
achieved. For example, at a hedge fund I used to work for, some colleagues come into the ofﬁce only once a month. The rest of the time,
they just sit at home and occasionally remotely monitor their ofﬁce
computers, which are trading for them.
I consider myself to be in the middle of the pack in terms of automation. The largest block of time I need to spend is in the morning
before the market opens: I typically need to run various programs to
download and process the latest historical data, read company news
that comes up on my alert screen, run programs to generate the orders for the day, and then launch a few baskets of orders before
the market opens and start a program that will launch orders automatically throughout the day. I would also update my spreadsheet
to record the previous day’s proﬁt and loss (P&L) of the different
strategies I run based on the brokerages’ statements. All of this takes
about two hours.
After that, I spend another half hour near the market close to direct the programs to exit various positions, manually checking that
those exit orders are correctly transmitted, and closing down various automated programs properly.
In between market open and close, everything is supposed to be
on autopilot. Alas, the spirit is willing but the ﬂesh is weak: I often
cannot resist the urge to take a look (sometimes many looks) at
the intraday P&L of the various strategies on my trading screens. In
extreme situations, I might even be transﬁxed by the huge swings
in P&L and be tempted to intervene by manually exiting positions.
Fortunately, I have learned to better resist the temptation as time
goes on.
The urge to intervene manually is also strong when I have too
much time on my hands. Hence, instead of just staring at your trading screen, it is actually important to engage yourself in some other,
more healthful and enjoyable activities, such as going to the gym
during the trading day.
When I said quantitative trading takes little of your time, I am
referring to the operational side of the business. If you want to grow
your business, or keep your current proﬁts from declining due to
--- page 29 ---

The Whats, Whos, and Whys of Quantitative Trading
7
increasing competition, you will need to spend time doing research
and backtesting on new strategies. But research and development of
new strategies is the creative part of any business, and it can be done
whenever you want to. So, between the market’s open and close, I
do my research; answer e-mails; chat with other traders, collaborators, or clients; go to the gym; and so on. I do some of that work in
the evening and on weekends, too, but only when I feel like it—not
because I am obligated to.
When I generate more earnings, I will devote more software development resources to further automate my process, so that the
programs can automatically start themselves up at the right time,
know how to download data automatically, maybe even know how
to interpret the news items that come across the newswire and take
appropriate actions, and shut themselves down automatically after
the market closes. When that day comes, the daily operation may
take no time at all, and it can run as it normally does even while I am
on vacation, as long as it can alert my mobile phone or a technical
support service when something goes wrong. In short, if you treasure your leisure time or if you need time and ﬁnancial resources
to explore other businesses, quantitative trading is the business
for you.
The Nonnecessity of Marketing
Here is the biggest and most obvious difference between quantitative trading and other small businesses. Marketing is crucial to most
small businesses—after all, you generate your revenue from other
people, who base their purchase decisions on things other than price
alone. In trading, your counterparties in the ﬁnancial marketplace
base their purchase decisions on nothing but the price. Unless you
are managing money for other people (which is beyond the scope of
this book), there is absolutely no marketing to do in a quantitative
trading business. This may seem obvious and trivial but is actually
an important difference, since the business of quantitative trading
allows you to focus exclusively on your product (the strategy and
the software), and not on anything that has to do with inﬂuencing
other people’s perception of yourself. To many people, this may
--- page 30 ---

8
QUANTITATIVE TRADING
be the ultimate beauty of starting your own quantitative trading
business.
THE WAY FORWARD
If you are convinced that you want to become a quantitative trader,
a number of questions immediately follow: How do you ﬁnd the right
strategy to trade? How do you recognize a good versus a bad strategy even before devoting any time to backtesting them? How do you
rigorously backtest them? If the backtest performance is good, what
steps do you need to take to implement the strategy, in terms of both
the business structure and the technological infrastructure? If the
strategy is proﬁtable in initial real-life trading, how does one scale
up the capital to make it into a growing income stream while managing the inevitable (but, hopefully, only occasional) losses that come
with trading? These nuts and bolts of quantitative trading will be
tackled in Chapters 2 through 6.
Though the list of processes to go through in order to get to the
ﬁnal destination of sustained and growing proﬁtability may seem
long and daunting, in reality it may be faster and easier than many
other businesses. When I ﬁrst started as an independent trader, it
took me only three months to ﬁnd and backtest my ﬁrst new strategy, set up a new brokerage account with $100,000 capital, implement the execution system, and start trading the strategy. The strategy immediately became proﬁtable in the ﬁrst month. Back in the
dot-com era, I started an Internet software ﬁrm. It took about 3 times
more investment, 5 times more human-power, and 24 times longer
to ﬁnd out that the business model didn’t work, whereupon all investors including myself lost 100 percent of their investments. Compared to that experience, it really has been a breeze trading quantitatively and proﬁtably.
