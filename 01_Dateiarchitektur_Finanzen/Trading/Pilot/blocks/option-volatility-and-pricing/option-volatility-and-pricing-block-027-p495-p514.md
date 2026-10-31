# Option Volatility and Pricing_ Advanced Trading Strategies -- Sheldon Natenberg -- 2nd ed, 2014 -- McGraw Hill Professional -- isbn13 9780071818773 -- 6a48d008bd9beef283debf7bad0b2e4a -- Anna’s Archive.pdf — pages 495–514

--- page 495 ---

478
O P T I O N V O L AT I L I T Y A N D P R I C I N G
at-the-money options. Suppose that with three days remaining to expiration,
the Black-Scholes model generates a value for an at-the-money call of 0.75.
What can we say about this call? Although we may not know the exact value
because we don’t know the true future volatility, there is high likelihood that in
the real world the call is worth more than 0.75 because the model doesn’t know
about the possibility of a gap in the market. If, on top of this, the call is trading
at a price below its model-generated value, say, 0.65, it is likely to be a good buy.
As with any strategy based on volatility, the trader who buys these calls will
try to establish a delta-neutral position. Because of the synthetic relationship, if
the calls are underpriced, the puts at the same exercise price will also be underpriced. Thus, a logical strategy might be the purchase of at-the-money straddles.
This enables a trader to buy both underpriced calls and underpriced puts and to
profit if the underlying market gaps either up or down.
In theory, all volatility strategies, including an expiration straddle, ought
to be adjusted periodically to remain delta neutral. However, with little time
remaining to expiration, the model is not only unreliable with respect to theoretical values, but also unreliable with respect to deltas. Because it is impossible
to say what the right delta is, it is also impossible to say what the correct adjustment is. For this reason, traders who buy expiration straddles often abandon
any attempt to remain delta neutral and simply sit on the position to expiration.
This may not be the theoretically correct way to manage a volatility position,
but given all the uncertainties associated with theoretical evaluation as expiration approaches, it may be a practical choice.
Even if a trader carefully chooses his expiration straddles, the great majority of time no gap will occur in the market. In any single case, the trader is more
likely to show a loss than a profit. But the primary concern is not the profit or
loss5 from any single trade, but what happens in the long run. Returning to the
roulette example in Chapter 5, a player who chooses a number at a roulette
table can expect to win on average only 1 time in 38. But, if the theoretical
value of the bet is 95 cents and the player can buy the bet for less than 95 cents,
he expects to be a winner in the long run. Even if he is able to pay a very low
price for the bet, say, 50 cents, he still expects to lose 37 times out of 38. But
now the bet is very attractive. Even if he only wins 1 time in 38, this will still
more than offset the small losses he takes each time he loses. The same logic
is true of expiration straddles. A trader may lose several times before winning.
But when he does win, he can expect a return that is great enough to more than
offset all the small losses.
The fact that an at-the-money straddle may be cheap does not mean
that a trader should buy these straddles in large numbers. Such strategies
are likely to result in a loss more often than a profit, so an intelligent trader
should only invest an amount that he can afford to lose. However, when conditions are right, a trader ought to be willing to make the investment. Even if
he loses several times in succession, in the long run, he will encounter gaps in
the market or large increases in volatility often enough to make such strategies profitable.
5 This assumes, of course, that the trader is able to absorb the loss and still stay in business for the long run.
--- page 496 ---

