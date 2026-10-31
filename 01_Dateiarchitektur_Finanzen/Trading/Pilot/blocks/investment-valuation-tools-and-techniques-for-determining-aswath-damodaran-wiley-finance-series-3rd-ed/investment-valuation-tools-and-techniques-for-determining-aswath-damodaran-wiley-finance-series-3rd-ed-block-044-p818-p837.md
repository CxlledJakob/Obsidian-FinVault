# INVESTMENT VALUATION TOOLS AND TECHNIQUES FOR DETERMINING -- Aswath Damodaran -- Wiley finance series, 3rd ed_, Hoboken, N_J, New Jersey, -- John -- isbn13 9781118011522 -- f84d1622bdc2de526da0dda803c52830 -- Anna’s.pdf — pages 818–837

--- page 818 ---

Valuing a Firm with Undeveloped Reserves
The examples provided earlier illustrate the use of option pricing theory in valuing
individual mines and oil tracts. Since the assets owned by a natural resource ﬁrm
can be viewed primarily as options, the ﬁrm itself can be valued using option pricing models.
Individual Reserves versus Aggregate Reserves
The preferred approach would be
to consider each reserve separately, value it, and cumulate the values of the reserves
Natural Resource Options
799
natres.xls: This spreadsheet allows you to estimate the value of an undeveloped
natural resource reserve.
MULTIPLE SOURCES OF UNCERTAINTY
In the preceding example, we assumed that there was no uncertainty about
the quantity of the reserve. Realistically, the oil company has an estimate of
the reserve of 50 million barrels but does not know it with certainty. If we introduce uncertainty about the quantity of the reserve into the analysis, there
will be two sources of variance and both can affect value. There are two ways
we can address this problem:
1. Combine the uncertainties into one value. If we consider the value of
the reserves to be the product of the price of oil and the oil reserves, the variance in the value should reﬂect the combined effect of the variances in each input.10 This would be the variance we would use in the option pricing model to
estimate a new value for the reserve.
2.
Keep the variances separate and value the option as a rainbow option. A rainbow option allows explicitly for more than one source of variance and allows us to keep the variances separate and still value the option.
While option pricing becomes more complicated, you may need to do this if
you expect the two sources of uncertainty to evolve differently over time—
the variance from one source (say, oil prices) may increase over time
whereas the variance from the other source (say, oil reserves) may decrease
over time.
10This is the variance of a product of two variables.
--- page 819 ---

to get the value of the ﬁrm. Since this information is likely to be difﬁcult to obtain
for large natural resource ﬁrms, such as oil companies, which own hundreds of
such reserves, a variant of this approach is to value the entire ﬁrm’s undeveloped
reserves as one option. A purist would probably disagree, arguing that valuing an
option on a portfolio of assets (as in this approach) will provide a lower value than
valuing a portfolio of options (which is what the natural resource ﬁrm really owns).
Nevertheless, the assumption that the only source of variance is the price of the
natural resource effectively makes the values of the reserves perfectly correlated and
allows us to use the short cut with limited or no cost.
Inputs to Option Valuation
If you decide to apply the option pricing approach to estimate the value of aggregate undeveloped reserves, you have to estimate the inputs
to the model. In general terms, while the process resembles the one used to value an
individual reserve, there are a few differences.
■Value of underlying asset. You should cumulate all of the undeveloped reserves
owned by a company and estimate the value of these reserves, based on the
price of the resource today and the average variable cost of extracting these reserves today. The variable costs are likely to be higher for some reserves and
lower for others, and weighting the variable costs at each reserve by the quantity of the resource of that reserve should give you a reasonable approximation
of this value. At least hypothetically, we are assuming that the company can decide to extract all of its undeveloped reserves at one time and not affect the
price of the resource.
■Exercise price. For this input, you should consider what it would cost the
company today to develop all of its undeveloped reserves. Again, the costs
might be higher for some reserves than for others, and you can use a weighted
average cost.
■Life of the option. A ﬁrm will probably have different lives for each of its reserves. As a consequence, you will have to use a weighted average of the lives
of the different reserves.11
■Variance in the value of the asset. Here, there is a strong argument for looking at only the oil price as the source of variance, since a ﬁrm should have
a much more precise estimate of its total reserves than it does of any one of
its reserves.
■Dividend yield (cost of delay). As with an individual reserve, a ﬁrm with viable
reserves will be giving up the cash ﬂows it could receive in the next period from
developing these reserves if it delays exercise. This cash ﬂow, stated as a percent
of the value of the reserves, becomes the equivalent of the dividend yield. The
development lag reduces the value of this option just as it reduces the value of
an individual reserve. The logical implication is that undeveloped reserves will
be worth more at oil companies that can develop their reserves quicker than at
less efﬁcient companies.
800
THE OPTION TO DELAY AND VALUATION IMPLICATIONS
11If you own some reserves in perpetuity, you should cap the life of the reserve at a large
value—say, 30 years—in making this estimate.
--- page 820 ---

