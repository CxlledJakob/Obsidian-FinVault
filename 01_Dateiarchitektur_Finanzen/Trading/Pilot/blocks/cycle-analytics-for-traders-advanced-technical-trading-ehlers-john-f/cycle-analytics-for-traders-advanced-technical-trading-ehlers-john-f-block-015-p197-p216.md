# Cycle Analytics for Traders (Advanced Technical Trading -- Ehlers, John F_ -- 10_1002_9781118728611, 2013 nov 18 -- John Wiley & Sons, Inc_ -- doi 10_1002_9781118728611 -- 1af2315757f5680b2f83029a006fd7ab -- Anna’s .pdf — Chapter 9: Fourier Transforms (pages 197–216)

--- page 197 ---

192
CYCLE ANALYTICS FOR TRADERS

■Homodyne
The third algorithm for computing the dominant cycle is the homodyne approach. Homodyne means the signal is multiplied by itself. More precisely,
we want to multiply the signal of the current bar with the complex value
of the signal one bar ago. The complex conjugate is, by definition, a complex number whose sign of the imaginary component has been reversed.
Expressing the signal in polar coordinates, the arithmetic is:
(
)(
)
(
)
ρ
ρ
ρ
ρ
ω
ω
ω
ω
e
e
s
e
j t
j t
j
t
t
j
n
n
n
n
−
−
−
−
=
=
1
1
2
2
The interesting result is that we get both the square of the signal amplitude and the angular frequency (2π / Period) from the product because the
difference in time between samples (tn −tn−1) is just one bar. In principle, this
means that we can get the instantaneous cycle period in just two successive
samples. The added benefit is that we also get the square of the signal amplitude. The calculations are carried out using the in-phase and quadrature
components rather than converting them to polar coordinates. Either way,
the results will be the same.
Since the differential angle is small in radian measure, the angle, the tangent of the angle and the arctangent of the angle are all approximately the
same. Therefore, the dominant cycle is computed by dividing 2π by the
ratio of the imaginary component to the real component. Ideally, the angle
cannot be negative because time cannot run backwards. Frankly, the purpose of the smoothing filter is to cover the erratic calculations caused by
noise.
The code to compute the dominant cycle using the homodyne method is
given in Code Listing 14-6.
Code Listing 14-5. (Continued)
//Resolve Instantaneous Period errors and smooth
If InstPeriod = 0 then InstPeriod = InstPeriod[1];
DomCycle = c1*(InstPeriod + InstPeriod[1]) / 2 +
c2*DomCycle[1] + c3*DomCycle[2];
Plot1(DomCycle);
--- page 198 ---

193
THE HILBERT TRANSFORMER
Code Listing 14-6. EasyLanguage Code to Compute the
Dominant Cycle Using the Homodyne Method
{
Measuring the Dominant Cycle using a HomoDyne
Discriminator
© 2013  John F. Ehlers
}
Inputs:
LPPeriod(20);
Vars:
alpha1(0),
HP(0),
a1(0),
b1(0),
c1(0),
c2(0),
c3(0),
Filt(0),
QFilt(0),
Real(0),
Quad(0),
Imag(0),
IPeak(0),
QPeak(0),
Re(0),
Im(0),
Period(0),
DomCycle(0);
//Highpass filter cyclic components whose periods are
shorter than 48 bars
alpha1 = (Cosine(.707*360 / 48) + Sine (.707*360 / 48) - 1) /
Cosine(.707*360 / 48);
HP = (1 - alpha1 / 2)*(1 - alpha1 / 2)*(Close - 2*Close[1] +
Close[2]) + 2*(1 - alpha1)*HP[1] - (1 - alpha1)*
(1 - alpha1)*HP[2];
//Smooth with a Super Smoother Filter from equation 3-3
a1 = expvalue(-1.414*3.14159 / LPPeriod);
b1 = 2*a1*Cosine(1.414*180 / LPPeriod);
c2 = b1;
(Continued)
--- page 199 ---

