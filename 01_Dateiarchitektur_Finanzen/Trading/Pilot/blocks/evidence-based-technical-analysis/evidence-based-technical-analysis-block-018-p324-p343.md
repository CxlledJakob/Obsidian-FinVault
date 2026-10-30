# Evidence-based Technical Analysis_ Applying the Scientific Method and Statistical Inference to Trading Signals.pdf — pages 324–343

--- page 324 ---

2. The slips of paper are then sampled with replacement 10 times. Each
time a date is withdrawn from the bucket, the date number is noted.
The number of samplings is 10 because that was the length of each
rule’s performance history. This is a requirement of the Bootstrap
Theorem. Suppose the following dates were selected: 5, 3, 5, 5, 7, 2,
5, 8, 1, 2.
3. Using the dates obtained in step 2, a pseudo-track record based on
the actual daily returns associated with these dates is created for R1.
This procedure is also carried out for R2. We now have a randomly
generated performance history of length 10 for each rule.
4. Recall that our goal is to generate the sampling distribution for the
best-performing rule in a universe of rules which have expected returns equal to zero. Because it is possible, in fact it is our hope, that
at least one of the rules tested has an expected return greater than
zero, the raw historical returns of R1 and R2 must be adjusted to have
mean returns of zero. To accomplish this, WRC determines the mean
daily return for each rule tested and subtracts this amount from each
individual daily return.44 In this example, R1’s mean daily return is 1
percent and R2’s is 2 percent. Thus 1 percent is deducted from each
of R1’s daily returns whereas 2 percent is deducted from each of R2’s
daily returns. This has the effect of shifting the distribution of daily
returns for each rule so that it is centered over zero. These adjusted
daily returns are now used.
5. The adjusted returns of R1 for days 5, 3, 5, 5, 7, 2, 5, 8, 1, 2 are averaged. The adjusted returns for R2 are also averaged.
6. The larger of these two mean values is held aside as the ﬁrst value
used to form the sampling distribution of the maximum mean return
of N rules. In this case N = 2.
7. Steps 2 through 6 are repeated many times (e.g., 500 or more times).
8. The sampling distribution of the statistic, maximum mean return
in a universe of N (2) rules whose expected returns are zero is
formed from these 500 values.
9. With the sampling distribution now in hand, the p-value can be
computed.
10. The p-value would simply be the fraction of the 500 values obtained
at step 7 that exceed the average return of the tested rule. (See Chapter 5 for the procedure.)
The example described above was intentionally highly simpliﬁed. In a
more realistic case the data miner would examine a much larger number
of rules over a much longer time period. But the procedure for generating
326 METHODOLOGICAL, PSYCHOLOGICAL, PHILOSOPHICAL, STATISTICAL FOUNDATIONS
--- page 325 ---

the sampling distribution would be the same. All this is done automatically by the WRC software, once it has been provided with the interval returns, (e.g., daily) of all rules tested. This set of data contains all the
information WRC needs to derive the sampling distribution that is appropriate for a particular data-mining venture. When many rules are tested
this can be a considerable amount of data. Currently, few data miners or
data-mining systems save this valuable information.
In Part Two of this book I will perform a case study of 6,402 rules for
trading the S&P 500 index. A version of WRC that incorporates some recent enhancements, which are described later, will serve as one method to
test the statistical signiﬁcance of the rules’ observed performances.
The Monte Carlo Permutation Method.
The Monte Carlo permutation method (MC) can also be used to generate the sampling distribution
required to evaluate the statistical signiﬁcance of rules found by data mining. As noted in Chapter 5, it uses different data than the bootstrap and it
tests a different formulation of the null hypothesis, or H0.
In terms of the data, MC uses the historical times series of a rule’s output values (i.e., +1, –1) as well as the market’s raw returns. In contrast, the
bootstrap uses the rule’s interval (e.g., daily) returns. In terms of the H0,
both WRC and MC test the notion that all rules examined during data mining have no predictive power. However, MC formulates H0 somewhat differently. To simulate the performance of a rule devoid of predictive power,
MC randomly pairs rule output values with daily market price changes. In
contrast to WRC, MC’s random coupling of output values and market
changes is done without replacement. Presumably, if rule output values
are randomly assigned to market changes, the performance would be consistent with the null hypothesis that the rule is worthless. The return
earned by the random pairings becomes the benchmark against which the
actual rule returns are compared. If a rule has genuine predictive power,
then its informed pairing of output values and market changes should generate signiﬁcantly better performance.
The performance of the random pairing is simply the rule’s value
(+1 or –1) multiplied by the market change randomly assigned to that day.
Thus, if a rule output of +1 gets paired with a day when the market rose,
the rule earns the market’s price change. Likewise, if a –1 rule output gets
randomly paired with a day on which the market fell, it earns that positive
amount that day. Losses occur on days when the sign of the rule’s output
value is opposite to that of the market’s price change.
After the full history of a rule’s output values have been paired with a
market price change, the mean return is computed. This is done for each
rule in the universe of N rules giving N mean returns. The maximum mean
return is selected, and this becomes the ﬁrst value used to construct the
Data-Mining Bias: The Fool’s Gold of Objective TA
327
--- page 326 ---

