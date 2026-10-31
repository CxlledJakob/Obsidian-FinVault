# Quantitative Risk Management_ Concepts, Techniques, and -- Alexander J_ McNeil, Rüdiger Frey, Paul Embrechts -- Princeton series in finance, -- isbn13 9780691122557 -- 478a0059673fecd0c76229cd3d8884e7 -- Anna’s Arc.pdf — pages 153–172

--- page 153 ---

4.2. Fundamentals of Time Series Analysis
137
makes use of ﬁtted ARMA (or ARIMA) models and is sometimes called the Box–
Jenkins approach (Box and Jenkins 1970). The second strategy is a model-free
approach to forecasting known as exponential smoothing, which is related to the
exponentially weighted moving-average technique for predicting volatility.
Prediction using ARMA models.
Consider the invertible ARMA model and its
representation in (4.13). Let Ft denote the history of the process up to and including time t as before and assume that the innovations (εt)t∈Z have the martingaledifference property with respect to (Ft)t∈Z.
For the prediction problem it will be convenient to denote our sample of n data
by Xt−n+1, . . . , Xt. We assume these are realizations of rvs following a particular
ARMA model. Our aim is to predict Xt+1 or more generally Xt+h, and we denote
our prediction by PtXt+h. The method we describe assumes that we have access
to the inﬁnite history of the process up to time t and derives a formula that is then
approximated for our ﬁnite sample.
As a predictor of Xt+h we use the conditional expectation E(Xt+h | Ft). Among
all predictions PtXt+h based on the inﬁnite history of the process up to time t, this
predictor minimizes the mean squared prediction error E((Xt+h −PtXt+h)2).
The basic idea is that, for h ⩾1, the prediction E(Xt+h | Ft) is recursively
evaluated in terms of E(Xt+h−1 | Ft). We use the fact that E(εt+h | Ft) = 0 (the
martingale-difference property of innovations) and that the rvs (Xs)s⩽t and (εs)s⩽t
are “known” at time t. The assumption of invertibility (4.12) ensures that the innovation εt can be written as a function of the inﬁnite history of the process (Xs)s⩽t.
To illustrate the approach it will sufﬁce to consider an ARMA(1, 1) model, the
generalization to ARMA(p, q) models following easily.
Example 4.15 (prediction for the ARMA(1, 1) model). Suppose an ARMA(1, 1)
model of the form (4.13) has been ﬁtted to the data and its parameters µ, φ and θ
have been determined. Our one-step prediction for Xt+1 is
E(Xt+1 | Ft) = µt+1 = µ + φ(Xt −µ) + θεt,
since E(εt+1 | Ft) = 0. For a two-step prediction we get
E(Xt+2 | Ft) = E(µt+2 | Ft) = µ + φ(E(Xt+1 | Ft) −µ)
= µ + φ2(Xt −µ) + φθεt,
and in general we have
E(Xt+h | Ft) = µ + φh(Xt −µ) + φh−1θεt.
Without knowing all historical values of (Xs)s⩽t this predictor cannot be evaluated exactly, but it can be accurately approximated if n is reasonably large. The
easiest way of doing this is to substitute the model residual ˆεt calculated from (4.15)
for εt. Note that limh→∞E(Xt+h | Ft) = µ, almost surely, so that the prediction
converges to the estimate of the unconditional mean of the process for longer time
horizons.
--- page 154 ---

138
4. Financial Time Series
Exponential smoothing.
This is a popular technique which is used for both prediction of time series and trend estimation. Here we do not necessarily assume that
the data come from a stationary model, although we do assume that there is no
deterministic seasonal component in the model. In general the method is less well
suited to return series with frequently changing signs and is better suited to undifferenced price or value series. It forms the basis of a very common method of volatility
prediction (see Section 4.4.1).
Suppose our data represent realizations of rvs Yt−n+1, . . . , Yt, considered without
referencetoanyconcreteparametricmodel.AsaforecastforYt+1 weuseaprediction
of the form
PtYt+1 =
n−1

i=0
α(1 −α)iYt−i,
where 0 < α < 1.
Thus we weight the data from most recent to most distant with a sequence of exponentially decreasing weights that sum to almost one. It is easily calculated that
PtYt+1 =
n−1

i=0
α(1 −α)iYt−i = αYt + (1 −α)
n−2

j=0
α(1 −α)jYt−1−j
= αYt + (1 −α)Pt−1Yt,
(4.16)
so that the prediction at time t is obtained from the prediction at time t −1 by
a simple recursive scheme. The choice of α is subjective; the larger the value the
more weight is put on the most recent observation. Empirical validation studies with
different datasets can be used to determine a value of α that gives good results.
Note that, although the method is commonly seen as a model-free forecasting
technique, it can be shown to be the natural prediction method based on conditional
expectation for a non-stationary ARIMA(0, 1, 1) model.
Notes and Comments
There are many texts covering the subject of classical time series analysis including
Box and Jenkins (1970), Priestley (1981),Abraham and Ledolter (1983), Brockwell
and Davis (1991, 2002), Hamilton (1994) and Chatﬁeld (1996). Our account of basic
concepts,ARMA models and analysis in the time domain closely follows Brockwell
and Davis (1991), which should be consulted for the rigorous background to ideas we
can only summarize. We have not discussed analysis of time series in the frequency
domain, which is less common for ﬁnancial time series; for this subject see, again,
Brockwell and Davis (1991) or Priestley (1981).
For more on tests of the strict white noise hypothesis (that is tests of randomness),
see Brockwell and Davis (2002). Original references for the Box–Pierce and Ljung–
Box tests are Box and Pierce (1970) and Ljung and Box (1978).
There is a vast literature on forecasting and prediction in linear models. A
good non-mathematical introduction is found in Chatﬁeld (1996). The approach
we describe based on the inﬁnite history of the time series is discussed in greater
detail in Hamilton (1994). Brockwell and Davis (2002) concentrate on exact linear
--- page 155 ---