194
CYCLE ANALYTICS FOR TRADERS

■Key Points to Remember
1. The classic Hilbert transformer uses a truncated FIR filter.
2. The classic Hilbert transformer cannot be used for trading because the
FIR filter introduces a large amount of lag, and shortening the FIR filter
introduces large amplitude variations across the pass band.
3. A modified Hilbert transformer can be created using a one-bar difference to establish phase quadrature and AGC to provide amplitude compensation.
4. The Hilbert transformer indicator provides predictive turning points
for swing trading. These predictions can be wrong if a new trend is established rather than a new swing.
5. Using the Hilbert transformer to compute the dominant cycle is the
price data is not advised.
Code Listing 14-6. (Continued)
c3 = -a1*a1;
c1 = 1 - c2 - c3;
Filt = c1*(HP + HP[1]) / 2 + c2*Filt[1] + c3*Filt[2];
IPeak = .991*IPeak[1];
If Absvalue(Filt) > IPeak Then IPeak = AbsValue(Filt);
Real = Filt / IPeak;
Quad = (Real - Real[1]);
QPeak = .991*QPeak[1];
If Absvalue(Quad) > QPeak Then QPeak = AbsValue(Quad);
Imag = Quad /QPeak;
Re = Real*Real[1] + Imag*Imag[1];
Im = Real[1]*Imag - Real*Imag[1];
If Im <> 0 and Re <> 0 Then Period = 6.28318 / AbsValue
((Im / Re));
If Period < 10 Then Period = 10;
If Period > 48 Then Period = 48;
DomCycle = c1*(Period + Period[1]) / 2 + c2*DomCycle[1] +
c3*DomCycle[2];
Plot1(DomCycle);
--- page 200 ---

195
Indicator
Transforms
“Now I see,” said Tom blindly.
C H A P T E R 1 5
A
n indicator transform is a means to shape the indicator to aid interpretation and use of the indicator itself. Other than shaping the display,
these transforms have no impact on the indicator. For example, they induce
no lag. While relatively trivial to implement, these transforms have a huge
impact on the interpretation and use of the indicators. There are primarily three indicators of interest to traders: the Fisher transform, the inverse
Fisher transform, and the cube transform. Each has its preferred application, which we describe in this chapter.

■Fisher Transform
A common fallacy in the use of technical indicators is that their probability distribution follows a normal, or Gaussian, probability distribution. That just is
not so, as you can prove for yourself by analyzing a reasonable amount of data.
If the data do not have a normal probability distribution, then the calculation
of a standard deviation is based on a false premise. The purpose of the Fisher
transform is to take any indicator having a nominally zero mean and bounded
between the limits of −1 to +1 and convert the amplitude so that the transformed indicator has an approximate normal probability distribution.
Plotting an indicator scaled to a normal probability distribution has a
huge advantage on indicator interpretation. If the transformed indicator has
a value of −1, it has a value of negative one standard deviation and therefore
Cycle Analytics for Traders: Advanced Technical Trading Concepts. John F. Ehlers.
© 2013 John F. Ehlers. Published 2013 by John Wiley & Sons, Inc.
--- page 201 ---

