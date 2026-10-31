# INVESTMENT VALUATION TOOLS AND TECHNIQUES FOR DETERMINING -- Aswath Damodaran -- Wiley finance series, 3rd ed_, Hoboken, N_J, New Jersey, -- John -- isbn13 9781118011522 -- f84d1622bdc2de526da0dda803c52830 -- Anna’s.pdf — pages 172–191

--- page 172 ---

Portfolio
Expected Price Appreciation
Expected Dividend Yield
High yield
9%
5%
Low yield
12%
1%
You are a taxable investor who faces a tax rate of 40% on dividends. What
would your tax rate on capital gains need to be for you to be indifferent between these two portfolios?
13. Answer true or false to the following questions:
a. Low price-earnings stocks, on average, earn returns in excess of expectations, while high price-earnings stocks earn less than expected. This is primarily because lower PE ratio stocks have lower risk.
True ____
False ____
b. The small ﬁrm effect, which refers the positive excess returns earned, on average, by small ﬁrms, is primarily caused by a few small ﬁrms that make
very high positive returns.
True ____
False ____
c. Investors generally cannot make money on analyst recommendations, because stock prices are not affected by these recommendations.
True ____
False ____
14. You are examining the performance of two mutual funds. AD Value Fund has
been in existence since January 1, 1988, and invests primarily in stocks with
low price-earnings ratios and high dividend yields. AD Growth Fund has also
been in existence since January 1, 1988, but it invests primarily in high-growth
stocks, with high PE ratios and low or no dividends. The performance of these
funds over the past ﬁve years is summarized as follows:
Average from 1988 to 1992
Price Appreciation
Dividend Yield
Beta
NYSE Composite
13%
3%
1.0
AD Value
11%
5%
0.8
AD Growth
15%
1%
1.2
The average risk-free rate during the period was 6%. The current risk-free rate
is 3%.
a. How well or badly did these funds perform after adjusting for risk?
b. Assume that the front-end load on each of these funds is 5% (i.e., if you put
$1,000 in each of these funds today, you would only be investing $950 after
the initial commission). Assume also that the excess returns you have calculated in part (a) will continue into the future and that you choose to invest
in the fund that outperformed the market. How many years would you have
to hold this fund to break even?
Questions and Short Problems
153
--- page 173 ---

CHAPTER 7
Riskless Rates and Risk Premiums
A
ll models of risk and return in ﬁnance are built around a rate that investors can
make on riskless investments and the risk premium or premiums that investors
should charge for investing in the average-risk investment. In the capital asset pricing model (CAPM), where there is only one source of market risk captured in the
market portfolio, this risk premium becomes the premium that investors would demand when investing in that portfolio. In multifactor models, there are multiple
risk premiums, each one measuring the premium demanded by investors for exposure to a speciﬁc market risk factor. This chapter examines how best to measure a
riskless rate and to estimate a risk premium or premiums for use in these models.
As noted in Chapter 4, risk is measured in terms of default risk for bonds, and
this default risk is captured in a default spread that ﬁrms have to pay over and above
the riskless rate. This chapter closes by considering how best to estimate these default spreads and the factors that may cause these spreads to change over time.
THE RISK-FREE RATE
Most risk and return models in ﬁnance start off with an asset that is deﬁned as risk
free, and use the expected return on that asset as the risk-free rate. The expected returns on risky investments are then measured relative to the risk-free rate, with the
risk creating an expected risk premium that is added to the risk-free rate. But what
makes an asset risk free? And what do we do when we cannot ﬁnd such an asset?
These are the questions that will be dealt with in this section.
Requirements for an Asset to Be Risk Free
Chapter 4 considers some of the requirements for an asset to be risk free. In particular, an asset is risk free if we know the expected returns on it with certainty (i.e.,
the actual return is always equal to the expected return). Under what conditions
will the actual returns on an investment be equal to the expected returns? There are
two basic conditions that have to be met. The ﬁrst is that there can be no default
risk. Essentially, this rules out any security issued by a private entity, since even the
largest and safest ones have some measure of default risk. The only securities that
have a chance of being risk free are government securities, not because governments are better run than corporations, but because they usually control the printing of currency. At least in nominal terms, they should be able to fulﬁll their
154
--- page 174 ---

promises. Even this assumption, straightforward though it might seem, does not always hold up, especially when governments refuse to honor claims made by previous regimes and when they borrow in currencies other than their own.
There is a second condition that riskless securities need to fulﬁll that is often
forgotten. For an investment to have an actual return equal to its expected return,
there can be no reinvestment risk. To illustrate this point, assume that you are trying to estimate the expected return over a ﬁve-year period and that you want a riskfree rate. A six-month Treasury bill rate, while default free, will not be risk free,
because there is the reinvestment risk of not knowing what the Treasury bill rate
will be in six months. Even a ﬁve-year Treasury bond is not risk free, since the
coupons on the bond will be reinvested at rates that cannot be predicted today. The
risk-free rate for a ﬁve-year time horizon has to be the expected return on a defaultfree (government) ﬁve-year zero coupon bond. This clearly has painful implications
for anyone doing corporate ﬁnance or valuation, where expected returns often have
to be estimated for periods ranging from 1 to 10 years. A purist’s view of risk-free
rates would then require different risk-free rates for each period, and different expected returns.
As a practical compromise, however, it is worth noting that the present value
effect of using year-speciﬁc risk-free rates tends to be small for most well-behaved
term structures.1 In these cases, we could use a duration matching strategy, where
the duration of the default-free security used as the risk-free asset is matched up to
the duration2 of the cash ﬂows in the analysis. If, however, there are very large differences, in either direction, between short-term and long-term rates, it does pay to
stick with year-speciﬁc risk-free rates in computing expected returns.
Practical Implications When a Default-Free Entity Exists
In most developed markets, where the government can be viewed as a default-free
entity, at least when it comes to borrowing in the local currency, the implications
are simple. When doing investment analysis on longer-term projects or valuations,
the risk-free rate should be the long-term government bond rate. If the analysis is
shorter-term, the short-term government security rate can be used as the risk-free
rate. The choice of a risk-free rate also has implications for how risk premiums are
estimated. If, as is often the case, historical risk premiums are used, where the excess return earned by stocks over and above a government security rate over a past
period is used as the risk premium, the government security chosen has to be the
same one as that used for the risk-free rate. Thus, the historical risk premium used
in the United States should be the excess return earned by stocks over Treasury
bonds, and not Treasury bills, for purposes of long-term analysis.
The Risk-Free Rate
155
1Well-behaved term structures would include a upward-sloping yield curve, where long-term
rates are at most 2 to 3 percent higher than short-term rates.
2In investment analysis, where we look at projects, these durations are usually between 3 and
10 years. In valuation, the durations tend to be much longer, since ﬁrms are assumed to have
inﬁnite lives. The durations in these cases are often well in excess of 10 years and increase
with the expected growth potential of the ﬁrm.
--- page 175 ---