4.3. GARCH Models for Changing Volatility
139
prediction methods for ﬁnite samples. A general review of exponential smoothing
is found in Gardner (1985).
4.3
GARCH Models for Changing Volatility
The most important models for daily risk-factor return series are addressed in this
section.We give deﬁnitions ofARCH (autoregressive conditionally heteroscedastic)
and GARCH (generalized ARCH) models and discuss some of their mathematical
properties before going on to talk about their use in practice.
4.3.1
ARCH Processes
Deﬁnition 4.16. Let (Zt)t∈Z be SWN(0, 1). The process (Xt)t∈Z is an ARCH(p)
process if it is strictly stationary and if it satisﬁes, for all t ∈Z and some strictly
positive-valued process (σt)t∈Z, the equations
Xt = σtZt,
(4.17)
σ 2
t = α0 +
p

i=1
αiX2
t−i,
(4.18)
where α0 > 0 and αi ⩾0, i = 1, . . . , p.
Let Ft = σ({Xs : s ⩽t}) again denote the sigma algebra representing the history
of the process up to time t so that (Ft)t∈Z is the natural ﬁltration. Clearly, the
construction (4.18) ensures that σt is measurable with respect to Ft−1. This allows
us to calculate that, provided E(|Xt|) < ∞,
E(Xt | Ft−1) = E(σtZt | Ft−1) = σtE(Zt | Ft−1) = σtE(Zt) = 0,
(4.19)
so that the ARCH process has the martingale-difference property with respect to
(Ft)t∈Z.Iftheprocessiscovariancestationary,itissimplyawhitenoise,asdiscussed
in Section 4.2.1.
Remark 4.17. Note that the independence of Zt and Ft−1 that we have assumed
above follows from the fact that an ARCH process must be causal, i.e. the equations (4.17) and (4.18) must have a solution of the form Xt = f (Zt, Zt−1, . . . )
for some f so that Zt is independent of previous values of the process. This contrasts with ARMA models where the equations can have non-causal solutions (see
Brockwell and Davis 1991, Example 3.1.2).
If we simply assume that the process is a covariance-stationary white noise (for
which we will give a condition in Proposition 4.18), then E(X2
t ) < ∞and
var(Xt | Ft−1) = E(σ 2
t Z2
t | Ft−1) = σ 2
t var(Zt) = σ 2
t .
Thus the model has the interesting property that its conditional standard deviation
σt, or volatility, is a continually changing function of the previous squared values of
the process. If one or more of |Xt−1|, . . . , |Xt−p| are particularly large, then Xt is
effectively drawn from a distribution with large variance, and may itself be large; in
--- page 156 ---

140
4. Financial Time Series
0
200
400
600
800 1000
−5
0
10
0
200
400
600
800 1000
4
Lag
0
10
15
20
25
30
Lag
ACF
0
10
15
20
25
30
0
0.2
0.4
0.6
0.8
1.0
(a)
(b)
(c)
(d)
5
2
1
3
5
6
5
5
ACF
0
0.2
0.4
0.6
0.8
1.0
Figure 4.6.
A simulated ARCH(1) process with Gaussian innovations and parameters
α0 = α1 = 0.5: (a) the realization of the process; (b) the realization of the volatility; and
correlograms of (c) the raw and (d) the squared values. The process is covariance stationary
with unit variance and a ﬁnite fourth moment (since α1 < 1/
√
3) and the squared values
follow an AR(1) process. The true form of the ACF of the squared values is represented by
the dashed line in the correlogram.
this way the model generates volatility clusters. The nameARCH refers to this structure: the model is autoregressive, since Xt clearly depends on previous Xt−i, and
conditionally heteroscedastic, since the conditional variance changes continually.
The distribution of the innovations (Zt)t∈Z can in principle be any zero-mean,
unit-variance distribution. For statistical ﬁtting purposes we may or may not choose
to actually specify the distribution, depending on whether we implement a maximum likelihood (ML), quasi-maximum likelihood (QML) or non-parametric ﬁtting method (see Section 4.3.4). For ML the most common choices are standard normal innovations or scaled t innovations. By the latter we mean that
Zt ∼t1(ν, 0, (ν −2)/ν) in the notation of Example 3.7, so that the variance of
--- page 157 ---

4.3. GARCH Models for Changing Volatility
141
the distribution is one. We keep these choices in mind when discussing further
theoretical properties of ARCH and GARCH models.
The ARCH(1) model.
In the rest of this section we analyse some of the properties
of the ARCH(1) model. These properties extend to the whole class of ARCH and
GARCH models, but are most easily introduced in the simplest case. A simulated
realization of an ARCH(1) process with Gaussian innovations and the corresponding
realization of the volatility process are shown in Figure 4.6.
Using X2
t = σ 2
t Z2
t and (4.18) in the case p = 1, we deduce that the squared
ARCH(1) process satisﬁes
X2
t = α0Z2
t + α1Z2
t X2
t−1.
(4.20)
A detailed mathematical analysis of the ARCH(1) model involves the study of
equation (4.20), which is a stochastic recurrence equation (SRE). Much as for the
AR(1) model in Example 4.11, we would like to know when this equation has
stationary solutions expressed in terms of the inﬁnite history of the innovations,
i.e. solutions of the form X2
t = f (Zt, Zt−1, . . . ).
For ARCH models we have to distinguish carefully between solutions that are
covariance stationary and solutions that are only strictly stationary. It is possible to
have ARCH(1) models with inﬁnite variance, which obviously cannot be covariance
stationary.
Stochastic recurrence relations.
The detailed theory required to analyse stochastic
recurrence relations of the form (4.20) is outside the scope of this book, and we give
only brief notes to indicate the ideas involved. Our treatment is based on Brandt
(1986) and Mikosch (2003); see Notes and Comments at the end of this section for
further references.
Equation (4.20) is a particular example of a class of recurrence equations of the
form
Yt = AtYt−1 + Bt,
(4.21)
where (At)t∈Z and (Bt)t∈Z are sequences of iid rvs. Sufﬁcient conditions for a
solution are that
E(max{0, ln |Bt|}) < ∞
and
E(ln |At|) < 0,
(4.22)
where ln+ x = max(0, ln x). The unique solution is given by
Yt = Bt +
∞

i=1
Bt−i
i−1
!
j=0
At−j,
(4.23)
where the sum converges absolutely, almost surely.
We can develop some intuition for the conditions (4.22) and the form of the
solution (4.23) by iterating equation (4.21) k times to obtain
Yt = At(At−1Yt−2 + Bt−1) + Bt
= Bt +
k

i=1
Bt−i
i−1
!
j=0
At−j + Yt−k−1
k!
i=0
At−i.
--- page 158 ---

