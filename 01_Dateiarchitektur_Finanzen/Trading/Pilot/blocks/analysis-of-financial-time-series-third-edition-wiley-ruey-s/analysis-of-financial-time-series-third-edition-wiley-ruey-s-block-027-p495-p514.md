# Analysis of Financial Time Series, Third Edition (Wiley -- Ruey S_ Tsay -- Wiley series in probability and statistics, 3rd ed_, -- John Wiley & Sons, -- isbn13 9780470414354 -- 9f99b80c7b2dedd477f463dc5323f3b6 -- An.pdf — pages 495–514

--- page 495 ---

468
principal component analysis and factor models
three types of factor models and their applications in ﬁnance. Principal component
analysis and factor models for asset returns are also discussed in Alexander (2001)
and Zivot and Wang (2003).
The chapter is organized as follows. Section 9.1 introduces a general factor
model for asset returns, and Section 9.2 discusses macroeconomic factor models
with some simple examples. The fundamental factor model and its applications are
given in Section 9.3. Section 9.4 introduces principal component analysis that serves
as the basic method for statistical factor analysis. The PCA can also be used to
reduce the dimension in multivariate analysis. Section 9.5 discusses the orthogonal
factor models, including factor rotation and its estimation, and provides several
examples. Finally, Section 9.6 introduces asymptotic principal component analysis.
9.1
A FACTOR MODEL
Suppose that there are k assets and T time periods. Let rit be the return of asset i
in the time period t. A general form for the factor model is
rit = αi + βi1f1t + · · · + βimfmt + ϵit,
t = 1, . . . , T ;
i = 1, . . . , k,
(9.1)
where αi is a constant representing the intercept, {fjt|j = 1, . . . , m} are m common
factors, βij is the factor loading for asset i on the jth factor, and ϵit is the speciﬁc
factor of asset i.
For asset returns, the factor f t = (f1t, . . . , fmt)′ is assumed to be an
m-dimensional stationary process such that
E(f t) = µf ,
Cov(f t) = f ,
an m × m matrix,
and the asset speciﬁc factor ϵit is a white noise series and uncorrelated with the
common factors fjt and other speciﬁc factors. Speciﬁcally, we assume that
E(ϵit) = 0
for all i and t,
Cov(fjt, ϵis) = 0
for all j, i, t and s,
Cov(ϵit, ϵjs) =

σ 2
i ,
if i = j and t = s,
0,
otherwise.
Thus, the common factors are uncorrelated with the speciﬁc factors, and the speciﬁc
factors are uncorrelated among each other. The common factors, however, need not
be uncorrelated with each other in some factor models.
In some applications, the number of assets k may be larger than the number
of time periods T . We discuss an approach to analyze such data in Section 9.6. It
--- page 496 ---

a factor model
469
is also common to assume that the factors, hence rt, are serially uncorrelated in
factor analysis. In applications, if the observed returns are serially dependent, then
the models in Chapter 8 can be used to remove the serial dependence.
In matrix form, the factor model in Eq. (9.1) can be written as
rit = αi + βif t + ϵit,
where βi = (βi1, . . . , βim) is a row vector of loadings, and the joint model for the
k assets at time t is
rt = α + βf t + ϵt,
t = 1, . . . , T
(9.2)
where
rt = (r1t, . . . , rkt)′,
α = (α1, . . . , αk)′,
β = [βij]
is
a
k × m
factorloading matrix, and ϵt = (ϵ1t, . . . , ϵkt)′ is the error vector with Cov(ϵt) = D =
diag{σ 2
1 , . . . , σ 2
k }, a k × k diagonal matrix. The covariance matrix of the return rt
is then
Cov(rt) = βf β′ + D.
The model presentation in Eq. (9.2) is in a cross-sectional regression form if the
factors fjt are observed.
Treating the factor model in Eq. (9.1) as a time series, we have
Ri = αi1T + Fβ′
i + Ei,
(9.3)
for the ith asset (i = 1, . . . , k), where Ri = (ri1, . . . , riT )′, 1T is a T -dimensional
vector of ones, F is a T × m matrix whose tth row is f ′
t, and Ei = (ϵi1, . . . , ϵiT )′.
The covariance matrix of Ei is Cov(Ei) = σ 2
i I, a T × T diagonal matrix.
Finally, we can rewrite Eq. (9.2) as
rt = ξgt + ϵt,
where gt = (1, f ′
t)′ and ξ = [α, β], which is a k × (m + 1) matrix. Taking the
transpose of the prior equation and stacking all data together, we have
R = Gξ ′ + E,
(9.4)
where R is a T × k matrix of returns whose tth row is r′
t or, equivalently, whose
ith column is Ri of Eq. (9.3), G is a T × (m + 1) matrix whose tth row is g′
t,
and E is a T × k matrix of speciﬁc factors whose tth row is ϵ′
t. If the common
factors f t are observed, then Eq. (9.4) is a special form of the multivariate linear
regression (MLR) model; see Johnson and Wichern (2007). For a general MLR
model, the covariance matrix of ϵt need not be diagonal.
--- page 497 ---

470
principal component analysis and factor models
9.2
MACROECONOMETRIC FACTOR MODELS
For macroeconomic factor models, the factors are observed and we can apply the
least-squares method to the MLR model in Eq. (9.4) to perform estimation. The
estimate is
ξ ′ =

 α′
β
′

= (G′G)−1(G′R),
from which the estimates of α and β are readily available. The residuals of Eq.
(9.4) are
E = R −Gξ′.
Based on the model assumption, the covariance matrix of ϵt is estimated by

