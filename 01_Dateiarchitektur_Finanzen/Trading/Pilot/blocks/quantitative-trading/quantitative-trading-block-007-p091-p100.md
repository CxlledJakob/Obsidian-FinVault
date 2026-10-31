# Quantitative Trading_ How to Build Your Own Algorithmic -- Ernest P_ Chan -- Wiley Trading, 1, 2008 -- John Wiley & Sons, Ltd_ -- isbn13 9780470284889 -- e4d660df1c1a75e8676a28ff4f852fa7 -- Anna’s Archive.pdf — Chapter 4: Setting Up Your Business (pages 91–100)

--- page 91 ---

C H A P T E R 4
Setting Up
Your Business
I
n this chapter, we will be taking a break from the technical aspect of trading to focus on the business side of it. Assuming that
your goal is to remain an independent trader and not work for
a money management institution, the choice of the business structure for trading is important. The main choice you have to make is
whether to open a retail brokerage account or to join a proprietary
trading ﬁrm. The next step is to determine what features of the brokerage or trading ﬁrm are important to you. Finally, you have to decide what kind of physical trading infrastructure you need in order
to execute your quantitative strategy.
BUSINESS STRUCTURE: RETAIL
OR PROPRIETARY?
As a trader, you can choose to be completely independent or semiindependent. To be completely independent, you can simply open a
retail brokerage account, deposit some cash, and start trading. No
one will question your strategy, and no one will guide you in your
trading. Furthermore, your leverage is limited by Securities and Exchange Commission (SEC) Regulation T—roughly two times your
69
--- page 92 ---

70
QUANTITATIVE TRADING
equity if you hold overnight positions. Naturally, all the proﬁts and
losses will accrue to you.
However, you can choose to join what is called a “proprietary
trading ﬁrm” such as Bright Trading, ECHOtrade, or Genesis Securities, and become a member of their ﬁrm. In order to become a
member of such ﬁrms, you have to pass the National Association of
Securities Dealers (NASD) Series 7 examination to qualify you as a
registered representative of a brokerage. You will still need to invest your own capital to start an account, but you will obtain much
higher leverage (or “buying power”) than is available through a retail account. Depending on how much capital you invested, you may
get to keep all your proﬁts, or some percentage of them. In terms
of liability, however, your loss is limited to your initial investment.
(Actually, liability is also limited if you form an S corporation or limited liability company [LLC] and open an account through this entity
at a retail brokerage.) Often, you can also receive training from the
ﬁrm, perhaps at an extra cost. You will also be subject to the various rules and regulations that the proprietary trading ﬁrm chooses
to impose on its members, in addition to rules imposed by the SEC
or NASD.
I made them sound like bad things when I spoke of rules and regulations imposed by proprietary trading ﬁrms. But, actually, some
of these rules (such as the prohibition from trading penny stocks
or the prohibition from carrying short positions overnight) are actually risk management measures for your own protection. Often,
when the going is good, traders will bemoan these constraints limiting their ﬂexibility and proﬁtability. They may even decide to start
their own retail trading accounts and start trading on their own.
However, when they suffer the (almost inevitable) big drawdown,
they wish that someone were there to restrain their risk appetites
and come to regret this unfettered freedom. (The teenager in us has
never left after all.)
The decision whether to go retail or to join a proprietary trading ﬁrm is generally based on your need of capital, the style of your
strategy, and your skill level. For example, if you run a low-risk,
market-neutral strategy that nevertheless requires a much higher
leverage than allowed by Regulation T in order to generate good
--- page 93 ---