ILLUSTRATION 28.5:
Valuing an Oil Company: Gulf Oil in 1984
Gulf Oil was the target of a takeover in early 1984 at $70 per share (It had 165.30 million shares outstanding and total debt of $9.9 billion). It had estimated reserves of 3,038 million barrels of oil and
the total cost of developing these reserves at that time was estimated to be $30.38 billion (the development lag is approximately two years). The average relinquishment life of the reserves is 12 years.
The price of oil was $22.38 per barrel, and the production costs, taxes, and royalties were estimated
at $7 per barrel. The bond rate at the time of the analysis was 9.00%. If Gulf were to choose to develop these reserves, it was expected to have cash ﬂows next year of approximately 5% of the value
of the developed reserves. The variance in oil prices is 0.03.
Value of underlying asset = Value of estimated reserves discounted back for period of development lag
= 3,038 × ($22.38 −$7)/1.052 = $42,380.44
Note that you could have used forecasted oil prices and estimated cash ﬂows over the production period and estimated the value of the underlying asset to be the present value of all of these cash ﬂows.
We have used a shortcut of assuming that the current contribution margin of $15.38 a barrel will remain unchanged in present value terms over the production period.
Exercise price = Estimated cost of developing reserves today = $30,380 million
Time to expiration = Average length of relinquishment option = 12 years
Variance in value of asset = Variance in oil prices = 0.03
Riskless interest rate = 9%
Dividend yield = Net production revenue/Value of developed reserves = 5%
Based on these inputs, the Black-Scholes model provides the following value for the call:12
d1 = 1.6548
N(d1) = 0.9510
d2 = 1.0548
N(d2) = 0.8542
Call value = 42,380.44 exp(−0.05)(12)(0.9510) −30,380 exp(−0.09)(12)(0.8542) = $13,306 million
This stands in contrast to the discounted cash ﬂow value of $12 billion that you obtain by taking the
difference between the present value of the cash ﬂows of developing the reserve today ($42.38 billion) and the cost of development ($30.38 billion). The difference can be attributed to the option possessed by Gulf to choose when to develop its reserves.
The option value ($13.3 billion) represents the value of the undeveloped reserves of oil owned by
Gulf Oil. In addition, Gulf Oil had free cash ﬂows to the ﬁrm from its oil and gas production of $915
million from already developed reserves and we assume that these cash-ﬂows are likely to be constant and continue for 10 years (the remaining lifetime of developed reserves). The present value of
these developed reserves, discounted at the weighted average cost of capital of 12.5%, yields:
Value of already developed reserves = 915(1 −1.125−10)/.125 = $5,065.83
Adding the value of the developed and undeveloped reserves of Gulf Oil provides the value of the ﬁrm.
Value of undeveloped reserves
$13,306 million
Value of production in place
$ 5,066 million
Total value of ﬁrm
$18,372 million
Less outstanding debt
$ 9,900 million
Value of equity
$ 8,472 million
Value per share
$ 8,472/165.3 = $51.25
This analysis would suggest that Gulf Oil was overvalued at $70 per share.
Natural Resource Options
801
12With a binomial model, we estimate the value of the reserves to be $13.73 billion.
--- page 821 ---

OTHER APPLICATIONS
While patents and undeveloped reserves of natural resource companies lend themselves best to applying option pricing, there are other assets referenced in earlier
chapters that can also be valued as options.
■Chapter 26, in the context of real estate valuation, noted that vacant land
could be viewed as an option on commercial development.
■Chapter 27 presented an argument that copyrights and licenses could be
viewed as options, even if they are not commercially viable today.
Table 28.1 presents the inputs you would use to value each of these options in
an option pricing model. Much of what we have said about the other option applications apply here as well. The value is derived from the exclusivity that you have
to commercially develop the asset. That exclusivity is obtained by legal sanction in
the case of licenses and copyrights, and from the scarcity of land in the case of undeveloped land.
CONCLUSION
In traditional investment analysis, we compute the net present value of a project’s
cash ﬂows and conclude that ﬁrms should not invest in a project with a negative net
present value. This is generally good advice, but it does not imply that the rights to
this project are not valuable. Projects that have negative net present values today
may have positive net present values in the future, and the likelihood of this occurring is directly a function of the volatility in the present value of the cash ﬂows
from the project.
802
THE OPTION TO DELAY AND VALUATION IMPLICATIONS
PRICE VOLATILITY AND NATURAL RESOURCE COMPANY VALUATION
An interesting implication of this analysis is that the value of a natural resource company depends not just on the price of the natural resource but
also on the expected volatility in that price. Thus, if the price of oil goes from
$25 a barrel to $40 a barrel, you would expect all oil companies to become
more valuable. If the price drops back to $25, the values of oil companies
may not decline to their old levels, since the perceived volatility in oil prices
may have changed. If investors believe that the volatility in oil prices has increased, you would expect an increase in values but the increase will be
greatest for companies that derive a higher proportion of their value from
undeveloped reserves.
If you regard undeveloped reserves as options, discounted cash ﬂow valuation will generally underestimate the value of natural resource companies,
because the expected price of the commodity is used to estimate revenues and
operating proﬁts. As a consequence, you miss the option component of value.
Again, the difference will be greatest for ﬁrms with signiﬁcant undeveloped reserves and with commodities whose price volatility is highest.
--- page 822 ---

This chapter valued the option to delay an investment and considered the implications of this option for three valuation scenarios—the value of a ﬁrm that derives all or a signiﬁcant portion of value from patents that have not yet been
commercially exploited, the value of a natural resource company with undeveloped
reserves of the resource, and the value of a real estate ﬁrm with undeveloped land.
In each case, using discounted cash ﬂow valuation would result in an understatement of the values of these ﬁrms.
QUESTIONS AND SHORT PROBLEMS
In the problems following, use an equity risk premium of 5.5 percent if none is
speciﬁed.
1. A company is considering delaying a project with after-tax cash ﬂows of $25
million but that costs $300 million to take on (the life of the project is 20 years,
and the cost of capital is 16%). A simulation of the cash ﬂows leads you to conclude that the standard deviation in the present value of cash inﬂows is 20%. If
you can acquire the rights to the project for the next 10 years, what is the value
of the rights? (The six-month T-bill rate is 8%, the 10-year bond rate is 12%,
and the 20-year bond rate is 14%.)
2. You are examining the ﬁnancial viability of investing in some abandoned copper
mines in Chile, which still have signiﬁcant copper deposits in them. A geologist
survey suggests that there might be 10 million pounds of copper in the mines
Questions and Short Problems
803
TABLE 28.1
Inputs to Value Other Options to Delay
Undeveloped Land
License/Copyright
Value of the
Present value of the cash ﬂows
Present value of the cash
underlying asset
that would be obtained from
ﬂows that would be
commercial development of
obtained from commercially
land today.
utilizing the license or
copyright today.
Variance in value of
Variance in the values of
Variance in the present values
underlying asset
commercial property in the
from commercial utilization
area where the real estate is
of copyright or license
located.
(from a simulation).
Exercise price
Cost of commercially
Up-front cost of
developing land today.
commercially utilizing
copyright or license today.
Life of the option
If land is under long-term lease,
Period for which you have
you could use the lease period.
rights to copyright or
If not, you should set the option
license.
life equal to the period when
the loan that you used to buy
the land comes due.
Cost of delay
Property taxes and other costs
Cash ﬂow you could
associated with holding land.
generate in next year as a
percent of present value of
the cash ﬂows today.
--- page 823 ---