M o d e l s a n d t h e R e a l W o r l d 	 479
Volatility Is Independent of the Price of the Underlying Contract
When a trader feeds a volatility into a theoretical pricing model, the volatility
defines a one standard deviation price change at any time during the life of the
option regardless of whether the underlying contract happens to be rising or falling
in price. If a contract is currently at 100 and we assume a volatility of 20 percent, a
one standard deviation price change is always based on this volatility of 20 percent.
If, at some later time during the life of the option, the contract should move up
to 125 or down to 75, the effective volatility is still assumed to be 20 percent.
In many markets, however, this assumption appears to be inconsistent with
most traders’ experience. If one were to ask a stock index trader whether his market becomes more volatile when rising or falling, he would probably say that it
becomes more volatile when falling. On the other hand, if one were to ask a commodity trader the same question, he likely would give the opposite answer. His
market will tend to become more volatile when rising. In other words, the volatility of a market is not independent of the price of the underlying contract. On the
contrary, the volatility over time seems to depend on the direction of movement
in the underlying contract. In some cases, a trader expects the market to become
more volatile if the movement is downward and less volatile if the movement is
upward; in other cases, a trader expects the market to become more volatile if the
movement is upward and less volatile if the movement is downward.
Because volatility in some markets seems to depend on the direction of
price movement in the underlying contract, a further variation of the Black-
Scholes model has been proposed. The constant-elasticity of variance (CEV) model 6
is based on the assumption that volatility changes as the price of the underlying contract changes. Price changes are still assumed to be random in the CEV
model, but the volatility, and consequently the magnitude of the price changes,
varies with the price of the underlying contract.
Like the jump-diffusion model, the CEV model is both mathematically complex and requires additional inputs in the form of a mathematical relationship
between the volatility and price movement in the underlying contract. Given these
difficulties, the CEV model has not found wide acceptance among option traders.
Underlying Prices at Expiration Are Lognormally Distributed
In the real world, do prices at expiration form a lognormal distribution? We
might try to answer this question by asking how the percent price changes are
distributed. If this distribution is normal, the continuous compounding of
price changes is likely to result in a lognormal distribution of prices.
Figure 23-8a is a histogram of daily Standard and Poor’s (S&P) 500
Index price changes for the 10-year period from 2003 through 2012. Each bar
represents the number of occurrences of a given price change rounded to the
6 For information on the CEV model, see John C. Cox and Stephen A. Ross, “The Valuation of Options for
Alternative Stochastic Processes,” Journal of Financial Economics 3(March):145–166, 1976; Stan Beckers, “The
Constant Elasticity of Variance Model and Its Implications for Option Pricing,” Journal of Finance, June 1980,
pp. 661–673; Mark Schroder, “Computing the Constant Elasticity of Variance Option Pricing Model,” Journal
of Finance 44(1):211–219, 1989; and Espen Gaarder Haug, The Complete Guide to Option Pricing Formulas, 2nd ed.
(New York: McGraw-Hill, 2006).
--- page 497 ---

480
O P T I O N V O L AT I L I T Y A N D P R I C I N G
nearest ¼ percent. As one would expect, most of the changes are relatively
small and close to 0. As we move away from the 0 in either direction, we encounter fewer and fewer occurrences. The distribution seems to have many of
the characteristics of a normal distribution. But is it really a normal distribution,
and if not, how does it differ from a true normal distribution?
Figure 23-8  (a) S&P 500 daily price changes: January 2003–December 2012. (b) Crude oil daily
price changes: January2003–December 2012. (c) Euro (versus dollar) daily price changes:
January 2003–December 2012. (d) Bund daily price changes: January 2003–December 2012.
0
25
50
75
100
125
150
175
200
225
250
275
300
325
350
375
–10%
–8%
–6%
–4%
–2%
0%
2%
4%
6%
8%
10%
12%
Daily price change (nearest 1/2 percent)
Number of occurrences
Number of days: 2,535
Biggest up move: +11.58% (October 13, 2008)
Biggest down move: –9.03% (October 15, 2008)
Mean: +0.296%
Standard deviation: 1.31%
Volatility: 20.81%
Skewness: –0.536
Kurtosis: +10.4150
More days with small moves
More days with
big moves
More days with
big moves
Fewer days with
intermediate moves
Fewer days with
intermediate moves
(a)
0
50
100
150
200
250
300
–12% –10% –8%
–6%
–4%
–2%
0%
2%
4%
6%
8%
10%
12%
14%
16%
Daily price change (nearest 1/2 percent)
Number of occurrences
Number of days: 2,514
Biggest up move: +14.27% (July 31, 2008)
Biggest down move: –10.80% (January 7, 2009)
Mean: +0.384%
Standard deviation: 2.25%
Volatility: 35.67%
Skewness: –0.188
Kurtosis: +2.6550
(b)
(continued)
--- page 498 ---

M o d e l s a n d t h e R e a l W o r l d 	 481
If the frequency distribution conforms exactly to a normal distribution, the
tops of the bars should coincide exactly with a true normal distribution. To find
out if this is the case, the mean (+0.0296 percent) and standard deviation (1.31
percent) have been calculated for all 2,535 daily price changes over the 10-year
period. From these numbers, a best-fit normal distribution has been overlaid on
the frequency chart. The actual frequency distribution is similar to the normal
distribution, but there are some clear differences. Because the bars representing
0
25
50
75
100
125
150
175
200
225
–3.0% –2.5% –2.0% –1.5% –1.0% –0.5% 0.0%
0.5%
1.0%
1.5%
2.0%
2.5%
3.0%
3.5%
4.0%
Daily price change (nearest.1%)
Number of occurrences
Number of days: 2,609
Biggest up move: +3.52% (March 18, 2009)
Biggest down move: –2.40% (October 24, 2008)
Mean: +0.110%
Standard deviation: 0.651%
Volatility: 10.52%
Skewness: +0.0669
Kurtosis: +1.4113
(c)
0
25
50
75
100
125
150
175
–1.75%
–1.50%
–1.25%
–1.00%
–0.75%
–0.50%
–0.25%
0.00%
0.25%
0.50%
0.75%
1.00%
1.25%
1.50%
1.75%
2.00%
2.25%
Daily price change (nearest .05%)
Number of occurrences
Number of days: 2,551
Biggest up move: +1.98% (November 1, 2011)
Biggest down move: –1.50% (September 2, 2003)
Mean: +0.0170%
Standard deviation: 0.364%
Volatility: 5.81%
Skewness: –0.0270
Kurtosis: +1.4388
(d)
Figure 23-8  (continued )
--- page 499 ---