Setting Up Your Business
71
returns, a proprietary account may be better for you. However, if
you engage in high-frequency futures trading that does not require
too much capital, a retail account may save you a lot of costs and
hassles. Similarly, a very experienced trader with strong risk management practices and emotional stability probably doesn’t need the
guidance given by a proprietary ﬁrm, but less experienced traders
may beneﬁt from the imposed restraints.
There is another consideration that applies to those of you who
have discovered some unique, highly proﬁtable strategies. In this situation, you may prefer to open a retail trading account, because if
you trade through a proprietary account, your proprietary trading
ﬁrm is going to ﬁnd out about your highly proﬁtable strategy and
may “piggyback” on your strategy with a lot of its own capital. In
this case, your strategy will suffer more market impact trading cost
as time goes on.
Table 4.1 summarizes the pros and cons for each choice.
One ﬁnal note: Some may think that there is a tax advantage
in joining a proprietary trading ﬁrm because any trading loss can
be deducted from current income instead of as capital loss. Actually, you can choose to apply for trader tax status even if you
have a retail brokerage account so that your trading loss can offset other income, and not just other capital gain. For details on the
tax considerations of a trading business, you can visit, for example,
www.greencompany.com.
CHOOSING A BROKERAGE OR
PROPRIETARY TRADING FIRM
Many traders use only one criterion to choose their brokerage or a
proprietary trading ﬁrm to join: the commission rate. This is clearly
an important criterion because if a trading strategy has a small return, high commissions may render it unproﬁtable. However, there
are other important considerations.
Commissions actually form only part of your total transaction
costs, sometimes even a small part. The speed of execution of
your brokerage as well as their access of the so-called “dark-pool”
--- page 94 ---

72
QUANTITATIVE TRADING
TABLE 4.1
Retail versus Proprietary Trading
Issue
Retail Trading
Proprietary Trading
Legal requirement to
open account.
None.
Need to pass NASD
Series 7 examination
and satisfy other
NASD-imposed
restrictions.
Initial capital requirement.
Substantial.
Small.
Available leverage or
buying power.
Determined by SEC
Regulation T.
Generally 2x leverage
for overnight
positions, and 4x for
intraday positions.
Based on ﬁrm’s
discretion. Can be as
high as 20x or more
for intraday or hedged
positions.
Liability to losses.
Unlimited, unless
account is opened
through an S
corporation or LLC.
Limited to initial
investment.
Commissions and fees.
Low commissions
(perhaps less than 0.5
cent a share) and
minimal monthly fees
for data.
Higher commissions and
signiﬁcant monthly
fees.
Bankruptcy risk of
brokerage.
No risk. Account
insured by Securities
Investor Protection
Corporation (SIPC).
Has risk. Account not
insured.
Training, mentoring,
guidance.
None.
May provide such
services, sometimes at
a fee.
Disclosure of trade
secrets.
Little or no risk,
especially if retail
brokerage does not
have proprietary
trading unit.
Has risk. Managers can
easily “piggyback” on
proﬁtable strategies.
Restrictions on trading
style.
No restrictions, as long
as it is allowed by SEC.
May have restrictions,
such as prohibitions
on holding overnight
short positions.
Risk management.
Mostly self-imposed.
More comprehensive
and imposed by
managers.
--- page 95 ---

Setting Up Your Business
73
liquidity also ﬁgures into your transaction costs. Dark-pool liquidity is formed by institutional orders facilitated away from the exchanges, or they come from the crossing of internal brokerage customer orders. These orders are not displayed as bid and ask quotes.
Some of the “alternative trading systems” that provide dark-pool
liquidity are Liquidnet and ITG’s Posit. Your brokerage may use one
or more of these providers, it may only use its internal crossing network, or it may use no alternative trading systems at all.
Sometimes, a better execution price at a large brokerage due
to its state-of-the-art execution system and high-speed access to
deeper dark pools of liquidity will more than compensate for its
higher commissions. This kind of cost/beneﬁt analysis cannot easily be carried out unless you actually trade on multiple brokerages
simultaneously and compare the actual execution costs.
For example, I trade through Goldman Sachs’s REDIPlus trading
platform, whose Sigma X execution engine routes orders to both its
internal crossing network as well as to external liquidity providers.
I have found that it often improves my execution price by more than
a few cents per share over execution on Interactive Brokers: more
than enough to offset its higher commissions.
Another consideration is the range of products you can trade.
Many retail brokerages or proprietary trading ﬁrms do not allow you
to trade futures or foreign currencies. This would be a serious limitation to your trading business’s growth.
Following these two fairly generic criteria, for a quantitative
trader, the next important one is: Does the trading platform offer an
application programming interface (API) so that your trading software can receive live data feed, generate orders, and automatically
transmit the orders for execution in your account? I will discuss
more about API in Chapter 5. The only point to note here is that
without an API, high-frequency quantitative trading is impossible.
Closely related to the availability of API is the availability of paper trading accounts. If a brokerage does not offer you a paper trading account, it is very hard to test an API without risking real losses.
Among the brokerages I know that offer paper trading accounts are
Interactive Brokers, Genesis Securities, PFG Futures (for futures
trading), and Oanda (for currency trading).
--- page 96 ---