Cash Flows and Risk-Free Rates: The Consistency Principle
The risk-free rate used to come up with expected returns should be measured consistently with how the cash ﬂows are measured. Thus, if cash ﬂows are estimated in
nominal U.S. dollar terms, the risk-free rate will be the U.S. Treasury bond rate.
This also implies that it is not where a ﬁrm is domiciled that determines the choice
of a risk-free rate, but the currency in which the cash ﬂows on the ﬁrm are estimated. Thus, Nestlé can be valued using cash ﬂows estimated in Swiss francs, discounted back at an expected return estimated using a Swiss long-term government
bond rate as the riskfree rate, or it can be valued in British pounds, with both the
cash ﬂows and the risk-free rate being in British pounds. Given that the same ﬁrm
can be valued in different currencies, will the ﬁnal results always be consistent? If
we assume purchasing power parity, then differences in interest rates reﬂect differences in expected inﬂation. Both the cash ﬂows and the discount rate are affected
by expected inﬂation; thus, a low discount rate arising from a low risk-free rate will
be exactly offset by a decline in expected nominal growth rates for cash ﬂows, and
the value will remain unchanged.
If the difference in interest rates across two currencies does not adequately
reﬂect the difference in expected inﬂation in these currencies, the values obtained
using the different currencies can be different. In particular, ﬁrms will be valued
more highly when the currency used is the one with low interest rates relative to
inﬂation. The risk, however, is that the interest rates will have to rise at some
point to correct for this divergence, at which point the values will also converge.
Real versus Nominal Risk-Free Rates
Under conditions of high and unstable inﬂation, valuation is often done in real
terms. Effectively, this means that cash ﬂows are estimated using real growth
rates and without allowing for the growth that comes from price inﬂation. To be
consistent, the discount rates used in these cases have to be real discount rates.
To get a real expected rate of return, we need to start with a real risk-free rate.
While government bills and bonds offer returns that are risk free in nominal
terms, they are not risk free in real terms, since expected inﬂation can be
volatile. The standard approach of subtracting an expected inﬂation rate from
the nominal interest rate to arrive at a real risk-free rate provides at best an estimate of the real risk-free rate.
Until recently, there were few traded default-free securities that could be used
to estimate real risk-free rates, but the introduction of inﬂation-indexed Treasuries
(TIPs) has ﬁlled this void. An inﬂation-indexed Treasury security does not offer a
guaranteed nominal return to buyers, but instead provides a guaranteed real return.
Thus, an inﬂation-indexed Treasury that offers a 3 percent real return will yield approximately 7 percent in nominal terms if inﬂation is 4 percent and only 5 percent
in nominal terms if inﬂation is only 2 percent.
The only problem is that real valuations are seldom called for or done in the
United States, which has historically had stable and low expected inﬂation. The
markets where we would most need to do real valuations, unfortunately, are markets without inﬂation-indexed default-free securities. The real risk-free rates in
these markets can be estimated by using one of two arguments:
156
RISKLESS RATES AND RISK PREMIUMS
--- page 176 ---

1. The ﬁrst argument is that as long as capital can ﬂow freely to those economies
with the highest real returns, there can be no differences in real risk-free rates
across markets. Using this argument, the real risk-free rate for the United
States, estimated from the inﬂation-indexed Treasury, can be used as the real
risk-free rate in any market.
2. The second argument applies if there are frictions and constraints in capital
ﬂowing across markets. In that case, the expected real return on an economy, in
the long term, should be equal to the expected real growth rate, again in the
long term, of that economy, for equilibrium. Thus, the real risk-free rate for a
mature economy like Germany should be much lower than the real risk-free
rate for a economy with greater growth potential, such as Hungary’s.
Risk-Free Rates When There Is No Default-Free Entity
Our discussion, hitherto, has been predicated on the assumption that governments
do not default, at least on local borrowing. There are many emerging market
economies and quite a few devloped markets where this assumption might not be
viewed as reasonable. Governments in these markets are perceived as capable of defaulting even on local borrowing. When this is coupled with the fact that some governments do not borrow long-term in the local currency, there are scenarios where
obtaining a local risk-free rate, especially for the long term, becomes difﬁcult. We
consider four alternatives in the section following.
Local Currency Government Bond
If the government issues long-term bonds denominated in the local currency and these bonds are traded, you can use the interest rates
on these bonds as a starting point for estimating the risk-free rate in that currency. In
early 2011, for instance, the Indian government issued 10-year rupee-denominated
bonds that were trading at a yield of 8 percent. This rate, though, is not a risk-free
rate, because investors perceive default risk in the Indian government. To back out
how much of the yield can be attributed to the default risk, we used the local currency sovereign rating3 of Ba2 assigned to India by Moody’s and estimated a default
spread of 2.40 percent for that rating.4
The resulting risk-free rate in rupees is:
Risk-free rate in rupees = Government bond rate – Default spread
= 8.00% – 2.40% = 5.60%
It is true that this number assumes that the ratings agency is correct in its assessment
of sovereign risk and that the default spread based on the rating is correct. An
The Risk-Free Rate
157
3Ratings agencies provide ratings for a country for borrowings in the local currency and a
foreign currency. The latter rating is usually lower (since countries have a greater chance of
defaulting when they borrow in a foreign currency), but the rating that matters for this
analysis is the rating in the  local currency. If the rating is Aaa (Moody’s) or AAA (S&P), the
government bond rate will be the  risk-free rate.
4The default spread for a rating is computed by looking at dollar-denominated bonds issued
by other  governments with a Ba2 rating and comparing the rates on these bonds to the U.S.
Treasury bond rate.
--- page 177 ---

