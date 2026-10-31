# INVESTMENT VALUATION TOOLS AND TECHNIQUES FOR DETERMINING -- Aswath Damodaran -- Wiley finance series, 3rd ed_, Hoboken, N_J, New Jersey, -- John -- isbn13 9781118011522 -- f84d1622bdc2de526da0dda803c52830 -- Anna’s.pdf — pages 191–210

--- page 191 ---

2. Assume that a company’s exposure to country risk is proportional to its exposure to all other market risk, which is measured by the beta. For Petrobras, this
would lead to a cost of equity estimate of:
Expected cost of equity = 3.50% + 0.80(4.31% + 4.82%) = 10.80%
This approach does differentiate between ﬁrms, but it assumes that betas that measure exposure to all other market risk measure exposure to country risk as well.
Thus, low-beta companies are less exposed to country risk than high-beta companies.
3. The most general approach, and our preferred approach, is to allow for each
company to have an exposure to country risk that is different from its exposure to
all other market risk. Measuring this exposure with λ, the cost of equity for any
ﬁrm is estimated as follows:
Expected return = Rf + Beta(Mature equity risk premium)
+ λ(Country risk premium)
How can we best estimate λ? This question is considered in far more detail in the
next chapter, but we would argue that commodity companies that get most of their
revenues in U.S. dollars14 by selling into a global market should be less exposed than
manufacturing companies that service the local market. Using this rationale, Petrobras, which derives most of its revenues in the global oil market in U.S. dollars,
should be less exposed than the typical Brazilian ﬁrm to country risk.15 Using a λ of
0.50, for instance, we get a cost of equity in U.S. dollar terms for Petrobras of:
Expected return = 3.5% + 0.80(4.31%) + 0.50(4.82%) = 9.36%
Note that the third approach essentially converts our expected return model to a
two-factor model, with the second factor being country risk, with λ measuring exposure to country risk. This approach also seems to offer the most promise in analyzing
companies with exposures in multiple countries like Coca-Cola and Nestlé. While these
ﬁrms are ostensibly developed market companies, they have substantial exposure to
risk in emerging markets, and their costs of equity should reﬂect this exposure. We
could estimate the country risk premiums for each country in which they operate and a
λ relative to each country, and use these to estimate a cost of equity for either company.
Alternative Approach: Implied Equity Premiums
There is an alternative to estimating risk premiums that does not require historical data or corrections for country risk, but does assume that the market,
172
RISKLESS RATES AND RISK PREMIUMS
14While I have categorized the revenues into dollar revenues and revenues in dollars, the
analysis can be generalized to look at revenues in stable currencies (e.g., the dollar, euro, etc.)
and revenues in risky currencies.
15λAracruz = % from local marketPR/% from local marketaverage Brazilian ﬁrm = 0.20/0.80 = 0.25.
ctryprem.xls: There is a dataset on the Web that contains the updated ratings for
countries and the risk premiums associated with each.
--- page 192 ---

overall, is correctly priced. Consider, for instance, a very simple valuation
model for stocks:
This is essentially the present value of dividends growing at a constant rate. Three
of the four inputs in this model can be obtained externally—the current level of the
market (value), the expected dividends next period, and the expected growth rate in
earnings and dividends in the long term. The only unknown is then the required return on equity; when we solve for it, we get an implied expected return on stocks.
Subtracting the risk-free rate will yield an implied equity risk premium.
To illustrate, assume that the current level of the S&P 500 index is 900, the expected dividend yield on the index is 2 percent, and the expected growth rate in
earnings and dividends in the long term is 7 percent. Solving for the required return
on equity yields the following:
900 = (.02 × 900)/(r – .07)
Solving for r,
r = (18 + 63)/900 = 9%
If the current risk-free rate is 6 percent, this will yield a premium of 3 percent.
This approach can be generalized to allow for high growth for a period, and extended to cover cash ﬂow–based, rather than dividend, models. To illustrate this, consider the S&P 500 index as of January 1, 2011. The index was at 1257.64, and the
cash ﬂows from dividends and stock buybacks during the course of 2010 were 53.96.
In addition, the consensus estimate16 of growth in earnings for companies in the index was approximately 6.95 percent for the next ﬁve years. Since this is not a growth
rate that can be sustained forever, we employ a two-stage valuation model, where we
allow growth to continue at 6.95 percent for ﬁve years, and then lower the growth
rate to the Treasury bond rate of 3.29 percent after that.17 The following table summarizes the expected cash ﬂows for the next ﬁve years of high growth and the ﬁrst
year of stable growth thereafter:
Year
Cash Flow on Index
1
53.96(1.0695) = 57.72
2
57.72(1.0695) = 61.73
3
61.73(1.0695) = 66.02
4
66.02(1.0695) = 70.60
5
70.60(1.0695) = 75.51
6
75.51(1.0329) = 77.99
Value =
Expected dividends next period
Required return on equity − Expected growth rate
Equity Risk Premium
173
16We used the average of the analyst estimates for individual ﬁrms (bottom-up). Alternatively,
we could have used the top-down estimate for the S&P 500 earnings (from economists).
17The Treasury bond rate is the sum of expected inﬂation and the expected real rate. If we assume that real growth is equal to the real rate, the long-term stable growth rate should be
equal to the Treasury bond rate.
--- page 193 ---

