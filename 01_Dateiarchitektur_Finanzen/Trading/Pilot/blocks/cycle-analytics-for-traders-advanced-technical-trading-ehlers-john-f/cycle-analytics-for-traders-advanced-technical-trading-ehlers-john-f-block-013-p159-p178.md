# Cycle Analytics for Traders (Advanced Technical Trading -- Ehlers, John F_ -- 10_1002_9781118728611, 2013 nov 18 -- John Wiley & Sons, Inc_ -- doi 10_1002_9781118728611 -- 1af2315757f5680b2f83029a006fd7ab -- Anna’s .pdf — Chapter 9: Fourier Transforms (pages 159–178)

--- page 159 ---

154
CYCLE ANALYTICS FOR TRADERS
Code Listing 11-4. (Continued)
Spx(0),
MaxPwr(0),
DominantCycle(0);
Arrays:
Corr[48](0),
CosinePart[48](0),
SinePart[48](0),
SqSum[48](0),
R[48, 2](0),
Pwr[48](0);
//Highpass filter cyclic components whose periods are
shorter than 48 bars
alpha1 = (Cosine(.707*360 / 48) + Sine (.707*360 / 48) - 1) /
Cosine(.707*360 / 48);
HP = (1 - alpha1 / 2)*(1 - alpha1 / 2)*(Close - 2*Close[1] +
Close[2]) + 2*(1 - alpha1)*HP[1] - (1 - alpha1)*
(1 - alpha1)*HP[2];
//Smooth with a Super Smoother Filter from equation 3-3
a1 = expvalue(-1.414*3.14159 / 10);
b1 = 2*a1*Cosine(1.414*180 / 10);
c2 = b1;
c3 = -a1*a1;
c1 = 1 - c2 - c3;
Filt = c1*(HP + HP[1]) / 2 + c2*Filt[1] + c3*Filt[2];
//Pearson correlation for each value of lag
For Lag = 0 to 48 Begin
//Set the averaging length as M
M = AvgLength;
If AvgLength = 0 Then M = Lag;
Sx = 0;
Sy = 0;
Sxx = 0;
Syy = 0;
Sxy = 0;
For count = 0 to M - 1 Begin
X = Filt[count];
--- page 160 ---

155
ADAPTIVE FILTERS
(Continued)
Code Listing 11-4. (Continued)
Y = Filt[Lag + count];
Sx = Sx + X;
Sy = Sy + Y;
Sxx = Sxx + X*X;
Sxy = Sxy + X*Y;
Syy = Syy + Y*Y;
End;
If (M*Sxx - Sx*Sx)*(M*Syy - Sy*Sy) > 0 Then Corr[Lag] =
(M*Sxy - Sx*Sy)/SquareRoot((M*Sxx - Sx*Sx)*(M*Syy - Sy*Sy));
End;
For Period = 10 to 48 Begin
CosinePart[Period] = 0;
SinePart[Period] = 0;
For N = 3 to 48 Begin
CosinePart[Period] = CosinePart[Period] +
Corr[N]*Cosine(360*N / Period);
SinePart[Period] = SinePart[Period] + Corr[N]*Sine(360*N /
Period);
End;
SqSum[Period] = CosinePart[Period]*CosinePart[Period] +
SinePart[Period]*SinePart[Period];
End;
For Period = 10 to 48 Begin
R[Period, 2] = R[Period, 1];
R[Period, 1] = .2*SqSum[Period]*SqSum[Period] +
.8*R[Period, 2];
End;
//Find Maximum Power Level for Normalization
MaxPwr = .995*MaxPwr;
For Period = 10 to 48 Begin
If R[Period, 1] > MaxPwr Then MaxPwr = R[Period, 1];
End;
For Period = 3 to 48 Begin
Pwr[Period] = R[Period, 1] / MaxPwr;
End;
//Compute the dominant cycle using the CG of the spectrum
Spx = 0;
Sp = 0;
--- page 161 ---