482
O P T I O N V O L AT I L I T Y A N D P R I C I N G
the small price changes rise above the normal distribution curve, there seem
to be more days with small price changes than one would expect from a true
normal distribution. Although they are not as obvious, there are also several
large price changes, or outliers, that rise above the extreme tails of the normal
distribution. These outliers seem to suggest that there are more large moves in
our frequency distribution than one would expect from a true normal distribution. Finally, in the midsections, between the peak of the distribution and the
extreme tails, there seem to be fewer occurrences than one would expect.
One might surmise that the differences in Figure 23-8a between the S&P
500 frequency distribution and the true normal distribution are either unique
to the S&P 500 or an aberration of the 10-year period in question, which admittedly included the financial crisis of 2008. However, studies tend to indicate that price-change distributions for almost all exchange-traded underlying
markets exhibit characteristics that are very similar to the S&P 500 distribution. There are always more days with small moves, more days with large
moves, and fewer days with intermediate moves than are predicted by a true
normal distribution. The differences between the actual and theoretical distributions can also be seen in several other histograms covering the same period of time: crude oil (Figure 23-8b), the euro (Figure 23-8c), and the Bund
(Figure 23-8d).
Skewness and Kurtosis
Distributions such as those in Figure 23-8a through 23-8d are approximately
normal but still differ from a true normal distribution. If one is trying to make
decisions based on the characteristics of a distribution, it might be useful to
know how the actual distribution differs from the normal. A perfectly normal
distribution can be fully described by its mean and standard deviation. But two
other numbers, the skewness and kurtosis, are often used to describe the extent to
which an actual distribution differs from a true normal distribution.7
The skewness of a distribution (Figure 23-9) can be thought of as the lopsidedness of the distribution, or the extent to which one tail is longer than the
other tail. In a positively skewed distribution, the right tail is longer than the left
tail. (The lognormal distribution shown in Figure 6-7 is positively skewed.) In
a negatively skewed distribution, the left tail is longer than the right tail. A perfectly normal distribution has a skewness of 0. The frequency distribution in
Figure 23-8c (euro) is positively skewed, while the distributions in Figures 23-8a
(S&P 500), 23-8b (crude oil), and 23-8d (Bund) are negatively skewed.
The kurtosis of a distribution (Figure 23-10) is the extent to which the center of the distribution is either unusually tall or unusually flat. A distribution
with a positive kurtosis has a tall peak (leptokurtic), whiles a distribution with a
negative kurtosis has a low or flat peak (platykurtic). A perfectly normal distribution has a kurtosis of 0 (mesokurtic).8
7 The skewness and kurtosis functions are included in most commonly used spreadsheets. Their formulas can
be found in a statistics or probability textbook.
8 Mathematically, a true normal distribution has a kurtosis of 3. However, as commonly expressed, 3 is usually
subtracted from the kurtosis value, so a true normal distribution has a kurtosis value of 0.
--- page 500 ---

M o d e l s a n d t h e R e a l W o r l d 	 483
At first sight, a positive kurtosis distribution looks similar to a low standard
deviation distribution because both have high peaks. But a distribution with a
low standard deviation also has short tails, while a distribution with a positive
kurtosis has elongated tails. One might think of a positive kurtosis distribution
as a normal distribution where the midsection to the left and right of the peak
has been squeezed inward. This forces the peak of the distribution upward
and the tails outward. The frequency distributions in Figures 23-8a through
23-8d all exhibit the same positive kurtosis, which is typical of almost all exchange-traded underlying markets. They have higher peaks (more days with
small moves), elongated tails (more days with big moves), and narrow midsections (fewer days with intermediate moves) than are predicted by a true normal
distribution. Traders sometimes refer to these as “fat tail” distributions.
The S&P 500 distribution has an unusually large kurtosis value of 10.415.
To see the extent to which the tails of this distribution are abnormally fat, we
can express the biggest up and down moves in standard deviations and then
consider the chances of these moves occurring under the assumption of a normal distribution. The biggest up move in the S&P over the 10-year period was
11.58 percent. With a standard deviation of 1.31 percent, this translates into an
8.84 standard deviation occurrence. The probability of such an occurrence is
approximately 1 chance in 2,000,000,000,000,000,000 (2 quintillion, for anyone who is counting). The biggest down move, 9.03 percent, translates into a
6.75 standard deviation occurrence, with a probability equal to approximately
1 chance in 350,000,000,000 (350 billion). Simply put, the likelihood of either
of these occurrences is so small that they will essentially never occur.9
The kurtosis values for crude oil, the euro, and the Bund are not as dramatic as the S&P 500. But even in these markets under the assumptions of a
9 Nassim Taleb has referred to such unlikely occurrences as “black swans.” See Nassim Nicholas Taleb, The
Black Swan: The Impact of the Highly Improbable (New York: Penguin Books, 2008).
Figure 23-9  Skewness—the degree to which one tail of a distribution is longer than the
other tail.
Normal
distribution
Positive skewness
(right tail is longer)
Negative skewness
(left tail is longer)
--- page 501 ---