MC sampling distribution. This entire process is repeated many times
(>500) with different random pairings each time. The sampling distribution is generated from this large number of values.
Note that there is no need to reposition each rule’s return distribution
to be centered over zero as is done with WRC because it assumes that all
rules have an expected return of zero. In contrast, the MC sampling distribution’s mean is the expected return of a useless rule in a data-mining
venture. If, after randomly assigning rule values to market returns, the
sampling distribution is situated at a value greater than zero, so be it. pvalues can be computed directly from the MC generated sampling distribution, just as they would be with a sampling distribution generated by
alternative methods. The p-value is the area in the right tail of the distribution that lies at or beyond the back-tested rule’s mean return.
A limitation of the MC method compared to WRC is that it cannot be
used to generate conﬁdence intervals because it does not test a hypothesis about the rule’s mean return. MC’s null hypothesis is simply that all
rules tested have output values that are randomly correlated with future
market behavior.
To recap, the steps by which the MC permutation method generates
the sampling distribution for a data miner are:
1. Obtain the daily rule output states for all N rules examined during the
data-mining venture.
2. Each rule’s output values are randomly paired with a scrambled version of the actual future market price changes. Note that it is important the same pairings be used for all rules. Thus, if a rule’s output
value for day 7 is paired with the market return for day 15, this same
pairing must be done for all competing rules. This is done to preserve
correlation structure that may be present in the rules, which is one of
the ﬁve factors impacting the data-mining bias.
3. Determine the mean rate of return for each rule.
4. Out of these N rules, select the highest mean return. This value becomes the ﬁrst value for the sampling distribution of the mean for the
best mean among N useless rules.
5. Repeat steps 2, 3, and 4, M times (where M = 500 or some large
number).
6. Form the sampling distribution from the M values obtained in steps 2
through 5.
7. The p-value for a back-tested rules can be determined by determining
the fraction of the values obtained by step 6 that are equal to or
greater than its mean return.
328 METHODOLOGICAL, PSYCHOLOGICAL, PHILOSOPHICAL, STATISTICAL FOUNDATIONS
--- page 327 ---

Potential Flaws in Initial WRC and MCP Methods.
Both WRC
and MC test the null hypothesis that all rules in the data-mined universe
are useless. The rule miner hopes to reject this hypothesis in favor of
the alternative hypothesis: that not all the rules examined are useless.
As pointed out earlier, the meaning of the term useless depends on the
randomization method used. In the context of WRC, a useless rule has
an expected return equal to zero. In the context of the MC, useless
refers to a rule whose output values are randomly paired with the market’s future change.
As was discussed in Chapter 5, a hypothesis test can err in two ways.
A type-I error occurs when the null hypothesis is true (all rules tested really are useless) is rejected in error. This occurs when a rule that is in fact
useless managed to earning a high mean return and a low p-value by luck.
This is the data miner’s fool’s gold.
A type-II error occurs when the null hypothesis is in fact false and
should be rejected, but the rule’s performance is too low to do so. That is
to say, the rule really does have predictive power, but its virtue remains
undetected because it experienced bad luck during the back test. The data
miner winds up leaving real TA gold in the ground.
The ability of a hypothesis test to avoid making a type-II error is
referred to as the test’s power, not to be confused with a rule’s predictive power. Here, we are speaking of the power of a statistical test to
detect a false H0. So a hypothesis test is characterized by two measures
of goodness: its signiﬁcance (probability of making a type-I error) and
its power (probability of avoiding a type-II error). It is with respect to
the issue of power that initial versions of WRC and MCP are open to
criticism.
As pointed out by economist Peter Hansen,45 WRC and, by extension,
the MCP would both suffer a loss of power (increased likelihood of making a type-II error) when the data-mined universe contains rules that are
worse than the benchmark. This refers to a situation in which one or more
rules are actually worse than useless—they have expected returns that
are less than zero. This could occur, for example, if one were to reverse
the output value of a rule that has an expected return that is truly greater
than zero. Because approximately half of the rules tested in Part Two of
this book are obtained in this fashion (i.e., inverse rules), the research
presented in Part Two of this book is vulnerable to the problem discussed
by Hansen.
To evaluate Hansen’s criticism, the power of both WRC and MCP was
evaluated by Dr. Timothy Masters, on an ATR universe that contained
rules that were both better than and worse than the benchmark. In other
words, the evaluation simulated exactly the case that troubles Hansen.
These tests showed that his concerns are justiﬁed for a situation in which
Data-Mining Bias: The Fool’s Gold of Objective TA
329
--- page 328 ---

