# INVESTMENT VALUATION TOOLS AND TECHNIQUES FOR DETERMINING -- Aswath Damodaran -- Wiley finance series, 3rd ed_, Hoboken, N_J, New Jersey, -- John -- isbn13 9781118011522 -- f84d1622bdc2de526da0dda803c52830 -- Anna’s.pdf — pages 77–96

--- page 77 ---

CHAPTER 4
The Basics of Risk
W
hen valuing assets and ﬁrms, we need to use discount rates that reﬂect the riskiness of the cash ﬂows. In particular, the cost of debt has to incorporate a default spread for the default risk in the debt, and the cost of equity has to include a
risk premium for equity risk. But how do we measure default and equity risk?
More importantly, how do we come up with the default and equity risk premiums?
This chapter lays the foundations for analyzing risk in valuation. It presents
alternative models for measuring risk and converting these risk measures into acceptable hurdle rates. It begins with a discussion of equity risk and presents the
analysis in three steps. In the ﬁrst step, risk is deﬁned in statistical terms to be the
variance in actual returns around an expected return. The greater this variance,
the more risky an investment is perceived to be. The next step, the central one, is
to decompose this risk into risk that can be diversiﬁed away by investors and risk
that cannot. The third step looks at how different risk and return models in ﬁ-
nance attempt to measure this nondiversiﬁable risk. It compares the most widely
used model, the capital asset pricing model (CAPM), with other models and explains how and why they diverge in their measures of risk and the implications for
the equity risk premium.
The ﬁnal part of this chapter considers default risk and how it is measured by
ratings agencies. By the end of the chapter, we should have a way of estimating the
equity risk and default risk for any ﬁrm.
WHAT IS RISK?
Risk, for most of us, refers to the likelihood that in life’s games of chance we will
receive an outcome that we will not like. For instance, the risk of driving a car too
fast is getting a speeding ticket or, worse still, getting into an accident. Merriam-
Webster’s Collegiate Dictionary, in fact, deﬁnes the verb to risk as “to expose to
hazard or danger.” Thus risk is perceived almost entirely in negative terms.
In ﬁnance, our deﬁnition of risk is both different and broader. Risk, as we see
it, refers to the likelihood that we will receive a return on an investment that is
different from the return we expect to make. Thus, risk includes not only the bad
outcomes (returns that are lower than expected), but also good outcomes (returns
that are higher than expected). In fact, we can refer to the former as downside
risk and the latter as upside risk, but we consider both when measuring risk. In
fact, the spirit of our deﬁnition of risk in ﬁnance is captured best by the Chinese
symbols for risk:
58
--- page 78 ---

Loosely deﬁned, the ﬁrst symbol is the symbol for “danger,” while the second is the
symbol for “opportunity,” making risk a mix of danger and opportunity. It illustrates very clearly the trade-off that every investor and business has to make—
between the higher rewards that come with the opportunity and the higher risk that
has to be borne as a consequence of the danger.
Much of this chapter can be viewed as an attempt to come up with a model that
best measures the danger in any investment, and then attempts to convert this into
the opportunity that we would need to compensate for the danger. In ﬁnance terms,
we term the danger to be “risk” and the opportunity to be “expected return.”
What makes the measurement of risk and expected return so challenging is that
it can vary depending on whose perspective we adopt. When analyzing the risk of a
ﬁrm, for instance, we can measure it from the viewpoint of the ﬁrm’s managers. Alternatively, we can argue that the ﬁrm’s equity is owned by its stockholders, and
that it is their perspective on risk that should matter. A ﬁrm’s stockholders, many of
whom hold the stock as one investment in a larger portfolio, might perceive the risk
in the ﬁrm very differently from the ﬁrm’s managers, who might have the bulk of
their capital, human and ﬁnancial, invested in the ﬁrm.
We argue that risk in an investment has to be perceived through the eyes of investors in the ﬁrm. Since ﬁrms often have thousands of investors, often with very
different perspectives, it can be asserted that risk has to be measured from the perspective of not just any investor in the stock, but of the marginal investor, deﬁned
to be the investor most likely to be trading on the stock at any given point in time.
The objective in valuation is to measure the value of an asset to those who will be
pricing it. If we want to stay true to this objective, we have to consider the viewpoint of those who set the stock prices, and they are the marginal investors.
EQUITY RISK AND EXPECTED RETURN
To demonstrate how risk is viewed in ﬁnance, risk analysis is presented here in
three steps: ﬁrst, deﬁning risk in terms of the distribution of actual returns around
an expected return; second, differentiating between risk that is speciﬁc to one or a
few investments and risk that affects a much wider cross section of investments (in
a market where the marginal investor is well diversiﬁed, it is only the latter risk,
called market risk, that will be rewarded); and third, alternative models for measuring this market risk and the expected returns that go with it.
Defining Risk
Investors who buy an asset expect to earn returns over the time horizon that they
hold the asset. Their actual returns over this holding period may be very different
from the expected returns, and it is this difference between actual and expected
returns that is a source of risk. For example, assume that you are an investor with
a one-year time horizon buying a one-year Treasury bill (or any other default-free
Equity Risk and Expected Return
59
--- page 79 ---

one-year bond) with a 5 percent expected return. At the end of the one-year holding period, the actual return on this investment will be 5 percent, which is equal
to the expected return. The return distribution for this investment is shown in
Figure 4.1. This is a riskless investment.
To provide a contrast to the riskless investment, consider an investor who buys
stock in a ﬁrm, say Boeing. This investor, having done her research, may conclude
that she can make an expected return of 30 percent on Boeing over her one-year
holding period. The actual return over this period will almost certainly not be equal
to 30 percent; it might be much greater or much lower. The distribution of returns
on this investment is illustrated in Figure 4.2.
In addition to the expected return, an investor now has to consider the following.
First, note that the actual returns, in this case, are different from the expected return.
The spread of the actual returns around the expected return is measured by the variance or standard deviation of the distribution; the greater the deviation of the actual
returns from the expected return, the greater the variance. Second, the bias toward
positive or negative returns is represented by the skewness of the distribution. The
distribution in Figure 4.2 is positively skewed, since there is a higher probability of
large positive returns than large negative returns. Third, the shape of the tails of the
distribution is measured by the kurtosis of the distribution; fatter tails lead to higher
kurtosis. In investment terms, this represents the tendency of the price of this investment to jump (up or down from current levels) in either direction.
In the special case where the distribution of returns is normal, investors do not
have to worry about skewness and kurtosis, since there is no skewness (normal distributions are symmetric) and a normal distribution is deﬁned to have a kurtosis of
zero. Figure 4.3 illustrates the return distributions on two investments with symmetric returns.
60
THE BASICS OF RISK
FIGURE 4.1
Probability Distribution of Returns on a Risk-Free Investment
--- page 80 ---