D = diag{ˆσ 2
1 , . . . , ˆσ 2
k },
where ˆσ 2
i is the (i, i)th element of E
′E/(T −m −1). Furthermore, the R2 of the
ith asset of Eq. (9.3) is
R2
i = 1 −[E
′E]i,i
[R′R]i,i
,
i = 1, . . . , k,
where Ai,i denotes the (i, i)th element of the matrix A.
Note that the aforementioned least-squares estimation does not impose the constraint that the speciﬁc factors ϵit are uncorrelated with each other. Consequently,
the estimates obtained are not efﬁcient in general. However, imposing the orthogonalization constraint requires nontrivial computation and is often ignored. One
can check the off-diagonal elements of the matrix E
′E/(T −m −1) to verify the
adequacy of the ﬁtted model. These elements should be close to zero.
9.2.1
Single-Factor Model
The best known macroeconomic factor model in ﬁnance is the market model; see
Sharpe (1970). This is a single-factor model and can be written as
rit = αi + βirmt + ϵit,
i = 1, . . . , k;
t = 1, . . . , T,
(9.5)
where rit is the excess return of the ith asset, rmt is the excess return of the market,
and βi is the well-known β for stock returns. To illustrate, we consider monthly
returns of 13 stocks and use the return of the S&P 500 index as the market return.
The stocks used and their tick symbols are given in Table 9.1, and the sample
period is from January 1990 to December 2003 so that k = 13 and T = 168. We
use the monthly series of 3-month Treasury bill rates of the secondary market as
--- page 498 ---

macroeconometric factor models
471
TABLE 9.1
Stocks Used and Their Tick Symbols in Analysis of Single-Factor Modela
Tick
Company
¯r(σr)
Tick
Company
¯r(σr)
AA
Alcoa
1.09(9.49)
KMB
Kimberly-Clark
0.78(6.50)
AGE
A.G. Edwards
1.36(10.2)
MEL
Mellon Financial
1.36(7.80)
CAT
Caterpillar
1.23(8.71)
NYT
New York Times
0.81(7.37)
F
Ford Motor
0.97(9.77)
PG
Procter & Gamble
1.08(6.75)
FDX
FedEx
1.14(9.49)
TRB
Chicago Tribune
0.95(7.84)
GM
General Motors
0.64(9.28)
TXN
Texas Instrument
2.19(13.8)
HPQ
Hewlett-Packard
1.37(11.8)
SP5
S&P 500 Index
0.42(4.33)
aSample means (standard errors) of excess returns are also given. The sample period is from January
1990 to December 2003.
the risk-free interest rate to obtain simple excess returns of the stock and market
index. The returns are in percentages.
We use S-Plus to implement the estimation method discussed in the previous
section. Most of the commands used also apply to the software R.
> x=read.matrix(‘‘m-fac9003.txt’’,header=T)
> xmtx=cbind(rep(1,168),x[,14])
> rtn=x[,1:13]
> xit.hat=solve(xmtx,rtn)
> beta.hat=t(xit.hat[2,])
> E.hat=rtn-xmtx%*%xit.hat
> D.hat=diag(crossprod(E.hat)/(168-2))
> r.square=1-(168-2)*D.hat/diag(var(rtn,SumSquares=T))
The estimates of βi, σ 2
i , and R2 for the ith asset return are given below:
> t(rbind(beta.hat,sqrt(D.hat),r.square))
beta.hat
sigma(i)
r.square
AA
1.292
7.694
0.347
AGE
1.514
7.808
0.415
CAT
0.941
7.725
0.219
F
1.219
8.241
0.292
FDX
0.805
8.854
0.135
GM
1.046
8.130
0.238
HPQ
1.628
9.469
0.358
KMB
0.550
6.070
0.134
MEL
1.123
6.120
0.388
NYT
0.771
6.590
0.205
PG
0.469
6.459
0.090
TRB
0.718
7.215
0.157
TXN
1.796
11.474
0.316
Figure 9.1 shows the bar plots of ˆβi and R2 of the 13 stocks. The ﬁnancial
stocks, AGE and MEL, and the high-tech stocks, HPQ and TXN, seem to have
higher β and R2. On the other hand, KMB and PG have lower β and R2. The R2
--- page 499 ---

472
principal component analysis and factor models
0.0
0.5
1.0
1.5
AA
AGE CAT
F
FDX GM HPQ
(a)
(b)
KMB MEL NYT
PG
TRB TXN
0.0 0.1 0.2 0.3 0.4
AA
AGE CAT
F
FDX GM HPQ KMB MEL NYT
PG
TRB TXN
Figure 9.1
Bar plots of (a) beta and (b) R2 for ﬁtting single-factor market model to monthly excess
returns of 13 stocks. S&P 500 index excess return is used as market index. Sample period is from
January 1990 to December 2003.
ranges from 0.09 to 0.41, indicating that the market return explains less than 50%
of the variabilities of the individual stocks used.
The covariance and correlation matrices of rt under the market model can be
estimated using the following:
> cov.r=var(x[,14])*(t(beta.hat)%*%beta.hat)+diag(D.hat)
> sd.r=sqrt(diag(cov.r))
> corr.r=cov.r/outer(sd.r,sd.r)
> print(corr.r,digits=1,width=2)
AA
AGE CAT
F
FDX
GM HPQ KMB MEL NYT
PG TRB TXN
AA 1.0 0.4 0.3 0.3 0.2 0.3 0.4 0.2 0.4 0.3 0.2 0.2 0.3
AGE 0.4 1.0 0.3 0.3 0.2 0.3 0.4 0.2 0.4 0.3 0.2 0.3 0.4
CAT 0.3 0.3 1.0 0.3 0.2 0.2 0.3 0.2 0.3 0.2 0.1 0.2 0.3
F 0.3 0.3 0.3 1.0 0.2 0.3 0.3 0.2 0.3 0.2 0.2 0.2 0.3
FDX 0.2 0.2 0.2 0.2 1.0 0.2 0.2 0.1 0.2 0.2 0.1 0.1 0.2
GM 0.3 0.3 0.2 0.3 0.2 1.0 0.3 0.2 0.3 0.2 0.1 0.2 0.3
HPQ 0.4 0.4 0.3 0.3 0.2 0.3 1.0 0.2 0.4 0.3 0.2 0.2 0.3
KMB 0.2 0.2 0.2 0.2 0.1 0.2 0.2 1.0 0.2 0.2 0.1 0.1 0.2
MEL 0.4 0.4 0.3 0.3 0.2 0.3 0.4 0.2 1.0 0.3 0.2 0.2 0.3
NYT 0.3 0.3 0.2 0.2 0.2 0.2 0.3 0.2 0.3 1.0 0.1 0.2 0.3
PG 0.2 0.2 0.1 0.2 0.1 0.1 0.2 0.1 0.2 0.1 1.0 0.1 0.2
TRB 0.2 0.3 0.2 0.2 0.1 0.2 0.2 0.1 0.2 0.2 0.1 1.0 0.2
TXN 0.3 0.4 0.3 0.3 0.2 0.3 0.3 0.2 0.3 0.3 0.2 0.2 1.0
--- page 500 ---

