# INVESTMENT VALUATION TOOLS AND TECHNIQUES FOR DETERMINING -- Aswath Damodaran -- Wiley finance series, 3rd ed_, Hoboken, N_J, New Jersey, -- John -- isbn13 9781118011522 -- f84d1622bdc2de526da0dda803c52830 -- Anna’s.pdf — pages 932–951

--- page 932 ---

Reinvestment rate = g/ROC = 2/21% = 9.52%
Adding the current cash balance ($32,007 million), subtracting out debt ($9,400 million) and dividing
by the number of shares (4,941.63 million) yields the value per share.
At its current stock price of $64.83, the stock looks slightly undervalued. However, that reﬂects the assumption that the current oil price (of $45 per barrel) is the normalized price.
Since the value per share is so dependent on the oil price, it would make more sense to allow the
oil price to vary and value the company as a function of this price, and simulations can help ﬂesh out
the numbers:
Step 1: Determine the probability distribution for the oil prices: We used historical data on oil prices,
adjusted for inﬂation, to both deﬁne the distribution and estimate its parameters. Figure 33.9
summarizes the distribution.
Note that oil prices can vary from about $8 a barrel at the minimum to more than $120 a
barrel. While we have used the current price of $45 as the mean of the distribution, we could
have inserted an oil view into the distribution by choosing a higher or lower mean value.7
Value per share =
Operating assets + Cash – Debt
Number of shares
= 32,0472 + 32007 – 9,400
4,941.63
= $69.43/share
Simulations
913
FIGURE 33.9
Oil Price Distribution—Historical data
Probability
$20.00
$40.00
$60.00
$80.00
$100.00
$120.00
$140.00
7We used thirty years of historical data on oil prices, adjusted for inﬂation, to create an empirical distribution. We
then chose the statistical distribution that seemed to provide the closest ﬁt (lognormal) and chose parameter values that yielded numbers closest to the historical data.
=
g
Operating income(1 + g)(1 − Tax rate) 1 − ROC
(Cost of capital − g)
=
= $320,472 million
2%
34,614(1.02)(1 − .38) 1 − 21%
(.0818 − .02)
Value of operating assets
--- page 933 ---

Step 2: Link the operating results to commodity price: To link the operating income to commodity
prices, we used the regression results from earlier in the illustration:
Operating income = –6,395 + 911.32 (Average oil price)       R2 = 90.2%
[2.95]   [14.59]
As we noted in the earlier section, the regression approach works well for Exxon but may
not for smaller, more volatile commodity companies.
Step 3: Estimate the value as a function of the operating results. As the operating income changes,
there are two levels at which the value of the ﬁrm is affected. The ﬁrst is that lower operating
income, other things remaining equal, lowers the free cash ﬂow, and reduces value. The second is that the return on capital is recomputed, holding the capital invested ﬁxed, as
the operating income changes. As operating income declines, the return on capital drops, and
the ﬁrm will have to reinvest more to sustain the stable growth rate of 2 percent. While we
could also have allowed the cost of capital and the growth rate to vary, we feel comfortable
with both numbers and have left them ﬁxed.
Step 4: Develop a distribution for the value: We ran 10,000 simulations, letting the oil price vary and
valuing the ﬁrm and equity value per share in each simulation. The results are summarized in
Figure 33.10.
The average value per share across the simulations was $69.59, with a minimum value of $2.25
and a maximum value of $324.42; there is, however, a greater than 50% chance that the value per
share will be less than $64.83 (the current stock price). Put differently, this approach yields not only
the value per share for the company but also the likelihood that the ﬁrm is really undervalued (less
than 50%). That information can feed into the investment decision.
914
PROBABILISTIC APPROACHES IN VALUATION
FIGURE 33.9
Oil Price Distribution—Historical Data
−Infinity
$0.00
0.00
0.01
Probability
0.02
10.000 Trials
Frequency View
9,833 Displayed
270
240
210
180
150
120
Frequency
90
60
30
0
Exxon Mobil — Value per Share: Oil price Simulation
$30.00
$60.00
$90.00
$120.00
$150.00
100.00
Certainty
Infinity
%
--- page 934 ---

Use in Decision Making
A well-done simulation provides us with more than just an expected value for an
asset or investment.
■Better input estimation. In an ideal simulation, analysts will examine both the
historical and cross-sectional data on each input variable before making a judgment on what distribution to use and the parameters of the distribution. In the
process, they may be able to avoid the sloppiness that is associated with the use
of point estimates; many discounted cash ﬂow valuations are based upon expected growth rates that are obtained from managers or analysts, often with no
basis in fact.
■It yields a distribution for expected value rather than a point estimate. Consider the valuation of Exxon Mobil that we completed in the last illustration.
In addition to reporting an expected value of $69.59/share, we also estimated a
standard deviation in that value and a breakdown of the values by percentile.
The distribution reinforces the obvious but important point that valuation
models yield estimates of value for risky assets that are imprecise and explains
why different analysts valuing the same asset may arrive at different estimates
of value.
Simulations
915
MARGIN OF SAFETY AND SIMULATION
The margin of safety (MOS) is a measure used widely by value investors to
control risk in investing. Here is how it works. A conservative value investor
will require that a stock be priced more than X percent (10,15, or 20 percent) below the value before she buys it; the margin of safety is the X percent. While intuitive, the margin of safety is not an alternative to traditional
risk measures, since you need to estimate the value of a stock ﬁrst, before
you can use the margin of safety. It is, however, a way in which you can
bring your uncertainty and risk aversion into the decision process, with the
margin of safety increasing as both increase. In practice, though, the margin
of safety is often arbitrarily set and can vary widely across investors and investments.
A well-run simulation can be used to set margins of safety, since it provides information on the estimation error in value. For instance, assume that
your margin of safety is 20 percent and that you are looking at Exxon Mobil
in early 2009. In the Exxon Mobil simulation, for instance, where the expected value is $69.59 per share, adding this requirement would require that
the stock be trading at less than $45 per share (separated by 20% or 2000
outcomes from the expected value of $69.59), for it to be a stock that you
would buy. Obviously, increasing (decreasing) the margin of safety would give
you a lower (or higher) price threshold. Furthermore, the margin of safety will
be greater for ﬁrms where you are more uncertain about the future than for
ﬁrms where you feel more conﬁdent in your inputs.
--- page 935 ---