Equity Risk and Expected Return
61
FIGURE 4.2
Return Distribution for Risky Investment
FIGURE 4.3
Return Distribution Comparisons
Expected Return
Low-Variance Investment
High-Variance Investment
--- page 81 ---

When return distributions are normal, the characteristics of any investment can
be measured with two variables—the expected return, which represents the opportunity in the investment, and the standard deviation or variance, which represents
the danger. In this scenario, a rational investor, faced with a choice between two investments with the same standard deviation but different expected returns, will
always pick the one with the higher expected return.
In the more general case, where distributions are neither symmetric nor normal, it is still conceivable that investors will choose between investments on the basis of only the expected return and the variance, if they possess utility functions that
allow them to do so.1 It is far more likely, however, that they prefer positive skewed
distributions to negatively skewed ones, and distributions with a lower likelihood
of jumps (lower kurtosis) over those with a higher likelihood of jumps (higher kurtosis). In this world, investors will trade off the good (higher expected returns and
more positive skewness) against the bad (higher variance and kurtosis) in making
investments.
In closing, it should be noted that the expected returns and variances that we
run into in practice are almost always estimated using past returns rather than future returns. The assumption made when using historical variances is that past return distributions are good indicators of future return distributions. When this
assumption is violated, as is the case when the asset’s characteristics have changed
signiﬁcantly over time, the historical estimates may not be good measures of risk.
Diversifiable and Nondiversifiable Risk
Although there are many reasons why actual returns may differ from expected returns, we can group the reasons into two categories: ﬁrm-speciﬁc and marketwide.
The risks that arise from ﬁrm-speciﬁc actions affect one or a few investments, while
the risks arising from marketwide reasons affect many or all investments. This distinction is critical to the way we assess risk in ﬁnance.
Components of Risk
When an investor buys stock or takes an equity position in a ﬁrm,
he or she is exposed to many risks. Some risk may affect only one or a few ﬁrms, and
this risk is categorized as ﬁrm-speciﬁc risk. Within this category, we would consider a
wide range of risks, starting with the risk that a ﬁrm may have misjudged the demand
for a product from its customers; we call this project risk. For instance, consider
62
THE BASICS OF RISK
1A utility function is a way of summarizing investor preferences into a generic term called
“utility” on the basis of some choice variables. In this case, for instance, the investors’ utility
or satisfaction is stated as a function of wealth. By doing so, we effectively can answer questions such as, Will investors be twice as happy if they have twice as much wealth? Does each
marginal increase in wealth lead to less additional utility than the prior marginal increase? In
one speciﬁc form of this function, the quadratic utility function, the entire utility of an investor can be compressed into the expected wealth measure and the standard deviation in
that wealth.
optvar.xls: This is a dataset on the Web that summarizes standard deviations and
variances of stocks in various sectors in the United States.
--- page 82 ---

Boeing’s investment in a Super Jumbo jet. This investment is based on the assumption
that airlines want a larger airplane and are willing to pay a high price for it. If Boeing
has misjudged this demand, it will clearly have an impact on Boeing’s earnings and
value, but it should not have a signiﬁcant effect on other ﬁrms in the market. The risk
could also arise from competitors proving to be stronger or weaker than anticipated,
called competitive risk. For instance, assume that Boeing and Airbus are competing for
an order from Qantas, the Australian airline. The possibility that Airbus may win the
bid is a potential source of risk to Boeing and perhaps some of its suppliers, but again,
few other ﬁrms will be affected by it. Similarly, Disney recently launched magazines
aimed at teenage girls, hoping to capitalize on the success of its TV shows. Whether it
succeeds is clearly important to Disney and its competitors, but it is unlikely to have
an impact on the rest of the market. In fact, risk measures can be extended to include
risks that may affect an entire sector but are restricted to that sector; we call this sector
risk. For instance, a cut in the defense budget in the United States will adversely affect
all ﬁrms in the defense business, including Boeing, but there should be no signiﬁcant
impact on other sectors. What is common across the three risks described—project,
competitive, and sector risk—is that they affect only a small subset of ﬁrms.
There is another group of risks that is much more pervasive and affects many if
not all investments. For instance, when interest rates increase, all investments are
negatively affected, albeit to different degrees. Similarly, when the economy weakens, all ﬁrms feel the effects, though cyclical ﬁrms (such as automobiles, steel, and
housing) may feel it more. We term this risk market risk.
Finally, there are risks that fall in a gray area, depending on how many assets
they affect. For instance, when the dollar strengthens against other currencies, it
has a signiﬁcant impact on the earnings and values of ﬁrms with international
operations. If most ﬁrms in the market have signiﬁcant international operations,
it could well be categorized as market risk. If only a few do, it would be closer
to ﬁrm-speciﬁc risk. Figure 4.4 summarizes the spectrum of ﬁrm-speciﬁc and
market risks.
Equity Risk and Expected Return
63
FIGURE 4.4
Breakdown of Risk
--- page 83 ---

