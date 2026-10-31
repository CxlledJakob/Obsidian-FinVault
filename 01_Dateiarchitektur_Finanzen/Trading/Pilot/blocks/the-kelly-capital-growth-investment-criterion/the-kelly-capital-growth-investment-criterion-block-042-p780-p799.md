# The Kelly capital growth investment criterion _ theory and -- Leonard C_ Maclean, Edward O_ Thorp, W_ T_ Ziemba, Leonard -- World Scientific Handbook -- isbn13 9781283148344 -- bec576e26410d0c695fd5b867d08ec4f -- An.pdf — pages 780–799

--- page 780 ---

A Dynamic Portfolio of Investment Strategies
751
Mulvey, J. M., S. S. N. Kaul, and K. D. Simsek (2004). Evaluating a trend-following commodity index for multi-period asset allocation. Journal of Alternative Investments,
7, 54- 69.
Mulvey, J. M. and W . C. Kim (Fall 2009). Evaluating style investment: Does a fund
market defined along equity styles add value? Quantitative Finance, 9, 637- 651.
Mulvey, J . M. and W. C. Kim (2009). Multi-stage financial planning: Integrating stochastic
programs and policy simulators. In G. Infanger (Ed.). Stochastic Programming: The
State of the Art.
Mulvey, J. M. and W. C. Kim (2008). Constantly rebalanced portfolio -
Is mean reversion
necessary? Encyclopedia of Quantitative Finance, 2, 714- 717.
Mulvey, J. M., B. Pauling, and R. E. Madey (2003a). Advantages of multiperiod portfolio
models. Journal of Portfolio Management, 29, 35- 45.
Mulvey, J. M., K. Simsek, Z. Zhang, and F. Fabozzi (2008) . Assisting defined-benefit
pension plans. Operations Research, 56, 1066- 1078.
Mulvey, J. M., K. Simsek, and Z. Zhang (2006). Improving investment performance for
pension plans. Journal of Asset Management, 7, 93- 108.
Mulvey, J. M., C. Ural, and Z. Zhang (2007). Improving performance for long-term investors: Wide diversification, leverage and overlay strategies. Quantitative Finance,
7(2) , 1- 13.
Mulvey, J. M. and S. Ling (2009). Replicating private equity returns by means of sector
ETFs. Working paper, Princeton University.
Rouwenhorst, K. G. (1998). International momentum strategies. The Journal of Finance,
53(1) , 267-284.
Samuelson, P. A. (1969). Lifetime portfolio selection by dynamic stochastic programming.
Review Economics Statistics, 51, 239- 246.
Samuelson, P. A. (1971) . The fallacy of maximizing the geometric mean in long sequences
of investing or gambling. Proceedings National Academy of Science, 68, 2493- 2496.
Samuelson, P. A. (1979). Why we should not make mean log of wealth big though years
to act are long. Journal of Banking and Finance, 3, 305-307.
Stutzer, M. (2003). Portfolio choice with endogenous utility: A large deviation approach.
Journal of Econometrics, 116, 365- 386.
Swensen, D. (2000). Pioneering Portfolio Management. US: Free Press.
Thorp, E. O. (1969). Optimal gambling systems for favorable games. Review of the International Statistical Institute, 37(3), 273- 293.
Zenios, S. A. and W. T. Ziemba (2006) , eds. Handbook of Asset and Liability Management.
Series of Handbooks in Finance, Vol. 1. Amsterdam: Elsevier.
Zenios, S. A. and W. T. Ziemba (2007), eds. Handbook of Asset and Liability Management.
Series of Handbooks in Finance, Vol. 2. Amsterdam: Elsevier.
Zhang, Z. (2006). Stochastic optimization for enterprise risk management. Doctoral Dissertation. Department of Operations Research and Financial Engineering, Princeton
University, Princeton, NJ.
Ziemba, W. T. and J. M. Mulvey (1998) , eds. Worldwide Asset and Liability Modeling.
UK: Cambridge University Press.
Ziemba, W. T. (2005). The symmetric downside risk Sharpe ratio and the evaluation of
great investors and speculators. Journal of Portfolio Management, Fall, 108- 122.
17
--- page 781 ---

This page is intentionally left blank
--- page 782 ---

Available online at www.sciencedirect.com
SCIENCE@DIR 'ECTO
JOURNAL OF
Economic
D)'!lamics
& Control
753
ELSEVIER
Journal of Economic Dynamics & Control 28 (2004) 975 - 990
www.elsevier.com/locate/econbase
51
Intertemporal surplus management
Markus RudolP'*, William T. Ziembab
a WHU-Ol/o Beisheil1l Graduate School ot Mal/aaement, Dresdnel" Bank chair 01 Finance, Burgplatz 2,
56179 Vallendar, Germal/y
b Facility (it Commerce, University 01 BriTish Columbia, 2053 Main Mall, Vancollt;er, BC,
Canada V6T 122
Abstract
This paper presents an intertemporal portfolio selection model for pension funds or life insurance funds that maximizes the intertemporal expected utility of the surplus of assets net of
liabilities.' Following Merton (Econometrica 41 (1973) 867), it is assumed that both the asset
and the liability retU11l follow Ito processes as functions of a state variable. The optimum occurs
for investors holding four funds: the market portfolio, the hedge portfolio for the state variable,
the hedge portfolio for the liabilities, and the riskless asset. In contrast to Merton's result in
the assets only case, the liability hedge is independent of preferences and only depends on the
funding ratio. With HARA utility the investments in the state variable hedge portfolio are also
preference independent. Finally, with log utility the market portfolio investment depends only
on the current funding ratio.
© 2003 Elsevier B.V. All rights reserved .
.! EL classification: G23; Gil
Keywords: Asset; Beta; Funding ratio; HARA utility function; Hedge portfolio; Intertcmporal capital assct
pricing model; Ito process; .! -li.mction: Liabilities; Log utility function: Safety first; Shortfall risk; State
variable; Surplus management
1. Introduction
intertemporal asset allocation models date to Merton (1969, 1971, 1973) (see also the
summary in Merton, 1990) and Samuelson (1969). Merton presents a continuous time
intertemporal model whereas Samuelson discusses the discrete time case. Both models
• Corresponding author. WHU-Otto Beisheim Hochschule, Burgplatz 2, 56179 Vallendar, Gelmany.
Tel.: + 49-261-6509421; fax: + 49-261-6509409.
E-Illail addres,w!s: markus.rudolf@unisg.ch, mrudolf@whu.edu (M. Rudolf), ziemba@interchange.ubc.ca
(W.T. Ziemba).
URL: http://www.whu.edu/banking
0165-1889/031$ - see front matter ~) 2003 Elsevier B.Y. All rights reserved.
doi: I 0.1 0 16/S0.l65-1889(03 )00058-7
--- page 783 ---

