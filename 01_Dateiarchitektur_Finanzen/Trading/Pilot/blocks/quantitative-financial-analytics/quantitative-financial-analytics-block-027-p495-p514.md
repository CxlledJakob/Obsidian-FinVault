# Quantitative financial analytics_ the path to investment profits.pdf — pages 495–514

--- page 495 ---

472
Quantitative Financial Analytics
The right side of Equation (10.14) is the expected geometric mean
return on portfolio i. The portfolio that maximizes this expectation
thus will maximize the expectation of terminal wealth. It can also
be shown (by the central-limit theorem) that the probability of the
maximum geometric mean portfolio resulting in greater terminal
wealth than any other available portfolio approaches unity as n
approaches inﬁnity.
All the above, however, are simply mathematical tautology. It
was shown earlier that the maximization of the geometric mean of
returns is consistent with the maximization of a log utility-of-wealth
function. Thus, if the investor possesses a log utility function or,
given the central limit theorem, if the number of investment periods
is inﬁnite, the geometric-mean criterion is suﬃcient. In some other
cases, it has been found to be a reasonable approximation. However,
Samuelson has shown that as long as n is ﬁnite, there exist classes of
utility functions for which the proposed criterion is not even a good
approximation. Indeed, he also demonstrated that there are classes
of utility functions for which no uniform strategy is optimal (see Paul
Samuelson, 1971) Even without Professor Samuelson’s argument,
there is a good question as to whether assumptions (1)–(3) above are
very realistic. The problems of multiperiod optimization are indeed
great, however, and are considered subsequently. It will soon be
apparent that the other techniques are suﬃciently troublesome that
geometric mean maximization becomes a very attractive alternative
if the assumptions are anywhere close to being fulﬁlled.
It should be noted from the outset that the portfolio and capital
market theory outlined above remains essentially unimplemented
even in the security investment ﬁeld. This result follows despite
the facts that: (1) securities are homogeneous and divisible; (2) the
returns from securities do not vary greatly with the holder (little
management and relatively simple tax eﬀects, at least at the margin);
(3) the markets for securities are relatively eﬃcient (in terms of
transaction costs, liquidity, and so on); (4) the returns from securities
appear to be independent over time (little if any serial correlation)
and, thus, independent of holding period; (5) a great deal of publicly
--- page 496 ---

Capital Market Theory, Eﬃciency, and Imperfections
473
available, machine-accessible information exist on most securities;
and (6) most securities of signiﬁcance trade in one national market.
Because none of the above analytical advantages apply as well (if
at all) to alternative investments such as real estate, private equity
holdings, etc., it should not be surprising to learn that, given the
current state of the art, it is impossible to integrate these investments
into portfolio selection in a completely satisfactory manner.
A very serious hindrance would appear to involve input generation. The diﬃculties with the determination of σ, µ for alternative
investments are considerable. For a Markowitz approach, it would be
necessary to estimate the covariance of returns between each holding
and every other holding. Obviously, an index approach would be
required. The Sharpe single index is probably too broad for mixed
asset portfolios, because no single index (such as gross domestic
product (GDP) or the prime rate of interest) could relate to all
assets and yet not include a great deal of “noise.” An intermediate
approach that oﬀers some promise is the use of a multiple index
model, which comes in two basic forms: (1) a model that relates the
returns on each class of asset to its appropriate index and then relates
the indices by means of a Markowitz covariance approach; and (2) a
model that relates index returns to another index (often GDP), in the
form of one index model on top of another. The latter is the easier
to solve because it essentially involves running the Sharpe model
twice (ﬁrst on the assets and then on the indexes); the diﬃculty
arises because of the amount of “noise” created by such a two-level
estimation procedure.
Finally, we are faced with the fact that prospective returns on
alternative investments cannot be estimated in the same way as
security returns. Because securities trade in reasonably good markets,
it is possible to employ the ﬁction of an “annual holding period,” from
which holding-period returns may be computed and regressed against
index (market) returns. Because of the assumption of independence
of securities’ returns, it then becomes possible to employ the expected
value of these historical relationships as a future estimate of the risk
and return of the security.
--- page 497 ---