142
4. Financial Time Series
The conditions (4.22) ensure that the middle term on the right-hand side converges
absolutely and the ﬁnal term disappears. In particular, note that
1
k + 1
k

i=0
ln |At−i|
a.s.
−→E(ln |At|) < 0
by the strong law of large numbers. So
k!
i=0
|At−i| = exp

k

i=0
ln |At−i|

a.s.
−→0,
which shows the importance of the E(ln |At|) < 0 condition. The solution (4.23) to
the SRE is a strictly stationary process (being a function of iid variables (As, Bs)s⩽t),
and the E(ln |At|) < 0 condition turns out to be the key to the strict stationarity of
ARCH and GARCH models.
Stationarity of ARCH(1).
The squared ARCH(1) model (4.20) is an SRE of the
form (4.21) with At = α1Z2
t and Bt = α0Z2
t . Thus the conditions in (4.22) translate
into the requirements that E(ln+ |α0Z2
t |) < ∞, which is automatically true for the
ARCH(1) process as we have deﬁned it, and E(ln(α1Z2
t )) < 0. This is the condition
for a strictly stationary solution of the ARCH(1) equations and it can be shown that
it is in fact a necessary and sufﬁcient condition for strict stationarity (see Bougerol
and Picard 1992). From (4.23), the solution of equation (4.20) takes the form
X2
t = α0
∞

i=0
αi
1
i!
j=0
Z2
t−j.
(4.24)
If the (Zt) are standard normal innovations, then the condition for a strictly stationary solution is approximately α1 < 3.562; perhaps somewhat surprisingly, if
the (Zt) are scaled t innovations with four degrees of freedom and variance 1, the
condition is α1 < 5.437. Strict stationarity depends on the distribution of the innovations but covariance stationarity does not; the necessary and sufﬁcient condition
for covariance stationarity is always α1 < 1, as we now prove.
Proposition 4.18. The ARCH(1) process is a covariance-stationary white noise
process if and only if α1 < 1. The variance of the covariance-stationary process is
given by α0/(1 −α1).
Proof. Assuming covariance stationarity it follows from (4.20) and E(Z2
t ) = 1 that
σ 2
x = E(X2
t ) = α0 + α1E(X2
t−1) = α0 + α1σ 2
x .
Clearly, σ 2
x = α0/(1 −α1) and we must have α1 < 1.
Conversely, if α1 < 1, then, by Jensen’s inequality,
E(ln(α1Z2
t )) ⩽ln(E(α1Z2
t )) = ln(α1) < 0,
and we can use (4.24) to calculate that
E(X2
t ) = α0
∞

i=0
αi
1 =
α0
1 −α1
.
--- page 159 ---

4.3. GARCH Models for Changing Volatility
143
−20
−10
0
10
Time
0
100
200
300
400
500
−104
104
0
108
−108
−1010
1010
0
1020
−1020
(a)
(b)
(c)
Figure 4.7.
(a), (b) Strictly stationary ARCH(1) models with Gaussian innovations which
are not covariance stationary (α1 = 1.2 and α1 = 3, respectively). (c) A non-stationary
(explosive) process generated by the ARCH(1) equations with α1 = 4. Note that (b) and (c)
use a special double-logarithmic y-axis where all values less than one in modulus are plotted
at zero.
The process (Xt)t∈Z is a martingale difference with a ﬁnite, non-time-dependent
second moment. Hence it is a white noise process.
See Figure 4.7 for examples of non-covariance-stationary ARCH(1) models
as well as an example of a non-stationary (explosive) process generated by the
ARCH(1) equations. The process in Figure 4.6 is covariance stationary.
On the stationary distribution of Xt.
It is clear from (4.24) that the distribution of
the (Xt) in an ARCH(1) model bears a complicated relationship to the distribution of
the innovations (Zt). Even if the innovations are Gaussian, the stationary distribution
of the time series is not Gaussian, but rather a leptokurtic distribution with more
slowly decaying tails.
Moreover, from (4.17) we see that the distribution of Xt is a normal mixture
distribution of the kind discussed in Section 3.2. Its distribution depends on the
distribution of σt, which has no simple form.
Proposition 4.19. For m ⩾1, the strictly stationary ARCH(1) process has ﬁnite
moments of order 2m if and only if E(Z2m
t
) < ∞and α1 < (E(Z2m
t
))−1/m.
--- page 160 ---

144
4. Financial Time Series
Proof. We rewrite (4.24) in the form X2
t = Z2
t
∞
i=0Yt,i for positive rvs Yt,i =
α0αi
1
i
j=1Z2
t−j, i ⩾1, and Yt,0 = α0. For m ⩾1 the following inequalities hold
(the latter being Minkowski’s inequality):
E(Y m
t,1) + E(Y m
t,2) ⩽E((Yt,1 + Yt,2)m) ⩽((E(Y m
t,1))1/m + (E(Y m
t,2))1/m)m.
Since
E(X2m
t
) = E(Z2m
t
)E
 ∞

i=0
Yt,i
m 
,
it follows that
E(Z2m
t
)
∞

i=0
E(Y m
t,i) ⩽E(X2m
t
) ⩽E(Z2m
t
)
 ∞