a rule with negative expected returns has an extremely large variance in
returns. This can drastically reduce the power of both WRC and MCP.
However, in cases that one is more likely to encounter in TA rule data mining, both methods are reasonably resistant to this problem. Therefore,
when there is one or more superior rules in the universe of examined
rules, both WRC and the MCP method have a reasonable chance of detecting them.
Recent Enhancement to WRC and MCP.
Despite the reasonable
power of the initial versions of WRC and MCP methods, a recent paper by
Romano and Wolf46 recommends a modiﬁcation that enhances the power
of WRC and that also appears to enhance the power of MCP. Thus the Romano and Wolf enhancement reduces the probability of a Type-II error.
This modiﬁcation was introduced to the versions of WRC and MC used in
Part Two’s case study. However, at this time, there is no commercial version of WRC with this enhancement. The MCP version with the enhancement is being placed in the public domain and codes for it will be made
available on a web site, www.evidencebasedta.com.
330 METHODOLOGICAL, PSYCHOLOGICAL, PHILOSOPHICAL, STATISTICAL FOUNDATIONS
--- page 329 ---

Theories of
Nonrandom
Price Motion
A
t the risk of stating the obvious, if market ﬂuctuations were completely random, TA would be pointless. TA is a justiﬁable endeavor
if and only if price movements are nonrandom to some degree
some portion of the time. This chapter offers several theories explaining
why episodes of nonrandom price movements ought to occur in ﬁnancial
market prices.
Although the occurrence of nonrandom price motion is necessary
to justify TA, this alone is not sufﬁcient to justify any speciﬁc TA
method. Each method must demonstrate, by objective evidence, its
ability to capture some part of the nonrandom price motion. Part Two
will evaluate a large number of TA rules with respect to their ability to
do just that.
THE IMPORTANCE OF THEORY
Several new theories from the ﬁeld of behavioral ﬁnance explain why
price movements are nonrandom to some degree and therefore potentially predictable . Thus, these novel theories take a position that is contrary to the efﬁcient markets hypothesis (EMH), a cornerstone of ﬁnance
theory for over 40 years. EMH contends that price changes in ﬁnancial
markets are random and, therefore, unpredictable. Therefore, these new
theories hold out hope for TA.
--- page 330 ---

The reader may wonder why theoretical support for nonrandomness
is even necessary. If a TA method has a proﬁtable back test, isn’t that all
that should be needed? It could be asserted that a signiﬁcantly proﬁtable
back test not only establishes that markets are nonrandom, it also establishes that the method is able to exploit some portion of the market’s nonrandomness.
This view misses the importance of theoretical support. Even when
all statistical precautions have been taken, a proﬁtable back test that is
not supported by sound theory is an isolated result and possibly still a
lucky one. A successful back test always provokes the question: Will the
rule continue to work in the future? Theory can be helpful here because a
back test that is consistent with sound theory is less likely to be a statistical ﬂuke. When a back test has theoretical foundation, it is no longer an
isolated fact, but part of a larger cohesive picture in which theory explains
fact and fact conﬁrms theory.
For example, the proﬁtability of technical trend-following systems in
commodity futures can be explained as compensation (i.e., a risk premium) for providing a valuable service to commercial hedgers, that of risk
transference. In other words, economic theory predicts that futures markets should manifest enough proﬁtable trends to motivate trend followers
to accept the price risks hedgers wish to shed.1 This is discussed later in
this chapter.
SCIENTIFIC THEORIES
In everyday speech, a theory is a speculative conjecture about why something is the way it is. As explained in Chapter 3, a scientiﬁc theory is something different. First, it offers a succinct explanation for a broad range of
prior observations. Second, and most importantly, it makes speciﬁc predictions that are later conﬁrmed by new observations.
Kepler’s laws of planetary motion2 concisely explained a large
number of prior astronomical observations and made speciﬁc predictions that were subsequently conﬁrmed by additional observations.
However, as good as Kepler’s laws were, Newton’s theory of gravitation
was better because it was broader in scope. It not only explained why
Kepler’s laws worked but explained a far wider variety of phenomena.
Theories of nonrandom price motion need not predict with the accuracy of physical theories. However, to be useful, they must not only succinctly describe a wide variety of previously observed market behavior,
but must also make testable predictions conﬁrmed by subsequent
observations.
332 METHODOLOGICAL, PSYCHOLOGICAL, PHILOSOPHICAL, STATISTICAL FOUNDATIONS
--- page 331 ---