484
O P T I O N V O L AT I L I T Y A N D P R I C I N G
normal distribution, we would expect to see the biggest up and down moves
only once in many millions of occurrences. Keeping in mind that the data covered a period of between 2,500 and 2,600 days, we can see how much more
often big moves occur are in the real world compared with what is predicted
by a normal distribution. The probabilities associated with the largest moves in
our sample distributions are shown in Figure 23-11.
Figure 23-10  Kurtosis—the degree to which a distribution has a taller peak and wider tails.
Normal
distribution
Positive kurtosis
(more big occurrences and
more small occurrences)
Negative kurtosis
(fewer big occurrences and
fewer small occurrences)
Product
One
Standard
Deviation
Biggest Move
in Percent
Biggest Move in
Standard Deviations
Probability
S&P 500
1.31%
Up 11.58%
Up 8.84 st. dev.
Too unlikely to calculate
Down 9.03%
Down 6.89 st. dev.
1 chance in 358,000,000,000
Crude oil
2.25%
Up 14.27%
Up 6.34 st. dev.
1 chance in 8,700,000,000
Down 10.80%
Down 4.80 st. dev.
1 chance in 1,260,000
Euro
0.651%
Up 3.52%
Up 5.41 st. dev.
1 chance in 31,700,000
Down 2.40%
Down 3.69 st. dev.
1 chance in 8,900
Bund
0.364%
Up 1.98%
Up 5.40 st. dev.
1 chance in 30,000,000
Down 1.50%
Down 4.10 st. dev.
1 chance in 48,000
Figure 23-11  Probabilities associated with the biggest up and down moves.
--- page 502 ---

485
Volatility Skews
There are clearly real problems associated with the use of a traditional theoretical pricing model. Markets are not frictionless, prices do not always follow a diffusion process, volatility may vary over the life of an option, the real
world may not look like a lognormal distribution. With all these weaknesses,
one might wonder whether theoretical pricing models have any practical value
at all. In fact, most traders have found that pricing models, while not perfect,
are an invaluable tool for making decisions in the option market. Even if a
model does not work perfectly, traders have found that using a model, even a
flawed one, is usually better than using no model at all.
Still, a trader who wants to make the best possible decisions cannot
afford to ignore the problems associated with a theoretical pricing model. Consequently, a trader who uses a pricing model might look for a way to reduce
the potential errors resulting from these weaknesses. Initially, one might simply
look for a better theoretical pricing model. If such a model exists, it will certainly be worth replacing the old model with the new one. But better is a relative
term. A model might be better in the sense that it gives slightly more accurate
theoretical values. But if the model is extremely complex and difficult to use,
or if it requires additional inputs of which a trader cannot always be certain,
then the model may merely substitute one set of problems for another. Given
the fact that most traders are not theoreticians, a more realistic solution might
be to use a less complex model and somehow fine-tune it so that it is consistent
with the realities of the marketplace.
A trader trying to compensate for weaknesses in a pricing model might
make the assumption that the marketplace is using the same model as the
trader and then ask how the marketplace is dealing with the weaknesses in the
model. This is somewhat analogous to calculating implied volatility where we
assume that everyone is using the same model, that the price of the option is
known, and that everyone agrees on all the inputs except volatility. From these
assumptions, we are able to determine the volatility that the marketplace is
implying to the underlying contract. We can take the same general approach
but ask instead what weaknesses the marketplace is implying to the model.
24
--- page 503 ---