alternative approach to estimating default spreads that has become available in
recent years is the credit default swap (CDS) market, where investors can buy insurance against default. While there were no traded CDSs on India in early 2011, there
were CDS contracts traded on approximately 60 countries in March 2011. The
Brazil CDS in March 2011 was trading at 75 basis points (0.75 percent), which can
be used in conjunction with the 10-year Brazilian real-denominated government
bond rate of 8.25 percent to compute the risk-free rate in Brazilian real (BR):
Risk-free rate in BR = Government bond rate in BR – Default spread
= 8.25% – 0.75%
The CDS market does provide a more dynamic and updated measure of the default spread but, being a market-traded number, is much more volatile. It also provides a dollar or euro based spread which may not apply to the local currency bonds.
Build-Up Approach
There are countries where either the government does not issue bonds denominated in the local currency or these bonds do not trade. In this
case, one alternative is to build up to a risk-free rate from fundamentals:
Build-up risk-free rate = Expected inﬂation + Expected long-term real growth rate
Since the risk-free rate in any currency can be written as the sum of expected
inﬂation in that currency and the expected real rate, we can try to estimate the two
components separately. To estimate expected inﬂation, we can start with the current inﬂation rate and extrapolate from that to expected inﬂation in the future.
For the real rate, we can use the rate on the inﬂation-indexed U.S. Treasury bond
rate, with the rationale that real rates should be the same globally. In 2011, for instance, adding the expected inﬂation rate of 6 percent in India to the interest rate
of 1 percent on the inﬂation-indexed U.S. Treasury would have yielded a risk-free
rate of 7 percent in Indian rupees.
Derivatives Markets
Forward and futures contracts on exchange rates provide information about interest rates in the currencies involved, since interest rate parity governs the relationship between spot and forward rates. For instance, the forward
rate between the Thai baht and the U.S. dollar can be written as follows:
For example, if the current spot rate is 38.10 Thai baht per U.S. dollar, the 10-year forward rate is 61.36 baht per dollar, and the current 10-year U.S. Treasury bond rate
is 5 percent, the 10-year Thai risk-free rate (in nominal baht) can be estimated as
follows:
Solving for the Thai interest rate yields a 10-year risk-free rate of 10.12 percent. The
biggest limitation of this approach, however, is that forward rates are difﬁcult to
61.36 = 38.10
(1 + Interest rateThai baht)10
(1.05)10
Forward ratet
baht,$ = Spot ratebaht,$ =
(1 + Interest rateThai baht)t
(1 + Interest rateU.S. dollar)t
158
RISKLESS RATES AND RISK PREMIUMS
--- page 178 ---

come by for periods beyond a year5 for many of the emerging  markets, where we
would be most interested in using them.
Risk-Free Rate Conversion
If the only reason for differences in risk-free rates in
different currencies is  expected inﬂation, you can convert the risk-free rate in a mature
market currency (U.S. dollars, euros) into a risk-free rate in an emerging market
currency, using differences in inﬂation across currencies.
– 1
For example, assume that the risk-free rate in U.S. dollars is 4 percent and that the
expected inﬂation rate in Indonesian rupiah is 11 percent (compared to the 2 percent
inﬂation rate in U.S. dollars). The Indonesian risk-free rate can be written as follows:
Cost of capitalrupiah = 1.04 ×
– 1 = 0.131764 or 13.18%
To make this conversion, we still have to estimate the expected inﬂation in the
local currency and the mature market currency.
What if none of these choices listed work? In other words, what if the government has no local currency bonds outstanding, there are no forward or futures contract on the currency, and/or expected inﬂation in the local currency is difﬁcult to
estimate? Faced with these problems, it is best to switch and do your valuation in a
different currency. Thus, rather than value a Nigerian or Vietnamese company in
the local currency, you would value it in euros or dollars. You will still have to estimate expected exchange rates in the future in order to convert local currency cash
ﬂows to foreign currency cash ﬂows, but that may be a more manageable exercise.
EQUITY RISK PREMIUM
The notion that risk matters, and that riskier investments should have a higher expected return than safer investments to be considered good investments, is intuitive. Thus, the expected return on any investment can be written as the sum of the
risk-free rate and an extra return to compensate for the risk. The disagreement, in
both theoretical and practical terms, remains on how to measure this risk, and
how to convert the risk measure into an expected return that compensates for risk.
This section looks at the estimation of an appropriate equity risk premium (ERP)
to use in risk and return models, in general, and in the capital asset pricing model,
in particular.
1.11
1.02
rlocal currency = (1 + rforeign currency) ×
1 + Expected inﬂationlocal currency
1 + Expected inﬂationforeign currency
Equity Risk Premium
159
5In cases where only a one-year forward rate exists, an approximation for the long-term rate
can be obtained by ﬁrst backing out the one-year local currency borrowing rate, taking the
spread over the one-year Treasury bill rate, and then adding this spread onto the long-term
Treasury bond rate. For instance, with a one-year forward rate of 39.95 on the Thai bond,
we obtain a one-year Thai baht riskless rate of 9.04 percent (given a one-year Treasury bill
rate of 4 percent). Adding the spread of 5.04 percent to the 10-year Treasury bond rate of
5 percent provides a 10-year Thai baht rate of 10.04 percent.
--- page 179 ---