WHAT IS WRONG WITH POPULAR TA THEORY?
Many TA texts offer no explanation about why their proposed methods
work. The statement of John Magee, author of one of TA’s seminal works3
is typical. He said, “We can never hope to know why the market behaves
as it does, we can only aspire to understand how. History obviously has
repetitive tendencies and that’s good enough.”
Some TA texts do offer explanations, but these are typically ad-hoc rationales that generate no testable predictions. According to author John
Murphy, the cornerstone premise of TA is “anything that can possibly affect the price—fundamentally, politically, psychologically, or otherwise—
is actually reﬂected in the price of that market.”4 One would be hard
pressed to extract testable predictions from such a vague statement.
Actually, this statement, which purports to explain why TA works,
contains a logical contradiction. For, if it were true that price did reﬂect
(i.e., discount) all possible information, it would imply that price was devoid of any predictive information. To understand why, assume a hypothetical price pattern has just occurred in stock XYZ, which is currently at
$50, and based on the pattern a move to $60 is implied. Then, by deﬁnition, when the pattern occurs its predictive implication has yet to be re-
ﬂected in prices. However, if the premise that price reﬂects all information
were true, the price would already be at the level predicted by the pattern,
thus negating the pattern’s forecasting ability.
This logical contradiction is even more apparent when it is pointed
out that EMH, a school of thought that rejects the efﬁcacy of TA, rests on
the very same premise; “prices fully reﬂect all available information.”5
Technical analysis cannot be based on the same premise as its mortal enemy. This contradiction is an example of cloudy uncritical thinking that is
all too common in the popular version of TA.
Fortunately for TA, its cornerstone premise that price reﬂects all information appears to be contradicted by fact. One example is the socalled underreaction effect, which has been postulated by behavioral
ﬁnance. It says that, because prices sometimes fail to respond to new information as rapidly as EMH theorists contend, a systematic price movement, or trend, toward a price level that does reﬂect the new information
occurs. The failure of prices to respond rapidly is caused by a several cognitive errors that afﬂict investors, such as the conservatism bias and the
anchoring effect. These are discussed later in this chapter.
Another popular justiﬁcation of TA is based on pop psychology. By
pop psychology, I mean principles of human behavior that seem plausible
but lack scientiﬁc support. According to noted economist and authority
in the ﬁeld of behavioral ﬁnance, Robert Shiller, “In considering lessons
from psychology, it must be noted that the many popular accounts of the
Theories of Nonrandom Price Motion
333
--- page 332 ---

psychology of investing are simply not credible. Investors are said to be
euphoric or frenzied during booms or panic-stricken during market
crashes. In both booms and crashes, investors are descried as blindly following the herd like so many sheep, with no minds of their own.”6 The
fact is, people are more rational than these pop-psychology theories suggest. “During the most signiﬁcant ﬁnancial events, most people are preoccupied with other personal matters, not with the ﬁnancial markets at all.
So it is hard to imagine that the market as a whole reﬂects the emotions
described by these psychological theories.”7 We will need to look beyond
the platitudes of popular texts for TA’s justiﬁcation. Fortunately, theories
developed in the ﬁeld of behavioral ﬁnance and elsewhere are beginning
to offer the theoretical support TA needs.
THE ENEMY’S POSITION: EFFICIENT MARKETS
AND RANDOM WALKS
Before discussing theories that explain why nonrandom price movements
should exist, we need to consider the enemy’s position, the EMH. Recently, some have argued that EMH does not necessarily imply that prices
follow unpredictable random walks,8 and that efﬁcient markets and price
predictability can coexist. However, the pioneers of EMH asserted that
random walks were a necessary consequence of efﬁcient markets. This
section states their case and examines its weaknesses.
What Is an Efﬁcient Market?
An efﬁcient market is a market that cannot be beaten. In such a market,
no fundamental or technical analysis strategy, formula, or system can earn
a risk-adjusted rate of return that beats the market deﬁned by a benchmark index. If the market is indeed efﬁcient, the risk-adjusted return
earned by buying and holding the market index is the best one can hope
for. This is so because prices in an efﬁcient market properly reﬂect all
known and knowable information. Therefore, the current price provides
the best estimate of each security’s value.
According to EMH, markets achieve a state of efﬁcient pricing because of the vigorous efforts of numerous rational investors attempting to
maximize their wealth. In their pursuit of true value, these investors are
constantly updating their beliefs with the latest information in a probabilistically correct manner9 so as to project each security’s future cash
ﬂows. Although no single investor is all knowing, collectively they know
as much as can possibly be known. This knowledge motivates investors to
334 METHODOLOGICAL, PSYCHOLOGICAL, PHILOSOPHICAL, STATISTICAL FOUNDATIONS
--- page 333 ---

buy and sell in such a way that prices settle at the equilibrium or rational
price level.
In such a world, prices change only when new information arrives.
When it does, prices change almost instantly to a new rational price that
properly reﬂects the news. Thus, prices do not gradually trend from one
rational price level to the next, giving the trend analyst a chance to get on
board. Not at all. In the world posited by EMH, prices trace a step function
as they move almost instantly from one rational level to the next. If the
news is favorable, prices rise, and if it’s unfavorable, prices fall. Because it
is not predictable whether the news will be favorable or unfavorable (it
wouldn’t be news if it was), price changes will be unpredictable as well.
This is illustrated in Figure 7.1.
The Consequences of Market Efﬁciency:
Good and Bad
Market efﬁciency has good and bad implications. They are good for the
economy as a whole but bad—very bad—for TA. They are good for the
economy because rational prices send vital signals of asset values that, in
turn, encourage the efﬁcient allocation of scarce resources, such as capital and labor. This fosters economic growth.10
However, prices in an efﬁcient market are unpredictable rendering all
forms of TA useless. According to Paul Samuelson, ﬁnancial market prices
Theories of Nonrandom Price Motion
335
Price
Time
Positive News Event
Negative News Event
Rational
Price
FIGURE 7.1
Efﬁcient market’s response to positive and negative news.
--- page 334 ---