156
CYCLE ANALYTICS FOR TRADERS
Code Listing 11-4. (Continued)
For Period = 10 to 48 Begin
If Pwr[Period] >= .5 Then Begin
Spx = Spx + Period*Pwr[Period];
Sp = Sp + Pwr[Period];
End;
End;
If Sp <> 0 Then DominantCycle = Spx / Sp;
If DominantCycle < 10 Then DominantCycle = 10;
//Adaptive BandPass indicator tunes a BandPass filter to 90%
of the period of the Dominant Cycle
Vars:
gamma1(0),
alpha2(0),
beta1(0),
BP(0),
Peak(0),
Signal(0),
Lead(0),
LeadPeak(0),
LeadSignal(0);
beta1 = Cosine(360 / (.9*DominantCycle));
gamma1 = 1 / Cosine(360*Bandwidth / (.9*DominantCycle));
alpha2 = gamma1 - SquareRoot(gamma1*gamma1 - 1);
BP = .5*(1 - alpha2)*(Filt - Filt[2]) + beta1*(1 +
alpha2)*BP[1] - alpha2*BP[2];
If Currentbar = 1 or CurrentBar = 2 Then BP = 0;
Peak = .991*Peak[1];
If AbsValue(BP) > Peak Then Peak = AbsValue(BP);
If Peak <> 0 Then Signal = BP / Peak;
Lead = 1.3*(Signal + Signal[1] - Signal[2] - Signal[3]) / 4;
LeadPeak = .93*LeadPeak[1];
If AbsValue(Lead) > LeadPeak Then LeadPeak = Absvalue(Lead);
If LeadPeak <> 0 Then LeadSignal = .7*Lead / LeadPeak;
Plot1(Signal);
Plot14(.9*Signal[1]);
Plot2(0);
Plot6(.707);
Plot10(-.707);
--- page 162 ---

157
ADAPTIVE FILTERS
The adaptive band-pass filter has been applied to Dollar General (symbol
DG) over roughly the past year in Figure 11.4. This indicator accurately displays cyclic entry points when the two indicator lines cross outside the plus
or minus 0.7 reference lines.

■Adaptive Indicator Comparison
It is instructive to view the adaptive indicators on a single chart so they can be
compared on a head-to-head basis. This comparison is available in Figure 11.5.
The most striking difference is that the band-pass filter has more high-
FIGURE 11.4
The Adaptive Band-Pass Filter Shows Buying and Selling
Opportunities
FIGURE 11.5
Comparison of the Adaptive Indicators
--- page 163 ---

158
CYCLE ANALYTICS FOR TRADERS
frequency components. It is also apparent to me that the RSI, Stochastic, and
CCI all pretty much indicate the same thing in the broad general sense. Without indicator transforms to enhance interpretation, which we cover in Chapter 15, there is no overwhelming reason to select one indicator over another.

■Key Points to Remember
1. When length is an input parameter to any indicator, that indicator can
often be optimized by tuning that length to the dominant cycle period
or a fraction thereof.
2. The preferred method of computing the dominant cycle is using the
autocorrelation periodogram.
3. The RSI indicator is optimized over half the period of the measured
dominant cycle to reach full-scale swings without oversaturation.
4. The stochastic indicator is optimized over the full period of the measured dominant cycle to ensure the highest close and the lowest close
have been included.
5. The CCI indicator is optimized over the full period of the measured
dominant cycle to ensure a complete measurement of the standard
deviation.
6. The band-pass filter is optimized by tuning the filter to 90 percent of
the measured dominant cycle period. This provides an approximate
60-degree phase lead in the indicator.
Notes
1. P. J. Kaufman, Trading Systems and Methods, 3rd ed. (New York: John
Wiley & Sons, 1998), pp. 436–438.
2. T. S. Chande and S. Kroll, The New Technical Trader (New York: John Wiley
& Sons, 1994).
3. J. Welles Wilder, Jr., New Concepts in Technical Trading Systems (Winston-
Salem, NC: Hunter, 1978).
4. D. Lambert, Commodities Magazine, October 1980.
--- page 164 ---