Competing Views on Risk Premiums
In Chapter 4, we considered several competing models of risk ranging from the capital
asset pricing model to multifactor models. Notwithstanding their different conclusions, they all share some common views about risk. First, they all deﬁne risk in terms
of variance in actual returns around an expected return; thus, an investment is riskless
when actual returns are always equal to the expected return. Second, they all argue
that risk has to be measured from the perspective of the marginal investor in an asset,
and that this marginal investor is well diversiﬁed. Therefore, the argument goes, it is
only the risk that an investment adds on to a diversiﬁed portfolio that should be measured and compensated. In fact, it is this view of risk that leads models of risk to break
the risk in any investment into two components. There is a ﬁrm-speciﬁc component
that measures risk that relates only to that investment or to a few investments like it,
and a market component that contains risk that affects a large subset or all investments. It is the latter risk that is not diversiﬁable and should be rewarded.
While all risk and return models agree on this fairly crucial distinction, they
part ways when it comes to how to measure this market risk. Table 7.1 summarizes
four models and the way each model attempts to measure risk.
In the ﬁrst three models, the expected return on any investment can be written as:
where
βj = Beta of investment relative to factor j
Risk premiumj = Risk premium for factor j
Expected return
Risk-free rate
Risk premium
j
j 1
j k
j
=
+
=
=
∑β (
)
160
RISKLESS RATES AND RISK PREMIUMS
TABLE 7.1
Comparing Risk and Return Models
Model
Assumptions
Measure of Market Risk
Capital asset pricing
There are no transaction
Beta measured against this
model (CAPM)
costs or private
market portfolio
information. Therefore, the
diversiﬁed portfolio includes
all traded investments, held
in proportion to their
market value.
Arbitrage pricing model
Investments with the same
Betas measured against multiple
(APM)
exposure to market risk have (unspeciﬁed) market risk
to trade at the same price
factors
(no arbitrage).
Multifactor model
There is the same no-
Betas measured against
arbitrage assumption as
multiple speciﬁed
with the APM.
macroeconomic factors
Proxy model
Over very long periods,
Proxies for market risk, for
higher returns on
example, include market
investments must be
capitalization and price–book
compensation for higher
value ratios.
market risk.
--- page 180 ---

Note that in the special case of a single-factor model, like the CAPM, each investment’s expected return will be determined by its beta relative to the risk premium for that factor.
Assuming that the risk-free rate is known, these models all require two inputs.
The ﬁrst is the beta or betas of the investment being analyzed, and the second is the
appropriate risk premium(s) for the factor or factors in the model. The issue of beta
estimation is examined in the next chapter, this section concentrates on the measurement of the risk premium.
What We Would Like to Measure As far as the risk premium is concerned, we
would like to know for each factor what investors, on average, require as a premium over the risk-free rate for an investment with average risk.
Without any loss of generality, let us consider the estimation of the beta and the
equity risk premium in the capital asset pricing model. Here, the risk premium
should measure what investors, on average, demand as extra return for investing in
the market portfolio relative to the risk-free asset.
Historical Risk Premiums
In practice, we usually estimate the risk premium by looking at the historical premium earned by stocks over default-free securities over long time periods. The
historical premium approach is simple. The actual returns earned on stocks
over a long time period are estimated, and then compared to the actual returns
earned on a default-free (usually government) security. The difference, on an
annual basis, between the two returns is computed and represents the historical risk premium. This approach might yield reasonable estimates in markets like
the United States, with a large and diversiﬁed stock market and a long history of
returns on both stocks and government securities. However, they yield meaningless estimates for the risk premiums in other countries, where the equity markets
represent a small proportion of the overall economy and the historical returns are
available only for short periods.
While users of risk and return models may have developed a consensus that
historical premium is, in fact, the best estimate of the risk premium looking forward, there are surprisingly large differences in the actual premiums we observe being used in practice. For instance, the risk premium estimated in the U.S. markets
by different investment banks, consultants, and corporations range from 3 percent
at the lower end to 12 percent at the upper end. Given that they almost all use the
same database of historical returns, provided by Ibbotson Associates,6 summarizing
data from 1926, these differences may seem surprising. There are, however, three
reasons for the divergence in risk premiums:
1. Time period used. While there are many who use all the data going back to
1926 (or earlier), there are almost as many using data over shorter time periods,
such as 50, 20, or even 10 years, to come up with historical risk premiums. The
Equity Risk Premium
161
6See Stocks, Bonds, Bills and Inﬂation, an annual edition that reports on annual returns on
stocks, Treasury bonds, and Treasury bills, as well as inﬂation rates from 1926 to the present
(www.ibbotson.com).
--- page 181 ---

rationale presented by those who use shorter periods is that the risk aversion of the
average investor is likely to change over time, and that using a shorter time period
provides a more updated estimate. This has to be offset against a cost associated
with using shorter time periods, which is the greater noise in the risk premium estimate. In fact, given the annual standard deviation in stock prices7 between 1926
and 2010 of 20 percent, the standard error8 associated with the risk premium estimate can be estimated for different estimation periods in Table 7.2.
Note that to get reasonable standard errors, we need very long time periods of
historical returns. Conversely, the standard errors from 10-year and 20-year estimates are likely to be almost as large as or larger than the actual risk premium estimated. This cost of using shorter time periods seems, in our view, to overwhelm
any advantages associated with getting a more updated premium.
2. Choice of risk-free security. The Ibbotson database reports returns on
both Treasury bills (T-bills) and Treasury bonds (T-bonds), and the risk premium
for stocks can be estimated relative to each. Given that the yield curve in the
United States has been upward-sloping for most of the past seven decades, the
risk premium is larger when estimated relative to shorter-term government securities (such as Treasury bills). The risk-free rate chosen in computing the premium has to be consistent with the risk-free rate used to compute expected
returns. Thus, if the Treasury bill rate is used as the risk-free rate, the premium
has to be the premium earned by stocks over that rate. If the Treasury bond rate
is used as the risk-free rate, the premium has to be estimated relative to that rate.
For the most part, in corporate ﬁnance and valuation, the risk-free rate will be a
long-term default-free Treasury (government) bond rate and not a Treasury bill
rate. Thus, the risk premium used should be the premium earned by stocks over
Treasury bonds.
3. Arithmetic and geometric averages. The ﬁnal sticking point when it comes
to estimating historical premiums relates to how the average returns on stocks,
Treasury bonds, and Treasury bills are computed. The arithmetic average return
measures the simple mean of the series of annual returns, whereas the geometric
162
RISKLESS RATES AND RISK PREMIUMS
7For the historical data on stock returns, bond returns, and bill returns, check under “Updated Data” in www.stern.nyu.edu/~adamodar.
8These estimates of the standard error are probably understated, because they are based on
the assumption that annual returns are uncorrelated over time. There is substantial empirical
evidence that returns are correlated over time, which would make this standard error estimate much larger.
TABLE 7.2
Standard Errors in Risk Premium Estimates
Estimation Period
Standard Error of Risk Premium Estimate
5 years
20%/√5   = 8.94%
10 years
20%/√10 = 6.32%
25 years
20%/√25 = 4.00%
50 years
20%/√50 = 2.83%
--- page 182 ---