Note that there are two claims about simulations that we are unwilling to
make. The ﬁrst is that simulations yield better estimates of expected value than
conventional risk-adjusted value models. In fact, the expected values from simulations should be fairly close to the expected value that we would obtain using
the expected values for each of the inputs (rather than the entire distribution).
The second is that simulations, by providing estimates of the expected value and
the distribution in that value, lead to better decisions. This may not always be the
case since the beneﬁts that decision makers obtain by getting a fuller picture of
the uncertainty in value in a risky asset may be more than offset by misuse of that
risk measure. As we will argue later in this chapter, it is all too common for risk
to be double counted in simulations and for decisions to be based on the wrong
type of risk.
Simulations with Constraints
There is a second use for simulations, and that is when you have a constraint that,
if violated, creates very large costs for the ﬁrm and perhaps even causes its demise.
You can examine the likelihood that the constraint will be violated, given the ﬁrm’s
current characteristics, and the implications for value. In this section, we will look
at some of these constraints.
Book Value Constraints
The book value of equity is an accounting construct and,
by itself, means little. Firms like Google and Apple trade at market values that are
several times their book values. At the other extreme, there are ﬁrms that trade at
well below book value. In fact, there are several hundred ﬁrms in the United
States, some with signiﬁcant market values, that have negative book values for
equity. There are two types of restrictions on book value of equity that may affect
value.
1. Regulatory capital restrictions. Financial service ﬁrms such as banks and insurance companies are required to maintain book equity as a fraction of
loans or other assets at or above a ﬂoor ratio speciﬁed by the authorities.
Firms that violate these capital constraints can be taken over by the regulatory authorities and will have to cease operating. Not surprisingly, ﬁnancial
service ﬁrms not only keep a close eye on their book value of equity (and the
related ratios) but are also conscious of the possibility that the risk in their
investments or positions can manifest itself as a drop in book equity. In fact,
value at risk (VAR), a risk measurement device used by many ﬁnancial service ﬁrms, represents the efforts to understand the potential risks in their investments and to be ready for the possibility of a catastrophic outcome,
though the probability of it occurring might be very small. By simulating the
values of their investments under a variety of scenarios, investors can identify not only the possibility of a bank falling below the regulatory ratios but
also the valuation consequences, which can range from loss of all equity
value, as a worst case, to dilution from new equity capital issues, as a best
case.
2. Negative book value for equity. As noted, there are hundreds of ﬁrms in the
United States with negative book values of equity that survive its occurrence
916
PROBABILISTIC APPROACHES IN VALUATION
--- page 936 ---

and have high market values for equity. There are some countries where a
negative book value of equity can create substantial costs for the ﬁrm and its
investors. For instance, companies with negative book values of equity in
parts of Europe are required to raise fresh equity capital to bring their book
values above zero. In some countries in Asia, companies that have negative
book values of equity are barred from paying dividends. Even in the United
States, lenders to ﬁrms can have loan covenants that allow them to gain at
least partial control of a ﬁrm if its book value of equity turns negative. As
with regulatory capital restrictions, investors can use simulations to assess
the probability of a negative book value for equity and to capture the consequences for value.
Debt Constraints
In discounted cash ﬂow valuation, the value of the ﬁrm is computed as a going concern, by discounting expected cash ﬂows at a riskadjusted discount rate. Deducting debt from this estimate yields equity value. The
possibility and potential costs of not being able to meet debt payments is considered only peripherally in the discount rate. In reality, the costs of not meeting
contractual obligations can be substantial. In fact, these costs are generally categorized as indirect bankruptcy costs and could include the loss of customers,
tighter supplier credit, and higher employee turnover. The perception that a ﬁrm
is in trouble can lead to further trouble. By allowing investors to compare the
value of a business to its outstanding claims in all possible scenarios (rather than
just the most likely one), simulations allow them to not only quantify the likelihood of distress but also build the cost of indirect bankruptcy costs into valuation. In effect, you can explicitly model the effect of distress on expected cash
ﬂows and discount rates.
Issues
The use of simulations in investment analysis was ﬁrst suggested in an article by
David Hertz in the Harvard Business Review.8 He argued that using probability
distributions for input variables, rather than single best estimates, would yield
more informative output. In the example that he provided in the paper, he used
simulations to compare the distributions of returns of two investments; the investment with the higher expected return also had a higher chance of losing
money (which was viewed as an indicator of its riskiness). In the aftermath,
there were several analysts who jumped on the simulation bandwagon, with
mixed results. In recent years, there has been a resurgence in interest in simulations as a tool for risk assessment, especially in the context of derivatives. There
are several key issues, though, that we have to deal when using simulations in
risk assessment:
■Garbage in, garbage out. For simulations to have value, the distributions chosen for the inputs should be based on analysis and data, rather than guesswork.
It is worth noting that simulations yield great-looking output, even when the
inputs are random. Unsuspecting decision makers may therefore be getting
meaningless pictures of the risk in an investment. It is also worth noting that
Simulations
917
8Hertz (1964) has a classic paper on the use of probabilistic approaches in decision making.
--- page 937 ---