159
The Even Better
Sinewave Indicator
“This is heavy stuff,” said Tom lighty.
C H A P T E R 1 2
I
first introduced the Sinewave Indicator as early as 1996.1,2 The concept
was based on the idea that no technical indicator is predictive. All indicators rely on historical data, and are therefore their signals are always lagging.
However, cycles exist in the market, and it is often true that an observed
cycle will continue for a short while into the future. Therefore, if we can
transfer the cyclic data swings to a sine wave, we can then artificially advance
the phase of the sine wave to create a predictive indicator.
Two conditions must be satisfied to make the Sinewave Indicator useful. First, the market must be in a cycle mode. Making a cyclic prediction
when the data are in a trend is basically futile. Second, the period of the
dominant cycle must be estimated with reasonable accuracy. The downside
of the Sinewave Indicator is that the amplitude swings must be from −1 to
+1, and therefore there is no direct indication of when the market is in a
trend mode.
Since the roofing filter gives control of the frequency content of the
data to be analyzed, the basic idea is to use the frequency content to an
advantage. This control enables the Even Better Sinewave Indicator to not
only enter a trade as quickly as possible, but also use the trend component to give the confidence to stay with an existing trade without being
whipsawed.
Cycle Analytics for Traders: Advanced Technical Trading Concepts. John F. Ehlers.
© 2013 John F. Ehlers. Published 2013 by John Wiley & Sons, Inc.
--- page 165 ---

160
CYCLE ANALYTICS FOR TRADERS

■Even Better Sinewave Approach
The original Sinewave Indicator was created by seeking the dominant cycle
phase angle that had the best correlation between the price data and a theoretical dominant cycle sine wave. The Even Better Sinewave Indicator skips
all the cycle measurements completely and relies on a strong normalization of the waveform at the output of a modified roofing filter. The modified roofing filter uses a single-pole high-pass filter to deliberately retain the
longer-period trend components. The single-pole high-pass filter basically
levels the amplitude of all the cycle components that would otherwise be
larger with longer wavelengths due to Spectral Dilation. Therefore, when
the waveform is normalized to the power in the waveform over a short period of time, the longer wavelength contributions tend to be an indication
to stay in a trade when the market is in a trend.
The Even Better Sinewave Indicator works extraordinarily well when the
market is in a trend mode. This means that the spectacular failures of most
swing wave indicators are mitigated when the expected price turning point
does not occur.
Although I have not studied it extensively, it appears that the Even Better
Sinewave Indicator works well on futures intraday data. It takes a position in
the correct direction and tends to stay with the good trades without excessive whipsawing.

■Even Better Sinewave Description
The Even Better Sinewave Indicator is described with reference to the
EasyLanguage code given in Code Listing 12-1. The only user input for the
indicator is the expected maximum duration of the trades when the market
is in a trend. Making the duration input parameter shorter will increase the
number of trades over a given time span, and will have a minor effect of
entering the trades a little sooner. Conversely, increasing the duration input
parameter has the primary effect of holding and indicated trade position
longer.
After declaring variables, the data is filtered in a single-pole high-pass filter. A single-pole high-pass filter is deliberately selected to equalize the data
spectrum and allow trending components through the filter into the indicator. The degree of the spectrum allowed through the filter is established by
the duration input. The value of the duration input is set to be approximately
--- page 166 ---