macroeconometric factor models
473
We can compare these estimated correlations with the sample correlations of the
excess returns.
> print(cor(rtn),digits=1,width=2)
AA
AGE CAT
F
FDX
GM HPQ KMB MEL NYT
PG TRB TXN
AA 1.0 0.3 0.6 0.5 0.2 0.4 0.5 0.3 0.4 0.4 0.1 0.3 0.5
AGE 0.3 1.0 0.3 0.3 0.3 0.3 0.3 0.3 0.4 0.4 0.2 0.2 0.3
CAT 0.6 0.3 1.0 0.4 0.2 0.3 0.2 0.3 0.4 0.3 0.1 0.4 0.3
F 0.5 0.3 0.4 1.0 0.3 0.6 0.3 0.3 0.4 0.4 0.1 0.3 0.3
FDX 0.2 0.3 0.2 0.3 1.0 0.2 0.3 0.3 0.2 0.2 0.1 0.3 0.2
GM 0.4 0.3 0.3 0.6 0.2 1.0 0.3 0.3 0.4 0.2 0.1 0.3 0.3
HPQ 0.5 0.3 0.2 0.3 0.3 0.3 1.0 0.1 0.3 0.3 0.1 0.2 0.6
KMB 0.3 0.3 0.3 0.2 0.3 0.3 0.1 1.0 0.3 0.2 0.3 0.3 0.1
MEL 0.4 0.4 0.4 0.4 0.2 0.4 0.3 0.4 1.0 0.3 0.4 0.3 0.3
NYT 0.4 0.4 0.3 0.4 0.3 0.2 0.3 0.2 0.3 1.0 0.2 0.5 0.2
PG 0.1 0.2 0.1 0.1 0.1 0.1 0.1 0.3 0.4 0.2 1.0 0.3 0.1
TRB 0.3 0.2 0.4 0.3 0.3 0.3 0.2 0.3 0.3 0.5 0.3 1.0 0.2
TXN 0.5 0.3 0.3 0.3 0.2 0.3 0.6 0.1 0.3 0.2 0.1 0.2 1.0
In ﬁnance, one can use the concept of global minimum variance portfolio
(GMVP) to compare the covariance matrix implied by a ﬁtted factor model with
the sample covariance matrix of the returns. For a given covariance matrix , the
global minimum variance portfolio is the portfolio ω that solves
min
ω σ 2
p,ω = ω′ω
such that
ω′1 = 1,
where σ 2
p,ω is the variance of the portfolio. The solution is given by
ω = −11
1′−11,
where 1 is the k-dimensional vector of ones.
For the market model considered, the GMVP for the ﬁtted model and the data
are as follows:
> w.gmin.model=solve(cov.r)%*%rep(1,nrow(cov.r))
> w.gmin.model=w.gmin.model/sum(w.gmin.model)
> t(w.gmin.model)
AA
AGE
CAT
F
FDX
GM
[1,] 0.0117 -0.0306 0.0792 0.0225 0.0802 0.0533
HPQ
KMB
MEL
NYT
PG
TRB
TXN
[1,] -0.0354 0.2503 0.0703 0.1539 0.2434 0.1400 -0.0388
> w.gmin.data=solve(var(rtn))%*%rep(1,nrow(cov.r))
> w.gmin.data=w.gmin.data/sum(w.gmin.data)
> t(w.gmin.data)
--- page 501 ---

474
principal component analysis and factor models
AA
AGE
CAT
F
FDX
GM
[1,] -0.0073 -0.0085 0.0866 -0.0232 0.0943 0.0916
HPQ
KMB
MEL
NYT
PG
TRB
TXN
[1,] 0.0345 0.2296 0.0495 0.1790 0.2651 0.0168
-0.0080
Comparing the two GMVPs, the weights assigned to TRB stock differ markedly.
The two portfolios, however, have larger weights for KMB, NYT, and PG stocks.
Finally, we examine the residual covariance and correlation matrices to verify
the assumption that the special factors are not correlated among the 13 stocks. The
ﬁrst four columns of the residual correlation matrix are given below and there exist
some large values in the residual cross correlations, for example, Cor(CAT,AA) =
0.45 and Cor(GM,F) = 0.48.
> resi.cov=t(E.hat)%*%E.hat/(168-2)
> resi.sd=sqrt(diag(resi.cov))
> resi.cor=resi.cov/outer(resi.sd,resi.sd)
> print(resi.cor,digits=1,width=2)
AA
AGE
CAT
F
AA
1.00 -0.13
0.45
0.22
AGE -0.13
1.00 -0.03 -0.01
CAT
0.45 -0.03
1.00
0.23
F
0.22 -0.01
0.23
1.00
FDX
0.00
0.14
0.05
0.07
GM
0.14 -0.09
0.15
0.48
HPQ
0.24 -0.13 -0.07 -0.00
KMB
0.16
0.06
0.18
0.05
MEL -0.02
0.06
0.09
0.10
NYT
0.13
0.10
0.07
0.19
PG -0.15 -0.02 -0.01 -0.07
TRB
0.12 -0.02
0.25
0.16
TXN
0.19 -0.17
0.09 -0.02
9.2.2
Multifactor Models
Chen, Roll, and Ross (1986) consider a multifactor model for stock returns. The factors used consist of unexpected changes or surprises of macroeconomic variables.
Here unexpected changes denote the residuals of the macroeconomic variables after
removing their dynamic dependence. A simple way to obtain unexpected changes
is to ﬁt a VAR model of Chapter 8 to the macroeconomic variables. For illustration,
we consider the following two monthly macroeconomic variables:
1. Consumer price index (CPI) for all urban consumers: all items and with index
1982−1984 = 100.
2. Civilian employment numbers 16 years and over (CE16): measured in thousands.
--- page 502 ---