follow a random walk because of the actions of many intelligent/rational
investors. In seeking to maximize wealth, they buy undervalued assets
pushing their prices higher and sell overvalued assets pushing prices
lower.11 “Taken to its logical extreme, it means that a blindfolded monkey
selecting stocks by throwing darts at a newspaper’s ﬁnancial pages could
do just as well as one carefully selected by the experts.”12
“EMH rules out the possibility of trading systems, based on available
information, that have expected proﬁts or returns in excess of equilibrium
expected proﬁt or return.”13 “In plain English, an average investor—
whether an individual, pension fund, or a mutual fund—cannot hope to
consistently beat the market, and the vast resources that such investors
dedicate to analyzing, picking and trading securities are wasted.”14 Although, under EMH, it is still possible to generate positive returns from an
investment strategy, when those returns are adjusted for risk, they will not
be superior to the return of buying and holding the market index portfolio.
The efﬁcient markets hypothesis also declares that when there is no
news entering the market, prices tend to oscillate in a random and unbiased fashion above and below the rational price level. See Figure 7.2. Because this level is itself subject to uncertainty, no technical or
fundamental indicator can reliably indicate when prices are above or below it. This means, for example, that in an efﬁcient market stocks with a
low price to book ratio, a well known fundamental indicator, are no more
likely to appreciate than stocks with a high price to book ratio. This is a
cold world for anyone looking for an edge.
336 METHODOLOGICAL, PSYCHOLOGICAL, PHILOSOPHICAL, STATISTICAL FOUNDATIONS
Price
Time
Rational
Price
FIGURE 7.2
Efﬁcient market hypothesis (random and unbiased pricing errors).
--- page 335 ---

False Notions of Market Efﬁciency
There are a number of commonly held but false notions about market ef-
ﬁciency. First is the idea that efﬁciency requires the market price to be
equal to rational value at all times. In fact, market efﬁciency simply requires that price deviates from rational value in an unbiased fashion.
Therefore, positive deviations from rational value are just as likely as
negative deviations, and at any point in time there is a roughly equal
chance that the asset’s price will be above its rational value as below it.
Moreover, these deviations are random. Thus the time series of pricing
errors in an efﬁcient market is a random variable whose probability distribution is centered at the rational price and is approximately symmetrical about it.
A second false notion about market efﬁciency is that it implies that
no one can beat the market. Actually, in any given time period, about 50
percent of all investors will outperform the benchmark index, while the
remaining 50 percent underperform. The notion that no single investor
or money manager can beat the market over the long term is equally
false. Given enough players, a small number are likely to have lengthy
streaks of market beating returns even if their strategies are totally without merit. Nassim Taleb15 shows that even if we assume money managers are no better than a blind monkey throwing darts16 (probability of
beating the market = 0.5) and the universe of managers is large enough,
say 10,000, after ﬁve years there is likely to be about 312 ﬁrms who have
beaten the market ﬁve years in a row. These lucky folks are the ones
who will send salesmen calling. The other 9,682 are less likely to knock
on your door.
The Evidence in Favor of EMH
As previously discussed, a scientiﬁc hypothesis plays a dual role: explanation and prediction. Its veracity is tested by comparing its predictions
with new observations. As discussed in Chapter 3, predictions are meaningful only if they are speciﬁc enough to offer the possibility of empirical
falsiﬁcation. If new observations do contradict a hypothesis’s predictions, the hypothesis is either reformulated and tested anew or thrown
out. However, what should be inferred when observations and predictions agree?
On this issue there is debate. Philosophers in the camp of David Hume
contend that no amount of conﬁrmatory evidence is ever sufﬁcient to
prove a theory, but in the practical world of science, conﬁrmation does
add strength to a hypothesis. If test after test yields observations that are
consistent with its predictions, that means something to most scientists.
Theories of Nonrandom Price Motion
337
--- page 336 ---

So EMH advocates have put forward a roster of supporting evidence.
Their evidence comes in two ﬂavors because EMH comes in two testable
ﬂavors: semistrong and weak.17 The semistrong form asserts it is impossible to beat the market with public information. Because this includes all
fundamental and technical data, the semistrong form predicts that neither
fundamental nor technical analysis can beat the market. This informal
prediction is not sufﬁciently speciﬁc to be testable, but it is in agreement
with the observation that people have great difﬁculty proﬁting consistently from market ﬂuctuations—and a lot try.
The semistrong form also makes several speciﬁc predictions that are
testable. One is that a security’s price will react quickly and accurately to
any news that bears on its value. The proper response of an efﬁcient market to news is illustrated in Figure 7.3.
This prediction implies prices should neither overreact nor underreact to news. This is testable in the following way. Imagine for a moment
that prices did not behave efﬁciently and did systematically overor underreact to new information. If this were the case, it would imply that
price movements would be predictable. To see why, consider what would
happen if a stock overreacted to news either by going up too much in response to good news or down too much in response to bad. Because EMH
says prices must stay close to rational values, overshooting rational value
would necessarily lead to a corrective movement back toward rational
value. This correction would not be random meandering but rather a pur-
338 METHODOLOGICAL, PSYCHOLOGICAL, PHILOSOPHICAL, STATISTICAL FOUNDATIONS
Price
Time
Bullish News Event
Rational
Price
FIGURE 7.3
Efﬁcient market response to bullish news.
--- page 337 ---