486
O P T I O N V O L AT I L I T Y A N D P R I C I N G
Figure 24-1 shows the implied volatilities across exercise prices for June
2012 FTSE 100 Index1 options traded on the London International Financial
Exchange on March 16, 2012. Calculations were made at the end of the trading
day from the average of the bid-ask spread using the Black-Scholes model. It is
immediately apparent that implied volatilities vary across exercise prices. If we
assume that the exercise price, time to expiration, underlying price, and interest rate are known, the theoretical value of an option in a Black-Scholes world
will depend solely on the volatility of the underlying contract over the life of
the option. Of course, we won’t know what that volatility is until we reach expiration, at which time we can look back and calculate the historical volatility
over the 13-week period from March 16 to June expiration. But the FTSE 100
Index can have only one volatility over this period. Because the underlying index
is the same for all options, it doesn’t make sense in a perfect Black-Scholes world
for every exercise price to have a different implied volatility. If the activity in the
marketplace were a result of everyone believing in the efficiency of the Black-
Scholes model, the selling of overpriced options and the buying of underpriced
options would eventually cause every option to have the same implied volatility.
Yet this almost never happens in any market.
The distribution of implied volatilities across exercise prices is often referred to as a volatility skew or, possibly, a volatility smile or volatility smirk depending
on the shape of the skew. One likely explanation for the distribution of implied volatilities has to do with the way in which options are used as a hedging
1 The Financial Times Stock Exchange 100 Index (the FTSE 100) is the most widely followed index of U.K.
stock prices.
Figure 24-1  June 2012 FTSE 100 implied volatilities: March 16, 2012.
Implied volatility
50%
45%
40%
35%
30%
25%
20%
15%
3000
3500
4000
4500
5500
5000
6000
6500
Exercise price
7000
10%
--- page 504 ---

V o l at i l i t y S k e w s 	 487
instrument. In the stock market, most investors are long stock2 and are therefore concerned about a decline in stock prices. The two most common hedging
strategies to protect a long underlying position, as described in Chapter 17, are
the purchase of protective puts and the sale of covered calls.
If a stock investor decides to purchase a protective put, which exercise
price will he choose? An out-of-the-money put costs less than an in-the-money
put but also offers less protection against a down move. However, if the investor
is so worried about a downward move that he needs the protection afforded by
an in-the-money put, he ought to simply sell the stock. The result is that most
protective puts are purchased at lower exercise prices.
If, instead, the investor decides to sell a covered call, he will almost always
do so at a higher exercise price. This will offer less protection than the sale of an
in-the-money call, but presumably the investor holds the stock because he believes that the stock price will rise. If it does rise, he will want to participate in at
least some of the upside profit potential. If the stock rises and the investor has
sold an in-the-money call, the stock will be quickly called away, limiting any upside profit. The result is that most covered calls are sold at higher exercise prices.
As a result of hedging activity, in the stock option market there tends to
be buying pressure on the lower exercise prices (the purchase of protective
puts) and selling pressure on the higher exercise prices (the sale of covered
calls). This causes the implied volatilities at lower exercise prices to rise and
the implied volatilities at higher exercise prices to fall. The resulting skew, such
as that in Figure 24-1, is sometimes referred to as an investment skew. It occurs
in markets in which people freely invest, the most obvious example being the
stock market. Traders sometimes describe an investment skew by saying that
the “skew is to the puts,” indicating that put implied volatilities are inflated. But
put-call parity dictates that if a put price is inflated, the call price at the same
exercise price must also be inflated, so perhaps it is more accurate to say that
the “skew is to the downside.”
While investors in the stock market may worry about falling stock prices,
in other markets hedgers may worry about rising prices. This is often the case
in commodity markets where end users try to protect themselves against rising prices by either buying protective calls at higher exercise prices or selling
covered puts at lower exercise prices. In the resulting demand or commodity skew
(there is a demand for the commodity), lower exercise prices have lower implied volatilities, and higher exercise prices have higher implied volatilities.
Of course, commodity producers, such as farmers, mining companies, and
oil drilling companies, are likely to worry about falling commodity prices, so
it might seem that there ought to be equal hedging activity between the longs
(producers) and the shorts (end users). But in many markets the end users tend
to dominate, perhaps because higher commodity prices, and the concomitant
inflationary pressures, are perceived as having a negative effect on the entire
economy. Moreover, in some countries, the government has a program of price
supports for agricultural products, so growers have less to worry about from
falling agricultural commodity prices than end users have from rising prices.
2 There are, of course, investors and traders who take short stock positions, but they are relatively small in number compared with those who are long stock.
--- page 505 ---