If we assume that these are reasonable estimates of the cash ﬂows and that the index is correctly priced, then:
Level of the index = 1,257.64 = 57.72/(1 + r) + 61.73/(1 + r)2 + 66.02/(1 + r)3
+ 70.60/(1 + r)4 + [75.51 + 77.99/(r – .0329)]/(1 + r)5
Note that the last term in the equation is the terminal value of the index, based on
the stable growth rate of 3.29 percent, discounted back to the present. Solving for r
in this equation yields us the required return on equity of 8.49 percent. Netting out
the Treasury bond rate of 3.29 percent yields an implied equity premium of 5.20
percent.
The advantage of this approach is that it is market-driven and current, and does
not require any historical data. Thus, it can be used to estimate implied equity premiums in any market. It is, however, bounded by whether the model used for the
valuation is the right one and by the availability and reliability of the inputs to that
model. For instance, the equity risk premium for the Brazilian market on September
30, 2009, was estimated from the following inputs. The index (Bovespa) was at
61,172, and the aggregate cash ﬂow yield on the index was 4.95 percent. Earnings
in companies in the index are expected to grow 6 percent (in U.S. dollar terms) over
the next ﬁve years, and 3.45 percent thereafter. These inputs yield a required return
on equity of 9.17 percent, which when compared to the U.S. Treasury bond rate of
3.45 percent on that day results in an implied equity premium of 5.72 percent. For
simplicity, we have used nominal dollar expected growth rates18 and Treasury bond
rates, but this analysis could have been done entirely in the local currency.
The implied equity premiums change over time as stock prices, earnings, and
interest rates change. In fact, the contrast between these premiums and the historical premiums is best illustrated by graphing out the implied premiums in the S&P
500 going back to 1960 in Figure 7.1. In terms of mechanics, smoothed historical
growth rates in earnings and dividends were used as projected growth rates, and a
two-stage dividend discount model was used. Looking at these numbers, the following conclusions would be drawn:
■The arithmetic average historical risk premium, which is used by many practitioners, has been higher than the implied premium over almost the entire 50-year
period (with 2009 the only exception). The geometric premium does provide a
more interesting mix of results, with implied premiums exceeding historical premiums in the mid-1970s and again following 2008.
■The implied equity premium did increase during the 1970s, as inﬂation increased. This does have interesting implications for risk premium estimation.
Instead of assuming that the risk premium is a constant and unaffected by the
level of inﬂation and interest rates, which is what we do with historical risk
premiums, it may be more realistic to increase the risk premium if expected in-
ﬂation and interest rates go up.
174
RISKLESS RATES AND RISK PREMIUMS
18The input that is most difﬁcult to estimate for emerging markets is a long-term expected
growth rate. For Brazilian stocks, I used the average consensus estimate of growth in earnings for the largest Brazilian companies that have American depositary receipts (ADRs) listed
on them. This estimate may be biased as a consequence.
--- page 194 ---

■While historical risk premiums have generally drifted down for the last few
decades, there is a strong tendency toward mean reversion in implied equity
premiums. Thus, the premium, which peaked at 6.5 percent in 1978, moved
down toward the average in the 1980s. By the same token, the premium of
2 percent that we observed at the end of the dot-com boom in the 1990s
quickly reverted back to the average during the market correction from
2000 to 2003. Given this tendency, it is possible that we can end up with a
far better estimate of the implied equity premium by looking at not just the
current premium, but also at historical trend lines.
Finally, the crisis of 2008 was unprecedented in terms of its impact on equity
risk premiums. Implied equity risk premiums rose more during 2008 than in any
one of the prior 50 years. Much of that change occurred in the last 15 weeks of the
year when the US and other developed markets went through gyrations more typical of emerging markets. A large portion of that increase dissipated in 2009 but returned again in 2010 and 2011.
As a ﬁnal point, there is a strong tendency toward mean reversion in
ﬁnancial markets. Given this tendency, it is possible that we can end up with a
far better estimate of the implied equity premium by looking not just at the current premium but also at historical data. There are two ways in which we can do
this:
1. We can use the average implied equity premium over longer periods, say 10 to
15 years. Note that we do not need as many years of data here as we did with
the historical premium estimate, because the standard errors tend to be
smaller.
2. A more rigorous approach would require relating implied equity risk premiums to fundamental macroeconomic data over the period. For instance, given
Equity Risk Premium
175
FIGURE 7.1
Implied Premiums for U.S. Equity Market (1960 to 2010)
0.00%
1960
1961
1962
1963
1964
1965
1966
1967
1968
1969
1970
1971
1972
1973
1974
1975
1976
1977
1978
1979
1980
1981
1982
1983
1984
Year
1985
1986
1987
1988
1989
1990
1991
1992
1993
1994
1995
1996
1997
1998
2099
2000
2001
2002
2003
2004
2005
2006
2007
2008
2009
2010
1.00%
2.00%
3.00%
4.00%
5.00%
6.00%
7.00%
Implied Premium
--- page 195 ---