poseful movement, as if the price were being magnetically drawn to the
rational level. Such a movement would be, to some degree, predictable.
Because EMH denies predictability, it must also deny the possibility of
overreactions to news. A hypothetical overreaction to bullish news and a
subsequent systematic movement back to rational levels is illustrated in
Figure 7.4.
By the same logic, EMH must also deny the possibility of underreaction to news, where prices move less than the news justiﬁes. In this case, a
systematic price movement would also develop as prices continued to
trend (drift) toward the new rational level implied by the news. Underreaction to bullish and bearish news events and the resultant nonrandom
movement toward rational value are illustrated in Figure 7.5.
Evidence supporting EMH’s prediction that overreactions and underreactions do not occur is presented in the event studies of Eugene Fama.18
He examined all types of corporate news events such as earnings and dividend announcements, takeovers, mergers, and so forth and found that after an initial, almost instantaneous, nonexploitable price movement
triggered by the news, there was no additional movement. These observations are consistent with EMH’s prediction that the markets quickly and
accurately discount news events.19
A second prediction of EMH is that prices should change only when
news arrives. It follows then, that prices should not change dramatically
in the absence of news or in response to noninformative events.20 These
Theories of Nonrandom Price Motion
339
Price
Time
Bullish News Event
Rational
Price
Overreaction
Nonrandom Price Movement Back to Rational Price Level
FIGURE 7.4
Overreaction to bullish news (implies nonrandom price movements).
--- page 338 ---

two predictions suggest yet a third that is most crucial to TA. EMH implies that stale information, information already in the public domain,
should have no predictive power and be of no value in making investment proﬁts. Clearly, all information used by TA qualiﬁes as stale. Thus,
EMH predicts that all TA methods should fail. If this were to be con-
ﬁrmed, it’s lights out for TA.
The prediction that all stale information strategies should have no
predictive power seems cut and dried until one tries to test it. Recall,
EMH says an investment strategy based on stale information should not
be able to generate excess proﬁts after risk adjustment. So the mere fact
that a strategy based on stale information makes gains is not sufﬁcient to
rebut EMH. To contradict EMH, it must be demonstrated that the gains
are excessive after adjusting for the strategy’s risk.
The notion of judging investment strategies on the basis of riskadjusted returns is entirely reasonable. For example, if a strategy makes
20 percent per year and the benchmark makes 10 percent, but the strategy
exposes the investor to three times the risk, the strategy has not beaten
the index after risk adjustment. The question is: How does one deﬁne and
quantify risk?
Quantifying risk requires a risk model. The most well known is the
capital asset pricing model21 (CAPM), which explains systematic differences in the returns of securities in terms of a single risk factor, the security’s relative volatility. This is to say, the risk of a stock is quantiﬁed by its
340 METHODOLOGICAL, PSYCHOLOGICAL, PHILOSOPHICAL, STATISTICAL FOUNDATIONS
Price
Time
Positive News
Negative News
Trend: A Gradual Adjustment to New
Rational Price Level
Rational
Price
FIGURE 7.5
Underreaction to news can explain nonrandom trends.
--- page 339 ---

volatility relative to the volatility of the market as a whole. Thus, if a stock
is twice as volatile as the market index, its returns should be twice that of
the market. Such a stock is said to earn excess returns when it earns more
than twice the market return. This approach works well when measuring
the risk of a single stock or a portfolio of long stock positions. However,
CAPM cannot quantify the risk exposures of more complex strategies. In
response to this limitation, capital market theorists have proposed other
risk models. One of the best known is APT (arbitrage pricing theory),
which attributes risk to several independent risk factors.22
However, EMH advocates have tacitly given themselves the liberty of
cooking up new risk factors whenever they wish. This makes it nearly impossible to refute their claim that stale information strategies cannot
beat the market. For, it is always possible to propose a new risk model
that explains away a strategy’s excess returns as compensation for risk.
As explained in Chapter 3, this is not a scientiﬁc sin if the risk factor(s)
were identiﬁed before the stale information strategy earning excess returns was discovered. However, proposing a new risk factor(s) after a
market-beating strategy has been discovered is nothing more than an ad
hoc hypothesis. This is an explanation cooked up after the fact for the
speciﬁc purpose of immunizing a theory, in this case EMH, from falsiﬁcation. This practice is frowned upon in science for good reason. Also, as
discussed in Chapter 3, the information content of a scientiﬁc theory is
roughly equivalent to the opportunities it presents for falsiﬁcation. The
unbridled ability to explain away any and all dissonant evidence effectively drains the theory of its information content. Thus, the freedom to
concoct new risk factors to explain each and every investment strategy
that beats the market with stale information effectively reduces EMH to a
meaningless theory.
The evidence conﬁrming the weak form of EMH, which states that
stale prices and indicators derived from them—such as price momentum—are without value, is based on auto-correlation studies. They measure the degree to which price changes are linearly correlated with prior
changes, at various lag intervals.23 These studies have conﬁrmed that price
changes (i.e., returns) are indeed linearly independent. This means that a
linear function of current and past returns cannot be used to predict future returns.24 Based on these ﬁndings, it was concluded by EMH advocates, that security returns are an unpredictable random walk.
However, autocorrelation studies are relatively weak tests in the
sense that they can only detect linear dependencies. Searching for linear structure is merely one way to determine if a time series is behaving
in a nonrandom fashion. Edgar Peters25 and Andrew Lo and A. Craig
MacKinlay26 have shown that alternative data analysis methods indicate
that ﬁnancial market time series do not behave like random walks. For
Theories of Nonrandom Price Motion
341
--- page 340 ---