196
CYCLE ANALYTICS FOR TRADERS
there is a 32 percent chance prices will go lower. If the transformed indicator has a value of −2, it has a value of negative two standard deviations, and
therefore there is only an 8 percent chance prices will go lower. This is a
high-probability buying opportunity. At a level of −3, the negative 3 standard deviations means there is only a 2 percent chance of the prices going
lower. The transformed values are symmetrical, so positive deviations are
high-probability indications to exit a long position or to sell short.
The equation for a Fisher transform is
Output
ln
Input
Input
0.5*
1
1
=
+
−
⎡
⎣⎢
⎤
⎦⎥
Since an input value of unity can cause the ratio to go to infinity, the input
must be limited to 0.999, which corresponds to an output on the order of
three standard deviations. Similarly, the argument of the natural logarithm
cannot be allowed to go to zero, and so the input must also be limited at
−0.999.
The transfer response of the Fisher transform is shown in Figure 15.1.
The straight line shows the range of inputs, and the curved line shows the
corresponding range of outputs. When the inputs are less than an absolute
value of 0.5, the outputs are almost the same as the inputs. However, there
is a greater and greater magnification of the outputs as the inputs approach
the absolute value of 1. It is this nonlinear magnification that produces the
“long tails” in the output probability distribution, thus creating the resulting
normal probability distribution.
3
2
1
0
–1
–1
–0.8
–0.6
–0.4
–0.2
0
0.2
0.4
0.6
0.8
–2
–3
FIGURE 15.1
Transfer
T
Response of the Fisher Transform Shows Greater
T
Magnification of the Outputs as the Inputs Approach an Absolute Value of 1
--- page 202 ---

197
INDICATOR TRANSFORMS
To implement the Fisher transform on the adaptive RSI, replace the plot
statements of Code Listing 11-1 with the following code fragment:
Code Listing 15-1. EasyLanguage Code Fragment to Add
the Fisher Transform to the Adaptive RSI Indicator
Vars:
TranslatedRSI(0),
AmplifiedRSI(0),
Fish(0);
TranslatedRSI = 2*(MyRSI - .5);
AmplifiedRSI = 1.5*TranslatedRSI;
If AmplifiedRSI > .999 Then AmplifiedRSI = .999;
If AmplifiedRSI < -.999 Then AmplifiedRSI = -.999;
Fish = .5*Log((1 + AmplifiedRSI) / (1 - AmplifiedRSI));
Plot1(Fish);
Plot2(2);
Plot6(-2);
The variable MyRSI ranges between zero and one, and therefore to ac
I
-
commodate the conditions for the Fisher transform, this variable must be
translated and dilated to range between −1 and +1. If the MyRSI variable
I
does not range fully between zero and one, you can shorten the RSI lookback period to be less than half the measured dominant cycle, or you can
simply multiply it by a magnification factor as I have done in the code fragment. The amplifying factor was selected to make the indicator rarely exceed the two sigma points in the output. The amplified RSI is then limited
to be within the range of −0.999 to +0.999 to avoid a computer crash,
and then is used to compute the Fisher transform. The plus and minus two
standard deviation levels are included in the indicator display. An example
of the adaptive RSI using the Fisher transform is shown in Figure 15.2. The
trend up is heralded by the Fisherized indicator’s falling below −2. Then, the
trend down is signaled by the Fisherized indicator rising above +2. These
major turning points are relatively rare events and are perhaps best used in
association with trend trading.
Since the Stochastic and commodity channel index (CCI) indicators
measure relative position in a channel, they tend to be near the upper or
lower limits during trends. That means that they do not have a zero mean in
the short run and therefore are not good candidates on which to apply the
--- page 203 ---

198
CYCLE ANALYTICS FOR TRADERS
Fisher transform. A band-pass filter would be a much better candidate, but
the major cyclic turning points are already easy to identify and don’t require
a more complex statistical approach.

■Inverse Fisher Transform
Whereas the Fisher transform expands the base indicator near the extremes,
the purpose of the inverse Fisher transform is to compress the indicator in
these regions. By compressing values near the extremes many extraneous
and irrelevant wiggles are removed from the indicator, making interpretation of the real meaning of the indicator be far simpler. In a sense, the inverse Fisher transform acts as a soft limiter.
The equation for the inverse Fisher transform is
Output
e
e
1
1
K Input
K Input
(2* *
)
(2* *
)
=
−
+
The input may have as large a value as desired. If the input values are very
large, then the exponential terms in both the numerator and denominator
are very large compared to one, and so the output is approximately 1. If the
input values are very large, but negative, then the exponential terms in both
the numerator and denominator are very small compare to one, with the
result that the output is approximately −1. The K in the expression is an op
K
-
tional amplifying term because conventional indicators already fall between
FIGURE 15.2
Adaptive RSI with FisherTransform Clearly Identifies Major
T
Turning
T
Points
--- page 204 ---