Why Diversification Reduces or Eliminates Firm-Specific Risk: An Intuitive Explanation
As an investor, you could invest all your portfolio in one asset. If you do so, you are
exposed to both ﬁrm-speciﬁc and market risk. If, however, you expand your portfolio
to include other assets or stocks, you are diversifying, and by doing so you can reduce
your exposure to ﬁrm-speciﬁc risk. There are two reasons why diversiﬁcation reduces
or, at the limit, eliminates ﬁrm-speciﬁc risk. The ﬁrst is that each investment in a diversiﬁed portfolio is a much smaller percentage of that portfolio than would be the case if
you were not diversiﬁed. Any action that increases or decreases the value of only that
investment or a small group of investments will have only a small impact on your
overall portfolio, whereas undiversiﬁed investors are much more exposed to changes
in the values of the investments in their portfolios. The second reason is that the effects
of ﬁrm-speciﬁc actions on the prices of individual assets in a portfolio can be either
positive or negative for each asset for any period. Thus, in very large portfolios this
risk will average out to zero and will not affect the overall value of the portfolio.
In contrast, the effects of marketwide movements are likely to be in the same
direction for most or all investments in a portfolio, though some assets may be affected more than others. For instance, other things being equal, an increase in interest rates will lower the values of most assets in a portfolio. Being more diversiﬁed
does not eliminate this risk.
A Statistical Analysis of Diversification-Reducing Risk
The effects of diversiﬁcation
on risk can be illustrated fairly dramatically by examining the effects of increasing
the number of assets in a portfolio on portfolio variance. The variance in a portfolio is partially determined by the variances of the individual assets in the portfolio
and partially by how they move together; the latter is measured statistically with a
correlation coefﬁcient or the covariance across investments in the portfolio. It is the
covariance term that provides an insight into why diversiﬁcation will reduce risk
and by how much.
Consider a portfolio of two assets. Asset A has an expected return of μA and a
variance in returns of σ2
A, while asset B has an expected return of μΒ and a variance
in returns of σ2
B. The correlation in returns between the two assets, which measures
how the assets move together, is ρAB. The expected returns and variances of a twoasset portfolio can be written as a function of these inputs and the proportion of
the portfolio going to each asset.
where wA = Proportion of the portfolio in asset A
The last term in the variance formulation is sometimes written in terms of the covariance in returns between the two assets, which is:
The savings that accrue from diversiﬁcation are a function of the correlation
coefﬁcient. Other things remaining equal, the higher the correlation in returns between the two assets, the smaller are the potential beneﬁts from diversiﬁcation. It is
σ
ρ
σ σ
AB
AB
A
B
=
64
THE BASICS OF RISK
μ
μ
μ
σ
σ
σ
ρ
σ σ
portfolio
A
A
A
B
portfolio
A
A
A
B
A
A
AB
A
B
w
w
w
w
w
w
=
+
−
=
+
−
+
−
(
)
(
)
(
)
1
1
2
1
2
2
2
2
2
--- page 84 ---

worth adding, though, that the beneﬁts of correlation exist even for positively correlated assets and are non-existent only when the correlation is equal to one.
Mean-Variance Models Measuring Market Risk
While most risk and return models in use in ﬁnance agree on the ﬁrst two steps of
the risk analysis process (i.e., that risk comes from the distribution of actual returns
around the expected return and that risk should be measured from the perspective of
a marginal investor who is well diversiﬁed), they part ways when it comes to measuring nondiversiﬁable or market risk. This section will discuss the different models
that exist in ﬁnance for measuring market risk and why they differ. It begins with
what still is the most widely used model for measuring market risk in ﬁnance—the
capital asset pricing model (CAPM)—and then discusses the alternatives to this
model that have developed over the past two decades. While the discussion will emphasize the differences, it will also look at what the models have in common.
Capital Asset Pricing Model
The risk and return model that has been in use the
longest and is still the standard for most practitioners is the capital asset pricing
model (CAPM). This section will examine the assumptions on which the model is
based and the measures of market risk that emerge from these assumptions.
Equity Risk and Expected Return
65
WHY IS THE MARGINAL INVESTOR ASSUMED TO BE DIVERSIFIED?
The argument that diversiﬁcation reduces an investor’s exposure to risk is clear
both intuitively and statistically, but risk and return models in ﬁnance go further. These models look at risk through the eyes of the investor most likely to be
trading on the investment at any point in time—the marginal investor. They argue that this investor, who sets prices for investments, is well diversiﬁed; thus,
the only risk that he or she cares about is the risk added to a diversiﬁed portfolio or market risk. This argument can be justiﬁed simply. The risk in an investment will always be perceived to be higher for an undiversiﬁed investor than for
a diversiﬁed one, since the latter does not shoulder any ﬁrm-speciﬁc risk and the
former does. If both investors have the same expectations about future earnings
and cash ﬂows on an asset, the diversiﬁed investor will be willing to pay a
higher price for that asset because of his or her perception of lower risk. Consequently, the asset, over time, will end up being held by diversiﬁed investors.
This argument is powerful, especially in markets where assets can be
traded easily and at low cost. Thus, it works well for a stock traded in developed markets, since investors can become diversiﬁed at fairly low cost. In addition, a signiﬁcant proportion of the trading in developed market stocks is
done by institutional investors, who tend to be well diversiﬁed. It becomes a
more difﬁcult argument to sustain when assets cannot be easily traded or the
costs of trading are high. In these markets, the marginal investor may well be
undiversiﬁed, and ﬁrm-speciﬁc risk may therefore continue to matter when
looking at individual investments. For instance, real estate in most countries is
still held by investors who are undiversiﬁed and have the bulk of their wealth
tied up in these investments.
--- page 85 ---