i=0
(E(Y m
t,i))1/m
m
.
Since E(Y m
t,i) = αm
0 αim
1 (E(Z2m
t
))i, it may be deduced that all three quantities are
ﬁnite if and only if E(Z2m
t
) < ∞and αm
1 E(Z2m
t
) < 1.
For example, for a ﬁnite fourth moment (m = 2) we require α1 < 1/
√
3 in the
case of Gaussian innovations and α1 < 1/
√
6 in the case of t innovations with
six degrees of freedom; for t innovations with four degrees of freedom the fourth
moment is undeﬁned.
Assuming the existence of a ﬁnite fourth moment, it is easy to calculate its value,
and also that of the kurtosis of the process. We square both sides of (4.20), take
expectations of both sides and then solve for E(X4
t ) to obtain
E(X4
t ) =
α2
0E(Z4
t )(1 −α2
1)
(1 −α1)2(1 −α2
1E(Z4t )).
The kurtosis of the stationary distribution κX can then calculated to be
κX = E(X4
t )
E(X2t )2 = κZ(1 −α2
1)
(1 −α2
1κZ),
where κZ = E(Z4
t ) denotes the kurtosis of the innovations. Clearly, when κZ > 1,
the kurtosis of the stationary distribution is inﬂated in comparison with that of the
innovation distribution; for Gaussian or t innovations κX > 3, so the stationary
distribution is leptokurtic. The kurtosis of the process in Figure 4.6 is 9.
Parallels with the AR(1) process.
We now turn our attention to the serial dependence structure of the squared series in the case of covariance stationarity (α1 < 1).
We write the squared process as
X2
t = σ 2
t Z2
t = σ 2
t + σ 2
t (Z2
t −1).
(4.25)
Setting Vt = σ 2
t (Z2
t −1) we note that (Vt)t∈Z forms a martingale difference series,
since E|Vt| < ∞and E(Vt | Ft−1) = σ 2
t E(Z2
t −1) = 0. Now we rewrite (4.25) as
X2
t = α0 + α1X2
t−1 + Vt, and observe that this closely resembles an AR(1) process
for X2
t , except that Vt is not necessarily a white noise process. If we restrict our
--- page 161 ---

4.3. GARCH Models for Changing Volatility
145
attention to processes where E(X4
t ) is ﬁnite, then Vt has a ﬁnite and constant second moment and is a white noise process. Under this assumption, X2
t is an AR(1)
according to Deﬁnition 4.7 of the form

X2
t −
α0
1 −α1

= α1

X2
t−1 −
α0
1 −α1

+ Vt.
It has mean α0/(1−α1) and we can use Example 4.11 to conclude that the autocorrelation function is ρ(h) = α|h|
1 , h ∈Z. Figure 4.6 shows an example of an ARCH(1)
process with ﬁnite fourth moment whose squared values follow an AR(1) process.
4.3.2
GARCH Processes
Deﬁnition 4.20. Let(Zt)t∈Z beSWN(0, 1).Theprocess(Xt)t∈Z isaGARCH(p, q)
process if it is strictly stationary and if it satisﬁes, for all t ∈Z and some strictly
positive-valued process (σt)t∈Z, the equations
Xt = σtZt,
σ 2
t = α0 +
p

i=1
αiX2
t−i +
q

j=1
βjσ 2
t−j,
(4.26)
where α0 > 0, αi ⩾0, i = 1, . . . , p, and βj ⩾0, j = 1, . . . , q.
The GARCH processes are generalized ARCH processes in the sense that the
squared volatility σ 2
t is allowed to depend on previous squared volatilities, as well
as previous squared values of the process.
The GARCH(1, 1) model.
In practice, low-order GARCH models are most widely
used and we will concentrate on the GARCH(1, 1) model. In this model periods of
high volatility tend to be persistent, since |Xt| has a chance of being large if either
|Xt−1| is large or σt−1 is large; the same effect can be achieved in ARCH models of
highorder,butlower-orderGARCHmodelsachievethiseffectmoreparsimoniously.
A simulated realization of a GARCH(1, 1) process with Gaussian innovations and
its volatility are shown in Figure 4.8; in comparison with the ARCH(1) model of
Figure 4.6 it is clear that the volatility persists longer at higher levels before decaying
to lower levels.
Stationarity.
It follows from (4.26) that for a GARCH(1, 1) model we have
σ 2
t = α0 + (α1Z2
t−1 + β)σ 2
t−1,
(4.27)
which is again an SRE of the form Yt = AtYt−1 + Bt, as in (4.21). This time it is an
SRE for Yt = σ 2
t rather than X2
t , but its analysis follows easily from the ARCH(1)
case.
The condition E(ln |At|) < 0 for a strictly stationary solution of (4.21) translates
to the condition E(ln(α1Z2
t + β)) < 0 for (4.27) and the general solution (4.23)
becomes
σ 2
t = α0 + α0
∞

i=1
i!
j=1
(α1Z2
t−j + β).
(4.28)
--- page 162 ---

146
4. Financial Time Series
If (σ 2
t )t∈Z is a strictly stationary process, then so is (Xt)t∈Z, since Xt = σtZt and
(Zt)t∈Z is simply strict white noise. The solution of the GARCH(1, 1) deﬁning
equations is then
Xt = Zt
"
#
#
$α0

1 +
∞

i=1
i!
j=1
(α1Z2
t−j + β)

,
(4.29)
and we can use this to derive the condition for covariance stationarity.
Proposition 4.21. The GARCH(1, 1) process is a covariance-stationary white noise
process if and only if α1 +β < 1. The variance of the covariance-stationary process
is given by α0/(1 −α1 −β).
Proof. We use a similar argument to Proposition 4.18 and make use of (4.29).
Fourth moments and kurtosis.
Using a similar approach to Proposition 4.19 we can
use (4.29) to derive conditions for the existence of higher moments of a covariancestationary GARCH(1, 1) process. For the existence of a fourth moment, a necessary
and sufﬁcient condition is that E((α1Z2
t + β)2) < 1, or alternatively that
(α1 + β)2 < 1 −(κZ −1)α2
1.
Assuming this to be true we calculate the fourth moment and kurtosis of Xt. We
square both sides of (4.27) and take expectations to obtain
E(σ 4
t ) = α2
0 + (α2
1κZ + β2 + 2α1β)E(σ 4
t ) + 2α0(α1 + β)E(σ 2
t ).
Solving for E(σ 4
t ), recalling that E(σ 2
t ) = E(X2
t ) = α0/(1 −α1 −β), and setting
E(X4
t ) = κZE(σ 4
t ) we obtain
E(X4
t ) =
α2
0κZ(1 −(α1 + β)2)
(1 −α1 −β)2(1 −α2
1κZ −β2 −2α1β),
from which it follows that
κX =
κZ(1 −(α1 + β)2)
(1 −(α1 + β)2 −(κZ −1)α2
1).
Again it is clear that the kurtosis of Xt is greater than that of Zt whenever κZ > 1,
such as for Gaussian and scaled t innovations. The kurtosis of the GARCH(1, 1)
model in Figure 4.8 is 3.77.
Parallels with the ARMA(1, 1) process.
Using the same representation as in equation (4.25), the covariance-stationary GARCH(1, 1) process may be written as
X2
t = α0 + α1X2
t−1 + βσ 2
t−1 + Vt,
where Vt is a martingale difference, given by Vt = σ 2
t (Z2
t −1). Since σ 2
t−1 =
X2
t−1 −Vt−1, we may write
X2
t = α0 + (α1 + β)X2
t−1 −βVt−1 + Vt,
(4.30)
--- page 163 ---