161
THE EVEN BETTER SINEWA
W V
A E INDICATOR
the length of a trade position in a continuing trend. The default value of the
duration input is 40 bars, so a maximum trade duration of about two months
can be expected with this setting. Increasing the duration input will increase
the maximum duration of a trade in a trend. This has the implication that
you will be working through some additional drawdowns throughout the
trade with the benefit that you will not be whipsawed out of a profitable
trending trade.
The high-pass filtered data is then filtered in a SuperSmoother filter
whose critical period is set to 10 bars.
After the data is passed through the modified roofing filter the threebar average of the wave amplitude and the power are computed. Power is
proportional to the square of the wave amplitude. The Even Better Sinewave is then computed by normalizing the averaged wave amplitude to
the square root of the averaged power, causing the indicator to swing between −1 and +1.
Code Listing 12-1. Even Better Sinewave
Indicator EasyLanguage Code
{
Even Better Sinewave Indicator
© 2013  John F. Ehlers
}
Inputs:
Duration(40);
Vars:
alpha1(0),
HP(0),
a1(0),
b1(0),
c1(0),
c2(0),
c3(0),
Filt(0),
count(0),
Wave(0),
Pwr(0);
(Continued)
--- page 167 ---

162
CYCLE ANALYTICS FOR TRADERS

■Using the Even Better Sinewave Indicator
The Even Better Sinewave Indicator is shown in Figure 12.1, using the default duration setting of 40 bars. This means that the maximum length of
a trade when the market is in a trend is about two months. This is because
the high-pass filter starts to attenuate the cyclic components that are longer
than 40 bars.
Interpretation of the Even Better Sinewave is simple. Hold a long position when the indicator value is near +1, and hold a short position (or go flat
if trading to the long side only) when the indicator value is near −1.
The trade duration in a trend can be extended just by increasing the duration input value. For example, the indicator using a duration value of 40
is shown in Figure 12.2. Sure enough, the indicated long position in the
uptrend is extended. Doing this causes some of the short-term reversals
during the trend to be eliminated. The duration input parameter is adjusted
to fit your trading style.
Code Listing 12-1. (Continued)
//HighPass filter cyclic components whose periods are
shorter than Duration input
alpha1 = (1 - Sine (360 / Duration)) / Cosine(360 /
Duration);
HP = .5*(1 + alpha1)*(Close - Close[1]) + alpha1*HP[1];
//Smooth with a Super Smoother Filter from equation 3-3
a1 = expvalue(-1.414*3.14159 / 10);
b1 = 2*a1*Cosine(1.414*180 / 10);
c2 = b1;
c3 = -a1*a1;
c1 = 1 - c2 - c3;
Filt = c1*(HP + HP[1]) / 2 + c2*Filt[1] + c3*Filt[2];
//3 Bar average of Wave amplitude and power
Wave = (Filt + Filt[1] + Filt[2]) / 3;
Pwr = (Filt*Filt + Filt[1]*Filt[1] + Filt[2]*Filt[2]) / 3;
//Normalize the Average Wave to Square Root of the Average
Power
Wave = Wave / SquareRoot(Pwr);
Plot1(Wave);
--- page 168 ---

163
THE EVEN BETTER SINEWA
W V
A E INDICATOR
Conversely, decreasing the duration input parameter shortens the maximum trade length when the market is in a trend, being more sensitive to the
shorter wavelengths in the data. For example, Figure 12.3 shows the indicator when the duration input is set to 20 bars. Some care should be taken
when shortening the duration input because the resulting shorter trades
are more sensitive to entry and exit timing and computational lag of the
indicator.
FIGURE 12.1
The Default Even Better Sinewave Indicator Holds a Position
for about Two Months in a
T
Trend
T
FIGURE 12.2
Trade
T
Position Length is Increased by Increasing the
Duration Input Parameter
--- page 169 ---

164
CYCLE ANALYTICS FOR TRADERS