Assumptions
While diversiﬁcation reduces the exposure of investors to ﬁrm-speciﬁc risk, most investors limit their diversiﬁcation to holding only a few assets.
Even large mutual funds rarely hold more than a few hundred stocks, and many of
them hold as few as 10 to 20. There are two reasons why investors stop diversifying. One is that an investor or mutual fund manager can obtain most of the beneﬁts
of diversiﬁcation from a relatively small portfolio, because the marginal beneﬁts of
diversiﬁcation become smaller as the portfolio gets more diversiﬁed. Consequently,
these beneﬁts may not cover the marginal costs of diversiﬁcation, which include
transactions and monitoring costs. Another reason for limiting diversiﬁcation is
that many investors (and funds) believe they can ﬁnd undervalued assets and thus
choose not to hold those assets that they believe to be fairly valued or overvalued.
The capital asset pricing model assumes that there are no transaction costs, all
assets are traded, and investments are inﬁnitely divisible (i.e., you can buy any fraction of a unit of the asset). It also assumes that everyone has access to the same information and that investors therefore cannot ﬁnd underor overvalued assets in
the marketplace. By making these assumptions, it allows investors to keep diversifying without additional cost. At the limit, their portfolios will not only include
every traded asset in the market but these assets will be held in proportion to their
market value.
The fact that this portfolio includes all traded assets in the market is the reason
it is called the market portfolio, which should not be a surprising result, given the
beneﬁts of diversiﬁcation and the absence of transaction costs in the capital asset
pricing model. If diversiﬁcation reduces exposure to ﬁrm-speciﬁc risk and there are
no costs associated with adding more assets to the portfolio, the logical limit to diversiﬁcation is to hold a small proportion of every traded asset in the economy. If
this seems abstract, consider the market portfolio to be an extremely well diversi-
ﬁed mutual fund that holds stocks and real assets. In the CAPM, all investors will
hold combinations of the riskier asset and that supremely diversiﬁed mutual fund.2
Investor Portfolios in the CAPM
If every investor in the market holds the identical market portfolio, how exactly do investors reﬂect their risk aversion in their investments? In the capital asset pricing model, investors adjust for their risk
preferences in their allocation decision, where they decide how much to invest in a
riskless asset and how much in the market portfolio. Investors who are risk averse
might choose to put much or even all of their wealth in the riskless asset. Investors
who want to take more risk will invest the bulk or even all of their wealth in the
market portfolio. Investors who invest all their wealth in the market portfolio and
are desirous of taking on still more risk would do so by borrowing at the riskless
rate and investing in the same market portfolio as everyone else.
These results are predicated on two additional assumptions. First, there exists a
riskless asset, where the expected returns are known with certainty. Second, investors can lend and borrow at the riskless rate to arrive at their optimal allocations. While lending at the riskless rate can be accomplished fairly simply by buying
Treasury bills or bonds, borrowing at the riskless rate might be more difﬁcult for
66
THE BASICS OF RISK
2The signiﬁcance of introducing the riskless asset into the choice mix and the implications for
portfolio choice were ﬁrst noted in Sharpe (1964) and Lintner (1965). Hence, the model is
sometimes called the Sharpe-Lintner model.
--- page 86 ---

individuals to do. There are variations of the CAPM that allow these assumptions
to be relaxed and still arrive at conclusions that are consistent with the model.
Measuring the Market Risk of an Individual Asset
The risk of any asset to an investor is the risk added by that asset to the investor’s overall portfolio. In the CAPM
world, where all investors hold the market portfolio, the risk to an investor of an individual asset will be the risk that this asset adds to the market portfolio. Intuitively,
if an asset moves independently of the market portfolio, it will not add much risk to
the market portfolio. In other words, most of the risk in this asset is ﬁrm-speciﬁc
and can be diversiﬁed away. In contrast, if an asset tends to move up when the market portfolio moves up and down when it moves down, it will add risk to the market
portfolio. This asset has more market risk and less ﬁrm-speciﬁc risk. Statistically,
this added risk is measured by the covariance of the asset with the market portfolio.
Measuring the Nondiversiﬁable Risk
In a world in which investors hold a combination of only two assets—the riskless asset and the market portfolio—the risk of
any individual asset will be measured relative to the market portfolio. In particular,
the risk of any asset will be the risk it adds to the market portfolio. To arrive at the
appropriate measure of this added risk, assume that σ2
m is the variance of the market portfolio prior to the addition of the new asset and that the variance of the individual asset being added to this portfolio is σ2
i. The market value portfolio weight
on this asset is wi, and the covariance in returns between the individual asset and
the market portfolio is σim. The variance of the market portfolio prior to and after
the addition of the individual asset can then be written as:
Variance prior to asset i being added = σ2
m
Variance after asset i is added = σ2
m′ = wi
2σ2
i + (1 – wi)2σ2
m + 2wi(1 – wi)σim
The market value weight on any individual asset in the market portfolio should
be small, since the market portfolio includes all traded assets in the economy. Consequently, the ﬁrst term in the equation should approach zero, and the second term
should approach σ2
m′ leaving the third term (σim′ the covariance) as the measure of
the risk added by asset i.
Standardizing Covariances
The covariance is a percentage value, and it is difﬁ-
cult to pass judgment on the relative risk of an investment by looking at this value.
In other words, knowing that the covariance of Boeing with the market portfolio
is 55 percent does not provide us a clue as to whether Boeing is riskier or safer
than the average asset. We therefore standardize the risk measure by dividing the
covariance of each asset with the market portfolio by the variance of the market
portfolio. This yields a risk measure called the beta of the asset:
Since the covariance of the market portfolio with itself is its variance, the beta
of the market portfolio (and, by extension, the average asset in it) is 1. Assets that
Beta of asset i
Covariance of asset i with market portfolio
Variance of the market portfolio
im
m
=
=
σ
σ2
Equity Risk and Expected Return
67
--- page 87 ---

are riskier than average (using this measure of risk) will have betas that exceed 1,
and assets that are safer than average will have betas that are lower than 1. The
riskless asset will have a beta of zero.
Getting Expected Returns
The fact that every investor holds some combination of
the riskless asset and the market portfolio leads to the next conclusion, which is
that the expected return on an asset is linearly related to the beta of the asset. In
particular, the expected return on an asset can be written as a function of the riskfree rate and the beta of that asset:
E(Ri) = Rf + βi[E(Rm) – Rf]
where E(Ri) = Expected return on asset i
Rf = Risk-free rate
E(Rm) = Expected return on market portfolio
βi = Beta of asset i
To use the capital asset pricing model, we need three inputs. While the next
chapter looks at the estimation process in far more detail, each of these inputs is estimated as follows:
■The riskless asset is deﬁned to be an asset for which the investor knows the expected return with certainty for the time horizon of the analysis.
■The risk premium is the premium demanded by investors for investing in the
market portfolio, which includes all risky assets in the market, instead of investing in a riskless asset.
■The beta, deﬁned as the covariance of the asset divided by the market portfolio,
measures the risk added by an investment to the market portfolio.
In summary, in the capital asset pricing model all the market risk is captured in
one beta measured relative to a market portfolio, which at least in theory should include all traded assets in the marketplace held in proportion to their market value.
Arbitrage Pricing Model
The restrictive assumptions on transaction costs and private information in the capital asset pricing model, and the model’s dependence on
the market portfolio, have long been viewed with skepticism by both academics
and practitioners. Ross (1976) suggested an alternative model for measuring risk
called the arbitrage pricing model (APM).
Assumptions
If investors can invest risklessly and earn more than the riskless rate,
they have found an arbitrage opportunity. The premise of the arbitrage pricing
model is that investors take advantage of such arbitrage opportunities, and in the
process eliminate them. If two portfolios have the same exposure to risk but offer
different expected returns, investors will buy the portfolio that has the higher expected returns and sell the portfolio with the lower expected returns, and earn the
difference as a riskless proﬁt. To prevent this arbitrage from occurring, the two
portfolios have to earn the same expected return.
Like the capital asset pricing model, the arbitrage pricing model begins by
breaking risk down into ﬁrm-speciﬁc and market risk components. As in the capital
68
THE BASICS OF RISK
--- page 88 ---