that implied equity premiums tend to be higher during periods with higher in-
ﬂation rates (and interest rates), we ran a regression of implied equity premiums against Treasury bond rates between 1960 and 2010:
Implied equity premium = 2.97% + 0.2903(T-bond rate)
[2.89]
The regression has some explanatory power, with an R-squared of 15 percent,
and the t statistics (in brackets under the coefﬁcients) indicate the statistical signiﬁ-
cance of the independent variable used. Substituting the current Treasury bond rate
into this equation should yield an updated estimate19 of the implied equity premium.
176
RISKLESS RATES AND RISK PREMIUMS
19On April 30, 2011, for instance, I substituted the Treasury bond rate of 3.5 percent  into
the regression equation to get:
.0297 + .149(.035) = .0349 or 3.49%
HISTORICAL VERSUS IMPLIED EQUITY PREMIUMS: EFFECT OF MARKET VIEWS
As you can see from the preceding discussion, historical premiums can be very
different from implied equity premiums. At the end of 2000, the historical risk
premium for stocks over bonds in the United States was 5.51 percent, whereas
the implied equity risk premium was 2.87 percent. In contrast, at the end of
2008, the historical risk premium was 3.88%, whereas the implied premium
was 6.43%. When doing discounted cash ﬂow valuation, you have to decide
which risk premium you will use in the valuation, and your choice will be determined by both your market views and your valuation mission.
Market Views: If you believe that the market is right in the aggregate,
though it may make mistakes on individual stocks, the risk premium you
should use is the current implied equity risk premium. If you believe that the
market often makes mistakes in the aggregate and that risk premiums in markets tend to move back to historical norms (mean reversion), you should go
with the historical premium (4.31 percent at the end of 2000). A way to split
the difference is to assume that markets are right across time, though they
may make mistakes at individual points in time. If you make this assumption,
you should use an average implied equity risk premium over time. The average implied equity risk premium from 1960 to 2010 is 3.95 percent. While
this book uses the historical premium a few times in its valuations, it sticks
with the average implied premium in most of the valuations.
Valuation mission: If your valuation requires you to be market neutral,
you should use the current implied equity risk premium. This is often the case
if you are an equity research analyst or if you have to value a company for an
acquisition.
histimpl.xls: This dataset on the Web shows the inputs used to calculate the
premium in each year for the U.S. market.
--- page 196 ---

DEFAULT SPREADS ON BONDS
The interest rates on bonds are determined by the default risk that investors perceive in the issuer of the bonds. This default risk is often measured with a bond
rating, and the interest rate that corresponds to the rating is estimated by adding
a default spread to the riskless rate. In Chapter 4, we examined the process used
by rating agencies to rate ﬁrms. This chapter considers how to estimate default
spreads for a given ratings class and why these spreads may change over time.
Estimating Default Spreads
The simplest way to estimate default spreads for each ratings class is to ﬁnd a sampling of bonds within that ratings class and obtain the current market interest rate
on these bonds. Why do we need a sampling rather than just one bond? A bond can
be misrated or mispriced. Using a sample reduces or eliminates this problem. In obtaining this sample, you should try to focus on the most liquid bonds with as few
special features attached to them as possible. Corporate bonds are often illiquid and
the interest rates on such bonds may not reﬂect current market rates. The presence
of special features on bonds such as convertibility can affect the pricing of these
bonds and consequently the interest rates estimated on them.
Once a sample of bonds within each ratings class has been identiﬁed, you need
to estimate the interest rate on these bonds. There are two measures that are widely
used. The ﬁrst is the yield on the bond, which is the coupon rate divided by the
market price. The second is the yield to maturity on the bond, which is the interest
rate that makes the present value of the coupons and face value of the bond equal
to the market price. In general, it is the yield to maturity that better measures the
market interest rate on the bond.
Having obtained the interest rates on the bonds in the sample, you have two
decisions to make. The ﬁrst relates to weighting. You could compute a simple average of the interest rates of the bonds in the sample or a weighted average, with the
weights based upon the trading volume—more liquid bonds will be weighted more
than less liquid bonds. The second relates to the index Treasury rate, since the average interest rate for a ratings class is compared to this rate to arrive at a default
spread. In general, the maturity of the Treasury should match the average maturity
of the corporate bonds chosen to estimate the average interest rate. Thus, the average interest rate for ﬁve-year BBB-rated corporate bonds should be compared to the
average interest rate for ﬁve-year Treasuries to derive the spread for the BBB-rated
bonds.
Publications like Barron’s have historically provided interest rates on at least
higher-rated bonds (BBB or higher), an increasing number of online services provide the same information today for all rated bonds. Table 7.6 is extracted from
one such online service in early 2011 for 10-year bonds  using a 10-year T Bond
rate of 3.5% as the riskfree rate.
Default Spreads on Bonds
177
implprem.xls: This spreadsheet allows you to estimate the implied equity premium
in a market.
--- page 197 ---