■Key Points to Remember
1. The Even Better Sinewave Indicator is a variant of the roofing filter, using a single-pole high-pass filter.
2. The unambiguous signals of the Even Better Sinewave Indicator are generated by normalizing the wave amplitude to the square root of the
power.
3. The only input for the Even Better Sinewave Indicator is the duration
parameter.
4. The duration parameter controls the maximum length of an indicated
position by setting the critical period of the high-pass filter.
Notes
1. John F. Ehlers, “Stay in Phase,” Stocks & Commodities, November 1996,
Vol. 14,
V
No. 11, p. 69.
2. John F. Ehlers, Rocket Science for Traders: Digital Signal Processing Applications (Hoboken, NJ: JohnWiley & Sons, 2001), Chapter 9.
FIGURE 12.3
Decreasing the Duration Input Parameter Make the
P
Even
Better Sinewave Indicator More Sensitive to Short-Term Variations in the Data
T
--- page 170 ---

165
Convolution
“I need to know when the market reverses,” said Tom pointedly.
C H A P T E R 1 3
O
ne of the major objectives of technical analysis is to decisively identify
a major reversal so that one can trade the market primarily in the
direction of the ensuing trend. Convolution is just the ticket to meet that
objective.
In mathematics, convolution is an operation on two functions that produces a third function. Convolution is similar to cross-correlation between
the two input functions—with a twist. A somewhat antique name for convolution is faltung, which means folding

in German. It is this folding concept
that makes convolution useful for trading.
In this chapter, we will spare you the details of the mathematics and will
jump from the theoretical concept to useful trading examples.

■Theoretical Foundation
Consider what happens at an idealized market bottom. The prices decrease
linearly until the bottom is reached and then increase linearly after the
bottom has occurred. If we fold these idealized prices about the market
bottom, the two price segments are perfectly correlated. That is, we have
cross-correlated two market segments that have been folded at the horizontal point of the market bottom. This perfect correlation occurs only at the
idealized market bottom that, in fact, establishes the need for prefiltering
before the correlation is calculated so that a relatively high correlation can
be achieved using real data.
Figure 13.1 shows two graphic examples of convolution in an initial uptrend. In the left-hand case, the folding has been done in the middle of a
Cycle Analytics for Traders: Advanced Technical Trading Concepts. John F. Ehlers.
© 2013 John F. Ehlers. Published 2013 by John Wiley & Sons, Inc.
--- page 171 ---

166
CYCLE ANALYTICS FOR TRADERS
continuing trend. The resultant is that the two price segments are not correlated after the folding operation. However, if the folding is done at exactly
the market peak, as shown in the right-hand case, the two price segments
are exactly correlated after the folding operation.
Since high correlation exists only at the market turning point, the convolution indicator is dependent on the lookback period used in the calculation.
Assuming the two price segments have an equal time duration, the peak correlation occurs at half the lookback period of the indicator. For example, if a
13-bar period is used, the market peak would appear with a 7-bar delay. The
same market peak would appear with a 19-bar delay if a 39-bar lookback
period were used in the convolution computation. The case of the market
peak’s not occurring at the folding point is illustrated in Figure 13.2, showing how the correlation decreases when the folding point does not occur at
the market peak.
Still another case is shown in Figure 13.3, where the market trend is
briefly interrupted and then resumes. As long as the lookback period is
equal to or less than twice the distance between the two vertical dotted
lines, a high-correlation event will occur at half the lookback period. However, when the lookback period becomes longer, the noncorrelated line segment is included in the convolution computation and the overall correlation
is reduced.
Trend
Convolution
No Correlation
Truning Point
Convolution
Correlation
FIGURE 13.1
High Correlations Occur Only at Major MarketTurning
T
Points
--- page 172 ---

167
CONVOLUTION
When the correlation is plotted as a conventional indicator, the highcorrelation point will show up at a spike that is delayed half the lookback
period from the current data bar. If the lookback period is short, the correlation spikes will be relatively current, but there will be a lot of them. If the
lookback period is long, convolution basically reports ancient history, and
the short-term interruptions will be eliminated. Consequently, the convolution display is dependent on the lookback period used in the computation.
Convolution
Poor Correlation
FIGURE 13.2
Good Correlation Occurs Only When the Folding Is Done at
the Market Reversal Point
FIGURE 13.3
Interruptions in MarketTrends
T
Have High Correlations for
Only Short Periods
Convolution
Short-Term Correlation
--- page 173 ---