488
O P T I O N V O L AT I L I T Y A N D P R I C I N G
Finally, there are markets where both longs and shorts are equally worried. Consider a U.S. company buying goods in Europe that must be paid for
on some future date in euros. The company clearly is worried about a rising
euro compared with the dollar. At the same time, a European company may
buy goods in the United States that must be paid for in dollars. This company
is worried about a falling euro compared with the dollar. If both companies
choose to hedge their risk in the currency option market, the hedging activity
will tend to result in a balanced skew, where there is no obvious domination of
implied volatilities at either higher or lower exercise prices. This does not mean
that implied volatilities will necessarily form a flat skew, but the distribution of
implied volatilities is likely to be symmetrical around the current underlying
price. The three common types of skews are shown in Figure 24-2.
In addition to distortions caused by hedging activity, we also know from
Chapter 23 that there are inherent weaknesses in many models. For example,
most traders believe that stock markets become more volatile when they are falling and less volatile when they are rising. We also know that an option is most
sensitive to volatility changes (it has its highest vega) when it is at the money. If
an underlying stock is trading at 100 and the market begins to fall, the vega of
the 95 put will rise because it is becoming more at the money. If the market also
becomes more volatile because the stock price is falling, this will increase the
volatility value of the 95 put. But, if the market begins to rise, the 105 call, even
though its vega is rising, will not benefit to the same extent as the 95 put because
the market is becoming less volatile. So it should not come as a surprise that the
95 put carries a higher implied volatility and the 105 call a lower implied volatility than expected. This is consistent with an investment skew.
Figure 24-2  (a ) Investment skew. (b ) Demand skew. (c ) Balanced skew.
Exercise price
Implied volatility
Lower exercise prices are inflated.
(a )
--- page 506 ---

V o l at i l i t y S k e w s 	 489
Exercise price
Implied volatility
Higher exercise prices are inflated.
(b )
Exercise price
Implied volatility
Both lower and higher exercise prices are inflated.
(c )
--- page 507 ---

490
O P T I O N V O L AT I L I T Y A N D P R I C I N G
The marketplace, like every individual trader, is trying to evaluate options
as efficiently as possible given all available information. Whether one believes
that markets are efficient or not, one can argue that the marketplace is trying to
be efficient. From the wide range of implied volatilities found in almost every
option market, we can reasonably infer that the marketplace does not think the
Black-Scholes model is perfectly efficient. Unfortunately, trying to identify the
source of the inefficiency may not be possible. It might have to do with how options are used in hedging strategies. Or it might have to do with weaknesses in
the theoretical pricing model. Whatever the reason, we can make the assumption that at any moment in time the marketplace believes that options are priced
efficiently, even if those prices happen to differ from model-generated values.
An option trader using a theoretical pricing model might take the view that
the volatility skew contains useful information that can be used in the decisionmaking process. By treating the volatility skew as an additional input into the
theoretical pricing model, the skew becomes an important aid in generating
theoretical values and managing risk. Moreover, analysis of the skew can form
the basis for a variety of option strategies.
Modeling the Skew
If we want to include a skew in our model, we need to do it in a way that the
model understands. This is typically done using a mathematical function that
generates a best fit for the skew
f(x) = y
where y is the implied volatility at each exercise price x. A trader can choose any
function that seems to yield a good fit, but many traders use a polynomial function of the form a + bx + cx2 + dx3 + …. A best-fit function for the implied volatilities in Figure 24-1 is shown in Figure 24-3.
If we think of the skew as an input into the model, then, as with all inputs,
we need to ask how changes in the input will affect a position. If we can model
possible changes in the skew as market conditions change, we will be in a better position to assess the risk associated with an option position. In particular, as
market conditions change, we will want to model both the location and shape
of the skew.
Of course, we might take the position that the location and shape of the
volatility skew will remain fixed. Under this sticky-strike assumption, the current
skew determines the implied volatility at each strike regardless of how market
conditions change.
Unfortunately, a sticky-strike skew, with its fixed volatilities at each exercise
price, is not consistent with the observed dynamics of the marketplace. In most option markets, the skew will shift as the underlying price moves or implied volatility changes. An alternative approach is to use a floating skew, where the entire skew
is shifted horizontally as the underlying price rises or falls or vertically as implied
volatility rises or falls. The shift is equal to the amount of change in either the price
or volatility. If the underlying price rises five points, the skew is shifted to the right
--- page 508 ---

V o l at i l i t y S k e w s 	 491
by five points. If implied volatility falls by two percentage points, the skew is shifted
downward by two percentage points. This type of skew is shown in Figure 24-4.
Figure 24-3  June 2012 FTSE 100 implied volatilities: March 16, 2012.
Implied volatility
50%
45%
40%
35%
30%
25%
20%
15%
3,000
3,500
4,000
4,500
5,500
5,000
6,000
6,500
Exercise price
7,000
10%
Figure 24-4  (a ) A simple floating skew as the underlying price changes. (b ) A simple
floating skew as implied volatility changes.
Implied volatility
Exercise price
(a)
If the underlying market
falls, the skew is shifted
to the left by that amount.
If the underlying market
rises, the skew is shifted
to the right by that amount.
--- page 509 ---