199
INDICATOR TRANSFORMS
the limits of −1 and +1, and so amplifying them is necessary to reap the
benefits of the soft limiting of the inverse Fisher transform.
The transfer response of the inverse Fisher transform is shown in Figure 15.3.
The input values are shown by the straight line, and the output values are
shown by the curved line. This graphical representation shows how larger and
larger absolute values of the input are compressed to essentially be unity.
To implement the inverse Fisher transform on an adaptive Stochastic
indicator, replace the plot statements of Code Listing 11-2 with the code
fragment given in Code Listing 15-2. I have chosen to amplify the adaptive
Stochastic by a factor of 3 when taking the inverse Fisher transform.
4
3
2
0
–1
–3
–3
–4
1
–2
–1
0
1
2
3
–2
FIGURE 15.3
Transfer
T
Response of the Inverse Fisher Transform Shows the
T
Compression of Larger Values of the Input
Code Listing 15-2. EasyLanguage Code Fragment
to Implement the Inverse Fisher Transform on
the Adaptive Stochastic Indicator
Vars:
IFish(0);
Value1 = 2*(AdaptiveStochastic - .5);
IFish = (ExpValue(2*3*Value1) - 1) / (ExpValue
(2*3*Value1) + 1);
Plot1(IFish);
Plot4(.9*IFish[1]);
--- page 205 ---

200
CYCLE ANALYTICS FOR TRADERS
I have also included a trigger line, which is just the inverse Fisher transform
delayed by one bar and attenuated to 90 percent. The crossings of the inverse
Fisher transform line and the trigger line provide clear and unequivocal indications for the buy and sell points, as demonstrated in the example of Figure 15.4.
The use of the inverse Fisher adaptive Stochastic indicator involves the crossings of the inverse Fisher line and the trigger line. When the inverse Fisher line
crosses over the trigger line, then buy. When the inverse Fisher line crosses
under the trigger line, then sell short, or if you choose, exit the long position.
The inverse Fisher transform should be one of the biggest weapons in
your arsenal of trading indicators and strategies. Its use as a soft limiter is
universal and can help remove many of the distracting and irrelevant squiggles in your indicators. The only constraint should be that the original input
has a nearly a zero mean. You may need to amplify the input to attain the
desired compression at the output. If you want a simple “digital” output, just
amplify the input by a large amount.

■Cube Transform
The purpose of the cube transform is to compress the signals near zero of
an indicator that swings between the limits of −1 and +1. This is handy for
an indicator such as the adaptive band-pass filter where you are concerned
only with the larger swings, and the squiggles in the middle are merely
distractions. The transform consists of merely cubing the indicator values.
FIGURE 15.4
The Inverse Fisher Transform of the
T
Adaptive Stochastic
Indicator Gives Clear and Unambiguous Indications of the Proper Buy and
Sell Points
--- page 206 ---

201
INDICATOR TRANSFORMS
Doing this, the values near +1 and −1 are nearly unchanged, but the smaller
absolute values are severely reduced in amplitude. Of course, this only works
if the effects of spectral dilation have been removed by a roofing filter or
some equivalent technique. The cubing of the display is only effective when
the original indicator has a nominally zero mean. The transfer response of the
cube transform is shown in Figure 15.5. In this figure, the input values are
shown by the straight line and the output values are shown by the curved line.
The effect of the cube transform is shown in Figure 15.6, where the
adaptive band-pass filter is shown in the first subgraph, and the adaptive
1
0.8
0.4
0
–0.4
–1
–0.8
–0.6
–0.4
–0.2
0
0.3
0.4
0.6
0.9
1
–0.8
–1
0.6
0.2
–0.7
–0.9
–0.5
–0.3
–0.1
0.1
0.2
0.5
0.7
0.8
–0.2
–0.6
FIGURE 15.5
The CubeTransform Compresses Smaller Values of the Input
T
FIGURE 15.6
The Cube Transform Clarifies Swinging Signals by
T
Compressing the Smaller Amplitude Swings
--- page 207 ---