474
Quantitative Financial Analytics
In conclusion, the inclusion of alternative investments in a
theoretically correct system of portfolio selection is hindered by
1. the lack of a quadratic integer programming algorithm;
2. the lack of an adequate index of returns;
3. the individualistic nature of such investments (with regard to
taxes, holding period, and so on) that makes the estimation of
returns from a general index (even a good one) diﬃcult;
4. the lack of market data to provide even ex post estimations of risk
and return;
5. the lack of independence of asset returns and non-replicability of
deals; and
6. portfolio restrictions, information imperfections, and so on that
preclude anyone from holding a perfectly diversiﬁed portfolio.
Over the course of time, expectations regarding the earning power
and dividend-paying potential of the ﬁrm, the risk of the same,
and the ﬁrm’s stock’s covariance with other securities will change.
Furthermore, the market price of the stock and the level of interest
rates will undoubtedly change. Finally, the investor’s utility function
itself may change or else changes in his level of wealth may cause
his degree of risk aversion to change. Any of these factors will tend
to cause the investor’s portfolio to be suboptimal. It then becomes
necessary to revise the portfolio.
Portfolio revision may be viewed as the general case of asset
acquisition and disposition, with portfolio selection representing the
special case of revision of the all-cash portfolio. As such, revision
involves all the problems of portfolio selection and some additional
diﬃculties as well. Any asset sold at a proﬁt, for example, becomes
subject to taxation that, in turn, reduces the amount of funds
available for reinvestment; it might thus be desirable to maintain
a position in a slightly inferior security if the capital gains taxes
would wipe out any advantage. Also, the purchase or sale of any
security will incur transaction costs, which also reduce the amount
to be invested. This problem could be ignored in portfolio selection
because it was assumed that the costs would be incurred no matter
--- page 498 ---

Capital Market Theory, Eﬃciency, and Imperfections
475
what was bought. A simple one-period revision model is presented
below to illustrate these eﬀects.
Let
µi = expected return on ith asset
Cij = covariance of return between ith and jth security
αi = amount invested in ith security at beginning of period
βi = amount invested in ith security at end of period before
portfolio revision
γi = amount in ith security after portfolio revision (decision
variable)
δi(ωi) = increase (decrease) in amount of ith asset held from
existing to revised portfolio
bi(si) = buying (selling) transfer cost of ith asset (b0 = s0 = 0 for
cash) and assumed proportional for convenience
ri = realized return on ith asset, composed of cash dividend
return (rc
i ) and capital gain return (rg
i ). By deﬁnition,
ri = rc
i + rg
i
tc, tg = ordinary income and capital gain tax rates for investor
The cash account at the end of the year is equal to beginning cash
plus all dividends after taxes:
βo = αo +
 n

i=1
rc
i αi

(1 −tc),
(10.15)
and the amount invested in each risk asset is:
βi(i=1,...,n) = (1 + rg
i )αi.
(10.16)
From this point, short sales and borrowing are excluded:
αi, βi, γi ≥0,
for all i, 0 to n.
(10.17)
By deﬁnition, the net change in holdings of the ith asset is given by
the diﬀerence between holdings in the end of period portfolio and the
--- page 499 ---

476
Quantitative Financial Analytics
revised portfolio:
δi −ωi = γi −βi,
δi, ωi ≥0
and δi or ωi or both = 0.
(10.18)
The total value of the portfolio after revision must equal the value
prior to revision less any transaction costs and taxes realized:
n

i=0
γi =
n

i=0
βi −
n

i=1

δibi + ωi

si +

1 + rg
i
−1
rg
i −si −rg
i si

tg

.
(10.19)
Subject to these constraints, the objective function then becomes:
Maximize Z,
Z =
n

i=0
(1 + µi)γi −λ


n

i=1
n

j=1
γiγjCij

.
(10.20)
Multiperiod revision models generally involve dynamic programming, in which the last-period portfolio is optimized ﬁrst and then
the model works backward to the present. Various limitations have
prevented the practical applications of such models except for very
small portfolios over a limited number of periods.
Two ﬁnal points should be made. One of the reasons that
dynamic programming is necessary stems from the contention that
one-period portfolio planning tends to be “myopic” (suboptimal over
many periods) unless the underlying utility function is a log or
power function. It has been shown, however, that if investors may be
assumed to be risk-averse and markets perfect, one-period investment
planning is consistent with long-run optimization. Finally, models of
the sort presented above include taxes and transaction costs, but not
information costs. But for the latter, the model could be run (and
revision take place) continuously. Because gathering information and
running the model do require time and money, however, the question
of how often to revise (or more precisely, consider revision) appears
to be unanswered at this time.
The reader will observe that much of the analysis (and citations
provided) above go back for ﬁve decades. Since then, research has
--- page 500 ---