asset pricing model, ﬁrm-speciﬁc risk covers information that affects primarily
the ﬁrm. Market risk affects many or all ﬁrms and would include unanticipated
changes in a number of economic variables, including gross national product,
inﬂation, and interest rates. Incorporating both types of risk into a return model,
we get:
R = E(R) + m + ε
where R is the actual return, E(R) is the expected return, m is the marketwide component of unanticipated risk, and ε is the ﬁrm-speciﬁc component. Thus, the actual
return can be different from the expected return, because of either market risk or
ﬁrm-speciﬁc actions.
Sources of Marketwide Risk
While both the capital asset pricing model and the
arbitrage pricing model make a distinction between ﬁrm-speciﬁc and marketwide
risk, they measure market risk differently. The CAPM assumes that market risk is
captured in the market portfolio, whereas the arbitrage pricing model allows for
multiple sources of marketwide risk and measures the sensitivity of investments to
changes in each source. In general, the market component of unanticipated returns
can be decomposed into economic factors:
R = E(R) + m + ε
= R + (β1F1 + β2F2 + . . . + βnFn) + ε
where βj = Sensitivity of investment to unanticipated changes in market risk factor j
Fj = Unanticipated changes in market risk factor j
Note that the measure of an investment’s sensitivity to any macroeconomic (or
market) factor takes the form of a beta, called a factor beta. In fact, this beta has
many of the same properties as the market beta in the CAPM.
Effects of Diversiﬁcation
The beneﬁts of diversiﬁcation were discussed earlier,
in the context of the breakdown of risk into market and ﬁrm-speciﬁc risk. The
primary point of that discussion was that diversiﬁcation eliminates ﬁrm-speciﬁc
risk. The arbitrage pricing model uses the same argument and concludes that the
return on a portfolio will not have a ﬁrm-speciﬁc component of unanticipated
returns. The return on a portfolio can be written as the sum of two weighted averages—that of the anticipated returns in the portfolio and that of the market
factors:
Rp = (w1R1 + w2R2 + . . . + wnRn) + (w1β1,1 + w2β1,2 + . . . + wnβ1, n)F1 +
(w1β2,1 + w2β2,2 + . . . + wnβ2,n)F2 . . .
where wj = Portfolio weight on asset j (where there are n assets)
Rj = Expected return on asset j
βi,j = Beta on factor i for asset j
Expected Returns and Betas
The ﬁnal step in this process is estimating an expected return as a function of the betas just speciﬁed. To do this, we should ﬁrst
note that the beta of a portfolio is the weighted average of the betas of the assets in
Equity Risk and Expected Return
69
--- page 89 ---

the portfolio. This property, in conjunction with the absence of arbitrage, leads to
the conclusion that expected returns should be linearly related to betas. To see why,
assume that there is only one factor and three portfolios. Portfolio A has a beta of
2.0 and an expected return of 20 percent; portfolio B has a beta of 1.0 and an expected return of 12 percent; and portfolio C has a beta of 1.5 and an expected return of 14 percent. Note that investors can put half of their wealth in portfolio A
and half in portfolio B and end up with portfolios with a beta of 1.5 and an expected return of 16 percent. Consequently no investor will choose to hold portfolio
C until the prices of assets in that portfolio drop and the expected return increases
to 16 percent. By the same rationale, the expected returns of every portfolio should
be a linear function of the beta. If they were not, we could combine two other portfolios, one with a higher beta and one with a lower beta, to earn a higher return
than the portfolio in question, creating an opportunity for arbitrage. This argument
can be extended to multiple factors with the same results. Therefore, the expected
return on an asset can be written as:
E(R) = Rf + β1[E(R1) – Rf] + β2[E(R2) – Rf] . . . + βK[E(RK) – Rf]
where
Rf = Expected return on a zero-beta portfolio
E(Rj) = Expected return on a portfolio with a factor beta of 1 for factor j,
and zero for all other factors (where j = 1, 2, . . . , K factors)
The terms in the brackets can be considered to be risk premiums for each of the factors in the model.
The capital asset pricing model can be considered to be a special case of the arbitrage pricing model, where there is only one economic factor driving marketwide
returns, and the market portfolio is the factor.
E(R) = Rf + βm[E(Rm) – Rf]
The APM in Practice
The arbitrage pricing model requires estimates of each of
the factor betas and factor risk premiums in addition to the riskless rate. In practice, these are usually estimated using historical data on asset returns and a factor
analysis. Intuitively, in a factor analysis, we examine the historical data looking for
common patterns that affect broad groups of assets (rather than just one sector or a
few assets). A factor analysis provides two output measures:
1. It speciﬁes the number of common factors that affected the historical return
data.
2. It measures the beta of each investment relative to each of the common factors
and provides an estimate of the actual risk premium earned by each factor.
The factor analysis does not, however, identify the factors in economic terms.
In summary, in the arbitrage pricing model the market risk is measured relative to
multiple unspeciﬁed macroeconomic variables, with the sensitivity of the investment relative to each factor being measured by a beta. The number of factors, the
factor betas, and the factor risk premiums can all be estimated using the factor
analysis.
70
THE BASICS OF RISK
--- page 90 ---