still, and that the cost of opening up the mines will be $3 million (in present
value dollars). The capacity output rate is 400,000 pounds a year, and the price
of copper is expected to increase 4% a year. The Chilean government is willing
to grant a 25-year lease on the mine. The average production cost is expected to
be 40 cents a pound, and the current price per pound of copper is 85 cents. (The
production cost is expected to grow 3% a year, once initiated.) The annualized
standard deviation in copper prices is 25%, and the 25-year bond rate is 7%.
a. Estimate the value of the mine using traditional capital budgeting techniques.
b. Estimate the value of the mine based on an option pricing model.
c. How would you explain the difference between the two values?
3. You have been asked to analyze the value of an oil company with substantial oil
reserves. The estimated reserves amount to 10 million barrels, and the estimated
cost of developing these reserves today is $120 million. The current price of oil
is $20 per barrel, and the average production cost is estimated to be $6 per barrel. The company has the rights to these reserves for the next 20 years, and the
20-year bond rate is 7%. The company also proposes to extract 4% of its reserves each year to meet cash ﬂow needs. The annualized standard deviation in
the price of the oil is 20%. What is the value of this oil company?
4. You are analyzing a capital budgeting project. The project is expected to have a
PV of cash inﬂows of $250 million and will cost $200 million today to take on.
You have done a simulation of the project cash ﬂows, and the simulation yields
a variance in present value of cash inﬂows of 0.04. You have the rights to this
project for the next 20 years. The 20-year Treasury bond rate is 8%.
a. What is the value of the project based on traditional NPV?
b. What is the value of the project as an option?
c. Why are the two values different? What factor or factors determine the magnitude of this difference?
5. Cyclops Inc., a high-technology company specializing in state-of-the-art visual
technology, is considering going public. While the company has no revenues or
proﬁts yet on its products, it has a 10-year patent to a product that will enable
contact lens users to get no-maintenance lenses that will last for years. While the
product is technically viable, it is exorbitantly expensive to manufacture, and
the potential market for it will be relatively small currently. (A cash ﬂow analysis
of the project suggests that the present value of the cash inﬂows on the project, if
adopted now, would be $250 million, while the cost of the project will be $500
million.) The technology is rapidly evolving, and a simulation of alternative scenarios yields a wide range of present values, with an annualized standard deviation of 60%. The 10-year bond rate is 6%.
a. Estimate the value of this company.
b. How sensitive is this value estimate to the variance in project cash ﬂows?
What broader lessons would you draw from this analysis?
804
THE OPTION TO DELAY AND VALUATION IMPLICATIONS
--- page 824 ---

CHAPTER 29
The Options to Expand and to
Abandon: Valuation Implications
T
he preceding chapter noted that traditional discounted cash ﬂow valuation does
not consider the value of the option that many ﬁrms have to delay making an investment, and consequently understates the value of these investments. This chapter
considers two other options that are often embedded in investments (and consequently in the values of the ﬁrms that possess them). The ﬁrst of these is the option
to expand an investment not only in new markets but to new products, to take advantage of favorable conditions. We argue that this option may sometimes make
young start-up ﬁrms signiﬁcantly more valuable than the present value of their expected cash ﬂows. The second option is the option to abandon or scale down investments, which can reduce the risk and downside from large investments and
therefore make them more valuable.
THE OPTION TO EXPAND
Firms sometimes invest in projects because the investments allow them either to
make further investments or to enter other markets in the future. In such cases, we
can view the initial projects as yielding options allowing the ﬁrm to invest in other
projects, and these options have value. Put another way, a ﬁrm may accept a negative net present value on the initial project because of the possibility of high positive
net present values on future projects.
Payoff on the Option to Expand
The option to expand can be evaluated at the time the initial project is analyzed. Assume that this initial project will give the ﬁrm the right to expand and invest in a
new project in the future. Assessed today, the expected present value of the cash
ﬂows from investing in the future project is V, and the total investment needed for
this project is X. The ﬁrm has a ﬁxed time horizon, at the end of which it has to
make the ﬁnal decision on whether to make the future investment. Finally, the ﬁrm
cannot move forward on this future investment if it does not take the initial project.
This scenario implies the option payoffs shown in Figure 29.1. As you can see, at
the expiration of the ﬁxed time horizon the ﬁrm will expand into the new project if
the present value of the expected cash ﬂows at that point in time exceeds the cost of
expansion.
805
--- page 825 ---

Inputs to Value the Option to Expand
To understand how to estimate the value of the
option to expand, let us begin by recognizing that there are two linked projects. The
ﬁrst project generally has a negative net present value and is recognized as a poor investment, even by the ﬁrm investing in it. The second project is the potential to expand
that comes with the ﬁrst project. It is the second project that represents the underlying
asset for the option. The inputs have to be deﬁned accordingly:
■The present value of the cash ﬂows that you would generate if you were to invest in the second project today (the expansion option) is the value of the underlying asset—S in the option pricing model.
■If there is substantial uncertainty about the expansion potential, the present value
is likely to be volatile and change over time as circumstances change. It is the variance in this present value that you would want to use to value the expansion option. Since projects are not traded, you have to either estimate this variance from
simulations or use the variance in values of publicly traded ﬁrms in the business.
■The cost that you would incur up front, if you invest in the expansion today, is
the equivalent of the strike price.
■The life of the option is fairly difﬁcult to deﬁne, since there is usually no externally imposed exercise period. (This is in contrast to the patents valued in the
preceding chapter, which have a legal life that can be used as the option life.)
When valuing the option to expand, the life of the option will be an internal
constraint imposed by the ﬁrm on itself. For instance, a ﬁrm that invests on a
small scale in China might impose a constraint that it will either expand within
ﬁve years or pull out of the market. Why might it do so? There may be considerable costs associated with maintaining the small presence or the ﬁrm may
have scarce resources that have to be committed elsewhere.
■As with other real options, there may be a cost to waiting once the expansion
option becomes viable. That cost may take the form of cash ﬂows that will be
lost on the expansion project if it is not taken or a cost imposed on the ﬁrm until it makes its ﬁnal decision. For instance, the ﬁrm may have to pay a fee every
year until it makes its ﬁnal decision.
806
THE OPTIONS TO EXPAND AND TO ABANDON: VALUATION IMPLICATIONS
FIGURE 29.1
The Option to Expand a Project
--- page 826 ---