example, the test statistic used by Lo and McKinlay, called the variance
ratio, can detect more complex (nonlinear) nonrandom behaviors that
would be invisible autocorrelation studies.
CHALLENGING EMH
A good theory is consistent in two ways. Its logic is internally consistent
and it is consistent with observed evidence. Thus a theory can be challenged either by showing that it contradicts itself or that it is contradicted
by evidence.
A theory is self-contradicting if it implies or predicts something that
would contradict the theory. An example was given earlier in this chapter:
I showed that a cornerstone premise of popular TA, which asserts that
price perfectly reﬂects all information, contradicts another of its central
premises, that price contains predictive information.
The Smart versus Dumb Paradox
One implication of market efﬁciency is that knowledgeable investors
should not be able to earn higher returns than investors who are less
knowledgeable. This follows from the premise that market efﬁciency
means that whatever information is known or knowable has already been
reﬂected in security prices. In an efﬁcient market, there is no competitive
advantage to being smart or disadvantage to being dumb.
However, this implication conﬂicts with another of EMH’s assumptions—that the arbitrage activities of rational investors are able to drive
prices toward rational levels. (See the heading titled “The Assumptions of
EMH” later in this chapter.) Arbitrage can only act as an enforcer of rational prices if arbitrageurs have more trading capital and, thus, greater
price-moving power than irrational, dumb investors. Having more trading
capital implies that smart arbitrageurs must have earned higher returns in
the past than less well informed (dumb) investors. Either market prices
are set by the smartest, richest participants or they are not. EMH implies
both. Paradoxical, isn’t it!
The Cost of Information Paradox
Another logical inconsistency of EMH has to do with the cost of information. It is reasonable to assume that it costs time, money, and intelligence
to gather information and process it into useful investing strategies. At the
same time EMH contends that such information cannot earn incremental
342 METHODOLOGICAL, PSYCHOLOGICAL, PHILOSOPHICAL, STATISTICAL FOUNDATIONS
--- page 341 ---

returns for investors who incur these costs. Remember, EMH contends
that information is instantly reﬂected in prices. This implies that no matter how wide or deep the research effort, whatever is discovered will be of
no value.
However, if EMH is correct that there is no payoff for information
gathering and processing, then investors would lack the motivation to
incur the costs of doing so. With no one to dig out the information and
act on it, it would not get reﬂected in price. In other words, if it is costly
to make markets informationally efﬁcient, investors would be motivated to do it only if they were compensated with excess risk-adjusted
returns. Thus the contradiction—EMH requires that information seekers be compensated for their efforts and simultaneously denies that
they will be.
This paradox is argued persuasively by Grossman and Stiglitz in
their article “On the Impossibility of Informationally Efﬁcient Markets.”27
They contend that inefﬁciencies are necessary to motivate rational investors to engage in information gathering and processing. The returns
they earn from the market’s pricing errors are compensation for their efforts, which, in turn, have the effect of moving prices toward rational levels. The gains of these rational investors are ﬁnanced by the losses of
noise traders and liquidity traders. Noise traders are investors who buy
and sell based on signals that they think are informative but that are not.
Rational investors also earn proﬁts from the losses of investors who trade
to increase their cash reserves (liquidity traders). One way for the rational
investor to gain would be if there were a delay between the time information is discovered and the time it is reﬂected in prices, but EMH denies the
possibility of gradual price adjustments. This is yet another logical inconsistency of EMH.
A similar logic applies to the costs of acting on information (e.g., commissions, slippage, bid-asked spreads). Unless investors were compensated for incurring trading costs there would be no point to their trading
activities, which are required by EMH to move the price to its rational
level. The bottom line is that any factor that limits trading—costs to trade,
costs to generate information, the rule that impairs short-selling, and so
forth—limits the ability of the market to attain efﬁciency. It simply does
not hold logically that there would be no compensation to those engaged
in trading.
The Assumptions of EMH
To appreciate the arguments made by EMH’s critics, it is necessary to
understand that EMH rests on three progressively weaker assumptions:
(1) investors are rational, (2) investors’ pricing errors are random, and
Theories of Nonrandom Price Motion
343
--- page 342 ---