168
CYCLE ANALYTICS FOR TRADERS

■Heat Map Display
The convolution indicator covers a range of lookback periods. The vertical scale of the indicator is the lookback period, and the indicator value is
converted to colors. An indicator is repeatedly calculated for each lookback
period for each new bar of data. The result is a heat map display that is in
time sync with the price data and the values of the indicator are shown for
the full range of useful lookback periods.
When the convolution computations are displayed as colors over the range
of lookback periods, the resulting chart shows the high correlation points as
“plumes” that point back precisely to the major market reversals. The interruptions in market trends show up as foreshorted and vestigial plumes.
The convolution for approximately the last year on the Dollar General
(symbol DG) is shown in Figure 13.4. By taking the direction of the trend
into account, market tops are displayed as red plumes (signaling a reversal to
the downside), and market bottoms are displayed as green plumes (signaling a
reversal to the upside). The foreshortened plumes in January 2011 signal that
the uptrend from the fall of 2010 is still in play. For the remainder of 2011,
the five red plumes and the six green plumes absolutely nail the major market
reversals. The reversal points are located at the bottom of the convolution
subgraph, and the long plumes identify each as a major turning point. Since a
finite amount of data is required to make the shortest calculation, convolution
is moved four bars to the left to better correlate the indicator with the actual
turning point. This technique is similar to that of a centered moving average.
FIGURE 13.4
Convolution Nailed Each Market Reversal over the Past Year
--- page 174 ---

169
CONVOLUTION

■Computing Convolution
For those interested in computing the convolution indicator on their
own, the process is relatively straightforward. A filter to minimize the effects of Spectral Dilation precedes the actual calculation, and the shortest and longest periods of this filter are profit as user inputs. The default
values are 40 bars and 80 bars. The shortest period can be reduced to reduce computational lag, but at the expense of additional display artifacts
near the bottom of the display. After declaring the variables and the arrays, undesired long-wave cyclic components are removed by a two-pole
high-pass filter tuned to the longest period. The high-pass filter is followed by the SuperSmoother of Equation 3-3, whose transfer response
is displayed in Figure 3.10. The 40-bar period for this filter was selected
to reduce the displays of all but the major turning points. Since the market data are fractal (the longer cycle periods have the larger swings), we
want to avoid spurious displays of relatively minor turning points. Thus,
the combination of the high-pass filter and the SuperSmoother form a
“roofing” filter that passes the desired range of frequency components
useful for convolution.
Textbook Pearson correlation is accomplished for each of the lookback
periods from 1 to 48, and a correlation value is assigned to each lookback
period. The variable X is the base data stream, and the variable
X
Y is the data
Y
stream folded back for each calculation loop. The values of X, Y, X *
X
X, X *
X
Y,
and Y *
Y
Y are summed over the lookback length before being applied to the
Y
correlation equation. The correlation resulting from the computations varies from −1 to +1. These correlation values are applied to an inverse Fisher
transform2 to sharpen the display and then rescaled to vary between 0 and
1 for plotting purposes.
There is a considerable amount of information to be displayed, and a
heat map is used to make sense of it all. The general scheme is that for
each horizontal axis time position the vertical displacement is equal to
the lag from 3 to 48. The correlation value for each lag is converted to a
color. If the slope of the prices over the lookback period is positive, then
the hue is red.  The saturation of the red color is determined by the value
of the correlation.  If the slope of the prices over the lookback period
is negative, then the hue is green.  The saturation of the green color is
determined by the value of the correlation.
The EasyLanguage code to compute the Convolution indicator is given
in Code Listing 13-1.
--- page 175 ---

