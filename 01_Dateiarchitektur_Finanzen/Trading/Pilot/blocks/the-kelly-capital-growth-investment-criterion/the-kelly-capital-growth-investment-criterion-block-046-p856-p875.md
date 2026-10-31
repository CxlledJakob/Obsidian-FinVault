# The Kelly capital growth investment criterion _ theory and -- Leonard C_ Maclean, Edward O_ Thorp, W_ T_ Ziemba, Leonard -- World Scientific Handbook -- isbn13 9781283148344 -- bec576e26410d0c695fd5b867d08ec4f -- An.pdf — pages 856–875

--- page 856 ---

The Kelly Criterion in Blackjack Sports Betting, and the Stock Market
827
Ch. 9:
The Kelly Criterion in Blackjack Sports Betting, and the Stock Market
423
p(x(t) :( at + b, 0 :( t :( T) = 1 -
PC) = N(a + fJ) - e- 2afJ N(a -
fJ)
for the probability the line is never surpassed. This follows from:
_1_1 00 e-·\·2j2T ds = _1_1 00
e-x2j2 dx = N( -a -
fJ )
.J2rrT aT+b
~
a./f+bj./f
--
eu-j2T du = N(a -
fJ)
1
j aT-b
?
.J2rrT
- 00
where s = aT + b, x = s / .JT = a.JT + b/ .JT, a = a.JT and fJ = b/ .JT.
The formula becomes:
p(sup[X(t) - (at + b)] ~ 0: 0 :( t :( T)
= N(-a -
fJ) + e- 2a/J N(a -
fJ)
= N(-a -
fJ) + e- 2afJ N(a -
fJ),
a , fJ > O.
Observe that
PC) < N(-a - m + N(a -
fJ) = {I - N(a +fJ)} + N(a -
fJ)
= jafJ a(x) dx + 1
00 a(x) dx < I
-00
a+fJ
as it should be.
Appendix C. Expected time to reach goal
and
Reference: Handbook of Mathematical Functions, Abramowitz and Stegun, Editors,
N.B.S. Applied Math. Series 55, June 1964.
P. 304, 7.4.33 gives with erf z == Jrr f~ er2 dt the integral:
f exp{ _(a 2 x2 + b2 /x2) } dx
= :- [e2a!Jerf(ax + b/x) + e- 211 !J erf(ax - b/x)] + C,
a i- O.
(C.l)
Now the left side is > 0 so for real a, we require a > 0 otherwise the right side is < 0,
a contradiction.
We also note that p. 302, 7.4.3. gives
roo exp{ -(at2 + b/ t 2)} dt = ~ ~e-2~
10
2V~
(C.2)
with ma > 0, mb > O.
--- page 857 ---

828
E. 0. Thorp
424
E.O. Thorp
To check (C.2) v. (C.l), suppose in (C.l) a > 0, b > 0 and find Iimx -> o and limt->oo
of erf(ax + b/x) and erf(ax - b/x),
lim (ax + b/x) = +00,
x.j.o+
lim (ax + b/ x) = +00,
. .\' ----7 00
Equation (C.l) becomes
lim (ax - b/x) = -00,
x.j.o+
lim (ax - b/x) = +00 .
x ---+oo
-Jii e-2al> [erf(oo) _ erf(-oo)] = -Jii e- 2ab2erf(00) = -Jii e- 2ab
4a
4a
2a
since we know erf( 00) = 1.
In (C.2) replace a by a2 , b by b2 to get
which is the same.
Note: if we choose the lower limit of integration to be 0 in (C. I), then we can find C:
0+
-Jii
0= [
exp{ _(a2x 2 + b2 /x2)} dx = -[
e2al>erf(00) + e- 2ah erf( -00)] + C
10
4a
= -Jii [e2al> _ e-211h ] + c.
4a
Whence
F(x) == fox exp{ _(a2x 2 + b2 / x2)} dx
= -Jii (e2"j,[erf(ax + b/x) -
I] + e- 211 j,[erf(ax - b/x) + I]}.
(C.3)
4a
To see how (C.3) might have been discovered, differentiate:
F'(x) = exp{-(a2x 2 +b2/x2)}
= -Jii {e211h (a _ b/x2) erf'(ax + b/ x)
4a
+ e- 211h (a + b/x2) erf'(ax - b/x)}.
Now erf' (z) = Jrr exp( - Z2) so
2
2
erf'(ax+b/ x) = -Jiiexp[-(ax+b/x)2] = -Jiiexp{-(a2x2+b2/x2+2ab)}
2
= -Jiie- 2a/J exp{ _(a2x 2 + b2 /x2)} ,
--- page 858 ---

The Kelly Criterion in Blackjack Sports Betting, and the Stock Market
Ch. 9:
The Kelly Criterion in Blackjack Sports Betting, and the Stock Market
and, setting b +- -b,
whence
F'(x) = :
{]rr(a - b/x2) + ]rr(a + b/x2)} exp{ _(a2x 2 + b2 /x2)}
= ~{2a} exp{ _(a2 x2 + b2 /x2)} = exp{ _(a2x2 + b2 /x2)} .
2a
Case of interest: a < 0, b > O.
Expect:
b > 0, a ::;; 0
::::}
F(T) t I as T -+ 00,
b> 0, a > 0
::::}
F(T) t c < 1 as T -+ 00.
If b > 0, a = 0:
F(T) = N(-f3) + N(-fi) = 2N(-b/.Jf) t 2N(0) = 1 as T t 00.
Also, as expected F(T) t I as h ~ O.
If b > 0, a < 0: See below.
If b > 0, a > 0:
F(T) = N(-afl - h/fl) +e-2abN(a.Jf -b/.Jf)
-+ N(-oo) +c 211i>N(00)
= e--2,,/! < I
as T i 00.
This is correct.
If b .= 0: F(T) = N (-(/ Jf) + N(a~) = l. This is correct.
829
425
Let F(T) = P(X (I) ;? (/1 + h for some t, 0 ::;; t ::;; T) which equals N( -a -
f3) +
e-2ab N(a -
f3) where a = (/ Jf and fi = b/~ so ab = af3; we assume b > 0 and
a < 0 in which case 0 ::;; F( T)' I and limT -+00 F(T) = I, limT -+0 F(T) = 0; F is a
probability distribution funct illll:
lim F(T) = N( -(0) + c 2,,/, N ( - 00) = 0,
T-+O
lim F(T)=N(+oo)+c 211"N(_00)=l.
T-+oo
The density function is
a
a
nn = P'(T) = -(-a -/l)N'( - a -
f3) +e-211"_(a - f3)N'(a -
f3)
.
aT
aT
where
il( y
I IIF
1/ 2
Afi
I ..
_
= _ __ hl
l / 2
;IF
1
aT
:2
--- page 859 ---

830
E. O. Thorp
426
E.O. Thorp
The expected time to the goal is
Eoo =
Tf(T) dT = -- '
T - I / 2 exp
dT,
1
00
be- IIh 100
{
(a 2T + b2/T) }
o
~
0
2
= x
2b -lIh
00
2
l
2
2
e
a
2
')
- 2
T I / 2
1
T - x
-
-
-
exp -
-
x + -
x
dx
dT -= 2x dx
- ~ 1 {[ (~)
(~) ] }
Now
I (a 2 b2 ) = jJi e- 2111iJI
so
0
,
21al
lo( (~r, (~r) = :'Ie-I"hl
whence
2b -IIi,
~
l
e
yJr
- llIhl
')
Eoo = -- ~-e
= -
a < 0, b > O.
~
~Ial
lal '
Note:
f(T)=F'(T)= -- T - 3/ 2 exp -
> 0
be-IIh
{
(a2T + b2/ T) }
~
2
for all a, e.g., a < 0, so F(T) is monotone increasing. Hence, since IimT--.oo F(T) = 1
for a < 0 and limr--.oo F(T) < I for a > 0,0 :::;; F(T) :::;; I for all T so we have more
--- page 860 ---

The Kelly Criterion in Blackjack Sports Betting, and the Stock Market
Ch. 9:
Th e Kelly Criterion in Blackjack Sports Belling, and the Stock Market
confidence in using the formula for a < 0 too.
Check:
Eoo(a , b) -I- 0 as -I- -00 yes,
Eoo(a, b) t as b t
yes,
Eoo (a , b) t aslal -Iyes,
note
lim Eoo(a, b) = +00
as suspected.
a~O+
831
427
This leads us to believe that in a fair coin toss (fair means no drift) and a gambler
with finite capital, the expected time to ruin is infinite.
This is correct. Feller gives D = z(a - z) as the duration of the game, where z is
initial capital, ruin is at 0, and (/ is the goal. Then lim,,->oo D(a) = +00.
Note: Eoo = b/lal means the expected time is the same as the point where aT + b
crosses X(t) = O. See Figure 2.
so
Eoo = h/lal ,
(/ = _ 111/.1'",
h = InA,
A = C/ Xo = normali/.ed goal.
m = p In(1 + fl + £I IIl( I - n == g(f),
s2 = pq{ln[(l + fl /( 1 - n1l 2,
Kelly fraction f* = p -
£f .
g(f*) = p In2p + q In2q,
Form> 0,
Eoo = (InA).I'2/g (f).
Now this is the expected time in variance units. However s2 variance units = 1 trial
Eoo
InA
InA
n(A , f) == ~
= g(f) = --;;;
is the expected number of trials.
Chcck:
I/(A , f) t
as A t ,
II (A , f) ---+ 00
as A ---+ 00,
II (A , f) t
as m -I- 0,
II(A, f) ---+ 00
as m ---+ O.
N(I\\ t:1 I ) it;IS uilique maximum at g(f*) where f* = p - q, the "Kelly fraction",
thcn'l, II,' 1111 , I) has a unique minimum for f = f*, Hence f* reaches a fixed goal in
leas I ("I"',It'lIIIlIlC in this, the continuous case, so we must be asymptotically close to
l e a~1 ( "
IIt" !t." 1111lL' ill the discrete case, which this approximates increasing by well in
thl' "('II',,' .. I I h,' ( 'I T (Central Limit Theorem) and its special case, the normal approxill);11 It III I .. 1111' hlllol11ial distribution, The difference here is the trials are asymmetric.
Till' 1"1',111\ " ,lIltllll'galive step sizes are unequal.
--- page 861 ---

832
E. 0. Thorp
428
£.0. Thorp
References
Associates First Capital Corporation, 1998. 1997 Annual Report. Associates First Capital Corporation, Dallas,
TX.
Black, E, Scholes, M., 1973. The pricing of options and corporate liabilities. Journal of Political Economy 81,
637-659.
Breiman, L., 1961 . Optimal gambling systems for favorable games. In: Fourth Berkeley Symposium on Probability and Statistics, vol. 1, pp. 65-78.
Browne, S., 1996. Reaching Goals by a Deadline: Continuous-Time Active Portfolio Management. Columbia
University, New York.
Browne, S., 1997. The return on investment from proportional investment strategies. Advances in Applied
Probability 30 (I), 216-238.
Buffett. M., Clark. D. , 1997. Buffettology. Rawson Associates, Simon and Schuster, New York.
Cox, D.R., Miller, H.D., 1965. The Theory of Stochastic Processes. Wiley, New York.
Feller, w., 1966. An Introduction to Probability Theory and Its Applications, vol. I, Revised. Wiley, New
York.
Griffin, P.A., 1979. The Theory of Blackjack. Huntington Press, Las Vegas. Revised 1995.
Hagstrom, R.G. Jr., 1994. The Warren Buffett Way. Wiley, New York.
Hagstrom, R.G. Jr., 2004. The Warren Buffett Way, second ed. Wiley, New York.
Hecht, R., 1995. Private correspondence.
Ibbotson Associates, 1998. Yearbook: Stocks, Bonds, Bills and Inflation (or any later edition). Ibbotson Associates, Chicago.
Institutional Investor, 1998. Ivory Tower Investing, pp. 43-55 (see p. 44), March.
Kelly, J.L., 1956. A new interpretation of information rate. Bell System Technical Journal 35, 917-926.
Kilpatrick, A., 1994. Of Permanent Value, the Story of Warren Buffet. Distributed by Southern Publishers
Group, Birmingham, AL.
Kritzman, M., 1998. Risk and utility: basics. In: Bernstein, Damodaran (Eds.), Investment Management. Wiley, New York. Chapter 2.
Lowenstein, R., 1995. The Making of an American Capitalist. Random House, New York.
Markowitz, H., 1959. Portfolio Selection. Cowles Monograph, vol. 16. Wiley, New York.
McEnally, R.W., 1986. Latane's bequest: the best of portfolio strategies. Journal of Portfolio Management 12
(2),21-30, Winter.
Quaife, A., 1995. Using the Sharpe ratio to evaluate investments. The Trans Times 4 (1), February. Trans
Time Inc., Oakland, CA.
Rotando, L.M., Thorp, E.O., 1992. The Kelly criterion and the stock market. American Mathematical
Monthly 99, 922-931, December.
Thorp, E.O., 1962. Beat the Dealer. Random House, New York.
Thorp, E.O., 1966. Beat the Dealer, second ed. Vintage. New York.
Thorp, E.O., 1969. Optimal gambling systems for favorable games. Review of the International Statistical
Institute 37, 273-293.
Thorp, E.O., 1971. Portfolio choice and the Kelly criterion. In: Proceedings of the 1971 Business and Economics Section of the American Statistical Association, pp. 215-224.
Thorp, E.O., 1984. The Mathematics of Gambling. Lyle Stuart, Secaucus, NJ.
Thorp, E.O., Kassouf, S.T., 1967. Beat the Market. Random House, New York.
Thorp, E.O., Walden, w., 1966. A winning bet in Nevada baccarat, part 1. Journal of the American Statistical
Association 61, 313-328.
Tucker, H., 1967. A Graduate Course in Probability. Academic Press, San Diego, CA.
Wong, S., 1994. Professional Blackjack. Pi Yee Press, La Jolla, CA.
--- page 862 ---

833
Bibliography
Aase, K. K. (2001). On the St. Petersburg Paradox. Scandinavian Actuarial Journal, 3(1),
69- 78.
Algoet, P. H. and T. M. Cover (1988). Asymptotic optimality and asymptotic equipartition
properties of log-optimum investment. Annals of Probability, 16(2), 876- 898.
Aucamp, D. (1977). An investment strategy with overshoot rebates which minimizes the
time to attain a specified goal. Management Science, 23(11) , 1234-1241.
Aucamp, D. (1993). On the extensive number of plays to achieve superior performance
with the geometric mean strategy. Management Science, 39, 1163- 1172.
Barron, A. R. and T. M. Cover (1988). A bound on the financial value of information.
IEEE Transactions of Information Theory, 34(5), 1097- 1100.
Bell, R. M. and T. M. Cover (1980). Competitive optimality of logarithmic investment.
Math of Operations Research, 5, 161- 166.
Bell, R. M. and T. M. Cover (1988). Game-theoretic optimal portfolios. Management
Science, 34(6), 724- 733.
Bellman, R. and R. Kalaba (1957). On the role of dynamic programming in statistical
communication theory. IRE Transactions of the Professional Group on Information
Theory, IT, 3(3), 197- 203.
Bernoulli, D. (1954). Exposition of a new theory on the measurement of risk (translated
by Louise Sommer). Econometrica, 22, 23- 36.
Bicksler, J. L. and E. O. Thorp (1973). The capital growth model: An empirical investigation. Journal of Financial and Quantitative Analysis, 8(2), 273- 287.
Breiman, L. (1960). Investment policies for expanding businesses optimal in a long run
sense. Naval Research Logistics Querterly, 4(4) , 647- 651.
Breiman, L. (1961). Optimal gambling system for favorable games. Proceedings of the 4th
Berkeley Symposium on Mathematical Statistics and Probability, 1, 63- 8.
Browne, S. (1997). Survival and growth with a liability: Optimal portfolios in continuous
time. Math of Operations Research, 22, 468- 493.
Browne, S. (2000). Risk-constrained dynamic active portfolio management. Management
Science, 46(9),1188- 1199.
Chapman, S. J. (2007). The Kelly criterion for spread bets. IMA Journal of Applied Mathematics, 72, 43- 51.
Chopra, V. K. and W. T. Ziemba (1993). The effect of errors in means, variances and covariances on optimal portfolio choice. Journal of Portfolio Management, 19, 6- 11.
Christensen, M. M. (2005). On the history of the growth optimal portfolio. Working Paper,
University of South Denmark.
Clark, R. and W. T. Ziemba (1987). Playing the t urn-of-the-year effect with index futures.
Operations Research, 35, 799- 813.
Cover, T. M. (1984). An algorithm for maximizing expected log investment return. IEEE
Transactions on Information Theory, 30(2), 369- 373.
Cover, T. M. (1987). Log optimal portfolios. In W. Eadington (Ed.) , Research: Gambling
and Risk Taking, Seventh International Conference, Vol 4: Quantitative Analysis
and Gambling, Reno, NV.
--- page 863 ---

834
Bibliography
Cover, T. M. (1991). Universal portfolios. Math Finance, 1, 1- 29.
Cover, T. M. and D. H. Gluss (19S6). Empirical Bayes stock market portfolios. Advances
in Applied Mathematics, 7, 170- 1S1.
Cover, T. M. and E. Ordentlich (1996). Universal portfolios with side information. IEEE
Transactions on Information Theory, 42(2) , 34S- 363.
Cover, T. M. and J. Thomas (2006). Elements of Information Theory, 2nd Edition. New
York: John Wiley & Sons.
Davis, M. and S. Lleo (2010). On benchmarks and fractional Kelly strategies.
Davis, M. H. A. and S. Lleo (200Sa). A risk sensitive asset and liability management model.
Working Paper.
Davis, M. H. A. and S. Lleo (200Sb). Risk-sensitive benchmarked asset management.
Quantitative Finance, S(4), 415426.
Dempster, M. A. H. , I. V. Evstigneev, and K. R. Schenk-Hoppe (2003). Exponential growth
of fixed mix assets in stationary markets. Finance and Stochastics, 7(2) , 263- 276.
Dempster, M. A. H. , I. V. Evstigneev, and K. R. Schenk-Hoppe (2007). Volatility-induced
financial growth. Quantitative Finance, 7(2) , 151- 160.
Dempster, M. A. H., I. V. Evstigneev, and K. R. Schenk-Hoppe (2010). Gaining wealth
with fixed-mix strategies.
Dubins, L. and L. Savage (1965). How to Gamble If You Must. New York: McGraw-Hill.
Epstein, R. A. (1977). The Theory of Gambling and Statistical Logic. London: Academic
Press.
Erkip, E. and T . M. Cover (199S). The efficiency of investment information. IEEE Transactions on Information Theory, 4(3), 1026- 1040.
Ethier, S. and N. Tavare (19S3). The proportional bettor's return on investment. Journal
of Applied Probability, 20, 563-573.
Ethier, S. N. (2004). The Kelly system maximizes median wealth. Journal of Applied
Probability, 41(4), 1230-1236.
Evstigneev, I. V., T . Hens, and K. R. Schenk-Hoppe (200S). Globally evolutionarily stable
portfolio rules. Journal of Economic Theory, 140, 197- 22S.
Evstigneev, I. V., T. Hens, and K. R. Schenk-Hoppe (2010). Survival and evolutionary
stability of the Kelly rule.
Feller, W. (1962). An Introduction to Probability Theory and Its Applications (2 ed.). New
York: John Wiley & Sons.
Ferguson, T . S. (1965). Betting systems which minimize the probability of ruin. Journal
of the Society for Industrial and Applied Mathematics, 13(3), 795- S1S.
Fernholz, R. and B. Shay (19S2). Stochastic portfolio theory and stock market equilibrium.
Journal of Finance, 37, 615- 624.
Finkelstein, M. and R. Whitley (19S1). Optimal strategies for repeated games. Advanced
Applied Probability, 13, 415-42S.
Fitt, A. D. , C. J. Howls, and M. Kabelka (2006). The valuation of soccer spread bets.
Journal of the Operational Research Society, 77, 975- 9S5.
Fuller, J. (2006). Optimize your portfolio with the Kelly formula. www.morningstar.com.
October 6.
Geyer, A. and W. T. Ziemba (200S). The Innovest Austrian pension fund planning model
InnoALM. Operations Research, 56(4) , 797-SlO.
Goldman, M. B. (1974). A negative report on the "near optimality" of the max-expected log
policy and appled to bounded utilities for long-lived programs. Journal of Financial
Economics, 1, 97- 103.
Gottlieb, G. (19S4). An optimal betting strategy for repeated games. Working paper, New
York University.
2
--- page 864 ---

Bibliography
835
Gottlieb, G. (1985). An analytic derivation of blackjack win rates. Operations Research,
33, 971- 988.
Grauer, R. R. and N. H. Hakansson (1986). A half century of returns on levered and
unlevered portfolios of stocks, bonds and bills, with and without small stocks. Journal
of Business, 592, 287- 318.
Haigh, J . The Kelly criterion and bet comparisons in spread betting. Statistician, 49,
531-539.
Hakansson, N. (1970). Optimal investment and consumption strategies under risk for a
class of utility functions. Econometrica, 38, 587-607.
Hakansson, N. H. (1971). On optimal myopic portfolio policies with and without serial
correlation. Journal of Business, 44, 324- 334.
Hakansson, N. H. and W. T. Ziemba (1995). Capital growth theory. In R. A. Jarrow,
V. Maksimovic, and W. T. Ziemba (Eds.), Finance, Handbooks in OR fj MS, 65-86.
Amsterdam: North Holland.
Hausch, D. B. and W. T. Ziemba (1985). Transaction costs, extent of inefficiencies, entries
and multiple wagers in a racetrack betting model. Management Science, 31, 381-394.
Hausch, D. B. , W. T. Ziemba, and M. E. Rubinstein (1981). Efficiency of the market for
racetrack betting. Management Science, 27, 1435-1452.
Hens, T. and K. Schenk-Hoppe (2005). Evolutionary stability of portfolio rules in incomplete markets. J. of Mathematical Economics, 41, 43- 66.
Iyengar, G. N. and T. M. Cover (2000). Growth optimal investment in horse race markets
with costs. IEEE Transactions on Information Theory, 46(7) , 2675- 2683.
Jackson, D. and P. Waldron (2003). Parimutuel place betting in Great Britain and Ireland.
In L. V. Williams (Ed.) , The Economics of Gambling, 18- 29.
Kelly, Jr. , J. R. (1956). A new interpretation of the information rate. Bell System Technical
Journal, 35, 917- 926.
Latane, H. (1959). Criteria for choice among risky ventures. Journal of Political Economy,
67, 144- 155.
Latane, H. (1978). The geometric-mean principle revisited - a reply. Journal of Banking
and Finance, 2(4), 395- 398.
Lee, E. (2006). How to calculate the Kelly formula. www.fool.com. October 31.
Leland, H. (1968). Dynamic portfolio theory. PhD thesis, Economics Department, Harvard
University.
Long, Jr, J. B. (1990). The numeraire portfolio. Journal of Financial Economics, 26(1) ,
29- 69.
Luenberger, D. G. (1993). A preference foundation for log mean-variance criteria in portfolio choice problems. Journal of Economic Dynamics and Control, 17, 887- 906.
Lv, Y. and B. K. Meister (2009). Application of the Kelly criterion to Ornstein-Uhlenbeck
processes. Lecture Notes of the Institute for Computer Sciences, 4, 1051- 1062,
Springer.
MacLean, L. C., R. Sanegre, Y. Zhao, and W. T. Ziemba (2004). Capital growth with
security. Journal of Economic Dynamics and Control, 28(4) , 937- 954.
MacLean, L. C., E. O. Thorp, Y. Zhao, and W. T. Ziemba (2010). Medium term simulations of Kelly and fractional Kelly and proportional betting strategies.
MacLean, L. C. , E. O. Thorp, and W. T. Ziemba (2010). Good and bad properties of the
Kelly criterion.
MacLean, L. C., Y. Zhao, and W. T. Ziemba (2009). Optimal capital growth with convex
loss penalties. Working paper, Dalhousie University.
MacLean, L. c., W. T. Ziemba, and G. Blazenko (1992). Growth versus security in dynamic
investment analysis. Management Science, 38, 1562- 85.
3
--- page 865 ---

836
Bibliography
MacLean, L. C. , W. T. Ziemba, and Li (2005). Time to wealth goals in capital accumulation and the optimal trade-off of growth versus security. Quantitative Finance, 5(4),
343- 357.
Markowitz, H. M. (1976). Investment for the long run: New evidence for an old rule.
Journal of Finance, 31(5), 1273- 1286.
Mathis, C. and T. M. Cover (2005). A statistic for measuring the influence of side information in investment. Proceedings of the IEEE International Symposium on Information
Theory, 1156- 1157.
McEnally, R. W. (1986). Latane's bequest: The best of portfolio strategies. Journal of
Portfolio Management, 12(2), 21- 30.
Menger, K. (1967). The role of uncertainty in economics. In Essays in Mathematical Economics in Honor of Oskar Morgenstern. New Jersey: Princeton University Press.
Merton, R. C. (1969). Lifetime portfolio selection under uncertainty: The continuous time
case. Review of Economics and Statistics, 51, 247- 259.
Merton, R. C. (1973). An intertemporal capital asset pricing model. Econometrica, 41 ,
867- 887.
Merton, R. C. (1990). Continuous-Time Finance. Cambridge, MA: Blackwell Publishers.
Merton, R. C. and P. A. Samuelson (1974). Fallacy of the log-normal approximation to optimal portfolio decision-making over many periods. Journal of Financial Economics,
1, 67-94.
Mossin, J. (1968). Optimal multiperiod portfolio policies. Journal of Business, 41, 215- 229.
Mulvey, J. M., M. Bilgili, and T. M. Vural (2010) . A dynamic portfolio of investment
strategies: Applying capital growth with drawdown penalties.
Ordentlich, E. and T. M. Cover (1998). The cost of achieving the best portfolio in hindsight.
Mathematics of Operations Research, 23(4),960- 982.
Osorio, R. (2008). A prospect theory approach to the Kelly criterion for fat-tail portfolios:
The case of the Student t-Distribution. Evnine and Associates Report.
Phelps, E. S. (1962). The accumulation of risky capital: A sequential utility analysis.
Econometrica, 30, 729-743.
Platen, E. (2010). A benchmark approach to investing and pricing.
Poundstone, W. (2005). Fortune's Formula: The Untold Story of the Scientific System
that Beat the Casinos and Wall Street. New York: Hill and Wang.
Pulley, L. B. (1983). Mean-variance approximation to expected logarithmic utility. Operations Research, 31, 685- 697.
Ramsey, F. P. (1928). A mathematical theory of saving. Economic Journal, 38, 543-559.
Roll, R. (1973). Evidence on the growth optimum model. The Journal of Finance, 28(3),
551-566.
Rotando, L. M. and E. Thorp (1992). The Kelly criterion and the stock market. The
American Mathematical Monthly, 99(10) , 922- 931.
Rubinstein, M. (1976). The strong case for the generalized logarithmic utility model as
the premier model of nancial markets. Journal of Finance, 31(2), 551-571.
Rubinstein, M. (1991). Continuously rebalanced portfolio strategies. Journal of Portfolio
Management, 18(1), 78-81.
Rudolf, M. and W. T. Ziemba (2004). Intertemporal surplus management. Journal of
Economic Dynamics and Control, 28, 975- 990.
Samuelson, P. A. (1969). Lifetime portfolio selection by dynamic stochastic programming.
Review of Economics and Statistics, 51, 239-246.
Samuelson, P. A. (1971). The "fallacy" of maximizing the geometric mean in long sequences
of investing or gambling. Proceedings National Academy of Science, 68, 2493- 2496.
4
--- page 866 ---

Bibliography
837
Samuelson, P. A. (1977). St. Petersburg paradoxes: Defanged, dissected and historically
described. Journal of Economic Literature, 15(1), 24-55.
Samuelson, P. A. (1979). Why we should not make mean log of wealth big though years
to act are long. Journal of Banking and Finance, 3, 305- 307.
Samuelson, P. A. (1991). Long-run risk tolerance when equity returns are mean regressing:
Pseudoparadoxes and vindication of business mens risk. In W. C. Brainard, W. D.
Nordhaus, and H. W. Watts (Eds.), Money, Macroeconomics and Economic Policy,
181-200. Cambridge, MA: MIT Press.
Stutzer, M. (2003). Portfolio choice with endogenous utility: A large deviations approach.
Journal of Econometrics, 116, 365- 386.
Stutzer, M. (2004). Asset allocation without unobservable parameters. Financial Analysts
Journal, 60(5), 38- 51.
Stutzer, M. (2010). On growth optimality security against underperformance.
Thorp, E. O. (1966). A favorable side bet in Nevada Baccarat.
Thorp, E. O. (1969). Optimal gambling systems for favorable games. Review of the International Statistical Institute, 37(3), 273- 293.
Thorp, E. O. (1971). Portfolio choice and the Kelly criterion. Proceedings of the Business
and Economics Section of the American Statistical Association, 215- 224.
Thorp, E. O. (2006). The Kelly criterion in blackjack sports betting and the stock market. In S. A. Zenios and W. T. Ziemba (Eds.), Handbook of Asset and Liability
Management, Volume 1, 387- 428. Amsterdam: North Holland.
Thorp, E. O. (2008) . Understanding the Kelly criterion. Wilmott, May and September.
Thorp, E. O. and R. Whitley (1972). Concave utilities are distinguished by their optimal
strategies. Colloquia Mathematica Societatis Janos Bolyai, 813- 830.
Wilcox, J. (2003a). Harry Markowitz and the discretionary wealth hypothesis. Journal of
Portfolio Management, 29 (Spring) , 58- 65.
Wilcox, J. (2003b). Risk management: Survival of the fittest. Wilcox Investment Inc.
Wilcox, J. (2005). A better paradigm for finance. Finance Letters, 3(1), 5- 11.
Williams, J. B. (1936). Speculation and the carryover. Quarterly Journal of Economics,
50(3), 436- 455.
Ziemba, R. E. S. and W. T. Ziemba (2007). Scenarios for Risk Management and Global
Investment Strategies. New York: Wiley.
Ziemba, W. T. (2005). The symmetric downside risk Sharpe ratio and the evaluation of
great investors and speculators. Journal of Portfolio Management Fall, 108- 122.
Ziemba, W. T. and D. B. Hausch (1984) . Beat the Racetrack. Harcourt, Brace and
Jovanovich.
Ziemba, W. T. and D. B. Hausch (1986). Betting at the Racetrack. Dr. Z Investments.
Ziemba, W. T. and D. B. Hausch (1987). Dr. Z 's Beat the Racetrack. Dr. Z Investments.
Ziemba, W. T. and D. B. Hausch (2008) . The Dr. Z betting system in England. In Efficiency
of Racetrack Betting Markets, 567- 574. Singapore: World Scientific.
Ziemba, W. T. and R. G. Vickson (2010). Models of optimal capital accumulation and
portfolio selection.
5
--- page 867 ---

This page is intentionally left blank
--- page 868 ---

839
Author Index
A
Aase, K. 5
Abbott, D. 450,453
Adler and Dumas 755, 767
Alais, M. 23
A1chian, M. 274
Algoet and Cover 143,145,157,281,
428,623
Ali, M. 666
Amir, R. 274
Arrow, KJ. 23,119,183,474
Arrow-Pratt 7,249
Artzner, P. 265
Aurell, E.R. 428
B
Baesel, 1. 824
Barron, A. 155, 156
Barron and Cover 153
Baumol, W.l. 3,11
Bell and Cover 4, 143, 144, 148,568,
582
Bellman, R. 49,60, 111, 146
Bellman and Kalaba 6, 38, 74, 80, 89
Benter, W. 776, 783
Bernoulli, D. 3, 12,38, 81, 500, 791
Bernoulli, N. 19,578
Bicksler and Thorp 248,463, 543,
555
Bicksler, 1. 89
Bielecki and Pliska 386,387,407
Black,F. 758,767
Black and Perold 308, 309, 374
Blackwell, D. 51,60, 183,209
Blume and Easley 275
Breiman, L. 6,47, 74, 75, 78, 236,
247,281,428,497,480,578,
791
Breitmeyer, C. 266, 359
Brown, G 99
Browne, S. 301, 303, 305, 373, 384,
428,620,623,649,791,795,796,
799,824
Bucklew, 1. 631,643
Buffett, W. 9, 11,510,511,515,566,
769,771,776,8l7
Burkhardt, T. 260
C
Campbell, 1. 262
Carino and Ziemba 271,369,756
Chopra, V.K. 249
Chopra and Ziemba 8,9, 145,249,
369,370,563,565, 776,778
Clark, D. 817
Clark, R. 593
Clark and Ziemba 353, 593, 595
Constantinides, G.c. 409,419,425,
754, 767
Cootner, P. 90
Cover and Thomas 4, 144, 566, 623,
642
Cover, T. 181,428,520
Cox and Leland
Cox and Miller 818
Culioli,l. 365
D
Davis and Lleo 303, 385, 386
Dempster, M.A.H. 331, 427
--- page 869 ---

840
Dempster, Evstigneev and Schenk-
Hoppe 427
Dexter, Yu and Ziemba 251, 257
Dixit and Pindyck 757, 767
Dreze, J. 91
Dubins and Savage 48, 60, 80, 316,
319
Durham, S. 246
Dybvig, P. 469
E
Emory 511
Epstein, RA. 65,301
Esscher 622, 636, 638
Estes, B.S. 77
Ethier, S. 335, 515,518
Evstigneev, LV. 284
Evstigneev, Hens and Schenk-Hoppe
273,454
Ezroy, D. 758, 767
F
Fama, E.F. 629, 680, 682
Farmer and Lo 284
Feller, W. 80, 301 , 338, 791, 792
Ferguson, T.S. 6, 80, 301,331 , 353
Fernholz, E.R 448
Finkelstein, M. 236
Finkelstein and Whitley 145, 209,235,
356
Fisher, I. 91, 587
Freund, RJ. 45.257
Friedman and Savage 23, 44, 539
G
Gauss, K.F. 67
Geyer and Ziemba 145, 462, 512,523,
780
Goetzmann, W. 782
Gottlieb, G. 346, 593, 595, 657
Grauer, R 249,591,592,595
Grauer and Hakansson 369, 703, 704
Griffin, P. 803, 808, 824
Grinold and Kahn 373,403, 407
Author Index
Gross, B. 373,515,516,657
Grossman and Zhou 360
H
Hagstrom 817
Hakansson and Liu 125, 126, 134
Hakansson and Ziemba 281,284,356,
575,577,579,595,622,627,642
Hakansson, N.H. 7,8,80,81,86,89,
91,113,125,133, 414,473, 475-
479,483,484,491,578,586,595
Harville, D.A. 667, 682
Hausch and Ziemba 346,347,351,
463,543,544,567,593, 595,598,
622,658, 659, 664,667, 677, 681,
683,691, 692,694-702,775
Hausch, Lo and Ziemba 695, 783
Hausch, Ziemba and Rubinstein 657,
663
Hecht, R. 799
Hensel and Ziemba 775, 783
Hodges, S.D. 782
Hume, D. 64
J
Jorion, P. 26~356 , 359 , 591,596
K
Kabanov and Stricker 438
Kallberg and Ziemba 145, 249, 250,
254,257,428,462,563, 592, 597,
672, 677, 684
Karlin and Taylor 266
Kassouf, S. 90,822
Kelly, J. 5, 25,49, 236,281,331,334,
428, 471 , 578,792
Keynes, J.M. 567
Kilpatrick, A. 817
Kritzman, M. 812
Kitamura, Y. 638, 645
L
Latane, H.A. 5, 8,35,82,461,471,
481, 484, 578
--- page 870 ---

Author Index
Lawley and Maxwell 263
Leib, J. 512,802
Leland, H.E. 113,586,597, 782
Leland and Mossin 8
Lensberg, T. 282
Levhari and Srinivasan 470
Levy and Markowitz 593
Li, Y. 590, 597
Lintner, J. 9, 125, 134
Lowenstein, R
817
Luenberger, D. 428,448,460, 575,
599
Lv and Meister 146,285
M
MacLean and Weldon 263
MacLean and Ziemba 260,271,566,
578,597,641,648
MacLean, Sanegre, Zhao and Ziemba
302,356,741,750
MacLean, Thorp and Ziemba 463,
563,576,741,750
MacLean, Thorp, Zhao and Ziemba
463, 543,564
MacLean, Zhao and Ziemba 303, 453,
454
MacLean, Ziemba and Blazenko 8,
283301,331,428,512,566,641,
643,648
MacLean, Ziemba and Li 145,259,
519,566
Markowitz, H.M. 7,8,44,78,82,85,
125,143,249,257,461,481,484,
495,511,539,583,589,592,593,
597,791,823,494,516,703,811
Markowitz and Van Dijk 516
Marschak, J. 23,44,91
Marshall, A. 44, 278
McEnally, RW. 791
Menger, K. 3-5, 11,22,23
Merton, R.C.
262,309,310, 315, 326,
332,356,373,374,376,385,386,
392,414,426,480,481,590,597,
753, 767
841
Merton and Samuelson 209,455, 500
Mielke, A. 454
Milnor and Shapley 274
Modigliani and Brumberg 92
Montmart, P. 3, 19, 21
Mordin, N. 698, 702
Morgenstern, O. 89,90,222,520
Mossin and Samuelson
83
Mossin, J. 90, 113,209,525,586,597
Mulvey, J.M. 591, 597, 735
Mulvey, Bilgili and Vural 660, 735
N
Nassim, N. 512
Neave,E. 473,474,484,663
o
Ordentlich and Cover 144, 145,211
P
Pabrai, M. 509, 523
Pearson, K. 64
Phelps, E. 91,96, 111,455,468,473,
484
Platen, E. 303,409,410
Platen and Heath 409-412, 417, 418,
420,422,423,426
Pliska,S. 309
Poincare, H. 64
Poundstone, W. 509,518,523,543,
547,657
Proebsting, T. 521-523
Pye,G. 478,484,664
Q
Quaife, A. 811,817,820,821,824
R
Radner, R
273, 284, 436
Rabin, M. 648
Ramsey, F.P. 455, 473, 484
Reid, R
824
Richard, S. 755, 768
Rockafeller and Uryasev 260,271
--- page 871 ---

842
Rockafeller and Ziemba 271
Roll, R. 7,8-10,125,133, 143,4l7,
481,484,598
Ross,S.A.
409,426, 586,587,598
Rotando, L.M. 598, 795
Roy, A.D. 45, 125
Rubinstein, M. 356, 372, 680
Rudolf and Ziemba 303,455, 660, 753
S
Samuelson, P.A. 5,23,82,83, 140,
148,209,453,455,460,465,466,
473-475, 484,487,488,491-493,
496,518,520,525,578,598,648,
753
Santa Fe Institute 274
Savage, L. J. 42-44
Schenk-Hoppe, K. 427
Schlesinger, D. 818,824
Shannon,C. 5,25,38, 39,428,509,
791
Shapley, L. 274
Sharpe and Tint 756, 768
Sharpe, W.P. 9, 125, l34, 373, 374,
428, 756
Shay,B. 448
Shubik and Whitt 274
Siegel, J. 555
Siegel, L. 407,781
Simons, J. 515,785, 787
Snyder, A. 804
Sommer, L.
3, 11
Soros, G. 769, 771
Spurgin, R.B. 782, 784
Stigler, G. 43
Stutzer, M. 575, 619,627,641, 648
Swensen, D. 736
T
Taleb, N. 512, 523
Author Index
Thorp and Kassouf 86, 795
Thorp and Whitley 248,462, 464,525,
519,539
Thorp, E.O.
6-8,61, 71, 81, 83, 143,
281,331,347,385,426,428,461,
463,480,481,484,509,521-523,
576,598,623,641,657,661,662,
789,791,800,811
Tucker, H. 796
V
von Neumann J. 520
von Neumann and Morgenstern 40, III
W
Wald, A. 51
Walden, L. 795
Weitzman, M. 666, 680
Whitley, R. 236
Williams, J.B. 147, 152,471,575,578
Wong, S. 795, 803,804
y
Yamashita, W.
804
Young and Trent 496
Z
Zabel, E. 473
Zenios and Ziemba 738
Ziemba and Hausch 547,590,777
Ziemba and Mulvey 428,589,591,
738, 754, 768
Ziemba and Vickson 249,257, 473,
475,476, 485, 509, 511, 512, 583,
598,671, 675, 683,685
Ziemba, R. 511
Ziemba, W.T. 259, 351,385,431, 455,
462, 485,481, 511, 565, 594,661,
769, 785
Ziemba and Ziemba 566, 785
--- page 872 ---

843
Subject Index
A
Acceptable set 360, 265
Action 824
Active portfolio management 373,
427
Actuarial pricing formula 419
Admissible strategy 277, 517
AEP 160
Alpha-omega targets 403
Alternate wealth sequences 500
American Express 511
Analysis of variance 128
Approximate form of transitivity 83
Arbitrage 809
Arbitrage and growth 429
Arbitrarily small bets are allowed 521
Arithmetic mean 40
Arithmetic mean rate return 569
Arithmetic MV 7
Asset market equilibrium 277
Asset market with stationary returns
435,442
Associates First Capital Corporation
814
Asymptotic equipartition property 171
Asymptotic growth 8, 108
Magnitude 54, 236
Time 50
Asymptotic optimality principle 168,
499, 794
Asymptotically best 48
AT&T 809
Augmented filtration 358
A vailable strategies 35
Avalanche Effect 128
B
Baccarat 63
Backward elimination 364
Balanced growth path 279,434
Balancing of measures 333
Bankruptcy 47,556
Basic investment problem 332
strategies 62, 276
Basic validity test 128
Bayes estimation 262, 324
empirical Bayes 262
Theorem 262, 369
Beat the dealer 509,515,516,791
Behavior of capital 108
Bellman backward induction 84,476
Benchmark 303, 373-379, 382, 384,
386
management 385
approach 409
dynamic 395
with alpha target 400
mutual fund theorem 397
Berkshire Hathaway 771,817,820
Bernoulli trials 5, 71, 72, 83
Bernoulli's logarithmitic function 470
Best portfolio in hindsight 211
Betting system in England 695
Betting your beliefs 281
Binary channel 26
Binary digital option 795
Binomial lattice price 226
Biotime 819
Black Swan 278,446,461
Blackjack 61, 344,461,515, 801,803,
816
--- page 873 ---

844
Blackjack forum 512,802
Black-Scholes 229
Bold play 316,319,323
Bookmakers 697
Borrowing 106
and lending 91
and solvency 115
limits 117
Boundedness 98
Breakage 690,691
Broker's call 814
Brownian motion 261,263
with drift 817
Buffett thinks like a Kelly investor 510
lunch 77
Businessman's risk 471
Buy low - sell high 438,477
Buy-and-hold strategy 428
C
Calculus of variations 466
Capital 521
Accumulation 259
Asset pricing model 8, 570
Growth 92, 331
Growth Theory 577
Market equilibrium 125
Position 105
Casestudy 819
Cash equivalent value 251,255,563
Casino betting 817
Cauchy equations 96
Central limit theorem 59, 109,488
Certain return 56
Chance events 28
Chemin de Fer 63
Classical gambler 33
Co-existence of portfolio rules 282
Coin tossing 792
Commodity futures 795
trading 593
Common factors 261
Communication channel 25
theory 25
Subject Index
Competitive optimality 147,463,567
Complete ruin 125
Completely mixed strategy 435
Compound growth 516
mean-variance efficient frontier
516,519
Computation of performance measures
336
Concavity 16
Conditional expected log return 158
Conditional Value-at-Risk, CVaR 260,
302
Conservative lower bound estimate 512
Constant proportions 316, 326, 374,
376
benchmark 398
portfolio 305
portfolio insurance (CPPI) 301,
305,310,325,326,331
strategy 428,435,443
Constant rebalanced portfolio 181
Constant returns to scale 8
Consumption hypothesis 92
Contingent claim 419
Continuous approximation 800,810
Continuous time portfolio theory 704
Continuous-time Kelly criterion 324,
325
Convertible hedge 86
security 67
Convex combinations 335
cost function 568
risk measure 369
shortfall penalty 303
Correction fund 391,397
Cost function 26
Coupled entries 687, 688
Cramer's Theorem (Bucklew) 629
Crash of October, 1987 817
Cross-sectional regression 135
Cross-sectional spread 136
Cumulative effects 37
Currency hedge portfolio 764
Currency markets 439
--- page 874 ---

Subject Index
D
Daily double bets 666
Darwinian theory of portfolio selection
274
Death constant 77, 89
Decay rate maximizing portfolios 627,
636
Derivative of expected growth 413
Derivative security 226
Description length 156
Difference equation 94
Dirichlet problem 309,311,313,319,
322,377,378,380,381
Discreteness of money 71
Discrimination statistic 645
Disjunctive problem 361
Distribution of returns 107
Distribution-free 212
Diversification 42, 721
theorem 423
portfolio 127,423
Doubling before halving 333
Doubling rate 153
for side information 153
Downside focus 265
Downside risk control 358
measure 260, 265, 356, 358
Sharpe ratio 782
Drawdown 359,376,511
Dynamic estimation 261
investment process 261
reallocation 812
Dynamic programming 49, 84,476,
496
Dynamic stochastic programming 465
E
E.L. Bruce short squeeze 795
Economic decision making 39
Edge/ Odds 5
Effective tradeoff 302, 335
Efficient frontier 334, 516
Efficient markets 665,693
Efficient portfolio 42, 44
845
Equilibrium conditions 134
Equity market returns 555
Equivalence classes of functions 539
Equivalent strategy 247
Ergodic 157
Mode 174
Errors in estimates 249,261
in means 255
in variances/covariances 250,
255
Esscher transformation 622, 636, 638
Essentially different strategy 6,81,
461,569,794,512
Evolutionary asset market model 275
dynamics 274, 278
finance 273
stability 281, 282
Excess risk adjusted returns 721
Expected average compound growth
489
growth rate of capital 123
loss 16
return on place bet 685
return ratio 139
time to goal 6,259,303,567,
800,827
utility 36, 501
utility counterexample 569
utility maximizer 487,496
value 27
wealth ratio 268, 568
Exponential dominance 209
gain 32
growth rate 27,73,77,236,433
440
Extinction 280
Extremal strategy 219
F
Factors 388
False corollary 82
Favorable investments 260,332
Favorable outcome 17
Favorableness 106
--- page 875 ---

846
Filtration 260
Financial engineering 438
Financial intermediation 361
Financial value of information 153
Finite goals 56
Finite yield assumption 120
First passage time 265, 333
First-order conditions 127
Fixed fraction strategy 48, 235, 238,
278,333,792
Fixed rebalance times 264
Fixed-mix investment strategies 282,
427,438
in currency markets 440
Fixed-weight portfolios 710
Flexibility condition 342
Flexible process 341
Ford Foundation 769, 771
Foreign currencies 761, 762
Fortune's formula 461,509,518,543
Four fund separation theorem 758, 764
Fractional Kelly strategies 283, 269,
301,331,335,390,397,517,565,
593,815,821
versus Kelly 813
Fractionalobjective 374
Fund separation theorem 398, 399
Fundamental problem 267, 365
Funding ratio 760, 763, 764
G
Gambler 26
Gambler's fallacy 442
ruin 71,792
capital 27
liability 237
Games
absolutely fair 16
fair 42,418
favourable 6,47,240
dynamic 276, 278
identically distributed independent
801
asset market 280, 283
Subject Index
alternate sequence 497
competitive investment 150
of survival 274
repeated 91
sequence 181
stochastic dynamic 264
two-person zero-sum 61,807
Gamma function 224
Gartner-Ellis Theorem 621, 643
GEICO 511
Generalized concavity 683
Generic programming 283
Geometric Brownian motion 305,309,
324,327,377,379,380,382
random walk 443
Wiener process 213
Geometric mean 38,40,358,471
Geometric mean fallacy 487
Geometric MV 7
Goal utility 48
Good and bad properties of Kelly 459,
563,566,568
Growth - security 8,331,355,578,589
profile 333
strategy 265, 268
tradeoffs 592
monotonicity 302
Growth and decay 555
Growth condition 263
Growth in stationary markets 428,429,
431
Growth measures 301,331
Growth optimality 413
optimal portfolio 414
model 4,125,130,265
Growth rate 157,436
of balanced strategies 436
of constant proportions strategies
444
of wealth 435
Growth under transaction costs 450
Growth-optimum theory 126
strategy 324
never risks ruin 582