Multifactor Models for Risk and Return
The arbitrage pricing model’s failure to
identify the factors speciﬁcally in the model may be a statistical strength, but it is an
intuitive weakness. The solution seems simple: Replace the unidentiﬁed statistical
factors with speciﬁc economic factors, and the resultant model should have an economic basis while still retaining much of the strength of the arbitrage pricing
model. That is precisely what multifactor models try to do.
Deriving a Multifactor Model
Multifactor models generally are determined by historical data rather than by economic modeling. Once the number of factors has been
identiﬁed in the arbitrage pricing model, their behavior over time can be extracted
from the data. The behavior of the unnamed factors over time can then be compared
to the behavior of macroeconomic variables over that same period, to see whether
any of the variables is correlated, over time, with the identiﬁed factors.
For instance, Chen, Roll, and Ross (1986) suggest that the following macroeconomic variables are highly correlated with the factors that come out of factor
analysis: industrial production, changes in default premium, shifts in the term
structure, unanticipated inﬂation, and changes in the real rate of return. These variables can then be correlated with returns to come up with a model of expected returns, with ﬁrm-speciﬁc betas calculated relative to each variable.
E(R) = Rf + βGNP [E(RGNP) – Rf] + βI[E(RI) – Rf] . . . + βδ[E(Rδ) – Rf]
where
βGNP = Beta relative to changes in industrial production
E(RGNP) = Expected return on a portfolio with a beta of one on the
industrial production factor and zero on all other factors
βI = Beta relative to changes in inﬂation
E(RI) = Expected return on a portfolio with a beta of one on the inﬂation
factor and zero on all other factors
The costs of going from the arbitrage pricing model to a macroeconomic multifactor model can be traced directly to the errors that can be made in identifying the
factors. The economic factors in the model can change over time, as will the risk
premium associated with each one. For instance, oil price changes were a signiﬁ-
cant economic factor driving expected returns in the 1970s but are not as signiﬁ-
cant in other time periods. Using the wrong factor or missing a signiﬁcant factor in
a multifactor model can lead to inferior estimates of expected return.
ALTERNATIVE MODELS FOR EQUITY RISK
The CAPM, arbitrage pricing model, and multifactor model represent attempts by
ﬁnancial economists to build risk and return models from the mean-variance base
established by Harry Markowitz (1991). There are many, though, who believe the
basis for the model is ﬂawed and that we should be looking at alternatives, and in
this section, we will look at some of them.
Different Return Distributions
From its very beginnings, the mean-variance framework has been controversial.
While there have been many who have challenged its applicability, we will consider
Alternative Models for Equity Risk
71
--- page 91 ---

these challenges in three groups. The ﬁrst group argues that stock prices, in particular, and investment returns, in general, exhibit too many large values to be drawn
from a normal distribution. They argue that the fat tails on stock price distributions lend themselves better to a class of distributions, called power law distributions, which exhibit inﬁnite variance and long periods of price dependence. The
second group takes issue with the symmetry of the normal distribution and argues
for measures that incorporate the asymmetry observed in actual return distributions into risk measures. The third group posits that distributions that allow for
price jumps are more realistic and that risk measures should consider the likelihood
and magnitude of price jumps.
Fat Tails and Power Law Distributions
Benoit Mandelbrot (1961; Mandelbrot and
Hudson, 2004), a mathematician who also did pioneering work on the behavior of
stock prices, was one of those who took issue with the use of normal and lognormal
distributions. He argued, based on his observation of stock and real asset prices,
that a power law distribution characterized them better. In a power-law distribution,
the relationship between two variables, Y and X, can be written as follows:
Y = αX
In this equation, α is a constant (constant of proportionality), and k is the power
law exponent. Mandelbrot’s key point was that the normal and log normal distributions were best suited for series that exhibited mild and well-behaved randomness,
whereas power law distributions were more suited for series that exhibited large
movements and what he termed wild randomness. Wild randomness occurs when a
single observation can affect the population in a disproportionate way; stock and
commodity prices exhibit wild randomness. Stock and commodity prices, with
their long periods of relatively small movements, punctuated by wild swings in
both directions, seem to ﬁt better into the wild randomness group.
What are the consequences for risk measures? If asset prices follow power law
distributions, the standard deviation or volatility ceases to be a good risk measure
and a good basis for computing probabilities. Assume, for instance, that the standard deviation in annual stock returns is 15 percent and that the average return is
10 percent. Using the normal distribution as the base for probability predictions,
this will imply that the stock returns will exceed 40 percent (average plus two standard deviations) only once every 44 years and 55 percent only (average plus three
standard deviations) only once every 740 years. In fact, stock returns will be
greater than 85 percent (average plus ﬁve standard deviations) only once every 3.5
million years. In reality, stock returns exceed these values far more frequently, a
ﬁnding consistent with power law distributions, where the probability of larger values declines linearly as a function of the power law exponent. As the value gets
doubled, the probability of its occurrence drops by the square of the exponent.
Thus, if the exponent in the distribution is 2, the likelihood of returns of 25 percent,
50 percent, and 100 percent can be computed as follows:
Returns will exceed 25 percent: once every 6 years.
Returns will exceed 50 percent: once every 24 years.
Returns will exceed 100 percent: once every 96 years.
72
THE BASICS OF RISK
--- page 92 ---