202
CYCLE ANALYTICS FOR TRADERS
band-pass filter with the cube transform is shown in the second subgraph.
The purpose of the cube transform is to clarify the major swings by compressing the distractions of the smaller swing values.

■Key Points to Remember
1. The purpose of a transformer is shape the indicator to aid interpretation
and use of the indicator itself.
2. Transformers do not induce lag.
3. A Fisher transform of an indicator swinging between −1 and +1 with a
nominal zero mean plots that indicator in terms of standard deviations
with a nearly normal probability distribution.
4. An inverse Fisher transform acts as a soft limiter to remove extraneous
wiggles in indicators have a nominal zero mean.
5. A cube transform compresses the smaller values of an indicator swinging between −1 and +1.
--- page 208 ---

C H A P T E R 1 6
203
SwamiCharts
“Now that’s a hot display,” said Tom coolly.
T
echnical indicators for trading are long on precision but short on
accuracy. For example, you know exactly when a relative strength index (RSI) crosses the 80 percent threshold. In my opinion, this precision
property of indicators gives traders a false sense of security and obscures
the fact that indicators are basically displays of a statistical process. Further,
most traders don’t have a clue regarding the proper setting of the indicator
lookback period. The end result is that the precise indicator can show you
pretty much anything you want, depending on how you set the parameters.
Part of the solution, as discussed in Chapter 11, is to make the indicator
adaptive to the measured cycle period.
In this chapter, I describe another completely different perspective,
which is to accept that indicators are inherently inaccurate and a better
approach is to look at that indicator over a range of lookback periods and
view the short-term movement in the context of the longer-term indictor
results. In a sense, the indicator is used as fuzzy logic. This is the purpose of
SwamiCharts.
Almost any oscillator-type indicator can be plotted as a SwamiChart.
If you do this, you will quickly isolate those indicators that have the best
performance. You will also find, as I did, that there are some indicators
that indicate nothing at all. As a quick visual example, Figure 16.1 shows
a conventional RSI and a conventional Stochastic on the same chart. They
seem to be giving different information. Part of the answer is that neither
has been compensated for Spectral Dilation. The rest of the answer is that
when viewed in context, these two indicators show just about the same
thing.
Cycle Analytics for Traders: Advanced Technical Trading Concepts. John F. Ehlers.
© 2013 John F. Ehlers. Published 2013 by John Wiley & Sons, Inc.
--- page 209 ---

204
CYCLE ANALYTICS FOR TRADERS

■SwamiCharts Overview
SwamiCharts retain the core functionality of the technical indicators with
which you’re already familiar, while packing much more information into
an easy-to-interpret heat map chart. With SwamiCharts, you now visualize
each indicator over a range of lookback periods to reveal a better view of the
indicator’s truer meaning in context.
SwamiCharts provide a better solution because you can now visualize
context over a wide range of lookback periods. Trends and cycles emerge
more succinctly, while continuation patterns and reversals become easier to
identify. SwamiCharts solves the data lookback problem by enabling you to
view market conditions at a glance, a feature that will dramatically facilitate
your trading.
SwamiCharts condenses much more information about each indicator’s
true meaning into an easy-to-interpret heat map chart. SwamiCharts indicators are created by computing the technical indicator multiple times over
a range of lookback periods. The vertical scale of the SwamiChart indicator is that range of those lookback periods. For each data bar and for each
lookback period the value of the indicator is computed in the conventional
way. After the indicator is computed, a color value is assigned to the matrix
location defined by the bar location in the horizontal plane and the lookback period in the vertical plane. The complete matrix looks like a heat map
when drawn below the price bars in a subgraph. The resulting basic display
FIGURE 16.1
RSI and Stochastic Indicators Seem to Impart Different
Information
--- page 210 ---