Determinants of Default Spreads
Table 7.6 provides default spreads at a point in time, but default spreads not only
vary across time, but they also can vary for bonds with the same rating but different maturities. This section considers how default spreads vary across time and for
bonds with varying maturities.
Default Spreads and Bond Maturity
Empirically, the default spread for corporate
bonds of a given ratings class seems to increase with the maturity of the bond.
Figure 7.2 presents the default spreads estimated for Aaa, Baa, and Caa-rated
bonds for maturities ranging from 1 to 30 years in January 2011.
At least there seems to be no perceptible pattern to default spreads over maturity in 2011. Thus, the default spread on the 10-year bond is not noticeably larger
than the default spread on a 1-year bond. This has not always been the case. There
have been some periods in history where default spreads were an increasing function of maturity and other periods where they were a decreasing function.
Default Spreads over Time
The default spreads presented in Table 7.6, after a year of
declining markets and a slowing economy, were signiﬁcantly higher than the default
spreads a year earlier. This phenomenon is not new. Historically, default spreads for
every ratings class have increased during recessions and decreased during economic
booms. Figure 7.3 graphs the spread between 10-year Moody’s Baa-rated bonds and
the 10-year Treasury bond rate each year from 1960 to 2010 and contrasts it with the
implied equity risk premium each year. The default spreads did increase during periods
of low economic growth; note the increase during 1973–1974 and 1979–1981 in particular. Although default spreads and equity risk premiums in most periods have generally moved in tandem, there have been exceptional periods when they moved in
different directions. In the late 1990s, for instance, the dot-com boom in stock prices
178
RISKLESS RATES AND RISK PREMIUMS
TABLE 7.6
Default Spreads and Interest Rates — January 2011
Bond Rating
Default Spread
Interest Rate on Debt
AAA
0.50%
4.00%
AA
0.65%
4.15%
A+
0.85%
4.35%
A
1.00%
4.50%
A–
1.10%
4.60%
BBB
1.60%
5.10%
BB+
3.00%
6.50%
BB
3.35%
6.85%
B+
3.75%
7.25%
B
5.00%
8.50%
B–
5.25%
8.75%
CCC
8.00%
11.50%
CC
10.00%
13.50%
C
12.00%
15.50%
D
15.00%
18.50%
Source: BondsOnline.com.
--- page 198 ---

Default Spreads on Bonds
179
FIGURE 7.2 Default Spreads by Maturity—January 2011
Source: BondsOnline.com.
1
0.00%
1.00%
2.00%
3.00%
4.00%
5.00%
6.00%
7.00%
8.00%
9.00%
2
3
5
7
Maturity (Years)
10
30
Aaa
Baa
Caa
FIGURE 7.3
Baa Bond Default Spread and Implied Equity Risk Premiums: 1960 to 2010
1960
0.00%
1.00%
2.00%
3.00%
Premium (Spread)
4.00%
5.00%
6.00%
7.00%
1962
1964
1966
1968
1970
1972
1974
1976
1978
1980
1982
1984
1986
1988
1990
1992
1994
1996
1998
2000
2002
2004
2006
2008
2010
Baa Default Spread
ERP
--- page 199 ---

resulted in declining equity risk premiums, while default spreads stayed relatively stable. In contrast, the subprime boom in 2004 to 2007 lowered default spreads, while
equity risk premiums stayed unchanged.
CONCLUSION
The risk-free rate is the starting point for all expected return models. For an asset to
be risk free, it has to be free of both default and reinvestment risk. Using these criteria, the appropriate risk-free rate to use to obtain expected returns should be a
default-free (government) zero coupon rate that is matched up to when the cash
ﬂow that is being discounted occurs. In practice, however, it is usually appropriate
to match up the duration of the risk-free asset to the duration of the cash ﬂows being analyzed. In valuation, this will lead us toward long-term government bond
rates as risk-free rates. It is also important that the risk-free rate be consistent with
the cash ﬂows being discounted. In particular, the currency in which the risk-free
rate is denominated and whether it is a real or nominal risk-free rate should be determined by the currency in which the cash ﬂows are estimated and whether the estimation is done in real or nominal terms.
The risk premium is a fundamental and critical component in portfolio management, corporate ﬁnance, and valuation. Given its importance, it is surprising that
more attention has not been paid in practical terms to estimation issues. This chapter
considered the conventional approach to estimating risk premiums, which is to use
historical returns on equity and government securities, and evaluated some of its
weaknesses. It also examined how to extend this approach to emerging markets,
where historical data tends to be both limited and volatile. The alternative to historical premiums is to estimate the equity premium implied by equity prices. This approach does require that we start with a valuation model for equities, and estimate
the expected growth and cash ﬂows, collectively, on equity investments. It has the advantages of not requiring historical data and of reﬂecting current market perceptions.
QUESTIONS AND SHORT PROBLEMS
In the problems following, use an equity risk premium of 5.5 percent if none is
speciﬁed.
1. Assume that you are valuing an Indonesian ﬁrm in U.S. dollars. What would
you use as the riskless rate?
2. Explain why a six-month Treasury bill rate is not an appropriate riskless rate in
discounting a ﬁve-year cash ﬂow.
3. You have been asked to estimate a riskless rate in Indonesian rupiah. The Indonesian government has rupiah-denominated bonds outstanding, with an interest
rate of 17%. S&P has a rating of BB on these bonds, and the typical spread for a
BB-rated country is 5% over a riskless rate. Estimate the rupiah riskless rate.
180
RISKLESS RATES AND RISK PREMIUMS
ratings.xls: This dataset on the Web summarizes default spreads by bond rating
class for the most recent period.
--- page 200 ---