average looks at the compounded return.9 Conventional wisdom argues for the
use of the arithmetic average. In fact, if annual returns are uncorrelated over time,
and our objective were to estimate the risk premium for the next year, the arithmetic average is the best unbiased estimate of the premium. In reality, however,
there are strong arguments that can be made for the use of geometric averages.
First, empirical studies seem to indicate that returns on stocks are negatively correlated over time.10 Consequently, the arithmetic average return is likely to overstate
the premium. Second, while asset pricing models may be single-period models,
the use of these models to get expected returns over long periods (such as 5 or
10 years) suggests that we are interested in returns over longer periods. In this
context, the argument for geometric average premiums becomes even stronger.
In summary, the risk premium estimates vary across users because of differences in time periods used, the choice of Treasury bills or bonds as the risk-free rate
and the use of arithmetic averages as opposed to geometric averages. The effect of
these choices is summarized in Table 7.3, which uses returns from 1928 to 2010.
Note that the premiums can range from –4.11 percent to 7.62 percent, depending
on the choices made. In fact, these differences are exacerbated by the fact that
many risk premiums that are in use today were estimated using historical data
three, four, or even 10 years ago. If forced to choose an equity risk premium on this
table, we would be inclined to go with 4.31 percent, the geometric average risk premium for stocks over Treasury bonds from 1928 to 2010.
Equity Risk Premium
163
histretSP.xls: There is a dataset on the Web that summarizes historical returns on
stocks, T-bonds, and T-bills in the United States going back to 1928.
9The compounded return is computed by taking the value of the investment at the start of
the period (Value0) and the value at the end (ValueN), and then computing the following:
10In other words, good years are more likely to be followed by poor years, and vice versa.
The evidence on negative serial correlation in stock returns over time is extensive, and can be
found in Fama and French (1988). While they ﬁnd that the one-year correlations are low, the
ﬁve-year serial correlations are strongly negative for all size classes.
Geometric average
Value
Value
N
0
1/N
= ⎛
⎝⎜
⎞
⎠⎟
−1
TABLE 7.3
Historical Risk Premiums for the United States
ERP: Stocks minus
ERP: Stocks minus
Treasury Bonds
Treasury Bonds
Arithmetic
Geometric
Arithmetic
Geometric
1928–2010
7.62%
5.67%
6.03%
4.31%
(2.25%)
(2.38%)
1960–2010
5.83%
4.44%
4.13%
3.09%
(2.42%)
(2.69%)
2000–2010
1.37%
–0.79%
–2.26%
–4.11%
(6.73%)
(9.00%)
Source: S&P and Federal Reserve Bank.
--- page 183 ---

Historical Risk Premiums: Other Markets
If it is difﬁcult to estimate a reliable historical premium for the U.S. market, it becomes doubly so when looking at markets
with short and volatile histories. This is clearly true for emerging markets, but it is
also true for the European equity markets. While the economies of Germany, Italy,
and France may be mature, their equity markets do not share the same characteristic. Until two decades ago, they tend to be dominated by a few large companies;
many businesses remain private; and trading was, except on a few stocks.
There are some practitioners who still use historical premiums for these markets. To capture some of the danger in this practice, Table 7.4 summarizes historical risk premiums11 for major non-U.S. markets for 1970 to 2010.
Note that some of the countries have very low historical risk premiums, and a
few others have high risk premiums. Before an attempt is made to come up with a
rationale for why this might be so, it is worth noting that the standard error on
each and every one of these estimates is high, notwithstanding the fact that the premiums are estimated over a very long time period.
164
RISKLESS RATES AND RISK PREMIUMS
TABLE 7.4
Historical Equity Risk Premiums: Markets outside the United States
Stocks minus Long-Term Government Securities
Geometric
Arithmetic
Standard
Standard
Country
Mean
Mean
Error
Deviation
Australia
5.9%
7.8%
1.9%
19.8%
Belgium
2.5%
4.9%
2.0%
21.4%
Canada
3.7%
5.3%
1.7%
18.2%
Denmark
2.0%
3.4%
1.6%
17.2%
Finland
5.6%
9.2%
2.9%
30.3%
France
3.2%
5.6%
2.2%
22.9%
Germany
5.4%
8.8%
2.7%
28.4%
Ireland
2.9%
4.9%
1.9%
19.8%
Italy
3.7%
7.2%
2.8%
29.6%
Japan
5.0%
9.1%
3.1%
32.8%
Netherlands
3.5%
5.8%
2.1%
22.2%
New Zealand
3.8%
5.4%
1.7%
18.1%
Norway
2.5%
5.5%
2.7%
28.0%
South Africa
5.5%
7.2%
1.9%
19.6%
Spain
2.3%
4.3%
2.0%
20.8%
Sweden
3.8%
6.1%
2.1%
22.3%
Switzerland
2.1%
3.6%
1.7%
17.6%
United Kingdom
3.9%
5.2%
1.6%
17.0%
United States
4.4%
6.4%
1.9%
20.5%
World-ex U.S.
3.8%
5.0%
1.5%
15.5%
World
3.8%
5.0%
1.5%
15.5%
Source: Dimson, Marsh, and Staunton (2010).
11This data is from the Credit Suisse Global Investment Returns Sourcebook 2011, updated
by Dimson, Marsh and Staunton at the London Business School.
--- page 184 ---