(3) there are always rational arbitrage investors to catch any pricing errors. Let’s examine each of these in a bit more detail.
First is EMH’s contention that investors are, by and large, rational. To
recap, rational investors, in aggregate, are purported to value securities
correctly. This means prices will reﬂect, as accurately as possible, the present discounted value of a security’s future cash ﬂows and risk characteristics. As rational investors learn new information, they respond quickly,
bidding up prices when news is good and letting the price fall when news
is bad. As a consequence, security prices adjust, almost instantly, to new
information.28
Even if this assumption were incorrect, EMH advocates still insist
that prices adjust quickly to rational levels anyway because of their second assumption: The valuation mistakes of individual investors are uncorrelated. This means that if one investor erroneously values a security too
high, that error will be offset by another investor’s error of valuing it too
low. Taken in aggregate, these valuation errors are self-canceling and have
an average value of zero. That is to say pricing errors are unbiased. This is
presumed to be true because the error-prone investors are likely to be using different, though useless, investment strategies. Therefore, their actions should be uncorrelated. To put it bluntly, as one foolish investor gets
an uninformative signal to buy, another investment fool is equally likely to
get an uninformative signal to sell. In effect they wind up trading with
each other, leaving prices very close to rational levels.
Moreover, even if this second assumption fails to keep prices at rational levels, EMH invokes yet a third assumption. That is, if the valuation
mistakes of irrational investors turn out to be biased (i.e., have an average value that is greater than or less than zero), arbitrage investors will
come to the rescue. They will notice that prices have systematically diverged from rational values. The arbitrageurs will buy when prices are
too low or sell when they are too high, thus forcing prices back to where
they should be.
In the EMH world, arbitrage is as close as it gets to a free lunch. An arbitrage transaction incurs no risk, requires no capital, and earns a guaranteed return. As envisioned by efﬁcient market advocates, an arbitrage
trade goes something like this: Consider two ﬁnancial assets, stocks X and
Y, which sell at equal prices and which are equally risky. However, they
have different expected future returns. Obviously, one of the two assets is
improperly priced. If asset X has a higher future return, then to take advantage of the mispricing, arbitrageurs would buy asset X while short-selling Y.
With the activities of like-minded arbitrageurs, the price of each stock will
converge to its proper fundamental value.29 Market efﬁciency attained in
this manner assumes there are always arbitrageurs ready, willing, and able
to jump on these opportunities. The better ones become very wealthy,
344 METHODOLOGICAL, PSYCHOLOGICAL, PHILOSOPHICAL, STATISTICAL FOUNDATIONS
--- page 343 ---

thereby enhancing their ability to drive prices to proper levels, while the
irrational investors eventually go broke losing their ability to push prices
away from equilibrium levels. The uninformed, irrational investors are driven out of the market the way a weak species is driven from an ecosystem, while the rational, well-informed arbitrageurs thrive.
Flaws in EMH Assumptions
This section considers each of the assumptions of EMH and how they
miss the mark.
Investors Are Rational.
Investors do not appear to be as rational as
EMH assumes. Many investors react to irrelevant information, what noted
economist Fischer Black calls “noise signals.”30 Though they think they
are acting intelligently, these investors can expect to earn the same return
as an investor who buys and sells based on a coin ﬂip. Investors who follow the advice of ﬁnancial gurus who base their advice on noise signals
are noise traders by proxy.
In fact, investors are guilty of numerous departures from rationality.
For example, they fail to diversify, they trade too actively, they increase
their tax liabilities by selling appreciated stocks but hold onto losing positions, and they trade mutual funds with high fees. Moreover, their failures
are recurring. “Investors’ deviations from the maxims of economic rationality turn out to be highly pervasive and systematic.”31 These departures
from rationality can be classiﬁed into three areas: inaccurate risk assessments, poor probability judgments, and irrational decision framing. I discuss each of these in turn.
Investors typically do not assess risks in conformity with the normative ideal put forward by Neumann and Morgenstern, known as “expected
utility theory.” In a perfectly rational world, an individual faced with
choosing among several options selects the one with the highest expected
value. The expected value of a particular choice is equal to a sum of products, where each product is the probability of each possible outcome multiplied by the value or utility of that outcome to the decision maker. The
problem is people do not actually behave this way. Research has shown
that investors make numerous systematic errors when assessing risks and
making choices.
These mistakes have been incorporated into a framework called
Prospect Theory, which was proposed by Kahneman and Tversky (1979).32
It explains how people actually make decisions under conditions of uncertainty. For example, it explains that investors hold onto losing stocks but
sell proﬁtable positions to avoid the psychic pain of realizing a loss. It also
explains why investors overvalue low-probability long-shot speculations.
Theories of Nonrandom Price Motion
345