4. You are valuing an Indian company in rupees. The current exchange rate is Rs
45 per dollar and you have been able to obtain a 10-year forward rate of Rs 70
per dollar. If the U.S. Treasury bond rate is 5%, estimate the riskless rate in Indian rupees.
5. You are attempting to do a valuation of a Chilean company in real terms. While
you have been unable to get a real riskless rate in Latin America, you know that
inﬂation-indexed Treasury bonds in the United States are yielding 3%. Could
you use this as a real riskless rate? Why or why not? What are the alternatives?
6. Assume you have estimated the historical risk premium, based on 50 years of
data, to be 6%. If the annual standard deviation in stock prices is 30%, estimate
the standard error in the risk premium estimate.
7. When you use a historical risk premium as your expected future risk premium,
what are the assumptions that you are making about investors and markets? Under what conditions would a historical risk premium give you too high a number (to use as an expected premium)?
8. You are trying to estimate a country equity risk premium for Poland. You ﬁnd
that S&P has assigned an A rating to Poland and that Poland has issued eurodenominated bonds that yield 7.6% in the market currently. (Germany, a AAArated country, has euro-denominated bonds outstanding that yield 5.1%.)
a. Estimate the country risk premium, using the default spread on the country
bond as the proxy.
b. If you were told that the standard deviation in the Polish equity market was
25% and that the standard deviation in the Polish euro bond was 15%, estimate the country risk premium.
9. The standard deviation in the Mexican Equity Index is 48%, and the standard
deviation in the S&P 500 is 20%. You use an equity risk premium of 5.5% for
the United States.
a. Estimate the country equity risk premium for Mexico using relative equity
standard deviations.
b. Now assume that you are told that Mexico is rated BBB by Standard &
Poor’s and that it has dollar-denominated bonds outstanding that trade at a
spread of about 3% above the Treasury bond rate. If the standard deviation
in these bonds is 24%, estimate the country risk premium for Mexico.
10. The S&P 500 is at 1,400. The expected dividends and cash ﬂows next year on
the stocks in the index are expected to be 5% of the index. If the expected
growth rate in dividends and cash ﬂows over the long term is expected to be
6% and the riskless rate is 5.5%, estimate the implied equity risk premium.
11. The Bovespa (Brazilian equity index) is at 15,000. The dividends on the index
last year were 5% of the index value, and analysts expect them to grow 15% a
year in real terms for the next ﬁve years. After the ﬁfth year, the growth is expected to drop to 5% in real terms in perpetuity. If the real riskless rate is 6%,
estimate the implied equity risk premium in this market.
12. As stock prices go up, implied equity risk premiums will go down. Is this statement always true? If not, when is it not true?
Questions and Short Problems
181
--- page 201 ---

182
CHAPTER 8
Estimating Risk Parameters
and Costs of Financing
T
he preceding chapter laid the groundwork for estimating the costs of equity and
capital for ﬁrms by looking at how best to estimate a riskless rate that operates as
a base for all costs, an equity risk premium for estimating the cost of equity, and default spreads for estimating the cost of debt. It did not, however, consider how to estimate the risk parameters for individual ﬁrms. This chapter examines the process of
estimating risk parameters for individual ﬁrms, for estimating both the cost of equity and the cost of debt.
For the cost of equity, we look at the standard process of estimating the beta for
a ﬁrm and consider alternative approaches. For the cost of debt, we examine bond
ratings as measures of default risk and the determinants of these ratings.
The chapter closes by bringing together the risk parameter estimates for individual ﬁrms and the economy-wide estimates of the risk-free rate and risk premiums
to estimate a cost of capital for the ﬁrm. To do this, the sources of capital have to be
weighted by their relative market values.
THE COST OF EQUITY AND CAPITAL
Firms raise money from both equity investors and lenders to fund investments. Both
groups of investors make their investments expecting to make a return. Chapter 4
argued that the expected return for equity investors would include a premium for
the equity risk in the investment. We label this expected return the cost of equity.
Similarly, the expected return that lenders hope to make on their investments includes a premium for default risk, and we call that expected return the cost of debt.
If we consider all of the ﬁnancing that the ﬁrm takes on, the composite cost of ﬁ-
nancing will be a weighted average of the costs of equity and debt, and this
weighted cost is the cost of capital.
The chapter begins by estimating the equity risk in a ﬁrm and using the equity
risk to estimate the cost of equity, and follows up by measuring the default risk to
estimate a cost of debt. It concludes by determining the weights we should attach to
each of these costs to arrive at a cost of capital.
--- page 202 ---

COST OF EQUITY
The cost of equity is the rate of return investors require on an equity investment in
a ﬁrm. The risk and return models described in Chapter 4 need a riskless rate and a
risk premium (in the CAPM) or premiums (in the APM and multifactor models),
which were estimated in the last chapter. They also need measures of a ﬁrm’s exposure to market risk in the form of betas. These inputs are used to arrive at an expected return on an equity investment:
Expected return = Riskless rate + Beta(Risk premium)
This expected return to equity investors includes compensation for the market risk
in the investment and is the cost of equity. This section concentrates on the estimation of the beta of a ﬁrm. While much of the discussion is directed at the CAPM, it
can be extended to apply to the arbitrage pricing and multifactor models, as well.
Betas
In the CAPM, the beta of an investment is the risk that the investment adds to a
market portfolio. In the APM and multifactor model, the betas of the investment
relative to each factor have to be measured. There are three approaches available
for estimating these parameters: One is to use historical data on market prices for
individual investments; the second is to estimate the betas from the fundamental
characteristics of the investment; and the third is to use accounting data. All three
approaches are described in this section.
Historical Market Betas
The conventional approach for estimating the beta of an
investment is a regression of returns on the investment against returns on a market
index. For ﬁrms that have been publicly traded for a length of time, it is relatively
straightforward to estimate returns that an investor would have made on investing
in the ﬁrms’ equity in intervals (such as a week or a month) over that period. In theory, these stock returns on the assets should be related to returns on a market portfolio (i.e., a portfolio that includes all traded assets) to estimate the betas of the
assets. In practice, we tend to use a stock index such as the S&P 500 as a proxy for
the market portfolio, and we estimate betas for stocks against the index.
Regression Estimates of Betas
The standard procedure for estimating betas is to
regress stock returns (Rj) against market returns (Rm):
Rj = a + b Rm
where a = Intercept from the regression
b = Slope of the regression = Covariance(Rj, Rm)/σ2
m
The slope of the regression corresponds to the beta of the stock and measures the
riskiness of the stock.
The intercept of the regression provides a simple measure of performance of
the investment during the period of the regression, when returns are measured
Cost of Equity
183
--- page 203 ---