ILLUSTRATION 29.1:
Valuing an Option to Expand: Ambev and Guarana
Guarana is a very popular caffeine-based soft drink in Brazil, and Ambev is the Brazilian beverage
manufacturer that is the largest producer of Guarana in the world. Assume that Ambev is considering
introducing the drink into the United States and that it has decided to do so in two steps:
1. Ambev will initially introduce Guarana in just the large metropolitan areas of the United
States to gauge potential demand. The expected cost of this limited introduction is $500
million and the estimated present value of the expected cash ﬂows is only $400 million. In
other words, Ambev expects to have a negative net present value of $100 million on this ﬁrst
investment.
2. If the limited introduction turns out to be a success, Ambev expects to introduce Guarana to the
rest of the U.S. market. At the moment, though, the ﬁrm is not optimistic about this expansion
potential and believes that while the cost of the full-scale introduction will be $1 billion, the expected present value of the cash ﬂows is only $750 million (making this a negative net present
value investment as well).
At ﬁrst sight, investing in a poor project to get a chance to invest in an even poorer project may
seem like a bad deal, but the second investment does have a redeeming feature. It is an option and
Ambev will not make the second investment (of $1 billion) if the expected present value of the cash
ﬂows stays below that number. Furthermore, there is considerable uncertainty about the size and potential for this market, and the ﬁrm may well ﬁnd itself with a lucrative investment.
To estimate the value of the second investment as an option, we begin by ﬁrst identifying the underlying asset—the expansion project—and using the current estimate of expected value ($750 million) as the value of the underlying asset. Since the investment needed for the investment of $1 billion
is the exercise price, this option is an out-of-the-money option. The two most problematic assumptions relate to the variance in the value of the underlying asset and the life of the option:
■We estimated the average standard deviation of 35% in ﬁrm values of small, publicly traded beverage companies in the United States and assumed that this would be a good proxy for the standard deviation in the value of the expansion option.
■We assumed that Ambev would have a ﬁve-year window to make its decision. We admit that this
is an arbitrary constraint but, in the real world, it may be driven by any of the following:
Financing constraints (loans will come due).
Strategic prerogatives (you have to choose where your resources will be invested).
Personnel decisions (management has to be hired and put in place).
Based on these inputs, we had the following inputs to the option pricing model:
S = Present value of cash ﬂows from expansion option today = $750
K = Exercise price = $1,000
t = 5 years
Standard deviation in value = 35%
We used a riskless rate of 5% and derived the expected up and down movements from the standard deviation:
u = 1.4032
d = 0.6968
The binomial tree is presented in Figure 29.2.
The Option to Expand
807
--- page 827 ---

Using the replicating portfolio framework described in Chapter 5, we estimate the value of the
expansion option to be $203 million. This value can be added on to the net present value of the original project under consideration.
NPV of limited introduction = −500 + 400 = −$100 million
Value of option to expand = $203 million
NPV with option to expand = −$100 million + $203 million = $103 million
Ambev should go ahead with the limited introduction, even though it has a negative net present value,
because it acquires an option of much greater value as a consequence.
808
THE OPTIONS TO EXPAND AND TO ABANDON: VALUATION IMPLICATIONS
FIGURE 29.2
Binomial Tree—Ambev Expansion Option
--- page 828 ---

The Option to Expand
809
ESTIMATING VARIANCES FROM MONTE CARLO SIMULATIONS
It has been suggested a couple of times in the last two chapters that the variances to be used in real option pricing models be derived from simulations. A
Monte Carlo simulation requires the following three steps:
1. You deﬁne probability distributions for each of the key inputs that underlie the cash ﬂows, and the parameters of the distributions—the average
and the standard deviation, if it is a normal distribution, for instance.
2. In each simulation, you draw one outcome from each distribution and estimate the present value of the cash ﬂows based on these draws.
3. After repeated simulations you should have a distribution of present values. The mean of this distribution should be the expected value of the
project, and the standard deviation of the distribution can be used as the
variance in the value to value options on the project.
While the process of running these simulations is straightforward and there
are a number of software packages that exist that allow you to do this,1 we
would add the following notes of caution:
• The most difﬁcult step is estimating the probability distributions and parameters for the key variables. It is easier to do when a ﬁrm has had experience with similar projects in the past—a retail store considering a new
store, for instance—than for a new product or a new market. If the distributions that feed into a simulation are random, the output, impressive
though it might look on paper, is meaningless.
• The standard deviation or variance that you want to use in option pricing
models is a variance in value over time and not at a point in time. What is
the difference, you might ask? Market testing, for instance, provides a distribution for the market potential today and reﬂects estimation uncertainty. The market itself will evolve over time, and it is the variance in
that distribution that you would like to estimate.2
• You should estimate the standard deviation in the value of the project—
the sum of the present value of the cash ﬂows—rather than the standard
deviation in annual income or annual cash ﬂows.
1Crystal Ball and @Risk are both add-on packages to Excel that allow you to run simulations.
2You could, for instance, be fairly certain about the size of the market today—the variance
would be low or even zero—but be uncertain about what the market will look like a year from
now or three years from now. It is the latter variance that determines the value of the option.
expand.xls: This spreadsheet allows you to estimate the value of the option to
expand a project to cover new markets or new products, using the Black-Scholes
model.
--- page 829 ---