If the standard errors on these estimates are high, consider how much more
noise there is in estimates of historical risk premiums for emerging market equity
markets, which often have a reliable history of 10 years or less and very large standard deviations in annual stock returns. Historical risk premiums for emerging
markets may provide for interesting anecdotes, but they clearly should not be used
in risk and return models.
Modified Historical Risk Premium
While historical risk premiums for markets outside
the United States cannot be used in risk models, we still need to estimate a risk premium for use in these markets. To approach this estimation question, let us start with
the basic proposition that the risk premium in any equity market can be written as:
Equity risk premium = Base premium for mature equity market + Country premium
The country premium could reﬂect the extra risk in a speciﬁc market. This boils
down our estimation to answering two questions:
1. What should the base premium for a mature equity market be?
2. Should there be a country premium, and if so, how do we estimate the
premium?
Equity Risk Premium
165
HISTORICAL RISK PREMIUM APPROACH: SOME CAVEATS
Given how widely the historical risk premium approach is used, it is surprising how ﬂawed it is and how little attention these ﬂaws have attracted. Consider ﬁrst the underlying assumption that investors’ risk premiums have not
changed over time and that the average risk investment (in the market portfolio) has remained stable over the period examined. We would be hard-pressed
to ﬁnd anyone who would be willing to sustain this argument with fervor.
The obvious ﬁx for this problem, which is to use a more recent time period, runs directly into a second problem, which is the large standard error associated with risk premium estimates. Though these standard errors may be
tolerable for very long time periods, they clearly are unacceptably high when
shorter periods are used.
Finally, even if there is a sufﬁciently long time period of history available
and investors’ risk aversion has not changed in a systematic way over that period, there is a ﬁnal problem. Markets that exhibit this characteristic, and let us
assume that the U.S. market is one such example, represent so-called survivor
markets. In other words, assume that one had invested in the 10 largest equity
markets in the world in 1928, of which the United States was one. In the period
extending from 1928 to 2010, investments in few of the other equity markets
would have earned as large a premium as the U.S. equity market, and some of
them (like Austria) would have resulted in investors earning little or even negative returns over the period. Thus, the survivor bias will result in historical premiums that are larger than expected premiums for markets like the United
States, even assuming that investors are rational and factor risk into prices.
--- page 185 ---

To answer the ﬁrst question, one can argue that the U.S. equity market is a mature market and that there is sufﬁcient historical data in the United States to make a
reasonable estimate of the risk premium. In fact, reverting back to our discussion of
historical premiums in the U.S. market, we will use the geometric average premium
earned by stocks over Treasury bonds of 4.31 percent between 1928 and 2010. We
have chosen the long time period to reduce standard error, the Treasury bond to be
consistent with our choice of a risk-free rate, and the geometric averages to reﬂect
our desire for a risk premium that we can use for longer-term expected returns.
On the issue of country premiums, there are some who argue that country risk
is diversiﬁable and that there should be no country risk premium. After looking at
the basis for their argument, and then considering the alternative view that there
should be a country risk premium, we present approaches for estimating country
risk premiums, one based on country bond default spreads and one based on equity
market volatility.
Should There Be a Country Risk Premium?
Is there more risk in investing in a
Malaysian or Brazilian stock than there is in investing in the United States? The answer, to most, seems to be obviously afﬁrmative. That, however, does not answer
the question of whether there should be an additional risk premium charged when
investing in those markets.
Note that the only risk that is relevant for purposes of estimating a cost of equity is market risk or risk that cannot be diversiﬁed away. The key question then
becomes whether the risk in an emerging market is diversiﬁable or nondiversiﬁable
risk. If, in fact, the additional risk of investing in Malaysia or Brazil can be diversi-
ﬁed away, then there should be no additional risk premium charged. If it cannot,
then it makes sense to think about estimating a country risk premium.
But diversiﬁed away by whom? Equity in a Brazilian or Malaysian ﬁrm can be
held by hundreds or thousands of investors, some of whom may hold only domestic stocks in their portfolio, whereas others may have more global exposure. For
purposes of analyzing country risk, we look at the marginal investor—the investor
most likely to be trading on the equity. If that marginal investor is globally diversi-
ﬁed, there is at least the potential for global diversiﬁcation. If the marginal investor
does not have a global portfolio, the likelihood of diversifying away country risk
declines substantially. Stulz (1999) made a similar point using different terminology. He differentiated between segmented markets, where risk premiums can be
different in each market because investors cannot or will not invest outside their
domestic markets, and open markets, where investors can invest across markets. In
a segmented market, the marginal investor will be diversiﬁed only across investments in that market, whereas in an open market, the marginal investor has the opportunity (even if he or she does not take it) to invest across markets.
Even if the marginal investor is globally diversiﬁed, there is a second test that has
to be met for country risk not to matter. All or much of country risk should be
country speciﬁc. In other words, there should be low correlation across markets.
Only then will the risk be diversiﬁable in a globally diversiﬁed portfolio. If, however,
the returns across countries have signiﬁcant positive correlation, country risk has a
market risk component, is not diversiﬁable, and can command a premium. Whether
returns across countries are positively correlated is an empirical question. Studies
from the 1970s and 1980s suggested that the correlation was low, and this was an
impetus for global diversiﬁcation. Partly because of the success of that sales pitch and
166
RISKLESS RATES AND RISK PREMIUMS
--- page 186 ---