74
QUANTITATIVE TRADING
In addition to paper trading accounts, some brokerages provide
a “simulator” account (an example is the demo account from
Interactive Brokers), where quotes from the past are displayed as if
they were real-time quotes, and an automated trading program can
trade against these quotes at any time of the day in order to debug
the program.
Finally, the reputation and ﬁnancial strength of the proprietary
trading ﬁrm you are considering is also important. This does not
matter to the choice of a retail brokerage because, as noted in Table 4.1, retail accounts are insured by the SIPC whereas proprietary
accounts are not. Hence, it is important that a proprietary trading
ﬁrm has a strong balance sheet and good risk management practices
to prevent the ﬁrm from collapsing because of bad trades made by
its fellow member traders. (WorldCom’s and Refco’s collapses are
good examples.) You should also make sure the ﬁrm is a brokerdealer registered with an exchange, so that it is regularly audited by
the exchange and the SEC. (As of this writing, non-broker-dealer
proprietary trading ﬁrms may all get shut down by the SEC anyway, starting with Tuco Trading in March 2008.) Furthermore, even
if times are good for the ﬁrm, does it have a good reputation for
easy redemption of your capital should you choose to do so? It is,
of course, difﬁcult for an outsider to assess whether a proprietary
trading ﬁrm has such good attributes, but you can read about the
ﬁrm’s reputation based on their current or ex-members’ opinions at
the online forum www.elitetrader.com.
If you are undecided whether to open a retail brokerage account
or a proprietary account, or which retail brokerage or proprietary
ﬁrm to use, you can in fact do both, or open multiple accounts. Unlike ﬁnding full-time employment in proprietary trading ﬁrms, just
joining them as a member, especially a remote-access member, does
not usually compel you to sign a noncompete agreement. You are
free to be a member of more than one proprietary ﬁrm, or have both
proprietary and retail trading accounts, as long as this fact is fully
disclosed to the proprietary trading ﬁrms involved and to the NASD
as “outside business activities” and prior permissions obtained. With
multiple accounts, it should be easier for you decide which cost
structure is more beneﬁcial to you and which account has the better
--- page 97 ---

Setting Up Your Business
75
infrastructure and tools for your automated trading system. And, in
fact, sometimes each account has its own pros and cons, and you
may want to have the ﬂexibility of keeping all of them open for trading different strategies!
PHYSICAL INFRASTRUCTURE
Now that you have set up the legal and administrative structure of
your trading business, it is time to consider the physical infrastructure. This applies to both retail and proprietary traders: Many proprietary trading ﬁrms allow their members to trade remotely in their
homes. If you are a proprietary trader who requires minimal coaching from your account manager and are conﬁdent in your ability to
set up the physical trading infrastructure yourself, there is no reason
not to trade remotely.
In the start-up phase of your business, the physical infrastructure can be light and simple. You probably have all the components you need in your home ofﬁce already: a good personal computer (practically any new computer with dual-core processors will
do), a high-speed (DSL or cable) Internet connection, and, less well
known, an uninterruptible power supply (UPS) so that your computer doesn’t get accidentally shut down in the middle of a trade because of electricity ﬂuctuations. The total initial investment should
not exceed a couple of thousand dollars at the maximum, and the
monthly cost should not be more than $50 or so if you don’t already
subscribe to cable TV.
Some traders wonder if having a TV tuned to CNBC or CNN
is a good idea. While it certainly won’t hurt, many professional
quantitative traders have found that it is not necessary, as long as
they also subscribe to another professional real-time newsfeed, such
as Thomson Reuters, Dow Jones, or Bloomberg. While Bloomberg
can cost almost $2,000 a month, various plans offered by Thomson
Reuters and Dow Jones can cost as little as $100 to $200 (though
some will require an annual contract). Bloomberg also has a free
Internet radio stream at www.bloomberg.com/tvradio/radio that announces breaking business news and commentaries. Also, instead
--- page 98 ---