754
M Rudolf and W T. Ziemba
976
M. Rudo/I w.T. ZiembalJournal o/Economic Dynamics & Conlrol28 (2004) 975 - 990
formulate a lifetime portfolio selection problem. Merton's (1973) intertemporal capital
asset pricing model derives equilibrium asset premia. In contrast to Sharpe's (1964)
CAPM, Merton's CAPM is based on a three-fund theorem. Each rational investor
holds the riskless asset, the market portfolio, and a hedge portfolio for a so-called
state variable in order to maximize his lifetime expected utility. The state variable is
a stochastic term, which affects the asset price processes. The hedge portfolio provides
maximum correlation to the state variable, i.e. it provides the best possible hedge
against the state variable variance. Continuous time models can be applied to surplus
optimization problems, since surplus optimizers, such as pension funds or life insurers,
distribute the surplus to those who are insured. Pension funds or life insurance funds are
frequently broadly internationally diversified. Exchange rate movements are considered
as state variables.
Merton, (1993, reprinted in Ziemba and Mulvey (1998), see also Constantinides'
(1993) comments on Merton's paper) addresses a problem similar to surplus optimization. He advocates the view that University endowment funds can be managed by using
Merton's (1969) intertemporal portfolio selection model. His objective function is to
maximize the lifetime expected utility of University activities with specific costs. The
University activity portfolio includes education, training, research, storage of knowledge, etc. Since the activities of a University have to be optimized with respect to their
costs, the activity costs are "liabilities" for universities. In contrast to our approach,
Merton (1993) specifies the University's non-endowment cash flows as Ito processes
dependent on the activity costs. This is the classical setting of Merton 's (1973) intertemporal CAPM, where the state variables are given by the activity costs. The result
is that each utility maximizing University holds three funds, the market portfolio, the
riskless portfolio and a hedge portfolio against fluctuations of the activity costs. The
composition across those three funds depends on the risk preferences towards market
and activity cost volatility.
This paper provides a synthesis of the surplus management and the continuous time
finance literature. Both the assets and liabilities of a pension fund are modeled as
stochastic processes dependent on stochastic state variables. Only the asset mix can
be influenced by the fund manager's decision. The paper provides a solution to his
decision problem. In comparison to Merton's (1993) setting, the advance made by the
paper is that one (or several) state variable(s) are allowed to be distinct from the
liabilities. I.e. in contrast to Merton (1993), this paper explicitly examines the impact
of long-term liabilities. Three important results developed are: first, if only one state
variable is considered, Merton's three-fund theorem is extended to a four-fund theorem.
The four distinct mutual funds are: the market portfolio, the state variable hedge portfolio, the liability hedge portfolio, and the riskless asset. Secondly and most important,
the investment in the liability hedge portfolio depends only on the current funding
ratio of a pension or life insurance fund and is independent of the utility function.
This result differs from Merton's (1993) findings. The preference independence of the
liability hedge portfolio has major implications for monitoring pension funds and life
insurance companies. Thirdly, the state variable hedging policy is preference independent if hyperbolic absolute risk aversion (HARA) utility functions are assumed. With
log utility, even the market portfolio investment is independent of the risk aversion
--- page 784 ---

Intertemporal Surplus Management
755
lvl. RudolJ: W. T Ziemba /Journal 0/ Economic Dynamics & Con/rol28 (2004 ) 975 - 990
977
coefficient which is caused by the fact that log utility is equivalent to HARA utility
with a risk tolerance coefficient of a = O.
[n Section 2, the intertemporal surplus management model and a four-fund theorem
are derived. In Section 3 we show that with HARA utility, the risk tolerance coefficients
of the model are related to the funding ratio and to the currency betas of the portfolio. A k state variable case is derived in Section 4. Section 5 describes a case study
for a surplus optimizer who is diversified across the stock, the bond markets, and cash
equivalents of four countries (EMU countries are treated as a single country). Section 6
concludes the paper.
2. An intertemporal surplus management model-a four-fund theorem
Having surplus over time is what life insurance companies and pension funds try
to achieve. In both life insurance companies and pension funds, parts of the surplus
are distributed to the clients usually once every year. Hence, optimizing the investment
strategy of a life insurance or a pension fund is equivalent to maximizing the expected
lifetime utility of the surplus.
For t ~ 0 we have the stochastic processes A(t),L(t), Y(t), representing assets, liabilities, and a state variable Y. An extension of the setting to k state variables is possible
without difficulties (see e.g. Richard (1979) and Adler and Dumas (1983» . Adler and
Dumas (1983) take purchasing power parities as state variables. The surplus S(t) and
the funding ratio F(t) are defined by
Set) := A(t) - L(t),
F(t) := A(t)/L(t).
(1 )
According to Merton (1973), the state variable Y follows a geometric Brownian motion
(i.e. log-normally distributed) where J.ly and O'y are constants representing the drift and
volatility, and Zy(t) is a standard Wiener process. The state variable as well as the
assets and the liabilities are assumed to follow the stochastic processes:
dY(t) = Y(t)[J.ly dt + O'y dZy(t)],
dA(t) = A(t)[J.lA(t, Y(t»dt + O'ACt, Y(t»dZACt)],
dL(t) = L(t)[J.lL(t, Y(t»dt + O'L(t, Y(t»dZL(t)] ,
(2)
where the drift and volatility parameters for the assets and liabilities are allowed to
depend on both time and state variable, and where ZAt),ZL(t) are Wiener processes
correlated with Z y(t) and also with each other. Hence, we have cross variations
dZA(t) dZy(t) = PAY dr,
dZL(t)dZy(t) = PLY dt,
--- page 785 ---

756
M Rudolf and W T. Ziemba
978
M. Rudolf; W.T Ziemba/Joul'l1([/ o./Ecol1omic Dynamics & Conlro/28 (2004) 975 - 990
where PAY represents the instantaneous correlation between the Wiener processes ZAt)
and Zy(t), PLY is the instantaneous correlation between ZL(t) and Zy(t), and PAL
refers to the instantaneous correlation between ZAt) and ZL(t). The return processes
Ry(t),RACt),RL(t) for the state variable, assets and liabilities are defined by
Ry(t) := dY(t)/ Y(t),
RAt) := dA(t)/A(t),
RL(t) := dL(t)/L(t).
Following Sharpe and Tint (1990) and according to Eq. (1), the surplus return process
is defined as
R ( ).= dS(t) = R (t) _ RL(t)
st.
A(t)
A
F(t)
= [f1A -
:C~)] dt + aA dZAt) -
:C~) dZL(t).
Since dS(t) = Rs(t)A(t), using Eq. (3) we have
E[dS(t)] = A(t) (f1A -
:C~») dt,
2 (2
az
aAL )
dS(t)dS(t) =A (t) aA + pet) - 2 F(t)
dt,
dS(t)dY(t)=A(t)Y(t) (aAY - ;g») dt,
dY(t) dY(t) = y2(t)a} dt,
(3 )
(4)
where aAL := PALUAuL,UAY := PAYUAuy,aLY := PLYaLay are the covariances of assets
with liabilities and of the state variable with assets and liabilities, respectively.
The objective is to maximize the expected lifetime utility of surplus, which implies
identifying an optimum surplus strategy. I For an analysis of a situation with convex
penalties for underfunding, see Carino and Ziemba (1998). The expected utility is positively related to the surplus in each period. This is because positive surpluses improve
the wealth position of the insurants of a pension or a life insurance fund, even if the
yearly retirement benefits are over-covered by the surplus. Hence, in this interpretation, the insurants are like shareholders of the fund. Then the following equation is the
fund's optimization problem, where U is an additively separable, twice differentiable,
I To avoid underfunding in particular periods we assume a steady state implying that the dollar value of
cmployecs (insurance policies) entering equals those leaving the pension fund (insurance company) dollar
value.
--- page 786 ---