205
SWAMICHARTS
is easy to interpret. Green means increasing values, red mean decreasing
values, and yellow means intermediate values. That is, the heat map is a socalled “stoplight” chart.

■SwamiCharts RSI
The RSI indicator was described in Chapter 11, where we made the indicator adaptive to the measured dominant cycle. In this case, we compute
multiple RSIs over the range of lookback periods of interest and plot all of
them as a heat map. The SwamiCharts RSI is described with reference to the
EasyLanguage code in Code Listing 16-1.
Since the MyRSI is computed for all values over the range of lookback
I
periods, it must be an array in EasyLanguage rather than a variable. The RSI
is computed relative to the output of the roofing filter rather than price
closes to eliminate the effects of Spectral Dilation. After the computation of
the ratio, the indicator is smoothed in a SuperSmoother filter, so we must
create the three most recent instances ourselves in the code. This is because
EasyLanguage retains historical values for variables but not for arrays. In
fact, ratio must be an array also for the same reasons. The coefficients for the
10-bar SuperSmoother filter are computed and are the same for all lookback
periods, and so can be outside the lookback loop to make the calculations a
little more efficient.
Code Listing 16-1. EasyLanguage Code to
Compute the SwamiCharts RSI
{
SwamiCharts RSI
© 2013  John F. Ehlers
}
Vars:
alpha1(0),
HP(0),
a1(0),
b1(0),
c1(0),
c2(0),
c3(0),
(Continued)
--- page 211 ---

206
CYCLE ANALYTICS FOR TRADERS
Code Listing 16-1. (Continued)
Filt(0),
Lookback(0),
ClosesUp(0),
ClosesDn(0),
count(0),
Denom(0),
Color1(0),
Color2(0),
Color3(0);
Arrays:
Ratio[48, 2](0),
MyRSI[48, 3](0);
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
For Lookback = 5 to 48 Begin
//range includes half the shortest period of interest
Ratio[Lookback, 2] = Ratio[Lookback, 1];
MyRSI[Lookback, 3] = MyRSI[Lookback, 2];
MyRSI[Lookback, 2] = MyRSI[Lookback, 1];
ClosesUp = 0;
ClosesDn = 0;
For count = 0 to Lookback - 1 Begin
If Filt[count] > Filt[count + 1] Then ClosesUp =
ClosesUp + (Filt[count] - Filt[count + 1]);
If Filt[count] < Filt[count + 1] Then ClosesDn =
ClosesDn + (Filt[count + 1] - Filt[count]);
End;
Denom = ClosesUp + ClosesDn;
--- page 212 ---