Problems in Valuing the Option to Expand
The practical considerations associated with estimating the value of the option to
expand are similar to those associated with valuing the option to delay. In most
cases, ﬁrms with options to expand have no speciﬁc time horizon by which they
have to make an expansion decision, making these open-ended options or, at best,
options with arbitrary lives. Even in those cases where a life can be estimated for
the option, neither the size nor the potential market for the product may be known,
and estimating either can be problematic. To illustrate, consider the Ambev example discussed earlier. While we adopted a period of ﬁve years, at the end of which
Ambev has to decide one way or another on its future expansion in United States, it
is entirely possible that this time frame is not speciﬁed at the time the initial investment is made. Furthermore, we have assumed that both the cost and the present
value of expansion are known at the time of the initial investment. In reality, the
ﬁrm may not have good estimates for either input before opening the ﬁrst store,
since it does not have much information on the underlying market.
Extensions and Implications of Expansion Options
The option to expand can be used by ﬁrms to rationalize investing in projects that
have negative net present values but provide signiﬁcant opportunities to enter new
markets or to sell new products. The option pricing approach adds rigor to this argument by estimating the value of these options, and it also provides insight into
those occasions when they are most valuable. The option to expand is clearly more
valuable for more volatile businesses with higher returns on projects (such as
biotechnology or computer software), than it is for stable businesses with lower returns (such as automobile production). We will consider three cases where the expansion option may yield useful insights—strategic acquisitions, research and
development expenses, and multistage projects.
Strategic Considerations in Acquisitions
In many acquisitions or investments, the
acquiring ﬁrm believes that the transaction will give it competitive advantages in
the future. These competitive advantages include:
■Entry into a large or growing market. An investment or acquisition may allow
the ﬁrm to enter a large or potentially large market much sooner than it otherwise would have been able to do so. A good example of this is the acquisition
of a Mexican retail ﬁrm by a U.S. ﬁrm, with the intent of expanding into the
Mexican market.
■Technological expertise. In some cases, the acquisition is motivated by the desire to acquire a proprietary technology that will allow the acquirer to either
expand its existing market or enter a new market.
■Brand name. Firms sometime pay large premiums over market price to acquire
ﬁrms with valuable brand names, because they believe that these brand names
can be used for expansion into new markets in the future.
While all these potential advantages may be used to justify large acquisition
premiums, not all of them create valuable options. Even if these advantages can be
viewed as valuable expansion options, the value has to be greater than the acquisition premium for stockholders to gain.
810
THE OPTIONS TO EXPAND AND TO ABANDON: VALUATION IMPLICATIONS
--- page 830 ---

Research, Development, and Test Market Expenses
Firms that spend considerable
amounts of money on research and development and test marketing are often
stymied when they try to evaluate these expenses, since the payoffs are in terms of
future investments. At the same time, there is the very real possibility that after the
money has been spent, the products or projects may turn out not to be viable; consequently, the expenditure must be treated as a sunk cost. In fact, R&D has the
characteristics of a call option—the amount spent on the R&D is the cost of the
call option, and the projects or products that might emerge from the research provide the payoffs on the options. If these products are viable (i.e., the present value
of the cash inﬂows exceeds the needed investment), the payoff is the difference between the two.
Several logical implications emerge from this view of R&D. First, other things
remaining equal, research expenditures should provide much higher value for ﬁrms
that are in volatile businesses, since the variance in product or project cash ﬂows is
positively correlated with the value of the call option. Thus, Minnesota Mining and
Manufacturing (3M), which expends a substantial amount on R&D on basic ofﬁce
products such as Post-it notes, should receive less option value for its research than
does Amgen, whose research primarily concerns biotechnology products.3 Second,
the value of research and the optimal amount to be spent on research will change
over time as businesses mature. The best example is the pharmaceutical industry:
Pharmaceutical companies spent most of the 1980s investing substantial amounts
in research and earning high returns on new products as health-care costs expanded. In the 1990s, however, as health-care costs started leveling off and the
business matured, many of these companies found that they were not getting the
same payoffs on research and started cutting back. Some companies moved research dollars from conventional drugs to biotechnology products, where uncertainty about future cash ﬂows remains high.
Multistage Projects/Investments
When entering new businesses or taking new investments, ﬁrms sometimes have the option to move in stages. While doing so may
reduce potential upside, it also protects the ﬁrm against downside risk by allowing it
at each stage to gauge demand and decide whether to go on to the next stage. In other
words, a standard project can be recast as a series of options to expand, with each
option being dependent on the previous one. There are two propositions that follow:
1. Some projects that are unattractive on a full-investment basis may be valuecreating if the ﬁrm can invest in stages.
2. Some projects that look attractive on a full-investment basis may become even
more attractive if taken in stages.
The gain in value from the options created by multistage investments has to be
weighed against the cost. Taking investments in stages may allow competitors who decide to enter the market on a full scale to capture the market. It may also lead to higher
costs at each stage, since the ﬁrm is not taking full advantage of economies of scale.
3This statement is based on the assumption that the quality of research is the same at both
ﬁrms, though the research is in different businesses, and that the only difference is in the
volatility of the underlying businesses.
The Option to Expand
811
--- page 831 ---