Intertemporal Surplus Management
757
M. RudoU: W. T Ziemba I Journal of Economic Dynamics & Control 28 (201J4 ) 975 · 990
979
concave utility function and T is the end of the fund's existence:
T
J(S,Y,t):= m\~xEt ([ U(S,Y,T)dT)
(!
I+ dt
j.T
)
= max Et
U(S, Y, T) dT +
U(S, Y, T) dT
.
II
t
.I+ dl
(5)
Et denotes expectation with respect to the information set at time t and the J -function
is the maximum of the life insurance or pension fund's expected lifetime utility. The
maximum in (5) is taken with respect to w, the vector of portfolio fractions of the
risky assets. Let n be the number of portfolio assets and Wi (I ::::; i ::::; n) be the portfolio
fraction of asset i, then WI := (WI, ... , wn ) . Applying the Bellman principle (see e.g.
Dixit and Pindyck (1994, Chapter 4», according to Merton (1969) and Merton (1990,
p. 102) and according to the mean value theorem for integrals yields
J(S, Y, t) = U(S, Y, t) dt + max Et[J(S + dS, Y + dY, t + dt)].
(6)
w
Let Js be the first partial derivative of J with respect to S, Jss the second partial
derivative of J with respect to S, Jy and J yy the first and second partial derivatives
with respect to Y, and JSY the derivative of J with respect to Sand Y. Applying Ito's
lemma and Eq. (4) yields (see the appendix for proof),
0= U(t,S, Y)
Jt + JsA(t) (/lA - :C~»)
1
2 (2
al
a
AL )
+JyY(t)/ly + 2. JssA (t) aA + F2(t) - 2· F(t)
w
(7)
+ max
+~ J yy y2(t)a} + JsyA(t)Y(t) (aAY -
;~;»)
Let rnA be the vector of expected asset returns of the risky assets of dimension n, e be
the n-dimensional vector of ones, V be the n x n matrix of covariances between the 11
risky assets, VAL and VAl' be the vectors of covariances between the 11 assets and the
liabilities, respectively, with the state variable. It is assumed that a riskless asset with
return r exists. Then rearranging (7) yields the following equation (see the appendix
for proof and definitions of the matrix and the vectors):
0= U(t,S, Y)
Jt+JsA(t)(w/(rnA-re)+r- :C~»)
I
2
('
al
w' VAL)
+Jy Y(t)/ly + 2. JssA (t) w Vw + F2(t) - 2 F(t) .
w
(8)
+ max
1
2
2
(
I
aLl' )
+2. JyyY (t)a y +JsyA(t)Y(t) w VAY - F(t)
--- page 787 ---

758
M Rudolf and W T. Ziemba
980
M. RudoU: W. T Ziemba/Journal 0/ Economic Dynamics & Control 28 (2()04) 975990
Differentiating (8) with respect to W yields 2
where
Js
V - Ie
)
Y(t)JSY V-I
V-IVAL
W = - ---
rnA - re -
VAY + ---
A(t)Jss
A(t)Jss
F(t)
Js
Y(t)JSY
c
=: -a --- . WM - b
. Wy + -- . WL,
A(t)Jss
A(t)Jss
F(t)
V -- I (rnA - re)
WM := e'V - I(rnA - re) '
V - I VAL
WL := ' V - I
'
e
V,1 L
(9)
The vectors WM, Wy, and WL are of dimension n with elements that sum to I; a, b,
and c are real constants. The optimum portfolio consists of four single portfolios: the
market portfolio WM, the hedge portfolio for the state variable Wy, which is Merton's
(J 973) state variable hedge portfolio, the hedge portfolio for the liabilities WL, and the
riskless asset. The state variable hedge portfolio Wy reveals the maximum correlation
with the state variable Y (see the appendix). A perfect hedge for the state variable
could be achieved if the universe of n risky assets contains forward contracts on the
state variable. Then the state variable hedge portfolio would consist of a single asset,
which is the forward contract. The third portfolio WL is interesting. For the liabilities
there exist no hedging opportunities at the financial markets (i.e. a portfolio which
hedges wage increases or inflation rates). Eq. (9) shows how a liability hedge can be
constructed. This is related to the problem addressed by Ezra (1991) and Black (1989)
and solves it intertemporally. In the four-fund theorem, life insurance and pension funds
invest in the following four funds, if they maximize their expected lifetime utility (5)
based on the stochastic differential equations (2) and (3):
1. The market portfolio WM with level - a(Js/A(t )Jss ).
2. The state variable hedge portfolio Wy with level - b(Y(t)Jsr/A(t)Jss ).
3. The riskless asset with level 1+ a(Js/A(t)Jss ) + b(Y(t)Jsr/A(t)Jss ) - c/F(t).
4. Finally, the liability hedge portfolio WI. with level c/F(t).
Thus, the holdings of the liability hedge portfolio are independent of preferences. The
most interesting result in the portfolio selection equation (9) is that the liability hedge
portfolio holdings depend only on the current funding ratio and not on the form of the
utility function. In order to maximize its lifetime expected utility, each life insurance
or pension fund should hedge the liabilities according to the financial endowment.
The percentages of each of the three other funds differ according to the risk preferences of the investors. For example, -a (Js/A (t)Jss ) is the percentage invested in
2 The derivati ve of (8) with respect to w is: 0 =.Js(m,j -re)+A(/).Jss Vw - [A(t)/ F(t)J./\:\·VAL + Y(/).JSy VAl"
--- page 788 ---

Intertemporal Surplus Management
759
il1. Rudolf, W. T. Ziemba /Journal of Economic Dynamics & Control 28 (2004) 975 ~ 990
981
the market p01ifolio. Since J is a "derived" utility function, this ratio is a times
the Arrow/Pratt relative risk tolerance with respect to changes in the surplus. That
is, the higher the risk tolerance towards market risk, the higher the fraction of the
market portfolio holdings. The percentage of the state variable hedge portfolio is
- be Y(t)Jsr/A(t)Jss ). Merton (1973) showed that this ratio is b times the Arrow/Pratt
relative risk tolerance with respect to changes in the state variable. The percentage of
the liability hedge portfolio is c/F(t). Surprisingly, and in contrast to Merton's results,
this portfolio does not depend on preferences nor on a specific utility function, but
only on the funding ratio of the pension fund. The lower the funding ratio, the higher
the percentage of the liability hedge portfolio.
This allows for a simple technique to monitor life insurance and pension funds,
which extends Merton's (1993) approach. In most funding systems, funds are legally
obliged to invest subject to a deterministic threshold return. Since payments of life
insurance or pension funds depend on the growth and the volatility of wage rates,
this is not appropriate. For instance, if the threshold return is 4% p.a. and the wages
grow by more than this, the liabilities cannot be covered by the assets. Our model
suggests instead that a portfolio manager of a pension fund should invest in a portfolio
which smoothes the fluctuation of the surplus returns caused by wage volatility, i.e.
in a liability hedge portfolio. Since the liability hedge portfolio depends only on the
funding ratio, preferences of the insurants have not to be specified.
3. Risk preference, funding ratio, and currency betas
Assume that the utility function is from the HARA class. Merton (1971 and 1990,
p. 140) shows that this is equivalent to assuming that the J-function (6) belongs to
the HARA class as well. Let rx < I be the risk tolerance coefficient. Then
U(S, Y, t) C HARA q J(S, Y, t) C HARA,
1 -
rx (KS
)rt.
J(S, Y,t) =J[S(A(y),t] = -(-
-1- + 11
,
eP rx
-
rx
(10)
where /( and 11 > ° are real constants and p is the utility deflator. Observe that (10)
implies linear absolute risk tolerance since -Js/lss = S/ (l -
rx) + I1/K. The HARA
class of utility functions as defined in (10) is commonly used; it implies the negative
exponential utility functions J = _e-as when rx approaches -00, 11 = 1, and p = 0.
Moreover, the isoelastic power utility (see Ingersoll (1987, p. 39» J=Srt./rx is obtained
for 11 = 0, P = 0, and K = (I -
rx )(rt.-I )/rt. . Log utility is that member of isoelastic power
utility when rx approaches ° (11 = P = 0), since by applying I'Hopital's rule to the
equivalent utility function,
lim J(S, Y, t) = lim Srt. - 1 = lim (SIX In S) = In S.
rt.~O
rt.~O
rx
rt.~O
( II )
--- page 789 ---

760
M Rudolf and W. T. Ziemba
982
M. Rudolf W. T Ziemba /Journal (J/ Ecol1omic Dynamics & Con/rol28 (2004) 975 990
Under the HARA utility function assumption,
K (KS
)~ -I
Js' = -
-- + 11
,
.
ePI
I -(X
n;2 (n;s
)~-2
Jss =- -
-- + 11
,
ePI
I -
(X
dJs
dJs
dS
dA
.
dA
Jsy = -
= -' -
. -=Jss' -'
dY
dS
dA
dY
dY
The percentage holdings of the market portfolio may be re-expressed as
( 12)
(13 )
The market portfolio holdings thus depend on the funding ratio and on the risk aversion.
The higher F, the higher the investment in the market portfolio, and the higher (X, the
lower the market portfolio investment for funding ratios smaller than I. If a sufficient
funding is observed (i.e. F > I), then there is a positive relationship between (X and F.
If (X approaches 0 (log utility case), the coefficient for the market portfolio investment
becomes I - I /F plus the constantl1/ (AK). Thus, for log utility pension or life insurance
funds, risk aversion does not matter. Indeed only the funding ratio matters to determine
the market portfolio investment. For either case of utility functions, if the funding
ratio is 100%, there will be no investment in the risky market portfolio. Thus, the
funding ratio of a fund does not only determine the capability to bear risk but also the
willingness to take risk.
We now consider the percentage holding of the state variable hedge portfolio. Suppose the state variable Y is an exchange rate fluctuation, which affects the surplus of
a life insurance or pension fund. Given (12) it follows that
YJSY
dA/A
AJss
dY/Y
(14 )
Hence, the weight of the state variable hedge portfolio (14) is preference independent
if HARA utility is assumed. Assume the regression model RA = {3(RA' Ry )R y (asset
returns are linear functions of currency returns). Hence, -RA/Ry is the negative beta
of the portfolio with respect to the state variable. Using (14) it follows that
YJSY
-
-
= -f3(RA,Ry).
AJss
(15 )
If Y is an exchange rate, then -Ii equals the minimum variance hedge ratio for the
foreign currency position. The holdings of the state variable hedge portfolio are independent of preferences; they only depend on the foreign currency exposure of the
portfolio. The higher the exchange rate risk in the p0!1folio, the higher the currency
hedging.
Hence, for the HARA utility case, only the investment in the market portfolio depends on the risk aversion ('I.. The investments in all other funds are preference independent. They depend only on the funding ratio and on the exposure of the asset
portfolio to the state variable.
--- page 790 ---

Intertemporal Surplus Management
761
III. Rudolf W T Ziemba / Journal 0/ Economic Dynamics & Control 28 (201J4) 975 ,, 990
983
4. The multiple state variable case
Let k be the number of foreign currencies contained in a life insurance or pension
fund's portfolio, YI , ... , Yk be the exchange rates in terms of the domestic currency,
and R Y" ... , R Yk the exchange rate retUll1S of the k currencies. Then
YIJSY,
YkJSYk
- --, = -/J(R,1,Ry, ), ... , - -- = - P(R,1,R yk),
AJss
AJss
which are the Arrow/Pratt relative risk tolerances with respect to changes in the exchange rates for the HARA case. Let V,1y" . . . ,V,1Yk be the covariance vectors of the
retUll1S of the asset portfolio with the k exchange rate retull1s,
V - I V,1Y,
._ y - IVAl'k
WY' := e'Vlv.1Y, ' '' ·'wyk .
I'
e'Y- VAYk
which are the state variable hedge portfolios I-k, and bl := e'VlvAy" ... ,b" :=
e'V- 1 vAYk are the coefficients of the state variable hedge portfolios. A pension or a life
insurance fund with HARA utility function facing k state variables has the following
investment strategy (R,: = dA,IA,: retUll1 on risky asset I, 1=1, .. . ,11):
[
a
(
I) all]
2:
k
c
W = --
I - --
+ -
WM -
bP(R4 Ry)wy + --WL
1-0:
F(t)
AI(
.
1
.
,
,
,
F(t)
,
1= 1
( 16)
where
II
P(R;I, Ry,) = 2: WI P(RI, Rr;).
1=1
Since the right-hand side of Eq. (16) depends on the portfolio allocation w, it is not
possible to solve (16) analytically for w, However, numerical solutions can be applied.
For k state variables a (k + 3 )-fund theorem thus follows.
5. Case study
The following case study is based on a USD-based surplus optimizer investing in
the stock and bond markets of the US, UK, Japan, the EMU countries, Canada, and
Switzerland. Monthly MSCI data between January 1987 and July 2000 (163 observations) are used for the stock markets. The monthly JP Morgan indices are used for the
bond markets in this period (Salomon Brothers for Switzerland). The stochastic benchmark for a surplus optimizer is the quarterly Thomson Financial Datastream index
for US wages and salaries. Quarterly data are linearly interpolated in order to obtain
monthly wages and salaries data. The average growth rate of wages and salaries in the
U.S. between January 1987 and July 2000 was 5.7% p.a. (see Table I) with annualized volatility of 4.0%. Table I also contains the stock and bond market descriptive
statistics in USD, and the currency betas of the indices.
All foreign currencies except CAD, i.e. GBP, JPY, EUR, and CHF, have volatility of
about 12% p.a., and all currencies except JPY depreciated against the USD by a little
--- page 791 ---

762
M. Rudolf and W T. Ziemba
984
11I. Rudolt: W.T Ziemba/Journal oI Economic Dynamics & Conlrol28 (2004) 975 - 990
Table I
Descriptive statistics
Mean
Volatility
Beta
Beta
Beta
Beta
Bela
return
GBP
JPY
EUR
CAD
CHF
Stocks
USA
13.47
14.74
0.18
0.05
0.35
- 0.59
0.35
UK
9.97
17.96
- 0.47
- 0.36
- 0.29
- 0.48
- 0.14
Japan
3.42
25.99
- 0.61
- 1.1 I
- 0.45
--0.44
- 0.43
EMU countries
10.48
15.80
- 0.32
- 0.27
- 0.26
- 0.45
- 0.11
Canada
5.52
18.07
0.05
- 0.02
0.27
- 1.44
0.34
Switzerland
11 .56
18. 17
- 0.14
- 0.32
- 0.26
0.13
- 0.32
Bonds
USA
5.04
4.50
- 0.03
0.00
- 0.06
- 0.04
- 0.06
UK
6.86
12.51
- 0.92
- 0.44
--0.80
- 0.39
- 0.59
Japan
3.77
14.46
-0.53
- 1.04
- 0.75
0.09
- 0.72
EMU countries
7.78
10.57
- 0.69
- 0.42
- 0.93
-0.06
- 0.74
Canada
5.16
8.44
- 0.09
· 0.03
- 0.02
- 1.14
0.02
Switzerland
3.56
12.09
-0.67
- 0.53
- UJ3
0.19
-0.99
Exchange
GBP
0.1 I
11.13
0.37
0.86
0.42
0.64
rates in
JPY
-2.75
12.54
0.48
0.65
0.04
0.61
USD
EUR"
1.13
10.08
0.7
0.42
I
0.1
0.79
CAD
0.79
4.73
0.08
0
0.02
- 0.02
CHF
0.32
11.57
0.69
0.52
1.04
- 0.13
I
Wages and salaries
5.71
4.0
0
0.01
0
- 0.01
0
The stock market data are based on MSC indices and the bond data on .IP Morgan indices (Switzerland
on Salomon Brothers data). The wage and salary growth rate is from datastream. Monthly data between
January 1987 and July 2000 (163 observations) is used. All coetncients are in USD. The average returns
and volatilities arc in percent per annum.
a ECU before January 1999.
more than 0 to 1.13% per year. From a USD viewpoint, for GBP-beta is especially
high (absolute value) for the UK bond market. The Japanese stock and bond market
reveal a lPY -beta of - 1.11 and - 1.04, respectively, and the EMU bond market has a
EUR-beta of -0.93. Furthennore, the CAD-beta of the Canadian bond market is -1.14,
the CHF-beta of the Swiss bond market is -0.99. All other countries have substantially
lower currency betas. Since the betas are close to zero, the wages and salaries in the
U.S. obviously do not depend on currency movements.
The investor faces an exposure against five foreign currencies (GBP, lPY, EUR,
CAD, CHF), and has to invest into eight funds. Five of them are hedge pOlifolios
for the state variables, which are assumed to be CUITency returns. The next step is to
calculate the compositions of the eight funds. The results appear in Table 2. The major
holdings in the market portfolio are investments in the US stock market and the EMU
bond market. Substantial short positions for the tangency portfolio are obtained for the
Canadian stock and the Swiss bond market. The US bond portfolio is a major part of
a portfolio providing the best hedge against fluctuations in wages and salaries. More
than 126% of the liability hedge portfolio are invested in the US bond market. The
bond markets of the respective currencies dominate the currency hedge portfolios.
--- page 792 ---

Intertemporal Surplus Management
763
I'd. RudoU: W. T ZiembaiJoul'na/ 0/ Economic Dynamics & Control 28 (2004 ) 975 990
985
Table 2
Optimum portfolios of an internationally diversified pension fund from a USD perspective
Market
Liability hedge
Hedge
Hedge
Hedge
Hedge
Hedge
poJtfolio
portfolio
portfolio
portfolio
portfolio
portfolio
portfolio
GBP
Jpy
EUR
CAD
CHF
Stocks
USA
83.9
- 30.4
3.9
-4.5
-7.5
60.9
-5.1
UK
- 14.8
60.6
-3 1.0
- 1.1
- 8.6
-85.3
1.9
Japan
-6.7
2.7
6. 1
8.9
-2.4
- 4.0
- 0.7
EMU
- 19.2
- 683
35.3
12.8
23.5
138.3
-3.8
Canada
- 39.2
5.1
14.6
13.6
5.5
--2.6
- 0.9
Switzer!'
21.6
1.5
-24.8
-14.6
- 14.7
-100.7
1.0
Bonds
USA
14.8
126.0
-126.4
- 28.6
- 41.2
- 627.3
-35.9
UK
- 9.7
- 56.8
189.7
7.9
-3.4
97.5
-8.5
Japan
0.6
39.1
-31.2
133.9
-3.6
-30.1
6.4
EMU
138.5
9.6
-1 6.4
-38.0
97.3
- 170.1
34.0
Canada
7.9
5.0
-11.8
-32.6
- 7.9
679.6
0.9
Switzer!'
-77.7
5.9
91.9
42.4
62.9
143.8
110.7
The portfolio holdings are based on Eg. (9). All portfolio fractions are percentages. A riskless rate of
interest of 2%) per annum is asslImed.
Table 3
Weightings of the funds due to difTerent funding ratios
Funding ratio
0.9
1. 1
1.2
1.3
1.5
Market pOlttolio (%)
-1 1.5
0.0
6.3
12.3
18.2
24.6
Liability hedge portfolio (% )
14.8
13.3
12.1
11.1
10.2
8.9
I-ledge portfolio GBp (%)
- 0.6
- 0.5
- 0.5
- 0.5
- 0.4
- 0.4
Hedge portfolio Jpy (%)
1.2
1.1
1.0
0.9
0.9
0.8
Hedge pOItft)lio EUR (%)
0.3
0.2
0.1
0.0
0.0
-0.1
Hedge portfolio CAD (% )
- 0.1
-0.1
-0.1
- 0.1
- 0.1
- 0.1
Hedge portfolio CHF (% )
1.1
1.0
0.9
0.8
0.8
0.7
Riskless assets (%)
94.9
85.1
80.2
75.3
70.4
65.6
Portfolio beta against GBP
- 0.01
- 0.01
- 0.01
- 0.01
- 0.0 1
-0.01
Portfolio beta against JPY
0.02
0.02
0.02
0.02
0.02
0.02
Portfolio beta against EUR
0.01
0.00
0.00
0.00
0.00
0.00
Portfolio beta against CAD
- 0.02
- 0.02
- 0.01
- 0.01
- 0.01
- 0.01
Portfolio beta against CI-IF
0.02
0.01
0.0 1
0.01
0.01
0.0 1
The weightings of the portfolios according to Eg. ( 16), where C( = 0, i.e. log utility, is assllmed.
As derived in Section 3, the holdings of the six funds depend only on the funding
ratio and on the currency betas of the distinct markets. Thts is shown in Table 3.
For a funding ratio of one, there is no investment in the market portfolio and only
diminishing investments in the currency hedge portfolios. The portfolio betas against
the five currencies are close to zero for all funding ratios. The higher the funding
ratio, the higher the investment in the market portfolio, the lower the investments in
--- page 793 ---

764
M Rudolf and W T. Ziemba
986
M. Rudolf W. T Ziemba I Journal oj' Economic Dynamics & Control 28 (2004) 975-- 990
the liability and the state variable hedge portfolios, and the lower the investment in
the riskless fund. Negative currency hedge portfolios imply an increase of the currency
exposure instcad of a hedge against it. The increase of the market portfolio holdings
and the reduction of the hedge portfolio holdings and the riskless fund for increasing
funding ratios shows that the funding ratio is directly related to the ability to bear risk.
Rather than risk aversion coefficients, the funding ratio provides an objective measure
to quantify attitudes towards risk.
6. Conclusions
This paper derives a four-fund theorem for intertemporal surplus optimizers such as
life insurance and pension funds. In addition to the three funds identified by Merton
( 1973), the expected utility maximizing portfolio contains a liability hedge portfolio,
which is preference independent. Its holdings depend only on the funding ratio of
a pension fund. The higher the funding ratio, the lower the necessity for liabilities
hedging. As a practical consequence, the hedging policy of pension or life insurance
funds could very easily be monitored by authorities. This is due to the fact that in
the optimum, only the funding ratio is decisive for the liabilities hedge, and not the
utility function, which hardly can be determined by law. Today's pension fund laws do
not contain any rules for the treatment of stochastic wage growths. Although Merton
( 1993) addresses a similar problem of the optimal investment strategy for University
endowment funds, his setting is different. He describes the "liabilities" of universities,
i.e. the costs for their activities, as state variables. He obtains a preference-dependent
hedge portfolio for the activity costs. In contrast, here the liability returns are specified
as a part of the surplus return. In contrast to Merton's results, the hedge portfolio for
the liabilities is exclusively dependent on the funding ratio (and not on risk preferences)
of a life insurance or pension fund. The funding ratio is an objective measure, whereas
risk preferences are hard to determine.
The model provides an intertemporal portfolio selection approach for surplus optimizers. The intertemporal surplus management approach holds for investors who have
to cover liabilities by their assets in each moment of time. Since the investment strategy
of all investors is consumption orientated, it is reasonable to assume that all investors
invest in order to cover their liabilities. If the growth rate of individual consumption
is related to the growth of wages and salaries, the relevant benchmark for surplus optimizers refers to the growth rate and the volatility of wages and salaries. Finally, this
model suggests a new type of product for investment banks. Pension and life insurance
funds need to protect themselves against unanticipated changes in the growth rates of
wages and salaries. Investment banks could offer liability protection and hedge those
positions by purchasing a liability hedge portfolio as is given by Eq. (9).
Acknowledgements
Two anonymous referees of this journal have contributed valuable comments. Without implicating them, the authors thank the participants in a workshop at the ETH in
--- page 794 ---

lntertemporal Surplus Management
765
M. Rudolf w.T. Ziemba /Joul'nal o/ Economic Dynamics & Confrol28 (201M) 975- 990
987
Zurich, May 1996, the Annual Conference of the Deutsche Gesellschaft fUr
Finanzwirtschaft (DGF) in Berlin, September 1996, the EURO INFORMS Meeting
in Barcelona, July 1997, the Eighth International Conference on Stochastic Programming, Vancouver, August 1998, the INQUIRE, Venice Meeting, October 2000, Gunter
Franke, Christian Hipp, Astrid Eisenberg, Karl Keiber, Alexander Kempf, Andre Kronimus, Matthias Muck, Stanley Pliska, Bernd Schips, and Heinz Zimmennann for helpful
comments on an earlier draft. All remaining errors are ours.
Appendix A
A.I. Derivation of (7)
The arguments of the J -function are dropped for simplicity. o( dt) summarizes all
terms of higher order than I of dt. For o(dt) : limd(--->o o(dt)/dt = O. Applying Itas
lemma yields
J(S, Y, t) = U(S, Y, t) dt + max E([J(S + dS, Y + dY, t + dt)]
w
= U dt + max E([J + J( dt + Js dS + J y dY + ! Jss dS2 + ! J yy dy2
w
+Jsy dS dY + o(dt)].
Transforming the expression above yields
0= U dt + max E([J( dt + Js dS + Jy dY + ! Jss dS2 + ! Jyy dy2
w
+Jsy dS dY + o(dt)],
0= U dt + max[J( dt + JsE( dS) + lyE(dY) + ! Jss dS dS
w
+ ! lyy d Y d Y + JSY dS d Y],
and sub&tituting in the expressions in (4) yields (7).
A.2. Derivation of (8)
Denote the prices of the n risky assets by Aj(t), i = 1, . .. , n, and suppose they follow
the processes
dAi(t) = Ai(t)[J.li dt + ai dZi(t)],
i = 1, ... n,
--- page 795 ---

766
M Rudolf and W T. Ziemba
988
M. Rudol{ W. T Ziemba !Journal 0/ Economic Dynamics & Conlrol28 (2004) 975 · 99IJ
which defines the vector of risky expected asset retul1ls m~ := (iJ.i, ' .. , iJ.,,). The Wiener
processes Zi(t), i = 1, ... 11, are correlated according to
where Pi} is the instantaneous correlation between Zi(t) and Zj(t). If the covariance
between assets i and j is denoted by (Jij, then we have (Jij = (Ji(JjPij and the covariance
matrix V has entries (Ju, i.e.
V=
Suppose the fund holds Xi(t) shares of asset i at time t, and that the cash in the asset
pOltfolio at time t is B(t). Then the asset portfolio value A(t) is given by (Ai(t): price
of asset i)
"
A(t) = I>i(t)Ai(t) + B(t).
io= 1
In the next infinitesimal time interval dt, this evolves according to
n
II
dA(t) = LXi(f)dAi(f) + dB(t) = LXi(l)dAi(t) + rB(t)dt
i= 1
i=1
where r is the riskless interest rate. Define the vector of pOltfolio fractions w' =
(WI, ... ,Wn ) by
.( ) ._ xi(t)Ai(f)
wzt.-
A(t)'
i = l, ... ,I1.
The sum of risky and riskless investments is assumed to be I. Hence, the fraction
invested in the riskless asset is B(t)/A(t) = 1 -
I:~ I Wi. Therefore, the expression
above for dA(t) becomes
dA(f) = A(t) [t[UJi(iJ.i-r) + r]df+ tWi(JidZi(t)].
Comparing the above expression with Eq. (2), i.e. dA(t) =A(t)[iJ.A dt + (JA dZAt»), and
assuming that e' := (I, ... , I) is the n-dimensional vector of ones, gives
iJ.A = w'(mA - re) + r,
n
(JA dZAt) = L
Wi(Ji dZi(t).
i=1
From this follows that
(J~ = w'Vw,
--- page 796 ---

Intertemporal Surplus Management
767
lv1. Rudol/ W. T Ziemba / Journal 0/ Economic Dynamics & Conlrol 28 (201N j 975····990
989
where V is the covariance matrix given earlier. Furthermore, define (JiL( (JiY) as the
covariance between the ith risky asset and the liabilities (state variable). Denote the
vector of these covariances by
V~ L:= ((JIL, ... ,(Jnd,
V~y:= «(Jly, ... ,(JnY).
Then the relationship (JA L = W'VAL and ClAY = W'VAY is obvious. From the last four
representations of expected returns, variances, and covariances Eg. (8) follows.
A.3. Discussing Eq. (9)
Maximizing the covariance between the asset portfolio and the state variable,
= W'VAY--> max
w
'y
2
s.t. w w = ClA ,
where R I, ... , Rn refer to the n asset returns. Let }, be a Lagrange multiplier:
L = W'VAY -
A(W'YW -
Cl~)
=>
oL/ow = VAY -
2A ' .. Yw = 0
=>
w = y- I VAr/(2A).
o2L/(owi < 0 if and only if Y is positive definite.
Hence, Wy (the state variable hedge portfolio) maximizes the correlation between the
asset portfolio and the state variable. Furthermore,
2}.. w'Yw = W'VAY <=} 2ACl~ = (JAY
ClAY
_I
2). = -2 = [JAY => Y
VAY = [JAYW.
(JA
Multiplying the fractions of the asset portfolio by the regression coefficient [JAY provides
the fractions of the hedge portfolio.
References
Adler, M., Dumas, B., 1983. International portfolio choice and corporation finance: a synthesis. The Journal
of Finance 38 (3), 925-984.
Black, F., 1989. Should you use stocks to hedge your pension liability? Financial Analysts Journal 22,
10- 12.
Carino, D.R., Ziemba, W.T., 1998. Fonnulation of the Russell Yasuda-Kasai financial planning model.
Operations Research 46 (4), 433- 449.
Constantinides, G.M., 1993. Comment. In:.Clotfelter, c.T., Rothschild, M. (Eds.), The Economics of Higher
Education. University of Chicago Press, National Bureau of Economic Research, Chicago, pp. 236-242.
Dixit, A.K., Pindyck, R.S., 1994. Investment under uncertainty. Princeton University Press, New Jersey.
Ezra, D.O., 1991. Asset allocation by surplus optimization. Financial Analysts Journal 24, 51 - 57.
--- page 797 ---

768
M Rudolf and W T. Ziemba
990
M. Rudoll w. T Ziemba /Journal 0/ Econol11ic Dyn({l11ics & Control 28 (2004) 975 990
Ingersoll Jr., J.E., 1987. Theory of Financial Decision Making. Rowman & Littlefield, New York.
Merton, R.C., 1969. Lifetime portfolio selection under uncertainty: the continuous-time case. The Review of
Economics and Statistics 51, 247-257.
Merton, R.C., 1971. Optimal consumption and portfolio rules in a continuous-time model. Journal of
Economic Theory 3, 373-413.
Merton, R.C., 1973. An intertemporal capital asset pricing model. Econometrica 41, 867-887.
Merton, R.C., 1990. Continuous Time Finance. Blackwell Publishers Inc., Cambridge, MA (reprinted 1995).
Merton, R.C., 1993. Optimal investment strategies for university endowment funds. In: Clotfelter, C.T.,
Rothschild, M. (Eds.), The Economics of Higher Education. University of Chicago Press, National Bureau
of Economic Research, Chicago (reprinted in: Ziemba,W.T., Mulvey, J.M. (Eds.), (1998), Worldwide
Asset and Liability Modeling, Cambridge University Press, Cambridge, MA).
Richard, S.F., 1979. A generalized capital asset pricing model. In: Gruber, M.J., Elton, E.J. (Eds.), Portfolio
Theory, 25 Years After. North-Holland, New York, pp. 215-232.
Samuelson, P.A., 1969. Lifetime portfolio selection by dynamic stochastic programming. The Review of
Economics and Statistics 51, 239-246.
Sharpe, W.F., 1964. Capital asset prices: a theory of market equilibriums under conditions of risk. The
Journal of Finance 19 (3), 425-442.
Sharpe, W.F., Tint, L.G., 1990. Liabilities-a new approach. The Journal of Portfolio Management 17,
5-10.
Ziemba, W.T., Mulvey, J.M. (Eds.) 1998. World Wide Asset and Liability Modeling. Cambridge University
Press, Cambridge, MA.
--- page 798 ---

Journal a/Portfolio Management, 32(1), 108- 122 (2005)
769
52
The Symmetric Downside-Risk
Sharpe Ratio
And the evaluation if great investors and speculators.
William T. Ziemba
WrLLIAM T. ZIEMBA
is the alumni professor of
financial modeling and
stochastic optimization
emeritus at the Sauder
School of Business of the
Univenity of British
Columbia in Vancouver,
Canada, and a visiting professor of finance at the
Sloan School of Management of the M.assachusetts
Institute of Technology in
Cambridge, MA.
108
THE SYMMETRIC DOWNSIDE-RISK SHARPe RATIO
T
he Sharpe ratio is a very useful measure of
investment performance. Because it is based on
mean-variance theory, and thus is basically
valid only for quadratic preferences or normal
distributions, skewed investment returns can lead to misleading conclusions. This is especially true for superior
investors with many high returns. Superior investors may
use capital growth wagering ideas to implement their
strategies, which produces higher growth rates but also
higher variability of wealth.
My simple modification of the Sharpe ratio to
assume that the upside deviation is identical to the downside risk provides a useful modification and gives more
realistic results.
Exhibit 1 plots wealth levels using monthly data
from December 1985 through March 2000 for the Windsor Fund of George Neff, the Ford Foundation, the
Tiger Fund of Julian Robertson, the Quantum Fund of
George Soros, and Berkshire Hathaway, the fund run by
Warren Buffett, as well as the S&P 500 total return index,
U.S. Treasuries, and T-bills. Yearly data are shown in
Exhibit 2.
The means, standard deviations, and Sharpe [1966,
1994] ratios of these six funds, based on monthly, quarterly, and yearly net arithmetic and geometric total return
data, are shown in Exhibit 3. Shown as well are data on
the Harvard endowment (quarterly) plus U.S. Treasuries,
T-bills, and U.S. inflation, and number of negative months
and quarters.
The first panel in Exhibit 3 shows the data behind
FALL 2005
--- page 799 ---

770
PERFORMANCE EVALUATION
-----AND RISK ANALySIS----
The Symmetric Downside-Risk
Sharpe Ratio
WILLIAM T. ZIEMBA
108
The Sharpe ratio, a most useful measure of investment performance, has the disadvantage that it is based on meanvariance theory and thus is valid basically only for quadratic
preferences or normal distributions. Hence skewed investment returns can engender rnisleading conclusions. This
is especially true for superior investors with a number of
high returns. Many of these superior investors use capital
growth wagering ideas to implement their strategies,
which means higher growth rates but also higher variability
of wealth. A simple modification of the Sharpe ratio to
assume that the upside deviation is identical to the downside risk gives more realistic results.
W T. Ziemba