Note that as the returns get doubled, the likelihood increases four-fold (the square
of the exponent). As the exponent decreases, the likelihood of larger values increases;
an exponent between 0 and 2 will yield extreme values more often than a normal distribution. An exponent between 1 and 2 yields power law distributions called stable
Paretian distributions, which have inﬁnite variance. In an early study, Fama (1965) estimated the exponent for stocks to be between 1.7 and 1.9, but subsequent studies
have found that the exponent is higher in both equity and currency markets.3
In practical terms, the power law proponents argue that using measures such as
volatility (and its derivatives such as beta) underestimate the risk of large movements.
The power law exponents for assets, in their view, provide investors with more realistic risk measures for these assets. Assets with higher exponents are less risky (since
extreme values become less common) than asset with lower exponents.
Mandelbrot’s challenge to the normal distribution was more than a procedural
one. Mandelbrot’s world, in contrast to the Gaussian mean-variance one, is a world
where prices move jaggedly over time and look as though they have no pattern at a
distance, but where patterns repeat themselves, when observed closely. In the 1970s,
Mandelbrot created a branch of mathematics called fractal geometry where
processes are not described by conventional statistical or mathematical measures but
by fractals; a fractal is a geometric shape that when broken down into smaller parts
replicates that shape. To illustrate the concept, he uses the example of the coastline
that, from a distance, looks irregular and up close looks roughly the same—fractal
patterns repeat themselves. In fractal geometry, higher fractal dimensions translate
into more jagged shapes; the rugged Cornish coastline has a fractal dimension of
1.25 whereas the much smoother South African coastline has a fractal dimension
of 1.02. Using the same reasoning, stock prices that look random, when observed at
longer time intervals, start revealing self-repeating patterns, when observed over
shorter time periods. More volatile stocks score higher on measures of fractal dimension, thus making it a measure of risk. With fractal geometry, Mandelbrot was
able to explain not only the higher frequency of price jumps (relative to the normal
distribution) but also long periods where prices move in the same direction and the
resulting price bubbles.
Asymmetric Distributions
Intuitively, it should be downside risk that concerns us and
not upside risk. In other words, it is not investments that go up signiﬁcantly that
create heartburn and unease but investments that go down signiﬁcantly. The meanvariance framework, by weighting both upside volatility and downside movements
equally, does not distinguish between the two. With a normal or any other symmetric distribution, the distinction between upside and downside risk is irrelevant because the risks are equivalent. With asymmetric distributions, though, there can be a
difference between upside and downside risk. Studies of risk aversion in humans
conclude that (1) they are loss averse; that is, they weigh the pain of a loss more than
the joy of an equivalent gain and (2) they value very large positive payoffs—long
shots—far more than they should given the likelihood of these payoffs.
Alternative Models for Equity Risk
73
3In a paper in Nature (Gabaix, X., Gopikrishnan, P., Plerou, V., and Stanley, H.E., 2003, A
theory of power law distributions in ﬁnancial market ﬂuctuations, Nature 423, 267–70),
researchers looked at stock prices on 500 stocks between 1929 and 1987 and concluded that
the exponent for stock returns is roughly 3.
--- page 93 ---

In practice, return distributions for stocks and most other assets are not symmetric. Instead, asset returns exhibit fat tails (i.e, more jumps) and are more likely
to have extreme positive values than extreme negative values (simply because returns are constrained to be no less than –100 percent). As a consequence, the distribution of stock returns has a higher incidence of extreme returns (fat tails or
kurtosis) and a tilt toward very large positive returns (positive skewness). Critics of
the mean-variance approach argue that it takes too narrow a view of both rewards
and risk. In their view, a fuller return measure should consider not just the magnitude of expected returns but also the likelihood of very large positive returns or
skewness, and a more complete risk measure should incorporate both variance and
the possibility of big jumps (co-kurtosis). Note that even as these approaches deviate
from the mean-variance approach in terms of how they deﬁne risk, they stay true to
the portfolio measure of risk. In other words, it is not the possibility of large positive
payoffs (skewness) or big jumps (kurtosis) that they argue should be considered, but
only that portion of the skewness (co-skewness) and kurtosis (co-kurtosis) that is
market-related and not diversiﬁable.
Jump Process Models
The normal, power law, and asymmetric distributions that
form the basis for the models we have discussed in this section are all continuous distributions. Observing the reality that stock prices do jump, there are
some who have argued for the use of jump process distributions to derive risk
measures.
Press (1967), in one of the earliest papers that attempted to model stock price
jumps, argued that stock prices follow a combination of a continuous price distribution and a Poisson distribution, where prices jump at irregular intervals. The key
parameters of the Poisson distribution are the expected size of the price jump (μ),
the variance in this value (δ2), and the likelihood of a price jump in any speciﬁed
time period (λ), and Press estimated these values for 10 stocks. In subsequent papers, Beckers (1981) and Ball and Torous (1983) suggest ways of reﬁning these estimates. In an attempt to bridge the gap between the CAPM and jump process
models, Jarrow and Rosenfeld (1984) derive a version of the capital asset pricing
model that includes a jump component that captures the likelihood of market
jumps and an individual asset’s correlation with these jumps.
While jump process models have gained some traction in option pricing, they
have had limited success in equity markets, largely because the parameters of jump
process models are difﬁcult to estimate with any degree of precision. Thus, while
everyone agrees that stock prices jump, there is little consensus on the best way to
measure how often this happens, whether these jumps are diversiﬁable, and how
best to incorporate their effect into risk measures.
Regression or Proxy Models
The conventional models for risk and return in ﬁnance (CAPM, arbitrage pricing
model, and even multifactor models) start by making assumptions about how investors behave and how markets work to derive models that measure risk and link
those measures to expected returns. While these models have the advantage of a
foundation in economic theory, they seem to fall short in explaining differences in
returns across investments. The reasons for the failure of these models run the
74
THE BASICS OF RISK
--- page 94 ---

gamut: The assumptions made about markets are unrealistic (no transactions costs,
perfect information) and investors don’t behave rationally (and behavioral ﬁnance
research provides ample evidence of this).
With proxy models, we essentially give up on building risk and return models
from economic theory. Instead, we start with how investments are priced by markets and relate returns earned to observable variables. Rather than talk in abstractions, consider the work done by Fama and French in the early 1990s. Examining
returns earned by individual stocks from 1962 to 1990, they concluded that
CAPM betas did not explain much of the variation in these returns. They then
took a different tack and looked for company-speciﬁc variables that did a better
job of explaining return differences they pinpointed two variables—the market
capitalization of a ﬁrm and its price-to-book ratio (the ratio of market cap to accounting book value for equity). Speciﬁcally, they concluded that small market cap
stocks earned much higher annual returns than large market cap stocks and that
low price to book ratio stocks earned much higher annual returns than stocks that
traded at high price-to-book ratios. Rather than view this as evidence of market
inefﬁciency (which is what prior studies that had found the same phenomena had
done), they argued if these stocks earned higher returns over long time periods,
they must be riskier than stocks that earned lower returns. In effect, market capitalization and price-to-book ratios were better proxies for risk, according to their
reasoning, than betas. In fact, they regressed returns on stocks against the market
capitalization of a company and its price-to-book ratio to arrive at the following
regression for U.S. stocks;
Expected monthly return = 1.77% – 0.11 [ln(Market capitalization in millions)]
+ 0.35 [ln(Book/Price)]
In a pure proxy model, you could plug the market capitalization and book-to-market
ratio for any company into this regression to get expected monthly returns.
In the two decades since the Fama-French paper brought proxy models to the
fore, researchers have probed the data (which has become more detailed and voluminous over time) to ﬁnd better and additional proxies for risk. Some of the proxies are highlighted here:
■Earnings momentum. Equity research analysts will ﬁnd vindication in research that
seems to indicate that companies that have reported stronger than expected earnings growth in the past earn higher returns than the rest of the market.
■Price momentum. Chartists will smile when they read this, but researchers have
concluded that price momentum carries over into future periods. Thus, the expected returns will be higher for stocks that have outperformed markets in recent time periods and lower for stocks that have lagged.
■Liquidity. In a nod to real-world costs, there seems to be clear evidence that stocks
that are less liquid (lower trading volume, higher bid-ask spreads) earn higher returns than more liquid stocks.
While the use of pure proxy models by practitioners is rare, they have adapted
the ﬁndings for these models into their day-to-day use. Many analysts have melded
the CAPM with proxy models to create composite or melded models. For instance,
Alternative Models for Equity Risk
75
--- page 95 ---