macroeconometric factor models
475
Both CPI and CE16 series are seasonally adjusted, and the data span is from January
1975 to December 2003. We use a longer period to obtain the surprise series of the
variables. For both series, we construct the growth rate series by taking the ﬁrst
difference of the logged data. The growth rates are in percentages.
To obtain the surprise series, we use the BIC criterion to identify a VAR(3)
model. Thus, the two macroeconomic factors used in the factor model are the
residuals of a VAR(3) model from 1990 to 2003. For the excess returns, we use
the same 13 stocks as before. Details of the analysis follow:
> da=read.table(’m-cpice16-dp7503.txt’),header=T)
> cpi=da[,1]
> cen=da[,2]
> x1=cbind(cpi,cen)
> y1=data.frame(x1)
> ord.choice=VAR(y1,max.ar=13)
> ord.choice$info
ar(1)
ar(2)
ar(3)
ar(4)
ar(5)
ar(6)
BIC
36.992
38.093
28.234
46.241
60.677
75.810
ar(7)
ar(8)
ar(9) ar(10)
ar(11)
ar(12)
ar(13)
BIC
86.23
99.294
111.27 125.46
138.01
146.71
166.92
> var3.fit=VAR(x1~ar(3))
> res=var3.fit$residuals[166:333,1:2]
> da=matrix(scan(file=’m-fac9003.txt’),14)
> xmtx = cbind(rep(1,168),res)
> da=t(da)
> rtn=da[,1:13]
> xit.hat=solve(xmtx,rtn)
> beta.hat=t(xit.hat[2:3,])
> E.hat=rtn - xmtx%*%xit.hat
> D.hat=diag(crossprod(E.hat)/(168-3))
> r.square=1-(168-3)*D.hat/diag(var(rtn,SumSquares=T))
Figure 9.2 shows the bar plots of the beta estimates and R2 for the 13 stocks. It
is interesting to see that all excess returns are negatively related to the unexpected
changes of CPI growth rate. This seems reasonable. However, the R2 of all excess
returns are low, indicating that the two macroeconomic variables used have very
little explanatory power in understanding the excess returns of the 13 stocks.
The estimated covariance and correlation matrices of the two-factor model can
be obtained using the following:
> cov.rtn=beta.hat%*%var(res)%*%t(beta.hat)+diag(D.hat)
> sd.rtn=sqrt(diag(cov.rtn))
> cor.rtn = cov.rtn/outer(sd.rtn,sd.rtn)
> print(cor.rtn,diits=1,width=2)
--- page 503 ---

476
principal component analysis and factor models
−14 −12 −10 −8 −6 −4 −2
0
Beta for CPI surprise
−4
−2
0
2
Beta for CE16 surprise
0.0
0.02
0.04
0.06
R2
AA
AGE
CAT
F
FDX
GM
HPQ
KMB
MEL
NYT
PG
TRB
TXN
Figure 9.2
Bar plots of betas and R2 for ﬁtting two-factor model to monthly excess returns of 13
stocks. Sample period is from January 1990 to December 2003.
The correlation matrix is very close to the identity matrix, indicating that the twofactor model used does not ﬁt the excess returns well. Finally, the correlation matrix
of the residuals of the two-factor model is given by the following:
> cov.resi=t(E.hat)%*%E.hat/(168-3)
> sd.resi=sqrt(diag(cov.resi))
> cor.resi=cov.resi/outer(sd.resi,sd.resi)
> print(cor.resi,digits=1,width=2)
As expected, this correlation matrix is close to that of the original excess returns
given before and is omitted.
9.3
FUNDAMENTAL FACTOR MODELS
Fundamental factor models use observable asset speciﬁc fundamentals such as
industrial classiﬁcation, market capitalization, book value, and style classiﬁcation
(growth or value) to construct common factors that explain the excess returns.
--- page 504 ---

fundamental factor models
477
There are two approaches to fundamental factor models available in the literature.
The ﬁrst approach is proposed by Bar Rosenberg, founder of BARRA Inc., and is
referred to as the BARRA approach; see Grinold and Kahn (2000). In contrast to
the macroeconomic factor models, this approach treats the observed asset speciﬁc
fundamentals as the factor betas, βi, and estimates the factors f t at each time
index t via regression methods. The betas are time invariant, but the realizations
f t evolve over time. The second approach is the Fama–French approach proposed
by Fama and French (1992). In this approach, the factor realization fjt for a given
speciﬁc fundamental is obtained by constructing some hedge portfolio based on
the observed fundamental. We brieﬂy discuss the two approaches in the next two
sections.
9.3.1
BARRA Factor Model
Assume that the excess returns and, hence, the factor realizations are mean corrected. At each time index t, the factor model in Eq. (9.2) reduces to
˜rt = βf t + ϵt,
(9.6)
where ˜rt denotes the (sample) mean-corrected excess returns and, for simplicity in
notation, we continue to use f t as factor realizations. Since β is given, the model
in Eq. (9.6) is a multiple linear regression with k observations and m unknowns.
Because the number of common factors m should be less than the number of
assets k, the regression is estimable. However, the regression is not homogeneous
because the covariance matrix of ϵt is D = diag{σ 2
1 , . . . , σ 2
k } with σ 2
i = Var(ϵit),
which depends on the ith asset. Consequently, the factor realization at time index t
can be estimated by the weighted least-squares (WLS) method using the standard
errors of the speciﬁc factors as the weights. The resulting estimate is
f t =