against the expected returns from the capital asset pricing model. To see why, consider the following rearrangement of the capital asset pricing model:
Rj = Rf + β(Rm – Rf)
= Rf(1 – β) + β Rm
Compare this formulation of the return on an investment to the return equation
from the regression:
Rj = a + b Rm
Thus, a comparison of the intercept a to Rf(1 – β) should provide a measure of the
stock’s performance, at least relative to the capital asset pricing model.1 In summary, then:
If a > Rf(1 – β) . . . Stock did better than expected during regression period.
a = Rf(1 – β) . . . Stock did as well as expected during regression period.
a < Rf(1 – β) . . . Stock did worse than expected during regression period.
The difference between a and Rf(1 – β) is called Jensen’s alpha2 and provides a
measure of whether the investment in question earned a return greater than or less
than its required return, given both market performance and risk. For instance, a
ﬁrm that earned 15 percent during a period when ﬁrms with similar betas earned
12 percent will have earned an excess return of 3 percent; its intercept will also exceed Rf(1 – β) by 3 percent.
The third statistic that emerges from the regression is the R-squared (R2) of
the regression. While the statistical explanation of the R-squared is that it
provides a measure of the goodness of ﬁt of the regression, the economic rationale is that it provides an estimate of the proportion of the risk of a ﬁrm that can
be attributed to market risk; the balance (1 – R2) can then be attributed to ﬁrmspeciﬁc risk.
The ﬁnal statistic worth noting is the standard error of the beta estimate. The
slope of the regression, like any statistical estimate, may be different from the true
value, and the standard error reveals just how much error there could be in the estimate. The standard error can also be used to arrive at conﬁdence intervals for the
“true” beta value from the slope estimate.
184
ESTIMATING RISK PARAMETERS AND COSTS OF FINANCING
1The regression is sometimes calculated using returns in excess of the riskless rate for both
the stock and the market. In that case, the intercept of the regression should be zero if the actual returns equal the expected returns from the CAPM, greater than zero if the stock does
better than expected, and less than zero if it does worse than expected.
2The terminology is confusing, since the intercept of the regression is sometimes also called
the alpha and is sometimes compared to zero as a measure of risk-adjusted performance. The
intercept can be compared to zero only if the regression is run with excess returns for both
the stock and the index; the riskless rate has to be subtracted from the raw return in each
month for both.
--- page 204 ---

ILLUSTRATION 8.1:
Estimating a Regression Beta for Boeing
Boeing Company is a ﬁrm in both the aerospace and defense businesses, and has been traded on the
New York Stock Exchange (NYSE) for decades. In assessing risk parameters for Boeing, we compute
the returns on the stock and the market index in two steps:
1. The returns to a stockholder in Boeing are computed month by month from January 1996 to
December 2000. These returns include both dividends and price appreciation and are deﬁned
as follows:
Stock returnBoeing, j = (PriceBoeing, j – PriceBoeing, j–1 + Dividendsj)/PriceBoeing, j–1
where Stock returnBoeing,j = Returns to a stockholder in Boeing in month j
PriceBoeing, j = Price of Boeing stock at the end of month j
Dividendsj = Dividends on Boeing stock in month j
Dividends are added to the returns of the month in which stockholders are entitled to the dividend.3
2. The returns on the S&P 500 market index are computed for each month of the period, using the
level of the index at the end of each month and the monthly dividend on stocks in the index.
Market returnj = (Indexj – Indexj–1 + Dividendsj)/Indexj–1
where indexj is the level of the index at the end of month j and dividendsj is the dividends paid on
the index in month j. Although the S&P 500 and the NYSE Composite are the most widely used
indexes for U.S. stocks, they are, at best, imperfect proxies for the market portfolio in the CAPM,
which is supposed to include all assets.
Figure 8.1 graphs monthly returns on Boeing against returns on the S&P 500 index from January 1996 to December 2000.
The regression statistics for Boeing are as follows:
(a) Slope of the regression = 0.56. This is Boeing’s beta, based on monthly returns from 1996 to
2000. Using a different time period for the regression or different return intervals (weekly or daily) for
the same period can result in a different beta.
(b) Intercept of the regression = 0.54%. This is a measure of Boeing’s performance, when it is
compared with Rf(1 – β). The monthly riskless rate (since the returns used in the regression are
monthly returns) between 1996 and 2000 averaged 0.4%, resulting in the following estimate for the
performance:
Rf(1 – β) = 0.4%(1 – 0.56) = 0.18%
Intercept – Rf(1 – β) = 0.54% – 0.18% = 0.36%
This analysis suggests that Boeing performed 0.36% better than expected, when expectations are
based on the CAPM, on a monthly basis between January 1996 and December 2000. This results in
an annualized excess return of approximately 4.41%.
Annualized excess return = (1 + Monthly excess return)12 – 1
= (1 – .0036)12 – 1 = 4.41%
Note, however, that this does not imply that Boeing would be a good investment in the future.
Cost of Equity
185
3The stock has to be bought by a day called the ex-dividend day in order for investors to be entitled to dividends.
The returns in a period include dividends if the ex-dividend day is in that period.
--- page 205 ---