many analysts who value small companies derive expected returns for these companies by adding a small cap premium to the CAPM expected return:
Expected return = Risk-free rate + Market beta × Equity risk premium
+ Small cap premium
The threshold for small capitalization varies across time but is generally set at
the bottom decile of publicly traded companies, and the small cap premium itself is
estimated by looking at the historical premium earned by small cap stocks over the
market. Using the Fama-French ﬁndings, the CAPM has been expanded to include
market capitalization and price-to-book ratios as additional variables, with the expected return stated as:
Expected return = Risk-free rate + Market beta × Equity risk premium
+ Size beta ∗Small cap risk premium
+ Book-to-market beta × Book-to-market premium
The size and the book-to-market betas are estimated by regressing a stock’s returns
against the size premium and book-to-market premiums over time; this is analogous to the way we get the market beta, by regressing stock returns against overall
market returns.
While the use of proxy and melded models offers a way of adjusting expected
returns to reﬂect market reality, there are three dangers in using these models.
1. Data mining. As the amount of data that we have on companies increases and
becomes more accessible, it is inevitable that we will ﬁnd more variables that are related to returns. It is also likely that most of these variables are not proxies for risk
and that the correlation is a function of the time period that we look at. In effect,
proxy models are statistical models and not economic models. Thus, there is no easy
way to separate the variables that matter from those that do not.
2. Standard error. Since proxy models come from looking at historical data, they
carry all of the burden of the noise in the data. Stock returns are extremely volatile
over time, and any historical premia that we compute (for market capitalization or any
other variable) are going to have signiﬁcant standard errors. The standard errors on
the size and book-to-market betas in the three-factor Fama-French model may be so
large that using them in practice creates almost as much noise as it adds in precision.
3.
Pricing error or risk proxy. For decades, value investors have argued that you
should invest in stocks with low PE ratios that trade at low multiples of book value and
have high dividend yields, pointing to the fact that you will earn higher returns by doing
so. (In fact, a scan of Benjamin Graham’s screens from security analysis4 for cheap companies unearths most of the proxies that you see in use today.) Proxy models incorporate
all of these variables into the expected return and thus render these assets to be fairly
priced. Using the circular logic of these models, markets are always efﬁcient because any
inefﬁciency that exists is just another risk proxy that needs to get built into the model.
A COMPARATIVE ANALYSIS OF EQUITY RISK MODELS
When faced with the choice of estimating expected returns on equity or cost of equity,
we are therefore faced with several choices, ranging from the CAPM to proxy models.
Table 4.1 summarizes the different models and presents their pluses and minuses.
76
THE BASICS OF RISK
4Graham, B., 1949, The Intelligent Investor (New York: HarperBusiness, reprinted in 2005).
--- page 96 ---

TABLE 4.1
Alternative Models for Cost of Equity
Model
Expected Return on Equity
Pluses
Minuses
The CAPM
E(R) = Rf + β‚ × ERP
Simple to
Does not explain
compute
differences in
returns across
stocks well.
APM
More nuanced
Factors are
(n factors)
breakdown of
statistical and
market risk
unnamed.
Multifactor
More intuitive
Factors are
model
than APM
unstable and
(n factors)
change over time.
Alternative
Depends on model
More realistic
Parameters for the
distributions
models are very
difﬁcult to estimate.
Proxy models
E(R) = a + b X1 + c X2
Explains
Variables in model
differences in
may not be proxies
past returns well
for risk and reﬂect
data mining.
Rf: Riskfree rate, ERP: Equity Risk Premium = E(Rm) – Rf. X1, X2: Company-speciﬁc variables.
The decision has to be based as much on theoretical considerations as it will be
on pragmatic considerations. The CAPM is the simplest of the models, insofar as it
requires only one ﬁrm-speciﬁc input (the beta), and that input can be estimated
readily from public information. To replace the CAPM with an alternative model,
whether it be from the mean variance family (arbitrage pricing model or multifactor models), alternative return process families (power, asymmetric, and jump distribution models), or proxy models, we need evidence of substantial improvement
in accuracy in future forecasts (and not just in explaining past returns).
Ultimately, the survival of the capital asset pricing model as the default model
for risk in real-world applications is a testament to both its intuitive appeal and the
failure of more complex models to deliver signiﬁcant improvement in terms of estimating expected returns. We would argue that a judicious use of the capital asset
pricing model, without an over reliance on historical data, is still the most effective
way of dealing with risk in valuation in most cases. In some sectors (commodities)
and segments (closely held companies, illiquid stocks), using other, more complete
models will be justiﬁed. We will return to the question of how improvements in estimating the inputs to the CAPM can generate far more payoff than switching to
more complicated models for cost of equity.
MODELS OF DEFAULT RISK
The risk discussed so far in this chapter relates to cash ﬂows on investments being
different from expected cash ﬂows. There are some investments, however, in which
the cash ﬂows are promised when the investment is made. This is the case, for instance, when you lend to a business or buy a corporate bond; the borrower may
Models of Default Risk
77
E R
( ) = Rf +
j =1
j=n
E Rj
(
)
Rf
βj
E R
( ) = Rf +
k =1
k=n
E Rk
(
)
Rf
βk