simulations require more than a passing knowledge of statistical distributions
and their characteristics; analysts who do not know the difference between
normal and uniform distributions should not be doing simulations.
■Real data may not ﬁt distributions. The problem with the real world is that the
data seldom ﬁts the stringent requirements of statistical distributions. Using a
probability distribution that bears little resemblance to the true distribution underlying an input variable will yield misleading results.
■Nonstationary distributions. Even when the data ﬁts a statistical distribution or
where historical data distributions are available, shifts in the market structure
can lead to shifts in the distribution as well. In some cases, this can change the
form of the distribution and in others it can change the parameters of the distribution. Thus, the mean and variance estimated from historical data for an input
that is normally distributed may change for the next period. What we would really like to use in simulations, but seldom can assess, are forward-looking probability distributions.
■Changing correlation across inputs. Earlier in this chapter, we noted that correlation across input variables can be modeled into simulations. However, this
works only if the correlations remain stable and predictable. To the extent that
correlations between input variables change over time, it becomes far more difﬁ-
cult to model them.
Risk-Adjusted Value and Simulations
In our discussion of decision trees, we referred to the common misconception that
decision trees are risk adjusted because they consider the likelihood of adverse
events. The same misconception is prevalent in simulations, where the argument is
that the cash ﬂows from simulations are somehow risk adjusted because of the use
of probability distributions and that the risk-free rate should be used in discounting
these cash ﬂows. With one exception, this argument does not make sense. Looking
across simulations, the cash ﬂows that we obtain are expected cash ﬂows and are
not risk adjusted. Consequently, we should be discounting these cash ﬂows at a
risk-adjusted rate.
The exception occurs when you use the standard deviation in values from a
simulation as a measure of investment or asset risk and make decisions based on
that. In this case, using a risk-adjusted discount rate will result in a double-counting of risk. Consider a simple example. Assume that you are trying to choose between two assets, both of which you have valued using simulations and
risk-adjusted discount rates. The following table below summarizes your ﬁndings.
Note that you view asset B to be riskier and have used a higher discount rate to
compute value. If you now proceed to reject asset B, because the standard deviation
is higher across the simulated values, you would be penalizing it twice. You can redo
the simulations using the riskfree rate as the discount rate for both assets, but a note
918
PROBABILISTIC APPROACHES IN VALUATION
Risk-Adjusted
Simulation:
Simulation:
Asset
Discount Rate
Expected Value
Standard Deviation
A
12%
$100
15%
B
15%
$100
21%
--- page 938 ---

of caution needs to be introduced. If we then base our choice between these assets
on the standard deviation in simulated values, we are assuming that all risk matters
in investment choice, rather than only the risk that cannot be diversiﬁed away. Put
another way, we may end up rejecting an asset because it has a high standard deviation in simulated values, even though adding that asset to a portfolio may result in
little additional risk (because much of its risk can be diversiﬁed away).
This is not to suggest that simulations are not useful to us in understanding risk.
Looking at the variance of the simulated values around the expected value provides
a visual reminder that we are estimating value in an uncertain environment. It is also
conceivable that we can use it as a decision tool in portfolio management in choosing between two stocks that are equally undervalued but have different value distributions. The stock with the less volatile value distribution may be considered a
better investment than another stock with a more volatile value distribution.
AN OVERALL ASSESSMENT OF PROBABILISTIC
RISK-ASSESSMENT APPROACHES
Now that we have looked at scenario analysis, decision trees, and simulations, we
can consider not only when each one is appropriate but also how these approaches
complement or replace risk-adjusted value approaches.
Comparing the Approaches
Assuming that you decide to use a probabilistic approach to assess risk and
could choose among scenario analysis, decision trees, and simulations, which
one should you pick? The answer will depend upon how you plan to use the output and what types of risk you are facing:
■Selective versus full risk analysis. In the best-case/worst-case scenario analysis,
we look at only three scenarios (the best case, the most likely case, and the
worst case) and ignore all other scenarios. Even when we consider multiple scenarios, we will not have a complete assessment of all possible outcomes from
risky investments or assets. With decision trees and simulations, we attempt to
consider all possible outcomes. In decision trees, we try to accomplish this by
converting continuous risk into a manageable set of possible outcomes. With
simulations, we can use distributions to capture all possible outcomes. Put in
terms of probability, the sum of the probabilities of the scenarios we examine
in scenario analysis can be less than 1, whereas the sum of the probabilities of
outcomes in decision trees and simulations has to equal 1. As a consequence,
we can compute expected values across outcomes in the latter, using the probabilities as weights, and these expected values are comparable to the single-estimate risk-adjusted values that we talked about in the preceding chapter.
■Discrete versus continuous risk. As noted earlier, scenario analysis and decision
trees are generally built around discrete outcomes in risky events, whereas simulations are better suited for continuous risks. Focusing on just scenario analysis and
decision trees, the latter are better suited for sequential risks, since risk is considered in phases, whereas the former is easier to use when risks occur concurrently.
■Correlation across risks. If the various risks that an investment is exposed to
are correlated, simulations allow for explicitly modeling these correlations (assuming that you can estimate and forecast them). In scenario analysis, we can
An Overall Assessment of Probabilistic Risk-Assessment Approaches
919
--- page 939 ---