76
QUANTITATIVE TRADING
of installing a TV in your ofﬁce, you can subscribe to CNBC Plus,
which will provide live streaming video to your computer. Of course,
too much real-time information may not necessarily lead to more
proﬁtable trades. For example, Michael Mauboussin of Legg Mason
cites a study that ﬁnds horse-racing handicappers less successful in
their predictions when they are given more information when ranking horses. (See Economist, 2007a, or Oldﬁeld, 2007.)
As your trading business grows, you may upgrade your infrastructure gradually. Perhaps you will purchase faster computers. A
quad-core computer at the time of this writing is considered fairly
high end. Of course, when you are reading this, an octal-core or better personal computer will probably be widely available. According
to a New York Times article (Markoff, 2007), PCs with octal-core
chips will be available as soon as 2010.
You will certainly want to purchase multiple monitors to hook
up to the same computer so that you have extended screen space
to monitor all the different trading applications and portfolios.
Maybe you will want to upgrade your Internet connection to a T1
line, too. As discussed in Chapter 2, any delay in the transmission of your order to your brokerage results in slippage, which
is quite real in terms of lost proﬁts. In fast-moving markets, every millisecond counts, and an upgrade in your Internet connection
speed may well pay for itself very quickly. (A T1 line can cost anywhere from $700 to $1,500, whereas a cable/DSL connection is usually under $50. A T1 line transmits information at 1.5Mbps, where
bps means “bits per second,” about twice as fast as a cable/DSL
connection.)
Once you have ﬁnally tested your trading strategy and discover
that it works in practice very well, it will be time to scale up the
business and consider “business continuity planning” so that your
trading strategy is resilient to common household disasters such as
Internet outage, electricity outage, ﬂooding, and so on. You can install your trading programs on a remote server located in a hosting
company; in fact, you can even “collocate” your computers containing your trading programs at the hosting company. (Having your
programs hosted or having your servers collocated will cost you
--- page 99 ---

Setting Up Your Business
77
anywhere from hundreds to over a thousand dollars a month.) You
can monitor, maintain, or update your trading programs running on
these servers remotely through common remote PC applications
such as GotoMyPC (about $15 a month), while the remote servers
will be sending orders directly to your brokerage. The advantage
of this setup is not only that your trading will almost never have
downtime, but that the Internet connection at the hosting company
is likely to be faster than what you have at home or in your ofﬁce. In
fact, for some ultra-high-frequency trading applications, it is advantageous to locate your servers near an Internet backbone as close as
possible to the exchange on which your trades will be executed. Just
Google the phrases “server hosting” or “collocation servers” and you
will ﬁnd numerous hosting ﬁrms offering such services.
SUMMARY
This chapter focused on those decisions and steps that you need to
take to bridge the research phase and the execution phase of your
trading business. I have covered the pros and cons of retail trading
versus proprietary trading and the issues to consider in choosing a
brokerage or proprietary trading ﬁrm.
In a nutshell, retail brokerages give you complete freedom and
better capital protection but smaller leverage, while proprietary
trading ﬁrms give you less freedom and less capital protection but
much high leverage. Finding a suitable retail brokerage is relatively
easy. It took me less than a month to research and settle on one and
I have not found a reason to switch yet. Finding a suitable proprietary trading ﬁrm is much more involved, since there are contracts
to sign and an exam (Series 7) to pass. It took me several months to
get my account set up at one.
Of course, you can choose to have both retail and proprietary
accounts, each tailored to the speciﬁc needs of your strategies. This
way, you can also easily compare their speed of execution and depth
of liquidity.
--- page 100 ---

78
QUANTITATIVE TRADING
Regardless of whether you have chosen to trade in a retail brokerage or join a proprietary trading ﬁrm, you need to make sure their
trading account and systems have these features:
r Relatively low commissions.
r Trade a good variety of ﬁnancial instruments.
r Access to deep pool of liquidity.
r Most importantly, API for real-time data retrieval and order
transmission.
I also described the progressive buildup of the physical infrastructure you need to build in order to run a trading business. Some
of the components of a trader’s operating environment mentioned
are:
r A dual-core or quad-core computer.
r A high-speed Internet connection (cable, DSL, or T1).
r A noninterruptible power supply.
r Real-time data and news feed and subscription to ﬁnancial TV
news channels.
r Server hosting or collocation.
Building out the physical trading infrastructure is actually quite
easy, since in the beginning you probably have all the components
ready in your home ofﬁce already. I have found that it is easy to
trade a million-dollar portfolio with nothing more than a few thousand dollars’ initial investment in your physical infrastructure, and
a few hundred dollars a month in operating cost. But if you want to
increase your trading capacity or improve your returns, additional
incremental investments will be needed.
Once you have considered and taken these steps, you are now
positioned to build an automated trading environment to execute
your strategy, which will be covered in the next chapter.