partly because economies around the world have become increasingly intertwined
over the past decades, more recent studies indicate that the correlation across markets
has risen. This is borne out by the speed with which troubles in one market, say Russia, can spread to a market with little or no obvious relationship to it, say Brazil.
So where do we stand? We believe that while the barriers to trading across
markets have dropped, investors still have a home bias in their portfolios and that
markets remain partially segmented. While globally diversiﬁed investors are playing
an increasing role in the pricing of equities around the world, the resulting increase
in correlation across markets has resulted in a portion of country risk being nondiversiﬁable or market risk. The next section considers how best to measure this
country risk and build it into expected returns.
Measuring Country Risk Premiums If country risk matters and leads to higher
premiums for riskier countries, the obvious follow-up question becomes how we
measure this additional premium. This section looks at three approaches. The ﬁrst
builds on default spreads on country bonds issued by each country, whereas the
second uses equity market volatility as its basis. The third is a melded approach
that uses both default spreads and equity market volatility.
Default Risk Spreads While there are several measures of country risk, one of the
simplest and most easily accessible is the rating assigned to a country’s debt by a
ratings agency; Standard & Poor’s (S&P), Moody’s Investors Service, and Fitch all
rate countries. These ratings measure default risk (rather than equity risk), but they
are affected by many of the factors that drive equity risk—the stability of a country’s currency, its budget and trade balances, and its political stability, for instance.12 The other advantage of ratings is that they can be used to estimate default
spreads over the riskless rate. The default spreads are estimated by comparing the
dollarand euro-denominated bonds issued by governments that share a sovereign
rating. For instance, a 10-year dollar-denominated bond issued by the Peruvian
government, rated Baa by Moody’s, traded at an interest rate of 5.2% in January
2011—a 1.7% spread over the U.S. Treasury bond rate of 3.5% at the time. Since
there can be country-speciﬁc factors that cause these rates to vary across bonds, we
average the spreads within each ratings class to arrive at the average spread for
each sovereign rating. Across six countries rated Baa in January 2011, for example,
the average default spread was 2.00%.  Thus, any country with a Baa rating would
be assigned a spread of 2.00% in January 2011.
The perils with sovereign ratings have been documented over the past few years.
Speciﬁcally, ratings agencies seem to lag markets in responding to changes in country
risk. An alternative approach to estimating default spreads is the CDS market. As we
noted previously in the section on risk-free rates, in early 2011 there were CDS instruments traded in about 60 countries, providing an updated market measure of default risk. In January 2011, for instance, the CDS spread for Peru was 160 basis
points (1.6 percent), close to the default spread estimated from the dollar-denominated
bond. Table 7.5 summarizes default spreads estimated for selected countries in January 2011, using both the sovereign rating and CDS approaches.
Equity Risk Premium
167
12The process by which country ratings are obtained is explained on the S&P web site at
www.standardandpoors.com.
--- page 187 ---

Analysts who use default spreads as measures of country risk typically add them
on to the cost of both equity and debt of every company traded in that country. For
instance, the cost of equity for a Peruvian company, estimated in U.S. dollars, will be
2.00 percent higher than the cost of equity of an otherwise similar U.S. company. If
we assume that the risk premium for the United States and other mature equity markets is 4.31 percent, the cost of equity for a Peruvian company with a beta of 1.2 can
be estimated as follows (with a U.S. Treasury bond rate of 3.5 percent).
Cost of equity (in U.S. dollars) = Risk-free rate + Beta × U.S. risk premium
+ Default spread
= 3.5% + 1.2(4.31%) + 2.00% = 10.67%
In some cases, analysts add the default spread to the U.S. risk premium and multiply the total risk premium by the beta. This increases the cost of equity for highbeta companies and lowers it for low-beta ﬁrms.
While ratings provide a convenient measure of country risk, there are costs associated with using them as the only measure. First, ratings agencies often lag markets when it comes to responding to changes in the underlying default risk. Second,
the ratings agency focus on default risk may obscure other risks that could still affect equity markets. What are the alternatives? There are numerical country risk
scores that have been developed by some services as much more comprehensive
measures of risk. The Economist, for instance, has a score that runs from 0 to 100
(where 0 is no risk, and 100 is most risky) that it uses to rank emerging markets.
Alternatively, country risk can be estimated from the bottom up by looking at economic fundamentals in each country. This, of course, requires signiﬁcantly more information than the other approaches. Finally, default spreads measure the risk
associated with bonds issued by countries and not the equity risk in these countries.
Since equities in any market are likely to be more risky than bonds, you could argue that default spreads understate equity risk premiums.
168
RISKLESS RATES AND RISK PREMIUMS
TABLE 7.5
Default Spreads for Selected Countries—January 2011
Sovereign Rating
Default
10-year CDS
Country
(Moody’s)
Spreada
Spreadb
Argentina
B3
6.00%
6.62%
Brazil
Baa3
2.00%
1.59%
Chile
Aa3
0.70%
1.00%
China
Aa3
0.70%
0.99%
India
Ba1
2.40%
NA
Indonesia
Ba2
2.75%
2.06%
Malaysia
A3
1.15%
0.99%
Peru
Baa3
2.00%
1.52%
Poland
A2
1.00%
1.64%
Russia
Baa1
1.50%
1.78%
South Africa
A3
1.15%
1.65%
Turkey
Ba2
2.75%
2.01%
aAverage default spread across countries with given sovereign rating.
bMarket price for 10-year CDS.
Source: Bloomberg.
--- page 188 ---

Relative Standard Deviations
There are some analysts who believe that investors in equity markets choose among these markets based on their assessed
riskiness and that the risk premiums should reﬂect the differences in equity risk.
A conventional measure of equity risk is the standard deviation in stock prices;
higher standard deviations are generally associated with more risk. If you scale
the standard deviation of one market against another, you obtain a measure of
relative risk.
Standard deviationU.S.
Relative standard deviationcountry X = Standard deviationcountry X
This relative standard deviation, when multiplied by the premium used for U.S.
stocks, should yield a measure of the total risk premium for any market.
Equity risk premiumcountry X = Risk premumU.S. × Relative standard deviationcountry X
Assume, for the moment, that you are using a mature market premium for the
United States of 4.31 percent and that the annual standard deviation of U.S. stocks
is 20 percent. If the annual standard deviation of Indonesian stocks is 35 percent,
the estimate of a total risk premium for Indonesia would be:
Equity risk premiumIndonesia = 4.31% × (35%/20%) = 7.54%
The country risk premium can be isolated as follows:
Country risk premiumIndonesia = 7.54% – 4.31% = 3.23%
While this approach has intuitive appeal, there are problems with using standard deviations computed in markets with widely different market structures and
liquidity. There are very risky emerging markets that have low standard deviations
for their equity markets because the markets are illiquid. This approach will understate the equity risk premiums in those markets. The second problem is related to
currencies, since the standard deviations are usually measured in local currency
terms; the standard deviation in the U.S. market is a dollar standard deviation,
Equity Risk Premium
169
THE DANGER OF DOUBLE COUNTING RISK
When assessing country risk, there is a substantial chance that the same risk
may be counted more than once in a valuation. For instance, there are analysts who use the dollar-denominated bonds issued by a country—the Brazilian dollar bond, for instance—as the risk-free rate when estimating cost of
equity for Brazilian companies. The interest rate on this bond already incorporates the default spreads discussed in the preceding section. If the risk premium is also adjusted upward to reﬂect country risk, there has been a double
counting of the risk. This effect is made worse when betas are adjusted upward and cash ﬂows are adjusted downward (a process called “haircutting”)
because of country risk.
--- page 189 ---