deal with correlations subjectively by creating scenarios that allow for them;
the high (low) interest rate scenario will also include slower (higher) economic
growth. Correlated risks are difﬁcult to model in decision trees.
Table 33.1 summarizes the relationship between risk type and the probabilistic
approach used.
Finally, the quality of the information will be a factor in your choice of
approach. Since simulations are heavily dependent upon being able to assess probability distributions and parameters, they work best in cases in which there is substantial historical and cross-sectional data available that can be used to make these
assessments. With decision trees, you need estimates of the probabilities of the outcomes at each chance node, making them best suited for risks where these risks can
be assessed, either using past data or population characteristics. Thus, it should
come as no surprise that when confronted with new and unpredictable risks, analysts continue to fall back on scenario analysis, notwithstanding its slapdash and
subjective ways of dealing with risk.
Complement or Replacement for Risk-Adjusted Value
As we noted in our discussion of both decision trees and simulations, these approaches can be used as either complements to or substitutes for risk-adjusted
value. Scenario analysis, on the other hand, will always be a complement to riskadjusted value, since it does not look at the full spectrum of possible outcomes.
When any of these approaches are used as complements to risk-adjusted value,
the caveats that we offered earlier in the chapter continue to apply and bear repeating. All of these approaches use expected rather than risk-adjusted cash ﬂows and
the discount rate that is used should be a risk-adjusted discount rate; the risk-free
rate cannot be used to discount expected cash ﬂows. In all three approaches,
though, we still preserve the ﬂexibility to change the risk-adjusted discount rate for
different outcomes. Since all of these approaches will also provide a range for estimated value and a measure of variability (in terms of value at the end nodes in a decision tree or as a standard deviation in value in a simulation), it is important that
we do not double count for risk. In other words, it is patently unfair to risky investments to discount their cash ﬂows back at a risk-adjusted rate (in simulations and
decision trees) and to then reject them because the variability in value is high.
Both simulations and decision trees can be used as alternatives to risk-adjusted
valuation, but there are constraints on the process. The ﬁrst is that the cash ﬂows
will be discounted back at a riskfree rate to arrive at value. The second is that we
now use the measure of variability in values that we obtain in both these approaches
as a measure of risk in the investment. Comparing two assets with the same
expected value (obtained with riskless rates as discount rates) from a simulation, we
will pick the one with the lower variability in simulated values as the better
920
PROBABILISTIC APPROACHES IN VALUATION
TABLE 33.1
Risk Type and Probabilistic Approaches
Discrete/Continuous
Correlated/Independent
Sequential/Concurrent
Risk Approach
Discrete
Independent
Sequential
Decision tree
Discrete
Correlated
Concurrent
Scenario analysis
Continuous
Either
Either
Simulations
--- page 940 ---

investment. If we do this, we are assuming that all of the risks that we have built
into the simulation are relevant for the investment decision. In effect, we are ignoring the line drawn between risks that could have been diversiﬁed away in a portfolio
and asset-speciﬁc risk on which much of modern ﬁnance is built. For investors considering investing all of their wealth in one asset, this should be reasonable. For a
portfolio managers comparing two risky stocks that they are considering adding to a
diversiﬁed portfolio, it can yield misleading results; the rejected stock with the
higher variance in simulated values may be uncorrelated with the other investments
in the portfolio and thus have little marginal risk.
The use of probabilistic approaches has become more common with the surge
in data availability and computing power. It is not uncommon now to see a capital
budgeting analysis, with a 20 to 30 scenarios, or a Monte Carlo simulation attached to an equity valuation.
CONCLUSION
Estimating the risk-adjusted value for a risky asset or investment may seem like an
exercise in futility. After all, the value is a function of the assumptions that we
make about how the risk will unfold in the future. With probabilistic approaches to
valuation, we estimate not only an expected value but also get a sense of the range
of possible outcomes for value, across good and bad scenarios.
■In the most extreme form of scenario analysis, you look at the value in the bestcase and worst-case scenarios and contrast them with the expected value. In its
more general form, you estimate the value under a small number of likely scenarios, ranging from optimistic to pessimistic.
■Decision trees are designed for sequential and discrete risks, where the risk in an
investment is considered in phases and the risk in each phase is captured in the
possible outcomes and the probabilities that they will occur. A decision tree provides a complete assessment of risk and can be used to determine the optimal
courses of action at each phase and an expected value for an asset today.
■Simulations provide the most complete assessments of risk since they are based
on probability distributions for each input (rather than just discrete outcomes).
The output from a simulation takes the form of an expected value across simulations and a distribution for the simulated values.
With all three approaches, the keys are to avoid double counting risk (by using
a risk-adjusted discount rate and considering the variability in estimated value as a
risk measure) or making decisions based on the wrong types of risk.
QUESTIONS AND SHORT PROBLEMS
In the problems following, use an equity risk premium of 5.5 percent if none if
speciﬁed.
1. You have estimated the value per share for Littleﬁeld Inc., a transportation company, under three scenarios: $5/share under the worst-case scenario, $30/share
under the best-case scenario, and $18/share under the most likely scenario. If
the stock is trading at $15, would you buy the stock? Why or why not?
Questions and Short Problems
921
--- page 941 ---

2. You are analyzing Delta Enterprises, a small publicly traded company with
$50 million of debt outstanding, and 25 million shares, trading at $10/share.
The ﬁrm generated $40 million in after-tax cash ﬂows last year, and you estimate that these cash ﬂows will grow 2% a year in perpetuity and that the cost
of capital for the ﬁrm is 12%.
a. Estimate a value per share for the ﬁrm, assuming it has no cash balance.
b. Now assume that you ﬁnd out that a signiﬁcant portion of the ﬁrm’s revenues
comes from one customer and that there is a 20 percent chance that this contract will be lost next year. Assuming that a lost contract will result in a 50%
drop in the after-tax cash ﬂows, estimate the value per share today. (You can
assume that the growth rate and cost of capital will be unaffected).
3. You are valuing Signet Bank during a period of substantial uncertainty about
future regulatory rules. Signet Bank generated $100 million in net income last
year on a book value of equity of $1 billion and paid out $70 million in dividends. While you expect Signet to be a stable growth company, you envision
the following regulatory scenarios for the future:
■Status quo—no changes in regulatory rules (40% probability): Signet will
continue to generate its current return on equity in perpetuity and maintain
its existing dividend payout ratio.
■Regulatory easing—lower regulatory capital ratios (25 percent probability):
Signet will be able to generate a return on equity of 12 percent on future investments, while maintaining its stable growth rate (at status quo levels).
■Regulatory tightening—higher regulatory capital ratios (35 percent probability): Signet will see its return on equity drop to 9%, while maintaining its
stable growth rate (at status quo levels).
■Estimate the value of equity in Signet Bank under each scenario. (You can
leave current net income unchanged under all scenarios.)
■Given the probabilities of each scenario unfolding, estimate the value of equity in Signet Bank today.
4. Sigma Energy is an alternative energy company that produces solar energy panels. The company is expected to generate $50 million in after-tax operating income in the next year, but its prospects for future growth are dependent upon
the level of oil prices and access to low-cost (and subsidized) government ﬁ-
nancing. You have outlined the following scenarios (with consequences for
growth (g), return on invested capital (ROC) and cost of capital (r)):
Government
Government
Subsidies Continue
Subsidies End
Oil prices > $100/barrel
g = 4%, ROC = 12%,
g = 4%, ROC = 12%,
(30% probability)
r = 8%
r = 10%
Oil prices between $60
g = 3%, ROC = 10%,
g = 3%, ROC = 10%,
and $100/barrel
r = 8%
r = 10%
(50% probability)
Oil prices < $60/barrel
g = 2%, ROC = 8%,
g = 2%, ROC = 8%,
(20% probability)
r = 8%
r = 10%
a. Estimate the value of the ﬁrm under each scenario. (You can leave the aftertax operating income for next year unchanged at $50 million under all the
scenarios.)
922
PROBABILISTIC APPROACHES IN VALUATION
--- page 942 ---

