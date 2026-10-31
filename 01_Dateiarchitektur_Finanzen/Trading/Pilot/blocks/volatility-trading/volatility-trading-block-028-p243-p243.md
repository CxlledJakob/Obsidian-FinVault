# Volatility Trading_ Sinclair_Volatility Trading -- Euan Sinclair(auth_) -- Wiley Trading, 1, 2013 -- John Wiley & Sons, Incorporated -- isbn13 9781118347133 -- 2634a86bfed8248fa7ba3fb72595bbbc -- Anna’s Archive.pdf — Chapter 9: Trade Evaluation — C H A P T E R 1 3 (pages 243–243)

--- page 243 ---

231
C H A P T E R 1 3
Leveraged ETFs
R
ecently, many leveraged exchange-traded fund (ETFs) have been listed.
These aim to magnify the daily returns of a given reference product.
For example, SSO returns twice the daily return of the S&P 500. The
leverage ratio is speciﬁed in the prospectus and is ﬁxed. Leverage ratios of
3, 2, −1, −2, and −3 are available. The crucial point to note is that the
relevant returns for most such products are daily returns (a smaller number
of ETFs that leverage monthly returns are also available). This leads to
confusion as many people misunderstand the way returns compound.
The confusion leads to the following myth: Leveraged ETFs decay to
zero.
Posts that promulgate this can be found all over the internet, but the
following from elitetrader.com are typical in their misunderstanding, even
if they are more quotable than many others.
‘‘Designed mathematically to go to zero’’ and ‘‘these toys/pieces of crap
are for those who will be separated from their money soon.’’
In this chapter we show that this myth is false. These instruments are
actually perpetual realized volatility products and that understanding them
leads to several volatility dependent trades.
The effect of volatility can easily be seen by considering a simple example.
Consider a traded instrument that on the ﬁrst day goes up 5 percent and
then on the second day it drops by 5 percent. So if it were initially trading
at $100 its price series would be $100, $105, $99.75. Even though we have
had two equal-size percentage moves in opposite directions, a long position
would have lost money. Algebraically this can be expressed as
(1 + x)(1 −x) = 1 −x2 < 1
(13.1)
(where x is the daily return). This is called volatility drag and occurs for all
instruments. But if we have leverage the returns are larger and the effect
Volatility Trading,   Second Edition.    Euan Sinclair
© 2013 Euan Sinclair. Published 2013 by John Wiley & Sons, Inc.