whereas the standard deviation in the Indonesian market is a rupiah standard deviation. This is a relatively simple problem to ﬁx, though, since the standard deviations can be measured in the same currency—you could estimate the standard
deviation in dollar returns for the Indonesian market.
Default Spreads + Relative Standard Deviations
The country default spreads that
come with country ratings provide an important ﬁrst step, but still only measure
the premium for default risk. Intuitively, we would expect the country equity risk
premium to be larger than the country default risk spread. To address the issue of
how much higher, one can look at the volatility of the equity market in a country
relative to the volatility of the country bond used to estimate the spread. This yields
the following estimate for the country equity risk premium:
To illustrate, consider the case of Brazil. In January 2011, Brazil was rated
Baa3 by Moody’s, resulting in a default spread of 2.00 percent. The annualized
standard deviation in the Brazilian equity index over the previous two years was
17.65 percent, while the annualized standard deviation in the Brazilian dollardenominated bond was 7.32 percent. The resulting country equity risk premium
for Brazil is as follows:
Note that this country risk premium will increase if the country rating drops or if
the relative volatility of the equity market increases. Adding this premium to the
mature market (U.S.) premium of 4.31 percent would yield a total equity risk premium for Brazil of 9.13 percent.
Why should equity risk premiums have any relationship to country bond spreads?
A simple explanation is that an investor who can make 11 percent on a dollar-denominated Brazilian government bond would not settle for an expected return of 10.5 percent (in dollar terms) on Brazilian equity. Playing devil’s advocate, however, a critic
could argue that the interest rate on a country bond, from which default spreads are
extracted, is not really an expected return since it is based on the promised cash ﬂows
(coupon and principal) on the bond rather than the expected cash ﬂows. In fact, if we
wanted to estimate a risk premium for bonds, we would need to estimate the expected
return based on expected cash ﬂows, allowing for the default risk. This would result in
a much lower default spread and equity risk premium.
Both this approach and the previous one use the standard deviation in equity of a
market to make a judgment about country risk premium, but they measure it relative
to different bases. This approach uses the country bond as a base, whereas the previous one uses the standard deviation in the U.S. market. This approach assumes that investors are more likely to choose between Brazilian bonds and Brazilian equity,
whereas the previous approach assumes that the choice is across equity markets.
Choosing among the Approaches
The three approaches to estimating country risk
premiums will generally give you different estimates, with the bond default spread
Brazil’s country risk premium = 2.00%
17.65%
7.32%
= 4.82%
⎛
⎝⎜
⎞
⎠⎟
Country risk premium
Country default spread
equity
country bond
=
×
⎛
⎝⎜
⎞
⎠⎟
σ
σ
170
RISKLESS RATES AND RISK PREMIUMS
--- page 190 ---

and relative equity standard deviation approaches yielding lower country risk premiums than the melded approach that uses both the country bond default spread and
the equity standard deviation. We believe that the larger country risk premiums that
emerge from the last approach are the most realistic for the immediate future, but
that country risk premiums will change over time. Just as companies mature and become less risky over time, countries can mature and become less risky as well.
One way to adjust country risk premiums over time is to begin with the premium that emerges from the melded approach and to adjust this premium down toward either the country bond default spread or the country premium estimated from
equity standard deviations. Another way of presenting this argument is to note that
the differences between standard deviations in equity and bond prices narrow over
longer periods, and the resulting relative volatility will generally be smaller.13 Thus,
the equity risk premium will converge on the country bond spread as we look at
longer-term expected returns. For example, the country risk premium for Brazil
would be 4.82 percent for the next year but decline over time to either the 2.00 percent (country default spread) or even lower.
Estimating Asset Exposure to Country Risk Premiums
Once country risk premiums have been estimated, the ﬁnal question that has to be addressed relates to the
exposure of individual companies within that country to country risk. There are
three alternative views of country risk:
1. Assume that all companies in a country are equally exposed to country risk.
Thus, for Brazil, with its estimated country risk premium of 4.82 percent, each
company in the market will have an additional country risk premium of 4.82 percent added to its expected returns. For instance, the cost of equity for Petrobras, an
integrated oil company listed in Brazil with a beta of 0.80, in U.S. dollar terms
would be (assuming a U.S. Treasury bond rate of 3.50 percent and a mature market
[U.S.] risk premium of 4.31 percent):
Expected cost of equity = 3.50% + 0.80(4.31%) + 4.82% = 11.77%
Note that the risk-free rate used is the U.S. Treasury bond rate and that the 4.31 percent is the equity risk premium for a mature equity market (estimated from historical
data in the U.S. market). The biggest limitation of this approach is that it assumes
that all ﬁrms in a country, no matter what their business or size, are equally exposed
to country risk. To convert this dollar cost of equity into a cost of equity in the local
currency, all that we need to do is to scale the estimate by relative inﬂation. To illustrate, if the Brazilian inﬂation rate is 6 percent and the U.S. inﬂation rate is 2 percent,
the cost of equity for Petrobras in Brazilian real (BR) terms can be written as:
Expected cost of equityBR = 1.1177(1.06/1.02) – 1 = 0.1615 or 16.15%
This will ensure consistency across estimates and valuations in different currencies.
Equity Risk Premium
171
13Jeremy Siegel reports on the standard deviation in equity markets in his book, Stocks for the
Very Long Run: The Deﬁnitive Guide to Investment Strategies (New York, McGraw-Hill,
2007), and notes that they tend to decrease with time horizon.
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