492
O P T I O N V O L AT I L I T Y A N D P R I C I N G
Shifting the entire skew might be a reasonable approach if a trader
believes that the shape of the skew will remain unchanged regardless of changing market conditions. But is this likely? The implied volatilities at different
exercise prices are likely to depend on how the marketplace views the likelihood
of either larger or smaller moves in the price of the underlying contract. But
all moves are relative with respect to both the underlying price and the time to
expiration. In relative terms, a price change of 10.00 is greater with an underlying price of 100 (a 10 percent move) than with an underlying price of 200
(a 5 percent move). In the same way, a 10 percent move is greater over a oneweek period than the same 10 percent move over a one-month period.
A first step in adjusting for the relative magnitude of price changes is to express each exercise price along the x axis in terms of its moneyness—how far in
the money or out of the money the exercise price is as a percent of the underlying price. The 90 exercise price with the underlying price at 100 will have a
moneyness of 0.90. This is the same moneyness as the 180 exercise price with
an underlying price of 200. We can make a further refinement by expressing
each exercise price in logarithmic terms ln (X/S), where S is the underlying or
spot price and X is the exercise price. This is consistent with the assumption
that underlying prices are lognormally distributed.
How will the passage of time affect the shape of the volatility skew? Consider a 90 put with the underlying contract trading at 100. As time passes, in
relative terms, the 90 put is moving further out of the money. In an investment
skew, as the option moves further out of the money, its implied volatility will rise.
In a sense, it is moving “up the skew.” This will cause the skew to appear more
severe as time passes, with lower exercise prices carrying increasingly higher
implied volatilities. Higher exercise prices may also be affected by the passage
of time because an out-of-the-money call will also go further out of the money.
Implied volatility
Exercise price
(b)
If implied volatility rises,
the skew is shifted
upward by that amount.
If implied volatility falls,
the skew is shifted
downward by that amount.
--- page 510 ---

V o l at i l i t y S k e w s 	 493
Depending on the shape of the skew and where an exercise price falls along the
skew, its implied volatility may rise, fall, or remain the same. If no adjustment is
made, the effect of time passing on the FTSE 100 skew is shown in Figure 24-5.
To compare volatility skews for different expirations, we need to determine
theoretically how far in the money or out of the money an option is. Perhaps the
easiest way to do this is to express each exercise price in terms of standard deviations away from at the money. Recalling the square-root relationship between
time and volatility, and using our logarithmic scale, the number of standard
deviations in the money or out of the money for each exercise price is given by
X S
t
ln(
/ )
σ
with an exactly at-the-money3 option having a standard deviation of 0. Skews for
several FTSE 100 option expirations as of March 16, 2012, are shown in Figure
24-6. When expressed in this format, the skew is sometimes referred to as a stickydelta skew because the delta is an approximation of how far in the money or out
of the money an option is.
The skews in Figure 24-6 appear to be similar, but they are clearly not identical. All adjustments thus far have been to the x axis, changing the calibration to more easily compare exercise prices. But we might also adjust the y axis,
3 A more theoretically correct approach involves using the forward price F rather than the spot price, S
X S
t
ln(
/ )
σ
In this case, the at-the-forward option has a standard deviation of 0.
Figure 24-5  FTSE 100 option implied volatilities, March 16, 2012 (FTSE = 5965.58).
Implied volatility
50%
45%
40%
35%
30%
25%
20%
15%
2,500
3,500
3,000
4,000
4,500
5,000
5,500
6,000
6,500
Exercise price
7,000
10%
June options (3 months to expiration)
December options (9 months to expiration)
April options (1 month to expiration)
--- page 511 ---

494
O P T I O N V O L AT I L I T Y A N D P R I C I N G
the volatility. When a trader refers to the overall implied volatility in a market,
he is almost always referring to the implied volatility of at-the-money options.
Whether the implied volatility at any exercise price is high or low will depend on
whether it is high or low compared with the at-the-money implied volatility. As a
result, many traders recalibrate the y axis in terms of how the implied volatility
at an exercise price compares with the at-the-money implied volatility. We can
do this by expressing y values as the difference between the implied volatility of
an at-the-money option and the implied volatility at each exercise price. If the
at-the-money implied volatility is 20 (percent) and the implied volatility at an exercise price is 25 (percent), the y value is 20 – 25 = –5. If the implied volatility at
a different exercise price is 18 (percent), the y value is 20 – 18 = 2.
This method may be satisfactory if implied volatilities remain relatively constant, but suppose that the at-the-money implied volatility doubles from 20 to
40 percent. We might also expect the volatility at each exercise to double. An exercise price that previously had an implied volatility of 25 percent will now have
an implied volatility of 50 percent, and an exercise price that previously had an
implied volatility of 18 percent will now have an implied volatility of 36 percent.
We can better calibrate the y axis by expressing the volatility at each exercise price
as a percent of at-the-money implied volatility. With an at-the-money implied
volatility of 20 percent, an implied volatility of 25 percent would be expressed as
25/20 = 125 percent. An implied volatility of 18 percent would be expressed as
18/20 = 90 percent. And an implied volatility equal to the at-the-money implied
Figure 24-6  FTSE 100 implied volatilities, March 16, 2012.
Implied volatility
50%
45%
40%
35%
30%
25%
20%
15%
–5
–4
–3
–2
0
–1
1
Exercise price
(standard deviations)
2
10%
April 2012 (1 month)
May 2012 (2 months)
June 2012 (3 months)
September 2012 (6 months)
December 2012 (9 months)
--- page 512 ---