β′D−1β
−1
β′D−1˜rt

.
(9.7)
In practice, the covariance matrix D is unknown so that we use a two-step procedure
to perform the estimation.
In step one, the ordinary least-squares (OLS) method is used at each time index
t to obtain a preliminary estimate of f t as
f t,o = (β′β)−1(β′˜rt),
where the second subscript o is used to denote the OLS estimate. This estimate of
factor realization is consistent, but not efﬁcient. The residual of the OLS regression is
ϵt,o = ˜rt −βf t,o.
--- page 505 ---

478
principal component analysis and factor models
Since the residual covariance matrix is time invariant, we can pool the residuals
together (for t = 1, . . . , T ) to obtain an estimate of D as

Do = diag

1
T −1
T

t=1
(ϵt,oϵ′
t,o)
+
.
In step two, we plug in the estimate 
Do to obtain a reﬁned estimate of the factor
realization
f t,g =

β′
D
−1
o β
−1 
β′
D
−1
o ˜rt

,
(9.8)
where the second subscript g denotes the generalized least-squares (GLS) estimate, which is a sample version of the WLS estimate. The residual of the reﬁned
regression is
ϵt,g = ˜rt −βf t,g,
from which we estimate the residual variance matrix as

Dg = diag

1
T −1
T

t=1
(ϵt,gϵ′
t,g)
+
.
Finally, the covariance matrix of the estimated factor realizations is
f =
1
T −1
T

t=1
(f t,g −¯f g)(f t,g −¯f g)′,
where
¯f g = 1
T
T

t=1
f t,g.
From Eq. (9.6), the covariance matrix of the excess returns under the BARRA
approach is
Cov(rt) = βf β′ + 
Dg.
Industry Factor Model
For illustration, we consider monthly excess returns of 10 stocks and use
industrial classiﬁcation as the speciﬁc asset fundamental. The stocks used are
given in Table 9.2 and can be classiﬁed into three industrial sectors—namely,
ﬁnancial services, computer and high-tech industry, and other. The sample period
is again from January 1990 to December 2003. Under the BARRA framework,
--- page 506 ---

fundamental factor models
479
TABLE 9.2
Stocks Used and Their Tick Symbols in Analysis of Industrial Factor
Modela
Tick
Company
¯r(σr)
Tick
Company
¯r(σr)
AGE
A.G. Edwards
1.36(10.2)
HPQ
Hewlett-Packard
1.37(11.8)
C
Citigroup
2.08(9.60)
IBM
Int. Bus. Machines
1.06(9.47)
MWD
Morgan Stanley
1.87(11.2)
AA
Alcoa
1.09(9.49)
MER
Merrill Lynch
2.08(10.4)
CAT
Caterpillar
1.23(8.71)
DELL
Dell Inc.
4.82(16.4)
PG
Procter & Gamble
1.08(6.75)
aSample mean and standard deviation of the excess returns are also given. The sample span is from
January 1990 to December 2003.
there are three common factors representing the three industrial sectors and the
betas are indicators for the three industrial sectors; that is,
˜rit = βi1f1t + βi2f2t + βi3f3t + ϵit,
i = 1, . . . , 10,
(9.9)
with the betas being
βij =
 1
if asset i belongs to the j industrial sector,
0
otherwise,
"
(9.10)
where j = 1, 2, 3 representing the ﬁnancial, high-tech, and other sectors, respectively. For instance, the beta vector for the IBM stock return is βi = (0, 1, 0)′ and
that for Alcoa stock return is βi = (0, 0, 1)′.
In Eq. (9.9), f1t is the factor realization of the ﬁnancial services sector, f2t is
that of the computer and high-tech sector, and f3t is for the other sector. Because
the βij are indicator variables, the OLS estimate of f t is extremely simple. Indeed,
f t is the vector consisting of the averages of sector excess returns at time t.
Speciﬁcally,
f t,o =


AGEt+Ct+MDWt+MERt
4
DELLt+HPQt+IBMt
3
AAt+CATt+PGt
3

.
The speciﬁc factor of the ith asset is simply the deviation of its excess return
from its industrial sample average. One can then obtain an estimate of the residual
variance matrix D to perform the generalized least-squares estimation. We use
S-Plus to perform the analysis. The commands also apply to R. First, load the
returns into S-Plus, remove the sample means, create the industrial dummies, and
compute the sample correlation matrix of the returns.
> da=read.table(’m-barra-9003.txt’),header=T)
> rm = matrix(apply(da,2,mean),1)
> rtn = da - matrix(1,168,1)%*%rm
--- page 507 ---