207
SWAMICHARTS
Code Listing 16-1. (Continued)
If Denom <> 0 Then Ratio[Lookback, 1] = ClosesUp / Denom;
//Smooth MyRSI with a 10 bar Super Smoother
MyRSI[Lookback, 1] = c1*(Ratio[Lookback, 1] +
Ratio[Lookback, 2]) / 2 + c2*MyRSI[Lookback, 2] +
c3*MyRSI[Lookback, 3];
//Ensure MyRSI does not fall outside color limits
If MyRSI[Lookback, 1] < 0 Then MyRSI[Lookback, 1] = 0;
If MyRSI[Lookback, 1] > 1 Then MyRSI[Lookback, 1] = 1;
End;
//Plot as a Heatmap
//Plotting data must range between 0 and 1
For Lookback = 5 to 48 Begin
// StopLight Colors
If MyRSI[Lookback, 1] >= .5 Then Begin
Color1 = 255*(2 - 2*MyRSI[Lookback, 1]);
Color2 = 255;
Color3 = 0;
End
Else If MyRSI[Lookback, 1] < .5 Then Begin
Color1 = 255;
Color2 = 255*2*MyRSI[Lookback, 1];
Color3 = 0;
End;
If Lookback = 5 Then Plot5(5, “S10”, RGB(Color1, Color2,
Color3),0,4);
If Lookback = 6 Then Plot6(6, “S10”, RGB(Color1, Color2,
Color3),0,4);
If Lookback = 7 Then Plot7(7, “S10”, RGB(Color1, Color2,
Color3),0,4);
If Lookback = 8 Then Plot8(8, “S10”, RGB(Color1, Color2,
Color3),0,4);
If Lookback = 9 Then Plot9(9, “S10”, RGB(Color1, Color2,
Color3),0,4);
If Lookback = 10 Then Plot10(10, “S10”, RGB(Color1,
Color2, Color3),0,4);
If Lookback = 11 Then Plot11(11, “S11”, RGB(Color1,
Color2, Color3),0,4);
If Lookback = 12 Then Plot12(12, “S12”, RGB(Color1,
Color2, Color3),0,4);
If Lookback = 13 Then Plot13(13, “S13”, RGB(Color1,
Color2, Color3),0,4);
(Continued)
--- page 213 ---

208
CYCLE ANALYTICS FOR TRADERS
Code Listing 16-1. (Continued)
If Lookback = 14 Then Plot14(14, “S14”, RGB(Color1,
Color2, Color3),0,4);
If Lookback = 15 Then Plot15(15, “S15”, RGB(Color1,
Color2, Color3),0,4);
If Lookback = 16 Then Plot16(16, “S16”, RGB(Color1,
Color2, Color3),0,4);
If Lookback = 17 Then Plot17(17, “S17”, RGB(Color1,
Color2, Color3),0,4);
If Lookback = 18 Then Plot18(18, “S18”, RGB(Color1,
Color2, Color3),0,4);
If Lookback = 19 Then Plot19(19, “S19”, RGB(Color1,
Color2, Color3),0,4);
If Lookback = 20 Then Plot20(20, “S20”, RGB(Color1,
Color2, Color3),0,4);
If Lookback = 21 Then Plot21(21, “S21”, RGB(Color1,
Color2, Color3),0,4);
If Lookback = 22 Then Plot22(22, “S22”, RGB(Color1,
Color2, Color3),0,4);
If Lookback = 23 Then Plot23(23, “S23”, RGB(Color1,
Color2, Color3),0,4);
If Lookback = 24 Then Plot24(24, “S24”, RGB(Color1,
Color2, Color3),0,4);
If Lookback = 25 Then Plot25(25, “S25”, RGB(Color1,
Color2, Color3),0,4);
If Lookback = 26 Then Plot26(26, “S26”, RGB(Color1,
Color2, Color3),0,4);
If Lookback = 27 Then Plot27(27, “S27”, RGB(Color1,
Color2, Color3),0,4);
If Lookback = 28 Then Plot28(28, “S28”, RGB(Color1,
Color2, Color3),0,4);
If Lookback = 29 Then Plot29(29, “S29”, RGB(Color1,
Color2, Color3),0,4);
If Lookback = 30 Then Plot30(30, “S30”, RGB(Color1,
Color2, Color3),0,4);
If Lookback = 31 Then Plot31(31, “S31”, RGB(Color1,
Color2, Color3),0,4);
If Lookback = 32 Then Plot32(32, “S32”, RGB(Color1,
Color2, Color3),0,4);
If Lookback = 33 Then Plot33(33, “S33”, RGB(Color1,
Color2, Color3),0,4);
If Lookback = 34 Then Plot34(34, “S34”, RGB(Color1,
Color2, Color3),0,4);
If Lookback = 35 Then Plot35(35, “S35”, RGB(Color1,
Color2, Color3),0,4);
--- page 214 ---