4.3. GARCH Models for Changing Volatility
147
0
200
400
600
800 1000
−4
−2
0
0
200
400
600
800 1000
0.8
1.0
1.2
1.4
1.6
1.8
2.0
Lag
0
10
15
20
25
30
Lag
ACF
0
10
15
20
25
30
0
0.2
0.4
0.6
0.8
1.0
(a)
(b)
(c)
(d)
5
5
ACF
0
0.2
0.4
0.6
0.8
1.0
2
4
Figure 4.8.
A GARCH(1, 1) process with Gaussian innovations and parameters α0 = 0.5,
α1 = 0.1, β = 0.85: (a) the realization of the process; (b) the realization of the volatility; and
correlograms of (c) the raw and (d) the squared values. The process is covariance stationary
with unit variance and a ﬁnite fourth moment and the squared values follow an ARMA(1, 1)
process. The true form of the ACF of the squared values is shown by a dashed line in the
correlogram.
which begins to resemble an ARMA(1, 1) process for X2
t . If we further assume that
E(X4
t ) < ∞, then, recalling that α1 + β < 1, we have formally that

X2
t −
α0
1 −α1 −β

= (α1 + β)

X2
t−1 −
α0
1 −α1 −β

−βVt−1 + Vt
is an ARMA(1, 1) process. Figure 4.8 shows an example of a GARCH(1, 1) process
with ﬁnite fourth moment whose squared values follow an ARMA(1, 1) process.
The GARCH(p, q) model.
Higher-order ARCH and GARCH models have the
same general behaviour as ARCH(1) and GARCH(1, 1), but their mathematical
analysis becomes more tedious. The condition for a strictly stationary solution of the
--- page 164 ---

148
4. Financial Time Series
deﬁning SRE has been derived by Bougerol and Picard (1992), but is complicated.
The necessary and sufﬁcient condition that this solution is covariance stationary is
p
i=1 αi + q
j=1 βj < 1.
A squared GARCH(p, q) process has the structure
X2
t = α0 +
max(p,q)

i=1
(αi + βi)X2
t−i −
q

j=1
βjVt−j + Vt,
where αi = 0 for i = p + 1, . . . , q if q > p, or βj = 0 for j = q + 1, . . . , p if
p > q. This resembles the ARMA(max(p, q), q) process and is formally such a
process provided EX4
t < ∞.
Integrated GARCH.
The study of integrated GARCH (or IGARCH) processes
has been motivated by the fact that, in some applications of GARCH modelling
to daily or higher-frequency risk-factor return series, the estimated ARCH and
GARCH coefﬁcients (α1, . . . , αp, β1, . . . , βq) are observed to sum to a number very close to one, and sometimes even slightly larger than one. In a model
where p
i=1 αi + q
j=1 βj ⩾1, the process has inﬁnite variance and is thus noncovariance-stationary. The special case where p
i=1 αi + q
j=1 βj = 1 is known
as IGARCH and has received some attention.
For simplicity consider the IGARCH(1, 1) model. We use (4.30) to conclude that
the squared process must satisfy
∇X2
t = X2
t −X2
t−1 = α0 −(1 −α1)Vt−1 + Vt,
where Vt is a noise sequence deﬁned by Vt = σ 2
t (Z2
t −1) and σ 2
t = α0 +α1X2
t−1 +
(1−α1)σ 2
t−1. This equation is reminiscent of an ARIMA(0, 1, 1) model (see (4.14))
for X2
t , although the noise Vt is not white noise, nor is it strictly speaking a martingale
difference according to Deﬁnition 4.6. E(Vt | Ft−1) is undeﬁned since E(σ 2
t ) =
E(X2
t ) = ∞, and therefore E|Vt| is undeﬁned.
4.3.3
Simple Extensions of the GARCH Model
Many variants on and extensions of the basic GARCH model have been proposed.
We mention only a few (see Notes and Comments for further reading).
ARMA models with GARCH errors.
We have seen thatARMA processes are driven
by a white noise (εt)t∈Z and that a covariance-stationary GARCH process is an
example of a white noise. In this section we put the ARMA and GARCH models
together by setting the ARMA error εt equal to σtZt, where σt follows a GARCH
volatility speciﬁcation in terms of historical values of εt. This gives us a ﬂexible
family of ARMA models with GARCH errors that combines the features of both
model classes.
Deﬁnition 4.22. Let (Zt)t∈Z be SWN(0, 1). The process (Xt)t∈Z is said to be an
ARMA(p1, q1) process with GARCH(p2, q2) errors if it is covariance stationary
--- page 165 ---

4.3. GARCH Models for Changing Volatility
149
and satisﬁes difference equations of the form
Xt = µt + σtZt,
µt = µ +
p1

i=1
φi(Xt−i −µ) +
q1

j=1
θj(Xt−j −µt−j),
σ 2
t = α0 +
p2

i=1
αi(Xt−i −µt−i)2 +
q2