V o l at i l i t y S k e w s 	 495
volatility would be expressed as 20/20 = 100 percent. In Figure 24-7, the y axis
for the sample FTSE 100 skews has been recalibrated using this approach.
Figure 24-7 is typical of many stock indexes, exhibiting a very pronounced investment skew, with lower exercise prices significantly inflated
compared with higher exercise prices. A different set of skews, for wheat options, is shown in Figure 24-8. In this example, the skews exhibit more curvature but with higher exercise prices somewhat more inflated, as is often the
case with a demand or commodity skew. The skews also seem to exhibit less
consistency across different expiration months than the FTSE 100. While
skews in a financial product tend to be similar across expiration months,
skews in a commodity market can often vary across different expirations,
perhaps owing to seasonal volatility considerations or because of short-term
supply and demand imbalances.
The foregoing method of modeling a skew is used by many traders but is
in no way meant to be definitive. Adjustments are often required to prevent
the model from generating illogical volatilities or theoretical values. For example, as we reduce volatility, an out-of-the-money option goes further out of
the money because it is a greater number of standard deviations away from
the underlying price. But in an investment skew, as a put goes further out of
the money, it’s volatility is rising—it is “climbing the skew.” If the skew is sufficiently steep, the increase in volatility may in fact cause the theoretical value of
the put to rise. This is inherently illogical because we expect all option values to
decline if we reduce volatility.
Figure 24-7  FTSE 100 implied volatilities, March 16, 2012.
Percent of at-the-money implied volatility
250%
225%
200%
175%
150%
125%
100%
75%
–5
–4
–3
–2
0
–1
1
Exercise price
(standard deviations)
2
50%
April 2012 (1 month)
May 2012 (3 months)
June 2012 (3 months)
September (6 months)
December 2012 (9 months)
--- page 513 ---

496
O P T I O N V O L AT I L I T Y A N D P R I C I N G
Skewness and Kurtosis
The shape of the skew is not constant. As market conditions change, option prices
will also change, often causing the shape of the skew to change. Two common
changes have to do with the tilt and curvature of the skew. The tilt, which defines
how much the implied volatilities of lower exercise prices differ from the implied
volatilities of higher exercise prices, is often referred to as the skewness. This follows
logically from the definition of skewness in Chapter 23 (see Figure 23-10). If the
probability distribution has a longer left tail (negative skewness), there is greater
likelihood of large down moves, resulting in greater demand for lower exercise
prices. If the distribution has a longer right tail (positive skewness), there is greater
likelihood of large up moves and, consequently, greater demand for higher exercise prices. Examples of positive and negative skewness are shown in Figure 24-9.
The curvature, or kurtosis, defines how much the implied volatilities of both
higher and lower exercise prices are inflated compared with the at-the-money
implied volatility. This also follows logically from the definition in Chapter 23
(see Figure 23-11). If the probability distribution has “fat tails,” there is a greater
likelihood of large moves in either direction. Consequently, there will be a greater
demand for out-of-the-money options (positive kurtosis). Examples of increasing
positive kurtosis are shown in Figure 24-10.4
4 Because all exchange-traded markets seem to exhibit positive kurtosis, we ignore negative kurtosis skews.
Figure 24-8  Wheat implied volatilities, January 27, 2012.
Fraction of at-the-money implied volatility
1.20
1.15
1.10
1.05
1.00
–2.5
–2
–1.5
–1
–0.5
0
0.5
1
1.5
2
2.5
Exercise price
(standard deviations)
3
0.95
March 2012 (1 month)
May 2012 (3 months)
July 2012 (5 months)
September 2012 (7 months)
December 2012 (10 months)
--- page 514 ---

V o l at i l i t y S k e w s 	 497
Figure 24-9  Skewness.
Negative skewness
(lower exercise prices carry
higher implied volatilities)
Positive skewness
(higher exercise prices carry
higher implied volatilities)
Zero skewness
(the volatility skew is
symmetrical)
Higher exercise prices
Implied volatility
Lower exercise prices
At the money
Figure 24-10  Kurtosis.
The implied volatility of both lower
and higher exercise prices increases.
As kurtosis increases, the volatility
skew becomes more curved.
Zero kurtosis
(the volatility skew
is a straight line)
Higher exercise prices
Implied volatility
Lower exercise prices
At the money
We might think of the skew as an input into a theoretical pricing model
(Figure 24-11), but the skew is input into the model as a formula rather than as