b. If the probability that the government will end subsidies is 40%, estimate
the value of the ﬁrm across the scenarios.
5. Chavez Enterprises is a small Venezuelan company. The ﬁrm is proﬁtable and is
expected to generate 120 million bolivars in after-tax operating income next
year on capital invested (book value) of 600 million bolivars. You have estimated a cost of capital of 12% for the ﬁrm and expect it to grow 4 percent a
year in perpetuity.
a. Estimate the value of the ﬁrm today.
b. Now assume that you are concerned that the ﬁrm may be nationalized. If nationalization occurs, you will be paid book value for the assets. Assuming a
30% probability for nationalization, estimate the value of the ﬁrm today.
6. Loral Drugs is a biotechnology ﬁrm that is working on a new drug to treat insomnia. The drug is working its way through the FDA approval process and is
expected to generate $150 million in after-tax cash ﬂows each year for 15
years, once it is approved. There are two more hurdles that the drug has to
cross before approval:
■A small sample test on laboratory animals that will take a year to complete
and is expected to cost $100 million (to be spent today); there is an 80 percent chance that it will succeed.
■If the lab animal test succeeds, it will be followed by a study on human subjects that will take two additional years to complete and cost $250 million
(to be spent at the end of year 1); there is a 60 percent chance that this study
will yield favorable results.
The cost of capital for biotechnology ﬁrms is 10%.
a. Outline the decision tree for the insomnia drug.
b. Estimate the expected value of the drug to the company today.
7. You are a venture capitalist who is interested in investing $50 million in
Friends Online, a social media company. The business will take three years to
become operational (during which period it will generate no positive cash
ﬂows), and once operational, it will generate $27 million in after-tax cash
ﬂows, growing 3% in perpetuity. The cost of capital for established social media companies is 12%, but there is a 60 percent chance that the business will
not survive (in which case it will have no assets of value to liquidate).
a. Estimate the value of Friends Online, once it is operational.
b. Given the likelihood of failure, estimate the proportion of equity in Friends
Online you would demand today in return for your $50 million investment.
(You can assume that Friends Online has no debt or cash.)
c. Estimate the target return you would demand over the next three years,
with the risk of failure incorporated into the return.
To solve the next two problems, you will need access to a simulation program
like Crystal Ball or @Risk.
8. You are valuing Stedman Inc., a chemical ﬁrm in stable growth (growing 3 percent a year) that is expected to generate $100 million in after-tax operating income next year. You have estimated the following:
■The return on invested capital on new investments is normally distributed,
with an expected value of 15%, with a standard deviation of 3%.
■The cost of capital for the ﬁrm is 10%, uniformly distributed, with a minimum value of 8% and a maximum value of 12%.
Questions and Short Problems
923
--- page 943 ---

The ﬁrm has $500 million in debt outstanding and a cash balance of $200
million. Develop a distribution of simulated values for Stedman Inc.
9. Simon Gold is a mature gold mining ﬁrm that has mines that are expected to
generate 100,000 ounces of gold every year for the next 25 years; at the end of
that period, the mines will be exhausted and will be worth nothing. The company has ﬁxed costs of $100 million that are expected to remain unchanged
over the next 25 years and no variable costs. The cost of capital for gold mining companies is 8%.
a. If the current gold price is $1,500 an ounce and is expected to remain unchanged for the next 25 years, estimate the value of Simon Gold.
b. Now assume that you believe that gold prices will be normally distributed
with an expected value of $1,500 an ounce and a standard deviation of
$200 an ounce. Develop a distribution of simulated values for Simon Gold.
10. You are a portfolio manager and have analysts who have used Monte Carlo
simulations to ﬁnd 10 undervalued companies, listed here:
% Chance
That the
Expected
Standard
Firm Is
Lowest
Highest
Company
Price
Value
Deviation
Undervalued
Value
Value
A
$    8.00
$  10.00
$  1.00
80%
$  7.00
$  13.00
B
$  12.00
$  13.50
$  0.50
75%
$10.00
$  16.00
C
$  15.00
$  20.00
$  5
50%
$  4.00
$  50.00
D
$    9.00
$  10.00
$  0.20
85%
$  8.50
$  13.00
E
$  50.00
$  80.00
$10.00
80%
$40.00
$150.00
F
$  22.00
$  25.00
$  1
88%
$18.00
$  28.00
G
$    3.00
$    5.00
$  0.50
70%
$  2.50
$    6.00
H
$150.00
$200.00
$30.00
60%
$40.00
$500.00
I
$  35.00
$  70.00
$20.00
65%
$  0.00
$200.00
J
$  80.00
$100.00
$  5.00
90%
$70.00
$115.00
a. Purely on an expected value basis, rank these companies (from best to worst
investments).
b. If you wanted to incorporate the uncertainty in the estimates into your ranking, how would the rankings change?
c. If you were worried about downside risk (because you are highly levered),
how would you incorporate that risk into your rankings?
d. Under what conditions might you incorporate the highest value into your
ranking process?
924
PROBABILISTIC APPROACHES IN VALUATION
--- page 944 ---