j=1
βjσ 2
t−j,
where α0 > 0, αi ⩾0, i = 1, . . . , p2, βj ⩾0, j = 1, . . . , q2, and p2
i=1αi +
q2
j=1βj < 1.
To be consistent with the previous deﬁnition of an ARMA process we build the
covariance-stationarity condition for the GARCH errors into the deﬁnition. For the
ARMAprocesstobeacausalandinvertiblelinearprocess,asbefore,thepolynomials
˜φ(z) = 1 −φ1z −· · · −φp1zp1 and ˜θ(z) = 1 + θ1z + · · · + θq1zq1 should have no
common roots and no roots inside the unit circle.
Let (Ft)t∈Z denote the natural ﬁltration of (Xt)t∈Z and assume that the ARMA
model is invertible. The invertibility of the ARMA process ensures that µt is
Ft−1-measurable as in (4.13). Moreover, since σt depends on the inﬁnite history
(Xs −µs)s⩽t−1, the ARMA invertibility also ensures that σt is Ft−1-measurable.
Simple calculations show that µt = E(Xt | Ft−1) and σ 2
t = var(Xt | Ft−1), so
that µt and σ 2
t are the conditional mean and variance of the new process.
GARCH with leverage.
One of the main criticisms of the standard ARCH and
GARCH models is the rigidly symmetric way in which the volatility reacts to recent
returns, regardless of their sign. Economic theory suggests that market information
should have an asymmetric effect on volatility, whereby bad news leading to a fall
in the equity value of a company tends to increase the volatility. This phenomenon
has been called a leverage effect, because a fall in equity value causes an increase in
the debt-to-equity ratio or so-called leverage of a company and should consequently
make the stock more volatile. At a less theoretical level it seems reasonable that
falling stock values might lead to a higher level of investor nervousness than rises
in value of the same magnitude.
One method of adding a leverage effect to a GARCH(1, 1) model is by introducing
an additional parameter into the volatility equation (4.26) to get
σ 2
t = α0 + α1(Xt−1 + δ|Xt−1|)2 + βσ 2
t−1.
(4.31)
We assume that δ ∈[−1, 1] and α1 ⩾0 as in the GARCH(1, 1) model. Observe
that (4.31) may be written as
σ 2
t =

α0 + α1(1 + δ)2X2
t−1 + βσ 2
t−1,
Xt−1 ⩾0,
α0 + α1(1 −δ)2X2
t−1 + βσ 2
t−1,
Xt−1 < 0,
and hence that
∂σ 2
t
∂X2
t−1
=

α1(1 + δ)2σ 2
t−1,
Xt−1 ⩾0,
α1(1 −δ)2σ 2
t−1,
Xt−1 < 0.
--- page 166 ---

150
4. Financial Time Series
The response of volatility to the magnitude of the most recent return depends on
the sign of that return, and we generally expect δ < 0, so bad news has the greater
effect.
Threshold GARCH.
Observe that (4.31) may easily be rewritten in the form
σ 2
t = α0 + ˜α1X2
t−1 + ˜δ1I{Xt−1<0}X2
t−1 + βσ 2
t−1,
(4.32)
where ˜α1 = α1(1 + δ)2 and ˜δ = −4δα1. Equation (4.32) gives the most common
version of a threshold GARCH (or TGARCH) model. In effect, a threshold has been
set at level zero, and at time t the dynamics depend on whether the previous value of
the process Xt−1 (or innovation Zt−1) was below or above this threshold. However,
it is also possible to set non-zero thresholds in TGARCH models, so this represents
a more general class of model than GARCH with leverage.
In a less common version of threshold GARCH the coefﬁcients of the GARCH
effects depend on the signs of previous values of the process; this gives a ﬁrst-order
process of the form
σ 2
t = α0 + α1X2
t−1 + βσ 2
t−1 + δ1{Xt−1<0}σ 2
t−1.
(4.33)
Remark 4.23. Note, also, that a further way to introduce asymmetry into a GARCH
model is to explicitly use an asymmetric innovation distribution (albeit normalized
to have mean zero and variance one). Candidate distributions could come from the
generalized hyperbolic family of Section 3.2.3.
4.3.4
Fitting GARCH Models to Data
Building the likelihood.
In practice, the most widely used approach to ﬁtting
GARCH models to data is maximum likelihood.We consider in turn the ﬁtting of the
ARCH(1) and GARCH(1, 1) models, from which the ﬁtting of general ARCH(p)
and GARCH(p, q) models easily follows.
For the ARCH(1) and GARCH(1, 1) models suppose we have a total of n + 1
data values X0, X1, . . . , Xn. It is useful to recall that we can write the joint density
of the corresponding rvs as
fX0,...,Xn(x0, . . . , xn) = fX0(x0)
n
!
t=1
fXt|Xt−1,...,X0(xt | xt−1, . . . , x0).
(4.34)
For the pure ARCH(1) process, which is ﬁrst-order Markovian, the conditional
densities fXt|Xt−1,...,X0 in (4.34) depend on the past only through the value of σt or,
equivalently, Xt−1. The conditional density is easily calculated to be
fXt|Xt−1,...,X0(xt | xt−1, . . . , x0) = fXt|Xt−1(xt | xt−1) = 1
σt
g
xt
σt

,
(4.35)
where σt = (α0 + α1x2
t−1)1/2 and g(z) denotes the density of the innovations
(Zt)t∈Z. We recall that this must have mean zero and variance one and typical
choices would be the standard normal density or the density of a t distribution
scaled to have unit variance.
--- page 167 ---

4.3. GARCH Models for Changing Volatility
151
However, the marginal density fX0 in (4.34) is not known in a tractable closed
form forARCH and GARCH models and this poses a problem for basing a likelihood
on (4.34).The solution employed in practice is to construct the conditional likelihood
given X0, which is calculated from
fX1,...,Xn|X0(x1, . . . , xn | x0) =
n
!
t=1
fXt|Xt−1,...,X0(xt | xt−1, . . . , x0).
(4.36)
For the ARCH(1) model this follows from (4.35) and is
L(α0, α1; X) = fX1,...,Xn|X0(X1, . . . , Xn | X0) =
n
!
t=1
1
σt
g
Xt
σt

,
with σt = (α0 + α1X2
t−1)1/2. For an ARCH(p) model we would use analogous
arguments to write down a likelihood conditional on the ﬁrst p values.
In the GARCH(1, 1) model σt is recursively deﬁned in terms of σt−1, and here,
instead of using (4.36), we construct the joint density of X1, . . . , Xn conditional on
realized values of both X0 and σ0, which is
fX1,...,Xn|X0,σ0(x1, . . . , xn | x0, σ0) =
n
!
t=1
fXt|Xt−1,...,X0,σ0(xt | xt−1, . . . , x0, σ0).
The conditional densities fXt|Xt−1,...,X0,σ0 depend on the past only through the value
of σt, which is given recursively from σ0, X0, . . . , Xt−1 using σ 2
t = α0 +α1X2
t−1 +
βσ 2
t−1. This gives us the conditional likelihood
L(α0, α1, β; X) =
n
!
t=1
1
σt
g
Xt
σt

,
σt =