Capital Market Theory, Eﬃciency, and Imperfections
477
gone oﬀin other directions (see below) but the seminal eﬀorts remain
the cornerstone of modern portfolio theory. Most Ph.D. students in
ﬁnancial economics have never actually read these early papers and
take for granted that the versions provided and embellished upon are
correct. It may be suggested that enterprising doctoral candidates
(especially in heterodox ﬁelds like statistics) could proﬁt by doing
further work suggested by these ancient papers.
Capital Markets: Eﬃciency and Imperfections
One of the major assumptions underlying capital market theory
presented so far was that investors possessed either homogeneous
(or a stable weighted average of) expectations regarding the future.
One implication of this assumption is that a change in expectations
will occur either unanimously or else in some stable average way
that is an operational equivalent of unanimity. Thus, if markets are
in equilibrium, a change in expectations will cause them to move
in a rapid and unbiased fashion to a new equilibrium. Markets
that behave in this manner will always “fully reﬂect” available
information, which is the deﬁnition of an eﬃcient market. Various
empirical tests have been made of the eﬃciency of the securities
markets, and these form the basis of the following discussion.
A point to be borne in mind, however, is that any proof of capital
market eﬃciency does not validate all the assumptions in Chapter 9.
Eﬃciency is a necessary condition for equilibrium, but it is not
altogether suﬃcient; we shall return to this point in the latter part
of the chapter.
It will be recalled, that, even in a world of perfect certainty,
prices of securities could be expected to change over time as long
as the income stream was not instantaneous and constant. Indeed,
price change would be necessary in such a case to cause the expected
return for each holding period to be obtained, that is,
P1 + D1 ≡P0(1 + r1),
(10.21)
or
P1 −P0 ≡r1(P0) −D1.
--- page 501 ---