CHAPTER 34
Overview and Conclusion
T
he problem in valuation is not that there are not enough models to value an asset, it is that there are too many. Choosing the right model to use in valuation is
as critical to arriving at a reasonable value as understanding how to use the model.
This chapter attempts to provide an overview of the valuation models introduced in
this book, and a general framework that can be used to pick the right model for any
task.
CHOICES IN VALUATION MODELS
In the broadest possible terms, ﬁrms or assets can be valued in one of four ways:
asset-based valuation approaches where you estimate what the assets owned by a
ﬁrm are worth currently, discounted cash ﬂow valuation approaches that discount
cash ﬂows to arrive at a value of equity or the ﬁrm, relative valuation approaches
that base value on how comparable assets are priced, and option pricing approaches
that use contingent claim valuation. Within each of these approaches, there are
further choices that help determine the ﬁnal value.
There are at least two ways in which you can value a ﬁrm using asset-based valuation techniques. One is liquidation value, where you consider what the market
will be willing to pay for assets if the assets were liquidated today. The other is replacement cost, where you evaluate how much it would cost you to replicate or replace the assets that a ﬁrm has in place today.
In the context of discounted cash ﬂow valuation, cash ﬂows to equity can be
discounted at the cost of equity to arrive at a value of equity, or cash ﬂows to the
ﬁrm can be discounted at the cost of capital to arrive at the value for the ﬁrm. The
cash ﬂows to equity themselves can be deﬁned in the strictest sense as dividends or
in a more expansive sense as free cash ﬂows to equity. These models can be further
categorized on the basis of assumptions about growth into stable-growth, twostage, three-stage and n-stage models. Finally, the measurement of earnings and
cash ﬂows may be modiﬁed to match the special characteristics of the ﬁrm/asset—
current earnings for ﬁrms/assets that have normal earnings, or normalized earnings
for ﬁrms/assets whose current earnings may be distorted either by temporary factors
or cyclical effects.
In the context of multiples, you can use either equity or ﬁrm value as your measure of value and relate it to a number of ﬁrm-speciﬁc variables— earnings, book
value, and sales. The multiples themselves can be estimated by using comparable
ﬁrms in the same business or from cross-sectional regressions that use the broader
universe. For other assets, such as real estate, the price can similarly be expressed as
925
--- page 945 ---

a function of gross income or per square foot of space. Here the comparables
would be other properties in the same locale with similar characteristics.
Contingent claim models can also be used in a variety of scenarios. When you
consider the option that a ﬁrm has to delay making investment decisions, you can
value a patent or an undeveloped natural resource reserve as an option. The option to expand may make young ﬁrms with potentially large markets trade at a
premium on their discounted cash ﬂow values. Finally, equity investors may derive value from the option to liquidate troubled ﬁrms with substantial debt. (See
Figure 34.1.)
WHICH APPROACH SHOULD YOU USE?
The values that you obtain from the four approaches can be very different, and deciding which one to use can be a critical step. This judgment, however, will depend
on several factors, some of which relate to the business being valued but many of
which relate to you as the analyst.
Asset or Business Characteristics
The approach you use to value a business will depend on how marketable its assets
are, whether it generates cash ﬂows, and how unique it is in terms of its operations.
Marketability of Assets
Liquidation valuation and replacement cost valuation are
easiest to do for ﬁrms that have assets that are separable and marketable. (See Figure
34.2.) For instance, you can estimate the liquidation value for a real estate company
because its properties can be sold individually, and you can estimate the value of
each property easily. The same can be said about a closed-end mutual fund. At the
other extreme, consider a brand-name consumer product like Proctor and Gamble.
926
OVERVIEW AND CONCLUSION
FIGURE 34.1
The Choices in Valuation Models
--- page 946 ---

Its assets are not only intangible but difﬁcult to separate out. For instance, you cannot separate the razor business easily from the shaving cream business, and brand
name value is inherent in both businesses.
You can also use this same analysis to see why the liquidation or replacement
cost value of a high-growth business may bear little resemblance to true value. Unlike assets in place, growth assets cannot be easily identiﬁed or sold.
Cash-Flow-Generating Capacity
You can categorize assets into three groups based
on their capacity to generate cash ﬂows: assets that are either generating cash ﬂows
currently or are expected to do so in the near future, assets that are not generating
cash ﬂows currently but could in the future in the event of a contingency, and assets
that will never generate cash ﬂows. (See Figure 34.3.)
1. The ﬁrst group includes most publicly traded companies, and these ﬁrms can
be valued using discounted cash ﬂow models. Note that a distinction is not
drawn between negative and positive cash ﬂows, and young start-up companies that generate negative cash ﬂow can still be valued using discounted cash
ﬂow models.
2. The second group includes assets such as drug patents, promising (but not viable) technology, undeveloped oil or mining reserves, and undeveloped land.
These assets may generate no cash ﬂows currently and could generate large
cash ﬂows in the future but only under certain conditions—if the FDA approves the drug patent, if the technology becomes commercially viable, if oil
prices and commercial property values go up. While you could estimate expected values using discounted cash ﬂow models by assigning probabilities to
these events, you will understate the value of the assets if you do so. You
should value these assets using option pricing models.
3. Assets that are never expected to generate cash ﬂows include your primary residence, a baseball card collection, or ﬁne art. These assets can only be valued
using relative valuation models.
Which Approach Should You Use?
927
FIGURE 34.2
Asset Marketability and Valuation Approaches
FIGURE 34.3
Cash Flows and Valuation Approaches
--- page 947 ---