Several implications emerge from viewing this choice between multistage and
one-time investments in an option framework. The projects where the gains will be
largest from making the investment in multiple stages include:
■Projects where there are signiﬁcant barriers to entry to competitors entering the
market and taking advantage of delays in full-scale production. Thus a ﬁrm with a
patent on a product or other legal protection against competition pays a much
smaller price for starting small and expanding as it learns more about the market.
■Projects where there is uncertainty about the size of the market and the eventual success of the project. Here, starting small and expanding in stages allows
the ﬁrm to reduce its losses if the product does not sell as well as anticipated,
and to learn more about the market at each stage. This information can be useful in both product design and marketing in subsequent stages.
■Projects where there is a substantial investment needed in infrastructure and high
operating leverage (ﬁxed costs). Since the savings from doing a project in multiple stages can be traced to the investments needed at each stage, the beneﬁt is
likely to be greater in ﬁrms where those costs are large. Capital-intensive projects
as well as projects that require large initial marketing expenses (a new brand
name product for a consumer product company), for example, will gain more
from the options created by investing in the projects in multiple stages.
WHEN ARE EXPANSION OPTIONS VALUABLE?
While the argument that some or many investments have valuable strategic or expansion options embedded in them has great allure, there is a danger that this argument can be used to justify poor investments. In fact, acquirers have long justiﬁed
huge premiums on acquisitions on synergistic and strategic grounds. We need to be
812
THE OPTIONS TO EXPAND AND TO ABANDON: VALUATION IMPLICATIONS
SEQUENTIAL AND COMPOUND OPTIONS: SOME THOUGHTS
A compound option is an option on an option. A simple example would be a
call option on a small company that has only one asset—a patent. Last chapter, we argued that a patent could be viewed as an option, and thus the call
option on the company becomes a compound option. You can also have a sequence of options where the value of each option is dependent on whether the
previous option is exercised. For instance, a ﬁve-stage project has sequential
options. Whether you reach the ﬁfth stage is obviously a function of whether
you make it through the ﬁrst four stages; the value of the ﬁfth option in the sequence is determined by what happens to the ﬁrst four options.
Needless to say, option pricing becomes more complicated when you have
sequential and compound options. There are two choices. One is to value these
options as simple options and accept the fact that the value that you obtain
will be an approximation. The other is to modify the option pricing model to
allow for the special characteristics of these options. While we do not consider
these models in this book, you can modify both the Black-Scholes and binomial models to allow them to price compound and sequential options.
--- page 832 ---

more rigorous in our measurement of the value of real options and in our use of
real options as justiﬁcation for paying high prices or making poor investments.
Quantitative Estimation
When real options are used to justify a decision, the justiﬁcation has to be in more
than qualitative terms. In other words, managers who argue for investing in a project with poor returns or paying a premium on an acquisition on the basis of the
real options generated by this investment should be required to value these real options and show that the economic beneﬁts exceed the costs. There will be two arguments made against this requirement. The ﬁrst is that real options cannot be easily
valued, since the inputs are difﬁcult to obtain and often noisy. The second is that
the inputs to option pricing models can be easily manipulated to back up whatever
the conclusion might be. While both arguments have some basis, an estimate is better than no estimate at all, and the process of trying to estimate the value of a real
option is, in fact, the ﬁrst step to understanding what drives its value.
Tests for Expansion Option to Have Value
Not all investments have options embedded in them, and not all options, even if
they do exist, have signiﬁcant value. To assess whether an investment creates
valuable options that need to be analyzed and valued, we need to answer three
key questions.
1. Is the ﬁrst investment a prerequisite for the later investment/expansion? If not,
how necessary is the ﬁrst investment for the later investment/expansion? Consider our
earlier analysis of the value of a patent or the value of an undeveloped oil reserve as
options. A ﬁrm cannot generate patents without investing in research or paying another ﬁrm for the patents, and it cannot get rights to an undeveloped oil reserve without spending on exploration, bidding on it at a government auction, or buying it from
another oil company. Clearly, the initial investment here (spending on R&D, bidding
at the auction) is required for the ﬁrm to have the second investment. Now consider
the Ambev investment in a limited introduction and the option to expand into the U.S.
market later. The initial investment provides Ambev with information about market
potential, without which presumably it is unwilling to expand into the larger market.
Unlike the patent and undeveloped reserves examples, the initial investment is not a
prerequisite for the second, though management might view it as such. The connection gets even weaker, and the option value lower, when we look at one ﬁrm acquiring
another to have the option to be able to enter a large market. Acquiring a social media
company in order to have a foothold in the social media market or buying a Chinese
brewery to preserve the option to enter the Chinese beer market would be examples of
less defensible options.
2. Does the ﬁrm have an exclusive right to the later investment/expansion? If not,
does the initial investment provide the ﬁrm with signiﬁcant competitive advantages on
subsequent investments? The value of the option ultimately derives not from the cash
ﬂows generated by the second and subsequent investments, but from the excess returns generated by these cash ﬂows. The greater the potential for excess returns on the
second investment, the greater the value of the expansion option in the ﬁrst investment. The potential for excess returns is closely tied to how much of a competitive
When Are Expansion Options Valuable?
813
--- page 833 ---

advantage the ﬁrst investment provides the ﬁrm when it takes subsequent investments.
At one extreme, again, consider investing in research and development to acquire a
patent. The patent gives the ﬁrm that owns it the exclusive rights to produce that
product, and if the market potential is large, the right to the excess returns from the
project. At the other extreme, the ﬁrm might get no competitive advantages on subsequent investments, in which case, it is questionable as to whether there can be any excess returns on these investments. In reality, most investments will fall in the
continuum between these two extremes, with greater competitive advantages being associated with higher excess returns and larger option values.
3. Are the competitive advantages sustainable? In a competitive marketplace,
excess returns attract competitors, and competition drives down excess returns.
The more sustainable the competitive advantages possessed by a ﬁrm, the greater
will be the value of the options embedded in the initial investment. The sustainability of competitive advantages is a function of two forces. The ﬁrst is the nature of
the competition; other things remaining equal, competitive advantages fade much
more quickly in sectors where there are aggressive competitors. The second is the
nature of the competitive advantage. If the resource controlled by the ﬁrm is ﬁnite
and scarce (as is the case with natural resource reserves and vacant land), the competitive advantage is likely to be sustainable for longer periods. Alternatively, if the
competitive advantage comes from being the ﬁrst mover in a market or from having
technological expertise, it will come under assault far sooner. The most direct way
of reﬂecting this competitive advantage in the value of the option is to estimate the
period of competitive advantage, and only the excess returns earned over this period count toward the value of the option.
If the answer is yes to all three questions, then the option to expand can be valuable. Applying the last two tests to the Ambev expansion option, you can see the potential problems. While Ambev is the largest producer of Guarana in the world, it
does not have exclusivity on the product. If the initial introduction proves successful,
it is entirely possible that Coke and Pepsi could produce their own versions of
Guarana for the national market. If this occurs, Ambev will have expended $100 million of its funds to provide market information to its competitors. Thus, if Ambev
gets no competitive advantage in the expansion market because of its initial investment, the option to expand ceases to have value and cannot be used to justify the initial investment. Now consider two intermediate scenarios: If Ambev gets a lead time
on the expansion investment because of its initial investment, you could build in
higher cash ﬂows for that lead time and a fading off to lower cash ﬂows thereafter.
This will lower the present value of the cash ﬂows for the expansion and the value of
the option. A simpler adjustment would be to cap the present value of the cash ﬂows,
the argument being that competition will restrict how large the net present value can
become, and value the option with the cap. For instance, if you assume that the present value of the cash ﬂows from the expansion option cannot exceed $2 billion, the
value of the expansion option drops to $142 million.4
814
THE OPTIONS TO EXPAND AND TO ABANDON: VALUATION IMPLICATIONS
4You can value the capped call by valuing the expansion option twice in the Black-Scholes
model, once with a strike price of $1,000 (yielding the original expansion option value of
$218 million) and once with the strike price of $2,000 (yield an option value of $76 million).
The difference between the two is the value of the expansion option with a cap on the
present value. You could also value it explicitly in the binomial by setting the value to
$2,000 whenever it exceeds that number in the binomial tree.
--- page 834 ---