480
principal component analysis and factor models
> fin = c(rep(1,4),rep(0,6))
> tech = c(rep(0,4),rep(1,3),rep(0,3)
> oth = c(rep(0,7),rep(1,3))
> ind.dum = cbind(fin,tech,oth)
> ind.dum
fin tech oth
[1,]
1
0
0
[2,]
1
0
0
[3,]
1
0
0
[4,]
1
0
0
[5,]
0
1
0
[6,]
0
1
0
[7,]
0
1
0
[8,]
0
0
1
[9,]
0
0
1
[10,]
0
0
1
> cov.rtn=var(rtn)
> sd.rtn=sqrt(diag(cov.rtn))
> corr.rtn=cov.rtn/outer(sd.rtn,sd.rtn)
> print(corr.rtn,digits=1,width=2)
AGE
C
MWD MER DELL HPQ IBM AA
CAT PG
AGE
1.0 0.6 0.6 0.6 0.3
0.3 0.3 0.3 0.3 0.2
C
0.6 1.0 0.7 0.7 0.2
0.4 0.4 0.4 0.4 0.3
MWD
0.6 0.7 1.0 0.8 0.3
0.5 0.4 0.4 0.3 0.3
MER
0.6 0.7 0.8 1.0 0.2
0.5 0.3 0.4 0.3 0.3
DELL 0.3 0.2 0.3 0.2 1.0
0.5 0.4 0.3 0.1 0.1
HPQ
0.3 0.4 0.5 0.5 0.4
1.0 0.5 0.5 0.2 0.1
IBM
0.3 0.4 0.4 0.3 0.4
0.5 1.0 0.4 0.3-0.0
AA
0.3 0.4 0.4 0.4 0.3
0.5 0.4 1.0 0.6 0.1
CAT
0.3 0.4 0.3 0.3 0.1
0.2 0.3 0.6 1.0 0.1
PG
0.2 0.3 0.3 0.3 0.1
0.1-0.0 0.1 0.1 1.0
The OLS estimates, their residuals, and residual variances are estimated as follows:
> F.hat.o = solve(crossprod(ind.dum))%*%t(ind.dum)%*%rtn.rm
> E.hat.o = rtn.rm - ind.dum%*%F.hat.o
> diagD.hat.o=rowVars(E.hat.o)
One can then obtain the generalized least-squares estimates.
> Dinv.hat = diag(diagD.hat.o^(-1))
> Hmtx=solve(t(ind.dum)%*%Dinv.hat%*%ind.dum)%*%t(ind.dum)
%*%Dinv.hat
> F.hat.g = Hmtx%*%rtn.rm
> F.hat.gt=t(F.hat.g)
> E.hat.g = rtn.rm - ind.dum%*%F.hat.g
> diagD.hat.g = rowVars(E.hat.g)
> t(Hmtx)
--- page 508 ---

fundamental factor models
481
fin
tech
oth
[1,]
0.1870
0.0000
0.0000
[2,]
0.2548
0.0000
0.0000
[3,]
0.2586
0.0000
0.0000
[4,]
0.2995
0.0000
0.0000
[5,]
0.0000
0.2272
0.0000
[6,]
0.0000
0.4015
0.0000
[7,]
0.0000
0.3713
0.0000
[8,]
0.0000
0.0000
0.3319
[9,]
0.0000
0.0000
0.4321
[10,]
0.0000
0.0000
0.2360
> cov.ind=ind.dum%*%var(F.hat.gt)%*%t(ind.dum)
+ diag(diagD.hat.g)
> sd.ind=sqrt(diag(cov.ind))
> corr.ind=cov.ind/outer(sd.ind,sd.ind)
> print(corr.ind,digits=1,width=2)
AGE C
MWD MER DELL HPQ IBM AA
CAT PG
AGE
1.0 0.7 0.7 0.7 0.3
0.3 0.3 0.3 0.3 0.3
C
0.7 1.0 0.8 0.8 0.3
0.4 0.4 0.3 0.3 0.3
MWD
0.7 0.8 1.0 0.8 0.3
0.4 0.4 0.3 0.4 0.3
MER
0.7 0.8 0.8 1.0 0.3
0.4 0.4 0.3 0.4 0.3
DELL 0.3 0.3 0.3 0.3 1.0
0.5 0.5 0.2 0.2 0.2
HPQ
0.3 0.4 0.4 0.4 0.5
1.0 0.7 0.3 0.3 0.2
IBM
0.3 0.4 0.4 0.4 0.5
0.7 1.0 0.3 0.3 0.2
AA
0.3 0.3 0.3 0.3 0.2
0.3 0.3 1.0 0.7 0.5
CAT
0.3 0.3 0.4 0.4 0.2
0.3 0.3 0.7 1.0 0.6
PG
0.3 0.3 0.3 0.3 0.2
0.2 0.2 0.5 0.6 1.0
The model-based correlations of stocks within an industrial sector are larger
than their sample counterparts. For instance, the sample correlation between CAT
and PG stock returns is only 0.1, but the correlation based on the ﬁtted model is
0.6. Finally, Figure 9.3 shows the time plots of the factor realizations based on the
generalized least-squares estimation.
Factor Mimicking Portfolio
Consider the special case of BARRA factor models with a single factor. Here the
WLS estimate of ft in Eq. (9.7) has a nice interpretation. Consider a portfolio
ω = (ω1, . . . , ωk)′ of the k assets that solves
min
ω ( 1
2ω′Dω)
such that
ω′β = 1.
It turns out that the solution to this portfolio problem is given by
ω′ = (β′D−1β)−1(β′D−1).
Thus, the estimated factor realization is the portfolio return
ˆft = ω′rt.
--- page 509 ---

482
principal component analysis and factor models
Year
(a)
Factor
1990
1992
1994
1996
1998
2000
2002
2004
Year
(b)
1990
1992
1994
1996
1998
2000
2002
2004
Year
(c)
1990
1992
1994
1996
1998
2000
2002
2004
−20
0
20
Factor
−20 0
20
Factor
−20 0
20
Figure 9.3
Estimated factor realizations of BARRA industrial factor model for 10 monthly stock
returns in 3 industrial sectors: (a) factor realizations: ﬁnancial sector, (b) high-tech sector, and (c) other
sector.
If the portfolio ω is normalized such that k
i=1 ωi = 1, it is referred to as a factor
mimicking portfolio. For multiple factors, one can apply the idea to each factor
individually.
Remark.
In practice, the sample mean of an excess return is often not significantly different from zero. Thus, one may not need to remove the sample mean
before ﬁtting a BARRA factor model.
□
9.3.2
Fama–French Approach
For a given asset fundamental (e.g., ratio of book-to-market value), Fama and
French (1992) determined factor realizations using a two-step procedure. First, they
sorted the assets based on the values of the observed fundamental. Then they formed
a hedge portfolio, which is long in the top quintile ( 1
3) of the sorted assets and
short in the bottom quintile of the sorted assets. The observed return on this hedge
portfolio at time t is the observed factor realization for the given asset fundamental.
--- page 510 ---

principal component analysis
483
The procedure is repeated for each asset fundamental under consideration. Finally,
given the observed factor realizations {f t|t = 1, . . . , T }, the betas for each asset
are estimated using a time series regression method. These authors identify three
observed fundamentals that explain high percentages of variability in excess returns.
The three fundamentals used by Fama and French are (a) the overall market return
(market excess return), (b) the performance of small stocks relative to large stocks
(SMB, small minus big), and (c) the performance of value stocks relative to growth
stocks (HML, high minus low). The size sorted by market equity and the ratio of
book equity to market equity is used to deﬁne value and growth stocks with value
stocks having high book equity to market equity ratio.
Remark.
The concepts of factor may differ between factor models. The three
factors used in the Fama–French approach are three ﬁnancial fundamentals. One
can combine the fundamentals to create a new attribute of the stocks and refer to the
resulting model as a single-factor model. This is particularly so because the model
used is a linear statistical model. Thus, care must be exercised when one refers to
the number of factors in a factor model. On the other hand, the number of factors
is more well deﬁned in statistical factor models, which we discuss next.
□
9.4
PRINCIPAL COMPONENT ANALYSIS
An important topic in multivariate time series analysis is the study of the covariance
(or correlation) structure of the series. For example, the covariance structure of a
vector return series plays an important role in portfolio selection. In what follows,
we discuss some statistical methods useful in studying the covariance structure of
a vector time series.
Given a k-dimensional random variable r = (r1, . . . , rk)′ with covariance matrix
r, a principal component analysis (PCA) is concerned with using a few linear
combinations of ri to explain the structure of r. If r denotes the monthly log
returns of k assets, then PCA can be used to study the main source of variations
of these k asset returns. Here the keyword is few so that simpliﬁcation can be
achieved in multivariate analysis.
9.4.1
Theory of PCA
Principal component analysis applies to either the covariance matrix r or the
correlation matrix ρr of r. Since the correlation matrix is the covariance matrix
of the standardized random vector r∗= S−1r, where S is the diagonal matrix
of standard deviations of the components of r, we use covariance matrix in our
theoretical discussion. Let wi = (wi1, . . . , wik)′ be a k-dimensional real-valued
vector, where i = 1, . . . , k. Then
yi = w′
ir =
k

j=1
wijrj
--- page 511 ---

484
principal component analysis and factor models
is a linear combination of the random vector r. If r consists of the simple returns
of k stocks, then yi is the return of a portfolio that assigns weight wij to the
jth stock. Since multiplying a constant to wi does not affect the proportion
of allocation assigned to the jth stock, we standardize the vector wi so that
w′
iwi=k
j=1 w2
ij = 1.
Using properties of a linear combination of random variables, we have
Var(yi) = w′
irwi,
i = 1, . . . , k,
(9.11)
Cov(yi, yj) = w′
irwj,
i, j = 1, . . . , k.
(9.12)
The idea of PCA is to ﬁnd linear combinations wi such that yi and yj are uncorrelated for i̸ = j and the variances of yi are as large as possible. More speciﬁcally:
1. The ﬁrst principal component of r is the linear combination y1 = w′
1r that
maximizes Var(y1) subject to the constraint w′
1w1 = 1.
2. The second principal component of r is the linear combination y2 = w′
2r
that maximizes Var(y2) subject to the constraints w′
2w2 = 1 and Cov(y2, y1)
= 0.
3. The ith principal component of r is the linear combination yi = w′
ir that
maximizes Var(yi) subject to the constraints w′
iwi = 1 and Cov(yi, yj) = 0
for j = 1, . . . , i −1.
Since the covariance matrix r is nonnegative deﬁnite, it has a spectral
decomposition; see Appendix A of Chapter 8. Let (λ1, e1), . . ., (λk, ek) be
the eigenvalue–eigenvector pairs of r, where λ1 ≥λ2 ≥· · · ≥λk ≥0 and
ei = (ei1, . . . , eik)′, which is properly normalized. We have the following
statistical result.
Result 9.1. The ith principal component of r is yi = e′
ir = k
j=1 eijrj for
i = 1, . . . , k. Moreover,
Var(yi) = e′
irei = λi,
i = 1, . . . , k,
Cov(yi, yj) = e′
irej = 0,
i̸ = j.
If some eigenvalues λi are equal, the choices of the corresponding eigenvectors ei
and hence yi are not unique. In addition, we have
k

i=1
Var(ri) = tr(r) =
k

i=1
λi =
k

i=1
Var(yi).
(9.13)
The result of Eq. (9.13) says that
Var(yi)
k
i=1 Var(ri)
=
λi
λ1 + · · · + λk
.
--- page 512 ---

principal component analysis
485
Consequently, the proportion of total variance in r explained by the ith principal component is simply the ratio between the ith eigenvalue and the sum of all
eigenvalues of r. One can also compute the cumulative proportion of total variance explained by the ﬁrst i principal components [i.e., (i
j=1 λj)/(k
j=1 λj)].
In practice, one selects a small i such that the resulting cumulative proportion is
large.
Since tr(ρr) = k, the proportion of variance explained by the ith principal
component becomes λi/k when the correlation matrix is used to perform the PCA.
A by-product of the PCA is that a zero eigenvalue of r, or ρr, indicates the
existence of an exact linear relationship between the components of r. For instance,
if the smallest eigenvalue λk = 0, then by Result 9.1 Var(yk) = 0. Therefore, yk =
k
j=1 ekjrj is a constant and there are only k −1 random quantities in r. In this
case, the dimension of r can be reduced. For this reason, PCA has been used in
the literature as a tool for dimension reduction.
9.4.2
Empirical PCA
In application, the covariance matrix r and the correlation matrix ρr of the return
vector r are unknown, but they can be estimated consistently by the sample covariance and correlation matrices under some regularity conditions. Assuming that the
returns are weakly stationary and the data consist of {rt|t = 1, . . . , T }, we have
the following estimates:
r ≡[ˆσij,r] =
1
T −1
T

t=1
(rt −¯r)(rt −¯r)′,
¯r = 1
T
T

t=1
rt,
(9.14)
ρr = S
−1rS
−1,
(9.15)
where S = diag{

ˆσ11,r, . . . ,

ˆσkk,r} is the diagonal matrix of sample standard
errors of rt. Methods to compute eigenvalues and eigenvectors of a symmetric
matrix can then be used to perform the PCA. Most statistical packages now have
the capability to perform principal component analysis. In R and S-Plus, the basic
command of PCA is princomp, and in FinMetrics the command is mfactor.
Example 9.1.
Consider the monthly log stock returns of International Business
Machines, Hewlett-Packard, Intel Corporation, J.P. Morgan Chase, and Bank of
America from January 1990 to December 2008. The returns are in percentages and
include dividends. The data set has 228 observations. Figure 9.4 shows the time
plots of these ﬁve monthly return series. As expected, returns of companies in the
same industrial sector tend to exhibit similar patterns.
Denote the returns by r′ = (IBM, HPQ, INTC, JPM, BAC). The sample mean
vector of the returns is (0.70, 0.99, 1.20, 0.82, 0.41)′ and the sample covariance
and correlation matrices are
--- page 513 ---

486
principal component analysis and factor models
Year
(a)
Returns
Returns
Returns
Returns
Returns
1990
1995
2000
2005
−30−10 10 30
−40−20 0 20
−60 −200 20
−40−20 0 20
−40
0 20
Year
(b)
1990
1995
2000
2005
Year
(c)
1990
1995
2000
2005
Year
(d)
1990
1995
2000
2005
Year
(e)
1990
1995
2000
2005
Figure 9.4
Time plots of monthly log stock returns in percentages and including dividends for (a)
International Business Machines, (b) Hewlett-Packard, (c) Intel, (d) J.P. Morgan Chase, and (e) Bank
of America from January 1990 to December 2008.
r =


74.64
42.28
112.22
48.03
70.45
146.50
30.10
42.42
44.59
106.04
21.07
26.30
29.24
67.45
91.83


,
ρr =


1.00
0.46
1.00
0.46
0.55
1.00
0.34
0.39
0.36
1.00
0.25
0.26
0.25
0.68
1.00


.
Table 9.3 gives the results of PCA using both the covariance and correlation
matrices. Also given are eigenvalues, eigenvectors, and proportions of variabilities
--- page 514 ---

principal component analysis
487
TABLE 9.3
Results of Principal Component Analysis for Monthly Log Returns,
Including Dividends of Stocks of IBM, Hewlett-Packard, Intel, J.P. Morgan Chase,
and Bank of America from January 1990 to December 2008a
Using Sample Covariance Matrix
Eigenvalue
284.17
112.93
57.43
46.81
29.87
Proportion
0.535
0.213
0.108
0.088
0.056
Cumulative
0.535
0.748
0.856
0.944
1.000
Eigenvector
0.330
0.139
−0.264
0.895
−0.014
0.483
0.279
−0.701
−0.430
−0.116
0.581
0.478
0.652
−0.096
−0.016
0.448
−0.550
0.013
−0.064
0.702
0.347
−0.610
0.119
−0.009
−0.702
Using Sample Correlation Matrix
Eigenvalue
2.607
1.072
0.569
0.451
0.301
Proportion
0.522
0.214
0.114
0.090
0.060
Cumulative
0.522
0.736
0.850
0.940
1.000
Eigenvector
0.428
0.341
0.837
−0.002
0.008
0.460
0.356
−0.380
0.704
0.145
0.451
0.385
−0.389
−0.704
0.022
0.479
−0.469
−0.046
0.052
−0.739
0.416
−0.623
0.035
−0.073
0.658
aThe eigenvectors are in columns.
explained by the principal components. Consider the correlation matrix and denote
the sample eigenvalues and eigenvectors by ˆλi and ei. We have
ˆλ1 = 2.608,
e1 = (0.428, 0.460, 0.451, 0.479, 0.416)′,
ˆλ2 = 1.072,
e2 = (0.341, 0.356, 0.385, −0.469, −0.623)′
for the ﬁrst two principal components. These two components explain about 74%
of the total variability of the data, and they have interesting interpretations. The ﬁrst
component is a roughly equally weighted linear combination of the stock returns.
This component might represent the general movement of the stock market and
hence is a market component. The second component represents the difference
between the two industrial sectors—namely, technologies versus ﬁnancial services.
It might be an industrial component. Similar interpretations of principal components
can also be found by using the covariance matrix of r.
An informal but useful procedure to determine the number of principal components needed in an application is to examine the scree plot, which is the time plot of
the eigenvalues ˆλi ordered from the largest to the smallest (i.e., a plot of ˆλi versus
i). Figure 9.5(a) shows the scree plot for the ﬁve stock returns of Example 9.1. By
looking for an elbow in the scree plot, indicating that the remaining eigenvalues
