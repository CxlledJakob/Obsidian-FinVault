# Cycle Analytics for Traders (Advanced Technical Trading -- Ehlers, John F_ -- 10_1002_9781118728611, 2013 nov 18 -- John Wiley & Sons, Inc_ -- doi 10_1002_9781118728611 -- 1af2315757f5680b2f83029a006fd7ab -- Anna’s .pdf — Chapter 8: Chapter 8 (pages 116–120)

--- page 116 ---

110
CYCLE ANALYTICS FOR TRADERS
Figure 8.5 is a time-frequency representation (TFR) that is easily usable
by traders by interpreting colors as the strength of the spectral components.
Academia1 uses contour plots and waterfall diagrams to display the results
of their calculations. A wide range of techniques is employed to measure the
spectra of market data, including wavelets. Many of these techniques require
analytic data that are not easily available to traders. Most important, none of
these techniques have compensation for Spectral Dilation.

■Autocorrelation Reversals
One of the distinctive characteristics of Figures 8.3 and 8.4 is that the autocorrelation shifts from green to red or from red to green at all values of lag at
the cyclic reversals of the price. Therefore, all we need do to determine these
reversals is to sum the bar-to-bar differences of the autocorrelation function
across all values of lag. When the sum is large a turning point has been identified. The EasyLanguage code to compute these turning points is shown in
Code Listing 8-4. The indicated reversals are very sensitive to the smoothing
of the price data. Therefore, the LPLength is made available as an indicator
input to decrease or increase the number of indicated reversals as desired.
The AvgLength parameter is also made available as an indicator because
this averaging also impacts the number of indicated reversals. Care should
be taken when increasing the value of this input because the lag of the indicator increases in direct proportion to the increase of the value of the
AvgLength. Typical delay of the indicator will be about three bars when the
AvgLength parameter is set to a value of 3.
The HPLength parameter is also made available as an input for complete
flexibility of the indicator. However, changing its value has a relatively minor
impact on the indicated reversals.
Code Listing 8-4. EasyLanguage Code to
Compute Autocorrelation Reversals
{
Autocorrelation Reversals
© 2013   John F. Ehlers
}
Inputs:
HPLength(48),
--- page 117 ---

111
AUTOCORRELATION
Code Listing 8-4. (Continued)
LPLength(10),
AvgLength(3);
Vars:
alpha1(0),
HP(0),
a1(0),
b1(0),
c1(0),
c2(0),
c3(0),
Filt(0),
M(0),
N(0),
X(0),
Y(0),
Lag(0),
count(0),
Sx(0),
Sy(0),
Sxx(0),
Syy(0),
Sxy(0),
SumDeltas(0),
Reversal(0);
Arrays:
Corr[48, 2](0);
//Highpass filter cyclic components whose periods are
shorter than 48 bars
alpha1 = (Cosine(.707*360 / 48) + Sine (.707*360 / 48) - 1) /
Cosine(.707*360 / 48);
HP = (1 - alpha1 / 2)*(1 - alpha1 / 2)*(Close - 2*Close[1] +
Close[2]) + 2*(1 - alpha1)*HP[1] - (1 - alpha1)*
(1 - alpha1)*HP[2];
//Smooth with a Super Smoother Filter from equation 3-3
a1 = expvalue(-1.414*3.14159 / LPLength);
b1 = 2*a1*Cosine(1.414*180 / LPLength);
c2 = b1;
c3 = -a1*a1;
(Continued)
--- page 118 ---

112
CYCLE ANALYTICS FOR TRADERS
Code Listing 8-4. (Continued)
c1 = 1 - c2 - c3;
Filt = c1*(HP + HP[1]) / 2 + c2*Filt[1] + c3*Filt[2];
//Pearson correlation for each value of lag
For Lag = 3 to 48 Begin
Corr[Lag, 2] = Corr[Lag, 1];
//Set the averaging length as M
M = AvgLength;
If AvgLength = 0 Then M = Lag;
//Initialize correlation sums
Sx = 0;
Sy = 0;
Sxx = 0;
Syy = 0;
Sxy = 0;
//Advance samples of both data streams and sum Pearson
components
For count = 0 to M - 1 Begin
X = Filt[count];
Y = Filt[Lag + count];
Sx = Sx + X;
Sy = Sy + Y;
Sxx = Sxx + X*X;
Sxy = Sxy + X*Y;
Syy = Syy + Y*Y;
End;
//Compute correlation for each value of lag
If (M*Sxx - Sx*Sx)*(M*Syy - Sy*Sy) > 0 Then Corr[Lag, 1] =
(M*Sxy - Sx*Sy)/SquareRoot((M*Sxx - Sx*Sx)*(M*Syy -
Sy*Sy));
//Scale each correlation to range between 0 and 1
Corr[Lag, 1] = .5*(Corr[Lag, 1] + 1);
End;
SumDeltas = 0;
For Lag = 3 to 48 Begin
If (Corr[Lag, 1] > .5 and Corr[Lag, 2] < .5) Or
(Corr[Lag, 1] < .5 and Corr[Lag, 2] > .5) Then SumDeltas =
SumDeltas + 1;
End;
--- page 119 ---

113
AUTOCORRELATION
The autocorrelation reversals indicator is shown in Figure 8.6 using two
different values of the LPLength input. The reversals in the first subgraph
are computed using an LPLength of 20, and would be suitable for trading
systems holding positions in the range from 10 bars to 20 bars. The reversals
in the bottom subgraph are computed using an LPLength of 10, and would
be more suitable for more active trading systems holding positions from a
few days to a week.

■Key Points to Remember
1. The autocorrelation periodogram has the least latency of all market data
spectral estimates.
2. The autocorrelation periodogram automatically estimates the total cyclic power in the data as a function of time.
Code Listing 8-4. (Continued)
Reversal = 0;
If SumDeltas > 24 Then Reversal = 1;
Plot1(Reversal);
FIGURE 8.6
The Number of Indicated Reversals Is Decreased by Increasing
the Value of the LPLength Parameter
--- page 120 ---

114
CYCLE ANALYTICS FOR TRADERS
3. The autocorrelation periodogram provides an accurate estimate of
the market spectrum without the need for compensation for Spectral
Dilation.
4. The autocorrelation periodogram resolution is independent of any windowing function of the price data.
5. Price reversals are indicated by a dramatic switch in correlations at all
values of lag. These reversals can be used as a reliable indicator.
Note
1. Boualem Boushash, Time-Frequency Signal Analysis (Kidlington, Oxford,
UK: Elsevier Ltd., 2003).