Uniqueness (or Presence of Comparables)
In a market where thousands of stocks
are traded and tens of thousands of assets are bought and sold every day, it may be dif-
ﬁcult to visualize an asset or business that is so unique that you cannot ﬁnd comparable assets. On a continuum, though, some assets and businesses are part of a large
group of similar assets, with no or very small differences across the assets. (See Figure
34.4.) These assets are tailor-made for relative valuation, since assembling comparable
assets (businesses) and controlling for differences is simple. The further you move
from this ideal, the less reliable is relative valuation. For businesses that are truly
unique, discounted cash ﬂow valuation will yield much better estimates of value.
Analyst Characteristics and Beliefs
The valuation approach that you choose to use will depend on your time horizon,
the reason that you are doing the valuation in the ﬁrst place, and what you think
about markets—whether they are efﬁcient, and if they are not, what form the inef-
ﬁciency takes.
Time Horizon
At one extreme, in discounted cash ﬂow valuation, you consider a
ﬁrm as a going concern that may last into perpetuity. At the other extreme, with
liquidation valuation, you are estimating value on the assumption that the ﬁrm will
cease operations today. With relative valuation and contingent claim valuation, you
take an intermediate position between the two. (See Figure 34.5.) Not surprisingly,
then, you should be using discounted cash ﬂow valuation if you have a long time
horizon, and relative valuation if you have a shorter time horizon. This may explain why discounted cash ﬂow valuation is more prevalent when valuing a ﬁrm for
an acquisition, and relative valuation is more common in equity research and portfolio management.
Reason for Doing the Valuation
Analysts value businesses for a number of reasons, and the valuation approach used will vary depending on the reason. (See
Figure 34.6.) If you are an equity research analyst following steel companies,
928
OVERVIEW AND CONCLUSION
FIGURE 34.4
Uniqueness of Asset and Valuation Approaches
FIGURE 34.5
Investor Time Horizon and Valuation Approaches
--- page 948 ---

your job description is simple. You are asked to ﬁnd the most underand overvalued companies in the sector, and not take a stand on whether the sector overall is underor overvalued. You can see why multiples would be your weapon of
choice when valuing companies. This effect is likely to be exaggerated if the way
you are judged and rewarded is on a relative basis (i.e., your recommendations
are compared to those made by other steel company analysts). But if you are
an individual investor setting money aside for retirement or a private businessperson valuing a business for purchase, you want to estimate intrinsic value.
Consequently, discounted cash ﬂow valuation is likely to be more appropriate
for your needs.
Beliefs about Markets
Embedded in each approach are assumptions about markets and how they work or fail to work. (See Figure 34.7.) With discounted cash
ﬂow valuation, you are assuming that market prices deviate from intrinsic value
but that they correct themselves over long periods. With relative valuation, you are
assuming that markets are on average right, and that while individual ﬁrms in a
sector or market may be mispriced, the sector or overall market is fairly priced.
With asset-based valuation models, you are assuming that the markets for real and
ﬁnancial assets can deviate and that you can take advantage of these differences. Finally, with option pricing models, you are assuming that markets are not very efﬁ-
cient at assessing the value of ﬂexibility that ﬁrms have, and that option pricing
models will therefore give you an advantage. In each and every one of these cases,
though, you are assuming that markets will eventually recognize their mistakes and
correct them.
CHOOSING THE RIGHT DISCOUNTED CASH FLOW MODEL
The model used in valuation should be tailored to match the characteristics of the
asset being valued. The unfortunate truth is that the reverse is often true. Time and
Choosing the Right Discounted Cash Flow Model
929
FIGURE 34.6
Market Neutrality and Valuation Approaches
FIGURE 34.7
Views on Market and Valuation Approaches
--- page 949 ---