The performance measure also does not provide a breakdown of how much of this excess return can
be attributed to the performance of the entire sector (aerospace and defense) and how much is speciﬁc to the ﬁrm. To make that breakdown, we would need to compute the excess over the same period for other ﬁrms in the aerospace and defense industry and compare them with Boeing’s excess
return. The difference would then be attributable to ﬁrm-speciﬁc actions. In this case, for instance,
the average annualized excess return on other aerospace/defense ﬁrms between 1996 and 2000 was
–0.85%, suggesting that the ﬁrm-speciﬁc component of performance for Boeing is actually 5.26%
[ﬁrm-speciﬁc Jensen’s alpha = 4.41% – (–0.85%)].
(c) R-squared of the regression = 9.43%. This statistic suggests that 9.43% of the risk (variance) in Boeing comes from market sources, and that the balance of 90.57% of the risk comes from
ﬁrm-speciﬁc components. The latter risk should be diversiﬁable and therefore will not be rewarded
with a higher expected return. Boeing’s R-squared is lower than the median R-squared of companies
listed on the New York Stock Exchange, which was approximately 19% in 2000.
(d) Standard error of beta estimate = 0.23. This statistic implies that the true beta for Boeing
could range from 0.33 to 0.79 (subtracting and adding one standard error to beta estimate of 0.56)
with 67% conﬁdence and from 0.10 to 1.02 (subtracting and adding two standard errors to beta estimate of 0.56) with 95% conﬁdence. While these ranges may seem large, they are not unusual for
most U.S. companies. This suggests that we should consider estimates of betas from regressions
with caution.
Using a Service Beta
Most of us who use betas obtain them from an estimation
service; Merrill Lynch, Barra, Value Line, Standard & Poor’s, Morningstar, and
Bloomberg are some of the well-known services. All these services begin with the
regression beta just described and adjust them to reﬂect what they feel are better estimates of future risk. Although many of these services do not reveal their estimation procedures, Bloomberg is an exception. Figure 8.2 is the beta calculation page
186
ESTIMATING RISK PARAMETERS AND COSTS OF FINANCING
FIGURE 8.1
Boeing versus S&P 500 from 1996 to 2000
--- page 206 ---

from Bloomberg for Boeing, using the same period as our regression (January 1996
to December 2000).
While the time period used is identical to the one used in our earlier regression,
there are subtle differences between this regression and the one in Figure 8.1. First,
Bloomberg uses price appreciation in the stock and the market index in estimating
betas and ignores dividends.4 The fact that dividends are ignored does not make
much difference for a company like Boeing, but it could make a difference for a
company that either pays no dividends or pays signiﬁcantly higher dividends than
the market. This explains the mild differences in the intercept (0.50% versus
0.54%) and the beta (0.57 versus 0.56).
Second, Bloomberg also computes what it calls an adjusted beta, which is estimated as follows:
Adjusted beta = Raw beta(0.67) + 1.00(0.33)
These weights (0.67 and 0.33) do not vary across stocks, and this process pushes all
estimated betas toward 1. Most services employ similar procedures to adjust betas
toward 1. In doing so, they are drawing on empirical evidence that suggests that the
betas for most companies, over time, tend to move toward the average beta, which
is 1. This may be explained by the fact that ﬁrms get more diversiﬁed in their product mix and client base as they get larger. While we agree with the notion that betas
move toward 1 over time, the weighting process used by most services strikes us as
arbitrary and not particularly useful.
Cost of Equity
187
FIGURE 8.2
Beta Estimate for Boeing
Copyright 2001 Bloomberg LP. Reprinted with permission. All rights reserved.
4This is done purely for computational convenience.
--- page 207 ---