α0 + α1X2
t−1 + βσ 2
t−1.
The problem remains that the value of σ 2
0 is not actually observed, and this is usually
solved by choosing a starting value, such as the sample variance of X1, . . . , Xn, or
even simply zero.
For a GARCH(p, q) model we would assume that we had n + p data values
labelled X−p+1, . . . , X0, X1, . . . , Xn.We would evaluate the likelihood conditional
on the (observed) values of X−p+1, . . . , X0 as well as the (unobserved) values of
σ−q+1, . . . , σ0, for which starting values would be used as above. For example, if
p = 1 and q = 3, we require starting values for σ0, σ−1 and σ−2.
A similar approach can be used to develop a likelihood for an ARMA model with
GARCH errors. In this case we would end up with a conditional likelihood of the
form
L(θ; X) =
n
!
t=1
1
σt
g
Xt −µt
σt

,
where σt follows a GARCH speciﬁcation and µt follows an ARMA speciﬁcation
as in Deﬁnition 4.22, and all unknown parameters (possibly including unknown
parameters of the innovation distribution) have been collected in the vector θ. We
could of course also consider models with leverage or threshold effects.
--- page 168 ---

152
4. Financial Time Series
Deriving parameter estimates.
Consider, then, a log-likelihood of the form
ln L(θ; X) =
n

t=1
lt(θ),
(4.37)
where lt denotes the log-likelihood contribution arising from the tth observation.
The maximum likelihood estimate ˆθ maximizes the (conditional) log-likelihood
in (4.37) and, being in general a local maximum, solves the likelihood equations
∂
∂θ ln L(θ; X) =
n

t=1
∂lt(θ)
∂θ
= 0,
(4.38)
where the left-hand side is also known as the score vector of the conditional likelihood. The equations (4.38) are usually solved numerically using so-called modiﬁed Newton–Raphson procedures. A particular method which is widely used for
GARCH models is the BHHH method of Berndt, Hall, Hall and Hausmann.
In describing the behaviour of parameter estimates in the following paragraphs,
we distinguish two situations. In the ﬁrst situation we assume that the model that has
been ﬁtted has been correctly speciﬁed, so that the data are truly generated by a time
series model with both the assumed dynamic form and innovation distribution. We
describe the asymptotic behaviour of the maximum likelihood estimates (MLEs)
under this idealization.
In the second situation we assume that the correct dynamic form is ﬁtted but that
the innovations are erroneously assumed to be Gaussian. Under this misspeciﬁcation
the model ﬁtting procedure is known as quasi-maximum likelihood (QML) and the
estimates obtained are QMLEs. Essentially, the Gaussian likelihood is treated as an
objective function to be maximized rather than a proper likelihood; our intuition
suggests that this may still give reasonable parameter estimates and this turns out to
be the case under appropriate assumptions about the true innovation distribution.
Properties of MLEs.
It helps to recall at this point the asymptotic distribution
theory for MLEs in the classical iid case, which is summarized in Section A.3. The
asymptotic results we give for GARCH models have a similar form to the results
in the iid case, but it is important to realize that this is not simply an application
of these results. The asymptotics have been separately and laboriously derived in a
series of papers for which starting references are given in Notes and Comments. We
will give results for pure GARCH models withoutARMA components or additional
leverage structure, which have been studied rigorously, but the form of the results
will apply more generally.
For a pure GARCH(p, q) model with Gaussian innovations it can be shown that
(assuming the model has been correctly speciﬁed)
√n( ˆθn −θ)
d−→Np+q+1(0, I(θ)−1),
where
I(θ) = E
∂lt(θ)
∂θ
∂lt(θ)
∂θ′

= −E
∂2lt(θ)
∂θ∂θ′

(4.39)
--- page 169 ---

4.3. GARCH Models for Changing Volatility
153
is the Fisher information matrix arising from any single observation. Thus we have
consistent and asymptotically normal estimates of the GARCH parameters. In practice, the expected information matrix I(θ) is approximated by an observed information matrix, and here we could take the observed information matrix coming from
either of the equivalent forms for the expected information matrix in (4.39). That is,
we could use
¯I(θ) = 1
n
n

t=1
∂lt(θ)
∂θ
∂lt(θ)
∂θ′

or
¯J(θ) = −1
n
n

t=1
∂2lt(θ)
∂θ∂θ′ ,
(4.40)
where the ﬁrst matrix is said to have outer-product form and the second is said to have
Hessian form. These matrices are estimated by evaluating them at the MLEs to get
¯I( ˆθ) or ¯J( ˆθ). In practice, this is done by numerical ﬁrst and second differencing of
the log-likelihood at the MLE and the necessary matrices are obtained as byproducts
of the BHHH procedure for deriving the parameter estimates.
If the model is correctly speciﬁed, the estimates ¯I( ˆθ) and ¯J( ˆθ) should be broadly
similar, being estimators based on two different expressions for the same Fisher
informationmatrix.Inpractice,wecouldalsoestimateI(θ)by ¯J( ˆθ) ¯I( ˆθ)−1 ¯J( ˆθ),and
this anticipates the so-called sandwich estimator that is used in the QML procedure.
Properties of QMLEs.
In this approach we assume that the true data-generating
mechanism is a GARCH(p, q) model with non-Gaussian innovations, but we
attempt to estimate the parameters of the process by maximizing the likelihood
for a GARCH(p, q) model with Gaussian innovations. We still obtain consistent
estimators of the model parameters and, if the true innovation distribution has a
ﬁnite fourth moment, we again get asymptotic normality; however, the form of the
asymptotic covariance matrix changes.
We now distinguish between matrices I(θ) and J(θ), given by
I(θ) = E
∂lt(θ)
∂θ
∂lt(θ)
∂θ′

,
J(θ) = −E
∂2lt(θ)
∂θ∂θ′

,
where the expectation is now taken with respect to the true model (not the misspeciﬁed Gaussian model). The matrices I(θ) and J(θ) differ in general (unless the
Gaussian model is correct). It may be shown that
√n( ˆθn −θ)
d−→Np+q+1(0, J(θ)−1I(θ)J(θ)−1),
(4.41)
and the asymptotic covariance matrix is said to be of sandwich form; it can be
estimated by ¯J( ˆθ)−1 ¯I( ˆθ) ¯J( ˆθ)−1, where ¯I(θ) and ¯J(θ) are deﬁned in (4.40). If
the model-checking procedures described below suggest that the dynamics have
been adequately described by the GARCH model, but the Gaussian assumption
seems doubtful, then standard errors for parameter estimates should be based on
this covariance matrix estimate.
Model checking.
As withARMA models it is usual to check ﬁtted GARCH models
usingresiduals.WeconsiderageneralARMA–GARCHmodeloftheformXt−µt =
εt = σtZt, with µt and σt as in Deﬁnition 4.22. In this model we distinguish
--- page 170 ---