478
Quantitative Financial Analytics
In a world of less-than-perfect certainty, changes in expected income
or the required rate of return (caused, in turn, by changes in the pure
rate or the perceived risk of the issue) could also cause the prices of
securities to change over time. It is argued, however, that only the
availability of new information or better analysis of already available
information should cause the expectations regarding income, risk,
and interest rates to change and, thus, prices to change for these
reasons. If it may be assumed that: (1) all relevant information
is available to all market participants; (2) any new information is
spread and assimilated immediately; and (3) vast numbers of market
participants employ the most sophisticated analytical techniques,
then the securities market may be viewed as a “fair game” where:
E[( ˜P1 + ˜D1)|I0] = P0[1 + E(˜r1|I0)].
(10.22)
The above merely states that the expected price of a security in
period one given the information available in period zero (assuming
all dividends or interests are reinvested) is equal to the price in
period zero times one plus the expected rate of return, given available
information. (This formula and material in this section are discussed
in more detail in Eugene F. Fama (1970). This hypothesis also implies
that (1) the excess market value of a security or (2) the excess
expected return to be earned by holding the security both have,
given available information, an expected value of zero.
Several points should be noted. Equation (10.22) does not imply
that prices need to be stable. Indeed, to the extent that E[ ˜D1]̸ =
E[˜r1](P0), then E[ ˜P1]̸ = P0. Thus, we have a probabilistic model
with implications similar to the certainty model (Equation (10.21)).
A major diﬀerence, however, is indicated by the presence of the
expectations operator and tildes for both the ( ˜P1 + ˜D1) and ˜r1 terms,
implying that they are random variables at time zero. Thus, although
the certainty model would indicate a constant rate of price change
over time (that is, linear on semilog graphs), the expectations model
indicates that price could be expected to vary about such a line.
Such a possibility is also reﬂected by the error term in the various
capital-market estimation models.
--- page 502 ---

Capital Market Theory, Eﬃciency, and Imperfections
479
Finally, it will be noted that both ( ˜P1 + ˜D1) and ˜r1 are conditioned by available information, Io. To the extent new information
or better analysis becomes available, E[ ˜P1 + ˜D1] and can alter, and
the expected rate of price change over time can shift. Adding the
assumption that the timing of the arrival of new information in the
market is a random variable, we see that shifts in the expectedprice-change line, as well as movement about it, can be treated as
random events. We shall now examine various eﬀorts to prove or
refute the eﬃcient markets hypothesis. This analysis answers some of
the questions that were suggested in Chapter 1 at the very beginning
of this book.
The earliest empirical work was produced by the “random walk”
hypothesis researchers primarily to attack the “technical analysts.”
Technical analysts have for many years contended that by analyzing
only the past price movements of a security, it is possible (or, “they
are able” — depending upon the size of the ego of the technical
analyst involved) to predict future price movements and thus make
greater-than-normal proﬁts. The distress of the random-walk followers is perhaps best expressed by Paul Cootner (1964, p. 232):
If any substantial group of buyers thought prices were too low,
their buying would force up the prices. The reverse would be true
for sellers. Except for appreciation due to earnings retention, the
conditional expectation of tomorrow’s price, given today’s price, is
today’s price.
In such a world, the only price changes that would occur are those
that result from new information. Since there is no reason to expect
that information to be nonrandom in appearance, the period-toperiod price changes of a stock should be random movements,
statistically independent of one another.
The early random walk writers, then, concerned themselves
with demonstrating that successive price changes were statistically
independent of each other, that various mechanical trading rules
based upon price changes did not yield proﬁts statistically superior
to a simple “buy-and-hold” strategy, and that “price changes from
transaction to transaction are independent, identically distributed
random variables with ﬁnite variances” implying, by the central
--- page 503 ---

480
Quantitative Financial Analytics
limit theorem, that for numerous transactions price changes will
be normally distributed (see Fama, op. cit., p. 399). The Cootner
volume contains many of the earlier studies and the Fama article has
an extensive bibliography, so one is not reproduced here. Selected
references are included at the end of the chapter.
More recent theorists have reﬁned certain parts of the basic
random-walk argument. In the ﬁrst place, it is suggested that price
changes do not follow a true random walk (with an expected value of
zero), but rather a submartingale (with an expected value greater
than zero). A martingale is a process in which the conditional
expectation of the (n+1)th observation, given a set of data, is the nth
observation. Rates of return are often assumed to follow a martingale,
such that the expected value of the price given information up to a
point t−1 (It−1) equals the price at time t−1, or E(Pt|It−1) = Pt−1.
A submartingale is a similar concept with E(Pt|It−1) ≥Pt−1; stock
prices are generally assumed to follow a submartingale process.
A random walk is a very strict form of martingale that assumes
not only the mean but the entire distribution to be the same.
Thus, the theory can take long-run price trends into account and
accept a very modest amount of serial correlation in successive price
changes. In view of the general upward trend of prices over time,
it was surprising to many observers that the statistical case against
absolute independence of successive price changes was as weak as it
was. The challenge to the technicians has become to demonstrate
that their rules can earn greater-than-normal proﬁts.
It has also been contended that price changes are not normally
distributed about an expected trend but rather belong to the broader
family of stable Paretian distributions of which the normal is only a
limiting case. The implication for our purposes is that the “fat-tailed”
stable distributions have an inﬁnite variance, such that the usual
portfolio approach employing σ and cannot be used if prices (and,
thus, returns) are so distributed. Fama has demonstrated, however,
that a similar form of analysis, employing a diﬀerent dispersion
parameter, can be employed. See Eugene F. Fama (1965).
Although the weak tests of capital market eﬃciency dealt with
the inability to make proﬁtable predictions of future prices from past
--- page 504 ---

Capital Market Theory, Eﬃciency, and Imperfections
481
prices, a second form of testing (called the “semi-strong eﬃcient
market hypothesis”) attempted to prove that prices reﬂect all
available information. These tests sought to demonstrate that new
information results in a rapid adjustment to a new equilibrium price
that, by implication, is taken to demonstrate that the price at any
time must reﬂect available information. Speciﬁcally, the tests took
events such as announcements of stock splits, earnings, dividends,
interest-rate changes, and so on, and studied (1) how rapidly a price
adjustment was made and (2) whether the price adjustment was
an unbiased evaluation of the information (such that subsequent
adjustments were as likely to be in one direction as the other).
The results of the tests conﬁrmed that price adjustments occur
rather quickly after the ﬁrst public announcement of the information,
implying that at least a signiﬁcant portion of the market receives
and interprets the information quickly. It follows, then, that the
initial price adjustment has been generally found to be unbiased.
A price trend caused by the slow spread and interpretation of new
information could result in a proﬁtable return for swift action; that
such a trend does not occur seems aﬃrmed.
In a crude sense, it could be said that the weak tests indicate
that one cannot become wealthy as a technician (forecasting price
or return movements based on past behavior), and the semi-strong
tests indicate that, by the time one reads some new information, it is
too late to proﬁt from it. The theory still allows a person possessing
superior information or analytical techniques to expect a better-thannormal return. A third form of testing (called the “strong eﬃcient
market hypothesis”) went all the way to asking if there can be any
information not reﬂected in the price of a security such that anyone
can expect above-average proﬁts. During the 1920s, it was claimed
that “any day is a good day to buy a good stock.” If the strong form
of the eﬃcient capital market hypothesis held, then, “any day is as
good as any other day to buy any stock (or bond, or mutual fund,
and so on).”
The rationale for the strong tests lies in a combination of the
semi-strong tests (information assimilated in a rapid and unbiased
fashion) and the fact that a great many supposedly knowledgeable
--- page 505 ---

482
Quantitative Financial Analytics
and trained people are engaged in the securities business. It is argued
that with so many people and so much information, there should
be few if any true “sleepers.” Studies have indicated that corporate
insiders may have superior information and thus higher expected
returns. Other investors, however, have not been shown to produce
consistently higher returns. In particular, numerous studies of mutual
funds have shown that their average performance is, if anything,
inferior to the market as a whole.
It also appears that, even for individual funds, past success is an
unreliable guide to future performance. In sum, it has been shown
that the investor could do better picking securities at random than
with the average mutual fund. And, because mutual funds are viewed
as possessing as much information, analytical skill, and diversiﬁcation
as any investor, their inability to out-perform the market is taken
as very compelling evidence in support of the strong form of the
eﬃcient markets hypothesis. It should be noted, however, that even
in academic circles, the strong form has a much smaller following
than the other two tests.
Capital Markets and the Real World
In order to justify the time and money spent on the study of
investments (including the purchase price of this book), it is necessary to come to terms with the strong form of the eﬃcient capital
markets hypothesis. Indeed, if the consumer groups gain additional
strength, it may soon be necessary to place on the dust jacket of
all investments books “Caution: Studies have shown that contents
provide no advantage over random selection.” Nevertheless, it should
be remembered that the strong-form tests are based almost entirely
on mutual-fund performance. Some may question the use of these
institutions as absolute proof that, if they cannot outperform the
market, no one can.
For several reasons, it may be argued that mutual funds are an
unconvincing choice for a test of the strong form of the eﬃcient
capital markets hypothesis. First, the level of training and education
of a number of fund managers is not terribly high. Although many
--- page 506 ---

Capital Market Theory, Eﬃciency, and Imperfections
483
funds are operated by competently trained managers, many more
are not. Second, The compensation scheme employed by most funds
encourages suboptimal behavior. Small funds take excessive risks in
order to achieve the top of the annual performance lists. This is
done in order to gain new shareholders and the subsequent proﬁts
derived from percentage-of-assets management fees. Third, large
funds cannot acquire substantial amounts of any promising issue
without inﬂuencing market price unless their position is accumulated
over time. Moreover, when a fund has acquired a large holding
of a thinly traded issue, the position cannot be liquidated easily
without inﬂuencing price. Fourth, even if large funds could ﬁnd small
companies whose stock evidenced very lucrative future potential, the
shares of these ﬁrms would represent only a small percentage of a
large fund’s assets. Hence, the fund could not increase its return
signiﬁcantly even if it did ﬁnd securities that signiﬁcantly outperformed the market. Fifth, legal requirements constrain open-ended
(mutual) funds to hold over-diversiﬁed portfolios.
There are a number of legal and institutional arrangements that
tend to undermine many of the assumptions required for a capital
market theory in addition to those that produce market ineﬃciency.
In particular, it appears unlikely that market portfolios are (or can
be) maintained by a substantial part of the investment community.
In the ﬁrst place, we can observe that legal and institutional
arrangements eliminate some securities from consideration, much less
selection, by certain investors. Banks and savings associations, for
example, are eﬀectively prohibited from owning any stock (with a
few insigniﬁcant exceptions). Banks, savings banks, and some other
institutional investors are also eﬀectively precluded from owning lowgrade (Ba or lower) bonds. Thus, whole classes of securities do not
appear in the investment universe for the aﬀected institutions.
More pervasive still than the outright prohibitions of securities
are the various limitations on holdings. Thus, although most life
insurance companies may legally purchase stock, they may only do
so to a very small extent (5–10 percent of total portfolio). The
legally required “crude” diversiﬁcation also applies to banks. Many
of the above restrictions, and others, reﬂect a rather curious legal
--- page 507 ---

484
Quantitative Financial Analytics
philosophy that completely ignores portfolio concepts. It is generally
agreed that most ﬁnancial institutions serve a public purpose that
requires that they continue to exist and avoid insolvency. It is then
contended that this goal is best served by requiring the institutions
to have a low-risk portfolio (this assertion alone is questionable).
Moreover, it is felt that a low-risk portfolio is composed of a large
number of low-risk securities. Hence, some institutions are provided
with a “legal list” of high-rated, low-risk securities from which to
select their portfolios.
Others, especially trust departments, operate under the “prudent
man rule” (requiring them to exhibit the care a prudent man would
in managing his own aﬀairs). Unfortunately, the courts seem to
feel that this philosophy represents prudence. Thus, the investment
manager must be concerned not only that the portfolio succeed but
also that no individual security fail lest he be sued. “Prudence”
usually prevails. It is an unfortunate truism that no trustee has
been successfully sued for portfolio dissipation because he invested
in government bonds. It should be observed that recent court actions
indicate that the prudent man rule may eventually be abandoned.
However, the growing demand that funds be channeled to “socially
desirable” investments (which can include mortgages, municipals,
minority loans, pollution control equipment loans, or loans to
whatever other powerful special-interest group desires cheap money)
is causing an entirely new set of constraints to arise to take its place.
A second set of legal and institutional constraints also mitigates
against the validity of some necessary assumptions of capital market
theory. It appears very likely that the separation theorem probably
does not apply in the real world. In addition to all the investment constraints already considered, it should be noted that many
institutions are prohibited from selling short, while individuals are
limited in this regard. Both institutions and individuals are also quite
restricted in borrowing against their portfolios. Some institutions
can have only a limited (or no) debt outstanding, and individuals
are subject to Federal Reserve margin requirements. It thus cannot
even be pretended that the crucial assumption that the investment
decision is independent of the ﬁnancing decision holds.
--- page 508 ---

Capital Market Theory, Eﬃciency, and Imperfections
485
It seems clear that many investors cannot hold the market
portfolio. It is also clear that the separation theorem does not apply.
Can it be argued, consequently, that capital market theory (and
eﬃciency implying equilibrium) is invalid? Economists would say no.
As long as some participants can borrow and others can lend and
every security can be held by at least some participants, the eﬃciency
proponents can bring forth their stable weighted average arguments.
The latter then becomes an argument in positive economics: markets
behave as though they were in static equilibrium with all participants
having free access and homogeneous expectations, even though this is
not indeed the case. This argument will fail to hold to the extent that
changes in the distribution of wealth alter the weights or diﬀerent
participants do not revise their expectations proportionately to new
information.
Expectations, Convergence, and the Eﬃcient
Market Hypothesis
In most areas of economics, dynamic theory is the most complicated form of analysis. This is true because expectations, rather
than existing conditions, are the main determinants. Equilibrium
is based on a given state of expectations, and any changes in
those expectations will force a movement to a new equilibrium.
Unfortunately, “the adjustments needed to bring about equilibrium
take time.” See J. R. Hicks (1946). When markets are ineﬃcient,
time becomes the most important variable to the analysis. But
when markets are eﬃcient, the adjustments occur rather quickly
and time is not terribly important. A perfectly eﬃcient market
will return to equilibrium immediately. Proponents of the eﬃcientcapital-market hypothesis maintain that timing is not important in
analyzing investments because the market digests new information
instantaneously, redetermines expectations, and recalculates prices
accordingly.
A condition of static equilibrium can cease to exist if new
information concerning systematic risk, expected dollar returns, or
the market price of systematic risk (that is, the slope of the SML) is
--- page 509 ---

486
Quantitative Financial Analytics
perceived. For example, let us assume a market in which all dividends
are reinvested so that returns over the next period (t = 1) are
given by:
˜r1 =
˜P1 −P0
P0
,
(10.23)
where ˜r1 is the expected return one period hence; ˜P1 the expected
market price of the stock one period hence (with dividends reinvested), and P0 the current market price (t = 0).
We further assume that time periods are very short (that is, they
are too short to act between t = 0 and t = 1). Finally, we assume
that R is the appropriate return for a given level of systematic risk
(taken from the SML). In equilibrium,
E(˜r1|I0) = R = r0.
(10.24)
If R changes because of either a shift in the SML or a change in the
systematic risk of a stock, there exists a new R∗(R∗̸ = R) which will
produce the potential for a windfall gain between t = 0 and t = 1
of ω.
E(˜r1|I∗) = R + λω
= R + λ
 ˜P ∗
1 −˜P1
P0

(10.25)
E(˜r2|I∗, λ = 1) = R∗,
(10.26)
where I0 = available information at period t = 0; I∗= new information becoming available between t = 0 and t = 1; R∗= the new
equilibrium return, given new information about either the level of
risk evidenced by the shares or the position of the SML; P0 = the
share price at t = 0; ˜P1 = the share price at t = 1 corresponding to
information; ˜P ∗
1 = the share price at t = 1 corresponding to information; λ = a one-period price adjustment coeﬃcient; and ω = the
potential windfall gain which would occur between t = 0 and t = 1
assuming complete adjustment (that is, where λ = 1).
If markets are eﬃcient, λ = 1 and adjustment takes place
immediately. Because time periods are assumed to be short, only
--- page 510 ---

Capital Market Theory, Eﬃciency, and Imperfections
487
those holding the security when new information reaches the market
will receive the windfall (that is, ω will result too quickly for anyone
to act on the information proﬁtably). Beyond period t = 1, the only
return expected would be the new equilibrium rate R∗. If markets are
ineﬃcient, λ̸ = 1 and adjustment will not take place immediately. In
the case 0 < λ < 1, the entire windfall gain will not be allocated
before proﬁtable action can be taken. Indeed, if λ < 0 (which
corresponds to a complete misinterpretation of the new information),
then a potential windfall even greater than ω could be possible to
the extent that the market eventually interprets the information
correctly. If λ >
1, the market overreacts, and a windfall in the
opposite direction is possible.
We have considered two of the conditions that will produce
a disturbance in the static equilibrium of stock prices. The third
condition (a change in expected dollar returns) will initially manifest
itself as ˜P ∗
1̸ = ˜P1 whereas, in the former conditions, the disturbance
was introduced by R∗̸ = R. The analysis proceeds along similar
lines, with Equation (10.23) remaining intact. The expected return
for t = 2, however, becomes:
E(˜r2|I∗, λ = 1) = R.
(10.27)
In all three instances, empirical evidence suggests that λ is close
to 1. Nevertheless, all the semi-strong studies have examined I∗of
a fairly obvious sort (earnings announcements, stock splits, and so
on). They do not address themselves to the fact that analysts may
obtain other kinds of I∗that cannot be neatly measured. The analyst
who has a better forecasting method, for example, may be able to
discern information that no simple sort of empirical investigation
could detect, and his long-term returns could be expected to surpass
the market return.
Of course, determining better I∗is what security analysis is all
about. The analyst should be cautioned, however, that his returns
will be above the market’s only if what he knows eventually becomes
known by the market (hence, producing a new equilibrium). If he
envisages a disequilibrium that will produce a windfall gain (ω) and
the market never “learns” (λ = 0 in all future periods), he is better
--- page 511 ---

488
Quantitative Financial Analytics
oﬀonly to the extent that his superior insight allows him to earn
higher returns for a given level of risk than would be provided by the
market’s perception of equilibrium risk–return relationships.
He does not earn the windfall adjustment return, however, that
would follow if the market eventually came to agree with his superior
insight. On the other hand, if the market received and correctly
interpreted new information at the same time as the analyst (λ = 1),
no above-normal returns would be expected. Thus, the analyst must
be rather sure that his insight is indeed superior, and that the market
will eventually agree with him, in order to derive the most beneﬁt
from his prognostications.
Expectations about future dollar returns (and estimated risk)
may be even more important than expectations about future rates of
return for making above-average proﬁts. If an analyst foresees better
prospects for a security than the market, he may get even greater
returns if the market eventually comes around to his view. Suppose
an analyst expects security C (Figure 10.15) to produce a future
stream that will yield 12 percent, given the current market price
($100), but the market only forecasts a 10 percent return, which
is the equilibrium yield. The analyst expects a perpetual earnings
stream (perhaps in the form of dividend payments) of $12, whereas
the market only expects $10. If the analyst turns out to be correct,
µ
µC’
µC
CiM
C’
C
fpure
SML
Figure 10.15. Diﬀerences in Expected Rates of Returns
--- page 512 ---

Capital Market Theory, Eﬃciency, and Imperfections
489
the price of the security will rise to $12/0.1 = $120, assuming the
stock is still in the 10 percent risk class. If the market moves toward
the analyst’s position within one year, his return would not only be
better than the equilibrium 10 percent, but also exceed his expected
12 percent. His yield, in fact, would be (120 + 12 −100)/100 =
32 percent.
This result can be found by using Equation (10.24). Assuming
the reinvestment of dividends, the stock price at t = 1 would be
$120 + $12 = $132. The price that would prevail without market
recognition would be expected to be $110 (the market anticipates
$10 in dividends, rather than $12, for reinvestment). Hence, when
recognition occurs λ = 1 and:
E(˜r1|I∗) = R + λ
 ˜P ∗
1 −˜P1
P0

= 10 percent + (1)

132 −110
100

= 32 percent.
Again, the time required for convergence is seen to be very important.
If it took the market three years to converge (suppose the stock paid
$12 in years one and two, but the market only became convinced
that this dividend could hold in the long run in period t = 3), his
return would be:
at 18 percent
t = 0
−$100(1.000) = −$100.00
t = 1–3
+
12(2.174) = +
26.09
t = 3
+ 120(0.609) = +
73.08
−$
0.83,
or just under 18 percent. If the market never came to accept the
analyst’s judgment (and the yield, in fact, was 12 percent), he would
still earn a larger return than that expected by the market. On the
other hand, if the analyst’s view were adopted by the market, his
return would be far greater still. Thus, having better insight than
the market would have given the analyst a 2 percent higher return
--- page 513 ---

490
Quantitative Financial Analytics
in our example (12 percent −10 percent), whereas having insight
about patterns of market expectations could produce a 20 percent
additional return (that is, 32 percent −12 percent).
The movement of stock prices from expected levels to those that
the analyst thinks are justiﬁable is called convergence. The principle
of convergence has been recognized by conventional authorities for
years, and the importance of timing in convergence has been given
renewed consideration. It is clear that rapidity of convergence will
greatly inﬂuence returns, and the longer the time required for the
market to recognize the superior insight of the analyst, the lower
will be his annual rate of return. In terms of the SML, convergence
takes place as the market realizes that a security is under (or over)
priced and that the security moves toward the line. In Figure 10.16,
two securities are shown. The ﬁrst, A, is seen to be “under” priced.
That is, the return from is greater than it should be given A’s
risk characteristic. Once the market agrees that A is under priced,
demanders will bid up prices until the security reaches the SML at A’.
At this point, the rate of return will be µ′
A, which, of course, is lower
than µA. In the process of reaching equilibrium, the security rises
in price, and investors who bought A when its yield was µA receive
a windfall gain. Similarly, security B is over priced, given its risk
characteristic. Its price will be bid down (expected returns rising
µ
µA’
µB
µA
µB’
CiM
B’
A’
A
B
rpure
SML
Figure 10.16. Convergence and the SML
--- page 514 ---

Capital Market Theory, Eﬃciency, and Imperfections
491
from B to B′) until it reaches the SML, if the analyst is correct in
his appraisal. Investors who sold B short would reap a windfall gain
as the price of B falls to yield µ′
B.
The investor who wishes to achieve returns above the market
must consistently ﬁnd securities that are under (over) priced, buy
(sell short), and hope that the market soon agrees with him. Eﬃcientmarket proponents would argue that no one could repeatedly ﬁnd
securities oﬀthe SML, and even if he could, this would not
constitute “beating the market.” It is suggested that even if a true
disequilibrium security is found and a capital gain is obtained, the
market has not been “beaten.” The equilibrating mechanism of
the market is what allowed the capital gain. Notwithstanding the
semantics of the argument, it seems only logical that one who could
ﬁnd securities oﬀthe SML frequently would enjoy above-average
returns.
Expectations play a major role in convergence. Furthermore,
it is changes in expectations, rather than simply new information,
that inﬂuence returns. This distinction is important because all new
information does not change expectations. A stock split, for example,
does not change the fundamental position of the ﬁrm, and it should
not be surprising that the long-run eﬀect of a split on investor returns
is nil. On the other hand, expectations can change even though new
information does not develop.
Although all three conditions producing disequilibrium can aﬀect
future expectations, we will focus our attention on the market price
of risk (that is, shifts in the SML) and not the parameters of
an individual security. Examination of market factors, rather than
unique security characteristics, is more conducive to generalization
and comparison to prior theoretical work. Extending a Hicksian
scheme over the entire SML (Hicks, op. cit., p. 205), it could
be argued that there exists an elasticity of expectations about
equilibrium rates of return at a given level of systematic risk that
may be deﬁned as:
εx = E[ ˜Rt+1 −Rt]
(Rt −Rt−1) ,
(10.28)