Estimation Choices for Beta Estimation
There are three decisions that must be
made in setting up the regression described earlier. The ﬁrst concerns the length of
the estimation period. Most estimates of betas, including those by Value Line and
Standard & Poor’s, use ﬁve years of data, while Bloomberg uses two years of data.
The trade-off is simple: A longer estimation period provides more data, but the ﬁrm
itself might have changed in its risk characteristics over the time period. Boeing,
during the period of our analysis, acquired both Rockwell and McDonnell
Douglas, changing its business mix and its basic risk characteristics.
The second estimation issue relates to the return interval. Returns on stocks are
available on an annual, a monthly, a weekly, a daily, and even an intraday basis.
Using daily or intraday returns increases the number of observations in the regression, but it exposes the estimation process to a signiﬁcant bias in beta estimates related to nontrading.5 For instance, the betas estimated for small ﬁrms, which are
more likely to suffer from nontrading, are biased downward when daily returns are
used. Using weekly or monthly returns can reduce the nontrading bias signiﬁ-
cantly.6 In this case, using weekly returns for two years yields a beta estimate for
Boeing of only 0.88, while the monthly beta estimate over the same period is 0.96.
The third estimation issue relates to the choice of a market index to be used in
the regression. The standard practice used by most beta estimation services is to estimate the betas of a company relative to the index of the market in which its stock
trades. Thus, the betas of German stocks are estimated relative to the Frankfurt
DAX, British stocks relative to the FTSE, Japanese stocks relative to the Nikkei,
and U.S. stocks relative to the NYSE Composite or the S&P 500. While this practice may yield an estimate that is a reasonable measure of risk for the domestic investor, it may not be the best approach for an international or cross-border
investor, who would be better served with a beta estimated relative to an international index. For instance, Boeing’s beta between 1996 and 2000 estimated relative
to the Morgan Stanley Capital International (MSCI) index that is composed of
stocks from different global markets yields a value of 0.82.
To the extent that different services use different estimation periods, use different market indexes, and adjust the regression beta differently, they will often provide different beta estimates for the same ﬁrm at the same point in time. While
these beta differences are troubling, note that the beta estimate delivered by each of
these services comes with a standard error, and it is very likely that all the betas reported for a ﬁrm fall within the range of standard errors from the regressions.
Historical Beta Estimation for Companies in Smaller (or Emerging) Markets
The
process for estimating betas in markets with fewer stocks listed on them is no different from the process described earlier, but the estimation choices on return intervals, the market index, and the return period can make a much bigger difference in
the estimate.
188
ESTIMATING RISK PARAMETERS AND COSTS OF FINANCING
5The nontrading bias arises because the returns in nontrading periods are zero (even though
the market may have moved up or down signiﬁcantly in those periods). Using these nontrading period returns in the regression will reduce the correlation between stock returns and
market returns and the beta of the stock.
6The bias can also be reduced using statistical techniques suggested by Dimson (1979) and
Scholes, and Williams (1977).
--- page 208 ---

Cost of Equity
189
INDEX DOMINATION AND BETA ESTIMATES
There are a number of indexes that are dominated by one or a few stocks.
One of the most striking cases was the Helsinki Stock Exchange (HEX) in the
late 1990s. Nokia, the telecommunications giant, represented 75 percent of
the Helsinki Index in terms of market value. Not surprisingly, a regression of
Nokia against the HEX yielded the results shown in Figure 8.3.
The regression looks impeccable. In fact, the noise problem that we
noted with Boeing, arising from the high standard errors, disappears. The
beta estimate has a standard error of 0.03, but the results are deceptive. The
low standard error is the result of a regression of Nokia on itself, since it
dominates the index. The beta is meaningless to a typical investor in Nokia,
who is likely to be diversiﬁed, if not globally, at least across European
stocks. Worse still, the betas of all other Finnish stocks against the HEX become betas estimated against Nokia. In fact, the beta of every other Finnish
stock at the time of this regression was less than 1. How is this possible, you
might ask, if the average beta is 1? It is the weighted average beta that is 1,
and if Nokia (which comprises three-quarters of the index) has a beta
greater than 1 (which it does), every other stock in the index could well end
up with a beta less than 1.
FIGURE 8.3
Beta Estimate for Nokia
Copyright 2001 Bloomberg LP. Reprinted with permission. All rights reserved.
--- page 209 ---

■When liquidity is limited, as it often is in many stocks in emerging markets, the
betas estimated using short return intervals tend to be much more biased. In
fact, using daily or even weekly returns in these markets will tend to yield betas
that are not good measures of the true market risk of the company.
■In many emerging markets, both the companies being analyzed and the market
itself change signiﬁcantly over short periods of time. Using ﬁve years of returns,
as we did for Boeing, for a regression may yield a beta for a company (and market) that bears little resemblance to the company (and market) as it exists today.
■Finally, the indices that measure market returns in many smaller markets tend to
be dominated by a few large companies. For instance, the Bovespa (the Brazilian
index) was dominated for several years by Telebras, which represented almost
half the index. Nor is this just a problem with emerging markets. The DAX, the
equity index for German stocks, is dominated by Allianz, Deutsche Bank,
Siemens, and Daimler. When an index is dominated by one or a few companies,
the betas estimated against that index are unlikely to be true measures of market
risk. In fact, the betas are likely to be close to 1 for the large companies that
dominate the index and wildly variable for all other companies.
ILLUSTRATION 8.2:
Estimating a Beta for Titan Cement Company
Titan Cement is a cement and construction company in Greece. Reproduced in Figure 8.4 is the beta
estimate for Titan from April 1999 to April 2001 (using weekly returns) obtained from a beta service
(Bloomberg). Note that the index used is the Athens Stock Exchange Index. Based on this regression,
we arrive at the following equation:
ReturnsTitan Cement = 0.31% + 0.93 ReturnsASE
R-squared = 57%
[0.08]
190
ESTIMATING RISK PARAMETERS AND COSTS OF FINANCING
FIGURE 8.4
Beta Estimate for Titan Cement: Athens Stock Exchange Index
Copyright 2001 Bloomberg LP. Reprinted with permission. All rights reserved.
--- page 210 ---

Cost of Equity
191
FIGURE 8.5
Beta Estimate for Titan Cement: MSCI European Index
Copyright 2001 Bloomberg LP. Reprinted with permission. All rights reserved.
FIGURE 8.6
Beta Estimate for Titan Cement: MSCI Global Index
Copyright 2001 Bloomberg LP. Reprinted with permission. All rights reserved.