154
4. Financial Time Series
between unstandardized and standardized residuals. The former are the residuals
ˆε1, . . . , ˆεn from theARMA part of the model; they are calculated using the approach
in (4.15), and under the hypothesized model they should behave like a realization of
a pure GARCH process. The latter are reconstructed realizations of the SWN that
is assumed to drive the GARCH part of the model, and they are calculated from the
former by
ˆZt = ˆεt/ˆσt,
ˆσ 2
t = ˆα0 +
p2

i=1
ˆαi ˆε2
t−i +
q2

j=1
ˆβj ˆσ 2
t−j.
(4.42)
To use (4.42) we need some initial values, and one solution is to set required starting
values of ˆεt equal to zero and required starting values of the volatility ˆσt equal to
either the sample variance or zero. Because the ﬁrst few values will be inﬂuenced
by these starting values, as well as the starting values required to calculate the
unstandardized residuals, they may be ignored in later analyses.
ThestandardizedresidualsshouldbehavelikeanSWNandthiscanbeinvestigated
by constructing correlograms of raw and absolute values and applying portmanteau
tests of strict white noise, as described in Section 4.2.3.
Assuming that the SWN hypothesis is not rejected, so that the dynamics have
been satisfactorily captured, the validity of the distribution used in the ML ﬁtting
can also be investigated using QQplots and goodness-of-ﬁt tests for the normal or
scaled t distributions. If the Gaussian likelihood does a reasonable job of estimating
dynamics, but the residuals do not behave like iid standard normal observations, then
the QML ﬁtting philosophy can be adopted and standard errors can be estimated
using the sandwich estimator implied by (4.41) above.
This opens up the possibility of two-stage analyses where ﬁrst the dynamics are
estimated by QML methods and then the innovation distribution is modelled using
the residuals from the dynamic model as data. The ﬁrst stage is sometimes called
pre-whitening of the data. In the second stage we might consider using heavier-tailed
models than the Gaussian that also allow some asymmetry in the innovations.
A disadvantage of the two-stage approach is that the error from the time series
modelling propagates through to the distributional ﬁtting in the second stage and the
overall error is hard to quantify, but the procedure does lead to more transparency in
model building and allows us to separate the tasks of volatility modelling and modelling the shocks that drive the process. In higher-dimensional risk-factor modelling
it may be a useful pragmatic approach.
Example 4.24 (GARCH model for Microsoft log-returns). We consider the
Microsoft daily log-returns for the period 1997–2000 (1009 values), as shown in
Figure 4.9.Although the raw returns show no evidence of serial correlation (see Figure 4.10), their absolute values do show serial correlation and they fail a Ljung–Box
test (based on the ﬁrst 10 estimated correlations) at the 5% level.
For these data, models with Student t innovations are clearly preferred to models
withGaussianinnovations,soweadoptanMLapproachtoﬁttingmodelswitht innovations. We compare the standard GARCH(1, 1) model (with a constant mean term)
--- page 171 ---

4.3. GARCH Models for Changing Volatility
155
0.02
0.04
0.06
Q1 Q2 Q3 Q4 Q1 Q2 Q3 Q4 Q1 Q2 Q3 Q4 Q1 Q2 Q3 Q4 Q1
1997
1998
1999
2000
2001
Conditional SD
−0.1
0
0.1
Original series
Values
Values
Figure 4.9.
Microsoft log-returns 1997–2000; data and estimate of
volatility from a GARCH(1, 1) model with a leverage term.
ACF
Lag
ACF
Lag
(a)
(b)
(c)
(d)
0
10
15
20
25
30
5
0
10
15
20
25
30
5
0
0.4
0.8
0
0.4
0.8
Figure 4.10. Microsoft log-returns 1997–2000; correlograms of data ((a) raw and (b) absolute values) and residuals ((c) raw and (d) absolute values) from a GARCH(1, 1) model.
with models that incorporate ARMA structure (AR(1), MA(1) and ARMA(1, 1))
for the conditional mean; the ARMA structure seems to offer little improvement in
the model and the basic GARCH(1, 1) model is favoured in an Akaike comparison.
However, a model with a leverage term as in (4.31) does seem to offer an improvement. Both the raw and absolute standardized residuals obtained from this model
show no visual evidence of serial correlation (see again Figure 4.10) and they do not
fail Ljung–Box tests. The estimated degrees-of-freedom parameter of the (scaled)
--- page 172 ---

156
4. Financial Time Series
−4
−2
0
2
4
6
−6
−4
−2
0
6
Quantiles of t distribution
Standardized residuals
2
4
Figure 4.11.
Microsoft log-returns 1997–2000; QQplot of residuals from a GARCH(1, 1)
model with leverage against a Student t distribution with 6.30 degrees of freedom.
Table 4.2.
Analysis of Microsoft log-returns for the period 1997–2000; ML estimates of
parameters and standard errors for a GARCH(1, 1) model with a leverage term under the
assumption of t innovations.
Parameter
Estimate
Standard error
Ratio
µ
9.35 × 10−4
7.21 × 10−4
1.30
α0
7.79 × 10−5
3.07 × 10−5
2.54
α1
0.108
0.0369
2.91
β
0.778
0.0673
11.57
δ
−0.178
0.123
−1.45
t distribution is 6.30 (the standard error is 1.07) and a QQplot of the residuals against
this reference distribution reveals a satisfactory correspondence (see Figure 4.11).
The estimates of the remaining parameters (with standard errors) in this model are
given in Table 4.2.
Notes and Comments
The ARCH process was originally proposed by Engle (1982), and the GARCH
process by Bollerslev (1986), who gave the condition for covariance stationarity.
Overview texts on GARCH models include the book by Gourieroux (1997) and
a number of useful review articles including Bollerslev, Chou and Kroner (1992),
Bollerslev, Engle and Nelson (1994) and Shephard (1996). There are also substantial
sections on GARCH models in the books by Alexander (2001), Tsay (2002) and