VALUING A FIRM WITH THE OPTION TO EXPAND
Is there an option to expand embedded in some ﬁrms that can lead to these ﬁrms to
trade at a premium over their discounted cash ﬂow values? At least in theory, there
is a rationale for making this argument for a small, high-growth ﬁrm in a large and
evolving market. The discounted cash ﬂow valuation is based on expected cash
ﬂows and expected growth and these expectations should reﬂect the probability
that the ﬁrm could be hugely successful (or a huge failure). What the expectations
might fail to consider is that, in the event of success, the ﬁrm could invest more,
add new products or expand into new markets and augment this success. This is
the real option that is creating the additional value.
Relationship to Discounted Cash Flow Valuation
If the value of this option to expand is estimated, the value of a ﬁrm can be written
as the sum of two components—a discounted cash ﬂow value based on expected
cash ﬂows and a value associated with the option to expand:
Value of ﬁrm = Discounted cash ﬂow value + Option to expand
The option pricing approach adds rigor to this argument by estimating the value
of the option to expand, and it also provides insight into those occasions when it is
most valuable. In general, the option to expand is clearly more valuable for more
volatile businesses with higher returns on projects and greater barriers to competitive entry (such as new technology), than in stable businesses with lower returns
(such as housing, utilities, or automobile production).
Again, though, you have to be careful not to double count the value of the option. If you use a higher growth rate than would be justiﬁed based on expectations
because of the option to expand, you have already counted the value of the option
in the discounted cash ﬂow valuation. Adding an additional component to reﬂect
the value of the option would be double counting.
Inputs for Valuing Expansion Option
To value a ﬁrm with the option to expand,
you have to begin by deﬁning the market that the ﬁrm has the option to enter and
specify the competitive advantages that you believe will give it some degree of exclusivity to make this entry. Once you are convinced that there is this exclusivity,
you should then estimate the expected cash ﬂows you would get if you entered
the market today and the cost of entering that market. Presumably, the costs will
exceed the expected cash ﬂows, or you would have entered the market already.
The cost of entering the market will become the exercise price of the option and
the expected cash ﬂows from entering the market today will become the value of
the underlying asset.
To estimate the variance in the value, you can either run simulations on how
the market will evolve over time or use the variances of publicly traded ﬁrms that
service that market today, and assume that this variance is a good proxy for the
volatility in the underlying market. You also have to specify a period by which you
have to make the decision of whether to enter the market; this will become the life
of the option. You may tie this assumption to the assumptions you made about
competitive advantages. For instance, if you have the exclusive license to enter a
market for the next 10 years, you would use 10 years as your option life.
Valuing a Firm with the Option to Expand
815
--- page 835 ---

ILLUSTRATION 29.2:
Valuing the Option to Expand: Secure Mail
Secure Mail is a young software company specializing in security software. Assume that you have
completed a conventional discounted cash ﬂow valuation of the company and estimated a value of
$111.54 million for the ﬁrm. However, there is the possibility that the company could use the customer base that it develops for the antivirus software and the technology on which the software is
based to create a database software program sometime in the next ﬁve years, and you have collected
the following information on the potential:
■It will cost Secure Mail about $500 million to develop a new database program if it decides to do it
today.
■Based on the information that Secure Mail has right now on the market for a database program,
the company can expect to generate about $40 million a year in after-tax cash ﬂows for 10 years.
The cost of capital for private companies that provide database software is 12%.
■The annualized standard deviation in ﬁrm value at publicly traded database companies is 50%.
■The ﬁve-year Treasury bond rate is 3%.
To value the expansion option, we used the information to derive the option inputs:
S = Value of the underlying asset
= PV of expected cash ﬂows from entering the database software market
K = Exercise price = Cost of entering the database software market = $500 million
t = Life of the option = Period over which expansion opportunity exists = 5 years
s = Standard deviation of underlying asset = 50%
r = Riskless rate = 3%
Inputting these numbers into the Black-Scholes model, we obtain the following:5
Value of call = S N(d1) −K e−rt N(d2)
= 226(0.4932) −500e−(.03) (5)(0.1282) = $56.30 million
Note that the numbers would not justify developing the database program today—the present value
of the expected cash ﬂows ($226 million) is well below the cost. However, Secure Mail has two
factors in its favor. The ﬁrst is that it can reﬁne its assessments of the market, based on how its
antivirus program performs. The second is that it can adapt the database program, based on the
information it collects, to increase the potential market and cash ﬂows.
If we accept this value for the expansion option, we should add it to the value that we derived for
Secure Mail earlier in the intrinsic valuation of $111.54 million. We would justify the use of the option
pricing model in this case by arguing that Secure Mail derives its exclusivity from its proprietary technology and access to customer lists (from its antivirus program).
5The values that we derive for d1 and d2 are as follows:
d2 = 0.0171 −0.50√5 = −1.1351
d1 =
(0.50)2
ln 226
500
+ 0.03  +
5
2
0.50 5
= 0.0171
today =
= $226 million
1 −
40
1
(1.12)10
0.12
816
THE OPTIONS TO EXPAND AND TO ABANDON: VALUATION IMPLICATIONS
--- page 836 ---