170
CYCLE ANALYTICS FOR TRADERS
Code Listing 13-1. EasyLanguage Code to
Compute and Display Convolution
{
Convolution Indicator
(c) 2013  John F. Ehlers
}
Inputs:
ShortestPeriod(40),
LongestPeriod(80);
Vars:
alpha1(0),
HP(0),
a1(0),
b1(0),
c1(0),
c2(0),
c3(0),
Filt(0),
N(0),
II(0),
X(0),
Y(0),
Sx(0),
Sy(0),
Sxx(0),
Syy(0),
Sxy(0),
Color1(0),
Color2(0),
Color3(0);
Arrays:
Corr[48](0),
Slope[48](0),
Convolution[48](0);
//HighPass filter cyclic components whose periods are
shorter than 48 bars
alpha1 = (Cosine(1.414*360 / LongestPeriod) + Sine
(1.414*360 / LongestPeriod) - 1) / Cosine(1.414*360 /
LongestPeriod);
--- page 176 ---

171
CONVOLUTION
Code Listing 13-1. (Continued)
HP = (1 - alpha1 / 2)*(1 - alpha1 / 2)*(Close - 2*Close[1] +
Close[2]) + 2*(1 - alpha1)*HP[1] - (1 - alpha1)*
(1 - alpha1)*HP[2];
//Smooth with a Super Smoother Filter from equation 3-3
a1 = expvalue(-1.414*3.14159 / ShortestPeriod);
b1 = 2*a1*Cosine(1.414*180 / ShortestPeriod);
c2 = b1;
c3 = -a1*a1;
c1 = 1 - c2 - c3;
Filt = c1*(HP + HP[1]) / 2 + c2*Filt[1] + c3*Filt[2];
For N = 1 to 48 Begin
Sx = 0;
Sy = 0;
Sxx = 0;
Syy = 0;
Sxy = 0;
For II = 1 to N Begin
X = Filt[II - 1];
Y = Filt[N - II];
Sx = Sx + X;
Sy = Sy + Y;
Sxx = Sxx + X*X;
Sxy = Sxy + X*Y;
Syy = Syy + Y*Y;
End;
If (N*Sxx - Sx*Sx)*(N*Syy - Sy*Sy) > 0 Then Corr[N] =
(N*Sxy - Sx*Sy)/SquareRoot((N*Sxx - Sx*Sx)*(N*Syy -
Sy*Sy));
Slope[N] = 1;
If Filt[IntPortion(.5*N)] < Filt Then Slope[N] = -1;
Convolution[N] = (1 + (ExpValue(3*Corr[N]) - 1) /
(ExpValue(3*Corr[N]) + 1)) / 2;
End;
//Plot as a Heatmap
For N = 3 to 48 Begin
If Slope[N] > 0 Then Begin
Color1 = 255*Convolution[N];
Color2 = 0;
End;
(Continued)
--- page 177 ---

