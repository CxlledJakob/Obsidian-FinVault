# Volatility Trading_ Sinclair_Volatility Trading -- Euan Sinclair(auth_) -- Wiley Trading, 1, 2013 -- John Wiley & Sons, Incorporated -- isbn13 9781118347133 -- 2634a86bfed8248fa7ba3fb72595bbbc -- Anna’s Archive.pdf — Chapter 9: Trade Evaluation — ABOUT THE WEBSITE (pages 285–285)

--- page 285 ---

ABOUT THE WEBSITE
276
■Trade Evaluation
This sheet is a template for the posttrade evaluation process. Daily proﬁt
and losses (P/Ls) are entered in Column C and haircuts in Column H. The
interest rate is entered in cell E2.
■Trading Goals
In this case we simulate the results of a strategy with a given expected P/L
and Sharpe ratio (cells C3 and C4). It plots 20 realizations of the process
over half a year. Clearly even very good traders can have very mediocre
results over the short term. Use the F9 key to recalculate.
■Corrado-Su Skew Curve
This sheet uses least squares and Solver to extract the implied volatility,
skewness, and kurtosis consistent with the Corrado-Su model, from the
quoted call option prices. This sheet makes use of the Solver add-in so it is
not protected. Set the parameters in cells C2 through C4. Set the lowest
strike in cell E3. Enter the call midmarket prices in cells H3 through H9.
Open Solver. It should be set to minimize cell J2 (the sum of the squares of
the differences of the market prices and the Corrado-Su prices) by changing
cells C5 through C7. The implied volatility curve as a function of strike can
be produced either by entering the implied volatilities directly into cells F3
through F9 or by using Solver. For example, to obtain the implied volatility
of the 35 strike, use Solver to minimize the difference between cells G3 and
H3 by changing cell F3.
■Mean Reversion Simulator
Here we have a simulation for trading a mean-reverting process using the
rules in Chapter 6. The tab ‘‘‘Normal Noise’ simple’’ uses a modiﬁed rule
to enter a trade where the underlying is driven by an Ornstein-Uhlenbeck
process with normally distributed innovations with a standard deviation of
one. The entry level is set by changing cell J3. A value of 2 means we enter
the trade when we deviate from fair value by two standard deviations. At
this point we commit half our available wealth. The position is held until
the asset returns to fair value. The tab ‘‘‘normal noise’ exact’’ scales our