209
SWAMICHARTS
Code Listing 16-1. (Continued)
If Lookback = 36 Then Plot36(36, “S36”, RGB(Color1,
Color2, Color3),0,4);
If Lookback = 37 Then Plot37(37, “S37”, RGB(Color1,
Color2, Color3),0,4);
If Lookback = 38 Then Plot38(38, “S38”, RGB(Color1,
Color2, Color3),0,4);
If Lookback = 39 Then Plot39(39, “S39”, RGB(Color1,
Color2, Color3),0,4);
If Lookback = 40 Then Plot40(40, “S40”, RGB(Color1,
Color2, Color3),0,4);
If Lookback = 41 Then Plot41(41, “S41”, RGB(Color1,
Color2, Color3),0,4);
If Lookback = 42 Then Plot42(42, “S42”, RGB(Color1,
Color2, Color3),0,4);
If Lookback = 43 Then Plot43(43, “S43”, RGB(Color1,
Color2, Color3),0,4);
If Lookback = 44 Then Plot44(44, “S44”, RGB(Color1,
Color2, Color3),0,4);
If Lookback = 45 Then Plot45(45, “S45”, RGB(Color1,
Color2, Color3),0,4);
If Lookback = 46 Then Plot46(46, “S46”, RGB(Color1,
Color2, Color3),0,4);
If Lookback = 47 Then Plot47(47, “S47”, RGB(Color1,
Color2, Color3),0,4);
If Lookback = 48 Then Plot48(48, “S48”, RGB(Color1,
Color2, Color3),0,4);
End;
Now, let’s see how the SwamiCharts RSI indicators look in Figure 16.2.
Wow! Now you can see the entire market activity at a glance. The shortterm downturns are shown in the context of caution to upside trends. When
the market turns down the short-term red areas expand into the longerterm down market. Then, at the right-hand edge of the chart, you can see
the short-term rising area expanding into the longer-term cautionary areas.
The RSI naturally equivocates at the longer lookback periods because the
value of the closes up start to approach the value of closes down over the
longer average.
--- page 215 ---

210
CYCLE ANALYTICS FOR TRADERS

■SwamiCharts Stochastic
The Stochastic indicator was also described in Chapter 11, where we made
the indicator adaptive to the measured dominant cycle. In this case, we compute multiple Stochastics over the range of lookback periods of interest and
plot all of them as a heat map. The SwamiCharts Stochastic is described with
reference to the EasyLanguage code in Code Listing 16-2.
Code Listing 16-2. EasyLanguage Code to Compute
the SwamiCharts Stochastic
{
SwamiCharts Stochastic
© 2013  John F. Ehlers
}
Vars:
alpha1(0),
HP(0),
a1(0),
b1(0),
c1(0),
c2(0),
c3(0),
FIGURE 16.2
SwamiCharts RSI Contains Much More Information than the
Standard RSI
--- page 216 ---

211
SWAMICHARTS
Code Listing 16-2. (Continued)
Filt(0),
Lookback(0),
count(0),
HighestC(0),
LowestC(0),
Color1(0),
Color2(0),
Color3(0);
Arrays:
Ratio[48, 2](0),
Stoc[48, 3](0);
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
//Compute Stochastic for each lookback period
For Lookback = 5 to 48 Begin
Ratio[Lookback, 2] = Ratio[Lookback, 1];
Stoc[Lookback, 3] = Stoc[Lookback, 2];
Stoc[Lookback, 2] = Stoc[Lookback, 1];
HighestC = Filt;
LowestC = Filt;
For count = 0 to Lookback -1  Begin
If Filt[count] > HighestC then HighestC = Filt[count];
If Filt[count] < LowestC then LowestC = Filt[count];
End;
Ratio[Lookback, 1] = (Filt - LowestC) / (HighestC -
LowestC);
(Continued)