resources are wasted trying to make assets ﬁt a prespeciﬁed valuation model, either
because it is considered to be the best model or because not enough thought goes
into the process of model choice. There is no one best model. The appropriate
model to use in a particular setting will depend on a number of the characteristics
of the asset or ﬁrm being valued.
Choosing a Cash Flow to Discount
With consistent assumptions about growth and leverage, you should get the same
value for your equity using the ﬁrm approach (where you value the ﬁrm and subtract outstanding debt) and the equity approach (where you value equity directly).
If this is the case, you might wonder why you would pick one approach over the
other. The answer is purely pragmatic. For ﬁrms that have stable leverage (i.e., they
have debt ratios that are not expected to change during the period of the valuation), there is little to choose between the models in terms of the inputs needed for
valuation. You use a debt ratio to estimate free cash ﬂows to equity in the equity
valuation model, and to estimate the cost of capital in the ﬁrm valuation model.
Under these circumstances, you should stay with the model that you are more intuitively comfortable with.
For ﬁrms that have unstable leverage (i.e., they have too much or too little debt
and want to move toward their optimal or target debt ratio during the period of the
930
OVERVIEW AND CONCLUSION
BRIDGING THE PHILOSOPHICAL DIVIDE
Philosophically, there is a big gap between discounted cash ﬂow valuation and
relative valuation. In discounted cash ﬂow valuation, we take a long-term perspective, evaluate a ﬁrm’s fundamentals in detail, and try to estimate a ﬁrm’s
intrinsic value. In relative valuation, we assume that the market is right on average and estimate the value of a ﬁrm by looking at how similar ﬁrms are
priced. There is something of value in both approaches, and it would be useful
if we could borrow the best features of relative valuation while doing discounted cash ﬂow valuation, or vice versa.
Assume that your instincts lead you to discounted cash ﬂow valuation,
but that you are expected, as an analyst, to be market-neutral. You can stay
market-neutral in a discounted cash ﬂow framework if you use the implied
risk premium for the market (described in Chapter 7) to estimate the cost of
equity for the valuation. You can also bring in information about comparable
ﬁrm margins and betas when estimating fundamentals for your ﬁrm. Your estimate of intrinsic value will then be market-neutral and include information
about comparables.
Alternatively, assume that you prefer relative valuation. Your analysis can
carry the rigor of a discounted cash ﬂow valuation if you can bring in the details of the fundamentals into your comparisons. The chapters on relative valuation attempted to do this by noting the link between multiples and
fundamentals, and also by examining how best to control for these differences
in the analysis.
--- page 950 ---

valuation), the ﬁrm valuation approach is much simpler to use because it does not
require cash ﬂow projections from interest and principal payments and is much less
sensitive to errors in estimating leverage changes. The calculation of the cost of capital requires an estimate of the debt ratio, but the cost of capital itself does not
change as much as a consequence of changing leverage as does the cash ﬂow to equity. If you prefer to work with assumptions about dollar debt rather than debt ratios, you can switch to the adjusted present value approach.
In valuing equity, you can discount dividends or free cash ﬂows to equity. You
should consider using the dividend discount model under the following circumstances:
■You cannot estimate cash ﬂows with any degree of precision either because you
have insufﬁcient or contradictory information about debt payments and reinvestments or because you have trouble deﬁning what comprises debt. This was
the rationale for using dividend discount models for valuing ﬁnancial service
ﬁrms in Chapter 21.
■There are signiﬁcant restrictions on stock buybacks and other forms of cash return, and you have little or no control over what the management of a ﬁrm
does with the cash. In this case, the only cash ﬂows you can expect to get from
your equity investment are the dividends that managers choose to pay out.
In all other cases, you will get much more realistic estimates of a ﬁrm’s value
using the free cash ﬂow to equity, which may be greater than or lower than the
dividend.
Should You Use Current or Normalized Earnings?
Most valuations begin with the current ﬁnancial statements of the ﬁrm and use the
reported earnings in those statements as the base for projections. There are some
ﬁrms, though, where you may not be able to do this, either because the ﬁrm’s earnings are negative or because these earnings are abnormally high or low (a ﬁrm’s
earnings are abnormal if they do not ﬁt in with the ﬁrm’s own history of earnings).
When earnings are negative or abnormal, you can sometimes replace current
earnings with a normalized value, estimated by looking at the company’s history or
industry averages, and value the ﬁrm based on these normalized earnings. This is
the easiest route to follow if the causes for the negative or abnormal earnings are
temporary or transitory, as in the following cases:
■A cyclical ﬁrm will generally report depressed earnings during an economic
downturn and high earnings during an economic boom. Neither may capture
properly the true earnings potential of the ﬁrm.
■A ﬁrm may report abnormally low earnings in a period during which it takes
an extraordinary charge.
■A ﬁrm in the process of restructuring may report low earnings during the restructuring period as the changes made to improve ﬁrm performance are put
into effect.
The presumption here is that earnings will quickly bounce back to normal levels
and that little will be lost by assuming that this will occur immediately.
Choosing the Right Discounted Cash Flow Model
931
--- page 951 ---

For some ﬁrms, though, the negative or low earnings may reﬂect factors that
are unlikely to disappear quickly. There are at least three groups of ﬁrms where the
negative earnings are likely to be a long-term phenomenon and may even threaten
the ﬁrm’s survival:
1. Firms with long-term operating, strategic, or ﬁnancial problems can have extended periods of negative or low earnings. If you replace current earnings with
normalized earnings and value these ﬁrms, you will overvalue them.
■If a ﬁrm seems to be in imminent danger of default, the only models that are
likely to provide meaningful measures of value are the option pricing model (if
ﬁnancial leverage is high) or a model based on liquidation value.
■If the ﬁrm is troubled but unlikely to go bankrupt, you will have to nurse it
back to ﬁnancial health. In practical terms, you will have to adjust the operating margins over time to healthier levels and value the ﬁrm based on its expected cash ﬂows.
2. An infrastructure ﬁrm may report negative earnings in its initial periods of
growth, not because it is unhealthy but because the investments it has made
take time to pay off. The cash ﬂows to the ﬁrm and equity are often also negative, because the capital expenditure needs for this type of ﬁrm tend to be disproportionately large relative to depreciation. For these ﬁrms to have value,
capital expenditure has to drop once the infrastructure investments have been
made and operating margins have to improve. The net result will be positive
cash ﬂows in future years and a value for the ﬁrm today.
3. Young start-up companies often report negative earnings early in their life cycles, as they concentrate on turning interesting ideas into commercial products.
To value such companies, you have to assume a combination of high revenue
growth and improving operating margins over time.
Growth Patterns
In general, when valuing a ﬁrm, you can assume that your ﬁrm is already in stable
growth, assume a period of constant high growth and then drop the growth rate to
stable growth (two-stage growth), or allow for a transition phase to get to stable
growth (three-stage or n-stage models). There are several factors you should consider
in making this judgment:
Growth Momentum
The choice of growth pattern will be inﬂuenced by the level of
current growth in earnings and revenues. You can categorize ﬁrms, based on
growth in recent periods, into three groups.
1. Stable-growth ﬁrms report earnings and revenues growing at or below the nominal growth rate in the economy that they operate in. Note that this growth rate
can even be negative.
2. Moderate-growth ﬁrms report earnings and revenues growing at a rate moderately higher than the nominal growth rate in the economy; as a rule of thumb,
consider any growth rate within 8 to 10 percent of the growth rate of the economy as a moderate growth rate.
3. High-growth ﬁrms report earnings and revenues growing at a rate much higher
than the nominal growth rate in the economy.
932
OVERVIEW AND CONCLUSION