VALUE OF FINANCIAL FLEXIBILITY
When making ﬁnancial decisions, managers consider the effects of such decisions
on their capacity to make new investments or meet unanticipated contingencies in
future periods. Practically, this translates into ﬁrms maintaining excess debt capacity or larger cash balances than are warranted by current needs in order to meet unexpected future requirements. While maintaining this ﬁnancing ﬂexibility has value
to ﬁrms, it also has a cost; the large cash balances might earn below-market returns, and excess debt capacity implies that the ﬁrm is giving up some value and
has a higher cost of capital.
Determinants of the Value of Financial Flexibility
One reason that a ﬁrm maintains large cash balances and excess debt capacity is to
have the future option to take unexpected projects with high returns. To value ﬁ-
nancial ﬂexibility as an option, assume that a ﬁrm has expectations about how
much it will need to reinvest in future periods, based on its own past history and
current conditions in the industry. Assume also that a ﬁrm has expectations about
how much it can raise from internal funds and its normal access to capital markets
in future periods. There is uncertainty about future reinvestment needs; for simplicity, we will assume that the capacity to generate funds is known with certainty to
the ﬁrm. The advantage (and value) of having excess debt capacity or large cash
balances is that the ﬁrm can meet any reinvestment needs, in excess of funds available, using its debt capacity. The payoff from these projects, however, comes from
the excess returns the ﬁrm expects to make on them. To value ﬁnancial ﬂexibility
on an annualized basis, therefore, we will use the measures listed in Table 29.1.
Value of Financial Flexibility
817
expand.xls: This spreadsheet allows you to estimate the value of the option to
expand an investment or project.
TABLE 29.1
Inputs to Option Valuation: Financing Flexibility
Input to Model
Measure
Estimation Approach
S
Expected annual reinvestment
Use historical average of (Net cap ex +
needs as percent of ﬁrm value
Change in noncash working
capital)/Market value of ﬁrm
K
Annual reinvestment needs as
If ﬁrm does not want to or cannot use
percent of ﬁrm value that can
external ﬁnancing:
be raised without ﬁnancing
(Net income −Dividend + Depreciation)/
ﬂexibility
Market value of ﬁrm
If ﬁrm uses external capital (bank debt,
bonds, or equity) regularly:
(Net income + Depreciation + Net
external ﬁnancing)/Market value of
ﬁrm
σs
Variance in reinvestment needs
Variance in the reinvestment as percent
of ﬁrm value (using historical data)
t
1 year
To get an annual estimate of the value
of ﬂexibility
--- page 837 ---

ILLUSTRATION 29.3:
Valuing Financial Flexibility at the Home Depot in 1999
The Home Depot is a giant retail chain that sells home improvement products, primarily in the United
States. This ﬁrm traditionally has not been a heavy user of debt and has also grown at an extraordinary
rate over the past decade. To estimate the value of ﬁnancial ﬂexibility for the Home Depot, we began by
estimating reinvestments as a percent of ﬁrm value from 1989 to 1998 in the following table:
Reinvestment Needs
ln
as Percent of Firm
(Reinvestment
Year
Reinvestment Needs
Firm Value
Value
Needs)
1989
$ 175
$ 2,758
6.35%
−2.7574751
1990
$ 374
$ 3,815
9.80%
−2.3224401
1991
$ 427
$ 5,137
8.31%
−2.4874405
1992
$ 456
$ 7,148
6.38%
−2.7520951
1993
$ 927
$ 9,239
10.03%
−2.2992354
1994
$1,176
$12,477
9.43%
−2.3617681
1995
$1,344
$15,470
8.69%
−2.4432524
1996
$1,086
$19,535
5.56%
−2.8897065
1997
$1,589
$24,156
6.58%
−2.7214279
1998
$1,817
$30,219
6.01%
−2.8112841
Average reinvestment needs as % of ﬁrm value = 7.71%
Standard deviation in ln(Reinvestment needs) = 22.36%
We followed up by estimating internal funds as a percent of ﬁrm value, using the sum of net income
and depreciation as a measure of internal funds:
Internal Funds/
Year
Net Income
Depreciation
Firm Value
Value
1989
$ 112
$ 21
$ 2,758
4.82%
1990
$ 163
$ 34
$ 3,815
5.16%
1991
$ 249
$ 52
$ 5,137
5.86%
1992
$ 363
$ 70
$ 7,148
6.06%
1993
$ 457
$ 90
$ 9,239
5.92%
1994
$ 605
$130
$12,477
5.89%
1995
$ 732
$181
$15,470
5.90%
1996
$ 938
$232
$19,535
5.99%
1997
$1,160
$283
$24,156
5.97%
1998
$1,614
$373
$30,219
6.58%
Internal funds, on average, were 5.82% of ﬁrm value between 1989 and 1998. Since the ﬁrm uses almost no external debt, the ﬁrm made up the difference between its reinvestment needs (7.71%) and
internal fund generation (5.82%) by issuing equity. We will assume, looking forward, that the Home
Depot will no longer issue new equity.
The Home Depot’s current debt ratio is 4.55%, and its current cost of capital is 9.51%. Using the
cost of capital framework developed in Chapter 15, we estimated its optimal debt ratio to be 20%, and
its cost of capital at that debt level is 9.17%. Finally, the Home Depot in 1998 earned a return on capital of 16.37%, and we will assume that this is the expected return on new projects as well.
S = Expected reinvestment needs as percent of ﬁrm value = 7.71%
K = Reinvestment needs that can be ﬁnanced without ﬂexibility = 5.82%
t = 1 year
σ2 = Variance in ln(Net capital expenditures) = (.2237)2 = .05
818
THE OPTIONS TO EXPAND AND TO ABANDON: VALUATION IMPLICATIONS