172
CYCLE ANALYTICS FOR TRADERS
Code Listing 13-1. (Continued)
If Slope[N] < 0 Then Begin
Color1 = 0;
Color2 = 255*Convolution[N];
End;
Color3 = 0;
If N = 2 Then Plot2[4](2, “S2”, RGB(Color1, Color2,
Color3),0,4);
If N = 3 Then Plot3[4](3, “S3”, RGB(Color1, Color2,
Color3),0,4);
If N = 4 Then Plot4[4](4, “S4”, RGB(Color1, Color2,
Color3),0,4);
If N = 5 Then Plot5[4](5, “S5”, RGB(Color1, Color2,
Color3),0,4);
If N = 6 Then Plot6[4](6, “S6”, RGB(Color1, Color2,
Color3),0,4);
If N = 7 Then Plot7[4](7, “S7”, RGB(Color1, Color2,
Color3),0,4);
If N = 8 Then Plot8[4](8, “S8”, RGB(Color1, Color2,
Color3),0,4);
If N = 9 Then Plot9[4](9, “S9”, RGB(Color1, Color2,
Color3),0,4);
If N = 10 Then Plot10[4](10, “S10”, RGB(Color1, Color2,
Color3),0,4);
If N = 11 Then Plot11[4](11, “S11”, RGB(Color1, Color2,
Color3),0,4);
If N = 12 Then Plot12[4](12, “S12”, RGB(Color1, Color2,
Color3),0,4);
If N = 13 Then Plot13[4](13, “S13”, RGB(Color1, Color2,
Color3),0,4);
If N = 14 Then Plot14[4](14, “S14”, RGB(Color1, Color2,
Color3),0,4);
If N = 15 Then Plot15[4](15, “S15”, RGB(Color1, Color2,
Color3),0,4);
If N = 16 Then Plot16[4](16, “S16”, RGB(Color1, Color2,
Color3),0,4);
If N = 17 Then Plot17[4](17, “S17”, RGB(Color1, Color2,
Color3),0,4);
If N = 18 Then Plot18[4](18, “S18”, RGB(Color1, Color2,
Color3),0,4);
If N = 19 Then Plot19[4](19, “S19”, RGB(Color1, Color2,
Color3),0,4);
If N = 20 Then Plot20[4](20, “S20”, RGB(Color1, Color2,
Color3),0,4);
--- page 178 ---

173
CONVOLUTION
Code Listing 13-1. (Continued)
If N = 21 Then Plot21[4](21, “S21”, RGB(Color1, Color2,
Color3),0,4);
If N = 22 Then Plot22[4](22, “S22”, RGB(Color1, Color2,
Color3),0,4);
If N = 23 Then Plot23[4](23, “S23”, RGB(Color1, Color2,
Color3),0,4);
If N = 24 Then Plot24[4](24, “S24”, RGB(Color1, Color2,
Color3),0,4);
If N = 25 Then Plot25[4](25, “S25”, RGB(Color1, Color2,
Color3),0,4);
If N = 26 Then Plot26[4](26, “S26”, RGB(Color1, Color2,
Color3),0,4);
If N = 27 Then Plot27[4](27, “S27”, RGB(Color1, Color2,
Color3),0,4);
If N = 28 Then Plot28[4](28, “S28”, RGB(Color1, Color2,
Color3),0,4);
If N = 29 Then Plot29[4](29, “S29”, RGB(Color1, Color2,
Color3),0,4);
If N = 30 Then Plot30[4](30, “S30”, RGB(Color1, Color2,
Color3),0,4);
If N = 31 Then Plot31[4](31, “S31”, RGB(Color1, Color2,
Color3),0,4);
If N = 32 Then Plot32[4](32, “S32”, RGB(Color1, Color2,
Color3),0,4);
If N = 33 Then Plot33[4](33, “S33”, RGB(Color1, Color2,
Color3),0,4);
If N = 34 Then Plot34[4](34, “S34”, RGB(Color1, Color2,
Color3),0,4);
If N = 35 Then Plot35[4](35, “S35”, RGB(Color1, Color2,
Color3),0,4);
If N = 36 Then Plot36[4](36, “S36”, RGB(Color1, Color2,
Color3),0,4);
If N = 37 Then Plot37[4](37, “S37”, RGB(Color1, Color2,
Color3),0,4);
If N = 38 Then Plot38[4](38, “S38”, RGB(Color1, Color2,
Color3),0,4);
If N = 39 Then Plot39[4](39, “S39”, RGB(Color1, Color2,
Color3),0,4);
If N = 40 Then Plot40[4](40, “S40”, RGB(Color1, Color2,
Color3),0,4);
If N = 41 Then Plot41[4](41, “S41”, RGB(Color1, Color2,
Color3),0,4);
If N = 42 Then Plot42[4](42, “S42”, RGB(Color1, Color2,
Color3),0,4);
(Continued)
